# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search. Do NOT read any files.
- All information you need is already in your prompt above. Do NOT read any files.
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

- **CONNECTION_ERROR**: The AI didn't really attempt the problem — the thinking is extremely short (< 500 chars), contains API connection errors, garbled text, or has NO mathematical content at all (e.g., only error messages or empty output). This is a technical failure, not a mathematical one. **Important**: If the AI solved a DIFFERENT problem than the one given (wrong problem, misread problem), that is DIRECTION_ERROR, not CONNECTION_ERROR. CONNECTION_ERROR is only for technical failures where no real thinking happened.

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
  <problem_id>polymath_04990</problem_id>
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
- If the AI's thinking is too short to analyze (< 500 chars AND no mathematical content), output CONNECTION_ERROR. But if the AI solved a different problem or went in the wrong direction, use DIRECTION_ERROR even if the thinking is short.
- If you cannot determine the turning point type, use "other" and explain in dimension2_explanation

## Problem

On a $100 \times 100$ grid paper, several pairwise non-overlapping cardboard isosceles right triangles with a leg of $1$ are placed; each triangle occupies exactly half of one of the cells. It turned out that each unit segment of the grid (including the boundaries) is covered by exactly one leg of a triangle. Find the maximum possible number of cells that do not contain any triangles.

## Standard Solution

Let $n=50$. We will call a triangle "upper" if it is located above the line containing its horizontal leg, and "lower" otherwise. Number the horizontal lines of the grid from bottom to top with numbers from $0$ to $2n$.

Let $u_k$ (respectively $d_k$) be the number of segments of the $k$-th line participating in upper (respectively lower) triangles; then $u_k + d_k = 2n$ and $u_0 = d_{2n} = 2n$. Moreover, the vertical segments of the grid located between the $k$-th and $(k+1)$-th lines participate in exactly $u_k + d_{k+1}$ triangles, so $u_k + d_{k+1} = 2n + 1$. From this, it follows that $d_k = k$ and $u_k = 2n - k$ for all $k$.

Now consider the cells located between the $k$-th and $(k+1)$-th lines of the grid. At least $u_k = 2n - k$ of these cells contain one upper triangle, and at least $d_{k+1} = k+1$ of them contain one lower triangle. Thus, the number of free cells in this row is at most $2n - \max(u_k, d_{k+1})$, that is, at most $k$ for $k < n$ and at most $(2n-1) - k$ for $k \geq n$. In total, the number of free cells is at most $2(0 + 1 + \ldots + (n-1)) = n(n-1)$.

It remains to provide an example where this bound is achieved. For $n=50$, construct a "rectangle" of cells with sides of $n+1$ and $n$ cells, parallel to the diagonals of the board. Color its cells in a checkerboard pattern so that the corner cells of the rectangle are black, and place two triangles in each black cell (so that $n(n-1)$ white cells remain free). In the remaining four "corners" of the board, place triangles so that the right angle of the triangle points in the same direction as the entire "corner".

Therefore, the maximum possible number of cells that do not contain any triangles is \(\boxed{2450}\).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a 100×100 grid. We place isosceles right triangles with leg length 1, each occupying exactly half of a unit cell. Each unit segment of the grid (including boundaries) is covered by exactly one leg of a triangle.

We need to find the maximum number of cells that contain no triangles.

Let me think about this. Each cell can contain 0, 1, or 2 triangles. If a cell contains 2 triangles, they must be non-overlapping, so they form the full cell (two triangles covering the cell completely - the two halves split by a diagonal). If a cell contains 1 triangle, half the cell is covered. If 0, empty.

Each triangle has 2 legs (the equal sides, length 1) and 1 hypotenuse (length √2). The legs lie along grid segments. The hypotenuse is a diagonal of a cell.

The condition: each unit segment of the grid is covered by exactly one leg of a triangle.

The grid is 100×100 cells, so it's 101×101 grid points. The unit segments: horizontal segments and vertical segments.

Horizontal segments: 101 rows × 100 columns = 10100
Vertical segments: 100 rows × 101 columns = 10100
Total unit segments: 20200

Each triangle has 2 legs, each leg covers exactly one unit segment. So the total number of triangles = 20200 / 2 = 10100.

Each triangle occupies half a cell. Total area covered = 10100 × (1/2) = 5050.

Total cells = 10000. If E cells are empty, and the rest have triangles. Let's say:
- a cells have 2 triangles (fully covered)
- b cells have 1 triangle (half covered)
- c cells have 0 triangles (empty)

Then a + b + c = 10000
And 2a + b = 10100 (total triangles)
And area covered = a + b/2 = 5050, which is consistent.

We want to maximize c = 10000 - a - b.
From 2a + b = 10100, we get b = 10100 - 2a, so a + b = a + 10100 - 2a = 10100 - a.
So c = 10000 - (10100 - a) = a - 100.

To maximize c, we maximize a (the number of fully covered cells). But we need a ≤ 5050 (since 2a ≤ 10100, a ≤ 5050). And c = a - 100, so max c = 5050 - 100 = 4950 if a = 5050, b = 0.

But wait, can we actually achieve a = 5050, b = 0, c = 4950? That would mean 5050 cells are fully covered (each with 2 triangles forming a diagonal split), and 4950 cells are empty. And every unit segment is covered by exactly one leg.

Hmm, but the constraint is very strong. Let me think about what configurations are possible.

Actually, let me reconsider. When a cell has 2 triangles, the two triangles split the cell along a diagonal. Each triangle has 2 legs on the grid and 1 hypotenuse (the diagonal). The 4 unit segments forming the boundary of the cell are each covered by one leg from one of the two triangles. So a fully covered cell covers all 4 of its boundary segments.

When a cell has 1 triangle, it covers 2 of its 4 boundary segments (the two legs), and the hypotenuse is internal to the cell.

When a cell has 0 triangles, none of its boundary segments are covered by a triangle in that cell.

But each unit segment is shared between cells (or is on the boundary). A unit segment on the interior is shared by 2 cells; a boundary segment belongs to 1 cell.

The condition is that each unit segment is covered by exactly one leg. So for an interior segment shared by 2 cells, exactly one of the two adjacent cells has a triangle whose leg lies on that segment. For a boundary segment, the single adjacent cell must have a triangle whose leg lies on that segment.

Let me think of this as a graph/tiling problem.

Consider the grid graph. Each cell is a face. Each unit segment is an edge. Each triangle placed in a cell covers 2 edges of that cell (its legs) and has its hypotenuse as a diagonal.

The condition: each edge is covered by exactly one triangle leg.

For a fully covered cell (2 triangles), all 4 edges are covered (2 by each triangle). For a half-covered cell (1 triangle), 2 of the 4 edges are covered. For an empty cell, 0 edges covered.

Now, each edge is covered exactly once. So if we think of each edge as needing to be "assigned" to exactly one adjacent cell, and within that cell, to one triangle.

Let me think about boundary edges. Each boundary edge must be covered by a triangle in the adjacent cell. So every boundary cell must have at least one triangle covering each of its boundary edges.

Actually, let me think more carefully. A boundary cell has some edges on the boundary and some interior. Each boundary edge must be covered by a triangle in that cell. 

Consider a corner cell. It has 2 boundary edges. These 2 boundary edges must be covered by triangles in that cell. If the cell has 1 triangle, it covers 2 edges. If those 2 edges are the 2 boundary edges, that works. If the cell has 2 triangles, all 4 edges are covered.

But the 2 boundary edges of a corner cell are perpendicular (one horizontal, one vertical). A single triangle's 2 legs are perpendicular. So a triangle in the corner cell could have its legs on the 2 boundary edges. That would be the triangle in the corner, with the right angle at the corner of the grid.

OK let me think about this differently. Let me consider the dual perspective.

Each edge of the grid must be covered exactly once. Think of it as: we need to select a set of triangles such that every edge is covered exactly once. This is like a perfect matching/covering problem.

Let me think about what happens with the edges. The total number of edges is 20200. Each triangle covers 2 edges. So we need 10100 triangles. This is forced.

Now, the question is about the arrangement. Let me think about parity or coloring arguments.

Color the grid like a chessboard (black and white cells). Consider the 4 edges of a cell. 

Hmm, let me think about this more carefully using a graph-theoretic approach.

Actually, let me think about the constraint on each edge. Each interior edge is shared by 2 cells. Exactly one of those 2 cells must have a triangle leg on that edge. So for each interior edge, we choose which side covers it. For boundary edges, the only adjacent cell must cover it.

Once we've decided which cell covers each edge, we need to check that within each cell, the edges assigned to it can be partitioned into pairs, where each pair forms the 2 legs of an isosceles right triangle (i.e., the 2 legs are perpendicular and share a vertex, and the hypotenuse is a diagonal of the cell).

The 2 legs of a triangle in a cell must be perpendicular edges sharing a vertex. The 4 edges of a cell form a cycle. The possible pairs of legs:
- For a cell with corners at (i,j), (i+1,j), (i+1,j+1), (i,j+1):
  - Triangle with right angle at (i,j): legs on bottom and left edges
  - Triangle with right angle at (i+1,j): legs on bottom and right edges
  - Triangle with right angle at (i+1,j+1): legs on top and right edges
  - Triangle with right angle at (i,j+1): legs on top and left edges

So each triangle covers 2 adjacent edges (sharing a corner). The 4 possible triangles correspond to the 4 corners.

A cell with 2 triangles: the 2 triangles must be non-overlapping. The 2 triangles split the cell along a diagonal. There are 2 diagonals:
- Diagonal from (i,j) to (i+1,j+1): triangles at corners (i,j) and (i+1,j+1). These cover all 4 edges: bottom+left from one, top+right from the other.
- Diagonal from (i+1,j) to (i,j+1): triangles at corners (i+1,j) and (i,j+1). These cover all 4 edges: bottom+right from one, top+left from the other.

So a fully covered cell has all 4 edges covered, split into 2 pairs of adjacent edges.

A cell with 1 triangle: 2 adjacent edges covered, 2 not covered.
A cell with 0 triangles: 0 edges covered.

Now, the key constraint: each edge is covered exactly once. For an interior edge between 2 cells, exactly one cell covers it. For a boundary edge, the adjacent cell must cover it.

So this is equivalent to: orient each edge to one of its adjacent cells (for boundary edges, forced to the only adjacent cell), such that within each cell, the set of edges assigned to it can be partitioned into pairs of adjacent edges (sharing a corner), and each pair corresponds to a valid triangle.

