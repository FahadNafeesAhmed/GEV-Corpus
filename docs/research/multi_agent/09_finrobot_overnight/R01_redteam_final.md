# Red-team the final synthesis (catch errors before the team relies on it)

_R01_redteam_final — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 04:24:57. Requests 56, input tokens 4609795, output tokens 46869._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# F01_final_synthesis audit (research input only; the team chooses its own numbers and writes every memo sentence)

## 1. Bottom line

- **The primary-source numbers in F01 hold up. Its framing often does not.** All 20 rows of the hand-verify table that I re-opened match the filings. I could not re-open rows 4, 10 and 18 myself (see the survivor list). The serious problems are claims presented as disclosed or confirmed when they are derived, circular or selective.
  - [S1: 10-Q 0001996810-26-000148, statements and Notes 9/14/24] [S2: Q2'26 release -26-000147; FY25 10-K -26-000015]
- **The CFO claim is wrong as F01 states it. The two sources conflict; they do not agree "exactly".**
  - The 8-K says McDonough becomes CFO effective **1 Jan 2027**, and Parks becomes strategic advisor from that date.
  - GEV's press release says Parks "will continue as GE Vernova's CFO through 2026 inclusive of the third and fourth quarter earnings calls."
  - So Parks is slated to present the late-January call, but McDonough holds the CFO title on that date.
  - [S1: 8-K -26-000153 Item 5.02, 2026-08-27] [S2: gevernova.com CFO-transition press release, 2026-08-27] [S3: CNBC 2026-08-28, "staying on… through its next two earnings calls"]
- **"Consensus implies FY27 Power 21.7–23.5%" is a back-solve, not a consensus figure.** No free segment consensus exists.
  - D01A derives 21.5–23.5% (F01 silently changed this to 21.7%) by assuming Electrification at 21–22%.
  - The only published figure is GLJ's 20.7%. That sits below F01's range and only 0.2–0.7 points above the builds' 20.0–20.5%.
  - [S1: D01A §1] [S2: evidence_brief.md "20.7%… GLJ's figure only"]
- **The equipment-margin "hand re-derivation ties exactly" is circular.** Equipment EBITDA is calculated as Power EBITDA minus the estimated services EBITDA, so the 17.63% check is guaranteed to tie. The 0.0% level comes entirely from four assumptions.
  - [S1: F01 Q2 steps 1–8] [S2: 10-Q Note 24 footnote (b): segment costs exclude D&A; no cost split is disclosed]
- **"Consensus is above trend" depends on which trend you pick.**
  - The recent pace (+6 to +10 points a year) gives the F01 result.
  - The FY23→H1'26 average of the same E01 series (~+11 points a year) gives 13.75% (from E01's 0% base) to 17.35% (from D06's 3.6% base) by FY27. Most of consensus's 12–18% requirement then sits on trend.
  - [computed §4-B; inputs E01 §1, D06]
- **"Never cut" is weaker than F01 says.** Wind was cut at Q3'25 to "~$400M" of losses, and then missed that figure: FY25 Wind EBITDA was −$598M.
  - [S1: Q3'25 release -25-000159 guidance section] [S2: Q4'25 release -26-000012 Wind table; FY25 10-K p.72]

## 2. Answer to the assignment: errata table (ordered by impact)

| # | F01 claim (location) | Verdict | Correct value / correct framing | S1 | S2 | Impact |
|---|---|---|---|---|---|---|
| 1 | "Parks, not McDonough, presents the January call"; evidence row 7 "exact" (BL, §7.1) | **MISLEADING / sources conflict** | The 8-K says McDonough is CFO effective 1 Jan 2027 and Parks is strategic advisor from 1 Jan. The PR says Parks remains CFO "through 2026 inclusive of the third and fourth quarter earnings calls and the publishing of the 2026 10-K". The Jan-27 outlook will likely be presented by Parks while McDonough holds the title. Both the brief's "first under new CFO" and F01's correction are half right. | 8-K -26-000153 Item 5.02 | GEV PR 2026-08-27; CNBC 08-28 | High: it defines the catalyst |
| 2 | Consensus FY27 Power margin "about 21.7–23.5%", cited to [MS][GF] (BL, Q1, A3) | **MISLEADING** (derived, presented as sourced) | D01A back-solved 21.5–23.5% from company consensus, assuming Electrification ~21–22% and assumed Wind/Corporate figures. The only published number is 20.7% (GLJ). Neither MS nor GF publishes Power margin. | D01A §1 | evidence_brief "20.7%… GLJ's figure only" | High: this is the size of the variant |
| 3 | "Re-derived E01 by hand… ties exactly… Check: 17.63% equals reported Power margin" (BL, Q2 step 8) | **MISLEADING** (circular) | The arithmetic is correct (2,755 + 153 − 117 − 308 = 2,483; 2,483 − 640 = 1,843; 1,842 − 1,843 = −1). But step 7 defines equipment as the residual, so step 8 must tie. The level rests on d = 1.75%, Wind services GM 10%, Electrification services GM 32.5% and a 58% overhead share. None is disclosed. | 10-Q Note 24 (costs excl. D&A; no split) | E01 §1 ("any equipment or services margin is an inference") | High |
| 4 | "Trend pace +6 to +10 pts/yr → consensus above trend; +12 to +18 points in ~1.25 years" (BL, A3) | **MISLEADING** | Both passes show year-on-year gains of +13.5/+13, +9.5/+8.7 and ~+11 annualised (FY25→H1'26), with the latest H1-on-H1 at +7 (E01). A full-period average of ~11 pts/yr × 1.25 = +14 puts FY27 at 13.75–17.35%. "+12 to +18" holds only from E01's 0% base; from D06's +3.6% base it is +8.7 to +14.4. | E01 §1 table | D06 central (via F01 Q2) | High: it decides whether the short is a variant |
| 5 | "All four guide/framework days closed up (+2.67% to +15.62%)" (Q4) | **MISLEADING** (selective set) | The numbers are correct on a reaction-day basis. But +2.67% (2025-01-22) was a **reaffirm** of the FY25 guide. The Dec-24 release day was −2.34% (next day +5.01%); the Dec-25 release day was +0.55% (next day +15.62%). Of the 11 report/event days since the spin, 3 closed down (−4.45, −1.59, −8.69). | evidence_lanes_full BX table | PP-36 (Nasdaq + Yahoo closes) | Medium |
| 6 | G2: "FY27 needs +5.15 pts; largest step so far +4.6" | **MISLEADING** | Both figures are measured from the FY26 **guide** midpoint (13.0%). +4.6 is a guided step, not a delivered one. Against FY26 consensus (13.74%), FY27 needs +4.41, which is *smaller* than the +5.34 FY26 step consensus already assumes. The largest delivered step is FY24→FY25, +2.57 (5.83%→8.40%). | MS consensus (CT-02) | FY25 10-K; DEF 14A (FY25 "up 57%" → FY24 ≈ $2.04B) | Medium: it reverses G2's inference |
| 7 | Rating split "30 Buy/7 Hold/0 Sell… exact" (evidence row 14) | **MISLEADING** | "0 Sell" is specific to MS's analyst set. GLJ's Sell ($470, 2026-09-14) is outside it: the MS low target is $940, while the full published range is $470–$1,450. | ad-hoc-news 2026-09-21 citing MS (low $940) | Motley Fool via Webull 2026-09-21 ("$470 to $1,450") | Medium: a judge-question trap |
| 8 | "'Never beaten first margin guide' is out of date; FY24 and FY25 first guides were qualitative and met; FY26's first numeric guide was raised" (§7.2) | **MISLEADING / partly right** | FY24 first guide: "high end of mid-single digits" (qualitative). FY25: "high-single digits", first numeric 8–9% at Q2'25; actual 8.40%, below the 8.5% midpoint. FY26: 11–13% → 12–14% (verified). But a raise is not a beat: FY26 is unfinished, and H1 was 10.5% vs the 12–14% guide. | Q1'24 release -24-000004; Q2'25 release -25-000132 | Q1'26 release -26-000063 (chunk 13603); Q2'26 release "remains 12%-14%" | Medium |
| 9 | "Never cut applies only to company revenue and FCF (Wind was cut)" (§7.3) | **CORRECT but understated** | Add: Wind then **missed** the cut guide ("~$400M of segment EBITDA losses" vs −$598M actual). D01A also reports Wind missing its FY24 guide and the 2028 Wind target falling from 10% to 6% (not re-verified here). | Q3'25 release -25-000159 | Q4'25 release -26-000012 Wind table; 10-K p.72 | Medium: bears on the FY26 Wind −$400M guide |
| 10 | E04: "a guide midpoint of 16.5–17.8% is consistent with consensus still being met" (BL, A5) | **MISLEADING** (n = 2 inference) | The FY25 AIP target of $2,900M vs a result of $3,196M (+10.2%) is verified, and so is FCF ($2,500M vs $3,710M). But these targets are dollar targets set against a *qualitative* guide (2,900 / 36,500 = 7.9% vs "high-single digits"). Applying the two historical cushions to FY27 is a hypothesis, not evidence. | DEF 14A -26-000049 AIP table | Q4'25 release / 10-K actuals | Medium |
| 11 | "FY27 base $8.6–8.9B held in every build and framing tonight" (BL) | **Overstated** | The builds are not independent: same pipeline, same corpus, and a shared Power 20–20.5% choice. D01A's own statistical band ($7.7–9.6B) *contains* consensus ($9,574M at its top). The consensus S2 ("GF Street $9.45B") is GLJ quoting the Street, not a vendor. | D01A §1 | business-news-today 09-16 ("consensus… around $9.5B", per GLJ) | Medium |
| 12 | P(guide < 18.15%) ≈ 82%, E[short] +4.3%, P(win) figures (BL, Q3, Q7) | **Overstated certainty; internally inconsistent** | The arithmetic is exact (§4). The inputs are subjective scenario weights (0.14/0.20/0.34/0.32). Q3 gives long-12m P(win) ~55%, but Q7 says "12 months ~50/50" and V12 says 0.52. | F01 A2 | F01 Q7 | Medium-low |
| 13 | "Company services GM fell 35.1%→31.6% while Power GM before D&A rose 23.0%→28.2%. The improvement came from equipment" (Q2) | **MISLEADING** (mixed bases) | All four numbers are right. But company services GM is *after* D&A and includes Wind and Electrification services, while Power GM is segment-level *before* D&A. The comparison suggests the conclusion; it does not prove it. | FY25 10-K income statement | 10-Q income statement + Note 24 | Low-medium |
| 14 | "Mgmt: YE2022 backlog margin 'approximately breakeven'… contribution-margin basis" (Q2) | **Quote CORRECT; basis is an inference** | Strazik: "directionally, the starting point is approximately breakeven" (margin in Power equipment backlog). "Contribution" is not in the quote. The corpus chunk is dated 2026-01-23, before the 01-28 call (a metadata error). | corpus chunk 246150 (Q4'25 call text) | F01 cites a GEV webcast transcript (not re-opened) | Low |
| 15 | "'29 or '30" Dec-25 statement, "speaker unverified" (BL §7.4) | **UNVERIFIABLE (date and venue)** | Chunk 246346 is a web page (src:2686), not a transcript. The text is verbatim ("orders we're taking today. We're shipping in '29 or '30") but carries no date or speaker tag. I could not re-open the Laguna "'29 and '30, largely" passage: the earningscalls.dev copy truncated before it. | chunk 246346 | — | Low-medium |
| 16 | "~$3.67B was bought back (treasury $3,385M → $7,057M)" (Q4, G24) | **CLOSE** | The cash-flow line is $3,671M and the treasury change is $3,672M. Note 17 gives $3,645M excluding commissions and excise tax. Comparing this with OCF excluding deposits (−$3,015M) is one-sided, per the brief's own caveat. | 10-Q CF "Purchases of common stock for treasury (3,671)" | 10-Q equity statement (Q1 1,299 + Q2 2,373) | Low |
| 17 | Page locators "10Q p.6 (income statement) / p.7 (balance sheet) / p.23 (segment)" | **Probably off by one** | 10-Q contents page: income statement p.5, financial position p.6, cash flows p.7, Note 24 from p.22. The H1'26 segment table sits before the "p.23" header. Cite printed page numbers after checking the PDF. | 10-Q table of contents | 10-Q page headers in text | Low |
| 18 | Row 12 S2 "FactSet $24.78" | **Stale second source** | Dated 2026-07-23 (cnyes), before the GLJ note and Laguna; MS is 09-29. Erste's $24.55 is one broker, not a consensus. | facts CT-10 | MarketBeat 2026-09-21 | Low |
| 19 | Row 11 S2 "Motley Fool 60% CAGR ≈ $13.09B" | **Weak S2 → effectively SINGLE-SOURCE (MS)** | 3,196 × 1.6³ = 13,091. A rounded CAGR is not an estimate. | MS | — | Low |
| 20 | Evidence row 15, SRA share "exact" | **Mislabelled** | The S1 (SE deck, 26/(69+26) = 27.4%) and the S2 (GEV release, 116 GW total) support *different* facts. Each is single-sourced. The Q2 release headline gives only 100→116 GW, not the 53/63 split. | SE Q3 FY26 deck (corpus 251674) | Q2'26 release p.1 | Low |
| 21 | "$500M of services revenue per GW of HA" tagged [SINGLE-SOURCE] (G-list) | **Upgrade → two sources** | "every gigawatt of HAs will generate $0.5 billion of high-margin services revenue over the first 20 years" (Strazik, Laguna 2026-09-16). | LAG-SA (per F01) | earningscalls.dev transcript 2026-09-16 | Positive |
| 22 | Contract liabilities in A6: "14,087 in Note 9" | **CLOSE** | The Note 9 narrative says **$14,088M**. The table total including non-current (40,037 − 25,950) is 14,087. The current line (39,944 − 25,774) is 14,170. | 10-Q Note 9 text | 10-Q Note 9 table / balance sheet | Low |

### Claims that survived (CORRECT, re-opened this session)
- **Price, shares and bridge:**
  - Price $962.49 [yfinance 2026-09-30].
  - 266,333,581 shares outstanding; diluted weighted average 270M for Q2 and 271M for H1 [10-Q].
  - Cash including restricted cash $13,120M; borrowings $2,849M (Note 14: senior notes $2,600M + other $305M − discount $56M; current portion $55M); NCI $1,158M; net cash $9,113M; EV $247,227M.
- **Income statement:** H1'26 equipment/services sales 11,713/8,729 and costs 10,328/5,974; adjusted EBITDA $2,146M (Q2 $1,250M, 11.3%).
- **Power H1'26 segment lines:** 3,834/6,593/22; cost 7,504; SG&A 918; R&D 286; other (100); EBITDA 1,842 (17.63%); Q2 1,031 (18.82%).
- **Power FY25 lines:** 6,420/13,072/276; cost 14,627; SG&A 1,836; R&D 549; other (147); EBITDA 2,902.
- **FY25 company:** services 17,134/11,774; revenue 38,068.
- **Definition trap (MD&A vs segment note):** the MD&A/deck basis of 3,850/6,598 was confirmed against the Q2'26 deck (Q1 1,885 + Q2 1,965; 3,086 + 3,512).
- **Guidance:** FY26 guide 45.5–46.5 / 12–14% / 11.5–12.5 and segments; Q1'26 margin raise from 11–13% to 12–14%; 2028 framework $56B / 20% / ≥$24B / 22-22-6.
- **RPO:** equipment RPO $64,245M with 37/69/97% recognised in 1/2/5 years, so $20,558M ± $642M lands in 2027. $87,821M at June 2026; total $176,284M.
- **CSA profit revisions:** −$319M (FY24 10-K), −$151M, −$218M.
- **Balance sheet and cash flow:** contract liabilities 39,944 / 25,774; treasury stock 7,057 / 3,385; cash-flow contract-liability line 13,695; OCF 10,680, so OCF excluding the contract-liability line is −3,015.
- **Gas capacity and commitments:**
  - 116 GW now, ≥125 GW by YE26; output of 20 GW in Q3'26, 24 GW in 2028, 30 GW in 2030 [Q2 release].
  - 5 GW a quarter in Q3–Q4'26, and H2 commitments "directionally 20 GW… likely to prove conservative" [earningscalls.dev Laguna copy].
- **Dates and pay:** Q3 report 10-28 at 7:30am ET [Kalkine 09-29; E07]. AIP FY25 EBITDA 2,900 → 3,196 and FCF 2,500 → 3,710.
- **Consensus and GLJ:**
  - Consensus target $1,237.34 with 37 analysts (MS via ad-hoc-news 09-21; Pomegra 09-28 "$1,237"; Barron's "~$1,240" via business-news-today).
  - GLJ's FY27 EBITDA $7.4B vs "~$9.5B" consensus.
- **All arithmetic in F01 §4 (A1–A7)** and the Q3, Q4 and Q7 price grids reproduce to the dollar (see §4).

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | CFO title on the Jan-27 call date | McDonough (title), Parks (presents) | 8-K -26-000153 Item 5.02 | GEV PR 08-27 | **conflict** | H that they conflict |
| 2 | Net cash bridge | 13,120 − 2,849 − 1,158 = 9,113 | 10-Q balance sheet | 10-Q Note 14 | exact | H |
| 3 | Power H1'26 EBITDA / margin | 1,842 / 17.63% | 10-Q Note 24 | Q2 deck 17.6% (via E01) | exact | H |
| 4 | Power MD&A basis H1'26 | Equipment 3,850–3,851 / services 6,598 | Q2'26 deck (gevernova.com PDF) | E03 (MD&A) | exact | H |
| 5 | FY25 first numeric margin guide vs actual | 8–9% vs 8.40% | Q2'25 release -25-000132 | Q3'25 release -25-000159 | exact | H |
| 6 | FY26 margin guide raise | 11–13% → 12–14% | Q1'26 release chunk 13603 | Q2'26 release "remains 12%-14%" | exact | H |
| 7 | Wind FY25 guide vs actual | ~−400 vs −598 | Q3'25 release | Q4'25 release / 10-K | exact | H |
| 8 | FY25 AIP EBITDA target / result | 2,900 / 3,196 | DEF 14A -26-000049 | 10-K / Q4 release | exact | H |
| 9 | Equipment RPO → 2027 | 20,558 ± 642 | FY25 10-K Note 9 | 10-Q MD&A RPO table (64,245) | exact | H |
| 10 | CSA revisions | −319 / −151 / −218 | FY24 10-K Note | FY25 10-K; 10-Q Note 9 | exact | H |
| 11 | H1 buybacks | 3,671 (CF) / 3,645 (Note 17) | 10-Q CF | 10-Q equity statement / Note 17 | close | H |
| 12 | Rating set includes a Sell? | MS: 0 Sell; market: GLJ Sell $470 | ad-hoc-news (MS low $940) | Motley Fool/Webull ($470–$1,450) | conflict (set definition) | H |
| 13 | FY27 Power consensus margin | not published; GLJ 20.7%; D01A back-solve 21.5–23.5% | evidence_brief | D01A | n/a (derived) | L |
| 14 | HA services $/GW | $0.5B over 20 years | LAG-SA (F01) | earningscalls.dev | exact | M-H |
| 15 | YE22 Power backlog margin | "approximately breakeven" | chunk 246150 | F01 cites GEV webcast (not re-opened) | quote exact; basis inferred | M |
| 16 | Q3 report date | 10-28, 7:30am ET | Kalkine 09-29 | E07 (GEV events page) | exact | H |
| 17 | SE SRA share | 26 / 95 = 27.4% | SE Q3 FY26 deck p.6 | [SINGLE-SOURCE] | — | M |

## 4. Arithmetic (all re-done)

**A. F01 checks (all reproduce)**
- **EV:** 962.49 × 266.33 = 256,340; minus 9,113 = 247,227.
- **NTM EBITDA and multiples:**
  - Jan NTM = 0.9167 × 9,574 + 0.0833 × 13,064 = 9,865, giving 25.06x.
  - Sep-27 NTM = 0.25 × 9,574 + 0.75 × 13,064 = 12,191, giving 20.28x.
  - Today's NTM = 0.25 × 6,359 + 0.75 × 9,574 = 8,770, giving 28.19x (matches "28.2x MS").
- **E02 expected prices:**
  - January: 0.14 × 1,105 + 0.20 × 1,025 + 0.34 × 913 + 0.32 × 785 = 921.3, a short return of +4.28%.
  - Sep-27: 0.25 × 1,198 + 0.30 × 1,019 + 0.30 × 888 + 0.15 × 722 = 979.9, a long return of +1.8%.
  - Weighted miss price: (0.34 × 913 + 0.32 × 785) / 0.66 = 850.9, or −11.6%.
- **Price grid** (price = (multiple × NTM EBITDA + 9,113) / 266.33):
  - (25 × 9,365 + 9,113) / 266.33 = 913.3.
  - At 22x / 25x on $10.5B: 901.6 / 1,019.8.
  - At 20x / 22x / 25x on 12,191: 949.7 / 1,041.2 / 1,178.6.
  - At 21x: 995.5 on 12,191; 885 on ~10,790.
  - Price stop: 28.2 × 9,865 = 278,193, plus 9,113 = 287,306, / 266.33 = $1,078.8.
- **Worst-case returns:** 1,181 / 962.49 = +22.7%; 646 → −32.9%; 1,338 → +39.0%; 687 → −28.6%.
- **A3, equipment margin needed,** e = (P − w·s) / (1 − w) with s = 28%:
  - w = 0.60: P = 21.7 gives 12.25; P = 23.5 gives 16.75; P = 20.0/20.5 gives 8.0/9.25.
  - w = 0.55: 14.0 / 18.0.
  - E01 table: P = 18.5 gives 4.25–6.9; P = 20.7 gives 9.75–11.8; P = 22 gives 13.0–14.7.
- **A4, split re-derivation:**
  - H1'26: 8,729 − 5,974 = 2,755; add 153; take off 117 and 308, giving 2,483 (37.66% of 6,593); overhead 918 + 286 − 100 = 1,104, × 0.58 = 640; services 1,843 (27.95%); equipment −1 on 3,856.
  - FY25: 17,134 − 11,774 = 5,360; + 300 − 186 − 705 = 4,769; overhead 1,836 + 549 − 147 = 2,238, × 0.58 = 1,298; services 3,471 on 13,072 = 26.55%; equipment −569 on 6,696 = −8.5%.
- **A5, E04 cushion:** 9,574 / 1.102 = 8,688 (16.47%); 9,574 / 1.0175 = 9,409 (17.84%).
- **A7, margin to dollars on 52,740:** 17.0% / 17.5% / 18.0% give 8,966 / 9,230 / 9,493; on $54.5B, 17.5% gives 9,537.5 (−0.38%).
- **Driver bridge:** −118 − 100 + 49 + 25 = −144.
- **Consensus vs research base:** 9,574 / 8,900 = +7.6%; 9,574 / 8,600 = +11.3%.
- **Wind swing:** 400 / 52,740 = 0.76 points.
- **Noise:** 3.34% × √81 = 30.1%.

**B. New computations (this audit)**
- **Equipment-margin pace, E01 central:**
  - −31 → −18 → −8.5 → 0 gives +13, +9.5, then +11.3 a year annualised (8.5 points / 0.75 years).
  - Full period: 31 points / 2.75 years (mid-FY23 to mid-H1'26) = 11.3 points a year.
  - D06: +13.5, +8.7, +11.2 annualised.
  - Latest H1-on-H1 (E01 recast): −7 → 0 = +7.
  - FY27 at the full-period pace: 0 + 1.25 × 11 = 13.75% (E01 base); 3.6 + 13.75 = 17.35% (D06 base).
- **G2 correction:**
  - FY26 consensus margin: 6,359 / 46,282 = 13.74%.
  - FY27 step vs FY26 consensus: 18.15 − 13.74 = +4.41 points.
  - FY26 step implied by consensus: 13.74 − 8.40 = +5.34 points.
  - FY24 margin: FY25 $3,196M "up 57%" gives FY24 ≈ 2,036, and 2,036 / 34,935 = 5.83%. Delivered FY24→FY25 step = +2.57 points.
- **Cash:**
  - H1 capital returned: buybacks 3,671 + dividends 273 = 3,944 (matches the Q2 release's "$3.9B").
  - OCF excluding the contract-liability line: 10,680 − 13,695 = −3,015.
  - Deposits relative to cash: 39,944 / 13,120 = 3.04x.
- **SE SRA share:** 26 / (69 + 26) = 27.4%. **GEV:** 63 / 116 = 54.3%.
- **FY25 first numeric guide:** midpoint of 8–9% is 8.5%; actual 3,196 / 38,068 = 8.40%.

## 5. General question bank items answered along the way

- **G2.** On FY26 consensus, the FY27 margin step (+4.41 points) is *smaller* than the FY26 step already assumed (+5.34). The largest *delivered* step is +2.57 points [§4-B; MS; 10-K].
- **G7.** The Q4'25 call confirms analysts already track backlog margin ("17 points of improvement since year-end '22"). The variant is not information-based [chunk 246150; Q4'25 release "equipment margin in backlog expanding six points"].
- **G11.** H2'26 commitments are "directionally 20 GW… likely conservative" after 40 GW in H1. Slots are being sold for 2032; 12 GW of 2030–31 supply was added "at premium pricing" [earningscalls.dev Laguna copy 09-16; Q2 release].
- **G17.** On the CFO handover, the Q4 call is a Parks call under a McDonough title. The guiding style on the FY27 outlook therefore likely stays Parks'. This weakens "new-CFO reset" framing in either direction [8-K; PR].
- **G20.** Definition traps found:
  - Consensus Power margin is back-solved, not published.
  - "0 Sell" depends on the vendor's analyst set.
  - Services GM after D&A vs Power GM before D&A are different bases.
  - Contract liabilities have three definitions (14,088 / 14,170 / 13,695).
  - Buybacks: 3,671 cash vs 3,645 in the note.
- **G21.** "If wrong, we'd see" an equipment-margin pace holding at ~11 points a year. The series already shows that in two of three intervals [§4-B].
- **G24.** FY26 MS EPS ($30.78) includes the Prolec gain (cash-flow line "(Gains) losses on… business interests (4,428)"). EPS-based FY26 multiples are distorted [10-Q CF; facts CT-04].

## 6. What would change this

- **Errata 1:** a GEV 8-K or IR notice naming the Q4 presenters, or the Q3 10-Q exhibits (the Parks and McDonough agreements are to be filed with the Q3 10-Q).
- **Errata 2:** any vendor segment consensus (Visible Alpha, FactSet or Bloomberg) for FY27 Power margin. A figure ≤ 20.7% would shrink the Power variant to under ~$0.2B.
- **Errata 4:** Q3'26 Power margin. If Q3 is ≥ 19% at a similar mix, the pace of ~11 points a year is being sustained. If ≤ 17.5%, the decelerating (+7) read gains weight.
- **Errata 9:** Wind H2'26. A Q3 Wind loss above ~$150M makes a second consecutive Wind guide miss likely.

## 7. Disagreements with the master brief

1. The CFO line should read: McDonough holds the CFO title from 1 Jan 2027, but Parks is slated to present the Q4 call.
2. "Adj EBITDA margin finished slightly below the first numeric guide in both years": for FY25 this is true only as "below the midpoint" (8.40% vs 8–9%). FY24 had no numeric first guide.
3. "Never cut" should note the Wind cut *and* the subsequent Wind miss (−598 vs ~−400).
4. The $14,087M figure is the Note 9 table total. The Note 9 narrative says $14,088M.

## 8. Open items

- The Laguna "'29 and '30, largely" passage: re-open the GEV-hosted Laguna transcript PDF (pp.9–11) or the full MarketScreener/S&P CapIQ copy. The earningscalls.dev page I could access truncated before that passage.
- Chunk 246346: find the original dated source (the Dec-2025 investor update transcript) and its speaker.
- FY24 AIP target ($2,000M) and FY24 adjusted EBITDA exact: DEF 14A -25-000049 AIP table, and the Q4'24 release -25-000004.
- Wind FY24 guide miss and the 2028 Wind target cut from 10% to 6% (D01A claim): check the Dec-2024 and Dec-2025 investor-update releases.
- Buyback authorization remaining ($3,037M): 10-Q Part II Item 2 table.
- Oglethorpe $/kW pair and the Q3 consensus EBITDA ($1,706M MS / $1,728M ChartMill): not re-opened in this audit.
- Printed page numbers for every 10-Q and 10-K locator: confirm against the PDF.
