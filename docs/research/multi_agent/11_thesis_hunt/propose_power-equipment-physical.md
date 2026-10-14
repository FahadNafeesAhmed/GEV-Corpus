# Power equipment as a physical quantity: gigawatts x signed price vs the Street

_Research input only (tables, formulas, sources). No memo sentences, no forecast chosen for the team. Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Lens: turn Street Power equipment revenue into GW x $/kW and compare with what the signed backlog and the stated output path contain.

## 0. Result in one table

Power equipment revenue, $B. "Signed price" = equipment RPO dollars per GW of the order layers that ship in that year (section 3). "Conversion" = share of opening equipment RPO recognised by the time the opening backlog GW has shipped (back-test, section 4: 0.80-0.99, mean 0.90).

| Period | Street (Bloomberg, 2026-10-01) | Output flat at 20 GW/yr | July plan (20 GW 2027, 23 GW 2028) | September ladder (21.5 GW 2027, 25.5 GW 2028) | Verdict |
|---|---|---|---|---|---|
| H2 2026 | 5.49 | 4.3-4.8 | same | same | Street = company guide; layers under-predict. No gap claimed |
| FY2027 | 12.15 | 12.5-12.9 (+3% to +6%) | same as flat | 13.5-14.0 (+11% to +15%) | Inside the error band (-9% to +22%). No candidate |
| **FY2028** | **15.89** | 15.7-16.2 (-1% to +2%) | **18.5-19.1 (+17% to +20%)**; band 16.5-20.4 | **20.8-21.4 (+31% to +35%)**; band 18.4-22.8 | **Candidate.** Street equals the no-ramp case |
| FY2029 | 19.26 | 16.7 | 21.8 (26 GW) | 23.4 (28 GW) | +13% to +22% but rests on unconverted reservations; note only |
| FY2030 | 23.47 | - | 25.1 (30 GW) | 25.1 | +7%; inside error |

Rows use conversion 0.90-0.93; "band" uses 0.80-0.99. 2029-30 use $900/kW x 0.93.

GW that the Street's revenue buys at the signed price (conversion 0.93): **2027 18.8 GW, 2028 19.6 GW, 2029 22.5 GW, 2030 28.0 GW.** Management's stated path: 2027 20-21.5, 2028 23-25.5, 2030 30. So the Street path either holds output near 20 GW through 2028, or assumes a price about 20% below the signed one in 2028.

## 1. Inputs and where they come from

