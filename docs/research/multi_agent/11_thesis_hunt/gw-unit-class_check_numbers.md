# Check (recompute and back-test): gw-unit-class

_Research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast chosen for the team (ranges and methods only). Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Check type: RECOMPUTE AND BACK-TEST. The model in `gw-unit-class.md` was rebuilt from scratch in Python from the primary files (10-Q / 10-K Power tables in `gev.db`, `segment_quarterly.json`, `06_modl.xlsx`, `01_eeo_annual.xlsx`, corpus sources 3161, 3796, 1844, 2648, 671, 3689, and the 16 September 2026 conference transcript). Money in $M unless stated.

Terms (same as the rebuild):
- **HA**: the largest gas turbine class (about 430 MW). **Other heavy-duty**: F, E and B class. **Aero**: aeroderivative units (about 40 MW).
- **Vintage**: the quarter a unit was ordered. **Oldest first**: units ship in the order they were booked.
- **Price index**: one heavy-duty-equivalent $/kW per order quarter, solved from that quarter's order dollars.
- **Bias**: reported revenue divided by model revenue over the back-test.
- **Flat-price null**: the same model with the same reported units, but every unit of a class carries one constant value. It holds no vintage information. It is the comparison that shows what the vintage prices add.
- **Street**: Bloomberg BEst mean, key `Total Revenue|Power|Equipment`.

## 0. Verdict

| Item | Rebuild | This check |
|---|---|---|
| Arithmetic reproduces from primary files | | **Yes.** Every table cell tested matches (section 1). Four small slips (section 2) |
| Gap, H1 2027 Power equipment revenue | +28% (median of 9,720 sets) | Reproduced: +30% raw, +27% to +28% with the H1 factor. **Corrected centre about +14%**, range +6% to +28% (section 7) |
| Error band, H1 2027 | about +/-20% | **about +/-23%** on a worst-miss basis, +/-19% on a root-mean-square basis (section 8) |
| Gap at least 7% | Yes | Yes (+14%) |
| Gap clearly larger than the band | 28 against 20 | **No.** 14 against 23. On the rebuild's own figures the ratio is 1.4 |
| Back-test supports the part of the model that makes the gap | Stated limit 1 | **No.** The flat-price null back-tests as well or better (section 4) |
| Kill reasons answered (of 6) | | 1 fully (reveal date); 3 in part (one layer, error band, profit); 2 not (rival explanation, thin Street data) |
| **survives** | holds = true | **false** |

Reasons, in order of weight:
1. The vintage prices have no measured skill. In the back-test they moved model revenue by -5% to +7% a half-year. Forward they move it by +29% (H2 2026) and +55% (H1 2027). The flat-price null has a lower error on every window type.
2. The H1 2027 gap is a step between two halves that share the same output (10 GW). The step exists only if units ship in strict quarterly order inside 2025 and the Q1 2025 layer is cheap while the Q2 and Q3 2025 layers are dear. With 2025 treated as one vintage the step falls from +23% to +6%.
3. 67% of the gas value the model ships in H1 2027 comes from two order layers (Q2 and Q3 2025). Management said in October 2025 that the dollars per GW of those two quarters were moved by aero mix, combined-cycle scope and non-gas orders. This is kill reason 2, one year earlier.
4. With the bias fitted only on data known at the time, the model's worst next-half miss is 20% (median of sets; 25% for the base set). The last H2-to-H1 step it called was +27%; the reported step was +4%.
5. The stress table in the rebuild is run on the most favourable output path. On the 5 GW a quarter path, one adverse input alone removes the gap.
6. The Street line is still thin and the company's own framework sits on the Street.

## 1. What was recomputed, and whether it matches

