# Backlog conversion vs Street revenue (lens: RPO schedule, equipment)

_AI-assisted research input only. Facts, arithmetic, tables and sources. The team writes every memo sentence, chooses every forecast number and chooses the direction. Bloomberg data is licensed for academic use: cite as "Bloomberg, 2026-10-01" and keep it inside the project folder._

Working date 2026-10-01. All figures $M unless stated. "Y1" = the dollar amount of equipment backlog that GEV says it will recognise within one year (equipment RPO x the "within 1 year" share). "Street" = Bloomberg BEst mean.

Scripts used (scratchpad, reproducible from the files below): `rpo_analysis.py`, `rpo_division.py`.

## 0. Result in four lines

| Item | Value |
|---|---|
| Line and period | Equipment revenue, four quarters Q3 2026 to Q2 2027 |
| Street | $30,245M (sum of the three division equipment lines) |
| GEV's own schedule (10-Q, 6/30/26) | $31,616M (36% of $87,821M; $31,176M to $32,055M allowing for rounding of the 36%) |
| Arithmetic range | $31.6B (schedule, no uplift) to $33.5B (schedule x the average uplift of the six post-spin windows); $32.9B at the seven-window average. That is +4.5% to +10.9% against the Street; +8.7% at the seven-window average |

Total-revenue effect about +2.7% to +6.6%. EBITDA effect about +2% to +8% of the four-quarter Street EBITDA ($8,210M). The back-test has one miss in seven windows (-8%), so the error band is close to the size of the gap.

## 1. Sources

| Data | Where |
|---|---|
| RPO note (equipment and services RPO, shares within 1, 2, 5 years) | Note 9 "Remaining Performance Obligation" in each 10-Q and 10-K: accessions 0001996810-24-000008, -24-000067, -24-000083, -25-000011, -25-000073, -25-000133, -25-000160, -26-000015, -26-000064, -26-000148. 12/31/23 values from the Information Statement, 8-K exhibit 99.1, 0001193125-24-063739 (page F-23) |
| Quarterly equipment and services revenue | XBRL `RevenueFromContractWithCustomerExcludingAssessedTax`, `ProductMember` / `ServiceMember`; `data/financials/gev_segments.csv` |
| Division equipment RPO | MD&A segment tables ("RPO / Equipment / Services / Total RPO") in each 10-Q and 10-K |
| Prolec revenue by quarter | 10-Q organic-revenue reconciliation, "Less: Acquisitions": Q1 2026 equipment $469M, services $17M; Q2 2026 equipment $834M, services $26M. Acquisition closed 2026-02-02 (Note 8) |
| Prolec backlog and plan | Acquisition presentation (corpus source 3788): about $4B equipment backlog at Q2 2025, revenue $3.0B (2025E), $3.4B (2026E), $4.2B (2028E) |
| Street by division and quarter | Bloomberg EEO "Company-Specific" exports, `GEV_Pull_2026-10-01/01-eeo-company-specific.xlsx` to `05-...xlsx`, sheet "Multiple Periods": row 24 Power equipment, row 27 Wind equipment, row 30 Electrification equipment, rows 25 / 28 / 31 services, row 22 total revenue, row 9 EBITDA, row 19 wind MW delivered; columns F to I are the four forward quarters in each file. Same data in `segment_quarterly.json` |
| Guidance | Q2 2026 call transcript (corpus source 3161); Q2 2026 release; Morgan Stanley Laguna conference 2026-09-16 (corpus sources 681, 3750) |

## 2. The RPO note, every period since the spin

