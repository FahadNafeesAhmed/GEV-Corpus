# Variation: explicit 12-month horizon (to 2027-09-30)

_V12_horizon_12m — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 03:51:39. Requests 23, input tokens 1167686, output tokens 22959._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova (GEV) at $962.49: research ladder R1–R14, long or short to 2027-09-30

*Research input only. Every range and probability below is a research estimate, and the team picks its own numbers.*

**Source key**
- **Q2REL**: 8-K 0001996810-26-000147 EX-99, 2026-07-22
- **10Q**: 0001996810-26-000148
- **10K**: 0001996810-26-000015
- **Q4REL**: 8-K 0001996810-26-000012, 2026-01-28
- **CALL2Q**: Q2'26 transcript, corpus src:3161
- **MS**: MarketScreener, fetched 2026-09-29 (facts CT-02/04/06)
- **INV**: Investing.com GEV page, fetched 2026-09-30
- **247**: 24/7 Wall St., 2026-09-16
- **MB**: MarketBeat / ad-hoc-news, 2026-09-21
- **GF**: GuruFocus GLJ wire, 2026-09-15
- **YF**: FinRobot yfinance quote, 2026-09-30 07:47 UTC
- **BX**: Yahoo and Nasdaq price feeds (facts BX-01..13)
- **CL**: Chartloom
- **LAG**: GEV-hosted Laguna transcript, 2026-09-16
- **CFO-PR / CFOD**: GEV CFO release 2026-08-27 / CFO Dive 2026-08-28
- **GE02AR**: GE 2002 Annual Report
- **GE7/02**: GE Power Systems release, 2002-07-23
- **PE02**: Power Engineering, 2002-06

Computed figures (marked [computed]) are in §4. D0x/E0x are tonight's non-V outputs, which I read and used; I did not read any V-series output.

---

## 1. Bottom line
- **Over 12 months this is close to a coin flip. My research call leans slightly long (p_long 0.52), and the short edge is a 4-month trade.**
  - The best-evidenced finding runs against consensus: FY27 adjusted EBITDA of about $8.8B vs $9,574M, about −8% [S1: MS] [S2: GF "Street $9.45B"].
  - That gap is worth about −$60 to −90 per share. The consensus roll-forward from FY27 to an FY28-weighted NTM is worth more (+27%) [computed A1, A6].
- **The price needs only about 20.3x NTM EV/EBITDA in Sep-2027 if consensus holds, or about 22.8x on the research path.** Today the stock trades at 28.2x [computed A6] [S1: MS] [S2: CL 27.7x].
- **Consensus FY27 needs a Power segment margin of about 23%.** Management's target for 2028 is 22% [S1: Q4REL] [S2: corpus src:671, 2028 outlook text]. H1'26 actual was 17.6% [S1: Q2REL segment table] [S2: 10Q MD&A].
- **The January FY27 guide is likely to disappoint:** P(margin midpoint < 18.15%) ≈ 80–85% [D04A/B via D10]. Historical reaction on such days is −4% to −12% [D04B; BX-13]. That argues for a short into January, not for a 12-month short.
- **The spring-2027 Capital Markets Day (CMD), with a 2030 outlook, falls inside the 12-month window.** It prices the 2029–30 margin step the CEO himself has pointed to ("mostly sold out through '30") [S1: CALL2Q chunk 251595] [S2: LAG p.10, SINGLE for the "'29 and '30" line]. Both past investor-event framework resets were raises (+4 and +6 margin points) [S1: facts BR-28] [S2: Dec-24/Dec-25 releases].
- **Analog:** in GE's 2001–02 gas bust, earnings rose about 30% in the shipment-peak year while orders collapsed [S1: GE02AR] [S2: GE7/02, orders −80%]. Reported EBITDA is therefore a lagging tell. The item that would flip the call is orders/commitments, not margin.

---

## 2. The ladder

