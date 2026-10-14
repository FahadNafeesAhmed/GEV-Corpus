# GE Vernova (GEV): the thesis file for the team

_AI-assisted research notes, to be disclosed under rule 10. Not submission text. Bloomberg figures are licensed for academic use._

## 1. The thesis on one page

> Side note. **In plain words.** We expect the share price to be about 14% higher in a year. The reason is not that the company will beat forecasts. It is that a year from now investors will be valuing a much larger profit, and we assume they pay a lower price for each dollar of it.

| Item | Value | Source |
|---|---|---|
| Position | Long GE Vernova (GEV), 12 months, to 30 September 2027 | |
| Price | $987.45, close of 1 October 2026 | [R12] |
| Base case | $1,126 (+14.0%): analysts' EBITDA, valued at 25x | section 8 |
| Bear case | $855 (-13.4%): the company's own plan path, 21x | section 8 |
| Bull case | $1,341 (+35.9%): analysts' EBITDA plus 5%, 28.5x | section 8 |
| Weighted 25 / 50 / 25 | $1,112 (+12.6%) | section 8 |
| Break-even multiple | 21.8x (the price ends flat) | section 8 |

> Side note. **Two terms.** *EBITDA* is profit before interest, tax, depreciation and amortisation. The *multiple* is the value of the whole company divided by the EBITDA expected over the next 12 months. A multiple of 25x means investors pay $25 for each $1 of yearly profit.

### The argument in three steps

1. **The profit the market prices will be about 36% larger in a year.** Next-12-month EBITDA is $8,687M today. At the target date it is $11,783M, on analysts' own figures. [R12]
2. **Those figures need nothing new to happen.** Seen in gigawatts: the price is already signed ($741 per kW in the backlog against the $579 to $662 analysts need), the demand is already signed or reserved (53 GW of firm orders plus 63 GW of paid factory reservations, against 111 GW of planned output to 2030), and the one open item is factory output (14.6 GW in the last four quarters against a plan of 20 a year). [R3] [R6] [R9]
3. **We assume the multiple falls, and the position still pays.** Today the multiple is 29.6x. The base case uses 25x. The position loses money only if the multiple ends below 21.8x.

### What this file does not claim

It does not claim that analysts are wrong on any number. Twenty-five attempts to find such a number either failed their checks or were too small to matter (section 9). An independent second AI repeated the search on the evening of 2 October and reached the same result.

_Figure: Share price in the three cases against today._ Source: Team reference arithmetic on Bloomberg consensus, 2026-10-01 [R12]; filings for share count and net cash [R3].

> Side note. **Reading the bridge.** If investors kept paying today's multiple, profit growth alone would lift the price by about $340. We assume they pay less, which takes back about $202. What is left is a gain of about $139.

_Figure: From today's price to the base target._ Source: Same arithmetic. Today's multiple of 29.6x is measured the same way as the target multiple.

## 2. How we got here: the process

> Side note. **Why this section matters.** A judge will ask what you tested and how you know. This is the answer. Six stages, each feeding the next.

The work ran from 19 September to 2 October 2026, in six stages. Each stage produced facts or tests that the next one used. The table lists what was built, why, and what came out.

_Figure: The six stages of the work._ 

| Stage | What was built or pulled | What it was for | What came out |
|---|---|---|---|
| 1. Information corpus (from 19 September) | One searchable database: 208 GE Vernova filings and the filings of 33 other companies; 339,610 reported financial data points; 3,915 outside sources (1,789 research papers, 840 web pages, 777 news articles, 254 competitor documents, call transcripts, grid-operator reports); the US government register of power plants. 469,353 text passages in all. | Trace every company fact to a filing. Search for patterns nobody models. | The backlog schedule, the roll of HA turbines in backlog, the gigawatt and price-per-kW series. |
| 2. Science and factory angle | Turbine physics and manufacturing: blades, foundries, casting capacity, lead times. | Ask whether the limit is demand, price or the factory. | The factory is the limit. That protects price and caps volume. |
| 3. Past winners | 20 winning pitches from leading student competitions, read in full. | Learn what a winning pitch contains. | A clear claim, dated tests and a sell rule. A long on consensus numbers is a call on the multiple; two past winners lost money that way. |
| 4. Bloomberg (1 and 2 October) | Consensus by year to 2030 and by segment, each broker's model for next quarter, the history of the multiple, peers, ownership, options, suppliers, customers. | Compare every research number with what the market expects. | No gap either way. The multiple is at the bottom of its 12-month range. |
| 5. Agent test runs | Eight research runs (333 agents) to 29 September; an overnight run of 49 tasks; a thesis hunt (37 agents: 15 candidates, 7 examined by three checkers each, three judges); a gigawatt rebuild (10 agents, three versions); a model check (4 checkers). | Generate candidate theses, then try to break each one. | No candidate won. The gigawatt view was kept as the way to explain the forecast, not as a gap. |
| 6. Stress tests | Both directions attacked with equal force; nine arithmetic tests that contain no forecast; every number checked three ways; every holding period from 3 to 12 months; a second Bloomberg pull. | Find out whether the call survives. | It did. Section 9 lists each test. |

> Side note. **The lesson in the table on the right.** The lean changed each time only one side had been attacked. It stopped changing once both sides were attacked together. That is why section 9 tests the long and the short.

### How the call moved

