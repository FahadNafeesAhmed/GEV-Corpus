# Outside view: how fast have competitors turned order prices into margins?

_S05_peer_conversion_pace — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 10:36:18. Requests 53, input tokens 3832674, output tokens 34704._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV outside view: how fast have peers turned order pricing into segment margin?

**Scope and method.** This is research input only: facts, arithmetic and ranges. Every "range" below is a research estimate; the team chooses its own numbers.

I read F01, V07 and P6 first. None of them had a peer margin base rate, so everything in this file is new work, built from:
- the competitor filings and decks in the corpus;
- Exa and web search for years the corpus lacks.

**On the two-citation rule.** Many peer numbers appear in two documents from the *same* publisher, for example the Siemens Energy earnings release and its analyst deck. They are independent documents but not independent publishers, and the tables flag this as "same-publisher".

**Source key**

| Key | Document | Location |
|---|---|---|
| SE-Q3P | Siemens Energy Q3 FY26 analyst deck (Aug-2026) | corpus src:3167, chunks 251676–79 |
| SE-Q3R | SE Q3 FY26 earnings release | src:3166, chunks 251647–48 |
| SE-Q2P | SE Q2 FY26 deck (May-2026) | src:3172, chunks 251757/59 |
| SE-Q2R | SE Q2 FY26 release | src:3171, chunks 251733–34; siemens-energy.com press release 2026-05-12 |
| SE-Q1R | SE Q1 FY26 release | src:3177, chunk 251841 |
| SE-AR25 | SE Annual Report 2025 | src:3180, chunk 251959, §2.4.2 |
| SE-FY25D | SE FY25 results deck with FY28 targets (Nov-2025) | src:3181, chunk 252553 |
| SE-CFO26 | SE CFO deck, Jan-2026 | src:3179, chunks 251878/80/93 |
| SE-IR26 | SE IR deck, Mar-2026 | src:3175, chunk 251823 |
| SE-Q4FY24 | SE Q4 FY24 release, 2024-11-13 | assets.siemens-energy.com …/Earnings-Release-Q4_EN_final.pdf |
| SE-CMR24 | SE FY24 Combined Management Report | assets.siemens-energy.com …/B-Combined-Management-Report-excl--NFS.pdf, segment table |
| SE-PR24 | SE press release and press deck, 2024-11-13 | siemens-energy.com |
| MHI-FY24 | MHI FY2024 results deck | src:3219, chunk 253146 |
| MHI-FY25 | MHI FY2025 results deck | src:3201, chunk 252771; src:3202 |
| MHI-QA | MHI FY2025 results Q&A | src:3203, chunk 252828 |
| MHI-Q1 | MHI Q1 FY2026 deck | src:3197, chunks 252664–65; src:3198, chunk 252683 |
| TP-MHI | Trade press on MHI's 2026-08-06 briefing | corpus src:345, chunk 218572; src:1743 (news 2026-08-13), chunk 235390 |
| HIT25 | Hitachi FY2025 outline, 2026-04-27 | hitachi.com …/2025_Anpre.pdf |
| HIT25b | Hitachi FY2025 results announcement | hitachi.com …/2025_An.pdf |
| ETN25 | Eaton 10-K 0001551182-26-000007 | chunk 20935 |
| ETN23 | Eaton 10-K 0001551182-24-000006 | chunks 99474–75 |
| HUBB25 / HUBB24 / HUBB23 | Hubbell 10-Ks 0001628280-26-007500 / -25-005311 / -24-003792 | segment results |
| SU25R / SU25P | Schneider FY25 release / presentation, 2026-02-26 | se.com |
| GEV10K | GEV 10-K 0001996810-26-000015 | segment MD&A and non-GAAP organic table |

---

## 1. Bottom line

- **Distribution of realised one-year margin steps.** Across 17 realised steps at direct and adjacent peer segments (FY22–FY25), the median step is **+3.1 pts**, the 75th percentile **+3.9 pts** and the maximum **+6.7 pts** (Hubbell Utility Solutions, 2023, adjusted operating margin).
  - The only other step above +4.4 pts is Siemens Energy (SE) Grid Technologies FY25, at about +4.8 pts.
  - The largest step in heavy-duty gas is **+3.5 pts** (SE Gas Services FY25). MHI Energy Systems managed +2.6 and +1.7.
  - [computed §4; inputs SE-AR25 + SE-CMR24; MHI-FY24 + MHI-FY25; ETN23 + ETN25; HUBB23 + HUBB24 + HUBB25; HIT25 + HIT25b]