**R1. What today's price requires.**
- Market cap is $256.3B on 266.33M shares outstanding [S1: YF $962.49] [S2: 10Q balance sheet shares]. EV is about $247.2B after $9,113M net cash (cash $13,120M − borrowings $2,849M − NCI $1,158M) [S1: 10Q] [S2: stockanalysis EV $247.34B].
- Financially, holding $962.49 into Sep-2027 needs:
  - 20.3x on consensus NTM EBITDA of $12,191M; or
  - 22.8x on the research NTM of $10,825M [computed A6].
- Physically:
  - Gas output rises from 15.3 GW in FY25 to about 20–22 GW in 2027 and 24 GW in 2028 [S1: 10K/10Q GW tables] [S2: CALL2Q; LAG p.4].
  - Power's margin has to go from 17.6% in H1'26 to about 22% by 2028 [S1: Q2REL] [S2: Q4REL].
  - The contracted pipeline has to reach ≥125 GW by YE26 (116 GW today) [S1: Q2REL "44 to 53 GW… 56 to 63 GW"] [S2: CALL2Q].

**R2. Consensus vs management's plan.**
- FY27: revenue $52,740M and adjusted EBITDA $9,574M (18.15%) [S1: MS] [S2: GF $9.45B; S&P/stockanalysis $52.74B revenue].
- FY28: adjusted EBITDA $13,064M (21.6%) on revenue of $60.5B [S1: MS] [S2: Motley Fool 60% CAGR ≈ $13.09B (D10 Q8)].
- Management's 2028 plan: $56B revenue, 20% margin (= $11.2B), cumulative FCF ≥ $24B; segment margins Power 22% / Electrification 22% / Wind 6% [S1: Q4REL] [S2: corpus src:27 news 2026-01-23; src:2660].
- **The Street's FY28 is 16.6% above the plan** [computed A2].
- For FY26, consensus implies an H2 margin of 16.3% against 15.0% at the guide midpoint [computed A3]. Guide: [S1: Q2REL] [S2: CALL2Q].
- There is no FY27 guide yet.

**R3. Delivery vs guidance since the spin.**

| Metric | FY24 | FY25 | Measured against |
|---|---|---|---|
| Revenue | +1.3% | +4.3% | First numeric-guide midpoint |
| Adjusted EBITDA margin | 5.83% vs 6.0% | 8.40% vs 8.5% | Mid-year *raised* numeric guides (the first guides were qualitative and were met) |
| FCF | +89% | +65% | Initial guide |

- Sources: [S1: facts BR-21/23/24, computed from 8-Ks] [S2: Q4REL FY25 actuals; MS FY25 actual].
- **Qualifier:** "never cut" applies to company revenue and FCF only. The Wind guide was cut at Q3'25, and the 2028 Wind margin target went from 10% to 6% [S1: 8-K 0001996810-25-000159] [S2: DEC25 via D10 Q7].
- The 2025 bonus targets (adjusted EBITDA $2.9B; actual $3,196M) were beatable [S1: DEF 14A -26-000049] [S2: Q4REL actuals]. The target levels are [SINGLE-SOURCE].

**R4. Where the evidence differs most.**
- **The line is FY27 Power segment EBITDA margin: consensus-implied about 23.3% vs a research base of about 20.5%**, a gap of about −$0.8B, which is −8% on total FY27 adjusted EBITDA [computed A4]. Inputs: [S1: Q2REL segments] [S2: 10Q].
- D01A and D01B independently reached $8,744M and $8,600M (via D10 Q2).
- On FY28, the gap to the Street is −12% on the research base ($11.5B) [computed A2].

**R5. Why the market may not already see it.**
- This is interpretation and timing, not new information:
  - Margin-in-backlog is published every January, and analysts asked about it on the Q4'25 call (brief §5; D10 Q5).
  - Consensus Power margin is not published, so there is no free segment consensus.
  - The only direct figure is GLJ's "20.7%" [SINGLE: GF].
- I could not verify any mechanism that would make the market *systematically* miss this, so I rate the edge from R4 as small.

