# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   24.3.9 * A shape obtained by removing a unit square from each corner of a $3 \times 3$ square is called a “cross-shape”.

On a $10 \times 11$ chessboard, what is the maximum number of non-overlapping “cross-shapes” that can be placed? (Each “cross-shape” exactly covers 5 small squares on the chessboard.)       — 题目文本
#   Analysis Answer: 15.

First, prove that the maximum number of "crosses" that can be placed is 15. Use proof by contradiction, assuming that 16 "crosses" can be placed.

For each "cross," we call the central square the "heart" (denoted as *). Remove the outermost layer of squares from the $10 \times 11$ chessboard, resulting in an $8 \times 9$ grid. Clearly, the "heart" of each "cross" can only appear within this $8 \times 9$ grid.
Note that in every $3 \times 3$ grid, at most two "hearts" can be placed:
We will discuss how to place as many "hearts" as possible in an $8 \times 3$ grid. Divide the $8 \times 3$ grid from top to bottom into three sub-grids: $3 \times 3$, $2 \times 3$, and $3 \times 3$. If one "heart" is placed in the middle $2 \times 3$ grid, then since at most two "hearts" can be placed in each $3 \times 3$ grid, a total of 5 "hearts" can be placed. If two "hearts" are placed in the middle $2 \times 3$ grid, then a total of 6 "hearts" can be placed in the $8 \times 3$ grid, at which point the third and sixth rows must be empty. Through exhaustive enumeration, it is known that there are only the two placement methods shown in the following diagram:
Now, divide the $8 \times 9$ grid into three $8 \times 3$ grids, from left to right, called grid (a), grid (b), and grid (c). Since there are 16 "hearts" in the $8 \times 9$ grid, one of the $8 \times 3$ grids must have 6 "hearts".

If grid (b) has 6 "hearts," since there are only two mutually symmetrical ways to place 6 "hearts" in an $8 \times 3$ grid, we can assume the 6 "hearts" are distributed as shown in the left diagram below:

It is easy to see that the 3rd and 7th columns cannot have "hearts." Thus, it is not difficult to see that at most 4 "hearts" can be placed in grids (a) and (c), resulting in a total of $4+6+4=14$ "hearts," leading to a contradiction.

If grids (a) and (c) each have 6 "hearts," then the 4th and 6th columns cannot have "hearts," so only the middle column in grid (b) can have "hearts." It is not difficult to see that at most 3 "hearts" can be placed in grid (b), resulting in a total of $6+3+6=15$ "hearts," also leading to a contradiction.

If 6 "hearts" are placed in either grid (a) or grid (c), assume 6 "hearts" are placed in grid (a), and they are placed as shown in the right diagram above. In this case, the 4th column cannot have "hearts," so at most 4 "hearts" can be placed in grid (b), resulting in a total of $6+4+5=15$ "hearts," also leading to a contradiction.
In summary, it is known that at most 15 "hearts" can be placed in the $8 \times 9$ grid.
Finally, in addition to the two examples already provided, we give two more examples to show that indeed 15 "hearts" can be placed:  — 标准解答
#   Let me solve this problem. A cross-shape is a 3x3 square with unit squares removed from each corner, leaving 5 squares (the center plus the 4 edge-midpoints). On a 10x11 board, find the maximum number of non-overlapping cross-shapes.

Let me think about this carefully.

A cross-shape covers 5 cells: the center of a 3x3 block, plus the 4 cells adjacent to it (up, down, left, right). So it's a plus/cross shape.

The board is 10x11 = 110 cells. Each cross covers 5 cells, so the upper bound is 110/5 = 22.

But can we achieve 22? That would require tiling the entire board with crosses. Let me think about whether that's possible.

Let me use a coloring argument. Color the board in a checkerboard pattern. A cross-shape centered at a cell covers that cell and its 4 neighbors. If the center is black, the 4 neighbors are white. So each cross covers 1 black + 4 white (if center is black) or 4 black + 1 white (if center is white).

On a 10x11 board, the number of black and white cells: 110 cells, 55 black and 55 white (since 110 is even).

If we have k crosses with black centers and m crosses with white centers, total black covered = k + 4m, total white covered = 4k + m. For a tiling (22 crosses), we need k + 4m = 55 and 4k + m = 55. Adding: 5k + 5m = 110, so k + m = 22. Subtracting: 3m - 3k = 0, so k = m = 11. So we'd need 11 black-centered and 11 white-centered crosses. That's consistent so far.

Let me think about a different coloring. Let me try coloring by columns mod something, or a more refined coloring.

Actually, let me think about this differently. Let me consider the problem more carefully.

Let me try a coloring with 4 colors based on (row mod 2, col mod 2). Actually, let me think about what constraints crosses impose.

A cross centered at (r, c) covers (r,c), (r-1,c), (r+1,c), (r,c-1), (r,c+1).

Let me try coloring by row+col mod 4 or something.

Actually, let me think about a known approach. Let me try to find the answer by construction and upper bound.

Upper bound: 22 (area bound). But is it achievable?

Let me think about whether 22 is achievable. We need to tile 10x11 completely with crosses.

Consider coloring columns with period 4: columns 1,2,3,4,5,6,7,8,9,10,11 (if 11 columns) colored A,B,C,D,A,B,C,D,A,B,C.

Hmm, let me think about a different approach. Let me consider the board coordinates (i,j) with 1≤i≤10, 1≤j≤11.

Let me try a coloring where I color cell (i,j) based on (i + 2j) mod 5 or something to get a bound.

Actually, let me think about this more carefully. Let me try to find a construction for 22 first, and if it fails, find the right upper bound.

For a tiling, consider the cross centered at (i,j). It covers cells with these (row, col) values. The sum of (i+j) mod 2 for the 5 cells: center has parity p, the 4 neighbors have parity 1-p. So 1 cell with parity p and 4 with parity 1-p.

Let me try a coloring mod 5. Color cell (i,j) with color (i + 2j) mod 5. For a cross centered at (i,j):
- Center: (i + 2j) mod 5
- Up (i-1,j): (i-1+2j) mod 5 = center - 1
- Down (i+1,j): center + 1
- Left (i,j-1): center - 2
- Right (i,j+1): center + 2

So the cross covers colors {c-1, c, c+1, c-2, c+2} mod 5 = all 5 colors! Each cross covers exactly one cell of each color mod 5.

So if we color by (i + 2j) mod 5, each cross covers exactly one of each color. For a complete tiling, we need each color to appear exactly 22 times on the board.

Let me count. The board is 10 rows × 11 columns. Color of (i,j) = (i + 2j) mod 5, where i from 1..10, j from 1..11.

For a fixed i, as j goes 1..11, 2j mod 5 cycles through: 2,4,1,3,0,2,4,1,3,0,2 (period 5). So in 11 columns, the values 2j mod 5 are: {2,4,1,3,0} each appearing twice, plus one extra 2 (the 11th). So counts: 0→2, 1→2, 2→3, 3→2, 4→2.

Then (i + 2j) mod 5 = (i mod 5 + 2j mod 5) mod 5. For fixed i, this shifts the distribution. Over all 10 rows, i mod 5 takes values 1,2,3,4,0,1,2,3,4,0 — each value appears twice.

For each row i, the color distribution is a cyclic shift of {0:2, 1:2, 2:3, 3:2, 4:2} by i mod 5.

Total count for color c = sum over i of (count of c in row i).

For rows with i mod 5 = 0: distribution {0:2,1:2,2:3,3:2,4:2}, shifted by 0 → same.
For rows with i mod 5 = 1: shifted by 1 → {1:2,2:2,3:3,4:2,0:2}.
For rows with i mod 5 = 2: shifted by 2 → {2:2,3:2,4:3,0:2,1:2}.
For rows with i mod 5 = 3: shifted by 3 → {3:2,4:2,0:3,1:2,2:2}.
For rows with i mod 5 = 4: shifted by 4 → {4:2,0:2,1:3,2:2,3:2}.

Each i mod 5 value appears in 2 rows. So total for color c:
- Color 0: 2×2 (from i≡0) + 2×2 (from i≡1, where 0 gets 2) + 2×2 (from i≡2, where 0 gets 2) + 2×3 (from i≡3, where 0 gets 3) + 2×2 (from i≡4, where 0 gets 2) = 4+4+4+6+4 = 22.
- Color 1: 2×2 + 2×2 + 2×2 + 2×2 + 2×3 = 4+4+4+4+6 = 22.
- Color 2: 2×3 + 2×2 + 2×2 + 2×2 + 2×2 = 6+4+4+4+4 = 22.
- Color 3: 2×2 + 2×3 + 2×2 + 2×2 + 2×2 = 4+6+4+4+4 = 22.
- Color 4: 2×2 + 2×2 + 2×3 + 2×2 + 2×2 = 4+4+6+4+4 = 22.

Each color appears exactly 22 times. So the mod-5 coloring doesn't rule out a tiling. Good, so 22 is not ruled out by this coloring.

Hmm, so maybe 22 is achievable? Let me think harder.

Actually wait, let me reconsider. The fact that each color appears 22 times and each cross covers one of each color means that IF a tiling exists, it's consistent. But it doesn't prove a tiling exists. Let me try to construct one.

Actually, let me reconsider the problem. 10×11 = 110, and 110/5 = 22. Let me try to actually construct a tiling.

A cross centered at (i,j) requires 2≤i≤9 and 2≤j≤10 (so that all 5 cells are on the board). Wait, the board is 10 rows × 11 columns. So valid centers are i from 2..9 and j from 2..10. That's 8 × 9 = 72 possible centers, and we need to choose 22 non-overlapping ones.

Let me try to think about tiling. Let me try a pattern.

Consider placing crosses in a regular grid. If I place crosses at centers (i,j) where i ≡ 2 mod 3 and j ≡ 2 mod 3... no, crosses overlap that way.

Let me think differently. Two crosses overlap if they share a cell. Cross at (i,j) and cross at (i',j') share a cell iff the Manhattan distance between centers is ≤ 2 and they're not the same. Actually more precisely, they overlap iff |i-i'| + |j-j'| ≤ 2 and (i,j) ≠ (i',j'), OR one center is a neighbor of the other's center... Let me think.

Cross at (i,j) covers {(i,j),(i±1,j),(i,j±1)}. Cross at (i',j') covers {(i',j'),(i'±1,j'),(i',j'±1)}. They overlap iff some cell is in both sets. The cells of the first cross are at Manhattan distance ≤1 from (i,j). The cells of the second are at Manhattan distance ≤1 from (i',j'). They share a cell iff there's a cell at distance ≤1 from both centers, i.e., the Manhattan distance between (i,j) and (i',j') is ≤ 2.

So two crosses are non-overlapping iff their centers are at Manhattan distance ≥ 3.

So we need to place 22 points in the grid {2,...,9} × {2,...,10} such that any two are at Manhattan distance ≥ 3, AND the 5-cell crosses centered at these points exactly cover the 10×11 board.

Wait, but actually the centers don't have to be at Manhattan distance ≥ 3 only — they need to be at distance ≥ 3 for non-overlap, but also the crosses must cover the board exactly (for a tiling). For just maximizing the count, we need non-overlap, which means Manhattan distance ≥ 3 between any two centers.

But for a tiling (22 crosses), we need the additional constraint that the crosses cover everything.

Hmm, but the problem asks for the maximum number of non-overlapping crosses, not necessarily a tiling. So the answer could be less than 22 if a tiling isn't possible but we can fit 22 non-overlapping crosses that don't cover everything... wait no, 22 crosses cover 110 cells = the whole board, so 22 non-overlapping crosses would be a tiling.

So the question is: can we place 22 non-overlapping crosses on the 10×11 board? That's equivalent to tiling.

Let me think about whether a tiling exists. Let me try to construct one.

Let me try to think about small cases first. Can we tile a 3×5 rectangle with crosses? 3×5 = 15 = 3 crosses. A cross in a 3×5... center at (2,2) covers (1,2),(2,1),(2,2),(2,3),(3,2). Center at (2,4) covers (1,4),(2,3),(2,4),(2,5),(3,4). These overlap at (2,3)! So we can't place both.

Hmm. Let me think about what rectangles can be tiled.

Actually, let me think about the structure differently. Let me try to tile the 10×11 board.

Let me try a specific construction. Place crosses at centers:
Row 2: (2,2), (2,5), (2,8)
Row 5: (5,3), (5,6), (5,9)  
Row 8: (8,2), (8,5), (8,8)

Wait, let me check distances. (2,2) and (2,5): Manhattan distance 3. Good. (2,2) and (5,3): distance 3+1=4. Good. (2,5) and (5,6): 3+1=4. Good. (5,3) and (5,6): 3. Good. (5,3) and (8,2): 3+1=4. Good.

But this only gives 9 crosses. Let me think about how to get 22.

Actually, let me think about this more systematically. The centers must be at Manhattan distance ≥ 3. In a grid, the maximum number of points at mutual Manhattan distance ≥ 3...

Actually, for a tiling, we need the crosses to cover every cell. Let me think about which cells can be centers and which must be covered.

Every cell must be covered by exactly one cross. A cell (i,j) is covered by a cross centered at (i,j), (i±1,j), or (i,j±1). So every cell must be at Manhattan distance ≤ 1 from some center.

Also, corner cells like (1,1) can only be covered by a cross centered at (1,1) [but that's not a valid center since it's on the edge], (2,1) [not valid], or (1,2) [not valid]. Wait, (1,1) can be covered by a cross centered at (2,1) — but (2,1) is on the edge (column 1), so the cross at (2,1) would need (2,0) which is off the board. So (2,1) is not a valid center.

Hmm wait. Let me reconsider. The center must be such that all 5 cells are on the board. Center at (i,j) needs (i-1,j), (i+1,j), (i,j-1), (i,j+1) all on the board. So 2 ≤ i ≤ 9 and 2 ≤ j ≤ 10 (for a 10×11 board with rows 1-10, cols 1-11).

So cell (1,1) can only be covered by a cross centered at (2,1) or (1,2) — but neither is a valid center! (2,1) has j=1 which is too small, (1,2) has i=1 which is too small.

Wait, that means (1,1) can never be covered by any cross! That means a complete tiling is IMPOSSIBLE.

Let me double-check. The cross centered at (i,j) covers (i,j), (i-1,j), (i+1,j), (i,j-1), (i,j+1). For (1,1) to be covered, we need one of these to equal (1,1):
- (i,j) = (1,1): center at (1,1), but then (0,1) is off-board. Invalid.
- (i-1,j) = (1,1): (i,j) = (2,1), but (2,0) is off-board. Invalid.
- (i+1,j) = (1,1): (i,j) = (0,1). Off-board. Invalid.
- (i,j-1) = (1,1): (i,j) = (1,2), but (0,2) is off-board. Invalid.
- (i,j+1) = (1,1): (i,j) = (1,0). Off-board. Invalid.

So (1,1) cannot be covered by any cross! Similarly, all four corners of the board cannot be covered.

So a tiling is impossible. The maximum is less than 22.

The four corners (1,1), (1,11), (10,1), (10,11) cannot be covered. So at most 110 - 4 = 106 cells can be covered, giving at most floor(106/5) = 21 crosses. But we need to check if 21 is achievable.

Wait, but it's not just about covering cells. We need 21 non-overlapping crosses, which cover 105 cells. The 4 corner cells can't be covered, so we'd have 110 - 105 = 5 uncovered cells, including the 4 corners plus 1 more.

Let me think about the upper bound more carefully. Can we achieve 21?

Let me think about which cells can't be covered. The corners (1,1), (1,11), (10,1), (10,11). Are there other cells that can't be covered?

Cell (1,2): can be covered by center at (2,2) [covers (1,2),(2,1),(2,2),(2,3),(3,2)] — yes, (1,2) is covered. Or center at (1,3) — but (1,3) is not valid (i=1). So (1,2) can be covered by (2,2). Good.

Cell (1,j) for 2 ≤ j ≤ 10: covered by center (2,j). Valid since 2 ≤ 2 ≤ 9 and 2 ≤ j ≤ 10. Good.

Cell (1,11): covered by center (2,11)? But j=11 > 10, so (2,11) is not a valid center. Center (1,10)? i=1, not valid. So (1,11) can't be covered. Confirmed.

So only the 4 corners can't be covered. So the upper bound from area is floor(106/5) = 21.

But we need to verify 21 is achievable. Let me think about whether there are additional constraints.

Let me use the mod-5 coloring again. Each cross covers one cell of each color. With 21 crosses, we cover 21 cells of each color. The board has 22 cells of each color (computed above). So we'd leave 1 cell of each color uncovered. The 4 corners are always uncovered. Let me check the colors of the 4 corners:

(1,1): (1 + 2·1) mod 5 = 3
(1,11): (1 + 22) mod 5 = 23 mod 5 = 3
(10,1): (10 + 2) mod 5 = 12 mod 5 = 2
(10,11): (10 + 22) mod 5 = 32 mod 5 = 2

So the 4 corners have colors 3, 3, 2, 2. If 21 crosses leave 5 cells uncovered (including these 4 corners), the uncovered cells must have one of each color (since 22 - 21 = 1 of each color uncovered). The 4 corners contribute 2 of color 3 and 2 of color 2. So we need 1 more uncovered cell, and the total uncovered should be 1 of each color: color 0: 1, color 1: 1, color 2: 1, color 3: 1, color 4: 1.

But the 4 corners already give color 2: 2 and color 3: 2, which exceeds 1 each. Contradiction!

So with 21 crosses, we'd leave 5 cells uncovered, and by the mod-5 coloring, exactly 1 of each color must be uncovered. But the 4 corners force at least 2 of color 2 and 2 of color 3 to be uncovered. That's a contradiction. So 21 is impossible!

Therefore the maximum is at most 20.

With 20 crosses, we cover 100 cells, leaving 10 uncovered. By the mod-5 coloring, we leave 22 - 20 = 2 of each color uncovered. The 4 corners give colors 3,3,2,2. We need 2 of each color total. So far we have color 2: 2 (done), color 3: 2 (done). We still need color 0: 2, color 1: 2, color 4: 2. That's 6 more uncovered cells, totaling 4 + 6 = 10. Consistent!

So 20 is not ruled out by this argument. Let me check if 20 is achievable.

Actually, let me also verify: is there another coloring that might give a tighter bound?

Let me try other colorings. Let me try (i + 3j) mod 5 or (2i + j) mod 5, etc.

For (2i + j) mod 5: Cross at (i,j) covers:
- Center: 2i + j
- (i-1,j): 2(i-1) + j = 2i + j - 2
- (i+1,j): 2i + j + 2
- (i,j-1): 2i + j - 1
- (i,j+1): 2i + j + 1

So colors {c-2, c-1, c, c+1, c+2} mod 5 = all 5. Same property.

For (i + 3j) mod 5: 
- Center: i + 3j
- (i-1,j): i + 3j - 1
- (i+1,j): i + 3j + 1
- (i,j-1): i + 3j - 3
- (i,j+1): i + 3j + 3

Colors {c-3, c-1, c, c+1, c+3} mod 5 = {c, c±1, c±3} mod 5. Is this all 5? c-3, c-1, c, c+1, c+3 mod 5. If c=0: {2, 4, 0, 1, 3} = all 5. Yes! So any coloring (ai + bj) mod 5 where {0, ±a, ±b} mod 5 = all of {0,1,2,3,4} works. This requires a, b nonzero and a ≠ ±b mod 5.

For (a,b) = (1,2): {0, ±1, ±2} = {0,1,4,2,3} = all 5. ✓
For (a,b) = (1,3): {0, ±1, ±3} = {0,1,4,3,2} = all 5. ✓
For (a,b) = (2,1): same as (1,2). ✓
For (a,b) = (1,4): {0, ±1, ±4} = {0,1,4,4,1} — only 3 values. ✗

So (1,2), (1,3), (2,1), (2,3), (3,1), (3,2) etc. all work. But they all give the same constraint: each cross covers one of each color, so the number of crosses ≤ min color count.

Let me check if different colorings give different color distributions on the 10×11 board, potentially with a smaller minimum.

For (i + 3j) mod 5: For fixed i, 3j mod 5 as j=1..11: 3,1,4,2,0,3,1,4,2,0,3. Counts: 0→2, 1→2, 2→2, 3→3, 4→2. Similar structure, just different color gets the extra. Over 10 rows with i mod 5 each appearing twice, by the same calculation, each color gets 22. Same result.

So all these colorings give 22 per color, and the constraint is the same: uncovered cells must have equal counts per color.

So the upper bound from this method is 20 (as derived above). Let me now try to construct a placement of 20 crosses.

Let me try to construct 20 non-overlapping crosses on the 10×11 board.

The centers must be at mutual Manhattan distance ≥ 3, and within {2..9} × {2..10}.

Let me try a systematic approach. Let me think of the board as 10 rows × 11 columns.

Let me try placing crosses in a pattern. Consider centers at positions where (i mod 3, j mod 3) takes specific values.

If I place centers at (i,j) where i ≡ 2 mod 3 and j ≡ 2 mod 3:
i ∈ {2, 5, 8}, j ∈ {2, 5, 8}. That's 3×3 = 9 centers. Manhattan distance between (2,2) and (2,5) is 3, between (2,2) and (5,2) is 3, between (2,2) and (5,5) is 6. All ≥ 3. Good, 9 crosses.

But I need 20. Let me think about a denser packing.

Actually, the constraint is Manhattan distance ≥ 3. Let me think about the maximum independent set in this graph.

Hmm, let me think about it differently. Let me try to use a pattern that covers more of the board.

Let me try centers at:
- Rows 2, 5, 8 (spaced 3 apart)
- In each row, centers at columns 2, 5, 8 (spaced 3 apart)

