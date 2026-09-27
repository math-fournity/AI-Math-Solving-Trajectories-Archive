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
  <problem_id>polymath_00659</problem_id>
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

Find the smallest \( k \) such that for any arrangement of 3000 checkers in a \( 2011 \times 2011 \) checkerboard, with at most one checker in each square, there exist \( k \) rows and \( k \) columns for which every checker is contained in at least one of these rows or columns.

## Standard Solution

If there is a checker in every square along a main diagonal, then we need at least 1006 rows and columns to contain all these checkers. We are left to show that 1006 is sufficient.

Take the 1006 rows with the greatest number of checkers. Assume without loss of generality they are the first 1006 rows. If the remaining 1005 rows contain at most 1005 checkers, then we can certainly choose 1006 columns that contain these checkers. Otherwise, there exists a row that contains at least 2 checkers, so every row in the first 1006 rows must contain at least 2 checkers. But this means that there are at least \( 2 \times 1006 + 1006 = 3018 \) checkers in total, which is a contradiction.

Thus, the smallest \( k \) is \(\boxed{1006}\).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a 2011 × 2011 checkerboard with 3000 checkers placed (at most one per square). We need to find the smallest k such that for any arrangement, there exist k rows and k columns such that every checker is in at least one of these rows or columns.

So we need to cover all 3000 checkers using k rows and k columns. A checker at position (r,c) is covered if row r is selected or column c is selected.

We want the minimum k such that no matter how 3000 checkers are placed, we can always find k rows and k columns covering all of them.

Let me think about this. We select k rows and k columns. The uncovered region is (2011-k) × (2011-k). For all checkers to be covered, no checker can be in the uncovered region. So we need: there exist k rows and k columns such that the (2011-k)×(2011-k) sub-board formed by the unselected rows and columns contains no checker.

Equivalently: we can remove k rows and k columns to eliminate all checkers. Or: there's a set of k rows and k columns whose removal leaves an empty board.

So the question is: what's the minimum k such that for any placement of 3000 checkers on a 2011×2011 board, we can find k rows and k columns covering all checkers?

The adversary wants to maximize the number of rows and columns needed. The question is the worst case.

Let me think about it differently. If we pick k rows and k columns, the checkers not covered are those in the complement: (2011-k) rows × (2011-k) columns. So we need to find k rows and k cols such that the remaining (2011-k)×(2011-k) region has no checkers.

The adversary places 3000 checkers to make this as hard as possible - i.e., to force k to be large.

Let's think about what configuration is hardest. If we spread checkers out, we need more rows/columns. Actually, let's think about it as a bipartite graph / covering problem.

