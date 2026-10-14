# Checker working: wind-h1-27-equipment-revenue against the 13 wedge tests (2026-10-01)

_AI-assisted research input only: facts, arithmetic, tables and sources. No memo sentences and no forecast choices; ranges and methods only. Bloomberg figures are licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep inside the project folder._

**Verdict: does not survive as a stand-alone wedge.** 5 tests pass (2 of them only with caveats), 8 fail. The must-pass error-band test fails. Two factual corrections change the candidate's numbers. What is left is a direction (Street H1 2027 Wind equipment looks high rather than low) that is usable as a supporting bound, not as a thesis.

## 0. Sources

| Tag | Source | Where |
|---|---|---|
| BBG | Bloomberg, 2026-10-01 | `data/bloomberg/GEV_Pull_2026-10-01/01-eeo-company-specific.xlsx` sheet "Multiple Periods" rows 19, 26-28; `segment_quarterly.json`; `06_modl.xlsx` rows 19, 27 |
| 10-Q / 10-K | Wind MD&A tables (units, GW, equipment RPO, equipment and offshore revenue) | corpus `gev.db` documents, accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148 |
| DECK 2Q26 | Earnings deck 2026-07-22, page 17 "Wind: key performance metrics" | corpus source 3157 |
| DECK 4Q25, 4Q24, 2Q24 | Earnings decks 2026-01-28, 2025-01-22, 2024-07-24, same page | gevernova.com `gev_webcast_presentation_01282026.pdf`, `_01222025.pdf`, `_07242024.pdf` (fetched 2026-10-01) |
| PR | Earnings releases, Wind segment table (total orders) | corpus documents 326, 291, 277, 268, 265, 226, 215 |
| CALL 2Q26 | Call transcript 2026-07-22 | corpus source 3161 |
| CONF | Conference coverage 2026-09-16/18 (secondary) | corpus sources 681, 3750 |
| TAX | Peer 10-K descriptions of the July 2025 tax law (wind must begin construction by 4 July 2026 or be in service by 31 Dec 2027) | corpus chunks 24201, 307419, 312370, 313456 |

Script: scratchpad `windcheck.py` (all figures below are its output).

## 1. Reproduction of the candidate's numbers

| Item | Candidate | Recomputed | Match |
|---|---|---|---|
| Street Wind equipment Q1'27 + Q2'27 | 1,019 + 1,259 = 2,278 | 1,019.0 + 1,258.7 = 2,277.8 (row 27, columns H-I) | yes |
| H1'26 actual | 2,283-2,284 | 889 + 1,395 = 2,284 (segment basis) | yes |
| Street MW delivered H1'27 | 1,882 | 693.7 + 1,188.2 = 1,881.8 | yes |
| Street offshore revenue H1'27 | 390 | 178.0 + 211.6 = 389.5 | yes |
| Implied equipment orders H1'24, H2'24, H1'25, H2'25, H1'26 | 2,325; 2,704; 2,203; 3,413; 1,368 | 2,338; 2,720; 2,220; 3,423; 1,369 (segment basis; candidate used external-only revenue) | yes |
| k on implied orders | 1.19, 1.41, 0.79; Street needs 1.38 | 1.189, 1.404, 0.781; Street needs 1.379 | yes |
| Four-quarter Street / equipment RPO | 71.1% vs 58.5-69.3% | 71.1% vs 58.7-69.5% (seven reported windows) | yes |

The arithmetic reproduces. The problems are in the inputs and in the reading.

## 2. Two corrections

### 2a. Wind equipment orders in dollars ARE published

The candidate's "why missed" says GEV does not publish Wind equipment orders in dollars. That is true of the 10-Q but not of the company's disclosure. The earnings deck prints them every quarter (DECK 2Q26 p.17: "Orders ($M) ... Equipment 1,614 / 721 (55)% ... YTD 1,816 / 1,460 (19)%"). They also equal segment orders in the release less services orders.

