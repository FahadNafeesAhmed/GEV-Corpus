# Verify (REPRODUCE): equipment-revenue-vs-rpo-schedule

_AI-assisted research input only: facts, arithmetic, sources. No memo sentences, no forecast chosen for the team. Bloomberg figures: "Bloomberg, 2026-10-01", licensed for academic use, keep inside the project folder._

Check type: recompute every number in the candidate from the primary files. Result: **the arithmetic reproduces; the headline gap needs to be cut from +8.7% to about +7% (range +1% to +11%) and the checkable floor from +4.5% to about +2.7-4.5%.** Survives the 5% test narrowly, on the equipment-revenue line only.

## 1. Sources used

| Item | File | Locator |
|---|---|---|
| Street quarterly equipment, services, total revenue, EBITDA | `data/bloomberg/GEV_Pull_2026-10-01/segment_quarterly.json` (same as rows 22-31 of `01-eeo-company-specific.xlsx`) | keys `Total Revenue\|Power\|Equipment` etc., 2026 Q3 to 2028 Q2 |
| Street Q3 2026 mean / low / high / median | `06_modl.xlsx` | rows "Revenue: Power Equipment" etc. |
| RPO schedule sentences | `gev.db` chunks | accessions listed in section 3 |
| Equipment / services revenue by quarter | `data/financials/gev_facts_long.csv` | `RevenueFromContractWithCustomerExcludingAssessedTax`, `ProductOrServiceAxis=ProductMember` / `ServiceMember`; Q4 = FY less nine months |
| Prolec equipment revenue | 10-Q Q1 2026 (0001996810-26-000064) and Q2 2026 (0001996810-26-000148), "Equipment and services organic revenues" table | "Less: Acquisitions 469" (Q1); "834 ... 1,303" (Q2, six months) |
| Segment equipment RPO | 10-Q Q2 2026 MD&A segment tables | Power 39,261; Wind 8,197; Electrification 40,589 |
| FY26 guide | `mgmt_guidance` table, 2026-07-22 | "$45.5-$46.5 billion, up from $44.5-$45.5 billion" |

Passage quoted (10-Q Q2 2026, 0001996810-26-000148, RPO note): "Equipment-related RPO of $87,821 million of which 36%, 65%, and 97% is expected to be recognized within 1, 2, and 5 years, respectively, and the remaining thereafter. (2) Services-related RPO of $88,463 million of which 16%, 54%, 79%, and 92% ..."

## 2. Street side, recomputed (Bloomberg, 2026-10-01)

| $M | Q3 2026 | Q4 2026 | Q1 2027 | Q2 2027 | Four quarters |
|---|---|---|---|---|---|
| Equipment (sum of three division rows) | 7,482.1 | 8,339.2 | 6,675.4 | 7,748.3 | **30,245.0** |
| Services (sum of three division rows) | 4,485.2 | 5,629.2 | 4,536.3 | 5,139.1 | 19,789.8 |
| Total revenue (consolidated consensus) | 11,992.9 | 13,914.6 | 11,143.2 | 12,968.1 | 50,018.8 |
| Sum of division totals | 11,997.3 | 14,016.3 | 11,254.5 | 13,055.1 | 50,323.2 |
| EBITDA | 1,671.8 | 2,499.7 | 1,810.4 | 2,228.2 | 8,210.0 |

By division (four quarters): Power equipment 10,873.8, Wind 5,830.0, Electrification 13,541.1. H1 2027 equipment 14,423.7 (Power + Electrification 12,145.9). All match the candidate.

Definition problems found (these change the Street figure, not the company figure):

