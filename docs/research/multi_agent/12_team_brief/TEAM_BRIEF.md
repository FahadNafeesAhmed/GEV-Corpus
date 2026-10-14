# GEV team brief: research notes for the memo and the model

_AI-assisted research input, to be disclosed under rule 10. This is not submission text. The team writes every memo sentence and builds the Excel model itself. Bloomberg figures are licensed for academic use: keep them within the team and cite them as "Bloomberg, 2026-10-01"._

Working date 2026-10-02. Money in $ millions unless stated.

## 0. Rules and deadline

- Deadline: **11:59 pm ET, 2 October 2026**. The form closes automatically. One person submits.
- Deliverables: a memo PDF of at most two pages (appendix included), an Excel valuation model, and a resume for each team member. Memo and model are blinded: no university, club or member names, including in file properties.
- Rule 10: AI may be used for initial research if clearly disclosed. The Submission (memo and model) "must not be generated in whole or in part" by a generative AI tool. So the sentences and the spreadsheet are the team's.
- The rules ask for: thesis and recommendation with the return profile; tangible, technical evidence with a predictive part; industry and competitors; strengths and weaknesses including management; upside and downside risks; justified model assumptions and the valuation process; cited data sources; public information only.
- Judging: quality and viability of thesis, model and thesis alignment, logic of model assumptions.

## 1. The call

Long GE Vernova, 12 months, to 30 September 2027. Price $987.45 (Bloomberg, 2026-10-01).

Answer key for a simple model that uses Bloomberg annual consensus directly:

| Case | FY2027 EBITDA | FY2028 EBITDA | Forward EBITDA at Sept 2027 | Multiple | Price | Return |
|---|---|---|---|---|---|---|
| Bear: GEV's own plan | 8,590 | 11,200 | 10,548 | 21x | $855 | -13.4% |
| Base: Street consensus | 9,471 | 12,553 | 11,783 | 25x | $1,126 | +14.0% |
| Bull: base plus 5% | 9,945 | 13,181 | 12,372 | 28.5x | $1,341 | +35.9% |

- Forward EBITDA at the target date = 25% of FY2027 + 75% of FY2028.
- Price = (multiple x forward EBITDA + net cash) / diluted shares.
- Weighted 25 / 50 / 25: $1,112 (+12.6%).
- Break-even multiple (price ends flat): 21.8x.
- Return split in the base case, on one consistent basis: today's multiple measured the same way as the target is 29.6x = (price x diluted shares - net cash) / (25% of FY2026 + 75% of FY2027 EBITDA = 8,687). Holding 29.6x gives $1,328 (+34.5% from EBITDA growth). The fall to 25x takes away 20.4%. Net +14.0%.
- The same split using Bloomberg's quoted 28.5x as today's multiple: +29.7% ($1,281) and -15.7%. Bloomberg's 28.5x rests on its own forward EBITDA (about 8,923), which a simple model cannot reproduce. Use one basis and say which. The target, the break-even and the three cases do not change.
- Price at other multiples on base EBITDA: 19x $864, 21x $951, 23x $1,039, 27x $1,214.
- Bear EBITDA path: FY2026 guide midpoint (46,000 x 13% = 5,980), 2028 framework (56,000 x 20% = 11,200), FY2027 halfway between (8,590).
- The reference model built during research rebuilds the forecast by segment and gives $1,134 for the base. The memo must quote the team's own model.

## 2. Valuation inputs and sources

