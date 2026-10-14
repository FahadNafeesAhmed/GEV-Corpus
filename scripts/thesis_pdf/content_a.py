"""Sections 1 to 6 of the thesis file. Blocks: ("note", text) | ("md", markdown) | ("wide", markdown) | ("chart", key, title, source) | ("widechart", ...)."""

S = []

S.append(("1. The thesis on one page", [
    ("note", "**In plain words.** We expect the share price to be about 14% higher in a year. The reason is not that the company will beat forecasts. It is that a year from now investors will be valuing a much larger profit, and we assume they pay a lower price for each dollar of it."),
    ("md", """
| Item | Value | Source |
|---|---|---|
| Position | Long GE Vernova (GEV), 12 months, to 30 September 2027 | |
| Price | $987.45, close of 1 October 2026 | [R12] |
| Base case | $1,126 (+14.0%): analysts' EBITDA, valued at 25x | section 8 |
| Bear case | $855 (-13.4%): the company's own plan path, 21x | section 8 |
| Bull case | $1,341 (+35.9%): analysts' EBITDA plus 5%, 28.5x | section 8 |
| Weighted 25 / 50 / 25 | $1,112 (+12.6%) | section 8 |
| Break-even multiple | 21.8x (the price ends flat) | section 8 |
"""),
    ("note", "**Two terms.** *EBITDA* is profit before interest, tax, depreciation and amortisation. The *multiple* is the value of the whole company divided by the EBITDA expected over the next 12 months. A multiple of 25x means investors pay $25 for each $1 of yearly profit."),
    ("md", """
### The argument in three steps

1. **The profit the market prices will be about 36% larger in a year.** Next-12-month EBITDA is $8,687M today. At the target date it is $11,783M, on analysts' own figures. [R12]
2. **Those figures need nothing new to happen.** Seen in gigawatts: the price is already signed ($741 per kW in the backlog against the $579 to $662 analysts need), the demand is already signed or reserved (53 GW of firm orders plus 63 GW of paid factory reservations, against 111 GW of planned output to 2030), and the one open item is factory output (14.6 GW in the last four quarters against a plan of 20 a year). [R3] [R6] [R9]
3. **We assume the multiple falls, and the position still pays.** Today the multiple is 29.6x. The base case uses 25x. The position loses money only if the multiple ends below 21.8x.

### What this file does not claim

It does not claim that analysts are wrong on any number. Twenty-five attempts to find such a number either failed their checks or were too small to matter (section 9). An independent second AI repeated the search on the evening of 2 October and reached the same result.
"""),
    ("chart", "cases", "Share price in the three cases against today", "Team reference arithmetic on Bloomberg consensus, 2026-10-01 [R12]; filings for share count and net cash [R3]"),
    ("note", "**Reading the bridge.** If investors kept paying today's multiple, profit growth alone would lift the price by about $340. We assume they pay less, which takes back about $202. What is left is a gain of about $139."),
    ("chart", "bridge", "From today's price to the base target", "Same arithmetic. Today's multiple of 29.6x is measured the same way as the target multiple"),
]))

