import asyncio
import json
import re
import time
import pandas as pd
from tqdm import tqdm
from playwright.async_api import async_playwright
import anthropic

PAGES_TO_SCRAPE = [
    "",           # Homepage
    "/about",
    "/about-us",
    "/products",
    "/services",
    "/leadership",
    "/team",
    "/management",
    "/news",
    "/press",
    "/media",
    "/careers",
    "/jobs",
    "/certifications",
    "/quality",
    "/contact",
]

MAX_TOKENS_PER_COMPANY = 8000   
RATE_LIMIT_DELAY = 2.0          
MAX_WORKERS = 4                 
HAIKU_MODEL = "claude-haiku-4-5-20251001"
SONNET_MODEL = "claude-sonnet-4-6"
BORDERLINE_LOWER = 40
BORDERLINE_UPPER = 60

async def scrape_company(browser, url_base: str) -> str:
    """Scrape multiple pages of a company website and return concatenated text."""
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    all_text = []

    for path in PAGES_TO_SCRAPE:
        url = url_base.rstrip("/") + path
        try:
            page = await context.new_page()
            await page.goto(url, timeout=10000, wait_until="domcontentloaded")
            await asyncio.sleep(RATE_LIMIT_DELAY)
            text = await page.evaluate("""
                () => {
                    const elements = document.querySelectorAll(
                        'p, h1, h2, h3, h4, li, td, th, span.content, div.about, div.description'
                    );
                    return Array.from(elements)
                        .map(el => el.innerText.trim())
                        .filter(t => t.length > 20)
                        .join(' | ');
                }
            """)
            if text:
                all_text.append(f"[PAGE: {path or 'HOME'}]\n{text[:2000]}")
            await page.close()

        except Exception as e:
            pass

    await context.close()

    combined = "\n\n".join(all_text)
    return combined[:MAX_TOKENS_PER_COMPANY * 4]

SCORING_SYSTEM_PROMPT = """You are a business analyst scoring Indian manufacturing companies
against an Ideal Customer Profile (ICP) for a B2B consulting firm.

ICP: Indian specialty manufacturer, Rs.50Cr–Rs.500Cr revenue, promoter-driven (not PE/VC controlled),
makes a PHYSICAL DIFFERENTIATED PRODUCT (not services), technical decision-maker (PhD/IIT/IISc/BITS/
ex-ISRO/DRDO), active growth signals.

AUTO-DISQUALIFY conditions (set auto_disqualify: true):
- Company sells services (testing, CRO, analytical services, contract research) — NOT physical products
- Revenue evidence suggests >Rs.500Cr
- Company is a subsidiary of a large group (Tata, Reliance, L&T divisions)
- PE/VC firm holds majority stake
- No meaningful product information on website (single-page placeholder)
- Company is a trader, distributor, or importer — not a manufacturer

SCORING RULES:
- C3 STRONG requires: patents, DSIR recognition, USFDA/EU-GMP approval, "first/only/pioneer in India",
  proprietary branded products. ISO 9001 ALONE IS NOT A DIFFERENTIATOR — score Weak.
- C4 STRONG requires: PhD, IIT/IISc/BITS/NIT alumni, ex-ISRO/DRDO/CSIR, scientific publications.
  A generic "B.Tech" or "MBA" without elite institution = Moderate at best.
- C6: count ONLY signals from 2023 onwards. News from 2019–2022 does NOT count.
- If NONE of the C6 signals (hiring/facility/certification/website activity/financial growth)
  are from 2023 onwards, score C6 Weak.

SCORING WEIGHTS:
C1 Manufacturer: 10 pts (Weak=0, Moderate=5, Strong=10)
C2 India-based: 5 pts (Weak=0, Moderate=2.5, Strong=5)
C3 Differentiated: 25 pts (Weak=0, Moderate=12.5, Strong=25)
C4 Technical DM: 20 pts (Weak=0, Moderate=10, Strong=20)
C5 Growing sector: 20 pts (Weak=0, Moderate=10, Strong=20)
C6 Growth signals: 20 pts (Weak=0, Moderate=10, Strong=20)

Return ONLY a valid JSON object. No preamble. No explanation outside JSON."""

