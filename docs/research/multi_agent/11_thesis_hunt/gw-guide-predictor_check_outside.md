# Check: ordinary explanation and already known — rebuild "gw-guide-predictor"

_Research input only: facts, arithmetic, tables, sources. No memo sentences. No forecast chosen for the team. Bloomberg figures are cited as "Bloomberg, 2026-10-01" and stay inside the project folder._

Working date 2026-10-01. All money in $M unless stated. Checked file: `gw-guide-predictor.md`.

**Result: does not survive as a thesis.** The rebuild's own verdict (holds = false, direction = none) is confirmed. Its numbers reproduce. Its exhibit (the Street in physical terms) is usable, with a label on data quality.

## 0. Verdict against the test

| Test | Result |
|---|---|
| Numbers reproduce from the primary files | Yes (section 1) |
| No ordinary explanation removes the gap | Fails. The Street's 2030 Power equipment line is reproduced three ordinary ways with no gap (section 2) |
| Gap is real after like-for-like comparison | Fails. Headline +2.6% revenue / +4.6% EBITDA falls to +1.3% / +1.3% on one basis; -2% to +1% with two further neutral choices (section 3) |
| Not already published | Fails. One large broker publishes a 2030 equipment figure above the rebuild's centre; management has said in public that its markers are conservative (section 4) |
| Street figure solid | Fails for the division lines; weak for company 2030 (20 estimates, spread 11%, no history) (section 5) |
| A company-reported number inside 12 months settles it | In form only. Two outlooks, not results; second date not set; the Street moves first (section 6) |
| **survives** | **false** |

## 1. What was recomputed

All from `segment_quarterly.json`, the workbook sheets `Consensus` and `ConsensusHistory`, `02-eeo-annual-2030.xlsx`, `06_modl.xlsx`, the 10-Q / 10-K Power tables in `gev.db`, and company documents on gevernova.com.

| Item | Rebuild | Recomputed |
|---|---|---|
| Street Power equipment 2027-30 | 12,151 / 15,888 / 19,256 / 23,469 | same |
| Street Power services 2030; Power 2030 | 22,357; 45,215 | same |
| Company 2030 annual mean: revenue; EBITDA (count, std dev, low, high) | 79,724; 19,544 (20; 2,147; 16,314; 25,769) | same; median 19,403 |
| Sum of 2030 quarters: revenue / EBITDA (models) | 80,718 / 19,471 (12 / 11) | same |
| Power equipment RPO and firm GW, price in backlog | $465 (9/30/24), $575 (9/30/25), $618 (12/31/25), $741 (6/30/26) | same; also $483 at 12/31/24 |
| k (implied equipment $/kW over price in backlog) | 0.99 and 1.16; mean 1.07 | 0.99 and 1.16; mean 1.074. Ranges 0.78-1.19 and 1.03-1.28 |
| Year-end 2026 price in backlog | $799-829 | $799-829 |
| 2030 on the rule: company revenue low / centre / high | 74,776 / 81,781 / 87,919 | 74,777 / 81,780 / 87,916 |
| 2030 EBITDA, method 2 | 17,946 / 20,445 / 23,738 | 17,947 / 20,445 / 23,737 |
| FY26 Power on H1 actual + Street H2; FY27 Street growth | 23,609; +19.1% | same |
| Outlook against Street on the eve (Dec 2025; Jan 2026) | revenue -0.6%, +3.4%; EBITDA +12.3%, +6.8% | same (rows 2025-12-05, 2026-01-23) |
| Street today against the 2028 framework ($56B; $11.2B) | +8.9%; +12.1% | same |
| Company statements (Dec 2024 deck and release; Dec 2025 deck, release, transcript; Jan 2026 deck; 2026-09-16 conference) | as quoted | confirmed in the company PDFs |

One citation to fix: the rebuild cites corpus source 3886 for "30 GW in 2030 at about $900/kW". The corpus copy of that article (5,944 characters) does not hold that sentence. Other copies of the same article do (for example legacycapitaledge.com, 2026-07-25): they report that the broker model now has 30 GW shipped in 2030 at about $900/kW, and that revenue and EBITDA projections were raised by $8B and $2B.

## 2. Ordinary explanations of the Street figure (no gap needed)

