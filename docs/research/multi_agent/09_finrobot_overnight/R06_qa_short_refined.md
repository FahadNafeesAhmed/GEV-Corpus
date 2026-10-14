# Judge Q&A for the refined short thesis

_R06_qa_short_refined — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 04:51:12. Requests 28, input tokens 1679843, output tokens 32381._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV refined short thesis: the 20 hardest Citadel-PM questions, with the facts to answer each

This is research input only. Nothing below is memo prose, and every range is labelled "team's choice". It builds on F01, E04 and E05, and applies the corrections in R01 (a red-team audit run after F01). New work this session:
- a cushion cross-check against FY26;
- an option-implied volatility (IV) check;
- the odds that the proposed price stop gets hit by noise alone;
- a peer-hedge grid;
- the CFO-transition facts;
- the GLJ thesis as reported by TIKR/Zhitong.

**Source key**
- **Company filings**
  - 10Q = 0001996810-26-000148; 10K = 0001996810-26-000015
  - Q2REL = 0001996810-26-000147 EX-99; Q1REL = -26-000063; Q4REL = -26-000012; Q3'25REL = -25-000159
  - DEC25 = Dec-2025 webcast press release PDF (facts BR-12)
  - PROXY25 = DEF 14A -25-000049 p.54; PROXY26 = DEF 14A -26-000049 p.50
  - CFO-8K = -26-000153 Item 5.02; CFO-PR = gevernova.com release, 2026-08-27
- **Press and conference sources**
  - RTR-CFO = Reuters 2026-08-27; CFOD = CFO Dive 2026-08-28
  - LAG-PDF = GEV-hosted Laguna transcript, 2026-09-16; LAG-SA = stockanalysis/earningscalls copy of the same
  - MB = MarketBeat Laguna write-up, 2026-09-18
  - TIKR = tikr.com, 2026-09-27
- **Market data**
  - MS = MarketScreener, 2026-09-29; GF = GuruFocus GLJ wire, 09-15; CM = ChartMill
  - BX = Yahoo + Nasdaq closes (facts BX-01..13)
  - THETA = thetaowl.com/options/GEV snapshot, 2026-09-23 close
  - POS-03/04 = evidence_lanes_full (built from stockanalysis price histories)

---

## 1. Bottom line

- **Weakness (a) is worse than E04 says.** Last year's pattern gives a fourth cushion reference point:
  - The Street's FY26 EBITDA ($6,359M) is +6.3% above the current FY26 guide midpoint ($5,980M).
  - It is about +14% above the first (Dec-2025) guide midpoint, ex-Prolec (my estimate).
  - If FY27 is guided the same way, a guide midpoint of **15.9%–17.8%** is consistent with the Street's 18.15%.
  - So the pass mark that actually proves the Street is too high is nearer **≤16.5%**. Research put P ≈ 32–36% on that, not the ~80% on "<18.15%".
  - [computed A1; S1: MS; S2: Q2REL guide; DEC25; PROXY25/26]
- **Weakness (b): none of the pre-announced January positives changes FY27 EBITDA mechanically.** The CEO maps the 2026 change in backlog margin to "'29 and '30, largely". The positives can still move the multiple, and the multiple is what the short needs to fall.
  - [S1: LAG-PDF p.10 (VF-02); S2: corpus chunk 246346, "shipping in '29 or '30", undated, speaker untagged]
- **Weakness (c) is quantifiable, and it is large.**
  - Over ~81 sessions to late January, noise is ~27% (implied vol) to ~30% (realised vol).
  - Against a central +4.3% edge, that gives only ~56% probability of profit.
  - A driftless random walk touches the proposed $1,079 price stop before late January with ~**67–70%** probability.
  - [computed A3–A4; S1: BX σ 3.34%; S2: THETA implied move]
- **The Power "variant" rests on a back-solve.**
  - The only published Street FY27 Power margin is GLJ's 20.7%.
  - If that is right, the Power gap versus the builds (20–20.5%) is only ~$55–193M.
  - [S1: D01A §1 / R01 row 2; S2: evidence_brief "20.7% … GLJ's figure only"]
- **CFO facts.**
  - Claire McDonough (ex-Rivian CFO) joins in Nov 2026 and becomes CFO on 1 Jan 2027.
  - Ken Parks stays CFO "through 2026 inclusive of the third and fourth quarter earnings calls", then retires on 2 Apr 2027.
  - So the brief's "first call under the new CFO" is half right.
  - [S1: CFO-8K; S2: CFO-PR; S3: RTR-CFO; CFOD]