| Item | Rebuild | Recomputed | Match |
|---|---|---|---|
| Units and GW ordered and sold by class, 14 quarters (10 filings) | section 2 | read again from each filing; all 84 unit cells and 28 GW cells match | yes |
| Power equipment revenue by quarter | 1,180 ... 1,965 | same, except Q2 2025 filed at 1,504 (rebuild 1,505) | yes |
| Power equipment RPO, 15 dates | 13,579 ... 39,261 | same | yes |
| Non-gas revenue by quarter (Nuclear + Hydro + Steam) | 939 ... 1,050 | same | yes |
| HA units in RPO, disclosed | 29, 32, 36, 32, 51 | 29 (3/31/24), 32 (6/30/24), 36 (9/30/24), 32 (12/31/24), 51 (12/31/25) | yes |
| HA roll | ties at all five dates; 70 at 6/30/26 | 22 + 8 - 1 = 29; +4 - 1 = 32; +9 - 5 = 36; +4 - 8 = 32; +43 - 24 = 51; +27 - 8 = 70 | yes |
| HA sold 2023 to H1 2026 = opening + 2023-24 orders | 61 = 28 + 8 + 25 | 14 + 15 + 24 + 8 = 61 | yes |
| Derived order dollars, 14 quarters | 1,593 ... 12,696 | same | yes |
| Price index and HA value by vintage | 286 opening; Q1 2025 321 / $166M; Q2 2025 482 / $249M; Q3 2025 478 / $246M; Q4 2025 594 / $307M; Q1 2026 564 / $291M; Q2 2026 751 / $387M | same | yes |
| Layers at 6/30/26 | HA 70 units $20,173M; other heavy-duty 17.5 GW $8,967M; aero 136 units $7,559M; total $36,699M | 20,173 / 8,967 / 7,559; total 36,698 | yes |
| Street (Bloomberg, 2026-10-01) | H2 2026 5,491; H1 2027 5,383; four quarters 10,874; FY2027 12,151; FY2028 15,888; FY2029 19,256; FY2030 23,469 | same | yes |
| Street low / high, Q3 2026 Power equipment (`06_modl.xlsx`) | 2,063 / 2,591 around 2,394 | same; median 2,433; no broker values shown on the row | yes |
| Estimate counts (`01_eeo_annual.xlsx`) | 22 revenue estimates for Q1 and Q2 2027 | 22 and 22; EBITDA 19 and 19 | yes |
| Base back-test, bias and annual misses | 0.961; -4.4%, -8.2%, +1.6%, -5.3% | 0.9613; same | yes |
| Base half-year misses | -12.9% to +15.3% | same | yes |
| Base rolling four quarters | -12.0% to +4.3% before bias; -8.4% to +8.5% after | -12.0% to +4.3%; -8.5% to +8.5% | yes |
| 9,720 sets: bias p10 / median / p90 | 0.92 / 1.00 / 1.08 | 0.925 / 0.997 / 1.078 (min 0.864, max 1.172) | yes |
| Worst miss, median of sets (p90): annual / half-year / four quarters | 7.6% (13.3%) / 16.5% (24.6%) / 9.5% (14.9%) | 7.6% (13.3%) / 16.5% (24.6%) / 9.5% (14.9%) | yes |
| H2 2026, all sets | 5,172 / 5,504 / 5,783 | 5,171 / 5,503 / 5,782 | yes |
| H1 2027, all sets | 6,408 / 7,019 / 7,718; with H1 factor 6,335 / 6,864 / 7,490 | 6,407 / 7,018 / 7,717; 6,334 / 6,863 / 7,489; lowest set 5,923 | yes |
| Four quarters, all sets | 11,643 / 12,531 / 13,434 | 11,641 / 12,529 / 13,433 | yes |
| FY2027, all sets | 14,409 / 15,819 / 17,445 | 14,408 / 15,818 / 17,444 | yes |
| FY2028 by path (medians) | 18,037 / 20,508 / 22,482 | 18,036 / 20,507 / 22,481 | yes |
| Share of sets with gap above own worst miss | H1 2027 92%; four quarters 76% | 91.7%; 76.4% | yes |
| H1 factor | 0.977 | 0.977 (range across sets 0.928 to 1.048; rebuild shows 0.936 to 1.021) | yes |
| Regression (HA, aero, trend) | 681 / 63.5 / 55.1 / 24.3; R2 0.96; H2 2026 4,604; H1 2027 4,909 | 680.7 / 63.5 / 55.1 / 24.3; 0.962; 4,604; 4,903 | yes |
| First-in-first-out GW layers | H2 2026 4,833 x 0.90 = 4,350; H1 2027 6,736 | 4,834; 4,351; 6,735 | yes |
| 24 HA due in the next four quarters against 19 shipped in the last four | $5.3B against $2.8B | 5,314 against 2,775 | yes |
| Stress table (section 10 of the rebuild) | 13 rows | all rows match on the September ladder path | yes |
| Company schedule check | 0.98 to 1.04 of $31.6B | 0.981 / 1.009 / 1.038 of 31,616; Street total 0.957 | yes |
| Street EBITDA H1 2027; Power revenue H1 2027; company revenue H1 2027 | 4,038; 12,946; 24,111 | 4,038; 12,946; 24,111 | yes |
| Profit effect, H1 2027 | +3.8% to +26.0% of 4,038 | same arithmetic | yes |
| Guide-implied H2 2026 equipment | $5.2B to $6.0B | 5,221 to 5,961 on the FY2025 base of 19,767; 5,346 to 6,088 on the restated base of 19,873 | yes |
| Company statements | 5 GW a quarter in Q3 and Q4 2026, "the beginning of next year will feel generally very similar", 6 GW "sometime in the second half of next year", then 7; 2026 backlog margin points to 2029 and 2030; 18% to 20% Power organic growth for 2026; aero "comes first"; December 2025 framework (high-teens Power growth to 2028, about 24 GW in 2028, 90 to 100 heavy-duty units, sold out through 2028) | each read again in the corpus or the transcript; wording confirmed | yes |