- **Where GEV's company steps sit.** The Street's +4.4 pts for FY27 sits at about the **88th percentile**: 2 of 17 peer segment-years reached it. The research base's +3.3 pts sits at about the **53rd percentile**.
  - Caveat: GEV's figure is a *company* margin, and it gets a mechanical lift from the Wind loss shrinking (about 0.76 pts, per F01/E05).
  - The closest company-level analog, SE group FY24→FY25 at **+5.0 pts**, was also driven by a wind loss narrowing [SE-AR25 §2.4.2; SE-Q4FY24 / SE-PR24].
- **The gas peers show the lag directly.** SE Gas Services backlog margin rose about 12 pts on new units and about 3 pts on service between FY22 and FY25. Reported GS margin rose only **+6.4 pts** (6.6% → 13.0%) over the same three years.
  - Weighting the backlog-margin gains 40/60 new unit/service gives about +6.6 pts. That is roughly equal to the reported gain.
  - This is consistent with the whole backlog-margin gain reaching the P&L within about three years at SE's 3+-year lead times.
  - [SE-CFO26 chunk 251878; SE-IR26 chunk 251823; SE-AR25; lead times per the Power Engineering / trade-press report in corpus src:1699 — **SINGLE-SOURCE** on lead times]
- **The gas peers are accelerating now, but the fiscal-year steps are still around 2.5–3.6 pts.**
  - SE Gas Services: Q3 FY26 17.3% vs 13.0% (+4.2 pts year on year); 9M FY26 16.6% vs 14.6%. The FY26 guide of 14–16% was never raised, even though 9M already sits above its top [SE-Q3R; SE-Q3P].
  - MHI Energy Systems: Q1 FY26 18.9% vs 13.3%. The full-year forecast is 15.5% vs 13.0% (+2.5 pts), unchanged at Q1 [MHI-Q1; MHI-FY25].
- **GEV's own Electrification already beats the peer base rate.** Its margin went +5.3 pts (FY24) and +5.9 pts (FY25), 3.7% → 9.0% → 14.9%, which would rank 2nd and 3rd in the peer set.
  - Going from the FY26 guide of 18–20% to 22% in 2028 needs only about +1–2 pts a year. That is below the peer median.
  - GEV Power's **organic** step in FY25 was only **+1.0 pt** (13.2% → 14.2%) against +2.2 pts reported.
  - [GEV10K segment MD&A and organic non-GAAP table; S2: master brief §3 / FACTS for the reported Power series]
- **No sign of heavy-duty pricing flattening was found.**
  - MHI is explicitly restraining bookings as it doubles capacity: "does not mean that we are immediately seeking to book twice as many orders" [TP-MHI, two corpus copies of the same trade article — **same-origin**].
  - MHI's FY26 order forecast (¥3,550bn, raised from ¥3,450bn) is still **below** FY25's ¥3,936.7bn, which is the first year-on-year decline guided by a heavy-duty OEM [MHI-Q1; MHI-FY25].

---

## 2. Answers

### Q1. Siemens Energy Gas Services (GS)

Definition: "Profit before Special items" is earnings before financial result, taxes, amortisation of acquired intangibles and goodwill impairment. It is **after depreciation**, so it is EBITA-like, not EBITDA [SE-FY25D footnote 2; SE-Q3P p.15 footnote]. The FY25 EBITDA-like proxy is 14.49% [facts PMX-36, AR25 Note 26].

**Annual series (fiscal years end September)**

| FY | Orders €M | Revenue €M | Profit bef. SI €M | Margin | Step | Sources |
|---|---|---|---|---|---|---|
| FY22 | n/f | n/f | n/f | 6.6% | — | SE CMD 2025 GS deck slide 5 (facts PMX-39). **SINGLE-SOURCE**: the SE-CFO26 chart shows the bars but not the value |
| FY23 | 12,897 | 10,914 | **not found** | **not found** | — | SE-CMR24 (orders and revenue only) |
| FY24 | 16,365 | 10,796 | 1,021 | 9.46% [computed]; "9%" / "9.5%" | FY22→24: +2.9 pts over two years | SE-AR25 (profit); SE-CMR24 (revenue); SE-PR24 deck ("9.5%") |
| FY25 | n/f (€23bn per the IR deck) | 12,198 | 1,580 | 12.95%; "13.0%" | **+3.5 pts** | SE-AR25; SE-CFO26 chunk 251880 |
| FY26 9M | 27.6bn | 10.3bn | 1,715 | 16.6% (9M FY25: 14.6%) | +2.0 pts YTD | SE-Q3P; SE-Q3R |

