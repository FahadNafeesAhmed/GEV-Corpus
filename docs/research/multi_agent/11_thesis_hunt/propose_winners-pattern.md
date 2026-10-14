# Thesis hunt — lens: pattern match to winning pitches

_Research input only: facts, arithmetic, tables, sources. No memo sentences and no forecast choices; ranges and methods only. Consensus figures: Bloomberg, 2026-10-01 (academic licence; keep inside the project folder). Working date 2026-10-01. Price $987.45._

Files used
- `pitch-winners-corpus/PLAYBOOK.md`, `GEV_GAP_CHECK.md`, `lenses/01_wedge.md`; wedge sections of 11 cases: psc-2022-pgny, bam-2025-frpt, pro-einhorn-2011-gmcr, witg-2025-vitl, psc-2026-dash, psc-2026-bkr, sohn-ny-2024-asml, cfa-rc-2021-vws, sohn-ny-2019-lw, cfa-rc-2023-qan, witg-2025-blbd.
- `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json` (keys `Block|Parent|Line|YYYY Qn`), `06_modl.xlsx` (Q3 2026 single period), `01_eeo_annual.xlsx`; `GEV_bloomberg_pull_filled_2026-10-01.xlsx` sheets Consensus and ConsensusHistory.
- `data/gev.db` (chunks / chunks_fts, mgmt_guidance, transcript_statements, sources); `data/financials/gev_quarterly.csv`, `gev_segments.csv`, `gev_facts_long.csv`.
- Prior research: `09_finrobot_overnight/BLOOMBERG_VERDICT.md`, `E03_model_inputs.md`, `S01_backlog_margin_conversion.md`, `ROBUSTNESS_PACK.md`, `E07_catalyst_calendar.md`.

---

## 1. Archetypes that won, and the GEV instance computed for each

| # | Archetype (cases) | GEV instance tested | Line / period | Street (Bloomberg) | Computed | Gap | Passes error-band test? |
|---|---|---|---|---|---|---|---|
| A | A company schedule consensus does not model (LW capacity tracker, PGNY contract timing) | 10-Q note: share of equipment RPO recognised within 1 year | Equipment revenue, Q3 2026 to Q2 2027 | $30,245M | $31,616M floor; $32.5–34.9B with history | +4.5% floor; +7.5% to +15.5% | Marginal (section 2) |
| A2 | Same schedule, total | Equipment + services 1-year schedule | Total revenue, Q3 2026 to Q2 2027 | $50,019M | $51.6–53.5B (6 windows); $52.3B (7-window mean) | +3.1% to +7.0%; central +4.5% to +5.6% | Yes for 6 windows; gap near the 5% bar |
| B | Guidance that is a floor, re-derived from a physical driver (DASH one-time cost, FRPT reverse build) | FCF = deposits on gas slots: GW signed × $/kW × 25% down | Free cash flow, FY26 (and Q3 2026) | FY26 $12,196M; Q3 $1,502M; H2 $2,651M | FY26 $12.7–16.4B, central about $14.5B | −1% to +34%; central +19% | Marginal (section 3) |
| C | KPI disclosed rarely / switched (VITL, GMCR) | Equipment margin added to backlog, disclosed once a year in January | FY26 KPI, revealed January 2027 | No Bloomberg field. Only anchor: management floor "at least $8B" | $12–22B | +50% to +175% vs the floor | Not a consensus line (section 4) |
| D | Price / consensus reversed into a physical quantity vs a ceiling (QAN, FRPT, VITL) | Street Power equipment revenue ÷ management output ladder = implied $/kW, vs order $/kW | Power equipment revenue 2027–2030 | 12,151 / 15,888 / 19,256 / 23,469 | Implied $552 / $636 / $688 / $782 per kW vs order prices $547–$916 | 0% to +33% (2029) | No. Realisation ratio ranges 0.73–1.26 (section 5.1) |
| E | Physical quantity vs the order book (short side) | Street wind MW deliveries vs wind orders one year earlier | Wind turbines delivered, H1 2027 | 1,882 MW | 1.3–2.1 GW | −31% to +12% | No. Band straddles Street (section 5.2) |
| F | Bull model re-run with evidenced inputs (GMCR) | Street gross margin → implied equipment gross margin vs disclosed backlog contribution margin | Equipment gross margin 2027–2030 (derived) | 22.5–23.8% / 26–27% / 31–32% / 32.5–33.7% | Backlog contribution margin 16–29% (YE25), 22–35% (YE26 est.) less an undisclosed fixed-cost layer | not provable | No (section 5.3) |
| G | Hidden economics rebuilt from disclosures (REAL, HLF) | LTSA "changes in estimated profitability" inside Power services | Power EBITDA | — | Unfavourable $319M FY24, $151M FY25, $218M H1 2026 | already in reported margins | Context only (section 5.4) |
| H | Outside anchor as ceiling (CP, BKR) | Siemens Energy Gas Services FY28 margin target 18–20% vs Street GEV Power 2028 EBITDA margin 23.3% | Power margin 2028 | 23.3% | Definitions differ (EBITA-type vs EBITDA) | not comparable 1:1 | Context only |
| I | Temporary condition priced as permanent (DE, VITL, LW) | Slot-reservation cash in 2026 | FCF FY27 | $7,654M (−37% y/y) | Depends on GW signed in 2027; $5.5–10B | band straddles Street | No (section 5.5) |

