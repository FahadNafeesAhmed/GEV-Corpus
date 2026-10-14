# Verify (reproduce): power-equipment-fy28-fy29

_Research input only: facts, arithmetic, sources. No memo sentences. No forecast chosen for the team. Bloomberg figures cited as "Bloomberg, 2026-10-01"; keep inside the project folder._

Check type: REPRODUCE. Every number in the candidate was recomputed from the primary files.

## 0. Verdict

| Item | Result |
|---|---|
| Arithmetic reproduces from primary files | Yes (small input slips, section 2) |
| Survives the test "gap at least about 5% and larger than its own error band" | **No** |
| Street FY2028 / FY2029 Power equipment revenue | $15,888M / $19,256M (reproduced) |
| Candidate's stated gap | +17% (FY2028 July plan x 0.90; FY2029 centre with no haircut) |
| Corrected centre | FY2028 about $17.2B (+8%); FY2029 about $20.4-21.0B (+6% to +9%) |
| Corrected range vs Street | FY2028 -11% to +26% across output paths at 0.90-0.93 conversion; -21% to +35% with the full conversion range. FY2029 -4% to +18% |
| Error band on our value | about +/-20% (one-year slice back-test 0.75 to 1.27; output path 20 to 25.5 GW; aeroderivative timing) |

Reasons it fails, in order of weight:
1. The whole FY2028 gap sits in H2 2028 and in one order layer (Q2 2026, $12.7B for 12.1 GW). H1 2028 shows no gap (section 4).
2. That layer's $1,049/kW is lifted by 61 aeroderivative units that ship early, not last. Moving them out of the 2028 slice cuts the July-plan gap from +17/+20% to +4/+13% (section 5).
3. The FY2029 leg multiplies GW by order price with no conversion haircut, while the FY2028 leg applies 0.90-0.93. With the same haircut the FY2029 centre falls from +17% to +6/+9% and the low end goes negative (section 6).
4. The gap exists only if 2028 output is 23 GW or more. At flat 20 GW the Street is right or high (-11% to +2%).
5. A one-year slice of the backlog has back-tested between 0.75 and 1.27 of the layer dollars (section 7). The band is wider than the corrected gap.
6. Management's own 2028 framework (December 2025, set with 2028 slots already sold) implies Power equipment of $13.2-15.6B, at or below the Street (section 8).
7. Neither year is reported inside 12 months.

## 1. Street values (Bloomberg, 2026-10-01)

