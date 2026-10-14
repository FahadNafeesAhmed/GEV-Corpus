# GEV Synthesis Report (run 2, 2026-09-21)

**Headline:** No finding survived this run. All four verified findings were reproduced but refuted as not novel or wrongly attributed. The angles below are rebuilt from (a) pieces the verifiers said were salvageable and (b) items verified in the earlier run. Anything marked *unverified* was not re-checked here.

## 1. Top angles

Ranking uses verifier materiality (all fallen items scored 2/5). Confidence is high where numbers reproduced, medium where only the finder ran the query.

### A. LTSA margin cuts are accelerating (verified earlier; novelty high; either side, leans short)
**Claim:** GEV cut its estimate of long-term service contract profit by $218M in H1'26, five times H1'25.
**Mechanism:** A long-term service agreement (LTSA) is a multi-year contract to maintain a turbine. GEV books profit on it using an estimate of future costs. When it cuts that estimate, the loss hits the current quarter. Cuts are growing while contract revenue is flat.

| Item | H1'25 | FY25 | H1'26 | Source |
|---|---|---|---|---|
| Net unfavorable estimate change | -$42M | -$151M | -$218M | 10-Q Note 9, 2026-07-22 |
| CSA revenue recognized | $2,720M | $5,412M | $2,689M | same |
| CSA billings | $2,533M | $5,362M | $2,392M | same |
| Share of Power EBITDA | | | 11.8% | 10-Q segment table |

**Why the market misses it:** The line sits in a footnote. Commentary chunks never mention it. Sell-side quotes the services backlog, not the estimate line.
**Prediction:** Q3'26 10-Q (about Oct 21) shows a 9-month figure worse than -$300M.
**Kill:** 9-month figure better than -$250M, or management gives a one-off reason on the call.
**Build (2 days, industrial engineer):** Pull the Note 9 sentence from every 10-Q/10-K since 2024, chart the series against Power EBITDA, and add the 10-K sensitivity (1 point of margin = $0.2B).
**Caveats:** Not re-verified this run. Power services revenue by turbine class is not disclosed, so the cause (HA wear, F-class, pricing) cannot be proven from filings.

### B. Wind guidance needs a first-ever profitable half (unverified; novelty medium; short, or a long catalyst if it happens)
**Claim:** The FY26 Wind guide of about -$400M implies H2'26 Wind EBITDA of about +$257M after -$657M in H1.
**Mechanism:** EBITDA is profit before interest, tax, and depreciation. No half since 2023 has been positive. The only visible bridge is the confidential Sept 16 Vineyard Wind settlement.

| Period | Wind EBITDA | Source |
|---|---|---|
| H1'25 | -$312M | 8-K/EX reconciliation |
| H2'25 | -$286M | derived |
| H1'26 | -$657M | 8-K/EX 2026-07-22 |
| H2'26 implied | +$257M | arithmetic |

**Why missed:** The guide was "reiterated," so nobody redid the half-year math.
**Prediction:** Q3'26 Wind EBITDA is positive or the guide is cut by Oct 21.
**Kill:** Q3 Wind EBITDA above +$100M with no one-off settlement gain disclosed.
**Build (1 day, industrial engineer):** Table of Wind quarterly EBITDA from 8-K reconciliations; flag any settlement gain in the Q3 10-Q.
**Caveats:** Settlement terms are secret. A one-time gain could make the guide true without any operating fix.

### C. Equipment backlog is going long-dated (unverified; novelty medium; short on 2027 estimates)
**Claim:** The share of equipment RPO due within 12 months fell from 46% (Q3'24) to 36% (Q2'26).
**Mechanism:** RPO (remaining performance obligations) is contracted work not yet booked as revenue. If less of it is near-term, revenue growth arrives later than the headline backlog suggests.

| Date | Equip RPO | 1-yr share | 3-5 yr tranche | Source |
|---|---|---|---|---|
| Q3'24 | $42.1B | 46% | $8.8B | 10-Q footnote |
| Dec-25 | $64.2B | 37% | ~$18B | 10-K |
| Q2'26 | $87.8B | 36% | $28.1B | 10-Q 2026-07-22 |

