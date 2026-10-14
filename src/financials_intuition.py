"""Thinking guides for the financials page: how to reason about each section, the market
intuitions that apply, and the questions a top buy-side analyst asks. Plain language.

SECTION_GUIDE[section title] = (how to think, [intuitions], [questions])
CHART_QUESTIONS[chart name] = [questions specific to that chart]
"""

SECTION_GUIDE = {
    "How big is the business": (
        "Revenue tells you scale, not health. The first job is to separate the part of revenue that repeats every year "
        "from the part that depends on winning new orders. Then ask what each part is worth on its own. A dollar of "
        "service revenue on a 20-year contract is worth more than a dollar of turbine revenue that must be re-won.",
        [
            "The market prices mix, not totals. Two companies with the same revenue trade at different multiples if one is half services.",
            "Growth that comes from an acquisition is bought, not earned. Strip it out before you call something 'growth'. GEV's 2026 Electrification jump is mostly Prolec.",
            "Look at what is shrinking as hard as what is growing. Onshore Wind falling is a fact the bulls skip.",
            "Reported segments are management's story. Product lines are closer to the truth. Always go one level finer than the press release.",
        ],
        [
            "What share of revenue would still arrive if GEV signed no new orders for two years?",
            "How much of the year-over-year growth is organic, how much is price, how much is acquired?",
            "Which product line is the marginal dollar coming from, and what margin does that line carry?",
            "If I only had the segment table, could I tell this company is in an 'AI supercycle'? If not, why does the stock trade like it is?",
            "What did management stop breaking out this year, and why?",
        ],
    ),
    "Is it making money": (
        "Profit has layers. Gross margin is pricing power minus factory cost. Operating margin adds overhead. Net margin adds "
        "tax and one-offs. When the three move together the business is changing. When one moves alone, something accounting-shaped "
        "happened. Always ask which layer moved and why before you believe a margin number.",
        [
            "Margin expansion during a volume ramp is rare and valuable. It means price is rising faster than cost. The question is how long it lasts.",
            "Segment EBITDA is the number the Street models. Get the segment margin bridge right and the rest of the model follows.",
            "A loss-making segment that management promises will break even is a bet, not a forecast. Check the arithmetic against the best quarter that segment ever had.",
            "One-offs that recur are not one-offs. Restructuring every quarter is a cost of doing business.",
            "The multiple is paid on next year's margin, not this year's. Every margin debate is really a 2027 debate.",
        ],
        [
            "Is gross margin rising because of price, mix, or volume absorbing fixed cost? Each has a different half-life.",
            "What was the margin on the units being built today priced at, and when were those prices set?",
            "If Wind cannot reach the guided loss, how much does that subtract from company EPS, and is it already in the consensus number?",
            "What is the incremental margin, meaning profit change divided by revenue change, over the last four quarters? Is it above or below the segment average?",
            "Which costs are stepping up with the factory expansion, and are they in cost of revenue or in SG&A?",
            "What effective tax rate should I use, and what is the one-off in the reported rate?",
        ],
    ),
    "Cash: what actually arrived": (
        "Profit is an opinion. Cash is a fact. But cash has timing. Customer deposits arrive years before the work, so a company "
        "in an order boom shows more cash than profit, and a company in an order bust shows less. Always ask: is this cash "
        "earned, or borrowed from the future?",
        [
            "Free cash flow far above net income means working capital is helping. Working capital help always reverses; the question is when.",
            "Deposits are customer money held in trust for work not yet done. They are a liability with a cash balance attached.",
            "The market rewards a cash beat on the day and forgets it in a month if the source was deposits, because everyone can see the reversal coming.",
            "Capex guided up is a signal of confidence. Capex delivered below guidance is a signal of caution, or of supplier bottlenecks.",
            "Buybacks funded by deposits are buybacks funded by customers. That works until orders slow.",
        ],
        [
            "What was free cash flow excluding the change in contract liabilities? That is the earned cash.",
            "How many quarters of the current burn rate does the deposit balance cover, and what happens to cash flow when inflow equals burn?",
            "What deposit percentage is implied by deposits divided by new commitments? Is it rising because customers are more desperate, or because GEV asks for more?",
            "Is second-half guidance conservative because management always guides low, or because they see the inflow slowing?",
            "Where did the Prolec cash come from, and what does the balance sheet look like without the deposit tailwind?",
        ],
    ),
    "The order book": (
        "A backlog is a promise, and promises have grades. Firm orders with penalties are the highest grade. Reservations with "
        "deposits are lower. Announced projects with no money down are noise. The market tends to price the headline number; "
        "the analyst prices the graded number and the speed at which it converts.",
        [
            "Backlog divided by annual capacity is years of visibility. Beyond about four years, more backlog adds little value today and mostly signals pricing power.",
            "The market stops rewarding a metric once it has been huge for several quarters. Watch whether the stock still moves on GW announcements.",
            "Timing matters more than size. Backlog delivered in 2029 is worth much less than backlog delivered in 2027, and it is exposed to cancellation.",
            "Reservation-to-order conversion is the honest demand signal. Signing is free; converting costs money.",
            "Compare the peer. If Siemens converts twice as fast, ask why GEV's customers wait longer.",
        ],
        [
            "What fraction of the '116 GW under contract' has a substantive cancellation penalty?",
            "What is the median age of a reservation before it converts, and is it lengthening?",
            "If capacity is 20 GW a year and backlog plus reservations are 116 GW, what must be true for a 2027 order to matter to 2027 revenue at all?",
            "How much of the equipment backlog is priced at 2024 levels, and how much at 2025 levels?",
            "What happens to the reservation pool if data-center projects slip a year? Which ones are tied to sites with permits and gas supply?",
            "Does the company's definition of backlog match the one the sell-side uses when quoting it?",
        ],
    ),
    "Quality signals": (
        "Quality means: will these profits hold. The clues are in the footnotes, not the headlines. Estimate changes, warranty reserves, "
        "and inventory turns tell you whether the company is over-earning today at the expense of tomorrow. Read the "
        "footnote every quarter and chart it. Nobody else does.",
        [
            "A negative revision to contract profit estimates is management admitting yesterday's profit was too high. A pattern of them is a trend, not noise.",
            "Warranty reserves that lag a product ramp are a future charge. New models fail more in their first years.",
            "Inventory rising faster than revenue is either pre-building for a ramp, which is good, or unsold product, which is bad. The company will call it the first. Check shipments.",
            "Restructuring that never ends is a margin cost the adjusted numbers hide.",
            "The best short ideas in industrials come from the quality section, not the revenue section.",
        ],
        [
            "What is the cumulative profit revision on service contracts over the last eight quarters, and what share of service backlog does it represent?",
            "What drove the revision: cost inflation, parts availability, fleet running harder than assumed, or contract renegotiation?",
            "Is warranty accrual per dollar of equipment revenue rising as new turbine models ramp?",
            "How many days of revenue is inventory, and how does that compare with the peer set?",
            "Which adjusted-earnings exclusions are recurring, and what is EPS without them?",
        ],
    ),
    "Balance sheet and shareholders": (
        "The balance sheet is where past decisions live. Goodwill is the premium paid for acquisitions. Debt is a claim ahead of "
        "shareholders. Buybacks are management's opinion of the share price, backed with cash. Read all three together: "
        "a company buying back stock at 35 times earnings while carrying fresh acquisition goodwill is making two bets at once.",
        [
            "Net cash gives optionality but earns nothing. The market values what the cash will do, not the cash itself.",
            "Goodwill is only a problem when it is written down. It is written down when the acquisition misses. Watch Prolec's organic growth.",
            "Buybacks lift EPS mechanically. Separate EPS growth from profit growth before you praise it.",
            "Liabilities that grow because of deposits are not leverage. Analysts who compute debt-to-equity without adjusting get GEV wrong.",
            "Share count falling while the stock rises means management is paying more for each share retired. Ask if they would buy at this price with their own money.",
        ],
        [
            "How much EPS growth in the last year came from a lower share count versus higher profit?",
            "At what share price does the buyback stop making sense against reinvesting in capacity?",
            "What return did GEV pay for Prolec, and what must Prolec earn for that goodwill to hold?",
            "What is the true net cash after subtracting deposits that will be worked off within a year?",
            "What is the dilution from stock awards each year, and does the buyback merely offset it?",
        ],
    ),
}

