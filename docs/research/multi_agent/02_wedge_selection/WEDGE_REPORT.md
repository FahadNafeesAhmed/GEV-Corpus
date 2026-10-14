
# GEV Wedge Decision — 2026-09-22

## Decision

**Primary wedge: Reservation/deposit conversion-quality gap — SHORT GE Vernova.**
GEV's slot-reservation (SRA) pool — the balance-sheet engine bulls treat as locked-in future high-margin revenue — is converting to priced orders and liquidating **slower than GEV's own history and slower than direct peer Siemens Energy**, even as the pool balloons in dollars. This is `reservation_dwell`, but reframed: drop the "price isn't locked at reservation" claim (already public via two write-ups using the same Maxim Power filing), and lead instead with the **quantified conversion-rate/dwell-time gap vs. Siemens Energy**, which nobody in the corpus, sell-side, or public commentary has assembled.

**Secondary pillar 1 — `services_markdown`:** the 10-quarter LTSA "net unfavorable changes in estimated profitability" series (no XBRL tag, zero prior analyst references), worst two readings in the two most recent quarters, corroborating from the P&L side that the installed base's economics are softer than the pricing narrative suggests.

**Secondary pillar 2 — `wind_h2`:** the single cleanest numeric test in the whole corpus — FY26 guide requires a company-record H2 EBITDA swing — used as the sharpest, most falsifiable dated kill-condition tied to the same print as the other two pillars.

## Correction to the record (verified today, live)

Every dossier that dated the Q3'26 print "~Oct 21, one day before finals" (`wind_h2`, `services_markdown`, several catalyst lists) got the date wrong. I checked **gevernova.com/investors/events** directly: **Q3 2026 earnings is confirmed for October 28, 2026, 7:30–8:30am EDT** — four days *after* HFAC finals (Oct 22-24) end, not one day before. I also confirmed via a direct DB query that the full 6-quarter SRA signed/converted/backlog series each dossier cites reproduces cleanly from the six 8-K press releases (accessions 0001996810-25-000132 through -26-000147). No December 2026 Investor Update date is listed yet. This matters: the team cannot claim the thesis resolves before judging — it resolves five days after. Present it honestly as the near-term proof point to track and to cite in Q&A, not as something that will already be known when the team presents.

## Why this one wins

Two of three independent panel reviews (the "CFA-grader" and "engineer" readings) ranked this #1; the third ranked it #3 mainly because it over-weighted `wind_h2`'s (incorrect) "one day before finals" framing. Correcting that date removes `wind_h2`'s main edge over this angle, so I resolve the tie toward `reservation_dwell`.

It clears the wedge test's hardest bar — "pros structurally miss it" — more cleanly than any other angle in the set:
- It requires joining **six of GEV's own inconsistently-worded quarterly 8-Ks**, **Siemens Energy's own disclosure of its own conversion cadence**, and a **five-filing NRG Energy trail** — three separate sources nobody has cross-referenced.
- Both original skeptics refuted it only because the *qualitative* "deposit ≠ locked price" claim is already public (Seeking Alpha, businessmodelanalyst.com, both using the same Maxim Power Corp filing). Neither skeptic's refutation addresses the **quantified peer-benchmark**, which is the actually novel part and survives their objection intact.
- It attacks the single load-bearing assumption under GEV's 35x forward multiple — that growing SRAs/backlog = locked-in future margin — directly, not just its price-lock corollary.

## The three pillars (sourced evidence)

**1. Reservation conversion/dwell gap (primary)**
- GEV converts ≈20% of its opening SRA balance to priced orders per quarter (implied 5-quarter dwell) vs. Siemens Energy's ≈44% in the same window; Siemens' own fiscal Q1'26 pre-close call showed 12GW converted vs. 12GW newly reserved (near 1:1), vs. GEV's Q1'26 of 6GW converted vs. 19GW newly reserved.
- Rebuilt 6-quarter GEV series (verified directly against 8-K/EX press releases, accessions 0001996810-25-000132/-000159, -26-000012/-000063/-000147): SRA balance 21→25→29→43→56→63 GW (Q1'25→Q2'26); conversion 3,7,8,6,10 GW/quarter.
- Contract-liability (deposit) liquidation slowing: 29% of opening balance converted in H1'26 vs. 40% in H1'25; equipment contract liabilities now 43% of equipment RPO.
- NRG Energy's own 10-K trail: SRA commitment with GEV grew 1.2GW (Feb-25) → 2.4GW (flat May/Aug/Nov-25) → 3.6GW (Feb-26) across five consecutive filings — never priced. One trackable, named counterparty confirming the pattern outside GEV's aggregate numbers.

