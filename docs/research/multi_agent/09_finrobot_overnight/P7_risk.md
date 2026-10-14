# FinRobot risk analysis on GEV

_P7_risk — generated 2026-09-30 00:16:25_

# GE Vernova (GEV): Financial Risk Assessment

## Executive Summary

GEV has a **strong balance sheet with low financial risk**: $9.0B net cash and debt of about 0.9x EBITDA. The main risks are **valuation and earnings quality**. At 63x EV/EBITDA, the stock prices in years of margin expansion from a business earning a 7.5% operating margin today. Reported net income ($9.5B) is more than twice EBITDA ($3.9B), and operating cash flow ($14.1B) is 3.6x EBITDA. That points to non-recurring gains and large customer-advance inflows rather than steady-state economics.

**Overall Risk Rating: Medium-High.** The balance sheet is low risk. Valuation and earnings quality are high risk.

---

## 0. Data Integrity Review

Several figures do not reconcile. They should be resolved before relying on this analysis.

| Issue | Observation | Implication |
|---|---|---|
| **FCF calculation error** | OCF $14.1B − CapEx $1.6B = **$12.5B**, not $15.7B. The reported figure appears to add CapEx instead of subtracting it. | Corrected FCF yield is **~4.9%**, not 6.1%. |
| **Net income > EBITDA** | Net income of $9.5B exceeds EBITDA of $3.9B by 2.4x. | Net income must include large non-operating items, such as divestiture or remeasurement gains or tax benefits. The reported P/E of 27.3x is therefore misleading. |
| **OCF ≫ EBITDA** | OCF/EBITDA = 3.6x. | Cash flow is driven by working capital, most likely customer down payments and slot reservations. It is not recurring earnings power. |
| **Implied D&A** | EBIT ≈ $3.1B (7.5% × $41.4B), so implied D&A ≈ $0.8B. | This is plausible, but D&A is not reported, so it cannot be verified. |

**Normalized earnings estimate:** EBIT of $3.1B, taxed at ~21%, gives about **$2.5B** of normalized net income. That implies a **normalized P/E of roughly 100x**, versus the reported 27.3x.

---

## 1. Operational Risk

| Risk | Severity | Driving Data Point | What to Monitor |
|---|---|---|---|
| **Thin margins** | **High** | Gross margin 20.6%; operating margin 7.5% | Segment margins, particularly Wind losses vs. Power and Electrification profitability |
| **Execution on fixed-price, long-cycle contracts** | **Medium-High** | 20.6% gross margin leaves little room for cost overruns on multi-year turbine and grid projects | Contract charges, warranty reserves, backlog margin vs. recognized margin |
| **Cost structure rigidity** | **Medium** | SG&A and R&D not disclosed. The gap between 20.6% gross and 7.5% operating margin means about 13% of revenue goes to opex. | Opex as % of revenue, headcount, and operating leverage as revenue grows |
| **Revenue concentration** | **Medium** (data limited) | No segment or customer data. Exposure is concentrated in utilities, IPPs and hyperscaler-driven power demand. | Backlog mix by segment and geography; share of orders tied to data-center load growth |

**Assessment:** The key question is whether GEV can move from a 7.5% operating margin toward the low-to-mid teens. With a 20.6% gross margin, every percentage point of margin is worth about $414M of EBIT. That is highly material relative to the $3.1B base, in both directions.

---

## 2. Financial Risk

| Risk | Severity | Driving Data Point | What to Monitor |
|---|---|---|---|
| **Leverage** | **Low** | Total debt $3.7B; Debt/EBITDA ≈ 0.95x; **net cash $9.0B** | Debt-funded M&A or buybacks |
| **Interest coverage** | **Low** | Interest expense not reported. $3.7B of debt at an assumed 5–6% implies ~$0.2B of interest, or about 15x EBIT coverage. | Actual interest expense disclosure |
| **Refinancing exposure** | **Low** | Cash of $12.7B covers total debt 3.4x | Debt maturity schedule |
| **Liquidity / working-capital reversal** | **Medium** | OCF of $14.1B vs. EBITDA of $3.9B means roughly $10B of the cash is likely customer advances, i.e., a liability owed back in deliverables | Contract liabilities trend, order intake vs. deliveries, OCF/EBITDA reverting toward ~1x |

