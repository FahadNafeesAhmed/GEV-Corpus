# Gigawatt angle: ruling, and how it can still be used

_AI-assisted research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast is chosen for the team (ranges and methods only). Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Working date 2026-10-01. Money in $M unless stated.

The angle: turn the Street's Power equipment revenue into a physical quantity (gigawatts shipped x revenue per kW). Then compare it with what GE Vernova has signed and says it will ship.

This file is the judge's ruling on three rebuilds of that angle. It also holds the exhibit the team can use.

Words used here.
- **Street**: Bloomberg consensus mean. The line is `Total Revenue|Power|Equipment`. It has the same definition as the "Equipment" revenue line in the 10-Q Power table.
- **Firm backlog**: gas turbines on firm order (53 GW at 6/30/26). It sits inside Power equipment RPO ($39,261M).
- **RPO**: remaining performance obligations. Signed orders not yet booked as revenue.
- **Reservation**: slot reservation agreement. A paid place in the factory queue. Not yet an order and not in RPO (63 GW at 6/30/26).
- **All-in $/kW**: Power equipment order dollars divided by gas GW ordered. The dollars include aeroderivative units, steam turbines and generators, and non-gas equipment.
- **Price in backlog**: Power equipment RPO divided by firm GW. Also all-in.
- **Conversion (k)**: reported revenue divided by the order dollars of the GW shipped. Back-tested at 0.79 to 0.99 over four quarters and 0.85 to 0.98 over eight quarters or more.
- **HA**: the largest gas turbine class (about 430 MW a unit). **Aero**: aeroderivative units (about 30 to 115 MW).

## 0. Ruling

**No version holds as a thesis.**

Standard applied: one number against the Street, on one line and one period; a gap larger than its back-tested error; revealed by a company-reported number inside 12 months. All three parts must pass.

| Rebuild | Line and period | Street (Bloomberg, 2026-10-01) | Gap as stated | Gap after the two checks | Error band after the checks | Gap larger than error? | Company-reported number inside 12 months? | Holds? |
|---|---|---|---|---|---|---|---|---|
| `gw-contracted-book` | Power equipment revenue, cumulative Q3 2026 to Q4 2030 | $76,256M | +7.0% | about +1% to +3.8% | +/-10% to +/-12% | No | No. Prints February 2031 | No |
| `gw-unit-class` | Power equipment revenue, six months to 30 June 2027 | $5,383M | +28% | about +14% (range +6% to +28%) and about +17% (range +3% to +28%) | +/-22% to +/-23% | No | Yes in form. Q2 2027 10-Q, late July 2027 | No |
| `gw-guide-predictor` | Company 2030 EBITDA as set in the spring 2027 outlook | $19,544M | +4.6% | +1.3% to +2.2% | +/-12% to +/-15% | No | No. An outlook is guidance, not a reported result | No |

The rebuilds' own authors ruled "does not hold" on the first and third. The second claimed to hold. Both of its checkers reproduced its arithmetic and both ruled it out.

### Why the closest one (`gw-unit-class`, H1 2027) fails

The judge re-ran the rebuild's model from its printed code. Results, July output plan:

| Version of the same model | Back-test: worst half-year miss / root-mean-square | H2 2026 vs Street | H1 2027 vs Street | H1 2027 if H2 2026 lands on the guide-anchored Street |
|---|---|---|---|---|
| As built (one price index per order quarter, oldest first) | 19.9% / 9.9% | +2% | +28% | +25% |
| 2025 orders given one common price (dollars unchanged) | 18.8% / 9.6% | +13% | +22% | +9% |
| No vintage prices at all (one fixed value per unit class) | 15.3% / 9.0% | -21% | -17% | +5% (step only) |
| As built, 2025-and-later prices 20% lower | 19.7% / 10.2% | -12% | +6% | |
| As built, output 20% short of 5 GW a quarter | 19.8% / 10.7% | -15% | +6% | |

