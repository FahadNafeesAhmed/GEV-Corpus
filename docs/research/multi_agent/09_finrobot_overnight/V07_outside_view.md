# Variation: outside view / base rates first

_V07_outside_view — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 01:45:40. Requests 34, input tokens 1539724, output tokens 29672._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova (GEV): outside-view base rates, then GEV-specific adjustments — direction over 3–12 months from $962.49 (2026-09-29 close)

*Research input only. Every probability here is a research judgement. Every forecast is a research estimate, and the team chooses its own number.*

**Source key**
- **10Q** = 10-Q 0001996810-26-000148 (2026-07-22)
- **PR2Q** = 8-K 0001996810-26-000147, Q2'26 press release
- **PR4Q** = 8-K 0001996810-26-000012, Q4'25 press release with the 2028 framework
- **10K25** = 10-K 0001996810-26-000015
- **MS** = MarketScreener consensus fetched 2026-09-29 (facts.csv CT-02)
- **SA** = stockanalysis.com consensus (market_briefing_0923.md)
- **FACTS-xx** = rows of the prior verified fact table
- **D01 / D04** = tonight's FY27 build and January-guide outputs. I did not read any V0x outputs.

---

## 1. Bottom line

- **The outside view on its own leans slightly long, not short.** Two effects pull against each other:
  - Expensive stocks do badly over 5 years.
  - But for expensive stocks that have been rising (winners), the value signal is weakest and momentum is strongest over the next 6–12 months [S1: Asness, "The Interaction of Value and Momentum Strategies", FAJ 1997, AQR PDF p.1] [S2: Siegel/Schwartz via WisdomTree, 2023-08-31: the "highest multiple stocks often see momentum enabling them to outperform for the following year"].
  - GEV fits that profile: up about 50% over 12 months and down about 14% in the month before 2026-09-20 [S1: Yahoo Finance 2026-09-20] [S2: 52-week range $530.16–$1,195.94, master brief §2; the price sits 82% above the low, computed].
- **Sell-side forecasts two or more years out are biased upward.** McKinsey found analysts forecast 10–12% a year of profit growth against 6% actual [S1: McKinsey, "Equity analysts: Still too bullish", 2010-04] [S2: City AM, 2010-04-25]. This base rate supports the claim that Street FY27–28 runs ahead of management.
- **GEV-specific evidence moves the ~52% outside-view prior to p_long ≈ 0.47.** That is a coin flip leaning slightly short, and weaker than the brief's 55–60% short lean.
  - The biggest negative is Street FY28 EBITDA $13,064M against management's $11,200M framework (+16.6%) [S1: MS] [S2: PR4Q].
  - The biggest positive is a record of never cutting, with organic framework raises at events. The spring-2027 Capital Markets Day (CMD) falls inside the horizon [S1: FACTS BR-28] [S2: Dec-2024 and Dec-2025 investor-update PDFs].
- **The gas-turbine bust analogs (2001–03, 2017–18) do not fit a 3–12-month short.** In both, earnings or guidance broke after demand or orders turned.
  - In 2002, GE Power Systems' earnings rose 29% while US orders were forecast to fall 80% or more [S1: GE 10-K 2003, ex13 MD&A] [S2: GE Power Systems release, 2002-07-23].
  - GEV shows no sign of orders turning. The CEO said 2032 slots are selling [S1: FACTS GLJ-35, Laguna transcript] [S2: MarketBeat 2026-09-18, corpus src:681].
- **Research estimate of the gap:** FY27 adjusted EBITDA about $8.9B (range $8.0–9.7B) vs consensus $9,574M, i.e. −7% or about −1.3 margin points (16.9% vs 18.15%) [computed; D01 base $8.7B; D04 straight-line 16.5–16.9%].
  - On today's EV the gap is worth about −7%. The +39% forward roll of next-twelve-month (NTM) EBITDA means a 12-month short also needs the multiple to fall below about 23x on this path (computed, §4).
- **Correction to the brief:** Ken Parks, not the new CFO, presents the January 2027 call [S1: GEV release 2026-08-27] [S2: MarketScreener 2026-08-28]. That weakens the "new CFO resets the bar" angle.

