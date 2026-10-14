# Verify: power-services-fy28 against the wedge tests (2026-10-01)

_AI-assisted research input only. Facts, arithmetic, tables and sources. The team writes every memo sentence, chooses every forecast number and chooses the direction. Bloomberg data is licensed for academic use: keep it inside the project folder and cite it as "Bloomberg, 2026-10-01"._

Role: checker. The job was to try to kill the candidate. Rule: it survives only if it fails no more than two tests and passes the line-item, distance, error-band and reveal-date tests.

**Result: does not survive.** The candidate's arithmetic reproduces from the primary files. It fails on what the arithmetic means: the gap is the same size as its own error band, the year that settles it is outside the horizon, and one input (the "5.8% growth" history) is understated by an accounting item the candidate left open.

Source keys: 10-K25 = 0001996810-26-000015; 10-Q1'26 = -26-000064; 10-Q2'26 = -26-000148; 10-Q2'25 = -25-000133; 10-Q3'25 = -25-000160; 10-K24 = -25-000011. IU25 deck = corpus src:1844 (slide 28). Q2'26 call = corpus src:3161. Street = `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json` and `06_modl.xlsx` (Bloomberg, 2026-10-01).

---

## 1. What reproduced

| Item | Candidate | Recomputed | Source |
|---|---|---|---|
| Street Power services FY27 / FY28 / FY29 / FY30 $M | 15,675 / 17,665 / 19,711 / 22,357 | same | segment_quarterly.json, key `Total Revenue\|Power\|Services` |
| Street FY26 (H1 actual + Street H2) | 14,259 | 14,259 (6,598 + 3,389.0 + 4,271.5) | same |
| Street growth FY26 to FY30 | 8.1 / 9.9 / 12.7 / 11.6 / 13.4% | same | |
| Street quarterly growth Q3'26 to Q2'27 (vs recast comps) | 8.7 / 11.6 / 11.0 / 10.2% | same | comps 3,119e / 3,828e / 3,086 / 3,512 |
| Q3'26 mean / median / low / high | 3,389 / 3,329 / 3,167 / 3,737 | same | 06_modl.xlsx |
| Chart growth rate (12 to 22 over ten years) | 6.25% | 6.25%; 5.6% to 6.9% if both figures are rounded to the nearest $1B | IU25 slide 28 |
| Chart-path FY28 total | $15.8B to $16.7B | $15.81B to $16.72B | |
| Component build FY28 | $16.0B to $17.1B; $17.3-17.6B at 15% non-contract | same (16,017 to 17,063; 17,294 to 17,574) | Note 9 sentences, verified in each filing |
| Contract-service revenue H1'25 / H1'26 | 2,720 / 2,689 | same | 10-Q2'25, 10-Q2'26 Note 9 |
| Contract-service revenue FY25 | 5,412 | same | 10-K25 Note 9 |
| Profitability revisions H1'25 / H1'26 / FY25 | -42 / -218 / -151 | same | Note 9 |
| Power services H1'26 vs H1'25 | 6,598 vs 6,238, +5.8% | same | 10-Q2'26 p.29 |
| Power services RPO, 6/30/25 to 6/30/26 | +14.7% | 63,088 to 72,388, +14.7% | 10-Q2'26 |

No arithmetic error found in the candidate.

## 2. Three findings that change the reading

### 2a. The "5.8%" history is depressed by contract revisions

Note 9 lists "revenues recognized" and "net unfavorable changes in estimated profitability" as separate movements in the contract asset. Under percentage-of-completion accounting a change in estimated profitability is a catch-up adjustment to revenue (10-K25: revisions result "in an adjustment of earnings"; one point of profitability moves the contract asset by $0.2B). So reported Power services revenue most likely already nets these revisions. The candidate flagged this as an open question; the filings point one way, but no filing states it in one sentence, so treat it as probable, not certain.

| Period | Reported services $M | Revision $M | Services before revisions $M | Growth reported | Growth before revisions |
|---|---|---|---|---|---|
| FY23 | 11,838 | +34 | 11,804 | +5.4% | |
| FY24 | 12,419 | -319 | 12,738 | +4.9% | +7.9% |
| FY25 | 13,081 | -151 | 13,232 | +5.3% | +3.9% |
| H1'25 (recast) | 6,238 | -42 | 6,280 | | |
| H1'26 | 6,598 | -218 | 6,816 | +5.8% | +8.5% |
| Q1'26 | 3,086 | -89 | 3,175 | +4.3% | +8.4% |
| Q2'26 | 3,512 | -129 | 3,641 | +7.1% | +8.7% |
| Q4'25 | 3,802 | -115 | 3,917 | +3.7% | +1.7% |