| As of | Equipment RPO | Within 1 yr | Within 2 yrs | Within 5 yrs | Y1 = RPO x 1-yr share | Services RPO | Within 1 yr |
|---|---|---|---|---|---|---|---|
| 12/31/23 | 40,478 | 51% | 77% | 100% | 20,644 | 75,120 | 16% |
| 3/31/24 | 42,210 | 45% | 71% | 93% | 18,994 | 74,083 | 16% |
| 6/30/24 | 41,561 | 47% | 69% | 91% | 19,534 | 73,915 | 17% |
| 9/30/24 | 42,069 | 46% | 70% | 91% | 19,352 | 75,678 | 17% |
| 12/31/24 | 43,047 | 44% | 69% | 93% | 18,941 | 75,976 | 18% |
| 3/31/25 | 45,478 | 45% | 71% | 91% | 20,465 | 77,959 | 18% |
| 6/30/25 | 49,712 | 42% | 70% | 92% | 20,879 | 78,938 | 17% |
| 9/30/25 | 54,092 | 41% | 71% | 97% | 22,178 | 81,177 | 17% |
| 12/31/25 | 64,245 | 37% | 69% | 97% | 23,771 | 85,993 | 17% |
| 3/31/26 | 75,924 | 38% | 69% | 98% | 28,851 | 87,352 | 16% |
| **6/30/26** | **87,821** | **36%** | **65%** | **97%** | **31,616** | 88,463 | 16% |

- The share within one year fell from 42% to 36% in a year. The dollar amount rose from $20,879M to $31,616M (+51%). Prolec's backlog (about $4B at acquisition) is inside the 3/31/26 and 6/30/26 figures.
- The 12/31/23 line comes from the pre-spin carve-out statements. Its five-year share (100%) dropped to 93% one quarter later, and the one-year share from 51% to 45%, so the method or the scope changed between those two dates.

Quarterly revenue used (consolidated, $M):

| | Q1 24 | Q2 24 | Q3 24 | Q4 24 | Q1 25 | Q2 25 | Q3 25 | Q4 25 | Q1 26 | Q2 26 |
|---|---|---|---|---|---|---|---|---|---|---|
| Equipment | 3,617 | 4,194 | 5,290 | 5,851 | 4,197 | 4,894 | 5,880 | 5,963 | 5,254 | 6,459 |
| of which Prolec | | | | | | | | | 469 | 834 |
| Services | 3,642 | 4,010 | 3,623 | 4,707 | 3,835 | 4,217 | 4,089 | 4,993 | 4,084 | 4,645 |

Street forward quarters (Bloomberg, 2026-10-01; segment basis, which includes about $30-45M a quarter of intersegment sales):

| | Q3 26 | Q4 26 | Q1 27 | Q2 27 | Q3 27 | Q4 27 | Q1 28 | Q2 28 |
|---|---|---|---|---|---|---|---|---|
| Power equipment | 2,394 | 3,097 | 2,585 | 2,798 | 3,025 | 3,743 | 3,445 | 3,654 |
| Wind equipment | 1,789 | 1,763 | 1,019 | 1,259 | 1,616 | 1,469 | 847 | 1,034 |
| Electrification equipment | 3,299 | 3,479 | 3,071 | 3,692 | 3,910 | 4,196 | 3,733 | 4,465 |
| **Equipment, sum** | **7,482** | **8,339** | **6,675** | **7,748** | 8,551 | 9,408 | 8,024 | 9,153 |
| Services, sum | 4,485 | 5,629 | 4,536 | 5,139 | 5,037 | 6,173 | 5,113 | 5,730 |
| Total revenue (headline consensus) | 11,993 | 13,915 | 11,143 | 12,968 | 13,581 | 15,404 | 13,053 | 14,808 |
| EBITDA | 1,672 | 2,500 | 1,810 | 2,228 | 2,345 | 3,008 | 2,625 | 3,004 |

## 3. Back-test: scheduled conversion against the next four quarters

Formula: ratio = (equipment revenue of the next four quarters, less Prolec revenue when the backlog date is before the acquisition) / Y1.

