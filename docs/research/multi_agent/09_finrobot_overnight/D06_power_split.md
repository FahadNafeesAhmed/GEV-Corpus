# Equipment vs services margin inside Power

_D06_power_split — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 02:21:35. Requests 48, input tokens 4048771, output tokens 41832._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV Power segment: equipment vs services margins (FY23–H1'26), and whether GLJ's ~3 pts on old equipment holds up

## 1. Bottom line

- **GEV's filings pin down the Power services margin better than the earlier work assumed.** Since the ASU 2023-07 segment disclosure, Note 24 gives Power's cost of revenues (excluding D&A), SG&A, R&D and other items. The income statement gives company-wide services gross margin, and Note 24 gives services revenue for Wind and Electrification. Put together, these limit Power's **services EBITDA margin to about 18–32%, central ~22–27%**, in every period from FY23 to H1'26. With a constant services margin, the plausible band is the s=20–29% rows of the old grid, not 15–35%. [S1: FY25 10-K 0001996810-26-000015, Note 24 "SEGMENT EBITDA" tables, p.72] [S2: FY24 10-K 0001996810-25-000011, Note 24, same tables; Q2'26 10-Q 0001996810-26-000148, p.23]
- **Implied Power equipment EBITDA margin, central case: FY23 −27%, FY24 −13.5%, FY25 −4.8%, H1'25 −2.5%, H1'26 +3.6%, Q2'26 about +4%.** Full ranges are in the Q5 grid (FY25 −13% to +3.5%; H1'26 −4% to +11%). Every scenario rises about 25–30 pts from FY23 to H1'26. This is research arithmetic; the team chooses the scenario (computed, Section 4).
- **Management's own history matches a thin-margin equipment book.** In 2020 Strazik (then Gas Power CEO) described Gas Power's roughly $4B equipment business expanding margins "from low single digits to mid-single digits". In January 2026 GEV agreed its Power equipment backlog margin started at YE2022 "approximately breakeven". Neither statement gives a vintage margin level. [S1: UBS conference transcript, 2020-06-03, earningscalls.dev] [S2: GEV Q4'25 webcast transcript, 2026-01-28, gevernova.com]
- **GLJ's "3 pts" is described as "backlog margin", which is GEV's contribution-margin metric, not EBITDA.** On that basis, GEV's slide data put the 2024 order vintage at about 5.5–7.5 pts above an ~breakeven YE22 base, and 2.5–10.5 pts once you allow ±3 pts of uncertainty in the base. **Verdict: plausible as a low-end figure, not proven, and undeterminable as a point estimate.** 3 pts is also exactly GEV's own FY24 year-over-year increment (+3), so GLJ may be reading a change as a level. [S1: Investing.com GLJ summary, 2026-09-14] [S2: GuruFocus/Yahoo, 2026-09-15; GEV 4Q'25 deck slide 5]
- **Peers disclose no equipment/services margin split either.** Siemens Energy Gas Services (66% service, FY25 13.0% margin before special items) says its margin gains come mainly from new-unit backlog. In Q2 FY26 its service ratio fell from 67% to 57% with the margin "on a comparable level", which suggests new-unit margins on processed backlog are now close to the segment average. MHI says GTCC "original equipment margins at the time of order booking have improved significantly". [S1: SE CMD Gas Services deck, Nov 2025, slides 5/14] [S2: SE Annual Report 2025 Note 26; SE pre-close call transcript 2026-06-29; MHI FY2025 results Q&A]
- **The "razor/blade" economics are asserted, not quantified.** The only direct management claim, from the December 2025 investor-update Q&A (speaker not verified), is that "the blade is still more lucrative than the razor in our gas business over the long term, including on an NPV basis." No public source splits unit-sale versus lifetime-service margin. [S1: corpus chunk 246348 (src:2686)] **[SINGLE-SOURCE]** for the quote; the direction is supported by the 2020 Strazik transcript and the GE Q4'23 call.

## 2. Answers

### Q1. What GEV and GE management have said about Power equipment, services and contribution margins

| # | Statement (verbatim, ≤40 words) | Speaker / venue / date | Sources |
|---|---|---|---|
| a | "The starting point would have been about a breakeven." / "directionally the starting point is approximately breakeven." (YE2022 Power equipment backlog margin) | Analyst (Coe) and CFO/CEO, Q4'25 call, 2026-01-28 | [S1: gev_webcast_transcript_01282026.pdf] [S2: research facts PMX-26; deck slide 5 increments +3/+3/+11] |
| b | "we will not begin delivering on the majority of the higher margin orders placed in 2024 and 2025 until 2027 and beyond." | Q4'25 call, 2026-01-28 | [S1: same transcript] [S2: 4Q'25 deck slide 5] |
| c | Slide footnote defines margin expansion as "increase or decrease in the average estimated contribution margin in backlog compared to prior year"; Power +3 (FY23), +3 (FY24), +11 (FY25) | 4Q'25 and 4Q'24 decks | [S1: gev_webcast_presentation_01282026.pdf slide 5] [S2: gev_webcast_presentation_01222025.pdf p.6] |
| d | "in totality, the equipment margin in backlog from '23 to '26, those 4 years will add at least $22 billion in equipment margin" | Strazik, Q4'25 call | [S1: corpus news chunk 246128, 2026-01-23] [S2: corpus web chunk 217531] |
| e | "equipment margin in backlog expanding six points year-over-year, reflecting favorable price and … disciplined underwriting" (company-wide) | CFO Parks, Q4'25 release | [S1: 8-K EX-99 0001996810-26-000012] [S2: corpus web chunk 243264] |
| f | "overall margin and backlog increasing approximately 5 points versus year-end 2023" | Q4'24 call, 2025-01-22 | [S1: gev_webcast_transcript_01222025.pdf] [S2: PMX-45] |
| g | "…improvements in Gas Power equipment profitability" (first time an equipment driver is named) | Q2'24 10-Q MD&A and release | [S1: 10-Q 0001996810-24-000067] [S2: 8-K EX 0001996810-24-000065] |
| h | Q1'24 and Q3'24 MD&A give services-only drivers (e.g. "increase in Gas Power services where volume, price, and productivity more than offset… inflation") | 10-Qs | [S1: 0001996810-24-000008] [S2: 0001996810-24-000083] |
| i | "The positive impact of volume was offset by mix." (Power) | Q3'25 call, 2025-10-22 | [S1: gev_webcast_transcript_10222025.pdf] **[SINGLE-SOURCE]**; the MD&A was not re-checked |
| j | "Growing, more profitable equipment" / "Services strength" (Power segment tagline) | 2025 and 2026 proxies | [S1: DEF 14A 0001996810-25-000049 p.5] [S2: DEF 14A 0001996810-26-000049 p.5] |
| k | SRAs carry "another 10 to 20 points of pricing strength" vs backlog; H1'26 >20% | Q4'25 and Q2'26 calls | [S1: 01282026 transcript] [S2: stocksfoundry.com recap, 2026-01-28] |
| l | Power services orders: "Both are experiencing real margin accretion." (equipment and services backlog) | CFO Parks, Q4'25 call | [S1: 01282026 transcript] [S2: PMX-31] |
| m | "When you look at Gas Power, 70% of the business is services" | Strazik, GE Vernova Investor Day, 2024-03-06 | [S1: 2024-mar-06-scott-strazik-transcript.pdf] [S2: GEV 2024 Investor Day CEO deck, "Power ~$73B backlog (81% services)"] |
| n | "roughly a $4 billion equipment revenue business … expand margins by 200 to 300 basis points from low single digits to mid-single digits." / "delivering mid-single-digit margins this year" (Gas Power equipment backlog, 2020) | Strazik as GE Gas Power CEO, UBS conference, 2020-06-03 | [S1: earningscalls.dev transcript] **[SINGLE-SOURCE]**; the ge.com PDF was not found |
| o | "Profit was over $750 million with low double digit margins driven by services strength. As expected, margins contracted given higher equipment volume." (GE Power Q4'23) | GE Q4'23 call, 2024-01-23 | [S1: roic.ai transcript] **[SINGLE-SOURCE]** |
| p | "the blade is still more lucrative than the razor in our gas business over the long term, including on an NPV basis." | Probably Strazik, Dec-2025 investor-update Q&A (context: "18 gigawatts in the quarter", hyperscalers ~1/3) | [S1: corpus chunk 246348] **[SINGLE-SOURCE]**; the speaker, venue and page were not verified |

**Not found:** no GEV filing, release or deck in the corpus gives a numeric equipment or services margin for Power. The phrases "low single digit", "mid-teens" or "breakeven" appear in GEV sources only as in (a) above. `ask_filings` on the FY25 10-K confirms there is no services-vs-equipment margin comparison in Items 1/1A.

### Q2. Siemens Energy Gas Services

- **Service share:** 66% of revenue in both FY25 and FY24 [S1: SE Annual Report 2025, GS section] [S2: SE CMD Nov-2025 GS deck, slide 14, "34% / 66%"]. The CMD also shows the backlog split as 23% new unit / 77% service, and new-unit orders at about 40% of FY25 orders.
- **Margin (profit before special items):** FY22 6.6%, FY23 9.5%, FY24 9.5%, FY25 13.0%; FY26 guide 14–16%; FY28 target 18–20% [S1: CMD slide 14] [S2: Annual Report 2025 Note 26, EUR1,580M / EUR12,198M]. Q3 FY26: 17.3% (EUR648M / EUR3,756M) [S1: SE Q3 FY26 earnings release, 2026-08-05] [S2: transcriptdaily.com call summary, 2026-08-05].
- **Split by category:** SE gives backlog-margin changes only: "New unit (~40%) +5 pp backlog margin (vs. FY24); Service (~60%) +1 pp" [S1: CMD slide 5]. It does not give new-unit versus service margin levels. The Annual Report attributes the FY25 rise to service volume and "a higher margin from the processed order backlog, especially in the new units business" [S2: AR 2025].
- **Trend signal:** the service ratio went from 67% to 57% in Q2 FY26 with a "comparable margin profile", "mainly driven by… the higher-margin projects we already signed for the new unit business" [S1: SE pre-close call transcript, 2026-06-29, Head of IR (corpus chunk 251706)] [S2: PMX-41]. **Inference:** at SE, new units now being processed earn roughly the segment-average margin; they are not dilutive. SE's new orders are priced at about €400m/GW [CMD slide 5] **[SINGLE-SOURCE]**.
- **Implied SE services margin** (an EBITDA-like proxy of 14.5%, 66% service): 24.5 / 22.0 / 19.4 / 16.8% if new-unit margins are −5 / 0 / +5 / +10% (PMX-44, computed). This is a definition mismatch against GEV segment EBITDA; treat it as a range check only.

### Q3. MHI and Baker Hughes

- **MHI:** GTCC revenue is split about 50% new installations / 50% services; no margin split is given [S1: mhi.com 2025_gtcc_summary.pdf] **[SINGLE-SOURCE]**. In the FY2025 results Q&A, Nishio said: "original equipment margins at the time of order booking have improved significantly… we expect margin improvements to continue as we steadily execute the backlog" [S1: MHI FY2025 results Q&A, corpus chunk 252828] [S2: MHI FY24→25 takeaways, corpus chunk 253075: GTCC "Business profit increased from revenue growth and improved margins"].
- **Baker Hughes IET:** FY25 revenue $13,409M, EBITDA $2,482M (18.5%); Q4'25 20.0% [S1: BKR Q4'25 release, GlobeNewswire 2026-01-25] [S2: BKR Q4'25 call transcript, bullfincher.io]. Gas Tech Equipment and Gas Tech Services revenue are disclosed, margins are not. Direction: "margins improving despite increasing mix headwinds" as GTE backlog converts, meaning equipment is dilutive [S1: BKR Q4'23 call, bullfincher.io, 2024-01-23] **[SINGLE-SOURCE]** for the quote.

### Q4. Historic GE Power disclosure

- GE's segment tables report Power revenue and segment profit only (2018: Power profit −$808M; 2017 $1,947M; 2016 $4,187M), with no equipment/services margin split [S1: GE 2018 10-K, R32.htm, sec.gov] [S2: GE Q3'17 10-Q, R53.htm]. I found no 2015–2019 GE 10-K with a Power equipment vs services margin.
- **Qualitative only:**
  - Q3'17: "lower volume in high margin aero and service businesses and higher volume in low margin grid and balance of plant resulted in a substantial margin headwind" [S1: goodmoat.com GE Q3'17 transcript] **[SINGLE-SOURCE]**; the speaker (probably the CFO) was not verified.
  - 2020 (UBS, Strazik): Gas Power had "negative high single-digit operating margin rates in '18"; the equipment book was going "from low single digits to mid-single digits" in 2020; services were an "$8 billion to $9 billion" business with "very attractive margins" [S1: earningscalls.dev 2020-06-03] **[SINGLE-SOURCE]**.
  - GE 2021 Investor Outlook: Power 2020 revenue $17.6B, 62% services, margin 1.6%, backlog $80B, 78% services [S1: ge_webcast_presentation_03102021.pdf p.1] **[SINGLE-SOURCE]**.