---

## 2. Ladder R1–R14

### Outside view first: reference classes and the prior

| Reference class | Base rate / finding | Sources | Applies to GEV? |
|---|---|---|---|
| Expensive stocks (high P/S), 12 months | 46% of all large stocks beat the S&P over the next 12 months; about 25% in the high-multiple buckets. Top-P/S stocks returned about −2%/yr over 5 years vs +10% for the market | WisdomTree/Siegel 2023-08-31. **[SINGLE-SOURCE]** — the underlying book (*Stocks for the Long Run*, 6th ed.) has the same authors | Weakly. GEV's P/S is about 5.5x FY26 (computed), far below the >25x/>40x buckets. The P/E premium, not P/S, is the relevant trait |
| Value × momentum interaction | Value is "quite weak among winner stocks"; momentum "is particularly strong among expensive stocks" | Asness FAJ 1997; Jegadeesh-Titman 1993 as cited there; Siegel/Schwartz on top-multiple stocks' next year | Yes. GEV is an expensive winner (+~50% over 12 months). This cuts against a 12-month short |
| Analyst forecast bias | Forecast growth of 10–12%/yr vs 6% actual (1985–2009) | McKinsey 2010; McKinsey 2001 "Prophets and profits" (same publisher); City AM 2010 | Yes. Supports "Street FY27–28 too high". Aggregate data, not stock-specific |
| Order/shipment ratio | A high new-orders-to-shipments ratio forecasts lower equity returns from 1 month to 1 year | Jones & Tuzel, RFS 2013. **[SINGLE-SOURCE]** | Aggregate market signal only. GEV's book-to-bill is above 1 |
| GE gas-turbine boom and bust, 1998–2003 | US orders ×10 in 1998; demand peaked in 2002; GE Power Systems earnings +29% in 2002, then fell in 2003; 46 GW cancelled Nov-2001 to Aug-2002 | GE 10-K 2003 ex13; GE 2002-07-23 release; Power Engineering 2002-09; PEi 2002 | Mechanism: earnings lag orders by 1–2 years. Needs an order turn, which is not visible now |
| GE Power, 2017–18 | A bullish guide in March 2017 despite flat demand; Power profit −45% in 2017; shares −50% or more from the March forecast | Reuters 2018-02-23; GE Integrated Summary Report 2017; POWER magazine 2018-02-28 | A guide that ignored weak demand. GEV's pattern is the opposite (conservative margin guides, cash beats) |
| Capex-boom supplier (Vestas, 2008) | Shares down more than 90% from 2008 by 2016 on overcapacity | PRX 2016-07-31; Institutional Investor ("almost went to zero") | Multi-year horizon. Relevant to GLJ's capacity claim, not to 3–12 months |

**Prior (research judgement):** P(long works over 12 months, absolute) ≈ **0.52**.
- Valuation base rates push below 0.5.
- The momentum interaction plus positive equity drift push back above.

### GEV-specific adjustments

| Evidence | Move | Why |
|---|---|---|
| Street FY28 +16.6% above the framework; the CEO dates the equipment-margin step to '29–'30 | −6 pts | Primary, recent, specific |
| January guide ~4 months out: straight-line margin 16.5–16.9% vs consensus 18.15% | −3 | The historical reaction to first guides was shallow and 4 of 4 positive (D04), so the net effect is smaller |
| Never cut; two organic framework raises; spring-2027 CMD with a 2030 outlook | +4 | Framework days: +5.01% and +15.62% (FACTS BR-38) |
| Orders still rising (2032 slots; backlog about $200B "very early" 2027) | +2 | The bust analogs need an order turn |
| NTM roll-forward +39% | +2 | A short needs a de-rating on top of an estimate cut |
| Macro: 10-year about 5%, Fed-hike odds, AI-trade sector beta | −2 | Raises variance for a ~2x-market multiple |
| Cash quality: FY27 consensus FCF −38%; operating cash flow ex-deposits negative | −2 | A narrative risk once the deposit inflow fades |
| **Net** | **≈ 0.47** | |

### R1. What does $962.49 require?

