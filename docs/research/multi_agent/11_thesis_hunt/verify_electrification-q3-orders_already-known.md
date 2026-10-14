# Check: ALREADY KNOWN OR BAD DATA — candidate `electrification-q3-orders`

_Research input only: facts, arithmetic, sources. No memo sentences, no forecast choices. Bloomberg data cited as "Bloomberg, 2026-10-01" (academic licence, keep inside the project folder)._

**Verdict: does not survive.** The numbers reproduce, but (1) the Street figure is thin and undated, (2) the input remark is public and widely syndicated, and (3) there is an ordinary explanation that removes most of the gap: the Street's second-half figure equals the CEO's remark applied to the trailing-four-quarter non-data-centre run-rate.

## 1. Reproduction (all recomputed from the primary files)

| Item | Value | Source |
|---|---|---|
| Street Q3'26 Electrification orders | mean 6,498.1; low 5,774.9; median 6,306.7; high 7,498.4 | Bloomberg, 2026-10-01: `06_modl.xlsx` row "Orders > Electrification"; `segment_quarterly.json` key `Orders||Electrification|2026 Q3` |
| Street Q4'26 / H2'26 | 7,492.0 / 13,990.1 | same JSON |
| Orders implied by the Street's RPO path | 46,998.4 - 44,563 + 3,880.7 = 6,316.1 (RPO low / high give 5,730 / 7,329) | same files |
| H1'26 orders | 7,112 + 6,347 = 13,459 | 8-K exhibits 0001996810-26-000063, -000147 (gev.db `documents`) |
| Data-centre orders | Q3'25 $0.4B; 9M'25 about $0.9B; FY25 "over $2B" (so Q4'25 about $1.1B); Q1'26 $2.4B; Q2'26 $2.7B; H1'26 share 5,100 / 13,459 = 37.9% | Q3'25 call (gev.db source 3796); Q4'25 call (source 2660); Q1'26 release; Q2'26 call (source 3161) |
| Conference wording, 2026-09-16 | data-centre orders "almost 40%" of segment orders in H1; "probably more like 20% of our Electrification orders in 3Q and 4Q; while growing the backlog, both the Electrification backlog and the data center backlog"; host asked whether the lumpiness is data-centre-specific, answer "That's right"; India HVDC (almost $1.5B) "won't cut in as an order until the fourth quarter"; "continue to grow our backlog in a very healthy way in both 3Q and 4Q in Electrification"; non-data-centre business also called lumpy | company-hosted transcript PDF, gevernova.com `ge-vernova-morgan-stanley-laguna-conference-2026-transcript.pdf` (fetched 2026-10-01) |
| Candidate arithmetic | 4,130 / 0.80 = 5,162; 5,162 / 6,498 - 1 = -20.6% | reproduces |

Electrification orders by quarter ($M, as first reported): Q1'24 3,571; Q2'24 4,823; Q3'24 2,510; Q4'24 4,786; Q1'25 3,393; Q2'25 3,338; Q3'25 5,110; Q4'25 7,424; Q1'26 7,112; Q2'26 6,347 (earnings-release 8-K exhibits in gev.db).

## 2. (a) Is the consensus figure robust? No.

- **Thin.** The export shows only mean / low / median / high for this row; every broker cell is blank and there is no count or date. The four statistics rule out 3 or 4 contributors (the mean cannot be matched); at least 5. A clean-decimal check (mean x n) points to 6 or 12. For comparison the same sheet's revenue mean is exactly 28 brokers (11,992.892857 x 28 = 335,801) and EBITDA 13 (or 26).
- **Skewed.** Mean is 3.0% above median. Against the median the candidate's centre is -18.1%, against the low -10.6%.
- **Stale relative to the remark.** Bloomberg ConsensusHistory: FY26 EBITDA mean 6,313.3 (09-11), 6,314.3 (09-18), 6,314.3 (09-25), count 36 throughout; FY27 revenue 52,951 / 52,949 / 52,949. Annual numbers were not touched in the two weeks after 09-16, so a division orders line was almost certainly not either. Bulk sheet: 12 of about 43 brokers carry a recommendation date on or after 09-16 (8 of them 09-29 to 10-01); most others are dated 07-22/23 (the Q2 report). Recommendation date is only a proxy for estimate date.
- **Not independently cross-checked.** The RPO-implied 6,316 comes from the same broker models, so it is not a second source. No other vendor (Visible Alpha, FactSet, company-compiled consensus) was found for this line by web search on 2026-10-01; one search connector was rate-limited.

Reading: 6,498 is the average of roughly half a dozen models last set around the July report. It is a weak stand-in for what investors expect on 28 October.

## 3. (b) Is the idea already stated? The input is fully public; the number itself was not found in print.

- Company-hosted transcript (gevernova.com), plus third-party copies (stockanalysis.com, Investing.com) on 09-16.
- Syndicated summary 09-18 to 09-21 (MarketBeat, Yahoo Finance, Longbridge, Transcript Daily; in gev.db as sources 681 and 3750): data centres "closer to 20% in the third and fourth quarters".
- Investing.com summary 09-16: data centres "should represent about 20% in the third and fourth quarters as other parts of the business catch up" (their gloss, not in the transcript).
- TIKR blog (after 09-18): lists "data center order run rate is guided to moderate in the second half" as a known risk.
- Not found: any broker note or preview printing a Q3 Electrification orders figure, or the "non-data-centre / 0.8" arithmetic.
- The remark was made in answer to a question from the host broker's covering analyst, in front of a buy-side audience. It is not a number "the company does not disclose".

## 4. (c) Has the stock moved on it?

- Bloomberg PricePositioning: 882.81 (09-15) to 925.09 (09-16) = +4.79% on the day of the remark; 987.45 on 10-01 (+6.7% since 09-16, +11.9% since 09-15). The day's headline was the "$200B backlog very early in 2027" comment; the data-centre moderation did not weigh on the price.
- No evidence that this line moves the stock on report days (candidate's own step 8: orders have not separated good days from bad).

## 5. (d) Ordinary explanation: base period for non-data-centre orders

Non-data-centre orders = segment orders less disclosed data-centre orders ($M):

| Quarter | Orders | Data centre | Non-data-centre | Note |
|---|---|---|---|---|
| Q3'25 | 5,110 | 400 | 4,710 | includes $1.6B Saudi grid-stability order; no Prolec |
| Q4'25 | 7,424 | about 1,100 | about 6,324 | no Prolec |
| Q1'26 | 7,112 | 2,400 | 4,712 | Prolec for two months (Prolec + FX about 850: 7,112 - 3,366 x 1.86) |
| Q2'26 | 6,347 | 2,700 | 3,647 | Prolec full quarter (about 900: 6,347 - 3,283 x 1.66) |
| Average, last 4 quarters | | | 4,848 | |
| Average, H1'26 | | | 4,180 (candidate uses 4,130) | |

Q3'26 = base / (1 - share):

| Base (non-data-centre) | 15% share | 20% share | 25% share | 20% case vs Street mean / median |
|---|---|---|---|---|
| Q2'26 alone, 3,647 | 4,291 | 4,559 | 4,863 | -29.8% / -27.7% |
| H1'26 average, 4,130 (candidate) | 4,859 | 5,162 | 5,507 | -20.6% / -18.1% |
| Q3'25, 4,710 | 5,541 | 5,888 | 6,280 | -9.4% / -6.6% |
| Last-4-quarter average, 4,842 | 5,696 | 6,052 | 6,456 | -6.9% / -4.0% |
| Q4'25, 6,324 | 7,440 | 7,905 | 8,432 | +21.7% / +25.3% |

**The Street's second half reconciles to the remark.** Street H2 orders 13,990 x 80% = 11,192 non-data-centre; less the India HVDC order (1,500, Q4) = 9,692 = 4,846 a quarter, against a last-4-quarter non-data-centre average of 4,848. Implied data-centre orders 1,400 a quarter (below the H1 pace of 2,550, above every 2025 quarter). So "20% share + India in Q4 + non-data-centre at its one-year average" gives the Street's H2 number to within 0.1%. The -20.6% appears only if the base is the two most recent quarters, in which non-data-centre orders fell from 4.7B to 3.6B.

Other points that bear on the base:
- Lumpiness of the line itself: absolute quarter-on-quarter change has averaged 35% over the last nine quarters (median 35%; range 2% to 91%). Using the prior quarter as the forecast, mean absolute error over the last six quarters is 24%; using the trailing-4-quarter average, 35%. A 20% gap is inside one ordinary quarterly swing.
- "Grow the backlog in a very healthy way": at 5,160 the segment backlog adds about 1.3B (book-to-bill 1.33), the smallest add since Q2'25 (about 1.1B); at the Street it adds 2.4-2.6B (Q2'26 added 2.1B). The wording does not settle it but leans away from the low centre.
- New products (MV-UPS launch order, more EMS) "will start to cut into the order book in the second half" (same transcript): upside to data-centre orders not in the H1 base.
- Q2 call guide for Q3: "continued solid equipment orders with healthy margins" (no number).
- No delivery slip, FX, reclassification or acquisition-accounting item is needed to explain the gap; Prolec is already in both H1'26 quarters. Year on year, the Street is +27% reported on 5,110 (about +10% after about 0.9B of Prolec); 5,160 would be +1% reported and an organic decline of about 17%.

## 6. Corrected figures

| Item | Candidate | After this check |
|---|---|---|
| Street | 6,498 mean | 6,498 mean / 6,307 median; at least 5 (probably 6) brokers, undated, almost certainly set before 09-16 |
| Arithmetic value | 5,160 centre (4,500-5,900); second lens up to 7,300 | two defensible bases give 5,160 (H1'26 base) and 6,050 (4-quarter base); midpoint about 5,600; full band 4,560-7,900 |
| Gap vs Street mean | -20.6% | -20.6% (H1 base) to -6.9% (4-quarter base); midpoint about -14%; vs median -18% to -4% |
| Error band on the value | not stated as one number | about -20% / +40% around 5,600 (roughly +/-30%); wider than the gap |

## 7. Why it fails this check

1. Street figure is not solid: thin, undated, skewed, pre-remark, no second vendor.
2. The input is public, syndicated within two days, and delivered at a broker conference; the stock rose 4.8% that day.
3. Ordinary explanation: the Street's H2 figure already equals the remark applied to the one-year non-data-centre run-rate. The gap is a choice of base period on a line whose normal quarterly swing is about 35%.
4. Candidate's own flag stands: no effect on revenue, EBITDA or cash in the horizon.

What would still be usable: as a dated side-test only. 28 Oct release, Electrification segment table, "Orders". Below 5,775 = under every broker in the Bloomberg sample; 6,050 or more = the 4-quarter base was right and there was no gap.

## 8. Files and queries used

- `data/bloomberg/GEV_Pull_2026-10-01/06_modl.xlsx`, `01-eeo-company-specific.xlsx`, `segment_quarterly.json`
- `data/bloomberg/GEV_bloomberg_pull_filled_2026-10-01.xlsx` sheets ConsensusHistory, PricePositioning, Bulk
- `data/gev.db` (read-only): `documents` (8-K/EX earnings releases Q1'24-Q2'26), `sources` ids 681, 3750, 1747, 823, 2369, 686, 3796, 2660, 3161; `chunks_fts` search "Laguna"
- Web (Exa, 2026-10-01): company transcript PDF; stockanalysis.com and Investing.com copies; MarketBeat / Longbridge / Transcript Daily summaries; TIKR blog; 24/7 Wall St. A second search connector returned a rate-limit error; Firecrawl was not authorised in this session.
