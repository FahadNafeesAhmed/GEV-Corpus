# Check: already known or bad data — candidate "power-equipment-fy28-fy29"

_Research input only (facts, arithmetic, sources). No memo sentences, no forecast chosen for the team. Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

**Result: does not survive this check.** The Street line is thin and not verifiable, the method and its inputs are already published by brokers and by management, and an ordinary explanation reproduces the Street's FY2028 number to the dollar.

## 0. What was recomputed (all from the primary files)

| Item | Candidate | Recomputed | Source |
|---|---|---|---|
| Street Power equipment FY2028 / FY2029 / FY2030 | 15,888 / 19,256 / 23,469 | 15,888 / 19,256 / 23,469 | `segment_quarterly.json`, key `Total Revenue\|Power\|Equipment` (Bloomberg, 2026-10-01) |
| H2 2026 / FY2027 | 5,491 / 12,151 | 5,491 / 12,151 | same |
| Power equipment RPO 6/30/26 | 39,261 | 39,261 | 10-Q Q2'26 (0001996810-26-000148), Power MD&A |
| Q2'26 order price | $1,049/kW | (39,261 - 28,530 + 1,965) / 12.1 = $1,049 | 10-Q Q2'26 |
| Q1'26 order price | $714/kW | (28,530 - 24,707 + 1,877) / 8.1 = $704 (10-Q shows 8.1 GW and $1,877M; candidate used 8.0 and $1,885M) | 10-Q Q1'26 (0001996810-26-000064) |
| Equipment RPO schedule 6/30/26 | 36 / 65 / 97% of 87,821 | same; 31,616 / 57,084 / 85,186 | 10-Q Q2'26 RPO note |
| FY2028 revenue consensus path | 59,196 -> 60,842 (+2.8%) | same; also 54,107 on 2026-01-02, so +12.7% year to date | workbook sheet `ConsensusHistory` |
| September output ladder | 5 / 6 / 7 GW a quarter | confirmed in the company-posted transcript | gevernova.com, Laguna conference transcript 2026-09-16 |