**Why missed:** Everyone quotes the $176B total; the percentage split is one sentence.
**Prediction:** Q3'26 1-year share at or below 35%.
**Kill:** Share rises above 40%, or 2027 revenue guide is raised above the RPO-implied figure.
**Build (1 day, computer engineer):** Regex over the eight filings, multiply by the percentages, compare the 12-month tranche to consensus 2027 equipment revenue.
**Caveats:** A falling share is also what a longer, sold-out order book looks like. It is a timing point, not a demand point.

### D. Customer affordability ladder (salvaged by skeptic; novelty medium; short, long horizon)
**Claim:** Oglethorpe's own budgets show all-in plant cost rising from ~$2,300/kW (2029 COD) to ~$3,200-3,800/kW (2033 COD).
**Mechanism:** GEV sells the turbine; the customer pays for the whole plant. If plant cost inflates faster than turbine price, the constraint becomes what utilities can get approved, not what GEV can charge. Arkansas already refused to call Entergy's Jefferson plant cost prudent (Jan 2026).

| Project | COD | $/kW all-in | OEM | Source |
|---|---|---|---|---|
| Smarr CC 1,425 MW | mid-2029 | $2,316 | GEV 7HA.03 | OPC 8-K Aug 2026 |
| Talbot 7 CT 240 MW | 2029 | $1,833 (was $1,500) | Siemens, not GEV | same |
| 209 MW CT | 2032 | $2,510-2,990 | unnamed | same |
| 713 MW CC | 2033 | $3,225-3,790 | unnamed | same |

**Why missed:** OPC is a co-op filer nobody reads for GEV.
**Prediction:** Next Georgia Power or OPC IRP filing (2027) shows CC cost above $2,500/kW for 2032+.
**Kill:** A 2032+ CC budget flat below $2,500/kW.
**Build (2 days, mining engineer, who knows capex escalation):** Merge the OPC ladder with the Entergy series ($1,583 to $2,773/kW, 2024-2026 filings) and Duke Cayuga ($2,012 to $2,236).
**Caveats:** The finder misattributed Talbot 7 to GEV. Turbine share of plant cost is an assumption. Nothing resolves inside 12 months.