- **Implication:** the pre-boom GE gas equipment book earned low-to-mid single-digit margins (definition not stated). By YE2022 it had fallen back to about breakeven contribution (Q1a). That drop is consistent with 2021–22 inflation, but I have not verified the cause.

### Q5. Solving the Power series

**Method 1 (constant services margin s; reproduced from PMX Grid A, verified):** e = (EBITDA − s × Services) / Equipment.

| Period | s=20% | s=22.5% | s=25% | s=27.5% | s giving e=3% |
|---|---|---|---|---|---|
| FY23 | −11.5% | −16.8% | −22.1% | −27.4% | 13.1% |
| FY24 | −3.8% | −9.2% | −14.7% | −20.1% | 16.9% |
| FY25 | 4.3% | −0.6% | −5.5% | −10.4% | 20.7% |
| H1'25r | 1.8% | −3.4% | −8.6% | −13.8% | 19.4% |
| H1'26 | 13.6% | 9.3% | 5.0% | 0.7% | 26.2% |
| Q2'26 | 16.7% | 12.3% | 7.8% | 3.4% | 27.7% |

The 22.5% and 27.5% columns are my interpolation, computed with the same formula.

**Method 2 (new: anchored in GAAP data).** Power services gross profit (ex-D&A) = consolidated services gross profit + d_s − g_n × non-Power services revenue, where:
- d_s = D&A inside cost of services (not disclosed; grid 200/350/500 for full years, 100/175/250 for halves);
- g_n = the services gross margin of Wind and Electrification (not disclosed; grid 15/25/35%).