**Financially**
- Market cap $256.3B; EV about $247.2B [computed: 266.33M shares (10Q cover) × $962.49; net cash $9,113M (10Q balance sheet; FACTS)].
- 25.8x FY27 consensus EBITDA and 38.7x FY27 EPS, against an S&P forward P/E of 19.1 (FactSet via Zaccardi 2026-09-12 and TheTradersSpread 2026-09-13; the brief says 19.2). That is about 2.0x the market.

**To hold the price 12 months out**
- NTM EV/EBITDA of **20.3x** on consensus NTM EBITDA of $12,191M.
- **22.9x** on management's plan path ($10,794M NTM).

**To justify today's EV at end-2028**
- The framework's $11.2B needs a 25.4–28.3x exit multiple.
- Consensus's $13,064M needs 21.8–24.3x [FACTS RV-22, discount rate 9–11%].

**Physically**
- The 2028 plan is revenue $56B at a 20% margin, Power 22% and Electrification 22% [PR4Q; FACTS RV-15].
- Gas output: 20 GW/yr run-rate from Q3'26 and 24 GW in 2028 [Q2'26 call; Laguna, FACTS PP-22].
- About 30 GW shipped over Q3'26–Q4'27 [D01, citing CALL-2Q26 and LAGUNA].

### R2. Consensus vs management's plan

| | Consensus | Management |
|---|---|---|
| FY27 revenue | $52,740M | No FY27 guide |
| FY27 adj EBITDA | $9,574M (18.15%) | No FY27 guide |
| FY28 revenue | $60,500M | $56B |
| FY28 adj EBITDA | $13,064M (21.6%) | $11,200M (20%) |

- Consensus is from [MS] [SA] (revenue matches to 0.004%, so the two may share one feed). The FY27 EBITDA figure is corroborated at $9.45B in GLJ's note (FACTS GLJ-04).
- FY28 consensus is +8.0% on revenue, +1.6 margin points and +16.6% on EBITDA vs the plan [FACTS BR-30].
- FY27 at 18.15% needs +5.15 points in one year from the FY26 guide midpoint of 13%. GEV's largest step so far is +4.6 points [D04, computed from the 8-K guides].

### R3. Delivered vs first guides since the spin

| | FY24 | FY25 |
|---|---|---|
| Revenue vs first guide | +1.3% | +4.3% |
| Adj EBITDA margin actual vs guide midpoint | 5.83% vs 6.0% | 8.40% vs 8.5% |
| FCF vs first guide | $1,701M vs $900M (+89%) | $3,710M vs $2,250M (+65%) |

- Sources: [FACTS BR-21/23; 10K25 and 10-K 0001996810-25-000011].
- Guidance has never been cut. On raise days the stock closed lower 2 times out of 7 [FACTS BR-38].
- 2025 bonus targets were beaten on FCF (200% payout) and EBITDA (130%) [DEF 14A 0001996810-26-000049 via D02; target levels are single-source].
- **The record is revenue and cash beats, not margin beats.**

### R4. Where the evidence most differs from consensus

- **FY27 adj EBITDA: research estimate $8.9B vs $9,574M (−7%, 16.9% vs 18.15% margin on consensus revenue).**
  - D01's bottom-up base is $8.7B (band $7.7–9.6B).
  - D04's straight line is 16.5–16.9%.
  - GLJ's $7.42B plus the maximum vintage fix gives about $8.0B (the low case).
- **FY28:** research base about $11.6B. That sits between the plan ($11.2B) and consensus ($13.06B), giving partial credit for GEV's record of raising the framework.
- The team chooses its own numbers.

### R5. Why the market might not already see it

- **It is interpretation and timing, not new information.** GEV publishes margin-in-backlog every January, and the CEO said at Laguna on 2026-09-16 that the 2026 backlog-margin change "tells you the equipment margins for '29 and '30, largely" [S1: GEV Laguna transcript] [S2: FACTS VF-02].
- A plausible reason the Street is ahead: it extrapolates the Power margin trend (+2.6, +2.2 and ~+3.3 points a year) and management's habit of raising the framework [D01].
- Because the edge is interpretive, it is thin.

### R6. Strongest long argument

