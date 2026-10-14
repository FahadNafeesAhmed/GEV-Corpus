# Check: REPRODUCE. Candidate `wind-h1-27-equipment-revenue`

_AI-assisted research input only: facts, arithmetic, tables and sources. No memo sentences and no forecast choices. Bloomberg figures are licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep inside the project folder._

Working date 2026-10-01. All figures $M unless stated.

## 0. Verdict

| Item | Result |
|---|---|
| Survives as a stand-alone candidate | **No** |
| Numbers reproduce from primary files | Yes for the Street figures, RPO, revenue, units and the candidate's own arithmetic. **No for the key input**: the candidate derives Wind equipment orders, but GEV discloses them, and the disclosed figures differ |
| Street value (confirmed) | 2,278 (Q1 2027 1,019.0 + Q2 2027 1,258.7) |
| Candidate's value | 1,471 to 2,018; 1,758 at k = 1.0; gap -23% |
| Corrected value (disclosed orders) | 1,675 to 2,294 over every observed k; centre 1,985. Same-season (first-half) observations only: 1,783 to 2,001 |
| Corrected gap | about -13% at the centre (-19% at k = 1.0; -11% at the mean of the three reported k) |
| Error band on our value | about +/-16% (310 on 1,985). **The band is wider than the gap; the Street sits inside it** |
| Use that remains | Supporting note only: the 87.8% break-even that shows Wind cannot absorb the company-level schedule gap (section 7) |

## 1. Sources opened

| Tag | Source | Locator |
|---|---|---|
| BBG | Bloomberg, 2026-10-01. `GEV_Pull_2026-10-01/01-eeo-company-specific.xlsx` sheet "Multiple Periods", rows 19, 26, 27, 28, columns E to I; `segment_quarterly.json`; `06_modl.xlsx` | re-read with openpyxl and json |
| 10-Q 2Q26 | accession 0001996810-26-000148, MD&A Wind, page 31 | corpus document 218 |
| 10-Q 1Q26, 10-K 2025, 10-Q 3Q25, 2Q25, 1Q25, 10-K 2024, 10-Q 3Q24, 2Q24 | accessions -26-000064, -26-000015, -25-000160, -25-000133, -25-000073, -25-000011, -24-000083, -24-000067 | Wind MD&A unit and RPO tables |
| PR | Earnings releases, 8-K exhibits: accessions 0001996810-26-000147, -26-000063, -26-000012, -25-000159, -25-000132, -25-000072, -25-000004, -24-000080, -24-000065, -24-000004 | Wind segment tables (total orders) |
| DECK 2Q26 | `gev_webcast_presentation_07222026.pdf`, slide 17 "Wind: key performance metrics" | corpus source 3157 |
| DECK 4Q25 | `gev_webcast_presentation_01282026.pdf`, slide 19 | fetched from gevernova.com, parsed with pypdf |
| DECK 2Q25 | `gev_webcast_presentation_07232025.pdf`, slide 17 | fetched from gevernova.com, parsed with pypdf |
| CALL 2Q26 | `gev_webcast_transcript_07222026.pdf` | corpus source 3161 |
| CONF | Conference transcript 2026-09-16 | project scratch copy; summary in corpus sources 681, 3750 |
| IU25 | Investor update deck 2025-12-09, slide 19 (offshore year-end equipment backlog: 2023 ~$4B, 2024 ~$3B, 2025E ~$2B) | corpus source 1844 |
| XBRL | `data/financials/gev_segments.csv`, `RevenueFromContractWithCustomerExcludingAssessedTax`, `OperatingSegments;Product;WindSegment` | external revenue only |

Script: scratchpad `windchk/final.py`.

## 2. Street figures: all confirmed

| Line (BBG) | Q3 26 | Q4 26 | Q1 27 | Q2 27 | H2 26 | H1 27 |
|---|---|---|---|---|---|---|
| Wind equipment revenue | 1,789.2 | 1,763.1 | 1,019.0 | 1,258.7 | 3,552.3 | **2,277.8** |
| Wind offshore revenue | 215.3 | 118.9 | 178.0 | 211.6 | 334.3 | 389.5 |
| Wind onshore revenue | 2,088.1 | 2,221.4 | 1,250.2 | 1,623.0 | 4,309.5 | 2,873.2 |
| Wind services revenue | 544.6 | 545.3 | 483.1 | 573.2 | 1,089.9 | 1,056.3 |
| Wind total revenue | 2,341.0 | 2,343.7 | 1,522.3 | 1,865.7 | 4,684.7 | 3,388.0 |
| Wind MW delivered | 1,648 | 1,633 | 694 | 1,188 | 3,281 | 1,882 |
| Wind adjusted EBITDA | 24.6 | 183.2 | (9.2) | (11.8) | 207.8 | (20.9) |
| Company EBITDA | 1,672 | 2,500 | 1,810 | 2,228 | 4,171 | 4,038 |