| Backlog date | Y1 | Y1 range (share +/-0.5 pt) | Next four quarters | Quarters that are Street | Prolec removed | Ratio | Revenue less Y1 |
|---|---|---|---|---|---|---|---|
| 12/31/23 | 20,644 | 20,441-20,846 | 18,952 | 0 | 0 | **0.918** | -1,692 |
| 3/31/24 | 18,994 | 18,783-19,206 | 19,532 | 0 | 0 | **1.028** | +538 |
| 6/30/24 | 19,534 | 19,326-19,741 | 20,232 | 0 | 0 | **1.036** | +698 |
| 9/30/24 | 19,352 | 19,141-19,562 | 20,822 | 0 | 0 | **1.076** | +1,470 |
| 12/31/24 | 18,941 | 18,725-19,156 | 20,934 | 0 | 0 | **1.105** | +1,993 |
| 3/31/25 | 20,465 | 20,238-20,692 | 21,991 | 0 | 469 | **1.052** | +1,057 |
| 6/30/25 | 20,879 | 20,630-21,128 | 23,556 | 0 | 1,303 | **1.066** | +1,374 |
| 9/30/25 | 22,178 | 21,907-22,448 | 25,158 | 1 | 2,153 (850 assumed for Q3 26) | 1.037 | +827 |
| 12/31/25 | 23,771 | 23,449-24,092 | 27,534 | 2 | 3,003 (850 a quarter assumed for H2 26) | 1.032 | +761 |
| 3/31/26 | 28,851 | 28,472-29,231 | 28,956 | 3 | 0 (Prolec is in the backlog) | 1.004 | +104 |
| **6/30/26** | **31,616** | **31,176-32,055** | **30,245** | 4 | 0 | **0.957** | **-1,371** |

Statistics on the seven fully reported windows:

| Sample | Mean ratio | Std dev | Min | Max |
|---|---|---|---|---|
| All seven | 1.040 | 0.060 | 0.918 | 1.105 |
| Six post-spin windows (from 3/31/24) | 1.061 | 0.028 | 1.028 | 1.105 |

- The Street's ratio for the current window (0.957) is 1.4 standard deviations below the seven-window mean and 3.7 below the post-spin mean.
- The windows overlap (a new one starts every quarter), so there are only about two independent years of data.
- The one miss (12/31/23 window, -8.2%): (a) pre-spin schedule, revised sharply one quarter later; (b) the Steam nuclear business sold to EDF in Q2 2024 (10-K 2024, Note 3) carried $3,708M of equipment RPO at 12/31/23 (10-K 2024 MD&A: "a reduction of approximately $3.9 billion"; investor-update reconciliation, corpus source 1844), and its revenue left the accounts for the rest of the window; (c) offshore wind stopped after the July 2024 blade failure.

Implied equipment revenue for Q3 2026 to Q2 2027:

| Method | Multiplier on Y1 | Implied $M | vs Street 30,245 |
|---|---|---|---|
| Rounding floor (35.5%), no uplift | 0.986 | 31,176 | +3.1% |
| Schedule as stated, no uplift | 1.000 | 31,616 | +4.5% |
| Seven-window mean less one std dev | 0.980 | 30,996 | +2.5% |
| Lowest post-spin window | 1.028 | 32,510 | +7.5% |
| Seven-window mean | 1.040 | 32,884 | +8.7% |
| Post-spin mean | 1.061 | 33,527 | +10.9% |
| Seven-window mean plus one std dev | 1.100 | 34,771 | +15.0% |
| A repeat of the 12/31/23 miss | 0.918 | 29,024 | -4.0% |

## 4. Windows still in progress

Share of Y1 already reported at the same stage (Prolec removed where the backlog date is before the acquisition):

| Stage | Window | Share of Y1 reported so far | How the window ended |
|---|---|---|---|
| After 3 quarters | 9/30/24 | 77.2% | 1.076 |
| After 3 quarters | 9/30/25 | 73.8% | open (Street Q3 26 gives 1.037) |
| After 2 quarters | 12/31/23 | 37.8% | 0.918 |
| After 2 quarters | 12/31/24 | 48.0% | 1.105 |
| After 2 quarters | 12/31/25 | 43.8% | open (Street H2 26 gives 1.032) |
| After 1 quarter | 3/31/24 | 22.1% | 1.028 |
| After 1 quarter | 3/31/25 | 23.9% | 1.052 |
| After 1 quarter | 3/31/26 | 22.4% | open (Street gives 1.004) |

