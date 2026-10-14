# GEV technical wedge hunt — final synthesis

**Bottom line: no finding clears the bar. Not one.** Sixteen lenses produced 36 findings. Every one was refuted by an independent skeptic. Every independent re-quantification landed "immaterial" or "marginal." The best-supported physics in the entire file is worth roughly $3–17/share with a sign nobody could resolve, and the dollars that *did* show up came from a line the team has already worked to death, with the physics contributing exactly zero to the arithmetic.

I am telling you this plainly because the alternative — handing you an elegant mechanism worth $5/share dressed as a wedge — would lose you the room.

---

## 1. The wedge: there isn't one

**What the best of a weak set is.** Three independent lenses converged on the same piece of engineering, and it is real. GE's own maintenance manual (GER-3620 Rev P, Figure 36, verified verbatim from the PDF by three separate agents) sets the 7HA.02/9HA.02 hot-gas-path inspection at **25,000 factored fired hours OR 720 factored starts, whichever comes first.** Divide: 25,000/720 = **34.7 fired hours per start** is the crossover. Run longer than that per start and hours govern. Run shorter and starts govern, and the machine needs an expensive outage far sooner than an hours-based cost model predicts.

The incoming US order vintage is on the wrong side of that line. Simple-cycle peakers run ~987 equivalent full-load hours a year (I recomputed this myself from EIA data: 10.4% / 10.7% / 11.6% / 11.3% capacity factor for 2022–2025) in 3–8 hour blocks, which is 4–8 hours per start — five times below the crossover.

**Why it still fails.** Three breaks, any one fatal.

First, the installed HA fleet is nowhere near the line. GE publishes 3.0M fired hours against 20,400 fired starts = **147 hours per start**, 4.2x clear on the hours side. The fleet that actually generates services revenue today is hours-limited, not starts-limited.

