# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Sofia and Viktor are playing a game on a $2022 \times 2022$ board:
- Sofia covers the board completely with dominoes, with no overlaps and all within the board.
- Viktor chooses a positive integer $n$.
- Viktor then selects and fixes $n$ dominoes.
- Sofia removes the remaining dominoes and tries to cover the board with a different arrangement of dominoes.
If Sofia succeeds, she wins; otherwise, Viktor wins. What is the minimum number $n$ for which Viktor can always win, regardless of Sofia's initial domino placement?       — 题目文本
#   To solve the problem of finding the minimum number \( n \) such that Viktor can always win by choosing \( n \) dominoes to fix, we need to understand the concept of a forcing set in the context of domino tilings on a grid.

### Step-by-Step Solution:

1. **Understanding the Problem:**
   - The board is a \( 2022 \times 2022 \) grid.
   - Each domino covers two adjacent squares.
   - Viktor's goal is to choose \( n \) dominoes such that Sofia cannot rearrange the remaining dominoes into a different tiling.

2. **Forcing Sets:**
   - A forcing set is a subset of dominoes such that fixing these dominoes uniquely determines the entire tiling.
   - To prevent any rearrangement, Viktor needs to ensure that no two adjacent squares can be part of a different tiling.

3. **2x2 Blocks and Flips:**
   - Consider the smallest unit of a tiling: a \( 2 \times 2 \) block.
   - Each \( 2 \times 2 \) block can be tiled in two ways: either both dominoes are horizontal or both are vertical.
   - To prevent any flip in a \( 2 \times 2 \) block, at least one domino in each block must be fixed.

4. **Partitioning the Grid:**
   - The \( 2022 \times 2022 \) grid can be divided into \( 1011 \times 1011 \) non-overlapping \( 2 \times 2 \) blocks.
   - Each \( 2 \times 2 \) block contains exactly 2 dominoes, and to prevent any flip, at least one domino in each block must be fixed.

5. **Calculating the Minimum Number \( n \):**
   - The total number of \( 2 \times 2 \) blocks is \( 1011 \times 1011 \).
   - Therefore, the minimum number of dominoes that need to be fixed is \( 1011 \times 1011 \).

6. **Final Calculation:**
   - \( 1011 \times 1011 = 1022121 \).

### Conclusion:
The minimum number \( n \) for which Viktor can always win, regardless of Sofia's initial domino placement, is \(\boxed{1022121}\).  — 标准解答
#   Let me analyze this problem carefully.

We have a 2022×2022 board. Sofia covers it with dominoes (each domino covers 2 adjacent cells). Then Viktor chooses a positive integer n and fixes n dominoes. Sofia removes the rest and tries to re-cover the board with a different arrangement of dominoes. If she succeeds, she wins; otherwise Viktor wins.

We need the minimum n such that Viktor can always win, regardless of Sofia's initial placement.

So Viktor wants to fix n dominoes such that the remaining uncovered cells (the board minus the 2n cells covered by fixed dominoes) cannot be tiled by dominoes in any way other than... wait, let me re-read.

"Sofia removes the remaining dominoes and tries to cover the board with a different arrangement of dominoes."

So after Viktor fixes n dominoes, Sofia removes all other dominoes. Now the board has 2n cells covered by fixed dominoes, and the rest is uncovered. Sofia tries to cover the ENTIRE board with a different arrangement of dominoes. The fixed dominoes stay in place. So Sofia needs to tile the remaining cells (the board minus the 2n cells covered by fixed dominoes) with dominoes, in a way that's different from the original tiling.

Wait, "cover the board with a different arrangement of dominoes" - does this mean cover the entire board (including where fixed dominoes are) or just the uncovered part? The fixed dominoes are already in place, so Sofia needs to tile the remaining uncovered cells. The "different arrangement" means different from the original arrangement of the non-fixed dominoes.

So Viktor wins if: after fixing n dominoes, the remaining cells can ONLY be tiled in the original way (i.e., the original tiling is the unique tiling of the remaining cells).

Actually, let me reconsider. Sofia tries to cover the board with a different arrangement. If the remaining cells have a unique tiling (which must be the original one since the original one works), then Sofia cannot find a different arrangement, so Viktor wins.

So Viktor wants to fix n dominoes such that the remaining uncovered cells have a UNIQUE domino tiling (which is forced to be the original tiling restricted to those cells).

The question: what is the minimum n such that for ANY initial tiling by Sofia, Viktor can choose n dominoes to fix so that the remaining cells have a unique tiling?

Let me think about this more carefully.

A tiling of a region is "frozen" or "rigid" if it's the unique tiling. We want to find a set of dominoes to remove (fix) such that the remaining region has a unique tiling.