**R6. Strongest long argument.**
1. **Roll-forward.** NTM EBITDA rises 27% from $9.574B to $12.19B by Sep-2027 on consensus, or 13% on the research path [computed A6].
2. **Pricing and capacity.**
   - SRAs carry 10–20+ points of pricing strength [S1: Q4'25 call] [S2: Q2'26 ">20%" via brief §6].
   - The book is "mostly sold out through '30" [S1: CALL2Q chunk 251595] [S2: corpus src:2207 news 2026-02-22].
   - Siemens Energy is also sold out to FY28 [S1: SE CFO deck src:3179] [S2: src:1699].
3. **Operating leverage.** Power's incremental margin was 44.4% from H1'25 to H1'26 [S1: 10Q] [S2: CALL2Q, +320 bp].
4. **The CMD is inside the horizon, and management has raised its framework at both past investor events** [S1: BR-28] [S2: Dec releases].
5. **FCF accretion.** Roughly $6–7B of FCF accrues to Sep-2027, about +$25 per share [computed A7; FY27 FCF [SINGLE: MS]].

**R7. Strongest short argument.**
1. **Street above plan.** Consensus FY27 needs Power at about 23%, a year before the 22% target. FY28 consensus is +16.6% above the plan [computed A2, A4].
2. **January guide.** P(midpoint < 18.15%) ≈ 80–85% [D04A/D04B].
3. **Worsening CSA revisions.** Contractual service agreement profitability revisions were −$218M in H1'26, against −$151M for all of FY25 [S1: 10Q Note 9] [S2: 10K Note 9].
4. **Slowing commitments.** H2 commitments are expected below H1's 40 GW [S1: LAG p.3] [S2: stockanalysis Laguna transcript (via D10)].
5. **Multiple and crowding.** The stock trades at about 2x the market on P/E (38.7x FY27 EPS) and sits in AI-theme short baskets. It has had five drawdowns of 15%+ since the spin, median −24.6% [S1: BX] [S2: Nasdaq closes].

**R8. Which side's evidence is stronger.**
- **Short:** on the *estimate* line, primary filings and two consensus vendors within 1.3% make this high quality.
- **Long:** on the *price* line, the roll-forward is simple arithmetic on consensus (high) plus the history of management's framework raises (primary, n=2, medium).
- **Weakest short leg:** the "'29 and '30" timing quote is [SINGLE-SOURCE: LAG p.10]. It also cuts both ways over 12 months, because the market in Sep-2027 prices FY28–29.

**R9. Dated reveals and pass marks.**

| Date | Event | Long passes if | Short passes if |
|---|---|---|---|
| Late Jan-2027 | FY27 guide (presented by Parks, not the new CFO [S1: CFO-PR] [S2: CFOD]) | Low end of margin range ≥ 18% | Midpoint ≤ 17% |
| Spring-2027 | CMD | 2028 raised to ≥ ~$12.5B, or 2030 outlook implies Power ≥ 24% | 2028 held at $11.2B |
| YE26 | Contracted gas GW | ≥ 125 GW | Below 125 GW |
| 2026-10-28 | Q3'26 (after the finals) | EBITDA ≥ $1,706–1,728M consensus | Below it |

- Q3 consensus sources: [S1: MS] [S2: ChartMill via D07].

**R10. Size of loss if wrong.**
- Since the spin the stock has had five closing drawdowns of ≥15%, median −24.6% and maximum −38.3% [S1: BX] [S2: Nasdaq].
- For the long, a median drawdown means about $725. A research-path path to 18x gives $749 [computed A6].
- For a short, the risk is consensus holding at 25x, about $1,179 (+22%) [computed A6].

**R11. What the market would pay in Sep-2027.** Formula: value = (m × NTM + $9,113M) / 266.33M, excluding FCF accretion (add ~$25 per share for it).

