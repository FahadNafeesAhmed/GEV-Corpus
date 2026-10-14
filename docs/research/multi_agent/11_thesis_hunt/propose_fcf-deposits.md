# Thesis hunt, lens: free cash flow and customer deposits

_Research input only: facts, arithmetic, tables and sources. No memo sentences. The team chooses every forecast number and the direction. Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Units: $M unless stated. "CL" = contract liabilities and deferred income (customer deposits and progress payments). "SRA" = slot reservation agreement. "Eq RPO" = equipment remaining performance obligation (firm backlog).

---

## 0. Result in one screen

| Question | Answer |
|---|---|
| Is Street FCF for 2027-2029 consistent with the Street's own orders and revenue? | **Yes, within the error of any deposit model.** Street FCF equals the case where gas GW under contract stays about flat at 125 GW after 2026. |
| FCF the order book implies, FY27 | $4.4B (SRAs run off) / **$8.4B (flat 125 GW)** / $10.4B (GW grows to 135). Street: $7,654M. If conversions bring no new cash in the year, subtract about $3B from each case. |
| Does any FCF line give a gap of 5% or more with an error band smaller than the gap? | **No.** FY26: +2% to +19%. FY27: -43% to +36%. Both bands are wider than the central gap. |
| The one Street number that arithmetic contradicts | **Q3'26 contract liabilities.** Bloomberg median = $39,944M, which is the Q2'26 reported balance to the dollar (no change). Mean = $37,492M (a fall). The balance has risen in 10 of 10 quarters. Arithmetic on the Street's own Q3 orders gives +$0.1B to +$2.7B. |
| Company framework check | "At least $24B" cumulative FCF 2025-28 is stale: FY25 actual + FY26 guide low end = $15.2B, leaving $8.8B for 2027+2028. Street has $17.2B for those two years. |

---

## 1. Street numbers used

### 1.1 Annual consensus (Bloomberg, 2026-10-01; `GEV_bloomberg_pull_filled_2026-10-01.xlsx`, sheet Consensus, rows 2-17)

| Year | Revenue (r2) | EBITDA (r3) | EBIT (r9) | Net income (r10) | FCF (r16) | Capex (r17) | FCF / NI |
|---|---|---|---|---|---|---|---|
| 2026 | 46,240 | 6,334 | 4,427 | 7,170 | 12,196 | 1,706 | n/m (Prolec gain) |
| 2027 | 53,029 | 9,471 | 8,034 | 6,642 | 7,654 | 1,441 | 115% |
| 2028 | 60,985 | 12,553 | 11,429 | 9,285 | 9,527 | 1,554 | 103% |
| 2029 | 70,851 | 16,496 | 14,891 | 12,034 | 9,702 | 1,647 | 81% |
| 2030 | 79,724 | 19,544 | 18,092 | 14,415 | 13,036 | 1,810 | 90% |

Cumulative FCF 2025-28 on Street numbers: 3,710 + 12,196 + 7,654 + 9,527 = **33,087**.

### 1.2 Quarterly consensus (Bloomberg, 2026-10-01; `GEV_Pull_2026-10-01/segment_quarterly.json`; `01_eeo_annual.xlsx` for analyst counts)

| Quarter | Orders | Power orders | Elec orders | Wind orders | Revenue | Power rev | Elec rev | Wind rev | FCF | # FCF est. | EBITDA |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q3'26 | 20,332 | 12,213 | 6,498 | 1,510 | 11,993 | 5,776 | 3,881 | 2,341 | 1,502 | 15 | 1,672 |
| Q4'26 | 25,071 | 14,991 | 7,492 | 1,761 | 13,915 | 7,384 | 4,289 | 2,344 | 1,148 | 15 | 2,500 |
| Q1'27 | 23,056 | 12,102 | 8,475 | 1,180 | 11,143 | 6,061 | 3,671 | 1,522 | 729 | 13 | 1,810 |
| Q2'27 | 23,737 | 13,659 | 6,782 | 1,296 | 12,968 | 6,885 | 4,304 | 1,866 | 1,726 | 12 | 2,228 |
| Q3'27 | 23,241 | 12,805 | 7,420 | 1,567 | 13,581 | 6,915 | 4,649 | 2,123 | 3,158 | | 2,345 |
| Q4'27 | 27,455 | 14,391 | 8,981 | 1,635 | 15,404 | 8,260 | 5,080 | 2,078 | 2,562 | | 3,008 |

