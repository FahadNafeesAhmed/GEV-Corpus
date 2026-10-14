# Verify: electrification-q3-orders against the wedge tests

Checker working, 2026-10-01. Research input only. Verdict: DOES NOT SURVIVE (4 tests pass, 9 fail; the error-band test, which is required, fails).

## 1. Sources re-read

| Tag | Source |
|---|---|
| BBG-Q | Bloomberg, 2026-10-01: `01-eeo-company-specific.xlsx` row 68 (Orders > Electrification), row 73 (RPO), row 29 (revenue); `segment_quarterly.json` key `Orders||Electrification|2026 Q3` |
| BBG-M | Bloomberg, 2026-10-01: `06_modl.xlsx`, Q3'26 single period, row "Orders Received Value: Electrification" |
| R | Earnings releases, segment tables, Q1'24 to Q2'26 (corpus `chunks`, 8-K exhibits; Q1'26 = 0001996810-26-000063, Q2'26 = 0001996810-26-000147) |
| CONF | Company-posted transcript of the 2026-09-16 investor conference (gevernova.com, 11 pages; pages 1, 3, 6, 7 read) |
| CALL | Q2'26 call transcript (corpus `sources.id=3161`), Q3'25 call (3771), Q4'25 call (2660), Q1'26 call summary (1849) |
| PX | corpus `prices` table (GEV daily close) |

## 2. What reproduces

| Item | Candidate | Re-computed | Status |
|---|---|---|---|
| Street Q3'26 Electrification orders, mean | 6,498 | 6,498.1 | ok (BBG-Q, BBG-M) |
| Low / median / high | 5,775 / 6,307 / 7,498 | 5,774.9 / 6,306.7 / 7,498.4 | ok (BBG-M) |
| Orders implied by the Street's RPO path | 6,316 | 46,998.4 - 44,563 + 3,880.7 = 6,316.1 | ok |
| Street Q4'26 | 7,492 | 7,492.0 | ok |
| H1'26 orders | 13,460 | 7,112 + 6,347 = 13,459 (release prints 13,460) | ok |
| Data-centre orders H1 | 5,000-5,380 | Q1 2,400 + Q2 2,700 = 5,100 = 37.9% of H1 | ok (CALL) |
| Quote | "almost 40%", "probably more like 20% ... in 3Q and 4Q" | verbatim on CONF p.6 | ok |
| Centre | 4,130 / 0.80 = 5,160; -20.6% | with disclosed 5,100: 4,180 / 0.80 = 5,224; -19.6% vs mean, -17.2% vs median | ok, small shift |
| Report date | 2026-10-28 | company events page lists the Q3 webcast for 2026-10-28 | ok |
| Report-day moves | +1.5, -4.5, +3.1, +14.6, +13.75, -8.69% | +1.46, -4.45, +3.07, +14.58, +13.75, -8.69% | ok (PX) |
| Move on 2026-09-16 | +4.8% | 882.81 to 925.09 = +4.79% | ok (PX) |

Not available: the number of brokers behind the 6,498 mean. The broker columns on that row are blank in BBG-M. Mean, median, low and high together need at least 5 contributors; 35 brokers publish EBITDA.

## 3. Context in the same transcript that the candidate does not carry

- CONF p.6, same sentence as the 20%: "while growing the backlog, both the Electrification backlog and the data center backlog, in 3Q, 4Q, but maybe not at the same run rate as the first half".
- CONF p.7: "I expect us to continue to grow our backlog in a very healthy way in both 3Q and 4Q in Electrification. But by default, Electrification can be a little bit more lumpy, both with data centers and, frankly, the non-data center business".
- CONF p.1 and p.3: "$200 billion milestone we should hit very early in 2027" on "the strength of the orders we expect to see in the third quarter"; "a very strong third quarter orders performance" (total company, from slot reservations converting to orders).
- CALL Q2'26: "we anticipate continued solid equipment orders with healthy margins" for Q3 Electrification.

The remark fixes a RATIO (data-centre share), not a LEVEL. The level in the candidate comes from a separate assumption: orders outside data centres stay at the H1'26 average.

## 4. The assumption tested

