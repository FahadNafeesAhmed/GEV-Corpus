# Run 09 morning summary (2026-09-30)

_AI-assisted research input only. The team writes every memo sentence and chooses every forecast number and the direction._

> **Superseded on direction, same day.** Later stress tests and seven more tasks (S01-S07) found that the short's estimate gap is fragile and that the short needs the multiple at its one-year low by January. The research lean moved to a 12-month long with low conviction. Read [ROBUSTNESS_PACK.md](ROBUSTNESS_PACK.md) first. The facts and fixes below still stand; the "only the short side has an edge" reading does not.

## What ran

- 49 research tasks on a hosted LLM, 00:04 to 05:02, 1,669 model requests.
- Estimated spend: about $72.48 on the model API and $1.56 on Exa (301 searches).
- Every task had to give two independent sources per number or tag it `[SINGLE-SOURCE]`.
- Start with `F01_final_synthesis.md`, then read this page for what phase 3 (R01-R08) changed.

## The one number

| | FY27 adj EBITDA | Source |
|---|---|---|
| Street consensus | **$9,574M** (18.15% of $52,740M) | MarketScreener 09-29; second vendor ~$9.45B |
| GEV's own path (straight line, FY26 guide midpoint to the 2028 framework) | **$8,590M** | computed from company guidance (R03) |
| Research range (two builds, twelve framings) | **$8.6-8.9B** | D01A/B, V01-V13 |

- FY28 shows the same gap: Street **$13,064M** against the 2028 framework's **$11,200M** (+16.6%). The FY28 Street figure has only one source.
- Lead with total FY27 EBITDA against published consensus. Do not lead with Power margin: the "Street needs Power 21.7-23.5%" figure is a back-solve, and the only published Power figure is GLJ's 20.7% (R01).

## What phase 3 changed

1. **Street above plan is the cleanest claim.** At BofA on 2026-03-18 the CEO said the 2025 order margins arrive in "'27, '28" with some trickling into "'29 and '30", and that this drives the 20% 2028 target. So GEV's own plan already includes the better 2025 orders, and the Street is above that plan anyway (R04).
2. **The "'29 and '30" quote we used is about 2026 orders, not 2025 orders** (R04, R06).
3. **The January test is weaker than we thought.** GEV has guided low every year: actuals beat the guide by 1.75% (FY24), 10.2% (FY25) and on current numbers about 12% (FY26). So a low January guide does not prove the Street wrong (R06, R07).
   - Guide at or above ~$9.4B (revenue midpoint x margin midpoint): thesis wrong. About 35%.
   - Guide between ~$8.55B and ~$9.4B: ambiguous. About 45%.
   - Guide at or below ~$8.55B: thesis right. About 20%.
   - About half the time January will not settle it. A second dated test is needed: the 2028 framework, in January or at the spring 2027 capital markets day.
4. **Price stops do not fit this edge.** A $1,079 short stop is hit by random movement alone 62-70% of the time before January. A stop that noise hits only a third of the time sits at $1,250-1,290, which is above the 52-week high. A -15% to -30% stop on a 12-month long is hit 45-76% of the time. Exit on dated events and size the position instead (R07).
5. **The Street is not cutting.** FY27 EPS is flat since July (+0.3%). No major broker cut an FY27 estimate or target from 09-14 to 09-29. **Jefferies raised ($1,155 to $1,185 on 09-11), it did not cut.** Revisions cluster in the day or two after each report, so expect most of any drift at the 10-28 Q3 report. If the gap closes before the January guide, most of the short's expected value goes: +4.3% if none closes, about +1.9% at half, about -0.6% if it all closes (R08).
6. **The long has no estimate edge.** Every build is below consensus, so a 12-month long is roll-forward plus multiple. Expected return is about +1% to +4%, roughly a coin flip. Its best catalyst is the spring 2027 capital markets day (both earlier framework resets were raises; the stock rose +5% and +16% those days). New demand evidence: slots sold for 2032 delivery, and 12 GW of added 2030-31 supply being contracted at premium prices (R05).
7. **The Q3 report on 10-28 is a checkpoint, not a verdict.** The company margin guide is what moves the stock: margin raises gave +14-16% days, and the July report (revenue and cash raised, margin guide held) closed -8.7% (R07).

