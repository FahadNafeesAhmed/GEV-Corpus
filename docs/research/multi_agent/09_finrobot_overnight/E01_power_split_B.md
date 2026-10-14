# Independent re-derivation of Power equipment vs services margin (verify D06)

_E01_power_split_B — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 03:12:06. Requests 37, input tokens 2601076, output tokens 39632._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV Power segment: equipment vs services margins, rebuilt from the segment note (FY23–Q2'26)

*Research input only. Every grid row is a research estimate, and the team picks its own number.*

## 1. Bottom line

- **The segment note does not split Power's costs between equipment and services.** For Power it gives equipment revenue, services revenue, intersegment revenue, one combined cost-of-revenues line (excluding D&A), SG&A, R&D and "other segment items". Any equipment or services margin is therefore an inference. It rests on three numbers GEV does not disclose:
  1. D&A inside cost of services (d);
  2. Wind and Electrification services gross margins;
  3. how Power's overhead (SG&A, R&D, other) is shared between equipment and services.
  [S1: FY25 10-K 0001996810-26-000015, "SEGMENT EBITDA" tables p.72–73] [S2: Q2'26 10-Q 0001996810-26-000148 p.23; FY24 10-K 0001996810-25-000011, same table]
- **Power services EBITDA margin comes out at about 19–35% across periods; my central case is 24–30%.** D06 said ~18–32%, central 22–27%. The ranges overlap almost entirely, so the services range is **confirmed**. Arithmetic in §4.
- **Implied Power equipment EBITDA margin, my central case:**

  | FY23 | FY24 | FY25 | H1'25 (recast) | H1'26 | Q2'26 |
  |---|---|---|---|---|---|
  | −31% | −18% | −8.5% | −7% | 0% | 0% |

  D06 had −27 / −13.5 / −4.8 / −2.5 / +3.6 / +4. My central is 3–5 points lower in every period. About 2.7 of those points come from one choice: D06 splits overhead by revenue share (services carry ~66%). I give services 58%, because the 10-K says only about half of R&D supports existing products and the installed base [S1: FY25 10-K p.7 "Research and Development"] [S2: FY25 10-K Note 24 R&D line 549 vs SG&A 1,836]. The rest comes from d and the non-Power services margins.
- **The finding that survives every assumption is the change, not the level.** Implied equipment margin rose about 30–32 points from FY23 to H1'26 in all my scenarios (low, central and high). It also rose about 6–8 points year on year from H1'25 to H1'26 on the same recast basis. Over the same time, company-wide services gross margin *fell*, from 35.1% (FY23) to 31.3% (FY25) and 31.6% (H1'26), while Power's gross margin before D&A rose from 23.0% to 28.2%. Power's improvement came from equipment. [S1: FY25 10-K income statement p.39] [S2: Q2'26 10-Q p.6; XBRL GrossProfit FY25 $7,535M, edgar_tools]
- **The management statements match the derivation, but on a different basis.** The YE2022 "approximately breakeven" figure and the 2019–20 "low-to-mid single digit" figure are both contribution margins, not EBITDA. GE's 2019 outlook deck says "Stabilizing Gas new unit contribution margins LSD-MSD". Contribution near zero is consistent with equipment EBITDA of about −20% to −30% in FY23, once fixed factory cost and overhead are taken off. [S1: GE 2019 Investor Outlook deck, ge.com/…/ge_webcast_presentation_03142019.pdf] [S2: GEV Q4'25 call, Strazik, corpus chunk 246150]
- **What FY27 needs.** The Street's FY27 Power margin of 20.7% (as GLJ reports it) needs equipment EBITDA of about 10–15% in FY27. My central H1'26 level is ~0% (D06: ~+4%). That means keeping the recent pace of roughly +6–10 points a year with no slowdown. GLJ's own 18.5% needs only about 4–7%, which is about +3–5 points a year. [S1: Yahoo Finance GLJ summary, 2026-09-15 (facts GLJ-04)] [S2: master brief §4 / FY26 guide Power 17–19%, Q2'26 deck]

**Verdict on D06: CONFIRMED WITH A DIFFERENT RANGE.**
- The services band is confirmed.
- The direction and size of the equipment turnaround (+~30 points) are confirmed.
- The equipment *levels* are about 3–5 points lower in my central case. The combined band I would give the team is:

| | FY23 | FY24 | FY25 | H1'26 |
|---|---|---|---|---|
| Implied equipment EBITDA margin | −41% to −19% | −29% to −5% | −18% to +3.5% | −9% to +11% |

---

## 2. Answers

### Q1. What the segment note discloses for Power (US$M)