| Input | Value | Source |
|---|---|---|
| Share price | $987.45 | Bloomberg, 2026-10-01 |
| Shares, basic | 266.334M | 10-Q Q2 2026, cover |
| Dilutive shares | 3M | 10-Q Q2 2026, Note 18 |
| Cash, including restricted | 13,120 | 10-Q Q2 2026, cash flow statement |
| Restricted cash | 400 | 10-Q Q2 2026, liquidity section. Rounded: the filing says "$0.4 billion" |
| Total borrowings | 2,849 | 10-Q Q2 2026, borrowings note (total, including current maturities) |
| Noncontrolling interests | 1,158 | 10-Q Q2 2026, balance sheet |
| Net cash used in the bridge | 8,713 | 13,120 - 400 - 2,849 - 1,158 |
| Forward EV/EBITDA today, as Bloomberg quotes it | 28.5x | Bloomberg, 2026-10-01 |
| The same multiple on the model's own basis | 29.6x | (987.45 x 269.334 - 8,713) / 8,687 |
| 12-month range of that multiple | 27.3x to 42.4x, median 32.5x | Bloomberg weekly history |
| Analyst ratings | 32 buy, 7 hold, 2 sell | Bloomberg, 2026-10-01 |
| Average price target | $1,225 | Bloomberg, 2026-10-01 |
| Short interest | 3.3% of float | Bloomberg, 2026-10-01 |

Street consensus (Bloomberg, 2026-10-01):

| | FY2026 | FY2027 | FY2028 | FY2029 |
|---|---|---|---|---|
| Revenue | 46,240 | 53,029 | 60,985 | 70,851 |
| Adjusted EBITDA | 6,334 | 9,471 | 12,553 | 16,496 |
| EBITDA margin | 13.7% | 17.9% | 20.6% | 23.3% |
| Number of estimates | 35 | 36 | 33 | 21 |
| Power equipment revenue | 9,342 | 12,151 | 15,888 | 19,256 |
| Power services revenue | 14,259 | 15,675 | 17,665 | 19,711 |
| Power EBITDA | 4,418 | 5,906 | 7,810 | 9,983 |
| Electrification revenue | 14,766 | 17,704 | 21,270 | 24,959 |
| Electrification EBITDA | 2,724 | 3,774 | 4,972 | 6,130 |
| Wind EBITDA | (449) | 188 | 373 | 598 |

Notes on the table. FY2026 segment figures are H1 2026 actual plus H2 2026 consensus. The segment EBITDA rows are Bloomberg's adjusted EBITDA by segment, which matches GEV's own segment measure. Bloomberg also carries a plain EBITDA-by-segment series that differs by 1-2% (Power FY2027 5,826, FY2028 7,949). Segment lines come from fewer brokers than the annual totals, so they do not add up exactly to the annual EBITDA.

Peers, forward EV/EBITDA (Bloomberg): Siemens Energy 12.5x, Mitsubishi Heavy 15.2x, Eaton 21.1x, Vertiv 20.6x, Quanta 22.3x, Hubbell 15.6x, ABB 18.7x, Schneider 16.5x, Hitachi 11.9x, Baker Hughes 10.9x. Median of the ten 16.0x.

## 3. Company facts (10-K FY2025, 10-Q Q2 2026)

| | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|
| Revenue | 33,239 | 34,935 | 38,068 | 17,143 | 20,442 |
| Adjusted EBITDA | 807 | 2,035 | 3,196 | 1,227 | 2,146 |
| Power revenue | 17,436 | 18,127 | 19,767 | 9,234 | 10,449 |
| Power equipment | 5,598 | 5,708 | 6,686 | 2,996 | 3,851 |
| Power services | 11,838 | 12,419 | 13,081 | 6,238 | 6,598 |
| Power EBITDA | 1,722 | 2,268 | 2,902 | 1,303 | 1,842 |
| Electrification revenue | 6,378 | 7,550 | 9,642 | 4,001 | 6,597 |
| Electrification EBITDA | 234 | 679 | 1,433 | 519 | 1,200 |
| Wind revenue | 9,826 | 9,701 | 9,110 | 4,095 | 3,459 |
| Wind EBITDA | (1,033) | (588) | (598) | (312) | (657) |
| Gas turbine GW sold | 13.8 | 11.9 | 15.3 | 8.2 | 7.5 |
| Gas turbine GW ordered | 9.5 | 20.2 | 29.8 | 12.2 | 20.1 |
| Power equipment revenue per kW sold | $406 | $480 | $437 | $365 | $513 |

- H1 2025 is restated to the 2026 segment basis.
- Guidance for FY2026 (Q2 2026 release): revenue 45.5-46.5B, EBITDA margin 12-14%, Power margin 17-19%, Electrification margin 18-20%.
- 2028 framework (Q4 2025 release): revenue 56B, margin 20%; Power 22%, Electrification 22%, Wind 6%.
- Prolec GE was acquired on 2026-02-02 and adds about $3.1B of Electrification revenue in FY2026.

