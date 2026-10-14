# Consensus drift: is the Street already cutting FY27?

_R08_consensus_drift — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 05:02:43. Requests 34, input tokens 2556277, output tokens 26668._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV consensus revisions tracker, FY26–FY28 (research input, as of 2026-09-30)

*Research input only. Every range is a research estimate, and the team picks its own numbers.*

**Source key**
- **CN** = FactSet surveys republished by cnyes: 2026-01-29 (news/id/6326311), 02-09 (/6338962), 04-23 (/6430863), 04-24/25 (/6432423), 07-23 (/6544296). All five pages were read this session. They are one vendor over time.
- **MS** = MarketScreener finances page, fetched 2026-09-29 (evidence_lanes CT-01/02/04).
- **YF** = Yahoo Finance /analysis "EPS Trend" table, read this session. It is a cached snapshot showing an intraday price of $944.66 (+2.46%). The exact date is unverified; it falls in the second half of September.
- **ZK** = Zacks consensus as republished: 2026-08-18 (corpus chunk 246541) and 2026-09-18 (swingtradebot/Zacks).
- **BC** = Barchart: 2026-02-03 (financialcontent) and 2026-09-24 (narrative-news).
- **GLJ** = GLJ wire via Yahoo/GuruFocus 2026-09-14/15 (corpus chunk 223211).
- **EQ** = Equibles, 09-18 and 09-23 snapshots (CT-09).
- **MW** = MarketWatch/FactSet, 09-02 (CT-12). Marked unverifiable in the prior work.

---

## 1. Bottom line

- **The Street is not moving FY27 down toward $8.6–8.9B.**
  - Over nine months, FY27 EPS rose **+18.6%** and revenue **+7.1%** [CN 01-29 → MS 09-29; cross-check YF, ZK].
  - Since Q2 (07-23), FY27 EPS is flat: **+0.3%** (24.78 → 24.85) [CN 07-23; MS]. It is −0.3% on FactSet's own 09-02 figure (24.70) [MW, unverifiable].
  - Since GLJ (09-14), the only visible drift is **−0.7% in seven days** on Yahoo (24.87 → 24.69) [YF], plus one trim (Erste 24.64 → 24.55) [tickerreport 09-23; ad-hoc-news 09-21].
- **No free FY27 adjusted-EBITDA time series exists.** EBITDA is observed at only two points, from two vendors:
  - GLJ's "Street $9.45B" (09-14) [GLJ; corpus 223189];
  - MarketScreener's $9,574M (09-29) [MS].
  - The 1.3% difference is best read as vendor dispersion, not a revision. The change in EBITDA below is inferred from EPS and revenue.
- **Revisions cluster in the one or two days after each print.** Between prints they are flat.
  - FY27 EPS moved +11.0% from Jan to Apr, +6.5% from Apr to Jul, and +0.3% from Jul to Sep [CN; MS].
  - A Q2'26 adjusted-EBITDA miss (−2.1% vs estimates [StockStory 07-22; Reuters 07-22 "below LSEG estimates"]) produced **no FY27 cut**. Yahoo's FY27 figure went 24.25 (90 days ago) → 24.36 (60 days ago) [YF], and the FactSet median target held at $1,254.50 [CN 07-23; MW 09-02].
- **Correction to the brief: Jefferies raised, it did not cut.** The target went **$1,155 → $1,185 on 2026-09-11** (Buy) [StreetInsider 09-11; MarketScreener 09-11], and was reiterated on 09-17 [Investing.com 09-17]. The Bernstein target went $1,206 → $1,298 on 09-15 [evidence_lanes POS-23; Bitget/Zhitong 09-16/17]. No cuts to targets or FY27 estimates by major brokers were found for 09-14 to 09-29.
- **How much of the gap could close before the January guide: research estimate.**
  - Gap from consensus to the midpoint of the research range is **−$824M (−8.6%)** [computed].
  - Most likely pre-guide closure is **0–25%** of that gap, mainly at the Q3 print on 10-28. P(≥50% closes) ≈ 15–20%.
  - This is research judgement from the clustering pattern. The team sets its own probabilities.
