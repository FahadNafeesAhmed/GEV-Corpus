# Verify (REPRODUCE): fy26-fcf-h2-deposits

_Research input only: facts, arithmetic, sources. No memo sentences, no forecast chosen for the team. Bloomberg figures cited as "Bloomberg, 2026-10-01"; keep inside the project folder. Units $M unless stated. CL = contract liabilities and deferred income (customer deposits and progress payments)._

## 0. Verdict

| Item | Result |
|---|---|
| Numbers reproduce from primary files? | **Yes.** Every Street and company figure in the candidate was recomputed. Eight corrections, none large (section 3). |
| Survives the test (gap at least about 5% and larger than its own error band)? | **No.** |
| Why | (1) FY26 range $11.6B to $16.4B straddles the Street ($12.2B to $12.5B): band about +/-17%, gap about +12% to +19%. (2) The Q3 test line is +3.6% to +4.6% against the Street median, under 5%, with a band of about +/-3%. (3) The like-for-like guide record (guides given in July) supports only +0% to +9% over the top of the range, which is FY26 $12.5B to $12.7B. |
| What is left | A sign call, not a number: CL has not fallen in any of 10 quarters, and the median broker has it flat. The skew is to the upside, but the size is not pinned. |

## 1. Street numbers (Bloomberg, 2026-10-01), recomputed

| Figure | Candidate | Recomputed | File, row |
|---|---|---|---|
| FY26 FCF | 12,196 | 12,196.3 | `GEV_bloomberg_pull_filled_2026-10-01.xlsx`, Consensus, BEST_ESTIMATE_FCF 1FY. Count, high, low not in the file |
| Q3'26 FCF | 1,502 (range -1,622 to +7,062) | 1,502.2; median 1,481.7; low -1,622.4; high 7,062.0 | `06_modl.xlsx` HEADLINE_FCF; `01_eeo_annual.xlsx` (15 analysts) |
| Q4'26 FCF | 1,148 | 1,148.5 (15 analysts) | `01_eeo_annual.xlsx` row 26 |
| H2'26 Street, quarterly basis | 2,651 | 2,650.7 | sum |
| H2'26 Street, annual basis | not stated | 12,196 - 9,897 = **2,299** | |
| FY26 on the quarterly basis | not stated | 9,897 + 2,651 = **12,548** | already above the top of the guide (12,500) |
| Q3 current CL | mean 37,492; median 39,944; low 19,487; high 41,817 | same | `06_modl.xlsx` BS_CONTRACT_LIABS_SHORT_TERM |
| Q3 change in CL | mean -1,402; median -50; low -8,795; high +1,873 | same | `06_modl.xlsx` CF_CHANGE_IN_CONTRACT_LIABS |
| Q3 orders / revenue: Power | 12,213 / 5,776 | 12,212.9 / 5,775.6 | `segment_quarterly.json` |
| Q3 orders / revenue: Electrification | 6,498 / 3,881 | 6,498.1 / 3,880.7 | same |
| Q3 orders / revenue: Wind | 1,510 / 2,341 | 1,509.5 / 2,341.0 | same |

Three facts the candidate does not state:

1. **Two Street figures exist.** Annual 12,196 implies H2 of 2,299. H1 actual plus the quarterly consensus is 12,548, which is above the guide top. Against 12,548 the candidate's central gap is +15.6%, not +18.9%.
2. **Broker count on the CL balance row is at least 7.** With min 19,487, max 41,817 and median 39,944, a mean of 37,492 is not possible with 3 to 6 contributors (the largest possible mean with 6 is 37,159). With 7 it is possible.
3. **The 19,487 entry is on another definition.** The lowest change entry is -8,795, which gives 31,149, not 19,487. The highest balance is exactly 39,944 + 1,873 = 41,817, so the top broker already models +$1.9B. Without the 19,487 entry the other brokers average about 38.5B to 40.2B (depends on the count), so "flat to slightly down" is the fair reading of the Street, and the +10.4% gap against the mean is an artifact.

## 2. Company numbers, recomputed from filings