Reproduced: yes. One small input difference (Q1'26: 8.1 GW, not 8.0). It does not change any conclusion.

## 1. (a) Is the Street figure solid? No.

1. **The contributor count for this line is not visible.** The EEO "Company-Specific" exports give a mean only. `06_modl.xlsx` (Q3 2026) lists 29 brokers, but the Power equipment row shows no broker values (hidden on this terminal); only mean, low, high, median.
2. **Even the nearest quarter is wide.** Q3 2026 Power equipment: mean 2,394, low 2,063 (-13.8%), high 2,591 (+8.3%). A 17% gap two to three years out is inside the spread seen one quarter out.
3. **The line comes from quarterly models only, a subset of the Street.** Quarterly revenue has 28 estimates for Q3'26, 22 for Q1'27, 12 for each 2030 quarter (`01_eeo_annual.xlsx`, `02-eeo-annual-2030.xlsx`), against 33 / 21 / 20 annual EBITDA estimates for 2028 / 2029 / 2030. `08_eeg_2028.xlsx` lists 15 brokers with 2028 quarterly EPS. The equipment/services split is a subset of those.
4. **Signs of very few contributors in the out-years:**
   - `Organic Growth Rate||Power` is exactly 18.0 in all eight quarters of 2027-28 and exactly 9.0 in all eight of 2029-30. That is one model.
   - `RPO||Power` jumps 162,817 -> 181,972 between Q4'28 and Q1'29 and falls to 171,827 in Q1'31. Contributors drop in and out.
   - Equipment + services differs from the Power total by -231 to +307 a quarter in 2027-2030 (up to 3%), and by exactly 0 in 2031. The lines rest on different, shrinking broker sets.
   - `Organic Growth Rate||Electrification` shows 84,484% and 130,922% in two quarters. The division feed is not cleaned.
5. **Freshness.** Of the 45 dated rating rows in sheet `Bulk`, 12 are dated on or after 2026-09-17 (after the ladder was stated); 17 are dated 2026-07-22 to 07-29 and 16 are older or in August to early September. Rating dates are only a proxy for model dates, but they suggest most division models pre-date the September ladder. FY2028 revenue consensus moved +0.2% after it.
6. **Other vendor.** TIKR's Street data (2026-09-25) shows 2030 revenue of about $78B against Bloomberg $79.7B, and 2027 free cash flow of about $7.4B against $7.65B. The top line agrees within 2%. No second vendor publishes the Power equipment split, so the split cannot be cross-checked.
7. **At least one large broker is already far above the mean.** Morgan Stanley's note of 2026-07-23 (as reported in the press: corpus source 3886, and a copy at fancyhints.com) "now assumes 30 GW of shipments in 2030 at a price of roughly $900 per kilowatt" = $27.0B of gas equipment alone, 15% above the Bloomberg mean for all Power equipment in 2030 ($23,469M). The candidate's 2029-30 figures sit inside the existing range of broker models, not outside it.

## 2. (b) Is the idea already stated? The method and both inputs are; everyone who has published puts the high-priced orders in 2029 or later.

| Who / when | What is public | Source |
|---|---|---|
| Company, Q2'26 call (2026-07-22) | "first half 2026 orders were priced more than 20% above 4Q'25 equipment orders"; Q2 dollar per kW was higher "given a higher mix of aeroderivatives versus heavy-duty gas turbines and incremental combined cycle equipment"; H2 orders at the higher end of 10-20 points above 4Q'25 | corpus source 3161 |
| Company, Q1'26 call (2026-04-22) | "The dollar-per-kilowatt growth is going to be very healthy in the second quarter" | Utility Dive 2026-04-23 |
| BNP Paribas note (2026-07-22) | Order price estimate: about $790/kW heavy-duty, $950/kW HA combined-cycle scope, $1,800/kW aeroderivative | Utility Dive, corpus source 301 |
| Morgan Stanley note (2026-07-23) | 2029 capacity sold out; 30 GW shipped in 2030 at about $900/kW; revenue and EBITDA projections raised by $8B and $2B | corpus source 3886 |
| Morningstar (2025-08-14, 2026-07-22) | Power 2028 built as GW shipped x price; "earnings will come down to how fast it can fill" demand | morningstar.com |
| Market estimate quoted in press (2026-07-22, 2026-08-23) | Turbine price "to $600 per kilowatt by 2027" (the Street's 2027 line is $552-608/kW on 20-22 GW) | corpus source 3487; energynewsbeat.co |
| Mizuho analyst on CNBC (2026-07-02) | "On the turbines, they are pretty much sold out until 2028. There's not much upside to the revenue estimates through 2030" | corpus source 1775 |
| GLJ Research Sell note (2026-09-14) | "high-premium orders to materialize only in 2029"; 2026-27 orders ship in 2030-31 | TIKR blog summary of the note |
| Company, Laguna conference (2026-09-16) | The 2026 change in equipment margin in backlog "tells you in '29 and '30 because that's most of when that equipment delivers" | gevernova.com transcript |

- The candidate's "why missed" says GEV discloses no price per kW and Bloomberg has no line for it. True for the dollar level, but the company gives the percentage change in dollar per kW every quarter, and at least two brokers publish the level. GW x $/kW is the standard build.
- Not found: any published statement that FY2028 Power equipment consensus is 17% too low. The opposite view (sold out, no revenue upside) is published.
- For FY2029-30, the candidate's arithmetic is the same as the Morgan Stanley published model. That part is already stated.

## 3. (d) Ordinary explanation that reproduces the Street's FY2028 number

Street FY2028 = $15,888M.

| GW in 2028 | Order price $/kW | Conversion | Result $M | vs Street |
|---|---|---|---|---|
| 24 (company's stated 2028 output, release 2026-07-22) | 735 (mid of Q4'25 $753 and Q1'26 $714) | 0.90 (candidate's own back-test mean) | 15,876 | -0.1% |
| 24 | 714-753 | 0.90 | 15,422-16,265 | -3% to +2% |
| 23-25.5 | 714-753 | 0.90-0.93 | 14,780-17,857 | -7% to +12% |
| 23 (July plan) | 895 (first-in-first-out, includes the Q2'26 layer) | 0.90-0.93 | 18,526-19,144 | +17% to +20% (the candidate) |

- The Street figure is the company's stated 2028 output at the prices of the orders booked in Q4'25 and Q1'26, with the normal conversion. The candidate's title gives two readings ("flat 20 GW" or "a price 15-25% below 2026 orders"). The second reading is not odd: it is the price of the orders next in the queue before Q2'26.
- It also equals the company's January 2026 framework: Power high-teens organic growth to 2028 from $19,767M = $31.7-33.3B; Street Power 2028 = $33,521M (19.2% a year). The 24 GW step and the sold-out 2028 slots were already known when that framework was set (investor update 2025-12-09: sold out through 2028, 24 GW by mid-2028).
- The whole FY2028 gap comes from one assumption: that the Q2'26 order layer (12.1 GW, $12.7B, $1,049/kW) ships in 2028. Against that:
  - Management says the 2026 orders deliver mostly in 2029-30 (section 2, last row).
  - Management says the Q2'26 price per kW is lifted by mix (61 aeroderivative units against 9-27 in earlier quarters) and added combined-cycle scope. It is not a like-for-like turbine price.
  - The filings do not give delivery year by order. First-in-first-out is an assumption, and the candidate's own second lens says so.
- Schedule test (company-wide equipment RPO, 10-Q notes): the beyond-two-years bucket rose from 23,536 (3/31/26) to 30,737 (6/30/26), +7,201 (rounding +/-0.8B). New equipment orders in Q2'26 = 18,387 (Power 12,696; Electrification + Wind 5,691; equipment revenue 6,490). Allowing $3-5B for the quarter that rolled into the two-year window, $10.2-12.2B of Q2'26 orders landed beyond June 2028. That is about 70-95% of the Q2'26 Power orders. This fits delivery from H2 2028 onward. It cannot separate H2 2028 from 2029, so it neither proves nor kills the FY2028 claim.
- Other ordinary reasons for a low 2028 line: H1'26 shipments fell year on year (7.5 GW vs 8.2 GW) and Q2'26 shipped 3.3 GW; the step to 24 GW needs "castings and forgings arriving in '27" (Q2'26 call); EPC capacity is "the gating item" (CEO, 2026-06-22, corpus source 3504); conversion has ranged 0.80-0.99.

## 4. Corrected ranges (method and range only)

FY2028 Power equipment revenue = GW x order $/kW x conversion.

| Case | GW | $/kW | Conversion | $B | vs Street 15.89 |
|---|---|---|---|---|---|
| Company timing (Q4'25-Q1'26 prices) | 23-25.5 | 714-753 | 0.90-0.93 | 14.8-17.9 | -7% to +12% |
| About half the 2028 units at 2026 prices | 24 | about 800 | 0.90-0.93 | 17.3-17.9 | +9% to +12% |
| First-in-first-out (candidate) | 23-25.5 | 895 | 0.90-0.93 | 18.5-21.2 | +17% to +34% |
| Any case at the low conversion | 23-25.5 | 714-895 | 0.80 | 13.1-18.3 | -17% to +15% |

FY2029 (26-28 GW; 2026 order prices $838-874/kW from the H2 guide; conversion applied the same way as for 2028):

| Conversion | $B | vs Street 19.26 |
|---|---|---|
| 0.80 | 17.4-19.6 | -9% to +2% |
| 0.90 | 19.6-22.0 | +2% to +14% |
| 0.93 | 20.3-22.8 | +5% to +18% |
| 1.00 (candidate's price-implied lens, no haircut) | 21.8-24.5 | +13% to +27% |

- The candidate's FY2029 centre ($22.6B, +17%) uses no conversion haircut, while its FY2028 figures use 0.90-0.93. On one basis the FY2029 centre is about $20.4-21.0B (27 GW x $838 x 0.90-0.93), +6% to +9%.
- Centre of the corrected ranges: about +8% for either year. Error band from conversion alone (0.80-0.99 around 0.90) is about +/-11%; with the GW and price ranges it is about +/-13%. The gap is inside the error band.
- The candidate states that total Power revenue for 2029 shows no gap ($37.3-43.3B vs $39.5B). The claim is a mix shift inside Power, on the thinnest line.

## 5. (c) Has the stock moved on it?

- 2026-07-22 (RPO jump and 30 GW disclosed): 1,078.81 -> 985.03, -8.7%. The reaction was to the EPS miss and Wind.
- 2026-09-14 (Sell initiation): -8.6%. 2026-09-16 (ladder stated): +4.8%.
- FY2028 revenue consensus is up 12.7% year to date and FY2029 EBITDA consensus up 27%, while the forward multiple fell to the 6th percentile. Rising out-year revenue estimates have not moved the stock; it has traded on margin and EPS prints. Nothing shows this line is what the market prices.

## 6. Verdict against the test

| Test | Result |
|---|---|
| Street figure solid | No. Contributor count hidden, quarterly-model subset, single-model signatures in the out-years, mostly pre-September, no second vendor. Nearest-quarter spread is -14% / +8% |
| Idea not already stated | Fails for FY2029-30 (Morgan Stanley: 30 GW x about $900/kW in 2030; BNP price per kW; management's own dollar-per-kW commentary). Not found stated for FY2028, where the published views place high-priced orders in 2029 or later |
| No ordinary explanation | Fails for FY2028. 24 GW x $735/kW x 0.90 = $15,876M, and the Street equals the January framework |
| Gap outside the error band | No. About +8% centre against about +/-13% |
| Date inside 12 months | No. FY2028 prints February 2029; only proxies before then |

What would change this result: a filing or company statement giving delivery year by order vintage, or broker-level detail for the Power equipment line (EEB / MODL for a 2028 period with contributors visible) showing at least 8-10 brokers within +/-5% of $15.9B.

Files: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, `06_modl.xlsx`, `01_eeo_annual.xlsx`, `02-eeo-annual-2030.xlsx`, `08_eeg_2028.xlsx`; `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` (sheets Consensus, ConsensusHistory, PricePositioning, Bulk); `data/gev.db` (chunks for accessions 0001996810-26-000148, -26-000064, -26-000015, -26-000012; sources 301, 1775, 3161, 3487, 3504, 3886).