- **Consensus FY27 FCF now has a second vendor.** TIKR shows ~$7.4B, against MS $7,417M, i.e. −38% vs FY26. That is a likely headline negative in the same January release.
  - [S1: MS; S2: TIKR 2026-09-27]

---

## 2. Answers: the 20 PM questions

Each entry gives the question, the facts, the weakest point, and the one fact that would most strengthen the answer.

### Weakness (a): guidance cushion

**Q1. "If GEV guides FY27 at 17–19%, haven't you lost?"**
- **Facts**
  - On consensus revenue of $52,740M, a 17–19% range converts to $8,966–10,021M, midpoint $9,493M (−0.8% vs $9,574M) [A2; S1: MS; S2: F01 A7].
  - Four cushion reference points give these "still-consistent" FY27 guide midpoints:

    | Reference point | FY27 midpoint still consistent with consensus |
    |---|---|
    | FY24: actual +1.75% vs bonus target | 17.84% |
    | FY25: actual +10.2% vs bonus target | 16.47% |
    | FY26: Street +6.3% vs current guide midpoint | 17.07% |
    | FY26: Street ≈ +14% vs first guide midpoint (ex-Prolec) | 15.92% |

    [A1; S1: PROXY25 p.54, PROXY26 p.50; S2: Q4REL / 4Q24 release actuals; FY26 inputs from MS, Q2REL, DEC25]
- **Weakest point**
  - n = 3, and the definitions are mixed: bonus targets were dollar figures set against qualitative guides (R01 row 10).
  - FY26 is not delivered yet (H1 margin 10.5%) [10Q; Q2REL].
  - The ex-Prolec figure uses an assumed Prolec margin of 22% (D10 Q7, single research derivation).
- **Would most strengthen:** a sell-side or buy-side note stating the *expected* FY27 guide range before January. If the whisper is already ~17%, a 17% guide is priced in. Not found.

**Q2. "What exact print is your pass mark, and why not just '<18%'?"**
- **Facts**
  - Kill-rule legs (research proposal): low end ≥18%; dollar midpoint ≥ ~$9.4B; 2028 raised to ≥$12.5B [F01 Q5; E02 Q4].
  - Probabilities (research judgement):

    | Guide midpoint | D04A | E02 (shaded) | D04B |
    |---|---|---|---|
    | ≤16.5% | 36% | 32% | — |
    | ≤17.5% | — | ~66% | 65–70% |
    | <18.15% | — | — | ~80% |

    [S1: D04A; S2: E02 J-table / D04B]
  - A cushion-adjusted pass mark (≤ ~16.5–17.1%) turns an ~80% event into a ~⅓ to ⅔ event.
- **Weakest point:** every probability is a subjective scenario weight (R01 row 12).
- **Would most strengthen:** how Street FY26 moved after the Dec-2025 first guide. Did it converge to the 12% midpoint or stay above it? This needs a dated consensus history (FactSet/Visible Alpha). Only today's snapshot is available.

**Q3. "Isn't 18.15% already the post-cushion Street number? The Street always sits above GEV."**
- **Facts**
  - The Street sits above management on every live horizon:
    - FY26: 13.74% vs guide midpoint 13%.
    - H2'26 implied: 16.3% vs 15.0%.
    - FY28 EBITDA: $13,064M vs the $11,200M framework (+16.6%).
    - [S1: MS; S2: Q2REL guide; Q4REL framework; DEC25]
  - If the Street's habitual premium over management is 6–17%, the FY27 guide midpoint consistent with the Street is ~15.5–17.1% [computed: 9,574/1.166 = 8,211 → 15.6%; 9,574/1.063 → 17.1%].
- **Weakest point:** this is an inference from the Street's behaviour, not a disclosed figure. It also means a "miss" versus 18.15% may already be expected.
- **Would most strengthen:** the Street's FY27 revision after the Jan-2026 framework reset (a dated consensus series).

### Weakness (b): bundled positives

**Q4. "January bundles positives. Which of them changes FY27 numbers?"**
- **Facts on each positive**
  - Backlog-margin change "larger than" 2025's +11 pts [S1: LAG-PDF p.5 (PP facts); S2: Q4REL / Q4'25 call for the +11]. The CEO says it "tells you the equipment margins for '29 and '30, largely" [S1: LAG-PDF p.10; S2: chunk 246346, related and undated].
  - ≥125 GW vs 116 GW at Q2 [S1: Q2REL p.1; S2: LAG].
  - $200B backlog "early in 2027" [S1: corpus chunk 468149 (news wire); S2: MB].
  - A buyback, possibly (see Q18).
