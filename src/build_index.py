"""Chunk filing text on SEC Item boundaries and build an FTS5 search index."""
from __future__ import annotations

import hashlib
import re

from common import connect, load_config, log


def chunk_key(acc: str, ordinal: int, text: str) -> str:
    return hashlib.sha1((acc + "|" + str(ordinal) + "|" + text).encode("utf-8", "ignore")).hexdigest()


UPSERT = """INSERT INTO chunks
              (accession, ticker, form, filing_date, section, ord, text, tier, kind, chunk_key)
            VALUES (?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(accession, ord) DO UPDATE SET
              ticker=excluded.ticker, form=excluded.form, filing_date=excluded.filing_date,
              section=excluded.section, text=excluded.text, tier=excluded.tier,
              kind=excluded.kind, chunk_key=excluded.chunk_key"""

# "Item 7. Management's Discussion..." / "ITEM 1A - RISK FACTORS"
ITEM_RE = re.compile(
    r"(?im)^\s*(item\s+(\d{1,2}[A-Z]?)\s*[\.\:\-–]?\s*([^\n]{0,120}))$"
)

FTS_SQL = """
DROP TABLE IF EXISTS chunks_fts;
CREATE VIRTUAL TABLE chunks_fts USING fts5(
    text,
    section UNINDEXED,
    form UNINDEXED,
    filing_date UNINDEXED,
    accession UNINDEXED,
    ticker UNINDEXED,
    content='chunks',
    content_rowid='id',
    tokenize='porter unicode61'
);
INSERT INTO chunks_fts(rowid, text, section, form, filing_date, accession, ticker)
    SELECT id, text, section, form, filing_date, accession, ticker FROM chunks;
"""


def split_sections(text: str) -> list[tuple[str, str]]:
    """Split a filing into (section_label, body) on Item headings; fall back to one block."""
    marks = [(m.start(), f"Item {m.group(2)} {m.group(3)}".strip()[:90])
             for m in ITEM_RE.finditer(text)]
    # Require a few real headings before trusting them (8-Ks often have none).
    if len(marks) < 3:
        return [("(document)", text)]
    out = []
    if marks[0][0] > 0:
        out.append(("(front matter)", text[:marks[0][0]]))
    for i, (pos, label) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        body = text[pos:end]
        if len(body) > 120:          # skip table-of-contents echoes
            out.append((label, body))
    return out


def window(body: str, size: int, overlap: int) -> list[str]:
    """Split a section into overlapping windows, preferring paragraph boundaries."""
    body = body.strip()
    if len(body) <= size:
        return [body] if body else []
    out, start = [], 0
    while start < len(body):
        end = min(start + size, len(body))
        if end < len(body):
            brk = body.rfind("\n\n", start + size // 2, end)
            if brk == -1:
                brk = body.rfind(". ", start + size // 2, end)
            if brk != -1:
                end = brk + 1
        piece = body[start:end].strip()
        if piece:
            out.append(piece)
        if end >= len(body):
            break
        start = max(end - overlap, start + 1)
    return out


def build(con, cfg) -> int:
    size, overlap = cfg["chunk_chars"], cfg["chunk_overlap"]
    # Upsert on (accession, ord): chunk ids are stable across rebuilds. A document
    # that shrank has its trailing ords deleted; nothing else is ever deleted.
    rows = con.execute(
        """SELECT accession, ticker, form, filing_date, text FROM documents
           ORDER BY filing_date DESC""").fetchall()
    log(f"chunking {len(rows)} documents (window {size}, overlap {overlap}, upsert)")

    total = 0
    for i, (acc, ticker, form, fdate, text) in enumerate(rows):
        if not text:
            continue
        ordinal = 0
        for label, body in split_sections(text):
            for piece in window(body, size, overlap):
                con.execute(UPSERT, (acc, ticker, form, fdate, label, ordinal, piece,
                                     "primary", "sec", chunk_key(acc, ordinal, piece)))
                ordinal += 1
                total += 1
        con.execute("DELETE FROM chunks WHERE accession=? AND ord>=?", (acc, ordinal))
        if i % 250 == 0 and i:
            con.commit()
            log(f"  {i}/{len(rows)} documents -> {total:,} chunks")
    con.commit()
    log(f"chunks: {total}")

    log("building FTS5 index...")
    con.executescript(FTS_SQL)
    con.commit()
    n = con.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0]
    log(f"FTS5 index: {n} searchable chunks")

    top = con.execute(
        """SELECT section, COUNT(*) c FROM chunks GROUP BY section ORDER BY c DESC LIMIT 12"""
    ).fetchall()
    log("largest sections:")
    for s, c in top:
        log(f"    {c:>5}  {s}")
    return total


def build_sources(con, cfg) -> int:
    """Chunk web/paper/transcript sources into the same chunks table as filings,
    tagged with tier and kind, so search, embeddings and extraction see one corpus."""
    size, overlap = cfg["chunk_chars"], cfg["chunk_overlap"]
    rows = con.execute(
        "SELECT id, kind, tier, angle, title, published, text FROM sources").fetchall()
    log(f"chunking {len(rows):,} web sources (upsert)")
    total = 0
    for sid, kind, tier, angle, title, pub, text in rows:
        if not text:
            continue
        acc = f"src:{sid}"
        header = f"{title}\n\n" if title else ""
        i = 0
        for i, piece in enumerate(window(header + text, size, overlap)):
            con.execute(UPSERT, (acc, "GEV", (kind or "web").upper(), (pub or "")[:10],
                                 angle or kind, i, piece, tier, kind,
                                 chunk_key(acc, i, piece)))
            total += 1
        con.execute("DELETE FROM chunks WHERE accession=? AND ord>?", (acc, i))
    con.commit()
    log(f"source chunks: {total:,}")
    return total


def rebuild_fts(con) -> None:
    con.executescript(FTS_SQL)
    con.commit()
    log(f"FTS5 index rebuilt: {con.execute('SELECT COUNT(*) FROM chunks_fts').fetchone()[0]:,} chunks")


def main():
    cfg = load_config()
    con = connect()
    build(con, cfg)
    con.close()


if __name__ == "__main__":
    main()
