# Bottom-up FY27/FY28 adjusted EBITDA by segment (pass A)

_D01_fy27_build_A — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 00:49:09. Requests 1, input tokens 114482, output tokens 16004 (salvaged: research reused, answer rewritten)._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova (GEV): bottom-up FY27 and FY28 adjusted EBITDA by segment, as of 2026-09-30

Every range below is a **research estimate. The team chooses its own number.**

**Source key**
- **10Q-2Q26** = 10-Q 0001996810-26-000148 (2026-07-22)
- **10Q-1Q26** = -26-000064
- **10Q-3Q25** = -25-000160
- **10Q-2Q25** = -25-000133
- **10Q-1Q25** = -25-000073
- **10Q-3Q24** = -24-000083
- **10Q-2Q24** = -24-000067
- **10Q-1Q24** = -24-000008
- **10K-25** = 10-K 0001996810-26-000015
- **10K-24** = -25-000011
- **REL-2Q26** = 8-K -26-000147 press release
- **REL-4Q25** = 8-K -26-000012 press release
- **CALL-2Q26** = Q2'26 call transcript, 2026-07-22 (corpus src:3161)
- **CALL-4Q25** = Q4'25 call transcript, 2026-01-28 (corpus src:2660)
- **WEB-UD** = trade-press copies of the Q4'25 quote (corpus src:149 and src:293)
- **LAGUNA** = GEV's own Morgan Stanley Laguna transcript PDF, 2026-09-16
- **MB-LAG** = MarketBeat write-up of Laguna, 2026-09-18 (corpus src:681)
- **DEC25** = December 2025 investor-update press release (gev_webcast_pressrelease_12092025.pdf; corpus src:2648)
- **PRO-DECK** = GEV's Prolec deal deck (corpus src:3788)
- **PRO-NEWS** = news article on the Prolec deal (corpus src:3812)
- **SE-Q3** = Siemens Energy Q3 FY26 earnings release, 2026-08-05 (siemens-energy.com)
- **SE-TR** = Siemens Energy Q3 FY26 transcripts (stockanalysis.com / transcriptdaily, 2026-08-05)
- **BKR-Q2** = Baker Hughes Q2'26 release (nasdaq.com, 2026-07-26) and the stocktitan 8-K summary
- **MHI** = MHI Q&A and presentation (corpus src:3203; MarketScreener, 2026-05-18)
- **MS** = MarketScreener consensus, fetched 2026-09-29
- **FACTS-xx** = prior verified fact table (facts.csv)

---

## 1. Bottom line

- **FY27 adjusted EBITDA range: $7.7B–$9.6B (base ~$8.7B, 16.7% margin).** That is a statistical band combining each segment's low/high swing (root-sum-square). If every segment lands low or high at once, the extremes are $7.0B and $10.1B.
  - Consensus of $9,574M [MS; FACTS CT-02] sits at the top of the band.
  - For consensus to hold, Power needs ~21.5–23.5% and Electrification ~21–22% **in 2027**. That is close to the 2028 targets of 22%/22% [REL-4Q25; DEC25].
- **FY28 range: $9.7B–$12.6B (base ~$11.2B, 19.2%).** Corners are $8.8B–$13.3B.
  - The base matches management's framework ($11.2B = 20% × $56B) [REL-4Q25; DEC25].
  - Consensus of $13,064M is above the statistical high. It needs Power and Electrification together at ~24.4% on consensus revenue, about 2.4 points above both 2028 targets.
- **Power margin is the biggest driver.** 1 point of Power margin in FY27 ≈ $275M; the 18.5%→21.5% range is worth ~$825M.
  - The trend cuts against an easy short. Power margin rose +2.6 pts in FY24, +2.2 in FY25 and ~+3.3 in FY26 (guide mid) [10K-24; 10K-25; REL-2Q26]. Another +2.5 pts reaches ~20.5% in FY27.
  - The 2028 target of 22% implies the pace slows to ~+2 pts over two years. Either management is conservative or the Street is early.
- **Power services are not a smooth compounder.**
  - Revenue from contractual service agreements (CSAs) was flat to down: $5,473M in FY24, $5,412M in FY25, $2,720M in H1'25 and $2,689M in H1'26 [10K-24 Note; 10K-25 Note 9; 10Q-2Q25; 10Q-2Q26 Note 9].
  - Revisions to CSA profitability were negative in every period. H1'26 (−$218M) already exceeds all of FY25 (−$151M).
  - Services growth of ~5–6% comes from non-CSA work (transactional, nuclear, upgrades), which grew ~10–11%.
- **Shipments lag the "20 GW" run-rate.**
  - Gas shipments ran 1.5–5.2 GW a quarter from Q1'24 to Q2'26, and H1'26 (7.5 GW) was below H1'25 (8.2 GW) [10Q-2Q26; 10Q-2Q25].
  - The CEO said GEV will ship "at least 30 gigawatts" over the six quarters Q3'26–Q4'27 [CALL-2Q26], and gave the cadence of 5 GW a quarter, rising to 6 in H2'27 [LAGUNA; FACTS PP-22]. That implies ~20–22 GW in 2027.
