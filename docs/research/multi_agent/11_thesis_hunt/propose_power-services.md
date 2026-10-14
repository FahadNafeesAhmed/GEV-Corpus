# Thesis hunt, lens: Power services (2026-10-01)

_AI-assisted research input only. Facts, arithmetic, tables and sources. The team writes every memo sentence, chooses every forecast number and chooses the direction. Bloomberg data is licensed for academic use: keep it inside the project folder and cite it as "Bloomberg, 2026-10-01"._

Method: number-first. Each section computes a figure from disclosed data, then compares it with Bloomberg consensus. Direction is stated last.

Source keys: 10-K24 = 0001996810-25-000011; 10-K25 = 0001996810-26-000015; 10-Q1'24 = -24-000008; 10-Q2'24 = -24-000067; 10-Q3'24 = -24-000083; 10-Q1'25 = -25-000073; 10-Q2'25 = -25-000133; 10-Q3'25 = -25-000160; 10-Q1'26 = -26-000064; 10-Q2'26 = -26-000148; Form 10 information statement = 0001193125-24-063739 (EX-99.1). IU25 = GE Vernova 2025 Investor Update, 2025-12-09 (deck slide 28, corpus src:1844; transcript gev_webcast_transcript_12092025.pdf, fetched 2026-10-01). Q2'26 call = corpus src:3161. Laguna = conference coverage 2026-09-16/18, corpus src:681 and src:686 (secondary source).

Street data: `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json`, key `Total Revenue|Power|Services|YYYY Qn` (same values as row 25 of `01..05-eeo-company-specific.xlsx`, segment id SEG4134880234), and `street_segments_annual_2026-10-01.csv`, column `power_services_rev`.

---

## 1. What the Street has for Power services

| Year | Power services $M | Growth | Power equipment $M | Power total $M | Power adj. EBITDA $M | Margin |
|---|---|---|---|---|---|---|
| FY22 actual | 11,228 | | 4,896 | 16,124 | 1,655 | 10.3% |
| FY23 actual | 11,838 | +5.4% | 5,598 | 17,436 | 1,722 | 9.9% |
| FY24 actual | 12,419 | +4.9% | 5,708 | 18,127 | 2,268 | 12.5% |
| FY25 actual (as reported / recast) | 13,081 / 13,187 | +5.3% | 6,686 | 19,767 / 19,873 | 2,902 | 14.7% |
| H1'26 actual | 6,598 (vs 6,238 recast) | +5.8% | 3,851 | 10,449 | 1,842 | 17.6% |
| FY26 (H1 actual + Street H2) | 14,259 | +8.1% | 9,341 | 23,608 | 4,418 | 18.7% |
| FY27 Street | 15,675 | +9.9% | 12,151 | 28,121 | 5,906 | 21.0% |
| FY28 Street | 17,665 | +12.7% | 15,888 | 33,521 | 7,810 | 23.3% |
| FY29 Street | 19,711 | +11.6% | 19,256 | 39,522 | 9,983 | 25.3% |
| FY30 Street | 22,357 | +13.4% | 23,469 | 45,215 | 12,174 | 26.9% |

- Actuals: Power MD&A tables in 10-K24 (FY22-FY24), 10-K25 (FY25), 10-Q2'26 p.29 (H1). Recast FY25 services = 13,081 + 106 (Power revenue recast 19,873 vs 19,767; H1 services recast +53: 6,238 vs 6,185). The recast Q3'25 and Q4'25 services figures (3,119 and 3,828) are estimates: reported 3,094 and 3,802 plus the quarterly recast of about 25-27.
- Street compound growth: FY25 recast to FY30 = 11.1% a year; FY26 to FY30 = 11.9% a year. Reported growth FY22-FY25 = 5.2% a year (4.9% to 5.4% each year).
- Street by quarter, year on year: Q3'26 +8.7% (mean 3,389; median 3,329 = +6.7%; low 3,167; high 3,737, from `06_modl.xlsx` row 25), Q4'26 +11.6%, Q1'27 +11.0%, Q2'27 +10.2%, Q3'27 +9.6%, Q4'27 +9.2%.
- Contributor counts for division lines are not shown on these exports. Sign that the set of brokers changes: Street Power services Q1'31 is 4,987 against Q1'30 4,880 (+2.2%), after +12% a year in 2029-2030; the Power RPO line steps from 162.8B (Q4'28) to 182.0B (Q1'29) and from 198.5B (Q4'30) to 171.8B (Q1'31). So 2029-2030 division lines come from a smaller, different set than 2027-2028.

