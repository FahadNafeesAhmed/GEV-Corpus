# Exhibit data: series for the 2-3 charts that differentiate the memo

_R03_exhibit_data — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 04:35:56. Requests 24, input tokens 1285035, output tokens 28905._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV exhibit data pack: Power equipment vs services margin, backlog $/kW vs shipped $/kW, FY26–FY28 EBITDA paths (as of 2026-09-30)

*Research input only. Every range is a research estimate, and the team chooses its own numbers.*

**Source key**
- **10Q-2Q26** = 0001996810-26-000148 (Power MD&A p.29; segment note p.23; income statement p.6)
- **10Q-1Q26** = -26-000064 (Power MD&A p.25)
- **10Q-3Q25** = -25-000160 (Power MD&A p.29)
- **10K-25** = -26-000015 (Power MD&A p.26; segment note p.72–73; income statement p.39)
- **10K-24** = -25-000011
- **10Q-3Q24** = -24-000083
- **Releases (REL):** 1Q25 -25-000072; 2Q25 -25-000132; 3Q25 -25-000159; 4Q25 -26-000012; 1Q26 -26-000063; 2Q26 -26-000147
- **Call transcripts (CALL):** 3Q25 corpus src:3796/3771; 4Q25 src:2660; 2Q26 src:3161
- **MS** = MarketScreener, fetched 2026-09-29
- **E01 / D06 / F01** = earlier outputs from tonight's run

---

## 1. Bottom line

- **Exhibit 1 (Power equipment vs services margin).** In every assumption set, implied equipment EBITDA margin rises by about +30 points from FY23 to H1'26, while implied services margin stays around 24–30%. The *level* is not reliable: H1'26 is anywhere from −9% to +11%. I re-derived the central case by hand for FY23, FY24, H1'25, Q2'26 and FY25/H1'26; it ties to E01 within 0.1 point. [S1: 10K-25 p.39, p.72] [S2: 10Q-2Q26 p.6, p.23; REL-4Q25 and REL-2Q26 Power tables]
- **Exhibit 2 (backlog $/kW vs shipped $/kW).**
  - Power equipment RPO per firm gas GW rose from $556/kW (Q2'25) to $741/kW (Q2'26).
  - Trailing-12-month Power equipment revenue per gas GW shipped rose from $381 to $516/kW.
  - Backlog has run about 1.4–1.5x trailing shipped revenue in every quarter. Both measures overstate gas-only $/kW (see caveats).
  - [S1: 10-Q/10-K Power MD&A tables] [S2: next-year comparatives; release GW statements]
- **Exhibit 2 add-on.** An RPO roll-forward gives implied equipment value per ordered GW of $620–753/kW for Q2'25–Q1'26 and **$1,049/kW in Q2'26**. Management attributes part of the Q2 $/kW rise to aeroderivative and combined-cycle mix, so this is not like-for-like. [S1: computed from 10Q-2Q26 p.29] [S2: CALL-2Q26 src:3161]
- **Exhibit 3 (EBITDA paths).**
  - FY27: consensus $9,574M vs the straight line from the FY26 guide midpoint to the 2028 framework at $8,590M. The gap is +11.5%. A geometric or margin-linear line gives $8.18–8.42B.
  - FY28: consensus $13,064M vs framework $11,200M, +16.6%.
  - Research base: FY27 $8.6–8.9B, FY28 $11.0–11.2B.
  - [S1: MS] [S2: FactSet $9.5B FY27 via MoneyCheck; Yahoo/GLJ "Street $9.45B"]
- **Fastest read for a 3–5 minute first-round reader: Exhibit 3.** Three lines, one sourced gap, no hidden assumptions. Exhibit 2 is second (two ratios, but caveats needed). Exhibit 1 is slowest: it rests on four undisclosed parameters and belongs in an appendix.
- **One new conflict for the brief.** A Morgan Stanley note summary (2026-07-25) says a "December analyst day is the next scheduled checkpoint". The brief says no December 2026 event is listed. **[SINGLE-SOURCE, low-quality aggregator]** (fancyhints.com); not resolved.

---

## 2. Answers

### Exhibit 1 — Power equipment vs services implied EBITDA margin (FY23 to Q2'26)

