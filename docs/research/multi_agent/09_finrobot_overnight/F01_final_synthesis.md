# FINAL synthesis — everything from both phases

_F01_final_synthesis — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 04:14:19. Requests 27, input tokens 2269385, output tokens 24729._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV final research synthesis (as of 2026-09-30)

This is research input only. Every range is a research estimate: the team picks its own numbers and writes every memo sentence.

**How I built this.** I read D10 and E01, E02, E04, E05, E06, E07, E08, V11, V12 and V13 (key sections), plus E03, D06 and INDEX. I also checked some primary sources myself this session:
- the Q2'26 10-Q segment note (p.23), income statement (p.6) and balance sheet (p.7);
- the Q1'26 release guide-raise text;
- the Dec-2025 Q&A chunk 246346;
- the stockanalysis Laguna transcript (the first ~45k characters);
- a live yfinance quote.

**Source key**
- **10Q** = 0001996810-26-000148
- **10K** = 0001996810-26-000015
- **Q2REL** = 0001996810-26-000147 EX-99
- **Q1REL** = 0001996810-26-000063 EX-99
- **Q4REL** = 0001996810-26-000012 EX-99
- **LAG-PDF** = GEV-hosted Laguna transcript, 2026-09-16
- **LAG-SA** = stockanalysis.com copy of the same transcript
- **MS** = MarketScreener, 2026-09-29
- **GF** = GuruFocus/Yahoo GLJ wire, 2026-09-15

---

## 1. Bottom line

- **FY27 adjusted EBITDA research base is $8.6–8.9B vs consensus $9,574M (−7% to −10%). This held in every build and framing tonight.** The line that decides it is FY27 Power segment margin: consensus implies about 21.7–23.5%, against 20.0–20.5% in the builds.
  - Consensus: [S1: MS] [S2: GF "Street $9.45B"]
  - Builds: [S1: D01A §4] [S2: D01B §4-J]
  - Power history: [S1: 10Q p.23] [S2: Q2REL segment table]
- **The Power equipment vs services split is confirmed as to direction and size of change, not as to level.**
  - Services EBITDA margin is about 22–30% (both passes overlap).
  - Implied equipment EBITDA margin rose about +30 points from FY23 to H1'26 in every scenario.
  - The H1'26 level is uncertain: E01 central 0%, D06 central +3.6%, joint band −9% to +11%.
  - I re-derived E01's central case by hand this session and it ties exactly: services 27.9%, equipment 0.0%, Power 17.63%.
  - [S1: 10Q p.6 and p.23] [S2: 10K p.39/p.72; Q2REL]
- **Consensus needs above-trend equipment margin progress; the builds need on-trend progress.**
  - Consensus Power 21.7–23.5% needs FY27 equipment margin of about 12–18% (s = 28%). That is +12 to +18 points in ~1.25 years.
  - The trend pace is +6 to +10 points a year, which gives +7.5 to +12.5 points over the same period.
  - The builds' 20–20.5% needs only about 8–9% [computed §4-A3; pace from E01 Q5].
- **Horizon decides direction.** E02 central expected returns: short into January +4.3% (−0.6% to +12.1% across multiple frames); long 12 months +1.8%; short 12 months −1.8%; long into January −4.3%.
  - V11 (3–4 months) gives p_long 0.42. V12 (12 months) gives 0.52. V13 (neutral) gives 0.45.
  - No 12-month edge survives ±1 turn of multiple (~$43/share) [S1: E02 §Q3] [S2: E06 §1, +1% to +4%].
- **The biggest threat to the January short is the gap between being right and getting paid, not the estimate.**
  - P(guide midpoint < 18.15%) ≈ 82%, yet P(short in the red at exit) ≈ 45–50%. Daily σ is 3.34%, so ~81 sessions carry ~30% noise [S1: E05 §1] [S2: D04A/D04B via D10 Q3].
  - E04 adds that GEV guides carry a cushion. A guide midpoint of 16.5–17.8% is consistent with consensus still being met [S1: DEF 14A -26-000049 p.50] [S2: Q4REL actuals].
