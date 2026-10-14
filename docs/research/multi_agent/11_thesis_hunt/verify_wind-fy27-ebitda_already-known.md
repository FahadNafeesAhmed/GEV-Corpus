# Check: ALREADY KNOWN OR BAD DATA — candidate `wind-fy27-ebitda`

_Research input only: facts, arithmetic, sources. No memo sentences, no forecast choices (ranges and methods only). Bloomberg data cited as "Bloomberg, 2026-10-01" (academic licence, keep inside the project folder)._

**Verdict: does not survive as a wedge.** The numbers reproduce. But (1) the Street figure is the mean of about four broker models with a known high outlier, no dates and no dispersion for 2027; (2) the idea ("Wind is the drag, offshore runs into 2027") is public, and management said the opposite direction in public two weeks ago; (3) ordinary explanations remove about half of the gap and put the Street inside the range, not at its edge. It stays useful as a model input (a haircut range on the Wind line) and as a risk note on first-half 2027.

## 1. Reproduction (recomputed from the primary files)

| Item | Value | Source |
|---|---|---|
| Street Wind adjusted EBITDA 2027 by quarter | -9.2 / -11.8 / +58.6 / +150.0 = +187.7 | Bloomberg, 2026-10-01: `segment_quarterly.json` keys `Adjusted EBITDA||Wind|2027 Q1..Q4`; `street_segments_annual_2026-10-01.csv` wind_adj_ebitda 2027 = 188 |
| Second Bloomberg series, "EBITDA - company basis: Wind" 2027 | -8.0 / +15.5 / +65.5 / +115.5 = +188.5 | same JSON, `EBITDA||Wind` |
| Street H2 2026 / H1 2027 / H2 2027 Wind adjusted EBITDA | +207.8 / -20.9 / +208.6 | same |
| Street FY26 | -657 (H1 actual) + 24.6 + 183.2 = -449 | same; H1 from `data/financials/gev_segments.csv` |
| Street 2027 Wind revenue / offshore / onshore line | 7,589 / 795 / 6,873 (onshore + offshore = 7,668, not 7,589) | same JSON |
| Street 2028 Wind | +373 on 6,813 = 5.5% | CSV |
| Wind segment EBITDA actuals | H1 2024 -290; H1 2025 -311; H1 2026 -657; FY24 -588; FY25 -598 | `gev_segments.csv` (XBRL) |
| Offshore revenue actuals | FY24 1,377; FY25 652; H1 2026 551 | same |
| Incremental offshore contract losses | 2023 $379M; 2024 $1,005M; 2025 $637M | 10-K FY2025, revenue-recognition note (gev.db chunk 29831, accession 0001996810-26-000015) |
| Offshore year-end equipment backlog | 2023 about $4B; 2024 about $3B; 2025E about $2B; 2026E bar shown without a label | investor update deck 2025-12-09, slide 19 |
| Candidate arithmetic (steps 4-9) | reproduces: 272 - 600 = -328; 340 - 407 = -67; 476 - 280 = +196; -67 - 188 = -255 = 2.7% of 9,471 | |

Small corrections to the candidate text: H1 2025 is -311 (not -312); H1 2026 revenue is 3,458.

## 2. (a) Is the consensus figure robust? No.

- **About four brokers.** `06_modl.xlsx` (Bloomberg, 2026-10-01) gives the Q3 2026 Wind adjusted EBITDA line as mean 24.6316, low -9.0, high 106.3853, median 0.5705. With four contributors, the two middle estimates must sum to 4 x 24.6316 - (-9.0) - 106.3853 = 1.1410, so the median is 0.5705. That matches the reported median to six decimals. Larger counts are not excluded but need a coincidence. The consolidated EBITDA consensus has 36 contributors.
- **Mean is pulled up by one model.** For Q3 2026 the mean is +24.6 and the median is +0.6; the company guide is "approximately break-even". One estimate at +106 adds about 24 to the mean. The 2027 quarters show a mean only (no low, high, median or count). If the same high model runs through 2027, the +188 mean overstates what the typical model has. This cannot be measured from the export.
- **The candidate's early read is affected.** "Q3 Wind vs Street +$25M" uses the skewed mean. Against the median (+0.6) a break-even print is in line.
- **Undated.** The export hides individual broker cells for this line (one broker is visible on the "EBITDA company basis" row at +23.8). Bulk sheet: 19 of 45 listed brokers have a recommendation date between 07-22 and 08-05 (the Q2 report); 12 are dated 09-17 or later. Recommendation date is only a proxy for model date. Consolidated FY27 EBITDA consensus moved 9,302 (07-17) to 9,427 (07-24) to 9,451 (09-25): no visible cut after the Q2 Wind loss, no move after the 09-16 conference.
- **Internally inconsistent block.** The two Wind EBITDA series agree for the year (187.7 vs 188.5) but not by quarter (Q2 2027 -11.8 vs +15.5; Q4 2027 150.0 vs 115.5), so they come from different broker sets. Onshore + offshore revenue lines sum to 7,668 against a segment line of 7,589. The Wind RPO line for Q3-Q4 2026 is corrupted by one entry (high 112,612 against a median of 19,756; the mean implies about six contributors).
- **No second vendor.** Web search on 2026-10-01 found no Visible Alpha, FactSet, LSEG or company-compiled figure for 2027 Wind EBITDA, and no broker note printing one. One search connector needed authorisation and was not used.
- Sum of division means for 2027: 5,906 + 3,774 + 188 - 455 = 9,413, against the consolidated mean of 9,471 (36 brokers). The Wind line does not tie to the number the price reflects.