That gives 9. But I can also use rows 3, 6, 9 with different column offsets.

Let me try:
Row 2: columns 2, 5, 8 → 3 crosses
Row 3: columns 3, 6, 9 → but (2,2) and (3,3) have Manhattan distance 2. Overlap!

So I can't use adjacent rows with offset 1. Let me think more carefully.

If two centers are in adjacent rows (differ by 1), their columns must differ by ≥ 2. If they're in the same row, columns differ by ≥ 3. If rows differ by 2, columns must differ by ≥ 1. If rows differ by ≥ 3, any columns OK.

Let me try a pattern with rows 2, 4, 6, 8 (every other row):
Row 2: cols 2, 5, 8 → 3
Row 4: cols 3, 6, 9 → check (2,2) vs (4,3): dist = 2+1 = 3. OK. (2,5) vs (4,3): 2+2=4. OK. (2,5) vs (4,6): 2+1=3. OK. (2,8) vs (4,9): 2+1=3. OK. (2,8) vs (4,6): 2+2=4. OK. Good.
Row 6: cols 2, 5, 8 → check (4,3) vs (6,2): 2+1=3. OK. (4,3) vs (6,5): 2+2=4. OK. (4,6) vs (6,5): 2+1=3. OK. (4,6) vs (6,8): 2+2=4. OK. (4,9) vs (6,8): 2+1=3. OK. Good.
Row 8: cols 3, 6, 9 → similar checks pass.

So rows 2,4,6,8 with alternating column offsets {2,5,8} and {3,6,9}:
Row 2: {2,5,8} → 3
Row 4: {3,6,9} → 3
Row 6: {2,5,8} → 3
Row 8: {3,6,9} → 3
Total: 12 crosses.

Can I do better? Let me also use rows 3, 5, 7, 9 or add more.

Actually, let me try to use all even rows: 2, 4, 6, 8. That's 4 rows × 3 = 12. Can I add more in odd rows?

Row 3 is between rows 2 and 4. A center in row 3 must be at distance ≥ 3 from all centers in rows 2 and 4. Centers in row 2 are at cols {2,5,8}, row 4 at cols {3,6,9}. A center at (3, c) must have |3-2| + |c - c'| ≥ 3 for all c' in {2,5,8}, i.e., 1 + |c - c'| ≥ 3, so |c - c'| ≥ 2 for all c' in {2,5,8}. So c ∉ {0,1,2,3,4, 3,4,5,6, 6,7,8,9} = c ∉ {0..9} effectively. And from row 4: |c - c'| ≥ 2 for c' in {3,6,9}, so c ∉ {1..5, 4..8, 7..11} = c ∉ {1..11}. So c must be outside {1..11}, impossible. So no centers in row 3.

Similarly, no centers in rows 5, 7 (between used rows). What about row 9? Row 9 is below row 8. (9, c) vs (8, c') in {3,6,9}: 1 + |c - c'| ≥ 3, so |c - c'| ≥ 2. c ∉ {1..5, 4..8, 7..11} = {1..11}. Impossible.

What about row 10? Not a valid center (i=10, need i≤9). Row 1? Not valid (i=1).

So with this pattern, 12 is what we get. That's not enough. Let me try a different approach.

Let me try using rows 2, 3, 5, 6, 8, 9 (pairs of adjacent rows, then a gap).

Row 2: cols 2, 5, 8 → 3
Row 3: must be at dist ≥ 3 from row 2 centers. |c - c'| ≥ 2 for c' in {2,5,8}. So c ∈ {4, 7, 10} (checking: c=4: |4-2|=2,|4-5|=1 <2. No!). Hmm, c=4: |4-2|=2 ✓, |4-5|=1 ✗. So c=4 doesn't work.

c must satisfy |c-2|≥2 AND |c-5|≥2 AND |c-8|≥2. So c ≤ 0 or c ∈ [4,4] (but |4-5|=1, no) or... Let me compute: c ∉ [0,4] ∪ [3,7] ∪ [6,10] = [0,10]. So c ∈ {11} but also need c ≤ 10 (valid center). So no valid c in row 3. 

Hmm, this is tricky. Let me think differently.

The issue is that in a row with 3 centers spaced 3 apart, the next row can't have any centers (because the gap requirement is too strict).

Let me try rows with only 2 centers, allowing more rows to be used.

Row 2: cols 2, 6 → 2 (distance 4, fine)
Row 3: cols 4, 8 → check vs row 2: (3,4) vs (2,2): 1+2=3 ✓. (3,4) vs (2,6): 1+2=3 ✓. (3,8) vs (2,6): 1+2=3 ✓. (3,8) vs (2,2): 1+6=7 ✓. Good. 2 crosses.
Row 4: cols 2, 6 → check vs row 3: (4,2) vs (3,4): 1+2=3 ✓. (4,2) vs (3,8): 1+6=7 ✓. (4,6) vs (3,4): 1+2=3 ✓. (4,6) vs (3,8): 1+2=3 ✓. Good. 2 crosses.
Row 5: cols 4, 8 → similar. 2 crosses.
...

This gives a pattern: even rows use cols {2,6}, odd rows use cols {4,8}. Wait, but I should also consider more columns.

Actually, let me try to maximize. With cols {2, 6} and {4, 8}, I get 2 per row. Over rows 2-9 (8 rows), that's 16 crosses. Can I add more columns?

Row 2: cols 2, 6, 10 → 3 (distances 4, 4, 8 — all ≥ 3 ✓)
Row 3: need |c - c'| ≥ 2 for c' in {2, 6, 10}. c ∉ [0,4] ∪ [4,8] ∪ [8,12] = [0,12]. So no valid c. Hmm.

So 3 per row blocks the next row entirely. 2 per row with the right offset allows alternating.

With the 2-per-row alternating pattern: rows 2,3,4,5,6,7,8,9 → 8 rows × 2 = 16 crosses. Can I do better?

Let me try 2 per row but with a different column choice to potentially fit 3 in some rows.

Actually, let me try:
Row 2: cols 2, 6, 10 → 3
Row 3: (blocked) → 0
Row 4: cols 2, 6, 10 → 3
Row 5: (blocked) → 0
Row 6: cols 2, 6, 10 → 3
Row 7: (blocked) → 0
Row 8: cols 2, 6, 10 → 3
Row 9: (blocked) → 0
Total: 12. Worse than 16.

What about mixing? 
Row 2: cols 2, 6 → 2
Row 3: cols 4, 8 → 2
Row 4: cols 2, 6 → 2
Row 5: cols 4, 8 → 2
Row 6: cols 2, 6 → 2
Row 7: cols 4, 8 → 2
Row 8: cols 2, 6 → 2
Row 9: cols 4, 8 → 2
Total: 16.

Can I add a 3rd column to some rows? In row 2 with cols {2, 6}, can I add col 10? (2,10) vs (3,8): 1+2=3 ✓. (2,10) vs (3,4): 1+6=7 ✓. So yes! Row 2: cols 2, 6, 10 → 3. But then row 3 with cols {4, 8}: (3,4) vs (2,10): 1+6=7 ✓, (3,8) vs (2,10): 1+2=3 ✓. Still OK!

But wait, does adding col 10 to row 2 block row 3? (3, c) vs (2, 10): need 1 + |c-10| ≥ 3, so |c-10| ≥ 2, c ≤ 8 or c ≥ 12. Row 3 has cols {4, 8}, both ≤ 8. ✓.

What about row 1? Not valid. 

Let me try to add more. Can row 3 also have 3 columns? Row 3: cols 4, 8, and what else? Need distance ≥ 3 from {4, 8} in same row: col c with |c-4|≥3 and |c-8|≥3. c ≤ 1 or c = 11... c ≤ 1: not valid (need ≥ 2). c = 11: not valid (need ≤ 10). Hmm, what about c = 11? No, max is 10. So only 2 in row 3 with this offset.

Wait, what if I use different offsets? Let me try:
Row 2: cols 2, 6, 10 → 3
Row 3: cols 4, 8 → 2
Row 4: cols 2, 6, 10 → 3
Row 5: cols 4, 8 → 2
Row 6: cols 2, 6, 10 → 3
Row 7: cols 4, 8 → 2
Row 8: cols 2, 6, 10 → 3
Row 9: cols 4, 8 → 2
Total: 3+2+3+2+3+2+3+2 = 20!

Let me verify all the distance constraints carefully.

Even rows (2,4,6,8): cols {2, 6, 10}
Odd rows (3,5,7,9): cols {4, 8}

Same-row distances: 
- Even: |2-6|=4, |6-10|=4, |2-10|=8. All ≥ 3. ✓
- Odd: |4-8|=4 ≥ 3. ✓

Adjacent row distances (differ by 1):
- Even row {2,6,10} vs odd row {4,8}: need 1 + |c_even - c_odd| ≥ 3, so |c_even - c_odd| ≥ 2.
  - |2-4|=2 ✓, |2-8|=6 ✓, |6-4|=2 ✓, |6-8|=2 ✓, |10-4|=6 ✓, |10-8|=2 ✓. All ≥ 2. ✓

Two-apart rows (differ by 2):
- Even vs even (e.g., row 2 vs row 4): need 2 + |c - c'| ≥ 3, so |c - c'| ≥ 1. Since all columns are from {2,6,10}, any two different ones differ by ≥ 4. Same column: |c-c|=0, so 2+0=2 < 3. ✗!

Wait, row 2 col 2 and row 4 col 2: Manhattan distance = 2 + 0 = 2 < 3. They overlap!

So this doesn't work. The crosses at (2,2) and (4,2) overlap because (2,2) covers (3,2) and (4,2) covers (3,2). Indeed Manhattan distance 2.

So I need to fix this. For rows differing by 2, columns must differ by ≥ 1.

So even rows can't all use the same columns. Let me adjust.

Let me try:
Row 2: cols 2, 6, 10
Row 3: cols 4, 8
Row 4: cols 3, 7 (shifted by 1 from row 2 to avoid same-column conflict)

Wait, but row 4 vs row 3: {3,7} vs {4,8}: |3-4|=1, need ≥ 2. 1+1=2 < 3. ✗.

Hmm. Let me reconsider.

For rows differing by 2, columns must differ by ≥ 1. For rows differing by 1, columns must differ by ≥ 2.

Let me try a 3-row pattern that repeats:
Row A: cols {2, 6, 10}
Row B: cols {4, 8}
Row C: cols {3, 7} (differs from A by ≥ 1 in each column, differs from B by ≥ 2)

Check B vs C: {4,8} vs {3,7}: |4-3|=1 < 2. ✗.

Try Row C: cols {5, 9}: vs B {4,8}: |5-4|=1 < 2. ✗.

Hmm. The problem is that with cols {4,8} in row B, row C (1 below) needs cols at distance ≥ 2 from both 4 and 8, and row C (2 below A) needs cols at distance ≥ 1 from {2,6,10}.

Distance ≥ 2 from {4,8}: c ∉ {2,3,4,5,6, 6,7,8,9,10} = {2..10}. So c ∈ {11} but max is 10. Or c ≤ 1, min is 2. So no valid columns! 

So the 3-per-row pattern for even rows blocks the row 2 below the odd row. This means we can't have a repeating pattern of ABA with 3 in A rows.

Let me try a different approach. Let me use a 4-row repeating pattern.

Actually, let me step back and think about this more carefully.

Let me try to use a pattern where every row has 2 crosses, but use all 8 rows (2-9), giving 16. Then try to add 4 more in strategic positions.

Or, let me try a different pattern entirely.

Let me think about it as follows. Consider the "diagonal" pattern. Place crosses at positions (i, j) where i + j ≡ 0 mod 3 and i - j ≡ 0 mod 2, or some such lattice.

Actually, let me think about the L∞ metric. Two crosses at (i,j) and (i',j') overlap iff |i-i'| + |j-j'| ≤ 2. Non-overlap requires Manhattan distance ≥ 3.

Let me think about this as a packing problem. I want to maximize the number of points in {2..9} × {2..10} with pairwise Manhattan distance ≥ 3.

The grid is 8 × 9 = 72 points. By an area argument, each point "blocks" a diamond of radius 2 (Manhattan), which has 1 + 4 + 8 = 13 cells... but that's not quite right for a packing bound.

Let me think about it differently. Consider the transformation u = i + j, v = i - j. Manhattan distance ≥ 3 in (i,j) corresponds to max(|Δu|, |Δv|) ≥ 3... no, that's L∞ in (u,v) which corresponds to L1 in (i,j) only if... actually |Δi| + |Δj| = max(|Δu|, |Δv|) is not correct. We have |Δi| + |Δj| = max(|Δu|, |Δv|) only when... no. Actually, |Δi| + |Δj| and max(|Δu|, |Δv|) = max(|Δi+Δj|, |Δi-Δj|). And |Δi| + |Δj| = max(|Δi+Δj|, |Δi-Δj|) is true! Because |a| + |b| = max(|a+b|, |a-b|).

So Manhattan distance in (i,j) = L∞ distance in (u,v) = (i+j, i-j). So we need L∞ distance ≥ 3 in the (u,v) coordinates.

So we need to pack points in the (u,v) plane with L∞ distance ≥ 3, which means we're placing points on a grid with spacing 3 in both u and v directions. The maximum density is 1/9 (one point per 3×3 square in (u,v)).

The (u,v) range: i from 2..9, j from 2..10. u = i+j ranges from 4 to 19. v = i-j ranges from -8 to 7. So u ∈ [4,19] (16 values), v ∈ [-8,7] (16 values). But u and v must have the same parity (since u+v = 2i is even). So effectively, we're on a 16×16 grid (in terms of valid (u,v) pairs with matching parity), but actually the number of valid (u,v) pairs is 72 (same as the number of (i,j) points).

With L∞ spacing 3, we can fit roughly (16/3) × (16/3) ≈ 5.33 × 5.33 ≈ 28 points. But that's an overestimate because of parity constraints and boundary effects.

Hmm, this is getting complicated. Let me just try to construct 20 explicitly.

Let me try a different approach. Let me use the (u,v) = (i+j, i-j) transformation and place points on a lattice.

If I place points at (u,v) where u ≡ a mod 3 and v ≡ b mod 3, then any two points have L∞ distance ≥ 3 (actually, they have L∞ distance that's a multiple of 3, so ≥ 3 if distinct). But I need u ≡ v mod 2 (parity constraint).

Let me try u ≡ 0 mod 3, v ≡ 0 mod 3. Then u ∈ {6, 9, 12, 15, 18}, v ∈ {-6, -3, 0, 3, 6}. But need u ≡ v mod 2: 6≡0, -6≡0: same parity ✓. 9≡1, -3≡1: same ✓. 12≡0, 0≡0 ✓. 15≡1, 3≡1 ✓. 18≡0, 6≡0 ✓. So all combinations where u and v have the same parity.

u=6 (even): v must be even: {-6, 0, 6} → 3 points
u=9 (odd): v must be odd: {-3, 3} → 2 points
u=12 (even): v even: {-6, 0, 6} → 3 points
u=15 (odd): v odd: {-3, 3} → 2 points
u=18 (even): v even: {-6, 0, 6} → 3 points

Total: 3+2+3+2+3 = 13 points.

Let me try u ≡ 1 mod 3, v ≡ 1 mod 3. u ∈ {4, 7, 10, 13, 16, 19}, v ∈ {-8, -5, -2, 1, 4, 7}.
Parity: u=4 (even), v must be even: {-8, -2, 4} → 3
u=7 (odd), v odd: {-5, 1, 7} → 3
u=10 (even), v even: {-8, -2, 4} → 3
u=13 (odd), v odd: {-5, 1, 7} → 3
u=16 (even), v even: {-8, -2, 4} → 3
u=19 (odd), v odd: {-5, 1, 7} → 3
Total: 18 points!

Let me verify these map to valid (i,j). For each (u,v), i = (u+v)/2, j = (u-v)/2. Need 2 ≤ i ≤ 9, 2 ≤ j ≤ 10.

u=4, v=-8: i=(4-8)/2=-2. Invalid.
u=4, v=-2: i=(4-2)/2=1. Invalid (need ≥2).
u=4, v=4: i=(4+4)/2=4, j=(4-4)/2=0. Invalid (need ≥2).

Hmm, u=4 is too small. Let me check which (u,v) pairs give valid (i,j).

i = (u+v)/2, j = (u-v)/2. Need 2 ≤ (u+v)/2 ≤ 9 and 2 ≤ (u-v)/2 ≤ 10.
So 4 ≤ u+v ≤ 18 and 4 ≤ u-v ≤ 20.

Let me enumerate for u ≡ 1 mod 3, v ≡ 1 mod 3:

u=4: v ∈ {-8,-2,4}. 
  v=-8: u+v=-4 <4. Invalid.
  v=-2: u+v=2 <4. Invalid.
  v=4: u-v=0 <4. Invalid.

u=7: v ∈ {-5,1,7}.
  v=-5: u+v=2 <4. Invalid.
  v=1: u+v=8 ✓, u-v=6 ✓. i=4, j=3. Valid!
  v=7: u+v=14 ✓, u-v=0 <4. Invalid.

u=10: v ∈ {-8,-2,4}.
  v=-8: u+v=2 <4. Invalid.
  v=-2: u+v=8 ✓, u-v=12 ✓. i=4, j=6. Valid!
  v=4: u+v=14 ✓, u-v=6 ✓. i=7, j=3. Valid!

u=13: v ∈ {-5,1,7}.
  v=-5: u+v=8 ✓, u-v=18 ✓. i=4, j=9. Valid!
  v=1: u+v=14 ✓, u-v=12 ✓. i=7, j=6. Valid!
  v=7: u+v=20 >18. Invalid.

u=16: v ∈ {-8,-2,4}.
  v=-8: u+v=8 ✓, u-v=24 >20. Invalid.
  v=-2: u+v=14 ✓, u-v=18 ✓. i=7, j=9. Valid!
  v=4: u+v=20 >18. Invalid.

u=19: v ∈ {-5,1,7}.
  v=-5: u+v=14 ✓, u-v=24 >20. Invalid.
  v=1: u+v=20 >18. Invalid.
  v=7: u+v=26 >18. Invalid.

Valid points: (4,3), (4,6), (7,3), (4,9), (7,6), (7,9). That's only 6 points! Much less than 18.

The issue is many (u,v) pairs map outside the board. The (u,v) region is a rotated rectangle, not axis-aligned, so the lattice doesn't pack as well.

Let me try a different lattice. Let me try u ≡ 0 mod 3, v ≡ 0 mod 3:

u ∈ {6, 9, 12, 15, 18}, v ∈ {-6, -3, 0, 3, 6}.

u=6 (even), v even {-6, 0, 6}:
  v=-6: u+v=0 <4. Invalid.
  v=0: u+v=6 ✓, u-v=6 ✓. i=3, j=3. Valid!
  v=6: u+v=12 ✓, u-v=0 <4. Invalid.

u=9 (odd), v odd {-3, 3}:
  v=-3: u+v=6 ✓, u-v=12 ✓. i=3, j=6. Valid!
  v=3: u+v=12 ✓, u-v=6 ✓. i=6, j=3. Valid!

u=12 (even), v even {-6, 0, 6}:
  v=-6: u+v=6 ✓, u-v=18 ✓. i=3, j=9. Valid!
  v=0: u+v=12 ✓, u-v=12 ✓. i=6, j=6. Valid!
  v=6: u+v=18 ✓, u-v=6 ✓. i=9, j=3. Valid!

u=15 (odd), v odd {-3, 3}:
  v=-3: u+v=12 ✓, u-v=18 ✓. i=6, j=9. Valid!
  v=3: u+v=18 ✓, u-v=12 ✓. i=9, j=6. Valid!

u=18 (even), v even {-6, 0, 6}:
  v=-6: u+v=12 ✓, u-v=24 >20. Invalid.
  v=0: u+v=18 ✓, u-v=18 ✓. i=9, j=9. Valid!
  v=6: u+v=24 >18. Invalid.

Valid: (3,3), (3,6), (6,3), (3,9), (6,6), (9,3), (6,9), (9,6), (9,9). That's 9 points.

These are the points where i ≡ 0 mod 3 and j ≡ 0 mod 3 (with i,j ∈ {3,6,9}). That's the 3×3 grid I found earlier.

Let me try combining two lattices. For example, u ≡ 0 mod 3, v ≡ 0 mod 3 AND u ≡ 1 mod 3, v ≡ 2 mod 3 (or some other shift). But I need to ensure cross-lattice distances are also ≥ 3.

Two points from different lattices: (u1, v1) with u1 ≡ 0, v1 ≡ 0 and (u2, v2) with u2 ≡ 1, v2 ≡ 2. Then Δu = u2 - u1 ≡ 1 mod 3, so |Δu| ≥ 1. Δv = v2 - v1 ≡ 2 mod 3, so |Δv| ≥ 2. L∞ distance = max(|Δu|, |Δv|) ≥ 2. But we need ≥ 3! So this doesn't work if |Δu| = 1 and |Δv| = 2.

Hmm. So combining lattices with shifts (1,2) gives L∞ distance potentially 2, which is too small.

For L∞ ≥ 3, I need both |Δu| ≥ 3 or both shifts to be 0 mod 3. So I can only use one lattice (one residue class mod 3 in both u and v). Unless I use a different spacing.

What if I use spacing 3 in one direction and something else in the other? Or a non-lattice arrangement?

Let me think about this differently. The maximum number of points with L∞ distance ≥ 3 in the (u,v) diamond-shaped region.

Actually, let me just try to construct 20 crosses directly by hand, or use a computer search... but I can't use tools. Let me think more carefully.

Let me reconsider. The (u,v) region: u = i+j, v = i-j, with 2≤i≤9, 2≤j≤10. The region is a parallelogram (rotated rectangle). In (u,v) coordinates, the constraints are:
- 4 ≤ u+v ≤ 18 (from 2≤i≤9)
- 4 ≤ u-v ≤ 20 (from 2≤j≤10)

And u, v have the same parity.

The L∞ distance ≥ 3 constraint means we're looking for an independent set in a grid graph with spacing 3.

The maximum number of points with L∞ ≥ 3 in a region is roughly area / 9. The area of the (u,v) region: it's a parallelogram. The original region has 72 points (8×9). In (u,v) space, the "area" per point is 2 (since (u,v) and (u+1,v+1) map to the same (i,j) if parity matches... actually the mapping is 1-1 for same-parity pairs). The parallelogram has vertices at (u,v) = (4,0), (12,-8), (18,0), (12,8)... let me compute:

Corners of the (i,j) region: (2,2)→(4,0), (2,10)→(12,-8), (9,2)→(11,7), (9,10)→(19,-1).

Hmm, it's a parallelogram with vertices (4,0), (12,-8), (19,-1), (11,7). The area = |det| of the side vectors. Side 1: (12,-8)-(4,0) = (8,-8). Side 2: (11,7)-(4,0) = (7,7). Area = |8·7 - (-8)·7| = |56+56| = 112. But this is in (u,v) space where each (i,j) point takes up 2 units of area (since u,v change by 2 for each step in i or j). So number of points ≈ 112/2 = 56... but we know there are 72 points. Let me recheck.

Actually, the mapping (i,j) → (u,v) = (i+j, i-j) has Jacobian 2. So area in (u,v) = 2 × area in (i,j) = 2 × 72 = 144. But the parallelogram area I computed is 112. Let me recheck the vertices.

(i,j) region: i from 2 to 9 (8 values), j from 2 to 10 (9 values). This is a rectangle with corners (2,2), (2,10), (9,2), (9,10).

(2,2) → u=4, v=0
(2,10) → u=12, v=-8
(9,2) → u=11, v=7
(9,10) → u=19, v=-1

Parallelogram with vertices (4,0), (12,-8), (19,-1), (11,7).
Side vectors: (12,-8)-(4,0) = (8,-8) and (11,7)-(4,0) = (7,7).
Area = |8·7 - (-8)·7| = |56 + 56| = 112.

But 2 × 8 × 9 = 144 ≠ 112. Something's wrong. Oh, the mapping (i,j) → (i+j, i-j) has Jacobian |det([[1,1],[1,-1]])| = |-2| = 2. So area in (u,v) = 2 × area in (i,j). The (i,j) rectangle has area 7 × 8 = 56 (continuous area, from 2 to 9 is length 7, from 2 to 10 is length 8). 2 × 56 = 112. ✓. The number of integer points is 8 × 9 = 72, and in (u,v) space with the parity constraint, we also get 72 points.

For L∞ packing with spacing 3, the max number of points is roughly area/9 = 112/9 ≈ 12.4. But this is a rough estimate. With the parity constraint and boundary effects, it could be more or less.

Hmm, 12 is close to what I got with the lattice. But I need 20. That seems way more than 12. Am I making an error?

Wait, I think I'm overcomplicating this. Let me reconsider.

Oh wait, I think the issue is that L∞ distance ≥ 3 in (u,v) is a very strong constraint. Each point blocks a 5×5 = 25 cell region (in (u,v) integer grid, but with parity constraint, effectively 13 points). So the max is roughly 72/13 ≈ 5.5... that's way too low.

No wait, that's not right either. The blocking argument gives an upper bound of 72/13 ≈ 5.5, but we already found 9 points with the lattice. The issue is that the blocking regions overlap near the boundary.

Actually, the L∞ distance ≥ 3 constraint means that in the (u,v) grid, we can place at most one point per 3×3 block. The (u,v) region spans u from 4 to 19 (16 values) and v from -8 to 7 (16 values), but only same-parity pairs are valid. If we think of the valid grid as having 16×16 = 256 cells but only 72 valid (same parity), then with 3×3 blocking, we can fit at most ceil(16/3) × ceil(16/3) = 6×6 = 36 points (without parity constraint). With parity, maybe ~18.

But I only found 9 with a single lattice. Let me try to do better by not using a lattice.

Actually, let me reconsider. The L∞ distance ≥ 3 means we need points that are at least 3 apart in both u and v. So if we sort by u, consecutive points differ by ≥ 3 in u OR they differ by ≥ 3 in v. Actually no, L∞ ≥ 3 means max(|Δu|, |Δv|) ≥ 3, which means |Δu| ≥ 3 OR |Δv| ≥ 3. Wait no! L∞ distance ≥ 3 means max(|Δu|, |Δv|) ≥ 3. But we need the distance to be ≥ 3, so we need max(|Δu|, |Δv|) ≥ 3.

Hmm wait, I think I had it backwards. Manhattan distance in (i,j) = |Δi| + |Δj|. And |Δi| + |Δj| = max(|Δi + Δj|, |Δi - Δj|) = max(|Δu|, |Δv|). So Manhattan distance = L∞ distance in (u,v). We need Manhattan ≥ 3, so L∞ ≥ 3, so max(|Δu|, |Δv|) ≥ 3.

But this means we need |Δu| ≥ 3 OR |Δv| ≥ 3. This is much weaker than requiring both! Two points can be close in u as long as they're far in v, and vice versa.

So the constraint is NOT that both |Δu| ≥ 3 and |Δv| ≥ 3. It's that at least one of them is ≥ 3. This means we can pack much more densely!

So in the (u,v) plane, we need an independent set in the graph where two points are connected if both |Δu| ≤ 2 and |Δv| ≤ 2 (i.e., L∞ distance ≤ 2). This is like a kings graph with radius 2.

The maximum independent set in a grid with L∞ distance ≥ 3... this is like a chess problem. We can place points in a "staggered" pattern.

For example, in a 1D line, we can place points every 3 units. In 2D with L∞ ≥ 3, we can place points in a pattern where each 3×3 block has one point, giving density 1/9. But we can also do better with non-lattice patterns? No, 1/9 is the max density for L∞ ≥ 3 in 2D.

Wait, is it? For L∞ ≥ 3, we need each 3×3 block (in the integer grid) to contain at most one point. The max density is 1/9. But with the parity constraint, it might be different.

Actually, 1/9 is the max density. With 72 valid points in a region of "area" 112 (in (u,v) continuous coordinates), the max is about 112/9 ≈ 12.4, so about 12 points. But this seems too low — we need 20.

Wait, I think I'm confusing myself. Let me recompute. The 72 valid (i,j) points map to 72 (u,v) points. The (u,v) region has area 112. With density 1/9, max points ≈ 112/9 ≈ 12.4. But we need 20 crosses, which means 20 centers. 20 > 12.4, so this suggests 20 is impossible?

But wait, the density 1/9 is for continuous space. In discrete space with the parity constraint, things might differ. Also, the 1/9 bound assumes we're tiling with 3×3 blocks, but the region is a parallelogram, and boundary effects can be significant.

Hmm, but actually, I realize the 1/9 density bound might not be tight for this specific region. Let me reconsider.

Actually, let me reconsider whether 1/9 is the right density. For L∞ distance ≥ 3, we need every pair of points to have |Δu| ≥ 3 or |Δv| ≥ 3. Consider the points in a column (fixed u). They must all have |Δv| ≥ 3 (since |Δu| = 0 < 3). So in each column, points are spaced ≥ 3 in v. Similarly, in each row (fixed v), points are spaced ≥ 3 in u.

But points in different columns can be close in v as long as they're ≥ 3 apart in u. So the density can be higher than 1/9? No, I think 1/9 is correct. Consider tiling the plane with 3×3 blocks. Each block can contain at most one point (since any two points in a 3×3 block have L∞ distance ≤ 2). So the density is at most 1/9.

But in our case, the "grid" only has same-parity (u,v) pairs. So each 3×3 block contains at most... let me think. A 3×3 block in (u,v) has 9 cells, but only about 5 have the right parity (either 4 or 5 depending on alignment). And at most 1 of those can be chosen. So the density among valid cells is at most 1/5 ≈ 0.2, giving max ≈ 72 × 0.2 ≈ 14.4, so about 14.

Hmm, but I already found 9 with a lattice. Let me try to find more.

Actually, I realize I should think about this problem differently. Let me go back to the (i,j) coordinates and think about it directly.

The constraint is: centers at mutual Manhattan distance ≥ 3. Let me try to find a good packing.

Let me try a "brick" pattern. In row i, place centers at columns j where j ≡ f(i) mod 3, for some function f.

If f(i) = i mod 3, then centers at (i, j) where j ≡ i mod 3. Two centers (i, j) and (i', j') with j ≡ i mod 3 and j' ≡ i' mod 3. Manhattan distance = |i-i'| + |j-j'|. We need this ≥ 3.

If i = i' (same row): |j - j'| ≥ 3 (since j ≡ j' mod 3 and j ≠ j', so |j-j'| ≥ 3). ✓
If |i - i'| = 1: j - j' ≡ i - i' ≡ ±1 mod 3, so |j - j'| ≥ 1 (could be 1, 2, 4, 5, ...). Manhattan = 1 + |j-j'|. If |j-j'| = 1, Manhattan = 2 < 3. ✗!

So this doesn't work for adjacent rows. Let me try f(i) = 2i mod 3.

j ≡ 2i mod 3. If |i-i'| = 1: j - j' ≡ 2(i-i') ≡ ±2 mod 3. So |j-j'| ≡ 2 mod 3, meaning |j-j'| ∈ {2, 5, 8, ...}. Minimum |j-j'| = 2. Manhattan = 1 + 2 = 3. ✓!

If |i-i'| = 2: j - j' ≡ 2·2 = 4 ≡ 1 mod 3. |j-j'| ∈ {1, 4, 7, ...}. Minimum 1. Manhattan = 2 + 1 = 3. ✓!

If |i-i'| ≥ 3: Manhattan ≥ 3. ✓.

So the pattern j ≡ 2i mod 3 works! All pairwise Manhattan distances are ≥ 3.

Now let me count how many such points fit in {2..9} × {2..10}.

For each row i from 2 to 9, j ≡ 2i mod 3, and j ∈ {2..10}.

i=2: 2i=4, 4 mod 3 = 1. j ≡ 1 mod 3. j ∈ {4, 7, 10}. 3 values.
i=3: 2i=6, 6 mod 3 = 0. j ≡ 0 mod 3. j ∈ {3, 6, 9}. 3 values.
i=4: 2i=8, 8 mod 3 = 2. j ≡ 2 mod 3. j ∈ {2, 5, 8}. 3 values.
i=5: 2i=10, 10 mod 3 = 1. j ≡ 1 mod 3. j ∈ {4, 7, 10}. 3 values.
i=6: 2i=12, 12 mod 3 = 0. j ≡ 0 mod 3. j ∈ {3, 6, 9}. 3 values.
i=7: 2i=14, 14 mod 3 = 2. j ≡ 2 mod 3. j ∈ {2, 5, 8}. 3 values.
i=8: 2i=16, 16 mod 3 = 1. j ≡ 1 mod 3. j ∈ {4, 7, 10}. 3 values.
i=9: 2i=18, 18 mod 3 = 0. j ≡ 0 mod 3. j ∈ {3, 6, 9}. 3 values.

Total: 8 × 3 = 24 points! But wait, we need to check that all these are valid centers, i.e., 2 ≤ i ≤ 9 and 2 ≤ j ≤ 10. Let me verify: all i are in {2..9} ✓, all j are in {2..10} ✓.

But 24 crosses would cover 24 × 5 = 120 cells, but the board only has 110 cells! That's impossible. So there must be overlaps.

Wait, I proved that all pairwise Manhattan distances are ≥ 3, which means no two crosses share a cell. But 24 × 5 = 120 > 110. Contradiction!

Let me recheck. Oh, I think the issue is that some crosses extend outside the board. A cross at (2, 4) covers (1,4), (3,4), (2,3), (2,4), (2,5). All on the board. A cross at (2, 10) covers (1,10), (3,10), (2,9), (2,10), (2,11). (2,11) is on the board (11 columns). ✓. A cross at (9, 3) covers (8,3), (10,3), (9,2), (9,3), (9,4). All on board. ✓.

So all 24 crosses are valid and non-overlapping, covering 120 cells. But the board has 110 cells. This is a contradiction, which means I made an error somewhere.

Let me recheck the Manhattan distance calculation. Take (2, 4) and (3, 3): |2-3| + |4-3| = 1 + 1 = 2 < 3. These overlap!

But according to my calculation: i=2, j=4: j ≡ 2·2 = 4 ≡ 1 mod 3. ✓. i=3, j=3: j ≡ 2·3 = 6 ≡ 0 mod 3. ✓. And |i-i'| = 1, j-j' = 4-3 = 1. But I said |j-j'| ≡ 2 mod 3. Let me recheck: j - j' = 4 - 3 = 1. 1 mod 3 = 1, not 2. 

Where did I go wrong? j ≡ 2i mod 3 and j' ≡ 2i' mod 3. j - j' ≡ 2(i - i') mod 3. If i - i' = 1, then j - j' ≡ 2 mod 3. But j - j' = 1, and 1 ≡ 1 mod 3, not 2. So the congruence doesn't hold?

Wait: j = 4, i = 2. 2i = 4. 4 mod 3 = 1. j = 4, 4 mod 3 = 1. ✓.
j' = 3, i' = 3. 2i' = 6. 6 mod 3 = 0. j' = 3, 3 mod 3 = 0. ✓.
j - j' = 1. 2(i - i') = 2·1 = 2. 2 mod 3 = 2. But j - j' = 1, 1 mod 3 = 1 ≠ 2.

So j - j' ≡ 1 mod 3 but 2(i-i') ≡ 2 mod 3. These should be equal but they're not! The issue is that j ≡ 2i mod 3 means j = 2i + 3k for some integer k, and j' = 2i' + 3k'. So j - j' = 2(i - i') + 3(k - k'). So j - j' ≡ 2(i - i') mod 3. With i - i' = 1: j - j' ≡ 2 mod 3. But j - j' = 1 ≡ 1 mod 3. Contradiction!

So either j ≡ 2i mod 3 is wrong for one of these, or my arithmetic is wrong.

j = 4, i = 2: 2·2 = 4. 4 mod 3 = 1. j mod 3 = 4 mod 3 = 1. ✓.
j' = 3, i' = 3: 2·3 = 6. 6 mod 3 = 0. j' mod 3 = 3 mod 3 = 0. ✓.

j - j' = 1. 2(i - i') = 2(2-3) = -2. -2 mod 3 = 1. Oh! I made an error: i - i' = 2 - 3 = -1, not 1. So 2(i - i') = -2 ≡ 1 mod 3. And j - j' = 1 ≡ 1 mod 3. ✓! They match.