| Date | Lean | What changed it |
|---|---|---|
| 22 Sep | Short | Worry that paid factory reservations would not turn into orders |
| 23 Sep | Long, weak | A technical sweep found no gap, and nine bear arguments failed their checks |
| 29 Sep | Long | The backlog schedule showed 2027 deliveries are mostly 2025 orders, against the Sell note |
| 30 Sep, early | Short into January considered | Research EBITDA for 2027 sat 7 to 10% below analysts |
| 30 Sep, later | Long 12 months, low conviction | Both sides attacked together: neither has an edge on a number; the multiple decides |
| 1 Oct | Long 12 months | Bloomberg showed no gap either way |
| 2 Oct | Unchanged | Second pull, Electrification test, horizon test |
| 2 Oct, evening | Unchanged | An independent second AI read the corpus: no number against the call, two wording fixes (section 9, rows 23 and 24) |

Research files for each stage are listed under [R39].

## 3. The company

> Side note. **What it sells.** *Power*: gas turbines (plus nuclear, hydro and steam), sold once and then serviced for decades. *Electrification*: grid equipment such as transformers and switchgear. *Wind*: onshore and offshore turbines. It was split off from General Electric in April 2024.

| $M | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|
| Revenue | 33,239 | 34,935 | 38,068 | 17,143 | 20,442 |
| Adjusted EBITDA | 807 | 2,035 | 3,196 | 1,227 | 2,146 |
| Power revenue | 17,436 | 18,127 | 19,767 | 9,234 | 10,449 |
| of which equipment | 5,598 | 5,708 | 6,686 | 2,996 | 3,851 |
| of which services | 11,838 | 12,419 | 13,081 | 6,238 | 6,598 |
| Power EBITDA | 1,722 | 2,268 | 2,902 | 1,303 | 1,842 |
| Electrification revenue | 6,378 | 7,550 | 9,642 | 4,001 | 6,597 |
| Electrification EBITDA | 234 | 679 | 1,433 | 519 | 1,200 |
| Wind revenue | 9,826 | 9,701 | 9,110 | 4,095 | 3,459 |
| Wind EBITDA | (1,033) | (588) | (598) | (312) | (657) |
| Gas turbine GW sold | 13.8 | 11.9 | 15.3 | 8.2 | 7.5 |
| Gas turbine GW ordered | 9.5 | 20.2 | 29.8 | 12.2 | 20.1 |

Sources: [R1] [R3]. H1 2025 is restated to the 2026 segment basis.

_Figure: Adjusted EBITDA: reported, then analysts' consensus ($M)._ Source: 10-K FY2025 [R1]; Bloomberg consensus, 2026-10-01 [R12].

> Side note. **Backlog** is work already under contract and not yet delivered. The filings call it remaining performance obligation, or RPO. A *slot reservation* is a paid place in the factory queue. It is not yet an order and is not in backlog.

- **Backlog at 30 June 2026:** $176,284M, of which equipment $87,821M and services $88,463M. Power equipment $39,261M. Electrification $44,563M. Wind $20,388M. [R3]
- **Balance sheet at 30 June 2026:** cash $13,120M including about $400M restricted; borrowings $2,849M. [R3]
- **Guidance for FY2026** (22 July 2026): revenue $45.5B to $46.5B; EBITDA margin 12% to 14%; Power margin 17% to 19%; Electrification revenue $14.5B to $15.0B and margin 18% to 20%; free cash flow $11.5B to $12.5B. [R6]
- **2028 framework** (28 January 2026): revenue $56B, EBITDA margin 20%; Power 22%, Electrification 22%, Wind 6%. [R7]
- **Guidance record:** company-level guidance has been raised or held at every report since the spin-off. The 2026 revenue guide went from $41B to $42B in December 2025 to $45.5B to $46.5B in July 2026. The Wind guide was cut once, at Q3 2025. [R6] [R7] [R8]
- **Tariffs:** the company cut its estimate of the 2026 tariff cost from $250M to $350M (April) to $100M to $200M (July), after contractual protections and mitigation. [R3] [R4]
- **Acquisition:** Prolec GE (transformers) bought on 2 February 2026 for $5,254M in cash. It adds about $3.1B of Electrification revenue in FY2026. [R3] [R6]
- **Next events:** Q3 results on 28 October 2026; the 2027 outlook with results in late January 2027; an investor day on the 2030 outlook in spring 2027. [R9] [R31]

## 4. The industry

> Side note. **In plain words.** Three companies in the world build large gas turbines. Buyers have ordered far more than the three can make, so prices rose and the queue is years long. Nobody knows how long this lasts. That question, not this year's profit, is what moves the share price.

### Demand

- World orders stood at 110 GW at the end of 2025 against factory capacity of 60 to 70 GW a year. Wood Mackenzie expects orders to peak in 2026 and turbine prices to reach about $600 per kW by the end of 2027, up 195% since 2019. [R16] [R18]
- The makers disagree on how long it lasts. Mitsubishi Heavy expects about 70 GW a year on average over five years. Siemens Energy's chief executive has spoken of up to 120 GW a year. [R15] [R19]
- The largest US grid (PJM) held its auction for 2028/29 in July 2026. It cleared at the price cap for the third time in a row. The next auction is on 9 December 2026. [R33]
- NRG's filings show its paid turbine reservations with GE Vernova rising from 1.2 GW (February 2025) to 3.6 GW (February 2026), beside a development agreement for up to 5.4 GW of new gas plants. [R40]
- Spending forecasts for 11 large US utilities: $140.6B (2026), $155.8B (2027, +10.9%), $160.9B (2028, +3.3%). [R13]
- Spending forecasts for the five largest data-centre builders: $844B, then $1,111B (+32%), then $1,203B (+8%). The last figure has been flat since early September. [R12] [R13]

### Supply