### 1a. Street (Bloomberg, 2026-10-01)
File `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, key `Total Revenue|Power|Equipment|YYYY Qn` (same as 01..05-eeo-company-specific.xlsx row "Power > Equipment"; annual sums tie to `street_segments_annual_2026-10-01.csv` column `power_equipment_rev`).

| $M | Q3 26 | Q4 26 | Q1 27 | Q2 27 | Q3 27 | Q4 27 | Q1 28 | Q2 28 | Q3 28 | Q4 28 |
|---|---|---|---|---|---|---|---|---|---|---|
| Power equipment | 2,394 | 3,097 | 2,585 | 2,798 | 3,025 | 3,743 | 3,445 | 3,654 | 4,000 | 4,790 |

| $M | H2 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| Power equipment | 5,491 | 12,151 | 15,888 | 19,256 | 23,469 |
| Power services | 7,661 | 15,675 | 17,665 | 19,711 | 22,357 |
| Power total | 13,160 | 28,121 | 33,521 | 39,522 | 45,215 |
| Gas line | 11,173 | 22,818 | 27,452 | 33,484 | 39,330 |
| Nuclear / Hydro lines | - | 3,486 / 1,021 | 3,697 / 1,098 | 4,388 / 1,198 | 5,352 / 1,237 |
| Power adj. EBITDA | - | 5,906 | 7,810 | 9,983 | 12,174 |

Bloomberg carries no consensus line for gas GW shipped or price per kW (only Wind MW delivered). Consensus history (workbook sheet `ConsensusHistory`): FY2028 revenue 59,196 (2026-07-10) -> 60,269 (07-24) -> 60,713 (09-04) -> 60,842 (09-25), i.e. +2.8% after Q2 and +0.2% after the September conference; FY2027 51,893 -> 52,949 (+2.0%).

### 1b. Company quarterly data (10-Q / 10-K MD&A "POWER" tables; accession numbers 0001996810-...)
24-000008, 24-000067, 24-000083, 25-000011 (10-K24), 25-000073, 25-000133, 25-000160, 26-000015 (10-K25), 26-000064, 26-000148. Q4 values are full year minus nine months.

| Quarter | GW sold | Units sold HD / of which HA / aero | Power equipment revenue $M | GW ordered | Units ordered HD / HA / aero | Power equipment RPO end $M | Equipment orders $M = change in RPO + revenue | Order $/kW |
|---|---|---|---|---|---|---|---|---|
| Q1 2024 | 2.3 | 10 / 1 / 7 | 1,201 | 4.9 | 16 / 8 / 18 | 14,394 | 1,959 | 400 |
| Q2 2024 | 1.4 | 8 / 1 / 7 | 1,285 | 4.1 | 14 / 4 / 1 | 10,978 | 1,769 (after adding back the $3.9B EDF sale) | 431 |
| Q3 2024 | 3.3 | 13 / 5 / 5 | 1,426 | 5.1 | 14 / 9 / 15 | 11,392 | 1,840 | 361 |
| Q4 2024 | 4.8 | 17 / 8 / 8 | 1,796 | 6.1 | 24 / 4 / 10 | 12,461 | 2,865 | 470 |
| Q1 2025 | 3.0 | 12 / 5 / 7 | 1,491 | 7.1 | 29 / 8 / 9 | 13,920 | 2,950 | 415 |
| Q2 2025 | 5.2 | 18 / 8 / 3 | 1,504 | 5.1 | 20 / 7 / 27 | 16,133 | 3,717 | 729 |
| Q3 2025 | 4.0 | 14 / 6 / 6 | 1,744 | 7.4 | 20 / 13 / 9 | 18,977 | 4,588 | 620 |
| Q4 2025 | 3.1 | 10 / 5 / 11 | 1,946 | 10.2 | 41 / 15 / 18 | 24,707 | 7,676 | 753 |
| Q1 2026 | 4.2 | 15 / 5 / 10 | 1,885 | 8.0 | 28 / 12 / 9 | 28,530 | 5,708 | 714 |
| Q2 2026 | 3.3 | 13 / 3 / 16 | 1,965 | 12.1 | 52 / 15 / 61 | 39,261 | 12,696 | 1,049 |

Checks on the derived order dollars:
- Reported Power orders (releases): Q3 2025 $7.8B, Q4 2025 $11.7B (FY $32.8B less nine months), Q1 2026 $10.0B, Q2 2026 $16.7B. Less the derived equipment orders leaves services orders of $3.2B / $4.0B / $4.3B / $4.0B, in line with services revenue of $3.1-3.8B a quarter.
- Management, Q2 2026 call (corpus source 3161): "first half 2026 orders were priced more than 20% above 4Q 25 equipment orders". Derived: H1 2026 $18,404M / 20.1 GW = $915/kW vs Q4 2025 $753/kW = +22%.
- BNP Paribas estimate for Q2 2026 orders (Utility Dive, 2026-07-22, corpus source 301): about $790/kW heavy-duty, $950/kW HA combined-cycle scope, $1,800/kW aeroderivative. With 61 aero (~2.3 GW), 15 HA (~6.8 GW) and 37 other heavy-duty (~3 GW) that gives about $13.0B, against the derived $12.7B.
- Yearly: 2024 $8,433M / 20.2 GW = $417/kW; 2025 $18,931M / 29.8 GW = $635/kW; H1 2026 $915/kW. Realised revenue per GW sold: 2023 $406, 2024 $484, 2025 $437, H1 2026 $513.
- Firm backlog GW roll (20.9 GW at YE22 + orders - sales) gives 29.1 / 32.5 / 39.6 / 43.5 / 52.3 GW for Q2 2025 to Q2 2026 against disclosed 29 / 33 / 40 / 44 / 53. HA units in RPO roll (29 at 3/31/24 + orders - sales) gives 32 and 36 at the next two quarter ends (disclosed 32, 36), 51 at YE25 (10-K: 51) and 70 at 6/30/26.

### 1c. Output path as stated
- Q2 2026 release (0001996810-26-000147): "on track to deliver 20 GW of annual gas turbine output in the third quarter of 2026, with 24 GW in 2028, and we are implementing actions to produce 30 GW in 2030."
- Q2 2026 call: "about three gigawatts of output a quarter to five gigawatts of output a quarter, starting in the third quarter"; "we are going to ship over the next six quarters at least 30 gigawatts".
- Morgan Stanley Laguna conference, 2026-09-16 (gevernova.com transcript PDF; also stockanalysis.com and earningscalls.dev copies): 5 GW a quarter in Q3 and Q4 2026, "the beginning of next year will feel generally very similar", "sometime in the second half of next year to the next ladder step, to six gigawatts a quarter", "into 2028, we may be at six gigawatts for a period of time, and then ... seven gigawatts a quarter".
- Same transcript: the 2026 change in margin in backlog tells you 2029 and 2030 "because that is most of when that equipment delivers". FY2027 outlook comes on the January 2027 call; capital markets day (2030 outlook) in spring 2027.
- Paths used: flat = 5 GW/qtr; July plan = 2027 20 GW, 2028 23 GW (5.5, 5.5, 6, 6); September ladder = 2027 21.5 GW (5, 5, 5.5, 6), 2028 25.5 GW (6, 6, 6.5, 7).

### 1d. Non-gas equipment inside Power (sizing)
- FY25 Power revenue: Gas $16,006M, Nuclear $1,018M, Hydro $806M, Steam $1,937M; equipment $6,686M, services $13,081M (10-K25 p.26). From 2026 Steam is folded into Nuclear (H1 2026: Gas $8,493M, Nuclear $1,575M, Hydro $382M).
- Not disclosed: equipment/services by sub-business. Estimate: non-gas services about $2.6B (steam ~80% services, nuclear ~75%, hydro ~30%), so gas services about $10.5B and gas equipment about $5.5B (34% of Gas Power; management said "70% of the business is services" in 2024). Non-gas equipment revenue about $1.2B a year (range $0.9-1.6B).
- Non-gas equipment RPO is not disclosed. YE24: $12,461M of RPO against 25 GW of gas backlog at roughly $380-420/kW implies $2-3B non-gas. MD&A: 2025 increases in Hydro and Nuclear equipment; H1 2026 increase "primarily at Gas Power". Working estimate at 6/30/26: $3-4B of the $39.3B (8-10%). This is the main reason conversion is below 1.0 (section 4).
- Revenue recognition: customised equipment is recognised over time on cost-to-cost, standard equipment at the point of delivery (10-K25 Note 2). The filing does not say which applies to gas turbines; the "sales in units / GW" table tracks delivery. Over-time recognition would pull revenue earlier than shipment, not later.

## 2. Street path as GW x $/kW

Street Power equipment revenue divided by GW on each path, $/kW (includes non-gas equipment):

| Path | H2 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| Flat 20 GW | 549 | 608 | 794 | - | - |
| July plan | 549 | 608 | 691 | 741 (26 GW) | 782 (30 GW) |
| September ladder | 549 | 565 | 623 | 688 (28 GW) | 782 (30 GW) |

Against: realised $513/kW in H1 2026; firm backlog average $741/kW at 6/30/26 ($39,261M / 53 GW; was $556 a year earlier); orders booked Q4 2025 to Q2 2026 at $753 / $714 / $1,049; management guides H2 2026 orders to "the higher end of 10 to 20 points versus 4Q 25", about $890-905/kW.

## 3. What the signed backlog contains: vintage layers at 30 June 2026

Layer dollars = equipment orders of that quarter (section 1b). Oldest layer set so that the layers sum to reported RPO (it carries the old non-gas book).

| Layer (order date) | GW | $M | $/kW | Cumulative GW | Cumulative $M |
|---|---|---|---|---|---|
| Before 2025 | 3.1 | 1,926 | 621 | 3.1 | 1,926 |
| Q1 2025 | 7.1 | 2,950 | 415 | 10.2 | 4,876 |
| Q2 2025 | 5.1 | 3,717 | 729 | 15.3 | 8,593 |
| Q3 2025 | 7.4 | 4,588 | 620 | 22.7 | 13,181 |
| Q4 2025 | 10.2 | 7,676 | 753 | 32.9 | 20,857 |
| Q1 2026 | 8.0 | 5,708 | 714 | 40.9 | 26,565 |
| Q2 2026 | 12.1 | 12,696 | 1,049 | 53.0 | 39,261 |
| Reservations still to convert | 63 | not disclosed; about $900/kW assumed | | | |

Slot arithmetic:
- Orders dated before 2026 still in backlog: 32.9 GW. Shipments planned for H2 2026 + 2027: 30-31.5 GW. So at most 1.4-2.9 GW of pre-2026 orders are left for 2028; the rest of 2028 output (17-24 GW) has to be units ordered in H1 2026 or later, whatever the delivery order.
- 2028 output on the July plan = backlog positions 30-53: 2.8 GW @ $753 + 8.0 GW @ $714 + 12.1 GW @ $1,049 = $20,586M for 23 GW = $895/kW.
- Judge-checkable residual: $39,261M - Street H2 2026 $5,491M - Street 2027 $12,151M = $21,619M of signed backlog left at end-2027, against 23 GW of firm backlog left (53 - 10 - 20). Street 2028 = $15,888M.
- Delivery order matters little for the 2.5-year sum: layers after Q1 2025 are all $620-1,049/kW and reservations are priced above Q4 2025 orders, so any re-ordering swaps like for like.

## 4. Back-tests (error band)

### 4a. Conversion over one backlog cycle
Take a date, the firm GW backlog and the equipment RPO at that date (less the $3.9B EDF item before Q2 2024), then add up Power equipment revenue until cumulative GW sold equals that opening backlog.

| Start | Backlog GW | RPO $M | Quarters to ship it | Revenue in that span $M | Ratio |
|---|---|---|---|---|---|
| YE22 | 20.9 | 9,679 | 7.0 | 9,547 | 0.99 |
| Q2 2023 | 19.4 | 10,080 | 5.9 | 8,867 | 0.88 |
| YE23 | 16.7 | 9,736 | 5.4 | 7,749 | 0.80 |
| Q2 2024 | 22.0 | 10,978 | 5.5 | 9,028 | 0.82 |
| YE24 | 25.1 | 12,461 | 6.5 | 11,636 (last half-quarter is Street) | 0.93 |
| Q2 2025 | 29.1 | 16,133 | 6.9 | 15,357 (last three quarters are Street) | 0.95 |

Mean 0.90, range 0.80-0.99. The shortfall is the long-dated non-gas book ($1-3B) less new short-cycle revenue. In dollars it has been $0.1-2.0B; if it stays a fixed amount rather than a fixed share, conversion on a $39B book is 0.95-0.99.

### 4b. Next-four-quarter test of first-in-first-out layers (actual GW, layer prices)
Actual / predicted: YE24 0.81, Q1 2025 0.85, Q2 2025 0.90; six quarters from YE24 0.93; YE25 to H1 2026 0.82. The oldest layer always holds the non-gas book and FIFO "ships" it first, so the method over-predicts short windows by 10-19% ($0.85-1.6B). **Consequence: no call on a four-quarter window from this lens.**

### 4c. Unit-class cross-check
Regression of quarterly Power equipment revenue on units sold, Q1 2023 to Q2 2026 (n=14, R2 0.92): constant $833M, HA $87M a unit, aero $69M a unit, other heavy-duty not significant. A split model (aero at $68M a unit and 16 a quarter; non-gas $0.35B a quarter; heavy-duty FIFO on layers net of aero and non-gas) gives H2 2026 $5.25B (Street/guide $5.49B), 2027 $14.5B flat / $15.4B ladder, 2028 $18.1B flat / $20.7B July plan / $23.0B ladder. Its own annual back-test error is large (actual / predicted 0.81, 0.97, 1.30, 0.98 for 2023, 2024, 2025, H1 2026), so it is a cross-check on direction, not a number.

## 5. Scenario table for FY2028 (the candidate)

FY2028 Power equipment revenue = (dollars of the backlog positions shipped in 2028) x conversion. Street $15,888M.

| Path (2028 GW) | Positions shipped in 2028 | Layer $M | x0.80 | x0.90 | x0.93 | x0.99 |
|---|---|---|---|---|---|---|
| Flat (20) | 30-50 | 17,439 | 13,951 (-12%) | 15,695 (-1%) | 16,218 (+2%) | 17,264 (+9%) |
| July plan (23) | 30-53 | 20,586 | 16,469 (+4%) | 18,528 (+17%) | 19,145 (+20%) | 20,381 (+28%) |
| September ladder (25.5) | 31.5-57 | 23,058 | 18,446 (+16%) | 20,752 (+31%) | 21,444 (+35%) | 22,827 (+44%) |

- Mid case used in the summary: 24 GW (positions 30.5-54.5, $21,559M) x 0.915 = $19.7B, +24%.
- Cumulative H2 2026 to 2028: Street $33,530M. Flat $32.5-33.6B (-3% to 0%); July plan $35.3-36.5B (+5% to +9%); ladder $38.6-39.9B (+15% to +19%).
- Total Power 2028 on the mid case and Street services: $17.7B + $19.7B = $37.4B vs Street $33.5B (+11%); company revenue about $64.8B vs $61.0B (+6%).
- GEV January framework (Q4 2025 release): Power "high-teens organic revenue growth CAGR" by 2028. From FY25 $19.77B at 17-19% that is $31.7-33.3B. The Street's $33.5B sits on it. The framework was set when Power equipment RPO was $24.7B; it is $39.3B six months later.

Profit and price arithmetic (ranges, not a forecast):
- Extra 2028 revenue on the July plan $2.6-3.3B, on the ladder $4.9-5.6B.
- At the Street's own 2028 Power margin (23.3%): +$0.6-0.8B, or +$1.1-1.3B on the ladder. At 15%: +$0.4-0.5B / +$0.7-0.8B.
- Against Street 2028 adj. EBITDA $12,553M: +3% to +6% (July plan), +6% to +10% (ladder).
- Per share at 25x: $1B of EBITDA = $94 a share (25 x 1,000 / 266.33).

## 6. Company schedule cross-check (10-Q Q2 2026, RPO note)

Equipment RPO $87,821M; 36% / 65% / 97% within 1 / 2 / 5 years = $31,616M / $57,084M / $85,186M; year two alone $25,468M. Segment equipment RPO: Power $39,261M, Electrification $40,589M, Wind $8,197M.

| $M | Year 1 (Q3 2026 to Q2 2027) | Year 2 (Q3 2027 to Q2 2028) |
|---|---|---|
| Company scheduled from backlog | 31,616 | 25,468 |
| Power layers, flat 5 GW/qtr (before conversion haircut) | 11,506 | 14,417 |
| Power layers, September ladder | 11,506 | 17,786 |
| Left for Electrification + Wind, flat | 20,110 | 11,051 |
| Left for Electrification + Wind, ladder | 20,110 | 7,682 |
| Street: Power / Electrification + Wind equipment revenue | 10,874 / 19,371 | 13,867 / 21,270 |

- The July 10-Q schedule fits Power at about 5 GW a quarter through mid-2028. It does not fit the September ladder (it would leave Electrification + Wind only $7.7B from backlog in year two). The ladder is therefore not yet in the filed schedule; the Q3 2026 10-Q (2026-10-28) is the first filing that can show it (watch the within-2-years percentage and dollars).
- Year one: physical range for Power is $10.5-12.3B (layers less the non-gas book, up to the unit-class split) against Street $10.87B. Power can explain between none and all of the known $1.4B company-level gap ($31.6B scheduled vs $30.2B Street); this lens cannot place it.

## 7. Checked, no usable gap

| Item | Street | Arithmetic | Why not a candidate |
|---|---|---|---|
| H2 2026 Power equipment | $5.49B | Layers $4.3-4.8B; unit split $5.25B | Street equals the company guide (FY Power +18-20%, Q3 +17-19%) |
| Q3 2026 to Q2 2027 | $10.87B | $10.5-12.3B | Four-quarter back-test error 10-19% |
| FY2027 | $12.15B | Flat $12.5-12.9B; ladder $13.5-14.0B | Band -9% to +22%; gap only exists with the H2 2027 step to 6 GW a quarter |
| Q1 2027 shape | $2,585M, 17% below Street Q4 2026 | Output is level at 5 GW; Q1 dip vs prior Q4 was -39%, -17%, -3% in 2024-26 | Quarterly revenue per GW has ranged $289-918; too noisy |
| FY2029 | $19.26B = 22.5 GW at $837 | 26-28 GW x $900 x 0.93 = $21.8-23.4B | Price of unconverted reservations not disclosed |
| FY2030 | $23.47B = 28 GW | 30 GW = $25.1B | +7%, inside error |
| H2 2026 Power orders | $27.2B | at least 20 GW x $890 + services $8.3B + non-gas = at least $26.6B | In line |
| Non-gas equipment | - | about $1.2B a year, RPO about $3-4B | Too small to make or break any year |

## 8. Weak points (for the red team)

1. The FY2028 gap needs output of at least 22-23 GW in 2028. With output flat at 20 GW the Street is right. Q2 2026 shipped 3.3 GW and Power revenue missed consensus ($5.48B vs $5.6B).
2. Conversion has ranged 0.80-0.99. At 0.80 the July-plan gap falls to +4%.
3. The delivery year of each order is inferred (FIFO and slot counting), not disclosed. Management's wording puts 2026 orders "mostly" in 2029-30.
4. The Street's GW are not observable. The same revenue could be plan GW at a price 20% below the signed one.
5. FY2028 is reported in early 2029. Inside twelve months there are only proxies (section 9).
6. Profit effect is +3% to +10% of 2028 EBITDA, and the Street's Power margin may already include the price in these orders.
7. Bloomberg's equipment / services split may rest on fewer brokers than the headline; the Power total ($33.5B) carries the same conclusion (+11% on the mid case).
8. A new CFO starts 2027-01-01 (8-K 0001996810-26-000153); the first outlook under a new CFO may be set low.

## 9. Company-reported checkpoints

| Date | Number | Level that supports / contradicts |
|---|---|---|
| 2026-10-28 (Q3 2026 10-Q and release) | Gas GW sold in Q3 | 4.8 GW or more supports; 4 GW or less contradicts the ramp |
| same | Power equipment RPO / firm backlog GW | $780/kW or more supports (was $741) |
| same | Equipment RPO within 2 years | A rise in the dollar amount beyond what new orders explain = ladder now in the schedule |
| Late January 2027 (Q4 2026 call, FY27 outlook) | 2027 gas output; FY27 Power organic growth | 21 GW or more, or growth guide midpoint of 21% or more, supports (Street implies +19%) |
| Spring 2027 (capital markets day) | 2028 output and Power revenue path | 2028 output of 24 GW or more restated, or implied 2028 Power revenue of $36B or more (Street $33.5B) |
| February 2029 (10-K 2028) | FY2028 Power equipment revenue | $18.0B or more |

## 10. Reproduce

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
EQ = 'Total Revenue|Power|Equipment'
street = {y: sum(d[f'{EQ}|{y} Q{q}'] for q in range(1, 5)) for y in (2027, 2028, 2029, 2030)}
h2_26 = d[EQ + '|2026 Q3'] + d[EQ + '|2026 Q4']
RPO = 39261   # Power equipment RPO 6/30/26, 10-Q p.29
# (GW ordered, equipment orders $M = change in Power equipment RPO + Power equipment revenue)
layers = [(7.1, 13920-12461+1491), (5.1, 16133-13920+1504), (7.4, 18977-16133+1744),
          (10.2, 24707-18977+1946), (8.0, 28530-24707+1885), (12.1, 39261-28530+1965)]
layers = [(53 - sum(g for g, _ in layers), RPO - sum(u for _, u in layers))] + layers
def cum(gw, p_res=900.0):            # dollars in the first `gw` GW of backlog, oldest first
    c = g = 0.0
    for a, b in layers:
        if g + a >= gw: return c + (gw - g) * b / a
        c += b; g += a
    return c + (gw - g) * p_res      # beyond 53 GW: converted reservations
for name, (a, b, c) in {'flat': (10, 20, 20), 'july': (10, 20, 23), 'ladder': (10, 21.5, 25.5)}.items():
    for k in (0.80, 0.90, 0.93, 0.99):
        fy28 = (cum(a + b + c) - cum(a + b)) * k
        print(name, k, round(fy28), f'{fy28 / street[2028] - 1:+.0%}')
```
Corpus queries: `SELECT accession, filing_date, text FROM chunks WHERE ticker='GEV' AND form IN ('10-Q','10-K') AND text LIKE '%Gas Turbine Gigawatts%'` (unit and GW tables, RPO, segment revenue); source id 3161 (Q2 2026 call), 681 and the gevernova.com PDF (Laguna), 301 (BNP price estimate).