**Series (%).** "Low equipment" is the case where every parameter pushes services margin to its high; "high equipment" is the reverse.

| Period | Power segment EBITDA margin (reported) | Services: central | Services band (low–high) | **Equipment: central** | Equipment band (low equip – high equip) | D06 central (alternative) | Joint E01+D06 band |
|---|---|---|---|---|---|---|---|
| FY23 | 9.88 | 29.7 | 24.8–34.5 | **−31.1** | −41.2 to −21.0 | −27 | −41 to −19 |
| FY24 | 12.51 | 26.7 | 21.8–31.6 | **−18.1** | −28.7 to −7.5 | −13.5 | −29 to −5 |
| FY25 | 14.68 | 26.6 | 21.5–31.6 | **−8.5** | −18.3 to +1.3 | −4.8 | −18 to +3.5 |
| H1'25 (recast) | 14.11 | 24.3 | 19.4–29.2 | **−7.0** | −17.3 to +3.2 | −2.5 | — |
| H1'26 | 17.63 | 27.9 | 22.7–33.1 | **0.0** | −8.9 to +8.9 | +3.6 | −9 to +11 |
| Q2'26 | 18.82 | 29.5 | 24.3–34.7 | **−0.2** | −9.4 to +9.0 | +4 | — |

Sources: [S1: E01 §2 Q2 scenario table, rebuilt from 10K-25 p.72–73 and 10Q-2Q26 p.23] [S2: D06 central via F01 Q2; reported Power margins in REL-4Q25 and REL-2Q26 Power tables].

**Formula.**
1. Power services gross profit before D&A = (company services revenue − company cost of services) + d − (Wind services revenue × gW) − (Electrification services revenue × gE)
2. Services EBITDA = Power services gross profit − k × (Power SG&A + R&D + other segment items)
3. Equipment EBITDA = Power segment EBITDA − services EBITDA
4. Equipment margin = equipment EBITDA ÷ (segment-note equipment revenue + intersegment revenue)

**Assumptions (all undisclosed by GEV; the team chooses):**

| Parameter | Central | Low-equipment case | High-equipment case | Basis |
|---|---|---|---|---|
| d = services D&A as % of company services revenue | 1.75% | 2.5% | 1.0% | FY25 total D&A $853M caps d [10K-25] |
| gW = Wind services gross margin | 10% | 0% | 20% | E01 |
| gE = Electrification services gross margin | 32.5% | 25% | 40% | E01 |
| k = services share of Power overhead | 58% | 50% | 66% | 58%: 10-K R&D description (~half supports installed base) [10K-25 p.7]. 66% = revenue share (D06) |

Central case holds all parameters constant over time. The band sets all four at their extremes at once; I verified this for FY25: 31.6% / −18.3%.

**Inputs (US$M), each with two sources:**

| Input | FY23 | FY24 | FY25 | H1'25r | H1'26 | Q2'26 |
|---|---|---|---|---|---|---|
| Company services sales / cost | 14,981 / 9,716 | 15,983 / 10,861 | 17,134 / 11,774 | 8,052 / 5,647 | 8,729 / 5,974 | 4,645 / 3,130 |
| Wind / Electrification services revenue | 1,488 / 1,733 | 1,642 / 1,923 | 1,858 / 2,168 | 885 / 916 | 1,174 / 948 | 631 / 497 |
| Power equipment / services / intersegment revenue (segment note) | 5,535 / 11,758 / 143 | 5,509 / 12,391 / 227 | 6,420 / 13,072 / 276 | 2,881 / 6,232 / 121 | 3,834 / 6,593 / 22 | 1,957 / 3,509 / 12 |
| Power SG&A / R&D / other | 2,124 / 315 / (149) | 2,022 / 384 / (155) | 1,836 / 549 / (147) | 930 / 242 / (59) | 918 / 286 / (100) | 472 / 154 / (45) |
| Power segment EBITDA | 1,722 | 2,268 | 2,902 | 1,303 | 1,842 | 1,031 |

