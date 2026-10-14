# Check: already known or bad data (candidate: equipment revenue vs backlog schedule)

_AI-assisted research input only. Facts, arithmetic, tables and sources. The team writes every memo sentence, chooses every forecast number and the direction. Bloomberg data: cite as "Bloomberg, 2026-10-01", keep inside the project folder._

Working date 2026-10-01. All figures $M unless stated. "Y1" = equipment backlog x the share GEV says converts within one year. "Street" = Bloomberg BEst mean.

## 0. Result

| Question | Answer |
|---|---|
| Key numbers recomputed from the primary files? | Yes. Street 30,244.95; Y1 31,616; seven back-test ratios 0.918 / 1.028 / 1.036 / 1.076 / 1.105 / 1.052 / 1.066 |
| Is the Street figure solid? | Total revenue: yes. The equipment split: only partly (section 1) |
| Is the arithmetic already published? | Not found in the corpus (9,715 documents) or on the web (section 2) |
| Is the predicted outcome already familiar to the market? | Yes. It is the same size as GEV's revenue beat over the last four quarters, +5.1% (section 3) |
| Has the stock gone up on it? | No. Three of the last four revenue beats were followed by a flat or lower share price (section 3) |
| Ordinary explanation that removes the gap? | None found. One explains why it exists: brokers follow the guide, and the guide starts below the schedule (section 4) |
| Verdict on this check | Not killed. The sign of the gap holds on every Street measure. The size does not: use about +5% (range +1% to +9%), not +8.7% |

## 1. Is the consensus figure robust?

**Coverage and freshness (Bloomberg, 2026-10-01).**

| Item | Value | Source |
|---|---|---|
| Brokers behind quarterly total revenue | 28 for Q3 and Q4 2026; 22 for Q1 and Q2 2027 | `01_eeo_annual.xlsx`, "#" columns |
| Brokers behind FY27 revenue / EBITDA | 36-38 / 36 | `GEV_bloomberg_pull_filled`, Consensus and ConsensusHistory |
| Quarterly sum vs annual consensus, 2027 | 53,096 vs 53,029 | same |
| Rating or target refreshed on or after 2026-07-22 (the day the 10-Q with the 36% was filed) | 37 of 45 listed brokers | Bulk sheet |
| Brokers behind each division equipment line | Not shown on this terminal | `06_modl.xlsx` has broker columns but the cells are blank |

**The equipment split is softer than the total.** Four Bloomberg readings of Q3 2026 Street equipment revenue:

| Measure (Q3 2026) | $M | vs the figure used (7,482) |
|---|---|---|
| Sum of the three division equipment means (the figure used) | 7,482 | |
| Sum of the three division equipment medians | 7,615 | +1.8% |
| Income-statement "Product revenue", mean | 7,361 | -1.6% |
| Income-statement "Product revenue", median | 7,304 | -2.4% |

Source: `06_modl.xlsx` (single period, Q3 2026). Medians and the product line are not exported for the other three quarters.

- Signs of a stale model inside the division means: Electrification Q3 low estimate 2,995 (equipment 2,301) against a company guide of $3.8-4.0B and a Q2 actual of 3,637; Power Transmission low 1,014 against a Q2 actual of 1,877. Those values look like a model without Prolec. Electrification services low is 39 against a Q2 actual of 507. Wind RPO high is 112,612 against an actual of 20,388.
- Segment equipment lines include about $30-45M a quarter of intersegment sales; the back-test uses consolidated revenue. Effect: the Street on a consolidated basis is about 0.5% lower.

**What that does to the checkable floor (Y1 with no uplift).** The Q3 ratio is applied to all four quarters, which is an assumption.

| Street measure, four quarters | Street $M | Gap, Y1 = 31,616 | Gap, Y1 at 35.5% = 31,176 |
|---|---|---|---|
| Division means (used) | 30,245 | +4.5% | +3.1% |
| Scaled to medians | 30,781 | +2.7% | +1.3% |
| Scaled to product-revenue mean | 29,757 | +6.2% | +4.8% |
| Scaled to product-revenue median | 29,526 | +7.1% | +5.6% |

The Street is below the schedule in all eight cells. The size runs from +1.3% to +7.1%.

**Second vendor.** Benzinga consensus page (2026-09-01): Q3 2026 revenue $12.02B and Q4 2026 $13.84B, sum $25.86B. Bloomberg: 11,993 + 13,915 = $25.91B. Difference 0.2%. For FY27 revenue the earlier research logged $52.74B from two other vendors against Bloomberg's $53.03B (0.5%). No second vendor was found for the equipment split.

