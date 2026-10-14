"""Sections 7 to 11 of the thesis file. Same block format as content_a."""

S = []

S.append(("7. What the market thinks", [
    ("note", "**Consensus** is the average of the forecasts that brokers send to Bloomberg. For 2027 EBITDA there are 36 of them. We call them \"analysts\" in this file."),
    ("md", "This section sets out what analysts forecast, what the share price already assumes, and how the market has behaved. All figures come from the two Bloomberg pulls unless marked."),
    ("wide", """
| Analysts' consensus, $M | FY2026 | FY2027 | FY2028 | FY2029 |
|---|---|---|---|---|
| Revenue | 46,240 | 53,029 | 60,985 | 70,851 |
| Adjusted EBITDA, mean | 6,334 | 9,471 | 12,553 | 16,496 |
| Adjusted EBITDA, median | 6,384 | 9,364 | 12,862 | 16,504 |
| Adjusted EBITDA, high / low | 6,823 / 5,112 | 11,029 / 6,612 | 17,141 / 4,786 | 19,385 / 14,183 |
| Number of estimates | 35 | 36 | 33 | 21 |
| EBITDA margin | 13.7% | 17.9% | 20.6% | 23.3% |
| EBITDA growth | +98% | +50% | +33% | +31% |
| Free cash flow | 12,196 | 7,654 | 9,527 | 9,702 |
| Power equipment revenue | 9,342 | 12,151 | 15,888 | 19,256 |
| Power services revenue | 14,259 | 15,675 | 17,665 | 19,711 |
| Power EBITDA | 4,418 | 5,906 | 7,810 | 9,983 |
| Electrification revenue | 14,766 | 17,704 | 21,270 | 24,959 |
| Electrification EBITDA | 2,724 | 3,774 | 4,972 | 6,130 |
| Wind EBITDA | (449) | 188 | 373 | 598 |
| Corporate and other | (490) | (455) | (473) | (478) |

Source: Bloomberg, 2026-10-01 [R12]. FY2026 segment figures are H1 2026 actual plus H2 2026 consensus. Segment lines come from fewer brokers than the totals and do not add up exactly.
"""),
    ("note", "**What is priced in.** Profit doubling in 2026 and rising by half again in 2027, at a multiple near the bottom of its 12-month range. The market already believes the growth. It is paying less for it than it did in April."),
    ("chart", "mult", "GE Vernova forward EV/EBITDA, weekly, April 2024 to September 2026", "Bloomberg weekly history [R12]. Dashed lines are on the model's basis, which reads about one turn higher than Bloomberg's (29.6x against 28.5x today)"),
    ("md", """
- **The multiple.** 28.5x as Bloomberg quotes it. Twelve-month range 27.3x to 42.4x, median 32.5x. No week at or below 26x in the last 53. The 2025 low was 18.5x on 4 April 2025. [R12]
- **The past year.** The price rose 63% ($606 to $988) while the multiple fell from 32.5x to 28.5x. Forward profit rose 85%. [R12]
- **The last three months.** The price fell 13%. Analysts' 2027 profit rose 2%. The multiple fell 19%. The 14 related stocks pulled on 2 October fell a median 11%, so the fall is group-wide. [R12] [R13]
- **What moves the price.** Across the 20 months with full data (February 2025 to September 2026), the monthly return moved with the change in the multiple (correlation 0.95), not with changes in analysts' 2027 profit (0.25) or with how far the average target sat above the price (0.02). [R12] [R14]
- **Analysts.** 32 buy, 7 hold, 2 sell. Average target $1,225, 24% above the price. Short interest 3.3% of the float. [R12]
- **Analysts have been too low.** Since listing, their average target sat about 7% above the price, while the stock returned 26%, 59% and 90% on average over the next 3, 6 and 9 months. [R12] [R14]
- **Estimate changes in three months.** Revenue +1.7%, +2.2%, +3.0%, +5.8% for 2026 to 2029. EBITDA +2.5%, +2.0%, -1.3%, +6.2%. No fresh wave of upgrades. [R13]
"""),
    ("chart", "price", "GE Vernova share price since listing ($)", "Daily closes [R14]; Bloomberg close for 1 October 2026 [R12]. First close $131.25 on 27 March 2024; highest close $1,174.86 on 30 June 2026"),
    ("note", "**The Sell note.** One research firm said on 14 September that the shares are worth $470. The shares fell 8.6% that day and have since recovered. Section 5 shows why its main premise does not fit the filings."),
    ("md", """
- **The Sell note.** GLJ Research began coverage on 14 September 2026 with a Sell rating and a $470 target. Its argument: turbines delivered in 2027 were ordered in 2024 at old prices. It puts 2027 EBITDA at $7.42B. The stock closed at $957.27 on 11 September and $874.76 on 14 September. Known from press summaries only. [R22]
- **Peak orders.** Wood Mackenzie expects orders to peak in 2026. A Jefferies note of 12 September said investors were too fixed on that and were overlooking services. Evercore ISI kept its Outperform rating and $1,350 target in early October. News reports. [R16] [R23] [R35]
- **Options.** Implied volatility is 50.9% for 30 days, 48.2% for 3 months and 49.3% for 12 months. That means a one-standard-deviation range of about $603 to $1,616 in a year. Options that protect against a fall cost about the same as options that gain from a rise. For the results day of 28 October they imply a move of about 5%; the average of the last ten results days is 5.4%. [R13] [R14]
"""),
]))

