# FinRobot investment-committee memo on GEV — AI-GENERATED, research input only, NEVER copy into the submission

_P5_ic_memo — FinRobot pipeline `ic_memo`, generated 2026-09-30 00:15:03_

> **AI-GENERATED. Research input only. Do not copy any of this text into the submission — the competition prohibits AI-generated submission content.**


## Situation Overview

# GE Vernova Inc. (GEV): Situation Overview

**Data as of:** 2026-09-30 (yfinance). **Reporting and quote currency:** USD.
**Period basis:** The provider labels the data TTM, but it flags `period_basis_unknown`. Both `period_end` and `ttm_quarter_ends` are empty. All income-statement figures below are labeled "TTM (provider-reported, unverified)".

---

## 1. Company Snapshot

| Item | Value | Source / Derivation |
|---|---|---|
| Company | GE Vernova Inc. (NYSE: GEV) | Provided |
| Sector / Industry | Industrials / Specialty Industrial Machinery | Provided |
| Domicile | United States (not an ADR) | Provided |
| Market cap | USD 256.34B | Provided |
| Shares outstanding | 266.33M | Provided |
| Implied share price | ~USD 962.49 | Market cap ÷ shares; matches TTM P/E 27.25x × TTM EPS USD 35.32 |
| Total debt | USD 3.72B | Provided |
| Total cash | USD 12.72B | Provided |
| Net cash | USD 9.00B | Cash – debt |
| Enterprise value | ~USD 247.34B | Mkt cap + debt – cash (preferred and NCI not reported, assumed nil) |
| Recent news flow | None returned by provider | yfinance news feed empty |

GEV is a large-cap industrial with a net cash balance sheet. Net cash is about 3.5% of market cap, so EV sits slightly below equity value.

---

## 2. Data Quality Flags (read before using any multiple)

1. **Period basis unverified.** No TTM quarter-end dates are provided. Revenue, EBITDA, net income and cash flow may not share the same four-quarter window.
2. **Net income exceeds EBITDA.** TTM net income is USD 9.53B against TTM EBITDA of USD 3.93B. That can only happen with large non-operating items, such as a gain on disposal, a revaluation gain or a tax benefit. **TTM EPS and TTM P/E are therefore not representative of recurring earnings.**
3. **Forward EPS is below trailing EPS.** Forward EPS is USD 25.13 versus TTM EPS of USD 35.32, a −28.9% drop. This supports the view that the TTM earnings are one-off-inflated.
4. **Forward net income vs. TTM operating profit.** Forward EPS × shares implies forward net income of about USD 6.69B. That is roughly 2.2x TTM operating income of about USD 3.09B and 1.7x TTM EBITDA. There are three possible explanations, which must be reconciled in the next step:
   - consensus expects a very steep margin ramp;
   - forward EPS still includes non-operating items; or
   - the TTM EBITDA field is stale or defined narrowly.
5. **Dividend yield units.** The `dividend_yield` field reads 0.21. Cross-check: USD 2.00 DPS ÷ ~USD 962.49 price = 0.21%. The field is a **percentage (0.21%)**, not 21%.
6. **Missing fields.** D&A, operating income (absolute), interest expense, tax expense, R&D, SG&A and beta are null. Two items are derived below: operating income from the operating margin, and D&A as EBITDA minus EBIT, which is approximate.

---

## 3. Scale and Profitability (TTM, provider-reported)

| Metric | Value | Derivation |
|---|---|---|
| Revenue | USD 41.37B | Provided |
| Gross profit | ~USD 8.51B | 20.57% × revenue |
| Gross margin | 20.57% | Provided |
| Operating income (EBIT) | ~USD 3.09B | 7.47% × revenue |
| Operating margin | 7.47% | Provided |
| EBITDA | USD 3.93B | Provided |
| EBITDA margin | 9.49% | EBITDA ÷ revenue |
| Implied D&A | ~USD 0.84B (2.0% of revenue) | EBITDA – EBIT (approximate) |
| Net income | USD 9.53B | Provided (includes non-recurring items; see §2) |
| Net margin | 23.04% | Distorted by non-operating items |
| ROE | 82.58% | Provided. Inflated by the TTM net income spike and a small equity base |
| Book equity | ~USD 11.96B | BVPS USD 44.895 × shares |

**Read-across:** On an operating basis, GEV is still a **high-single-digit margin business**, with a 7.5% EBIT margin and a 9.5% EBITDA margin. The 23% net margin and 83% ROE are artifacts of non-operating items. They should not be used as peer-comparison anchors for returns.

---

## 4. Cash Flow and Balance Sheet (TTM, provider-reported)

