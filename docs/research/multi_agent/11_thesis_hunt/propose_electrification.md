# Thesis hunt — Electrification lens (2026-10-01)

_AI-assisted research input only: facts, arithmetic, tables and sources. The team writes every memo sentence, chooses every forecast number and chooses the direction. Bloomberg figures are licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep inside the project folder._

Method: number-first. For each Electrification line the Street publishes, rebuild it from GEV's filings and compare. "Street" = Bloomberg BEst mean unless stated. $M unless stated.

## 0. Result in six lines

1. **No Electrification line shows a gap of 7% or more that is tighter than its own error band.** The Street's Electrification model matches the filings to within about 5% on every line tested for H2'26 and FY27.
2. The lean is on the long side and small: next-four-quarter revenue about +4% (range +1.5% to +7%), FY27 segment EBITDA 0% to +6%.
3. The sharpest single quarter is **Q1'27 revenue: Street $3,671M implies +13% to +17% organic growth, against +18.5% and +22.6% in the quarters on either side.** Rebuilt: $3.72–3.96B, central about $3.80–3.85B (+3.5% to +4.8%). That is under the 5% bar once Prolec's weaker first quarter is allowed for. **No candidate is returned from this lens.**
4. The order-vintage arithmetic brackets the Street's FY27 margin (20.6–22.9% vs 21.3%) and sits above it later: 2029 about 26.5% vs 24.6% (+8% on segment EBITDA), but the band is -3% to +18%.
5. One correction to the team's surviving equipment-conversion test: Bloomberg's Electrification **services** line is too high by about $0.33–0.48B over the four quarters, so the Street's **equipment** line is too low by a similar amount. The no-uplift gap falls from $1.37B (4.5%) to about $1.0B (3.3%).
6. Two below-the-line items: Street amortisation is about $60–70M a quarter too low through January 2028 (Q3'26 EPS effect about -3%); Prolec's margin inside GEV is 22.0%, not the 25% in the deal release.

## 1. Sources and cells

| Tag | Source |
|---|---|
| BBG-Q | `data/bloomberg/GEV_Pull_2026-10-01/01..05-eeo-company-specific.xlsx`, rows 29–31 (revenue, equipment, services), 36 (EBITDA), 42 (margin), 52 (D&A), 68 (orders), 73 (RPO), 78 (adjusted EBITDA), 91–94 (product lines); same data in `segment_quarterly.json`, keys of the form "Total Revenue / Electrification / YYYY Qn" |
| BBG-M | `06_modl.xlsx` (Q3'26 only): row 29 mean 3,880.7 / low 2,995.0 / high 4,049.7 / median 3,936.8; row 36 EBITDA mean 745.2 / median 747.9; row 52 D&A mean 161.7 / median 230; row 67 orders mean 6,498 / median 6,307 |
| BBG-A | `01_eeo_annual.xlsx`: Depreciation Q3'26 185.3 (12 analysts), Amortization 166.8 (11); Q4'26 195.5 / 176.5; Q1'27 220.3 / 181.9; Q2'27 238.6 / 180.6; EBIT Q3'26 1,295.5 (24); EBITDA 1,671.8 (26); EPS 4.04 (27) |
| 10Q2 | 10-Q for Q2'26, accession 0001996810-26-000148: Note 8 (acquisition), Note 24 (segments), MD&A segment tables, non-GAAP organic table |
| 10Q1 | 10-Q for Q1'26, accession 0001996810-26-000064 |
| 10K25 | 10-K FY2025, accession 0001996810-26-000015, Note 24 segment expense table (2023–2025) and MD&A |
| R | Earnings releases (8-K exhibits) Q1'24–Q2'26: segment table with orders, cost of revenues, SG&A, R&D, other segment items; guidance bullets |
| T2Q26 | Q2'26 call transcript, corpus `sources.id=3161` |
| T3Q25 / T4Q25 | Q3'25 call (corpus `sources.id=3771`), Q4'25 call (`sources.id=2660`) |
| DEAL | Prolec deal release 2025-10-21 (corpus `sources.id=3761`) |
| LAG | September 2026 investor-conference write-up (corpus `sources.id=681`) and FACTS.csv RQ-23 (verified quote) |
| SE | Siemens Energy Q3 FY26 earnings release and analyst deck (corpus `sources.id=3166, 3167`) |

## 2. The Street's Electrification model (BBG-Q)

| Quarter | Revenue | Equipment | Services | EBITDA | Margin | Orders | RPO |
|---|---|---|---|---|---|---|---|
| Q2'26 actual | 3,637 | 3,130 | 507 | 671 | 18.4% | 6,347 | 44,563 |
| Q3'26 | 3,881 | 3,299 | 552 | 745 | 19.2% | 6,498 | 46,998 |
| Q4'26 | 4,289 | 3,479 | 812 | 917 | 21.4% | 7,492 | 50,252 |
| Q1'27 | 3,671 | 3,071 | 629 | 725 | 19.7% | 8,475 | 55,157 |
| Q2'27 | 4,304 | 3,692 | 696 | 885 | 20.6% | 6,782 | 57,559 |
| Q3'27 | 4,649 | 3,910 | 830 | 987 | 21.2% | 7,420 | 60,283 |
| Q4'27 | 5,080 | 4,196 | 963 | 1,156 | 22.8% | 8,981 | 64,222 |

| Year | Revenue | EBITDA (adjusted line) | Margin | Orders | Year-end RPO |
|---|---|---|---|---|---|
| 2026 (H1 actual + Street H2) | 14,765 | 2,862 (EBITDA line) / 2,723 (adjusted line) | 19.4% / 18.4% | 27,450 | 50,252 |
| 2027 | 17,704 | 3,774 | 21.3% | 31,657 | 64,222 |
| 2028 | 21,270 | 4,972 | 23.4% | 36,060 | 78,028 |
| 2029 | 24,959 | 6,130 | 24.6% | 40,580 | 94,988 |
| 2030 | 28,422 | 7,264 | 25.6% | 44,941 | 109,309 |

Notes:
- Bloomberg carries two segment profit lines ("EBITDA" and "Adjusted EBITDA"). They differ by 9% in Q3'26 and Q4'26 (745 vs 681; 917 vs 843) and agree from 2027. The "EBITDA" line sums to the company consensus, so it is used for 2026.
- The Q3'26 mean is pulled down by one stale low ($2,995M). The median is $3,937M.
- GEV's guide: FY26 revenue $14.5–15.0B including about $3.1B Prolec, margin 18–20%; Q3'26 revenue $3.8–4.0B, margin "modestly above" 18.4% [R Q2'26; T2Q26]. 2028 framework: high-teens organic growth a year plus about $4B Prolec, 22% margin [R Q4'25]. An analyst on the Q2 call put that at "$20 billion" for 2028 and the CEO agreed [T2Q26]. The Street's 2028 is $21.3B and 23.4%.

## 3. What the filings give

### 3.1 Segment profit and loss by cost line (R; 10K25 Note 24)

| Period | Revenue | Cost of revenues | SG&A + R&D | Other segment items | EBITDA | Gross margin | Opex / revenue | Margin | Margin ex other items |
|---|---|---|---|---|---|---|---|---|---|
| FY23 | 6,378 | 4,690 | 1,533 | (79) | 234 | 26.5% | 24.0% | 3.7% | 2.4% |
| FY24 | 7,550 | 5,359 | 1,640 | (128) | 679 | 29.0% | 21.7% | 9.0% | 7.3% |
| FY25 | 9,642 | 6,644 | 1,776 | (212) | 1,433 | 31.1% | 18.4% | 14.9% | 12.7% |
| Q1'25 recast | 1,840 | 1,272 | 412 | (49) | 205 | 30.9% | 22.4% | 11.1% | 8.5% |
| Q2'25 recast | 2,162 | 1,505 | 406 | (64) | 314 | 30.4% | 18.8% | 14.5% | 11.6% |
| Q3'25 | 2,601 | 1,824 | 451 | (67) | 393 | 29.9% | 17.3% | 15.1% | 12.5% |
| Q4'25 | 2,960 | 2,019 | 468 | (32) | 505 | 31.8% | 15.8% | 17.1% | 16.0% |
| Q1'26 | 2,959 | 2,027 | 461 | (57) | 528 | 31.5% | 15.6% | 17.8% | 15.9% |
| Q2'26 | 3,637 | 2,512 | 453 | 1 | 671 | 30.9% | 12.5% | 18.4% | 18.5% |

- Costs exclude depreciation and amortisation. "Other segment items" is mainly equity-method income from the Prolec joint venture plus interest and investment income. The joint-venture income was $17M / $93M / $105M in 2022 / 2023 / 2024 [DEAL footnote b]. It stopped on 2026-02-02.
- **Segment gross margin has been flat at 30–32% for six quarters.** The margin gain since Q1'25 came from operating costs falling from 22% to 12.5% of revenue, less the loss of the joint-venture income.

### 3.2 Prolec and the organic business (10Q1 and 10Q2, organic reconciliation table)

| | Revenue | EBITDA | Margin |
|---|---|---|---|
| Q1'26 acquisitions (Prolec, two months) | 486 | 112 | 23.0% |
| Q2'26 acquisitions (Prolec) | 860 | 183 | 21.3% |
| H1'26 acquisitions | 1,346 | 296 | **22.0%** |
| Q1'26 organic | 2,318 | 338 | 14.6% (Q1'25 8.7%) |
| Q2'26 organic | 2,727 | 522 | 19.1% (Q2'25 12.1%) |
| H1'26 organic | 5,045 | 860 | 17.0% (H1'25 10.5%) |