- **Wind is the second-largest swing in FY27, with the weakest guidance record.**
  - The FY26 guide of about −$400M needs +$257M in H2 [FACTS RQ-10].
  - The CEO expects Wind to be "materially better in 2027 than in 2026" [MB-LAG; LAGUNA].
  - Wind missed its FY24 and FY25 guides, and its 2028 margin target was cut from 10% to 6% [DEC25; FACTS BR-11].

---

## 2. Answers to the questions

### Q1. Gas-turbine shipments by quarter, and realistic 2027 GW

Each quarter's figure appears in two documents: that quarter's 10-Q and the next year's 10-Q, which repeats it as the comparative. Q4 is derived as the full year minus nine months.

| Qtr | GW | Units | Heavy-duty | HA | Aero | Sources |
|---|---|---|---|---|---|---|
| Q1'24 | 2.3 | 17 | 10 | 1 | 7 | 10Q-1Q24; 10Q-1Q25 |
| Q2'24 | 1.5 | 15 | 8 | 1 | 7 | 10Q-2Q24; 10Q-2Q25 |
| Q3'24 | 3.3 | 18 | 13 | 5 | 5 | 10Q-3Q24; 10Q-3Q25 |
| Q4'24* | 4.8 | 25 | 17 | 8 | 8 | 10K-24 or 10K-25 minus 10Q-3Q25 (9M) |
| Q1'25 | 3.0 | 19 | 12 | 5 | 7 | 10Q-1Q25; 10Q-1Q26 |
| Q2'25 | 5.2 | 21 | 18 | 8 | 3 | 10Q-2Q25; 10Q-2Q26 |
| Q3'25 | 4.0 | 20 | 14 | 6 | 6 | 10Q-3Q25 [S2 missing: Q3'26 10-Q not filed] |
| Q4'25* | 3.1 | 21 | 10 | 5 | 11 | 10K-25 (FY 15.3/81/54/24/27) minus 10Q-3Q25 (9M 12.2/60/44/19/16) |
| Q1'26 | 4.2 | 25 | 15 | 5 | 10 | 10Q-1Q26; 10Q-2Q26 (H1 minus Q2) |
| Q2'26 | 3.3 | 29 | 13 | 3 | 16 | 10Q-2Q26; CALL-2Q26 ("we shipped three gigawatts"; "29 gas turbines… including 16 aeroderivatives") |

*Derived. Full years tie: FY24 = 11.9 GW and FY25 = 15.3 GW [10K-25].

