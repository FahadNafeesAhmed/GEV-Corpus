# Kill-rule and pass-mark design for Q3 (10-28) and January

_R07_kill_rules — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 04:56:42. Requests 22, input tokens 1301372, output tokens 29676._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV kill rules, pass marks and price stops for the two candidate pitches (research input; the team sets every threshold)

## 1. Bottom line

- **A kill rule based on the FY27 margin guide alone cannot tell "thesis right" from "thesis wrong".** Management has historically beaten its own guides, so a guide below consensus can still be consistent with consensus being met. That cushion is wider than E04 found.
  - E04's two completed years: actual adj EBITDA beat the bonus target (set at about the guide midpoint) by +1.75% (FY24) and +10.2% (FY25) [S1: DEF 14A 0001996810-25-000049 p.54; DEF 14A 0001996810-26-000049 p.50] [S2: 4Q24 release 0001996810-25-000004; 4Q25 release 0001996810-26-000012].
  - FY26 adds a third, larger data point. The January 2026 guide midpoint was $5,340M ($44.5B × 12%). The current guide midpoint is $5,980M, which is +12.0%. Consensus is $6,359M, which is +19.1% [S1: 0001996810-26-000012 EX-99 "expects revenue of $44-$45 billion… 11%-13%"] [S2: news corpus src:27, 2026-01-23; current guide from Q2REL 0001996810-26-000147; consensus from MS and ChartMill $6.4B].
  - Dividing consensus FY27 ($9,574M) by these cushions gives the guide midpoint that would still be consistent with consensus: $9,409M, $8,688M, $8,548M and $8,039M. On consensus revenue that is 17.84%, 16.47%, 16.21% and 15.24%.
- **The research proposal is a three-zone January test, measured in dollars, not margin points.** Dollars = revenue-guide midpoint × margin-guide midpoint.
  - Thesis-wrong zone (short killed): midpoint ≥ ~$9.4B.
  - Ambiguous zone: ~$8.55–9.4B.
  - Thesis-right zone: ≤ ~$8.55B, i.e. below every observed cushion except the FY26 consensus-implied one.
  - Mapped onto D04B's margin distribution, this gives roughly 35% / 45% / 20% (research judgement; see A3). **About half the time the January call will not settle the thesis.** A second dated test is needed: the 2028 framework at the January call or the spring CMD.
- **The Q3 print on 2026-10-28 is a gate, not a verdict.** The line that has moved the stock is the company margin guide.
  - The three margin or framework raise days closed +13.75%, +14.58% and +15.62%. Q2'26, a revenue and FCF raise with the margin guide held, closed −8.69% [S1: BX-13, Yahoo/Nasdaq closes] [S2: D07 citing Reuters/MoneyTimes 2026-07-22; Barron's 2025-12-12].
  - Pass marks should sit on the FY26 margin guide, Q3 EBITDA against the guide-implied $1,535–1,716M, and Q3 Power margin against the 17–18% Q3 guide.
- **Volatility check.** Since-spin daily σ is 3.34% (53% annualised) [S1: BX series] [S2: verifier 3.35%]. The 30-day close-to-close figure is 47.1% on 09-25 [S1: alphaquery] and the 20-day figure 50.3% on 09-16 [S2: thetaOwl]. Implied vol is about 45% (alphaquery 30-day mean IV 45.2%); the thetaOwl expected-move curve implies about 45–49%.
  - Over the 81 sessions to late January, that is 26.6–30.1% of 1σ noise.
- **F01's $1,079 short stop (+12.1%) gets hit before January about 62–70% of the time under zero-drift noise alone** [computed A5]. A stop that pure noise hits only ~1/3 of the time sits at about +30–34% ($1,250–1,290). That is above the 52-week high of $1,195.94 and about 7x the central expected gain of +4.3% (E02). A pure price stop does not fit a thin edge, so the realistic choices are thesis-event exits plus sizing or defined-risk structures (options below).
- **For a 12-month long, any stop between −15% and −30% gets hit 45–76% of the time under noise alone** [computed A6]. Two of the five post-spin drawdowns (−24.6% and −25.5%) would have triggered a −25% stop [S1: BX-07/08, Yahoo chart] [S2: Nasdaq historical, 626 sessions agree].

## 2. Answers to the assignment