So |i - i'| = 1, and j - j' ≡ 2·(-1) = -2 ≡ 1 mod 3. So |j - j'| ≡ 1 mod 3, meaning |j - j'| ∈ {1, 4, 7, ...}. Minimum 1. Manhattan = 1 + 1 = 2 < 3. ✗!

So my error was in the sign. When |i - i'| = 1, |j - j'| ≡ 1 mod 3 (not 2), so minimum |j - j'| = 1, giving Manhattan distance 2. This doesn't work!

Let me redo the analysis. j ≡ 2i mod 3. For two points (i,j) and (i',j'):
j - j' ≡ 2(i - i') mod 3.

If |i - i'| = 1: |j - j'| ≡ 2 mod 3. So |j - j'| ∈ {2, 5, 8, ...}. Minimum 2. Manhattan = 1 + 2 = 3. ✓.

Wait, but I just showed a counterexample. Let me recheck.

(2, 4) and (3, 3): i = 2, i' = 3. i - i' = -1. j - j' = 4 - 3 = 1. 2(i - i') = -2. -2 mod 3 = 1. j - j' = 1. 1 mod 3 = 1. ✓ (they match). But |j - j'| = 1, and 1 mod 3 = 1, not 2. 

The issue is: j - j' ≡ 2(i - i') mod 3. i - i' = -1. 2(-1) = -2 ≡ 1 mod 3. So j - j' ≡ 1 mod 3. |j - j'| = 1, and 1 ≡ 1 mod 3. ✓.

But I claimed |j - j'| ≡ 2 mod 3 when |i - i'| = 1. The error is that 2(i - i') mod 3 depends on the sign of i - i'. If i - i' = 1, then 2 mod 3 = 2. If i - i' = -1, then -2 mod 3 = 1. So |j - j'| ≡ 1 or 2 mod 3 depending on direction. Since we take absolute value, |j - j'| could be 1 or 2 (mod 3). So the minimum |j - j'| is 1, not 2.

So the pattern j ≡ 2i mod 3 does NOT guarantee Manhattan distance ≥ 3 for adjacent rows. My earlier analysis was wrong.

Let me try j ≡ ci mod 3 for various c and check when it works.

For |i - i'| = 1, we need |j - j'| ≥ 2. j - j' ≡ c(i - i') mod 3. If c = 1: j - j' ≡ ±1 mod 3, so |j - j'| ∈ {1, 4, 7, ...}. Min 1. ✗.
If c = 2: j - j' ≡ ±2 mod 3, so |j - j'| ∈ {2, 5, 8, ...} when i - i' = 1, or |j - j'| ∈ {1, 4, 7, ...} when i - i' = -1. Wait, 2·1 = 2 mod 3 = 2, and 2·(-1) = -2 mod 3 = 1. So depending on direction, |j - j'| ≡ 1 or 2 mod 3. Min could be 1. ✗.

Hmm, so no linear pattern j ≡ ci mod 3 works for adjacent rows? That's because in mod 3, the only nonzero values are 1 and 2, and c · 1 and c · (-1) = -c give c and -c, which are 1 and 2 or 2 and 1. So one direction always gives |j - j'| ≡ 1 mod 3 (min 1).

So a simple mod-3 pattern can't work. We need a more sophisticated approach.

Let me try a mod-5 pattern or a different approach.

Actually, let me try j ≡ 2i mod 5. For |i - i'| = 1: j - j' ≡ 2(i - i') ≡ ±2 mod 5. |j - j'| ∈ {2, 7, 12, ...}. Min 2. Manhattan = 1 + 2 = 3. ✓.
For |i - i'| = 2: j - j' ≡ ±4 mod 5. |j - j'| ∈ {4, 9, ...} or {1, 6, ...}. Wait, 4 mod 5: |j-j'| ∈ {4, 9, ...}. -4 mod 5 = 1: |j-j'| ∈ {1, 6, ...}. So min |j-j'| = 1. Manhattan = 2 + 1 = 3. ✓ (barely).
For |i - i'| = 3: Manhattan ≥ 3. ✓ (regardless of j).
For |i - i'| = 4: j - j' ≡ ±8 ≡ ±3 mod 5. |j-j'| ∈ {3, 8, ...} or {2, 7, ...}. Min 2. Manhattan = 4 + 2 = 6. ✓.

Wait, for |i - i'| = 2, if i - i' = 2: j - j' ≡ 4 mod 5, |j-j'| ∈ {4, 9, ...}, min 4. Manhattan = 2 + 4 = 6. ✓.
If i - i' = -2: j - j' ≡ -4 ≡ 1 mod 5, |j-j'| ∈ {1, 6, ...}, min 1. Manhattan = 2 + 1 = 3. ✓.

So for |i - i'| = 2, the minimum Manhattan distance is 3 (achieved when j - j' ≡ 1 mod 5). This is exactly 3, so it's OK (≥ 3).

So j ≡ 2i mod 5 works! Let me count the points.

For each row i from 2 to 9, j ≡ 2i mod 5, j ∈ {2..10} (9 values).

i=2: 2i=4, j ≡ 4 mod 5. j ∈ {4, 9}. 2 values.
i=3: 2i=6, 6 mod 5 = 1. j ≡ 1 mod 5. j ∈ {6}. Wait, j ∈ {2..10}, j ≡ 1 mod 5: j ∈ {6}. Just 1? Let me check: 1, 6, 11. In {2..10}: only 6. 1 value.

Hmm, that's not many. Let me check all:

i=2: j ≡ 4 mod 5, j ∈ {2..10}: {4, 9}. 2 values.
i=3: j ≡ 1 mod 5, j ∈ {2..10}: {6}. 1 value.
i=4: j ≡ 3 mod 5, j ∈ {2..10}: {3, 8}. 2 values.
i=5: j ≡ 0 mod 5, j ∈ {2..10}: {5, 10}. 2 values.
i=6: j ≡ 2 mod 5, j ∈ {2..10}: {2, 7}. 2 values.
i=7: j ≡ 4 mod 5, j ∈ {2..10}: {4, 9}. 2 values.
i=8: j ≡ 1 mod 5, j ∈ {2..10}: {6}. 1 value.
i=9: j ≡ 3 mod 5, j ∈ {2..10}: {3, 8}. 2 values.

Total: 2+1+2+2+2+2+1+2 = 14.

So 14 crosses with this pattern. Better than 9, but still not 20.

Can I combine multiple mod-5 patterns? If I use j ≡ 2i mod 5 and j ≡ 2i + r mod 5 for some r, I need cross-pattern distances ≥ 3 too.

Two points, one from pattern r=0 and one from r=s: (i, j) with j ≡ 2i mod 5, and (i', j') with j' ≡ 2i' + s mod 5. j - j' ≡ 2(i - i') - s mod 5.