| Figure | Candidate | Recomputed | Source |
|---|---|---|---|
| H1'26 FCF | 9,897 | 10,680 CFO - 783 capex = 9,897 | 10-Q Q2'26, acc. 0001996810-26-000148, p.32: "Free cash flow (Non-GAAP) $9,897" |
| Q1'26 / Q2'26 FCF | 4.79B / 5.11B | 4,791 / 5,106 | XBRL NetCashProvidedByUsedInOperatingActivities, PaymentsToAcquireProductiveAssets |
| FY25 FCF by quarter | - | 975 / 194 / 733 / 1,808 = 3,710 | same tags, 10-K FY25 acc. 0001996810-26-000015 |
| FY26 guide | 11.5-12.5B | same; H2 implied 1,603 to 2,603 | Q2'26 release: "free cash flow* of $11.5-$12.5 billion, up from $6.5-$7.5 billion" |
| CL total by quarter, YE23 to Q2'26 | 15,247 to 40,037 | 15,247 / 16,115 / 16,728 / 17,107 / 17,744 / 18,851 / 19,751 / 20,304 / 25,950 / 31,949 / 40,037 | XBRL ContractWithCustomerLiability |
| Current CL at 6/30/26 | 39,944 | 39,944 (non-current 93) | 10-Q Q2'26 balance sheet and Note 9 |
| Balance change by quarter | smallest +379; Q3s +379, +553; last three +5,646, +5,999, +8,088 | same | differences of the row above |
| Cash-flow line by quarter | not given | 885 / 711 / **64** / 1,139 / 1,124 / 736 / 559 / 5,600 / 5,574 / 8,121 | XBRL IncreaseDecreaseInContractWithCustomerLiability |
| Segment CL Q3'25 to Q2'26 | Power 12,645 / 16,547 / 20,400 / 27,685; Elec 5,268 / 6,462 / 8,269 / 9,124; Wind 2,390 / 2,938 / 3,278 / 3,227 | same | `gev_segments.csv`; Note 9 |
| Power product CL change, Q2'25 to Q2'26 | 923 (Q3'25), 7,320 (Q2'26), sum 17,035 | 930 / 923 / 3,933 / 3,929 / 7,320 = 17,035 | Note 9, equipment and other service agreement liabilities |
| Power equipment RPO | 39,261; YE23 13,636 | 39,261 (6/30/26), 24,707 (YE25), 18,977 (9/30/25), 13,636 (YE23) | 10-Q Q2'26 p.29; 10-K FY25; 10-Q Q3'25 acc. 0001996810-25-000160 |
| Order price per kW | Q4'25 $753; H1'26 $916 | (24,707 - 18,977 + 1,871) / 10.2 GW = **$745**; (39,261 - 24,707 + 3,834) / 20.1 GW = $915 | GW ordered: 10-K FY25 29.8 less 9M 19.6; 10-Q Q2'26 20.1 |
| Cash taxes H1'26 vs H1'25 | 1,258 vs 363 | same | 10-Q Q2'26 cash-flow statement |
| H1'26 working-capital lines | - | receivables -843; inventories -1,744; contract assets -358; payables +949; CL +13,695 | same |
| CFO remark | H1 FCF "substantially higher" than H2 | "we expect our free cash flow in the first half of the year to be substantially higher than the second half, as many of these slot reservations convert to orders" | Q2'26 call, corpus src:3161 |
| CEO remark | about 25% down | "a gas slot reservation agreement that has, like, 25% down" (offhand, in a Wind answer) | conference transcript 2026-09-16, company-hosted PDF |
| H2 gas commitments | 18-25 GW | "directionally 20 gigawatts ... likely to prove to be conservative"; H1 was 40 GW; Q4 larger than Q3 | same transcript |
| Stock on 2026-07-22 | -8.7% | 1,078.81 to 985.03 = -8.69% | `prices` table |
| Per-share size | $6-9, under 1% | 1,500 / 266.334 = $5.63; 2,300 / 266.334 = $8.64; 0.57% to 0.87% of $987.45 | |
| Reveal date | 2026-10-28 | Confirmed on the company events page per `E07_catalyst_calendar.md` line 13. The corpus `catalyst_calendar` table still shows an estimated 10-21. E07 also notes the date falls after the competition finals. | |

Guide record, all ten guide points (candidate shows six):

| Guide date | Implied remainder $B | Actual remainder $B | Actual / top of range |
|---|---|---|---|
| 2024-04-25 | 1.36-1.76 | 2.36 | 1.34 |
| 2024-07-24 | 1.14-1.54 | 1.54 | **1.00** |
| 2024-10-23 | 0.17-0.57 | 0.57 | **1.00** |
| 2025-01-22 | 2.00-2.50 | 3.71 | 1.48 |
| 2025-04-23 | 1.03-1.53 | 2.74 | 1.79 |
| 2025-07-23 | 1.83-2.33 | 2.54 | **1.09** |
| 2025-10-22 | 1.10-1.60 | 1.81 | **1.13** |
| 2025-12-09 | 1.60-2.10 | 1.81 | **0.86** (inside) |
| 2026-01-28 | 5.0-5.5 (full year) | 9.90 in H1 | 1.80, period not finished |
| 2026-04-22 | 1.71-2.71 | 5.11 in Q2 | 1.88, period not finished |
| 2026-07-22 | 1.60-2.60 | open | Street 2.30 (annual) / 2.65 (quarterly) |

