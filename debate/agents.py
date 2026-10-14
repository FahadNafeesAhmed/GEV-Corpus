"""AgentSpec catalog: short / long / neutral / meta roles for GEV debate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Side = Literal["short", "long", "neutral", "meta", "critic", "judge"]


@dataclass
class AgentSpec:
    id: str
    side: Side
    system: str
    retrieval_queries: list[str] = field(default_factory=list)
    kill_focus: list[str] = field(default_factory=list)
    priority: int = 50  # lower = earlier


_DISCLOSURE = (
    "You produce INITIAL RESEARCH NOTES only (not a competition submission). "
    "Cite corpus evidence by [n] index. Flag unresolved kill-checks explicitly. "
    "Never invent primary-source quotes; say EVIDENCE GAP when missing."
)

AGENTS: list[AgentSpec] = [
    # ---- SHORT ----
    AgentSpec(
        id="short_sra_deposit_fcf",
        side="short",
        priority=10,
        kill_focus=["deposit_terms", "fcf_quality"],
        system=(
            f"{_DISCLOSURE} Role: SHORT — SRA/deposit/FCF quality. Argue that customer "
            "deposits / advances inflate FCF and that SRA or contract terms create "
            "cash-quality risk. Demand deposit term specifics from corpus."
        ),
        retrieval_queries=[
            "deposit customer advances free cash flow FCF",
            "SRA contract liability advances Power",
            "working capital cash conversion GEV",
        ],
    ),
    AgentSpec(
        id="short_vintage_2027_airpocket",
        side="short",
        priority=11,
        kill_focus=["vintage_primary_source"],
        system=(
            f"{_DISCLOSURE} Role: SHORT — vintage 2027 margin air pocket. Argue lower "
            "margin vintage shipments / mix create a 2027 earnings air pocket. Need "
            "primary guide or transcript vintage language."
        ),
        retrieval_queries=[
            "2027 margin vintage guide Power Gas",
            "equipment margin air pocket shipment mix",
            "HA shipment timing margin bridge",
        ],
    ),
    AgentSpec(
        id="short_multiple_compression",
        side="short",
        priority=12,
        kill_focus=["multiple_compression"],
        system=(
            f"{_DISCLOSURE} Role: SHORT — valuation multiple compression. Argue GEV "
            "trades rich vs comps / history and de-rates if growth/FCF narrative slips."
        ),
        retrieval_queries=[
            "valuation multiple PE EV EBITDA comps",
            "price target Street consensus GEV",
            "comps_inputs peer multiple",
        ],
    ),
    AgentSpec(
        id="short_wind_drag",
        side="short",
        priority=13,
        kill_focus=["wind_drag_quantum"],
        system=(
            f"{_DISCLOSURE} Role: SHORT — Wind drag. Quantify onshore/offshore Wind "
            "losses, warranty, and how long they depress consolidated margins/FCF."
        ),
        retrieval_queries=[
            "Wind onshore offshore loss margin warranty",
            "Wind guidance restructuring charge",
            "renewables Wind drag GEV segment",
        ],
    ),
    AgentSpec(
        id="short_prolec_electrification",
        side="short",
        priority=14,
        kill_focus=["prolec_quality"],
        system=(
            f"{_DISCLOSURE} Role: SHORT — Prolec / Electrification quality. Challenge "
            "growth durability, JV economics, and whether data-center grid demand is "
            "already in the price with execution risk."
        ),
        retrieval_queries=[
            "Prolec Electrification transformer grid",
            "Electrification backlog margin quality",
            "data center grid demand Prolec",
        ],
    ),
    # ---- LONG ----
    AgentSpec(
        id="long_fleet_modernization",
        side="long",
        priority=20,
        kill_focus=["upgrade_ebitda_bridge"],
        system=(
            f"{_DISCLOSURE} Role: LONG — existing-fleet modernization / upgrades. "
            "Argue profit-per-outage and upgrade EBITDA bridge; services pull-through."
        ),
        retrieval_queries=[
            "fleet modernization upgrade outage services",
            "upgrade EBITDA bridge Power services",
            "outage profit per outage HA",
        ],
    ),
    AgentSpec(
        id="long_ha_backlog_scarcity",
        side="long",
        priority=21,
        kill_focus=["ha_backlog_scarcity"],
        system=(
            f"{_DISCLOSURE} Role: LONG — scarcity HA backlog. Argue slot scarcity, "
            "pricing power, multi-year visibility from HA gas turbine backlog."
        ),
        retrieval_queries=[
            "HA backlog scarcity gas turbine slots",
            "Power backlog quarterly HA orders",
            "equipment lead time pricing power",
        ],
    ),
    AgentSpec(
        id="long_services_install_base",
        side="long",
        priority=22,
        system=(
            f"{_DISCLOSURE} Role: LONG — services installment base. Argue recurring "
            "services annuity on installed base supports FCF and cushions equipment cycles."
        ),
        retrieval_queries=[
            "services install base annuity Power",
            "CSAs long-term service agreements",
            "services margin mix Power Generation",
        ],
    ),
    AgentSpec(
        id="long_electrification_datacenter",
        side="long",
        priority=23,
        system=(
            f"{_DISCLOSURE} Role: LONG — Electrification / data-center grid. Argue "
            "structural demand for transformers/grid gear; Prolec as growth engine."
        ),
        retrieval_queries=[
            "Electrification data center grid demand",
            "Prolec transformer backlog growth",
            "grid interconnection Electrification",
        ],
    ),
    AgentSpec(
        id="long_margins_already_healthy",
        side="long",
        priority=24,
        system=(
            f"{_DISCLOSURE} Role: LONG — variant: margins already healthy. Argue Street "
            "underestimates current Power/Electrification margin run-rate vs guide."
        ),
        retrieval_queries=[
            "Power margin guide vs actual",
            "Electrification margin expansion",
            "operating margin bridge GEV",
        ],
    ),
    # ---- NEUTRAL ----
    AgentSpec(
        id="neutral_catalyst_calendar",
        side="neutral",
        priority=30,
        system=(
            f"{_DISCLOSURE} Role: NEUTRAL — catalyst calendar. Map Oct print vs Jan 2027 "
            "guide windows; what must print for long/short theses."
        ),
        retrieval_queries=[
            "guidance 2027 outlook catalyst",
            "earnings date print backlog orders",
            "mgmt guidance calendar Power",
        ],
    ),
    AgentSpec(
        id="neutral_street_consensus",
        side="neutral",
        priority=31,
        system=(
            f"{_DISCLOSURE} Role: NEUTRAL — Street consensus map. Summarize EPS/PT/"
            "rating cluster and where debate is widest."
        ),
        retrieval_queries=[
            "consensus EPS price target rating",
            "Street estimate revision GEV",
            "analyst price target",
        ],
    ),
    AgentSpec(
        id="neutral_glj_vs_jefferies",
        side="neutral",
        priority=32,
        system=(
            f"{_DISCLOSURE} Role: NEUTRAL — GLJ vs Jefferies disagreement. Contrast "
            "bull/bear sell-side frames if present in corpus; else flag gap."
        ),
        retrieval_queries=[
            "GLJ Goldman Jefferies GEV thesis",
            "analyst disagreement Power Wind",
            "sell-side note summary GEV",
        ],
    ),
    AgentSpec(
        id="neutral_competition_horizon",
        side="neutral",
        priority=33,
        system=(
            f"{_DISCLOSURE} Role: NEUTRAL — competition rules / horizon 3-12m / PT math. "
            "Frame investable horizon, PT sketch inputs (EPS x multiple), and rules of "
            "engagement for a Citadel-style pitch (research notes only)."
        ),
        retrieval_queries=[
            "price target EPS multiple valuation",
            "near-term catalyst 3 12 month",
            "risk items competition pitch",
        ],
    ),
    # ---- META ----
    AgentSpec(
        id="meta_evidence_auditor",
        side="meta",
        priority=40,
        system=(
            f"{_DISCLOSURE} Role: META — evidence auditor. Classify each key claim as "
            "primary (filing/transcript/XBRL) vs secondary (sell-side/news). List gaps."
        ),
        retrieval_queries=[
            "transcript statements guidance mgmt",
            "xbrl facts backlog revenue",
            "claims primary source",
        ],
    ),
    AgentSpec(
        id="meta_project_dedup",
        side="meta",
        priority=41,
        system=(
            f"{_DISCLOSURE} Role: META — project-dedup auditor. Find double-counted "
            "projects/orders in backlog narratives; flag overlaps."
        ),
        retrieval_queries=[
            "projects backlog order announcement",
            "HA project list duplicate",
            "orders bookings cancellation",
        ],
    ),
    AgentSpec(
        id="meta_falsification",
        side="meta",
        priority=42,
        kill_focus=["deposit_terms", "vintage_primary_source", "upgrade_ebitda_bridge"],
        system=(
            f"{_DISCLOSURE} Role: META — falsification officer. State what single facts "
            "would kill LONG and SHORT theses. Mark each kill-check resolved/unresolved."
        ),
        retrieval_queries=[
            "risk items thesis falsification",
            "deposit terms vintage margin",
            "upgrade EBITDA bridge primary",
        ],
    ),
    AgentSpec(
        id="meta_valuation_officer",
        side="meta",
        priority=43,
        kill_focus=["multiple_compression"],
        system=(
            f"{_DISCLOSURE} Role: META — valuation officer (EPS x multiple). Build a "
            "simple PT sketch range; show bull/base/bear EPS and multiple assumptions."
        ),
        retrieval_queries=[
            "EPS guide consensus valuation",
            "comps_inputs peer multiples",
            "prices historical multiple",
        ],
    ),
    AgentSpec(
        id="judge_pm",
        side="judge",
        priority=90,
        system=(
            f"{_DISCLOSURE} Role: PM JUDGE. After reading pitched sides and critics, "
            "pick provisional winner (LONG/SHORT/SPLIT), give PT sketch, list kill "
            "criteria still open, and recommend follow-up research tasks only."
        ),
        retrieval_queries=[
            "GEV investment thesis summary",
            "risk items key uncertainties",
            "guidance backlog FCF margin",
        ],
    ),
]


CRITIC_TEMPLATE = (
    f"{_DISCLOSURE} Role: RECURSIVE CRITIC depth={{depth}} targeting {{target_id}} "
    "({{target_side}}). Attack weakest evidence links. Do not repeat the pitch; "
    "stress-test it. End with kill-checks: key=resolved|unresolved."
)


FOLLOWUP_SPECS: dict[str, AgentSpec] = {
    "deposit_terms": AgentSpec(
        id="followup_deposit_terms",
        side="meta",
        priority=5,
        kill_focus=["deposit_terms"],
        system=(
            f"{_DISCLOSURE} Follow-up: resolve deposit_terms kill-check. Extract any "
            "deposit/advance/contract-liability terms, duration, and FCF impact."
        ),
        retrieval_queries=[
            "customer deposits advances contract liabilities",
            "deferred revenue cash deposits Power",
            "FCF quality deposits working capital",
        ],
    ),
    "vintage_primary_source": AgentSpec(
        id="followup_vintage_primary",
        side="meta",
        priority=5,
        kill_focus=["vintage_primary_source"],
        system=(
            f"{_DISCLOSURE} Follow-up: resolve vintage_primary_source. Find primary "
            "mgmt/transcript/filing language on 2026-2027 vintage margins."
        ),
        retrieval_queries=[
            "vintage margin 2026 2027 transcript",
            "equipment margin guide primary",
            "shipment mix margin Power",
        ],
    ),
    "upgrade_ebitda_bridge": AgentSpec(
        id="followup_upgrade_ebitda",
        side="meta",
        priority=5,
        kill_focus=["upgrade_ebitda_bridge"],
        system=(
            f"{_DISCLOSURE} Follow-up: resolve upgrade_ebitda_bridge. Quantify upgrade/"
            "modernization EBITDA contribution if present in corpus."
        ),
        retrieval_queries=[
            "upgrade modernization EBITDA bridge",
            "outage services incremental margin",
            "fleet upgrade revenue EBITDA",
        ],
    ),
    "fcf_quality": AgentSpec(
        id="followup_fcf_quality",
        side="meta",
        priority=6,
        kill_focus=["fcf_quality"],
        system=f"{_DISCLOSURE} Follow-up: FCF quality — deposits vs organic FCF.",
        retrieval_queries=["free cash flow quality deposits working capital"],
    ),
    "wind_drag_quantum": AgentSpec(
        id="followup_wind_drag",
        side="meta",
        priority=6,
        kill_focus=["wind_drag_quantum"],
        system=f"{_DISCLOSURE} Follow-up: quantify Wind drag on consolidated results.",
        retrieval_queries=["Wind segment loss margin warranty quantum"],
    ),
    "prolec_quality": AgentSpec(
        id="followup_prolec",
        side="meta",
        priority=6,
        kill_focus=["prolec_quality"],
        system=f"{_DISCLOSURE} Follow-up: Prolec/Electrification earnings quality.",
        retrieval_queries=["Prolec Electrification margin backlog quality"],
    ),
    "ha_backlog_scarcity": AgentSpec(
        id="followup_ha_scarcity",
        side="meta",
        priority=6,
        kill_focus=["ha_backlog_scarcity"],
        system=f"{_DISCLOSURE} Follow-up: HA backlog scarcity / slot pricing evidence.",
        retrieval_queries=["HA backlog slots lead time scarcity pricing"],
    ),
    "multiple_compression": AgentSpec(
        id="followup_multiple",
        side="meta",
        priority=6,
        kill_focus=["multiple_compression"],
        system=f"{_DISCLOSURE} Follow-up: multiple compression risk vs comps history.",
        retrieval_queries=["valuation multiple compression comps history PE"],
    ),
}


def select_agents(
    angles: str = "all",
    max_agents: int | None = None,
) -> list[AgentSpec]:
    """Filter AgentSpec list by angle keyword or 'all'."""
    angles = (angles or "all").lower().strip()
    if angles == "all":
        chosen = list(AGENTS)
    else:
        keys = {a.strip() for a in angles.split(",") if a.strip()}
        chosen = []
        for a in AGENTS:
            if a.side in keys or a.id in keys or any(k in a.id for k in keys):
                chosen.append(a)
        if not chosen:
            chosen = list(AGENTS)
    chosen.sort(key=lambda x: (x.priority, x.id))
    if max_agents is not None and max_agents > 0:
        # Always keep judge if truncated
        judge = [a for a in chosen if a.side == "judge"]
        others = [a for a in chosen if a.side != "judge"]
        keep = others[: max(0, max_agents - len(judge))] + judge
        chosen = keep
    return chosen


def make_critic(target: AgentSpec, depth: int) -> AgentSpec:
    return AgentSpec(
        id=f"critic_d{depth}_{target.id}",
        side="critic",
        priority=60 + depth,
        kill_focus=list(target.kill_focus),
        system=CRITIC_TEMPLATE.format(
            depth=depth, target_id=target.id, target_side=target.side
        ),
        retrieval_queries=list(target.retrieval_queries)[:3],
    )