Second, the accounting kills it. GEV recognizes service-contract revenue on **cost-to-cost percentage-of-completion** — revenue is booked as costs are incurred, not as hours are billed. (Percentage-of-completion means you recognize a share of a long contract's total revenue equal to the share of its total expected costs you have already spent.) The FY25 10-K also says billing happens "per hour of usage **and upon the occurrence of a major maintenance event**." Several researchers quoted only the first half. A duty cycle that pulls maintenance forward pulls billings forward with it.

Third, only 7.9 GW of the 21.5 GW of planned US simple-cycle gas is in units ≥400 MW — i.e. large enough to be a 7HA at all. Most of the "peaker wave" is aeroderivatives and small frames that GER-3620's HA intervals don't govern.

**Independent dollars: $2.65 to $17.49/share** (0.3%–1.9%), depending on how much of the 116 GW you judge exposed. The researchers claimed $48, $33 and $14. Two of the three were 2–18x too high. **Sign unresolved:** nobody — not the researchers, not the skeptics — could determine from public sources whether GEV's service contracts bill on *actual* or *factored* fired hours. If they bill on factored hours, GE's own severity formula already prices this and the effect is zero. If contracts bill per maintenance event, more cycling is more revenue and the trade is **long**. Do not trade a 1% idea whose direction you cannot establish.

---

## 2. Runners-up

**(a) The services-contract revision line.** This is where all the dollars actually landed, across a dozen lenses, and it is your existing angle. Verified from filings: net unfavorable revisions to estimated contract profitability were **−$319M in FY24, −$151M in FY25, −$89M in Q1'26, −$218M in H1'26.** Independent quantifiers put a fresh escalation at **$8–17/share.** But see §3 — the FY24 number breaks the story.

**(b) The 800VDC / solid-state-transformer content claim.** Management says data-center electrical content per GW goes from ~$300M to "two to three times" that. The peer-reviewed efficiency ladder (Huber & Kolar, IPEC 2022) shows 800VDC does **not** require a solid-state transformer — a conventional transformer plus a central rectifier hits 97.9% vs the SST path's 97.7%. So GEV's upside leg is a compound bet: the SST architecture must win *and* GEV must win it, against Eaton (10 SST prototypes ordered, flexible UPS/SST lines) and four funded startups. Independent quant: **~$27/share of shortfall if it fails**, but this is a de-rating of an expectation nobody has shown is in the $940 price. Management explicitly says none of it is in the $5B of H1'26 data-center orders. You cannot mark down what was never marked up.

**(c) Gas-turbine castings capacity.** GE Aerospace is buying Consolidated Precision Products for $11.75B, closing H2 2027; CPP Eastlake makes the world's largest industrial gas-turbine blades. Single-crystal casting is the shared bottleneck between new-unit builds and replacement parts. The published version of the idea is saturated; the honest incremental number, after correcting the researcher's arithmetic, is **~$30/share on a permanent-cap framing and ~$0 on a deferral framing** — a 273x spread on an interpretive choice with no physical content. That spread is the finding.

---

## 3. What the physics killed

This section is the real deliverable. These kills protect you from a wrong pitch.

**The revision series is not a clean escalation, and FY24 proves it.** I pulled both filings myself. FY24: revisions of −$319M against $5,473M of contract revenue = **5.83%**. FY25: −$151M against $5,412M = **2.79%**. H1'26: −$218M against $2,689M = 8.11%. FY24 ran at more than double the FY25 "baseline," and GEV attributed it in its own words to "higher costs." FY24 happened when essentially **zero** data-center-tied HA capacity was in commercial operation. So the phenomenon occurs at near the claimed intensity with no AI load present. If you pitch "AI duty cycles are eating the services annuity," a judge with the FY24 10-K ends you in one question.

**Part-load operation is free.** The obvious bear story — "data centers and renewables force turbines to run at part load, so they wear out faster" — is false. GER-3620 sets the hours-based load severity factor at **1.0 all the way down to base load**, and in combined-cycle mode firing temperature doesn't drop until below ~80% of rated output. Part-load start cycles below 60% get a factor of **0.5** — they *extend* the interval. Do not say this on stage.

**The PUE-deflation bear case is dead.** Uptime Institute puts industry average power usage effectiveness at 1.52, flat for seven years. Nobody sizes generation off a survey mean of a legacy fleet; campuses sanctioned in 2026 are designed at 1.1–1.25 and the contract embeds *that* number. The researcher priced the avoided error at $76/share; correctly scoped it is under $4.

**Demand haircuts cannot reach revenue in your horizon.** GEV has 116 GW under contract against 20 GW/yr of output rising to 30 GW/yr by 2030 — roughly five years oversubscribed, in an industry-wide shortage. Trimming demand trims the *back of the queue*. Equipment revenue is recognized over time on costs incurred against contracts already signed. Every "AI needs less power than people think" thesis dies here.

**Batteries are not eating peakers.** Operating US battery capacity went 8.9 → 53.3 GW (+499%) from Jan-2023 to Jul-2026 while simple-cycle utilization went **up**. Planned reciprocating-engine capacity is flat at ~1.0 GW while planned turbine capacity went 11.3 → 44.1 GW; recip share of planned gas collapsed from ~8% to 2.2%.

**Hydrogen is worth approximately zero.** EIA's planned-generator file contains exactly **one** hydrogen unit nationally — 50 MW, and it's a fusion pilot miscoded.

---

## 4. Direction check

**The surviving technical findings point long, or nowhere. They conflict with your short-leaning framing.**

- The HA fleet averages **28,571 operating hours per unit** (3.6M / 126, from the FY25 10-K). The major inspection is at 50,000 factored fired hours. **The average unit has not reached its first major.** At the measured ~6,000 h/yr run rate it arrives in ~3.6 years. That single fact explains the gap between management's $25M/GW-yr services target and today's realized ~$15M/GW-yr with *zero* duty-cycle content — and it is a tailwind, not a headwind.
- US combined-cycle capacity factor (my own computation): 50.6% → 53.1% → 54.4% → 52.6%. Flat to up. Utilization is not collapsing.
- GEV's own FY24 10-K: "gas turbine installed base utilization was flat compared to the same period last year."
- If contracts bill per maintenance event, harsher duty is **more** revenue.
- GEV sells the mitigation hardware for grid instability (grid-forming STATCOMs, synchronous condensers), so Electrification partly hedges Power.

The reservation-conversion and revision-margin legs of your thesis are not *refuted* by any of this. But the physics does not reinforce them, and in several places it argues the other way. Go in knowing that.

---

## 5. How to build it in the days remaining

**Electrical/computer engineer — resolve the sign, today.** One question to GEV investor relations, or one contract disclosure: *do HA service agreements bill on actual fired hours, factored fired hours, or per maintenance event?* This single answer determines the direction of roughly a third of this research. If it comes back "factored," delete the duty-cycle angle entirely and save yourselves two days.

**Industrial engineer — own the fleet-maturity arithmetic.** Build the HA vintage distribution: units by commercial operation date, hours accumulated, and when each crosses 25,000 and 50,000 factored fired hours. Inputs: the 10-K/10-Q installed-base series (94/2.0M → 100/2.5M → 106/2.7M → 115/2.9M → 126/3.6M) plus the `projects` table for CODs. This is disclosed-number arithmetic with no assumption chain, and it is the strongest defensible claim in the file — in either direction.

**Mining engineer — own the castings constraint.** You have the materials background. The question is narrow and answerable: what share of the 116 GW backlog is gated by single-crystal blade casting capacity, and does the CPP acquisition (closing H2 2027) change GEV's access? Sources: EPRI's Shingledecker interview, the Bernstein Howmet note, GEV's own Greenville disclosures.

**All three, before anything gets written:** re-read the FY24 10-K Note 9 paragraph quoted in §3. If your memo cannot survive that sentence, rewrite the memo.

---

## 6. Papers worth reading

1. **GE Vernova, GER-3620 Rev P** (2021-03-15, 60pp, free on gevernova.com). Figures 36, 40, 42, Appendix A. The single most important document. Read Figure 36 and Appendix A yourselves — three agents misread it in three different ways.
2. **GEV FY2025 Form 10-K**, Note 9 and the critical-accounting-estimates page. Net LTSA balance $3.4B ≈ 4% of life-of-contract billings (implying ~$85B), contracts ~29% complete, 1 percentage point of lifetime profitability = $0.2B of contract asset. This is your sizing lever for any services thesis.
3. **Huber, Wallmeier, Pieper, Schafmeister & Kolar, IPEC 2022 (ECCE Asia)** — the 800VDC efficiency ladder, open access from ETH.
4. **Li, She & Zhang, arXiv:2608.10999** (Aug 2026) — SMR-vs-grid economics for hyperscale data centers. Note its own caveat that the $5,000/kWe threshold is specific to the 2023 price year.
5. **Norris et al., "Rethinking Load Growth," Duke Nicholas Institute (2025)** — the flexibility headroom numbers everyone cites.

---

## 7. Dead ends — do not repeat

- **Part-load degradation** (severity factor is 1.0 to base load).
- **PUE deflation shrinking contracted GW** (fleet PUE flat seven years; contracts written at design PUE, not survey mean).
- **Batteries displacing peakers** (utilization rose through a 6x storage build).
- **Reciprocating engines taking turbine share** (recip share of planned gas fell to 2.2%).
- **Hydrogen blending** (zero planned US hydrogen turbines).
- **Grid-enhancing technologies displacing gas** (FERC excluded dynamic line ratings from Order 2023's alternative-technologies list; reconductoring is a 2035-horizon program).
- **Demand haircuts of any kind** (GEV is supply-constrained; orders trim the back of a five-year queue).
- **The corpus academic tier for AI-hardware physics** — it is a power-systems and wind corpus. Zero hits for "energy per token," "roofline," "arithmetic intensity," "factored fired hours." Go to arXiv directly.
- **The `projects` table** for exposure sizing — duplicated rows, blank models, one row carrying 74,000 MW that is actually GEV's entire global installed HA fleet, not a project.
- **EIA-860M for behind-the-meter reciprocating capacity** — it is structurally blind to it.

*(~2,090 words)*