- **Operating leverage in Power:** incremental margin of 44.4% from H1'25 to H1'26; Q2'26 Power margin 18.82% [S1: 10Q MD&A] [S2: Q2'26 call, corpus src:3161].
- **Pricing and capacity:** SRAs carry ">20%" pricing strength; Siemens Energy is "sold-out until FY28" [D02: SE deck, corpus src:3179; trade press, corpus src:1699].
- **Raise record and in-horizon catalysts:** a spring CMD with a 2030 outlook, and backlog of about $200B "very early" in 2027 [Yahoo 2026-09-20; Laguna via MarketBeat].
- **Base rate:** momentum among expensive winners (Asness 1997).

### R7. Strongest short argument

- The Street's FY27–28 margins sit ahead of management's own 2028 plan (+16.6% on FY28) and ahead of the CEO's '29–'30 timing [MS; PR4Q; Laguna].
- GEV has never beaten a first margin guide [FACTS BR-23].
- H2'26 consensus implies a 16.3% margin vs a 15.0% guide midpoint (master brief §4).
- FY27 consensus FCF is $7.42B, down 38% (MS only, **[SINGLE-SOURCE]**).
- The analyst-optimism base rate (McKinsey) supports all of the above.

### R8. Which side's evidence is stronger?

**Roughly equal, and both are primary.**
- The short's central comparison rests on single-vendor EBITDA consensus (MarketScreener). No second EBITDA vendor was found (D02), which weakens it.
- The long's best facts are audited 10-Q margins and order data, which are strong, but they describe the past.
- The short's timing evidence (the CEO's own words) is the most recent primary item on either side.

### R9. Dated reveal and pass mark

- **Event:** the Q4'26 call in late January 2027, with the FY27 outlook. The exact date is not yet set; the prior year's was 2026-01-28.
- **Pass mark for the short:** FY27 adj EBITDA margin midpoint below about 17.5%, or guided EBITDA dollars below about $9.2B (computed: 17.5% × $52.74B).
- **Kill level:** a margin midpoint at or above 18% (for example an 18–19% range).
- **Research-judgement odds (D04):** P(midpoint < 18.15%) ≈ 85%; P(≤ 17.5%) ≈ 66%.
- **Expected reaction if it lands ≥0.5 point below consensus:** −4% to −11%, with a high chance of partial reversal inside a week [D04; FACTS BR-38].
- **Second event:** the spring-2027 CMD (date not set).

### R10. If wrong, how much and how fast?

- **For a short:**
  - Back to the 52-week high of $1,195.94 = +24.3%.
  - Consensus target $1,237 = +28.6% [SA].
  - A single framework day has delivered +15.62% [FACTS BR-38].
- **For a long:** five closing drawdowns of 15% or more since the spin (median −24.6%), about two a year (master brief §6; corpus price table).

### R11. What the market would pay a year from now (Sep-2027)

Formula: (multiple × NTM EBITDA + $9,113M) / 266.33M shares. NTM EBITDA = 0.25 × FY27 + 0.75 × FY28.

| Path | NTM EBITDA | 20x | 23x | 25x |
|---|---|---|---|---|
| Consensus | $12,191M | $950 | $1,087 | $1,179 |
| Research base | $10,925M | $855 | $978 | $1,060 |
| Low (GLJ-ish) | $9,875M | $776 | $887 | $961 |

- The table ignores FY27 FCF (about +$28/share if kept as cash) and buybacks.

### R12. Best-fitting analog

- **For the mechanism: GE Power Systems, 2001–02.**
  - Earnings kept rising for about a year after orders turned.
  - Cancellations even added income at first: a $70M after-tax benefit from terminated orders in Q2'02 [GE Q2'02 earnings release; **SINGLE-SOURCE**].
  - The signal to watch was orders and cancellations, not earnings. For GEV that means SRA-to-firm conversion (SRAs are 54% of the gas pipeline).
- **2017:** says guidance breaks when it is set against flat demand. GEV today is the reverse.
- **Conclusion:** neither analog supports a cycle-bust short inside 12 months. They support a timing-of-estimates short at most.

### R13. Single observation that flips the view

