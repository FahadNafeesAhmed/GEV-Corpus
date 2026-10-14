# Judge Q&A preparation for both directions

_D09_judge_prep — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 02:40:19. Requests 37, input tokens 2458797, output tokens 35485._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV Q&A preparation for both pitch directions: research input only, as of 2026-09-30

This is research input, not memo text. Every probability is research judgement. Every forecast range is labelled "team's choice". I've written no answer scripts, only the facts an answer would rest on and where it breaks.

**Source key**

| Key | Source |
|---|---|
| REL2Q26 | 8-K 0001996810-26-000147, EX-99 press release, 2026-07-22 |
| 10Q2Q26 | 10-Q 0001996810-26-000148, 2026-07-22 |
| 10K25 | 10-K 0001996810-26-000015, 2026-01-29 |
| REL4Q25 | 8-K 0001996810-26-000012, 2026-01-28 |
| LAG | GEV-hosted Morgan Stanley Laguna transcript PDF, 2026-09-16 |
| MB-LAG | MarketBeat write-up of Laguna, corpus src:681, 2026-09-18 |
| MS | MarketScreener consensus pages, fetched 2026-09-29 |
| GF-GLJ | GuruFocus/Yahoo article on GLJ's initiation, 2026-09-15 |
| BX | Yahoo chart API and Nasdaq historical closes (facts BX-03..08) |

---

## 1. Bottom line

- **The first question in both directions is the gap between the Street and management's plan.**
  - Consensus FY27 adjusted EBITDA is $9,574M (18.15% margin).
  - A straight line from the FY26 guide midpoint ($5,980M) to the 2028 framework ($11.2B) gives about $8.59B.
  - Consensus FY28 of $13,064M is 16.6% above the framework.
  - Sources: [S1: MS] [S2: GF-GLJ, which puts the "Street" at $9.45B, within 1.3%]; framework [S1: REL4Q25] [S2: Prolec news, corpus src:3806].
  - A short has to explain why that gap closes downward in January. A long has to explain why the Street, not management, is right.
- **The single most damaging follow-up for the short is not about evidence. It is the +39% NTM EBITDA roll-forward.**
  - On consensus, the stock is flat at 20.3x NTM in Sep-2027 [computed from MS, §4-A3].
  - So the short needs an estimate cut AND a de-rating. GLJ's 8.6% drop was 106% recovered within about 11 sessions [S1: BX] [S2: Motley Fool, 2026-09-14].
- **The single most damaging follow-up for the long is "what is your variant view?"**
  - A long built on consensus numbers is a pure multiple bet at 38.7x FY27 EPS, about 2x the S&P [S1: MS] [S2: FactSet mean $24.78 via cnyes; D08].
  - The winners' study shows judges press exactly this ("your beat is 16%; why is the upside 63%?", asked of the Baker Hughes team) [S1: winners_playbook §6] [S2: psc-2026-bkr transcript].
- **Correction to the brief: the "new CFO" angle is weaker than stated.** Ken Parks stays CFO "through 2026 inclusive of the third and fourth quarter earnings calls" and the 2026 10-K. McDonough formally becomes CFO on 2027-01-01.
  - Sources: [S1: GEV release, 2026-08-27] [S2: CFO Dive, 2026-08-28] [S3: 8-K 0001996810-26-000153, Item 5.02].
- **New accounting fact that bears on the GLJ "shipping" framing.** Gas equipment revenue and margin are recognised over time, by percentage of completion (costs incurred), not at shipment [S1: 10K25 Note 1, revenue recognition, offset ~250k].
  - So "2027 ships a 2024-priced book" really means 2027 recognises cost-to-date on those contracts. The RPO 1/2/5-year schedule already reflects that [S2: 10K25 Note 9 RPO paragraph, "expected to be recognized within 1, 2, and 5 years"].