Street 2030 Power equipment = $23,469M (Bloomberg, 2026-10-01).

| # | Ordinary reading | Arithmetic | vs Street |
|---|---|---|---|
| A | Company plan volume at today's price in backlog | 30 GW x $741 x 1.06 | 0% (the rebuild's own exhibit) |
| B | Company plan volume at the order price management guided for H2 2026, with the back-tested conversion | 30 GW x $871 x 0.90 = 23,516. Range $838-904: 22,635 to 24,397 | +0.2% (-3.6% to +4.0%) |
| C | The same form year by year: Street equipment / plan GW / 0.90 | 2028: $736/kW (24 GW). 2029: $792 (27 GW). 2030: $869 (30 GW) | Each equals the price of the orders that ship in that year: Q4 2025 to Q1 2026 orders $713-735 for 2028; H2 2026 guide $838-904 for 2030 |
| D | Analysts extend the company framework | Street Power 2025-28 CAGR 19.2% (framework: high-teens). Street Power 2028-30 CAGR 16.1%. Street company 2028-30 CAGR 14.3% (framework: low-teens to 2028) | The framework growth rates carried on two more years |
| E | Gas-only version | Street 2030 less $1.5-3.5B of non-gas equipment = $20.0-22.0B = 30 GW x $666-732. Gas-only price in backlog today (RPO less $3-4B non-gas) = $665-684 | Same conclusion without the non-gas book |

- $838 = $729 x 1.15 and $904 = $753 x 1.20 (management guided H2 2026 order prices to the higher end of 10 to 20 points above Q4 2025; deck and derived Q4 2025 prices).
- Reading B is the 2030 twin of kill reason 1 (Street 2028 = 24 GW x $735 x 0.90 = 15,876).
- FY27: Street Power +19.1% on FY26. One contributor carries exactly 18.0% organic growth in all eight 2027-28 quarters. The company framework says high-teens. The FY26 guide is 18-20%. The rebuild's centre (17.5%) is 1.4% below the Street. No gap, and the sign is opposite to the 2030 centre.
- The rebuild agrees with reading A in its own section 8 and section 9, row 1.

## 3. Where the rebuild's +2.6% / +4.6% centre comes from

The centre is not produced by the rule alone. It comes from four choices stacked together.

| Choice in the rebuild | Neutral alternative | Effect on the centre gap |
|---|---|---|
| Centre is built from Street division lines (quarterly models; they sum to 80,718) but compared with the annual mean (79,724) | Compare with the sum of quarters, the same broker set | Revenue gap +2.6% becomes +1.3%. The two bases differ by 994 (1.25%) |
| EBITDA centre uses a 25% margin; the Street has 24.5% | Use the Street margin | Of the +901 EBITDA gap, +396 is the margin assumption and +504 is revenue. On the same basis and Street margin: +260 (+1.3%) |
| k = 1.07, mean of two values taken on the 9/30 price in backlog | k on the year-end price ($483, $618), which is the date basis used for the forward step: 0.95 and 1.08, mean 1.02. Management said in December 2025 that the outlook is tied to the price in backlog at that time, which is k = 1.0 | Equipment 26,258 becomes 24,830 (k 1.02) or 24,450 (k 1.0). Company revenue against the sum of quarters: -0.5% / -0.9% |
| Price in backlog is all-in ($815 at year-end, lifted by 61 aeroderivative units) | The rebuild's own ex-aeroderivative price, $762-790 (mid $776) | With k 1.07: -0.2%. With k 1.02: -1.9% |

Decomposition of the centre against the sum of quarters (80,718): equipment +2,789; services -1,607; Wind -640; eliminations -90; Electrification 0. Total +1,062 (+1.3%).

Corrected centre gap: **+1.3%** on revenue and on EBITDA (same basis, Street margin). Range across the neutral choices above: about -2% to +3%. In units of the Street's own spread (std dev 2,147): +4.6% is 0.42; +1.3% is 0.12.

Error band: the rebuild's own low-to-high EBITDA range is -8.2% to +21.5% (half-width about 15%). Outlook-against-Street back-test: EBITDA -12% / +12% / +7%; revenue -2.8% / -0.6% / +3.4% (mean about zero). Band of about +/-13% to +/-15% stands. The gap is well inside it.