## 2. Slips found (none changes a conclusion on its own)

| # | Point | Effect |
|---|---|---|
| 1 | The stress table uses the September ladder path, where the H1 2027 base gap is +35%. The headline gap (+28%) is the median over three paths. The ladder ships the same 10 GW in H1 2027 but books revenue early for the 5.5 and 6 GW quarters that follow | On the 5 GW a quarter path each stress case is 6 to 8 points lower (section 6). "The gap goes to zero only when several adverse inputs are combined" holds on the ladder only |
| 2 | Street H1 2027 in class terms: "$122M to $166M per HA" uses aero at $45M only. With aero at $68M (the other end of the range the rebuild states) it is $52M to $98M | Range is wider than shown |
| 3 | "Power revenue H1 2027 +8% to +18%" adds the extra equipment revenue without the H1 factor to the Street Power total. Street services (7,294) plus the model's equipment with the H1 factor is +5% / +9% / +14% | Smaller than shown |
| 4 | "The 0.90 haircut is not supported" and "the model matches the guided half" are both true only for the strict quarterly ordering. For the target half the model's figure (6,864 to 6,900) equals the first build's layer dollars for backlog positions 10 to 20 GW with no haircut (6,735) | The H1 2027 centre is the first build's number without its 0.90 conversion |
| 5 | Equipment revenue Q2 2025 is 1,504 as filed (1,505 used); H1 2026 is 3,851 as filed (3,850 used) | None |

## 3. Back-test on every window

### 3a. Base parameters, every window (reported / (model x bias) - 1)

| Window type | Windows | Misses | Worst | Root mean square |
|---|---|---|---|---|
| Single quarters | 14 | -14%, -5%, +9%, +6%, -3%, +8%, -10%, -8%, -6%, -9%, +15%, +25%, +5%, -7% | 25% | 11% |
| Rolling two quarters | 13 | -9%, +2%, +7%, +2%, +2%, -3%, -9%, -7%, -8%, +2%, +20%, +14%, -1% | 20% | 9% |
| Calendar half-years | 7 | -9.4%, +6.8%, +2.2%, -9.1%, -7.8%, +19.9%, -1.4% | 19.9% | 9.9% |
| Rolling four quarters | 11 | -0.6%, +2.1%, +4.8%, -0.1%, -4.5%, -5.2%, -8.5%, -2.8%, +5.7%, +8.5%, +8.0% | 8.5% | 5.4% |
| Annual (2023, 2024, 2025, H1 2026) | 4 | -0.6%, -4.5%, +5.7%, -1.4% | 5.7% | 3.7% |