Orders outside data centres, by quarter ($M). Data-centre orders: Q3'25 $400M and nine-month 2025 about $900M (CALL Q3'25); 2025 "over $2 billion" (CALL Q4'25), so Q4'25 about 1,100; Q1'26 2,400; Q2'26 2,700. The H1'25 split of 250/250 is an assumption.

| Quarter | Total orders | Data centre | Share | Other orders | Change on prior quarter |
|---|---|---|---|---|---|
| Q1'25 (recast) | 3,366 | ~250 | 7% | ~3,116 | |
| Q2'25 (recast) | 3,283 | ~250 | 8% | ~3,033 | -3% |
| Q3'25 | 5,110 | 400 | 8% | 4,710 | +55% |
| Q4'25 | 7,424 | ~1,100 | 15% | ~6,324 | +34% |
| Q1'26 | 7,112 | 2,400 | 34% | 4,712 | -25% |
| Q2'26 | 6,347 | 2,700 | 43% | 3,647 | -23% |

Back-test of the candidate's rule (next quarter = average of the prior two quarters) on other orders: Q3'25 -35%, Q4'25 -39%, Q1'26 +17%, Q2'26 +51%. Mean absolute error 35%.

Same rule on total Electrification orders, Q3'23 to Q2'26 (12 tests): mean absolute error 39.5%, median 36.7%; 9 of 12 errors are larger than 20.6%. "Next quarter = last quarter": mean absolute error 37.6%, 9 of 13 larger than 20.6%. Quarter-on-quarter changes range from -57% to +91%.

Total orders used (R): Q1'23 3,856; Q2'23 5,011; Q3'23 2,143; Q4'23 2,193; Q1'24 3,571; Q2'24 4,823; Q3'24 2,510; Q4'24 4,786; Q1'25 3,393; Q2'25 3,338; Q3'25 5,110; Q4'25 7,424; Q1'26 7,112; Q2'26 6,347.

Gap claimed: 20.6% (19.6% on the disclosed inputs). Back-test error: 35-40%. The error is about 1.8x the gap.

What the Street number needs, given the same 20% share: other orders of 6,498 x 0.80 = 5,198 and data-centre orders of 1,300. Other orders were 4,712 in Q1'26, 4,710 in Q3'25 and about 6,324 in Q4'25, so 5,198 is inside the last four quarters' range. Data-centre orders of 1,300 are half the H1 pace, which also fits "won't likely go at that same run rate". The Street number is therefore consistent with the same remark.

Sensitivity (total orders; gap to 6,498):

| Other orders | 20% share | 25% share | 30% share |
|---|---|---|---|
| 3,647 (Q2'26) | 4,559 (-30%) | 4,863 (-25%) | 5,210 (-20%) |
| 4,180 (H1 average) | 5,225 (-20%) | 5,573 (-14%) | 5,971 (-8%) |
| 4,712 (Q1'26) | 5,890 (-9%) | 6,283 (-3%) | 6,731 (+4%) |
| 5,198 (Street-consistent) | 6,498 (0%) | 6,931 (+7%) | 7,426 (+14%) |

One order the size of the Q3'25 Saudi award (1,600) is 1.26x the whole dollar gap (1,274).

## 5. The 13 tests

| # | Test | Result | Evidence |
|---|---|---|---|
| 1 | Line-item | PASS | One line (Electrification segment orders), one period (Q3'26), sourced consensus 6,498.1 (BBG-Q, BBG-M). Qualifier: it is an orders line, not revenue, profit or cash. |
| 2 | Consensus-side | PASS, weak | The number rebutted is the Bloomberg mean, not an outlier; the median (6,307) and the RPO-implied figure (6,316) agree with each other. Contributor count unknown, at least 5 of 35 brokers. |
| 3 | Distance | PASS at the centre only | -19.6% to -20.6% vs mean, -17.2% vs median: inside the 7-22% zone. The sign is not robust: with Q1'26-level other orders and a 25-30% share the gap is -3% to +4%; the second lens reaches +12%. |
| 4 | Ratio | FAIL | No target price or return; direction is "either". Year-on-year Electrification order growth vs report-day move, 10 reports Q1'24-Q2'26: correlation -0.14. No return can be attributed to this line. |
| 5 | Physical quantity | FAIL | Consensus converts to data-centre orders of 1,300 and other orders of 5,198, book-to-bill 1.67. All sit inside the company's last four quarters (other orders 3,647-6,324; book-to-bill 1.7-2.5). No ceiling or own-history check rejects the Street. Dollar amounts, not units. |
| 6 | Rival explanation | FAIL | The same 20% remark fits the Street (section 4). The CEO called the non-data-centre business lumpy too and guided "very healthy" backlog growth in Q3 and Q4; the CFO guided "continued solid equipment orders". Timing of single large awards, Prolec orders (about 840-890 a quarter by the gap between reported and organic growth) and FX are not separated. |
| 7 | Error band | FAIL (required) | Back-test error 35-40% vs gap 19.6-20.6% (section 4). |
| 8 | Why missed | FAIL | The input is a remark at a conference hosted by a covering broker, posted by the company and repeated in a public news write-up the same week (corpus `sources.id=681`). That is a timing lag in broker models, not a structural gap in disclosure. |
| 9 | Already priced | FAIL | The remark was public on 2026-09-16; the stock closed +4.79% that day and stood at $987.45 on 2026-10-01 (+6.7% from the 09-16 close). The market heard it and paid up for total orders. No evidence the price depends on this line. |
| 10 | Cash | FAIL | No change to revenue, EBITDA or EPS in the horizon. Deposit effect of a 1,274 order shortfall at 10-22.5% (contract liabilities / equipment RPO was 22.5% at 6/30/26): $127-287M, 1.1-2.4% of the FY26 FCF guide midpoint. The shortfall is 6.3% of Street total Q3 orders (20,332), and Power orders may offset. |
| 11 | Reveal date | PASS | Company-reported cell, 2026-10-28, levels set in advance (below 5,775; 5,900 or less; above 6,300). Qualifiers: 5,900-6,300 is a dead zone; the date is 4 weeks out, before the 3-month start of the horizon, and nothing follows it. |
| 12 | Counter-move | FAIL | Booking date is partly in management's and customers' hands (conversion of reservations, when a large award "cuts in"). One 1,600 award closes 126% of the gap. Not stressed in the candidate. |
| 13 | Multiple consistency | FAIL | No exit multiple and no valuation link. |

Count: 4 pass (1, 2, 3, 11), 9 fail (4, 5, 6, 7, 8, 9, 10, 12, 13). Rule: no more than 2 fails, and tests 1, 3, 7 and 11 must pass. Test 7 fails. Not a wedge.

## 6. Corrected figures for anyone who still uses the line

- Street: 6,498 mean; 6,307 median; 6,316 implied by the Street's own RPO path. Range 5,775-7,498.
- Method value (range, not a forecast): centre 5,225 on disclosed inputs (other orders 4,180 a quarter, 20% share). Band from the back-test: plus or minus 35-40%, about 3,100-7,300. The Street sits inside the band.
- What remains usable: a dated accuracy check only. It cannot carry a position.
