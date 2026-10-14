# More primary evidence: utility dockets on gas-turbine pricing 2024-2026

_E08_dockets — FinRobot lead agent + GEV corpus tools, hosted-llm, generated 2026-09-30 04:09:15. Requests 47, input tokens 3423561, output tokens 25558._

> Research input only. The team writes every memo sentence and chooses every forecast number.

# GE Vernova gas-turbine and combined-cycle pricing by contract year: utility dockets, SEC filings and developer disclosures, 2024-2026

## 1. Bottom line

- **No public source gives a GE turbine-only price by contract year.** Every docket and SEC datapoint found is an all-in plant budget that includes EPC, owner's costs and often escalation to a later in-service date. The GE-linked all-in series runs about $1,400/kW for a 2024 GE order, about $2,150-2,330/kW for 2025 reservations and contracts, and about $3,230-3,790/kW for a 2026-approved GE 7HA.03 block (a preliminary range). [S1: KY PSC Case 2025-00045 Tummonds rebuttal p.4-5, 2025-07-18] [S2: GridLab "New Reality of Power Generation" Table 2 p.10, Sep-2025] [S3: Oglethorpe Q2'26 Investor Briefing, SEC 0000788816-26-000050, slides 4/8, 2026-08-18]
- **New finding: a second same-owner, same-configuration GE pair.** Oglethorpe Power has two GE 7HA.03 1x1 combined-cycle projects:
  - Smarr CC: two 1x1 blocks, 1,425 MW, GE OEM contract "signed earlier in 2025", $3.3B = **$2,316/kW**, in service 2029.
  - New CC: one 1x1 block, 713 MW, approved Q2 2026, $2.3-2.7B = **$3,226-3,787/kW**, in service 2033.
  - The change is **+39% to +64% nominal**. That includes about 4 years of extra escalation to the later in-service date, and the 2033 budget is preliminary. [S1: Oglethorpe Q3'25 Investor Briefing, SEC 0000788816-25-000023, slide 4, 2025-11-13] [S2: Oglethorpe Q2'26 Investor Briefing, 0000788816-26-000050, slides 5/8] Both sources are Oglethorpe documents; the 2033 figure is [SINGLE-SOURCE].