**Total revenue, which does not depend on the split.** Street four quarters 50,019. Services taken as the last four reported quarters (17,811) grown 8.0% (its own latest growth) to 11.1% (what the Street has).

| Equipment case | Services +8.0% | Services +11.1% |
|---|---|---|
| Y1 at 35.5% (31,176) | 50,412 (+0.8%) | 50,964 (+1.9%) |
| Y1 (31,616) | 50,851 (+1.7%) | 51,404 (+2.8%) |
| Y1 x 1.02 | 51,484 (+2.9%) | 52,036 (+4.0%) |
| Y1 x 1.04 | 52,116 (+4.2%) | 52,668 (+5.3%) |

On the line with 22-28 brokers the floor is +0.8% to +2.8%.

## 2. Is it already stated somewhere?

| Where looked | Found |
|---|---|
| Corpus full-text search: "backlog conversion", "RPO conversion", "within one year" + equipment, "next 12 months" + backlog, "2027 revenue" + consensus, "book and ship" | The 36% sentence appears in every 10-Q and 10-K since the spin and in the Q2 2026 10-Q PDF on the company site. Two press pieces quote "36% within one year" (Motley Fool 2026-08-22; EBC Financial 2026-07-23). Neither multiplies it by the backlog or compares it with consensus |
| Web search (two engines), July-October 2026 | The same two press pieces. No broker summary, blog or article with $31.6B or a comparison with Street equipment revenue |
| Company materials | Release and slides give equipment RPO by division but not the one-year share. Q2 call: "we're going to ship over the next six quarters at least 30 gigawatts" and "growth next year at 20 gigawatts"; Electrification 2026 revenue guide raised to $14.5-15.0B. So the volume drivers are public |
| Published estimate above consensus | Lark Research, 2026-08-04: 2027 revenue $54.5B (+18.6%), which is 2.8% above Bloomberg's $53.0B. It does not cite the schedule. Single source |
| Company-compiled consensus | None found on the investor site |

Limit: full broker notes are not in the corpus or on the open web, so a broker using the schedule in a paid note cannot be ruled out.

## 3. Is the outcome already familiar, and has the stock moved on it?

**Revenue against the pre-print consensus, last four quarters.**

| Quarter | Consensus $B | Actual $B | Surprise | Share move on the day |
|---|---|---|---|---|
| Q3 2025 | 9.17 | 9.97 | +8.7% | -1.59% |
| Q4 2025 | 10.15 (earlier research: 10.23) | 10.96 | +7.9% | +2.73% |
| Q1 2026 | 9.28 | 9.34 | +0.6% | +13.75% (margin guide raised) |
| Q2 2026 | 10.75 (FactSet via Dow Jones: 10.79) | 11.10 | +3.3% | -8.69% (margin guide held) |
| Four quarters | 39.35 | 41.37 | **+5.1%** | |

Sources: Benzinga earnings page (consensus and actual; single source for Q3 2025 and Q1 2026); `S04_multiple_evidence.md` (day moves).

- The candidate's total-revenue range (+2.7% to +6.6%; +0.8% to +5.3% in section 1) is the same size as the +5.1% GEV has just delivered against consensus over four quarters.
- The same shortfall was there a year ago. Pre-print consensus for those four quarters, less Prolec (1,346) and less actual services, gives Street equipment of about 20,236 against Y1 at 6/30/25 of 20,879: ratio 0.969. The actual ratio was 1.066. Pre-print consensus is higher than consensus at the start of a window, so the starting ratio was at or below 0.97.
- Street FY27 revenue has risen from 50,282 (2026-02-06, after Prolec) to 53,029: +5.5% in eight months, about 0.7% a month. A +3% view on FY27 revenue equals four to five months of that drift.
- Reuters, 2026-07-22, quoting a broker: investors "were expecting another EBITDA beat and raise". That day revenue beat by 3.3%, the revenue guide rose $1B, and the shares fell 8.7%.

Reading: the schedule explains why GEV keeps beating revenue. The beat itself is not new to the market, and the share price has not gone up on it.

## 4. Ordinary explanations