## 4. The thesis in gigawatts

Power equipment revenue = gigawatts shipped x dollars per kW.

| Question | What the Street needs | What GEV has | Settled? |
|---|---|---|---|
| Price | $579/kW in 2027, $662 in 2028 | $741/kW in signed backlog; $513 realised in H1 2026 | Yes |
| Demand | Buyers for 111 GW of planned output, H2 2026 to 2030 | 53 GW firm + 63 GW reserved = 116 GW | Yes |
| Output | 20 GW a year from Q3 2026 | 14.6 GW in the last four quarters | No |

Numbers behind the table:

- Street price per kW = Street Power equipment revenue / GW on the company's path (17.5, 21, 24, 26 GW for 2026-29): $534, $579, $662, $741. The GW path is not a Street figure. 2026 is 7.5 actual plus 5 a quarter. 2028 is the stated 24 GW rate. The 21 GW for 2027 and 26 GW for 2029 are readings of the plan, not numbers the company gave.
- Signed backlog price = $39,261M Power equipment backlog (10-Q Q2 2026) / 53 GW (Q2 2026 release). It is all-in: it includes non-gas equipment and moves with product mix.
- Planned output H2 2026 to 2030 = 10 + 21 + 24 + 26 + 30 = 111 GW. Reservations are paid factory slots, not orders, and some firm orders deliver in 2031.
- GW sold by quarter: Q1 2025 3.0, Q2 2025 5.2, Q3 2025 4.0, Q4 2025 3.1, Q1 2026 4.2, Q2 2026 3.3. Plan: 5 a quarter from Q3 2026, a step up of 37% on the last four quarters. GEV shipped 5.2 GW in Q2 2025.
- Street price per kW by half-year at the stated output: H1 2026 actual $513, H2 2026 $549, H1 2027 $538, H2 2027 $615.
- What ships next: 70 HA turbines (the largest class) in backlog at 6/30/26. Unit roll: 32 at 12/31/24 + 43 ordered - 24 sold in 2025 = 51; + 27 ordered - 8 sold in H1 2026 = 70. Between 62 and 70 of them were ordered in 2025 or later.
- Margin: Power EBITDA margin 14.7% (2025), 17.6% (H1 2026); Street 18.7% (2026), 21.2% (2027), 23.3% (2028). Power is about 62% of Street 2028 EBITDA.
- Near-term check: 36% of the $87,821M equipment backlog is due within a year = $31,616M, against Street equipment revenue of $30,245M for Q3 2026 to Q2 2027 (+4.5%). In seven past windows, actual revenue beat the scheduled amount six times. The profit effect is small: about $0.2B.

What these numbers support: the Street's forecast assumes GEV's own output plan at prices already signed. It needs no new orders and no new price rises.

What they do not support: any claim that the Street is too low by a stated percent. Three attempts at that failed their error tests.

## 5. Why output is the limit (manufacturing)

- First-stage turbine blades run in gas hotter than the melting point of their own metal. Each is a single-crystal nickel casting with cooling channels and a ceramic coating. (Trade press and standard engineering references in the corpus.)
- Four Western foundries make them at scale: Precision Castparts, Howmet, CPP, Doncasters. They also make jet-engine blades. (Trade press.)
- GEV, Q2 2026 call, 22 July 2026 (primary): output moves from about 3 GW a quarter to 5 from Q3 2026 and is on track; 325 new machines installed, about 400 by year end; workers hired and trained a year ahead; the 2028 step to 24 GW depends on castings and forgings arriving in 2027; new HA units reach their first major outage four years after start.
- GE Aerospace, a separate company, agreed in September 2026 to buy CPP for $11.75B, closing in H2 2027. (News.)
- Wood Mackenzie: world capacity 60-70 GW a year against 110 GW of orders; turbine orders expected to peak in 2026. (Press release and trade press.)
- One industry estimate has world capacity rising from 67 to 102 GW a year by 2030. Mitsubishi Heavy expects demand of about 70 GW a year on average over five years. (Mitsubishi: its FY2025 Q4 investor Q&A, primary.)
- Units sold (10-K, 10-Q): heavy-duty turbines 54 in 2025, 15 in Q1 2026, 13 in Q2 2026. HA units 24 in 2025, 5 in Q1 2026, 3 in Q2 2026.

