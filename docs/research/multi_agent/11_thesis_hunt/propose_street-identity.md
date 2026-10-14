# Thesis hunt, lens: internal consistency of the Street (2026-10-01)

_AI-assisted research input only: facts, arithmetic, tables and sources. No memo sentences and no forecast choices; ranges and methods only. Bloomberg figures are licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep inside the project folder._

Method: take the Street's own quarterly division model (orders, RPO, revenue, EBITDA, D&A, capex, FCF, wind MW) and test accounting identities. Where the lines cannot all be true at once, use the filings to say which line is wrong and what the corrected value is. $M unless stated. "Street" = Bloomberg mean unless stated.

## 0. Result

| Question | Answer |
|---|---|
| Does any identity break give a profit line (EBITDA, EBIT) that is 5% or more from the Street inside the 3-12 month horizon? | **No.** At the EBITDA line the breaks net to about -5% to +7% for the next four quarters, centre about +1%. |
| Is the Street's division model arithmetically coherent? | **Yes for Power and Electrification.** Start RPO + orders - revenue reproduces the Street's own RPO within 0.2% at end-2027 and within 2.6% through 2028. So the low equipment revenue is a deliberate assumption (slower conversion), not a slip. |
| The one line returned as a candidate | **Power + Electrification equipment revenue, Q3'26 to Q2'27: Street 24,415; GEV's own schedule gives at least 25,346 to 25,786 and 26,288 at the centre (+3.8% / +5.6% / +7.7%).** Same line the Wind lens reached; derived here independently and tied to the roll-forward. |
| Street lines that are artefacts and should not be quoted | Total RPO mean for Q3'26 and Q4'26 (overstated by $12-14B); Wind RPO for Q3'26 and Q4'26 (+80% to +100%); total orders line (8% above the division sum in 2027); FY26 EPS mean; division D&A lines; Electrification services line. Corrected values in section 6. |
| Mix finding | The two RPO schedules together say more equipment and (weakly) less services than the Street. Revenue about +3% to +5%, EBITDA about flat, margin 0.2 to 0.5 points lower. |

## 1. Sources and cells