- FY27 Wind adjusted EBITDA = 187.7. Confirmed.
- H1 2026 actual Wind equipment revenue = 889 + 1,395 = 2,284 (segment basis, 10-Q) or 889 + 1,394 = 2,283 (XBRL, external). Street H1 2027 is -0.3% on that. Confirmed.
- Definition: the Bloomberg line carries the 2Q26 actual as 1,395, so it is on GEV's segment basis. Same definition as the 10-Q.
- **Quality of the line (new):** the sub-lines come from different broker sets and do not add. Q1 2027: equipment + services = 1,502 against total 1,522; onshore + offshore = 1,428 against 1,522. Taking the Street's offshore figure away from the Street's equipment figure mixes two sets of brokers.
- **Spread (new):** `06_modl.xlsx` gives the same line for Q3 2026: mean 1,789, low 1,274, high 2,244, median 1,813. That is -29% to +25% around the mean one quarter out. No per-broker values and no contributor count are exposed for this line. The spread for Q1 and Q2 2027 is not in the export.

## 3. Company figures: confirmed, with three small corrections

Units and backlog, 10-Q 2Q26 page 31 (accession 0001996810-26-000148), quoted from the table: "Wind Turbines 147 / 381 / 293 / 404; Repower Units — / 205 / 49 / 205; Wind Turbine and Repower Units Gigawatts 0.6 / 1.6 / 1.2 / 1.8" (three months 2026, 2025; six months 2026, 2025). RPO: "Equipment $8,197 / $9,112 / $9,731" (6/30/26, 12/31/25, 6/30/25). Revenues: "Equipment $1,395 / $1,797 / $2,284 / $3,209"; "Offshore Wind 305 / 225 / 551 / 430".

| Item | Candidate | Recomputed | Note |
|---|---|---|---|
| H1 26 orders, units | 342 vs 609 | 342 vs 609 (-43.8%) | confirmed; turbines alone 293 vs 404 (-27.5%) |
| H1 26 orders, GW | 1.2 vs 1.8 | 1.2 vs 1.8 (-33%) | confirmed; both figures rounded to 0.1 |
| Wind equipment RPO 6/30/26, 12/31/25 | 8,197; 9,112 | same | confirmed |
| H1 25 equipment revenue | 3,192 | 3,209 segment; 3,192 external | candidate used the external (XBRL) figure; difference is intersegment sales |
| H1 25 offshore revenue | 429 | 430 | 10-Q six-month figure |
| H2 24 orders, GW | 2.7 | 2.8 (FY 5.3 less H1 2.5) | GW ratio for H2 25 is 1.39, not 1.44 |
| Implied equipment orders (RPO change + revenue) | 2,325; 2,704; 2,203; 3,413; 1,368 | same on XBRL revenue; 2,338; 2,720; 2,220; 3,423; 1,369 on segment revenue | arithmetic confirmed |
| Four-quarter turnover on equipment RPO | 58.5-69.3% | 58.5-69.3% external; 58.7-69.5% segment; Street 71.1% | confirmed |

Quotes confirmed:
- CALL 2Q26: "We expect improvement in Wind revenue and EBITDA in the second half of the year, given 70% of 2025 equipment orders were in the second half and will be delivered in the second half of 2026."
- PR 2Q26 (accession 0001996810-26-000147): revenues decreased "primarily driven by equipment at Onshore Wind as a result of soft orders in the first half of 2025."
- CONF 2026-09-16: "the second half orders, yes, will be materially larger than the first half orders in Onshore Wind"; "I wouldn't expect a different orders dynamic in the third quarter".

## 4. The key input is wrong: Wind equipment orders in dollars ARE disclosed

The candidate says GEV does not publish Wind equipment orders in dollars and derives them from the RPO change. That holds for the 10-Q only. Every earnings deck carries a slide "Wind: key performance metrics" with "Orders ($M): Equipment / Services / Total Orders".