- Three firms build large gas turbines at scale: GE Vernova, Siemens Energy and Mitsubishi Heavy. [R21]
- Reported order books: GE Vernova 116 GW (53 firm plus 63 reserved); Siemens Energy 69 GW firm; Mitsubishi 35 GW of large-frame units. The three do not count the same things. [R6] [R19]
- One industry estimate has world capacity rising from 67 GW to 102 GW a year by 2030. One source only. [R24]
- GE Vernova's lead time is about three years. In July 2026 it said it was mostly sold out through 2030 and expected more than half of 2031 to be contracted by year end. [R9] [R26]

_Figure: GE Vernova gas order book: firm backlog and slot reservations (GW)._ Source: GE Vernova earnings releases, Q3 2025 to Q2 2026 [R6] [R7] [R8]. Reservations converted into orders: 7, 8, 6 and 10 GW in the last four quarters.

## 5. Thesis part one: the forecast in gigawatts

> Side note. **The idea.** Turbine revenue is two numbers multiplied: how many gigawatts ship, and the price per kilowatt. One gigawatt is one million kilowatts, about the output of one large power plant. So we can ask of the analysts' forecast: is the price settled, is the demand settled, is the output settled?

Power equipment revenue = gigawatts shipped x dollars per kW.

| Question | What analysts' figures need | What GE Vernova has | Settled? |
|---|---|---|---|
| Price | $579 per kW in 2027, $662 in 2028 | $741 per kW in signed backlog; $513 realised in H1 2026 | 2027 yes. 2028 needs backlog prices to keep rising, as they have for four quarters |
| Demand | Buyers for 111 GW of planned output, H2 2026 to 2030 | 53 GW firm + 63 GW of paid reservations = 116 GW | Firm orders cover 48%; reservations the rest, and 7, 8, 6 and 10 GW of them converted in the last four quarters |
| Output | 20 GW a year from Q3 2026 | 14.6 GW in the last four quarters | No |

_Figure: Gas turbine gigawatts shipped each quarter, and the plan._ Source: 10-K FY2025, 10-Q Q1 and Q2 2026 [R1] [R3] [R4]; plan from the Q2 2026 call [R9]. Hollow bars are the plan.

> Side note. **The open item.** The company must go from about 3.7 GW a quarter to 5. That is a 37% step. It shipped 5.2 GW once before, in Q2 2025. The first reading comes on 28 October.

### The numbers behind the table

- **Price analysts need** = their Power equipment revenue divided by gigawatts on the company's path (17.5, 21, 24 and 26 GW for 2026 to 2029): $534, $579, $662, $741. The 21 GW for 2027 and 26 GW for 2029 are readings of the plan, not figures the company gave. [R12] [R9]
- **Signed price** = $39,261M of Power equipment backlog divided by 53 GW = $741 per kW. It includes non-gas equipment and moves with the product mix. [R3] [R6]
- **The signed price has risen four quarters running:** $556 (June 2025), $575, $618, $648, $741 per kW (June 2026), from each filing's Power equipment backlog and the firm gigawatts in the releases. [R1] [R3] [R4] [R5] [R11]
- **Realised price lags the backlog average.** Over five yearly windows, revenue per kW shipped was 78% to 94% of the backlog price at the start of the window (average 87%). On $741 that is $578 to $697, average $645. 2027 ($579) is covered at the average. 2028 ($662) needs the backlog price near $760 per kW by December 2027; new orders are entering at about $900 per kW (an inference), so that is likely but not settled. A 2028 shortfall of 7% to 11% would cost 2% to 14% of 2028 EBITDA, depending on whether it is mix or price. Found by the second-opinion check.
- **Planned output**, H2 2026 to 2030 = 10 + 21 + 24 + 26 + 30 = 111 GW. Some firm orders deliver in 2031. [R9]
- **Shipped by quarter:** 3.0, 5.2, 4.0, 3.1 (2025), then 4.2 and 3.3 (2026). [R1] [R3] [R4]

_Figure: Power equipment revenue per kW: reported, and what analysts' figures imply._ Source: Filings [R1] [R3]; Bloomberg consensus, 2026-10-01 [R12]; dashed line is the signed backlog price.

> Side note. **HA turbines** are the largest and newest class. The Sell note of 14 September said 2027 deliveries were ordered in 2024 at old prices. The unit count in the filings says otherwise for this class.

### What ships next

- 70 HA turbines were in backlog at 30 June 2026. The roll: 32 at the end of 2024, plus 43 ordered, less 24 sold in 2025 = 51; plus 27 ordered, less 8 sold in H1 2026 = 70. [R1] [R2] [R3]
- Between 62 and 70 of the 70 were ordered in 2025 or later. If the oldest ship first it is all 70. Without that assumption the floor is 62. [R1] [R3]
- **Near-term check.** The 10-Q says 36% of the $87,821M equipment backlog is due within a year: $31,616M. Analysts have $30,245M of equipment revenue for the same four quarters. The schedule is 4.5% higher before any new order. In seven past windows the actual figure beat the schedule six times. The profit effect is small, about $0.2B. [R3] [R11] [R12]

_Figure: Backlog schedule back-test: actual equipment revenue divided by the scheduled amount (1.00 = schedule met)._ Source: 10-K and 10-Q filings, seven windows opening December 2023 to June 2025 [R1] [R2] [R11].

_Figure: Power EBITDA margin: reported, then analysts (%)._ Source: Filings [R1] [R3]; Bloomberg segment consensus, 2026-10-01 [R12]; dashed line is the company's 2028 target of 22% [R7].

**What these numbers support.** Analysts' forecast assumes the company's own output plan at prices already signed. It needs no new orders and no new price rises.

**What they do not support.** Any claim that analysts are too low by a stated percent. Three attempts at that failed their error tests (section 9, rows 5 to 8).

## 6. Thesis part two: why the factory is the limit