- **The brief needs four corrections:**
  1. Parks, not McDonough, presents the January call [S1: CFO-PR 2026-08-27] [S2: 8-K -26-000153 Item 5.02].
  2. The FY26 first margin guide (11–13%) was raised to 12–14% [S1: Q1REL, corpus chunk 13603] [S2: Q2REL "remains 12%-14%"].
  3. "Never cut" applies only to company revenue and FCF; Wind was cut at Q3'25 [S1: 8-K -25-000159] [S2: DEC25].
  4. The "'29 and '30" line is still single-source, but a Dec-2025 Q&A statement points the same way ("orders we're taking today. We're shipping in '29 or '30") [S1: LAG-PDF p.10] [S2: corpus chunk 246346, speaker unverified].

---

## 2. Answers

### Q1. The one number: FY27/FY28 adjusted EBITDA

**Research range (the team chooses its own number)**

| $M | Low | Base | High | Consensus (MS) | Consensus vs base |
|---|---|---|---|---|---|
| FY27 | 7,700 (D01A stat.); 7,330 (D01B corner); 8,000 (V11: GLJ + max vintage fix) | **8,600–8,900** (D01A 8,744; D01B 8,600; variant median 8,800; V11 ~8,900) | 9,580 (D01A stat.); 9,700 (V11, 18.5% guide); 9,970 (D01B corner) | 9,574 (18.15% on 52,740) | +8% to +11% |
| FY28 | 9,200–9,700 | **11,000–11,200** (≈ framework $11.2B); V11 12,000; variant range 10.8–12.0B | 12,600 (A) / 13,000 (B) | 13,064 (21.6%) | +17–19% vs 11.0–11.2B |

**Where D01A and D01B differ** (FY27, B − A = −$144M):

| Driver | Difference |
|---|---|
| Power (21 vs 20 GW; 20.5% vs 20.0%) | −118 |
| Wind (0 vs −100) | −100 |
| Electrification | +49 |
| Corporate | +25 |

Source: D01A §4, D01B §4-J, reconciled in D10 Q2.

**E01 cross-check.** FY27 equipment margin needed at each Power margin, with services s = 28% and services share w = 0.60 / 0.55:

| FY27 Power margin | Equipment margin needed |
|---|---|
| 18.5% | 4–7% |
| 20.7% | 10–12% |
| 22% | 13–15% |

Trend from E01's H1'26 level gives FY27 equipment at +7.5% to +12.5%; from D06's level, +11% to +16%. **Result: the builds' base sits on trend, and consensus Power at 21.7–23.5% sits above trend.**

**Driver that matters most.** FY27 Power segment margin is worth ~$275M per point (D01A) and needs ~2 points of equipment margin per point of Power margin. Second is Wind (the swing from −$400M to ~0 is worth ~0.76 points of company margin, E05 Q1). Third is revenue: $54.5B (Lark, single-source) vs $52.74B.

**Dollar translation of margin guides** (on $52,740M consensus revenue):

| Guide midpoint | EBITDA | vs consensus |
|---|---|---|
| 17.0% | $8,966M | −6.4% |
| 17.5% | $9,230M | −3.6% |
| 18.0% | $9,493M | −0.8% |

On $54.5B of revenue, 17.5% gives −0.4% [E05 A2].

### Q2. Power equipment vs services split: E01 vs D06

**Verdict: confirmed on direction and change; not confirmed on level.** GEV does not disclose it, and every level depends on three undisclosed parameters:
- D&A inside cost of services (d);
- Wind and Electrification services gross margins;
- how Power overhead is allocated between equipment and services.

| Implied Power equipment EBITDA margin | FY23 | FY24 | FY25 | H1'26 |
|---|---|---|---|---|
| D06 central | −27% | −13.5% | −4.8% | +3.6% |
| E01 central | −31% | −18% | −8.5% | 0.0% |
| Joint band (E01 §1) | −41 to −19 | −29 to −5 | −18 to +3.5 | −9 to +11 |
| Power services EBITDA margin (E01 central) | 29.7% | 26.7% | 26.6% | 27.9% |

