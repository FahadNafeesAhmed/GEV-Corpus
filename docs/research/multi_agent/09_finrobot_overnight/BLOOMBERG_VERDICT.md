# Bloomberg pull and verdict (2026-10-01)

_AI-assisted research input only. The team writes every memo sentence, chooses every forecast number and chooses the direction. Bloomberg data is licensed for academic use: keep it within the team and cite it as "Bloomberg, 2026-10-01"._

Source file: `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` (BEst mean consensus, Standard source). Price $987.45, enterprise value $254,694M, 266.33M shares.

## 1. The Street by year (Bloomberg BEst)

| Year | Revenue $M | Adj. EBITDA $M | Margin | Growth | Analysts | High / low | Std dev | FCF $M |
|---|---|---|---|---|---|---|---|---|
| 2025 actual | 38,068 | 3,196 | 8.4% | | | | | 3,710 |
| 2026 | 46,240 | 6,334 | 13.7% | | 35 | 6,823 / 5,112 | 280 | 12,196 |
| 2027 | 53,029 | 9,471 | 17.9% | +49.5% | 36 | 11,029 / 6,612 | 917 | 7,654 |
| 2028 | 60,985 | 12,553 | 20.6% | +32.5% | 33 | 17,141 / 4,786 | 2,235 | 9,527 |
| 2029 | 70,851 | 16,496 | 23.3% | +31.4% | 21 | 19,385 / 14,183 | 1,348 | 9,702 |
| 2030 | 79,724 | 19,544 | 24.5% | +18.5% | 20 | 25,769 / 16,314 | 2,147 | 13,036 |

- The 2025 actual matches GEV's adjusted EBITDA ($3,196M), so the series is on GEV's definition.
- Medians: 6,384 / 9,364 / 12,862 / 16,504 / 19,403.
- Quarterly: Q3'26 $1,672M (26 analysts), Q4'26 $2,500M, Q1'27 $1,810M, Q2'27 $2,228M.

## 2. Gap test

| Year | Street | Research build | Research vs Street | In Street standard deviations |
|---|---|---|---|---|
| 2027 | 9,471 | 8,744 (range 8,600-8,900) | -7.7% | 0.8 below |
| 2028 | 12,553 | 11,190 | -10.9% | 0.6 below |
| 2029 | 16,496 | 15,400 (range 10,800-20,400) | -6.6% | 0.8 below |
| 2030 | 19,544 | about 17,300 | -11.5% | 1.0 below |

- **No long-side gap.** The Street does not flatten margins after 2028. It has 2029 above the research build, with 21 analysts, and that estimate has risen 27% this year (12,958 on 2026-01-02 to 16,496).
- **The research sits 7-11% below the Street in every year, inside the Street's own range.** It is a below-consensus view, not an outlier. It rests on management's path and on a cautious Wind and starting-point assumption (see `ROBUSTNESS_PACK.md` T6 and T7).
- **Against GEV's 2028 framework ($11,200M):** the Street is +12.1%, not +16.6% as the free vendor showed. Revenue is +8.9% above the framework's $56B; the Street's margin (20.6%) is close to the framework's 20%.

## 3. Are estimates moving?

| EBITDA consensus | 2026-01-02 | 2026-04-03 | 2026-07-03 | 2026-07-31 | 2026-09-04 | 2026-09-25 | 2026-10-01 |
|---|---|---|---|---|---|---|---|
| 2027 | 8,003 | 8,631 | 9,273 | 9,443 | 9,427 | 9,451 | 9,471 |
| 2028 | 10,535 | 11,783 | 12,716 | 12,712 | 12,459 | 12,511 | 12,553 |
| 2029 | 12,958 | 14,392 | 15,526 | 15,933 | 16,009 | 16,088 | 16,496 |

2027 is flat to slightly up since July. 2028 dipped about 2% in August-September. 2029 is still being raised.

## 4. The multiple (Bloomberg, weekly, forward EV/EBITDA)

- Today 28.5x. Twelve-month range 27.3x to 42.4x, median 32.5x. Today sits at about the 6th percentile.
- **No week in the last twelve months closed at or below 26x.** The March-April 2025 sell-off reached about 18-21x.
- Peers today: Quanta 22.3x, Eaton 21.1x, Vertiv 20.6x, ABB 18.7x, Schneider 16.5x, Hubbell 15.6x, Mitsubishi Heavy 15.2x, Siemens Energy 12.5x, Hitachi 11.9x, Baker Hughes 10.9x, Bloom Energy 51.7x.
- Two-year EBITDA growth: GEV 40.8%, Siemens Energy 27.4%, Mitsubishi Heavy 15.9%. Multiple divided by growth: GEV 0.70, Siemens Energy 0.46, Mitsubishi Heavy 0.95.
- The Street has Siemens Energy's margin levelling near 20% from fiscal 2028 (15.5 / 17.8 / 19.4 / 20.0 / 20.3%) while GEV's keeps rising to 24.5% in 2030.

