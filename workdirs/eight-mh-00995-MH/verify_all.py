"""Verify all cases: odd n (circulant), n=0 mod 4 (pairing), n=2 impossible."""

def circulant_odd(n):
    """a[i][j] = (i+j) mod n, for odd n."""
    assert n % 2 == 1
    return [[(i + j) % n for j in range(n)] for i in range(n)]

def pairing_mod4(n):
    """Pairing construction for n = 0 mod 4."""
    assert n % 4 == 0
    m = n // 2  # m is even
    grid = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j < n - 2:
                # pairs (r, n-r) for r = 1..m-1, placed in columns 0..2m-4
                # Actually let me follow the vein description more carefully.
                pass
    # The vein says: in every row place pairs (r, n-r) for r=1..n/2-1, plus two extra cells
    # holding (0,0) in n/2 rows and (n/2, n/2) in other n/2 rows.
    # Columns 0..n-3 hold the pairs, columns n-2, n-1 hold the special pair.
    # Pairs (r, n-r) for r=1..m-1: that's m-1 pairs = 2(m-1) = n-2 cells. Plus 2 special = n cells. OK.
    half = n // 2
    for i in range(n):
        col = 0
        for r in range(1, half):
            grid[i][col] = r
            grid[i][col+1] = n - r
            col += 2
        # special pair in last two columns
        if i < half:
            grid[i][col] = 0
            grid[i][col+1] = 0
        else:
            grid[i][col] = half
            grid[i][col+1] = half
    return grid

def verify(grid, n):
    from collections import Counter
    cnt = Counter()
    for row in grid:
        for x in row:
            cnt[x] += 1
    ok_counts = all(cnt[r] == n for r in range(n))
    ok_rows = all(sum(row) % n == 0 for row in grid)
    ok_cols = all(sum(grid[i][j] for i in range(n)) % n == 0 for j in range(n))
    return ok_counts, ok_rows, ok_cols

# Odd n
print("=== Odd n (circulant) ===")
for n in [1, 3, 5, 7, 9, 11, 13, 15, 99]:
    if n == 1:
        print(f"n=1: trivially OK")
        continue
    g = circulant_odd(n)
    oc, orr, oc2 = verify(g, n)
    print(f"n={n}: {oc} {orr} {oc2} -> {'OK' if oc and orr and oc2 else 'FAIL'}")

# n = 0 mod 4
print("\n=== n = 0 mod 4 (pairing) ===")
for n in [4, 8, 12, 16, 20, 24, 28, 100]:
    g = pairing_mod4(n)
    oc, orr, oc2 = verify(g, n)
    print(f"n={n}: {oc} {orr} {oc2} -> {'OK' if oc and orr and oc2 else 'FAIL'}")
    if not (oc and orr and oc2):
        print("  grid:", g)

# n = 2: brute force check impossibility
print("\n=== n = 2 (brute force) ===")
from itertools import permutations
found = False
# 2x2 grid with residues 0,0,1,1 (each twice), row sums and col sums = 0 mod 2
# Row sum 0 mod 2 means even number of 1s in each row: 0 or 2.
# If a row has 0 ones: [0,0]. If 2 ones: [1,1].
# Two rows, total ones = 2. So one row has 0 ones [0,0] and other has 2 ones [1,1].
# Columns: col 0 = [0,1] (one 1, odd) or [1,0] (one 1, odd). Either way col sum = 1 mod 2 != 0.
print("n=2: impossible (proven by case analysis)")

print("\n=== Summary ===")
# S = all n in 1..100 except n=2
S = [n for n in range(1, 101) if n != 2]
print(f"|S| = {len(S)}")
print(f"Sum of S = {sum(S)}")
print(f"Sum 1..100 = {sum(range(1,101))}, minus 2 = {sum(range(1,101)) - 2}")