- Other reconciling items: Q1'26 dispositions 26 revenue / 54 EBITDA and currency 129 / 24; Q2'26 currency 50 / (34). H1'25 dispositions 82 revenue / 100 EBITDA: the EBITDA is larger than the revenue because the removed joint-venture income had no revenue attached.
- Organic incremental margin: H1'26 (860 - 410) / (5,045 - 3,906) = 39.5%; Q2'26 268 / 621 = 43.2%. FY24 38.0%, FY25 36.0% on reported figures.
- Deal release: Prolec "$3B in revenue at ~25% adjusted EBITDA margin in 2025", EBITDA above $1B in 2028 before synergies, "incremental $800 million" to GEV in 2028 [DEAL; T3Q25]. Inside GEV the margin has been 22.0%. The CFO said "just over 20%" for February–March (corpus `sources.id=1849`).
- Purchase accounting (10Q2 Note 8): consideration $9,656M; intangibles $4,172M = customer $2,860M (12 years), technology $533M (6), software $8M (3), **trademarks and other $771M (2 years)**; goodwill $5,313M. Inventory step-up charged to cost of equipment: $106M in H1'26 (Q2 $35M), excluded from adjusted EBITDA. Prolec loss before tax from closing to 6/30/26: $(166)M.

### 3.3 Backlog, orders, customer advances