Power equipment gross profit = Power segment gross profit (ex-D&A, Note 24) − Power services gross profit. Opex (SG&A + R&D + other segment items) is allocated pro rata to revenue.

| Period | Power GP ex-D&A (margin) | Opex % rev | Services EBITDA margin: central / range | **Equipment EBITDA margin: central / range** | Equipment GP margin (central) |
|---|---|---|---|---|---|
| FY23 | 4,011 (23.0%) | 13.1% | 27.5% / 23.5–31.5% | **−27.4% / −35.8 to −19.0%** | −14.3% |
| FY24 | 4,519 (24.9%) | 12.4% | 24.5% / 20.4–28.5% | **−13.5% / −22.4 to −4.6%** | −1.1% |
| FY25 | 5,140 (26.0%) | 11.3% | 24.6% / 20.4–28.9% | **−4.8% / −13.0 to +3.5%** | 6.5% |
| H1'25r | 2,416 (26.2%) | 12.1% | 22.1% / 18.0–26.2% | **−2.5% / −11.0 to +6.0%** | 9.5% |
| H1'26 | 2,945 (28.2%) | 10.6% | 25.8% / 21.4–30.2% | **+3.6% / −3.9 to +11.1%** | 14.2% |
| Q2'26 | 1,611 (29.4%) | 10.6% | ~24.4% (central only) | **~+4.0%** | ~14.6% |