- **History cuts both ways.** In the 2001–02 US gas bubble, GE Power Systems earnings kept growing in 2002 (+29%) and fell only in 2003. Cancellations showed up first as termination-fee *income*: a $70M after-tax benefit in Q2'02.
  - Sources: [S1: GE 2003 annual report financial section, SEC 0000797463-04-000012 ex99b] [S2: GE Q2'02 earnings release, SEC 0000040545-02-000031]; order-collapse forecast of 80% or more [S3: GE Power Systems release, 2002-07-23].
  - Implication: a demand turn shows up in orders and SRAs before EBITDA. That makes a 12-month EBITDA-based short harder, and makes orders/SRA conversion the long's key leading indicator.

---

## 2. Answers to the questions

### Q1. What in guidance or consensus must change, and when?

**(a) Facts**

*The FY27 guide event*
- No FY27 guidance exists yet. The FY27 outlook comes on the late-January 2027 call: "We'll also provide you a '27 financial outlook in our January earnings call" [S1: LAG] [S2: InsiderFinance, 2026-09-16, "January 2027 call to provide detailed 2027 guidance and equipment-margin expectations"].
- GEV guides margin in whole-number ranges 1–2 points wide: 5–7%, 8–9%, 11–13%, 12–14% [S1: REL2Q26 guidance box and prior releases] [S2: Dec-2025 investor update; TheFly/TipRanks, 2026-04-22; via D04].
- So consensus of 18.15% is matched only by a guide with a low end of at least 18%. A 17–19% range has an 18.0% midpoint, about $79M below consensus [computed, §4-A5].

*FY26 guide vs consensus*
- The FY26 guide is margin 12–14% on revenue of $45.5–46.5B [S1: REL2Q26] [S2: Reuters, 2026-07-22].
- H2 margins implied by the guide run 13.2–16.9% (midpoint 15.0%), against 16.3% implied by consensus [computed, §4-A4; inputs S1: 10Q2Q26 H1 non-GAAP table] [S2: MS].

*No cushion before January*
- The first FY25 and FY26 guides came at December investor events, each paired with a framework raise. Reaction days were +5.01% (2024-12-11) and +15.62% (2025-12-10) [S1: corpus price table, BR-36] [S2: Proactive and Morningstar, 2025-12-10].
- No December 2026 event is listed. The 2030 outlook waits for a spring-2027 Capital Markets Day [S1: LAG p.10–11] [S2: InsiderFinance, 2026-09-16].

*What each side needs*
- **Short:** a FY27 guide midpoint below 18.15% and no framework raise.
- **Long:** a guide low end of 18% or higher, or a 2028 framework raised to Street levels (about 21.6%) at the spring CMD.

**(b) Weakest point.** GEV's revenue guides tend to land at or above consensus (first guides were beaten by +1.3% in FY24 and +4.3% in FY25) [S1: REL4Q25] [S2: facts BR-21]. So a margin miss can come with an EBITDA-dollar match. A PM will ask: "what if it's 17–19% on $54B?" That is roughly $9.7B, in line.

**(c) Would most strengthen it.** Any management statement on FY27 margin or the phasing of 2027 equipment margin. At the Q3 call (10-28), watch whether management frames 2027 against the 2028 framework.

### Q2. Why is the price move you expect larger than your estimate gap?

**(a) Facts**
- **The price move is the estimate change times the multiple change.**
  - A 10% FY27 cut at a constant 25x gives about −9.6% vs the 25x-consensus value [computed, §4-A6].
  - The same cut plus a de-rating to 22x gives $746 (−22.5% vs $962.49) [computed].
- **GEV has de-rated fast before.**
  - NTM EV/EBITDA troughs: 15.6x (2025-04-04), 22.8x (DeepSeek day), 25.4x (2026-09-14) [S1: Chartloom via D05] [S2: point-in-time P/E cross-checks on Yahoo; D05]. **[Near SINGLE-SOURCE for EV/EBITDA history: only Chartloom.]**
  - Five closing drawdowns of 15% or more; median −24.6% [S1: Yahoo chart API] [S2: Nasdaq historical].
- **Long version.** The upside comes mostly from the roll-forward (+39%), not from a beat.
  - Sep-2027 at 22x on consensus NTM $12,191M is $1,041 (+8.2%) [computed from MS].
  - The consensus target of $1,237 equals about 26.3x NTM [S1: D05, from MS] [S2: TIKR, 2026-09-21].

**(b) Weakest point.**
- Short: the only evidence for de-rating is analogy (own drawdowns, peer multiples). Cautious-guide analogues (−8.69%, −8.6%) partly reversed within days [S1: BX] [S2: Reuters, 2026-07-22].
- Long: the upside rests entirely on the multiple holding at 22x or more, with no beat.

**(c) Would most strengthen it.** A guide-day analogue where GEV (or Siemens Energy) de-rated and did *not* recover within 30 days. None has been found in GEV's 10 earnings days.

### Q3. How do you treat SBC, deposits and cash conversion?

**(a) Facts**
- **SBC (pre-tax):** FY24 $155M, FY25 $257M, H1'26 $135M [S1: 10K25 equity statement] [S2: 10Q2Q26 equity statement].
  - GEV's adjusted EBITDA reconciliation has no general SBC add-back. The separation-cost add-back ($180M FY25, $61M H1'26) includes a "one-time stock option grant" [S1: REL2Q26 footnote (a)] [S2: 8-K Q2'25 release, 0001996810-25-000132, same footnote]. Both sources are the same issuer, so independence is weak.
  - FY25 SBC was 8.0% of adjusted EBITDA; H1'26 was 6.3%. Capitalised at 25x, FY25 SBC is about $24 a share [computed].
- **Deposits.**
  - The H1'26 contract-liability inflow in operating cash flow was $13,695M; OCF was $10,680M; so OCF ex-deposits was −$3,015M [S1: 10Q2Q26 cash-flow statement] [S2: Q2 call on mechanism only: "received a significant amount of down payments"]. The $13,695M line itself is **[SINGLE-SOURCE]** (10-Q only).
  - Current contract liabilities are $39.9B (Power $27.7B) vs cash of $13.1B, about 3.0x [S1: 10Q2Q26 Note 9] [S2: 10K25 Note 9 base $25.8B].
- **Cash conversion.**
  - FCF/adjusted EBITDA: FY25 1.16x; H1'26 4.61x [computed; S1: REL4Q25] [S2: REL2Q26].
  - Consensus FCF falls from FY26 $12,017M to FY27 $7,417M (−38%) [S1: MS] **[SINGLE-SOURCE; stockanalysis/S&P paywalls FY27]**.

**(b) Weakest point.** Deposits are real, non-refundable cash. SRA deposits are "non-refundable" per a third-party customer, Maxim Power [S1: Maxim release, corpus src:232] [S2: corpus src:238 explainer]. A PM can argue net cash of $9.1B belongs to shareholders. Treating it as debt-like takes about $34 a share off at the net-cash line [computed: $9,113M / 266.33M].

**(c) Would most strengthen it.** Q3 10-Q contract-liability roll: whether inflows slow as H2 commitments fall below H1's ~40 GW [LAG p.3; the H1 ~40 GW figure is **SINGLE-SOURCE**].

### Q4. What if management buys back less, or does an acquisition?

**(a) Facts**
- **Buybacks.**
  - H1'26: 4,266,417 shares for $3,645M, average $854.43. Cumulative $6,963M; $3,037M remaining at 6/30 [S1: 10Q2Q26 Part II Item 2 / Note 17] [S2: TradingView, 2026-07-23, Q2 "~2.5M shares for ~$2.3B"].
  - Cumulative plus remaining is $10.0B [computed].
  - The remaining $3,037M at $962.49 buys about 3.16M shares, 1.2% of the share count [computed].
  - The CEO called Q3 "another good opportunity" for buybacks [S1: LAG] [S2: MB-LAG, via D07].
  - Diluted weighted-average shares: 270M in Q2'26 vs 276M in Q2'25 (−2.2%) [S1: 10Q2Q26 Note 18] [S2: release-implied $668M / $2.47 = 270.4M].
- **M&A.**
  - Prolec GE remaining 50% bought for $5,254M cash ($9,656M total consideration). It added about $3.1B of FY26 Electrification revenue and moved the 2028 framework from $52B to $56B [S1: 10Q2Q26 Note 8] [S2: REL2Q26 guidance; src:3806].
  - Intangible amortisation rose to H1 $411M vs $116M [S1: 10Q2Q26 Note 8] **[SINGLE-SOURCE document]**.

**(b) Weakest point.**
- Short: FY26 FCF guide midpoint of $12.0B is about 4.7% of market cap. The company can absorb a drawdown with buybacks [computed].
- Long: M&A raises headline revenue and framework numbers without raising organic margin. The Jan-2026 framework step was entirely Prolec.

**(c) Would most strengthen it.** A new authorisation amount (none since the $10B). Watch the Q3 10-Q Part II Item 2.

### Q5. Why hasn't the market seen your point? Who is on the other side?

**(a) Facts**
- **This is not new information.**
  - GEV publishes margin-in-backlog every January (Power increments +3/+3/+11) [S1: 4Q'25 deck slide 5] [S2: 4Q'24 deck p.6].
  - Analysts asked about vintage timing on the Q4'25 call. Management said: "we will not begin delivering on the majority of the higher margin orders placed in 2024 and 2025 until 2027 and beyond" [S1: Q4'25 transcript, gevernova.com] [S2: corpus src:2660 / trade copies].
