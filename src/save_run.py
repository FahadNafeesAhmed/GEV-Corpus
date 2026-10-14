"""
Save a multi-agent workflow output as a run folder under docs/research/multi_agent/.

Usage:
  python src/save_run.py <workflow-output.json> <run_folder_name> <kind>

kind is one of:
  vintage   - the backlog-vintage verification run (result.verdict + result.assignments)
  winners   - the pitch-winners corpus run (result.playbook; full corpus lives in ../pitch-winners-corpus)
  brief     - the evidence-brief run (result.brief + result.lanes), also writes FACTS.csv
  journal   - a run still in progress: renders whatever agents have finished, from journal.jsonl

Writes SYNTHESIS.md (the decision-level report), DIGEST.md (every agent's output in readable
form) and agents.json (the structured result), matching runs 01-05.
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_BASE = ROOT / "docs" / "research" / "multi_agent"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HEADER = ("_AI-assisted research input for the team, disclosed as such under the competition rules. "
          "Not submission text. Every figure carries a source so a teammate can re-check it._\n")


def md(obj, depth=3):
    """Render any JSON value as readable markdown."""
    out = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            title = str(k).replace("_", " ")
            if isinstance(v, str):
                if "\n" in v or len(v) > 160:
                    out.append("%s %s\n\n%s\n" % ("#" * min(depth, 6), title, v))
                else:
                    out.append("**%s:** %s  " % (title, v))
            elif isinstance(v, (int, float, bool)) or v is None:
                out.append("**%s:** %s  " % (title, v))
            else:
                out.append("\n%s %s\n" % ("#" * min(depth, 6), title))
                out.append(md(v, depth + 1))
    elif isinstance(obj, list):
        if obj and all(isinstance(x, dict) for x in obj) and _flat(obj):
            out.append(_table(obj))
        else:
            for x in obj:
                if isinstance(x, (dict, list)):
                    out.append(md(x, depth))
                    out.append("")
                else:
                    out.append("- %s" % x)
    else:
        out.append(str(obj))
    return "\n".join(out) + "\n"


def _flat(rows):
    return all(all(not isinstance(v, (dict, list)) or (isinstance(v, list) and all(isinstance(i, str) for i in v))
                   for v in r.values()) for r in rows)


def _cell(v):
    if isinstance(v, list):
        v = ", ".join(v)
    return str(v if v is not None else "").replace("|", "/").replace("\n", " ")


def _table(rows):
    cols = []
    for r in rows:
        for k in r:
            if k not in cols:
                cols.append(k)
    lines = ["| " + " | ".join(c.replace("_", " ") for c in cols) + " |",
             "|" + "---|" * len(cols)]
    for r in rows:
        lines.append("| " + " | ".join(_cell(r.get(c)) for c in cols) + " |")
    return "\n".join(lines) + "\n"


def load(path):
    blob = json.loads(Path(path).read_text(encoding="utf-8"))
    return blob, blob.get("result", blob)


def write(run_dir, synthesis, digest, data):
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "SYNTHESIS.md").write_text(synthesis, encoding="utf-8")
    (run_dir / "DIGEST.md").write_text(digest, encoding="utf-8")
    (run_dir / "agents.json").write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", run_dir)


def save_vintage(blob, res, run_dir):
    v = res.get("verdict") or {}
    s = ["# Run 06 — backlog-vintage verification\n", HEADER,
         "**Survives:** %s\n" % v.get("survives", ""),
         "## Verdict\n", v.get("report", ""),
         "\n## Final range\n", v.get("final_range", ""),
         "\n## Lead fact with citation (research statement, not memo text)\n", v.get("one_sentence_for_memo", ""),
         "\n## The three hardest judge challenges\n", v.get("judge_exchange", ""),
         "\n## Model drivers\n", v.get("model_drivers", ""),
         "\n## Corrections to figures the team was carrying\n"]
    s += ["%d. %s" % (i, c) for i, c in enumerate(v.get("corrections") or [], 1)]
    d = ["# Run 06 — every assignment's output\n", HEADER,
         "Tally: `%s`\n" % json.dumps(res.get("tally"))]
    for a in res.get("assignments") or []:
        d.append("\n---\n\n## %s\n" % a.get("assignment", ""))
        d.append(md({k: a[k] for k in a if k != "assignment"}))
    write(run_dir, "\n".join(s) + "\n", "\n".join(d), res)


def save_winners(blob, res, run_dir):
    pb = res.get("playbook") or {}
    s = ["# Run 07 — elite pitch-winners corpus\n", HEADER,
         "The underlying deck corpus is not published (third-party copyright); it lived in: `<local>/pitch-winners-corpus\\` "
         "(PLAYBOOK.md, GEV_GAP_CHECK.md, INDEX.md, lenses/, cases/, raw/ with 262 source texts, corpus.db). "
         "Search it with `python src/search.py \"query\"` from that folder.\n",
         "33 agents: 6 finders, 1 curator, 20 blind per-case readers, 5 cross-case lenses, 1 playbook.\n",
         "## Honest verdict on the GEV pitch\n", pb.get("honest_verdict", ""),
         "\n## Gap check, priority order\n",
         _table(sorted(pb.get("gev_gap_check") or [], key=lambda r: (r.get("priority", 9), r.get("status", "")))),
         "\n## Tests a wedge must pass\n"]
    s += ["%d. %s" % (i, t) for i, t in enumerate(pb.get("wedge_tests") or [], 1)]
    d = ["# Run 07 — playbook and lens reports\n", HEADER, pb.get("playbook_md", "")]
    for L in res.get("lenses") or []:
        d.append("\n---\n\n# Lens: %s\n" % (L.get("lens", "")[:120]))
        d.append(L.get("report_md", ""))
    write(run_dir, "\n".join(s) + "\n", "\n".join(d), res)


def save_brief(blob, res, run_dir):
    b = res.get("brief") or {}
    s = ["# Run 08 — evidence brief\n", HEADER,
         b.get("brief_md", ""),
         "\n## Decisive tests\n", _table(b.get("decisive_tests") or []),
         "\n## Direction lookup (the team picks the row)\n", b.get("direction_lookup_md", ""),
         "\n## Model inputs\n", b.get("model_inputs_md", ""),
         "\n## Memo element checklist (elements only — the team writes every sentence)\n", b.get("memo_checklist_md", ""),
         "\n## Struck figures — do not use\n"]
    s += ["- %s" % x for x in b.get("struck") or []]
    s += ["\n## Open items\n"] + ["- %s" % x for x in b.get("open_items") or []]
    q = ["# Judge question bank — facts to answer from\n", HEADER]
    for i, x in enumerate(b.get("qa_bank") or [], 1):
        q.append("## %d. %s\n\n%s\n\n_Fact ids: %s_\n" % (i, x.get("question", ""), x.get("facts_to_answer_with", ""),
                                                         ", ".join(x.get("fact_ids") or [])))
    d = lanes_digest("Run 08 — every research lane and its verification", res.get("lanes") or [])
    write(run_dir, "\n".join(s) + "\n", d, res)
    (run_dir / "QA_BANK.md").write_text("\n".join(q), encoding="utf-8")
    rows = b.get("fact_table") or []
    with open(run_dir / "FACTS.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["id", "fact", "value", "source", "locator", "verifier_status", "use",
                    "team_checked_by", "team_page_found", "matches_Y_N", "team_note"])
        for r in rows:
            w.writerow([r.get("id"), r.get("fact"), r.get("value"), r.get("source"), r.get("locator"),
                        r.get("status"), r.get("use"), "", "", "", ""])
    print("wrote FACTS.csv with %d rows" % len(rows))


def lanes_digest(title, pairs):
    d = ["# %s\n" % title, HEADER]
    for p in pairs:
        r, v = p.get("research") or {}, p.get("verify") or {}
        status = {c.get("fact_id"): c for c in v.get("checks") or []}
        d.append("\n---\n\n## %s\n" % r.get("lane", ""))
        d.append("**Headline:** %s\n" % r.get("headline", ""))
        d.append("**Confidence:** %s/5 · **Verifier:** %s\n" % (r.get("confidence"), v.get("summary", "")))
        d.append("### Facts, with the verifier's status\n")
        d.append("| id | claim | value | period | source | locator | verifier | corrected / evidence |")
        d.append("|---|---|---|---|---|---|---|---|")
        for f in r.get("facts") or []:
            c = status.get(f.get("id")) or {}
            note = c.get("correct_value", "") if c.get("status") != "verified" else ""
            if c.get("status") not in (None, "verified"):
                note = "%s — %s" % (note, c.get("evidence", ""))
            d.append("| %s |" % " | ".join(_cell(x) for x in [f.get("id"), f.get("claim"), f.get("value"),
                                                              f.get("period"), f.get("source"), f.get("locator"),
                                                              c.get("status", "unchecked"), note]))
        d.append("\n### Tests\n")
        d.append(_table(r.get("tests") or []) if r.get("tests") else "_none_\n")
        if r.get("grids_md"):
            d.append("\n### Grids (team's choice)\n\n" + r["grids_md"])
        for label, key in [("Verifier's audit of the tests", "test_audit")]:
            items = v.get(key) or []
            if items:
                d.append("\n### %s\n" % label)
                d += ["- %s" % x for x in items]
        for label, key in [("Unresolved", "unresolved"), ("Corrections to the verified state", "corrections_to_verified_state")]:
            items = r.get(key) or []
            if items:
                d.append("\n### %s\n" % label)
                d += ["- %s" % x for x in items]
    return "\n".join(d) + "\n"


def save_journal(journal, run_dir):
    """Render finished lanes of a run that is still going, from its journal."""
    rows = [json.loads(l) for l in Path(journal).read_text(encoding="utf-8").splitlines() if l.strip()]
    res = [r.get("result") or r.get("value") for r in rows if r.get("type") == "result"]
    research = [x for x in res if isinstance(x, dict) and "facts" in x]
    verify = {(x.get("lane") or "")[:6]: x for x in res if isinstance(x, dict) and "checks" in x}
    pairs = [{"research": r, "verify": verify.get((r.get("lane") or "")[:6])} for r in research]
    s = ["# Run 08 — evidence brief (IN PROGRESS)\n", HEADER,
         "The final assembly had not finished when this was saved. DIGEST.md holds every finished research "
         "lane with its verifier's status on each fact. This file is replaced when the run completes.\n"]
    write(run_dir, "\n".join(s), lanes_digest("Run 08 — research lanes finished so far", pairs), {"lanes": pairs})


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    src, name, kind = sys.argv[1], sys.argv[2], sys.argv[3]
    run_dir = OUT_BASE / name
    if kind == "journal":
        return save_journal(src, run_dir)
    blob, res = load(src)
    {"vintage": save_vintage, "winners": save_winners, "brief": save_brief}[kind](blob, res, run_dir)


if __name__ == "__main__":
    main()