| Tag | Source |
|---|---|
| BBG-A | `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx`, sheet Consensus, rows 2-18, columns C-G (2026-2030): revenue r2, EBITDA r3, EBIT r9, net income r10, EPS r11-r15, FCF r16, capex r17, gross margin r18 |
| BBG-Q | `GEV_Pull_2026-10-01/segment_quarterly.json`, keys `Block|Parent|Line|YYYY Qn` (same data as `01..05-eeo-company-specific.xlsx`) |
| BBG-M | `06_modl.xlsx` (Q3'26, mean / low / high / median): r13 FCF, r64 orders, r69 RPO, r96-97 product and service revenue, r101-102 cost of equipment and services, r104 gross margin, r115-116 D&A, r125 tax rate, r172 contract liabilities, r205 change in contract liabilities |
| BBG-E | `01_eeo_annual.xlsx`, `02-eeo-annual-2030.xlsx`: depreciation, amortization, net debt, analyst counts |
| 10-Q / 10-K | corpus `gev.db`: 10-Q Q2'26 0001996810-26-000148 (RPO note p.15, segment MD&A pp.29-31, acquisition note p.14, cash flow p.8); 10-Q Q1'26 -26-000064; 10-K FY25 -26-000015; 10-Q Q3'25 -25-000160; 10-Q Q2'25 -25-000133; 10-Q Q1'25 -25-000073; 10-K FY24 -25-000011; 2024 10-Qs -24-000008, -24-000067, -24-000083; information statement 0001193125-24-063739 |
| REL | Earnings releases (8-K exhibits) Q1'24 to Q2'26: segment orders |
| CALL | Q2'26 call transcript (corpus `sources.id=3161`); Q1'26 and Q4'25 call transcripts (company webcast transcripts, read 2026-10-01) |
| CONF | September 2026 investor-conference write-up (corpus `sources.id=681`). Single secondary source |

## 2. Identity audit

### 2.1 RPO roll-forward (start + orders - revenue against the Street's RPO line) [BBG-Q]

Start values at 6/30/26 from the 10-Q: Power 111,649; Wind 20,388; Electrification 44,563; company 176,284.

| | Q3'26 | Q4'26 | Q4'27 | Q4'28 | Q4'29 | Q4'30 |
|---|---|---|---|---|---|---|
| Power: identity | 118,086 | 125,693 | 150,529 | 167,247 | 180,208 | 189,305 |
| Power: Street | 118,799 | 127,667 | 150,768 | 162,817 | 190,424 | 198,546 |
| Power: difference | +0.6% | +1.6% | +0.2% | -2.6% | +5.7% | +4.9% |
| Electrification: identity | 47,180 | 50,384 | 64,337 | 79,127 | 94,748 | 111,267 |
| Electrification: Street | 46,998 | 50,252 | 64,222 | 78,028 | 94,988 | 109,309 |
| Electrification: difference | -0.4% | -0.3% | -0.2% | -1.4% | +0.3% | -1.8% |
| Wind: identity | 19,556 | 18,974 | 17,063 | 15,888 | 13,859 | 11,889 |
| Wind: Street | 35,153 | 38,068 | 17,590 | 16,920 | 15,927 | 15,608 |
| Wind: difference | **+79.8%** | **+100.6%** | +3.1% | +6.5% | +14.9% | +31.3% |
| Company: identity (company orders line) | 184,623 | 195,780 | 240,172 | 270,153 | 299,012 | 328,264 |
| Company: identity (division-sum orders) | 184,512 | 194,841 | 232,037 | 262,553 | 289,418 | 313,424 |
| Company: Street | 196,789 | 209,676 | 233,294 | 234,079 | 296,141 | 322,355 |
| Company: Street vs identity (company orders line) | **+6.6%** | **+7.1%** | -2.9% | **-13.4%** | -1.0% | -1.8% |

Readings:

- Power and Electrification hold within 0.2% at end-2027. The same brokers' orders, revenue and RPO are one coherent model.
- Wind RPO for Q3'26 and Q4'26 is bad data. BBG-M r69: Wind high estimate $112.6B, median $19,756M, mean $35,153M. One outlier.
- That outlier lifts the company RPO mean by $12-14B. BBG-M company RPO for Q3'26: mean 196,789; median 185,946. Identity: 184,623.
- Corrected path: $184.6B at 9/30/26, $194.8-195.8B at year-end, $205.5-207.7B at 3/31/27. This matches the company statement that backlog reaches $200B "early in 2027" [CONF]. The Street mean ($209.7B at year-end 2026) does not.
- The Q4'28 company figure (234,079, below Q3'28 at 250,205) is a change in the set of brokers, not a forecast.

### 2.2 Division sums against totals [BBG-Q]

| | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|
| Orders: company line | 97,489 | 91,401 | 100,408 | 109,969 |
| Orders: sum of three divisions | 90,292 | 91,937 | 98,414 | 104,724 |
| Difference | **+8.0%** | -0.6% | +2.0% | +5.0% |
| Revenue: company line vs division sum | -0.6% | -0.3% | -0.4% | -0.4% |
| EBITDA: company line | 9,391 | 12,880 | 16,231 | 19,471 |
| EBITDA: divisions ("EBITDA" rows) + Other | 9,313 | 12,760 | 16,249 | 19,354 |
| EBITDA: divisions ("Adjusted EBITDA" rows) + Other | 9,413 | 12,682 | 16,232 | 19,561 |

- The 2027 company orders line ($97.5B) and the division lines ($90.3B) come from different broker sets. By quarter the gap is +0.5% (Q3'26), +3.4% (Q4'26), +6.0% (Q1'27), +9.2% (Q2'27).
- Division revenue sums run 0.3-0.6% above the company line. GEV reports eliminations of -$62M in H1'26 and -$451M in FY25. The Street carries almost none.
- Q3'26: company EBITDA 1,672; division "EBITDA" rows sum to 1,652; "Adjusted EBITDA" rows to 1,608. The headline is 4.0% above the adjusted-row sum. Guide-implied range 1,544-1,705 (Power 17-18% on +17-19% growth; Electrification $3.8-4.0B at 18.6-19.2%; Wind about zero; corporate $105-130M).

### 2.3 Quarterly sums against annual consensus [BBG-A, BBG-Q]

| | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| Revenue: quarters / annual | +0.2% | +0.1% | +0.7% | +1.0% | +1.2% |
| EBITDA: quarters / annual | -0.3% | -0.8% | +2.6% | -1.6% | -0.4% |
| FCF: sum of quarters | 12,548 | 8,176 | 9,303 | 8,176 | 13,301 |
| FCF: annual | 12,196 | 7,654 | 9,527 | 9,702 | 13,036 |
| FCF: difference | +2.9% | **+6.8%** | -2.3% | **-15.7%** | +2.0% |
| EPS: quarters / annual | n/a | 24.44 / 24.52 | 34.24 / 34.80 | 44.93 / 45.21 | 53.65 / 54.73 |

- Revenue, EBITDA and EPS tie. FCF does not: the FY27 "consensus" is $7.65B or $8.18B depending on the screen; FY29 is $9.70B or $8.18B (Q1'29 is -$1,684M on the quarterly screen).

### 2.4 EBITDA, EBIT and D&A [BBG-A, BBG-Q, BBG-E, 10-Q]

| | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| Annual EBITDA - EBIT | 1,907 | 1,437 | 1,124 | 1,605 | 1,453 |
| Division D&A rows, summed | 1,473 (H1 actual 760 + Street H2) | 1,435 | 1,303 | 1,287 | 1,276 |

- Reported D&A: 342 (Q1'26), 418 (Q2'26). Q2 = depreciation 182 + amortization 236.
- Prolec intangibles [10-Q p.14]: customer 2,860 over 12 years; technology 533 over 6; software 8 over 3; trademarks and other 771 over 2. Straight line: 238 + 89 + 3 + 386 = **$715M a year, $179M a quarter**, through January 2028; then about $330M a year.
- Floor for FY27 D&A: 4 x 418 = 1,672, before depreciation on capex of $1.4-1.7B a year. Street: 1,437 (annual EBITDA - EBIT) and 1,435 (division rows).
- Effect: FY27 EBIT 236-414 lower than 8,034 (-2.9% to -5.2%); EPS -$0.67 to -$1.18 on $24.52 (-2.7% to -4.8%). No EBITDA effect.
- The broad Street is partly right already: BBG-M r115-116 median D&A for Q3'26 is 415-416 (mean 349-370, low 183-209). BBG-E depreciation + amortization: 352 (Q3'26), 372, 402, 419 (Q2'27). The stale figures sit in the division rows and in the mean.
- Result: under 5% on EBIT and EPS. Not a candidate.

### 2.5 EPS, net income and share count [BBG-A, BBG-Q, BBG-E]

| | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| Annual net income / annual EPS (implied shares, M) | 294.0 | 270.9 | 266.8 | 266.2 | 263.4 |
| Quarterly adjusted net income / quarterly EPS | n/a | 265.2 | 265.4 | 264.3 | 266.6 |

- FY26 EPS mean (24.39) mixes GAAP figures that include the $4.0B Prolec gain with figures that exclude it (median 28.68; high 33.86; low 12.42). H1 actual 19.96 + Street Q3 4.04 + Q4 5.61 = 29.6. The FY26 mean is unusable.
- Shares outstanding 266.33M; Q3'26 diluted 269.7M (BBG-M). The Street holds the count about flat to 2030.
- Net debt [BBG-E]: -9,455 (Q2'26 actual), -11,645, -11,968, -12,071, -13,327 (Q2'27); -41,410 (Q4'30). Net cash rises 3,872 over four quarters against Street FCF of 5,106 for the same quarters. Implied dividends plus buybacks about 1.2B, against 3,944 returned in H1'26 alone. The Street models buybacks nearly stopping.
- EV bridge note: a price grid for September 2027 that uses today's bridge (+8,298) leaves out the cash built in between. On Street numbers that is about +3.9B by mid-2027 and about +7B by Q3'27 (Q3'27 Street FCF 3,158), or $15-26 a share (1.5-2.7% of $987).

### 2.6 Revenue per unit: wind MW [BBG-Q, 10-Q]

| | H2'26 | H1'27 | H2'27 | FY27 | FY28 | FY29 | FY30 |
|---|---|---|---|---|---|---|---|
| Street MW delivered | 3,281 | 1,882 | 3,086 | 4,968 | 4,479 | 6,087 | 6,316 |
| Street Wind equipment revenue | 3,552 | 2,278 | 3,085 | 5,363 | 4,537 | 5,258 | 5,315 |
| Equipment revenue per kW ($) | 1,083 | 1,210 | 1,000 | 1,080 | 1,013 | 864 | 842 |

- Reported: FY24 $1,032/kW; FY25 $1,051/kW; H1'26 $1,142/kW (all equipment revenue over GW sold, offshore included).
- The 2029-2030 MW line (+36%) and the revenue line (+16%) do not agree: $/kW falls 15-17%. Different broker sets.
- Orders against deliveries (GW, 10-Q units tables): orders H1'24 2.5, H2'24 2.7, H1'25 1.7, H2'25 3.1, H1'26 1.2. Sales H1'25 3.0, H2'25 3.9, H1'26 2.0. Sales over orders two halves earlier: 1.20, 1.44, 1.18. Street: H2'26 1.06; **H1'27 1.57** (1.88 GW on 1.2 GW of orders).
- At 1.18-1.44 the H1'27 figure is 1.4-1.7 GW (-8% to -25% on MW). Wind revenue effect about -$0.2B to -$0.55B in H1'27. Other lenses put the Street inside a wider band (1.3-2.1 GW). Kept as a risk line, not a candidate.
- Street Wind equipment backlog, rolled forward (8,197 + Street Wind orders - Street services revenue - Street equipment revenue): about 6.8B (end-2026), 5.0B, 4.1B, 2.1B, 0.2B (end-2030). The Street's Wind orders and Wind revenue cannot both hold after 2028.

### 2.7 Gross-margin components for Q3'26 [BBG-M]

| Line | Mean | Median |
|---|---|---|
| Product revenue (r96) / cost of equipment (r101) | 7,361 / 5,952 = 19.1% margin | 7,304 / 5,832 = 20.2% |
| Service revenue (r97) / cost of services (r102) | 4,617 / 3,029 = 34.4% | 4,557 / 2,961 = 35.0% |
| Gross margin from the four lines | 25.0% | 25.9% |
| Gross margin headline (r104) | 24.2% | 23.9% |

- Reported Q2'26: equipment 13.1% (6,459 / 5,613), services 32.6% (4,645 / 3,130), total 21.25%. H1'26: 11.8% and 31.6%.
- The component lines imply equipment margin up 6-7 points in one quarter; the headline implies about 5. Wind moving from -275 to about zero is worth 3.7 points of equipment margin on 7,361. The rest is Power and Electrification.
- The component lines and the headline differ by 0.8-2.0 points: different broker sets. Use the headline.

## 3. Candidate: Power + Electrification equipment revenue, Q3'26 to Q2'27

### 3.1 What the roll-forward says the Street assumes

Street next-four-quarter equipment revenue over 6/30/26 equipment RPO [BBG-Q; 10-Q MD&A]:

| Division | Equipment RPO 6/30/26 | Street next 4Q | Street ratio | Reported ratios, each window since 12/31/23 (next 4Q revenue / opening RPO) |
|---|---|---|---|---|
| Power | 39,261 | 10,874 | 27.7% | 41.9, 41.7, 56.6, 57.4, 53.7, 50.9, 46.7% |
| Electrification | 40,589 | 13,541 | 33.4% | 41.8, 38.4, 34.7, 35.8, 36.9, 38.6 (36.5 without Prolec), 41.5 (36.2 without Prolec)% |
| Wind | 8,197 | 5,830 | 71.1% | 58.7, 62.7, 63.6, 66.2, 67.6, 69.5, 65.0% |

- Power and Electrification are at their lowest on record. Wind is at its highest.
- Because section 2.1 holds, this is what the Street intends: backlog grows faster than output, so conversion slows. The 10-Q schedule says otherwise for the next year.

### 3.2 Company schedule with Wind removed

- 10-Q Q2'26 p.15: equipment RPO 87,821, 36% within one year = 31,616 (35.5%: 31,176; 36.5%: 32,055).
- Wind's share of that schedule cannot exceed what Wind recognises in the year. Reported Wind turnover has been 58.7-69.5% of its equipment RPO, and that includes orders booked and shipped inside the year.

| Wind assumption | Wind | Power + Electrification scheduled (35.5% / 36% / 36.5%) | vs Street 24,415 |
|---|---|---|---|
| Street's own Wind figure (71.1%) | 5,830 | 25,346 / 25,786 / 26,225 | +3.8% / +5.6% / +7.4% |
| 69.5% (highest reported) | 5,697 | 25,480 / 25,919 / 26,358 | +4.4% / +6.2% / +8.0% |
| 65% (median) | 5,328 | 25,848 / 26,288 / 26,727 | +5.9% / +7.7% / +9.5% |
| 58.7% (lowest reported) | 4,812 | 26,365 / 26,804 / 27,243 | +8.0% / +9.8% / +11.6% |

- For the Street's Power + Electrification figure to equal the schedule, Wind would have to convert (31,616 - 24,415) / 8,197 = 87.9% of its equipment backlog.
- Allocation of the 1,371 company gap (31,616 - 30,245) at the centre: Electrification about +1.07B (36% of 40,589 = 14,612 against 13,541), Power about +0.80B (residual: 31,616 - 14,612 - 5,328 = 11,676 against 10,874), Wind about -0.50B (65% of 8,197 = 5,328 against 5,830).

### 3.3 Back-test of the same statistic (external segment equipment revenue; sums to company "sales of equipment")

Ratio = Power + Electrification actual next-4Q equipment revenue / (company scheduled - Wind actual).

| Window opens | Scheduled | Wind actual | Scheduled less Wind | P + E actual | Ratio | Without Prolec |
|---|---|---|---|---|---|---|
| 12/31/23 | 20,644 | 8,018 | 12,626 | 10,934 | **0.866** | 0.866 |
| 3/31/24 | 18,994 | 8,197 | 10,798 | 11,335 | 1.050 | 1.050 |
| 6/30/24 | 19,534 | 8,323 | 11,211 | 11,909 | 1.062 | 1.062 |
| 9/30/24 | 19,352 | 8,029 | 11,323 | 12,793 | 1.130 | 1.130 |
| 12/31/24 | 18,941 | 7,224 | 11,717 | 13,710 | 1.170 | 1.170 |
| 3/31/25 | 20,465 | 6,707 | 13,758 | 15,284 | 1.111 | 1.077 |
| 6/30/25 | 20,879 | 6,315 | 14,564 | 17,241 | 1.184 | 1.096 |
| 6/30/26 (Street) | 31,616 | 5,830 (Street) | 25,786 | 24,415 (Street) | 0.947 | |

- Six of seven reported windows are at 1.05 or higher. One is 0.866 (the 2024 window: the sale of part of Steam Power's nuclear activities removed backlog mid-year, and offshore wind slipped, so Wind's actual understates Wind's schedule).
- Company-level version of the same back-test (actual equipment revenue / scheduled): 0.918, 1.028, 1.036, 1.076, 1.105, 1.075, 1.128. Street for the 6/30/26 window: 0.957.
- Applying 1.05 / 1.096 to the 26,288 centre gives 27.6B / 28.8B (+13% / +18%). Applying 0.866 gives 22.8B (-7%).

### 3.4 Where it sits in time

- H2'26 is pinned by the FY26 guide. Street Power + Electrification equipment: Q3 5,693; Q4 6,576; H2 12,269.
- If H2'26 lands on the Street, the schedule leaves 13,077 to 13,517 (floor) and 14,019 (centre) for H1'27 against the Street's 12,146: **+7.7% to +11.3% floor; +15.4% centre.**
- Company equipment revenue in H1'27 would then be up about 35% on H1'26; the Street has +23%.

### 3.5 Corrections that shrink it

- Bloomberg's Electrification services row is high: 2,689 for the four quarters against 2,135-2,213 trailing and +3.1% growth in H1'26. If the total (16,145) is right, Electrification equipment on the Street is 13.8-13.9B, not 13,541 (Electrification lens, T7). The Street's Power + Electrification figure is then 24,746-24,896, and the gap is +1.8% to +4.2% at the floor (25,346-25,786) and +5.6% to +6.2% at the centre (26,288).
- Division equipment rows include intersegment sales (31 in Q2'26). Company "product revenue" for Q3'26 is 7,361 (BBG-M) against a division sum of 7,482. On the company basis the gap is about 0.4 points wider.

### 3.6 Profit and margin effect

| Case | Extra equipment revenue | At 15% / 30% margin | Share of Street next-4Q EBITDA (8,210) |
|---|---|---|---|
| Floor (25,786) | +1,371 | +206 / +411 | +2.5% / +5.0% |
| Centre (26,288) | +1,873 | +281 / +562 | +3.4% / +6.8% |
| Centre x 1.05 | +3,187 | +478 / +956 | +5.8% / +11.6% |

- Reported incremental segment margins for scale: Electrification +681 EBITDA on +2,596 revenue in H1'26 (26%; about 32% without Prolec); Power +539 on +1,215 (44%, with services price in it). Equipment gross margin was 11.8% in H1'26.
- More equipment lowers the company margin percentage (section 4.1).

### 3.7 Reveal dates and marks

| Date | Number | Street comparator | Mark |
|---|---|---|---|
| 28 Oct 2026 | 10-Q Q3'26: new one-year share x equipment RPO at 9/30/26, less Wind at 65-71% of Wind equipment RPO | Power + Electrification equipment Q4'26-Q3'27: 25,657 (Power 11,505; Electrification 14,152) | 5% or more above keeps the gap |
| 28 Oct 2026 | Power + Electrification equipment revenue, Q3'26 (segment MD&A) | 5,693 | 6.0B or more |
| Late Jan 2027 | 10-K: one-year share x year-end equipment RPO | FY27 equipment 32,383; Power + Electrification 27,020 | |
| Late Apr and late Jul 2027 | Power + Electrification equipment revenue, Q1'27 + Q2'27 | 12,146 | 13.5B or more passes; 12.5B or less fails |

## 4. Items under the 5% bar or with a band wider than the gap

### 4.1 Services schedule and the equipment / services mix

Services RPO x one-year share against next-4Q services revenue [10-Q notes; income statements; BBG-Q]:

| Window opens | Scheduled | Next 4Q services | Ratio | Band for rounding of the % |
|---|---|---|---|---|
| 12/31/23 | 12,019 (16%) | 15,982 | 1.330 | 1.289-1.373 |
| 3/31/24 | 11,853 (16%) | 16,175 | 1.365 | 1.323-1.409 |
| 6/30/24 | 12,566 (17%) | 16,382 | 1.304 | 1.266-1.343 |
| 9/30/24 | 12,865 (17%) | 16,848 | 1.310 | 1.272-1.349 |
| 12/31/24 | 13,676 (18%) | 17,134 | 1.253 | 1.219-1.289 |
| 3/31/25 | 14,033 (18%) | 17,383 | 1.239 | 1.205-1.274 |
| 6/30/25 | 13,419 (17%) | 17,811 | 1.327 | 1.289-1.367 |
| 6/30/26 (Street) | 14,154 (16%) | 19,790 | **1.398** | 1.356-1.443 |

- The Street's ratio is above all seven reported windows, by 2.4% over the highest and 6.3% over the median (1.31). At 1.31-1.365: 18.5-19.3B against 19,790 (-2.4% to -6.3%).
- Scheduled year-one services grew 5.5% (14,154 against 13,419). The Street's services grow 11.1%. Years two to five of the schedule grew 18.3% (54% x 88,463 less year one = 33,616, against 28,418), so the services step-up in the schedule is later.
- Part of the excess is the Electrification services row (section 3.5). Rounding of the 16% is worth +/-3.1%. Band wider than the gap: not a candidate.
- Equipment share of revenue: FY24 54.2%; FY25 55.0%; H1'26 57.3%; Street next 4Q 60.4%; Street FY27 60.8%. The two schedules at their centres (31,616 x 1.05 and 14,154 x 1.31) give 64.2%.

Next-4Q sensitivity (Street: revenue 50,019; EBITDA 8,210; margin 16.4%):

| Equipment | Services | Margin on the change (equipment / services) | Revenue | EBITDA | Margin |
|---|---|---|---|---|---|
| 31,616 | 19,790 | 15% / 35% | +2.7% | +2.5% | 16.4% |
| 33,197 | 18,542 | 15% / 35% | +3.4% | +0.1% | 15.9% |
| 33,197 | 18,542 | 20% / 35% | +3.4% | +1.9% | 16.2% |
| 33,197 | 19,320 | 20% / 33% | +5.0% | +5.3% | 16.5% |
| 31,616 | 18,542 | 15% / 35% | +0.2% | -2.8% | 15.9% |
| 34,019 | 17,537 | 12% / 38% | +3.0% | -4.9% | 15.1% |

- Reading: taking both schedules at face value gives revenue +3% to +5% and EBITDA about flat. Precedent: Q2'26 revenue was 2.9% above consensus, adjusted EBITDA about 2% below, the margin guide was held and the stock fell 8.7% on the day.

### 4.2 Electrification revenue, FY27

- Street: revenue 17,704; equipment 14,869; services 3,118; RPO at end-2026 50,252 (equipment about 46.0-46.2B after 4.1-4.3B of services RPO).
- Street conversion 32.2-32.4% of that backlog. At 34.7-36.9% (the last five reported windows, without Prolec): equipment 15.9-17.0B, revenue 18.8-19.9B (+6% to +12%). After the services-row correction: about +4% to +10%.
- Organic equipment growth, reported: +40%, +45%, +47%, +38% (Q3'25 to Q2'26, Prolec taken out at 95% of its revenue). Street-implied: +21%, +16%, +9%, +23% (Q3'26 to Q2'27); +17% for the four quarters.
- Guide record: Q2'26 revenue guide $3.3-3.5B, actual 3,637 (+3.9% over the top). FY26 guide raised by $0.5B at each of the last two reports.
- Why not returned: the conversion ratio falls when backlog outgrows output, and the guide already takes the legacy ratio to about 30-32%. The Electrification lens rebuilds the next four quarters at about +4% (range +1.5% to +7%). Band about as wide as the gap.

### 4.3 Wind revenue, FY27

- Street: revenue 7,589; equipment 5,363; services 2,092; 4,968 MW.
- Street Wind equipment backlog at end-2026, rolled forward: 6.4-6.8B. Street FY27 equipment is 79-84% of it. Reported blended turnover 58.7-69.5% gives 3.8-4.7B (Wind revenue -8% to -21%). With offshore taken out the reported range is higher (Wind lens: 73-85% onshore-only), which puts the Street at the top of the range, not outside it.
- Company framework: down low-double digits a year from 9,110 gives 6.9-7.2B for 2027 (Street +5% to +10% above).
- Street Wind EBITDA: +208 in Q4'26 alone, +188 for all of FY27.
- Band about as wide as the gap. Model input and risk line.

### 4.4 Contract liabilities and FCF

- BBG-M r172: Q3'26 current contract liabilities mean 37,492, median 39,944. The 6/30/26 reported figure is 39,944. The median holds the balance flat; the mean has it falling 2.5B. BBG-M r205: change in contract liabilities mean -1,402, median -50.
- The cash-flow line has been positive in all 10 quarters since the spin (64 to 8,121). As a share of (segment orders - revenue): 36%, 19%, 12%, 41%, 50%, 22%, 12%, 50%, 62%, 61%.
- Street Q3'26 orders - revenue = 8,339. At 12% / 37% / 62%: +1.0B / +3.1B / +5.2B.
- FY27 bridge on Street lines: EBITDA 9,471 - capex 1,441 - cash tax 1,750 to 2,300 - other 1,000 to 1,500 = 4,230-5,280, so Street FCF of 7,654 implies working capital of +2.4B to +3.4B. Reported working capital (five cash-flow lines): +1.1B (FY24), +4.1B (FY25), +11.7B (H1'26).
- Report-day record: the largest FCF raise (+$5B, 22 Jul 2026) came with -8.7%. Low price relevance. Band wider than the gap for FY26 and FY27 FCF (see the FCF lens).

### 4.5 Power backlog against the shipment ladder (no gap)

- Firm gas backlog 53 GW at 6/30/26. Shipments guided at 5 GW a quarter in H2'26 and early 2027, 6 GW a quarter in H2'27, 6-7 in 2028 [CALL, CONF]: about 10 + 22 + 25 = 57 GW by end-2028.
- Street Power equipment revenue H2'26 to FY28: 5,491 + 12,151 + 15,888 = 33,530, against Power equipment RPO of 39,261.
- Two-year check: company schedule 65% x 87,821 = 57,084. Less Wind at about 95% (7.8B) and Electrification at 60-65% (24.4-26.4B) leaves 22.9-24.9B for Power. Street Power equipment for Q3'26 to Q2'28: 24,741. Consistent. No gap on the two-year view.

### 4.6 Out-year breaks (outside the horizon)

| Line | Street | Check |
|---|---|---|
| Wind equipment backlog | about zero by end-2030 on the Street's own orders and revenue | Street Wind revenue rises 8% in 2029 |
| Electrification conversion | Street revenue / opening RPO falls to about 28% by 2030; orders 1.58-1.79x revenue every year | Backlog reaches 3.8 years of revenue |
| Power services | 14,259 / 15,675 / 17,665 / 19,711 / 22,357 (2026-2030): 11.3% a year | Reported +4.9% (FY24), +5.3% (FY25), +5.8% (H1'26). The company's own chart is $12B (2025) to $22B (2035), 6.2% a year. The Street reaches the 2035 figure in 2030 |
| Power RPO | steps +19B between Q4'28 and Q1'29 | change of broker set |

## 5. Net of everything for the next four quarters (ranges, not a forecast)

| Line | Change against the Street | EBITDA at the stated margin |
|---|---|---|
| Power + Electrification equipment | +1.4B to +1.9B (schedule only) | +0.2B to +0.6B (15-30%) |
| Wind equipment | -0.1B to -0.6B | -0.02B to -0.15B (15-25%) |
| Services | 0 to -1.25B | 0 to -0.44B (35%) |
| Total | -0.45B to +1.8B revenue (-0.9% to +3.6%) | -0.4B to +0.6B (-5% to +7%); centre about +0.1B (+1%) |

## 6. Street lines to correct before use

| Line | Street figure | Problem | Use instead |
|---|---|---|---|
| Company RPO, Q3'26 / Q4'26 | 196,789 / 209,676 | one Wind outlier ($112.6B) in the mean | 184.6B / 194.8-195.8B (identity); median 185,946 for Q3 |
| Wind RPO, Q3'26 / Q4'26 | 35,153 / 38,068 | same outlier | 19.6B / 19.0B |
| Company RPO, Q4'28 | 234,079 | broker set changes | 262.6-270.2B (identity) |
| Orders, FY27 | 97,489 | company line and division lines differ 8% | 90,292 (division sum) alongside it |
| EPS, FY26 | 24.39 mean | GAAP and ex-gain figures mixed | 28.68 median, or 29.6 = H1 actual + Street quarters |
| D&A, FY27 | 1,435-1,437 | below the Q2'26 run-rate of 1,672 | 1,672 floor |
| FCF, FY27 / FY29 | 7,654 / 9,702 | quarterly screen gives 8,176 / 8,176 | state both |
| Electrification services, next 4Q | 2,689 | +22% to +26% on trailing; H1'26 grew 3% | 2.2-2.4B, with equipment raised by the difference |
| Q3'26 contract liabilities | 39,944 median; 37,492 mean | flat or falling; never happened | 41-45B |
| Wind MW 2029-2030 | +36% | revenue line +16% | treat as unreliable |

## 7. Overlap with the other lens files

- Section 3 reaches the same line as the Wind lens (T7) and the equipment-schedule lens. New here: the roll-forward evidence that the low conversion is an intended assumption; the seven-window back-test of the Wind-removed statistic including the 0.866 window; the split by half-year.
- Sections 4.1 to 4.4 agree with the services, Electrification, Wind and FCF lens files on direction and on "band wider than gap".
- Sections 2.1 to 2.5 and section 6 (artefact list, EV bridge note) are specific to this lens.

## 8. Reproduce

- Street quarters: `segment_quarterly.json`; year = sum of four quarters; "next 4Q" = Q3'26 + Q4'26 + Q1'27 + Q2'27.
- Identity: RPO(t) = RPO(t-1) + Orders(t) - Revenue(t), by division and for the company, from the 6/30/26 10-Q values.
- Scheduled = equipment (or services) RPO x one-year share from the RPO note of each filing.
- Segment equipment revenue: MD&A tables (segment basis) for the conversion ratios; segment-note external product revenue for the Wind-removed back-test (Power 1,185 / 1,284 / 1,378 / 1,662 / 1,422 / 1,459 / 1,668 / 1,871 / 1,877 / 1,957; Wind 1,227 / 1,660 / 2,488 / 2,643 / 1,406 / 1,786 / 2,194 / 1,838 / 889 / 1,394; Electrification 1,203 / 1,246 / 1,419 / 1,544 / 1,369 / 1,649 / 2,019 / 2,253 / 2,488 / 3,109 for Q1'24 to Q2'26).
- Prolec revenue 485 (Q1'26) and 859 (Q2'26) [10-Q p.14]; 95% taken as equipment (assumption).
- Hand-checks before use: the September conference statements have one secondary source; the 2024 window explanation (divestiture and offshore slippage) is a reading, not a disclosed reconciliation; Bloomberg division rows show no contributor counts.
