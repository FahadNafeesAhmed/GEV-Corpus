# Independent audit of the decision-critical facts

_D08_fact_audit — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 02:27:24. Requests 46, input tokens 3142168, output tokens 27190._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV decision-critical fact re-verification (as of 2026-09-30)

## 1. Bottom line

- **Two of the 30 facts are weak, and both carry the short case.**
  - The CEO's "'29 and '30" quote rests on one document: GEV's own Laguna transcript PDF, p.10. I found other transcript copies (stockanalysis, Seeking Alpha, earningscalls.dev) but could not reach the passage in them.
  - GLJ's FY27 numbers ($7.42B EBITDA; Power margin 18.5% vs 20.7%) come from one GuruFocus wire. The Yahoo copy is the same article. [S1: Laguna PDF, gevernova.com, 2026-09-16] [S1: GuruFocus 9079408, 2026-09-15; corpus src:684/src:679 are the same text]
- **The valuation base holds.** Price, shares, cash, debt, FY25 actuals, the FY26 guide, the 2028 framework, RPO and gas GW all tie across two documents, or across a filing and a data vendor.
  - Price $962.49 [S1: yfinance quote, 2026-09-30 06:22 UTC] [S2: Zacks/Yahoo, 2026-09-29: "closed at $962.49, +1.34%"].
  - Shares 266,333,581 [S1: 10-Q 0001996810-26-000148, balance sheet] [S2: yfinance shares_outstanding 266,333,581; MarketScreener 266,334K].
- **Consensus EBITDA agrees across sources to within ~1–2%, but only MarketScreener publishes the full FY26–FY28 row.**
  - FY27 $9,574M is confirmed within 1.3% by GLJ's quoted "Street $9.45B". A Motley Fool EV/multiple back-solve gives about $9.6B.
  - FY28 $13,064M is confirmed within 0.2% by Motley Fool's "60% CAGR 2025–2028" on FY25's $3,196M.
  - FY26 EBITDA ($6,359M) and FY27–28 FCF are single-vendor. [S1: MarketScreener finances] [S2: GuruFocus 2026-09-15; Motley Fool 2026-09-29]