Reading: the factory limit supports the next 12 months of earnings (capacity is installed) and protects price (all three makers share it). It also caps upside in volume, and "sold out" means orders must slow, which is a reason for a lower multiple.

## 6. What the market thinks

- Consensus is bullish (section 2), and the stock trades near the bottom of its 12-month multiple range.
- A Sell note of 14 September 2026 (target $470) argued that 2027 ships 2024-priced orders and put 2027 EBITDA at $7.42B against consensus near $9.45B. The stock closed at $957.27 on 11 September and $874.76 on 14 September (-8.6%). It has since recovered. Known only from press summaries.
- The HA unit roll in section 4 contradicts that premise for the largest turbines.
- A Jefferies note reported on 12 September 2026 says investors are fixed on "peak orders". (News.)

## 7. Dated tests

| Date | What to read | Supports the long | Warning |
|---|---|---|---|
| 28 Oct 2026, Q3 results | Gas GW sold | about 5 | 4.2 or less |
| same | HA units sold | 6 or more | 3 again |
| same | Power equipment revenue | Street is $2,394M | well below |
| Late Jan 2027 | 2027 outlook; castings for 2028 | reaffirmed | hedged |
| Spring 2027 | Investor day, 2030 outlook | at or above the Street | below |
| Late Jul 2027, Q2 results | H1 2027 Power equipment revenue | above Street $5,383M | below |

## 8. Risks

- Output misses the plan. In the reference model, 10% fewer GW cuts base EBITDA by about 3%, because equipment is the low-margin part of Power. The larger damage would be to the multiple.
- The multiple falls below 21.8x. The 2025 low was about 18-21x; the peer median is 16.0x.
- Wind keeps losing money: (657) in H1 2026 against a Street figure of +188 for FY2027.
- Reservations do not convert into orders.
- Costs or tariffs absorb the higher prices, so the Power margin does not reach 23%.
- The long is crowded: 32 of 41 analysts rate it a buy.
- Not counted as upside: about $7.2B of cash built by September 2027 (about $27 a share).

## 9. Questions a judge is likely to ask

1. Why 25x, when the peer median is 16x and Siemens Energy trades at 12.5x?
2. Last quarter was 3.3 GW. Why will it be 5?
3. Power equipment is a quarter of revenue. Why is the thesis about it?
4. If you agree with consensus earnings, what do you know that the market does not?
5. What makes you sell?

## 10. How these numbers were checked (2026-10-02)

Each number was checked three ways where three ways exist.

1. Against the primary source: the filing text in the corpus, or the Bloomberg workbook.
2. Against a second source: XBRL data for balance-sheet and revenue items, the raw Bloomberg screen exports for consensus, a second filing or table for unit counts.
3. By recalculation: every derived figure was recomputed from the typed inputs, and totals were cross-footed.

Results: 79 filing checks and 131 Bloomberg and calculation checks, all agreeing with this brief. The 12-month multiple range uses 53 weekly points to 2026-09-25, with no week at or below 26x. The 2025 low was 18.5x on 2025-04-04.

What has fewer than three sources:
- Unit and GW counts exist only in the filings' Power tables. They were checked in each filing and by arithmetic (for example, full year less nine months).
- Restricted cash is a rounded figure.
- The world capacity estimate of 67 to 102 GW rests on one post. The Sell note is known from press summaries (four agree on the $470 target, three on the $7.42B).
- The GW path for 2027 and 2029 is a reading, not a company number.

## 11. Sources