---

## 2. Instance A — the conversion schedule (deepened and attacked)

### 2.1 Source sentences (all filings; text search `"Equipment-related" AND "expected to be" AND recognized`)

| As of | Document | Equipment RPO $M | % within 1 / 2 / 5 yrs | Services RPO $M | % within 1 / 5 / 10 / 15 yrs |
|---|---|---|---|---|---|
| 12/31/23 | S-1 0001193125-24-066951 | 40,478 | 51 / 77 / 100 | 75,120 | 16 / 51 / 77 / 90 |
| 3/31/24 | 10-Q 0001996810-24-000008 | 42,210 | 45 / 71 / 93 | 74,083 | 16 / 52 / 77 / 91 |
| 6/30/24 | 424B3 0001996810-24-000069 | 41,561 | 47 / 69 / 91 | 73,915 | 17 / 52 / 77 / 91 |
| 9/30/24 | 424B3 0001996810-24-000084 | 42,069 | 46 / 70 / 91 | 75,678 | 17 / 52 / 78 / 91 |
| 12/31/24 | 424B3 0001996810-25-000012 | 43,047 | 44 / 69 / 93 | 75,976 | 18 / 53 / 78 / 91 |
| 3/31/25 | 424B3 0001996810-25-000074 | 45,478 | 45 / 71 / 91 | 77,959 | 18 / 53 / 78 / 91 |
| 6/30/25 | 10-Q 0001996810-25-000133 | 49,712 | 42 / 70 / 92 | 78,938 | 17 / 53 / 78 / 91 |
| 9/30/25 | 10-Q 0001996810-25-000160 | 54,092 | 41 / 71 / 97 | 81,177 | 17 / 53 / 78 / 91 |
| 12/31/25 | 10-K 0001996810-26-000015 | 64,245 | 37 / 69 / 97 | 85,993 | 17 / 52 / 77 / 91 |
| 3/31/26 | 10-Q 0001996810-26-000064 | 75,924 | 38 / 69 / 98 | 87,352 | 16 / 53 / 78 / 91 |
| 6/30/26 | 10-Q 0001996810-26-000148 | 87,821 | 36 / 65 / 97 | 88,463 | 16 / 54 / 79 / 92 |

The earlier back-test used three windows (12/31/24 to 6/30/25). Four more exist (12/31/23 to 9/30/24).

### 2.2 Back-test: next-four-quarter revenue ÷ scheduled amount

Formula: scheduled = RPO × % within 1 year. Ratio = revenue of the four quarters after the date ÷ scheduled. Reported equipment / services revenue by quarter from `gev_segments.csv` (rows `Product`, `Service`). Street quarters = sum of `Total Revenue|{Power,Wind,Electrification}|{Equipment,Services}`.

| As of | Equip. scheduled $M | Next 4Q equip. $M | Ratio | Ex-Prolec | Total scheduled $M | Next 4Q total $M | Ratio | Ex-Prolec | Street quarters in window |
|---|---|---|---|---|---|---|---|---|---|
| 12/31/23 | 20,644 | 18,952 | 0.918 | 0.918 | 32,663 | 34,934 | 1.070 | 1.070 | 0 |
| 3/31/24 | 18,994 | 19,532 | 1.028 | 1.028 | 30,848 | 35,707 | 1.158 | 1.158 | 0 |
| 6/30/24 | 19,534 | 20,232 | 1.036 | 1.036 | 32,099 | 36,614 | 1.141 | 1.141 | 0 |
| 9/30/24 | 19,352 | 20,822 | 1.076 | 1.076 | 32,217 | 37,670 | 1.169 | 1.169 | 0 |
| 12/31/24 | 18,941 | 20,934 | 1.105 | 1.105 | 32,616 | 38,068 | 1.167 | 1.167 | 0 |
| 3/31/25 | 20,465 | 21,991 | 1.075 | 1.050 | 34,498 | 39,374 | 1.141 | 1.127 | 0 |
| 6/30/25 | 20,879 | 23,556 | 1.128 | 1.061 | 34,298 | 41,367 | 1.206 | 1.165 | 0 |
| 9/30/25 | 22,178 | 25,158 | 1.134 | ~1.03 | 35,978 | 43,365 | 1.205 | ~1.14 | 1 |
| 12/31/25 | 23,771 | 27,534 | 1.158 | ~1.03 | 38,389 | 46,378 | 1.208 | ~1.13 | 2 |
| 3/31/26 | 28,851 | 28,956 | 1.004 | 1.004 | 42,827 | 48,251 | 1.127 | 1.127 | 3 |
| **6/30/26** | **31,616** | **30,245** | **0.957** | **0.957** | **45,770** | **50,035** | **1.093** | **1.093** | **4** |