- **Why they differ:** about 2.7 of the 3–5 points comes from overhead share (D06 66% by revenue; E01 58%, citing the 10-K R&D description p.7). The rest comes from d and the non-Power services margins.
- **What survives every scenario:**
  - The change from FY23 to H1'26 is +29.9 to +32.3 points [E01 Q3].
  - Company services gross margin *fell* from 35.1% to 31.6% while Power's gross margin before D&A rose from 23.0% to 28.2%. The improvement came from equipment [S1: 10K p.39] [S2: 10Q p.6].
- **Management statements match on a contribution-margin basis only:**
  - YE2022 backlog margin "approximately breakeven" [S1: Q4'25 call chunk 246150] [S2: GEV webcast transcript 01-28-2026].
  - "Stabilizing Gas new unit contribution margins LSD-MSD" [S1: GE 2019 outlook deck] [S2: 2020 UBS transcript via D06].
- **Definition trap (E03):** Power equipment/services revenue differs between the segment note (H1'26 3,834 / 6,593 / 22 intersegment) and the MD&A (3,851 / 6,598). Use the segment-note figures for the split, because the cost lines sit there.

**How the team re-derives it by hand** (H1'26; each step verified this session):
1. Company services gross profit (after D&A) = 8,729 − 5,974 = **2,755** [10Q p.6; Q2REL income statement].
2. Add back services D&A. d = 1.75% × 8,729 = **153** (assumption, team's choice of 1.0–2.5%).
3. Take off non-Power services gross profit. Wind: 10% × 1,174 = 117. Electrification: 32.5% × 948 = 308 (assumptions). Revenues are from 10Q p.23.
4. Power services gross profit before D&A = 2,755 + 153 − 117 − 308 = **2,483** (37.7% of 6,593).
5. Power overhead = SG&A 918 + R&D 286 + other (100) = **1,104** [10Q p.23]. Services share 58% = 640.
6. Power services EBITDA = 2,483 − 640 = **1,843 (27.95%)**.
7. Equipment EBITDA = 1,842 − 1,843 = **−1**, on equipment plus intersegment revenue of 3,856 = **0.0%**.
8. Check: (1,843 − 1) / 10,449 = 17.63%, which equals the reported Power margin.

FY25, same method: services 26.55%, equipment −8.5%. That matches E01.

### Q3. Horizon decision table (E02, checked against V11, V12, V13)

| Pitch | Central E[return] | Frame range | P(win) (research) | Worst plausible | Checked by | Ease of defence (E02 ranking) |
|---|---|---|---|---|---|---|
| (a) Short into late-Jan-27 guide | **+4.3%** | −0.6% (sticky multiple) to +12.1% (harsh) | ~50–55% (E05: 45–50% in the red) | −22.7% ($1,181, J1 at 30x) | V11 p_long 0.42; V13 0.45 | 1st: one number, dated event and kill rule all align |
| (b) Long 12 months (Sep-27) | +1.8% (E06 +1% to +4% incl. net-cash build) | ±4.5% per turn of multiple | ~55% | −32.9% ($646, 16x) | V12 p_long 0.52 | 2nd: pure multiple/roll bet on FY28 consensus, which is 16.6% above plan |
| (c) Short 12 months | −1.8% | same | ~45% | −39% ($1,338) | V12 | 3rd |
| (d) Long into January | −4.3% | −5.1% to +0.6% | ~45% | −28.6% ($687) | — | 4th: bets against P ≈ 82% of a guide below consensus |

- **Flat-price multiples:**
  - Jan-27: 25.1x on NTM $9,865M = 11/12 × 9,574 + 1/12 × 13,064.
  - Sep-27: 20.3x on NTM $12,191M. Today: 28.2x (MS) / 27.7x (Chartloom) [computed §4-A1].
- **Q3 print (10-28) sits between the finals and the January guide.** A clean beat takes (a) to about +0.8% [E02 Q4].
- **Not researched:** a peer-hedged short (E05 Q12 item 8). The GLJ-day excess move vs peers was only about −3%, so beta dominates the noise. This is an open item.

### Q4. Strongest red-team attack on each candidate

| Candidate | Strongest attack | Evidence | Does it break the thesis? |
|---|---|---|---|
| (a) Short into Jan | **"Right, but too small":** a 17–19% range (P ≈ 52%) is only −0.8% to +2.5% vs consensus. January bundles positives (backlog-margin change "larger" than +11 pts, a likely new buyback, ≥125 GW, $200B backlog). All four guide/framework days closed up (+2.67% to +15.62%) | [S1: E05 §1, BX-13] [S2: LAG p.5; Barron's 2025-12-12] | **No, but it cuts the edge to about coin-flip after noise.** Counter-evidence: Q2'26 held margin and fell −8.69% [BX-13; Reuters 07-22]. Also, no FY guide has ever been given first on a January call |
| (a), second attack | First guides are sandbagged. FY26 went 11–13% → 12–14% by Q1; the E04 bonus cushion (+1.75% to +10.2%) | [S1: Q1REL] [S2: DEF 14A -26-000049 p.50] | Weakens the "sub-18% guide = consensus too high" inference. The short needs a *dollar* guide clearly below ~$8.7B, or the market has to read it as a cut |
| (b) Long 12 months | **Multiple:** at the US-peer median ~21x, Sep-27 value is $995 (+3%); on the plan path $885 (−8%). The +39% roll rests on FY28 consensus that is 16.6% above plan. The GE 2000–02 analogue: P/E halved while EPS rose | [S1: E06 §Q1, MS peer multiples (mostly single-source)] [S2: GE 2003 10-K ex13; NY Post 2002-04-16] | **No, it turns the long into poor reward/risk.** E06 says the thesis is "not destroyed": P(>+10%) ~22%, P(<−10%) ~25% |
| (b), second attack | Deposits: H1 OCF excluding contract liabilities −$3.0B while ~$3.67B was bought back (treasury $3,385M → $7,057M). FY27 FCF −38% [SINGLE: MS] | [S1: 10Q p.7, verified] [S2: 10Q cash-flow statement] | A quality flag, not a FY27 EBITDA driver |

### Q5. Catalyst calendar (E07) and kill rule

| Date | Event | Status | Short passes if | Long passes if |
|---|---|---|---|---|
| 10-23 | Finals | fixed | — | — |
| 10-28, 7:30 ET | Q3'26 + 10-Q; same day FOMC 2:00pm; GOOGL/META/MSFT est. | GEV date confirmed [S1: GEV events page] [S2: earningscountdown] | EBITDA < $1,706M (MS) / $1,728M (ChartMill); FY26 margin guide held; Power < 17% | Beat plus margin-guide raise (+13.75% precedent) |
| 11-11 | Siemens Energy FY26 + mid-term (FY28 14–16%) | [S1: SE IR calendar] [S2: SE Q3 call] | No peer margin raise | Peer raise, pricing confirmed |
| Dec 8–9 / Dec PJM auction / 12-10 ERCOT | FOMC; PJM 2029/30; ERCOT audit | E07 rows 20, 24, 27 | Hike / weak load evidence | — |
| Dec | No GEV investor event listed (vs Dec-24, Dec-25) | M-confidence; the tell would come on 10-28 | Absence | Surprise event (P ≈ 10%, E05 Q7) |
| YE26 | Gas ≥125 GW (116 at Q2) | [S1: Q2REL p.1] [S2: Q2 transcript] | < 125 GW | ≥ 125 GW |
| Late Jan-27 (est. 01-20 or 01-27; unannounced) | Q4 + FY27 outlook + 2026 backlog-margin change, presented by Parks | [S1: LAG-PDF p.10–11] [S2: MarketBeat 09-18] | Midpoint ≤ 17.0% **and** dollars ≤ ~$9.0B, 2028 held at 20% | Low end ≥ 18%, or dollars ≥ consensus |
| Spring-27 (may fall after 03-31) | CMD, 2030 outlook | date TBD | 2028 held ~$11.2B | 2028 raised ≥ ~$12.5B |

**Kill rule (research proposal; the team sets its own)**
- **Short:** FY27 guide low end ≥ 18%; or EBITDA guide midpoint ≥ ~$9.4B (−2% vs consensus); or 2028 raised to ≥ $12.5B.
  - The price stop is $1,079: consensus rolled at a constant 28.2x [E02 Q4].
  - I added a dollar leg because of E04/E05: a revenue-led guide can land below 18% on margin and still be close to consensus in dollars.
- **Long:** midpoint ≤ 17% with no 2028 raise, or NTM EV/EBITDA ≤ 20x.

### Q6. What incentives (E04) and pricing evidence (E08) add

**E04, incentives**
- Bonus EBITDA targets were set at about the guide midpoint (FY24 $2,000M; FY25 $2,900M). FCF targets were set at the top of the guide.
- Actual EBITDA beat the target by +1.75% and +10.2%; FCF by +70% and +48% [S1: DEF 14A -25-000049 p.54; -26-000049 p.50] [S2: 4Q24 / 4Q25 releases].
- The "beats are cash, not margin" pattern is now in the pay record.
- No 2026 targets are disclosed. The 2024–26 PSU targets appear only in the spring-2027 proxy.
- **What it adds:** the pay record supports conservative guiding. That weakens any inference from "guide < consensus" to "consensus too high".

**E08, pricing**
- There is no turbine-only price by vintage. The GE-linked all-in plant cost steps are:
  - 2024 → 2025: +53% to +66% (LG&E/KU $1,398 → $2,144/kW; JEA $2,326) [S1: KY PSC 2025-00045 Tummonds p.4–5] [S2: GridLab T2].
  - A new same-owner pair (Oglethorpe 7HA.03): $2,316 → $3,226–3,787/kW, +39% to +64% nominal, about +19% to +45% after escalation (the 2033 figure is single-source) [S1: 0000788816-25-000023 slide 4] [S2: 0000788816-26-000050 slides 5/8].
- CEO-endorsed GE slice: ~$750/kW (30% × $2,500) [S1: Q3'25 transcript src:3796] [S2: Motley Fool].
- **What it adds:** support for a big vintage price step, which is long-leaning beyond 2027. It gives no FY27 timing information. There is no escalation clause evidence, and older fixed-price backlog cannot be repriced [10K Item 1A; E06 Q6].

### Q7. One-page decision summary (research input; the team decides)

| Item | Research input |
|---|---|
| Direction options | (a) Short into Jan: P(correct call on guide) ~82%, P(profitable at exit) ~50–55%, E +4.3%. (b) Long 12m: P(up) ~55%, E +1.8%. (c) Short 12m: E −1.8%. (d) Long into Jan: E −4.3%. Untested: peer-hedged short |
| Probabilities by horizon | Through Jan: short ~55 / long ~45. 12 months: ~50 / 50 [D10 Q6; V10; V11–V13] |
| Target formula | Price = (m × NTM EBITDA + $9,113M) / 266.33M. NTM Jan = 11/12 FY27 + 1/12 FY28; Sep-27 = 0.25 FY27 + 0.75 FY28 |
| Research target grid | Jan short, given a miss: $785–913 (probability-weighted $851, −11.6%). Sep-27 on the research path ($10.5B): $902 at 22x, $1,020 at 25x. Consensus path ($12,191M): $950 / $1,041 / $1,179 at 20 / 22 / 25x |
| One number | FY27 adjusted EBITDA $8.6–8.9B (team's choice) vs $9,574M; driver is FY27 Power margin 20–20.5% vs ~21.7–23.5% implied |
| Kill | See Q5 (18% low end / ~$9.4B / 2028 ≥ $12.5B; price $1,079) |
| Catalysts | 10-28 Q3 (after the finals); 11-11 SE; YE 125 GW; late-Jan FY27 outlook; spring CMD |

### Q8. The 20 numbers to hand-verify

| # | Number | Value | S1 (locator) | S2 (locator) |
|---|---|---|---|---|
| 1 | Close 2026-09-29 | $962.49 | yfinance quote 2026-09-30 08:10 UTC (re-pulled this session) | Zacks/Yahoo close 9/29 (D08 #1) |
| 2 | Shares outstanding | 266,333,581 | 10Q p.7 equity section (read this session) | MS 266,334K |
| 3 | Cash incl. restricted / borrowings / NCI | 13,120 / 2,849 (LT 2,794) / 1,158 | 10Q p.7 (read this session) | Q2REL "$13.1B cash" (NCI filing-only) |
| 4 | EV | $247.2B [computed] | from rows 1–3 | stockanalysis $247.34B |
| 5 | FY25 revenue / adj EBITDA | 38,068 / 3,196 | 10K p.26 & p.72 | Q4REL p.2; MS actual |
| 6 | H1'26 revenue / adj EBITDA | 20,442 / 2,146 | 10Q p.6 / p.24 | Q2REL p.2 |
| 7 | FY26 guide | $45.5–46.5B; 12–14%; FCF $11.5–12.5B | Q2REL guide box | Q2 transcript / Kalkine 9/29 |
| 8 | FY26 first margin guide raised | 11–13% → 12–14% | Q1REL (corpus chunk 13603) | Q2REL "remains 12%-14%" |
| 9 | 2028 framework | $56B; 20%; Power / Electrification / Wind 22 / 22 / 6 | Q4REL | DEC25 release |
| 10 | Consensus FY27 EBITDA / revenue | 9,574 / 52,740 | MS 09-29 | GF $9.45B; S&P $52.74B; FactSet $52,632M |
| 11 | Consensus FY28 EBITDA | 13,064 | MS | Motley Fool 60% CAGR ≈ $13.09B |
| 12 | Consensus FY27 EPS | $24.85 | MS | FactSet $24.78; Erste $24.55 (MarketBeat 09-21) |
| 13 | Power H1'26 segment note lines | Eq 3,834; Svc 6,593; ISR 22; Cost 7,504; SG&A 918; R&D 286; Other (100); EBITDA 1,842 | 10Q p.23 (read this session) | Q2REL Power table |
| 14 | Company H1'26 services / equipment sales and cost | 8,729 / 5,974; 11,713 / 10,328 | 10Q p.6 (read this session) | Q2REL income statement |
| 15 | Power FY25 lines | 19,767 revenue; 2,902 EBITDA; cost 14,627 | 10K p.72 | Q4REL Power table |
| 16 | Equipment RPO → 2027 | $64,245M × 32% = $20,558M (±$0.64B) | 10K Note 9 | Q4'25 call "$64B" |
| 17 | Gas backlog + SRAs | 53 + 63 = 116 GW; ≥125 GW YE26 | Q2REL p.1 (read this session) | Q2 transcript |
| 18 | Output ladder | 5 GW/qtr Q3–Q4'26 → 6 GW/qtr "second half of next year" | LAG-PDF p.4 | LAG-SA (read this session) |
| 19 | CSA profit revisions | FY24 −319; FY25 −151; H1'26 −218 | 10Q Note 9 | 10K Note 9 |
| 20 | Contract liabilities / treasury stock | 39,944 (vs 25,774); treasury 7,057 (vs 3,385) | 10Q p.7 (read this session) | Q2REL balance sheet / 10Q Note 9 |

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | FY27 consensus EBITDA | $9,574M | MS 09-29 | GF "Street $9.45B" | close (−1.3%) | M |
| 2 | FY27 research base | $8.6–8.9B | D01A §4 | D01B §4-J; V10 median $8.8B | close | M |
| 3 | Power H1'26 note lines | row 13 above | 10Q p.23 | Q2REL | exact | H |
| 4 | Services gross margin H1'26 | 31.6% | 10Q p.6 (computed) | E01 via 10K/Q2REL | exact | H |
| 5 | Equipment margin change FY23 → H1'26 | +30 to +32 pts (E01); +25 to +30 (D06) | E01 Q3 | D06 §1 | close | M |
| 6 | Equipment level H1'26 | 0% (E01) vs +3.6% (D06) | E01 | D06 | conflict (assumption-driven) | L |
| 7 | Parks presents the Jan call | through Q3 and Q4 calls | CFO-PR 08-27 | 8-K -26-000153 | exact | H |
| 8 | "'29 and '30" timing | quote | LAG-PDF p.10 | Dec-25 Q&A chunk 246346 (related, different event) | directional only | L–M |
| 9 | Guide/framework-day returns | +5.01 / +2.67 / +15.62 / +2.73% | BX-13 | Barron's 2025-12-12 | exact | H |
| 10 | Q2'26 margin-held day | −8.69% | BX-13 | Reuters 07-22 | exact | H |
| 11 | Bonus cushion | EBITDA +1.75% / +10.2% vs target | DEF 14A -25-000049 p.54; -26-000049 p.50 | Q4 releases | exact | H |
| 12 | Oglethorpe GE 7HA.03 pair | $2,316 → $3,226–3,787/kW | OPC SEC briefing slide 4 | OPC SEC briefing slides 5/8 | same publisher | M |
| 13 | Consensus price target | $1,237.34 (MS) vs $1,145.83 (MarketBeat) | MS | ad-hoc-news citing MarketBeat 09-21 | **conflict** (analyst sets differ) | M |
| 14 | Rating split | 30 Buy (6 Strong Buy + 24 Buy) / 7 Hold / 0 Sell | MS | 24/7 Wall St. 09-16 | exact | H |
| 15 | SRA share | 54.3% GEV vs 27.4% SE | SE Q3 FY26 pres. p.6 | Q2REL GW | exact | H |

---

## 4. Arithmetic

- **A1, flat-price multiples.**
  - EV = 962.49 × 266.33 − 9,113 = 247,227.
  - Jan NTM = 0.9167 × 9,574 + 0.0833 × 13,064 = 9,865 → 25.06x.
  - Sep-27 NTM = 0.25 × 9,574 + 0.75 × 13,064 = 12,191 → 20.28x.
- **A2, E02 January expected price.** 0.14 × 1,105 + 0.20 × 1,025 + 0.34 × 913 + 0.32 × 785 = $921.3. Short return = (962.49 − 921.3) / 962.49 = +4.3%.
- **A2b, E02 Sep-27 expected price.** 0.25 × 1,198 + 0.30 × 1,019 + 0.30 × 888 + 0.15 × 722 = $980 → +1.8%.
- **A2c, check of one scenario (J3).** (25 × 9,365 + 9,113) / 266.33 = $913.3.
- **A3, required equipment margin.** e = (P − w·s) / (1 − w), with s = 28%:
  - Consensus P 21.7–23.5%: w = 0.60 gives 12.3–16.8%; w = 0.55 gives 14.0–18.0%.
  - Builds P 20.0–20.5%: w = 0.60 gives 8.0–9.3%.
  - Trend: an H1'26 base of 0–3.6% plus 1.25 years × 6–10 points a year gives 7.5–16%.
- **A4, split re-derivation.** Q2 steps 1–8 above. FY25 version:
  - Services gross profit = 17,134 − 11,774 = 5,360.
  - Power services gross profit = 5,360 + 300 − 186 − 705 = 4,769.
  - Overhead = 1,836 + 549 − 147 = 2,238; 58% = 1,298.
  - Services EBITDA = 3,471 (26.55%). Equipment = 2,902 − 3,471 = −569 on 6,696 = −8.5%.
- **A5, E04 cushion.** 9,574 / 1.102 = 8,688 (16.47% on 52,740); 9,574 / 1.0175 = 9,409 (17.84%).
- **A6, contract-liability balance change.** 39,944 − 25,774 = 14,170 (balance sheet, includes Prolec). This compares with 14,087 in Note 9 and 13,695 in the cash-flow line: three different numbers for three different definitions.
- **A7, margin-to-dollar translation.** 17.0% / 17.5% / 18.0% × 52,740 = 8,966 / 9,230 / 9,493.

---

## 5. General question bank items answered

- **G1.** At a flat price the stock needs 25.1x in January and 20.3x in Sep-27. Physically: 5 → 6 GW a quarter, 24 GW in 2028, Power at 22% by 2028 [A1; LAG-SA].
- **G2.** Consensus FY27 needs +5.15 points of company margin; the largest step so far is +4.6 points (V11 R1). It also needs above-trend equipment margin (A3).
- **G7.** The gap is interpretation and timing, not information. The backlog-margin slide is published every January (V10).
- **G12.** Fixed-price equipment with no escalation found, and deposits at 3.0x cash. Old backlog cannot be repriced [E06 Q6/Q7].
- **G15.** Five drawdowns of 15% or more since the spin, median −24.6%; the GLJ-day drop was 106% recovered in 11 sessions [BX; Nasdaq].
- **G16.** Rates: a Fed hike on 09-16 and 49–64% odds of an October hike [E07 rows 22–23].
- **G17.** Buybacks: $3,037M left, and a new authorisation plausibly comes in January (inference). The guiding cushion is visible in the pay record (E04).
- **G19.** GE 2000–02: the multiple de-rated 1.5–2 years before earnings fell, and earnings broke only after orders turned. No order turn is visible yet; H2'26 signings are set to roughly halve [E06 Q2/Q4].
- **G24.** H1 OCF excluding deposits was −$3.0B while ~$3.67B was bought back [10Q p.7].
- **New from LAG-SA (read this session):** "every gigawatt of HAs will generate $500,000,000 of high-margin services revenue over the first 20 years" [SINGLE-SOURCE until checked against LAG-PDF].

---

## 6. What would change these findings

- **FY27 gap:** a paid segment consensus showing Power ≤ 21%. That would mean the gap is Wind or Corporate, not Power.
- **Split:** any GEV disclosure of services D&A or Power equipment margin. Also a Siemens Energy new-unit margin disclosure on 11-11.
- **Short (a):**
  - Q3 margin-guide raise on 10-28.
  - A December event.
  - A guide with low end ≥ 18%, or dollars ≥ ~$9.4B.
  - Option-implied vol well below 53% would strengthen the short, because it lowers the noise problem.
- **Long (b):** 2028 held at $11.2B at the CMD with FY28 consensus converging down, or NTM ≤ 20x. H2'26 commitments well under 19 GW.

---

## 7. Disagreements with the master brief

1. "First call under the new CFO" is wrong; Parks presents [CFO-PR; 8-K -26-000153].
2. "Never beaten its first margin guide" is out of date. FY24 and FY25 first guides were qualitative and were met; FY26's first numeric guide was raised [Q1REL; Q2REL].
3. "Never cut" should be restricted to company revenue and FCF (Wind was cut).
4. The lean should be ~55% short only through January, not 55–60%, and ~50/50 at 12 months.
5. Cash of $13,120M includes restricted cash (10Q p.7 label).
6. The consensus target is vendor-dependent: $1,237.34 (MS) vs $1,145.83 (MarketBeat).
7. Prolec runs at 22.0%, not 25% (D10 Q7).
8. The kill rule at an 18% margin should get a dollar leg (E04/E05).

---

## 8. Open items

- A second full-row vendor for FY27/FY28 EBITDA (FactSet, Bloomberg or Visible Alpha). None was found free; the Exa search this session found only EPS (Erste $24.55).
- The "'29 and '30" line in full context: LAG-PDF pp.9–11. My LAG-SA read stopped at ~45k characters.
- Peer-hedged short arithmetic (GEV vs VRT/ETN/SE basket): not computed.
- Hyperscaler Q3 capex dates: estimated only.
- The Q4'26 call date and the CMD date: watch the GEV events page.
- Power D&A split and services D&A: not disclosed. Ask IR, or check the FY26 10-K.
- The 52-week low conflict ($529.18 vs $530.16): check intraday vs closing basis on Nasdaq historical.