- FY23–FY25: [S1: 10K-25 p.39, p.72–73] [S2: 10K-24 same tables; REL-4Q25 Power table (FY25 exact)]
- H1 and Q2: [S1: 10Q-2Q26 p.6, p.23] [S2: REL-2Q26 Power table; the Q2'26 MD&A p.29 reads segment EBITDA $1,031 / $1,842 and margins 18.8% / 17.6%, which I checked this session]

**What the chart shows.** The Power margin climb from 9.9% to 18.8% sits almost entirely in implied equipment margin (about +30 points). Implied services margin is roughly flat.

**Traps to label on the chart:**
- Segment-note equipment revenue (H1'26 3,834) differs from MD&A equipment revenue (3,851), which folds in intersegment revenue. Use the segment note.
- H1'25 is recast for the 1-Jan-2026 business realignment (services 6,178 → 6,232). FY23–FY25 are on the old basis.
- These are EBITDA margins. Management's "breakeven at YE2022" is a backlog *contribution* margin, a different basis.
- Holding gW and gE constant over time is itself an assumption. If Electrification services margin rose over the period, early-year equipment margins would be less negative and the +30-point change would shrink. I did not quantify this.

### Exhibit 2 — Power equipment backlog $/kW vs revenue $/kW shipped, by quarter

**Series.** All values in $/kW; 1 $M per GW = $1/kW.

| Quarter-end | Power equipment RPO ($M) | Firm gas backlog (GW) | **Backlog $/kW** | Power equipment revenue in quarter ($M, MD&A) | Gas GW shipped | Quarterly rev $/kW | **TTM rev $/kW** | Backlog ÷ TTM | Gas GW ordered | Implied additions $/kW* |
|---|---|---|---|---|---|---|---|---|---|---|
| FY23 (year) | 13,636 | n.a. | n.a. | 5,598 | 13.8 | — | 406 (FY) | — | 9.5 | — |
| Q3'24 | 11,392 | n.a. | n.a. | 1,426 | 3.3 | 432 | — | — | 5.1 | — |
| Q4'24 | 12,461 | ~25 (derived) | ~498 | 1,796 | 4.8 | 374 | 480 (FY24) | ~1.04 | — | — |
| Q1'25 | 13,920 | 29 | 480 | 1,491 | 3.0 | 497 | — | — | 7.1 | 415 |
| Q2'25 | 16,133 | 29 | 556 | 1,504 | 5.2 | 289 | 381 | 1.46 | 5.1 | 729 |
| Q3'25 | 18,977 | 33 | 575 | 1,744 | 4.0 | 436 | 384 | 1.50 | 7.4 | 620 |
| Q4'25 | 24,707 | 40 | 618 | 1,946 (derived) | 3.1 (derived) | 628 | 437 (FY25) | 1.41 | 10.2 (derived) | 753 |
| Q1'26 | 28,530 | 44 | 648 | 1,885 | 4.2 | 449 | 429 | 1.51 | 8.1 | 705 |
| Q2'26 | 39,261 | 53 | **741** | 1,965 | 3.3 | 595 | **516** | 1.44 | 12.1 | **1,049** |

*Implied additions $/kW = (ΔRPO + equipment revenue in the quarter) ÷ gas GW ordered.

**Formulas.**
- Backlog $/kW = Power equipment RPO ÷ firm gas backlog GW
- TTM rev $/kW = sum of the last four quarters' Power equipment revenue ÷ sum of GW shipped
- Implied additions $/kW = (RPO_t − RPO_t−1 + equipment revenue_t) ÷ GW ordered_t

**Input sources:**
- **Power equipment RPO:**
  - Q2'26 39,261 and Q2'25 16,133: [S1: 10Q-2Q26 p.29] [S2: web analysis src:234, "$39.3 billion", which also gives YE24 $12.5B].
  - Q1'26 28,530 and Q1'25 13,920: [S1: 10Q-1Q26 p.25]. Q1'26 is **[SINGLE-PUBLISHER]**; its comparative arrives in the Q1'27 10-Q.
  - Q3'25 18,977, YE24 12,461 and Q3'24 11,392: [S1: 10Q-3Q25 p.29] [S2: 10K-25 p.26 for YE24; 10Q-3Q24 for Q3'24].
  - YE25 24,707: [S1: 10K-25 p.26] [S2: 10Q-1Q26 and 10Q-2Q26 comparatives, exact].
  - Note: YE25 *services* RPO is 69,680 in the 10-K but 69,841 in the 2026 10-Qs (recast). Equipment is unchanged.
- **Firm GW:**
  - Q1'25 29: [S1: REL-1Q25] [S2: Simon Mahan on X, corpus src:241].
  - Q2'25 29 ("backlog remaining at 29 GW"): [S1: REL-2Q25] [S2: REL-3Q25 "from 29 to 33"].
  - Q3'25 33: [S1: REL-3Q25] [S2: CALL-3Q25 src:3796].
  - Q4'25 40: [S1: REL-4Q25 via REL-1Q26 "from 40"] [S2: CALL-4Q25 src:2660, "backlog increasing from 33 to 40 gigawatts"].
  - Q1'26 44: [S1: REL-1Q26] [S2: trade press src:230/227].
  - Q2'26 53: [S1: REL-2Q26] [S2: CALL-2Q26 src:3161, "100 to 116" total].
  - YE24 ~25 is derived: 29 − 7.1 ordered + 3.0 shipped. No direct YE24 firm-GW disclosure found.
  - **Tie-out:** backlog_t−1 + ordered − shipped reproduces each reported GW within 0.6 GW (Q2'25 28.9; Q3'25 32.4 vs 33; Q4'25 40.1; Q1'26 43.9; Q2'26 52.8). That is an internal second check from the 10-Q unit tables.
- **GW shipped and ordered:** [S1: each quarter's 10-Q "Sales in units" / "Orders in units"] [S2: next year's 10-Q comparative (D01A §Q1 table), plus release lines "shipped 5/4/4/3 GW"]. Q4 figures are derived as FY (10K-25: 15.3 shipped, 29.8 ordered) minus 9M (10Q-3Q25: 12.2 / 19.6).
- **Power equipment revenue (MD&A basis):**
  - Q2'26 1,965 and Q2'25 1,504: [10Q-2Q26 p.29].
  - Q1'26 1,885 and Q1'25 1,491: [10Q-1Q26 p.25].
  - Q3'25 1,744 and 9M 4,740: [10Q-3Q25 p.29].
  - FY25 6,686, FY24 5,708 and FY23 5,598: [10K-25 p.26].
  - Q3'24 1,426 and 9M'24 3,912: [10Q-3Q25 comparatives].
  - Recast check: old-basis H1'25 (4,740 − 1,744 = 2,996) equals recast H1'25 (2,996), so the realignment did not move Power *equipment* revenue.
  - The releases do not show Power equipment revenue (I searched the 2Q26 release), so the second source for each figure is a later filing's comparative (same publisher). **[M confidence]**

**Caveats, which the team must state on the chart:**
1. RPO includes nuclear, hydro and steam equipment, but GW counts gas turbines only. This biases backlog $/kW **up**.
2. RPO excludes revenue already recognised on over-time contracts, while GW counts full units until shipped. This biases backlog $/kW **down**.
3. Revenue per kW shipped includes non-gas equipment revenue and over-time revenue not tied to shipments. That makes it a scaling ratio, not a price.
4. Aeroderivative mix: Q2'26 shipped 16 aero of 29 units, and the Q2'26 order mix was aero- and combined-cycle-heavy [S1: 10Q-2Q26 p.29 units] [S2: CALL-2Q26 src:3161, "higher dollar per kW price in orders, given a higher mix of aeroderivatives"].
5. Firm GW are rounded integers: ±0.5 GW moves Q2'26 backlog $/kW by about ±$7.

**Cross-checks on the level:**
- CEO-endorsed GE slice of plant cost ≈ $750/kW (30% × $2,500) [S1: CALL-3Q25 src:3796] [S2: Motley Fool transcript, via F01 Q6].
- Morgan Stanley reportedly assumes ~$900/kW on 2030 shipments **[SINGLE-SOURCE: fancyhints.com, 2026-07-25]**.

**What the chart shows.** Backlog $/kW and trailing shipped $/kW both rose by about a third over four quarters. Backlog stays about 40–50% above what is being shipped. The Q2'26 order value per GW jumped to about $1,049/kW, partly because of mix.

### Exhibit 3 — FY26 → FY27 → FY28 adjusted EBITDA paths ($M)

| Path | FY25 actual | FY26 | FY27 | FY28 | FY27 vs consensus | FY28 vs consensus |
|---|---|---|---|---|---|---|
| **Consensus (MS)** | 3,196 | 6,359 (13.74%) | 9,574 (18.15%) | 13,064 (21.59%) | — | — |
| **Straight line, $ (guide mid → framework)** | 3,196 | 5,980 (range 5,460–6,510) | **8,590** | 11,200 | −10.3% | −14.3% |
| Straight line, geometric (constant growth) | 3,196 | 5,980 | 8,184 | 11,200 | −14.5% | — |
| Straight line, revenue and margin separately | 3,196 | 5,980 (46.0B × 13%) | 8,415 (51.0B × 16.5%) | 11,200 (56B × 20%) | −12.1% | — |
| Straight line from consensus FY26 | 3,196 | 6,359 | 8,780 | 11,200 | −8.3% | — |
| **Research base (team's choice)** | 3,196 | within guide 5,460–6,510 (not separately built) | **8,600–8,900** (low 7,700 / high 9,580, D01A) | **11,000–11,200** (low 9,700 / high 12,600) | −7% to −10% | −14% to −16% |

**Input sources:**
- FY25 3,196: [S1: 10K-25 p.72] [S2: REL-4Q25 p.2].
- FY26 guide ($45.5–46.5B revenue, 12–14% margin): [S1: REL-2Q26 guide box] [S2: CALL-2Q26; Reuters 2026-07-22, "unchanged at 12%-14%"].
- 2028 framework ($56B, 20%): [S1: REL-4Q25] [S2: DEC25 release, per F01 row 9].
- Consensus FY27 9,574: [S1: MS, EBITDA row, 2026-09-29] [S2: FactSet "$9.5 billion" via MoneyCheck; Yahoo/GLJ "Street's $9.45 billion"]. Agreement: close (−0.8% / −1.3%).
- Consensus FY26 6,359: [S1: MS] [S2: Barron's via MSN, July 2026, "Wall Street currently projects Ebitda of $6.2 billion"]. **Conflict of −2.5%.** The likely cause is vintage (the Barron's figure dates from the Q2 print) or vendor differences; not resolved.
- Consensus FY28 13,064: [S1: MS] [S2: Motley Fool "~60% CAGR". I computed (13,064 / 3,196)^(1/3) − 1 = 59.9%, which reconciles].
- Research base: [S1: D01A §1/§4] [S2: D01B §4-J; F01 Q1].

**What the chart shows.** Consensus bends above the straight line to management's own 2028 plan from FY27 onward. The gap is about $1.0B in FY27 and $1.9B in FY28. The research base tracks the plan line.

### Which exhibit is fastest for a first-round reader

Exhibit 3. It has three lines, public anchors (guide and framework), and one sourced gap (+11.5% in FY27, +16.6% in FY28). The only definition trap is the adjusted-EBITDA basis, and MS matches GEV's adjusted basis on FY24/FY25 actuals (facts CT-02).

Exhibit 2 needs roughly one line of caveats. Exhibit 1 needs four stated assumptions and a band wider than the signal in level terms. It persuades only on *change*, so it fits an appendix better than the front page. This is an observation, not a layout choice.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Power segment margins FY23–Q2'26 | 9.88 / 12.51 / 14.68 / 14.11 / 17.63 / 18.82% | 10K-25 p.72; 10Q-2Q26 p.23 | REL-4Q25 and REL-2Q26 Power tables; 10Q-2Q26 MD&A p.29 | exact | H |
| 2 | Implied equipment margin change FY23 → H1'26 | +30 to +32 pts (E01); +25 to +31 (D06) | E01 §1 | D06 via F01 Q2; my re-derivation | close | M |
| 3 | Equipment level H1'26 | 0.0% central; band −9 to +11% | E01 | D06 +3.6% | conflict (assumption-driven) | L |
| 4 | Power equipment RPO Q2'26 | $39,261M | 10Q-2Q26 p.29 | src:234 "$39.3B" | exact | H |
| 5 | Power equipment RPO Q1'26 | $28,530M | 10Q-1Q26 p.25 | — **[SINGLE-PUBLISHER]** | — | M |
| 6 | Firm gas backlog Q3'25 → Q2'26 | 33 / 40 / 44 / 53 GW | REL-3Q25, REL-1Q26, REL-2Q26 | CALL-3Q25, CALL-4Q25, trade press, CALL-2Q26; unit roll-forward ties | exact | H |
| 7 | GW shipped Q1'25 → Q2'26 | 3.0 / 5.2 / 4.0 / 3.1 / 4.2 / 3.3 | 10-Q unit tables | next-year comparatives; release "shipped" lines | exact (Q4 derived) | H |
| 8 | Power equipment revenue Q2'26 / Q1'26 | 1,965 / 1,885 | 10Q-2Q26 p.29; 10Q-1Q26 p.25 | 10Q-2Q26 H1 3,851 (sum ties) | exact | M–H |
| 9 | Backlog $/kW Q2'26 | $741 | computed #4 ÷ #6 | facts RV-25 "$740.8" | exact | M (definition caveats) |
| 10 | Q2'26 order $/kW lifted by mix | quote | CALL-2Q26 src:3161 | facts GLJ-30 lane note | exact | H |
| 11 | Consensus FY27 EBITDA | $9,574M | MS 09-29 | FactSet $9.5B (MoneyCheck); Street $9.45B (Yahoo/GLJ) | close | M–H |
| 12 | Consensus FY26 EBITDA | $6,359M | MS | Barron's/MSN $6.2B (Jul-26) | conflict (−2.5%) | M |
| 13 | Consensus FY28 EBITDA | $13,064M | MS | Motley Fool 60% CAGR (reconciles) | close | M |
| 14 | 2028 framework | $56B / 20% / $11.2B | REL-4Q25 | DEC25 release | exact | H |
| 15 | FY26 guide | $45.5–46.5B; 12–14% | REL-2Q26 | Reuters 07-22; CALL-2Q26 | exact | H |
| 16 | "December analyst day" per MS note | claim | fancyhints 2026-07-25 | none **[SINGLE-SOURCE]** | conflicts with brief | L |

---

## 4. Arithmetic

**A1. Exhibit 1 re-derivation (central case; ties to E01):**
- FY23:
  - Services GP = 14,981 − 9,716 = 5,265.
  - Power services GP = 5,265 + 262 − 149 − 563 = 4,815.
  - Overhead = 2,124 + 315 − 149 = 2,290; × 0.58 = 1,328.
  - Services EBITDA = 3,487 / 11,758 = **29.7%**.
  - Equipment = 1,722 − 3,487 = −1,765 / 5,678 = **−31.1%**.
- FY24:
  - Power services GP = 5,122 + 280 − 164 − 625 = 4,613.
  - Overhead = 2,251 × 0.58 = 1,306.
  - Services = 3,307 / 12,391 = **26.7%**.
  - Equipment = −1,039 / 5,736 = **−18.1%**.
- H1'25 recast:
  - Power services GP = 2,405 + 141 − 88.5 − 297.7 = 2,160.
  - Overhead = 1,113 × 0.58 = 645.5.
  - Services = 1,514 / 6,232 = **24.3%**.
  - Equipment = −211 / 3,002 = **−7.0%**.
- Q2'26:
  - Power services GP = 1,515 + 81 − 63 − 161.5 = 1,372.
  - Overhead = 581 × 0.58 = 337.
  - Services = 1,035 / 3,509 = **29.5%**.
  - Equipment = −3.7 / 1,969 = **−0.2%**.
- FY25 and H1'26: see F01 A4 and Q2 (26.55% / −8.5%; 27.95% / 0.0%).
- FY25 all-corners (high-services) check: (5,360 + 428 − 0 − 542 − 1,119) / 13,072 = 31.6%, and equipment (2,902 − 4,127) / 6,696 = −18.3%. This confirms the band is the simultaneous-extremes case.

**A2. Exhibit 2:**
- Q2'26 backlog $/kW: 39,261 / 53 = 740.8.
- TTM Q2'26 revenue $/kW: (1,744 + 1,946 + 1,885 + 1,965) / (4.0 + 3.1 + 4.2 + 3.3) = 7,540 / 14.6 = 516.4.
- TTM Q2'25: (1,426 + 1,796 + 1,491 + 1,504) / (3.3 + 4.8 + 3.0 + 5.2) = 6,217 / 16.3 = 381.
- Q4'25 derived lines:
  - Equipment revenue: 6,686 − 4,740 = 1,946.
  - GW shipped: 15.3 − 12.2 = 3.1.
  - GW ordered: 29.8 − 19.6 = 10.2.
- Q4'24 equipment revenue: 5,708 − 3,912 = 1,796.
- Implied Q2'26 additions: (39,261 − 28,530 + 1,965) / 12.1 = 12,696 / 12.1 = 1,049.
- Four-quarter changes:
  - Backlog $/kW: 741 / 556 = +33%.
  - TTM rev $/kW: 516 / 381 = +35%.

**A3. Exhibit 3:**
- Guide midpoint: 46.0 × 13% = 5,980. Low: 45.5 × 12% = 5,460. High: 46.5 × 14% = 6,510.
- FY27 straight lines:
  - Dollar: (5,980 + 11,200) / 2 = 8,590.
  - Geometric: √(5,980 × 11,200) = 8,184.
  - Revenue and margin: 51.0B × 16.5% = 8,415.
  - From consensus FY26: (6,359 + 11,200) / 2 = 8,780.
- Gaps: 9,574 / 8,590 − 1 = +11.5%; 13,064 / 11,200 − 1 = +16.6%.
- Framework CAGR FY25 → FY28: (11,200 / 3,196)^(1/3) − 1 = 51.9%, vs consensus 59.9%.

---

## 5. General question bank items answered

- **G1 (physical terms).** The backlog now carries about $741/kW (upper bound), against about $516/kW shipped TTM. The priced-in path needs the higher-value backlog to convert, but shipped $/kW was flat around $430 until Q2'26.
- **G6 (where the variant sits).** FY27 by about $1.0B vs the plan line, and FY28 by about $1.9B vs the framework (A3).
- **G12 (accounting timing).** The RPO roll shows $12.7B of equipment added in Q2'26 against $1.97B recognised. Revenue lags orders by years, and TTM shipped $/kW moves slowly. [S1: 10Q-2Q26 p.29] [S2: F01 row 16, RPO timing]
- **G20 (definition traps).**
  - Segment-note vs MD&A equipment revenue.
  - Recast H1'25.
  - Services RPO recast at YE25 (69,680 vs 69,841).
  - Contribution vs EBITDA margin.
  - RPO includes non-gas equipment.

---

## 6. What would change this

- **Exhibit 1:** any GEV disclosure of Power services D&A or the equipment/services cost split (FY26 10-K, CMD). A Siemens Energy new-unit margin disclosure on 11-11 could also cross-check the level.
- **Exhibit 2:**
  - If Q3'26 TTM shipped $/kW does not rise as 5 GW/qtr heavy-duty deliveries start, the backlog-vs-shipped gap reflects mix and scope rather than price.
  - A nuclear-heavy RPO build (SMR orders) would inflate backlog $/kW without any gas pricing change.
- **Exhibit 3:**
  - A second full-row vendor (FactSet or Bloomberg FY26 and FY28 EBITDA) differing by more than 3% from MS.
  - A 2028 framework raise at a December or spring event, which would move the plan line up.

---

## 7. Disagreements with the master brief

1. The brief says no December 2026 investor event is listed. A 2026-07-25 summary of a Morgan Stanley note says a "December analyst day is the next scheduled checkpoint" **[SINGLE-SOURCE, low quality]**. This needs a check of the GEV events page and the 10-28 call.
2. The FY26 consensus EBITDA of $6,359M is not vendor-robust: Barron's (July) has $6.2B.
3. Otherwise none. The F01 corrections carry over.

---

## 8. Open items

- **Q1'26 and Q3'25 Power equipment RPO second source:** the comparatives only arrive in the Q1'27 and Q3'26 10-Qs. Check the quarterly earnings decks on gevernova.com/investors for a segment RPO chart.
- **YE24 firm gas GW:** derived (~25). Check the Q4'24 release (Jan-2025) or the Q4'24 call.
- **Non-gas share of Power equipment RPO:** not disclosed. The Gas/Nuclear/Hydro revenue split is total revenue only (10Q-2Q26 p.29).
- **Consensus FY26 and FY28 from a second vendor:** Visible Alpha, FactSet or Bloomberg.
- **Exhibit 1 sensitivity to a rising Electrification services margin over time:** not quantified.
- **The "December analyst day" claim:** verify it against the Morgan Stanley note or the GEV events calendar.