**2. Services-contract profitability markdown (services_markdown)**
- 10-quarter LTSA "net unfavorable changes in estimated profitability" series, no XBRL tag anywhere (`SELECT DISTINCT tag ... LIKE '%Profitab%'` returns zero rows), confirmed zero prior corpus/analyst references to it as a time series.
- Series (10-Q/10-K, $M): -29, -60, -46, -184, +29, -71, +6, -115, -89, -129 (Q1'24→Q2'26); two worst readings are the two most recent quarters.
- Ties to a physical mechanism: GE's own GER-3620 maintenance document shows 126 HA units averaging ~28,600 factored hours against a 25,000-hour first-hot-gas-path interval — the fleet is aging past its first major service interval, which is a plausible driver of the accelerating markdown.
- Management said services are seeing "solid pricing" (Q2'26 call) the same quarter this footnote posted its second-worst reading ever — a direct, checkable contradiction.

**3. Wind H2 EBITDA bridge (wind_h2)**
- H1'26 Wind EBITDA = -$657M (Q1 -$382M + Q2 -$275M) vs. FY26 guide of ~-$400M, implying H2 must swing to +$257M — ~37x the segment's biggest-ever half-over-half improvement (+$25M, 2025) and ~14x its best-ever single quarter (+$19M, Q4'24).
- Confidential Vineyard Wind settlement (Sep 16, 2026) is structurally analogous to the ~$0.3B one-time gain that produced that only-ever positive quarter — bound the settlement's plausible size against that precedent as the pillar's numeric kill condition.

## Catalyst calendar

| Date | Event | Test |
|---|---|---|
| Oct 2, 2026 | Memo/model/resumes due | — |
| Oct 12, 2026 | Finalists notified | — |
| Oct 22-24, 2026 | HFAC Finals, NYC | Thesis is pitched *before* any of the below resolves |
| **Oct 28, 2026, 7:30am ET** | GEV Q3'26 earnings (confirmed) | All three pillars tested simultaneously: new SRA signed/converted/backlog GW+$; LTSA profitability-revision footnote; Wind EBITDA vs. -$400M guide |
| Dec 2026 (undated) | Possible annual Investor Update (precedent: Dec 9, 2025 caused GEV's largest-ever scheduled one-day move, +15.62% on 3.75x volume, reversed in 5 sessions) | FY27 initial guidance |
| ~Jan/Feb 2027 | FY26 10-K, Q4'26 earnings | First full-year reconciliation |

## What kills it

On Oct 28, if **all three** of the following happen together, concede the short and pivot to `bull_steelman` (Electrification margin inflection) as the balanced long case: (1) SRA conversion rate snaps back toward ~35-44%/quarter (Siemens-like pace) rather than staying near 20%; (2) the LTSA markdown flips positive or stays under ~$30M; (3) Wind EBITDA shows a clean step toward the guided pace with the beat sized no larger than a Vineyard-Wind-settlement-scale one-time item (~$0.2-0.4B) can explain. If instead conversion stays near 20%, the markdown worsens further, or the Wind beat exceeds what the settlement alone can plausibly explain, all three corroborate the "backlog/margin quality worse than headline growth implies" short.

## Rejected alternatives (one line each)

- **rpo_timing** — Own data contradicts itself: equipment revenue accelerated +28.8% YoY while the 1-yr RPO bucket fell, more consistent with backlog-size dilution than demand deceleration.
- **peaker_mix** — Confirmed GE-linked 2026-27 sample is n=1 (146.7MW); conclusion flips sign when the window widens to include Homer City.
- **vintage_fifo** — Its own steelman concedes the "rebuttal" can be read as confirming GLJ's short is live *now*, not deferred to 2027.
- **entergy_exclusivity** — Vendor is never named in any filing (inference only, could invert bullish); volume (11-12GW) is under 10% of GEV's own backlog target and was never in GEV's booked backlog.
- **narrative_gap** — The "AI hype vs. cyclical reality" framing was already fought publicly by GLJ (Sep 14, -8.6%) and Bernstein (Sep 18), eight days before this research began.
- **deposit_bull_case** — A defensive rebuttal to the team's own short case, not an independent thesis; its most likely outcome (deposits merely decelerate) produces no surprise at all.
- **incentive_plan** — Genuinely novel cross-document join, but Adjusted EBITDA (accrual-based, not deposit-boosted) also hit near-max payout in the same periods as FCF, undercutting the causal claim; no dated forcing event in-window.
- **physical_ramp** — Shipped-GW is a headline 8-K bullet, Mizuho's own stated price-target driver, and the explicit basis of GLJ's Sept 14 note — zero incremental edge.
- **december_catalyst** — The 2026 event's date isn't announced (confirmed today: not yet on GEV's IR page), and even on best-case precedent it lands after finals — a calendar footnote only.
- **bull_steelman** — Real long case, but its own reverse-engineered consensus EBITDA already lands near its bullish build, and Morgan Stanley already cited electrification demand in a target raise.
- **blind_discovery** — Fully explained by the public Aug 25 CFO-transition announcement plus a thin 1-2-person historical trading base; no P&L mechanism at all.

## What's still needed before the memo is written

1. **Tie-break outreach/filing check:** pull Siemens Energy's next quarterly SRA/conversion disclosure (similar cadence) to confirm the ~44%/quarter pace is a trend, not a single-quarter snapshot — this is the one piece of unchecked data that would most sharpen pillar 1's peer-gap claim.
2. **Resolve the 2027 consensus EPS discrepancy** (MarketScreener ~$24.85 declining from FY26 vs. stockanalysis.com $25.31 growing from a very different FY26 base of $15.21 — >50% spread) via a third source (Visible Alpha/Seeking Alpha) before citing any EPS-impact number.
3. **Bound the Vineyard Wind settlement's plausible size** against the Q3'24 precedent (~$0.3B) so pillar 3's kill condition is a stated number, not a vague "does it beat or miss."
4. **One physical/primary-source proof outside SEC filings**, per what actually won Carlisle — the team's industrial/mining background suits extending `peaker_mix`'s EIA-860M/projects-table join past its current n=1 sample, or a short, dated outreach log (an EPC contractor, a customer IR desk, an analyst) confirming reservation-to-order lag times independently of GEV's own disclosures.
5. **State the three Oct 28 kill-condition thresholds explicitly and numerically in the memo itself** (not just implied), since Oct 28 lands after judging — the team needs the thesis to stand on pre-finals evidence alone, with Oct 28 offered as the tracked, falsifiable near-term test.
