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
  <problem_id>polymath_01806</problem_id>
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

A $5 \times 100$  table is divided into $500$ unit square cells, where $n$ of them are coloured black and the rest are coloured white. Two unit square cells are called [i]adjacent[/i] if they share a common side. Each of the unit square cells has at most two adjacent black unit square cells. Find the largest possible value of $n$.

## Standard Solution

1. **Construction**:
   - We need to find the largest possible number of black cells, \( n \), in a \( 5 \times 100 \) grid such that each black cell has at most two adjacent black cells.
   - Consider a general \( 5 \times k \) grid. We will color black all \( 2k + 6 \) cells on the border along with the middle \( k - 4 \) cells in the center row. This construction ensures that each black cell has at most two adjacent black cells.
   - For \( k = 100 \), the number of black cells is \( 2 \times 100 + 6 + (100 - 4) = 200 + 6 + 96 = 302 \).

2. **Bounding the Number of Black Cells**:
   - Let \( n \) be the number of black cells. We denote by \( a, b, c \) the number of black cells that are adjacent to exactly 2, 3, and 4 black cells respectively. Thus, \( a + b + c = n \).
   - Note that \( a \leq 4 \) since such a cell uses a corner of the grid, and \( b \leq 2k + 2 \) as such a cell is on the boundary of the grid.
   - We will count the number of pairs (cell \( c \), black cell adjacent to \( c \)). On one hand, this number is at most \( 2 \times (\#\text{cells}) \) since each cell is adjacent to at most 2 black cells. Counting from the perspective of black cells, we get:
     \[
     \#\text{Pairs} = 2a + 3b + 4c
     \]
     Since \( a + b + c = n \), we can rewrite this as:
     \[
     \#\text{Pairs} = 2a + 3b + 4(n - a - b) = 4n - 2a - b
     \]
     Given \( a \leq 4 \) and \( b \leq 2k + 2 \), we have:
     \[
     4n - 2a - b \geq 4n - 8 - (2k + 2) = 4n - 2k - 10
     \]
     This gives us the following inequality:
     \[
     4n - 2k - 10 \leq 2 \times (\#\text{cells}) = 2 \times 5k = 10k
     \]
     Simplifying, we get:
     \[
     4n - 2k - 10 \leq 10k \implies 4n \leq 12k + 10 \implies n \leq \frac{12k + 10}{4} = 3k + 2.5
     \]
     Since \( n \) must be an integer, we have:
     \[
     n \leq 3k + 2
     \]

3. **Conclusion**:
   - For \( k = 100 \), the largest possible value of \( n \) is \( 3 \times 100 + 2 = 302 \).

The final answer is \( \boxed{302} \)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have a 5×100 grid, n cells black, each cell has at most 2 adjacent black cells. Find max n.

Let me think about this carefully.

The grid is 5 rows × 100 columns. Each cell has at most 2 adjacent (sharing a side) black cells. We want to maximize the number of black cells.

Let me think about the structure. Consider the black cells as a graph where edges connect adjacent black cells. The condition is that every cell (black or white) has at most 2 black neighbors.

Wait, re-read: "Each of the unit square cells has at most two adjacent black unit square cells." So every cell (whether black or white) has at most 2 black neighbors.

Actually, let me re-read. "Each of the unit square cells has at most two adjacent black unit square cells." This means for every cell, the number of its adjacent cells that are black is at most 2.

So for every cell v, |{black neighbors of v}| ≤ 2.

We want to maximize the number of black cells.

Let me think about this as a constraint. Consider the bipartite-like structure. Actually, let me think column by column.

Let me think about what configurations work. 

Consider a column of 5 cells. The black cells form a subset of {1,2,3,4,5} in each column.

Let me think about the constraint more carefully. Each cell has at most 2 black neighbors. Neighbors are up, down, left, right (within the grid).

For a cell at position (r, c), its neighbors are (r±1, c) and (r, c±1) where they exist.

The constraint: for every cell (r,c), at most 2 of its existing neighbors are black.

Let me think about dense configurations. 

If we color everything black, each interior cell has 4 black neighbors, violating the constraint. So we can't do that.

Let me think about a pattern. What if we use a checkerboard-like pattern but denser?

Consider coloring cells such that each cell has exactly 2 black neighbors (to maximize density).

Let me think about a "stripe" pattern. In each column, color 3 cells black. Say rows 1,3,5 in odd columns and rows 2,4 in even columns? Let me check.

Actually, let me think about this differently. Let's think about the black cells as inducing a subgraph. The constraint is about the degree in the "black neighbor" sense for ALL cells, not just black ones.

Hmm, let me think about a specific pattern. 

Pattern idea: In each column, color 3 cells. Let's say column c has black cells at rows {1, 3, 5} if c is odd, and {2, 4} if c is even. 

Wait, let me just think about what maximizes density.

Let me consider a simpler approach. Think of the grid as columns. In each column, we choose a subset of rows to be black. The constraint involves horizontal (between columns) and vertical (within column) adjacencies.

Vertical: within a column, if rows r and r+1 are both black, they're adjacent black cells (to each other). The constraint is about each cell having at most 2 black neighbors total.

Let me think about the total count. Let's denote the black cells. For each cell, count its black neighbors. Sum over all cells of (black neighbors) = 2 × (number of adjacent black-black pairs) [each pair counted from both sides]. 

The constraint: each cell has ≤ 2 black neighbors. So the sum ≤ 2 × 500 = 1000. Thus the number of adjacent black-black pairs ≤ 500.

Now, the number of adjacent black-black pairs = (horizontal pairs) + (vertical pairs).

Let B = number of black cells = n.
Let H = number of horizontal adjacent black-black pairs (between columns c and c+1).
Let V = number of vertical adjacent black-black pairs (within columns).
Then H + V ≤ 500.

Now, we want to maximize n. We need to relate n to H and V.

In each column, if k cells are black, the minimum number of vertical black-black pairs... well, if the k black cells are consecutive, V_col = k-1. If they're spread out, V_col could be less. But we want to minimize V+H to allow more black cells? No, we want to maximize n, and the constraint is H+V ≤ 500.

Actually, we want to maximize n subject to H+V ≤ 500 and the per-cell constraint (each cell ≤ 2 black neighbors).

Hmm, but H+V ≤ 500 is a necessary condition derived from the per-cell constraint, but it might not be sufficient. Let me think more.

Actually, let me think about it differently. Let me think about the "complement" — white cells.

Each cell has at most 2 black neighbors. An interior cell has 4 neighbors, so it has at least 2 white neighbors. A cell on the edge has 3 neighbors, so at least 1 white neighbor. A corner cell has 2 neighbors, so at least 0 white neighbors.

Hmm, this is about every cell having at most 2 black neighbors. Let me think about the white cells as a "dominating" kind of structure.

Actually, let me think about it from the perspective of: each cell needs at least (degree - 2) white neighbors, where degree is 4 for interior, 3 for edge, 2 for corner.

Let me think about a specific construction first, then try to prove optimality.

Construction attempt: Color cells in a pattern where each column has 3 black cells, arranged as rows {1,2,3} or {3,4,5} or {1,3,5} etc.

Let me try: every column has black cells at rows {1, 3, 5}. Then:
- Vertical pairs: (1,2)? No, row 2 is white. (2,3)? Row 2 white. (3,4)? Row 4 white. (4,5)? Row 4 white. So V = 0 per column, total V = 0.
- Horizontal: between column c and c+1, both have rows 1,3,5 black. So pairs (1,c)-(1,c+1), (3,c)-(3,c+1), (5,c)-(5,c+1). That's 3 per column gap, 99 gaps, H = 297.
- Total H+V = 297 ≤ 500. ✓
- Now check per-cell constraint:
  - Cell (1, c) for interior column: neighbors (2,c) white, (0,c) doesn't exist, (1,c-1) black, (1,c+1) black. So 2 black neighbors. ✓
  - Cell (2, c): neighbors (1,c) black, (3,c) black, (2,c-1) white, (2,c+1) white. 2 black neighbors. ✓
  - Cell (3, c): neighbors (2,c) white, (4,c) white, (3,c-1) black, (3,c+1) black. 2 black. ✓
  - Cell (4, c): neighbors (3,c) black, (5,c) black, (4,c-1) white, (4,c+1) white. 2 black. ✓
  - Cell (5, c): neighbors (4,c) white, (5,c-1) black, (5,c+1) black. 2 black. ✓
  - Edge columns: column 1, cell (1,1): neighbors (2,1) white, (1,2) black. 1 black neighbor. ✓ etc.

So this gives n = 3 × 100 = 300. And the constraint is satisfied.

Can we do better? Let me try 4 black cells per column in some pattern.

Try: columns alternate between {1,2,3,4} and {2,3,4,5}.

Column odd: {1,2,3,4}, column even: {2,3,4,5}.

Vertical pairs in odd column: (1,2),(2,3),(3,4) → 3 pairs. In even column: (2,3),(3,4),(4,5) → 3 pairs. Total V = 3 × 100 = 300.

Horizontal pairs between odd and even column: common rows are {2,3,4}. So 3 pairs per gap. 99 gaps → H = 297.

H + V = 597 > 500. Violates the sum constraint. So this doesn't work (and indeed the per-cell constraint would be violated).

Let me check: cell (2, odd column): neighbors (1,odd) black, (3,odd) black, (2, odd-1) [even col, row 2 black], (2, odd+1) [even col, row 2 black]. That's 4 black neighbors. Violates.

So 4 per column in this pattern doesn't work.

Let me try a different 4-per-column pattern. What about {1,2,4,5} in every column?

Vertical: (1,2) and (4,5) → 2 per column. V = 200.
Horizontal: rows 1,2,4,5 all match between adjacent columns → 4 per gap. H = 4 × 99 = 396.
H+V = 596 > 500.

Cell (2, c): neighbors (1,c) black, (3,c) white, (2,c-1) black, (2,c+1) black. 3 black. Violates.

What about alternating {1,2,4,5} and {1,3,4,5} or something?

Let me think more systematically. 

Let me think about the problem column by column. Let the state of column c be the set S_c ⊆ {1,2,3,4,5} of black rows.

The per-cell constraint for cell (r, c):
- Vertical black neighbors: indicator(r-1 ∈ S_c) + indicator(r+1 ∈ S_c)
- Horizontal black neighbors: indicator(r ∈ S_{c-1}) + indicator(r ∈ S_{c+1})
- Total ≤ 2.

We want to maximize Σ|S_c|.

This is a complex optimization. Let me think about upper bounds.

Upper bound approach: 

Consider the sum Σ_c |S_c| = n. We want to show n ≤ 300, or find a better bound.

Hmm, but maybe we can do better than 300. Let me think.

What if we use a pattern with some columns having 4 and some having 2 or 3?

Let me try: column pattern repeating with period 2: {1,2,3} and {3,4,5}.

Column odd: {1,2,3}, column even: {3,4,5}.

Vertical in odd: (1,2),(2,3) → 2. In even: (3,4),(4,5) → 2. V = 200.
Horizontal between odd and even: common row is {3}. So 1 pair per gap. H = 99.
H + V = 299 ≤ 500. ✓

Check per-cell:
- Cell (3, odd): neighbors (2,odd) black, (4,odd) white, (3, even) black, (3, prev even) black. Wait, for interior odd column c: (3,c-1) is even column, row 3 ∈ {3,4,5} ✓ black. (3,c+1) is even column, row 3 black. (2,c) black, (4,c) white. So 3 black neighbors. Violates!

Hmm. So cell (3, odd column) has 3 black neighbors. Bad.

Let me try {1,2,3} and {1,4,5} alternating.

Odd: {1,2,3}, Even: {1,4,5}.
Vertical odd: (1,2),(2,3) → 2. Even: (4,5) → 1. V per period = 3, over 100 columns ≈ 150 (roughly).
Horizontal: common row between {1,2,3} and {1,4,5} is {1}. 1 pair per gap. H = 99.
H + V ≈ 249.

Check per-cell:
- Cell (1, odd): (2,odd) black, (1,even) black, (1, prev even) black. 3 black. Violates (for interior).

Hmm. The issue is row 1 is black in both, so cell (1, odd) has horizontal black neighbors on both sides plus vertical.

Let me try {1,2,3} and {4,5} alternating. Wait, but then we need to check.

Odd: {1,2,3}, Even: {4,5}.
n = 50×3 + 50×2 = 250. Less than 300.

Not better.

Let me try to think about whether 300 is optimal or if we can beat it.

Let me think about the constraint more carefully with a counting/discharging argument.

Alternative: think about it as follows. Consider the "black neighbor count" b(v) for each cell v. We need b(v) ≤ 2 for all v.

Sum of b(v) over all v = 2(H + V) ≤ 1000, so H + V ≤ 500.

Now, can we get a better upper bound on n?

Let me think about vertical structure. In a single column with k black cells, what's the minimum V (vertical black-black pairs)? If the k cells are as spread out as possible. For k cells in 5 rows, the minimum number of adjacent pairs... 

If k=0: V=0
k=1: V=0
k=2: V=0 if non-adjacent (e.g., {1,3}, {1,4}, {1,5}, {2,4}, {2,5}, {3,5}), V=1 if adjacent.
k=3: V≥1 (pigeonhole: 3 cells in 5 positions, at least one adjacent pair). Min V=1 with {1,3,5}.
k=4: V≥2. Min V=2 with {1,2,4,5} or {1,3,4,5}... wait {1,3,4,5} has (3,4),(4,5) = 2. {1,2,4,5} has (1,2),(4,5)=2. Can we do V=1? 4 cells in 5 positions means at most 1 gap, so at least... 4 cells, 5 positions, the white cell splits into at most 2 groups. If white is at position 3: {1,2} and {4,5}, V=2. If white at position 1: {2,3,4,5}, V=3. If white at position 2: {1} and {3,4,5}, V=2. So min V=2.
k=5: V=4.

So minimum V per column:
k=0: 0, k=1: 0, k=2: 0, k=3: 1, k=4: 2, k=5: 4.

Now for horizontal: between columns c and c+1, the number of horizontal black-black pairs = |S_c ∩ S_{c+1}|.

H = Σ_{c=1}^{99} |S_c ∩ S_{c+1}|.

Constraint: H + V ≤ 500 where V = Σ V_c.

We want to maximize n = Σ|S_c|.

Hmm, this is still complex. Let me think about whether we can beat 300.

With the {1,3,5} pattern: n=300, V=0, H=297, H+V=297. We have room: 500-297 = 203 more budget for H+V.

Can we add more black cells? If we change some columns from 3 to 4 black cells, we add 1 black cell but increase V by at least 1 (from 0 to at least 1, but actually from the {1,3,5} base, adding any cell creates a vertical pair). Also might increase H.

Let me think: starting from all columns = {1,3,5}. Change some columns to {1,2,3,5} (add row 2). Then V increases by 1 (pair (1,2) and (2,3) → actually (1,2) and (2,3), that's 2 new vertical pairs). H: the new column has rows {1,2,3,5}, adjacent columns have {1,3,5}. Intersection = {1,3,5}, so |intersection| = 3, same as before. So H unchanged. V increases by 2. 

But we also need to check the per-cell constraint, not just H+V ≤ 500.

Cell (2, modified column): neighbors (1, col) black, (3, col) black, (2, col-1) white, (2, col+1) white. 2 black. ✓
Cell (1, modified column): (2, col) black, (1, col-1) black, (1, col+1) black. 3 black. Violates!

So cell (1, modified column) now has 3 black neighbors. Bad.

What if we add row 4 instead: {1,3,4,5}?
Cell (4, col): (3,col) black, (5,col) black, (4,col-1) white, (4,col+1) white. 2 black. ✓
Cell (3, col): (2,col) white, (4,col) black, (3,col-1) black, (3,col+1) black. 3 black. Violates!

Same issue. Adding a cell adjacent (vertically) to a cell that already has 2 horizontal black neighbors pushes it to 3.

So in the {1,3,5} pattern, rows 1, 3, 5 each have 2 horizontal black neighbors (from adjacent columns). Adding any vertically adjacent cell would push them to 3.

What if we modify two adjacent columns together? Like column c = {1,2,3,5} and column c+1 = {1,3,4,5}?

Hmm, this is getting complicated. Let me think about it more carefully.

Actually, let me reconsider. The key insight: in the {1,3,5} pattern, every black cell has exactly 2 black neighbors (both horizontal), and the constraint is tight for all black cells. White cells (rows 2, 4) have exactly 2 black neighbors (both vertical). So the constraint is tight everywhere.

To add more black cells, we'd need to relax some constraints, but they're all tight. So maybe 300 is optimal?

Wait, but maybe a different pattern with some cells having fewer than 2 black neighbors could allow a higher total.

Let me think about a different approach. Let me consider the problem as a graph coloring / independent set type problem.

Actually, let me think about it as follows. The constraint is that the black cells form a subgraph where every vertex (cell) in the full grid sees at most 2 black neighbors. 

Let me think about a "path-like" structure. If the black cells form a set of disjoint paths (in the grid graph), then each black cell has at most 2 black neighbors (its path neighbors), and white cells adjacent to the path have at most 2 black neighbors (if the path passes by). But we need ALL cells to have at most 2 black neighbors, including white cells that might be adjacent to multiple path segments.

Hmm, let me think about the problem differently.

Let me consider the dual perspective. Define for each cell its "black degree" = number of black neighbors. We need black degree ≤ 2 for all cells.

Consider the white cells. A white cell with black degree d means d of its neighbors are black. We need d ≤ 2.

Now, think about it as: the black cells form a structure where no cell (black or white) is adjacent to more than 2 black cells.

Let me think about the maximum density. In an infinite grid, what's the maximum density of such a configuration?

Consider the {1,3,5} pattern extended infinitely: density 3/5. Can we do better on an infinite grid?

Let me think about a "thick diagonal" pattern. Color cells (r, c) where r + c ≡ 0 or 1 (mod 3)? That gives density 2/3. Let me check.

In a 5×∞ grid, color (r,c) black if (r+c) mod 3 ∈ {0, 1}. Density 2/3.

Cell (r,c): neighbors (r±1, c) and (r, c±1). Their (r+c) mod 3 values are (r+c±1) mod 3. So the neighbors have residues (r+c+1) mod 3 and (r+c-1) mod 3. 

If (r+c) mod 3 = 0: neighbors have residues 1 and 2. Black neighbors = those with residue 1 (since 1 ∈ {0,1}) and those with residue 2 (not black). Wait, neighbors: (r+1,c) has residue 1, (r-1,c) has residue 2, (r,c+1) has residue 1, (r,c-1) has residue 2. So black neighbors (residue 0 or 1): (r+1,c) residue 1 ✓, (r-1,c) residue 2 ✗, (r,c+1) residue 1 ✓, (r,c-1) residue 2 ✗. So 2 black neighbors. ✓

If (r+c) mod 3 = 1: neighbors have residues 0 and 2. (r+1,c) residue 2 ✗, (r-1,c) residue 0 ✓, (r,c+1) residue 2 ✗, (r,c-1) residue 0 ✓. 2 black neighbors. ✓

If (r+c) mod 3 = 2 (white cell): neighbors have residues 0 and 1. (r+1,c) residue 0 ✓, (r-1,c) residue 1 ✓, (r,c+1) residue 0 ✓, (r,c-1) residue 1 ✓. 4 black neighbors! Violates!

So this doesn't work because white cells have 4 black neighbors.

The issue is that white cells surrounded by black cells have too many black neighbors.

So we need white cells to also have ≤ 2 black neighbors. This means white cells can't be too "surrounded" by black.

Let me think about this more carefully. The constraint on white cells is quite restrictive. A white cell needs at most 2 black neighbors, meaning at least (degree - 2) of its neighbors are white.

For interior white cells (degree 4): at least 2 white neighbors.
For edge white cells (degree 3): at least 1 white neighbor.
For corner white cells (degree 2): at least 0 white neighbors (no constraint from being white).

So white cells need to be "connected" in some sense — interior white cells need at least 2 white neighbors.

This is like a domination/covering problem. The white cells need to form a structure where each interior white cell has at least 2 white neighbors.

Hmm, let me think about the white cells forming "paths" or "strips."

If white cells form horizontal strips (entire rows white), then each white cell in the strip has 2 white neighbors (left and right), satisfying the constraint. And the black cells above and below the strip...

Let me consider: make row 2 and row 4 entirely white. Then rows 1, 3, 5 can be black. This is the {1,3,5} pattern. Each white cell in row 2 has neighbors: (1,c) black, (3,c) black, (2,c-1) white, (2,c+1) white. 2 black neighbors. ✓. Each white cell in row 4: (3,c) black, (5,c) black, (4,c-1) white, (4,c+1) white. 2 black. ✓.

Now, can we make only one row white? Say row 3 is entirely white, and rows 1,2,4,5 are black.

White cell (3,c): neighbors (2,c) black, (4,c) black, (3,c-1) white, (3,c+1) white. 2 black. ✓.
Black cell (2,c): neighbors (1,c) black, (3,c) white, (2,c-1) black, (2,c+1) black. 3 black. Violates!

So rows 1,2 both black causes cell (2,c) to have 3 black neighbors (left, right, and above). 

What if we make rows 1,2 black but not all columns? We need to break the horizontal adjacency in row 2.

This is getting complex. Let me think about the problem as an optimization over column states.

Since the grid is 5×100, and the constraint is local (depends on adjacent columns), this is amenable to dynamic programming. But I need to solve it analytically.

Let me enumerate possible column states and think about which pairs of consecutive states are compatible.

A column state is a subset S ⊆ {1,2,3,4,5}. There are 32 states. For two consecutive columns with states S and T, and the previous column having state R, the constraint on column S involves R, S, T.

Actually, the per-cell constraint for cell (r, c) depends on S_{c-1}, S_c, S_{c+1}. So it's a 3-column constraint. This makes it a bit more complex for DP but still manageable.

But I need to find the answer analytically. Let me think about upper bounds more carefully.

Let me try a different counting argument.

Consider the 5×100 grid. Look at each 2×2 block of cells. Actually, let me think about 2-row strips.

Consider rows 1-2. In this 2×100 strip, look at each column. If both cells in a column are black (rows 1 and 2 both black), then:
- Cell (1, c) has a black neighbor below: (2, c). It can have at most 1 more black neighbor among (1, c-1) and (1, c+1).
- Cell (2, c) has a black neighbor above: (1, c). It can have at most 1 more black neighbor among (2, c-1), (2, c+1), (3, c).

Hmm, this is getting complicated. Let me try a different approach.

Let me think about the problem in terms of "columns" and use a transfer matrix / DP approach mentally.

Actually, let me just try to see if we can beat 300 with a clever pattern.

Idea: Use a pattern with period 3 or 4 that achieves density > 3/5.

Let me try a period-3 pattern. Columns cycle through states A, B, C.

We need each cell to have ≤ 2 black neighbors. Let me try to find states A, B, C (subsets of {1,2,3,4,5}) that maximize (|A|+|B|+|C|)/3 while satisfying constraints.

The constraint for a cell in column with state B (middle of A, B, C):
- Cell (r) in column B: black neighbors = [r-1 ∈ B] + [r+1 ∈ B] + [r ∈ A] + [r ∈ C] ≤ 2.

For edge columns, the constraint is weaker (fewer neighbors), so let me focus on interior columns.

Let me try A = {1,2,3}, B = {1,3,5}, C = {3,4,5}.

Check cell (r) in column B = {1,3,5}, with A = {1,2,3} on left, C = {3,4,5} on right:
- r=1: [0∈B]=0, [2∈B]=0, [1∈A]=1, [1∈C]=0. Total=1. ✓
- r=2: [1∈B]=1, [3∈B]=1, [2∈A]=1, [2∈C]=0. Total=3. Violates!

Hmm. Let me try A = {1,2,4}, B = {1,3,5}, C = {2,4,5}.

Cell in B = {1,3,5}, A = {1,2,4}, C = {2,4,5}:
- r=1: [2∈B]=0, [1∈A]=1, [1∈C]=0. Total=1. ✓
- r=2: [1∈B]=1, [3∈B]=1, [2∈A]=1, [2∈C]=1. Total=4. Violates!

The problem is that row 2 in B has black neighbors above (row 1) and below (row 3) within B, plus potentially horizontal. So if both row 1 and row 3 are in B, row 2 (even if white) has 2 vertical black neighbors, and any horizontal black neighbor would push it to 3.

So if B = {1,3,5}, then for row 2 (white in B): vertical black neighbors = [1∈B] + [3∈B] = 2. So horizontal black neighbors must be 0: [2∈A] + [2∈C] = 0. So 2 ∉ A and 2 ∉ C. Similarly for row 4: 4 ∉ A and 4 ∉ C.

So if B = {1,3,5}, then A and C cannot contain 2 or 4. So A, C ⊆ {1,3,5}. Then |A|, |C| ≤ 3. And we're back to the {1,3,5} pattern.

Similarly, for row 1 (black in B): vertical = [2∈B] = 0. Horizontal = [1∈A] + [1∈C] ≤ 2. So at most 2, which is fine.
Row 3 (black in B): vertical = [2∈B] + [4∈B] = 0. Horizontal = [3∈A] + [3∈C] ≤ 2. Fine.
Row 5 (black in B): vertical = [4∈B] = 0. Horizontal = [5∈A] + [5∈C] ≤ 2. Fine.

So if any column has state {1,3,5}, its neighbors must be subsets of {1,3,5}. This means once we use {1,3,5}, we're locked into subsets of {1,3,5} for all adjacent columns, and by induction, all columns. So the {1,3,5} pattern is "rigid" — we can't mix it with other patterns.

But maybe we can use a pattern that never uses {1,3,5} and achieves higher density.

Let me think about what column states allow 4 black cells. The 4-element subsets of {1,2,3,4,5} are:
{1,2,3,4}, {1,2,3,5}, {1,2,4,5}, {1,3,4,5}, {2,3,4,5}.

For a column with 4 black cells, there are vertical pairs. Let's check the constraint on the white cell in that column.

If S = {1,2,3,4} (row 5 white): white cell (5,c) has vertical neighbor (4,c) black. Horizontal: [5∈A] + [5∈C]. So total = 1 + [5∈A] + [5∈C] ≤ 2, meaning [5∈A] + [5∈C] ≤ 1. So at most one neighbor column has row 5 black.

Also, black cells in the column: e.g., cell (1,c): vertical [2∈S]=1. Horizontal [1∈A]+[1∈C] ≤ 1. So at most one neighbor has row 1.
Cell (2,c): vertical [1∈S]+[3∈S] = 2. Horizontal [2∈A]+[2∈C] = 0. So 2∉A and 2∉C.
Cell (3,c): vertical [2∈S]+[4∈S] = 2. Horizontal [3∈A]+[3∈C] = 0. So 3∉A and 3∉C.
Cell (4,c): vertical [3∈S]+[5∈S] = 1. Horizontal [4∈A]+[4∈C] ≤ 1. At most one neighbor has row 4.

So if S = {1,2,3,4}: A and C cannot contain 2 or 3. And at most one of A, C contains 1; at most one contains 4; at most one contains 5.

So A, C ⊆ {1,4,5} (since 2,3 excluded). And |A ∩ {1}| + |C ∩ {1}| ≤ 1, |A ∩ {4}| + |C ∩ {4}| ≤ 1, |A ∩ {5}| + |C ∩ {5}| ≤ 1.

So |A| + |C| ≤ 3 (at most 1 for each of rows 1, 4, 5 across both A and C). Actually more precisely, A ⊆ {1,4,5} and C ⊆ {1,4,5} and for each row r ∈ {1,4,5}, at most one of A, C contains r. So |A| + |C| ≤ 3.

If we have a column with 4 black cells, its two neighbors together have at most 3 black cells. So the average over 3 columns is (4+3)/3 ≈ 2.33, which is less than 3. Not great.

What if we alternate: 4, 1, 4, 1, ...? No wait, the neighbors of a 4-column have at most 3 total, so if one neighbor has 3, the other has 0. Or 2+1, etc.

Pattern: 4, 3, 0, 4, 3, 0, ...? Average = 7/3 ≈ 2.33. Worse than 3.

Pattern: 4, 2, 1, 4, 2, 1, ...? Need to check compatibility. Average = 7/3. Still worse.

Hmm. What about using columns with 3 black cells but not {1,3,5}?

3-element subsets with V=1 (one vertical pair): {1,2,4}, {1,2,5}, {1,3,4}, {1,4,5}, {2,3,5}, {2,4,5}.
3-element subsets with V=2 (two vertical pairs): {1,2,3}, {2,3,4}, {3,4,5}.
3-element subset with V=0: {1,3,5} only.

For a column with 3 black cells and V=1, say S = {1,2,4}:
- Cell (1,c): vertical [2∈S]=1. Horizontal [1∈A]+[1∈C] ≤ 1.
- Cell (2,c): vertical [1∈S]+[3∈S] = 1+0 = 1. Horizontal [2∈A]+[2∈C] ≤ 1.
- Cell (3,c) (white): vertical [2∈S]+[4∈S] = 1+1 = 2. Horizontal [3∈A]+[3∈C] = 0. So 3∉A, 3∉C.
- Cell (4,c): vertical [3∈S]+[5∈S] = 0. Horizontal [4∈A]+[4∈C] ≤ 2.
- Cell (5,c) (white): vertical [4∈S] = 1. Horizontal [5∈A]+[5∈C] ≤ 1.

So A, C cannot contain 3. A, C ⊆ {1,2,4,5} with constraints: [1∈A]+[1∈C] ≤ 1, [2∈A]+[2∈C] ≤ 1, [5∈A]+[5∈C] ≤ 1. And [4∈A]+[4∈C] ≤ 2 (no constraint from row 4).

So |A| + |C| ≤ 1+1+2+1 = 5. But also A, C ⊆ {1,2,4,5} (4 elements), so |A| ≤ 4, |C| ≤ 4.

Can we have |A| = 3, |C| = 2? Or |A| = |C| = 2?

Let me try a repeating pattern with S = {1,2,4}. Then A = C = {1,2,4} (same state).

Check: A = C = {1,2,4}, S = {1,2,4}.
- Row 1: [2∈S]=1, [1∈A]+[1∈C] = 1+1 = 2. Total = 3. Violates!

So we can't have the same state repeat. Let me try A = {1,4,5}, S = {1,2,4}, C = {2,4,5}.

Check constraints on S with A on left, C on right:
- Row 1: [2∈S]=1, [1∈A]=1, [1∈C]=0. Total=2. ✓
- Row 2: [1∈S]+[3∈S]=1, [2∈A]=0, [2∈C]=1. Total=2. ✓
- Row 3 (white): [2∈S]+[4∈S]=2, [3∈A]+[3∈C]=0. Total=2. ✓
- Row 4: [3∈S]+[5∈S]=0, [4∈A]=1, [4∈C]=1. Total=2. ✓
- Row 5 (white): [4∈S]=1, [5∈A]=1, [5∈C]=1. Total=3. Violates!

Row 5 has 3 black neighbors. Bad.

Let me try A = {1,4,5}, S = {1,2,4}, C = {2,4}.

- Row 5 (white): [4∈S]=1, [5∈A]=1, [5∈C]=0. Total=2. ✓
- Row 1: [2∈S]=1, [1∈A]=1, [1∈C]=0. Total=2. ✓
- Row 2: [1∈S]+[3∈S]=1, [2∈A]=0, [2∈C]=1. Total=2. ✓
- Row 3 (white): 2+0=2. ✓
- Row 4: [3∈S]+[5∈S]=0, [4∈A]=1, [4∈C]=1. Total=2. ✓

So A={1,4,5}, S={1,2,4}, C={2,4} works for the middle column. But now I need to check the constraints on A and C as well, which depend on their neighbors.

This is getting very complex. Let me try a computational approach mentally — think about what the maximum average column density could be.

Let me think about it differently. Let me consider the constraint from the perspective of "each cell has at most 2 black neighbors" and try to find an upper bound.

Consider partitioning the grid into 2×2 blocks. There are 2×99 = 198 such blocks (2 ways to partition rows: {1,2},{3,4} or {2,3},{4,5}; and 99 column pairs). Actually, let me think about overlapping 2×2 blocks.

Hmm, let me try a different counting approach.

Consider the "L-shaped" or other structures.

Actually, let me think about the problem as a linear programming relaxation. 

Variables: x_{r,c} ∈ {0,1} for each cell.
Constraint: for each cell (r,c), sum of x over neighbors ≤ 2.
Maximize: sum of x.

The LP relaxation: x ∈ [0,1], same constraints. The LP optimum is an upper bound on the IP optimum.

For the LP, by symmetry and the structure, the optimal might be x = 3/5 for all cells, giving 500 × 3/5 = 300. Let me check: if all x = 3/5, each interior cell has 4 × 3/5 = 12/5 = 2.4 > 2. Violates!

So uniform 3/5 doesn't satisfy the LP. The LP bound might be different.

Hmm wait, the {1,3,5} pattern gives exactly 300 and satisfies all constraints. Let me see if the LP can do better.

Actually, let me think about the dual LP. The dual is: minimize 2 × Σ y_v subject to for each cell u, Σ_{v ~ u} y_v ≥ 1 (for black cells) ... hmm, this isn't quite right because the constraint is on all cells, not just black ones.

Let me re-formulate. Primal:
max Σ x_v
s.t. for each cell v: Σ_{u ~ v} x_u ≤ 2
     x_v ∈ [0,1]

Dual:
min 2 Σ y_v
s.t. for each cell u: Σ_{v ~ u} y_v ≥ 1
     y_v ≥ 0

The dual says: assign non-negative weights y_v to cells such that for each cell u, the sum of weights of its neighbors is ≥ 1. Minimize 2 Σ y_v.

If we can find a dual solution with 2 Σ y_v = 300, then 300 is optimal.

Try y_v = 1/2 for all cells. Then for each interior cell u, Σ_{v~u} y_v = 4 × 1/2 = 2 ≥ 1. ✓ For edge cells: 3 × 1/2 = 1.5 ≥ 1. ✓ For corner cells: 2 × 1/2 = 1 ≥ 1. ✓.

2 Σ y_v = 2 × 500 × 1/2 = 500. So this gives an upper bound of 500. Not tight.

Try y_v = 1/4 for all cells. Interior: 4 × 1/4 = 1 ≥ 1. ✓. Edge: 3 × 1/4 = 3/4 < 1. ✗.

So uniform 1/4 doesn't work for edge/corner cells. We need higher weights on edge/corner cells.

Let me try: y_v = 1/4 for interior cells, y_v = 1/3 for edge cells, y_v = 1/2 for corner cells.

Interior cell u: neighbors are 4 interior/edge cells. If u is truly interior (not adjacent to border), all 4 neighbors have y ≥ 1/4, so sum ≥ 1. ✓.

But cells adjacent to the border have some neighbors that are edge/corner cells. Let me be more careful.

Actually, the grid is 5×100. Let me think about which cells are interior (4 neighbors), edge (3 neighbors), corner (2 neighbors).

Corner cells: (1,1), (1,100), (5,1), (5,100). 4 corners.
Edge cells on top/bottom rows (rows 1 and 5, columns 2-99): 2 × 98 = 196.
Edge cells on left/right columns (rows 2-4, columns 1 and 100): 3 × 2 = 6.
Interior cells: 500 - 4 - 196 - 6 = 294.

For the dual, let me try to find a good assignment.

Actually, let me think about this differently. The 5×100 grid is "thin" (only 5 rows). Let me think about the column structure.

Let me try a dual solution based on columns. Assign weights based on row position.

Let y_{r,c} = a_r for all c (same weight for each row). Then for cell (r,c) in an interior column:
Σ_{v~(r,c)} y_v = a_{r-1} + a_{r+1} + a_r + a_r = a_{r-1} + a_{r+1} + 2a_r (for interior rows 2,3,4).
For row 1: a_2 + 2a_1 (only right neighbor in same column is... wait.

Wait, cell (r,c) neighbors: (r-1,c), (r+1,c), (r,c-1), (r,c+1). With y_{r,c} = a_r:
- For interior column c (2 ≤ c ≤ 99) and interior row r (2 ≤ r ≤ 4): sum = a_{r-1} + a_{r+1} + a_r + a_r = a_{r-1} + a_{r+1} + 2a_r.
- For row 1, interior column: a_2 + a_1 + a_1 = a_2 + 2a_1. (No row 0.)
- For row 5, interior column: a_4 + 2a_5.
- For edge column (c=1 or c=100), interior row: a_{r-1} + a_{r+1} + a_r. (Only one horizontal neighbor.)
- For corner (1,1): a_2 + a_1.

We need all these ≥ 1.

For interior columns:
- Row 1: a_2 + 2a_1 ≥ 1
- Row 2: a_1 + a_3 + 2a_2 ≥ 1
- Row 3: a_2 + a_4 + 2a_3 ≥ 1
- Row 4: a_3 + a_5 + 2a_4 ≥ 1
- Row 5: a_4 + 2a_5 ≥ 1

For edge columns (c=1, c=100):
- Row 1 (corner): a_2 + a_1 ≥ 1
- Row 2: a_1 + a_3 + a_2 ≥ 1
- Row 3: a_2 + a_4 + a_3 ≥ 1
- Row 4: a_3 + a_5 + a_4 ≥ 1
- Row 5 (corner): a_4 + a_5 ≥ 1

We want to minimize 2 × Σ y_v = 2 × 100 × (a_1 + a_2 + a_3 + a_4 + a_5).

The edge column constraints are tighter (one fewer neighbor). To satisfy both interior and edge column constraints, we need the edge column constraints to hold, which are stricter.

Edge column constraints:
1. a_1 + a_2 ≥ 1
2. a_1 + a_2 + a_3 ≥ 1 (implied by 1)
3. a_2 + a_3 + a_4 ≥ 1
4. a_3 + a_4 + a_5 ≥ 1
5. a_4 + a_5 ≥ 1

And interior column constraints:
1'. a_2 + 2a_1 ≥ 1
2'. a_1 + a_3 + 2a_2 ≥ 1
3'. a_2 + a_4 + 2a_3 ≥ 1
4'. a_3 + a_5 + 2a_4 ≥ 1
5'. a_4 + 2a_5 ≥ 1

By symmetry (rows 1↔5, 2↔4), let's try a_1 = a_5, a_2 = a_4.

Then:
Edge: a_1 + a_2 ≥ 1, a_2 + a_3 + a_2 ≥ 1 → 2a_2 + a_3 ≥ 1, a_1 + a_2 ≥ 1 (same as first).
Interior: a_2 + 2a_1 ≥ 1, a_1 + a_3 + 2a_2 ≥ 1, 2a_2 + 2a_3 ≥ 1 (from row 3: a_2 + a_2 + 2a_3), a_1 + a_3 + 2a_2 ≥ 1 (same as row 2), a_2 + 2a_1 ≥ 1 (same as row 1).

So constraints:
- a_1 + a_2 ≥ 1 (edge, rows 1&5)
- 2a_2 + a_3 ≥ 1 (edge, row 3)
- a_2 + 2a_1 ≥ 1 (interior, rows 1&5)
- a_1 + a_3 + 2a_2 ≥ 1 (interior, rows 2&4)
- a_2 + a_3 ≥ 1/2 (interior, row 3: 2a_2 + 2a_3 ≥ 1)

Minimize 2 × 100 × (2a_1 + 2a_2 + a_3) = 200(2a_1 + 2a_2 + a_3).

Note: a_1 + a_2 ≥ 1 and a_2 + 2a_1 ≥ 1. The first gives a_1 ≥ 1 - a_2. The second gives a_1 ≥ (1 - a_2)/2. Since 1 - a_2 ≥ (1 - a_2)/2 (when a_2 ≤ 1), the binding constraint is a_1 + a_2 ≥ 1, i.e., a_1 ≥ 1 - a_2.

Also 2a_2 + a_3 ≥ 1 gives a_3 ≥ 1 - 2a_2.
And a_1 + a_3 + 2a_2 ≥ 1: (1 - a_2) + a_3 + 2a_2 = 1 + a_2 + a_3 ≥ 1, always satisfied if a_2, a_3 ≥ 0.
And a_2 + a_3 ≥ 1/2.

So the binding constraints are:
- a_1 ≥ 1 - a_2 (from a_1 + a_2 ≥ 1)
- a_3 ≥ max(1 - 2a_2, 1/2 - a_2) (from 2a_2 + a_3 ≥ 1 and a_2 + a_3 ≥ 1/2)

For a_2 ≤ 1/2: 1 - 2a_2 ≥ 1/2 - a_2 (since 1 - 2a_2 - (1/2 - a_2) = 1/2 - a_2 ≥ 0). So a_3 ≥ 1 - 2a_2.
For a_2 ≥ 1/2: 1 - 2a_2 ≤ 0, and 1/2 - a_2 ≤ 0, so a_3 ≥ 0.

Objective: 200(2a_1 + 2a_2 + a_3) = 200(2(1 - a_2) + 2a_2 + a_3) = 200(2 + a_3) when a_1 = 1 - a_2.

Wait, 2a_1 + 2a_2 = 2(1-a_2) + 2a_2 = 2. So objective = 200(2 + a_3).

To minimize, minimize a_3.

For a_2 ≤ 1/2: a_3 ≥ 1 - 2a_2. Minimize a_3 = 1 - 2a_2, achieved at a_2 = 1/2, giving a_3 = 0.
For a_2 ≥ 1/2: a_3 ≥ 0. Minimize a_3 = 0.

At a_2 = 1/2: a_1 = 1 - 1/2 = 1/2, a_3 = 0, a_4 = 1/2, a_5 = 1/2.

Objective = 200(2 + 0) = 400. So the dual gives 400. Not tight (300 < 400).

Hmm, so this dual solution gives 400, not 300. The uniform-by-row dual isn't tight enough.

Let me try a different dual solution. Maybe non-uniform across columns.

Actually, let me think about whether 300 is really optimal. Maybe we can do better than 300.

Let me try to construct a pattern with density > 3/5.

Idea: Use a pattern where some columns have 4 black cells and others have 2, averaging > 3.

From the analysis above, a column with 4 black cells (say {1,2,3,4}) forces its neighbors to not contain rows 2,3, and at most one neighbor contains row 1, at most one contains row 4, at most one contains row 5. So neighbors ⊆ {1,4,5} with |A ∩ {1}| + |C ∩ {1}| ≤ 1, etc.

If S = {1,2,3,4}, the best neighbors: A = {1,4,5}, C = {} (or vice versa). Then |A| + |C| = 3. Over 3 columns: 4 + 3 + 0 = 7, average 7/3 ≈ 2.33.

Or A = {4,5}, C = {1}: |A|+|C| = 3. Same.

Or A = {1,5}, C = {4}: |A|+|C| = 3. Same.

What if S = {1,2,4,5}? (V = 2: pairs (1,2) and (4,5))

- Cell (1,c): vertical [2∈S]=1. Horizontal [1∈A]+[1∈C] ≤ 1.
- Cell (2,c): vertical [1∈S]+[3∈S]=1. Horizontal [2∈A]+[2∈C] ≤ 1.
- Cell (3,c) (white): vertical [2∈S]+[4∈S]=2. Horizontal [3∈A]+[3∈C]=0. So 3∉A, 3∉C.
- Cell (4,c): vertical [3∈S]+[5∈S]=1. Horizontal [4∈A]+[4∈C] ≤ 1.
- Cell (5,c): vertical [4∈S]=1. Horizontal [5∈A]+[5∈C] ≤ 1.

So A, C ⊆ {1,2,4,5} (not 3). Constraints: for each r ∈ {1,2,4,5}, [r∈A]+[r∈C] ≤ 1. So |A| + |C| ≤ 4.

Best case: |A| = 2, |C| = 2. Over 3 columns: 4 + 2 + 2 = 8, average 8/3 ≈ 2.67. Still less than 3.

Or |A| = 3, |C| = 1: 4 + 3 + 1 = 8, same average.

What about a pattern with all columns having 3 black cells but different from {1,3,5}?

We showed that {1,3,5} is rigid (locks neighbors to subsets of {1,3,5}). What about other 3-element subsets?

Let me try S = {1,2,4} (V=1).

From earlier: A, C ⊆ {1,2,4,5} (not 3). Constraints: [1∈A]+[1∈C] ≤ 1, [2∈A]+[2∈C] ≤ 1, [5∈A]+[5∈C] ≤ 1. No constraint on row 4 (other than ≤ 2).

So for row 4: [4∈A]+[4∈C] ≤ 2. So both A and C can contain 4.

Best case for |A|+|C|: rows 1,2,5 each contribute at most 1 total, row 4 contributes at most 2. So |A|+|C| ≤ 1+1+2+1 = 5. With |A|, |C| ≤ 4 (since ⊆ {1,2,4,5}).

Can we have |A| = 3, |C| = 2? E.g., A = {1,4,5}, C = {2,4}.

Check: [1∈A]+[1∈C] = 1+0 = 1 ✓. [2∈A]+[2∈C] = 0+1 = 1 ✓. [5∈A]+[5∈C] = 1+0 = 1 ✓. [4∈A]+[4∈C] = 1+1 = 2 ✓.

So A={1,4,5}, S={1,2,4}, C={2,4}. Over 3 columns: 3+3+2 = 8, average 8/3 ≈ 2.67. Still less than 3.

But wait, can we chain this? If the pattern is A, S, C, A, S, C, ... with A={1,4,5}, S={1,2,4}, C={2,4}?

We need to check that C={2,4} is compatible with the next A={1,4,5}.

For column C={2,4} with left neighbor S={1,2,4} and right neighbor A={1,4,5}:
- Row 1 (white): vertical [2∈C]=1. Horizontal [1∈S]+[1∈A] = 1+1 = 2. Total = 3. Violates!

So this doesn't chain. The issue is row 1 is white in C but black in both neighbors.

Let me try to find a chainable pattern. 

Let me think about this more carefully. I want a periodic pattern with period p where the average column density is > 3.

Let me try period 2: states A, B alternating.

Constraints on A (with B on both sides):
For each row r: [r-1∈A] + [r+1∈A] + 2[r∈B] ≤ 2.

Constraints on B (with A on both sides):
For each row r: [r-1∈B] + [r+1∈B] + 2[r∈A] ≤ 2.

We want to maximize (|A| + |B|)/2.

From the constraint on A: 2[r∈B] ≤ 2 - [r-1∈A] - [r+1∈A].
If r ∈ A and (r-1 ∈ A or r+1 ∈ A): then [r-1∈A]+[r+1∈A] ≥ 1, so 2[r∈B] ≤ 1, meaning r ∉ B.
If r ∈ A and neither r-1 nor r+1 ∈ A: 2[r∈B] ≤ 2, so r can be in B.

Similarly from constraint on B.

Let me enumerate. Let A and B be subsets of {1,2,3,4,5}.

Case 1: A = {1,3,5} (V=0). Then for each r ∈ A, r-1 and r+1: 
- r=1: r-1 doesn't exist, r+1=2 ∉ A. So [r-1∈A]+[r+1∈A] = 0. 2[r∈B] ≤ 2, so 1 can be in B.
- r=3: r-1=2 ∉ A, r+1=4 ∉ A. Sum = 0. 3 can be in B.
- r=5: r-1=4 ∉ A, sum = 0. 5 can be in B.
For r ∉ A (r=2,4):
- r=2: [1∈A]+[3∈A] = 2. 2[2∈B] ≤ 0. So 2 ∉ B.
- r=4: [3∈A]+[5∈A] = 2. So 4 ∉ B.
So B ⊆ {1,3,5}. And from the B constraint: for r ∈ B, [r-1∈B]+[r+1∈B] + 2[r∈A] ≤ 2. If r ∈ B ∩ A, then 2[r∈A] = 2, so [r-1∈B]+[r+1∈B] = 0. So no two adjacent elements of {1,3,5} can both be in B (but 1,3,5 are not adjacent in rows, so this is automatically satisfied). Actually, [r-1∈B] means row r-1, which for r=3 is row 2, and 2 ∉ B. So [r-1∈B]+[r+1∈B] = 0 for all r ∈ {1,3,5}. So B can be any subset of {1,3,5}.

Max |A|+|B| = 3 + 3 = 6, average 3. Same as {1,3,5} everywhere.

Case 2: A = {1,2,4} (V=1). 
Constraint on A (B on both sides):
- r=1: [2∈A]=1. 2[1∈B] ≤ 1. So 1 ∉ B.
- r=2: [1∈A]+[3∈A]=1. 2[2∈B] ≤ 1. So 2 ∉ B.
- r=3 (white): [2∈A]+[4∈A]=2. 2[3∈B] ≤ 0. 3 ∉ B.
- r=4: [3∈A]+[5∈A]=0. 2[4∈B] ≤ 2. 4 can be in B.
- r=5 (white): [4∈A]=1. 2[5∈B] ≤ 1. 5 ∉ B.
So B ⊆ {4}. |B| ≤ 1.

Constraint on B (A on both sides): B ⊆ {4}.
- r=4: [3∈B]+[5∈B]=0. 2[4∈A]=2. Total = 2. ✓.
So B = {4} or B = {}.

|A|+|B| = 3 + 1 = 4, average 2. Worse.

Case 3: A = {1,2,3} (V=2).
- r=1: [2∈A]=1. 2[1∈B] ≤ 1. 1 ∉ B.
- r=2: [1∈A]+[3∈A]=2. 2[2∈B] ≤ 0. 2 ∉ B.
- r=3: [2∈A]+[4∈A]=1. 2[3∈B] ≤ 1. 3 ∉ B.
- r=4 (white): [3∈A]+[5∈A]=1. 2[4∈B] ≤ 1. 4 ∉ B.
- r=5 (white): [4∈A]=0. 2[5∈B] ≤ 2. 5 can be in B.
So B ⊆ {5}. |B| ≤ 1. Average = (3+1)/2 = 2. Worse.

Case 4: A = {1,3,4} (V=1, pair (3,4)).
- r=1: [2∈A]=0. 2[1∈B] ≤ 2. 1 can be in B.
- r=2 (white): [1∈A]+[3∈A]=2. 2[2∈B] ≤ 0. 2 ∉ B.
- r=3: [2∈A]+[4∈A]=1. 2[3∈B] ≤ 1. 3 ∉ B.
- r=4: [3∈A]+[5∈A]=1. 2[4∈B] ≤ 1. 4 ∉ B.
- r=5 (white): [4∈A]=1. 2[5∈B] ≤ 1. 5 ∉ B.
So B ⊆ {1}. |B| ≤ 1.

Constraint on B (A on both sides), B={1}:
- r=1: [2∈B]=0. 2[1∈A]=2. Total=2. ✓.
So B = {1}. |A|+|B| = 3+1 = 4, average 2. Worse.

Case 5: A = {2,4} (V=0, non-adjacent).
- r=1 (white): [2∈A]=1. 2[1∈B] ≤ 1. 1 ∉ B.
- r=2: [1∈A]+[3∈A]=0. 2[2∈B] ≤ 2. 2 can be in B.
- r=3 (white): [2∈A]+[4∈A]=2. 2[3∈B] ≤ 0. 3 ∉ B.
- r=4: [3∈A]+[5∈A]=0. 2[4∈B] ≤ 2. 4 can be in B.
- r=5 (white): [4∈A]=1. 2[5∈B] ≤ 1. 5 ∉ B.
So B ⊆ {2,4}. 

Constraint on B (A on both sides), B ⊆ {2,4}:
- r=2: [1∈B]+[3∈B]=0. 2[2∈A]=2. Total=2. ✓.
- r=4: [3∈B]+[5∈B]=0. 2[4∈A]=2. Total=2. ✓.
So B can be {2}, {4}, {2,4}, or {}.

Max |A|+|B| = 2+2 = 4, average 2. Worse.

Case 6: A = {1,4} (V=0).
- r=1: [2∈A]=0. 2[1∈B] ≤ 2. 1 ∈ B ok.
- r=2 (white): [1∈A]+[3∈A]=1. 2[2∈B] ≤ 1. 2 ∉ B.
- r=3 (white): [2∈A]+[4∈A]=1. 2[3∈B] ≤ 1. 3 ∉ B.
- r=4: [3∈A]+[5∈A]=0. 2[4∈B] ≤ 2. 4 ∈ B ok.
- r=5 (white): [4∈A]=1. 2[5∈B] ≤ 1. 5 ∉ B.
B ⊆ {1,4}.

Constraint on B, B ⊆ {1,4}:
- r=1: [2∈B]=0. 2[1∈A]=2. Total=2. ✓.
- r=4: [3∈B]+[5∈B]=0. 2[4∈A]=2. Total=2. ✓.
B can be {1,4}. |A|+|B| = 2+2 = 4, average 2.

Case 7: A = {1,2,4,5} (V=2).
- r=1: [2∈A]=1. 2[1∈B] ≤ 1. 1 ∉ B.
- r=2: [1∈A]+[3∈A]=1. 2[2∈B] ≤ 1. 2 ∉ B.
- r=3 (white): [2∈A]+[4∈A]=2. 3 ∉ B.
- r=4: [3∈A]+[5∈A]=1. 4 ∉ B.
- r=5: [4∈A]=1. 5 ∉ B.
B = {}. |A|+|B| = 4. Average 2.

Case 8: A = {1,2,5} (V=1, pair (1,2)).
- r=1: [2∈A]=1. 1 ∉ B.
- r=2: [1∈A]+[3∈A]=1. 2 ∉ B.
- r=3 (white): [2∈A]+[4∈A]=1. 2[3∈B] ≤ 1. 3 ∉ B.
- r=4 (white): [3∈A]+[5∈A]=1. 2[4∈B] ≤ 1. 4 ∉ B.
- r=5: [4∈A]=0. 2[5∈B] ≤ 2. 5 ∈ B ok.
B ⊆ {5}. |A|+|B| ≤ 3+1 = 4. Average 2.

It seems like for period 2, the best we can do is average 3 (with the {1,3,5} pattern). Let me check a few more.

Case 9: A = {1,3,5}, B = {1,3,5}. |A|+|B| = 6, average 3. This is the {1,3,5} pattern (same state).

Case 10: A = {2,4}, B = {1,3,5}.
Check constraint on A={2,4} (B={1,3,5} on both sides):
- r=1 (white): [2∈A]=1. 2[1∈B] = 2. Total = 3. Violates!

Nope.

Case 11: A = {1,3,5}, B = {2,4}.
Constraint on A (B on both sides):
- r=2 (white): [1∈A]+[3∈A]=2. 2[2∈B]=2. Total=4. Violates!

Nope.

So for period 2, the maximum average is 3, achieved only by {1,3,5} repeated.

Let me try period 3.

States A, B, C repeating. Constraints:
- Column A (B on left, C on right): [r-1∈A]+[r+1∈A]+[r∈B]+[r∈C] ≤ 2 for all r.
- Column B (C on left, A on right): [r-1∈B]+[r+1∈B]+[r∈C]+[r∈A] ≤ 2.
- Column C (A on left, B on right): [r-1∈C]+[r+1∈C]+[r∈A]+[r∈B] ≤ 2.

We want to maximize (|A|+|B|+|C|)/3.

This is more flexible. Let me try A = {1,2,3}, B = {3,4,5}, C = {1,3,5}? No wait, let me be systematic.

Hmm, actually, let me try A = {1,2,3}, B = {}, C = {3,4,5}. Average = 6/3 = 2. Bad.

Let me try to think about what patterns could work.

For the constraint on column A: [r-1∈A]+[r+1∈A]+[r∈B]+[r∈C] ≤ 2.

If A = {1,3,5} (no vertical pairs), then [r-1∈A]+[r+1∈A] = 0 for all r (since 1,3,5 are non-adjacent). So [r∈B]+[r∈C] ≤ 2 for all r. This is always satisfied. But also, for r ∉ A (r=2,4): [r-1∈A]+[r+1∈A] = 2, so [r∈B]+[r∈C] = 0. So 2 ∉ B, 2 ∉ C, 4 ∉ B, 4 ∉ C. So B, C ⊆ {1,3,5}.

Then for column B: [r-1∈B]+[r+1∈B]+[r∈C]+[r∈A] ≤ 2. For r ∈ {1,3,5}: [r∈A] = 1, so [r-1∈B]+[r+1∈B]+[r∈C] ≤ 1. Since B, C ⊆ {1,3,5} and elements of {1,3,5} are non-adjacent, [r-1∈B]+[r+1∈B] = 0 (r-1 and r+1 are even, not in {1,3,5}). So [r∈C] ≤ 1, always true.

So if A = {1,3,5}, then B, C ⊆ {1,3,5}, and all constraints are satisfied. Max |A|+|B|+|C| = 9, average 3.

So period 3 with {1,3,5} also gives average 3.

Can we do better with period 3 using non-{1,3,5} states?

Let me try A = {1,2,4}, B = {1,4,5}, C = {2,4,5}. Hmm, let me just check.

Actually, this is getting really tedious. Let me think about it from a higher level.

Key observation: In any valid configuration, consider the white cells. Each interior white cell has at least 2 white neighbors. This means white cells form a structure where interior white cells have degree ≥ 2 in the white subgraph.

Hmm, let me think about this differently. Let me consider the problem row by row.

Actually, let me think about a cleaner upper bound argument.

Consider the 5×100 grid. Look at 2×1 dominoes (vertical pairs). There are 4×100 = 400 vertical dominoes (pairs (r,c),(r+1,c) for r=1..4, c=1..100).

For each vertical domino, if both cells are black, that's a "black vertical pair." The number of such pairs is V.

Now, consider a cell (r,c) that is black. Its black neighbors include vertical and horizontal. The constraint says ≤ 2 total.

Hmm, I don't see a clean argument yet. Let me try to think about it computationally — maybe the answer is 300, or maybe it's higher.

Let me try a specific construction that might beat 300.

Construction: Use a "zigzag" pattern. In odd columns, black cells at rows {1,2,3}. In even columns, black cells at rows {3,4,5}.

We already checked this: cell (3, odd) has 3 black neighbors. Violates.

What about: odd columns {1,2,3}, even columns {1,2,3} but with some modification?

{1,2,3} in all columns: 
- Cell (2,c): [1∈S]+[3∈S]+[2∈S_{c-1}]+[2∈S_{c+1}] = 1+1+1+1 = 4. Violates badly.

What about a "checkerboard" on top of stripes?

Let me try: columns alternate between {1,2,3} and {4,5}.

Odd: {1,2,3}, Even: {4,5}.
- Column odd, cell (3,c): [2∈S]+[4∈S]+[3∈even]+[3∈even] = 1+0+0+0 = 1. ✓
- Cell (2,c) in odd: [1∈S]+[3∈S]+[2∈even]+[2∈even] = 1+1+0+0 = 2. ✓
- Cell (1,c) in odd: [2∈S]+[1∈even]+[1∈even] = 1+0+0 = 1. ✓
- Column even, cell (4,c): [3∈S]+[5∈S]+[4∈odd]+[4∈odd] = 0+1+0+0 = 1. ✓
- Cell (5,c) in even: [4∈S]+[5∈odd]+[5∈odd] = 1+0+0 = 1. ✓
- Cell (3,c) in even (white): [2∈S]+[4∈S]+[3∈odd]+[3∈odd] = 0+1+1+1 = 3. Violates!

Cell (3, even) has neighbors (2,even) white, (4,even) black, (3,odd) black, (3,odd) black. 3 black. Violates.

What about odd: {1,2,3}, even: {4,5} but with column 3 (the shared row) handled?

The issue is row 3 is black in odd columns, and row 4 is black in even columns, so cell (3, even) sees row 3 black in both adjacent odd columns plus row 4 black in its own column.

What if we separate them more? Odd: {1,2}, even: {4,5}. Then row 3 is always white.

- Cell (3,c) (always white): [2∈S_c]+[4∈S_c]+[3∈S_{c-1}]+[3∈S_{c+1}]. 
  - In odd column: [2∈{1,2}]+[4∈{1,2}]+0+0 = 1+0 = 1. ✓
  - In even column: [2∈{4,5}]+[4∈{4,5}]+0+0 = 0+1 = 1. ✓
- Cell (2,c) in odd: [1∈S]+[3∈S]+[2∈even]+[2∈even] = 1+0+0+0 = 1. ✓
- Cell (1,c) in odd: [2∈S]+[1∈even]+[1∈even] = 1+0+0 = 1. ✓
- Cell (4,c) in even: [3∈S]+[5∈S]+[4∈odd]+[4∈odd] = 0+1+0+0 = 1. ✓
- Cell (5,c) in even: [4∈S]+[5∈odd]+[5∈odd] = 1+0+0 = 1. ✓

This works! n = 50×2 + 50×2 = 200. But that's less than 300.

Can we add row 3 to some columns? If we add row 3 to odd columns: odd becomes {1,2,3}.

- Cell (3,c) in odd: [2∈S]+[4∈S]+[3∈even]+[3∈even] = 1+0+0+0 = 1. ✓
- Cell (2,c) in odd: [1∈S]+[3∈S]+[2∈even]+[2∈even] = 1+1+0+0 = 2. ✓
- Cell (3,c) in even (white): [2∈S]+[4∈S]+[3∈odd]+[3∈odd] = 0+1+1+1 = 3. Violates!

Same issue as before. Cell (3, even) sees row 3 black in both adjacent odd columns.

What if we add row 3 only to every other odd column? Like a period-4 pattern: {1,2,3}, {4,5}, {1,2}, {4,5,3}?

Hmm, let me think about this differently. Let me try period 4: A, B, C, D.

Actually, let me try a different approach. Let me think about what the answer might be and try to prove it.

Given the {1,3,5} construction gives 300, and I haven't found anything better, let me hypothesize the answer is 300 and try to prove it.

But wait, let me try one more construction. What about a "staircase" pattern?

Columns: c mod 5 gives the pattern. Let me try:
- c ≡ 0: {1,2,3}
- c ≡ 1: {2,3,4}
- c ≡ 2: {3,4,5}
- c ≡ 3: {1,2,3}
- c ≡ 4: {2,3,4}

Wait, this has overlapping row 3 everywhere. Let me check cell (3, c≡0): [2∈S]+[4∈S]+[3∈prev]+[3∈next] = 1+1+[3∈{2,3,4}]+[3∈{2,3,4}] = 2+1+1 = 4. Violates.

The problem is row 3 is in too many columns.

Let me try a "sliding window" that avoids overlap:
- c ≡ 0: {1,2,3}
- c ≡ 1: {3,4,5}
- c ≡ 2: {1,2,3}
- c ≡ 3: {3,4,5}
...

This is period 2: {1,2,3}, {3,4,5}. We already checked: cell (3, {1,2,3} column) has [2∈S]+[4∈S]+[3∈{3,4,5}]+[3∈{3,4,5}] = 1+0+1+1 = 3. Violates.

The issue is row 3 is shared. What if we use:
- c ≡ 0: {1,2,3}
- c ≡ 1: {4,5}
- c ≡ 2: {1,2}
- c ≡ 3: {3,4,5}

Period 4: A={1,2,3}, B={4,5}, C={1,2}, D={3,4,5}.

Check column A (B on right, D on left for periodic):
Actually for a periodic pattern with period 4, column A has D on left and B on right.

Column A = {1,2,3}, left D = {3,4,5}, right B = {4,5}:
- r=1: [2∈A]=1, [1∈D]+[1∈B] = 0+0 = 0. Total=1. ✓
- r=2: [1∈A]+[3∈A]=2, [2∈D]+[2∈B]=0+0=0. Total=2. ✓
- r=3: [2∈A]+[4∈A]=1, [3∈D]+[3∈B]=1+0=1. Total=2. ✓
- r=4 (white): [3∈A]+[5∈A]=1, [4∈D]+[4∈B]=1+1=2. Total=3. Violates!

Cell (4, A) sees row 4 in D and B. Bad.

Let me try: A={1,2,3}, B={4,5}, C={1,2,3}, D={4,5}. Period 2 effectively. Already checked, doesn't work due to row 3.

Hmm. Let me try: A={1,2,3}, B={}, C={3,4,5}, D={}. Period 4, average 6/4 = 1.5. Bad.

Let me try a completely different approach. What about making some rows fully black and others fully white, but with a twist?

Rows 1, 3, 5 fully black, rows 2, 4 fully white: this is the {1,3,5} pattern, n=300.

What if rows 1, 2 are black in some columns and rows 4, 5 in others, with row 3 as a buffer?

Pattern: odd columns {1,2}, even columns {4,5}. We checked this works, n=200.

Can we add row 3 to some columns without violating?

If we add row 3 to an odd column (making it {1,2,3}):
- Cell (3, odd): [2∈S]+[4∈S]+[3∈even_left]+[3∈even_right] = 1+0+0+0 = 1. ✓
- Cell (2, odd): [1∈S]+[3∈S]+[2∈even_left]+[2∈even_right] = 1+1+0+0 = 2. ✓
- Cell (3, even_right) (white): [2∈S]+[4∈S]+[3∈odd]+[3∈next_odd] = 0+1+1+0 = 2. ✓ (if next odd doesn't have row 3)
- Cell (3, even_left) (white): [2∈S]+[4∈S]+[3∈prev_odd]+[3∈odd] = 0+1+0+1 = 2. ✓

So adding row 3 to a single odd column works if adjacent even columns' row 3 cells still have ≤ 2 black neighbors. Let me check more carefully.

If only one odd column (say column 1) has {1,2,3}, and all other odd columns have {1,2}, all even columns have {4,5}:

Column 1 = {1,2,3}, column 2 = {4,5}, column 3 = {1,2}, column 0 doesn't exist (column 1 is first).

Cell (3, 2) (even, white): [2∈{4,5}]+[4∈{4,5}]+[3∈col1]+[3∈col3] = 0+1+1+0 = 2. ✓
Cell (3, 1) (odd, black): [2∈col1]+[4∈col1]+[3∈col2] = 1+0+0 = 1. ✓ (no left neighbor since col 1 is first, or if not first, col 0 is even {4,5}, [3∈col0]=0)

What if we add row 3 to two consecutive odd columns? Say columns 1 and 3 both have {1,2,3}.

Cell (3, 2) (even, white): [2∈{4,5}]+[4∈{4,5}]+[3∈col1]+[3∈col3] = 0+1+1+1 = 3. Violates!

So we can't add row 3 to two odd columns that are separated by one even column. They need to be at least 2 even columns apart, i.e., odd columns at positions 1 and 5 (with columns 2,3,4 between, where 3 is odd with {1,2}).

Wait, columns 1, 3, 5 are odd. If columns 1 and 5 have row 3, column 3 doesn't:
Cell (3, 2): [3∈col1]+[3∈col3] = 1+0 = 1. Plus [4∈col2] = 1. Total = 2. ✓
Cell (3, 4): [3∈col3]+[3∈col5] = 0+1 = 1. Plus [4∈col4] = 1. Total = 2. ✓

So we can add row 3 to odd columns 1 and 5 (and 9, 13, ...) — every 4th odd column, i.e., every 8th column overall? No wait, odd columns are 1, 3, 5, 7, 9, ... Adding row 3 to columns 1, 5, 9, 13, ... (every 4th odd = every 8th column? No, 1, 5, 9 is every 4th column).

Wait, columns 1, 5, 9, ... are every 4th column. Between 1 and 5, we have columns 2 (even, {4,5}), 3 (odd, {1,2}), 4 (even, {4,5}). Cell (3,2): [3∈1]+[3∈3] = 1+0 = 1, +[4∈2] = 1, total 2. ✓. Cell (3,4): [3∈3]+[3∈5] = 0+1 = 1, +[4∈4] = 1, total 2. ✓. 

So we can add row 3 to every 4th odd column (columns 1, 5, 9, ...). There are 50 odd columns, so we can add row 3 to 50/4 ≈ 12 or 13 of them. That adds 12-13 black cells, giving n ≈ 212-213. Still way less than 300.

OK so this approach (base {1,2}/{4,5} + additions) is much worse than {1,3,5}.

Let me go back to the {1,3,5} pattern and see if we can modify it to add cells.

In {1,3,5}, every cell has exactly 2 black neighbors. The constraint is tight everywhere. To add a black cell, we need to change the configuration to make room.

What if we remove some cells and add others? For example, in some columns, replace {1,3,5} with {2,3,4} or something, and adjust neighbors.

This is like a local search. Let me think about whether there's a fundamentally different pattern with higher density.

Let me try to think about the LP relaxation more carefully. Maybe the LP bound is exactly 300, which would prove optimality.

Actually, let me think about a better dual solution. Instead of uniform by row, let me try a dual solution that's uniform by column but varies by row, and also accounts for edge effects.

Actually, the issue is that the grid is 5×100, which is very long and thin. The edge effects (top/bottom rows) are significant (2 out of 5 rows are edge rows), but the left/right edge effects are small (2 out of 100 columns).

Let me try a dual solution that's periodic in columns (ignoring left/right edges) and optimized for rows.

For an infinite 5×∞ grid, the dual is:
min 2 × (per-column weight) × ∞
s.t. for each cell, neighbor weights sum ≥ 1.

With y_{r,c} = a_r (row-dependent only):
- Row 1: a_2 + 2a_1 ≥ 1
- Row 2: a_1 + a_3 + 2a_2 ≥ 1
- Row 3: a_2 + a_4 + 2a_3 ≥ 1
- Row 4: a_3 + a_5 + 2a_4 ≥ 1
- Row 5: a_4 + 2a_5 ≥ 1

Minimize 2(a_1+a_2+a_3+a_4+a_5) per column.

By symmetry a_1=a_5, a_2=a_4:
- a_2 + 2a_1 ≥ 1
- a_1 + a_3 + 2a_2 ≥ 1
- 2a_2 + 2a_3 ≥ 1 → a_2 + a_3 ≥ 1/2

Minimize 2(2a_1 + 2a_2 + a_3).

From a_2 + 2a_1 ≥ 1: a_1 ≥ (1-a_2)/2.
From a_1 + a_3 + 2a_2 ≥ 1: a_3 ≥ 1 - a_1 - 2a_2.
From a_2 + a_3 ≥ 1/2: a_3 ≥ 1/2 - a_2.

Substituting a_1 = (1-a_2)/2:
a_3 ≥ 1 - (1-a_2)/2 - 2a_2 = 1 - 1/2 + a_2/2 - 2a_2 = 1/2 - 3a_2/2.
a_3 ≥ 1/2 - a_2.

For a_2 ≤ 0: not valid (a_2 ≥ 0).
For 0 ≤ a_2 ≤ 1/2: 1/2 - 3a_2/2 vs 1/2 - a_2. Since 3a_2/2 ≥ a_2, we have 1/2-3a_2/2 ≤ 1/2-a_2. So binding is a_3 ≥ 1/2 - a_2.
For a_2 ≥ 1/2: 1/2-3a_2/2 ≤ 0 and 1/2-a_2 ≤ 0, so a_3 ≥ 0.

Objective per column: 2(2·(1-a_2)/2 + 2a_2 + a_3) = 2(1-a_2 + 2a_2 + a_3) = 2(1 + a_2 + a_3).

Minimize 1 + a_2 + a_3.
For a_2 ≤ 1/2: a_3 = 1/2 - a_2. 1 + a_2 + 1/2 - a_2 = 3/2. Constant! So objective = 2 × 3/2 = 3 per column.
For a_2 ≥ 1/2: a_3 = 0. 1 + a_2 + 0 = 1 + a_2 ≥ 3/2. Worse.

So the minimum is 3 per column, achieved for any 0 ≤ a_2 ≤ 1/2 with a_1 = (1-a_2)/2, a_3 = 1/2 - a_2, a_4 = a_2, a_5 = (1-a_2)/2.

For example, a_2 = 0: a_1 = 1/2, a_2 = 0, a_3 = 1/2, a_4 = 0, a_5 = 1/2. This gives weight 1/2 to rows 1, 3, 5 and 0 to rows 2, 4. Per column: 3/2. Total dual: 2 × 100 × 3/2 = 300.

Wait, but this is for the infinite grid (ignoring left/right edge effects). For the actual 5×100 grid, the edge columns have fewer neighbors, so the dual constraints are tighter there. Let me check if this dual solution works for the actual grid.

With a_1 = 1/2, a_2 = 0, a_3 = 1/2, a_4 = 0, a_5 = 1/2:

For edge column (c=1), cell (r, 1): neighbors are (r-1,1), (r+1,1), (r,2). Sum of y = a_{r-1} + a_{r+1} + a_r.
- r=1: a_2 + a_1 = 0 + 1/2 = 1/2 < 1. Violates!

So the dual solution doesn't work for edge columns. We need to increase weights for edge columns.

Let me use a dual solution with higher weights on edge columns. Let y_{r,c} = a_r for interior columns (c=2..99) and y_{r,c} = b_r for edge columns (c=1, 100).

For interior column cell (r, c), c ∈ {2..99}: neighbors (r±1, c) and (r, c±1). 
- If c ∈ {3..98}: all neighbors are interior columns. Sum = a_{r-1} + a_{r+1} + 2a_r.
- If c = 2: neighbors (r±1, 2) and (r, 1), (r, 3). Sum = a_{r-1} + a_{r+1} + b_r + a_r.
- If c = 99: similarly a_{r-1} + a_{r+1} + a_r + b_r.

For edge column cell (r, 1): neighbors (r±1, 1) and (r, 2). Sum = b_{r-1} + b_{r+1} + a_r.

We need all these ≥ 1.

For c ∈ {3..98}: a_{r-1} + a_{r+1} + 2a_r ≥ 1 (same as before).
For c = 2 or 99: a_{r-1} + a_{r+1} + a_r + b_r ≥ 1.
For c = 1 or 100: b_{r-1} + b_{r+1} + a_r ≥ 1.

Objective: 2 × [98 × Σa_r + 2 × Σb_r] = 2 × [98 × (a_1+a_2+a_3+a_4+a_5) + 2 × (b_1+b_2+b_3+b_4+b_5)].

We want to minimize this. The interior column constraints require Σa_r ≥ 3/2 (from the infinite grid analysis, per column). So 98 × 3/2 = 147.

For the edge columns, we need b_r to satisfy:
- b_{r-1} + b_{r+1} + a_r ≥ 1 (edge column constraint)
- a_{r-1} + a_{r+1} + a_r + b_r ≥ 1 (column 2 constraint)

From the second: b_r ≥ 1 - a_{r-1} - a_{r+1} - a_r.
From the first: b_{r-1} + b_{r+1} ≥ 1 - a_r.

Let me use a_1 = 1/2, a_2 = 0, a_3 = 1/2, a_4 = 0, a_5 = 1/2.

Then:
b_r ≥ 1 - a_{r-1} - a_{r+1} - a_r:
- r=1: b_1 ≥ 1 - a_2 - a_1 = 1 - 0 - 1/2 = 1/2. (No a_0, so just a_2 + a_1... wait, for r=1, the column 2 constraint is a_2 + a_1 + b_1? No.

Wait, let me re-derive. For cell (r, 2), neighbors are (r-1, 2), (r+1, 2), (r, 1), (r, 3). Weights: a_{r-1} + a_{r+1} + b_r + a_r. (For r=1: a_0 doesn't exist, so it's a_2 + b_1 + a_1. For r=5: a_4 + b_5 + a_5.)

Let me redo:
- r=1: a_2 + b_1 + a_1 = 0 + b_1 + 1/2 ≥ 1 → b_1 ≥ 1/2.
- r=2: a_1 + a_3 + b_2 + a_2 = 1/2 + 1/2 + b_2 + 0 ≥ 1 → b_2 ≥ 0.
- r=3: a_2 + a_4 + b_3 + a_3 = 0 + 0 + b_3 + 1/2 ≥ 1 → b_3 ≥ 1/2.
- r=4: a_3 + a_5 + b_4 + a_4 = 1/2 + 1/2 + b_4 + 0 ≥ 1 → b_4 ≥ 0.
- r=5: a_4 + b_5 + a_5 = 0 + b_5 + 1/2 ≥ 1 → b_5 ≥ 1/2.

Edge column constraint (cell (r, 1)): b_{r-1} + b_{r+1} + a_r ≥ 1:
- r=1: b_2 + a_1 = b_2 + 1/2 ≥ 1 → b_2 ≥ 1/2.
- r=2: b_1 + b_3 + a_2 = b_1 + b_3 + 0 ≥ 1 → b_1 + b_3 ≥ 1.
- r=3: b_2 + b_4 + a_3 = b_2 + b_4 + 1/2 ≥ 1 → b_2 + b_4 ≥ 1/2.
- r=4: b_3 + b_5 + a_4 = b_3 + b_5 + 0 ≥ 1 → b_3 + b_5 ≥ 1.
- r=5: b_4 + a_5 = b_4 + 1/2 ≥ 1 → b_4 ≥ 1/2.

So combining:
- b_1 ≥ 1/2 (from column 2 constraint)
- b_2 ≥ 1/2 (from edge column constraint, r=1)
- b_3 ≥ 1/2 (from column 2 constraint)
- b_4 ≥ 1/2 (from edge column constraint, r=5)
- b_5 ≥ 1/2 (from column 2 constraint)
- b_1 + b_3 ≥ 1 (from edge, r=2). With b_1, b_3 ≥ 1/2, this is satisfied.
- b_3 + b_5 ≥ 1 (from edge, r=4). Similarly satisfied.
- b_2 + b_4 ≥ 1/2 (from edge, r=3). With b_2, b_4 ≥ 1/2, satisfied.

So minimum: b_1 = b_2 = b_3 = b_4 = b_5 = 1/2. Σb = 5/2.

Objective: 2 × [98 × 3/2 + 2 × 5/2] = 2 × [147 + 5] = 2 × 152 = 304.

Hmm, 304 > 300. So this dual solution gives 304, not 300. The edge effects add 4 to the bound.

But wait, maybe I can choose a different a_r to reduce the edge cost. Let me try to optimize the full objective.

Let me parameterize: a_1 = a_5 = α, a_2 = a_4 = β, a_3 = γ. With constraints:
- β + 2α ≥ 1 (interior, row 1)
- α + γ + 2β ≥ 1 (interior, row 2)
- 2β + 2γ ≥ 1 (interior, row 3) → β + γ ≥ 1/2

Objective (interior part): 98 × (2α + 2β + γ) × 2. Wait, the objective is 2 × [98 × (2α + 2β + γ) + 2 × (b_1+b_2+b_3+b_4+b_5)].

Let me also parameterize b_r. By symmetry b_1 = b_5 = p, b_2 = b_4 = q, b_3 = s.

Constraints from column 2 (cell (r, 2)):
- r=1: β + p + α ≥ 1 → p ≥ 1 - α - β
- r=2: α + γ + q + β ≥ 1 → q ≥ 1 - α - β - γ
- r=3: β + β + s + γ ≥ 1 → s ≥ 1 - 2β - γ. Wait, a_2 + a_4 + b_3 + a_3 = β + β + s + γ = 2β + s + γ ≥ 1 → s ≥ 1 - 2β - γ.
- r=4: γ + α + q + β ≥ 1 → q ≥ 1 - α - β - γ (same as r=2)
- r=5: β + p + α ≥ 1 → p ≥ 1 - α - β (same as r=1)

Constraints from edge column (cell (r, 1)):
- r=1: q + α ≥ 1 → q ≥ 1 - α
- r=2: p + s + β ≥ 1 → p + s ≥ 1 - β
- r=3: q + q + γ ≥ 1 → 2q + γ ≥ 1 → q ≥ (1 - γ)/2
- r=4: s + p + β ≥ 1 → p + s ≥ 1 - β (same as r=2)
- r=5: q + α ≥ 1 → q ≥ 1 - α (same as r=1)

So:
p ≥ max(1 - α - β, 0) [from column 2, and p ≥ 0]
q ≥ max(1 - α, 1 - α - β - γ, (1 - γ)/2, 0)
s ≥ max(1 - 2β - γ, 0)
p + s ≥ 1 - β

Objective: 2 × [98(2α + 2β + γ) + 2(2p + 2q + s)]

This is a complex optimization. Let me try to see if the total can be 300.

For the total to be 300: 98(2α + 2β + γ) + 2(2p + 2q + s) = 150.

If the interior part is minimized at 2α + 2β + γ = 3/2 (from the infinite grid analysis), then 98 × 3/2 = 147. So 2(2p + 2q + s) = 150 - 147 = 3, meaning 2p + 2q + s = 3/2.

With α = 1/2, β = 0, γ = 1/2 (the solution we found): 
p ≥ 1 - 1/2 - 0 = 1/2
q ≥ max(1 - 1/2, 1 - 1/2 - 0 - 1/2, (1 - 1/2)/2, 0) = max(1/2, 0, 1/4, 0) = 1/2
s ≥ max(1 - 0 - 1/2, 0) = 1/2
p + s ≥ 1 - 0 = 1. With p = s = 1/2, satisfied.

2p + 2q + s = 1 + 1 + 1/2 = 5/2. But we need 3/2. 5/2 > 3/2. So this doesn't achieve 300.

Can we choose different α, β, γ to reduce the edge cost while keeping interior cost at 3/2?

Let me try β = 1/4, α = 3/8 (from β + 2α ≥ 1: 1/4 + 3/4 = 1 ✓), γ = 1/4 (from β + γ ≥ 1/2: 1/4 + 1/4 = 1/2 ✓). Check α + γ + 2β = 3/8 + 1/4 + 1/2 = 3/8 + 2/8 + 4/8 = 9/8 ≥ 1 ✓.

2α + 2β + γ = 3/4 + 1/2 + 1/4 = 3/2. ✓ (interior cost still 3/2 per column).

Now edge costs:
p ≥ 1 - α - β = 1 - 3/8 - 1/4 = 1 - 3/8 - 2/8 = 3/8.
q ≥ max(1 - α, 1 - α - β - γ, (1-γ)/2) = max(1 - 3/8, 1 - 3/8 - 1/4 - 1/4, (1 - 1/4)/2) = max(5/8, 1/8, 3/8) = 5/8.
s ≥ max(1 - 2β - γ, 0) = max(1 - 1/2 - 1/4, 0) = 1/4.
p + s ≥ 1 - β = 3/4. With p = 3/8, s = 1/4: 3/8 + 1/4 = 5/8 < 3/4. Not satisfied! Need p + s ≥ 3/4.

So increase p or s. p + s = 3/4, with p ≥ 3/8, s ≥ 1/4. Minimize 2p + 2q + s = 2p + 2q + s. With q = 5/8 fixed, minimize 2p + s subject to p ≥ 3/8, s ≥ 1/4, p + s ≥ 3/4.

p + s = 3/4, so s = 3/4 - p. 2p + s = 2p + 3/4 - p = p + 3/4. Minimize by p = 3/8: 2p + s = 3/8 + 3/4 = 9/8. Then s = 3/4 - 3/8 = 3/8.

2p + 2q + s = 2(3/8) + 2(5/8) + 3/8 = 6/8 + 10/8 + 3/8 = 19/8.

Total: 98 × 3/2 + 2 × 19/8 = 147 + 19/4 = 147 + 4.75 = 151.75. Times 2 = 303.5. Worse than 304.

Hmm. Let me try β = 1/2, α = 0, γ = 0. Check: β + 2α = 1/2 ≥ 1? No, 1/2 < 1. Violates.

β = 1/2, α = 1/4: β + 2α = 1/2 + 1/2 = 1 ✓. γ: β + γ ≥ 1/2 → γ ≥ 0. α + γ + 2β = 1/4 + γ + 1 ≥ 1 ✓. 2α + 2β + γ = 1/2 + 1 + γ = 3/2 + γ. To keep at 3/2, γ = 0.

Edge: p ≥ 1 - 1/4 - 1/2 = 1/4. q ≥ max(1 - 1/4, 1 - 1/4 - 1/2 - 0, (1-0)/2) = max(3/4, 1/4, 1/2) = 3/4. s ≥ max(1 - 1 - 0, 0) = 0. p + s ≥ 1 - 1/2 = 1/2. With p = 1/4, s