Guides given in July or later (bold): 1.00, 1.00, 1.09, 1.13, 0.86. Median 1.00, mean 1.02. The 1.79 multiplier comes from guides given in January and April, before first-half deposit surprises.

## 3. Corrections to the candidate

| # | Candidate text | Correction |
|---|---|---|
| 1 | "Five of six finished above the top" | True for the six shown. All ten: 7 above, 2 exactly at the top, 1 inside. The 2024 points were left out. The two July guides finished at 1.00 and 1.09 of the top. |
| 2 | "x 1.79 (median overshoot) = $4.65B (FY $14.5B)" | Arithmetic is right. The comparison is not like for like. July-guide record gives 2.60 x 1.00 to 1.09 = $2.60B to $2.84B, FY26 $12.5B to $12.7B: +2.5% to +4.4% vs 12,196 and -0.4% to +1.5% vs 12,548. |
| 3 | "smallest rise +379 (Q3'24)" | True for the balance. The cash-flow line that quarter was **+64**, close to the Street median of -50. The Street test line "change in contract liabilities" is the cash-flow line. |
| 4 | "18-25 GW x $950 x 25% x 1.12 less 0.4 = $3.9-6.2B" | 18 GW gives $4.4B, not $3.9B ($3.9B needs 16 GW). 25 GW gives $6.25B. Low total becomes $5.6B, low-case FY26 $13.4B. |
| 5 | "reproduces the five-quarter change ... within 10%" | 15,265 vs 17,035 is 10.4% low, with a different price put in for each quarter. By quarter the model is +111% (Q3'25) to -45% (Q2'26). Actual Power product CL change per GW of new commitments: $103M, $71M, $164M, $187M, $366M. |
| 6 | "Q4'25 $753" per kW | $745 on 10.2 GW from the filings. Not material. |
| 7 | "+10.4% vs the mean" | The mean carries one entry at 19,487 on another definition. Use the median (+3.6%). |
| 8 | Power services backlog growth 1,100 a quarter (fcf-deposits lens) | Power services RPO rose 69,841 to 72,388 in H1'26, about 1,270 a quarter. Power firm term becomes 30% x (12,213 - 5,776 - 1,270) = +1,550 instead of +1,601. Not material. |

## 4. Own recomputation of H2 2026