Prolec adjustment: Prolec revenue "nearly $500M" in Q1 2026 and "nearly $900M" in Q2 2026 (call summaries, corpus src:1849 and src:1016) removed from windows that predate the acquisition.

Seven fully reported windows, ex-Prolec:

| Series | Values | Mean | Median | Std dev | Min | Max |
|---|---|---|---|---|---|---|
| Equipment | 0.918, 1.028, 1.036, 1.076, 1.105, 1.050, 1.061 | 1.039 | 1.050 | 0.059 | 0.918 | 1.105 |
| Equipment, without 12/31/23 | six values | 1.059 | 1.056 | 0.028 | 1.028 | 1.105 |
| Total | 1.070, 1.158, 1.141, 1.169, 1.167, 1.127, 1.165 | 1.142 | 1.158 | 0.036 | 1.070 | 1.169 |
| Total, without 12/31/23 | six values | 1.154 | 1.161 | 0.017 | 1.127 | 1.169 |

New facts from the longer back-test
- One window missed the schedule: 12/31/23 (FY24 equipment revenue 18,952 vs 20,644 scheduled, −8.2%). That window is the S-1 carve-out figure (51 / 77 / 100; one quarter later the same schedule read 45 / 71 / 93). FY24 included the sale of part of Steam Power nuclear activities to EDF (closed 2024-05-31; equipment RPO adjustment about $3.7B per the Q4 2024 deck, cited in S01) and the Vineyard Wind blade event (July 2024).
- The Street-implied ratio for the 6/30/26 window (0.957 equipment, 1.093 total) is below six of seven reported windows on both series.
- The more Street quarters a window contains, the lower its ratio: about 1.03, 1.03, 1.004, 0.957 (equipment, ex-Prolec).

### 2.3 Values for Q3 2026 to Q2 2027

| Line | Street $M | Method | Value $M | vs Street |
|---|---|---|---|---|
| Equipment | 30,245 | schedule, no in-window orders (ratio 1.00) | 31,616 (31,176–32,055 for rounding of 36%) | +4.5% (+3.1% to +6.0%) |
| Equipment | 30,245 | lowest of six windows (1.028) | 32,501 | +7.5% |
| Equipment | 30,245 | seven-window mean ex-Prolec (1.039) | 32,854 | +8.6% |
| Equipment | 30,245 | seven-window median ex-Prolec (1.050) | 33,201 | +9.8% |
| Equipment | 30,245 | highest ex-Prolec (1.105) | 34,935 | +15.5% |
| Equipment | 30,245 | worst window (0.918) | 29,023 | −4.0% |
| Total | 50,019 | lowest of six (1.127) | 51,575 | +3.1% |
| Total | 50,019 | seven-window mean (1.142) | 52,284 | +4.5% |
| Total | 50,019 | six-window mean (1.154) | 52,839 | +5.6% |
| Total | 50,019 | highest (1.169) | 53,517 | +7.0% |
| Total | 50,019 | worst window (1.070) | 48,952 | −2.1% |

Where the gap sits if H2 2026 lands on guidance. FY26 revenue guide $45.5–46.5B less H1 $20,442M gives H2 2026 of $25.06–26.06B; Street H2 2026 is $25,908M. Street H1 2027 is $24,111M (11,143 + 12,968).

| Total ratio | H2 2026 assumed $M | H1 2027 implied $M | vs Street H1 2027 |
|---|---|---|---|
| 1.127 | 25,908 | 25,668 | +6.5% |
| 1.154 | 25,908 | 26,931 | +11.7% |
| 1.169 | 25,908 | 27,609 | +14.5% |
| 1.154 | 26,408 (guide top + $0.35B) | 26,431 | +9.6% |

Equipment only: 31,616 − Street H2 2026 equipment 15,821 = 15,795 for H1 2027 before any in-window orders, vs Street H1 2027 equipment 14,424 (+9.5%) and vs H1 2026 actual 11,713 (+34.9% year on year).

### 2.4 Attacks