- **Only company-attributed number for GE's slice:** on the Q3'25 call the CEO agreed that "$2,500/kW" all-in combined-cycle cost with GE capturing about 30% is "a practical illustration." That implies about **$750/kW** of GE scope in October 2025. For comparison, the RPO-derived backlog $/kW upper bound is $575 at Q3'25 and $741 at Q2'26. [S1: GEV Q3'25 call transcript, corpus src:3796] [S2: Motley Fool Q3 2025 transcript]
- **Other 2025-26 GE-named or OEM-cited datapoints** fall inside the $2,150-2,330/kW band:
  - JEA, GE 7HA.03 reservation Aug-2025: "up to" $1.57B / 675 MW = $2,326/kW.
  - Santee Cooper/Dominion Canadys: about $5B / 2,180 MW = $2,294/kW. The CEO described it as "$1,200 → $2,300" per kW. OEM not named.
  - All of these sit well below the 2026 no-reservation market indications of $2,800-3,200/kW.
  - [S1: Power Engineering 2025-09-03] [S2: Florida Times-Union via AOL 2026-04-14] [S3: Post and Courier 2025-12-14] [S4: SC PSC Docket 2025-323-E joint notice]
- **Escalation clauses: no GE customer contract found anywhere that discloses an index-escalation clause.** The contract-term evidence points both ways:
  - A GE reservation paid "to lock in firm pricing for the equipment" (LG&E/KU Brown 12).
  - Reservations where price is set later: Maxim's deposit amount is finalized in the definitive contract; Entergy's exclusivity deal "does not establish final pricing"; MC6 showed "updated commercial pricing" after the June 2026 power-island signing.
  - GEV's own 10-K flags fixed-price risk. Its 2024 S-1 says it was "improving protections embedded in customer agreements to protect against inflation."
  - [S1: KY PSC Order 2025-10-28 p.10] [S2: GEV 10-K FY25 0001996810-26-000015 Item 1A] [S3: S-1/A 0001193125-24-131304]
- **Direction for the vintage debate (research reading, team decides).** GE-linked all-in cost rose about 55-65% between 2024 and 2025 decisions, and a further about 40-64% nominal (about +19% to +45% after a team-chosen 3-4%/yr escalation to in-service date) into 2026. That backs a large price step between the pre-2025 and 2025-26 vintages. But plant cost cannot be split into GE price versus EPC inflation without an assumed turbine share (decomposition grid in section 4).

---

## 2. The findings in detail

### Q1. Datapoint table, beyond LG&E/KU

Plant-level unless noted. Some rows were verified in earlier tasks tonight (see facts.csv TP-xx); rows marked **NEW** were added in this task.

| # | Owner / docket or filing | Decision or contract date | Project, MW, COD | OEM | Cost; $/kW (basis) | Escalation / reservation terms | Sources |
|---|---|---|---|---|---|---|---|
| 1 | LG&E/KU, KY PSC 2022-00402 / 2025-00045 | GE MC5 order announced 2024-04-11 (estimate 2022-23) | Mill Creek 5, 645 MW, 2027 | GE 7HA.03 | $902M → $913.4M; **$1,398-1,416** (all-in) | none disclosed | Tummonds rebuttal p.5; GridLab T2 ($1,427 on 640 MW) |
| 2 | LG&E/KU, KY PSC 2025-00045 | $25M GE unit reservation before Feb-2025 | Brown 12, 645 MW, 2030 | GE | $1.383B; **$2,144** | $25M (1.8%) "to lock in firm pricing for the equipment" | Tummonds p.4; KY PSC Order p.10; GridLab T2 |
| 3 | LG&E/KU, KY PSC 2025-00313 | reservation 2025-08-27; power island signed 2026-06-23 | Mill Creek 6, 645 MW, 2031 | GE | $1.415B; **$2,194**; "trending above" after signing | "updated commercial pricing"; "protracted negotiations with GEV" | MC6 Updates #2/#3; KY PSC Order p.80 |
| 4 **NEW** | Oglethorpe Power (SEC filer 788816) | GE OEM contract "signed earlier in 2025"; selection announced 2025-05-20; EPC 2025-09-26 | Smarr CC, 2×1x1, 1,425 MW, mid-2029 | GE 7HA.03 | $3.3B; **$2,316** (budget, all-in) | power island bought directly by owner; EPC excludes power island and transformers | Q3'25 briefing slides 4-5; Q2'26 briefing slide 5; GEV press release 2025-05-20 (OEM) |
| 5 **NEW** | Oglethorpe | approved by members Q2-2026 | New CC, 1x1, 713 MW, 2033 | GE 7HA.03 | $2.3-2.7B; **$3,226-3,787** (preliminary range) | none disclosed | Q2'26 briefing slide 8 [SINGLE-SOURCE] |
| 6 **NEW** | Oglethorpe | approved Q2-2026 | New CT, 209 MW, 2032 | GE 7F.05 | $525-625M; **$2,512-2,990** (simple cycle) | none disclosed | Q2'26 briefing slide 8 [SINGLE-SOURCE] |
| 7 **NEW** | Oglethorpe (comparator) | re-baselined 2026 | Talbot 7 CT, 240 MW, 2029 | Siemens SGT6-5000F | $440M; **$1,833** | "Re-Baselined Budget" (no prior figure given) | Q2'26 briefing slide 6 [SINGLE-SOURCE] |
| 8 **NEW** | JEA (FL municipal; FL PSC need filing planned) | board vote 2025-08-26; non-refundable GE payment by end-Aug-2025 | St. Johns CC, ~675 MW, 2032 | GE 7HA.03 (pictured and named) | "up to" $1.57B; **~$2,326** | non-refundable reservation payment, amount undisclosed; lock-in to avoid "risk of cost escalation" | Power Engineering 2025-09-03; Times-Union/AOL 2026-04-14 (MW from Power Engineering only) |
| 9 **NEW** | Santee Cooper / Dominion SC, SC PSC 2025-323-E | boards approved 2025-10-31; PSC approved 2026-05-14 | Canadys, 2,180 MW net, ~2032-33 | not named (GE, Siemens and MHI cited generically) | ~$5B; **~$2,294**; original $2.5-3.0B (~$1,150-1,380) | $120M for turbine "down-payments" | Post and Courier 2025-12-14; SC PSC Exhibit D notice; Dominion 10-K 0001193125-26-063120 (2.2 GW, 2033) |
| 10 **NEW** | Dominion Virginia Power, VA SCC | approved 2025 | Chesterfield ERC, 944 MW simple cycle, 2029 | not named | $1.5B ex-financing; **$1,589** (GridLab: $1,470M, $1,557) | none | Dominion 10-K 0001193125-26-063120; GridLab T1 |
| 11 **NEW** | NRG, Texas Energy Fund (ERCOT) | loan signed 2025-09-26 | Cedar Bayou 5, 721 MW, 2028 | not named | $936M; **$1,298** | TEF loan $562M (60%) at 3% | Utility Dive 2025-09-29; TX Governor release 2025-09-26 |
| 12 **NEW** | East Kentucky Power Coop | announced 2024-11-21 | Cooper CCGT, 745 MW, 2030 | not named | $1,317M; **$1,768** | none | GridLab T2 [SINGLE-SOURCE] |
| 13 | Entergy (MS / LA / AR / TX), Evergy (MHI), Duke IN/SC | 2024-2026 | various | Entergy vendor unnamed; Evergy MHI | $1,583-2,773 (see TP-15 to TP-25) | Entergy exclusivity "does not establish final pricing" | Entergy and Duke 10-Qs/10-K; KCC 2025-07-07 |
| 14 **NEW** | Georgia Power, GA PSC 56298/56310 | certified Dec-2025 | Bowen 7-8, Wansley 10-11, McIntosh 12 (3,693 MW) | not disclosed | $/kW redacted; intervenor says CC costs "more than doubled" vs 2025 IRP | none public | Metz testimony (Synapse); Southern 10-K 0000092122-26-000006 (MW/COD) |

Searched with no usable price: Xcel (GE Strategic Alliance 2026-02-03, five F-class reserved), Duke Person County (GE; NCUC costs confidential), NIPSCO GenCo ($7B total including transmission and BESS; OEM not confirmed), AEP I&M Rockport (1,520 MW, cost not captured), TVA (buys from all three OEMs, now ordering "five years before delivery"), APS, PacifiCorp, Ameren (Castle Bluff simple cycle $900M/800 MW = $1,125/kW; GridLab T1; OEM not named), Homer City (GE 7HA.02 ×7; the "$10B" in GridLab covers power *and* data centres per the GE release wording, so it is excluded as a definition trap), and Maple Creek (GE 7HA.03, Oct-2025, no price).

### Q2. How much have GE-linked prices risen, by contract year?

**All-in, GE-linked only** (rows 1-5, 8):

| Contract / decision year | $/kW all-in | n |
|---|---|---|
| 2024 order (MC5) | 1,398-1,416 | 1 |
| 2025 reservation / contract | 2,144 / 2,194 / 2,316 / 2,326 (median ~2,255) | 4 |
| 2026 approval (Oglethorpe 1x1, preliminary) | 3,226-3,787 | 1 |

Steps:
- 2024 → 2025: **+53% to +66%**.
- 2025 → 2026 (Oglethorpe pair): **+39% to +64% nominal**, or about **+19% to +45%** after removing 4 years of escalation at 3-4%/yr (the rate is the team's choice).

**GE's scope specifically**, three rough, differently defined anchors:
- CEO-endorsed about $750/kW (30% × $2,500, Oct-2025).
- Backlog $/kW upper bound $575 → $741 (+29%, Q3'25 → Q2'26; includes mix and non-gas equipment).
- WoodMac turbine-only about $600/kW by end-2027 (+195% since 2019).

Management's own new-versus-backlog pricing statements: "10-20 points" (Q4'25/Q1'26) and ">20%" for H1'26 orders versus 4Q'25 orders. Part of that is aeroderivative mix (TP-32; evidence_lanes TP-13 note).

**Research estimate (team chooses):** GE equipment price on 2025 contracts was plausibly +60% to +160% above 2024-vintage orders, depending on turbine share and non-turbine inflation (grid in section 4). 2026 contracts add roughly +10% to +45% more in real terms. No filing isolates this.

### Q3. Is there evidence of escalation clauses in customer contracts?

**No disclosed index-escalation clause in any GE customer contract was found.** The evidence found:

| Point | Where | What it says |
|---|---|---|
| (a) | LG&E/KU Brown 12, KY PSC Order p.10 | $25M reservation paid "to lock in firm pricing for the equipment." Fixed price at reservation, not escalation. |
| (b) | MC6 | GT and generator reserved Aug-2025; "Negotiate & Refresh Balance of OEM Scope" Nov-2025 to Jun-2026; cost "trending above… due to… updated commercial pricing." Price was reset on part of GE's scope at conversion. |
| (c) | Maxim Power 7HA.02 reservation (Feb-2026) | Non-refundable deposit "amount and exact payment date to be finalized" in the definitive contract (EveryTicker 2026-02-09; not independently confirmed). |
| (d) | Entergy exclusivity (10-K FY25) | "does not establish final pricing." |
| (e) | GEV itself | 10-K FY25 Item 1A: "contracts that commit to a fixed price well before project completion." Item 1: Power "adjusted product and service pricing in line with market demand, inflation." S-1/A 2024-05-06: "improving protections embedded in customer agreements to protect against inflation." |
| (f) | Tariffs | GEV said it would pass through or renegotiate where "change in law" provisions apply (Power Engineering 2025-04-23). |

**Reading.** Older fixed-price contracts appear to carry limited upside repricing. 2025+ contracts carry some GEV-described inflation protection of unknown form. Reservations sometimes fix price and sometimes defer it.

---

## 3. Evidence table

| # | Claim | Value | S1 | S2 | Agreement | Conf. |
|---|---|---|---|---|---|---|
| 1 | Smarr CC budget, GE 7HA.03, 1,425 MW | $3.3B; $2,316/kW | Oglethorpe Q3'25 briefing, 0000788816-25-000023, slide 4 | Oglethorpe Q2'26 briefing, 0000788816-26-000050, slide 5 | exact (same publisher). **Conflict:** ENR 2026-01-30 "$2.5B", Power Engineering 2026-01-14 "$2 billion". Likely EPC-only or older figures; SEC budget preferred | H (budget) / M (why press differs) |
| 2 | Smarr GE OEM contract signed 2025 | "earlier in 2025" | Q3'25 briefing slide 4 | GEV/OPC press release 2025-05-20 (selection) | close | H |
| 3 | Oglethorpe 2033 1x1 CC, GE 7HA.03 | $2.3-2.7B / 713 MW; $3,226-3,787/kW | Q2'26 briefing slide 8 | none found | [SINGLE-SOURCE]; also searched ENR, OPC site | M |
| 4 | Oglethorpe 2032 7F.05 CT | $525-625M / 209 MW | Q2'26 briefing slide 8 | none | [SINGLE-SOURCE] | M |
| 5 | JEA CC cost and GE reservation | ≤$1.57B, board 2025-08-26, non-refundable by end-Aug-2025 | Power Engineering 2025-09-03 | Times-Union/AOL 2026-04-14 | exact | H (MW: M, single) |
| 6 | Canadys cost | ~$5B, 2,180 MW; "$1,200 → $2,300/kW" | Post and Courier 2025-12-14 | SC PSC 2025-323-E notice (MW); Dominion 10-K (2.2 GW, 2033) | close; $ from press only | M |
| 7 | Chesterfield ERC | $1.5B / 944 MW simple cycle | Dominion 10-K 0001193125-26-063120, Item 1 | GridLab T1 ($1,470M) | close (−2%) | H |
| 8 | Cedar Bayou 5 | $936M / 721 MW | Utility Dive 2025-09-29 | TX Governor 2025-09-26 | exact (MW) | H |
| 9 | CEO: $2,500/kW, ~30% GE share | "practical illustration… I agree" | corpus transcript src:3796 | Motley Fool Q3'25 transcript | exact | H |
| 10 | Brown 12 reservation locks firm pricing | $25M | KY PSC Order 2025-10-28 p.10 | facts.csv VF-03 / Bellar Direct p.11 (cited in order) | exact | H |
| 11 | MC6 cost above CPCN after GE power island | direction only | MC6 Update #3, 2026-07-31 p.2 | MC6 Update #2 (GEV negotiations) | consistent | H |
| 12 | GEV fixed-price risk and inflation-protection language | text | 10-K FY25 Item 1A/Item 1 | S-1/A 0001193125-24-131304 | consistent (same issuer) | M |
| 13 | Entergy vendor pricing not fixed | text | Entergy 10-K FY25 0000065984-26-000174 | Entergy 10-Q Q3'25 | exact | H |
| 14 | Maxim reservation deposit set in the definitive contract | text | EveryTicker 2026-02-09 | Forbes 2026-04-17 (mentions reservation, not terms) | partial | L |
| 15 | Georgia Power CC cost "more than doubled" | redacted | Metz testimony GA PSC 56298/56310 p.31 | Gas-plant coverage 2025-12-24 (corpus src:2894) | consistent | M |
| 16 | ~$25M down payment per train (industry) | $25M | projectfinance.law 2025-08-01 | KY PSC Order p.10 (Brown 12 $25M) | close | M |

---

## 4. Arithmetic

**$/kW computations (cost ÷ MW):**
- Smarr: 3,300/1,425 = **2,316**.
- New CC: 2,300/713 = **3,226**; 2,700/713 = **3,787**; midpoint 2,500/713 = 3,506.
- 7F.05 CT: 525/209 = 2,512; 625/209 = 2,990.
- Talbot 7: 440/240 = 1,833.
- JEA: 1,570/675 = **2,326**.
- Canadys: 5,000/2,180 = **2,294**; original range 2,500-3,000/2,180 = 1,147-1,376.
- Chesterfield: 1,500/944 = 1,589.
- Cedar Bayou 5: 936/721 = 1,298.

**Step changes:**
- 2024 → 2025 GE-linked: 2,144/1,398 = 1.534; 2,326/1,398 = 1.664. Range **+53% to +66%**.
- Oglethorpe pair: 3,226/2,316 = 1.393; 3,787/2,316 = 1.635. Range **+39% to +64%**.
- Escalation-adjusted (COD 2029 → 2033, 4 years): 1.03^4 = 1.126 and 1.04^4 = 1.170. Low end 1.393/1.170 = 1.19 → +19%; high end 1.635/1.126 = 1.45 → +45%. The escalation rate is the team's choice.

**GE slice:**
- 0.30 × 2,500 = **$750/kW** (Oct-2025).
- Backlog upper bound: 741/575 = 1.289 (+29%, Q3'25 → Q2'26) (facts RV-25).

**Plant-to-equipment decomposition** (from prior verified lane, reused):
- Formula: g = (P − (1−t)(1+n))/t − 1.
- For P = 1.60 (midpoint of 2024 → 2025 GE-linked):
  - t = 30%, n = 35%: g = (1.60 − 0.945)/0.30 − 1 = **+118%**.
  - t = 30%, n = 50%: (1.60 − 1.05)/0.30 − 1 = +83%.
  - t = 25%, n = 20%: (1.60 − 0.90)/0.25 − 1 = +180%.
- All three input values (t, n, P) are the team's choice.

---

## 5. General question bank items answered

- **G11 (physics).** TVA now orders turbines five years before delivery and seven years before operation, versus three and five historically (Chattanooga Times Free Press 2026-07-28; consistent with GEV's 2031-32 slot sales at Laguna 2026-09-16).
- **G12 (timing).** Oglethorpe buys the power island directly, outside the EPC contract, with 2029 COD on a 2025 contract. That means about 4 years from contract to COD; GEV's revenue timing for this contract is not disclosed. So 2025-priced GE content ships about 2027-29.
- **G20 (definition traps):**
  - Homer City's "$10B" includes data centres.
  - Canadys: the "$/kWh" in the press quote means $/kW.
  - The CEO's "30%" GE share likely covers the full GE scope (GT, ST, HRSG, generators), not the turbine alone. WoodMac's $600/kW is turbine-only.
  - Oglethorpe press figures ($2B / $2.5B) differ from its SEC budget ($3.3B).
- **G21 (evidence if the price step is wrong).** A flat same-owner pair would falsify it; the only flat pairs are Entergy MS (0%) and Duke (+5%), neither OEM-named. The two GE-named same-owner pairs (LG&E/KU and Oglethorpe) both show large steps.

## 6. What would change these findings

- The Oglethorpe 2033 figure is preliminary. A 10-K or 10-Q budget below about $2.6B/713 MW would pull the 2026 step toward +15-25% nominal.
- An MC6 60-day update giving a post-power-island dollar figure would show GE's 2026 repricing on part of the scope directly.
- A docket or contract exhibit showing a GE price-adjustment formula (PPI or metals index) would overturn "no escalation clause found".
- A disclosed Maxim or JEA reservation fee as a share of contract value would confirm or refute the pattern of paying about 2% for a firm price.

## 7. Disagreements with the master brief

- The brief (section 6) says framework customers show flat 2024-25 costs and treats LG&E/KU as the one GE pair. **There is now a second GE-named same-owner pair (Oglethorpe), and it shows a further large step into 2026.** The flat Entergy MS and Duke pairs are not OEM-named, so they should carry less weight against GE-specific pricing than the brief's framing implies.
- Minor: the brief's "$25M reservation… lock in firm pricing" stands, but Maxim, Entergy and MC6 show that not every reservation fixes price. The brief's single-case reading should be treated as one contract type among several.

## 8. Open items

1. The Oglethorpe 10-K FY25 and 10-Q Q2'26 (filed 2026-03-27 and 2026-08-13) may give the GE power-island contract value and terms: search "GE Vernova", "power island", "escalat".
2. The JEA FL PSC need-determination filing (planned June 2026) should state the reservation fee and MW.
3. The SC PSC 2025-323-E testimony should name the Canadys OEM and any escalation terms.
4. The AEP I&M Rockport IURC filing (Jul-2026) needs its cost and OEM.
5. NIPSCO GenCo (IURC Cause 46322 and follow-on CPCN) needs its OEM and per-plant cost.
6. The Georgia Power trade-secret $/kW figures remain unavailable in public dockets.
7. The Duke Person County NCUC figures are confidential.
8. The Q3'25 call date for the CEO's "$2,500/kW" remark: the corpus source is undated and the Motley Fool URL carries a 2026 date. The content (29 GW SRA / 33 GW firm backlog) matches Q3'25; the exact date still needs confirming from GEV IR.