**Assessment:** Solvency risk is minimal. The subtler risk is that the cash pile is partly funded by customers. If order momentum slows, down payments will unwind as units ship. OCF could then fall well below EBITDA for several periods. Treat part of the $12.7B cash as operationally committed.

---

## 3. Market Risk

| Risk | Severity | Driving Data Point | What to Monitor |
|---|---|---|---|
| **Valuation / multiple compression** | **High** | EV/EBITDA 63.0x; normalized P/E ~100x; EV/Sales ~6.0x on a 7.5% margin business | Consensus margin trajectory vs. delivery; peer multiples (Siemens Energy, Mitsubishi Heavy, Schneider, Eaton) |
| **Growth expectations embedded** | **High** | Worked example: at a 25x EV/EBITDA multiple for a mature industrial, EBITDA would need to reach about $9.9B, **2.5x today's level**, to justify the current EV | Revenue growth, backlog conversion, and margin guidance revisions |
| **Sector cyclicality** | **Medium-High** | Power equipment has historically been boom-bust, and the current cycle rests on the AI/data-center electricity demand narrative | Utility capex plans, hyperscaler capex guidance, interest rates, gas turbine pricing |
| **Corrected FCF yield** | **Medium** | 4.9% corrected yield, flattered by advances. On a normalized basis (EBITDA − CapEx ≈ $2.3B), the yield is **~0.9%**. | FCF excluding changes in contract liabilities |

**Assessment:** This is the dominant risk. The valuation assumes that a multi-year up-cycle in power demand converts into sustained pricing power and margin expansion. Several things could trigger a sharp de-rating:

- a moderation in data-center capex,
- gas turbine capacity additions by competitors, or
- a miss on margin targets.

Even a move from 63x to 35x EV/EBITDA would imply about 45% EV downside at constant EBITDA.

---

## 4. Strategic Risk

| Risk | Severity | Driving Data Point | What to Monitor |
|---|---|---|---|
| **R&D adequacy** | **Medium** (unverifiable) | R&D not disclosed. The 20.6% gross margin limits reinvestment capacity relative to higher-margin electrification peers. | R&D as % of revenue; SMR (BWRX-300), grid software and HVDC investment |
| **Competitive positioning** | **Medium** | Pricing power in gas turbines is strong now, but the 7.5% consolidated margin suggests weaker units (likely Wind) are diluting results | Segment disclosure, pricing on new orders vs. backlog, offshore wind exposure/exit |
| **Capital allocation** | **Medium** | FCF of $12.5B against CapEx of only $1.6B (3.9% of revenue) creates large deployable cash | Buybacks at a 63x multiple (value-destructive risk), M&A discipline, capacity expansion adequacy |
| **Capacity underinvestment** | **Low-Medium** | CapEx/Revenue of 3.9% is modest if demand is truly structural | Lead times, slot reservation backlog, capex guidance |

---

## Risk Matrix Summary

| Dimension | Severity | Key Driver |
|---|---|---|
| Operational | **Medium-High** | 7.5% operating margin; 20.6% gross margin leaves little execution buffer |
| Financial | **Low** | $9.0B net cash; ~0.9x Debt/EBITDA |
| Market | **High** | 63x EV/EBITDA; ~100x normalized P/E |
| Strategic | **Medium** | Undisclosed R&D; margin dilution from weaker segments; buyback risk at peak multiples |
| Earnings Quality (cross-cutting) | **High** | Net income 2.4x EBITDA; OCF 3.6x EBITDA |

---

## Key Monitoring Dashboard

1. **Operating margin trajectory:** the target path from 7.5% toward double digits, tracked quarterly.
2. **Contract liabilities and customer advances:** the leading indicator of an OCF reversal.
3. **Order intake vs. revenue (book-to-bill):** below 1.0x would signal a cycle peak.
4. **Normalized earnings:** strip out gains and tax items to rebuild a clean P/E.
5. **Hyperscaler and utility capex guidance:** the primary demand driver behind the multiple.
6. **Capital deployment:** the scale and pricing of buybacks relative to intrinsic value.

**Bottom line:** GEV is financially safe but priced for perfection. The balance sheet can absorb operational shocks. The equity valuation could not absorb a disappointment in margins or in the demand cycle.