These use a bias fitted on the whole sample, so they are in-sample.

### 3b. Bias fitted only on data to the vantage date (reported units still used)

| Vantage | Bias to date | Next half-year miss | Next four-quarter miss |
|---|---|---|---|
| End 2023 | 0.956 | +2.8% | -3.9% |
| Q1 2024 | 0.951 | -1.6% | -4.2% |
| Q2 2024 | 0.964 | -9.3% | -8.7% |
| Q3 2024 | 0.947 | -5.8% | -1.3% |
| End 2024 | 0.936 | -5.3% | +8.5% |
| Q1 2025 | 0.932 | +5.4% | +11.9% |
| Q2 2025 | 0.925 | +24.6% | +12.2% |
| Q3 2025 | 0.942 | +16.8% | |
| End 2025 | 0.964 | -1.7% | |

- Base set: worst next-half miss 24.6%, root mean square 10.9%. Worst next-four-quarter miss 12.2%, root mean square 8.2%.
- 600 sets sampled from the 9,720: worst next-half miss 12.9% / 20.4% / 37.5% (p10 / median / p90), root mean square 13.3%. Worst next-four-quarter miss 8.0% / 13.2% / 22.4%, root mean square 9.7%.
- The in-sample figures in the rebuild (16.5% half-year, 9.5% four quarters) become 20.4% and 13.2% on this basis.

### 3c. Half-year steps (the form the H1 2027 claim takes)

H2 2026 is common ground (model equals the guide-anchored Street). The claim is the step from H2 2026 to H1 2027: model +23% (base), +20% to +38% (p10 to p90 of sets); Street -2%.

| Step | Reported | Base model | Difference, points |
|---|---|---|---|
| H1 2023 to H2 2023 | +41% | +19% | -21 |
| H2 2023 to H1 2024 | -24% | -21% | +3 |
| H1 2024 to H2 2024 | +30% | +46% | +16 |
| H2 2024 to H1 2025 | -7% | -8% | -1 |
| H1 2025 to H2 2025 | +23% | -5% | -28 |
| H2 2025 to H1 2026 | +4% | +27% | +23 |

- Standard deviation of the difference: 20 points (matches the rebuild).
- Forecast of each half as "last reported half x model step", all sets: root mean square miss 8.6% / 14.3% / 23.3% (p10 / median / p90); worst miss, median of sets, 23%. Last two targets: H2 2025 reported 21% above the forecast; H1 2026 reported 11% below it.
- Reported H2-to-H1 steps: -24%, -7%, +4%. Street H2 2026 to H1 2027: -2%.
- H1 share of the year: 41.6% (2023), 43.6% (2024), 44.8% (2025). Street 2027: 44.3%. Model 2027: 44.8% (July path). So the H1 2027 gap is the FY2027 level gap (+27% to +30%) seen through its first half; it is not a separate timing finding.

## 4. The test the back-test cannot pass: what do the vintage prices add?

Flat-price null: same units, same recognition profiles, same 9,720 parameter sets, one constant value per class, own bias.

| Statistic (after own bias) | Vintage model | Flat-price null |
|---|---|---|
| Worst annual miss, median of sets (p90) | 7.6% (13.3%) | 5.5% (11.7%) |
| Worst half-year miss, median of sets (p90) | 16.5% (24.6%) | 15.4% (19.7%) |
| Worst rolling four-quarter miss, median of sets (p90) | 9.5% (14.9%) | 9.3% (12.1%) |
| Pooled root mean square: annual / half-year / rolling four quarters / single quarter | 5.8% / 9.9% / 5.7% / 12.2% | 4.7% / 8.6% / 4.6% / 10.8% |
| H2 2026 against the Street | -6% / 0% / +5% | -22% / -20% / -18% |
| H1 2027 against the Street | +19% / +30% / +43% | -18% / -15% / -10% |
| Step H2 2026 to H1 2027 | +20% / +27% / +38% | 0% / +5% / +10% |
| H1 2027 if H2 2026 lands on the Street (5,491 x step) | +23% / +30% / +41% | +2% / +7% / +13% |

