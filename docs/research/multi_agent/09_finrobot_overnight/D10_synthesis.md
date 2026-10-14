# Overnight synthesis — what tonight's work changes

_D10_synthesis — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 03:04:09. Requests 20, input tokens 2121143, output tokens 31087._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV overnight synthesis: FinRobot pipelines vs verified research, EBITDA range, January-guide odds, long/short scoring (as of 2026-09-30)

Research input only. The team writes all memo text and picks every forecast number. Where a range is given, it is a research estimate and the team chooses its own number.

**How I read the inputs:**
- **Read in full or nearly in full:** D01A, D01B, D02, D03, D04A (first 62%), D04B (first 95%), D05, D08, V10, P1, P2, P3, P5 (first 79%), P6, P7.
- **Read in part:** P4 (the first half; its surprise dataset was empty), D06, D07, D09 (roughly the first quarter to third of each).
- **V01–V09 not read directly.** I relied on V10, which says it read all nine in full.
- **Checked myself this session:**
  - The Laguna transcript on stockanalysis.com. It confirms the "H2 commitments below 40 GW" remark, the 5→6 GW/quarter output ladder, the Wind "2027 much better than 2026" remark and the "do better internally" line. That is a second publisher next to GEV's own PDF.
  - Two Exa searches for the "'29 and '30" line. Neither found it outside GEV's PDF.
  - A phrase search of the 10-K for "recognize revenue over time". Not found. D09's over-time recognition claim is therefore not re-checked.

**Source key** (the underlying tasks carry the full citations):
- **Q2REL** = 8-K 0001996810-26-000147, EX-99 (2026-07-22)
- **10Q** = 10-Q 0001996810-26-000148
- **10K** = 10-K 0001996810-26-000015
- **Q4REL** = 8-K 0001996810-26-000012
- **DEC25** = Dec-2025 investor-update release/deck
- **LAG-PDF** = GEV-hosted Laguna transcript, 2026-09-16
- **LAG-SA** = stockanalysis.com Laguna transcript (read this session)
- **MS** = MarketScreener, fetched 2026-09-29
- **GF** = GuruFocus GLJ wire 9079408, 2026-09-15
- **CFO-PR** = GEV CFO-transition release, 2026-08-27
- **CFOD** = CFO Dive, 2026-08-28
- **BX** = Yahoo chart API and Nasdaq closes (facts BX-03..08, BX-13)

---

## 1. Bottom line

- **Every run tonight lands FY27 below consensus.** FY27 adjusted EBITDA: D01A base $8,744M (statistical band $7.68–9.58B), D01B base $8,600M ($7.33–9.97B), and the nine variants a median of $8,800M (base range $8.7–8.9B). Against MS consensus of $9,574M, that is roughly −8% to −10%.
  - Consensus inputs: [S1: MS 2026-09-29] [S2: GF, "Street $9.45B", −1.3%].
  - Build inputs: [S1: 10Q segment note] [S2: Q2REL segment table].
  - This is the most robust finding of the night, and it held across all framings (V10 §Q4).
- **What consensus needs from Power.** Holding Electrification, Wind and Corporate at the builds' base, FY27 consensus needs Power segment EBITDA margin of about 21.7–23.5%. Management's target for 2028 is 22%.
  - Computed in D01A Q11 and D01B §4-L; D04B gets 23.9% with its own split.
  - 2028 target: [S1: Q4REL] [S2: DEC25].
- **Direction is not robust, and it depends on horizon.** Across nine prompt framings, p_long had a median of 0.46 (range 0.43–0.55). Anchoring moved it by 0.07 against a noise swing of 0.03.
  - Every 4–5-month framing was short (median 0.45). The 12-month median was about 0.51.
  - Source: [S1: V10 FINAL_BLOCK table] [S2: V08 A8, 0.45 at 4 months vs 0.57 at 12 months].
- **The January 2027 FY27 margin guide.** Combining D04A and D04B:
  - P(guide midpoint < 18.15% consensus) ≈ 80–85%.
  - P(midpoint ≤ 17.5%) ≈ 65–68%.
  - Ken Parks, not the new CFO, most likely presents it [S1: CFO-PR, "inclusive of the third and fourth quarter earnings calls"] [S2: CFOD].
  - The brief's "new-CFO reset" leg should be dropped.
- **The price mechanics favour the long over 12 months.** At a constant 25x, the consensus NTM roll-forward from Jan-2027 to Sep-2027 is worth about +$218/share (computed §4-A7). The evidence-based FY27 gap is worth about $60–90/share [S1: V10 A4] [S2: V03 R14 via V10].
  - A short therefore needs a de-rating. About $109 of the typical short target in a January frame comes from an assumed 28.2x→25x multiple cut [V10 A4; V04 A3].