> Side note. **The physics.** The first row of blades sits in gas hotter than the melting point of the blade's own metal. Each blade is grown as a single crystal of nickel alloy, with cooling channels inside and a ceramic coat outside. Few foundries can make them, and the same foundries make jet-engine blades.

- Four Western foundries make these blades at scale: Precision Castparts, Howmet, CPP and Doncasters. [R18] [R27]
- **From the company, 22 July 2026:** output moves from about 3 GW a quarter to 5 from the third quarter and is "very well on track"; 325 new machines are installed and about 400 will be by year end; workers were hired and trained a year ahead; the step to 24 GW in 2028 depends on castings and forgings arriving in 2027; a new HA unit reaches its first major service four years after start. [R9]
- **From the blade maker.** Howmet's gas turbine revenue was $321M in Q2 2026 against $233M a year earlier (+38%), and $605M in H1 2026 against $437M (+38%), from its 10-Q; $944M in FY2025 from its 10-K. The whole company grew 24%. [R41] Its chief executive: "Demand in the gas turbines market is extraordinary with customers already revisiting and adding to their demand outlooks." [R28]
- On its call Howmet claimed a share "in excess of 50% globally for turbine blades" and described a new plant in Japan, an expansion in Europe and more equipment in Virginia, with more capacity "in '27, but with another major step into '28 and '29". Secondary source. [R29]
- **Supplier timing, from their filings.** Howmet's main capacity additions land in 2028 and 2029, and a new commitment takes about 24 months. Carpenter's new melt capacity is commissioned about mid-2027. ATI says it is prioritising aerospace. Woodward sold its heavy-duty combustion parts line in FY2025. Nothing contradicts the 2027 output plan; the 2028 step to 24 GW carries timing risk. No supplier states capacity in gigawatts or units. [R41]
- GE Aerospace, a separate company, agreed in September 2026 to buy CPP for $11.75B. SpaceX is building its own blade foundry. News reports. [R20] [R21]
- Units sold: heavy-duty turbines 54 in 2025, 15 in Q1 2026, 13 in Q2 2026. HA units 24 in 2025, then 5 and 3. [R1] [R3] [R4]

_Figure: Howmet revenue growth, year on year, by quarter (%)._ Source: Bloomberg, 2026-10-02 [R13]; gas turbine line from Howmet's Q2 2026 release [R28].

> Side note. **Two edges to this.** The limit helps the next 12 months: the capacity is already installed and all three makers face the same shortage, so prices hold. It also means orders must slow once the factories are sold out. That is a reason for a lower multiple, and it is why the base case uses 25x and not today's 29.6x.

**Reading.** The factory limit supports the next year of earnings and protects price. It caps upside in volume, and "sold out" means order growth must slow.

## 7. What the market thinks

> Side note. **Consensus** is the average of the forecasts that brokers send to Bloomberg. For 2027 EBITDA there are 36 of them. We call them "analysts" in this file.

This section sets out what analysts forecast, what the share price already assumes, and how the market has behaved. All figures come from the two Bloomberg pulls unless marked.

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

> Side note. **What is priced in.** Profit doubling in 2026 and rising by half again in 2027, at a multiple near the bottom of its 12-month range. The market already believes the growth. It is paying less for it than it did in April.


- **The multiple.** 28.5x as Bloomberg quotes it. Twelve-month range 27.3x to 42.4x, median 32.5x. No week at or below 26x in the last 53. The 2025 low was 18.5x on 4 April 2025. [R12]
- **The past year.** The price rose 63% ($606 to $988) while the multiple fell from 32.5x to 28.5x. Forward profit rose 85%. [R12]
- **The last three months.** The price fell 13%. Analysts' 2027 profit rose 2%. The multiple fell 19%. The 14 related stocks pulled on 2 October fell a median 11%, so the fall is group-wide. [R12] [R13]
- **What moves the price.** Across the 20 months with full data (February 2025 to September 2026), the monthly return moved with the change in the multiple (correlation 0.95), not with changes in analysts' 2027 profit (0.25) or with how far the average target sat above the price (0.02). [R12] [R14]
- **Analysts.** 32 buy, 7 hold, 2 sell. Average target $1,225, 24% above the price. Short interest 3.3% of the float. [R12]
- **Analysts have been too low.** Since listing, their average target sat about 7% above the price, while the stock returned 26%, 59% and 90% on average over the next 3, 6 and 9 months. [R12] [R14]
- **Estimate changes in three months.** Revenue +1.7%, +2.2%, +3.0%, +5.8% for 2026 to 2029. EBITDA +2.5%, +2.0%, -1.3%, +6.2%. No fresh wave of upgrades. [R13]

_Figure: GE Vernova share price since listing ($)._ Source: Daily closes [R14]; Bloomberg close for 1 October 2026 [R12]. First close $131.25 on 27 March 2024; highest close $1,174.86 on 30 June 2026.

> Side note. **The Sell note.** One research firm said on 14 September that the shares are worth $470. The shares fell 8.6% that day and have since recovered. Section 5 shows why its main premise does not fit the filings.

- **The Sell note.** GLJ Research began coverage on 14 September 2026 with a Sell rating and a $470 target. Its argument: turbines delivered in 2027 were ordered in 2024 at old prices. It puts 2027 EBITDA at $7.42B. The stock closed at $957.27 on 11 September and $874.76 on 14 September. Known from press summaries only. [R22]
- **Peak orders.** Wood Mackenzie expects orders to peak in 2026. A Jefferies note of 12 September said investors were too fixed on that and were overlooking services. Evercore ISI kept its Outperform rating and $1,350 target in early October. News reports. [R16] [R23] [R35]
- **Options.** Implied volatility is 50.9% for 30 days, 48.2% for 3 months and 49.3% for 12 months. That means a one-standard-deviation range of about $603 to $1,616 in a year. Options that protect against a fall cost about the same as options that gain from a rise. For the results day of 28 October they imply a move of about 5%; the average of the last ten results days is 5.4%. [R13] [R14]