S.append(("8. Valuation", [
    ("note", "**How a target price is built.** Take the profit expected for the 12 months after the target date. Multiply it by the multiple. Add the cash the company holds beyond what it owes. Divide by the number of shares."),
    ("md", """
### Inputs

| Input | Value | Source |
|---|---|---|
| Share price | $987.45 | Bloomberg, close of 1 October 2026 [R12] |
| Shares, basic | 266.334M | 10-Q Q2 2026, cover [R3] |
| Dilutive shares | 3M | 10-Q Q2 2026, Note 18 [R3] |
| Diluted shares | 269.334M | sum |
| Cash, including restricted | 13,120 | 10-Q Q2 2026, cash flow statement [R3] |
| Less restricted cash | (400) | 10-Q Q2 2026, liquidity section. Rounded: the filing says "$0.4 billion" [R3] |
| Less total borrowings | (2,849) | 10-Q Q2 2026, borrowings note [R3] |
| Less noncontrolling interests | (1,158) | 10-Q Q2 2026, balance sheet [R3] |
| Net cash | 8,713 | sum |
| Analysts' EBITDA, 2026 / 2027 / 2028 | 6,334 / 9,471 / 12,553 | Bloomberg, 2026-10-01 [R12] |
| Company plan path, 2026 / 2027 / 2028 | 5,980 / 8,590 / 11,200 | Guide midpoint 46,000 x 13%; framework 56,000 x 20%; 2027 halfway [R6] [R7] |

### The base case, line by line

| Step | Arithmetic | Result |
|---|---|---|
| Forward EBITDA at 30 September 2027 | 25% of 9,471 + 75% of 12,553 | 11,782.5 |
| Enterprise value | 25 x 11,782.5 | 294,562.5 |
| Equity value | 294,562.5 + 8,713 | 303,275.5 |
| Price | 303,275.5 / 269.334 | $1,126.02 |
| Return | 1,126.02 / 987.45 - 1 | +14.0% |
| Enterprise value today | 987.45 x 269.334 - 8,713 | 257,240.9 |
| Forward EBITDA today | 25% of 6,334 + 75% of 9,471 | 8,686.75 |
| Multiple today, same basis | 257,240.9 / 8,686.75 | 29.6x |
| Break-even multiple | 257,240.9 / 11,782.5 | 21.8x |
"""),
    ("note", "**Why 25% and 75%.** The target date is 30 September 2027. The 12 months after it cover the last quarter of 2027 and the first three quarters of 2028. So the forward profit is one quarter of the 2027 figure plus three quarters of the 2028 figure."),
    ("md", """
### The three cases

| Case | FY2027 EBITDA | FY2028 EBITDA | Forward EBITDA | Multiple | Price | Return |
|---|---|---|---|---|---|---|
| Bear: the company's own plan | 8,590 | 11,200 | 10,548 | 21x | $855 | -13.4% |
| Base: analysts' consensus | 9,471 | 12,553 | 11,783 | 25x | $1,126 | +14.0% |
| Bull: base plus 5% | 9,945 | 13,181 | 12,372 | 28.5x | $1,341 | +35.9% |

Weighted 25 / 50 / 25: $1,112 (+12.6%).

### Price at each multiple

| Multiple | Bear EBITDA 10,548 | Base EBITDA 11,783 | Bull EBITDA 12,372 |
|---|---|---|---|
| 18.5x | $757 (-23.4%) | $842 (-14.8%) | $882 (-10.7%) |
| 21x | $855 (-13.4%) | $951 (-3.7%) | $997 (+1.0%) |
| 23x | $933 (-5.5%) | $1,039 (+5.2%) | $1,089 (+10.3%) |
| 25x | $1,011 (+2.4%) | $1,126 (+14.0%) | $1,181 (+19.6%) |
| 27x | $1,090 (+10.4%) | $1,214 (+22.9%) | $1,273 (+28.9%) |
| 28.5x | $1,148 (+16.3%) | $1,279 (+29.5%) | $1,341 (+35.9%) |
"""),
    ("note", "**The split.** Holding today's 29.6x would give $1,328, which is +34.5% from profit growth alone. The fall to 25x takes away 20.4%. Net +14.0%. If you start from Bloomberg's quoted 28.5x instead, the split reads +29.7% and -15.7%. Use one basis and say which. The target does not change."),
    ("md", """
### Why 25x: the reference points

| Reference | Multiple | Comment |
|---|---|---|
| Today, model basis | 29.6x | |
| Today, as Bloomberg quotes it | 28.5x | Rests on Bloomberg's own forward EBITDA, about 8,923 |
| Last 12 months | 27.3x to 42.4x | Median 32.5x |
| 2025 low | 18.5x | 4 April 2025 |
| Howmet, GE Aerospace | 25.7x, 25.0x | Related businesses; profit growth of 18% and 13% next year |
| Siemens Energy, Mitsubishi Heavy | 12.7x, 15.1x | The two direct rivals; growth of 31% and 17% |
| Median of ten electrical peers | 16.0x | First pull [R12] |
| **Base assumption** | **25x** | Below every week of the last 12 months |
| Break-even | 21.8x | |

25x is an assumption. It is the weakest point of the case and the one a judge will press. [R12] [R13]
"""),
    ("chart", "peers", "EV / next-12-month EBITDA, with profit growth expected next year", "Bloomberg, 2026-10-02 [R13]; GE Vernova from 2026-10-01 [R12]"),
    ("note", "**Why 12 months.** Each month you hold, the profit being valued grows about 3%. So the multiple you need to break even drops by about half a turn a month. Twelve months is the longest the rules allow, so it has the lowest hurdle."),
    ("md", "The rules allow a holding period of 3 to 12 months. The table below works out every one of them on the same figures, so the choice of 12 can be defended."),
    ("wide", """
### Every holding period from 3 to 12 months

| Months | Ends | Forward EBITDA vs today | Break-even multiple | Room for the multiple to fall | Base-path price | Bear-path return | Past windows where the multiple fell by more |
|---|---|---|---|---|---|---|---|
| 3 | 1 Jan 2027 | +9.0% | 27.2x | 8.3% | $1,033 (+4.6%) | -8.0% | 26% |
| 4 | 1 Feb 2027 | +12.0% | 26.4x | 10.7% | $1,046 (+6.0%) | -8.2% | 19% |
| 5 | 1 Mar 2027 | +14.9% | 25.8x | 13.0% | $1,059 (+7.2%) | -8.4% | 13% |
| 6 | 1 Apr 2027 | +17.9% | 25.1x | 15.2% | $1,071 (+8.4%) | -8.8% | 6% |
| 7 | 1 May 2027 | +20.9% | 24.5x | 17.3% | $1,082 (+9.5%) | -9.3% | 1% |
| 8 | 1 Jun 2027 | +23.8% | 23.9x | 19.2% | $1,092 (+10.6%) | -9.9% | 0% |
| 9 | 1 Jul 2027 | +26.8% | 23.4x | 21.1% | $1,102 (+11.6%) | -10.6% | 0% |
| 10 | 1 Aug 2027 | +29.7% | 22.8x | 22.9% | $1,111 (+12.5%) | -11.4% | 0% |
| 11 | 1 Sep 2027 | +32.7% | 22.3x | 24.6% | $1,119 (+13.3%) | -12.4% | 0% |
| 12 | 1 Oct 2027 | +35.6% | 21.8x | 26.3% | $1,126 (+14.0%) | -13.4% | 0% |

The base path lets the multiple slide in a straight line from 29.6x to 25x at month 12. The last column uses Bloomberg's weekly multiple from April 2024 to September 2026 (77 to 117 overlapping windows per row). That history is short and the multiple rose from 12x to 28x in it, so it flatters the long. [R12]
"""),
    ("chart", "horizon", "The hurdle falls every month: break-even multiple against the base-path multiple", "Arithmetic on Bloomberg consensus, 2026-10-01 [R12]"),
    ("md", """
### Other checks on the target

- **Medians instead of means:** forward EBITDA 11,987, price at 25x $1,145, break-even 21.5x. [R13]
- **A harder downside:** the 2025 low of 18.5x on bear EBITDA gives $757 (-23%). The bear case is not the worst case.
- **Not counted as upside:** about $7.2B of cash built by September 2027, about $27 a share.
- **A second build:** the reference model made during research rebuilds the forecast by segment and gives $1,134 for the base. The memo must quote the team's own model.
"""),
]))