- Growth before revisions was already about 8.5% in H1'26. The Street's next four quarters (+8.7% to +11.6%) are 0 to 3 points above that, not 3 to 6 points above 5.8%.
- The "steady 5%" of FY23-FY25 is partly coincidence: before revisions it was 7.9% then 3.9%.
- Comps: Q4'25, Q1'26 and Q2'26 carried -115, -89 and -129. If the matching quarters a year later carry no revision, reported growth gains about 3.0, 2.9 and 3.7 points with no change in the business. The candidate's pass mark (8% or less in each of Q4'26, Q1'27, Q2'27) can be missed on this alone.
- Q4'26 redone with the revision not repeating: contract 1,588 x 0.95-1.05 plus other services (3,828 - 1,588 + 115) x 1.11-1.16 = 4,123 to 4,399. Street is 4,272. Inside the range. (Candidate's version: 3,995 to 4,266.)

### 2b. The company's own five-year schedule for services is growing faster than the Street's path

Services RPO due within five years (company-wide; Power is 82% of services RPO), from the RPO note in each filing:

| As of | Services RPO $M | Within 5 years | Scheduled $M | Year on year |
|---|---|---|---|---|
| 6/30/24 | 73,915 | 52% | 38,436 | |
| 12/31/24 | 75,976 | 53% | 40,267 | |
| 6/30/25 | 78,938 | 53% | 41,837 | +8.8% |
| 12/31/25 | 85,993 | 52% | 44,716 | +11.0% |
| 3/31/26 | 87,352 | 53% | 46,297 | |
| 6/30/26 | 88,463 | 54% | 47,770 | +14.2% (12.1% to 16.3% after rounding) |

- Street Power services for the five years from Q3'26 ($93.9B) against the five years from Q3'25 ($84.6B, four quarters actual) is a ratio of 1.109.
- So the amount the company itself schedules for the next five years rose 12-16% in a year, and the Street's five-year total rose 11%. On this disclosed schedule the Street is not ahead of the company.
- Limit: the schedule covers about 40% of five-year services revenue, and Wind and Electrification services are in it.

### 2c. The chart is a floor, and a gap to a floor is expected

- Slide 28 (verified): gas + steam services about $12B (2025E) to about $22B (2035E), "accelerating in the 2030s", upgrades "at least 50% growth '25 to '30+", "strong escalation on existing contracts and price on new contracts".
- The CEO called the 2035 figure a floor, declined to quantify 2026-2028, and (September 2026, secondary source) called the path conservative. On the Q2'26 call: transactional orders per unit "rise by double digits annually"; services benefit from "increased volume and solid pricing".
- A sell-side analyst questioned the chart at the event itself. The Street sits above the chart knowingly. A constant-rate reading of a floor gives a lower bound, not a central estimate.

## 3. Corrected range (method only, no forecast chosen)

| Method for FY28 Power services | $B | vs Street 17.665 |
|---|---|---|
| Reported trend 5.5% a year from FY26 | 15.5-15.8 | -12% to -11% |
| Chart at constant rate + nuclear/hydro at 6-13% | 15.8-16.7 | -10.5% to -5.4% |
| Component build, contract 0-5%, other 11-13% | 16.0-17.1 | -9.3% to -3.4% |
| Growth before revisions (8.5%) held, revisions continue | 16.6 | -5.8% |
| Same, revisions fall to zero by FY28 | 17.0-17.2 | -3.6% to -2.9% |
| Component build with other services at 15% | 17.3-17.6 | -2.1% to -0.5% |
| Five-year schedule growth 11-14% applied to FY26 | 17.4-18.4 | -1.4% to +4.0% |

- Range across the chart, component and revision-adjusted methods: about $15.8B to $17.6B. Midpoint $16.7B, gap -5.5%. Half-width plus or minus 5.5%.
- The Street sits at the top edge of the range, not outside it.
- Annual sums of Street equipment + services differ from the Street Power total by -295 (FY27), +33 (FY28), -555 (FY29), +611 (FY30): the lines come from different sets of brokers. Contributor counts for division lines are not on the exports. FY30 is on the thinnest set.

## 4. The wedge tests