- **Effect on the short's expected value.** Drift before the guide does not change the post-guide EBITDA, so the estimate part of the P&L measured from today's entry survives; it just arrives sooner.
  - What drift removes is the surprise-driven de-rating. With E02's frames, that takes the short's EV from **+4.3% at f=0 to about +1.9% at f=0.5 and −0.6% at f=1** (f = fraction of the gap closed before the guide) [computed from E02 §Q1].
  - Drift that happens before the team's entry date lowers the pitch's edge directly. Drift after entry mostly moves the timing.

---

## 2. Answers

### Q1. How consensus has moved, datapoint by datapoint

**FY27 (the key year)**

| Date | FY27 EPS (mean) | FY27 revenue ($M, mean) | FY27 adj EBITDA | S1 | S2 / cross-check |
|---|---|---|---|---|---|
| 2026-01-29 | 20.96 (median 20.97) | 49,236 | n/a | CN 6326311 | Barchart 02-03 FY26 $13.32 matches CN FY26 median 13.31 (same vintage); no second FY27 source for this date |
| 2026-02-09 | 21.81 | 50,436 | n/a | CN 6338962 | [SINGLE-SOURCE] for FY27 |
| 2026-04-23 | 23.27 | 51,140 | n/a | CN 6430863 | [SINGLE-SOURCE] |
| 2026-04-24/25 | 23.76 | 51,642 | n/a | CN 6432423 | [SINGLE-SOURCE] |
| ~late Jun (YF "90 days ago") | 24.25 | — | n/a | YF | Different vendor; 2.1% below CN 07-23 |
| 2026-07-23 | 24.78 (median 24.68; range 17.16–30.41) | 52,632 (median 52,405) | n/a | CN 6544296 | YF "60 days ago" 24.36 |
| 2026-08-18 | 24.27 (implied: −21.2% vs FY26 30.80) | — | n/a | ZK via corpus 246541 | CT-25 Zacks 24.27 |
| 2026-09-02 | 24.70 | — | n/a | MW (unverifiable) | — |
| 2026-09-14 | — | — | **"Street $9.45B"** | GLJ via corpus 223211 | corpus 223189, 235411 (same wire) |
| 09-18 / 09-23 | 24.84 / 24.85 | 52,743 / 52,740 | — | EQ | MS (**shared feed, not independent**) |
| Late Sep (YF current) | 24.69; 7 days earlier 24.87; 30 days earlier 24.85 | 52,680 | — | YF | MS 24.85 |
| 2026-09-24 | 24.09 | — | — | BC narrative-news | — |
| 2026-09-29 | 24.85 | 52,740 | **9,574 (18.15%)** | MS | EQ; GLJ $9.45B (−1.3%) |

- Vendor spread on current FY27 EPS is **24.09–24.87 (3.2%)**.
- Yahoo revision counts for FY27: 18 up / 3 down over 30 days; 1 up / 1 down over 7 days [YF].
- 24/7 Wall St (09-16) reports 3 up / 2 down over 30 days, a different vendor window [247wallst 09-16].

**FY26**

| Metric | Path |
|---|---|
| Revenue, FactSet mean ($M) | 43,031 (01-29) → 44,324 (02-09) → 44,933 (04-23) → 45,171 (04-24) → 45,913 (07-23) |
| Revenue, 09-29 | MS $46,282M; YF $46.26B; ZK $46.3B (09-18) |
| Revenue guide midpoint, for comparison | $44.5B (Jan) → $45.0B (Apr) → $46.0B (Jul) [TipRanks/TheFly 04-22; Reuters 07-22] |
| Adjusted EBITDA | $6,359M (13.74%) [MS]; FactSet 13.7% at Q2 [CNBC 07-22 via CT-26] |
| EPS, GAAP-type basis | ZK "shifted 1.34% downward over the past month" (09-18); YF 31.02 (90 days ago) → 30.74 (current) |