S.append(("2. How we got here: the process", [
    ("note", "**Why this section matters.** A judge will ask what you tested and how you know. This is the answer. Six stages, each feeding the next."),
    ("md", "The work ran from 19 September to 2 October 2026, in six stages. Each stage produced facts or tests that the next one used. The table lists what was built, why, and what came out."),
    ("widechart", "flow", "The six stages of the work", ""),
    ("wide", """
| Stage | What was built or pulled | What it was for | What came out |
|---|---|---|---|
| 1. Information corpus (from 19 September) | One searchable database: 208 GE Vernova filings and the filings of 33 other companies; 339,610 reported financial data points; 3,915 outside sources (1,789 research papers, 840 web pages, 777 news articles, 254 competitor documents, call transcripts, grid-operator reports); the US government register of power plants. 469,353 text passages in all. | Trace every company fact to a filing. Search for patterns nobody models. | The backlog schedule, the roll of HA turbines in backlog, the gigawatt and price-per-kW series. |
| 2. Science and factory angle | Turbine physics and manufacturing: blades, foundries, casting capacity, lead times. | Ask whether the limit is demand, price or the factory. | The factory is the limit. That protects price and caps volume. |
| 3. Past winners | 20 winning pitches from leading student competitions, read in full. | Learn what a winning pitch contains. | A clear claim, dated tests and a sell rule. A long on consensus numbers is a call on the multiple; two past winners lost money that way. |
| 4. Bloomberg (1 and 2 October) | Consensus by year to 2030 and by segment, each broker's model for next quarter, the history of the multiple, peers, ownership, options, suppliers, customers. | Compare every research number with what the market expects. | No gap either way. The multiple is at the bottom of its 12-month range. |
| 5. Agent test runs | Eight research runs (333 agents) to 29 September; an overnight run of 49 tasks; a thesis hunt (37 agents: 15 candidates, 7 examined by three checkers each, three judges); a gigawatt rebuild (10 agents, three versions); a model check (4 checkers). | Generate candidate theses, then try to break each one. | No candidate won. The gigawatt view was kept as the way to explain the forecast, not as a gap. |
| 6. Stress tests | Both directions attacked with equal force; nine arithmetic tests that contain no forecast; every number checked three ways; every holding period from 3 to 12 months; a second Bloomberg pull. | Find out whether the call survives. | It did. Section 9 lists each test. |
"""),
    ("note", "**The lesson in the table on the right.** The lean changed each time only one side had been attacked. It stopped changing once both sides were attacked together. That is why section 9 tests the long and the short."),
    ("md", """
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
"""),
]))

S.append(("3. The company", [
    ("note", "**What it sells.** *Power*: gas turbines (plus nuclear, hydro and steam), sold once and then serviced for decades. *Electrification*: grid equipment such as transformers and switchgear. *Wind*: onshore and offshore turbines. It was split off from General Electric in April 2024."),
    ("md", """
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
"""),
    ("chart", "ebitda", "Adjusted EBITDA: reported, then analysts' consensus ($M)", "10-K FY2025 [R1]; Bloomberg consensus, 2026-10-01 [R12]"),
    ("note", "**Backlog** is work already under contract and not yet delivered. The filings call it remaining performance obligation, or RPO. A *slot reservation* is a paid place in the factory queue. It is not yet an order and is not in backlog."),
    ("md", """
- **Backlog at 30 June 2026:** $176,284M, of which equipment $87,821M and services $88,463M. Power equipment $39,261M. Electrification $44,563M. Wind $20,388M. [R3]
- **Balance sheet at 30 June 2026:** cash $13,120M including about $400M restricted; borrowings $2,849M. [R3]
- **Guidance for FY2026** (22 July 2026): revenue $45.5B to $46.5B; EBITDA margin 12% to 14%; Power margin 17% to 19%; Electrification revenue $14.5B to $15.0B and margin 18% to 20%; free cash flow $11.5B to $12.5B. [R6]
- **2028 framework** (28 January 2026): revenue $56B, EBITDA margin 20%; Power 22%, Electrification 22%, Wind 6%. [R7]
- **Guidance record:** company-level guidance has been raised or held at every report since the spin-off. The 2026 revenue guide went from $41B to $42B in December 2025 to $45.5B to $46.5B in July 2026. The Wind guide was cut once, at Q3 2025. [R6] [R7] [R8]
- **Tariffs:** the company cut its estimate of the 2026 tariff cost from $250M to $350M (April) to $100M to $200M (July), after contractual protections and mitigation. [R3] [R4]
- **Acquisition:** Prolec GE (transformers) bought on 2 February 2026 for $5,254M in cash. It adds about $3.1B of Electrification revenue in FY2026. [R3] [R6]
- **Next events:** Q3 results on 28 October 2026; the 2027 outlook with results in late January 2027; an investor day on the 2030 outlook in spring 2027. [R9] [R31]
"""),
]))

S.append(("4. The industry", [
    ("note", "**In plain words.** Three companies in the world build large gas turbines. Buyers have ordered far more than the three can make, so prices rose and the queue is years long. Nobody knows how long this lasts. That question, not this year's profit, is what moves the share price."),
    ("md", """
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
"""),
    ("chart", "stack", "GE Vernova gas order book: firm backlog and slot reservations (GW)", "GE Vernova earnings releases, Q3 2025 to Q2 2026 [R6] [R7] [R8]. Reservations converted into orders: 7, 8, 6 and 10 GW in the last four quarters"),
]))