**FY26 quarters**

| Quarter | Orders €M | Revenue €M | Profit bef. SI €M | Margin | YoY | Sources |
|---|---|---|---|---|---|---|
| Q1 FY26 | 8,751 (Q1 FY25: 5,009) | 3,097 | 515 | 16.6% (14.6%) | +2.1 pts | SE-Q1R; SE-Q2P (H1 − Q2 = 17.6 − 8.9 = €8.7bn orders; 1,067 − 552 = 515) |
| Q2 FY26 | 8.9bn (7.0bn) | 3.5bn (3.2bn) | 552 (511) | 15.9% (16.1%) | −0.2 pts | SE-Q2P; SE-Q2R |
| Q3 FY26 | 9,967 (6,180) | 3,756 (3,118) | 648 (406) | 17.3% (13.0%) | +4.2 pts | SE-Q3R; SE-Q3P |

- **Backlog:** €60bn (Q1), €66bn (Q2), €73bn (Q3; Q3 FY25 was €53bn) [SE-Q1R; SE-Q2P; SE-Q3P].
- **Book-to-bill:** 2.83, 2.6, 2.7.
- **In gigawatts:** 69 GW firm plus 26 GW of SRAs [facts RQ-16, SE Q3 FY26 deck p.6]. The trade press also reports 69 GW, with 15 GW booked in Q3 [corpus src:1699].

**FY26 guidance path (GS: comparable revenue growth / margin)**
- Set in Nov-2025 at 16–18% / 14–16% [SE-FY25D].
- Unchanged at Q1 [SE-Q1R/src:3177 chunk 251847].
- "(unchanged)" at Q2 [SE-Q2P chunk 251759; SE-Q2R chunk 251734].
- Reaffirmed at Q3 [SE-Q3P p.15; SE-Q3R chunk 251647].
- **The 9M margin of 16.6% is already above the top of the range.** GS Q4 is seasonally weak: Q4 FY24 was 5.2% after a legacy-project legal charge [SE-Q4FY24]. So the unraised guide is consistent with conservative guiding or Q4 risk. That is my inference, not a company statement.
- The group guide, by contrast, was raised at Q2 from 9–11% to 10–12%, with "a tendency towards the upper end" at Q3 [SE-Q2P; SE-Q3P].

**FY28 targets (GS margin)**
- CMD 2023 set 12–14% ("previous mid-term targets"), which carried through the Nov-2024 target upgrade [SE-CFO26 chunk 251880 footnote; SE-Q4FY24 group target 10–12%].
- **Raised to 18–20%** in Nov-2025, with revenue CAGR moving from "LSD/MSD" to "mid-teens" [SE-FY25D; SE-CFO26].
- So the GS FY28 margin target moved +6 pts in one step, about 3 years out.
- Date check: the SE-FY25D calendar dates Q1 FY26 to Feb 11, 2026, which places that deck in Nov-2025. The exact release day was not fetched.

**Management statements on pricing, backlog margin and conversion**
- Backlog margin: "Gas Services backlog margin up ~12 pp in new unit and ~3 pp in Service since FY22" [SE-CFO26 chunk 251878].
  - Split: +7 pp new unit / +2 pp service in FY22–24, then +5 / +1 in FY25 [SE-CFO26 chart; SE-IR26 "New unit (~40%) +5 pp… Service (~60%) +1 pp"].
- Q3 FY26: "Record order backlog with improved backlog margins"; about 87% of expected FY27 revenue is covered by existing backlog [SE-Q3P slide 9]. **SINGLE-SOURCE**, deck only.
- Q1 FY26 release attributes the gain partly to "higher profitability of the processed order backlog" [SE-Q1R chunk 251841].
- CFO, Q3 FY26: new orders "are still coming in at higher margins than older backlog" [facts TP-30, Investing.com transcript 2026-08-05]. I could not open a second transcript copy.
- Time to the P&L: SE did not state it in quarters. The nearest data points are lead times of "three years or longer" [corpus src:1699 — **SINGLE-SOURCE**] and the FY22→FY25 conversion arithmetic in §4.

**Next results date**
- Q4 FY26 plus FY27 guidance: **conflict between 2026-11-11 and 2026-11-12.**
  - facts PP-38 (SE IR page and Q3 FY26 deck p.18) gives 11 Nov and says it includes a "medium-term framework".
  - The Nov-2025 deck calendar (SE-FY25D) gives 12 Nov.
  - The later document (the Q3 FY26 deck) should govern. Re-check the SE IR calendar.
