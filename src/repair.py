"""Integrity repair. Run before any night; never skip it.

    python repair.py --check      report only
    python repair.py              apply

Fixes the problems the audit found:
  * chunk ids were reassigned by a full rebuild at 2026-09-20 00:24 while 20
    extraction marks and 25 guidance rows from before it were left in place -
    they now point at unrelated chunks, and the stale marks make the anti-join
    skip real work forever;
  * duplicate (accession, ord) chunk rows would block the stable-id unique index;
  * chunk_key and source versioning columns need backfilling for rows that
    predate them;
  * embeddings / extractions whose chunk no longer exists.
"""
from __future__ import annotations

import argparse
import hashlib
import time

from common import connect, log

# Every extraction created before the full rebuild references pre-rebuild ids.
REBUILD_CUTOFF = "2026-09-20T00:24:00"
# Web-source chunks were rebuilt again at 03:43 (DELETE+INSERT, before the stable
# upsert existed), so any src: extraction older than that is stale too.
SRC_REBUILD_CUTOFF = "2026-09-20T03:44:00"


def dedupe_chunks(con, apply: bool) -> int:
    dups = con.execute(
        "SELECT COUNT(*) - COUNT(DISTINCT accession || '|' || ord) FROM chunks").fetchone()[0]
    log(f"duplicate (accession, ord) chunk rows: {dups}")
    if apply and dups:
        con.execute("""DELETE FROM chunks WHERE id NOT IN
                         (SELECT MIN(id) FROM chunks GROUP BY accession, ord)""")
    return dups


def stale_extractions(con, apply: bool) -> int:
    n = con.execute("SELECT COUNT(*) FROM extractions WHERE ts < ?", (REBUILD_CUTOFF,)).fetchone()[0]
    log(f"extraction marks older than the {REBUILD_CUTOFF} rebuild: {n}")
    if apply and n:
        con.execute("DELETE FROM extractions WHERE ts < ?", (REBUILD_CUTOFF,))
    # ticker disagreement is the second signal for a reassigned id
    m = con.execute("""SELECT COUNT(*) FROM extractions e JOIN chunks c ON c.id=e.chunk_id
                       WHERE e.ticker IS NOT NULL AND c.ticker IS NOT NULL AND e.ticker != c.ticker
                         AND c.accession NOT LIKE 'src:%'""").fetchone()[0]
    log(f"extraction marks whose chunk now belongs to another ticker: {m}")
    if apply and m:
        con.execute("""DELETE FROM extractions WHERE id IN (
                         SELECT e.id FROM extractions e JOIN chunks c ON c.id=e.chunk_id
                         WHERE e.ticker IS NOT NULL AND c.ticker IS NOT NULL
                           AND e.ticker != c.ticker AND c.accession NOT LIKE 'src:%')""")
    s = con.execute("""SELECT COUNT(*) FROM extractions e JOIN chunks c ON c.id=e.chunk_id
                       WHERE c.accession LIKE 'src:%' AND e.ts < ?""", (SRC_REBUILD_CUTOFF,)).fetchone()[0]
    log(f"extraction marks on web chunks older than the {SRC_REBUILD_CUTOFF} rebuild: {s}")
    if apply and s:
        con.execute("""DELETE FROM extractions WHERE id IN (
                         SELECT e.id FROM extractions e JOIN chunks c ON c.id=e.chunk_id
                         WHERE c.accession LIKE 'src:%' AND e.ts < ?)""", (SRC_REBUILD_CUTOFF,))
    return n + m + s


def orphaned(con, table: str, apply: bool) -> int:
    """Rows whose chunk is gone, or whose stored accession disagrees with the chunk."""
    if table in ("embeddings", "extractions"):
        n = con.execute(f"""SELECT COUNT(*) FROM {table} t LEFT JOIN chunks c ON c.id=t.chunk_id
                            WHERE c.id IS NULL""").fetchone()[0]
        log(f"{table}: {n} rows whose chunk no longer exists")
        if apply and n:
            con.execute(f"DELETE FROM {table} WHERE chunk_id NOT IN (SELECT id FROM chunks)")
        return n
    n = con.execute(f"""SELECT COUNT(*) FROM {table} t LEFT JOIN chunks c ON c.id=t.chunk_id
                        WHERE c.id IS NULL OR c.accession != t.accession""").fetchone()[0]
    log(f"{table}: {n} rows orphaned or pointing at a chunk with a different accession")
    if apply and n:
        con.execute(f"""DELETE FROM {table} WHERE id IN (
                          SELECT t.id FROM {table} t LEFT JOIN chunks c ON c.id=t.chunk_id
                          WHERE c.id IS NULL OR c.accession != t.accession)""")
    return n