| Half | Disclosed equipment orders | Source | Candidate's implied figure | Disclosed less implied |
|---|---|---|---|---|
| H1 2024 | 2,518 | DECK 2Q25 slide 17 | 2,325 | +193 |
| H2 2024 | 2,929 (FY 5,447 less H1) | DECK 4Q25 slide 19 | 2,704 | +225 |
| H1 2025 | 1,816 | DECK 2Q25, DECK 2Q26 | 2,203 | -387 |
| H2 2025 | 3,656 (FY 5,472 less H1) | DECK 4Q25 slide 19 | 3,413 | +243 |
| H1 2026 | 1,460 | DECK 2Q26 slide 17 | 1,368 | +92 |

- Cross-check: disclosed equipment + services orders equal the total Wind orders in each release (for example H1 2026: 1,460 + 988 = 2,448; PR 2Q26 "Orders ... $2,448").
- The implied figure also carries currency moves and contract changes in the backlog. It overstates H1 2025 by 387.
- Management's "70% of 2025 equipment orders were in the second half": disclosed figures give 66.8%; implied figures give 60.8%. The disclosed series is the one management is describing.
- **Year-on-year fall in H1 2026 equipment orders: -19.6% in dollars** (DECK 2Q26 shows "(19) %" organic). The candidate's implied series gives -37.9%. The title's "33-44%" is GW and units, not dollars. Total Wind orders in dollars fell 9% (PR 2Q26).
- Order value per MW rose: 1.01 (H1 24), 1.05, 1.01 (H1 25), 1.18, 1.22 (H1 26) $M per MW. So GW understates the dollar orders that feed H1 2027 revenue.

## 5. The k test redone on disclosed orders

k = (Wind equipment revenue less offshore revenue) / equipment orders two halves earlier. Segment-basis revenue.

| Revenue half | Orders half | k, disclosed orders | k, candidate | GW sold / GW ordered |
|---|---|---|---|---|
| H1 25 (3,209 - 430) | H1 24 (2,518) | 1.104 | 1.19 | 1.20 |
| H2 25 (4,042 - 222) | H2 24 (2,929) | 1.304 | 1.41 | 1.39 |
| H1 26 (2,284 - 551) | H1 25 (1,816) | 0.954 | 0.79 | 1.11 |
| H2 26 Street (3,552 - 334) | H2 25 (3,656) | 0.880 | 0.94 | 1.06 |
| **H1 27 Street (2,278 - 390)** | **H1 26 (1,460)** | **1.293 needed** | 1.38 | 1.57 (1.51-1.64 for rounding of 1.2 GW) |

H1 2027 Wind equipment revenue = 1,460 x k + 390:

| k used | Value | vs Street 2,278 |
|---|---|---|
| 0.880 (Street's own H2 26) | 1,675 | -26.5% |
| 0.954 (lowest reported) | 1,783 | -21.7% |
| 1.000 | 1,850 | -18.8% |
| 1.104 (other first-half observation) | 2,001 | -12.2% |
| 1.121 (mean of the three reported) | 2,026 | -11.1% |
| 1.304 (highest reported) | 2,294 | +0.7% |

- Three reported observations. The Street needs 1.293 and one of the three is 1.304. The band reaches the Street.
- Full band 1,675-2,294: centre 1,985 (-12.9%), half-width 310 (+/-15.6%). **Gap smaller than the band.**
- The GW version still shows the Street above every observation (1.57 against 1.06-1.39). Weaknesses: the MW line has an unknown and probably small number of brokers; GW figures are rounded to 0.1; and dollars per MW ordered rose 21% between the H1 25 and H1 26 order books.

## 6. Two further tests the candidate does not pass

### 6a. The same arithmetic applied to H2 2026 contradicts the company's own guide
- Street H2 2026 Wind revenue (4,685) matches the guide (organic revenue down low double digits; Q3 down low double digits). The Street's H2 2026 onshore equipment is 3,218, which is k = 0.880 on H2 2025 orders of 3,656.
- If k were about 1.0 in both halves, H2 2026 would be 3,990 (+12% against the Street and above the guide) and H1 2027 1,850 (-19%). Four-quarter total: 5,840 against Street 5,830. No gap over four quarters.
- Four-quarter ratio (onshore equipment revenue / equipment orders a year earlier): FY25 on FY24 1.211; H2 25 + H1 26 on H2 24 + H1 25 1.170; Street H2 26 + H1 27 on H2 25 + H1 26 **0.998**. On this measure the Street is below history, not above.
- On the guide, 438 of H2 2025 orders (3,656 less 3,218) are not delivered in H2 2026 and stay in backlog. If they deliver in H1 2027: 1,460 x 0.954 to 1.104 + 390 + 438 = 2,221 to 2,439, which is -2.5% to +7.1% against the Street.
- So the candidate is a statement about the split between two halves, and its own method disagrees with the guided half.

### 6b. Backlog cross-check with offshore removed
Offshore equipment backlog from IU25 slide 19 (year-end ~$4B, ~$3B, ~$2B) less first-half offshore revenue. Approximate, rounded to the nearest $1B at source.

| Date | Wind equipment RPO | Offshore backlog (approx.) | Onshore equipment RPO (approx.) | Next H2 onshore equipment, share | Following H1 onshore equipment, share | Four quarters |
|---|---|---|---|---|---|---|
| 6/30/24 | 13,147 | 3,206 | 9,941 | 4,564 = 45.9% | 2,779 = 28.0% | 73.9% |
| 6/30/25 | 9,731 | 2,570 | 7,161 | 3,820 = 53.3% | 1,733 = 24.2% | 77.5% |
| 6/30/26 (Street) | 8,197 | 1,449 | 6,748 | 3,218 = 47.7% | 1,888 = 28.0% | 75.7% |

- H1 2027 at 24.2% to 28.0% of the June onshore backlog, plus the Street's offshore 390: 2,023 to 2,276, which is -11.2% to -0.1% against the Street.
- The candidate's step 6 (71.1% against a 58.5-69.5% range) uses the blended ratio. Offshore converts slowly and its share of the equipment backlog fell from about 24-26% to about 18%, which lifts the blended ratio without any change in onshore conversion. With offshore removed the Street is inside the range in every column.
- The candidate's step 6 arithmetic itself reproduces: 8,197 x 64-67% = 5,246-5,492; less Street H2 26 3,552 = 1,694-1,940.

## 7. What still stands

- Step 8 conclusion (Wind cannot hold the company-level equipment-schedule gap) stands, but on a different footing. For the Street's Power + Electrification equipment (10,874 + 13,541 = 24,415) to equal the schedule (31,616), Wind would have to convert (31,616 - 24,415) / 8,197 = **87.8%** of its equipment backlog in a year. Reported blended range 58.7-69.5%; onshore-only about 74-78%. The claim "Street Wind is already above anything Wind has converted" does not stand once offshore is removed.
- Street H1 2027 MW delivered against GW ordered a year earlier (1.57) is above every observation. This is a volume observation on a thin line, not a revenue gap.

## 8. Profit size, recomputed

| Case | Revenue below Street | At 10% contribution | At 20% contribution | Share of Street H1 27 EBITDA 4,038 |
|---|---|---|---|---|
| Same-season band (k 0.954-1.104) | 277 to 495 | 28 to 49 | 55 to 99 | 0.7% to 2.5% |
| Candidate's band | 260 to 807 | 26 to 81 | 52 to 161 | 0.6% to 4.0% |

The 10-20% contribution rate is assumed; GEV does not disclose onshore equipment margin.

## 9. Reveal dates

- Q1 2027 and Q2 2027 prints (late April and late July 2027): Street Wind equipment 1,019 and 1,259. Confirmed as the settling numbers.
- Q3 2026 print: the candidate gives 2026-10-28. The corpus calendar holds only an unconfirmed estimate of 2026-10-21 from filing cadence. Date not verified here.
- Earlier read: Wind equipment orders in dollars for Q3 2026 will be on the deck slide "Wind: key performance metrics" (no need to derive them).

## 10. List of flaws

1. Derived orders used where disclosed orders exist; the two differ by -387 to +243 a half. Corrected: needed k 1.29 (not 1.38), low k 0.95 (not 0.79), order fall -20% in dollars (not -38%).
2. Three observations of k; the highest (1.304) reaches the Street (1.293). Gap about -13% at the centre, band about +/-16%.
3. The method contradicts the guided half (H2 2026 at k = 0.88) and shows no gap over four quarters (0.998 against 1.17-1.21).
4. Backlog cross-check fails once offshore is removed (Street 28.0% against 24.2-28.0%).
5. "Why missed" is partly false: the dollar figure is on a slide in every earnings deck.
6. Street line is thin: contributor count not visible, one-quarter-out spread -29% / +25%, sub-lines from different broker sets.
7. Profit effect 0.7-2.5% of half-year EBITDA on an assumed margin.