S.append(("5. Thesis part one: the forecast in gigawatts", [
    ("note", "**The idea.** Turbine revenue is two numbers multiplied: how many gigawatts ship, and the price per kilowatt. One gigawatt is one million kilowatts, about the output of one large power plant. So we can ask of the analysts' forecast: is the price settled, is the demand settled, is the output settled?"),
    ("md", """
Power equipment revenue = gigawatts shipped x dollars per kW.

| Question | What analysts' figures need | What GE Vernova has | Settled? |
|---|---|---|---|
| Price | $579 per kW in 2027, $662 in 2028 | $741 per kW in signed backlog; $513 realised in H1 2026 | 2027 yes. 2028 needs backlog prices to keep rising, as they have for four quarters |
| Demand | Buyers for 111 GW of planned output, H2 2026 to 2030 | 53 GW firm + 63 GW of paid reservations = 116 GW | Firm orders cover 48%; reservations the rest, and 7, 8, 6 and 10 GW of them converted in the last four quarters |
| Output | 20 GW a year from Q3 2026 | 14.6 GW in the last four quarters | No |
"""),
    ("chart", "qship", "Gas turbine gigawatts shipped each quarter, and the plan", "10-K FY2025, 10-Q Q1 and Q2 2026 [R1] [R3] [R4]; plan from the Q2 2026 call [R9]. Hollow bars are the plan"),
    ("note", "**The open item.** The company must go from about 3.7 GW a quarter to 5. That is a 37% step. It shipped 5.2 GW once before, in Q2 2025. The first reading comes on 28 October."),
    ("md", """
### The numbers behind the table

- **Price analysts need** = their Power equipment revenue divided by gigawatts on the company's path (17.5, 21, 24 and 26 GW for 2026 to 2029): $534, $579, $662, $741. The 21 GW for 2027 and 26 GW for 2029 are readings of the plan, not figures the company gave. [R12] [R9]
- **Signed price** = $39,261M of Power equipment backlog divided by 53 GW = $741 per kW. It includes non-gas equipment and moves with the product mix. [R3] [R6]
- **The signed price has risen four quarters running:** $556 (June 2025), $575, $618, $648, $741 per kW (June 2026), from each filing's Power equipment backlog and the firm gigawatts in the releases. [R1] [R3] [R4] [R5] [R11]
- **Realised price lags the backlog average.** Over five yearly windows, revenue per kW shipped was 78% to 94% of the backlog price at the start of the window (average 87%). On $741 that is $578 to $697, average $645. 2027 ($579) is covered at the average. 2028 ($662) needs the backlog price near $760 per kW by December 2027; new orders are entering at about $900 per kW (an inference), so that is likely but not settled. A 2028 shortfall of 7% to 11% would cost 2% to 14% of 2028 EBITDA, depending on whether it is mix or price. Found by the second-opinion check.
- **Planned output**, H2 2026 to 2030 = 10 + 21 + 24 + 26 + 30 = 111 GW. Some firm orders deliver in 2031. [R9]
- **Shipped by quarter:** 3.0, 5.2, 4.0, 3.1 (2025), then 4.2 and 3.3 (2026). [R1] [R3] [R4]
"""),
    ("chart", "kw", "Power equipment revenue per kW: reported, and what analysts' figures imply", "Filings [R1] [R3]; Bloomberg consensus, 2026-10-01 [R12]; dashed line is the signed backlog price"),
    ("note", "**HA turbines** are the largest and newest class. The Sell note of 14 September said 2027 deliveries were ordered in 2024 at old prices. The unit count in the filings says otherwise for this class."),
    ("md", """
### What ships next

- 70 HA turbines were in backlog at 30 June 2026. The roll: 32 at the end of 2024, plus 43 ordered, less 24 sold in 2025 = 51; plus 27 ordered, less 8 sold in H1 2026 = 70. [R1] [R2] [R3]
- Between 62 and 70 of the 70 were ordered in 2025 or later. If the oldest ship first it is all 70. Without that assumption the floor is 62. [R1] [R3]
- **Near-term check.** The 10-Q says 36% of the $87,821M equipment backlog is due within a year: $31,616M. Analysts have $30,245M of equipment revenue for the same four quarters. The schedule is 4.5% higher before any new order. In seven past windows the actual figure beat the schedule six times. The profit effect is small, about $0.2B. [R3] [R11] [R12]
"""),
    ("chart", "bt", "Backlog schedule back-test: actual equipment revenue divided by the scheduled amount (1.00 = schedule met)", "10-K and 10-Q filings, seven windows opening December 2023 to June 2025 [R1] [R2] [R11]"),
    ("chart", "margin", "Power EBITDA margin: reported, then analysts (%)", "Filings [R1] [R3]; Bloomberg segment consensus, 2026-10-01 [R12]; dashed line is the company's 2028 target of 22% [R7]"),
    ("md", """
**What these numbers support.** Analysts' forecast assumes the company's own output plan at prices already signed. It needs no new orders and no new price rises.

**What they do not support.** Any claim that analysts are too low by a stated percent. Three attempts at that failed their error tests (section 9, rows 5 to 8).
"""),
]))