Reading:
1. The back-test cannot tell the three versions apart. All fit past revenue about equally well. The version with no vintage prices fits half-years slightly better.
2. So the back-tested error (about +/-17% to +/-20%) measures "units x a steady value per unit". It does not measure the price step that makes the gap. No unit ordered in 2025 or later has shipped yet.
3. The +28% needs units to ship in strict order-quarter sequence inside 2025. The Q1 2025 layer is cheap (index 321). The Q2 and Q3 2025 layers are dear (index 482 and 478). Management said the Q2 and Q3 2025 dollars per GW were moved by aero mix, small turbines, combined-cycle scope and non-gas orders (Q3 2025 call).
4. With 2025 treated as one vintage the model sits 13% above the guided half. Then either the guide is low, or the model's level is high and the H1 2027 gap is about +9%.
5. The Street line is thin for this period. No broker count is shown. In H1 2027 the Street's equipment plus services is $269M below its own Power total. That is 5% of the equipment line.
6. The reveal passes only in form. The FY2027 guide comes in late January 2027 and resets the Street before any 2027 quarter is reported. The model needs Power growth of +27% to +40% in 2027. The company framework and the Street are at about +19%.

What stands from this rebuild: the sign. Every variant run by the rebuild, the two checkers and the judge gives H1 2027 above the Street (+3% to +39%), except stress cases that also put H2 2026 well below the company guide. The size is not established.

## 1. The six kill reasons after three rebuilds

| # | Kill reason of the first version | `gw-contracted-book` | `gw-unit-class` | `gw-guide-predictor` |
|---|---|---|---|---|
| 1 | Rival explanation: the Street equals the company plan at signed prices x 0.90 | Stands in every window. Street to end-2028 = firm RPO x 0.854. Street to end-2030 = firm backlog + 56 GW of reservations at $725 to $812/kW | Not answered. Street H1 2027 = the guided H2 2026 run-rate held flat ($538 against $549/kW at 10 GW). Street FY2027 Power growth = the company's high-teens framework | Conceded. Street 2030 = 30 GW x $782/kW = 1.06 x today's price in backlog |
| 2 | The gap sat in one order layer (Q2 2026, lifted by mix) | Diluted, not removed. That layer is still about half of the centre gap to end-2030 | Moved one year earlier. 67% of the gas value shipped in H1 2027 comes from the Q2 and Q3 2025 layers | Timing no longer matters. Price still does, and unbooked H2 2026 orders are added |
| 3 | Error band (four-quarter misses of -27% to +25%) | Not cleared. +/-10% to +/-12% against +1% to +4% | Not cleared. +/-22% to +/-23% against +14% to +17%. The back-test does not cover the price step | Not cleared. Two outlooks only. +/-12% to +/-15% against +1% to +2% |
| 4 | Reveal date outside 12 months | Worse. February 2029 to July 2031 | Answered in form. Late April and late July 2027 | In form only. Two outlooks, not results. Second date not set |
| 5 | Thin Street data on the division line | Worse in long windows. 21 and 20 annual estimates for 2029-30. One model in 2031 | Not fixed. No broker count. One model behind the flat 18% Power growth in 2027 | Not fixed. 20 estimates for 2030 with an 11% standard deviation. No history |
| 6 | Small profit effect | 1% to 3% of cumulative EBITDA. Zero inside 12 months | +3% to +8% of H1 2027 EBITDA at the corrected gap | About +1% to +2% of 2030 EBITDA. Range has both signs |

## 2. How the angle can be used (plain statement)

| Use | Verdict | Condition |
|---|---|---|
| As the thesis | **No** | No version has a gap larger than its error |
| As an exhibit of what consensus assumes in physical terms | **Yes. This is the main use** | Section 3. Carry the labels in section 3e |
| As the driver structure of the Power equipment line in the model | **Yes** | Section 4. Use ranges. One conversion value for all windows |
| As supporting evidence for a direction | **Yes, narrowly** | Only the facts in section 5. They support the sign (long), not a size |

What the numbers support:
- The Street's Power equipment path equals the company's stated output at prices already signed. It assumes no ramp failure and no price above the signed book.
- Every Street dollar of Power equipment revenue to end-2030 is covered by firm orders plus reservations (108% to 126%). What is left to deliver it is output and conversion, not new demand.
- HA units that ship from mid-2026 were almost all ordered in 2025 or later (62 to 70 of 70).

What the numbers do not support:
- "The Street's Power equipment revenue is X% too low" for any period.
- "The Street assumes output stays at 20 GW." It does not need to. Plan output at Q4 2025 to Q1 2026 prices gives the same number.
- Any claim that the January 2027 guide or the spring 2027 outlook will beat the Street by a stated amount.