- **The other side.**
  - Rating panel: 37 analysts, 24 Strong Buy / 6 Buy / 7 Hold / 0 Sell; mean target $1,237.34 [S1: stockanalysis/S&P] [S2: MS].
  - Short interest: 8.76M shares, 3.29%, days-to-cover 3.6–4.6 [S1: MarketBeat] [S2: stockanalysis/Finviz].
  - Top four holders are about 25.6%, mostly index funds [S1: Longbridge] [S2: MarketBeat 13F alert, 2026-08-23].
  - Hedge-fund holders fell from 118 to 106 in Q2 [Insider Monkey] **[SINGLE-SOURCE]**.
- **No sell-side rebuttal of GLJ's vintage math was found.** Bernstein defended on demand mix: data centres were 38% of Electrification orders [S1: Yahoo, 2026-09-18] [S2: Investing.com, 2026-09-16].

**(b) Weakest point.** The gap is interpretation and timing, not information. "Why would 37 analysts miss something on GEV's own slide?" has no hard answer, only the observation that the Street is 16.6% above the framework.

**(c) Would most strengthen it.** Evidence of how analysts built FY27 Power margin: a sell-side segment model. The "20.7% consensus Power 2027 margin" is GLJ-only [GF-GLJ; **SINGLE-SOURCE**].

### Q6. Is the Power margin climb price, mix or productivity?

**(a) Facts**
- **Power segment EBITDA margin:** 9.88% (FY23), 12.51% (FY24), 14.68% (FY25), 17.63% (H1'26), 18.82% (Q2'26) [S1: 10K25 / 10Q2Q26 segment tables] [S2: REL2Q26; Q2 call "320 basis points to 18.8%"].
- **Not segment mix.** Services share of Power revenue fell from 67.9% to 63.1% [computed from S1: 10K25 Note 24] [S2: 10Q2Q26].
- **Management attribution.**
  - H1'26 MD&A: "primarily at Gas Power due to favorable pricing, higher volume, and increased productivity, partially offset by the impact of inflation" [S1: 10Q2Q26 MD&A].
  - Q3'25 10-Q: "favorable price and increased productivity" [S2: 10-Q 0001996810-25-000160 MD&A].
  - It is not quantified by driver in any filing found.