- Q1 FY27: 2027-02-11 [PP-38].

### Q2. MHI Energy Systems / GTCC

Fiscal years end March, so MHI's FY2025 = Apr-2025 to Mar-2026. "Profit from business activities" is an operating-profit measure, not EBITDA. Series are retroactively restated for reorganisations (GX Solutions in FY23; the Apr-2026 changes in FY25), which is a definition trap.

| FY | Orders ¥bn | Revenue ¥bn | Business profit ¥bn | Margin | Step | Sources |
|---|---|---|---|---|---|---|
| FY2022 | not found | not found | not found | — | — | — |
| FY2023 (restated) | 2,412.2 | 1,723.6 | 149.8 | 8.7% | — | MHI-FY24 chunk 253146; S2 not found (**SINGLE-SOURCE**) |
| FY2024 | 2,622.4 | 1,815.7 | 205.3 | 11.3% | +2.6 | MHI-FY24; MHI FY25-forecast deck src:3210 chunk 253005 (same figures) |
| FY2025 (restated) | 3,936.7 | 2,062.6 | 267.2 | 13.0% | +1.7 | MHI-FY25 chunk 252771; MHI-Q1 chunk 252664 |
| FY2026 forecast | 3,450 → **3,550** (Q1 raise) | 2,200 | 340 | 15.5% | +2.5 forecast | MHI-FY25; MHI-Q1 |
| Q1 FY2026 (Apr–Jun 2026) | 1,359.3 (871.3) | 536.3 (423.2) | 101.3 (56.4) | 18.9% vs 13.3% [computed] | +5.6 year on year | MHI-Q1 chunk 252683; S2 not found |

- **GTCC:** FY25 orders ¥2,652.6bn and revenue ¥992.2bn; FY26 forecast ¥2,300bn / ¥1,100bn [MHI-FY25].
- **GW:** 35 large-frame gas turbines totalling 16 GW sold in FY2025; turbine backlog 32 GW vs 23 GW; 10 large-frame orders in Q1 FY26 [TP-MHI, two corpus copies of one article, **same-origin**].
- **Management on margins:** "original equipment margins at the time of order booking have improved significantly… we expect margin improvements to continue as we steadily execute the backlog" (Nishio, CFO, FY2025 results Q&A) [MHI-QA]. The same idea, with "improving each year for the time being", appears in the MHI Q&A of 2026-05-27 p.2 [facts TP-31].
- **Medium-term plan:** double large-frame capacity from the 2024 level (by about FY2030, per trade press corpus src:244). The FY2026 MTP margin target for Energy Systems was **not found**.

### Q3. Grid equipment

| Segment (metric) | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 guide/forecast | Largest one-year step | Sources |
|---|---|---|---|---|---|---|---|---|
| Eaton Electrical Americas (op. margin) | 20.6% | 22.5% | 26.5% | 30.2% | 29.9% | n/f | **+4.0** (2023) | ETN23; ETN25 (2024 repeated in both at 30.2%) |
| Hubbell Utility Solutions (adj. op. margin) | n/f | 17.2% | 23.9% | 23.5% (HUBB24) / 23.6% (HUBB25, restated) | 24.1% | n/f | **+6.7** (2023; GAAP +6.4, 15.3% → 21.7%) | HUBB23; HUBB24; HUBB25 |
| SE Grid Technologies (profit bef. SI) | — | n/f | n/f | 11% (AR table, rounded) | 15.8% | 18–20% (raised at Q2 from 16–18%); 9M FY26 18.3%; Q3 FY26 19.9% | **~+4.8** (FY25; AR shows "5 p.p.") | SE-AR25; SE-CFO26; SE-Q2P; SE-Q3P |
| Hitachi "Energy" segment (adj. EBITA; includes Power Grids) | — | — | — | ~9.6% [computed] | 12.9% | 13.5% (¥500bn on ¥3,700bn) | ~+3.3 (FY25) | HIT25; HIT25b |
| Schneider (group adj. EBITA; segment not fetched) | — | — | — | 18.6% | 18.7% (+50 bps organic) | +50–80 bps organic target | ~+0.5 organic | SU25R; SU25P (same-publisher) |

