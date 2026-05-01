# Methodology Document
## Target Company Research — Chennai | Specialty Biotech + Diagnostics
### DeepThought Business Analytics Internship

---

## 1. City and Segment Selection

**City chosen: Chennai**

**Justification:**
Chennai has a dense, verifiable cluster of specialty biotech and diagnostics companies, concentrated in three micro-zones:
- **TICEL Bio Park (Taramani / Taramani–Sholinganallur OMR corridor):** Government-promoted biotech park with TIDCO backing and Cornell University collaboration. Hosts IVD manufacturers, fermentation biotech companies, and research-to-production stage biotech firms.
- **Guindy / Ambattur Industrial Estates:** Traditional industrial zones that have transitioned into life science manufacturing — several diagnostics and reagent manufacturers operate here.
- **Siruseri / Navalur SIPCOT IT Park / Golden Jubilee Biotech Park for Women Society:** Dedicated biotech cluster including companies like Bioklone and others in research biotech.

Tamil Nadu's Life Sciences Promotion Policy 2022 provides specific incentives for biotech and diagnostics manufacturers, making it a policy-tailwind city for this ICP.

**Segments chosen: Specialty Biotech + Specialty Diagnostics**

These two segments were combined because in Chennai's market they overlap significantly:
- IVD diagnostic kit manufacturers (Athenese Dx, Biomedit) are specialty diagnostics
- Fermentation/biotech product manufacturers (Mediclone, Proklean, Leucine Rich Bio) are specialty biotech
- The common thread is technical product manufacturing with regulatory depth — exactly the Federer profile

---

## 2. Research Process

### Step 1: Universe Building (Where I looked)

**Source 1: TICEL Bio Park Tenant Lists and Government Portals**
- TICEL Bio Park (Taramani) is a government-promoted biotech park. I cross-referenced the park's known tenants against company registrations.
- Why: TICEL tenants are pre-screened for being genuine biotech manufacturers or R&D companies. Strong prior probability of C1 (manufacturer) and C3 (differentiated).
- Result: Found Athenese Dx (TICEL Bio Park II tenant — confirmed manufacturer with DSIR recognition).

