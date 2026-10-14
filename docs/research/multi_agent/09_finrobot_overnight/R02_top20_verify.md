# Independent two-source verification of the 20 key numbers

_R02_top20_verify — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 04:30:58. Requests 65, input tokens 5658098, output tokens 26659._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GEV: the 20 hand-verify numbers from F01, each checked against two sources with exact locators (research input only)

## 1. Bottom line

- **All 20 values tie to a primary SEC filing, and most tie exactly.** I re-read each one this session in the Q2'26 10-Q (0001996810-26-000148), the Q1'26 10-Q (‑26‑000064), the FY25 10-K (‑26‑000015), and the 4Q25 / 1Q26 / 2Q26 releases (‑26‑000012 / ‑26‑000063 / ‑26‑000147).
- **Several of F01's S2 locators do not exist.** The 2Q26 press release has no income statement cost lines, no Power equipment/services split, no balance sheet, no contract-liability or treasury lines and no NCI. So F01's S2 for rows 3 (NCI), 13 (split), 14 (costs) and 20 is wrong.
  - **Replacement second source:** add the Q1'26 10-Q three-month column to the Q2'26 10-Q three-month column. That ties to H1 within $1M of rounding.
- **Row 5/15 trap: the FY25 Power numbers are on the old segment basis.** Power FY25 of $19,767M / $2,902M comes from the 10-K and the 4Q25 release, both published before the 1-Jan-2026 realignment.
  - Restated H1'25 Power is $9,234M / $1,303M (14.1%), against $9,180M / $1,286M (14.0%) as originally published in 2Q25.
  - Restated full-year FY25 Power was **not found** in the corpus.
- **Consensus rows 10–12 rest on one vendor (MarketScreener) plus close-not-exact checks.** The only MarketScreener page I could open is its **2026-09-04** snapshot: FY27 EBITDA 9,570, revenue 52,731, FY28 13,059. The brief's 9/29 figures are 9,574 / 52,740 / 13,064. The team must re-pull the page and date-stamp it.
- **Row 19 (CSA profit revisions): each figure sits in one filing only.** FY24 −319 is in the FY24 10-K, FY25 −151 in the FY25 10-K, H1'26 −218 in the Q2 10-Q. F01's "10-Q and 10-K" pairing is three different numbers, not two sources for one number. The only partial cross-check is Q1'26 at −89 (Q1 10-Q).
- **Two independent tie-outs strengthen the cash rows:**
  - Treasury stock change 7,057 − 3,385 = 3,672, against the cash-flow buyback line of 3,671 and the release's "4.3 million shares … average price of $854" (≈ $3.67B).
  - EV $247.23B (computed) against stockanalysis's implied $247.34B at $962.49. The match comes from offsetting definitions: vendor cash excludes restricted cash, vendor debt includes leases, and the vendor has no NCI.

## 2. Answer: the verification table