### Q1. Kill rules and pass marks: SHORT into the late-January 2027 FY27 outlook

**Checkpoint 0: 10-23 finals.** Nothing is reported before the finals. Every rule has to be pre-committed without seeing Q3.

**Checkpoint 1: Q3'26 on 10-28, 7:30 ET.** FOMC is the same day and megacap reports fall around it, so noise stacks up [S1: GEV events page] [S2: earningscountdown, via F01].

| Line | Short pass mark | Neutral | Short kill / warning | Why this threshold |
|---|---|---|---|---|
| FY26 adj EBITDA margin guide (12–14%) | Held at 12–14%, or "low half" language | Held, plus "upper half" | **Range raised** (e.g. to 13–14% or higher) | All three raise days closed +13.75% to +15.62% [BX-13; D07]. Consensus 13.74% already sits 86% up the guide's dollar range [D07 Q2]. A raise to 13–14% implies a 15.9% H2 margin, which ratifies consensus (16.3%). A range above that beats it (A4) |
| Q3 adj EBITDA vs consensus $1,706M (MS) / $1,728M (ChartMill) | ≤ ~$1,625M (the guide-implied midpoint) | $1,625–1,760M | ≥ ~$1,800M (about $85M above the guide-implied top of $1,716M) | Consensus already sits at the top of the range rebuilt from segment guides [S1: D07 Q2 rebuild from the Q2'26 transcript] [S2: MS / ChartMill]. A print above the top of the guide is the only one that signals margin upside the guide does not already contain. The $1,800M level is a research choice |
| Q3 Power segment EBITDA margin (guide 17–18%; Q2'26 18.82%) | ≤ 18.0% (inside the guide) | 18–19.5% | ≥ ~19.5% | Guide [S1: news corpus src:3801, 2026-07-22] [S2: src:1016, 2026-07-22]. Consensus FY27 Power margin is 21.7–23.5% in the D01A/B builds, or 20.7% per GLJ (**conflict**, see §7). A Q3 at ≥19.5% plus a seasonally stronger Q4 would leave an exit rate within ~2 points of 21.7%, which weakens the "above trend" argument |
| December investor event announced on the call | None announced | — | Announced | The Dec-2025 event was flagged on the Q3'25 call [E05 Q7]. December event days closed +5.01% and +15.62% [BX-13]. Research P ≈ 10% |
| Q3 10-Q equipment RPO conversion % at 9/30 | Share due within 2 years flat or down | — | Up materially | This refreshes the $20.6B estimate of 2027 equipment revenue (10-K Note 9). It is a secondary line because dollar share is not margin share (brief §5) |

**Checkpoint 2: late-January 2027, Q4'26 results plus the FY27 outlook.** The date is not announced. Past January calls were 2025-01-22 and 2026-01-28. Per D04B, Parks, not McDonough, presents.

| Line | Kill (thesis wrong) | Ambiguous (no read) | Pass (thesis right) | Why |
|---|---|---|---|---|
| **FY27 adj EBITDA guide midpoint, in dollars** | **≥ $9.4B** | $8.55–9.4B | **≤ $8.55B** | $9,409M = 9,574 / 1.0175, the smallest historical cushion. At or above it, consensus is met even on the least conservative guiding GEV has shown. $8,548M = 9,574 / 1.12, which is below both completed-year cushions and FY26's guide-to-guide raise. Only the FY26 consensus-implied +19.1% would reconcile a lower guide with consensus. Dollars rather than margin, because a revenue-led guide (e.g. $54.5B, Lark) at 17.5% is only −0.4% below consensus [E05 A2] |
| Same test expressed as a margin on consensus revenue of $52,740M | ≥ 17.84% | 16.2–17.84% | ≤ 16.2% | Only valid if the revenue guide ≈ $52.7B. Otherwise use the dollar row |
| 2028 framework ($56B / 20% = $11.2B) | Raised to **≥ ~$12.3–12.5B** | $11.5–12.3B | Held at ≤ $11.5B | $12.32B = 22% × $56B. $12.5B closes ~80% of the 16.6% gap to FY28 consensus of $13,064M. A held framework keeps FY28 consensus ~17% above the plan [S1: Q4REL framework] [S2: DEC25 release] |
| FY27 Power segment margin guide (if given) | Midpoint ≥ 21.5% | 20.5–21.5% | ≤ 20.5% | The builds put consensus at 21.7–23.5% and GLJ puts it at 20.7%, so the pass mark sits below both. Each Power point is worth ~$275M (D01A) |
| Q4'26 adj EBITDA margin (reported the same day) | ≥ 18.5% | 17.5–18.5% | ≤ 17.5% | Consensus implies Q4 at 18.1% [D07 Q2], about equal to FY27 consensus of 18.15%. Caveat: next-year vs prior-Q4 margin is not stable. FY25 came in 1.8 points *below* Q4'24's 10.2%. FY26 consensus sits 3.1 points *above* Q4'25's 10.6% [S1: 0001996810-25-000004; 0001996810-26-000012] [S2: 10-K FY figures]. Use this line only as corroboration |

**Bundled positives (E05) and how to pre-commit to them.** These are all expected on the January call:
- Power backlog-margin change "larger" than +11 points [LAG p.5];
- gas at ≥125 GW;
- backlog at $200B;
- a likely new buyback authorisation (research P ≈ 50–60%; inference only).

None of these moves FY27 EBITDA. If the team wants its rule to survive the call, it should state in advance that they do not trigger the kill. The trade-off: all four past guide or framework days closed up (+2.67% to +15.62%) [BX-13; Barron's]. The price can therefore rise through a stop even when the thesis passes, which is the reason not to rely on a price stop alone (Q3).

**Checkpoint 3 (for the ambiguous zone, ~45%): the spring-2027 CMD with a 2030 outlook.** The date is not set and may fall after 03-31.
- Pass: 2028 held at ≤ $11.5B and FY28 consensus revised down toward it.
- Kill: 2028 raised to ≥ $12.3B.
- A time stop is one option: if January lands in the ambiguous zone and the CMD date falls beyond the team's horizon, close the position at the Q1'27 print (late April), where the first FY27 guide revision can occur. The FY26 precedent is a raise at Q1 [S1: Q1REL 0001996810-26-000063] [S2: Q2REL "remains 12%-14%"].

### Q2. Kill rules and pass marks: LONG 12 months (to about Sep-2027)

The long needs two things: FY28 consensus near $13B not converging down to the $11.2B plan, and the NTM multiple holding at ≥ ~22x. At a flat price the Sep-27 multiple is 20.3x [F01 A1].

| Date | Line | Long pass | Long kill | Why |
|---|---|---|---|---|
| 10-28 | FY26 margin guide / Q3 EBITDA / Power | Range raised, or Q3 ≥ $1,706M with Power ≥ 18% | Guide steered to the low end, **or** Q3 < $1,535M (the guide-implied floor), **or** Power < 17% (below the Q3 guide) | Q2'26 shows a held margin alone produced −8.69% (−12.55% over 5 days) [BX-13; Reuters]. A miss below the guide floor would be the first below-guide quarter at a ~2x market multiple |
| Late Jan-27 | FY27 dollar guide midpoint | ≥ $9.4B, or 2028 raised ≥ $12.3B | ≤ $8.55B **and** 2028 held | Mirrors the short's zones. The long can live with the ambiguous zone only if 2028 is raised or the CMD is dated |
| Spring-27 CMD | 2028 / 2030 outlook | 2028 ≥ $12.3–12.5B, or a 2030 path consistent with FY28 consensus | 2028 held at $11.2B | FY28 consensus is 16.6% above the plan. The +39% NTM roll-forward rests on that gap [brief §4, §7] |
| Late Apr / late Jul-27 | FY27 guide revision at Q1 / Q2 | Raised | Cut or held with a margin miss | FY26 precedent: first guide raised at Q1 [Q1REL; Q2REL] |
| Continuous | NTM EV/EBITDA | ≥ 22x | ≤ 20x | 20x on Sep-27 NTM $12,191M is $950, about flat. On the plan path ($10,794M) it is $845 [brief §7] |

### Q3. Price-based stop: how to set its level from realised volatility (options with trade-offs)

**Inputs**
- Daily σ 3.34% since the spin [BX; verifier 3.35%].
- HV30 47.1% (alphaquery, 09-25); HV20 50.3% (thetaOwl, 09-16).
- Implied vol ~45–49%: alphaquery IV mean 45.2%, and the thetaOwl expected-move curve (09-15) backs out 44.8% (Oct-16 expiry) to 48.8% (Mar-19). thetaOwl's headline IV of 71.8% (09-16, the day after the GLJ drop) is an outlier (**conflict**, §3).
- Q3 event move: the historical RMS over 10 print days is 7.26% (mean absolute 5.42%) [BX-13]. The options-implied figure is about ±7.7% one-sd (A7). The two agree.

**Method.** Choose the stop so that the probability that noise alone touches it before the thesis date equals a tolerance the team picks. Zero-drift barrier formula: P(hit) = 2·[1 − Φ(ln(1+b) / (σ√T))] (A5). Closing-price monitoring lowers these figures by about 3–5 points.

Short, entry $962.49, horizon 81 sessions to about 01-27:

| Stop | Price | Anchor | P(noise hit) at σ√T 30.1% (3.34%/day) | at 26.6% (47% p.a.) |
|---|---|---|---|---|
| +10% | $1,059 | — | 75% | 72% |
| +12.1% | $1,079 | Consensus at constant 28.2x (F01/E02) | 70% (66% close-monitored) | 67% (62%) |
| +19.0% | $1,145 | 30x Jan-NTM $9,865M [computed] | 56% | 51% |
| +22.1% | $1,175 | All-time closing high, 2026-06-30 [BX-08] | 51% | 45% |
| +25% | $1,203 | Just above the 52-week high of $1,195.94 | 46% | 40% |
| +30% | $1,251 | ≈1σ of the horizon | 38% | 32% |

**Five stop designs and their trade-offs**

| Option | Stop | Pros | Cons |
|---|---|---|---|
| S1 | Valuation stop at $1,079 | Easy to defend ("the market re-rates consensus") | Noise-out ~2/3 of the time before the thesis date |
| S2 | Technical stop just above the $1,174.86 closing high, or the $1,195.94 52-week high | A new high reads as the market rejecting the thesis | ~45–51% hit probability; loss at the stop is 5x the E02 central gain |
| S3 | σ-sized stop (+30–34%) | Hit by noise ≤ ~1/3 of the time | Loss at the stop ≈ 7x the expected gain, so it needs small sizing. If position = risk budget / stop distance, a 1% NAV risk means ~3% NAV at +30% |
| S4 | **Staged, event-conditioned** | Separates noise from thesis evidence; pairs naturally with Q1 | More complex to explain in 10 minutes |
| S5 | Defined risk: put spread / call-spread-overlay through a Feb- or Mar-27 expiry | Max loss known up front; no stop-out on noise | Premium at ~45–49% IV; the Jan-15 expiry falls before the likely guide date; strikes and pricing need a live chain (not pulled) |

How S4 is staged:
- Window 1, to 10-27 (20 sessions, σ√T 13.2–14.9%): stop only at about +20% ($1,155), roughly 1.4σ, so noise hits it ~15–20% of the time.
- 10-28: exit on the Q1 kill lines (FY26 margin raise, EBITDA ≥ ~$1,800M), not on price.
- Window 2, to January (~60 sessions, σ√T 22.9–25.9%): stop around +25–30% from the post-Q3 close, or at a fixed level such as $1,195.

**Long, 12 months (252 sessions):**

| Stop | Price | P(noise hit) at 53% p.a. | at 47% p.a. |
|---|---|---|---|
| −15% | $818 | 76% | 73% |
| −20% | $770 | 67% | 64% |
| −25% | $722 | 59% | 54% |
| −30% | $674 | 50% | 45% |
| −38.3% (largest post-spin drawdown) | $594 | 36% | 30% |

For the long, the valuation-anchored alternative is NTM ≤ 20x. On Jan-NTM $9,865M that is $775 (−19.5%) [computed A8]. The price-equivalent of that level rises as the NTM roll-forward proceeds.

**Untested: a peer-relative stop** (GEV against a VRT/ETN/SE basket). On the GLJ day the peers fell 7.6–8.0% and GEV's excess move was only about −3% (brief §5). A relative stop would strip out the sector beta that dominated that day. The beta was not computed (open item).

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | FY24/FY25 EBITDA beat vs bonus target | +1.75% / +10.2% | DEF 14A -25-000049 p.54; -26-000049 p.50 | 4Q24 / 4Q25 releases | exact | H |
| 2 | FY26 January guide | $44–45B; 11–13% | 8-K EX-99 0001996810-26-000012 | news src:27, 2026-01-23 | exact | H |
| 3 | FY26 current guide | $45.5–46.5B; 12–14% | Q2REL 0001996810-26-000147 | D07 / MoneyTimes 07-22 | exact | H |
| 4 | FY26 consensus EBITDA | $6,359M / $6.4B | MS 09-29 | ChartMill | close | M |
| 5 | FY27 consensus EBITDA | $9,574M | MS | GF "Street $9.45B" | close (−1.3%) | M |
| 6 | Q3 Power guide | 17–18% margin, +17–19% revenue | news src:3801 | news src:1016 | exact | H |
| 7 | Q3 EBITDA consensus | $1,706M / $1,728M | MS | ChartMill | close | M |
| 8 | Guide-implied Q3 EBITDA | $1,535–1,716M | D07 rebuild (Q2 transcript) | — | computed, [SINGLE-SOURCE inputs partly] | M |
| 9 | Earnings-day moves (10) | RMS 7.26%, mean absolute 5.42% | BX-13 Yahoo | Nasdaq closes (626 sessions agree) | exact | H |
| 10 | Daily σ since spin | 3.34% | BX | verifier 3.35% | close | H |
| 11 | HV 30d / 20d | 47.1% (09-25) / 50.3% (09-16) | alphaquery | thetaOwl | close (different windows) | M |
| 12 | Implied vol | 45.2% mean IV (09-25) vs 71.8% (09-16) | alphaquery | thetaOwl | **conflict**. The thetaOwl expected-move curve implies ~45–49%, supporting ~45%. The 71.8% is likely a post-GLJ near-dated read | M |
| 13 | Options expected move, Oct-16 / Oct-30 / Jan-15 / Mar-19 | ±10.4% / ±13.9% / ±22.0% / ±27.8% (spot $882.81, 09-15) | thetaOwl | — [SINGLE-SOURCE; Barchart / Market Chameleon not read]. The Oct-23 row (±5.7%) is internally inconsistent | L–M |
| 14 | Q4'24 / Q4'25 adj EBITDA margin | 10.2% / 10.6% | 0001996810-25-000004 | 0001996810-26-000012 | company releases only | M |
| 15 | Drawdowns ≥15% since spin | 5; median −24.6%; max −38.3% | BX-03..08 Yahoo | Nasdaq | exact | H |
| 16 | Closing high / 52-week high | $1,174.86 (06-30) / $1,195.94 | BX-08 | brief §2 (vendor) | close (close vs intraday) | M |
| 17 | FY27 margin-guide distribution | <15: 5%, 15–16: 10%, 16–17: 25%, 17–18: 30%, 18–19: 22%, ≥19: 8% | D04B §1 | D04A via E02 (≥18% ≈30%) | close | L (judgement) |
| 18 | Price | $962.49 | yfinance 2026-09-30 | Zacks/Yahoo via D08 | exact | H |

## 4. Arithmetic

- **A1, cushion ladder.** 9,574 / 1.0175 = 9,409 (17.84%); / 1.102 = 8,688 (16.47%); / 1.120 = 8,548 (16.21%); / 1.191 = 8,039 (15.24%). Margins are on $52,740M.
- **A2, FY26 cushion.** Jan-26 guide midpoint: 44.5 × 12% = 5,340. Current: 46.0 × 13% = 5,980, and 5,980 / 5,340 = 1.120. Consensus: 6,359 / 5,340 = 1.191.
  - Caveat: the Jan-26 guide includes Prolec for 11 months. I could not verify how much of the later raise was organic versus inorganic.
- **A3, zone probabilities from D04B** (uniform within each bucket; research judgement):
  - Kill (≥17.84%): 30% + 22% + 8% plus 0.16 × 30% ≈ 35%.
  - Pass (≤16.21%): 5% + 10% + 0.21 × 25% ≈ 20%.
  - Ambiguous: ≈ 45%.
- **A4, FY26 raise to 13–14%.** (13.5% × 46,000 − 2,146) / 25,558 = 4,064 / 25,558 = 15.9% H2 margin, vs consensus H2 16.3% [H1 figures: 10-Q / Q2REL].
- **A5, barrier probability.** P = 2[1 − Φ(ln(1+b) / (σ√T))].
  - σ√T = 3.34% × √81 = 30.1%, or 47% / √252 × 9 = 26.6%.
  - Example, $1,079: ln 1.121 = 0.1142; 0.1142 / 0.301 = 0.379; Φ = 0.648; P = 70%.
  - Close-monitoring correction: shift the barrier by +0.5826 × σ_daily ≈ +1.9 points, giving 66%.
  - The ~1/3 tolerance needs z = 0.974, i.e. a barrier of 0.974 × 26.6–30.1% = 25.9–29.3% in log terms, or +29.6% to +34.0%.
- **A6, long.** σ√T = 53% or 47%. Example, −25%: ln 0.75 = −0.2877; 0.2877 / 0.53 = 0.543; Φ = 0.706; P = 59%.
- **A7, implied Q3 event move** (thetaOwl, 09-15; the straddle ≈ 0.8σ√t convention is an approximation):
  - Oct-16 base σ = (10.44 / 0.8) / √(31/365) = 44.8%.
  - Oct-30 variance = (13.9 / 0.8)² = 301.9.
  - Base variance over 44 days = 44.8² × 44/365 = 241.9.
  - Event sd = √60.0 = 7.7%.
- **A8, stop prices.** (30 × 9,865 + 9,113) / 266.33 = $1,145. (28.2 × 9,865 + 9,113) / 266.33 = $1,079. (20 × 9,865 + 9,113) / 266.33 = $775.
- **A9, session counts.** Oct 22 + Nov 20 + Dec 22 + Jan 1–27 17 = 81. Window 1 (09-30 to 10-27) = 20.

## 5. General question bank items answered

- **G13 (dated event and pass mark):** 10-28 (gate) and late-Jan (dollar-midpoint zones, §2 Q1). The CMD is the fallback test.
- **G14 (what could push the reveal beyond the horizon):** ~45% ambiguous-zone odds (A3) push the answer to the CMD, which may land after the 12-month horizon for a short that began in October.
- **G15 (how wrong, how fast):** single-day upside tail +15.62%; median drawdown −24.6%. A short can lose ~10–15% in one session on a margin-guide raise [BX-13].
- **G17 (what management controls):** guidance cushion (A1–A2); buyback authorisation timing; bundling of positives on the January call.
- **G18 (kill rule):** §2.
- **G21 (what we would see if wrong):** Q3 EBITDA ≥ ~$1,800M or Power ≥ 19.5% (above guide); a FY26 margin raise.

## 6. What would change this

- **FY27 guided in dollars with no margin figure:** the zones apply directly. If only a margin range is given, convert using the revenue-guide midpoint, not consensus revenue.
- **A disclosed 2026 bonus target (proxy):** would recalibrate the cushion. It is not available until spring 2027 (E04).
- **A live options chain showing IV well below 45%:** narrows every stop grid. A spike toward 70% widens it.
- **Paid segment consensus putting FY27 Power ≤ 21%:** move the Power kill line down to about 20.5%.

## 7. Disagreements with the master brief

1. **"FY27 guide margin at or above ~18%" as the short's kill rule.** It should be a dollar line at ≥ ~$9.4B (17.84% only at consensus revenue). A pass needs ≤ ~$8.55B, not just "below 18%".
2. **E04's 16.5–17.8% cushion band understates the ambiguity.** FY26 extends it down to 15.2–16.2% (A1).
3. **F01's $1,079 stop.** On volatility alone it has a ~62–70% chance of being hit before the thesis date.
4. **Consensus FY27 Power margin.** GLJ's 20.7% conflicts with the builds' 21.7–23.5%. The Power line thresholds should sit below both.

## 8. Open items

- **Live option chain:** Feb/Mar-27 IV, and strikes/cost for a put spread (Barchart / CBOE). Only thetaOwl's 09-15 snapshot was read.
- **Peer-relative stop:** GEV beta to a VRT/ETN/SE basket, and residual σ.
- **January call date:** GEV events page, probably announced on 10-28.
- **FY26 raise split:** organic versus Prolec (Q1REL bridge).
- **thetaOwl data quality:** the Oct-23 row anomaly; cross-check on Market Chameleon.
