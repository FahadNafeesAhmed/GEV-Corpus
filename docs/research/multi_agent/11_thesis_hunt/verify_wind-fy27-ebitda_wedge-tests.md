# Verify: wind-fy27-ebitda against the wedge tests (2026-10-01)

_AI-assisted research input only: facts, arithmetic, tables and sources. No memo sentences, no forecast choices (ranges and methods only). Bloomberg figures are licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep inside the project folder._

**Verdict: does not survive as a wedge. Keep as a model input (a haircut range on the Wind line) and as a known offset to the long-side candidates.**

Fails 6 of 13 tests, including two of the four that must pass (distance on the line the price reflects, error band).

## 1. What was re-computed from the primary files

| Item | Candidate | Re-computed | Source |
|---|---|---|---|
| Street Wind adj. EBITDA FY27 | +188 (-9 / -12 / +59 / +150) | +187.7 (-9.2 / -11.8 / +58.6 / +150.0); company-basis EBITDA line +188.5 | `segment_quarterly.json`, keys `Adjusted EBITDA||Wind|2027 Qn`, `EBITDA||Wind|2027 Qn` |
| Street FY26 Wind | -449 | -382 - 275 + 24.6 + 183.2 = -449.2 | same; H1 actual from `gev_segments.csv` |
| Street H1 2027 | -21 on revenue 3,388 | -20.9 on 3,388.0 | same |
| Street 2027 Wind revenue / offshore | 7,589 / 795 | 7,588.5 / 794.6 (onshore line 6,873.4; revenue less offshore 6,793.9) | same |
| Wind EBITDA 2024, 2025, H1 2026 | -588, -598, -657 | -588, -598, -657 | `gev_segments.csv` (XBRL) |
| H1 EBITDA 2024, 2025 | -290, -312 | -290, -311 | same |
| Offshore revenue 2024, 2025, H1 2026 | 1,377; 652; 551 | 1,377; 652; 551 | same |
| Incremental offshore contract losses | 379 / 1,005 / 637 | 379 / 1,005 / 637 | 10-K 2025 revenue-recognition note (accession 0001996810-26-000015) |
| Offshore loss by subtraction | 1,133-1,171; 1,190-1,280; 690-830 | 1,133-1,171; 1,190-1,275; 688-832 | arithmetic |
| Loss / opening backlog | 28-29%, 40-43%, 35-42% | 28.3-29.3%, 39.7-42.7%, 34.5-41.5% | arithmetic |
| FY27 build | -328 / -67 / +196 | -328 / -67 / +196 | arithmetic |
| Share of company EBITDA | 2.7% (range +0.1% to -5.4%) | 2.69% (+0.1% to -5.4%) | 255 / 9,471 |

The arithmetic reproduces. The problems are in the inputs and in what the arithmetic can prove.

## 2. Input checks that change the picture

1. **Opening 2027 offshore backlog is lower than the 1.0-1.4B used.** Investor update 12/9/2025, slide 19 ("Year-end equipment backlog"): bars for 2023 "~$4B", 2024 "~$3B", 2025E "~$2B", and a 2026E bar with no label. Measured bar heights put 2026E at about 48% of the 2025E bar, so about $0.85-1.0B. Cross-check: ~2.0B less 2026 offshore revenue of 885 (H1 actual 551 + Street H2 334) = about 1.1B. Supported range: 0.85-1.1B. The 1.4B top end has no support.
2. **The loss ratio is not a mechanical rate.** The 10-K policy says a loss is provided "when it is expected that we will incur such loss", and the incremental losses came "primarily as a result of changes in product and project cost estimates". Once a loss is provided, remaining backlog burns at about zero margin. A further loss needs a new estimate change. The ratio therefore forecasts future surprises, it does not compute a scheduled cost.
3. **The 2024-2025 surprises were tied to one project that is now finished and settled.** 2024: blade failure and removal of installed blades at Vineyard Wind. 4Q25: accrual for the US stop-work order of 12/22/2025 at Vineyard Wind (CFO, 1/28/2026 call: without it the segment "was on the path" to the -400 guide). Vineyard installation was completed in 1Q26 and all disputes were settled on 9/16/2026. What is left is Dogger Bank B and C (UK).
4. **Only two of the three ratio points are observations.** The 2026 point (35-42%) is built from the company's -400 guide and the December 2025 "mid-single digit" onshore comment. It is not a reported result.
5. **The numerator rests on spoken margins that disagree with each other.** 2024 onshore is "approximately 7%" on the January 2025 call but "high single digit" in the 2025 proxy letter (DEF 14A filed 3/28/2025). One point of onshore margin is $68M on 2027 revenue.
6. **The offshore loss is far larger than the disclosed charges.** By the candidate's subtraction the 2025 offshore loss is 1,190-1,275 against incremental contract losses of 637, and the 2024 loss is 1,133-1,171 against 1,005 of charges less a 300 gain. That leaves an unexplained 430-640 a year (overhead, factory under-absorption, a supply-agreement termination in 1Q25, tariffs, LM Wind). Either the onshore margin was lower than stated or offshore carries a large fixed cost. The split is not known to within a few hundred million.
7. **The 2026 profile inside the year does not fit a steady rate.** H1 2026 was -657. The -400 guide implies H2 2026 of +257 (3Q "approximately break-even", so 4Q about +257); the Street has H2 at +208. The 2Q26 call gave "lower project costs for Offshore" as a reason for the 3Q guide.
8. **Management is on record against the candidate, two weeks ago.** Conference transcript 9/16/2026: "we're reaching a profitability pivot point in Wind", profitability "will be much better in the second half of the year than the first, and '27 will be much better than '26", "we've really governed our Offshore Wind economics". The same management will write the January 2027 guide.
9. **The Wind consensus is thin.** `06_modl.xlsx` (3Q26): Wind adj. EBITDA mean 24.63, low -9, high 106.39, median 0.57. The mean reproduces exactly with four contributors ((-9 + 106.39 + 2 x 0.57) / 4 = 24.63), so one high estimate lifts the mean by about 24. Company adj. EBITDA has 36 contributors. Low / high / count for the 2027 Wind quarters are not on the export.

