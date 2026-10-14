# Candidate file: equipment revenue vs GEV's own backlog schedule

_AI-assisted research input only: facts, arithmetic, tables and sources. No memo sentences. The team writes every sentence, chooses every forecast number, every pass mark and the direction. Bloomberg data is licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep it inside the project folder._

Working date 2026-10-01. All figures $M unless stated. Recomputed for this file with Python from the primary files (scripts listed in section 9).

Terms used:
- **RPO**: remaining performance obligations. Signed orders not yet delivered. GEV calls it backlog.
- **Y1**: equipment RPO x the share GEV says it will recognise "within 1 year". A dollar amount for the next four quarters.
- **Uplift**: actual next-four-quarter equipment revenue divided by Y1. Above 1.00 means orders were booked and shipped inside the year on top of the schedule.
- **Street**: Bloomberg BEst mean consensus, 2026-10-01.
- **NTM**: next twelve months.
- **Drop-through**: adjusted EBITDA earned on each extra dollar of equipment revenue.

## 0. Status after three checks

| Check | Result | Corrected gap | Error band |
|---|---|---|---|
| Reproduce | Survives, narrowly. Every number on the line reproduces | about +7% (range +1% to +11%) | +/-4.5% |
| Already known or bad data | Survives, cut down. Sign holds on all eight Street readings tested | about +5% (range +1.3% to +9%) | +/-5% |
| 13 wedge tests | **Does not survive as a stand-alone wedge.** 6 of 13 pass; distance and error-band tests fail | about +5.5% (range +3% to +9%) | +/-7% |

What that means for use:
- The fact is solid: the Street's equipment revenue for Q3 2026 to Q2 2027 is below the amount GEV itself filed as scheduled for those quarters.
- The size is small: about +5% to +7% on equipment revenue, +1% to +5% on total revenue, +1.5% to +6.6% on EBITDA.
- The checkers' common reading: usable as a supporting fact for the revenue line and as a dated test (10-K schedule, late January 2027). Not enough by itself to carry a target.
- The headline "+8.7%" and the "gap sits in H1 2027" form should not be used. Both rest on assumptions the checks did not support.

---

## 1. The X, Y, Z line

Line: **consolidated equipment revenue**. Period: **Q3 2026 to Q2 2027** (four quarters, straddles FY26 and FY27).

| | Number | Source and method |
|---|---|---|
| **X: what the market expects** | **$30,245M** = 7,482 / 8,339 / 6,675 / 7,748 by quarter. Other fair readings of the same line: $29.5B to $30.8B (section 2.2) | Bloomberg, 2026-10-01. `GEV_Pull_2026-10-01/01-eeo-company-specific.xlsx`, sheet "Multiple Periods", rows 24 + 27 + 30, columns F to I |
| **Y: what the price implies** | $987.45 = 28.54x x $8,923M NTM EBITDA, which is the Street. So the price implies X, at a multiple in the 6th percentile of the last 12 months. To hold $987.45 in late January 2027 the multiple can fall to 26.2x on Street numbers. If it falls to 24.6x (peer line, section 4.4) the price needs NTM EBITDA of $10,353M, +6.4% on the Street, which is about +$3.1B to +$4.8B of equipment revenue at a 13-20% drop-through | Snapshot sheet row 3 (PX_LAST, CURR_ENTP_VAL, BEST_EV_TO_BEST_EBITDA). 254,694 / 28.544 = 8,923. (987.45 x 266.334 - 8,298) / 9,727 = 26.2 |
| **Z: arithmetic on disclosed data** | Schedule alone: **$31,616M** ($31,176M to $32,055M for rounding of the 36%). With an uplift of 1.00 to 1.03: **$31.6B to $32.6B**. $32.9B only at 1.04 (the seven-window mean). $29.0B if the one miss (0.918) repeats | 10-Q Q2 2026, accession 0001996810-26-000148, RPO note: 87,821 x 36%. Uplift from the back-test in section 2.4 |
| **Gap, Z vs X** | Floor (no uplift): +4.5% on the printed Street; +2.7% to +4.9% on four of the five Street readings (+7.1% on the fifth); +1.3% if the 36% is really 35.5% and the Street is read on medians. With uplift 1.02-1.03: +4.8% to +8.1%. **Checkers' centre: +5% to +7%** | Section 2.3 matrix |
| **Error band on Z** | +/-4.5% to +/-7% (one standard deviation). The gap is about 1.0 to 1.6 times its error | Section 2.4 |
| **D: the date you find out** | Final: Q2 2027 10-Q, late July 2027 (prior Q2 dates 2025-07-23, 2026-07-22). First interim: **2026-10-28**, 7:30 am ET (company events page). Main interim: late January 2027 (Q4 release, FY27 guide, 10-K schedule) | gevernova.com/investors/events; Snapshot EXPECTED_REPORT_DT |
| **Pass marks (candidates; the team sets its own)** | 2026-10-28: new one-year amount at 9/30/26 of $32.9B or more (5% above Street Q4'26-Q3'27 equipment $31,314M). Late January 2027: 10-K one-year amount of $34.0B or more (5% above Street FY27 equipment $32,383M). Late July 2027: four-quarter equipment revenue of $31.6B or more | Section 6 |

Same line on other bases, for reference:

| Line (same four quarters) | Street | Arithmetic range | Gap |
|---|---|---|---|
| Total revenue | 50,019 (22-28 brokers) | 50,400 to 52,700 | +0.8% to +5.3% |
| Power + Electrification equipment (Wind removed) | 24,415 | 25,300 to 26,300 floor (Wind at Street's 71% down to 65% of its backlog) | +3.8% to +7.7% |
| Adjusted EBITDA | 8,210 | +137 to +541 on top | +1.7% to +6.6% (-3% to +6.6% if Street services are too high) |

---

## 2. The proof table

### 2.1 Company side: every input

| # | Input | Value | Where | Formula |
|---|---|---|---|---|
| 1 | Equipment RPO at 6/30/26 | 87,821 | 10-Q Q2 2026, accession 0001996810-26-000148, Note on RPO, between page footers 15 and 16; corpus chunk 5683. Also the Q2 2026 slide appendix | |
| 2 | Share recognised within 1 / 2 / 5 years | 36% / 65% / 97% | same sentence: "Equipment-related RPO of $87,821 million of which 36%, 65%, and 97% is expected to be recognized within 1, 2, and 5 years" | |
| 3 | Y1 at 6/30/26 | **31,616** | | 87,821 x 0.36 = 31,615.6 |
| 4 | Y1, rounding range | 31,176 to 32,055 | | 87,821 x 0.355 and x 0.365 |
| 5 | Division equipment RPO at 6/30/26 | Power 39,261; Wind 8,197; Electrification 40,589 (sum 88,047 before eliminations) | same 10-Q, MD&A segment RPO tables; chunks 5735, 5740, 5737; Q2 2026 slide appendix | |
| 6 | Services RPO and one-year share | 88,463; 16% | same sentence, part (2) | 88,463 x 0.16 = 14,154 |
| 7 | Equipment revenue by quarter, reported | Q1'24 3,617; Q2 4,194; Q3 5,290; Q4 5,851; Q1'25 4,197; Q2 4,894; Q3 5,880; Q4 5,963; Q1'26 5,254; Q2 6,459 | XBRL `RevenueFromContractWithCustomerExcludingAssessedTax`, ProductMember; `data/financials/gev_segments.csv`, row "Product". Q4 = full year less nine months | |
| 8 | Prolec equipment revenue | Q1'26 469; Q2'26 834 (six months 1,303) | 10-Q Q1 2026 (0001996810-26-000064) and Q2 2026, table "Equipment and services organic revenues", line "Less: Acquisitions"; chunks 13731, 5768 | Removed from windows whose backlog date is before the 2026-02-02 deal |
| 9 | FY26 revenue guide | $45.5B to $46.5B | Q2 2026 release, 2026-07-22; table `mgmt_guidance` | |
| 10 | H1 2026 revenue; equipment; services | 20,442; 11,713; 8,729 | 10-Q Q2 2026 income statement | |

### 2.2 Street side: every input (Bloomberg, 2026-10-01)

| # | Input | Q3'26 | Q4'26 | Q1'27 | Q2'27 | Sum | Where |
|---|---|---|---|---|---|---|---|
| 11 | Power equipment | 2,393.9 | 3,096.7 | 2,585.5 | 2,797.8 | 10,874 | `01-eeo-company-specific.xlsx`, "Multiple Periods", row 24, F:I |
| 12 | Wind equipment | 1,789.2 | 1,763.1 | 1,019.0 | 1,258.7 | 5,830 | row 27, F:I |
| 13 | Electrification equipment | 3,299.0 | 3,479.4 | 3,070.8 | 3,691.9 | 13,541 | row 30, F:I |
| 14 | **Equipment, total** | 7,482.1 | 8,339.2 | 6,675.4 | 7,748.3 | **30,245.0** | 11 + 12 + 13. Same as `segment_quarterly.json` keys `Total Revenue\|Power\|Equipment` etc. |
| 15 | Services, total | 4,485.2 | 5,629.2 | 4,536.3 | 5,139.1 | 19,789.8 | rows 25 + 28 + 31 |
| 16 | Total revenue | 11,992.9 | 13,914.6 | 11,143.2 | 12,968.1 | 50,018.8 | row 7 |
| 17 | EBITDA (GEV's adjusted basis) | 1,671.8 | 2,499.7 | 1,810.4 | 2,228.2 | 8,210.0 | row 9 |
| 18 | Diluted EPS | 4.04 | 5.61 | 4.49 | 5.67 | 19.81 | row 6 |
| 19 | Free cash flow | 1,502.2 | 1,148.5 | 729.5 | 1,725.8 | 5,106.0 | row 13 |

Other readings of row 14 (why the Street figure is soft by about 2%):

| Reading | Four quarters | Method | Source |
|---|---|---|---|
| Division means, as printed | 30,245 | rows 24 + 27 + 30 | as above |
| Consolidated basis | about 30,125 | less about 30 a quarter of intersegment sales (Bloomberg Q2'26 actual rows sum to 6,490; GEV reported 6,459) | rows 24/27/30 column E vs 10-Q |
| Electrification services row corrected | 30,545 to 30,685 | total revenue less services, with the Electrification services row cut by 331 to 481 | `propose_electrification.md` |
| Scaled to Q3 medians | 30,781 | Q3 medians 2,433 + 1,813 + 3,369 = 7,615 vs means 7,482 (+1.8%), applied to all four quarters | `06_modl.xlsx`, "Single Period", rows 24/27/30, column H |
| Scaled to income-statement product revenue | 29,526 (median) to 29,757 (mean) | Q3 product revenue 7,304 median, 7,361 mean | `06_modl.xlsx` row 96 |

Limits: broker-level cells for the equipment rows are blank on the export, so the number of contributors is unknown. Medians exist for Q3 2026 only. Total revenue (row 16) has 28 brokers for H2 2026 and 22 for H1 2027.

### 2.3 The gap, on every pairing

Rows = Street reading. Columns = company-side value.

| Street reading | 35.5% share, no uplift (31,176) | Schedule (31,616) | x1.02 (32,248) | x1.03 (32,564) | x1.04 (32,880) | x0.918 (29,023) |
|---|---|---|---|---|---|---|
| Product-revenue median scaling (29,526) | +5.6% | +7.1% | +9.2% | +10.3% | +11.4% | -1.7% |
| Consolidated basis (30,125) | +3.5% | +4.9% | +7.0% | +8.1% | +9.1% | -3.7% |
| **Division means, printed (30,245)** | +3.1% | **+4.5%** | +6.6% | +7.7% | +8.7% | -4.0% |
| Services-row corrected (30,545 to 30,685) | +1.6% to +2.1% | +3.0% to +3.5% | +5.1% to +5.6% | +6.1% to +6.6% | +7.2% to +7.6% | -5.0% to -5.4% |
| Scaled to Q3 medians (30,781) | +1.3% | +2.7% | +4.8% | +5.8% | +6.8% | -5.7% |

Dollar gap on the printed Street: +931 / +1,371 / +2,003 / +2,319 / +2,635 / -1,222.

### 2.4 Back-test: every window since the schedule was first disclosed

Scheduled = equipment RPO x one-year share in that filing. Actual = equipment revenue in the next four quarters (input 7). Ratio ex-Prolec removes input 8.

| Backlog date | Accession | Equipment RPO | 1-yr share | Scheduled (Y1) | Next 4 quarters | Ratio | Ratio ex-Prolec | Growth the schedule demanded (Y1 / trailing 4 quarters) | Growth realised |
|---|---|---|---|---|---|---|---|---|---|
| 12/31/23 | 0001193125-24-131304 (S-1/A; same in S-1 0001193125-24-066951) | 40,478 | 51% | 20,644 | 18,952 | 0.918 | 0.918 | +13.1% | +3.8% |
| 3/31/24 | 0001996810-24-000008 | 42,210 | 45% | 18,994 | 19,532 | 1.028 | 1.028 | +3.3% | +6.2% |
| 6/30/24 | 0001996810-24-000067 | 41,561 | 47% | 19,534 | 20,232 | 1.036 | 1.036 | +7.4% | +11.2% |
| 9/30/24 | 0001996810-24-000083 | 42,069 | 46% | 19,352 | 20,822 | 1.076 | 1.076 | +4.0% | +11.9% |
| 12/31/24 | 0001996810-25-000011 | 43,047 | 44% | 18,941 | 20,934 | 1.105 | 1.105 | -0.1% | +10.5% |
| 3/31/25 | 0001996810-25-000073 | 45,478 | 45% | 20,465 | 21,991 | 1.075 | 1.052 | +4.8% | +10.2% |
| 6/30/25 | 0001996810-25-000133 | 49,712 | 42% | 20,879 | 23,556 | 1.128 | 1.066 | +3.2% | +10.0% |
| 9/30/25 (1 Street quarter) | 0001996810-25-000160 | 54,092 | 41% | 22,178 | 25,158 | 1.134 | 1.031 to 1.037 | +6.5% | open |
| 12/31/25 (2 Street quarters) | 0001996810-26-000015 | 64,245 | 37% | 23,771 | 27,534 | 1.158 | 1.019 to 1.032 | +13.6% | open |
| 3/31/26 (3 Street quarters) | 0001996810-26-000064 | 75,924 | 38% | 28,851 | 28,956 | 1.004 | 1.004 | +31.2% | open |
| **6/30/26 (4 Street quarters)** | 0001996810-26-000148 | 87,821 | 36% | **31,616** | **30,245** | **0.957** | 0.957 | **+34.2%** | Street +28.4% |

Partly reported rows assume Prolec equipment of 850 to 1,000 a quarter in Q3-Q4 2026 (not disclosed in advance).

Statistics (ratio ex-Prolec):

| Sample | Mean | Std dev | Min | Max | Street's 0.957 in std devs |
|---|---|---|---|---|---|
| Seven fully reported windows | 1.040 | 0.060 | 0.918 | 1.105 | 1.4 below |
| Six post-spin windows | 1.060 | 0.028 | 1.028 | 1.105 | 3.7 below |
| Median, seven windows | 1.052 | | | | |

Error of the method, and why the checkers cut the uplift to 1.00-1.03:

| Fact | Number | Meaning |
|---|---|---|
| Leave-one-out error of "Y1 x mean ratio" | 6.4% (largest miss 14.2%) | About the size of the gap |
| Windows overlap | Six post-spin windows cover about two independent years | Predictive std dev about 5% to 7% |
| A naive model (trailing four quarters x average growth) | error 3.2%; today it gives about $28.0B, below the Street | In the past, steady 10% growth explained revenue better than the schedule did |
| Correlation of the ratio with the growth the schedule demanded | -0.93 (seven windows); -0.74 (six) | The schedule was beaten when it asked for little growth (-0.1% to +7.4%). The one window that asked for +13.1% missed by 8.2%. Today's asks for +34% (about +26% organic) |
| Open windows on reported quarters | 9/30/25 window is at 73.8% of Y1 after three quarters (77.2% a year earlier). FY26 window is at 43.8% after two quarters (48.0% a year earlier) | Uplift is running lower than in 2025 |
| GEV's own FY26 guide against the 12/31/25 schedule | 0.98 to 1.05 (recomputed: guide 45.5-46.5B, services at Street or +8.4%, Prolec 1.7-2.0B in H2) | Management's own number sits at 1.00 to 1.04 |
| The 12/31/23 miss, adjusted for the nuclear business sold to EDF | about 0.94 to 0.99 (assumes $350M of removed revenue; not disclosed) | Still the lowest window, still at or below 1.00 |
| Currency | Equipment revenue carried +149 (Q1'26) and +55 (Q2'26) of currency effect; backlog is translated at the balance-sheet rate | Not tested further; no FX series in the pull |

A second way to reach 1.00-1.03 that uses only the Q3 Street figure (which equals management's Q3 guide) and history:

| Step | Number |
|---|---|
| Share of Y1 delivered in quarters 2 to 4 of the two earlier June windows | 76.6% (6/30/24) and 78.4% (6/30/25, ex-Prolec) |
| Q3 2026 at the Street | 7,482 = 23.7% of Y1 (the earlier June windows opened at 27.1% and 28.2%) |
| Four-quarter total if quarters 2 to 4 deliver the same share as before | 7,482 + 0.766 x 31,616 = 31,700 (1.003 x Y1) to 7,482 + 0.784 x 31,616 = 32,269 (1.021 x Y1) |
| Against the Street | +4.8% to +6.7% on four quarters; +6.4% to +8.9% on Q4'26 to Q2'27 (Street 22,763) |

### 2.5 Supporting arithmetic (reproduced)

| Check | Arithmetic | Result |
|---|---|---|
| Step in the schedule vs step in the Street | Y1 rose 28,851 to 31,616 = +2,764 in a quarter (+1,946 at worst after rounding). The Street's four-quarter window rose 28,956 to 30,245 = +1,289 | The Street moved less than half as much as the schedule |
| Ratio as Street quarters enter the window | 1.03-1.04 (1 Street quarter), 1.02-1.03 (2), 1.004 (3), 0.957 (4) | The shortfall is in broker models, not in reported quarters |
| Remainder for H1 2027 | 31,616 - Street H2'26 equipment 15,821 = 15,794 vs Street H1'27 14,424 | +9.5%; needs H1'27 equipment +34.8% y/y vs the Street's +23.1%. Not an independent finding: it assumes H2'26 lands on the Street |
| Wind bound | Street has Wind converting 5,830 / 8,197 = 71.1% of its equipment backlog. Reported: 58.5% to 69.3% in seven windows | Wind cannot absorb the gap. Power + Electrification scheduled = 31,616 - Wind: 25,786 at Street's Wind (+5.6% vs 24,415), 26,288 at 65% (+7.7%). Break-even: Wind would need 87.8% |
| Total-revenue form | Scheduled 31,616 + 14,154 = 45,770. Street 50,019 / 45,770 = 1.093. Seven windows ex-Prolec: 1.070, 1.158, 1.141, 1.169, 1.167, 1.127, 1.167 (mean 1.143) | Street is below six of seven |
| Two-year form | 65% x 87,821 = 57,084. Street eight quarters 65,382 = 1.145x. Three completed two-year windows: 1.280, 1.370, 1.481 | Street needs $8.3B of book-and-ship in two years; the last three windows had $8.7B to $13.8B on a much smaller order book. Explained by longer-dated orders; no gap claimed |
| Services | Street 19,790 = 22.4% of services RPO (history 21.3% to 22.6%) and 1.398x the 16% schedule (history 1.239x to 1.365x) | Inside the range on one measure, above it on the other |
| Prior precedent | January 2026 guide implied organic equipment at 0.94-0.98 of the 12/31/25 schedule; after two raises it implies 0.98-1.05 | The guide started below the schedule and was raised toward it |

Contrary arithmetic, kept on the page:

| Check | Result |
|---|---|
| Physical output | Gas output guided at 5 GW a quarter: 20 GW in the window vs 14.6 GW trailing (+37%). Street Power equipment is already +47.5% (10,874 vs 7,373). A bottom-up count gives H1'27 equipment of $14.4B to $15.2B: the Street to +5% |
| Wind orders | H1 2026 wind orders -33% in GW; the Street has H1'27 wind equipment flat |
| Electrification | Management's Q3 guide ($3.8B to $4.0B) equals the Street ($3,881M). No Electrification line was found with a gap of 7% or more |
| Months 13 to 24 | Street year-two equipment 35,137 vs 25,468 scheduled: no gap. The finding is about the next four quarters only |

---

## 3. From the line to profit

### 3.1 Margin assumptions, as ranges with their evidence

| Drop-through on extra equipment revenue | Evidence | Source |
|---|---|---|
| 10% to 13% (low) | Equipment gross margin: 10.3% (Q1'26), 13.1% (Q2'26), 11.8% (H1'26), 10.4% (FY25) | XBRL cost of equipment sold, `gev_facts_long.csv`, `CostOfGoodsAndServicesSold` / ProductMember |
| 14% to 20% (middle; the checkers used 12-20.5%) | Extra equipment gross profit per extra dollar, year on year: 13.9% (Q2'26), 18.1% (H1'26). Street Q3'26 equipment gross margin 19.2% (7,361 revenue, 5,952 cost). Street segment EBITDA margins for the four quarters: Power 20.0%, Electrification 19.3%, Wind 2.3% | same XBRL; `06_modl.xlsx` rows 96 and 101; `segment_quarterly.json` Adjusted EBITDA rows |
| 26% to 41% (high; upper bound only) | Segment EBITDA gained per extra dollar of segment revenue, H1'26 on H1'25: Electrification 26%, Power 41%. These include services and price, so they overstate equipment | XBRL segment revenue and segment EBITDA |

Other inputs: tax 20% to 25% (Street net income is 71% to 83% of EBITDA less D&A); diluted shares 266.3M (Bloomberg) to 270M (Q2'26 10-Q); Street average margin for the window 16.4% (8,210 / 50,019).

### 3.2 Effect by size of the revenue gap (four quarters, vs printed Street)

| Case | Equipment revenue | Extra revenue | Total revenue | EBITDA at 10% | at 13% | at 20% | at 30% | EPS effect (13% to 20%) |
|---|---|---|---|---|---|---|---|---|
| Low: 35.5% share, no uplift | 31,176 | +931 (+3.1%) | 50,950 (+1.9%) | +93 (+1.1%) | +121 (+1.5%) | +186 (+2.3%) | +279 (+3.4%) | +$0.34 to +$0.56 |
| Schedule, no uplift | 31,616 | +1,371 (+4.5%) | 51,390 (+2.7%) | +137 (+1.7%) | +178 (+2.2%) | +274 (+3.3%) | +411 (+5.0%) | +$0.49 to +$0.82 |
| x1.02 | 32,248 | +2,003 (+6.6%) | 52,022 (+4.0%) | +200 (+2.4%) | +260 (+3.2%) | +401 (+4.9%) | +601 (+7.3%) | +$0.72 to +$1.20 |
| x1.03 | 32,564 | +2,319 (+7.7%) | 52,338 (+4.6%) | +232 (+2.8%) | +301 (+3.7%) | +464 (+5.6%) | +696 (+8.5%) | +$0.84 to +$1.39 |
| x1.04 | 32,880 | +2,635 (+8.7%) | 52,654 (+5.3%) | +264 (+3.2%) | +343 (+4.2%) | +527 (+6.4%) | +791 (+9.6%) | +$0.95 to +$1.58 |
| Downside: 0.918 repeats | 29,023 | -1,222 (-4.0%) | 48,797 (-2.4%) | -122 (-1.5%) | -159 (-1.9%) | -244 (-3.0%) | -367 (-4.5%) | -$0.44 to -$0.73 |

- EBITDA percentages are of the Street's $8,210M. EPS effect = extra EBITDA x (1 - tax) / shares; Street EPS for the four quarters is $19.81, so +$0.49 to +$1.39 is +2.5% to +7.0%.
- On the corrected Street ($30.5B to $30.8B) subtract $255M to $535M of revenue from every "extra revenue" cell.
- Margin percentage: below a 16.4% drop-through the EBITDA margin falls (by 0.1 to 0.3 point at 10-13%); above it the margin rises. The stock has reacted to the margin guide, not to revenue.
- Services offset, if the team accepts it: Street services at 1.398x the schedule against 1.239x to 1.365x in history. Services at 1.33x to 1.365x would be 470 to 965 below the Street (-2.4% to -4.9%), about -150 to -310 of EBITDA at a 32% services gross margin. Net EBITDA range then runs from about -3% to +6.6%.

### 3.3 Effect by quarter (two timings the data cannot tell apart)

Timing B = H2 2026 lands on the Street (which equals the guide) and all of the gap falls in H1 2027. Timing C = the gap is spread across the four quarters in proportion to the Street.

| Case | Line | Q3'26 | Q4'26 | Q1'27 | Q2'27 | FY26 effect | FY27 effect (H1 only) |
|---|---|---|---|---|---|---|---|
| Schedule x1.00, timing B | Extra equipment revenue | 0 | 0 | +634 | +736 | 0 | +1,371 (+2.6% of 53,029) |
| | Extra EBITDA, 13% to 20% | 0 | 0 | +82 to +127 | +96 to +147 | 0 | +178 to +274 (+1.9% to +2.9% of 9,471) |
| | Extra EPS | 0 | 0 | +$0.23 to +$0.38 | +$0.27 to +$0.44 | | |
| Schedule x1.00, timing C | Extra equipment revenue | +339 | +378 | +303 | +351 | +717 (FY26 revenue 46,957; guide top 46,500) | +654 |
| | Extra EBITDA, 13% to 20% | +44 to +68 | +49 to +76 | +39 to +61 | +46 to +70 | +93 to +143 (+1.5% to +2.3% of 6,334) | +85 to +131 |
| x1.03, timing B | Extra equipment revenue | 0 | 0 | +1,073 | +1,246 | 0 | +2,319 (+4.4%) |
| | Extra EBITDA, 13% to 20% | 0 | 0 | +140 to +215 | +162 to +249 | 0 | +301 to +464 (+3.2% to +4.9%) |
| x1.03, timing C | Extra equipment revenue | +574 | +639 | +512 | +594 | +1,213 (FY26 revenue 47,453) | +1,106 |
| | Extra EBITDA, 13% to 20% | +75 to +115 | +83 to +128 | +67 to +102 | +77 to +119 | +158 to +243 (+2.5% to +3.8%) | +144 to +221 |

What each timing requires:
- Timing B: H1 2027 equipment revenue up 35% to 43% on H1 2026, against the Street's +23%. It also puts FY27 revenue at $56B or more if normal seasonality holds, above GEV's own 2028 target of $56B.
- Timing C: FY26 revenue of $47.0B to $47.5B, above the $46.5B guide top, while management's own Q3 guide equals the Street.
- A third timing, the pattern of the two earlier June windows (57% of Y1 in the first two quarters), gives FY26 revenue of $48.5B to $49.1B and H1 2027 equipment below the Street. The Q3 guide makes this the least likely.

### 3.4 Free cash flow

| Method | Effect on four-quarter FCF (Street 5,106) | Why |
|---|---|---|
| Cash follows profit | +$0.10B to +$0.43B | Extra EBITDA (137 to 541) x (1 - tax) |
| Deposits already collected | about zero, possibly negative | Contract liabilities were 40,037 at 6/30/26. Revenue recognised from backlog releases a deposit already in the bank; only the unbilled part is new cash, and the build cost is paid in or before the period |

GEV does not disclose billing terms by contract, so the sign is not identified. The separate FCF lens (`propose_fcf-deposits.md`) found a band wider than its gap. FCF is not the line for this candidate.

---

## 4. From profit to price

Bridge used throughout (Bloomberg, 2026-10-01): price = (multiple x NTM EBITDA + 8,298) / 266.334. Today: 28.544 x 8,923 = 254,694; (254,694 + 8,298) / 266.334 = $987.45.

### 4.1 Which NTM EBITDA the thesis can move

| Valuation date | Street NTM EBITDA (blend of annual consensus) | Sum of Street quarters | Does the thesis period (Q3'26-Q2'27) overlap the NTM window? |
|---|---|---|---|
| Late January 2027 | 9,727 = 11/12 x 9,471 + 1/12 x 12,553 | 9,391 | Yes, H1 2027 only |
| Late April 2027 | 10,498 | 10,206 | Q2 2027 only |
| Late July 2027 | 11,269 = 5/12 x 9,471 + 7/12 x 12,553 | 10,981 | **No** |
| 1 October 2027 (12 months) | 11,783 | 11,906 | **No** |

So for a horizon of 10 to 12 months the direct effect on forward EBITDA is zero. Any effect comes from brokers carrying a higher level forward. Facts on that:
- If the Street lifts forward equipment revenue by the same percentage as the four-quarter gap (4.5% to 8.7%) at a 13-20% drop-through, NTM EBITDA rises 1.9% to 5.8% (January 2027) and 1.8% to 5.4% (July and October 2027).
- After each of the last four reports the FY27 consensus moved within 30 days: revenue +4.1%, +4.8%, +2.4%, +2.0%; EBITDA +5.3%, +6.4%, +7.4%, +1.3% (ConsensusHistory sheet; the January 2026 step includes Prolec).
- The months-13-to-24 test shows no gap, which argues for timing, not level.

The grids below therefore show the Street path and four "corrected" paths (+1.5%, +3%, +5%, +6.6% on NTM EBITDA) plus the downside (-3%). The team picks the path its model supports.

### 4.2 Price grid

**Late January 2027** (Street NTM 9,727; break-even multiple 26.2x)

| Path | NTM EBITDA | 21x | 23x | 24.6x | 26x | 27.3x | 28.5x | 30x | 32.5x |
|---|---|---|---|---|---|---|---|---|---|
| Street | 9,727 | $798 (-19%) | $871 (-12%) | $930 (-6%) | $981 (-1%) | $1,028 (+4%) | $1,072 (+9%) | $1,127 (+14%) | $1,218 (+23%) |
| +1.5% | 9,873 | $810 (-18%) | $884 (-10%) | $943 (-4%) | $995 (+1%) | $1,043 (+6%) | $1,088 (+10%) | $1,143 (+16%) | $1,236 (+25%) |
| +3% | 10,019 | $821 (-17%) | $896 (-9%) | $957 (-3%) | $1,009 (+2%) | $1,058 (+7%) | $1,103 (+12%) | $1,160 (+17%) | $1,254 (+27%) |
| +5% | 10,214 | $837 (-15%) | $913 (-8%) | $975 (-1%) | $1,028 (+4%) | $1,078 (+9%) | $1,124 (+14%) | $1,182 (+20%) | $1,278 (+29%) |
| +6.6% | 10,369 | $849 (-14%) | $927 (-6%) | $989 (0%) | $1,043 (+6%) | $1,094 (+11%) | $1,141 (+16%) | $1,199 (+21%) | $1,297 (+31%) |
| -3% | 9,436 | $775 (-22%) | $846 (-14%) | $903 (-9%) | $952 (-4%) | $998 (+1%) | $1,041 (+5%) | $1,094 (+11%) | $1,183 (+20%) |

**Late July 2027** (Street NTM 11,269; break-even multiple 22.6x)

| Path | NTM EBITDA | 21x | 23x | 24.6x | 26x | 27.3x | 28.5x | 30x | 32.5x |
|---|---|---|---|---|---|---|---|---|---|
| Street | 11,269 | $920 (-7%) | $1,004 (+2%) | $1,072 (+9%) | $1,131 (+15%) | $1,186 (+20%) | $1,237 (+25%) | $1,300 (+32%) | $1,406 (+42%) |
| +1.5% | 11,438 | $933 (-6%) | $1,019 (+3%) | $1,088 (+10%) | $1,148 (+16%) | $1,204 (+22%) | $1,255 (+27%) | $1,320 (+34%) | $1,427 (+45%) |
| +3% | 11,607 | $946 (-4%) | $1,034 (+5%) | $1,103 (+12%) | $1,164 (+18%) | $1,221 (+24%) | $1,273 (+29%) | $1,339 (+36%) | $1,448 (+47%) |
| +5% | 11,832 | $964 (-2%) | $1,053 (+7%) | $1,124 (+14%) | $1,186 (+20%) | $1,244 (+26%) | $1,297 (+31%) | $1,364 (+38%) | $1,475 (+49%) |
| +6.6% | 12,013 | $978 (-1%) | $1,069 (+8%) | $1,141 (+16%) | $1,204 (+22%) | $1,262 (+28%) | $1,317 (+33%) | $1,384 (+40%) | $1,497 (+52%) |
| -3% | 10,931 | $893 (-10%) | $975 (-1%) | $1,041 (+5%) | $1,098 (+11%) | $1,152 (+17%) | $1,201 (+22%) | $1,262 (+28%) | $1,365 (+38%) |

**1 October 2027** (Street NTM 11,783; break-even multiple 21.6x)

| Path | NTM EBITDA | 21x | 23x | 24.6x | 26x | 27.3x | 28.5x | 30x | 32.5x |
|---|---|---|---|---|---|---|---|---|---|
| Street | 11,783 | $960 (-3%) | $1,049 (+6%) | $1,119 (+13%) | $1,181 (+20%) | $1,239 (+25%) | $1,292 (+31%) | $1,358 (+38%) | $1,469 (+49%) |
| +1.5% | 11,959 | $974 (-1%) | $1,064 (+8%) | $1,136 (+15%) | $1,199 (+21%) | $1,257 (+27%) | $1,311 (+33%) | $1,378 (+40%) | $1,491 (+51%) |
| +3% | 12,136 | $988 (0%) | $1,079 (+9%) | $1,152 (+17%) | $1,216 (+23%) | $1,275 (+29%) | $1,330 (+35%) | $1,398 (+42%) | $1,512 (+53%) |
| +5% | 12,372 | $1,007 (+2%) | $1,100 (+11%) | $1,174 (+19%) | $1,239 (+25%) | $1,299 (+32%) | $1,355 (+37%) | $1,425 (+44%) | $1,541 (+56%) |
| +6.6% | 12,560 | $1,022 (+3%) | $1,116 (+13%) | $1,191 (+21%) | $1,257 (+27%) | $1,319 (+34%) | $1,375 (+39%) | $1,446 (+46%) | $1,564 (+58%) |
| -3% | 11,429 | $932 (-6%) | $1,018 (+3%) | $1,087 (+10%) | $1,147 (+16%) | $1,203 (+22%) | $1,254 (+27%) | $1,319 (+34%) | $1,426 (+44%) |

### 4.3 How much of a target is the estimate and how much is the multiple

Split used: roll-forward = price at today's 28.54x on the Street's NTM at the date; estimate = the change from the corrected path at 28.54x; multiple = the rest. Points of return on $987.45.

| Date | Path | Exit multiple | Price | Total return | Roll-forward | Estimate | Multiple |
|---|---|---|---|---|---|---|---|
| Late Jan 2027 | +3% | 24.6x | $957 | -3.1% | +8.7 | +3.2 | -15.0 |
| Late Jan 2027 | +3% | 27.3x | $1,058 | +7.2% | +8.7 | +3.2 | -4.7 |
| Late Jan 2027 | +5% | 28.5x | $1,126 | +14.0% | +8.7 | +5.3 | 0.0 |
| Late Jan 2027 | +5% | 32.5x | $1,278 | +29.4% | +8.7 | +5.3 | +15.4 |
| Late Jul 2027 | +3% | 24.6x | $1,103 | +11.7% | +25.5 | +3.7 | -17.4 |
| Late Jul 2027 | +3% | 27.3x | $1,221 | +23.6% | +25.5 | +3.7 | -5.5 |
| Late Jul 2027 | +5% | 28.5x | $1,299 | +31.6% | +25.5 | +6.1 | 0.0 |
| 1 Oct 2027 | Street | 27.0x | $1,225 (sell-side mean target) | +24.1% | +31.0 | 0.0 | -6.9 |
| 1 Oct 2027 | +3% | 24.6x | $1,152 | +16.7% | +31.0 | +3.8 | -18.2 |
| 1 Oct 2027 | +3% | 27.3x | $1,275 | +29.1% | +31.0 | +3.8 | -5.7 |
| 1 Oct 2027 | +5% | 28.5x | $1,357 | +37.4% | +31.0 | +6.4 | 0.0 |

Sizes to keep in view:
- One turn of the multiple is worth $36 to $44 a share (3.7% to 4.5% of today's price). One percent of NTM EBITDA at 28.5x is worth $10 to $13 (1.05% to 1.28%).
- The whole estimate leg (+1.6 to +8.4 points) equals 0.4 to 1.9 turns of the multiple.
- The roll-forward leg (+8.7 points by January, +25.5 by July, +31.0 by October) is the Street's own EBITDA growth at an unchanged multiple. It is not this thesis.
- So any target above about +10% is carried by the multiple holding, not by this line.

### 4.4 Evidence available for the multiple

| Anchor | Level | Source |
|---|---|---|
| Today | 28.5x (27.9x on the last weekly print) | Snapshot; Multiples sheet |
| Last 52 weeks | low 27.3x (2026-08-28), median 32.4x, high 42.4x; no week at or below 26x | Multiples sheet |
| Since the spin (130 weeks) | 26 weeks at or below 21x; 40 at or below 25x; the last was April 2025 | same |
| March-April 2025 sell-off | 18.5x to 24.0x on weekly closes | same |
| Peer line: multiple = 5.48 + 0.521 x two-year EBITDA growth + 0.121 x margin (11 peers) | R-squared 0.82, residual error 5.4 turns. GEV fitted: 28.9x today, **24.6x late January 2027**, 21.2x late September 2027. Re-run for this file: same coefficients | Consensus and Snapshot sheets |
| Same line without Bloom Energy | R-squared 0.04; GEV fitted 17.7x | The slope rests on one company |
| Peers today | 10.9x to 22.3x (Bloom 51.7x) | Snapshot |

---

## 5. Model tabs and lines that carry this

Existing workbook: `data/model/GEV_model_shell.xlsx` (tabs README, Drivers, Segments, P&L, Cash, Valuation, Scenarios, vs Consensus, Backlog vintage). It is annual (FY26-FY28) and values on a P/E. The thesis line is a four-quarter window, so the model needs a half-year or quarterly bridge.

| Tab | Line or block | Driver and formula in words | Status in the shell |
|---|---|---|---|
| Backlog vintage | Rows 8-17: equipment RPO, one-year share, Y1, accession | Y1 = RPO x share. Already there for ten dates | Present. Add the 12/31/23 row (40,478; 51%) |
| Backlog vintage (new columns) | Next-four-quarter equipment revenue; Prolec; ratio; demanded growth | Ratio = (next four quarters - Prolec) / Y1. Demanded growth = Y1 / trailing four quarters - 1 | Add. Values in section 2.4 |
| Backlog vintage (new block) | "Conversion, Q3'26-Q2'27" | Equipment revenue for the window = Y1 x uplift. Uplift is one yellow input (range 0.92 to 1.04; the checks support 1.00 to 1.03). Rounding switch for the share (35.5 / 36 / 36.5%) | Add. This is the thesis driver |
| Segments (new rows) | Equipment and services revenue by division, by half-year: H2'26, H1'27, H2'27 | Window total from the block above. Split to divisions: Wind = Wind equipment RPO (8,197) x a turnover input (58% to 71%); Power + Electrification = total - Wind; split of those two is an input, not disclosed. Split to halves: one input, the share of Y1 that falls in H2'26 (Street 50%; guide-implied 47-51%; earlier June windows 57%); H2'26 = Y1 x that share, H1'27 = window total - H2'26 | Add. The shell builds Power equipment as GW x $/kW and Electrification and Wind as growth rates, with no equipment / services split outside Power |
| Segments (check row) | "Annual build vs conversion build" | FY26 equipment = H1'26 actual 11,713 + H2'26 from the window. FY27 equipment = H1'27 from the window + H2'27 input. Compare with GW x $/kW + Electrification + Wind from the annual drivers; the two must agree | Add |
| Drivers | Drop-through on extra equipment revenue (10% to 30%); services ratio to schedule (1.24 to 1.40) | Extra EBITDA = (model equipment revenue - Street equipment revenue) x drop-through | Add two yellow cells |
| P&L | Revenue, adjusted EBITDA, EPS by half-year for H2'26 and H1'27, then FY | EBITDA = Street EBITDA for the period + extra EBITDA (or the segment-margin build if the team prefers). EPS = (EBITDA - D&A + interest) x (1 - tax) / shares | Shell is annual; add the two half-years |
| Cash | Customer deposits line | Leave the thesis out of FCF, or carry extra EBITDA after tax as an upper case. State which | Present, empty |
| vs Consensus | New rows: equipment revenue Q3'26-Q2'27 (Street 30,245); H1'27 equipment (14,424); FY27 equipment (32,383); total revenue for the window (50,019); EBITDA for the window (8,210) | Difference and percentage; source column = the Bloomberg file and cell | Shell has FY27 rows only, with free-vendor placeholders (52,740 / 9,570 / 25.08 / 7,420). Bloomberg values are 53,029 / 9,471 / 24.52 / 7,654 |
| Valuation | EV/EBITDA bridge | Price = (multiple x NTM EBITDA + 8,298) / 266.334, with the NTM blend by date from section 4.1. Three-leg split: roll-forward, estimate, multiple | Shell uses exit P/E x FY27 EPS and a reference price of $940.33 (2026-09-18). Update to $987.45 or add the EBITDA bridge beside it |
| Scenarios | Rows = uplift (0.918 / 1.00 / 1.03), drop-through, services ratio, exit multiple (bear anchored on 21x-24.6x; base 27.3x-28.5x; bull 30x-32.5x) | Each scenario reads the same driver cells | Shell rows are GW, $/kW, growth rates, P/E |
| Sensitivity (new) | Two-way table: uplift x exit multiple, at the chosen date | Section 4.2 is this table at fixed paths | Add |
| Checks | Y1 = 31,616; Street window = 30,245; price bridge returns $987.45 at 28.544x and 8,923; half-years sum to fiscal years; every memo number equals a cell | | Add |

---

## 6. Dated tests, pass and fail marks, kill rule

All numbers below are reported by GEV. Marks are candidates computed from the data; the team fixes its own before 2026-10-28.

| Date | Number GEV reports | Compare with | Pass (candidate) | Fail (candidate) | Notes |
|---|---|---|---|---|---|
| **2026-10-28**, Q3 release and 10-Q | (a) New one-year amount = equipment RPO at 9/30/26 x new one-year share | Street Q4'26-Q3'27 equipment 31,314 | 32,880 or more (+5%). Needs Y1 to rise 1,264 or more in the quarter; the last three organic steps were +1,299, +1,593, +2,764 | 31,314 or less | Rounding of the share is worth about +/-480. Lookup table below |
| | (b) Q3 equipment revenue | Street 7,482 (7,304 to 7,615 across readings) | 7,860 or more (+5%) | below 7,300 | Weak test: management's Q3 guide equals the Street |
| | (c) The 9/30/25 window closes: (Q4'25 to Q3'26 equipment less acquisitions) / 22,178 | 1.03 | Q3 equipment less the "Less: Acquisitions" line of 6,470 or more | below 5,805 (ratio under 1.00) | First new completed window; demanded growth was +6.5% |
| **Late January 2027**, Q4 release, FY27 guide, 10-K (prior dates 2025-01-22, 2026-01-28) | (d) 10-K one-year amount at 12/31/26 | Street FY27 equipment 32,383 | 34,000 or more (+5%) | 32,383 or less | Turns the claim into a fiscal-year line. The check the 13-test reviewer said would reopen the candidate |
| | (e) The FY26 window closes: (FY26 equipment less acquisitions) / 23,771 | 1.03 | 24,484 or more (H2 organic equipment of 14,074 or more) | below 23,771 (H2 organic below 13,361) | First completed window that demanded double-digit growth (+13.6%) |
| | (f) FY26 revenue | Guide top 46,500; Street 46,240 | above 46,500 | below 45,500 | |
| | (g) FY27 revenue guide, midpoint | Street 53,029 | At or above the Street (one lens used 54,500) | Not a fail by itself | The January 2026 guide started 2% to 6% below its schedule and was raised twice |
| **Late April 2027**, Q1 10-Q (prior 2025-04-23, 2026-04-22) | (h) Cumulative equipment revenue Q3'26 to Q1'27 | Street 22,497 (71.2% of Y1). Earlier June windows stood at 78.5% and 79.6% at this point | 23,712 or more (75% of Y1; on track for 1.00) | 22,497 or less | |
| **Late July 2027**, Q2 10-Q (prior 2025-07-23, 2026-07-22) | (i) Four-quarter equipment revenue | Street 30,245; schedule 31,616 | 31,616 or more | 30,781 or less (top of the Street's range) | Final |

Lookup for test (a): equipment RPO at 9/30/26 (rows) x the one-year share printed (columns), against 31,314.

| RPO | 33% | 34% | 35% | 36% |
|---|---|---|---|---|
| 92,000 | 30,360 (-3.0%) | 31,280 (-0.1%) | 32,200 (+2.8%) | 33,120 (+5.8%) |
| 94,000 | 31,020 (-0.9%) | 31,960 (+2.1%) | 32,900 (+5.1%) | 33,840 (+8.1%) |
| 96,000 | 31,680 (+1.2%) | 32,640 (+4.2%) | 33,600 (+7.3%) | 34,560 (+10.4%) |
| 98,000 | 32,340 (+3.3%) | 33,320 (+6.4%) | 34,300 (+9.5%) | 35,280 (+12.7%) |
| 100,000 | 33,000 (+5.4%) | 34,000 (+8.6%) | 35,000 (+11.8%) | 36,000 (+15.0%) |

Lookup for test (d): equipment RPO at 12/31/26 x share, against 32,383.

| RPO | 31% | 32% | 33% | 34% | 35% |
|---|---|---|---|---|---|
| 98,000 | 30,380 (-6.2%) | 31,360 (-3.2%) | 32,340 (-0.1%) | 33,320 (+2.9%) | 34,300 (+5.9%) |
| 102,000 | 31,620 (-2.4%) | 32,640 (+0.8%) | 33,660 (+3.9%) | 34,680 (+7.1%) | 35,700 (+10.2%) |
| 106,000 | 32,860 (+1.5%) | 33,920 (+4.7%) | 34,980 (+8.0%) | 36,040 (+11.3%) | 37,100 (+14.6%) |
| 110,000 | 34,100 (+5.3%) | 35,200 (+8.7%) | 36,300 (+12.1%) | 37,400 (+15.5%) | 38,500 (+18.9%) |

Kill-rule candidates (measurable; the team writes its own):

| # | Date | Condition | What it would show |
|---|---|---|---|
| K1 | 2026-10-28 | New one-year amount at 9/30/26 at or below $31.3B | The schedule no longer differs from the Street |
| K2 | Late January 2027 | FY26 organic equipment below $23,771M (ratio under 1.00) and the 10-K one-year amount at or below $32.4B | The first high-demand window missed and the next year's schedule equals the Street |
| K3 | Any report | Cumulative equipment revenue from Q3 2026 more than 2% below the Street's cumulative path (7,482 / 15,821 / 22,497 / 30,245) | Slippage, as in the 12/31/23 window |
| K4 | Any date | A disclosed deferral or cancellation of scheduled deliveries larger than about $1.4B (the floor gap) | Customer counter-move |

Risks set aside, each with the observation that would show it is not noise:

| Risk set aside | Observation that would show it matters |
|---|---|
| Rounding of the 36% | The next filing prints a share that implies Y1 fell (table above) |
| Soft Street sub-line | A MODL pull for Q4'26 to Q2'27 shows medians more than 3% above the means |
| Currency | Dollar strengthens: the "foreign currency effect" line in the organic reconciliation turns negative by more than 1% of equipment revenue |
| Deliveries slip | Gas GW shipped in Q3 2026 (10-Q units table) below 4.5 against the 5 GW guide |
| Revenue beats do not move the stock | Report-day move negative on 2026-10-28 with a revenue beat and a held margin guide (as on 2026-07-22) |

---

## 7. The ten hardest questions

| # | Question | Facts that answer it | Weakest point |
|---|---|---|---|
| 1 | The gap is about 5%. Why would the stock move on that? | Section 4.3: the estimate leg is +1.6 to +8.4 points; one turn of the multiple is 3.7% to 4.5%. Revenue surprises of +8.7% / +7.9% / +0.6% / +3.3% over the last four reports (+5.1% on the sum; a second vendor gives +9.0% / +7.3% / +1.6% / +2.9%, +5.2%) came with day moves of -1.6% / +2.7% / +13.8% / -8.7% | It does not, by itself. The return in any target above about +10% is the multiple and the Street's own growth |
| 2 | Management knows its schedule and still guided FY26 in line with the Street. Who is wrong? | The January 2026 guide implied 0.94 to 0.98 of the 12/31/25 schedule; after two raises it implies 0.98 to 1.05. Guides were raised in April (+$0.5B) and July (+$1.0B). Y1 rose $2,764M in the quarter; the Street's window rose $1,289M | Management's Q3 guide equals the Street. The data cannot tell a cautious guide from a back-loaded schedule |
| 3 | Is the back-test error bigger than the gap? | Std dev 6.0% (2.8% post-spin); leave-one-out error 6.4%; about two independent years. Gap is 1.0 to 1.6 times the error. Floor gap of 4.5% is inside the error | Yes on the floor. A repeat of the one miss puts revenue 4% below the Street |
| 4 | The schedule asks for +34% growth. Has GEV ever delivered that? | No completed window asked for more than +13.1%, and that one missed by 8.2%. Correlation of the ratio with demanded growth is -0.93. H1 2026 equipment grew +28.8% reported, +14.5% without Prolec and +12% organic on GEV's definition (which also removes currency); the Street already has +28.4% for the window | The multiplier is applied outside its sample. The first test of a high-demand window is the FY26 close in late January 2027 |
| 5 | Where physically does the extra $1.4B to $2.3B come from? | Wind cannot hold it: the Street already has Wind converting 71.1% of its backlog against 58.5% to 69.3% reported. Power + Electrification scheduled is at least 25,786 against the Street's 24,415 | Gas output is guided at 20 GW for the window (+37%) and the Street's Power equipment is already +47.5%. If Power is capped, H1 2027 Electrification equipment must be 21% to 33% above the Street, and management's Q3 Electrification guide equals the Street. The Power / Electrification split is not disclosed |
| 6 | Is the Street number real? | Total revenue: 28 and 22 brokers; ties to the annual figure (53,096 vs 53,029); a second vendor is within 0.2% on H2 2026. Equipment: the Street is below the schedule on all eight readings tested | The equipment split has no visible contributor count, a likely stale model without Prolec (Electrification equipment low 2,301 vs mean 3,299), and a 4% spread between Bloomberg's own readings |
| 7 | Timing or level? | Months 13 to 24: Street 35,137 vs 25,468 scheduled, no gap. Two-year: Street 1.145x the schedule vs 1.28x to 1.48x in three completed windows | Timing, on this evidence. Then the NTM windows at 10 to 12 months do not contain the thesis period (section 4.1) |
| 8 | What does it do to margin and cash? | EBITDA +1.5% to +6.6% of $8,210M. Below a 16.4% drop-through the margin percentage falls. FCF sign not identified | The stock fell 8.7% on 2026-07-22 with a revenue beat, a raised revenue guide and a held margin guide. Possible services offset of -$150M to -$310M |
| 9 | Is this already known or already priced? | The 36% is quoted in the press (2026-07-23, 2026-08-22) as slow conversion, not multiplied out. The multiplication was not found in 9,715 corpus documents or in web searches (re-run 2026-10-01). FY27 revenue consensus rose 5.5% in eight months | The outcome it predicts (revenue about 5% above consensus) is what GEV has delivered for four quarters. One published estimate already has FY27 revenue at $54.5B (+2.8%). Paid broker notes could not be read |
| 10 | What multiple do you exit on, and what if it falls? | Section 4.4. Break-even on Street numbers: 26.2x in January, 22.6x in July, 21.6x in October 2027. 52-week low 27.3x; no week at or below 26x in the last year | The peer line points to 24.6x by January and 21.2x by next September. At 24.6x in January the price is -6% on the Street and -1% to 0% on the +5% to +6.6% paths. The 2025 sell-off reached 18.5x |

Two more that came up in the checks:
- "The one-year share fell from 42% to 36%. Is that not a slowdown?" The dollar amount rose 51% (20,879 to 31,616). The share falls because long-dated gas orders were added to the denominator.
- "Can you redo it live?" Every number on the line can be redone by hand from one 10-Q sentence, ten earlier sentences, the XBRL equipment revenue line and three Bloomberg rows (sections 2.1 and 2.2).

---

## 8. What to hand-check first, and what is single-source

Hand-check, in this order:

| # | Check | Where | Expected |
|---|---|---|---|
| 1 | The RPO sentence | 10-Q Q2 2026 PDF, RPO note (page 15 or 16) | "Equipment-related RPO of $87,821 million of which 36%, 65%, and 97%" |
| 2 | The multiplication | Calculator | 87,821 x 0.36 = 31,616 |
| 3 | The Street rows | `01-eeo-company-specific.xlsx`, "Multiple Periods", rows 24, 27, 30, columns F:I | Sum 30,245 |
| 4 | Two back-test windows by hand | 10-K 2024 RPO note (43,047; 44%) and FY25 equipment revenue (20,934); 10-Q Q2 2025 (49,712; 42%) and the next four quarters (5,880 + 5,963 + 5,254 + 6,459 = 23,556, less Prolec 1,303) | 1.105 and 1.066 |
| 5 | Prolec equipment lines | 10-Q Q1 and Q2 2026, "Equipment and services organic revenues", "Less: Acquisitions" | 469; 834 (six months 1,303) |
| 6 | Division equipment RPO | 10-Q Q2 2026 MD&A segment tables | 39,261 / 8,197 / 40,589 |
| 7 | Price bridge | Snapshot sheet row 3 | (28.544 x 8,923 + 8,298) / 266.334 = $987.45 |
| 8 | Report date | gevernova.com/investors/events | October 28, 2026, 7:30 am ET |

Terminal pulls that would firm up the Street side: MODL for Q4 2026, Q1 2027 and Q2 2027 (medians and the product-revenue line); EEO broker detail for the three division equipment rows (contributor count and dates).

Single-source or assumed:

| Item | Status |
|---|---|
| Street equipment split by division | Bloomberg only; contributor count not visible; no second vendor |
| Electrification services-row correction (331 to 481) | One lens (`propose_electrification.md`); not re-derived here |
| Prolec equipment revenue in Q3-Q4 2026 (850 to 1,000 a quarter) | Assumption; disclosed only after each quarter |
| EDF-disposal adjustment to the 12/31/23 window | Assumes $350M of removed revenue and a 25% to 51% one-year share; neither disclosed |
| Division equipment RPO before 6/30/25 (used for Wind turnover history) | Taken from the lens files; three of eleven dates re-read in the filing for this file |
| Pre-report revenue consensus for Q3 2025 and Q1 2026 | Benzinga; MarketBeat now gives a second reading within 1 point for all four quarters |
| Lark Research FY27 revenue $54.5B | One source |
| Bottom-up H1 2027 equipment count ($14.4B to $15.2B) | One lens; not re-run |
| Naive-model error (3.2%), leave-one-out error (6.4%), EDF adjustment | From the 13-test checker's working; not re-run here |
| Correlation of revenue surprise with report-day move (-0.22) | One lens; not re-run |
| Drop-through on extra equipment revenue | Not disclosed; bracketed by gross margin (10% to 13%) and segment margins (19% to 20%) |
| Peer regression (24.6x) | Re-run here, same result; rests on Bloom Energy |
| Whether a broker note already uses the schedule | Unknown; paid research not readable |

---

## 9. Sources and working

- Bloomberg, 2026-10-01: `data/bloomberg/GEV_Pull_2026-10-01/01-eeo-company-specific.xlsx`, `segment_quarterly.json`, `06_modl.xlsx`; `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` (Snapshot, Consensus, ConsensusHistory, Multiples).
- GEV filings in `data/gev.db` (read-only): RPO-note sentences in chunks 5683, 13656, 29868, 38506, 44098, 54581, 67387, 77798, 83462, 90281, 89498; organic reconciliation chunks 5768 and 13731; segment RPO chunks 5735, 5737, 5740.
- XBRL: `data/financials/gev_segments.csv`, `gev_facts_long.csv`, `gev_quarterly.csv`.
- Checkers' working: `verify_equipment-revenue-vs-rpo-schedule_reproduce.md`, `_already-known.md`, `_wedge-tests.md` (this folder). Lens files: `propose_rpo-equipment.md`, `propose_street-identity.md`, `propose_wind.md`, `propose_price-implied.md`, `propose_january-event.md`, `propose_electrification.md`.
- Web, 2026-10-01: gevernova.com/investors/events (Q3 webcast date); marketbeat.com/stocks/NYSE/GEV/earnings (revenue estimates and actuals); fool.com 2026-08-22 and ebc.com 2026-07-23 (the 36% quoted, not multiplied out).
- Model shell: `data/model/GEV_model_shell.xlsx`.
- Scripts for this file (session scratchpad, folder `cand_eqrpo`): `core.py` (schedules, back-test), `extra.py` (open windows, forms, lookups), `margins.py`, `profit.py`, `qtab.py`, `price.py`, `fin.py`, `reg.py`, `hist.py`.