Consider the bipartite graph where rows are one side, columns the other, and checkers are edges. We want a vertex cover using at most k vertices from each side. Actually, we want exactly k from each side (or at most k from each side, but since we want minimum k, it's the same).

Wait, actually we want: k rows and k columns. So the vertex cover has exactly k from the row side and k from the column side. Total 2k vertices.

Hmm, but actually the constraint is k from each side, not 2k total. So it's a balanced vertex cover.

Let me think about the worst case. The adversary wants to place 3000 checkers such that any covering requires many rows and many columns.

Key insight: If we use k rows, they cover all checkers in those rows. The remaining checkers are in (2011-k) rows. These remaining checkers need to be covered by k columns. So the remaining checkers must fit in k columns, meaning they occupy at most k columns.

So the strategy is: pick k rows that cover as many checkers as possible, then the remaining checkers must be coverable by k columns (i.e., they span at most k columns).

Adversary's goal: place checkers so that no matter which k rows we pick, the remaining checkers span more than k columns.

Let me think about extremal configurations.

Configuration 1: Place checkers in a grid pattern. Say we place checkers in an a × b grid (a rows, b columns, all a*b cells filled). Then to cover them, we can pick all a rows (if a ≤ k) and need the columns to cover... wait, if we pick a rows, all checkers are covered, so we need 0 columns. So we'd need k ≥ a. But we could also pick some rows and some columns.

For an a × b full grid: we need to cover a*b cells with k rows and k cols. If we pick r rows and c columns (r,c ≤ k), the uncovered region is (a-r)×(b-c), which must be 0. So (a-r)(b-c) = 0, meaning r = a or c = b. So either we pick all a rows (need a ≤ k) or all b columns (need b ≤ k). So k = min(a,b).

To maximize min(a,b) with a*b = 3000, we want a and b as close as possible. 3000 = ... √3000 ≈ 54.77. So a=50, b=60 gives min=50. Or a=54, b= 3000/54 ≈ 55.5, not integer. Let's find the best: we want a*b ≥ 3000 (we can place 3000 checkers in an a×b grid if a*b ≥ 3000, actually exactly a*b if we fill it, but we only have 3000 checkers). Wait, we have exactly 3000 checkers. If a*b = 3000, we fill the entire grid. If a*b > 3000, we place 3000 of the a*b cells.

Hmm, but if we don't fill the entire grid, the analysis changes. Let me reconsider.

Actually, if we place 3000 checkers in an a × b grid but not filling all cells, then the covering might be easier. Let me think about the full grid case where a*b = 3000.

For a full a×b grid with a*b = 3000: k = min(a,b). To maximize this, maximize min(a,b) subject to a*b = 3000. The maximum is achieved when a and b are closest. Divisors of 3000: 3000 = 2³ × 3 × 5³. Divisors near √3000 ≈ 54.77: 50 (3000/50=60), 60. Also 54? 3000/54 = 55.55, not integer. 55? 3000/55 = 54.5, no. 56? 3000/56 = 53.57, no. 50×60: min=50. 40×75: min=40. 30×100: min=30. 60×50: same. What about 75×40: min=40. So the best full grid gives k=50.

But maybe a non-grid configuration is worse. Let me think more carefully.

Configuration 2: Consider a "matching" type configuration. Place checkers so that each row has few checkers and each column has few checkers, spread out maximally. 

Actually, let me think about the dual problem. We want the minimum k such that for any 3000-checker placement, there exist k rows and k columns covering all checkers.

The complement: the maximum over all placements of the minimum k needed.

For a given placement, the minimum k needed is: min over (r rows, c columns covering all) of max(r, c). Wait no, we need exactly k rows and k columns (we can pick up to k of each). Actually, we need k rows and k columns - we pick exactly k rows and k columns, and all checkers must be covered. We can always pick extra rows/columns that don't help, so the question is: can we cover all checkers with at most k rows and at most k columns?

So for a given placement, the minimum k is: min{max(r,c) : r rows and c columns cover all checkers, r ≤ k, c ≤ k}... no. The minimum k for a placement is:

min k such that ∃ r ≤ k rows and c ≤ k columns with r rows ∪ c columns covering all checkers.

= min over all covers (r rows, c cols) of max(r, c).

So we want to find a vertex cover of the bipartite graph that minimizes max(r, c) where r is the number of row-vertices and c is the number of column-vertices.

And we want the maximum of this over all placements of 3000 checkers.

Let me think about what placement maximizes this.

Consider placing checkers in a "staircase" or "anti-diagonal" pattern. 

Let me think about it as follows. Suppose the adversary places checkers in a set S of cells. We want to find the minimum max(r,c) over covers.

Claim: The worst case is a full rectangular grid.

Hmm, not necessarily. Let me think about small examples.

Consider a 3×3 board with some checkers. If we place checkers on the diagonal (3 checkers), we need to cover 3 cells, each in a different row and column. We need at least... we can cover with 1 row + 2 columns (cover row 1, then columns 2,3), so max(1,2)=2. Or 2 rows + 1 column, max=2. Or actually, can we do 1 row + 1 column? That covers at most 2 of the 3 diagonal cells (the one in the row and the one in the column; if they're different, 2 cells covered, 1 remains). So we need max(r,c) ≥ 2. So k=2 for 3 diagonal checkers on 3×3.

If we place 3 checkers in a 1×3 row, we need 1 row, 0 columns, so k=1.

If we place 4 checkers in a 2×2 grid, we need 2 rows (or 2 columns), so k=2.

If we place 2 checkers in different rows and columns (a matching of size 2), we need 1 row + 1 column, k=1.

So for 3 checkers on 3×3, the diagonal (matching of size 3) gives k=2, while a 1×3 row gives k=1, and a 2×2 grid (4 checkers, but we only have 3) ... with 3 checkers in 2×2 grid, we can cover with 2 rows, k=2.

Interesting. So a matching of size m requires k = ceil(m/2)? No. A matching of size m: each checker is in a unique row and column. To cover m checkers with r rows and c columns, we cover r + c checkers at most (since each row covers 1, each column covers 1, and they're all in different rows/columns, but a checker could be covered by both its row and column). Actually, with r rows and c columns, we cover at most r + c checkers from a matching (each row covers at most 1, each column covers at most 1, but a checker at the intersection of a chosen row and column is counted once). So we need r + c ≥ m, and we want to minimize max(r,c), so r = c = ceil(m/2). So k = ceil(m/2) for a matching of size m.

For m = 3000, k = 1500. But wait, the board is 2011×2011, so a matching of size 3000 is possible (since 3000 ≤ 2011... wait, 3000 > 2011). A matching can have at most 2011 checkers (since each row has at most 1). So the maximum matching size is 2011.

For a matching of size 2011, k = ceil(2011/2) = 1006.

But we have 3000 checkers, not 2011. So we can't just use a matching. We need to place 3000 checkers.

Let me reconsider. With 3000 checkers on a 2011×2011 board, what's the worst case?

Let me think about this more carefully. We want to find the placement of 3000 checkers that maximizes the minimum max(r,c) over all covers.

Let me think about lower bounds (adversary constructions) and upper bounds.

**Upper bound approach:** Given any placement of 3000 checkers, we want to show we can always cover with k rows and k columns for some k.

Greedy approach: Pick the rows with the most checkers. If we pick the top k rows by checker count, they cover some number of checkers. The remaining checkers are in (2011-k) rows and need to be covered by k columns, so they must span at most k columns.

Alternatively, think of it as: we want to find k rows and k columns such that the (2011-k)×(2011-k) sub-board (unselected rows × unselected columns) has no checkers.

So the question is: what's the minimum k such that for any placement of 3000 checkers, there's a (2011-k)×(2011-k) empty sub-board?

The adversary wants to place 3000 checkers to hit every (2011-k)×(2011-k) sub-board. A (2011-k)×(2011-k) sub-board is determined by choosing 2011-k rows and 2011-k columns. The adversary needs every such choice to contain at least one checker.

Let s = 2011 - k. The adversary needs: for every choice of s rows and s columns, the s×s sub-board contains at least one checker. And the adversary has 3000 checkers.

So we need: the minimum number of checkers to hit all s×s sub-boards. If this minimum is > 3000, then k = 2011 - s works (any 3000-checker placement can be covered by k rows and k columns). If the minimum is ≤ 3000, then the adversary can place 3000 checkers to hit all s×s sub-boards, so k = 2011 - s doesn't work.

So we need to find the largest s such that the minimum hitting set for all s×s sub-boards is ≤ 3000. Then k = 2011 - s.

Wait, let me re-derive. We want the smallest k such that for any placement of 3000 checkers, there's an empty s×s sub-board where s = 2011 - k. 

This is equivalent to: the minimum number of checkers needed to hit all s×s sub-boards is > 3000. (If you need more than 3000 checkers to hit all s×s sub-boards, then 3000 checkers can't hit all of them, so there's always an empty one.)

So we want the smallest k, i.e., the largest s = 2011 - k, such that the minimum hitting set for all s×s sub-boards has size > 3000.

The minimum hitting set for all s×s sub-boards: we need to place checkers so that every s×s sub-board (formed by choosing s rows and s columns) contains at least one checker.

When does a set of checkers hit all s×s sub-boards? A set of checkers fails to hit some s×s sub-board iff there exist s rows and s columns with no checker in their intersection. So the checkers hit all s×s sub-boards iff for every s rows and s columns, there's a checker in the intersection.

Equivalently: there's no s×s all-empty sub-board.

So the minimum number of checkers to have no s×s empty sub-board = the minimum number of checkers such that every s×s sub-board is hit.

Let f(s) = minimum number of checkers on a 2011×2011 board such that every s×s sub-board contains at least one checker.

We want the largest s such that f(s) > 3000. Then k = 2011 - s.

Now, what is f(s)?

f(s) is the minimum number of 1s in a 2011×2011 0-1 matrix such that there's no s×s all-zero submatrix.

This is a classical extremal problem! The Zarankiewicz-type problem or the problem of avoiding all-zero submatrices.

By a result related to the Kővári–Sós–Turán theorem or direct counting:

If we have a 0-1 matrix with m ones (checkers) and no s×s all-zero submatrix, what's the minimum m?

Actually, let me think about it directly. We have a 2011×2011 matrix. We want to place the minimum number of 1s such that there's no s×s submatrix of all 0s.

Equivalently, if we think of the 0s: we want the maximum number of 0s such that there's no s×s all-0 submatrix. Then f(s) = 2011² - (max 0s with no s×s all-0 submatrix).

Hmm, this is getting complex. Let me think about it differently.

**Direct approach to f(s):** 

We want to place checkers (1s) so that every s×s sub-board has at least one 1. 

Think of it as: we choose a set of rows R and columns C with |R| = s, |C| = s, and we need at least one checker in R × C.

The complement: there exist s rows and s columns with no checker. We want to avoid this.

A classical result: the minimum number of 1s in an n×n matrix with no s×s all-0 submatrix.

Let me think about constructions. 

**Construction for lower bound on f(s):** Place checkers in a grid pattern. Divide the 2011 rows into groups and columns into groups. 

Actually, let me think about a specific construction. Suppose we place checkers so that each row has checkers in a specific pattern.

**Simple construction:** Place checkers in a "grid" with spacing. If we place a checker every ⌈2011/s⌉ rows and every ⌈2011/s⌉ columns... hmm, this isn't quite right.

Let me think about it more carefully. 

**Claim:** f(s) = ⌈2011/s⌉² might not be right. Let me think again.

Actually, think about it this way. We want every s×s sub-board to have a checker. Consider dividing the rows into ⌈2011/s⌉ groups of size at most s (actually, we need groups of size at most s, so that any s consecutive... no, the sub-board doesn't need to be consecutive).

Wait, the s×s sub-board is formed by choosing ANY s rows and ANY s columns, not necessarily consecutive. So this is much harder.

So we need: for any s rows and any s columns, there's a checker in their intersection.

This means: if we look at the set of rows that have checkers, call it R₀, and for each row in R₀, the set of columns with checkers. 

Actually, let me think about the complement. There's no s×s all-zero submatrix iff: for every set of s rows, the union of their "zero columns" has size < s... no, that's not right either.

Let me think about it as a bipartite graph. Rows on one side, columns on the other, checker = edge. No s×s all-zero submatrix means: there's no independent set of size s in the row side and s in the column side that are completely non-adjacent. In other words, for every set S of s rows and T of s columns, there's an edge between S and T.

This is related to the bipartite Ramsey-type problem.

**Key insight:** If we place checkers such that every row has at least t checkers, and every column has at least t checkers, does that help? Not directly, because the s rows might avoid the columns with checkers.

Let me think about the contrapositive. There exists an s×s all-zero submatrix iff there exist s rows and s columns with no checker in their intersection. 

This happens iff we can find s rows R' and s columns C' such that no checker has its row in R' and column in C'.

Equivalently, if we let A_i = set of columns with checkers in row i, then we need: for every set of s rows, the complement of the union of their A_i's has size < s. I.e., the union of A_i's over any s rows has size > 2011 - s.

Hmm, this is getting complicated. Let me try a different approach.

**Approach via the probabilistic method or direct counting:**

Let's think about what the adversary can do. The adversary places 3000 checkers to maximize the minimum k. We want to find this maximum.

Let me think about specific constructions.

**Construction A: Full a×b grid.** Place 3000 checkers in a 50×60 grid (filling all 3000 cells). Then as computed, k = min(50, 60) = 50.

**Construction B: Matching-like.** We can have at most 2011 checkers in a matching (one per row, one per column). With 3000 checkers, we can have a matching of size 2011 plus 989 more checkers.

For a matching of size m, k = ⌈m/2⌉. For m = 2011, k = 1006. But we have 3000 checkers, so we need to place 989 more. These extra checkers might not increase k much if they're placed in rows/columns already used.

Wait, but if we have a matching of size 2011 (one checker per row, one per column, all 2011 rows and 2011 columns used), then to cover all checkers, we need r rows and c columns with r + c ≥ 2011 (since it's a perfect matching, each row-column pair covers exactly one checker, and we need to cover 2011 checkers, each requiring either its row or column). So max(r,c) ≥ ⌈2011/2⌉ = 1006.

But we have 3000 checkers, not 2011. If we place a matching of 2011 and then 989 more checkers, the extra checkers are in rows and columns that already have checkers. Do they increase k?

Let me think. With a perfect matching (2011 checkers, one per row and column), k = 1006. Now add 989 more checkers. These additional checkers are in cells (r, c) where row r and column c already have a matching checker. Adding more checkers to a row-column pair that's already covered doesn't increase k, because any cover of the matching also covers these extra checkers (if a row is selected, all checkers in that row are covered; if a column is selected, all checkers in that column are covered).

Wait, that's the key point! If we have a matching of size 2011, any cover (r rows, c columns) with r + c ≥ 2011 covers all matching checkers. But does it cover the extra checkers?

An extra checker at (r, c) is covered if row r is selected or column c is selected. In the matching, row r has a checker at (r, σ(r)) and column c has a checker at (σ⁻¹(c), c). If row r is selected, the extra checker is covered. If column c is selected, the extra checker is covered. If neither is selected, then the matching checkers at (r, σ(r)) and (σ⁻¹(c), c) must be covered by their columns/rows respectively: column σ(r) is selected and row σ⁻¹(c) is selected.

So the extra checker at (r,c) is not covered iff row r is not selected and column c is not selected. But then, for the matching to be covered, column σ(r) must be selected (to cover (r, σ(r))) and row σ⁻¹(c) must be selected (to cover (σ⁻¹(c), c)).

So it's possible that an extra checker is not covered even if the matching is covered. So adding extra checkers CAN increase k.

Hmm, so the matching construction with extra checkers might require larger k. Let me think about this more carefully.

Actually, let me reconsider. The problem is to cover ALL 3000 checkers, not just the matching. So the extra checkers matter.

Let me think about the worst case more carefully.

**Reformulation:** We have a bipartite graph G with parts R (2011 rows) and C (2011 columns), and 3000 edges (checkers). We want to find a vertex cover (S_R ⊆ R, S_C ⊆ C) minimizing max(|S_R|, |S_C|). We want to find the maximum of this over all bipartite graphs with 2011+2011 vertices and 3000 edges.

Let me denote this maximum as K. We want to find K.

**Lower bound construction:** I'll try to construct a graph where any balanced cover needs large k.

Consider the following construction: Take a set of a rows and b columns, and place checkers to form a complete bipartite graph K_{a,b} (all a*b cells filled), with a*b = 3000. As computed, this requires k = min(a,b). The best is a=50, b=60, giving k=50. This is not great.

**Better construction:** Consider a "spread out" construction. Place checkers so that they form a structure where many rows and columns are needed.

Let me think about the following: place 3000 checkers such that they form a union of matchings or some other structure.

Actually, let me think about the problem from the upper bound side.

**Upper bound:** Given 3000 checkers, we want to show we can always cover with k rows and k columns for some k.

Approach: Pick the k rows with the most checkers. These cover some checkers. The remaining checkers are in 2011-k rows. If the remaining checkers span at most k columns, we're done.

Let's say the total checkers is 3000. If we pick the top k rows, they cover at least 3000k/2011 checkers (by averaging, the top k rows have at least as many as k/2011 fraction). Actually, the top k rows have at least k * (3000/2011) checkers on average, but they could have more.

The remaining checkers: at most 3000 - (checkers in top k rows). These are in 2011-k rows. The remaining checkers span some number of columns. If they span at most k columns, we're done.

Hmm, this is hard to bound directly. Let me think about it differently.

**Another approach:** Think of it as choosing which rows and columns to NOT select. We leave s = 2011-k rows and s = 2011-k columns unselected, forming an s×s sub-board that must be empty. So we need to find s rows and s columns with no checker in their intersection, where s = 2011-k is as large as possible.

The adversary wants to place 3000 checkers so that every s×s sub-board has a checker. We want the largest s where the adversary can't do this with 3000 checkers.

So: what's the minimum number of checkers to hit all s×s sub-boards of a 2011×2011 board?

Let me think about this. To hit all s×s sub-boards, we need: for every choice of s rows and s columns, at least one checker in the intersection.

**Claim:** The minimum number of checkers to hit all s×s sub-boards is ⌈n/s⌉ · ⌈n/s⌉ where n = 2011... no, that's for consecutive sub-boards. For arbitrary sub-boards, it's different.

Wait, actually for arbitrary sub-boards (any s rows, any s columns), the problem is:

Minimum number of edges in a bipartite graph G on (R, C) with |R| = |C| = n such that every s×s induced subgraph has at least one edge.

This is equivalent to: the bipartite complement has no K_{s,s}. By the Kővári–Sós–Turán theorem, the maximum number of edges in a bipartite graph on (n, n) with no K_{s,s} is at most ... well, the KST theorem gives an upper bound on edges with no K_{s,t}.

But we want the minimum number of edges such that the complement has no K_{s,s}. The complement has n² - m edges (where m is the number of checkers). We need the complement to have no K_{s,s}, so n² - m ≤ ex(n, n, K_{s,s}), where ex is the Zarankiewicz number.

So m ≥ n² - ex(n, n, K_{s,s}).

The Zarankiewicz number z(n, n, s, s) = maximum edges in bipartite graph on (n,n) with no K_{s,s}. By KST, z(n,n,s,s) ≤ (s-1)^{1/s} · n^{2-1/s} + (s-1)n. (Roughly.)

So m ≥ n² - z(n,n,s,s) ≈ n² - O(n^{2-1/s}).

For n = 2011 and s around... we want m > 3000, so n² - z(n,n,s,s) > 3000, i.e., z(n,n,s,s) < n² - 3000 = 2011² - 3000 = 4044121 - 3000 = 4041121.

But z(n,n,s,s) for s ≥ 2 is at most about n^{2-1/s} which for n=2011 is much less than n². So for s ≥ 2, the minimum m is close to n², way more than 3000. That means for s ≥ 2, we can always find an empty s×s sub-board with only 3000 checkers.

Wait, that can't be right. Let me re-examine.

If s = 2: we need every 2×2 sub-board to have a checker. The minimum number of checkers for this is... well, the complement (0s) has no 2×2 all-0 submatrix, meaning the 0s form a bipartite graph with no K_{2,2} = no C_4. The maximum number of 0s with no C_4 is the Zarankiewicz number z(n,n,2,2) ≈ n^{3/2}. So the minimum number of 1s is n² - n^{3/2} ≈ 2011² - 2011^{1.5} ≈ 4,044,121 - 90,200 ≈ 3,953,921. This is way more than 3000.

So with only 3000 checkers, we definitely can't hit all 2×2 sub-boards. So s = 2 works, meaning k = 2011 - 2 = 2009. But that's a terrible bound; we want the smallest k, so the largest s.

Hmm wait, I think I have the direction confused. Let me re-examine.

We want the smallest k such that for any 3000-checker placement, we can cover with k rows and k columns. This means: for any 3000-checker placement, there's an empty s×s sub-board with s = 2011 - k. We want the smallest k, i.e., the largest s, such that this is guaranteed.

The guarantee fails when the adversary can place 3000 checkers hitting all s×s sub-boards. So we need f(s) > 3000, where f(s) = min checkers to hit all s×s sub-boards.

f(s) = n² - z(n,n,s,s) where z is the Zarankiewicz number (max edges in bipartite graph on (n,n) with no K_{s,s}).

We need f(s) > 3000, i.e., n² - z(n,n,s,s) > 3000, i.e., z(n,n,s,s) < n² - 3000.

For s = 2: z(2011,2011,2,2) ≈ 2011^{3/2} ≈ 90,200. And n² - 3000 ≈ 4,041,121. So 90,200 < 4,041,121. ✓ So f(2) > 3000. ✓

For large s: z(n,n,s,s) decreases (fewer edges allowed without K_{s,s}), so f(s) = n² - z increases. So for larger s, f(s) is even larger, and the condition f(s) > 3000 is even easier to satisfy.

Wait, that means for ALL s ≥ 2, f(s) > 3000? That would mean k = 2011 - s for any s, and the smallest k would be... s can be as large as 2011, giving k = 0? That's obviously wrong.

I think I have the direction backwards. Let me reconsider.

If s is large (close to n), then an s×s sub-board is almost the entire board. To hit all s×s sub-boards, we need a checker in every s×s sub-board. If s = n, the only s×s sub-board is the entire board, so we need at least 1 checker. f(n) = 1.

If s = n-1, an s×s sub-board is formed by removing 1 row and 1 column. There are n² such sub-boards. To hit all of them, we need... a checker that's not in the removed row and column. So for every row r and column c, there's a checker not in row r and not in column c. This means the checkers can't all be in one row or one column. f(n-1) = 2 (place 2 checkers in different rows and columns).

So f(s) decreases as s increases. For s close to n, f(s) is small. For s small, f(s) is large (close to n²).

So we want the largest s such that f(s) > 3000. Since f is decreasing in s, we want the transition point.

Let me reconsider the formula. f(s) = minimum checkers so that every s×s sub-board has a checker. The complement: maximum 0s (empty cells) such that no s×s all-0 sub-board exists. f(s) = n² - max_0s.

max_0s with no s×s all-0 sub-board = z(n, n, s, s) (Zarankiewicz: max edges in bipartite graph on (n,n) with no K_{s,s}).

So f(s) = n² - z(n, n, s, s).

For s = 1: z(n,n,1,1) = 0 (no K_{1,1} means no edges, so max 0s = 0, f(1) = n²). Makes sense: to hit all 1×1 sub-boards (every cell), need n² checkers.

For s = 2: z(n,n,2,2) ≈ n^{3/2}, f(2) ≈ n² - n^{3/2} ≈ 3.95M. 

For s = n: z(n,n,n,n) = n² - 1 (can have all edges except... wait, K_{n,n} is the complete bipartite graph. No K_{n,n} means we can't have all n² edges. So z = n² - 1. f(n) = n² - (n²-1) = 1. ✓

For s = n-1: z(n,n,n-1,n-1) = ? We need no K_{n-1,n-1}. The max edges without K_{n-1,n-1}: we can have all edges except we need to avoid a complete (n-1)×(n-1) subgraph. If we remove one edge, say (r₁, c₁), then any (n-1)×(n-1) subgraph that includes row r₁ and column c₁ is missing that edge, so it's not complete. But a (n-1)×(n-1) subgraph that excludes row r₁ or column c₁ could be complete. If we exclude row r₁, the remaining n-1 rows and any n-1 columns form a complete subgraph (since we only removed edge (r₁,c₁)). So removing 1 edge isn't enough. 

We need: for every set of n-1 rows and n-1 columns, at least one edge is missing. The missing edges form a set M. For every (n-1) rows R' and (n-1) columns C', M ∩ (R' × C') ≠ ∅. This means: for every row r and column c (the excluded ones), there's a missing edge in the (n-1)×(n-1) sub-board excluding r and c. I.e., for every (r, c), there's a missing edge (r', c') with r' ≠ r and c' ≠ c. 

This means the missing edges can't all share a common row or common column. The minimum such set: 2 missing edges in different rows and different columns. So z(n,n,n-1,n-1) = n² - 2, f(n-1) = 2. ✓

OK so now I need to find the largest s such that f(s) > 3000, i.e., n² - z(n,n,s,s) > 3000, i.e., z(n,n,s,s) < n² - 3000 = 2011² - 3000 = 4,044,121 - 3,000 = 4,041,121.

Since z(n,n,s,s) is the max edges in a bipartite graph on (n,n) with no K_{s,s}, and n² = 4,044,121, we need z < 4,041,121, i.e., z < n² - 3000.

Equivalently, the maximum number of 0s (empty cells) without an s×s all-0 sub-board must be less than n² - 3000. Or, any set of n² - 3000 empty cells (i.e., 3000 checkers) must contain an s×s all-empty sub-board.

Hmm, let me think about this differently. We have 3000 checkers and n² - 3000 empty cells. We want to find the largest s such that any set of n² - 3000 empty cells contains an s×s all-empty sub-board. Wait, no: we want that for any placement of 3000 checkers, there's an s×s empty sub-board. The empty cells are n² - 3000, and we want them to always contain an s×s complete bipartite subgraph.

So: any bipartite graph on (n,n) with n² - 3000 edges contains K_{s,s}. We want the largest such s.

By KST theorem, if a bipartite graph on (n,n) has more than (s-1)^{1/s} · n^{2-1/s} + (s-1)·n edges, it contains K_{s,s}. 

We have n² - 3000 edges. We need n² - 3000 > (s-1)^{1/s} · n^{2-1/s} + (s-1)·n.

For n = 2011, n² - 3000 = 4,041,121. We need this to exceed the KST bound.

The KST bound is approximately (s-1)^{1/s} · n^{2-1/s}. For large s, (s-1)^{1/s} ≈ 1, so the bound is ≈ n^{2-1/s}. We need n² - 3000 > n^{2-1/s}, i.e., n² > n^{2-1/s} + 3000. Since n² = n^{2-1/s} · n^{1/s}, this is n^{2-1/s}(n^{1/s} - 1) > 3000.

For n = 2011: n^{1/s} = 2011^{1/s}. We need 2011^{2-1/s} · (2011^{1/s} - 1) > 3000.

Let me try s = 2: 2011^{3/2} · (2011^{1/2} - 1) ≈ 90,200 · (44.8 - 1) ≈ 90,200 · 43.8 ≈ 3,950,000 > 3000. ✓

s = 100: 2011^{2-1/100} · (2011^{1/100} - 1) = 2011^{1.99} · (2011^{0.01} - 1). 2011^{0.01} = e^{0.01 · ln(2011)} = e^{0.01 · 7.606} = e^{0.07606} ≈ 1.0790. So (1.079 - 1) = 0.079. 2011^{1.99} = 2011² / 2011^{0.01} ≈ 4,044,121 / 1.079 ≈ 3,748,000. So 3,748,000 · 0.079 ≈ 296,000 > 3000. ✓

s = 1000: 2011^{2-1/1000} · (2011^{1/1000} - 1). 2011^{1/1000} = e^{7.606/1000} = e^{0.007606} ≈ 1.00763. (1.00763 - 1) = 0.00763. 2011^{1.999} ≈ 4,044,121 / 1.00763 ≈ 4,013,500. 4,013,500 · 0.00763 ≈ 30,623 > 3000. ✓

s = 2000: 2011^{2-1/2000} · (2011^{1/2000} - 1). 2011^{1/2000} = e^{7.606/2000} = e^{0.003803} ≈ 1.00381. (1.00381 - 1) = 0.00381. 2011^{1.9995} ≈ 4,044,121 / 1.00381 ≈ 4,028,800. 4,028,800 · 0.00381 ≈ 15,350 > 3000. ✓

s = 2010: 2011^{2-1/2010} · (2011^{1/2010} - 1). 2011^{1/2010} = e^{7.606/2010} = e^{0.003784} ≈ 1.00379. (1.00379 - 1) = 0.00379. 2011^{1.9995} ≈ 4,044,121 / 1.00379 ≈ 4,028,800. 4,028,800 · 0.00379 ≈ 15,269 > 3000. ✓

Hmm, so even for s = 2010, the KST bound is satisfied. But wait, the KST bound is an upper bound on z, and we need z < n² - 3000. The KST bound says z ≤ (s-1)^{1/s} n^{2-1/s} + (s-1)n. If this upper bound is less than n² - 3000, then z < n² - 3000, and we're done.

But the KST bound might be very loose. Let me check: for s = 2010, the KST bound is approximately 2010^{1/2010} · 2011^{2-1/2010} + 2009 · 2011 ≈ 1 · 4,028,800 + 4,044,099 ≈ 8,072,899. But n² = 4,044,121. So the KST bound 8,072,899 > n² = 4,044,121! The bound is useless here (it exceeds n², the total possible edges).

So the KST bound is only useful when it's less than n². Let me find when (s-1)^{1/s} · n^{2-1/s} + (s-1)·n < n².

For large s, (s-1)n ≈ sn, and we need sn < n², i.e., s < n. And (s-1)^{1/s} · n^{2-1/s} ≈ n^{2-1/s} which is close to n² for large s. So the bound is close to n² + sn > n². So for s close to n, the KST bound exceeds n² and is useless.

Let me find the crossover. We need (s-1)^{1/s} · n^{2-1/s} + (s-1)·n < n² - 3000.

For the first term: (s-1)^{1/s} · n^{2-1/s} ≈ n^{2-1/s} (since (s-1)^{1/s} ≈ 1 for large s). This is n² / n^{1/s}. So the first term ≈ n² / n^{1/s}.

We need n²/n^{1/s} + sn < n² - 3000. I.e., n²(1 - 1/n^{1/s}) > sn + 3000.

n^{1/s} = e^{(ln n)/s}. For large s, n^{1/s} ≈ 1 + (ln n)/s. So 1 - 1/n^{1/s} ≈ 1 - 1/(1 + (ln n)/s) ≈ (ln n)/s.

So n² · (ln n)/s > sn + 3000. I.e., n² ln n > s²n + 3000s. For n = 2011: n² ln n ≈ 4,044,121 · 7.606 ≈ 30,770,000. And s²n = 2011 s². So 30,770,000 > 2011 s² + 3000s. 

2011 s² < 30,770,000 → s² < 15,300 → s < 124. So for s up to about 124, the KST bound is useful.

But this only gives us s up to ~124, meaning k = 2011 - 124 = 1887. That's a very weak bound. The KST bound is not tight enough.

I think the issue is that the KST bound is a general bound for K_{s,s}-free bipartite graphs, but our setting is more specific (we have a dense graph with n² - 3000 edges, and we want to find K_{s,s}).

Let me think about this differently. With n² - 3000 edges (almost complete), we should be able to find very large complete bipartite subgraphs.

**Direct approach:** We have 3000 missing edges (checkers). We want to find s rows and s columns with no missing edges in their intersection (i.e., all cells empty, forming K_{s,s} in the empty-cell graph).

The 3000 checkers are in some rows and columns. Let's say the checkers occupy r distinct rows and c distinct columns. Then r ≤ 3000, c ≤ 3000 (and r, c ≤ 2011).

If we avoid these r rows and c columns, the remaining (2011 - r) rows and (2011 - c) columns form a completely empty sub-board. So s = min(2011 - r, 2011 - c).

To minimize s (adversary's goal), the adversary maximizes r and c. The adversary can have checkers in all 2011 rows (r = 2011) and all 2011 columns (c = 2011) with just 2011 checkers (a perfect matching). Then s = min(0, 0) = 0. But that's the approach of avoiding ALL rows and columns with checkers, which is too restrictive.

We don't need to avoid all rows with checkers; we just need to find s rows and s columns with no checker in their intersection. Even if a row has checkers, we can include it as long as the columns we choose don't coincide with the checker columns in that row.

Let me think about this more carefully.

**Refined approach:** Let's say the 3000 checkers are placed. For each row i, let c_i be the set of columns with checkers in row i. We want to find s rows R and s columns C such that for every row r in R, c_r ∩ C = ∅. I.e., C avoids ∪_{r ∈ R} c_r.

So for a set R of s rows, the forbidden columns are ∪_{r ∈ R} c_r. We need |∪_{r ∈ R} c_r| ≤ 2011 - s, so that we can find s columns outside this union.

So we need: there exist s rows R such that |∪_{r ∈ R} c_r| ≤ 2011 - s.

The adversary wants: for every set R of s rows, |∪_{r ∈ R} c_r| > 2011 - s.

I.e., every s rows have checkers in more than 2011 - s columns, i.e., in at least 2012 - s columns.

So the adversary needs: every set of s rows has checkers spanning at least 2012 - s columns.

With 3000 checkers total, the adversary needs to distribute them so that any s rows span at least 2012 - s columns.

Hmm, let me think about what s can be achieved.

If s is small, say s = 1: every 1 row has checkers in at least 2011 columns. But a row can have at most 2011 checkers, and we have 3000 total. If one row has 2011 checkers, the remaining 989 are in other rows. But then those other rows might have 0 checkers, violating the condition for s = 1 (every row needs ≥ 2011 checkers, impossible with 3000 total and 2011 rows). So s = 1 is easy for us (hard for adversary).

If s is large, say s = 2011: every 2011 rows (all rows) span at least 1 column. This just means there's at least one checker. Easy for adversary with 3000 checkers.

We want the largest s where the adversary CANNOT satisfy the condition. The adversary's condition: every s rows span at least 2012 - s columns.

Let me think about the adversary's best strategy. The adversary wants to maximize the minimum over all s-row subsets of the number of columns spanned.

Actually, the adversary wants: min over all s-row subsets R of |∪_{r ∈ R} c_r| ≥ 2012 - s.

To make this hold, the adversary needs even the "worst" s rows (those with fewest checkers) to span many columns.

If the adversary spreads checkers uniformly: 3000 checkers over 2011 rows, about 1.49 per row. If each row has 1 or 2 checkers, then s rows span at most 2s columns. We need 2s ≥ 2012 - s, i.e., 3s ≥ 2012, s ≥ 671. So for s ≤ 670, even the worst s rows (with 1 checker each) span at least s columns, and we need s ≥ 2012 - s... wait, let me redo this.

If each row has at most 2 checkers, then s rows span at most 2s columns. The adversary needs 2s ≥ 2012 - s, i.e., 3s ≥ 2012, s ≥ 671. So for s < 671, the adversary's condition fails (there exist s rows spanning < 2012 - s columns), meaning we CAN find an empty s×s sub-board.

But wait, the adversary can choose the distribution. Let me think about the adversary's optimal strategy more carefully.

The adversary has 3000 checkers to distribute among 2011 rows. Let a_i = number of checkers in row i. Σa_i = 3000, 0 ≤ a_i ≤ 2011.

For a set R of s rows, the number of columns spanned is at most Σ_{r ∈ R} a_r (could be less due to overlaps, but at most this). The adversary wants every s rows to span ≥ 2012 - s columns.

A necessary condition: the s rows with the fewest checkers must span ≥ 2012 - s columns. The s rows with fewest checkers have at most 3000s/2011 checkers total (by averaging). So the columns spanned ≤ 3000s/2011.

We need 3000s/2011 ≥ 2012 - s. I.e., 3000s/2011 + s ≥ 2012. s(3000/2011 + 1) ≥ 2012. s(5011/2011) ≥ 2012. s ≥ 2012 · 2011/5011 = 2012 · 2011 / 5011.

2012 · 2011 = 4,046,132. 4,046,132 / 5011 ≈ 807.4. So s ≥ 808.

Wait, but this is a necessary condition for the adversary. If s < 808, the adversary cannot satisfy the condition (the s rows with fewest checkers have too few checkers to span enough columns). So for s ≤ 807, we can always find an empty s×s sub-board, meaning k = 2011 - 807 = 1204 suffices.

But this is just a necessary condition. The adversary might not be able to achieve s = 808 either. And also, the bound 3000s/2011 is the average, which is an upper bound on the minimum, but the actual minimum could be lower.

Hmm wait, I need to be more careful. The s rows with the fewest checkers have at most ⌊3000s/2011⌋ checkers total (this is an upper bound on the sum of the smallest s values, which is at most s times the average). Actually, the sum of the smallest s values is at most s · (total/n) = 3000s/2011. But it could be much less if the distribution is uneven.

But the adversary controls the distribution! The adversary wants to make the minimum (over s-row subsets) of columns spanned as large as possible. So the adversary would spread checkers evenly.

If the adversary spreads checkers evenly: each row gets either ⌊3000/2011⌋ = 1 or ⌈3000/2011⌉ = 2 checkers. 3000 = 2011 + 989, so 989 rows get 2 checkers and 2011 - 989 = 1022 rows get 1 checker.

Now, the s rows with the fewest checkers: if s ≤ 1022, we can pick s rows each with 1 checker. These span at most s columns (each has 1 checker, possibly in different columns). The adversary needs s ≥ 2012 - s, i.e., 2s ≥ 2012, s ≥ 1006. So for s ≤ 1005, if we can find s rows with 1 checker each, they span at most s columns, and we need s < 2012 - s, i.e., 2s < 2012, s < 1006. So for s ≤ 1005, we can find s rows spanning ≤ s < 2012 - s columns, giving us an empty s×s sub-board.

Wait, but the adversary can choose which columns the checkers are in. If s rows each have 1 checker, and the adversary places them all in the same column, they span only 1 column. But the adversary wants to MAXIMIZE the columns spanned. So the adversary would place them in different columns. But there are only 2011 columns.

Hmm, but the adversary's goal is to make EVERY s-row subset span many columns. If 1022 rows have 1 checker each, and we pick s ≤ 1022 of them, the adversary wants these s rows to span ≥ 2012 - s columns. But s rows with 1 checker each span at most s columns. So we need s ≥ 2012 - s, i.e., s ≥ 1006.

So for s ≤ 1005: there exist s rows (with 1 checker each) spanning at most s ≤ 1005 columns. We need s ≤ 2011 - (2012 - s) = s - 1, which means the columns spanned (≤ s) must be ≤ 2011 - s. We need s ≤ 2011 - s, i.e., 2s ≤ 2011, s ≤ 1005. And the columns spanned ≤ s ≤ 1005 ≤ 2011 - 1005 = 1006. So we can find s columns outside the spanned columns (since 2011 - s ≥ 2011 - 1005 = 1006 ≥ s = 1005). So we get an empty s×s sub-board. ✓

For s = 1006: the s rows with 1 checker each span at most 1006 columns. We need 1006 ≤ 2011 - 1006 = 1005. But 1006 > 1005. So this doesn't work directly. But maybe we can pick a different set of s rows?

Hmm, let me reconsider. For s = 1006, we need to find 1006 rows and 1006 columns with no checker in their intersection. The 1006 rows span some columns; we need the spanned columns to be ≤ 2011 - 1006 = 1005, so we can find 1006 columns outside.

If we pick 1006 rows with 1 checker each (possible since 1022 ≥ 1006), they span at most 1006 columns. We need ≤ 1005. If the adversary places these checkers in distinct columns, they span exactly 1006 columns, and 1006 > 1005. So we can't find 1006 empty columns.

But maybe we can pick a different set of 1006 rows. What if we pick some rows with 2 checkers? That would span more columns, which is worse. Or rows with 0 checkers? But all rows have at least 1 checker in this distribution.

Actually wait, can the adversary do better than the uniform distribution? Let me reconsider.

The adversary's goal: maximize the minimum s such that they can prevent an empty s×s sub-board. Equivalently, maximize the minimum over all s-row subsets of the number of columns spanned, and make this ≥ 2012 - s.

Let me think about what the adversary can achieve. The adversary has 3000 checkers. The adversary wants: for every set of s rows, the checkers in those rows span at least 2012 - s columns.

Consider the adversary's optimal strategy. The adversary needs even the worst s rows to span ≥ 2012 - s columns. The worst s rows are those with the fewest checkers (and those checkers concentrated in few columns).

To maximize the minimum columns spanned by any s rows, the adversary should:
1. Spread checkers evenly across rows (so no row has too few).
2. Spread checkers within each row across different columns (so columns spanned is close to the number of checkers).

But there's tension: if checkers are in different columns for each row, but many rows use the same columns, then the union of columns for s rows might not be much larger than for 1 row.

Let me think about the adversary's best construction.

**Adversary construction 1: Uniform distribution.** 989 rows with 2 checkers, 1022 rows with 1 checker. Place checkers so that each column has about 3000/2011 ≈ 1.49 checkers. 

For s = 1006: pick 1006 rows with 1 checker each. They span at most 1006 columns (if all in distinct columns). The adversary needs this to be ≥ 2012 - 1006 = 1006. So the adversary needs these 1006 checkers to be in 1006 distinct columns. If the adversary can arrange this, then the condition is exactly met (1006 ≥ 1006), and we can't find an empty 1006×1006 sub-board using these rows.

But can the adversary arrange for every set of 1006 single-checker rows to have their checkers in distinct columns? That would require that no two single-checker rows share a column. There are 1022 single-checker rows, so they'd need 1022 distinct columns. That's possible (1022 ≤ 2011). But then the 989 double-checker rows use the remaining 2011 - 1022 = 989 columns, plus possibly some of the 1022 columns. Each double-checker row has 2 checkers, so 1978 checkers in these rows. If they use 989 columns, each column gets about 2 checkers.

But wait, the condition must hold for EVERY set of s rows, not just the single-checker ones. What about a set of s rows that includes some double-checker rows?

If we pick s rows including some double-checker rows, they span more columns (good for the adversary). The worst case for the adversary is the set of s rows with the fewest total checkers, which is the s single-checker rows (if s ≤ 1022).

So the adversary's bottleneck is the single-checker rows. For s ≤ 1022, the worst s rows have 1 checker each, spanning at most s columns. The adversary needs s ≥ 2012 - s, i.e., s ≥ 1006.

So for s = 1006, the adversary can potentially prevent an empty 1006×1006 sub-board (if the 1022 single-checker rows all have checkers in distinct columns, then any 1006 of them span 1006 columns, and 1006 = 2012 - 1006, so the condition is exactly met).

But for s = 1007: the worst 1007 rows have 1 checker each (since 1022 ≥ 1007), spanning at most 1007 columns. The adversary needs 1007 ≥ 2012 - 1007 = 1005. This is satisfied (1007 ≥ 1005). So the adversary can prevent an empty 1007×1007 sub-board too?

Wait, I think I need to re-examine the condition. The condition for the adversary to prevent an empty s×s sub-board is: for every set R of s rows, |∪_{r ∈ R} c_r| > 2011 - s, i.e., ≥ 2012 - s.

For s = 1007: worst 1007 rows (1 checker each) span at most 1007 columns. Need ≥ 2012 - 1007 = 1005. 1007 ≥ 1005. ✓ So the adversary can prevent it.

For s = 1500: worst 1500 rows. We have 1022 rows with 1 checker and 989 with 2. The worst 1500 rows include all 1022 single-checker rows and 478 double-checker rows. Total checkers: 1022 + 478·2 = 1022 + 956 = 1978. These span at most 1978 columns. Need ≥ 2012 - 1500 = 512. 1978 ≥ 512. ✓

For s = 2000: worst 2000 rows = all rows except 11. Total checkers ≈ 3000 - (checkers in best 11 rows). The best 11 rows have at most 22 checkers (11 double-checker rows). So worst 2000 rows have ≥ 2978 checkers, spanning ≥ ... well, at most 2011 columns. Need ≥ 2012 - 2000 = 12. 2011 ≥ 12. ✓

So it seems like for all s, the adversary can prevent an empty s×s sub-board? That can't be right for small s.

Let me recheck for s = 2. Worst 2 rows: 2 single-checker rows, spanning at most 2 columns. Need ≥ 2012 - 2 = 2010. 2 ≥ 2010? NO. ✗

So for s = 2, the adversary cannot prevent an empty 2×2 sub-board. Good.

For s = 1006: worst 1006 rows span at most 1006 columns. Need ≥ 1006. 1006 ≥ 1006. ✓ (barely).

For s = 1005: worst 1005 rows span at most 1005 columns. Need ≥ 2012 - 1005 = 1007. 1005 ≥ 1007? NO. ✗

So the threshold is s = 1006. For s ≤ 1005, the adversary cannot prevent an empty s×s sub-board (we can always find one). For s = 1006, the adversary might be able to prevent it.

But wait, I need to check whether the adversary can actually achieve the bound for s = 1006. The condition is that the worst 1006 rows span ≥ 1006 columns. The worst 1006 rows are 1006 single-checker rows, each with 1 checker. For them to span 1006 columns, all 1006 checkers must be in distinct columns. The adversary can arrange this (place 1022 single-checker rows with checkers in 1022 distinct columns).

But we also need the condition to hold for ALL sets of 1006 rows, not just the single-checker ones. For a set of 1006 rows that includes some double-checker rows, the spanned columns are ≥ 1006 (since even 1006 single-checker rows span 1006 columns, and adding double-checker rows only adds more). Wait, no: a set of 1006 rows could include, say, 500 single-checker and 506 double-checker rows. Total checkers: 500 + 1012 = 1512, spanning at most 1512 columns. Need ≥ 1006. 1512 ≥ 1006. ✓

Actually, any set of 1006 rows has at least 1006 checkers (since each row has ≥ 1 checker). If all checkers are in distinct columns, they span exactly (number of checkers) columns ≥ 1006. But checkers might share columns. The adversary needs to ensure that even with sharing, the span is ≥ 1006.

Hmm, so the adversary needs: for every set of 1006 rows, the checkers in those rows span ≥ 1006 columns. This is a stronger condition than just the single-checker rows having distinct columns.

Let me think about whether the adversary can achieve this. The adversary has 3000 checkers in 2011 rows and 2011 columns. The condition is: every 1006 rows span ≥ 1006 columns.

This is equivalent to: there's no set of 1006 rows and 1006 columns with no checker in their intersection. I.e., there's no empty 1006×1006 sub-board.

Can the adversary place 3000 checkers to avoid any empty 1006×1006 sub-board?

By our earlier analysis, f(1006) = minimum checkers to hit all 1006×1006 sub-boards. We need f(1006) ≤ 3000 for the adversary to succeed.

Let me compute f(1006) more carefully. f(s) = minimum checkers such that every s×s sub-board has a checker.

We showed that with the uniform distribution (1022 rows with 1 checker, 989 with 2), the condition for s = 1006 is barely met IF the single-checker rows have distinct columns. But we need ALL sets of 1006 rows to span ≥ 1006 columns.

Let me think about a potential counterexample. Suppose the adversary places checkers as follows: 1022 rows have 1 checker each, in columns 1 through 1022 (distinct). 989 rows have 2 checkers each, in columns 1023 through 2011 (each of these 989 columns gets about 2 checkers, but from different rows).

Now consider 1006 rows: 1006 single-checker rows. Their checkers are in 1006 distinct columns (from columns 1-1022). So they span 1006 columns. ✓ (exactly 1006).

Consider 1006 rows: 1000 single-checker + 6 double-checker. Checkers in 1000 columns (from 1-1022) + up to 12 columns (from 1023-2011). Total spanned: up to 1012. ≥ 1006. ✓

Consider 1006 rows: all 989 double-checker + 17 single-checker. Checkers: 989·2 + 17 = 1995. Spanned columns: up to 2011. ≥ 1006. ✓

So it seems like the adversary can achieve s = 1006. But can the adversary achieve s = 1007?

For s = 1007: worst 1007 rows = 1007 single-checker rows (since 1022 ≥ 1007). They span at most 1007 columns. Need ≥ 2012 - 1007 = 1005. 1007 ≥ 1005. ✓

Wait, so the adversary can also achieve s = 1007? Let me recheck.

For s = 1007, the condition is: every 1007 rows span ≥ 1005 columns. The worst 1007 rows have 1007 checkers (1 each), spanning at most 1007 columns. 1007 ≥ 1005. ✓

But can the adversary actually ensure this? The 1007 single-checker rows have checkers in at most 1007 distinct columns (from the 1022 available). So they span ≤ 1007 columns. The condition needs ≥ 1005. If the adversary places them in distinct columns, they span 1007 ≥ 1005. ✓

But what if some of the 1007 single-checker rows share columns? The adversary controls the placement, so they can ensure distinct columns. So yes, the adversary can achieve s = 1007.

Hmm, so let me reconsider. The condition for the adversary to block an empty s×s sub-board is: every s rows span ≥ 2012 - s columns. The worst case is the s rows with the fewest checkers.

With the uniform distribution (1022 rows with 1, 989 with 2):
- For s ≤ 1022: worst s rows have s checkers, spanning ≤ s columns. Need s ≥ 2012 - s, i.e., 2s ≥ 2012, s ≥ 1006.
- For 1023 ≤ s ≤ 2011: worst s rows include all 1022 single-checker rows and s - 1022 double-checker rows. Total checkers: 1022 + 2(s - 1022) = 2s - 1022. Spanning ≤ 2s - 1022 columns. Need 2s - 1022 ≥ 2012 - s, i.e., 3s ≥ 3034, s ≥ 1012.

Wait, so for s between 1023 and 2011, the condition is s ≥ 1012, which is always satisfied (since s ≥ 1023 > 1012). And for s ≤ 1022, the condition is s ≥ 1006.

So the adversary can block empty s×s sub-boards for s ≥ 1006 (with the uniform distribution and distinct columns for single-checker rows).

And for s ≤ 1005, the adversary cannot block it (the worst s rows span ≤ s ≤ 1005 < 1007 = 2012 - 1005 columns).

Wait, for s = 1005: worst 1005 rows span ≤ 1005 columns. Need ≥ 2012 - 1005 = 1007. 1005 < 1007. ✗ So the adversary cannot block s = 1005.

For s = 1006: worst 1006 rows span ≤ 1006 columns. Need ≥ 1006. 1006 ≥ 1006. ✓ (if checkers are in distinct columns).

So the threshold is s = 1006. The adversary can block s = 1006 but not s = 1005.

This means: the largest s for which we can always find an empty s×s sub-board is s = 1005. So k = 2011 - 1005 = 1006.

But wait, I need to verify that the adversary can actually achieve s = 1006, i.e., place 3000 checkers so that every 1006×1006 sub-board has a checker. And I need to verify that for s = 1005, no matter how the adversary places 3000 checkers, there's always an empty 1005×1005 sub-board.

Let me also check: can the adversary do better than the uniform distribution? Maybe a different distribution allows blocking larger s?

**Adversary's optimization:** The adversary wants to maximize the minimum s they can block. The blocking condition for s is: every s rows span ≥ 2012 - s columns. The adversary controls the distribution of 3000 checkers.

The bottleneck is the worst s rows (fewest checkers). To maximize the minimum columns spanned by the worst s rows, the adversary should:
1. Make the distribution as even as possible (minimize the number of checkers in the worst rows).
2. Ensure checkers are in distinct columns within each row (maximize columns spanned per checker).

With 3000 checkers and 2011 rows, the most even distribution has each row with 1 or 2 checkers (1022 with 1, 989 with 2). The worst s rows (for s ≤ 1022) have 1 checker each, spanning at most s columns.

Can the adversary do better by using fewer rows? E.g., put all 3000 checkers in 1500 rows (2 each). Then 511 rows have 0 checkers. For s = 511, we can pick 511 empty rows, spanning 0 columns. Need 0 ≥ 2012 - 511 = 1501. ✗ So the adversary can't even block s = 511. Worse.

What about putting 3000 checkers in 1000 rows (3 each)? Then 1011 rows have 0 checkers. For s = 1011, pick all empty rows, span 0 columns. Need 0 ≥ 1001. ✗ Much worse.

So the uniform distribution (using all 2011 rows) is best for the adversary. The adversary should use all rows.

With all 2011 rows used (each with ≥ 1 checker), 3000 = 2011 + 989, so 989 rows get an extra checker. The worst s rows have 1 checker each (for s ≤ 1022).

So the adversary's best is s = 1006 (blocking empty 1006×1006 sub-boards).

Now let me verify both directions rigorously.

**Upper bound (k = 1006 suffices):** For any placement of 3000 checkers, there exist 1006 rows and 1006 columns covering all checkers. Equivalently, there's an empty 1005×1005 sub-board.

We need to show: for any placement of 3000 checkers on a 2011×2011 board, there exist 1005 rows and 1005 columns with no checker in their intersection.

Proof: Sort rows by number of checkers in decreasing order: a₁ ≥ a₂ ≥ ... ≥ a₂₀₁₁. The bottom 1005 rows have the fewest checkers. The total checkers in these 1005 rows is at most 3000 · 1005/2011 (by averaging). Actually, the bottom 1005 rows have at most 1005 · (3000/2011) ≈ 1500 checkers. But more precisely, the bottom 1005 rows have at most ⌊3000 · 1005 / 2011⌋ checkers.

Hmm, actually the sum of the smallest 1005 values is at most 1005 · (average) = 1005 · 3000/2011 ≈ 1500. But this is an upper bound on the sum, not directly useful.

Let me think differently. The bottom 1005 rows have at most 3000 - (checkers in top 1006 rows) checkers. The top 1006 rows have at least 1006 · 3000/2011 ≈ 1500 checkers. So the bottom 1005 rows have at most 3000 - 1500 = 1500 checkers.

These 1500 checkers are in at most 1500 columns. So the bottom 1005 rows have checkers in at most 1500 columns. Thus, there are at least 2011 - 1500 = 511 columns with no checker in any of the bottom 1005 rows.

We need 1005 columns with no checker in the bottom 1005 rows. But we only have 511 such columns. 511 < 1005. So this approach doesn't work directly.

Hmm, so the simple approach of taking the bottom 1005 rows doesn't give us enough empty columns. Let me reconsider.

The issue is that 3000 checkers in 1005 rows could span up to 1005 columns (if each row has 3 checkers in distinct columns, 1005 rows could span up to 2011 columns). Wait, 1005 rows with 1500 checkers could span up to 1500 columns (if all in distinct columns). Then 2011 - 1500 = 511 empty columns, which is less than 1005.

So the approach of taking the rows with fewest checkers doesn't directly work for s = 1005. Let me reconsider.

Maybe I need a different approach. Let me think about it as an optimization problem.

We want to find s rows and s columns with no checker in their intersection. This is equivalent to finding an independent set of size s in the row side and s in the column side in the bipartite graph (where edges are checkers).

Actually, it's finding a complete bipartite subgraph K_{s,s} in the complement graph (empty cells). The complement has n² - 3000 edges.

By the Kővári–Sós–Turán theorem, a bipartite graph on (n,n) with more than (t-1)^{1/t} n^{2-1/t} + (t-1)n edges contains K_{t,t}. But as we saw, this bound is weak for large t.

Let me try a different approach. Maybe I should think about the problem more directly.

**Direct approach for the upper bound:**

We want to show that for any 3000 checkers, we can find 1006 rows and 1006 columns covering all checkers. Equivalently, we can remove 1005 rows and 1005 columns to eliminate all checkers.

Strategy: Greedily remove rows/columns with the most checkers.

Actually, let me think about the problem as a vertex cover in the bipartite graph. We have a bipartite graph with 2011 + 2011 vertices and 3000 edges. We want a vertex cover with at most k vertices on each side. We want the minimum such k, maximized over all graphs with 3000 edges.

By König's theorem, the minimum vertex cover equals the maximum matching. But we have the additional constraint of balance (k on each side).

Let me think about the maximum matching. With 3000 edges on a 2011×2011 bipartite graph, the maximum matching can be at most 2011 (since each side has 2011 vertices). 

If the maximum matching is m, then the minimum vertex cover has size m. But we need a balanced cover (k on each side). 

If the minimum vertex cover has size m, can we always find a balanced cover with max(r,c) ≤ ⌈m/2⌉? Not necessarily, because the cover might be unbalanced.

Hmm, but actually, from a vertex cover of size m, we can potentially rebalance. If the cover has r rows and c columns with r + c = m, then max(r,c) ≥ ⌈m/2⌉. But can we always achieve max(r,c) = ⌈m/2⌉? Not necessarily, because the minimum vertex cover might be unique and unbalanced.

But we're not restricted to minimum vertex covers. We can use a larger cover that's more balanced. The question is: what's the minimum max(r,c) over all vertex covers (r rows, c columns)?

Let me think about this. Given a bipartite graph, we want min over all vertex covers (R', C') of max(|R'|, |C'|).

This is not a standard problem, but let me think about it.

For a matching of size m (m edges, no two sharing a vertex), any vertex cover needs at least m vertices (one per edge). If the matching uses m rows and m columns, a balanced cover needs max(r,c) ≥ ⌈m/2⌉. And we can achieve ⌈m/2⌉ by taking ⌈m/2⌉ rows and ⌊m/2⌋ columns from the matching. But we need to cover all edges, not just the matching.

OK let me think about this problem differently. Let me consider the specific structure.

**Key idea:** The answer might be 1006. Let me try to prove it.

**Lower bound (k ≥ 1006):** Construct a placement of 3000 checkers where any cover needs at least 1006 rows and 1006 columns.

Construction: Place a perfect matching of size 2011 (one checker in each row, each column, e.g., on the diagonal). Then add 989 more checkers in existing rows/columns.

Wait, a perfect matching of 2011 checkers requires max(r,c) ≥ ⌈2011/2⌉ = 1006 for any cover. Because each of the 2011 matching edges needs its row or column in the cover, and each row/column covers at most 1 matching edge. So r + c ≥ 2011, hence max(r,c) ≥ 1006.

But we have 3000 checkers, not 2011. The extra 989 checkers might force an even larger k. Or they might not, if they're covered by the same rows/columns.

Let me place the extra 989 checkers carefully. Place them in cells (i, i) for i = 1, ..., 989 (which already have matching checkers). Wait, we can't place two checkers in the same cell. Place them in cells (i, σ(i) + 1 mod 2011) for i = 1, ..., 989, where σ is the matching permutation. These are in rows 1-989 and columns that are different from the matching columns.

Hmm, this is getting complicated. Let me just use the perfect matching and add extra checkers in cells that are already covered by any cover of the matching.

Actually, the extra checkers can only increase k, not decrease it. So if the matching alone requires k ≥ 1006, then with extra checkers, k ≥ 1006. But can the extra checkers force k > 1006?

Consider a cover of the matching with r = 1006 rows and c = 1005 columns (r + c = 2011). This covers all matching edges. Does it cover the extra 989 checkers?

An extra checker at (i, j) is covered if row i is in the cover or column j is in the cover. If neither is in the cover, it's not covered. For the matching to be covered, if row i is not in the cover, then column σ(i) must be in the cover (to cover matching edge (i, σ(i))). Similarly, if column j is not in the cover, then row σ⁻¹(j) must be in the cover.

So an extra checker at (i, j) is uncovered iff row i ∉ cover and column j ∉ cover. But then column σ(i) ∈ cover (to cover (i, σ(i))) and row σ⁻¹(j) ∈ cover (to cover (σ⁻¹(j), j)).

So the uncovered extra checkers are those (i, j) where row i and column j are both not in the cover. The uncovered rows are 2011 - 1006 = 1005 rows, and uncovered columns are 2011 - 1005 = 1006 columns. The uncovered region is 1005 × 1006.

If we place extra checkers in this uncovered region, they won't be covered. But the adversary doesn't know which cover we'll choose. The adversary places checkers first, then we choose the cover.

So the adversary needs: for every cover (r rows, c columns) of the matching with r + c = 2011 and max(r,c) = 1006, the extra checkers are not all covered. I.e., for every such cover, at least one extra checker is in the uncovered region.

The uncovered region for a cover (R', C') with |R'| = 1006, |C'| = 1005 is (rows not in R') × (columns not in C'), which has size 1005 × 1006. The adversary needs to place 989 extra checkers so that every such uncovered region contains at least one.

The number of possible covers is large. But the adversary only needs to hit all possible uncovered regions. An uncovered region is determined by choosing 1005 rows and 1006 columns (the complement of the cover). The adversary needs: for every 1005 rows and 1006 columns, at least one extra checker in their intersection.

This is the hitting set problem for 1005×1006 sub-boards. The minimum hitting set size is f(1005, 1006) (generalizing to rectangular).

By similar analysis, f(a, b) = minimum checkers to hit all a×b sub-boards. With n = 2011, f(a, b) = n² - z(n, n, a, b) where z is the max edges in bipartite graph on (n,n) with no K_{a,b}.

This is getting very complex. Let me step back and think about whether the answer is indeed 1006.

Actually, let me reconsider the lower bound construction. The perfect matching gives k ≥ 1006. Can the adversary do better (achieve k > 1006)?

With 3000 checkers, can the adversary force k ≥ 1007? That would require: for every cover with 1006 rows and 1006 columns, at least one checker is uncovered. I.e., for every 1005 rows and 1005 columns, at least one checker is in their intersection. I.e., the adversary can hit all 1005×1005 sub-boards with 3000 checkers.

From our earlier analysis, the adversary can hit all 1006×1006 sub-boards with 3000 checkers (using the uniform distribution). Can they hit all 1005×1005 sub-boards?

For 1005×1005: the condition is every 1005 rows span ≥ 2012 - 1005 = 1007 columns. The worst 1005 rows (with 1 checker each, in the uniform distribution) span at most 1005 columns. 1005 < 1007. ✗

So with the uniform distribution, the adversary cannot hit all 1005×1005 sub-boards. Can a different distribution do better?

The adversary needs: every 1005 rows span ≥ 1007 columns. The worst 1005 rows have at most ⌊3000 · 1005 / 2011⌋ = ⌊1500.7⌋ = 1500 checkers. Wait, that's the sum of the smallest 1005 a_i's, which is at most 1005 · (3000/2011) ≈ 1500. But the adversary controls the distribution.

To maximize the minimum columns spanned by any 1005 rows, the adversary wants to maximize the number of checkers in the worst 1005 rows, and spread them across columns.

The worst 1005 rows have at most ⌊3000 · 1005 / 2011⌋ checkers? No, that's not right. The sum of the smallest 1005 values of a_i (where Σa_i = 3000, 0 ≤ a_i ≤ 2011) is maximized when the distribution is as even as possible. With 3000 checkers and 2011 rows, the most even distribution has 989 rows with 2 and 1022 with 1. The smallest 1005 values: 1005 rows with 1 checker each (since 1022 ≥ 1005). Sum = 1005.

So the worst 1005 rows have exactly 1005 checkers (in the best case for the adversary). These span at most 1005 columns. The adversary needs ≥ 1007. 1005 < 1007. ✗

Can the adversary use a different distribution? If the adversary puts more checkers in some rows, other rows have fewer, making the worst 1005 rows even worse. If the adversary puts fewer checkers in some rows (0), the worst 1005 rows could include those, making it worse.

The most even distribution maximizes the minimum sum of any 1005 rows. With 3000 = 2011 + 989, the most even is 989 rows with 2, 1022 with 1. The worst 1005 rows have 1005 checkers. No other distribution can do better (any deviation makes some rows have fewer checkers).

So the adversary cannot hit all 1005×1005 sub-boards with 3000 checkers. Therefore, for any 3000-checker placement, there's an empty 1005×1005 sub-board, meaning k = 1006 suffices.

Wait, but I need to be more careful. The condition for hitting all s×s sub-boards is that every s rows span ≥ n - s + 1 columns. But "span" means the number of distinct columns with checkers in those rows. Even if the worst 1005 rows have 1005 checkers, if they're all in distinct columns, they span 1005 columns. The adversary needs ≥ 1007. 1005 < 1007. So the adversary can't do it.

But wait, is the condition "every s rows span ≥ n - s + 1 columns" both necessary and sufficient?

Sufficient: If every s rows span ≥ n - s + 1 columns, then for any s rows R, the columns with checkers in R have size ≥ n - s + 1, so the columns without checkers in R have size ≤ n - (n - s + 1) = s - 1 < s. So we can't find s columns all without checkers in R. So every s×s sub-board has a checker. ✓

Necessary: If there exist s rows spanning ≤ n - s columns, then the columns without checkers in those rows have size ≥ n - (n - s) = s. So we can find s columns all without checkers in those s rows, forming an empty s×s sub-board. ✗ for the adversary.

So the condition is exactly: every s rows span ≥ n - s + 1 columns. (Note: n - s + 1, not n - s.)

Let me redo with n = 2011, s = 1005: need every 1005 rows span ≥ 2011 - 1005 + 1 = 1007 columns. Worst 1005 rows have 1005 checkers, spanning ≤ 1005 < 1007. ✗ So adversary can't block. ✓

For s = 1006: need every 1006 rows span ≥ 2011 - 1006 + 1 = 1006 columns. Worst 1006 rows have 1006 checkers, spanning ≤ 1006. Need ≥ 1006. If checkers are in distinct columns, span = 1006 ≥ 1006. ✓ So adversary can block (with the right placement).

So the answer is k = 2011 - 1005 = 1006.

Wait, let me double-check. The largest s such that the adversary cannot block is s = 1005. So k = n - s = 2011 - 1005 = 1006.

But I need to verify that the adversary CAN block s = 1006, i.e., place 3000 checkers so that every 1006 rows span ≥ 1006 columns.

**Adversary construction for s = 1006:**

Place checkers as follows:
- 1022 rows have 1 checker each, in distinct columns (columns 1 through 1022).
- 989 rows have 2 checkers each, in columns 1023 through 2011 (each of these 989 rows has 2 checkers in this range).

Wait, 989 rows with 2 checkers each = 1978 checkers, using columns 1023-2011 (989 columns). Each column gets about 2 checkers. Plus 1022 checkers in columns 1-1022. Total: 1022 + 1978 = 3000. ✓

Now check: every 1006 rows span ≥ 1006 columns.

Case 1: 1006 rows all from the 1022 single-checker rows. Each has 1 checker in a distinct column (columns 1-1022). So they span 1006 distinct columns. ✓ (1006 ≥ 1006).

Case 2: 1006 rows include some double-checker rows. Say j double-checker rows and 1006 - j single-checker rows (j ≥ 1). The single-checker rows contribute 1006 - j distinct columns (from 1-1022). The double-checker rows contribute checkers in columns 1023-2011. Even if all j double-checker rows share the same 2 columns, they add 2 new columns. Total spanned: (1006 - j) + 2 = 1008 - j. For j ≤ 2, this is ≥ 1006. For j > 2, the single-checker rows contribute 1006 - j < 1004, but the double-checker rows contribute up to 2j columns. Total: (1006 - j) + min(2j, 989). For j ≤ 989, this is 1006 - j + 2j = 1006 + j ≥ 1006. ✓ (assuming the double-checker rows' columns are all new, i.e., in 1023-2011, which they are).

Wait, but what if some double-checker rows have checkers in columns 1-1022 (overlapping with single-checker rows)? In my construction, double-checker rows only use columns 1023-2011, so no overlap. So the total spanned is (1006 - j) + (columns from double-checker rows in 1023-2011). The double-checker rows have 2j checkers in columns 1023-2011, spanning at most min(2j, 989) columns. But we need the total to be ≥ 1006.

Total spanned = (1006 - j) + (span of double-checker rows). The span of j double-checker rows is at least... well, it could be as low as 2 (if all j rows share the same 2 columns). So total ≥ (1006 - j) + 2 = 1008 - j. For j ≤ 2, this is ≥ 1006. For j = 3, 1005 < 1006. ✗!

Hmm, so if we pick 3 double-checker rows that all share the same 2 columns, and 1003 single-checker rows, the total span is 1003 + 2 = 1005 < 1006. This violates the condition!

So my construction doesn't work. I need to be more careful.

The issue is that double-checker rows might share columns. I need to ensure that any j double-checker rows span enough new columns.

Alternative: make the double-checker rows also have checkers in distinct columns. But 989 rows with 2 checkers each need 1978 checkers in distinct column-pairs, but columns 1023-2011 only have 989 columns. So each column is used by about 2 rows. Two rows sharing a column is inevitable.

Let me reconsider. Maybe I need a different construction.

**Better construction:** Place 3000 checkers as a "partial matching" plus extras. 

Actually, let me think about this differently. The condition is: every 1006 rows span ≥ 1006 columns. This is equivalent to: the bipartite complement graph (empty cells) has no K_{1006, 1006}.

We need to place 3000 checkers (edges in the original graph) so that the complement has no K_{1006, 1006}. The complement has n² - 3000 edges. We need: any bipartite graph on (2011, 2011) with n² - 3000 edges contains K_{1006, 1006}.

Hmm wait, we need the opposite: we need to show there EXISTS a placement of 3000 checkers such that the complement has no K_{1006, 1006}. And we need to show that for ANY placement of 3000 checkers, the complement has K_{1005, 1005}.

For the lower bound (k ≥ 1006), we need to exhibit a placement of 3000 checkers such that no 1006 rows and 1006 columns cover all checkers. I.e., the complement has no K_{1005, 1005}.

Wait, I'm getting confused. Let me re-clarify.

k rows and k columns cover all checkers iff the (n-k)×(n-k) sub-board of unselected rows and columns is empty. So:
- k works for a placement iff there's an empty (n-k)×(n-k) sub-board.
- k doesn't work iff every (n-k)×(n-k) sub-board has a checker.

For the lower bound (k ≥ 1006), we need a placement where k = 1005 doesn't work, i.e., every 1006×1006 sub-board has a checker. (Since n - 1005 = 1006.)

For the upper bound (k ≤ 1006), we need: for every placement, k = 1006 works, i.e., there's an empty 1005×1005 sub-board. (Since n - 1006 = 1005.)

So:
- Lower bound: exhibit 3000 checkers hitting all 1006×1006 sub-boards.
- Upper bound: show any 3000 checkers leave an empty 1005×1005 sub-board.

For the upper bound: every 1005 rows span ≥ 1007 columns is needed by the adversary. The worst 1005 rows have at most 1005 checkers (in the best distribution for the adversary), spanning ≤ 1005 < 1007. So the adversary can't block. ✓

For the lower bound: every 1006 rows span ≥ 1006 columns is needed. We need to construct 3000 checkers achieving this.

The issue with my previous construction was that double-checker rows might share columns. Let me think about how to fix this.

**Construction:** Place 3000 checkers such that:
- Each row has 1 or 2 checkers (1022 rows with 1, 989 with 2).
- The checkers are placed so that any 1006 rows span ≥ 1006 columns.

The critical case is when we pick 1006 rows with the fewest checkers. If we pick 1006 single-checker rows, they span 1006 columns (if checkers are in distinct columns). ✓

If we pick some double-checker rows, the total checkers increase, but the spanned columns might not increase enough if double-checker rows share columns with single-checker rows or with each other.

Key insight: if double-checker rows have their checkers in columns that are NOT used by single-checker rows, then any set of rows that includes both types spans (single-checker columns) + (double-checker columns), and the double-checker columns are all new.

Let me refine:
- 1022 single-checker rows: checkers in columns 1-1022 (one per row, all distinct).
- 989 double-checker rows: checkers in columns 1023-2011 (989 columns, 1978 checkers).

Now, any set of 1006 rows:
- j double-checker rows, 1006-j single-checker rows.
- Single-checker rows span 1006-j columns (from 1-1022, all distinct).
- Double-checker rows span some columns from 1023-2011.
- Total spanned = (1006-j) + (span of j double-checker rows in 1023-2011).

The span of j double-checker rows: each has 2 checkers in columns 1023-2011. The minimum span is 2 (if all share the same 2 columns). But we need total ≥ 1006, so (1006-j) + span ≥ 1006, i.e., span ≥ j.

So we need: any j double-checker rows span ≥ j columns (in columns 1023-2011). Since each double-checker row has 2 checkers, j rows have 2j checkers. If these span ≥ j columns, we're fine.

When do j rows with 2 checkers each span < j columns? This means the 2j checkers are in fewer than j columns, i.e., some columns have ≥ 3 checkers. But each column has at most... well, the adversary controls this.

In our construction, 989 double-checker rows have 1978 checkers in 989 columns (1023-2011). Average 2 per column. If we arrange it so each column has exactly 2 checkers (a 2-regular bipartite graph on 989 rows and 989 columns), then any j rows have 2j checkers in some columns. The minimum span of j rows: if the 2-regular graph is a union of cycles, then j consecutive rows in a cycle span j columns (in a cycle of length L, j consecutive rows span j columns). But non-consecutive rows could span fewer.

Actually, in a 2-regular bipartite graph (union of even cycles), any j rows have 2j edges. The minimum number of columns spanned by j rows: consider a cycle of length 2L (L rows, L columns, 2L edges). If we pick j ≤ L rows from this cycle, they have 2j edges, spanning at least j+1 columns (in a cycle, j rows are adjacent to at least j+1 columns, unless j = L in which case they span L columns). Wait, in a cycle C_{2L}, j rows have 2j edges. If the j rows are consecutive in the cycle, they span j+1 columns (for j < L) or L columns (for j = L). If the j rows are not consecutive, they span more. So the minimum span is j+1 for j < L, and L for j = L.

Hmm, so for j < L, span ≥ j + 1 > j. For j = L, span = L = j. So span ≥ j always. ✓

But what if the graph is not a single cycle but multiple cycles? If j rows are from a cycle of length L < j, then we need j > L rows from a cycle of length L, which means all L rows from that cycle plus some from another. All L rows from a cycle of length L span L columns. Plus rows from another cycle span more. So total ≥ L + (something) ≥ j (since j ≤ L + (rows from other cycles), and those other rows contribute their own columns).

Actually, let me think about this more carefully. In a 2-regular bipartite graph (union of cycles), any set of j rows spans at least j columns. This is because the graph is a union of cycles, and in each cycle, the rows and columns are in 1-1 correspondence (L rows ↔ L columns). So j rows from a cycle of length L (j ≤ L) span at least j columns (since each row is adjacent to 2 columns, and in a cycle, the j rows are adjacent to at least j distinct columns).

More formally: in a 2-regular bipartite graph, the rows and columns in each connected component (cycle) are equinumerous. For any set of j rows, the columns spanned are at least j (by Hall's theorem, since the graph restricted to these j rows has each row with degree 2, and the graph is a union of cycles, so Hall's condition is satisfied).

Wait, is that true? Hall's theorem says j rows can be matched to j distinct columns iff for every subset S of these rows, |N(S)| ≥ |S|. In a 2-regular graph (union of cycles), for any subset S of rows, |N(S)| ≥ |S| because each row has degree 2 and the graph is a disjoint union of cycles (which are 2-regular, so Hall's condition holds). Actually, in a cycle, any subset of rows has at least as many neighbors. In a cycle of length 2L (L rows, L columns), any subset of k rows has at least k neighbors (since the cycle is a 2-regular bipartite graph, which satisfies Hall's condition). So by Hall's theorem, any j rows can be matched to j columns, meaning they span ≥ j columns. ✓

So in our construction, any j double-checker rows span ≥ j columns. Therefore, any 1006 rows (j double + 1006-j single) span ≥ (1006-j) + j = 1006 columns. ✓

So the construction works! Let me verify the details:

**Construction:**
- Rows 1-1022: each has 1 checker, in columns 1-1022 respectively (row i has checker in column i, for i = 1, ..., 1022). This is a matching of size 1022.
- Rows 1023-2011 (989 rows): each has 2 checkers in columns 1023-2011 (989 columns). The checkers form a 2-regular bipartite graph between rows 1023-2011 and columns 1023-2011 (e.g., a union of cycles covering all 989 rows and 989 columns).

Total checkers: 1022 + 2 × 989 = 1022 + 1978 = 3000. ✓

**Verification that every 1006×1006 sub-board has a checker:**

Take any 1006 rows. Let j be the number of double-checker rows among them (0 ≤ j ≤ 989), and 1006-j single-checker rows.

- The 1006-j single-checker rows have checkers in 1006-j distinct columns (from columns 1-1022).
- The j double-checker rows have checkers in columns 1023-2011. By the 2-regular property (Hall's theorem), they span ≥ j columns.

Total columns spanned: ≥ (1006-j) + j = 1006.

So the 1006 rows span ≥ 1006 columns, meaning the columns WITHOUT checkers in these rows are ≤ 2011 - 1006 = 1005 < 1006. So we can't find 1006 columns all without checkers in these 1006 rows. Therefore, every 1006×1006 sub-board has a checker. ✓

**Upper bound: any 3000 checkers leave an empty 1005×1005 sub-board.**

For any placement of 3000 checkers, sort rows by checker count: a₁ ≥ a₂ ≥ ... ≥ a₂₀₁₁. The 1005 rows with the fewest checkers (rows 1007-2011 in this ordering) have at most 1005 checkers total.

Wait, why? The sum of the smallest 1005 values is at most 1005 × (3000/2011) ≈ 1500. That's not 1005.

Hmm, I need a tighter bound. Let me think again.

The sum of the smallest 1005 a_i's: with Σa_i = 3000 and 2011 values, the sum of the smallest 1005 is at most... 

If the distribution is as even as possible (989 twos, 1022 ones), the smallest 1005 are all 1's, sum = 1005. But if the distribution is uneven, the smallest 1005 could be smaller.

Actually, the sum of the smallest 1005 values is maximized when the distribution is as even as possible. With 3000 = 2011 + 789... wait, 3000 - 2011 = 989. So 989 rows get an extra checker. The most even distribution: 989 rows with 2, 1022 with 1. The smallest 1005 values are all 1 (since 1022 ≥ 1005), sum = 1005.

But could a less even distribution give a larger sum for the smallest 1005? No! Making the distribution more uneven means some values increase and others decrease, so the smallest values decrease. The most even distribution maximizes the minimum values.

So the sum of the smallest 1005 a_i's is at most 1005 (achieved by the most even distribution). Wait, is that right? Let me verify.

With 3000 checkers and 2011 rows, if we want to maximize the sum of the smallest 1005 a_i's, we should make all a_i's as equal as possible. The most equal distribution is 989 rows with 2 and 1022 with 1. The smallest 1005 are 1's, sum = 1005.

Could we do better? What if we use 3 rows with 1000 checkers each and 2008 rows with 0? Then the smallest 1005 have 0, sum = 0. Worse.

What about 1000 rows with 3 and 1011 rows with 0? Smallest 1005 have 0, sum = 0. Worse.

What about 1500 rows with 2 and 511 rows with 0? Smallest 1005: 511 zeros + 494 twos, sum = 988. Worse than 1005.

So the most even distribution (989 twos, 1022 ones) maximizes the sum of the smallest 1005, giving 1005.

Wait, but what about a distribution where all rows have at least 1? Then 3000 - 2011 = 989 extra checkers. The most even: 989 rows with 2, 1022 with 1. Sum of smallest 1005 = 1005.

What if some rows have 0? Then the remaining rows have more, but the smallest 1005 include those 0s, making the sum smaller. So having all rows with ≥ 1 is better.

What if some rows have 3? Then 3000 = 2011 + 989, and if x rows have 3, they use 2x extra checkers, leaving 989 - 2x extra for rows with 2. So x rows with 3, 989 - 2x rows with 2, 2011 - x - (989-2x) = 1022 + x rows with 1. The smallest 1005: if 1022 + x ≥ 1005 (i.e., x ≥ -17, always true), then the smallest 1005 are all 1's, sum = 1005. Same!

So as long as all rows have ≥ 1 and at least 1005 rows have exactly 1, the sum of the smallest 1005 is 1005. This is the case when the number of rows with ≥ 2 is at most 2011 - 1005 = 1006. Since 3000 - 2011 = 989 ≤ 1006, we can have at most 989 rows with ≥ 2 (if each has exactly 2), leaving 1022 rows with 1. So the sum of the smallest 1005 is always ≤ 1005.

Wait, but what if some