- **FinRobot's own pipelines (P1–P7) should not be used for valuation.**
  - Their DCF ($190.59; WACC 8.3%; g 3.0%) runs on a 4.7% EBITDA margin from yfinance history. That is not GEV's adjusted EBITDA, and GEV guides 12–14% for FY26 and 20% for 2028.
  - Comps failed with no peers. The LBO/IC gate was entered at 8x trailing.
  - Sources: [S1: P2 "Dcf Calc"] [S2: P5 "Financial Analysis"]. Guide: [S1: Q2REL] [S2: Q4REL].

---

## 2. Answers

### Q1. FinRobot pipelines (P1–P7) vs verified research

| Item | FinRobot (P#) | Verified research | Which is right, and why |
|---|---|---|---|
| Price | $962.49 (P1–P5) | $962.49 [S1: yfinance] [S2: Zacks/Yahoo 9/29] (D08 #1) | Agree |
| 52-week low | $529.18 (P1/P2) | $530.16 (Motley Fool quote box; D08 #2 flags it [SINGLE]) | **Conflict, unresolved.** One is probably intraday and the other a close; hand-verify (§8 #9). The high of $1,195.94 is intraday; the record close is $1,174.86 (D08) |
| EV | $247.34B = mcap + $3.72B debt − $12.72B cash; NCI treated as null (P1/P2/P5) | $247.23B = mcap + $2,849M borrowings + $1,158M NCI − $13,120M cash [S1: 10Q balance sheet] [S2: stockanalysis $247.34B] (D08 #8) | Equal within 0.05%, but only because errors offset. FinRobot leaves out NCI (+$1.16B) and uses debt including ~$0.87B of leases and cash excluding ~$0.4B restricted. Use the 10-Q bridge |
| TTM EBITDA | $3.927B; EV/EBITDA 63x (P1–P7) | Company adjusted TTM = 3,196 − 1,227 + 2,146 = **$4,115M** [S1: Q4REL, Q2REL] [S2: 10Q; V10 G20] | yfinance EBITDA is a different definition. **Do not cite 63x.** Forward is 25.8x FY27 / 28.2x NTM (D05) |
| Historical EBITDA | FY24 $1.64B (4.7%), FY25 $2.24B (5.9%) (P1/P2) | Adjusted $2,035M (5.8%), $3,196M (8.4%) [S1: Q4REL] [S2: MS FY25 actual] | yfinance is not GEV-adjusted, so the DCF margin input starts from the wrong base |
| DCF | $190.59; WACC 8.3%; g 3.0%; 10-year; revenue growth 8.7% fading to 3%; EBITDA margin 4.7%; capex 2.5%; D&A 2.9%; NWC −3.4%; band $145–344; Monte Carlo P5–P95 $90.76–$329.24, current price at the 100th percentile (P1/P2/P5) | FY26 guide: revenue $45.5–46.5B (+20.8% at midpoint vs $38,068M), margin 12–14%; 2028: 20% on $56B [S1: Q2REL] [S2: Q4REL/DEC25] | **The research is right.** The pipeline DCF ignores guidance, backlog and consensus: its margin is about ¼ of the 2028 plan and its growth about ⅖ of the FY26 guide. Its own "market-implied 30.6%/yr growth" figure is the only usable output. The WACC/g inputs are not wrong, but they are not the binding assumption |
| Comps | Failed ("peer candidates unavailable") (P3). P6 gives peers labelled "indicative approximations… not verified", e.g. Siemens Energy ~30–40x TTM | Computed NTM: US electrical median ≈21x; all-eight median ≈17.7x; Siemens Energy 12.6x FY27 [S1: MS BX-29..36] [S2: TIKR cross-checks, VRT ~24x, SU ~17x] (D05 Q2) | **Do not use P6's peer numbers.** They are unverified and on a different basis. D05's peer EBITDA multiples are largely [SINGLE-SOURCE: MS] |
| FY27/FY28 estimates | None; yfinance forward EPS $25.13 only (P1–P5) | FY27 EPS $24.85 (MS) / $24.78 (FactSet) / $25.13 (S&P); EBITDA $9,574M / $13,064M (MS) (D08 #21–24) | Pipelines had no estimate data. Weight them at zero on forward numbers |
| P/E | Trailing 27.25x, forward 38.31x (P1) | Trailing figure includes the $3,992M Prolec remeasurement gain and the $330M Proficy gain [S1: Q2REL footnote (a)] [S2: D07 Q1; D08 Q4 #1] | Trailing P/E is distorted; FY27 38.7x is consistent across vendors |
| LBO / IC gate | Entry at 8.0x TTM EBITDA, MOIC 0.3x, IRR −21.5% → "PASS", SELL (P5) | Market is at 25.8x FY27 | An artefact: the entry multiple is about ⅓ of the market. Not evidence for either side |
| Risks | Earnings quality (NI > EBITDA), OCF 3.6x EBITDA from advances, valuation (P5/P6/P7) | NI gap = Prolec gain (above). OCF: contract-liability inflow $13,695M in H1'26 [S1: 10Q cash flow] [S2: Q2 call, mechanism only; the numeric is SINGLE] (D08 #17) | **Direction agrees; the numbers do not.** P7's "normalized P/E ~100x" and "0.9% normalized FCF yield" are built on the yfinance EBITDA and should not be used |
| Earnings history | Empty dataset, "0% beat rate" as a placeholder (P4) | Q2'26 EPS miss; Q4'25 adj EBITDA $1.16B vs $1.29B estimate [SINGLE: StockStory via D04A] | P4 carries no information |

### Q2. FY27/FY28 EBITDA: reconciling D01A and D01B

| $M | D01A base | D01B base | Difference (B − A) | Why |
|---|---|---|---|---|
| Power | 5,638 (20.5% on 27,503; 21 GW) | 5,520 (20.0% on 27,600; 20 GW) | −118 | GW (21 vs 20) and margin (+0.5 pt) |
| Electrification | 3,581 (20.5%) | 3,630 (20.5%) | +49 | Revenue |
| Wind | 0 | −100 | −100 | Offshore close-out assumption |
| Corporate | −475 | −450 | +25 | — |
| **Total** | **8,744 (16.7%)** | **8,600 (16.4%)** | **−144** | Power volume/margin (~80%) plus Wind (~70%), partly offset by Electrification/Corporate |

Sources: D01A §4 FY27 table; D01B §4-J. Inputs: [S1: 10Q segment note] [S2: Q2REL]; GW [S1: Q2 transcript "at least 30 gigawatts"] [S2: LAG-SA ladder, read this session].

**Research range (the team chooses its own number)**

| Year | Low | Base | High | Consensus (MS) | Position of consensus |
|---|---|---|---|---|---|
| FY27 | ~$7.7B (A statistical); $7.3B (B corner) | **$8.6–8.8B** (variant median $8.8B) | ~$9.6B (A statistical; variant-median high); $10.0B (B corner) | $9,574M | At the top of the statistical band |
| FY28 | $9.2–9.7B | **$11.0–11.2B** (≈ framework $11.2B) | $12.6B (A statistical); $13.0B (B) | $13,064M | Above A's high, at B's high |

**What drives the gap to consensus.** In both builds it is the FY27 Power margin: about $275M per point in A, and $125M per point of equipment margin in B. Consensus needs about 23.5% in both builds, against 20.0–20.5% in their bases.

**A new cross-check from D06.**
- D06 puts H1'26 Power equipment EBITDA margin at a central +3.6% (range −4% to +11%), with services at about 22–27% [S1: 10K Note 24] [S2: FY24 10-K Note 24; 10Q p.23].
- Holding services at 24.5% on D01A's $14.8B, D01A's base Power margin (20.5%) needs FY27 equipment at about 15.8%. Consensus (23.5%) needs about 22.4% (computed §4-A3).
- From D06's +3.6%, those are rises of about 12 and 19 points in six quarters. The FY23→H1'26 pace was about 25–30 points over roughly 2.5 years.
- So the builds' base sits on trend, and consensus sits well above it.
- Caveat: D01A's own split (equipment 7–14% in H1'26) is higher than D06's. The two tasks disagree on the services margin, and GEV does not disclose it.

### Q3. January-guide distribution: combining D04A and D04B

FY27 adjusted EBITDA margin guide, midpoint (research judgement):

| Bucket | D04A | D04B | Combined (mean) |
|---|---|---|---|
| <15% | 4% | 5% | 4.5% |
| 15–16% | 10% | 10% | 10% |
| 16–17% | 22% | 25% | 23.5% |
| 17–18% | 34% | 30% | 32% |
| 18–19% | 23% | 22% | 22.5% |
| ≥19% | 7% | 8% | 7.5% |

| Derived probability | D04A | D04B | Combined |
|---|---|---|---|
| P(midpoint < 18.15%) | 85% | 80% (band 70–85%) | **~82% (band 75–85%)** |
| P(midpoint ≤ 17.5%) | 66% | 65–70% | **~66–68%** |
| P(midpoint ≤ 17.0%) | 56% | ~40% on its buckets | **40–56%: the passes disagree** |

- **Why the last row diverges.** GEV guides in whole-number ranges [S1: 8-Ks BR-03/10/12/19] [S2: DEC25; TheFly/TipRanks 2026-04-22]. A 2-point range therefore has an integer midpoint (16–18 gives exactly 17.0). D04A puts much of its 17–18% bucket at exactly 17.0; D04B does not. The team should state which it assumes.
- **Dollar translation** (computed §4-A5, on consensus revenue $52,740M): 17.0% → $8,966M (−6.4%); 17.5% → $9,230M (−3.6%); 18.0% → $9,493M (−0.8%).
  - A margin miss can come with an EBITDA-dollar match if revenue is guided higher. D09: 17–19% on $54B ≈ $9.7B.
- **Reaction base rates** [S1: BX-13] [S2: event press per D04B Q9]:
  - Cautious-guide analogues: −4% to −12%.
  - Past framework/margin-raise days: +13.75% to +15.62%.
  - The Q2'26 day, when margin was held: −8.69%.

### Q4. Scoring the long (D02) against the short (D03)

| Side | # | Argument | Evidence quality | Size in $/share (computed §4) | Note |
|---|---|---|---|---|---|
| Short | S1 | Street FY27 is 9–17% above the path from the FY26 guide to the 2028 plan; Power at its 2028 target a year early | **H**: inputs two-sourced; consensus two vendors within 1.3% | −$60 to −90 (FY27 gap $0.8–1.0B) | Survived all nine framings |
| Short | S2 | CEO's "'29 and '30" timing; Street FY28 pulls ~6–7 points of Power equipment margin forward | **L–M**: [SINGLE-SOURCE: LAG-PDF p.10]; not in LAG-SA or other copies; refers to the *2026* backlog-margin change | Up to −$115 on Sep-27 NTM (0.75 × $1.9B FY28 gap at 22x) | Fragile leg (D08 Q5) |
| Short | S3 | Margin finished below the mid-year numeric-guide midpoint 2/2; the H2'26 step needed is 2.6x any past step | **M**: n=2, misses of $40–61M; first guides were qualitative and were met (D03/D04B) | FY26 −$379M if H2 lands at the guide midpoint | Q3 (10-28) tests it, after the finals |
| Short | S4 | AI-capex sentiment beta; five 15%+ drawdowns, median −24.6% | **H** as history; carries no timing | ~$40–46 per turn of multiple | Main route to the de-rating the short needs |
| Short | S5 | CSA profit revisions worsening: −$218M in H1'26 vs −$151M in all of FY25 | **H** [S1: 10Q Note 9] [S2: 10K Note 9] | ~−$0.2–0.4B/yr | Newest short-leaning fact |
| Short | S6 | H2'26 commitments below H1's 40 GW; some SRAs set price later (Maxim) | **M**: now two-source [S1: LAG-PDF p.3] [S2: LAG-SA, read this session] | FCF/orders, not FY27 EBITDA | — |
| Long | L1 | +39% NTM roll-forward; breakeven 20.3x in Sep-27 | **H** arithmetic; **M** consensus source | +$150 (research path) to +$218 (consensus) at constant 25x, Jan→Sep 2027 | Biggest single magnitude of the night |
| Long | L2 | Power incremental margin 44.4% (H1'26); opex ratio 12.7% → 11.5% | **H** [S1: 10Q] [S2: Q2 call] | Already inside both builds | Does not close the gap to consensus's 23.5% |
| Long | L3 | 2025 vintage is 47–62% of 2027 equipment dollars | **M**: RPO curve ±$0.64B, all-segment | Rebuts GLJ by $0.55–0.62B, **not consensus** | Dollar share ≠ margin share |
| Long | L4 | Electrification: +29% organic, RPO +69% | **H** | $3.3–3.8B FY27 | Prolec is running at 22.0%, not 25% (see Q7) |
| Long | L5 | Wind runoff, "'27 much better than '26" | **M**: now two-source [S1: LAG-PDF] [S2: LAG-SA]; poor guide record | +$0.1–0.65B FY27 | — |
| Long | L6 | Industry capacity sold out to about FY28; pricing +10–20 points | **M–H** | Mostly beyond the horizon; supports the January backlog page | — |
| Long | L7 | Framework raises in Dec-24/Dec-25; spring-27 CMD | **M**: no Dec-2026 event listed | Kill for the short if 2028 is raised toward ~$13B (P ≈ 40–50%, D02) | — |

**Verdict (research judgement):**
- **On the estimate line, the short's evidence is stronger.** S1 is the best-evidenced finding of the night; no long argument refutes it, and L2–L5 are already inside the builds that produce the gap.
- **On the price line, the long's evidence is stronger.** L1 is about 2–3x the size of S1 over 12 months, and it is also H-quality.
- **Net by horizon:**
  - Through the January call (roll-forward only about ⅓ realised), the short has a small edge of roughly +5 to +10 points of probability.
  - At 12 months there is no edge.
  - This matches V10.

### Q5. The prompt-variation experiment (V01–V09, from V10)

- **Held under every framing:**
  - FY27 base $8.7–8.9B, about −8% vs consensus.
  - Street FY28 +16.6% above plan.
  - The margin record: revenue and FCF beat, margin lands inside the range below the midpoint.
  - The gap is interpretation/timing, not information.
  - The January guide is the reveal, and a low end ≥18% kills the short.
  - The multiple dominates the estimate gap.
  - The gas-bust analogues do not support a bust inside the horizon.
  - Confidence 2/5 everywhere [S1: V10 §Q4] [S2: V01–V09 FINAL_BLOCKs as tabulated in V10 Q1].
- **Moved with framing:**
  - Direction (3 long / 6 short).
  - Horizon choice, which fully sorts direction among the brief-fed runs.
  - Target ranges.
  - FY28 base ($10.8–12.0B).
  - The January short pass mark (16.5–17.5%).
  - The "new-CFO" angle, which only the runs without web access kept.
- **How much weight tonight's direction call deserves: low.**
  - The anchoring effect (0.07) is about 2.3x the noise band, and that band rests on a single noise pair.
  - All nine runs share the same model and corpus, so repetition is not independent confirmation.
  - Use the direction only conditioned on horizon.

### Q6. Direction assessment (research input; the team decides)

**Probabilities (research judgement)**

| Horizon | P(short right) | P(long right) | Basis |
|---|---|---|---|
| Through the late-Jan-2027 call (~4 months) | ~55% | ~45% | V10 4–5-month median p_long 0.45; P(guide < consensus) ~82% |
| 12 months (Sep-2027) | ~48–50% | ~50–52% | V10 12-month median 0.51; D03 P(≤$866 at 12m) 30–35%; D02 P(+15%) 30–40% |

**Where the evidence most clearly differs from consensus:**
- **FY27 adjusted EBITDA (GEV-adjusted basis).** Consensus $9,574M / 18.15% [S1: MS] [S2: GF $9.45B]. Research range $7.7–9.6B, base $8.6–8.8B.
- **The driver line is the FY27 Power segment EBITDA margin.** Consensus-implied 21.7–23.5% vs research 18.5–21.5% (base 20.0–20.5%).
  - Consensus Power margin is derived, not published. The only direct figure is GLJ's 20.7% [SINGLE-SOURCE: GF].

**Target-range formula.** Value = (m × NTM EBITDA + $9,113M) / 266.33M.

| Frame | NTM definition | Research path NTM | 22x | 25x | 28.2x | Consensus path NTM |
|---|---|---|---|---|---|---|
| Jan-2027 | 11/12 × FY27 + 1/12 × FY28 | $8,900M (FY27 8.7 / FY28 11.1) | $769 | $870 | $977 | $9,865M → $1,079 at 28.2x |
| Sep-2027 | 0.25 × FY27 + 0.75 × FY28 | $10,500M | $902 | $1,020 | — | $12,191M → $950 / $1,041 / $1,179 at 20 / 22 / 25x |

Research path at Sep-2027, 20x: $823. Computed §4-A6; the multiple is the team's choice. D05 anchors: consensus-holds 22–28x; cut 5–10% 20–25x; cut 10–15% 16–22x.

**Dated proof points and pass marks**

| Date | Event | Short passes if | Long passes if | Sources |
|---|---|---|---|---|
| 2026-10-28 (after finals) | Q3'26 | EBITDA < $1,706M, or Wind well below breakeven, or Power < 17% | ≥ $1,706–1,728M with Wind ≥ breakeven and Power ≥ 18% | [S1: MS] [S2: ChartMill] (D07) |
| YE2026 | Gas GW | < 125 GW | ≥ 125 GW | [S1: Q2REL] [S2: Q2 transcript] |
| Late Jan-2027 | FY27 guide | Midpoint ≤ 17.0–17.5% with 2028 held at 20% | Low end ≥ 18% | D04A/B; team picks the mark |
| Late Jan-2027 | 2026 Power backlog-margin change | ≤ +11 points | > +11 points (CEO pre-signalled "larger") | [S1: LAG-PDF p.5] [S2: Exa highlight of same; Q4REL +11] |
| Spring 2027 | CMD | 2028 held at ~$11.2B | 2028 raised toward $12.5–13B | [S1: LAG-PDF p.11] [S2: GuruFocus src:686] |

**Kill rules (research suggestion; the team sets its own):**
- **Short:** FY27 guide low end ≥ 18%, or 2028 framework raised to ≥ ~$12.5B.
- **Long:** FY27 midpoint ≤ 17% with no 2028 raise, or NTM EV/EBITDA ≤ 20x.

**How this changes the brief's lean.**
- The brief's "modest short, 55–60%" holds only for a horizon that ends shortly after the January call. Even there it should be about 55%, not 60%, now that the new-CFO leg is gone.
- At 12 months the evidence supports no directional edge (~50%).

### Q7. Facts that failed the audit (D08 and cross-task findings)

| Fact | Status | What it changes |
|---|---|---|
| "'29 and '30" CEO quote | [SINGLE-SOURCE: LAG-PDF p.10]. Not found in stockanalysis, Seeking Alpha, earningscalls.dev or MarketScreener (paywalled) this session | The short's timing leg (S2) becomes L–M. Leaves the case as "Street above plan", which the brief itself calls fairly priced at ~23x |
| GLJ FY27 $7,420M; Power 18.5% vs "20.7% consensus" | [SINGLE: GF wire; the Yahoo copy is the same text] | Do not cite 20.7% as consensus |
| FY26 EBITDA consensus $6,359M; FY27–28 FCF; Q3 $1,706M | [SINGLE: MS] (ChartMill $1,728M gives Q3 a second source per D07) | FY27 FCF −38% cannot be a headline number |
| NCI $1,158M; $13,695M contract-liability line; −38.3% peak $437.71 | Filing-only, or not re-found | Low impact |
| "Below first numeric guide" | First guides were qualitative and were met; the numeric misses were against mid-year guides (D03, D04B) | Rephrase the margin-record claim |
| "First call under the new CFO" | Contradicted [S1: CFO-PR] [S2: CFOD] | Drop the leg |
| "Never cut" | Company revenue/FCF only. Wind was cut at Q3'25 and the 2028 Wind margin target went from 10% to 6% [S1: 8-K -25-000159] [S2: DEC25] | Qualify |
| 2027 RPO bucket $20,558M | ±$0.64B from rounding; covers all segments | Present as $19.9–21.2B |
| "20 GW run-rate" | Calendar 2027 ≤ ~22 GW [S1: LAG-PDF] [S2: LAG-SA] | FY27 gas volume growth +14% to +26% |
| Prolec margin ~25% | H1'26 actual 22.0% ($296M / $1,346M) [S1: Q2REL organic table per D01B] [S2: pre-deal 25% per deck: this conflicts] | D02's ex-Prolec Electrification margin of 16.3% becomes ~17.2% (§4-A4). D02's derived Prolec revenue ($1,436M) conflicts with the reported $1,346M |
| FY26 EPS basis | GAAP-type $30.49–30.78 vs ex-items $15.16–15.52 | State the basis; FY27 is consistent |
| GLJ's "38.9x" | It is the FY26 multiple | Definition trap |

### Q8. The 20 numbers the team will use

| # | Number | Value | S1 | S2 |
|---|---|---|---|---|
| 1 | Close 2026-09-29 | $962.49 | yfinance quote | Zacks/Yahoo 9/29 |
| 2 | Shares outstanding | 266,333,581 | 10Q balance sheet | yfinance; MS 266,334K |
| 3 | Net cash (cash 13,120 − borrowings 2,849 − NCI 1,158) | $9,113M | 10Q balance sheet | Q2REL "$13.1B cash" (NCI [SINGLE]) |
| 4 | EV | $247.2B | Computed from rows 1–3 | stockanalysis $247.34B |
| 5 | FY25 adj EBITDA / revenue | $3,196M / $38,068M | Q4REL | MS actual; XBRL/stockanalysis |
| 6 | H1'26 revenue / adj EBITDA | $20,442M / $2,146M | Q2REL | 10Q; MS Q1 + Q2 |
| 7 | FY26 guide | $45.5–46.5B; 12–14%; FCF $11.5–12.5B | Q2REL guide box | Kalkine 9/29; Q2 transcript |
| 8 | 2028 framework | $56B; 20%; $11.2B; Power/Elec/Wind 22/22/6 | Q4REL | DEC25 (+ Prolec) |
| 9 | Consensus FY27 adj EBITDA | $9,574M (18.15%) | MS | GF $9.45B |
| 10 | Consensus FY28 adj EBITDA | $13,064M | MS | Motley Fool 60% CAGR → $13,091M |
| 11 | Consensus FY27 revenue | $52,740M | MS | S&P/stockanalysis $52.74B; FactSet $52,632M |
| 12 | Consensus FY27 EPS | $24.85 | MS | FactSet $24.78; S&P $25.13 |
| 13 | Power H1'26 EBITDA / revenue | $1,842M / $10,449M (17.63%) | Q2REL segment table | 10Q MD&A p.29 |
| 14 | Power FY25 EBITDA / revenue | $2,902M / $19,767M (14.68%) | 10K MD&A | FY24 10-K comparative (company-only) |
| 15 | Equipment RPO YE25 → 2027 | $64,245M × 32% = $20,558M (±$0.64B) | 10K Note 9 | Q4'25 call "$64B" |
| 16 | Gas backlog + SRAs | 53 + 63 = 116 GW; ≥125 GW YE26 | Q2REL | Q2 transcript |
| 17 | Output ladder | 5 GW/quarter H2'26 → 6 in H2'27 → 24 GW 2028 | LAG-PDF p.4 | LAG-SA (this session); Q2REL |
| 18 | CSA profitability revisions | FY24 −$319M; FY25 −$151M; H1'26 −$218M | 10Q Note 9 | 10K / FY24 10-K Note 9 |
| 19 | NTM EV/EBITDA today | 28.2x (MS-computed) / 27.7x | MS | Chartloom |
| 20 | Closing drawdowns ≥15% | 5; median −24.6%; max −38.3% | Yahoo chart API | Nasdaq historical (peak $437.71 not re-found) |

### Q9. Ten things to hand-verify before submitting (priority order)

1. **Consensus FY27/FY28 EBITDA from a second full-row vendor** (FactSet, Bloomberg or Visible Alpha on a university terminal). Re-pull price and consensus on the morning of 10-02.
2. **Laguna PDF pp.9–11 in full**, for the exact context of "'29 and '30".
3. **10Q balance-sheet bridge:** cash including restricted, long-term plus current borrowings, NCI, shares. Decide outstanding vs diluted (270M).
4. **Q2REL guide box and Q4REL framework**, including the segment margin targets.
5. **Segment notes:** Power H1'26 and FY25 revenue and EBITDA; recompute 17.63% and 14.68%.
6. **10K Note 9 RPO percentages** (37/69/97); show the rounding band and that the figure covers all segments.
7. **CFO-PR wording on who presents the Q4'26 call.**
8. **Margin-guide history:** 5–7% → 5.5–6%; "HSD" → 8–9%; 11–13% → 12–14%; FY24/FY25 actuals 5.83% / 8.40%.
9. **Event-day closes and drawdown prices from a vendor:** 52-week low $529.18 vs $530.16; record close $1,174.86; +15.62%, −8.69%.
10. **Q2REL organic table (Prolec 22.0%) and 10K Note 1 revenue recognition.** Check whether gas equipment is recognised over time, as D09 claims. My phrase search did not find it, and it changes the "2027 ships a 2024 book" framing.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf |
|---|---|---|---|---|---|---|
| 1 | FY27 research base | $8.6–8.8B | D01A §4 | D01B §4-J; V10 median $8.8B | close | M–H |
| 2 | FY28 research base | $11.0–11.2B | D01A | D01B | close | M |
| 3 | Consensus Power margin needed | 21.7–23.5% | D01A Q11 | D01B §4-L; D04B 23.9% | close | M |
| 4 | P(guide midpoint < 18.15%) | 80–85% | D04A | D04B | close | M (judgement) |
| 5 | Parks presents Jan call | — | CFO-PR | CFOD | exact | H |
| 6 | H2'26 commitments < H1 40 GW | quote | LAG-PDF p.3 | LAG-SA (this session) | exact | H (upgraded) |
| 7 | Wind "2027 much better than 2026" | quote | LAG-PDF | LAG-SA | exact | H |
| 8 | "'29 and '30" quote | quote | LAG-PDF p.10 | not found | SINGLE | M |
| 9 | Prolec H1'26 margin | 22.0% | Q2REL organic table (D01B) | deck 25% pre-deal | conflict (actual vs plan) | M |
| 10 | Company adj TTM EBITDA | $4,115M | Q4REL + Q2REL | 10Q | exact | H |
| 11 | P-pipeline DCF | $190.59 at 4.7% margin | P2 | P5 | exact (same engine) | H that it is wrong |
| 12 | p_long across variants | median 0.46 | V10 A1 | V01–V09 FINAL_BLOCKs | exact | H |
| 13 | CSA revisions | −$218M H1'26 | 10Q Note 9 | 10K Note 9 | exact | H |
| 14 | 52-week low | $529.18 vs $530.16 | yfinance (P1) | Motley Fool (D08) | conflict | M |

---

## 4. Arithmetic

- **A1. EV.** 962.49 × 266.333581M = $256,343M; + 2,849 + 1,158 − 13,120 = **$247,230M**.
  - FinRobot's version: 256,343 + 3,720 − 12,720 = $247,343M.
- **A2. D01 reconciliation.** Power 5,520 − 5,638 = −118; Electrification 3,630 − 3,581 = +49; Wind −100 − 0 = −100; Corporate −450 − (−475) = +25. Sum −144 = 8,600 − 8,744.
- **A3. Equipment margin needed** (services fixed at 24.5% × $14,823M = $3,632M; equipment revenue $12,680M; D01A revenues):
  - Base: (5,638 − 3,632) / 12,680 = **15.8%**.
  - Consensus (23.5% × 27,503 = 6,463): (6,463 − 3,632) / 12,680 = **22.3%**.
  - Versus D06's central H1'26 +3.6%.
- **A4. Electrification ex-Prolec, H1'26.** (1,200 − 296) / (6,597 − 1,346) = 904 / 5,251 = **17.2%** (D02 had 16.3%).
- **A5. Guide to dollars.** 52,740 × 17.0% = 8,966 (−6.4%); × 17.5% = 9,230 (−3.6%); × 18.0% = 9,493 (−0.8%).
  - One point of margin = $527M. × 25 / 266.33 = $49.5/share.
- **A6. Research-path value.**
  - January NTM = 11/12 × 8,700 + 1/12 × 11,100 = **8,900**.
    - 22x: (195,800 + 9,113) / 266.33 = $769.
    - 25x: 231,613 / 266.33 = $870.
    - 28.2x: 260,093 / 266.33 = $977.
  - September NTM = 0.25 × 8,700 + 0.75 × 11,100 = **10,500**.
    - 20x: $823.
    - 22x: $902.
    - 25x: $1,020.
- **A7. Roll-forward value at 25x.**
  - Consensus: January NTM = 11/12 × 9,574 + 1/12 × 13,064 = 9,865; September = 12,191. Δ2,326 × 25 / 266.33 = **+$218**.
  - Research path: Δ(10,500 − 8,900) = 1,600 → **+$150**.
  - Today's NTM is implied as 247,227 / 28.2 ≈ 8,767. The roll from today to January is about +1,098, worth +$103 at 25x.
- **A8. Estimate-gap value.** $0.8–1.0B × 25 / 266.33 = **$75–94/share**. V10 A4 has $88 at 28.2x in a January frame.
- **A9. D04 combined.** Bucket means as in Q3. P(<18%) = 4.5 + 10 + 23.5 + 32 = 70%, plus the part of the 18–19% bucket near 18.0% → ~80–85%.

---

## 5. General question bank

- **G1 / G5.** A flat price for 12 months implies NTM EV/EBITDA of 20.3x on consensus, or about 22.9x on the plan path [D05; V10 G5]. Physically, consensus FY27 needs about 20–22 GW and Power at about 22–23.5% [D01; LAG-SA].
- **G7.** The gap is interpretation and timing, not information; 9/9 variants agree [V10].
- **G8.** The estimate gap is about $60–90/share; one turn of multiple is about $40–46/share; the roll-forward is about $150–218/share at 25x (§4).
- **G13 / G18.** See the Q6 proof-point table and kill rules.
- **G15.** Median drawdown −24.6%; +24% to the 52-week high [BX; D08].
- **G20.** Single-source items: the "'29 and '30" quote, GLJ's figures, FY26 EBITDA consensus and FY27–28 FCF consensus, and D05's peer EBITDA multiples.
- **G24.** Recurring SBC ($257M in FY25) is not added back in adjusted EBITDA [S1: 10K equity statement] [S2: 10Q] (D09).
- **G25.** This session I checked the Laguna quotes against stockanalysis.com by reading the page. Everything else in this note is carried over from tonight's tool outputs.

## 6. What would change this

- **FY27 range:** a second consensus vendor showing FY27 below ~$9.2B would shrink the variant. A disclosed Power equipment/services split would re-anchor the Power path.
- **P(guide < consensus):** consensus drifting down after Q3, or a December 2026 event being announced.
- **Evidence scoring:** full Laguna p.10 context that ties "'29 and '30" to 2026 SRA conversions only would move S2 to L. A PIT multiple series with troughs above 25x would strengthen L1.
- **Direction:** V03/V04 re-run at a fixed 12-month horizon that still split beyond noise.

## 7. Disagreements with the master brief

1. The lean of 55–60% short holds only for a horizon ending around the January call, and even then it is about 55%. At 12 months it is about 50%.
2. "First call under the new CFO" is contradicted by CFO-PR and CFOD.
3. The margin record: the first guides were qualitative and were met. The misses were against mid-year numeric guides.
4. The "'29 and '30" quote is single-source, not verified on the two-source standard.
5. "Never cut" does not cover Wind.
6. Prolec is running at 22.0%, not 25%.
7. The 2027 RPO bucket is a range ($19.9–21.2B) and covers all segments.
8. The brief's §7 "management plan" NTM of $10,794M uses consensus FY27. On a plan-consistent FY27 it is $10,548–10,625M [V10 §7].
9. The brief's short range (−9% to −14% at 25x) leaves out the four-month roll. At a constant 28.2x, the January value on the research path is about $977–991.

## 8. Open items

- A second full-row consensus vendor (FactSet, Bloomberg or Visible Alpha).
- Laguna p.10 in full.
- 10K Note 1, to settle whether gas equipment revenue is recognised over time.
- The 52-week low (intraday vs close).
- A PIT NTM EV/EBITDA series.
- The GLJ full note.
- Whether a December 2026 investor event gets added (GEV IR events page).
- The Q3 10-Q (10-28): RPO percentages, buybacks, the Vineyard Wind settlement cost, and whether CSA revisions sit in Gas or Nuclear.
- A second noise pair for the variant experiment.
- V01–V09 were not re-read directly. If a specific variant figure goes into the model, check it against its own file.