| Estimate path (NTM) | 20x | 22x | 23x | 25x |
|---|---|---|---|---|
| Research, $10,825M | $847 | $928 | $969 | $1,050 |
| Consensus, $12,191M | $950 | $1,041 | — | $1,179 |

- Scenario-weighted value centred on the research FY28 path is about $971, +0.9% [computed A8].

**R12. Historical analog.**
- In the GE Power Systems boom and bust of 1999–2002:
  - 2002 earnings grew "nearly 30% as shipments of gas turbines in the U.S. peaked" [S1: GE02AR].
  - US orders and shipments were forecast to fall "80 percent or more over the next two years" [S2: GE7/02].
  - The collapse came through merchant IPP cancellations: Calpine restructured about $3.4B of turbine commitments in Feb-2003 [S1: PE02] [S2: Calpine 8-K Feb-2003, SEC 0000916457-03-000003].
- GE's stock went from $60 (42.6x) to $31.85 (21.1x) while EPS rose 19% (D05, from GE ex-99 filings and the NY Post). That is a single-publisher chain through D05, so treat it as medium confidence.
- **What the analog implies here:**
  - The bust signal is orders and cancellations, not EBITDA.
  - GEV's orders are still accelerating: Power orders +134% organically in Q2 [S1: Q2REL] [S2: CALL2Q].
  - GEV's customers today are regulated utilities and hyperscalers, not merchant IPPs; I did not verify this mix. SRAs (54% of contracted GW) are the soft spot.
  - A 2002-style de-rating inside 12 months needs an orders break that no evidence currently shows.

**R13. The observation that would flip the view.**
- Gas commitments of < ~20 GW in H2'26, or the YE26 total below 125 GW, together with any SRA cancellation disclosure (Q3 or Q4 10-Q/10-K). That would be the 2001-style tell.
- On the estimate side: an FY27 margin guide midpoint ≤ 17% with the 2028 plan held.

