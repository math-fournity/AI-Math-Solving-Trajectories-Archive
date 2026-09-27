# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   One hundred and one of the squares of an $n\times n$ table are colored blue. It is known that there exists a unique way to cut the table to rectangles along boundaries of its squares with the following property: every rectangle contains exactly one blue square. Find the smallest possible $n$.       — 题目文本
#   1. **Initial Setup and Assumption:**
   - We are given an \( n \times n \) table with 101 blue squares.
   - There exists a unique way to cut the table into rectangles such that each rectangle contains exactly one blue square.
   - We need to find the smallest possible \( n \).

2. **Verification for \( n = 101 \):**
   - Consider a \( 101 \times 101 \) table.
   - Color the top row entirely blue, resulting in 101 blue squares.
   - This configuration ensures that each row and column has at most one blue square, making it possible to partition the table uniquely into \( 1 \times 101 \) rectangles, each containing exactly one blue square.

3. **Lemma 1:**
   - **Statement:** For a blue square and its non-blue neighbor, there exists a way to cut the table into rectangles which partitions these two squares into the same rectangle.
   - **Proof:**
     - Assume the blue square and its non-blue neighbor are in the same row (otherwise, rotate the board by 90 degrees).
     - Partition the non-fallow rows (rows with blue squares) into \( 1 \times k \) rectangles, each containing exactly one blue square.
     - Ensure the two squares (blue and non-blue neighbor) are in the same rectangle.
     - Collapse the fallow rows (rows without blue squares) into the existing rectangles by adding each square in a fallow row to the first rectangle below it (or above it if there are none below).
     - This ensures a unique partitioning, proving the lemma. \(\blacksquare\)

4. **Corollary:**
   - **Statement:** The set of blue squares in any row is contiguous.
   - **Proof:**
     - If not, we could partition that row into \( 1 \times k \) rectangles in more than one way.
     - Proceeding as described in Lemma 1 would result in at least two possible ways to partition the grid, contradicting the uniqueness of the partitioning. \(\blacksquare\)
   - A similar statement holds for columns.

5. **Lemma 2:**
   - **Statement:** Any non-blue square \( s \) cannot have two blue neighbors.
   - **Proof:**
     - By the corollary, we only need to prove this when the two blue neighbors are not in the same row or column.
     - Let \( n_1 \) be the blue neighbor in the same row and \( n_2 \) be the blue neighbor in the same column.
     - Use the algorithm described in Lemma 1 to get a partition with \( n_1, s \) in the same rectangle but not \( n_2 \), and another with \( n_2, s \) in the same rectangle but not \( n_1 \).
     - This results in a contradiction, proving the lemma. \(\blacksquare\)

6. **Lemma 3:**
   - **Statement:** If \( a, b \) are blue squares which aren't in the same row or the same column, then the rectangle with \( a, b \) as opposite corners is entirely blue.
   - **Proof:**
     - Assume \( a \) is lower than \( b \) and to the left of \( b \).
     - Consider the path \( a, s_1, s_2, \ldots, s_k, b \) which first goes up and then to the right, moving one step each time.
     - Let \( s_t \) be the turning point, i.e., \( s_t \) is above \( s_{t-1} \) and to the left of \( s_{t+1} \).
     - If any \( s_i \) is not blue, then \( s_t \) is not blue by the corollary.
     - Suppose \( s_t \) is not blue. Let \( 0 \le i < t \) be the largest \( i \) with \( s_i \) blue, where \( s_0 = a \) by convention.
     - Let \( t < j \le k+1 \) be the smallest \( j \) with \( s_j \) blue, where \( s_{k+1} = b \) by convention.
     - Apply the algorithm in Lemma 1 to get a partitioning where \( s_i, s_t \) are in the same rectangle but not \( s_j \), and another where \( s_j, s_t \) are in the same rectangle but not \( s_i \).
     - These give a contradiction, so all \( s_i \)'s are blue.
     - Using Lemma 2, we can prove that the entire rectangle is blue. \(\blacksquare\)

7. **Conclusion:**
   - Lemma 3 implies that the set of blue squares forms a rectangle.
   - The set of blue squares must be a \( 1 \times 101 \) rectangle, which implies \( n \ge 101 \).

Hence, the desired minimum value of \( n \) is \( \boxed{101} \).  — 标准解答
#   Let me analyze this problem carefully.

We have an $n \times n$ table with 101 squares colored blue. There exists a unique way to cut the table into rectangles along grid boundaries such that every rectangle contains exactly one blue square. Find the smallest possible $n$.

First, let me understand the problem. We need to partition the $n \times n$ grid into rectangles (with sides along grid lines) such that each rectangle contains exactly one blue cell. The partition must be unique. We want to find the smallest $n$ for which this is possible with 101 blue cells.

Let me think about what makes a partition unique.

A partition into rectangles where each rectangle has exactly one blue cell is called a "rectangular partition" or "guillotine-free rectangular partition" with the constraint.

Let me think about when such a partition is unique.

Key insight: Consider two adjacent blue cells. If they're in the same row with no other blue cells between them, and they're adjacent (horizontally), then we need to decide where to cut between them. Actually, let me think more carefully.

Let me think about this differently. Consider the partition problem. We need to cut the grid into rectangles, each containing exactly one blue cell. 

For uniqueness, let me think about what configurations force a unique partition.

Consider a row of the grid. If a row contains blue cells, the cuts in that row are constrained.

Let me think about a simpler version first. 

Actually, let me think about the structure. A partition of the grid into rectangles where each rectangle has exactly one blue cell. 

Consider two blue cells that are in the same row, say at positions (r, c1) and (r, c2) with c1 < c2. There must be a vertical cut between them somewhere. But also, the rectangles containing them might extend across multiple rows.

Let me think about when the partition is forced to be unique.

Key observation: If we have a blue cell at position (r, c), and we look at its "territory" - the rectangle containing it. The rectangle is bounded by cuts (grid lines) on all four sides.

For the partition to be unique, every cut must be forced.

Let me think about a specific construction. 

Consider placing blue cells such that the partition is forced. One natural idea: place blue cells in a "staircase" or "diagonal" pattern.

Actually, let me think about this more carefully using the concept of "forced cuts."

A cut between two adjacent cells (i,j) and (i,j+1) (a vertical cut) is forced if the blue cells on the left and right must be separated. Similarly for horizontal cuts.

Let me think about the problem in terms of a graph. Consider the grid graph. We need to partition it into rectangles, each containing exactly one blue cell. 

Actually, I think the key insight is about "dominance" and the structure of forced partitions.

Let me think about a 1D version first: a 1×n strip with k blue cells. The partition into intervals each containing one blue cell is unique if and only if... well, actually in 1D, if we have k blue cells at positions p1 < p2 < ... < pk in a 1×n strip, the partition into intervals is unique: the cut between pi and pi+1 must be at some position between pi and pi+1. But wait, there could be multiple positions. So the partition is unique only if every pair of consecutive blue cells is adjacent (pi+1 = pi + 1), in which case the cut is forced to be between them. But also the ends: the first interval starts at position 1 and the last ends at position n. Actually no—in 1D, the cuts between consecutive blue cells can be at any position between them, so uniqueness requires consecutive blue cells to be adjacent.

Wait, but that's for 1D. In 2D, the situation is more complex because rectangles can be 2D.

Let me reconsider. In 2D, the partition into rectangles is more flexible. 

Let me think about what makes a 2D rectangular partition unique.

Consider a configuration where blue cells are placed on the main diagonal: (1,1), (2,2), ..., (n,n) in an n×n grid. Is the partition unique? Each blue cell (i,i) needs its own rectangle. 

For the diagonal configuration, consider cells (i,i) and (i+1,i+1). The cell (i,i+1) is between them. It could go to either rectangle. So the partition is not unique in general.

Hmm, let me think differently.

Let me think about the problem from the perspective of the answer. We need 101 blue cells and the smallest n. 

101 is a specific number. Let me think about what configurations give unique partitions.

Key idea: A configuration where the partition is forced. 

Consider a "staircase" of blue cells. Place blue cells at positions:
(1,1), (1,2), ..., (1, a1), 
(2, a1), (2, a1+1), ..., (2, a2),
...

Hmm, this is getting complicated. Let me think about it differently.

Let me think about the concept of a "Mondrian partition" or more specifically, when is a rectangular partition unique?

A rectangular partition of a grid into rectangles is determined by the set of cuts (horizontal and vertical line segments along grid lines). 

For the partition to be unique with the constraint that each rectangle has exactly one blue cell, every cut must be forced.

Let me think about a specific type of configuration. Consider blue cells placed such that they form a "tree" structure or a specific pattern.

Actually, let me think about this problem from a competition perspective. This is likely a competition problem, and the answer is probably a specific number.

Let me think about the structure more carefully.

Consider a configuration where we have blue cells arranged in a specific pattern that forces a unique partition.

Key insight: Consider a 2×2 block. If we have two blue cells in a 2×2 block, say at (1,1) and (2,2), then we can partition in two ways: either cut vertically (giving rectangles {(1,1),(1,2)} and {(2,1),(2,2)}) or cut horizontally (giving rectangles {(1,1),(2,1)} and {(1,2),(2,2)}). Both give each rectangle one blue cell. So this is not unique.

If we have blue cells at (1,1) and (1,2) in a 1×2 or 2×2 block, then we must cut vertically between them, and this is forced.

If we have blue cells at (1,1) and (2,1), we must cut horizontally, forced.

So for uniqueness, we need to avoid "diagonal" configurations of blue cells that allow multiple partitions.

Now, let me think about a larger structure. 

