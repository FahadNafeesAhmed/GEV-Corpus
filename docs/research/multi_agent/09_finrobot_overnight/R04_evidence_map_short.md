# Evidence map: SHORT into the January 2027 guide (elements only)

_R04_evidence_map_short — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 04:41:58. Requests 38, input tokens 2945819, output tokens 29182._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV short into the late-January 2027 FY27 guide: evidence mapped to each memo element (research input only)

The team writes every memo sentence and picks every forecast number. All ranges below are labelled "team's choice".

**Source key**

| Key | Document |
|---|---|
| 10Q | 0001996810-26-000148 (Q2'26 10-Q, 2026-07-22) |
| 10K | 0001996810-26-000015 (FY25 10-K) |
| Q2REL / Q1REL / Q4REL / Q3'25REL / Q4'24REL | 8-K EX-99 releases: -26-000147 (07-22-26), -26-000063 (04-22-26), -26-000012 (01-28-26), -25-000159, -25-000004 (01-22-25) |
| DEC25 | Dec-2025 investor-update release (corpus src:2711) |
| 8K-CFO | 8-K -26-000153, Item 5.02 (08-27-26) |
| CFO-PR | GEV CFO release (08-27-26) |
| LAG | GEV-hosted Laguna transcript PDF (09-16-26). I read pp.1–4 this session. The p.10 content comes from D03/F01 reads |
| BOFA | GEV-hosted BofA Global Industrials transcript (2026-03-18, gevernova.com PDF). Read this session; **new** |
| Q4'25CALL | Corpus chunks 246127 / 246149 / 246150 (src:2660) |
| DEC25QA | Corpus chunk 246346 |
| MS | MarketScreener, 09-29-26 |
| TIKR | tikr.com blog, 2026-09-27. Read this session |
| IM | Insider Monkey, 2026-09-18. Read this session |
| GF | GuruFocus GLJ wire, corpus chunk 223211, 09-15-26 |
| INV | Investing.com GLJ initiation, 09-14-26 (facts GLJ-01) |
| MB | MarketBeat Laguna write-up (corpus src:681, 09-18-26) |
| BX | Yahoo/Nasdaq closes (facts BX-13) |
| DEF14A-25 / -26 | 0001996810-25-000049 / -26-000049 |
| yf | yfinance quote, 2026-09-30 08:37 UTC. Pulled this session |

---

## 1. Bottom line

- **The one-number gap is real, but its size depends on a derived figure.**
  - Consensus FY27 adjusted EBITDA is $9,574M, an 18.15% margin on $52,740M [S1: MS] [S2: GF/IM, "Street $9.45B", GLJ "22% below"].
  - The research range is $8.6–8.9B, i.e. 16.3–16.9% margin (team's choice) [S1: D01A §4] [S2: D01B §4-J].
  - Caveat: the builds are not independent, and D01A's own statistical band ($7.7–9.6B) contains consensus [R01 #11].
  - The only *published* FY27 Power-margin consensus figure is GLJ's 20.7% [S1: GF] [S2: INV]. The 21.5–23.5% figure is a back-solve [R01 #2].
- **New primary evidence this session supports thesis 1 (Street above plan) but weakens a pure "timing" thesis.**
  - At BofA on 2026-03-18 the CEO said the 2025 backlog-margin step ($8B, +6 pts) comes through "'27, '28, and some of it will trickle through into '29 and '30." He said this is what drives 8.5% → 20% by 2028 [S1: BOFA p.2].
  - So management's own 20%-in-2028 plan already contains the 2025 vintage.
  - The "'29 and '30" line from Laguna refers to the **2026** step [S1: LAG p.10 via D03] [S2: DEC25QA "orders we're taking today. We're shipping in '29 or '30"].
- **Plan vs Street is the cleanest arithmetic element.**
  - FY28 consensus is $13,064M (21.6%) vs the framework $11,200M (20% × $56B), a gap of +16.6% [S1: MS **(FY28 EBITDA is SINGLE-SOURCE)**] [framework S1: Q4REL; S2: BOFA "20% by 2028"].
- **For a January exit, the model's hurdle is the multiple, not the roll.**
  - Today's NTM is 28.2x on $8,770M. January NTM on consensus is $9,865M (+12.5% roll). A flat price needs 25.1x [computed §4].
  - Unchanged consensus at a constant 28.2x gives $1,079, the natural price stop [computed; R01 re-check].
- **Being right on the estimate and getting paid are different events.**
  - Daily σ is 3.34%, which is ~30% over 81 sessions [S1: BX] [S2: E05 verifier, 3.35%].
  - P(short in the red at exit) ≈ 45–50% even though P(guide midpoint < 18.15%) ≈ 80% [E05 A5; D04B]. These are subjective scenario weights.
- **Dated catalysts.**
  - Q3'26 on 10-28, after the finals [S1: GEV events page via E07] [S2: Kalkine 09-29 via R01].
  - The FY27 outlook comes on the January call, date unannounced. Prior Q4 prints were 01-22-25 and 01-28-26 [S1: Q4'24REL] [S2: Q4REL]. The CEO confirmed the January venue [S1: LAG] [S2: MB].

---

## 2. Answers: element-by-element map

### Q1. Header facts

| Element | Fact | S1 | S2 | Note |
|---|---|---|---|---|
| Price | $962.49, 09-29 close | yf 09-30 | Zacks/Yahoo close (D08 #1); MarketBeat last $963.85 (E05) | TIKR's $957.63 is the 09-25 close, a different date |
| Shares | 266,333,581 outstanding; 270M diluted WA (Q2) | 10Q equity section / Note 18 | MS 266,334K | The target formula uses shares outstanding. State which count is used |
| Net cash | $9,113M = 13,120 (incl. restricted) − 2,849 − 1,158 NCI | 10Q balance sheet | 10Q Note 14 (borrowings) | "Cash" includes restricted cash (10Q label) |
| EV | $247,227M [computed] | from rows above | stockanalysis $247.34B | |
| Target formula | Price = (m × NTM EBITDA + 9,113) / 266.33. Jan-27 NTM = 11/12 FY27 + 1/12 FY28 | E02 / F01 A1 | R01 §4 re-check | Multiple m = team's choice |
| Horizon / catalyst | ~4 months to the Q4'26 + FY27 outlook call, late Jan-27 (unannounced; the pattern suggests 01-20 to 01-28) | Q4'24REL (01-22-25), Q4REL (01-28-26) | LAG ("'27 financial outlook in our January earnings call"); MB | E07: the events page listed nothing past 10-28 |
| Who presents | Title conflict: McDonough is CFO effective 1 Jan 2027; Parks presents the Q3/Q4 calls | 8K-CFO Item 5.02 | CFO-PR ("through 2026 inclusive of the third and fourth quarter earnings calls") | **Conflict**; report both (R01 #1) |
| Street target | $1,237.34 (MS, 37 analysts); ~$1,237 (TIKR, 33 targets, low $940); $1,145.83 (MarketBeat) | MS | TIKR 09-27 | Vendor-dependent |
| Bear anchor | GLJ Sell $470; FY27 EBITDA $7.42B | INV | GF; IM | Outside the MS/TIKR analyst sets ("0 Sell" is set-specific) |

### Q2. The one number vs consensus

| Fact | Value | S1 | S2 | Conf. |
|---|---|---|---|---|
| Consensus FY27 adj EBITDA / revenue | $9,574M / $52,740M (18.15%) | MS 09-29 | GF "Street $9.45B"; IM (GLJ $7.42B = "22% below") | M (only one vendor gives the full line) |
| Research FY27 range (team's choice) | $8.6–8.9B = 16.3–16.9% on $52,740M [computed] | D01A §4 (8,744) | D01B §4-J (8,600) | M; builds not independent |
| Deciding line: FY27 Power segment margin | GLJ 18.5% vs "consensus 20.7%"; builds 20.0–20.5% | GF | INV (same wire, GLJ-02) | L; no free segment consensus |
| Power margin history | FY23 9.88% → FY24 12.51% → FY25 14.68% → H1'26 17.63% (Q2 18.82%) | 10Q Note 24; 10K p.72 | Q2REL / Q4REL segment tables | H |
| FY26 Power guide | 17–19% margin | Q2REL guide box | Q2'26 transcript (src:3161) | H |
| Dollar translation of guide midpoints | 17.0% → $8,966M (−6.4%); 17.5% → $9,230M (−3.6%); 18.0% → $9,493M (−0.8%) | computed on MS revenue | E05 A2 grid | H (arithmetic) |

- **Physical translation for the header line.** The research range needs FY27 Power at ~20–20.5%. That is +2.4 to +2.9 pts over H1'26 17.63%. Consensus needs more, but *how much* more is derived, not published.

### Q3. Three numbered theses: top facts per thesis

**Thesis 1: Street FY27–28 runs above management's own plan path**

| # | Fact | S1 | S2 |
|---|---|---|---|
| 1a | 2028 framework: $56B revenue, 20% margin (= $11,200M), FCF ≥ $24B cumulative; Power / Electrification / Wind 22 / 22 / 6% | Q4REL | DEC25; BOFA ("8.5% in '25, 20% in '28") |
| 1b | FY28 consensus $13,064M (21.6% on $60.5B), +16.6% vs framework; margin excess ≈ 1.59 pts × $60.5B ≈ $962M | MS | **SINGLE-SOURCE.** Checked WallStreetZen (net income only: FY28 $9.30B) and Motley Fool (a CAGR, not an estimate) |
| 1c | Straight path FY26 → FY28 plan gives FY27 $8.2B (geometric from the $5,980M guide midpoint) to $8.8B (linear from $6,359M consensus), vs $9,574M | computed; FY26 guide from Q2REL | D03 §1 |
| 1d | **Counter-fact:** the 2028 plan embeds the 2025 vintage. "enough of that cutting in '27 and '28 to drive that shift from 8.5% to 20% at a company level" (Strazik, BofA, 2026-03-18) | BOFA p.2 | Q4'25CALL chunk 246127 ($8B added in '25, +6 pts) |

**Thesis 2: timing. The next margin step (the 2026 vintage) lands after FY28**

| # | Fact | S1 | S2 |
|---|---|---|---|
| 2a | The 2026 change in backlog margin "tells you the equipment margins for '29 and '30, largely" (Strazik, Laguna, 09-16-26) | LAG p.10 (read by D03/F01; not re-opened this session) | MB paraphrase; DEC25QA "orders we're taking today. We're shipping in '29 or '30" (undated web page) |
| 2b | The 2025 step (+6 pts, $8B) flows "'27, '28, and some of it will trickle through into '29 and '30" | BOFA p.2 | Q4'25CALL: "at least $8 billion" again in '26 |
| 2c | GLJ also places high-premium deliveries in 2029 ("high-premium orders to materialize only in 2029") | TIKR (citing Zhitong) | GF (vintage framing) |
| 2d | Equipment RPO landing in 2027: $64,245M × (69% − 37%) = $20,558M | 10K Note 9 | 10Q MD&A RPO table; R01 re-check |
| 2e | SRAs priced 10–20 pts above backlog; SRA-to-order conversion 6–18 months | BOFA p.2 | Q4'25 call via stocksfoundry 01-28-26 |

- **Research reading of 2a–2b.** Timing argues against FY28 *above* 20%, not against FY27 improving.
- **Definition trap.** The CEO's "+5 pts ('24), +6 pts ('25)" is company *equipment* backlog margin. "+11 pts in 2025, +17 since YE22" is the *Power* backlog [Q4'25CALL chunk 246149]. Do not mix the two.

**Thesis 3: delivery record on margin vs what consensus asks**

| # | Fact | S1 | S2 |
|---|---|---|---|
| 3a | FY24 5.83% vs first numeric 5–7% (midpoint 6.0%), **but above** the narrowed 5.5–6% midpoint (5.75%). FY25 8.40% vs 8–9% (midpoint 8.5%) | 10-Q -25-000133 p.36; Dec-24 release src:2653 | Q2'25 release -25-000132; Q3'25REL (R01 row 5) |
| 3b | H2 step over H1: FY24 and FY25 each +2.2 pts. FY26 consensus needs +5.8 (10.5% → 16.3%); the guide midpoint needs +4.5 | D03 Q4 table (10-Q -25-000133) | 10Q non-GAAP table; MS FY26 $6,359M |
| 3c | Q3 EBITDA consensus $1,706M (MS) / ~$1.7B (TIKR) / $1,728M (ChartMill), vs guide-implied $1,535–1,716M | MS | TIKR 09-27 |
| 3d | Wind needs +$257M in H2'26 after −$657M in H1. FY25 Wind missed its own cut guide (~−$400M guide vs −$598M actual) | Q2REL Wind table | Q3'25REL; Q4REL / 10K p.72 |
| 3e | The market reacts to the margin line: Q2'26 (revenue and FCF raised, margin held) closed −8.69%. William Blair: investors "had expected another EBITDA beat with margin expansion" | BX-13 | Reuters via Fancy Hints 07-25 and Marketscold. **Conflict:** Fancy Hints "6.4%", TIKR ">6%", Morgan Stanley note "~9%". Use BX close-to-close and state the basis |

### Q4. Valuation (inputs and formulas only; the team picks the row)

Formula: price = (m × NTM EBITDA + 9,113) / 266.33, with Jan-27 NTM = 11/12 FY27 + 1/12 FY28. Returns are vs $962.49 (stock move, not short P&L).

| NTM EBITDA (inputs) | 20x | 22x | 25x | 28.2x (today) |
|---|---|---|---|---|
| $8,208M (FY27 $8.0B, GLJ + max vintage fix; FY28 $10.5B) | $651 (−32%) | $712 (−26%) | $805 (−16%) | $903 (−6%) |
| $9,000M (FY27 $8.8B; FY28 at plan $11.2B) | $710 (−26%) | $778 (−19%) | $879 (−9%) | $987 (+3%) |
| $9,865M (consensus 9,574 / 13,064) | $775 (−19%) | $849 (−12%) | $960 (0%) | $1,079 (+12%) |

- **Multiple anchors** (team's choice):
  - Today: 28.2x NTM (MS-based) / 27.7x (Chartloom).
  - 25.8x FY27 [computed: 247,227 / 9,574].
  - US grid-peer median ~21x (PWR 22.0x, ETN 21.3x, VRT 20.6x, HUBB 15.1x) [S1: MS valuation pages via D05] [S2: TIKR for VRT/Schneider only; the others **SINGLE-SOURCE**].
  - Own trough 15.6x NTM EV/EBITDA, Apr-25 (Chartloom, not point-in-time) [S1: Chartloom] [S2: BX price closes; series **SINGLE-SOURCE**].
- **Drawdown anchors:** since the spin, the median closing drawdown is −24.6% (→ $726) and the worst is −38.3% (→ $594). Three of the five came while the S&P rose [S1: BX-03..08] [S2: evidence_brief Test 14].
- **Model tie-out items the judges will check:**
  - Diluted (270M) vs outstanding (266.33M) shares.
  - Restricted cash included in the $13,120M.
  - NCI deducted.
  - Adjusted EBITDA definition (company non-GAAP, which matches the proxy AIP definition; E04).

### Q5. Catalysts with dates and pass marks (research proposals; the team sets its own)

| Date | Event | S1 / S2 for the date | Pass mark (short) | Fail mark (short) |
|---|---|---|---|---|
| 10-28, 7:30 ET | Q3'26 + 10-Q; FOMC at 14:00 the same day | GEV events page / Kalkine 09-29 | EBITDA < $1,706M; FY26 margin guide held at 12–14%; Power < 17%; no December event announced | FY26 margin raise (Q1'26 raise day was +13.75%); December event notice |
| 11-11 | Siemens Energy FY26 + mid-term (FY28 14–16%) | SE IR / SE Q3 call (E07) | No peer margin raise | Peer target raise |
| Dec (8–9 FOMC; PJM 2029/30 auction, results ~12-22; ERCOT audit 12-10) | Macro / power policy | Fed calendar / ESAI, PJM (E07) | Hike; weak load evidence | — |
| YE26 | Gas under contract ≥125 GW (116 at Q2); backlog GW > SRA GW | Q2REL / T2Q (Strazik) | < 125 GW; H2 signings well under ~20 GW | ≥125 GW |
| Late Jan-27 (unannounced) | FY27 outlook + 2026 backlog-margin change (≥$8B floor) | LAG / MB | Midpoint ≤ ~17.0% **and** dollars ≤ ~$9.0B; 2028 held at $56B / 20% | Low end ≥18%, or dollar midpoint ≥ ~$9.4B |
| Spring-27 | CMD, 2030 outlook | MB / Transcript Daily 09-21 | 2028 held | 2028 raised |

- **Date conflict.** A Morgan Stanley note summarised on 07-25 called a "December analyst day" the next checkpoint [Fancy Hints 07-25]. The CEO later (09-16) set January for the FY27 outlook and the spring for the CMD [LAG; MB]. The later, first-party statement governs; watch the 10-28 call for any December notice.

### Q6. Risks with observables

| Risk | Observable | Evidence (S1 / S2) |
|---|---|---|
| Horizon noise swamps the edge | σ 3.34%/day ≈ 30% over 81 sessions vs ~−8% value impact of an 8% cut | BX; E05 verifier 3.35% |
| Q3 beat-and-raise before January | 10-28 FY26 margin guide ↑ | Up-day precedents +13.75% / +14.58% / +15.62% all came with margin raises (BX-13; D07 Q5) |
| January bundles positives | Backlog-margin page (≥$8B, "floor… substantially higher"); ≥125 GW; $200B backlog "very early in 2027"; new buyback (Dec-24 $6B and Dec-25 $10B came at December events) | LAG p.1; Q3'25 call chunk 468475 / 10Q MD&A liquidity |
| Revenue-led guide close to consensus in dollars | Revenue guide ≥ $54B (Lark $54.5B **SINGLE-SOURCE**); 17.5% × $54.5B = −0.4% vs consensus | Lark 08-04; E05 A2 |
| AI-capex sentiment | Hyperscaler Q3 capex prints ~10-28 to 10-30 (dates estimated) | E07; Reuters 09-15 via E06 (DeepSeek −21.5% reversed) |
| Rates (a tailwind for the short) | Oct/Dec FOMC hike odds 49% CME / 64% Kalshi | Investing.com 09-30 / Straits Times (E07) |
| Buyback support | $3,037M left = 1.18% of shares; the CEO says Q3 was "another good opportunity" | 10Q Note 17 / TIKR (4.3M shares at $854 avg through 6/30) |
| Wind swing | CEO: "'27 will be much better than '26". Swing −$400M → 0 ≈ +0.76 pts of company margin | LAG p.2 (read) / MB; E05 A3 |

### Q7. Kill rule (research proposal)

| Leg | Trigger | Basis |
|---|---|---|
| Early (10-28) | FY26 margin guide raised above 12–14%, or a December investor event announced | E05 Q2/Q7; BX up-day precedents |
| Guide (Jan) | FY27 margin low end ≥ 18%, **or** EBITDA dollar midpoint ≥ ~$9.4B (−2% vs $9,574M) | D04B; E04 dollar-leg argument |
| Plan | 2028 raised to ≥ ~$12.5B EBITDA | F01 Q5 |
| Price stop | $1,079 = (28.2 × 9,865 + 9,113) / 266.33 | computed; R01 §4 |

### Q8. Five strongest counter-arguments to pre-empt, and the fact that answers each

| # | Counter (source) | Strongest supporting facts | Answering facts (with limits) |
|---|---|---|---|
| 1 | First guides are sandbagged, so a sub-18% guide does not mean consensus is wrong (E04, E05) | FY26 guide 11–13% → 12–14% within ~3 months [S1: Q1REL] [S2: Q2REL "remains 12%-14%"]. AIP EBITDA actual vs target +1.75% / +10.2% [S1: DEF14A-25 p.54; DEF14A-26 p.50] [S2: Q4'24REL; Q4REL]. "I always have an expectation that we do better internally relative to what we commit to you externally" [LAG p.4, read; MB] | A raise is not a beat: H1'26 was 10.5% vs 12–14%. Both completed years finished below the first numeric midpoint (3a). The bonus cushion is n=2, dollar targets set against qualitative guides [R01 #10]. **Limit:** this counter is only answered by the dollar leg of the kill rule |
| 2 | Guide/framework days go up, and January bundles positives (E05) | +5.01% / +2.67% / +15.62% / +2.73% [S1: BX-13] [S2: Barron's 12-12-25] | The set is selective: the Dec-24 release day closed −2.34%, and 3 of 11 event days closed down [R01 #5; PP-36]. +2.67% was a reaffirm. No FY guide has ever been given first on a January call. Q2'26 margin-held: −8.69% (3e) |
| 3 | The 2025 vintage ships '27-'28, so a big FY27 margin step is legitimate (BOFA, new; E06 roll-forward) | BOFA p.2 quote (2b). "'27 and beyond" [S1: Q4'25CALL src:2660] [S2: trade-press copies src:149/293 per D03] | The same CEO statement ties the 2025 vintage to the *20% in 2028* plan (1d). Consensus FY28 at 21.6% needs more than that vintage, and the next step is '29-'30 (2a). **Limit:** this does not show FY27 consensus is too high, only that FY28 is above plan |
| 4 | Revenue and output upside offsets margin (E05) | 5 → 6 GW/quarter "sometime in the second half of next year" [S1: LAG p.3, read] [S2: MB]. Lark $54.5B [SINGLE-SOURCE] | Q2'26: a revenue raise did not rescue a held margin (3e). A −8% dollar gap needs a midpoint ≤ 16.2% on $54.5B [E05 A2]. The CEO: H2 commitments "aren't going to be at a 40-gigawatt run rate every six months" [LAG p.3, read; TIKR] |
| 5 | The stock sits near the bottom of its own multiple range; +39% NTM roll; GE 2000–02 is a bad analogue (E06) | NTM P/E 33.8–68.9x (median 50.8x), Chartloom [SINGLE-SOURCE series]. EV/EBITDA-to-growth 0.65 ≈ Vertiv 0.64 [D05, MS] | Into January the roll is only +12.5% (8,770 → 9,865), not +39%. A flat price needs 25.1x. The Chartloom range is not point-in-time (trough upper bound). The Apr-25 trough was 15.6x. GE P/E halved (42.6x → 21.1x) while EPS rose 19% [S1: GE ex-99b on SEC] [S2: NY Post 04-16-02, via E06]. **Limit:** the GE case also carried conglomerate and Enron-era factors |

Also cite if asked:
- The GLJ day was mostly sector: excess vs peers ≈ −3%, not significant (brief §5).
- Hedge-fund holders fell from 118 to 106 in Q2 [S1: IM] [S2: D05].
- Short interest is 3.29% [S1: IM] [S2: MarketBeat / stockanalysis, E05].

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Price | $962.49 | yf 09-30 | Zacks/Yahoo (D08) | exact | H |
| 2 | Net cash / EV | $9,113M / $247.2B | 10Q balance sheet | stockanalysis $247.34B | close | H |
| 3 | FY27 consensus EBITDA | $9,574M | MS | GF/IM ($9.45B) | close (−1.3%) | M |
| 4 | GLJ FY27 EBITDA / Power margin | $7.42B / 18.5% vs 20.7% | GF | IM ($7.42B); INV | exact | M-H |
| 5 | 2028 framework | $56B / 20% | Q4REL | BOFA; DEC25 | exact | H |
| 6 | FY28 consensus | $13,064M | MS | none | SINGLE | L-M |
| 7 | 2025 vintage timing | "'27, '28 … trickle '29 and '30" | BOFA p.2 | Q4'25CALL chunk 246127 ($8B, +6 pts) | consistent | H |
| 8 | 2026 vintage timing | "'29 and '30, largely" | LAG p.10 (D03) | DEC25QA; MB | directional | M |
| 9 | Equipment RPO → 2027 | $20,558M | 10K Note 9 | 10Q MD&A | exact | H |
| 10 | Q3 EBITDA consensus | $1,706M / ~$1.7B | MS | TIKR | close | M |
| 11 | FY27 FCF consensus | ~$7.4B | MS | TIKR ("around $7.4 billion") | close; **upgraded from single** | M |
| 12 | Street target | $1,237.34 / ~$1,237 / $1,145.83 | MS | TIKR; MarketBeat | conflict (vendor set) | M |
| 13 | Q2'26 day move | −8.69% close | BX-13 | Fancy Hints 6.4%; TIKR >6% | conflict (basis) | M |
| 14 | FY26 margin guide raise | 11–13 → 12–14% | Q1REL | Q2REL | exact | H |
| 15 | FY25 margin vs guide | 8.40% vs 8–9% | 10K / Q4REL | Q2'25 release | exact | H |
| 16 | Wind FY25 guide vs actual | ~−400 vs −598 | Q3'25REL | Q4REL; 10K | exact | H |
| 17 | Bonus EBITDA cushion | +1.75% / +10.2% | DEF14A-25 / -26 | Q4'24REL / Q4REL | exact | H |
| 18 | Buyback remaining | $3,037M | 10Q Note 17 | LAG p.9 / E05 | exact | H |
| 19 | CFO on the Jan call | title McDonough / presenter Parks | 8K-CFO | CFO-PR | conflict | H |
| 20 | Output ladder | 5 GW/q → 6 GW/q in H2'27 | LAG p.3 (read) | MB | exact | H |
| 21 | HA services $/GW | $0.5B over 20 yrs | LAG p.2 (read) | TIKR | exact | H |
| 22 | Deposits on SRAs | 20–25% of turbine contract | BOFA p.2 | none in a GEV filing | SINGLE | M |
| 23 | Hedge-fund holders | 118 → 106 | IM | D05 | close | M |

## 4. Arithmetic

- **EV:** 962.49 × 266.33 − 9,113 = 247,227. FY27 multiple = 247,227 / 9,574 = 25.8x.
- **NTM EBITDA:**
  - Today: 0.25 × 6,359 + 0.75 × 9,574 = 8,770 → 28.2x.
  - Jan-27: 0.9167 × 9,574 + 0.0833 × 13,064 = 9,865 → 25.1x at a flat price. Roll = 9,865 / 8,770 − 1 = +12.5%.
- **Grid (§Q4):** e.g. (25 × 9,000 + 9,113) / 266.33 = 879.0; (28.2 × 9,865 + 9,113) / 266.33 = 1,078.8; (22 × 8,208 + 9,113) / 266.33 = 712.2.
  - Base NTM = 0.9167 × 8,800 + 0.0833 × 11,200 = 9,000.
  - Short-best NTM = 0.9167 × 8,000 + 0.0833 × 10,500 = 8,208.
- **Framework gap:** 13,064 / 11,200 − 1 = +16.6%. Margin excess = (21.59% − 20%) × 60,500 ≈ 962.
- **Straight path to FY27:**
  - Linear from consensus: (6,359 + 11,200) / 2 = 8,780.
  - Geometric from the guide midpoint (13% × 46,000 = 5,980): √(5,980 × 11,200) = 8,184.
- **Research range as margin:** 8,600 / 52,740 = 16.3%; 8,900 / 52,740 = 16.9%.
- **Drawdown anchors:** 962.49 × (1 − 0.246) = 725.7; × (1 − 0.383) = 593.9.
- **Buyback:** 3,037 / 962.49 = 3.16M shares = 1.18% of 266.33M.
- **Noise:** 3.34% × √81 = 30.1%.

## 5. General question bank items

- **G1.** A flat price into January needs 25.1x NTM. Physically: Power ~20.5%+ in FY27, and 5 → 6 GW/quarter from H2'27 [LAG p.3].
- **G7.** The gap is interpretation and timing, not information. Management publishes margin in backlog every January and has said where each vintage lands [BOFA; LAG].
- **G9.** The best opposing fact is BOFA: the 2025 vintage lands in '27-'28 (counter #3).
- **G13 / G18.** See Q5 and Q7.
- **G14.** A spring CMD may let the market look through a cautious January guide [MB; Blockonomi per E05].
- **G17.** Management controls:
  - buyback authorisation timing (last two came in December);
  - bundling of the January release;
  - the CMD date;
  - SRA deposits of 20–25% [BOFA].
- **G24.** FY27 FCF consensus is ~$7.4B, down from ~$12B, with FY26 lifted by working capital [S1: MS] [S2: TIKR].

## 6. What would change this

- **Thesis 1 fails if:**
  - a paid segment consensus shows the FY27 gap sits in Wind or Corporate; or
  - the 2028 plan is raised toward ~$13B at the CMD or on 10-28.
- **Thesis 2 fails if:**
  - the January backlog page attributes 2026 margin growth to 2027–28 deliveries; or
  - the LAG p.10 wording, re-read in full, turns out narrower than quoted (I could not reach p.10 this session: the PDF read stopped around p.4).
- **Thesis 3 fails if** the Q3 margin beats and raises (FY26 ≥ 14% top end), or the FY26 finish is ≥ 14%.
- **The valuation leg fails if** the multiple holds ≥ 28x into January on unchanged estimates.

## 7. Disagreements with the master brief

1. **CEO timing.** The brief frames the "'29-'30" line as the margin step relevant to 2027. The BOFA transcript (2026-03-18) shows the 2025 step lands mainly in '27-'28 and underpins the 20% plan. "'29-'30" applies to the 2026 step. The usable form of the timing argument is "FY28 above plan", not "FY27 too early".
2. **"Never beaten first margin guide".** FY24's 5.83% beat the narrowed 5.5–6% midpoint while missing the first 5–7% midpoint. FY26's first guide was raised.
3. **CFO.** McDonough holds the title from 1 Jan 2027, but Parks presents the January call (8K-CFO vs CFO-PR conflict).
4. **"0 Sell".** This is specific to the MS/TIKR analyst sets; GLJ's Sell sits outside them.
5. **Q2'26 reaction.** The size depends on basis: −8.69% close-to-close vs 6.4%/">6%" in press.
6. **FY27 FCF.** No longer single-source (TIKR confirms ~$7.4B).

## 8. Open items

- The full LAG p.10 passage: read the GEV PDF from ~p.9 onward, or the MarketScreener / S&P Capital IQ transcript copy.
- A second vendor for FY28 EBITDA (FactSet, Visible Alpha): still SINGLE-SOURCE.
- The January call date (GEV events page); any December event notice (10-28 call).
- The basis of the Q2'26 day move: check Nasdaq historical closes for 07-21 and 07-22.
- The "December analyst day" reference in Morgan Stanley's July note vs the CEO's January/spring calendar.
- Peer-hedged short arithmetic, and option-implied vol to January: not computed or found.
- Whether the BOFA "20–25% deposit" appears in any GEV filing: not found in 10Q/10K searches by earlier tasks.