- 10-K FY2025, accession 0001996810-26-000015. 10-K FY2024, 0001996810-25-000011.
- 10-Q Q2 2026, 0001996810-26-000148. 10-Q Q1 2026, 0001996810-26-000064. 10-Q Q3 2025, 0001996810-25-000160.
- Q2 2026 earnings release, 0001996810-26-000147. Q4 2025 earnings release, 0001996810-26-000012.
- Q2 2026 earnings call transcript, gevernova.com, 22 July 2026.
- Morgan Stanley Laguna conference transcript, gevernova.com, 16 September 2026.
- Bloomberg, 2026-10-01: consensus, segment consensus, multiples, ratings, peers.
- Bloomberg, 2026-10-02: suppliers, customers, options, estimate detail (section 12). File: `data/bloomberg/GEV_bloomberg_pull_2_filled_2026-10-02.xlsx`.
- Trade press and third-party items are marked as such above. Check them before citing.

## 12. Added 2 October: second Bloomberg pull and the Electrification test

Result: no number against the Street. The call in section 1 does not change. These are extra facts.

### 12.1 Multiples against growth (Bloomberg, 2026-10-02)

EV / next-12-month EBITDA, and consensus EBITDA growth for each company's own next two fiscal years.

| Company | Multiple | Growth, next year | Year after | Price, 3 months |
|---|---|---|---|---|
| GE Vernova | 28.5x | +49.5% | +32.5% | about -13% |
| Howmet (blade supplier) | 25.7x | +18.2% | +14.9% | -14.2% |
| GE Aerospace | 25.0x | +13.1% | +11.1% | -17.9% |
| Doosan Enerbility | 28.2x | +28.0% | +22.1% | -6.4% |
| ATI | 20.6x | +17.8% | +12.8% | +2.4% |
| Woodward | 20.0x | +11.3% | +14.6% | -20.4% |
| Caterpillar | 19.3x | +18.5% | +16.1% | -12.2% |
| Carpenter Technology | 17.7x | +13.6% | +19.3% | -34.7% |
| Mitsubishi Heavy | 15.1x | +16.8% | +15.0% | +0.6% |
| Siemens Energy | 12.7x | +31.3% | +23.6% | -12.3% |
| Baker Hughes | 11.1x | +16.6% | +12.9% | +6.0% |

- Two related companies with slower growth trade near 25x: Howmet and GE Aerospace. The two direct rivals trade at 12.7x and 15.1x. Both facts belong in any answer to "why 25x".
- Median three-month price change of the 14 related stocks pulled: -11.0%. The recent fall is group-wide.
- Fiscal years differ: Siemens Energy and Woodward end in September, Mitsubishi Heavy in March, Carpenter in June.

### 12.2 What options prices imply (Bloomberg, 2026-10-02)

- Implied volatility: 50.9% (30 days), 48.2% (3 months), 49.3% (12 months). Realised: 43.9% (30 days), 54.8% (90 days).
- A 49.3% yearly figure means a one-standard-deviation range of about $603 to $1,616 in 12 months (price $987.62). The bear case ($855) is -0.29 standard deviations; the bull case ($1,341) is +0.62.
- Downside and upside options cost about the same: 3-month implied volatility is 48.5% at a strike 10% below the price and 47.9% at 10% above.
- Three-month implied volatility is at the 25th percentile of the last 52 weeks (range 46.4 to 63.5). Peak since listing: 73.8 on 2025-04-04.
- Rough reading for 28 October: an expected move of about 5% either way (calculated from the 30-day and 60-day figures; an estimate, not a quote). Past ten results days: average move 5.4%, median 2.9%, seven up. Largest: +14.6% (2025-07-23), +13.7% (2026-04-22), -8.7% (2026-07-22). Prices from the corpus.

### 12.3 Suppliers (Bloomberg, 2026-10-02)