| Period (sum of quarters) | Orders | Power | Elec | Wind | Revenue | Power | Elec | Wind | FCF | Book-to-bill |
|---|---|---|---|---|---|---|---|---|---|---|
| H2 2026 | 45,403 | 27,204 | 13,990 | 3,271 | 25,908 | 13,160 | 8,169 | 4,685 | 2,651 | 1.75 |
| 2027 | 97,489 | 52,958 | 31,657 | 5,678 | 53,097 | 28,121 | 17,704 | 7,589 | 8,176 | 1.84 |
| 2028 | 91,401 | 50,239 | 36,060 | 5,638 | 61,421 | 33,521 | 21,270 | 6,813 | 9,303 | 1.49 |
| 2029 | 100,408 | 52,482 | 40,580 | 5,352 | 71,549 | 39,522 | 24,959 | 7,381 | 8,176 | 1.40 |
| 2030 | 109,969 | 54,312 | 44,941 | 5,471 | 80,718 | 45,215 | 28,422 | 7,440 | 13,301 | 1.36 |

Notes: quarterly FCF sums differ from annual BEst (FY27 8,176 vs 7,654) because fewer brokers supply quarters. Q1'29 FCF is -1,684 (9 brokers). The annual BEst figure is used as "the Street".

### 1.3 Q3'26 balance-sheet and cash-flow consensus (Bloomberg MODL, 2026-10-01; `06_modl.xlsx`, sheet "Single Period", period 2026:Q3)

| Line (Bloomberg field) | Mean | Median | Low | High |
|---|---|---|---|---|
| Contract liabilities, short-term (BS_CONTRACT_LIABS_SHORT_TERM), row 171 | 37,492 | 39,944 | 19,487 | 41,817 |
| Change in contract liabilities (CF_CHANGE_IN_CONTRACT_LIABS), row 204 | -1,402 | -50 | -8,795 | +1,873 |
| Change in accounts receivable, row 200 | +1,141 | +242 | -957 | +4,616 |
| Change in inventories, row 201 | +947 | +896 | -300 | +2,994 |
| Change in contract assets, row 203 | -1,280 | -926 | -2,981 | 0 |
| Cash from operations, row 205 | 1,793 | 1,709 | -1,422 | 7,356 |
| Free cash flow (HEADLINE_FCF), row 228 | 1,502 | 1,482 | -1,622 | 7,062 |

The reported Q2'26 current contract liabilities and deferred income are 40,037 - 93 non-current = **39,944** (10-Q Q2'26, balance sheet and Note 9; `data/financials/gev_quarterly.csv`). The Bloomberg median equals that figure exactly. The number of brokers behind the contract-liabilities rows is not shown on the export.

---

## 2. History: deposits against orders, revenue and backlog

### 2.1 Quarterly table (10-Q / 10-K Note 9 and segment MD&A; XBRL in `gev.db`; `data/financials/gev_segments.csv`)