def backfill_chunk_keys(con, apply: bool) -> int:
    n = con.execute("SELECT COUNT(*) FROM chunks WHERE chunk_key IS NULL").fetchone()[0]
    log(f"chunks missing chunk_key: {n:,}")
    if apply and n:
        cur = con.execute("SELECT id, accession, ord, text FROM chunks WHERE chunk_key IS NULL")
        batch = []
        for cid, acc, o, txt in cur:
            k = hashlib.sha1((acc + "|" + str(o) + "|" + (txt or "")).encode("utf-8", "ignore")).hexdigest()
            batch.append((k, cid))
            if len(batch) >= 5000:
                con.executemany("UPDATE chunks SET chunk_key=? WHERE id=?", batch)
                con.commit()
                batch = []
        if batch:
            con.executemany("UPDATE chunks SET chunk_key=? WHERE id=?", batch)
        con.commit()
    return n


def backfill_source_versions(con, apply: bool) -> int:
    n = con.execute("SELECT COUNT(*) FROM sources WHERE content_hash IS NULL").fetchone()[0]
    log(f"sources missing version metadata: {n:,}")
    if apply and n:
        for sid, url, title, text, ret in con.execute(
                "SELECT id, url, title, text, retrieved_at FROM sources WHERE content_hash IS NULL").fetchall():
            h = hashlib.sha1((text or "").encode("utf-8", "ignore")).hexdigest()
            con.execute("""UPDATE sources SET content_hash=?, first_seen=?, last_checked=?, version=1
                           WHERE id=?""", (h, ret, ret, sid))
            con.execute("""INSERT OR IGNORE INTO source_versions
                           (url, version, content_hash, title, text, n_chars, retrieved_at)
                           VALUES (?,1,?,?,?,?,?)""",
                        (url, h, title, text, len(text or ""), ret))
        con.commit()
    return n


def verify_quotes(con, table: str, sample: int = 300) -> None:
    """Whitespace-insensitive check that extracted quotes exist in their chunk."""
    rows = con.execute(f"""SELECT t.quote, c.text FROM {table} t JOIN chunks c ON c.id=t.chunk_id
                           WHERE t.quote IS NOT NULL AND t.quote != ''
                           ORDER BY RANDOM() LIMIT {int(sample)}""").fetchall()
    if not rows:
        log(f"{table}: no quotes to verify")
        return
    def squash(s):
        return "".join((s or "").split()).lower()
    ok = sum(1 for q, t in rows if squash(q) in squash(t))
    log(f"{table}: quote fidelity {ok}/{len(rows)} verbatim ({100*ok/len(rows):.0f}%) on a random sample")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--check", action="store_true", help="report only, change nothing")
    a = p.parse_args()
    apply = not a.check
    con = connect()
    log("=" * 60)
    log("REPAIR " + ("(apply)" if apply else "(check only)"))
    log("=" * 60)
    dedupe_chunks(con, apply)
    stale_extractions(con, apply)
    for t in ("guidance", "risk_items", "claims"):
        orphaned(con, t, apply)
    for t in ("extractions", "embeddings"):
        orphaned(con, t, apply)
    backfill_chunk_keys(con, apply)
    backfill_source_versions(con, apply)
    con.commit()
    if apply:
        # the stable-id index is created on connect(); confirm it now exists
        idx = con.execute("SELECT name FROM sqlite_master WHERE name='ux_chunks_acc_ord'").fetchone()
        log("stable chunk-id index present: " + ("yes" if idx else "NO - duplicates remain, re-run"))
    for t in ("guidance", "risk_items", "claims"):
        verify_quotes(con, t)
    log("repair done")
    con.close()


if __name__ == "__main__":
    main()