- A FY27 margin guide midpoint at or above 18%.
- Or a raise of the 2028 framework to about 21.5%+ or about $13B at the CMD.
- In the other direction: a sequential decline in SRA-plus-firm GW, or SRA cancellations, would strengthen the short a lot.

### R14. Confidence

- **Low: 2/5.** p_long is 0.47.
- The largest uncertainty is the multiple, not the estimates. A −7% estimate gap is smaller than one typical earnings-day move (mean absolute 5.42%, range −8.69% to +14.58%; D04).
- Second uncertainty: whether management raises at the CMD.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf |
|---|---|---|---|---|---|---|
| 1 | Price | $962.49 | yfinance quote 2026-09-30 | master brief §2 | exact | H |
| 2 | 12-month momentum | ~+50%; −14% over 1 month | Yahoo 2026-09-20 | 52-week range, brief §2 (computed +82% off the low) | close | M |
| 3 | S&P forward P/E | 19.1 | FactSet via Zaccardi 2026-09-12 | TheTradersSpread 2026-09-13 | exact (brief 19.2) | M |
| 4 | FY27 consensus EBITDA | $9,574M | MS | GLJ-cited $9.45B (FACTS GLJ-04) | close | M |
| 5 | 2028 framework | $56B / 20% | PR4Q | FACTS RV-15 / Dec-25 PDF | exact | H |
| 6 | FY28 consensus vs plan | +16.6% | MS | PR4Q (computed) | computed | M |
| 7 | CEO dates the margin step to '29–'30 | quote | Laguna transcript 2026-09-16 | FACTS VF-02 / MarketBeat | exact | H |
| 8 | Parks presents the Jan call | through Q4 calls | GEV release 2026-08-27 | MarketScreener 2026-08-28 | exact | H |
| 9 | RPO | $176.3B | 10Q / Q2 deck (corpus 5726) | corpus src:234 | exact; **Yahoo's "$167B" conflicts (wrong)** | H |
| 10 | Value weak / momentum strong among expensive winners | qualitative | Asness FAJ 1997 | WisdomTree/Siegel 2023 | close | M |
| 11 | High-multiple 12-month odds of beating the market | ~25% vs 46% | WisdomTree 2023 | — **[SINGLE-SOURCE]** | — | L |
| 12 | Analyst optimism | 10–12% forecast vs 6% actual | McKinsey 2010 | City AM 2010 (repeats McKinsey) | exact | M |
| 13 | GE power bubble peaked 2002; Power Systems earnings +29% in 2002 | | GE 10-K 2003 ex13 | GE 2004 dex99b (same issuer) | exact | M |
| 14 | US gas-turbine orders to fall ≥80% | July 2002 | GE PS release 2002-07-23 | Power Eng. 2002-09 (46 GW cancelled) | close | M |
| 15 | GE Power 2017 profit | −45% | GE ISR 2017 | Reuters 2018-02-23 | exact (Reuters May-2018 says −53%, a different measure) | H |
| 16 | Vestas decline | >90% from 2008 | PRX 2016 | Institutional Investor | close | M |
| 17 | First-guide margin record | FY24 5.83% vs 6.0%; FY25 8.40% vs 8.5% | FACTS BR-23 | 10K25 | exact | H |
| 18 | Raise-day reactions | 2 of 7 negative | FACTS BR-38 (corpus prices) | Yahoo closes | exact | M |

---

## 4. Arithmetic

**Valuation today**
- Market cap: 266.33M × 962.49 = $256,340M.
- EV: 256,340 − 9,113 = $247,227M, where net cash = 13,120 − 2,849 − 1,158.
- P/E FY27: 962.49 / 24.85 = 38.7x; vs the market: 38.7 / 19.1 = 2.03x.
- NTM EPS: 0.25 × 15.21 + 0.75 × 24.85 = $22.44, giving 42.9x.

**Growth and margin**
- EPS growth: FY27 24.85 / 15.21 = +63%; FY28 34.22 / 24.85 = +38%.
- Consensus FY27 margin: 9,574 / 52,740 = 18.15%.
- Research base margin: 8,900 / 52,740 = 16.9%, i.e. −$674M (−7.0%).
- FY28 consensus vs plan: 13,064 / 11,200 = 1.166.