| Quarter | CL total | Equipment CL: Power / Elec / Wind | Services CL | Eq RPO: Power / Elec / Wind | CL / Eq RPO: Power / Elec / Wind | All equipment CL / Eq RPO | Change in CL (balance) | Cash-flow line | Gas GW under contract | Power eq. CL per GW ($M) |
|---|---|---|---|---|---|---|---|---|---|---|
| Q4'23 | 15,247 | 5,732 / 2,352 / 4,819 | 1,810 | 13,636 / 13,233 / 13,709 | 42.0% / 17.8% / 35.2% | 31.9% | | | | |
| Q1'24 | 16,115 | 5,980 / 2,664 / 5,134 | 1,804 | 14,394 / 14,849 / 13,119 | 41.5% / 17.9% / 39.1% | 32.6% | +868 | +885 | | |
| Q2'24 | 16,728 | 6,327 / 3,154 / 4,970 | 1,806 | 10,978 / 17,540 / 13,147 | 57.6% / 18.0% / 37.8% | 34.8% | +613 | +711 | | |
| Q3'24 | 17,107 | 7,134 / 3,500 / 4,067 | 1,914 | 11,392 / 18,624 / 12,182 | 62.6% / 18.8% / 33.4% | 34.9% | +379 | +64 | | |
| Q4'24 | 17,744 | 7,879 / 3,946 / 3,684 | 1,789 | 12,461 / 20,005 / 10,720 | 63.2% / 19.7% / 34.4% | 36.0% | +637 | +1,139 | ~45 | 175 |
| Q1'25 | 18,851 | 8,764 / 4,489 / 3,270 | 1,876 | 13,920 / 21,996 / 9,676 | 63.0% / 20.4% / 33.8% | 36.3% | +1,107 | +1,124 | 50 | 175 |
| Q2'25 | 19,751 | 9,694 / 5,052 / 2,624 | 1,914 | 16,133 / 23,950 / 9,731 | 60.1% / 21.1% / 27.0% | 34.9% | +900 | +736 | 54 | 180 |
| Q3'25 | 20,304 | 10,617 / 5,204 / 2,042 | 1,989 | 18,977 / 26,455 / 8,782 | 55.9% / 19.7% / 23.3% | 33.0% | +553 | +559 | 62 | 171 |
| Q4'25 | 25,950 | 14,550 / 6,449 / 2,796 | 1,977 | 24,707 / 30,508 / 9,112 | 58.9% / 21.1% / 30.7% | 37.0% | +5,646 | +5,600 | 83 | 175 |
| Q1'26 | 31,949 | 18,479 / 8,259 / 3,173 | 1,917 | 28,530 / 38,598 / 8,905 | 64.8% / 21.4% / 35.6% | 39.4% | +5,999 | +5,574 | 100 | 185 |
| Q2'26 | 40,037 | 25,799 / 9,113 / 3,150 | 1,880 | 39,261 / 40,589 / 8,197 | 65.7% / 22.5% / 38.4% | 43.3% | +8,088 | +8,121 | 116 | 222 |