| Half | Reported equipment orders $M | Candidate's implied orders $M | Difference | Source of reported |
|---|---|---|---|---|
| H1 2023 | 5,121 | n/a | | DECK 2Q24 |
| H2 2023 | 4,816 (9,937 - 5,121) | n/a | | DECK 4Q24 |
| H1 2024 | 2,518 | 2,338 | -180 | DECK 2Q24 |
| H2 2024 | 2,929 (5,447 - 2,518) | 2,720 | -209 | DECK 4Q24 |
| H1 2025 | 1,816 | 2,220 | **+404** | DECK 2Q26 |
| H2 2025 | 3,656 (5,472 - 1,816) | 3,423 | -233 | DECK 4Q25 |
| H1 2026 | 1,460 | 1,369 | -91 | DECK 2Q26 |

- Reported H1'26 vs H1'25: **-19.6%** (deck: -19% organic). Implied: -38.3%. The implied figure doubles the decline because the H1'25 backlog change carried about +$404M of non-order movement (currency revaluation and contract changes).
- Total Wind orders H1'26 vs H1'25: 2,448 vs 2,702 = -9% (PR 2Q26).
- The title's "33-44%" is GW (1.2 vs 1.8) and units (342 vs 609). Both are correct. The dollar line that feeds a dollar revenue forecast fell 20%.
- Order value per MW rose: 1.01 (H1'24), 1.05, 1.01 (H1'25), 1.18 (H2'25), 1.22 (H1'26) $M per MW.

### 2b. k recomputed on reported orders

k = (Wind equipment revenue - offshore revenue) / reported equipment orders two halves earlier.

| Revenue half | Equipment rev | Offshore rev | Numerator | Orders two halves earlier | k (reported) | k (candidate, implied) |
|---|---|---|---|---|---|---|
| H1 2025 | 3,209 | 430 | 2,779 | 2,518 | 1.104 | 1.19 |
| H2 2025 | 4,042 | 223 | 3,819 | 2,929 | 1.304 | 1.41 |
| H1 2026 | 2,284 | 551 | 1,733 | 1,816 | 0.954 | 0.79 |
| H2 2026 (Street) | 3,552 | 334 | 3,218 | 3,656 | 0.880 | 0.94 |
| **H1 2027 (Street)** | 2,278 | 390 | 1,888 | 1,460 | **1.293 needed** | 1.38 needed |

- Reported range 0.954-1.304, mean 1.121, standard deviation 0.175 (three points). The Street's 1.293 is **inside** the range, at the top.
- H1'27 equipment at k = 0.954 / 1.121 / 1.304, plus Street offshore 390: **1,783 / 2,026 / 2,293** = **-21.7% / -11.1% / +0.7%** against 2,278.
- Even on the candidate's own implied-order k the Street (1.38) is below the highest observation (1.40). The candidate's range of 0.79-1.19 dropped that observation.
- Two earlier, contaminated observations (2023 orders included a cancelled offshore order and one very large multi-year US order): H1'24 k = 0.41, H2'24 k = 0.95. k is not a stable constant.

## 3. Other lenses on the same line