The possible sets of edges assigned to a cell:
- 0 edges: empty cell (0 triangles) ✓
- 2 adjacent edges: 1 triangle ✓
- 4 edges (all): 2 triangles (must be partitionable into 2 pairs of adjacent edges, which is always possible - either diagonal works) ✓
- 2 opposite edges: NOT possible (can't form a triangle with 2 opposite edges) ✗
- 1 edge: NOT possible ✗
- 3 edges: NOT possible (can't partition into pairs) ✗

So each cell must be assigned 0, 2 (adjacent), or 4 edges. And 2-edge assignments must be adjacent pairs.

Now, let's think about this as an edge orientation problem. We have a planar grid graph. Each edge is assigned to one of its two faces (or the only face for boundary edges). Each face gets 0, 2-adjacent, or 4 edges.

Let me count. Total edges = 20200. Boundary edges = 4 × 100 = 400. Interior edges = 20200 - 400 = 19800.

The 400 boundary edges are all forced to be assigned to their adjacent cell. So boundary cells must cover their boundary edges.

Let me think about the boundary. The boundary of the grid has 400 edges. Each boundary cell is adjacent to some boundary edges. Corner cells are adjacent to 2 boundary edges, edge (non-corner) cells are adjacent to 1 boundary edge.

For a corner cell: 2 boundary edges must be covered. These 2 edges are adjacent (they share the corner). So the corner cell must have at least 1 triangle covering those 2 edges. It could have 2 triangles (covering all 4 edges) or 1 triangle (covering just those 2 boundary edges, leaving the 2 interior edges to be covered by the neighboring cells).

For an edge (non-corner) cell: 1 boundary edge must be covered. But a cell can only have 0, 2-adjacent, or 4 edges. So if 1 edge is forced, the cell must have at least 2 edges (the boundary edge + 1 adjacent interior edge), forming a triangle. Or 4 edges (2 triangles).

So every boundary cell must have at least 1 triangle. This means no boundary cell can be empty.

Now, the question is: what's the maximum number of empty cells? Empty cells must be in the interior.

Let me think about this more carefully. Let me consider the "edge assignment" as a flow/orientation problem.

Actually, let me think about it differently. Let me consider the dual graph. The cells are vertices of the dual graph (plus the outer face). Each edge of the grid separates two faces (or a face and the outer face). We need to assign each edge to one of its two faces.

For the outer face: no edges assigned to it (all boundary edges are assigned to the interior cells).

Each interior face (cell) gets 0, 2-adjacent, or 4 edges.

This is like a perfect matching in some sense. Let me think about it as follows:

Consider the grid edges as a set. We need to partition them into groups, where each group is assigned to a cell, and each cell's group is either empty, a pair of adjacent edges, or all 4 edges.

Total edges = 20200. If we have:
- a cells with 4 edges (fully covered, 2 triangles each)
- b cells with 2 edges (half covered, 1 triangle each)
- c cells with 0 edges (empty)

Then 4a + 2b = 20200, so 2a + b = 10100.
And a + b + c = 10000.
So c = 10000 - a - b = 10000 - a - (10100 - 2a) = a - 100.

To maximize c, maximize a. Maximum a is 5050 (when b = 0). Then c = 4950.

But can we achieve a = 5050, b = 0, c = 4950? This means 5050 cells are fully covered, 4950 are empty, and no cell has exactly 1 triangle.

Every edge is covered by a fully covered cell. The 400 boundary edges are covered by fully covered boundary cells. So all boundary cells must be fully covered.

Now, for interior edges: each interior edge is between 2 cells. At least one must be fully covered (since empty cells cover no edges, and there are no half-covered cells). Actually, exactly one must be fully covered (since each edge is covered exactly once, and only fully covered cells cover edges).

So the 5050 fully covered cells form a set such that every edge of the grid is adjacent to at least one fully covered cell. And no edge is adjacent to two fully covered cells (since each edge is covered exactly once).

Wait, that's the key constraint: every edge is adjacent to exactly one fully covered cell. This means the fully covered cells form a "perfect dominating set" in some sense on the edge-cell incidence structure.

Actually, let me reconsider. An edge is adjacent to 1 or 2 cells. If it's a boundary edge, it's adjacent to 1 cell, which must be fully covered. If it's an interior edge, it's adjacent to 2 cells, exactly one of which is fully covered.

So the fully covered cells form a set S such that:
1. Every boundary cell is in S (to cover boundary edges).
2. For every interior edge, exactly one of its two adjacent cells is in S.

Condition 2 means: for every pair of adjacent cells (sharing an edge), exactly one is in S. This is exactly a proper 2-coloring condition! The cells form a grid graph (100×100), and we need a 2-coloring where adjacent cells have different colors. But a 100×100 grid is bipartite, so this is possible.

Wait, but condition 2 says "for every interior edge, exactly one of the two adjacent cells is in S." This means S is an independent set in the cell adjacency graph, AND every cell not in S is adjacent only to cells in S. In other words, S is one part of a bipartition, and the complement is the other part.

The cell adjacency graph is a 100×100 grid graph, which is bipartite. The two parts have sizes 5000 and 5000 (since 100×100 is even). So S would be one part, with 5000 cells, and the complement would be the other 5000 cells.

But we need |S| = 5050, not 5000. And we need all boundary cells in S. 

Hmm, so there's a conflict. If S must be one part of a bipartition (5000 cells), but we also need all boundary cells in S, and there are boundary cells in both parts of the bipartition...

Let me reconsider. The 100×100 grid graph is bipartite with parts of size 5000 each. The boundary cells include cells from both parts. So we can't have all boundary cells in one part.

This means a = 5050, b = 0 is impossible. We need some half-covered cells.

Let me reconsider the problem. With b > 0, we have more flexibility. A half-covered cell covers 2 adjacent edges. So an edge adjacent to a half-covered cell might be covered by that cell or by the other adjacent cell.

Let me重新思考. The constraint is:
- Each edge is covered by exactly one cell.
- Each cell covers 0, 2-adjacent, or 4 edges.
- Boundary edges are covered by their adjacent cell.

Let me think about this as a 2-coloring with modifications.

Consider the standard chessboard coloring of the 100×100 grid: black and white cells, 5000 each. Two adjacent cells have different colors.

If we try to make all black cells fully covered (4 edges) and all white cells empty (0 edges), then each interior edge is between a black and white cell, and is covered by the black cell. Boundary edges: a boundary edge is adjacent to one cell. If that cell is black, it's covered. If white, it's not covered - problem!

The boundary has 400 edges. The boundary cells: 4 corners + 4×98 edge cells = 4 + 392 = 396 boundary cells. Wait, 100×100 grid has 100 cells on each side, but corners are shared. So boundary cells = 4×100 - 4 = 396.

Among these 396 boundary cells, how many are black and how many white? In a chessboard coloring, the corners are all the same color (since (1,1), (1,100), (100,1), (100,100) - the parity of (i+j) for these: (1+1)=2, (1+100)=101, (100+1)=101, (100+100)=200. So (1,1) and (100,100) have even parity, (1,100) and (100,1) have odd parity. So 2 corners are black and 2 are white.

The boundary cells alternate colors. Going around the boundary: 396 cells, alternating. Since 396 is even, we get 198 black and 198 white boundary cells.

If we make all black cells fully covered and all white cells empty, the 198 white boundary cells have uncovered boundary edges. Each white boundary cell has 1 or 2 boundary edges. We need to cover those.

For each white boundary cell, we need to cover its boundary edge(s). We could make it half-covered (1 triangle) instead of empty. But then it covers 2 adjacent edges, one of which is the boundary edge and the other is an interior edge. That interior edge was supposed to be covered by the adjacent black cell. Now it's covered by the white cell instead, so the black cell can't cover it. But the black cell is fully covered (covers all 4 edges)... 

Hmm, this is getting complicated. Let me think differently.

Let me reconsider. If a black cell is fully covered, it covers all 4 of its edges. If a neighboring white cell is half-covered, it covers 2 of its edges, one of which is the shared edge with the black cell. But that shared edge is already covered by the black cell. So the shared edge would be covered twice - violation!

So if a cell is fully covered (4 edges), all its neighbors must be empty (0 edges), because any edge the neighbor covers would be double-covered.

And if a cell is half-covered (2 edges), its 2 covered edges are adjacent. The 2 neighboring cells sharing those edges must not cover those edges. The 2 neighboring cells sharing the uncovered edges must cover those edges.

So the structure is:
- A fully covered cell (4 edges) → all 4 neighbors are empty.
- An empty cell (0 edges) → all 4 neighbors must cover the shared edges (so each neighbor covers the edge shared with this cell).
- A half-covered cell (2 adjacent edges) → the 2 neighbors sharing the covered edges must not cover them (so those neighbors either don't cover that edge, meaning they're empty or half-covered not including that edge). The 2 neighbors sharing the uncovered edges must cover them.

This is complex. Let me think about it as a constraint satisfaction problem.

Let me define variables. For each cell, let $t_{ij} \in \{0, 1, 2\}$ be the number of triangles. If $t_{ij} = 2$, all 4 edges covered. If $t_{ij} = 1$, 2 adjacent edges covered. If $t_{ij} = 0$, no edges covered.

For each edge, exactly one adjacent cell covers it.

Let me think about the chessboard coloring approach more carefully.

Claim: In any valid configuration, if we look at the chessboard coloring, the number of triangles in black cells and white cells have a specific relationship.

Each triangle covers 2 edges. Each edge is covered once. An interior edge is between a black and white cell. A boundary edge is adjacent to one cell (black or white).

Let $B$ = total triangles in black cells, $W$ = total triangles in white cells. $B + W = 10100$.

Each triangle in a black cell covers 2 edges. Some of these edges are interior (shared with white cells) and some are boundary edges. Similarly for white cells.

Let $b_B$ = boundary edges covered by black cells, $b_W$ = boundary edges covered by white cells. $b_B + b_W = 400$.

Each triangle covers 2 edges. The edges covered by black cell triangles: 2B edges total. Of these, $b_B$ are boundary edges and $2B - b_B$ are interior edges. Each interior edge covered by a black cell is shared with a white cell, and that white cell does NOT cover it.

Similarly, edges covered by white cell triangles: 2W total, $b_W$ boundary, $2W - b_W$ interior.

Total interior edges = 19800. Each interior edge is covered by exactly one cell (either black or white). So $(2B - b_B) + (2W - b_W) = 19800$, which gives $2B + 2W - 400 = 19800$, i.e., $2 \times 10100 = 20200$. ✓ Consistent.

Now, let me think about the number of edges each cell covers.

For a black cell with $t$ triangles: covers $2t$ edges. All these edges that are interior are shared with white neighbors, and those white neighbors don't cover them.

For a white cell with $t$ triangles: covers $2t$ edges.

Now, consider a white cell. It has 4 edges (or fewer if on boundary). Some are covered by itself, some by black neighbors. If the white cell has $t$ triangles, it covers $2t$ of its edges. The remaining $4 - 2t$ edges (or $e - 2t$ where $e$ is the number of edges of the cell) must be covered by the neighboring black cells.

For an interior white cell with $t$ triangles: $4 - 2t$ edges covered by black neighbors. Since $t \in \{0, 1, 2\}$, we have $4 - 2t \in \{4, 2, 0\}$.

If $t = 0$ (empty): all 4 edges covered by black neighbors. So all 4 black neighbors must cover the shared edge.
If $t = 1$: 2 edges covered by self, 2 by black neighbors.
If $t = 2$: all 4 covered by self, 0 by black neighbors.

Now, a black neighbor covers the shared edge if and only if the black cell covers that edge. A black cell covers all 4 edges if $t = 2$, covers 2 adjacent edges if $t = 1$, covers 0 if $t = 0$.

So for a white cell with $t = 0$: all 4 black neighbors must have $t = 2$ (since they need to cover the shared edge, and the only way to guarantee covering a specific edge is $t = 2$... wait, no, $t = 1$ could also cover it if the triangle's legs include that edge).

Hmm, this is getting complicated because with $t = 1$, we need to know which 2 edges are covered.

Let me try a different approach. Let me consider the case where all cells are either fully covered ($t = 2$) or empty ($t = 0$), with no half-covered cells.

In this case, each cell is either "full" or "empty". A full cell covers all 4 edges, an empty cell covers 0. Each edge is covered exactly once, so for each edge, exactly one adjacent cell is full.

For interior edges: exactly one of the two adjacent cells is full. This means full and empty cells alternate like a chessboard. So the full cells form one part of a bipartition.

For boundary edges: the adjacent cell must be full. So all boundary cells must be full.

But in a chessboard bipartition, boundary cells are in both parts. So we can't have all boundary cells in one part. Contradiction.

So we can't have all cells be full or empty. We need some half-covered cells.

Now, let me think about how to maximize the number of empty cells. We want to minimize the number of non-empty cells (full + half-covered), or equivalently, given $c = a - 100 + (\text{something related to } b)$... 

Wait, let me recompute. We have $c = a - 100$ regardless of $b$? No:

$4a + 2b = 20200 \Rightarrow 2a + b = 10100$
$a + b + c = 10000$
$c = 10000 - a - b = 10000 - a - (10100 - 2a) = a - 100$

So $c = a - 100$ regardless of $b$! To maximize $c$, we maximize $a$, the number of fully covered cells.

So the question becomes: what is the maximum number of fully covered cells $a$?

Constraints:
- $a \leq 5050$ (from $2a \leq 10100$)
- All boundary cells must be non-empty (they must cover their boundary edges).
- The structural constraints about edge coverage.

Let me think about the maximum $a$.

If a cell is fully covered, all its neighbors must be empty (since the fully covered cell covers all shared edges, so neighbors can't cover any shared edge, meaning neighbors cover 0 edges from the shared ones).

Wait, not necessarily. A neighbor could be half-covered, covering 2 edges that don't include the shared edge with the full cell. But a cell has 4 edges. If one is covered by the full neighbor, the cell can cover at most 2 of the remaining 3 edges... but it can only cover 0, 2, or 4. If it covers 2, those 2 must be adjacent. The 3 remaining edges (after 1 is covered by the full neighbor) - can 2 of them be adjacent? 

Let's say the cell has edges N, E, S, W, and the S edge is covered by the full neighbor below. The remaining edges are N, E, W. Can we pick 2 adjacent ones? N and E are adjacent (share a corner), N and W are adjacent, E and W are not adjacent. So yes, we could cover N and E, or N and W. So a half-covered cell can be adjacent to a full cell.

But wait, if the half-covered cell covers N and E, then the N edge is covered by this cell, and the neighbor above must not cover it. And the E edge is covered by this cell, and the neighbor to the right must not cover it. The S edge is covered by the full neighbor below, and W edge must be covered by the neighbor to the left.

So the structure can be more complex than just alternating full/empty.

Let me think about this more carefully using the chessboard coloring.

Let me use the chessboard coloring. Black cells have $(i+j)$ even, white cells have $(i+j)$ odd. 5000 each.

Key insight: Consider an interior edge between a black cell and a white cell. This edge is covered by exactly one of them. Let's say it's covered by the black cell. Then the black cell "claims" this edge.

Now, a black cell that is fully covered claims all 4 of its edges. A black cell that is half-covered claims 2 adjacent edges. A black cell that is empty claims 0 edges.

For a white cell: the edges it doesn't claim are claimed by its black neighbors. 

Let me think about the "claim" pattern. Each black cell claims 0, 2, or 4 of its edges. Each edge is claimed by exactly one of its adjacent cells.

Now, consider a white cell. Its 4 edges are each claimed by either itself or a black neighbor. If the white cell claims $k$ edges ($k \in \{0, 2, 4\}$), then $4 - k$ edges are claimed by black neighbors.

For the white cell to claim 0 edges (be empty): all 4 edges claimed by black neighbors. Each black neighbor must claim the shared edge. A black neighbor claims the shared edge if it's full (claims all 4) or half-covered with a triangle including that edge.

For the white cell to claim 4 edges (be full): no black neighbor claims the shared edge. So each black neighbor must not claim the shared edge. If a black neighbor is empty, it claims nothing - OK. If a black neighbor is half-covered, it claims 2 edges, and the shared edge must not be one of them.

For the white cell to claim 2 edges (be half-covered): 2 edges claimed by self, 2 by black neighbors.

This is quite flexible. Let me think about upper bounds on $a$.

Let me count more carefully. Let $a_B$ = full black cells, $a_W$ = full white cells, $a = a_B + a_W$. Similarly $b_B, b_W$ for half-covered, $c_B, c_W$ for empty.

From the edge counting:
- Black cells claim $2(2a_B + b_B) = 4a_B + 2b_B$ edges total.
- White cells claim $4a_W + 2b_W$ edges total.
- Total: $4a + 2b = 20200$. ✓

Now, consider the boundary. Boundary edges must be claimed by the adjacent cell. Let's count boundary edges claimed by black and white cells.

Let $e_B$ = boundary edges adjacent to black cells, $e_W$ = boundary edges adjacent to white cells. $e_B + e_W = 400$.

By the chessboard coloring, the boundary alternates black and white. The boundary has 400 edges. Going around: the 400 boundary edges alternate between black-adjacent and white-adjacent. So $e_B = e_W = 200$.

Each boundary edge must be claimed by its adjacent cell. So black boundary cells must claim at least their boundary edges, and white boundary cells must claim at least their boundary edges.

A black boundary cell with a boundary edge must claim that edge, so it's either full or half-covered (with a triangle including the boundary edge). It can't be empty.

So all boundary cells are non-empty. There are 396 boundary cells. Among them, 198 black and 198 white.

Now, let me think about the constraint more carefully. 

Consider a full black cell. It claims all 4 edges. Its 4 white neighbors each have one edge (the shared one) claimed by this black cell. So each white neighbor has at most 3 remaining edges to claim (or have claimed by other black neighbors).

If a white neighbor is also full, it would try to claim the shared edge too - contradiction. So a full black cell's neighbors cannot be full. They must be half-covered or empty.

If a white neighbor is empty, all its edges are claimed by black neighbors. The shared edge with our full black cell is claimed by the full black cell. The other 3 edges must be claimed by other black neighbors.

If a white neighbor is half-covered, it claims 2 adjacent edges, none of which is the shared edge with our full black cell. So the 2 claimed edges are among the other 3, and they must be adjacent. The remaining 1 edge is claimed by another black neighbor.

OK this is getting very complex. Let me try to think about it from a higher level.

Let me consider the problem as a flow problem or use a coloring/parity argument.

Alternative approach: Think of the grid as a graph $G$ with vertices = grid points, edges = unit segments. We need to decompose the edges of $G$ into paths of length 2 (each triangle's 2 legs form a path of length 2 in $G$, with the bend at the right-angle vertex). Each such path of length 2 is a "V" shape (two perpendicular edges sharing a vertex).

Wait, actually each triangle's 2 legs form a path of length 2 in the grid graph, where the two edges are perpendicular (they share a vertex and go in perpendicular directions). The hypotenuse is the diagonal, not part of the grid graph.

So we need to decompose all 20200 edges of the grid graph into 10100 paths of length 2, where each path consists of 2 perpendicular edges sharing a vertex.

And additionally, each path must lie within a single cell (the 2 legs and the hypotenuse are all within one cell). So the 2 edges of the path must be 2 adjacent edges of some cell.

This is a constrained path decomposition. Let me think about what configurations are possible.

Each grid point has degree 2, 3, or 4 (corner = 2, edge = 3, interior = 4). In the decomposition, each edge is in exactly one path. At each vertex, the edges incident to it are paired into paths. Each path uses 2 edges at its middle vertex, and 1 edge at each endpoint.

Wait, let me reconsider. A path of length 2 has 3 vertices: start, middle, end. The 2 edges share the middle vertex. At the middle vertex, 2 edges are used. At each endpoint, 1 edge is used.

But in the decomposition, every edge is in exactly one path. So at each vertex $v$ with degree $d$, the $d$ edges incident to $v$ are distributed among paths. Each path that has $v$ as an endpoint uses 1 edge at $v$, and each path that has $v$ as a middle uses 2 edges at $v$.

Let $m_v$ = number of paths with $v$ as middle, $e_v$ = number of paths with $v$ as endpoint. Then $2m_v + e_v = d_v$ (degree of $v$).

Also, the total number of path endpoints = $2 \times 10100 = 20200$ (each path has 2 endpoints). And $\sum_v e_v = 20200$.

And $\sum_v 2m_v = 2 \times 10100 = 20200$ (each path has 1 middle, contributing 2 edges). So $\sum_v m_v = 10100$.

Check: $\sum_v d_v = 2 \times 20200 = 40400$ (each edge contributes 2 to the sum of degrees). And $\sum_v (2m_v + e_v) = 2 \times 10100 + 20200 = 40400$. ✓

Now, at each vertex $v$ with degree $d_v$:
- If $d_v = 2$ (corner): $2m_v + e_v = 2$. Options: $(m_v, e_v) = (0, 2)$ or $(1, 0)$.
  - $(1, 0)$: 1 path with $v$ as middle, using both edges. The 2 edges are perpendicular (corner has 2 perpendicular edges). This is valid - the path forms a right angle at the corner, and it's within the corner cell.
  - $(0, 2)$: 2 paths with $v$ as endpoint. Each uses 1 edge. But then each of these paths has its middle at the other endpoint of the edge. This is also valid.
  
- If $d_v = 3$ (boundary, non-corner): $2m_v + e_v = 3$. Options: $(m_v, e_v) = (0, 3)$ or $(1, 1)$.
  - $(1, 1)$: 1 path with $v$ as middle (using 2 of the 3 edges, must be perpendicular), 1 path with $v$ as endpoint (using the remaining edge).
  - $(0, 3)$: 3 paths with $v$ as endpoint.

- If $d_v = 4$ (interior): $2m_v + e_v = 4$. Options: $(m_v, e_v) = (0, 4), (1, 2), (2, 0)$.
  - $(2, 0)$: 2 paths with $v$ as middle. Each uses 2 perpendicular edges. The 4 edges are split into 2 pairs of perpendicular edges. There are 2 ways: (N+E, S+W) or (N+W, S+E). Each pair is within a different cell.
  - $(1, 2)$: 1 path with $v$ as middle (2 perpendicular edges), 2 paths with $v$ as endpoint.
  - $(0, 4)$: 4 paths with $v$ as endpoint.

Now, the constraint that each path lies within a single cell: the 2 edges of a path (with $v$ as middle) must be 2 adjacent edges of a cell. At an interior vertex, the 4 edges go N, E, S, W. The pairs (N, E) belong to the NE cell, (E, S) to the SE cell, (S, W) to the SW cell, (W, N) to the NW cell. So each path-with-middle at an interior vertex is assigned to one of the 4 adjacent cells.

At a corner vertex (say bottom-left), the 2 edges go E and N. The pair (E, N) belongs to the corner cell.

At a boundary vertex (say on the bottom edge, not corner), the 3 edges go E, W (along the boundary) and N (into the interior). The perpendicular pairs: (E, N) belongs to the cell to the NE, (W, N) belongs to the cell to the NW. (E, W) are collinear, not perpendicular, so can't form a path.

Now, the number of triangles in a cell = number of paths assigned to that cell. A cell can have 0, 1, or 2 paths. If 2 paths, they must be non-overlapping (the 2 triangles don't overlap). The 2 paths in a cell correspond to 2 triangles, and they must not overlap, which means they're on opposite sides of a diagonal.

For a cell with corners at SW, SE, NE, NW:
- Path at SW vertex: edges S and W → triangle in SW corner
- Path at SE vertex: edges S and E → triangle in SE corner
- Path at NE vertex: edges N and E → triangle in NE corner
- Path at NW vertex: edges N and W → triangle in NW corner

Two paths in the same cell don't overlap iff they're on opposite corners (SW+NE or SE+NW), i.e., they share the diagonal.

Two paths on adjacent corners (e.g., SW and SE) would overlap (they share the bottom edge region... actually, do they? The SW triangle occupies the lower-left half below the SW-NE diagonal, and the SE triangle occupies the lower-right half below the SE-NW diagonal. These do overlap in the lower part of the cell).

So a cell with 2 paths must have them on opposite corners (sharing a diagonal). A cell with 2 paths on adjacent corners is invalid.

Now, let me think about the problem in terms of the vertex decomposition.

At each vertex $v$, we choose how to pair the edges into paths (with $v$ as middle) and leave some as path endpoints. The constraint is:
1. Each edge is in exactly one path (globally consistent).
2. Each cell has 0, 1, or 2 paths, and if 2, they're on opposite corners.

The edge consistency means: if edge $e = (u, v)$ is part of a path with middle $u$, then $v$ is an endpoint of that path, so $e$ is an endpoint-edge at $v$. If $e$ is part of a path with middle $v$, then $u$ is an endpoint. If $e$ is part of a path with middle at some other vertex... no, a path of length 2 has its middle at one of the 3 vertices. The edge $(u,v)$ could have its path's middle at $u$ (then $v$ is an endpoint), or at $v$ (then $u$ is an endpoint), or the path could be $(w, u, v)$ with middle $u$... wait, no. A path of length 2 is $(a, b, c)$ with edges $(a,b)$ and $(b,c)$. The middle is $b$. So edge $(a,b)$ has middle $b$, and edge $(b,c)$ has middle $b$. 

So for edge $(u, v)$: either $u$ is the middle (and $v$ is an endpoint, and the other edge of the path is some edge $(u, w)$ perpendicular to $(u,v)$), or $v$ is the middle (and $u$ is an endpoint, and the other edge is $(v, w)$ perpendicular to $(u,v)$).

So each edge is "owned" by one of its endpoints (the middle of its path). At each vertex, the edges it owns are paired into perpendicular pairs (paths with this vertex as middle).

So the problem reduces to: orient each edge to one of its endpoints (the "middle"), such that at each vertex, the edges oriented towards it can be paired into perpendicular pairs. And the cell constraint: each cell has 0, 1, or 2 paths, and if 2, on opposite corners.

Wait, but "oriented towards" the middle means the edge is owned by the middle vertex. Let me rephrase: each edge is assigned to one of its 2 endpoints. At each vertex, the assigned edges must be pairable into perpendicular pairs (each pair forms a right angle at the vertex).

At a vertex with $d$ edges assigned to it: $d$ must be even (since they're paired), and the pairs must be perpendicular. At an interior vertex with 4 edges, if all 4 are assigned, they must pair into 2 perpendicular pairs (2 ways: (N,E)+(S,W) or (N,W)+(S,E)). If 2 are assigned, they must be perpendicular. If 0, fine.

At a corner with 2 edges: if both assigned, they're perpendicular (always the case at a corner). If 0, fine.

At a boundary vertex with 3 edges: the assigned edges must be even, so 0 or 2. If 2, they must be perpendicular. The 3 edges are, say, E, W, N. Perpendicular pairs: (E, N) or (W, N). (E, W) is not perpendicular. So if 2 are assigned, one must be N and the other E or W.

Now, each edge is assigned to one endpoint. So if edge $(u,v)$ is assigned to $u$, then $v$ doesn't get this edge. The total assigned edges at $v$ = edges assigned to $v$ from all its neighbors.

Let me denote the assignment as a function on edges. For each edge $e = (u,v)$, $\text{owner}(e) \in \{u, v\}$.

At each vertex $v$: the edges owned by $v$ must be pairable into perpendicular pairs.

Now, the cell constraint: each path (pair of perpendicular edges at a vertex) belongs to a cell (the cell in the quadrant of the perpendicular pair). Each cell can have 0, 1, or 2 paths, and if 2, on opposite corners.

Let me count. The total number of paths = total edges / 2 = 10100. Each path is at a vertex and belongs to a cell. The number of paths = $\sum_v m_v$ where $m_v$ = number of pairs at $v$ = (edges owned by $v$) / 2.

We want to maximize empty cells = cells with 0 paths. Equivalently, minimize cells with ≥1 path. But we also have the constraint that cells with 2 paths must have them on opposite corners.

Hmm, let me think about this differently. Let me consider the number of paths per cell. If a cell has 2 paths (on opposite corners), it contributes 2 to the path count. If 1, contributes 1. If 0, contributes 0. Total = 10100.

$c = 10000 - a - b$ where $a$ = cells with 2 paths, $b$ = cells with 1 path. $2a + b = 10100$, $a + b + c = 10000$, $c = a - 100$.

Maximize $a$ = maximize cells with 2 paths on opposite corners.

Now, let me think about the vertex assignment problem. At each interior vertex, 4 edges meet. The vertex can own 0, 2, or 4 of them. If it owns 4, it creates 2 paths (in 2 different cells, on opposite corners of the respective cells... wait, no. At an interior vertex, the 4 edges go N, E, S, W. The 2 pairings:
- (N, E) + (S, W): (N,E) is in the NE cell, (S,W) is in the SW cell. These are opposite cells (diagonally opposite).
- (N, W) + (S, E): (N,W) is in the NW cell, (S,E) is in the SE cell. These are also diagonally opposite.

So if a vertex owns all 4 edges, it creates 2 paths in 2 diagonally opposite cells. Each of those cells gets 1 path from this vertex.

If a vertex owns 2 edges (a perpendicular pair), it creates 1 path in 1 cell.

If a vertex owns 0 edges, it creates 0 paths.

Now, for a cell to have 2 paths (on opposite corners), it needs 2 vertices (opposite corners of the cell) to each own the 2 edges of the cell at that corner. 

For a cell with corners SW, SE, NE, NW:
- 2 paths on SW and NE corners: SW vertex owns (S, W) edges of this cell, NE vertex owns (N, E) edges.
- 2 paths on SE and NW corners: SE vertex owns (S, E) edges, NW vertex owns (N, W) edges.

For a cell to have 2 paths, 2 of its 4 corner vertices must each own the 2 cell-edges at that corner, and those 2 vertices must be diagonally opposite.

Now, each vertex is shared by 4 cells (or 2 for boundary, 1 for corner). If a vertex owns all 4 of its edges, it contributes 1 path to each of 2 diagonally opposite cells. If it owns 2 edges, it contributes 1 path to 1 cell.

Let me think about what happens at an interior vertex. It has 4 edges: N, E, S, W. Each edge is shared with a neighbor vertex. The edge is owned by either this vertex or the neighbor.

If the vertex owns all 4 edges: it creates paths in 2 diagonally opposite cells. The 4 neighbor vertices each lose 1 edge (they don't own the shared edge).

If the vertex owns 2 edges (say N and E): it creates a path in the NE cell. The N-neighbor and E-neighbor each lose 1 edge. The S and W edges are owned by the S-neighbor and W-neighbor respectively.

If the vertex owns 0 edges: all 4 edges are owned by the 4 neighbors.

Now, the constraint at each vertex: the owned edges must be pairable into perpendicular pairs. So the owned set must be:
- 0 edges: OK
- 2 perpendicular edges: OK
- 4 edges: OK (pairable in 2 ways)
- 2 collinear edges (e.g., N and S): NOT OK
- 1 or 3 edges: NOT OK (odd)

So at each vertex, the owned edges are 0, 2-perpendicular, or 4.

Now, let's think about this as an orientation problem on the grid graph. Each edge is oriented towards its owner. At each vertex, the in-edges (owned edges) must form 0, a perpendicular pair, or 2 perpendicular pairs.

Let me think about the degree constraints. At an interior vertex with 4 edges:
- Owns 4: all edges oriented in. All 4 neighbors have this edge oriented away.
- Owns 2 perpendicular: 2 edges oriented in, 2 oriented out.
- Owns 0: all edges oriented out. All 4 neighbors have this edge oriented in.

At a boundary vertex (degree 3, say on bottom edge with edges E, W, N):
- Owns 2 perpendicular: must include N and one of E/W. So (N, E) or (N, W). The remaining edge (W or E) is oriented out.
- Owns 0: all 3 edges oriented out. But then the 3 neighbors each get 1 edge oriented in.

Wait, but at a boundary vertex, the edges E and W go to boundary-adjacent vertices, and N goes to an interior vertex. If the boundary vertex owns 0, then E is owned by the E-neighbor, W by the W-neighbor, N by the N-neighbor.

At a corner vertex (degree 2, edges E and N):
- Owns 2: both edges, which are perpendicular. OK.
- Owns 0: both edges oriented out.

Now, let me think about the total number of paths. Each vertex owning $k$ edges creates $k/2$ paths. Total paths = $\sum_v k_v/2 = 10100$ where $k_v$ = edges owned by $v$. And $\sum_v k_v = 20200$ (total edges). ✓

Now, each path belongs to a cell. A cell with 2 paths (on opposite corners) is "full". We want to maximize the number of full cells.

A cell is full iff 2 of its diagonally opposite corner vertices each own the 2 cell-edges at that corner.

Let me think about what prevents a cell from being full. A cell's corner vertex owns the 2 cell-edges at that corner only if both those edges are oriented towards the vertex. If even one of the 2 edges is oriented away (owned by the other endpoint), the vertex doesn't own the pair, and the cell doesn't get a path from this corner.

So for a cell to be full, we need 2 diagonally opposite vertices to each own both cell-edges at their corner. This means:
- For the SW corner: the S and W edges of the cell are owned by the SW vertex.
- For the NE corner: the N and E edges of the cell are owned by the NE vertex.
(Or similarly for SE and NW.)

The S edge of the cell is the edge between SW and SE vertices. For SW to own it, it must be oriented towards SW (away from SE).
The W edge is between SW and NW. For SW to own it, oriented towards SW (away from NW).
The N edge is between NW and NE. For NE to own it, oriented towards NE (away from NW).
The E edge is between SE and NE. For NE to own it, oriented towards NE (away from SE).

So for the SW-NE diagonal full cell:
- S edge: SW ← SE (oriented towards SW)
- W edge: SW ← NW (oriented towards SW)
- N edge: NE ← NW (oriented towards NE)
- E edge: NE ← SE (oriented towards NE)

The SE vertex: both S and E edges are oriented away from SE (towards SW and NE respectively). So SE owns neither of these. SE might own its other 2 edges (the ones going further E and further S, if they exist).

The NW vertex: both N and W edges are oriented away from NW (towards NE and SW). So NW owns neither. NW might own its other 2 edges.

Now, for the SE-NW diagonal full cell:
- S edge: SE ← SW (oriented towards SE)
- E edge: SE ← NE (oriented towards SE)
- N edge: NW ← NE (oriented towards NW)
- W edge: NW ← SW (oriented towards NW)

Notice the contrast: for SW-NE full, S edge is oriented towards SW; for SE-NW full, S edge is oriented towards SE. These are opposite orientations.

So two adjacent cells sharing an edge: if one is full (SW-NE) and the other is full (SE-NW), the shared edge would need to be oriented both ways - contradiction. So two adjacent cells can't both be full if they require opposite orientations of the shared edge.

Let me check: two horizontally adjacent cells, left cell and right cell, sharing the E edge of the left cell = W edge of the right cell.

Left cell full (SW-NE): E edge oriented towards NE of left cell.
Right cell full (SW-NE): W edge oriented towards SW of right cell.

NE of left cell and SW of right cell are the same vertex? No. Left cell has corners at $(i,j), (i+1,j), (i+1,j+1), (i,j+1)$ (using grid coordinates). Right cell has corners at $(i+1,j), (i+2,j), (i+2,j+1), (i+1,j+1)$. The shared edge is from $(i+1,j)$ to $(i+1,j+1)$.

For left cell SW-NE full: NE of left = $(i,j+1)$... wait, let me use a clearer notation.

Let me use cell $(i,j)$ with $0 \le i,j \le 99$, with corners at grid points $(i,j), (i+1,j), (i+1,j+1), (i,j+1)$. SW = $(i,j)$, SE = $(i+1,j)$, NE = $(i+1,j+1)$, NW = $(i,j+1)$.

For cell $(i,j)$ full on SW-NE diagonal:
- Edge from $(i,j)$ to $(i+1,j)$ (S edge, bottom): owned by $(i,j)$ (SW).
- Edge from $(i,j)$ to $(i,j+1)$ (W edge, left): owned by $(i,j)$ (SW).
- Edge from $(i,j+1)$ to $(i+1,j+1)$ (N edge, top): owned by $(i+1,j+1)$ (NE).
- Edge from $(i+1,j)$ to $(i+1,j+1)$ (E edge, right): owned by $(i+1,j+1)$ (NE).

For cell $(i,j)$ full on SE-NW diagonal:
- S edge: owned by $(i+1,j)$ (SE).
- E edge: owned by $(i+1,j)$ (SE).
- N edge: owned by $(i,j+1)$ (NW).
- W edge: owned by $(i,j+1)$ (NW).

Now consider two horizontally adjacent cells: $(i,j)$ and $(i+1,j)$. Shared edge: from $(i+1,j)$ to $(i+1,j+1)$ (E edge of cell $(i,j)$, W edge of cell $(i+1,j)$).

Case 1: Cell $(i,j)$ full on SW-NE. E edge owned by $(i+1,j+1)$.
Case 2: Cell $(i+1,j)$ full on SW-NE. W edge owned by $(i+1,j)$.

These are different vertices, so the edge would need to be owned by both $(i+1,j+1)$ and $(i+1,j)$ - contradiction. So both can't be full on SW-NE.

Case 1: Cell $(i,j)$ full on SW-NE. E edge owned by $(i+1,j+1)$.
Case 3: Cell $(i+1,j)$ full on SE-NW. W edge owned by $(i+2,j+1)$ (NW of cell $(i+1,j)$).

$(i+1,j+1)$ and $(i+2,j+1)$ are different vertices, so again contradiction.

Case 4: Cell $(i,j)$ full on SE-NW. E edge owned by $(i+1,j)$ (SE).
Case 2: Cell $(i+1,j)$ full on SW-NE. W edge owned by $(i+1,j)$ (SW).

Both owned by $(i+1,j)$! So this is compatible! Cell $(i,j)$ full on SE-NW and cell $(i+1,j)$ full on SW-NE: the shared edge is owned by $(i+1,j)$, which is SE of cell $(i,j)$ and SW of cell $(i+1,j)$.

But wait, $(i+1,j)$ owns the E edge of cell $(i,j)$ (which is the edge from $(i+1,j)$ to $(i+1,j+1)$) and the W edge of cell $(i+1,j)$ (which is the same edge!). So $(i+1,j)$ owns this edge, and it's part of the SE triangle of cell $(i,j)$ and the SW triangle of cell $(i+1,j)$.

For the SE triangle of cell $(i,j)$: $(i+1,j)$ owns the S edge (from $(i,j)$ to $(i+1,j)$) and E edge (from $(i+1,j)$ to $(i+1,j+1)$). These are perpendicular at $(i+1,j)$. ✓

For the SW triangle of cell $(i+1,j)$: $(i+1,j)$ owns the W edge (from $(i+1,j)$ to $(i+1,j+1)$) and S edge (from $(i+1,j)$ to $(i+2,j)$). These are perpendicular at $(i+1,j)$. ✓

So $(i+1,j)$ owns 3 edges: S edge of cell $(i,j)$ (from $(i,j)$ to $(i+1,j)$), shared edge (from $(i+1,j)$ to $(i+1,j+1)$), and S edge of cell $(i+1,j)$ (from $(i+1,j)$ to $(i+2,j)$). That's 3 edges, which is odd - not allowed! A vertex must own 0, 2, or 4 edges.

Hmm, so this doesn't work. Let me recheck.

$(i+1,j)$ is a grid point. Its edges are:
- To $(i,j)$: West
- To $(i+2,j)$: East
- To $(i+1,j-1)$: South (if $j > 0$)
- To $(i+1,j+1)$: North

For cell $(i,j)$ full on SE-NW: SE = $(i+1,j)$ owns S edge (from $(i,j)$ to $(i+1,j)$, which is the West edge of $(i+1,j)$) and E edge (from $(i+1,j)$ to $(i+1,j+1)$, which is the North edge of $(i+1,j)$).

For cell $(i+1,j)$ full on SW-NE: SW = $(i+1,j)$ owns S edge (from $(i+1,j)$ to $(i+2,j)$, which is the East edge of $(i+1,j)$) and W edge (from $(i+1,j)$ to $(i+1,j+1)$, which is the North edge of $(i+1,j)$).

So $(i+1,j)$ owns: West, North, East. That's 3 edges. Not allowed (must be even).

So this configuration doesn't work either. The issue is that the shared edge is owned by one vertex, and that vertex also needs to own another edge for each cell, leading to 3 owned edges.

Let me reconsider. Maybe two adjacent cells can't both be full at all?

Let me check all 4 combinations for two horizontally adjacent cells $(i,j)$ and $(i+1,j)$:

Shared edge: from $(i+1,j)$ to $(i+1,j+1)$.

Cell $(i,j)$ full on SW-NE: shared edge owned by NE = $(i+1,j+1)$.
Cell $(i,j)$ full on SE-NW: shared edge owned by SE = $(i+1,j)$.

Cell $(i+1,j)$ full on SW-NE: shared edge owned by SW = $(i+1,j)$.
Cell $(i+1,j)$ full on SE-NW: shared edge owned by NW = $(i+1,j+1)$.

Combinations:
1. $(i,j)$ SW-NE + $(i+1,j)$ SW-NE: shared edge owned by $(i+1,j+1)$ and $(i+1,j)$. Contradiction.
2. $(i,j)$ SW-NE + $(i+1,j)$ SE-NW: shared edge owned by $(i+1,j+1)$ (both). Compatible! But check the other edges.
3. $(i,j)$ SE-NW + $(i+1,j)$ SW-NE: shared edge owned by $(i+1,j)$ (both). Compatible! But check other edges.
4. $(i,j)$ SE-NW + $(i+1,j)$ SE-NW: shared edge owned by $(i+1,j)$ and $(i+1,j+1)$. Contradiction.

So combinations 2 and 3 are potentially compatible. Let me check combination 2 in detail.

Cell $(i,j)$ full on SW-NE:
- S edge (from $(i,j)$ to $(i+1,j)$): owned by SW = $(i,j)$.
- W edge (from $(i,j)$ to $(i,j+1)$): owned by SW = $(i,j)$.
- N edge (from $(i,j+1)$ to $(i+1,j+1)$): owned by NE = $(i+1,j+1)$.
- E edge (shared, from $(i+1,j)$ to $(i+1,j+1)$): owned by NE = $(i+1,j+1)$.

Cell $(i+1,j)$ full on SE-NW:
- S edge (from $(i+1,j)$ to $(i+2,j)$): owned by SE = $(i+2,j)$.
- E edge (from $(i+2,j)$ to $(i+2,j+1)$): owned by SE = $(i+2,j)$.
- N edge (from $(i+1,j+1)$ to $(i+2,j+1)$): owned by NW = $(i+1,j+1)$.
- W edge (shared, from $(i+1,j)$ to $(i+1,j+1)$): owned by NW = $(i+1,j+1)$.

So the shared edge is owned by $(i+1,j+1)$ in both cases. ✓

Now, what does $(i+1,j+1)$ own? From cell $(i,j)$: N edge (from $(i,j+1)$ to $(i+1,j+1)$) and E edge (from $(i+1,j)$ to $(i+1,j+1)$). From cell $(i+1,j)$: N edge (from $(i+1,j+1)$ to $(i+2,j+1)$) and W edge (from $(i+1,j)$ to $(i+1,j+1)$).

Wait, the E edge of cell $(i,j)$ and the W edge of cell $(i+1,j)$ are the same edge (the shared edge). So $(i+1,j+1)$ owns:
- From cell $(i,j)$: N edge = $(i,j+1)$ to $(i+1,j+1)$ (this is the edge going West from $(i+1,j+1)$), and E edge = $(i+1,j)$ to $(i+1,j+1)$ (this is the edge going South from $(i+1,j+1)$).
- From cell $(i+1,j)$: N edge = $(i+1,j+1)$ to $(i+2,j+1)$ (edge going East from $(i+1,j+1)$), and W edge = $(i+1,j)$ to $(i+1,j+1)$ (edge going South, same as E edge of cell $(i,j)$).

So the edges owned by $(i+1,j+1)$: West (to $(i,j+1)$), South (to $(i+1,j)$), East (to $(i+2,j+1)$). That's 3 edges again! The South edge is shared between the two cells.

The issue is that $(i+1,j+1)$ is the NE corner of cell $(i,j)$ and the NW corner of cell $(i+1,j)$. The shared edge goes South from $(i+1,j+1)$. This edge is counted once but is part of both cells' triangles. So $(i+1,j+1)$ owns: West, South, East = 3 edges. Not allowed.

So combination 2 also doesn't work because the vertex at the shared edge's endpoint owns 3 edges.

Hmm, so it seems like two adjacent cells can never both be full. Let me verify this more carefully.

Two horizontally adjacent cells share an edge. The edge has 2 endpoints. For both cells to be full, the shared edge must be owned by one endpoint (say the top one). That endpoint is a corner of both cells. For one cell, it's the NE or NW corner; for the other, it's the NW or NE corner. In either case, that vertex owns the shared edge plus one more edge from each cell. The two "more edges" are different (one goes left, one goes right), so the vertex owns 3 edges total. Not allowed.

Similarly for vertically adjacent cells. So two adjacent cells can never both be full.

This means the full cells form an independent set in the cell adjacency graph! The 100×100 grid graph has maximum independent set = 5000 (the chessboard coloring).

But wait, we also have the boundary constraint. All boundary cells must be non-empty. If a boundary cell is not full, it must be half-covered (1 triangle). And we showed $c = a - 100$, so we want to maximize $a$.

If full cells form an independent set, then $a \leq 5000$. But can we achieve $a = 5000$ with all the other constraints?

If $a = 5000$, then $c = 4900$ and $b = 10100 - 2 \times 5000 = 100$. So 100 half-covered cells and 4900 empty cells.

The 5000 full cells form a maximum independent set, which is one color class of the chessboard coloring. Say all black cells are full. Then all white cells are either half-covered or empty. There are 5000 white cells, of which 100 are half-covered and 4900 are empty.

But we need all boundary cells to be non-empty. The boundary has 198 white cells, all of which must be non-empty (half-covered, since they can't be full if full cells are the black cells). So we need at least 198 half-covered white cells. But we only have 100 half-covered cells. Contradiction!

So $a = 5000$ is not achievable. We need more half-covered cells.

Let me reconsider. The boundary has 396 cells, 198 black and 198 white. If all black cells are full, the 198 white boundary cells must be half-covered. So $b \geq 198$. Then $a = (10100 - b)/2 \leq (10100 - 198)/2 = 9902/2 = 4951$. And $c = a - 100 \leq 4851$.

But wait, we also need to check that the 198 white boundary cells being half-covered is consistent with the edge ownership constraints. And there might be additional constraints from the interior.

Hmm, but actually I need to be more careful. The full cells don't have to be exactly one chessboard color. They just need to form an independent set. And the half-covered cells can be of either color.

Let me reconsider. Let me not assume the full cells are one chessboard color. Let me think about this more generally.

We have:
- Full cells form an independent set (no two adjacent).
- All boundary cells are non-empty (full or half-covered).
- $c = a - 100$, $b = 10100 - 2a$.
- Maximize $a$ (equivalently maximize $c$).

Constraints:
1. Full cells form an independent set: $a \leq 5000$.
2. All 396 boundary cells are non-empty.
3. Edge ownership constraints must be satisfiable.

From constraint 2: the boundary cells that are not full must be half-covered. If $a_B$ of the boundary cells are full, then $396 - a_B$ boundary cells are half-covered. So $b \geq 396 - a_B$.

Also, $b = 10100 - 2a$, so $10100 - 2a \geq 396 - a_B$, i.e., $a_B \geq 2a - 9704$.

Since $a_B \leq 396$ (at most all boundary cells are full), we need $2a - 9704 \leq 396$, i.e., $a \leq 5050$. Not very restrictive.

But also $a_B \leq a$ (obviously), and $a_B \leq 396$.

The binding constraint is $a \leq 5000$ (independent set). But we also need $b \geq 198$ (at least the boundary cells of the non-full color must be half-covered, assuming the full cells are one color).

Actually, let me think more carefully. The full cells form an independent set, but not necessarily a complete color class. Some cells of the "full color" might be half-covered or empty, and some cells of the "other color" might be... wait, can a cell of the "other color" be full?

If full cells form an independent set, and the grid is bipartite with parts $X$ (black) and $Y$ (white), then the full cells are a subset of $X$ or a subset of $Y$ or a mix. But if a full cell is in $X$ and another in $Y$, they might be adjacent (since $X$ and $Y$ are the two parts, any edge connects an $X$ cell to a $Y$ cell). Two full cells in different parts could be adjacent. So the independent set constraint means no two full cells are adjacent, regardless of color.

The maximum independent set in a 100×100 grid is 5000 (one color class). But we could have a smaller independent set that includes cells from both colors.

Now, the key question: given the independent set constraint and the boundary constraint, what's the maximum $a$?

Let me think about it differently. We need:
- $a$ full cells (independent set)
- $b = 10100 - 2a$ half-covered cells
- $c = a - 100$ empty cells
- All 396 boundary cells are in $\{$full $\cup$ half-covered$\}$
- The edge ownership constraints are satisfiable.

The boundary constraint: $b \geq 396 - a_B$ where $a_B$ = full boundary cells. Since $a_B \leq \min(a, 396)$, we need $b \geq 396 - \min(a, 396)$. If $a \geq 396$, then $b \geq 0$, which is always true. But we also need the boundary cells of the non-full color to be half-covered.

Hmm wait, I think I need to be more careful. Let me reconsider whether the independent set constraint is the only constraint on full cells, or whether there are additional constraints from the edge ownership.

Let me re-examine. I showed that two adjacent cells can't both be full because the shared edge's endpoint would own 3 edges. But are there other constraints?

Consider a full cell and a half-covered neighbor. The full cell covers all 4 of its edges. The half-covered neighbor covers 2 of its edges, which must not include the shared edge (since the full cell already covers it). So the half-covered cell's 2 covered edges are the 2 edges not shared with the full cell. But the half-covered cell has 4 edges, one shared with the full cell. The remaining 3 edges: the half-covered cell covers 2 of them (adjacent pair). The 3rd edge must be covered by its other neighbor.

Wait, but the 3 remaining edges: one is opposite to the shared edge, and two are adjacent to the shared edge. The 2 adjacent ones share a corner with the shared edge. The opposite one doesn't share a corner with the shared edge.

For the half-covered cell to cover 2 adjacent edges from the remaining 3: the 2 adjacent edges must share a corner. Among the 3 remaining edges (say N, E, S if the shared edge is W): N and E share a corner, E and S share a corner, N and S don't. So the half-covered cell can cover (N, E) or (E, S). In either case, the E edge is covered. The remaining edge (S or N) must be covered by its neighbor.

So a full cell with a half-covered neighbor is possible, but the half-covered cell's triangle must not include the shared edge, and the specific pair of edges covered depends on the geometry.

This seems like it could work. Let me think about whether we can achieve $a$ close to 5000.

Let me consider the chessboard coloring with black cells full. Then:
- All 5000 black cells are full.
- White cells: 198 boundary cells must be half-covered, the rest (4802) can be empty.
- $b = 198$, $a = 5000$, $c = 4900$.

Check: $2a + b = 10000 + 198 = 10198 \neq 10100$. That's wrong!

Wait, $2a + b = 10100$. If $a = 5000$, $b = 10100 - 10000 = 100$. But we need $b \geq 198$ for the boundary. Contradiction. So $a = 5000$ doesn't work.

With $b = 198$: $a = (10100 - 198)/2 = 4951$. $c = 4951 - 100 = 4851$.

But can we achieve $a = 4951$ with $b = 198$? We need 4951 full cells (independent set) and 198 half-covered cells (all on the boundary), and 4851 empty cells.

The 4951 full cells form an independent set. The 198 half-covered cells are boundary cells. The 4851 empty cells are the rest.

Total: 4951 + 198 + 4851 = 10000. ✓

Now, the 198 half-covered boundary cells must be of the "non-full" color (if the full cells are one color). But we have 5000 cells of each color. If full cells are black: 4951 black cells are full, 49 black cells are... not full. These 49 black cells could be empty or half-covered. But the 198 half-covered cells are white boundary cells. So 49 black cells are empty, and 4802 white cells are empty (5000 - 198 = 4802). Total empty = 49 + 4802 = 4851. ✓

But wait, the 49 non-full black cells: are they on the boundary? The boundary has 198 black cells. If 49 black cells are not full, and they're on the boundary, then 198 - 49 = 149 black boundary cells are full. But boundary cells must be non-empty. So the 49 non-full black boundary cells must be half-covered. Then $b \geq 198 + 49 = 247$, not 198.

Hmm, I think I need to be more careful. Let me reconsider.

The boundary has 396 cells: 198 black, 198 white. All must be non-empty. If full cells are all black, then:
- Black boundary cells: can be full or half-covered.
- White boundary cells: must be half-covered (can't be full if only black cells are full).

So all 198 white boundary cells are half-covered. The black boundary cells: some are full, some might be half-covered (if they're not in the independent set).

If $a$ black cells are full (including some boundary and some interior), and the remaining $5000 - a$ black cells are empty, then the $5000 - a$ non-full black cells include some boundary cells. Those boundary cells must be half-covered.

Let $a_{BB}$ = full black boundary cells, $a_{BI}$ = full black interior cells. $a = a_{BB} + a_{BI}$.
Non-full black boundary cells = $198 - a_{BB}$, which must be half-covered.
Non-full white boundary cells = 198 (all white boundary cells), which must be half-covered.
Total half-covered: $b = (198 - a_{BB}) + 198 = 396 - a_{BB}$.

Also, $b = 10100 - 2a$. So $396 - a_{BB} = 10100 - 2a$, giving $a_{BB} = 2a - 9704$.

Since $a_{BB} \geq 0$: $a \geq 4852$.
Since $a_{BB} \leq 198$: $2a - 9704 \leq 198$, so $a \leq 4951$.
Since $a_{BB} \leq a$: always satisfied for $a \leq 4951$.
Since $a \leq 5000$ (independent set): $a \leq 5000$, but the binding constraint is $a \leq 4951$.

Also, $a_{BI} = a - a_{BB} = a - (2a - 9704) = 9704 - a$. Since $a_{BI} \geq 0$: $a \leq 9704$, always satisfied.
Since $a_{BI} \leq 4802$ (interior black cells = 5000 - 198 = 4802): $9704 - a \leq 4802$, so $a \geq 4902$.

So combining: $4902 \leq a \leq 4951$, and $c = a - 100$, so $4802 \leq c \leq 4851$.

But this assumes all full cells are black. What if we allow full cells of both colors?

If we allow full cells of both colors, the independent set constraint still applies (no two adjacent full cells). The maximum independent set is 5000, but we might be able to include more boundary cells in the independent set by mixing colors.

Actually, the issue is that the boundary has both black and white cells, and all boundary cells must be non-empty. If a boundary cell is full, it doesn't need to be half-covered. So we want to maximize the number of full boundary cells to minimize $b$.

But the independent set constraint limits how many boundary cells can be full. On the boundary, adjacent boundary cells are adjacent in the grid, so they can't both be full. The boundary forms a cycle of 396 cells, and the maximum independent set on a cycle of 396 is 198.

So at most 198 boundary cells can be full. This gives $a_{BB} + a_{WB} \leq 198$ (where $a_{WB}$ = full white boundary cells, but we assumed all full cells are black, so $a_{WB} = 0$).

Wait, I was assuming all full cells are one color. Let me relax this.

Let me not assume full cells are one color. Let $a$ = total full cells, $b$ = total half-covered, $c$ = total empty. $c = a - 100$, $b = 10100 - 2a$.

Boundary: 396 cells, all non-empty. Let $a_{bd}$ = full boundary cells, $b_{bd}$ = half-covered boundary cells. $a_{bd} + b_{bd} = 396$, $b_{bd} = 396 - a_{bd}$.

Since full cells form an independent set, and boundary cells form a cycle of 396, $a_{bd} \leq 198$.

$b \geq b_{bd} = 396 - a_{bd} \geq 396 - 198 = 198$.

So $b \geq 198$, giving $a \leq (10100 - 198)/2 = 4951$, $c \leq 4851$.

But is $a = 4951$ achievable? We need to check all constraints, not just the counting.

With $a = 4951$, $b = 198$, $c = 4851$. All 198 half-covered cells are on the boundary, and 198 boundary cells are full. The 4951 full cells form an independent set with 198 on the boundary and 4753 in the interior.

The interior has 9604 cells. 4753 full + 4851 empty = 9604. ✓

Now, the 4753 full interior cells form an independent set in the interior grid. The interior grid is 98×98 = 9604 cells. Maximum independent set = 4802. So 4753 ≤ 4802. ✓

But we also need the full cells (boundary + interior) to form an independent set in the full 100×100 grid. The 198 full boundary cells and 4753 full interior cells must have no two adjacent.

On the boundary, 198 out of 396 cells are full, forming an independent set on the boundary cycle. This is a maximum independent set on the cycle, so every other boundary cell is full.

Now, the interior cells adjacent to full boundary cells can't be full. Each full boundary cell has 1 interior neighbor (for edge cells) or 0 (for corner cells, which have 2 boundary neighbors and 0 interior neighbors... wait, corner cells have 2 neighbors, both on the boundary).

Actually, a corner cell has 2 neighbors: one horizontal and one vertical, both on the boundary. So corner cells have 0 interior neighbors.

An edge (non-corner) boundary cell has 3 neighbors: 2 on the boundary and 1 interior. So each full edge boundary cell blocks 1 interior cell from being full.

There are 198 full boundary cells. How many are corners? The 4 corners: in a maximum independent set on the boundary cycle of 396, we can choose whether corners are included or not. Let me think about this.

The boundary cycle has 396 cells. A maximum independent set has 198 cells. The corners are at positions that are 99 apart on the cycle (since each side has 100 cells, and the corner is shared between two sides). Actually, let me index the boundary cells. Going around: 100 on top, 100 on right, 100 on bottom, 100 on left, minus 4 corners counted twice = 396.

The cycle has 396 vertices. Maximum independent set = 198. We can choose any maximum independent set. The question is how many interior cells are blocked.

Each full boundary cell that is a non-corner edge cell blocks 1 interior neighbor. Corner cells block 0 interior neighbors. So the number of blocked interior cells = (number of full non-corner boundary cells) = 198 - (number of full corner cells).

To minimize blocked interior cells, maximize full corner cells. Can all 4 corners be in the independent set? The corners are at positions 0, 99, 198, 297 on the cycle (if we go around starting from a corner). The distance between consecutive corners is 99. In an independent set on a cycle, no two adjacent vertices. The corners at positions 0 and 99: are they adjacent? Position 0 and position 1 are adjacent, position 0 and 395 are adjacent. Position 99 and 100 are adjacent, position 99 and 98 are adjacent. So positions 0 and 99 are not adjacent (distance 99). So all 4 corners can be in the independent set.

If all 4 corners are full, then 198 - 4 = 194 full non-corner boundary cells, blocking 194 interior cells.

The interior grid is 98×98. The 194 blocked interior cells are adjacent to full boundary cells. The remaining 9604 - 194 = 9410 interior cells are available for full/empty. We need 4753 full interior cells from these 9410, forming an independent set (along with the boundary full cells).

But the 194 blocked interior cells are not available for full. So we need an independent set of size 4753 in the interior grid minus the 194 blocked cells. The interior grid (98×98) has maximum independent set 4802. Removing 194 cells: the maximum independent set in the remaining graph is at most 4802, but could be less depending on which cells are removed.

Actually, the 194 blocked cells are specific cells: those adjacent to full non-corner boundary cells. These are the cells in the "second row" from the boundary, adjacent to full boundary cells.

Hmm, this is getting complicated. Let me think about whether $a = 4951$ is actually achievable by trying to construct a configuration.

Let me try the chessboard coloring approach. Color the 100×100 grid like a chessboard. Say cell $(i,j)$ is black if $i+j$ is even, white if odd. 5000 black, 5000 white.

Make all black cells full. Then all white cells must be empty or half-covered. Each white cell has all 4 edges covered by its black neighbors (since black neighbors are full). So white cells can be empty. But white boundary cells have boundary edges that must be covered by themselves (not by a black neighbor, since the boundary edge has no neighbor on the other side). Wait, the boundary edge of a white boundary cell: is it covered by the white cell or by a black neighbor?

A boundary edge is adjacent to only 1 cell. If that cell is white, the white cell must cover it. But if the white cell is empty, it covers nothing. So the white boundary cell must be half-covered (at least).

But if a white boundary cell is half-covered, it covers 2 adjacent edges. One is the boundary edge, the other is an interior edge. That interior edge was supposed to be covered by the adjacent black cell (which is full and covers all 4 edges). Now it's covered by the white cell too - double coverage! Contradiction.

So making all black cells full and all white cells empty doesn't work for white boundary cells. The white boundary cell can't be empty (boundary edge uncovered) and can't be half-covered (double coverage with black neighbor).

This means we can't simply make all cells of one color full. We need a more nuanced approach.

Let me reconsider. The issue is that a full cell covers all 4 edges, including edges shared with neighbors. If a neighbor is half-covered, the half-covered cell's covered edges must not include any edge shared with the full cell. But for a boundary cell, the boundary edge must be covered, and the boundary edge is not shared with any full cell. So the half-covered boundary cell must cover the boundary edge and one adjacent interior edge. But that interior edge is shared with a full neighbor, causing double coverage.

So a half-covered cell cannot be adjacent to a full cell on the side where it covers an edge. More precisely, the half-covered cell's 2 covered edges must not be shared with any full neighbor.

For a boundary cell with 1 boundary edge: if it's half-covered, it covers the boundary edge and 1 adjacent interior edge. That interior edge is shared with a neighbor. If that neighbor is full, double coverage. So the neighbor sharing that interior edge must not be full.

For a corner cell with 2 boundary edges: if it's half-covered, it covers the 2 boundary edges (which are adjacent, sharing the corner). These 2 edges are both boundary edges, not shared with any full cell. So a half-covered corner cell is fine even if its neighbors are full! Because the 2 covered edges are both boundary edges.

Wait, really? A corner cell has 4 edges: 2 boundary and 2 interior. If it's half-covered with the triangle at the corner, the 2 legs are the 2 boundary edges. The 2 interior edges are not covered by this cell. They must be covered by the adjacent cells. If the adjacent cells are full, they cover those edges. ✓ No double coverage.

So a half-covered corner cell (with triangle at the grid corner) is compatible with full neighbors.

But a half-covered edge (non-corner) boundary cell: it has 1 boundary edge and 3 interior edges. If half-covered, it covers 2 adjacent edges. The boundary edge must be one of them (since it must be covered by this cell). The other covered edge is an interior edge adjacent to the boundary edge. That interior edge is shared with a neighbor, which must not be full.

So for a half-covered non-corner boundary cell, the interior neighbor sharing the covered interior edge must not be full.

This adds constraints. Let me reconsider the problem.

Let me think about the boundary more carefully. The boundary has:
- 4 corner cells: each has 2 boundary edges.
- 392 edge cells: each has 1 boundary edge.

For a corner cell: can be full (covers all 4 edges) or half-covered (covers 2 boundary edges). If half-covered, the 2 interior edges are covered by neighbors.

For an edge cell: can be full (covers all 4 edges) or half-covered (covers 1 boundary + 1 interior edge). If half-covered, the covered interior edge's neighbor must not be full. The other 2 interior edges must be covered by their respective neighbors.

Now, let me think about the boundary structure. Going around the boundary, cells alternate colors (chessboard). Let me consider the bottom row (row 0, cells $(0,0)$ to $(99,0)$). These cells alternate black/white. The boundary edge of each is the bottom edge.

If a bottom-row cell is full, it covers all 4 edges including the bottom boundary edge. ✓
If a bottom-row cell is half-covered, it covers the bottom edge and one adjacent interior edge (either the left or right edge of the cell, or the top edge). Wait, the bottom edge is adjacent to the left edge (sharing the bottom-left corner) and the right edge (sharing the bottom-right corner). But the top edge is not adjacent to the bottom edge (they're opposite). So the half-covered cell covers the bottom edge and either the left or right edge.

If it covers the bottom and left edges: the left edge is shared with the left neighbor. That neighbor must not be full.
If it covers the bottom and right edges: the right edge is shared with the right neighbor. That neighbor must not be full.

So a half-covered boundary cell forces one of its horizontal neighbors to not be full.

Now, along the bottom row, if we alternate full and half-covered cells (like a chessboard pattern), each half-covered cell forces its full neighbor to not be full. But in a chessboard pattern, the half-covered cell's neighbor is full. Contradiction!

Wait, let me be more specific. Bottom row, cells $(0,0), (1,0), \ldots, (99,0)$. Say $(0,0)$ is half-covered (covers bottom and right edges). Then $(1,0)$ (the right neighbor) must not be full. So $(1,0)$ is half-covered or empty. But $(1,0)$ is a boundary cell, so it must be non-empty. So $(1,0)$ is half-covered.

$(1,0)$ is half-covered: covers bottom edge and either left or right edge. If it covers bottom and left: left edge shared with $(0,0)$. $(0,0)$ is half-covered (not full), so no double coverage. ✓ But then $(0,0)$'s right edge is covered by $(1,0)$, and $(0,0)$'s right edge was covered by $(0,0)$ (since $(0,0)$ covers bottom and right). Double coverage! 

Hmm, wait. $(0,0)$ covers bottom and right. $(1,0)$ covers bottom and left. The left edge of $(1,0)$ is the right edge of $(0,0)$. So both $(0,0)$ and $(1,0)$ cover this edge. Double coverage! Bad.

So if $(0,0)$ covers bottom+right, then $(1,0)$ can't cover bottom+left. $(1,0)$ must cover bottom+right. Then $(2,0)$ can't be full (its left edge is covered by $(1,0)$). So $(2,0)$ is half-covered, covering bottom+right. And so on.

This cascades: all cells in the bottom row are half-covered, each covering bottom+right. But then the rightmost cell $(99,0)$ covers bottom+right, and the right edge is a boundary edge. So $(99,0)$ covers 2 boundary edges (bottom and right). That's fine for a corner cell.

But wait, $(99,0)$ is a corner cell (bottom-right corner). It has 2 boundary edges: bottom and right. If it's half-covered covering bottom+right, that's the corner triangle. ✓

But what about the top edge of these bottom-row cells? Each bottom-row cell has a top edge, which is an interior edge shared with the cell above. If the bottom-row cell is half-covered (covering bottom+right), the top edge is not covered by this cell. So the top edge must be covered by the cell above. The cell above must be full or half-covered (covering its bottom edge).

If the cell above is full, it covers all 4 edges including the bottom edge (shared with the bottom-row cell). ✓ No double coverage (bottom-row cell doesn't cover top edge).

So the cells above the half-covered bottom-row cells can be full. 

But this means the entire bottom row is half-covered (100 cells), and similarly for other boundary rows. That's a lot of half-covered cells.

Actually wait, I think I made an error. Let me reconsider. If $(0,0)$ is half-covered covering bottom+right, then $(1,0)$'s left edge is covered by $(0,0)$. So $(1,0)$ can't cover its left edge. $(1,0)$ must cover its bottom edge (boundary). The other covered edge must be adjacent to bottom and not be the left edge. So it must be the right edge. So $(1,0)$ covers bottom+right. Then $(2,0)$'s left edge is covered by $(1,0)$, so $(2,0)$ covers bottom+right. And so on.

This means the entire bottom row is half-covered, each covering bottom+right. That's 100 half-covered cells just for the bottom row. Similarly for the other 3 sides. But corners are shared, so total boundary half-covered = 4 × 100 - 4 = 396 (all boundary cells). That gives $b \geq 396$, $a \leq (10100 - 396)/2 = 4852$, $c \leq 4752$.

But wait, this was for the case where the first cell $(0,0)$ is half-covered. What if $(0,0)$ is full instead?

If $(0,0)$ is full, it covers all 4 edges. Then $(1,0)$'s left edge is covered by $(0,0)$. $(1,0)$ must cover its bottom edge. The other covered edge is adjacent to bottom and not left, so right. So $(1,0)$ covers bottom+right. Then $(2,0)$'s left edge is covered by $(1,0)$, so $(2,0)$ covers bottom+right. And so on until $(99,0)$.

So even if $(0,0)$ is full, the rest of the bottom row is half-covered. That's 99 half-covered cells on the bottom row (excluding $(0,0)$ which is full).

Hmm, but what about $(99,0)$? It covers bottom+right. Its right edge is a boundary edge. So it covers 2 boundary edges. That's fine for a corner cell. But then the cell above $(99,0)$, which is $(99,1)$, has its bottom edge covered by $(99,0)$. And $(99,1)$ is on the right boundary. Its right edge is a boundary edge that must be covered.

This is getting very complex. Let me think about it more systematically.

Let me consider the bottom row of cells: $(0,0), (1,0), \ldots, (99,0)$. Each has a bottom boundary edge. Going left to right:

Case 1: $(0,0)$ is full. Then $(1,0)$'s left edge is covered by $(0,0)$. $(1,0)$ must cover bottom (boundary) + right (since left is taken). Then $(2,0)$'s left is covered by $(1,0)$, so $(2,0)$ covers bottom+right. ... $(99,0)$ covers bottom+right.

But $(99,0)$ is the bottom-right corner. Its right edge is a boundary edge. So $(99,0)$ covers bottom+right, both boundary edges. The triangle is at the bottom-right corner. Its top and left edges are not covered by $(99,0)$. The left edge is covered by $(98,0)$ (which covers bottom+right, and its right edge = $(99,0)$'s left edge). ✓ The top edge of $(99,0)$ must be covered by $(99,1)$.

Case 2: $(0,0)$ is half-covered. It covers bottom+left (both boundary edges, corner triangle) or bottom+right.

If $(0,0)$ covers bottom+left: left edge is a boundary edge. ✓. Right edge not covered by $(0,0)$. $(1,0)$'s left edge is not covered by $(0,0)$. $(1,0)$ must cover bottom. Other edge: left or right. If left: $(1,0)$ covers bottom+left. Left edge shared with $(0,0)$, which doesn't cover its right edge. ✓ No double coverage. Then $(2,0)$'s left is covered by $(1,0)$, so $(2,0)$ covers bottom+right. Then $(3,0)$'s left is covered, covers bottom+right. ... $(99,0)$ covers bottom+right.

If $(0,0)$ covers bottom+right: as before, cascades to all covering bottom+right.

So in Case 2 with bottom+left: $(0,0)$ covers bottom+left, $(1,0)$ covers bottom+left, $(2,0)$ covers bottom+right, $(3,0)$ covers bottom+right, ..., $(99,0)$ covers bottom+right.

Wait, that doesn't seem right. Let me recheck. $(1,0)$ covers bottom+left. Its left edge is shared with $(0,0)$. $(0,0)$ covers bottom+left (not right). So $(0,0)$'s right edge is not covered by $(0,0)$. $(1,0)$'s left edge = $(0,0)$'s right edge, covered by $(1,0)$. ✓ No double coverage.

$(2,0)$'s left edge is shared with $(1,0)$. $(1,0)$ covers bottom+left (not right). So $(1,0)$'s right edge is not covered by $(1,0)$. $(2,0)$ can cover its left edge. $(2,0)$ covers bottom+left. Then $(3,0)$'s left is covered by $(2,0)$... wait, $(2,0)$ covers bottom+left, not right. So $(3,0)$'s left edge (= $(2,0)$'s right edge) is not covered by $(2,0)$. $(3,0)$ can cover bottom+left. And so on.

So in this case, all cells cover bottom+left. But $(99,0)$ covers bottom+left. Its left edge is shared with $(98,0)$. $(98,0)$ covers bottom+left (not right). So $(99,0)$'s left edge is not covered by $(98,0)$. $(99,0)$ covers it. ✓. But $(99,0)$'s right edge is a boundary edge, not covered by $(99,0)$ (it covers bottom+left). So the right boundary edge of $(99,0)$ is uncovered! Problem!

So this doesn't work. $(99,0)$ must cover its right boundary edge. So $(99,0)$ must cover bottom+right (or be full).

Let me reconsider. The issue is that the rightmost cell must cover its right boundary edge, and the leftmost cell must cover its left boundary edge. So:
- $(0,0)$ must cover its left boundary edge.
- $(99,0)$ must cover its right boundary edge.

If all cells cover bottom+left: $(99,0)$ doesn't cover right. Bad.
If all cells cover bottom+right: $(0,0)$ doesn't cover left. Bad (unless $(0,0)$ is a corner and covers left via a different mechanism).

Wait, $(0,0)$ is the bottom-left corner. It has 2 boundary edges: bottom and left. If it covers bottom+right, it doesn't cover left. The left boundary edge is uncovered. Bad.

So $(0,0)$ must cover left. And $(99,0)$ must cover right. Both must also cover bottom. So $(0,0)$ covers bottom+left, and $(99,0)$ covers bottom+right. But as we saw, if $(0,0)$ covers bottom+left, the cascade makes all cells cover bottom+left, and $(99,0)$ doesn't cover right. Contradiction.

Unless some cells are full. Let me intersperse full cells.

Pattern: $(0,0)$ half-covered (bottom+left), $(1,0)$ full, $(2,0)$ half-covered (bottom+right), $(3,0)$ full, ...

$(0,0)$ covers bottom+left. $(1,0)$ is full, covers all 4 edges. $(0,0)$'s right edge = $(1,0)$'s left edge, covered by $(1,0)$. $(0,0)$ doesn't cover right. ✓ No double coverage.

$(1,0)$ full: covers all 4. $(2,0)$'s left edge = $(1,0)$'s right edge, covered by $(1,0)$. So $(2,0)$ can't cover left. $(2,0)$ covers bottom+right. ✓

$(2,0)$ covers bottom+right. $(3,0)$'s left edge = $(2,0)$'s right edge, covered by $(2,0)$. So $(3,0)$ can't cover left. $(3,0)$ is full, covers all 4. $(2,0)$'s right edge covered by $(2,0)$ and also by $(3,0)$? No, $(3,0)$ covers its left edge = $(2,0)$'s right edge. Double coverage! Bad.

So $(3,0)$ can't be full if $(2,0)$ covers right. $(3,0)$ must not cover its left edge. $(3,0)$ covers bottom+right. Then $(4,0)$'s left is covered by $(3,0)$, so $(4,0)$ covers bottom+right. And so on until $(99,0)$ covers bottom+right. ✓

So the pattern is: $(0,0)$ half (bottom+left), $(1,0)$ full, $(2,0)$ half (bottom+right), $(3,0)$ half (bottom+right), ..., $(99,0)$ half (bottom+right).

That's 1 full + 99 half-covered on the bottom row. Not great.

Alternatively: $(0,0)$ half (bottom+left), $(1,0)$ half (bottom+right), $(2,0)$ full, $(3,0)$ half (bottom+left), $(4,0)$ half (bottom+right), $(5,0)$ full, ...

Let me check: $(0,0)$ covers bottom+left. $(1,0)$ covers bottom+right. $(0,0)$'s right = $(1,0)$'s left. $(0,0)$ doesn't cover right. $(1,0)$ doesn't cover left. So this edge is uncovered! Bad.

Hmm. So adjacent half-covered cells where one covers right and the other doesn't cover left leaves the shared edge uncovered.

Let me reconsider. For the bottom row, each cell covers its bottom edge. The question is what else it covers. The options for the "other" edge are: left, right, or top (if full, all).

If a cell covers bottom+left: its left edge is covered. Its right edge is not covered by it. The right neighbor must cover the shared edge (via the right neighbor covering its left edge) or the right neighbor is full.

If a cell covers bottom+right: its right edge is covered. Its left edge is not covered by it. The left neighbor must cover the shared edge or be full.

So for each interior edge in the bottom row (between $(k,0)$ and $(k+1,0)$): exactly one of them covers it. $(k,0)$ covers it if $(k,0)$ covers right. $(k+1,0)$ covers it if $(k+1,0)$ covers left. Or one of them is full.

If $(k,0)$ covers bottom+right: covers the edge. $(k+1,0)$ must not cover left. So $(k+1,0)$ covers bottom+right or is full (but if full, it covers left too - double coverage). So $(k+1,0)$ covers bottom+right.

If $(k,0)$ covers bottom+left: doesn't cover right. $(k+1,0)$ must cover left (covers bottom+left) or be full (covers all, including left). If $(k+1,0)$ is full, it covers left. ✓ But then $(k+1,0)$ also covers right, and $(k+2,0)$'s left is covered by $(k+1,0)$. So $(k+2,0)$ covers bottom+right.

If $(k,0)$ is full: covers right. $(k+1,0)$ must not cover left. So $(k+1,0)$ covers bottom+right.

So the pattern along the bottom row is:
- A cell covering bottom+left forces the next cell to cover bottom+left or be full.
- A cell covering bottom+right forces the next cell to cover bottom+right.
- A full cell forces the next cell to cover bottom+right.

And:
- $(0,0)$ must cover left (boundary). So it covers bottom+left or is full.
- $(99,0)$ must cover right (boundary). So it covers bottom+right or is full.

If $(0,0)$ covers bottom+left: the next cell covers bottom+left or is full. If the next is bottom+left, the next next is bottom+left or full. This can continue, but eventually we need to reach $(99,0)$ which covers bottom+right.

To transition from bottom+left to bottom+right, we need a full cell. A full cell forces the next to be bottom+right. But the cell before the full cell: if it covers bottom+left, the full cell covers left (shared edge) - but the bottom+left cell doesn't cover right, so no double coverage. ✓

Wait, let me recheck. $(k,0)$ covers bottom+left (doesn't cover right). $(k+1,0)$ is full (covers all, including left = $(k,0)$'s right). $(k,0)$'s right edge is covered by $(k+1,0)$ only. ✓ No double coverage. And $(k+1,0)$ covers right, so $(k+2,0)$ must cover bottom+right. ✓

So the transition works: ...bottom+left, full, bottom+right, bottom+right, ...

Now, to maximize full cells, we want as many full cells as possible. But full cells can't be adjacent (independent set). And each full cell on the bottom row "resets" the cascade.

Pattern: bottom+left, full, bottom+right, full, bottom+right, full, ...

Wait, after a full cell, the next is bottom+right. After bottom+right, the next is bottom+right (not full, since bottom+right forces next to be bottom+right). So we can't have two full cells separated by just one bottom+right.

Actually, after a full cell, next is bottom+right. After bottom+right, next is bottom+right. So once we go to bottom+right, we stay there. We can only have full cells in the bottom+left region.

Pattern: bottom+left, bottom+left, ..., bottom+left, full, bottom+right, bottom+right, ..., bottom+right.

We can have at most 1 full cell in the bottom row (the transition point). Or 0 if we go directly from bottom+left to bottom+right... but that doesn't work (bottom+left forces next to be bottom+left or full, not bottom+right).

Wait, can we have multiple transitions? bottom+left, full, bottom+right, ..., but then we're stuck in bottom+right. To go back to bottom+left, we'd need... a cell covering bottom+left after bottom+right. But bottom+right forces next to be bottom+right. So we can't go back.

Unless we use a full cell to transition. After bottom+right, the next is bottom+right. If we make a cell full, it covers all edges. But the previous cell covers bottom+right (covers right edge = full cell's left edge). Full cell also covers left. Double coverage! Bad.

So once we go to bottom+right, we can't have any more full cells. The pattern is: some bottom+left cells, then one full cell, then bottom+right cells. At most 1 full cell per row.

Similarly, if $(0,0)$ is full: covers all. Next is bottom+right. Then bottom+right, ..., bottom+right. $(99,0)$ covers bottom+right. ✓. 1 full cell.

If $(0,0)$ is full and $(99,0)$ is full: $(0,0)$ full, $(1,0)$ bottom+right, ..., $(98,0)$ bottom+right, $(99,0)$ full. But $(98,0)$ covers bottom+right (covers right = $(99,0)$'s left). $(99,0)$ full covers left. Double coverage! Bad.

So at most 1 full cell per boundary row. With 4 boundary rows (top, bottom, left, right), and corners shared, this is complex.

Hmm wait, I think I'm overcomplicating this. Let me reconsider.

Actually, I realize the bottom row analysis shows that on each side of the boundary, we can have at most 1 full cell (or a limited number). This severely limits the number of full boundary cells.

But actually, I was only considering half-covered cells that cover bottom+left or bottom+right. What about half-covered cells that cover bottom+top? Wait, bottom and top are opposite edges, not adjacent. A half-covered cell covers 2 adjacent edges. Bottom is adjacent to left and right, not top. So the only options for a bottom-row half-covered cell are bottom+left or bottom+right.

OK so my analysis is correct. On the bottom row, the pattern is constrained.

Let me reconsider the whole problem. Maybe the approach of making all cells of one chessboard color full is wrong, and we need a different strategy.

Let me think about this problem from a different angle. 

Let me consider the "edge orientation" model. Each edge is oriented towards its owner (the middle vertex of its path). At each vertex, the in-edges form perpendicular pairs.

Consider the grid as a graph and think about what orientations are valid.

At each interior vertex (degree 4), the in-edges are 0, 2-perpendicular, or 4. If 4, they pair into 2 perpendicular pairs (2 ways). If 2, they must be perpendicular (4 choices: N+E, E+S, S+W, W+N). If 0, nothing.

At each boundary vertex (degree 3), the in-edges are 0 or 2. If 2, they must be perpendicular. For a bottom-edge vertex