Cash before working capital, H2'26: Street EBITDA 1,672 + 2,500 = 4,172; capex 720 to 920 (Street quarters 722; annual BEst less H1 = 923; H2'25 actual 918); cash taxes 900 to 1,500 (H1'26 1,258; H2'25 467); other -300 to -900 (plug was -572 in H2'25). Result about 1.55B, range 0.85B to 2.25B. The candidate's 1.7B (1.0 to 2.1) is consistent.

H2 change in CL, scaled by value of new gas commitments:

| Period | New commitments GW | Price $B/GW | Value $B | Power product CL change $B | Share of value |
|---|---|---|---|---|---|
| H2'25 | 37 | about 0.70 | 25.9 | 4.86 | 18.8% |
| H1'26 | 41 | about 0.92 | 37.7 | 11.25 | 29.8% |
| H2'26 | 20 to 28 | 0.95 | 19.0 to 26.6 | 3.6 to 7.9, less 0.4 for 5 GW a quarter shipments | 18.8% to 29.8% |

Add Electrification +1.0 to +1.8 (Q2'26 +0.85; H1 included the acquired Prolec balance) and Wind -0.3 to 0. Total about +3.9B to +9.3B, central about +6.3B. This agrees with the candidate's $5.1B to $8.0B.

Other working capital took back 3.63B in H2'25 (receivables -2.96B, most of it in Q4: -2.49B) against CL growth of 6.16B. H1'26 took back 2.0B against 13.7B.

| Case | Cash before WC | CL change | Share kept (k) | H2 FCF | FY26 | vs 12,196 | vs 12,548 |
|---|---|---|---|---|---|---|---|
| Adverse (candidate) | 1.1-1.6 | 5.1 | H2'25 take-back x 1.24 | 1.7-2.2 | 11.6-12.1 | -5% to -1% | -8% to -4% |
| Guide top | | | | 2.60 | 12.5 | +2.5% | -0.4% |
| July-guide record (x1.09) | | | | 2.84 | 12.7 | +4.4% | +1.5% |
| H2'25 pattern (k 0.32) | 1.55 | 6.3 | 0.32 | 3.6 | 13.5 | +10.5% | +7.4% |
| Middle (k 0.45) | 1.55 | 6.3 | 0.45 | 4.4 | 14.3 | +17% | +14% |
| Candidate central | 1.7 | 6.5 | 0.45 | 4.6 | 14.5 | +18.9% | +15.6% |
| High | 1.7 | 8.0 | 0.60 | 6.5 | 16.4 | +34.5% | +30.7% |

Corrected central: about $13.5B to $14.5B (mid $14.0B: +15% vs 12,196, +12% vs 12,548). Range $11.6B to $16.4B, which is about +/-17% of $14.0B. The low end is below both Street figures. **Band (17%) is not smaller than the gap (12% to 15%).**

Q3 balance, own check: 8 to 12 GW of new commitments x $206M per GW (four-quarter average; quarterly range $71M to $366M) = +1.65B to +2.5B, less 0.2 to 0.4 for higher shipments; Electrification +0.2 to +0.9; Wind -0.6 to -0.1 (prior third quarters -903, -582). Total about +0.9B to +3.1B, central about +1.9B. Balance about 41.8B (40.8B to 43.0B): **+4.6% vs the median, band about +/-3%, equal to the highest broker (41,817)**. With the fcf-deposits central (41.4B) the gap is +3.6%. Both are under 5%.

## 5. Definition checks

| Check | Result |
|---|---|
| FCF definition, Street vs company | Same. Bloomberg HEADLINE_FCF Q2'26 actual 5,106 equals company FCF (CFO less gross additions to PP&E and internal-use software). |
| CL definition, Street vs company | Same line. Median 39,944 equals "Contract liabilities and current deferred income" at 6/30/26 to the dollar. Excludes 93 non-current. |
| Balance vs cash-flow line | They differ by acquisitions and currency. H1'26: balance +14,088, cash-flow +13,695; the 10-Q says the balance rose "as a result of the acquisition of Prolec GE" as well as collections. Q3'24: balance +379, cash flow +64. |
| Acquisition effect in H2'26 | None known for CL. Prolec closed 2026-02-02 and is in the 6/30/26 base. |
| Equipment vs services | Services CL is 1,880 of 40,037 and flat (1,789 to 1,989 for 10 quarters). The line is equipment deposits. |
| Reservations vs orders | Reservation deposits sit in CL; reservations are not in orders or RPO (10-Q definition of RPO). Confirmed. |
| Deposit terms | No filing gives the percentage. "Like, 25%" is one spoken remark; "around 20%" is a secondary report. |
| Periods | Fiscal year = calendar year. H2 = Q3 + Q4 2026. No fiscal-year mismatch. |
| Stale estimates in the annual FCF mean | Cannot be checked: no broker detail, count or dates on BEST_ESTIMATE_FCF. The 352 difference between 12,196 and 12,548 may be stale entries or a different broker set. |
| "Positive free cash flow" in Q3 (CFO, July call) | Boilerplate. The same words preceded Q4'25 (actual 1.81B) and Q1'26 (actual 4.79B). No information. |

## 6. Files used

- `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` (Consensus); `GEV_Pull_2026-10-01/06_modl.xlsx`, `01_eeo_annual.xlsx`, `01-eeo-company-specific.xlsx`, `segment_quarterly.json`.
- `data/gev.db`: `xbrl_facts`, `mgmt_guidance`, `prices`, `sources` 2648 (Dec-2025 release), 2667 (Q2'26 release), 953, 671, 3689, 3161 (Q2'26 call), 3771 (Q3'25 call), 2660 (Q4'25 call).
- 10-Q Q2'26 0001996810-26-000148; 10-K FY25 0001996810-26-000015; 10-Q Q3'25 0001996810-25-000160.
- `data/financials/gev_quarterly.csv`, `gev_segments.csv`, `gev_operational.csv`.
- `09_finrobot_overnight/E07_catalyst_calendar.md`; `04_market_briefing/DIGEST.md` (conference transcript quotes).