- **Hitachi FY24 derivation:** revenue 3,219.9 / 1.23 = ~2,618; EBITA 416.0 − 164.0 = 252.0.
- **Hitachi Energy standalone** (FY22–FY24) and **Schneider Energy Management segment** margins were not found this session.
- **Other SE GT data points:** backlog €51bn; book-to-bill 1.5; backlog margin up 9 pp since FY22 (+6 pp in FY22–24, +3 pp in FY25) [SE-Q3P; SE-CFO26 chunk 251878].
- **Base rate for GEV Electrification's 18–20% → 22% (2028).** That needs about +1.0–2.0 pts a year for 2 years [computed]. Every grid peer except Hubbell 2024 and Eaton 2025 exceeded +1.9 pts in at least one year. Peers also show that after the big price-driven step, margins **plateau**: Eaton 30.2% → 29.9%; Hubbell 23.9% → 23.5% → 24.1%.

### Q4. The lag between order pricing and reported margin, in management's words

| Company | Statement | Lag implied | Sources |
|---|---|---|---|
| SE GS | Backlog-margin gains FY22–25 (+12 new unit / +3 service) vs reported +6.4 pts; lead times "three years or longer"; "higher profitability of the processed order backlog" | About 2–3 years for new units; not stated in quarters | SE-CFO26; SE-IR26; SE-Q1R; src:1699 (single) |
| SE GT / TI | Q4 FY24: margin rose on "higher margin of the processed order backlog year-over-year" | About 1–2 years (GT backlog margin +6 pp FY22–24; reported margin surged in FY25) | SE-Q4FY24; SE-CFO26 |
| MHI | "margins at the time of order booking have improved significantly… as we steadily execute the backlog" | Not quantified | MHI-QA; facts TP-31 |
| Hubbell | 2023: "high single digit" price realisation plus "approximately 10 percentage points of margin expansion from favorable price realization, improved operational productivity and lower material costs" | Same year: short-cycle, book-and-ship | HUBB23 (chunk 105599); S2: HUBB24 shows the 2023 base at 23.9% |
| Eaton EA | 2023 margin up "primarily due to higher sales volumes and net price realization" | Same year | ETN23; S2: ETN25 series |
| GEV (for comparison) | CEO: the 2026 backlog-margin change "tells you the equipment margins for '29 and '30, largely" (Laguna, 2026-09-16) | About 3–4 years | Brief §5; F01 (LAG-PDF p.10 and chunk 246346) |

**Finding:** no competitor gives a lag in quarters.
- Long-cycle heavy-duty gas (SE GS, MHI) implies **about 8–12 quarters**, going by lead times and the FY22→25 conversion. This is a research estimate.
- Short-cycle grid products (Hubbell, Eaton) show **0–4 quarters**.
- Project-heavy grid (SE GT, HVDC) sits in between.

### Q5. Base-rate distribution

The core sample is 17 realised annual steps (§4):

| Statistic | All 17 | 12 direct-only (ex SE TI, ex Schneider) |
|---|---|---|
| Median | **+3.1 pts** | +2.95 pts |
| 75th percentile | **+3.9 pts** | +3.8 pts |
| 90th percentile | +4.3 pts | — |
| Maximum | **+6.7 pts** | +6.7 pts |

Where the GEV steps sit:

| GEV step | Value | Share of peer steps at or below | Percentile |
|---|---|---|---|
| Company, research base (FY27) | +3.3 pts | 9 of 17 | ~53rd |
| Company, consensus (FY27) | +4.4 pts | 15 of 17 | ~88th (only SE GT FY25 and Hubbell 2023 exceed it) |
| Power, research base | +2.5 pts | 7 of 17 | ~41st |
| Power, consensus-implied: 21.7–23.5% (F01) vs FY26 guide midpoint 18% | +3.7 to +5.5 pts | — | 75th percentile to near the maximum |
| Power, FY25 organic | +1.0 pt | — | ~29th |

- **Heavy-duty gas only** (SE GS FY25 +3.5; MHI FY24 +2.6 and FY25 +1.7; FY26 forecasts SE GS about +2 at the guide midpoint and MHI +2.5): the maximum realised step is **+3.5 pts**. Consensus GEV Power at +3.7 to +5.5 would exceed every gas peer year.
- **Company-level caveat:** GEV company steps include mix (Wind loss shrinking about 0.76 pts; Prolec). The one company-level analog, SE group FY25 at +5.0 pts on a wind loss narrowing, shows company steps can exceed segment steps.

### Q6. What could justify a faster GEV step