| # | Test | Result | Evidence |
|---|---|---|---|
| 1 | Line-item | **Pass** | Power segment services revenue, FY2028, Street $17,665M (Bloomberg, 2026-10-01). Named line, named year, sourced. |
| 2 | Consensus-side | Pass, qualified | The view rebutted is the Street mean, not an outlier. Qualifier: it is a division sub-line on an unknown, smaller broker set; the Q3'26 mean is 1.8% above the median; the price is set on total EBITDA (33 analysts for 2028), not on this split. |
| 3 | Distance | **Fail** | Central gap -5.5% (candidate -6.6%), under the 7% floor. Range -10.5% to about 0%. Near-term lines: FY27 -2%, Q3'26-Q2'27 -3.4% to +1.1%. On GEV EBITDA the gap is 2-7% for FY28, central about 4%. |
| 4 | Ratio | **Fail** | At Street numbers and a constant 28.5x, the September 2027 price is $1,292 (+31%). With the services cut (about $0.3-0.45B off NTM EBITDA of 11,782) it is $1,244-1,260 (+26% to +28%). The break-even multiple moves from 21.6x to 22.2-22.5x. A short earns only if the multiple falls more than 21%; the estimate gap supplies about 3 points. It is a multiple call. |
| 5 | Physical quantity | Fail (partial) | The HA cross-check ($25M per GW a year) bounds about $1.1B of the 2030 rise and says nothing about 2028. The rest is price, upgrades and transactional scope on the existing fleet, which has no hard ceiling. Shop capacity is mentioned by the company but not quantified. |
| 6 | Rival explanation | **Fail** | Three rivals fit the reported trend as well or better: (i) contract revisions masked 2.7 points of growth in H1'26 (section 2a); (ii) contract-service revenue is lumpy (+17.5% FY24, -1.1% FY25) and moves opposite to other services, so extrapolating the two parts separately is unstable; (iii) price: transactional orders per unit up double digits, services RPO +14.7%, five-year schedule +12-16%. The candidate does not show its variable is the one that moves. |
| 7 | Error band | **Fail** | Range half-width plus or minus 5.5% against a gap of 5.5%. Quarterly growth over ten quarters: mean 5.7%, standard deviation 2.7 points, range 2.2% to 11.6%; the difference between the Street (10-11.6%) and the candidate (6-9%) is 1 to 5 points. Revisions alone swing a quarter by about 3 points. No back-test exists for either method at a two-year distance; the chart dates from December 2025. |
| 8 | Why missed | **Fail** | The chart is on a public slide, was challenged by a sell-side analyst at the event, and has been called a floor by the CEO twice. The untagged Note 9 sentence is a real information gap, but it cuts both ways: the same sentence holds the revisions that explain the low reported growth. |
| 9 | Already priced | Pass, qualified | No sign the stock has moved on services. Qualifier for a short: the multiple is at the 6th percentile of its 12-month range and the stock is 16% below its June high. |
| 10 | Cash | Pass, qualified | Services drop through at 35-50%, so EBITDA moves: $0.3-0.8B in FY28 (candidate), about $0.3-0.5B at the corrected midpoint. Inside the horizon the effect on reported EBITDA is about -3% to +1% of the four-quarter Street figure ($8,210M), so earnings prints will not show it. |
| 11 | Reveal date | **Fail** | FY2028 Power services is reported in late January 2029, 27 months out. Inside the horizon there are only quarterly growth prints, where the gap is 0-3% and inside the noise (test 7); the January guide carries no services number; the capital markets day has no date. The dated reads do not separate the two views. |
| 12 | Counter-move | Fail | Each available move works against a short: the company has said the 2035 figure is a floor and may be raised; the 2028 outlook was raised in December 2025 and January 2026 and the FY26 guide three times; price escalation is built into contracts; revisions can stop. The candidate's own fail conditions (2035 raised to about $30B, 2028 margin target raised) are things management has signalled. |
| 13 | Multiple consistency | Fail (not shown) | No exit multiple is given. The thesis cuts FY28-FY30 EBITDA growth from 24.8% to about 22.7% a year, which does not by itself support a multiple 21% lower. No week in the last 12 months closed at or below 26x. |

Count: 4 pass (1, 2, 9, 10; three of them qualified), 9 fail (3, 4, 5, 6, 7, 8, 11, 12, 13). Required passes: line-item yes; distance no; error-band no; reveal-date no.

## 5. What is still usable

- As a model check, not a wedge: the Street's FY28 Power margin (23.3% vs the 22% target) rests partly on services growing 12.7%. The model's comparison tab can show its services growth rate with the revision effect on a separate row.
- Two dated facts to track regardless of direction: nine-month contract-service revenue and the profitability revision in the Q3'26 10-Q (2026-10-28; last year 3,824 and -36), and the same pair in the FY26 10-K (late January 2027; last year 5,412 and -151).
- The FY2030 extension has a larger gap (-14% central) but is further outside the horizon, on the thinnest broker set, and against a figure the company calls a floor.

## 6. Reproduce

```python
import json
d = json.load(open('data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json'))
S = 'Total Revenue|Power|Services'
fy = lambda y: sum(d[f'{S}|{y} Q{i}'] for i in range(1, 5))          # 15675, 17665, 19711, 22357
under_h1 = (6598 + 218) / (6238 + 42) - 1                            # 8.5% before revisions
sched = {'6/30/25': 78938 * .53, '6/30/26': 88463 * .54}             # 41,837 -> 47,770, +14.2%
be = lambda E: (987.45 * 266.334 - 8298) / E                         # break-even multiple
print(be(11782), be(11782 - 390))                                    # 21.6x, 22.4x
```