| Line | FY23 | FY24 | FY25 | H1'25 as first filed | H1'25 recast | H1'26 | Q2'26 |
|---|---|---|---|---|---|---|---|
| Equipment revenues | 5,535 | 5,509 | 6,420 | 2,881 | 2,881 | 3,834 | 1,957 |
| Services revenues | 11,758 | 12,391 | 13,072 | 6,178 | 6,232 | 6,593 | 3,509 |
| Intersegment revenues | 143 | 227 | 276 | 121 | 121 | 22 | 12 |
| Segment revenues | 17,436 | 18,127 | 19,767 | 9,180 | 9,234 | 10,449 | 5,477 |
| Cost of revenues (excl. D&A) | 13,425 | 13,608 | 14,627 | 6,819 | 6,818 | 7,504 | 3,866 |
| SG&A (excl. D&A) | 2,124 | 2,022 | 1,836 | 902 | 930 | 918 | 472 |
| R&D (excl. D&A) | 315 | 384 | 549 | 232 | 242 | 286 | 154 |
| Other segment items | (149) | (155) | (147) | (59) | (59) | (100) | (45) |
| **Segment EBITDA** | **1,722** | **2,268** | **2,902** | **1,286** | **1,303** | **1,842** | **1,031** |
| Margin | 9.88% | 12.51% | 14.68% | 14.01% | 14.11% | 17.63% | 18.82% |
| Power D&A (full year only) | 494 | 519 | 467 | – | – | – | – |

