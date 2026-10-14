# Q3'26 preview (reports 2026-10-28, after the finals)

_D07_q3_preview — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 02:33:47. Requests 33, input tokens 2675382, output tokens 33794._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova (GEV): Q3'26 earnings preparation (reports 2026-10-28, five days after the finals)

## 1. Bottom line

- **Consensus is in two layers.** Revenue, EPS and EBITDA have two or more sources each. Orders, gas GW/SRAs, FCF and segment margins have no public consensus I could find. Q3 revenue is $12.01–12.12B across three sources. Q3 EPS is $4.04–4.09 across four. Q3 EBITDA is $1,706M (MarketScreener) and $1,728M (ChartMill; the page snapshot is dated 2026-08-20). [S1: MarketScreener calendar, fetched 2026-09-29 (research PP-19)] [S2: ChartMill GEV analyst-ratings page, quarterly table] [S3: Zacks via Yahoo Finance, 2026-09-16]
- **Street FY26 EBITDA sits in the upper part of the guide range.** H2 margin is 16.3% on either consensus source, against a guide midpoint of 15.0%. That leaves Q4 at about 18.1% margin and Wind at about +$257M in Q4. Wind's best quarter since the spin was +$19M. [S1: Q2'26 release, 8-K 0001996810-26-000147] [S2: ChartMill FY26 EBITDA $6.4B]
- **Q3 EBITDA consensus is at or above the top of the range I rebuilt from the segment guides** ($1,535–1,716M). The Q3 guide has no numeric company-level margin; it only promises "margin expansion" on Q3'25's 8.1%. [S1: Q2'26 call transcript, gevernova.com 07-22-2026] [S2: Q3'25 release, 0001996810-25-000159]
- **The line that has moved the stock on earnings days is the company-level adj EBITDA margin guide, plus EBITDA/EPS against consensus.** Orders and FCF have not. Q1'26 (margin guide raised) closed +13.75%. Q2'26 (FCF guide raised by $5B at the midpoint, record orders, margin guide held, EPS miss) closed −8.69%. Both previous Q3 prints only reaffirmed guidance: +1.25% and −1.59%. The sample is 10 events, so this is a pattern, not a proven cause. [S1: research BX-13, corpus prices + Yahoo chart] [S2: MoneyTimes and Reuters, 2026-07-22; TIKR, 2026-04-23]
- **Intra-quarter, the CEO leaned positive** at Morgan Stanley Laguna on 2026-09-16:
  - "very strong" Q3 orders
  - $200B backlog "very early in 2027"
  - H2 gas commitments of ~20 GW "likely to prove to be conservative", with Q4 bigger than Q3
  - premium pricing on 12 GW of 2030-31 slots
  - Wind "much better" in H2
  - Q3 "another good opportunity" for buybacks

  He also named tariffs and Section 232 as live uncertainties for Wind. [S1: Laguna transcript PDF, gevernova.com] [S2: MarketBeat/Transcript Daily, 2026-09-18/21]
- **Q3 is not the decisive test for a FY27-margin thesis.** Management will not guide FY27 until January 2027. The Q3 10-Q will, however, print the 9/30 RPO conversion percentages, the Q3 buyback and possibly the Vineyard Wind settlement cost. The settlement was signed 2026-09-16, inside Q3, on confidential terms. [S1: Laguna p.10-11] [S2: GEV press release and Reuters, 2026-09-16]

---

## 2. Answers

### Q1. Q3'26 consensus, line by line