| Explanation | Test | Result |
|---|---|---|
| Brokers follow the guide | Street H2 2026 revenue 25,908 against guide-implied 25,058-26,058; Street Q3 11,993 against a guide rebuild of $11.7-12.1B | True. This is why the gap exists; it does not remove it |
| The guide itself starts below the schedule | January 2026: organic guide $41-42B less organic services (18,745) = equipment 22,255-23,255 against Y1 at 12/31/25 of 23,771: ratio 0.936-0.978. After two raises (+$0.5B April, +$1.0B July) the guide implies 23,654-24,654: ratio 0.995-1.037 | A precedent in the candidate's favour: the same shortfall closed upward within six months. It also shows the pattern is routine |
| Uplift is shrinking | Latest windows using actuals plus the company's own guide: 9/30/25 window about 1.03 (three quarters actual); 12/31/25 window 1.00-1.04. Earlier windows 1.05-1.11 | The uplift to use is about 1.00-1.04, not 1.04-1.06 |
| Deliveries slip | The schedule needs equipment +24% on a pro-forma base of 25,491 (Street +18.6%; with 1.04 uplift +29%). Reported organic growth was +12% in H1 2026. Gas output has to step from 14.6 GW to 20 GW. One window in seven missed by 8% | Cannot be excluded. This is the live risk |
| The H1 2027 form breaks seasonality | Street H1 2027 is 45.4% of Street FY27 (history 44.2-45.0%). Adding 1,371 to H1 2027 and holding that share gives FY27 revenue of $56.1-57.7B, above GEV's own 2028 target of $56B | The "gap sits in H1 2027" form needs a break in seasonality or FY27 growth of 21-25%. An H2 2026 beat is the more ordinary reading |
| Acquisition accounting | Prolec is in the 3/31/26 and 6/30/26 backlog and in Street revenue; it is removed from windows that start before 2026-02-02 | No distortion found |
| Reclassification | Equipment and services wording unchanged across the ten filings read | None found |
| Currency | Street assumes almost none (Power -16, Electrification +8 a quarter). Backlog is translated at the 6/30/26 rate | Not tested; no FX series in the pull |
| Rounding of the 36% | Y1 31,176-32,055 | Takes up to 1.4 points off the floor |

## 5. Corrected numbers for this candidate

| Item | Candidate | After this check |
|---|---|---|
| Street, equipment, four quarters | 30,245 | 30,245 on division means; 29,526-30,781 across the four Bloomberg measures |
| Arithmetic value | 32,884 (Y1 x 1.040) | 31,616 (Y1) to 32,880 (x 1.04); centre 32,250 (x 1.02) |
| Gap | +8.7% | About +5% (centre 32,250 against 30,245-30,781 = +4.8% to +6.6%); full range +1.3% to +9% |
| Total revenue gap | +2.7% to +6.6% | +0.8% to +5.3% |
| Why missed | Footnote percentage nobody multiplies | The multiplication is not published anywhere found. The result it predicts (revenue about 5% above consensus) has happened for four quarters and has not lifted the shares |

## 6. Hand-checks before use

- Benzinga consensus figures for Q3 2025 and Q1 2026: single source.
- Lark Research $54.5B: single source.
- Broker count behind the division equipment lines: not visible. Ask the terminal for the contributor list (EEO broker detail) for Q1 and Q2 2027.
- Medians and the product-revenue line for Q4 2026 to Q2 2027: pull `MODL` for each quarter. This check scaled the Q3 ratios.
- H2 2026 Prolec equipment revenue is assumed at 850 a quarter.

## 7. Sources

- Bloomberg, 2026-10-01: `GEV_Pull_2026-10-01/segment_quarterly.json`, `06_modl.xlsx`, `01_eeo_annual.xlsx`, `01-eeo-company-specific.xlsx`; `GEV_bloomberg_pull_filled_2026-10-01.xlsx` (Consensus, ConsensusHistory, Bulk).
- GEV 10-Q Q2 2026, accession 0001996810-26-000148, RPO note (corpus chunk 5683); earlier RPO notes, chunks 13656, 29868, 38506, 44098, 54581, 67387, 77798, 83462, 90281, 98108.
- XBRL product and service revenue: `data/financials/gev_segments.csv`.
- Q2 2026 call transcript (corpus source 3161); guidance history in table `mgmt_guidance`.
- Press: fool.com 2026-08-22; ebc.com 2026-07-23; reuters.com 2026-07-22; benzinga.com/quote/GEV/earnings-forecasts; larkresearch.com/ge-vernova-gev-26q2-results (2026-08-04).
- Prior research: `09_finrobot_overnight/S04_multiple_evidence.md`, `BLOOMBERG_VERDICT.md`; `11_thesis_hunt/propose_rpo-equipment.md`.
