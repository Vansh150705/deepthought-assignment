# DeepThought Business Analytics Internship Assignment
## Target Company Research — Chennai | Specialty Biotech + Diagnostics

**Submitted by:** Vansh Mahajan
**Date:** May 2026
**Assignment:** Business Analytics Role Simulation — Federer Company Research

---

## Repository Structure

```
├── companies.csv              # Part A: 25 companies (scored with Federer criteria)
├── methodology.md             # Part A: How I found and scored these companies
├── pipeline.py                # Part A: Python scraping + AI scoring pipeline code
├── part-b-proposal.md         # Part B: Sourcing methods + 1000-company proposal
└── README.md                  # This file
```

---

## Part A Summary

**City:** Chennai
**Segments:** Specialty Biotech + Specialty Diagnostics (IVD)

**Companies researched:** ~80
**Companies in final CSV:** 25 (including documented passes, borderlines, and fails)
**Expected yield rate:** ~30% (consistent with assignment guideline)

### Pass / Fail Breakdown

| Category | Count |
|----------|-------|
| A-band (Strong Federer, 80–100) | 3 |
| B-band (Probable Federer, 60–79) | 2 |
| C-band (Borderline, 40–59) | 3 |
| D-band (Auto-disqualify / Fail) | 17 |

### Key Findings

**Strongest pass:** Athenese Dx (Rs.72.7Cr IVD manufacturer at TICEL Bio Park, DSIR-recognized R&D, proprietary TRUSTline and TRUEchemie brands, 329 employees growing 5% YoY).

**Most important pattern discovered:** Chennai's biotech cluster has a severe CRO trap. Many companies in Guindy, Anna Nagar, Taramani, and Siruseri use "biotech" and "diagnostics" language but are contract research organizations, testing labs, or analytical service providers — not manufacturers. C1 verification (what does the company actually sell? products or services?) is the most critical filtering step for this geography.

**Why Chennai is harder than Hyderabad for this ICP:**
- Fewer Rs.100–300Cr specialty manufacturers in biotech/diagnostics than Hyderabad's defence electronics cluster
- More service companies (CROs) disguised as manufacturers
- Cluster is younger (TICEL Bio Park founded 2004 vs Hyderabad's Genome Valley 1990s)
- Stronger fits likely exist in Chennai's medical device / diagnostic instrument sub-segment (Trivitron, Athenese Dx) but Trivitron has exceeded the revenue ceiling

---

## Part B Summary

See `part-b-proposal.md` for the full 1000-company proposal.

**High-level plan:**
- Week 1: Build 3,500–4,000 company universe from 7 sources (DSIR list, BSE SME, CDSCO, expo directories, export data, LinkedIn Sales Navigator, association directories)
- Week 2: Scrape all company websites (Playwright + Python) and run Claude Haiku first-pass ICP scoring
- Week 3: Claude Sonnet re-scoring on borderline cases + human QA on ~400 flagged companies
- Week 4: Final assembly of 1,000 verified companies + Priority-200 with personalization hooks

**Estimated AI cost:** ~Rs.4,000 for the full pipeline
**Estimated yield:** 1,000 passes from a 3,500-company starting universe (28–30% pass rate)

---

## Anti-Hallucination Approach

This assignment required significant discipline to avoid AI hallucination. My approach:

1. **Revenue numbers only from MCA-traceable sources** (Tofler, Tracxn with MCA citations). Never used EasyLeadz, RocketReach, or ZoomInfo revenue estimates as primary — always cross-checked.

2. **City verified from operational address** — not from company name, media mentions, or database labels. Multiple companies (HiMedia, Agappe, Vimta, Mylab) had Chennai mentions but operational addresses elsewhere.

3. **C1 (Manufacturer) verified from product listings** — IndiaMART product listings and company website /products page. Companies listing "services" rather than "products for sale" = CRO fail.

4. **Where I disagreed with AI suggestions:** The strongest example is Bioklone. Multiple databases labeled Bioklone as a "manufacturer" and it has a PhD IISc founder with a genuine production facility. AI would likely score it as C3 Strong + C4 Strong. I overrode this: Bioklone sells custom antibody development services, not finished antibody products for sale. It is a CRO. The distinction is what the customer is buying — a custom service or a standard product. Revenue of Rs.80L and -17% decline confirmed the override.

5. **C3 inflation prevention:** ISO 9001 alone is explicitly scored Weak in my framework. AI consistently wants to inflate C3 for any certified company. I set this as a hard rule in my scoring prompt (see pipeline.py).

---

## Submission Checklist

- [x] CSV with 25 companies (scored with evidence) — `companies.csv`
- [x] Methodology document — `methodology.md`
- [x] Scraping + scoring code — `pipeline.py`
- [x] Part B sourcing methods — `part-b-proposal.md`
- [ ] **Hand-drawn diagram** — submitted separately in Internshala chat window (mandatory)

---

*Questions about methodology or data sources: vansh150705@gmail.com*