## 2. The company's own services path

IU25 slide 28, title "A valuable asset ... the Power services annuity stream":

| Item | 2025E | 2035E |
|---|---|---|
| Total Gas Power and Steam Power services revenue | about $12B | about $22B (+$10B); the CEO said "at least $22 billion" |
| Installed HA units | about 125 | about 400 |
| Installed HA GW | about 50 | about 150 |
| HA services revenue per year | about $1B | about $4B |
| Upgrades | | "at least 50% growth '25 to '30+" |
| Slide sub-title | | services revenue "accelerating in the 2030s" |

Other statements at the same event (transcript):
- Press release: "More profitable, recurring Gas Power services revenue beginning in the 2030s."
- CEO: gas equipment is delivered between now and 2030 and the first major outage comes four or five years after delivery; orders taken today ship in 2029-2030 and reach their first outage about 2035.
- CEO, asked whether the figure could reach the $30Bs: the 2035 figure is a "financial floor"; "we should expect a higher services revenue base in 2026 and 2027 and 2028"; "I don't think we're ready to ... quantify that number".
- A sell-side analyst at the event put the existing $12B at about $16B by 2035 on escalation alone, with the doubled base taking it above $30B around 2038-2040.
- CEO: growing services from $12B to $22B "takes a lot of heavy-duty supply chain output"; outage numbers grow "substantially in the middle of the next decade".
- Laguna, September 2026 (secondary source): the CEO called the $12B to $22B path conservative; HA services about $1B today; 130 HA units running and 195 more under contract; about $500M of service revenue per GW of HA over the first 20 years.

Arithmetic on the chart:
- $12B to $22B over ten years = (22/12)^(1/10) - 1 = 6.25% a year.
- Other Power services (nuclear, hydro) in 2025 = 13.19 - 12.0 = about $1.2B.

| Year | Gas+steam, constant 6.25% | Gas+steam, straight line (+$1B a year) | Nuclear+hydro services at 6% to 13% a year | Total Power services $B | Street $B | Chart path vs Street |
|---|---|---|---|---|---|---|
| 2026 | 12.75 | 13.0 | 1.26-1.34 | 14.0-14.3 | 14.26 | -1.8% to +0.6% |
| 2027 | 13.55 | 14.0 | 1.33-1.52 | 14.9-15.5 | 15.67 | -5.1% to -1.0% |
| 2028 | 14.39 | 15.0 | 1.41-1.71 | 15.8-16.7 | 17.67 | -10.5% to -5.4% |
| 2029 | 15.29 | 16.0 | 1.50-1.94 | 16.8-17.9 | 19.71 | -14.8% to -9.0% |
| 2030 | 16.25 | 17.0 | 1.59-2.19 | 17.8-19.2 | 22.36 | -20.2% to -14.2% |

- Street 2030 Power services ($22.4B) less $1.6B to $3.0B for nuclear and hydro services leaves gas+steam services of $19.4B to $20.8B. On the company's chart that level is reached in 2032-2034. The Street is about three to four years ahead of the chart, and its 2030 total equals the chart's 2035 figure.
- If the Street's 2030 figure and the chart's 2035 figure were both right, gas+steam services would grow 1% to 2.5% a year in 2030-2035, the period the company says growth accelerates.
- Limits: the chart figure is a floor ("at least"), the CEO has called it conservative, and the company declined to quantify 2026-2028.

## 3. Component build from Note 9 (contractual service agreements)

Note 9 of each 10-Q and 10-K gives revenue recognised and billings on contractual service agreements (all in Power), in one sentence with no XBRL tag.

