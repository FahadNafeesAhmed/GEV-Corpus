# Multi-agent research runs on GE Vernova (GEV)

All of this is **AI-assisted research input** for the team, disclosed as such under the competition rules. None of it is submission text. Every number carries a source (table + query, filing + date, or URL) so a teammate can re-check it in one step.

| Run | Date | What it did | Agents | Verdict |
|---|---|---|---|---|
| [01_hidden_patterns_sweep](01_hidden_patterns_sweep/SYNTHESIS.md) | 2026-09-21 | 12 finders swept the corpus and web for unexpected quantified patterns; a reproducer and a skeptic per finding | 46 | Found the service-revision series and the reservation mechanics; about half the findings were refuted on verification |
| [02_wedge_selection](02_wedge_selection/SYNTHESIS.md) | 2026-09-22 | 14 candidate wedges deep-dived, 2 skeptics each, a 3-judge panel | 46 | Chose SHORT on the reservation-conversion gap. Corrected the Q3 earnings date to **Oct 28** (after the finals) |
| [03_technical_wedge_hunt](03_technical_wedge_hunt/SYNTHESIS.md) | 2026-09-22 | 16 physics/engineering/AI-hardware lenses over arXiv, IEEE, OpenAlex and the corpus academic tier; a physics skeptic and an independent $/share quantifier per finding | 91 | **No technical wedge.** 212 papers read, 38 findings, zero survivors. Killed nine popular bear arguments |
| [04_market_briefing](04_market_briefing/SYNTHESIS.md) | 2026-09-23 | 15 collectors on consensus, valuation-implied assumptions, guidance base rates, ownership, short interest, drawdown anatomy, credit, suppliers, customer filings, regulation, physical signals, the pitch field and the sell-side map; each reproduced | 31 | Eleven corrections to facts the team was carrying, plus a proper consensus baseline |
| [05_decision](05_decision/SYNTHESIS.md) | 2026-09-23 | 16 full cases (8 long, 8 short), 2 red-teamers each, a 5-judge panel | 54 | **LONG**, defensive, 4-1 on a forced choice. All 16 cases were killed; the shorts died on wrong mechanisms, the longs on being already priced |
| [06_vintage_verify](06_vintage_verify/SYNTHESIS.md) | 2026-09-29 | 8 surgical attacks on the backlog-vintage calculation (RPO conversion schedule vs the GLJ Sell note), then an adjudicator | 9 | **Survives, narrower.** Cut at 31-Dec-2025: $20,558M of 2027 revenue from that book; 2027 equipment revenue 8-20% pre-2025 vintage, 47-62% 2025 vintage, 29-35% later; Power-only 6-16%. 15 figure corrections |
| [07_pitch_winners](07_pitch_winners/SYNTHESIS.md) | 2026-09-29 | 20 elite pitch winners read from their own decks, 5 cross-case lenses, a playbook and a gap check on this pitch. Full corpus in `../../../../pitch-winners-corpus/` | 33 | "A well-evidenced rebuttal, not yet a pitch with an edge." Needs one number on one line next to consensus |
| [08_evidence_brief](08_evidence_brief/SYNTHESIS.md) | 2026-09-29 | 11 research lanes on the gap-check tests, each re-derived by its own verifier, then an assembler. `FACTS.csv` is the team's hand-verification sheet | 23 | Complete. Decisive tests, direction lookup, model inputs, memo element checklist, judge question bank (`QA_BANK.md`) |

| [09_finrobot_overnight](09_finrobot_overnight/MORNING_SUMMARY.md) | 2026-09-30 | 49 single-model research tasks overnight (a hosted LLM via FinRobot, with the corpus, filings and Exa as tools): two FY27 builds, 13 framing variations, red teams, a final synthesis, then red-team, top-20 verification, exhibit data, evidence maps, kill rules and consensus drift. Two sources per number required. `INDEX.md` lists every task | 56 tasks | Overnight: research FY27 adj EBITDA $8.6-8.9B vs Street $9.34-9.57B; Street FY28 16.6% above GEV's own framework. Morning robustness tasks (S01-S07): the estimate gap is fragile, the multiple decides, research lean is a 12-month long with low conviction. See `ROBUSTNESS_PACK.md` |

**333 agents across eight runs, plus 56 single-model tasks in run 09.** An earlier ninth run (2026-09-29, percentage-of-completion check) was stopped before any agent finished and replaced by run 06.