**R14. Confidence: 2/5. The main source of uncertainty is the Sep-2027 multiple (20–25x).**
- One turn of multiple is about $41–46 per share, which is larger than the whole FY27 estimate gap [computed A6].
- The second-biggest uncertainty is whether the CMD raises 2028–30.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Confidence |
|---|---|---|---|---|---|---|
| 1 | Close 2026-09-29 | $962.49 | YF 2026-09-30 | Zacks/Yahoo (D08 #1) | exact | H |
| 2 | FY26 guide | $45.5–46.5B; 12–14%; FCF $11.5–12.5B | Q2REL "2026 Guidance" | CALL2Q chunk 251609 / corpus src:1016 | exact | H |
| 3 | 2028 plan | $56B; 20%; FCF ≥ $24B | Q4REL | corpus src:27 (2026-01-23) | exact | H |
| 4 | Power H1'26 EBITDA / margin | $1,842M / 17.6%; Q2 18.8% | Q2REL segment table | 10Q MD&A | exact | H |
| 5 | Electrification H1'26 | $1,200M / 18.2% | Q2REL | 10Q | exact | H |
| 6 | H1'26 adjusted EBITDA / FCF | $2,146M / $9,897M | Q2REL | 10Q | exact | H |
| 7 | Consensus FY27 EBITDA | $9,574M | MS | GF $9.45B | close (−1.3%) | M |
| 8 | Consensus FY28 EBITDA | $13,064M | MS | Motley Fool ≈ $13.09B | close | M |
| 9 | Consensus target | $1,237.34; 30 Buy / 0 Sell | INV | 247 (6 SB + 24 B / 7 H) | exact; **conflict with MB $1,145.83** (different panel) | M |
| 10 | Equipment RPO YE25 in 1/2/5 years | $64,245M; 37/69/97% | 10K Note 9 (chunk 29868) | Q4'25 call "$64B" | exact | H |
| 11 | Gas GW | 53 + 63 = 116 GW; ≥ 125 GW YE26 | Q2REL | CALL2Q chunk 251595 | exact | H |
| 12 | CSA revisions | −$218M H1'26 vs −$151M FY25 | 10Q Note 9 | 10K Note 9 | exact | H |
| 13 | Drawdowns ≥ 15% | 5; median −24.6% | Yahoo (BX) | Nasdaq closes | exact | H |
| 14 | "'29 and '30" equipment-margin line | CEO, 2026-09-16 | LAG p.10 | not found elsewhere | [SINGLE-SOURCE] | L–M |
| 15 | GE 2002 analog | earnings +~30% at shipment peak; orders −80% | GE02AR | GE7/02 | consistent | H |
| 16 | January presenter is Parks | — | CFO-PR | CFOD | exact | H |
| 17 | Erste FY27 EPS | $24.55 (vs MS $24.85) | MB 2026-09-21 | TickerReport 2026-09-23 | exact (same wire) | M |

---

## 4. Arithmetic
- **A1. FY27 gap.** (8,800 − 9,574) / 9,574 = −8.1%. At 25x: −774 × 25 / 266.33 = −$73 per share.
- **A2. FY28 comparisons.**
  - 13,064 / 11,200 = +16.6% (Street vs plan).
  - 11,500 / 13,064 = −12.0% (research base vs Street).
- **A3. FY26 H2 margin.**
  - Guide midpoint: 13% × 46,000 = 5,980. H2 = 5,980 − 2,146 = 3,834, on revenue of 46,000 − 20,442 = 25,558 → 15.0%.
  - Consensus: 6,359 − 2,146 = 4,213, on revenue of 46,282 − 20,442 = 25,840 → 16.3%.
- **A4. FY27 segment build (research estimate; the team chooses).**
  - Power revenue: 19,767 × 1.19 = 23,523 (FY26), × 1.165 = 27,404 (FY27). At 20.5% → 5,618.
  - Electrification: 14,750 × 1.20 = 17,700. At 21% → 3,717.
  - Wind −50. Corporate −475. Corporate is based on FY25 −541 (= 3,196 − (2,902 + 1,433 − 598)) and H1'26 −239 (= 2,146 − (1,842 + 1,200 − 657)).
  - Total = 8,810.
  - Consensus-implied Power margin: (9,574 − 3,717 + 50 + 475) / 27,404 = 23.3%.
  - Low: 19% × 27.0B + 20% × 17.4B − 200 − 500 = 7,910.
  - High: 22% × 27.8B + 22% × 18.0B + 100 − 450 = 9,726.
- **A5. Market cap.** 962.49 × 266.33 = $256,340M. EV = 256,340 − 9,113 = $247,227M.
- **A6. Sep-2027 values.**
  - Research NTM = 0.25 × 8,800 + 0.75 × 11,500 = 10,825. Consensus NTM = 0.25 × 9,574 + 0.75 × 13,064 = 12,191.
  - Price = (m × NTM + 9,113) / 266.33, giving the R11 grid. At 18x on the research NTM: $749.
  - Breakeven multiples: 247,227 / 10,825 = 22.84x; 247,227 / 12,191 = 20.28x.
  - One turn of multiple = NTM / 266.33 = $40.6 (research) to $45.8 (consensus).
- **A7. FCF accretion to Sep-2027.**
  - H2'26: 12,000 − 9,897 = 2,103.
  - Plus 0.75 × FY27 FCF of 7,417 [SINGLE: MS] = 5,563.
  - ≈ $7.7B gross; about $6–7B after dividends (dividend amount not verified) → about +$25 per share.
- **A8. Scenario-weighted Sep-2027 value (including ~$7B accretion; research judgement, the team chooses).**

| Scenario | P | FY28 | NTM | Multiple | Price |
|---|---|---|---|---|---|
| Raise | 20% | 13.0B | 12.1B | 25x | $1,196 |
| Trim | 30% | 12.0B | 11.2B | 23x | $1,028 |
| Plan | 35% | 11.2B | 10.6B | 21x | $896 |
| Cut + de-rating | 15% | 10.5B | 9.9B | 18x | $730 |

  - Expected value = $971 (+0.9%); without the accretion, about −1.8%. P(up) ≈ 50%.

---

## 5. General question bank items answered along the way
- **G1/G5:** see R1 and A6. If the stock is flat for 12 months, the multiple must have fallen to about 20–23x.
- **G14:** the reveal could slip beyond the horizon if the CMD moves past Sep-2027. Its date is not set [LAG p.11] [src:686].
- **G19:** see R12.
- **G20:** these rest on one source or carry a definition trap: the "'29 and '30" line, GLJ's 20.7%, FY27 FCF and NCI. The MarketBeat vs Investing.com target gap ($1,145.83 vs $1,237.34) is a panel-definition trap.
- **G24:** FY27 FCF consensus falls to $7.4B (−38%) as deposit inflows normalise [SINGLE: MS].

## 6. What would change this
- **For the long:** YE26 contracted gas below 125 GW, an SRA cancellation, a Jan midpoint ≤ 17% with no CMD raise, or NTM ≤ 20x.
- **For the short:** a Jan low end ≥ 18%, 2028 raised to ≥ $12.5B, or Q3 EBITDA well above $1,728M.
- **For the R4 gap:** a published Power FY27 consensus near 20.5%, which would mean no gap exists.

## 7. Disagreements with the master brief
1. **The brief's lean (short, 55–60%) holds for about a 4-month horizon only.** At 12 months my research finds about 50/50, tilted slightly long, because the roll-forward, the CMD and FCF accretion all fall inside the window.
2. **The "first call under the new CFO" point is wrong:** Parks presents the January call [CFO-PR] [CFOD].
3. **"Margin below first numeric guide" is wrong as worded:** the misses were against mid-year raised guides (BR-23).
4. **"Never cut" is wrong as worded:** Wind was cut (R3).
5. **The brief's value formula leaves out about $25 per share** of FCF accretion by Sep-2027.
6. **The consensus target is vendor-dependent:** $1,237.34 (INV) vs $1,145.83 (MB).

## 8. Open items
- A second full-row vendor for FY27/FY28 EBITDA (FactSet or Bloomberg).
- Laguna pp.9–11 in full, to check the "'29 and '30" line.
- GEV's dividend amount, for the accretion figure.
- The CMD date.
- Whether the move from the Dec-25 FY26 margin guide (11–13%, ex-Prolec) to today's 12–14% was organic or came from Prolec (check the Q1'26 8-K).
- Customer mix of SRAs (utility vs merchant vs hyperscaler).