CHART_QUESTIONS = {
    "revenue_mix": ["Is services growing in dollars, or only holding share while equipment ramps?", "What would revenue look like with equipment flat? That is the floor."],
    "segment_revenue": ["What is Electrification's organic growth once Prolec is removed?", "Is Wind shrinking by choice or by loss of orders?"],
    "subsegment_revenue": ["Is Gas Power revenue rising because of units, price, or scope such as combined-cycle equipment?", "Which small lines are being quietly wound down?"],
    "segment_ebitda": ["What does the second half need from Wind for the annual guide to hold, and has Wind ever done that?", "Is Power's growth in EBITDA faster than its growth in revenue?"],
    "segment_margin": ["Is Power margin expanding on price, mix or volume, and which of those survives a ramp?", "What margin do the units ordered in 2024 carry versus those ordered in 2025?"],
    "margins": ["Which of the three lines moved this quarter, and was the cause operating or accounting?", "What is net margin excluding the Prolec revaluation and the tax benefit?"],
    "cost_structure": ["Is cost of revenue falling as a share because of price, or because of mix toward services?", "When does the 1,500-worker hiring wave show up in cost of revenue?"],
    "below_the_line": ["What tax rate belongs in the model, and why does the reported one swing?", "Is interest income from cash that belongs to customers as deposits?"],
    "cash": ["What is free cash flow excluding the change in deposits?", "Why is second-half guidance so much lower than the first half?"],
    "cash_sources": ["How much of financing outflow is buybacks, and is it funded by earned cash or deposits?", "Was the Prolec purchase price matched by the cash it will generate?"],
    "deposits": ["What deposit rate on new commitments does the balance imply, and is it rising?", "Under what conditions does this balance shrink, and how fast?"],
    "deposits_by_segment": ["Why is nearly all deposit growth in Power, and what does that say about Electrification's contract terms?", "Are Wind deposits shrinking because deliveries are happening or because orders stopped?"],
    "deposit_burn": ["When do inflow and burn cross, and what is cash flow in that quarter?", "How much of the burn is Power versus Wind?"],
    "rpo_split": ["Has services backlog grown from new contracts or from re-estimating existing ones?", "What is equipment backlog divided by annual capacity, in years?"],
    "rpo_timing": ["If only 36% of equipment backlog arrives within a year, what 2027 revenue does that imply, and what is consensus?", "Why is the one-year share falling: longer lead times or later-dated new orders?"],
    "gas_gw": ["Did shipped gigawatts reach 5 in the third quarter? If not, why not, and what does that do to 2027?", "What share of signed gigawatts are reservations versus firm orders, quarter by quarter?"],
    "gas_backlog": ["Why are reservations now bigger than firm backlog, and what is the conversion lag?", "How many gigawatts of reservations belong to customers without a site, a permit, or gas supply?"],
    "ltsa_revisions": ["What is the nine-month revision in the Q3 10-Q, and did management explain it?", "Is the revision concentrated in one fleet or contract type, for example HA turbines under fixed-price service agreements?"],
    "warranty": ["Is the reserve per dollar of equipment revenue rising as new models ship?", "What is the claims-paid trend versus reserve additions?"],
    "working_capital": ["Is inventory growth explained by the Q3 shipment plan, or is it building faster than shipments?", "Are receivables growing faster than revenue, meaning customers are paying slower?"],
    "restructuring": ["What was excluded from adjusted EPS in the last four quarters, and does it add up to a recurring cost?"],
    "balance_sheet": ["What is net cash after subtracting deposits due within a year?", "Why did GEV issue bonds while holding net cash?"],
    "goodwill": ["What organic growth must Prolec deliver to justify $9.7B of purchase price?", "How much of reported profit decline is amortization that EBITDA ignores?"],
    "capital_return": ["How much EPS growth is share count versus profit?", "Would management buy at this price with their own money? Check insider purchases."],
    "eps": ["What is EPS excluding one-offs, and how does the forward multiple look on that number?", "How much of next year's EPS growth is already in the deposit-funded buyback?"],
}