- The balance rose in all 10 quarters. Smallest rise: +379 (Q3'24). Q3 is the weakest quarter in both years (+379, +553) because Wind deliveries burn Wind deposits.
- Q2'24 Power Eq RPO fell about $3.9B for a non-cash reason (10-Q Q2'24), so the Power ratio before and after is not comparable.
- Q1'26 Electrification includes Prolec GE. H1'26 balance change 14,088 vs cash-flow line 13,695: the 393 gap is Prolec and currency (10-Q Q2'26 Note 9).
- YE24 gas GW is approximate (Q1'25 release: 29 GW backlog + 21 GW SRAs = 50 GW after about 5 GW net growth).

### 2.2 Gas contracts by quarter (earnings releases, corpus `sources` ids 3689, 671, 953, 2667; 8-K exhibits)

| Quarter | SRAs signed GW | Direct orders GW | SRAs converted GW | Shipped GW | Backlog GW | SRA GW | Total GW | Change in Power equipment CL | Per GW signed ($M) |
|---|---|---|---|---|---|---|---|---|---|
| Q2'25 | 7 | 2 | 3 | 5.2 | 29 | 25 | 54 | +930 | 103 |
| Q3'25 | 12 | 1 | 7 | 4.0 | 33 | 29 | 62 | +923 | 71 |
| Q4'25 | 21 | 3 | 8 | 3.1 | 40 | 43 | 83 | +3,933 | 164 |
| Q1'26 | 19 | 2 | 6 | 4.2 | 44 | 56 | 100 | +3,929 | 187 |
| Q2'26 | 18 | 2 | 10 | 3.3 | 53 | 63 | 116 | +7,320 | 366 |

- A four-variable fit on five quarters does not identify the terms (residuals of 40-200% on 2025 quarters). A value-weighted fit puts most of the cash on firm orders (about 52% of order value) and none on SRAs; an unweighted fit puts $277M per GW signed. Neither is reliable.
- Year-end GW targets: "approximately 80 GW" for YE25 (Dec-2025 update) vs 83 actual; "at least 110 GW" for YE26 (Q1'26 release) passed one quarter later at 116; now "at least 125 GW" (Q2'26 release).
- "At least 125" is close to the physical slot count: H2'26 10 + 2027 20 + 2028 24 + 2029 about 27 + 2030 30 = 111 GW, plus half of 2031 (15) = 126 GW. More than 125 requires selling more of 2031-32.

### 2.3 Deposit terms found

| Term | Source | Value |
|---|---|---|
| SRA deposit | Company statement at a May-2025 broker conference, reported by ElectronEconomics 2025-12-15 (single secondary source) | "around 20%" of the gas turbine contract price; no slot held "without substantial cash down" |
| SRA deposit | News, 2026-06-22 (corpus src:2674) | "20% to 25% of a turbine's total value upfront" |
| Early reservation fee | KY PSC Order 2025-10-28 p.10 (Brown 12), `E08_dockets.md` | $25M per train, about 2% of plant cost, "to lock in firm pricing" |
| Refundability | CFO, Q3'25 call (corpus src:3796) | SRA deposits and order down payments are both "nonrefundable" |
| Timing | CFO, Q2'26 call (corpus src:3161) | Down payments "correlate with the timing of orders"; H1'26 FCF "substantially higher than the second half, as many of these slot reservations convert to orders" |
| Accounting | 10-Q Q2'26 Note 9 | CL = "cash received from customers under ordinary commercial payment terms in advance of delivery" |

### 2.4 Derived ratios (formulas shown)

| Ratio | Formula | FY24 | FY25 | H1'26 | Cumulative YE23 to Q2'26 |
|---|---|---|---|---|---|
| Gross deposit additions | cash-flow change + revenue recognised from opening CL | 2,799 + 9,933 = 12,732 | 8,019 + 11,225 = 19,244 | 13,695 + 7,512 = 21,207 | |
| Burn of opening CL in the period | revenue recognised from opening CL / opening CL | 65% | 63% | 29% (half year) | |
| Gross additions / orders | orders 44.1B / 59.3B / 42.5B | 29% | 32% | 50% | |
| Change in CL / (orders - revenue) | | 31% | 38% | 62% | |
| Change in equipment CL / change in Eq RPO | | 2,606 / 2,569 = 101% | 8,286 / 21,198 = 39% | 14,267 / 23,576 = 61% | 25,159 / 47,343 = 53% |
| Electrification, incremental | (9,113 - 2,352) / (40,589 - 13,233) | | | | 24.7% (level 17.8% to 22.5%) |

SRA deposits are in CL but SRAs are not in orders or RPO, so every ratio above is inflated from Q4'25 on.

Splitting Power equipment CL at Q2'26 (25,799) into an SRA bucket and firm-order deposits:

| Assumed SRA price ($B/GW) | SRA bucket = 63 GW x price x 20% | Firm-order CL | Firm CL / Power Eq RPO (39,261) | Incremental firm ratio since YE23 |
|---|---|---|---|---|
| 0.80 | 10,080 | 15,719 | 40.0% | 39.0% |
| 0.95 | 11,970 | 13,829 | 35.2% | 31.6% |
| 1.10 | 13,860 | 11,939 | 30.4% | 24.2% |

Price check: H1'26 Power equipment orders = (39,261 - 24,707) + 3,851 equipment revenue = $18.4B on 20.1 GW of gas orders plus nuclear and hydro, so about $0.85-0.95B per GW.

### 2.5 FCF bridge by period (cash-flow statements; XBRL)

| Period | Adj. EBITDA | Capex | Cash taxes | Receivables | Inventories | Contract assets | Payables | CL | Total working capital | FCF | Other (plug) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FY24 | 2,035 | -883 | -623 | -1,289 | -641 | -409 | +1,066 | +2,799 | +1,526 | 1,701 | -354 |
| FY25 | 3,196 | -1,277 | -830 | -1,928 | -1,433 | -456 | -105 | +8,019 | +4,097 | 3,710 | -1,476 |
| H1'25 | 1,227 | -359 | -363 | +1,031 | -883 | -647 | +207 | +1,860 | +1,568 | 1,169 | -904 |
| H2'25 | 1,969 | -918 | -467 | -2,959 | -550 | +191 | -312 | +6,159 | +2,529 | 2,541 | -572 |
| H1'26 | 2,146 | -783 | -1,258 | -843 | -1,744 | -358 | +949 | +13,695 | +11,699 | 9,897 | -1,907 |

- FCF excluding the change in CL: FY24 -1,098; FY25 -4,309; H1'26 -3,798. All reported FCF since the spin is customer deposits.
- Working capital other than CL: FY24 -1,273; FY25 -3,922; H2'25 -3,630; H1'26 -1,996.
- (Receivables + inventories + current contract assets - trade payables) / trailing revenue: YE24 20.4B / 34.9B = 58%; YE25 23.8B / 38.1B = 62%; Q2'26 26.7B / 41.4B = 64%.
- H1'26 cash taxes (1,258) are twice the tax provision (630). The 10-Q gives no reason.
- H1'26 "other" includes the $0.5B voluntary pension contribution and the China XD gain moved to investing.

### 2.6 FCF guidance record (releases; `mgmt_guidance` table)

| Guide date | Full-year guide | FCF already reported | Implied remaining | Actual remaining | Actual vs top of implied range |
|---|---|---|---|---|---|
| 2024-04-25 | 0.7-1.1B | Q1'24 -0.66B | 1.36-1.76B | 2.36B | +34% |
| 2024-07-24 | 1.3-1.7B | H1'24 0.16B | 1.14-1.54B | 1.54B | 0% |
| 2024-10-23 | 1.3-1.7B | 9M'24 1.13B | 0.17-0.57B | 0.57B | 0% |
| 2025-01-22 | 2.0-2.5B | none | 2.0-2.5B | 3.71B | +48% |
| 2025-04-23 | 2.0-2.5B | Q1'25 0.98B | 1.03-1.53B | 2.74B | +79% |
| 2025-07-23 | 3.0-3.5B | H1'25 1.17B | 1.83-2.33B | 2.54B | +9% |
| 2025-10-22 | 3.0-3.5B | 9M'25 1.90B | 1.10-1.60B | 1.81B | +13% |
| 2025-12-09 | 3.5-4.0B | 9M'25 1.90B | 1.60-2.10B | 1.81B | inside range |
| 2026-04-22 | 6.5-7.5B | Q1'26 4.79B | 1.71-2.71B | Q2 alone 5.11B | +88% with two quarters left |
| **2026-07-22** | **11.5-12.5B** | H1'26 9.90B | **1.60-2.60B** | due Jan-2027 | Street: 2.30B (annual) / 2.65B (quarterly) |

- FY26 guide path: 4.5-5.0B (Dec-2025), 5.0-5.5B, 6.5-7.5B, 11.5-12.5B.
- Second-half guides were the tightest: actual H2 at the top (2024) and 9% above the top (2025). Applying +0% to +9% to the H2'26 top gives H2 FCF 2.60-2.83B and FY26 12.5-12.7B, which is +2.5% to +4.4% above the Street's 12,196.

### 2.7 Cumulative framework

| Version | Cumulative FCF 2025-28 | Source |
|---|---|---|
| Dec-2024 | at least $14B | Dec-2025 investor-day notes (corpus src:2686) |
| Dec-2025 | at least $22B | Press release 2025-12-09 |
| Jan-2026 | at least $24B (Prolec added) | Q4'25 release |
| Reported to Q2'26 (6 of 16 quarters) | 3,710 + 9,897 = $13.6B | |
| FY25 actual + FY26 guide | $15.2-16.2B | |
| Implied by the $24B floor for 2027 + 2028 | $7.8-8.8B for the two years | |
| Street, 2027 + 2028 | 7,654 + 9,527 = $17.2B | Bloomberg, 2026-10-01 |
| Street, 2025-28 | $33.1B, 38% above the floor | |

Mechanical roll-forward of the framework for the FY26 guide raise alone: 24 + (12.0 - 5.25) = about $30.8B, which is 7% below the Street's $33.1B. The framework is a floor ("at least"). No December 2026 event is listed; the next scheduled outlook is the Q4'26 call, late January 2027 (`E07_catalyst_calendar.md`).

---

## 3. What Street FCF implies for working capital

Method A: Street WC = FCF - (net income + D&A - capex), with D&A = EBITDA - EBIT.
Method B: Street WC = FCF - (EBITDA - capex - cash taxes - other), with cash taxes = 23% x (EBIT + 900 of interest and non-operating benefit income), other = 800 (range 300-1,300; history -354, -1,476).

| Year | FCF | Method A | Method B, central (range) | Revenue growth | Other working capital at 0.5 x revenue growth | Street-implied change in CL (Method B) |
|---|---|---|---|---|---|---|
| 2027 | 7,654 | +1,016 | +2,479 (1,671 to 3,287) | 6,789 | -3,394 | **+5,873** |
| 2028 | 9,527 | +672 | +2,164 (1,238 to 3,089) | 7,956 | -3,978 | +6,142 |
| 2029 | 9,702 | -2,290 | -715 (-1,760 to +330) | 9,866 | -4,933 | +4,218 |
| 2030 | 13,036 | -1,021 | +470 (-685 to +1,625) | 8,873 | -4,436 | +4,907 |

The 0.5 factor is below the 58-64% balance ratio in section 2.5 because $5.4B of contract assets are long-term service agreements that do not scale with equipment revenue. Each 0.1 on the factor moves the implied change in CL by about $0.7-1.0B a year.

---

## 4. What the Street's own order book implies for deposits

### 4.1 Model

- Electrification: change in CL = 22.5% x (orders - revenue - services backlog growth of 300 a year). Ratio range 20-25%.
- Wind: change in CL = 35% x (orders - revenue). Range 30-40%.
- Power, firm orders: change in CL = 30% x (orders - revenue - services backlog growth of 4,500 a year). Range 24-39% (section 2.4).
- Power, SRA bucket: 20% x SRA GW x price ($0.95B per GW at Q2'26, $0.975B H2'26, $1.0B 2027, $1.05B after). When an SRA converts, its 20% leaves the bucket and the 30% firm rate applies, so a conversion is assumed to bring 10% of value in new cash in the period.
- Firm gas orders in GW = (Power orders - Power services orders - 2,500 of non-gas equipment) / price. Shipments: 10 GW H2'26, 20, 24, 27, 30.

### 4.2 Segment arithmetic on Street orders and revenue

| Period | Change in Eq RPO: Elec / Wind / Power | Elec CL | Wind CL | Power firm CL | Sum before SRA bucket | Implied firm gas orders, GW |
|---|---|---|---|---|---|---|
| H2 2026 | 5,671 / -1,414 / 11,794 | +1,276 | -495 | +3,538 | +4,319 | 16.5 |
| 2027 | 13,653 / -1,911 / 20,336 | +3,072 | -669 | +6,101 | +8,504 | 31.1 |
| 2028 | 14,490 / -1,175 / 12,218 | +3,260 | -411 | +3,665 | +6,514 | 25.6 |
| 2029 | 15,321 / -2,029 / 8,460 | +3,447 | -710 | +2,538 | +5,275 | 25.8 |
| 2030 | 16,219 / -1,969 / 4,597 | +3,649 | -689 | +1,379 | +4,339 | 25.0 |

Electrification is the tight piece: about +$3.1-3.6B a year in every year, on a ratio that has stayed between 17.8% and 22.5% for 11 quarters.

### 4.3 Three paths for gas GW under contract

| Period | Run-off (no new SRAs after 2026): backlog / SRA / total GW | Change in CL | Flat at 125 GW | Change in CL | Growth (135 at YE27, 145 from YE28) | Change in CL |
|---|---|---|---|---|---|---|
| H2 2026 | 59 / 66 / 125 | +5,131 | 59 / 66 / 125 | +5,131 | 59 / 66 / 125 | +5,131 |
| 2027 | 71 / 34 / 105 | +2,620 | 71 / 54 / 125 | +6,620 | 71 / 64 / 135 | +8,620 |
| 2028 | 72 / 9 / 81 | +1,489 | 72 / 53 / 125 | +6,729 | 72 / 73 / 145 | +8,929 |
| 2029 | 71 / 0 / 71 | +3,403 | 71 / 54 / 125 | +5,533 | 71 / 74 / 145 | +5,533 |
| 2030 | 66 / 0 / 66 | +4,339 | 66 / 59 / 125 | +5,398 | 66 / 79 / 145 | +5,398 |

Company statements on the path: "at least 125 gigawatts under contract by the end of the year"; "in '27, we expect our combined gigawatts under contract to continue to grow"; backlog GW to exceed SRA GW in H2'26 (Q2'26 call). The Street's H2'26 Power orders convert only about 16.5 GW, which leaves SRAs (66) above backlog (59) at year-end, slightly short of that last statement.

### 4.4 FCF by path against the Street

FCF = EBITDA - capex - cash taxes - 800 + change in CL - 0.5 x revenue growth, all other lines at Street values.

| Year | Street FCF | Ex-working-capital FCF | Street-implied change in CL | Run-off: FCF (vs Street) | Flat 125 GW: FCF (vs Street) | Growth: FCF (vs Street) |
|---|---|---|---|---|---|---|
| 2027 | 7,654 | 5,175 | 5,873 | 4,401 (-43%) | **8,401 (+10%)** | 10,401 (+36%) |
| 2028 | 9,527 | 7,363 | 6,142 | 4,874 (-49%) | **10,114 (+6%)** | 12,314 (+29%) |
| 2029 | 9,702 | 10,417 | 4,218 | 8,888 (-8%) | **11,017 (+14%)** | 11,017 (+14%) |
| 2030 | 13,036 | 12,566 | 4,907 | 12,468 (-4%) | **13,528 (+4%)** | 13,528 (+4%) |

Cumulative 2027-29: Street 26,883; flat 29,532 (+10%); growth 33,732 (+25%); run-off 18,163 (-32%).

Reading of the table (research, not a view): Street FCF in every year sits within 4-14% of the flat-125-GW path. Street FCF is therefore consistent with its own orders if gas GW under contract stays about flat after 2026.

### 4.5 Sensitivities (each alone, FY27 FCF)

| Input | Change | Effect on FY27 FCF |
|---|---|---|
| SRA GW at YE27 | +/- 10 GW | +/- $2.0B (20% x $1.0B per GW) |
| New cash at conversion | none in the year instead of 10% of value | about -$3.0B (31 GW x $0.975B x 10%) |
| Firm deposit rate | 24% or 39% instead of 30% | -$1.2B / +$1.8B |
| Other working capital factor | 0.4 or 0.6 instead of 0.5 | +/- $0.7B |
| Cash taxes and other | range in section 3 | +/- $0.8B |
| Power services backlog growth | 3,000 or 6,000 instead of 4,500 | +/- $0.45B |

Combined: flat path $5.4B to $8.4B; growth path $7.4B to $10.4B. Street's $7,654M is inside both. **The error band is wider than any gap. No FY27 FCF wedge.**

### 4.6 H2 2026

| Item | Value |
|---|---|
| Ex-working-capital FCF, H2'26 | 4,172 EBITDA - 923 capex - 900 taxes - 400 other = 1,949 |
| Other working capital | -0.5 x (46,240 - 41,400 trailing revenue) = -2,420 (H2'25 actual -3,630; H2'24 -354) |
| Guide-implied change in CL | 1,600 to 2,600 FCF gives +2,071 to +3,071 |
| Street-implied change in CL | +2,770 (annual BEst) / +3,122 (quarterly sum) |
| Model, 10% new cash at conversion | +5,131, H2 FCF 4,660, FY26 14,557 (+19% vs 12,196) |
| Model, no new cash at conversion | 5,131 - 10% x 16.5 GW x $0.975B = about +3,520, H2 FCF about 3,050, FY26 about 12,950 (+6%) |

The guide range sits just below the "no new cash at conversion" variant at exactly 125 GW. Each GW of SRAs above 125 adds about $0.2B. FY26 range: +2.5% to +4.4% on the guidance record (section 2.6), +6% to +19% on the model. The band is wider than the gap.

---

## 5. Q3'26 contract liabilities: the one line where the Street and the arithmetic differ

| Step | Arithmetic | Low | Central | High |
|---|---|---|---|---|
| Electrification | 22.5% x (6,498 orders - 3,881 revenue - 80) = +571; low case = Q3 seasonality (+152 in Q3'25, +346 in Q3'24) | +150 | +450 | +640 |
| Wind | 35% x (1,510 - 2,341) = -291; low case = Q3 history (-582, -903) | -600 | -400 | -250 |
| Power, firm | 30% x (12,213 - 5,776 - 1,100) = +1,601; low case removes 10% new cash on about 7.5 GW converted (-750) | +850 | +1,250 | +1,600 |
| Power, SRA bucket | new SRAs 5 to 10 GW x $1.03B x 20% less 7.5 GW converted x $0.9B x 20% | -320 | +200 | +710 |
| **Total change in CL, Q3'26** | | **+80** | **about +1,500** | **+2,700** |
| Balance at 30 Sep 2026 (current) | 39,944 + change | 40,000 | **about 41,400** | 42,600 |

| Comparison | Street (Bloomberg MODL, 2026-10-01) | Arithmetic, central | Gap |
|---|---|---|---|
| Balance, mean | 37,492 | 41,400 | +10.4% |
| Balance, median | 39,944 | 41,400 | +3.6% |
| Balance, high | 41,817 | 41,400 | -1.0% |
| Cash-flow change, mean | -1,402 | +1,500 | +$2.9B |
| Cash-flow change, median | -50 | +1,500 | +$1.55B |

- History check: 10 increases in 10 quarters; the smallest was +379; the two prior third quarters were +379 and +553, when Power orders were $5.2B and $7.8B against the Street's $12.2B for Q3'26.
- Reveal: Q3'26 release and 10-Q, 2026-10-28 (confirmed date). Balance-sheet line "contract liabilities and deferred income" and the cash-flow line "increase (decrease) in contract liabilities and current deferred income".
- Limits: the mean is pulled down by one low entry (19,487); against the median the gap is 3.6%. The number of contributing brokers is not visible. It is a cash and leading-indicator line, not profit. On 2026-07-22 the FCF guide rose by $5B and the stock still fell.

---

## 6. Other checks (no gap)

| Check | Result |
|---|---|
| Street 2029 FCF below 2028 trend (FCF / NI 81%) | Method B implies working capital of -0.7B; flat path gives +0.6B. Gap +14%, inside the band, and outside a 12-month reveal. |
| Street cash build vs Street FCF | Net cash 9,455 (Q2'26) to 13,327 (Q2'27), +3.9B, against 5.1B of FCF over the four quarters less about 0.5B of dividends and small buybacks. Consistent. |
| Interest income on the cash balance | About $13-18B at 3.6-4% = $0.5-0.7B a year, against H1'26 net interest and other of +$100M. Worth about $0.5 a share; under 2% of FY27 EPS. |
| Advance payments and cash taxes | H1'26 cash taxes 1,258 vs provision 630. No disclosure links this to deposits. Not usable. |
| Deposit unwind analog (GE Power Systems 2002-03) | Kill condition from the earlier sweep: contract liabilities falling quarter on quarter while revenue still rises. Not observed in any of 10 quarters. |

---

## 7. Sources

- GEV 10-Q Q2'26 (0001996810-26-000148): cash-flow statement, Note 9, MD&A cash flows, segment RPO tables.
- GEV 10-K FY25 (0001996810-26-000015), 10-K FY24 (0001996810-25-000011), 10-Qs 2024-2026: segment RPO, contract liabilities by segment.
- Earnings releases Q3'25 to Q2'26 and the December 2025 investor update (corpus `sources` 3689, 671, 953, 2667, 2648); Q2'26 call transcript (3161); Q3'25 call transcript (3796); December 2025 investor-day notes (2686).
- XBRL facts in `gev.db`: IncreaseDecreaseInContractWithCustomerLiability, ContractWithCustomerLiabilityRevenueRecognized, IncomeTaxesPaidNet, PaymentsToAcquireProductiveAssets, NetCashProvidedByUsedInOperatingActivities, InventoryNet, ReceivablesNetCurrent, ContractWithCustomerAssetNetCurrent, AccountsPayableTradeCurrent.
- `data/financials/gev_quarterly.csv`, `gev_segments.csv`, `gev_operational.csv`.
- Bloomberg, 2026-10-01: `GEV_bloomberg_pull_filled_2026-10-01.xlsx` (Consensus rows 2-17); `GEV_Pull_2026-10-01/segment_quarterly.json`; `01_eeo_annual.xlsx`; `06_modl.xlsx`.
- Prior research: `09_finrobot_overnight/E03_model_inputs.md`, `E07_catalyst_calendar.md`, `E08_dockets.md`, `BLOOMBERG_VERDICT.md`.
- Web: ElectronEconomics, "Slotting In the Future: Gas Turbine Reservations", 2025-12-15 (20% SRA deposit, secondary report of a company conference remark).