## 3. Exhibit: what the Street assumes in gigawatts and price per kW

All inputs were re-read by the judge from the primary files (section 9).

### 3a. Street Power equipment revenue as GW x $/kW

| Period | Street Power equipment revenue, $M | Output on the company's stated path, GW | Street $ per kW at that output | Order price this implies at 0.90 conversion, $/kW | GW the Street buys at today's price in backlog ($741/kW) | Nearest signed or stated price |
|---|---|---|---|---|---|---|
| H2 2026 | 5,491 | 10 (5 a quarter) | 549 | 610 | 7.4 | Realised in the last four quarters: $516. This half is guide-anchored |
| 2027 | 12,151 | 20 to 21.5 | 608 to 565 | 675 to 628 | 16.4 | FY2025 orders: $612 (deck) to $635 (derived) |
| 2028 | 15,888 | 23 / 24 / 25.5 | 691 / 662 / 623 | 768 / 736 / 692 | 21.4 | Q4 2025 and Q1 2026 orders: $705 to $753 |
| 2029 | 19,256 | 26 to 28 (not stated; between the 2028 and 2030 rates) | 741 to 688 | 823 to 764 | 26.0 | Price in backlog at 6/30/26: $741 |
| 2030 | 23,469 | 30 | 782 | 869 | 31.7 | H2 2026 order guide: $838 to $904. One broker: about $900 |
| H1 2031 | 12,340 | 15 (30 a year) | 823 | 914 | 16.7 | Rests on about one model |
| Q3 2026 to Q4 2028 | 33,530 | 53 | 633 | 703 | | Firm backlog is 53 GW at $741 |
| Q3 2026 to Q4 2030 | 76,256 | 109 | 700 | 777 | | |