| Attack | Arithmetic | Effect |
|---|---|---|
| Street equipment / services split is a broker classification | Street Electrification services Q1 2027 629 and Q2 2027 696 vs actual Q1 2026 451 and Q2 2026 497 (+39%, +40%); Bloomberg low for Q3 2026 is 38.9. If about $0.4–0.5B is equipment, Street equipment is about $30.7B | Equipment floor gap falls to about +3%. Total-revenue test is unaffected |
| Segment eliminations | Company equipment revenue Q2 2026 6,459 vs segment sum 6,490 | Street consolidated equipment about $0.15B lower; gap slightly larger |
| Services cross-check with the same method | Street services 19,790 ÷ scheduled 14,154 = 1.398, above all seven windows (1.239–1.365) | Not robust: ±0.5 pt rounding of 16% moves the scheduled amount ±$442M (±3.1%). On an RPO-level basis Street services is 22.4% of services RPO vs 21.3–22.6% in seven windows: in line. No services gap |
| Bottom-up capacity for H1 2027 equipment | Power 5 GW a quarter vs 3.75 in H1 2026 (+33%) with price/mix about +10%: about $5.6B; Electrification H1 2026 5,631 at +25% organic plus one extra Prolec month: about $7.3B; Wind $1.5–2.3B. Sum $14.4–15.2B | Bottom-up lands at Street (14.4) to +5%, not at 15.8 or more. The schedule needs +35% year on year |
| Management guide | Q3 guide (Power +17–19%, Electrification $3.8–4.0B, Wind down low double digits) sums to about $11.95B vs Street $11,993M | First two quarters of the window are pinned near Street by guidance. Any gap must appear in Q4 2026 (a guide beat) or H1 2027 |
| Schedule has been missed once | 12/31/23 window 0.918 | A slip of the same size would put equipment revenue 4% below Street |
| Year-two version | Scheduled months 13–24 at 6/30/26: (65 − 36)% × 87,821 = 25,468 vs Street Q3 2027 to Q2 2028 equipment 35,137 (ratio 1.38; history 1.99–2.58 with large in-window orders) | No usable gap; prior finding stands |
| Mix | Extra equipment at 10–20% incremental margin: +$0.14–0.66B on $1.4–3.3B | Next-4Q EBITDA +1.7% to +8% vs Street $8,210M; margin rate lower by about 0.3–0.6 pt |
| Precedent for a revenue beat with margin held | 2026-07-22: revenue guide +$1B, margin guide unchanged, stock −8.7% on the day | Revenue beats have not been rewarded on their own |

### 2.5 Street conversion rates by division (Street next-4Q equipment ÷ 6/30/26 equipment RPO)

| Division | Equipment RPO $M | Street next-4Q equipment $M | Street % | History |
|---|---|---|---|---|
| Power | 39,261 | 10,874 | 27.7% | 54% (YE24 to FY25), 47% (6/30/25 window), 38% (YE25 to FY26E) |
| Wind | 8,197 | 5,830 | 71.1% | 58%, 67%, 65%, 64% |
| Electrification | 40,589 | 13,541 | 33.4% | 41% (35.6% ex-Prolec), 31.5% ex-Prolec |
| Sum (segment basis) | 88,047 | 30,245 | 34.4% | company statement: 36% |

For the company 36% to hold with Wind and Electrification at Street, Power equipment must be 31,616 − 5,830 − 13,541 + about 150 (eliminations) = about $12.4B, 14% above the Street $10,874M.

### 2.6 Reveal dates and comparators

| Date | Disclosure | Street comparator |
|---|---|---|
| 2026-10-28 | Q3 10-Q: equipment RPO at 9/30/26 × % within 1 year | Street equipment Q4 2026 to Q3 2027 $31,314M; total $51,607M |
| 2026-10-28 | Q3 equipment revenue | $7,482M (segment sum); $7,361M (MODL product revenue) |
| late Jan 2027 | 10-K: 12/31/26 schedule = FY27 scheduled equipment conversion | Street FY27 equipment $32,383M; FY27 revenue $53,029M |
| late Jan 2027 | FY27 revenue guide | $53,029M |
| Apr and Jul 2027 | Q1 2027, Q2 2027 revenue | $11,143M, $12,968M |

---

## 3. Instance B — FY26 free cash flow and the deposit arithmetic

### 3.1 What the Street has

| Item | Value | Source |
|---|---|---|
| FY26 FCF consensus | $12,196M | Consensus sheet, BEST_ESTIMATE_FCF 1FY |
| Q3 2026 / Q4 2026 FCF | $1,502M / $1,148M (15 analysts each); H2 $2,651M | `01_eeo_annual.xlsx`, segment_quarterly.json `Free Cash Flow` |
| H1 2026 actual | $9,897M | 10-Q Q2 2026 p.32 |
| Company FY26 guide | $11.5–12.5B, so H2 $1.60–2.60B | Q2 2026 release |
| Street Q3 2026 change in contract liabilities | mean −$1,402M, median −$50M, high +$1,873M, low −$8,795M | `06_modl.xlsx` row "Change in Contract Liabilities" (contributor count not shown) |
| Street contract liabilities at 9/30/26 | mean $37,492M, median $39,944M, high $41,817M | `06_modl.xlsx`; actual 6/30/26 $40,037M current |
| FY27 FCF consensus | $7,654M | Consensus sheet |