FY26 EPS is not usable as a trend series. The pool mixes estimates with and without the $3,992M Prolec gain: the CN mean jumps 13.35 → 21.1 → 24.57 → 29.67 as analysts add the gain, and the 07-23 low is 14.39.

**FY28**

| Metric | Path |
|---|---|
| EPS, FactSet mean | 28.69 (01-29) → 30.18 (02-09) → 32.63 (04-23) → 33.44 (04-24) → 34.71 (07-23) = **+21.0%** [CN; CT-16] |
| EPS, 09-29 | MS 34.22 (−1.4% vs FactSet 07-23; vendor difference, not a revision) |
| Revenue, FactSet mean ($M) | 56,452 → 57,400 → 58,142 → 58,666 → 60,511 = **+7.2%** |
| Revenue, 09-29 | MS $60,500M (matches) |
| Adjusted EBITDA | $13,064M, MS only; no time series |

**Price targets**

| Series | Path |
|---|---|
| FactSet median [CN] | $800 (01-29) → $836 (02-09) → $1,083.50 (04-23) → $1,250 (04-24) → $1,254.50 (07-23) |
| FactSet median, 09-02 [MW] | $1,254.50 |
| Mean, other vendors | $815.92 (BC 02-03); $837 (TIKR 02-24); $860.62 (TIKR 03-12); $1,237.34 (TIKR 09-18; MS 09-18 and 09-29) |

TIKR says the mean target "has risen every quarter since mid-2025" [TIKR 09-21].

### Q2. Is the Street moving FY27 down toward $8.6–8.9B?

**No.** The evidence:
1. **The last visible direction is flat.** FY27 EPS is flat since 07-23, and −0.7% over seven days after GLJ [YF]. At an EPS-to-EBITDA factor of ~0.93 (§4-A2), −0.7% is about **−$62M of EBITDA, roughly 7.5% of the $824M gap**.
2. **Brokers are raising targets after GLJ, not cutting.** Jefferies (+$30, 09-11) and Bernstein (+$92, 09-15) raised. MarketScreener's mean target is unchanged at $1,237.34 [MS 09-18/09-29], and its low of $940 excludes GLJ [POS-25].
3. **Crude EBITDA proxy (not observed data).** Scaling today's $9,574M back by the Jan→Sep EPS change puts the January-2026 vintage of FY27 EBITDA at about **$8.2B**. Scaling by revenue at constant margin puts it at about **$8.9B** (§4-A3).
   - So the research range $8.6–8.9B ≈ where the Street was in Q1-2026, before the Q1 raise.
   - The Street moved away from the range at the April and July prints and has not come back.

### Q3. How much of the gap could close before the January guide

**Mechanisms, in order of likely size**

| # | Event | Why it matters |
|---|---|---|
| 1 | Q3 print, 10-28 | Revisions cluster at prints. Q3 consensus EBITDA is $1,706M (MS) / $1,728M (ChartMill) [E02/D07] |
| 2 | Conference commentary Nov–Dec, and the pre-guide "consensus positioning" call | No Dec-2026 investor event is announced (brief §4). Jefferies expects FY27 guidance in January and long-term guidance in **March 2027** [edgex 09-12, citing the Jefferies note] |
| 3 | Siemens Energy mid-term update, 11-11 | Read-across on peer margins |

**Precedent**
- A −2.1% quarterly EBITDA miss in Q2 produced no FY27 cut (Q1 above).
- The one-day revision after the Q1 beat was +2.1% on FY27 EPS (CN 04-23 → 04-24).
- Implication: Q3-driven moves are of order ±1–3%, which is 10–35% of the gap.

**Research estimate grid (the team chooses its own)**

| Pre-guide FY27 consensus change | ≈ $M | Share of $824M gap closed (f) | Research P |
|---|---|---|---|
| Up (Q3 beat plus guide raise) | +100 to +300 | negative | ~25–30% |
| 0 to −1.5% | 0 to −145 | 0–18% | ~40–45% |
| −1.5% to −4% | −145 to −380 | 18–46% | ~15–20% |
| Worse than −4% | beyond −380 | above 46% | ~10% |