| Factor | Evidence | Direction |
|---|---|---|
| Wind loss going away | −$400M → ~0 is about 0.76 pts of company margin (F01 / E05). The FY26 Wind guide needs +$257M in H2 (brief §4) | Supports about 0.5–0.8 pts of the +4.4 without any segment step |
| Services mix | Power services share fell 67.9% → 63.1% (brief §3). Company services gross margin fell 35.1% → 31.6% (F01, 10-K / 10-Q) | **Against**: mix has been a headwind, and margin gains came from equipment |
| Slot-reservation economics | SRAs are 54% of GEV's GW vs 27% at SE (facts RQ-16). SRA pricing "10 to 20 points" and ">20%" above backlog (brief §6). But the CEO dates the margin to '29–'30 | Supports price; the timing evidence argues against FY27 |
| Size of price increases | LG&E/KU all-in cost +53–57% (brief §6). Wood Mackenzie sees about $600/kW by end-2027, +195% vs 2019 (corpus src:3846; **SINGLE-SOURCE**, secondary) | Industry-wide, so it also flows to SE and MHI, whose steps are still ≤3.5 |
| Prolec | +$3.1B revenue in the Electrification guide (brief §4). Prolec's margin was not verified this session | Unknown |
| GEV's own record | Electrification +5.3 / +5.9 (GEV10K) beat peers; Power +2.6 / +2.2 reported, only +1.0 organic in FY25 (GEV10K non-GAAP table) | Electrification: GEV can beat base rates. Power: it has not so far |
| Operating leverage | Power incremental margin 44.4% from H1'25 to H1'26 (V07 R6, citing the 10-Q) | Supports acceleration; the peer analog is MHI's Q1 FY26 +5.6 pts |

### Q7. Capacity and pricing behaviour

**Capacity plans**
- **GEV:** 20 GW/yr run-rate from Q3'26, 24 GW in 2028, toward 30 GW by 2030 (brief §3; facts PP-22).
- **SE:** about 35 large-GT manufacturing units, +15 in 2027; medium units 80 → about 100 by 2028; 15–16 GW of deliveries in FY26; 6 GW shipped in Q3 [corpus src:1699 — **SINGLE-SOURCE** trade article of the Q3 call]. SE sold 194 gas turbines in FY25, about 2x FY24 [SE-CFO26 chunk 251877; corpus src:3189 "~200 GTs"].
- **MHI:** double large-frame capacity vs 2024 (trade press corpus src:244; TP-MHI). The CFO said the doubling "does not mean that we are immediately seeking to book twice as many orders as before" (2026-08-06 briefing) [TP-MHI].

**Signs of flattening**
- **Pricing:** none found. SE says new orders still carry higher margins than the backlog (TP-30), and MHI says margins at booking are improving (MHI-QA).
- **Softer signals:**
  1. MHI's FY26 order forecast is ¥3,550bn vs ¥3,936.7bn actual in FY25 (−10%) [MHI-Q1; MHI-FY25].
  2. SE GT book-to-bill is flat at 1.5 [SE-Q3P].
- **Lead times:** no evidence of shortening. SE is at 3+ years (src:1699); GEV is selling 2031–32 slots (V07; corpus src:3846).
- **Capacity vs orders:** Wood Mackenzie puts manufacturing capacity at 60–70 GW against about 110 GW of orders at end-2025 (corpus src:3846 and src:137 — two web pages citing the same Wood Mackenzie figure, **same-origin**).

### Q8. Read-through dates before late January 2027