### 3.2 The guide for the rest of the year vs what happened

Remainder = full-year guide range less FCF already reported at the date of the guide. Sources: `mgmt_guidance` table (8-K releases), E03 Q7 and Q8.

| Guide date | Full-year guide $B | Reported to date $B | Implied remainder $B | Actual remainder $B | Actual vs top of range |
|---|---|---|---|---|---|
| 2025-04-23 | FY25 2.0–2.5 | Q1 0.975 | 1.03–1.53 (Q2–Q4) | 2.74 | +79% |
| 2025-07-23 | FY25 3.0–3.5 | H1 1.169 | 1.83–2.33 (H2) | 2.54 | +9% |
| 2025-10-22 | FY25 3.0–3.5 | 9M 1.902 | 1.10–1.60 (Q4) | 1.81 | +13% |
| 2025-12-09 | FY25 3.5–4.0 | 9M 1.902 | 1.60–2.10 (Q4) | 1.81 | inside the range (the one case with no beat; guide given three weeks before year-end) |
| 2026-01-28 | FY26 5.0–5.5 | — | 5.0–5.5 (FY) | 9.90 in H1 alone | +80% with H2 to come |
| 2026-04-22 | FY26 6.5–7.5 | Q1 4.791 | 1.71–2.71 (Q2–Q4) | 5.11 in Q2 alone | +88% with H2 to come |
| 2026-07-22 | FY26 11.5–12.5 | H1 9.897 | 1.60–2.60 (H2) | open | — |

Applied to H2 2026: top of range $2.60B × 1.09 = $2.83B (FY $12.7B); × 1.79 (median of the five guides given with at least one quarter still to run) = $4.65B (FY $14.5B). Five of six remainders finished above the top of the implied range; the sixth finished inside it.

### 3.3 Deposit arithmetic

Inputs
- Slot reservations carry "like, 25% down" (Morgan Stanley Laguna transcript, 2026-09-16, GEV-hosted PDF; verified in `04_market_briefing/DIGEST.md`).
- Order price per kW of gas-turbine capacity ordered = (change in Power equipment RPO + Power equipment revenue) ÷ GW ordered: H1 2025 $547, H2 2025 $697, Q4 2025 $753, H1 2026 $916 (includes hydro and nuclear equipment orders: about $0.5B in Q4 2025, $0.2B in Q1 2026 per the Q1 2026 call). Management: H1 2026 orders priced "more than 20% above" Q4 2025 (Q2 2026 call).
- H2 2026 new gas commitments: about 20 GW, "likely to prove to be conservative", Q4 above Q3, below the 40 GW first-half pace (Laguna).

Calibration: Power product contract liabilities (`gev_segments.csv`, `ContractWithCustomerLiability… Product;PowerSegment`) vs reservations signed

| Quarter | Reservation GW signed | Model: GW × $/kW × 25% | Actual change in Power product contract liabilities $M | Per GW signed (all contracts) |
|---|---|---|---|---|
| Q2 2025 | 7 | 7 × 600 × 0.25 = 1,050 | 930 | $103/kW |
| Q3 2025 | 12 | 12 × 650 × 0.25 = 1,950 | 923 | $71/kW |
| Q4 2025 | 21 | 21 × 750 × 0.25 = 3,940 | 3,933 | $164/kW |
| Q1 2026 | 19 | 19 × 900 × 0.25 = 4,275 | 3,929 | $187/kW |
| Q2 2026 | 18 | 18 × 900 × 0.25 = 4,050 | 7,320 | $366/kW |
| Sum | 77 | 15,265 | 17,035 (model 12% low) | |

Balance check: Power product contract liabilities ÷ GW under contract = $175, $180, $171, $175, $185, $222 per kW (Q1 2025 to Q2 2026).

H2 2026 change in contract liabilities

| Component | Low | High | Basis |
|---|---|---|---|
| Power: 18–25 GW of reservations × $950 × 25% (× 1.12 fit), less 0.4 for higher shipments | 3.9 | 6.2 | above |
| Electrification | 1.5 | 1.8 | H1 2026 +2.66B including the acquired Prolec balance; Q2 2026 +0.86B; Street H2 orders $14.0B vs $13.4B in H1 |
| Wind | −0.3 | 0.0 | deliveries of 3.3 GW draw down deposits |
| Total $B | 5.1 | 8.0 | central 6.5 (H1 2026: 13.7; H2 2025: 6.2) |

Cash kept per dollar of contract-liability growth, k = (FCF − cash before working capital) ÷ change in contract liabilities