## 3. Back-tests

**A. The candidate's method, out of sample.** At the start of 2025 the inputs were: onshore guide "high single digit" (7-9%) on revenue that came in at 8,458 (onshore + LM), opening offshore backlog ~3.0B, and the one known ratio (2024: 28.3-29.3%).

| | Low | High |
|---|---|---|
| Onshore 7-9% x 8,458 | 592 | 761 |
| Offshore loss 28.3-29.3% x 3,000 | (879) | (849) |
| Predicted 2025 Wind EBITDA | (287) | (88) |
| Actual | (598) | (598) |
| Error | (311) | (510) |

One true out-of-sample year, error $311-510M. The claimed 2027 gap is $255M. The error is larger than the gap.

**B. Company Wind guide against the result (the Street tracks the guide).**

| Year | First guide | Last guide before year end | Actual | Miss vs first guide |
|---|---|---|---|---|
| 2024 | "approaching profitability" (8-K 4/25/2024, 7/24/2024) | "nearly 50% segment EBITDA improvement", about -520 (8-K 10/23/2024) | (588) | about (490) to (590) |
| 2025 | loss of 200-400 (8-K 4/23/2025) | about (400) (8-K 10/22/2025; investor update 12/9/2025) | (598) | (198) to (398) |
| 2026 | about (400) (12/9/2025; held 7/22/2026) | n/a | H1 (657); Street FY (449) | open |

Two complete years, both missed on the loss side by $200-590M. This supports the direction of the candidate. It is two observations, each with a named one-off cause, and it is not arithmetic on a disclosed schedule.

**C. Two alternative builds (method checks, not forecasts).**

| Build | Inputs | Range | Mid |
|---|---|---|---|
| A: candidate's method with the supported backlog | onshore 4-7% x 6,794; loss 28-43% x 0.85-1.1B | (201) to +238 | about +13 (5.5%, 37%, 0.975B) |
| C: second-half 2026 run rate | H2 2026 Wind +208 (Street) to +257 (guide) less H2 onshore 9-12% x 4,310 gives H2 offshore (131) to (309); doubled for 2027; onshore 4-7% x 6,794 | (347) to +214 | about (66) |
| Candidate | as submitted | (328) to +196 | (67) |

Across the three: about (350) to +240, mid-points (67) to +13. The Street's +188 is inside every range, near the top.

**D. First-half comparison (the strongest piece of the candidate).** Street H1 2027: (21) on revenue 3,388 and 1,882 MW delivered (Bloomberg, 2026-10-01). Actual H1 2026: (657) on 3,458 and about 2,000 MW. Same volume, $636M better. Before incremental offshore charges, H1 2024 and H1 2025 were both (187) on 2.7 and 3.0 GW. Items that could close the $636M: no repeat of the unprotected-tariff shipments (about $70M in 1Q26 alone), onshore services margin (management: "double-digit margin expansion" year over year in 1Q26; H1 services revenue about 1.1-1.2B), no repeat of the H1 2026 offshore charges (amount not disclosed), cost reduction. None of these is quantified in a filing, so the $636M cannot be split.

## 4. The 13 tests

