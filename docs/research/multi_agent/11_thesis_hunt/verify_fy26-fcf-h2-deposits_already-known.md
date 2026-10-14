# Check: already known or bad data — candidate `fy26-fcf-h2-deposits`

_Research input only: facts, arithmetic, tables, sources. No memo sentences. The team picks every forecast number and the direction. Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Units: $M unless stated. "CL" = contract liabilities and deferred income (customer deposits).

## 0. Verdict

| Item | Result |
|---|---|
| Survives as a stand-alone wedge (FY26 FCF +19% vs Street)? | **No** |
| Key numbers recomputed from primary files? | Yes (section 1) |
| Street FY26 FCF figure solid? | Yes: three vendors within 1.5% ($12.0-12.2B) |
| Street Q3 CL "test line" solid? | **No**: thin, one bad entry, median is a carry-forward |
| Idea already stated in public? | **Yes**: company (16 Sep 2026) and a broker note (22 Jul 2026) |
| Stock already moved on it? | Partly: +4.8% on 16 Sep; +11.9% from 15 Sep to 1 Oct |
| Ordinary explanation that shrinks the gap? | Yes: like-for-like guide record gives +2.5% to +4.4%, not +19% |
| What is left | Direction only: FY26 FCF at or above the guide top ($12.5B) is likely. Gap about +2.5% to +7.5% vs the annual consensus, 0% to +4.5% vs the brokers who publish quarters. Supporting evidence, not a thesis. |

## 1. Numbers recomputed

| Number | Value | Source | Matches candidate? |
|---|---|---|---|
| H1 2026 FCF | 10,680 CFO - 783 capex = 9,897 | `data/financials/gev_quarterly.csv`; 10-Q Q2'26 cash-flow statement | Yes |
| CL at 6/30/26, total / non-current / current | 40,037 / 93 / 39,944 | `gev_quarterly.csv` | Yes |
| CL by quarter Q4'23 to Q2'26 | 15,247; 16,115; 16,728; 17,107; 17,744; 18,851; 19,751; 20,304; 25,950; 31,949; 40,037 | same | Yes (10 of 10 up; prior Q3s +379, +553) |
| Street FY26 FCF | 12,196 | Bloomberg, 2026-10-01; Consensus sheet row 16 | Yes |
| Street Q3 / Q4 FCF | 1,502 (15 brokers) / 1,148 (15) | Bloomberg, 2026-10-01; `01_eeo_annual.xlsx` row 27 | Yes |
| Street Q3 FCF low / median / high | -1,622 / 1,482 / 7,062 | Bloomberg, 2026-10-01; `06_modl.xlsx` row 229 | Yes |
| Street Q3 current CL mean / median / low / high | 37,492 / 39,944 / 19,487 / 41,817 | `06_modl.xlsx` row 172 | Yes |
| Street Q3 change in CL mean / median / low / high | -1,402 / -50 / -8,795 / +1,873 | `06_modl.xlsx` row 205 | Yes |
| Cash taxes paid Q1'26 / Q2'26 / H1'26 | 534 / 724 / 1,258 | 10-Q Q1'26 and Q2'26 cash-flow statements | Yes |

## 2. Is the Street figure robust?

### 2.1 FY26 FCF: yes

| Vendor | FY26 FCF | Date | Note |
|---|---|---|---|
| Bloomberg BEst (annual) | 12,196 | 2026-10-01 | analyst count for the FCF row not in the pull |
| Bloomberg, quarterly panel | 9,897 + 1,502 + 1,148 = **12,548** | 2026-10-01 | 15 brokers; already at the guide top of 12,500 |
| S&P Global (via stockanalysis.com forecast page) | 12,020 | updated 2026-09-22 | 31 analysts on the forecast table |
| MarketScreener | 12,017 | fetched 2026-09-29 (`D07_q3_preview.md`) | |
| TIKR article | "about $12 billion" | 2026-09-27 | |

- Annual figures sit at 12.0-12.2B, the upper half of the 11.5-12.5B guide. Annual-implied H2 = 12,196 - 9,897 = 2,299.
- The brokers who publish quarters are at 12,548 for the year. For that panel "the Street copies the guide" is not accurate: it is already 0.4% above the guide top.
- The Q3 FCF range is -1.6B to +7.1B. At least one of 15 brokers already has a Q3 of 7.1B, so a deposit-driven beat is already in someone's published model. Mean without the high entry: 1,105.