| Way of measuring "Street equipment, four quarters" | $M | Schedule-only gap | Gap at x1.04 |
|---|---|---|---|
| Division equipment rows, means (candidate's figure) | 30,245 | +4.5% | +8.7% |
| Consolidated total less services rows (50,019 - 19,790) | 30,229 | +4.6% | +8.8% |
| Rows less intersegment sales (Bloomberg Q2'26 actual rows sum to 6,490; reported consolidated equipment is 6,459) | 30,100 | +5.0% | +9.2% |
| Rows scaled to medians (Q3'26 medians 2,433 + 1,813 + 3,369 = 7,615 vs means 7,482, +1.8%; only Q3 has medians) | 30,781 | +2.7% | +6.8% |
| Total less services, with Electrification services row cut by 331 / 481 (the electrification lens's correction) | 30,560 / 30,710 | +3.5% / +3.0% | +7.6% / +7.1% |

- The equipment and services rows do not add to the division totals: Power is short by 277, Wind by 97, Electrification over by 85 (different broker samples per row). Contributor counts for the split rows are not visible on this export; broker-level cells are blank.
- Q3'26 Electrification equipment: low 2,301, high 3,848, median 3,369 against a mean of 3,299. Low outliers pull the mean down, so the median reading is a fair alternative.
- **Corrected Street value: $30.2B as printed; $30.1-30.8B across definitions; mid about $30.5B.**

## 3. Company side, recomputed

Schedule at each balance-sheet date (equipment RPO x one-year share) and what followed. Actual = consolidated equipment revenue, next four quarters. Prolec removed where the backlog date is before 2026-02-02.

| Backlog date | Accession | Equipment RPO | 1-yr share | Scheduled | Next 4 quarters | Street quarters in it | Ratio | Ratio ex-Prolec |
|---|---|---|---|---|---|---|---|---|
| 12/31/23 | 0001193125-24-066951 (S-1) | 40,478 | 51% | 20,644 | 18,952 | 0 | 0.918 | 0.918 |
| 3/31/24 | 0001996810-24-000008 | 42,210 | 45% | 18,994 | 19,532 | 0 | 1.028 | 1.028 |
| 6/30/24 | 0001996810-24-000067 | 41,561 | 47% | 19,534 | 20,232 | 0 | 1.036 | 1.036 |
| 9/30/24 | 0001996810-24-000083 | 42,069 | 46% | 19,352 | 20,822 | 0 | 1.076 | 1.076 |
| 12/31/24 | 0001996810-25-000011 | 43,047 | 44% | 18,941 | 20,934 | 0 | 1.105 | 1.105 |
| 3/31/25 | 0001996810-25-000073 | 45,478 | 45% | 20,465 | 21,991 | 0 | 1.075 | 1.052 |
| 6/30/25 | 0001996810-25-000133 | 49,712 | 42% | 20,879 | 23,556 | 0 | 1.128 | 1.066 |
| 9/30/25 | 0001996810-25-000160 | 54,092 | 41% | 22,178 | 25,158 | 1 | 1.134 | 1.033-1.037 |
| 12/31/25 | 0001996810-26-000015 | 64,245 | 37% | 23,771 | 27,534 | 2 | 1.158 | 1.021-1.030 |
| 3/31/26 | 0001996810-26-000064 | 75,924 | 38% | 28,851 | 28,956 | 3 | 1.004 | 1.004 |
| 6/30/26 | 0001996810-26-000148 | 87,821 | 36% | 31,616 | 30,245 | 4 | 0.957 | 0.957 |

- Seven fully reported windows, ex-Prolec: mean 1.040, sd 0.060, median 1.052. Six post-spin: mean 1.060 (candidate says 1.061), sd 0.028, min 1.028, max 1.105. Street's 0.957 is 1.4 sd below the seven-window mean and 3.7 sd below the post-spin mean. Matches.
- Dollar uplift over schedule, ex-Prolec: -1,692; +538; +698; +1,470; +1,993; +1,057; +1,374.
- Prolec equipment in unreported quarters assumed 850-1,000 a quarter (not disclosed); affects only the two partly reported rows.
- 87,821 x 0.36 = 31,615.6. Rounding of the share (35.5-36.5%) gives 31,176-32,055. Matches.
- Multipliers: x1.028 = 32,501 (+7.5%); x1.040 = 32,880 (+8.7%; candidate prints 32,884); x1.050 = 33,196 (+9.8%); x1.061 = 33,544 (+10.9%; candidate prints 33,527); x1.105 = 34,935 (+15.5%); x0.918 = 29,023 (-4.0%). Differences are rounding only.

Other items reproduced:

| Candidate item | Recomputed | Verdict |
|---|---|---|
| H1 2026 revenue 20,442; H2 guide 25.1-26.1B; Street H2 25,908 | 20,443 (quarters) / 20,442 (10-Q six months); 25,057-26,057; 25,907.5 | ok |
| Street H2'26 equipment 15,821; guide-implied 14,944-15,944 | 15,821.3; 14,943-15,943 with Street services, 15,212-16,212 with services at +8.4% | ok, range slightly wider |
| Remainder for H1'27 15,795 vs Street 14,424, +9.5% (+6.5% to +12.5%) | 15,794 vs 14,424 = +9.5% (+6.5% / +12.6%) | ok |
| H1'27 needs +35% y/y vs Street +23% | +34.8% vs +23.1% | ok |
| June windows: H2 took 57% of the scheduled year | 57.0% (2024), 56.7% (2025); Street has 50.0%; guide 47-51% | ok |
| Wind conversion: Street 71.1%; history 58.5-69.3% | 58.5, 62.5, 63.3, 65.9, 67.4, 69.3, 64.9% on reported external equipment | ok; maximum is 69.3%, so "never above 67.6%" is wrong |
| Power + Electrification scheduled 25,786 / 26,288 / 26,804 (+5.6 / +7.7 / +9.8%) | same; +3.8% at a 35.5% share | ok |
| Wind break-even 87.9% | 87.8% | ok |
| P+E statistic 0.866, 1.050, 1.062, 1.130, 1.170, 1.111 (1.077), 1.184 (1.096); Street 0.947 | 0.866, 1.050, 1.062, 1.130, 1.170, 1.111 (1.077), 1.184 (1.094); 0.947 | ok |
| Street converts 27.7% of Power and 33.4% of Electrification equipment RPO | 27.7%, 33.4% (history 39.9-54.5% and 34.1-41.2%) | ok |
| One-year scheduled amount 28,851 to 31,616, +2,765 (min +1,945); Street window +1,289 | +2,764; +1,946; +1,289 | ok |
| Total form: 45,770 scheduled; realised ratios 1.070 ... 1.165; Street 1.093 | 45,770; 1.070, 1.158, 1.141, 1.169, 1.167, 1.127, 1.167 (mean 1.143); 1.093 | ok |
| Services: Street 22.4% of services RPO (history 21.3-22.6%); 1.398x the 16% schedule (history 1.24-1.365x); +11.1% on trailing 17,811 | 22.4% (21.3-22.6%); 1.398 (1.239-1.365); +11.1% | ok |
| Equipment gross margin 12-13%, services 32% | Q2'26 13.1% / 32.6%; H1'26 11.8% / 31.6%; incremental equipment gross margin H1'26 on H1'25 18% | ok |
| Street four-quarter EBITDA 8,210; H1'27 4,038 | 8,210.0; 4,038.5 | ok |
| Year two: Street 35,137 vs 25,468 scheduled | 35,136.7; 25,468 | ok |
| Street Q4'26-Q3'27 equipment 31,314; FY27 equipment 32,383 | 31,314.3; 32,383.1 | ok |
| Flat price at 24.6x needs NTM EBITDA 10,353, +6.4% on 9,727 | 254,694 / 24.6 = 10,353; +6.4% | arithmetic ok; the peer regression itself was not re-fitted |
| 2026-07-22 share move -8.7% | 1,078.81 to 985.03 = -8.7% (prices table) | ok |

## 4. What the reproduction changes

1. **Street figure is soft by about 2%.** Printed 30,245; 30.1-30.8B on other fair readings. The schedule-only gap is +2.7% to +5.0% (and +1.3% to +3.6% if the 36% is really 35.5%). The floor does not clear 5% on any reading except one.
2. **The uplift ratio is drifting down on reported data, so 1.04-1.06 is not the neutral centre.**
   - 9/30/25 window: three reported quarters ex-Prolec are 16,373 = 73.8% of the schedule. The 9/30/24 window stood at 77.2% at the same point and finished at 1.076. Same final-quarter share (30.4%) gives about 1.04.
   - FY26 window (12/31/25 schedule 23,771): H1 ex-Prolec is 10,410 = 43.8% of the schedule, against 48.0% at the same point in the FY25 window (finished 1.105) and 37.8% in FY24 (finished 0.918).
   - GEV's own FY26 guide puts FY26 ex-Prolec equipment at 0.99-1.05x that schedule (guide 45.5-46.5B, services 18.6-18.8B, Prolec 3.0-3.2B). Midpoint about 1.02.
   - A centre of about 1.03 (range 1.00-1.07) fits these better than 1.040-1.061.
3. **Corrected central figures.** Company-side value 31,616 x 1.03 = about $32.6B (schedule-only 31.6B; x1.07 = 33.8B; one-sigma band about 31.2-34.0B). Against Street 30.2-30.8B that is **+5.8% to +7.7%, centre about +7%**. The candidate's +8.7% uses the printed mean rows and x1.04.
4. **Error band on the company-side value: about +/-4.5%.** Parts: share rounding +/-1.4% (hard limits); uplift ratio sd 2.8% post-spin, 6.0% with the pre-spin window; six overlapping post-spin windows are about two independent years. Downside tail is longer: a repeat of 0.918 gives 29.0B, 4% below the Street.
5. **Size on other lines.** Total revenue: +2.1B to +2.6B on 50,019 = about +4% to +5% (the total-revenue form gives +3.1% to +7.0%). EBITDA: +2.1-2.6B x 12-20% = +0.25-0.5B = +3% to +6% of 8,210; if Street services are 2-6% too high (-0.4 to -1.2B at about 32% gross margin) the net is about -1% to +5%.

## 5. Errors and loose ends in the candidate text

- "Wind has never exceeded 67.6%": the reported maximum is 69.3% (3/31/25 window). The candidate already flags this.
- 12/31/25 window ex-Prolec ratio is 1.021-1.030, not 1.028-1.032 (depends on the Prolec assumption for Q3-Q4 2026).
- The 12/31/23 window (0.918) is a pre-spin schedule (51% / 77% / 100%, cut to 45% / 71% / 93% one quarter later) and includes the Steam Power nuclear activities sold to EDF in Q2 2024 (about $3.9B of RPO removed, 10-Q Q2 2024, 0001996810-24-000067). It is a weak comparator in both directions.
- The equipment rows in Bloomberg include intersegment sales; the company schedule is consolidated. Effect about -0.5% on the Street figure.
- Not reproduced: the 11-peer regression behind 24.6x; the -0.22 correlation of revenue surprise with report-day move; the bottom-up H1'27 count of $14.4-15.2B. None sits on the candidate's own line.
- Not testable from the files: whether "Street below schedule" was also true at earlier dates (ConsensusHistory holds only FY27 and FY28 revenue, no quarterly or division history).

## 6. Result

| | Candidate | Corrected |
|---|---|---|
| Street, equipment revenue Q3'26-Q2'27 | $30,245M | $30,245M printed; $30.1-30.8B by definition; mid $30.5B |
| Company-side value | $31.6B floor; $32.9B at x1.040 | $31.6B floor ($31.2-32.1B); about $32.6B at x1.03; band $31.2-34.0B |
| Gap | +8.7% (floor +4.5%) | about +7% (range +1% to +11%); floor +2.7% to +4.5% |
| Error band on company-side value | "about as large as the gap" | about +/-4.5% |
| Survives (gap at least about 5% and above its error band) | | Yes, narrowly, on equipment revenue only. No on the schedule-only floor. No on EBITDA (about +3% to +6%, possibly near zero after services). |

Working script: recomputation ran from `segment_quarterly.json`, `gev_facts_long.csv` and `gev.db` (read-only); no project file other than this one was written.