| Period | FCF $M | Cash before working capital $M (adj. EBITDA − cash taxes − capex − pension + interest − restructuring) | Change in contract liabilities $M | k |
|---|---|---|---|---|
| FY24 | 1,701 | 359 | 2,799 | 0.48 |
| H1 2025 | 1,169 | 502 | 1,860 | 0.36 |
| H2 2025 | 2,541 | 570 | 6,159 | 0.32 |
| H1 2026 | 9,897 | −411 | 13,695 | 0.75 |

H2 2026: cash before working capital = Street EBITDA 4.19 − cash taxes 1.2–1.7 − capex 1.0 + 0.1 − 0.15 = about $1.7B (1.0–2.1).

| Case | k | Change in contract liabilities $B | H2 FCF $B | FY26 FCF $B | vs Street $12,196M |
|---|---|---|---|---|---|
| Guide top | — | — | 2.6 | 12.5 | +2.5% |
| Smallest historical beat (+9%) | — | — | 2.83 | 12.7 | +4.4% |
| Low | 0.32 | 5.1 | 3.3 | 13.2 | +8% |
| Central | 0.45 | 6.5 | 4.6 | 14.5 | +19% |
| Median historical beat (+79%) | — | — | 4.65 | 14.5 | +19% |
| High | 0.60 | 8.0 | 6.5 | 16.4 | +34% |
| Adverse (H2 2025 working-capital pattern scaled to +24% revenue, deposits at 5.1) | — | 5.1 | 1.7–2.2 | 11.6–12.1 | −5% to −1% |

What the guide requires: 1.7 + k × change ≤ 2.6, so k × change ≤ $0.9B; at k = 0.32 the increase in contract liabilities must be ≤ $2.8B in H2, against $13.7B in H1 and $6.2B in H2 2025.

Q3 2026 alone: cash before working capital about 0.7; change in contract liabilities 2.3–3.4 (8–12 GW of reservations); k 0.30–0.87 (last four quarters: 0.54, 0.30, 0.87, 0.67) gives $1.4–3.7B, central about $2.3B, vs Street $1,502M. The Street Q3 change in contract liabilities: median about zero, highest +$1.9B.

### 3.4 Attacks

| Attack | Evidence | Effect |
|---|---|---|
| Management said H1 FCF "substantially higher than the second half, as many of these slot reservations convert to orders" | Q2 2026 call | Consistent with H2 of $3–6B against H1 of $9.9B; also consistent with the guide |
| Cash taxes on deposits | Cash taxes paid: FY25 $830M; H1 2026 $1,258M (H1 2025 $363M). Cause not disclosed; tax treatment of reservation fees not found in the filings | If deposits are taxed the year after receipt, H2 2026 and FY27 cash taxes rise. Open item; it lowers FY27 more than FY26 |
| Q4 receivables build | Receivables +$2.4B in Q4 2025 while contract liabilities rose $5.6B (billed, not yet collected) | A late-December signing rush moves cash into Q1 2027; k for H2 2025 was 0.32 |
| Other outflows | Vineyard Wind settlement (2026-09-16; amount not found), supplier commitments, inventory for the 6 GW a quarter step | Unsized |
| Market reaction | Q2 2026: FCF $5.1B vs about $1.2B expected, guide +$5B, stock −8.7% on the day | A deposit-driven cash beat has not moved the stock by itself |
| Pull-forward | Street FY27 FCF already falls 37% | A higher FY26 can mean a lower FY27 if 2027 signings slow |
| MODL contributor count | Not visible for the contract-liability rows | The Street "flat deposits" figure may rest on few brokers |

### 3.5 Reveal dates

| Date | Number | Comparator |
|---|---|---|
| 2026-10-28 | Q3 FCF; contract liabilities at 9/30; GW signed; FY26 FCF guide | Street Q3 FCF $1,502M; balance $39.9B median; guide $11.5–12.5B |
| late Jan 2027 | FY26 FCF; FY27 FCF guide; cumulative 2025–28 outlook (now "at least $24B": 2025 actual 3.7 + 2026 guide 11.5–12.5 leaves only $7.8–8.8B for 2027–28 vs Street $17.2B) | Street FY26 $12,196M; FY27 $7,654M |

---

## 4. Instance C — the once-a-year backlog-margin number

Not a Bloomberg line. The only public anchor is the management floor.

| Input | Value | Source |
|---|---|---|
| Equipment margin added to backlog, 2023 + 2024 | more than $6B | Q4 2024 call |
| 2025 | $8B, +6 pts (Power +11, Electrification +3, Wind −2) | Q4 2025 release and call, deck slide 5 |
| 2026 expectation | "at least as much … as in '25"; "a floor with an opportunity for it to be substantially higher"; Power change in 2026 larger than in 2025 | Q4 2025 call; Q1 2026 call; Laguna 2026-09-16 |
| Next disclosure | January 2027 call | Laguna |
| Equipment orders FY25 | 64,245 − 43,047 + 20,934 = $42,132M | RPO roll |
| Equipment orders H1 2026 | total orders 18.3 + 24.2 = 42.5B less services orders (8,729 + 2,470) = $31,301M; the RPO roll gives 35,289, so the acquired Prolec backlog is about $4.0B | releases, 10-Q |
| Equipment orders H2 2026 | Street orders 20,332 + 25,071 = 45,403 less services orders 11.5–12.6B = $32.8–33.9B | Bloomberg, 2026-10-01 |