| Date | Event | What it can tell the team | Source |
|---|---|---|---|
| Late Oct / early Nov 2026 (exact dates not verified) | Hubbell, Eaton, Hitachi and Schneider Q3 | Whether grid margins are plateauing (the Eaton/Hubbell pattern) | Not verified; check IR calendars |
| 2026-10-28 | GEV Q3'26 | After the finals | Brief §4 |
| Early Nov 2026 (not verified) | MHI H1 FY2026 | Whether ES holds 15.5% after Q1's 18.9%; GTCC order run-rate vs the ¥2,300bn forecast | MHI-Q1 (forecast); date not found |
| **2026-11-11 or 11-12** | **SE Q4 FY26, FY27 guidance, "medium-term framework"** | The key peer read. Pass marks: GS FY26 margin vs 14–16% (9M 16.6%); FY27 GS guide step vs FY26 (peer history +2 to +3.5 pts); any FY28 GS target raise above 18–20% | PP-38; SE-FY25D (date conflict) |
| 2027-02-11 | SE Q1 FY27 | After the January GEV call | PP-38 |

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Confidence |
|---|---|---|---|---|---|---|
| 1 | SE GS FY25 margin | 12.95% (1,580 / 12,198) | SE-AR25 §2.4.2 | SE-CFO26 "13.0%" | exact (same-publisher) | H |
| 2 | SE GS FY24 margin | 9.46% | SE-AR25 (profit 1,021, "9%") | SE-CMR24 (revenue 10,796); SE-PR24 "9.5%" | exact | H |
| 3 | SE GS FY22 margin | 6.6% | facts PMX-39 (CMD deck) | — | **SINGLE-SOURCE** | M |
| 4 | SE GS Q3 FY26 | 17.3% vs 13.0%; orders 9,967 | SE-Q3R | SE-Q3P | exact | H |
| 5 | SE GS Q2 FY26 | 15.9% vs 16.1% | SE-Q2P | SE-Q2R | exact | H |
| 6 | SE GS Q1 FY26 | 16.6% vs 14.6%; orders 8,751 | SE-Q1R | SE-Q2P (H1 − Q2) | exact | H |
| 7 | SE GS FY26 guide unchanged at 14–16% | Nov-25 → Q3 | SE-Q2P / SE-Q2R | SE-Q3P | exact | H |
| 8 | SE GS FY28 target raised from 12–14% to 18–20% | Nov-2025 | SE-FY25D | SE-CFO26 | exact | H |
| 9 | GS backlog margin +12 pp new unit / +3 pp service since FY22 | — | SE-CFO26 | SE-IR26 (FY25 +5 / +1) | close | H |
| 10 | SE GT FY25 15.8% vs FY24 11% | ~+4.8 pts | SE-AR25 | SE-CFO26 | close (rounding) | M |
| 11 | MHI ES margins | 8.7 / 11.3 / 13.0 / 15.5 forecast | MHI-FY24 | MHI-FY25; MHI-Q1 | exact (restated series) | M-H |
| 12 | MHI ES Q1 FY26 | 18.9% vs 13.3% [computed] | MHI-Q1 src:3198 | MHI-Q1 src:3197 (same deck) | same-origin | M |
| 13 | MHI on booking margins | quote | MHI-QA | facts TP-31 | close | H |
| 14 | Eaton EA margins | 20.6 / 22.5 / 26.5 / 30.2 / 29.9 | ETN23 | ETN25 | exact (2024–23 overlap) | H |
| 15 | Hubbell Utility adj. margin | 17.2 / 23.9 / 23.5–23.6 / 24.1 | HUBB23 | HUBB24; HUBB25 | **conflict** on 2024 (23.5 vs 23.6; restated adj. op. income 847.5 vs 849.5) | H |
| 16 | Hitachi Energy segment | FY25 12.9%; FY24 ~9.6% [computed] | HIT25 | HIT25b / HIT Q3 outline | close | M |
| 17 | Schneider group adj. EBITA | 18.6% → 18.7% (+50 bps organic) | SU25R | SU25P | exact (same-publisher) | H |
| 18 | GEV Electrification margins | 3.7 / 9.0 / 14.9% | GEV10K segment MD&A | GEV10K organic table (14.9 vs 9.0) | exact (same document) — second publisher: Q4'25 release, not re-read | M-H |
| 19 | GEV Power FY25 organic step | 13.2% → 14.2% (+1.0) | GEV10K non-GAAP table | — | **SINGLE-SOURCE** (not re-checked in the release) | M |
| 20 | MHI capacity-discipline quote | quote | TP-MHI src:345 | src:1743 (news 2026-08-13) | same-origin | M |
| 21 | SE FY26 results date | 11 vs 12 Nov 2026 | facts PP-38 | SE-FY25D | **conflict** | M |

---

## 4. Arithmetic

**A1. Peer one-year steps (pts)**
- SE GS FY25: 12.95 − 9.46 = **+3.5**
- SE GT FY25: 15.8 − 11.0 = **+4.8** (±0.5 from rounding the FY24 figure)
- SE TI (SE-CFO26 chunk 251893: −2.0 / 1.1 / 5.1 / 7.4 / 11.3): **+3.1, +4.0, +2.3, +3.9** [**SINGLE-SOURCE**; the AR shows FY24 7% and FY25 11%, consistent]
- MHI ES: **+2.6, +1.7**
- Hitachi Energy segment: 12.92 − 9.63 = **+3.3**
- Eaton EA: **+1.9, +4.0, +3.7, −0.3**
- Hubbell adj.: **+6.7, −0.4, +0.5**
- Schneider (organic): **+0.5**; I used the reported +0.1 in the sort.

