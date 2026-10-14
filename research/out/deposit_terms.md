# RESEARCH NOTES — NOT A COMPETITION SUBMISSION

**AI-research disclosure:** Local Ollama extraction (qwen3:8b) over private GEV corpus with quote-must-match verification. Initial research only; verify against primary filings before any memo use.

---


# SRA / deposit / refund terms (primary filings)

- Model: `qwen3:8b`
- Evidence hits: **27**
- Verified claims: **4** (rejected 2)
- Elapsed: 36.96s

## Working verdict

PRIMARY: down payments on orders AND slot reservations drive contract liabilities / FCF. NON-REFUNDABLE terms NOT found in this retrieval. Risk factor: SRAs may not convert to orders.

## Deterministic flags

- `mentions_slot_reservation`: **True**
- `mentions_down_payment`: **True**
- `mentions_deposit`: **False**
- `mentions_refund`: **False**
- `mentions_nonrefundable`: **False**
- `mentions_may_not_place_orders`: **False**

## Verified claims

- **Slot reservation agreements (SRA) contributed to contract liabilities and deferred income, with Power and Electrification being key segments.**
  - quote: “contract liabilities and current deferred income of $13.7 billion, driven by down payments on orders and slot reservation agreements at Power, and down payments at Electrification”
  - confidence: 90
- **Contract liabilities and deferred income increased by $14.088 billion in the six months ended June 30, 2026, due to new collections exceeding revenue recognition.**
  - quote: “Contract liabilities and deferred income increase d $14,088 million in the six months ended June 30, 2026 primarily due to new collections received in excess of revenue recognition”
  - confidence: 90
- **GE Vernova's contract liabilities and deferred income totaled $39.944 billion as of June 30, 2026, with Power accounting for $27.679 billion.**
  - quote: “contract liabilities and current deferred income $27,679 $9,113 $3,150 $39,944”
  - confidence: 95
- **GE Vernova's remaining performance obligation (RPO) related to GE credit support obligations was estimated at $12 billion as of June 30, 2025.**
  - quote: “we estimated GE Vernova RPO and other obligations that relate to GE credit support to be approximately $12 billion”
  - confidence: 90

## Unresolved

- The evidence does not specify refundability terms for customer deposits, down payments, or slot reservation agreements (SRA).
- No information is provided about forfeiture conditions for unfulfilled SRA obligations.

## Rejected claims (failed quote check)

- GE Vernova's contract liabilities and deferred income increased due to down payments on orders and slot reservation agreements (SRA) at Power and Electrification. —_quote_not_in_evidence_
- Contract liabilities and deferred income were $25.774 billion as of December 31, 2025, with Power accounting for $16.527 billion. —_quote_not_in_evidence_

## Evidence index

- [1] 10-Q 2026-07-22 | Item 2 MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF | chunks_like | id=5751
- [2] 10-Q 2026-07-22 | Item 2 MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF | chunks_like | id=5750
- [3] 10-Q 2026-07-22 | Item 2 MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF | chunks_like | id=5748
- [4] 10-Q 2026-07-22 | Item 1 FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA. | chunks_like | id=5682
- [5] 10-Q 2026-07-22 | Item 1 FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA. | chunks_like | id=5681
- [6] 10-Q 2026-07-22 | Item 1 FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA. | chunks_like | id=5680
- [7] 10-Q 2026-07-22 | Item 1 FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA. | chunks_like | id=5661
- [8] 10-Q 2026-07-22 | Item 1 FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA. | chunks_like | id=5659
- [9] 10-Q 2026-07-22 | Item 1 Financial Statements and Supplementary Data | chunks_like | id=5649
- [10] 10-Q 2026-04-22 | Item 2 MANAGEMENT’S | chunks_like | id=13715
- [11] 10-Q 2026-04-22 | Item 2 MANAGEMENT’S | chunks_like | id=13714
- [12] 10-Q 2026-04-22 | Item 2 MANAGEMENT’S | chunks_like | id=13712
- [13] 10-Q 2025-04-23 | contract_liabilities | backlog_quarterly | id=bq-6929
- [14] 10-Q 2025-04-23 | contract_liabilities | backlog_quarterly | id=bq-6928
- [15] 10-Q 2025-04-23 | contract_liabilities | backlog_quarterly | id=bq-6927
- [16] 10-Q 2025-04-23 | contract_liabilities | backlog_quarterly | id=bq-6926
- [17] 10-Q 2025-04-23 | contract_liabilities | backlog_quarterly | id=bq-6925
- [18] 8-K/EX 2025-04-23 | reservation_gw | backlog_quarterly | id=bq-6909
- [19] 8-K/EX 2025-04-23 | equipment_backlog | backlog_quarterly | id=bq-6908
- [20] 8-K/EX 2025-04-23 | working_capital | backlog_quarterly | id=bq-6906
- [21] 8-K/EX 2025-04-23 | orders_value | backlog_quarterly | id=bq-6901
- [22] 8-K/EX 2025-04-23 | orders_value | backlog_quarterly | id=bq-6900
- [23] 10-Q 2025-07-23 | contract_liabilities | backlog_quarterly | id=bq-6889
- [24] 10-Q 2025-07-23 | contract_liabilities | backlog_quarterly | id=bq-6888
- [25] 10-Q 2025-07-23 | contract_liabilities | backlog_quarterly | id=bq-6866
- [26] 10-Q 2025-07-23 | contract_liabilities | backlog_quarterly | id=bq-6863
- [27] 10-Q 2025-07-23 | contract_liabilities | backlog_quarterly | id=bq-6861

## Summary (model)