| Period | Power services $M | CSA revenue recognised $M | CSA billings $M | Change in estimated profitability $M | Non-CSA services $M (services less CSA revenue) |
|---|---|---|---|---|---|
| FY23 | 11,838 | 4,658 | 5,047 | +34 | 7,180 |
| FY24 | 12,419 | 5,473 (+17.5%) | 5,021 | -319 | 6,946 (-3.3%; part of Steam sold in 2024) |
| FY25 | 13,081 | 5,412 (-1.1%) | 5,362 | -151 | 7,669 (+10.4%) |
| H1'25 | 6,238 recast | 2,720 | 2,533 | -42 | 3,518 |
| H1'26 | 6,598 | 2,689 (-1.1%) | 2,392 (-5.6%) | -218 | 3,909 (+11.1%) |

- CSA revenue by quarter, Q1'24 to Q2'26: 1,174 / 1,363 / 1,173 / 1,763 / 1,261 / 1,459 / 1,104 / 1,588 / 1,280 / 1,409.
- CSA revenue has not grown for ten quarters. All growth is in non-CSA services (transactional parts, repairs and upgrades, steam, aeroderivative, nuclear, hydro).
- Open question: whether the profitability revisions are netted inside reported services revenue. If they are, non-CSA growth is +7.6% (FY25) and +15.9% (H1'26). The range used below is 11% to 16%.
- 10-K25 (Item 1): about 7,000 gas turbines installed, about 1,800 under long-term service agreements, average remaining contract life about 10 years; 126 HA units installed, 43 being installed and commissioned, 51 in RPO.

Scenarios (FY26 base = H1 actual + H2'25 recast grown at the scenario rates; CSA flat in H2'26):

| CSA growth | Non-CSA growth | 2027 | 2028 | 2029 | 2030 | 2030 vs Street |
|---|---|---|---|---|---|---|
| 0% | 11% | 14,963 | 16,017 | 17,186 | 18,485 | -17.3% |
| 2.5% | 11% | 15,097 | 16,289 | 17,600 | 19,044 | -14.8% |
| 2.5% | 13% | 15,366 | 16,784 | 18,373 | 20,153 | -9.9% |
| 5% | 13% | 15,500 | 17,063 | 18,807 | 20,754 | -7.2% |
| 2.5% | 15% | 15,638 | 17,294 | 19,182 | 21,335 | -4.6% |
| 5% | 15% | 15,773 | 17,574 | 19,616 | 21,936 | -1.9% |
| 5% | 16% | 15,910 | 17,834 | 20,035 | 22,555 | +0.9% |
| Street | | 15,675 | 17,665 | 19,711 | 22,357 | |

- To reach the Street's 2030 figure, non-CSA services must compound at 15.5% (CSA +5% a year) to 17.6% (CSA flat) for four years from FY26.
- FY27: the component range is 14,963 to 15,773 against Street 15,675 (-4.5% to +0.6%). No gap in FY27.

HA cross-check: $500M per GW over 20 years = $25M per GW a year. 130 units x about 0.4 GW = 52 GW = $1.3B a year (company: about $1B). An average of 200 to 240 HA units running in 2030 gives 80 to 96 GW = $2.0B to $2.4B at the 20-year average rate, and less in early years because revenue follows cost and the first major outage comes four or five years after start-up. So HA adds at most about $1.1B by 2030. The Street's rise from FY25 recast to 2030 is $9.2B. The other $8.1B would have to come from the existing fleet and from steam, aeroderivative, nuclear and hydro services: $12.1B to $20.2B, +67% in five years (10.8% a year), against 5.2% a year for total Power services in FY22-FY25.

## 4. Where the two methods land

| Period | Street $M | Chart path $B | Component build $B | Combined range $B | Central $B | Central gap |
|---|---|---|---|---|---|---|
| FY27 | 15,675 | 14.9-15.5 | 15.0-15.8 | 14.9-15.8 | 15.3 | -2% (no gap) |
| FY28 | 17,665 | 15.8-16.7 | 16.0-17.1 (to 17.6 at 15% non-CSA) | 15.8-17.1 | 16.5 | -6.6% |
| FY29 | 19,711 | 16.8-17.9 | 17.2-18.8 | 16.8-18.8 | 17.9 | -9% |
| FY30 | 22,357 | 17.8-19.2 | 18.5-20.8 (to 21.9 at 15% non-CSA) | 17.8-20.8 | 19.3 | -14% |

EBITDA effect (services gap x 35% to 50%; company services gross margin was 31.6% in H1'26, and the incremental gross margin on services H1'26 vs H1'25 was 350/677 = 52%):

| Year | Services gap $B | EBITDA effect $B | Share of Street Power EBITDA | Share of Street GEV EBITDA | Street Power margin | Power margin after the change |
|---|---|---|---|---|---|---|
| FY28 | 0.8 to 1.7 | 0.27 to 0.83 | 3% to 11% (7,810) | 2% to 7% (12,553) | 23.3% | 21.9% to 23.0% |
| FY30 | 2.2 to 4.1 | 0.76 to 2.03 | 6% to 17% (12,174) | 4% to 10% (19,544) | 26.9% | 24.6% to 26.5% |

- FY28 tie-out: the company framework is Power revenue at a high-teens growth rate from FY25 (19,767 x 1.17^3 to 1.19^3 = $31.7B to $33.3B) and a 22% margin ($7.0B to $7.3B). Street is $33.5B and 23.3% ($7.8B). Street equipment ($15.9B) is about what the framework leaves after chart-path services ($31.7-33.3B less $15.8-16.7B = $15.0B to $17.5B). The Street's excess over the framework sits in services.
- Growth effect: Street GEV EBITDA 12,553 (FY28) to 19,544 (FY30) is 24.8% a year. With FY28 lower by about $0.5B and FY30 by about $1.4B it is about 22.7% a year ((18,144 / 12,053)^0.5 - 1). The FY30 row above uses $18.3B to $20.2B, the centre of the combined range.

## 5. Near-term checks that showed no gap

| Line | Street | Arithmetic | Result |
|---|---|---|---|
| Power services Q3'26 | 3,389 mean, 3,329 median | CSA 1,104 x 0.95-1.05, non-CSA 2,015 x 1.11-1.16 = 3,286 to 3,496 | inside |
| Power services Q4'26 | 4,272 (+11.6%) | CSA 1,588 x 0.95-1.05, non-CSA 2,240 x 1.11-1.16 = 3,995 to 4,265 | -0.2% to -6.5%, central -3.3% |
| Power services Q3'26-Q2'27 | 14,955 (+10.4%) | CSA 5,381 x 1.00-1.05, non-CSA 8,164 x 1.11-1.16 = 14,443 to 15,120 | -3.4% to +1.1% |
| Power services FY27 | 15,675 | 14,963 to 15,773 | -4.5% to +0.6% |
| Q4 share of the year | 30.0% (FY26), 29.8% (FY27) | 29.3% (FY24), 29.1% (FY25) | consistent |

## 6. Services RPO schedule (company-wide; Power is 82% of services RPO)

A = services RPO x share due within one year. S = services revenue in the next four quarters. B = S - A (work booked and delivered inside the year).

| As of | Services RPO $M | 1-yr share | A $M (rounding band) | S $M | S / A | B $M | Basis | Years 2-5 scheduled, per year $M |
|---|---|---|---|---|---|---|---|---|
| 12/31/23 | 75,120 | 16% | 12,019 (11,644-12,395) | 15,982 | 1.330 | 3,963 | reported | 6,573 |
| 3/31/24 | 74,083 | 16% | 11,853 | 16,175 | 1.365 | 4,322 | reported | 6,667 |
| 6/30/24 | 73,915 | 17% | 12,566 | 16,382 | 1.304 | 3,816 | reported | 6,468 |
| 9/30/24 | 75,678 | 17% | 12,865 | 16,848 | 1.310 | 3,983 | reported | 6,622 |
| 12/31/24 | 75,976 | 18% | 13,676 | 17,134 | 1.253 | 3,458 | reported | 6,648 |
| 3/31/25 | 77,959 | 18% | 14,033 | 17,383 | 1.239 | 3,350 | reported | 6,821 |
| 6/30/25 | 78,938 | 17% | 13,419 | 17,811 | 1.327 | 4,392 | reported | 7,104 |
| 9/30/25 | 81,177 | 17% | 13,800 | 18,207 | 1.319 | 4,407 | 1 quarter Street | 7,306 |
| 12/31/25 | 85,993 | 17% | 14,619 | 18,843 | 1.289 | 4,225 | 2 quarters Street | 7,524 |
| 3/31/26 | 87,352 | 16% | 13,976 | 19,296 | 1.381 | 5,319 | 3 quarters Street | 8,080 |
| 6/30/26 | 88,463 | 16% | 14,154 (13,712-14,596) | 19,790 | 1.398 (1.356-1.443) | 5,636 | all Street | 8,404 |

- Seven reported windows: S / A between 1.239 and 1.365, mean 1.304. The Street's next four quarters need 1.398. At the mean ratio S = 18,454 (-6.8% vs Street); at the highest reported ratio 19,315 (-2.4%).
- Not returned as a candidate, for three reasons. The 16% is rounded (plus or minus 3.1% on A). The Power-only component check in section 5 shows no gap. Much of the excess is in the Street's Electrification services line (2,689 for the four quarters against about 2,135 trailing, +26%; H1'26 actual growth was +3%), which looks like noise in how brokers split equipment and services.
- Scheduled one-year conversion is growing slowly: average A for 12/31/25 to 6/30/26 is 14,250 against 13,709 a year earlier (+3.9%).
- Evidence for the Street: services scheduled for years 2-5 rose from $6.6B a year (12/31/24) to $8.4B a year (6/30/26), +26% in 18 months (+20% to +33% after rounding). Contracted work for mid-2027 to mid-2031 is building faster than revenue.
- Five-year test: Street services for the 20 quarters Q3'26-Q2'31 = $123.2B against $47.8B scheduled (2.58x). The same ratio for the 12/31/23 and 12/31/24 schedules, using actuals plus Street, is 2.51x and 2.63x. No information.

## 7. Adverse contract revisions (Note 9) and margin

| | FY23 | FY24 | FY25 | H1'25 | H1'26 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|---|---|
| Net change in estimated CSA profitability $M | +34 | -319 | -151 | -42 | -218 | -89 | -129 |
| Share of Power EBITDA | | 14.1% | 5.2% | 3.2% | 11.8% | 11.0% | 12.5% |
| Points of Power margin | | 1.8 | 0.8 | 0.5 | 2.1 | 1.8 | 2.4 |

- 10-K25 sensitivity: one point of lifetime CSA profitability = $0.2B. H1'26 = about 1.1 points. Forward run-rate cost = 1.1% x $5.4B of CSA revenue = about $59M a year (1% of Street FY27 Power EBITDA).
- H1'26 Power margin was 17.6%; without the revisions it was 19.3% to 19.7% ((1,842 + 218) / 10,667 or / 10,449, depending on whether the revisions also reduced revenue). Street FY27 is 21.0%.
- FY26 at the first-half pace would be about -$330M to -$450M. If FY27 revisions were zero the swing is +$0.33B to +$0.45B (3.5% to 4.8% of Street GEV FY27 EBITDA 9,471); if they doubled it is the same amount negative. The filings give no basis to call the direction (FY24 cited "higher costs"; later filings give no reason). No candidate. The Q3'26 10-Q and the FY26 10-K give the next two readings.

## 8. Effect on the equipment-schedule discrepancy (BLOOMBERG_VERDICT section 10)

Four earlier windows added (schedules from the Form 10 and the 2024 10-Qs):

| As of | Equipment scheduled $M | Next four quarters $M | Ratio | Services ratio | Total scheduled $M | Total next four quarters $M | Total ratio (ex-Prolec) |
|---|---|---|---|---|---|---|---|
| 12/31/23 | 20,644 (40,478 x 51%) | 18,952 | 0.918 | 1.330 | 32,663 | 34,934 | 1.070 |
| 3/31/24 | 18,994 (42,210 x 45%) | 19,532 | 1.028 | 1.365 | 30,848 | 35,707 | 1.158 |
| 6/30/24 | 19,534 (41,561 x 47%) | 20,232 | 1.036 | 1.304 | 32,099 | 36,614 | 1.141 |
| 9/30/24 | 19,352 (42,069 x 46%) | 20,822 | 1.076 | 1.310 | 32,217 | 37,670 | 1.169 |
| 12/31/24 | 18,941 | 20,934 | 1.105 | 1.253 | 32,616 | 38,068 | 1.167 |
| 3/31/25 | 20,465 | 21,991 | 1.075 (1.048) | 1.239 | 34,498 | 39,374 | 1.141 (1.126) |
| 6/30/25 | 20,879 | 23,556 | 1.128 (1.061) | 1.327 | 34,298 | 41,367 | 1.206 (1.165) |
| 6/30/26, Street | 31,616 | 30,245 | 0.957 | 1.398 | 45,770 | 50,019 | 1.093 |

- In the 12/31/23 window equipment revenue came in 8% below the schedule (0.918). Wind was about a third of equipment RPO then and is about 9% now ($8.0B of $87.8B). The statement "actual equipment revenue ran 5-11% above schedule in every reported window" holds for three windows, not for seven: the seven-window range is 0.92 to 1.13, and the Street's 0.957 is inside it.
- On total revenue the ratio is steadier: 1.126 to 1.169 in six windows and 1.070 in the 12/31/23 window. Street is 1.093. Six windows imply total revenue of $51.5B to $53.5B for Q3'26-Q2'27 (+3.0% to +7.0% vs Street 50,019); the 12/31/23 window implies $49.0B (-2.1%). Mean of seven (1.142): $52.3B (+4.5%). Rounding of the two shares adds plus or minus 1.9%.
- Mix: a schedule-consistent split of $52.96B is services $18.46B (34.9%) and equipment $34.50B, against the Street's 39.6% services share. With equipment gross margin 11.8% to 13.1% and services 31.6% to 32.6% (H1'26, Q2'26), the EBITDA effect of the extra revenue is -$0.16B to +$0.42B against Street EBITDA of $8,210M for the four quarters. Revenue above the Street, profit about in line, margin rate about 0.5 to 1.0 point lower.

## 9. Reveal dates and pass marks

| Date | Number reported | Reading that supports the Street path | Reading that supports the arithmetic |
|---|---|---|---|
| 2026-10-28 (Q3 call and 10-Q) | Power services Q3'26 (Street 3,389; +8.7%) and 9-month CSA revenue (3,824 last year) | services +9% or more; CSA revenue up | services +7% or less; CSA revenue at or below 3,824 |
| Late January 2027 (Q4, FY27 guide, 10-K) | Power services Q4'26 (Street 4,272; +11.6%); FY26 CSA revenue (5,412 in FY25); services RPO one-year share | Q4 +11% or more; CSA growth resumes at 5% or more; one-year scheduled services at $15.7B or more | Q4 +7% or less; CSA flat; one-year scheduled services near $14-14.6B |
| April and July 2027 | Power services Q1'27 and Q2'27 (Street +11.0%, +10.2%) | three straight quarters at +10% or more | growth stays at 6% to 8% |
| Spring 2027 capital markets day (date not set) | 2030 outlook | Power services for 2030 at $21B or more, or the 2035 figure raised to about $30B | 2030 Power services at $20B or less; 2035 figure left near $22B |

## 10. Reproduce

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
yr = lambda key, y: sum(d[f'{key}|{y} Q{i}'] for i in range(1, 5))
street = {y: yr('Total Revenue|Power|Services', y) for y in (2027, 2028, 2029, 2030)}
cagr = (22 / 12) ** 0.1 - 1                      # company chart, 2025E to 2035E
chart = {y: 12 * (1 + cagr) ** (y - 2025) for y in street}   # gas + steam services, $B
csa26 = 2689 + 1104 + 1588                       # H1'26 + H2'25 CSA revenue (Note 9)
non26 = (6598 - 2689) + ((3119 + 3828) - (1104 + 1588)) * 1.13
build = {y: csa26 * 1.025 ** (y - 2026) + non26 * 1.13 ** (y - 2026) for y in street}
A = 88463 * 0.16                                 # services RPO due within one year, 10-Q2'26
```

Files read: Bloomberg exports listed above; `gev.db` documents and sources tables (read-only); prior research BLOOMBERG_VERDICT.md, ROBUSTNESS_PACK.md, E03_model_inputs.md, 01_hidden_patterns_sweep/DIGEST.md (CSA series cross-check).