Per share: +$901M at 13.0x = +$44. The like-for-like +$260M = +$13 (1.3% of $987.45).

## 4. Already published

| Who / when | What is public | Source |
|---|---|---|
| Large broker note, 2026-07-23 | 30 GW shipped in 2030 at about $900/kW = $27.0B. That is 15% above the Street mean for the line and 2.8% above the rebuild's centre ($26.3B). Revenue and EBITDA projections raised by $8B and $2B | press copies of the same article, 2026-07-25 (not in the corpus copy 3886) |
| Second broker, 2026-07-27 | Raised its FY2030 adjusted EBITDA estimate by 5% after Q2 | investing.com |
| Third broker, 2026-07-22 | Order price per class: about $790/kW heavy-duty, $950 HA combined-cycle scope, $1,800 aeroderivative | corpus source 301 |
| Bloomberg, 2026-10-01 | Highest 2030 EBITDA estimate 25,769 (+32%). The rebuild's high case is 23,737 | workbook sheet Consensus |
| Company, 2025-12-09 | Deck assumption: pricing reflects recent orders; 20 GW then about 24 GW in 2028. Listed upside: price above current order levels | gevernova.com deck p.8-9 |
| Company, 2026-09-16 | The 2035 services marker ($22B) is called conservative. A 2030 financial case, split into equipment and services, comes at the next capital markets day (expected in spring, before summer). The date is to be set on the January call. Stock +4.8% on the day (882.81 to 925.09) | gevernova.com transcript; corpus sources 681, 686, 1265, 1747, 3750 |
| Press, 2026-07-25 | An investor event with refreshed 2028 and 2030 guidance was already expected | same article as row 1 |
| Press, 2026-08-28 | An article notes how quickly the December 2024 framework was replaced: raises to frameworks are a known pattern | Seeking Alpha |
| Sell note, 2026-09-14 | Opposite view: 2027 EBITDA 22% below consensus; premium-priced orders only from 2029 | GuruFocus, Seeking Alpha |
| Street path | 2028 consensus is 8.9% (revenue) and 12.1% (EBITDA) above the standing framework. FY2028 EBITDA consensus +19% and FY2029 +27% since 2026-01-02 | workbook sheet ConsensusHistory |

- The method (GW x $/kW + services) is the standard broker build.
- The event, its timing and its likely direction are public. The Street already sits above the company's last outlook.
- Not found: a published statement that the 2030 outlook will be above or below a named Street figure by a stated percentage.

## 5. How solid is the Street figure for the periods used

| Line | What the pull shows |
|---|---|
| Company 2030 EBITDA, annual | 20 estimates; std dev 11%; low -17%, high +32%; mean 0.7% above median |
| Company 2030 revenue, annual | Mean 79,724. The count was not pulled |
| 2030 quarterly models | 12 for revenue, 11 for EBITDA. Their sum is 1.25% above the annual revenue mean and 0.4% below the annual EBITDA mean |
| Power equipment and services, 2030 | Contributor count hidden. Equipment + services is 611 above the Power total (2.6% of the equipment line). Gas + nuclear + hydro is 704 above the Power total. The lines rest on different broker sets |
| Power organic growth | Exactly 9.0% in all eight quarters of 2029-30 and exactly 18.0% in all eight of 2027-28: one model |
| Nearest quarter (Q3 2026) Power equipment | Mean 2,394; low -13.8%; high +8.3%; no broker values shown (`06_modl.xlsx`) |
| History | None for 2030 and none for any division line. The outlook-against-Street back-test cannot be run for the line the rebuild claims |

The inconsistency inside the division lines (1.3% to 2.6%) is as large as the corrected gap.

## 6. Can a company-reported number inside 12 months settle it

| Event | Inside 12 months | What it settles |
|---|---|---|
| 2026-10-28, Q3 10-Q: Power equipment RPO and firm GW | Yes | An input (price in backlog). Not the claim |
| Late January 2027: FY27 Power growth guide; 10-K RPO and firm GW | Yes | An outlook. Rebuild's centre is 1.4% below the Street; back-tested one-year guides missed by -3 and +8 points |
| Spring 2027 capital markets day: 2030 outlook | Likely (date not set; before summer) | An outlook, not a result. Format unknown (earlier outlooks were stated as minimum figures). FY2030 results print in early 2031 |