S.append(("9. Every stress test, and what happened", [
    ("note", "**How to read this table.** Each row is one attempt to find a number where analysts are wrong, or a reason the call fails. \"Error band\" is how wrong our own estimate could be. A gap smaller than its error band proves nothing."),
    ("md", "Each row below is one test. Rows 1 to 13 looked for a number where analysts are wrong. Rows 14 to 18 tested the bear side and the short. Rows 19 to 22 were run on 2 October, after the second Bloomberg pull. Rows 23 to 25 come from an independent second AI that read the corpus and the suppliers' filings on the evening of 2 October."),
    ("wide", """
| # | Test | What was compared | Result | Check | Verdict |
|---|---|---|---|---|---|
| 1 | 2027 EBITDA built from segments | Research $8.6B to $8.9B against analysts' $9,471M | 7 to 11% below | Inside analysts' own range (0.6 to 1.0 standard deviations) | No edge. Three small segment differences |
| 2 | 2028: analysts against the company's framework | $12,553M against $11,200M | Analysts 12% above | Guidance raised or held at every report | Not a short signal. Used as the bear case |
| 3 | 2029 EBITDA | Research $15.4B against analysts' $16,496M | Analysts 7% above | Build rests on assumptions | No long gap |
| 4 | Equipment revenue, next four quarters | Backlog schedule $31,616M against analysts' $30,245M | +4.5% | Beat in 6 of 7 past windows | Real but small, about $0.2B of EBITDA. Supports the long |
| 5 | Power equipment revenue, H1 2027 | Unit-by-unit build against analysts' $5,383M | +14 to +17% | Error band about 22% | The sign holds in every variant, the size does not. Not usable as a number |
| 6 | Power equipment revenue, 2028 | 24 GW x $735 per kW x 0.90 = $15,876M against analysts' $15,888M | No gap | | Analysts are on the company's plan |
| 7 | Contracted order book to 2030 | Cumulative revenue against analysts | +1 to +3.8% | Error band 10 to 12% | No |
| 8 | The 2030 outlook due in spring 2027 | Predicted outlook against analysts | +1 to +2% | Error band 12 to 15% | No |
| 9 | Free cash flow, FY2026 | Research build against analysts | No gap survived | Three checkers | Rejected 3 to 0 |
| 10 | Electrification orders, Q3 2026 | Research build against analysts | No gap survived | Three checkers | Rejected 3 to 0 |
| 11 | Wind EBITDA, FY2027 | Analysts' +$188M against a loss of $657M in H1 2026 | No tradable gap | Three checkers | Rejected 3 to 0. Kept as a risk |
| 12 | Wind equipment, H1 2027 | Research build against analysts | No gap survived | Three checkers | Rejected 3 to 0 |
| 13 | Power services, FY2028 | Research build against analysts | No gap survived | Three checkers | Rejected 3 to 0 |
| 14 | The Sell note's premise | "2027 ships 2024 orders" against the unit roll | 62 to 70 of 70 HA units are 2025 or later | Counted from filings | Premise contradicted. The price has already recovered, so this removes a risk and adds no upside |
| 15 | The January 2027 outlook | First guide against analysts' 17.9% margin | Judgement: 65 to 70% that the midpoint is 17.5% or lower | Only two earlier first guides | A risk to name, not a trade |
| 16 | A short into January | A three to four month short | Chance of profit about 56%; expected gain near zero once the monthly rise in forward profit is counted | A stop-loss would be hit by noise in 62 to 70% of paths | No |
| 17 | Nine bear arguments | Each checked against filings | All nine failed | Run of 23 September | No short case on a number |
| 18 | Reservations fail to convert | The first short idea | 7, 8, 6 and 10 GW converted in the last four quarters | Earnings releases | Rejected |
| 19 | Electrification backlog conversion | Analysts' next four quarters as a share of backlog | 36.2% against 39 to 46% before | Analysts equal the guide midpoint; harder comparison | Small plus: 2 to 3% of EBITDA |
| 20 | Options and the results day | Implied move against history | About 5% against 5.4% | Ten results days | Fairly priced |
| 21 | Suppliers and customers | Howmet; 11 utilities; 5 data-centre builders | Blade sales +38%; utility spending +10.9% then +3.3% | Second Bloomberg pull | Fits the plan. Spending growth slows in 2028 |
| 22 | Every holding period, 3 to 12 months | Break-even multiple by month | No month stands out | Bloomberg weekly history | 12 months kept: lowest hurdle |
| 23 | Realised price against the backlog price | Revenue per kW shipped against the backlog average at the start of the window, five yearly windows | 78% to 94%, average 87%: $578 to $697 on today's $741 | 2028 lands at -2% against analysts, band -17% to +12% | Inside its band. 2027 covered; 2028 needs the backlog price near $760 by December 2027. Wording of the price claim changed |
| 24 | The US plant register | Planned US gas plants by year against the output plan | Planned US gas capacity for 2026 to 2031 grew from 21.7 to 65.3 GW in 18 months; 55% has no regulatory filing yet; the largest project (8.8 GW) uses Siemens turbines | Register has no turbine-maker field | Fits demand; cannot test the 20 GW plan. No number against the call |
| 25 | Customer deposits and the 2027 cash guide | Analysts' FY2027 free cash flow of $7,654M rebuilt as a cash bridge | Analysts need deposits to grow about $5.5B in 2027, after $15.7B in 2026; with flat deposits FY2027 free cash flow would be about $2.1B | Inference; the company does not split deposits between orders and reservations; band about $1.8B | No change to EBITDA or the target. A dated risk to the multiple at the January 2027 outlook (section 11) |
"""),
    ("chart", "elec", "Electrification: share of opening backlog recognised as revenue in the next four quarters (%)", "10-K and 10-Q segment tables [R1] [R2] [R3] [R4] [R5] [R11]; last bar is analysts' figure, Bloomberg 2026-10-01 [R12]. Prolec removed from the two 2025 windows"),
    ("note", "**Three ways to check a number.** First, against the filing or Bloomberg file it came from. Second, against a second source, such as the machine-readable data the company files. Third, by recalculating it from the typed inputs."),
    ("md", """
### How the numbers were checked

- 79 checks against filing text and filed data, and 131 checks against the Bloomberg files and by recalculation. All agreed with the figures in sections 1 to 8.
- The sections added on 2 October (second pull, Electrification, holding periods) were recalculated by script from the workbook and the filings.
- A four-checker review of the reference model produced 50 corrections. All are applied. The largest: diluted shares, not basic; restricted cash taken out of net cash.
- What has fewer than three sources: gigawatt and unit counts (filings only); restricted cash (a rounded figure); the 67 to 102 GW capacity estimate (one post); the Sell note (press summaries); the 21 GW and 26 GW path for 2027 and 2029 (a reading of the plan); Howmet's call remarks (a transcript site).
"""),
]))