- **The EPS basis is a trap.** For FY27 the three vendors are close: MarketScreener $24.85, FactSet mean $24.78, S&P/stockanalysis $25.13 (labelled non-GAAP). For FY26 they are not: GAAP-type $30.49–30.78 vs ex-items $15.16. The gap is the $3,992M Prolec gain. [S1: MarketScreener; Zacks 2026-09-29] [S2: stockanalysis forecast (S&P), 2026-09-22; cnyes/FactSet 2026-07-23]
- **Nothing decision-relevant has changed since 2026-09-29.** There are no new filings (last 8-K was 2026-08-27) and the yfinance news feed was empty. Consensus drifted slightly *up* between the 2026-09-04 MarketScreener snapshot and the brief's 2026-09-29 figures (FY27 EBITDA 9,570 → 9,574). Zacks says its FY26 EPS moved 0.63% lower over the month. [S1: MarketScreener snapshots] [S2: Zacks 2026-09-29]
- **The 2027 RPO bucket ($20,558M) is arithmetically right but less precise than it looks.** Each disclosed percentage is rounded, so it is ±~$0.64B. It covers all-segment equipment RPO, not Power only. [S1: 10-K 0001996810-26-000015 Note 9] [S2: Q4'25 call, corpus src:2660: "$64 billion in equipment backlog"]

## 2. Answers to the questions

**Q1. Confirmed with two independent sources (24 of 30 rows):**
- Market inputs: price; shares outstanding.
- Balance sheet: cash, with a definition note (below).
- FY25 actuals: revenue, adj EBITDA, FCF.
- H1'26: revenue, adj EBITDA, OCF, FCF.
- Guidance: FY26 guide; 2028 framework.
- Consensus: revenue FY26–28; FY27 and FY28 EBITDA (close, not exact).
- Backlog: total RPO $176B; gas 53 + 63 = 116 GW and the ≥125 GW target; output path 20 → 24 → 30 GW.
- GLJ day and stock history: $470 target and date; GLJ-day close; record close $1,174.86.
- Timing quote: the Q4'25 "'27 and beyond" line.
- Targets: consensus target ~$1,237.

Only company documents (release + 10-Q/10-K, same publisher, no vendor check):
- Power segment margins: FY23–FY25 series; H1'26 17.6% and Q2'26 18.8%.
- Equipment RPO conversion percentages (Note 9 only).
- Borrowings of $2,849M. yfinance total debt of $3,720M reconciles only after adding ~$871M of operating leases.

Sources are listed per row in the table in section 3.

**Q2. Single-source, and where else I looked:**
1. **CEO "'29 and '30" quote.** Only source is the gevernova.com Laguna PDF p.10, verified by the prior verifier. I read the stockanalysis transcript to ~30k characters without reaching the passage. Two Exa phrase searches returned the adjacent passage (the 2026 backlog-margin change will be "larger than … '25 … low double digits"), not this line.
2. **GLJ FY27 EBITDA $7,420M, Power 18.5% vs "consensus 20.7%", Street $9.45B.** Only GuruFocus (Renato Neves, 2026-09-15). Seeking Alpha, 24/7 Wall St, Yahoo/StockStory, AInvest and Tiger all confirm the $470 target but not these figures.
3. **Consensus FY26 EBITDA $6,359M, FY27–28 FCF, Q3 EBITDA $1,706M.** MarketScreener only. stockanalysis/S&P shows FY26 FCF of $12.02B but hides FY27–28 behind a paywall. Zacks gives only EPS and revenue.
4. **NCI $1,158M.** 10-Q only; yfinance returns null.
5. **Diluted weighted-average shares 270M.** 10-Q only. The release gives an implied cross-check: $668M ÷ $2.47 = 270.4M.
6. **H1 contract-liability line $13,695M.** 10-Q only. The Q2 release has no cash-flow line for it. The Q2 transcript confirms the mechanism only ("received a significant amount of down payments"; Q2 working capital "$6.4 billion cash benefit").
7. **The −38.3% drawdown peak ($437.71).** The trough of $270.13 is confirmed (Smartkarma 2025-03-11: $284.21 less $14.08). The peak was not re-found this session.
8. **CFO change.** 8-K 0001996810-26-000153 only (I did not search for a second source). It says Claire McDonough becomes CFO effective 2027-01-01 and joins as advisor on 2026-11-01.

**Q3. Changed since 2026-09-29.**
- No company-reported change.
- Consensus moved within ±0.2% between 2026-09-04 and 2026-09-29: revenue FY26 46,259 → 46,282; FY27 EBITDA 9,570 → 9,574; FY28 13,059 → 13,064; FY26 FCF 12,011 → 12,017. [S1: MarketScreener 09-04 cache] [S2: brief/facts.csv CT-01/02, fetched 09-29]
- Jefferies cut its target from $1,210 to $1,185 on 2026-09-22. [stockanalysis/TipRanks]
- Q3 consensus from Zacks: EPS $4.08, revenue $12.07B. MarketScreener has Q3 revenue at $12,004M. [Zacks 2026-09-29; MarketScreener]
- I could not get a quote after 9/29: the live feed still returns $962.49.

**Q4. Definition traps (highest impact first):**
1. **FY26 EPS basis:** GAAP-type $30.49 (Zacks) or $30.78 (MarketScreener) vs ex-items $15.16 (S&P). FY27 is consistent across vendors at $24.78–25.13.
2. **"Consensus EBITDA" means GEV-adjusted EBITDA.** MarketScreener's FY24 and FY25 actuals ($2,035M and $3,196M) match GEV's adjusted figures exactly [Q4'25 release]. Segment EBITDA ≠ company adj EBITDA.
3. **GLJ's "38.9x forward EV/EBITDA" is the FY26 multiple, not FY27.** Check: $247,230M ÷ $6,359M = 38.9x.
4. **Backlog margin vs segment margin.** "Contribution margin in backlog, change vs prior year" (+11 pts Power FY25; "low double digits" at Laguna) is not a segment EBITDA margin.
5. **Cash of $13,120M includes restricted cash (~$0.4B).** yfinance shows $12.72B. **Debt of $2,849M excludes operating leases (~$0.87B).** Together they move EV by +$1.3B (+0.5%).
6. **Shares:** 266.33M outstanding vs 270M diluted weighted-average (−1.4% per share on the diluted count).
7. **52-week high of $1,195.94 is intraday.** The record close is $1,174.86, and the drawdowns are measured on closes.
8. **RPO "within 2 years" at 12/31/25 is calendar 2027 exactly.** At 6/30/26 the 1–2-year bucket (65% − 36%) is mid-2027 to mid-2028, not calendar. It is all-segment equipment, not Power.
9. **The "20 GW run-rate" is 5 GW/quarter in Q3–Q4'26.** Laguna says early 2027 "will feel generally very similar", with 6 GW/quarter "sometime in the second half of next year". That makes calendar-2027 output about 22 GW at most (research estimate, computed), not 24.

**Q5. Which single error would flip the direction call.**
The short lean rests on two legs:
- (a) Street FY27–28 EBITDA sits above management's plan. This is **robust**: two vendors agree within ~1–2%, and FY28 is +16.6% over the framework either way.
- (b) Management's own timing, where margin uplift lands in '29–'30. This is **fragile**: one document, and it maps the *2026* backlog-margin change to '29–'30. The claim that 2024 orders dominate FY27 margin is an extrapolation of that lag, not a statement.

If the p.10 wording or context turns out to differ (for example, it refers only to 2026 SRA conversions, or the lag is shorter for aeroderivatives), the timing leg falls away. The case then reduces to the Street being above the plan, which the brief itself says is roughly fairly priced on the plan at ~23x. Re-read p.10 in full, and one independent transcript, before relying on it.

## 3. Evidence table (30 facts)

| # | Fact | Brief value | S1 value + locator | S2 value + locator | Match | Note / confidence |
|---|---|---|---|---|---|---|
| 1 | Close 9/29 | $962.49 | yfinance $962.49 (2026-09-30 06:22 UTC) | Zacks/Yahoo 9/29 "closed at $962.49" | Y | H |
| 2 | 52-wk range | $530.16–1,195.94 | Motley Fool 9/29 quote box $530.16–$1,195.94 | not re-found | Y/[SINGLE] | High is intraday; record close $1,174.86 (Fool). M |
| 3 | Shares outstanding | 266.33M | 10-Q -26-000148 BS: 266,333,581 | yfinance 266,333,581; MarketScreener 266,334K | Y | H |
| 4 | Diluted WA shares Q2 | 270M | 10-Q income statement: 270 (6M: 271) | release: $668M ÷ $2.47 = 270.4M (computed) | Y | Same-company docs. H |
| 5 | Cash | $13,120M | 10-Q BS "Cash, cash equivalents, and restricted cash $13,120" | release "$13.1B cash balance"; yfinance $12.72B | Close | Includes restricted cash. H |
| 6 | Borrowings | $2,849M | 10-Q BS LT $2,794M (+$55M current per Note 14) | yfinance total debt $3.72B = 2,849 + ~871 op leases | Close | Definition. M-H |
| 7 | NCI | $1,158M | 10-Q BS $1,158M | none found | [SINGLE] | H (filing) |
| 8 | Simple EV | $247.2B | computed 256,343 + 2,849 + 1,158 − 13,120 = 247,230 | stockanalysis $247.34B (prior); Motley Fool "$241B" | Conflict (Fool) | Fool bridge unknown; filing math holds. H |
| 9 | FY25 revenue | $38,068M | Q4'25 release 8-K -26-000012 | XBRL latest_revenue $38,068M; stockanalysis $38.07B | Y | H |
| 10 | FY25 adj EBITDA | $3,196M (8.4%) | Q4'25 release | MarketScreener FY25 actual $3,196M | Y | H |
| 11 | FY25 FCF | $3,710M | Q4'25 release | MarketScreener and stockanalysis $3,710M / $3.71B | Y | H |
| 12 | Power FY25 revenue / EBITDA | $19,767M / $2,902M | 10-K MD&A Power table (14.7%) | Q4'25 transcript "11 points of growth in Power" (backlog, not P&L) | Y (filing) | Release segment table not opened. H |
| 13 | Power margin FY23 / FY24 | 9.88% / 12.51% | 10-K FY25 3-yr table 1,722/17,436; 2,268/18,127 | FY24 10-K (facts PMX-02) | Y | Company-only. H |
| 14 | Power H1'26 / Q2'26 | 17.63% / 18.82% | Q2 release segment table 1,842/10,449; 1,031/5,477 | 10-Q MD&A p.29 (PMX-05) | Y | H |
| 15 | H1'26 revenue / adj EBITDA | $20,442M / $2,146M | Q2 release total-company table | 10-Q IS $20,442M; MarketScreener Q1 + Q2 = 896 + 1,250 = 2,146 | Y | H |
| 16 | H1'26 OCF / FCF | $10,680M / $9,897M | 10-Q CF 10,680; capex (783) | Q2 release 10,680 / 9,897 | Y | H |
| 17 | Contract-liability OCF line | $13,695M | 10-Q CF "13,695 / 1,860" | Q2 transcript: down payments; Q2 WC +$6.4B (qualitative) | [SINGLE numeric] | Do not use Note 9's $14,088M. H |
| 18 | FY26 guide | $45.5–46.5B; 12–14%; FCF $11.5–12.5B; Power 18–20% growth / 17–19% margin | Q2 release "2026 Guidance" | Kalkine 2026-09-29 (same numbers); Q2 transcript FCF | Y | Lark Research wrote FCF "$11.5–13.5B", which is an error. H |
| 19 | 2028 framework | $56B; 20%; FCF ≥$24B; Power 22 / Elec 22 / Wind 6 | Q4'25 release "revenue of $56 billion, up from $52 billion" | stockintent 2026-09-19 (20%, up from 14%) | Y | H |
| 20 | Consensus revenue FY26/27/28 | 46,282 / 52,740 / 60,500 | MarketScreener (09-04: 46,259 / 52,731 / 60,466) | stockanalysis/S&P 46.28B / 52.74B; Zacks FY26 46.29B; FactSet (7/23) FY27 52,632 / FY28 60,511 | Close | H |
| 21 | Consensus FY27 EBITDA | $9,574M | MarketScreener (09-04: 9,570; 18.15%) | GLJ-quoted "Street $9.45B" (−1.3%); Fool EV $241B at 25x ≈ $9.6B | Close | M-H |
| 22 | Consensus FY28 EBITDA | $13,064M | MarketScreener (09-04: 13,059; 21.6%) | Fool "60% CAGR 2025–28" → 3,196 × 1.6³ = 13,091 | Close | M |
| 23 | Consensus FY26 EBITDA | $6,359M | MarketScreener (09-04: 6,353) | none | [SINGLE] | M |
| 24 | Consensus FY27 EPS | $24.85 | MarketScreener (09-04: 24.80) | FactSet mean 24.78 (cnyes 7/23); S&P 25.13; yfinance fwd 25.13 | Close | Basis differs. H |
| 25 | Consensus FCF FY26/27/28 | 12,017 / 7,417 / 9,248 | MarketScreener (09-04: 12,011 / 7,402 / 9,240) | stockanalysis FY26 12.02B only | FY26 Y; FY27–28 [SINGLE] | M |
| 26 | RPO total; equipment + conversion | $176B; $87,821M at 36/65/97 | 10-Q Note 9: 176,284; 87,821 at 36%, 65%, 97% | Q2 release "$176 billion"; Laguna "$176 billion backlog" | Y (total) | Percentages single-doc. H |
| 27 | YE25 equipment RPO → 2027 | $64,245M × (69 − 37%) = $20,558M | 10-K Note 9: 64,245 at 37%, 69%, 97% | Q4'25 call (src:2660) "$64 billion in equipment backlog" | Y | ±$0.64B from rounding. H |
| 28 | Gas GW | 53 + 63 = 116; ≥125 by YE26 | Q2 release "44 to 53 GW … 56 to 63 GW" | Q2 transcript src:3161 same | Y | Laguna: H2 "20 GW likely to prove conservative". H |
| 29 | Output path | 20 GW Q3'26 → 24 GW 2028 → 30 GW 2030 | Q2 release CEO quote | Laguna: 5 GW/qtr Q3–Q4; 6 GW/qtr in H2'27; 7 GW/qtr later | Close | H |
| 30a | GLJ target / date / day move | $470; 9/14; −8.6% | Seeking Alpha 9/14 "plunged 8.6%" | stockanalysis/TipRanks (Sep 14, $470); history: 957.27 → 874.76 (−8.62%); TECHi same | Y | GuruFocus $874.85 vs $874.76 (tiny). H |
| 30b | GLJ FY27 figures | $7,420M vs $9,450M; Power 18.5% vs 20.7% | GuruFocus 9079408 (2026-09-15) | Yahoo copy = same wire | [SINGLE] | M |
| — | Drawdowns (for reference) | −38.3% (437.71 → 270.13); record close 1,174.86 | Smartkarma 3/11/25: 284.21 − 14.08 → 270.13 | Fool 9/29: record close $1,174.86 in June | Partial | Peak 437.71 not re-found. M-H |
| — | CEO '29–'30 quote | "tells you the equipment margins for '29 and '30, largely" | Laguna PDF p.10 (prior verifier) | not reached | [SINGLE] | M |
| — | Q4'25 timing quote | "'27 and beyond" | Q4'25 call text (corpus src:2660) | trade press src:149 (quotes Strazik) | Y | Corpus date label says 01-23; the call was 01-28. H |

## 4. Arithmetic

- **Market cap:** 266,333,581 × 962.49 = $256,343M. **EV:** 256,343 + 2,849 + 1,158 − 13,120 = $247,230M.
  - Variant: exclude ~$400M restricted cash (13,120 − 12,720) and add ~$871M operating leases → ~$248.5B.
- **Power margins:** 1,722/17,436 = 9.88%; 2,268/18,127 = 12.51%; 2,902/19,767 = 14.68%; 1,842/10,449 = 17.63%; 1,031/5,477 = 18.82%.
- **FCF check:** 10,680 − 783 = 9,897.
- **2027 equipment RPO:** 64,245 × 0.32 = 20,558. Rounding band 31–33% gives 19,916–21,201.
- **Multiples:**
  - FY27 EBITDA: 247,230 / 9,574 = 25.8x. At GLJ's Street figure: 247,230 / 9,450 = 26.2x.
  - FY26 EBITDA: 247,230 / 6,359 = 38.9x (matches GLJ's "38.9x forward").
  - P/E: 962.49 / 24.85 = 38.7x; / 25.13 = 38.3x; / 24.78 = 38.8x.
- **FY28 cross-check:** 3,196 × 1.6³ = 13,091 vs 13,064 (−0.2%).
- **Consensus vs framework:** FY28 13,064 / 11,200 = +16.6%. On GLJ's FY27 Street figure the gap is unchanged; FY28 has no second level source.
- **GLJ gap:** 7,420 / 9,450 − 1 = −21.5%. GuruFocus rounds this to "22%".
- **GLJ-day moves:** 874.76 / 957.27 − 1 = −8.62%. 9/29: 962.49 / 949.77 − 1 = +1.34%.
- **Implied H2'26 FCF at guide midpoint:** 12,000 − 9,897 ≈ $2.1B. This fits the CFO's "first half … substantially higher than the second half".
- **Gas output (research estimate, computed from Laguna):** 2026 ≈ 7.5 (H1 actual) + 5 + 5 = 17.5 GW. 2027 at most 5 + 5 + 6 + 6 = 22 GW, i.e. +14% to +26% year on year.

## 5. General question bank items answered along the way

- **G11 (physical constraint).** Output steps up by ladder: 5 GW/quarter through early 2027, 6 GW/quarter from H2'27. That caps FY27 gas volume growth at roughly +14–26%, so FY27 Power growth needs price and mix as well as volume. [Laguna transcript, gevernova PDF and stockanalysis copy]
- **G12 (accounting timing).** H1 FCF of $9,897M includes $13,695M of contract-liability inflow. Management guides H2 FCF much lower as SRAs convert to orders. [10-Q CF; Q2 transcript src:3161]
- **G13/G14 (catalyst).** Q3 results are on 2026-10-28, after the finals [Kalkine 9/29; IR events]. The FY27 outlook and the 2026 backlog-margin change come on the January 2027 call [Laguna]. The new CFO starts 2027-01-01 [8-K -26-000153].
- **G15 (downside path).** The trough-to-date on the open drawdown was −25.5% on closes ($1,174.86 → $874.76). [Fool 9/29; stockanalysis history]
- **G20 (evidence quality).** See the single-source list in Q2 and the definition traps in Q4.

## 6. What would change these findings

- **p.10 wording.** If the full Laguna text limits "'29 and '30" to 2026 SRA conversions, or to heavy-duty gas only, the timing leg weakens.
- **A second consensus EBITDA feed.** If Visible Alpha, FactSet or Bloomberg shows FY27 below ~$9.2B or FY28 below ~$12.5B, the "Street above plan" gap shrinks by a third or more.
- **The Q3 10-Q (after 10/28).** New RPO conversion percentages and Q3 buyback counts will make the share count and RPO buckets stale.

## 7. Disagreements with the master brief

- **The 2027 RPO bucket is shown to the dollar.** It is ±~$0.6B from rounding and covers all segments. It should be presented as a range (research estimate).
- **"20 GW/yr run-rate from Q3'26" should not be read as 2027 output of 20+ GW rising fast.** Laguna implies about 22 GW at most for calendar 2027.
- **The "'29–'30" quote is listed as verified.** On two-source standards it is single-source.
- **GLJ's FY27 build figures are single-wire**, even though facts.csv marks them "verified".
- **FY26 EPS labels:** the brief's P/E framing should state the basis. FY27 is consistent across vendors; FY26 is not.
- **Minor:** corpus src:2660 is dated 2026-01-23, but the Q4'25 call was on 2026-01-28.

## 8. Open items

1. Read Laguna PDF pp.9–11 in full, plus the Seeking Alpha transcript, for the exact "'29 and '30" context.
2. Get a second consensus EBITDA row for FY26 and FY28, and FY27–28 FCF, from a university terminal (FactSet/Bloomberg/Visible Alpha).
3. Find the full GLJ note (the source of the 20.7% "consensus Power 2027 margin").
4. Find a second source for the $437.71 peak close (2025-01-23), e.g. the Nasdaq historical page.
5. Find a second source for NCI and the $13,695M line: EDGAR XBRL frames (us-gaap MinorityInterest; IncreaseDecreaseInContractWithCustomerLiability).
6. Re-pull price and consensus on the morning of submission (2026-10-02).