```FINAL_BLOCK
{"direction": "long",
 "p_long": 0.52,
 "fy27_adj_ebitda_usd_m": {"low": 7900, "base": 8800, "high": 9700},
 "fy28_adj_ebitda_usd_m_base": 11500,
 "one_number": "FY27 Power segment EBITDA margin: consensus-implied ~23.3% vs research ~20.5% (~-$0.8B; FY27 adj EBITDA ~$8.8B vs $9,574M consensus, -8%)",
 "target_price_range_usd": [850, 1180],
 "target_formula": "Sep-2027: 23x x NTM EBITDA $10,825M (0.25x$8.8B FY27 + 0.75x$11.5B FY28) + $9,113M net cash / 266.33M = $969 (~$995 incl ~$7B FCF accretion); range 20x research NTM ($847) to 25x consensus NTM $12,191M ($1,179)",
 "horizon_months": 12,
 "kill_rule": "Long is wrong if the late-Jan-2027 FY27 adj EBITDA margin guide midpoint is <=17.0% AND the 2028 framework is not raised at the spring-2027 CMD (by 2027-06-30), or if YE2026 gas backlog+SRAs <125 GW",
 "top_reason": "Over 12 months the FY27->FY28 consensus roll-forward (+27% NTM) plus an in-horizon 2030 CMD outweigh a likely ~8% FY27 estimate cut; breakeven is ~20-23x NTM versus 28x today",
 "confidence_1_to_5": 2}
```