## 8. Valuation

> Side note. **How a target price is built.** Take the profit expected for the 12 months after the target date. Multiply it by the multiple. Add the cash the company holds beyond what it owes. Divide by the number of shares.

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

> Side note. **Why 25% and 75%.** The target date is 30 September 2027. The 12 months after it cover the last quarter of 2027 and the first three quarters of 2028. So the forward profit is one quarter of the 2027 figure plus three quarters of the 2028 figure.

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

> Side note. **The split.** Holding today's 29.6x would give $1,328, which is +34.5% from profit growth alone. The fall to 25x takes away 20.4%. Net +14.0%. If you start from Bloomberg's quoted 28.5x instead, the split reads +29.7% and -15.7%. Use one basis and say which. The target does not change.

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

_Figure: EV / next-12-month EBITDA, with profit growth expected next year._ Source: Bloomberg, 2026-10-02 [R13]; GE Vernova from 2026-10-01 [R12].

> Side note. **Why 12 months.** Each month you hold, the profit being valued grows about 3%. So the multiple you need to break even drops by about half a turn a month. Twelve months is the longest the rules allow, so it has the lowest hurdle.

The rules allow a holding period of 3 to 12 months. The table below works out every one of them on the same figures, so the choice of 12 can be defended.

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

_Figure: The hurdle falls every month: break-even multiple against the base-path multiple._ Source: Arithmetic on Bloomberg consensus, 2026-10-01 [R12].

### Other checks on the target

- **Medians instead of means:** forward EBITDA 11,987, price at 25x $1,145, break-even 21.5x. [R13]
- **A harder downside:** the 2025 low of 18.5x on bear EBITDA gives $757 (-23%). The bear case is not the worst case.
- **Not counted as upside:** about $7.2B of cash built by September 2027, about $27 a share.
- **A second build:** the reference model made during research rebuilds the forecast by segment and gives $1,134 for the base. The memo must quote the team's own model.

## 9. Every stress test, and what happened

> Side note. **How to read this table.** Each row is one attempt to find a number where analysts are wrong, or a reason the call fails. "Error band" is how wrong our own estimate could be. A gap smaller than its error band proves nothing.

Each row below is one test. Rows 1 to 13 looked for a number where analysts are wrong. Rows 14 to 18 tested the bear side and the short. Rows 19 to 22 were run on 2 October, after the second Bloomberg pull. Rows 23 to 25 come from an independent second AI that read the corpus and the suppliers' filings on the evening of 2 October.

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

_Figure: Electrification: share of opening backlog recognised as revenue in the next four quarters (%)._ Source: 10-K and 10-Q segment tables [R1] [R2] [R3] [R4] [R5] [R11]; last bar is analysts' figure, Bloomberg 2026-10-01 [R12]. Prolec removed from the two 2025 windows.

> Side note. **Three ways to check a number.** First, against the filing or Bloomberg file it came from. Second, against a second source, such as the machine-readable data the company files. Third, by recalculating it from the typed inputs.

### How the numbers were checked

- 79 checks against filing text and filed data, and 131 checks against the Bloomberg files and by recalculation. All agreed with the figures in sections 1 to 8.
- The sections added on 2 October (second pull, Electrification, holding periods) were recalculated by script from the workbook and the filings.
- A four-checker review of the reference model produced 50 corrections. All are applied. The largest: diluted shares, not basic; restricted cash taken out of net cash.
- What has fewer than three sources: gigawatt and unit counts (filings only); restricted cash (a rounded figure); the 67 to 102 GW capacity estimate (one post); the Sell note (press summaries); the 21 GW and 26 GW path for 2027 and 2029 (a reading of the plan); Howmet's call remarks (a transcript site).

## 10. Dated tests

> Side note. **Why dated tests.** The rules ask for evidence with a predictive part. Each row is something that will be published on a known date and can prove the view right or wrong.

Each row is a figure that will be published on a known date. The last two columns say what would support the long and what would warn against it.

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

## 11. Risks, and what would make us sell

> Side note. **The main risk in plain words.** The company can do everything right and the shares can still fall, if investors decide to pay less for each dollar of profit. That happened in the last three months.

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

## 12. Questions a judge is likely to ask, with the facts

> Side note. **Use.** These are the facts for each answer. The words of the answer are the team's.

Eight questions, each with the facts that answer it.