Price effect of the vintage layers (vintage model / flat null - 1), base set:

| Half | H1 2023 | H2 2023 | H1 2024 | H2 2024 | H1 2025 | H2 2025 | H1 2026 | H2 2026 | H1 2027 |
|---|---|---|---|---|---|---|---|---|---|
| Price effect in the model | -5% | -2% | -3% | +4% | 0% | -4% | +7% | +29% | +55% |
| What the flat null missed (reported / null - 1) | -14% | +4% | -1% | -5% | -8% | +15% | +6% | | |

- Correlation between the model's price effect and what the null missed: 0.07 (half-years), 0.08 (quarters), -0.12 (rolling four quarters).
- Reading: the back-test measures "units x a stable value per unit". It gives the same or a lower error with the vintage information removed. The forward price effect is four to eight times the largest one in the sample. The error figures in section 3 therefore do not describe the error of the forward price step.
- What is in favour of the rebuild: the flat null, the regression and the GW layers x 0.90 all sit 16% to 21% below the guide-implied H2 2026 range ($5.2B to $6.1B). Value per unit is rising in the guided half. That step is already in the Street (5,491). The claim is a second step in H1 2027 that the Street does not have.

## 5. Where the H1 2027 gap sits

Gas value the base model ships in H1 2027, by order quarter: Q1 2025 865; Q2 2025 1,366; Q3 2025 2,637; Q4 2025 976; Q1 2026 103. Total 5,947. **Q2 and Q3 2025 are 67%.**

| Order quarter | All-in $/kW (derived) | Index | HA $M a unit | HA shipped H2 2026 | HA shipped H1 2027 |
|---|---|---|---|---|---|
| Q1 2025 | 415 | 321 | 166 | 8.0 | |
| Q2 2025 | 729 | 482 | 249 | 4.2 | 2.8 |
| Q3 2025 | 620 | 478 | 246 | | 9.1 |

- The index rises 50% between Q1 and Q2 2025. The model reads that as price and ships the cheap layer first.
- Management, Q3 2025 call (corpus source 3796): the change in order dollars per GW is "more mix"; Q2 2025 had "substantially more smaller gas turbines, more aeroderivatives"; combined-cycle equipment booked in a quarter "can sway" the ratio; some non-gas orders carry no GW; on a like basis Q3 2025 was "relatively flat" on Q2 2025.
- The index adjusts for aero count with one broker's 2026 price ratio. It cannot adjust for combined-cycle scope or for the size mix inside other heavy-duty. The rebuild calls the index "rough quarter by quarter".
- The HA identity (70 in RPO = 70 ordered since Q1 2025) is arithmetic under oldest-first. The filings do not state which units remain.

Same model with the four 2025 layers treated as one vintage (average 2025 values in every 2025 unit):

| Case | Path | H2 2026 | H1 2027 | Step | H1 2027 if H2 2026 lands on the Street |
|---|---|---|---|---|---|
| Strict quarterly order (rebuild base) | July / flat | 5,616 (+2%) | 6,899 (+28%) | +23% | +25% |
| 2025 blended | July / flat | 6,198 (+13%) | 6,565 (+22%) | +6% | +8% |
| 2025 blended, company-published order dollars | July / flat | 6,025 (+10%) | 6,344 (+18%) | +5% | +7% |
| Strict quarterly order | ladder | 5,669 (+3%) | 7,262 (+35%) | +28% | +31% |
| 2025 blended | ladder | 6,241 (+14%) | 6,889 (+28%) | +10% | +13% |
| 60 blended sets (3 paths x 5 profiles x 2 order-dollar bases x 2 aero ratios) | all | +8% / +12% / +18% | +19% / +25% / +31% | | +7% / +12% / +16% |
| 60 strict sets, same grid | all | -5% / 0% / +4% | +20% / +27% / +35% | | +24% / +27% / +32% |