S.append(("10. Dated tests", [
    ("note", "**Why dated tests.** The rules ask for evidence with a predictive part. Each row is something that will be published on a known date and can prove the view right or wrong."),
    ("md", "Each row is a figure that will be published on a known date. The last two columns say what would support the long and what would warn against it."),
    ("wide", """
| Date | What to read | Supports the long | Warning |
|---|---|---|---|
| 28 Oct 2026, Q3 results | Gas gigawatts sold | About 5 | 4.2 or less |
| same | HA units sold | 6 or more | 3 again |
| same | Power equipment revenue | Analysts have $2,394M (range $2,063M to $2,591M) | Well below |
| same | Electrification revenue | $3.9B or more (guide $3.8B to $4.0B; analysts $3,881M) | Below $3.8B |
| same | Company EBITDA | Analysts have $1,672M (26 brokers; range $1,378M to $1,795M) | Below the range |
| 11 Nov 2026 | Siemens Energy full-year results and outlook | Gas margin and order outlook raised | Order outlook cut |
| 9 Dec 2026 | PJM capacity auction for 2029/30 | Clears at or near the cap again | Clears well below |
| Late Jan 2027 | 2027 outlook; castings for 2028 | Midpoint near $9.0B of EBITDA or better; 2028 step reaffirmed | Midpoint at or below about $7.7B |
| Spring 2027 | Investor day: the 2030 outlook | At or above analysts | Below analysts |
| Late Jul 2027, Q2 results | Power equipment revenue, H1 2027 | Above analysts' $5,383M | Below |

Sources: analysts' figures from Bloomberg [R12] [R13]; guides from the Q2 2026 release and call [R6] [R9]; dates from Bloomberg, Siemens Energy and PJM [R13] [R33] [R34]; the January thresholds from the research files [R39].
"""),
]))