## Where the direction stands

The research does not pick the direction. The team does, by a rule written down before the model is run. The two cases on the evidence:

| | Short into the January guide | Long over 12 months |
|---|---|---|
| Estimate edge | Yes: research range 7-10% below Street FY27 | None |
| Expected return (research) | about +4.3%, falling to about -0.6% if the Street closes the gap first | about +1% to +4% |
| Chance of profit | about 56% | about 50% |
| What pays it | January guide at or below ~$8.55B, or a de-rating | multiple holds; spring 2027 framework raise |
| What kills it | January guide at or above ~$9.4B | framework not raised; multiple compresses from 28x |

The winners' corpus says a pitch needs a variant view on one number next to consensus. On this evidence, only the short side has one. The open question for the team is whether that edge can pay inside the competition window.

## Fixes to carry into the model and memo

- **FY25 Power numbers are on the old segment basis.** GEV realigned segments on 2026-01-01. Restated H1'25 Power is $9,234M revenue / $1,303M EBITDA (originally $9,180M / $1,286M). No restated full-year FY25 was found. Label the basis on every column (R02).
- **Consensus rests on one vendor.** Re-pull MarketScreener, plus one second vendor, and write the date on the tab (R02).
- **Some second-source locators in F01 do not exist.** Use the Q1'26 plus Q2'26 10-Q three-month columns instead. R02 lists the exact page for each of the 20 key numbers.
- **Equipment margin: use the trend, not the level.** The +30 point turnaround since FY23 is solid. The H1'26 level (about 0%, band -9% to +11%) rests on four undisclosed assumptions. Appendix only (R01, R03).
- **CFO timing.** Ken Parks presents the Q3 and January calls. Claire McDonough becomes CFO on 2027-01-01 (R06).
- **The FY26 first margin guide was raised (11-13% to 12-14%).** "Never beat the first margin guide" is out of date (R01).
- **Street FY27 free cash flow is about $7.4B, down 38% on FY26.** Two vendors agree. It is a likely negative headline in the same January release (R06).
- **Unresolved: a December 2026 analyst day?** One weak source says Morgan Stanley expects one. Check GEV's events page (R03).

## Citation audit (local check)

A local 8B-model auditor tried to open every cited source and check the number (`citation_audit/SUMMARY.md`).

- It could open only about a fifth of the citations. The rest point to vendor pages that block automated reading, call transcripts, or earlier run outputs. So "0 verified" on most rows means "the auditor could not open it", not "wrong".
- Of the citations it could open, 68 supported the claim, 118 were unclear and 44 were contradicted on first reading. On the tie-break, 30 of the 44 became "supported" and only 2 stayed contradicted.
- Both double-contradicted cells are the same claim: the $13.7B contract-liability inflow (D03). Run 08 traced this figure to the cash-flow line, so the auditor probably matched a different period. Hand-check it anyway.
- **Treat the audit as a triage list, not a verification.** The real checks are R02 (the top 20 numbers, all tied to SEC filings) and the team's own hand-check of `../08_evidence_brief/FACTS.csv`.

## Today's plan

1. Re-pull consensus, with a date stamp. Check the GEV events page for a December event.
2. Write the direction rule on paper before building anything. Say which result means short, which means long, and which means "no edge, pick the defensible side".
3. Build the model from `E03_model_inputs.md`. The team types every input; `GEV_model_shell.xlsx` is reference only.
4. Hand-check the top 20 numbers using R02's locators.
5. Run the rule and decide. Then write the memo, and disclose the AI-assisted research.

## Files to open first

`F01_final_synthesis.md` · `R01_redteam_final.md` (errata) · `R07_kill_rules.md` · `R08_consensus_drift.md` · `E03_model_inputs.md` · `R02_top20_verify.md` (locators) · `R03_exhibit_data.md` (chart series)