| Date | Equipment RPO | Services RPO | Orders in quarter | Contract liabilities | Contract liabilities / equipment RPO |
|---|---|---|---|---|---|
| 12/31/22 | 6,384 | 2,587 | | | |
| 12/31/23 | 13,233 | 3,109 | | 2,500 | 18.9% |
| 6/30/24 | 17,540 | 3,139 | 4,823 | 3,278 | 18.7% |
| 12/31/24 | 20,005 | 3,448 | 4,786 | 4,050 | 20.2% |
| 6/30/25 | 23,950 | 3,168 (recast) | 3,283 (recast) | 5,175 | 21.6% |
| 9/30/25 | 26,455 | 3,725 | 5,110 | 5,268 | 19.9% |
| 12/31/25 | 30,508 | 3,734 (recast) | 7,424 | 6,462 | 21.2% |
| 3/31/26 | 38,598 | 3,842 | 7,112 | 8,269 | 21.4% |
| 6/30/26 | 40,589 | 3,974 | 6,347 | 9,124 | 22.5% |

- Both 2026 quarters say the equipment backlog includes "$5 billion from Prolec GE" [R]. Legacy equipment RPO at 6/30/26 is therefore about $35.6B, up 49% in a year.
- Data-centre orders: about $2B in 2025; $2.4B in Q1'26; $2.7B in Q2'26; "more like 20%" of segment orders in Q3 and Q4 [T2Q26; LAG].