| Folder | Date | What it holds | Verdict |
|---|---|---|---|
| [11_thesis_hunt](11_thesis_hunt/THESIS_HUNT.md) | 2026-10-01 | A number-first hunt: 10 lenses, 15 candidates, 7 examined by three checkers each, three judges (37 agents). Then the gigawatt view rebuilt three ways (10 agents, `GIGAWATT_ANGLE.md`) | **No winning thesis.** One small survivor: equipment revenue for the next four quarters, 4.5% above analysts |
| [12_team_brief](12_team_brief/TEAM_BRIEF.md) | 2026-10-02 | Research notes for the memo and the model. Every number checked three ways. Section 12 adds the second Bloomberg pull, the Electrification test and the 3-to-12-month table | 12-month long: base $1,126, bear $855, bull $1,341, break-even 21.8x |
| [13_thesis_dossier](13_thesis_dossier/GEV_THESIS_DOSSIER.html) | 2026-10-02 | The thesis in note form with 11 charts and 26 sources | Same call |
| [14_full_thesis](14_full_thesis/GEV_FULL_THESIS.pdf) | 2026-10-02 | The full thesis file for the team (PDF, and the same text as `GEV_FULL_THESIS.md`): the process, 22 stress tests, valuation inputs, 39 references | Same call. **Start here** |

## Where things stand, as of 2026-10-02 (final)

- **The call:** long, 12 months, to 30 September 2027. Base $1,126 (+14.0%) on analysts' EBITDA at 25x; bear $855; bull $1,341; break-even multiple 21.8x.
- **No provable gap against analysts in either direction.** Twenty-five tests are listed in section 9 of the full thesis file, the last three from an independent second AI that read the corpus and the suppliers' filings on the evening of 2 October. The case rests on arithmetic (forward profit grows about 36% in a year) and on one assumption (the 25x multiple).
- **Bloomberg data** from 1 and 2 October 2026 is in `data/bloomberg/`. It is licensed for academic use: keep it inside the team.

## Where things stand, as of 2026-09-30 late morning (run 09 plus the robustness tasks)

Start with [09_finrobot_overnight/ROBUSTNESS_PACK.md](09_finrobot_overnight/ROBUSTNESS_PACK.md). Both directions were attacked with equal force (nine arithmetic tests in `src/robustness_tests.py`, seven more tasks S01-S07, about $16).

- **Neither direction has an edge on a number.** The short's FY27 gap shrinks to 1-7% under fair changes to the starting point and Wind. The long has no figure above consensus.
- **The outcome turns on the multiple.** The short needs about 26x or lower by late January. The long needs at least 23.4x in September 2027 on GEV's own path, or 20.3x on consensus. Growth-based methods give 17-24x for then.
- **Research lean: long over 12 months, low conviction.** The team decides with its own model.
- **The check that matters most:** Bloomberg FY29 EBITDA consensus. About $15B or more favours the long; about $14B or less favours the short side.

## Where things stood, as of 2026-09-30 early morning (run 09)

[09_finrobot_overnight/MORNING_SUMMARY.md](09_finrobot_overnight/MORNING_SUMMARY.md) has the overnight facts and fixes. Its direction reading is superseded above. The short version:

- **The one number.** FY27 adj EBITDA: Street $9,574M; a straight line on GEV's own guidance gives $8,590M; the research range is $8.6-8.9B. Street FY28 ($13,064M) is 16.6% above the 2028 framework ($11,200M).
- **GEV's own 2028 plan already includes the better-priced 2025 orders** (CEO, BofA, 2026-03-18). So "the Street is above the company's plan" is the cleanest claim.
- **GEV guides low every year**, so a low January guide does not by itself prove the Street wrong. Use the three-zone test in `R07_kill_rules.md`.
- **The Street is not cutting.** FY27 EPS is flat since July; Jefferies raised, not cut.
- **Fixes:** label the segment basis (realigned 2026-01-01); re-pull consensus with a date; use R02's locators for the top 20 numbers.

## Where things stood, as of 2026-09-29 (runs 06-08)

Research facts only. The team writes the memo and chooses every forecast.