Consider placing blue cells in a "comb" pattern. For instance, in a row, place blue cells at every other position. But then the cuts between them are not forced (there's a gap).

Wait, I think I need to think about this more carefully.

Let me consider the following: a partition into rectangles is unique if and only if there's no "alternating cycle" or some similar obstruction.

Actually, let me think about it from the perspective of the dual. 

Hmm, let me try a different approach. Let me think about specific constructions and count.

Construction 1: All blue cells in a single row. Say row 1, columns 1 through 101. Then n must be at least 101 (since we need 101 columns). But wait, n×n with n ≥ 101. In this case, the partition: each blue cell (1, j) for j=1,...,101 needs its own rectangle. The cells in rows 2 through n need to be assigned to some rectangle. 

If all blue cells are in row 1, then each rectangle must extend downward. The vertical cuts between consecutive blue cells are forced (they're adjacent, so the cut is between column j and j+1). But the horizontal extent: each rectangle is a column strip from row 1 to row n, containing one blue cell. But wait, what about columns beyond 101? If n > 101, there are columns 102 through n with no blue cells. Those cells need to be part of some rectangle, but every rectangle must have exactly one blue cell. So the cells in columns 102 through n can't form valid rectangles (no blue cell). So we need n = 101 and all cells in the grid are in columns 1-101. But then each rectangle is a column of height n = 101, containing one blue cell at row 1. Is this unique? 

The vertical cuts are forced (between adjacent blue cells). The left and right boundaries are the grid edges. The top and bottom are grid edges. So yes, each rectangle is a full column, and this is unique. But n = 101 and we use 101 blue cells in a single row. This gives n = 101.

But can we do better? Can we use a 2D arrangement to get a smaller n?

Construction 2: Use multiple rows. If we use 2 rows, we can fit more blue cells per column-width. But we need to ensure uniqueness.

Let me think about a 2-row arrangement. Say we have blue cells in rows 1 and 2. Consider columns where row 1 has a blue cell and columns where row 2 has a blue cell. 

If column j has a blue cell in row 1 only, and column j+1 has a blue cell in row 2 only, then we have a diagonal situation, which creates ambiguity.

So for uniqueness, we need to avoid such diagonal configurations. 

One way: in each column, either both rows have blue cells, or neither. If both rows of a column have blue cells, we cut horizontally between rows 1 and 2, giving two 1×1 rectangles (if the column is isolated) or two 1×k rectangles.

Wait, but if both cells in a column are blue, we need a horizontal cut between them. Then each gets its own rectangle. The rectangle for (1,j) extends left/right until it hits a vertical cut, and the rectangle for (2,j) extends left/right until it hits a vertical cut. But the vertical cuts for row 1 and row 2 might be different!

Hmm, this is getting complicated. Let me think about it differently.

If we have a 2×n grid with blue cells at (1,j) and (2,j) for j = 1, ..., k (so 2k blue cells), and we need n ≥ k. The horizontal cut between rows 1 and 2 is forced (each rectangle needs exactly one blue cell, and if a rectangle spans both rows in a column with two blue cells, it would have 2 blue cells). Wait, not necessarily—a rectangle spanning both rows might span multiple columns and have blue cells in both rows.

Let me reconsider. If we have blue cells at (1,1), (1,2), (2,1), (2,2) in a 2×2 grid, we need to partition into 4 rectangles each with one blue cell. The only way is to cut both horizontally and vertically, giving 4 1×1 rectangles. This is unique.

If we have blue cells at (1,1), (1,2), (2,1), (2,2) in a 2×3 grid (extra column 3 with no blue cells), we need the cells in column 3 to be part of some rectangle. But every rectangle needs exactly one blue cell. So (1,3) must be in a rectangle with exactly one blue cell. It could join the rectangle of (1,2) (extending it to the right) or (2,2)'s rectangle (but that would require the rectangle to span both rows, which would include (1,2) too if it also spans... no, a rectangle is contiguous). 

Actually, (1,3) could be in the rectangle containing (1,2), extending it to a 1×2 rectangle covering (1,2) and (1,3). Similarly, (2,3) could be in the rectangle containing (2,2). But also, (1,3) and (2,3) could form a 2×1 rectangle—but that has no blue cell, which is invalid. So (1,3) must join some rectangle with a blue cell, and (2,3) must join some rectangle with a blue cell. The only options are: (1,3) joins (1,2)'s rectangle, (2,3) joins (2,2)'s rectangle. Or... could (1,3) join (2,2)'s rectangle? That would require a rectangle covering (1,3) and (2,2), which would be the 2×2 block (1,2),(1,3),(2,2),(2,3), containing 2 blue cells. Invalid. So the only option is (1,3) joins (1,2) and (2,3) joins (2,2). This is forced, so unique.

OK so this seems to work. The partition is: cut horizontally between rows 1 and 2, cut vertically between columns 1 and 2, and columns 2-3 are together (no vertical cut between 2 and 3). So rectangles are: {(1,1)}, {(2,1)}, {(1,2),(1,3)}, {(2,2),(2,3)}. Each has one blue cell. Unique.

But wait, could we also cut vertically between columns 2 and 3? Then we'd have rectangles: {(1,1)}, {(2,1)}, {(1,2)}, {(2,2)}, and then (1,3) and (2,3) form a 2×1 rectangle with no blue cell. Invalid. So no, we can't cut there. The partition is unique.

Now, what if we have a 2×n grid with blue cells at (1,j) and (2,j) for j=1,...,k, and n > k? The cells in columns k+1 through n must be assigned. By the same logic, (1, k+1) must join (1, k)'s rectangle, (2, k+1) must join (2, k)'s rectangle, and so on. So the partition is unique: horizontal cut between rows, vertical cuts between columns 1-2, 2-3, ..., (k-1)-k, and no cuts beyond column k. Each rectangle in column j (for j < k) is 1×1, and column k's rectangles extend to the right edge.

But this uses 2k blue cells in a 2×n grid with n ≥ k. To get 101 blue cells, we need 2k = 101, but 101 is odd. So we can't use exactly 2k = 101 with this symmetric pattern.

Let me think about asymmetric patterns. 

What if we use a pattern where some columns have 2 blue cells and some have 1?

Consider a 2×n grid. In some columns, both cells are blue; in some, only one is blue; in some, neither.

For uniqueness, we need to be careful about columns with only one blue cell.

If column j has a blue cell only in row 1 (not row 2), and column j+1 has a blue cell only in row 2 (not row 1), we get a diagonal configuration that might create ambiguity.

Let me think about this. Say we have a 2×2 grid with blue at (1,1) and (2,2). As I noted, this has two valid partitions (vertical cut or horizontal cut). Not unique.

So we need to avoid having a column with blue only in row 1 adjacent to a column with blue only in row 2.

What if all single-blue columns have the blue in the same row? Say columns 1 through a have blue in row 1 only, and columns a+1 through b have blue in both rows, and columns b+1 through c have blue in row 1 only. Wait, but then between the "both" section and the "row 1 only" section, we might have issues.

Hmm, let me think about this more carefully.

Actually, let me think about a cleaner approach. Let me consider the problem as follows:

We want to find a configuration of 101 blue cells in an n×n grid such that the rectangular partition (each rectangle has exactly one blue cell) is unique, and n is minimized.

Let me think about what constraints uniqueness imposes.

Claim: The partition is unique if and only if there is no "alternating rectangle" — a 2×2 subgrid where the blue cells are at opposite corners (a "checkerboard" pattern), and additionally, the partition is "locally forced" everywhere.

Actually, I think the condition for uniqueness is more subtle. Let me think about it in terms of the structure of the partition.

A rectangular partition is determined by its cuts. A cut is a horizontal or vertical segment along a grid line that separates two rectangles. 

For the partition to be unique, every cut must be "forced" — meaning that without it, some rectangle would contain 0 or ≥2 blue cells.

Let me think about necessary conditions for a cut to be forced.

A vertical cut between columns j and j+1, spanning rows r1 to r2, is forced if removing it would cause some rectangle to have 0 or ≥2 blue cells. 

This is getting complex. Let me try to think about the problem from the answer's perspective.

We need 101 blue cells. 101 = 10² + 1 = 10*10 + 1. Or 101 is prime. 

Hmm, let me think about what n could be. If we use a single row, n = 101. If we use 2 rows, we might get n ≈ 51. If we use k rows, we might get n ≈ 101/k + something.

But the constraint is that the partition must be unique, which limits how we can arrange blue cells.

Let me think about a "staircase" construction.

Consider placing blue cells in a staircase pattern. For example:
- Row 1: columns 1, 2, ..., a1
- Row 2: columns a1, a1+1, ..., a2
- Row 3: columns a2, a2+1, ..., a3
- ...

Where each row shares one column with the next (the "turn" column has blue cells in two adjacent rows).

Wait, but if a column has blue cells in two adjacent rows, we need a horizontal cut between them, which is fine.

Let me think about a specific staircase. Consider an L-shaped arrangement:
- Row 1: columns 1 through a (a blue cells)
- Column a: rows 1 through b (b blue cells, but (1,a) is shared, so a + b - 1 blue cells)

This gives a + b - 1 blue cells in a grid that's max(a, b) × max(a, b) roughly. But actually the grid is b × a (b rows, a columns), and we need it to be n × n, so n = max(a, b).

Hmm wait, but we need to check uniqueness.

Let me consider a specific example: blue cells at (1,1), (1,2), (1,3), (2,3), (3,3) in a 3×3 grid. That's 5 blue cells. Is the partition unique?

The blue cells are in an L-shape. Let me figure out the partition.

Row 1 has blue at columns 1, 2, 3. Column 3 has blue at rows 1, 2, 3.

Cell (1,1): needs a rectangle with only this blue cell. 
Cell (1,2): needs a rectangle with only this blue cell.
Cell (1,3): needs a rectangle with only this blue cell.
Cell (2,3): needs a rectangle with only this blue cell.
Cell (3,3): needs a rectangle with only this blue cell.

Non-blue cells: (2,1), (2,2), (3,1), (3,2).

(2,1) must be in a rectangle with exactly one blue cell. The only blue cell it could be with is (1,1) (if the rectangle spans rows 1-2, column 1). So (2,1) joins (1,1)'s rectangle: rectangle is {(1,1), (2,1)}.

(2,2) must be in a rectangle with exactly one blue cell. Options: join (1,2)'s rectangle (spanning rows 1-2, column 2), or join (1,1)'s rectangle (but that already has (1,1) and (2,1), so adding (2,2) would make it a 2×2 rectangle with 1 blue cell... wait, (1,1) is blue, so a 2×2 rectangle {(1,1),(1,2),(2,1),(2,2)} has 2 blue cells. Invalid. So (2,2) can join (1,2)'s rectangle: {(1,2), (2,2)}. Or could (2,2) join (2,3)'s rectangle? That would be {(2,2), (2,3)}, a 1×2 rectangle with 1 blue cell (2,3). Valid! So there are two options for (2,2).

Hmm, so the partition might not be unique. Let me check.

Option A: (2,2) joins (1,2). Rectangles so far: {(1,1),(2,1)}, {(1,2),(2,2)}, {(1,3)}, {(2,3)}, {(3,3)}.
Then (3,1) and (3,2) need rectangles. (3,1) could join {(1,1),(2,1)} extending to row 3: {(1,1),(2,1),(3,1)} - 1 blue cell. Valid. (3,2) could join {(1,2),(2,2)} extending to row 3: {(1,2),(2,2),(3,2)} - 1 blue cell. Valid. 
So partition: {(1,1),(2,1),(3,1)}, {(1,2),(2,2),(3,2)}, {(1,3)}, {(2,3)}, {(3,3)}. Each has 1 blue cell. Valid.

Option B: (2,2) joins (2,3). Rectangles: {(1,1),(2,1)}, {(1,2)}, {(1,3)}, {(2,2),(2,3)}, {(3,3)}.
Then (3,1) joins {(1,1),(2,1)} → {(1,1),(2,1),(3,1)}. (3,2) needs a rectangle. Could join {(2,2),(2,3)} extending to row 3: {(2,2),(2,3),(3,2),(3,3)} - 2 blue cells. Invalid. Could join {(1,2)} extending to row 3: {(1,2),(2,2),(3,2)} - but (2,2) is already in {(2,2),(2,3)}. Conflict. 

Hmm wait, I need to be more careful. In option B, (2,2) is in the rectangle {(2,2),(2,3)}. So (3,2) can't join (1,2)'s rectangle by going through (2,2) (since (2,2) is taken). (3,2) could form a rectangle with (3,1) and (3,3)? (3,1) is in {(1,1),(2,1),(3,1)}. So (3,2) is isolated. It could be a 1×1 rectangle, but that has 0 blue cells. Invalid. 

So (3,2) must join some rectangle with a blue cell. The adjacent rectangles are: {(1,1),(2,1),(3,1)} (has blue at (1,1)), {(2,2),(2,3)} (has blue at (2,3)), {(3,3)} (has blue at (3,3)). 

(3,2) joining {(3,3)}: rectangle {(3,2),(3,3)} - 1 blue cell. Valid!
(3,2) joining {(1,1),(2,1),(3,1)}: would need rectangle covering (3,1) and (3,2), so at least row 3, columns 1-2. But (2,1) is in this rectangle, so the rectangle is at least rows 1-3, columns 1-2 = {(1,1),(1,2),(2,1),(2,2),(3,1),(3,2)}. But (1,2) is blue and in a different rectangle, and (2,2) is in {(2,2),(2,3)}. Conflict.

So in option B, (3,2) joins {(3,3)}: rectangle {(3,2),(3,3)}. Then partition: {(1,1),(2,1),(3,1)}, {(1,2)}, {(1,3)}, {(2,2),(2,3)}, {(3,2),(3,3)}. Each has 1 blue cell. Valid!

So we have at least two valid partitions (option A and option B). The L-shape doesn't give uniqueness.

OK so the staircase/L-shape doesn't work directly. Let me think about what does work.

Going back to the "full columns" idea: if every column that has blue cells has blue cells in all rows (of the relevant subgrid), then the horizontal cuts are forced and we just need vertical cuts, which are forced if blue cells are adjacent.

But that uses n² blue cells for an n×n grid, which is too many.

Let me think about a different approach. What if we use a "comb" pattern?

Consider a grid where we have some columns fully filled with blue cells and some columns empty. But empty columns can't exist (their cells need to join a rectangle with a blue cell).

Hmm, let me reconsider. The key issue is: how to arrange blue cells in 2D to minimize n while maintaining uniqueness.

Let me think about the problem differently. 

Consider the grid as a graph where we need to find a unique rectangular partition. 

I think the key insight is about "separating" blue cells. Two blue cells need to be separated by a cut. A cut is forced if there's no alternative.

Let me think about a "path" of blue cells. Consider blue cells arranged in a path (each consecutive pair is adjacent). For example, a snake-like path through the grid. 

If blue cells form a path where each consecutive pair is adjacent (horizontally or vertically), then between each consecutive pair, there must be a cut. But is the partition unique?

Consider a path: (1,1), (1,2), (2,2), (2,3), (3,3), ... This is a staircase path. Between (1,1) and (1,2), there's a vertical cut. Between (1,2) and (2,2), there's a horizontal cut. Etc.

But the issue is that the non-blue cells need to be assigned, and there might be multiple ways.

Let me think about a Hamiltonian path of blue cells. If all n² cells are blue, then each rectangle is 1×1, and the partition is trivially unique. But we need exactly 101 blue cells, not n².

Let me think about the problem from the competition answer perspective. 

For 101 blue cells, we want the smallest n. 

I think the answer might be related to the following construction: arrange blue cells in a "cross" or "T" or some specific shape.

Actually, let me think about this more carefully. Let me consider the problem of when a rectangular partition is unique.

Theorem (informal): A rectangular partition of a grid into rectangles each containing exactly one blue cell is unique if and only if there is no "alternating cycle" in the "conflict graph."

Actually, I think the right framework is this: Consider the grid graph. Two adjacent cells (sharing an edge) are "separated" if there's a cut between them. We need to determine which edges of the grid graph are cuts. 

A valid partition is a set of cuts (edges of the grid graph to remove) such that:
1. The resulting regions are all rectangles.
2. Each region contains exactly one blue cell.

For uniqueness, there should be exactly one such set of cuts.

Now, an edge between cells (i,j) and (i,j+1) must be a cut if they're in different "blue regions." An edge must NOT be a cut if cutting it would create a non-rectangle or if the two cells are in the same blue region.

Let me think about necessary conditions. If two blue cells are in the same row with no blue cell between them, and they're not adjacent, then the cut between them can be at any position between them. So for uniqueness, either they're adjacent (cut is forced at one specific position) or there's some other constraint.

Wait, actually, that's not quite right either, because the rectangles might not be single rows.

Let me think about a cleaner characterization.

I think the key insight is:

Lemma: If two blue cells are "visible" to each other (in the same row or column with no other blue cell between them), and they are not adjacent, then the partition is not unique.

Proof: If blue cells A and B are in the same row with no blue cell between them, and they're not adjacent, then there's at least one non-blue cell between them. The cut separating A's rectangle from B's rectangle can be placed at any of the positions between A and B. But wait, the cut might not be a simple vertical line—it could be more complex if the rectangles aren't single-row rectangles.

Hmm, actually this isn't quite right because the rectangles could span multiple rows.

Let me think about a specific case. Blue cells at (1,1) and (1,3) in a 1×3 grid. The cell (1,2) must be in one of the two rectangles. Either {(1,1),(1,2)} and {(1,3)}, or {(1,1)} and {(1,2),(1,3)}. Both valid, so not unique. ✓

Blue cells at (1,1) and (1,3) in a 2×3 grid. Cells (1,2), (2,1), (2,2), (2,3) are non-blue. 
- (1,2) can join (1,1) or (1,3).
- (2,1) can join (1,1).
- (2,3) can join (1,3).
- (2,2) can join (1,1) (via (2,1)) or (1,3) (via (2,3)) or (1,2) (but (1,2) is not blue).

Actually, (2,2) must be in a rectangle with exactly one blue cell. The rectangle containing (2,2) must also contain a blue cell. The blue cells are (1,1) and (1,3). A rectangle containing (2,2) and (1,1) would need to cover at least rows 1-2 and columns 1-2, i.e., {(1,1),(1,2),(2,1),(2,2)}. This has 1 blue cell. Valid. A rectangle containing (2,2) and (1,3) would need to cover at least rows 1-2 and columns 2-3, i.e., {(1,2),(1,3),(2,2),(2,3)}. This has 1 blue cell. Valid.

So (2,2) can go with either (1,1) or (1,3). Not unique. ✓

So the lemma seems to hold: if two blue cells are visible to each other (same row or column, no blue cell between) and not adjacent, the partition is not unique.

Wait, but I should check: is the converse true? If every pair of blue cells that are visible to each other are adjacent, is the partition unique?

This would mean: in each row, the blue cells form a contiguous block (since any two in the same row must be adjacent, by induction they form a contiguous block). Similarly for each column.

Wait, that's not quite right. "Visible" means same row/column with no other blue cell between. If blue cells in a row are at positions 1, 2, 4, then 2 and 4 are visible (no blue cell at position 3) and not adjacent. So this violates the condition. So the condition requires that in each row, blue cells form a contiguous block. Similarly for each column.

So the condition is: in every row, the blue cells form a contiguous interval, and in every column, the blue cells form a contiguous interval.

Is this sufficient for uniqueness? Let me check.

Consider blue cells at (1,1), (1,2), (2,1), (2,2) in a 2×2 grid. Each row has a contiguous block, each column has a contiguous block. The partition: cut horizontally and vertically, giving 4 1×1 rectangles. Is this unique? 

Could we have a different partition? The only other option would be to not cut somewhere. If we don't cut horizontally, then rows 1 and 2 are together, and we'd have a 2×1 or 2×2 rectangle with 2 blue cells. Invalid. If we don't cut vertically, similar issue. So yes, unique. ✓

Consider blue cells at (1,1), (1,2), (2,2), (2,3) in a 2×3 grid. Row 1: blue at 1,2 (contiguous). Row 2: blue at 2,3 (contiguous). Column 1: blue at 1 only. Column 2: blue at 1,2 (contiguous). Column 3: blue at 2 only. So the condition is satisfied.

Is the partition unique? Blue cells: (1,1), (1,2), (2,2), (2,3). Non-blue: (2,1), (1,3).

(2,1) must join a rectangle with a blue cell. Adjacent blue cell: (1,1). Rectangle {(1,1),(2,1)}: 1 blue cell. Could (2,1) join (1,2)? Rectangle would be at least {(1,1),(1,2),(2,1),(2,2)}: 2 blue cells. Invalid. Could (2,1) join (2,2)? Rectangle {(2,1),(2,2)}: 1 blue cell. Valid! So (2,1) has two options.

So the partition is NOT unique, even though the contiguity condition is satisfied. So the contiguity condition is necessary but not sufficient.

Hmm. So my lemma gives a necessary condition but not a sufficient one.

Let me reconsider. The issue in the above example is that (2,1) can join either (1,1) or (2,2). This is because (1,1) and (2,2) are at "opposite corners" of a 2×2 block, creating ambiguity.

So the condition for uniqueness is stronger. Let me think about what the right condition is.

I think the right condition involves the concept of a "grid intersection graph" or something similar.

Let me think about it differently. Consider the "row intervals" and "column intervals" of blue cells. 

In the example above: Row 1 has blue in columns [1,2]. Row 2 has blue in columns [2,3]. Column 1 has blue in rows [1,1]. Column 2 has blue in rows [1,2]. Column 3 has blue in rows [2,2].

The issue is that row 1's interval [1,2] and row 2's interval [2,3] overlap at column 2 but are "shifted." This creates the diagonal ambiguity.

For uniqueness, I think we need that the row intervals are "nested" or "non-overlapping" in a specific way.

Actually, let me think about this problem from a different angle. Let me consider the concept of a "staircase" partition.

A staircase partition is one where the rectangles form a staircase pattern. 

Hmm, let me try to think about what configurations give unique partitions, and then optimize for 101 blue cells.

Let me consider the following type of configuration: blue cells arranged in a "Young diagram" or "Ferrers diagram" shape.

A Ferrers diagram with row lengths λ1 ≥ λ2 ≥ ... ≥ λk. Blue cells are at (i, j) for 1 ≤ j ≤ λi. The total number of blue cells is λ1 + λ2 + ... + λk.

For this configuration:
- Each row has a contiguous block of blue cells (columns 1 to λi).
- Each column j has blue cells in rows 1 to max{i : λi ≥ j}, which is contiguous.

Now, is the partition unique for a Ferrers diagram?

Let me check with the example: λ = (2, 1), i.e., blue at (1,1), (1,2), (2,1). This is a 2×2 grid with 3 blue cells.

Non-blue cell: (2,2). (2,2) must join a rectangle with one blue cell. Options:
- Join (1,2): rectangle {(1,2),(2,2)}: 1 blue cell. Valid.
- Join (2,1): rectangle {(2,1),(2,2)}: 1 blue cell. Valid.
- Join (1,1): rectangle would be {(1,1),(1,2),(2,1),(2,2)}: 3 blue cells. Invalid.

So (2,2) has two options. Not unique.

So Ferrers diagrams don't automatically give uniqueness either.

Hmm. Let me think about what does guarantee uniqueness.

Let me go back to the "full rectangle" idea. If the blue cells form a full a×b rectangle, then the partition is unique: cut into a×b unit rectangles. But this uses ab blue cells, and n = max(a, b), so we'd need ab = 101 with n = max(a,b) minimized. Since 101 is prime, the only factorization is 1×101, giving n = 101. Same as the single row.

So we need a non-rectangular arrangement. Let me think about what shapes work.

Let me consider the following: a "staircase" where each step is a full rectangle.

Actually, let me think about the problem more carefully. Let me consider the concept of "guillotine cuts."

A guillotine cut is a cut that goes all the way across a rectangle. A partition is a guillotine partition if it can be obtained by a sequence of guillotine cuts.

For uniqueness, I think we need the partition to be "forced" at every step.

Let me think about a recursive structure. 

Consider a grid where we can make a forced guillotine cut, splitting it into two sub-grids, each of which has a forced guillotine cut, etc.

A guillotine cut is forced if one side has exactly one "row" or "column" of blue cells that can't be split.

Hmm, this is getting complicated. Let me try a different approach: think about small cases and find a pattern.

Let me think about what the answer might be. We need 101 blue cells. The answer is the smallest n.

If we could use a √101 × √101 arrangement, n would be about 11. But 101 is prime, so we can't make a rectangle.

Let me think about a "near-square" arrangement. 101 = 10 × 10 + 1 = 10² + 1. Or 101 = 9 × 11 + 2. Or 101 = 7 × 14 + 3. Etc.

Actually, let me think about the problem differently. Let me consider the following construction:

Place blue cells in a "staircase" pattern where each row has one more (or one fewer) blue cell than the previous, and the rows are "aligned" in a specific way.

Wait, I showed that Ferrers diagrams don't work. Let me think about what additional structure is needed.

Let me reconsider the problem. The key difficulty is assigning non-blue cells to rectangles uniquely. 

What if there are no non-blue cells? Then n² = 101, but 101 isn't a perfect square. So there must be non-blue cells.

What if there's exactly one non-blue cell? Then n² = 102. 102 isn't a perfect square either. n² - 101 non-blue cells. For n = 11, n² = 121, so 20 non-blue cells. For n = 10, n² = 100 < 101. So n ≥ 11.

Wait, n = 10 gives 100 cells, which is less than 101. So n ≥ 11.

Can we achieve n = 11? We'd have 121 cells, 101 blue, 20 non-blue. We need to arrange 101 blue cells in an 11×11 grid with a unique partition.

Hmm, let me think about whether n = 11 is achievable.

Actually wait. Let me reconsider. Maybe the answer is larger than 11.

Let me think about upper bounds on the number of blue cells for a unique partition in an n×n grid.

For a unique partition, I claim that the blue cells must form a "staircase" shape (in a generalized sense), and the maximum number of blue cells for a unique partition in an n×n grid is related to n.

Let me think about what the maximum number of blue cells is such that the partition is unique.

From the necessary condition (contiguous in each row and column), the blue cells form a "polyomino" that is "convex" (row-convex and column-convex). But we showed this isn't sufficient.

Let me think about a stronger condition. 

I think the right condition for uniqueness is that the blue cells form a "staircase" where the row intervals are "nested" — i.e., the intervals are either identical or one is completely to the left/right of the other, or they share an endpoint in a specific way.

Actually, let me think about this more carefully with a key example.

Consider blue cells forming a "cross" or "plus" shape. Or consider a specific construction that I know works.

Let me think about the "staircase" construction more carefully.

Consider the following arrangement in an n×n grid:
- Row 1: columns 1, 2, ..., n (all blue)
- Row 2: column n only
- Row 3: column n only
- ...
- Row n: column n only

Total blue cells: n + (n-1) = 2n - 1.

Is the partition unique? Row 1 has all blue cells, columns 1 through n-1 have blue only in row 1, column n has blue in all rows.

For row 1, the blue cells are contiguous (columns 1 to n). For each column, blue cells are contiguous (column j, j < n: just row 1; column n: rows 1 to n).

Non-blue cells: (i, j) for 2 ≤ i ≤ n, 1 ≤ j ≤ n-1.

Cell (2, 1) must join a rectangle with one blue cell. The only adjacent blue cell is (1, 1). Rectangle {(1,1), (2,1)}: 1 blue cell. Could (2,1) join (1,2)? Rectangle would include (1,1), (1,2), (2,1), and possibly (2,2): 2 blue cells. Invalid. Could (2,1) join (2,n)? Not contiguous. So (2,1) must join (1,1).

Similarly, (2, j) for j < n must join (1, j). So the rectangles for row 1 blue cells extend down to row 2.

But wait, (2, j) joins (1, j), making rectangle {(1,j), (2,j)}. Then (3, j) must join a rectangle with one blue cell. It can join {(1,j), (2,j)} extending to row 3: {(1,j), (2,j), (3,j)}: 1 blue cell. Or join (3, n) if j = n-1... (3, n-1) and (3, n): rectangle {(3, n-1), (3, n)}: but (3, n) is blue, so 1 blue cell. But (3, n-1) is non-blue. Is this valid? The rectangle {(3, n-1), (3, n)} has 1 blue cell (at (3,n)). But we need to check if this is a valid rectangle in the partition. (3, n) is blue and needs its own rectangle. If (3, n-1) joins (3, n)'s rectangle, then (3, n)'s rectangle is {(3, n-1), (3, n)} or larger. But (2, n) is also blue and needs its own rectangle. 

Hmm, let me be more careful. Let me consider n = 3: blue at (1,1), (1,2), (1,3), (2,3), (3,3). 5 blue cells in a 3×3 grid. Non-blue: (2,1), (2,2), (3,1), (3,2).

This is the L-shape I considered earlier, and I showed it's NOT unique (two valid partitions).

So the "L-shape" doesn't work. The issue is that (2,2) can join either (1,2) or (2,3).

So what arrangement does work?

Let me think about what makes the L-shape fail. The problem is at the "corner" of the L, where (1,2) and (2,3) are diagonal, and (2,2) is the cell between them that can go either way.

To fix this, I need to prevent (2,2) from having two options. One way: make (2,2) blue. Then the L-shape becomes a 2×2 block plus an extension, and we need to check uniqueness.

Blue at (1,1), (1,2), (1,3), (2,2), (2,3), (3,3) in a 3×3 grid. 6 blue cells. Non-blue: (2,1), (3,1), (3,2).

Row 1: [1,3] contiguous. Row 2: [2,3] contiguous. Row 3: [3,3] contiguous.
Column 1: [1,1]. Column 2: [1,2]. Column 3: [1,3]. All contiguous.

(2,1) must join a rectangle with one blue cell. Adjacent blue: (1,1). Rectangle {(1,1),(2,1)}: 1 blue. Could join (2,2)? Rectangle {(2,1),(2,2)}: 1 blue. Valid! So (2,1) has two options. Not unique.

Hmm. So even adding (2,2) doesn't fix it because (2,1) can join either (1,1) or (2,2).

The issue is that (1,1) and (2,2) are diagonal in the 2×2 block {(1,1),(1,2),(2,1),(2,2)}, with (1,2) also blue. So (2,1) can join (1,1) (making a vertical 2×1) or join (2,2) (making a horizontal 1×2), and both are valid because (1,2) is in its own rectangle.

So the problem is fundamentally about 2×2 blocks with 3 blue cells (one non-blue cell). The non-blue cell can join either of its two blue neighbors (if both are blue and diagonal).

Wait, in the 2×2 block {(1,1),(1,2),(2,1),(2,2)} with (1,1), (1,2), (2,2) blue and (2,1) non-blue: (2,1) can join (1,1) (vertical pair) or (2,2) (horizontal pair). Both give rectangles with 1 blue cell. And (1,2) is separate. So not unique.

To make it unique, we need to eliminate this ambiguity. One way: make all 4 cells blue (then each is its own rectangle, forced). Another way: make only 2 cells blue, but they must be adjacent (not diagonal).

So in any 2×2 block, if there are exactly 3 blue cells, the partition is not unique (the non-blue cell has two options). If there are 2 blue cells that are diagonal, not unique. If there are 2 blue cells that are adjacent, it might be OK (the non-blue cells must join the adjacent blue cell's rectangle, but need to check globally).

So for uniqueness, we need: in every 2×2 block, the blue cells are either 0, 1, 2 (adjacent), or 4. No 2×2 block with 3 blue cells, and no 2×2 block with 2 diagonal blue cells.

Wait, but 0 blue cells in a 2×2 block is fine (those cells join other rectangles). 1 blue cell is fine. 2 adjacent is fine (potentially). 4 is fine (each is its own rectangle). 3 is bad. 2 diagonal is bad.

So the condition is: no 2×2 block has exactly 3 blue cells, and no 2×2 block has 2 diagonal blue cells.

The "no 2 diagonal blue cells in a 2×2 block" condition means: if (i,j) and (i+1,j+1) are both blue, then at least one of (i,j+1) or (i+1,j) must also be blue. Similarly for (i,j+1) and (i+1,j).

And "no 3 blue cells in a 2×2 block" means: if 3 of the 4 cells in a 2×2 block are blue, that's forbidden.

These two conditions together mean: in every 2×2 block, the number of blue cells is 0, 1, 2 (adjacent), or 4. Equivalently, the blue cells in any 2×2 block form a "connected" subset (in the sense that they don't have a diagonal pair without a connecting cell).

Wait, let me re-examine. 2 adjacent blue cells in a 2×2 block: is the partition always unique (locally)? 

Consider a 2×2 block with blue at (1,1) and (1,2), non-blue at (2,1) and (2,2). (2,1) must join (1,1) (the only adjacent blue cell). (2,2) must join (1,2) (the only adjacent blue cell). So locally, it's forced. But globally, could (2,1) join some other blue cell outside this block? Only if there's a blue cell at (3,1) or (2,0) (out of bounds). If (3,1) is blue, then (2,1) could join (3,1) instead. So we need to consider the global structure.

OK so the local conditions (no 3 in a 2×2, no 2 diagonal in a 2×2) are necessary but might not be sufficient. But let me assume they're the key conditions and see where they lead.

So the blue cells must satisfy:
1. In every 2×2 subgrid, the blue cells are not exactly 3.
2. In every 2×2 subgrid, the blue cells don't form a diagonal pair.

Condition 2 means: the blue cells form a "polyomino" that is both row-convex and column-convex (no holes in any row or column), AND additionally, the shape is "staircase-like" — the row intervals shift by at most 1 at each step.

Wait, let me think about condition 2 more carefully. No diagonal pair in any 2×2 block means: if (i,j) is blue and (i+1,j+1) is blue, then (i,j+1) or (i+1,j) is blue. This is exactly the condition that the blue cells form a "Young diagram" (Ferrers diagram) shape, or more generally, a "staircase convex" shape.

Actually, the condition "no diagonal pair in any 2×2 block" is equivalent to saying the blue region is "hv-convex" and "connected in a specific way." Let me think...

If (i,j) and (i+1,j+1) are blue but (i,j+1) and (i+1,j) are not, that's a diagonal pair. The condition forbids this. This means: if row i has blue at column j and row i+1 has blue at column j+1, then either row i also has blue at column j+1, or row i+1 also has blue at column j.

For Ferrers diagrams (row-convex, column-convex, rows are left-justified and non-increasing), this condition is automatically satisfied: if (i,j) is blue (j ≤ λi) and (i+1,j+1) is blue (j+1 ≤ λi+1 ≤ λi), then (i,j+1) is blue (j+1 ≤ λi). So Ferrers diagrams satisfy condition 2.

But we also need condition 1: no 2×2 block with exactly 3 blue cells. For a Ferrers diagram, consider the "corner" at row i where λi > λi+1. The 2×2 block at rows i, i+1 and columns λi+1, λi+1 + 1 (if λi ≥ λi+1 + 1). Wait, let me be more specific.

Consider λ = (3, 1). Blue at (1,1), (1,2), (1,3), (2,1). The 2×2 block at rows 1-2, columns 1-2: blue at (1,1), (1,2), (2,1). That's 3 blue cells. Violates condition 1!

So Ferrers diagrams with "jumps" (λi - λi+1 ≥ 2) violate condition 1.

For condition 1 to hold, we need λi - λi+1 ≤ 1 for all i (the row lengths decrease by at most 1). And also, the first row can't be too long compared to the second, etc.

Wait, let me re-examine. For a Ferrers diagram with row lengths λ1 ≥ λ2 ≥ ... ≥ λk, condition 1 (no 3 blue in any 2×2) requires: for each i, the 2×2 block at rows i, i+1 and columns λi+1, λi+1 + 1 has at most 2 blue cells (if λi ≥ λi+1 + 1). The blue cells in this block are: (i, λi+1) [blue since λi+1 ≤ λi], (i, λi+1 + 1) [blue if λi+1 + 1 ≤ λi, i.e., λi ≥ λi+1 + 1], (i+1, λi+1) [blue], (i+1, λi+1 + 1) [not blue since λi+1 + 1 > λi+1]. So if λi ≥ λi+1 + 1, the block has 3 blue cells. So we need λi ≤ λi+1 + 1, i.e., λi - λi+1 ≤ 1.

But also, consider the 2×2 block at rows i, i+1 and columns λi+1 + 1, λi+1 + 2 (if λi ≥ λi+1 + 2). Blue cells: (i, λi+1 + 1) [blue], (i, λi+1 + 2) [blue if λi ≥ λi+1 + 2], (i+1, λi+1 + 1) [not blue], (i+1, λi+1 + 2) [not blue]. That's 2 blue cells, and they're adjacent (both in row i). So this is fine.

So the only problematic 2×2 blocks are those at the "step" where λi > λi+1. And the condition is λi - λi+1 ≤ 1.

So for a Ferrers diagram, the conditions for uniqueness (assuming they're sufficient) are:
1. λi - λi+1 ≤ 1 for all i (row lengths decrease by at most 1).
2. The shape is a Ferrers diagram (which automatically satisfies condition 2).

But wait, I need to also check condition 1 for 2×2 blocks not at the "step." For a Ferrers diagram, the only 2×2 blocks with 3 blue cells are at the steps. And 2×2 blocks with 2 diagonal blue cells don't occur (as I argued). So the conditions are:
- Ferrers diagram (left-justified, non-increasing row lengths)
- λi - λi+1 ≤ 1 for all i (including λk ≥ 0, so the last row has at least λk-1 - 1 blue cells, etc.)

But wait, I also need to consider 2×2 blocks where the blue cells are in rows i, i+1 but the columns span a "step" in a different way. Let me re-examine.

For a Ferrers diagram, the blue cells in row i are columns 1 to λi. Consider a 2×2 block at rows i, i+1, columns j, j+1.

Case 1: j+1 ≤ λi+1. Then all 4 cells are blue. Fine (4 blue cells).
Case 2: j = λi+1, j+1 ≤ λi. Then (i,j), (i,j+1), (i+1,j) are blue, (i+1,j+1) is not. 3 blue cells. This is the step case, and we need λi ≤ λi+1 + 1, i.e., j+1 ≤ λi+1 + 1, i.e., λi ≤ λi+1 + 1.
Case 3: j = λi+1, j+1 > λi. Then (i,j) is blue (j = λi+1 ≤ λi), (i+1,j) is blue, (i,j+1) is not blue (j+1 > λi), (i+1,j+1) is not blue. 2 blue cells, adjacent (same column). Fine.
Case 4: j > λi+1, j+1 ≤ λi. Then (i,j), (i,j+1) are blue, (i+1,j), (i+1,j+1) are not. 2 blue cells, adjacent (same row). Fine.
Case 5: j > λi. No blue cells. Fine.

So the only problematic case is Case 2, which requires λi ≤ λi+1 + 1.

So for a Ferrers diagram, the conditions reduce to: λi - λi+1 ≤ 1 for all i (where λk+1 = 0, so λk ≤ 1, meaning the last row has at most 1 blue cell).

Wait, λk - 0 ≤ 1, so λk ≤ 1. The last row has at most 1 blue cell. And λk-1 - λk ≤ 1, so λk-1 ≤ λk + 1 ≤ 2. And so on: λi ≤ λi+1 + 1, so λ1 ≤ λ2 + 1 ≤ λ3 + 2 ≤ ... ≤ λk + (k-1) ≤ 1 + (k-1) = k.

So λ1 ≤ k, meaning the first row has at most k blue cells (where k is the number of rows). And the total number of blue cells is λ1 + λ2 + ... + λk.

To maximize the total with the constraint λi - λi+1 ≤ 1 and λi ≥ λi+1 (Ferrers) and λk ≥ 1 (at least one blue cell in the last row):

The maximum is achieved when λi - λi+1 = 1 for all i, giving λi = λk + (k - i). With λk = 1: λi = k - i + 1. So λ = (k, k-1, ..., 2, 1). Total = k + (k-1) + ... + 1 = k(k+1)/2.

And the grid size is n × n where n ≥ k (since λ1 = k) and n ≥ k (number of rows). So n = k.

Total blue cells = k(k+1)/2. We need k(k+1)/2 ≥ 101.

k(k+1)/2 ≥ 101 → k(k+1) ≥ 202 → k ≥ 14 (since 13×14 = 182 < 202, 14×15 = 210 ≥ 202).

But wait, we need exactly 101 blue cells, not at least 101. And we need the partition to be unique.

Hmm, but I've only shown these conditions are necessary. I haven't shown they're sufficient. And I've only considered Ferrers diagrams. There might be other shapes that work.

Also, I assumed the conditions (no 3 in a 2×2, no 2 diagonal in a 2×2) are sufficient for uniqueness, which I haven't proven.

Let me step back and think about this more carefully.

Actually, wait. I think I was too hasty. Let me reconsider whether the conditions are sufficient.

Let me check: Ferrers diagram with λ = (2, 1). Blue at (1,1), (1,2), (2,1). 2×2 block at rows 1-2, columns 1-2: 3 blue cells. Violates condition 1. So this is correctly identified as non-unique.

Ferrers diagram with λ = (2, 2). Blue at (1,1), (1,2), (2,1), (2,2). 4 blue cells in the only 2×2 block. Conditions satisfied. Is the partition unique? Yes, each cell is its own rectangle. ✓

Ferrers diagram with λ = (3, 2, 1). Blue at (1,1), (1,2), (1,3), (2,1), (2,2), (3,1). 6 blue cells in a 3×3 grid.

Check conditions:
- 2×2 at rows 1-2, cols 1-2: all 4 blue. ✓
- 2×2 at rows 1-2, cols 2-3: (1,2), (1,3) blue, (2,2) blue, (2,3) not blue. 3 blue cells. ✗!

So λ = (3, 2, 1) violates condition 1 (λ1 - λ2 = 1 is OK, but the 2×2 block at cols 2-3 has 3 blue cells). Wait, let me recheck.

Row 1: blue at 1, 2, 3. Row 2: blue at 1, 2. 2×2 block at rows 1-2, cols 2-3: (1,2) blue, (1,3) blue, (2,2) blue, (2,3) not blue. 3 blue cells. Yes, this violates condition 1.

But λ1 - λ2 = 3 - 2 = 1 ≤ 1. So my earlier analysis was wrong? Let me recheck.

The 2×2 block at rows 1-2, columns 2-3. λ2 = 2, so column 2 is the last blue column in row 2. The step is at column 2/3. j = λ2 = 2, j+1 = 3. λ1 = 3 ≥ 3 = j+1, so (1, 3) is blue. This is Case 2: (i, j) = (1, 2) blue, (i, j+1) = (1, 3) blue, (i+1, j) = (2, 2) blue, (i+1, j+1) = (2, 3) not blue. 3 blue cells. Condition: λ1 ≤ λ2 + 1 = 3. λ1 = 3 ≤ 3. ✓.

Wait, so the condition λi ≤ λi+1 + 1 is satisfied (3 ≤ 2 + 1 = 3), but there are still 3 blue cells in the 2×2 block. So my condition was wrong!

Let me re-derive. The 2×2 block at rows i, i+1, columns j, j+1 where j = λi+1. Blue cells: (i, j) [blue since j = λi+1 ≤ λi], (i, j+1) [blue if j+1 ≤ λi], (i+1, j) [blue since j = λi+1], (i+1, j+1) [not blue since j+1 > λi+1]. So 3 blue cells if j+1 ≤ λi, i.e., λi+1 + 1 ≤ λi, i.e., λi ≥ λi+1 + 2. And 2 blue cells if λi = λi+1 + 1 (then j+1 = λi+1 + 1 = λi, so (i, j+1) = (i, λi) is blue... wait, j+1 = λi+1 + 1. If λi = λi+1 + 1, then j+1 = λi, so (i, j+1) = (i, λi) is blue. So 3 blue cells.

Hmm wait, let me redo this. j = λi+1. (i, j+1) is blue iff j+1 ≤ λi iff λi+1 + 1 ≤ λi iff λi ≥ λi+1 + 1.

If λi = λi+1: j = λi+1 = λi. j+1 = λi + 1 > λi. So (i, j+1) is not blue. 2 blue cells: (i, j) and (i+1, j). Adjacent (same column). Fine.

If λi = λi+1 + 1: j = λi+1. j+1 = λi+1 + 1 = λi. (i, j+1) = (i, λi) is blue. 3 blue cells. Bad!

If λi ≥ λi+1 + 2: j = λi+1. j+1 = λi+1 + 1 ≤ λi. (i, j+1) is blue. 3 blue cells. Bad!

So the condition for no 3 blue cells in any 2×2 block is: λi = λi+1 for all i (since λi ≥ λi+1 for Ferrers, and λi > λi+1 gives 3 blue cells).

But that means all rows have the same length, i.e., the blue cells form a rectangle! And a rectangle with 101 blue cells requires 101 = a × b with n = max(a, b) ≥ 11 (since 101 is prime, a = 1, b = 101, n = 101).

That can't be right—the answer would be 101, which seems too large for a competition problem.

Wait, I think I'm being too restrictive. I was only considering Ferrers diagrams (left-justified). There might be other shapes that satisfy the conditions.

Let me reconsider. The conditions are:
1. No 2×2 block has exactly 3 blue cells.
2. No 2×2 block has 2 diagonal blue cells.

These don't require the shape to be a Ferrers diagram. Let me think about other shapes.

Consider a "staircase" that goes in both directions. For example:
Row 1: columns 1 to a (blue)
Row 2: columns 2 to a+1 (blue)
Row 3: columns 3 to a+2 (blue)
...

This is a "shifted" staircase. Let me check the conditions.

Row i: columns i to a+i-1 (blue). 

2×2 block at rows i, i+1, columns j, j+1:
- Row i has blue at j, j+1 iff i ≤ j and j+1 ≤ a+i-1, i.e., j ≥ i and j ≤ a+i-2.
- Row i+1 has blue at j, j+1 iff i+1 ≤ j and j+1 ≤ a+i, i.e., j ≥ i+1 and j ≤ a+i-1.

Case: j = i. Row i: blue at j=i, j+1=i+1 (if i+1 ≤ a+i-1, i.e., a ≥ 2). Row i+1: not blue at j=i (since i < i+1). So blue cells: (i, i), (i, i+1). 2 blue cells, adjacent. Fine (if a ≥ 2).

Case: j = i+1. Row i: blue at j=i+1, j+1=i+2 (if i+2 ≤ a+i-1, i.e., a ≥ 3). Row i+1: blue at j=i+1, j+1=i+2 (if i+2 ≤ a+i, i.e., a ≥ 2). If a ≥ 3: all 4 blue. Fine. If a = 2: row i has blue at i+1 but not i+2 (since i+2 > a+i-1 = i+1). Row i+1 has blue at i+1 and i+2 (since i+2 = a+i). So blue: (i, i+1), (i+1, i+1), (i+1, i+2). 3 blue cells. Bad!

So the shifted staircase with a = 2 has 3 blue cells in some 2×2 blocks. With a ≥ 3, the interior 2×2 blocks are fine, but I need to check the boundary blocks.

Actually, this is getting quite complex. Let me think about the problem differently.

Let me reconsider: maybe the conditions I stated (no 3 in a 2×2, no 2 diagonal in a 2×2) are not sufficient for uniqueness, and the actual condition is different.

Let me go back to first principles and think about what makes a rectangular partition unique.

Actually, I realize I should think about this more carefully. The conditions I derived are necessary (if violated, the partition is not unique). But they might not be sufficient. Let me think about whether there are other sources of non-uniqueness.

Consider a 1×4 grid with blue at positions 1 and 3. Non-blue at 2 and 4. 

2×2 conditions don't apply (only 1 row). But the partition is not unique: {(1),(2)} and {(3),(4)}, or {(1)} and {(2),(3)} and {(4)}... wait, {(2),(3)} has 1 blue cell (3). But then we have 3 rectangles: {(1)}, {(2),(3)}, {(4)}. But {(4)} has 0 blue cells. Invalid. 

Actually, let me reconsider. 1×4 grid, blue at 1 and 3. We need 2 rectangles (one per blue cell). 
- {(1),(2)} and {(3),(4)}: each has 1 blue. Valid.
- {(1)} and {(2),(3),(4)}: 1 blue each. Valid.
- {(1),(2),(3)} and {(4)}: 2 blue and 0 blue. Invalid.
- {(1)} and {(2),(3)} and {(4)}: 3 rectangles but only 2 blue cells. Invalid (each rectangle needs exactly 1 blue cell, so we need exactly 2 rectangles).

Wait, actually we need exactly as many rectangles as blue cells. So 2 rectangles.

- {(1),(2)} and {(3),(4)}: valid.
- {(1)} and {(2),(3),(4)}: valid.
- {(1),(2),(3)} and {(4)}: invalid (2 blue in first).

So 2 valid partitions. Not unique. The issue is that blue cells 1 and 3 are not adjacent, so the cut between them can be at position 1-2 or 2-3.

So in 1D, uniqueness requires all blue cells to be adjacent (consecutive). This is the "contiguous" condition.

In 2D, the situation is more complex. Let me think about whether the 2×2 conditions plus contiguity are sufficient.

Actually, I think the right way to think about this is:

The partition is unique if and only if every "cut" is forced. A cut is forced if removing it creates an invalid partition (some rectangle with 0 or ≥2 blue cells).

Let me think about when a cut is not forced. A cut between two adjacent cells is not forced if both cells can be in the same rectangle (i.e., removing the cut still gives a valid partition). This happens when the two cells are in the same "blue region" and combining them doesn't create a rectangle with ≥2 blue cells.

Hmm, this is still complex. Let me try a different approach: think about the problem as a competition problem and try to find the answer.

Let me consider the possibility that the answer is 101 (the trivial single-row construction). But that seems too easy for a competition problem. Let me think about whether we can do better.

Let me consider the "staircase" construction more carefully, but with a different shape.

Consider the following arrangement: a "path" of blue cells where each blue cell is adjacent to the next, forming a Hamiltonian-like path. But we need the partition to be unique.

Actually, let me think about a "snake" path. Consider a 1×n strip folded into a snake:

Row 1: columns 1, 2, ..., n (all blue)
Row 2: columns n, n-1, ..., 1 ... no, this doesn't make sense for a path.

Let me think about a different construction. Consider an arrangement where the blue cells form a "staircase" that goes down and right:

(1,1), (2,1), (2,2), (3,2), (3,3), (4,3), (4,4), ...

Each blue cell is adjacent to the next. The path goes: right, down, right, down, ...

For this path, consider the 2×2 block at rows 1-2, columns 1-2: blue at (1,1), (2,1), (2,2). 3 blue cells. Violates condition 1.

So this staircase path doesn't work either.

What if we "fill in" the staircase to avoid 3-in-a-2×2? We'd need to add (1,2) to make it 4, or remove one of the 3.

If we add (1,2): blue at (1,1), (1,2), (2,1), (2,2). That's a 2×2 block. Then continue: (2,2), (3,2), (3,3), (4,3), (4,4), ... But (2,2) is already in the 2×2 block. The next step is (3,2). 2×2 block at rows 2-3, columns 2-3: blue at (2,2), (3,2), (3,3). 3 blue cells. Need to add (2,3). Then 2×2 block at rows 2-3, cols 2-3: all 4 blue. Continue with (3,3), (4,3), (4,4), ... 2×2 at rows 3-4, cols 3-4: (3,3), (4,3), (4,4). 3 blue. Add (3,4). 

So the pattern is: 2×2 blocks along the diagonal. Blue cells at (i,j) where i ∈ {2k-1, 2k} and j ∈ {2k-1, 2k} for k = 1, 2, ..., m. This gives 4m blue cells in a 2m × 2m grid. For 101 blue cells, 4m = 101 doesn't work (101 not divisible by 4).

Hmm. Let me think about this differently.

What if we use a mix of 2×2 blocks and single cells?

Actually, let me reconsider the problem. Maybe the conditions I stated are not the right ones, or maybe I need to think about the problem differently.

Let me re-examine the problem statement: "there exists a unique way to cut the table to rectangles along boundaries of its squares with the following property: every rectangle contains exactly one blue square."

So we need: (1) there exists at least one valid partition, and (2) there is at most one valid partition.

Let me think about what configurations have a unique valid partition.

Key insight: I think the right way to think about this is in terms of "separating lines."

Consider two blue cells A and B. They must be in different rectangles. The rectangles must be separated by a cut. If A and B are in the same row (resp. column), the cut must be a vertical (resp. horizontal) line segment between them. If they're not in the same row or column, the separation is more complex.

For the partition to be unique, every separation must be forced.

Let me think about a cleaner characterization. 

I think the key is: the partition is unique if and only if the blue cells form a "staircase" where each row's blue interval and each column's blue interval are "compatible" in a specific way.

Actually, let me try to think about this problem from the answer. Let me consider that the answer might be 15 or 20 or something in that range.

Let me think about the maximum number of blue cells in an n×n grid with a unique partition.

From the analysis of Ferrers diagrams, the maximum with all rows equal is n² (full grid), but that requires n² = 101, impossible.

What if we don't require a Ferrers diagram? Let me think about other shapes.

Consider a "cross" shape: row k is fully blue (n cells), and column k is fully blue (n cells), with the center cell shared. Total: 2n - 1 blue cells. For 2n - 1 = 101, n = 51. Grid size: 51 × 51. But is the partition unique?

In a cross shape, the 2×2 blocks at the corners of the cross (e.g., rows k-1, k, columns k-1, k) have 3 blue cells (the cross covers (k, k-1), (k, k), (k-1, k) but not (k-1, k-1)). So condition 1 is violated. Not unique.

What about a "plus" shape where we fill in the corners? That would be a full grid, which gives n² blue cells.

Let me think about a different type of construction. What if the blue cells form a "thick diagonal"?

Consider blue cells at (i, j) where |i - j| ≤ d for some d. This is a band around the diagonal. For d = 0, it's the diagonal (n cells). For d = 1, it's a tridiagonal (3n - 2 cells). Etc.

For the tridiagonal (d = 1), consider the 2×2 block at rows 1-2, columns 1-2: (1,1), (1,2), (2,1), (2,2) all satisfy |i-j| ≤ 1. All 4 blue. Fine. Block at rows 1-2, columns 2-3: (1,2) |1-2|=1 ✓, (1,3) |1-3|=2 ✗, (2,2) ✓, (2,3) |2-3|=1 ✓. 3 blue cells. Bad!

So the tridiagonal doesn't work.

Hmm. Let me think about what shapes avoid both conditions.

The conditions are:
1. No 2×2 block has exactly 3 blue cells.
2. No 2×2 block has exactly 2 diagonal blue cells.

These together mean: in every 2×2 block, the blue cells form either: empty, 1 cell, 2 adjacent cells, or all 4 cells.

This is equivalent to: the blue cells form a "polyomino" that is a union of disjoint rectangles, where no two rectangles are "diagonally adjacent" (i.e., if two rectangles touch at a corner, they must also share an edge).

Wait, that's not quite right. Let me think again.

Actually, the condition "in every 2×2 block, blue cells are 0, 1, 2 adjacent, or 4" is equivalent to saying the blue region is a "convex polyomino" that is both "row-convex" and "column-convex" AND "monotone" in some sense.

Hmm, actually, I think this condition is equivalent to: the blue region can be decomposed into rectangles such that the rectangles form a "laminar" family (any two are either disjoint, nested, or share a full side).

No, that's not right either. Let me think more carefully.

The condition "no 2×2 block has 3 blue or 2 diagonal blue" means: if (i,j) is blue and (i+1,j+1) is blue, then (i,j+1) and (i+1,j) are both blue. And if (i,j+1) is blue and (i+1,j) is blue, then (i,j) and (i+1,j+1) are both blue.

This means: the blue region is closed under "rectangular completion" — if two diagonal cells of a 2×2 block are blue, the other two must be blue too. This is exactly the condition that the blue region is a "rectangular" or "orthogonal convex" polyomino that is also "hv-convex."

Wait, I think this condition means the blue region is a union of rectangles that are "aligned" in a specific way. Actually, I think it means the blue region is a "staircase polyomino" or "convex polyomino with the additional property."

Let me think about it differently. The condition says: the indicator function of blue cells is "2D-monotone" in some sense. 

Actually, I recall that a set S of grid cells satisfying "if (i,j) and (i+1,j+1) are in S, then (i,j+1) and (i+1,j) are in S" (and the symmetric condition) is called a "convex" set in the sense that it's an intersection of the grid with a convex region. No wait, that's not right either.

Let me just think about what shapes satisfy the condition. 

The condition is: the blue cells form a set where every 2×2 subgrid has 0, 1, 2-adjacent, or 4 blue cells. 

This is equivalent to: the blue cells form a set that is a "disjoint union of rectangles, where the rectangles are separated by at least one empty row or column, OR the rectangles share full edges (not just corners)."

Wait, no. Consider two 2×2 blocks sharing a side. If one is all blue and the other is all blue, together they form a 2×4 or 4×2 rectangle, which is fine. If one is all blue and the other has 2 adjacent blue cells, we need to check the combined 2×3 or 3×2 region.

I think the condition is equivalent to: the blue region is a "polyomino" that can be built by starting with rectangles and merging them only along full sides. But I'm not sure.

Let me try a different approach. Let me just think about what the maximum number of blue cells is in an n×n grid satisfying the 2×2 condition, and see if that helps.

For the 2×2 condition (no 3, no 2-diagonal in any 2×2), the maximum is n² (all cells blue, every 2×2 has 4). But we need exactly 101, not n².

The question is: for which n can we place 101 blue cells in an n×n grid satisfying the 2×2 condition, AND the partition is unique?

But I haven't verified that the 2×2 condition is sufficient for uniqueness. Let me check with a larger example.

Consider a 3×3 grid with all 9 cells blue. Every 2×2 has 4 blue. Partition: 9 unit rectangles. Unique? Yes, because any larger rectangle would have ≥2 blue cells. ✓

Consider a 3×3 grid with blue at (1,1), (1,2), (2,1), (2,2) (a 2×2 block in the corner). 4 blue cells. Non-blue: (1,3), (2,3), (3,1), (3,2), (3,3).

2×2 conditions:
- Rows 1-2, cols 1-2: 4 blue. ✓
- Rows 1-2, cols 2-3: (1,2) blue, (1,3) not, (2,2) blue, (2,3) not. 2 adjacent. ✓
- Rows 2-3, cols 1-2: (2,1) blue, (2,2) blue, (3,1) not, (3,2) not. 2 adjacent. ✓
- Rows 2-3, cols 2-3: (2,2) blue, (2,3) not, (3,2) not, (3,3) not. 1 blue. ✓

Conditions satisfied. Is the partition unique?

Non-blue cells: (1,3), (2,3), (3,1), (3,2), (3,3).

(1,3): must join a rectangle with 1 blue cell. Adjacent blue: (1,2). Rectangle {(1,2), (1,3)}: 1 blue. Could (1,3) join (2,2)? Rectangle would be {(1,2), (1,3), (2,2), (2,3)}: 2 blue. Invalid. So (1,3) joins (1,2). Forced.

(2,3): adjacent blue: (2,2). Rectangle {(2,2), (2,3)}: 1 blue. But (1,3) already joined (1,2), and (2,3) joining (2,2) would make rectangle {(2,2), (2,3)}. Is there another option? (2,3) joining (1,3)? (1,3) is not blue. (2,3) joining (3,3)? (3,3) is not blue. So (2,3) must join (2,2). Forced.

(3,1): adjacent blue: (2,1). Rectangle {(2,1), (3,1)}: 1 blue. Other options? (3,1) joining (3,2)? (3,2) not blue. So forced.

(3,2): adjacent blue: (2,2). But (2,2) is already in rectangle {(2,2), (2,3)}. Can (3,2) join that? Rectangle {(2,2), (2,3), (3,2), (3,3)}: 1 blue. Valid! Or (3,2) joining (2,1)? (2,1) is in {(2,1), (3,1)}. Adding (3,2) would make {(2,1), (3,1), (3,2)}: 1 blue. But is this a rectangle? (2,1), (3,1), (3,2) is not a rectangle (it's an L-shape). Invalid. Or (3,2) joining (3,1)? (3,1) is in {(2,1), (3,1)}. Adding (3,2): {(2,1), (3,1), (3,2)} not a rectangle. Invalid.

So (3,2) must join the rectangle containing (2,2), which is {(2,2), (2,3)}. Extended to {(2,2), (2,3), (3,2), (3,3)}. 1 blue. Valid. Forced.

(3,3): already in the rectangle {(2,2), (2,3), (3,2), (3,3)}. 

So the partition is:
- {(1,1)}, {(1,2), (1,3)}, {(2,1), (3,1)}, {(2,2), (2,3), (3,2), (3,3)}.

Wait, but I need to check: is (3,3) forced to be in the rectangle with (2,2)? (3,3) is adjacent to (3,2) and (2,3), both of which are in the (2,2) rectangle. (3,3) could also be its own rectangle, but that has 0 blue cells. Invalid. So (3,3) must join a rectangle with a blue cell. The only adjacent cells with blue cells are (3,2) and (2,3), both in the (2,2) rectangle. So (3,3) joins that rectangle. Forced.

But wait, I need to also check: could (3,2) and (3,3) form a separate rectangle with (2,3)? Like, instead of (3,2) joining (2,2)'s rectangle, could we have a different partition where (3,2) and (3,3) join (2,3)?

Let me reconsider. The rectangle containing (2,2) must be a rectangle containing (2,2) and no other blue cell. The blue cells are (1,1), (1,2), (2,1), (2,2). So (2,2)'s rectangle contains only (2,2) as a blue cell.

What are the possible rectangles containing (2,2) with no other blue cell?
- {(2,2)}: 1 blue. Valid.
- {(2,2), (2,3)}: 1 blue. Valid.
- {(2,2), (3,2)}: 1 blue. Valid.
- {(2,2), (2,3), (3,2), (3,3)}: 1 blue. Valid.
- {(2,2), (1,2)}: 2 blue. Invalid.
- {(2,2), (2,1)}: 2 blue. Invalid.
- {(2,2), (1,3)}: not a rectangle (not contiguous). Invalid.
- {(2,2), (2,3), (3,2)}: not a rectangle (L-shape). Invalid.
- {(1,2), (1,3), (2,2), (2,3)}: 2 blue. Invalid.
- Larger rectangles including (2,2): any rectangle including (1,2) or (2,1) has 2 blue. So the rectangle can only extend right and/or down.

So the possible rectangles for (2,2) are: {(2,2)}, {(2,2),(2,3)}, {(2,2),(3,2)}, {(2,2),(2,3),(3,2),(3,3)}.

Now, (1,3) must be in some rectangle with 1 blue cell. (1,3) is adjacent to (1,2) [blue] and (2,3) [not blue]. 
- If (1,3) joins (1,2): rectangle {(1,2), (1,3)}. Then (2,2)'s rectangle can be any of the 4 options.
- If (1,3) doesn't join (1,2): (1,3) must join a rectangle with some blue cell. The only blue cell reachable is (1,2) (since (2,3) is not blue and (1,3) is in the corner). Actually, (1,3) could be in a rectangle with (2,2) if the rectangle is {(1,2), (1,3), (2,2), (2,3)}: 2 blue. Invalid. Or {(1,3), (2,3)}: 0 blue. Invalid. So (1,3) must join (1,2). Forced.

Similarly, (2,3) must join a rectangle with 1 blue cell. (2,3) is adjacent to (1,3) [in (1,2)'s rectangle], (2,2) [blue], (3,3) [not blue]. 
- (2,3) joining (2,2): rectangle could be {(2,2), (2,3)} or larger.
- (2,3) joining (1,2)'s rectangle: would need rectangle including (1,2), (1,3), (2,2), (2,3): 2 blue. Invalid.
- (2,3) joining (3,3): 0 blue. Invalid.
So (2,3) must join (2,2). Forced.

(3,1) must join (2,1) (only adjacent blue cell). Forced.

(3,2): adjacent to (3,1) [in (2,1)'s rectangle], (2,2) [blue], (3,3) [not blue].
- (3,2) joining (2,2): rectangle {(2,2), (3,2)} or larger. But (2,3) is already in (2,2)'s rectangle, so the rectangle is at least {(2,2), (2,3), (3,2), (3,3)} (to be a valid rectangle). 1 blue. Valid.
- (3,2) joining (2,1)'s rectangle: would need rectangle including (2,1), (3,1), (3,2): L-shape. Invalid. Or (2,1), (2,2), (3,1), (3,2): 2 blue. Invalid.
- (3,2) joining (3,3): 0 blue. Invalid.
So (3,2) must join (2,2)'s rectangle. Forced.

(3,3): adjacent to (3,2) [in (2,2)'s rectangle], (2,3) [in (2,2)'s rectangle]. Must join (2,2)'s rectangle. Forced.

So the partition is unique:
- {(1,1)}, {(1,2), (1,3)}, {(2,1), (3,1)}, {(2,2), (2,3), (3,2), (3,3)}.

Great, so the 2×2 block in the corner of a 3×3 grid gives a unique partition. ✓

Now, the question is: can we combine multiple such blocks to get 101 blue cells in a small grid?

Let me think about combining blocks. Consider a grid made of multiple 2×2 blocks of blue cells, separated by gaps.

For example, two 2×2 blocks: one at rows 1-2, cols 1-2, and one at rows 1-2, cols 4-5. In a 2×5 grid. 8 blue cells. Non-blue: (1,3), (2,3).

2×2 conditions:
- Rows 1-2, cols 1-2: 4 blue. ✓
- Rows 1-2, cols 2-3: (1,2) blue, (1,3) not, (2,2) blue, (2,3) not. 2 adjacent. ✓
- Rows 1-2, cols 3-4: (1,3) not, (1,4) blue, (2,3) not, (2,4) blue. 2 diagonal! ✗

So two 2×2 blocks in the same rows, separated by one column, violate condition 2 (diagonal pair in the 2×2 block at cols 3-4). 

To fix this, we need at least 2 empty columns between blocks (so that the 2×2 blocks at the boundary have at most 1 blue cell). Or we need the blocks to be in different rows.

If blocks are in different rows and different columns (no overlap), separated by at least one empty row and one empty column, then the 2×2 conditions are satisfied at the boundaries.

But this is wasteful. Let me think about more efficient arrangements.

What if the blocks share a row or column? For example, a 2×4 block (two 2×2 blocks side by side). This is just a 2×4 rectangle of blue cells. 8 blue cells. The partition: each cell is its own rectangle (since any 1×2 or 2×1 rectangle has 2 blue cells). Unique. ✓

So a full a×b rectangle of blue cells gives ab blue cells, and the partition is unique (each cell is 1×1). The grid size is max(a, b). For ab = 101 (prime), we need a=1, b=101, n=101. Not helpful.

But what if we combine a rectangle with some extensions?

Consider a 10×10 rectangle of blue cells (100 blue cells) plus 1 more blue cell. The 10×10 block has a unique partition (each cell is 1×1). The extra blue cell needs to be placed such that the overall partition is still unique.

If the extra blue cell is at (11, 1) (just below the 10×10 block), then the grid is 11×10 (but we need n×n, so 11×11). The non-blue cells are in row 11, columns 2-11, and column 11, rows 1-10.

Wait, the 10×10 block is at rows 1-10, cols 1-10. Extra blue at (11, 1). Grid is 11×11. Non-blue: row 11, cols 2-11 (10 cells), and col 11, rows 1-10 (10 cells). Total non-blue: 20. Total blue: 101. ✓

Is the partition unique?

The 10×10 block: each cell is 1×1 (since any larger rectangle within the block has ≥2 blue cells). So the 100 blue cells in the block each get a 1×1 rectangle. But wait, the non-blue cells need to join some rectangle. 

Cell (1, 11): adjacent to (1, 10) [blue, in 1×1 rectangle]. Can join (1, 10)'s rectangle: {(1,10), (1,11)}: 1 blue. Valid. Any other option? (1, 11) adjacent to (2, 11) [not blue]. So (1, 11) must join (1, 10). Forced.

Similarly, (i, 11) for i = 1, ..., 10 must join (i, 10). Forced.

Cell (11, 2): adjacent to (11, 1) [blue], (10, 2) [blue]. 
- Join (11, 1): rectangle {(11, 1), (11, 2)}: 1 blue. Valid.
- Join (10, 2): rectangle {(10, 2), (11, 2)}: 1 blue. Valid.
Two options! Not unique. ✗

So the extra blue cell at (11, 1) creates ambiguity for (11, 2), which can join either (11, 1) or (10, 2).

To fix this, I need to prevent (11, 2) from joining (10, 2). One way: make (10, 2) unable to extend downward. But (10, 2) is in a 1×1 rectangle, and extending to (11, 2) gives a 2×1 rectangle with 1 blue cell. There's no way to prevent this in the current setup.

Another approach: place the extra blue cell such that it doesn't create this ambiguity. 

What if the extra blue cell is at (11, 11) (diagonally adjacent to the 10×10 block)? Then (11, 11) is adjacent to (10, 11) [not blue] and (11, 10) [not blue]. So (11, 11) is isolated from blue cells. It can't be in a rectangle with any blue cell. Invalid (a 1×1 rectangle at (11,11) has 1 blue cell, but we also need to assign (10, 11) and (11, 10) to rectangles with blue cells).

Actually, (11, 11) is a blue cell, so it needs its own rectangle. The rectangle can be just {(11, 11)}. Then (10, 11) needs to join a rectangle with a blue cell: adjacent to (10, 10) [blue]. Join (10, 10): {(10, 10), (10, 11)}: 1 blue. Valid. (11, 10) needs to join: adjacent to (10, 10) [in rectangle with (10, 11)], (11, 9) [not blue], (11, 11) [blue]. 
- Join (10, 10)'s rectangle: would need rectangle {(10, 10), (10, 11), (11, 10), (11, 11)}: 2 blue. Invalid.
- Join (11, 11): rectangle {(11, 10), (11, 11)}: 1 blue. Valid.
So (11, 10) joins (11, 11). Forced.

But what about (10, 11)? It joins (10, 10). Could (10, 11) join (11, 11)? Rectangle {(10, 11), (11, 11)}: 1 blue. Valid! So (10, 11) has two options: join (10, 10) or join (11, 11). Not unique. ✗

Hmm. The issue is always the same: a non-blue cell adjacent to two blue cells can join either.

So the key challenge is: how to place blue cells such that every non-blue cell is adjacent to at most one blue cell (or more precisely, can join only one blue cell's rectangle).

Wait, that's too strong. A non-blue cell might be adjacent to two blue cells but only able to join one (because joining the other would create an invalid rectangle).

Let me reconsider. The condition for uniqueness is: every non-blue cell can be assigned to exactly one blue cell's rectangle, considering the global constraint that all rectangles must be valid (rectangular, each with exactly 1 blue cell).

This is a global constraint, not just local. So the analysis is more complex.

Let me think about this differently. Maybe I should think about the problem in terms of "forced extensions."

Consider a blue cell B. Its rectangle R(B) must be a rectangle containing B and no other blue cell. The rectangle is determined by its boundaries (top, bottom, left, right). For uniqueness, the boundaries must be forced.

A boundary is forced if moving it would include another blue cell or exclude B.

So R(B) is the "maximal" rectangle around B that contains no other blue cell, in some sense. But "maximal" isn't quite right because the rectangle must partition the grid with other rectangles.

Hmm, let me think about this differently.

Actually, I think the problem is equivalent to: the blue cells are "separated" by a unique set of cuts. The cuts form a "guillotine partition" or more generally a "rectangular partition."

Let me think about the problem from the perspective of the dual graph. 

OK let me try yet another approach. Let me think about the problem as a competition problem and try to find the answer by construction.

I'll try to construct a configuration with 101 blue cells and a unique partition, minimizing n.

Construction idea: Use a "staircase" of rectangles.

Consider the following: divide the n×n grid into rectangles R1, R2, ..., R101, each containing one blue cell. The partition is unique if the rectangles are "forced."

One way to force the partition: make the rectangles form a "guillotine partition" where each cut is forced.

A guillotine cut is forced if one of the two resulting pieces has exactly one blue cell. Then that piece must be a single rectangle, and the cut is the only option.

So consider the following recursive construction:
1. Start with the n×n grid containing 101 blue cells.
2. Find a guillotine cut that separates one blue cell from the rest. This cut is forced (the piece with 1 blue cell must be a rectangle containing just that cell, and the cut position is forced if the piece is determined).
3. Recurse on the remaining piece with 100 blue cells.

For this to work, at each step, we need a forced guillotine cut. A guillotine cut that separates exactly 1 blue cell is forced if the resulting 1-blue-cell piece is a rectangle (which it is, since it's a guillotine cut).

But we also need the cut to be uniquely determined. If there are multiple positions for the guillotine cut that separate 1 blue cell, the partition is not unique.

Hmm, so we need: at each step, there's exactly one guillotine cut that separates exactly 1 blue cell.

Wait, actually, we need the entire partition to be unique, not just the guillotine cuts. There might be non-guillotine partitions that are also valid.

But if we can show that the only valid partition is the one obtained by the forced guillotine cuts, then it's unique.

Let me think about a specific construction.

Construction: "Staircase" of 1-wide strips.

Consider an n×n grid. Place blue cells as follows:
- Row 1, column 1: blue. (1 blue cell)
- Row 1, columns 2 to n: non-blue. Row 2, column 1: non-blue. These non-blue cells must join the (1,1) rectangle.

Wait, this doesn't scale well. Let me think differently.

Let me consider the "peeling" construction:

Place 1 blue cell at (1, 1). The rest of row 1 and column 1 must join (1,1)'s rectangle. So (1,1)'s rectangle is the entire first row and first column? No, it must be a rectangle. So it's either the first row (1×n) or the first column (n×1) or a k×l rectangle including (1,1).

Hmm, this is ambiguous. Let me think more carefully.

Actually, let me think about a construction where the partition is a "staircase" of rectangles, each being a 1×k strip.

Consider the following partition of an n×n grid into 101 rectangles:
- R1 = row 1, columns 1 to a1 (1×a1 strip)
- R2 = column a1, rows 2 to a2 (actually this doesn't work as a staircase)

Let me think about a "staircase partition" more carefully.

A staircase partition: 
- R1: rows 1 to r1, column 1 (r1×1 strip)
- R2: row r1+1, columns 1 to c2 (1×c2 strip)
- R3: rows r1+2 to r3, column c2 (actually this is getting complicated)

Let me try a specific example. Consider a 3×3 grid partitioned as:
- R1: {(1,1), (2,1), (3,1)} (column 1, 3×1)
- R2: {(1,2), (1,3)} (row 1, columns 2-3, 1×2)
- R3: {(2,2), (3,2), (3,3)} ... no, this isn't a rectangle.

Let me try:
- R1: {(1,1), (2,1)} (2×1)
- R2: {(1,2), (1,3)} (1×2)
- R3: {(2,2)} (1×1)
- R4: {(2,3), (3,3)} (2×1)
- R5: {(3,1), (3,2)} (1×2)

Blue cells at (1,1), (1,2), (2,2), (2,3), (3,1). 5 blue cells in 3×3.

Is this partition unique? Let me check.

Blue: (1,1), (1,2), (2,2), (2,3), (3,1). Non-blue: (1,3), (2,1), (3,2), (3,3).

Wait, (2,1) is non-blue but it's in R1 with (1,1). (1,3) is non-blue in R2 with (1,2). (3,2) is non-blue in R5 with (3,1). (3,3) is non-blue in R4 with (2,3).

Let me check if there's another valid partition.

(2,1) must join a rectangle with 1 blue cell. Adjacent blue: (1,1), (3,1). 
- Join (1,1): rectangle {(1,1), (2,1)}: 1 blue. Valid.
- Join (3,1): rectangle {(2,1), (3,1)}: 1 blue. Valid.
Two options. Not unique. ✗

So this doesn't work either. The issue is that (2,1) is between two blue cells in the same column.

For uniqueness, we need: no non-blue cell is between two blue cells in the same row or column (unless there's a constraint that forces it one way).

Wait, but in the 2×2 block example that worked, (1,3) was adjacent to only one blue cell (1,2), and (3,1) was adjacent to only one blue cell (2,1). The non-blue cells on the "boundary" were each adjacent to only one blue cell.

So the key insight might be: every non-blue cell must be "forced" to join exactly one blue cell's rectangle, and this happens when the non-blue cell is on the "boundary" of the blue region, adjacent to only one blue cell (or more precisely, can only extend one blue cell's rectangle).

Let me think about this more carefully. 

In the 2×2 block example (3×3 grid, blue at (1,1), (1,2), (2,1), (2,2)):
- (1,3) is adjacent to (1,2) only (among blue cells). Forced to join (1,2).
- (2,3) is adjacent to (2,2) only. Forced.
- (3,1) is adjacent to (2,1) only. Forced.
- (3,2) is adjacent to (2,2) only (among blue cells; (3,1) is not blue). Forced.
- (3,3) is adjacent to (3,2) and (2,3), both non-blue. But (3,2) is in (2,2)'s rectangle and (2,3) is in (2,2)'s rectangle. So (3,3) joins (2,2)'s rectangle. Forced.

So the non-blue cells are "peeled" from the outside in, each forced to join the unique adjacent blue cell's rectangle.

This suggests a construction: place blue cells in a "block" (rectangle) and let the non-blue cells around it be forced to join.

For a k×k block of blue cells in an n×n grid (k < n), the non-blue cells form an L-shaped border. Each non-blue cell on the border is adjacent to exactly one blue cell (the one on the edge of the block), except for the "corner" non-blue cells.

Wait, let me think about a k×k block at the top-left corner of an n×n grid. Non-blue cells: rows 1 to k, columns k+1 to n (right strip), and rows k+1 to n, columns 1 to n (bottom strip).

Cell (1, k+1): adjacent to (1, k) [blue]. Forced to join (1, k).
Cell (2, k+1): adjacent to (2, k) [blue]. Forced.
...
Cell (k, k+1): adjacent to (k, k) [blue]. Forced.
Cell (k+1, 1): adjacent to (k, 1) [blue]. Forced.
...
Cell (k+1, k): adjacent to (k, k) [blue]. But (k, k) is also adjacent to (k, k+1) which is non-blue. 

Wait, (k+1, k) is adjacent to (k, k) [blue] and (k+1, k-1) [non-blue] and (k+1, k+1) [non-blue]. So (k+1, k) can only join (k, k        — AI历史解题过程（thinking）
#   polymath_01445         — 题目ID

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
  <problem_id>polymath_01445</problem_id>
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

One hundred and one of the squares of an $n\times n$ table are colored blue. It is known that there exists a unique way to cut the table to rectangles along boundaries of its squares with the following property: every rectangle contains exactly one blue square. Find the smallest possible $n$.

## Standard Solution

1. **Initial Setup and Assumption:**
   - We are given an \( n \times n \) table with 101 blue squares.
   - There exists a unique way to cut the table into rectangles such that each rectangle contains exactly one blue square.
   - We need to find the smallest possible \( n \).

2. **Verification for \( n = 101 \):**
   - Consider a \( 101 \times 101 \) table.
   - Color the top row entirely blue, resulting in 101 blue squares.
   - This configuration ensures that each row and column has at most one blue square, making it possible to partition the table uniquely into \( 1 \times 101 \) rectangles, each containing exactly one blue square.

3. **Lemma 1:**
   - **Statement:** For a blue square and its non-blue neighbor, there exists a way to cut the table into rectangles which partitions these two squares into the same rectangle.
   - **Proof:**
     - Assume the blue square and its non-blue neighbor are in the same row (otherwise, rotate the board by 90 degrees).
     - Partition the non-fallow rows (rows with blue squares) into \( 1 \times k \) rectangles, each containing exactly one blue square.
     - Ensure the two squares (blue and non-blue neighbor) are in the same rectangle.
     - Collapse the fallow rows (rows without blue squares) into the existing rectangles by adding each square in a fallow row to the first rectangle below it (or above it if there are none below).
     - This ensures a unique partitioning, proving the lemma. \(\blacksquare\)

4. **Corollary:**
   - **Statement:** The set of blue squares in any row is contiguous.
   - **Proof:**
     - If not, we could partition that row into \( 1 \times k \) rectangles in more than one way.
     - Proceeding as described in Lemma 1 would result in at least two possible ways to partition the grid, contradicting the uniqueness of the partitioning. \(\blacksquare\)
   - A similar statement holds for columns.

5. **Lemma 2:**
   - **Statement:** Any non-blue square \( s \) cannot have two blue neighbors.
   - **Proof:**
     - By the corollary, we only need to prove this when the two blue neighbors are not in the same row or column.
     - Let \( n_1 \) be the blue neighbor in the same row and \( n_2 \) be the blue neighbor in the same column.
     - Use the algorithm described in Lemma 1 to get a partition with \( n_1, s \) in the same rectangle but not \( n_2 \), and another with \( n_2, s \) in the same rectangle but not \( n_1 \).
     - This results in a contradiction, proving the lemma. \(\blacksquare\)

6. **Lemma 3:**
   - **Statement:** If \( a, b \) are blue squares which aren't in the same row or the same column, then the rectangle with \( a, b \) as opposite corners is entirely blue.
   - **Proof:**
     - Assume \( a \) is lower than \( b \) and to the left of \( b \).
     - Consider the path \( a, s_1, s_2, \ldots, s_k, b \) which first goes up and then to the right, moving one step each time.
     - Let \( s_t \) be the turning point, i.e., \( s_t \) is above \( s_{t-1} \) and to the left of \( s_{t+1} \).
     - If any \( s_i \) is not blue, then \( s_t \) is not blue by the corollary.
     - Suppose \( s_t \) is not blue. Let \( 0 \le i < t \) be the largest \( i \) with \( s_i \) blue, where \( s_0 = a \) by convention.
     - Let \( t < j \le k+1 \) be the smallest \( j \) with \( s_j \) blue, where \( s_{k+1} = b \) by convention.
     - Apply the algorithm in Lemma 1 to get a partitioning where \( s_i, s_t \) are in the same rectangle but not \( s_j \), and another where \( s_j, s_t \) are in the same rectangle but not \( s_i \).
     - These give a contradiction, so all \( s_i \)'s are blue.
     - Using Lemma 2, we can prove that the entire rectangle is blue. \(\blacksquare\)

7. **Conclusion:**
   - Lemma 3 implies that the set of blue squares forms a rectangle.
   - The set of blue squares must be a \( 1 \times 101 \) rectangle, which implies \( n \ge 101 \).

Hence, the desired minimum value of \( n \) is \( \boxed{101} \).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have an $n \times n$ table with 101 squares colored blue. There exists a unique way to cut the table into rectangles along grid boundaries such that every rectangle contains exactly one blue square. Find the smallest possible $n$.

First, let me understand the problem. We need to partition the $n \times n$ grid into rectangles (with sides along grid lines) such that each rectangle contains exactly one blue cell. The partition must be unique. We want to find the smallest $n$ for which this is possible with 101 blue cells.

Let me think about what makes a partition unique.

A partition into rectangles where each rectangle has exactly one blue cell is called a "rectangular partition" or "guillotine-free rectangular partition" with the constraint.

Let me think about when such a partition is unique.

Key insight: Consider two adjacent blue cells. If they're in the same row with no other blue cells between them, and they're adjacent (horizontally), then we need to decide where to cut between them. Actually, let me think more carefully.

Let me think about this differently. Consider the partition problem. We need to cut the grid into rectangles, each containing exactly one blue cell. 

For uniqueness, let me think about what configurations force a unique partition.

Consider a row of the grid. If a row contains blue cells, the cuts in that row are constrained.

Let me think about a simpler version first. 

Actually, let me think about the structure. A partition of the grid into rectangles where each rectangle has exactly one blue cell. 

Consider two blue cells that are in the same row, say at positions (r, c1) and (r, c2) with c1 < c2. There must be a vertical cut between them somewhere. But also, the rectangles containing them might extend across multiple rows.

Let me think about when the partition is forced to be unique.

Key observation: If we have a blue cell at position (r, c), and we look at its "territory" - the rectangle containing it. The rectangle is bounded by cuts (grid lines) on all four sides.

For the partition to be unique, every cut must be forced.

Let me think about a specific construction. 

Consider placing blue cells such that the partition is forced. One natural idea: place blue cells in a "staircase" or "diagonal" pattern.

Actually, let me think about this more carefully using the concept of "forced cuts."

A cut between two adjacent cells (i,j) and (i,j+1) (a vertical cut) is forced if the blue cells on the left and right must be separated. Similarly for horizontal cuts.

Let me think about the problem in terms of a graph. Consider the grid graph. We need to partition it into rectangles, each containing exactly one blue cell. 

Actually, I think the key insight is about "dominance" and the structure of forced partitions.

Let me think about a 1D version first: a 1×n strip with k blue cells. The partition into intervals each containing one blue cell is unique if and only if... well, actually in 1D, if we have k blue cells at positions p1 < p2 < ... < pk in a 1×n strip, the partition into intervals is unique: the cut between pi and pi+1 must be at some position between pi and pi+1. But wait, there could be multiple positions. So the partition is unique only if every pair of consecutive blue cells is adjacent (pi+1 = pi + 1), in which case the cut is forced to be between them. But also the ends: the first interval starts at position 1 and the last ends at position n. Actually no—in 1D, the cuts between consecutive blue cells can be at any position between them, so uniqueness requires consecutive blue cells to be adjacent.

Wait, but that's for 1D. In 2D, the situation is more complex because rectangles can be 2D.

Let me reconsider. In 2D, the partition into rectangles is more flexible. 

Let me think about what makes a 2D rectangular partition unique.

Consider a configuration where blue cells are placed on the main diagonal: (1,1), (2,2), ..., (n,n) in an n×n grid. Is the partition unique? Each blue cell (i,i) needs its own rectangle. 

For the diagonal configuration, consider cells (i,i) and (i+1,i+1). The cell (i,i+1) is between them. It could go to either rectangle. So the partition is not unique in general.

Hmm, let me think differently.

Let me think about the problem from the perspective of the answer. We need 101 blue cells and the smallest n. 

101 is a specific number. Let me think about what configurations give unique partitions.

Key idea: A configuration where the partition is forced. 

Consider a "staircase" of blue cells. Place blue cells at positions:
(1,1), (1,2), ..., (1, a1), 
(2, a1), (2, a1+1), ..., (2, a2),
...

Hmm, this is getting complicated. Let me think about it differently.

Let me think about the concept of a "Mondrian partition" or more specifically, when is a rectangular partition unique?

A rectangular partition of a grid into rectangles is determined by the set of cuts (horizontal and vertical line segments along grid lines). 

For the partition to be unique with the constraint that each rectangle has exactly one blue cell, every cut must be forced.

Let me think about a specific type of configuration. Consider blue cells placed such that they form a "tree" structure or a specific pattern.

Actually, let me think about this problem from a competition perspective. This is likely a competition problem, and the answer is probably a specific number.

Let me think about the structure more carefully.

Consider a configuration where we have blue cells arranged in a specific pattern that forces a unique partition.

Key insight: Consider a 2×2 block. If we have two blue cells in a 2×2 block, say at (1,1) and (2,2), then we can partition in two ways: either cut vertically (giving rectangles {(1,1),(1,2)} and {(2,1),(2,2)}) or cut horizontally (giving rectangles {(1,1),(2,1)} and {(1,2),(2,2)}). Both give each rectangle one blue cell. So this is not unique.

If we have blue cells at (1,1) and (1,2) in a 1×2 or 2×2 block, then we must cut vertically between them, and this is forced.

If we have blue cells at (1,1) and (2,1), we must cut horizontally, forced.

So for uniqueness, we need to avoid "diagonal" configurations of blue cells that allow multiple partitions.

Now, let me think about a larger structure. 

Consider placing blue cells in a "comb" pattern. For instance, in a row, place blue cells at every other position. But then the cuts between them are not forced (there's a gap).

Wait, I think I need to think about this more carefully.

Let me consider the following: a partition into rectangles is unique if and only if there's no "alternating cycle" or some similar obstruction.

Actually, let me think about it from the perspective of the dual. 

Hmm, let me try a different approach. Let me think about specific constructions and count.

Construction 1: All blue cells in a single row. Say row 1, columns 1 through 101. Then n must be at least 101 (since we need 101 columns). But wait, n×n with n ≥ 101. In this case, the partition: each blue cell (1, j) for j=1,...,101 needs its own rectangle. The cells in rows 2 through n need to be assigned to some rectangle. 

If all blue cells are in row 1, then each rectangle must extend downward. The vertical cuts between consecutive blue cells are forced (they're adjacent, so the cut is between column j and j+1). But the horizontal extent: each rectangle is a column strip from row 1 to row n, containing one blue cell. But wait, what about columns beyond 101? If n > 101, there are columns 102 through n with no blue cells. Those cells need to be part of some rectangle, but every rectangle must have exactly one blue cell. So the cells in columns 102 through n can't form valid rectangles (no blue cell). So we need n = 101 and all cells in the grid are in columns 1-101. But then each rectangle is a column of height n = 101, containing one blue cell at row 1. Is this unique? 

The vertical cuts are forced (between adjacent blue cells). The left and right boundaries are the grid edges. The top and bottom are grid edges. So yes, each rectangle is a full column, and this is unique. But n = 101 and we use 101 blue cells in a single row. This gives n = 101.

But can we do better? Can we use a 2D arrangement to get a smaller n?

Construction 2: Use multiple rows. If we use 2 rows, we can fit more blue cells per column-width. But we need to ensure uniqueness.

Let me think about a 2-row arrangement. Say we have blue cells in rows 1 and 2. Consider columns where row 1 has a blue cell and columns where row 2 has a blue cell. 

If column j has a blue cell in row 1 only, and column j+1 has a blue cell in row 2 only, then we have a diagonal situation, which creates ambiguity.

So for uniqueness, we need to avoid such diagonal configurations. 

One way: in each column, either both rows have blue cells, or neither. If both rows of a column have blue cells, we cut horizontally between rows 1 and 2, giving two 1×1 rectangles (if the column is isolated) or two 1×k rectangles.

Wait, but if both cells in a column are blue, we need a horizontal cut between them. Then each gets its own rectangle. The rectangle for (1,j) extends left/right until it hits a vertical cut, and the rectangle for (2,j) extends left/right until it hits a vertical cut. But the vertical cuts for row 1 and row 2 might be different!

Hmm, this is getting complicated. Let me think about it differently.

If we have a 2×n grid with blue cells at (1,j) and (2,j) for j = 1, ..., k (so 2k blue cells), and we need n ≥ k. The horizontal cut between rows 1 and 2 is forced (each rectangle needs exactly one blue cell, and if a rectangle spans both rows in a column with two blue cells, it would have 2 blue cells). Wait, not necessarily—a rectangle spanning both rows might span multiple columns and have blue cells in both rows.

Let me reconsider. If we have blue cells at (1,1), (1,2), (2,1), (2,2) in a 2×2 grid, we need to partition into 4 rectangles each with one blue cell. The only way is to cut both horizontally and vertically, giving 4 1×1 rectangles. This is unique.

If we have blue cells at (1,1), (1,2), (2,1), (2,2) in a 2×3 grid (extra column 3 with no blue cells), we need the cells in column 3 to be part of some rectangle. But every rectangle needs exactly one blue cell. So (1,3) must be in a rectangle with exactly one blue cell. It could join the rectangle of (1,2) (extending it to the right) or (2,2)'s rectangle (but that would require the rectangle to span both rows, which would include (1,2) too if it also spans... no, a rectangle is contiguous). 

Actually, (1,3) could be in the rectangle containing (1,2), extending it to a 1×2 rectangle covering (1,2) and (1,3). Similarly, (2,3) could be in the rectangle containing (2,2). But also, (1,3) and (2,3) could form a 2×1 rectangle—but that has no blue cell, which is invalid. So (1,3) must join some rectangle with a blue cell, and (2,3) must join some rectangle with a blue cell. The only options are: (1,3) joins (1,2)'s rectangle, (2,3) joins (2,2)'s rectangle. Or... could (1,3) join (2,2)'s rectangle? That would require a rectangle covering (1,3) and (2,2), which would be the 2×2 block (1,2),(1,3),(2,2),(2,3), containing 2 blue cells. Invalid. So the only option is (1,3) joins (1,2) and (2,3) joins (2,2). This is forced, so unique.

OK so this seems to work. The partition is: cut horizontally between rows 1 and 2, cut vertically between columns 1 and 2, and columns 2-3 are together (no vertical cut between 2 and 3). So rectangles are: {(1,1)}, {(2,1)}, {(1,2),(1,3)}, {(2,2),(2,3)}. Each has one blue cell. Unique.

But wait, could we also cut vertically between columns 2 and 3? Then we'd have rectangles: {(1,1)}, {(2,1)}, {(1,2)}, {(2,2)}, and then (1,3) and (2,3) form a 2×1 rectangle with no blue cell. Invalid. So no, we can't cut there. The partition is unique.

Now, what if we have a 2×n grid with blue cells at (1,j) and (2,j) for j=1,...,k, and n > k? The cells in columns k+1 through n must be assigned. By the same logic, (1, k+1) must join (1, k)'s rectangle, (2, k+1) must join (2, k)'s rectangle, and so on. So the partition is unique: horizontal cut between rows, vertical cuts between columns 1-2, 2-3, ..., (k-1)-k, and no cuts beyond column k. Each rectangle in column j (for j < k) is 1×1, and column k's rectangles extend to the right edge.

But this uses 2k blue cells in a 2×n grid with n ≥ k. To get 101 blue cells, we need 2k = 101, but 101 is odd. So we can't use exactly 2k = 101 with this symmetric pattern.

Let me think about asymmetric patterns. 

What if we use a pattern where some columns have 2 blue cells and some have 1?

Consider a 2×n grid. In some columns, both cells are blue; in some, only one is blue; in some, neither.

For uniqueness, we need to be careful about columns with only one blue cell.

If column j has a blue cell only in row 1 (not row 2), and column j+1 has a blue cell only in row 2 (not row 1), we get a diagonal configuration that might create ambiguity.

Let me think about this. Say we have a 2×2 grid with blue at (1,1) and (2,2). As I noted, this has two valid partitions (vertical cut or horizontal cut). Not unique.

So we need to avoid having a column with blue only in row 1 adjacent to a column with blue only in row 2.

What if all single-blue columns have the blue in the same row? Say columns 1 through a have blue in row 1 only, and columns a+1 through b have blue in both rows, and columns b+1 through c have blue in row 1 only. Wait, but then between the "both" section and the "row 1 only" section, we might have issues.

Hmm, let me think about this more carefully.

Actually, let me think about a cleaner approach. Let me consider the problem as follows:

We want to find a configuration of 101 blue cells in an n×n grid such that the rectangular partition (each rectangle has exactly one blue cell) is unique, and n is minimized.

Let me think about what constraints uniqueness imposes.

Claim: The partition is unique if and only if there is no "alternating rectangle" — a 2×2 subgrid where the blue cells are at opposite corners (a "checkerboard" pattern), and additionally, the partition is "locally forced" everywhere.

Actually, I think the condition for uniqueness is more subtle. Let me think about it in terms of the structure of the partition.

A rectangular partition is determined by its cuts. A cut is a horizontal or vertical segment along a grid line that separates two rectangles. 

For the partition to be unique, every cut must be "forced" — meaning that without it, some rectangle would contain 0 or ≥2 blue cells.

Let me think about necessary conditions for a cut to be forced.

A vertical cut between columns j and j+1, spanning rows r1 to r2, is forced if removing it would cause some rectangle to have 0 or ≥2 blue cells. 

This is getting complex. Let me try to think about the problem from the answer's perspective.

We need 101 blue cells. 101 = 10² + 1 = 10*10 + 1. Or 101 is prime. 

Hmm, let me think about what n could be. If we use a single row, n = 101. If we use 2 rows, we might get n ≈ 51. If we use k rows, we might get n ≈ 101/k + something.

But the constraint is that the partition must be unique, which limits how we can arrange blue cells.

Let me think about a "staircase" construction.

Consider placing blue cells in a staircase pattern. For example:
- Row 1: columns 1, 2, ..., a1
- Row 2: columns a1, a1+1, ..., a2
- Row 3: columns a2, a2+1, ..., a3
- ...

Where each row shares one column with the next (the "turn" column has blue cells in two adjacent rows).

Wait, but if a column has blue cells in two adjacent rows, we need a horizontal cut between them, which is fine.

Let me think about a specific staircase. Consider an L-shaped arrangement:
- Row 1: columns 1 through a (a blue cells)
- Column a: rows 1 through b (b blue cells, but (1,a) is shared, so a + b - 1 blue cells)

This gives a + b - 1 blue cells in a grid that's max(a, b) × max(a, b) roughly. But actually the grid is b × a (b rows, a columns), and we need it to be n × n, so n = max(a, b).

Hmm wait, but we need to check uniqueness.

Let me consider a specific example: blue cells at (1,1), (1,2), (1,3), (2,3), (3,3) in a 3×3 grid. That's 5 blue cells. Is the partition unique?

The blue cells are in an L-shape. Let me figure out the partition.

Row 1 has blue at columns 1, 2, 3. Column 3 has blue at rows 1, 2, 3.

Cell (1,1): needs a rectangle with only this blue cell. 
Cell (1,2): needs a rectangle with only this blue cell.
Cell (1,3): needs a rectangle with only this blue cell.
Cell (2,3): needs a rectangle with only this blue cell.
Cell (3,3): needs a rectangle with only this blue cell.

Non-blue cells: (2,1), (2,2), (3,1), (3,2).

(2,1) must be in a rectangle with exactly one blue cell. The only blue cell it could be with is (1,1) (if the rectangle spans rows 1-2, column 1). So (2,1) joins (1,1)'s rectangle: rectangle is {(1,1), (2,1)}.

(2,2) must be in a rectangle with exactly one blue cell. Options: join (1,2)'s rectangle (spanning rows 1-2, column 2), or join (1,1)'s rectangle (but that already has (1,1) and (2,1), so adding (2,2) would make it a 2×2 rectangle with 1 blue cell... wait, (1,1) is blue, so a 2×2 rectangle {(1,1),(1,2),(2,1),(2,2)} has 2 blue cells. Invalid. So (2,2) can join (1,2)'s rectangle: {(1,2), (2,2)}. Or could (2,2) join (2,3)'s rectangle? That would be {(2,2), (2,3)}, a 1×2 rectangle with 1 blue cell (2,3). Valid! So there are two options for (2,2).

Hmm, so the partition might not be unique. Let me check.

Option A: (2,2) joins (1,2). Rectangles so far: {(1,1),(2,1)}, {(1,2),(2,2)}, {(1,3)}, {(2,3)}, {(3,3)}.
Then (3,1) and (3,2) need rectangles. (3,1) could join {(1,1),(2,1)} extending to row 3: {(1,1),(2,1),(3,1)} - 1 blue cell. Valid. (3,2) could join {(1,2),(2,2)} extending to row 3: {(1,2),(2,2),(3,2)} - 1 blue cell. Valid. 
So partition: {(1,1),(2,1),(3,1)}, {(1,2),(2,2),(3,2)}, {(1,3)}, {(2,3)}, {(3,3)}. Each has 1 blue cell. Valid.

Option B: (2,2) joins (2,3). Rectangles: {(1,1),(2,1)}, {(1,2)}, {(1,3)}, {(2,2),(2,3)}, {(3,3)}.
Then (3,1) joins {(1,1),(2,1)} → {(1,1),(2,1),(3,1)}. (3,2) needs a rectangle. Could join {(2,2),(2,3)} extending to row 3: {(2,2),(2,3),(3,2),(3,3)} - 2 blue cells. Invalid. Could join {(1,2)} extending to row 3: {(1,2),(2,2),(3,2)} - but (2,2) is already in {(2,2),(2,3)}. Conflict. 

Hmm wait, I need to be more careful. In option B, (2,2) is in the rectangle {(2,2),(2,3)}. So (3,2) can't join (1,2)'s rectangle by going through (2,2) (since (2,2) is taken). (3,2) could form a rectangle with (3,1) and (3,3)? (3,1) is in {(1,1),(2,1),(3,1)}. So (3,2) is isolated. It could be a 1×1 rectangle, but that has 0 blue cells. Invalid. 

So (3,2) must join some rectangle with a blue cell. The adjacent rectangles are: {(1,1),(2,1),(3,1)} (has blue at (1,1)), {(2,2),(2,3)} (has blue at (2,3)), {(3,3)} (has blue at (3,3)). 

(3,2) joining {(3,3)}: rectangle {(3,2),(3,3)} - 1 blue cell. Valid!
(3,2) joining {(1,1),(2,1),(3,1)}: would need rectangle covering (3,1) and (3,2), so at least row 3, columns 1-2. But (2,1) is in this rectangle, so the rectangle is at least rows 1-3, columns 1-2 = {(1,1),(1,2),(2,1),(2,2),(3,1),(3,2)}. But (1,2) is blue and in a different rectangle, and (2,2) is in {(2,2),(2,3)}. Conflict.

So in option B, (3,2) joins {(3,3)}: rectangle {(3,2),(3,3)}. Then partition: {(1,1),(2,1),(3,1)}, {(1,2)}, {(1,3)}, {(2,2),(2,3)}, {(3,2),(3,3)}. Each has 1 blue cell. Valid!

So we have at least two valid partitions (option A and option B). The L-shape doesn't give uniqueness.

OK so the staircase/L-shape doesn't work directly. Let me think about what does work.

Going back to the "full columns" idea: if every column that has blue cells has blue cells in all rows (of the relevant subgrid), then the horizontal cuts are forced and we just need vertical cuts, which are forced if blue cells are adjacent.

But that uses n² blue cells for an n×n grid, which is too many.

Let me think about a different approach. What if we use a "comb" pattern?

Consider a grid where we have some columns fully filled with blue cells and some columns empty. But empty columns can't exist (their cells need to join a rectangle with a blue cell).

Hmm, let me reconsider. The key issue is: how to arrange blue cells in 2D to minimize n while maintaining uniqueness.

Let me think about the problem differently. 

Consider the grid as a graph where we need to find a unique rectangular partition. 

I think the key insight is about "separating" blue cells. Two blue cells need to be separated by a cut. A cut is forced if there's no alternative.

Let me think about a "path" of blue cells. Consider blue cells arranged in a path (each consecutive pair is adjacent). For example, a snake-like path through the grid. 

If blue cells form a path where each consecutive pair is adjacent (horizontally or vertically), then between each consecutive pair, there must be a cut. But is the partition unique?

Consider a path: (1,1), (1,2), (2,2), (2,3), (3,3), ... This is a staircase path. Between (1,1) and (1,2), there's a vertical cut. Between (1,2) and (2,2), there's a horizontal cut. Etc.

But the issue is that the non-blue cells need to be assigned, and there might be multiple ways.

Let me think about a Hamiltonian path of blue cells. If all n² cells are blue, then each rectangle is 1×1, and the partition is trivially unique. But we need exactly 101 blue cells, not n².

Let me think about the problem from the competition answer perspective. 

For 101 blue cells, we want the smallest n. 

I think the answer might be related to the following construction: arrange blue cells in a "cross" or "T" or some specific shape.

Actually, let me think about this more carefully. Let me consider the problem of when a rectangular partition is unique.

Theorem (informal): A rectangular partition of a grid into rectangles each containing exactly one blue cell is unique if and only if there is no "alternating cycle" in the "conflict graph."

Actually, I think the right framework is this: Consider the grid graph. Two adjacent cells (sharing an edge) are "separated" if there's a cut between them. We need to determine which edges of the grid graph are cuts. 

A valid partition is a set of cuts (edges of the grid graph to remove) such that:
1. The resulting regions are all rectangles.
2. Each region contains exactly one blue cell.

For uniqueness, there should be exactly one such set of cuts.

Now, an edge between cells (i,j) and (i,j+1) must be a cut if they're in different "blue regions." An edge must NOT be a cut if cutting it would create a non-rectangle or if the two cells are in the same blue region.

Let me think about necessary conditions. If two blue cells are in the same row with no blue cell between them, and they're not adjacent, then the cut between them can be at any position between them. So for uniqueness, either they're adjacent (cut is forced at one specific position) or there's some other constraint.

Wait, actually, that's not quite right either, because the rectangles might not be single rows.

Let me think about a cleaner characterization.

I think the key insight is:

Lemma: If two blue cells are "visible" to each other (in the same row or column with no other blue cell between them), and they are not adjacent, then the partition is not unique.

Proof: If blue cells A and B are in the same row with no blue cell between them, and they're not adjacent, then there's at least one non-blue cell between them. The cut separating A's rectangle from B's rectangle can be placed at any of the positions between A and B. But wait, the cut might not be a simple vertical line—it could be more complex if the rectangles aren't single-row rectangles.

Hmm, actually this isn't quite right because the rectangles could span multiple rows.

Let me think about a specific case. Blue cells at (1,1) and (1,3) in a 1×3 grid. The cell (1,2) must be in one of the two rectangles. Either {(1,1),(1,2)} and {(1,3)}, or {(1,1)} and {(1,2),(1,3)}. Both valid, so not unique. ✓

Blue cells at (1,1) and (1,3) in a 2×3 grid. Cells (1,2), (2,1), (2,2), (2,3) are non-blue. 
- (1,2) can join (1,1) or (1,3).
- (2,1) can join (1,1).
- (2,3) can join (1,3).
- (2,2) can join (1,1) (via (2,1)) or (1,3) (via (2,3)) or (1,2) (but (1,2) is not blue).

Actually, (2,2) must be in a rectangle with exactly one blue cell. The rectangle containing (2,2) must also contain a blue cell. The blue cells are (1,1) and (1,3). A rectangle containing (2,2) and (1,1) would need to cover at least rows 1-2 and columns 1-2, i.e., {(1,1),(1,2),(2,1),(2,2)}. This has 1 blue cell. Valid. A rectangle containing (2,2) and (1,3) would need to cover at least rows 1-2 and columns 2-3, i.e., {(1,2),(1,3),(2,2),(2,3)}. This has 1 blue cell. Valid.

So (2,2) can go with either (1,1) or (1,3). Not unique. ✓

So the lemma seems to hold: if two blue cells are visible to each other (same row or column, no blue cell between) and not adjacent, the partition is not unique.

Wait, but I should check: is the converse true? If every pair of blue cells that are visible to each other are adjacent, is the partition unique?

This would mean: in each row, the blue cells form a contiguous block (since any two in the same row must be adjacent, by induction they form a contiguous block). Similarly for each column.

Wait, that's not quite right. "Visible" means same row/column with no other blue cell between. If blue cells in a row are at positions 1, 2, 4, then 2 and 4 are visible (no blue cell at position 3) and not adjacent. So this violates the condition. So the condition requires that in each row, blue cells form a contiguous block. Similarly for each column.

So the condition is: in every row, the blue cells form a contiguous interval, and in every column, the blue cells form a contiguous interval.

Is this sufficient for uniqueness? Let me check.

Consider blue cells at (1,1), (1,2), (2,1), (2,2) in a 2×2 grid. Each row has a contiguous block, each column has a contiguous block. The partition: cut horizontally and vertically, giving 4 1×1 rectangles. Is this unique? 

Could we have a different partition? The only other option would be to not cut somewhere. If we don't cut horizontally, then rows 1 and 2 are together, and we'd have a 2×1 or 2×2 rectangle with 2 blue cells. Invalid. If we don't cut vertically, similar issue. So yes, unique. ✓

Consider blue cells at (1,1), (1,2), (2,2), (2,3) in a 2×3 grid. Row 1: blue at 1,2 (contiguous). Row 2: blue at 2,3 (contiguous). Column 1: blue at 1 only. Column 2: blue at 1,2 (contiguous). Column 3: blue at 2 only. So the condition is satisfied.

Is the partition unique? Blue cells: (1,1), (1,2), (2,2), (2,3). Non-blue: (2,1), (1,3).

(2,1) must join a rectangle with a blue cell. Adjacent blue cell: (1,1). Rectangle {(1,1),(2,1)}: 1 blue cell. Could (2,1) join (1,2)? Rectangle would be at least {(1,1),(1,2),(2,1),(2,2)}: 2 blue cells. Invalid. Could (2,1) join (2,2)? Rectangle {(2,1),(2,2)}: 1 blue cell. Valid! So (2,1) has two options.

So the partition is NOT unique, even though the contiguity condition is satisfied. So the contiguity condition is necessary but not sufficient.

Hmm. So my lemma gives a necessary condition but not a sufficient one.

Let me reconsider. The issue in the above example is that (2,1) can join either (1,1) or (2,2). This is because (1,1) and (2,2) are at "opposite corners" of a 2×2 block, creating ambiguity.

So the condition for uniqueness is stronger. Let me think about what the right condition is.

I think the right condition involves the concept of a "grid intersection graph" or something similar.

Let me think about it differently. Consider the "row intervals" and "column intervals" of blue cells. 

In the example above: Row 1 has blue in columns [1,2]. Row 2 has blue in columns [2,3]. Column 1 has blue in rows [1,1]. Column 2 has blue in rows [1,2]. Column 3 has blue in rows [2,2].

The issue is that row 1's interval [1,2] and row 2's interval [2,3] overlap at column 2 but are "shifted." This creates the diagonal ambiguity.

For uniqueness, I think we need that the row intervals are "nested" or "non-overlapping" in a specific way.

Actually, let me think about this problem from a different angle. Let me consider the concept of a "staircase" partition.

A staircase partition is one where the rectangles form a staircase pattern. 

Hmm, let me try to think about what configurations give unique partitions, and then optimize for 101 blue cells.

Let me consider the following type of configuration: blue cells arranged in a "Young diagram" or "Ferrers diagram" shape.

A Ferrers diagram with row lengths λ1 ≥ λ2 ≥ ... ≥ λk. Blue cells are at (i, j) for 1 ≤ j ≤ λi. The total number of blue cells is λ1 + λ2 + ... + λk.

For this configuration:
- Each row has a contiguous block of blue cells (columns 1 to λi).
- Each column j has blue cells in rows 1 to max{i : λi ≥ j}, which is contiguous.

Now, is the partition unique for a Ferrers diagram?

Let me check with the example: λ = (2, 1), i.e., blue at (1,1), (1,2), (2,1). This is a 2×2 grid with 3 blue cells.

Non-blue cell: (2,2). (2,2) must join a rectangle with one blue cell. Options:
- Join (1,2): rectangle {(1,2),(2,2)}: 1 blue cell. Valid.
- Join (2,1): rectangle {(2,1),(2,2)}: 1 blue cell. Valid.
- Join (1,1): rectangle would be {(1,1),(1,2),(2,1),(2,2)}: 3 blue cells. Invalid.

So (2,2) has two options. Not unique.

So Ferrers diagrams don't automatically give uniqueness either.

Hmm. Let me think about what does guarantee uniqueness.

Let me go back to the "full rectangle" idea. If the blue cells form a full a×b rectangle, then the partition is unique: cut into a×b unit rectangles. But this uses ab blue cells, and n = max(a, b), so we'd need ab = 101 with n = max(a,b) minimized. Since 101 is prime, the only factorization is 1×101, giving n = 101. Same as the single row.

So we need a non-rectangular arrangement. Let me think about what shapes work.

Let me consider the following: a "staircase" where each step is a full rectangle.

Actually, let me think about the problem more carefully. Let me consider the concept of "guillotine cuts."

A guillotine cut is a cut that goes all the way across a rectangle. A partition is a guillotine partition if it can be obtained by a sequence of guillotine cuts.

For uniqueness, I think we need the partition to be "forced" at every step.

Let me think about a recursive structure. 

Consider a grid where we can make a forced guillotine cut, splitting it into two sub-grids, each of which has a forced guillotine cut, etc.

A guillotine cut is forced if one side has exactly one "row" or "column" of blue cells that can't be split.

Hmm, this is getting complicated. Let me try a different approach: think about small cases and find a pattern.

Let me think about what the answer might be. We need 101 blue cells. The answer is the smallest n.

If we could use a √101 × √101 arrangement, n would be about 11. But 101 is prime, so we can't make a rectangle.

Let me think about a "near-square" arrangement. 101 = 10 × 10 + 1 = 10² + 1. Or 101 = 9 × 11 + 2. Or 101 = 7 × 14 + 3. Etc.

Actually, let me think about the problem differently. Let me consider the following construction:

Place blue cells in a "staircase" pattern where each row has one more (or one fewer) blue cell than the previous, and the rows are "aligned" in a specific way.

Wait, I showed that Ferrers diagrams don't work. Let me think about what additional structure is needed.

Let me reconsider the problem. The key difficulty is assigning non-blue cells to rectangles uniquely. 

What if there are no non-blue cells? Then n² = 101, but 101 isn't a perfect square. So there must be non-blue cells.

What if there's exactly one non-blue cell? Then n² = 102. 102 isn't a perfect square either. n² - 101 non-blue cells. For n = 11, n² = 121, so 20 non-blue cells. For n = 10, n² = 100 < 101. So n ≥ 11.

Wait, n = 10 gives 100 cells, which is less than 101. So n ≥ 11.

Can we achieve n = 11? We'd have 121 cells, 101 blue, 20 non-blue. We need to arrange 101 blue cells in an 11×11 grid with a unique partition.

Hmm, let me think about whether n = 11 is achievable.

Actually wait. Let me reconsider. Maybe the answer is larger than 11.

Let me think about upper bounds on the number of blue cells for a unique partition in an n×n grid.

For a unique partition, I claim that the blue cells must form a "staircase" shape (in a generalized sense), and the maximum number of blue cells for a unique partition in an n×n grid is related to n.

Let me think about what the maximum number of blue cells is such that the partition is unique.

From the necessary condition (contiguous in each row and column), the blue cells form a "polyomino" that is "convex" (row-convex and column-convex). But we showed this isn't sufficient.

Let me think about a stronger condition. 

I think the right condition for uniqueness is that the blue cells form a "staircase" where the row intervals are "nested" — i.e., the intervals are either identical or one is completely to the left/right of the other, or they share an endpoint in a specific way.

Actually, let me think about this more carefully with a key example.

Consider blue cells forming a "cross" or "plus" shape. Or consider a specific construction that I know works.

Let me think about the "staircase" construction more carefully.

Consider the following arrangement in an n×n grid:
- Row 1: columns 1, 2, ..., n (all blue)
- Row 2: column n only
- Row 3: column n only
- ...
- Row n: column n only

Total blue cells: n + (n-1) = 2n - 1.

Is the partition unique? Row 1 has all blue cells, columns 1 through n-1 have blue only in row 1, column n has blue in all rows.

For row 1, the blue cells are contiguous (columns 1 to n). For each column, blue cells are contiguous (column j, j < n: just row 1; column n: rows 1 to n).

Non-blue cells: (i, j) for 2 ≤ i ≤ n, 1 ≤ j ≤ n-1.

Cell (2, 1) must join a rectangle with one blue cell. The only adjacent blue cell is (1, 1). Rectangle {(1,1), (2,1)}: 1 blue cell. Could (2,1) join (1,2)? Rectangle would include (1,1), (1,2), (2,1), and possibly (2,2): 2 blue cells. Invalid. Could (2,1) join (2,n)? Not contiguous. So (2,1) must join (1,1).

Similarly, (2, j) for j < n must join (1, j). So the rectangles for row 1 blue cells extend down to row 2.

But wait, (2, j) joins (1, j), making rectangle {(1,j), (2,j)}. Then (3, j) must join a rectangle with one blue cell. It can join {(1,j), (2,j)} extending to row 3: {(1,j), (2,j), (3,j)}: 1 blue cell. Or join (3, n) if j = n-1... (3, n-1) and (3, n): rectangle {(3, n-1), (3, n)}: but (3, n) is blue, so 1 blue cell. But (3, n-1) is non-blue. Is this valid? The rectangle {(3, n-1), (3, n)} has 1 blue cell (at (3,n)). But we need to check if this is a valid rectangle in the partition. (3, n) is blue and needs its own rectangle. If (3, n-1) joins (3, n)'s rectangle, then (3, n)'s rectangle is {(3, n-1), (3, n)} or larger. But (2, n) is also blue and needs its own rectangle. 

Hmm, let me be more careful. Let me consider n = 3: blue at (1,1), (1,2), (1,3), (2,3), (3,3). 5 blue cells in a 3×3 grid. Non-blue: (2,1), (2,2), (3,1), (3,2).

This is the L-shape I considered earlier, and I showed it's NOT unique (two valid partitions).

So the "L-shape" doesn't work. The issue is that (2,2) can join either (1,2) or (2,3).

So what arrangement does work?

Let me think about what makes the L-shape fail. The problem is at the "corner" of the L, where (1,2) and (2,3) are diagonal, and (2,2) is the cell between them that can go either way.

To fix this, I need to prevent (2,2) from having two options. One way: make (2,2) blue. Then the L-shape becomes a 2×2 block plus an extension, and we need to check uniqueness.

Blue at (1,1), (1,2), (1,3), (2,2), (2,3), (3,3) in a 3×3 grid. 6 blue cells. Non-blue: (2,1), (3,1), (3,2).

Row 1: [1,3] contiguous. Row 2: [2,3] contiguous. Row 3: [3,3] contiguous.
Column 1: [1,1]. Column 2: [1,2]. Column 3: [1,3]. All contiguous.

(2,1) must join a rectangle with one blue cell. Adjacent blue: (1,1). Rectangle {(1,1),(2,1)}: 1 blue. Could join (2,2)? Rectangle {(2,1),(2,2)}: 1 blue. Valid! So (2,1) has two options. Not unique.

Hmm. So even adding (2,2) doesn't fix it because (2,1) can join either (1,1) or (2,2).

The issue is that (1,1) and (2,2) are diagonal in the 2×2 block {(1,1),(1,2),(2,1),(2,2)}, with (1,2) also blue. So (2,1) can join (1,1) (making a vertical 2×1) or join (2,2) (making a horizontal 1×2), and both are valid because (1,2) is in its own rectangle.

So the problem is fundamentally about 2×2 blocks with 3 blue cells (one non-blue cell). The non-blue cell can join either of its two blue neighbors (if both are blue and diagonal).

Wait, in the 2×2 block {(1,1),(1,2),(2,1),(2,2)} with (1,1), (1,2), (2,2) blue and (2,1) non-blue: (2,1) can join (1,1) (vertical pair) or (2,2) (horizontal pair). Both give rectangles with 1 blue cell. And (1,2) is separate. So not unique.

To make it unique, we need to eliminate this ambiguity. One way: make all 4 cells blue (then each is its own rectangle, forced). Another way: make only 2 cells blue, but they must be adjacent (not diagonal).

So in any 2×2 block, if there are exactly 3 blue cells, the partition is not unique (the non-blue cell has two options). If there are 2 blue cells that are diagonal, not unique. If there are 2 blue cells that are adjacent, it might be OK (the non-blue cells must join the adjacent blue cell's rectangle, but need to check globally).

So for uniqueness, we need: in every 2×2 block, the blue cells are either 0, 1, 2 (adjacent), or 4. No 2×2 block with 3 blue cells, and no 2×2 block with 2 diagonal blue cells.

Wait, but 0 blue cells in a 2×2 block is fine (those cells join other rectangles). 1 blue cell is fine. 2 adjacent is fine (potentially). 4 is fine (each is its own rectangle). 3 is bad. 2 diagonal is bad.

So the condition is: no 2×2 block has exactly 3 blue cells, and no 2×2 block has 2 diagonal blue cells.

The "no 2 diagonal blue cells in a 2×2 block" condition means: if (i,j) and (i+1,j+1) are both blue, then at least one of (i,j+1) or (i+1,j) must also be blue. Similarly for (i,j+1) and (i+1,j).

And "no 3 blue cells in a 2×2 block" means: if 3 of the 4 cells in a 2×2 block are blue, that's forbidden.

These two conditions together mean: in every 2×2 block, the number of blue cells is 0, 1, 2 (adjacent), or 4. Equivalently, the blue cells in any 2×2 block form a "connected" subset (in the sense that they don't have a diagonal pair without a connecting cell).

Wait, let me re-examine. 2 adjacent blue cells in a 2×2 block: is the partition always unique (locally)? 

Consider a 2×2 block with blue at (1,1) and (1,2), non-blue at (2,1) and (2,2). (2,1) must join (1,1) (the only adjacent blue cell). (2,2) must join (1,2) (the only adjacent blue cell). So locally, it's forced. But globally, could (2,1) join some other blue cell outside this block? Only if there's a blue cell at (3,1) or (2,0) (out of bounds). If (3,1) is blue, then (2,1) could join (3,1) instead. So we need to consider the global structure.

OK so the local conditions (no 3 in a 2×2, no 2 diagonal in a 2×2) are necessary but might not be sufficient. But let me assume they're the key conditions and see where they lead.

So the blue cells must satisfy:
1. In every 2×2 subgrid, the blue cells are not exactly 3.
2. In every 2×2 subgrid, the blue cells don't form a diagonal pair.

Condition 2 means: the blue cells form a "polyomino" that is both row-convex and column-convex (no holes in any row or column), AND additionally, the shape is "staircase-like" — the row intervals shift by at most 1 at each step.

Wait, let me think about condition 2 more carefully. No diagonal pair in any 2×2 block means: if (i,j) is blue and (i+1,j+1) is blue, then (i,j+1) or (i+1,j) is blue. This is exactly the condition that the blue cells form a "Young diagram" (Ferrers diagram) shape, or more generally, a "staircase convex" shape.

Actually, the condition "no diagonal pair in any 2×2 block" is equivalent to saying the blue region is "hv-convex" and "connected in a specific way." Let me think...

If (i,j) and (i+1,j+1) are blue but (i,j+1) and (i+1,j) are not, that's a diagonal pair. The condition forbids this. This means: if row i has blue at column j and row i+1 has blue at column j+1, then either row i also has blue at column j+1, or row i+1 also has blue at column j.

For Ferrers diagrams (row-convex, column-convex, rows are left-justified and non-increasing), this condition is automatically satisfied: if (i,j) is blue (j ≤ λi) and (i+1,j+1) is blue (j+1 ≤ λi+1 ≤ λi), then (i,j+1) is blue (j+1 ≤ λi). So Ferrers diagrams satisfy condition 2.

But we also need condition 1: no 2×2 block with exactly 3 blue cells. For a Ferrers diagram, consider the "corner" at row i where λi > λi+1. The 2×2 block at rows i, i+1 and columns λi+1, λi+1 + 1 (if λi ≥ λi+1 + 1). Wait, let me be more specific.

Consider λ = (3, 1). Blue at (1,1), (1,2), (1,3), (2,1). The 2×2 block at rows 1-2, columns 1-2: blue at (1,1), (1,2), (2,1). That's 3 blue cells. Violates condition 1!

So Ferrers diagrams with "jumps" (λi - λi+1 ≥ 2) violate condition 1.

For condition 1 to hold, we need λi - λi+1 ≤ 1 for all i (the row lengths decrease by at most 1). And also, the first row can't be too long compared to the second, etc.

Wait, let me re-examine. For a Ferrers diagram with row lengths λ1 ≥ λ2 ≥ ... ≥ λk, condition 1 (no 3 blue in any 2×2) requires: for each i, the 2×2 block at rows i, i+1 and columns λi+1, λi+1 + 1 has at most 2 blue cells (if λi ≥ λi+1 + 1). The blue cells in this block are: (i, λi+1) [blue since λi+1 ≤ λi], (i, λi+1 + 1) [blue if λi+1 + 1 ≤ λi, i.e., λi ≥ λi+1 + 1], (i+1, λi+1) [blue], (i+1, λi+1 + 1) [not blue since λi+1 + 1 > λi+1]. So if λi ≥ λi+1 + 1, the block has 3 blue cells. So we need λi ≤ λi+1 + 1, i.e., λi - λi+1 ≤ 1.

But also, consider the 2×2 block at rows i, i+1 and columns λi+1 + 1, λi+1 + 2 (if λi ≥ λi+1 + 2). Blue cells: (i, λi+1 + 1) [blue], (i, λi+1 + 2) [blue if λi ≥ λi+1 + 2], (i+1, λi+1 + 1) [not blue], (i+1, λi+1 + 2) [not blue]. That's 2 blue cells, and they're adjacent (both in row i). So this is fine.

So the only problematic 2×2 blocks are those at the "step" where λi > λi+1. And the condition is λi - λi+1 ≤ 1.

So for a Ferrers diagram, the conditions for uniqueness (assuming they're sufficient) are:
1. λi - λi+1 ≤ 1 for all i (row lengths decrease by at most 1).
2. The shape is a Ferrers diagram (which automatically satisfies condition 2).

But wait, I need to also check condition 1 for 2×2 blocks not at the "step." For a Ferrers diagram, the only 2×2 blocks with 3 blue cells are at the steps. And 2×2 blocks with 2 diagonal blue cells don't occur (as I argued). So the conditions are:
- Ferrers diagram (left-justified, non-increasing row lengths)
- λi - λi+1 ≤ 1 for all i (including λk ≥ 0, so the last row has at least λk-1 - 1 blue cells, etc.)

But wait, I also need to consider 2×2 blocks where the blue cells are in rows i, i+1 but the columns span a "step" in a different way. Let me re-examine.

For a Ferrers diagram, the blue cells in row i are columns 1 to λi. Consider a 2×2 block at rows i, i+1, columns j, j+1.

Case 1: j+1 ≤ λi+1. Then all 4 cells are blue. Fine (4 blue cells).
Case 2: j = λi+1, j+1 ≤ λi. Then (i,j), (i,j+1), (i+1,j) are blue, (i+1,j+1) is not. 3 blue cells. This is the step case, and we need λi ≤ λi+1 + 1, i.e., j+1 ≤ λi+1 + 1, i.e., λi ≤ λi+1 + 1.
Case 3: j = λi+1, j+1 > λi. Then (i,j) is blue (j = λi+1 ≤ λi), (i+1,j) is blue, (i,j+1) is not blue (j+1 > λi), (i+1,j+1) is not blue. 2 blue cells, adjacent (same column). Fine.
Case 4: j > λi+1, j+1 ≤ λi. Then (i,j), (i,j+1) are blue, (i+1,j), (i+1,j+1) are not. 2 blue cells, adjacent (same row). Fine.
Case 5: j > λi. No blue cells. Fine.

So the only problematic case is Case 2, which requires λi ≤ λi+1 + 1.

So for a Ferrers diagram, the conditions reduce to: λi - λi+1 ≤ 1 for all i (where λk+1 = 0, so λk ≤ 1, meaning the last row has at most 1 blue cell).

Wait, λk - 0 ≤ 1, so λk ≤ 1. The last row has at most 1 blue cell. And λk-1 - λk ≤ 1, so λk-1 ≤ λk + 1 ≤ 2. And so on: λi ≤ λi+1 + 1, so λ1 ≤ λ2 + 1 ≤ λ3 + 2 ≤ ... ≤ λk + (k-1) ≤ 1 + (k-1) = k.

So λ1 ≤ k, meaning the first row has at most k blue cells (where k is the number of rows). And the total number of blue cells is λ1 + λ2 + ... + λk.

To maximize the total with the constraint λi - λi+1 ≤ 1 and λi ≥ λi+1 (Ferrers) and λk ≥ 1 (at least one blue cell in the last row):

The maximum is achieved when λi - λi+1 = 1 for all i, giving λi = λk + (k - i). With λk = 1: λi = k - i + 1. So λ = (k, k-1, ..., 2, 1). Total = k + (k-1) + ... + 1 = k(k+1)/2.

And the grid size is n × n where n ≥ k (since λ1 = k) and n ≥ k (number of rows). So n = k.

Total blue cells = k(k+1)/2. We need k(k+1)/2 ≥ 101.

k(k+1)/2 ≥ 101 → k(k+1) ≥ 202 → k ≥ 14 (since 13×14 = 182 < 202, 14×15 = 210 ≥ 202).

But wait, we need exactly 101 blue cells, not at least 101. And we need the partition to be unique.

Hmm, but I've only shown these conditions are necessary. I haven't shown they're sufficient. And I've only considered Ferrers diagrams. There might be other shapes that work.

Also, I assumed the conditions (no 3 in a 2×2, no 2 diagonal in a 2×2) are sufficient for uniqueness, which I haven't proven.

Let me step back and think about this more carefully.

Actually, wait. I think I was too hasty. Let me reconsider whether the conditions are sufficient.

Let me check: Ferrers diagram with λ = (2, 1). Blue at (1,1), (1,2), (2,1). 2×2 block at rows 1-2, columns 1-2: 3 blue cells. Violates condition 1. So this is correctly identified as non-unique.

Ferrers diagram with λ = (2, 2). Blue at (1,1), (1,2), (2,1), (2,2). 4 blue cells in the only 2×2 block. Conditions satisfied. Is the partition unique? Yes, each cell is its own rectangle. ✓

Ferrers diagram with λ = (3, 2, 1). Blue at (1,1), (1,2), (1,3), (2,1), (2,2), (3,1). 6 blue cells in a 3×3 grid.

Check conditions:
- 2×2 at rows 1-2, cols 1-2: all 4 blue. ✓
- 2×2 at rows 1-2, cols 2-3: (1,2), (1,3) blue, (2,2) blue, (2,3) not blue. 3 blue cells. ✗!

So λ = (3, 2, 1) violates condition 1 (λ1 - λ2 = 1 is OK, but the 2×2 block at cols 2-3 has 3 blue cells). Wait, let me recheck.

Row 1: blue at 1, 2, 3. Row 2: blue at 1, 2. 2×2 block at rows 1-2, cols 2-3: (1,2) blue, (1,3) blue, (2,2) blue, (2,3) not blue. 3 blue cells. Yes, this violates condition 1.

But λ1 - λ2 = 3 - 2 = 1 ≤ 1. So my earlier analysis was wrong? Let me recheck.

The 2×2 block at rows 1-2, columns 2-3. λ2 = 2, so column 2 is the last blue column in row 2. The step is at column 2/3. j = λ2 = 2, j+1 = 3. λ1 = 3 ≥ 3 = j+1, so (1, 3) is blue. This is Case 2: (i, j) = (1, 2) blue, (i, j+1) = (1, 3) blue, (i+1, j) = (2, 2) blue, (i+1, j+1) = (2, 3) not blue. 3 blue cells. Condition: λ1 ≤ λ2 + 1 = 3. λ1 = 3 ≤ 3. ✓.

Wait, so the condition λi ≤ λi+1 + 1 is satisfied (3 ≤ 2 + 1 = 3), but there are still 3 blue cells in the 2×2 block. So my condition was wrong!

Let me re-derive. The 2×2 block at rows i, i+1, columns j, j+1 where j = λi+1. Blue cells: (i, j) [blue since j = λi+1 ≤ λi], (i, j+1) [blue if j+1 ≤ λi], (i+1, j) [blue since j = λi+1], (i+1, j+1) [not blue since j+1 > λi+1]. So 3 blue cells if j+1 ≤ λi, i.e., λi+1 + 1 ≤ λi, i.e., λi ≥ λi+1 + 2. And 2 blue cells if λi = λi+1 + 1 (then j+1 = λi+1 + 1 = λi, so (i, j+1) = (i, λi) is blue... wait, j+1 = λi+1 + 1. If λi = λi+1 + 1, then j+1 = λi, so (i, j+1) = (i, λi) is blue. So 3 blue cells.

Hmm wait, let me redo this. j = λi+1. (i, j+1) is blue iff j+1 ≤ λi iff λi+1 + 1 ≤ λi iff λi ≥ λi+1 + 1.

If λi = λi+1: j = λi+1 = λi. j+1 = λi + 1 > λi. So (i, j+1) is not blue. 2 blue cells: (i, j) and (i+1, j). Adjacent (same column). Fine.

If λi = λi+1 + 1: j = λi+1. j+1 = λi+1 + 1 = λi. (i, j+1) = (i, λi) is blue. 3 blue cells. Bad!

If λi ≥ λi+1 + 2: j = λi+1. j+1 = λi+1 + 1 ≤ λi. (i, j+1) is blue. 3 blue cells. Bad!

So the condition for no 3 blue cells in any 2×2 block is: λi = λi+1 for all i (since λi ≥ λi+1 for Ferrers, and λi > λi+1 gives 3 blue cells).

But that means all rows have the same length, i.e., the blue cells form a rectangle! And a rectangle with 101 blue cells requires 101 = a × b with n = max(a, b) ≥ 11 (since 101 is prime, a = 1, b = 101, n = 101).

That can't be right—the answer would be 101, which seems too large for a competition problem.

Wait, I think I'm being too restrictive. I was only considering Ferrers diagrams (left-justified). There might be other shapes that satisfy the conditions.

Let me reconsider. The conditions are:
1. No 2×2 block has exactly 3 blue cells.
2. No 2×2 block has 2 diagonal blue cells.

These don't require the shape to be a Ferrers diagram. Let me think about other shapes.

Consider a "staircase" that goes in both directions. For example:
Row 1: columns 1 to a (blue)
Row 2: columns 2 to a+1 (blue)
Row 3: columns 3 to a+2 (blue)
...

This is a "shifted" staircase. Let me check the conditions.

Row i: columns i to a+i-1 (blue). 

2×2 block at rows i, i+1, columns j, j+1:
- Row i has blue at j, j+1 iff i ≤ j and j+1 ≤ a+i-1, i.e., j ≥ i and j ≤ a+i-2.
- Row i+1 has blue at j, j+1 iff i+1 ≤ j and j+1 ≤ a+i, i.e., j ≥ i+1 and j ≤ a+i-1.

Case: j = i. Row i: blue at j=i, j+1=i+1 (if i+1 ≤ a+i-1, i.e., a ≥ 2). Row i+1: not blue at j=i (since i < i+1). So blue cells: (i, i), (i, i+1). 2 blue cells, adjacent. Fine (if a ≥ 2).

Case: j = i+1. Row i: blue at j=i+1, j+1=i+2 (if i+2 ≤ a+i-1, i.e., a ≥ 3). Row i+1: blue at j=i+1, j+1=i+2 (if i+2 ≤ a+i, i.e., a ≥ 2). If a ≥ 3: all 4 blue. Fine. If a = 2: row i has blue at i+1 but not i+2 (since i+2 > a+i-1 = i+1). Row i+1 has blue at i+1 and i+2 (since i+2 = a+i). So blue: (i, i+1), (i+1, i+1), (i+1, i+2). 3 blue cells. Bad!

So the shifted staircase with a = 2 has 3 blue cells in some 2×2 blocks. With a ≥ 3, the interior 2×2 blocks are fine, but I need to check the boundary blocks.

Actually, this is getting quite complex. Let me think about the problem differently.

Let me reconsider: maybe the conditions I stated (no 3 in a 2×2, no 2 diagonal in a 2×2) are not sufficient for uniqueness, and the actual condition is different.

Let me go back to first principles and think about what makes a rectangular partition unique.

Actually, I realize I should think about this more carefully. The conditions I derived are necessary (if violated, the partition is not unique). But they might not be sufficient. Let me think about whether there are other sources of non-uniqueness.

Consider a 1×4 grid with blue at positions 1 and 3. Non-blue at 2 and 4. 

2×2 conditions don't apply (only 1 row). But the partition is not unique: {(1),(2)} and {(3),(4)}, or {(1)} and {(2),(3)} and {(4)}... wait, {(2),(3)} has 1 blue cell (3). But then we have 3 rectangles: {(1)}, {(2),(3)}, {(4)}. But {(4)} has 0 blue cells. Invalid. 

Actually, let me reconsider. 1×4 grid, blue at 1 and 3. We need 2 rectangles (one per blue cell). 
- {(1),(2)} and {(3),(4)}: each has 1 blue. Valid.
- {(1)} and {(2),(3),(4)}: 1 blue each. Valid.
- {(1),(2),(3)} and {(4)}: 2 blue and 0 blue. Invalid.
- {(1)} and {(2),(3)} and {(4)}: 3 rectangles but only 2 blue cells. Invalid (each rectangle needs exactly 1 blue cell, so we need exactly 2 rectangles).

Wait, actually we need exactly as many rectangles as blue cells. So 2 rectangles.

- {(1),(2)} and {(3),(4)}: valid.
- {(1)} and {(2),(3),(4)}: valid.
- {(1),(2),(3)} and {(4)}: invalid (2 blue in first).

So 2 valid partitions. Not unique. The issue is that blue cells 1 and 3 are not adjacent, so the cut between them can be at position 1-2 or 2-3.

So in 1D, uniqueness requires all blue cells to be adjacent (consecutive). This is the "contiguous" condition.

In 2D, the situation is more complex. Let me think about whether the 2×2 conditions plus contiguity are sufficient.

Actually, I think the right way to think about this is:

The partition is unique if and only if every "cut" is forced. A cut is forced if removing it creates an invalid partition (some rectangle with 0 or ≥2 blue cells).

Let me think about when a cut is not forced. A cut between two adjacent cells is not forced if both cells can be in the same rectangle (i.e., removing the cut still gives a valid partition). This happens when the two cells are in the same "blue region" and combining them doesn't create a rectangle with ≥2 blue cells.

Hmm, this is still complex. Let me try a different approach: think about the problem as a competition problem and try to find the answer.

Let me consider the possibility that the answer is 101 (the trivial single-row construction). But that seems too easy for a competition problem. Let me think about whether we can do better.

Let me consider the "staircase" construction more carefully, but with a different shape.

Consider the following arrangement: a "path" of blue cells where each blue cell is adjacent to the next, forming a Hamiltonian-like path. But we need the partition to be unique.

Actually, let me think about a "snake" path. Consider a 1×n strip folded into a snake:

Row 1: columns 1, 2, ..., n (all blue)
Row 2: columns n, n-1, ..., 1 ... no, this doesn't make sense for a path.

Let me think about a different construction. Consider an arrangement where the blue cells form a "staircase" that goes down and right:

(1,1), (2,1), (2,2), (3,2), (3,3), (4,3), (4,4), ...

Each blue cell is adjacent to the next. The path goes: right, down, right, down, ...

For this path, consider the 2×2 block at rows 1-2, columns 1-2: blue at (1,1), (2,1), (2,2). 3 blue cells. Violates condition 1.

So this staircase path doesn't work either.

What if we "fill in" the staircase to avoid 3-in-a-2×2? We'd need to add (1,2) to make it 4, or remove one of the 3.

If we add (1,2): blue at (1,1), (1,2), (2,1), (2,2). That's a 2×2 block. Then continue: (2,2), (3,2), (3,3), (4,3), (4,4), ... But (2,2) is already in the 2×2 block. The next step is (3,2). 2×2 block at rows 2-3, columns 2-3: blue at (2,2), (3,2), (3,3). 3 blue cells. Need to add (2,3). Then 2×2 block at rows 2-3, cols 2-3: all 4 blue. Continue with (3,3), (4,3), (4,4), ... 2×2 at rows 3-4, cols 3-4: (3,3), (4,3), (4,4). 3 blue. Add (3,4). 

So the pattern is: 2×2 blocks along the diagonal. Blue cells at (i,j) where i ∈ {2k-1, 2k} and j ∈ {2k-1, 2k} for k = 1, 2, ..., m. This gives 4m blue cells in a 2m × 2m grid. For 101 blue cells, 4m = 101 doesn't work (101 not divisible by 4).

Hmm. Let me think about this differently.

What if we use a mix of 2×2 blocks and single cells?

Actually, let me reconsider the problem. Maybe the conditions I stated are not the right ones, or maybe I need to think about the problem differently.

Let me re-examine the problem statement: "there exists a unique way to cut the table to rectangles along boundaries of its squares with the following property: every rectangle contains exactly one blue square."

So we need: (1) there exists at least one valid partition, and (2) there is at most one valid partition.

Let me think about what configurations have a unique valid partition.

Key insight: I think the right way to think about this is in terms of "separating lines."

Consider two blue cells A and B. They must be in different rectangles. The rectangles must be separated by a cut. If A and B are in the same row (resp. column), the cut must be a vertical (resp. horizontal) line segment between them. If they're not in the same row or column, the separation is more complex.

For the partition to be unique, every separation must be forced.

Let me think about a cleaner characterization. 

I think the key is: the partition is unique if and only if the blue cells form a "staircase" where each row's blue interval and each column's blue interval are "compatible" in a specific way.

Actually, let me try to think about this problem from the answer. Let me consider that the answer might be 15 or 20 or something in that range.

Let me think about the maximum number of blue cells in an n×n grid with a unique partition.

From the analysis of Ferrers diagrams, the maximum with all rows equal is n² (full grid), but that requires n² = 101, impossible.

What if we don't require a Ferrers diagram? Let me think about other shapes.

Consider a "cross" shape: row k is fully blue (n cells), and column k is fully blue (n cells), with the center cell shared. Total: 2n - 1 blue cells. For 2n - 1 = 101, n = 51. Grid size: 51 × 51. But is the partition unique?

In a cross shape, the 2×2 blocks at the corners of the cross (e.g., rows k-1, k, columns k-1, k) have 3 blue cells (the cross covers (k, k-1), (k, k), (k-1, k) but not (k-1, k-1)). So condition 1 is violated. Not unique.

What about a "plus" shape where we fill in the corners? That would be a full grid, which gives n² blue cells.

Let me think about a different type of construction. What if the blue cells form a "thick diagonal"?

Consider blue cells at (i, j) where |i - j| ≤ d for some d. This is a band around the diagonal. For d = 0, it's the diagonal (n cells). For d = 1, it's a tridiagonal (3n - 2 cells). Etc.

For the tridiagonal (d = 1), consider the 2×2 block at rows 1-2, columns 1-2: (1,1), (1,2), (2,1), (2,2) all satisfy |i-j| ≤ 1. All 4 blue. Fine. Block at rows 1-2, columns 2-3: (1,2) |1-2|=1 ✓, (1,3) |1-3|=2 ✗, (2,2) ✓, (2,3) |2-3|=1 ✓. 3 blue cells. Bad!

So the tridiagonal doesn't work.

Hmm. Let me think about what shapes avoid both conditions.

The conditions are:
1. No 2×2 block has exactly 3 blue cells.
2. No 2×2 block has exactly 2 diagonal blue cells.

These together mean: in every 2×2 block, the blue cells form either: empty, 1 cell, 2 adjacent cells, or all 4 cells.

This is equivalent to: the blue cells form a "polyomino" that is a union of disjoint rectangles, where no two rectangles are "diagonally adjacent" (i.e., if two rectangles touch at a corner, they must also share an edge).

Wait, that's not quite right. Let me think again.

Actually, the condition "in every 2×2 block, blue cells are 0, 1, 2 adjacent, or 4" is equivalent to saying the blue region is a "convex polyomino" that is both "row-convex" and "column-convex" AND "monotone" in some sense.

Hmm, actually, I think this condition is equivalent to: the blue region can be decomposed into rectangles such that the rectangles form a "laminar" family (any two are either disjoint, nested, or share a full side).

No, that's not right either. Let me think more carefully.

The condition "no 2×2 block has 3 blue or 2 diagonal blue" means: if (i,j) is blue and (i+1,j+1) is blue, then (i,j+1) and (i+1,j) are both blue. And if (i,j+1) is blue and (i+1,j) is blue, then (i,j) and (i+1,j+1) are both blue.

This means: the blue region is closed under "rectangular completion" — if two diagonal cells of a 2×2 block are blue, the other two must be blue too. This is exactly the condition that the blue region is a "rectangular" or "orthogonal convex" polyomino that is also "hv-convex."

Wait, I think this condition means the blue region is a union of rectangles that are "aligned" in a specific way. Actually, I think it means the blue region is a "staircase polyomino" or "convex polyomino with the additional property."

Let me think about it differently. The condition says: the indicator function of blue cells is "2D-monotone" in some sense. 

Actually, I recall that a set S of grid cells satisfying "if (i,j) and (i+1,j+1) are in S, then (i,j+1) and (i+1,j) are in S" (and the symmetric condition) is called a "convex" set in the sense that it's an intersection of the grid with a convex region. No wait, that's not right either.

Let me just think about what shapes satisfy the condition. 

The condition is: the blue cells form a set where every 2×2 subgrid has 0, 1, 2-adjacent, or 4 blue cells. 

This is equivalent to: the blue cells form a set that is a "disjoint union of rectangles, where the rectangles are separated by at least one empty row or column, OR the rectangles share full edges (not just corners)."

Wait, no. Consider two 2×2 blocks sharing a side. If one is all blue and the other is all blue, together they form a 2×4 or 4×2 rectangle, which is fine. If one is all blue and the other has 2 adjacent blue cells, we need to check the combined 2×3 or 3×2 region.

I think the condition is equivalent to: the blue region is a "polyomino" that can be built by starting with rectangles and merging them only along full sides. But I'm not sure.

Let me try a different approach. Let me just think about what the maximum number of blue cells is in an n×n grid satisfying the 2×2 condition, and see if that helps.

For the 2×2 condition (no 3, no 2-diagonal in any 2×2), the maximum is n² (all cells blue, every 2×2 has 4). But we need exactly 101, not n².

The question is: for which n can we place 101 blue cells in an n×n grid satisfying the 2×2 condition, AND the partition is unique?

But I haven't verified that the 2×2 condition is sufficient for uniqueness. Let me check with a larger example.

Consider a 3×3 grid with all 9 cells blue. Every 2×2 has 4 blue. Partition: 9 unit rectangles. Unique? Yes, because any larger rectangle would have ≥2 blue cells. ✓

Consider a 3×3 grid with blue at (1,1), (1,2), (2,1), (2,2) (a 2×2 block in the corner). 4 blue cells. Non-blue: (1,3), (2,3), (3,1), (3,2), (3,3).

2×2 conditions:
- Rows 1-2, cols 1-2: 4 blue. ✓
- Rows 1-2, cols 2-3: (1,2) blue, (1,3) not, (2,2) blue, (2,3) not. 2 adjacent. ✓
- Rows 2-3, cols 1-2: (2,1) blue, (2,2) blue, (3,1) not, (3,2) not. 2 adjacent. ✓
- Rows 2-3, cols 2-3: (2,2) blue, (2,3) not, (3,2) not, (3,3) not. 1 blue. ✓

Conditions satisfied. Is the partition unique?

Non-blue cells: (1,3), (2,3), (3,1), (3,2), (3,3).

(1,3): must join a rectangle with 1 blue cell. Adjacent blue: (1,2). Rectangle {(1,2), (1,3)}: 1 blue. Could (1,3) join (2,2)? Rectangle would be {(1,2), (1,3), (2,2), (2,3)}: 2 blue. Invalid. So (1,3) joins (1,2). Forced.

(2,3): adjacent blue: (2,2). Rectangle {(2,2), (2,3)}: 1 blue. But (1,3) already joined (1,2), and (2,3) joining (2,2) would make rectangle {(2,2), (2,3)}. Is there another option? (2,3) joining (1,3)? (1,3) is not blue. (2,3) joining (3,3)? (3,3) is not blue. So (2,3) must join (2,2). Forced.

(3,1): adjacent blue: (2,1). Rectangle {(2,1), (3,1)}: 1 blue. Other options? (3,1) joining (3,2)? (3,2) not blue. So forced.

(3,2): adjacent blue: (2,2). But (2,2) is already in rectangle {(2,2), (2,3)}. Can (3,2) join that? Rectangle {(2,2), (2,3), (3,2), (3,3)}: 1 blue. Valid! Or (3,2) joining (2,1)? (2,1) is in {(2,1), (3,1)}. Adding (3,2) would make {(2,1), (3,1), (3,2)}: 1 blue. But is this a rectangle? (2,1), (3,1), (3,2) is not a rectangle (it's an L-shape). Invalid. Or (3,2) joining (3,1)? (3,1) is in {(2,1), (3,1)}. Adding (3,2): {(2,1), (3,1), (3,2)} not a rectangle. Invalid.

So (3,2) must join the rectangle containing (2,2), which is {(2,2), (2,3)}. Extended to {(2,2), (2,3), (3,2), (3,3)}. 1 blue. Valid. Forced.

(3,3): already in the rectangle {(2,2), (2,3), (3,2), (3,3)}. 

So the partition is:
- {(1,1)}, {(1,2), (1,3)}, {(2,1), (3,1)}, {(2,2), (2,3), (3,2), (3,3)}.

Wait, but I need to check: is (3,3) forced to be in the rectangle with (2,2)? (3,3) is adjacent to (3,2) and (2,3), both of which are in the (2,2) rectangle. (3,3) could also be its own rectangle, but that has 0 blue cells. Invalid. So (3,3) must join a rectangle with a blue cell. The only adjacent cells with blue cells are (3,2) and (2,3), both in the (2,2) rectangle. So (3,3) joins that rectangle. Forced.

But wait, I need to also check: could (3,2) and (3,3) form a separate rectangle with (2,3)? Like, instead of (3,2) joining (2,2)'s rectangle, could we have a different partition where (3,2) and (3,3) join (2,3)?

Let me reconsider. The rectangle containing (2,2) must be a rectangle containing (2,2) and no other blue cell. The blue cells are (1,1), (1,2), (2,1), (2,2). So (2,2)'s rectangle contains only (2,2) as a blue cell.

What are the possible rectangles containing (2,2) with no other blue cell?
- {(2,2)}: 1 blue. Valid.
- {(2,2), (2,3)}: 1 blue. Valid.
- {(2,2), (3,2)}: 1 blue. Valid.
- {(2,2), (2,3), (3,2), (3,3)}: 1 blue. Valid.
- {(2,2), (1,2)}: 2 blue. Invalid.
- {(2,2), (2,1)}: 2 blue. Invalid.
- {(2,2), (1,3)}: not a rectangle (not contiguous). Invalid.
- {(2,2), (2,3), (3,2)}: not a rectangle (L-shape). Invalid.
- {(1,2), (1,3), (2,2), (2,3)}: 2 blue. Invalid.
- Larger rectangles including (2,2): any rectangle including (1,2) or (2,1) has 2 blue. So the rectangle can only extend right and/or down.

So the possible rectangles for (2,2) are: {(2,2)}, {(2,2),(2,3)}, {(2,2),(3,2)}, {(2,2),(2,3),(3,2),(3,3)}.

Now, (1,3) must be in some rectangle with 1 blue cell. (1,3) is adjacent to (1,2) [blue] and (2,3) [not blue]. 
- If (1,3) joins (1,2): rectangle {(1,2), (1,3)}. Then (2,2)'s rectangle can be any of the 4 options.
- If (1,3) doesn't join (1,2): (1,3) must join a rectangle with some blue cell. The only blue cell reachable is (1,2) (since (2,3) is not blue and (1,3) is in the corner). Actually, (1,3) could be in a rectangle with (2,2) if the rectangle is {(1,2), (1,3), (2,2), (2,3)}: 2 blue. Invalid. Or {(1,3), (2,3)}: 0 blue. Invalid. So (1,3) must join (1,2). Forced.

Similarly, (2,3) must join a rectangle with 1 blue cell. (2,3) is adjacent to (1,3) [in (1,2)'s rectangle], (2,2) [blue], (3,3) [not blue]. 
- (2,3) joining (2,2): rectangle could be {(2,2), (2,3)} or larger.
- (2,3) joining (1,2)'s rectangle: would need rectangle including (1,2), (1,3), (2,2), (2,3): 2 blue. Invalid.
- (2,3) joining (3,3): 0 blue. Invalid.
So (2,3) must join (2,2). Forced.

(3,1) must join (2,1) (only adjacent blue cell). Forced.

(3,2): adjacent to (3,1) [in (2,1)'s rectangle], (2,2) [blue], (3,3) [not blue].
- (3,2) joining (2,2): rectangle {(2,2), (3,2)} or larger. But (2,3) is already in (2,2)'s rectangle, so the rectangle is at least {(2,2), (2,3), (3,2), (3,3)} (to be a valid rectangle). 1 blue. Valid.
- (3,2) joining (2,1)'s rectangle: would need rectangle including (2,1), (3,1), (3,2): L-shape. Invalid. Or (2,1), (2,2), (3,1), (3,2): 2 blue. Invalid.
- (3,2) joining (3,3): 0 blue. Invalid.
So (3,2) must join (2,2)'s rectangle. Forced.

(3,3): adjacent to (3,2) [in (2,2)'s rectangle], (2,3) [in (2,2)'s rectangle]. Must join (2,2)'s rectangle. Forced.

So the partition is unique:
- {(1,1)}, {(1,2), (1,3)}, {(2,1), (3,1)}, {(2,2), (2,3), (3,2), (3,3)}.

Great, so the 2×2 block in the corner of a 3×3 grid gives a unique partition. ✓

Now, the question is: can we combine multiple such blocks to get 101 blue cells in a small grid?

Let me think about combining blocks. Consider a grid made of multiple 2×2 blocks of blue cells, separated by gaps.

For example, two 2×2 blocks: one at rows 1-2, cols 1-2, and one at rows 1-2, cols 4-5. In a 2×5 grid. 8 blue cells. Non-blue: (1,3), (2,3).

2×2 conditions:
- Rows 1-2, cols 1-2: 4 blue. ✓
- Rows 1-2, cols 2-3: (1,2) blue, (1,3) not, (2,2) blue, (2,3) not. 2 adjacent. ✓
- Rows 1-2, cols 3-4: (1,3) not, (1,4) blue, (2,3) not, (2,4) blue. 2 diagonal! ✗

So two 2×2 blocks in the same rows, separated by one column, violate condition 2 (diagonal pair in the 2×2 block at cols 3-4). 

To fix this, we need at least 2 empty columns between blocks (so that the 2×2 blocks at the boundary have at most 1 blue cell). Or we need the blocks to be in different rows.

If blocks are in different rows and different columns (no overlap), separated by at least one empty row and one empty column, then the 2×2 conditions are satisfied at the boundaries.

But this is wasteful. Let me think about more efficient arrangements.

What if the blocks share a row or column? For example, a 2×4 block (two 2×2 blocks side by side). This is just a 2×4 rectangle of blue cells. 8 blue cells. The partition: each cell is its own rectangle (since any 1×2 or 2×1 rectangle has 2 blue cells). Unique. ✓

So a full a×b rectangle of blue cells gives ab blue cells, and the partition is unique (each cell is 1×1). The grid size is max(a, b). For ab = 101 (prime), we need a=1, b=101, n=101. Not helpful.

But what if we combine a rectangle with some extensions?

Consider a 10×10 rectangle of blue cells (100 blue cells) plus 1 more blue cell. The 10×10 block has a unique partition (each cell is 1×1). The extra blue cell needs to be placed such that the overall partition is still unique.

If the extra blue cell is at (11, 1) (just below the 10×10 block), then the grid is 11×10 (but we need n×n, so 11×11). The non-blue cells are in row 11, columns 2-11, and column 11, rows 1-10.

Wait, the 10×10 block is at rows 1-10, cols 1-10. Extra blue at (11, 1). Grid is 11×11. Non-blue: row 11, cols 2-11 (10 cells), and col 11, rows 1-10 (10 cells). Total non-blue: 20. Total blue: 101. ✓

Is the partition unique?

The 10×10 block: each cell is 1×1 (since any larger rectangle within the block has ≥2 blue cells). So the 100 blue cells in the block each get a 1×1 rectangle. But wait, the non-blue cells need to join some rectangle. 

Cell (1, 11): adjacent to (1, 10) [blue, in 1×1 rectangle]. Can join (1, 10)'s rectangle: {(1,10), (1,11)}: 1 blue. Valid. Any other option? (1, 11) adjacent to (2, 11) [not blue]. So (1, 11) must join (1, 10). Forced.

Similarly, (i, 11) for i = 1, ..., 10 must join (i, 10). Forced.

Cell (11, 2): adjacent to (11, 1) [blue], (10, 2) [blue]. 
- Join (11, 1): rectangle {(11, 1), (11, 2)}: 1 blue. Valid.
- Join (10, 2): rectangle {(10, 2), (11, 2)}: 1 blue. Valid.
Two options! Not unique. ✗

So the extra blue cell at (11, 1) creates ambiguity for (11, 2), which can join either (11, 1) or (10, 2).

To fix this, I need to prevent (11, 2) from joining (10, 2). One way: make (10, 2) unable to extend downward. But (10, 2) is in a 1×1 rectangle, and extending to (11, 2) gives a 2×1 rectangle with 1 blue cell. There's no way to prevent this in the current setup.

Another approach: place the extra blue cell such that it doesn't create this ambiguity. 

What if the extra blue cell is at (11, 11) (diagonally adjacent to the 10×10 block)? Then (11, 11) is adjacent to (10, 11) [not blue] and (11, 10) [not blue]. So (11, 11) is isolated from blue cells. It can't be in a rectangle with any blue cell. Invalid (a 1×1 rectangle at (11,11) has 1 blue cell, but we also need to assign (10, 11) and (11, 10) to rectangles with blue cells).

Actually, (11, 11) is a blue cell, so it needs its own rectangle. The rectangle can be just {(11, 11)}. Then (10, 11) needs to join a rectangle with a blue cell: adjacent to (10, 10) [blue]. Join (10, 10): {(10, 10), (10, 11)}: 1 blue. Valid. (11, 10) needs to join: adjacent to (10, 10) [in rectangle with (10, 11)], (11, 9) [not blue], (11, 11) [blue]. 
- Join (10, 10)'s rectangle: would need rectangle {(10, 10), (10, 11), (11, 10), (11, 11)}: 2 blue. Invalid.
- Join (11, 11): rectangle {(11, 10), (11, 11)}: 1 blue. Valid.
So (11, 10) joins (11, 11). Forced.

But what about (10, 11)? It joins (10, 10). Could (10, 11) join (11, 11)? Rectangle {(10, 11), (11, 11)}: 1 blue. Valid! So (10, 11) has two options: join (10, 10) or join (11, 11). Not unique. ✗

Hmm. The issue is always the same: a non-blue cell adjacent to two blue cells can join either.

So the key challenge is: how to place blue cells such that every non-blue cell is adjacent to at most one blue cell (or more precisely, can join only one blue cell's rectangle).

Wait, that's too strong. A non-blue cell might be adjacent to two blue cells but only able to join one (because joining the other would create an invalid rectangle).

Let me reconsider. The condition for uniqueness is: every non-blue cell can be assigned to exactly one blue cell's rectangle, considering the global constraint that all rectangles must be valid (rectangular, each with exactly 1 blue cell).

This is a global constraint, not just local. So the analysis is more complex.

Let me think about this differently. Maybe I should think about the problem in terms of "forced extensions."

Consider a blue cell B. Its rectangle R(B) must be a rectangle containing B and no other blue cell. The rectangle is determined by its boundaries (top, bottom, left, right). For uniqueness, the boundaries must be forced.

A boundary is forced if moving it would include another blue cell or exclude B.

So R(B) is the "maximal" rectangle around B that contains no other blue cell, in some sense. But "maximal" isn't quite right because the rectangle must partition the grid with other rectangles.

Hmm, let me think about this differently.

Actually, I think the problem is equivalent to: the blue cells are "separated" by a unique set of cuts. The cuts form a "guillotine partition" or more generally a "rectangular partition."

Let me think about the problem from the perspective of the dual graph. 

OK let me try yet another approach. Let me think about the problem as a competition problem and try to find the answer by construction.

I'll try to construct a configuration with 101 blue cells and a unique partition, minimizing n.

Construction idea: Use a "staircase" of rectangles.

Consider the following: divide the n×n grid into rectangles R1, R2, ..., R101, each containing one blue cell. The partition is unique if the rectangles are "forced."

One way to force the partition: make the rectangles form a "guillotine partition" where each cut is forced.

A guillotine cut is forced if one of the two resulting pieces has exactly one blue cell. Then that piece must be a single rectangle, and the cut is the only option.

So consider the following recursive construction:
1. Start with the n×n grid containing 101 blue cells.
2. Find a guillotine cut that separates one blue cell from the rest. This cut is forced (the piece with 1 blue cell must be a rectangle containing just that cell, and the cut position is forced if the piece is determined).
3. Recurse on the remaining piece with 100 blue cells.

For this to work, at each step, we need a forced guillotine cut. A guillotine cut that separates exactly 1 blue cell is forced if the resulting 1-blue-cell piece is a rectangle (which it is, since it's a guillotine cut).

But we also need the cut to be uniquely determined. If there are multiple positions for the guillotine cut that separate 1 blue cell, the partition is not unique.

Hmm, so we need: at each step, there's exactly one guillotine cut that separates exactly 1 blue cell.

Wait, actually, we need the entire partition to be unique, not just the guillotine cuts. There might be non-guillotine partitions that are also valid.

But if we can show that the only valid partition is the one obtained by the forced guillotine cuts, then it's unique.

Let me think about a specific construction.

Construction: "Staircase" of 1-wide strips.

Consider an n×n grid. Place blue cells as follows:
- Row 1, column 1: blue. (1 blue cell)
- Row 1, columns 2 to n: non-blue. Row 2, column 1: non-blue. These non-blue cells must join the (1,1) rectangle.

Wait, this doesn't scale well. Let me think differently.

Let me consider the "peeling" construction:

Place 1 blue cell at (1, 1). The rest of row 1 and column 1 must join (1,1)'s rectangle. So (1,1)'s rectangle is the entire first row and first column? No, it must be a rectangle. So it's either the first row (1×n) or the first column (n×1) or a k×l rectangle including (1,1).

Hmm, this is ambiguous. Let me think more carefully.

Actually, let me think about a construction where the partition is a "staircase" of rectangles, each being a 1×k strip.

Consider the following partition of an n×n grid into 101 rectangles:
- R1 = row 1, columns 1 to a1 (1×a1 strip)
- R2 = column a1, rows 2 to a2 (actually this doesn't work as a staircase)

Let me think about a "staircase partition" more carefully.

A staircase partition: 
- R1: rows 1 to r1, column 1 (r1×1 strip)
- R2: row r1+1, columns 1 to c2 (1×c2 strip)
- R3: rows r1+2 to r3, column c2 (actually this is getting complicated)

Let me try a specific example. Consider a 3×3 grid partitioned as:
- R1: {(1,1), (2,1), (3,1)} (column 1, 3×1)
- R2: {(1,2), (1,3)} (row 1, columns 2-3, 1×2)
- R3: {(2,2), (3,2), (3,3)} ... no, this isn't a rectangle.

Let me try:
- R1: {(1,1), (2,1)} (2×1)
- R2: {(1,2), (1,3)} (1×2)
- R3: {(2,2)} (1×1)
- R4: {(2,3), (3,3)} (2×1)
- R5: {(3,1), (3,2)} (1×2)

Blue cells at (1,1), (1,2), (2,2), (2,3), (3,1). 5 blue cells in 3×3.

Is this partition unique? Let me check.

Blue: (1,1), (1,2), (2,2), (2,3), (3,1). Non-blue: (1,3), (2,1), (3,2), (3,3).

Wait, (2,1) is non-blue but it's in R1 with (1,1). (1,3) is non-blue in R2 with (1,2). (3,2) is non-blue in R5 with (3,1). (3,3) is non-blue in R4 with (2,3).

Let me check if there's another valid partition.

(2,1) must join a rectangle with 1 blue cell. Adjacent blue: (1,1), (3,1). 
- Join (1,1): rectangle {(1,1), (2,1)}: 1 blue. Valid.
- Join (3,1): rectangle {(2,1), (3,1)}: 1 blue. Valid.
Two options. Not unique. ✗

So this doesn't work either. The issue is that (2,1) is between two blue cells in the same column.

For uniqueness, we need: no non-blue cell is between two blue cells in the same row or column (unless there's a constraint that forces it one way).

Wait, but in the 2×2 block example that worked, (1,3) was adjacent to only one blue cell (1,2), and (3,1) was adjacent to only one blue cell (2,1). The non-blue cells on the "boundary" were each adjacent to only one blue cell.

So the key insight might be: every non-blue cell must be "forced" to join exactly one blue cell's rectangle, and this happens when the non-blue cell is on the "boundary" of the blue region, adjacent to only one blue cell (or more precisely, can only extend one blue cell's rectangle).

Let me think about this more carefully. 

In the 2×2 block example (3×3 grid, blue at (1,1), (1,2), (2,1), (2,2)):
- (1,3) is adjacent to (1,2) only (among blue cells). Forced to join (1,2).
- (2,3) is adjacent to (2,2) only. Forced.
- (3,1) is adjacent to (2,1) only. Forced.
- (3,2) is adjacent to (2,2) only (among blue cells; (3,1) is not blue). Forced.
- (3,3) is adjacent to (3,2) and (2,3), both non-blue. But (3,2) is in (2,2)'s rectangle and (2,3) is in (2,2)'s rectangle. So (3,3) joins (2,2)'s rectangle. Forced.

So the non-blue cells are "peeled" from the outside in, each forced to join the unique adjacent blue cell's rectangle.

This suggests a construction: place blue cells in a "block" (rectangle) and let the non-blue cells around it be forced to join.

For a k×k block of blue cells in an n×n grid (k < n), the non-blue cells form an L-shaped border. Each non-blue cell on the border is adjacent to exactly one blue cell (the one on the edge of the block), except for the "corner" non-blue cells.

Wait, let me think about a k×k block at the top-left corner of an n×n grid. Non-blue cells: rows 1 to k, columns k+1 to n (right strip), and rows k+1 to n, columns 1 to n (bottom strip).

Cell (1, k+1): adjacent to (1, k) [blue]. Forced to join (1, k).
Cell (2, k+1): adjacent to (2, k) [blue]. Forced.
...
Cell (k, k+1): adjacent to (k, k) [blue]. Forced.
Cell (k+1, 1): adjacent to (k, 1) [blue]. Forced.
...
Cell (k+1, k): adjacent to (k, k) [blue]. But (k, k) is also adjacent to (k, k+1) which is non-blue. 

Wait, (k+1, k) is adjacent to (k, k) [blue] and (k+1, k-1) [non-blue] and (k+1, k+1) [non-blue]. So (k+1, k) can only join (k, k