S.append(("11. Risks, and what would make us sell", [
    ("note", "**The main risk in plain words.** The company can do everything right and the shares can still fall, if investors decide to pay less for each dollar of profit. That happened in the last three months."),
    ("md", """
- **The multiple falls below 21.8x.** The 2025 low was 18.5x. Direct rivals trade at 12.7x and 15.1x. Customer spending growth slows in 2028 on today's forecasts.
- **Output misses the plan.** In the reference model, 10% fewer gigawatts cuts base EBITDA by about 3%, because equipment is the low-margin part of Power. The larger damage would be to the multiple.
- **The January outlook lands below analysts.** Judged 65 to 70% likely. Past first guides were cautious and were later raised.
- **Wind keeps losing money:** a loss of $657M in H1 2026 against analysts' +$188M for FY2027.
- **Reservations do not convert into orders.** So far they have: 7, 8, 6 and 10 GW in the last four quarters.
- **Costs or tariffs absorb the higher prices,** so the Power margin does not reach 23%.
- **The long is crowded:** 32 of 41 analysts rate it a buy.
- **The January 2027 cash guide.** Customer deposits rose from $17.7B (December 2024) to $40.0B (June 2026), four fifths of the rise at Power. Analysts' 2027 free cash flow of $7,654M needs deposits to grow about $5.5B more in 2027, after $15.7B in 2026; if deposits only hold flat, 2027 free cash flow would be about $2.1B (second-opinion inference, band about $1.8B). The company's own floor, cumulative free cash flow of at least $24B for 2025 to 2028, leaves $7.8B to $8.8B for 2027 and 2028 together against analysts' $17.2B; that floor was set before the 2026 guide nearly doubled, so expect it to be raised. None of this touches EBITDA. It is a risk to the multiple on the day of the outlook. [R3] [R7] [R12]
- **The US pipeline is early-stage.** In the US plant register, 55% of the 67 GW of planned gas capacity has no regulatory filing yet. The largest project (8.8 GW, Texas) uses Siemens turbines, so it is not GE Vernova demand. Reservations could convert more slowly in 2027 and 2028. From the second-opinion check of the register; the company does not disclose its customer mix.
- **Supplier timing for 2028.** Howmet's main capacity step lands in 2028 and 2029 with a 24-month lead on new commitments; Carpenter's new capacity arrives mid-2027. If 2028 output is 21 to 22 GW instead of 24, Power equipment revenue is 8% to 13% lower, about 1% to 3% of 2028 EBITDA. [R41]
- **Offshore Wind.** The Vineyard Wind dispute was settled in September 2026 on undisclosed terms; any cash effect would show in the second-half 2026 results. [R3] [R42]

### Sell rules that came out of the research

| Rule | Trigger |
|---|---|
| Output | Gas gigawatts sold stay at 4.2 or less for two quarters after the plan date |
| January outlook | Midpoint implies 2027 EBITDA at or below about $7.7B |
| 2028 framework | The 20% margin target is cut |
| Price | The team should set its own stop. A price stop alone fits badly: the stock moves about 3% on an ordinary day |

These are research inputs. The team chooses its own rules.
"""),
]))