| Line | Value | S1 | S2 / S3 | Status |
|---|---|---|---|---|
| Revenue | $12,013M / $12.07B / $12,118M | MarketScreener calendar, Q3'26 column (fetched 09-29) | Zacks $12.07B (+21.11% YoY; SwingTradeBot 2026-09-18); ChartMill $12.118B (29 analysts) | Close (spread 0.9%) |
| Adj EBITDA | $1,706M (14.2%) / $1,728M (14.3%) | MarketScreener | ChartMill quarterly table | Close. **Definition caveat:** ChartMill shows +60.74% YoY, which implies a Q3'25 base of ~$1,075M. GEV's reported Q3'25 adj EBITDA was $811M. So ChartMill's history is not on GEV's adjusted basis, though its FY26 figure ($6.4B) matches MarketScreener ($6,359M). |
| EPS | $4.08 (Zacks) / $4.09 (ChartMill) / $4.04 (Chartloom) / $4.08, range $3.08–5.28 (TipRanks) | Yahoo/Zacks 2026-09-16 | ChartMill; TipRanks; research BX-14 (Chartloom) | Close |
| EPS basis | GAAP-comparable. Zacks +148.8% YoY implies a base of $1.64, which equals GEV's Q3'25 GAAP diluted EPS ($1.64). | Q3'25 release, Total Company table | Zacks/Yahoo % change | Exact. GEV publishes no adjusted EPS (research RQ-32). |
| EPS revisions | −1.5% (1M), −2.1% (3M) ChartMill; −2.9% over 30 days Zacks | ChartMill | Yahoo/Zacks 09-16 | Close. Estimates drifted down into the print. |
| FCF | No Q3 consensus found. FY26 consensus $12,017M implies H2 ≈ $2,120M. Guide: Q3 "positive FCF". | MarketScreener FY (research) | Q2'26 transcript (PP-17) | **[SINGLE-SOURCE]** for FY FCF. Looked at ChartMill, Zacks and TipRanks; none show quarterly FCF. |
| Orders | No public consensus found. Base Q3'25 = $14.6B; Q2'26 = $24.2B. Management: "very strong third quarter orders performance". | Q3'25 release | Laguna p.3; MarketBeat 09-18 | Consensus: **not found** (Visible Alpha-type data is paywalled) |
| Gas GW / SRAs | No consensus. Management framing: H2 new commitments ~20 GW, "likely… conservative", Q4 > Q3; ≥125 GW by YE26 (from 116); shipments at 5 GW/quarter in Q3 and Q4 (Q2 was 3.3 GW). | Laguna p.3-4 | Q2'26 release; MarketBeat 09-18 | Management framing only. It implies Q3 gross commitments below ~10 GW if H2 is exactly 20 GW. |
| Segment margins | No public segment consensus. Guide: Power ~17–18% on +17–19% revenue growth; Electrification $3.8–4.0B at a margin "modestly above" Q2's 18.4%; Wind revenue down low-double-digits, EBITDA ≈ break-even. | Q2'26 transcript (research PP-12, 15, 16) | Reuters, 2026-07-22 (Wind Q3 revenue decline) | Guide: two sources. Consensus: **not found**. The 20.7% FY27 Power figure remains GLJ-only. |

**Definition trap on FY EPS.** FY26 EPS consensus is either $30.49 (Zacks, 09-16) or $15.36–15.52 (MarketBeat/Erste 09-23; ChartMill). The ~$15 gap is the H1 Prolec remeasurement gain ($3,992M pre-tax) plus the Proficy gain ($330M) (Q2 release, footnote (a)). Anyone quoting "FY26 EPS" must state which basis.

### Q2. H2/Q4 hurdle, recomputed

Inputs:
- H1'26 revenue $20,442M, adj EBITDA $2,146M (Q2 release six-month columns; 10-Q 0001996810-26-000148).
- FY26 guide: revenue $45.5–46.5B, margin 12–14% (Q2 release; MoneyTimes 07-22).

| Case | FY EBITDA | H2 EBITDA | H2 revenue | H2 margin |
|---|---|---|---|---|
| Low margin × low revenue | 5,460 | 3,314 | 25,058 | **13.23%** |
| Low margin × high revenue | 5,580 | 3,434 | 26,058 | 13.18% |
| Midpoint (13% × 46,000) | 5,980 | 3,834 | 25,558 | **15.00%** |
| High margin × high revenue | 6,510 | 4,364 | 26,058 | 16.75% |
| High margin × low revenue | 6,370 | 4,224 | 25,058 | **16.86%** |
| Consensus (MarketScreener: 6,359 / 46,282) | 6,359 | 4,213 | 25,840 | **16.30%** |
| Consensus (ChartMill: 6.4B / 46.511B) | 6,400 | 4,254 | 26,069 | 16.32% |