| Question | Facts to answer with |
|---|---|
| Why 25x, when the direct rivals trade at 12.7x and 15.1x? | Every week of the last 12 months was above 27x. Howmet and GE Aerospace trade at 25.7x and 25.0x with a third of the growth. The case still returns -3.7% at 21x on base EBITDA and breaks even at 21.8x. It is an assumption, and the file says so. |
| Last quarter was 3.3 GW. Why will it be 5? | The company shipped 5.2 GW in Q2 2025. 325 machines are installed and about 400 will be by year end. The blade maker's turbine sales grew 38%. The first reading is 28 October. |
| Power equipment is a quarter of revenue. Why build the thesis on it? | It is where the growth is: analysts have it rising from $9,342M to $15,888M between 2026 and 2028. Each turbine shipped adds decades of service revenue. Power is about 62% of analysts' 2028 EBITDA. |
| If you agree with analysts' earnings, what do you know that the market does not? | Nothing about earnings, and the file does not claim to. The view is about the hurdle: the multiple can fall 26% before the position loses, and in the stock's history it has not fallen that much over any 8 to 12 month window. |
| Why 12 months and not 3 or 6? | The break-even multiple is 27.2x at 3 months, 25.1x at 6 and 21.8x at 12. The return builds evenly, at a little over 1% a month. Safety is what grows with time. |
| Why not short? | The short's best window is 3 months, and it needs the multiple below 27.2x. Company guidance has been raised or held at every report. Nine bear arguments failed their checks. |
| Is the Sell note right? | For the largest turbines its premise is contradicted: 62 to 70 of the 70 HA units in backlog were ordered in 2025 or later. |
| How much of the $741 per kW will actually be realised? | Over five yearly windows, revenue per kW shipped ran at 78% to 94% of the backlog average, 87% on average. On $741 that is $578 to $697. Analysts need $579 in 2027 and $662 in 2028. |
| What happens to cash flow when the deposits stop growing? | Analysts have free cash flow falling from $12.2B to $7.7B in 2027 while EBITDA rises; that already assumes deposit growth slows from $15.7B to about $5.5B. The company's own floor of at least $24B for 2025 to 2028 sits below analysts for 2027 and 2028. The valuation rests on EBITDA, not cash. |
| What makes you sell? | Section 11. |

## 13. What the research does not support

> Side note. **Why list these.** A judge who finds one claim that does not hold will doubt the rest. These are the claims to leave out.

- That analysts are too low, or too high, by any stated percent.
- That the H1 2027 Power equipment figure will beat by 14 to 17%. The sign held in every variant; the size did not.
- That the 21 GW (2027) and 26 GW (2029) output figures are company numbers. They are readings of the plan.
- That world capacity will rise from 67 to 102 GW a year. One source.
- The details of the Sell note. It is known only from press summaries.
- That past price behaviour predicts the next year. The history is two and a half years long and covers one long rise.
- Howmet's call remarks on capacity and market share, which come from a transcript site. Its dollar figures ($321M in Q2 2026, $605M in H1 2026, $944M in FY2025) are from its own filings and can be cited.

## 14. Starting the model

> Side note. **The model is the team's.** This section lists the inputs, where each comes from, and the totals your own workbook should reach. It does not lay out cells or formulas.

**What the rules ask of the model:** clearly formatted, easy to follow, with the assumptions shown and justified, and consistent with the thesis. Judging looks at how well the model and the thesis fit together. [R37]

### What a valuation model of this kind usually shows

1. An inputs page. Every typed number appears once, with its unit, date and source.
2. Reported history by segment (section 3).
3. The forecast by year: analysts' figures, the company plan path, and any view of your own (sections 7 and 8).
4. The gigawatt exhibit: output and price per kW against analysts' Power equipment revenue (section 5).
5. The valuation: forward profit, multiple, net cash, diluted shares, price (section 8).
6. The three cases side by side, and the weighted value.
7. A sensitivity grid: price at each multiple and each profit case.
8. A row of checks that should all read zero or "OK".

### Totals your own workbook should reach

| Check | Value |
|---|---|
| Diluted shares | 269.334M |
| Net cash | 8,713 |
| Forward EBITDA at 30 September 2027: bear / base / bull | 10,547.5 / 11,782.5 / 12,371.6 |
| Price: bear / base / bull | $855 / $1,126 / $1,341 |
| Weighted price | $1,112 |
| Break-even multiple | 21.8x |
| Multiple today on the same basis | 29.6x |
| Price if the multiple held at 29.6x | $1,328 |

### Traps that moved the answer during research

- Basic shares instead of diluted shares.
- Leaving restricted cash and noncontrolling interests in net cash.
- Mixing Bloomberg's 28.5x with a forward profit built another way. Section 8 explains the two bases.
- Prices from different dates. Keep 1 October 2026 throughout.
- Two segment EBITDA series on Bloomberg. The tables here use the adjusted series, which matches the company's own measure.
- H1 2025 figures: use the ones restated to the 2026 segments.

### Where the facts for each part of the memo are

| Memo part | Sections of this file |
|---|---|
| Recommendation, price, target, return | 1, 8 |
| Thesis points | 5 and 6 (gigawatts and the factory); 1 and 8 (profit growth against the multiple) |
| Market view | 7 |
| Company and industry | 3, 4 |
| Valuation and scenarios | 8 |
| Catalysts | 10 |
| Risks and mitigants | 11 |
| Sources | 16 |

## 15. The Bloomberg work: what was pulled and how to cite it

> Side note. **How the pulls worked.** A workbook of Bloomberg formulas was prepared in advance. Opened on a terminal, it filled itself with live data. Screens that formulas cannot reach were exported by hand.

Two full pulls were made on a Bloomberg terminal, on 1 and 2 October 2026. A third, short workbook is waiting to be filled. The table lists what each one holds.

| Pull | What it holds | Bloomberg fields or screens | Main result | File |
|---|---|---|---|---|
| 1 October, workbook | Price and value, analysts' forecasts for four years, their weekly history, the multiple and its history, ratings, short interest | PX_LAST, CUR_MKT_CAP, CURR_ENTP_VAL, BEST_EV_TO_BEST_EBITDA, BEST_SALES, BEST_EBITDA with median, high, low and count, BEST_ESTIMATE_FCF, BEST_TARGET_PRICE, TOT_BUY_REC, SI_PERCENT_EQUITY_FLOAT | Analysts' EBITDA 6,334 / 9,471 / 12,553 / 16,496; multiple 28.5x; no gap against research either way | GEV_bloomberg_pull_filled_2026-10-01.xlsx |
| 1 October, 20 screen exports | Forecasts to 2030, forecasts by segment, each broker's model for Q3 2026, valuation against history and peers, holders, customers | EEO, EEO Company Specific, MODL, EEG, EQRV, RV, HDS, SPLC, DDM | Segment forecasts by quarter and year; premium to the benchmark at its two-year average | GEV_Pull_2026-10-01 folder |
| 2 October, workbook | 14 suppliers and rivals, 28 customers, options, estimate changes | CHG_PCT_3M, SALES_REV_TURN, BEST_CAPEX, implied-volatility fields, the 4-week and 3-month change fields, SUPPLY_CHAIN_SUPPLIERS | Sections 7 to 9: group-wide fall, fair options, Howmet's growth, slower customer spending in 2028 | GEV_bloomberg_pull_2_filled_2026-10-02.xlsx |
| 2 October, third workbook | Howmet's quarterly outlook; supply-chain links in dollars | BEST_SALES by quarter; RELATIONSHIP_AMOUNT (untested) | Not yet returned | GEV_bloomberg_pull_3.xlsx |

