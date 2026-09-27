"""
Search for a 6x6 residue grid.
Fill with residues 0..5, each exactly 6 times.
Every row sum and column sum == 0 mod 6.

Strategy: Use constraint programming / backtracking with pruning.
Represent each row as a multiset of 6 residues (from 0..5, total count of each residue across all rows = 6).
Row sum must be 0 mod 6. Total sum of all entries = 6*(0+1+2+3+4+5) = 6*15 = 90, which is 0 mod 6. Good.

We enumerate rows: each row is a sorted tuple of 6 residues summing to 0 mod 6.
Then we need to pick 6 rows (with repetition allowed as multisets, but tracking counts)
such that the total count of each residue is exactly 6, AND there's a column assignment
where each column also sums to 0 mod 6.

This is a 2D problem. Let me use a smarter approach: ILP via PuLP or just backtracking.

Actually let me try a direct backtracking: fill cell by cell (row by row, left to right),
tracking remaining counts of each residue, and check row sums at end of each row,
and column sums at the end.

Pruning: at the end of each row, check row sum mod 6 == 0.
At the end (row 6), check all column sums mod 6 == 0.
Track remaining counts; if any count goes negative, prune.
Also: at the last row, the entries are forced by column-sum and remaining-count constraints.

Let me make it efficient with the last-row forced.
"""

import sys
from itertools import product

def solve():
    n = 6
    target_counts = [n]*n  # each residue used n times
    counts = list(target_counts)
    grid = [[None]*n for _ in range(n)]
    col_sum = [0]*n
    
    solutions = []
    
    def backtrack(r, c, remaining_total):
        if r == n:
            # check column sums
            for j in range(n):
                if col_sum[j] % n != 0:
                    return
            solutions.append([row[:] for row in grid])
            return True if len(solutions) >= 1 else False  # find first
        
        if c == n:
            # row complete, check row sum
            if sum(grid[r]) % n != 0:
                return False
            return backtrack(r+1, 0, remaining_total)
        
        # For the last row, entries are forced by column sums and counts
        # Actually let's just try all residues with count > 0
        # Pruning: remaining cells in row r from column c to n-1 is (n - c)
        # remaining_total counts must fit
        
        # Strong pruning for last row
        if r == n-1 and c == 0:
            # Last row is forced: for each column j, the entry must make col_sum[j] + entry ≡ 0 mod n
            # So entry_j = (-col_sum[j]) mod n. Check counts match.
            forced = [(-col_sum[j]) % n for j in range(n)]
            # check counts
            need = [0]*n
            for f in forced:
                need[f] += 1
            for i in range(n):
                if need[i] != counts[i]:
                    return False
            # check row sum
            if sum(forced) % n != 0:
                return False
            grid[r] = forced[:]
            solutions.append([row[:] for row in grid])
            return True
        
        # try residues in order
        for v in range(n):
            if counts[v] > 0:
                # prune: enough remaining cells to place remaining counts? basic
                grid[r][c] = v
                counts[v] -= 1
                col_sum[c] += v
                ok = backtrack(r, c+1, remaining_total-1)
                if ok:
                    return True
                col_sum[c] -= v
                counts[v] += 1
                grid[r][c] = None
        return False
    
    backtrack(0, 0, n*n)
    return solutions

sols = solve()
if sols:
    print("FOUND solution for n=6:")
    for row in sols[0]:
        print(row)
    # verify
    g = sols[0]
    from collections import Counter
    cnt = Counter()
    for row in g:
        for x in row:
            cnt[x]+=1
    print("counts:", dict(sorted(cnt.items())))
    print("row sums mod 6:", [sum(r)%6 for r in g])
    print("col sums mod 6:", [sum(g[i][j] for i in range(6))%6 for j in range(6)])
else:
    print("No solution found for n=6")