Reading: "+$188M" is the average of roughly four models, at least one of which is far above the guide for the nearest quarter. It is a weak stand-in for market expectations.

## 3. (b) Is the idea already stated? Yes in general form; the by-parts number was not found in print.

Company statements (all public):
- Conference, 2026-09-16 (company-hosted transcript, pp. 2-3 and 10): Wind is "reaching a profitability pivot point"; "'27 will be much better than '26"; profitability "will be drastically better, going forward"; the company expects "a healthy positive change in margin in backlog in Wind" at year-end. Syndicated 09-18 (gev.db sources 681 and 3750).
- Q2 2026 call, 2026-07-22: FY26 Wind about -$400M reaffirmed; Q3 "approximately break-even"; "lower project costs for Offshore" in Q3.
- Q1 2026 call, 2026-04-22: Dogger Bank B and C "through the better part of '27".
- Investor update, 2025-12-09: "As we reduce the existing Offshore backlog, we expect EBITDA losses to improve"; 2028 Wind target 6% with "both Offshore Wind projects in backlog complete".
- 10-K FY2025 wording: "could result in further losses beyond the amounts that we currently estimate."

Third-party (the bear point in general form):
- Reuters 2026-07-22: second-quarter core profit missed estimates "as losses in its Wind business widened".
- New Energy Weekly 2026-07-23, Lark Research 2026-08-04, Finsee (Q1 2026 review): each notes that the FY26 guide needs a positive second half and flags guidance risk.
- TIKR blog (April 2026): lists Wind losses staying above $400M as the risk to the 2028 margin target.
- Motley Fool 2026-08-17: Wind called a "dead weight"; argues investors ignore it because Power and Electrification offset it.

Not found: any source that backs out offshore EBITDA from the onshore margin comments, applies a loss-to-backlog ratio, or prints a 2027 Wind figure. The method is new; the conclusion it points to is a known risk.

## 4. (c) Has the stock moved on it?

| Date | Event | GEV close-to-close |
|---|---|---|
| 2024-10-23 | Q3 2024: Wind -317, offshore charge $676M | +1.3% |
| 2026-01-28 | FY25 Wind -598 against a -400 guide | +2.7% |
| 2026-04-22 | Q1 2026 Wind -382 | +13.8% |
| 2026-07-22 | Q2 2026 Wind -275; consolidated EBITDA missed | -8.7% |
| 2026-09-16 | Vineyard settlement and "pivot point" remark | +4.8% |

Source: gev.db `prices`; Bloomberg PricePositioning for September. Three of four Wind disappointments came with the stock up. The one down day (07-22) had a consolidated miss. A $255M Wind shortfall is 2.7% of FY27 EBITDA; the record says this line alone does not move the stock.

## 5. (d) Ordinary explanations

**5.1 Loss-contract accounting.** The 10-K states "We provide for a potential loss on these agreements when it is expected that we will incur such loss", and the $379M / $1,005M / $637M are "incremental" losses from changes in estimates. The expected loss on remaining work is already provided; later revenue is booked at about zero margin unless estimates change again. The candidate's 28-43% "loss / opening backlog" is therefore three years of repeated estimate changes, not a margin on backlog. Each year had a named cause: 2024 blade events; Q4 2025 the US stop-work order on Vineyard (the call on 2026-01-28 ties the Q4 accrual to it and says no "significant additional negative EBITDA impacts" are expected for that project); Q1 2026 "higher contract losses". Vineyard installation finished in Q1 2026 and the dispute was settled on 2026-09-16. The 2027 backlog is Dogger Bank B and C only. Applying a ratio earned on a backlog that included Vineyard to a backlog that does not is not like-for-like.