All files are in `gev-corpus/data/bloomberg/`.

- **How to cite:** "Bloomberg, 2026-10-01" or "Bloomberg, 2026-10-02", with the measure named, for example "Bloomberg consensus adjusted EBITDA, 36 estimates".
- **Licence:** the data is for academic use. Keep the files inside the team. Do not post them.
- **One caution on the multiple:** Bloomberg's 28.5x uses its own blend of forecast years. A simple model cannot reproduce it, which is why this file also gives 29.6x on the model's basis.
- **One caution on segments:** segment forecasts come from fewer brokers than company totals. The export hides most broker names, so the count behind each segment line is not known.

## 17. Limits of this file

> Side note. **Bottom line.** The call is a 12-month long that rests on arithmetic and on one assumption, the 25x multiple. Everything else in this file is there so the team can check it.

- This is a research file made with AI assistance. Under rule 10 that use has to be disclosed, and the memo and the model have to be the team's own work. [R37]
- It contains no private information. Every source is a public filing, a public release or call, a licensed Bloomberg figure, or a published article.
- News items and transcript sites are marked as secondary. Check them before citing.
- Figures are as of 1 and 2 October 2026. Results on 28 October will date them.
- Charts for the memo should be remade by the team from its own model.
- An independent second AI (Grok) read the corpus and the suppliers' filings on the evening of 2 October 2026, in two passes, and found no number against the call. Its findings are in section 9 (rows 23 to 25), sections 5 and 6, and section 11. Disclose its use with the rest.

## 16. References