- **The Pillar 1 question below is resolved, by a different route.** GEV's RPO note discloses how much equipment backlog converts within 1, 2 and 5 years. Applied to the 31-Dec-2025 book, the two-year window ends exactly on 31-Dec-2027: $64,245M x (69% - 37%) = $20,558M of 2027 revenue, no interpolation. The curve predicted $18.9B of 2025 equipment revenue against $20.9B actual. Code: `src/vintage_model.py`; model tab: "Backlog vintage".
- **What the rebuttal does and does not do (run 08).** GLJ's "3 vs 10-11 points" most likely matches GEV's own slide of year-over-year changes in the *average* backlog margin, not margins on each year's orders. Re-weighting GLJ's own inputs by the conversion schedule closes only about $0.6-1.3B of its $2.0B EBITDA gap, which still leaves it below the Street. The rebuttal moves the bear toward consensus, not above it.
- **The GLJ-day drop was mostly a sector move.** Peers fell 7.6-8.0% the same day; GEV's excess move against a peer basket was about -3%, not statistically significant, and had fully caught up with peers by 09-29.
- **Beat-and-raise is revenue and cash, not margin.** First revenue guides were beaten by +1.3% (FY24) and +4.3% (FY25); adj EBITDA margin finished slightly below the first numeric guide both years; FCF beat by 65-89%. Street FY28 needs the 2028 framework raised by +8.0% revenue and +1.6 pts margin.
- **Valuation.** EV about $250.7B at $962.49. Management's 2028 framework supports the price only at roughly 25-28x year-end-2028 EBITDA; Street 2028 needs about 22-24x. GEV trades near 43x NTM earnings, the bottom of its 34-69x range since the spin, and about 2.2-2.4x the S&P 500.
- **Cash.** The $14,087M figure is sourced after all: it is the Note 9 change in total contract liabilities (includes Prolec). The cash-flow line is $13,695M. Operating cash excluding the contract-liability inflow was negative in FY23, FY24, FY25 and H1'26 (the verifier notes this measure is one-sided: deposits also fund inventory and receivables).
- **The gap the winners' corpus flagged first:** no variant view yet — one number, on one line, for one year, next to a sourced consensus figure.

## The earlier conclusion, as of 2026-09-23 (partly superseded above)

**There is no hidden fact that moves this stock 20%.** Five runs established that, which is a real result but a negative one. The debate is the multiple: GEV trades at about 38x forward earnings against roughly 19x for the S&P 500, so about twice the market.

What the team actually has: a well-verified map of what is and is not true about GEV, nine dead bear arguments that other teams will walk into, a corrected consensus baseline, and a defensible direction with an honest target.

**Resolved by run 06 — kept for the record.** ~~Read this before using run 05's Pillar 1.~~ The rebuttal to GLJ Research's Sell note — that percentage-of-completion accounting already ran the cheap 2024 order vintage through 2025-26 earnings — is a **hypothesis, not an established finding**. Percentage-of-completion fixes the margin rate at contract inception and changes when margin is recognised, not how much. The rebuttal only holds if the 2024-signed contracts are largely complete by the end of 2026, and nobody in the process established that. GLJ covers the name professionally and knows the accounting. **Establish the completion share from the filings before this goes anywhere near the memo.**

Similarly deflated: the "like, 25% down" deposit quote is under-cited rather than novel and has not been personally verified in the transcript; the January cash-flow arithmetic was never checked against whether anyone has published it, and the cumulative target has been raised at both prior December events; the services run-off correction fixes an error one of our own earlier agents made.

## How to read a run folder

- `SYNTHESIS.md` is the final decision report. Start there.
- `DIGEST.md` is every agent's full output in readable form: dossiers, skeptic verdicts, per-share arithmetic, papers read, dead ends.
- `agents.json` is the same content as structured data.
- Runs 02 to 05 also carry their standalone report (`WEDGE_REPORT.md`, `TECHNICAL_WEDGE_REPORT.md`, `MARKET_BRIEFING.md`, `DECISION_MEMO.md`).

## The rest of the project

- Corpus: `data/gev.db` (9,715 filings and 4,189 other sources, 477,621 chunks, 34 companies)
- Everything in this folder is also inside the database. `python src/compile_research.py` adds the research files, the Bloomberg pulls and the reference model as searchable text. Search them with `python src/ask.py search "break-even multiple" --form RESEARCH` (or `--form BLOOMBERG`, `--form MODEL`). In the `chunks` table they carry `kind` = `research`, `bloomberg` or `model`
- Bloomberg text carries `tier` = `licensed`. Leave those rows out of anything that is sent outside the team
- Bloomberg pull workbooks: built by `src/build_bloomberg_pull.py`, `build_bloomberg_pull2.py` and `build_bloomberg_pull3.py`; the filled copies are in `data/bloomberg/`
- Thesis PDF: rebuilt with `python scripts/thesis_pdf/build.py`
- Cleaned financials: `data/financials/` — built by `src/financials_dump.py` from every GEV 10-K and 10-Q via SEC XBRL
- Chart page: `data/financials/index.html` — rebuild with `python src/financials_charts.py GEV`
- Model shell: `data/model/GEV_model_shell.xlsx` — history filled, forecasts are live formulas, assumption cells left empty for the team; consensus pre-filled on the vs Consensus tab; a Backlog vintage tab. Reference only: the submitted workbook is the team's own build
- Vintage exhibit: `python src/vintage_model.py`
- Saving a run: `python src/save_run.py <workflow-output.json> <folder> vintage|winners|brief|journal`