File `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, key `Total Revenue|Power|Equipment|YYYY Qn`. Same values in `01-eeo-company-specific.xlsx` row "Power > Equipment" and in `street_segments_annual_2026-10-01.csv`.

| $M | H2 2026 | FY2027 | FY2028 | FY2029 | FY2030 |
|---|---|---|---|---|---|
| Power equipment | 5,491 | 12,151 | 15,888 | 19,256 | 23,469 |
| Power services | 7,661 | 15,675 | 17,665 | 19,711 | 22,357 |
| Power total | 13,160 | 28,121 | 33,521 | 39,522 | 45,215 |
| Equipment + services less total | | -295 | +33 | -555 | +611 |

- FY2028 quarters: 3,445 + 3,654 + 4,000 + 4,790 = 15,888. H1 2028 = 7,099; H2 2028 = 8,790.
- Definition check: Bloomberg Q2 2026 actual on this line is 1,965 = the 10-Q MD&A Power "Equipment" segment revenue (0001996810-26-000148). Same definition as the company figure.
- Quality of the line: the export gives no broker count for division lines. For Q3 2026 (file `06_modl.xlsx`) the low / high on this line are 2,063 / 2,591 against a mean of 2,394 (-14% / +8%), one quarter out. Equipment + services differ from the Power total by up to 1.4% in 2029-30, so contributor sets differ. Bloomberg's "Organic Growth Rate | Power" is a flat 18.0 for every 2027-28 quarter and 9.0 for 2029-30 (one contributor). Street Power RPO jumps $19B between Q4 2028 and Q1 2029 (contributor change).
- ConsensusHistory sheet: FY2028 revenue 59,196 (2026-07-10) to 60,842 (2026-09-25) = +2.8%; 60,713 (09-04) to 60,842 (09-25) = +0.2%. Reproduced.

## 2. Company inputs (quoted from filings in gev.db)

10-Q / 10-K MD&A "POWER" tables. Accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148.

| Quarter | GW ordered | GW sold | Equipment revenue $M | Equipment RPO end $M | Orders $M = change in RPO + revenue | $/kW |
|---|---|---|---|---|---|---|
| Q1 2025 | 7.1 | 3.0 | 1,491 | 13,920 | 2,950 | 415 |
| Q2 2025 | 5.1 | 5.2 | 1,504 | 16,133 | 3,717 | 729 |
| Q3 2025 | 7.4 | 4.0 | 1,744 | 18,977 | 4,588 | 620 |
| Q4 2025 | 10.2 | 3.1 | 1,946 | 24,707 | 7,676 | 753 |
| Q1 2026 | 8.1 | 4.2 | 1,885 | 28,530 | 5,708 | 705 |
| Q2 2026 | 12.1 | 3.3 | 1,965 | 39,261 | 12,696 | 1,049 |

Corrections to the candidate's inputs (small):
- Q1 2026 GW ordered is 8.1 in the Q1 10-Q (candidate uses 8.0 = 20.1 - 12.1). Price is $705/kW, not $714.
- Q2 2024 GW sold is 1.5 in the Q2 2024 10-Q (physical lens uses 1.4).
- H1 2026: 18,404 / 20.1 = $916/kW; +21.7% vs Q4 2025 $753. Matches "more than 20% above 4Q'25" (Q2 2026 call, corpus source 3161).
- Deck cross-check found in corpus source 3157 (Q2 2026 deck, page 15): Power equipment orders Q2 2026 12,650; H1 2026 18,261; Q2 2025 3,519; H1 2025 6,361. Derived values are 0.4% to 5% above the deck values. FY24 8,340, FY25 18,241 and Q4 2025 7,432 are from the January 2026 deck, which is not in the corpus text; not verified here.
- 6/30/26: $39,261M / 53 GW = $741/kW. Reproduced.
- RPO schedule, 10-Q Q2 2026 note: "Equipment-related RPO of $87,821 million of which 36%, 65%, and 97% is expected to be recognized within 1, 2, and 5 years". Reproduced.
- Output path. Q2 2026 call: "three gigawatts of output a quarter to five gigawatts of output a quarter, starting in the third quarter"; "that next step-up in output in '28 to 24 gigawatts annualized"; "ship over the next six quarters at least 30 gigawatts". Laguna conference transcript 2026-09-16 (gevernova.com PDF, fetched 2026-10-01): "five gigawatts ... sometime in the second half of next year to the next ladder step, to six gigawatts a quarter ... into 2028, we may be at six gigawatts for a period of time, and then ... seven gigawatts a quarter." Both reproduced. Note "24 gigawatts annualized" in 2028 is a run rate, not a stated calendar-year delivery total.
- Mix statement, Q2 2026 call: "In 2Q, we booked a higher dollar per kW price in orders, given a higher mix of aeroderivatives versus heavy-duty gas turbines and incremental combined cycle equipment as SRAs converted to orders."
- Timing statements. Laguna: the 2026 change in backlog margin "tells you in '29 and '30 - because that's most of when that equipment delivers". Q2 2026 call: "the complement of aero that comes first and heavy-duty that will be shipped in '30, '31".
- Revenue recognition, 10-K 2025: "customized goods, including power generation equipment such as gas and certain wind turbines" are recognised over time on cost incurred. Revenue therefore leads shipment by an unknown amount; "GW sold x price" is an approximation.

## 3. Candidate arithmetic, recomputed

Layers at 6/30/26 (oldest layer set so the sum equals $39,261M): 3.1 GW $1,926M; 7.1 / 2,950; 5.1 / 3,717; 7.4 / 4,588; 10.2 / 7,676; 8.0 / 5,708; 12.1 / 12,696.

| FY2028 path | Layer $M | x0.80 | x0.90 | x0.93 | x0.99 |
|---|---|---|---|---|---|
| Flat 20 GW | 17,439 | 13,951 (-12%) | 15,695 (-1%) | 16,218 (+2%) | 17,264 (+9%) |
| July plan 23 GW | 20,586 | 16,469 (+4%) | 18,528 (+17%) | 19,145 (+20%) | 20,381 (+28%) |
| Mid 24 GW | 21,560 | 17,248 (+9%) | 19,404 (+22%) | 20,051 (+26%) | 21,345 (+34%) |
| Ladder 25.5 GW | 23,058 | 18,446 (+16%) | 20,752 (+31%) | 21,444 (+35%) | 22,827 (+44%) |

- All cells match the candidate. Using 8.1 GW for Q1 2026 moves each cell by under 0.5%.
- Residual: 39,261 - 5,491 - 12,151 = 21,619. Reproduced. It assumes all Street H2 2026 and 2027 revenue comes out of the 6/30/26 backlog and that the rest lands in 2028; neither is disclosed.
- Street $/kW: 2028 = 794 / 691 / 662 / 623 / 611 at 20 / 23 / 24 / 25.5 / 26 GW; 2029 = 741 / 688 at 26 / 28 GW; 2030 = 782 at 30 GW. Reproduced.
- FY2029 table (26 x 790 = 20,540; 27 x 838 = 22,626; 28 x 875 = 24,500; 26 x 729 = 18,954) reproduced. H2 2026 guide: 729 x 1.15 to 1.20 = 838-875. Reproduced.
- Three-year check: 58,614 - 18,261 = 40,353; / 55 = 734; / 63 = 641. Reproduced.
- Profit: +$2.6-3.3B (July) or +$4.9-5.6B (ladder) at 15% to 23.3% = +$0.4B to +$1.3B = +3% to +10% of $12,553M. Reproduced.
- Identity: 16.7 + 20.2 + 29.8 = 66.7 = 11.9 + 15.3 + 17.5 + 22.0. Reproduced. Rolling the backlog back from 53 GW with the filed quarterly GW gives 40.3 / 33.2 / 29.8 GW at Q4 / Q3 / Q2 2025 against disclosed 40 / 33 / 29, so backlog GW carries about +/-1 GW of rounding.

## 4. Where the FY2028 gap sits

July plan (5.5, 5.5, 6, 6 GW by quarter), FIFO layers x 0.90:

| Half | Backlog positions | Layer $M | x0.90 | Street | Gap |
|---|---|---|---|---|---|
| H1 2028 | 30-41 GW | 7,995 | 7,196 | 7,099 | +1% |
| H2 2028 | 41-53 GW (all Q2 2026 orders) | 12,591 | 11,332 | 8,790 | +29% |

The FY2028 gap is the assumption that the 12.1 GW ordered in Q2 2026 at $1,049/kW all ship in H2 2028.

## 5. Aeroderivative timing in the Q2 2026 layer

- Q2 2026 orders: 52 heavy-duty units (15 HA) and 61 aeroderivatives (10-Q). Laguna: aeroderivatives are "30-, 35-megawatt applications". 61 x 30-35 MW = 1.8-2.1 GW. News summary of the call (corpus source 354): 20 GW signed = 18 GW reservations + 2 GW firm orders; 10 GW of reservations converted. 2 + 10 = 12 GW of orders, so the direct firm orders are about the size of the aeroderivative units.
- Price: one broker estimate (BNP Paribas via Utility Dive, corpus source 301): about $1,800/kW aeroderivative, $790/kW heavy-duty, $950/kW HA combined-cycle scope. Unverified third-party figure.
- Shipping pace: 16 aeroderivative units sold in Q2 2026, 26 in H1 2026, 27 in all of 2025. 70 units ordered in H1 2026 clear in about four to five quarters at the Q2 pace. CEO: aero "comes first".
- Effect of taking 2.1 GW of aeroderivatives ($1,400-1,800/kW, so $2.9-3.8B) out of the 2028 slice and moving heavy-duty units up the queue:

| FY2028 path | Layer $M | x0.90-0.93 | vs Street | x0.80 | x1.00 |
|---|---|---|---|---|---|
| Flat 20 GW | 15,712-16,300 | 14,141-15,159 | -11% to -5% | -21% | +3% |
| July plan 23 GW | 18,387-19,227 | 16,548-17,881 | +4% to +13% | -7% | +21% |
| Mid 24 GW | 19,294-20,134 | 17,365-18,725 | +9% to +18% | -3% | +27% |
| Ladder 25.5 GW | 20,682-21,522 | 18,614-20,015 | +17% to +26% | +4% | +35% |

Corrected centre (July plan, mid of the 0.90-0.93 cell): about $17.2B, +8%. The same dollars move into H2 2026-2027, where the Street already sits above the layer arithmetic (H2 2026: Street 5,491 vs layers 4,793).

## 6. FY2029 leg with a consistent haircut

The FY2028 leg applies conversion 0.90-0.93. The FY2029 leg applies none. Same table with the haircut (Street $19,256M):

| GW x $/kW | No haircut | x0.90 | x0.93 |
|---|---|---|---|
| 26 x 790 | 20,540 (+7%) | 18,486 (-4%) | 19,102 (-1%) |
| 27 x 838 | 22,626 (+18%) | 20,363 (+6%) | 21,042 (+9%) |
| 28 x 875 | 24,500 (+27%) | 22,050 (+15%) | 22,785 (+18%) |
| 26 x 729 | 18,954 (-2%) | 17,059 (-11%) | 17,627 (-8%) |

Three-year check with the haircut: Street 2028-30 of 58,614 needs order dollars of 63,026-65,127; less H1 2026 orders 18,261 leaves 44,765-46,866 = $711-852/kW on 55-63 GW of reservations. Guided H2 2026 conversions are $838-875/kW. With the haircut the Street's 2028-30 total is 0% to about 15% below the guided price, not 15-25%.

Also: $838-875/kW is an all-in measure (aeroderivatives, combined-cycle scope and non-gas equipment in the numerator). The price of the 63 GW reservation book is not disclosed.

## 7. Back-tests (error band)

Cycle conversion (revenue until the opening backlog GW has shipped / opening equipment RPO, ex the $3.9B EDF item), recomputed with filed GW and a backlog rolled back from 53 GW: YE22 1.02; Q2 2023 0.92; YE23 0.82; Q2 2024 0.86; YE24 0.96; Q2 2025 0.97. Mean 0.93, range 0.82-1.02. Candidate shows 0.99, 0.88, 0.80, 0.82, 0.93, 0.95 (mean 0.90); the difference is the +/-1 GW backlog rounding. Last two windows include Street quarters.

One-year slices (FIFO layer dollars for the GW shipped in the window vs actual equipment revenue):

| Vantage | Window | Positions GW | Predicted $M | Actual $M | Actual / predicted |
|---|---|---|---|---|---|
| YE23 | 2024 | 0-11.9 | 6,539 | 5,708 | 0.87 |
| Q2 2024 | Q3 2024-Q2 2025 | 0-16.3 | 8,289 | 6,217 | 0.75 |
| YE24 | 2025 | 0-15.3 | 8,009 | 6,685 | 0.83 |
| YE24 | H1 2026 (back of backlog) | 15.3-22.8 | 3,043 | 3,850 | 1.27 |
| Q2 2025 | Q3 2025-Q2 2026 | 0-14.6 | 8,057 | 7,540 | 0.94 |
| YE25 | H1 2026 | 0-7.5 | 4,367 | 3,850 | 0.88 |

- FY2028 is a one-year slice. One-year slices have run 0.75 to 1.27. The only back-of-backlog slice is above 1 (n = 1), which would favour the candidate, but it is one observation.
- The physical lens itself states "no call on a four-quarter window from this lens" (its section 4b), then makes a four-quarter call for FY2028.

## 8. Company framework cross-check

December 2025 investor update (corpus source 1844): "Revenue up high teens at Power & Electrification"; "Pricing reflecting recent orders"; "Gas turbine deliveries reach 20 GW annualized output in mid '26, increasing to ~24 GW in '28"; "Now sold out on new equipment through '28 ... less than 10 GW left to sell for '29". So the framework was set with 2028 slots sold and priced.

| Power CAGR 2025-28 (base $19,767M) | Power 2028 $M | Less Street services 17,665 | Per kW at 24 GW |
|---|---|---|---|
| 16% | 30,854 | 13,189 | 550 |
| 17% | 31,659 | 13,994 | 583 |
| 18% | 32,478 | 14,812 | 617 |
| 19% | 33,311 | 15,645 | 652 |

- Street Power 2028 $33,521M = 19.2% CAGR, at the top of the framework.
- Candidate equipment of $18.5-19.7B plus Street services = Power $36.2-37.4B = 22.3-23.6% CAGR, 8-12% above the Street Power total and above "high teens". The candidate therefore needs the company's own framework to be low by about $3-5B in one division. The framework predates the September ladder (+1.5 to +2 GW in 2028) and management calls its markers conservative; neither is arithmetic on disclosed data.

## 9. RPO schedule check (does not settle it)

Company: $31,616M in year one, $25,468M in year two, $28,102M in years three to five, $2,635M after (each +/-$440M for rounding). July-plan FIFO puts Power at $11.5B / $15.2B (before haircut) in years one / two and $12.6B in H2 2028. That leaves Electrification + Wind $20.1B / $10.3B from backlog against Street equipment revenue of $19.4B / $21.3B for those divisions. Year two would be only 48% covered by a $48.8B backlog. Possible, not proven either way. The Q3 2026 10-Q (2026-10-28) updates the percentages.

## 10. Corrected values

| Field | Candidate | Corrected |
|---|---|---|
| Street FY2028 / FY2029 | 15,888 / 19,256 | same |
| FY2028 our value, July plan | 18.5-19.1B (+17% to +20%) | 16.5-17.9B (+4% to +13%), centre about 17.2B (+8%), after aeroderivative timing |
| FY2028 full range | 15.7-21.4B | 14.1-20.0B (-11% to +26%) at 0.90-0.93; 12.6-21.5B (-21% to +35%) at 0.80-1.00 |
| FY2029 our value | 20.5-24.5B, centre 22.6B (+17%) | 18.5-22.8B, centre 20.4-21.0B (+6% to +9%), with the same haircut |
| Three-year implied reservation price | $641-734/kW | $711-852/kW with the haircut (guide $838-875) |
| Q1 2026 order price | $714/kW | $705/kW (8.1 GW in the 10-Q) |
| Conversion ratios | 0.80-0.99, mean 0.90 | 0.82-1.02, mean 0.93 (cycle); 0.75-1.27 (one-year slices) |
| Error band on our value | not stated as one figure | about +/-20% |
| Gap vs band | +17% | about +8% vs +/-20%: gap smaller than band |

## 11. What would change the verdict (company-reported)

- 2026-10-28: aeroderivative units sold in Q3 and remaining aeroderivative order count; gas GW sold (5 GW run rate); Power equipment RPO / backlog GW; the new within-1 / within-2-year RPO percentages.
- Late January 2027: stated 2027 gas output; FY27 Power growth guide; H2 2026 order $/kW by unit class if given.
- Spring 2027 capital markets day: 2028 calendar-year GW and the 2030 equipment / services split.
- A disclosed delivery-year split of backlog, or a heavy-duty-only order price, would remove the two largest sources of error (sections 4-6).

## 12. Scripts

Scratchpad: `repro.py` (Street sums, derived orders, layers, FY2028 and FY2029 tables), `repro2.py` (cycle conversion and one-year slice tests), `repro3.py` and `repro4.py` (aeroderivative timing, framework, three-year check). Inputs: `segment_quarterly.json`, `06_modl.xlsx`, `GEV_bloomberg_pull_filled_2026-10-01.xlsx` (Consensus, ConsensusHistory), gev.db documents for the ten accessions above, corpus sources 3161, 3157, 1844, 301, 354, 681, and the Laguna transcript PDF on gevernova.com.
