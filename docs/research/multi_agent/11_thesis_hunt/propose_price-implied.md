# Thesis hunt, lens: what the price implies (2026-10-01)

_AI-assisted research input only: facts, arithmetic, tables and sources. No memo sentences. The team chooses every forecast number and the direction. Bloomberg data is licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep it inside the project folder._

Units: $M unless stated. "Street" = Bloomberg BEst mean. "NTM" = next twelve months. "SRA" = slot reservation agreement (a paid reservation of a gas-turbine production slot; not in backlog). "All-in $/kW" = Power equipment orders in dollars divided by gas-turbine gigawatts ordered in the same period (it includes steam turbines, generators, aeroderivatives and non-gas equipment in the numerator).

Scripts (scratchpad, reproducible from the files named below): `implied.py`, `peers.py`, `hist.py`, `rpo.py`, `tables.py`, `gw.py`.

---

## 0. Result on one screen

| Question | Answer |
|---|---|
| What does $987.45 need from EBITDA if the multiple stays at 28.5x? | Nothing new. At 28.5x the price is covered by NTM EBITDA of $8,937M. Street NTM is $8,686M (calendar blend) to $8,923M (Bloomberg's own blend). |
| What does it need if the multiple moves to where peers' growth puts it? | Late January 2027 (fitted 24.6x): NTM EBITDA of $10,250-10,350M, which is **5.4% to 6.4% above the Street** ($9,727M). End of September 2027 (fitted 21.2x): $11,650-12,010M, **-1% to +2% against the Street** ($11,783M). |
| Break-even multiple on Street numbers | 26.2x in late January 2027; 21.6x at end of September 2027 (21.0x after counting the Street's own free cash flow). |
| What multiple do the sell-side targets assume? | The average target of $1,225 equals 27.0x the Street's September-2027 NTM EBITDA. The price itself only needs 21.6x. The gap between the two is 5.4 turns. |
| Reverse DCF on Street free cash flow | 86% of enterprise value sits after 2030. At a 9% discount rate the price needs a 2030 exit of 16.2x trailing EBITDA, or free cash flow growing 4.7% a year for ever from $13.0B. |
| Operating number the price most clearly mis-states (near term) | Equipment revenue already scheduled in backlog. The 10-Q schedule leaves $15.8B for H1 2027; the Street has $14.4B. (Full work in `propose_rpo-equipment.md`; this file adds the price translation.) |
| Operating number the price most clearly mis-states (long term) | The price per kW inside the Street's 2029 Power equipment revenue. $19,256M over the stated 26-28 GW is $688-741/kW. Orders booked in H1 2026 were $909/kW, and management guided H2 2026 orders to about $838-874/kW. |
| Does either one make the stock cheap by itself? | No. The near-term gap (+2% to +8% EBITDA) is about the size the price already needs by January on the peer line (+5.4% to +6.4%). The long-term gap is offset in revenue terms by Street Power services running ahead of the company's own path (`propose_power-services.md`). |

---

## 1. Inputs and where they are

| Item | Value | Source |
|---|---|---|
| Price | $987.45 | Bloomberg, 2026-10-01; workbook `GEV_bloomberg_pull_filled_2026-10-01.xlsx`, sheet Snapshot, row 3, PX_LAST |
| Market capitalisation | $262,991M | Snapshot row 3, CUR_MKT_CAP |
| Enterprise value | $254,694M | Snapshot row 3, CURR_ENTP_VAL |
| Shares | 266.33M | Snapshot row 3, EQY_SH_OUT |
| Equity bridge (market cap less EV) | +$8,297M | computed |
| Forward EV/EBITDA | 28.54x, so Bloomberg's NTM EBITDA = 254,694 / 28.544 = $8,923M | Snapshot row 3, BEST_EV_TO_BEST_EBITDA |
| Street EBITDA 2026-2030 | 6,334 / 9,471 / 12,553 / 16,496 / 19,544 | sheet Consensus, row 3 |
| Street revenue 2026-2030 | 46,240 / 53,029 / 60,985 / 70,851 / 79,724 | Consensus row 2 |
| Street FCF 2026-2030 | 12,196 / 7,654 / 9,527 / 9,702 / 13,036 | Consensus row 16 |
| Quarterly and division Street | `GEV_Pull_2026-10-01/segment_quarterly.json`, keys "Block\|Parent\|Line\|YYYY Qn" | Bloomberg EEO company-specific exports |
| Average price target, ratings | $1,225.32; 32 buy / 7 hold / 2 sell | Snapshot row 3 |
| 30-day implied volatility | 48.33% (weekly series: 43.0-44.7% in September) | Snapshot row 3; sheet PricePositioning |

NTM EBITDA used below (calendar blend of Street annual figures):

| Date | Formula | NTM EBITDA | NTM revenue | Margin | Sum of the four Street quarters |
|---|---|---|---|---|---|
| 1 Oct 2026 | 0.25 x FY26 + 0.75 x FY27 | 8,686 | 51,332 | 16.9% | 8,883 (Q4'26-Q3'27) |
| Late Jan 2027 | 11/12 x FY27 + 1/12 x FY28 | 9,727 | 53,692 | 18.1% | 9,391 (FY27 quarters) |
| End Sep 2027 | 0.25 x FY27 + 0.75 x FY28 | 11,783 | 58,996 | 20.0% | 11,906 (Q4'27-Q3'28) |

---

## 2. The price reversed into EBITDA

Formula: NTM EBITDA needed = (target price x 266.334 - 8,297) / multiple. "With cash" also subtracts the Street's own free cash flow from 30 June 2026 to the date, less dividends ($2,518M by late January 2027; $7,679M by end of September 2027).

### 2.1 Late January 2027 (Street NTM $9,727M)

| Target price | 20x | 23x | 25x | 28.5x |
|---|---|---|---|---|
| Flat, $987.45 | 12,735 (+30.9%) | 11,074 (+13.8%) | 10,188 (+4.7%) | 8,937 (-8.1%) |
| Flat, with cash | 12,609 (+29.6%) | 10,964 (+12.7%) | 10,087 (+3.7%) | 8,848 (-9.0%) |
| +10% a year, $1,018 | 13,142 (+35.1%) | 11,428 (+17.5%) | 10,514 (+8.1%) | 9,222 (-5.2%) |
| +20%, $1,185 | 15,365 (+58.0%) | 13,361 (+37.3%) | 12,292 (+26.4%) | 10,782 (+10.8%) |

Margin on Street NTM revenue ($53,692M) that each flat-price cell needs: 23.7% / 20.6% / 19.0% / 16.6%. The Street has 18.1%.

### 2.2 End of September 2027 (Street NTM $11,783M)

| Target price | 20x | 23x | 25x | 28.5x |
|---|---|---|---|---|
| Flat, $987.45 | 12,735 (+8.1%) | 11,074 (-6.0%) | 10,188 (-13.5%) | 8,937 (-24.2%) |
| Flat, with cash | 12,351 (+4.8%) | 10,740 (-8.9%) | 9,881 (-16.1%) | 8,667 (-26.4%) |
| +10%, $1,086 | 14,050 (+19.2%) | 12,217 (+3.7%) | 11,240 (-4.6%) | 9,859 (-16.3%) |
| +20%, $1,185 | 15,365 (+30.4%) | 13,361 (+13.4%) | 12,292 (+4.3%) | 10,782 (-8.5%) |

Margin on Street NTM revenue ($58,996M) for the flat-price row: 21.6% / 18.8% / 17.3% / 15.1%. The Street has 20.0%.

### 2.3 Price on Street numbers at each multiple

| Date | 16.5x | 20x | 21.2x | 23x | 24.6x | 25x | 27.3x | 28.5x | Break-even multiple |
|---|---|---|---|---|---|---|---|---|---|
| Late Jan 2027 | $634 (-36%) | $762 (-23%) | $805 (-18%) | $871 (-12%) | $930 (-6%) | $944 (-4%) | $1,028 (+4%) | $1,072 (+9%) | 26.2x (25.9x with cash) |
| End Sep 2027 | $761 (-23%) | $916 (-7%) | $969 (-2%) | $1,049 (+6%) | $1,119 (+13%) | $1,137 (+15%) | $1,239 (+25%) | $1,292 (+31%) | 21.6x (21.0x with cash) |

27.3x is the lowest weekly close of the last twelve months (2026-08-28). Since the 2024 spin the weekly series has 130 observations; 26 were at or below 21x and 40 at or below 25x; the last of them was the week of 2025-04-18.

### 2.4 Reverse DCF on Street free cash flow

Cash flows: H2 2026 $2,651M (Street Q3 + Q4), then 7,654 / 9,527 / 9,702 / 13,036. Terminal value needed at end of 2030 = (EV - present value of those cash flows) x (1 + r)^4.25.

| Discount rate | PV of FCF to 2030 | Share of EV | Terminal value needed | As a multiple of 2030 EBITDA (trailing) | Perpetual FCF growth it implies |
|---|---|---|---|---|---|
| 8% | 35,796 | 14% | 303,594 | 15.5x | 3.6% |
| 9% | 35,081 | 14% | 316,753 | 16.2x | 4.7% |
| 10% | 34,392 | 14% | 330,322 | 16.9x | 5.8% |
| 11% | 33,726 | 13% | 344,311 | 17.6x | 7.0% |

- EV / Street EBITDA by year: 40.2x (2026), 26.9x (2027), 20.3x (2028), 15.4x (2029), 13.0x (2030).
- Street FCF as a share of market capitalisation: 4.6% / 2.9% / 3.6% / 3.7% / 5.0%. Street FCF as a share of Street EBITDA: 193% / 81% / 76% / 59% / 67%.
- Reading for the model: about six-sevenths of the value rests on what 2030 EBITDA is made of and how long it lasts. Section 6 looks at its make-up.

---

## 3. Where peers trade for the growth they are expected to deliver

Inputs from sheet Consensus (BEST_EBITDA and BEST_SALES rows of each company block) and sheet Snapshot column I. Growth = two-year compound growth of EBITDA from the first to the third forecast year. Margin = second forecast year.

| Company | Forward EV/EBITDA | EBITDA growth yr1-yr3 | yr2-yr4 | yr3-yr5 | Margin yr2 | Multiple / growth |
|---|---|---|---|---|---|---|
| GE Vernova | 28.5 | 40.8% | 32.0% | 24.8% | 17.9% | 0.70 |
| Bloom Energy | 51.7 | 76.6% | 47.1% | 29.6% | 26.0% | 0.67 |
| Vertiv | 20.6 | 31.8% | 20.0% | 15.3% | 26.3% | 0.65 |
| Siemens Energy | 12.5 | 27.4% | 18.7% | 12.6% | 17.8% | 0.46 |
| Quanta | 22.3 | 16.0% | 14.9% | 14.0% | 10.5% | 1.39 |
| Mitsubishi Heavy | 15.2 | 15.9% | 14.8% | 13.6% | 14.4% | 0.96 |
| Eaton | 21.1 | 14.5% | 13.9% | 12.5% | 24.9% | 1.46 |
| Baker Hughes | 10.9 | 14.3% | 12.8% | 7.0% | 18.6% | 0.76 |
| ABB | 18.7 | 14.1% | 11.4% | 6.5% | 22.4% | 1.33 |
| Schneider | 16.5 | 13.6% | 12.4% | 12.4% | 22.9% | 1.21 |
| Hitachi | 11.9 | 12.9% | 15.3% | 13.9% | 17.2% | 0.92 |
| Hubbell | 15.6 | 10.7% | 6.1% | 5.3% | 25.3% | 1.46 |

Least-squares fits, multiple = a + b x growth (in points) + c x margin (in points):

| Sample | a | b | c | R-squared | Residual s.e. | GEV fitted today | Late Jan 2027 (growth 32.0%, margin 20.6%) | End Sep 2027 (growth 24.8%, margin 23.3%) |
|---|---|---|---|---|---|---|---|---|
| 11 peers | 5.48 | 0.521 | 0.121 | 0.82 | 5.4 turns | 28.9x (actual 28.5x) | 24.6x | 21.2x |
| 11 peers, growth only | 7.71 | 0.533 | | 0.81 | 5.1 | 29.5x | 24.8x | 20.9x |
| 10 peers, Bloom removed | 12.87 | 0.076 | 0.117 | 0.04 | 4.5 | 18.1x | 17.7x | 17.5x |

- With Bloom Energy in the sample, GEV sits on the line today. The slope is about half a turn per point of growth, so the fitted multiple falls 4 turns by January and 7 turns by next September as the growth in the window slows from 41% to 25%.
- The slope rests on one company. Without Bloom Energy there is no relation between growth and multiple among these peers, and GEV trades 10 turns above the group.
- GEV against its own history (sheets Multiples and ConsensusHistory): forward multiple divided by the Street's FY27-to-FY29 EBITDA growth (in points) has ranged from 0.90 to 1.68 since January 2025, median 1.20. It is 0.89-0.91 now, the lowest reading; it was 0.97 to 1.20 in the March-April 2025 sell-off. Applied to 24.8% growth next September: 22.6x at today's ratio, 24.1x to 29.8x at the 2025 sell-off ratios.
- The sell-side: average target $1,225.32. (1,225.32 x 266.334 - 8,297) / 11,783 = **27.0x** September-2027 NTM EBITDA. The targets assume the multiple barely moves; the peer line says 21x; the price needs 21.6x.

Multiple range to carry into scenarios for September 2027: 17.5x (peers without Bloom), 21-22.6x (peer line; own ratio today), 24-27.3x (low end of the own 2025 sell-off ratios; 12-month low), 28.5x (today).

---

## 4. Bloomberg DDM screen and options

**DDM screenshot (`18_ddm.png`, default settings).** Inputs shown: EPS $24.388 / $24.517 / $34.802 for FY1-FY3; dividend $1.991; 3 growth years then 14 transition years; long-term growth 67.72% (the consensus field); payout 8.164% in growth years and 45% at maturity; growth at maturity 9.302%; bond rate 5.241%; country premium 9.613%; beta 1.214. Discount rate = 5.241 + 1.214 x 9.613 = 16.91%.

| Output | Value | What it means |
|---|---|---|
| Theoretical price | $4,106 (+316%) | Uses the 67.72% growth field for three years. Not usable. |
| Implied growth rate | 44.2% | EPS growth in the three growth years (after FY3, so 2029-2031) at which the model equals $987.45, at a 16.9% discount rate. |
| Street EPS growth for comparison | +42.0% (2028), +29.9% (2029), +21.0% (2030) | Consensus sheet row 11 |

The screen's discount rate is far above any rate used in section 2.4, so its "implied growth" is high for that reason. It adds no number that section 2 does not give more directly.

**Options.** 30-day implied volatility 48.33% on 1 October; it was 43.0-44.7% through September, before the 28 October report entered the 30-day window.

| Item | Arithmetic | Result |
|---|---|---|
| Total 30-day variance | 0.4833^2 x 30/365 | 0.01920 |
| Less 29 ordinary days at 43-45% | 0.43^2 to 0.45^2 x 29/365 | 0.01469 to 0.01609 |
| Variance left for the report day | | 0.00311 to 0.00451 |
| Implied one-day move (one standard deviation) | square root | 5.6% to 6.7% (average absolute move about 4.4% to 5.4%) |
| Past report-day moves (nine since the spin) | -4.5, +1.3, +2.7, +3.1, +14.6, -1.6, +2.7, +13.8, -8.7 | mean absolute 5.9%, median 3.1% |
| One standard deviation to late January 2027 at 48% | 0.4833 x sqrt(118/365) | +/-27.5%: $750 to $1,300 |
| One standard deviation over twelve months | | +/-48%: $609 to $1,601 |

The options price a report-day move in line with the stock's own average. Put-to-call open interest 1.45 (1.06 in January). Short interest 8.76M shares, down from 11.68M in early July.

---

## 5. What the price needs set against each number-first finding

Y for the X-Y-Z sentence, by line. "Needed" figures come from section 2; "arithmetic" figures come from the lens files in this folder and from section 6.

| Line and period | X: Street | Y: what the price needs | Z: arithmetic on disclosed data | Reading |
|---|---|---|---|---|
| Adj. EBITDA, FY27 (as seen in late January 2027) | $9,471M (36 analysts) | $10,250-10,350M NTM for a flat price at the peer-line multiple of 24.6x, i.e. +5.4% to +6.4%; $8,850-8,940M if the multiple stays 28.5x | Backlog schedule adds $0.2-0.7B to four-quarter EBITDA (+2% to +8%); Wind H1 2027 takes off $0.05-0.25B | The arithmetic upside is about what the price needs. No excess. |
| Adj. EBITDA, NTM at end of September 2027 | $11,783M | $11,650-12,010M at 21.2x (flat); $13,250M for +10% at 21.2x (+12.5%); $12,290M for +20% at 25x (+4.3%) | No line in any lens moves FY28 EBITDA by 12% | A return above 10% needs a multiple above 23x, not a number. |
| Equipment revenue, Q3 2026 to Q2 2027 | $30,245M | At the Street's margin the January requirement (+$0.5-0.6B EBITDA) is about +$2.6-3.1B of revenue | $31,616M scheduled; $32.5-34.9B with the uplift seen in six of seven windows (+7.5% to +15.5%); $29.0B if the one miss repeats | Candidate 1 below |
| Power equipment revenue, FY2029 | $19,256M | The price capitalises 2030 EBITDA at about 16x (section 2.4); the Street's 2029-2030 equipment line embeds $688-782/kW | 26-28 GW x $790-875/kW = $20.5-24.5B (+7% to +27%) | Candidate 2 below |
| Power services revenue, FY2030 | $22,357M | Same terminal value; the Street has services at 49% of 2030 Power revenue | $17.8-20.8B on the company's own chart and a component build (`propose_power-services.md`) | Offsets candidate 2 in revenue; changes the mix of 2030 profit |
| Free cash flow, FY26 and FY27 | $12,196M / $7,654M | 2.9% FCF yield on FY27 | FY26 +2% to +19%; FY27 -43% to +36% (`propose_fcf-deposits.md`); this lens's own roll-forward gives H2 2026 $1.6-8.0B against Street $2.65B | Band wider than gap. Not a candidate. |

---

## 6. The price translated into gigawatts and dollars per kilowatt

### 6.1 Disclosed inputs

Power equipment orders in dollars (earnings-deck appendix, "Power: key performance metrics", decks of 2026-01-28 and 2026-07-22) and gas-turbine gigawatts ordered (10-Q and 10-K unit tables):

| Period | Power equipment orders $M | Gas GW ordered | All-in $/kW |
|---|---|---|---|
| FY24 | 8,340 | 20.2 | 413 |
| Q4 24 | 2,906 | 6.1 | 476 |
| Q1 25 | 2,842 (6,361 less 3,519) | 7.1 | 400 |
| Q2 25 | 3,519 | 5.1 | 690 |
| Q3 25 | 4,448 (18,241 less 6,361 less 7,432) | 7.4 | 601 |
| Q4 25 | 7,432 | 10.2 | 729 |
| FY25 | 18,241 | 29.8 | 612 |
| Q1 26 | 5,611 (18,261 less 12,650) | 8.0 | 701 |
| Q2 26 | 12,650 | 12.1 | 1,045 |
| H1 26 | 18,261 | 20.1 | 909 |

- Check against management: "first half 2026 orders were priced more than 20% above 4Q'25 equipment orders" (Q2 2026 call). 909 / 729 = +24.7%. The measure reproduces the statement.
- H2 2026 guide (same call): gas equipment orders "at the higher end of the range of 10 to 20 points versus 4Q'25 orders", tied to the "large SRA balance". 729 x 1.15 to 1.20 = **$838-874/kW**.
- Q2 2026 is lifted by mix: 61 aeroderivative units and "incremental combined cycle equipment as SRAs converted to orders". Q1 2026 was heavy-duty and HA-weighted (28 heavy-duty units, 12 HA, 9 aeroderivatives) at $701/kW.
- Realised Power equipment revenue per kW shipped: $480 (FY24: 5,708 / 11.9 GW), $437 (FY25: 6,686 / 15.3), $513 (H1 26: 3,851 / 7.5). FY25-H1 26 shipments carry roughly the FY24 order price ($413) plus aeroderivative and non-gas equipment.

Gigawatts:

| Item | Value | Source |
|---|---|---|
| Under contract 30 June 2026 | 53 GW backlog + 63 GW SRAs = 116 GW | Q2 2026 release |
| Output plan at the Q2 call (2026-07-22) | 5 GW a quarter from Q3 2026 ("at least 30 gigawatts" over six quarters); 24 GW annualised in 2028; 30 GW in 2030 | Q2 2026 call transcript, corpus source 3161 |
| Output plan at the September conference (2026-09-16) | 5 GW a quarter in Q3-Q4 2026 and early 2027; 6 GW a quarter "sometime in the second half of next year"; in 2028 "six gigawatts for a period of time" then 7 GW a quarter | Conference transcript, gevernova.com PDF |
| Deliveries by year on the two plans | 2027: 20 / 22 GW; 2028: 24 / 26; 2029: 26 / 28; 2030: 30 / 30 | computed |
| Identity check | Backlog end-2023 (16.7 GW) + orders 2024 (20.2) + 2025 (29.8) = 66.7 GW = deliveries 2024 (11.9) + 2025 (15.3) + 2026 (17.5) + 2027 (22.0) | So deliveries from 2028 on come from orders booked in 2026 or later, apart from sequencing between short-lead and long-lead units |
| Second check | 10 + 22 + 26 + 28 + 30 = 116 GW for H2 2026 to 2030 = the 116 GW under contract | "mostly sold out through '30" (Q2 call) |
| Management on timing | 2025 margin reaches the income statement in "'27, '28"; the 2026 change "tells you the equipment margins for '29 and '30, largely" | S01 research file; September conference |

### 6.2 What the Street's Power equipment line implies

Street Power equipment revenue (sum of quarters, key `Total Revenue|Power|Equipment`):

| Year | Street $M | $/kW at the July plan | $/kW at the September plan | GW the Street figure buys at $612 (FY25 orders) | at $729 (Q4 25) | at $856 (H2 26 guide mid) | at $909 (H1 26) |
|---|---|---|---|---|---|---|---|
| 2027 | 12,151 | 608 (20 GW) | 552 (22 GW) | 19.9 | 16.7 | 14.2 | 13.4 |
| 2028 | 15,888 | 662 (24 GW) | 611 (26 GW) | 26.0 | 21.8 | 18.6 | 17.5 |
| 2029 | 19,256 | 741 (26 GW) | 688 (28 GW) | 31.5 | 26.4 | 22.5 | 21.2 |
| 2030 | 23,469 | 782 (30 GW) | 782 (30 GW) | 38.3 | 32.2 | 27.4 | 25.8 |

- 2027: $552-608/kW sits between the FY24 and FY25 order prices. Consistent with deliveries of 2024-2025 orders plus short-lead units. **No gap.**
- 2028: $611-662/kW equals the FY25 order price ($612) on the September plan. Consistent with GEV's own 2028 framework (Power revenue at a high-teens growth rate implies about $15-17B of equipment). **No gap on management's timing.** On the gigawatt identity alone (2028 deliveries come from 2026 orders) it would be 26 x $701-909 = $18.2-23.6B; the two readings differ by which orders fill which slots, and the filings do not say.
- 2029: $688-741/kW is at or below the Q4 2025 order price. Orders booked in 2026 are $838-909/kW, and both the gigawatt identity and management's own timing put 2026 orders into 2029 deliveries.
- 2030: $782/kW at 30 GW is 7-14% below the 2026 order price.
- Three-year check: Street 2028-2030 = $58,614M. If the $18,261M of H1 2026 orders is delivered in those years, the Street leaves $40,353M for the slot-reservation book, which is $641-734/kW on 55-63 GW. The 2026 conversions were booked at $701/kW (Q1, HA-weighted) to $1,045/kW (Q2, aeroderivative-weighted).

### 6.3 FY2029 arithmetic

Power equipment revenue = gigawatts delivered x all-in order price of the orders that fill those slots.

| GW delivered | at $729 (Q4 25) | at $790 | at $838 (guide low) | at $875 (guide high) | at $909 (H1 26) |
|---|---|---|---|---|---|
| 26 (July plan) | 18,954 (-2%) | 20,540 (+7%) | 21,788 (+13%) | 22,750 (+18%) | 23,608 (+23%) |
| 28 (September plan) | 20,412 (+6%) | 22,120 (+15%) | 23,464 (+22%) | 24,500 (+27%) | 25,424 (+32%) |

- Range used: $20.5-24.5B (26 GW at $790 to 28 GW at $875), +7% to +27% against $19,256M. Centre about $22.6B (27 GW x $838), +17%.
- The $790 low end allows three-tenths of 2029 deliveries to carry the Q4 2025 price and the rest the low end of the guide.
- Floor: if every 2029 delivery carried the Q4 2025 price on the July plan, the result is $19.0B, 2% below the Street.
- FY2030 by the same method: 28-30 GW x $790-909 = $22.1-27.2B, -6% to +16%, centre $25.7B (+9%). The band crosses zero, so 2030 is not a candidate on its own.

### 6.4 What it does to profit and to the mix

| Item | Street 2029 | With section 6.3 and the services lens |
|---|---|---|
| Power equipment | 19,256 | 20,500-24,500 |
| Power services | 19,711 | 16,800-18,800 (`propose_power-services.md` section 4) |
| Power revenue | 39,522 | 37,300-43,300 (-6% to +10%) |
| Equipment share of Power revenue | 48.7% | 52% to 59% |
| Power adj. EBITDA | 9,983 (25.3%) | Equipment: +$1.2-5.2B of revenue. If it is price on the same gigawatts it drops through at 60-90%; if it is extra gigawatts, at about 35-40%. Services: -$0.9-2.9B of revenue at 35-50%. Net from about -$1.0B (small extra-gigawatt gain, large services shortfall) to +$4.4B (price gain, small services shortfall); centre about +$1.2B (+$3.3B x 60% less $1.8B x 42%), which is +7% of Street GEV EBITDA ($16,496M). |

- Total Power revenue shows no gap. The finding is about what the revenue is made of: more equipment at 2026 prices, less services.
- Earlier work on order-vintage margins put 2029 Power EBITDA 9% above the Street and total EBITDA 4% above (`BLOOMBERG_VERDICT.md` section 9). This revenue view agrees in direction and is no tighter.
- For the terminal value in section 2.4: equipment revenue depends on how long 30 GW a year lasts; services revenue does not. A 2030 profit base with 55-60% equipment is a different thing to capitalise at 16x than one with 50%.

---

## 7. Candidates from this lens

### Candidate 1. Equipment revenue, Q3 2026 to Q2 2027 (price translation of the backlog schedule)

| Field | Value |
|---|---|
| X | $30,245M (Power 10,874; Electrification 13,541; Wind 5,830). H1 2027 alone: $14,424M |
| Z | $31,616M scheduled (36% x $87,821M, 10-Q Q2 2026 note 9); $32.5-34.9B at the conversion ratios of six of the seven reported windows (1.028 to 1.105); $29.0B at the one miss (0.918, the 12/31/23 window) |
| Gap | +4.5% (schedule only); +7.5% to +15.5% (six windows); -4.0% (repeat of the miss). Median of seven: +9.8% |
| H1 2027 | 31,616 - 15,821 (Street H2 2026, which matches the FY26 guide) = $15,795M against $14,424M: +9.5% (+6.5% to +12.5% for rounding of the 36%) |
| Y | For a flat price in late January at the peer-line multiple (24.6x) the Street's FY27 EBITDA has to rise 5.4-6.4%, about $0.5-0.6B. At a 13-20% drop-through that is $2.6-4.6B of extra revenue. The schedule supplies $1.4-4.7B. |
| Seven-window back-test | 0.918, 1.028, 1.036, 1.076, 1.105, 1.050, 1.062 (last two after removing Prolec revenue). Half-year version (schedule less first half, against second half): 0.87, 1.08, 1.20, 1.14 |
| By division (history of next-four-quarter equipment revenue over division equipment RPO) | Wind: 64-67% reported, Street 71%. Electrification: 34-41% reported, Street 33%. Power: 54% -> 47% -> 38% -> Street 28% (falling as the backlog lengthens). If Wind converts at 64-67% and Electrification at 34-37%, the schedule leaves $11.2-12.7B for Power against the Street's $10.9B. |
| Reveal | 2026-10-28: 9/30/26 schedule in the 10-Q against Street Q4 2026-Q3 2027 equipment of $31,314M. Late January 2027: FY27 revenue guide against $53,029M; 12/31/26 schedule in the 10-K against Street 2027 equipment of $32,383M. Late April and late July 2027: H1 2027 equipment revenue against $14,424M. |

### Candidate 2. Power equipment revenue, FY2029 (gigawatts x order price)

| Field | Value |
|---|---|
| X | $19,256M (sum of four quarters, `Total Revenue|Power|Equipment`); equals $688/kW on 28 GW or $741/kW on 26 GW |
| Z | 26-28 GW x $790-875/kW = $20.5-24.5B; centre $22.6B |
| Gap | +7% to +27%; centre +17%. Floor case -2% |
| Y | The Street's line is 21.2-22.5 GW at 2026 order prices ($856-909/kW), about the 2027 output level, against a plan of 26-28 GW. Section 2.4: the price capitalises 2030 EBITDA at about 16x, so it carries this line. |
| Reveal | 2026-10-28 and late January 2027: Power equipment orders in dollars and gas GW ordered for Q3 and Q4 (pass if H2 2026 is at or above $838/kW on 20 GW or more). Late January 2027: change in margin in Power equipment backlog (management: larger than 2025's 11 points). Spring 2027 capital markets day: 2030 outlook with the equipment and services split (compare Street 2030 Power equipment $23,469M, services $22,357M). |

---

## 8. Checks that showed no gap

| Check | Result |
|---|---|
| Street Q3 2026 against management's quarter guide | Rebuild $11.8-12.1B revenue, about $1.62-1.70B EBITDA; Street $11,993M and $1,672M |
| Street FY26 EBITDA against the guide | $6,334M = 13.7% margin, upper half of 12-14%; Q4 needs 18.0% |
| Street H2 2026 orders against "$200B backlog very early in 2027" | 176.3 + 45.4 - 25.9 = about $196B at year-end; consistent |
| Power equipment 2027 and 2028 per kW | $552-662/kW, inside the FY24-FY25 order price range (section 6.2) |
| Power and Electrification H1 2027 against the normal seasonal step from H2 | Street -1.6% and -2.4%; reported steps -1.8% to -4.7% and -0.7% to -6.5% |
| Total Power revenue 2029-2030 | Equipment above and services below roughly cancel (section 6.4) |
| Free cash flow H2 2026 | Roll-forward: EBITDA 4.17B less cash costs and working capital other than deposits 5.4-7.2B, plus deposits 4.6-9.2B (slot reservations at "like, 25% down" on 20-28 GW at $850-1,000/kW; Electrification 0.8-2.0B) = $1.6-8.0B against Street $2.65B and a guide-implied $1.6-2.6B. Band wider than gap. |
| Free cash flow FY27 | Depends on gigawatts under contract after 2026; range spans the Street |
| Consensus mean against median and outliers | FY27 EBITDA mean 9,471, median 9,364, 9,552 without the low of 6,612. FY28 mean 12,553, median 12,862, 12,796 without the low of 4,786. Differences of 1-2.5% |
| Share count, interest income, tax | Each under 3% of EPS |
| Wind deliveries H1 2027 (reproduced, owned by `propose_wind.md`) | Street 1,882 MW. H1 2026 orders 1.2 GW x the 1.11-1.39 ratio of sales to orders one year earlier = 1.33-1.67 GW, -11% to -29%. Equipment revenue effect -$0.3-0.7B; EBITDA effect small. The same ratio puts H2 2026 above the Street (3.4-4.3 GW against 3.28). |

---

## 9. Limits

1. The peer fit is one outlier away from having no slope (section 3). Treat 21-25x as a range, not a point.
2. Candidate 1 has one miss in seven windows and overlapping windows; the Street's 0.957 ratio is inside the seven-window range. On total revenue the gap is +3% to +7%.
3. Candidate 2 rests on the all-in $/kW measure. It moves with mix: $701/kW in a heavy-duty quarter, $1,045/kW in an aeroderivative quarter. The dollar value of the 63 GW slot-reservation book is not disclosed.
4. The Street's 2029-2030 division lines come from fewer brokers than 2027-2028 (the Street's Power RPO line jumps $19B between Q4 2028 and Q1 2029). The annual totals for those years have 20-21 contributors and agree with the division sums within 1%; the equipment and services split is the less reliable part.
5. No 2029 figure is reported inside twelve months. The checks inside the horizon are order prices (two prints), the January backlog-margin page and the 2030 outlook at the capital markets day, whose date is not set.
6. Management's own 2028 framework ($56B revenue, Power at a high-teens growth rate) is consistent with the Street's 2028 equipment figure. The framework predates the H1 2026 orders.

## 10. Sources

| Data | Where |
|---|---|
| Bloomberg consensus, multiples, positioning | `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` (sheets Snapshot, Consensus, ConsensusHistory, Multiples, PricePositioning, Bulk); `data/bloomberg/GEV_Pull_2026-10-01/` (`segment_quarterly.json`, `01..05-eeo-company-specific.xlsx`, `06_modl.xlsx`, `18_ddm.png`). Bloomberg, 2026-10-01 |
| RPO schedule and division RPO | Note 9 and MD&A segment tables of each 10-Q and 10-K, accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148; 12/31/23 schedule from the S-1 (corpus document 385) |
| Gas and wind unit tables (GW ordered and sold) | Same filings, MD&A Power and Wind sections |
| Power equipment orders in dollars | Earnings decks: gevernova.com `gev_webcast_presentation_01282026.pdf` (appendix pages 18 and 22) and `gev_webcast_presentation_07222026.pdf` (corpus source 3157, page 15) |
| Output plan, order pricing, slot deposits ("like, 25% down"), timing of backlog margin | Q2 2026 call transcript (corpus source 3161); conference transcript 2026-09-16, gevernova.com `ge-vernova-morgan-stanley-laguna-conference-2026-transcript.pdf` |
| Cash-flow lines | 10-Q Q2 2026, 10-Q Q1 2026, 10-Q Q3 2025, 10-K 2025 statements of cash flows; deck free-cash-flow pages |
| Other lens files | `propose_rpo-equipment.md`, `propose_power-services.md`, `propose_fcf-deposits.md`, `propose_wind.md` in this folder; `09_finrobot_overnight/BLOOMBERG_VERDICT.md`, `S01_backlog_margin_conversion.md` |