| # | Test | Result | Evidence |
|---|---|---|---|
| 1 | Line-item | PASS | Wind segment adjusted EBITDA, FY2027, Street +188 (Bloomberg, 2026-10-01). Named line, sourced number, named year. |
| 2 | Consensus-side | PASS, qualified | The view rebutted is the consensus mean and the company's own stated direction, not an outlier. But the Wind line has about 4 contributors and one high estimate moves the mean. |
| 3 | Distance | FAIL | -136% is a ratio to a number near zero and has no meaning. On company adj. EBITDA the gap is 2.7% (1.8% with the supported backlog), far below the 7-22% band. On Wind revenue it is 3.4 margin points. The playbook reads a near-zero gap on the priced line as a call on the multiple. |
| 4 | Ratio | FAIL | $255M at the current 28.5x is $7.3B of enterprise value, $27 a share, 2.8% of the price. At a 10x segment multiple it is under $10 a share. Any short target of 15% or more would be over 80% multiple change, and the candidate gives no evidence for one. |
| 5 | Physical quantity | PASS, weak | Checkable in seconds: Street H1 2027 Wind at (21) on 1,882 MW against H1 2026 at (657) on about 2,000 MW. The offshore-loss figure itself is not disclosed and cannot be checked directly. |
| 6 | Rival explanation | FAIL | The same Street number can come from tariffs not repeating, services margin, no new offshore charges, or cost cuts. The onshore / offshore split is backed out from spoken margin ranges with a 430-640 unexplained residual (section 2, items 5 and 6). The candidate cannot show which variable moves. |
| 7 | Error band | FAIL | Candidate range (328) to +196 contains the Street. Half-width 262 against a gap of 255. Out-of-sample back-test error 311-510 (section 3A). |
| 8 | Why missed | PASS, weak | Offshore profit is not disclosed (a real, checkable gap). But the inputs (Dogger Bank B and C through "the better part of '27", backlog slide, "expect to reduce EBITDA losses") are all in calls and decks, and there is no evidence the Street has not read them. The Street is taking management's word. |
| 9 | Already priced | PASS | Not in the price. The stock rose 4.8% on 9/16/2026 (settlement and conference). Caveat that cuts against use as a wedge: the stock has not fallen on Wind misses (FY25 Wind at (598) against a (400) guide, reported 1/28/2026: stock +2.7%; 1Q26 Wind at (382), 4/22/2026: stock +13.7%). |
| 10 | Cash | PASS | Segment EBITDA and, with a lag, cash. |
| 11 | Reveal date | PASS, qualified | Company number on known dates inside the horizon: FY27 Wind guide and 1Q27 Wind guide in late January 2027; 1Q27 and 2Q27 results in late April and late July 2027; early read 10/28/2026. Pass marks are set. Qualifier: the January event is a guide written by a management that said "pivot point" on 9/16/2026, and section 3B shows guides run above results. The January read is more likely to go against the candidate than for it; the results that could confirm it come in April and July 2027. The FY27 actual comes in January 2028, outside the horizon. |
| 12 | Counter-move | FAIL | Not stressed. Management has settled claims (Vineyard, 9/16/2026), booked gains on cancelled contracts ($300M in 3Q24; a supply-agreement termination in 1Q25), is pursuing tariff recovery (10-Q 2Q26), is cutting cost and merging offshore functions into onshore (slide 19), and controls the timing of estimate changes. Each can move the 2027 line by $100M or more. |
| 13 | Multiple consistency | FAIL | No target and no exit multiple. A 2.7% EBITDA change is consistent with no change in the multiple, so the candidate cannot carry a short on its own. |

Count: 7 pass (4 of them qualified or weak), 6 fail. Required passes: line-item yes, reveal-date yes (qualified), distance no, error band no.

## 5. Corrected numbers for the model (ranges and methods only)

- Street: Wind adj. EBITDA FY27 +188; H1 2027 (21); about 4 contributors (Bloomberg, 2026-10-01).
- Arithmetic range across three builds: about (350) to +240. Mid-points (67) to +13.
- Gap at the mid-points: (175) to (255), which is 1.8% to 2.7% of Street FY27 adj. EBITDA of 9,471.
- The band is wider than the gap in every build.
- Test levels to watch: 3Q26 Wind against the "approximately break-even" guide (10/28/2026); the implied 4Q26 (about +257 needed for the (400) guide); FY27 and 1Q27 Wind guides (late January 2027); the 2026 incremental offshore loss in the FY26 10-K; H1 2027 Wind against the Street's (21).

## 6. Sources

- Bloomberg, 2026-10-01: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `06_modl.xlsx`, `01-eeo-company-specific.xlsx`; `data/bloomberg/street_segments_annual_2026-10-01.csv`.
- `data/financials/gev_segments.csv` (XBRL segment history).
- Corpus `gev.db`: 10-Q 2Q26 (0001996810-26-000148, Wind MD&A p.31); 10-K 2025 (0001996810-26-000015, Wind MD&A p.27, revenue-recognition note); earnings releases 4/25/2024, 7/24/2024, 10/23/2024, 4/23/2025, 7/23/2025, 10/22/2025, 7/22/2026; DEF 14A 3/28/2025; 2Q26 call transcript (source 3161); 4Q25 call transcript (source 2660); 3Q25 call transcript (source 3771); price table.
- Company website copies held in the session scratch folder: investor update 12/9/2025 deck (slide 19, slide 7) and transcript; 1Q26 call transcript 4/22/2026; conference transcript 9/16/2026.
- Proposal under test: `propose_wind.md` in this folder.