| Metric | Value | Derivation |
|---|---|---|
| Operating cash flow | USD 14.14B | Provided |
| Capex | USD 1.58B (3.8% of revenue) | Provided |
| Free cash flow | ~USD 12.56B | OCF – capex |
| FCF margin | 30.35% | FCF ÷ revenue |
| OCF / EBITDA | 3.6x | Cash conversion well above 100% |
| FCF / net income | 1.32x | |
| FCF yield (on market cap) | 4.90% | FCF ÷ market cap |
| Net cash | USD 9.00B | |
| Dividend per share | USD 2.00 | Payout ratio 5.73% of TTM EPS (provided) |

**Key observation:** OCF at 3.6x EBITDA cannot come from earnings alone. The cash flow statement is most likely benefiting from a large **working-capital inflow**, such as customer advances or progress payments on backlog. This is a hypothesis to verify against the cash flow statement, which was not provided. If it is correct, TTM FCF overstates steady-state FCF, and the 4.9% FCF yield is not a clean valuation anchor.

---

## 5. Valuation Snapshot (as of 2026-09-30)

| Multiple | Value | Basis |
|---|---|---|
| EV / TTM Revenue | 5.98x | USD 247.34B ÷ USD 41.37B |
| EV / TTM EBITDA | 62.99x | USD


## Financial Analysis

DCF: $190.59/share (WACC 8.3%). LBO: 0.3× MOIC, -21.5% IRR (5yr hold).


## Investment Thesis

# GE Vernova Inc. (GEV): Investment Thesis

**Recommendation: SELL**
**Price target: Withheld (null).** Only one valuation method is usable, so there is no cross-check. The direction comes from the market-implied gap.
**Indicative 12-month value range:** USD 145–344/share, from the DCF sensitivity grid (WACC 6.31–10.31%, terminal growth 2.0–4.0%). DCF base case is USD 190.59/share.
**Current price:** USD 962.49 (as of 2026-09-30).
**Currency / basis:** USD. Income figures are "TTM (provider-reported, unverified)" unless noted otherwise.

---

## 1. Headline Call

GEV trades at USD 962.49/share. The only intrinsic valuation computed upstream, a 10-year DCF at 8.3% WACC and 3.0% terminal growth, gives USD 190.59/share. That puts the price about 5.05x the DCF value, implying roughly −80% to base.

Even the most generous cell in the sensitivity grid (6.31% WACC, 4.0% terminal growth) gives USD 344.32/share. That is still about 64% below the current price.

The market is valuing GEV as if its operating earnings power will be several times what the business has produced to date. We think the headline valuation metrics obscure the size of that bet:
- The 27.25x TTM P/E is flattered by one-off income.
- The 4.9% FCF yield is flattered by working-capital inflows.

Stated cautiously, the market is pricing near-flawless execution of a margin ramp that TTM operating data does not yet support. We rate the stock **SELL**.

We withhold a point target because the DCF is the only real valuation method, and its margin input (4.7% EBITDA) is likely conservative relative to TTM (9.49%) and consensus. The LBO is not a valuation cross-check (see §4). An honest point estimate would require corroboration we do not have. The direction, however, is unambiguous: the gap is too large to close by adjusting the DCF assumptions within the provided sensitivity range.

---

## 2. Business and Model Overview

- **What GEV is:** A U.S.-domiciled large-cap industrial (Industrials / Specialty Industrial Machinery) with USD 256.34B market cap and 266.33M shares outstanding.
- **Segments and end markets:** The segment, end-market and geographic split was **not supplied** in the upstream data, so we do not break revenue down by business line.
- **Model characteristics visible in the data:**
  - **Low-to-mid margin, capital-light manufacturing.**
    - Gross margin: 20.57% (TTM).
    - EBIT margin: ~7.47% (TTM, ~USD 3.09B).
    - EBITDA margin: 9.49% (TTM, USD 3.93B).
    - Capex: USD 1.58B, 3.8% of TTM revenue.
  - **Cash conversion far above earnings.**
    - OCF of USD 14.14B (TTM) is about 3.6x TTM EBITDA.
    - The situation overview hypothesizes a large working-capital inflow, such as customer advances or progress payments on backlog. This is consistent with a long-cycle, order-backed equipment business.
    - The cash flow statement was not supplied, so this remains a hypothesis.
  - **Balance sheet:**
    - Net cash of USD 9.00B (cash USD 12.72B less debt USD 3.72B), about USD 33.8/share.
    - The dividend is small: USD 2.00 DPS, a 0.21% yield and a 5.73% payout of TTM EPS.
- **Growth history:** Trailing 4-year revenue CAGR is 8.7%, per the DCF input provenance.

---

## 3. Financial Profile: Separating Signal from Noise