### 2.2 Q3 CL balance (the candidate's "first test"): no

| Problem | Evidence |
|---|---|
| Contributor count hidden | The MODL export shows no broker values on rows 172 and 205. From mean / median / low / high alone, at least 7 brokers on the balance and at least 5 on the change are needed; the true count is unknown. |
| One entry is not a forecast of the reported line | Low = 19,487, about half the reported 39,944. Either a stale model or a different definition. It pulls the mean to 37,492. |
| The median is a default, not a view | Median balance = 39,944 = the last reported balance to the dollar; median change = -50. Brokers who do not forecast the line carry it forward. |
| The same Street's FCF contradicts "flat deposits" | Street Q3 EBITDA 1,672 - capex 296 = 1,376; Street Q3 FCF 1,502. With cash taxes of 534-724 a quarter (H1'26 run-rate) and 100-250 of other outflows, Street FCF embeds a net working-capital inflow of about **+760 to +1,100** in Q3. The fcf-deposits lens central for the Q3 CL build is +1,500. The FCF panel and the candidate are close for Q3. |
| Different panels | FCF: 15 brokers. Net debt: 11. CL rows: unknown. A gap between a 15-broker FCF and a thin CL line is a panel artefact. |

Reading: a 9/30/26 balance above 39,944 beats a placeholder. It is not evidence that the Street was wrong on cash.

## 3. Is the idea already stated?

| Date | Who | What was said | Source |
|---|---|---|---|
| 2026-07-22 | CFO, Q2 call | H1 FCF "substantially higher than the second half, as many of these slot reservations convert to orders"; Q3 FCF "positive"; down payments "correlate with the timing of orders" | corpus src:3161 |
| 2026-07-22 | BNP Paribas note, quoted by Utility Dive 07-23 | The 125 GW year-end figure reads as conservative given a "track record of under-guiding and over-delivering"; the market is "likely looking for" 130-140 GW at year-end | corpus src:301, src:239; utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/ |
| 2026-07-22/23 | Press (EBC, StockTi, Seeking Alpha) | $13.7B of H1 cash was customer advances; "working-capital benefit will moderate"; FCF timing (H1 above H2) listed as a key risk | ebc.com; stockti.com; seekingalpha.com/news/4616815 |
| 2026-09-16 | CEO, broker conference | H2 commitments of about 20 GW are "likely to prove to be conservative"; Q4 larger than Q3; 12 GW of added 2030-31 supply "in some form of contracting", mostly Q4; reservations carry "like, 25% down" | company transcript PDF (gevernova.com, Laguna 2026); Investing.com 09-16; TIKR 09-27; corpus src:681, src:3750 |
| 2026-09-16 | Host analyst, same event | "you've now increased free cash flow guidance multiple times this year" | same transcript |

What the public GW figure implies, using the candidate's own arithmetic ($950/kW, 20-25% down):

| Year-end GW | vs 125 guided | Extra deposits at 20% / 25% | FY26 FCF if the 12.0B guide midpoint was built on 125 GW, k = 0.5 / k = 1.0 |
|---|---|---|---|
| 130 | +5 | 0.95B / 1.19B | 12.5-12.6B / 13.0-13.2B |
| 135 | +10 | 1.90B / 2.38B | 13.0-13.2B / 13.9-14.4B |
| 140 | +15 | 2.85B / 3.56B | 13.4-13.8B / 14.9-15.6B |

- The candidate's central (14.5B) is what a 135-140 GW year-end produces. A broker said in July that the market is looking for 130-140 GW. The candidate's number is close to the published investor expectation, not different from it.
- Not found: a published sell-side FY26 FCF estimate above 12.5B, or a note that builds FCF from GW signed. Broker-level values are not visible in the pull. The 7.1B Q3 high shows at least one exists.
- The September Sell initiation ($470 target) argues 2027 margin and 2030 supply, not FY26 cash (GuruFocus, gmt8press summaries).

## 4. Has the stock moved?