- **R1** GE Vernova, Form 10-K for FY2025, filed 29 January 2026 (accession 0001996810-26-000015). https://www.sec.gov/Archives/edgar/data/1996810/000199681026000015/gev-20251231.htm
- **R2** GE Vernova, Form 10-K for FY2024, filed 6 February 2025 (0001996810-25-000011). https://www.sec.gov/Archives/edgar/data/1996810/000199681025000011/gev-20241231.htm
- **R3** GE Vernova, Form 10-Q for Q2 2026, filed 22 July 2026 (0001996810-26-000148). https://www.sec.gov/Archives/edgar/data/1996810/000199681026000148/gev-20260630.htm
- **R4** GE Vernova, Form 10-Q for Q1 2026, filed 22 April 2026 (0001996810-26-000064). https://www.sec.gov/Archives/edgar/data/1996810/000199681026000064/gev-20260331.htm
- **R5** GE Vernova, Form 10-Q for Q3 2025, filed 22 October 2025 (0001996810-25-000160). https://www.sec.gov/Archives/edgar/data/1996810/000199681025000160/gev-20250930.htm
- **R6** GE Vernova, Q2 2026 earnings release, 22 July 2026 (8-K 0001996810-26-000147). https://www.sec.gov/Archives/edgar/data/1996810/000199681026000147/gev-20260722.htm
- **R7** GE Vernova, Q4 2025 earnings release, 28 January 2026 (8-K 0001996810-26-000012). https://www.sec.gov/Archives/edgar/data/1996810/000199681026000012/gev-20260128.htm
- **R8** GE Vernova, Q1 2026 earnings release, 22 April 2026 (8-K 0001996810-26-000063); Q3 2025 release (8-K 0001996810-25-000159); 2025 Investor Update press release, 9 December 2025. https://www.sec.gov/Archives/edgar/data/1996810/000199681026000063/gev-20260422.htm
- **R9** GE Vernova, Q2 2026 earnings call transcript, 22 July 2026. https://www.gevernova.com/sites/default/files/gev_webcast_transcript_07222026.pdf
- **R10** GE Vernova at the Morgan Stanley Laguna conference, transcript, 16 September 2026 (gevernova.com investor pages; read 1 October 2026). 
- **R11** Earlier filings used for the back-tests: Forms 10-Q for Q1 to Q3 2024 and Q1 to Q2 2025; Form S-1/A of 2024. https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1996810&type=10-Q
- **R12** Bloomberg, 2026-10-01: consensus (BEst), segment consensus (EEO Company Specific), broker models (MODL), multiples and their weekly history, ratings, peers (RV, EQRV). Academic licence; no public link. 
- **R13** Bloomberg, 2026-10-02: suppliers and rivals, customers' capital spending, implied volatility, estimate changes, supply-chain lists. Academic licence; no public link. 
- **R14** Daily closing prices in the research database, 27 March 2024 to 18 September 2026. 
- **R15** Mitsubishi Heavy Industries, FY2025 fourth-quarter results, questions and answers. https://www.mhi.com/finance/library/result/pdf/fy20254q/qa_20254q.pdf
- **R16** Wood Mackenzie, press release: gas turbine prices soar 195% as market faces supply-demand crisis. https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis/
- **R17** Utility Dive: GE Vernova gas turbine backlog climbs to 116 GW. https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/
- **R18** Trade article: Gas Turbine Orders 2025-26: Backlog, Price and Lead-Time Data (secondwatt.com). https://secondwatt.com/resources/gas-turbine-orders-2025-backlog-lead-times-buyer-guide
- **R19** News: The Gas Turbine Shortage Just Became AI's Biggest Constraint (Yahoo Finance). https://finance.yahoo.com/energy/articles/gas-turbine-shortage-just-became-210000180.html
- **R20** News on the SpaceX blade foundry, 30 August and 2 September 2026 (Yahoo Finance). https://finance.yahoo.com/technology/ai/articles/elon-musk-trying-break-ge-141624492.html
- **R21** News on GE Aerospace buying Consolidated Precision Products, September 2026 (Yahoo Finance). https://finance.yahoo.com/economy/policy/articles/good-ge-aerospace-may-not-154622399.html
- **R22** Press summary of the GLJ Research Sell initiation, September 2026 (Yahoo Finance). https://finance.yahoo.com/markets/stocks/articles/glj-starts-ge-vernova-sell-122234358.html
- **R23** Press summary of the Jefferies note of 12 September 2026 (Blockonomi). https://blockonomi.com/ge-vernova-gev-stock-jefferies-says-recent-23-decline-creates-entry-point/
- **R24** Enverus Intelligence Research post citing BloombergNEF capacity data (LinkedIn). One source. https://www.linkedin.com/posts/enverus-intelligence-research_gas-turbine-manufacturing-capacity-not-demand-activity-7500600955910959104-osJ0
- **R25** SemiAnalysis: How AI Labs Are Solving the Power Crisis. https://newsletter.semianalysis.com/p/how-ai-labs-are-solving-the-power
- **R26** Earnings call highlight articles for Q1 and Q2 2026 (Yahoo Finance). https://finance.yahoo.com/sectors/energy/articles/ge-vernova-q1-earnings-call-030652565.html
- **R27** Clean Air Task Force, report on hydrogen in heavy-duty gas turbines (blade casting cost and yield). https://cdn.catf.us/wp-content/uploads/2023/07/13144950/emissions-performance-implications-hydrogen-fuel-heavy-duty-gas-turbines.pdf
- **R28** Howmet Aerospace, second quarter 2026 results, press release of 6 August 2026. https://www.howmet.com/press-release/2026-08-06/howmet-aerospace-reports-second-quarter-2026-results/
- **R29** Howmet Aerospace, Q2 2026 earnings call transcript (Motley Fool). Secondary. https://www.fool.com/earnings/call-transcripts/2026/08/13/howmet-aerospace-hwm-q2-2026-earnings-call-transcript/
- **R30** Zacks Equity Research on Howmet's Q2 2026 results (via Yahoo Finance). Secondary. https://finance.yahoo.com/markets/stocks/articles/hwm-q2-earnings-beat-estimates-164300840.html
- **R31** TheStreet: report of the chief executive's remarks on the $200 billion backlog, the January outlook and the spring 2027 investor day. https://www.thestreet.com/investing/stocks/gev-ge-vernova-ceo-strazik-says-200b-backlog-target-on-track-very-early-2027
- **R32** Power Engineering: first US construction permit for the BWRX-300 small reactor, 29 September 2026. https://www.power-eng.com/nuclear/smrs/tennessee-clinch-river-bwrx-300-smr-nrc-construction-permit/
- **R33** NRG, market update on the PJM auction for 2028/29, July 2026; PJM auction schedule. https://www.nrg.com/assets/documents/insights/white-papers-and-webinars/pjm-bra-results-july2026.pdf
- **R34** Siemens Energy, investor relations: results calendar and Q3 FY2026 earnings release. https://www.siemens-energy.com/global/en/home/investor-relations.html
- **R35** Investing.com: Evercore ISI reiterates its GE Vernova rating on raised estimates. https://www.investing.com/news/analyst-ratings/evercore-isi-reiterates-ge-vernova-stock-rating-on-raised-estimates-93CH-4926745
- **R36** GE Vernova, press release: fourth quarter 2026 dividend, 30 September 2026. https://www.gevernova.com/news/press-releases/ge-vernova-declares-fourth-quarter-2026-dividend
- **R37** Citadel Fall 2026 Pitch Competition, Official Rules. https://www.citadel.com/wp-content/uploads/2026/06/Citadel-Fall-2026-Pitch-Competition-Official-Rules.pdf
- **R38** GE Vernova, 2025 Investor Update: press release and presentation, 9 December 2025. https://www.gevernova.com/sites/default/files/gev_webcast_pressrelease_12092025.pdf
- **R39** Team research files in gev-corpus/docs/research/multi_agent/: 03 technical wedge hunt; 07 pitch winners; 09 overnight run (ROBUSTNESS_PACK, BLOOMBERG_VERDICT, D04 January guide); 11 thesis hunt (THESIS_HUNT, GIGAWATT_ANGLE); 12 team brief; 13 thesis dossier. 
- **R41** Supplier filings on SEC EDGAR, read by the second-opinion check: Howmet 10-K FY2025 and 10-Q Q2 2026 (end-market revenue table); Carpenter Technology 10-K FY2026; ATI 10-Q Q2 2026; Woodward 10-Q June 2026. https://www.sec.gov/Archives/edgar/data/4281/000000428126000025/hwm-20260630.htm
- **R42** News reports of the Vineyard Wind settlement, 16 to 18 September 2026 (in the research corpus). 
- **R40** NRG Energy filings: Q4 2024 results release (February 2025), Form 10-Q for Q1 2025, Form 10-K for FY2025 (filed 24 February 2026). https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1013871&type=10-K