- The rebuild lists the blended case as a stress that leaves the gap at +28%. It does: but the same case puts H2 2026 13% to 14% above the guide-anchored Street, above the top of the guide-implied range in most sets. The match to the guided half, used as the model's main forward check, exists only under strict quarterly ordering.
- Two readings of the blended case: (a) the guide is low and both halves print high (first test: H2 2026 Power equipment revenue of $6.0B or more, late January 2027); (b) the model's level is about 12% high and the H1 2027 gap is +7% to +16%.

## 6. Stress cases on the 5 GW a quarter path (base parameters, bias-corrected)

| Case | H2 2026 | H1 2027 | Q3 2026 to Q2 2027 | FY2027 |
|---|---|---|---|---|
| Base | 5,616 (+2%) | 6,899 (+28%) | +15% | +27% |
| Company-published order dollars | 5,436 (-1%) | 6,679 (+24%) | +11% | +24% |
| Output 4.5 GW a quarter | 5,065 (-8%) | 6,140 (+14%) | +3% | +12% |
| Output 4 GW a quarter | 4,540 (-17%) | 5,404 (0%) | -9% | -2% |
| Index of 2025 and later vintages 10% lower | 5,217 (-5%) | 6,312 (+17%) | +6% | +16% |
| Index of 2025 and later vintages 20% lower | 4,813 (-12%) | 5,718 (+6%) | -3% | +5% |
| Index of Q2 2025 and later 20% lower, Q1 2025 kept | 5,051 (-8%) | 5,772 (+7%) | 0% | +5% |
| Output 4.5 GW and index 10% lower | 4,717 (-14%) | 5,621 (+4%) | -5% | +2% |
| 2025 blended | 6,198 (+13%) | 6,565 (+22%) | +17% | +18% |
| 40% of heavy-duty value after shipment (four quarters) | 5,237 (-5%) | 6,539 (+21%) | +8% | +22% |
| 50% of heavy-duty value over eight quarters after shipment | 5,631 (+3%) | 6,730 (+25%) | +14% | +23% |
| Aero relativity 4.0 | 5,780 (+5%) | 7,494 (+39%) | +22% | +36% |
| HA at 4 a quarter (H1 2026 pace), same GW, rest other heavy-duty | 5,474 (0%) | 7,120 (+32%) | +16% | +29% |

- The recognition profile is not what decides the result (+21% to +30%). Q2 2026 call: commissioning of a heavy-duty unit "could take another 18 months at site" after shipment; the eight-quarter tail was added here for that reason.
- Output and the index level decide it. Last four quarters shipped 14.6 GW (3.65 GW a quarter); Q2 2026 shipped 3.3 GW.

## 7. Corrected gap for H1 2027 (Street 5,383)

| Reading | H1 2027 against the Street | Note |
|---|---|---|
| Strict quarterly order, derived order dollars (rebuild) | +28% | reproduced |
| Same with company-published order dollars and the H1 factor | +21% | 6,679 x 0.977 |
| 2025 blended, level kept | +22% to +25% | needs H2 2026 about 12% above the Street |
| 2025 blended, level tied to the guided half | +12% (+7% to +16%) | |
| 10 GW x FY2025 all-in order price ($612 to $635/kW) | +14% to +18% | rebuild section 11d |
| First-in-first-out GW layers x 0.90 | +13% | rebuild section 11d |
| No vintage information, step applied to the guided half | +7% (flat null); +9% (regression step +6.5%) | |
| Company guide history: Power organic growth beat or raised by 3 to 5 points (FY2025 guide 6% to 7%, reported 10%; FY2026 guide 16% to 18%, raised to 18% to 20%), all placed in equipment | +6% to +10% | 3 to 5 points x 10,449 = $313M to $522M |

