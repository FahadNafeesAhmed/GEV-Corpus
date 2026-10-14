"""Small static SVG chart helpers for the thesis dossier (no JavaScript, prints cleanly)."""
import html

W = 760
BLUE, ORANGE, GRAY, RED, GREEN, INK, GRID = "#2a78d6", "#eb6834", "#888780", "#d03b3b", "#1baf7a", "#1a1a19", "#e1e0d9"


def esc(s):
    return html.escape(str(s), quote=True)


def _frame(h, ymin, ymax, yfmt, L=58, R=16, T=22, B=46, nt=5):
    pw, ph = W - L - R, h - T - B

    def y(v):
        return T + ph * (1 - (v - ymin) / float(ymax - ymin))

    out = []
    for i in range(nt + 1):
        val = ymin + (ymax - ymin) * i / nt
        yy = y(val)
        out.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1"/>' % (L, yy, W - R, yy, GRID))
        out.append('<text x="%d" y="%.1f" font-size="12" fill="#666" text-anchor="end">%s</text>' % (L - 6, yy + 4, esc(yfmt(val))))
    return out, y, L, R, T, B, pw, ph


def _open(h, label):
    return '<svg viewBox="0 0 %d %d" width="100%%" role="img" aria-label="%s" xmlns="http://www.w3.org/2000/svg" font-family="Arial, Helvetica, sans-serif">' % (W, h, esc(label))


def legend(items):
    """items: (name, color, style) with style in solid | outlined | dash | dot."""
    out = ['<div class="legend">']
    for name, color, style in items:
        if style == "solid":
            sw = '<span class="sw" style="background:%s"></span>' % color
        elif style == "outlined":
            sw = '<span class="sw" style="border:2px solid %s;background:#fff"></span>' % color
        elif style == "dash":
            sw = '<span class="ln" style="border-top:2px dashed %s"></span>' % color
        elif style == "dot":
            sw = '<span class="ln" style="border-top:2px dotted %s"></span>' % color
        else:
            sw = '<span class="ln" style="border-top:2px solid %s"></span>' % color
        out.append("<span>%s%s</span>" % (sw, esc(name)))
    out.append("</div>")
    return "".join(out)


def bars(label, cats, series, ymax, yfmt=lambda v: "%g" % v, ymin=0, h=290, stacked=False, hline=None, maxbar=34, nt=5):
    """series: dicts with vals (None allowed), color, outlined (bool), txt (labels or None)."""
    out = [_open(h, label)]
    grid, y, L, R, T, B, pw, ph = _frame(h, ymin, ymax, yfmt, nt=nt)
    out += grid
    n = len(cats)
    slot = pw / float(n)
    k = 1 if stacked else len(series)
    bw = min(maxbar, slot * 0.74 / k)
    for i, c in enumerate(cats):
        cx = L + slot * (i + 0.5)
        out.append('<text x="%.1f" y="%d" font-size="12" fill="#444" text-anchor="middle">%s</text>' % (cx, h - B + 18, esc(c)))
        base = ymin
        for j, s in enumerate(series):
            v = s["vals"][i]
            if v is None:
                continue
            if stacked:
                x0, lo, hi = cx - bw / 2, base, base + v
                base = hi
            else:
                x0, lo, hi = cx - bw * k / 2 + bw * j, min(v, max(ymin, 0)), max(v, max(ymin, 0))
            y0, y1 = y(hi), y(lo)
            fill = "#ffffff" if s.get("outlined") else s["color"]
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="%s"/>' % (
                x0 + 1, y0, bw - 2, max(0.5, y1 - y0), fill, s["color"], 2 if s.get("outlined") else 0))
            t = s.get("txt")
            if t and t[i]:
                ty = (y0 + y1) / 2 + 4 if stacked else y0 - 5
                col = "#fff" if (stacked and not s.get("outlined")) else INK
                out.append('<text x="%.1f" y="%.1f" font-size="12" fill="%s" text-anchor="middle">%s</text>' % (x0 + bw / 2, ty, col, esc(t[i])))
    if hline:
        yy = y(hline[0])
        out.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.5" stroke-dasharray="5 4"/>' % (L, yy, W - R, yy, hline[2]))
        out.append('<text x="%d" y="%.1f" font-size="12" fill="%s">%s</text>' % (L + 6, yy - 5, hline[2], esc(hline[1])))
    out.append("</svg>")
    return "".join(out)