All cells are research estimates; the team chooses its own number. Each central case reproduces reported segment EBITDA within $4M (Section 4).

- **Opex allocation sensitivity (H1'26 central):** if equipment carries 8% of revenue in opex, e = +6.2% and s = 24.3%; at 15%, e = −0.8% and s = 28.4%. R&D is plausibly equipment-heavy, which would push e lower.
- **Reading the grids:**
  - Both methods agree that implied equipment EBITDA rises about 25–30 pts from FY23 to H1'26, and that the rise happened within the equipment category.
  - In FY25 equipment was probably around or below breakeven at the EBITDA level. Only the corner case with the lowest non-Power services margin gets FY25 above +3.5%.
  - FY23 is distorted by the Steam new-build wind-down, a $118M FX effect and Russia-related charges (PMX-17).

### Q6. Unit sale vs lifetime services ("razor/blade")

- **Direction is well supported, magnitude is not:**
  - Strazik 2020: equipment ~$4B vs services $8–9B; the installed base has "very attractive margins and a dependable cash annuity stream" [UBS 2020-06-03].
  - Strazik, December 2025 (speaker unverified): "blade is still more lucrative than the razor… including on an NPV basis"; services "calories" start 4–5 years after delivery [corpus chunks 246347–8]. The two are from different years and venues but largely the same speaker.
- **Duration:**
  - SE: ~20-year service lifecycle [CMD slide 5]; average LTSA duration 17 years [transcriptdaily, SE Q3 FY26 call, 2026-08-05].
  - GEV CSAs "generally run for 5 to 25 years" [corpus chunk 462461 quoting the GEV 10-K]. I did not re-open the 10-K to confirm.
- **Pricing per GW:** SE new units ~€400m/GW [CMD]. GEV Power equipment revenue per GW shipped is a crude $437M (FY25) to $513M (H1'26) [PMX-09, computed].
- **Not found:** any public NPV or margin split of a unit sale versus its lifetime services. Do not state a ratio.

### Q7. GLJ's ~3 pts on old equipment

**Verdict: undeterminable as a point estimate. Plausible only as a low-end figure on its own contribution basis.** Why:

1. **Basis.** GLJ's wording is "approximately 3 percentage points of backlog margin on the 2027 vintage" [Investing.com 2026-09-14; GuruFocus/Yahoo 2026-09-15]. That is GEV's contribution metric (Q1c), not EBITDA.
2. **As a level on the contribution basis:**
   - The EDF-corrected 2024 vintage is about 7.5 pts above the YE22 base (about 5.5 pts under FIFO), per PMX-29.
   - The base is "approximately breakeven" but not exact. With b = −3 to +3, the 2024 vintage is about 2.5–10.5.
   - 3 pts is inside the envelope only at its low corner (FIFO plus a negative base).
3. **As an increment,** it matches GEV's FY24 +3 exactly. GLJ may be citing the change as a level.
4. **As an EBITDA check:**
   - H1'26 shipments are mostly older vintages (Q1b). They earn a central +3.6% equipment EBITDA (range −3.9% to +11.1%).
   - If the 2024 vintage earned ~3 pts of EBITDA, it would be no better than what ships today, which runs against the +8 pt within-equipment trend from FY25 to H1'26 (central case).
   - It is still possible if price gains are absorbed by cost inflation or tariffs.
5. **What matters for FY27 is the spread and the timing, not the level.** The research has already established that the old-vs-new spread (~12–15 pts) is larger than GLJ's, and that management's timing statements favour GLJ.

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Power FY25 cost of revenues ex-D&A / SG&A / R&D / other | 14,627 / 1,836 / 549 / (147) | FY25 10-K -26-000015 Note 24 p.72 | Reconciles to MD&A EBITDA $2,902 (same doc, p.26) | exact | H |
| 2 | Power FY24 and FY23 same lines | FY24 13,608/2,022/384/(155); FY23 13,425/2,124/315/(149) | FY24 10-K -25-000011 Note 24 | FY25 10-K -26-000015 Note 24 | exact | H |
| 3 | Power H1'26 and H1'25 same lines | H1'26 7,504/918/286/(100); H1'25 6,818/930/242/(59) | Q2'26 10-Q -26-000148 p.23 | EBITDA ties to the Q2'26 release -26-000147 ($1,842/$1,303) | exact (EBITDA only) | H/M |
| 4 | Services revenue by segment FY25 | Power 13,072; Wind 1,858; Electrification 2,168 | FY25 10-K Note 24 | FY24 10-K for FY24/23 comparatives | exact | H |
| 5 | Consolidated services revenue/cost | FY25 17,134/11,774; FY24 15,983/10,861; FY23 14,981/9,716; H1'26 8,729/5,974; H1'25 8,052/5,647 | FY25 10-K p.38; Q2'26 10-Q p.5 | PMX-21 (FY24 10-K p.51) | exact | H |
| 6 | D&A total (upper bound for d_s) | FY25 853; FY24 1,172; FY23 964; H1'26 760; H1'25 406; Power FY25 467 | FY25 10-K Note 24 p.73 | Q2'26 10-Q reconciliation | exact | H |
| 7 | YE22 Power equipment backlog margin ≈ breakeven | ~0 (contribution) | Q4'25 transcript 2026-01-28 | PMX-26 | exact | H |
| 8 | 2020 Gas Power equipment margins LSD → MSD | ~$4B equipment | UBS transcript 2020-06-03 | — | SINGLE | M |
| 9 | SE GS 66% service; margin 13.0% FY25 | — | SE AR 2025 | SE CMD slide 14 | exact | H |
| 10 | SE new-unit backlog margin +5 pp, service +1 pp | — | SE CMD slide 5 | SE AR 2025 driver text (qualitative) | close | M |
| 11 | SE service ratio 67%→57%, margin comparable | Q2 FY26 | SE pre-close call 2026-06-29 | PMX-41 (same doc) | SINGLE | M |
| 12 | MHI GTCC OE margins at booking improved | qualitative | MHI FY2025 Q&A (chunk 252828) | MHI takeaways (chunk 253075) | close | M |
| 13 | BKR IET 18.5% FY25; equipment mix a headwind | — | BKR Q4'25 release | BKR Q4'23/Q4'25 calls | close | M |
| 14 | GLJ "3 pts of backlog margin" | 3 vs 10–11 | Investing.com 2026-09-14 | GuruFocus/Yahoo 2026-09-15 (likely the same wire) | exact | M |
| 15 | Razor/blade NPV quote | — | corpus chunk 246348 | — | SINGLE | L/M |
| 16 | GE 2020 Power revenue $17.6B, 62% services, 1.6% margin | — | GE Investor Outlook 2021 deck | — | SINGLE | M |

## 4. Arithmetic

**Power segment gross profit ex-D&A** = segment revenue − cost of revenues (Note 24). For FY25: 19,767 − 14,627 = 5,140 (26.0%).

**Opex** = SG&A + R&D + other items. For FY25: 1,836 + 549 − 147 = 2,238 (11.32%). Check: 5,140 − 2,238 = 2,902 = reported EBITDA ✓.
- Other periods: FY24 2,251 (12.42%); FY23 2,290 (13.13%); H1'26 1,104 (10.57%); H1'25 1,113 (12.05%); Q2'26 472 + 154 − 45 = 581 (10.6%).

**Consolidated services gross profit (incl. D&A):** FY25 5,360; FY24 5,122; FY23 5,265; H1'26 2,755; H1'25 2,405; Q2'26 1,515.

**Non-Power services revenue (Note 24):** FY25 4,026; FY24 3,565; FY23 3,221; H1'26 2,122; H1'25 1,801; Q2'26 1,128.

**Power services GP = consolidated services GP + d_s − g_n × non-Power services revenue.** Unallocated "other" services revenue (36/14) is ignored.

- **FY25 central** (d = 350, g = 25%): 5,360 + 350 − 1,006.5 = 4,703.5 → x = 35.96% of 13,081 → s = 35.96 − 11.32 = 24.64%.
  - Equipment GP = 5,140 − 4,703.5 = 436.5 → 6.53% of 6,686 → e = −4.79%.
  - Tie-out: 0.2464 × 13,081 − 0.0479 × 6,686 = 2,903 ✓.
  - FY25 corners (equipment GP margin): d200: 2.8 / 8.8 / 14.8% for g_n 15 / 25 / 35%; d350: 0.5 / 6.5 / 12.5%; d500: −1.7 / 4.3 / 10.3%. Subtract 11.32 for EBITDA.
- **H1'26 central** (d = 175, g = 25%): 2,755 + 175 − 530.5 = 2,399.5 → x = 36.37% → s = 25.80%.
  - Equipment GP 545.5 / 3,851 = 14.17% → e = 3.60%.
  - Tie-out: 1,702 + 139 = 1,841 ✓.
  - Corners: equipment EBITDA from 0.0 / 5.6 / 11.1% (d100) to −3.9 / 1.7 / 7.2% (d250).
- **FY24 central:** 5,122 + 350 − 891.25 = 4,580.75 → s = 24.47%; equipment GP −61.75 → e = −13.50%. Tie-out 2,268 ✓.
- **FY23 central:** 5,265 + 350 − 805.25 = 4,809.75 → s = 27.50%; equipment GP −798.75 → e = −27.40%. Tie-out 1,721 ✓.
- **H1'25 central:** 2,405 + 175 − 450.25 = 2,129.75 → s = 22.09%; equipment 286.25 → e = −2.50%. Tie-out 1,303 ✓.
- **Q2'26 central** (d = 90): 1,515 + 90 − 282 = 1,323; equipment 1,611 − 1,323 = 288 / 1,965 = 14.7% → e ≈ 4.0%.

**GLJ contribution envelope:** from PMX-29, v24 = (12,461 × 6 − 4,220 × 3) / 8,241 ≈ 7.5 pts above the base (FIFO ≈ 5.5). With the base b ∈ [−3, +3], the range is 2.5–10.5.

## 5. General question bank items answered along the way

- **G2:** Street FY27 Power ~20.7% (GLJ-sourced). The GAAP-anchored split says H1'26 equipment is about +4% EBITDA (central) and services about 26%. Reaching ~21% segment margin with equipment at ~40% of revenue needs equipment EBITDA of about 14% at s = 26% (computed: (0.207 − 0.6 × 0.26) / 0.4 = 12.75%; about 14% if s = 25%). That is roughly +9–10 pts more within-equipment gain in about 18 months, versus about +8 pts FY25→H1'26 (central). A similar pace has happened before, so this is not unprecedented.
- **G12:** Deposits and percentage-of-completion revenue timing are unaffected by this split. The segment cost excludes D&A, so the equipment/services split lives in cost of revenues only.
- **G19:** The GE gas equipment book ran low/mid single-digit margins in 2019–20, and "negative high single-digit" segment operating margins in 2018 (Strazik, 2020). Thin equipment margins are the historical norm outside booms.
- **G20:** Definition traps:
  - "backlog margin" (contribution, average of the whole book) vs segment EBITDA;
  - GEV segment EBITDA vs SE profit before special items;
  - Note 24 external revenue (6,420) vs MD&A equipment including intersegment (6,686).
- **G21:** If equipment were flat and services drove the gains, the company services gross margin would have needed to rise about 7–10 pts. It rose only +1.7 pts from H1'25 to H1'26 and fell from FY23 to FY25 (PMX-21/35). That points against services as the driver.

## 6. What would change these findings

- Any disclosure of Wind or Electrification services margins, or of D&A inside cost of services, would narrow Method 2. A Wind services margin below 15% pushes Power services up and equipment down.
- A GEV statement quantifying Gas Power equipment EBITDA or contribution margin (the January 2027 call or the spring-2027 Capital Markets Day) would supersede everything above.
- GLJ's full note defining "backlog margin" as EBITDA, or as a level rather than an increment, would change the Q7 framing.
- A Q3'26 Power margin of 17% or less with equipment-led revenue growth, or services-only MD&A drivers, would argue for a lower equipment margin.
- A Q3'26 margin of 18% or more on revenue growth of +17% or more would argue for a higher one.

## 7. Where I disagree with the master brief

1. "GEV does not disclose equipment vs services margins inside Power" is true, but **Note 24 (ASU 2023-07) gives enough cost data to bound the split.** Combined with the consolidated services gross margin, it limits services EBITDA to about 18–32% rather than leaving it a free assumption.
2. The brief treats GLJ's "3 pts" as a margin on old equipment. **GLJ calls it "backlog margin"**, so it should be tested against contribution-margin vintages, not EBITDA, and it is plausible at the low end of that range.
3. PMX Grid A's footnote "Steam moved out" is wrong: Steam was realigned within Power (the verifier already flagged this).

## 8. Open items

- **d_s and the non-Power services margin:** look for a DISE (ASU 2024-03) early adoption, or for any Wind/Electrification services margin commentary in the Dec-2024 and Dec-2025 investor decks, which the corpus search did not reach.
- **The 2020 UBS quote:** find a second copy (ge.com transcript PDF) and confirm which margin definition Strazik meant.
- **The razor/NPV quote:** confirm the speaker and page. The inpayvantage.com Dec-2025 transcript is a candidate; I did not read it all.
- **GLJ's full note:** its definition of "backlog margin" and its FY27 Power build.
- **Other definitions:** GE 10-K statements of the gas equipment margin before 2018; SE new-unit margin levels (not disclosed); MHI GTCC split (not disclosed).
- **Q3'26 10-Q (2026-10-28, after the finals):** re-run Method 2 with the new Note 24 lines.
