# Variation: neutral framing (B — identical prompt, noise check)

_V02_neutral_B — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 01:18:27. Requests 17, input tokens 822087, output tokens 15590._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova (GEV): long or short over 3–12 months from $962.49 (research as of 2026-09-30)

*This is research input only. Every range is a research estimate, and the team chooses its own numbers.*

**Source key**
- **10K-25** = 10-K 0001996810-26-000015
- **10Q-2Q26** = 10-Q 0001996810-26-000148
- **REL-2Q26** = 8-K -26-000147 press release (Q2'26 results)
- **REL-4Q25** = 8-K -26-000012 press release (Q4'25 results)
- **DEC25** = December 2025 investor-update release (corpus src:2648/2711)
- **CALL-2Q26** / **CALL-4Q25** = earnings-call transcripts (corpus src:3161 and src:2660)
- **LAGUNA** = GEV-hosted Morgan Stanley Laguna transcript PDF, 2026-09-16
- **MB-LAG** = MarketBeat write-up of Laguna, 2026-09-18 (corpus src:681)
- **MS** = MarketScreener consensus, fetched 2026-09-29
- **FS** = FactSet surveys via cnyes (facts CT-10/11/16)
- **GLJ** = Yahoo and Investing.com write-ups of the GLJ note, 2026-09-14 (facts GLJ-01/04)
- **YF** = yfinance quote, 2026-09-30 (last price still $962.49, i.e. the 9/29 close)
- **D01–D04** = earlier outputs tonight, each carrying its own primary citations

## 1. Bottom line

- **Direction: a slight long lean, p_long ≈ 0.55, low confidence. The brief's modest short lean (55–60%) does not survive when the horizon runs the full 12 months.** The short needs both an estimate cut and a de-rating to about 20–23x NTM EV/EBITDA, against 28.2x today (facts VF-08, computed from MS and the 10Q-2Q26 bridge). The evidence supports only the first of those, and only weakly.
- **Where I differ from consensus is FY27 adjusted EBITDA: base ~$8.8B, about −8% vs MS $9,574M** (GLJ puts the Street at $9,450M, which is close).
  - A straight line from the FY26 guide to management's own 2028 plan gives FY27 of $8.2–8.8B [REL-2Q26; REL-4Q25; D03 §1].
  - Consensus needs Power at about 21.7–23.5% in 2027, roughly its 2028 target of 22% a year early [D01 Q11; REL-4Q25 / DEC25].
- **That gap is small next to the 12-month roll-forward.** On management's 2028 plan ($11.2B), with FY27 at my $8.8B base, Sep-2027 NTM EBITDA is about $10.8B. At 23x that is roughly today's price; at 25x, about $1,047 [computed; REL-4Q25; MS].
- **The short's dated catalyst is weaker than the brief assumes.**
  - Ken Parks remains CFO "inclusive of the third and fourth quarter earnings calls", so he is on the January call and McDonough is not presenting her own first guide [GEV release 2026-08-27; CFO Dive 2026-08-28; via D04].
  - GEV's past guide and framework days rose 4 of 4 [D04; facts BR-38].
  - The one analogous sell-off (Q2'26, −8.69%) partly reversed the next day (+4.69%) [D04; facts BR-38].
- **The long's best evidence is capacity scarcity plus pricing through FY28.**
  - GEV sold 2032 slots and added 12 GW of 2030–31 capacity "at premium pricing", with all 12 GW "in some stage of contracting" [MB-LAG; LAGUNA].
  - Siemens Energy is "sold-out until FY28" [SE CFO deck, corpus src:3179; src:1699].
- **The real risk to a long is the multiple, not the earnings.** GEV has had five closing drawdowns of 15% or more since the spin, median −24.6% [facts BX-03..08; Yahoo and Nasdaq closes agree]. It trades as an AI-capex proxy (DeepSeek day −21.5%) [D03; Motley Fool 2026-09-14].

## 2. The ladder, R1–R14

**R1. What the price requires**
- EV is about $247.2B: 256,343 market cap + 2,849 borrowings + 1,158 NCI − 13,120 cash [10Q-2Q26 balance sheet; stockanalysis EV $247.34B cross-check, facts RV-*].
- That is 25.8x FY27 consensus EBITDA and 28.2x NTM ($8,755M) [MS; computed].
- **Financially:** holding today's 28.2x NTM through Sep-2027 needs NTM EBITDA to stay at about $8.8B. To earn +15% needs about $10.5B at 25x, or about $12.2B at ~22x.
- **Physically:** about 20–22 GW of gas shipments in 2027 [D01 Q1: CALL-2Q26 "at least 30 gigawatts" over Q3'26–Q4'27; LAGUNA cadence], rising to 24 GW in 2028 [REL-2Q26; CALL-2Q26].
- The price also needs Power margin to climb from 17.63% (H1'26) toward 22% [10Q-2Q26 segment note; REL-4Q25].
- Power equipment RPO per firm GW, a proxy for backlog price, is already $741/kW, up 29% in three quarters [facts RV-25: 10Q-2Q26 RPO table and REL-2Q26 GW].

**R2. Consensus vs management's plan**
- Consensus EBITDA: FY27 $9,574M (18.15%), FY28 $13,064M (21.59%) [MS; single EBITDA vendor. GLJ's "Street $9,450M" is the only near-independent check, −1.3%].
- Consensus revenue: FY27 $52,740M / FY28 $60,500M [MS], against FactSet $52,632M / $60,511M [FS]. These agree closely.
- Management's 2028 plan: $56B revenue at 20%, i.e. $11.2B [REL-4Q25, verified text: "revenue of $56 billion… adjusted EBITDA margin of 20%"; DEC25].
- Consensus FY28 is therefore +16.6% above the plan [computed].
- For FY27, consensus needs 74% of the 13%→20% margin path covered in a single year: +5.15 pts, against GEV's largest yearly step of +4.6 [D04; computed from REL-2Q26 and MS].

**R3. Delivery vs guidance since the spin**

| Line | Result vs guide | Sources |
|---|---|---|
| Revenue | +1.3% (FY24), +4.3% (FY25) vs the first numeric guide | facts BR-21; 10K-25 |
| Adj EBITDA margin | 5.83% vs 6.0% midpoint (FY24); 8.40% vs 8.5% (FY25), i.e. slightly below midpoint both years | facts BR-23; 10Q-2Q25 p.36; 10K-25 |
| FCF | +89% / +65% vs initial guide | facts BR-24; 10K-25; REL-4Q25 |

- Company-level guidance was never cut. Wind was cut at Q3'25 [8-K -25-000159; DEC25].
- The 2028 framework was raised twice, organically, at December events [facts BR-28; DEC25].
- Management beats the EBITDA bonus target: 2025 target $2.9B vs actual $3,196M, a 130% payout [DEF 14A -26-000049; 10K-25]. The target levels are single-sourced.

**R4. Where the evidence differs from consensus most clearly**
- **FY27 adjusted EBITDA: research base ~$8.8B vs $9,574M (−8%); band $7.9–9.6B** [D01 build; D03 straight line].
- The driver is Power's 2027 margin: evidence points to ~19.5–21% vs the ~21.7–23.5% consensus implies, and 1 point ≈ $275M [D01 Q11/Q13].
- FY28 is a bigger gap in percentage terms: base ~$11.5B vs $13,064M (−12%). But FY28 is outside the proof window.

**R5. Why the market may not already know**
- This is interpretation, not new information. GEV publishes margin-in-backlog every January, and analysts asked about it on CALL-4Q25 [CALL-4Q25; facts].
- The CEO's timing ("tells you the equipment margins for '29 and '30, largely") is public [LAGUNA p.10; MB-LAG].
- The market may simply be pricing FY28–30 and ignoring the FY27 step, which is itself a reason a FY27 miss may not move the stock much (G7).

**R6. The strongest long**
- The NTM roll-forward: +39% on consensus, about +24% on the plan path [computed].
- Supply is scarce through FY28 [src:3179; src:1699; MHI backlog 35 GW, Utility Dive src:1743 / MHI Q&A].
- Pricing is rising:
  - SRAs carry "another 10 to 20 points of pricing strength" [CALL-4Q25]; ">20%" [CALL-2Q26].
  - LG&E/KU all-in plant cost rose +53–57% [KY PSC 2025-00045; facts TP-05].
- The 2026 backlog-margin change is guided above 11 pts [LAGUNA p.5; facts PP-04]. That datapoint arrives in January alongside the FY27 guide.
- The spring-2027 CMD is set to give a 2030 outlook [MB-LAG; GuruFocus src:686]. The framework has been raised at each of the last two framework events.
- Electrification: organic revenue +29%, H1 margin 18.2%, equipment RPO +69% [10Q-2Q26; CALL-2Q26].
- The multiple sits near the 10th–25th percentile of its own post-spin range [Chartloom BX-15; GuruFocus src:686, a different measure].

**R7. The strongest short**
- Consensus FY27 is 9–17% above the straight-line plan path, and FY28 is 16.6% above the plan [computed from REL-2Q26, REL-4Q25, MS].
- GEV has never finished above its mid-year margin-guide midpoint [facts BR-23; 10Q-2Q25].
- FY26 consensus needs an H2 margin of 16.3% vs 15.0% at the guide midpoint [D03 §Q4; 10Q-2Q26].
- CSA profitability revisions are negative and getting worse: H1'26 −$218M vs FY25 −$151M [10Q-2Q26 Note 9; 10K-25 Note 9].
- Cash is deposit-driven: H1'26 contract-liability inflow $13.7B vs $1.9B a year earlier [10Q-2Q26 MD&A; 10Q-2Q25 MD&A]. FY27 FCF consensus is −38% [MS, single-source].
- The stock is an AI-sentiment proxy at about 2x the market P/E [MS EPS; S&P ~19.2x per brief].

**R8. Which side has better evidence**
- The short's estimate evidence is higher quality: primary filings and the CEO's own words, two-sourced.
- The short's price mechanism (de-rating to ≤20–23x) has no primary evidence. It rests on base rates (drawdowns) and sentiment.
- The long's evidence on the mechanism (roll-forward arithmetic, capacity, pricing) is also primary and recent.
- Net: the short wins on "the number is too high", and the long wins on "it may not matter within 12 months".

**R9. The dated test**

| Date | Event | Pass mark |
|---|---|---|
| 2026-10-28 | Q3'26 results | Q3 EBITDA vs the $1,535–1,716M guide-implied range; consensus is $1,706M [facts VF-10; MS] |
| Late Jan-2027 | FY27 guide + 2026 backlog-margin change | For the short: margin midpoint ≤17% (~$8.96B on $52.7B). For the long: ≥18% low end, or a backlog-margin change >11 pts [D04; LAGUNA p.5] |
| Spring 2027 | CMD with 2030 outlook | Any lift to the 2028 plan toward $13B |

- D04's research judgement: P(FY27 guide margin midpoint < 18.15%) ≈ 85%, and P(≤17%) ≈ 56%.

**R10. How much you can lose**
- Five drawdowns of 15% or more since the spin; median −24.6%, maximum −38.3% [facts BX-03..08; Yahoo and Nasdaq].
- Three of them happened while the S&P rose, which is a risk for a long.
- For a short, the risk is squeeze-type recoveries: 106% of the GLJ-day drop was recovered by 9/29 [facts; D04]. The +15.62% on the Dec-25 framework day is another example [facts BR-38; Proactive].
- Either way, about ±25% inside 3–6 months is the stock's normal range.

**R11. What the market would pay in Sep-2027**
- NTM on the plan path with my FY27 base = 0.25 × 8,800 + 0.75 × 11,200 = $10,600M. Value = (multiple × NTM + $9,113M) / 266.33M.

| Multiple | Plan path ($10,600M) | Plan path, brief's version ($10,794M) | Consensus ($12,191M) |
|---|---|---|---|
| 20x | $830 | $845 | $950 |
| 22x | — | — | $1,041 |
| 23x | $950 | $966 | — |
| 25x | $1,029 | $1,047 | $1,179 |

- The brief's $10,794M "management plan" figure blends consensus FY27 ($9,574M) with the plan FY28 (see §7).
- Net cash could grow by about $7.7B by Sep-2027 before buybacks and dividends: H2'26 FCF of $2,120M (= 12,017 − 9,897) plus 0.75 × $7,417M. That is roughly +$29/share [MS; 10Q-2Q26].

**R12. Historical analogs**
- **GE 2001–02:** orders collapsed before earnings did.
  - GE Power Systems forecast US gas-turbine orders and shipments to fall "80 percent or more over the next two years" [GE press release, 2002-07-23; Troy Record, 2002-07-24].
  - GE still booked a "$70 million after-tax benefit from terminations of Power Systems gas turbine orders" in Q2'02 [GE Q2'02 release, sec.gov 0000040545-02-000031]. Power World (2002-09) counted about 46 GW of projects cancelled.
  - Lesson: the P&L lags. The signal to watch is orders and SRA conversion, not EBITDA.
- **GE 2017–18:** a bullish forecast into flat demand was followed by GE Power profit −45% and shares −50%+ [Reuters, 2018-02-23]. Then came a $22.1B goodwill impairment [GE 10-K 2018; Reuters, 2018-10-30].
- Neither analog fits today inside the horizon. Demand indicators are still rising: 116 GW of backlog plus SRAs, and 2032 slots being sold [REL-2Q26; MB-LAG].
- The analogs point to a post-2028 risk, when supply roughly doubles [src:3179], not a 2027 one.

**R13. What would flip my view to short**
- A FY27 guide with an adjusted EBITDA midpoint below ~$8.3B *and* no reaffirmation of the 2028 plan.
- Or, equivalently for the long thesis: gas backlog plus SRAs falling below 116 GW, or H2'26 commitments well below H1's 40 GW. The CEO has already said H2 will be lower [LAGUNA p.3; single-source].

**R14. Confidence**
- 2 out of 5.
- The biggest uncertainty is the multiple path, since a de-rating from 28x to 23x erases the whole long.
- Next is the undisclosed split between services and equipment margins inside Power [10Q-2Q26: not disclosed].
- The FY27 EBITDA gap is small next to multiple swings: 1 turn of multiple ≈ $10.6B of EV, about $40/share.

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Confidence |
|---|---|---|---|---|---|---|
| 1 | 2028 plan | $56B / 20% / $11.2B | REL-4Q25 text | DEC25 + facts RV-15 | exact | H |
| 2 | FY26 guide | $45.5–46.5B, 12–14% | REL-2Q26 | CALL-2Q26 | exact | H |
| 3 | Consensus FY27 / FY28 EBITDA | $9,574M / $13,064M | MS | GLJ "Street $9,450M" (FY27 only) | close | M |
| 4 | Consensus revenue FY27 / FY28 | $52.7B / $60.5B | MS | FS | exact | H |
| 5 | CEO timing of margin step | "'29 and '30, largely" | LAGUNA p.10 | MB-LAG | close | H |
| 6 | Margin finished below guide midpoint twice | 5.83 vs 6.0; 8.40 vs 8.5 | 10Q-2Q25 p.36 | 10K-25 / Dec-24 release | exact | H |
| 7 | CSA revisions | H1'26 −$218M; FY25 −$151M | 10Q-2Q26 Note 9 | 10K-25 Note 9 | exact | H |
| 8 | Parks presents the Jan call | through Q4 call and 10-K | GEV release 2026-08-27 | CFO Dive 2026-08-28 | exact | H |
| 9 | Drawdowns | median −24.6%, max −38.3% | Yahoo | Nasdaq | exact | H |
| 10 | New 2030–31 capacity at premium pricing | 12 GW | LAGUNA | MB-LAG | exact | M |
| 11 | 2002 order collapse | −80% US gas-turbine orders | GE release 2002-07-23 | Troy Record 2002-07-24 | exact | H |
| 12 | 2017 GE Power profit | −45% | Reuters 2018-02-23 | GE 10-K 2018 (impairment) | close | M |
| 13 | FY27 FCF consensus | $7,417M | MS | — **[SINGLE-SOURCE]** | — | L |

## 4. Arithmetic
- **Straight-line FY27:** FY26 $5,980M (guide midpoint, 13% × $46.0B) or $6,359M (MS); FY28 $11,200M. The midpoints are $8,590M and $8,780M. D03's $8.2–8.8B band is not the plain midpoint: it follows from D03's own path assumptions.
- **Value per share** = (multiple × EBITDA + 9,113) / 266.33:
  - 25 × 10,600 = 265,000 → $1,029
  - 23 × 10,600 → $950
  - 20 × 10,600 → $830
  - 24 × 10,825 → $1,010
  - 22 × 10,825 → $928
  - 26 × 10,825 → $1,091
- **Brief's NTM check:** 0.25 × 9,574 + 0.75 × 11,200 = 10,794, which confirms it embeds consensus FY27.
- **Accrued cash:** 12,017 − 9,897 = 2,120; plus 0.75 × 7,417 = 5,563; total 7,683 / 266.33 = $28.8/share.

## 5. General question bank
- **G5 (if the stock goes nowhere):** at a constant price, the NTM multiple on the plan path falls from 28.2x to about 23x.
- **G7:** the gap is interpretation, not new information (R5).
- **G12:** deposits dominate cash flow [10Q-2Q26; 10Q-2Q25].
- **G14:** a December or CMD raise to the framework could land before the short's thesis plays out.
- **G19:** see R12.
- **G24:** recurring SBC of $257M (FY25) is not added back to adjusted EBITDA [10K-25 equity statement; facts RV-35].

## 6. What would change this
- **Against the long:** a FY27 guide midpoint ≤16%, or the stock breaking below its 2026-06-10 low of $867 on a sector de-rating (10-year at 5%).
- **For a stronger long:** a 2026 backlog-margin change well above 11 pts, or a framework lift at the CMD.

## 7. Disagreements with the master brief
1. **Who presents the January guide.** The FY27 guide will not be the new CFO's first print: Parks stays through the Q4 call [GEV release; CFO Dive]. That weakens the "new CFO reset" angle.
2. **The "management's plan" NTM of $10,794M.** It uses consensus FY27. With a plan-consistent FY27 it is about $10.6B, lowering each valuation row by about $18–30.
3. **The direction.** The brief's short lean judges value at a January frame (FY27 multiple). Over 12 months, the roll-forward and the history of positive guide days make the long slightly more likely. This rests on research judgement, not new data.

## 8. Open items
- A second EBITDA consensus vendor (Visible Alpha or LSEG).
- GLJ's full note.
- The margin split inside Power between services and equipment.
- Whether a December 2026 investor event will be held (check the GEV IR events page).
- Q3'26 buybacks: the 10-Q is due 2026-10-28.

```FINAL_BLOCK
{"direction": "long",
 "p_long": 0.55,
 "fy27_adj_ebitda_usd_m": {"low": 7900, "base": 8800, "high": 9600},
 "fy28_adj_ebitda_usd_m_base": 11500,
 "one_number": "FY27 adjusted EBITDA ~$8.8B vs MarketScreener consensus $9,574M (-8%), driven by Power 2027 margin ~20% vs ~21.7-23.5% implied",
 "target_price_range_usd": [930, 1090],
 "target_formula": "22-26x Sep-2027 NTM adj EBITDA $10,825M (0.25x$8,800M FY27 + 0.75x$11,500M FY28) + $9,113M net cash, / 266.33M shares; midpoint 24x = $1,010",
 "horizon_months": 12,
 "kill_rule": "Late-Jan-2027 FY27 outlook with adj EBITDA midpoint below $8.3B (~15.75% margin on ~$52.7B) and no reaffirmation of the $11.2B 2028 plan, or the 2028 plan lowered at any point before the spring-2027 CMD",
 "top_reason": "Consensus FY27 looks ~8% too high, but the 12-month NTM roll to FY28 on management's own plan needs only ~23x (vs 28x today) to hold the price, and GEV's guide/framework days have historically been positive, so a short needs a de-rating that no primary evidence yet supports",
 "confidence_1_to_5": 2}
```