## 5. Price by scenario (price = (multiple x NTM EBITDA + $8,298M) / 266.33M)

| | NTM EBITDA | Break-even multiple | 21x | 23x | 25x | 27.3x (12-month low) | 28.5x |
|---|---|---|---|---|---|---|---|
| September 2027, Street | 11,782 | 21.6x | $960 (-3%) | $1,049 (+6%) | $1,137 (+15%) | $1,239 (+25%) | $1,292 (+31%) |
| September 2027, research | 10,578 | 24.1x | $865 (-12%) | $945 (-4%) | $1,024 (+4%) | $1,115 (+13%) | $1,163 (+18%) |

| | NTM EBITDA | Break-even multiple | 23x | 25x | 26x | 27.3x | 28.5x |
|---|---|---|---|---|---|---|---|
| January 2027, Street | 9,728 | 26.2x | $871 (-12%) | $944 (-4%) | $981 (-1%) | $1,028 (+4%) | $1,072 (+9%) |
| January 2027, research | 8,948 | 28.5x | $804 (-19%) | $871 (-12%) | $905 (-8%) | $948 (-4%) | $989 (0%) |

## 6. Positioning and demand

- Ratings: 32 buy, 7 hold, 2 sell. Average target $1,225. The two sells are small firms (targets $841.50 and $976.87). Mizuho is neutral at $949 (2026-09-30).
- Short interest 8.8M shares, 3.3% of float, 4.6 days to cover; the peak was 11.7M in early July 2026.
- Thirty-day implied volatility 48%. Put-to-call open interest rose from 1.06 in January to 1.45.
- US 10-year yield 5.16%.
- Data-centre builders' capex consensus (Microsoft, Alphabet, Amazon, Meta, Oracle): about $844B, then $1,111B (+32%), then $1,203B (+8%). Every one rose through 2026. Growth slows sharply in the third year.

## 7. Verdict under the draft rule

| Rule row | Result |
|---|---|
| Street 2029 at least 7% below the research build | No. The Street is 7% above it |
| Street 2027 or 2028 at least 7% above the team's model, and a multiple of 26x or lower is common | Estimate half: yes on the research numbers (the team's model is not built). Multiple half: no. Zero weeks at or below 26x in twelve months |
| Anything else | **This row applies: a 12-month long, stated openly as a call on the multiple** |

What the long rests on: the stock is at the bottom of its one-year multiple range after falling 16% from its June high while estimates rose; on the Street's numbers it breaks even at 21.6x in September 2027, and on the research numbers at 24.1x; the Street's 31% growth for 2029 supports the multiple.

What can break it: the multiple falling toward peers (about 21x for US electrical names) as growth slows, as it did in March-April 2025; the January guide; a slowdown in data-centre capex growth, which the Street already shows for the third year.

## 8. Still worth pulling

`MODL` and the EEO "Company-Specific" tab (forecasts by division, for the model's comparison tab), and `EEB` for 2028 (the low estimate of $4,786M and the high of $17,141M explain the wide spread).

## 9. The Street by division (added after the full export set)

Source: the EEO "Company-Specific" exports in `data/bloomberg/GEV_Pull_2026-10-01/`, quarterly forecasts summed to years (`data/bloomberg/street_segments_annual_2026-10-01.csv`). Quarterly sums differ slightly from the annual consensus because fewer brokers supply quarters, and very few supply 2029-2030.

| Year | Power revenue $M (equipment / services) | Power margin | Electrification revenue $M | Electrification margin | Wind revenue $M | Wind margin | Corporate $M | Sum $M |
|---|---|---|---|---|---|---|---|---|
| 2027 | 28,121 (12,150 / 15,674) | 21.0% | 17,704 | 21.3% | 7,589 | 2.5% | -454 | 9,391 |
| 2028 | 33,520 (15,888 / 17,665) | 23.3% | 21,269 | 23.4% | 6,813 | 5.5% | -473 | 12,879 |
| 2029 | 39,521 (19,256 / 19,710) | 25.3% | 24,959 | 24.6% | 7,381 | 8.1% | -478 | 16,231 |
| 2030 | 45,215 (23,469 / 22,356) | 26.9% | 28,421 | 25.6% | 7,440 | 8.5% | -507 | 19,471 |

GEV's own numbers for comparison: FY26 guide Power 17-19%, Electrification 18-20%, Wind about -$400M; 2028 targets Power 22%, Electrification 22%, Wind 6%, revenue $56B.

What this changes:

- **The Street's 2027 Power margin is 21.0%.** The earlier "Street needs Power at 21.7-23.5%" was a back-solve and it was wrong. The research build had 20.5%.
- **The 2027 gap is three small differences, not one view.** Street minus research: Power +$267M (half a point of margin and 2% more revenue), Electrification +$193M (0.8 points), Wind +$187M, corporate +$20M.
- **2028 is where the Street is clearly above the company:** Power 23.3% and Electrification 23.4% against a 22% target for each, and revenue of $61.4B against $56B. Wind is slightly below its target.
- **The earlier "research is 7% below the Street on 2029" was not a view.** It came from a placeholder Electrification figure. On Power, the order-vintage build ($10.9B base, range $7.3-15.4B) is 9% above the Street's $9.98B. With the Street's own Electrification, Wind and corporate figures, the research total for 2029 is about $17.1B, 4% above the Street. That is inside the error band and under the 7% threshold.
- **Conclusion unchanged: no gap in either direction that survives the research's own uncertainty.** The Street's division forecasts are consistent with the order-vintage margins.

Other exports: Bloomberg's relative-value screen (EQRV) puts GEV's forward EV/EBITDA at its two-year average (0.1 standard deviations above), forward P/E 0.4 above, EV/EBIT 1.4 below. The supply-chain screen lists customers but no single customer above 1% of revenue.

## 10. Second pass: the one place the Street disagrees with GEV's own filing

Test: the Street's equipment revenue for the next four quarters against the amount GEV says will convert from backlog in that window (10-Q Q2'26, remaining performance obligations note: "Equipment-related RPO of $87,821 million of which 36%, 65%, and 97% is expected to be recognized within 1, 2, and 5 years").