| Lens | History | Street H1'27 | H1'27 implied | vs Street 2,278 |
|---|---|---|---|---|
| k on reported $ orders (section 2b) | 0.95-1.30 | 1.29 | 1,783-2,293 | -22% to +1% |
| H1 equipment / prior H2 equipment | 0.620, 0.623, 0.565 | 0.641 | 2,007-2,215 (on Street H2'26 3,552) | -12% to -3% |
| GW sold / GW ordered a year earlier | 1.20, 1.39, 1.11 | 1.57 (1.51-1.64 for rounding of 1.2 GW) | above range | supports candidate |
| Units sold / units ordered a year earlier | 1.05, 1.19, 0.85 | about 1.42 (1,882 MW at 3.87 MW per unit = 486 units / 342) | above range | supports candidate |
| Same, at the H1'26 order price of $1.22M per MW | | 1,888 / 1.22 = 1,552 MW = 1.29 x GW ordered | inside range | neutral |
| Four-quarter onshore-type equipment revenue / orders of the matching four quarters | 1.21, 1.17 | 1.00 (5,106 / 5,116) | Street is BELOW history on the year | against candidate |
| Four-quarter equipment revenue / blended equipment RPO | 58.7-69.5% | 71.1% | above range, but offshore run-off lifts the blended ratio | weak support |
| Same, onshore only (propose_wind.md T2) | 72.8-85.1% | 79.4% | inside range | neutral |

Reading: the Street's four-quarter Wind equipment figure is not high. What looks high is the share of it placed in H1 2027 rather than H2 2026. H2 2026 is anchored by company guidance (FY26 Wind organic revenue down low double digits; Street H2 revenue 4,685 vs guide-implied 4.5-4.8B, propose_wind.md T1), so the claim reduces to a timing split between two halves.

## 4. Back-test error of the method

| Test | Predicted | Actual (numerator) | Error on numerator | Error on total equipment line |
|---|---|---|---|---|
| H2'25 from k of H1'25 (1.104) | 3,233 | 3,819 | -15.4% | -14.5% |
| H1'26 from mean k of the two earlier halves (1.204) | 2,186 | 1,733 | +26.1% | +19.8% |
| H1'26 from same-half k (H1'25) | 2,004 | 1,733 | +15.7% | +11.9% |
| Leave-one-out H1'25 / H2'25 / H1'26 | | | +2.3% / -21.1% / +26.1% | +2.0% / -19.9% / +19.8% |
| Implied-orders version, H1'26 from mean prior k | | | | +50.1% |