Reading: the open windows run a little behind the 2025 windows and well ahead of the 12/31/23 window. They point to an uplift of about 2-4%, not 6-10%.

## 5. Where the gap sits by quarter

Change in Y1 between two schedules, against the change in the quarter that enters and the quarter that leaves:

| Schedules | Change in Y1 | Quarter in less quarter out | Y1 change less swap |
|---|---|---|---|
| 3/31/24 to 6/30/24 | +539 | Q2 25 less Q2 24 = +700 | -161 |
| 6/30/24 to 9/30/24 | -182 | Q3 25 less Q3 24 = +590 | -772 |
| 9/30/24 to 12/31/24 | -411 | Q4 25 less Q4 24 = +112 | -523 |
| 12/31/24 to 3/31/25 | +1,524 | Q1 26 less Q1 25 = +1,057 | +467 |
| 3/31/25 to 6/30/25 | +414 | Q2 26 less Q2 25 = +1,565 | -1,151 |
| 6/30/25 to 9/30/25 | +1,299 | Q3 26 (Street) less Q3 25 = +1,602 | -303 |
| 9/30/25 to 12/31/25 | +1,593 | Q4 26 (Street) less Q4 25 = +2,376 | -783 |
| 12/31/25 to 3/31/26 | +5,080 (about +$3B is Prolec's backlog) | Q1 27 (Street) less Q1 26 = +1,421 | +3,659 (about +0.6B after Prolec) |
| 3/31/26 to 6/30/26 | +2,764 | Q2 27 (Street) less Q2 26 = +1,289 | **+1,475** |

- Up to the 12/31/25 schedule the Street's quarters keep pace with the schedule. The shortfall opens with the Street's Q1 2027 and Q2 2027.
- Halves: Street H2 2026 equipment $15,821M; Street H1 2027 $14,424M; H1 2026 actual $11,713M.
- If H2 2026 lands on the Street (which matches the FY26 guide, see below), the schedule leaves 31,616 - 15,821 = **$15,795M for H1 2027 from the 6/30/26 backlog alone, +9.5% against the Street's $14,424M**, before any order booked after June that ships by June 2027.

Split of Y1 between the two halves of a June window:

| June window | H2 share of Y1 | H1 (following year) share of Y1 | Total |
|---|---|---|---|
| 6/30/24 (actual) | 57.0% | 46.5% | 103.6% |
| 6/30/25 (actual, ex-Prolec) | 56.7% | 49.9% | 106.6% |
| 6/30/26 (Street) | 50.0% | 45.6% | 95.7% |

What management's July guide implied for H2 equipment, as a share of the June Y1 (H2 guide revenue less H2 services):

| Year | July guide for the year | Implied H2 revenue | H2 services | Implied H2 equipment | Share of June Y1 | Actual H2 equipment share |
|---|---|---|---|---|---|---|
| 2024 | "higher end of $34-35B" | 19,537 | 8,330 (actual) | 11,207 | 57.4% | 57.0% |
| 2025 | "higher end of $36-37B" | 19,857 | 9,082 (actual) | 10,775 | 51.6% | 56.7% (FY25 revenue $38,068M, $1.07B above the top of the guide) |
| 2026 | $45.5-46.5B | 25,058-26,058 | 10,114 (Street) | 14,944-15,944 | 47.3-50.4% | not yet reported |

Three outcomes are possible, and the filing does not say which:

| Outcome | What it needs | Reveal |
|---|---|---|
| A. H2 2026 beats the guide | H2 equipment at 53-57% of Y1 = $16.8-18.0B, FY26 revenue about $47.3-48.6B against a guide top of $46.5B | Q3 print 2026-10-28; Q4 print late January 2027 |
| B. H2 2026 on guide, H1 2027 above the Street | H1 2027 equipment of at least $15.8B against $14.4B | FY27 guide on the January call; Q1 print late April 2027; Q2 print late July 2027 |
| C. GEV misses its own schedule | At least $1.4B (4.3%) of the scheduled amount slips past June 2027 and nothing books and ships inside the window | The same prints. Happened once in seven windows |

Management's own Q3 guide (Power revenue +17-19%, Electrification $3.8-4.0B, Wind down low double digits) rebuilds to about $11.7-12.1B of revenue, in line with the Street's $11,993M. That makes outcome A less likely for Q3 itself and points to Q4 2026 or H1 2027.

## 6. By division

Division equipment RPO at 6/30/26 (10-Q MD&A): Power $39,261M, Wind $8,197M, Electrification $40,589M (sum $88,047M; consolidated $87,821M). GEV does not give the one-year share by division, so the split of the $31.6B cannot be read from the filings. What can be done is a bound.

Turnover = next-four-quarter division equipment revenue / division equipment RPO at the start:

| Backlog date | Power | Wind | Electrification | Electrification ex-Prolec | Quarters that are Street |
|---|---|---|---|---|---|
| 12/31/23 | 40.4% | 58.5% | 40.9% | 40.9% | 0 |
| 3/31/24 | 39.9% | 62.5% | 37.6% | 37.6% | 0 |
| 6/30/24 | 53.9% | 63.3% | 34.1% | 34.1% | 0 |
| 9/30/24 | 54.5% | 65.9% | 35.3% | 35.3% | 0 |
| 12/31/24 | 51.5% | 67.4% | 36.4% | 36.4% | 0 |
| 3/31/25 | 49.4% | 69.3% | 38.2% | 36.1% | 0 |
| 6/30/25 | 45.7% | 64.9% | 41.2% | 35.8% | 0 |
| 9/30/25 | 42.7% | 67.3% | 42.1% | 34.0% | 1 |
| 12/31/25 | 37.7% | 64.0% | 40.6% | 30.7% | 2 |
| 3/31/26 | 35.2% | 67.0% | 33.6% | 33.6% | 3 |
| **6/30/26 (Street)** | **27.7%** | **71.1%** | **33.4%** | 33.4% | 4 |

Bound on the split (Y1 = 31,616; Street: Power 10,874, Wind 5,830, Electrification 13,541):

| If Wind converts this share of its equipment RPO in a year | Wind Y1 | Power + Electrification Y1 | vs Street Power + Electrification 24,415 |
|---|---|---|---|
| 55% | 4,508 | 27,107 | +11.0% (+2,692) |
| 60% | 4,918 | 26,697 | +9.3% (+2,282) |
| 65% | 5,328 | 26,288 | +7.7% (+1,873) |
| 71.1% (the Street's own Wind figure; above every reported window) | 5,828 | 25,787 | +5.6% (+1,373) |

- Wind cannot hold the gap: the Street already has Wind converting a larger share of its backlog than in any reported window. So the shortfall against the schedule is in Power and Electrification together, at least $1.4B and up to about $2.7B before any uplift.
- Between Power and Electrification the split is not identified. Example: with Electrification at 36% and Wind at 60-67%, Power's scheduled amount is $11.5-12.1B (29-31% of its RPO) against a Street of $10.9B. With Electrification at 38% and Wind at 67%, Power is $10.7B, equal to the Street.
- Street organic growth for Electrification equipment over the four quarters is about +17% ((13,541 - about 3,500 Prolec) / (9,869 - 1,303)). Reported organic growth was +39% in Q1 2026 and +37% in Q2 2026 (segment equipment 3,130 less 834 against 1,673). Management's Q3 guide ($3.8-4.0B) implies about +13-20% organic for the segment.
- Physical cross-check: gas shipments are guided at 5 GW a quarter from Q3 2026 and 6 GW a quarter in H2 2027 (20 GW over the four quarters against 14.6 GW in the last four: 4.0, 3.1, 4.2, 3.3). A rough build (Power equipment +37% volume and +5-15% price and mix; Electrification organic +28-36% plus Prolec $3.4-3.6B; Wind $5.3-5.8B) gives $30.3-32.7B. The Street sits at the low end of that range and the schedule near the middle.

### Wind: a second, smaller check that goes the other way

Implied equipment orders = change in division equipment RPO + division equipment revenue (GEV does not publish equipment orders in dollars by division in the 10-Q).

| Half | Wind implied equipment orders $M | Wind orders, GW (10-Q units table) | Wind equipment revenue two halves later $M | Offshore revenue in that half $M | Onshore equipment / orders (k) | GW sold / GW ordered |
|---|---|---|---|---|---|---|
| H1 2024 | 2,325 | 2.5 | H1 2025: 3,192 | 429 | 1.19 | 3.0 / 2.5 = 1.20 |
| H2 2024 | 2,704 | 2.7 | H2 2025: 4,032 | 223 | 1.41 | 3.9 / 2.7 = 1.44 |
| H1 2025 | 2,203 | 1.8 | H1 2026: 2,283 | 551 | 0.79 | 2.0 / 1.8 = 1.11 |
| H2 2025 | 3,413 | 3.1 | H2 2026 (Street): 3,552 | 334 (Street) | 0.94 | 3.28 / 3.1 = 1.06 (Street) |
| **H1 2026** | **1,368** | **1.2** | **H1 2027 (Street): 2,278** | 390 (Street) | **1.38 needed** | **1.88 / 1.2 = 1.57 needed** |

- H1 2026 wind orders fell 33% in GW (1.2 against 1.8) and 44% in units (342 against 609). The Street has H1 2027 wind equipment revenue flat on H1 2026 (2,278 against 2,284).
- Management ties deliveries to orders a year earlier (Q2 2026 call: "70% of 2025 equipment orders were in the second half and will be delivered in the second half of 2026"; Q2 2026 release: lower deliveries "as a result of soft orders in the first half of 2025").
- With k of 0.79-1.19 and the Street's own offshore figure: H1 2027 wind equipment = 1,368 x k + 390 = $1.47-2.02B, which is -11% to -35% against the Street. With the single highest k on record (1.41, when the 2023 backlog was still being delivered) the Street's number is reachable.
- Profit effect is small: $0.26-0.8B less revenue at an assumed 10-20% contribution is about -$30M to -$160M, against a Street H1 2027 EBITDA of $4,038M and a Street H1 2027 Wind adjusted EBITDA of -$21M.
- Offsets: management expects H2 2026 onshore orders "materially higher" than H1 (Laguna, 2026-09-16); some could ship by June 2027.

## 7. Services schedule

| Backlog date | Services RPO x 1-yr share | Next four quarters services | Ratio to schedule | Turnover on services RPO | Street quarters |
|---|---|---|---|---|---|
| 12/31/23 | 12,019 | 15,982 | 1.330 | 21.3% | 0 |
| 3/31/24 | 11,853 | 16,175 | 1.365 | 21.8% | 0 |
| 6/30/24 | 12,566 | 16,382 | 1.304 | 22.2% | 0 |
| 9/30/24 | 12,865 | 16,848 | 1.310 | 22.3% | 0 |
| 12/31/24 | 13,676 | 17,134 | 1.253 | 22.6% | 0 |
| 3/31/25 | 14,033 | 17,383 | 1.239 | 22.3% | 0 |
| 6/30/25 | 13,419 | 17,811 | 1.327 | 22.6% | 0 |
| 9/30/25 | 13,800 | 18,207 | 1.319 | 22.4% | 1 |
| 12/31/25 | 14,619 | 18,843 | 1.289 | 21.9% | 2 |
| 3/31/26 | 13,976 | 19,296 | 1.381 | 22.1% | 3 |
| 6/30/26 | 14,154 | 19,790 | 1.398 | 22.4% | 4 |

- The one-year share is rounded to a whole percent on a base of $75-88B, so each point is $0.75-0.9B. The ratio to schedule is too noisy to use (16% against 17% moves it by 6%).
- On turnover the Street's services ($19,790M, 22.4% of services RPO) is inside the reported range (21.3-22.6%). **No gap in services.** So the total-revenue gap equals the equipment gap.

## 8. Total revenue and EBITDA for the four quarters

Street: total revenue $50,019M (22-28 analysts), services $19,790M, EBITDA $8,210M. The division lines sum to within $16M of the headline total, so the equipment and services split is consistent with the headline consensus.

| Case | Extra equipment revenue | Total revenue | vs Street | EBITDA at 13% | at 18% | at 20.5% |
|---|---|---|---|---|---|---|
| Schedule, no uplift | +1,371 | 51,389 | +2.7% | +178 (+2.2%) | +247 (+3.0%) | +281 (+3.4%) |
| Seven-window mean | +2,639 | 52,657 | +5.3% | +343 (+4.2%) | +475 (+5.8%) | +541 (+6.6%) |
| Post-spin mean | +3,282 | 53,301 | +6.6% | +427 (+5.2%) | +591 (+7.2%) | +673 (+8.2%) |

Drop-through rates and where they come from:
- 13%: consolidated equipment gross margin in Q2 2026 (equipment revenue 6,459, cost of equipment 5,613; XBRL `CostOfGoodsAndServicesSold`, `ProductMember`). Services gross margin in the same quarter was 32.6%.
- 18%: change in equipment gross profit over change in equipment revenue, H1 2026 against H1 2025 (revenue +2,622, cost +2,147).
- 20.5%: Street division EBITDA margins for the four quarters (Power 20.0%, Electrification 19.3%), an upper bound because equipment earns less than services.
- More equipment in the mix lowers the company margin percentage slightly even as EBITDA dollars rise.

## 9. Year two and calendar 2027

Two-year schedule (Y2 = RPO x (2-yr share less 1-yr share), for months 13-24):

| Backlog date | Y2 | Revenue in months 13-24 | Ratio | Revenue less Y2 ("fill") | Street quarters in months 13-24 |
|---|---|---|---|---|---|
| 12/31/23 | 10,524 | 20,934 | 1.99 | 10,410 | 0 |
| 3/31/24 | 10,975 | 21,991 | 2.00 | 11,016 | 0 |
| 6/30/24 | 9,143 | 23,556 | 2.58 | 14,413 | 0 |
| 9/30/24 | 10,097 | 25,158 | 2.49 | 15,062 | 1 |
| 12/31/24 | 10,762 | 27,534 | 2.56 | 16,773 | 2 |
| 3/31/25 | 11,824 | 28,956 | 2.45 | 17,131 | 3 |
| 6/30/25 | 13,919 | 30,245 | 2.17 | 16,326 | 4 |
| 9/30/25 | 16,228 | 31,314 | 1.93 | 15,087 | 4 |
| 12/31/25 | 20,558 | 32,383 (Street 2027) | 1.58 | 11,825 | 4 |
| 3/31/26 | 23,536 | 33,732 | 1.43 | 10,196 | 4 |
| 6/30/26 | 25,468 | 35,137 | 1.38 | 9,669 | 4 |

(The fill figures from 3/31/24 to 12/31/25 include $0.5-3.5B of Prolec revenue that was not in the backlog at the start.)

- The Street's fill for year two falls from $10.4-13.1B (the three reported windows, ex-Prolec) to $8-10B while equipment orders run two to three times higher. That is consistent with customers ordering earlier, which moves revenue out of "fill" and into the schedule. It is not proof of a gap. **Year two: no finding.**
- Calendar 2027 equipment, Street $32,383M (Power 12,151, Wind 5,363, Electrification 14,869). Built as H1 2027 (from section 5: $14.8-17.1B depending on whether H2 2026 beats) plus H2 2027 (Street $17,959M, or $18.3B with fill at the lowest reported dollar level): $32.8-35.4B, which is +1% to +9%. On total 2027 revenue (Street $53,029M, 36 analysts) that is +0.8% to +5.7%, about +3% in the middle. **Under the 5% threshold: not a stand-alone candidate.**
- The 12/31/26 schedule in the 10-K (late January or early February 2027) will give the 2027 figure directly: Y1 at 12/31/26 against the Street's 2027 equipment revenue of $32,383M.
- Street 2027 revenue history (Bloomberg): $48,075M on 2026-01-02, $50,282M on 2026-02-06 (Prolec), $51,926M on 2026-05-01, $52,537M on 2026-07-24, $53,029M on 2026-10-01. It has risen about 1% a quarter outside the Prolec step.

## 10. Has anyone already said it

- The 36% figure is public and quoted in the popular press, framed as slow conversion ("only 36% of equipment backlog ... is expected to become revenue within one year", EBC Financial Group 2026-07-23; Motley Fool 2026-08-22). Neither multiplies it out or compares it with consensus.
- The percentage fell (42% to 36%) while the dollar amount rose 51%. The percentage is in a 10-Q footnote, rounded to a whole point, with no division split, and is not in the release or the slides.
- Prolec entered the backlog in Q1 2026, which blurs year-on-year comparisons of both the schedule and revenue.
- Revenue surprises so far: Q4 2025 $11.0B against $10.23B consensus; Q2 2026 $11.10B against $10.79B. The stock fell 8.7% on the Q2 2026 day because the margin guide was held. A revenue beat has not been what moves this stock.

## 11. Limits

1. One miss in seven windows (-8%). A repeat would put equipment revenue 4% below the Street.
2. Overlapping windows: about two independent years.
3. The uplift may be shrinking as lead times lengthen (open windows point to +2-4%).
4. The Street's equipment lines come from the division consensus, contributor count not visible on this terminal. For Q3 2026 the medians of the three equipment lines sum to $7,615M against a mean sum of $7,482M (+1.8%); medians are not available for the other quarters. On medians the gap to the schedule would be nearer 2.5-3% than 4.5%.
5. Rounding of the 36%: Y1 is $31,176M to $32,055M.
6. Management's FY26 guide implies H2 2026 equipment of only 47-50% of Y1, against 57% delivered in the second half of both earlier June windows. Either the guide is cautious again or this year's schedule is back-loaded.
7. Profit effect is small and depends on an equipment margin GEV does not disclose by division.
8. The division split of the schedule is a bound, not a disclosure.

## 12. Checks that showed no gap

| Check | Result |
|---|---|
| Services, four quarters | Street turnover 22.4% of services RPO; reported range 21.3-22.6% |
| Equipment, months 13-24 | Street fill $9.7B against $10.4-13.1B reported (ex-Prolec); explained by earlier ordering |
| Equipment, eight quarters | Street $65,382M = 1.145x the two-year schedule ($57,084M); reported 1.28-1.48x (ex-Prolec); same explanation |
| Calendar 2027 total revenue | +0.8% to +5.7%, middle about +3% |
| Five-year coverage | 97% of equipment RPO ($85.2B) within five years against Street five-year equipment revenue of about $214B (40% covered); nothing to test |
| Division attribution between Power and Electrification | Not identified by disclosed data |

## 13. Dates and marks (for the team to set its own)

| Date | Number reported by GEV | Compare with |
|---|---|---|
| 2026-10-28 (Q3 10-Q) | Q3 equipment revenue; equipment RPO and one-year share at 9/30/26 | Street Q3 equipment $7,482M; Street Q4 2026 to Q3 2027 equipment $31,314M |
| Late January 2027 (Q4 release, FY27 guide, 10-K) | FY26 revenue; FY27 revenue guide; Y1 at 12/31/26 | Guide top $46.5B; Street FY27 revenue $53,029M; Street 2027 equipment $32,383M |
| Late April 2027 | Q1 2027 equipment revenue | Street $6,675M (Wind $1,019M) |
| Late July 2027 | Q2 2027 equipment revenue; four-quarter sum | Street $7,748M (Wind $1,259M); Street four-quarter $30,245M; schedule $31,616M |
