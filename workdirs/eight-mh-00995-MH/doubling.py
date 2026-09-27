"""
General doubling construction for n = 2m, m odd, m >= 3.

Construction:
1. Form m x m circulant B[j][l] = (j+l) mod m.
2. For each value s in {0,...,m-1}, define a 2x2 block using {s, s, s+m, s+m}.
   Block types:
   Type 1: [[s, s], [s+m, s+m]]  (rows: 2s, 2s+2m; cols: 2s+m, 2s+m)
   Type 2: [[s+m, s+m], [s, s]]  (rows: 2s+2m, 2s; cols: 2s+m, 2s+m)
   Type 3: [[s, s+m], [s, s+m]]  (rows: 2s+m, 2s+m; cols: 2s, 2s+2m)
   Type 4: [[s+m, s], [s+m, s]]  (rows: 2s+m, 2s+m; cols: 2s+2m, 2s)
   Type 5: [[s, s+m], [s+m, s]]  (rows: 2s+m, 2s+m; cols: 2s+m, 2s+m)
   Type 6: [[s+m, s], [s, s+m]]  (rows: 2s+m, 2s+m; cols: 2s+m, 2s+m)

3. Choose s1=0 -> type 5, s2=1 -> type 4, all others -> type 1.
   Conditions: |D3|+|D4| odd (cols), |C| even (rows).
   With |D3|=0, |D4|=1, |D56|=1: |D3|+|D4|=1 odd, |C|=2 even. OK.

4. Replace each entry s in circulant with its 2x2 block -> 2m x 2m grid.
"""

def make_grid(n):
    assert n % 2 == 0 and n >= 6
    m = n // 2
    assert m % 2 == 1 and m >= 3

    # circulant
    B = [[(j + l) % m for l in range(m)] for j in range(m)]

    # block types
    def block(s):
        if s == 0:
            # type 5: [[s, s+m], [s+m, s]]
            return [[s, s + m], [s + m, s]]
        elif s == 1:
            # type 4: [[s+m, s], [s+m, s]]
            return [[s + m, s], [s + m, s]]
        else:
            # type 1: [[s, s], [s+m, s+m]]
            return [[s, s], [s + m, s + m]]

    # build 2m x 2m grid
    grid = [[0] * n for _ in range(n)]
    for j in range(m):
        for l in range(m):
            s = B[j][l]
            blk = block(s)
            grid[2*j][2*l]     = blk[0][0]
            grid[2*j][2*l+1]   = blk[0][1]
            grid[2*j+1][2*l]   = blk[1][0]
            grid[2*j+1][2*l+1] = blk[1][1]

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

# Test for n = 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98
for n in range(6, 101, 4):  # n = 6, 10, 14, ...
    grid = make_grid(n)
    oc, orr, oc2 = verify(grid, n)
    status = "OK" if (oc and orr and oc2) else "FAIL"
    print(f"n={n}: counts={oc} rows={orr} cols={oc2} -> {status}")
    if status == "FAIL":
        print("  grid:", grid)
        break