| Date | Event | GEV close-to-close | Source |
|---|---|---|---|
| 2026-07-22 | FCF guide raised by 5.0B at the midpoint; margin guide held; EPS miss | 1,078.81 to 985.03 = **-8.7%** | corpus `prices` |
| 2026-09-14 | Sell initiation | 957.27 to 874.76 = -8.6% | corpus `prices` |
| 2026-09-16 | CEO: backlog $200B "very early" 2027; 20 GW H2 "conservative" | 882.81 to 925.09 = **+4.8%** | corpus `prices`; Investing.com; 247wallst |
| 2026-09-15 to 2026-10-01 | | 882.81 to 987.45 = **+11.9%** | corpus `prices`; Bloomberg, 2026-10-01 |

- The largest FCF raise on record came with the worst print-day reaction. A second deposit-driven cash beat has no record of moving the price.
- The signal behind the candidate (more GW than guided in H2) was given by the CEO on 16 Sep and the stock rose that day.

## 5. Ordinary explanations for the gap

### 5.1 The guide record, complete

Remainder = full-year guide less FCF already reported at the guide date. Sources: `mgmt_guidance` table, releases, `propose_fcf-deposits.md` section 2.6.

| Guide date | Implied remainder $B | Actual $B | Actual / top of range |
|---|---|---|---|
| 2024-04-25 | 1.36-1.76 | 2.36 | 1.34 |
| **2024-07-24** | 1.14-1.54 (H2) | 1.54 | **1.00** |
| 2024-10-23 | 0.17-0.57 | 0.57 | 1.00 |
| 2025-01-22 | 2.00-2.50 | 3.71 | 1.48 |
| 2025-04-23 | 1.03-1.53 | 2.74 | 1.79 |
| **2025-07-23** | 1.83-2.33 (H2) | 2.54 | **1.09** |
| 2025-10-22 | 1.10-1.60 | 1.81 | 1.13 |
| 2025-12-09 | 1.60-2.10 | 1.81 | 0.86 (inside) |
| 2026-01-28 (open) | 5.0-5.5 | 9.90 by H1 | 1.80 so far |
| 2026-04-22 (open) | 1.71-2.71 | 5.11 in Q2 | 1.88 so far |

- The candidate's proof lists six guides from 2025-04-23 on and says five of six finished above the top. The full record of completed remainders is 8: five above the top, **two exactly at the top (both 2024, omitted)**, one inside.
- The 1.79 multiple is the median of five guides, three of them issued in January or April. Guides issued in July (the like-for-like case for an H2 remainder): 1.00 and 1.09. Guides issued in July or later: 1.00, 1.00, 1.09, 1.13, 0.86; median 1.00.

| Multiple applied to the 2.60B top | H2 FCF $B | FY26 FCF $B | vs Bloomberg annual 12,196 | vs quarterly panel 12,548 | vs S&P 12,020 |
|---|---|---|---|---|---|
| 1.00 (guide top; July-or-later median) | 2.60 | 12.50 | +2.5% | -0.4% | +4.0% |
| 1.09 (best July guide) | 2.83 | 12.73 | +4.4% | +1.5% | +5.9% |
| 1.11 (median, all 8 completed) | 2.89 | 12.78 | +4.8% | +1.9% | +6.4% |
| 1.24 (median incl. the two open 2026 guides as floors) | 3.21 | 13.11 | +7.5% | +4.5% | +9.1% |
| 1.79 (candidate) | 4.65 | 14.55 | +19.3% | +16.0% | +21.1% |

### 5.2 Why H2 can be low without the guide being wrong