- **Implied Power equipment EBITDA margin, research grid (team's choice of scenario):** FY23 about −27%, FY25 about −4.8%, H1'26 about +3.6% [S1: D06, from 10K25 Note 24 cost lines] [S2: FY24 10-K 0001996810-25-000011 Note 24].
- **Operating leverage.** Incremental margin was 44.4% from H1'25 to H1'26 [S1: 10Q2Q26] [S2: Q2 call; D02].
- **Offsetting drag.** Net unfavourable CSA profitability changes: FY24 −$319M, FY25 −$151M, H1'26 −$218M [S1: 10K25 Note 9] [S2: 10Q2Q26 Note 9]. Same issuer.

**(b) Weakest point.** The split between price, volume and productivity is undisclosed. Any split the team gives is an estimate, and a PM can call it arbitrary.

**(c) Would most strengthen it.** A peer disclosure. Siemens Energy Gas Services says margin gains come mainly from new-unit backlog [S1: SE CMD deck Nov-2025] [S2: SE pre-close call, 2026-06-29; via D06].

### Q7. What is your kill rule, and when would you know?

**(a) Facts (thresholds are research suggestions; team's choice)**
- **Dated event:** the late-January 2027 Q4 call, with the FY27 outlook [S1: LAG] [S2: InsiderFinance, 2026-09-16].
- **Short kill:** FY27 margin guide low end of 18% or more, or the 2028 framework raised toward about 21.6%. Research-judgement P(midpoint ≥ 18.15%) is about 15% [D04; judgement, not data].
- **Long kill (research suggestion):** FY27 margin midpoint of 17% or less with no framework raise (research-judgement P about 56%) [D04]. Or YE26 gas contracts below 125 GW [S1: REL2Q26 "at least 125 GW"] [S2: Utility Dive, 2026-07-23].
- **Earlier read, Q3 on 10-28** (after the finals): the FY26 margin guide stays at 12–14% vs a raise.

**(b) Weakest point.** January is about four months into a 3–12-month horizon, and the CMD comes later in spring. A long can argue January is noise before the CMD.

**(c) Would most strengthen it.** Confirmation of the January call date. Not yet published. Look for a GEV IR release in early January.

### Q8. What happens at Q3 (2026-10-28)?

**(a) Facts**
- **Date:** 2026-10-28, 7:30am EDT [S1: Kalkine, 2026-09-29] [S2: ChartMill; InsiderFinance].
- **Consensus**
  - Revenue $12.01–12.12B [S1: MS] [S2: ChartMill; Zacks $12.07B].
  - Adjusted EBITDA $1,706M / $1,728M [S1: MS] [S2: ChartMill].
  - EPS $4.08–4.09 on a GAAP basis [S1: Zacks/Yahoo, 2026-09-16] [S2: ChartMill].
  - EPS revisions −1.5% to −2.9% over the last month [S1: ChartMill] [S2: Zacks].
- **The rebuilt guide range ($1,535–1,716M) puts consensus at its top** [D07, from Q2 call segment guides] [S2: REL2Q26].
- **Management framing**
  - "Very strong" Q3 orders [S1: LAG] [S2: TIKR article].
  - H2 commitments of about 20 GW "likely… conservative" [S1: LAG] [S2: TIKR / MB-LAG].
  - Shipments at 5 GW a quarter vs 3.3 GW in Q2 [S1: LAG p.4] [S2: MB-LAG].
- **Past Q3 prints only reaffirmed guidance:** +1.25% and −1.59%. The Q2'26 print closed −8.69% after missing adjusted-EBITDA estimates [S1: corpus prices, BX-13] [S2: Reuters, 2026-07-22, "misses core profit estimates as Wind weakness persists"].
- **The Q3 10-Q prints new data points:**
  - 9/30 RPO conversion percentages
  - Q3 buyback
  - possibly a Vineyard Wind settlement charge (terms confidential) [S1: GEV release, 2026-09-16] [S2: Reuters, 2026-09-16].

**(b) Weakest point.** Q3 comes after the finals, so the team cannot show it. Consensus sitting at the top of the range cuts both ways: a small beat is possible if Wind recovers.

**(c) Would most strengthen it.** Q3 Wind EBITDA. The guide needs about break-even in Q3 and about +$257M across H2 [S1: REL2Q26 Wind table] [S2: New Energy Weekly, 2026-07-23, H1 −$657M].

### Q9. What does the stock's own history say about your downside?

**(a) Facts**
- **Drawdowns:** −38.3% ($437.71 → $270.13, Jan–Mar 2025), −17.5%, −15.0%, −24.6%, and an open −25.5% ($1,174.86 on 6/30 → $874.76 on 9/14). The stock is −18.1% from that peak today [S1: Yahoo chart API] [S2: Nasdaq historical].
- Three of the five drawdowns came while the S&P rose [same sources].
- **Short-side risk:** the 52-week high of $1,195.94 is +24% from here [S1: ad-hoc-news, 2026-08-25] [S2: brief/yfinance].
- **Day moves:** DeepSeek day −21.5%; GLJ day −8.6% [S1: Motley Fool] [S2: BX].
- **Multiple history:** NTM P/E since the spin runs 33.75–68.94x, median 50.85x; today about 46.85x [S1: Chartloom] [S2: Yahoo point-in-time spot checks 49.4x/40.4x; D05]. Chartloom is not point-in-time.

**(b) Weakest point.** Every past drawdown recovered to new highs. The history supports "volatile", not "permanently re-rated".

**(c) Would most strengthen it.** An out-of-sample analogue. GE's multiple went from 42.6x FY01 EPS (Aug-2000) to 21.1x (Apr-2002) while EPS rose 19% [S1: GE 2000/2002 ex-99b on SEC] [S2: NY Post, 2002-04-16; via D05].

### Q10. Did you use AI, and what did you verify by hand?

**(a) Facts.** The competition allows AI for initial research if disclosed, and bans submissions generated by AI (brief §1). Priority hand-checks, each on a filing page:

| Figure | Where to check it |
|---|---|
| Price $962.49 | two feeds [yfinance; Zacks, 2026-09-29] |
| Shares 266,333,581 | 10Q2Q26 cover and balance sheet |
| Net cash bridge ($13,120M cash / $2,849M borrowings / $1,158M NCI) | 10Q2Q26 balance sheet |
| Equipment RPO $64,245M × (69% − 37%) = $20,558M | 10K25 Note 9 |
| H1 contract-liability line $13,695M | 10Q2Q26 cash-flow statement |
| 2028 framework $56B / 20% | REL4Q25 |
| FY27 consensus $9,574M | MS page screenshot, dated |

**(b) Weakest point.** Several decisive inputs are single-source: the CEO's "'29 and '30" quote (LAG p.10 only), the GLJ segment figures (GuruFocus only), and FY27–28 FCF consensus (MS only) [D08]. A PM asking "did you read the transcript yourself?" should get a yes on the page.

**(c) Would most strengthen it.** A team member independently re-reading LAG p.10 and saving the page.

### Q11–Q25. GEV-specific questions a Citadel PM would ask

**Q11. Half of the 116 GW is reservations. What if SRAs don't convert?**
- **(a) Facts**
  - Q2'26: 20 GW signed (18 SRA + 2 orders), 10 GW converted, 3 GW shipped; 53 GW backlog + 63 GW SRAs [S1: REL2Q26] [S2: Utility Dive, 2026-07-23].
  - SRAs are 54.3% of GEV's total vs 27.4% at Siemens Energy (26 of 95 GW) [S1: SE Q3 FY26 presentation p.6] [S2: REL2Q26].
  - RPO excludes orders cancellable "without incurring a substantive penalty" [S1: 10K25 MD&A RPO definition]. Risk factor: "slot reservation agreements may not result in orders" [S2: 10K25 Item 1A].
- **(b) Weak point.** A cumulative SRA conversion rate is not disclosed. Deposits are non-refundable, but the size of deposit relative to turbine price is not public.
- **(c) Strengthen.** Q3/Q4 SRA-to-order conversion GW. Management said more than half of 2031 slots would be sold by YE26 [S1: Utility Dive, 2026-07-23] [S2: thegridreport, 2026-07-23].

**Q12. Can the factory actually deliver 20 → 24 GW?**
- **(a) Facts**
  - 20 GW annual output from Q3'26, 24 GW in 2028, 30 GW by 2030 [S1: REL2Q26] [S2: LinkedIn post by the CEO, 2026-07-22].
  - Q2 shipped 3.3 GW vs 5 GW a quarter targeted for Q3–Q4 [S1: LAG p.4] [S2: MB-LAG].
  - Industry casting bottleneck: GE Aerospace agreed to buy CPP for about $11.75B; "severe casting capacity shortages through 2030" [S1: corpus src:3864, 2026-09-06] [S2: corpus src:3849, 2026-08-30].
- **(b) Weak point.** GEV's specific casting suppliers and exposure are not disclosed. The link is inferred.
- **(c) Strengthen.** Q3 gas units/GW shipped in the Q3 release.

**Q13. Isn't this 2001 again?**
- **(a) Facts**
  - GE Power Systems forecast US gas turbine orders and shipments down "80 percent or more over the next two years" and cut 2,500 jobs [S1: GE release, 2002-07-23].
  - About 46,000 MW of gas projects were shelved or cancelled from Nov-2001 to Sep-2002 [S2: Power Engineering, 2002-09].
  - Power Systems earnings still rose 29% in 2002 before dropping in 2003 [S1: GE 2003 ex99b]. Q2'02 included a $70M after-tax benefit from order terminations [S2: GE Q2'02 release].
  - Today: BNEF says announced expansions lift global output by more than half by 2030, and "today's scarcity could become tomorrow's overcapacity" [BNEF, 2026-09-10] **[SINGLE-SOURCE for the figure]**.
- **(b) Weak point.** Today's buyers are regulated utilities and hyperscalers, not 2001-style merchant IPPs. The analogy's customer mix differs. GE shipped more than 60 GW in 2001 [corpus src:296] **[SINGLE-SOURCE]**.
- **(c) Strengthen.** 2001–02 order data from GE 10-Ks (open item).

**Q14. What does percentage-of-completion accounting do to *when* the old book shows up?**
- **(a) Facts**
  - Equipment revenue is recognised over time as costs are incurred: "percentage of completion method, which is based on our costs incurred to date" [S1: 10K25 Note 1].
  - Liquidated-damages estimates are included in variable consideration [S1: same]. The RPO schedule shows 37%/69%/97% recognised within 1/2/5 years [S2: 10K25 Note 9].
  - Cumulative catch-ups on estimate changes hit current-period margin (the CSA line in Q6).
- **(b) Weak point.** The over-time vs point-in-time split is not disclosed. How much of 2027 margin is already "baked" at YE26 is unknowable from outside.
- **(c) Strengthen.** The 9/30 RPO percentages in the Q3 10-Q.

**Q15. GLJ says 3 points on 2024 orders. Right or wrong?**
- **(a) Facts**
  - GLJ: $470 target; FY27 EBITDA $7,420M vs Street $9.45B [S1: GF-GLJ] [S2: Investing.com, 2026-09-14; TIKR confirms the $470 target].
  - GEV's slide shows the *change* in average backlog contribution margin: +3 (FY24), +11 (FY25) [S1: 4Q'25 deck slide 5] [S2: 4Q'24 deck].
  - Implied 2024-vintage level is about 5.5–7.5 points (research) [vintage_verification; D06].
  - The CEO maps the 2026 change to "'29 and '30" margins [S1: LAG p.10] **[SINGLE-SOURCE passage; MB-LAG gives context only]**.
- **(b) Weak point.** Even the maximum vintage fix explains only about $0.55–0.62B of GLJ's $2.03B gap. About $1.4B has no public explanation.
- **(c) Strengthen.** GLJ's full note (not accessible).

**Q16. Is turbine pricing still rising outside GEV's own words?**
- **(a) Facts**
  - LG&E/KU, same site, GE 7HA: all-in plant cost +53–57% (April 2024 → June 2026), including escalation [S1: KY PSC Case 2025-00045 rebuttal] [S2: KY PSC Order, 2025-10-28].
  - Management: SRAs carry "10 to 20 points" more pricing; H1'26 orders priced more than 20% higher [S1: Q4'25 transcript] [S2: Q2'26 call / stocksfoundry recap].
  - MHI: GTCC OEM margins at booking "improved significantly" [S1: MHI FY2025 Q&A] [S2: D06].
- **(b) Weak point.** The LG&E/KU figure is plant-level cost, not turbine price. Framework customers (Entergy Mississippi, Duke) show flat costs.
- **(c) Strengthen.** A second docket pair with turbine-only pricing.

**Q17. Who else can supply, and are new entrants a threat within 12 months?**
- **(a) Facts**
  - Siemens Energy is "sold-out until FY28", with a 69 GW backlog and lead times of 3 years or more [S1: SE CFO deck, src:3179] [S2: trade press, src:1699].
  - MHI backlog is 35 GW, up from 23 GW [S1: Utility Dive, src:1743] [S2: MHI Q&A]. MHI targets +30% output [DCD, 2026-05-08].
  - Doosan is scaling a 380 MW turbine [Gas Turbine World, 2026-08-11] **[SINGLE-SOURCE]**.
  - The big three hold about 66% of global capacity [BNEF, 2026-09-10].
- **(b) Weak point.** Behind-the-meter substitutes are growing: 29.6 GW of US behind-the-meter gas through 2030, about 88% for data centres, favouring small or aero turbines [S1: Reuters/Enverus, 2026-09-29]. Wärtsilä engines are an example (412 MW Ohio order) [S2: corpus src:3552]. GEV's aeroderivative share of that market is not quantified.
- **(c) Strengthen.** Siemens Energy medium-term framework on 2026-11-11 (pricing and capacity commentary) [facts PP-38].

**Q18. How dependent are you on AI data-centre capex?**
- **(a) Facts**
  - Data centres were 38% of H1'26 Electrification orders ($5B) [S1: Yahoo/Bernstein, 2026-09-18] [S2: Investing.com, 2026-09-16].
  - The 2026-09-14 drop coincided with AI-lab leaders calling for a slowdown [S1: CNBC, 2026-09-14] [S2: Recharge / Motley Fool, 2026-09-14; via V08].
  - The DeepSeek day was −21.5% [BX; Motley Fool].
- **(b) Weak point.** The data-centre share of *gas* orders and SRAs was **not found** (corpus and Exa searched).
- **(c) Strengthen.** A management statement on data-centre GW within the 116 GW.

**Q19. Wind: can it earn +$257M in H2, and what did Vineyard cost?**
- **(a) Facts**
  - The guide is about −$400M for FY26 vs H1 −$657M. The last positive quarter was Q4'24 at +$19M [S1: REL2Q26 / REL4Q25 Wind tables] [S2: New Energy Weekly, 2026-07-23].
  - Wind orders −40% organically [S1: REL2Q26] [S2: Utility Dive, 2026-07-23].
  - About 60% of Onshore equipment RPO is in the US [S1: 10K25 Item 1] [S2: facts RQ-39].
  - Vineyard settled on 2026-09-16 with confidential terms [S1: GEV release] [S2: Reuters].
- **(b) Weak point.** The settlement cost is unknown until the Q3 10-Q.
- **(c) Strengthen.** Q3 Wind EBITDA and any settlement disclosure.

**Q20. Policy: tariffs, Section 232, tax credits?**
- **(a) Facts**
  - 2026 tariff cost estimate cut to $100–200M from $250–350M [S1: 10Q2Q26 MD&A] [S2: Reuters, 2026-07-22].
  - The CEO said Section 232 guidance could bring "order clarity" in H2 [S1: Utility Dive, 2026-07-23] [S2: LAG, via D07].
  - The OBBBA begin-construction deadline of July 4, 2026 has passed. Safe-harboured projects have four years to finish [S1: Latitude Media, 2026-07-06] [S2: Knobbe Martens, 2026-07-20].
- **(b) Weak point.** The net effect of wind safe-harbour demand on GEV onshore orders is not quantified.
- **(c) Strengthen.** Final Section 232 wind rule text and date (open).

**Q21. Walk me from EV to price. Is net cash really yours?**
- **(a) Facts.** EV of $247.2B = 962.49 × 266.33M − $9,113M. Contract liabilities are 3.0x cash (Q3 facts) [S1: 10Q2Q26 balance sheet / Note 9] [S2: yfinance shares 266,333,581; MS 266,334K].
- **(b) Weak point.** The fuller bridge (pension, leases) gives $250.7B. Total debt of $3,720M on yfinance vs $2,849M borrowings reconciles only after about $871M of leases [D08].
- **(c) Strengthen.** A written bridge convention table in the model.

**Q22. Why pay about 2x the market; what are the peers?**
- **(a) Facts.** Calendar-weighted NTM EV/EBITDA [S1: MS valuation pages] [S2: TIKR, 2026-08-25, VRT about 24x, Schneider about 17x]:
  - PWR 22.0x, ETN 21.3x, VRT 20.6x, ABB 19.0x, Schneider 16.4x, MHI 14.7x, Siemens Energy 12.6x
  - GEV 28.2x
- **(b) Weak point.** GEV has the highest EBITDA growth in the set (2-year CAGR about 43%, MS), so a lower multiple needs a growth-adjusted argument.
- **(c) Strengthen.** A growth-adjusted comparison (EV/EBITDA ÷ growth). Siemens Energy is the closest business match at 12.6x.

**Q23. Why did the stock fall 8.7% on a beat-and-raise in July?**
- **(a) Facts.** Adjusted core profit missed estimates on Wind losses; the margin guide was held; the FCF guide was raised by $5B at the midpoint [S1: Reuters, 2026-07-22] [S2: REL2Q26; D07]. Two of seven raise days closed lower [S1: corpus prices] [S2: Yahoo].
- **(b) Weak point.** The next day reversed +4.69% [D04].
- **(c) Strengthen.** None needed. It is a base-rate fact.

**Q24. Management's discretion: what could break your thesis from inside?**
- **(a) Facts**
  - 2025 bonus targets paid 200% on FCF, 130% on EBITDA and 178% on growth [S1: DEF 14A 0001996810-26-000049] **[SINGLE-SOURCE for targets]**; actuals [S2: REL4Q25].
  - Frameworks were raised organically at December events in both 2024 (+4 points) and 2025 (+6 points) [S1: Dec-2024/2025 investor PDFs] [S2: Morningstar, 2025-12-10].
- **(b) Weak point.** For the short: management can pull a framework raise forward or add a December event. For the long: a new CMD could re-base at the 2030 horizon.
- **(c) Strengthen.** IR events page checked weekly for any December event.

**Q25. Where does the multiple go if rates stay at 5%+?**
- **(a) Facts.** The 10-year went from 4.34% (April) to 5.24% (9/28), and the Fed hiked 25bp on 9/16 [S1: FRED DGS10] [S2: Fed release; facts RQ-28]. GEV rose from $874.76 to $962.49 over 9/14–9/29 [S1: BX] [S2: Zacks, 2026-09-29].
- **(b) Weak point.** Rate sensitivity cannot be isolated because AI and GLJ co-drivers were present at the same time [D05].
- **(c) Strengthen.** A rolling regression of GEV on the 10-year (not done).

### Ranked question lists by direction (likelihood × damage; H/M/L is research judgement)

**SHORT version: 25 hardest questions**

| # | Question | Facts in | Short-specific weak point | Best strengthener |
|---|---|---|---|---|
| 1 | The roll-forward is +39%; how do you make money over 12 months? | Q2, §4-A3 | Needs a de-rating to about 20x on consensus | Evidence for a de-rating trigger |
| 2 | What must change, and when? | Q1 | A 17–19% guide on higher revenue is about in-line | Management 2027 phasing language |
| 3 | Management has never cut; why now? | Q24, Q1 | Six raises vs zero cuts | No December event (Q1) |
| 4 | 37 analysts, 0 Sells; what do they miss? | Q5 | Interpretation, not information | A sell-side segment build |
| 5 | Your CEO quote is one page; did you verify it? | Q10, Q15 | [SINGLE-SOURCE] LAG p.10 | Saved page, re-read |
| 6 | GLJ's drop fully reversed; why is your short different? | Q9, Q2 | 106% recovery | Dated company event (Jan) vs a note |
| 7 | Kill rule? | Q7 | January is 4 months in; the CMD later | Call date |
| 8 | Buybacks of $12B FCF | Q4 | 4.7% of market cap | Q3 buyback size |
| 9 | Squeeze or takeover risk? | Q5 | Short interest 3.29%, DTC up to 4.6 | Borrow cost (not found) |
| 10 | Pricing +20% on new orders; isn't that bullish? | Q16 | Supports direction | Timing of recognition (Q14) |
| 11 | POC recognises margin during build; doesn't 2025 margin show in 2027? | Q14 | Undisclosed over-time share | 9/30 RPO data |
| 12 | Deposits are non-refundable cash; why penalise them? | Q3 | Net cash is real | FY27 FCF drop (single-source) |
| 13 | What if Q3 beats and raises the margin guide? | Q8 | Q1'26 raise day was +13.75% | Wind Q3 |
| 14 | Your downside is below GLJ's; what multiple and why? | Q9, Q22 | Peers at 20–22x | Own trough 15.6x (single-source) |
| 15 | New CFO kitchen-sink? | Q1 | Parks presents | — |
| 16 | Power margin is price and productivity, which persist | Q6 | Undisclosed split | SE peer read |
| 17 | SRAs lock 2030–31 pricing; the story extends | Q11 | Supports long duration | Conversion data |
| 18 | Electrification +29% organic offsets Power | Q18 | Clean growth | Ex-Prolec margin 16.3% |
| 19 | Rates were already 5% and the stock rose | Q25 | Counter-evidence | — |
| 20 | Wind upside if H2 improves | Q19 | CEO: "much better" | Q3 print |
| 21 | Spring CMD 2030 raise | Q24 | Framework raise history | Timing: CMD after January |
| 22 | SBC treatment | Q3 | Small (6–8% of EBITDA) | — |
| 23 | Tariff tailwind (estimate cut) | Q20 | Lower cost | — |
| 24 | Competitors sold out, so no price war | Q17 | Supports pricing | BNEF oversupply by 2030 |
| 25 | Did you use AI? | Q10 | — | Hand-verification list |

**LONG version: 25 hardest questions**

| # | Question | Facts in | Long-specific weak point | Best strengthener |
|---|---|---|---|---|
| 1 | What is your variant view vs consensus? | Q5, Q2 | None: consensus numbers | A line-item beat source |
| 2 | Street FY28 is +16.6% above management; why believe it? | Q1, Q24 | Needs a framework raise | CMD timing / December event |
| 3 | Your upside is all multiple; what supports 22x+? | Q2, Q22 | Peers at 12.6–22x | Growth-adjusted comp |
| 4 | CEO says margin step is '29–'30; FY27 consensus Power about 22%? | Q15, Q6 | Management timing contradicts the Street | Management 2027 language |
| 5 | GEV never beat its first margin guide | Q1 | FY24 and FY25 both below midpoint | H2'26 delivery |
| 6 | January guide below 18%: what's your downside? | Q7, Q9 | Analogues −8.6% to −8.7% | Reversal history |
| 7 | FCF is deposits; FY27 FCF −38% | Q3 | Single-source FY27 | Q3 CL roll |
| 8 | AI capex slowdown? | Q18 | DeepSeek −21.5% | Gas data-centre share (not found) |
| 9 | 54% SRAs vs 27% at Siemens Energy | Q11 | Conversion undisclosed | Q3/Q4 conversion |
| 10 | 2001 analogy | Q13 | Orders turn before EBITDA | Customer-mix evidence |
| 11 | 2x the market multiple | Q22 | Valvoline precedent | — |
| 12 | Factory ramp 3.3 → 5 GW a quarter | Q12 | Casting bottleneck | Q3 GW shipped |
| 13 | Consensus Q3 sits at the top of the range | Q8 | Beat hard | Wind |
| 14 | GLJ's $7.4B; what's unexplained? | Q15 | About $1.4B | GLJ full note |
| 15 | Kill rule | Q7 | 125 GW / January | — |
| 16 | New entrants and behind-the-meter substitutes | Q17 | 29.6 GW behind-the-meter | Aero share |
| 17 | Wind losses and Vineyard | Q19 | Confidential terms | Q3 10-Q |
| 18 | Rates at 5.24% | Q25 | Unisolated | — |
| 19 | Price, mix or productivity? | Q6 | Undisclosed | — |
| 20 | M&A inflates the framework | Q4 | Prolec was the Jan step | — |
| 21 | Hedge funds exiting (118 → 106) | Q5 | Single-source | 13F Q3 (Nov) |
| 22 | EV bridge and net cash | Q21 | Contract liabilities 3x cash | — |
| 23 | SBC treatment | Q3 | Option grant in add-back | — |
| 24 | Tariffs / Section 232 | Q20 | Wind exposure | Rule text |
| 25 | Did you use AI? | Q10 | — | — |

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | FY27 consensus adjusted EBITDA | $9,574M | MS, 2026-09-29 | GF-GLJ "Street $9.45B", 2026-09-15 | close (1.3%) | M |
| 2 | 2028 framework | $56B / 20% | REL4Q25 | corpus src:3806, 2026-06-22 | exact | H |
| 3 | FY28 consensus EBITDA | $13,064M | MS | Motley Fool "60% CAGR", 2026-09-29 | close | M |
| 4 | January FY27 outlook | Q4 call | LAG | InsiderFinance, 2026-09-16 | exact | H |
| 5 | Parks presents Q4 call | through the 10-K | GEV release, 2026-08-27 | CFO Dive, 2026-08-28 | exact | H |
| 6 | Q3 date | 2026-10-28 | Kalkine, 2026-09-29 | ChartMill | exact | H |
| 7 | Q3 consensus EBITDA | $1,706M / $1,728M | MS | ChartMill | close | M |
| 8 | POC over-time recognition | cost-to-date | 10K25 Note 1 | 10K25 Note 9 RPO timing | consistent (same doc) | H (single document) |
| 9 | SRA deposits non-refundable | yes (Maxim) | Maxim release, src:232 | src:238 | exact | M |
| 10 | Power H1'26 drivers | price, volume, productivity | 10Q2Q26 MD&A | 10-Q -25-000160 MD&A | consistent | H (same issuer) |
| 11 | Tariff cost 2026 | $100–200M | 10Q2Q26 MD&A | Reuters, 2026-07-22 | exact | H |
| 12 | Wind orders | −40% | REL2Q26 | Utility Dive, 2026-07-23 | exact | H |
| 13 | Vineyard settlement | confidential | GEV release, 2026-09-16 | Reuters, 2026-09-16 | exact | H |
| 14 | H1 buyback | $3,645M; $3,037M left | 10Q2Q26 Part II | TradingView, 2026-07-23 (Q2 $2.3B) | close | H |
| 15 | SBC FY25 | $257M | 10K25 | 10Q2Q26 comparative | exact | H |
| 16 | H1 contract-liability inflow | $13,695M | 10Q2Q26 cash-flow statement | — | [SINGLE-SOURCE] | M |
| 17 | Short interest | 3.29% | MarketBeat | stockanalysis | exact | H |
| 18 | Drawdowns | median −24.6% | Yahoo | Nasdaq | exact | H |
| 19 | GE 2002: US orders −80%+ | forecast | GE release, 2002-07-23 | Power Eng. 46 GW cancelled | consistent | M |
| 20 | GE Q2'02 termination benefit | $70M after-tax | SEC 0000040545-02-000031 | GE 2003 ex99b (earnings peak 2002) | consistent | M |
| 21 | Big three capacity share | ~66% | BNEF, 2026-09-10 | — | [SINGLE-SOURCE] | M |
| 22 | Behind-the-meter gas to 2030 | 29.6 GW, 88% data centres | Reuters/Enverus, 2026-09-29 | — | [SINGLE-SOURCE] | M |
| 23 | Data centres share of Electrification orders | 38% | Yahoo, 2026-09-18 | Investing.com, 2026-09-16 | exact | H |
| 24 | Casting shortage through 2030 | industry | src:3864 | src:3849 | consistent (GEV link unverified) | L |
| 25 | CEO "'29 and '30" | timing | LAG p.10 | — | [SINGLE-SOURCE] | M |
| 26 | OBBBA deadline passed | 2026-07-04 | Latitude Media | Knobbe Martens | exact | H |

---

## 4. Arithmetic

- **A1. EV.** 962.49 × 266.33M = $256,340M; minus net cash $9,113M = $247,227M.
  - Inputs: yfinance/Zacks price; 10Q2Q26 balance sheet.
- **A2. Straight-line FY27.** (5,980 + 11,200) / 2 = $8,590M.
  - At 25x: (214,750 + 9,113) / 266.33 = $840.5 (−12.7%).
- **A3. Sep-2027 on consensus.**
  - NTM = 0.25 × 9,574 + 0.75 × 13,064 = $12,191M.
  - At 22x: (268,202 + 9,113) / 266.33 = $1,041.2 (+8.2%).
  - Breakeven multiple: (256,340 − 9,113) / 12,191 = 20.3x.
  - Roll-forward: 12,191 / 8,770 = +39.0%, where today's NTM is 0.25 × 6,359 + 0.75 × 9,574 = 8,770.
- **A4. H2 margins.**
  - Consensus: (6,359 − 2,146) / (46,282 − 20,442) = 4,213 / 25,840 = 16.30%.
  - Guide midpoint: (5,980 − 2,146) / 25,558 = 15.0%.
- **A5. 17–19% guide.** 18.0% vs 18.15% on $52,740M revenue = −$79M.
- **A6. Estimate × multiple.**
  - 25x consensus: (239,350 + 9,113) / 266.33 = $932.9.
  - −10% EBITDA at 25x: (215,415 + 9,113) / 266.33 = $843.0 (−9.6% vs $932.9).
  - −10% at 22x: (22 × 8,616.6 + 9,113) / 266.33 = $746.0 (−22.5% vs $962.49).
- **A7. Buyback capacity.**
  - $3,037M / $962.49 = 3.155M shares = 1.18% of 266.33M.
  - FY26 FCF midpoint $12,000M / $256,340M = 4.7%.
- **A8. SBC.**
  - 257 / 3,196 = 8.0%; 135 / 2,146 = 6.3%.
  - 257 × 25 / 266.33 = $24.1 a share.
- **A9. Deposits.**
  - OCF ex-deposits: 10,680 − 13,695 = −$3,015M.
  - Contract liabilities / cash: (27,679 + 9,113 + 3,150) / 13,120 = 3.04x.
- **A10. Wind H2 need.** −400 − (−657) = +$257M.
- **A11. 2027 RPO slice.** 64,245 × (0.69 − 0.37) = $20,558M, ±~$0.64B from rounding.
- **A12. GLJ multiple.** (470 × 266.33 − 9,113) / 7,420 = (125,175 − 9,113) / 7,420 = 15.6x.
- **A13. Diluted shares.** 270 / 276 − 1 = −2.2%.

---

## 5. General question bank items answered along the way

- **G1.** Holding $962.49 at 20.3x in Sep-2027 needs consensus FY28 of $13.1B (21.6% margin on $60.5B), plus gas output of about 20–24 GW (A3; REL2Q26; LAG).
- **G5.** If the stock is flat for 12 months on consensus, the multiple compresses from 28.2x to about 20.3x NTM (A3).
- **G12.** Over-time recognition by percentage of completion means margin arrives as costs are incurred, not at shipment (Q14).
- **G14.** The spring-2027 CMD could push the reveal past January for a long thesis (Q1).
- **G16.** Behind-the-meter substitution and the casting bottleneck are under-discussed (Q12, Q17).
- **G19.** In 2001–02, earnings lagged orders by about one year; the multiple halved while EPS rose (Q13, Q9).
- **G20.** Single-source items: LAG p.10, GLJ segment figures, FY27–28 FCF, the $13,695M line, BNEF capacity share, Chartloom multiple history.
- **G24.** See Q3.

---

## 6. What would change this

- **Street-vs-management gap (the short's core).** A management 2027 margin statement at 18% or higher, or a December event with a framework raise. Either would erase it.
- **The long's "no variant view" problem.** Evidence that FY27 revenue or pricing beats consensus by more than 5%, for example Q3 orders plus pricing disclosures.
- **The POC timing point.** If Q3 10-Q RPO percentages show faster conversion (a higher 1-year share), more 2025-vintage margin lands in 2027, which weakens the short.
- **The 2001 analogy.** Evidence that SRAs are predominantly utility-backed (regulated) rather than merchant or hyperscaler-speculative would weaken it.

---

## 7. Disagreements with the master brief

1. **CFO.** Parks, not McDonough, presents the Q4 call and the FY27 outlook. The brief's "first under the new CFO" is inaccurate in substance (GEV release 2026-08-27; CFO Dive).
2. **Shipping vs recognition.** The brief and GLJ talk about what "2027 ships". Gas equipment is recognised over time by percentage of completion (10K25 Note 1), so the right term is "recognises". The RPO schedule already embeds this.
3. **GLJ day.** The brief attributes the 9/14 drop to a sector and yield move. The same day also carried AI-lab slowdown comments (CNBC/Recharge via V08), which argues for an AI-sentiment channel, not just rates.
4. **Drawdown 5.** The −25.5% drawdown is still open (the stock is −18.1% from peak), not closed (facts BX-08).

---

## 8. Open items

- **Gas-specific data-centre share of orders and SRAs.** Not found. Check the Q3 call (10-28) and the Q4'25 deck.
- **GEV's casting suppliers and CPP exposure.** Check the 10-K supplier-concentration risk factor and ask IR.
- **SRA deposit size and cumulative conversion rate.** Not disclosed. Look in utility dockets (KY PSC, Georgia PSC) for reservation fees relative to turbine price.
- **GE 2001 GW shipped (>60 GW) and GE Power 2017–19 analogue.** Single-source or not researched. Check GE 10-Ks for 2001–2003 and 2017–2019 on EDGAR (CIK 40545).
- **Borrow cost for a short.** Not found. Check a broker or IBKR stock-loan data.
- **Rolling beta of GEV to the 10-year yield.** Not computed.
- **GLJ full note.** Still inaccessible.