**2027 GW — research estimate: low 19 / base 21 / high 22.5.**
- "At least 30 GW" over Q3'26–Q4'27 [CALL-2Q26], less H2'26 at ~5 GW a quarter, leaves ≥~20 GW for 2027.
- The quarterly cadence (5 GW a quarter into early 2027, 6 a quarter sometime in H2'27) gives 21–22 GW [LAGUNA p.4; FACTS PP-22].
- 2028 is set at 24 GW [REL-2Q26; CALL-2Q26].
- The low case reflects history: shipments have come in below capacity, and Q2'26 was only 3.3 GW.

### Q2. Realised price per kW in the backlog, and SRA pricing

No gas-only $/kW is disclosed. Two proxies, both upper-bounded because Power equipment also includes nuclear, hydro and steam:

- **Power equipment RPO ÷ firm gas backlog GW:** Q3'25 $575, Q4'25 $618, Q1'26 $648, Q2'26 $741 per kW, i.e. +29% in three quarters [FACTS RV-25, built from the RPO tables in 10K-25 / 10Q-2Q26 and GW from REL-2Q26].
- **Power equipment revenue ÷ gas GW shipped:** FY24 $480/kW (5,708/11.9), FY25 $437 (6,686/15.3), H1'26 $511 (3,834/7.5) [10K-25 segment table; 10Q-2Q26 segment note]. H1'26 is flattered by an aero-heavy mix.
- **New slot reservation agreement (SRA) pricing vs backlog:** "another 10 to 20 points of pricing strength" [CALL-4Q25]. H1'26 orders were priced ">20%" above 4Q'25 orders, which is not like-for-like because of aero and combined-cycle mix [CALL-2Q26; FACTS PMX-30].
- **Independent checks:**
  - LG&E/KU, same site, GE 7HA: all-in plant cost rose +53–57% between April 2024 and June 2026, including escalation [KY PSC Case 2025-00045; FACTS TP-05].
  - LG&E/KU market indications for a combined-cycle plant without a reservation: $2,800/kW (May) to $3,000–3,200/kW (July) [KY PSC Case 2025-00313; FACTS TP-12].
  - Siemens Energy's CFO: orders are "still coming in at higher margins than older backlog" [FACTS TP-30].

### Q3. Vintage share of 2027 Power equipment revenue: dollars vs GW

- **By dollars** (prior verified work, RPO-curve method): pre-2025 orders 8–20%, 2025 orders 47–62%, 2026+ orders 29–35% [FACTS GLJ-21 with the vintage model; 10K-25 RPO note].
- **By GW — computed, first-in-first-out (FIFO) bound:**
  - Firm backlog at 6/30/26 = 53 GW [REL-2Q26; CALL-2Q26].
  - Implied YE25 backlog = 53 − 20.1 (H1'26 orders) + 7.5 (H1'26 shipments) ≈ 40.4 GW.
  - Implied YE24 backlog = 40.4 − 29.8 (FY25 orders) + 15.3 (FY25 shipments) ≈ 25.9 GW.
  - Order and sales GW come from 10K-25 and 10Q-2Q26. These backlog figures are derived and ignore cancellations and conversions.
  - Shipments from 1/1/25 through YE26 ≈ 15.3 + 7.5 + ~10 = ~32.8 GW, which exceeds the 25.9 GW pre-2025 backlog. So under strict FIFO the **pre-2025 GW share of 2027 is ~0%**, and 2025-vintage orders (29.8 GW) fill essentially all of 2027.
  - Under management's own description, 2024–25 high-margin orders deliver "'27 and beyond" [CALL-4Q25; WEB-UD]. That points to non-FIFO slotting, with aero shipping fast and HA units waiting for their slots. A plausible pre-2025 GW share is **0–25%**, but it cannot be computed from disclosures.
- **Why the two views differ:**
  - Dollars include nuclear, hydro and steam; GW is gas only.
  - 2025 orders are priced higher per kW, so their dollar share exceeds their GW share.
  - Revenue on long projects may be recognised over time, before shipment; the over-time vs point-in-time split is not disclosed.
  - HA units ordered in 2023–24 (33) roughly equal HA units sold in FY25 plus H1'26 (32) [10K-25; 10Q-2Q26]. But the HA backlog at YE22 is unknown, so HA-level FIFO cannot be closed.

### Q4. What Power services growth is made of

| | FY23 | FY24 | FY25 | H1'25 | H1'26 |
|---|---|---|---|---|---|
| Power services revenue ($M) | 11,838 | 12,419 (+4.9%) | 13,081 (+5.3%) | 6,232 | 6,593 (+5.8%) |
| CSA revenue ($M) | n/a | 5,473 | 5,412 (−1.1%) | 2,720 | 2,689 (−1.1%) |
| Services excluding CSA ($M) | n/a | 6,946 | 7,669 (+10.4%) | 3,512 | 3,904 (+11.2%) |
| Net unfavourable CSA profitability revisions ($M) | n/a | −319 ("due primarily to higher costs") | −151 | −42 | −218 |

- Sources: Power services revenue from the 10K-24, 10K-25 and 10Q-2Q26 segment tables. CSA revenue and revisions from the contract-assets notes in 10K-24, 10K-25 Note 9, 10Q-2Q25 and 10Q-2Q26 Note 9. CSA assets are 100% in Power [10Q-2Q26 Note 9].
- The split between installed base, price, upgrades and outages is not disclosed. The stated drivers are "Nuclear Power and Gas Power from higher volume and favorable pricing" [10Q-2Q26 MD&A] and, in 2024, "higher outages and transactional service volume" [10Q-2Q24; 10Q-3Q24].
- Power services orders grew +12% in Q2'26 [CALL-2Q26]. Company organic services revenue grew +10% in Q2'26 [10Q-2Q26].
- The CFO expects "incremental pricing" on new service contracts [CALL-4Q25; FACTS PMX-31].

### Q5. Equipment/services margin pairs consistent with Power's 17.63% in H1'26

Inputs from 10Q-2Q26: equipment $3,834M, services $6,593M, EBITDA $1,842M. Formula: e = (1,842 − s × 6,593) / 3,834.

| Services margin s | 18% | 20% | 22% | 24% | 26% | 27.9% |
|---|---|---|---|---|---|---|
| Implied equipment margin e | 17.1% | 13.6% | 10.2% | 6.8% | 3.3% | 0% |

Peer anchors:
- Siemens Energy Gas Services: FY25 profit before special items 13.0% (~14.5% as an EBITDA proxy) [FACTS PMX-36]; FY26 guide 14–16% [SE-Q3]. Its implied services margin is 19.4–24.5% if new-unit margins are +5% to −5% [FACTS PMX-44].
- Baker Hughes Industrial & Energy Technology (IET): EBITDA margin 20.6% in Q2'26 (mixed equipment and services) [BKR-Q2].
- MHI Energy Systems: business profit 13% in FY25, 15.5% forecast for FY26 (after D&A) [MHI src:3203; MHI Q&A says margin improvement is driven by gas-turbine combined cycle].
- GEV company-level GAAP services gross margin was 31.6% in H1'26 before SG&A and R&D [FACTS PMX-21]. Power SG&A plus R&D runs at 11.5% of revenue [10Q-2Q26].

**Plausible band (research estimate): services 20–24%, equipment 7–14%.** At the same s = 22%, FY25 equipment margin ≈ 0.4%. Equipment margin therefore rose about 10 points in roughly a year.

### Q6. Operating leverage from ~15 GW to 20–24 GW

- **Power costs, H1'25 → H1'26** [10Q-2Q26 segment note, both periods]:
  - Cost of revenues fell from 73.8% to 71.8% of revenue (6,818/9,234 → 7,504/10,449): +2.0 pts.
  - SG&A plus R&D went from 1,172 (12.7%) to 1,204 (11.5%) while revenue grew +13.2%: +1.2 pts.
  - Other items (equity income) added ~+0.3 pts.
  - The organic margin gain was +4.1 pts [FACTS PMX-19].
- **FY27 opex leverage (computed):** if Power SG&A plus R&D grows ~6% against revenue growth of ~16%, the opex ratio falls from ~10.4% to ~9.5%, adding ~+0.9 pts from opex alone.
- **Management's wording** (Power section of CALL-2Q26): margins expanded on "favorable price and higher volume, more than offsetting inflation, as well as additional expenses to support capacity investments at Gas". On Q3: "volume, price and productivity should more than offset inflation" [CALL-2Q26; REL-2Q26].
- A GW-to-margin leverage figure has not been quantified by management [not found in CALL-2Q26, CALL-4Q25, LAGUNA].

### Q7. Cost headwinds and contract terms

- **Fixed price** [10K-25 Item 1A; 10K-24 Item 1]: "We enter into contracts that commit to a fixed price well before project completion." The 10-K lists "inflation, labor and material cost increases" and "liquidated or other damages" as risks.
- **Liquidated damages** are estimated inside variable consideration, using "specified liquidated damages rates" [10K-25 Item 8; 10K-24 Item 8]. The amounts are not disclosed.
- **Tariffs:** the 2026 estimate is $100–200M, down from $250–350M at Q1; the FY25 actual was ~$250M [10Q-2Q26 MD&A; FACTS RQ-01].
- **Wind tariffs:** H1'26 onshore volume "had fewer contractual protections for tariffs since we signed these orders before their implementation" [CALL-2Q26]. This implies newer contracts carry tariff protection (single-source for that inference).
- **Firm pricing at reservation:** a customer paid a $25M reservation partly "to lock in firm pricing for the equipment" [KY PSC Order, 2025-10-28; FACTS VF-03].
- **Escalation clauses in gas contracts: not found** in filings or transcripts searched [SINGLE-SOURCE gap].
- **CSA cost overruns:** FY24 −$319M "due primarily to higher costs"; H1'26 −$218M [10K-24; 10Q-2Q26].

### Q8. Electrification drivers, Prolec margin, 2027 margin path

- **Q2'26 revenue by business unit** (Q2'25 → Q2'26, $M, 10Q-2Q26):

  | Unit | Q2'25 | Q2'26 | Growth |
  |---|---|---|---|
  | Power Transmission (incl. Prolec ~$900M) | 759 | 1,877 | ~+29% ex-Prolec |
  | Grid Systems Integration (substations, HVDC) | 579 | 806 | +39% |
  | Power Conversion & Storage | 411 | 539 | +31% |
  | Grid Automation & Software | 412 | 416 | +1% |

  Whole segment: organic +29%, reported +68%. Backlog is $41B (+69%). Air-insulated switchgear is ~$5B of backlog [CALL-2Q26].
- **Prolec economics:**
  - Purchase price $5.275B; 13.9x 2025E and 9.4x 2028E adjusted EBITDA on a $10.6B EV. That implies ~$763M of 2025E EBITDA on ~$3B revenue (~25%) and ~$1,128M in 2028E.
  - Cost synergies of $60–120M by 2028 [PRO-DECK; PRO-NEWS: "~$3 billion in revenue… adjusted EBITDA margin of approximately 25%"].
  - The deal closed 2026-02-02, with ~$3.1B of Prolec revenue expected in FY26 [10Q-2Q26 Note 8; REL-2Q26].
- **Margin path:**
  - FY24 9.0% → FY25 14.9% [10K-25].
  - H1'26 18.2%, Q2'26 18.4% [10Q-2Q26; CALL-2Q26].
  - Q3'26 guide: "modestly above 18.4%" [CALL-2Q26].
  - FY26 guide 18–20%; 2028 target 22% [REL-2Q26; REL-4Q25].
  - Backlog margin rose +3 pts in FY25; 2026 is expected "similar… maybe a little bit larger" [LAGUNA; FACTS POS-17].
  - Peer anchor: Siemens Energy Grid Technologies FY26 guide is 18–20% profit before special items [SE-Q3].
- **FY27 research estimate:** low 19% / base 20.5% / high 22%.

### Q9. Wind: when losses stop, and what is left offshore

- **Segment EBITDA history:** FY23 −$1,033M, FY24 −$588M, FY25 −$598M [10K-25]; H1'26 −$657M (Q2 −$275M) [10Q-2Q26; CALL-2Q26].
- **Near-term guide:** Q3'26 "approximately break-even"; FY26 about −$400M [CALL-2Q26; REL-2Q26].
- **2027:** the CEO expects Wind profitability to be "materially better in 2027 than in 2026" [MB-LAG; LAGUNA]. 2028 target margin is 6%, down from 10% [DEC25; FACTS BR-11].
- **Offshore:**
  - Vineyard Wind installation was completed in Q1'26 [10Q-2Q26]. Litigation was settled 2026-09-16 on confidential terms [FACTS RQ-11: GEV release; Boston Globe].
  - Dogger Bank B is being installed [CALL-2Q26].
  - Offshore RPO is falling as contracts are executed [10Q-2Q26]. The remaining offshore loss exposure is **not quantified** in any source found.
- **Onshore:** ~60% of equipment RPO is in the US, and Q2 orders fell −40% [10K-25; REL-2Q26].
- **FY27 research estimate:** −$300M / $0 / +$250M.

### Q10. Corporate costs and the segment-to-adjusted-EBITDA reconciliation

| Period | Segment EBITDA ($M) | Corporate & other ($M) | Adjusted EBITDA ($M) |
|---|---|---|---|
| FY25 | 3,737 | −541 | 3,196 |
| FY24 | 2,358 | −323 | 2,035 |
| H1'26 | 2,384 | −239 | 2,146 (2,145 by addition; rounding) |
| Q2'26 | 1,427 | −177 | 1,250 |

- Sources: 10K-25 segment note and MD&A table; 10Q-2Q26 reconciliation and MD&A.
- FY26 corporate guide is $450–500M, which implies −$211M to −$261M in H2 [CALL-2Q26; FACTS evidence brief].
- **What adjusted EBITDA excludes:** restructuring, separation costs (FY25 −$180M, H1'26 −$61M, including a one-time option grant), gains or losses on business interests, D&A, non-operating benefit income, and net interest. Financial Services interest and tax are included [10K-25; 10Q-2Q26].
- Recurring stock-based compensation ($257M in FY25) is not added back [10K-25 equity statement; FACTS RV-35].
- **FY27 research estimate:** −$550M / −$475M / −$425M.

### Q11. What each segment must earn for FY27 consensus of $9,574M

Required segment EBITDA = 9,574 + ~475 corporate = **~$10,049M**. On base revenues (Power $27.5B, Electrification $17.5B):
- (a) Electrification 20.5% ($3.58B) and Wind $0 → Power needs $6.47B = **23.5%**, above the 2028 target.
- (b) Electrification 22% ($3.84B) and Wind +$250M → Power needs **21.7%**.
- (c) Power at 20.7% (GLJ's quoted "consensus Power margin" [FACTS GLJ-04]) on ~$28.5B = $5.9B → Electrification plus Wind need ~$4.15B, e.g. Electrification 22% on $18B plus Wind +$0.19B.

**Who carries the FY26→FY27 jump:** consensus rises +$3,215M (6,359 → 9,574). Under (c), Power contributes ~+$1.65B (~51%), Electrification ~+$1.16B and Wind ~+$0.59B.

### Q12. What management has said about 2027 margins and timing

- Strazik, Q4'25 call, 2026-01-28: "we will not begin delivering on the majority of the higher-margin orders placed in '24 and '25 until '27 and beyond." [CALL-4Q25; WEB-UD src:149/293]
- Strazik, Laguna, 2026-09-16, p.10: "…that really tells you the equipment margins for '29 and '30, largely." Also p.5–6: "that's most of when that equipment delivers." [LAGUNA; FACTS VF-02/PP-06]
- Q2'26 call, 2026-07-22, on Power: "favorable price and higher volume, more than offsetting inflation." [CALL-2Q26; REL-2Q26]
- Q4'25 call: "In Wind, we expect relatively stable margins this year." [CALL-4Q25]
- There is **no FY27 margin guidance.** The FY27 outlook comes on the January 2027 call [LAGUNA; MB-LAG].

### Q13. Largest swing per unit of uncertainty

- **Power segment margin:** $275M per point; $825M over the range.
- Within Power: 1 point of equipment margin ≈ $127M (on ~$12.7B); 1 point of services margin ≈ $148M (on ~$14.8B).
- **Wind** has the largest swing relative to its size ($550M on ~$7.7B revenue) and the poorest guidance record.

### Q14. FY28: framework ($11.2B) vs consensus ($13.1B)

- **The framework rebuilds from its own components** [DEC25 segment table]:
  - Power and Electrification: "high-teens organic CAGR" from 2025; Wind: "down low-double-digit" CAGR.
  - At 17%: Power 19,873 × 1.17³ ≈ $31.8B; Electrification (9,589 × 1.17³) + ~$4.0B Prolec ≈ $19.4B; Wind 9,110 × 0.89³ ≈ $6.4B.
  - At 22% / 22% / 6% less ~$450M corporate: EBITDA ≈ **$11.2B**. Revenue comes to ~$57B vs the $56B stated, so the fit is slightly loose.
- **What consensus needs:** $13,564M of segment EBITDA.
  - At consensus revenue of $60.5B with Wind ~$7B, Power plus Electrification (~$54B) need **~24.4%** blended.
  - Alternatively, at 22% margins they need ~$59.8B of revenue, about 17% above the framework.
- **Precedent:** management raised the 2028 Power target from 16% to 22% within one year [DEC25; FACTS BR-13]. A similar December or CMD raise would close the gap. No December 2026 event is listed [FACTS BR-44]; the CMD is planned for spring 2027 [LAGUNA].

### Q15. Three hand-checkable tests

1. **Reconciliation tie-out.** In the 10Q-2Q26 segment note, check segments − corporate = adjusted EBITDA (2,384 − 239 = 2,145 ≈ 2,146). Then plug the FY26 guide: Power 18–20% growth at 17–19%, Electrification $14.5–15.0B at 18–20%, Wind −$400M, corporate $450–500M. That gives ~$6.0–6.4B.
2. **Equipment/services margin grid.** Use the 10Q-2Q26 segment-note split (equipment 3,834 / services 6,593 / EBITDA 1,842) and run e = (EBITDA − s·S)/E across s = 18–26%. Repeat for FY25 from 10K-25. Compare with Siemens Energy [SE-Q3] and Baker Hughes IET [BKR-Q2].
3. **RPO and GW check on FY27 equipment revenue.**
   - From the YE25 book: equipment RPO $64,245M × (69% − 37%) = **$20,558M** lands in 2027 [10K-25 RPO note].
   - The base FY27 equipment revenue here is ~$32.6B (Power 12.7 + Electrification ~14.9 + Wind ~5.0). The ~$12B gap must come from Prolec plus orders booked in 2026–27.
   - For Power: 21 GW × ~$604/kW ≈ $12.7B, using the GW table [10-Qs] and the $/kW proxies in Q2.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Confidence |
|---|---|---|---|---|---|---|
| 1 | FY25 segment EBITDA / corporate / adj EBITDA | 2,902; 1,433; −598 / −541 / 3,196 | 10K-25 MD&A table | 10K-25 segment note reconciliation (the same filing; the Q4'25 release is the independent S2 [FACTS]) | exact | H |
| 2 | H1'26 segment EBITDA | Power 1,842; Elec 1,200; Wind −657; Corp −239; adj 2,146 | 10Q-2Q26 segment note | 10Q-2Q26 MD&A / REL-2Q26 | exact | H |
| 3 | Quarterly GW / units / HA | Q1 table | Current-quarter 10-Q | Prior-year comparative in the next year's 10-Q | exact | H (Q3'25 single) |
| 4 | 2027 GW ≥~20 | ≥30 GW over 6 qtrs | CALL-2Q26 | LAGUNA cadence (FACTS PP-22) | close | M |
| 5 | 2028 24 GW | 24 | REL-2Q26 | CALL-2Q26 | exact | H |
| 6 | RPO/GW $/kW | 575→741 | 10-Q RPO tables | REL-2Q26 GW (FACTS RV-25) | computed | M |
| 7 | SRA pricing premium | 10–20 pts; >20% | CALL-4Q25 | CALL-2Q26 | close (different bases) | M |
| 8 | CSA revenue flat | 5,473 / 5,412; 2,720 / 2,689 | 10K-24 / 10K-25 notes | 10Q-2Q25 / 10Q-2Q26 notes | exact | H |
| 9 | CSA revisions | −319 / −151 / −218 | 10K-24; 10K-25 | 10Q-2Q26 (FACTS RQ-13) | exact | H |
| 10 | Siemens Energy Gas Services margin | FY25 13.0%; FY26 guide 14–16% | SE AR25 (FACTS PMX-36) | SE-Q3 release | close | H |
| 11 | Baker Hughes IET EBITDA margin | 20.6% Q2'26 | BKR-Q2 nasdaq release | stocktitan 8-K summary | exact | H |
| 12 | MHI Energy Systems margin | 13% → 15.5%e | MHI src:3203 | MHI Q&A (MarketScreener; qualitative) | close | M |
| 13 | Prolec ~25% EBITDA margin | ~$763M on ~$3B | PRO-DECK (13.9x on $10.6B) | PRO-NEWS | close | M |
| 14 | Electrification Q2 margin 18.4%, backlog $41B | as stated | 10Q-2Q26 | CALL-2Q26 | exact | H |
| 15 | Corporate FY26 guide | $450–500M | CALL-2Q26 | FACTS evidence brief (Q2 release) | exact | H |
| 16 | 2028 segment framework | Power/Elec high-teens CAGR at 22%; Wind LDD decline at 6% | DEC25 | REL-4Q25 ($56B incl. Prolec) | close | H |
| 17 | Timing quote "'27 and beyond" | verbatim | CALL-4Q25 | WEB-UD | exact | H |
| 18 | "'29 and '30" quote | verbatim | LAGUNA p.10 | FACTS VF-02 (verified PDF) [effectively SINGLE-SOURCE primary] | exact | H |
| 19 | Wind "materially better 2027" | paraphrase | MB-LAG | LAGUNA | close | M |
| 20 | Fixed-price contracts | risk factor | 10K-25 1A | 10K-24 Item 1 | exact | H |
| 21 | Tariffs 2026 | $100–200M | 10Q-2Q26 | FACTS RQ-01 (Q1 10-Q $250–350M) | close | H |
| 22 | Power opex leverage | 12.7% → 11.5% | 10Q-2Q26 H1'26 table | 10Q-2Q26 H1'25 comparative (the 10Q-2Q25 has the original) | exact | H |
| 23 | Consensus EBITDA | 6,359 / 9,574 / 13,064 | MS | FactSet EPS/revenue cross-check (cnyes; revenue only) [EBITDA SINGLE-SOURCE] | n/a | M |

---

## 4. Arithmetic

### Base FY26 (from guide midpoints)

| Segment | Revenue ($M) | EBITDA ($M) | Basis |
|---|---|---|---|
| Power | 23,649 | 4,257 (18%) | recast 19,873 × 1.19 |
| Electrification | 14,750 | 2,803 (19%) | guide midpoints |
| Wind | ~8,100 | −400 | 9,110 × 0.89 |
| Corporate | n/a | −475 | guide midpoint |
| Eliminations | −450 | n/a | |
| **Total** | **46,049** | **6,185 (13.4%)** | consensus 6,359 |

H2'26 Power implied: 13,200 revenue / 2,415 EBITDA. With services at 7,260 (+6% on H2'25's 6,849), equipment ≈ 5,940, so FY26 Power equipment ≈ 9,774 ≈ $559/kW on 17.5 GW.

### FY27 (research estimate; the team chooses)

| Driver | Low | Base | High | Sources |
|---|---|---|---|---|
| Gas GW | 19 | 21 | 22.5 | CALL-2Q26; LAGUNA |
| Power equipment $/kW (all Power equipment ÷ gas GW) | 575 | 604 | 630 | 10-Q revenue/GW; RPO/GW |
| Power equipment revenue | 10,925 | 12,680 | 14,175 | computed |
| Power services growth | +5% (14,546) | +7% (14,823) | +9% (15,100) | 10K-25; 10Q-2Q26 |
| Power revenue | 25,471 | 27,503 | 29,275 | computed |
| Power margin | 18.5% | 20.5% | 21.5% | trend 10K/10Q; GLJ (FACTS GLJ-04); DEC25 |
| **Power EBITDA** | **4,712** | **5,638** | **6,294** | |
| Electrification organic growth / Prolec | +12% / +5% | +18% / FY26 ×12/11 ×1.10 | +24% / +13% | CALL-2Q26; DEC25; PRO-DECK |
| Electrification revenue | 16,600 | 17,470 | 18,300 | |
| Electrification margin | 19% | 20.5% | 22% | REL-2Q26; SE-Q3 |
| **Electrification EBITDA** | **3,154** | **3,581** | **4,026** | |
| Wind revenue / EBITDA | 7,130 / −300 | 7,700 / 0 | 8,100 / +250 | CALL-2Q26; MB-LAG; DEC25 |
| Corporate | −550 | −475 | −425 | CALL-2Q26; 10K-25 |
| **Total revenue** | **48,751** | **52,223** | **55,225** | consensus 52,740 |
| **Adjusted EBITDA** | **7,016 (corner)** | **8,744 (16.7%)** | **10,145 (corner)** | consensus 9,574 |

- **Statistical band (root-sum-square of segment deviations):**
  - Low: √(926² + 427² + 300² + 75²) = 1,066 → **7,678**.
  - High: √(656² + 445² + 250² + 50²) = 833 → **9,577**.
- **Cross-check on the base Power margin:** services at 22.5% × 14,823 = 3,335, so equipment must earn 2,303 / 12,680 = **18.2%**. That compares with ~10.2% in H1'26 (at s = 22%) and ~0.4% in FY25.

**FY26 → FY27 bridge (base), total +2,559:**

| Component | $M | Calculation |
|---|---|---|
| Power volume at FY26 margin | +694 | 3,854 × 18% |
| Power margin | +688 | 2.5 pts × 27,503 (6 rounding) |
| Electrification volume | +517 | 2,720 × 19% |
| Electrification margin | +262 | 1.5 pts × 17,470 |
| Wind | +400 | |
| Corporate | 0 | |

Group margin moves from 13.4% to 16.7%.

### FY28 (research estimate)

| Segment | Low | Base | High |
|---|---|---|---|
| Power | 22 GW × $600 + services 15,270 = 28,470 @ 20% → **5,694** | 24 × $652 + 15,860 = 31,510 @ 22% → **6,932** | 25 × $690 + 16,460 = 33,710 @ 24% → **8,090** |
| Electrification | 18,260 @ 20% → **3,652** | 20,265 @ 22% → **4,458** | 21,960 @ 23.5% → **5,161** |
| Wind | **0** | **+300** (on ~7.0B) | **+450** |
| Corporate | −575 | −500 | −450 |
| **Total** | **8,771** | **11,190 (on 58,325 = 19.2%)** | **13,251** |

- Statistical band: low 11,190 − 1,509 = **9,681**; high 11,190 + 1,364 = **12,554**.

### Consensus-implied margin tests

- FY27: (10,049 − E − W) / Power revenue (Q11).
- FY28: (13,564 − 420) / 53,950 = **24.4%**.

### Tornado (FY27, base 8,744; incremental margin on volume assumed 25%)

| Rank | Driver | Swing ($M) | Low / high ($M) |
|---|---|---|---|
| 1 | Power margin | 825 | −550 / +275 |
| 2 | Wind EBITDA | 550 | −300 / +250 |
| 3 | Gas GW | 529 | −302 / +227 |
| 4 | Electrification margin | 524 | ±262 |
| 5 | Electrification growth | 414 | −215 / +199 |
| 6 | $/kW (recognition mix) | 289 | −152 / +137 |
| 7 | Corporate | 125 | −75 / +50 |
| 8 | Power services growth | 122 | ±61 |

---

## 5. General question bank items answered along the way

- **G2:** Consensus FY27 needs Power margin about +3.5–5.5 pts in one year (18% → 21.5–23.5%). History shows +2.2 to +3.3 pts a year (items 1–2).
- **G6:** The evidence differs from consensus in FY27 Power margin (~1–3 pts, $275–825M) and in FY28 Power plus Electrification margin (24.4% needed vs 22% targeted).
- **G11:** Shipments ran 1.5–5.2 GW a quarter from Q1'24 to Q2'26, and H1'26 shipments were below H1'25. The capacity ramp is not yet visible in shipments (Q1 table).
- **G12:** CSA revenue is flat while revisions are negative. Deposits sit outside EBITDA.
- **G16:** CSA profitability revisions (−$218M in H1'26) are a Power margin risk that is being treated as noise.
- **G20:** Definition traps:
  - Power $/kW includes non-gas equipment.
  - Siemens Energy and MHI margins are after D&A (profit before special items / business profit), unlike GEV's segment EBITDA.
  - Consensus EBITDA is single-source.
  - Recurring stock-based compensation is not added back to adjusted EBITDA.
- **G22:** The FY27 guide on the January 2027 call must show a margin of ~18% or higher (not the Power figure alone) for consensus to stand. For FY28 consensus, a raise of the 2028 plan is needed.
- **G24:** Recurring stock-based compensation ($257M) is expensed inside adjusted EBITDA. The one-time option grant is excluded via separation costs [10K-25; FACTS VF-12].

---

## 6. What would change this

- **Power margin at 19% or higher in Q3'26** (guide 17–18% [CALL-2Q26]), or a Q4'26 margin at 20% or higher, supports the high case of 21.5%.
- **CSA revisions turning favourable**, or CSA revenue growing, would move the services margin up and the base up.
- **Q3/Q4'26 shipments of 5 GW or more a quarter** confirm 21–22 GW for 2027. Shipments at or below 4 GW point to the low case.
- **Wind at breakeven or better in Q3'26 and H2 of +$257M** supports FY27 Wind above zero. Another miss supports the low case.
- **Disclosure of equipment vs services margins** (possible at the spring 2027 CMD [LAGUNA]) would replace the Q5 grid.
- **A January 2027 FY27 guide at 17% or higher adjusted EBITDA margin** would put the base below management's guide.

## 7. Disagreements with the master brief

- **Section 3 ("20 GW/yr run-rate from Q3'26")**: this describes production capacity. Recognised shipments were 7.5 GW in H1'26, below H1'25's 8.2 GW. The team should model GW shipped, not output.
- **Section 6**: services pricing and growth are treated as uniformly positive. The filings show CSA revenue flat for two years and negative profitability revisions in every period, with H1'26 the worst half since FY24.
- **Section 8 frames the long case as "Power margin gains are real"**: they are, and the trend pace (+2–3 pts a year) supports ~20.5% in FY27. That is stronger for the long side than the brief implies. The 2028 22% target, not the trend, is what makes consensus look early.
- Otherwise none.

## 8. Open items

- **Q3'25 quarterly units** have only one source until the Q3'26 10-Q (due 2026-10-28).
- **Offshore remaining loss exposure** and the Vineyard settlement terms are not disclosed. Look at Q3'26 10-Q Note 9 and the offshore RPO.
- **Contract escalation terms** for gas equipment were not found. Look in utility rate-case dockets (KY PSC 2025-00045 exhibits) and SE/MHI Q&A.
- **Free segment-level consensus does not exist.** The Power consensus margin (20.7%) comes only from GLJ. Check a broker note or Visible Alpha if accessible.
- **The over-time vs point-in-time revenue split** for heavy-duty units is not found. Look at 10K-25 Note 9 on revenue-recognition policy.
- **Prolec actual FY26 margin** is not separately disclosed. Watch Q3'26 commentary; the ~$900M of Q2 revenue is known [CALL-2Q26].
- **The FY26 base** assumes H2'26 Power services at +6% and Wind revenue −11%. The team should re-derive both once Q3'26 prints.