SCORING_USER_TEMPLATE = """Score this company against the ICP criteria.

Company website text:
---
{website_text}
---

Return ONLY this JSON (no other text):
{{
  "C1_manufacturer": {{"score": "Strong/Moderate/Weak", "evidence": "exact quote from text", "confidence": "high/medium/low"}},
  "C2_india_based": {{"score": "Strong/Moderate/Weak", "evidence": "exact quote from text", "confidence": "high/medium/low"}},
  "C3_differentiated": {{"score": "Strong/Moderate/Weak", "evidence": "exact quote from text", "confidence": "high/medium/low"}},
  "C4_technical_dm": {{"score": "Strong/Moderate/Weak", "evidence": "exact quote from text", "confidence": "high/medium/low"}},
  "C5_growing_sector": {{"score": "Strong/Moderate/Weak", "evidence": "exact quote from text", "confidence": "high/medium/low"}},
  "C6_growth_signals": {{"score": "Strong/Moderate/Weak", "evidence": "exact quote from text", "confidence": "high/medium/low"}},
  "auto_disqualify": false,
  "disqualify_reason": "",
  "federer_score": 0,
  "verdict": "strong_pass/pass/borderline/fail",
  "low_confidence_flags": ["list any criteria where confidence is low"]
}}"""


def score_weights(score_str: str, weight: int) -> float:
    mapping = {"Strong": weight, "Moderate": weight / 2, "Weak": 0}
    return mapping.get(score_str, 0)


def compute_federer_score(result: dict) -> int:
    weights = {
        "C1_manufacturer": 10,
        "C2_india_based": 5,
        "C3_differentiated": 25,
        "C4_technical_dm": 20,
        "C5_growing_sector": 20,
        "C6_growth_signals": 20,
    }
    total = 0
    for criterion, weight in weights.items():
        if criterion in result:
            total += score_weights(result[criterion].get("score", "Weak"), weight)
    return int(total)


def call_claude(website_text: str, model: str, client: anthropic.Anthropic) -> dict:
    """Call Claude API for ICP scoring. Returns parsed JSON or empty dict on failure."""
    try:
        response = client.messages.create(
            model=model,
            max_tokens=1000,
            system=SCORING_SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": SCORING_USER_TEMPLATE.format(website_text=website_text[:20000]),
                }
            ],
        )
        raw_text = response.content[0].text.strip()
        
        raw_text = re.sub(r"```json|```", "", raw_text).strip()
        result = json.loads(raw_text)
        
        if result.get("federer_score", 0) == 0 and not result.get("auto_disqualify"):
            result["federer_score"] = compute_federer_score(result)
        return result
    except Exception as e:
        return {"error": str(e), "auto_disqualify": False, "federer_score": 0, "verdict": "error"}


AUTO_QA_RULES = [
    
    (
        "iso_only_c3",
        lambda r: (
            r.get("C3_differentiated", {}).get("score") in ("Moderate", "Strong")
            and "iso 9001" in r.get("C3_differentiated", {}).get("evidence", "").lower()
            and "dsir" not in r.get("C3_differentiated", {}).get("evidence", "").lower()
            and "fda" not in r.get("C3_differentiated", {}).get("evidence", "").lower()
            and "patent" not in r.get("C3_differentiated", {}).get("evidence", "").lower()
        ),
    ),
    (
        "stale_c6_evidence",
        lambda r: (
            r.get("C6_growth_signals", {}).get("score") in ("Moderate", "Strong")
            and any(
                yr in r.get("C6_growth_signals", {}).get("evidence", "")
                for yr in ["2019", "2020", "2021", "2022"]
            )
            and not any(
                yr in r.get("C6_growth_signals", {}).get("evidence", "")
                for yr in ["2023", "2024", "2025", "2026"]
            )
        ),
    ),
    (
        "low_confidence_c4",
        lambda r: "C4_technical_dm" in r.get("low_confidence_flags", []),
    ),
    (
        "borderline_score",
        lambda r: BORDERLINE_LOWER <= r.get("federer_score", 0) <= BORDERLINE_UPPER,
    ),
    (
        "cro_language",
        lambda r: any(
            kw in r.get("C1_manufacturer", {}).get("evidence", "").lower()
            for kw in ["cro", "testing service", "analytical service", "contract research"]
        ),
    ),
]


