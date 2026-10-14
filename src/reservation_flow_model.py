"""Reservation/backlog flow model: does the pasted critique's 'crossover' claim survive?

Model: each quarter, GEV's opening firm backlog (B) and reservation pool (S) evolve as
  B_end = B + D + C - H      (direct orders in, conversions in, shipments out)
  S_end = S + N - C          (new reservations in, conversions out)
where D=new direct orders, N=new reservations, C=conversions (SRA->order), H=shipped GW.

The critique's own assumptions: D=2, N=18, C=10, H=5 per quarter (mirrors the actual
just-reported Q2'26 pace). Its own algebraic condition for B_end > S_end after one step:
  C > (S - B + N - D + H) / 2
This script (a) reproduces the critique's table under its stated assumptions to see if it
checks out, and (b) sweeps C and N to find the actual combinations where a crossover happens
by Q4, since that is the real, reusable answer regardless of who is right about the table.
"""
B0, S0 = 53.0, 63.0  # June 30, 2026 actuals (8-K/EX Q2'26)

def step(B, S, D, N, C, H):
    return B + D + C - H, S + N - C

def run(D, N, C, H, quarters=2):
    B, S = B0, S0
    path = [(B, S)]
    for _ in range(quarters):
        B, S = step(B, S, D, N, C, H)
        path.append((B, S))
    return path

print("=== Reproducing the critique's own table under its own stated assumptions ===")
print("D=2, N=18, C=10, H=5 per quarter, from B0=%.0f S0=%.0f" % (B0, S0))
path = run(D=2, N=18, C=10, H=5, quarters=2)
labels = ["Jun 30 (actual)", "Q3 (modeled)", "Q4 (modeled)"]
for lab, (B, S) in zip(labels, path):
    pct = None
    print("  %-16s firm=%.1f  reservations=%.1f  total=%.1f  %s" % (
        lab, B, S, B + S, "firm > reservations" if B > S else "reservations still ahead"))
print("  Critique's stated table: Q3 firm=59 res=62 | Q4 firm=65 res=61 (crossover at Q4)")
print("  This model:              Q3 firm=%.0f res=%.0f | Q4 firm=%.0f res=%.0f (%s)" % (
    path[1][0], path[1][1], path[2][0], path[2][1],
    "crossover" if path[2][0] > path[2][1] else "NO crossover"))

print("\n=== The critique's own crossover condition, evaluated at its own assumptions ===")
# C > (S - B + N - D + H) / 2, applied at the opening point each step
for i, (B, S) in enumerate(path[:-1]):
    need = (S - B + 18 - 2 + 5) / 2
    print("  Before quarter %d: need C > %.1f to cross THIS quarter (assumed C=10 -> %s)" % (
        i + 1, need, "crosses" if 10 > need else "does not cross"))

print("\n=== Sweep: what (N, C) combinations produce a Q4 crossover, holding D=2, H=5 ===")
print("  %6s" % "N\\C", end="")
for C in range(6, 21, 2):
    print("%6d" % C, end="")
print()
for N in range(6, 21, 2):
    print("  %6d" % N, end="")
    for C in range(6, 21, 2):
        B, S = run(D=2, N=N, C=C, H=5, quarters=2)[-1]
        print("%6s" % ("YES" if B > S else "no"), end="")
    print()
print("  Rows = new reservations/quarter, columns = conversions/quarter. YES = firm backlog")
print("  exceeds reservations by Q4 under that combination.")

print("\n=== Bottom line ===")
crosses_at_stated = run(D=2, N=18, C=10, H=5, quarters=2)[-1]
print("  At the pace GEV actually just reported (N=18, C=10), backlog does NOT catch")
print("  reservations by Q4: firm=%.0f vs reservations=%.0f." % crosses_at_stated)
print("  A crossover needs EITHER conversions to rise well above the current pace,")
print("  OR new reservations to slow well below it -- not 'maintain the current pace.'")