## 4. Tests

### T1. Revenue against the guide (H2'26)

- Guide-implied H2'26: $14.5–15.0B less H1 $6,597M = $7,903–8,403M, midpoint $8,153M. Street H2: $8,169M. **The Street is on the midpoint.**
- Legacy (ex-Prolec) H2'26 at the guide: $6,149–6,649M against a comparable H2'25 base of about $5,395M = +14% to +23%, midpoint +18.6%. H1'26 organic growth was +29%. Two-year stack: H1'26 about 48–49%; H2'26 at the guide midpoint about 51%. So the guide is not a slowdown on a two-year view.
- Back-test of the July guide (R):

| Year | July guide | July-implied H2 | Actual H2 | Beat |
|---|---|---|---|---|
| 2024 | mid-to-high-teens organic (17% used) | 4,021 | 4,109 | +2.2% |
| 2025 | about 20% organic | 5,102 | 5,562 | +9.0% |
| 2026 | $14.5–15.0B | 8,153 | Street 8,169 | |

- The October guide was then within 1–3% of the Q4 actual (+1.1% in 2024, +2.7% in 2025). The one quarter-ahead revenue guide found for 2026 was exact (Q1'26 "similar to Q4'25" $2,960M; actual $2,959M).
- FY26 revenue guide history: $13.5–14.0B (January) → $14.0–14.5B (April) → $14.5–15.0B (July). Two raises of $0.5B.
- Applying the two beats to 2026: H2 $8,332–8,887M, +2.0% to +8.8% vs the Street, central +5.4%. Two data points only.

### T2. Backlog conversion

Next-four-quarter equipment revenue (segment basis, ex-Prolec) divided by opening equipment RPO:

| Window opens | Equipment RPO | Next 4Q equipment revenue | Ratio | Basis |
|---|---|---|---|---|
| 12/31/22 | 6,384 | 4,532 | 71.0% | reported |
| 12/31/23 | 13,233 | 5,534 | 41.8% | reported |
| 6/30/24 | 17,540 | 6,082 | 34.7% | reported |
| 12/31/24 | 20,005 | 7,378 | 36.9% | reported |
| 3/31/25 | 21,996 | 8,018 | 36.5% | reported |
| 6/30/25 | 23,950 | 8,641 | 36.1% | reported |
| 9/30/25 | 26,455 | 9,006–9,206 | 34.0–34.8% | Q3'26 at the guide |
| 12/31/25 | 30,508 | 9,198–9,898 | 30.1–32.4% | H2'26 at the guide |
| 6/30/26 | 35,589 legacy | 10,091 (Street) | 28.4% | all Street; Prolec taken as $850–880M a quarter |

- The Street's 28.4% is the lowest on record, but the guide itself already takes the ratio from 36% to about 31% in two quarters. Backlog (+49%) is growing faster than output. The ratio is a result of the growth rate, not an independent check.
- Sensitivity: 30% gives +4.3% on the Street's equipment line; 31% gives +7.0%; 32% gives +9.6%.
- Peer: Siemens Energy Grid Technologies, June-2026 quarter: revenue €3,624M (+28.6% comparable), backlog €51B. Annualised revenue / backlog = 28.4%. Its FY26 guide is +25–27% comparable growth and an 18–20% margin after depreciation (EBITDA margin 20.6% in the quarter) [SE].
- Legacy equipment growth: last four quarters $8,641M vs $6,082M = +42%. Street next four quarters: +16.8%. Guide-implied H2'26: about +21%.

### T3. Capacity

- Air-insulated switchgear: about 9,000 units in 2025, about 10,500 planned for 2026 (+17%), "growth to accelerate in '27"; about $5B of backlog [T2Q26].
- Transformers and switchgear output to double from 2024 to 2028 (about +19% a year) [T4Q25].
- The July raise was "due to accelerated output on our capacity plans and better Prolec revenue" [T2Q26]. September: "greater-than-expected potential to expand production from the acquired factories with modest capital expenditures" [LAG].
- Segment capital spending: $273M in 2025; $192M in H1'26 excluding $942M of acquired Prolec plant; Q2'26 $97M including Prolec (10Q2 Note 24). Street: about $100–127M a quarter.
- Reading: units +17–20% a year plus price and mix. Reported organic growth has run 9–12 points above unit growth. The Street's FY27 legacy growth (about +20%) equals unit growth plus about 0–3 points of price.

### T4. Margin, built from cost lines

| Item | Assumption | Result | Street | Gap |
|---|---|---|---|---|
| Q3'26 | revenue $3.8–4.0B; gross margin 30.5–31.2%; opex $460–470M | $689–788M (18.1–19.7%) | 745 | in range |
| Q4'26, cost lines | Street revenue; gross margin 31.5–32.2% (Q4 ran 0.4–0.7 pt above the year in 2024 and 2025); opex $489–507M | $844–892M (19.7–20.8%) | 917 | -3% to -8% |
| Q4'26, margin seasonality | Q2-to-Q4 uplift ex other items was +3.8 pts (2024) and +4.4 pts (2025) | $957–983M | 917 | +4% to +7% |
| FY27, cost lines | Street revenue $17,704M; gross margin 31.5–33.0%; opex $1,876M (FY26E) +5–10% | $3,513–3,873M (19.8–21.9%) | 3,774 | -6.9% to +2.6% |
| FY27, incremental margin | legacy revenue +$2.34B at 33–43%; Prolec +$0.6B at 25%; FY26 base $2,788–2,862M | $3,695–4,002M (20.9–22.6%) | 3,774 | -2.1% to +6.1% |

- The two Q4 methods bracket the Street. The two FY27 methods bracket the Street. **No gap.**
- The Street's FY27 needs a gross margin of about 32.7% (opex +7.5%), against 31.2% in H1'26. Estimated legacy gross margin is already about 32% (Prolec assumed at 27%).
- Street-implied gross margin if opex grows 7% a year: 32.7% (2027), 33.5% (2028), 33.8% (2029), 34.2% (2030). Opex falls to 8.7% of revenue by 2030.
- Operating leverage is fading by arithmetic: at 12.5% of revenue, 20% growth with opex +8% adds about 1.3 points a year, against 3–6 points a year in 2024–H1'26.

### T5. Order-vintage arithmetic (pricing in backlog)

Inputs: equipment RPO at each year-end (section 3.3); equipment revenue $4,532M / $5,534M / $7,378M (2023–25); the company's disclosed change in average contribution margin of the Electrification equipment backlog: +5 / +4 / +3 points (2023 / 2024 / 2025) and "something similar… maybe a little bit larger" for 2026 (S01 table, slide and conference sources). Solve for the margin on each year's orders, in points above the year-end-2022 backlog average:

closing RPO × closing margin = sum(remaining cohorts × margin) + orders × order margin

| Orders booked in | First-in-first-out burn | Proportional burn |
|---|---|---|
| 2023 | +5.8 | +5.8 |
| 2024 | +11.0 | +11.5 |
| 2025 | +12.8 | +14.1 |
| 2026 (+3.0 to +3.5 on the backlog; legacy equipment orders about $20B) | +17.6 to +18.6 | +18.1 to +19.2 |

Margin on equipment revenue recognised each year, points above the same base:

| | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|---|---|---|
| First-in-first-out | 0.0 | 3.9 | 5.8 | 10.8 | 12.3 | 14.3 | 17.6 | 17.6 |
| Proportional | 0.0 | 5.0 | 9.0 | 12.0 | 15.0 | 16.2 | 17.0 | 17.5 |

Back-test against reported equipment gross margin (services gross margin assumed 42%; Prolec 27%): FY23 20.1%, FY24 24.3% (+4.2), FY25 27.8% (+3.5), H1'26 legacy about 30.2% (+2.4 vs FY25; +3.1 year on year). Model: +3.9 to +5.0, +1.9 to +4.0, +3.0 to +5.0. Cumulative FY23 to H1'26: reported about +10 points against +10.8 to +12.0. Pass-through about 0.85–0.95.

Forward, change from 2026:

| | 2027 | 2028 | 2029 |
|---|---|---|---|
| Equipment margin gain (both burn methods) | +1.5 to +3.0 | +3.5 to +4.2 | +4.3 to +7.8 |
| Segment margin: FY26 base 18.9–19.4%, plus gain × pass-through 0.85–0.95 × legacy equipment share 0.64–0.71, plus Prolec (+0 to +0.7), less mix (-0.1 to -0.4), plus opex leverage (opex +5% to +10% a year) | 20.6–22.9%, central about 21.8% | 22.7–25.3%, central about 24.0% | 23.7–29.0%, central about 26.5% |
| Street | 21.3% | 23.4% | 24.6% |
| Segment EBITDA vs Street | -3% to +8% | -3% to +8% | -3% to +18%, central about +8% ($6.6B vs $6.13B) |

- 2027 and 2028: the arithmetic brackets the Street. 2029: central above it, but the band crosses zero.
- Added to the earlier Power vintage base ($10.9B vs Street $9.98B), the 2029 company total would be about $17.7B against $16.5B (+7%), with wide bands on both parts.

### T6. Prolec purchase accounting against the Street's amortisation

- Schedule: 2,860/12 + 533/6 + 8/3 + 771/2 = **$715M a year, $179M a quarter**. Legacy amortisation about $57–60M a quarter (Q2'25 total $60M). Total about $238M a quarter; actual Q2'26 $236M, Q1'26 $175M with two months of Prolec (10Q2 Note 8).
- The $771M two-year item ends in January 2028; amortisation then falls by about $96M a quarter to about $142M.
- Street amortisation (BBG-A): 166.8 / 176.5 / 181.9 / 180.6 for Q3'26–Q2'27: **about $56–71M a quarter too low**. Street depreciation 185 / 196 / 220 / 239 against $182M actual in Q2'26.
- Q3'26: EBITDA 1,672 less EBIT 1,296 = implied D&A of $376M, against $418M reported in Q2. At $418–428M, EBIT is 3.2–4.0% below the Street and EPS is about $3.90–3.93 against $4.04 (-3%), if EBITDA is in line.
- Segment D&A (BBG-M): mean 161.7 but median 230 (actual Q2 230). The median analyst is right; the mean is polluted by a stale $23M.
- Size: under the 5% threshold. It is a print-day note for 2026-10-28, not a wedge. In Q2'26 EPS missed by about 19% with revenue ahead.

### T7. The Street's equipment / services split, and the team's conversion test

- Electrification services, actual: 448 / 488 (Q1, Q2'25 recast), 566 / 681 (Q3, Q4'25, old basis), 459 / 507 (Q1, Q2'26). H1'26 growth +3.1%.
- Street services next four quarters: 552 + 812 + 629 + 696 = $2,689M, +22% to +26% on the last four quarters ($2,135–2,213M).
- At +3% to +10% growth, services are $2,208–2,358M. **The Street's services line is $331–481M too high, so the equipment consistent with the Street's total ($16,145M) is $13.79–13.94B, not $13,541M.**
- Effect on the surviving company-wide test (schedule $31,616M; rounding band $31,176–32,055M):

| | Street equipment | Gap to schedule | Gap % |
|---|---|---|---|
| As in BLOOMBERG_VERDICT §10 | 30,245 | 1,371 | 4.5% |
| After the services correction | 30,545–30,685 | 931–1,071 | 3.0–3.5% |

- Power services on the Street grow 10.8% over the same window against 5.8% in H1'26; a similar but smaller artefact may sit there. The total-revenue version of the test is not affected.
- If H2'26 equipment lands on the Street ($15,821M, consistent with the guide), the schedule leaves $15,795M for H1'27: +34.8% on H1'26 ($11,713M), against the Street's $14,424M (+23.1%). The whole gap sits in H1'27.

### T8. Q1'27 revenue (closest to a candidate; fails the 5% bar)

Legacy growth implied by the Street, quarter by quarter (Prolec taken as $880–900M a quarter; Proficy removed from the base; H2'25 on the recast basis):

| Quarter | Street revenue | Legacy | Comparable base | Legacy growth | Two-year stack |
|---|---|---|---|---|---|
| Q3'26 | 3,881 | 3,001 | 2,521 | +19.0% | about 51% |
| Q4'26 | 4,289 | 3,409 | 2,876 | +18.5% | about 51.5% |
| **Q1'27** | **3,671** | **2,771–2,791** | 2,447 | **+13.2% to +14.0%** (+12.1% to +12.9% on the unadjusted base of 2,473) | about 43% |
| Q2'27 | 4,304 | 3,404–3,424 | 2,777 | +22.6% to +23.3% | about 52% |

- Bases: Q3'25 recast $2,564.8M less about $44M Proficy; Q4'25 recast is an estimate ($2,960M less about $40M, the recast figure was not found) less $44M; Q1'26 $2,959M less Prolec $486M less Proficy $26M; Q2'26 $3,637M less Prolec $860M. Prior-year organic growth for the stack: +32% (Q3'25), about +32% (Q4'25, backed out of the +26% full year), +29% (Q1'26), +29% (Q2'26).
- Q1'26 held only two months of Prolec ($486M). On reported figures the Street's Q1'27 is +24.1%, which reads like the trend. After adding the missing January it is about +13%.
- Prolec's first-quarter level is the swing input. February–March 2026 ran $8.38M a day ($486M over 58 days); Q2'26 ran $9.45M a day ($860M over 91 days), 13% higher. The H2'26 guide implies about $877M a quarter. For Q1'27: the February–March daily rate for 90 days plus 8–12% growth gives $814–845M; the H2'26 run-rate gives $876M; $900M is the top of the range.
- Street-implied legacy growth in Q1'27 by Prolec assumption: +16.7% ($815M), +15.3% ($850M), +14.2% ($876M), +13.2% ($900M). The dip against the neighbouring quarters is 2 to 9 points, not a fixed 6.
- Seasonality check: legacy Q1 has been 0.836–0.847 of the prior Q4 in three years. On the Street's own Q4'26 legacy ($3,409M) that gives $2,850–2,887M plus Prolec $815–900M = $3,665–3,787M (-0.2% to +3.2%).
- Rebuild grid (Q1'27 revenue, $M, and % vs Street $3,671M):

| Legacy growth | Prolec $815M | Prolec $850M | Prolec $900M |
|---|---|---|---|
| +18.5% (the Street's Q4'26 rate) | 3,715 (+1.2%) | 3,750 (+2.1%) | 3,800 (+3.5%) |
| +20.5% (average of the Street's Q4'26 and Q2'27 rates) | 3,764 (+2.5%) | 3,799 (+3.5%) | 3,849 (+4.8%) |
| +22.5% (a 51.5% two-year stack) | 3,813 (+3.9%) | 3,848 (+4.8%) | 3,898 (+6.2%) |
| +25% | 3,874 (+5.5%) | 3,909 (+6.5%) | 3,959 (+7.8%) |

- Central: about $3.80–3.85B, +3.5% to +4.8%. Full range +1.2% to +7.8%.
- Profit effect at a 31–33% drop-through: +$15–95M, central about +$45M, against Street Q1'27 segment EBITDA of $725M (+6%) and company EBITDA of $1,810M (+2.5%).
- Other weak points: the Q1'27 mean may hold a stale low as Q3'26 does (mean 1.4% under the median there); broker detail for Q1'27 was not exported; fewer brokers supply quarters.
- Where it would show: GEV has given a quarter-ahead Electrification revenue range on recent calls (Q1'26 on the January call; Q3'26 on the July call). A Q1'27 range on the late-January 2027 call with a midpoint of $3.8B or more would sit above the Street.

### T9. Orders (no usable gap)

- Street Q3'26 orders $6,498M (median $6,307M; low $5,775M; high $7,498M) [BBG-M].
- If data centres are 20% of orders and the rest holds the H1'26 pace ($4.2B a quarter), orders are $5.3B (-18%). If the rest repeats Q3'25 ($4.5B) plus Prolec ($0.9B) plus 10% growth, orders are $7.3B (+12%). The band is wider than any gap. Orders have not separated good print days from bad ones (D07).

### T10. Customer advances (input for the cash line)

- Electrification contract liabilities have been 18.7–22.5% of equipment RPO (19.5–20.5% of total RPO in 2026) for ten quarters. Change: +$1,550M (2024), +$2,412M (2025), +$2,662M (H1'26, including acquired balances).
- On the Street's own RPO path (+$13.97B in 2027, +$13.81B in 2028), advances add about $2.7–2.9B a year before receivables and inventory.
- Street company FCF is $7,654M in 2027. EBITDA $9,471M less tax, capex ($1,441M) and other items leaves only about $1.0–1.4B of working-capital inflow in that figure. This belongs to the cash lens.

## 5. What was checked and showed no gap

| Line | Period | Street | Rebuilt | Verdict |
|---|---|---|---|---|
| Revenue | H2'26 | 8,169 | 8,153 at the guide; 8,332–8,887 on the back-test | +2% to +9%, two data points |
| Revenue | next four quarters | 16,145 | 16.4–17.3B, central about 16.8B | about +4% |
| Revenue | Q1'27 | 3,671 | 3,715–3,959, central about 3,800–3,850 | +3.5% to +4.8% central; under the bar |
| Revenue | FY27 | 17,704 | 17.65–19.5B | band wider than gap |
| Segment EBITDA | Q3'26 | 745 | 689–788 | in line |
| Segment EBITDA | Q4'26 | 917 | 844–983 | methods bracket the Street |
| Segment EBITDA | FY27 | 3,774 | 3,513–4,002 | methods bracket the Street |
| Segment EBITDA | 2028 | 4,972 | 22.7–25.3% margin ($4.8–5.4B) | brackets the Street |
| Segment EBITDA | 2029 | 6,130 | 5.9–7.2B | central +8%, band crosses zero |
| Orders | Q3'26 | 6,498 | 5.3–7.3B | no read |
| D&A, EPS | Q3'26 | D&A 352–376; EPS 4.04 | D&A 418–428; EPS 3.90–3.93 | -3% on EPS |
| Prolec margin | 2026 | not published | 22.0% vs 25% deal case | about $90M a year; not material |
| 2028 framework | 2028 | 21.3B, 23.4% | $20B, 22% (company) | Street above the company; already known |

## 6. Scripts

Working scripts are in the session scratchpad (`calc1.py` to `calc4.py`, `vintage_elec.py`, `rpo_seg.py`, `guides.py`). They read `segment_quarterly.json`, the Bloomberg workbooks and `gev.db` (read-only). Every table above can be rebuilt from the sources in section 1.