- Howmet quarterly revenue, year on year: +6.5%, +9.2%, +13.8%, +14.6% (2025), then +19.1% and +24.1% (Q1 and Q2 2026). This is total revenue, mostly jet-engine parts. The gas turbine line needs the Company Specific screen.
- Analysts raised Howmet's 2027 revenue estimate from $10,512M (1 May) to $11,569M (2 October).
- Woodward +21.2%, GE Aerospace +21.1%, Siemens Energy +17.5%, Mitsubishi Heavy +15.5% in the June quarter.
- Bloomberg's supply-chain data lists Howmet and Woodward among GE Vernova's suppliers, and GE Vernova and Mitsubishi Heavy among Howmet's customers.
- Howmet's own Q2 2026 release (6 August 2026, primary): revenue from the gas turbines market grew 38% year on year; total revenue grew 24%. The chief executive: "Demand in the gas turbines market is extraordinary with customers already revisiting and adding to their demand outlooks." Link: https://www.howmet.com/press-release/2026-08-06/howmet-aerospace-reports-second-quarter-2026-results/
- For scale: GE Vernova's plan of 5 GW a quarter is 37% above the 14.6 GW of the last four quarters. Howmet's 38% is in dollars (price and volume) and covers all turbine makers, so the two are not the same measure.
- Howmet's Q2 2026 call (transcript on fool.com, secondary): a share "in excess of 50% globally for turbine blades" in gas turbines; a new plant in Japan, an expansion in Europe and more equipment in Virginia; more capacity "in '27, but with another major step into '28 and '29".
- Gas turbines were 13% of Howmet's Q2 2026 revenue, about $0.33B (Zacks, secondary).

### 12.4 Customers (Bloomberg, 2026-10-02)

- Capital spending consensus for 11 large US utilities (Duke, Southern, Entergy, NextEra, Dominion, AEP, Xcel, PPL, DTE, Ameren, CenterPoint): $140.6B (2026), $155.8B (2027, +10.9%), $160.9B (2028, +3.3%).
- Consensus 2028 capital spending for the five largest data-centre builders has been flat since early September ($1,203B in total).
- Reading: on today's estimates, customer spending growth slows in 2028. Utility plans are usually raised once a year, so these may be stale.

### 12.5 Estimate changes (Bloomberg, 2026-10-02)

| | 2026 | 2027 | 2028 | 2029 |
|---|---|---|---|---|
| Revenue, 3-month change | +1.7% | +2.2% | +3.0% | +5.8% |
| EBITDA, 3-month change | +2.5% | +2.0% | -1.3% | +6.2% |
| EBITDA spread (standard deviation / mean) | 4.4% | 9.7% | 17.8% | 8.2% |
| EBITDA median against mean | +0.8% | -1.1% | +2.5% | 0.0% |

- Using medians instead of means, forward EBITDA at the target date is $11,987M, the 25x price is $1,145 and the break-even multiple is 21.5x.
- Next quarter (Q3 2026): revenue $11,993M (28 analysts), EBITDA $1,672M (26 analysts; range $1,378M to $1,795M).

### 12.6 Electrification: how fast backlog becomes revenue (10-K, 10-Q, Bloomberg 2026-10-01)

Share of the segment's opening backlog recognised as revenue in the following four quarters. Prolec GE (bought 2 February 2026; revenue $485M in Q1 and $859M in Q2 2026) is removed from the last two rows.

| Backlog date | Backlog ($M) | Next four quarters' revenue ($M) | Share |
|---|---|---|---|
| 31 Dec 2023 | 16,342 | 7,550 | 46.2% |
| 30 Jun 2024 | 20,679 | 8,189 | 39.6% |
| 31 Dec 2024 | 23,453 | 9,642 | 41.1% |
| 31 Mar 2025 | 25,462 | 10,236 | 40.2% |
| 30 Jun 2025 | 27,530 | 10,813 | 39.3% |
| 30 Jun 2026, Street | 44,563 | 16,145 | 36.2% |

- The Street assumes the lowest share in the record. But its 2026 figure ($14,765M) equals the company's guide midpoint ($14.5B to $15.0B, including about $3.1B from Prolec).
- The company raised that guide by $0.5B in April and again in July. The Q3 guide is $3.8B to $4.0B; the Street has $3,881M.
- Most of the slowdown is a harder comparison: the second half of 2025 grew 35%, the first half 19%.
- If growth before Prolec holds at 25% instead of about 16%, revenue is about $1.0B higher and EBITDA $0.2B to $0.3B higher (2% to 3% of company EBITDA).
- Equipment backlog equals 4.1 years of equipment revenue (2.9 years at end-2023).
- From the Q2 2026 call: air-insulated switchgear is about $5B of backlog; about 9,000 units shipped in 2025, about 10,500 planned for 2026; data-centre orders above $5B in the first half of 2026.