**A2. Distribution**
- Sorted (n = 17): −0.4, −0.3, 0.1, 0.5, 1.7, 1.9, 2.3, 2.6, 3.1, 3.3, 3.5, 3.7, 3.9, 4.0, 4.0, 4.8, 6.7.
- Median = 9th value = 3.1. P75 = 13th value = 3.9. P90 ≈ 4.3. Max = 6.7.
- Direct-only (n = 12): median (2.6 + 3.3) / 2 = 2.95; P75 ≈ 3.78.

**A3. GEV positions**
- Consensus company step: 18.15% − (6,359 / 46,282 = 13.74%) = **+4.41 pts** (MS consensus per the brief).
- Percentiles are counts from A2.

**A4. SE GS conversion check**
- Blended backlog-margin gain = 0.40 × 12 + 0.60 × 3 = **6.6 pp**.
- Reported margin gain FY22→FY25 = 13.0 − 6.6 = **+6.4 pts**.
- Weights are FY25 backlog weights (SE-IR26), which is an approximation.

**A5. GEV Electrification to 2028**
- (22 − 19) / 2 = +1.5 pts a year (range +1.0 to +2.0 across the 18–20% guide).

**A6. MHI Q1 margins**
- 101.3 / 536.3 = 18.9%; 56.4 / 423.2 = 13.3%.

---

## 5. General question bank items answered along the way

- **G2 (has GEV delivered the consensus pace before?).** At company level, yes: FY26 is about +5.3 pts. In Power, no single year has exceeded +2.6 reported or +1.0 organic (FY25). Among gas peers, no year has exceeded +3.5 (§Q5).
- **G11 (physical constraints).** SE lead times are 3+ years and MHI is restraining bookings. Capacity additions arrive in 2027–30 (§Q7), so price-to-margin conversion is lead-time-bound.
- **G12 (when accounting shows results).** SE's reported margin tracked backlog margin with about a 3-year lag (A4). That is consistent with the GEV CEO's '29–'30 statement, not with a front-loaded FY27.
- **G19 (analogies).** Grid peers plateaued after their big step (Eaton 2025 −0.3; Hubbell 2024 −0.4). The step-then-plateau pattern is the base rate for short-cycle price realisation.
- **G21 (what we'd see if the short view were wrong).** SE's FY27 GS guide stepping more than +3.5 pts, or MHI's ES reaching about 18% for the full year. Q1 FY26 was 18.9%.

## 6. What would change these findings

- **The "+4.4 is ~88th percentile" finding** changes if SE guides FY27 GS at ≥ +4.4 pts above its FY26 actual (Nov-2026), or if MHI H1 ES stays above 18%. Either would show gas peers now converting faster than their history.
- **The "lag of ~8–12 quarters" finding** changes if SE or MHI management state explicitly that FY27 absorbs most of the 2025 pricing.
- **The "no pricing flattening" finding** changes on any OEM comment on flat or declining pricing, SRA cancellations, or lead times below 3 years. MHI's lower FY26 order forecast is the watch item.

## 7. Disagreements with the master brief

1. The brief implies a steady climb in Power margin. **Organically, the FY25 Power step was only +1.0 pt** (13.2% → 14.2%) against +2.2 reported; the difference comes from FX and dispositions [GEV10K non-GAAP organic table; single document]. The team should use organic figures when citing the pace.
2. The SE Q4 FY26 date of 2026-11-11 conflicts with 2026-11-12 in SE's own Nov-2025 calendar. Re-verify.
3. Not a contradiction but worth flagging: GEV Electrification's past steps (+5.3, +5.9) are *above* every grid peer except Hubbell 2023. Peer base rates do not argue against the 22% 2028 Electrification target.

## 8. Open items

- **SE GS FY23 profit and margin; SE GT FY22–FY23.** Look in the SE Annual Report 2023/2024 segment tables (§2.4.2) or Q4 FY23 release appendix at assets.siemens-energy.com.
- **MHI ES FY2022; MHI FY2026 MTP segment targets.** Look in the MHI FY2023 results deck and the 2026 MTP deck.
- **Hitachi Energy standalone adj. EBITA** (FY22–FY25) and **Schneider Energy Management segment margins.** Look in Hitachi Energy IR and Schneider FY24/FY25 presentation segment pages.
- **Prolec margin**, which is needed for Q6.
- **Q3 and Q4 2026 reporting dates** for MHI, Hitachi, Eaton, Hubbell and Schneider.
- **A second source** for SE lead times ("three years or longer") and the SE Q3 CFO quote. The SE Q3 FY26 call transcript on the SE IR site would serve.