One-step-ahead error on the line: about 15-20% in absolute terms (mean 17%), on two usable tests. Corrected central gap: -11%. Candidate's claimed central gap: -23%. Street's own dispersion on the nearest quarter (Q3'26 Wind equipment, BBG MODL): mean 1,789, low 1,274, high 2,244 = -29% / +25%.

## 5. The 13 tests

| # | Test | Result | Evidence |
|---|---|---|---|
| 1 | Line-item | **Pass** | Wind equipment revenue, Q1'27 + Q2'27, Street 2,278 (BBG row 27, H-I). Caveat: contributor count not shown; Street sub-lines come from different broker sets (Q1'27 onshore + offshore = 1,428 vs Wind total 1,522). |
| 2 | Consensus-side | **Pass, with caveat** | It is the Bloomberg mean, not an outlier. But this line is 9% of Street H1'27 revenue (2,278 / 24,111) and the segment's EBITDA is about zero; the price does not rest on it. |
| 3 | Distance | **Pass, weak** | Corrected central -11% (range -22% to +1%); seasonal lens -3% to -12%. Candidate's -23% is not reproduced as a central figure. At company level the gap is 1.0% of H1'27 revenue, i.e. near zero. |
| 4 | Ratio | **Fail** | EBITDA effect at the corrected gap: $23-46M central, up to about $100M = 0.2-1.1% of FY27 EBITDA 9,471. At 28.5x that is $0.7-2.9B of enterprise value = $2.5-10.7 a share on $987.45 (0.2-1.1%). Any short target would be almost all multiple, with no multiple evidence in the candidate. |
| 5 | Physical quantity | **Pass, with caveat** | Street 1,882 MW in H1'27 against 1.2 GW / 342 units ordered in H1'26: ratio 1.57 (GW) and about 1.42 (units), above 1.11-1.39 and 0.85-1.19. Checkable in seconds. Caveats: three observations; order price per MW is up about 20%, which brings the needed ratio to 1.29; the Bloomberg MW line may come from different brokers than the revenue line. |
| 6 | Rival explanation | **Fail** | Not separated: (a) price and mix, $/MW of orders 1.01 to 1.22; (b) timing of the large H2'25 order book (3,656): the Street has H2'26 at k = 0.88, the lowest on record, leaving room for spill into H1'27; four-quarter ratio 1.00 vs 1.17-1.21; (c) H2'26 orders shipping by June 2027; (d) repower, which converts faster; (e) currency. |
| 7 | Error band | **Fail** | Back-test error about 15-20% (section 4) against a corrected gap of 11%. Even against the candidate's 23% the band reaches the Street (highest k gives +1%). Two or three data points. |
| 8 | Why missed | **Fail** | The stated gap is wrong: equipment orders in dollars are in every earnings deck (section 2a). The mechanism is said by management on the call (CALL 2Q26: lower deliveries "as a result of soft orders in the first half of 2025"; "the US market for new onshore equipment remains soft"). An input already in an earnings call fails this test. |
| 9 | Already priced | **Fail (not a price driver)** | Wind weakness is public and guided (2028 framework: Wind organic revenue down at a low-double-digit rate from a 2025 base; Street FY27 Wind revenue 7,589, about -7% on FY26; press headline 2026-07-22 on wind weakness). There is no evidence the share price responds to this line. |
| 10 | Cash | **Fail** | Moves EBITDA by $23-100M on an assumed, not derived, 10-20% contribution: 0.6-2.5% of Street H1'27 EBITDA 4,038. Inside one quarter's noise for the company. |
| 11 | Reveal date | **Pass** | Company-reported Wind equipment revenue, about 2027-04-21 and 2027-07-21, inside 12 months, with a pre-set level (kill at 2.2B). Caveats: the full figure needs the July print (month 10); the Street figure will be reset when FY27 Wind guidance is given in late January 2027, so the gap can close before the print. |
| 12 | Counter-move | **Fail** | Shortfall to the Street at k = 0.95-1.12 is $251-495M. Street H2'26 Wind orders 3,271 less services of about 1,050 = about 2,220 of equipment orders; 11-22% of that shipping by 30 June 2027 closes it. Management expects H2 onshore orders "materially higher" than H1 (CONF); about 10 GW of repower already qualified for credits (CALL 2Q26); projects that did not begin construction by 4 July 2026 must be in service by 31 Dec 2027 (TAX), which pulls deliveries into 2027. Not stressed in the candidate. |
| 13 | Multiple consistency | **Fail** | No exit multiple or bear multiple. A line worth about 0.5% of EBITDA cannot carry a view on a 28.5x multiple. |

Count: pass 1, 2, 3, 5, 11. Fail 4, 6, 7, 8, 9, 10, 12, 13. Rule: survive only with at most two fails and passes on line-item, distance, error band and reveal date. Error band fails; eight fail in total.

## 6. Corrected figures for anyone who still uses the line

| | Value | Basis |
|---|---|---|
| Street | $2,278M | Bloomberg, 2026-10-01 |
| Arithmetic range | $1.78B to $2.29B | reported equipment orders 1,460 x k of 0.954 to 1.304, plus Street offshore 390 |
| Mid-point of that range | about $2.03B | k = 1.121 (mean of three) |
| Seasonal cross-check | $2.01B to $2.21B | 0.565-0.623 x Street H2'26 equipment 3,552 |
| Gap to Street | -22% to +1%; about -11% at the mean | |
| Error band on the method | about +/-17% on the line | one-step-ahead back-test, two tests |
| Revenue effect at -11% | about -$250M = 1.0% of Street H1'27 revenue | |
| EBITDA effect | -$23M to -$46M at 10-20% contribution (assumed) | 0.6-1.1% of Street H1'27 EBITDA |

## 7. What still holds

- Supporting use for the equipment-schedule candidate: on every lens the Street's Wind equipment figure for Q3'26-Q2'27 is at or above what Wind has converted before (71.1% of blended equipment RPO vs 58.7-69.5%; inside the range onshore-only). So Wind is not where a shortfall against the company's 36% one-year schedule could sit. That bound does not need this candidate to be right.
- Early read on 2026-10-28: Q3'26 Wind equipment orders in the deck (Street total Wind orders 1,510; equipment about 960-1,000 after services), GW and units in the 10-Q, Wind equipment RPO against 8,197.
- Open items: Wind equipment RPO split onshore / offshore at 30 June 2026 (estimated only); number of brokers behind the Wind equipment and MW lines (not shown on the export); share of H2 orders that are repower or short-cycle.