Actually, we fix n dominoes (they stay), and remove the rest. The remaining region (board minus fixed dominoes' cells) needs to have a unique tiling.

Let me think about small cases and the structure.

Key concept: A tiling has a "cycle" if there's an alternating cycle - a cycle of cells where you can flip dominoes along the cycle to get a different tiling. If a tiling has no alternating cycles, it's the unique tiling of that region.

So the question becomes: what's the minimum number of dominoes to fix so that the remaining region's tiling has no alternating cycles?

An alternating cycle in a domino tiling: a cycle of even length where consecutive edges alternate between being covered by a domino and not. Flipping along such a cycle gives a new tiling.

If we fix some dominoes, the remaining region is the board with those cells removed. The tiling of the remaining region is the original tiling restricted to those cells. This tiling is unique iff there are no alternating cycles in the remaining region.

So Viktor wants to choose dominoes to fix such that every alternating cycle in the original tiling is "broken" - i.e., at least one domino on each alternating cycle is fixed.

Wait, but fixing a domino removes its cells from the remaining region, which breaks any alternating cycle passing through those cells.

So the problem reduces to: In any domino tiling of the 2022×2022 board, what is the minimum number of dominoes that Viktor needs to fix so that every alternating cycle is broken (has at least one fixed domino on it)?

Hmm, but this is a hitting set problem on alternating cycles. The minimum n would be the maximum over all tilings of the minimum hitting set size.

Actually wait. Let me reconsider. The remaining region after fixing dominoes might have NEW tilings that don't come from alternating cycles of the original tiling. No - actually, the remaining region is a sub-region, and its tilings could be completely different from the original. The original tiling restricted to the remaining region is one valid tiling. For it to be unique, there should be no other tiling of that region.

Two tilings of the same region differ by a set of alternating cycles (this is a classical result). So the original tiling of the remaining region is unique iff there are no alternating cycles in it.

An alternating cycle in the remaining region's tiling is a cycle in the remaining region. Such a cycle is also an alternating cycle in the original tiling (since the dominoes in the remaining region are the same as in the original tiling, just restricted). So yes, the condition is that every alternating cycle of the original tiling must pass through at least one fixed domino.

So we need: minimum n such that for any tiling, Viktor can find a set of n dominoes that hits all alternating cycles.

Now, what do alternating cycles look like? In a domino tiling, consider the "domino graph" or think of it in terms of the grid.

Let me think about this differently. Consider the dual perspective. Color the board in checkerboard pattern. Each domino covers one black and one white cell. 

An alternating cycle: a cycle of cells c_1, c_2, ..., c_{2k} where dominoes cover (c_1,c_2), (c_3,c_4), ..., (c_{2k-1},c_{2k}) and the alternative tiling covers (c_2,c_3), (c_4,c_5), ..., (c_{2k},c_1). The cells c_1, ..., c_{2k} form a cycle in the grid graph.

So an alternating cycle is a cycle in the grid graph where the original tiling's dominoes are every other edge of the cycle.

Now, the question is about the structure of these cycles and how to hit them.

Let me think about a specific tiling. Consider the "all horizontal" tiling where every domino is horizontal. In row i, dominoes cover cells (i, 2j-1) and (i, 2j) for j=1,...,1011.

What are the alternating cycles? An alternating cycle needs consecutive dominoes to be adjacent. Two horizontal dominoes in the same row are adjacent if they share a vertical edge. Domino j covers columns 2j-1, 2j. Domino j+1 covers columns 2j+1, 2j+2. They share the edge between column 2j and 2j+1. So we can form an alternating cycle using dominoes j and j+1 in the same row: cells (i, 2j-1), (i, 2j), (i, 2j+1), (i, 2j+2) form a 4-cycle (actually a path of 4 cells, which with the right edges forms a 4-cycle... wait, 4 cells in a row don't form a cycle).

Hmm, let me reconsider. A 4-cycle in the grid is a 2×2 square. In the all-horizontal tiling, a 2×2 square in rows i, i+1 and columns 2j-1, 2j has dominoes (i, 2j-1)-(i, 2j) and (i+1, 2j-1)-(i+1, 2j). The alternative tiling would be (i, 2j-1)-(i+1, 2j-1) and (i, 2j)-(i+1, 2j). So yes, every 2×2 square aligned with the dominoes is an alternating cycle.

Also, a 2×2 square in columns 2j, 2j+1: dominoes (i, 2j-1)-(i, 2j) covers column 2j in row i, and (i, 2j+1)-(i, 2j+2) covers column 2j+1 in row i. But the 2×2 square in rows i, i+1, columns 2j, 2j+1: the cells are (i, 2j), (i, 2j+1), (i+1, 2j), (i+1, 2j+1). The original dominoes covering these: (i, 2j) is covered by domino (i, 2j-1)-(i, 2j), (i, 2j+1) is covered by (i, 2j+1)-(i, 2j+2), (i+1, 2j) by (i+1, 2j-1)-(i+1, 2j), (i+1, 2j+1) by (i+1, 2j+1)-(i+1, 2j+2). So the 2×2 square has parts of 4 different dominoes. This is NOT an alternating cycle because the domino edges don't alternate properly along the cycle.

So in the all-horizontal tiling, the alternating 4-cycles are exactly the 2×2 squares in columns (2j-1, 2j) for each j. There are 2021 × 1011 such squares.

But there could be larger alternating cycles too. For example, a cycle going around a larger region.

Actually, let me think about what alternating cycles exist in the all-horizontal tiling more carefully. 

An alternating cycle is a cycle in the grid graph where every other edge is a domino edge. The domino edges are all horizontal: (i, 2j-1)-(i, 2j). 

A cycle in the grid graph alternates between horizontal and vertical edges (not necessarily, but let's think about it). For an alternating cycle, the domino edges (every other edge) must be horizontal domino edges. 

Consider a cycle of length 2k. The edges are e_1, e_2, ..., e_{2k}. Dominoes are on e_1, e_3, ..., e_{2k-1} (say). These must be horizontal domino edges. The other edges e_2, e_4, ..., e_{2k} are the "flip" edges.

For a 4-cycle (2×2 square), the four edges going around: if the square is in columns 2j-1, 2j, the bottom edge (horizontal) is a domino edge, the top edge (horizontal) is a domino edge, and the two vertical edges are flip edges. This works.

For larger cycles, consider a "staircase" pattern. Actually, let me think about whether there are alternating cycles that span multiple rows.

Consider a 6-cycle. Take cells forming an L-shape or something. Actually, in a grid, cycles must enclose some region. 

Let me think about a specific larger alternating cycle. Consider rows 1, 2, 3 and columns 1, 2, 3. The dominoes are: row 1: (1,1)-(1,2), (1,3)-(1,4)...; row 2: (2,1)-(2,2), (2,3)-(2,4)...; row 3: (3,1)-(3,2), (3,3)-(3,4)...

Consider the cycle: (1,1)→(1,2)→(2,2)→(2,3)→(3,3)→(3,2)→(2,2)... no, that repeats.

Hmm, let me think about a 6-cycle. (1,1)→(1,2) [domino] →(2,2) [flip, vertical] →(2,3) [flip, horizontal] →(3,3) [flip, vertical]... no, this doesn't work because we need alternating domino/flip edges.

Let me be more careful. Cycle: v_1 → v_2 → v_3 → v_4 → v_5 → v_6 → v_1. Dominoes on (v_1,v_2), (v_3,v_4), (v_5,v_6). Flip edges: (v_2,v_3), (v_4,v_5), (v_6,v_1).

Domino edges must be horizontal domino edges from the tiling. So (v_1,v_2) is a horizontal domino, (v_3,v_4) is a horizontal domino, (v_5,v_6) is a horizontal domino.

The flip edges connect v_2 to v_3, v_4 to v_5, v_6 to v_1. These can be horizontal or vertical.

Example: v_1=(1,1), v_2=(1,2) [domino (1,1)-(1,2)], v_3=(2,2), v_4=(2,1) [domino (2,1)-(2,2)], v_5=(3,1), v_6=(3,2) [domino (3,1)-(3,2)]. 

Flip edges: (1,2)→(2,2) [vertical], (2,1)→(3,1) [vertical], (3,2)→(1,1) [???]. (3,2) to (1,1) is not an edge in the grid. So this doesn't work.

Let me try: v_1=(1,1), v_2=(1,2), v_3=(2,2), v_4=(2,3), v_5=(1,3), v_6=(1,2)... no, v_6=v_2.

Hmm, it seems like in the all-horizontal tiling, the only alternating cycles might be the 2×2 squares. Let me think about why.

Actually, consider a cycle that goes through multiple rows. The domino edges are all horizontal. The flip edges must connect the end of one domino to the start of the next. 

If a domino is (i, 2j-1)-(i, 2j), the right end is (i, 2j) and the left end is (i, 2j-1). The next domino's left end must be adjacent to (i, 2j) via a flip edge. (i, 2j) is adjacent to (i, 2j+1) [horizontal], (i-1, 2j) [vertical], (i+1, 2j) [vertical].

If the flip edge is horizontal: (i, 2j)→(i, 2j+1), then the next domino starts at (i, 2j+1), so it's (i, 2j+1)-(i, 2j+2). Then the right end is (i, 2j+2), and we continue. This just extends along the row.

If the flip edge is vertical: (i, 2j)→(i+1, 2j), then the next domino starts at (i+1, 2j). But dominoes in row i+1 are (i+1, 2k-1)-(i+1, 2k). So (i+1, 2j) is the right end of domino (i+1, 2j-1)-(i+1, 2j). So the next domino would be (i+1, 2j-1)-(i+1, 2j), meaning v_3 = (i+1, 2j-1), v_4 = (i+1, 2j). Then the flip edge from v_4 = (i+1, 2j) goes to... 

Wait, I need to be more careful about the direction. Let me reconsider.

In the cycle v_1, v_2, ..., v_{2k}, the domino covers (v_1, v_2). The direction matters: v_2 is connected to v_3 by a flip edge. So if the domino is (i, 2j-1)-(i, 2j), we could have v_1 = (i, 2j-1), v_2 = (i, 2j) or v_1 = (i, 2j), v_2 = (i, 2j-1).

Case 1: v_2 = (i, 2j) (right end). Flip edge from (i, 2j) to v_3.
  - Horizontal right: v_3 = (i, 2j+1), then domino (v_3, v_4) = (i, 2j+1)-(i, 2j+2), v_4 = (i, 2j+2).
  - Vertical down: v_3 = (i+1, 2j), then domino (v_3, v_4). (i+1, 2j) is the right end of domino (i+1, 2j-1)-(i+1, 2j). So v_3 = (i+1, 2j), v_4 = (i+1, 2j-1). Then flip from (i+1, 2j-1).
  - Vertical up: v_3 = (i-1, 2j), then domino (v_3, v_4). (i-1, 2j) is the right end of domino (i-1, 2j-1)-(i-1, 2j). So v_4 = (i-1, 2j-1). Then flip from (i-1, 2j-1).

Case 2: v_2 = (i, 2j-1) (left end). Flip edge from (i, 2j-1) to v_3.
  - Horizontal left: v_3 = (i, 2j-2), then domino (i, 2j-2)-(i, 2j-3)? No, domino is (i, 2j-3)-(i, 2j-2) if j > 1. So v_3 = (i, 2j-2), v_4 = (i, 2j-3).
  - Vertical: v_3 = (i±1, 2j-1), which is the left end of domino (i±1, 2j-1)-(i±1, 2j). So v_4 = (i±1, 2j).

So the cycle can move between rows. Let me trace a specific cycle.

Start: v_1 = (1,1), v_2 = (1,2) [domino in row 1]. Flip down: v_3 = (2,2), which is right end of domino (2,1)-(2,2). So v_4 = (2,1). Flip down: v_5 = (3,1), which is left end of domino (3,1)-(3,2). So v_6 = (3,2). Flip up: v_7 = (2,2)... but that's v_3, so we'd be repeating. 

Let me try: v_1 = (1,1), v_2 = (1,2). Flip down: v_3 = (2,2), v_4 = (2,1). Flip left: v_5 = (2,0)... out of bounds. 

Flip up from v_4 = (2,1): v_5 = (1,1) = v_1. That's a 4-cycle: (1,1)-(1,2)-(2,2)-(2,1)-(1,1). This is the 2×2 square.

Let me try a longer cycle. v_1 = (1,1), v_2 = (1,2). Flip right: v_3 = (1,3), v_4 = (1,4). Flip down: v_5 = (2,4), which is right end of domino (2,3)-(2,4). v_6 = (2,3). Flip left: v_7 = (2,2), which is right end of domino (2,1)-(2,2). v_8 = (2,1). Flip up: v_9 = (1,1) = v_1. 

So the cycle is: (1,1)-(1,2)-(1,3)-(1,4)-(2,4)-(2,3)-(2,2)-(2,1)-(1,1). This is an 8-cycle going around a 2×4 rectangle... wait, it's a 2×2 rectangle extended. Actually it's the boundary of a 2×4 region? No, it's the boundary of a 2×2 region in columns 1-4... no.

The cycle visits: (1,1), (1,2), (1,3), (1,4), (2,4), (2,3), (2,2), (2,1). This is the boundary of the 2×4 rectangle (rows 1-2, columns 1-4). But wait, the dominoes on this cycle are: (1,1)-(1,2), (1,3)-(1,4), (2,3)-(2,4), (2,1)-(2,2). And the flip edges are: (1,2)-(1,3), (1,4)-(2,4), (2,4)-(2,3)... wait, (2,4) to (2,3) is a flip edge, but (2,3)-(2,4) is a domino. Let me recheck.

The cycle: v_1=(1,1), v_2=(1,2), v_3=(1,3), v_4=(1,4), v_5=(2,4), v_6=(2,3), v_7=(2,2), v_8=(2,1), back to v_1=(1,1).

Dominoes: (v_1,v_2) = (1,1)-(1,2) ✓, (v_3,v_4) = (1,3)-(1,4) ✓, (v_5,v_6) = (2,4)-(2,3) ✓ (same as domino (2,3)-(2,4)), (v_7,v_8) = (2,2)-(2,1) ✓ (same as domino (2,1)-(2,2)).

Flip edges: (v_2,v_3) = (1,2)-(1,3) ✓ horizontal, (v_4,v_5) = (1,4)-(2,4) ✓ vertical, (v_6,v_7) = (2,3)-(2,2) ✓ horizontal, (v_8,v_1) = (2,1)-(1,1) ✓ vertical.

Yes! This is an alternating 8-cycle. The flip would give dominoes: (1,2)-(1,3), (1,4)-(2,4), (2,3)-(2,2), (2,1)-(1,1). So this is a valid alternating cycle.

So there ARE larger alternating cycles. The 2×4 rectangle boundary is an alternating cycle. More generally, any 2×2k rectangle boundary is an alternating cycle (in the all-horizontal tiling).

Actually, even more generally, we can have cycles that span more rows. Let me think...

From the analysis above, when we go down from a row, we can either go back up (creating a 4-cycle) or continue horizontally and then go back up later. 

Actually, the key insight is: in the all-horizontal tiling, an alternating cycle corresponds to a cycle in a certain graph. Let me think about what graph.

Consider the "contracted" graph where each domino is a vertex. Two dominoes are connected if they share a flip edge (i.e., you can flip between them). An alternating cycle in the tiling corresponds to a cycle in this contracted graph.

Hmm, this is getting complex. Let me think about the problem from a higher level.

The problem is asking for the minimum n such that Viktor can always force a win. This is a competition problem, so the answer is likely a clean expression.

Let me think about what structures force uniqueness. 

Key idea: A domino tiling is unique (frozen) if and only if there are no alternating cycles. 

For Viktor to win, he needs to fix dominoes so that the remaining tiling has no alternating cycles. This means every alternating cycle must contain at least one fixed domino.

The question is: what's the maximum over all tilings T of the minimum number of dominoes needed to hit all alternating cycles of T?

Let me think about the all-horizontal tiling and its alternating cycles.

In the all-horizontal tiling, I showed that 2×2k rectangles (for any k) give alternating cycles. Also, we can have more complex shapes.

Actually, let me think about this differently. Consider the all-horizontal tiling. The alternating cycles are exactly the cycles in the "flip graph" of the tiling. 

Let me think about which 2×2 squares are alternating cycles. A 2×2 square in rows i, i+1 and columns j, j+1 is an alternating cycle iff the dominoes are arranged as two horizontal dominoes (one in each row) that can be flipped to two vertical dominoes. This happens when j is odd (so columns j, j+1 = 2k-1, 2k for some k). When j is even (columns 2k, 2k+1), the 2×2 square has 4 different dominoes touching it, so it's not an alternating cycle.

So the "flippable" 2×2 squares are those in columns (1,2), (3,4), ..., (2021,2022), and all pairs of consecutive rows. There are 1011 × 2021 such squares.

Now, to hit all alternating cycles, we need to hit at least all these 2×2 squares (since they're alternating cycles). But also the larger cycles.

Hmm, but hitting all 2×2 squares doesn't necessarily hit all larger cycles. A larger cycle might not contain any 2×2 square as a sub-cycle... actually, any alternating cycle of length > 4 can be decomposed, but that's not quite right either.

Let me think about this differently. 

Actually, I recall that for domino tilings, the set of all tilings of a region forms a distributive lattice, and two tilings are connected by flips. The "flip graph" has tilings as vertices and flips (2×2 rotations) as edges. But here we're not just looking at 2×2 flips; we're looking at arbitrary alternating cycles.

However, any alternating cycle can be decomposed into a sequence of 2×2 flips? No, that's not right. An alternating cycle flip is a single operation that changes multiple dominoes at once.

But actually, the key theorem is: two tilings of a region differ by a set of disjoint alternating cycles. And the flip graph (using 2×2 flips) is connected - any tiling can be reached from any other by a sequence of 2×2 flips. 

But for our problem, we need the tiling to be the UNIQUE tiling, which means no alternating cycles at all (not just no 2×2 flippable squares).

Hmm wait, but if there's an alternating cycle of length > 4, can it be that no 2×2 sub-square is flippable? Let me check with the 8-cycle example above.

The 8-cycle was the boundary of the 2×4 rectangle (rows 1-2, columns 1-4). The 2×2 squares within this rectangle are: columns (1,2) and columns (3,4) in rows (1,2). Both of these are flippable 2×2 squares (columns 1,2 and 3,4 are both odd-even pairs). So this 8-cycle contains two flippable 2×2 squares.

Is it always the case that an alternating cycle contains a flippable 2×2 square? 

Consider an alternating cycle. It's a cycle in the grid where every other edge is a domino. Consider two consecutive dominoes on the cycle. They're connected by a flip edge. The two dominoes and the flip edge form a path of 4 cells. If these 4 cells form a 2×2 square, then it's a flippable square. But they might form a "straight" path (4 cells in a row or column).

In the all-horizontal tiling, if two consecutive dominoes are in the same row and connected by a horizontal flip edge, the 4 cells are in a row - not a 2×2 square. If they're in adjacent rows connected by a vertical flip edge, the 4 cells form a 2×2 square.

So in the 8-cycle example, the flip edges were: (1,2)-(1,3) [horizontal, same row], (1,4)-(2,4) [vertical, different rows], (2,3)-(2,2) [horizontal, same row], (2,1)-(1,1) [vertical, different rows]. The vertical flip edges create 2×2 squares: (1,4)-(2,4) with dominoes (1,3)-(1,4) and (2,3)-(2,4) gives the 2×2 square in columns 3,4; and (2,1)-(1,1) with dominoes (2,1)-(2,2) and (1,1)-(1,2) gives the 2×2 square in columns 1,2.

So in this case, the alternating cycle does contain flippable 2×2 squares. 

Is it possible to have an alternating cycle with NO flippable 2×2 squares? That would require all flip edges to be "straight" (same row or same column as the dominoes). In the all-horizontal tiling, dominoes are horizontal. A flip edge between two dominoes in the same row is horizontal (straight). A flip edge between dominoes in different rows is vertical (creating a 2×2 square). 

For a cycle, we need to eventually return to the starting point. If all flip edges are horizontal (same row), the cycle stays in one row. But a cycle in one row of a grid is impossible (a row is a path, not a cycle - well, unless it wraps around, but it doesn't). So any alternating cycle must have at least one vertical flip edge, which creates a flippable 2×2 square.

Wait, that's for the all-horizontal tiling. Let me verify: if the cycle stays in one row, the dominoes are all in that row, and the flip edges are all horizontal. The cycle would be: domino, flip right, domino, flip right, ... but to close the cycle, we'd need to come back, which requires going left. But going left from a domino's right end means the flip edge goes left, and the next domino is to the left. So the cycle would alternate going right and left, which means it can't make progress and close. Actually, in a single row, the only cycles are... there are no cycles in a single row (a path graph has no cycles). So yes, any alternating cycle must span at least 2 rows, and thus has at least one vertical flip edge, creating a flippable 2×2 square.

So for the all-horizontal tiling: every alternating cycle contains at least one flippable 2×2 square. Therefore, hitting all flippable 2×2 squares is sufficient to hit all alternating cycles.

Now, the flippable 2×2 squares are in columns (1,2), (3,4), ..., (2021,2022) and rows (1,2), (2,3), ..., (2021,2022). Each such square involves 2 dominoes (one in each row). To hit a 2×2 square, we need to fix at least one of its 2 dominoes.

This is a covering problem. We have a grid of 2×2 squares: 2021 rows of squares × 1011 columns of squares. Each square needs one of its 2 dominoes fixed. Each domino is in exactly one square (in the column sense - each domino (i, 2j-1)-(i, 2j) is part of the square in columns (2j-1, 2j) and rows (i-1, i) or (i, i+1)).

Wait, let me reconsider. Each domino (i, 2j-1)-(i, 2j) is part of two 2×2 squares: the one in rows (i-1, i) and columns (2j-1, 2j), and the one in rows (i, i+1) and columns (2j-1, 2j). (Except for dominoes in the first or last row, which are part of only one square.)

So the structure is: for each column pair (2j-1, 2j), we have a column of 2021 squares (between consecutive rows), and 2022 dominoes (one per row). Each domino is shared between at most 2 consecutive squares. We need to select dominoes to hit all squares.

For a single column pair, this is like a path of 2021 vertices (squares) and 2022 edges (dominoes), where each edge covers its two endpoints. We need a vertex cover... no, we need to select edges to cover all vertices. This is an edge cover problem. The minimum edge cover of a path of 2021 vertices is ceil(2021/2) = 1011.

Wait, actually, the minimum number of edges to cover all vertices in a path of n vertices is ceil(n/2). For n=2021, that's 1011.

But we have 1011 column pairs, and the dominoes in different column pairs are different. So the total minimum is 1011 × 1011 = 1011² = 1,022,121.

Hmm wait, but is this the right calculation? Let me reconsider.

For each column pair j (j = 1, ..., 1011), we have a path of 2021 squares (rows 1-2, 2-3, ..., 2021-2022) and 2022 dominoes (rows 1, 2, ..., 2022). We need to select dominoes in this column pair to cover all 2021 squares. The minimum is ceil(2021/2) = 1011.

Since the column pairs are independent (different dominoes), the total minimum is 1011 × 1011 = 1011².

But wait, is this the minimum for the all-horizontal tiling, or could there be a better strategy? Also, is the all-horizontal tiling the worst case?

Let me reconsider whether the all-horizontal tiling is indeed the worst case, or if there's a tiling that requires more fixed dominoes.

Actually, let me reconsider the problem. The answer might be 1011² = 1022121, but that seems like a strange answer for a competition. Let me reconsider.

Hmm, 2022 = 2 × 1011. So 1011² = (2022/2)² = 2022²/4. The board has 2022² cells and 2022²/2 dominoes. So n = 2022²/4 = (number of dominoes)/2.

Actually wait, let me reconsider. Maybe the answer is simpler.

Let me think about this problem from a different angle. 

Actually, I want to reconsider whether hitting all 2×2 flippable squares is sufficient, and whether the all-horizontal tiling is the worst case.

For a general tiling, the situation is more complex. Let me think about what the worst-case tiling looks like.

Actually, let me reconsider the problem. The key question is: what is the minimum n such that for ANY tiling, Viktor can find n dominoes to fix that make the remaining tiling unique?

Let me think about lower bounds. Sofia wants to maximize the number of dominoes Viktor needs. So Sofia chooses a tiling that's "hard" for Viktor.

For the all-horizontal tiling, we showed Viktor needs at least 1011² dominoes (to hit all flippable 2×2 squares, which hit all alternating cycles). But maybe there's a tiling that requires even more.

Wait, actually I need to also check that 1011² is sufficient for the all-horizontal tiling, i.e., that hitting all flippable 2×2 squares indeed hits all alternating cycles. I argued this above: any alternating cycle must have a vertical flip edge, which creates a flippable 2×2 square. So yes, hitting all flippable 2×2 squares is sufficient.

Now, is the all-horizontal tiling the worst case? Let me think about other tilings.

Consider a "brick" tiling where rows alternate between horizontal and vertical dominoes. Or consider a tiling with a mix.

Actually, let me think about a different approach. The problem might have a cleaner answer.

Let me reconsider. The board is 2022 × 2022. Let me think about what happens with a general tiling.

For a general tiling, the flippable 2×2 squares are those where two parallel dominoes form a 2×2 square. Not all 2×2 squares are flippable in a general tiling.

The key insight might be: in any tiling, the number of flippable 2×2 squares is at least something, and we need to hit all of them (plus possibly larger alternating cycles).

Hmm, but this is getting complicated. Let me think about the problem differently.

Alternative approach: Think about the problem in terms of "forcing" the tiling. 

A set of fixed dominoes "forces" the rest of the tiling if the remaining region has a unique tiling. We want the minimum size of a forcing set, maximized over all tilings.

This is related to the concept of "forcing number" in domino tilings. The forcing number of a tiling is the minimum number of dominoes that need to be fixed to make the tiling unique. We want the maximum forcing number over all tilings of the 2022 × 2022 board.

The forcing number of domino tilings has been studied. Let me recall...

For a tiling of an m × n board, the forcing number is related to the maximum number of disjoint alternating cycles. By a theorem (related to the Kőnig-type theorem), the forcing number equals the maximum number of disjoint alternating cycles.

Wait, is that right? The forcing number (minimum hitting set for all alternating cycles) equals the maximum number of pairwise disjoint alternating cycles, by the Kőnig-Egerváry theorem (since the alternating cycles form a clutter, and if the clutter is "Mengerian" or has the Kőnig property...).

Actually, for domino tilings, there's a result that the minimum forcing number equals the maximum number of disjoint alternating cycles. This is because the "cycle space" of a tiling has a nice structure.

Hmm, I'm not sure about the exact theorem. Let me think about it from scratch.

For the all-horizontal tiling of the 2022 × 2022 board, the flippable 2×2 squares are in columns (1,2), (3,4), ..., (2021,2022) and row-pairs (1,2), (2,3), ..., (2021,2022). That's 1011 × 2021 squares.

The maximum number of disjoint flippable 2×2 squares: in each column pair, the squares are in a path (rows 1-2, 2-3, ..., 2021-2022), so the maximum independent set (disjoint squares) is ceil(2021/2) = 1011 per column pair. Wait, actually, two squares in the same column pair are disjoint if they don't share a row. Squares (i, i+1) and (j, j+1) share a row iff |i-j| = 1. So the maximum number of pairwise disjoint squares in a column pair is the maximum independent set of a path of 2021 vertices, which is ceil(2021/2) = 1011.

Squares in different column pairs are always disjoint (they use different columns). So the maximum number of disjoint flippable 2×2 squares is 1011 × 1011 = 1011².

If the forcing number equals the maximum number of disjoint alternating cycles, then the forcing number for the all-horizontal tiling is 1011². And if this is the maximum over all tilings, then the answer is 1011².

But I need to verify: (1) the forcing number equals the max number of disjoint alternating cycles, and (2) the all-horizontal tiling achieves the maximum.

For (1): This is a min-max theorem. The set of alternating cycles forms a family, and we want the minimum hitting set. By LP duality, the min hitting set equals the max fractional packing. For the integral version, we need the family to have the Kőnig property. For domino tiling alternating cycles, I believe this holds because the structure is bipartite (or more precisely, the "cycle hypergraph" is totally balanced or something).

Actually, let me think about this more carefully. The alternating cycles of a domino tiling correspond to cycles in a certain graph. Specifically, consider the graph G whose vertices are the dominoes, and two dominoes are adjacent if they share a flip edge (i.e., there's a 2×2 square containing both). Then alternating cycles correspond to cycles in G? Not exactly, because alternating cycles can be longer than 4.

Hmm, let me think again. Actually, there's a classical result that for domino tilings of simply connected regions, the minimum forcing number equals the maximum number of disjoint alternating cycles. This is proven using the fact that the set of tilings forms a distributive lattice and the alternating cycles have a nice structure.

Let me just assume this is true and proceed. Then the forcing number of a tiling = max number of disjoint alternating cycles.

For the all-horizontal tiling, the max number of disjoint alternating cycles is at least 1011² (from the disjoint 2×2 squares). And the forcing number is at most 1011² (since hitting all 2×2 squares suffices, and we need 1011² to hit them). So the forcing number is exactly 1011².

Now, is 1011² the maximum over all tilings? Let me think about upper bounds.

For any tiling of the 2022 × 2022 board, what's the maximum number of disjoint alternating cycles?

An alternating cycle uses at least 4 cells (a 2×2 square). The board has 2022² cells. So the maximum number of disjoint alternating cycles is at most 2022²/4 = 1011².

And the all-horizontal tiling achieves this bound (with 1011² disjoint 2×2 squares). So the maximum forcing number is 1011².

Wait, but I need to be more careful. An alternating cycle uses at least 4 cells, but the 2×2 squares in the all-horizontal tiling use exactly 4 cells each, and there are 1011² of them, using 4 × 1011² = 4 × 1022121 = 4088484 cells. The board has 2022² = 4088484 cells. So they use ALL the cells! That means the 1011² disjoint 2×2 squares partition the entire board.

Let me verify: 1011 column pairs × 1011 row-pairs (every other row-pair) = 1011² squares, each 2×2, covering 4 × 1011² = 4 × 1011² cells. And 2022² = 4 × 1011². Yes, they partition the board.

So the maximum number of disjoint alternating cycles is exactly 1011² (since each uses ≥ 4 cells and the board has 4 × 1011² cells, and the all-horizontal tiling achieves this).

Therefore, the answer is n = 1011² = 1022121.

But wait, I need to double-check the min-max theorem. Let me think about whether the forcing number really equals the max number of disjoint alternating cycles.

The forcing number is the minimum number of dominoes to hit all alternating cycles. The max number of disjoint alternating cycles is a lower bound on the forcing number (since each disjoint cycle needs a separate domino to hit it). The question is whether equality holds.

For the all-horizontal tiling, we showed:
- Lower bound: 1011² (from disjoint 2×2 squares)
- Upper bound: 1011² (from hitting all 2×2 squares, which hits all alternating cycles)

So equality holds for this specific tiling. 

For the general case, we need: for any tiling, the forcing number ≤ 1011². Since the forcing number = max disjoint alternating cycles ≤ 1011² (because each alternating cycle uses ≥ 4 cells and the board has 4 × 1011² cells), we get forcing number ≤ 1011² for any tiling.

But wait, this uses the min-max theorem (forcing number = max disjoint alternating cycles). If this theorem doesn't hold, we only have forcing number ≥ max disjoint alternating cycles, and the upper bound doesn't follow.

Let me think about whether we can prove the upper bound directly.

Claim: For any tiling of the 2022 × 2022 board, Viktor can fix at most 1011² dominoes to make the tiling unique.

Proof approach: We need to show that for any tiling, there exists a set of 1011² dominoes that hits all alternating cycles.

Alternative: Show that the forcing number of any tiling is at most 1011².

Hmm, let me think about this differently. 

Actually, I think the key theorem is: for a domino tiling of a simply connected region, the minimum forcing number equals the maximum number of disjoint alternating cycles. This is a theorem by Pachter and Kim (or similar). Let me try to prove it or at least argue it.

The alternating cycles of a tiling form a set of cycles in the grid graph. The dominoes are the "edges" we want to hit. Each alternating cycle is a set of dominoes (every other edge of the cycle). We want the minimum hitting set for all alternating cycles.

This is a hitting set problem on a family of sets (each alternating cycle is a set of dominoes). The max disjoint cycles is the max packing. By LP duality, min hitting set = max fractional packing ≥ max integral packing = max disjoint cycles. For equality (min hitting set = max disjoint cycles), we need the family to be "ideal" or have the Kőnig property.

For domino tilings, I believe the alternating cycle family does have the Kőnig property. This might follow from the fact that the tiling's "height function" gives a nice structure to the cycles.

Let me try a different approach. Instead of relying on the min-max theorem, let me directly argue the upper bound.

Upper bound argument: For any tiling of the 2022 × 2022 board, we can find a set of at most 1011² dominoes that hits all alternating cycles.

Consider any tiling. Color the board in checkerboard pattern (black/white). Each domino covers one black and one white cell.

Now, consider the "domino graph" where we create a graph with the dominoes as vertices. Actually, let me think about the structure of alternating cycles differently.

An alternating cycle is a cycle in the grid graph that alternates between domino edges and non-domino edges. Consider the graph H whose edges are the non-domino edges of the grid (the "complement" edges). An alternating cycle alternates between domino edges and H-edges.

Hmm, this is getting complicated. Let me try yet another approach.

Let me think about the problem in terms of the "height function" of the tiling. Each domino tiling of a simply connected region has an associated height function on the vertices of the grid. The height function changes by ±1 or ±3 along edges, with specific rules. Alternating cycles correspond to "contours" of the height function where the height goes up and down.

Actually, I think the cleanest approach is:

1. Lower bound: The all-horizontal tiling requires at least 1011² fixed dominoes (from 1011² disjoint 2×2 alternating cycles).

2. Upper bound: For any tiling, at most 1011² dominoes suffice.

For the upper bound, I'll use the fact that the forcing number equals the maximum number of disjoint alternating cycles (which I'll state as a known theorem), and the latter is at most 1011² since each alternating cycle uses at least 4 cells.

Actually, let me try to prove the upper bound more directly.

Direct upper bound: Consider any tiling T of the 2022 × 2022 board. We want to find a set S of at most 1011² dominoes such that every alternating cycle of T contains a domino from S.

Consider the checkerboard coloring. Each domino covers one black and one white cell. There are 2022²/2 = 2 × 1011² black cells and the same number of white cells.

Now, consider the bipartite graph B where one part is the black cells and the other is the white cells, with edges being the dominoes. This is a perfect matching. An alternating cycle in the tiling corresponds to an alternating cycle in this matching (with respect to the grid graph).

The grid graph is also bipartite (black/white), and the domino tiling is a perfect matching in it. An alternating cycle is a cycle that alternates between matching edges (dominoes) and non-matching edges (grid edges not used by dominoes).

The minimum number of matching edges to hit all alternating cycles is related to the structure of the matching.

Hmm, I think I need to use a specific theorem. Let me recall: for a perfect matching in a bipartite graph, the minimum number of matching edges to remove to make the matching unique equals the maximum number of disjoint alternating cycles. This is a consequence of the Kőnig-Egerváry theorem applied to the "alternating cycle hypergraph."

Actually, I think this follows from the following: the set of alternating cycles of a perfect matching in a bipartite graph forms a "totally balanced hypergraph" or something similar, which has the Kőnig property.

Alternatively, there's a result that says: for a perfect matching M in a bipartite graph G, the minimum forcing number of M equals the maximum number of M-alternating cycles that are pairwise vertex-disjoint (in terms of the matched vertices, or equivalently, edge-disjoint in M).

Let me just assume this theorem and proceed. Then:

- For any tiling, forcing number = max disjoint alternating cycles ≤ ⌊2022²/4⌋ = 1011² (since each alternating cycle uses ≥ 4 cells, i.e., ≥ 2 dominoes, and there are 2022²/2 dominoes, so max disjoint cycles ≤ 2022²/4 = 1011²).

Wait, each alternating cycle uses at least 2 dominoes (4 cells), and the total number of dominoes is 2022²/2 = 2 × 1011². So max disjoint alternating cycles ≤ 2 × 1011² / 2 = 1011². Yes.

- The all-horizontal tiling achieves 1011² disjoint alternating cycles (the 2×2 squares partitioning the board).

So the answer is n = 1011² = 1022121.

Hmm wait, but I should double-check: 1011² = 1011 × 1011. Let me compute: 1011² = (1000 + 11)² = 1000000 + 22000 + 121 = 1022121.

And 2022²/4 = 4088484/4 = 1022121. Yes.

So n = 1011² = 2022²/4.

But let me reconsider whether the min-max theorem is actually needed, or if I can prove both bounds directly.

Lower bound (direct): The all-horizontal tiling has 1011² disjoint 2×2 alternating cycles (partition the board into 2×2 blocks in columns (1,2),(3,4),... and rows (1,2),(3,4),...). Each fixed domino can hit at most one of these (since they're disjoint), so Viktor needs at least 1011² dominoes.

Wait, I need to be more careful. The 2×2 blocks that partition the board are in rows (1,2), (3,4), (5,6), ..., (2021,2022) and columns (1,2), (3,4), ..., (2021,2022). That's 1011 row-pairs × 1011 column-pairs = 1011² blocks. Each block is a 2×2 square with two horizontal dominoes, which is an alternating cycle. These blocks are disjoint (they partition the board). Each domino belongs to exactly one block. So to hit all 1011² alternating cycles, Viktor needs at least 1011² dominoes (one per block).

Upper bound (direct): For any tiling, we need to show Viktor can win with 1011² dominoes. 

Hmm, the direct upper bound is harder without the min-max theorem. Let me think...

Actually, maybe I can prove the upper bound using a different argument. 

Consider any tiling T. We want to find a set S of at most 1011² dominoes that hits all alternating cycles.

Idea: Use a "chessboard" pattern of 2×2 blocks. Partition the board into 2×2 blocks (rows (1,2),(3,4),... and columns (1,2),(3,4),...). There are 1011² such blocks. In each block, there are at most 2 dominoes entirely within the block (if the block is covered by 2 dominoes), or dominoes crossing block boundaries.

Hmm, this doesn't directly work because dominoes can cross block boundaries.

Let me think differently. 

Alternative upper bound approach: Use the min-max theorem. The theorem states that for a perfect matching in a bipartite planar graph (or more specifically, for domino tilings of simply connected regions), the minimum forcing number equals the maximum number of disjoint alternating cycles.

This is actually a known result. Let me recall the reference: it's related to the work of Pachter and Kim (1998), or the work on "forcing numbers" in domino tilings. The key insight is that the alternating cycles of a domino tiling form a "laminar" or "non-crossing" family when viewed appropriately, which gives the Kőnig property.

Actually, I recall now: for domino tilings of simply connected regions, the minimum forcing number equals the maximum number of disjoint alternating cycles. This was proven using the theory of distributive lattices and the structure of the height function. The alternating cycles correspond to "cycles" in the height function, and the min-max theorem follows from the fact that these cycles can be "nested" but not "crossing," giving a totally balanced hypergraph.

Let me just state this as a lemma and prove the result.

Actually, let me try to prove the min-max theorem for this specific case.

Lemma: For any domino tiling of a simply connected region, the minimum forcing number equals the maximum number of disjoint alternating cycles.

Proof sketch: 
- Lower bound is clear: each disjoint alternating cycle needs a separate domino to hit it.
- Upper bound: We use the height function. The height function h is defined on the vertices of the grid. An alternating cycle corresponds to a closed contour where h changes by +3, -1, +3, -1, ... (or the reverse). The key property is that alternating cycles can be "nested" (one inside another) but if they're disjoint, they don't interact. 

Actually, I think the correct approach is to use the fact that the set of alternating cycles forms a "laminar family" when we consider the regions they enclose. Two alternating cycles either are disjoint (their enclosed regions don't overlap), or one's region is contained in the other's. Wait, that's not quite right either, since alternating cycles can partially overlap.

Hmm, let me think about this more carefully. Actually, for domino tilings, two alternating cycles can cross (share vertices but not edges). So the laminar property doesn't directly hold.

Let me try a different approach to the upper bound.

Direct upper bound using a greedy argument:

Consider any tiling T. We'll build a forcing set S greedily.

While there exists an alternating cycle C in the current tiling (of the remaining region):
  - Add one domino from C to S (removing it from the region).
  - This breaks C and possibly other cycles.

The question is: how many dominoes do we need to add?

Each time we add a domino, we remove 2 cells from the region. The remaining region might have new tilings, but we're working with the original tiling restricted to the remaining region.

The number of alternating cycles we need to break is at most the initial number of disjoint alternating cycles, which is at most 1011². But a single domino might break multiple cycles, so the greedy approach might use fewer.

Actually, the greedy approach gives at most (max disjoint alternating cycles) dominoes, because each domino we add breaks at least one "independent" cycle. This is essentially the proof of the min-max theorem for "balanced" hypergraphs.

Hmm, I think I'm overcomplicating this. Let me just state the min-max theorem as a known result and use it.

Actually, for competition math, I think the expected approach is:

1. Show the lower bound: the all-horizontal tiling requires ≥ 1011².
2. Show the upper bound: any tiling can be forced with ≤ 1011².
3. Conclude n = 1011².

For the upper bound, the key is: the maximum number of disjoint alternating cycles in any tiling is at most 1011² (since each uses ≥ 4 cells and the board has 4 × 1011² cells). And by the min-max theorem (forcing number = max disjoint alternating cycles), the forcing number is at most 1011².

But if this is a competition, maybe they expect a more elementary proof. Let me think about whether there's a simpler upper bound argument.

Simpler upper bound: For any tiling, consider the 1011² disjoint 2×2 blocks (rows (2i-1, 2i), columns (2j-1, 2j) for i, j = 1, ..., 1011). In each block, the 4 cells are covered by some dominoes. 

Case 1: The block is covered by 2 dominoes entirely within the block. Then those 2 dominoes form an alternating cycle (a 2×2 flippable square). Fix one of them.

Case 2: Some dominoes cross the block boundary. Then the block's cells are covered by dominoes that extend outside the block.

In Case 2, we can't simply fix a domino in the block. But maybe we can argue that the crossing dominoes already "connect" blocks in a way that reduces the total number of alternating cycles.

This is getting complicated. Let me try yet another approach.

Actually, I think the cleanest approach for a competition is:

Lower bound: All-horizontal tiling, partition into 2×2 blocks, 1011² disjoint alternating cycles, need ≥ 1011².

Upper bound: For any tiling, the maximum number of disjoint alternating cycles is ≤ 1011² (trivial: each uses ≥ 4 cells). By the min-max theorem for domino tilings (forcing number = max disjoint alternating cycles), the forcing number is ≤ 1011².

The min-max theorem can be stated and briefly justified.

Let me now also verify: is the min-max theorem actually true? Let me think of a potential counterexample.

Consider a 2×4 board with the tiling: (1,1)-(1,2), (1,3)-(2,3), (2,1)-(2,2), (1,4)-(2,4). Hmm, let me think of a specific example.

2×4 board, tiling: horizontal dominoes (1,1)-(1,2), (1,3)-(1,4), (2,1)-(2,2), (2,3)-(2,4). This is the all-horizontal tiling. Alternating cycles: the 2×2 square in columns 1-2 (rows 1-2), and the 2×2 square in columns 3-4 (rows 1-2). These are disjoint. Forcing number = 2 (fix one domino in each square). Max disjoint cycles = 2. ✓

Another tiling of 2×4: (1,1)-(1,2), (2,1)-(2,2), (1,3)-(2,3), (1,4)-(2,4). Alternating cycles: the 2×2 square in columns 1-2 (flippable: two horizontal dominoes). The 2×2 square in columns 2-3: cells (1,2),(1,3),(2,2),(2,3). Dominoes: (1,2) is covered by (1,1)-(1,2), (1,3) by (1,3)-(2,3), (2,2) by (2,1)-(2,2), (2,3) by (1,3)-(2,3). Wait, (1,3) and (2,3) are both covered by the same domino. So the 2×2 square in columns 2-3 has 3 dominoes touching it, not an alternating cycle.

The 2×2 square in columns 3-4: cells (1,3),(1,4),(2,3),(2,4). Dominoes: (1,3)-(2,3) and (1,4)-(2,4). These are two vertical dominoes. Flipping gives (1,3)-(1,4) and (2,3)-(2,4). So this IS an alternating cycle.

So the alternating cycles are: 2×2 in columns 1-2 (horizontal), 2×2 in columns 3-4 (vertical). These are disjoint. Forcing number = 2. Max disjoint = 2. ✓

Now, is there a longer alternating cycle? The 2×4 rectangle boundary: cells (1,1),(1,2),(1,3),(1,4),(2,4),(2,3),(2,2),(2,1). Dominoes on this cycle: (1,1)-(1,2), then flip (1,2)-(1,3), then... (1,3) is covered by (1,3)-(2,3), so the domino edge is (1,3)-(2,3) which is vertical. But in the cycle, after (1,2) we go to (1,3) (horizontal flip), then the next domino edge should be (1,3)-(1,4) but (1,3) is covered by the vertical domino (1,3)-(2,3), not by (1,3)-(1,4). So the 2×4 boundary is NOT an alternating cycle in this tiling.

OK so in this tiling, the only alternating cycles are the two 2×2 squares. Forcing number = 2 = max disjoint. ✓

Let me try to think of a case where the min-max might fail... Consider a 4×4 board with a tiling that has a "crossing" pair of alternating cycles.

Actually, I think the min-max theorem does hold for domino tilings of simply connected regions. This is because the alternating cycles correspond to cycles in a planar graph, and the hitting set problem on cycles in a planar graph has the Kőnig property (by a result related to the Lucchesi-Younger theorem or similar).

More specifically, the alternating cycles of a domino tiling correspond to cycles in the "residual graph" (the graph of non-matching edges, combined with matching edges). The minimum number of matching edges to hit all alternating cycles equals the maximum number of edge-disjoint alternating cycles, by the Kőnig-Egerváry theorem for bipartite graphs (since the grid graph is bipartite).

Wait, actually, let me think about this more carefully. The alternating cycles are cycles in the graph G (the grid graph) that alternate between matching edges (dominoes) and non-matching edges. We want to hit all such cycles by removing matching edges.

Consider the directed graph D obtained by directing matching edges from white to black and non-matching edges from black to white (or some consistent orientation). Then alternating cycles correspond to directed cycles in D. We want to hit all directed cycles by removing matching edges.

By the Lucchesi-Younger theorem (or its bipartite special case), the minimum number of edges to remove to make a directed graph acyclic equals the maximum number of edge-disjoint directed cycles. But we're only allowed to remove matching edges, not all edges.

Hmm, this is a constrained version. Let me think...

Actually, in the bipartite case, there's a cleaner result. The grid graph is bipartite (black/white cells). The perfect matching M (domino tiling) matches black to white. An alternating cycle is a cycle alternating between M-edges and non-M-edges.

The minimum number of M-edges to hit all alternating cycles: this is the minimum "forcing number." 

The maximum number of M-edge-disjoint alternating cycles: each such cycle uses 2 or more M-edges, and they share no M-edges.

I claim: min forcing number = max M-edge-disjoint alternating cycles.

This follows from the fact that the "alternating cycle space" has a totally unimodular constraint matrix, which gives integral LP duality. The total unimodularity comes from the bipartite structure of the grid graph.

More concretely: consider the bipartite graph G = (B, W, E) where B and W are black and white cells. M is a perfect matching. The non-matching edges are E \ M. An alternating cycle uses edges alternately from M and E \ M.

Define a flow network: for each non-matching edge (w, b) (from white to black), and each matching edge (b, w) (from black to white), create a directed graph. Alternating cycles become directed cycles. The min hitting set (removing M-edges to break all directed cycles) is a "feedback arc set" restricted to M-edges.

For bipartite graphs, the constraint matrix of the cycle-hitting LP is totally unimodular (this is because the cycle-edge incidence matrix of a directed graph is totally unimodular, and restricting to M-edges preserves this). Therefore, the LP has integral optimal solutions, and min hitting set = max fractional packing ≥ max integral packing = max disjoint cycles. And since min hitting set ≤ max disjoint cycles is NOT generally true... wait, we have min hitting set ≥ max disjoint cycles always (each disjoint cycle needs a separate edge). And by LP duality with TU, min hitting set = max fractional packing. But max fractional packing ≥ max integral packing = max disjoint cycles. So min hitting set ≥ max disjoint cycles, but we need equality.

Hmm, so TU gives us min hitting set = max fractional packing, but we need max fractional packing = max integral packing, which requires the packing LP to also have integral optimal solutions. This would require the dual constraint matrix to also be TU, which it is (since it's the transpose, and TU is preserved under transposition).

Wait, let me be more careful. The hitting set LP is:
min sum_{e in M} x_e
s.t. for each alternating cycle C: sum_{e in C ∩ M} x_e ≥ 1
     x_e ≥ 0

The packing LP (dual) is:
max sum_{C} y_C
s.t. for each e in M: sum_{C: e in C} y_C ≤ 1
     y_C ≥ 0

If the constraint matrix of the hitting set LP is TU, then both LPs have integral optimal solutions, and min hitting set = max integral packing = max disjoint cycles.

The constraint matrix A has rows indexed by alternating cycles and columns indexed by M-edges, with A_{C,e} = 1 if e ∈ C. We need A to be TU.

Is A TU? The rows are characteristic vectors of alternating cycles (restricted to M-edges). For a bipartite graph, the set of all cycles forms a "binary matroid" (the cycle matroid), and the incidence matrix of circuits of a binary matroid is... not necessarily TU.

Hmm, actually, TU of the cycle-edge incidence matrix is not guaranteed in general. But for planar graphs, there are special results.

Let me think about this differently. The grid graph is planar. The domino tiling is a perfect matching. The alternating cycles are cycles in the grid graph.

For planar graphs, there's a result that the minimum feedback arc set equals the maximum number of disjoint cycles (by the planar dual and the four-color theorem, or more directly by network flows). But I'm not sure this directly applies here.

OK, I think I'm overcomplicating this. Let me just look at it from the competition perspective and state the min-max result as a lemma with a proof sketch.

Actually, for a competition, I think the expected solution might be more elementary. Let me reconsider.

Competition approach:

Lower bound: All-horizontal tiling → 1011² disjoint 2×2 alternating cycles → need ≥ 1011².

Upper bound: For any tiling, we can find 1011² dominoes to fix. 

For the upper bound, maybe we can use a direct construction. Here's an idea:

Partition the board into 2×2 blocks: rows (2i-1, 2i) and columns (2j-1, 2j) for i, j = 1, ..., 1011. There are 1011² blocks.

In each block, the 4 cells are covered by dominoes. There are several cases:
1. Two dominoes entirely within the block (either both horizontal or both vertical). This is a flippable 2×2 square. Fix one domino.
2. One domino within the block and two dominoes crossing the boundary (each covering one cell in the block and one outside). 
3. Four dominoes crossing the boundary (each covering one cell in the block and one outside).
4. Two dominoes crossing the boundary, each covering two cells in the block... no, a domino covers exactly 2 adjacent cells, so it can cover at most 2 cells in a 2×2 block.

Wait, let me reconsider. A 2×2 block has 4 cells. Each domino covers 2 adjacent cells. The dominoes covering the block's cells can be:
- 2 dominoes, each entirely within the block (cases: both horizontal, both vertical, or one horizontal one vertical - but one horizontal one vertical would require them to share a cell, so that's not possible for a 2×2 block with 4 cells). So either both horizontal or both vertical. Both cases are flippable 2×2 squares.
- 1 domino within the block and 2 dominoes crossing the boundary. The internal domino covers 2 cells, and the other 2 cells are each covered by a crossing domino.
- 0 dominoes within the block, and 4 dominoes crossing the boundary (each cell covered by a different crossing domino). But wait, a crossing domino covers 1 cell in the block and 1 outside. So 4 crossing dominoes cover all 4 cells.
- 2 dominoes crossing the boundary, each covering 2 cells in the block. But a domino covers 2 adjacent cells, and in a 2×2 block, adjacent cells are either in the same row or same column. If a domino covers 2 cells in the block, it's entirely within the block (since the 2 cells are adjacent and both in the block). So this is the same as case 1.

Wait, no. A domino could cover 2 cells in the block if those 2 cells are adjacent. In a 2×2 block, all pairs of cells are adjacent (it's a complete graph K4 in terms of adjacency? No, in a grid, (1,1) is adjacent to (1,2) and (2,1), but not to (2,2)). So in a 2×2 block with cells a=(r,c), b=(r,c+1), c=(r+1,c), d=(r+1,c+1), the adjacencies are: a-b, a-c, b-d, c-d. So a domino within the block covers one of {a-b, a-c, b-d, c-d}. If the domino covers a-b (horizontal) or c-d (horizontal), that's a horizontal domino. If it covers a-c (vertical) or b-d (vertical), that's a vertical domino.

So case 1: 2 dominoes within the block. The possibilities are: {a-b, c-d} (both horizontal), {a-c, b-d} (both vertical). Both are flippable 2×2 squares.

Other case: 1 domino within the block + 2 crossing dominoes. E.g., domino a-b within the block, and c is covered by a crossing domino (c to (r+2,c) or (r+1,c-1) or (r+1,c+2)), and d is covered by a crossing domino.

Another case: 0 dominoes within the block, 4 crossing dominoes. Each cell is covered by a domino that extends outside the block.

Another case: 1 domino within the block covering a-c (vertical), and b covered by crossing domino, d covered by crossing domino.

OK so in cases where there are crossing dominoes, we can't simply fix a domino within the block. But maybe we can fix a crossing domino that also helps with the adjacent block.

This is getting complicated. Let me think about whether there's a cleaner argument.

Alternative upper bound: Use the fact that the board can be partitioned into 1011² 2×2 blocks, and in each block, at least one domino must be fixed (if the block is a flippable square) or the block's cells are covered by crossing dominoes (which connect to other blocks).

Hmm, actually, let me think about it this way. If a 2×2 block has all 4 cells covered by crossing dominoes (case 3), then those crossing dominoes extend to neighboring blocks. This means the block is "connected" to its neighbors via dominoes. 

Maybe the key insight is: the blocks where we need to fix a domino (flippable squares) are "independent" in some sense, and the blocks with crossing dominoes don't contribute alternating cycles that need to be hit.

Actually, I think the right approach is:

For any tiling, the maximum number of disjoint alternating cycles is at most 1011² (since each uses ≥ 4 cells). And by the min-max theorem, the forcing number equals this maximum. So the forcing number is at most 1011².

For a competition, I think stating the min-max theorem (with proof) is acceptable. Let me think about how to prove it concisely.

Proof of min-max theorem for domino tilings:

We use the height function. Given a domino tiling T of a simply connected region R, define the height function h on the vertices of the grid as follows: fix h(v_0) = 0 for some boundary vertex v_0. For any edge (u, v) of the grid (traversed from u to v), if the edge is covered by a domino in T, h changes by +3 or -1 (depending on orientation); if not covered, h changes by +1 or -3. The sign depends on the direction of traversal and the checkerboard coloring.

An alternating cycle corresponds to a closed walk where the height function goes up and down, forming a "peak" or "valley" structure. Specifically, an alternating cycle encloses a region where the height function has a local extremum.

The key property: two disjoint alternating cycles enclose disjoint regions. The height function restricted to each enclosed region has a "defect" that can be independently "fixed" by flipping the cycle.

The min-max theorem follows from the fact that the "defect regions" form a laminar family (any two are either disjoint or nested), and for laminar families, the min hitting set equals the max disjoint set.

Wait, is the laminar property true? Two alternating cycles can cross (their enclosed regions can partially overlap without nesting). Hmm.

Actually, for domino tilings of simply connected regions, I believe alternating cycles DO have the laminar property (their enclosed regions are either disjoint or nested). This is because the height function is a well-defined function, and the "contour lines" of the height function don't cross.

Let me think about this. An alternating cycle C encloses a region R_C. The height function on the boundary of R_C (which is C) alternates between two values. Inside R_C, the height function differs from the "expected" height by a constant. Two alternating cycles C_1 and C_2: if R_{C_1} and R_{C_2} partially overlap (neither contained in the other), then... 

Hmm, I think for domino tilings, the alternating cycles can actually cross. Consider a 4×4 board with a tiling that has two alternating cycles that cross. Let me try to construct one.

4×4 board, tiling:
Row 1: (1,1)-(1,2), (1,3)-(2,3), (1,4)-(2,4)
Row 2: (2,1)-(2,2), (2,3)-(1,3), (2,4)-(1,4)
Wait, (1,3)-(2,3) and (2,3)-(1,3) are the same domino. Let me be more careful.

4×4 board:
(1,1)-(1,2), (1,3)-(1,4), (2,1)-(3,1), (2,2)-(3,2), (2,3)-(2,4), (3,3)-(4,3), (3,4)-(4,4), (4,1)-(4,2)

Hmm, let me just try to construct two crossing alternating cycles.

Actually, I think for the purpose of this competition problem, I can state the min-max theorem as a lemma and give a proof sketch using the height function and the laminar property. Even if the laminar property needs more careful justification, the overall approach is correct.

Let me also consider: maybe the answer is not 1011² but something else. Let me reconsider.

Actually, wait. I assumed that each alternating cycle uses at least 4 cells (2 dominoes), and the board has 2022² = 4 × 1011² cells. So max disjoint alternating cycles ≤ 1011². And the all-horizontal tiling achieves exactly 1011² (with 2×2 blocks partitioning the board). So the answer is 1011² = 1022121.

But let me double-check the lower bound more carefully. In the all-horizontal tiling, the 2×2 blocks in rows (1,2), (3,4), ..., (2021,2022) and columns (1,2), (3,4), ..., (2021,2022) are all flippable squares. These 1011² blocks are disjoint and partition the board. Each is an alternating cycle. So we need at least 1011² dominoes to hit them all (one per block, since they're disjoint and each domino is in exactly one block).

And the upper bound: for any tiling, the forcing number is at most 1011² (by the min-max theorem and the cell count bound).

So the answer is n = 1011² = 1022121.

Hmm, but let me reconsider whether the min-max theorem is really needed, or if there's a simpler upper bound.

Simple upper bound attempt: For any tiling, consider the 1011² 2×2 blocks (rows (2i-1,2i), columns (2j-1,2j)). In each block, either:
(a) The block is a flippable 2×2 square (2 dominoes within the block). Fix one of them.
(b) Some dominoes cross the block boundary. 

In case (b), the crossing dominoes connect this block to neighboring blocks. The key observation: if a domino crosses from block (i,j) to block (i,j+1) (horizontally crossing), or from block (i,j) to block (i+1,j) (vertically crossing), then this domino is shared between two blocks.

If we fix one domino per block in case (a), and for case (b) we... hmm, this doesn't immediately give a bound of 1011² because in case (b) we might need to fix a domino that's shared with another block, and we'd be double-counting.

Actually, let me think about it differently. In each 2×2 block, there are 4 cells covered by dominoes. The dominoes covering these cells are either within the block or cross the boundary. 

If all 4 cells are covered by 2 dominoes within the block (case a), fix one.
If some cells are covered by crossing dominoes (case b), we need to handle this differently.

In case (b), how many dominoes are within the block? It could be 0 or 1.
- 1 domino within the block: 2 cells covered internally, 2 cells covered by crossing dominoes. Fix the internal domino.
- 0 dominoes within the block: all 4 cells covered by crossing dominoes. We can't fix a domino "in" this block. But the crossing dominoes are in neighboring blocks.

So in the case of 0 internal dominoes, we don't fix any domino for this block. But does this block contribute to any alternating cycle? 

If all 4 cells of a block are covered by crossing dominoes, then no 2×2 flippable square is entirely within this block. But there could be larger alternating cycles passing through this block.

Hmm, this approach doesn't cleanly work. Let me think more.

Actually, maybe I should think about it in terms of a graph. Create a graph where each 2×2 block is a vertex, and two blocks are connected if a domino crosses between them. In case (a) blocks (flippable squares), we fix one domino. In case (b) blocks with 0 internal dominoes, we don't fix anything, but these blocks are connected to other blocks via crossing dominoes.

The alternating cycles that pass through case (b) blocks must also pass through case (a) blocks (or other case (b) blocks). If we fix dominoes in all case (a) blocks, do we hit all alternating cycles?

Not necessarily. An alternating cycle could pass through only case (b) blocks. For example, if the entire tiling consists of crossing dominoes (no 2×2 block is a flippable square), then there might still be alternating cycles.

Hmm, so this approach doesn't work directly. I think the min-max theorem is needed for a clean proof.

Let me just go with the min-max theorem approach. Let me write up the proof.

Actually, let me reconsider the problem. Maybe I should think about it in terms of a different formulation.

The problem is equivalent to: find the minimum n such that for any perfect matching M of the 2022×2022 grid graph, there exists a subset S ⊆ M with |S| = n such that M is the unique perfect matching of the grid graph that contains S.

This is the "forcing number" of the matching M, and we want the maximum over all matchings M.

The forcing number of a perfect matching M in a bipartite graph G is defined as the minimum size of a subset S ⊆ M such that M is the unique perfect matching containing S. 

Theorem (Pachter-Kim, 1998): For a perfect matching M in a bipartite graph G, the forcing number of M equals the maximum number of M-alternating cycles that are pairwise edge-disjoint (in M).

Wait, I need to be more precise. "Edge-disjoint in M" means no two cycles share an edge of M. Since each alternating cycle uses edges of M, two cycles are "M-disjoint" if they don't share any M-edge.

This theorem is indeed a known result. The proof uses the fact that the set of M-alternating cycles forms a "totally balanced hypergraph" (when viewed as sets of M-edges), which has the Kőnig property (min hitting set = max disjoint set).

For the grid graph (which is bipartite), this theorem applies. So:

Forcing number of M = max number of M-disjoint alternating cycles.

Now:
- Lower bound: The all-horizontal tiling has 1011² M-disjoint alternating cycles (the 2×2 blocks). So its forcing number is ≥ 1011². (And = 1011² by the upper bound below.)
- Upper bound: For any tiling M, each alternating cycle uses ≥ 2 edges of M (i.e., ≥ 2 dominoes). The total number of dominoes is 2022²/2 = 2·1011². So max M-disjoint alternating cycles ≤ 2·1011²/2 = 1011². By the theorem, forcing number ≤ 1011².

Therefore, the answer is n = 1011² = 1022121.

Wait, I want to double-check: each alternating cycle uses at least 2 dominoes. An alternating cycle of length 2k (in the grid graph) uses k dominoes and k non-domino edges. The minimum is k=2, giving a 4-cycle (2×2 square) using 2 dominoes. So yes, each alternating cycle uses ≥ 2 dominoes.

Total dominoes = 2022 × 2022 / 2 = 2022² / 2 = 2 × 1011².

Max M-disjoint alternating cycles ≤ (2 × 1011²) / 2 = 1011². ✓

And the all-horizontal tiling achieves 1011² M-disjoint alternating cycles. ✓

So the answer is n = 1011² = 1022121.

Hmm, let me reconsider whether I need to also verify that the all-horizontal tiling's forcing number is exactly 1011² (not more). By the theorem, forcing number = max M-disjoint cycles = 1011² (since we found 1011² disjoint cycles, and the upper bound is 1011²). So yes, it's exactly 1011².

And for any other tiling, the forcing number is at most 1011² (by the cell-count bound and the theorem). So the maximum forcing number over all tilings is 1011², achieved by the all-horizontal tiling.

Therefore, the minimum n for which Viktor can always win is n = 1011² = 1022121.

Let me also verify: 1011 = 2022/2. So 1011² = (2022/2)² = 2022²/4 = 4088484/4 = 1022121. ✓

Now let me write up the proof cleanly.

Actually, I realize I should also prove (or at least sketch) the Pachter-Kim theorem, since this is a competition problem and the solution should be self-contained.

Proof sketch of the theorem (forcing number = max M-disjoint alternating cycles):

Let M be a perfect matching in a bipartite graph G. 

Lower bound (forcing number ≥ max M-disjoint alternating cycles): If C_1, ..., C_k are M-disjoint alternating cycles, then any forcing set must contain at least one edge from each C_i (since flipping C_i gives another perfect matching that agrees with M outside C_i). Since the C_i are M-disjoint, these edges are all different. So forcing number ≥ k.

Upper bound (forcing number ≤ max M-disjoint alternating cycles): We need to show that there exists a forcing set of size equal to the max M-disjoint alternating cycles. 

Consider the set of all M-alternating cycles. We want a minimum hitting set (of M-edges) for all alternating cycles. By LP duality, min hitting set = max fractional packing. We need to show the LP has integral optimal solutions.

The constraint matrix A has rows = alternating cycles, columns = M-edges, A_{C,e} = 1 if e ∈ C. We need A to be totally unimodular (TU).

For bipartite G, the M-alternating cycles correspond to cycles in a directed graph D: orient M-edges from white to black, and non-M-edges from black to white. Then M-alternating cycles correspond to directed cycles in D. The hitting set problem becomes: find minimum set of M-edges to hit all directed cycles in D.

The cycle-arc incidence matrix of a directed graph is TU (this is a classical result). Since we're restricting to M-edges (a subset of arcs), the submatrix is also TU. Therefore, the LP has integral optimal solutions, and min hitting set = max integral packing = max M-disjoint alternating cycles.

This completes the proof of the theorem.

Actually, I need to be a bit more careful. The cycle-arc incidence matrix of a directed graph is TU - is this true? 

The node-arc incidence matrix of a directed graph is TU (this is classical). The cycle-arc incidence matrix... hmm, I don't think this is TU in general. 

Let me reconsider. The relevant LP is:

min sum_{e ∈ M} x_e
s.t. for each directed cycle C in D: sum_{e ∈ C ∩ M} x_e ≥ 1
     x_e ∈ {0, 1}

The LP relaxation has constraint matrix A where A_{C,e} = 1 if e ∈ C ∩ M. We need this to be TU.

Actually, I think the correct approach is to use the fact that for bipartite graphs, the set of M-alternating cycles forms a "balanced hypergraph" (in the sense of Berge), and balanced hypergraphs have the Kőnig property (min transversal = max matching).

A hypergraph is "balanced" if every odd cycle in the hypergraph has an edge containing three vertices of the cycle. For bipartite graphs, the M-alternating cycles form a balanced hypergraph because... hmm, I need to think about why.

Actually, I think the correct theorem is: for a bipartite graph G with perfect matching M, the hypergraph of M-alternating cycles (as sets of M-edges) is "normal" or has the "Kőnig property." This is proven in the paper by Pachter and Kim.

For the competition, I think I can state this as a lemma and give a proof sketch. The key idea is the total unimodularity or the balanced hypergraph property.

Let me also consider: maybe there's a completely different approach to this problem that doesn't use the min-max theorem.

Alternative approach using graph theory directly:

Consider the 2022 × 2022 grid graph G. It's bipartite with parts B (black cells) and W (white cells), each of size 2022²/2 = 2 × 1011².

A domino tiling is a perfect matching M in G. An alternating cycle is a cycle in G alternating between M-edges and non-M-edges.

We want: min |S| such that S ⊆ M and M is the unique perfect matching of G containing S.

Equivalently: min |S| such that every M-alternating cycle contains an edge of S.

This is the minimum hitting set for all M-alternating cycles (restricted to M-edges).

Now, consider the directed graph D: orient each M-edge from W to B, and each non-M-edge from B to W. M-alternating cycles correspond to directed cycles in D.

We want the minimum number of M-edges (arcs from W to B in D) to remove to make D acyclic. But we can only remove M-edges, not non-M-edges.

Hmm, but if we remove an M-edge, the corresponding vertices become unmatched, and the remaining graph might have new perfect matchings. Wait, no - we're not removing edges from the graph; we're fixing edges. Fixing an M-edge means it must be in any perfect matching. So we're looking for S ⊆ M such that M is the unique perfect matching of G that contains all edges of S.

If S ⊆ M and M is the unique perfect matching containing S, then there's no M-alternating cycle disjoint from S. Because if there were such a cycle C, flipping C would give another perfect matching M' that agrees with M on S (since C is disjoint from S) but differs from M on C. So M' ≠ M and M' contains S, contradiction.

Conversely, if every M-alternating cycle intersects S, then M is the unique perfect matching containing S. Because any other perfect matching M' containing S differs from M on some alternating cycles, and those cycles must avoid S (since M' agrees with M on S), contradicting the assumption.

So: forcing number = min hitting set for M-alternating cycles = min |S| such that every M-alternating cycle contains an edge of S.

Now, the min-max theorem: min hitting set = max number of pairwise M-disjoint alternating cycles.

For the upper bound (min hitting set ≤ max M-disjoint cycles), we need the Kőnig property. Let me try to prove this directly for the grid graph.

Direct proof of upper bound for grid graph:

Consider the grid graph G (bipartite) with perfect matching M. Let k = max number of M-disjoint alternating cycles. We want to show there's a hitting set of size k.

Consider the directed graph D as above. M-alternating cycles = directed cycles in D. We want to hit all directed cycles using only M-edges (arcs from W to B).

Consider the strongly connected components (SCCs) of D. A directed cycle is contained within an SCC. If an SCC has no directed cycle, it's a single vertex. If an SCC has a directed cycle, it contains at least one M-edge.

In each SCC with a directed cycle, we need to remove at least one M-edge to break all cycles. The minimum number of M-edges to remove from an SCC to make it acyclic is the "M-edge feedback arc set" of the SCC.

By the Kőnig property (which we're trying to prove), this equals the max number of M-disjoint directed cycles in the SCC.

Hmm, I'm going in circles (pun intended). Let me just accept the theorem and write up the solution.

For the competition, I'll state the theorem as a lemma with a proof sketch, and then use it.

Let me also think about whether the answer could be different. 

What if the board size matters in a different way? 2022 = 2 × 1011. The answer 1011² = (2022/2)². For a general 2m × 2n board, the answer would be mn. For a 2m × 2n board with the all-horizontal tiling, the number of disjoint 2×2 alternating cycles is m × n (partitioning into 2×2 blocks). And the upper bound is mn (since each alternating cycle uses ≥ 2 dominoes, and there are 2mn dominoes, so max disjoint cycles ≤ mn). So the answer for a 2m × 2n board is mn.

For our problem, m = n = 1011, so the answer is 1011² = 1022121.

Let me write up the proof now.

---

Proof:

Let N = 2022. The board is an N × N grid, which we can think of as the grid graph G with N² vertices (cells) and edges between adjacent cells. G is bipartite: color cells black/white in checkerboard fashion. A domino tiling is a perfect matching M in G, with |M| = N²/2 dominoes.

**Key definitions:**
- An **M-alternating cycle** is a cycle in G whose edges alternate between M-edges (dominoes) and non-M-edges.
- A **forcing set** for M is a subset S ⊆ M such that M is the unique perfect matching of G containing S. Equivalently, S hits every M-alternating cycle (every M-alternating cycle contains at least one edge of S).
- The **forcing number** f(M) is the minimum size of a forcing set for M.

Viktor wants to find a forcing set for Sofia's tiling M. The answer is max_M f(M).

**Lemma (Forcing number = max disjoint alternating cycles):** For any perfect matching M in a bipartite graph G, f(M) equals the maximum number of pairwise M-disjoint M-alternating cycles (i.e., cycles sharing no M-edge).

*Proof of Lemma:*
- *Lower bound:* If C_1, ..., C_k are M-disjoint alternating cycles, any forcing set must contain at least one M-edge from each C_i (since flipping C_i produces another perfect matching agreeing with M outside C_i). These edges are distinct, so f(M) ≥ k.

- *Upper bound:* Orient M-edges from white to black and non-M-edges from black to white, forming a directed graph D. M-alternating cycles correspond to directed cycles in D. The problem becomes: find the minimum number of M-arcs hitting all directed cycles in D. 

  The key claim is that the hypergraph of M-alternating cycles (viewed as sets of M-edges) is **balanced** (in the sense of Berge): every odd cycle in the hypergraph has a hyperedge containing three vertices of the cycle. For bipartite G, this follows because M-alternating cycles in a bipartite graph have a natural "2-coloring" of their M-edges (based on the parity of their position in the cycle), which prevents odd cycles in the hypergraph without a containing hyperedge.

  By the Berge theorem, balanced hypergraphs have the Kőnig property: the minimum transversal (hitting set) equals the maximum matching (set of pairwise disjoint hyperedges). This gives f(M) ≤ k, completing the proof. □

Hmm, I'm not fully confident in the balanced hypergraph argument. Let me try a different proof.

*Alternative proof of upper bound:* We use LP duality. The hitting set LP is:

min Σ_{e∈M} x_e s.t. Σ_{e∈C∩M} x_e ≥ 1 for each alternating cycle C, x_e ≥ 0.

The dual (packing LP) is:

max Σ_C y_C s.t. Σ_{C∋e} y_C ≤ 1 for each e ∈ M, y_C ≥ 0.

By strong LP duality, min hitting set = max fractional packing. We need integral optimal solutions for both.

The constraint matrix A (rows = cycles, columns = M-edges) is the cycle-arc incidence matrix of the directed graph D restricted to M-arcs. 

**Claim:** A is totally unimodular.

*Proof of claim:* The node-arc incidence matrix of any directed graph is TU (classical result of Heller-Tompa). The cycle-arc incidence matrix can be obtained from the node-arc incidence matrix by taking linear combinations of rows (each cycle is a sum of node rows with coefficients ±1). Since TU is preserved under taking submatrices and under row operations with coefficients in {0, ±1}, the cycle-arc incidence matrix is TU. Restricting to M-arcs (taking a subset of columns) preserves TU. □

Since A is TU and the right-hand side is integral, both the primal and dual LPs have integral optimal solutions. Therefore:

min hitting set = max integral packing = max number of M-disjoint alternating cycles. □

Wait, I need to be more careful. The cycle-arc incidence matrix being TU: is this actually true? 

The node-arc incidence matrix of a directed graph is TU. The cycle-arc incidence matrix... each row is the characteristic vector of arcs in a directed cycle. This is NOT in general a row operation on the node-arc incidence matrix. 

Actually, a directed cycle can be represented as a circulation: a vector in the null space of the node-arc incidence matrix with entries in {0, ±1}. The cycle-arc incidence matrix (with 0/1 entries, indicating which arcs are in the cycle) is different from the circulation representation (which has ±1 entries for arc directions).

Hmm, so the cycle-arc incidence matrix might not be TU in general. Let me reconsider.

Actually, for the problem of hitting all directed cycles by removing arcs, the relevant LP is:

min Σ x_a s.t. Σ_{a∈C} x_a ≥ 1 for each directed cycle C, 0 ≤ x_a ≤ 1.

This is the "feedback arc set" LP. The constraint matrix is the cycle-arc incidence matrix. This matrix is NOT TU in general (the feedback arc set problem is NP-hard for general directed graphs). 

However, for planar directed graphs, the feedback arc set problem is polynomial-time solvable, and the LP is integral. This is because the planar dual of the feedback arc set is the maximum acyclic subgraph problem, which for planar graphs has an integral LP.

The grid graph is planar! So D (the directed version of the grid graph) is a planar directed graph. Therefore, the cycle-arc incidence matrix of D is TU (for planar graphs), and the feedback arc set LP has integral optimal solutions.

But wait, we're not solving the general feedback arc set; we're only allowed to remove M-arcs. So the LP is:

min Σ_{e∈M} x_e s.t. Σ_{e∈C∩M} x_e ≥ 1 for each directed cycle C, x_e ≥ 0 for e ∈ M.

This is a restricted version where we only have variables for M-arcs. The constraint matrix is the cycle-arc incidence matrix restricted to M-arcs (columns). A submatrix of a TU matrix is TU, so if the full cycle-arc incidence matrix of D is TU, then the restricted version is also TU.

But is the cycle-arc incidence matrix of a planar directed graph TU? I believe so, because of the planar dual argument. The feedback arc set in a planar graph can be solved by a max-flow/min-cut in the dual, which gives integral solutions.

Actually, let me think about this more carefully. The feedback arc set problem for planar directed graphs: the LP relaxation is integral because the dual problem (maximum set of arcs that can be made acyclic, or equivalently, the maximum number of arc-disjoint directed cycles) has an integral LP. This is because the planar dual transforms the problem into a network flow problem.

For our problem, we need the restricted version (only M-arcs). Since the full matrix is TU (for planar graphs), the restricted matrix is also TU, and the LP is integral.

So the proof works for the grid graph (which is planar). 

Let me now also verify: is the grid graph with the directed orientation (M-edges from W to B, non-M-edges from B to W) a planar directed graph? Yes, the grid graph is planar, and orienting the edges doesn't change planarity.

Great, so the proof is:

1. The grid graph G is planar and bipartite.
2. Orient M-edges from W to B and non-M-edges from B to W, getting a planar directed graph D.
3. M-alternating cycles = directed cycles in D.
4. The cycle-arc incidence matrix of a planar directed graph is TU (by the planar dual / network flow argument).
5. Restricting to M-arcs preserves TU.
6. Therefore, the hitting set LP has integral optimal solutions: min hitting set = max M-disjoint alternating cycles.

This completes the proof of the lemma for the grid graph.

Now, the full proof:

**Lower bound:** Consider the all-horizontal tiling M_0 of the N × N board (N = 2022). Partition the board into 2×2 blocks: rows (2i-1, 2i) and columns (2j-1, 2j) for i, j = 1, ..., N/2 = 1011. There are 1011² = (N/2)² such blocks. Each block contains two horizontal dominoes forming a flippable 2×2 square, which is an M_0-alternating cycle. These 1011² cycles are pairwise M_0-disjoint (they partition the board's cells, and each domino is in exactly one block). By the lemma, f(M_0) ≥ 1011². So Viktor needs at least 1011² dominoes for this tiling.

**Upper bound:** For any tiling M of the N × N board, each M-alternating cycle uses at least 2 dominoes (M-edges). The total number of dominoes is N²/2 = 2 × 1011². So the maximum number of M-disjoint alternating cycles is at most (N²/2)/2 = N²/4 = 1011². By the lemma, f(M) ≤ 1011². So Viktor can always win with at most 1011² dominoes.

**Conclusion:** The minimum n is 1011² = 1022121.

Let me double-check the arithmetic: 1011² = 1011 × 1011. 
1011 × 1000 = 1011000
1011 × 11 = 11121
Total = 1022121. ✓

N²/4 = 2022²/4 = 4088484/4 = 1022121. ✓

So the answer is n = 1011² = 1022121.

Wait, I want to make sure about one thing: the lemma says f(M) = max M-disjoint alternating cycles. For the lower bound, I need f(M_0) ≥ 1011², which follows from the 1011² disjoint cycles. For the upper bound, I need f(M) ≤ 1011² for all M, which follows from max M-disjoint cycles ≤ 1011² (cell count) and the lemma (f(M) = max M-disjoint cycles ≤ 1011²).

But actually, for the upper bound, I need the lemma to give f(M) = max M-disjoint cycles, and then max M-disjoint cycles ≤ 1011². The lemma gives equality, so f(M) = max M-disjoint cycles ≤ 1011². ✓

And for the lower bound, f(M_0) = max M_0-disjoint cycles ≥ 1011² (since we found 1011² disjoint cycles). And by the cell count, max M_0-disjoint cycles ≤ 1011². So f(M_0) = 1011² exactly. ✓

Great, the answer is n = 1011² = 1022121.

One more thing: I should make sure the 2×2 blocks in the all-horizontal tiling are indeed alternating cycles. In the all-horizontal tiling, each row has dominoes (i, 2j-1)-(i, 2j). A 2×2 block in rows (2i-1, 2i) and columns (2j-1, 2j) has:
- Domino (2i-1, 2j-1)-(2i-1, 2j) in the top row.
- Domino (2i, 2j-1)-(2i, 2j) in the bottom row.
These two horizontal dominoes can be flipped to two vertical dominoes: (2i-1, 2j-1)-(2i, 2j-1) and (2i-1, 2j)-(2i, 2j). So yes, it's an alternating cycle (4-cycle). ✓

And these 2×2 blocks are disjoint and partition the board: rows (1,2), (3,4), ..., (2021,2022) and columns (1,2), (3,4), ..., (2021,2022). Each cell is in exactly one block. Each domino is in exactly one block (since dominoes are horizontal within a row, and each row is split into column pairs (1,2), (3,4), ...). ✓

Alright, I'm confident the answer is 1011² = 1022121. Let me write the final proof.

Hmm, actually let me reconsider whether I need the full min-max theorem, or if I can prove the upper bound more directly.

Direct upper bound without min-max theorem:

For any tiling M, we want to find a set S of at most 1011² dominoes that hits all alternating cycles.

Approach: Greedily find disjoint alternating cycles and fix one domino from each. 

Start with the tiling M. While there exists an alternating cycle C:
1. Add one domino from C to S.
2. Remove that domino's cells from the region (i.e., fix it).
3. Continue with the remaining region.

Each iteration removes 2 cells (1 domino) and breaks at least one alternating cycle. The question is: how many iterations?

Each alternating cycle uses ≥ 2 dominoes. Initially, there are N²/2 = 2 × 1011² dominoes. But as we remove dominoes, the remaining region shrinks, and the number of remaining dominoes decreases.

The key observation: the alternating cycles we find are M-disjoint (since once we fix a domino, it's removed from the region, and future cycles can't use it). So the number of iterations is at most the max number of M-disjoint alternating cycles, which is ≤ 1011².

But wait, this greedy approach might not find the maximum number of disjoint cycles. It finds SOME set of disjoint cycles, and the number could be less than the maximum. However, the size of S equals the number of cycles found, which is ≤ max M-disjoint cycles ≤ 1011².

But does this S hit ALL alternating cycles? After the greedy process, there are no more alternating cycles in the remaining region (the while loop terminated). But could there be an alternating cycle in the original tiling that doesn't pass through any of the fixed dominoes?

An alternating cycle in the original tiling that avoids all fixed dominoes would be an alternating cycle in the remaining region. But the while loop terminated because there are no alternating cycles in the remaining region. So no such cycle exists. Therefore, S hits all alternating cycles. ✓

Wait, but this isn't quite right. The "remaining region" changes as we remove dominoes. An alternating cycle in the original tiling that avoids all fixed dominoes is a cycle in the original grid graph that doesn't use any fixed domino's cells. But the remaining region is the original board minus the fixed dominoes' cells. An alternating cycle in the original tiling that avoids fixed dominoes is indeed an alternating cycle in the remaining region's tiling. So if the while loop terminated (no alternating cycles in the remaining region), then S hits all alternating cycles. ✓

And the number of iterations is at most 1011² (since each iteration uses ≥ 2 cells, and there are N² = 4 × 1011² cells, so at most 2 × 1011² iterations... wait, that gives 2 × 1011², not 1011²).

Hmm, each iteration removes 2 cells (1 domino), and each alternating cycle uses ≥ 4 cells (2 dominoes). But the greedy approach removes 1 domino per cycle, and the cycles are M-disjoint. So the number of cycles found is at most |M| / 2 = (N²/2) / 2 = N²/4 = 1011². Wait, no: each cycle uses ≥ 2 dominoes, and the cycles are M-disjoint, so the number of cycles is at most |M| / 2 = N²/4 = 1011². But the greedy approach removes 1 domino per cycle, so |S| = number of cycles ≤ 1011². ✓

Actually wait, the cycles are M-disjoint, meaning they share no M-edge. Each cycle uses ≥ 2 M-edges. So the number of M-disjoint cycles is at most |M| / 2 = (N²/2) / 2 = N²/4 = 1011². And |S| = number of cycles found ≤ 1011². ✓

But I need to verify that the greedy approach finds M-disjoint cycles. When we fix        — AI历史解题过程（thinking）
#   polymath_05037         — 题目ID

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
  <problem_id>polymath_05037</problem_id>
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

Sofia and Viktor are playing a game on a $2022 \times 2022$ board:
- Sofia covers the board completely with dominoes, with no overlaps and all within the board.
- Viktor chooses a positive integer $n$.
- Viktor then selects and fixes $n$ dominoes.
- Sofia removes the remaining dominoes and tries to cover the board with a different arrangement of dominoes.
If Sofia succeeds, she wins; otherwise, Viktor wins. What is the minimum number $n$ for which Viktor can always win, regardless of Sofia's initial domino placement?

## Standard Solution

To solve the problem of finding the minimum number \( n \) such that Viktor can always win by choosing \( n \) dominoes to fix, we need to understand the concept of a forcing set in the context of domino tilings on a grid.

### Step-by-Step Solution:

1. **Understanding the Problem:**
   - The board is a \( 2022 \times 2022 \) grid.
   - Each domino covers two adjacent squares.
   - Viktor's goal is to choose \( n \) dominoes such that Sofia cannot rearrange the remaining dominoes into a different tiling.

2. **Forcing Sets:**
   - A forcing set is a subset of dominoes such that fixing these dominoes uniquely determines the entire tiling.
   - To prevent any rearrangement, Viktor needs to ensure that no two adjacent squares can be part of a different tiling.

3. **2x2 Blocks and Flips:**
   - Consider the smallest unit of a tiling: a \( 2 \times 2 \) block.
   - Each \( 2 \times 2 \) block can be tiled in two ways: either both dominoes are horizontal or both are vertical.
   - To prevent any flip in a \( 2 \times 2 \) block, at least one domino in each block must be fixed.

4. **Partitioning the Grid:**
   - The \( 2022 \times 2022 \) grid can be divided into \( 1011 \times 1011 \) non-overlapping \( 2 \times 2 \) blocks.
   - Each \( 2 \times 2 \) block contains exactly 2 dominoes, and to prevent any flip, at least one domino in each block must be fixed.

5. **Calculating the Minimum Number \( n \):**
   - The total number of \( 2 \times 2 \) blocks is \( 1011 \times 1011 \).
   - Therefore, the minimum number of dominoes that need to be fixed is \( 1011 \times 1011 \).

6. **Final Calculation:**
   - \( 1011 \times 1011 = 1022121 \).

### Conclusion:
The minimum number \( n \) for which Viktor can always win, regardless of Sofia's initial domino placement, is \(\boxed{1022121}\).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a 2022×2022 board. Sofia covers it with dominoes (each domino covers 2 adjacent cells). Then Viktor chooses a positive integer n and fixes n dominoes. Sofia removes the rest and tries to re-cover the board with a different arrangement of dominoes. If she succeeds, she wins; otherwise Viktor wins.

We need the minimum n such that Viktor can always win, regardless of Sofia's initial placement.

So Viktor wants to fix n dominoes such that the remaining uncovered cells (the board minus the 2n cells covered by fixed dominoes) cannot be tiled by dominoes in any way other than... wait, let me re-read.

"Sofia removes the remaining dominoes and tries to cover the board with a different arrangement of dominoes."

So after Viktor fixes n dominoes, Sofia removes all other dominoes. Now the board has 2n cells covered by fixed dominoes, and the rest is uncovered. Sofia tries to cover the ENTIRE board with a different arrangement of dominoes. The fixed dominoes stay in place. So Sofia needs to tile the remaining cells (the board minus the 2n cells covered by fixed dominoes) with dominoes, in a way that's different from the original tiling.

Wait, "cover the board with a different arrangement of dominoes" - does this mean cover the entire board (including where fixed dominoes are) or just the uncovered part? The fixed dominoes are already in place, so Sofia needs to tile the remaining uncovered cells. The "different arrangement" means different from the original arrangement of the non-fixed dominoes.

So Viktor wins if: after fixing n dominoes, the remaining cells can ONLY be tiled in the original way (i.e., the original tiling is the unique tiling of the remaining cells).

Actually, let me reconsider. Sofia tries to cover the board with a different arrangement. If the remaining cells have a unique tiling (which must be the original one since the original one works), then Sofia cannot find a different arrangement, so Viktor wins.

So Viktor wants to fix n dominoes such that the remaining uncovered cells have a UNIQUE domino tiling (which is forced to be the original tiling restricted to those cells).

The question: what is the minimum n such that for ANY initial tiling by Sofia, Viktor can choose n dominoes to fix so that the remaining cells have a unique tiling?

Let me think about this more carefully.

A tiling of a region is "frozen" or "rigid" if it's the unique tiling. We want to find a set of dominoes to remove (fix) such that the remaining region has a unique tiling.

Actually, we fix n dominoes (they stay), and remove the rest. The remaining region (board minus fixed dominoes' cells) needs to have a unique tiling.

Let me think about small cases and the structure.

Key concept: A tiling has a "cycle" if there's an alternating cycle - a cycle of cells where you can flip dominoes along the cycle to get a different tiling. If a tiling has no alternating cycles, it's the unique tiling of that region.

So the question becomes: what's the minimum number of dominoes to fix so that the remaining region's tiling has no alternating cycles?

An alternating cycle in a domino tiling: a cycle of even length where consecutive edges alternate between being covered by a domino and not. Flipping along such a cycle gives a new tiling.

If we fix some dominoes, the remaining region is the board with those cells removed. The tiling of the remaining region is the original tiling restricted to those cells. This tiling is unique iff there are no alternating cycles in the remaining region.

So Viktor wants to choose dominoes to fix such that every alternating cycle in the original tiling is "broken" - i.e., at least one domino on each alternating cycle is fixed.

Wait, but fixing a domino removes its cells from the remaining region, which breaks any alternating cycle passing through those cells.

So the problem reduces to: In any domino tiling of the 2022×2022 board, what is the minimum number of dominoes that Viktor needs to fix so that every alternating cycle is broken (has at least one fixed domino on it)?

Hmm, but this is a hitting set problem on alternating cycles. The minimum n would be the maximum over all tilings of the minimum hitting set size.

Actually wait. Let me reconsider. The remaining region after fixing dominoes might have NEW tilings that don't come from alternating cycles of the original tiling. No - actually, the remaining region is a sub-region, and its tilings could be completely different from the original. The original tiling restricted to the remaining region is one valid tiling. For it to be unique, there should be no other tiling of that region.

Two tilings of the same region differ by a set of alternating cycles (this is a classical result). So the original tiling of the remaining region is unique iff there are no alternating cycles in it.

An alternating cycle in the remaining region's tiling is a cycle in the remaining region. Such a cycle is also an alternating cycle in the original tiling (since the dominoes in the remaining region are the same as in the original tiling, just restricted). So yes, the condition is that every alternating cycle of the original tiling must pass through at least one fixed domino.

So we need: minimum n such that for any tiling, Viktor can find a set of n dominoes that hits all alternating cycles.

Now, what do alternating cycles look like? In a domino tiling, consider the "domino graph" or think of it in terms of the grid.

Let me think about this differently. Consider the dual perspective. Color the board in checkerboard pattern. Each domino covers one black and one white cell. 

An alternating cycle: a cycle of cells c_1, c_2, ..., c_{2k} where dominoes cover (c_1,c_2), (c_3,c_4), ..., (c_{2k-1},c_{2k}) and the alternative tiling covers (c_2,c_3), (c_4,c_5), ..., (c_{2k},c_1). The cells c_1, ..., c_{2k} form a cycle in the grid graph.

So an alternating cycle is a cycle in the grid graph where the original tiling's dominoes are every other edge of the cycle.

Now, the question is about the structure of these cycles and how to hit them.

Let me think about a specific tiling. Consider the "all horizontal" tiling where every domino is horizontal. In row i, dominoes cover cells (i, 2j-1) and (i, 2j) for j=1,...,1011.

What are the alternating cycles? An alternating cycle needs consecutive dominoes to be adjacent. Two horizontal dominoes in the same row are adjacent if they share a vertical edge. Domino j covers columns 2j-1, 2j. Domino j+1 covers columns 2j+1, 2j+2. They share the edge between column 2j and 2j+1. So we can form an alternating cycle using dominoes j and j+1 in the same row: cells (i, 2j-1), (i, 2j), (i, 2j+1), (i, 2j+2) form a 4-cycle (actually a path of 4 cells, which with the right edges forms a 4-cycle... wait, 4 cells in a row don't form a cycle).

Hmm, let me reconsider. A 4-cycle in the grid is a 2×2 square. In the all-horizontal tiling, a 2×2 square in rows i, i+1 and columns 2j-1, 2j has dominoes (i, 2j-1)-(i, 2j) and (i+1, 2j-1)-(i+1, 2j). The alternative tiling would be (i, 2j-1)-(i+1, 2j-1) and (i, 2j)-(i+1, 2j). So yes, every 2×2 square aligned with the dominoes is an alternating cycle.

Also, a 2×2 square in columns 2j, 2j+1: dominoes (i, 2j-1)-(i, 2j) covers column 2j in row i, and (i, 2j+1)-(i, 2j+2) covers column 2j+1 in row i. But the 2×2 square in rows i, i+1, columns 2j, 2j+1: the cells are (i, 2j), (i, 2j+1), (i+1, 2j), (i+1, 2j+1). The original dominoes covering these: (i, 2j) is covered by domino (i, 2j-1)-(i, 2j), (i, 2j+1) is covered by (i, 2j+1)-(i, 2j+2), (i+1, 2j) by (i+1, 2j-1)-(i+1, 2j), (i+1, 2j+1) by (i+1, 2j+1)-(i+1, 2j+2). So the 2×2 square has parts of 4 different dominoes. This is NOT an alternating cycle because the domino edges don't alternate properly along the cycle.

So in the all-horizontal tiling, the alternating 4-cycles are exactly the 2×2 squares in columns (2j-1, 2j) for each j. There are 2021 × 1011 such squares.

But there could be larger alternating cycles too. For example, a cycle going around a larger region.

Actually, let me think about what alternating cycles exist in the all-horizontal tiling more carefully. 

An alternating cycle is a cycle in the grid graph where every other edge is a domino edge. The domino edges are all horizontal: (i, 2j-1)-(i, 2j). 

A cycle in the grid graph alternates between horizontal and vertical edges (not necessarily, but let's think about it). For an alternating cycle, the domino edges (every other edge) must be horizontal domino edges. 

Consider a cycle of length 2k. The edges are e_1, e_2, ..., e_{2k}. Dominoes are on e_1, e_3, ..., e_{2k-1} (say). These must be horizontal domino edges. The other edges e_2, e_4, ..., e_{2k} are the "flip" edges.

For a 4-cycle (2×2 square), the four edges going around: if the square is in columns 2j-1, 2j, the bottom edge (horizontal) is a domino edge, the top edge (horizontal) is a domino edge, and the two vertical edges are flip edges. This works.

For larger cycles, consider a "staircase" pattern. Actually, let me think about whether there are alternating cycles that span multiple rows.

Consider a 6-cycle. Take cells forming an L-shape or something. Actually, in a grid, cycles must enclose some region. 

Let me think about a specific larger alternating cycle. Consider rows 1, 2, 3 and columns 1, 2, 3. The dominoes are: row 1: (1,1)-(1,2), (1,3)-(1,4)...; row 2: (2,1)-(2,2), (2,3)-(2,4)...; row 3: (3,1)-(3,2), (3,3)-(3,4)...

Consider the cycle: (1,1)→(1,2)→(2,2)→(2,3)→(3,3)→(3,2)→(2,2)... no, that repeats.

Hmm, let me think about a 6-cycle. (1,1)→(1,2) [domino] →(2,2) [flip, vertical] →(2,3) [flip, horizontal] →(3,3) [flip, vertical]... no, this doesn't work because we need alternating domino/flip edges.

Let me be more careful. Cycle: v_1 → v_2 → v_3 → v_4 → v_5 → v_6 → v_1. Dominoes on (v_1,v_2), (v_3,v_4), (v_5,v_6). Flip edges: (v_2,v_3), (v_4,v_5), (v_6,v_1).

Domino edges must be horizontal domino edges from the tiling. So (v_1,v_2) is a horizontal domino, (v_3,v_4) is a horizontal domino, (v_5,v_6) is a horizontal domino.

The flip edges connect v_2 to v_3, v_4 to v_5, v_6 to v_1. These can be horizontal or vertical.

Example: v_1=(1,1), v_2=(1,2) [domino (1,1)-(1,2)], v_3=(2,2), v_4=(2,1) [domino (2,1)-(2,2)], v_5=(3,1), v_6=(3,2) [domino (3,1)-(3,2)]. 

Flip edges: (1,2)→(2,2) [vertical], (2,1)→(3,1) [vertical], (3,2)→(1,1) [???]. (3,2) to (1,1) is not an edge in the grid. So this doesn't work.

Let me try: v_1=(1,1), v_2=(1,2), v_3=(2,2), v_4=(2,3), v_5=(1,3), v_6=(1,2)... no, v_6=v_2.

Hmm, it seems like in the all-horizontal tiling, the only alternating cycles might be the 2×2 squares. Let me think about why.

Actually, consider a cycle that goes through multiple rows. The domino edges are all horizontal. The flip edges must connect the end of one domino to the start of the next. 

If a domino is (i, 2j-1)-(i, 2j), the right end is (i, 2j) and the left end is (i, 2j-1). The next domino's left end must be adjacent to (i, 2j) via a flip edge. (i, 2j) is adjacent to (i, 2j+1) [horizontal], (i-1, 2j) [vertical], (i+1, 2j) [vertical].

If the flip edge is horizontal: (i, 2j)→(i, 2j+1), then the next domino starts at (i, 2j+1), so it's (i, 2j+1)-(i, 2j+2). Then the right end is (i, 2j+2), and we continue. This just extends along the row.

If the flip edge is vertical: (i, 2j)→(i+1, 2j), then the next domino starts at (i+1, 2j). But dominoes in row i+1 are (i+1, 2k-1)-(i+1, 2k). So (i+1, 2j) is the right end of domino (i+1, 2j-1)-(i+1, 2j). So the next domino would be (i+1, 2j-1)-(i+1, 2j), meaning v_3 = (i+1, 2j-1), v_4 = (i+1, 2j). Then the flip edge from v_4 = (i+1, 2j) goes to... 

Wait, I need to be more careful about the direction. Let me reconsider.

In the cycle v_1, v_2, ..., v_{2k}, the domino covers (v_1, v_2). The direction matters: v_2 is connected to v_3 by a flip edge. So if the domino is (i, 2j-1)-(i, 2j), we could have v_1 = (i, 2j-1), v_2 = (i, 2j) or v_1 = (i, 2j), v_2 = (i, 2j-1).

Case 1: v_2 = (i, 2j) (right end). Flip edge from (i, 2j) to v_3.
  - Horizontal right: v_3 = (i, 2j+1), then domino (v_3, v_4) = (i, 2j+1)-(i, 2j+2), v_4 = (i, 2j+2).
  - Vertical down: v_3 = (i+1, 2j), then domino (v_3, v_4). (i+1, 2j) is the right end of domino (i+1, 2j-1)-(i+1, 2j). So v_3 = (i+1, 2j), v_4 = (i+1, 2j-1). Then flip from (i+1, 2j-1).
  - Vertical up: v_3 = (i-1, 2j), then domino (v_3, v_4). (i-1, 2j) is the right end of domino (i-1, 2j-1)-(i-1, 2j). So v_4 = (i-1, 2j-1). Then flip from (i-1, 2j-1).

Case 2: v_2 = (i, 2j-1) (left end). Flip edge from (i, 2j-1) to v_3.
  - Horizontal left: v_3 = (i, 2j-2), then domino (i, 2j-2)-(i, 2j-3)? No, domino is (i, 2j-3)-(i, 2j-2) if j > 1. So v_3 = (i, 2j-2), v_4 = (i, 2j-3).
  - Vertical: v_3 = (i±1, 2j-1), which is the left end of domino (i±1, 2j-1)-(i±1, 2j). So v_4 = (i±1, 2j).

So the cycle can move between rows. Let me trace a specific cycle.

Start: v_1 = (1,1), v_2 = (1,2) [domino in row 1]. Flip down: v_3 = (2,2), which is right end of domino (2,1)-(2,2). So v_4 = (2,1). Flip down: v_5 = (3,1), which is left end of domino (3,1)-(3,2). So v_6 = (3,2). Flip up: v_7 = (2,2)... but that's v_3, so we'd be repeating. 

Let me try: v_1 = (1,1), v_2 = (1,2). Flip down: v_3 = (2,2), v_4 = (2,1). Flip left: v_5 = (2,0)... out of bounds. 

Flip up from v_4 = (2,1): v_5 = (1,1) = v_1. That's a 4-cycle: (1,1)-(1,2)-(2,2)-(2,1)-(1,1). This is the 2×2 square.

Let me try a longer cycle. v_1 = (1,1), v_2 = (1,2). Flip right: v_3 = (1,3), v_4 = (1,4). Flip down: v_5 = (2,4), which is right end of domino (2,3)-(2,4). v_6 = (2,3). Flip left: v_7 = (2,2), which is right end of domino (2,1)-(2,2). v_8 = (2,1). Flip up: v_9 = (1,1) = v_1. 

So the cycle is: (1,1)-(1,2)-(1,3)-(1,4)-(2,4)-(2,3)-(2,2)-(2,1)-(1,1). This is an 8-cycle going around a 2×4 rectangle... wait, it's a 2×2 rectangle extended. Actually it's the boundary of a 2×4 region? No, it's the boundary of a 2×2 region in columns 1-4... no.

The cycle visits: (1,1), (1,2), (1,3), (1,4), (2,4), (2,3), (2,2), (2,1). This is the boundary of the 2×4 rectangle (rows 1-2, columns 1-4). But wait, the dominoes on this cycle are: (1,1)-(1,2), (1,3)-(1,4), (2,3)-(2,4), (2,1)-(2,2). And the flip edges are: (1,2)-(1,3), (1,4)-(2,4), (2,4)-(2,3)... wait, (2,4) to (2,3) is a flip edge, but (2,3)-(2,4) is a domino. Let me recheck.

The cycle: v_1=(1,1), v_2=(1,2), v_3=(1,3), v_4=(1,4), v_5=(2,4), v_6=(2,3), v_7=(2,2), v_8=(2,1), back to v_1=(1,1).

Dominoes: (v_1,v_2) = (1,1)-(1,2) ✓, (v_3,v_4) = (1,3)-(1,4) ✓, (v_5,v_6) = (2,4)-(2,3) ✓ (same as domino (2,3)-(2,4)), (v_7,v_8) = (2,2)-(2,1) ✓ (same as domino (2,1)-(2,2)).

Flip edges: (v_2,v_3) = (1,2)-(1,3) ✓ horizontal, (v_4,v_5) = (1,4)-(2,4) ✓ vertical, (v_6,v_7) = (2,3)-(2,2) ✓ horizontal, (v_8,v_1) = (2,1)-(1,1) ✓ vertical.

Yes! This is an alternating 8-cycle. The flip would give dominoes: (1,2)-(1,3), (1,4)-(2,4), (2,3)-(2,2), (2,1)-(1,1). So this is a valid alternating cycle.

So there ARE larger alternating cycles. The 2×4 rectangle boundary is an alternating cycle. More generally, any 2×2k rectangle boundary is an alternating cycle (in the all-horizontal tiling).

Actually, even more generally, we can have cycles that span more rows. Let me think...

From the analysis above, when we go down from a row, we can either go back up (creating a 4-cycle) or continue horizontally and then go back up later. 

Actually, the key insight is: in the all-horizontal tiling, an alternating cycle corresponds to a cycle in a certain graph. Let me think about what graph.

Consider the "contracted" graph where each domino is a vertex. Two dominoes are connected if they share a flip edge (i.e., you can flip between them). An alternating cycle in the tiling corresponds to a cycle in this contracted graph.

Hmm, this is getting complex. Let me think about the problem from a higher level.

The problem is asking for the minimum n such that Viktor can always force a win. This is a competition problem, so the answer is likely a clean expression.

Let me think about what structures force uniqueness. 

Key idea: A domino tiling is unique (frozen) if and only if there are no alternating cycles. 

For Viktor to win, he needs to fix dominoes so that the remaining tiling has no alternating cycles. This means every alternating cycle must contain at least one fixed domino.

The question is: what's the maximum over all tilings T of the minimum number of dominoes needed to hit all alternating cycles of T?

Let me think about the all-horizontal tiling and its alternating cycles.

In the all-horizontal tiling, I showed that 2×2k rectangles (for any k) give alternating cycles. Also, we can have more complex shapes.

Actually, let me think about this differently. Consider the all-horizontal tiling. The alternating cycles are exactly the cycles in the "flip graph" of the tiling. 

Let me think about which 2×2 squares are alternating cycles. A 2×2 square in rows i, i+1 and columns j, j+1 is an alternating cycle iff the dominoes are arranged as two horizontal dominoes (one in each row) that can be flipped to two vertical dominoes. This happens when j is odd (so columns j, j+1 = 2k-1, 2k for some k). When j is even (columns 2k, 2k+1), the 2×2 square has 4 different dominoes touching it, so it's not an alternating cycle.

So the "flippable" 2×2 squares are those in columns (1,2), (3,4), ..., (2021,2022), and all pairs of consecutive rows. There are 1011 × 2021 such squares.

Now, to hit all alternating cycles, we need to hit at least all these 2×2 squares (since they're alternating cycles). But also the larger cycles.

Hmm, but hitting all 2×2 squares doesn't necessarily hit all larger cycles. A larger cycle might not contain any 2×2 square as a sub-cycle... actually, any alternating cycle of length > 4 can be decomposed, but that's not quite right either.

Let me think about this differently. 

Actually, I recall that for domino tilings, the set of all tilings of a region forms a distributive lattice, and two tilings are connected by flips. The "flip graph" has tilings as vertices and flips (2×2 rotations) as edges. But here we're not just looking at 2×2 flips; we're looking at arbitrary alternating cycles.

However, any alternating cycle can be decomposed into a sequence of 2×2 flips? No, that's not right. An alternating cycle flip is a single operation that changes multiple dominoes at once.

But actually, the key theorem is: two tilings of a region differ by a set of disjoint alternating cycles. And the flip graph (using 2×2 flips) is connected - any tiling can be reached from any other by a sequence of 2×2 flips. 

But for our problem, we need the tiling to be the UNIQUE tiling, which means no alternating cycles at all (not just no 2×2 flippable squares).

Hmm wait, but if there's an alternating cycle of length > 4, can it be that no 2×2 sub-square is flippable? Let me check with the 8-cycle example above.

The 8-cycle was the boundary of the 2×4 rectangle (rows 1-2, columns 1-4). The 2×2 squares within this rectangle are: columns (1,2) and columns (3,4) in rows (1,2). Both of these are flippable 2×2 squares (columns 1,2 and 3,4 are both odd-even pairs). So this 8-cycle contains two flippable 2×2 squares.

Is it always the case that an alternating cycle contains a flippable 2×2 square? 

Consider an alternating cycle. It's a cycle in the grid where every other edge is a domino. Consider two consecutive dominoes on the cycle. They're connected by a flip edge. The two dominoes and the flip edge form a path of 4 cells. If these 4 cells form a 2×2 square, then it's a flippable square. But they might form a "straight" path (4 cells in a row or column).

In the all-horizontal tiling, if two consecutive dominoes are in the same row and connected by a horizontal flip edge, the 4 cells are in a row - not a 2×2 square. If they're in adjacent rows connected by a vertical flip edge, the 4 cells form a 2×2 square.

So in the 8-cycle example, the flip edges were: (1,2)-(1,3) [horizontal, same row], (1,4)-(2,4) [vertical, different rows], (2,3)-(2,2) [horizontal, same row], (2,1)-(1,1) [vertical, different rows]. The vertical flip edges create 2×2 squares: (1,4)-(2,4) with dominoes (1,3)-(1,4) and (2,3)-(2,4) gives the 2×2 square in columns 3,4; and (2,1)-(1,1) with dominoes (2,1)-(2,2) and (1,1)-(1,2) gives the 2×2 square in columns 1,2.

So in this case, the alternating cycle does contain flippable 2×2 squares. 

Is it possible to have an alternating cycle with NO flippable 2×2 squares? That would require all flip edges to be "straight" (same row or same column as the dominoes). In the all-horizontal tiling, dominoes are horizontal. A flip edge between two dominoes in the same row is horizontal (straight). A flip edge between dominoes in different rows is vertical (creating a 2×2 square). 

For a cycle, we need to eventually return to the starting point. If all flip edges are horizontal (same row), the cycle stays in one row. But a cycle in one row of a grid is impossible (a row is a path, not a cycle - well, unless it wraps around, but it doesn't). So any alternating cycle must have at least one vertical flip edge, which creates a flippable 2×2 square.

Wait, that's for the all-horizontal tiling. Let me verify: if the cycle stays in one row, the dominoes are all in that row, and the flip edges are all horizontal. The cycle would be: domino, flip right, domino, flip right, ... but to close the cycle, we'd need to come back, which requires going left. But going left from a domino's right end means the flip edge goes left, and the next domino is to the left. So the cycle would alternate going right and left, which means it can't make progress and close. Actually, in a single row, the only cycles are... there are no cycles in a single row (a path graph has no cycles). So yes, any alternating cycle must span at least 2 rows, and thus has at least one vertical flip edge, creating a flippable 2×2 square.

So for the all-horizontal tiling: every alternating cycle contains at least one flippable 2×2 square. Therefore, hitting all flippable 2×2 squares is sufficient to hit all alternating cycles.

Now, the flippable 2×2 squares are in columns (1,2), (3,4), ..., (2021,2022) and rows (1,2), (2,3), ..., (2021,2022). Each such square involves 2 dominoes (one in each row). To hit a 2×2 square, we need to fix at least one of its 2 dominoes.

This is a covering problem. We have a grid of 2×2 squares: 2021 rows of squares × 1011 columns of squares. Each square needs one of its 2 dominoes fixed. Each domino is in exactly one square (in the column sense - each domino (i, 2j-1)-(i, 2j) is part of the square in columns (2j-1, 2j) and rows (i-1, i) or (i, i+1)).

Wait, let me reconsider. Each domino (i, 2j-1)-(i, 2j) is part of two 2×2 squares: the one in rows (i-1, i) and columns (2j-1, 2j), and the one in rows (i, i+1) and columns (2j-1, 2j). (Except for dominoes in the first or last row, which are part of only one square.)

So the structure is: for each column pair (2j-1, 2j), we have a column of 2021 squares (between consecutive rows), and 2022 dominoes (one per row). Each domino is shared between at most 2 consecutive squares. We need to select dominoes to hit all squares.

For a single column pair, this is like a path of 2021 vertices (squares) and 2022 edges (dominoes), where each edge covers its two endpoints. We need a vertex cover... no, we need to select edges to cover all vertices. This is an edge cover problem. The minimum edge cover of a path of 2021 vertices is ceil(2021/2) = 1011.

Wait, actually, the minimum number of edges to cover all vertices in a path of n vertices is ceil(n/2). For n=2021, that's 1011.

But we have 1011 column pairs, and the dominoes in different column pairs are different. So the total minimum is 1011 × 1011 = 1011² = 1,022,121.

Hmm wait, but is this the right calculation? Let me reconsider.

For each column pair j (j = 1, ..., 1011), we have a path of 2021 squares (rows 1-2, 2-3, ..., 2021-2022) and 2022 dominoes (rows 1, 2, ..., 2022). We need to select dominoes in this column pair to cover all 2021 squares. The minimum is ceil(2021/2) = 1011.

Since the column pairs are independent (different dominoes), the total minimum is 1011 × 1011 = 1011².

But wait, is this the minimum for the all-horizontal tiling, or could there be a better strategy? Also, is the all-horizontal tiling the worst case?

Let me reconsider whether the all-horizontal tiling is indeed the worst case, or if there's a tiling that requires more fixed dominoes.

Actually, let me reconsider the problem. The answer might be 1011² = 1022121, but that seems like a strange answer for a competition. Let me reconsider.

Hmm, 2022 = 2 × 1011. So 1011² = (2022/2)² = 2022²/4. The board has 2022² cells and 2022²/2 dominoes. So n = 2022²/4 = (number of dominoes)/2.

Actually wait, let me reconsider. Maybe the answer is simpler.

Let me think about this problem from a different angle. 

Actually, I want to reconsider whether hitting all 2×2 flippable squares is sufficient, and whether the all-horizontal tiling is the worst case.

For a general tiling, the situation is more complex. Let me think about what the worst-case tiling looks like.

Actually, let me reconsider the problem. The key question is: what is the minimum n such that for ANY tiling, Viktor can find n dominoes to fix that make the remaining tiling unique?

Let me think about lower bounds. Sofia wants to maximize the number of dominoes Viktor needs. So Sofia chooses a tiling that's "hard" for Viktor.

For the all-horizontal tiling, we showed Viktor needs at least 1011² dominoes (to hit all flippable 2×2 squares, which hit all alternating cycles). But maybe there's a tiling that requires even more.

Wait, actually I need to also check that 1011² is sufficient for the all-horizontal tiling, i.e., that hitting all flippable 2×2 squares indeed hits all alternating cycles. I argued this above: any alternating cycle must have a vertical flip edge, which creates a flippable 2×2 square. So yes, hitting all flippable 2×2 squares is sufficient.

Now, is the all-horizontal tiling the worst case? Let me think about other tilings.

Consider a "brick" tiling where rows alternate between horizontal and vertical dominoes. Or consider a tiling with a mix.

Actually, let me think about a different approach. The problem might have a cleaner answer.

Let me reconsider. The board is 2022 × 2022. Let me think about what happens with a general tiling.

For a general tiling, the flippable 2×2 squares are those where two parallel dominoes form a 2×2 square. Not all 2×2 squares are flippable in a general tiling.

The key insight might be: in any tiling, the number of flippable 2×2 squares is at least something, and we need to hit all of them (plus possibly larger alternating cycles).

Hmm, but this is getting complicated. Let me think about the problem differently.

Alternative approach: Think about the problem in terms of "forcing" the tiling. 

A set of fixed dominoes "forces" the rest of the tiling if the remaining region has a unique tiling. We want the minimum size of a forcing set, maximized over all tilings.

This is related to the concept of "forcing number" in domino tilings. The forcing number of a tiling is the minimum number of dominoes that need to be fixed to make the tiling unique. We want the maximum forcing number over all tilings of the 2022 × 2022 board.

The forcing number of domino tilings has been studied. Let me recall...

For a tiling of an m × n board, the forcing number is related to the maximum number of disjoint alternating cycles. By a theorem (related to the Kőnig-type theorem), the forcing number equals the maximum number of disjoint alternating cycles.

Wait, is that right? The forcing number (minimum hitting set for all alternating cycles) equals the maximum number of pairwise disjoint alternating cycles, by the Kőnig-Egerváry theorem (since the alternating cycles form a clutter, and if the clutter is "Mengerian" or has the Kőnig property...).

Actually, for domino tilings, there's a result that the minimum forcing number equals the maximum number of disjoint alternating cycles. This is because the "cycle space" of a tiling has a nice structure.

Hmm, I'm not sure about the exact theorem. Let me think about it from scratch.

For the all-horizontal tiling of the 2022 × 2022 board, the flippable 2×2 squares are in columns (1,2), (3,4), ..., (2021,2022) and row-pairs (1,2), (2,3), ..., (2021,2022). That's 1011 × 2021 squares.

The maximum number of disjoint flippable 2×2 squares: in each column pair, the squares are in a path (rows 1-2, 2-3, ..., 2021-2022), so the maximum independent set (disjoint squares) is ceil(2021/2) = 1011 per column pair. Wait, actually, two squares in the same column pair are disjoint if they don't share a row. Squares (i, i+1) and (j, j+1) share a row iff |i-j| = 1. So the maximum number of pairwise disjoint squares in a column pair is the maximum independent set of a path of 2021 vertices, which is ceil(2021/2) = 1011.

Squares in different column pairs are always disjoint (they use different columns). So the maximum number of disjoint flippable 2×2 squares is 1011 × 1011 = 1011².

If the forcing number equals the maximum number of disjoint alternating cycles, then the forcing number for the all-horizontal tiling is 1011². And if this is the maximum over all tilings, then the answer is 1011².

But I need to verify: (1) the forcing number equals the max number of disjoint alternating cycles, and (2) the all-horizontal tiling achieves the maximum.

For (1): This is a min-max theorem. The set of alternating cycles forms a family, and we want the minimum hitting set. By LP duality, the min hitting set equals the max fractional packing. For the integral version, we need the family to have the Kőnig property. For domino tiling alternating cycles, I believe this holds because the structure is bipartite (or more precisely, the "cycle hypergraph" is totally balanced or something).

Actually, let me think about this more carefully. The alternating cycles of a domino tiling correspond to cycles in a certain graph. Specifically, consider the graph G whose vertices are the dominoes, and two dominoes are adjacent if they share a flip edge (i.e., there's a 2×2 square containing both). Then alternating cycles correspond to cycles in G? Not exactly, because alternating cycles can be longer than 4.

Hmm, let me think again. Actually, there's a classical result that for domino tilings of simply connected regions, the minimum forcing number equals the maximum number of disjoint alternating cycles. This is proven using the fact that the set of tilings forms a distributive lattice and the alternating cycles have a nice structure.

Let me just assume this is true and proceed. Then the forcing number of a tiling = max number of disjoint alternating cycles.

For the all-horizontal tiling, the max number of disjoint alternating cycles is at least 1011² (from the disjoint 2×2 squares). And the forcing number is at most 1011² (since hitting all 2×2 squares suffices, and we need 1011² to hit them). So the forcing number is exactly 1011².

Now, is 1011² the maximum over all tilings? Let me think about upper bounds.

For any tiling of the 2022 × 2022 board, what's the maximum number of disjoint alternating cycles?

An alternating cycle uses at least 4 cells (a 2×2 square). The board has 2022² cells. So the maximum number of disjoint alternating cycles is at most 2022²/4 = 1011².

And the all-horizontal tiling achieves this bound (with 1011² disjoint 2×2 squares). So the maximum forcing number is 1011².

Wait, but I need to be more careful. An alternating cycle uses at least 4 cells, but the 2×2 squares in the all-horizontal tiling use exactly 4 cells each, and there are 1011² of them, using 4 × 1011² = 4 × 1022121 = 4088484 cells. The board has 2022² = 4088484 cells. So they use ALL the cells! That means the 1011² disjoint 2×2 squares partition the entire board.

Let me verify: 1011 column pairs × 1011 row-pairs (every other row-pair) = 1011² squares, each 2×2, covering 4 × 1011² = 4 × 1011² cells. And 2022² = 4 × 1011². Yes, they partition the board.

So the maximum number of disjoint alternating cycles is exactly 1011² (since each uses ≥ 4 cells and the board has 4 × 1011² cells, and the all-horizontal tiling achieves this).

Therefore, the answer is n = 1011² = 1022121.

But wait, I need to double-check the min-max theorem. Let me think about whether the forcing number really equals the max number of disjoint alternating cycles.

The forcing number is the minimum number of dominoes to hit all alternating cycles. The max number of disjoint alternating cycles is a lower bound on the forcing number (since each disjoint cycle needs a separate domino to hit it). The question is whether equality holds.

For the all-horizontal tiling, we showed:
- Lower bound: 1011² (from disjoint 2×2 squares)
- Upper bound: 1011² (from hitting all 2×2 squares, which hits all alternating cycles)

So equality holds for this specific tiling. 

For the general case, we need: for any tiling, the forcing number ≤ 1011². Since the forcing number = max disjoint alternating cycles ≤ 1011² (because each alternating cycle uses ≥ 4 cells and the board has 4 × 1011² cells), we get forcing number ≤ 1011² for any tiling.

But wait, this uses the min-max theorem (forcing number = max disjoint alternating cycles). If this theorem doesn't hold, we only have forcing number ≥ max disjoint alternating cycles, and the upper bound doesn't follow.

Let me think about whether we can prove the upper bound directly.

Claim: For any tiling of the 2022 × 2022 board, Viktor can fix at most 1011² dominoes to make the tiling unique.

Proof approach: We need to show that for any tiling, there exists a set of 1011² dominoes that hits all alternating cycles.

Alternative: Show that the forcing number of any tiling is at most 1011².

Hmm, let me think about this differently. 

Actually, I think the key theorem is: for a domino tiling of a simply connected region, the minimum forcing number equals the maximum number of disjoint alternating cycles. This is a theorem by Pachter and Kim (or similar). Let me try to prove it or at least argue it.

The alternating cycles of a tiling form a set of cycles in the grid graph. The dominoes are the "edges" we want to hit. Each alternating cycle is a set of dominoes (every other edge of the cycle). We want the minimum hitting set for all alternating cycles.

This is a hitting set problem on a family of sets (each alternating cycle is a set of dominoes). The max disjoint cycles is the max packing. By LP duality, min hitting set = max fractional packing ≥ max integral packing = max disjoint cycles. For equality (min hitting set = max disjoint cycles), we need the family to be "ideal" or have the Kőnig property.

For domino tilings, I believe the alternating cycle family does have the Kőnig property. This might follow from the fact that the tiling's "height function" gives a nice structure to the cycles.

Let me try a different approach. Instead of relying on the min-max theorem, let me directly argue the upper bound.

Upper bound argument: For any tiling of the 2022 × 2022 board, we can find a set of at most 1011² dominoes that hits all alternating cycles.

Consider any tiling. Color the board in checkerboard pattern (black/white). Each domino covers one black and one white cell.

Now, consider the "domino graph" where we create a graph with the dominoes as vertices. Actually, let me think about the structure of alternating cycles differently.

An alternating cycle is a cycle in the grid graph that alternates between domino edges and non-domino edges. Consider the graph H whose edges are the non-domino edges of the grid (the "complement" edges). An alternating cycle alternates between domino edges and H-edges.

Hmm, this is getting complicated. Let me try yet another approach.

Let me think about the problem in terms of the "height function" of the tiling. Each domino tiling of a simply connected region has an associated height function on the vertices of the grid. The height function changes by ±1 or ±3 along edges, with specific rules. Alternating cycles correspond to "contours" of the height function where the height goes up and down.

Actually, I think the cleanest approach is:

1. Lower bound: The all-horizontal tiling requires at least 1011² fixed dominoes (from 1011² disjoint 2×2 alternating cycles).

2. Upper bound: For any tiling, at most 1011² dominoes suffice.

For the upper bound, I'll use the fact that the forcing number equals the maximum number of disjoint alternating cycles (which I'll state as a known theorem), and the latter is at most 1011² since each alternating cycle uses at least 4 cells.

Actually, let me try to prove the upper bound more directly.

Direct upper bound: Consider any tiling T of the 2022 × 2022 board. We want to find a set S of at most 1011² dominoes such that every alternating cycle of T contains a domino from S.

Consider the checkerboard coloring. Each domino covers one black and one white cell. There are 2022²/2 = 2 × 1011² black cells and the same number of white cells.

Now, consider the bipartite graph B where one part is the black cells and the other is the white cells, with edges being the dominoes. This is a perfect matching. An alternating cycle in the tiling corresponds to an alternating cycle in this matching (with respect to the grid graph).

The grid graph is also bipartite (black/white), and the domino tiling is a perfect matching in it. An alternating cycle is a cycle that alternates between matching edges (dominoes) and non-matching edges (grid edges not used by dominoes).

The minimum number of matching edges to hit all alternating cycles is related to the structure of the matching.

Hmm, I think I need to use a specific theorem. Let me recall: for a perfect matching in a bipartite graph, the minimum number of matching edges to remove to make the matching unique equals the maximum number of disjoint alternating cycles. This is a consequence of the Kőnig-Egerváry theorem applied to the "alternating cycle hypergraph."

Actually, I think this follows from the following: the set of alternating cycles of a perfect matching in a bipartite graph forms a "totally balanced hypergraph" or something similar, which has the Kőnig property.

Alternatively, there's a result that says: for a perfect matching M in a bipartite graph G, the minimum forcing number of M equals the maximum number of M-alternating cycles that are pairwise vertex-disjoint (in terms of the matched vertices, or equivalently, edge-disjoint in M).

Let me just assume this theorem and proceed. Then:

- For any tiling, forcing number = max disjoint alternating cycles ≤ ⌊2022²/4⌋ = 1011² (since each alternating cycle uses ≥ 4 cells, i.e., ≥ 2 dominoes, and there are 2022²/2 dominoes, so max disjoint cycles ≤ 2022²/4 = 1011²).

Wait, each alternating cycle uses at least 2 dominoes (4 cells), and the total number of dominoes is 2022²/2 = 2 × 1011². So max disjoint alternating cycles ≤ 2 × 1011² / 2 = 1011². Yes.

- The all-horizontal tiling achieves 1011² disjoint alternating cycles (the 2×2 squares partitioning the board).

So the answer is n = 1011² = 1022121.

Hmm wait, but I should double-check: 1011² = 1011 × 1011. Let me compute: 1011² = (1000 + 11)² = 1000000 + 22000 + 121 = 1022121.

And 2022²/4 = 4088484/4 = 1022121. Yes.

So n = 1011² = 2022²/4.

But let me reconsider whether the min-max theorem is actually needed, or if I can prove both bounds directly.

Lower bound (direct): The all-horizontal tiling has 1011² disjoint 2×2 alternating cycles (partition the board into 2×2 blocks in columns (1,2),(3,4),... and rows (1,2),(3,4),...). Each fixed domino can hit at most one of these (since they're disjoint), so Viktor needs at least 1011² dominoes.

Wait, I need to be more careful. The 2×2 blocks that partition the board are in rows (1,2), (3,4), (5,6), ..., (2021,2022) and columns (1,2), (3,4), ..., (2021,2022). That's 1011 row-pairs × 1011 column-pairs = 1011² blocks. Each block is a 2×2 square with two horizontal dominoes, which is an alternating cycle. These blocks are disjoint (they partition the board). Each domino belongs to exactly one block. So to hit all 1011² alternating cycles, Viktor needs at least 1011² dominoes (one per block).

Upper bound (direct): For any tiling, we need to show Viktor can win with 1011² dominoes. 

Hmm, the direct upper bound is harder without the min-max theorem. Let me think...

Actually, maybe I can prove the upper bound using a different argument. 

Consider any tiling T. We want to find a set S of at most 1011² dominoes that hits all alternating cycles.

Idea: Use a "chessboard" pattern of 2×2 blocks. Partition the board into 2×2 blocks (rows (1,2),(3,4),... and columns (1,2),(3,4),...). There are 1011² such blocks. In each block, there are at most 2 dominoes entirely within the block (if the block is covered by 2 dominoes), or dominoes crossing block boundaries.

Hmm, this doesn't directly work because dominoes can cross block boundaries.

Let me think differently. 

Alternative upper bound approach: Use the min-max theorem. The theorem states that for a perfect matching in a bipartite planar graph (or more specifically, for domino tilings of simply connected regions), the minimum forcing number equals the maximum number of disjoint alternating cycles.

This is actually a known result. Let me recall the reference: it's related to the work of Pachter and Kim (1998), or the work on "forcing numbers" in domino tilings. The key insight is that the alternating cycles of a domino tiling form a "laminar" or "non-crossing" family when viewed appropriately, which gives the Kőnig property.

Actually, I recall now: for domino tilings of simply connected regions, the minimum forcing number equals the maximum number of disjoint alternating cycles. This was proven using the theory of distributive lattices and the structure of the height function. The alternating cycles correspond to "cycles" in the height function, and the min-max theorem follows from the fact that these cycles can be "nested" but not "crossing," giving a totally balanced hypergraph.

Let me just state this as a lemma and prove the result.

Actually, let me try to prove the min-max theorem for this specific case.

Lemma: For any domino tiling of a simply connected region, the minimum forcing number equals the maximum number of disjoint alternating cycles.

Proof sketch: 
- Lower bound is clear: each disjoint alternating cycle needs a separate domino to hit it.
- Upper bound: We use the height function. The height function h is defined on the vertices of the grid. An alternating cycle corresponds to a closed contour where h changes by +3, -1, +3, -1, ... (or the reverse). The key property is that alternating cycles can be "nested" (one inside another) but if they're disjoint, they don't interact. 

Actually, I think the correct approach is to use the fact that the set of alternating cycles forms a "laminar family" when we consider the regions they enclose. Two alternating cycles either are disjoint (their enclosed regions don't overlap), or one's region is contained in the other's. Wait, that's not quite right either, since alternating cycles can partially overlap.

Hmm, let me think about this more carefully. Actually, for domino tilings, two alternating cycles can cross (share vertices but not edges). So the laminar property doesn't directly hold.

Let me try a different approach to the upper bound.

Direct upper bound using a greedy argument:

Consider any tiling T. We'll build a forcing set S greedily.

While there exists an alternating cycle C in the current tiling (of the remaining region):
  - Add one domino from C to S (removing it from the region).
  - This breaks C and possibly other cycles.

The question is: how many dominoes do we need to add?

Each time we add a domino, we remove 2 cells from the region. The remaining region might have new tilings, but we're working with the original tiling restricted to the remaining region.

The number of alternating cycles we need to break is at most the initial number of disjoint alternating cycles, which is at most 1011². But a single domino might break multiple cycles, so the greedy approach might use fewer.

Actually, the greedy approach gives at most (max disjoint alternating cycles) dominoes, because each domino we add breaks at least one "independent" cycle. This is essentially the proof of the min-max theorem for "balanced" hypergraphs.

Hmm, I think I'm overcomplicating this. Let me just state the min-max theorem as a known result and use it.

Actually, for competition math, I think the expected approach is:

1. Show the lower bound: the all-horizontal tiling requires ≥ 1011².
2. Show the upper bound: any tiling can be forced with ≤ 1011².
3. Conclude n = 1011².

For the upper bound, the key is: the maximum number of disjoint alternating cycles in any tiling is at most 1011² (since each uses ≥ 4 cells and the board has 4 × 1011² cells). And by the min-max theorem (forcing number = max disjoint alternating cycles), the forcing number is at most 1011².

But if this is a competition, maybe they expect a more elementary proof. Let me think about whether there's a simpler upper bound argument.

Simpler upper bound: For any tiling, consider the 1011² disjoint 2×2 blocks (rows (2i-1, 2i), columns (2j-1, 2j) for i, j = 1, ..., 1011). In each block, the 4 cells are covered by some dominoes. 

Case 1: The block is covered by 2 dominoes entirely within the block. Then those 2 dominoes form an alternating cycle (a 2×2 flippable square). Fix one of them.

Case 2: Some dominoes cross the block boundary. Then the block's cells are covered by dominoes that extend outside the block.

In Case 2, we can't simply fix a domino in the block. But maybe we can argue that the crossing dominoes already "connect" blocks in a way that reduces the total number of alternating cycles.

This is getting complicated. Let me try yet another approach.

Actually, I think the cleanest approach for a competition is:

Lower bound: All-horizontal tiling, partition into 2×2 blocks, 1011² disjoint alternating cycles, need ≥ 1011².

Upper bound: For any tiling, the maximum number of disjoint alternating cycles is ≤ 1011² (trivial: each uses ≥ 4 cells). By the min-max theorem for domino tilings (forcing number = max disjoint alternating cycles), the forcing number is ≤ 1011².

The min-max theorem can be stated and briefly justified.

Let me now also verify: is the min-max theorem actually true? Let me think of a potential counterexample.

Consider a 2×4 board with the tiling: (1,1)-(1,2), (1,3)-(2,3), (2,1)-(2,2), (1,4)-(2,4). Hmm, let me think of a specific example.

2×4 board, tiling: horizontal dominoes (1,1)-(1,2), (1,3)-(1,4), (2,1)-(2,2), (2,3)-(2,4). This is the all-horizontal tiling. Alternating cycles: the 2×2 square in columns 1-2 (rows 1-2), and the 2×2 square in columns 3-4 (rows 1-2). These are disjoint. Forcing number = 2 (fix one domino in each square). Max disjoint cycles = 2. ✓

Another tiling of 2×4: (1,1)-(1,2), (2,1)-(2,2), (1,3)-(2,3), (1,4)-(2,4). Alternating cycles: the 2×2 square in columns 1-2 (flippable: two horizontal dominoes). The 2×2 square in columns 2-3: cells (1,2),(1,3),(2,2),(2,3). Dominoes: (1,2) is covered by (1,1)-(1,2), (1,3) by (1,3)-(2,3), (2,2) by (2,1)-(2,2), (2,3) by (1,3)-(2,3). Wait, (1,3) and (2,3) are both covered by the same domino. So the 2×2 square in columns 2-3 has 3 dominoes touching it, not an alternating cycle.

The 2×2 square in columns 3-4: cells (1,3),(1,4),(2,3),(2,4). Dominoes: (1,3)-(2,3) and (1,4)-(2,4). These are two vertical dominoes. Flipping gives (1,3)-(1,4) and (2,3)-(2,4). So this IS an alternating cycle.

So the alternating cycles are: 2×2 in columns 1-2 (horizontal), 2×2 in columns 3-4 (vertical). These are disjoint. Forcing number = 2. Max disjoint = 2. ✓

Now, is there a longer alternating cycle? The 2×4 rectangle boundary: cells (1,1),(1,2),(1,3),(1,4),(2,4),(2,3),(2,2),(2,1). Dominoes on this cycle: (1,1)-(1,2), then flip (1,2)-(1,3), then... (1,3) is covered by (1,3)-(2,3), so the domino edge is (1,3)-(2,3) which is vertical. But in the cycle, after (1,2) we go to (1,3) (horizontal flip), then the next domino edge should be (1,3)-(1,4) but (1,3) is covered by the vertical domino (1,3)-(2,3), not by (1,3)-(1,4). So the 2×4 boundary is NOT an alternating cycle in this tiling.

OK so in this tiling, the only alternating cycles are the two 2×2 squares. Forcing number = 2 = max disjoint. ✓

Let me try to think of a case where the min-max might fail... Consider a 4×4 board with a tiling that has a "crossing" pair of alternating cycles.

Actually, I think the min-max theorem does hold for domino tilings of simply connected regions. This is because the alternating cycles correspond to cycles in a planar graph, and the hitting set problem on cycles in a planar graph has the Kőnig property (by a result related to the Lucchesi-Younger theorem or similar).

More specifically, the alternating cycles of a domino tiling correspond to cycles in the "residual graph" (the graph of non-matching edges, combined with matching edges). The minimum number of matching edges to hit all alternating cycles equals the maximum number of edge-disjoint alternating cycles, by the Kőnig-Egerváry theorem for bipartite graphs (since the grid graph is bipartite).

Wait, actually, let me think about this more carefully. The alternating cycles are cycles in the graph G (the grid graph) that alternate between matching edges (dominoes) and non-matching edges. We want to hit all such cycles by removing matching edges.

Consider the directed graph D obtained by directing matching edges from white to black and non-matching edges from black to white (or some consistent orientation). Then alternating cycles correspond to directed cycles in D. We want to hit all directed cycles by removing matching edges.

By the Lucchesi-Younger theorem (or its bipartite special case), the minimum number of edges to remove to make a directed graph acyclic equals the maximum number of edge-disjoint directed cycles. But we're only allowed to remove matching edges, not all edges.

Hmm, this is a constrained version. Let me think...

Actually, in the bipartite case, there's a cleaner result. The grid graph is bipartite (black/white cells). The perfect matching M (domino tiling) matches black to white. An alternating cycle is a cycle alternating between M-edges and non-M-edges.

The minimum number of M-edges to hit all alternating cycles: this is the minimum "forcing number." 

The maximum number of M-edge-disjoint alternating cycles: each such cycle uses 2 or more M-edges, and they share no M-edges.

I claim: min forcing number = max M-edge-disjoint alternating cycles.

This follows from the fact that the "alternating cycle space" has a totally unimodular constraint matrix, which gives integral LP duality. The total unimodularity comes from the bipartite structure of the grid graph.

More concretely: consider the bipartite graph G = (B, W, E) where B and W are black and white cells. M is a perfect matching. The non-matching edges are E \ M. An alternating cycle uses edges alternately from M and E \ M.

Define a flow network: for each non-matching edge (w, b) (from white to black), and each matching edge (b, w) (from black to white), create a directed graph. Alternating cycles become directed cycles. The min hitting set (removing M-edges to break all directed cycles) is a "feedback arc set" restricted to M-edges.

For bipartite graphs, the constraint matrix of the cycle-hitting LP is totally unimodular (this is because the cycle-edge incidence matrix of a directed graph is totally unimodular, and restricting to M-edges preserves this). Therefore, the LP has integral optimal solutions, and min hitting set = max fractional packing ≥ max integral packing = max disjoint cycles. And since min hitting set ≤ max disjoint cycles is NOT generally true... wait, we have min hitting set ≥ max disjoint cycles always (each disjoint cycle needs a separate edge). And by LP duality with TU, min hitting set = max fractional packing. But max fractional packing ≥ max integral packing = max disjoint cycles. So min hitting set ≥ max disjoint cycles, but we need equality.

Hmm, so TU gives us min hitting set = max fractional packing, but we need max fractional packing = max integral packing, which requires the packing LP to also have integral optimal solutions. This would require the dual constraint matrix to also be TU, which it is (since it's the transpose, and TU is preserved under transposition).

Wait, let me be more careful. The hitting set LP is:
min sum_{e in M} x_e
s.t. for each alternating cycle C: sum_{e in C ∩ M} x_e ≥ 1
     x_e ≥ 0

The packing LP (dual) is:
max sum_{C} y_C
s.t. for each e in M: sum_{C: e in C} y_C ≤ 1
     y_C ≥ 0

If the constraint matrix of the hitting set LP is TU, then both LPs have integral optimal solutions, and min hitting set = max integral packing = max disjoint cycles.

The constraint matrix A has rows indexed by alternating cycles and columns indexed by M-edges, with A_{C,e} = 1 if e ∈ C. We need A to be TU.

Is A TU? The rows are characteristic vectors of alternating cycles (restricted to M-edges). For a bipartite graph, the set of all cycles forms a "binary matroid" (the cycle matroid), and the incidence matrix of circuits of a binary matroid is... not necessarily TU.

Hmm, actually, TU of the cycle-edge incidence matrix is not guaranteed in general. But for planar graphs, there are special results.

Let me think about this differently. The grid graph is planar. The domino tiling is a perfect matching. The alternating cycles are cycles in the grid graph.

For planar graphs, there's a result that the minimum feedback arc set equals the maximum number of disjoint cycles (by the planar dual and the four-color theorem, or more directly by network flows). But I'm not sure this directly applies here.

OK, I think I'm overcomplicating this. Let me just look at it from the competition perspective and state the min-max result as a lemma with a proof sketch.

Actually, for a competition, I think the expected solution might be more elementary. Let me reconsider.

Competition approach:

Lower bound: All-horizontal tiling → 1011² disjoint 2×2 alternating cycles → need ≥ 1011².

Upper bound: For any tiling, we can find 1011² dominoes to fix. 

For the upper bound, maybe we can use a direct construction. Here's an idea:

Partition the board into 2×2 blocks: rows (2i-1, 2i) and columns (2j-1, 2j) for i, j = 1, ..., 1011. There are 1011² blocks.

In each block, the 4 cells are covered by dominoes. There are several cases:
1. Two dominoes entirely within the block (either both horizontal or both vertical). This is a flippable 2×2 square. Fix one domino.
2. One domino within the block and two dominoes crossing the boundary (each covering one cell in the block and one outside). 
3. Four dominoes crossing the boundary (each covering one cell in the block and one outside).
4. Two dominoes crossing the boundary, each covering two cells in the block... no, a domino covers exactly 2 adjacent cells, so it can cover at most 2 cells in a 2×2 block.

Wait, let me reconsider. A 2×2 block has 4 cells. Each domino covers 2 adjacent cells. The dominoes covering the block's cells can be:
- 2 dominoes, each entirely within the block (cases: both horizontal, both vertical, or one horizontal one vertical - but one horizontal one vertical would require them to share a cell, so that's not possible for a 2×2 block with 4 cells). So either both horizontal or both vertical. Both cases are flippable 2×2 squares.
- 1 domino within the block and 2 dominoes crossing the boundary. The internal domino covers 2 cells, and the other 2 cells are each covered by a crossing domino.
- 0 dominoes within the block, and 4 dominoes crossing the boundary (each cell covered by a different crossing domino). But wait, a crossing domino covers 1 cell in the block and 1 outside. So 4 crossing dominoes cover all 4 cells.
- 2 dominoes crossing the boundary, each covering 2 cells in the block. But a domino covers 2 adjacent cells, and in a 2×2 block, adjacent cells are either in the same row or same column. If a domino covers 2 cells in the block, it's entirely within the block (since the 2 cells are adjacent and both in the block). So this is the same as case 1.

Wait, no. A domino could cover 2 cells in the block if those 2 cells are adjacent. In a 2×2 block, all pairs of cells are adjacent (it's a complete graph K4 in terms of adjacency? No, in a grid, (1,1) is adjacent to (1,2) and (2,1), but not to (2,2)). So in a 2×2 block with cells a=(r,c), b=(r,c+1), c=(r+1,c), d=(r+1,c+1), the adjacencies are: a-b, a-c, b-d, c-d. So a domino within the block covers one of {a-b, a-c, b-d, c-d}. If the domino covers a-b (horizontal) or c-d (horizontal), that's a horizontal domino. If it covers a-c (vertical) or b-d (vertical), that's a vertical domino.

So case 1: 2 dominoes within the block. The possibilities are: {a-b, c-d} (both horizontal), {a-c, b-d} (both vertical). Both are flippable 2×2 squares.

Other case: 1 domino within the block + 2 crossing dominoes. E.g., domino a-b within the block, and c is covered by a crossing domino (c to (r+2,c) or (r+1,c-1) or (r+1,c+2)), and d is covered by a crossing domino.

Another case: 0 dominoes within the block, 4 crossing dominoes. Each cell is covered by a domino that extends outside the block.

Another case: 1 domino within the block covering a-c (vertical), and b covered by crossing domino, d covered by crossing domino.

OK so in cases where there are crossing dominoes, we can't simply fix a domino within the block. But maybe we can fix a crossing domino that also helps with the adjacent block.

This is getting complicated. Let me think about whether there's a cleaner argument.

Alternative upper bound: Use the fact that the board can be partitioned into 1011² 2×2 blocks, and in each block, at least one domino must be fixed (if the block is a flippable square) or the block's cells are covered by crossing dominoes (which connect to other blocks).

Hmm, actually, let me think about it this way. If a 2×2 block has all 4 cells covered by crossing dominoes (case 3), then those crossing dominoes extend to neighboring blocks. This means the block is "connected" to its neighbors via dominoes. 

Maybe the key insight is: the blocks where we need to fix a domino (flippable squares) are "independent" in some sense, and the blocks with crossing dominoes don't contribute alternating cycles that need to be hit.

Actually, I think the right approach is:

For any tiling, the maximum number of disjoint alternating cycles is at most 1011² (since each uses ≥ 4 cells). And by the min-max theorem, the forcing number equals this maximum. So the forcing number is at most 1011².

For a competition, I think stating the min-max theorem (with proof) is acceptable. Let me think about how to prove it concisely.

Proof of min-max theorem for domino tilings:

We use the height function. Given a domino tiling T of a simply connected region R, define the height function h on the vertices of the grid as follows: fix h(v_0) = 0 for some boundary vertex v_0. For any edge (u, v) of the grid (traversed from u to v), if the edge is covered by a domino in T, h changes by +3 or -1 (depending on orientation); if not covered, h changes by +1 or -3. The sign depends on the direction of traversal and the checkerboard coloring.

An alternating cycle corresponds to a closed walk where the height function goes up and down, forming a "peak" or "valley" structure. Specifically, an alternating cycle encloses a region where the height function has a local extremum.

The key property: two disjoint alternating cycles enclose disjoint regions. The height function restricted to each enclosed region has a "defect" that can be independently "fixed" by flipping the cycle.

The min-max theorem follows from the fact that the "defect regions" form a laminar family (any two are either disjoint or nested), and for laminar families, the min hitting set equals the max disjoint set.

Wait, is the laminar property true? Two alternating cycles can cross (their enclosed regions can partially overlap without nesting). Hmm.

Actually, for domino tilings of simply connected regions, I believe alternating cycles DO have the laminar property (their enclosed regions are either disjoint or nested). This is because the height function is a well-defined function, and the "contour lines" of the height function don't cross.

Let me think about this. An alternating cycle C encloses a region R_C. The height function on the boundary of R_C (which is C) alternates between two values. Inside R_C, the height function differs from the "expected" height by a constant. Two alternating cycles C_1 and C_2: if R_{C_1} and R_{C_2} partially overlap (neither contained in the other), then... 

Hmm, I think for domino tilings, the alternating cycles can actually cross. Consider a 4×4 board with a tiling that has two alternating cycles that cross. Let me try to construct one.

4×4 board, tiling:
Row 1: (1,1)-(1,2), (1,3)-(2,3), (1,4)-(2,4)
Row 2: (2,1)-(2,2), (2,3)-(1,3), (2,4)-(1,4)
Wait, (1,3)-(2,3) and (2,3)-(1,3) are the same domino. Let me be more careful.

4×4 board:
(1,1)-(1,2), (1,3)-(1,4), (2,1)-(3,1), (2,2)-(3,2), (2,3)-(2,4), (3,3)-(4,3), (3,4)-(4,4), (4,1)-(4,2)

Hmm, let me just try to construct two crossing alternating cycles.

Actually, I think for the purpose of this competition problem, I can state the min-max theorem as a lemma and give a proof sketch using the height function and the laminar property. Even if the laminar property needs more careful justification, the overall approach is correct.

Let me also consider: maybe the answer is not 1011² but something else. Let me reconsider.

Actually, wait. I assumed that each alternating cycle uses at least 4 cells (2 dominoes), and the board has 2022² = 4 × 1011² cells. So max disjoint alternating cycles ≤ 1011². And the all-horizontal tiling achieves exactly 1011² (with 2×2 blocks partitioning the board). So the answer is 1011² = 1022121.

But let me double-check the lower bound more carefully. In the all-horizontal tiling, the 2×2 blocks in rows (1,2), (3,4), ..., (2021,2022) and columns (1,2), (3,4), ..., (2021,2022) are all flippable squares. These 1011² blocks are disjoint and partition the board. Each is an alternating cycle. So we need at least 1011² dominoes to hit them all (one per block, since they're disjoint and each domino is in exactly one block).

And the upper bound: for any tiling, the forcing number is at most 1011² (by the min-max theorem and the cell count bound).

So the answer is n = 1011² = 1022121.

Hmm, but let me reconsider whether the min-max theorem is really needed, or if there's a simpler upper bound.

Simple upper bound attempt: For any tiling, consider the 1011² 2×2 blocks (rows (2i-1,2i), columns (2j-1,2j)). In each block, either:
(a) The block is a flippable 2×2 square (2 dominoes within the block). Fix one of them.
(b) Some dominoes cross the block boundary. 

In case (b), the crossing dominoes connect this block to neighboring blocks. The key observation: if a domino crosses from block (i,j) to block (i,j+1) (horizontally crossing), or from block (i,j) to block (i+1,j) (vertically crossing), then this domino is shared between two blocks.

If we fix one domino per block in case (a), and for case (b) we... hmm, this doesn't immediately give a bound of 1011² because in case (b) we might need to fix a domino that's shared with another block, and we'd be double-counting.

Actually, let me think about it differently. In each 2×2 block, there are 4 cells covered by dominoes. The dominoes covering these cells are either within the block or cross the boundary. 

If all 4 cells are covered by 2 dominoes within the block (case a), fix one.
If some cells are covered by crossing dominoes (case b), we need to handle this differently.

In case (b), how many dominoes are within the block? It could be 0 or 1.
- 1 domino within the block: 2 cells covered internally, 2 cells covered by crossing dominoes. Fix the internal domino.
- 0 dominoes within the block: all 4 cells covered by crossing dominoes. We can't fix a domino "in" this block. But the crossing dominoes are in neighboring blocks.

So in the case of 0 internal dominoes, we don't fix any domino for this block. But does this block contribute to any alternating cycle? 

If all 4 cells of a block are covered by crossing dominoes, then no 2×2 flippable square is entirely within this block. But there could be larger alternating cycles passing through this block.

Hmm, this approach doesn't cleanly work. Let me think more.

Actually, maybe I should think about it in terms of a graph. Create a graph where each 2×2 block is a vertex, and two blocks are connected if a domino crosses between them. In case (a) blocks (flippable squares), we fix one domino. In case (b) blocks with 0 internal dominoes, we don't fix anything, but these blocks are connected to other blocks via crossing dominoes.

The alternating cycles that pass through case (b) blocks must also pass through case (a) blocks (or other case (b) blocks). If we fix dominoes in all case (a) blocks, do we hit all alternating cycles?

Not necessarily. An alternating cycle could pass through only case (b) blocks. For example, if the entire tiling consists of crossing dominoes (no 2×2 block is a flippable square), then there might still be alternating cycles.

Hmm, so this approach doesn't work directly. I think the min-max theorem is needed for a clean proof.

Let me just go with the min-max theorem approach. Let me write up the proof.

Actually, let me reconsider the problem. Maybe I should think about it in terms of a different formulation.

The problem is equivalent to: find the minimum n such that for any perfect matching M of the 2022×2022 grid graph, there exists a subset S ⊆ M with |S| = n such that M is the unique perfect matching of the grid graph that contains S.

This is the "forcing number" of the matching M, and we want the maximum over all matchings M.

The forcing number of a perfect matching M in a bipartite graph G is defined as the minimum size of a subset S ⊆ M such that M is the unique perfect matching containing S. 

Theorem (Pachter-Kim, 1998): For a perfect matching M in a bipartite graph G, the forcing number of M equals the maximum number of M-alternating cycles that are pairwise edge-disjoint (in M).

Wait, I need to be more precise. "Edge-disjoint in M" means no two cycles share an edge of M. Since each alternating cycle uses edges of M, two cycles are "M-disjoint" if they don't share any M-edge.

This theorem is indeed a known result. The proof uses the fact that the set of M-alternating cycles forms a "totally balanced hypergraph" (when viewed as sets of M-edges), which has the Kőnig property (min hitting set = max disjoint set).

For the grid graph (which is bipartite), this theorem applies. So:

Forcing number of M = max number of M-disjoint alternating cycles.

Now:
- Lower bound: The all-horizontal tiling has 1011² M-disjoint alternating cycles (the 2×2 blocks). So its forcing number is ≥ 1011². (And = 1011² by the upper bound below.)
- Upper bound: For any tiling M, each alternating cycle uses ≥ 2 edges of M (i.e., ≥ 2 dominoes). The total number of dominoes is 2022²/2 = 2·1011². So max M-disjoint alternating cycles ≤ 2·1011²/2 = 1011². By the theorem, forcing number ≤ 1011².

Therefore, the answer is n = 1011² = 1022121.

Wait, I want to double-check: each alternating cycle uses at least 2 dominoes. An alternating cycle of length 2k (in the grid graph) uses k dominoes and k non-domino edges. The minimum is k=2, giving a 4-cycle (2×2 square) using 2 dominoes. So yes, each alternating cycle uses ≥ 2 dominoes.

Total dominoes = 2022 × 2022 / 2 = 2022² / 2 = 2 × 1011².

Max M-disjoint alternating cycles ≤ (2 × 1011²) / 2 = 1011². ✓

And the all-horizontal tiling achieves 1011² M-disjoint alternating cycles. ✓

So the answer is n = 1011² = 1022121.

Hmm, let me reconsider whether I need to also verify that the all-horizontal tiling's forcing number is exactly 1011² (not more). By the theorem, forcing number = max M-disjoint cycles = 1011² (since we found 1011² disjoint cycles, and the upper bound is 1011²). So yes, it's exactly 1011².

And for any other tiling, the forcing number is at most 1011² (by the cell-count bound and the theorem). So the maximum forcing number over all tilings is 1011², achieved by the all-horizontal tiling.

Therefore, the minimum n for which Viktor can always win is n = 1011² = 1022121.

Let me also verify: 1011 = 2022/2. So 1011² = (2022/2)² = 2022²/4 = 4088484/4 = 1022121. ✓

Now let me write up the proof cleanly.

Actually, I realize I should also prove (or at least sketch) the Pachter-Kim theorem, since this is a competition problem and the solution should be self-contained.

Proof sketch of the theorem (forcing number = max M-disjoint alternating cycles):

Let M be a perfect matching in a bipartite graph G. 

Lower bound (forcing number ≥ max M-disjoint alternating cycles): If C_1, ..., C_k are M-disjoint alternating cycles, then any forcing set must contain at least one edge from each C_i (since flipping C_i gives another perfect matching that agrees with M outside C_i). Since the C_i are M-disjoint, these edges are all different. So forcing number ≥ k.

Upper bound (forcing number ≤ max M-disjoint alternating cycles): We need to show that there exists a forcing set of size equal to the max M-disjoint alternating cycles. 

Consider the set of all M-alternating cycles. We want a minimum hitting set (of M-edges) for all alternating cycles. By LP duality, min hitting set = max fractional packing. We need to show the LP has integral optimal solutions.

The constraint matrix A has rows = alternating cycles, columns = M-edges, A_{C,e} = 1 if e ∈ C. We need A to be totally unimodular (TU).

For bipartite G, the M-alternating cycles correspond to cycles in a directed graph D: orient M-edges from white to black, and non-M-edges from black to white. Then M-alternating cycles correspond to directed cycles in D. The hitting set problem becomes: find minimum set of M-edges to hit all directed cycles in D.

The cycle-arc incidence matrix of a directed graph is TU (this is a classical result). Since we're restricting to M-edges (a subset of arcs), the submatrix is also TU. Therefore, the LP has integral optimal solutions, and min hitting set = max integral packing = max M-disjoint alternating cycles.

This completes the proof of the theorem.

Actually, I need to be a bit more careful. The cycle-arc incidence matrix of a directed graph is TU - is this true? 

The node-arc incidence matrix of a directed graph is TU (this is classical). The cycle-arc incidence matrix... hmm, I don't think this is TU in general. 

Let me reconsider. The relevant LP is:

min sum_{e ∈ M} x_e
s.t. for each directed cycle C in D: sum_{e ∈ C ∩ M} x_e ≥ 1
     x_e ∈ {0, 1}

The LP relaxation has constraint matrix A where A_{C,e} = 1 if e ∈ C ∩ M. We need this to be TU.

Actually, I think the correct approach is to use the fact that for bipartite graphs, the set of M-alternating cycles forms a "balanced hypergraph" (in the sense of Berge), and balanced hypergraphs have the Kőnig property (min transversal = max matching).

A hypergraph is "balanced" if every odd cycle in the hypergraph has an edge containing three vertices of the cycle. For bipartite graphs, the M-alternating cycles form a balanced hypergraph because... hmm, I need to think about why.

Actually, I think the correct theorem is: for a bipartite graph G with perfect matching M, the hypergraph of M-alternating cycles (as sets of M-edges) is "normal" or has the "Kőnig property." This is proven in the paper by Pachter and Kim.

For the competition, I think I can state this as a lemma and give a proof sketch. The key idea is the total unimodularity or the balanced hypergraph property.

Let me also consider: maybe there's a completely different approach to this problem that doesn't use the min-max theorem.

Alternative approach using graph theory directly:

Consider the 2022 × 2022 grid graph G. It's bipartite with parts B (black cells) and W (white cells), each of size 2022²/2 = 2 × 1011².

A domino tiling is a perfect matching M in G. An alternating cycle is a cycle in G alternating between M-edges and non-M-edges.

We want: min |S| such that S ⊆ M and M is the unique perfect matching of G containing S.

Equivalently: min |S| such that every M-alternating cycle contains an edge of S.

This is the minimum hitting set for all M-alternating cycles (restricted to M-edges).

Now, consider the directed graph D: orient each M-edge from W to B, and each non-M-edge from B to W. M-alternating cycles correspond to directed cycles in D.

We want the minimum number of M-edges (arcs from W to B in D) to remove to make D acyclic. But we can only remove M-edges, not non-M-edges.

Hmm, but if we remove an M-edge, the corresponding vertices become unmatched, and the remaining graph might have new perfect matchings. Wait, no - we're not removing edges from the graph; we're fixing edges. Fixing an M-edge means it must be in any perfect matching. So we're looking for S ⊆ M such that M is the unique perfect matching of G that contains all edges of S.

If S ⊆ M and M is the unique perfect matching containing S, then there's no M-alternating cycle disjoint from S. Because if there were such a cycle C, flipping C would give another perfect matching M' that agrees with M on S (since C is disjoint from S) but differs from M on C. So M' ≠ M and M' contains S, contradiction.

Conversely, if every M-alternating cycle intersects S, then M is the unique perfect matching containing S. Because any other perfect matching M' containing S differs from M on some alternating cycles, and those cycles must avoid S (since M' agrees with M on S), contradicting the assumption.

So: forcing number = min hitting set for M-alternating cycles = min |S| such that every M-alternating cycle contains an edge of S.

Now, the min-max theorem: min hitting set = max number of pairwise M-disjoint alternating cycles.

For the upper bound (min hitting set ≤ max M-disjoint cycles), we need the Kőnig property. Let me try to prove this directly for the grid graph.

Direct proof of upper bound for grid graph:

Consider the grid graph G (bipartite) with perfect matching M. Let k = max number of M-disjoint alternating cycles. We want to show there's a hitting set of size k.

Consider the directed graph D as above. M-alternating cycles = directed cycles in D. We want to hit all directed cycles using only M-edges (arcs from W to B).

Consider the strongly connected components (SCCs) of D. A directed cycle is contained within an SCC. If an SCC has no directed cycle, it's a single vertex. If an SCC has a directed cycle, it contains at least one M-edge.

In each SCC with a directed cycle, we need to remove at least one M-edge to break all cycles. The minimum number of M-edges to remove from an SCC to make it acyclic is the "M-edge feedback arc set" of the SCC.

By the Kőnig property (which we're trying to prove), this equals the max number of M-disjoint directed cycles in the SCC.

Hmm, I'm going in circles (pun intended). Let me just accept the theorem and write up the solution.

For the competition, I'll state the theorem as a lemma with a proof sketch, and then use it.

Let me also think about whether the answer could be different. 

What if the board size matters in a different way? 2022 = 2 × 1011. The answer 1011² = (2022/2)². For a general 2m × 2n board, the answer would be mn. For a 2m × 2n board with the all-horizontal tiling, the number of disjoint 2×2 alternating cycles is m × n (partitioning into 2×2 blocks). And the upper bound is mn (since each alternating cycle uses ≥ 2 dominoes, and there are 2mn dominoes, so max disjoint cycles ≤ mn). So the answer for a 2m × 2n board is mn.

For our problem, m = n = 1011, so the answer is 1011² = 1022121.

Let me write up the proof now.

---

Proof:

Let N = 2022. The board is an N × N grid, which we can think of as the grid graph G with N² vertices (cells) and edges between adjacent cells. G is bipartite: color cells black/white in checkerboard fashion. A domino tiling is a perfect matching M in G, with |M| = N²/2 dominoes.

**Key definitions:**
- An **M-alternating cycle** is a cycle in G whose edges alternate between M-edges (dominoes) and non-M-edges.
- A **forcing set** for M is a subset S ⊆ M such that M is the unique perfect matching of G containing S. Equivalently, S hits every M-alternating cycle (every M-alternating cycle contains at least one edge of S).
- The **forcing number** f(M) is the minimum size of a forcing set for M.

Viktor wants to find a forcing set for Sofia's tiling M. The answer is max_M f(M).

**Lemma (Forcing number = max disjoint alternating cycles):** For any perfect matching M in a bipartite graph G, f(M) equals the maximum number of pairwise M-disjoint M-alternating cycles (i.e., cycles sharing no M-edge).

*Proof of Lemma:*
- *Lower bound:* If C_1, ..., C_k are M-disjoint alternating cycles, any forcing set must contain at least one M-edge from each C_i (since flipping C_i produces another perfect matching agreeing with M outside C_i). These edges are distinct, so f(M) ≥ k.

- *Upper bound:* Orient M-edges from white to black and non-M-edges from black to white, forming a directed graph D. M-alternating cycles correspond to directed cycles in D. The problem becomes: find the minimum number of M-arcs hitting all directed cycles in D. 

  The key claim is that the hypergraph of M-alternating cycles (viewed as sets of M-edges) is **balanced** (in the sense of Berge): every odd cycle in the hypergraph has a hyperedge containing three vertices of the cycle. For bipartite G, this follows because M-alternating cycles in a bipartite graph have a natural "2-coloring" of their M-edges (based on the parity of their position in the cycle), which prevents odd cycles in the hypergraph without a containing hyperedge.

  By the Berge theorem, balanced hypergraphs have the Kőnig property: the minimum transversal (hitting set) equals the maximum matching (set of pairwise disjoint hyperedges). This gives f(M) ≤ k, completing the proof. □

Hmm, I'm not fully confident in the balanced hypergraph argument. Let me try a different proof.

*Alternative proof of upper bound:* We use LP duality. The hitting set LP is:

min Σ_{e∈M} x_e s.t. Σ_{e∈C∩M} x_e ≥ 1 for each alternating cycle C, x_e ≥ 0.

The dual (packing LP) is:

max Σ_C y_C s.t. Σ_{C∋e} y_C ≤ 1 for each e ∈ M, y_C ≥ 0.

By strong LP duality, min hitting set = max fractional packing. We need integral optimal solutions for both.

The constraint matrix A (rows = cycles, columns = M-edges) is the cycle-arc incidence matrix of the directed graph D restricted to M-arcs. 

**Claim:** A is totally unimodular.

*Proof of claim:* The node-arc incidence matrix of any directed graph is TU (classical result of Heller-Tompa). The cycle-arc incidence matrix can be obtained from the node-arc incidence matrix by taking linear combinations of rows (each cycle is a sum of node rows with coefficients ±1). Since TU is preserved under taking submatrices and under row operations with coefficients in {0, ±1}, the cycle-arc incidence matrix is TU. Restricting to M-arcs (taking a subset of columns) preserves TU. □

Since A is TU and the right-hand side is integral, both the primal and dual LPs have integral optimal solutions. Therefore:

min hitting set = max integral packing = max number of M-disjoint alternating cycles. □

Wait, I need to be more careful. The cycle-arc incidence matrix being TU: is this actually true? 

The node-arc incidence matrix of a directed graph is TU. The cycle-arc incidence matrix... each row is the characteristic vector of arcs in a directed cycle. This is NOT in general a row operation on the node-arc incidence matrix. 

Actually, a directed cycle can be represented as a circulation: a vector in the null space of the node-arc incidence matrix with entries in {0, ±1}. The cycle-arc incidence matrix (with 0/1 entries, indicating which arcs are in the cycle) is different from the circulation representation (which has ±1 entries for arc directions).

Hmm, so the cycle-arc incidence matrix might not be TU in general. Let me reconsider.

Actually, for the problem of hitting all directed cycles by removing arcs, the relevant LP is:

min Σ x_a s.t. Σ_{a∈C} x_a ≥ 1 for each directed cycle C, 0 ≤ x_a ≤ 1.

This is the "feedback arc set" LP. The constraint matrix is the cycle-arc incidence matrix. This matrix is NOT TU in general (the feedback arc set problem is NP-hard for general directed graphs). 

However, for planar directed graphs, the feedback arc set problem is polynomial-time solvable, and the LP is integral. This is because the planar dual of the feedback arc set is the maximum acyclic subgraph problem, which for planar graphs has an integral LP.

The grid graph is planar! So D (the directed version of the grid graph) is a planar directed graph. Therefore, the cycle-arc incidence matrix of D is TU (for planar graphs), and the feedback arc set LP has integral optimal solutions.

But wait, we're not solving the general feedback arc set; we're only allowed to remove M-arcs. So the LP is:

min Σ_{e∈M} x_e s.t. Σ_{e∈C∩M} x_e ≥ 1 for each directed cycle C, x_e ≥ 0 for e ∈ M.

This is a restricted version where we only have variables for M-arcs. The constraint matrix is the cycle-arc incidence matrix restricted to M-arcs (columns). A submatrix of a TU matrix is TU, so if the full cycle-arc incidence matrix of D is TU, then the restricted version is also TU.

But is the cycle-arc incidence matrix of a planar directed graph TU? I believe so, because of the planar dual argument. The feedback arc set in a planar graph can be solved by a max-flow/min-cut in the dual, which gives integral solutions.

Actually, let me think about this more carefully. The feedback arc set problem for planar directed graphs: the LP relaxation is integral because the dual problem (maximum set of arcs that can be made acyclic, or equivalently, the maximum number of arc-disjoint directed cycles) has an integral LP. This is because the planar dual transforms the problem into a network flow problem.

For our problem, we need the restricted version (only M-arcs). Since the full matrix is TU (for planar graphs), the restricted matrix is also TU, and the LP is integral.

So the proof works for the grid graph (which is planar). 

Let me now also verify: is the grid graph with the directed orientation (M-edges from W to B, non-M-edges from B to W) a planar directed graph? Yes, the grid graph is planar, and orienting the edges doesn't change planarity.

Great, so the proof is:

1. The grid graph G is planar and bipartite.
2. Orient M-edges from W to B and non-M-edges from B to W, getting a planar directed graph D.
3. M-alternating cycles = directed cycles in D.
4. The cycle-arc incidence matrix of a planar directed graph is TU (by the planar dual / network flow argument).
5. Restricting to M-arcs preserves TU.
6. Therefore, the hitting set LP has integral optimal solutions: min hitting set = max M-disjoint alternating cycles.

This completes the proof of the lemma for the grid graph.

Now, the full proof:

**Lower bound:** Consider the all-horizontal tiling M_0 of the N × N board (N = 2022). Partition the board into 2×2 blocks: rows (2i-1, 2i) and columns (2j-1, 2j) for i, j = 1, ..., N/2 = 1011. There are 1011² = (N/2)² such blocks. Each block contains two horizontal dominoes forming a flippable 2×2 square, which is an M_0-alternating cycle. These 1011² cycles are pairwise M_0-disjoint (they partition the board's cells, and each domino is in exactly one block). By the lemma, f(M_0) ≥ 1011². So Viktor needs at least 1011² dominoes for this tiling.

**Upper bound:** For any tiling M of the N × N board, each M-alternating cycle uses at least 2 dominoes (M-edges). The total number of dominoes is N²/2 = 2 × 1011². So the maximum number of M-disjoint alternating cycles is at most (N²/2)/2 = N²/4 = 1011². By the lemma, f(M) ≤ 1011². So Viktor can always win with at most 1011² dominoes.

**Conclusion:** The minimum n is 1011² = 1022121.

Let me double-check the arithmetic: 1011² = 1011 × 1011. 
1011 × 1000 = 1011000
1011 × 11 = 11121
Total = 1022121. ✓

N²/4 = 2022²/4 = 4088484/4 = 1022121. ✓

So the answer is n = 1011² = 1022121.

Wait, I want to make sure about one thing: the lemma says f(M) = max M-disjoint alternating cycles. For the lower bound, I need f(M_0) ≥ 1011², which follows from the 1011² disjoint cycles. For the upper bound, I need f(M) ≤ 1011² for all M, which follows from max M-disjoint cycles ≤ 1011² (cell count) and the lemma (f(M) = max M-disjoint cycles ≤ 1011²).

But actually, for the upper bound, I need the lemma to give f(M) = max M-disjoint cycles, and then max M-disjoint cycles ≤ 1011². The lemma gives equality, so f(M) = max M-disjoint cycles ≤ 1011². ✓

And for the lower bound, f(M_0) = max M_0-disjoint cycles ≥ 1011² (since we found 1011² disjoint cycles). And by the cell count, max M_0-disjoint cycles ≤ 1011². So f(M_0) = 1011² exactly. ✓

Great, the answer is n = 1011² = 1022121.

One more thing: I should make sure the 2×2 blocks in the all-horizontal tiling are indeed alternating cycles. In the all-horizontal tiling, each row has dominoes (i, 2j-1)-(i, 2j). A 2×2 block in rows (2i-1, 2i) and columns (2j-1, 2j) has:
- Domino (2i-1, 2j-1)-(2i-1, 2j) in the top row.
- Domino (2i, 2j-1)-(2i, 2j) in the bottom row.
These two horizontal dominoes can be flipped to two vertical dominoes: (2i-1, 2j-1)-(2i, 2j-1) and (2i-1, 2j)-(2i, 2j). So yes, it's an alternating cycle (4-cycle). ✓

And these 2×2 blocks are disjoint and partition the board: rows (1,2), (3,4), ..., (2021,2022) and columns (1,2), (3,4), ..., (2021,2022). Each cell is in exactly one block. Each domino is in exactly one block (since dominoes are horizontal within a row, and each row is split into column pairs (1,2), (3,4), ...). ✓

Alright, I'm confident the answer is 1011² = 1022121. Let me write the final proof.

Hmm, actually let me reconsider whether I need the full min-max theorem, or if I can prove the upper bound more directly.

Direct upper bound without min-max theorem:

For any tiling M, we want to find a set S of at most 1011² dominoes that hits all alternating cycles.

Approach: Greedily find disjoint alternating cycles and fix one domino from each. 

Start with the tiling M. While there exists an alternating cycle C:
1. Add one domino from C to S.
2. Remove that domino's cells from the region (i.e., fix it).
3. Continue with the remaining region.

Each iteration removes 2 cells (1 domino) and breaks at least one alternating cycle. The question is: how many iterations?

Each alternating cycle uses ≥ 2 dominoes. Initially, there are N²/2 = 2 × 1011² dominoes. But as we remove dominoes, the remaining region shrinks, and the number of remaining dominoes decreases.

The key observation: the alternating cycles we find are M-disjoint (since once we fix a domino, it's removed from the region, and future cycles can't use it). So the number of iterations is at most the max number of M-disjoint alternating cycles, which is ≤ 1011².

But wait, this greedy approach might not find the maximum number of disjoint cycles. It finds SOME set of disjoint cycles, and the number could be less than the maximum. However, the size of S equals the number of cycles found, which is ≤ max M-disjoint cycles ≤ 1011².

But does this S hit ALL alternating cycles? After the greedy process, there are no more alternating cycles in the remaining region (the while loop terminated). But could there be an alternating cycle in the original tiling that doesn't pass through any of the fixed dominoes?

An alternating cycle in the original tiling that avoids all fixed dominoes would be an alternating cycle in the remaining region. But the while loop terminated because there are no alternating cycles in the remaining region. So no such cycle exists. Therefore, S hits all alternating cycles. ✓

Wait, but this isn't quite right. The "remaining region" changes as we remove dominoes. An alternating cycle in the original tiling that avoids all fixed dominoes is a cycle in the original grid graph that doesn't use any fixed domino's cells. But the remaining region is the original board minus the fixed dominoes' cells. An alternating cycle in the original tiling that avoids fixed dominoes is indeed an alternating cycle in the remaining region's tiling. So if the while loop terminated (no alternating cycles in the remaining region), then S hits all alternating cycles. ✓

And the number of iterations is at most 1011² (since each iteration uses ≥ 2 cells, and there are N² = 4 × 1011² cells, so at most 2 × 1011² iterations... wait, that gives 2 × 1011², not 1011²).

Hmm, each iteration removes 2 cells (1 domino), and each alternating cycle uses ≥ 4 cells (2 dominoes). But the greedy approach removes 1 domino per cycle, and the cycles are M-disjoint. So the number of cycles found is at most |M| / 2 = (N²/2) / 2 = N²/4 = 1011². Wait, no: each cycle uses ≥ 2 dominoes, and the cycles are M-disjoint, so the number of cycles is at most |M| / 2 = N²/4 = 1011². But the greedy approach removes 1 domino per cycle, so |S| = number of cycles ≤ 1011². ✓

Actually wait, the cycles are M-disjoint, meaning they share no M-edge. Each cycle uses ≥ 2 M-edges. So the number of M-disjoint cycles is at most |M| / 2 = (N²/2) / 2 = N²/4 = 1011². And |S| = number of cycles found ≤ 1011². ✓

But I need to verify that the greedy approach finds M-disjoint cycles. When we fix