S.append(("6. Thesis part two: why the factory is the limit", [
    ("note", "**The physics.** The first row of blades sits in gas hotter than the melting point of the blade's own metal. Each blade is grown as a single crystal of nickel alloy, with cooling channels inside and a ceramic coat outside. Few foundries can make them, and the same foundries make jet-engine blades."),
    ("md", """
- Four Western foundries make these blades at scale: Precision Castparts, Howmet, CPP and Doncasters. [R18] [R27]
- **From the company, 22 July 2026:** output moves from about 3 GW a quarter to 5 from the third quarter and is "very well on track"; 325 new machines are installed and about 400 will be by year end; workers were hired and trained a year ahead; the step to 24 GW in 2028 depends on castings and forgings arriving in 2027; a new HA unit reaches its first major service four years after start. [R9]
- **From the blade maker.** Howmet's gas turbine revenue was $321M in Q2 2026 against $233M a year earlier (+38%), and $605M in H1 2026 against $437M (+38%), from its 10-Q; $944M in FY2025 from its 10-K. The whole company grew 24%. [R41] Its chief executive: "Demand in the gas turbines market is extraordinary with customers already revisiting and adding to their demand outlooks." [R28]
- On its call Howmet claimed a share "in excess of 50% globally for turbine blades" and described a new plant in Japan, an expansion in Europe and more equipment in Virginia, with more capacity "in '27, but with another major step into '28 and '29". Secondary source. [R29]
- **Supplier timing, from their filings.** Howmet's main capacity additions land in 2028 and 2029, and a new commitment takes about 24 months. Carpenter's new melt capacity is commissioned about mid-2027. ATI says it is prioritising aerospace. Woodward sold its heavy-duty combustion parts line in FY2025. Nothing contradicts the 2027 output plan; the 2028 step to 24 GW carries timing risk. No supplier states capacity in gigawatts or units. [R41]
- GE Aerospace, a separate company, agreed in September 2026 to buy CPP for $11.75B. SpaceX is building its own blade foundry. News reports. [R20] [R21]
- Units sold: heavy-duty turbines 54 in 2025, 15 in Q1 2026, 13 in Q2 2026. HA units 24 in 2025, then 5 and 3. [R1] [R3] [R4]
"""),
    ("chart", "howmet", "Howmet revenue growth, year on year, by quarter (%)", "Bloomberg, 2026-10-02 [R13]; gas turbine line from Howmet's Q2 2026 release [R28]"),
    ("note", "**Two edges to this.** The limit helps the next 12 months: the capacity is already installed and all three makers face the same shortage, so prices hold. It also means orders must slow once the factories are sold out. That is a reason for a lower multiple, and it is why the base case uses 25x and not today's 29.6x."),
    ("md", """
**Reading.** The factory limit supports the next year of earnings and protects price. It caps upside in volume, and "sold out" means order growth must slow.
"""),
]))