def lines(label, n, series, ymin, ymax, yfmt, xticks, hlines=(), vlines=(), h=300, nt=5, pad=0):
    """series: dicts with vals (len n, None allowed), color, dash ('' | '6 4' | '2 4'), marker (bool). xticks: (index, text)."""
    out = [_open(h, label)]
    grid, y, L, R, T, B, pw, ph = _frame(h, ymin, ymax, yfmt, nt=nt)
    out += grid

    def x(i):
        return L + pad + (pw - 2 * pad) * (i / float(max(1, n - 1)))

    for i, t in xticks:
        out.append('<text x="%.1f" y="%d" font-size="12" fill="#444" text-anchor="middle">%s</text>' % (x(i), h - B + 18, esc(t)))
    for i, t, col in vlines:
        out.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>' % (x(i), T, x(i), h - B, col))
        out.append('<text x="%.1f" y="%d" font-size="11" fill="%s" text-anchor="end">%s</text>' % (x(i) - 4, T + 11, col, esc(t)))
    for yv, t, col in hlines:
        out.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.5" stroke-dasharray="5 4"/>' % (L, y(yv), W - R, y(yv), col))
        out.append('<text x="%d" y="%.1f" font-size="12" fill="%s">%s</text>' % (L + 6, y(yv) - 5, col, esc(t)))
    for s in series:
        seg = []
        for i, v in enumerate(s["vals"]):
            if v is None:
                if len(seg) > 1:
                    out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2" stroke-linejoin="round" stroke-dasharray="%s"/>' % (" ".join(seg), s["color"], s.get("dash", "")))
                seg = []
                continue
            seg.append("%.1f,%.1f" % (x(i), y(v)))
            if s.get("marker"):
                out.append('<circle cx="%.1f" cy="%.1f" r="4" fill="%s" stroke="#fff" stroke-width="1.5"/>' % (x(i), y(v), s["color"]))
                if s.get("txt"):
                    out.append('<text x="%.1f" y="%.1f" font-size="12" fill="%s" text-anchor="middle">%s</text>' % (x(i), y(v) - 9, INK, esc(s["txt"][i])))
        if len(seg) > 1:
            out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2" stroke-linejoin="round" stroke-dasharray="%s"/>' % (" ".join(seg), s["color"], s.get("dash", "")))
    out.append("</svg>")
    return "".join(out)


def waterfall(label, cats, spans, ymax, yfmt, h=290):
    """spans: (lo, hi, color, text)."""
    out = [_open(h, label)]
    grid, y, L, R, T, B, pw, ph = _frame(h, 0, ymax, yfmt)
    out += grid
    slot = pw / float(len(cats))
    bw = min(70, slot * 0.6)
    for i, (c, (lo, hi, col, txt)) in enumerate(zip(cats, spans)):
        cx = L + slot * (i + 0.5)
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (cx - bw / 2, y(max(lo, hi)), bw, abs(y(lo) - y(hi)), col))
        out.append('<text x="%.1f" y="%.1f" font-size="13" fill="%s" text-anchor="middle">%s</text>' % (cx, y(max(lo, hi)) - 6, INK, esc(txt)))
        out.append('<text x="%.1f" y="%d" font-size="12" fill="#444" text-anchor="middle">%s</text>' % (cx, h - B + 18, esc(c)))
    out.append("</svg>")
    return "".join(out)


def hbars(label, names, vals, colors, fmt, xmax):
    rh = 26
    h = 20 + rh * len(names) + 10
    L, R = 170, 60
    out = [_open(h, label)]
    for i, (nm, v, col) in enumerate(zip(names, vals, colors)):
        yy = 14 + rh * i
        w = (W - L - R) * v / float(xmax)
        out.append('<text x="%d" y="%d" font-size="13" fill="#333" text-anchor="end">%s</text>' % (L - 8, yy + 13, esc(nm)))
        out.append('<rect x="%d" y="%d" width="%.1f" height="16" fill="%s"/>' % (L, yy, w, col))
        out.append('<text x="%.1f" y="%d" font-size="12" fill="%s">%s</text>' % (L + w + 6, yy + 13, INK, esc(fmt(v))))
    out.append("</svg>")
    return "".join(out)