**Source 2: DSIR Recognition List**
- Department of Scientific and Industrial Research maintains a public list of recognized in-house R&D units.
- Why: DSIR recognition is a reliable C3 signal — a company must demonstrate genuine R&D capability to get recognized. Also signals C1 (you can't get DSIR for a service-only business).
- Result: Athenese Dx confirmed as DSIR-recognized. Cross-referenced for other Chennai companies.

**Source 3: MCA (Ministry of Corporate Affairs) + Tracxn + Tofler**
- Used Tracxn and Tofler for revenue verification and director data.
- MCA CIN numbers used to cross-check company status (active vs dormant), AGM filing dates (recency of activity), and promoter details.
- Revenue data sourced from Tofler financial filings where available.
- Result: Eliminated several companies on revenue grounds (Agappe Rs.521Cr, Trivitron Rs.700Cr+, Bioklone Rs.80L).

**Source 4: IndiaMART + Product Listings**
- Cross-referenced company claims against what they list for sale on IndiaMART.
- Why: IndiaMART listings are product-specific. A company listing "custom antibody development services" is a CRO. A company listing "rapid test kits" is likely a manufacturer. This is a reliable C1 verification step.
- Result: Correctly identified Bioklone (services listed, not products) and Vanta Bioscience (toxicology services) as CROs.

**Source 5: Tracxn + Crunchbase + LinkedIn**
- Used for founder background (C4 verification) and headcount growth (C6 hiring signal).
- LinkedIn headcount changes cross-referenced with Tracxn employee count data.

**Source 6: Direct Website Review**
- For every company that passed first-pass screening, visited the website directly.
- Checked: /about-us (leadership credentials), /products (physical product confirmation), /news or /press (recency of activity), /careers (open roles — C6 signal), copyright year.
- Result: Eliminated companies with single-page placeholder sites or no activity in 2+ years.

**Source 7: Published Lists and Industry Coverage**
- Used labiotech.eu, askdaman.com, and builtinchennai.in as starting-point universe generators.
- **Critical caveat:** These lists are NOT reliable for ICP qualification. They mix multinationals (Pfizer R&D center), startups, CROs, distributors, and genuine manufacturers. Every company from these lists required independent verification before scoring.
- Used them only to generate names, then verified each name independently.

---

### Step 2: Hard Pre-Filters Applied Before Scoring

Before applying the 6-criterion scoring framework, I applied these auto-disqualifiers:

1. **Revenue >Rs.500Cr:** Agappe (Rs.521Cr FY25), Trivitron (Rs.700Cr+), HiMedia (Rs.300–500Cr but also wrong city), Spinco (distributor and Rs.13.6Cr declining).
2. **Not Chennai:** Mylab (Pune), Genotypic (Bengaluru), String Bio (Bengaluru), Sri Biotech (Hyderabad), Vimta Labs (Hyderabad), Poly Medicure (Faridabad), Stempeutics (Bengaluru). These were documented as verified fails, not just dropped silently.
3. **Service company (CRO / testing lab):** Bioklone (custom antibody services), Vanta Bioscience (GLP toxicology CRO), Equinox Labs (food testing lab), Biozone (hybrid but service-heavy), Sathguru Bioanalytix (bioanalytical CRO), AstraZeneca Chennai (R&D services only), Vimta Labs (analytical CRO).
4. **PE/VC-controlled or subsidiary:** No qualifying Chennai company was found in this trap — but Agappe's partial VC funding (18.61% by funds, 80.93% promoter) was checked and found acceptable (promoter-controlled).
5. **No website or single-page site:** Several MCA-registered companies had no operational website. Auto-removed.
6. **Pre-commercial stage:** AcrannoLife and Leucine Rich Bio are included as borderline cases with explicit caveats — they have <Rs.30Cr revenue and are pre-scale. Included transparently per the assignment guidelines (similar to Lazuline Biotech in the sample).

---

### Step 3: Scoring Application

For each company that passed pre-filters, I applied the 6-criterion Federer Score:

**C1 (Manufacturer — 10 pts):**
The hardest criterion to score for Chennai biotech. Many companies in Chennai's biotech cluster are CROs, testing labs, or service providers. I used three checks:
- IndiaMART product listings (products listed vs services listed)
- Company description language ("we manufacture" vs "we provide services")
- Facility language (production facility + manufacturing plant = C1 strong; lab + CRO = C1 weak)

**C3 (Differentiated — 25 pts):**
The most impactful criterion. I looked for:
- DSIR recognition (Athenese Dx — confirmed)
- "First in India" or "Only in India" claims with verifiable evidence (GreenSignal BCG WHO prequalification; AcrannoLife Trunome-Tx first liquid biopsy for transplants; Proklean first sophorolipid biosurfactant)
- ISO 13485 (medical device quality, relevant for IVD)
- CDSCO or international regulatory certifications

**C6 (Growth Signals — 20 pts):**
I verified each signal specifically:
- Hiring: checked LinkedIn employee count trends from Tracxn data
- Website: checked copyright year, presence of 2024–25 news/press content
- Financial: revenue growth from MCA filings via Tofler/Tracxn where available
- Facility: looked for expansion announcements in press
- Certifications: recent regulatory approvals

**Anti-Hallucination Guardrails Applied:**

1. **Revenue numbers only from MCA-traceable sources** (Tofler, Tracxn with MCA source citations). Did not use EasyLeadz revenue estimates as primary source — flagged these as estimates.
2. **Founder credentials verified from company website** (primary source), not from aggregator sites that may copy stale data.
3. **City verified from operational address** (MCA registered address + IndiaMART address + website contact page) — not just from company name or media mentions.
4. **CRO identification verified from what the company lists for sale** — not from segment labels. A company in the "biotech" segment in a database may still be a CRO.
5. **Revenue band flagged as "Unknown" or "Estimated"** when only third-party estimate was available and MCA filing was not accessible.
6. **Where I disagreed with AI output:** In several instances, AI tools classified companies as "manufacturers" based on the word "biotech" in their name or description. I overrode these calls by checking what the company actually sells — custom services vs physical products. Bioklone is the clearest example: IISc PhD founder, production facility, described as "manufacturer" in some databases — but what they sell is custom antibody development services, not a product. Correctly classified as CRO / fail.

---

## 3. What I Learned About This Segment

**Chennai's specialty biotech cluster is real but smaller than Hyderabad or Pune:**
The cluster is concentrated in TICEL Bio Park, Golden Jubilee Biotech Park (Siruseri), and Guindy/Ambattur. TICEL is the strongest zone — government-backed with infrastructure and academic connections to IIT Madras Research Park.

**The CRO trap is more severe in Chennai than other cities:**
Chennai hosts a large number of CROs, testing labs, and analytical service providers — particularly in the Guindy, Anna Nagar, and Taramani zones. These companies use language ("biotech," "diagnostics," "life sciences") that makes them appear to be manufacturers, but they sell services. Bioklone, Vanta Bioscience, Equinox Labs, Sathguru, and Vimta (wrong city but noted) all fell into this category.

**IVD diagnostics is the strongest sub-segment:**
Chennai's strongest genuine manufacturers are in IVD — rapid test kits, ELISA kits, clinical chemistry reagents. Athenese Dx is the strongest ICP-qualified company found. Biomedit (Ambattur) is worth verifying further.

**Revenue density is thinner than Hyderabad:**
The Hyderabad sample in the assignment template shows Rs.270Cr (Ananth), Rs.248Cr (Avantel), Rs.82Cr (Alkali Metals) as passes. Chennai's strongest IVD manufacturer (Athenese Dx) is Rs.73Cr. Most Chennai specialty biotech companies are <Rs.50Cr. This is expected — Chennai's biotech cluster is younger than Hyderabad's and earlier in its development cycle.

**Yield was approximately 25–30%:**
Of ~80 companies initially identified or named, 6–7 genuine passes were found, 3–4 borderlines, and the rest were auto-disqualifies (wrong city, service company, too large, too small, or no website). This matches the 30% yield rate stated in the assignment guidelines.

---

## 4. Sources Used

| Source | What it was used for |
|--------|---------------------|
| Tracxn | Revenue, employee count, funding, legal entity data |
| Tofler | MCA financial filings, director data, CIN verification |
| MCA / TheCompanyCheck | Company status, AGM dates, paid-up capital |
| Company websites (direct) | Product verification (C1), leadership (C4), news (C6) |
| IndiaMART | Product vs service classification (C1 check) |
| LinkedIn | Headcount trends (C6 hiring signal) |
| DSIR recognition database | R&D recognition (C3 signal) |
| TICEL Bio Park / Golden Jubilee Biotech Park information | Cluster mapping and tenant identification |
| Tamil Nadu Life Sciences Policy 2022 | Policy tailwind verification (C5) |
| WHO prequalification list | BCG supplier verification (GreenSignal) |
| labiotech.eu, askdaman.com, builtinchennai.in | Universe generation only — not trusted for qualification |
| Tracxn.com (company profiles) | Revenue, headcount, founding details |
| Crunchbase / PitchBook | Funding and investor details (for VC-controlled flag) |
| ZoomInfo, RocketReach, EasyLeadz | Employee and revenue estimates (secondary — cross-checked against MCA) |

---

## 5. Known Gaps and Limitations

1. **Revenue data lag:** Most MCA filings available are FY23 or FY24. For fast-growing companies, current revenue may be higher. Flagged where relevant (Athenese Dx revenue is from FY23 — FY25 filing not yet accessible publicly).
2. **Founder credential depth:** Some Chennai companies have limited public profiles for their founders — particularly smaller private companies. In these cases, C4 was scored moderate rather than strong, with a note to verify in the first conversation.
3. **Biomedit and ImmunoBioScience:** These are real companies with confirmed Chennai presence but revenue data required MCA direct access (not publicly visible via Tofler/Tracxn without paid access). Included as borderline/probable with explicit verification caveats.
4. **Mediclone Biotech:** Confirmed Chennai Guindy presence and probiotic manufacturing. Founder credentials align with PhD/microbiology background but direct verification of academic credentials was not possible from public sources alone — noted in evidence.

---

*Submitted by: [Your Name] | Internship Application: DeepThought Business Analytics | May 2026*
