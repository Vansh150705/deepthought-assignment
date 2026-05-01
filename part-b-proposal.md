# Proposal: 1000 ICP-Qualified Companies in One Month
## Part B — Sourcing Strategy + Scale-Up Proposal
### DeepThought Business Analytics Internship | Chennai + Specialty Biotech / Diagnostics Segment

---

## Part B — Question 1: Sourcing Methods

**How would I find Federer-profile companies at scale across India?**

The methods below are specific to the Specialty Biotech + Diagnostics ICP. Each is evaluated for why it works for *this* ICP, not generically.

---

### Method 1: DSIR Recognized R&D Units List (dsir.gov.in)

**What it is:** The Department of Scientific and Industrial Research maintains a publicly downloadable list of Indian companies whose in-house R&D units are formally recognized. As of 2024, there are 1,500+ companies on this list.

**Why it works for this ICP specifically:**
- DSIR recognition is a direct proxy for C3 (differentiation) — you cannot get DSIR recognition without demonstrating genuine R&D investment, personnel, and equipment.
- It simultaneously signals C1 (the company is a manufacturer — DSIR doesn't recognize CRO service labs in the same way) and C4 (someone in leadership is technical enough to manage a recognized R&D unit).
- For diagnostics and biotech, most DSIR-recognized companies are specialty manufacturers, not commodity producers.

**How to use it:** Download the Excel from dsir.gov.in. Filter by state (Tamil Nadu, Maharashtra, Gujarat, Karnataka, Telangana — our target states). Filter by industry category (pharmaceuticals, biotechnology, chemicals). Cross-match with company name Google search to find websites. Exclude companies without websites immediately.

**Expected yield:** ~400–600 relevant companies after filtering to target states and segments. ~30–35% will pass full ICP screening.

**Limitation:** Skews toward older, established companies (DSIR recognition takes time). Misses newer biotech companies founded after 2020 that haven't yet applied. Also doesn't give revenue data — need to cross-reference with MCA/Tofler.

---

### Method 2: Regulatory Approval Lists — CDSCO, USFDA, WHO-GMP

**What it is:**
- CDSCO (Central Drugs Standard Control Organisation) maintains a list of licensed manufacturers of drugs and medical devices in India.
- USFDA maintains a public list of approved manufacturing facilities in India.
- WHO-GMP prequalification list is publicly available.

**Why it works for this ICP specifically:**
- Regulatory approvals are the hardest-to-fake signal of C3 (differentiation) and C1 (manufacturer). A USFDA-approved facility cannot be a CRO or trading company — it must be a genuine manufacturing site.
- CDSCO manufacturing licenses specifically cover diagnostic kits and biologics — exactly our target segment.
- WHO-GMP prequalification is rare (only ~40–50 Indian companies) and identifies the most differentiated players.

**How to use it:** CDSCO data is downloadable as a state-wise list of licensed manufacturers. Filter by product category (diagnostics, biologics, biopharma). USFDA data is searchable at fda.gov/inspections-compliance-enforcement-and-criminal-investigations/compliance-actions-and-activities/warning-letters — more useful for identifying *who has been approved*, not who has been warned.

**Expected yield:** CDSCO list: ~800–1000 diagnostic/biotech manufacturers. USFDA India facilities: ~300 relevant after filtering to MSME segment (below Rs.500Cr). WHO-GMP: ~40–50. Overlap between lists is significant — deduplicate.

**Limitation:** Heavy pharma bias. Medical device and IVD companies are less well-represented in USFDA lists. WHO-GMP is rare and slow to update.

---

### Method 3: Industry Expo Exhibitor Directories

**Target expos:**
- **BioAsia (Hyderabad):** Premier Indian biotech expo. 500+ exhibitors annually. Exhibitor list published on bioasia.in.
- **CPHI India (Mumbai):** Pharma and biotech ingredients. 700+ exhibitors. CPhI exhibitor directory is downloadable.
- **Medicall (Chennai):** Medical devices and diagnostics focused on South India. Strong IVD presence.
- **India Lab Expo (Mumbai/Delhi):** Lab instrumentation — catches diagnostic tool manufacturers.
- **Bio Innovation Forum (multiple cities):** ABLE (Association of Biotech-Led Enterprises) events.

**Why it works for this ICP specifically:**
- Self-selection: a company that pays Rs.2–10L for an exhibition booth is spending money to grow — C6 (growth signal: active expansion intent) is almost guaranteed.
- Expo segmentation maps directly to our industry baskets — BioAsia exhibitors are by definition in biotech, not commodity manufacturing.
- Exhibitor profiles often include product descriptions, certifications, and contact information — reduces research time per company.

**How to use it:** Most expos publish exhibitor directories online (website, PDF, or app). Historical exhibitor lists (2022–2024) are often still accessible. Scrape or manually extract: company name, website, segment tag. For past expos, use Wayback Machine for archived exhibitor pages.

**Expected yield:** 600–800 unique companies across 5 expos (after deduplication). ~25–30% ICP pass rate (expos attract some distributors and service companies too).

**Limitation:** Expo participation is self-selected toward companies that can afford booths (typically Rs.50Cr+). Misses bootstrap-funded smaller MSMEs. Strong Hyderabad, Mumbai, and Delhi bias — Chennai companies underrepresented.

---

### Method 4: Ministry of Commerce — Export Data (DGFT / Zauba / Volza)

**What it is:** India's export data (shipping bills) is partially public via platforms like Volza.com and Zauba.com. These show which Indian companies exported which products to which countries.

**Why it works for this ICP specifically:**
- Export activity is a direct C6 signal (active growth: new export markets entered).
- Export of biotech/diagnostics products requires CDSCO compliance and often international regulatory approvals — signals C3 simultaneously.
- Filtering by HS code (HSN code for diagnostics, biologics, specialty chemicals) gives a pre-qualified universe.
- Exporting companies are by definition manufacturers (you cannot export a service in this context).

**How to use it:** Filter Volza or Zauba by HS codes for our segments:
- 3002 (blood; antisera; vaccines; toxins; cultures of microorganisms) — covers specialty biotech
- 3822 (diagnostic reagents) — covers IVD
- 9027 (instruments for physical/chemical analysis) — covers diagnostic instruments
Filter to Indian exporters, sort by export frequency (regular exporters preferred over one-time), filter to MSME size proxy (exclude companies with >$5M per shipment as these are likely >Rs.500Cr).

**Expected yield:** 500–700 relevant companies. High C1 pass rate (exporters are manufacturers). Some overlap with DSIR list.

**Limitation:** Export data lags by 6–9 months. Companies that only sell domestically (most MSMEs) won't appear. Volza/Zauba have paid access — license cost.

---

### Method 5: ABLE + ADMI + BDMA Association Member Directories

**Associations:**
- **ABLE** (Association of Biotech-Led Enterprises): Indian biotech association. Member directory includes specialty biotech companies across segments.
- **ADMI** (Association of Diagnostics Manufacturers of India): Specifically diagnostics — most members are genuine IVD manufacturers.
- **BDMA** (Bulk Drug Manufacturers Association): API manufacturers — useful for pharma sub-segments.
- **FICCI Healthcare and Life Sciences Committee:** Members include specialty manufacturers.

**Why it works for this ICP specifically:**
- Active association membership signals an operating company that is engaged with industry — C6 growth signal.
- ADMI membership specifically means "diagnostics manufacturer" — strong C1 signal for the diagnostics segment.
- ABLE members are vetted — not traders or CROs.

**How to use it:** ADMI publishes a partial member directory on admi-india.org. ABLE directory is members-only but attendee lists from ABLE events are sometimes public. Email ABLE/ADMI directly — they sometimes share non-confidential member counts by segment.

**Expected yield:** 200–400 companies from these three associations combined. High ICP pass rate (~40%) because associations are more curated than generic databases.

**Limitation:** Not all members are public. Directory access sometimes requires membership or registration.

---

### Method 6: LinkedIn Sales Navigator — Inverted Search (DM-first)

**What it is:** Search for technically-qualified decision-makers in manufacturing companies in target cities, then identify their company.

**Why it works for this ICP specifically:**
- This inverts the normal search. Instead of finding companies and checking if the DM is technical, I find IIT/IISc/BITS/PhD founders in manufacturing, which pre-qualifies C4 (technical DM).
- LinkedIn filters: Industry: Biotechnology, Pharmaceuticals, Medical Devices; Geography: Chennai, Pune, Ahmedabad, Hyderabad, Bengaluru, Coimbatore; Seniority: Owner, CXO, Founder, Managing Director; Keywords: "IISc" OR "IIT" OR "BITS" OR "PhD" OR "Dr." in the profile.

**How to use it:** Sales Navigator search → export company names and founder profiles → cross-reference against MCA to get website and financials.

**Expected yield:** 400–600 unique founder profiles mapping to 300–400 companies. Strong C4 pre-qualification. Revenue verification needed from MCA.

**Limitation:** LinkedIn data is self-reported. Company headcount can be wrong for Indian MSMEs. Requires Sales Navigator license. Cannot directly see company revenue.

---

### Method 7: Government Scheme Beneficiary Lists — PLI + Make in India

**What it is:** Companies that received PLI (Production-Linked Incentive) scheme approval or Make in India certifications are public records. Relevant PLI schemes: Medical Devices PLI; Pharma PLI.

**Why it works for this ICP specifically:**
- PLI approval = government verified that the company is a genuine manufacturer (C1) in an eligible segment (C5 tailwind) with sufficient investment commitment (C6 growth).
- The application and approval process filters out traders, CROs, and distributors.
- Government published beneficiary lists for Medical Devices PLI are available from Ministry of Chemicals & Fertilizers.

**Expected yield:** 100–200 companies in diagnostics/biotech PLI. High pass rate — ~50% likely ICP qualified.

**Limitation:** PLI focus is on capital-intensive manufacturing at scale. May skew larger (Rs.300–500Cr+). Some PLI beneficiaries may have already crossed the Rs.500Cr threshold.

---

## Part B — Question 2: The 1000-Company Proposal

**Goal:** Build a verified list of 1000 ICP-qualified companies (Federer profile) within 30 calendar days.

**Constraint:** Quality over volume — every company must have evidence-backed scores on all 6 criteria.

**Key assumption from Part A research:** ~30% yield rate. To get 1000 passes, I need a starting universe of ~3,500 companies.

---

## The Sourcing Funnel

```
Universe Building — Week 1
(Target: 3,500–4,000 raw company names)

  ↓ Hard Pre-Filters (automated)
  Remove: no website / revenue >Rs.500Cr / "Trading" in name / dormant MCA status

Screened Pool — End of Week 1
(Target: 2,000–2,500 companies with websites)

  ↓ Website Scraping + AI First-Pass Scoring (Weeks 2–3)
  Claude Haiku: C1, C2, C5 (factual, lower judgment)
  Claude Sonnet: C3, C4, C6 (judgment-heavy, higher stakes)

First-Pass Qualified — End of Week 3
(Target: 1,200–1,400 pass / 300–400 borderline flagged)

  ↓ Human QA on Flagged Companies (Week 4)
  Review 300–400 borderline + spot-check 50 strong-pass

Final Verified List — End of Week 4
(Target: 1,000 companies with full evidence backing)
```

---

## Week 1: Building the Universe (Days 1–7)

**Goal:** 3,500–4,000 unique company names with city, segment tag, and website URL.

### Day 1–2: Structured Data Sources (Fastest to Process)

**DSIR Recognized R&D Units List:**
- Download from dsir.gov.in
- Parse Excel/PDF: extract company name, city, state, industry category
- Filter to: target states (TN, MH, GJ, KA, TS, RJ) + target industry categories (pharma, biotech, medical devices, industrial chemicals)
- Expected yield after filter: 800–1,000 companies

**BSE SME / NSE Emerge Listed Companies:**
- Download sector-wise lists from BSE/NSE
- Filter to NIC codes: 21 (pharma), 2100 (basic pharma), 2109 (other pharma/biotech), 3250 (medical/dental instruments), 20 (chemicals)
- Expected yield: 400–500 companies
- Advantage: immediate revenue data from public filings (filters >Rs.500Cr automatically)

**CDSCO Licensed Manufacturers:**
- Download state-wise manufacturer license lists from cdsco.gov.in
- Filter to: diagnostics kits, biologicals, medical devices (Class B and C)
- Expected yield: 600–800 relevant companies

### Day 3–4: Expo Directories and Association Lists

**Scraper: BioAsia 2023, 2024 Exhibitor Directories**
```python
# Playwright scraper for exhibitor pages
# Target: bioasia.in/exhibitors, cphi.in/exhibitors, medicall.in/exhibitors
# Extract: company name, website, segment, city
# Politeness: 2-second delay between requests
```
Expected yield: 400–500 unique companies (after dedup with DSIR + BSE)

**ADMI Member Directory:**
- admi-india.org (partial public list)
- Manual + scrape: ~150–200 diagnostics manufacturers

**ABLE Event Attendee Lists:**
- Public PDFs from BioAsia, India Bio conferences
- Expected: 200–300 companies

### Day 5–6: Export Data + LinkedIn

**Volza / Zauba Export Data:**
- Filter by HS codes: 3002, 3822, 9027, 3808 (biopesticides)
- Filter: India exporters, 2022–2024 shipment dates, exclude shipments >$10M/year (likely >Rs.500Cr companies)
- Expected: 500–700 companies

**LinkedIn Sales Navigator:**
- Technical DM search across 8 target cities
- Export company list
- Expected: 300–400 unique companies

### Day 7: Deduplication and Website Discovery

**Deduplication:**
- Fuzzy name matching (Levenshtein distance + CIN number matching for listed companies)
- Manual review of top 100 suspected duplicates
- Tool: Python `fuzzywuzzy` library or `recordlinkage`

**Website discovery for companies without URLs:**
- Google Search API: "{company name} {city} official website"
- Automate with Python `googlesearch-python` library
- Expected: 60% of universe has website from structured sources; 40% needs discovery

**Week 1 Output:**
- 3,500–4,000 unique companies
- Fields: company name, city, state, segment tag, website URL (if found), source tag
- Format: PostgreSQL database + CSV master file

---

## Week 2: Scraping + AI First-Pass Scoring (Days 8–14)

### The Scraper

**Tool:** Python + Playwright (handles JavaScript-heavy sites)

**Pages scraped per company (up to 8):**
- Homepage
- /about or /about-us
- /products or /services (critical for C1 determination)
- /leadership or /team or /management (critical for C4)
- /news or /press or /media (C6 website signal)
- /careers or /jobs (C6 hiring signal)
- /certifications or /quality
- /contact (city confirmation — C2)

**Rate limiting:** 2-second delays; 5 parallel workers; timeout 10 seconds per page. Respects robots.txt.

**Data storage:** Concatenate page text to ~8,000 tokens max. Store in PostgreSQL with company ID.

**Estimated time:** 3,500 companies × ~40 seconds/company average ÷ 5 parallel workers = ~8 hours continuous run.

### The AI Scoring Pipeline

**Prompt architecture (sent to Claude Haiku for first pass):**

```
You are scoring an Indian manufacturing company against 6 ICP criteria for a B2B consulting firm.

ICP: Indian specialty manufacturer, Rs.50Cr–Rs.500Cr revenue, promoter-driven, 
differentiated physical product, technical decision-maker, active growth signals.

Company website text:
[SCRAPED_TEXT_8K_TOKENS]

Score each criterion as Weak / Moderate / Strong with ONE specific evidence quote from the text.
Return ONLY a JSON object with this exact structure:

{
  "C1_manufacturer": {"score": "Strong/Moderate/Weak", "evidence": "...", "confidence": "high/medium/low"},
  "C2_india_based": {"score": "Strong/Moderate/Weak", "evidence": "...", "confidence": "high/medium/low"},
  "C3_differentiated": {"score": "Strong/Moderate/Weak", "evidence": "...", "confidence": "high/medium/low"},
  "C4_technical_dm": {"score": "Strong/Moderate/Weak", "evidence": "...", "confidence": "high/medium/low"},
  "C5_growing_sector": {"score": "Strong/Moderate/Weak", "evidence": "...", "confidence": "high/medium/low"},
  "C6_growth_signals": {"score": "Strong/Moderate/Weak", "evidence": "...", "confidence": "high/medium/low"},
  "auto_disqualify": true/false,
  "disqualify_reason": "...",
  "federer_score": [0-100],
  "verdict": "strong_pass/pass/borderline/fail"
}

CRITICAL RULES:
- If the company sells services (testing, consulting, analytical services) not physical products: C1 = Weak, auto_disqualify = true
- If revenue evidence suggests >Rs.500Cr: auto_disqualify = true
- ISO 9001 alone is NOT a differentiator. Score C3 Weak if only ISO 9001 is mentioned.
- C3 Strong requires: patents, DSIR, USFDA/EU-GMP, "first/only/pioneer", proprietary products
- C4 Strong requires: PhD, IIT/IISc/BITS alumni, ex-ISRO/DRDO, publications
- C6: count only signals from the last 18 months (2023 onwards)
```

**Two-tier scoring:**
- **Claude Haiku** for first pass: all 3,500 companies. ~Rs.0.40/company = Rs.1,400 total.
- **Claude Sonnet** for borderline re-score: companies scoring 40–60 total Federer score (~700 companies). ~Rs.3.50/company = Rs.2,450 total.

**Total AI cost estimate: ~Rs.4,000 for the full pipeline.**

**Estimated runtime:**
- Scraping: ~8 hours (5 parallel workers)
- Haiku scoring: ~3 seconds/company × 3,500 = ~3 hours
- Sonnet re-scoring: ~5 seconds × 700 = ~1 hour
- Total: ~12 hours compute time spread across 3–4 days

### Week 2 Output:
- All 3,500 companies scored
- ~1,200–1,400 first-pass "pass" or "strong_pass"
- ~300–400 flagged as borderline or low-confidence
- ~1,800–2,000 documented fails

---

## Week 3: Re-Scoring + QA Start (Days 15–21)

### Known AI Scoring Failure Modes (from Part A experience)

The Part A research revealed specific patterns where AI scoring goes wrong. I'll build auto-QA rules around each:

**Failure Mode 1 — C3 Inflation (ISO 9001 scored as differentiator):**
- Auto-flag: any company where C3 = "Moderate" or "Strong" and evidence only mentions "ISO 9001" or "ISO 14001"
- Action: re-score C3 as Weak, recalculate total

**Failure Mode 2 — C4 False Positives (any engineering degree = Strong):**
- Auto-flag: any company where C4 = "Strong" but evidence is only "B.Tech from [unspecified university]" without IIT/IISc/BITS/DRDO/ISRO/PhD
- Action: re-score C4 as Moderate

**Failure Mode 3 — C6 Stale Evidence (news from 2019–2021 scored as growth signal):**
- Auto-flag: any company where C6 ≥ "Moderate" but evidence quotes contain years 2020, 2021, 2022
- Action: re-score C6 as Weak

**Failure Mode 4 — CRO False Pass (service company slips through C1):**
- Auto-flag: any company where C1 = "Strong" but company name or description contains "CRO", "testing services", "analytical services", "contract research", "lab services"
- Action: manual review immediately

**Failure Mode 5 — City Mismatch (company with branch office scored as Chennai-based):**
- Auto-flag: any company where C2 = "Strong" for Chennai but city evidence mentions "Mumbai" or "Delhi" or "Hyderabad" as primary
- Action: manual review

### Human QA Process (Days 18–21)

**Review queue:** ~400 flagged companies + 50 random spot-checks of strong_pass

**Per-company QA (3–4 minutes each):**
1. Open website directly in browser
2. Check /products: is this a manufacturer? What specific physical product?
3. Check /about: founder credentials — do they match C4 evidence?
4. Check /news: any press from 2023 onwards?
5. Check LinkedIn: current headcount vs 1 year ago
6. Make accept/reject/adjust decision

**Weekly QA targets:**
- Day 18–19: 200 flagged companies reviewed (100/day)
- Day 20–21: 200 more reviewed

**QA tracking:** Google Sheets with columns: Company ID | Auto-flag reason | QA decision | Adjuster score | Notes

---

## Week 4: Final Assembly + Personalization (Days 22–30)

### Days 22–24: Final Assembly

**Merge sources:**
1. All confirmed strong_pass from first-pass scoring (unflagged)
2. QA-verified pass from flagged queue
3. Drop all remaining borderline/unverified

**Deduplication final pass:**
- CIN number match for all companies where CIN is known
- Fuzzy name match for remainder
- Manual review of top 50 suspected duplicates

**Target count:** 1,000 verified companies

If yield is below 1,000 at this stage, pull from the reserve pool:
- Reopen borderline cases (40–59 Federer score) for human review
- Expand to adjacent cities (Coimbatore for Chennai; Surat for Ahmedabad)
- Add one additional expo directory (IMTEX for machine tools; AgriIntex for agri-biotech)

### Days 25–27: Priority Tier Enrichment

**Priority-200 list:** Top 200 companies by Federer score across all segments and cities

For each Priority-200 company, add:
- **Personalization hook:** Specific, recent, true detail about the company usable in line 1 of an outreach email (sourced from website /news, press coverage, LinkedIn posts, or recent product launch)
- **Contact details:** Founder/MD name, LinkedIn profile URL, company email format
- **Outreach readiness flag:** "Ready to contact" vs "Needs additional research"

### Days 28–30: Final Deliverables + Buffer

**Final CSV fields for each of 1,000 companies:**
- Company name, website, city, state, segment
- Revenue band (verified or estimated with source)
- Decision-maker name + title + background
- C1–C6 scores (Weak/Moderate/Strong) + evidence quote per criterion
- Federer score (0–100) + score band (A/B/C/D)
- Verdict + verdict reasoning (1 sentence)
- Personalization hook (Priority-200 only)
- Data confidence flag (high/medium/low)
- Source list (which databases contributed data)

**Day 30: Buffer** for overruns, final QA, documentation.

---

## Realistic Yield Projections

| Stage | Companies | Notes |
|-------|-----------|-------|
| Raw universe | 3,500–4,000 | Before any filtering |
| After hard pre-filters | 2,000–2,500 | Removed: no website, dormant MCA, obvious traders |
| After AI first-pass scoring | 1,200–1,400 pass | ~35% pass rate at this stage |
| After Sonnet re-scoring of borderline | +100–150 additional passes | Some borderlines upgrade after deeper scoring |
| After human QA (net of adjustments) | 1,000–1,100 | QA removes ~10–15% of first-pass passes as false positives |
| Final verified list | **1,000** | Target achieved |

---

## Risk Mitigation

| Risk | Probability | Mitigation |
|------|-------------|------------|
| Yield lower than 30% (1,000 passes from 3,500) | Medium | Expand universe: add state industrial directories (TIDCO for Tamil Nadu, MIDC for Maharashtra, GIDC for Gujarat), add 2 more expo lists |
| Scraper blocked by websites | Low-Medium | Rotate user agents; add delays; use headless Playwright over requests. Fall back to manual for key blocked sites. |
| AI scoring accuracy <80% | Medium | Calibrate on 20 companies before full run. Retune prompt on specific failure modes. Split C1/C2 (easy) and C3/C4 (hard) into separate prompts. |
| QA bottleneck | Medium | Pre-sort flagged queue by Federer score — review borderline near-passes first, quick-reject clear fails. |
| Revenue data not available | High (common) | Use proxy signals: employee count (500+ = likely >Rs.50Cr), paid-up capital from MCA (>Rs.50L paid-up usually signals operating company), IndiaMART export badges |
| Duplicates across sources | Medium | Fuzzy matching + CIN number matching. Manual review of top 50 suspected duplicates. |

---

## Tools and Budget

| Tool | Purpose | Cost Estimate |
|------|---------|--------------|
| Claude Haiku API | First-pass scoring (3,500 companies) | ~Rs.1,400 |
| Claude Sonnet API | Borderline re-scoring (700 companies) | ~Rs.2,450 |
| Playwright + Python | Website scraping | Free (open source) |
| GitHub Copilot | Code assistance for pipeline | Licence provided |
| LinkedIn Sales Navigator | DM discovery | Licence provided |
| Antigravity / Tofler / Tracxn | MCA data + revenue verification | Licence provided |
| Volza / Zauba | Export data | Licence provided (~Rs.15,000/month) |
| Google Sheets + PostgreSQL | Master data storage + QA tracking | Free |
| **Total AI cost** | | **~Rs.4,000** |
| **Total data licence cost** | | **~Rs.15,000–20,000** |
| **Total one-month budget** | | **~Rs.20,000–25,000** |

---

## Final Deliverables

1. **Master CSV** — 1,000 companies with all fields per the assignment format
2. **Priority-200 list** — Top 200 with personalization hooks ready for outbound
3. **Fail list** — 500–700 documented rejections with reason codes (for team learning)
4. **Methodology document** — Sources, pipeline architecture, prompt used, QA process, yield rates at each stage
5. **Code repository** — Scraper, scoring pipeline, deduplication notebook, QA tracker — all reproducible end-to-end
6. **Source breakdown dashboard** — Which sources contributed how many final passes (to guide future sourcing investment)

---

*This proposal is the written version submitted to GitHub. A hand-drawn diagram showing the sourcing funnel, weekly flow, tools at each stage, and quality checkpoints has been submitted separately in the Internshala chat window.*

*DeepThought | PDGMS — AI Execution Workspace | Submitted by: [Your Name] | May 2026*