- **Conclusion from the facts:** none of these moves FY27 EBITDA by construction. All of them feed FY28+ numbers and the multiple.
- **Precedent:** the Jan-2026 call (+11 pts slide plus the inorganic framework step) closed +2.73%; Dec-2025 closed +15.62% the next day [S1: BX-13; S2: Barron's 2025-12-12].
- **Weakest point:** at 25x, value is long-duration, so '29–'30 news can dominate a FY27 trim.
- **Would most strengthen:** the stock's reaction split on 2026-01-28 (backlog slide vs framework). Not separable from public data.

**Q5. "Which January items are negative, so the bundle isn't one-sided?"**
- **Facts**
  - FY27 FCF consensus ~$7.4B vs FY26 guide $11.5–12.5B (−38% vs consensus FY26 $12,017M) [S1: MS; S2: TIKR].
  - Wind: FY25 was cut to ~−$400M and came in at −$598M. FY26 H1 was −$657M against a −$400M full-year guide [S1: Q3'25REL; S2: Q4REL / 10K p.72; H1: 10Q Note 24].
  - CSA profit revisions worsened: FY25 −$151M, H1'26 −$218M [S1: 10Q Note 9; S2: 10K Note 9].
- **Weakest point:** the FCF decline is already in consensus, and GEV has beaten its first FCF guide by 65–89% (facts BR-24). A FY27 FCF guide could therefore land *above* $7.4B.
- **Would most strengthen:** management language on the 2027 down-payment/deposit run-off. Not found in the Laguna copy read.

### Weakness (c): the trade can lose even if the thesis is right

**Q6. "At 3.3% daily vol, why is this a trade and not a coin flip?"**
- **Facts**
  - Realised σ is 3.34%/day, which is 53% annualised [S1: BX; S2: verifier recompute 3.35%, evidence_lanes].
  - THETA's implied move is ±10.8% at 30 DTE (Oct-23 expiry) and ±12.4% at 37 DTE. That implies ~47–49% annualised [A3; SINGLE-SOURCE, see Q20].
  - Horizon noise over ~81 sessions is 26.8–30.1%. With a +4.3% central edge, P(profit) is ≈55.7–56.4% [A3].
  - THETA shows IV Rank 2, i.e. premium near a 1-year low [THETA 09-23].
- **Weakest point:** the normal approximation ignores fat tails. Up-days of +15.62%, +14.58% and +13.75% show the right tail is thick [BX-13].
- **Would most strengthen:** a second IV source and the Jan-2027 expiry implied move. Only near-dated expiries were seen.

**Q7. "Your price stop at $1,079: what is the chance noise alone triggers it before January?"**
- **Facts**
  - The stop is $1,078.8, i.e. consensus rolled at a constant 28.2x (+12.1%) [S1: E02 Q4; S2: R01 §4 reproduction].
  - Driftless barrier-touch probability is **67% (IV) to 70% (realised)** [A4].
  - The drop on the GLJ day was 106% recovered in 11 sessions [S1: BX; S2: Nasdaq closes].
- **Weakest point:** the answer implies either a wider stop (and larger loss) or a smaller position. The 1-sd move is ~$260–290/share.
- **Would most strengthen:** a stop defined on a *fundamental* trigger (the kill rule) rather than price. That is the team's choice; this is the fact that frames it.

**Q8. "Would you pair it? What is left once sector beta is stripped?"**
- **Facts**
  - GLJ day (09-14): GEV −8.6% vs an equal-weight VRT/ETN/ENR basket at −7.76%, so the raw excess is **−0.86 pp** [S1: POS-03 (stockanalysis histories); S2: BX for GEV].
  - 09-11 to 09-29: GEV +0.55% vs basket −0.10% [POS-04].
  - Residual σ grid (optimal-β hedge; ρ not measured):

    | ρ | Residual σ to January |
    |---|---|
    | 0.5 | ~23–26% |
    | 0.7 | ~19–21% |
    | 0.8 | ~16–18% |

    [A5]
- **Weakest point:**
  - ρ has not been computed.
  - Siemens Energy reports on 11-11 with its own mid-term margin update, so the hedge leg carries its own event risk [E07].
  - The competition deliverable is a single-name long/short.
- **Would most strengthen:** the 1-year daily correlation of GEV with VRT/ETN/ENR. The price-data tool failed this session.

### Model and variant

**Q9. "Is the gap really in Power? The only published Street FY27 Power margin is 20.7%."**
- **Facts**
  - D01A back-solves Street Power at 21.5–23.5% (it assumes Electrification at 21–22%). GLJ quotes 20.7% [S1: D01A §1 / R01 row 2; S2: evidence_brief].
  - The builds use 20–20.5%, at ~$275M per point [D01A]. If 20.7% is right, the Power gap is $55–193M [A6].
  - The $0.7–1.0B total gap would then have to sit in Electrification, Wind or Corporate.
- **Weakest point:** this is the single largest vulnerability. The variant's location is inferred, not observed.
- **Would most strengthen:** a paid segment consensus (Visible Alpha / FactSet) for FY27 Power and Electrification.

**Q10. "Has GEV ever delivered the margin step consensus needs?"**
- **Facts**
  - Largest *delivered* annual step: +2.57 pts (FY24 5.83% → FY25 8.40%).
  - The Street already assumes +5.34 pts in FY26 (13.74%) and +4.41 pts in FY27.
  - H1'26 was 10.5%; H2 implied 16.3%.
  - Power margin: 9.88% → 12.51% → 14.68% → 17.63% (Q2'26 18.82%).
  - [S1: 10K; 10Q Note 24; MS; S2: Q4REL / Q2REL segment tables; R01 row 6]
- **Weakest point:** if H2'26 prints ~16%, then FY27 at 18% is mostly carry-forward, not a heroic step (R01 row 6).
- **Would most strengthen:** the Q3'26 actual margin on 10-28. The Q3 Power guide is ~17–18% on a recast Q3'25 base of 13.39% (PP-12).

**Q11. "Your timing evidence: the CEO says '29–'30, the RPO says 2027 is mostly 2025 vintage. Which is it?"**
- **Facts**
  - $64,245M × (69% − 37%) = $20,558M of equipment RPO lands in 2027 [S1: 10K Note 9; S2: Q4'25 call "$64B"].
  - Dollar vintage split of 2027: pre-2025 8–20%; 2025 vintage 47–62%; 2026+ 29–35% [brief §5; evidence_brief].
  - Implied vintage contribution margins: 2024 ~7.5 pts; 2025 ~19–20 pts [brief §5].
  - Management: most higher-margin 2024–25 orders deliver "2027 and beyond" [S1: Q4'25 call (GLJ-12); S2: LAG-PDF p.10 ('29–'30)].
- **Weakest point:** the dollar evidence leans long (2025 vintage dominates 2027 dollars). The margin-share argument (heavy-duty gas has the longest lead times) is qualitative only.
- **Would most strengthen:** Power-only RPO conversion, or the backlog-margin slide by delivery year. Neither is disclosed. Check the Q3 10-Q Note 9.

**Q12. "Aren't you just a softer GLJ? What do you have that GLJ doesn't?"**
- **Facts**
  - GLJ: FY27 $7,420M vs Street ~$9.45–9.5B; $470 target; outside MS's analyst set (MS low target $940) [S1: GF; S2: TIKR "33 targets, $940 low, no Sell"].
  - Per Zhitong via TIKR, GLJ argues:
    - premium orders materialise in 2029;
    - 2026–27 orders ship in 2030–31;
    - industry capacity is 104–113 GW against 88–90 GW of orders.
    - [S1: TIKR; S2: none: **SINGLE-SOURCE**, GLJ note not accessible]
  - ~$1.4–1.5B of GLJ's gap has no public explanation [brief §5].
- **Weakest point:** the refined thesis sides with GLJ on *when* and with consensus on *how much*. A PM will ask which part is proprietary.
- **Would most strengthen:** the GLJ full note (segment build), to show exactly which $0.6–0.9B of the thesis is independent.

### Valuation, tails and management

**Q13. "Why does the multiple fall on a ~5% cut? Isn't that where the money is made?"**
- **Facts**
  - For the price to stay flat into January, NTM EV/EBITDA must go from 28.2x to 25.1x [S1: F01 A1; S2: R01 §4].
  - 2026 NTM troughs: 28.5x, 27.5x and 25.4x (GLJ day) [S1: Chartloom via D05; S2: MS-computed 28.2x].
  - Post-spin NTM P/E range 33.8–68.9x, median 50.8x (Chartloom, not point-in-time).
  - ~$100–110/share of typical short targets is multiple compression [V10 A4; V04 A3].
- **Weakest point:** the de-rating step is the least evidenced link in the causal chain (G10).
- **Would most strengthen:** the multiple change on the one margin-held day (Q2'26, −8.69%), with the estimate revisions separated out. This needs dated consensus.

**Q14. "What does the right tail look like, and how fast does it arrive?"**
- **Facts**
  - J1 (guide ≥18.5%): $1,105 central, $1,181 at 30x (−22.7% to the short).
  - Record close $1,174.86; 52-week high $1,195.94.
  - [S1: E02; BX-08; S2: D08; THETA 52-week high $1,195.94]
  - Three margin-raise days of +13.75% to +15.62% [BX-13].
  - Ratings: 30 Buy / 7 Hold. Bernstein, Baird and Guggenheim reiterated $1,298–1,450 after Laguna [S1: MS; S2: Investing.com 09-17 / 24/7 Wall St. 09-16].
- **Weakest point:** a single +15% day wipes out ~3.5x the central edge.
- **Would most strengthen:** option skew (call vs put IV). Not found.

**Q15. "Q3 prints 10-28, five days after the finals. What does a beat-and-raise do?"**
- **Facts**
  - Q3 consensus EBITDA: $1,706M (MS) / $1,728M (CM). The guide-implied range is $1,535–1,716M [S1: MS; S2: CM, via D07].
  - P(FY26 margin guide raised) ≈ 20–25%, and margin-raise days have gone +10–15% [E05 Q2; BX-13].
  - A clean beat cuts E[short] from +4.3% to ~+0.8% [E02 Q4].
  - Date confirmed [S1: GEV IR events page (E07); S2: Kalkine 09-29]. **Conflict:** THETA lists 2026-10-21, which is wrong.
- **Weakest point:** the step most likely to hurt the short falls *before* the thesis event.
- **Would most strengthen:** evidence that H2 margin commentary is linear. On Laguna the CEO leaned bullish ("very strong" Q3 orders) [LAG p.3; MB].

**Q16. "Who guides in January, and why would they sandbag?"**
- **Facts**
  - Parks presents Q3 and Q4 per the PR. McDonough holds the CFO title from 1 Jan and joined from Rivian [S1: CFO-8K; S2: CFO-PR; RTR-CFO; CFOD].
  - Pay design:
    - AIP EBITDA target set at about the guide midpoint;
    - 2025–27 PSUs on cumulative EBITDA/FCF;
    - 2024–26 PSU targets are first disclosed in the spring-2027 proxy.
    - [S1: PROXY26 pp.46, 53; S2: PROXY25 pp.51, 55]
- **Weakest point:** the new CFO's guiding style is unknown, and the CEO set both the FY26 guide and the framework.
- **Would most strengthen:** McDonough's Rivian guidance record (first guide vs actual). Not researched.

**Q17. "Pricing is rising everywhere. Why doesn't that kill a short?"**
- **Facts**
  - SRAs carry "another 10 to 20 points" and ">20%" of pricing strength [S1: Q4'25 call; S2: Q2'26 call, 07-22].
  - Utility dockets:
    - LG&E/KU all-in cost +53–57% [S1: KY PSC 2025-00045; S2: GridLab].
    - Oglethorpe 7HA.03: $2,316 → $3,226–3,787/kW, same publisher, so M confidence [OPC SEC briefings].
  - 2032 slots are being sold with cash committed, in "single-digit gigawatts" [S1: TIKR; S2: LAG-PDF].
- **Weakest point:** all of this raises FY28+ numbers and supports the multiple. The FY27 argument depends on fixed-price old backlog that cannot be repriced (10K Item 1A; E06 Q6).
- **Would most strengthen:** evidence that Street FY28 ($13,064M, +16.6% vs framework) already capitalises this pricing, which would leave no upside from it.

**Q18. "Can buybacks overwhelm a ~5% estimate cut?"**
- **Facts**
  - $3,037M remained at 6/30. That is ≈3.16M shares, ≈1.18% of shares outstanding [S1: 10Q Note 17 / Part II Item 2; S2: MB (12.4M shares repurchased since inception, avg ~$560)].
  - Program history: $6B announced 2024-12-10; raised to $10B on 2025-12-09 (+$4B ≈ 1.56% of today's market cap) [S1: 10Q p.18; S2: 10Q MD&A liquidity].
  - Q3 buying was signalled ("another good opportunity") [S1: LAG p.9; S2: TIKR].
- **Weakest point:** the size and timing of a new authorisation are unknown. With no December event, it may land in the January release (inference).
- **Would most strengthen:** the Q3 10-Q repurchase table (10-28) and any 2027 capital-allocation framework.

**Q19. "Base rates: GEV on event days, and GE's own 1999–2002 / 2017–19 history?"**
- **Facts**
  - 11 report/event days since the spin; 3 closed down (−4.45%, −1.59%, −8.69%) [S1: evidence_lanes BX; S2: PP-36 Nasdaq + Yahoo].
  - No FY guide has ever been given first on a January call (FY25 and FY26 guides came in December) [S1: DEC25; S2: Dec-2024 update / Reuters 2024-12-11].
  - GE 2000–02: the multiple de-rated 1.5–2 years before earnings fell, and earnings broke only after orders turned [S1: GE 2003 10-K ex13; S2: NY Post 2002-04-16, via E06].
  - Today: 2032 slots selling. The CEO says H2 orders will not run at the 40 GW pace [LAG p.3; TIKR].
- **Weakest point:** the January first-guide event is out of sample, and the historical analogues need an order turn that is not visible.
- **Would most strengthen:** Q3 commitments against the "directionally 20 GW" H2 figure [LAG-SA].

**Q20. "What is single-sourced or a definition trap, and what did you verify by hand?"**
- **Single-sourced**
  - Full-row FY27/FY28 EBITDA consensus: MS only. GLJ's "~$9.5B" is a quote, not a vendor.
  - FY27 Power margin 20.7% (GLJ).
  - Lark's $54.5B FY27 revenue.
  - The "'29 and '30" quote: LAG-PDF only, because the secondary copy truncates.
  - IV: THETA only, and its earnings date is wrong.
  - SE SRA share of 27.4%.
- **Upgraded this session:** FY27 FCF (MS + TIKR).
- **Unverified:** a "Morgan Stanley downgrade to Underweight 8/3" appears only in MarketBeat-family syndication (Lincolnian, Ticker Report, BBNS). Morgan Stanley raised its target to $1,350 (Overweight) on 7/23 and hosted Laguna on 9/16. No independent confirmation was found, so this is likely a data error. Do not cite it.
- **Definition traps**
  - Contract liabilities: 13,695 (cash-flow line) / 14,087–14,088 (Note 9) / 14,170 (current balance sheet).
  - Power revenue: segment note vs MD&A basis.
  - Page numbers in 10Q citations may be off by one (R01 row 17).
- **Weakest point:** the consensus row that anchors the "one number" is effectively single-vendor.
- **Would most strengthen:** a second full-row vendor (FactSet, Bloomberg or Visible Alpha).

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf |
|---|---|---|---|---|---|---|
| 1 | FY27 consensus EBITDA / revenue | 9,574 / 52,740 | MS 09-29 | GF "~$9.45B" (GLJ quoting Street) | close | M |
| 2 | FY26 consensus EBITDA / revenue | 6,359 / 46,282 | MS | — | SINGLE-SOURCE | M |
| 3 | FY26 current guide | $45.5–46.5B; 12–14% | Q2REL | Q1REL raise text | exact | H |
| 4 | FY26 first guide (ex-Prolec) | $41–42B; 11–13% | DEC25 (BR-12) | Q1REL (raise from 11–13%) | exact | H |
| 5 | Bonus EBITDA target vs actual | 2,000/2,035; 2,900/3,196 | PROXY25 p.54; PROXY26 p.50 | 4Q24 / 4Q25 releases | exact | H |
| 6 | FY28 framework vs Street | 11,200 vs 13,064 | Q4REL | MS | derived | H/M |
| 7 | "'29 and '30" backlog-margin mapping | quote | LAG-PDF p.10 | chunk 246346 (related, undated) | directional | L–M |
| 8 | Change in backlog margin '26 > '25 | >+11 pts | LAG-PDF p.5 | Q4REL (+11 FY25) | exact | M-H |
| 9 | CFO transition | McDonough CFO 1-Jan-27; Parks presents Q4; retires 2-Apr-27 | CFO-8K | CFO-PR; RTR-CFO; CFOD | close (title vs presenter) | H |
| 10 | Daily σ | 3.34% | BX | verifier recompute 3.35% | close (same dataset) | M |
| 11 | Implied move 30 / 37 DTE | ±10.8% / ±12.4% | THETA 09-23 | — | SINGLE-SOURCE | L |
| 12 | GLJ-day excess vs basket | −0.86 pp raw | POS-03 | brief says ~−3% | **conflict** (raw vs model-based?) | M |
| 13 | Q3 EBITDA consensus | 1,706 / 1,728 | MS | CM | close | M |
| 14 | Q3 report date | 10-28 | GEV IR (E07) | Kalkine 09-29; THETA says 10-21 (wrong) | conflict (THETA) | H |
| 15 | FY27 FCF consensus | 7,417 / ~7,400 | MS | TIKR 09-27 | close | M |
| 16 | Buyback program | $6B (12/24) → $10B (12/25); $3,037M left | 10Q p.18 | 10Q MD&A liquidity; MB | exact | H |
| 17 | Wind FY25 guide vs actual | ~−400 vs −598 | Q3'25REL | Q4REL / 10K p.72 | exact | H |
| 18 | CSA revisions | −151 FY25; −218 H1'26 | 10Q Note 9 | 10K Note 9 | exact | H |
| 19 | Street Power FY27 margin | 20.7% published; 21.5–23.5% back-solve | evidence_brief (GLJ) | D01A §1 | n/a (derived) | L |
| 20 | Largest delivered margin step | +2.57 pts | 10K | Q4REL | exact | H |
| 21 | Event-day record | 11 days, 3 down | evidence_lanes BX | PP-36 | exact | H |
| 22 | GLJ timing thesis | premium orders 2029; 2026–27 orders ship 2030–31 | TIKR (citing Zhitong) | — | SINGLE-SOURCE | L-M |
| 23 | 2032 slots sold with cash | "single-digit GW" | TIKR | LAG-PDF | close | M |
| 24 | MS rating set: 0 Sell; GLJ Sell outside it | $940 low vs $470 | MS / ad-hoc-news | TIKR; Motley Fool/Webull | conflict (set definition) | H |
| 25 | "MS downgrade to UW 8/3" | unverified | MarketBeat syndication | none independent | not confirmed | L |

---

## 4. Arithmetic

**A1. Cushion equivalents (research estimates; the team chooses its own number)**
- FY26 Street vs current guide midpoint:
  - 46.0B × 13% = 5,980. Street 6,359 / 5,980 = **1.0634**.
  - FY27 equivalent: 9,574 / 1.0634 = 9,003, i.e. 17.07% on 52,740.
- FY26 Street vs first guide midpoint (ex-Prolec):
  - First guide midpoint: 41.5B × 12% = 4,980.
  - Prolec estimate: 3,100 × 22% = 682 (both are assumptions: ~$3.1B from Q2REL; 22% from D10).
  - Street ex-Prolec: 6,359 − 682 = 5,677. Ratio 5,677 / 4,980 = **1.140**.
  - FY27 equivalent: 9,574 / 1.14 = 8,398, i.e. **15.92%**.
- FY24 bonus cushion: 9,574 / 1.0175 = 9,409 (**17.84%**).
- FY25 bonus cushion: 9,574 / 1.102 = 8,688 (**16.47%**).
- FY28 premium: 13,064 / 11,200 = 1.166. Applied to FY27: 9,574 / 1.166 = 8,211 (15.6%).

**A2. Margin guide in dollars (on revenue of 52,740)**
- 17% → 8,966; 18% → 9,493 (−0.8% vs consensus); 19% → 10,021.

**A3. Horizon noise**
- Realised: 3.34% × √81 = 30.1%.
- Implied: σ = 0.108 / (0.798 × √(30/365)) = 0.108 / 0.2288 = 47.2%. The 37-DTE expiry gives 0.124 / (0.798 × 0.3184) = 48.8%. (Assumes expected move ≈ ATM straddle ≈ 0.798σ√t; THETA does not state its method.)
- Implied over 81 sessions: 47.2% × √(81/252) = 26.8%.
- P(profit) ≈ Φ(4.3 / 26.8) = Φ(0.160) = 56.4%; Φ(4.3 / 30.1) = Φ(0.143) = 55.7%.

**A4. Probability of touching the stop (driftless, reflection principle)**
- ln(1,078.8 / 962.49) = 0.1141.
- P = 2 × [1 − Φ(0.1141 / σ_T)]:
  - σ_T 0.268 → 2 × (1 − Φ(0.426)) = 2 × 0.335 = **0.670**.
  - σ_T 0.301 → 2 × (1 − Φ(0.379)) = **0.705**.
- A −4.3% drift in the short's favour lowers this modestly. Not computed exactly.

**A5. Residual volatility after a hedge**
- Residual σ = σ × √(1 − ρ²), applied to 26.8–30.1%:
  - ρ = 0.5 → ×0.866 → 23.2–26.1%.
  - ρ = 0.7 → ×0.714 → 19.1–21.5%.
  - ρ = 0.8 → ×0.6 → 16.1–18.1%.

**A6. Power gap if Street Power is 20.7%**
- (20.7 − 20.5) × 275 = $55M; (20.7 − 20.0) × 275 = $193M.

**A7. Buyback capacity**
- 3,037 / 962.49 = 3.155M shares; / 266.33M = 1.18%.
- Market cap 962.49 × 266.33 = 256,340; the Dec-2025 +$4,000M = 1.56% of it.

**A8. Margin steps**
- FY24 → FY25: 8.40 − 5.83 = 2.57 pts.
- FY26 Street: 6,359 / 46,282 = 13.74%, i.e. +5.34 pts.
- FY27 Street: 18.15 − 13.74 = +4.41 pts.

**A9. FCF**
- 7,417 / 12,017 − 1 = −38.3%.

**A10. Wind**
- 400 / 52,740 = 0.76 pts of FY27 company margin.

---

## 5. General question bank items answered

- **G1:** at a flat price, the stock needs 25.1x NTM EBITDA in January (A1 in F01).
- **G2:** largest delivered margin step is +2.57 pts, vs +4.41 pts needed in FY27 (A8).
- **G4:** the market's story would be falsified by a FY27 guide midpoint well below the cushion-adjusted ~16.5–17.1%, i.e. roughly ≤16.5% (A1).
- **G10:** weakest step is the de-rating (Q13).
- **G13/G14:** the late-January outlook, which is not yet dated. The Q3 print on 10-28 comes before it, and the spring CMD may let the market look through January (E05 Q7).
- **G15:** see Q7 (67–70% chance of touching the stop).
- **G17:** buybacks and the timing of a new authorisation (Q18); the CFO handover (Q16).
- **G20:** see Q20.
- **G22:** see Q1–Q3.
- **G24:** FCF decline and deposits (Q5).

---

## 6. What would change these findings

| Finding | What would overturn it |
|---|---|
| Cushion finding (Q1–Q3) | A dated consensus history showing Street FY26 converged to the first guide after Dec-2025. That would make the cushion adjustment smaller. |
| Noise findings (Q6–Q8) | Jan-2027 implied vol ≲35%, or a measured ρ ≥ 0.8 with the peer basket (a pair then roughly halves the noise). |
| Power variant (Q9) | A paid segment consensus showing Power ≥21.5%, which restores it; or ≤20.7%, which moves it out of Power. |
| Bundled positives (Q4) | A management statement tying the 2026 backlog-margin change to 2027–28 deliveries rather than '29–'30. |

---

## 7. Disagreements with the master brief

1. **CFO.** The Q4 call is presented by Parks while McDonough holds the CFO title (CFO-8K; CFO-PR; RTR-CFO).
2. **GLJ-day excess move.** The brief says ~−3% vs the peer basket; the raw equal-weight basket gives −0.86 pp (POS-03). The −3% may be beta-adjusted. The team should state which method it uses.
3. **"0 Sell".** That holds only for MS's analyst set; GLJ's Sell sits outside it.
4. **Conviction.** The "55–60% short" lean overstates the case for the *trade*. After cushion and noise, P(profit) is ≈56% at the central edge, and less if the pass mark moves to ≤16.5%.
5. **Consensus Power margin.** The brief's "Street 2027–28 margins run ahead of management" holds at company level. The Power-level version rests on a back-solve (Q9).

---

## 8. Open items

1. **GEV/peer correlation and idiosyncratic σ.** Compute from stockanalysis histories for VRT, ETN and ENR. The price-range tool failed this session.
2. **Jan-2027 option implied move and skew.** Needs a second IV source, e.g. CBOE or Market Chameleon.
3. **Dated FY26/FY27 consensus history** around Dec-2025 and Jan-2026 (FactSet or Visible Alpha).
4. **McDonough's Rivian guidance track record.** Check Rivian 8-K earnings releases, 2022–26.
5. **LAG-PDF pp.9–11** in full, to get the context of the "'29 and '30" line.
6. **Q3 10-Q (10-28):** repurchase table, the Note 9 RPO percentages, and any announcement of a December event.
7. **GLJ full note:** the segment build and how it reaches $470.