Sources. Street: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json` (Bloomberg, 2026-10-01). Output path: Q2 2026 release and call ("20 GW of annual gas turbine output in the third quarter of 2026, with 24 GW in 2028", actions toward 30 GW in 2030; "24 gigawatts annualized"); conference transcript of 2026-09-16 on gevernova.com (5 GW a quarter in Q3 and Q4 2026, start of 2027 "very similar", 6 GW a quarter some time in H2 2027, then 6 and 7 GW a quarter in 2028). Price in backlog: $39,261M (10-Q Q2 2026, accession 0001996810-26-000148) / 53 GW (Q2 2026 release, 0001996810-26-000147).

Notes on the output column.
- 2027: 20 GW is 5 a quarter all year. 21.5 GW has a step to 5.5 and then 6 GW in the second half.
- 2028: 23 GW is a quarterly path of 5.5, 5.5, 6, 6. 24 GW is the stated annualised rate. 25.5 GW is 6, 6, 6.5, 7 from the September statement. The company has not given a calendar-year delivery total for 2028.
- 2029: no company statement.
- The Street publishes no gas GW line. The GW are the company's, not the Street's.

Three ordinary readings that reproduce the Street with no gap:
- 2028: 24 GW x $735/kW x 0.90 = $15,876M (Street $15,888M).
- 2030: 30 GW x $871/kW x 0.90 = $23,517M (Street $23,469M). $871 is the middle of the H2 2026 order guide.
- 2028 against the company framework: (19,767 x 1.18^3 - 13,081 x 1.08^3) / 24 GW = $667/kW, against the Street's $662. This uses 18% Power growth and 8% services growth as assumptions.

### 3b. Reference prices

| Measure | Values, $/kW | Source |
|---|---|---|
| Revenue per kW sold (reported Power equipment revenue / gas GW sold) | 2023: 406. 2024: 480. 2025: 437. H1 2026: 513. Last four quarters: 516 | 10-K 2024 and 2025; 10-Q Q1 and Q2 2026 |
| Price in backlog (Power equipment RPO / firm GW) | 3/31/25: 480. 6/30/25: 556. 9/30/25: 575. 12/31/25: 618. 3/31/26: 648. 6/30/26: 741 | 10-Q / 10-K Power tables; earnings releases |
| All-in order price, derived (change in Power equipment RPO + equipment revenue, over GW ordered) | FY2024: 417. Q1 2025: 415. Q2 2025: 729. Q3 2025: 620. Q4 2025: 753. FY2025: 635. Q1 2026: 705. Q2 2026: 1,049. H1 2026: 911 to 916 | same filings |
| All-in order price, company deck order dollars | Q1 2025: 400. Q2 2025: 690. Q3 2025: 601. Q4 2025: 729. FY2025: 612. Q1 2026: 693. Q2 2026: 1,045. H1 2026: 909 | Q2 2026 deck p.15 (corpus source 3157), re-read by the judge. January 2026 deck p.18 (gevernova.com), re-read by two checkers |
| Company guide for H2 2026 gas equipment orders | "higher end of the range of 10 to 20 points versus 4Q'25 orders" = 838 to 904 | Q2 2026 call (corpus source 3161) |
| Company on reservations | 10 to 20 points above the backlog. As worded on $618: 680 to 742 | Q4 2025 call (corpus source 2660) |
| Price in backlog at 12/31/26 (estimate; needs H2 orders not yet booked) | 799 to 829 | `gw-guide-predictor.md`, section 6 |

Management's own caution on these prices: the Q2 2026 price was lifted by "a higher mix of aeroderivatives versus heavy-duty gas turbines and incremental combined cycle equipment" (Q2 2026 call). Q2 2026 orders included 61 aero units against 9 to 27 in earlier quarters.

### 3c. Published broker and third-party figures

| Who, when | Figure | Against the Street | Source |
|---|---|---|---|
| Morgan Stanley note, 2026-07-23 | 30 GW shipped in 2030 at about $900/kW = $27.0B | 15% above the Street's 2030 Power equipment line ($23,469M) | Press article "Morgan Stanley strongly resets GE Vernova stock target", copies dated 2026-07-25 (found by web search on 2026-10-01). The sentence is missing from the corpus copy (source 3886) |
| Same note | Reservations price near $3,000/kW of implied whole-plant cost | Whole plant, not turbine. Not comparable with the table above | corpus source 3886 |
| BNP Paribas note, 2026-07-22 | Q2 2026 orders: about $790/kW heavy-duty, $950/kW HA with combined-cycle scope, $1,800/kW aero | Class prices. An estimate, not company data | Utility Dive (corpus source 301) |
| Wood Mackenzie | Turbine price about $600/kW by end-2027 | Turbine only. Street 2027 is $565 to $608 all-in | Press release (corpus source 145) |
| Mizuho analyst, CNBC, 2026-07-02 | "There's not much upside to the revenue estimates through 2030" | The opposite view, in print | corpus source 1775 |
| GLJ Research Sell note, 2026-09-14 | 2027 turbine deliveries are 2024 orders; 2027 EBITDA $7.42B against consensus $9.45B | Below the Street | Press summaries, re-read by one checker (`gw-unit-class_check_outside.md`, section 4) |

### 3d. Coverage of the Street by the signed book

| Statement | Arithmetic | Qualifier that must go with it |
|---|---|---|
| Firm Power equipment RPO is 117% of Street revenue from Q3 2026 to Q4 2028 | 39,261 / 33,530 | About $3B to $4B of that RPO is non-gas (an estimate; not disclosed). Management places 2026 heavy-duty orders mostly in 2029-31. So not all of it can land by end-2028 |
| The Street to end-2028 equals the firm book x 0.854 | 33,530 / 39,261 | 0.854 is at the low edge of the back-tested range (0.85 to 0.98) |
| Firm RPO plus 63 GW of reservations is 108% / 113% / 120% / 126% of Street revenue from Q3 2026 to Q4 2030 | (39,261 + 63 x P) / 76,256 for P = $680 / $750 / $825 / $900 | The reservation price is not disclosed. The 10-K says reservations "may not result in orders". No lapse is visible so far |
| The Street to end-2030 equals the firm backlog plus 56 GW of reservations at $725 / $769 / $812 per kW | (76,256 / k - 39,261) / 56 for k = 0.955 / 0.926 / 0.90 | 109 GW shipped to end-2030 is the July plan. Published reservation prices run $680 to $900 |

### 3e. Labels the exhibit must carry

1. The Street figure is a Bloomberg division-line mean. The number of brokers behind it is not shown. One quarter out (Q3 2026) the low and high are -14% and +8% around the mean.
2. Out-years are thinner: 21 and 20 annual EBITDA estimates for 2029 and 2030 against 33 to 36 for 2026-28. Equipment plus services differs from the Power total by -$295M (2027), +$33M (2028), -$555M (2029), +$611M (2030).
3. The GW are the company's stated path, not a Street figure.
4. Every $/kW is all-in. It moves with aero mix, combined-cycle scope and non-gas equipment, with no change in like-for-like turbine price.
5. Revenue on customised equipment is recognised over time on cost incurred (10-K 2025). Revenue can lead shipment. "GW x price" is an approximation.
6. The exhibit shows what consensus assumes. It is not evidence that consensus is wrong.

## 4. Driver structure for the model's Power equipment line

Structure (the team sets the values):

`Power equipment revenue = non-gas equipment + [aero units x value per unit + HA units x value per unit + other heavy-duty GW x $/kW] x conversion`

Simpler form with the same back-test: `GW shipped x order price of the layer that ships x conversion`.

| Driver | Verified facts and ranges | Source |
|---|---|---|
| Output | 5 GW a quarter from Q3 2026; 6 some time in H2 2027; 6 then 7 in 2028; 30 GW in 2030. Last four quarters shipped 14.6 GW (4.0, 3.1, 4.2, 3.3). The plan needs a 37% step | Company statements above; 10-Q tables |
| Backlog by class at 6/30/26 | 70 HA units (about 30 GW). About 17.5 GW of other heavy-duty. About 136 to 160 aero units (5 to 6 GW). The HA count ties to five disclosed dates; the rest are estimates | `gw-unit-class.md` section 3; `gw-contracted-book.md` section 2 |
| Firm layers by order date (GW / $M) | Before 2025: 3.0 / 1,926. Q1 2025: 7.1 / 2,950. Q2 2025: 5.1 / 3,717. Q3 2025: 7.4 / 4,588. Q4 2025: 10.2 / 7,676. Q1 2026: 8.1 / 5,708. Q2 2026: 12.1 / 12,696. Total 53 / 39,261 | Derived from the 10-Q / 10-K Power tables |
| Reservations | 63 GW. Price range $680 to $900/kW | Section 3b |
| Conversion | Four quarters: 0.79 to 0.99, mean 0.906 (0.73 to 1.26 if one continuous stack). Eight quarters or more: 0.85 to 0.98, mean 0.926 (16 windows, one overlapping series). Use one value for all window lengths | Re-run by the judge; matches both checkers |
| Non-gas equipment | About $0.9B to $1.6B a year (estimate; the split is not disclosed) | `propose_power-equipment-physical.md` section 1d |
| Delivery year of each order | Not disclosed. Oldest-first is an assumption. The back-test cannot confirm it: shipping at the average backlog price fits as well | `gw-contracted-book_check_numbers.md` section 2c |

Sensitivities to end-2030 on the July plan: $50/kW on reservations = $2.7B. 0.01 of conversion = $0.85B. 1 GW of cumulative output = $0.8B. Half a GW a quarter of slippage = about -$7B.

Limits. Windows of four quarters or fewer are too noisy for a call (half-year revenue per kW has ranged $365 to $654 since 2023). The vintage price step has not yet been seen in reported revenue.

## 5. Supporting facts and their limits

| Fact | Status | Limit |
|---|---|---|
| 62 to 70 of the 70 HA units in RPO at 6/30/26 were ordered in 2025 or later (51 in RPO at end-2025; 43 ordered in 2025; 27 ordered and 8 sold in H1 2026) | Solid. From filings. Holds without assuming oldest-first | Dollars per HA by order quarter are not disclosed. Other heavy-duty and aero may still carry older orders |
| This contradicts the published Sell-note claim that 2027 turbine deliveries are 2024 orders, at least for HA units | Usable. Same point as the team's backlog-vintage work | It is a unit count. It does not size revenue or margin |
| Every method with no price step (fixed value per unit, unit regression, GW layers x 0.90) is 16% to 21% below the guide-implied H2 2026 Power equipment range ($5.2B to $6.1B) | Usable. Value per unit is already rising in the guided half | That step is already in the Street ($5,491M) |
| The Street holds revenue per kW about flat from H2 2026 ($549) to H1 2027 ($538), then steps to $677 in H2 2027 | Usable as an exhibit | The CEO said the start of 2027 will feel "very similar" to H2 2026. The Street matches that |
| H1 2027 is above the Street in every model variant (+3% to +39%) | Supports the sign only | Size not established: about +14% to +17% against +/-22% to +/-23% |
| Coverage: firm plus reservations is 108% to 126% of the Street to end-2030 | Usable with the qualifiers in 3d | Restates "sold out through 2030" in dollars. Already public |

## 6. Dated checks (company-reported; candidate marks only, the team sets its own)

Pull the Street again on the eve of each date. Compare like with like (annual with annual, quarterly with quarterly).

| Date | Company number | Street today (Bloomberg, 2026-10-01) | Reading that supports the upper end | Reading that supports the lower end | What it tests |
|---|---|---|---|---|---|
| 2026-10-28, Q3 2026 10-Q | Gas GW sold | none | 4.8 to 5.0 GW or more | 4.2 GW or less | Output ramp |
| same | HA and aero units sold | none | 6 or more HA; 14 or more aero | | First quarter that ships 2025-ordered HA units |
| same | Power equipment revenue | $2,394M (low 2,063, high 2,591). Company guide implies 2,226 to 2,478 | $2.6B or more on about 5 GW | $2.4B or less | Level of value per unit. A print near the Street confirms the Street |
| same | All-in order price = (change in Power equipment RPO + equipment revenue) / GW ordered | Power orders $12.2B (equipment and services together) | $838/kW or more | $753/kW or less | Whether reservations convert at the guided price |
| same | Power equipment RPO / firm GW | none | $775/kW or more | under $760 | Price in backlog |
| Late January 2027, Q4 call and 10-K | H2 2026 Power equipment revenue | $5,491M | $6.0B or more on about 10 GW | $5.0B or less with 10 GW shipped | Whether the higher-priced layers are converting |
| same | FY2027 Power organic growth guide | +19.1% | +25% or more | +20% or less | Whether management sees a price step in 2027 |
| same | Power equipment RPO and firm GW at 12/31/26 | Street's own H2 orders imply about $51.5B to $52.5B | $50.5B or more on 63 GW or more ($800/kW or more) | $48.8B or less | Order price. A result on the guide confirms the Street |
| same | 2027 gas output; 2026 change in backlog margin; HA units in RPO | none | 21 GW or more; more than 11 points | 20 GW or fewer | Output and price |
| Late April 2027, Q1 10-Q | Q1 2027 Power equipment revenue | $2,585M | $3.0B or more | $2.7B or less | First 2027 quarter |
| Spring 2027, capital markets day | 2030 outlook, with the equipment and services split | Power equipment $23,469M; company revenue $79,724M; EBITDA $19,544M | Equipment $25.5B or more; revenue $84B or more; EBITDA $20.5B or more | At or below the Street | An outlook, not a reported result. Date not yet set |
| Late July 2027, Q2 10-Q | Power equipment revenue, six months to 30 June 2027 | $5,383M | $6.2B or more | $5.6B or less | The `gw-unit-class` line |
| same | GW sold over Q3 2026 to Q2 2027 | none | 20 GW or more | 18 GW or fewer | Output |

Arithmetic behind the year-end marks: 39,261 + 20 GW x $838 - 5,491 = $50.5B. At $753: $48.8B.

## 7. What would change the ruling

1. A company statement of delivery year by order year, or equipment RPO by delivery year for Power.
2. A disclosed reservation price, or a heavy-duty-only order price.
3. Broker-level detail on the Power equipment line with 8 to 10 visible contributors.
4. Two reported quarters at about 5 GW with Power equipment revenue of $2.6B or more and 6 or more HA sold. That would be the first out-of-sample test of the vintage price step. The earliest date is late January 2027.

## 8. Corrections to carry when using the earlier files

1. Cite the Morgan Stanley "30 GW at roughly $900 per kilowatt" sentence to the press article, not to corpus source 3886.
2. The January 2026 statement compares reservations with the backlog, not with Q4 2025 orders. As worded it gives $680 to $742/kW, not $828 to $904.
3. The next capital markets day is "in the spring, before summer" (company transcript, 2026-09-16). A press article says "December analyst day". The transcript governs.
4. Q4 2025 release: 21 GW of new reservations and 3 GW of direct orders (not 22 and 2).
5. Q1 2026 GW ordered is 8.1 (10-Q), so the Q1 2026 order price is $705, not $714.
6. "24 GW in 2028" is an annualised rate. It is not a stated calendar-year delivery total.
7. In `gw-contracted-book.md`, use one conversion value for all windows (0.85 to 0.98). The step up to 0.955 for long windows is not supported.
8. In `gw-unit-class.md`, the stress table is run on the most favourable output path. On the 5 GW a quarter path one adverse input alone removes most of the gap.
9. In `gw-guide-predictor.md`, the centre is built from quarterly models (sum $80,718M) but compared with the annual mean ($79,724M). On one basis the gap is +1.3%.

## 9. Sources and reproduce

| Data | Where |
|---|---|
| Street by division and quarter | `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`; low and high for Q3 2026 in `06_modl.xlsx`; annual means and counts in `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx`, sheet Consensus. Bloomberg, 2026-10-01 |
| GW and units ordered and sold, Power equipment revenue and RPO | `data/gev.db` (read-only), 10-Q / 10-K Power tables, accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148 |
| Firm backlog and reservation GW | Earnings releases, 8-K exhibits 0001996810-25-000132, -25-000159, -26-000012, -26-000063, -26-000147 |
| Equipment RPO schedule (36% / 65% / 97% of $87,821M) | 10-Q Q2 2026, RPO note |
| Company statements | Corpus sources 3161 (Q2 2026 call), 3157 (Q2 2026 deck), 2660 (Q4 2025 call), 3796 (Q3 2025 call), 1844 (December 2025 update). Conference transcript of 2026-09-16: gevernova.com `ge-vernova-morgan-stanley-laguna-conference-2026-transcript.pdf` (read 2026-10-01) |
| Broker and third-party figures | Corpus sources 301, 3886, 145, 1775; web search of 2026-10-01 for the $900/kW sentence |
| Rebuilds and checks ruled on | `gw-contracted-book.md`, `gw-unit-class.md`, `gw-guide-predictor.md`, and each file's `_check_numbers.md` and `_check_outside.md` (this folder) |
| First version and its checks | `propose_power-equipment-physical.md`; `verify_power-equipment-fy28-fy29_reproduce.md`, `_already-known.md`, `_wedge-tests.md`; `propose_price-implied.md`; `propose_rpo-equipment.md` |

What the judge re-ran: all Street sums; the 2025-26 Power tables and the RPO note from the filings; the quotes in section 3; the layer back-test (4, 8, 10, 12, 14 quarters); the `gw-unit-class` model from its printed code, plus the variants in section 0. Not re-run: the 9,720-set grid, the January 2026 deck figures, and the press summaries of the Sell note. Those rest on the checkers.

Run from the `gev-corpus` folder. It prints table 3a and the coverage lines in 3d.

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))      # Bloomberg, 2026-10-01
EQ = 'Total Revenue|Power|Equipment'
FQ = [f'{y} Q{q}' for y in range(2026, 2032) for q in range(1, 5)][2:22]              # Q3 2026 .. Q2 2031
eq = [d[f'{EQ}|{q}'] for q in FQ]
per = {'H2 2026': (0, 2, (10,)), '2027': (2, 6, (20, 21.5)), '2028': (6, 10, (23, 24, 25.5)),
       '2029': (10, 14, (26, 27, 28)), '2030': (14, 18, (30,)), 'H1 2031': (18, 20, (15,))}
RPO, FIRM, RES = 39261, 53, 63                                                         # 10-Q Q2 2026; Q2 2026 release
for p, (a, b, gws) in per.items():                                                     # (GW, Street $/kW, order price at 0.90)
    s = sum(eq[a:b])
    print(p, round(s), [(g, round(s / g), round(s / g / 0.90)) for g in gws], 'GW at backlog price:', round(s / (RPO / FIRM), 1))
c28, c30 = sum(eq[:10]), sum(eq[:18])
print('firm RPO / Street to end-2028: %.0f%%' % (100 * RPO / c28), '| Street / firm RPO: %.3f' % (c28 / RPO))
print('firm + reservations / Street to end-2030:', [(P, '%.0f%%' % (100 * (RPO + RES * P) / c30)) for P in (680, 750, 825, 900)])
print('reservation price in Street to end-2030:', [(k, round((c30 / k - RPO) / (109 - FIRM))) for k in (0.955, 0.926, 0.90)])
```