For |i - i'| = 0 (same row): j - j' ≡ -s mod 5. Need |j - j'| ≥ 3. So |s| ≥ 3 mod 5, i.e., s ∈ {3, 2} (since |3| = 3, |2| = 2 < 3). So s = 3 (or -2). Then |j - j'| ≡ 3 mod 5, min |j - j'| = 3. ✓.

For |i - i'| = 1: j - j' ≡ ±2 - s mod 5. Need |j - j'| ≥ 2 (since Manhattan = 1 + |j-j'| ≥ 3). 
If s = 3: j - j' ≡ 2 - 3 = -1 ≡ 4 mod 5, or -2 - 3 = -5 ≡ 0 mod 5. |j - j'| ≡ 4 or 0 mod 5. Min |j-j'| for ≡4: 4. For ≡0: 5 (since j ≠ j' if same row, but different rows could have j = j'). Wait, if j = j', then |j-j'| = 0, Manhattan = 1 + 0 = 1 < 3. ✗!

So when i - i' = -1 (i.e., i' = i + 1), j - j' ≡ -2 - 3 = -5 ≡ 0 mod 5. So j = j' is possible (j - j' = 0 ≡ 0 mod 5). Manhattan = 1 + 0 = 1. ✗.

So s = 3 doesn't work for adjacent rows. Let me try other values of s.

For s = 1: same row, |j - j'| ≡ 1 mod 5, min 1 < 3. ✗.
For s = 2: same row, |j - j'| ≡ 2 mod 5, min 2 < 3. ✗.
For s = 3: same row OK (min 3), but adjacent rows fail (as shown).
For s = 4: same as s = -4 ≡ 1. ✗.

So no two mod-5 patterns can be combined. The maximum with a single mod-5 pattern is 14.

Hmm. Let me think about this differently. Maybe I should not use a lattice pattern at all.

Let me reconsider the problem. We need to place points in {2..9} × {2..10} with pairwise Manhattan distance ≥ 3. The maximum number of such points is what we need, and then we need to check it's ≤ 20 (from the upper bound) and construct 20.

Wait, actually, I realize the upper bound of 20 came from the mod-5 coloring argument. But I should double-check that argument.

The mod-5 coloring: color (i,j) by (i + 2j) mod 5. Each cross covers one cell of each color. The board has 22 cells of each color. With k crosses, we cover k cells of each color, leaving 22 - k of each color uncovered. The 4 corners are always uncovered and have colors 3, 3, 2, 2. For k = 21: 1 of each color uncovered, but corners give 2 of color 2 and 2 of color 3. Contradiction. For k = 20: 2 of each color uncovered, corners give 2 of color 2 and 2 of color 3, leaving 2 more each of colors 0, 1, 4. Total uncovered = 4 + 6 = 10 = 110 - 100. ✓.

So the upper bound is 20. Now I need to construct 20 non-overlapping crosses.

Let me try a different approach to construction. Let me try to use a mix of patterns.

Actually, let me try to think about this more carefully using the (u,v) transformation.

In (u,v) = (i+j, i-j) coordinates, we need L∞ distance ≥ 3. The valid region is the parallelogram with vertices (4,0), (12,-8), (19,-1), (11,7), and only same-parity (u,v) pairs are valid.

The L∞ ≥ 3 constraint means we can place at most one point per 3×3 block. Let me think about how many 3×3 blocks fit in the parallelogram.

The u range is 4 to 19 (16 values), v range is -8 to 7 (16 values). With 3×3 blocks, we can fit ceil(16/3) = 6 blocks in each direction, giving 36 blocks. But many of these blocks are outside the parallelogram.

This is getting complicated. Let me try a direct construction.

Let me try to place crosses row by row, maximizing the count.

Row 2 (i=2): Place crosses at j = 2, 5, 8. These are at distance 3 apart. 3 crosses. These cover cells in rows 1, 2, 3.
Row 3 (i=3): Crosses here would overlap with row 2 crosses (distance 1 in rows). Need |j - j'| ≥ 2 for all j' in {2, 5, 8}. j ∉ {0,1,2,3,4, 3,4,5,6, 6,7,8,9} = {0..9}. j ∈ {10}. 1 cross at (3, 10).

But wait, (3, 10) vs (2, 8): |3-2| + |10-8| = 1 + 2 = 3. ✓. (3, 10) vs (2, 5): 1 + 5 = 6. ✓. (3, 10) vs (2, 2): 1 + 8 = 9. ✓.

Row 4 (i=4): Need distance ≥ 3 from row 2 ({2,5,8}) and row 3 ({10}).
vs row 2 (|i-i'|=2): need |j - j'| ≥ 1. j ∉ {2, 5, 8} (exactly). So j ∈ {3, 4, 6, 7, 9, 10}.
vs row 3 (|i-i'|=1): need |j - 10| ≥ 2. j ∉ {8, 9, 10, 11, 12} ∩ {2..10} = {8, 9, 10}. So j ∈ {2..7}.
Combining: j ∈ {3, 4, 6, 7} (from row 2 constraint) ∩ {2..7} (from row 3 constraint) = {3, 4, 6, 7}.
Within row 4, need pairwise distance ≥ 3. From {3, 4, 6, 7}: {3, 6} or {3, 7} or {4, 7}. Max 2 crosses. Let's pick {3, 7}: distance 4. ✓. Or {3, 6}: distance 3. ✓.

Let me pick row 4: j = 3, 7. But wait, (4, 3) vs (2, 2): |4-2| + |3-2| = 2 + 1 = 3. ✓. (4, 3) vs (2, 5): 2 + 2 = 4. ✓. (4, 7) vs (2, 8): 2 + 1 = 3. ✓. (4, 7) vs (2, 5): 2 + 2 = 4. ✓. (4, 3) vs (3, 10): 1 + 7 = 8. ✓. (4, 7) vs (3, 10): 1 + 3 = 4. ✓. Good.

Row 5 (i=5): vs row 4 ({3,7}, |i-i'|=1): |j-3| ≥ 2 and |j-7| ≥ 2. j ∉ {1..5, 5..9} = {1..9}. j ∈ {10}. 
vs row 3 ({10}, |i-i'|=2): |j-10| ≥ 1. j ≠ 10. But j ∈ {10} from above and j ≠ 10. Contradiction. So 0 crosses in row 5.

Row 6 (i=6): vs row 4 ({3,7}, |i-i'|=2): |j-3| ≥ 1 and |j-7| ≥ 1. j ∉ {3, 7}. j ∈ {2,4,5,6,8,9,10}.
vs row 5: no crosses. 
Within row 6: pairwise ≥ 3. From {2,4,5,6,8,9,10}: best is {2, 5, 8} or {2, 5, 10} or {2, 6, 10} or {4, 8} etc. {2, 5, 8}: distances 3, 3, 6. ✓. 3 crosses.
Check vs row 4: (6, 2) vs (4, 3): 2+1=3 ✓. (6, 5) vs (4, 3): 2+2=4 ✓. (6, 5) vs (4, 7): 2+2=4 ✓. (6, 8) vs (4, 7): 2+1=3 ✓. All good. 3 crosses.

Row 7 (i=7): vs row 6 ({2,5,8}, |i-i'|=1): |j-2|≥2, |j-5|≥2, |j-8|≥2. j ∉ {0..4, 3..7, 6..10} = {0..10}. j ∈ {} (within 2..10). 0 crosses.

Hmm, that's 0. Let me reconsider. Maybe I should choose row 6 differently to leave room for row 7.

Let me try row 6: {2, 6, 10} instead. vs row 4 ({3,7}): (6,2) vs (4,3): 2+1=3 ✓. (6,6) vs (4,7): 2+1=3 ✓. (6,10) vs (4,7): 2+3=5 ✓. (6,6) vs (4,3): 2+3=5 ✓. (6,10) vs (4,3): 2+7=9 ✓. (6,2) vs (4,7): 2+5=7 ✓. All good. 3 crosses.

Row 7: vs row 6 ({2,6,10}, |i-i'|=1): |j-2|≥2, |j-6|≥2, |j-10|≥2. j ∉ {0..4, 4..8, 8..12} = {0..12}. j ∈ {} (within 2..10). 0 crosses.

Still 0. The problem is that 3 crosses in a row spaced 3 apart block the adjacent rows completely.

Let me try 2 crosses in row 6 instead. Row 6: {3, 8}. vs row 4 ({3,7}): (6,3) vs (4,3): 2+0=2 < 3. ✗!

Row 6: {4, 8}. vs row 4 ({3,7}): (6,4) vs (4,3): 2+1=3 ✓. (6,4) vs (4,7): 2+3=5 ✓. (6,8) vs (4,7): 2+1=3 ✓. (6,8) vs (4,3): 2+5=7 ✓. Good. 2 crosses.

Row 7: vs row 6 ({4,8}, |i-i'|=1): |j-4|≥2, |j-8|≥2. j ∉ {2..6, 6..10} = {2..10}. j ∈ {}. 0 crosses.

Still 0. 2 crosses spaced 4 apart also block adjacent rows (since the gap is 4, and we need ≥ 2 from each, leaving no room).

What about 2 crosses spaced 5 apart? Row 6: {2, 7}. vs row 4 ({3,7}): (6,7) vs (4,7): 2+0=2. ✗.

Row 6: {2, 8}. vs row 4 ({3,7}): (6,2) vs (4,3): 2+1=3 ✓. (6,8) vs (4,7): 2+1=3 ✓. (6,2) vs (4,7): 2+5=7 ✓. (6,8) vs (4,3): 2+5=7 ✓. Good. 2 crosses.

Row 7: vs row 6 ({2,8}, |i-i'|=1): |j-2|≥2, |j-8|≥2. j ∉ {0..4, 6..10} = {0..10}. j ∈ {}. 0 crosses.

Hmm, still 0. The problem is that with 2 crosses at distance 6, the "exclusion zones" (±2 in column) cover {0..4} and {6..10}, which is everything.

What if the 2 crosses are closer? Row 6: {4, 7}. Distance 3. vs row 4 ({3,7}): (6,7) vs (4,7): 2+0=2. ✗.

Row 6: {5, 8}. vs row 4 ({3,7}): (6,5) vs (4,3): 2+2=4 ✓. (6,5) vs (4,7): 2+2=4 ✓. (6,8) vs (4,7): 2+1=3 ✓. (6,8) vs (4,3): 2+5=7 ✓. Good. 2 crosses.

Row 7: vs row 6 ({5,8}, |i-i'|=1): |j-5|≥2, |j-8|≥2. j ∉ {3..7, 6..10} = {3..10}. j ∈ {2}. 1 cross at (7, 2).

Check (7, 2) vs (4, 3): 3+1=4 ✓. (7, 2) vs (4, 7): 3+5=8 ✓. (7, 2) vs (5, ...) — no crosses in row 5. (7, 2) vs (6, 5): 1+3=4 ✓. (7, 2) vs (6, 8): 1+6=7 ✓. Good.

Row 8: vs row 7 ({2}, |i-i'|=1): |j-2|≥2. j ∉ {0..4}. j ∈ {5..10}.
vs row 6 ({5,8}, |i-i'|=2): |j-5|≥1, |j-8|≥1. j ∉ {5, 8}. j ∈ {6, 7, 9, 10}.
Combining: j ∈ {5..10} ∩ {6,7,9,10} = {6, 7, 9, 10}.
Within row 8: pairwise ≥ 3. From {6, 7, 9, 10}: {6, 9} or {6, 10} or {7, 10}. Max 2. Pick {6, 10}: distance 4. ✓.

Check (8, 6) vs (7, 2): 1+4=5 ✓. (8, 10) vs (7, 2): 1+8=9 ✓. (8, 6) vs (6, 5): 2+1=3 ✓. (8, 6) vs (6, 8): 2+2=4 ✓. (8, 10) vs (6, 8): 2+2=4 ✓. (8, 10) vs (6, 5): 2+5=7 ✓. Good. 2 crosses.

Row 9: vs row 8 ({6,10}, |i-i'|=1): |j-6|≥2, |j-10|≥2. j ∉ {4..8, 8..12} = {4..12}. j ∈ {2, 3}.
vs row 7 ({2}, |i-i'|=2): |j-2|≥1. j ≠ 2. j ∈ {3}.
1 cross at (9, 3).

Check (9, 3) vs (8, 6): 1+3=4 ✓. (9, 3) vs (8, 10): 1+7=8 ✓. (9, 3) vs (7, 2): 2+1=3 ✓. (9, 3) vs (6, 5): 3+2=5 ✓. (9, 3) vs (6, 8): 3+5=8 ✓. Good.

Now let me also check row 2 vs row 4, and row 3 vs row 5 (which had 0 crosses).

Let me also check if I can add crosses in row 5. Row 5: vs row 4 ({3,7}, |i-i'|=1): |j-3|≥2, |j-7|≥2. j ∉ {1..5, 5..9} = {1..9}. j ∈ {10}. vs row 3 ({10}, |i-i'|=2): |j-10|≥1. j ≠ 10. Contradiction. 0 crosses. ✓ (as before).

vs row 6 ({5,8}, |i-i'|=1): |j-5|≥2, |j-8|≥2. j ∉ {3..7, 6..10} = {3..10}. j ∈ {2}. But also need vs row 4 and row 3 constraints. j=10 from row 4 constraint, j=2 from row 6 constraint. Contradiction. 0.

OK so let me tally up:
Row 2: 3 (j = 2, 5, 8)
Row 3: 1 (j = 10)
Row 4: 2 (j = 3, 7)
Row 5: 0
Row 6: 2 (j = 5, 8)
Row 7: 1 (j = 2)
Row 8: 2 (j = 6, 10)
Row 9: 1 (j = 3)

Total: 3 + 1 + 2 + 0 + 2 + 1 + 2 + 1 = 12. Not great.

Let me try a completely different approach. Let me try to be more systematic.

Actually, let me try the pattern where we use 2 crosses per row for all 8 rows.

Row 2: {2, 6}
Row 3: {4, 8}
Row 4: {2, 6} — but (4, 2) vs (2, 2): 2+0=2 < 3. ✗.

So I can't repeat the same columns in rows 2 apart. Let me use a 3-row cycle:

Row 2: {2, 6}
Row 3: {4, 8}
Row 4: {6, 10} — vs row 2 ({2,6}): (4,6) vs (2,6): 2+0=2. ✗.

Hmm. Let me try:
Row 2: {2, 7}
Row 3: {4, 9}
Row 4: {6} — vs row 2 ({2,7}): (4,6) vs (2,7): 2+1=3 ✓, (4,6) vs (2,2): 2+4=6 ✓. vs row 3 ({4,9}): (4,6) vs (3,4): 1+2=3 ✓, (4,6) vs (3,9): 1+3=4 ✓. Can I add more? {6, 10}: (4,10) vs (3,9): 1+1=2. ✗. {6}: just 1. Or {6, 11}? 11 > 10. No.

Actually wait, can I do {6, 10}? (4,10) vs (2,7): 2+3=5 ✓. (4,10) vs (2,2): 2+8=10 ✓. (4,10) vs (3,9): 1+1=2. ✗. So no.

What about row 4: {6}? Or {5, 10}? (4,5) vs (3,4): 1+1=2. ✗. {7}? (4,7) vs (3,9): 1+2=3 ✓. (4,7) vs (3,4): 1+3=4 ✓. (4,7) vs (2,7): 2+0=2. ✗.

{8}? (4,8) vs (3,9): 1+1=2. ✗. {6, 10} doesn't work. {6} only.

Hmm, this is getting tedious. Let me try a different strategy.

Let me try to think about what the theoretical maximum is for the independent set (Manhattan distance ≥ 3) in the 8×9 grid, and whether 20 is achievable.

Actually, let me reconsider. The upper bound of 20 came from the coloring argument. But maybe the actual maximum of the independent set is less than 20, and the answer is less than 20. But the problem asks for the maximum number of non-overlapping crosses, which equals the maximum independent set (since non-overlapping = Manhattan distance ≥ 3 between centers, and all centers must be valid).

Wait, actually, I need to be more careful. Non-overlapping crosses means the 5-cell sets don't intersect. Two crosses at Manhattan distance exactly 2 share a cell. At distance 1, they share cells. At distance 0, same cross. At distance ≥ 3, no shared cells. So non-overlapping ⟺ Manhattan distance ≥ 3. ✓.

So the answer is the maximum independent set in the graph on {2..9}×{2..10} where edges connect points at Manhattan distance ≤ 2.

Let me try to compute this more carefully. Let me try a different construction.

Let me try a "staircase" pattern. Place crosses at:
(2,2), (2,5), (2,8) — row 2, 3 crosses
(4,3), (4,6), (4,9) — row 4, 3 crosses (check vs row 2: (4,3) vs (2,2): 2+1=3 ✓, (4,3) vs (2,5): 2+2=4 ✓, (4,6) vs (2,5): 2+1=3 ✓, (4,6) vs (2,8): 2+2=4 ✓, (4,9) vs (2,8): 2+1=3 ✓. All good.)
(6,2), (6,5), (6,8) — row 6, 3 crosses (check vs row 4: (6,2) vs (4,3): 2+1=3 ✓, (6,5) vs (4,3): 2+2=4 ✓, (6,5) vs (4,6): 2+1=3 ✓, (6,8) vs (4,6): 2+2=4 ✓, (6,8) vs (4,9): 2+1=3 ✓. All good.)
(8,3), (8,6), (8,9) — row 8, 3 crosses (check vs row 6: (8,3) vs (6,2): 2+1=3 ✓, (8,3) vs (6,5): 2+2=4 ✓, (8,6) vs (6,5): 2+1=3 ✓, (8,6) vs (6,8): 2+2=4 ✓, (8,9) vs (6,8): 2+1=3 ✓. All good.)

Total: 12 crosses. Same as before. Can I add more in the odd rows?

Row 3: vs row 2 ({2,5,8}, |i-i'|=1): |j-2|≥2, |j-5|≥2, |j-8|≥2. j ∉ {0..4, 3..7, 6..10} = {0..10}. j ∈ {}. 0 crosses.
Row 5: vs row 4 ({3,6,9}, |i-i'|=1): |j-3|≥2, |j-6|≥2, |j-9|≥2. j ∉ {1..5, 4..8, 7..11} = {1..11}. j ∈ {}. 0 crosses.
Row 7: vs row 6 ({2,5,8}, |i-i'|=1): same as row 3. 0 crosses.
Row 9: vs row 8 ({3,6,9}, |i-i'|=1): same as row 5. 0 crosses.

So 12 is all we get with this pattern. The 3-per-even-row pattern blocks all odd rows.

Let me try 2 per row with a clever pattern that allows all 8 rows.

The key constraint: for rows differing by 1, columns must differ by ≥ 2. For rows differing by 2, columns must differ by ≥ 1.

Let me use a 4-row repeating pattern: A, B, C, D where:
- A and C differ by ≥ 1 in each column (rows 2 apart)
- B and D differ by ≥ 1 in each column (rows 2 apart)  
- A and B differ by ≥ 2 in each column (adjacent)
- B and C differ by ≥ 2 in each column (adjacent)
- C and D differ by ≥ 2 in each column (adjacent)
- A and D: rows differ by 3, no constraint.

Let me try:
A (row 2): {2, 7}
B (row 3): {4, 9} — vs A: |2-4|=2 ✓, |2-9|=7 ✓, |7-4|=3 ✓, |7-9|=2 ✓. All ≥ 2. ✓.
C (row 4): {6} — vs B: |6-4|=2 ✓, |6-9|=3 ✓. vs A: |        — AI历史解题过程（thinking）
#   polymath_01628         — 题目ID

# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search.
- All information you need is in this AGENTS.md file.
- Output your analysis directly in your response (in this TUI).
- End your analysis with a line containing exactly: `### ANALYSIS COMPLETE`

## Analysis Task

You are given three inputs:
1. **Problem** — a math competition problem
2. **Standard Solution** — the correct solution from the problem bank
3. **AI's Thinking** — an AI's attempted solution process (its reasoning when it tried to solve the problem, but failed)

Your task: analyze WHY the AI failed, by comparing its thinking with the standard solution.

### Dimension 1: Failure Type

Compare the standard solution's key approach with the AI's thinking:

- **DIRECTION_ERROR**: The AI's thinking went in a fundamentally wrong direction. The standard solution uses a specific mathematical approach that the AI never considered. The AI was exploring a completely different strategy. The failure is about *which direction to explore*, not about running out of time.

- **TOKEN_LIMIT**: The AI's thinking was going in the RIGHT direction — it was using the same key approach as the standard solution (or a valid alternative) — but ran out of tokens before completing the proof. The failure is about *not enough time*, not about *wrong direction*.

- **CONNECTION_ERROR**: The AI didn't really attempt the problem. The thinking is very short, contains connection errors, or has no meaningful mathematical content. This is a technical failure, not a mathematical one.

- **PARTIAL_PROGRESS**: The AI's thinking was partially in the right direction — it identified some key ideas from the standard solution — but missed the crucial turning point. The AI was on the right track but took a wrong turn at a critical juncture.

### Dimension 2: Key Turning Point Type

If the verdict is DIRECTION_ERROR or PARTIAL_PROGRESS, identify what type of key turning point the standard solution uses:

1. **mod_p_grouping**: The standard solution uses modular arithmetic (mod p, where p is small/obvious like 4, 8) to group/categorize objects and find a contradiction or hidden structure.

2. **mod_p_non_obvious**: The standard solution uses modular arithmetic where the prime p is NOT obvious from the problem statement (e.g., mod 11, mod p where p needs to be discovered through analysis).

3. **quadratic_residue_euler**: The standard solution uses quadratic residues, Legendre symbols, or Euler's criterion.

4. **lte_lemma**: The standard solution uses the Lifting The Exponent (LTE) lemma.

5. **p_adic_valuation**: The standard solution uses p-adic valuation (v_p) analysis.

6. **multi_step_mod_p**: The standard solution uses multiple steps of modular arithmetic analysis (not just one mod operation).

7. **crt**: The standard solution uses the Chinese Remainder Theorem (combining information from multiple moduli).

8. **permutation_polynomial**: The standard solution uses properties of permutation polynomials over finite fields.

9. **finite_field_structure**: The standard solution exploits the structure of finite fields (Z/pZ, F_p, F_p^k).

10. **other**: None of the above categories fit. Describe the technique in dimension2_explanation.

### Output Format

Output your analysis in this EXACT XML format. The XML must be well-formed and parseable.

```xml
<analysis>
  <problem_id>polymath_01628</problem_id>
  <dimension1_verdict>DIRECTION_ERROR|TOKEN_LIMIT|CONNECTION_ERROR|PARTIAL_PROGRESS</dimension1_verdict>
  <dimension1_explanation>1-3 sentences explaining the verdict</dimension1_explanation>
  <dimension2_turning_point_type>mod_p_grouping|mod_p_non_obvious|quadratic_residue_euler|lte_lemma|p_adic_valuation|multi_step_mod_p|crt|permutation_polynomial|finite_field_structure|other</dimension2_turning_point_type>
  <dimension2_explanation>1-3 sentences describing the key turning point in the standard solution</dimension2_explanation>
  <ai_direction_summary>1 sentence describing what direction the AI's thinking went</ai_direction_summary>
  <standard_solution_key_technique>1 sentence describing the key technique in the standard solution</standard_solution_key_technique>
  <confidence>high|medium|low</confidence>
</analysis>
```

After the XML block, output exactly: `### ANALYSIS COMPLETE`

**Rules:**
- The XML must be inside a ```xml code block
- Do NOT add any text before or after the XML block (except ### ANALYSIS COMPLETE)
- If the AI's thinking is too short to analyze (< 500 chars of mathematical content), output CONNECTION_ERROR
- If you cannot determine the turning point type, use "other" and explain in dimension2_explanation

## Problem

24.3.9 * A shape obtained by removing a unit square from each corner of a $3 \times 3$ square is called a “cross-shape”.

On a $10 \times 11$ chessboard, what is the maximum number of non-overlapping “cross-shapes” that can be placed? (Each “cross-shape” exactly covers 5 small squares on the chessboard.)

## Standard Solution

Analysis Answer: 15.

First, prove that the maximum number of "crosses" that can be placed is 15. Use proof by contradiction, assuming that 16 "crosses" can be placed.

For each "cross," we call the central square the "heart" (denoted as *). Remove the outermost layer of squares from the $10 \times 11$ chessboard, resulting in an $8 \times 9$ grid. Clearly, the "heart" of each "cross" can only appear within this $8 \times 9$ grid.
Note that in every $3 \times 3$ grid, at most two "hearts" can be placed:
We will discuss how to place as many "hearts" as possible in an $8 \times 3$ grid. Divide the $8 \times 3$ grid from top to bottom into three sub-grids: $3 \times 3$, $2 \times 3$, and $3 \times 3$. If one "heart" is placed in the middle $2 \times 3$ grid, then since at most two "hearts" can be placed in each $3 \times 3$ grid, a total of 5 "hearts" can be placed. If two "hearts" are placed in the middle $2 \times 3$ grid, then a total of 6 "hearts" can be placed in the $8 \times 3$ grid, at which point the third and sixth rows must be empty. Through exhaustive enumeration, it is known that there are only the two placement methods shown in the following diagram:
Now, divide the $8 \times 9$ grid into three $8 \times 3$ grids, from left to right, called grid (a), grid (b), and grid (c). Since there are 16 "hearts" in the $8 \times 9$ grid, one of the $8 \times 3$ grids must have 6 "hearts".

If grid (b) has 6 "hearts," since there are only two mutually symmetrical ways to place 6 "hearts" in an $8 \times 3$ grid, we can assume the 6 "hearts" are distributed as shown in the left diagram below:

It is easy to see that the 3rd and 7th columns cannot have "hearts." Thus, it is not difficult to see that at most 4 "hearts" can be placed in grids (a) and (c), resulting in a total of $4+6+4=14$ "hearts," leading to a contradiction.

If grids (a) and (c) each have 6 "hearts," then the 4th and 6th columns cannot have "hearts," so only the middle column in grid (b) can have "hearts." It is not difficult to see that at most 3 "hearts" can be placed in grid (b), resulting in a total of $6+3+6=15$ "hearts," also leading to a contradiction.

If 6 "hearts" are placed in either grid (a) or grid (c), assume 6 "hearts" are placed in grid (a), and they are placed as shown in the right diagram above. In this case, the 4th column cannot have "hearts," so at most 4 "hearts" can be placed in grid (b), resulting in a total of $6+4+5=15$ "hearts," also leading to a contradiction.
In summary, it is known that at most 15 "hearts" can be placed in the $8 \times 9$ grid.
Finally, in addition to the two examples already provided, we give two more examples to show that indeed 15 "hearts" can be placed:

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. A cross-shape is a 3x3 square with unit squares removed from each corner, leaving 5 squares (the center plus the 4 edge-midpoints). On a 10x11 board, find the maximum number of non-overlapping cross-shapes.

Let me think about this carefully.

A cross-shape covers 5 cells: the center of a 3x3 block, plus the 4 cells adjacent to it (up, down, left, right). So it's a plus/cross shape.

The board is 10x11 = 110 cells. Each cross covers 5 cells, so the upper bound is 110/5 = 22.

But can we achieve 22? That would require tiling the entire board with crosses. Let me think about whether that's possible.

Let me use a coloring argument. Color the board in a checkerboard pattern. A cross-shape centered at a cell covers that cell and its 4 neighbors. If the center is black, the 4 neighbors are white. So each cross covers 1 black + 4 white (if center is black) or 4 black + 1 white (if center is white).

On a 10x11 board, the number of black and white cells: 110 cells, 55 black and 55 white (since 110 is even).

If we have k crosses with black centers and m crosses with white centers, total black covered = k + 4m, total white covered = 4k + m. For a tiling (22 crosses), we need k + 4m = 55 and 4k + m = 55. Adding: 5k + 5m = 110, so k + m = 22. Subtracting: 3m - 3k = 0, so k = m = 11. So we'd need 11 black-centered and 11 white-centered crosses. That's consistent so far.

Let me think about a different coloring. Let me try coloring by columns mod something, or a more refined coloring.

Actually, let me think about this differently. Let me consider the problem more carefully.

Let me try a coloring with 4 colors based on (row mod 2, col mod 2). Actually, let me think about what constraints crosses impose.

A cross centered at (r, c) covers (r,c), (r-1,c), (r+1,c), (r,c-1), (r,c+1).

Let me try coloring by row+col mod 4 or something.

Actually, let me think about a known approach. Let me try to find the answer by construction and upper bound.

Upper bound: 22 (area bound). But is it achievable?

Let me think about whether 22 is achievable. We need to tile 10x11 completely with crosses.

Consider coloring columns with period 4: columns 1,2,3,4,5,6,7,8,9,10,11 (if 11 columns) colored A,B,C,D,A,B,C,D,A,B,C.

Hmm, let me think about a different approach. Let me consider the board coordinates (i,j) with 1≤i≤10, 1≤j≤11.

Let me try a coloring where I color cell (i,j) based on (i + 2j) mod 5 or something to get a bound.

Actually, let me think about this more carefully. Let me try to find a construction for 22 first, and if it fails, find the right upper bound.

For a tiling, consider the cross centered at (i,j). It covers cells with these (row, col) values. The sum of (i+j) mod 2 for the 5 cells: center has parity p, the 4 neighbors have parity 1-p. So 1 cell with parity p and 4 with parity 1-p.

Let me try a coloring mod 5. Color cell (i,j) with color (i + 2j) mod 5. For a cross centered at (i,j):
- Center: (i + 2j) mod 5
- Up (i-1,j): (i-1+2j) mod 5 = center - 1
- Down (i+1,j): center + 1
- Left (i,j-1): center - 2
- Right (i,j+1): center + 2

So the cross covers colors {c-1, c, c+1, c-2, c+2} mod 5 = all 5 colors! Each cross covers exactly one cell of each color mod 5.

So if we color by (i + 2j) mod 5, each cross covers exactly one of each color. For a complete tiling, we need each color to appear exactly 22 times on the board.

Let me count. The board is 10 rows × 11 columns. Color of (i,j) = (i + 2j) mod 5, where i from 1..10, j from 1..11.

For a fixed i, as j goes 1..11, 2j mod 5 cycles through: 2,4,1,3,0,2,4,1,3,0,2 (period 5). So in 11 columns, the values 2j mod 5 are: {2,4,1,3,0} each appearing twice, plus one extra 2 (the 11th). So counts: 0→2, 1→2, 2→3, 3→2, 4→2.

Then (i + 2j) mod 5 = (i mod 5 + 2j mod 5) mod 5. For fixed i, this shifts the distribution. Over all 10 rows, i mod 5 takes values 1,2,3,4,0,1,2,3,4,0 — each value appears twice.

For each row i, the color distribution is a cyclic shift of {0:2, 1:2, 2:3, 3:2, 4:2} by i mod 5.

Total count for color c = sum over i of (count of c in row i).

For rows with i mod 5 = 0: distribution {0:2,1:2,2:3,3:2,4:2}, shifted by 0 → same.
For rows with i mod 5 = 1: shifted by 1 → {1:2,2:2,3:3,4:2,0:2}.
For rows with i mod 5 = 2: shifted by 2 → {2:2,3:2,4:3,0:2,1:2}.
For rows with i mod 5 = 3: shifted by 3 → {3:2,4:2,0:3,1:2,2:2}.
For rows with i mod 5 = 4: shifted by 4 → {4:2,0:2,1:3,2:2,3:2}.

Each i mod 5 value appears in 2 rows. So total for color c:
- Color 0: 2×2 (from i≡0) + 2×2 (from i≡1, where 0 gets 2) + 2×2 (from i≡2, where 0 gets 2) + 2×3 (from i≡3, where 0 gets 3) + 2×2 (from i≡4, where 0 gets 2) = 4+4+4+6+4 = 22.
- Color 1: 2×2 + 2×2 + 2×2 + 2×2 + 2×3 = 4+4+4+4+6 = 22.
- Color 2: 2×3 + 2×2 + 2×2 + 2×2 + 2×2 = 6+4+4+4+4 = 22.
- Color 3: 2×2 + 2×3 + 2×2 + 2×2 + 2×2 = 4+6+4+4+4 = 22.
- Color 4: 2×2 + 2×2 + 2×3 + 2×2 + 2×2 = 4+4+6+4+4 = 22.

Each color appears exactly 22 times. So the mod-5 coloring doesn't rule out a tiling. Good, so 22 is not ruled out by this coloring.

Hmm, so maybe 22 is achievable? Let me think harder.

Actually wait, let me reconsider. The fact that each color appears 22 times and each cross covers one of each color means that IF a tiling exists, it's consistent. But it doesn't prove a tiling exists. Let me try to construct one.

Actually, let me reconsider the problem. 10×11 = 110, and 110/5 = 22. Let me try to actually construct a tiling.

A cross centered at (i,j) requires 2≤i≤9 and 2≤j≤10 (so that all 5 cells are on the board). Wait, the board is 10 rows × 11 columns. So valid centers are i from 2..9 and j from 2..10. That's 8 × 9 = 72 possible centers, and we need to choose 22 non-overlapping ones.

Let me try to think about tiling. Let me try a pattern.

Consider placing crosses in a regular grid. If I place crosses at centers (i,j) where i ≡ 2 mod 3 and j ≡ 2 mod 3... no, crosses overlap that way.

Let me think differently. Two crosses overlap if they share a cell. Cross at (i,j) and cross at (i',j') share a cell iff the Manhattan distance between centers is ≤ 2 and they're not the same. Actually more precisely, they overlap iff |i-i'| + |j-j'| ≤ 2 and (i,j) ≠ (i',j'), OR one center is a neighbor of the other's center... Let me think.

Cross at (i,j) covers {(i,j),(i±1,j),(i,j±1)}. Cross at (i',j') covers {(i',j'),(i'±1,j'),(i',j'±1)}. They overlap iff some cell is in both sets. The cells of the first cross are at Manhattan distance ≤1 from (i,j). The cells of the second are at Manhattan distance ≤1 from (i',j'). They share a cell iff there's a cell at distance ≤1 from both centers, i.e., the Manhattan distance between (i,j) and (i',j') is ≤ 2.

So two crosses are non-overlapping iff their centers are at Manhattan distance ≥ 3.

So we need to place 22 points in the grid {2,...,9} × {2,...,10} such that any two are at Manhattan distance ≥ 3, AND the 5-cell crosses centered at these points exactly cover the 10×11 board.

Wait, but actually the centers don't have to be at Manhattan distance ≥ 3 only — they need to be at distance ≥ 3 for non-overlap, but also the crosses must cover the board exactly (for a tiling). For just maximizing the count, we need non-overlap, which means Manhattan distance ≥ 3 between any two centers.

But for a tiling (22 crosses), we need the additional constraint that the crosses cover everything.

Hmm, but the problem asks for the maximum number of non-overlapping crosses, not necessarily a tiling. So the answer could be less than 22 if a tiling isn't possible but we can fit 22 non-overlapping crosses that don't cover everything... wait no, 22 crosses cover 110 cells = the whole board, so 22 non-overlapping crosses would be a tiling.

So the question is: can we place 22 non-overlapping crosses on the 10×11 board? That's equivalent to tiling.

Let me think about whether a tiling exists. Let me try to construct one.

Let me try to think about small cases first. Can we tile a 3×5 rectangle with crosses? 3×5 = 15 = 3 crosses. A cross in a 3×5... center at (2,2) covers (1,2),(2,1),(2,2),(2,3),(3,2). Center at (2,4) covers (1,4),(2,3),(2,4),(2,5),(3,4). These overlap at (2,3)! So we can't place both.

Hmm. Let me think about what rectangles can be tiled.

Actually, let me think about the structure differently. Let me try to tile the 10×11 board.

Let me try a specific construction. Place crosses at centers:
Row 2: (2,2), (2,5), (2,8)
Row 5: (5,3), (5,6), (5,9)  
Row 8: (8,2), (8,5), (8,8)

Wait, let me check distances. (2,2) and (2,5): Manhattan distance 3. Good. (2,2) and (5,3): distance 3+1=4. Good. (2,5) and (5,6): 3+1=4. Good. (5,3) and (5,6): 3. Good. (5,3) and (8,2): 3+1=4. Good.

But this only gives 9 crosses. Let me think about how to get 22.

Actually, let me think about this more systematically. The centers must be at Manhattan distance ≥ 3. In a grid, the maximum number of points at mutual Manhattan distance ≥ 3...

Actually, for a tiling, we need the crosses to cover every cell. Let me think about which cells can be centers and which must be covered.

Every cell must be covered by exactly one cross. A cell (i,j) is covered by a cross centered at (i,j), (i±1,j), or (i,j±1). So every cell must be at Manhattan distance ≤ 1 from some center.

Also, corner cells like (1,1) can only be covered by a cross centered at (1,1) [but that's not a valid center since it's on the edge], (2,1) [not valid], or (1,2) [not valid]. Wait, (1,1) can be covered by a cross centered at (2,1) — but (2,1) is on the edge (column 1), so the cross at (2,1) would need (2,0) which is off the board. So (2,1) is not a valid center.

Hmm wait. Let me reconsider. The center must be such that all 5 cells are on the board. Center at (i,j) needs (i-1,j), (i+1,j), (i,j-1), (i,j+1) all on the board. So 2 ≤ i ≤ 9 and 2 ≤ j ≤ 10 (for a 10×11 board with rows 1-10, cols 1-11).

So cell (1,1) can only be covered by a cross centered at (2,1) or (1,2) — but neither is a valid center! (2,1) has j=1 which is too small, (1,2) has i=1 which is too small.

Wait, that means (1,1) can never be covered by any cross! That means a complete tiling is IMPOSSIBLE.

Let me double-check. The cross centered at (i,j) covers (i,j), (i-1,j), (i+1,j), (i,j-1), (i,j+1). For (1,1) to be covered, we need one of these to equal (1,1):
- (i,j) = (1,1): center at (1,1), but then (0,1) is off-board. Invalid.
- (i-1,j) = (1,1): (i,j) = (2,1), but (2,0) is off-board. Invalid.
- (i+1,j) = (1,1): (i,j) = (0,1). Off-board. Invalid.
- (i,j-1) = (1,1): (i,j) = (1,2), but (0,2) is off-board. Invalid.
- (i,j+1) = (1,1): (i,j) = (1,0). Off-board. Invalid.

So (1,1) cannot be covered by any cross! Similarly, all four corners of the board cannot be covered.

So a tiling is impossible. The maximum is less than 22.

The four corners (1,1), (1,11), (10,1), (10,11) cannot be covered. So at most 110 - 4 = 106 cells can be covered, giving at most floor(106/5) = 21 crosses. But we need to check if 21 is achievable.

Wait, but it's not just about covering cells. We need 21 non-overlapping crosses, which cover 105 cells. The 4 corner cells can't be covered, so we'd have 110 - 105 = 5 uncovered cells, including the 4 corners plus 1 more.

Let me think about the upper bound more carefully. Can we achieve 21?

Let me think about which cells can't be covered. The corners (1,1), (1,11), (10,1), (10,11). Are there other cells that can't be covered?

Cell (1,2): can be covered by center at (2,2) [covers (1,2),(2,1),(2,2),(2,3),(3,2)] — yes, (1,2) is covered. Or center at (1,3) — but (1,3) is not valid (i=1). So (1,2) can be covered by (2,2). Good.

Cell (1,j) for 2 ≤ j ≤ 10: covered by center (2,j). Valid since 2 ≤ 2 ≤ 9 and 2 ≤ j ≤ 10. Good.

Cell (1,11): covered by center (2,11)? But j=11 > 10, so (2,11) is not a valid center. Center (1,10)? i=1, not valid. So (1,11) can't be covered. Confirmed.

So only the 4 corners can't be covered. So the upper bound from area is floor(106/5) = 21.

But we need to verify 21 is achievable. Let me think about whether there are additional constraints.

Let me use the mod-5 coloring again. Each cross covers one cell of each color. With 21 crosses, we cover 21 cells of each color. The board has 22 cells of each color (computed above). So we'd leave 1 cell of each color uncovered. The 4 corners are always uncovered. Let me check the colors of the 4 corners:

(1,1): (1 + 2·1) mod 5 = 3
(1,11): (1 + 22) mod 5 = 23 mod 5 = 3
(10,1): (10 + 2) mod 5 = 12 mod 5 = 2
(10,11): (10 + 22) mod 5 = 32 mod 5 = 2

So the 4 corners have colors 3, 3, 2, 2. If 21 crosses leave 5 cells uncovered (including these 4 corners), the uncovered cells must have one of each color (since 22 - 21 = 1 of each color uncovered). The 4 corners contribute 2 of color 3 and 2 of color 2. So we need 1 more uncovered cell, and the total uncovered should be 1 of each color: color 0: 1, color 1: 1, color 2: 1, color 3: 1, color 4: 1.

But the 4 corners already give color 2: 2 and color 3: 2, which exceeds 1 each. Contradiction!

So with 21 crosses, we'd leave 5 cells uncovered, and by the mod-5 coloring, exactly 1 of each color must be uncovered. But the 4 corners force at least 2 of color 2 and 2 of color 3 to be uncovered. That's a contradiction. So 21 is impossible!

Therefore the maximum is at most 20.

With 20 crosses, we cover 100 cells, leaving 10 uncovered. By the mod-5 coloring, we leave 22 - 20 = 2 of each color uncovered. The 4 corners give colors 3,3,2,2. We need 2 of each color total. So far we have color 2: 2 (done), color 3: 2 (done). We still need color 0: 2, color 1: 2, color 4: 2. That's 6 more uncovered cells, totaling 4 + 6 = 10. Consistent!

So 20 is not ruled out by this argument. Let me check if 20 is achievable.

Actually, let me also verify: is there another coloring that might give a tighter bound?

Let me try other colorings. Let me try (i + 3j) mod 5 or (2i + j) mod 5, etc.

For (2i + j) mod 5: Cross at (i,j) covers:
- Center: 2i + j
- (i-1,j): 2(i-1) + j = 2i + j - 2
- (i+1,j): 2i + j + 2
- (i,j-1): 2i + j - 1
- (i,j+1): 2i + j + 1

So colors {c-2, c-1, c, c+1, c+2} mod 5 = all 5. Same property.

For (i + 3j) mod 5: 
- Center: i + 3j
- (i-1,j): i + 3j - 1
- (i+1,j): i + 3j + 1
- (i,j-1): i + 3j - 3
- (i,j+1): i + 3j + 3

Colors {c-3, c-1, c, c+1, c+3} mod 5 = {c, c±1, c±3} mod 5. Is this all 5? c-3, c-1, c, c+1, c+3 mod 5. If c=0: {2, 4, 0, 1, 3} = all 5. Yes! So any coloring (ai + bj) mod 5 where {0, ±a, ±b} mod 5 = all of {0,1,2,3,4} works. This requires a, b nonzero and a ≠ ±b mod 5.

For (a,b) = (1,2): {0, ±1, ±2} = {0,1,4,2,3} = all 5. ✓
For (a,b) = (1,3): {0, ±1, ±3} = {0,1,4,3,2} = all 5. ✓
For (a,b) = (2,1): same as (1,2). ✓
For (a,b) = (1,4): {0, ±1, ±4} = {0,1,4,4,1} — only 3 values. ✗

So (1,2), (1,3), (2,1), (2,3), (3,1), (3,2) etc. all work. But they all give the same constraint: each cross covers one of each color, so the number of crosses ≤ min color count.

Let me check if different colorings give different color distributions on the 10×11 board, potentially with a smaller minimum.

For (i + 3j) mod 5: For fixed i, 3j mod 5 as j=1..11: 3,1,4,2,0,3,1,4,2,0,3. Counts: 0→2, 1→2, 2→2, 3→3, 4→2. Similar structure, just different color gets the extra. Over 10 rows with i mod 5 each appearing twice, by the same calculation, each color gets 22. Same result.

So all these colorings give 22 per color, and the constraint is the same: uncovered cells must have equal counts per color.

So the upper bound from this method is 20 (as derived above). Let me now try to construct a placement of 20 crosses.

Let me try to construct 20 non-overlapping crosses on the 10×11 board.

The centers must be at mutual Manhattan distance ≥ 3, and within {2..9} × {2..10}.

Let me try a systematic approach. Let me think of the board as 10 rows × 11 columns.

Let me try placing crosses in a pattern. Consider centers at positions where (i mod 3, j mod 3) takes specific values.

If I place centers at (i,j) where i ≡ 2 mod 3 and j ≡ 2 mod 3:
i ∈ {2, 5, 8}, j ∈ {2, 5, 8}. That's 3×3 = 9 centers. Manhattan distance between (2,2) and (2,5) is 3, between (2,2) and (5,2) is 3, between (2,2) and (5,5) is 6. All ≥ 3. Good, 9 crosses.

But I need 20. Let me think about a denser packing.

Actually, the constraint is Manhattan distance ≥ 3. Let me think about the maximum independent set in this graph.

Hmm, let me think about it differently. Let me try to use a pattern that covers more of the board.

Let me try centers at:
- Rows 2, 5, 8 (spaced 3 apart)
- In each row, centers at columns 2, 5, 8 (spaced 3 apart)

That gives 9. But I can also use rows 3, 6, 9 with different column offsets.

Let me try:
Row 2: columns 2, 5, 8 → 3 crosses
Row 3: columns 3, 6, 9 → but (2,2) and (3,3) have Manhattan distance 2. Overlap!

So I can't use adjacent rows with offset 1. Let me think more carefully.

If two centers are in adjacent rows (differ by 1), their columns must differ by ≥ 2. If they're in the same row, columns differ by ≥ 3. If rows differ by 2, columns must differ by ≥ 1. If rows differ by ≥ 3, any columns OK.

Let me try a pattern with rows 2, 4, 6, 8 (every other row):
Row 2: cols 2, 5, 8 → 3
Row 4: cols 3, 6, 9 → check (2,2) vs (4,3): dist = 2+1 = 3. OK. (2,5) vs (4,3): 2+2=4. OK. (2,5) vs (4,6): 2+1=3. OK. (2,8) vs (4,9): 2+1=3. OK. (2,8) vs (4,6): 2+2=4. OK. Good.
Row 6: cols 2, 5, 8 → check (4,3) vs (6,2): 2+1=3. OK. (4,3) vs (6,5): 2+2=4. OK. (4,6) vs (6,5): 2+1=3. OK. (4,6) vs (6,8): 2+2=4. OK. (4,9) vs (6,8): 2+1=3. OK. Good.
Row 8: cols 3, 6, 9 → similar checks pass.

So rows 2,4,6,8 with alternating column offsets {2,5,8} and {3,6,9}:
Row 2: {2,5,8} → 3
Row 4: {3,6,9} → 3
Row 6: {2,5,8} → 3
Row 8: {3,6,9} → 3
Total: 12 crosses.

Can I do better? Let me also use rows 3, 5, 7, 9 or add more.

Actually, let me try to use all even rows: 2, 4, 6, 8. That's 4 rows × 3 = 12. Can I add more in odd rows?

Row 3 is between rows 2 and 4. A center in row 3 must be at distance ≥ 3 from all centers in rows 2 and 4. Centers in row 2 are at cols {2,5,8}, row 4 at cols {3,6,9}. A center at (3, c) must have |3-2| + |c - c'| ≥ 3 for all c' in {2,5,8}, i.e., 1 + |c - c'| ≥ 3, so |c - c'| ≥ 2 for all c' in {2,5,8}. So c ∉ {0,1,2,3,4, 3,4,5,6, 6,7,8,9} = c ∉ {0..9} effectively. And from row 4: |c - c'| ≥ 2 for c' in {3,6,9}, so c ∉ {1..5, 4..8, 7..11} = c ∉ {1..11}. So c must be outside {1..11}, impossible. So no centers in row 3.

Similarly, no centers in rows 5, 7 (between used rows). What about row 9? Row 9 is below row 8. (9, c) vs (8, c') in {3,6,9}: 1 + |c - c'| ≥ 3, so |c - c'| ≥ 2. c ∉ {1..5, 4..8, 7..11} = {1..11}. Impossible.

What about row 10? Not a valid center (i=10, need i≤9). Row 1? Not valid (i=1).

So with this pattern, 12 is what we get. That's not enough. Let me try a different approach.

Let me try using rows 2, 3, 5, 6, 8, 9 (pairs of adjacent rows, then a gap).

Row 2: cols 2, 5, 8 → 3
Row 3: must be at dist ≥ 3 from row 2 centers. |c - c'| ≥ 2 for c' in {2,5,8}. So c ∈ {4, 7, 10} (checking: c=4: |4-2|=2,|4-5|=1 <2. No!). Hmm, c=4: |4-2|=2 ✓, |4-5|=1 ✗. So c=4 doesn't work.

c must satisfy |c-2|≥2 AND |c-5|≥2 AND |c-8|≥2. So c ≤ 0 or c ∈ [4,4] (but |4-5|=1, no) or... Let me compute: c ∉ [0,4] ∪ [3,7] ∪ [6,10] = [0,10]. So c ∈ {11} but also need c ≤ 10 (valid center). So no valid c in row 3. 

Hmm, this is tricky. Let me think differently.

The issue is that in a row with 3 centers spaced 3 apart, the next row can't have any centers (because the gap requirement is too strict).

Let me try rows with only 2 centers, allowing more rows to be used.

Row 2: cols 2, 6 → 2 (distance 4, fine)
Row 3: cols 4, 8 → check vs row 2: (3,4) vs (2,2): 1+2=3 ✓. (3,4) vs (2,6): 1+2=3 ✓. (3,8) vs (2,6): 1+2=3 ✓. (3,8) vs (2,2): 1+6=7 ✓. Good. 2 crosses.
Row 4: cols 2, 6 → check vs row 3: (4,2) vs (3,4): 1+2=3 ✓. (4,2) vs (3,8): 1+6=7 ✓. (4,6) vs (3,4): 1+2=3 ✓. (4,6) vs (3,8): 1+2=3 ✓. Good. 2 crosses.
Row 5: cols 4, 8 → similar. 2 crosses.
...

This gives a pattern: even rows use cols {2,6}, odd rows use cols {4,8}. Wait, but I should also consider more columns.

Actually, let me try to maximize. With cols {2, 6} and {4, 8}, I get 2 per row. Over rows 2-9 (8 rows), that's 16 crosses. Can I add more columns?

Row 2: cols 2, 6, 10 → 3 (distances 4, 4, 8 — all ≥ 3 ✓)
Row 3: need |c - c'| ≥ 2 for c' in {2, 6, 10}. c ∉ [0,4] ∪ [4,8] ∪ [8,12] = [0,12]. So no valid c. Hmm.

So 3 per row blocks the next row entirely. 2 per row with the right offset allows alternating.

With the 2-per-row alternating pattern: rows 2,3,4,5,6,7,8,9 → 8 rows × 2 = 16 crosses. Can I do better?

Let me try 2 per row but with a different column choice to potentially fit 3 in some rows.

Actually, let me try:
Row 2: cols 2, 6, 10 → 3
Row 3: (blocked) → 0
Row 4: cols 2, 6, 10 → 3
Row 5: (blocked) → 0
Row 6: cols 2, 6, 10 → 3
Row 7: (blocked) → 0
Row 8: cols 2, 6, 10 → 3
Row 9: (blocked) → 0
Total: 12. Worse than 16.

What about mixing? 
Row 2: cols 2, 6 → 2
Row 3: cols 4, 8 → 2
Row 4: cols 2, 6 → 2
Row 5: cols 4, 8 → 2
Row 6: cols 2, 6 → 2
Row 7: cols 4, 8 → 2
Row 8: cols 2, 6 → 2
Row 9: cols 4, 8 → 2
Total: 16.

Can I add a 3rd column to some rows? In row 2 with cols {2, 6}, can I add col 10? (2,10) vs (3,8): 1+2=3 ✓. (2,10) vs (3,4): 1+6=7 ✓. So yes! Row 2: cols 2, 6, 10 → 3. But then row 3 with cols {4, 8}: (3,4) vs (2,10): 1+6=7 ✓, (3,8) vs (2,10): 1+2=3 ✓. Still OK!

But wait, does adding col 10 to row 2 block row 3? (3, c) vs (2, 10): need 1 + |c-10| ≥ 3, so |c-10| ≥ 2, c ≤ 8 or c ≥ 12. Row 3 has cols {4, 8}, both ≤ 8. ✓.

What about row 1? Not valid. 

Let me try to add more. Can row 3 also have 3 columns? Row 3: cols 4, 8, and what else? Need distance ≥ 3 from {4, 8} in same row: col c with |c-4|≥3 and |c-8|≥3. c ≤ 1 or c = 11... c ≤ 1: not valid (need ≥ 2). c = 11: not valid (need ≤ 10). Hmm, what about c = 11? No, max is 10. So only 2 in row 3 with this offset.

Wait, what if I use different offsets? Let me try:
Row 2: cols 2, 6, 10 → 3
Row 3: cols 4, 8 → 2
Row 4: cols 2, 6, 10 → 3
Row 5: cols 4, 8 → 2
Row 6: cols 2, 6, 10 → 3
Row 7: cols 4, 8 → 2
Row 8: cols 2, 6, 10 → 3
Row 9: cols 4, 8 → 2
Total: 3+2+3+2+3+2+3+2 = 20!

Let me verify all the distance constraints carefully.

Even rows (2,4,6,8): cols {2, 6, 10}
Odd rows (3,5,7,9): cols {4, 8}

Same-row distances: 
- Even: |2-6|=4, |6-10|=4, |2-10|=8. All ≥ 3. ✓
- Odd: |4-8|=4 ≥ 3. ✓

Adjacent row distances (differ by 1):
- Even row {2,6,10} vs odd row {4,8}: need 1 + |c_even - c_odd| ≥ 3, so |c_even - c_odd| ≥ 2.
  - |2-4|=2 ✓, |2-8|=6 ✓, |6-4|=2 ✓, |6-8|=2 ✓, |10-4|=6 ✓, |10-8|=2 ✓. All ≥ 2. ✓

Two-apart rows (differ by 2):
- Even vs even (e.g., row 2 vs row 4): need 2 + |c - c'| ≥ 3, so |c - c'| ≥ 1. Since all columns are from {2,6,10}, any two different ones differ by ≥ 4. Same column: |c-c|=0, so 2+0=2 < 3. ✗!

Wait, row 2 col 2 and row 4 col 2: Manhattan distance = 2 + 0 = 2 < 3. They overlap!

So this doesn't work. The crosses at (2,2) and (4,2) overlap because (2,2) covers (3,2) and (4,2) covers (3,2). Indeed Manhattan distance 2.

So I need to fix this. For rows differing by 2, columns must differ by ≥ 1.

So even rows can't all use the same columns. Let me adjust.

Let me try:
Row 2: cols 2, 6, 10
Row 3: cols 4, 8
Row 4: cols 3, 7 (shifted by 1 from row 2 to avoid same-column conflict)

Wait, but row 4 vs row 3: {3,7} vs {4,8}: |3-4|=1, need ≥ 2. 1+1=2 < 3. ✗.

Hmm. Let me reconsider.

For rows differing by 2, columns must differ by ≥ 1. For rows differing by 1, columns must differ by ≥ 2.

Let me try a 3-row pattern that repeats:
Row A: cols {2, 6, 10}
Row B: cols {4, 8}
Row C: cols {3, 7} (differs from A by ≥ 1 in each column, differs from B by ≥ 2)

Check B vs C: {4,8} vs {3,7}: |4-3|=1 < 2. ✗.

Try Row C: cols {5, 9}: vs B {4,8}: |5-4|=1 < 2. ✗.

Hmm. The problem is that with cols {4,8} in row B, row C (1 below) needs cols at distance ≥ 2 from both 4 and 8, and row C (2 below A) needs cols at distance ≥ 1 from {2,6,10}.

Distance ≥ 2 from {4,8}: c ∉ {2,3,4,5,6, 6,7,8,9,10} = {2..10}. So c ∈ {11} but max is 10. Or c ≤ 1, min is 2. So no valid columns! 

So the 3-per-row pattern for even rows blocks the row 2 below the odd row. This means we can't have a repeating pattern of ABA with 3 in A rows.

Let me try a different approach. Let me use a 4-row repeating pattern.

Actually, let me step back and think about this more carefully.

Let me try to use a pattern where every row has 2 crosses, but use all 8 rows (2-9), giving 16. Then try to add 4 more in strategic positions.

Or, let me try a different pattern entirely.

Let me think about it as follows. Consider the "diagonal" pattern. Place crosses at positions (i, j) where i + j ≡ 0 mod 3 and i - j ≡ 0 mod 2, or some such lattice.

Actually, let me think about the L∞ metric. Two crosses at (i,j) and (i',j') overlap iff |i-i'| + |j-j'| ≤ 2. Non-overlap requires Manhattan distance ≥ 3.

Let me think about this as a packing problem. I want to maximize the number of points in {2..9} × {2..10} with pairwise Manhattan distance ≥ 3.

The grid is 8 × 9 = 72 points. By an area argument, each point "blocks" a diamond of radius 2 (Manhattan), which has 1 + 4 + 8 = 13 cells... but that's not quite right for a packing bound.

Let me think about it differently. Consider the transformation u = i + j, v = i - j. Manhattan distance ≥ 3 in (i,j) corresponds to max(|Δu|, |Δv|) ≥ 3... no, that's L∞ in (u,v) which corresponds to L1 in (i,j) only if... actually |Δi| + |Δj| = max(|Δu|, |Δv|) is not correct. We have |Δi| + |Δj| = max(|Δu|, |Δv|) only when... no. Actually, |Δi| + |Δj| and max(|Δu|, |Δv|) = max(|Δi+Δj|, |Δi-Δj|). And |Δi| + |Δj| = max(|Δi+Δj|, |Δi-Δj|) is true! Because |a| + |b| = max(|a+b|, |a-b|).

So Manhattan distance in (i,j) = L∞ distance in (u,v) = (i+j, i-j). So we need L∞ distance ≥ 3 in the (u,v) coordinates.

So we need to pack points in the (u,v) plane with L∞ distance ≥ 3, which means we're placing points on a grid with spacing 3 in both u and v directions. The maximum density is 1/9 (one point per 3×3 square in (u,v)).

The (u,v) range: i from 2..9, j from 2..10. u = i+j ranges from 4 to 19. v = i-j ranges from -8 to 7. So u ∈ [4,19] (16 values), v ∈ [-8,7] (16 values). But u and v must have the same parity (since u+v = 2i is even). So effectively, we're on a 16×16 grid (in terms of valid (u,v) pairs with matching parity), but actually the number of valid (u,v) pairs is 72 (same as the number of (i,j) points).

With L∞ spacing 3, we can fit roughly (16/3) × (16/3) ≈ 5.33 × 5.33 ≈ 28 points. But that's an overestimate because of parity constraints and boundary effects.

Hmm, this is getting complicated. Let me just try to construct 20 explicitly.

Let me try a different approach. Let me use the (u,v) = (i+j, i-j) transformation and place points on a lattice.

If I place points at (u,v) where u ≡ a mod 3 and v ≡ b mod 3, then any two points have L∞ distance ≥ 3 (actually, they have L∞ distance that's a multiple of 3, so ≥ 3 if distinct). But I need u ≡ v mod 2 (parity constraint).

Let me try u ≡ 0 mod 3, v ≡ 0 mod 3. Then u ∈ {6, 9, 12, 15, 18}, v ∈ {-6, -3, 0, 3, 6}. But need u ≡ v mod 2: 6≡0, -6≡0: same parity ✓. 9≡1, -3≡1: same ✓. 12≡0, 0≡0 ✓. 15≡1, 3≡1 ✓. 18≡0, 6≡0 ✓. So all combinations where u and v have the same parity.

u=6 (even): v must be even: {-6, 0, 6} → 3 points
u=9 (odd): v must be odd: {-3, 3} → 2 points
u=12 (even): v even: {-6, 0, 6} → 3 points
u=15 (odd): v odd: {-3, 3} → 2 points
u=18 (even): v even: {-6, 0, 6} → 3 points

Total: 3+2+3+2+3 = 13 points.

Let me try u ≡ 1 mod 3, v ≡ 1 mod 3. u ∈ {4, 7, 10, 13, 16, 19}, v ∈ {-8, -5, -2, 1, 4, 7}.
Parity: u=4 (even), v must be even: {-8, -2, 4} → 3
u=7 (odd), v odd: {-5, 1, 7} → 3
u=10 (even), v even: {-8, -2, 4} → 3
u=13 (odd), v odd: {-5, 1, 7} → 3
u=16 (even), v even: {-8, -2, 4} → 3
u=19 (odd), v odd: {-5, 1, 7} → 3
Total: 18 points!

Let me verify these map to valid (i,j). For each (u,v), i = (u+v)/2, j = (u-v)/2. Need 2 ≤ i ≤ 9, 2 ≤ j ≤ 10.

u=4, v=-8: i=(4-8)/2=-2. Invalid.
u=4, v=-2: i=(4-2)/2=1. Invalid (need ≥2).
u=4, v=4: i=(4+4)/2=4, j=(4-4)/2=0. Invalid (need ≥2).

Hmm, u=4 is too small. Let me check which (u,v) pairs give valid (i,j).

i = (u+v)/2, j = (u-v)/2. Need 2 ≤ (u+v)/2 ≤ 9 and 2 ≤ (u-v)/2 ≤ 10.
So 4 ≤ u+v ≤ 18 and 4 ≤ u-v ≤ 20.

Let me enumerate for u ≡ 1 mod 3, v ≡ 1 mod 3:

u=4: v ∈ {-8,-2,4}. 
  v=-8: u+v=-4 <4. Invalid.
  v=-2: u+v=2 <4. Invalid.
  v=4: u-v=0 <4. Invalid.

u=7: v ∈ {-5,1,7}.
  v=-5: u+v=2 <4. Invalid.
  v=1: u+v=8 ✓, u-v=6 ✓. i=4, j=3. Valid!
  v=7: u+v=14 ✓, u-v=0 <4. Invalid.

u=10: v ∈ {-8,-2,4}.
  v=-8: u+v=2 <4. Invalid.
  v=-2: u+v=8 ✓, u-v=12 ✓. i=4, j=6. Valid!
  v=4: u+v=14 ✓, u-v=6 ✓. i=7, j=3. Valid!

u=13: v ∈ {-5,1,7}.
  v=-5: u+v=8 ✓, u-v=18 ✓. i=4, j=9. Valid!
  v=1: u+v=14 ✓, u-v=12 ✓. i=7, j=6. Valid!
  v=7: u+v=20 >18. Invalid.

u=16: v ∈ {-8,-2,4}.
  v=-8: u+v=8 ✓, u-v=24 >20. Invalid.
  v=-2: u+v=14 ✓, u-v=18 ✓. i=7, j=9. Valid!
  v=4: u+v=20 >18. Invalid.

u=19: v ∈ {-5,1,7}.
  v=-5: u+v=14 ✓, u-v=24 >20. Invalid.
  v=1: u+v=20 >18. Invalid.
  v=7: u+v=26 >18. Invalid.

Valid points: (4,3), (4,6), (7,3), (4,9), (7,6), (7,9). That's only 6 points! Much less than 18.

The issue is many (u,v) pairs map outside the board. The (u,v) region is a rotated rectangle, not axis-aligned, so the lattice doesn't pack as well.

Let me try a different lattice. Let me try u ≡ 0 mod 3, v ≡ 0 mod 3:

u ∈ {6, 9, 12, 15, 18}, v ∈ {-6, -3, 0, 3, 6}.

u=6 (even), v even {-6, 0, 6}:
  v=-6: u+v=0 <4. Invalid.
  v=0: u+v=6 ✓, u-v=6 ✓. i=3, j=3. Valid!
  v=6: u+v=12 ✓, u-v=0 <4. Invalid.

u=9 (odd), v odd {-3, 3}:
  v=-3: u+v=6 ✓, u-v=12 ✓. i=3, j=6. Valid!
  v=3: u+v=12 ✓, u-v=6 ✓. i=6, j=3. Valid!

u=12 (even), v even {-6, 0, 6}:
  v=-6: u+v=6 ✓, u-v=18 ✓. i=3, j=9. Valid!
  v=0: u+v=12 ✓, u-v=12 ✓. i=6, j=6. Valid!
  v=6: u+v=18 ✓, u-v=6 ✓. i=9, j=3. Valid!

u=15 (odd), v odd {-3, 3}:
  v=-3: u+v=12 ✓, u-v=18 ✓. i=6, j=9. Valid!
  v=3: u+v=18 ✓, u-v=12 ✓. i=9, j=6. Valid!

u=18 (even), v even {-6, 0, 6}:
  v=-6: u+v=12 ✓, u-v=24 >20. Invalid.
  v=0: u+v=18 ✓, u-v=18 ✓. i=9, j=9. Valid!
  v=6: u+v=24 >18. Invalid.

Valid: (3,3), (3,6), (6,3), (3,9), (6,6), (9,3), (6,9), (9,6), (9,9). That's 9 points.

These are the points where i ≡ 0 mod 3 and j ≡ 0 mod 3 (with i,j ∈ {3,6,9}). That's the 3×3 grid I found earlier.

Let me try combining two lattices. For example, u ≡ 0 mod 3, v ≡ 0 mod 3 AND u ≡ 1 mod 3, v ≡ 2 mod 3 (or some other shift). But I need to ensure cross-lattice distances are also ≥ 3.

Two points from different lattices: (u1, v1) with u1 ≡ 0, v1 ≡ 0 and (u2, v2) with u2 ≡ 1, v2 ≡ 2. Then Δu = u2 - u1 ≡ 1 mod 3, so |Δu| ≥ 1. Δv = v2 - v1 ≡ 2 mod 3, so |Δv| ≥ 2. L∞ distance = max(|Δu|, |Δv|) ≥ 2. But we need ≥ 3! So this doesn't work if |Δu| = 1 and |Δv| = 2.

Hmm. So combining lattices with shifts (1,2) gives L∞ distance potentially 2, which is too small.

For L∞ ≥ 3, I need both |Δu| ≥ 3 or both shifts to be 0 mod 3. So I can only use one lattice (one residue class mod 3 in both u and v). Unless I use a different spacing.

What if I use spacing 3 in one direction and something else in the other? Or a non-lattice arrangement?

Let me think about this differently. The maximum number of points with L∞ distance ≥ 3 in the (u,v) diamond-shaped region.

Actually, let me just try to construct 20 crosses directly by hand, or use a computer search... but I can't use tools. Let me think more carefully.

Let me reconsider. The (u,v) region: u = i+j, v = i-j, with 2≤i≤9, 2≤j≤10. The region is a parallelogram (rotated rectangle). In (u,v) coordinates, the constraints are:
- 4 ≤ u+v ≤ 18 (from 2≤i≤9)
- 4 ≤ u-v ≤ 20 (from 2≤j≤10)

And u, v have the same parity.

The L∞ distance ≥ 3 constraint means we're looking for an independent set in a grid graph with spacing 3.

The maximum number of points with L∞ ≥ 3 in a region is roughly area / 9. The area of the (u,v) region: it's a parallelogram. The original region has 72 points (8×9). In (u,v) space, the "area" per point is 2 (since (u,v) and (u+1,v+1) map to the same (i,j) if parity matches... actually the mapping is 1-1 for same-parity pairs). The parallelogram has vertices at (u,v) = (4,0), (12,-8), (18,0), (12,8)... let me compute:

Corners of the (i,j) region: (2,2)→(4,0), (2,10)→(12,-8), (9,2)→(11,7), (9,10)→(19,-1).

Hmm, it's a parallelogram with vertices (4,0), (12,-8), (19,-1), (11,7). The area = |det| of the side vectors. Side 1: (12,-8)-(4,0) = (8,-8). Side 2: (11,7)-(4,0) = (7,7). Area = |8·7 - (-8)·7| = |56+56| = 112. But this is in (u,v) space where each (i,j) point takes up 2 units of area (since u,v change by 2 for each step in i or j). So number of points ≈ 112/2 = 56... but we know there are 72 points. Let me recheck.

Actually, the mapping (i,j) → (u,v) = (i+j, i-j) has Jacobian 2. So area in (u,v) = 2 × area in (i,j) = 2 × 72 = 144. But the parallelogram area I computed is 112. Let me recheck the vertices.

(i,j) region: i from 2 to 9 (8 values), j from 2 to 10 (9 values). This is a rectangle with corners (2,2), (2,10), (9,2), (9,10).

(2,2) → u=4, v=0
(2,10) → u=12, v=-8
(9,2) → u=11, v=7
(9,10) → u=19, v=-1

Parallelogram with vertices (4,0), (12,-8), (19,-1), (11,7).
Side vectors: (12,-8)-(4,0) = (8,-8) and (11,7)-(4,0) = (7,7).
Area = |8·7 - (-8)·7| = |56 + 56| = 112.

But 2 × 8 × 9 = 144 ≠ 112. Something's wrong. Oh, the mapping (i,j) → (i+j, i-j) has Jacobian |det([[1,1],[1,-1]])| = |-2| = 2. So area in (u,v) = 2 × area in (i,j). The (i,j) rectangle has area 7 × 8 = 56 (continuous area, from 2 to 9 is length 7, from 2 to 10 is length 8). 2 × 56 = 112. ✓. The number of integer points is 8 × 9 = 72, and in (u,v) space with the parity constraint, we also get 72 points.

For L∞ packing with spacing 3, the max number of points is roughly area/9 = 112/9 ≈ 12.4. But this is a rough estimate. With the parity constraint and boundary effects, it could be more or less.

Hmm, 12 is close to what I got with the lattice. But I need 20. That seems way more than 12. Am I making an error?

Wait, I think I'm overcomplicating this. Let me reconsider.

Oh wait, I think the issue is that L∞ distance ≥ 3 in (u,v) is a very strong constraint. Each point blocks a 5×5 = 25 cell region (in (u,v) integer grid, but with parity constraint, effectively 13 points). So the max is roughly 72/13 ≈ 5.5... that's way too low.

No wait, that's not right either. The blocking argument gives an upper bound of 72/13 ≈ 5.5, but we already found 9 points with the lattice. The issue is that the blocking regions overlap near the boundary.

Actually, the L∞ distance ≥ 3 constraint means that in the (u,v) grid, we can place at most one point per 3×3 block. The (u,v) region spans u from 4 to 19 (16 values) and v from -8 to 7 (16 values), but only same-parity pairs are valid. If we think of the valid grid as having 16×16 = 256 cells but only 72 valid (same parity), then with 3×3 blocking, we can fit at most ceil(16/3) × ceil(16/3) = 6×6 = 36 points (without parity constraint). With parity, maybe ~18.

But I only found 9 with a single lattice. Let me try to do better by not using a lattice.

Actually, let me reconsider. The L∞ distance ≥ 3 means we need points that are at least 3 apart in both u and v. So if we sort by u, consecutive points differ by ≥ 3 in u OR they differ by ≥ 3 in v. Actually no, L∞ ≥ 3 means max(|Δu|, |Δv|) ≥ 3, which means |Δu| ≥ 3 OR |Δv| ≥ 3. Wait no! L∞ distance ≥ 3 means max(|Δu|, |Δv|) ≥ 3. But we need the distance to be ≥ 3, so we need max(|Δu|, |Δv|) ≥ 3.

Hmm wait, I think I had it backwards. Manhattan distance in (i,j) = |Δi| + |Δj|. And |Δi| + |Δj| = max(|Δi + Δj|, |Δi - Δj|) = max(|Δu|, |Δv|). So Manhattan distance = L∞ distance in (u,v). We need Manhattan ≥ 3, so L∞ ≥ 3, so max(|Δu|, |Δv|) ≥ 3.

But this means we need |Δu| ≥ 3 OR |Δv| ≥ 3. This is much weaker than requiring both! Two points can be close in u as long as they're far in v, and vice versa.

So the constraint is NOT that both |Δu| ≥ 3 and |Δv| ≥ 3. It's that at least one of them is ≥ 3. This means we can pack much more densely!

So in the (u,v) plane, we need an independent set in the graph where two points are connected if both |Δu| ≤ 2 and |Δv| ≤ 2 (i.e., L∞ distance ≤ 2). This is like a kings graph with radius 2.

The maximum independent set in a grid with L∞ distance ≥ 3... this is like a chess problem. We can place points in a "staggered" pattern.

For example, in a 1D line, we can place points every 3 units. In 2D with L∞ ≥ 3, we can place points in a pattern where each 3×3 block has one point, giving density 1/9. But we can also do better with non-lattice patterns? No, 1/9 is the max density for L∞ ≥ 3 in 2D.

Wait, is it? For L∞ ≥ 3, we need each 3×3 block (in the integer grid) to contain at most one point. The max density is 1/9. But with the parity constraint, it might be different.

Actually, 1/9 is the max density. With 72 valid points in a region of "area" 112 (in (u,v) continuous coordinates), the max is about 112/9 ≈ 12.4, so about 12 points. But this seems too low — we need 20.

Wait, I think I'm confusing myself. Let me recompute. The 72 valid (i,j) points map to 72 (u,v) points. The (u,v) region has area 112. With density 1/9, max points ≈ 112/9 ≈ 12.4. But we need 20 crosses, which means 20 centers. 20 > 12.4, so this suggests 20 is impossible?

But wait, the density 1/9 is for continuous space. In discrete space with the parity constraint, things might differ. Also, the 1/9 bound assumes we're tiling with 3×3 blocks, but the region is a parallelogram, and boundary effects can be significant.

Hmm, but actually, I realize the 1/9 density bound might not be tight for this specific region. Let me reconsider.

Actually, let me reconsider whether 1/9 is the right density. For L∞ distance ≥ 3, we need every pair of points to have |Δu| ≥ 3 or |Δv| ≥ 3. Consider the points in a column (fixed u). They must all have |Δv| ≥ 3 (since |Δu| = 0 < 3). So in each column, points are spaced ≥ 3 in v. Similarly, in each row (fixed v), points are spaced ≥ 3 in u.

But points in different columns can be close in v as long as they're ≥ 3 apart in u. So the density can be higher than 1/9? No, I think 1/9 is correct. Consider tiling the plane with 3×3 blocks. Each block can contain at most one point (since any two points in a 3×3 block have L∞ distance ≤ 2). So the density is at most 1/9.

But in our case, the "grid" only has same-parity (u,v) pairs. So each 3×3 block contains at most... let me think. A 3×3 block in (u,v) has 9 cells, but only about 5 have the right parity (either 4 or 5 depending on alignment). And at most 1 of those can be chosen. So the density among valid cells is at most 1/5 ≈ 0.2, giving max ≈ 72 × 0.2 ≈ 14.4, so about 14.

Hmm, but I already found 9 with a lattice. Let me try to find more.

Actually, I realize I should think about this problem differently. Let me go back to the (i,j) coordinates and think about it directly.

The constraint is: centers at mutual Manhattan distance ≥ 3. Let me try to find a good packing.

Let me try a "brick" pattern. In row i, place centers at columns j where j ≡ f(i) mod 3, for some function f.

If f(i) = i mod 3, then centers at (i, j) where j ≡ i mod 3. Two centers (i, j) and (i', j') with j ≡ i mod 3 and j' ≡ i' mod 3. Manhattan distance = |i-i'| + |j-j'|. We need this ≥ 3.

If i = i' (same row): |j - j'| ≥ 3 (since j ≡ j' mod 3 and j ≠ j', so |j-j'| ≥ 3). ✓
If |i - i'| = 1: j - j' ≡ i - i' ≡ ±1 mod 3, so |j - j'| ≥ 1 (could be 1, 2, 4, 5, ...). Manhattan = 1 + |j-j'|. If |j-j'| = 1, Manhattan = 2 < 3. ✗!

So this doesn't work for adjacent rows. Let me try f(i) = 2i mod 3.

j ≡ 2i mod 3. If |i-i'| = 1: j - j' ≡ 2(i-i') ≡ ±2 mod 3. So |j-j'| ≡ 2 mod 3, meaning |j-j'| ∈ {2, 5, 8, ...}. Minimum |j-j'| = 2. Manhattan = 1 + 2 = 3. ✓!

If |i-i'| = 2: j - j' ≡ 2·2 = 4 ≡ 1 mod 3. |j-j'| ∈ {1, 4, 7, ...}. Minimum 1. Manhattan = 2 + 1 = 3. ✓!

If |i-i'| ≥ 3: Manhattan ≥ 3. ✓.

So the pattern j ≡ 2i mod 3 works! All pairwise Manhattan distances are ≥ 3.

Now let me count how many such points fit in {2..9} × {2..10}.

For each row i from 2 to 9, j ≡ 2i mod 3, and j ∈ {2..10}.

i=2: 2i=4, 4 mod 3 = 1. j ≡ 1 mod 3. j ∈ {4, 7, 10}. 3 values.
i=3: 2i=6, 6 mod 3 = 0. j ≡ 0 mod 3. j ∈ {3, 6, 9}. 3 values.
i=4: 2i=8, 8 mod 3 = 2. j ≡ 2 mod 3. j ∈ {2, 5, 8}. 3 values.
i=5: 2i=10, 10 mod 3 = 1. j ≡ 1 mod 3. j ∈ {4, 7, 10}. 3 values.
i=6: 2i=12, 12 mod 3 = 0. j ≡ 0 mod 3. j ∈ {3, 6, 9}. 3 values.
i=7: 2i=14, 14 mod 3 = 2. j ≡ 2 mod 3. j ∈ {2, 5, 8}. 3 values.
i=8: 2i=16, 16 mod 3 = 1. j ≡ 1 mod 3. j ∈ {4, 7, 10}. 3 values.
i=9: 2i=18, 18 mod 3 = 0. j ≡ 0 mod 3. j ∈ {3, 6, 9}. 3 values.

Total: 8 × 3 = 24 points! But wait, we need to check that all these are valid centers, i.e., 2 ≤ i ≤ 9 and 2 ≤ j ≤ 10. Let me verify: all i are in {2..9} ✓, all j are in {2..10} ✓.

But 24 crosses would cover 24 × 5 = 120 cells, but the board only has 110 cells! That's impossible. So there must be overlaps.

Wait, I proved that all pairwise Manhattan distances are ≥ 3, which means no two crosses share a cell. But 24 × 5 = 120 > 110. Contradiction!

Let me recheck. Oh, I think the issue is that some crosses extend outside the board. A cross at (2, 4) covers (1,4), (3,4), (2,3), (2,4), (2,5). All on the board. A cross at (2, 10) covers (1,10), (3,10), (2,9), (2,10), (2,11). (2,11) is on the board (11 columns). ✓. A cross at (9, 3) covers (8,3), (10,3), (9,2), (9,3), (9,4). All on board. ✓.

So all 24 crosses are valid and non-overlapping, covering 120 cells. But the board has 110 cells. This is a contradiction, which means I made an error somewhere.

Let me recheck the Manhattan distance calculation. Take (2, 4) and (3, 3): |2-3| + |4-3| = 1 + 1 = 2 < 3. These overlap!

But according to my calculation: i=2, j=4: j ≡ 2·2 = 4 ≡ 1 mod 3. ✓. i=3, j=3: j ≡ 2·3 = 6 ≡ 0 mod 3. ✓. And |i-i'| = 1, j-j' = 4-3 = 1. But I said |j-j'| ≡ 2 mod 3. Let me recheck: j - j' = 4 - 3 = 1. 1 mod 3 = 1, not 2. 

Where did I go wrong? j ≡ 2i mod 3 and j' ≡ 2i' mod 3. j - j' ≡ 2(i - i') mod 3. If i - i' = 1, then j - j' ≡ 2 mod 3. But j - j' = 1, and 1 ≡ 1 mod 3, not 2. So the congruence doesn't hold?

Wait: j = 4, i = 2. 2i = 4. 4 mod 3 = 1. j = 4, 4 mod 3 = 1. ✓.
j' = 3, i' = 3. 2i' = 6. 6 mod 3 = 0. j' = 3, 3 mod 3 = 0. ✓.
j - j' = 1. 2(i - i') = 2·1 = 2. 2 mod 3 = 2. But j - j' = 1, 1 mod 3 = 1 ≠ 2.

So j - j' ≡ 1 mod 3 but 2(i-i') ≡ 2 mod 3. These should be equal but they're not! The issue is that j ≡ 2i mod 3 means j = 2i + 3k for some integer k, and j' = 2i' + 3k'. So j - j' = 2(i - i') + 3(k - k'). So j - j' ≡ 2(i - i') mod 3. With i - i' = 1: j - j' ≡ 2 mod 3. But j - j' = 1 ≡ 1 mod 3. Contradiction!

So either j ≡ 2i mod 3 is wrong for one of these, or my arithmetic is wrong.

j = 4, i = 2: 2·2 = 4. 4 mod 3 = 1. j mod 3 = 4 mod 3 = 1. ✓.
j' = 3, i' = 3: 2·3 = 6. 6 mod 3 = 0. j' mod 3 = 3 mod 3 = 0. ✓.

j - j' = 1. 2(i - i') = 2(2-3) = -2. -2 mod 3 = 1. Oh! I made an error: i - i' = 2 - 3 = -1, not 1. So 2(i - i') = -2 ≡ 1 mod 3. And j - j' = 1 ≡ 1 mod 3. ✓! They match.

So |i - i'| = 1, and j - j' ≡ 2·(-1) = -2 ≡ 1 mod 3. So |j - j'| ≡ 1 mod 3, meaning |j - j'| ∈ {1, 4, 7, ...}. Minimum 1. Manhattan = 1 + 1 = 2 < 3. ✗!

So my error was in the sign. When |i - i'| = 1, |j - j'| ≡ 1 mod 3 (not 2), so minimum |j - j'| = 1, giving Manhattan distance 2. This doesn't work!

Let me redo the analysis. j ≡ 2i mod 3. For two points (i,j) and (i',j'):
j - j' ≡ 2(i - i') mod 3.

If |i - i'| = 1: |j - j'| ≡ 2 mod 3. So |j - j'| ∈ {2, 5, 8, ...}. Minimum 2. Manhattan = 1 + 2 = 3. ✓.

Wait, but I just showed a counterexample. Let me recheck.

(2, 4) and (3, 3): i = 2, i' = 3. i - i' = -1. j - j' = 4 - 3 = 1. 2(i - i') = -2. -2 mod 3 = 1. j - j' = 1. 1 mod 3 = 1. ✓ (they match). But |j - j'| = 1, and 1 mod 3 = 1, not 2. 

The issue is: j - j' ≡ 2(i - i') mod 3. i - i' = -1. 2(-1) = -2 ≡ 1 mod 3. So j - j' ≡ 1 mod 3. |j - j'| = 1, and 1 ≡ 1 mod 3. ✓.

But I claimed |j - j'| ≡ 2 mod 3 when |i - i'| = 1. The error is that 2(i - i') mod 3 depends on the sign of i - i'. If i - i' = 1, then 2 mod 3 = 2. If i - i' = -1, then -2 mod 3 = 1. So |j - j'| ≡ 1 or 2 mod 3 depending on direction. Since we take absolute value, |j - j'| could be 1 or 2 (mod 3). So the minimum |j - j'| is 1, not 2.

So the pattern j ≡ 2i mod 3 does NOT guarantee Manhattan distance ≥ 3 for adjacent rows. My earlier analysis was wrong.

Let me try j ≡ ci mod 3 for various c and check when it works.

For |i - i'| = 1, we need |j - j'| ≥ 2. j - j' ≡ c(i - i') mod 3. If c = 1: j - j' ≡ ±1 mod 3, so |j - j'| ∈ {1, 4, 7, ...}. Min 1. ✗.
If c = 2: j - j' ≡ ±2 mod 3, so |j - j'| ∈ {2, 5, 8, ...} when i - i' = 1, or |j - j'| ∈ {1, 4, 7, ...} when i - i' = -1. Wait, 2·1 = 2 mod 3 = 2, and 2·(-1) = -2 mod 3 = 1. So depending on direction, |j - j'| ≡ 1 or 2 mod 3. Min could be 1. ✗.

Hmm, so no linear pattern j ≡ ci mod 3 works for adjacent rows? That's because in mod 3, the only nonzero values are 1 and 2, and c · 1 and c · (-1) = -c give c and -c, which are 1 and 2 or 2 and 1. So one direction always gives |j - j'| ≡ 1 mod 3 (min 1).

So a simple mod-3 pattern can't work. We need a more sophisticated approach.

Let me try a mod-5 pattern or a different approach.

Actually, let me try j ≡ 2i mod 5. For |i - i'| = 1: j - j' ≡ 2(i - i') ≡ ±2 mod 5. |j - j'| ∈ {2, 7, 12, ...}. Min 2. Manhattan = 1 + 2 = 3. ✓.
For |i - i'| = 2: j - j' ≡ ±4 mod 5. |j - j'| ∈ {4, 9, ...} or {1, 6, ...}. Wait, 4 mod 5: |j-j'| ∈ {4, 9, ...}. -4 mod 5 = 1: |j-j'| ∈ {1, 6, ...}. So min |j-j'| = 1. Manhattan = 2 + 1 = 3. ✓ (barely).
For |i - i'| = 3: Manhattan ≥ 3. ✓ (regardless of j).
For |i - i'| = 4: j - j' ≡ ±8 ≡ ±3 mod 5. |j-j'| ∈ {3, 8, ...} or {2, 7, ...}. Min 2. Manhattan = 4 + 2 = 6. ✓.

Wait, for |i - i'| = 2, if i - i' = 2: j - j' ≡ 4 mod 5, |j-j'| ∈ {4, 9, ...}, min 4. Manhattan = 2 + 4 = 6. ✓.
If i - i' = -2: j - j' ≡ -4 ≡ 1 mod 5, |j-j'| ∈ {1, 6, ...}, min 1. Manhattan = 2 + 1 = 3. ✓.

So for |i - i'| = 2, the minimum Manhattan distance is 3 (achieved when j - j' ≡ 1 mod 5). This is exactly 3, so it's OK (≥ 3).

So j ≡ 2i mod 5 works! Let me count the points.

For each row i from 2 to 9, j ≡ 2i mod 5, j ∈ {2..10} (9 values).

i=2: 2i=4, j ≡ 4 mod 5. j ∈ {4, 9}. 2 values.
i=3: 2i=6, 6 mod 5 = 1. j ≡ 1 mod 5. j ∈ {6}. Wait, j ∈ {2..10}, j ≡ 1 mod 5: j ∈ {6}. Just 1? Let me check: 1, 6, 11. In {2..10}: only 6. 1 value.

Hmm, that's not many. Let me check all:

i=2: j ≡ 4 mod 5, j ∈ {2..10}: {4, 9}. 2 values.
i=3: j ≡ 1 mod 5, j ∈ {2..10}: {6}. 1 value.
i=4: j ≡ 3 mod 5, j ∈ {2..10}: {3, 8}. 2 values.
i=5: j ≡ 0 mod 5, j ∈ {2..10}: {5, 10}. 2 values.
i=6: j ≡ 2 mod 5, j ∈ {2..10}: {2, 7}. 2 values.
i=7: j ≡ 4 mod 5, j ∈ {2..10}: {4, 9}. 2 values.
i=8: j ≡ 1 mod 5, j ∈ {2..10}: {6}. 1 value.
i=9: j ≡ 3 mod 5, j ∈ {2..10}: {3, 8}. 2 values.

Total: 2+1+2+2+2+2+1+2 = 14.

So 14 crosses with this pattern. Better than 9, but still not 20.

Can I combine multiple mod-5 patterns? If I use j ≡ 2i mod 5 and j ≡ 2i + r mod 5 for some r, I need cross-pattern distances ≥ 3 too.

Two points, one from pattern r=0 and one from r=s: (i, j) with j ≡ 2i mod 5, and (i', j') with j' ≡ 2i' + s mod 5. j - j' ≡ 2(i - i') - s mod 5.

For |i - i'| = 0 (same row): j - j' ≡ -s mod 5. Need |j - j'| ≥ 3. So |s| ≥ 3 mod 5, i.e., s ∈ {3, 2} (since |3| = 3, |2| = 2 < 3). So s = 3 (or -2). Then |j - j'| ≡ 3 mod 5, min |j - j'| = 3. ✓.

For |i - i'| = 1: j - j' ≡ ±2 - s mod 5. Need |j - j'| ≥ 2 (since Manhattan = 1 + |j-j'| ≥ 3). 
If s = 3: j - j' ≡ 2 - 3 = -1 ≡ 4 mod 5, or -2 - 3 = -5 ≡ 0 mod 5. |j - j'| ≡ 4 or 0 mod 5. Min |j-j'| for ≡4: 4. For ≡0: 5 (since j ≠ j' if same row, but different rows could have j = j'). Wait, if j = j', then |j-j'| = 0, Manhattan = 1 + 0 = 1 < 3. ✗!

So when i - i' = -1 (i.e., i' = i + 1), j - j' ≡ -2 - 3 = -5 ≡ 0 mod 5. So j = j' is possible (j - j' = 0 ≡ 0 mod 5). Manhattan = 1 + 0 = 1. ✗.

So s = 3 doesn't work for adjacent rows. Let me try other values of s.

For s = 1: same row, |j - j'| ≡ 1 mod 5, min 1 < 3. ✗.
For s = 2: same row, |j - j'| ≡ 2 mod 5, min 2 < 3. ✗.
For s = 3: same row OK (min 3), but adjacent rows fail (as shown).
For s = 4: same as s = -4 ≡ 1. ✗.

So no two mod-5 patterns can be combined. The maximum with a single mod-5 pattern is 14.

Hmm. Let me think about this differently. Maybe I should not use a lattice pattern at all.

Let me reconsider the problem. We need to place points in {2..9} × {2..10} with pairwise Manhattan distance ≥ 3. The maximum number of such points is what we need, and then we need to check it's ≤ 20 (from the upper bound) and construct 20.

Wait, actually, I realize the upper bound of 20 came from the mod-5 coloring argument. But I should double-check that argument.

The mod-5 coloring: color (i,j) by (i + 2j) mod 5. Each cross covers one cell of each color. The board has 22 cells of each color. With k crosses, we cover k cells of each color, leaving 22 - k of each color uncovered. The 4 corners are always uncovered and have colors 3, 3, 2, 2. For k = 21: 1 of each color uncovered, but corners give 2 of color 2 and 2 of color 3. Contradiction. For k = 20: 2 of each color uncovered, corners give 2 of color 2 and 2 of color 3, leaving 2 more each of colors 0, 1, 4. Total uncovered = 4 + 6 = 10 = 110 - 100. ✓.

So the upper bound is 20. Now I need to construct 20 non-overlapping crosses.

Let me try a different approach to construction. Let me try to use a mix of patterns.

Actually, let me try to think about this more carefully using the (u,v) transformation.

In (u,v) = (i+j, i-j) coordinates, we need L∞ distance ≥ 3. The valid region is the parallelogram with vertices (4,0), (12,-8), (19,-1), (11,7), and only same-parity (u,v) pairs are valid.

The L∞ ≥ 3 constraint means we can place at most one point per 3×3 block. Let me think about how many 3×3 blocks fit in the parallelogram.

The u range is 4 to 19 (16 values), v range is -8 to 7 (16 values). With 3×3 blocks, we can fit ceil(16/3) = 6 blocks in each direction, giving 36 blocks. But many of these blocks are outside the parallelogram.

This is getting complicated. Let me try a direct construction.

Let me try to place crosses row by row, maximizing the count.

Row 2 (i=2): Place crosses at j = 2, 5, 8. These are at distance 3 apart. 3 crosses. These cover cells in rows 1, 2, 3.
Row 3 (i=3): Crosses here would overlap with row 2 crosses (distance 1 in rows). Need |j - j'| ≥ 2 for all j' in {2, 5, 8}. j ∉ {0,1,2,3,4, 3,4,5,6, 6,7,8,9} = {0..9}. j ∈ {10}. 1 cross at (3, 10).

But wait, (3, 10) vs (2, 8): |3-2| + |10-8| = 1 + 2 = 3. ✓. (3, 10) vs (2, 5): 1 + 5 = 6. ✓. (3, 10) vs (2, 2): 1 + 8 = 9. ✓.

Row 4 (i=4): Need distance ≥ 3 from row 2 ({2,5,8}) and row 3 ({10}).
vs row 2 (|i-i'|=2): need |j - j'| ≥ 1. j ∉ {2, 5, 8} (exactly). So j ∈ {3, 4, 6, 7, 9, 10}.
vs row 3 (|i-i'|=1): need |j - 10| ≥ 2. j ∉ {8, 9, 10, 11, 12} ∩ {2..10} = {8, 9, 10}. So j ∈ {2..7}.
Combining: j ∈ {3, 4, 6, 7} (from row 2 constraint) ∩ {2..7} (from row 3 constraint) = {3, 4, 6, 7}.
Within row 4, need pairwise distance ≥ 3. From {3, 4, 6, 7}: {3, 6} or {3, 7} or {4, 7}. Max 2 crosses. Let's pick {3, 7}: distance 4. ✓. Or {3, 6}: distance 3. ✓.

Let me pick row 4: j = 3, 7. But wait, (4, 3) vs (2, 2): |4-2| + |3-2| = 2 + 1 = 3. ✓. (4, 3) vs (2, 5): 2 + 2 = 4. ✓. (4, 7) vs (2, 8): 2 + 1 = 3. ✓. (4, 7) vs (2, 5): 2 + 2 = 4. ✓. (4, 3) vs (3, 10): 1 + 7 = 8. ✓. (4, 7) vs (3, 10): 1 + 3 = 4. ✓. Good.

Row 5 (i=5): vs row 4 ({3,7}, |i-i'|=1): |j-3| ≥ 2 and |j-7| ≥ 2. j ∉ {1..5, 5..9} = {1..9}. j ∈ {10}. 
vs row 3 ({10}, |i-i'|=2): |j-10| ≥ 1. j ≠ 10. But j ∈ {10} from above and j ≠ 10. Contradiction. So 0 crosses in row 5.

Row 6 (i=6): vs row 4 ({3,7}, |i-i'|=2): |j-3| ≥ 1 and |j-7| ≥ 1. j ∉ {3, 7}. j ∈ {2,4,5,6,8,9,10}.
vs row 5: no crosses. 
Within row 6: pairwise ≥ 3. From {2,4,5,6,8,9,10}: best is {2, 5, 8} or {2, 5, 10} or {2, 6, 10} or {4, 8} etc. {2, 5, 8}: distances 3, 3, 6. ✓. 3 crosses.
Check vs row 4: (6, 2) vs (4, 3): 2+1=3 ✓. (6, 5) vs (4, 3): 2+2=4 ✓. (6, 5) vs (4, 7): 2+2=4 ✓. (6, 8) vs (4, 7): 2+1=3 ✓. All good. 3 crosses.

Row 7 (i=7): vs row 6 ({2,5,8}, |i-i'|=1): |j-2|≥2, |j-5|≥2, |j-8|≥2. j ∉ {0..4, 3..7, 6..10} = {0..10}. j ∈ {} (within 2..10). 0 crosses.

Hmm, that's 0. Let me reconsider. Maybe I should choose row 6 differently to leave room for row 7.

Let me try row 6: {2, 6, 10} instead. vs row 4 ({3,7}): (6,2) vs (4,3): 2+1=3 ✓. (6,6) vs (4,7): 2+1=3 ✓. (6,10) vs (4,7): 2+3=5 ✓. (6,6) vs (4,3): 2+3=5 ✓. (6,10) vs (4,3): 2+7=9 ✓. (6,2) vs (4,7): 2+5=7 ✓. All good. 3 crosses.

Row 7: vs row 6 ({2,6,10}, |i-i'|=1): |j-2|≥2, |j-6|≥2, |j-10|≥2. j ∉ {0..4, 4..8, 8..12} = {0..12}. j ∈ {} (within 2..10). 0 crosses.

Still 0. The problem is that 3 crosses in a row spaced 3 apart block the adjacent rows completely.

Let me try 2 crosses in row 6 instead. Row 6: {3, 8}. vs row 4 ({3,7}): (6,3) vs (4,3): 2+0=2 < 3. ✗!

Row 6: {4, 8}. vs row 4 ({3,7}): (6,4) vs (4,3): 2+1=3 ✓. (6,4) vs (4,7): 2+3=5 ✓. (6,8) vs (4,7): 2+1=3 ✓. (6,8) vs (4,3): 2+5=7 ✓. Good. 2 crosses.

Row 7: vs row 6 ({4,8}, |i-i'|=1): |j-4|≥2, |j-8|≥2. j ∉ {2..6, 6..10} = {2..10}. j ∈ {}. 0 crosses.

Still 0. 2 crosses spaced 4 apart also block adjacent rows (since the gap is 4, and we need ≥ 2 from each, leaving no room).

What about 2 crosses spaced 5 apart? Row 6: {2, 7}. vs row 4 ({3,7}): (6,7) vs (4,7): 2+0=2. ✗.

Row 6: {2, 8}. vs row 4 ({3,7}): (6,2) vs (4,3): 2+1=3 ✓. (6,8) vs (4,7): 2+1=3 ✓. (6,2) vs (4,7): 2+5=7 ✓. (6,8) vs (4,3): 2+5=7 ✓. Good. 2 crosses.

Row 7: vs row 6 ({2,8}, |i-i'|=1): |j-2|≥2, |j-8|≥2. j ∉ {0..4, 6..10} = {0..10}. j ∈ {}. 0 crosses.

Hmm, still 0. The problem is that with 2 crosses at distance 6, the "exclusion zones" (±2 in column) cover {0..4} and {6..10}, which is everything.

What if the 2 crosses are closer? Row 6: {4, 7}. Distance 3. vs row 4 ({3,7}): (6,7) vs (4,7): 2+0=2. ✗.

Row 6: {5, 8}. vs row 4 ({3,7}): (6,5) vs (4,3): 2+2=4 ✓. (6,5) vs (4,7): 2+2=4 ✓. (6,8) vs (4,7): 2+1=3 ✓. (6,8) vs (4,3): 2+5=7 ✓. Good. 2 crosses.

Row 7: vs row 6 ({5,8}, |i-i'|=1): |j-5|≥2, |j-8|≥2. j ∉ {3..7, 6..10} = {3..10}. j ∈ {2}. 1 cross at (7, 2).

Check (7, 2) vs (4, 3): 3+1=4 ✓. (7, 2) vs (4, 7): 3+5=8 ✓. (7, 2) vs (5, ...) — no crosses in row 5. (7, 2) vs (6, 5): 1+3=4 ✓. (7, 2) vs (6, 8): 1+6=7 ✓. Good.

Row 8: vs row 7 ({2}, |i-i'|=1): |j-2|≥2. j ∉ {0..4}. j ∈ {5..10}.
vs row 6 ({5,8}, |i-i'|=2): |j-5|≥1, |j-8|≥1. j ∉ {5, 8}. j ∈ {6, 7, 9, 10}.
Combining: j ∈ {5..10} ∩ {6,7,9,10} = {6, 7, 9, 10}.
Within row 8: pairwise ≥ 3. From {6, 7, 9, 10}: {6, 9} or {6, 10} or {7, 10}. Max 2. Pick {6, 10}: distance 4. ✓.

Check (8, 6) vs (7, 2): 1+4=5 ✓. (8, 10) vs (7, 2): 1+8=9 ✓. (8, 6) vs (6, 5): 2+1=3 ✓. (8, 6) vs (6, 8): 2+2=4 ✓. (8, 10) vs (6, 8): 2+2=4 ✓. (8, 10) vs (6, 5): 2+5=7 ✓. Good. 2 crosses.

Row 9: vs row 8 ({6,10}, |i-i'|=1): |j-6|≥2, |j-10|≥2. j ∉ {4..8, 8..12} = {4..12}. j ∈ {2, 3}.
vs row 7 ({2}, |i-i'|=2): |j-2|≥1. j ≠ 2. j ∈ {3}.
1 cross at (9, 3).

Check (9, 3) vs (8, 6): 1+3=4 ✓. (9, 3) vs (8, 10): 1+7=8 ✓. (9, 3) vs (7, 2): 2+1=3 ✓. (9, 3) vs (6, 5): 3+2=5 ✓. (9, 3) vs (6, 8): 3+5=8 ✓. Good.

Now let me also check row 2 vs row 4, and row 3 vs row 5 (which had 0 crosses).

Let me also check if I can add crosses in row 5. Row 5: vs row 4 ({3,7}, |i-i'|=1): |j-3|≥2, |j-7|≥2. j ∉ {1..5, 5..9} = {1..9}. j ∈ {10}. vs row 3 ({10}, |i-i'|=2): |j-10|≥1. j ≠ 10. Contradiction. 0 crosses. ✓ (as before).

vs row 6 ({5,8}, |i-i'|=1): |j-5|≥2, |j-8|≥2. j ∉ {3..7, 6..10} = {3..10}. j ∈ {2}. But also need vs row 4 and row 3 constraints. j=10 from row 4 constraint, j=2 from row 6 constraint. Contradiction. 0.

OK so let me tally up:
Row 2: 3 (j = 2, 5, 8)
Row 3: 1 (j = 10)
Row 4: 2 (j = 3, 7)
Row 5: 0
Row 6: 2 (j = 5, 8)
Row 7: 1 (j = 2)
Row 8: 2 (j = 6, 10)
Row 9: 1 (j = 3)

Total: 3 + 1 + 2 + 0 + 2 + 1 + 2 + 1 = 12. Not great.

Let me try a completely different approach. Let me try to be more systematic.

Actually, let me try the pattern where we use 2 crosses per row for all 8 rows.

Row 2: {2, 6}
Row 3: {4, 8}
Row 4: {2, 6} — but (4, 2) vs (2, 2): 2+0=2 < 3. ✗.

So I can't repeat the same columns in rows 2 apart. Let me use a 3-row cycle:

Row 2: {2, 6}
Row 3: {4, 8}
Row 4: {6, 10} — vs row 2 ({2,6}): (4,6) vs (2,6): 2+0=2. ✗.

Hmm. Let me try:
Row 2: {2, 7}
Row 3: {4, 9}
Row 4: {6} — vs row 2 ({2,7}): (4,6) vs (2,7): 2+1=3 ✓, (4,6) vs (2,2): 2+4=6 ✓. vs row 3 ({4,9}): (4,6) vs (3,4): 1+2=3 ✓, (4,6) vs (3,9): 1+3=4 ✓. Can I add more? {6, 10}: (4,10) vs (3,9): 1+1=2. ✗. {6}: just 1. Or {6, 11}? 11 > 10. No.

Actually wait, can I do {6, 10}? (4,10) vs (2,7): 2+3=5 ✓. (4,10) vs (2,2): 2+8=10 ✓. (4,10) vs (3,9): 1+1=2. ✗. So no.

What about row 4: {6}? Or {5, 10}? (4,5) vs (3,4): 1+1=2. ✗. {7}? (4,7) vs (3,9): 1+2=3 ✓. (4,7) vs (3,4): 1+3=4 ✓. (4,7) vs (2,7): 2+0=2. ✗.

{8}? (4,8) vs (3,9): 1+1=2. ✗. {6, 10} doesn't work. {6} only.

Hmm, this is getting tedious. Let me try a different strategy.

Let me try to think about what the theoretical maximum is for the independent set (Manhattan distance ≥ 3) in the 8×9 grid, and whether 20 is achievable.

Actually, let me reconsider. The upper bound of 20 came from the coloring argument. But maybe the actual maximum of the independent set is less than 20, and the answer is less than 20. But the problem asks for the maximum number of non-overlapping crosses, which equals the maximum independent set (since non-overlapping = Manhattan distance ≥ 3 between centers, and all centers must be valid).

Wait, actually, I need to be more careful. Non-overlapping crosses means the 5-cell sets don't intersect. Two crosses at Manhattan distance exactly 2 share a cell. At distance 1, they share cells. At distance 0, same cross. At distance ≥ 3, no shared cells. So non-overlapping ⟺ Manhattan distance ≥ 3. ✓.

So the answer is the maximum independent set in the graph on {2..9}×{2..10} where edges connect points at Manhattan distance ≤ 2.

Let me try to compute this more carefully. Let me try a different construction.

Let me try a "staircase" pattern. Place crosses at:
(2,2), (2,5), (2,8) — row 2, 3 crosses
(4,3), (4,6), (4,9) — row 4, 3 crosses (check vs row 2: (4,3) vs (2,2): 2+1=3 ✓, (4,3) vs (2,5): 2+2=4 ✓, (4,6) vs (2,5): 2+1=3 ✓, (4,6) vs (2,8): 2+2=4 ✓, (4,9) vs (2,8): 2+1=3 ✓. All good.)
(6,2), (6,5), (6,8) — row 6, 3 crosses (check vs row 4: (6,2) vs (4,3): 2+1=3 ✓, (6,5) vs (4,3): 2+2=4 ✓, (6,5) vs (4,6): 2+1=3 ✓, (6,8) vs (4,6): 2+2=4 ✓, (6,8) vs (4,9): 2+1=3 ✓. All good.)
(8,3), (8,6), (8,9) — row 8, 3 crosses (check vs row 6: (8,3) vs (6,2): 2+1=3 ✓, (8,3) vs (6,5): 2+2=4 ✓, (8,6) vs (6,5): 2+1=3 ✓, (8,6) vs (6,8): 2+2=4 ✓, (8,9) vs (6,8): 2+1=3 ✓. All good.)

Total: 12 crosses. Same as before. Can I add more in the odd rows?

Row 3: vs row 2 ({2,5,8}, |i-i'|=1): |j-2|≥2, |j-5|≥2, |j-8|≥2. j ∉ {0..4, 3..7, 6..10} = {0..10}. j ∈ {}. 0 crosses.
Row 5: vs row 4 ({3,6,9}, |i-i'|=1): |j-3|≥2, |j-6|≥2, |j-9|≥2. j ∉ {1..5, 4..8, 7..11} = {1..11}. j ∈ {}. 0 crosses.
Row 7: vs row 6 ({2,5,8}, |i-i'|=1): same as row 3. 0 crosses.
Row 9: vs row 8 ({3,6,9}, |i-i'|=1): same as row 5. 0 crosses.

So 12 is all we get with this pattern. The 3-per-even-row pattern blocks all odd rows.

Let me try 2 per row with a clever pattern that allows all 8 rows.

The key constraint: for rows differing by 1, columns must differ by ≥ 2. For rows differing by 2, columns must differ by ≥ 1.

Let me use a 4-row repeating pattern: A, B, C, D where:
- A and C differ by ≥ 1 in each column (rows 2 apart)
- B and D differ by ≥ 1 in each column (rows 2 apart)  
- A and B differ by ≥ 2 in each column (adjacent)
- B and C differ by ≥ 2 in each column (adjacent)
- C and D differ by ≥ 2 in each column (adjacent)
- A and D: rows differ by 3, no constraint.

Let me try:
A (row 2): {2, 7}
B (row 3): {4, 9} — vs A: |2-4|=2 ✓, |2-9|=7 ✓, |7-4|=3 ✓, |7-9|=2 ✓. All ≥ 2. ✓.
C (row 4): {6} — vs B: |6-4|=2 ✓, |6-9|=3 ✓. vs A: |