- Median of the eight readings (mid-points 28, 21, 23, 12, 16, 13, 8, 8): **about +14%**, about $6.1B. Range +6% to +28%.
- Four quarters Q3 2026 to Q2 2027 on the same basis: H2 2026 at the Street and H1 2027 at +14% gives about +7% (rebuild +15%).
- Model-implied Power revenue growth: FY2027 +27% / +33% / +40% (Street services 15,675 plus model equipment, on 23,609 for 2026). Street +19.1%. Company framework: high-teens a year to 2028 (December 2025 and January 2026 releases). H1 2027 Power: model +30% to +41% year on year; Street +23.9%.
- Street per kW: H2 2026 $549, H1 2027 $538, H2 2027 $677, FY2027 $608, FY2028 $691 at 23 GW; last four quarters reported $516. The Street has the price step by H2 2027 (6,768, close to the model's H1 2027 figure of 6,864). Street FY2027 equals 20 GW x the FY2025 all-in order price ($612 to $635/kW) x 0.96 to 0.99.

## 8. Corrected error band for H1 2027

| Source | Size | Basis |
|---|---|---|
| Model with units known, bias known only to date, next half-year | 20.4% worst (median of sets); 13.3% root mean square | section 3b |
| Same, in-sample (rebuild) | 16.5% worst; 9.9% root mean square | reproduced |
| Output: +/-10% of GW | +/-8% | rebuild section 6e |
| Aero rate: +/-4 a quarter | +/-3% | rebuild section 6e |
| Index split between classes | +/-7% | rebuild section 6e |
| Order of 2025 vintages (strict against blended, level tied to the guided half) | +/-7.5% | half of 27% less 12%, section 5 |
| Price step never observed in the sample | not measurable | section 4 |

- Combined (root of the sum of squares): worst-miss basis sqrt(20.4^2 + 8^2 + 3^2 + 7^2 + 7.5^2) = **about +/-24%**; with the rebuild's 16.5% it is +/-21%; root-mean-square basis sqrt(13.3^2 + 8^2 + 3^2 + 7^2 + 7.5^2) = +/-19%. Used: **about +/-23%**.
- Four quarters: sqrt(13.2^2 + 8^2 + 3^2 + 7^2) = about +/-17% (rebuild +/-9.5% before inputs).
- Gap against band: +14% against +/-23% (H1 2027); +7% against +/-17% (four quarters). On the rebuild's own figures: +28% against +/-20%.

## 9. The six kill reasons, one by one

| # | Kill reason | Rebuild's answer | Check | Status |
|---|---|---|---|---|
| 1 | Rival explanation of the Street | Conceded for FY2028. For H1 2027: the Street needs 2024-vintage dollars per HA, and no pre-2025 HA is left in RPO | The HA count is right under oldest-first. The dollar value per HA by quarter is not identified (section 5). Other ordinary readings of Street H1 2027 fit: (a) the usual H1 share of the year (44.3% against 41.6% to 44.8%); (b) FY2027 = 20 GW x FY2025 all-in order price; (c) FY2027 Power +19%, equal to the company's high-teens framework; (d) the Street carries the step two quarters later ($677/kW in H2 2027). Disclosed data cannot reject any of them | **Not answered** (argued) |
| 2 | Gap sat in one order layer lifted by aero mix and combined-cycle scope | H1 2027 uses no Q2 2026 heavy-duty dollars | True. The gap now sits in the Q2 and Q3 2025 layers (67% of the value shipped), against a cheap Q1 2025 layer. Management gave the same mix and scope explanation for those quarters. With Q2 2025 and later layers 20% lower the gap is +7%; with 2025 blended and the level tied to the guided half, +8% | **In part** (moved to another layer pair) |
| 3 | Error band | 9.5% four quarters, 16.5% half-year, 7.6% annual; +/-20% used | Reproduced. With bias known only to date: 13.2% and 20.4%. The flat-price null does as well or better, so the band covers units, not the price step that makes the gap | **In part** |
| 4 | Reveal date | H1 2027 in the Q2 2027 10-Q, late July 2027; Q1 2027 in late April 2027 | Inside 12 months. Q2 10-Qs were filed 2024-07-24, 2025-07-23, 2026-07-22. The FY2027 guide (late January 2027) comes first; by the rebuild's own marks a guide of +20% or less contradicts | **Answered** |
| 5 | Thin Street data | "Not fixed" | Confirmed: no broker values on the Power equipment row; Q3 2026 low / high -14% / +8%; Street Power organic growth is 18.0 in all four 2027 quarters; equipment + services is 269 below the Power total in H1 2027. At the corrected gap the company revenue line moves +3%, inside the Q3 2026 low / high of -4% / +3% | **Not answered** (conceded) |
| 6 | Small profit effect | +4% to +26% of H1 2027 EBITDA | Arithmetic reproduced. At the corrected gap (+14%, $753M): $113M / $188M / $339M at 15% / 25% / 45% = +2.8% / +4.7% / +8.4% of 4,038. Same size as the first build's +3% to +10% | **In part** (only at the uncorrected gap) |

## 10. What stands whatever the verdict

1. Unit facts are right: HA roll ties to the five disclosed counts; 70 HA, about 17.5 GW of other heavy-duty and about 136 aero make 53.0 GW (aero opening is an assumption).
2. Every method with no price step (flat null, regression, GW layers x 0.90) is 16% to 21% below the guide-implied H2 2026 equipment range. Value per unit is stepping up in the guided half.
3. The Street in physical terms: $538 to $549/kW through H1 2027, $608 for FY2027, against 2025 all-in order prices of $612 to $635 and Q4 2025 to Q2 2026 orders at $705 to $1,049.
4. The driver structure (non-gas base + aero units x value + HA units x value + other heavy-duty GW x $/kW, with a recognition profile) back-tests at 4% to 6% on annual windows with units known. The vintage layer adds nothing measurable yet.

## 11. Company-reported numbers that would change this check

| Date | Number | What it would show |
|---|---|---|
| 2026-10-28 (Q3 10-Q) | GW sold; HA, other heavy-duty and aero units sold; Power equipment revenue | First quarter that ships 2025-ordered HA under oldest-first. At 5 GW, 6 HA and 16 aero: flat null about 2,170 to 2,190; Street 2,394; strict-order model 2,410 to 2,620 (by profile); 2025 blended about 3,070. Only a print near 3.0B separates the model from the Street this early |
| Late January 2027 | H2 2026 Power equipment revenue | $6.0B or more on about 10 GW supports the blended level (both halves high); about $5.5B leaves only the strict-order step |
| Late January 2027 | FY2027 Power organic growth guide | The model needs +27% or more; Street and framework are at +19% |
| Late April 2027 (Q1 10-Q) | Q1 2027 Power equipment revenue | Flat null about 2,220 to 2,310; Street 2,585; model 3,100 to 3,260 |
| Any filing | Equipment RPO by delivery year, a heavy-duty-only order price, or HA units in RPO by order year | Would remove the ordering and scope questions in section 5 |

## 12. Reproduce

Scripts (scratchpad `ucchk/`): `m.py` (independent model: classes, vintage layers, profiles, flat-price null, blended 2025, deck order dollars), `t1.py` (base), `t2.py` and `t3.py` (9,720 sets, vintage and null), `t4.py` (half-year steps), `t5.py` (every window, bias to date, price-effect test, one-at-a-time cases), `t7.py` (regression, GW layers, class split of the Street, schedule, profit), `t8.py` (stress cases by path, blended grids), `t9.py` (by path, bias-to-date across sets), `x1.py` (Bloomberg low / high and counts), `q2.py` to `q5.py`, `s1.py`, `s2.py` (corpus reads). The rebuild's own section 17 script was also run as written and prints the figures it states.

Flat-price null in one step: in the rebuild's `model()`, after the loop, replace each class's quarterly shipped value with (sum of shipped value 2023 to H1 2026 / sum of units shipped 2023 to H1 2026) x units shipped, then apply the same profiles and bias.

Inputs: `data/gev.db` (read-only; accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148; sources 3161, 3796, 1844, 2648, 671, 3689); `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `06_modl.xlsx`, `01_eeo_annual.xlsx` (Bloomberg, 2026-10-01); gevernova.com conference transcript of 2026-09-16.