| Metric | Reported (TTM) | Read-through |
|---|---|---|
| Revenue | USD 41.37B | Clean anchor |
| EBITDA | USD 3.93B (9.49%) | Operating reality: high single-digit margin |
| Net income | USD 9.53B (23.04%) | **Exceeds EBITDA.** Must include large non-operating items |
| TTM EPS / P/E | USD 35.32 / 27.25x | **Not representative** of recurring earnings |
| Forward EPS | USD 25.13 (−28.9% vs TTM) | Forward P/E ≈ 38.3x (USD 962.49 ÷ USD 25.13) |
| FCF | ~USD 12.56B (30.35% margin) | Likely inflated by working-capital inflow |
| FCF yield | 4.90% on market cap | Not a clean steady-state anchor |
| EV / EBITDA | 62.99x | On operating EBITDA |
| ROE | 82.58% | Artifact of the net income spike |

**The unresolved gap.** Forward EPS × shares implies about USD 6.69B of forward net income. That is roughly 2.2x TTM EBIT (~USD 3.09B) and 1.7x TTM EBITDA (USD 3.93B). The current price is only defensible if consensus is right about a very steep margin ramp. If forward EPS still carries non-operating items, even the ~38.3x forward P/E understates the true multiple.

---

## 4. Valuation Bridge

### 4a. DCF (primary and only usable intrinsic method)

**Key inputs, all trailing-derived per upstream provenance:**
- Revenue base: USD 41.37B.
- Growth: 8.7% fading linearly to 3.0%.
- EBITDA margin: 4.7% (trailing 3-year median).
- Capex: 2.5% of revenue. D&A: 2.9% of revenue.
- NWC: −3.4% of revenue (a cash inflow), mo


## Risk Factors

# GE Vernova Inc. (GEV): Risk Factors

**Data as of:** 2026-09-30 (yfinance). **Currency:** USD throughout.
**Period basis:** Income-statement figures are "TTM (provider-reported, unverified)". The provider flags `period_basis_unknown`, and `fiscal_period_end` and `ttm_quarter_ends` are empty. DCF projections are labeled "DCF Yr-n". Figures marked *(derived)* are my arithmetic on upstream data, not provider outputs.
**Standing recommendation:** SELL. The point target is withheld. The indicative range is USD 145–344/share, from the DCF sensitivity grid.

---

## 1. Risk Map Summary

This section covers two kinds of risk:
- **Risks to our SELL call.** These are upside risks to the stock.
- **Risks that reinforce the call.** These are downside risks to the business or valuation.

It also covers model and data integrity risks, which cut both ways.

| # | Risk | Effect on SELL thesis | Likelihood | Impact | Key monitor |
|---|---|---|---|---|---|
| 1 | Margin ramp delivers (consensus forward EPS proves right) | **Against** | Medium | High | Quarterly EBITDA margin vs 9.49% TTM |
| 2 | DCF margin input (4.7%) is too conservative | **Against** (partial) | High | Medium | Segment margins, if disclosed |
| 3 | Momentum persists / valuation stays disconnected (timing risk) | **Against** | Medium–High | High | Price vs USD 1,195.94 52w high |
| 4 | Working-capital inflow reverses | **For** | Medium | High | OCF vs EBITDA conversion |
| 5 | TTM net income contains large non-recurring items | **For** | High | Medium | Forward EPS USD 25.13 vs TTM EPS USD 35.32 |
| 6 | Net cash partly reflects customer advances, not excess cash | **For** | Medium | Medium | Contract liabilities (not supplied) |
| 7 | Period basis unknown / data inconsistencies | Both | Confirmed |


## Recommendation

[CODE GATE: LBO IRR -21.5% is below the 15% minimum hurdle. Recommendation overridden to: PASS]

# GE Vernova Inc. (GEV): Recommendation

**Data as of:** 2026-09-30 (yfinance). **Currency:** USD throughout.

**Period basis:** Income-statement figures are "TTM (provider-reported, unverified)". The provider flags `period_basis_unknown`, and `fiscal_period_end` and `ttm_quarter_ends` are empty. DCF projections are labeled "DCF Yr-n". Figures marked *(derived)* are my own arithmetic on upstream data, not provider or model outputs.

---

## 1. Recommendation Summary

| Item | Value |
|---|---|
| **Rating** | **SELL** |
| **Price target** | **Withheld (null)** |
| **Indicative 12-month value range** | USD 145–344/share (DCF sensitivity grid: WACC 6.31–10.31%, terminal growth 2.0–4.0%) |
| **DCF base case** | USD 190.59/share (WACC 8.31%, terminal growth 3.0%, 10-year projection) |
| **Current price** | USD 962.49/share |
| **Price / DCF base** | ~5.05x *(derived)*, implying about −80% to the base case |
| **Price vs most generous grid cell** | USD 344.32/share, about −64% *(derived)* |
| **Timeframe** | 12 months |
| **Conviction** | Directional: high. Timing: low to medium, because of momentum. |

### Why the price target is withheld