### Q4. What drift does to the short's expected value (E02 frames)

- The post-guide EBITDA outcome is fixed by the guide itself. Pre-guide drift therefore shifts **when** the estimate part is paid, not whether.
- What drift erodes is the de-rating on the day of the surprise. Taking "sticky" as the no-surprise frame, EV(f) ≈ 4.3% − f × 4.9pt:

| f | Short EV |
|---|---|
| 0 | +4.3% |
| 0.25 | +3.1% |
| 0.5 | +1.9% |
| 0.75 | +0.6% |
| 1 | −0.6% |

- Upper bound: if drift itself triggers revision-momentum de-rating (E02's "harsh" frame), the EV can **rise** toward +12%.
- Probability-weighting f over the Q3 grid gives a research EV of about **+3.5% to +4.0%**. Negative-f (upward) outcomes feed into E02's own +0.8% Q3-beat case.
- Timing trap: drift before the team's entry date is lost edge; drift after entry is P&L banked early.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf |
|---|---|---|---|---|---|---|
| 1 | FY27 EPS, Jan 2026 | 20.96 mean | CN 6326311 (01-29) | none for FY27 [SINGLE-SOURCE]; BC 02-03 confirms the FY26 vintage (13.32) | close (FY26) | M |
| 2 | FY27 EPS, Jul 2026 | 24.78 | CN 6544296 | YF 60 days ago 24.36; ZK 08-18 24.27 | close (±2%) | M |
| 3 | FY27 EPS, late Sep | 24.85 | MS 09-29 | YF 24.69; EQ 24.85 (shared feed) | close | H |
| 4 | FY27 revenue, Jan → Sep | 49,236 → 52,740 | CN 01-29 | MS; YF 52.68B | close (endpoint) | M |
| 5 | FY27 EBITDA "Street" | 9,450 / 9,574 | GLJ via Yahoo 09-14 (corpus 223211) | MS 09-29 | conflict 1.3% (vendor) | M |
| 6 | Post-GLJ 7-day FY27 drift | −0.7% | YF | Erste 24.64 → 24.55 (tickerreport 09-23; ad-hoc-news 09-21) | directionally close | M |
| 7 | FY28 EPS +21% Jan → Jul | 28.69 → 34.71 | CN (5 posts) | MW 34.76 (09-02); MS 34.22 | close | M |
| 8 | FY28 revenue | 60,511 / 60,500 | CN 07-23 | MS | exact | H |
| 9 | Jefferies target raise on 09-11 | $1,155 → $1,185 | StreetInsider 09-11 | MarketScreener 09-11; edgex 09-12 | exact; **conflicts with the brief** | H |
| 10 | Bernstein target raise | $1,206 → $1,298 | POS-23 (Investing.com 09-16) | Bitget/Zhitong 09-16/17 | exact | H |
| 11 | Mean target $1,237.34 | 37 analysts | MS 09-18 / 09-29 | TIKR 09-21 | exact | H |
| 12 | Q2 adjusted-EBITDA miss | $1.25B vs $1.28B | StockStory 07-22 | Reuters 07-22 (LSEG) | close | H |
| 13 | Zacks FY26 EPS −1.34% over one month | 30.49 | ZK 09-18 | YF FY26 31.02 → 30.74 | close | M |
| 14 | FY27 guide in Jan; long-term guidance in Mar-27 | — | edgex 09-12 (Jefferies) | brief §4 (CMD spring 2027) | close | M |

---

## 4. Arithmetic

- **A1. Gap to the research range.** 9,574 − 8,750 = 824 (−8.6%). To 8,600: −10.2%. To 8,900: −7.0% [inputs: MS; brief].
- **A2. EPS-to-EBITDA factor.**
  - MS FY27 net income / EBT = 6,655 / 8,864 = 0.751.
  - 1% of EPS ≈ 66.6M of net income, which is 66.6 / 0.751 = $88.6M of EBITDA = 0.93% of 9,574.
  - This assumes D&A, interest and share count are fixed. Buybacks bias it: flat EPS with a falling share count means EBITDA is slightly down.
  - −0.7% EPS × 0.93 × 9,574 ≈ −$62M.
- **A3. Proxies for the Jan-2026 vintage of FY27 EBITDA.**
  - EPS-scaled: 1 − 20.96/24.85 = 15.65%; × 0.93 = 14.6%; 9,574 × 0.854 ≈ **8,180**.
  - Revenue-scaled at constant margin: 9,574 × 49,236/52,740 ≈ **8,938**.
  - Both are proxies, not observed data. Prolec D&A and buybacks distort them.
- **A4. Revision steps.** FY27 EPS: 23.27/20.96 = +11.0%; 24.78/23.27 = +6.5%; 24.85/24.78 = +0.3%; Jan → Sep 24.85/20.96 = +18.6%. Revenue: 52,740/49,236 = +7.1%. FY28 EPS: 34.71/28.69 = +21.0%.
- **A5. Short EV under drift.**
  - E02 central +4.3%, sticky −0.6%, so the gap between frames is 4.9pt. EV(f) = 4.3 − 4.9f.
  - Cross-check of E02's central frame:
    - E[NTM] = 0.14×10,183 + 0.20×9,769 + 0.34×9,365 + 0.32×8,693 = 9,345 (−5.3% vs 9,865).
    - Probability-weighted multiple = 25.2x, roughly the flat-price 25.1x.
    - So E02's central EV is essentially the estimate part; the "surprise premium" sits in the dispersion of multiples across scenarios.
- **A6. Price per 1% of FY27 EBITDA** at 25x: 95.7 × 25 / 266.33 = $8.99/share ≈ 0.93% of $962.49.

---

## 5. General question bank

- **G2 / G22.** Consensus moved at prints, not between them. The FY27 bar rose 18.6% in 2026 without any FY27 guidance.
- **G5.** Over nine months the stock has run ahead of the move in estimates: FY27 EPS +18.6% vs the price up ~40% year to date [edgex 09-12, "42% YTD"; Jefferies/Investing 09-17]. TIKR reads it the other way ("estimates catching up to the stock") because the NTM P/E fell 56.3x → 44.7x [TIKR 09-21].
- **G7.** The bear's variant is not being adopted. It is a timing/interpretation gap that the Street has not priced, and no revision momentum supports it yet.
- **G14.** Jefferies expects long-term guidance in March 2027. A reset at that point could fall outside a short-into-January window.
- **G20.** Two definition traps:
  - MS and Equibles share a feed, so they are not independent.
  - The FY26 EPS pools mix bases (with and without the Prolec gain).

## 6. What would change this

1. Any major broker cutting FY27 EBITDA by ≥5% before 10-28 would overturn "not moving".
2. MarketScreener's FY27 EBITDA below ~$9.3B on any re-fetch.
3. The Q3 print missing $1,706M **and** analysts trimming FY27 ≥3% within 48 hours, which would put f at ~0.35 or more.
4. A newly announced Dec-2026 investor event, which moves the reveal earlier.

## 7. Disagreements with the master brief

- **Jefferies:** the target was *raised* from $1,155 to $1,185 on 2026-09-11 (reiterated 09-17). It was not a cut on 09-22 [StreetInsider; MarketScreener; Investing.com].
- **Consensus EPS sources:** MarketScreener and Equibles are one feed, so they should not count as two sources for $24.85.
- **"Street" FY27 EBITDA:** it is not a single number. It is $9.45B (GLJ's vendor) to $9,574M (MS), so the gap itself carries about ±$124M of vendor noise.

## 8. Open items

- **FY27 EBITDA time series:** needs FactSet, Bloomberg or Visible Alpha (terminal or library access). Wayback copies of MarketScreener returned nothing.
- **Exact date of the Yahoo snapshot:** match the $921.97 prior close against Nasdaq daily history.
- **cnyes FactSet posts for August–September:** none found. Watch for the first post after Q3.
- **Q3-day revisions:** capture MS, YF and Zacks on 10-27 and again on 10-30 to measure f directly.