- **Confirmed: 13.2–16.9%**, taking the low-revenue corners. The low end is 13.2% whichever revenue you pair with 12%, so the range holds under any pairing.
- The consensus FY margin is 13.74%. It sits 86% of the way up the guide's EBITDA range: (6,359 − 5,460) / (6,510 − 5,460).
- **Q4 implied** = FY consensus − H1 − Q3 consensus:
  - MarketScreener: $13,827M revenue / $2,507M EBITDA, **18.1%**
  - ChartMill's own Q4 row: $13,954M / $2,520M, **18.1%**
  - Management: Q4 will be "the highest revenue and EBITDA" quarter (Q2 transcript, research PP-20).
- **Wind:** H1 = Q1 −$382M + Q2 −$275M = −$657M (Q2 release Wind table; Reuters 07-22 for the −$275M). To hit ~−$400M, H2 needs **+$257M**. With Q3 at break-even per the guide, all of it falls in Q4. Reference points: last positive quarter +$19M (Q4'24); Q4'25 recast −$225.2M (research PP-21, realignment supplement). **Confirmed.**
- **Q3 guide-implied range** (research PP-18, recomputed):
  - Power: $4,862.9M × 1.17–1.19 = $5,690–5,787M; × 17–18% = $967–1,042M
  - Electrification: $3.8–4.0B × 18.4–19.5% = $699–780M. The 19.5% ceiling is an analyst assumption.
  - Wind: $2,303–2,383M / $0
  - Corporate: −$106M to −$131M (FY $450–500M less H1 $238M, split over two quarters; assumption)
  - Eliminations: about −$36M
  - **Total: revenue $11,757–12,134M; EBITDA $1,535–1,716M.** MarketScreener's $1,706M sits $10M below the top. ChartMill's $1,728M sits $12M above it.
- **FCF:** the guide implies H2 of $1,603–2,603M ($11.5–12.5B less H1 $9,897M). Consensus H2 is about $2,120M, just above the midpoint.

### Q3. What management said during the quarter

8-Ks since the Q2 print: only **0001996810-26-000153** (filed 2026-08-27, Item 5.02). CFO Parks retires 2027-04-02. Claire McDonough joins 2026-11-01 as advisor and becomes CFO on 2027-01-01. Second source: GEV press release, 2026-08-27. No Reg FD or guidance 8-K was filed. The only September investor appearance I found was Laguna (2026-09-16). An Exa search for other September CFO or conference appearances found none.

Laguna quotes (CEO Strazik, Morgan Stanley Laguna, 2026-09-16; GEV-hosted transcript PDF; independent copies on Seeking Alpha, GuruFocus and MarketScreener/S&P CapIQ):

- **Orders:** "on the strength of the orders we expect to see in the third quarter, that $200 billion milestone we should hit very early in 2027." (p.1-2). MarketBeat 09-18 confirms.
- **Gas commitments:** "20 gigawatts is likely to prove to be conservative for the second half of the year, but we also aren't going to be at a 40-gigawatt run rate every six months." (p.3). Most of the 12 GW of 2030-31 capacity "will get contracted in the fourth quarter versus the third quarter." MarketBeat confirms both.
- **Pricing:** on the 12 GW added for 2030-31, "a very strong market response to that at premium pricing, in which all 12 gigawatts is in some form of contracting right now." (p.3). MarketBeat confirms. From the Q2 call: H2 gas orders at a $/kW "at the higher end" of 10–20 points above 4Q'25 orders (research PP-26, single transcript).
- **Output:** "We will hit the five-gigawatt run rate for the third quarter and the fourth quarter of this year." (p.4). MarketBeat confirms.
- **Wind:** "we're reaching a profitability pivot point in Wind… the profitability of that business will be much better in the second half of the year than the first, and '27 will be much better than '26." (p.2-3). MarketBeat confirms.
- **Tariffs / 232:** "we continue to have elements of uncertainty with tariffs, 232 classifications, with permitting with end customers." (p.9-10, per research PP-44). MarketBeat paraphrases it. The 10-Q puts the 2026 tariff cost at $100–200M net of mitigation (0001996810-26-000148, MD&A). **[SINGLE-SOURCE]** for the $ estimate; only the filing gives it.
- **Buybacks:** "we've acquired 12.4 million shares at an average price of $560… The third quarter has given us another good opportunity" (p.8-9, per research PP-33). MarketBeat confirms the 12.4M shares at $560 but not the "opportunity" sentence. $3,037M of authorisation was left at 6/30 (10-Q Note 17). If fully used at ~$950, that is about 3.2M shares (computed).
- **Electrification:** data-center orders fall to about 20% of segment orders in Q3/Q4 from about 40% in H1. MarketBeat 09-18 confirms.
- **Wind legal:** Vineyard Wind settlement signed 2026-09-16; GEV withdrew its termination notice; terms confidential (GEV press release; Reuters; Offshorewind.biz 09-17). Whether a cost lands in Q3 Wind segment EBITDA is **not disclosed**.

### Q4. One-day moves on every earnings report since the spin

Returns are close-to-close on the 8-K Item 2.02 date. Price sources for every row: [S1: corpus price table] [S2: Yahoo chart API], research BX-13 and RQ-30. SPY moves are from research grid C.

| Date | Qtr | GEV | SPY | Guide action | What drove it | Driver sources |
|---|---|---|---|---|---|---|
| 2024-04-25 | Q1'24 | +1.46% | n/a | Reaffirm | First print; margin expansion in all segments; backlog $116B | GEV release 04-25-24; MarketBeat report |
| 2024-07-24 | Q2'24 | −4.45% | −2.27% | Raise (per research BR-38; details not re-verified) | Vineyard Wind blade failure blamed on a "manufacturing deviation" | Offshorewind.biz 07-25-24; Recharge 07-24-24 |
| 2024-10-23 | Q3'24 | +1.25% | −0.91% | Reaffirm | Power/Electrification offset more Wind losses; adj EBITDA margin 2.7% | GEV Q3'24 transcript; SEC release 0001996810-24-000080 |
| 2025-01-22 | Q4'24 | +2.67% | +0.56% | Reaffirm | Orders $13.2B +22%; backlog $119B | GEV release 01-22-25; MarketScreener transcript |
| 2025-04-23 | Q1'25 | +3.07% | +1.55% | Reaffirm incl. $300–400M tariffs | Revenue beat; tariff absorbed inside the guide | Reuters 04-23-25; GEV release / Finnhub transcript |
| 2025-07-23 | Q2'25 | **+14.58%** | +0.85% | **Raise: margin low end to 8–9%; FCF $2.0–2.5B → $3.0–3.5B** | Profit beat plus margin and FCF raise | GEV release PDF; Reuters 07-23-25; Investopedia |
| 2025-10-22 | Q3'25 | −1.59% | −0.52% | Reaffirm; **Wind loss guide worsened to ~$400M** | Prolec deal ($5.28B) announced; Dec-9 event announced | 8-K 0001996810-25-000159; Reuters 10-22-25 |
| 2026-01-28 | Q4'25 | +2.73% | −0.01% | Raise (Prolec consolidation) | Revenue beat; the raise was inorganic | Yahoo 01-28-26; research PP-35 (release). One press headline says "slip", so intraday reads conflict. |
| 2026-04-22 | Q1'26 | **+13.75%** | +1.01% | **Raise: revenue, margin 11–13% → 12–14%, FCF** | Orders $18.3B +71% | 8-K 0001996810-26-000063; TIKR 04-23-26; Investing.com |
| 2026-07-22 | Q2'26 | **−8.69%** | −0.12% | Raise revenue and FCF (to $11.5–12.5B); **margin held at 12–14%** | GAAP EPS $2.47 vs $3.04 (−18.8%); Wind loss $275M; "adjusted core profit" miss | Q2 release; MoneyTimes; Reuters; EBC 07-23 |

Summary statistics (computed):
- Mean +2.48%; median +2.07%; mean absolute move 5.42%; 7 of 10 up.
- Daily σ since the spin is 3.34% (research), so a typical earnings day is about 1.6σ.
- Implied move from options: **not found**.

### Q5. Which line moves the stock most

- **Margin guidance and EBITDA/EPS against consensus.**
  - The three largest up-days all came with a margin raise: Q2'25 +14.58%, Q1'26 +13.75%, and the Dec-2025 framework day +15.62% (+6 margin points on the 2028 framework).
  - The largest down-day, Q2'26 at −8.69%, is the only print where revenue and FCF were raised but the margin guide was held and EPS missed.
- **Orders do not separate outcomes.** Q1'26 orders +71% gave +13.75%. Q2'26 orders +88% gave −8.69%.
- **FCF does not either.** The biggest FCF raise ever (+$5.0B at the midpoint, Q2'26) coincided with the worst print-day reaction.
- **Reaffirm-only days** stayed within −1.6% to +3.1% in all five cases.
- **Caveat.** n = 10. Returns are raw, with no measure of surprise size. Research's verifier concluded this supports "no reliable link" statistically, not causation (evidence_lanes, test 4 audit).
- **Research inference on Q2'26.** The EBITDA miss was small: $1,250M actual vs a press figure of $1.28B, about −2.3%. The $1.28B is itself unverified (research RQ-32). Most of the EPS gap was below EBITDA. D&A was $418M vs $202M a year earlier, after Prolec (Q2 release reconciliation). The headline EPS line can "miss" even when EBITDA is roughly in line.

### Q6. What beat, in-line and miss look like

The thresholds below are a research grid; **the team chooses its own marks.**

| Line | Clean beat | In-line | Miss |
|---|---|---|---|
| Adj EBITDA (cons. $1,706–1,728M) | ≥ ~$1,800M (above the guide-implied top of $1,716M by >5%) | $1,620–1,780M | < ~$1,620M |
| Power margin (guide ~17–18%) | ≥ 18.5% | 17–18.5% | < 17% |
| Electrification margin | > 19% | 18.4–19% | ≤ 18.4% (breaks "modestly above Q2") |
| Wind EBITDA (guide ≈ 0) | Positive, with FY −$400M kept | −$50M to +$50M | Clearly negative, or FY Wind loss guide widened (the Q3'25 precedent) |
| FY26 guide | **Margin guide raised or narrowed to the upper half** (the Q1'26 / Q2'25 pattern) | 12–14% reaffirmed, possibly with revenue/FCF raised (the Q2'26 pattern: stock fell) | Margin guide cut, or Q4 hurdle visibly stretched |
| EPS (cons. $4.04–4.09) | > $4.30 | $3.85–4.30 | < $3.85 |
| Gas | Q3 gross commitments ≥ 10 GW; SRA→order conversion ≥ Q2's 10 GW; 5 GW shipped | Commitments of 7–10 GW; ≥ 4.5 GW shipped | Shipments < 4.5 GW (TTM ~14 GW; Q2 3.3 GW) |
| Orders | Above Q2's $24.2B | $18–24B | Below Q1'26's $18.3B |
| 10-Q items | 1-/2-year RPO conversion % stable or higher | Small drift | Further fall (41→37→38→36% one-year history, research PP-27) |

**EPS consistency check (research estimate):**
- Start from Q2's bridge (Q2 release reconciliation): D&A $418M; non-operating benefit income +$119M; net interest income +$73M; restructuring and separation about −$47M; tax rate about 30% ($279M on $928M pre-tax).
- Consensus EBITDA of $1,706M then gives pre-tax income of about $1,433M.
- Net income is about $1.00B at a 30% tax rate, or $1.07B at 25%.
- Using Q2's EPS-to-net-income ratio (2.47/649), that is **about $3.82–4.09**.
- So the $4.08 consensus is consistent with $1,706M EBITDA **only at about a 25% tax rate or with other below-EBITDA help**. At Q2's tax rate, EBITDA in line with consensus would still print EPS of about $3.8, roughly 7% below.

**What each outcome means for the positions (research framing, not a recommendation):**

- **Long:**
  - A beat plus a margin raise matches the only reaction pattern above +10%. It also puts H2 at the Street's 16.3% with evidence behind it.
  - In-line plus reaffirm has historically gone flat, between −1.6% and +3.1%.
  - A miss or held margin guide at ~2x the market multiple is the Q2'26 pattern (−8.69% that day, −12.55% over 5 days).
- **Short:**
  - Q3 does not test the FY27 thesis; January does. A Q3 beat does not refute "Street 2027-28 margins ahead of management". It does weaken it if management raises FY26 margin or signals the 2028 framework moving toward consensus, for example by announcing a December event.
  - The in-quarter tells for a short:
    - the margin guide held while Q4 needs 18%
    - the Wind Q4 +$257M hurdle unchanged or widened
    - falling RPO conversion percentages
    - a Vineyard Wind charge
  - The risk for a short is that Q3 is the quarter management leaned into ("very strong" orders, gas "conservative"), and positive order/backlog headlines land 5 days after the pitch.

### Q7. What finals judges are likely to ask about Q3

1. "Q3 reports five days after this pitch. What would you do on the print, and which single line would make you wrong?" Needs a number and a line: margin guide, Power margin or EBITDA.
2. "Consensus Q3 EBITDA is already at the top of the guide-implied range. Is the bar high or low?" Expect them to probe the team's own rebuild and the 13.2–16.9% H2 range.
3. "GEV has raised at every print. Why would Q3 be different?" Base rate: both previous Q3 prints were reaffirms, and Q3'25 worsened the Wind guide.
4. "Q2'26 raised FCF by $5B and the stock fell 8.7%. What does that tell you about what the market prices?" Tests Q5.
5. "Wind needs +$257M in Q4. Has it ever done that?" Best quarter since the spin: +$19M. Also, the Vineyard Wind settlement cost.
6. "Management says Q3 orders will be very strong and the $200B backlog comes early. Doesn't that break a short?" Separate orders and backlog, which are not in the model, from margin and timing.
7. "What EPS basis is your consensus on?" GAAP-comparable. FY26 is either $15.4–15.5 or $30.5 depending on the Prolec gain.
8. "Did buybacks in Q3 change your share count?" $3,037M left at 6/30; Q3 activity will be in the 10-Q.
9. "The new CFO starts 11-01. Does that change the Q3 call or the January guide style?" Parks still reports Q3.
10. "What did you verify by hand?" Re-derive the H2 hurdle and the Q3 range from the filing pages.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Q3 revenue consensus | $12.01–12.12B | MarketScreener calendar (fetched 09-29) | ChartMill; Zacks/SwingTradeBot 09-18 | Close | H |
| 2 | Q3 EBITDA consensus | $1,706M / $1,728M | MarketScreener | ChartMill (snapshot 08-20) | Close; basis caveat | M |
| 3 | Q3 EPS consensus | $4.04–4.09 | Zacks/Yahoo 09-16 | ChartMill; TipRanks; Chartloom | Close | H |
| 4 | Q3'25 GAAP diluted EPS | $1.64 | Q3'25 release 0001996810-25-000159 | Zacks +148.8% implied base | Exact | H |
| 5 | Q3'25 revenue / adj EBITDA / FCF | $9,969M / $811M / $732M | Q3'25 release | Zacks +21.11% ↔ $12.07B (revenue only) | Exact (revenue); **[SINGLE-SOURCE]** for EBITDA/FCF beyond the filing | H |
| 6 | H1'26 revenue / adj EBITDA / FCF | $20,442M / $2,146M / $9,897M | Q2 release | 10-Q 0001996810-26-000148 | Exact | H |
| 7 | FY26 guide | $45.5–46.5B; 12–14%; FCF $11.5–12.5B | Q2 release | MoneyTimes 07-22; StockTitan | Exact | H |
| 8 | FY26 EBITDA consensus | $6,359M / $6.4B | MarketScreener | ChartMill | Close | M |
| 9 | FY27 / FY28 EBITDA consensus | $9,574M / $13,064M vs $9.652B / $13.184B | MarketScreener | ChartMill | Close (+0.8%, +0.9%) | M |
| 10 | Q3 segment guides | Power +17–19%, ~17–18%; Electrification $3.8–4.0B, >18.4%; Wind ~0 | Q2'26 transcript (PP-12, 15, 16) | Reuters 07-22 (Wind revenue decline) | Close | H |
| 11 | Wind H1 loss | −$657M | Q2 release Wind table | Reuters 07-22 (Q2 −$275M) | Exact | H |
| 12 | Q2'26 reaction | −8.69% | Corpus prices / Yahoo | EBC 07-23 ("fell 8.7%") | Exact | H |
| 13 | Q2'26 EPS miss | $2.47 vs $3.04 | MoneyTimes 07-22 | Investing.com | **Conflict:** MarketBeat says $3.17; EBC gives a $3.04–3.18 range | M |
| 14 | Q1'26 margin guide raise | 11–13% → 12–14% | 8-K 0001996810-26-000063 | Market Daily / Investing 04-22 | Exact | H |
| 15 | Q1'26 reaction | +13.75% | Corpus / Yahoo | TIKR ("jumped 14%") | Close | H |
| 16 | Q2'25 reaction and raise | +14.58%; FCF $3.0–3.5B | GEV release PDF | Reuters / Investopedia | Close | H |
| 17 | Q3'25 reaffirm and Wind worse | ~$400M loss | Q3'25 release | Reuters 10-22-25 | Exact | H |
| 18 | Laguna Q3 orders / $200B | "very early in 2027" | Laguna PDF p.1-2 | MarketBeat 09-18 | Exact | H |
| 19 | H2 gas ~20 GW "conservative"; Q4 > Q3 | — | Laguna p.3 | MarketBeat 09-18 | Exact | H |
| 20 | Buyback 12.4M shares at $560; Q3 "opportunity" | — | Laguna p.8-9 | MarketBeat (12.4M/$560 only) | Partial | M |
| 21 | CFO transition | McDonough 2027-01-01 | 8-K 0001996810-26-000153 | GEV press release 08-27 | Exact | H |
| 22 | Vineyard Wind settlement | 2026-09-16, confidential | GEV press release | Reuters; Offshorewind.biz | Exact | H |
| 23 | 2026 tariff cost | $100–200M | Q2 10-Q MD&A | — | **[SINGLE-SOURCE]** | M |
| 24 | Q2'26 D&A | $418M vs $202M | Q2 release reconciliation | 10-Q | Exact | H |
| 25 | FY26 EPS consensus basis split | $30.49 vs $15.36–15.52 | Zacks/Yahoo 09-16 | MarketBeat/Erste 09-23; ChartMill | Conflict, explained by the Prolec gain | M |

---

## 4. Arithmetic

- **H2 margin:** (FY guide EBITDA − 2,146) / (FY revenue − 20,442). Corners shown in Q2. Consensus: (6,359 − 2,146) / (46,282 − 20,442) = 4,213 / 25,840 = 16.30%.
- **Q4 implied:** revenue 46,282 − 20,442 − 12,013 = 13,827; EBITDA 6,359 − 2,146 − 1,706 = 2,507; 2,507 / 13,827 = 18.13%.
- **Wind:** −400 − (−657) = +257 for H2.
- **Q3 range:** see Q2 (inputs PP-12..17).
- **Guide percentile:** (6,359 − 5,460) / (6,510 − 5,460) = 85.6%.
- **Q2 bridge check:** 1,250 − 9 − 48 − 38 + 119 − 418 + 73 − 279 = 650, against a reported $649M.
- **Q3 EPS estimate:** pre-tax = 1,706 − 418 + 119 + 73 − 47 = 1,433. Net income = 1,433 × (0.70–0.75) = 1,003–1,075. EPS = NI × (2.47 / 649) = $3.82–4.09.
- **Gas net add:** 125 − 116 = +9 GW net. Plus ~10 GW shipped in H2 (5 GW × 2) gives ~19 GW gross, consistent with the ~20 GW H2 guide.
- **Earnings-day stats:** sum of returns +24.78% / 10 = 2.48% mean; absolute sum 54.24 / 10 = 5.42%.
- **Buyback capacity:** 3,037 / ~950 ≈ 3.2M shares.

## 5. General question bank items answered

- **G13 (dated reveal):** Q3 on 10-28 tests the H2 path (Q4 at 18% margin, Wind +$257M) and prints RPO conversion. The FY27 test is the January call (Laguna p.10-11; MarketBeat).
- **G14 (what could push the reveal out):** management's statement that 12 GW of contracting slips into Q4, and no December event listed. Q3'25 announced its December event in the release, so watch whether Q3'26 does the same.
- **G17 (management levers):** buyback cadence, margin-guide wording, Wind charge placement and settlement disclosure; CFO handover.
- **G22 (what has to change):** for the Street's H2 16.3% to hold, the FY margin guide must reach at least its upper half. A reaffirmed 12–14% leaves consensus needing the top.
- **G24 (cash):** the Q3 FCF guide is only "positive". H2 FCF implied by the FY guide is $1.6–2.6B, against H1's $9.9B.

## 6. What would change these findings

- **"Margin guide is the line that matters":** a Q3 with a margin raise and a negative close, or a reaffirm with a ±10% move.
- **"Consensus at the top of the guide range":** if MarketScreener or ChartMill revise Q3 EBITDA below $1,650M before 10-28, the bar resets.
- **EPS consistency check:** if the Q3 tax rate or D&A differ materially from Q2 (for example, the Prolec amortization schedule).
- **Wind hurdle:** if management widens the FY Wind loss (the Q3'25 precedent) while holding the company margin guide.

## 7. Disagreements with the master brief

1. **H2 range.** "13.2–16.9%" holds as stated. The low end is 13.2% with any revenue pairing (13.18% at high revenue). The high end drops to 16.75% if 14% is paired with top-end revenue.
2. **Q3 EBITDA.** The brief says consensus "sits at the top" of the guide range. On ChartMill ($1,728M) it sits **above** the top ($1,716M). ChartMill's historical EBITDA basis also differs from GEV's adjusted basis.
3. **EPS basis.** The brief's Q3 context gives no EPS. Quarterly consensus ($4.04–4.09) is GAAP-comparable, but FY26 EPS consensus comes on two bases ($15.4–15.5 vs $30.5). The brief's FY27 EPS figure ($24.85) should carry its basis; ChartMill shows $24.75 and Zacks $24.09.
4. **Q2'26 EPS consensus** is not a single number: $3.04 vs $3.17 depending on source.

## 8. Open items

- **Orders, gas GW, FCF and segment-margin consensus:** needs Visible Alpha, Bloomberg or FactSet. Nothing free was found.
- **Q2'26 EBITDA consensus ($1.28B):** unsourced. Check Reuters/LSEG body text; the article was paywalled beyond the lede.
- **Vineyard Wind settlement cost and segment placement:** Q3 10-Q, legal proceedings / Wind segment notes.
- **Options-implied earnings move:** check near-dated straddle pricing around 10-28 closer to the date.
- **Whether a December 2026 event is announced:** Q3 release, 10-28.
- **The "another good opportunity" buyback quote** has one transcript source in the research. Verify it directly in the Laguna PDF p.8-9; my page read was truncated before p.8.
- **Q2'24 guide-raise details:** not re-verified. Check the 07-24-2024 release.