### 12.8 Why 12 months: every holding period from 3 to 12 months (Bloomberg consensus, 2026-10-01)

Method. Forward EBITDA at each date is the analysts' calendar-year figures weighted by months (2026: 6,334; 2027: 9,471; 2028: 12,553). Enterprise value today is $257,241M and today's multiple on this basis is 29.6x. The break-even multiple is the one at which the price is unchanged. The base path lets the multiple slide in a straight line from 29.6x to 25x at month 12.

| Months | Ends | Forward EBITDA vs today | Break-even multiple | Room for the multiple to fall | Base-path price | Past windows where the multiple fell by more |
|---|---|---|---|---|---|---|
| 3 | 1 Jan 2027 | +9.0% | 27.2x | 8.3% | $1,033 (+4.6%) | 26% |
| 4 | 1 Feb 2027 | +12.0% | 26.4x | 10.7% | $1,046 (+6.0%) | 19% |
| 5 | 1 Mar 2027 | +14.9% | 25.8x | 13.0% | $1,059 (+7.2%) | 13% |
| 6 | 1 Apr 2027 | +17.9% | 25.1x | 15.2% | $1,071 (+8.4%) | 6% |
| 7 | 1 May 2027 | +20.9% | 24.5x | 17.3% | $1,082 (+9.5%) | 1% |
| 8 | 1 Jun 2027 | +23.8% | 23.9x | 19.2% | $1,092 (+10.6%) | 0% |
| 9 | 1 Jul 2027 | +26.8% | 23.4x | 21.1% | $1,102 (+11.6%) | 0% |
| 10 | 1 Aug 2027 | +29.7% | 22.8x | 22.9% | $1,111 (+12.5%) | 0% |
| 11 | 1 Sep 2027 | +32.7% | 22.3x | 24.6% | $1,119 (+13.3%) | 0% |
| 12 | 1 Oct 2027 | +35.6% | 21.8x | 26.3% | $1,126 (+14.0%) | 0% |

- The last column uses Bloomberg's weekly forward multiple from April 2024 to September 2026 (77 to 117 overlapping windows per row). The history is short and the multiple rose from 12x to 28x in it, so it flatters the long.
- The return builds evenly, at a little over 1% a month. No single month stands out. What grows with time is the room for the multiple to fall: about 2.3 points a month.
- Bear path by horizon (bear EBITDA, multiple sliding to 21x): -8.0% at 3 months, -8.8% at 6, -10.6% at 9, -13.4% at 12. Weighted return: +3.5%, +7.2%, +10.2%, +12.6%.
- A short is the mirror image. Its best window is the shortest one, and on this history it would have lost in about three windows out of four.

Dated events inside the windows (web, 2026-10-02; check each before citing):

- 28 October 2026: Q3 results (company; Bloomberg).
- 11 November 2026: Siemens Energy full-year results and next-year outlook (Siemens Energy investor relations).
- 9 December 2026: next PJM capacity auction, for 2029/30. The July 2026 auction cleared at the price cap for the third time in a row (PJM; NRG market update).
- No GE Vernova investor update is listed for December 2026. The 2027 outlook comes with results in late January 2027, and a capital markets day on 2030 is planned for spring 2027 (company statements reported by TheStreet, September 2026).
- 29 September 2026: US regulators issued the first construction permit for the company's small nuclear reactor design, at the Clinch River site in Tennessee (news).

### 12.9 Second-opinion check (an independent AI read the corpus, evening of 2 October)

Result: no number against the call. Direction, target and odds unchanged. Two claims were worded too strongly and are now fixed in the thesis file. Figures below were re-checked against the filings in the corpus.

