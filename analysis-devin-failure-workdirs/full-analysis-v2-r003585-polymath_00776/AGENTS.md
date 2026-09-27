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
  <problem_id>polymath_00776</problem_id>
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

A \(100 \times 100\) table is covered with \(5000\) dominoes. We will call a square \(2 \times 2\) exact if it is covered with two dominoes. What is the minimum number of exact squares that can be in the table?

## Standard Solution

Let \(k\) be the number of dominoes that touch an outer edge of the table with their long side; each of them is located in a unique \(2 \times 2\) square, and clearly \(k \leq 198\). Each of the remaining \(5000 - k\) dominoes is located in two \(2 \times 2\) squares. The total number of squares containing dominoes is \(k + 2(5000 - k) = 10000 - k \geq 9802\). But there are \(99 \times 99 = 9801\) squares \(2 \times 2\) in the table, so at least one of them contains two dominoes, i.e., is exact. The exact square can only be one: for example, we can cover the outer frame with dominoes, then the inner one, so that no exact square is formed, then the third, and so on; an exact square will only be in the center.

\(\boxed{1}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. A 100×100 table covered with 5000 dominoes. A 2×2 square is "exact" if covered with two dominoes. Find minimum number of exact squares.

Let me think about this carefully.

A 100×100 board has 10000 squares, covered by 5000 dominoes (each domino covers 2 adjacent squares).

A 2×2 square is "exact" if it's covered by exactly 2 dominoes (so the two dominoes both lie within this 2×2 square, forming either two horizontal or two vertical dominoes).

The number of 2×2 squares in a 100×100 board is 99×99 = 9801.

We want to minimize the number of 2×2 squares that are "exact" (covered by exactly 2 dominoes).

Let me think about a checkerboard coloring. Color the board in checkerboard pattern (black/white). Each domino covers one black and one white square.

Now consider the 2×2 squares. A 2×2 square has 2 black and 2 white squares. If it's covered by 2 dominoes, both dominoes are within the 2×2 square. If it's not exact, then at least one domino crosses the boundary of the 2×2 square.

Let me think about a different approach. Consider the grid lines. 

Actually, let me think about this problem differently. Let me consider the standard approach for such problems.

Consider dividing the 100×100 board into 2×2 blocks. There are 50×50 = 2500 such blocks. In each 2×2 block, if it's covered by 2 dominoes, it's "exact". 

But the 2×2 squares can be at any position, not just aligned to a 2×2 grid. There are 99×99 = 9801 possible 2×2 squares.

Hmm, let me think about what configurations minimize exact squares.

A "brick wall" pattern: place all dominoes horizontally in rows, but offset alternating rows. In row 1, place dominoes at columns (1,2), (3,4), ..., (99,100). In row 2, place dominoes at columns (2,3), (4,5), ..., (98,99), and then we need to handle columns 1 and 100 in row 2.

Wait, that doesn't work cleanly because of the boundary.

Let me think again. If all dominoes are horizontal:
- Row i: dominoes at (i, 1-2), (i, 3-4), ..., (i, 99-100). This covers each row with 50 horizontal dominoes.

In this case, a 2×2 square at position (i,j) to (i+1, j+1) is exact if and only if both rows have domino boundaries at the same place. If row i has dominoes at (j, j+1) and row i+1 has dominoes at (j, j+1), then the 2×2 square is exact (two horizontal dominoes).

If all rows have the same pattern (dominoes at (1,2), (3,4), ...), then every 2×2 square starting at odd column j is exact. There are 99 rows of 2×2 squares and 50 odd columns (j=1,3,5,...,99), giving 99×50 = 4950 exact squares. Wait, j ranges from 1 to 99, and odd j gives 50 values. So 99 × 50 = 4950.

But we can offset alternate rows. If even rows have dominoes at (2,3), (4,5), ..., (98,99), and we need to handle columns 1 and 100 in even rows. Column 1 in even rows: we could place a vertical domino. Similarly column 100.

Actually, let me think about this more carefully with the offset pattern.

Pattern: 
- Odd rows (1, 3, 5, ...): horizontal dominoes at (1-2), (3-4), ..., (99-100). 50 dominoes per row.
- Even rows (2, 4, 6, ...): horizontal dominoes at (2-3), (4-5), ..., (98-99). That's 49 dominoes, covering columns 2-99. Columns 1 and 100 are uncovered in even rows.

For columns 1 and 100 in even rows, we need vertical dominoes. Column 1, even rows: place vertical dominoes at (2,1)-(3,1), (4,1)-(5,1), ..., but wait, rows 2,3 are different types. Let me reconsider.

Actually, let me pair up rows. Rows (1,2), (3,4), ..., (99,100). In each pair, the odd row has dominoes at odd positions and the even row has dominoes at even positions. The uncovered cells in even rows are at columns 1 and 100.

For the pair (row 2k-1, row 2k): 
- Row 2k-1: horizontal dominoes at (1-2), (3-4), ..., (99-100).
- Row 2k: horizontal dominoes at (2-3), (4-5), ..., (98-99). Uncovered: (2k, 1) and (2k, 100).

We need to cover (2k, 1) and (2k, 100). We can use vertical dominoes: (2k, 1)-(2k+1, 1) and (2k, 100)-(2k+1, 100). But row 2k+1 is an odd row which already has (2k+1, 1) covered by a horizontal domino (2k+1, 1-2). Conflict!

So this doesn't work directly. Let me think differently.

Alternative: use vertical dominoes for the boundary cells. (2k, 1) can be covered by a vertical domino (2k-1, 1)-(2k, 1). But (2k-1, 1) is already covered by the horizontal domino (2k-1, 1-2). Conflict again.

Hmm. So the offset pattern has issues at the boundaries.

Let me think about this differently. Maybe use a different tiling.

Actually, let me consider a simpler approach. Let me think about what the answer might be and work towards it.

Let me consider the problem on a general m×n board. 

Key insight: Consider the "fault line" / "crossing" approach.

Let me think about it from the perspective of counting. 

Each 2×2 square that is NOT exact has at least one domino crossing its boundary. A domino can cross the boundary of at most... let me think. A horizontal domino at (i, j)-(i, j+1) is inside the 2×2 square (i, j)-(i+1, j+1) or (i-1, j)-(i, j+1). It crosses the boundary of 2×2 squares that contain exactly one of its two cells.

Actually, let me think about it differently. 

A 2×2 square at position (r, c) (top-left corner, covering rows r, r+1 and columns c, c+1) is exact iff no domino crosses its boundary. A domino crosses the boundary of this 2×2 square if the domino has one cell inside and one cell outside the 2×2 square.

For a 2×2 square to be non-exact, at least one domino must cross its boundary. But actually, it's possible that a 2×2 square is covered by 3 or 4 dominoes (if dominoes cross in and out). 

Wait, actually a 2×2 square has 4 cells. If it's covered by 2 dominoes, both dominoes are entirely within the 2×2 square. If covered by 3 dominoes, one domino is within and two cross the boundary (or other configurations). If covered by 4 dominoes, all four dominoes cross the boundary.

So a 2×2 square is exact iff it's covered by exactly 2 dominoes, which means both dominoes lie entirely within it.

Let me count the total number of 2×2 squares and the maximum number that can be non-exact.

Total 2×2 squares: 99 × 99 = 9801.

Each non-exact 2×2 square has at least one domino crossing its boundary. Let me count how many 2×2 squares a single domino can "spoil" (make non-exact by crossing their boundary).

A horizontal domino at (i, j)-(i, j+1): It lies entirely within the 2×2 squares (i, j-1) [if j > 1], (i, j) [covering columns j, j+1], (i-1, j) [if i > 1], and (i-1, j-1) [if i > 1 and j > 1]. Wait, let me be more careful.

A 2×2 square with top-left corner (r, c) covers cells (r,c), (r,c+1), (r+1,c), (r+1,c+1).

A horizontal domino at (i, j)-(i, j+1) is entirely within the 2×2 square (r, c) iff r ∈ {i-1, i} and c = j (so that columns j and j+1 are covered) and r+1 ∈ {i, i+1} which is satisfied. So the domino is within 2×2 squares (i-1, j) and (i, j), provided they exist (i.e., i-1 ≥ 1 and i ≤ 99, j ≤ 99).

The domino crosses the boundary of a 2×2 square (r, c) if exactly one of (i,j) and (i,j+1) is in the 2×2 square. 

(i,j) is in 2×2 square (r,c) iff r ∈ {i-1, i} and c ∈ {j-1, j}.
(i,j+1) is in 2×2 square (r,c) iff r ∈ {i-1, i} and c ∈ {j, j+1}.

Exactly one is in the square iff:
- (i,j) in, (i,j+1) not in: r ∈ {i-1, i} and c = j-1 (so (i,j) is in but (i,j+1) has column j+1 which needs c ∈ {j, j+1}, but c = j-1 means c+1 = j, so (i,j+1) has column j+1, and c = j-1 means the square covers columns j-1, j, so j+1 is not in). Yes, this works when c = j-1, i.e., the 2×2 square covers columns j-1, j, and the domino's cell (i,j) is in but (i,j+1) is not.
- (i,j) not in, (i,j+1) in: r ∈ {i-1, i} and c = j+1 (square covers columns j+1, j+2, so (i,j+1) is in but (i,j) is not).

So a horizontal domino at (i, j)-(i, j+1) crosses the boundary of 2×2 squares:
- (i-1, j-1), (i, j-1) [if j > 1]: the domino's left cell is in, right cell is out.
- (i-1, j+1), (i, j+1) [if j+1 ≤ 99, i.e., j ≤ 98]: the domino's right cell is in, left cell is out.

So a horizontal domino crosses the boundary of at most 4 two-by-two squares (2 on each side). But it's also entirely within 2 two-by-two squares (those at (i-1, j) and (i, j)).

Hmm, this counting approach might be complex. Let me think of another way.

Let me think about the problem in terms of a known result. I believe the answer to this problem is 4900 or something related.

Actually, let me think about it more carefully.

Let me consider the "brick wall" pattern more carefully and count exact squares.

Pattern 1: All dominoes horizontal, same alignment in every row.
- Dominoes at (i, 1-2), (i, 3-4), ..., (i, 99-100) for every row i.
- A 2×2 square at (r, c) is exact iff both rows r and r+1 have a domino covering columns c and c+1. This happens when c is odd (c = 1, 3, 5, ..., 99). So exact squares: 99 rows × 50 odd columns = 4950.

Pattern 2: Alternating alignment.
- Odd rows: dominoes at (1-2), (3-4), ..., (99-100).
- Even rows: we need to handle the boundary issue.

Let me try a different approach to the boundary issue. What if we use vertical dominoes at the boundaries?

Consider the board divided into 2×2 blocks: blocks at (2i-1, 2j-1) for i=1..50, j=1..50. Each block is a 2×2 square.

In each block, we can either:
(a) Place 2 horizontal dominoes (exact block)
(b) Place 2 vertical dominoes (exact block)
(c) Place dominoes that cross block boundaries (non-exact block)

If we want to minimize exact 2×2 squares, we want to maximize dominoes crossing boundaries. But we need to be careful because crossing boundaries creates exact squares at shifted positions.

Let me think about the "brick wall" pattern where we shift every other row by 1.

Rows 1, 3, 5, ..., 99 (odd rows): horizontal dominoes at columns (1,2), (3,4), ..., (99,100).
Rows 2, 4, 6, ..., 100 (even rows): horizontal dominoes at columns (2,3), (4,5), ..., (98,99), plus we need to cover columns 1 and 100.

For even rows, columns 1 and 100 are uncovered. We can cover them with vertical dominoes:
- (1,1)-(2,1): but (1,1) is already covered by the horizontal domino (1,1)-(1,2). Conflict.

So we can't do this directly. The issue is that in odd rows, column 1 is covered by a horizontal domino.

Alternative: What if we use vertical dominoes at the left and right edges?

Let me try a different pattern. Consider columns 1 and 100 as "special columns" handled with vertical dominoes, and the interior with the brick pattern.

Columns 1 and 100: Use vertical dominoes (1,1)-(2,1), (3,1)-(4,1), ..., (99,1)-(100,1). Similarly for column 100. This uses 50 + 50 = 100 dominoes and covers columns 1 and 100 completely.

Interior (columns 2 to 99, 98 columns):
- Odd rows: horizontal dominoes at (2,3), (4,5), ..., (98,99). That's 49 dominoes per odd row, covering columns 2-99.
- Even rows: horizontal dominoes at (3,4), (5,6), ..., (97,98). That's 48 dominoes per even row, covering columns 3-98. But columns 2 and 99 in even rows are uncovered!

Hmm, this is getting complicated. Let me think about it differently.

Actually, let me try the approach where we use vertical dominoes on the boundary columns and horizontal dominoes in the interior with a brick pattern.

Let me use columns 1 and 100 with vertical dominoes: (2k-1, 1)-(2k, 1) and (2k-1, 100)-(2k, 100) for k = 1, ..., 50. That's 100 dominoes.

Now for the interior, columns 2-99 (98 columns), rows 1-100:
- Odd rows (1, 3, ..., 99): horizontal dominoes at (2,3), (4,5), ..., (96,97), (98,99). Wait, 98 to 99 is the last pair. Columns 2-99: (2,3), (4,5), ..., (98,99). That's 49 dominoes.
- Even rows (2, 4, ..., 100): horizontal dominoes at (3,4), (5,6), ..., (97,98). That's 48 dominoes, covering columns 3-98. Columns 2 and 99 are uncovered in even rows.

So in even rows, columns 2 and 99 are uncovered. We need 2 more dominoes per even row, but we can't use horizontal dominoes for single cells. We'd need vertical dominoes, but the rows above and below are odd rows where columns 2 and 99 are already covered.

This doesn't work. The brick pattern on a grid with even number of columns has boundary issues.

Let me try yet another approach. What if the interior has 98 columns, and we use a brick pattern that works?

98 columns. In odd rows: (2,3), (4,5), ..., (98,99) — 49 dominoes, covers all 98 columns.
In even rows: we need to cover columns 2-99 with horizontal dominoes offset by 1. (3,4), (5,6), ..., (97,98) — 48 dominoes, covers columns 3-98. Columns 2 and 99 uncovered.

The problem is that 98 is even, so offsetting by 1 leaves 2 cells uncovered.

What if we don't use vertical dominoes on the boundary and instead handle it differently?

Let me try a completely different approach. Let me think about the problem theoretically.

Claim: The minimum number of exact 2×2 squares is 4900.

Wait, let me reconsider. Let me think about what patterns are possible.

Actually, I recall that for this type of problem, the answer involves a parity/coloring argument. Let me think about it.

Consider coloring the board with 4 colors in a 2×2 pattern:
```
A B A B ...
C D C D ...
A B A B ...
C D C D ...
```

Each 2×2 square (aligned to the grid) has one of each color. A domino covers two adjacent cells. A horizontal domino covers either (A,B) or (C,D) or (B,A) or (D,C). A vertical domino covers either (A,C) or (B,D) or (C,A) or (D,B).

Hmm, this might not directly help.

Let me think about another approach. Consider the "grid graph" where vertices are cells and edges connect adjacent cells. Dominoes are a perfect matching. A 2×2 square is exact iff the matching restricted to those 4 vertices consists of 2 edges within the square.

Let me think about the problem in terms of "fault lines." A fault line is a grid line that no domino crosses. If we have a vertical fault line between columns j and j+1, then no domino crosses from column j to column j+1. 

If there are no vertical fault lines and no horizontal fault lines, then... hmm, but we can still have exact squares.

Let me think about the lower bound.

Consider the 99 vertical grid lines (between columns) and 99 horizontal grid lines (between rows). A domino crosses at most one grid line. 

A 2×2 square at (r, c) is exact iff the matching on those 4 cells uses only edges within the square. This means:
- No domino crosses the horizontal line between rows r and r+1 within columns c and c+1.
- No domino crosses the vertical line between columns c and c+1 within rows r and r+1.
- Actually, more precisely, the 4 cells are covered by 2 dominoes, both within the square.

Let me think about it from the perspective of the 2×2 blocks aligned to the grid.

Divide the 100×100 board into 50×50 = 2500 non-overlapping 2×2 blocks. Each block is at position (2i-1, 2j-1) for i, j = 1, ..., 50.

In each block, either:
- 2 dominoes are within the block (exact), or
- Some dominoes cross the block boundary.

If a block is not exact, at least one domino crosses its boundary. A domino crossing a block boundary goes from one block to an adjacent block.

Now, a domino that crosses a block boundary: consider a horizontal domino at (2i-1, 2j)-(2i-1, 2j+1). This crosses the vertical boundary between block (i, j) and block (i, j+1). This domino makes both blocks (i, j) and (i, j+1) non-exact (at least this domino crosses their boundary).

Similarly for vertical dominoes crossing horizontal boundaries.

So each domino that crosses a block boundary spoils 2 blocks. But a block might be spoiled by multiple dominoes.

To minimize exact blocks, we want to maximize the number of spoiled blocks. But we need to be careful about double-counting.

Actually, let me think about this differently. Let me consider the "crossing" dominoes.

If we use the brick pattern within each 2×2 block... no, that doesn't make sense.

Let me think about the problem from the answer's perspective. I think the answer is 4900.

Wait, let me reconsider. Let me think about small cases first.

2×2 board: 1 domino... no, 2 dominoes. 1 possible 2×2 square. It must be exact. Answer: 1.

2×4 board: 4 dominoes. 2×2 squares at positions (1,1), (1,2), (1,3). 3 squares.
- Pattern: all horizontal. (1,1-2), (1,3-4), (2,1-2), (2,3-4). Exact squares: (1,1) and (1,3). (1,2) is not exact because the dominoes (1,1-2) and (1,3-4) don't form a 2×2 at (1,2). Actually, (1,2) covers cells (1,2),(1,3),(2,2),(2,3). (1,2) is covered by domino (1,1-2), (1,3) by (1,3-4), (2,2) by (2,1-2), (2,3) by (2,3-4). So 4 dominoes cover this 2×2 square, it's not exact. So 2 exact squares.
- Pattern: brick. (1,1-2), (1,3-4), (2,2-3), and then (2,1) and (2,4) need covering. (2,1) can be vertical: (1,1)-(2,1) but (1,1) is taken. Hmm.
  Let me try: (1,2-3), (2,1-2), (2,3-4), and (1,1) and (1,4) need covering. (1,1) vertical: (1,1)-(2,1) but (2,1) is taken by (2,1-2). 
  Try: (1,1-2), (2,2-3), (1,3-4), (2,4)... (2,4) needs a partner. (2,4)-(1,4)? (1,4) is taken by (1,3-4). (2,4)-(2,3)? (2,3) is taken by (2,2-3). 
  Hmm, 2×4 is tricky for brick pattern.

Let me try: (1,1)-(2,1) vertical, (1,2)-(1,3) horizontal, (2,2)-(2,3) horizontal, (1,4)-(2,4) vertical.
2×2 squares: (1,1): cells (1,1),(1,2),(2,1),(2,2). (1,1) in vertical domino, (2,1) in vertical domino, (1,2) in horizontal (1,2-3), (2,2) in horizontal (2,2-3). 4 dominoes, not exact.
(1,2): cells (1,2),(1,3),(2,2),(2,3). (1,2) in (1,2-3), (1,3) in (1,2-3), (2,2) in (2,2-3), (2,3) in (2,2-3). 2 dominoes, both within! Exact!
(1,3): cells (1,3),(1,4),(2,3),(2,4). (1,3) in (1,2-3), (1,4) in vertical (1,4-2,4), (2,3) in (2,2-3), (2,4) in vertical. 4 dominoes, not exact.
So 1 exact square. Better than 2!

Can we do 0? We need all 3 squares non-exact. 
(1,1) non-exact: at least one domino crosses its boundary.
(1,2) non-exact: at least one domino crosses its boundary.
(1,3) non-exact: at least one domino crosses its boundary.

Try: (1,1)-(1,2) horizontal, (2,1)-(2,2) horizontal, (1,3)-(2,3) vertical, (1,4)-(2,4) vertical.
(1,1): cells (1,1),(1,2),(2,1),(2,2). All in horizontal dominoes within the square. Exact! 2 dominoes. Not good.

Try: (1,1)-(2,1) vertical, (1,2)-(2,2) vertical, (1,3)-(1,4) horizontal, (2,3)-(2,4) horizontal.
(1,1): (1,1) in vert, (1,2) in vert, (2,1) in vert, (2,2) in vert. 2 dominoes within. Exact!
(1,2): (1,2) in vert, (1,3) in horiz, (2,2) in vert, (2,3) in horiz. 4 dominoes. Not exact.
(1,3): (1,3) in horiz, (1,4) in horiz, (2,3) in horiz, (2,4) in horiz. 2 dominoes within. Exact!
So 2 exact.

Try: (1,1)-(1,2) horiz, (2,2)-(2,3) horiz, (1,3)-(2,3)... wait (2,3) is taken.
Try: (1,1)-(2,1) vert, (1,2)-(1,3) horiz, (2,2)-(2,3) horiz, (1,4)-(2,4) vert. This is the same as before, 1 exact.

Can we get 0 for 2×4? We need a perfect matching where no 2×2 sub-square has both dominoes inside.

The 2×2 squares are at columns 1-2, 2-3, 3-4.
- Square 1-2: need a domino crossing its boundary.
- Square 2-3: need a domino crossing its boundary.
- Square 3-4: need a domino crossing its boundary.

A domino crossing square 1-2's boundary: either a horizontal domino from col 2 to col 3 (crossing right boundary), or a vertical domino from row 2 to... well, the board is only 2 rows, so vertical dominoes are within a column and don't cross horizontal boundaries. Actually in a 2-row board, vertical dominoes are (1,j)-(2,j) and they don't cross any horizontal grid line (there's only one horizontal line, between rows 1 and 2, and vertical dominoes cross it, but that's within a column).

Wait, in a 2×4 board, the 2×2 square at (1,1) covers all of rows 1-2, columns 1-2. A domino crosses its boundary if it has one cell inside and one outside. The boundary is the vertical line between columns 2 and 3. So a horizontal domino at (i, 2)-(i, 3) crosses this boundary.

Similarly, square at (1,2) (columns 2-3): boundary at column 1-2 and column 3-4. A horizontal domino at (i,1)-(i,2) or (i,3)-(i,4) crosses it.

Square at (1,3) (columns 3-4): boundary at column 2-3. A horizontal domino at (i,2)-(i,3) crosses it.

So to make all 3 non-exact:
- Square 1-2: need a horizontal domino (1,2)-(1,3) or (2,2)-(2,3).
- Square 3-4: need a horizontal domino (1,2)-(1,3) or (2,2)-(2,3). (Same as above!)
- Square 2-3: need a horizontal domino (1,1)-(1,2) or (2,1)-(2,2) or (1,3)-(1,4) or (2,3)-(2,4).

So we need at least one of {(1,2)-(1,3), (2,2)-(2,3)} and at least one of {(1,1)-(1,2), (2,1)-(2,2), (1,3)-(1,4), (2,3)-(2,4)}.

If we use (1,2)-(1,3) and (2,1)-(2,2):
Remaining cells: (1,1), (1,4), (2,3), (2,4).
(1,1) can pair with (2,1) but (2,1) is taken. (1,1) can pair with (1,2) but taken. So (1,1) must pair with... nothing horizontal works. (1,1)-(2,1) vertical but (2,1) taken. Dead end.

If we use (1,2)-(1,3) and (1,1)-(1,2): conflict, (1,2) in both.

If we use (1,2)-(1,3) and (1,3)-(1,4): conflict, (1,3) in both.

If we use (1,2)-(1,3) and (2,3)-(2,4):
Remaining: (1,1), (1,4), (2,1), (2,2).
(1,1)-(2,1) vertical, (1,4)... (1,4)-(2,4) but (2,4) taken. (2,1)-(2,2) horizontal, (1,1)... (1,1)-(1,2) but (1,2) taken. (1,1)-(2,1) vert, (2,2)... (2,2)-(2,1) but (2,1) taken by vert. (1,4)-(2,4) but (2,4) taken.
Remaining: (1,1), (1,4), (2,1), (2,2). 
Options: (1,1)-(2,1) vert and (1,4)... can't pair. (2,1)-(2,2) horiz and (1,1)... can't pair. (1,1) and (1,4) not adjacent. (2,1) and (2,2) adjacent but then (1,1) and (1,4) left, not adjacent.
Dead end.

If we use (2,2)-(2,3) and (1,1)-(1,2):
Remaining: (1,3), (1,4), (2,1), (2,4).
(1,3)-(1,4) horiz, (2,1)... (2,1)-(2,2) but (2,2) taken. (2,1) and (2,4) not adjacent. Dead end.
(1,3)-(2,3) vert but (2,3) taken. (1,4)-(2,4) vert, (1,3)... (1,3)-(1,2) but (1,2) taken. (1,3)-(1,4) but (1,4) taken by vert. Dead end.

If we use (2,2)-(2,3) and (2,1)-(2,2): conflict.

If we use (2,2)-(2,3) and (1,3)-(1,4):
Remaining: (1,1), (1,2), (2,1), (2,4).
(1,1)-(1,2) horiz, (2,1)... (2,1)-(2,2) but taken. (2,1) and (2,4) not adjacent. Dead end.
(1,1)-(2,1) vert, (1,2)... (1,2)-(1,1) but taken. (1,2)-(2,2) but (2,2) taken. (1,2) and (2,4) not adjacent. Dead end.

So it seems impossible to get 0 exact squares for 2×4. The minimum is 1.

Interesting. So for 2×4, the answer is 1.

Let me check 2×2: answer is 1 (only 1 square, must be exact).
2×4: answer is 1.
2×6: Let me think... 

Actually, let me think about the general 2×2n case.

For a 2×2n board, the 2×2 squares are at positions (1,1), (1,2), ..., (1,2n-1). There are 2n-1 squares.

Using the pattern: vertical dominoes at columns 1 and 2n, horizontal dominoes in between with brick pattern.
- (1,1)-(2,1) vertical, (1,2n)-(2,2n) vertical.
- Row 1: (1,2)-(1,3), (1,4)-(1,5), ..., (1,2n-2)-(1,2n-1). That's n-1 dominoes.
- Row 2: (2,3)-(2,4), (2,5)-(2,6), ..., (2,2n-3)-(2,2n-2). That's n-2 dominoes, covering columns 3 to 2n-2. But columns 2 and 2n-1 in row 2 are uncovered!

Hmm, this doesn't work for the same reason as before.

Let me reconsider. For 2×4 (n=2):
- Vertical at columns 1 and 4: (1,1)-(2,1), (1,4)-(2,4).
- Row 1: (1,2)-(1,3). 1 domino.
- Row 2: need to cover (2,2) and (2,3). (2,2)-(2,3) horizontal. 1 domino.
Total: 2 + 1 + 1 = 4 dominoes. ✓

2×2 squares:
(1,1): (1,1) vert, (1,2) horiz(1,2-3), (2,1) vert, (2,2) horiz(2,2-3). 4 dominoes, not exact.
(1,2): (1,2) horiz, (1,3) horiz, (2,2) horiz, (2,3) horiz. Both horizontal dominoes within. Exact!
(1,3): (1,3) horiz, (1,4) vert, (2,3) horiz, (2,4) vert. 4 dominoes, not exact.
1 exact square. ✓

For 2×6 (n=3):
- Vertical at columns 1 and 6: (1,1)-(2,1), (1,6)-(2,6).
- Row 1: (1,2)-(1,3), (1,4)-(1,5). 2 dominoes.
- Row 2: (2,2)-(2,3), (2,4)-(2,5). 2 dominoes.
Total: 2 + 2 + 2 = 6 dominoes. ✓

But wait, this is just the same pattern in both rows (no offset). Let me check:
2×2 squares:
(1,1): vert, horiz, vert, horiz. Not exact.
(1,2): (1,2)-(1,3) horiz, (2,2)-(2,3) horiz. Both within. Exact!
(1,3): (1,3) in (1,2-3), (1,4) in (1,4-5), (2,3) in (2,2-3), (2,4) in (2,4-5). 4 dominoes. Not exact.
(1,4): (1,4)-(1,5) horiz, (2,4)-(2,5) horiz. Both within. Exact!
(1,5): horiz, vert, horiz, vert. Not exact.
2 exact squares.

Can we do better with offset?
- Vertical at columns 1 and 6.
- Row 1: (1,2)-(1,3), (1,4)-(1,5).
- Row 2: (2,3)-(2,4), and then (2,2) and (2,5) are uncovered. (2,2) can't pair with (2,1) (taken by vert) or (2,3) (taken). Dead end.

What about:
- (1,1)-(2,1) vert, (1,6)-(2,6) vert.
- (1,2)-(1,3), (1,4)-(1,5) in row 1.
- (2,2)-(2,3), (2,4)-(2,5) in row 2.
This gives 2 exact squares as computed above.

Alternative without vertical dominoes:
- (1,1)-(1,2), (1,3)-(1,4), (1,5)-(1,6) in row 1.
- (2,2)-(2,3), (2,4)-(2,5) in row 2, and (2,1), (2,6) uncovered.
- (2,1)-(1,1) vert but (1,1) taken. Dead end.

- (1,2)-(1,3), (1,4)-(1,5) in row 1, (1,1) and (1,6) uncovered.
- (2,1)-(2,2), (2,3)-(2,4), (2,5)-(2,6) in row 2.
- (1,1)-(2,1) vert but (2,1) taken. (1,1)-(1,2) but (1,2) taken. Dead end.

- (1,1)-(1,2), (1,3)-(1,4), (1,5)-(1,6) row 1.
- (2,1)-(2,2), (2,3)-(2,4), (2,5)-(2,6) row 2.
All same alignment. Exact squares: (1,1), (1,3), (1,5). 3 exact. Worse.

- (1,1)-(1,2), (1,3)-(1,4), (1,5)-(1,6) row 1.
- (2,2)-(2,3), (2,4)-(2,5) row 2, (2,1) and (2,6) need vertical: (1,1)-(2,1) but (1,1) taken. Dead end.

Hmm, it seems hard to do better than 2 for 2×6. Let me try:
- (1,1)-(2,1) vert, (1,2)-(1,3) horiz, (2,2)-(2,3) horiz, (1,4)-(1,5) horiz, (2,4)-(2,5) horiz, (1,6)-(2,6) vert.
This is the same as before, 2 exact.

What about:
- (1,1)-(2,1) vert, (1,2)-(2,2) vert, (1,3)-(1,4) horiz, (2,3)-(2,4) horiz, (1,5)-(2,5) vert, (1,6)-(2,6) vert.
2×2 squares:
(1,1): (1,1) vert, (1,2) vert, (2,1) vert, (2,2) vert. 2 dominoes within. Exact!
(1,2): (1,2) vert, (1,3) horiz, (2,2) vert, (2,3) horiz. 4 dominoes. Not exact.
(1,3): (1,3) horiz, (1,4) horiz, (2,3) horiz, (2,4) horiz. 2 within. Exact!
(1,4): (1,4) horiz, (1,5) vert, (2,4) horiz, (2,5) vert. 4 dominoes. Not exact.
(1,5): (1,5) vert, (1,6) vert, (2,5) vert, (2,6) vert. 2 within. Exact!
3 exact. Worse.

Let me try to find a pattern with fewer exact squares for 2×6.

- (1,1)-(2,1) vert, (1,2)-(1,3) horiz, (2,4)-(2,5) horiz, (1,4)-(2,4)... (2,4) taken. 

Let me try:
- (1,1)-(2,1) vert, (1,6)-(2,6) vert.
- (1,2)-(1,3), (1,4)-(1,5) row 1.
- (2,3)-(2,4), (2,5)... (2,5)-(2,6) but (2,6) taken. (2,2)-(2,3) but (2,3) taken. (2,2) and (2,5) uncovered.
Dead end.

- (1,1)-(2,1) vert, (1,6)-(2,6) vert.
- (1,2)-(1,3), (1,4)-(1,5) row 1.
- (2,2)-(2,3), (2,4)-(2,5) row 2.
This works (same as before), 2 exact.

Can we get 1 exact for 2×6? Let me try to be more creative.

- (1,1)-(1,2), (2,1)-(2,2), (1,3)-(2,3), (1,4)-(2,4), (1,5)-(1,6), (2,5)-(2,6).
2×2 squares:
(1,1): (1,1)-(1,2) horiz, (2,1)-(2,2) horiz. 2 within. Exact!
(1,2): (1,2) in (1,1-2), (1,3) in vert, (2,2) in (2,1-2), (2,3) in vert. 4 dominoes. Not exact.
(1,3): (1,3) vert, (1,4) vert, (2,3) vert, (2,4) vert. 2 within. Exact!
(1,4): (1,4) vert, (1,5) horiz, (2,4) vert, (2,5) horiz. 4. Not exact.
(1,5): (1,5)-(1,6) horiz, (2,5)-(2,6) horiz. 2 within. Exact!
3 exact. Worse.

Let me try a "zigzag" pattern:
- (1,1)-(2,1) vert, (1,2)-(2,2) vert, (1,3)-(1,4) horiz, (2,3)-(2,4) horiz, (1,5)-(1,6) horiz, (2,5)-(2,6) horiz.
(1,1): 2 vert within. Exact.
(1,2): vert, horiz, vert, horiz. Not exact.
(1,3): 2 horiz within. Exact.
(1,4): horiz, horiz, horiz, horiz. 2 within. Exact.
(1,5): 2 horiz within. Exact.
4 exact. Worse.

Hmm. Let me try:
- (1,1)-(1,2) horiz, (2,2)-(2,3) horiz, (1,3)-(1,4) horiz, (2,4)-(2,5) horiz, (1,5)-(1,6) horiz, (2,1)... and (2,6) uncovered.
(2,1) and (2,6): (2,1)-(1,1) vert but (1,1) taken. Dead end.

- (1,2)-(1,3) horiz, (2,1)-(2,2) horiz, (1,4)-(1,5) horiz, (2,3)-(2,4) horiz, (1,6)... and (2,5)-(2,6) horiz, (1,1) uncovered.
(1,1): (1,1)-(1,2) but (1,2) taken. (1,1)-(2,1) but (2,1) taken. Dead end.

It seems like for 2×6, the minimum is 2. Let me see the pattern:
- 2×2: 1 exact
- 2×4: 1 exact
- 2×6: 2 exact

Hmm, let me recheck 2×4. The pattern I found gives 1 exact. Can we get 0?

I showed above that 0 is impossible for 2×4. So 2×4: 1 exact.

For 2×6: is 1 possible? Let me try harder.

- (1,1)-(2,1) vert, (1,2)-(1,3) horiz, (2,2)-(2,3) horiz, (1,4)-(2,4) vert, (1,5)-(1,6) horiz, (2,5)-(2,6) horiz.
(1,1): vert, horiz, vert, horiz. Not exact.
(1,2): (1,2)-(1,3) horiz, (2,2)-(2,3) horiz. 2 within. Exact!
(1,3): (1,3) in (1,2-3), (1,4) vert, (2,3) in (2,2-3), (2,4) vert. 4. Not exact.
(1,4): (1,4) vert, (1,5) horiz, (2,4) vert, (2,5) horiz. 4. Not exact.
(1,5): (1,5)-(1,6) horiz, (2,5)-(2,6) horiz. 2 within. Exact!
2 exact.

- (1,1)-(2,1) vert, (1,2)-(1,3) horiz, (2,3)-(2,4) horiz, (1,4)-(1,5) horiz, (2,5)-(2,6) horiz, (2,2)... uncovered.
(2,2): (2,2)-(2,1) but (2,1) taken. (2,2)-(2,3) but (2,3) taken. (1,2)-(2,2) but (1,2) taken. Dead end.

- (1,1)-(1,2) horiz, (2,1)-(2,2) horiz, (1,3)-(2,3) vert, (1,4)-(1,5) horiz, (2,4)-(2,5) horiz, (1,6)-(2,6) vert.
(1,1): 2 horiz within. Exact!
(1,2): horiz, vert, horiz, vert. Not exact.
(1,3): vert, horiz, vert, horiz. Not exact.
(1,4): (1,4)-(1,5) horiz, (2,4)-(2,5) horiz. 2 within. Exact!
(1,5): horiz, vert, horiz, vert. Not exact.
2 exact.

- (1,1)-(2,1) vert, (1,2)-(2,2) vert, (1,3)-(2,3) vert, (1,4)-(1,5) horiz, (2,4)-(2,5) horiz, (1,6)-(2,6) vert.
(1,1): 2 vert within. Exact.
(1,2): vert, vert, vert, vert. 2 within. Exact!
(1,3): vert, horiz, vert, horiz. Not exact.
(1,4): 2 horiz within. Exact!
(1,5): horiz, vert, horiz, vert. Not exact.
3 exact. Worse.

I'm starting to think 2×6 minimum is 2. Let me see if there's a pattern.

2×2: 1
2×4: 1
2×6: 2
2×8: ?

For 2×2n, it seems like the minimum might be n-1 or floor(n/2) or something.

Wait, let me reconsider 2×4. I had the pattern:
(1,1)-(2,1) vert, (1,2)-(1,3) horiz, (2,2)-(2,3) horiz, (1,4)-(2,4) vert.
1 exact (at position (1,2)).

For 2×6, can I extend this?
(1,1)-(2,1) vert, (1,2)-(1,3) horiz, (2,2)-(2,3) horiz, (1,4)-(2,4) vert, (1,5)-(1,6) horiz, (2,5)-(2,6) horiz.
(1,1): not exact.
(1,2): exact (2 horiz within).
(1,3): not exact.
(1,4): not exact (vert, horiz, vert, horiz).
(1,5): exact (2 horiz within).
2 exact.

Alternatively:
(1,1)-(2,1) vert, (1,2)-(1,3) horiz, (2,2)-(2,3) horiz, (1,4)-(1,5) horiz, (2,4)-(2,5) horiz, (1,6)-(2,6) vert.
(1,1): not exact.
(1,2): exact.
(1,3): not exact.
(1,4): exact.
(1,5): not exact.
2 exact.

Can I do:
(1,1)-(2,1) vert, (1,2)-(1,3) horiz, (2,2)-(2,3) horiz, (1,4)-(2,4) vert, (1,5)-(2,5) vert, (1,6)-(2,6) vert.
(1,1): not exact.
(1,2): exact.
(1,3): not exact.
(1,4): not exact.
(1,5): 2 vert within. Exact!
2 exact.

Hmm, what if I try:
(1,1)-(2,1) vert, (1,2)-(2,2) vert, (1,3)-(1,4) horiz, (2,3)-(2,4) horiz, (1,5)-(2,5) vert, (1,6)-(2,6) vert.
(1,1): 2 vert. Exact!
(1,2): vert, horiz, vert, horiz. Not exact.
(1,3): 2 horiz. Exact!
(1,4): horiz, vert, horiz, vert. Not exact.
(1,5): 2 vert. Exact!
3 exact. Worse.

It really seems like 2 is the minimum for 2×6. The pattern for 2×2n seems to be:
- With the "vert-horiz-vert" pattern, we get exact squares at the horiz-horiz positions.
- For 2×4: 1 exact.
- For 2×6: 2 exact.
- For 2×2n: n-1 exact? No, 2×4 has n=2, 1 exact = n-1. 2×6 has n=3, 2 exact = n-1. 2×2 has n=1, 1 exact ≠ n-1 = 0.

Hmm, 2×2 is special because the only square must be exact.

So for 2×2n with n ≥ 2, the minimum might be n-1.

For 2×100 (n=50), that would be 49. But our board is 100×100, not 2×100.

Let me think about the 100×100 problem differently.

Actually, let me think about this problem more carefully. I think the key insight involves a coloring argument.

Let me try a different coloring. Color the cells with 4 colors based on (row mod 2, col mod 2):
- Type A: (odd, odd) — 50×50 = 2500 cells
- Type B: (odd, even) — 50×50 = 2500 cells
- Type C: (even, odd) — 50×50 = 2500 cells
- Type D: (even, even) — 50×50 = 2500 cells

A horizontal domino covers either (A, B) or (C, D) [if in odd row: A-B, if in even row: C-D] or (B, A) or (D, C).
A vertical domino covers either (A, C) or (B, D) [if in odd column: A-C, if in even column: B-D] or (C, A) or (D, B).

A 2×2 square aligned to the grid (at position (2i-1, 2j-1)) contains one cell of each type: A, B, C, D. It's exact iff covered by 2 dominoes within it, which means either:
- 2 horizontal: (A,B) and (C,D), or
- 2 vertical: (A,C) and (B,D).

A 2×2 square at position (2i-1, 2j) (shifted right by 1) contains: B, A, D, C (i.e., (odd, even), (odd, odd+1=even)... wait, let me recompute.

Position (2i-1, 2j): cells (2i-1, 2j), (2i-1, 2j+1), (2i, 2j), (2i, 2j+1).
(2i-1, 2j): odd row, even col → B
(2i-1, 2j+1): odd row, odd col → A
(2i, 2j): even row, even col → D
(2i, 2j+1): even row, odd col → C
So it's B, A, D, C — same set {A, B, C, D}.

Actually, every 2×2 square contains one of each type, regardless of position. Because in any 2×2 square, there's one (odd,odd), one (odd,even), one (even,odd), one (even,even).

Now, let me count. Let h₁ = number of horizontal dominoes in odd rows (covering A-B pairs), h₂ = number in even rows (covering C-D pairs), v₁ = number of vertical dominoes in odd columns (covering A-C pairs), v₂ = number in even columns (covering B-D pairs).

Total dominoes: h₁ + h₂ + v₁ + v₂ = 5000.

Each A cell is covered by exactly one domino, which is either h₁ (horizontal, A-B) or v₁ (vertical, A-C). So h₁ + v₁ = 2500 (number of A cells).
Similarly: h₁ + v₂ = 2500 (B cells), h₂ + v₁ = 2500 (C cells), h₂ + v₂ = 2500 (D cells).

From these: h₁ + v₁ = 2500, h₁ + v₂ = 2500 → v₁ = v₂. And h₂ + v₁ = 2500, h₂ + v₂ = 2500 → consistent. Also h₁ + h₂ + v₁ + v₂ = 5000 → h₁ + h₂ + 2v₁ = 5000, and h₁ + v₁ = 2500 → h₂ + v₁ = 2500 → h₁ = h₂ and v₁ = v₂. So h₁ = h₂ = h, v₁ = v₂ = v, with h + v = 2500 and 2h + 2v = 5000. Consistent.

Now, let's think about exact 2×2 squares. A 2×2 square at position (r, c) is exact iff it's covered by 2 dominoes within it.

For a 2×2 square at (2i-1, 2j-1) (aligned): exact iff either (h₁ domino at (2i-1, 2j-1)-(2i-1, 2j) AND h₂ domino at (2i, 2j-1)-(2i, 2j)) OR (v₁ domino at (2i-1, 2j-1)-(2i, 2j-1) AND v₂ domino at (2i-1, 2j)-(2i, 2j)).

For a 2×2 square at (2i-1, 2j) (shifted right): exact iff either (h₁ domino at (2i-1, 2j)-(2i-1, 2j+1) AND h₂ domino at (2i, 2j)-(2i, 2j+1)) OR (v₂ domino at (2i-1, 2j)-(2i, 2j) AND v₁ domino at (2i-1, 2j+1)-(2i, 2j+1)).

For a 2×2 square at (2i, 2j-1) (shifted down): exact iff either (h₂ domino at (2i, 2j-1)-(2i, 2j) AND h₁ domino at (2i+1, 2j-1)-(2i+1, 2j)) OR (v₁ domino at (2i, 2j-1)-(2i+1, 2j-1) AND v₂ domino at (2i, 2j)-(2i+1, 2j)).

For a 2×2 square at (2i, 2j) (shifted both): exact iff either (h₂ domino at (2i, 2j)-(2i, 2j+1) AND h₁ domino at (2i+1, 2j)-(2i+1, 2j+1)) OR (v₂ domino at (2i, 2j)-(2i+1, 2j) AND v₁ domino at (2i, 2j+1)-(2i+1, 2j+1)).

This is getting complex. Let me think about it differently.

Let me define:
- For each pair of adjacent rows (2i-1, 2i), let a_i = number of positions j where both row 2i-1 and row 2i have a horizontal domino at columns (2j-1, 2j). These contribute to exact squares at aligned positions.
- Similarly for other types.

Actually, this is getting very complicated. Let me think about the problem from a higher level.

I think the answer is 4900. Let me try to verify this.

Consider the "all horizontal, alternating offset" pattern, but handle boundaries properly.

Actually, let me think about a cleaner pattern. Consider the board as a 50×50 grid of 2×2 blocks. In each block, place 2 vertical dominoes. Then every aligned 2×2 square is exact. That gives 50×50 = 2500 exact squares. But there are also shifted 2×2 squares to consider.

With all vertical dominoes: every cell (i, j) is paired with (i+1, j) or (i-1, j). If we use the pattern (1,j)-(2,j), (3,j)-(4,j), ..., then:
- Aligned 2×2 squares at (2i-1, 2j-1): covered by 2 vertical dominoes. Exact. 2500 of these.
- Shifted 2×2 squares at (2i, 2j-1): cells (2i, 2j-1), (2i, 2j), (2i+1, 2j-1), (2i+1, 2j). (2i, 2j-1) is in vertical domino (2i, 2j-1)-(2i+1, 2j-1) [if 2i is the start of a pair, i.e., i is such that 2i ≡ 1 mod 2... wait, the pairs are (1,j)-(2,j), (3,j)-(4,j), etc. So (2i, j) is paired with (2i-1, j) if i is... let me re-index. Pairs: (1,j)-(2,j), (3,j)-(4,j), ..., (2k-1, j)-(2k, j). So (2i, j) is paired with (2i-1, j) when i = k, i.e., always (for even rows). And (2i+1, j) is paired with (2i+2, j).

So for the shifted square at (2i, 2j-1): (2i, 2j-1) paired with (2i-1, 2j-1) [outside the square, since the square starts at row 2i]. So this domino crosses the boundary. Not exact.
Similarly, (2i, 2j) paired with (2i-1, 2j) [outside]. (2i+1, 2j-1) paired with (2i+2, 2j-1) [outside]. (2i+1, 2j) paired with (2i+2, 2j) [outside]. All 4 dominoes cross the boundary. Not exact.

So with all vertical dominoes (aligned), we get 2500 exact squares (the aligned ones) and 0 exact shifted squares. Total: 2500.

Similarly, with all horizontal dominoes (aligned), we get 2500 exact squares.

Now, can we do better? The brick pattern might help.

Let me think about the brick pattern for the 100×100 board.

Consider the pattern where:
- Rows 1, 3, 5, ..., 99: horizontal dominoes at (1-2), (3-4), ..., (99-100).
- Rows 2, 4, 6, ..., 100: horizontal dominoes at (2-3), (4-5), ..., (98-99), and vertical dominoes at columns 1 and 100.

For even rows, columns 1 and 100: use vertical dominoes (2i, 1)-(2i+1, 1) and (2i, 100)-(2i+1, 100). But (2i+1, 1) is in an odd row, already covered by horizontal domino (2i+1, 1)-(2i+1, 2). Conflict!

Alternative: (2i-1, 1)-(2i, 1) vertical, but (2i-1, 1) is in an odd row, covered by (2i-1, 1)-(2i-1, 2). Conflict!

So the brick pattern with horizontal dominoes doesn't work on a 100×100 board because of boundary issues (100 is even, so the offset leaves boundary cells uncovered).

What if we use a different approach? Let me think about using vertical dominoes on the boundary columns.

Columns 1 and 100: vertical dominoes (1,1)-(2,1), (3,1)-(4,1), ..., (99,1)-(100,1). Same for column 100. 100 dominoes.

Interior columns 2-99 (98 columns, which is even):
- Odd rows: horizontal at (2,3), (4,5), ..., (98,99). 49 dominoes per odd row. 50 odd rows → 2450 dominoes.
- Even rows: horizontal at (3,4), (5,6), ..., (97,98). 48 dominoes per even row. Covers columns 3-98. Columns 2 and 99 uncovered in even rows. 50 even rows → 2400 dominoes, but 100 cells uncovered (2 per even row).

Total so far: 100 + 2450 + 2400 = 4950 dominoes, covering 10000 - 100 = 9900 cells. 100 cells uncovered (columns 2 and 99 in even rows). We need 50 more dominoes to cover these 100 cells.

The uncovered cells are (2i, 2) and (2i, 99) for i = 1, ..., 50. These are in even rows, columns 2 and 99. They're not adjacent to each other (column 2 and 99 are far apart). Each needs to be paired with an adjacent cell.

(2i, 2) is adjacent to (2i, 1) [covered by vertical domino], (2i, 3) [covered by horizontal domino (2i, 3)-(2i, 4)], (2i-1, 2) [covered by horizontal domino (2i-1, 2)-(2i-1, 3)], (2i+1, 2) [covered by horizontal domino (2i+1, 2)-(2i+1, 3)].

All neighbors are covered! So we can't pair (2i, 2) with anything. This pattern doesn't work.

The issue is that the brick pattern on an even-width interior doesn't work because the offset leaves isolated cells.

Let me try a different approach entirely. What if we use a mix of horizontal and vertical dominoes in a more clever pattern?

Actually, let me think about the problem from the perspective of the answer. I've seen similar problems before, and I believe the answer is 4900.

Let me try to construct a pattern with 4900 exact squares and then prove it's optimal.

Wait, actually, let me reconsider. With all horizontal dominoes (same alignment), we get 99 × 50 = 4950 exact squares (every 2×2 square starting at an odd column). Can we do better?

With all vertical dominoes (same alignment), we get 50 × 99 = 4950 exact squares (every 2×2 square starting at an odd row).

Can we reduce this? Let me think about the brick pattern more carefully.

What if we use a 4×4 repeating pattern? Or some other pattern?

Let me think about a 4×4 block:
```
H H V V
H H V V
V V H H
V V H H
```
Where H = horizontal domino, V = vertical domino.

In this 4×4 block:
Row 1: (1,1)-(1,2) H, (1,3)-(2,3) V, (1,4)-(2,4) V.
Row 2: (2,1)-(2,2) H, (2,3) in V, (2,4) in V.
Row 3: (3,1)-(4,1) V, (3,2)-(4,2) V, (3,3)-(3,4) H.
Row 4: (4,1) in V, (4,2) in V, (4,3)-(4,4) H.

2×2 squares within this block (positions (1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)):
(1,1): (1,1)-(1,2) H, (2,1)-(2,2) H. 2 within. Exact!
(1,2): (1,2) in H(1,1-2), (1,3) in V(1,3-2,3), (2,2) in H(2,1-2), (2,3) in V. 4 dominoes. Not exact.
(1,3): (1,3) in V, (1,4) in V, (2,3) in V, (2,4) in V. 2 within. Exact!
(2,1): (2,1)-(2,2) H, (3,1) in V(3,1-4,1), (3,2) in V(3,2-4,2). Wait, (2,1) and (2,2) are in H, (3,1) and (3,2) are in V dominoes that go to row 4. So the 2×2 square at (2,1) has cells (2,1),(2,2),(3,1),(3,2). (2,1)-(2,2) is within. (3,1) is in V(3,1-4,1) which crosses the bottom boundary. (3,2) is in V(3,2-4,2) which crosses. So 3 dominoes. Not exact.
(2,2): (2,2) in H, (2,3) in V, (3,2) in V, (3,3) in H(3,3-3,4). 4 dominoes. Not exact.
(2,3): (2,3) in V(1,3-2,3), (2,4) in V(1,4-2,4), (3,3)-(3,4) H, (3,4) in H. Wait, cells are (2,3),(2,4),(3,3),(3,4). (2,3) in V crossing top, (2,4) in V crossing top, (3,3)-(3,4) H within. 3 dominoes. Not exact.
(3,1): (3,1) in V(3,1-4,1), (3,2) in V(3,2-4,2), (4,1) in V, (4,2) in V. 2 within. Exact!
(3,2): (3,2) in V, (3,3) in H, (4,2) in V, (4,3) in H. 4. Not exact.
(3,3): (3,3)-(3,4) H, (4,3)-(4,4) H. 2 within. Exact!

So in this 4×4 block, we have 4 exact squares out of 9. With all horizontal, we'd have 6 exact out of 9 (at (1,1),(1,3),(2,1),(2,3),(3,1),(3,3) — wait, no. With all horizontal at (1-2),(3-4) in each row, exact squares are at odd columns: (1,1),(1,3),(2,1),(2,3),(3,1),(3,3). That's 6 out of 9.

So the 4×4 pattern gives 4/9 exact, compared to 6/9 for all-horizontal. That's better!

If we tile the 100×100 board with this 4×4 pattern, we'd have 25×25 = 625 blocks, each with 4 exact squares, giving 2500 exact squares. But we also need to check the 2×2 squares that straddle block boundaries.

Hmm, this is getting complicated. Let me think about whether 2500 is achievable or if we can do even better.

Actually, wait. Let me reconsider the problem. The 4×4 pattern I described has 4 exact squares per 4×4 block. If we tile the board perfectly, the 2×2 squares at block boundaries might also be exact or not.

Let me think about this more carefully. The 4×4 pattern is:
```
Row 1: H H V V
Row 2: H H V V
Row 3: V V H H
Row 4: V V H H
```

If we tile this, the next block to the right starts at column 5:
```
Row 1: H H V V | H H V V
Row 2: H H V V | H H V V
Row 3: V V H H | V V H H
Row 4: V V H H | V V H H
```

The 2×2 square at (1,4) (columns 4-5): (1,4) in V(1,4-2,4), (1,5) in H(1,5-1,6), (2,4) in V, (2,5) in H. 4 dominoes. Not exact.

The 2×2 square at (3,4): (3,4) in H(3,3-3,4), (3,5) in V(3,5-4,5), (4,4) in H(4,3-4,4), (4,5) in V. 4. Not exact.

Similarly, vertically tiling:
```
Row 1: H H V V
Row 2: H H V V
Row 3: V V H H
Row 4: V V H H
Row 5: H H V V
Row 6: H H V V
```

2×2 square at (4,1): (4,1) in V(3,1-4,1), (4,2) in V(3,2-4,2), (5,1) in H(5,1-5,2), (5,2) in H. 4. Not exact.

2×2 square at (4,3): (4,3) in H(3,3-4,3)... wait, no. (4,3) is in H(4,3-4,4). (5,3) is in V(5,3-6,3). So (4,3)-(4,4) H, (5,3) in V, (5,4) in V. 3 dominoes. Not exact.

So the block boundaries don't create additional exact squares. 

Now, within each 4×4 block, the 2×2 squares at positions (1,1), (1,3), (3,1), (3,3) are exact (4 per block). The 2×2 squares at (1,2), (2,1), (2,2), (2,3), (3,2) are not exact (5 per block). And the boundary squares are not exact.

In a 100×100 board with 25×25 blocks:
- Internal exact squares: 25 × 25 × 4 = 2500.
- Boundary 2×2 squares (between blocks): need to check.

The 2×2 squares at block boundaries (both horizontal and vertical): these are at positions where r ≡ 0 mod 4 or c ≡ 0 mod 4 (or both). From the analysis above, these are not exact.

But wait, I need to be more careful. The 2×2 squares within a block are at positions (4i+1, 4j+1), (4i+1, 4j+2), (4i+1, 4j+3), (4i+2, 4j+1), (4i+2, 4j+2), (4i+2, 4j+3), (4i+3, 4j+1), (4i+3, 4j+2), (4i+3, 4j+3) for block (i,j). That's 9 per block, but some of these are at block boundaries.

Actually, the 2×2 squares within block (i,j) (starting at row 4i+1, col 4j+1) are at positions (4i+1, 4j+1) through (4i+3, 4j+3), which is 9 squares. The ones at the edge of the block (e.g., (4i+3, 4j+3)) might overlap with the next block.

Wait, the 2×2 square at (4i+3, 4j+3) covers rows 4i+3, 4i+4 and columns 4j+3, 4j+4. Row 4i+4 is in the next block (block (i+1, j)). Column 4j+4 is in the next block (block (i, j+1)). So this square straddles blocks.

Let me re-examine. The 2×2 square at (3,3) in the first block covers rows 3,4 and columns 3,4. In my 4×4 pattern, (3,3)-(3,4) is H and (4,3)-(4,4) is H, so it's exact. But this square is at the corner of the block, and row 4 is the last row of the block, column 4 is the last column. So it doesn't straddle.

Actually, the 2×2 square at (3,3) covers (3,3), (3,4), (4,3), (4,4), all within the first 4×4 block. So it's fine.

The 2×2 square at (4,1) covers (4,1), (4,2), (5,1), (5,2). Row 5 is in the next block. This straddles.

So the 2×2 squares that straddle blocks are those at row positions 4, 8, 12, ..., 96 (i.e., r ≡ 0 mod 4) and column positions 4, 8, 12, ..., 96 (c ≡ 0 mod 4).

Number of straddling squares: 
- Horizontal straddle (r ≡ 0 mod 4, any c): 24 values of r (4, 8, ..., 96) × 99 values of c = 2376.
- Vertical straddle (any r, c ≡ 0 mod 4): 99 values of r × 24 values of c = 2376.
- Both straddle (r ≡ 0 mod 4, c ≡ 0 mod 4): 24 × 24 = 576.
- Total straddling: 2376 + 2376 - 576 = 4176.

Non-straddling: 9801 - 4176 = 5625. These are the 9 per block × 625 blocks = 5625. ✓

From the analysis, the straddling squares are not exact. The non-straddling squares: 4 exact per block × 625 = 2500 exact, 5 non-exact per block × 625 = 3125 non-exact.

Total exact: 2500. That's better than 4950!

Can we do even better? Let me think about whether we can reduce the exact squares within each block.

In the 4×4 block, we have 4 exact squares. Can we design a pattern with fewer?

Let me try a 4×4 block with a different pattern:
```
Row 1: H V V H
Row 2: H V V H
Row 3: H V V H
Row 4: H V V H
```
Wait, this doesn't make sense. Let me be more explicit.

Actually, let me try:
```
(1,1)-(1,2) H, (1,3)-(2,3) V, (1,4)-(2,4) V
(2,1)-(2,2) H, (2,3) in V, (2,4) in V
(3,1)-(3,2) H, (3,3)-(4,3) V, (3,4)-(4,4) V
(4,1)-(4,2) H, (4,3) in V, (4,4) in V
```
This is just all H in columns 1-2 and all V in columns 3-4.

2×2 squares:
(1,1): H, H. Exact.
(1,2): H(1,1-2), V(1,3-2,3), H(2,1-2), V(2,3-... wait, (2,3) is in V(1,3-2,3). So (1,2) in H, (1,3) in V, (2,2) in H, (2,3) in V. 4. Not exact.
(1,3): V(1,3-2,3), V(1,4-2,4). 2 within. Exact!
(2,1): H(2,1-2), H(3,1-3,2). Wait, (3,1)-(3,2) is H. So (2,1)-(2,2) H within, (3,1)-(3,2) H within. 2 within. Exact!
(2,2): H(2,1-2), V(2,3-... (2,3) in V(1,3-2,3)), H(3,1-3,2), V(3,3-4,3). 4. Not exact.
(2,3): V(1,3-2,3), V(1,4-2,4), V(3,3-4,3), V(3,4-4,4). (2,3) in V crossing up, (2,4) in V crossing up, (3,3) in V crossing down, (3,4) in V crossing down. 4. Not exact.
(3,1): H(3,1-3,2), H(4,1-4,2). 2 within. Exact!
(3,2): H, V, H, V. Not exact.
(3,3): V(3,3-4,3), V(3,4-4,4). 2 within. Exact!

5 exact. Worse than 4.

Let me try another 4×4 pattern:
```
(1,1)-(2,1) V, (1,2)-(1,3) H, (1,4)-(2,4) V
(2,1) in V, (2,2)-(2,3) H, (2,4) in V
(3,1)-(4,1) V, (3,2)-(3,3) H, (3,4)-(4,4) V
(4,1) in V, (4,2)-(4,3) H, (4,4) in V
```

2×2 squares:
(1,1): V(1,1-2,1), H(1,2-1,3), V(1,4-2,4)... wait, (1,1) in V, (1,2) in H, (2,1) in V, (2,2) in H(2,2-2,3). 4. Not exact.
(1,2): H(1,2-1,3), H(2,2-2,3). 2 within. Exact!
(1,3): H(1,2-1,3), V(1,4-2,4), H(2,2-2,3), V. (1,3) in H, (1,4) in V, (2,3) in H, (2,4) in V. 4. Not exact.
(2,1): V(1,1-2,1), H(2,2-2,3), V(3,1-4,1), H(3,2-3,3). (2,1) in V crossing up, (2,2) in H, (3,1) in V crossing down, (3,2) in H. 4. Not exact.
(2,2): H(2,2-2,3), H(3,2-3,3). 2 within. Exact!
(2,3): H(2,2-2,3), V(2,4-... (2,4) in V(1,4-2,4)), H(3,2-3,3), V(3,4-4,4). 4. Not exact.
(3,1): V(3,1-4,1), H(3,2-3,3), V... (4,1) in V, (4,2) in H(4,2-4,3). (3,1) in V, (3,2) in H, (4,1) in V, (4,2) in H. 4. Not exact.
(3,2): H(3,2-3,3), H(4,2-4,3). 2 within. Exact!
(3,3): H(3,2-3,3), V(3,4-4,4), H(4,2-4,3), V. 4. Not exact.

3 exact! Better than 4!

So this pattern gives 3 exact per 4×4 block. If we can tile the 100×100 board with this, we'd get 25×25×3 = 1875 exact squares (plus boundary effects to check).

Let me check the boundary effects. The pattern is:
```
V H H V
V H H V
V H H V
V H H V
```
Where V = vertical domino, H = horizontal domino. Columns 1 and 4 have vertical dominoes, columns 2-3 have horizontal dominoes.

If we tile this horizontally:
```
V H H V | V H H V
V H H V | V H H V
```

At the boundary (columns 4-5): (1,4) in V(1,4-2,4), (1,5) in V(1,5-2,5), (2,4) in V, (2,5) in V. 4 dominoes, all crossing. Not exact. ✓

If we tile vertically:
```
V H H V
V H H V
V H H V
V H H V
V H H V
V H H V
```

At the boundary (rows 4-5): (4,1) in V(3,1-4,1), (4,2) in H(4,2-4,3), (5,1) in V(5,1-6,1), (5,2) in H(5,2-5,3). 4. Not exact. ✓

What about the 2×2 square at (4,2): (4,2) in H(4,2-4,3), (4,3) in H, (5,2) in H(5,2-5,3), (5,3) in H. 2 within. Exact! 

Oh no, this is a boundary square that's exact! So the vertical tiling creates extra exact squares.

Let me re-examine. The 2×2 square at (4,2) covers (4,2), (4,3), (5,2), (5,3). In the pattern, row 4 has H at (4,2)-(4,3), and row 5 has H at (5,2)-(5,3). So both dominoes are within the 2×2 square. Exact!

So when we tile vertically, the boundary between blocks at row 4-5 creates exact squares at columns 2-3 (and 6-7, 10-11, etc.). That's 1 extra exact square per vertical boundary per horizontal block.

With 25×25 blocks, there are 24 vertical boundaries (between rows 4-5, 8-9, ..., 96-97) and 25 horizontal block positions. Each vertical boundary × each horizontal block gives 1 extra exact square. So 24 × 25 = 600 extra. Plus the 3 per block × 625 = 1875. Total: 2475.

Hmm, but I also need to check horizontal boundaries. At the horizontal boundary (columns 4-5), the 2×2 square at (r, 4) for various r:
(r, 4): (r,4) in V, (r,5) in V, (r+1,4) in V, (r+1,5) in V. All vertical dominoes crossing. Not exact. ✓

And the 2×2 square at (4,4) (both boundaries): (4,4) in V(3,4-4,4), (4,5) in V(4,5-5,5)... wait, (4,5) is in V(5,5-6,5)? No, let me re-examine the tiling.

Actually, I need to be more careful about the tiling. Let me re-examine.

The 4×4 block pattern:
- Columns 1, 4: vertical dominoes. (1,1)-(2,1), (3,1)-(4,1), (1,4)-(2,4), (3,4)-(4,4).
- Columns 2-3: horizontal dominoes. (1,2)-(1,3), (2,2)-(2,3), (3,2)-(3,3), (4,2)-(4,3).

When tiling horizontally, the next block starts at column 5:
- Columns 5, 8: vertical dominoes.
- Columns 6-7: horizontal dominoes.

The 2×2 square at (1,4): (1,4) in V(1,4-2,4), (1,5) in V(1,5-2,5), (2,4) in V, (2,5) in V. Not exact. ✓

When tiling vertically, the next block starts at row 5:
- Columns 1, 4: vertical dominoes. (5,1)-(6,1), (7,1)-(8,1), (5,4)-(6,4), (7,4)-(8,4).
- Columns 2-3: horizontal. (5,2)-(5,3), (6,2)-(6,3), (7,2)-(7,3), (8,2)-(8,3).

The 2×2 square at (4,2): (4,2) in H(4,2-4,3), (4,3) in H, (5,2) in H(5,2-5,3), (5,3) in H. Exact! ✗

So vertical tiling creates exact squares at the H-H boundary. This is because the H pattern is the same in rows 4 and 5 (both have H at columns 2-3).

To avoid this, I need the H pattern to be offset between adjacent blocks. But in this pattern, the H is always at columns 2-3, so it can't be offset within the block structure.

What if I alternate the block pattern? Use the pattern and its "mirror" alternately?

Block A:
```
V H H V
V H H V
V H H V
V H H V
```

Block B (mirror):
```
H H V V
H H V V
V V H H
V V H H
```

Hmm, this is getting complicated. Let me think about this differently.

Actually, let me reconsider. The key issue is that when we tile the pattern vertically, the H dominoes at the boundary create exact squares. To avoid this, we need the rows at the boundary to have different H alignments.

What if we use a pattern where the H alignment alternates every 2 rows?

Pattern:
```
Row 1: V H H V  (H at 2-3)
Row 2: V H H V  (H at 2-3)
Row 3: V H H V  (H at 2-3)
Row 4: V H H V  (H at 2-3)
Row 5: V H H V  (H at 2-3)
...
```

All rows have H at 2-3, so every pair of adjacent rows creates an exact square at (r, 2). That's 99 exact squares per column pair (2-3), times 25 column pairs = 2475. Plus the V-V exact squares... wait, the V columns don't create exact squares between blocks because the V dominoes cross the block boundary.

Hmm, actually in this pattern (all rows the same), the exact squares are:
- At (r, 2) for r = 1, ..., 99: H-H exact. 99 per block-column, 25 block-columns → 2475.
- At (r, 1) for r = 1, 3, 5, ..., 99 (odd r): V-V exact (both (r,1)-(r+1,1) and (r,2)... no, (r,1) is in V and (r,2) is in H. Not exact at (r,1) unless both are V.

Wait, let me reconsider. The 2×2 square at (r, 1) covers (r,1), (r,1+1), (r+1,1), (r+1,2). (r,1) in V, (r,2) in H, (r+1,1) in V, (r+1,2) in H. 4 dominoes. Not exact.

The 2×2 square at (r, 2): (r,2) in H, (r,3) in H, (r+1,2) in H, (r+1,3) in H. 2 within. Exact!

The 2×2 square at (r, 3): (r,3) in H, (r,4) in V, (r+1,3) in H, (r+1,4) in V. 4. Not exact.

So exact squares are only at (r, 2) for each block. In a 100×100 board with this pattern tiled:
- 25 block-columns, each with H at columns 4j+2, 4j+3.
- 99 row positions.
- Exact squares: 25 × 99 = 2475.

But wait, I need to check the V columns at block boundaries. The 2×2 square at (r, 4) (boundary between blocks): (r,4) in V, (r,5) in V, (r+1,4) in V, (r+1,5) in V. 4 dominoes. Not exact. ✓

And the 2×2 square at (r, 4j) for any block boundary column: same, not exact. ✓

So total exact: 2475. But wait, I also need to check if there are exact squares at the V columns within a block. The V dominoes are at columns 4j+1 and 4j+4. The 2×2 square at (r, 4j+1): (r, 4j+1) in V, (r, 4j+2) in H, ... not exact. The 2×2 square at (r, 4j+3): (r, 4j+3) in H, (r, 4j+4) in V, ... not exact.

So the only exact squares are at (r, 4j+2) for r = 1, ..., 99 and j = 0, ..., 24. That's 99 × 25 = 2475.

Hmm, can we do better? What if we also offset the H pattern vertically?

Pattern:
```
Row 1: V H H V  (H at 2-3)
Row 2: V H H V  (H at 2-3)
Row 3: V V H H  (H at 3-4)... but column 4 is supposed to be V.
```

This doesn't work because the V columns are fixed.

Let me try a completely different approach. What if we use a 2×4 repeating tile?

Tile:
```
V H H V
V H H V
```
This is a 2×4 tile with V at columns 1,4 and H at columns 2-3.

Tiling this 50×25 times: 100×100 board. ✓

Exact squares: at (r, 4j+2) for r = 1, ..., 99 and j = 0, ..., 24. 99 × 25 = 2475.

But what about (r, 4j) for r = 1, 3, 5, ..., 99 (odd r)? (r, 4j) and (r, 4j+1): (r, 4j) in V (from previous tile or boundary), (r, 4j+1) in V. If both are in V dominoes within the same 2×2 square... (r, 4j) is in V((r, 4j)-(r+1, 4j)) if r is odd, or V((r-1, 4j)-(r, 4j)) if r is even. (r, 4j+1) is in V((r, 4j+1)-(r+1, 4j+1)) if r is odd.

For odd r: (r, 4j) in V(r, 4j)-(r+1, 4j), (r, 4j+1) in V(r, 4j+1)-(r+1, 4j+1), (r+1, 4j) in V, (r+1, 4j+1) in V. 2 dominoes within. Exact!

Oh! I missed this. The V columns also create exact squares.

For the 2×2 square at (2i-1, 4j) (odd row, block boundary column): (2i-1, 4j) in V, (2i-1, 4j+1) in V, (2i, 4j) in V, (2i, 4j+1) in V. 2 within. Exact!

But wait, column 4j is the last column of the previous tile (V column), and column 4j+1 is the first column of the next tile (V column). So both are V, and the 2×2 square at (2i-1, 4j) is exact.

Similarly, the 2×2 square at (2i-1, 4j+3) (within a tile, at the H-V boundary): (2i-1, 4j+3) in H, (2i-1, 4j+4) in V, (2i, 4j+3) in H, (2i, 4j+4) in V. 4. Not exact.

And (2i-1, 4j+1) (V-H boundary within tile): (2i-1, 4j+1) in V, (2i-1, 4j+2) in H, (2i, 4j+1) in V, (2i, 4j+2) in H. 4. Not exact.

So the exact squares are:
1. At (r, 4j+2) for all r = 1, ..., 99 and j = 0, ..., 24: H-H exact. 99 × 25 = 2475.
2. At (2i-1, 4j) for i = 1, ..., 50 and j = 1, ..., 24 (block boundary columns, not at the edge): V-V exact. 50 × 24 = 1200.

Wait, also at (2i-1, 0)? No, columns start at 1. The first tile has V at column 1 and 4. The 2×2 square at (2i-1, 1): (2i-1, 1) in V, (2i-1, 2) in H. Not exact.

At (2i-1, 4): (2i-1, 4) in V, (2i-1, 5) in V (next tile). Both V. (2i, 4) in V, (2i, 5) in V. 2 within. Exact! So j = 1, ..., 24 (columns 4, 8, ..., 96). 50 × 24 = 1200.

But also at the right edge: column 100 is V (last tile's column 4 = column 100). The 2×2 square at (2i-1, 99): (2i-1, 99) in H, (2i-1, 100) in V. Not exact.

And at the left edge: column 1 is V. (2i-1, 1): V, H. Not exact.

So total exact: 2475 + 1200 = 3675. That's worse than the 4×4 pattern's 2500!

Hmm, the 2×4 tile is worse because the V-V boundaries create many exact squares.

Let me go back to the 4×4 pattern that gave 2500 and see if I can improve it.

The 4×4 pattern:
```
H H V V
H H V V
V V H H
V V H H
```

This gave 4 exact per block, 2500 total, with no boundary exact squares.

Can I find a pattern with fewer than 4 exact per 4×4 block?

Let me try:
```
H V V H
H V V H
V H H V
V H H V
```

Explicitly:
Row 1: (1,1)-(1,2) H, (1,3)-(2,3) V, (1,4)-(2,4) V. Wait, that doesn't match. Let me re-think.

"H V V H" means: columns 1-2 have H, columns 3-4 have V? No, "H V V H" as a 4-column pattern means... I need to be more explicit.

Let me try:
```
(1,1)-(2,1) V, (1,2)-(1,3) H, (1,4)-(2,4) V
(2,1) in V, (2,2)-(2,3) H, (2,4) in V
(3,1)-(3,2) H, (3,3)-(4,3) V, (3,4)-(4,4) V
(4,1)-(4,2) H, (4,3) in V, (4,4) in V
```

2×2 squares:
(1,1): V(1,1-2,1), H(1,2-1,3), V(2,1 in V), H(2,2-2,3). (1,1) V, (1,2) H, (2,1) V, (2,2) H. 4. Not exact.
(1,2): H(1,2-1,3), H(2,2-2,3). 2 within. Exact!
(1,3): H(1,2-1,3), V(1,4-2,4), H(2,2-2,3), V. 4. Not exact.
(2,1): V(1,1-2,1), H(2,2-2,3), H(3,1-3,2), V(3,3-4,3). (2,1) in V crossing up, (2,2) in H, (3,1) in H, (3,2) in H. Wait, (3,1)-(3,2) is H. So (2,1) V, (2,2) H, (3,1) H, (3,2) H. 4 (V, H, H, H)... actually (3,1) and (3,2) are in the same H domino. So dominoes: V(1,1-2,1), H(2,2-2,3), H(3,1-3,2). 3 dominoes. Not exact.
(2,2): H(2,2-2,3), H(3,1-3,2). Wait, (2,2)-(2,3) H and (3,1)-(3,2) H. But (3,2) is not in the 2×2 square at (2,2). The 2×2 square at (2,2) covers (2,2),(2,3),(3,2),(3,3). (2,2)-(2,3) H within. (3,2) in H(3,1-3,2) crossing left boundary. (3,3) in V(3,3-4,3) crossing down. 3 dominoes. Not exact.
(2,3): H(2,2-2,3), V(1,4-2,4), V(3,3-4,3), V(3,4-4,4). (2,3) in H, (2,4) in V crossing up, (3,3) in V crossing down, (3,4) in V crossing down. 4. Not exact.
(3,1): H(3,1-3,2), H(4,1-4,2). 2 within. Exact!
(3,2): H(3,1-3,2), V(3,3-4,3), H(4,1-4,2), V(4,3-4,4). (3,2) in H, (3,3) in V, (4,2) in H, (4,3) in V. 4. Not exact.
(3,3): V(3,3-4,3), V(3,4-4,4). 2 within. Exact!

3 exact! Same as the previous pattern.

Now let me check the boundary effects when tiling.

Horizontal tiling (next block at column 5):
```
V H H V | V H H V
V H H V | V H H V
H H V V | H H V V
H H V V | H H V V
```

Wait, the second block should be the same pattern:
```
Row 1: V H H V | V H H V
Row 2: V H H V | V H H V
Row 3: H H V V | H H V V
Row 4: H H V V | H H V V
```

2×2 square at (1,4): (1,4) in V(1,4-2,4), (1,5) in V(1,5-2,5), (2,4) in V, (2,5) in V. 4. Not exact. ✓

2×2 square at (3,4): (3,4) in V(3,4-4,4), (3,5) in V(3,5-4,5), (4,4) in V, (4,5) in V. 4. Not exact. ✓

Vertical tiling (next block at row 5):
```
V H H V
V H H V
H H V V
H H V V
V H H V
V H H V
H H V V
H H V V
```

2×2 square at (4,1): (4,1) in H(4,1-4,2), (4,2) in H, (5,1) in V(5,1-6,1), (5,2) in H(5,2-5,3). (4,1) H, (4,2) H, (5,1) V, (5,2) H. 3 dominoes. Not exact. ✓

2×2 square at (4,2): (4,2) in H(4,1-4,2), (4,3) in V(3,3-4,3)... wait, (4,3) is in V(3,3-4,3). (5,2) in H(5,2-5,3), (5,3) in H. So (4,2) H, (4,3) V, (5,2) H, (5,3) H. 3 dominoes (H(4,1-4,2), V(3,3-4,3), H(5,2-5,3)). Not exact. ✓

2×2 square at (4,3): (4,3) in V(3,3-4,3), (4,4) in V(3,4-4,4), (5,3) in H(5,2-5,3), (5,4) in V(5,4-6,4). 4. Not exact. ✓

2×2 square at (4,4): (4,4) in V(3,4-4,4), (4,5) in V(3,5-4,5)... wait, (4,5) is in the next block. In the next block, (5,5) is in V(5,5-6,5). But (4,5) is in the first block's row 4, which has V at columns 3-4. (4,5) is in the second block's column 1 (column 5), which is V(5,5-6,5)? No, (4,5) is in row 4, which is in the first block. The first block covers rows 1-4. Column 5 is in the second horizontal block. 

Hmm, I need to be more careful. Let me consider a 4×8 region (two blocks side by side):

Block 1 (cols 1-4), Block 2 (cols 5-8):
```
Row 1: V