- The comparison is with the Street on the eve, which cannot be known today. After the December 2025 outlook the Street's 2028 EBITDA rose 12% in one week.
- The two events point in opposite directions in the rebuild (FY27 below, 2030 above). No position follows from them.

## 7. Weak points in the back-test itself

1. Two outlooks. The December 2024 Power figure is a residual: the release gave company revenue ($45B) and segment margins only, no Power revenue. Its k ranges from 0.78 to 1.19.
2. The January 2026 restatement kept the same Power figures while the price in backlog had moved from $575 to $618. On that date k = 1.08, not 1.16.
3. The one-year method fails (rebuild section 4). The rebuild says so.

## 8. What can still be used

| Use | Status |
|---|---|
| Exhibit: the Street in physical terms (Street Power equipment buys 16.4 / 21.4 / 26.0 / 31.7 GW in 2027-30 at $741/kW; or plan GW at $608 / $662 / $713-741 / $782) | Usable. Label it as Bloomberg division lines with hidden contributor count, and show the 0.90-conversion version next to it (order price $736 / $792 / $869) |
| Driver structure (GW x price in backlog x k + services) | Standard build. Usable with k = 1.0 and wide ranges; k = 1.07 is not supported |
| A claim that the 2030 outlook or the FY27 guide will beat the Street | Not supported |

What would change this result: a division-level broker table for 2030 with at least 8-10 visible contributors; a 2030 consensus history; or a company statement of delivery year and price by order vintage.

## 9. Reproduce

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
yr = lambda s, y: sum(d[f'{s}|{y} Q{q}'] for q in range(1, 5))
EQ, SV, PW = 'Total Revenue|Power|Equipment', 'Total Revenue|Power|Services', 'Total Revenue||Power'
EL, WI, TOT = 'Total Revenue||Electrification', 'Total Revenue||Wind', 'Total Revenue||Total Revenue'
A_REV, A_EB = 79723.7, 19544.4                    # workbook sheet Consensus, 2030
S_eq, S_tot = yr(EQ, 2030), yr(TOT, 2030)         # 23,469 ; 80,718
print(S_tot / A_REV - 1, yr(EQ, 2030) + yr(SV, 2030) - yr(PW, 2030))            # +1.25% ; +611
# ordinary reading B and C
print([30 * p * 0.90 / S_eq - 1 for p in (729 * 1.15, (729 * 1.15 + 753 * 1.20) / 2, 753 * 1.20)])   # -3.6% / +0.2% / +4.0%
print({y: round(yr(EQ, y) / g / 0.90) for y, g in ((2028, 24), (2029, 27), (2030, 30))})            # 736 / 792 / 869
# k on both date bases
imp24 = (45000 + 450 - 8000 - 7550 * 1.17 * 1.125 ** 3 - 12419 * 1.06 ** 4) / 20                    # 460
imp25 = (19767 * 1.18 ** 3 - 13081 * 1.08 ** 3) / 24                                                 # 667
k_a = (imp24 / (11392 / 24.5) + imp25 / (18977 / 33)) / 2                                            # 1.074
k_b = (imp24 / (12461 / 25.8) + imp25 / (24707 / 40)) / 2                                            # 1.016
# centre and its corrections
co = 30 * 815 * k_a + 20750 + yr(EL, 2030) + 6800 - 450                                              # 81,780
m = A_EB / A_REV
print(co / A_REV - 1, co / S_tot - 1, co * .25 / A_EB - 1, (co - S_tot) * m / A_EB)                 # +2.6% / +1.3% / +4.6% / +1.3%
for price, k in ((815, 1.0), (815, k_b), (776, k_a), (776, k_b)):
    print(price, round(k, 3), (co - 30 * 815 * k_a + 30 * price * k) / S_tot - 1)                    # -0.9% / -0.5% / -0.2% / -1.9%
```

Web pages were read with the Exa fetch and search tools. The Firecrawl connector was not authorised in this session (it needs authorising through /mcp or the connector settings before it can be used).