- **Backlog price has risen four quarters running:** Power equipment backlog divided by firm gas GW = $556 (Jun 2025), $575 (Sep 2025), $618 (Dec 2025), $648 (Mar 2026), $741 (Jun 2026). Backlog from the 10-Qs and 10-K; GW from the releases.
- **Realised price lags the backlog average.** Revenue per kW shipped was 94% of the opening backlog price in H2 2025 and 83% in H1 2026. On $741 that gives $615 to $697. Analysts need $579 in 2027 (covered) and $662 in 2028 (covered only if backlog prices keep rising). Say "2027 is covered", not "price is settled".
- **"116 GW under contract" needs the split:** 53 GW of firm orders plus 63 GW of paid reservations, of which 7, 8, 6 and 10 GW converted in the last four quarters. Q2 2026 brought about 2 GW of new firm orders directly; the rest of the firm growth came from converted reservations.
- **Tariffs:** the 2026 cost estimate fell from $250M to $350M (10-Q April 2026) to $100M to $200M (10-Q July 2026). Small help; consensus already dates from after the cut.
- **Customer deposits:** $17.7B (Dec 2024), $26.0B (Dec 2025), $31.9B (Mar 2026), $40.0B (Jun 2026); $7.5B of the opening balance became revenue in H1 2026. Analysts have free cash flow falling from $12,196M to $7,654M in 2027. If orders peak, the fall could be larger: a risk to the multiple.
- **NRG** (customer filings): paid reservations with GE Vernova rose from 1.2 GW (Feb 2025) to 3.6 GW (Feb 2026), beside a development agreement for up to 5.4 GW.
- **US plant register:** planned US gas capacity grew from 21.7 to 65.3 GW between the January 2025 and July 2026 editions; 55% of it has no regulatory filing yet and one 8.8 GW project is almost half of the 2030 total. Fits demand; cannot test the 20 GW plan (no turbine-maker field).
- **Offshore Wind:** the Q2 2026 10-Q mentions claims and counterclaims on Vineyard Wind, no amount given. Name it as a risk.
- Not used: an inferred $898 per kW on new H1 2026 orders (inference only, band about 25%).

Deep pass (same check, later that evening; figures re-verified where the corpus allows):

- **Price lag, five yearly windows:** realised price was 78% to 94% of the opening backlog price (average 87%). On $741: $578 to $697. 2027 ($579) covered at the average; 2028 ($662) needs the backlog price near $760 per kW by December 2027. A 2028 shortfall of 7 to 11% would cost 2 to 14% of 2028 EBITDA depending on mix or price.
- **Howmet's gas turbine revenue, from its own filings:** $321M in Q2 2026 vs $233M (+38%); $605M in H1 2026 vs $437M (+38%); $944M in FY2025. Use these, not the $341M from a transcript site.
- **Supplier timing (filings):** Howmet's main capacity step is 2028 to 2029 with a 24-month lead; Carpenter's new melt capacity is commissioned about mid-2027; ATI prioritises aerospace; Woodward sold its heavy-duty combustion parts line. Nothing contradicts the 2027 plan; the 2028 step to 24 GW carries timing risk.
- **Deposits and the January 2027 cash guide:** deposits by segment at June 2026: Power $27,685M, Electrification $9,124M, Wind $3,227M; Power is about four fifths of the rise. Analysts' FY2027 free cash flow of $7,654M needs deposits to grow about $5.5B in 2027 after $15.7B in 2026 (inference from the cash bridge, band about $1.8B). Flat deposits would give about $2.1B. The company's floor, "cumulative free cash flow of at least $24 billion" for 2025 to 2028 (Q4 2025 release), leaves $7.8B to $8.8B for 2027 and 2028 together against analysts' $17.2B; the floor predates the FY2026 guide rising to $11.5B to $12.5B and will probably be raised. No effect on EBITDA or the target; a risk to the multiple on the day of the outlook.
- **Corrections to the first pass:** the 8.8 GW Texas project (Fermi) uses Siemens turbines, so the US pipeline risk is smaller for GE Vernova; Vineyard Wind was settled in September 2026 on undisclosed terms.

### 12.7 Report dates around 28 October (Bloomberg, 2026-10-02)

GE Aerospace 20 October, Carpenter 22 October, Baker Hughes 27 October, GE Vernova, ATI, NextEra and Bloom Energy 28 October, Howmet and Caterpillar 29 October, Mitsubishi Heavy 5 November, Siemens Energy 11 November.