| Reading (S01 defines both) | Formula | 2026 result |
|---|---|---|
| Flow: margin on the orders of the year | 2025 rate = 8,000 ÷ 42,132 = 19.0%. FY26 orders $64.1–65.2B × 19.0% | $12.2–12.4B |
| Flow with the gas price step | gas orders about 58% of the total; +20% price on a 20% margin lifts it to 33%; blended about 26.7% | $17.1–17.4B |
| Stock: change in (equipment RPO × average margin) | YE25 margin 25.6% (21.7–28.9% for rounding); YE26 RPO about 87,821 + 33.3B − 15.8B = about $105B; 2026 change +7.0 to +9.4 pts (Power 12–15 × 45%, Electrification 3–5 × 46%, Wind 2–4 × 9%) | $16.1–22.0B |
| By 6/30/26, stock reading at +3 to +5 pts | (25.6% + change) × 87,821 − 16,447 | $8.7–10.4B already |

Range $12–22B against a floor of $8B. Direct value of each extra $8B: about $30 a share before tax, spread over deliveries to 2031, so the number matters through 2029–2030 estimates, not by itself. Street 2029 EBITDA has already risen from $12,958M (2026-01-02) to $16,496M.

---

## 5. Instances that showed no gap

### 5.1 Gas output ladder × price (physical quantity)

Management ladder: 5 GW a quarter in Q3 and Q4 2026, "the beginning of next year will feel generally very similar", 6 GW a quarter "sometime in the second half of next year", "may be at six gigawatts for a period of time" in 2028 before 7 (Laguna); 30 GW in 2030 (Q2 2026 call). Taken as 22 / 25 / 28 / 30 GW for 2027–2030.

| Year | Street Power equipment $M | GW | Street $ per kW shipped | Order price of the vintage likely shipping |
|---|---|---|---|---|
| 2027 | 12,151 | 22 | 552 | H1 2025 orders: $547 |
| 2028 | 15,888 | 25 | 636 | H2 2025 orders: $697 |
| 2029 | 19,256 | 28 | 688 | H1 2026 orders: $916 |
| 2030 | 23,469 | 30 | 782 | H2 2026 orders: "higher end of 10–20 points" above Q4 2025 |

Why it fails: revenue per GW shipped does not track order price. Power equipment revenue ÷ GW shipped by quarter (Q1 2025 to Q2 2026): $497, $289, $436, $628, $449, $595; correlation of revenue with GW shipped −0.37. Revenue per GW vs the order price about two years earlier: FY25 $437 vs FY23 $602 (0.73); H1 2026 $513 vs FY24 $408 (1.26). At 1.0 the 2029 figure would be 28 × 916 = $25.6B (+33% vs Street); at 0.75 it equals Street. The band is wider than the gap. Street estimates did not move after Laguna (FY27 revenue 52,951 on 09-11, 53,029 on 10-01; FY28 60,838 to 60,985).

### 5.2 Wind deliveries vs orders

| Half | Orders GW (turbines + repower units) | Sales GW one year later | Ratio (turbine units) |
|---|---|---|---|
| H1 2024 | 2.5 (621 + 246) | H1 2025 3.0 (627 + 286) | 1.01 |
| H2 2024 | 2.8 (591 + 410) | H2 2025 3.9 (891 + 303) | 1.51 |
| H1 2025 | 1.8 (404 + 205) | H1 2026 2.0 (490 + 27) | 1.21 |
| H2 2025 | 3.1 (450 + 403) | H2 2026 Street 3.28 | — |
| H1 2026 | 1.2 (293 + 49) | H1 2027 Street 1.88 (694 + 1,188 MW) | Street needs about 1.57 on GW |

Sources: 10-K FY25 p.26, 10-Q Q2 2026 p.30, 10-Q Q2 2025 p.29; management: "70% of 2025 equipment orders were in the second half and will be delivered in the second half of 2026". Estimate for H1 2027: 293 turbines × 1.0–1.5 × about 4 MW = 1.2–1.8 GW plus repower and offshore 0.1–0.3 GW = 1.3–2.1 GW vs Street 1.88 GW. Street sits inside the band. Effect if deliveries were 1.4 GW: Wind revenue about −$0.5B, EBITDA about −$0.1B in H1 2027 (about 2–3% of company H1 2027 EBITDA of $4,039M). Useful as a risk line; Q3 and Q4 wind orders (10-28, late January) narrow it.