| Backlog date | Equipment RPO $M | Share within 1 year | Scheduled $M | Next four quarters $M | Ratio | Ratio excluding Prolec | Basis |
|---|---|---|---|---|---|---|---|
| 12/31/24 | 43,047 | 44% | 18,941 | 20,934 | 1.105 | 1.105 | all reported |
| 3/31/25 | 45,478 | 45% | 20,465 | 21,991 | 1.075 | 1.048 | all reported |
| 6/30/25 | 49,712 | 42% | 20,879 | 23,556 | 1.128 | 1.061 | all reported |
| 9/30/25 | 54,092 | 41% | 22,178 | 25,158 | 1.134 | 1.033 | 1 quarter is Street |
| 12/31/25 | 64,245 | 37% | 23,771 | 27,534 | 1.158 | 1.028 | 2 quarters are Street |
| 3/31/26 | 75,924 | 38% | 28,851 | 28,956 | 1.004 | 1.004 | 3 quarters are Street |
| **6/30/26** | **87,821** | **36%** | **31,616** | **30,245** | **0.957** | **0.957** | all Street |

- In the three fully reported windows, equipment revenue came in 5-11% above the scheduled conversion (new orders that book and ship inside the year). The Prolec adjustment is an estimate (about $3.1B of 2026 revenue).
- **For the next four quarters (Q3'26 to Q2'27) the Street's equipment revenue ($30,245M) is below the scheduled conversion itself ($31,616M; $31,176-32,055M allowing for rounding of the 36%).**
- With the historical uplift of 3-6%, implied equipment revenue is $32.6-33.5B, which is $2.3-3.3B (8-11%) above the Street. With no uplift at all it is $1.4B (4.5%) above.
- On total revenue (Street $50,019M for the four quarters, 22-28 analysts): about +2% to +7%, central about +4%. The gap is concentrated in the first half of 2027.
- Profit effect is small: at an 12-25% margin on the extra equipment revenue, about +$0.2-0.8B against the Street's $8,210M of EBITDA for the four quarters (+2% to +10%).

Limits, stated plainly:
- Only three windows are fully reported, so the back-test is short.
- The Street's equipment / services split comes from the division consensus; individual broker values are not visible on this terminal. The total-revenue version of the test does not depend on the split.
- GEV's own FY26 revenue guide sits near the Street, and management knows its schedule. Either the guide is cautious again (it was raised three times in 2026), or deliveries slip (section 9 of `ROBUSTNESS_PACK.md` notes one slip).
- This stock has moved on the margin guide, not on revenue beats. GEV's record is revenue and cash beats with margin in line.
- A year-two version of the test (months 13-24) is consistent with the Street and shows no gap.

Reading: this is the first number that still differs from the Street after real consensus data. It supports "revenue beats and raises continue through mid-2027", which helps the 12-month long. It is a modest edge on revenue, not an edge on profit.

Other second-pass checks:
- Bloomberg's relative-value screen shows GEV's forward EV/EBITDA premium to its benchmark at its two-year average. In absolute terms the multiple is at a one-year low, but relative to the market it is not cheap.
- The Street's Q4'26 needs Wind at about +$180-210M, a record quarter, as GEV's own guide implies.
- The 2028 spread among analysts is wide (standard deviation 18% of the mean; low $4,786M, high $17,141M); the median ($12,862M) is 2.5% above the mean.