**Break-even multiples (hold $962 in 12 months)**
- Consensus path: 247,227 / 12,191 = 20.3x.
- Management path: 247,227 / 10,794 = 22.9x.

**NTM EBITDA paths (Sep-2027)**
- Research base: 0.25 × 8,900 + 0.75 × 11,600 = $10,925M.
- Low: 0.25 × 8,000 + 0.75 × 10,500 = $9,875M.

**Price targets**
- 25x × 8,900 = 222,500; plus 9,113 = 231,613; / 266.33 = **$870**.
- Range: 24x → $836; 27x → $937.

**Other**
- P/S: 256,340 / 46,282 = 5.5x.
- Drawdown frequency: 5 in about 2.5 years ≈ 2 a year.
- FY27 FCF per share: 7,417 / 266.33 = $27.85.

---

## 5. General question bank (answered along the way)

- **G1:** see R1.
- **G5:** if the stock goes nowhere for 12 months, the multiple falls to about 20x (consensus path) or 23x (management path) NTM, from 28.2x today.
- **G7:** the gap is interpretation and timing, not information.
- **G8:** the −7% estimate gap is smaller than one earnings-day range, so it is marginal after the multiple.
- **G14:** a CMD date after April, or no FY27 margin guide at all, would push the reveal out.
- **G16:** rates. The 10-year closed at 4.96% on 2026-09-11, its 2026 high (TheTradersSpread, **SINGLE-SOURCE**; the brief says 5%). The GLJ-day sector move shows high beta to rates.
- **G19:** see R12.
- **G20:** EBITDA consensus is single-vendor; FCF consensus is single-source.

---

## 6. What would change this

- **Estimate-gap finding:** a FY27 guide ≥18%, or consensus drifting down toward $9.0B before January (which would remove the gap).
- **Analog finding:** SRA cancellations or a sequential fall in gas GW, which would make the 2001–02 analog live.
- **Momentum base rate:** a break below the 52-week trend (for example under the $874.85 close on the GLJ day) would remove the momentum support.

---

## 7. Disagreements with the master brief

1. Parks, not McDonough, presents the January FY27 outlook [GEV release 2026-08-27; MarketScreener 2026-08-28].
2. The outside view does not support the brief's 55–60% short lean. The research estimate is about 53% short (p_long 0.47).
3. The S&P forward P/E is 19.1 (FactSet 2026-09-12), not 19.2. Immaterial.

---

## 8. Open items

- A second consensus EBITDA vendor (Visible Alpha / FactSet via the terminal).
- An exact GEV 12-month price return from an exchange price series (it rests on Yahoo commentary here).
- P/E-decile 12-month base rates for S&P 500 stocks (the Ken French or Siegel datasets).
- The date of the January call and the CMD (GEV IR events page).
- GE's 2001–02 share-price path against its Power Systems orders (GE 10-K 2001/2002 segment orders tables).

---

```FINAL_BLOCK
{"direction": "short",
 "p_long": 0.47,
 "fy27_adj_ebitda_usd_m": {"low": 8000, "base": 8900, "high": 9700},
 "fy28_adj_ebitda_usd_m_base": 11600,
 "one_number": "FY27 adjusted EBITDA ~$8.9B vs MarketScreener consensus $9,574M: -7%, 16.9% vs 18.15% margin on consensus revenue",
 "target_price_range_usd": [836, 937],
 "target_formula": "24-27x (base 25x) x FY27 adj EBITDA $8,900M + net cash $9,113M, / 266.33M shares = $836-$937 (base $870)",
 "horizon_months": 5,
 "kill_rule": "FY27 adj EBITDA margin guide midpoint >=18% (or guided EBITDA >=$9.4B) on the late-January 2027 Q4'26 call, or 2028 framework raised to >=$13B at the spring-2027 CMD",
 "top_reason": "Street FY27-28 EBITDA runs ahead of management's own 2028 plan (+16.6%) and the CEO's '29-'30 margin timing, but momentum among expensive winners and GEV's raise record make this close to a coin flip",
 "confidence_1_to_5": 2}
```