**Sources by column:**
- FY23 and FY24: [S1: FY24 10-K -25-000011, SEGMENT EBITDA table] [S2: FY25 10-K -26-000015 p.72–73, comparatives agree exactly].
- FY25: [S1: FY25 10-K p.72] [S2: Q4'25 release 8-K EX-99 -26-000012, Power table (cost 14,627 / SG&A 1,836 / R&D 549 / other (147) / EBITDA 2,902) — exact].
- H1'26 and Q2'26: [S1: Q2'26 10-Q p.23] [S2: Q2'26 release -26-000147 Power table (7,504 / 918 / 286 / (100) / 1,842; Q2 3,866 / 472 / 154 / (45) / 1,031); Q2'26 deck margins 18.8% and 17.6% (corpus chunk 251297) — exact].
- H1'25 as first filed: [Q2'25 10-Q -25-000133 p.23].
- D&A: [FY25 10-K p.73, "Depreciation and amortization" by segment] **[SINGLE-SOURCE for FY25]**. The FY24 and FY23 figures are comparatives in the same table.

**Conflict: H1'25 was recast.** The Q2'25 10-Q showed Power services at 6,178 and EBITDA at 1,286. The Q2'26 10-Q comparative shows 6,232 and 1,303. The reason is the realignment effective 1 January 2026: a component of Electrification Software moved into Gas Power, and Steam was folded into Nuclear, Hydro and Gas inside Power [S1: Q1'26 10-Q -26-000064 Note 1 (corpus chunk 13642)] [S2: Q2'26 10-Q MD&A "Business Unit Realignment" (chunk 5722)]. Use the recast figure when comparing H1'25 with H1'26. FY23–FY25 are on the old basis.

**Company-wide inputs:**

| | FY23 | FY24 | FY25 | H1'25 | H1'26 | Q2'26 |
|---|---|---|---|---|---|---|
| Services sales / cost | 14,981 / 9,716 | 15,983 / 10,861 | 17,134 / 11,774 | 8,052 / 5,647 | 8,729 / 5,974 | 4,645 / 3,130 |
| Equipment sales / cost | 18,258 / 18,705 | 18,952 / 17,989 | 20,934 / 18,759 | 9,091 / 8,181 | 11,713 / 10,328 | 6,459 / 5,613 |
| Wind services revenue | 1,488 | 1,642 | 1,858 | 885 | 1,174 | 631 |
| Electrification services revenue | 1,733 | 1,923 | 2,168 | 916 | 948 | 497 |

[S1: FY25 10-K p.39; Q2'26 10-Q p.6] [S2: FY24 10-K comparatives; Q2'26 release]. Services revenue by segment is from the segment note in the same filings.

### Q2. What bounds Power's services margin

The identity is:

> Power services gross profit before D&A = company services gross profit (after D&A) + d − Wind services gross profit − Electrification services gross profit.

Then:

> Power services EBITDA = Power services gross profit − the services share of Power overhead (SG&A + R&D + other).

**Parameter ranges I used:**
- d = 1.0% / 1.75% / 2.5% of company services revenue. FY25 that is $171M / $300M / $428M, against total D&A of $853M.
- Wind services gross margin 20% / 10% / 0%.
- Electrification services gross margin 40% / 32.5% / 25%.
- Services share of overhead 66% / 58% / 50%.

**FY25 bounds:**
- **Hard ceiling (not realistic):** all D&A in cost of services and zero Wind/Electrification services profit gives (5,360 + 853) / 13,072 = 47.5% gross.
- **Realistic floor:** Wind services 30%, Electrification services 45%, d = 0 gives 29.3% gross. Less 66% of overhead (11.3% of revenue) leaves **~18% EBITDA**.
- **Realistic ceiling:** d = 500, Wind services 0%, Electrification services 20% gives 41.5% gross. Less 50% of overhead (8.6% of revenue) leaves **~33%**.

**Scenario results:**

| Period | Low / central / high services margin | Implied equipment margin |
|---|---|---|
| FY23 | 24.8 / 29.7 / 34.5 | −21.0 / −31.1 / −41.2 |
| FY24 | 21.8 / 26.7 / 31.6 | −7.5 / −18.1 / −28.7 |
| FY25 | 21.5 / 26.6 / 31.6 | +1.3 / −8.5 / −18.3 |
| H1'25 recast | 19.4 / 24.3 / 29.2 | +3.2 / −7.0 / −17.3 |
| H1'26 | 22.7 / 27.9 / 33.1 | +8.9 / 0.0 / −8.9 |
| Q2'26 | 24.3 / 29.5 / 34.7 | +9.0 / −0.2 / −9.4 |

A higher services margin means a lower equipment margin. Equipment margins are on equipment plus intersegment revenue.

**Sensitivities (FY25):**
- d ±$100M moves s by ∓0.8 points and e by ±1.5 points.
- Overhead share ±1 point moves e by ∓0.33 points.
- Wind services margin ±1 point moves e by ±0.28 points.
- One point of s is worth about 2.0 points of e in FY25 and 1.7 points in H1'26 (the services/equipment revenue ratio).

**Independent check:** Siemens Energy Gas Services implies services at ~17–25% on an EBITDA-like proxy (facts PMX-36/44 [S1: SE Annual Report 2025 Note 26] [S2: SE CMD Nov-2025 slide 14]). That is a definition mismatch, so treat it only as a range check. It sits at or below my low end.

### Q3. Implied equipment EBITDA margin

Low / central / high as in the Q2 table. The key rows:
- FY25: −18.3% to +1.3%, central −8.5%.
- H1'26: −8.9% to +8.9%, central 0.0%.
- Q1'26 (H1 less Q2): central +0.2%, so no sequential improvement from Q1 to Q2 in my central case.
- Change FY23 → H1'26: low-s scenario +29.9, central +31.1, high-s scenario +32.3 points.

### Q4. Do management statements agree?

**Yes on direction. The size cannot be tested, because the metrics are defined differently.**

- **YE2022 "approximately breakeven."** Strazik: "directionally, the starting point is approximately breakeven" (Q4'25 call, January 2026) [S1: corpus chunk 246150] [S2: facts PMX-26, gev_webcast_transcript_01282026.pdf]. GEV's backlog margin is a contribution-margin metric. D06 quotes a slide footnote, "average estimated contribution margin in backlog", which I could not find in the corpus (see §7). Contribution near zero minus fixed factory cost minus 13–20% overhead gives FY23 equipment EBITDA of about −15% to −35%. My FY23 band is −21% to −41%, central −31%. That is consistent, and it favours the lower-services-margin end.
- **2019–20 "LSD-MSD."**
  - GE's 2019 outlook deck: "Stabilizing Gas new unit contribution margins LSD-MSD" [S1: ge.com 2019 Investor Outlook deck].
  - Strazik at UBS, 2020-06-03, per D06's transcript: "from low single digits to mid-single digits" [S2: earningscalls.dev transcript as cited in D06]. The event date is confirmed by GE's IR note of 2020-06-10, which does not contain the phrase. **This is the same contribution basis, not EBITDA.**
- **Cumulative change in backlog margin:** +3 (FY23), +3 (FY24), +11 (FY25) points [facts PMX; D06 cites deck slide 5]. Taking FY25 shipments from backlog at roughly +3 to +6 points of contribution fits FY25 equipment EBITDA of about −5% to −12%.

### Q5. FY27 equipment margin: trend vs what consensus needs

**Required equipment margin:** e = (Power margin − w × s) / (1 − w), where w is the services share of Power revenue. H1'26 w was 63%. As equipment grows faster, a plausible FY27 w is 0.55–0.60 (research estimate).

| Power FY27 margin | s = 25%, w .60 / .55 | s = 28%, w .60 / .55 | s = 30%, w .60 / .55 |
|---|---|---|---|
| 18.5% (GLJ) | 7.8 / 9.1 | 4.3 / 6.9 | 1.8 / 4.4 |
| 19% (top of FY26 guide) | 10.0 / 11.7 | 5.5 / 8.0 | 2.5 / 5.2 |
| 20.7% (Street, per GLJ) | 14.3 / 15.4 | 9.8 / 11.8 | 6.8 / 9.3 |
| 22% (2028 framework) | 17.5 / 18.3 | 13.0 / 14.7 | 10.0 / 12.2 |

**Trend paths to FY27 (research estimate — the team chooses its own):**
- Same-basis pace from H1'25 to H1'26 is +7.0 points central (range 5.7–8.4). From FY25 to H1'26 it is about +10 points annualised.
- From H1'26 (midpoint April 2026) to FY27 (midpoint July 2027) is about 1.25 years. At 6–10 points a year, that is +7.5 to +12.5 points. FY27 e lands at **+7.5% to +12.5%** on my levels, or **+11% to +16%** on D06's.
- The Street's ~10–12% (at s = 28%) is reachable only if the pace does not slow.

**Timing evidence points to slower pace:**
- Strazik: "we will not begin delivering on the majority of the higher-margin orders placed in '24 and '25 until '27 and beyond" [S1: Q4'25 call, corpus chunk 246127] [S2: trade press, corpus chunk 216351].
- The CEO said the 2026 change in margin in backlog "tells you the equipment margins for '29 and '30, largely" [Morgan Stanley Laguna, 2026-09-16, gevernova.com PDF p.10 (facts VF-02)] **[SINGLE-SOURCE; not re-read tonight]**.
- If FY27 adds only +3 to +5 points, e is about 4–6% and Power margin about 18.6–19.0% at s = 28%, w = 0.6. That is GLJ territory.
- **Offsets:** services pricing (CFO Parks, chunk 246150) and overhead leverage (10.6% of Power revenue in H1'26 vs 13.1% in FY23). Each +1 point of s cuts the required e by 1.5 points at w = 0.6.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Power FY25 note lines | Q1 table | FY25 10-K p.72 | Q4'25 release Power table | exact | H |
| 2 | Power FY23/FY24 lines | Q1 table | FY24 10-K SEGMENT EBITDA | FY25 10-K p.72–73 | exact | H |
| 3 | Power H1'26 / Q2'26 lines | Q1 table | Q2'26 10-Q p.23 | Q2'26 release; deck chunk 251297 | exact | H |
| 4 | H1'25 recast | 6,178→6,232 services; EBITDA 1,286→1,303 | Q2'25 10-Q p.23 | Q2'26 10-Q p.23; reason in Q1'26 10-Q Note 1 | conflict, explained | H |
| 5 | Equipment/services split by segment, FY25 | 6,420 / 13,072 etc. | FY25 10-K p.72 | ties to income statement 20,934 | internal tie only | M-H |
| 6 | Company-wide services and equipment P&L | see Q1 | FY25 10-K p.39; Q2'26 10-Q p.6 | XBRL GrossProfit 7,535; FY24 10-K comparatives | exact | H |
| 7 | D&A by segment | Power 467 / 519 / 494 | FY25 10-K p.73 | — **[SINGLE-SOURCE]** | – | M |
| 8 | Cost lines exclude D&A; not split by equipment/services | — | FY25 10-K p.72 footnote (b) | Q2'26 10-Q p.23 footnote (b) | exact | H |
| 9 | About half of R&D supports existing products and the installed base | ~50% | FY25 10-K p.7 | — **[SINGLE-SOURCE]** | – | M |
| 10 | YE22 Power equipment backlog margin ≈ breakeven | ~0, contribution | chunk 246150 | facts PMX-26 (same call) | exact, same event | M-H |
| 11 | GE gas new-unit contribution margin LSD-MSD | 2019–20 | GE 2019 outlook deck | UBS 2020 transcript (via D06) | close | M |
| 12 | Higher-margin 2024-25 orders deliver "'27 and beyond" | — | chunk 246127 | chunk 216351 (trade press) | exact | H |
| 13 | '29-'30 timing quote | — | MS Laguna PDF p.10 | — | SINGLE | M |
| 14 | GLJ Power FY27 18.5% vs "consensus" 20.7% | — | Yahoo 2026-09-15 | Investing.com (likely the same wire) | exact | M-L |
| 15 | Company services gross margin falling | 35.1 → 32.0 → 31.3 → 31.6% | computed from #6 | D06 §5 G21 (independent recomputation) | exact | H |

## 4. Arithmetic

**Power gross profit before D&A** = segment revenue − cost of revenues: FY23 4,011; FY24 4,519; FY25 5,140; H1'25r 2,416; H1'26 2,945; Q2'26 1,611.

**Overhead** = SG&A + R&D + other: 2,290 / 2,251 / 2,238 / 1,113 / 1,104 / 581. Each ties to reported EBITDA within $1M (for example, 5,140 − 2,238 = 2,902).

**Company services gross profit:** 5,265 / 5,122 / 5,360 / 2,405 / 2,755 / 1,515.

**FY25 central case:**
1. d = 0.0175 × 17,134 = 300; Wind services profit 0.10 × 1,858 = 186; Electrification services profit 0.325 × 2,168 = 705.
2. Power services gross profit = 5,360 + 300 − 186 − 705 = 4,770 (36.5%).
3. Services overhead = 0.58 × 2,238 = 1,298, so services EBITDA = 3,472 (26.6%).
4. Equipment EBITDA = 2,902 − 3,472 = −570, which is −8.5% of 6,696 (6,420 + 276). On external equipment revenue only it is −8.9%.

**H1'26 central case:**
1. d = 153; Wind 117; Electrification 308. Power services gross profit = 2,482 (37.7%).
2. Services overhead = 640, so services EBITDA = 1,842 (27.9%).
3. Equipment EBITDA = 1,842 − 1,842 ≈ 0, which is 0.0% of 3,856.

**Low and high corners** use the parameter sets in Q2. I recomputed each and they tie to segment EBITDA by construction.

**Reproducing D06's FY25 central case** (d = 350, 25% blended non-Power services margin, overhead by revenue share): 5,360 + 350 − 1,006.5 = 4,703.5, which gives e = −4.79%. That confirms D06's arithmetic. Changing only the overhead share to 58% gives e = −7.5%.

**Q5 formula:** e = (M − w × s) / (1 − w). Example: (20.7 − 0.6 × 28) / 0.4 = 9.75%.

## 5. General question bank (G-numbers)

- **G2.** FY27 Power at 20.7% needs equipment EBITDA of about 10–15%, from about 0–4% in H1'26. The last 12 months delivered about +6–8 points, so this is not unprecedented, but it assumes no slowdown (Q5).
- **G12.** The segment cost excludes D&A, and the equipment/services split lives only inside one combined cost line. Revenue timing (percentage of completion, deposits) does not affect this split.
- **G20.** Definition traps:
  - contribution margin (backlog, 2019-20 LSD-MSD) vs EBITDA;
  - external vs intersegment revenue in the denominator (6,420 vs 6,696);
  - the recast of H1'25.
- **G21.** If services were driving the gains, company services gross margin should have risen. It fell 3.8 points from FY23 to FY25 (§3 row 15).

## 6. What would change this

- A disclosure of Wind or Electrification services margins, or of D&A inside cost of services. Early adoption of DISE (ASU 2024-03) would give an expense disaggregation.
- A GEV statement of equipment EBITDA or contribution margin, for example on the January 2027 call or at the spring-2027 CMD.
- Q3'26 10-Q, 2026-10-28, after the finals. If company services gross margin rises 2 points or more while Power margin is flat, the implied equipment margin falls. Power at 18% or more on equipment-led growth supports the steeper trend.

## 7. Disagreements with the master brief and D06

1. The assignment's premise that the segment note gives a cost split is wrong. It gives only a combined Power cost of revenues. The equipment/services split rests on three undisclosed parameters.
2. D06's central equipment levels look 3–5 points too high, mainly because it splits overhead by revenue share. The 10-K R&D language supports a higher equipment share of overhead.
3. The "breakeven" and "LSD-MSD" figures are contribution margins, which GE's 2019 deck states explicitly. They must not be compared directly with equipment EBITDA.
4. The research files contradict each other. D06 quotes a deck footnote defining backlog margin as "contribution margin"; evidence_lanes says GEV "has never defined" it. I could not find the footnote in the corpus.
5. The corpus labels the Q4'25 transcript 2026-01-23. The call and release were 2026-01-28.

## 8. Open items

- d and the Wind/Electrification services margins. Look in the Dec-2024 and Dec-2025 investor decks, and check for DISE early adoption.
- A second source for the '29-'30 quote. Re-read the Morgan Stanley Laguna PDF p.10.
- The 4Q'25 slide-5 footnote wording, which the corpus search did not return.
- An independent FY27 Power consensus other than GLJ's 20.7%. No free source was found.
- Power's FY27 services share (w). This is the team's modelling choice.