### 5.3 Street gross margin vs backlog contribution margin

Street gross profit = BEST_GROSS_MARGIN × BEST_SALES: 10,737 / 14,344 / 17,771 / 22,786 / 26,349 (2026–2030). Less services revenue (Street segment sums 18,835 / 20,885 / 23,297 / 25,847 / 28,998) at a 32–34% services gross margin (FY25 31.3%, H1 2026 31.6%) gives implied equipment gross margin 15.8–17.2% / 22.5–23.8% / 26.1–27.4% / 31.1–32.3% / 32.5–33.7%. Reported: 10.4% FY25, 11.8% H1 2026, 13.1% Q2 2026. Backlog contribution margin: 25.6% at YE25 on the stock reading or about 16.5% on the flow reading; reported gross margin has run 4–17 points below it (S01). The two readings bracket the Street path; no gap can be shown.

### 5.4 LTSA estimate changes

Contract-assets note: net unfavourable changes in estimated profitability of $319M (FY24), $151M (FY25), $42M (H1 2025), $218M (H1 2026) (`LTSA_ProfitRevision`; 10-Q Q2 2026, 10-K FY25). Power margin expanded with these included. H1 2026 Power margin 17.6% would be 19.7% without the $218M. Recurring in every period, so it is not a one-off to add back.

### 5.5 FY27 FCF

Deposits in 2027 = GW of new reservations × price × 25% plus progress payments less deposits released on about 22 GW shipped. At 30–40 GW of new reservations the result is near Street ($7.65B); at 20 GW about $5.5B; at 50 GW about $10B. Management: "in '27, we expect our combined gigawatts under contract to continue to grow"; 2032 slots sold "in single-digit gigawatts" so far. Not identifiable.

### 5.6 Other checks

| Check | Result |
|---|---|
| Street vs FY26 guide by division | Power 18.6% (guide 17–19), Electrification 19.4% (18–20), Wind −$445M (about −$400M): inside |
| Q3 guide-implied EBITDA | about $1,540–1,680M vs Street $1,672M |
| EPS FY27 rebuilt from Street EBITDA with Q2 2026 run-rates (D&A $418M a quarter, tax 24%, 266M shares) | about $24.1 vs Street $24.52 |
| Contract liabilities vs backlog and reservation GW (two-variable fit, six quarters) | coefficients unstable (backlog $62–753/kW; reservations −$40 to +$314/kW) |
| Siemens Energy Gas Services FY28 target 18–20% vs Street GEV Power 23.3% | different margin definitions; context |

---

## 6. Playbook tests

| Test | A: equipment revenue Q3 2026 to Q2 2027 | B: FY26 FCF |
|---|---|---|
| 1 Line item | Yes: equipment revenue; Street 30,245 | Yes: FCF; Street 12,196 |
| 2 Consensus side | Yes: consensus line | Yes: consensus equals the guide |
| 3 Distance | +4.5% floor; +7.5% to +15.5% with history; total revenue +3% to +7% | +19% central; −1% to +34% |
| 4 Ratio | Revenue only; return would rest on the multiple | Cash only; same |
| 5 Physical quantity | Bottom-up capacity gives Street to +5% | GW signed × $/kW × 25% |
| 6 Rival explanation | Broker split; slippage; wind orders | Receivables timing; cash taxes; settlement |
| 7 Error band | Std dev 5.9% (7 windows) or 2.8% (6) vs gap 4.5–9.8% | Band about ±$2B vs gap $2.3B: marginal |
| 8 Why missed | Percentages sit in the RPO note; no Bloomberg field; models use GW × price and guides | Deposit terms appear in one conference remark; Street follows a guide that has implied near-zero deposits for the remainder each time |
| 9 Already priced | Three revenue-guide raises in 2026; another may be expected | Guide raised three times in 2026 |
| 10 Cash | EBITDA +2% to +8% at most | Yes, FCF; little effect on EBITDA |
| 11 Reveal | 10-28 (9/30 schedule), late Jan (12/31 schedule, FY27 guide), Apr/Jul 2027 | 10-28 (Q3 FCF, deposits), late Jan |
| 12 Counter-move | Deliveries slip; customers not ready on site | Supplier prepayments; cash used for buybacks or M&A |
| 13 Multiple | Not addressed by this lens | Not addressed |

## 7. Hand-checks before use

- Re-read the seven RPO sentences in the filings and re-add the four quarters after each date.
- Confirm the 12/31/23 schedule basis (S-1) and the EDF-related equipment RPO removed in 2024.
- Open EEB or MODL on a terminal for broker-level equipment / services and for the contributor count on contract liabilities.
- Find the cash-tax treatment of reservation fees (10-K income-tax note) and the Vineyard Wind settlement amount.
- Re-compute Power product contract liabilities by quarter from the segment note.