def apply_auto_qa(result: dict) -> list:
    """Return list of flag names triggered for this result."""
    flags = []
    for flag_name, condition in AUTO_QA_RULES:
        try:
            if condition(result):
                flags.append(flag_name)
        except Exception:
            pass
    return flags

async def process_company(browser, company: dict, client: anthropic.Anthropic) -> dict:
    """Scrape + score one company. Returns enriched company dict."""
    website = company.get("website", "")
    if not website.startswith("http"):
        website = "https://" + website

    try:
        website_text = await scrape_company(browser, website)
    except Exception as e:
        website_text = ""
        company["scrape_error"] = str(e)

    if not website_text:
        company["verdict"] = "fail_no_website_content"
        company["federer_score"] = 0
        return company

    result = call_claude(website_text, HAIKU_MODEL, client)
    company.update(result)
    company["model_used"] = HAIKU_MODEL

    score = result.get("federer_score", 0)
    if BORDERLINE_LOWER <= score <= BORDERLINE_UPPER and not result.get("auto_disqualify"):
        sonnet_result = call_claude(website_text, SONNET_MODEL, client)
        company.update(sonnet_result)
        company["model_used"] = SONNET_MODEL

    company["qa_flags"] = apply_auto_qa(company)
    company["needs_human_qa"] = bool(company["qa_flags"])

    return company


async def run_pipeline(input_csv: str, output_csv: str):
    """Main async pipeline runner."""
    df = pd.read_csv(input_csv)
    companies = df.to_dict("records")

    client = anthropic.Anthropic()  #
    results = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        semaphore = asyncio.Semaphore(MAX_WORKERS)

        async def process_with_semaphore(company):
            async with semaphore:
                return await process_company(browser, company, client)

        tasks = [process_with_semaphore(c) for c in companies]
        for coro in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Scoring companies"):
            result = await coro
            results.append(result)

        await browser.close()

    results_df = pd.DataFrame(results)
    results_df.to_csv(output_csv, index=False)
    print(f"\n Pipeline complete. {len(results_df)} companies scored.")
    print(f"   Strong pass (80+): {len(results_df[results_df['federer_score'] >= 80])}")
    print(f"   Pass (60–79):      {len(results_df[(results_df['federer_score'] >= 60) & (results_df['federer_score'] < 80)])}")
    print(f"   Borderline (40–59): {len(results_df[(results_df['federer_score'] >= 40) & (results_df['federer_score'] < 60)])}")
    print(f"   Fail (<40 or disqualified): {len(results_df[results_df['federer_score'] < 40])}")
    print(f"   Needs human QA: {results_df['needs_human_qa'].sum()}")
    print(f"\nResults saved to: {output_csv}")


def deduplicate_companies(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate companies by fuzzy name matching + CIN matching."""
    from fuzzywuzzy import fuzz

    if "cin" in df.columns:
        df = df.drop_duplicates(subset=["cin"], keep="first")

    names = df["company_name"].str.lower().str.strip().tolist()
    to_drop = set()
    for i in range(len(names)):
        if i in to_drop:
            continue
        for j in range(i + 1, len(names)):
            if j in to_drop:
                continue
            if fuzz.token_sort_ratio(names[i], names[j]) >= 90:
                to_drop.add(j)

    df = df.drop(df.index[list(to_drop)])
    print(f"Deduplication: removed {len(to_drop)} duplicates. {len(df)} unique companies remain.")
    return df.reset_index(drop=True)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python pipeline.py <input_companies.csv> <output_scored.csv>")
        print("\nInput CSV must have at minimum: company_name, website columns")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    asyncio.run(run_pipeline(input_file, output_file))