- **Only one method is usable.** The DCF is the only intrinsic method computed upstream, so there is no second method to corroborate a point estimate.
- **The LBO is not a valuation method here.**
  - It is priced off an 8.0x TTM EBITDA entry, giving a USD 31.42B entry EV.
  - It is flagged "NOT self-financing": cumulative levered FCF is −USD 463M over 5 years and net debt rises from USD 19.64B to USD 20.10B.
  - It returns an IRR of −21.5% and a MOIC of 0.30x.
  - It tells us a sponsor could not underwrite GEV at its operating earnings. It does not give a value per share to cross-check the DCF.
- **The DCF's margin input is probably conservative.** It uses a 4.7% EBITDA margin (trailing 3-year median), against 9.49% TTM EBITDA margin.
- **Conclusion on the target.** Publishing a single number would imply more precision than the evidence supports.

### Why the direction is still unambiguous

- Every one of the 25 cells in the DCF sensitivity grid sits between USD 145.34 and USD 344.32/share. All are well below USD 962.49.
- The upstream `market_implied` field is null. My approximate reverse-DCF below suggests that no plausible margin assumption closes the gap.

---

## 2. What the Market Is Missing: The Reverse-DCF Gap

The market's enterprise value is USD 247.34B. The DCF enterprise value is USD 41.76B. The market is therefore capitalizing GEV at about **5.9x the DCF EV** *(derived)*.

### Step 1: The DCF re-run at the TTM margin (approximation, derived)

Method: take DCF Yr-1 and linearly rescale it, holding revenue, capex, D&A, NWC and the 21.3% tax rate constant.

| Line (DCF Yr-1) | At 4.7% margin (model) | At 9.49% TTM margin *(derived)* |
|---|---|---|
| Revenue | USD 44.96B | USD 44.96B |
| EBITDA | USD 2.11B | ~USD 4.27B |
| FCF | USD 2.33B | ~USD 4.0B (~1.7x) |
| Implied value/share | USD 190.59 | **~USD 300** (rough) |

Even with the margin roughly doubled to the TTM level, the result lands inside the USD 145–344 grid range. That is still about 70% below the current price.

### Step 2: What the market price requires (approximation, derived)

- **Required cash flow.** To justify a USD 247.34B EV at the model's roughly 17.9x EV/Yr-1 FCF multiple, Yr-1 FCF would need to be about USD 13.8B.
- **Required margin.** Under the same cost structure, that implies an EBITDA margin in the mid-30s % on DCF Yr-1 revenue of USD 44.96B.
- **The problem.** That required margin is **above GEV's 20.57% TTM gross margin**. Sustained EBITDA cannot exceed gross profit without a fundamental change in cost structure.

**The mispricing, in one sentence:** the headline 27.25x TTM P/E and 4.90% FCF yield make GEV look like a premium-but-reasonable compounder. Both numbers are inflated by items that do not recur.
- TTM net income is USD 9.53B, which is **above** TTM EBITDA of USD 3.93B.
- TTM FCF is ~USD 12.56B, against OCF of USD 14.14B, about 3.6x EBITDA. This is consistent with working-capital inflows such as customer advances.

On operating earnings the stock trades at **62.99x TTM EV/EBITDA**, and at about 38.3x forward P/E *(derived: USD 962.49 ÷ USD 25.13)*.

**Caveat.** This reverse-DCF is a linear approximation and not an upstream model output. It is directionally robust, but a proper market-implied solve should replace it once available.

---

## 3. Bull-Case Catalysts (Upside Drivers That Would Hurt the SELL Call)

1. **The margin ramp delivers.**
   - Consensus forward EPS of USD 25.13 implies about USD 6.69B of forward net income *(derived)*. That is ~1.7x TTM EBITDA and ~2.2x TTM EBIT (~USD 3.09B).
   - Quarterly EBITDA margins stepping clearly above the 9.49% TTM level would validate part of the market's bet.
2. **Revenue growth accelerates beyond the 8.7% trailing 4-year CAGR.**
   - The DCF fades growth linearly from ~8.7% to 3.0%.
   - Sustained high-single or double-digit growth with operating leverage would lift every cell of the grid.
3. **The order-backed cash model persists.**
   - OCF of USD 14.14B and net cash of USD 9.00B (~USD 33.8/share) give room for buybacks or dividend growth. The current payout is only 5.73% (USD 2.00 DPS, 0.21% yield).
   - Capital return could support the multiple even without a change in intrinsic value.
4. **Momentum and flows.**
   - The stock is up +56.9% over the trailing year. The 52-week range is USD 529.18–1,195.94, and the current price is about 20% below the high *(derived)*.
   - Continued sector enthusiasm could keep the valuation disconnected for longer than 12 months.
5. **Better disclosure shows a higher-margin mix.