| Explanation | Evidence | Effect |
|---|---|---|
| Fewer new reservations | 40 GW of new commitments in H1; about 20 GW guided for H2 (CEO says conservative) | Deposits on new slots roughly halve even on a beat |
| Conversions bring little new cash | CFO ties the H1/H2 split to reservations converting to orders | A converted GW adds to orders and RPO, not much to CL |
| Q4-weighted signing | CEO: most of the 12 GW added supply contracts in Q4, Q4 above Q3 | Billed in December, collected in Q1: in Q4'25 CL rose 5.6B while receivables rose 2.4B; H2'25 cash kept per dollar of CL growth was 0.32. This pattern scaled gives FY26 of 11.6-12.1B, at or below the Street (candidate's own adverse case) |
| Cash taxes rising | 534 in Q1'26, 724 in Q2'26 vs 363 in all of H1'25; cause not disclosed | 1.3-1.7B in H2 on the H1 run-rate |
| Output ramp consumes cash | Gas output from about 3 to 5 GW a quarter from Q3; inventories -1.7B in H1; supplier advances up "across all segments" (10-Q Q2'26 MD&A); capacity secured "funded by customer down payments" (CEO) | Unsized outflow in inventories and supplier advances |
| Capex step-up | Guide includes about +30% R&D and capex; Street H2 capex about 0.72B after 0.78B in H1 | Small |
| Not explanations | Prolec accounting (Q1 only, non-cash 0.4B), FX, reclassification | No effect on H2 |

None of these proves the guide is right. Together they explain why management can guide H2 at 1.6-2.6B in good faith, and why the error band on any H2 estimate (11.6B to 16.4B in the candidate's own table) is wider than the gap.

## 6. Corrected figures (ranges and methods only)

| | Candidate | After this check |
|---|---|---|
| Street | 12,196 | 12,020-12,196 annual (three vendors); 12,548 for the 15 brokers with quarters |
| Research range | 12.7-16.4B, central 14.5B | 12.5B (guide top) to about 13.1B on the full guide record; deposit-model cases 11.6B to 14.6B |
| Gap vs Bloomberg annual | +19% | about +2.5% to +7.5%, centre near +5% |
| Gap vs quarterly panel | not shown | about 0% to +4.5% |
| Error band on the research value | "as wide as the gap" | about plus or minus 10% (11.6B to 14.6B around 12.8-13.1B) |
| Q3 CL test | balance vs 39,944 median | not a usable Street figure (section 2.2) |

## 7. Playbook tests this candidate fails

| Test | Result |
|---|---|
| The market expects X, sourced | Printed consensus is 12.0-12.5B, but a broker note says investors are looking for 130-140 GW, which maps to 12.5-15.6B. X is not what the market expects. |
| Reason the market missed it | Not missed: stated by the CEO on 16 Sep and by a broker on 22 Jul |
| Gap larger than the error band | No |
| A judge can check the proof in seconds | The guide record is quick to check, and the check shows two omitted 2024 guides that finished exactly at the top |
| The line moves the stock | No record: -8.7% on the day of the 5.0B FCF raise |

## 8. What could be kept

- "FY26 FCF finishes at or above the top of the guide" (7 of 8 completed remainders at or above the top). Direction: consistent with a long. Size: 0.3-0.9B, about $1-3 a share.
- The 28 Oct 2026 numbers worth recording against it: Q3 FCF vs 1,502; gas GW signed in Q3 vs the "about 20 GW for H2, Q4 larger" remark; any change to the 11.5-12.5B guide; year-end GW vs 125 guided and 130-140 looked for.
- Not checked: individual broker FCF models (not visible in the pull); whether the annual BEst mean still contains any estimate dated before 22 Jul 2026.

## 9. Sources

- Bloomberg, 2026-10-01: `GEV_bloomberg_pull_filled_2026-10-01.xlsx` (Consensus); `GEV_Pull_2026-10-01/01_eeo_annual.xlsx`, `01_eeo_growth.xlsx`, `06_modl.xlsx`, `segment_quarterly.json`.
- `data/financials/gev_quarterly.csv`; 10-Q Q2'26 (0001996810-26-000148) cash-flow statement, Note 4, MD&A cash flows; 10-Q Q1'26.
- `gev.db`: `mgmt_guidance`, `prices`, `sources` ids 3161 (Q2'26 call), 301 and 239 (Utility Dive, 2026-07-23), 681 and 3750 (conference coverage), 2674.
- Company transcript, broker conference 2026-09-16 (gevernova.com PDF).
- Web, fetched 2026-10-01: stockanalysis.com/stocks/gev/forecast/ (S&P Global consensus, updated 2026-09-22); ca.investing.com conference summary 2026-09-16; 247wallst.com 2026-09-16; tikr.com blog 2026-09-27; ebc.com 2026-07-23; stockti.com 2026-07-22; seekingalpha.com/news/4616815; gurufocus.com/news/9079408; gmt8press.com/content/detail/431387.
- Prior research: `propose_fcf-deposits.md`, `propose_winners-pattern.md`, `09_finrobot_overnight/BLOOMBERG_VERDICT.md`, `D07_q3_preview.md`.