### E. HA fleet: the 2-year lag model, not a stall (salvaged; novelty low; either)
**Claim:** Running HA units track shipments two years earlier, so FY26 10-K should show ~139-141 running units.
**Mechanism:** Shipped 2023: 14, 2024: 15, 2025: 24. Running base rose +11 in 2025. Service revenue starts only after commissioning plus a warranty period.
**Evidence:** installed base 94/100/106/115/126/~130 (10-Qs 2024 to Q2'26 call); queue 30 to 43; hours per unit rising ~5,800 to ~7,400.
**Prediction:** FY26 10-K (Jan 2027) shows 139-141 running.
**Kill (real warning sign):** below 135 running with queue above 50.
**Build (half day, computer engineer):** Small table; ties to the customer COD ladder (Entergy seven CCs 2030-31, Duke Anderson end-2030), which supports the "services lag to the 2030s" view.
**Caveats:** Verifiers found the "stall" reading wrong; utilization is rising. Use as a base case, not a catalyst.

### F. No large turbines have entered US service since 2023 (verified earlier; novelty low; short on near-term US deliveries)
**Claim:** EIA-860M shows 0.0 GW of HA-class (300 MW+) turbines reaching operation in 2024, 2025, or 2026 YTD; status-P (no approvals) planned GW grew 7.7x while under-construction GW grew 2.6x.
**Evidence:** P-status 4.8 GW (2024-06) to 37.0 GW (2026-07); under construction 5.0 to 12.9 GW; 2027 COD pipeline 11.1 GW, only 3.6 GW under construction.
**Prediction:** 2026-12 vintage shows under-construction GW below 16.
**Kill:** Under-construction GW above 20 by year-end.
**Build (1 day, computer engineer):** Rerun the vintage queries; exclude Fermi (11.7 GW, Siemens) explicitly.
**Caveats:** GEV revenue is cost-to-cost, so US commissioning does not drive reported sales. 17% of the pipeline is one Siemens campus.

## 2. Patterns across findings

The salvageable pieces point one way: GEV's numbers are real, but the timing is later than the narrative. Services from new HA units start in the 2030s (angles D, E, F). Equipment revenue is pushed out (C). Meanwhile the existing service book is being written down (A) and Wind must flip to profit on faith (B).

Conflict: the verifiers repeatedly found that "shipments" and "commissioning" do not drive GEV's reported revenue because it is booked as costs are incurred. So physical-lag angles (E, F) are weak for a 3-12 month price call. Accounting angles (A, B, C) are the ones with dated catalysts (Oct 21 10-Q).

Single most useful check: the Q3'26 Note 9 estimate-change figure. If it is worse than -$300M for nine months, angle A becomes a memo-grade risk with a mechanism; if it snaps back, the services thesis is intact and the short case rests only on Wind.

## 3. Refuted or not reproduced

- **Entergy dropped 2028 date:** whole regulatory paragraph fell out of the 10-Q, not the date; Franklin Farms is not a GEV plant; late-2028 reaffirmed publicly Dec 2025.
- **HA activation stall:** queue grew because shipments jumped (24 = 13 queue + 11 running); 1.8-year lag is normal; utilization rising.
- **HA shipments down, inventory up:** Q2'25 was the series high; trailing-4Q GW flat (14.6 vs 15.3); inventory build disclosed and part-Wind; revenue grew 14% while GW fell 37%.
- **Oglethorpe $/kW:** Talbot 7 is Siemens, budget +22%; Smarr $2,300/kW is in public decks.
- **Earlier run:** June-Sept drawdown decomposition, hyperscaler prints, tariff cut, 80/20 data-center split, $0.3B availability shortfall — all not novel or wrongly attributed. The availability shortfall is a Wind charge, not HA; do not pair it with gas.

## 4. Low-novelty but true

- SRA pool dwell ~15-19 months vs Siemens 6-12; SRAs are 54% of GEV's 116 GW.
- GW under contract no longer moves the stock (Q2'26: +16 GW, -8.5% ex-basket).
- Sep 14 was half a sector rout (basket -6.3%, Siemens Energy -8.1%).
- $200B backlog target restated three times; straight line already reached it.
- "300% price rise" and "$3,000/kW" are single-origin analyst/plant-cost figures; GEV says +10-20%.
- "$70M per GW-year" is a Jefferies 2030s projection; today's figure is at most ~$15-33M.
- Three-OEM capacity (~85-90 GW/yr) exceeds MHI's post-2027 market view (40-50 GW).
- FY25 10-K added over-investment and hyperscaler-credit risk factors.
- Prolec: 21% EBITDA margin but 98% of price is goodwill/intangibles; ~$180M/qtr amortization.
- FERC ordered NERC data-center load standards by Dec 31 2026 (Electrification catalyst).
- F-class rotor life limit (144k hours) puts ~800-900 7F units into a rotor window; third parties compete for it.
- Onshore Wind orders -61% units in Q2'26 with zero repowers.
- US CC fleet generation fell 3.1% in 2025; capacity factor flat 53-55%.

## 5. Dead ends and gaps

**Dead ends (deduplicated):** No customer filing discloses SRA deposit or refund terms (NRG, Kenon only give GW). No OEM says whether SRA price is fixed at reservation. Hyperscaler 10-Ks have zero turbine content. Utility filings never name the OEM. No filing gives Power services by turbine class, US/international order split, or offshore loss provisions. `queue_projects`, `operator_forecasts`, `events` tables are empty; `competitor_financials` is unusable for MHI/Vestas/Hitachi; `mgmt_guidance.prior_value` is unreliable; XBRL tags for CSA billings and Wind losses are mislabeled. Prices table lacks NVDA, hyperscalers, Siemens, MHI. No 2026 GEV transcript chunks with dates. Vineyard settlement terms are confidential. Semantic search was not used by any lens.

**Gaps to ingest next:** Q4'25 Power services RPO jump (+$4.8B in one quarter) is unexplained and worth a question. Entergy Q3 call and LPSC docket for real COD dates. Kenon 20-F and 6-K exhibits (flagged for "advance payment" + GE Vernova, not read). TVA Cumberland lease exhibits. Sell-side notes (none checked directly). NERC's own Virginia incident report. Ollama semantic search over the corpus. Melius and Jefferies underlying notes.

**Weak spots:** Every angle above is a timing or accounting observation; none has a proven price-moving catalyst. Materiality was 2/5 on everything verified. The team should expect the memo's edge to come from combining A, B and C into one "quality of the ramp" argument, not from any single number.