Source key:
- **10Q** = 0001996810-26-000148 (Q2'26 10-Q)
- **10Q1** = ‑26‑000064 (Q1'26 10-Q)
- **10K** = ‑26‑000015 (FY25 10-K)
- **Q2REL** = ‑26‑000147#gevpressrelease2q26.htm
- **Q1REL** = ‑26‑000063#gevpressrelease1q26.htm
- **Q4REL** = ‑26‑000012#gevpressrelease4q25.htm

Page numbers are the filing footers ("2026 2Q FORM 10-Q n").

| # | Number | Value | S1 locator | S2 locator | Exact match? | How to find it by hand (one line) + definition trap |
|---|---|---|---|---|---|---|
| 1 | Close 2026-09-29 | $962.49 | yfinance quote, pulled 2026-09-30 08:27 UTC: 962.49 | Zacks via Yahoo Finance, "GE Vernova (GEV) Gains As Market Dips", 2026-09-29 21:00 UTC: "closed at $962.49, marking a +1.34% move". Check: MarketBeat 9/29 prior close $949.77 × 1.0134 = $962.50 | Exact | Yahoo GEV history, row Sep 29 2026, "Close". **Trap:** the $1,195.94 52-week high is intraday; the record close is lower |
| 2 | Shares outstanding | 266,333,581 at 6/30/26 | 10Q p.7, balance sheet, common stock line ("266,333,581 and 269,529,464 shares outstanding") | stockanalysis.com/stocks/gev/statistics (page cached 2026-09-18): "266.33M" | Exact (to vendor rounding) | Ctrl-F "shares outstanding as of" in the 10-Q. **Trap:** diluted weighted-average is 270M for Q2 and 271M for H1 (10Q p.6 and Note 18 p.18). Do not mix the two in per-share maths |
| 3a | Cash | $13,120M | 10Q p.7, "Cash, cash equivalents, and restricted cash"; also p.8, cash-flow ending balance | Q2REL p.1 bullet "$13.1B cash balance" | Exact / rounded | **Trap:** includes restricted cash. stockanalysis shows $12.72B |
| 3b | Borrowings | $2,849M total; $2,794M long-term; $55M current | 10Q Note 14 p.16, "Total $2,849 … Less current maturities 55" | Same note, arithmetic: notes 600 + 1,000 + 1,000 + other 305 − 56 = 2,849. Independent vendor: stockanalysis debt $3.72B, which **includes ~$0.87B of leases** | Company-only; vendor conflict is a definition difference | The balance sheet shows only 2,794, because the current $55M sits in "All other current liabilities". **Trap:** in the FY25 10-K the Dec-25 LT borrowings ($265M) were inside "All other liabilities" (5,416 vs 5,151 recast) |
| 3c | NCI | $1,158M | 10Q p.7, "Noncontrolling interests 1,158" | **[SINGLE-SOURCE]**. Not in Q2REL (read in full); yfinance null (per D08) | — | Treat as company-only |
| 4 | EV | $247.23B [computed] | Inputs from rows 1–3: 962.49 × 266.3336M = $256,343M; − 13,120 + 2,849 + 1,158 | stockanalysis implied: $256.34B − (12.72 − 3.72) = $247.34B | Close (+0.05%) | Different definitions offset (see §4 A1). A fuller bridge including pension deficit gives ~$250.7B (brief) |
| 5 | FY25 revenue / adj EBITDA / FCF | 38,068 / 3,196 / 3,710 | 10K MD&A "EARNINGS (LOSS)" table (Adjusted EBITDA* 3,196) and segment summary (Total revenues $38,068) | Q4REL p.3, Total Company Results; also SEC XBRL RevenueFromContract… FY25 = 38,068,000,000 | Exact | Ctrl-F "3,196" in the 10-K. **Trap:** adj EBITDA is non-GAAP. MarketScreener's FY25 "EBITDA" equals 3,196, so vendor EBITDA is on the GEV-adjusted basis |
| 6 | H1'26 revenue / adj EBITDA | 20,442 / 2,146 (10.5%) | 10Q p.6 income statement; p.28 "SUMMARY OF REPORTABLE SEGMENTS" (Adjusted EBITDA $2,146) | Q2REL p.2 Total Company Results; also Q1 896 + Q2 1,250 = 2,146 (Q1REL; MarketScreener quarterly row) | Exact | **Trap:** H1 GAAP net income of $5,398M includes the $3,992M Prolec remeasurement gain (Q2REL p.8 note (a)) |
| 7 | FY26 guide | Revenue $45.5–46.5B; adj EBITDA margin 12–14%; FCF $11.5–12.5B | Q2REL p.2 "2026 Guidance" | News article in the corpus, src:2673 (chunk 246278, 2026-07-23), quoting Parks: "$45.5 billion to $46.5 billion … $11.5 billion to $12.5 billion … stayed at 12% to 14%" | Exact | Segments: Power 18–20% organic growth and 17–19% margin; Electrification $14.5–15.0B incl ~$3.1B Prolec at 18–20%; Wind ~−$400M |
| 8 | FY26 margin guide raised | 11–13% → 12–14% | Q1REL p.2 "2026 Guidance": "12%-14%, up from 11%-13%" | Q2REL p.2: "adjusted EBITDA margin* guidance remains 12%-14%"; origin: Q4REL p.2 "11%-13%" | Exact | **Trap:** 11–13% was already stated before Jan-28 (Motley Fool Q4'25 transcript summary says "remains 11%-13%"). The first numeric guide therefore predates Q4REL (Dec-2025 event) |
| 9 | 2028 framework | $56B revenue; 20% adj EBITDA margin; cumulative FCF ≥ $24B; Power 22% / Electrification 22% / Wind 6% | Q4REL p.2 "Multi-Year Financial Outlook": "$56 billion, up from $52 billion … 20% … at least $24 billion" | Motley Fool Q4'25 call transcript, fool.com 2026-01-28: "at least $56 billion … 20% adjusted EBITDA margin target, now including Prolec GE" | Exact | **Trap:** $52B → $56B is Prolec (~$4B), not organic. "At least $56B" (transcript) vs "$56 billion" (release) |
| 10 | Consensus FY27 EBITDA / revenue | 9,574 / 52,740 (brief, MarketScreener 9/29) | MarketScreener /finances/ (only the 2026-09-04 snapshot was reachable: 9,570 / 52,731; 9/29 values per facts.csv CT-01/02) | EBITDA: GuruFocus GLJ wire 2026-09-15 (corpus src:684): "Street's $9.45 billion". Revenue: FactSet mean $52,632M (cnyes 6544296, 2026-07-23) | Close (−1.3% / −0.2%) | **Trap:** vendor, date and definition all matter. MarketScreener EBITDA is GEV-adjusted. GLJ's "38.9x forward EV/EBITDA" is FY26, not FY27 |
| 11 | Consensus FY28 EBITDA | 13,064 | MarketScreener (9/29 per CT-02; the 09-04 snapshot shows 13,059, 21.6%) | No independent full-row vendor found this session. D08's "Motley Fool 60% CAGR" (3,196 × 1.6³ = 13,091) was **not re-found** | **[SINGLE-VENDOR]** | Compare with the plan: 20% × 56,000 = 11,200 → +16.6% |
| 12 | Consensus FY27 EPS | $24.85 | MarketScreener EPS row (facts.csv CT-04, fetched 9/29) | FactSet mean $24.78, median $24.68 (cnyes 6544296, 2026-07-23) | Close (−0.3%) | **Trap:** FY26 EPS is GAAP-type $30.78 (MarketScreener) vs ex-items ~$15.16 (S&P) because of Prolec. Erste's $24.64 (Zolmax 09-01) is one analyst, not consensus |
| 13 | Power H1'26 segment lines | Equipment 3,834; services 6,593; intersegment 22; cost 7,504; SG&A 918; R&D 286; other (100); EBITDA 1,842 (17.63%) | 10Q Note 24 p.23, "Six months ended June 30, 2026" table | Cost lines and EBITDA: Q2REL p.3 Power table (7,504 / 918 / 286 / (100) / 1,842). Split: 10Q1 Note 24 p.21 (1,877 / 3,084 / 11) + 10Q Q2 table p.22–23 (1,957 / 3,509 / 12) = 3,834 / 6,593 / 23 | Exact except intersegment (23 vs 22) and SG&A (917 vs 918), both rounding | The Q2REL does **not** show the equipment/services split. **Trap:** segment-note totals (equipment 11,714; services 8,715) differ from the income statement (11,713; 8,729) because of other revenues and eliminations |
| 14 | Company H1'26 services / equipment sales and cost | Services 8,729 / 5,974; equipment 11,713 / 10,328 | 10Q p.6 income statement, six-month column | 10Q1 p.5 (services 4,084 / 2,843; equipment 5,254 / 4,714) + 10Q Q2 column (4,645 / 3,130; 6,459 / 5,613) = 8,729 / 5,973; 11,713 / 10,327. Revenue also in Q2REL p.7 organic table | Revenue exact; costs ±1 (rounding) | **Trap:** cost of services is **after D&A**, but segment "Cost of revenues" excludes D&A (footnote (b)). Do not subtract one from the other without a D&A adjustment |
| 15 | Power FY25 | Revenue 19,767; EBITDA 2,902 (14.68%); cost 14,627 | 10K Segment Information note, "SEGMENT EBITDA Year ended December 31, 2025" (equipment 6,420 / services 13,072 / intersegment 276) | Q4REL p.3 Power table: 19,767 / 14,627 / 1,836 / 549 / (147) / 2,902 / 14.7% | Exact | **Trap ("r"):** this is the pre-realignment basis. The restated basis lifts H1'25 Power by +$54M revenue and +$17M EBITDA (Q2REL p.6 vs the 2Q25 release). Restated FY25 was not found |
| 16 | Equipment RPO landing in 2027 | $64,245M × (69% − 37%) = $20,558M | 10K Note 9, RPO paragraph: "Equipment-related RPO of $64,245 million of which 37%, 69%, and 97% … within 1, 2, and 5 years" | $64,245M: 10Q MD&A RPO table, Dec-31-2025 column; Q4'25 call (corpus src:2660, chunk 246129): "equipment backlog increasing to $64 billion" | $ exact; % single-document | **Traps:** covers all segments, not Power only; each percentage is rounded (±~$0.64B); 37/69% appears only in the 10-K |
| 17 | Gas GW | Backlog 53 + SRAs 63 = 116 GW; ≥125 GW by YE26 | Q2REL p.1 highlights and Power bullet ("backlog growth from 44 to 53 GW … 56 to 63 GW") | Q2'26 call transcript (corpus src:3161, chunks 251589 / 251621): "from 100 to 116 gigawatts … at least 125 gigawatts" | Exact | **Trap:** SRAs are not RPO; only the 53 GW is backlog |
| 18 | Output ladder | 5 GW/qtr in Q3–Q4'26; early 2027 "very similar"; 6 GW/qtr in H2'27 | stockanalysis Laguna transcript, 2026-09-16 (…/transcripts/745262-…): "We will hit the 5 GW run rate for the third quarter and the fourth quarter … beginning of next year will feel generally very similar" | MarketBeat 2026-09-18, "GE Vernova Eyes $200B Backlog": "increase quarterly production from 5 gigawatts to 6 gigawatts in the second half of 2027" | Exact (MarketBeat is a paraphrase) | GEV-hosted PDF p.4 is a third copy (not re-opened). **Trap:** "20 GW run-rate" ≠ 20 GW shipped in calendar 2027 (~22 GW at most on this ladder) |
| 19 | CSA net unfavorable profit revisions | FY24 −319; FY25 −151; H1'26 −218 | FY24: 10-K 0001996810-25-000011 Note 9 ("$319 million … due primarily to higher costs"). FY25: 10K Note 9 ("$151 million"). H1'26: 10Q Note 9 p.14 ("$218 million") | FY24 also in 424B3 ‑25‑000012 (same text, same publisher). H1'26 partial: 10Q1 Note 9 Q1 = −$89M → implied Q2 −$129M | Each figure is **[SINGLE-DOCUMENT]** | Ctrl-F "changes in estimated profitability". **Trap:** this covers Power CSAs (services), not equipment margin |
| 20 | Contract liabilities / treasury stock | 39,944 (vs 25,774); treasury 7,057 (vs 3,385) | 10Q p.7 balance sheet | 25,774: 10K balance sheet (Dec-31-2025). Treasury change of 3,672: 10Q p.8 cash flow, "Purchases of common stock for treasury (3,671)"; Q2REL p.2, "4.3 million shares … average price of $854" (≈ $3.67B) | Exact; within ±1 | **Trap: three contract-liability "changes"**: balance-sheet delta 14,170; Note 9 text **$14,088M** (not 14,087); cash-flow line **13,695** (p.8). Use 13,695 as the cash line |

## 3. Evidence table (additions beyond §2)

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| E1 | Q2REL contains no full financial statements | Only a total-company table, segment tables, non-GAAP reconciliations and FCF | Q2REL read in full (33,580 chars) | 10Q is the only source of the balance sheet and cost lines | — | H |
| E2 | Segment restatement effect | H1'25 Power: 9,180 / 1,286 (orig.) → 9,234 / 1,303 (restated) | 2Q25 release (‑25‑000132) p.6 organic table | Q2REL p.6 / 10Q p.35 | Conflict by design (recast) | H |
| E3 | Realignment scope | Steam split into Nuclear/Hydro/Gas; part of Electrification Software moved into Gas Power | 10Q1 Note 1 (chunk 13642) | 10Q Note 1 (chunk 5666) | Exact | H |
| E4 | Q3'26 date | 2026-10-28 7:30am ET; stockanalysis still shows an "estimated Oct 21" | Kalkine 2026-09-29 | stockanalysis statistics page (vendor estimate, wrong) | Conflict → use company date | H |
| E5 | Short interest | 8.76M shares, 3.29% of shares outstanding | stockanalysis statistics | brief ~3.3% | Close | M |

## 4. Arithmetic

- **A1, EV.** Market cap = 962.49 × 266.333581 = 256,343.
  - Research bridge: EV = 256,343 − 13,120 + 2,849 + 1,158 = **247,230**.
  - Vendor bridge (stockanalysis): 256,343 − 12,720 + 3,720 = 247,343.
  - Gap: +113 (+0.05%). That is +400 restricted cash, −871 leases, −1,158 NCI, plus rounding.
- **A2, H1 = Q1 + Q2 tie-outs.**
  - Power: equipment 1,877 + 1,957 = 3,834; services 3,084 + 3,509 = 6,593; cost 3,638 + 3,866 = 7,504; EBITDA 811 + 1,031 = 1,842.
  - Company: services cost 2,843 + 3,130 = 5,973 (vs 5,974); equipment cost 4,714 + 5,613 = 10,327 (vs 10,328).
- **A3, margins.** 1,842 / 10,449 = 17.63%. 2,902 / 19,767 = 14.68%. 3,196 / 38,068 = 8.40%. 2,146 / 20,442 = 10.50%.
- **A4, RPO landing in 2027.** 64,245 × (0.69 − 0.37) = 20,558. Rounding band: each percentage ±0.5 pt, so ±1 pt ≈ ±642.
- **A5, treasury.** 7,057 − 3,385 = 3,672 vs cash-flow 3,671. Shares: 12,663,683 − 8,397,266 = 4,266,417 ≈ "4.3 million". 4.2664M × $854 = $3,644M. The ~$28M gap is consistent with the average price being rounded and timing.
- **A6, contract liabilities.** 39,944 − 25,774 = 14,170 (balance sheet) vs 14,088 (Note 9 text) vs 13,695 (cash flow). The gap between the balance sheet and the cash-flow line is mostly Prolec's acquired balance plus FX (inferred, not disclosed).
- **A7, implied Q2'26 CSA revision.** −218 − (−89) = −129.
- **A8, FY28 check.** 3,196 × 1.6³ = 13,091 vs 13,064 (+0.2%). The underlying "60% CAGR" source was not re-verified.

## 5. General question bank items answered along the way

- **G20 (single-source numbers and definition traps).**
  - Single source: NCI; CSA revisions; RPO percentages; FY28 EBITDA consensus (one vendor); restated FY25 Power (not found).
  - Definition traps: restricted cash; leases in debt; diluted vs outstanding shares; old vs restated segment basis; cost of services after D&A vs segment cost before D&A; three contract-liability "changes"; GAAP-type vs ex-items FY26 EPS.
- **G24 (deposits).** The H1 deposit line is $13,695M against H1 OCF of $10,680M (10Q p.8), while $3,671M went to buybacks.
- **G25 (what was checked by hand).** Every row in §2 was checked this session against the filing text. The consensus rows depend on vendor pages; only the MarketScreener 09-04 snapshot was reachable.

## 6. What would change this

- A 9/29 MarketScreener re-pull that differs from 9,574 / 52,740 / 13,064 → update rows 10–11.
- A restated FY25 Power figure (GEV IR recast file, linked from Q2REL p.3 "can be accessed here") → rows 5 and 15, and the margin-path series (FY25 14.68% may become ~14.7–14.8%; not computed).
- The GEV Laguna PDF p.4 wording differing from the stockanalysis copy → row 18.

## 7. Disagreements with the master brief and F01

1. **The S2 locators F01 gives inside Q2REL do not exist** for rows 3 (NCI), 13 (equipment/services split), 14 (costs) and 20 (balance-sheet items). Use the Q1 10-Q + Q2 three-month sums, or the 10-K for Dec-25 balances.
2. **The Note 9 contract-liability change is $14,088M, not $14,087M** (10Q Note 9 p.14).
3. **FY25 Power figures need an "old basis" tag.** The brief's FY23–FY25 margin series (9.88 / 12.51 / 14.68%) sits on the pre-2026 segment basis, while H1'26 (17.63%) is on the new basis. The size of the H1'25 recast (+0.1 pt) suggests the effect is small, but it is not zero.
4. **The FY26 "first" margin guide of 11–13% predates the Jan-28 release** (it is described there as maintained). F01 is right that it was raised.
5. **F01's row 19 pairing** (10-Q Note 9 / 10-K Note 9) does not give two sources for any single figure.

## 8. Open items

- **Restated FY25 Power** (revenue, EBITDA, equipment/services split): GEV IR "2025 segment financial information" recast file (gevernova.com/investors).
- **MarketScreener 9/29 values:** re-pull /finances/ with a timestamp. The EPS row was not visible in my snapshot.
- **A second vendor for the FY27–FY28 EBITDA row:** Visible Alpha, FactSet or Bloomberg. Nothing free was found.
- **GEV Laguna PDF p.4** (ladder) and p.10 ("'29 and '30") need a re-read of the original.
- **NCI $1,158M:** no second source. Check the SEC XBRL frame "MinorityInterest" for 2026-06-30. It comes from the same filing, but it is machine-readable.