**5.2 The Street is a guide-follower here.** FY26 guide -400 (Street -449); Q3 guide break-even (Street median +0.6); guide-implied H2 2026 = -400 + 657 = +257 (Street +208); 2028 target 6% (Street 5.5%). Street 2027 has H2 flat on H2 2026 (+209 vs +208) and H1 at about break-even. The +188 sits 77% of the way from the FY26 figure to the FY28 figure ((188 + 449) / (373 + 449)).

**5.3 The onshore margin input does half the work.** The candidate's centre uses 5% for 2027 onshore. Stated history: about 7% / "high single digit" for 2024 (January 2025 call; 2025 proxy letter), high single digit guided for 2025, mid-single digit for 2026 (lower volume plus tariffs on contracts signed before the tariffs; about $70M in Q1 2026 alone). Offshore loss the Street needs = onshore margin x 6,794 - 188:

| Onshore margin 2027 | 4% | 5% | 6% | 7% | 8% |
|---|---|---|---|---|---|
| Onshore EBITDA | 272 | 340 | 408 | 476 | 544 |
| Street-implied offshore loss | 84 | 152 | 220 | 288 | 356 |

At 7-8% the Street-implied offshore loss (288-356) falls inside the candidate's own offshore range (280-600). Moving the centre from 5% to 7% removes 136 of the 255 gap.

**5.4 First-half bridge.** H1 2026 -657 included tariff costs on unprotected contracts and offshore charges ("higher contract losses" Q1, "higher project costs" Q2), neither quantified. Segment EBITDA before incremental offshore charges was -187 in both H1 2024 and H1 2025 (on revenue 3,701 and 4,095), and +304 / +226 in H2 2024 / H2 2025 (the 2024 figure also removes the $300M settlement gain). Street 2027: H1 -21 on 3,388; H2 +209 on 4,201. So the Street's H2 is at or below the ex-charge history; the Street's H1 is 166 better than the ex-charge history on lower revenue. This is the one place where the candidate's direction is supported by reported numbers. Size: 166, or 1.8% of FY27 EBITDA, before any new charge.

**5.5 What does not explain it away: the guide record.** Annual Wind guidance has missed in both completed years: 2024 "approaching profitability" (held through October 2024), actual -588; 2025 "-200 to -400", then "about -400" (October 2025), actual -598. 2026 quarterly guides were met at the weak end (Q1 -300 to -400, actual -382; Q2 -200 to -300, actual -275). So "analysts follow a reliable guide" is not available as a defence of the Street; "analysts follow the guide" is.

**5.6 Unknown sign.** Vineyard settlement terms are confidential (company claimed $300-360M owed; customer claimed $850M of damages). Its Q3 2026 effect could be either sign and resets the base.

## 6. Corrected figures

| Item | Candidate | After this check |
|---|---|---|
| Street FY27 Wind adjusted EBITDA | +188 | +188 mean of about 4 models, undated, no median; nearest-quarter mean is 24 above its median |
| Range by parts | -328 to +196, centre -67 (onshore 4-7%, centre 5%) | -328 to +264 with onshore 4-8%; centre about 0 at 6% onshore and the same offshore centre (408 - 407). Ex-charge cross-check: H1 at -187 with Street H2 +209 gives +22 before any new offshore charge |
| Gap to Street | -255 (-136% of the line; 2.7% of FY27 EBITDA) | about -165 to -190 at the corrected centres (about -100% of the line; 1.7-2.0% of FY27 EBITDA); range -516 to +76 (-5.4% to +0.8%) |
| Position of the Street | "top edge of the range" | inside the range |
| Early read Q3 2026 | vs Street +25 | vs median +0.6 (break-even guide) |

## 7. Qualifiers the team must carry if the item is used

1. Model input and risk note only; not a thesis line. Error band (about plus or minus $300M) is larger than the gap.
2. Street Wind figure: about four models; say so wherever the +188 appears.
3. The offshore loss is a string of estimate changes under loss-contract accounting, not a run-rate; the remaining projects are Dogger Bank B and C only.
4. Management's public stance (2026-09-16) is the opposite direction; annual Wind guides missed in 2024 and 2025.
5. The supportable piece is first-half 2027 (-21 Street vs -187 ex-charge history); test dates are the January 2027 guide and the Q1 2027 guide.
6. Vineyard settlement effect in Q3 2026 is unknown.
