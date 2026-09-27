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
  <problem_id>polymath_00612</problem_id>
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

Each cell of an $n \times n$ board is painted either black or white, where $n=100$. All cells adjacent to the boundary of the board are black. Let $S$ be the number of $2 \times 2$ squares on the board that are either monochromatic or painted in a checkerboard pattern. If there are no monochromatic $2 \times 2$ squares on the board, find the minimum possible value of $S$.

## Standard Solution

Let $N$ be the number of grid segments separating differently colored cells. According to the original solution, if a $2 \times 2$ square is neither monochromatic nor checkerboard, it contains exactly 2 separators. If it is a checkerboard pattern, it contains 4 separators. Let $C$ be the number of checkerboard $2 \times 2$ squares and $M$ be the number of monochromatic $2 \times 2$ squares. The total number of squares is $(n-1)^2$.
The total number of interior separators is $N = \frac{1}{2}(2((n-1)^2 - C - M) + 4C) = (n-1)^2 + C - M$.
The solution states that $N$ must be even because the first and last cells of every row and column are black, forcing an even number of color changes in each row/column.
Given $M=0$, we have $N = (n-1)^2 + C$. For $n=100$, $(n-1)^2 = 99^2$, which is odd. For $N$ to be even, $C$ must be at least 1.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have an $n \times n$ board with $n=100$. Each cell is black or white. All cells adjacent to the boundary are black (so the entire first and last row, and first and last column are black).

Let $S$ be the number of $2 \times 2$ squares that are either monochromatic or painted in a checkerboard pattern.

If there are no monochromatic $2 \times 2$ squares, find the minimum possible value of $S$.

So $S$ counts $2 \times 2$ squares that are either:
- Monochromatic (all 4 cells same color), or
- Checkerboard pattern (alternating colors, like BW/WB or WB/BW)

A $2 \times 2$ square is "checkerboard" if it has 2 black and 2 white cells arranged in alternating pattern. There are two checkerboard patterns:
```
B W    W B
W B    B W
```

So a $2 \times 2$ square is counted in $S$ if it's monochromatic (all same) or checkerboard (alternating).

A $2 \times 2$ square is NOT counted in $S$ if it has 2 black and 2 white but NOT in checkerboard pattern - i.e., it has two adjacent cells of the same color forming an "L" or "stripe" pattern. These are the 4 non-checkerboard, non-monochromatic patterns:
```
B B    B W    B B    W B
B W    B W    W W    W B
```
Wait, let me think more carefully. A $2 \times 2$ square with cells $a, b, c, d$ (top-left, top-right, bottom-left, bottom-right).

Monochromatic: all same. (2 patterns: all black, all white)
Checkerboard: $a \neq b, a \neq c, b = d, c = d$ — i.e., $a = d \neq b = c$. (2 patterns)
Other: everything else.

Total $2 \times 2$ colorings: $2^4 = 16$.
Monochromatic: 2
Checkerboard: 2
Other: 12

The "other" patterns are those where the coloring is neither monochromatic nor checkerboard. These have exactly 2 black and 2 white but in a non-alternating arrangement, OR 3-1 splits.

Wait, 3-1 splits: 8 patterns (4 positions for the odd one out × 2 colors). These are "other".
2-2 splits: $\binom{4}{2} = 6$ patterns. Of these, 2 are checkerboard, 4 are "other" (the stripe/L patterns).
1-3 splits: same as 3-1, already counted.
0-4 and 4-0: monochromatic, 2 patterns.

So: 2 (mono) + 2 (checker) + 4 (2-2 other) + 8 (3-1) = 16. ✓

So a $2 \times 2$ square is NOT in $S$ iff it's one of the 12 "other" patterns.

We want to minimize $S$ subject to:
1. No monochromatic $2 \times 2$ square (so all $2 \times 2$ squares are either checkerboard or "other").
2. Boundary cells are all black.

So under constraint 1, $S$ = number of checkerboard $2 \times 2$ squares. We want to minimize the number of checkerboard $2 \times 2$ squares.

Total $2 \times 2$ squares = $(n-1)^2 = 99^2 = 9801$.

Each $2 \times 2$ square is either checkerboard or "other" (since no monochromatic). We want to minimize checkerboard count, equivalently maximize "other" count.

Let me think about what "other" means in terms of the coloring. Let me use a different representation. Let $x_{i,j} \in \{0, 1\}$ where 0 = white, 1 = black.

A $2 \times 2$ square at position $(i,j)$ (top-left corner) has cells $(i,j), (i,j+1), (i+1,j), (i+1,j+1)$.

Monochromatic: all four equal.
Checkerboard: $x_{i,j} \neq x_{i,j+1}$, $x_{i,j} \neq x_{i+1,j}$, $x_{i,j} = x_{i+1,j+1}$, $x_{i,j+1} = x_{i+1,j}$.

Let me think in terms of "transitions". Define horizontal transition $h_{i,j} = x_{i,j} \oplus x_{i,j+1}$ and vertical transition $v_{i,j} = x_{i,j} \oplus x_{i+1,j}$.

For a $2 \times 2$ square at $(i,j)$:
- $h_{i,j}$ = horizontal transition in top row
- $h_{i+1,j}$ = horizontal transition in bottom row
- $v_{i,j}$ = vertical transition in left column
- $v_{i,j+1}$ = vertical transition in right column

Monochromatic: $h_{i,j} = h_{i+1,j} = v_{i,j} = v_{i,j+1} = 0$.
Checkerboard: $h_{i,j} = h_{i+1,j} = 1$ and $v_{i,j} = v_{i,j+1} = 1$ (and they're consistent, which they automatically are).

Actually, let me verify. Checkerboard means $x_{i,j} \neq x_{i,j+1}$ (so $h_{i,j}=1$), $x_{i+1,j} \neq x_{i+1,j+1}$ (so $h_{i+1,j}=1$), $x_{i,j} \neq x_{i+1,j}$ (so $v_{i,j}=1$), $x_{i,j+1} \neq x_{i+1,j+1}$ (so $v_{i,j+1}=1$). And consistency: $x_{i,j} \oplus x_{i+1,j+1} = h_{i,j} \oplus v_{i+1,j} = v_{i,j} \oplus h_{i+1,j}$. For checkerboard, $x_{i,j} = x_{i+1,j+1}$, so $h_{i,j} \oplus v_{i+1,j} = 0$, i.e., $h_{i,j} = v_{i+1,j}$... hmm, this is getting complicated.

Let me think differently. The four transition values $h_{i,j}, h_{i+1,j}, v_{i,j}, v_{i,j+1}$ around a $2 \times 2$ square satisfy a constraint: $h_{i,j} \oplus h_{i+1,j} = v_{i,j} \oplus v_{i,j+1}$ (this is because both equal $x_{i,j} \oplus x_{i,j+1} \oplus x_{i+1,j} \oplus x_{i+1,j+1}$).

So the constraint is: $h_{i,j} \oplus h_{i+1,j} \oplus v_{i,j} \oplus v_{i,j+1} = 0$.

Given this constraint, the possible $(h_{i,j}, h_{i+1,j}, v_{i,j}, v_{i,j+1})$ with even parity:
- (0,0,0,0): monochromatic
- (1,1,1,1): checkerboard
- (1,1,0,0): "other" - two horizontal transitions, no vertical
- (0,0,1,1): "other" - two vertical transitions, no horizontal
- (1,0,1,0): "other"
- (0,1,0,1): "other"
- (1,0,0,1): "other"
- (0,1,1,0): "other"

So 8 patterns with even parity. Monochromatic = (0,0,0,0), checkerboard = (1,1,1,1), other = the 6 remaining.

Wait, but I said there are 12 "other" patterns out of 16 total. The 8 with even parity correspond to... hmm, actually each pattern of $(h, h', v, v')$ with even parity corresponds to exactly 2 colorings (choose $x_{i,j}$ freely, the rest determined). So 8 parity patterns × 2 = 16 colorings. ✓

Monochromatic (0,0,0,0): 2 colorings. ✓
Checkerboard (1,1,1,1): 2 colorings. ✓
Other (6 patterns): 6 × 2 = 12 colorings. ✓

Great. So under the constraint of no monochromatic $2 \times 2$ squares, every $2 \times 2$ square has transition pattern that's either (1,1,1,1) [checkerboard] or one of the 6 "other" even-parity patterns.

Now, $S$ = number of checkerboard $2 \times 2$ squares = number of $(i,j)$ where the transition pattern is (1,1,1,1).

We want to minimize this, subject to:
- No $2 \times 2$ square has pattern (0,0,0,0).
- Boundary cells all black.

Let me think about this more carefully. The boundary condition: all cells in row 1, row $n$, column 1, column $n$ are black (1).

So $x_{1,j} = 1$ for all $j$, $x_{n,j} = 1$ for all $j$, $x_{i,1} = 1$ for all $i$, $x_{i,n} = 1$ for all $i$.

This means:
- $h_{1,j} = 0$ for $j = 1, \ldots, n-1$ (top row all black, no horizontal transitions)
- $h_{n,j} = 0$ for $j = 1, \ldots, n-1$ (bottom row all black)
- $v_{i,1} = 0$ for $i = 1, \ldots, n-1$ (left column all black)
- $v_{i,n} = 0$ for $i = 1, \ldots, n-1$ (right column all black)

Now, the interior is the $(n-2) \times (n-2) = 98 \times 98$ grid from rows 2 to 99, columns 2 to 99.

Let me think about the structure. We have a grid of horizontal transitions $h_{i,j}$ for $i = 1, \ldots, n$ and $j = 1, \ldots, n-1$, and vertical transitions $v_{i,j}$ for $i = 1, \ldots, n-1$ and $j = 1, \ldots, n$.

The constraints are:
1. Parity constraint for each $2 \times 2$ square: $h_{i,j} \oplus h_{i+1,j} \oplus v_{i,j} \oplus v_{i,j+1} = 0$ for $i = 1, \ldots, n-1$, $j = 1, \ldots, n-1$.
2. No monochromatic: not all of $h_{i,j}, h_{i+1,j}, v_{i,j}, v_{i,j+1}$ are 0.
3. Boundary: $h_{1,j} = h_{n,j} = 0$, $v_{i,1} = v_{i,n} = 0$.
4. The transitions must be realizable (i.e., there exists a coloring). This is guaranteed if the parity constraints are all satisfied and we fix one cell.

Actually, the transitions are realizable iff all parity constraints are satisfied (the grid is simply connected). So constraints 1 and 3 (fixing boundary) plus choosing $x_{1,1} = 1$ determines everything... no wait, the transitions don't uniquely determine the coloring, but if all parity constraints hold, a coloring exists.

Hmm, but actually the transitions DO determine the coloring up to a global flip. Given all $h$ and $v$ values satisfying parity constraints, and fixing one cell, the entire coloring is determined.

But we're choosing the coloring, which determines the transitions. So we're free to choose any coloring, which gives transitions satisfying parity, and we have the boundary constraints.

Let me think about this differently. Let me consider the "interior" cells, rows 2 to $n-1$ and columns 2 to $n-1$ (i.e., the $98 \times 98$ interior). The boundary is all black.

Actually, let me think about what patterns avoid monochromatic $2 \times 2$ squares while minimizing checkerboard $2 \times 2$ squares.

A $2 \times 2$ square is "other" (not in $S$, not monochromatic) if its transition pattern is one of:
- (1,1,0,0): horizontal stripes (top row differs from bottom row, each row uniform)
- (0,0,1,1): vertical stripes
- (1,0,1,0), (0,1,0,1), (1,0,0,1), (0,1,1,0): various L-shapes

To minimize checkerboard squares, we want as many "other" squares as possible.

Let me think about a specific construction. Consider a coloring where each row is either all black or all white, except we need to avoid monochromatic $2 \times 2$ squares.

If two consecutive rows are both all black, then every $2 \times 2$ square spanning them is monochromatic. So we can't have two consecutive all-black rows. Similarly for all-white.

But the boundary rows (row 1 and row $n$) are all black. So row 2 cannot be all black (otherwise $2 \times 2$ squares in rows 1-2 are monochromatic). 

Hmm, but if row 2 is all white, then $2 \times 2$ squares in rows 1-2 have pattern (1,1,0,0) — top row black, bottom row white, which is "other" (horizontal stripes). Good, not monochromatic, not checkerboard.

But then row 3: if row 3 is all black, then rows 2-3 have pattern (0,0,1,1) — wait no. If row 2 is all white and row 3 is all black, then $h_{2,j} = 0$ (row 2 uniform white), $h_{3,j} = 0$ (row 3 uniform black), $v_{2,j} = 1$ (white to black), $v_{2,j+1} = 1$. So pattern is (0,0,1,1) = vertical stripes = "other". Good.

If row 3 is all white, then rows 2-3 are both all white, giving monochromatic $2 \times 2$ squares. Bad.

So with the "uniform rows" approach: rows alternate between all-black and all-white. Row 1 = black, row 2 = white, row 3 = black, row 4 = white, etc. But row $n = 100$ must be black. With alternating starting from black: row 1 = B, row 2 = W, row 3 = B, ..., row 100 = B (since 100 is even, row 100 = B). ✓

In this construction, every $2 \times 2$ square has pattern (0,0,1,1) or (1,1,0,0) — all "other". So $S = 0$?

Wait, but we need to check: are there any monochromatic $2 \times 2$ squares? No, because consecutive rows always differ. Are there any checkerboard $2 \times 2$ squares? A checkerboard requires $h_{i,j} = h_{i+1,j} = 1$ and $v_{i,j} = v_{i,j+1} = 1$. But in our construction, $h_{i,j} = 0$ for all $i, j$ (every row is uniform). So no checkerboard squares. And no monochromatic squares (consecutive rows differ). So $S = 0$.

But wait — the problem says "all cells adjacent to the boundary are black." Let me re-read.

"All cells adjacent to the boundary of the board are black."

Hmm, "adjacent to the boundary" — does this mean the cells touching the boundary, i.e., the outermost ring? Or cells adjacent to the boundary, meaning one cell in from the boundary?

I think "adjacent to the boundary" means the cells that share an edge with the boundary of the board, i.e., the outermost cells. So the first row, last row, first column, last column are all black. That's what I assumed.

With this interpretation, $S = 0$ seems achievable with the alternating rows construction. But that seems too easy for a competition problem. Let me re-read the problem.

"Each cell of an $n \times n$ board is painted either black or white, where $n=100$. All cells adjacent to the boundary of the board are black. Let $S$ be the number of $2 \times 2$ squares on the board that are either monochromatic or painted in a checkerboard pattern. If there are no monochromatic $2 \times 2$ squares on the board, find the minimum possible value of $S$."

Hmm, with my construction, $S = 0$. But that can't be right for a competition problem. Let me reconsider what "adjacent to the boundary" means.

Maybe "adjacent to the boundary" means the cells that are adjacent (share an edge) with the boundary cells, i.e., the second ring? No, that doesn't make sense either.

Actually, in some problem formulations, "cells adjacent to the boundary" could mean cells that share an edge or corner with the boundary. But the most natural reading is the outermost cells.

Wait, maybe I should reconsider. Perhaps "adjacent to the boundary" means cells that are next to (i.e., touching) the boundary — the boundary is the edge of the board, so cells adjacent to the boundary are the cells on the edge. That's the outermost ring.

With the alternating rows construction, $S = 0$. Let me double-check with a small example. $n = 4$:

```
B B B B
W W W W
B B B B
B B B B
```

Wait, row 4 must be black (boundary). Row 3 = B, row 4 = B. Then the $2 \times 2$ squares in rows 3-4 are all black = monochromatic! That violates the constraint.

Oh wait, I need $n = 100$ and row 100 = B. With alternating B, W, B, W, ..., row $k$ = B if $k$ odd, W if $k$ even. Row 100 is even, so row 100 = W. But row 100 must be B! Contradiction!

Let me recheck. Row 1 = B, row 2 = W, row 3 = B, ..., row $k$ = B if $k$ is odd, W if $k$ is even. Row 100 is even → W. But boundary requires row 100 = B. So this doesn't work for $n = 100$ (even).

Hmm, so for even $n$, the simple alternating rows don't work because both the first and last rows need to be black, but they're an odd number of rows apart (99 rows apart), so they'd have different colors in the alternating scheme.

Wait, row 1 and row 100 are 99 rows apart. 99 is odd. So if row 1 = B, row 100 = W in the alternating scheme. But we need row 100 = B. So we need to break the alternation somewhere.

OK so this is more interesting. Let me reconsider.

We need a coloring where:
- Row 1 and row 100 are all black (boundary).
- Column 1 and column 100 are all black (boundary).
- No monochromatic $2 \times 2$ square.
- Minimize the number of checkerboard $2 \times 2$ squares.

The boundary condition forces row 1 = all B and row 100 = all B. Since no two consecutive rows can both be all-B (that creates monochromatic $2 \times 2$ squares), row 2 must not be all-B, and row 99 must not be all-B.

But actually, we don't need uniform rows. Let me think more generally.

Let me reconsider the problem. The key constraint is that the boundary is all black, and we need no monochromatic $2 \times 2$ squares, and we minimize checkerboard $2 \times 2$ squares.

Let me think about what happens near the boundary. Consider the $2 \times 2$ square at position $(1, j)$ (top-left corner at row 1, column $j$), for $j = 1, \ldots, 99$. This square has cells $(1, j), (1, j+1), (2, j), (2, j+1)$. Since row 1 is all black, $(1, j) = (1, j+1) = B$. For this not to be monochromatic, at least one of $(2, j), (2, j+1)$ must be white. For this not to be checkerboard, we need... let's see. The transitions are $h_{1,j} = 0$ (both black), $v_{1,j} = x_{1,j} \oplus x_{2,j} = x_{2,j}$, $v_{1,j+1} = x_{2,j+1}$, $h_{2,j} = x_{2,j} \oplus x_{2,j+1}$.

The pattern is $(h_{1,j}, h_{2,j}, v_{1,j}, v_{1,j+1}) = (0, h_{2,j}, v_{1,j}, v_{1,j+1})$ with parity constraint $0 \oplus h_{2,j} \oplus v_{1,j} \oplus v_{1,j+1} = 0$, i.e., $h_{2,j} = v_{1,j} \oplus v_{1,j+1}$.

This is automatically satisfied since $h_{2,j} = x_{2,j} \oplus x_{2,j+1} = v_{1,j} \oplus v_{1,j+1}$ (since $x_{1,j} = x_{1,j+1} = 1$).

For not monochromatic: not all transitions 0, i.e., at least one of $h_{2,j}, v_{1,j}, v_{1,j+1}$ is 1. Since $v_{1,j} = x_{2,j}$ and $v_{1,j+1} = x_{2,j+1}$ (as $x_{1,*} = 1$), this means at least one of $x_{2,j}, x_{2,j+1}$ is white (0), or $h_{2,j} = 1$ (i.e., $x_{2,j} \neq x_{2,j+1}$).

Actually, if both $x_{2,j}$ and $x_{2,j+1}$ are black (1), then $v_{1,j} = v_{1,j+1} = 0$ and $h_{2,j} = 0$, so it's monochromatic. So we need: for every $j$, not both $x_{2,j} = 1$ and $x_{2,j+1} = 1$. In other words, row 2 has no two consecutive black cells.

Similarly, for the $2 \times 2$ square at position $(99, j)$ (rows 99-100), since row 100 is all black, we need row 99 to have no two consecutive black cells.

For the $2 \times 2$ square at position $(i, 1)$ (columns 1-2), since column 1 is all black, we need column 2 to have no two consecutive black cells.

For the $2 \times 2$ square at position $(i, 99)$ (columns 99-100), since column 100 is all black, we need column 99 to have no two consecutive black cells.

Now, for the $2 \times 2$ square at position $(1, j)$: is it checkerboard? Checkerboard requires all four transitions to be 1. But $h_{1,j} = 0$ (row 1 all black). So it can never be checkerboard. Similarly, $2 \times 2$ squares in the first row, last row, first column, last column can never be checkerboard (because one of the boundary transitions is 0).

So checkerboard $2 \times 2$ squares can only occur in the interior, i.e., at positions $(i, j)$ with $2 \leq i \leq 98$ and $2 \leq j \leq 98$.

Wait, let me be more precise. A $2 \times 2$ square at position $(i, j)$ involves rows $i, i+1$ and columns $j, j+1$. For it to potentially be checkerboard, we need all four transitions to be 1. The transitions involve $h_{i,j}, h_{i+1,j}, v_{i,j}, v_{i,j+1}$.

If $i = 1$: $h_{1,j} = 0$ (row 1 all black), so not checkerboard.
If $i = 99$: $h_{100,j} = 0$ (row 100 all black), so not checkerboard.
If $j = 1$: $v_{i,1} = 0$ (column 1 all black), so not checkerboard.
If $j = 99$: $v_{i,100} = 0$ (column 100 all black), so not checkerboard.

So checkerboard squares can only be at positions $(i, j)$ with $2 \leq i \leq 98$ and $2 \leq j \leq 98$. That's $97 \times 97 = 9409$ positions.

Now, the total number of $2 \times 2$ squares is $99 \times 99 = 9801$. The boundary $2 \times 2$ squares (those in the first/last row or first/last column of $2 \times 2$ positions) number $9801 - 9409 = 392$. These are all "other" (not monochromatic by constraint, not checkerboard as shown). So they contribute 0 to $S$.

We need to minimize checkerboard squares among the $97 \times 97$ interior positions.

Now, let me think about the interior more carefully. The interior cells are rows 2 to 99, columns 2 to 99 (a $98 \times 98$ grid). But the "interior" $2 \times 2$ squares involve rows 2 to 99 and columns 2 to 99 (positions $(i,j)$ with $2 \leq i \leq 98, 2 \leq j \leq 98$).

Hmm, this is getting complex. Let me think about a different approach.

Let me consider the problem in terms of the "second ring" — the cells in row 2, row 99, column 2, column 99 (just inside the boundary).

Actually, let me think about this more carefully using the transition framework.

Let me define the problem on the interior. Consider the grid of cells $x_{i,j}$ for $2 \leq i \leq 99, 2 \leq j \leq 99$ (the $98 \times 98$ interior). The boundary cells (row 1, row 100, col 1, col 100) are all 1 (black).

The constraints from no monochromatic $2 \times 2$:
- For $2 \times 2$ squares touching the boundary, we derived conditions on the second ring.
- For interior $2 \times 2$ squares (positions $2 \leq i \leq 98, 2 \leq j \leq 98$), the constraint is just that they're not monochromatic.

We want to minimize the number of checkerboard $2 \times 2$ squares among interior positions.

Let me think about what kind of coloring minimizes checkerboard squares while avoiding monochromatic ones.

A checkerboard $2 \times 2$ square has all four transitions equal to 1. An "other" square has some transitions 0 and some 1 (with even parity, not all 0).

To avoid checkerboard, we want to avoid having all four transitions be 1 simultaneously. To avoid monochromatic, we want to avoid all four being 0.

One approach: make many transitions 0. If we can make, say, all horizontal transitions 0 (uniform rows), then no $2 \times 2$ square can be checkerboard (since $h_{i,j} = 0$) and no $2 \times 2$ square can be monochromatic as long as consecutive rows differ (so $v_{i,j} = 1$ for all $i, j$). But we saw this doesn't work because of the boundary condition with even $n$.

Let me think about it differently. With uniform rows: row $i$ is all $c_i \in \{0, 1\}$. Then $h_{i,j} = 0$ for all $i, j$. $v_{i,j} = c_i \oplus c_{i+1}$. 

No monochromatic $2 \times 2$: $v_{i,j} = 1$ for all $i, j$, i.e., $c_i \neq c_{i+1}$ for all $i$. So rows strictly alternate.

Boundary: $c_1 = 1$ (row 1 black), $c_{100} = 1$ (row 100 black). With strict alternation: $c_i = 1$ if $i$ odd, $c_i = 0$ if $i$ even. Then $c_{100} = 0 \neq 1$. Contradiction.

So uniform rows don't work. What if we use uniform columns instead? Same issue by symmetry: column 1 and column 100 are both black, 99 columns apart, can't strictly alternate.

What about a mixed approach? Let me think about what happens if we use uniform rows except for one "break" row.

For instance: rows 1 to $k$ alternate B, W, B, W, ..., and rows $k$ to 100 alternate starting from the other phase. We need $c_1 = 1$ and $c_{100} = 1$.

If we have strict alternation except at one point where two consecutive rows have the same color, that creates monochromatic $2 \times 2$ squares at that boundary. So we can't simply break the alternation with uniform rows.

Hmm, so the uniform rows approach can't work for even $n$ with both boundary rows black. We need a more sophisticated approach.

Let me think about this differently. Let me consider the "stripe" pattern where we have uniform rows, but allow one row to be non-uniform.

Actually, let me think about the problem more carefully. Let me consider small cases first to build intuition.

For $n = 4$: The board is $4 \times 4$, boundary all black. Interior is $2 \times 2$ (rows 2-3, cols 2-3). The $2 \times 2$ squares are at positions $(i,j)$ for $i, j \in \{1, 2, 3\}$, so $9$ squares total.

The boundary $2 \times 2$ squares (touching the boundary) can't be checkerboard. The only interior $2 \times 2$ square is at position $(2, 2)$, involving cells $(2,2), (2,3), (3,2), (3,3)$.

For no monochromatic: 
- Square $(1,1)$: cells $(1,1)=B, (1,2)=B, (2,1)=B, (2,2)$. Not monochromatic requires $(2,2) = W$.
- Square $(1,2)$: cells $(1,2)=B, (1,3)=B, (2,2), (2,3)$. Not monochromatic requires at least one of $(2,2), (2,3)$ to be W.
- Square $(1,3)$: cells $(1,3)=B, (1,4)=B, (2,3), (2,4)=B$. Not monochromatic requires $(2,3) = W$.
- Square $(2,1)$: cells $(2,1)=B, (2,2), (3,1)=B, (3,2)$. Not monochromatic requires at least one of $(2,2), (3,2)$ to be W.
- Square $(3,1)$: cells $(3,1)=B, (3,2), (4,1)=B, (4,2)=B$. Not monochromatic requires $(3,2) = W$.
- Square $(3,2)$: cells $(3,2), (3,3), (4,2)=B, (4,3)=B$. Not monochromatic requires at least one of $(3,2), (3,3)$ to be W.
- Square $(3,3)$: cells $(3,3), (3,4)=B, (4,3)=B, (4,4)=B$. Not monochromatic requires $(3,3) = W$.
- Square $(2,3)$: cells $(2,3), (2,4)=B, (3,3), (3,4)=B$. Not monochromatic requires at least one of $(2,3), (3,3)$ to be W.
- Square $(2,2)$: cells $(2,2), (2,3), (3,2), (3,3)$. Not monochromatic.

From above: $(2,2) = W$ (from square $(1,1)$), $(2,3) = W$ (from square $(1,3)$), $(3,2) = W$ (from square $(3,1)$), $(3,3) = W$ (from square $(3,3)$).

So the entire interior is white! Then square $(2,2)$: all white = monochromatic. Contradiction!

So for $n = 4$, there's no valid coloring? That can't be right...

Wait, let me recheck. Square $(1,1)$: cells $(1,1), (1,2), (2,1), (2,2)$. All boundary except $(2,2)$. $(1,1) = B, (1,2) = B, (2,1) = B$. For not monochromatic, $(2,2) \neq B$, so $(2,2) = W$. ✓

Square $(1,3)$: cells $(1,3), (1,4), (2,3), (2,4)$. $(1,3) = B, (1,4) = B, (2,4) = B$. So $(2,3) = W$. ✓

Square $(3,1)$: cells $(3,1), (3,2), (4,1), (4,2)$. $(3,1) = B, (4,1) = B, (4,2) = B$. So $(3,2) = W$. ✓

Square $(3,3)$: cells $(3,3), (3,4), (4,3), (4,4)$. $(3,4) = B, (4,3) = B, (4,4) = B$. So $(3,3) = W$. ✓

Then square $(2,2)$: $(2,2) = W, (2,3) = W, (3,2) = W, (3,3) = W$. All white = monochromatic. 

So for $n = 4$, it's impossible to have no monochromatic $2 \times 2$ squares! Interesting.

Hmm, but the problem states $n = 100$ and asks for the minimum $S$ assuming no monochromatic $2 \times 2$ squares. So presumably for $n = 100$ it is possible.

Let me check $n = 5$. Interior is $3 \times 3$ (rows 2-4, cols 2-4).

Corner $2 \times 2$ squares:
- $(1,1)$: forces $(2,2) = W$.
- $(1,4)$: forces $(2,4) = W$.
- $(4,1)$: forces $(4,2) = W$.
- $(4,4)$: forces $(4,4) = W$.

Edge $2 \times 2$ squares:
- $(1,2)$: cells $(1,2)=B, (1,3)=B, (2,2), (2,3)$. Need at least one of $(2,2), (2,3)$ to be W. $(2,2) = W$ already, so OK regardless of $(2,3)$.
- $(1,3)$: cells $(1,3)=B, (1,4)=B, (2,3), (2,4)$. $(2,4) = W$ already, so OK.
- $(2,1)$: cells $(2,1)=B, (2,2), (3,1)=B, (3,2)$. $(2,2) = W$ already, so OK.
- $(3,1)$: cells $(3,1)=B, (3,2), (4,1)=B, (4,2)$. $(4,2) = W$ already, so OK.
- $(4,2)$: cells $(4,2), (4,3), (5,2)=B, (5,3)=B$. $(4,2) = W$ already, so OK.
- $(4,3)$: cells $(4,3), (4,4), (5,3)=B, (5,4)=B$. $(4,4) = W$ already, so OK.
- $(2,4)$: cells $(2,4), (2,5)=B, (3,4), (3,5)=B$. $(2,4) = W$ already, so OK.
- $(3,4)$: cells $(3,4), (3,5)=B, (4,4), (4,5)=B$. $(4,4) = W$ already, so OK.

Interior $2 \times 2$ squares:
- $(2,2)$: cells $(2,2)=W, (2,3), (3,2), (3,3)$. Need not monochromatic. Since $(2,2) = W$, need at least one of $(2,3), (3,2), (3,3)$ to be B.
- $(2,3)$: cells $(2,3), (2,4)=W, (3,3), (3,4)$. Need not monochromatic. Since $(2,4) = W$, need at least one of $(2,3), (3,3), (3,4)$ to be B.
- $(3,2)$: cells $(3,2), (3,3), (4,2)=W, (4,3)$. Need not monochromatic. Since $(4,2) = W$, need at least one of $(3,2), (3,3), (4,3)$ to be B.
- $(3,3)$: cells $(3,3), (3,4), (4,3), (4,4)=W$. Need not monochromatic. Since $(4,4) = W$, need at least one of $(3,3), (3,4), (4,3)$ to be B.

So we need to fill in $(2,3), (3,2), (3,3), (3,4), (4,3)$ such that each of the four interior $2 \times 2$ squares is not monochromatic.

Let me try: $(2,3) = B, (3,2) = B, (3,3) = B, (3,4) = B, (4,3) = B$.

Check:
- $(2,2)$: $W, B, B, B$. Not monochromatic. ✓ Is it checkerboard? $W, B / B, B$ — no, 3B 1W. "Other". ✓
- $(2,3)$: $B, W, B, B$. Not monochromatic. ✓ "Other".
- $(3,2)$: $B, B, W, B$. Not monochromatic. ✓ "Other".
- $(3,3)$: $B, B, B, W$. Not monochromatic. ✓ "Other".

So $S = 0$ for $n = 5$! Great, so for odd $n$, we can achieve $S = 0$.

Now for $n = 100$ (even), the situation is different. Let me think about why even $n$ is harder.

For $n = 4$ (even), we showed it's impossible. For $n = 6$ (even), let me check.

Actually, let me think about this more generally. The key issue with even $n$ is a parity/alternation argument.

Let me think about the corner cells. The cell $(2,2)$ is forced to be white (from the $2 \times 2$ square at corner $(1,1)$). Similarly, $(2, n-1)$ is forced white (from corner $(1, n-1)$), $(n-1, 2)$ is forced white (from corner $(n-1, 1)$), $(n-1, n-1)$ is forced white (from corner $(n-1, n-1)$).

Now consider the top edge. Row 1 is all black. For $2 \times 2$ square at $(1, j)$: cells $(1, j) = B, (1, j+1) = B, (2, j), (2, j+1)$. Not monochromatic requires at least one of $(2, j), (2, j+1)$ to be white. So row 2 has no two consecutive black cells.

Similarly, row $n-1$ has no two consecutive black cells, column 2 has no two consecutive black cells, column $n-1$ has no two consecutive black cells.

Now, row 2 has no two consecutive black cells, and $(2, 2) = W$, $(2, n-1) = W$. Row 2 has $n - 2 = 98$ cells (columns 2 to 99). With no two consecutive black cells, the maximum number of black cells in a row of 98 cells with no two consecutive blacks is $\lceil 98/2 \rceil = 49$.

Hmm, I'm not sure this line of reasoning directly leads to the answer. Let me think about the problem differently.

Let me think about a "checkerboard-like" coloring. Consider the standard checkerboard: $x_{i,j} = (i + j) \mod 2$. Then every $2 \times 2$ square is a checkerboard pattern. But the boundary: $x_{1,j} = (1 + j) \mod 2$, which alternates, not all black. So this doesn't satisfy the boundary condition.

What if we use a modified checkerboard in the interior? Let me think...

Actually, let me think about the problem in terms of a "defect" or "domain wall" argument.

Consider the coloring as a function $f: \{1, \ldots, n\}^2 \to \{0, 1\}$. Define $g(i,j) = f(i,j) \oplus (i + j \mod 2)$, which measures the deviation from a standard checkerboard.

A $2 \times 2$ square is checkerboard iff $g$ is constant on that square (all four cells have the same $g$ value). A $2 \times 2$ square is monochromatic iff $g$ alternates in the same pattern as the checkerboard (i.e., $g$ is a checkerboard on that square).

Hmm, this is an interesting duality. Let me verify.

If $f(i,j) = (i+j) \mod 2$ (standard checkerboard), then $g = 0$ everywhere. Every $2 \times 2$ square has $g$ constant (= 0), so every $2 \times 2$ square is checkerboard. ✓

If $f$ is constant (all black), then $g(i,j) = (i+j) \mod 2$, which is a checkerboard. Every $2 \times 2$ square has $g$ in checkerboard pattern, so every $2 \times 2$ square is monochromatic. ✓

So: $2 \times 2$ square is checkerboard in $f$ ⟺ $g$ is constant on that square.
$2 \times 2$ square is monochromatic in $f$ ⟺ $g$ is checkerboard on that square.
$2 \times 2$ square is "other" in $f$ ⟺ $g$ is "other" on that square.

This is a perfect duality! The problem asks: no monochromatic $2 \times 2$ squares in $f$ (i.e., no checkerboard $2 \times 2$ squares in $g$), minimize the number of checkerboard $2 \times 2$ squares in $f$ (i.e., minimize the number of monochromatic $2 \times 2$ squares in $g$).

Wait, that's the same problem but with the roles swapped! So the problem is self-dual under this transformation.

Hmm, but the boundary conditions change. In $f$, the boundary is all black (all 1). In $g$, the boundary is $g(i,j) = 1 \oplus (i + j \mod 2)$, which is a checkerboard pattern on the boundary.

So the dual problem is: $g$ has a checkerboard pattern on the boundary, no monochromatic $2 \times 2$ squares in $g$ (wait, no — no checkerboard $2 \times 2$ squares in $g$, which means no monochromatic in $f$), minimize monochromatic $2 \times 2$ squares in $g$ (which equals checkerboard in $f$ = $S$).

Hmm, this duality is interesting but might not directly help. Let me think differently.

Let me go back to thinking about constructions.

For even $n$, we can't have uniform alternating rows (because both boundary rows are black and they're an odd distance apart). So we need some non-uniform rows or a different structure.

Idea: Use a "stripe" pattern with one "defect" row. For example, rows alternate B, W, B, W, ..., but at some point we insert a non-uniform row to fix the parity.

Let me think about this more carefully. With $n = 100$:
- Rows 1, 3, 5, ..., 99 are all black (odd rows).
- Rows 2, 4, 6, ..., 98 are all white (even rows).
- Row 100 is all black.

But rows 99 and 100 are both all black, creating monochromatic $2 \times 2$ squares. Bad.

Alternative: 
- Rows 1, 3, 5, ..., 97 are all black.
- Rows 2, 4, 6, ..., 98 are all white.
- Row 99: needs to differ from row 98 (all white) and row 100 (all black).
  - If row 99 is all black: rows 99-100 both black → monochromatic. Bad.
  - If row 99 is all white: rows 98-99 both white → monochromatic. Bad.
  - So row 99 must be non-uniform.

Row 99 must have no two consecutive black cells (because row 100 is all black, so $2 \times 2$ squares in rows 99-100 need row 99 to not have two consecutive blacks). Also, row 99 must have no two consecutive white cells (because row 98 is all white, so $2 \times 2$ squares in rows 98-99 need row 99 to not have two consecutive whites). 

Wait, that's not quite right. Let me re-derive.

$2 \times 2$ square at $(98, j)$: rows 98-99, columns $j, j+1$. Row 98 is all white. Cells: $(98, j) = W, (98, j+1) = W, (99, j), (99, j+1)$. Not monochromatic requires at least one of $(99, j), (99, j+1)$ to be black. So row 99 has no two consecutive white cells.

$2 \times 2$ square at $(99, j)$: rows 99-100, columns $j, j+1$. Row 100 is all black. Cells: $(99, j), (99, j+1), (100, j) = B, (100, j+1) = B$. Not monochromatic requires at least one of $(99, j), (99, j+1)$ to be white. So row 99 has no two consecutive black cells.

So row 99 must have no two consecutive white cells AND no two consecutive black cells. This means row 99 must strictly alternate: B, W, B, W, ... or W, B, W, B, ...

Row 99 has cells in columns 1 to 100. Column 1 and column 100 are black (boundary). So $(99, 1) = B$ and $(99, 100) = B$. With strict alternation starting from B: B, W, B, W, ..., B (column 100 is even, so B if starting from B at column 1). Wait, column 1 = B, column 2 = W, column 3 = B, ..., column $j$ = B if $j$ odd, W if $j$ even. Column 100 is even → W. But we need column 100 = B. Contradiction!

With strict alternation starting from W: W, B, W, B, ..., column 1 = W. But we need column 1 = B. Contradiction!

So row 99 can't strictly alternate while satisfying the boundary conditions. This means the approach of having all other rows uniform and only row 99 non-uniform doesn't work either!

So we need more non-uniform rows. This is getting complex. Let me think about the problem structure more carefully.

Let me consider the problem as a constraint satisfaction / optimization problem and think about lower bounds.

Actually, let me think about this using the transition framework more carefully.

Let me focus on the "second ring" — row 2, row 99, column 2, column 99.

From the boundary conditions:
- Row 2: no two consecutive black cells (from row 1 being all black). Also $(2, 1) = B$ and $(2, 100) = B$ (boundary). But wait, $(2, 1)$ is in column 1, which is boundary (black). And $(2, 100)$ is in column 100, boundary (black). So row 2 has black at positions 1 and 100, and no two consecutive blacks in positions 1-100. But positions 1 and 2: $(2, 1) = B$, so $(2, 2) \neq B$, i.e., $(2, 2) = W$. Position 99 and 100: $(2, 100) = B$, so $(2, 99) \neq B$, i.e., $(2, 99) = W$.

Similarly:
- Row 99: no two consecutive black cells (from row 100 being all black). $(99, 1) = B, (99, 100) = B$. So $(99, 2) = W, (99, 99) = W$.
- Column 2: no two consecutive black cells (from column 1 being all black). $(1, 2) = B, (100, 2) = B$. So $(2, 2) = W, (99, 2) = W$.
- Column 99: no two consecutive black cells (from column 100 being all black). $(1, 99) = B, (100, 99) = B$. So $(2, 99) = W, (99, 99) = W$.

Now, let me think about row 2 more carefully. Row 2 has cells $(2, 1) = B, (2, 2) = W, \ldots, (2, 99) = W, (2, 100) = B$. No two consecutive blacks. The cells from column 2 to 99 (98 cells) start and end with W, and have no two consecutive blacks. 

The maximum number of blacks in positions 2 to 99 (98 cells, starting and ending with W, no two consecutive blacks): we can place blacks at positions 3, 5, 7, ..., 97 (odd positions from 3 to 97), which is 48 blacks. Or positions 4, 6, ..., 98, which is 48 blacks. So max 48 blacks in the interior of row 2.

But actually, we also need to consider the constraint from column 2 and column 99.

$(2, 2) = W$ (from both row and column constraints). $(2, 99) = W$ (from both row and column constraints).

Now, column 2 has no two consecutive black cells, with $(1, 2) = B, (100, 2) = B, (2, 2) = W, (99, 2) = W$. So in column 2, positions 2 and 99 are W, and no two consecutive blacks.

Similarly for column 99 and row 99.

This is getting quite involved. Let me try to think about the problem from a higher level.

The key insight might be related to a "parity" or "winding number" argument. Let me think about the dual problem again.

Recall: $g(i,j) = f(i,j) \oplus ((i+j) \mod 2)$. The boundary of $g$ is a checkerboard pattern. We want no checkerboard $2 \times 2$ squares in $g$ (equivalent to no monochromatic in $f$), and we want to minimize monochromatic $2 \times 2$ squares in $g$ (equivalent to minimizing $S$).

A monochromatic $2 \times 2$ square in $g$ means $g$ is constant on that square. No checkerboard $2 \times 2$ square in $g$ means $g$ doesn't have the alternating pattern on any square.

Hmm, the dual problem has a checkerboard boundary, which is a different kind of constraint.

Let me try yet another approach. Let me think about the problem in terms of "runs" and "defects."

Actually, let me try to think about this problem computationally for small even $n$ to find a pattern.

For $n = 4$: impossible (shown above).
For $n = 6$: Let me try to find a valid coloring.

$n = 6$, boundary all black. Interior is $4 \times 4$ (rows 2-5, cols 2-5).

Corner constraints: $(2,2) = W, (2,5) = W, (5,2) = W, (5,5) = W$.

Row 2: no two consecutive blacks. $(2,1) = B, (2,6) = B, (2,2) = W, (2,5) = W$. Cells $(2,3), (2,4)$ are free (subject to no two consecutive blacks). Since $(2,2) = W$, $(2,3)$ can be B or W. If $(2,3) = B$, then $(2,4) = W$ (no two consecutive blacks, and $(2,5) = W$ so that's fine). If $(2,3) = W$, then $(2,4)$ can be B or W, but if $(2,4) = B$, then $(2,5) = W$ is fine.

Let me try $(2,3) = B, (2,4) = W$. Row 2: B W B W W B. No two consecutive blacks: positions 1,3 are black, not consecutive. ✓

Similarly, row 5: no two consecutive blacks. $(5,1) = B, (5,6) = B, (5,2) = W, (5,5) = W$. Let me try $(5,3) = B, (5,4) = W$. Row 5: B W B W W B. ✓

Column 2: no two consecutive blacks. $(1,2) = B, (6,2) = B, (2,2) = W, (5,2) = W$. Cells $(3,2), (4,2)$ free. Try $(3,2) = B, (4,2) = W$. Column 2: B W B W W B. ✓

Column 5: no two consecutive blacks. $(1,5) = B, (6,5) = B, (2,5) = W, (5,5) = W$. Try $(3,5) = B, (4,5) = W$. Column 5: B W B W W B. ✓

Now I need to fill in the remaining interior cells: $(3,3), (3,4), (4,3), (4,4)$.

Let me also check the constraints from the $2 \times 2$ squares involving row 2 and row 3, etc.

$2 \times 2$ square at $(2, 2)$: cells $(2,2)=W, (2,3)=B, (3,2)=B, (3,3)$. Not monochromatic: already has W and B. ✓. Is it checkerboard? $W, B / B, ?$. For checkerboard: $W, B / B, W$, so $(3,3) = W$. Or $W, B / B, W$ — yes, checkerboard requires $(3,3) = W$.

$2 \times 2$ square at $(2, 3)$: cells $(2,3)=B, (2,4)=W, (3,3), (3,4)$. Not monochromatic: has B and W. ✓. Checkerboard? $B, W / ?, ?$. For checkerboard: $B, W / W, B$, so $(3,3) = W, (3,4) = B$.

$2 \times 2$ square at $(2, 4)$: cells $(2,4)=W, (2,5)=W, (3,4), (3,5)=B$. Not monochromatic: has W and B. ✓. Checkerboard? $W, W / ?, B$. For checkerboard, need $W, B / B, W$ or $B, W / W, B$. But top row is $W, W$, not alternating. So not checkerboard. ✓

$2 \times 2$ square at $(3, 2)$: cells $(3,2)=B, (3,3), (4,2)=W, (4,3)$. Not monochromatic: has B and W. ✓. Checkerboard? $B, ? / W, ?$. For checkerboard: $B, W / W, B$, so $(3,3) = W, (4,3) = B$.

$2 \times 2$ square at $(3, 3)$: cells $(3,3), (3,4), (4,3), (4,4)$. Need not monochromatic.

$2 \times 2$ square at $(3, 4)$: cells $(3,4), (3,5)=B, (4,4), (4,5)=W$. Not monochromatic: has B and W. ✓. Checkerboard? $?, B / ?, W$. For checkerboard: $W, B / B, W$, so $(3,4) = W, (4,4) = B$. Or $B, B / W, W$ — no, that's not checkerboard.

$2 \times 2$ square at $(4, 2)$: cells $(4,2)=W, (4,3), (5,2)=W, (5,3)=B$. Not monochromatic: has W and B. ✓. Checkerboard? $W, ? / W, B$. Top-left and bottom-left both W, so not checkerboard. ✓

$2 \times 2$ square at $(4, 3)$: cells $(4,3), (4,4), (5,3)=B, (5,4)=W$. Not monochromatic: has B and W. ✓. Checkerboard? $?, ? / B, W$. For checkerboard: $W, B / B, W$, so $(4,3) = W, (4,4) = B$.

$2 \times 2$ square at $(4, 4)$: cells $(4,4), (4,5)=W, (5,4)=W, (5,5)=W$. Not monochromatic: need at least one B. So $(4,4) = B$.

Now let me collect the constraints on $(3,3), (3,4), (4,3), (4,4)$:
- From $(2,2)$ checkerboard: $(3,3) = W$ (if it's checkerboard, but we want to avoid checkerboard, so this is only if we make it checkerboard).
- From $(2,3)$ checkerboard: $(3,3) = W, (3,4) = B$ (if checkerboard).
- From $(3,2)$ checkerboard: $(3,3) = W, (4,3) = B$ (if checkerboard).
- From $(3,4)$ checkerboard: $(3,4) = W, (4,4) = B$ (if checkerboard).
- From $(4,3)$ checkerboard: $(4,3) = W, (4,4) = B$ (if checkerboard).
- From $(4,4)$ not monochromatic: $(4,4) = B$ (forced).

So $(4,4) = B$.

Now, $2 \times 2$ square at $(3, 3)$: cells $(3,3), (3,4), (4,3), (4,4) = B$. Need not monochromatic.

Let me try to minimize checkerboard squares. Let me set $(3,3) = B, (3,4) = B, (4,3) = B, (4,4) = B$. Then square $(3,3)$: all B = monochromatic. Bad.

Try $(3,3) = B, (3,4) = W, (4,3) = W, (4,4) = B$. Square $(3,3)$: $B, W / W, B$ = checkerboard! That's in $S$.

Try $(3,3) = W, (3,4) = B, (4,3) = B, (4,4) = B$. Square $(3,3)$: $W, B / B, B$ = not monochromatic, not checkerboard. ✓

Now check other squares:
- $(2,2)$: $W, B / B, W$ = checkerboard! In $S$.
- $(2,3)$: $B, W / W, B$ = checkerboard! In $S$.
- $(3,2)$: $B, W / W, B$ = checkerboard! In $S$.
- $(3,4)$: $B, B / B, W$ = not mono, not checker. ✓
- $(4,3)$: $W, B / B, W$ = checkerboard! In $S$.

So $S = 4$ with this assignment. Can we do better?

Let me try $(3,3) = B, (3,4) = B, (4,3) = W, (4,4) = B$. Square $(3,3)$: $B, B / W, B$ = not mono, not checker. ✓

Check:
- $(2,2)$: $W, B / B, W$ = checkerboard! ($W,B/B,W$). In $S$.
- $(2,3)$: $B, B / B, B$... wait, $(3,4) = B$. $B, B / B, B$? No: $(2,3) = B, (2,4) = W, (3,3) = B, (3,4) = B$. So it's $B, W / B, B$. Not mono, not checker. ✓
- $(3,2)$: $B, B / W, W$... $(3,2) = B, (3,3) = B, (4,2) = W, (4,3) = W$. Pattern: $B, B / W, W$ = not mono, not checker. ✓
- $(3,4)$: $(3,4) = B, (3,5) = B, (4,4) = B, (4,5) = W$. Pattern: $B, B / B, W$ = not mono, not checker. ✓
- $(4,3)$: $(4,3) = W, (4,4) = B, (5,3) = B, (5,4) = W$. Pattern: $W, B / B, W$ = checkerboard! In $S$.

So $S = 2$ (squares $(2,2)$ and $(4,3)$). Can we do better?

Let me try $(3,3) = B, (3,4) = W, (4,3) = B, (4,4) = B$. Square $(3,3)$: $B, W / B, B$ = not mono, not checker. ✓

Check:
- $(2,2)$: $W, B / B, B$ = not mono, not checker. ✓
- $(2,3)$: $B, W / B, W$ = not mono, not checker. ✓ (Pattern: $B,W/B,W$ — this is vertical stripes, "other".)
- $(3,2)$: $B, B / W, B$ = not mono, not checker. ✓
- $(3,4)$: $W, B / B, W$ = checkerboard! In $S$.
- $(4,3)$: $B, B / B, W$ = not mono, not checker. ✓

So $S = 1$! Only square $(3,4)$ is checkerboard.

Can we achieve $S = 0$? Let me check all possibilities.

We need $(4,4) = B$ (forced). We need to choose $(3,3), (3,4), (4,3) \in \{B, W\}$ (8 possibilities) such that:
- Square $(3,3)$ not monochromatic: not all of $(3,3), (3,4), (4,3), B$ are equal. Since $(4,4) = B$, this means not all four are B, i.e., at least one of $(3,3), (3,4), (4,3)$ is W.
- No checkerboard squares among all 9 interior squares.

Let me enumerate. The interior $2 \times 2$ squares are at positions $(2,2), (2,3), (2,4), (3,2), (3,3), (3,4), (4,2), (4,3), (4,4)$.

The ones that could be checkerboard (involving the free variables) are:
- $(2,2)$: $W, B / B, (3,3)$. Checkerboard iff $(3,3) = W$ (pattern $W,B/B,W$).
- $(2,3)$: $B, W / (3,3), (3,4)$. Checkerboard iff $(3,3) = W, (3,4) = B$ (pattern $B,W/W,B$).
- $(2,4)$: $W, W / (3,4), B$. Top row $W,W$ not alternating, so never checkerboard. ✓
- $(3,2)$: $B, (3,3) / W, (4,3)$. Checkerboard iff $(3,3) = W, (4,3) = B$ (pattern $B,W/W,B$).
- $(3,3)$: $(3,3), (3,4) / (4,3), B$. Checkerboard iff $(3,3) = W, (3,4) = B, (4,3) = B$ (pattern $W,B/B,W$) — wait, $W,B/B,W$ means $(3,3)=W, (3,4)=B, (4,3)=B, (4,4)=W$. But $(4,4) = B \neq W$. So not checkerboard. Or $B,W/W,B$: $(3,3)=B, (3,4)=W, (4,3)=W, (4,4)=B$. Yes! So checkerboard iff $(3,3) = B, (3,4) = W, (4,3) = W$.
- $(3,4)$: $(3,4), B / (4,4), W$ = $(3,4), B / B, W$. Checkerboard iff $(3,4) = W$ (pattern $W,B/B,W$).
- $(4,2)$: $W, (4,3) / W, B$. Left column $W, W$ not alternating, never checkerboard. ✓
- $(4,3)$: $(4,3), B / B, W$. Checkerboard iff $(4,3) = W$ (pattern $W,B/B,W$).
- $(4,4)$: $B, W / W, W$. Not checkerboard (bottom row $W,W$). ✓

So checkerboard conditions:
- $(2,2)$: $(3,3) = W$
- $(2,3)$: $(3,3) = W \land (3,4) = B$
- $(3,2)$: $(3,3) = W \land (4,3) = B$
- $(3,3)$: $(3,3) = B \land (3,4) = W \land (4,3) = W$
- $(3,4)$: $(3,4) = W$
- $(4,3)$: $(4,3) = W$

We want none of these to hold. So:
- $(3,3) \neq W$ → $(3,3) = B$ (from $(2,2)$)
- $(3,4) \neq W$ → $(3,4) = B$ (from $(3,4)$)
- $(4,3) \neq W$ → $(4,3) = B$ (from $(4,3)$)

But then square $(3,3)$: $B, B / B, B$ = monochromatic! Violates the constraint.

So $S = 0$ is impossible for $n = 6$. The minimum is $S = 1$ (which we achieved).

Interesting! So for $n = 6$, the minimum is $S = 1$.

Let me check $n = 8$ to see if there's a pattern. Actually, this is getting very tedious by hand. Let me think about the structure more abstractly.

Let me think about what's happening. The boundary is all black. The "second ring" (row 2, row 99, col 2, col 99) is constrained. The key issue is a parity problem: the boundary forms a closed loop of black cells, and the alternation pattern can't be consistent around this loop.

Let me think about it in terms of the dual / $g$ function. Recall $g(i,j) = f(i,j) \oplus ((i+j) \mod 2)$. The boundary of $g$ is a checkerboard (since $f = 1$ on the boundary, $g = 1 \oplus (i+j \mod 2) = (i+j+1) \mod 2$).

We want: no checkerboard $2 \times 2$ in $g$ (no monochromatic in $f$), minimize monochromatic $2 \times 2$ in $g$ (minimize $S$).

A monochromatic $2 \times 2$ in $g$ means $g$ is constant on that square. No checkerboard $2 \times 2$ in $g$ means $g$ doesn't alternate on any square.

The boundary of $g$ alternates (checkerboard). Going around the boundary, the $g$ values alternate. The boundary is a closed loop of length $4(n-1) = 4 \times 99 = 396$. Since 396 is even, the alternation is consistent around the loop. So the boundary condition is consistent.

Now, $g$ on the boundary alternates. We want to extend $g$ to the interior such that:
1. No $2 \times 2$ square has $g$ in checkerboard pattern (i.e., no $2 \times 2$ square where $g$ alternates).
2. Minimize the number of $2 \times 2$ squares where $g$ is constant (monochromatic in $g$).

A $2 \times 2$ square where $g$ is constant means all four $g$ values are the same. A $2 \times 2$ square where $g$ alternates (checkerboard) means $g(i,j) \neq g(i,j+1)$, $g(i,j) \neq g(i+1,j)$, etc.

The "other" case for $g$ is when the $2 \times 2$ square has two adjacent cells with the same $g$ value and the other two with the other value, but not in alternating pattern.

Hmm, this dual perspective might be more natural. Let me think about it.

In the dual, the boundary alternates. We want to fill the interior to avoid alternating $2 \times 2$ squares and minimize constant $2 \times 2$ squares.

A constant $2 \times 2$ square in $g$ is a "monochromatic" region. An alternating $2 \times 2$ square is a "checkerboard" region. We want to avoid checkerboard regions and minimize monochromatic regions.

If $g$ were constant everywhere, there would be no checkerboard squares but many monochromatic squares. But the boundary alternates, so $g$ can't be constant everywhere.

If $g$ alternates everywhere (checkerboard), there would be no monochromatic squares but all squares would be checkerboard. But we want to avoid checkerboard squares.

So we want $g$ to be "mostly constant" with transitions only where needed to accommodate the alternating boundary.

Think of $g$ as a binary image. The boundary alternates. We want to extend it inward, keeping $g$ as constant as possible (to minimize checkerboard squares in $g$, which are monochromatic in $f$... wait, I'm getting confused).

Let me re-clarify:
- $S$ = number of checkerboard $2 \times 2$ in $f$ = number of monochromatic (constant) $2 \times 2$ in $g$.
- Constraint: no monochromatic $2 \times 2$ in $f$ = no checkerboard (alternating) $2 \times 2$ in $g$.
- We want to minimize $S$ = minimize constant $2 \times 2$ in $g$.
- Subject to: no alternating $2 \times 2$ in $g$, and $g$ has alternating boundary.

So in the dual, we want to minimize the number of constant $2 \times 2$ squares, subject to no alternating $2 \times 2$ squares, with an alternating boundary.

A constant $2 \times 2$ square in $g$ means $g$ doesn't change across that square. An alternating $2 \times 2$ means $g$ changes in both directions.

To avoid alternating $2 \times 2$ squares: for every $2 \times 2$ square, $g$ must not alternate. This means for every $2 \times 2$ square, either $g$ is constant, or $g$ changes in only one direction (horizontal or vertical stripes), or $g$ has an L-shape.

To minimize constant $2 \times 2$ squares: we want $g$ to change as much as possible, but only in one direction at a time per square.

Hmm, this is still complex. Let me think about it differently.

Let me consider the "transition" variables for $g$. Define $h'_ {i,j} = g(i,j) \oplus g(i,j+1)$ and $v'_{i,j} = g(i,j) \oplus g(i+1,j)$.

A $2 \times 2$ square in $g$ is:
- Constant: $h'_{i,j} = h'_{i+1,j} = v'_{i,j} = v'_{i,j+1} = 0$.
- Alternating (checkerboard): all four = 1.
- Other: mixed.

We want: no square with all four transitions = 1 (no alternating), minimize squares with all four = 0 (minimize constant).

The boundary of $g$ alternates. On the top row (row 1), $g(1, j) = (1 + j + 1) \mod 2 = (j + 2) \mod 2 = j \mod 2$. So $g(1, j)$ alternates: $g(1, 1) = 1, g(1, 2) = 0, g(1, 3) = 1, \ldots$. So $h'_{1,j} = 1$ for all $j$ (top row alternates).

Similarly, bottom row (row $n$): $g(n, j) = (n + j + 1) \mod 2$. With $n = 100$: $g(100, j) = (101 + j) \mod 2 = (j + 1) \mod 2$. So $g(100, 1) = 0, g(100, 2) = 1, \ldots$. $h'_{100, j} = 1$ for all $j$.

Left column (col 1): $g(i, 1) = (i + 2) \mod 2$. $g(1, 1) = 1, g(2, 1) = 0, g(3, 1) = 1, \ldots$. $v'_{i, 1} = 1$ for all $i$.

Right column (col $n$): $g(i, 100) = (i + 101) \mod 2 = (i + 1) \mod 2$. $g(1, 100) = 0, g(2, 100) = 1, \ldots$. $v'_{i, 100} = 1$ for all $i$.

So in the dual, the boundary transitions are all 1 (the boundary alternates in both directions). This is the opposite of the original problem where boundary transitions were all 0.

Now, the $2 \times 2$ squares on the boundary (touching the edge) have at least one transition = 1 (from the boundary). So they can't be constant (all 0). They could be alternating (all 1) or "other". We need them to not be alternating. 

For a $2 \times 2$ square at position $(1, j)$ (top row): $h'_{1,j} = 1$ (boundary). For not alternating, we need at least one of $h'_{2,j}, v'_{1,j}, v'_{1,j+1}$ to be 0.

For a $2 \times 2$ square at position $(i, 1)$ (left column): $v'_{i,1} = 1$ (boundary). For not alternating, need at least one of $h'_{i,1}, h'_{i+1,1}, v'_{i,2}$ to be 0.

And so on for all boundary-adjacent squares.

For the corner $2 \times 2$ square at $(1, 1)$: $h'_{1,1} = 1, v'_{1,1} = 1$. For not alternating, need at least one of $h'_{2,1}, v'_{1,2}$ to be 0.

OK, this dual perspective is interesting but I'm not sure it's simpler. Let me go back to the original formulation and think about lower bounds.

Let me think about the problem in terms of the original $f$ (black/white coloring with black boundary).

Key observation: The boundary is all black. The $2 \times 2$ squares touching the boundary can't be checkerboard (as shown). So $S$ only counts interior $2 \times 2$ squares (positions $2 \leq i \leq 98, 2 \leq j \leq 98$).

For the interior, we need to color the $98 \times 98$ interior (rows 2-99, cols 2-99) such that:
1. No $2 \times 2$ square (anywhere on the board) is monochromatic.
2. Minimize the number of checkerboard $2 \times 2$ squares among interior positions.

The constraints from the boundary affect the second ring (row 2, row 99, col 2, col 99) as we discussed.

Let me think about a lower bound on $S$.

Consider the "second ring" cells. Row 2 has no two consecutive black cells (from row 1 being all black). Row 99 has no two consecutive black cells (from row 100 being all black). Column 2 has no two consecutive black cells. Column 99 has no two consecutive black cells.

Now, consider the $2 \times 2$ squares at position $(2, j)$ for $j = 2, \ldots, 98$. These involve rows 2-3, columns $j, j+1$. The cells in row 2 have no two consecutive blacks. 

Hmm, I think I need a different approach. Let me think about the problem in terms of a "parity" or "index" argument.

Consider the second ring: the cells at positions $(i, j)$ where $\min(i, j, 101-i, 101-j) = 2$, i.e., row 2, row 99, column 2, column 99 (excluding corners which are counted once).

Actually, let me think about the problem in a more structured way. Let me consider the "defect" that must occur due to the parity mismatch.

In the original problem, the boundary is all black (all transitions 0 on the boundary). We need no monochromatic $2 \times 2$ (no all-zero transition squares). We want to minimize checkerboard $2 \times 2$ (all-one transition squares).

The transitions form a grid. Let me think about the horizontal transitions $h_{i,j}$ for $i = 1, \ldots, 100$ and $j = 1, \ldots, 99$, and vertical transitions $v_{i,j}$ for $i = 1, \ldots, 99$ and $j = 1, \ldots, 100$.

Boundary: $h_{1,j} = 0, h_{100,j} = 0, v_{i,1} = 0, v_{i,100} = 0$.

Parity constraint: $h_{i,j} \oplus h_{i+1,j} \oplus v_{i,j} \oplus v_{i,j+1} = 0$ for $i = 1, \ldots, 99, j = 1, \ldots, 99$.

No monochromatic: for each $(i,j)$, not all of $h_{i,j}, h_{i+1,j}, v_{i,j}, v_{i,j+1}$ are 0.

Minimize: number of $(i,j)$ where all of $h_{i,j}, h_{i+1,j}, v_{i,j}, v_{i,j+1}$ are 1.

Now, from the parity constraint, $h_{i,j} \oplus h_{i+1,j} = v_{i,j} \oplus v_{i,j+1}$. So the "horizontal parity" equals the "vertical parity" at each square.

Let me define $p_{i,j} = h_{i,j} \oplus h_{i+1,j} = v_{i,j} \oplus v_{i,j+1}$ for each $2 \times 2$ square at $(i,j)$.

If $p_{i,j} = 0$: either both horizontal transitions are equal and both vertical transitions are equal. Sub-cases:
- $h_{i,j} = h_{i+1,j} = 0, v_{i,j} = v_{i,j+1} = 0$: monochromatic (forbidden).
- $h_{i,j} = h_{i+1,j} = 1, v_{i,j} = v_{i,j+1} = 1$: checkerboard (counted in $S$).
- $h_{i,j} = h_{i+1,j} = 0, v_{i,j} = v_{i,j+1} = 1$: vertical stripes ("other").
- $h_{i,j} = h_{i+1,j} = 1, v_{i,j} = v_{i,j+1} = 0$: horizontal stripes ("other").

If $p_{i,j} = 1$: the horizontal transitions differ and the vertical transitions differ. Sub-cases:
- $h_{i,j} = 1, h_{i+1,j} = 0, v_{i,j} = 1, v_{i,j+1} = 0$: "other".
- $h_{i,j} = 1, h_{i+1,j} = 0, v_{i,j} = 0, v_{i,j+1} = 1$: "other".
- $h_{i,j} = 0, h_{i+1,j} = 1, v_{i,j} = 1, v_{i,j+1} = 0$: "other".
- $h_{i,j} = 0, h_{i+1,j} = 1, v_{i,j} = 0, v_{i,j+1} = 1$: "other".

So when $p_{i,j} = 1$, the square is always "other" (never monochromatic or checkerboard). When $p_{i,j} = 0$, the square is either monochromatic (forbidden), checkerboard (in $S$), or stripes ("other").

So to minimize $S$, we want to maximize the number of squares with $p_{i,j} = 1$ (these are always "other" and safe), and among the $p_{i,j} = 0$ squares, we want them to be stripes rather than checkerboard (and never monochromatic).

But the $p_{i,j}$ values are determined by the transitions, which are determined by the coloring. Let me think about what constraints the $p_{i,j}$ satisfy.

$p_{i,j} = h_{i,j} \oplus h_{i+1,j}$. So $p$ is like a "vertical difference" of the horizontal transition field $h$. Similarly, $p_{i,j} = v_{i,j} \oplus v_{i,j+1}$, a "horizontal difference" of the vertical transition field $v$.

The $h$ field is a $100 \times 99$ binary matrix, and $v$ is a $99 \times 100$ binary matrix, related by the parity constraints.

Hmm, this is getting complicated. Let me try a different approach: think about the problem as a kind of "Ising model" or "tiling" problem.

Let me consider the approach of using "stripes" — either horizontal or vertical stripes — in the interior, with some "defects" to handle the parity issue.

Construction idea: Use horizontal stripes (uniform rows) for most of the board, with alternating black and white rows, but handle the parity issue at one end.

For $n = 100$:
- Rows 1 to 99: alternate B, W, B, W, ..., B (row 99 is B since 99 is odd).
- Row 100: B (boundary).

But rows 99 and 100 are both B → monochromatic $2 \times 2$ squares. Bad.

Alternative: 
- Rows 1 to 98: alternate B, W, B, W, ..., W (row 98 is W since 98 is even).
- Row 99: non-uniform (must differ from row 98 = all W and row 100 = all B).
- Row 100: B.

Row 99 must have no two consecutive W (from row 98 = all W) and no two consecutive B (from row 100 = all B). So row 99 must strictly alternate. But $(99, 1) = B$ and $(99, 100) = B$ (boundary), and strict alternation from B gives $(99, 100) = W$ (since 100 is even). Contradiction.

So we can't have just one non-uniform row. We need at least two.

Let me try:
- Rows 1 to 97: alternate B, W, B, W, ..., B (row 97 is B since 97 is odd).
- Row 98: non-uniform.
- Row 99: non-uniform.
- Row 100: B.

Row 98 must differ from row 97 = all B (no two consecutive B in row 98) and from row 99 (whatever that is).

Row 99 must differ from row 98 and from row 100 = all B (no two consecutive B in row 99).

This is getting complicated. Let me think about it differently.

What if we use a "checkerboard-like" pattern in a small region and stripes elsewhere?

Actually, let me think about the problem from the perspective of the dual $g$ function, which might be cleaner.

In the dual, the boundary alternates (all boundary transitions are 1). We want no alternating $2 \times 2$ squares in $g$ (no all-1 transition squares) and minimize constant $2 \times 2$ squares (all-0 transition squares).

The boundary transitions are all 1. The $2 \times 2$ squares on the boundary have at least one transition = 1, so they can't be constant. They must be "other" (not all-1, since we forbid alternating). So we need at least one non-boundary transition to be 0 in each boundary square.

For the corner square at $(1,1)$: $h'_{1,1} = 1, v'_{1,1} = 1$. Need at least one of $h'_{2,1}, v'_{1,2}$ to be 0.

For the top edge square at $(1, j)$ (for $j = 2, \ldots, 98$): $h'_{1,j} = 1$. Need at least one of $h'_{2,j}, v'_{1,j}, v'_{1,j+1}$ to be 0. But $v'_{1,j} = g(1,j) \oplus g(2,j)$. On the top row, $g(1,j) = j \mod 2$. So $v'_{1,j} = (j \mod 2) \oplus g(2,j)$.

Hmm, this is still complex. Let me try to think about the problem more cleverly.

Let me consider the following approach: think of the coloring as a function on the grid, and consider "paths" from one side of the board to the other.

Actually, let me think about a key structural observation.

Consider the $2 \times 2$ squares in the first row of squares (positions $(1, j)$ for $j = 1, \ldots, 99$). These all have $h_{1,j} = 0$ (row 1 all black). For not monochromatic, we need at least one transition to be 1. Since $h_{1,j} = 0$, we need at least one of $h_{2,j}, v_{1,j}, v_{1,j+1}$ to be 1. But $v_{1,j} = f(1,j) \oplus f(2,j) = 1 \oplus f(2,j) = \neg f(2,j)$ (since $f(1,j) = 1$). So $v_{1,j} = 1$ iff $f(2,j) = 0$ (white).

So the condition is: for each $j$, at least one of $h_{2,j}, v_{1,j}, v_{1,j+1}$ is 1, i.e., at least one of:
- $f(2,j) \neq f(2,j+1)$ (i.e., $h_{2,j} = 1$), or
- $f(2,j) = 0$ (i.e., $v_{1,j} = 1$), or
- $f(2,j+1) = 0$ (i.e., $v_{1,j+1} = 1$).

This is equivalent to: not both $f(2,j) = 1$ and $f(2,j+1) = 1$, i.e., no two consecutive blacks in row 2. (As we already knew.)

Now, here's a key insight. Consider the second ring as a "cycle" going around the board: row 2 (left to right), then column 99 (top to bottom), then row 99 (right to left), then column 2 (bottom to top). This forms a cycle of length $4 \times 97 = 388$ (excluding the four corner cells which are shared).

Wait, let me be more careful. The second ring consists of:
- Row 2: columns 2 to 99 (98 cells, but corners $(2,2)$ and $(2,99)$ are shared with columns).
- Column 99: rows 2 to 99 (98 cells, corners $(2,99)$ and $(99,99)$ shared).
- Row 99: columns 99 to 2 (98 cells, corners $(99,99)$ and $(99,2)$ shared).
- Column 2: rows 99 to 2 (98 cells, corners $(99,2)$ and $(2,2)$ shared).

Total unique cells: $4 \times 98 - 4 = 388$ (subtracting 4 corners counted twice). Actually, $4 \times 98 - 4 = 388$. Hmm, $4 \times 98 = 392$, minus 4 = 388. Yes.

The constraints on the second ring:
- Row 2 (cols 2-99): no two consecutive blacks. Plus $(2,2) = W$ and $(2,99) = W$ (from corner constraints).
- Row 99 (cols 2-99): no two consecutive blacks. Plus $(99,2) = W$ and $(99,99) = W$.
- Column 2 (rows 2-99): no two consecutive blacks. Plus $(2,2) = W$ and $(99,2) = W$.
- Column 99 (rows 2-99): no two consecutive blacks. Plus $(2,99) = W$ and $(99,99) = W$.

Now, the second ring forms a cycle. On this cycle, no two consecutive cells are both black. The corners are all white. 

Let me think about the cycle more carefully. Going around the cycle:
- Start at $(2,2) = W$, go right along row 2 to $(2,99) = W$ (98 cells).
- Go down along column 99 to $(99,99) = W$ (98 cells, but $(2,99)$ already counted, so 97 new cells).
- Go left along row 99 to $(99,2) = W$ (98 cells, but $(99,99)$ already counted, so 97 new cells).
- Go up along column 2 to $(2,2) = W$ (98 cells, but $(99,2)$ and $(2,2)$ already counted, so 96 new cells).

Total: $98 + 97 + 97 + 96 = 388$ cells. ✓

On this cycle, no two consecutive cells (in the cycle order) are both black. The four corners are white.

Now, here's the key question: what does this imply about the interior?

Actually, I think the key insight is about the "checkerboard" $2 \times 2$ squares that are forced to exist.

Let me think about this differently. Let me consider the "interior" as a separate problem. The interior is the $98 \times 98$ grid (rows 2-99, cols 2-99), with boundary conditions on its boundary (the second ring).

The boundary of the interior (second ring) has specific constraints: no two consecutive blacks on each side, corners are white.

Now, within the interior, we need no monochromatic $2 \times 2$ and minimize checkerboard $2 \times 2$.

Hmm, but the interior's boundary conditions are complex. Let me think about a simpler model.

Actually, let me try to think about the problem in terms of "defect lines" or "domain walls."

In the dual picture ($g$ function), the boundary alternates. We want to extend $g$ to the interior with no alternating $2 \times 2$ squares and minimize constant $2 \times 2$ squares.

Think of $g$ as a binary image. The boundary alternates (like a checkerboard on the boundary). We want to "fill in" the interior.

If we extend the checkerboard pattern to the interior, every $2 \times 2$ square is alternating — but that's forbidden. So we need to "break" the checkerboard pattern.

If we make $g$ constant in large regions, we get many constant $2 \times 2$ squares (which contribute to $S$). We want to minimize these.

The optimal strategy might be to have $g$ change in only one direction (say, only horizontally or only vertically) in most of the interior, with a small "defect" region where the direction of change switches.

Let me think about this. If $g$ changes only horizontally (i.e., $g(i,j)$ depends only on $j$), then $v'_{i,j} = 0$ for all $i, j$ (no vertical transitions). Each $2 \times 2$ square has $v'_{i,j} = v'_{i,j+1} = 0$, so it's constant if $h'_{i,j} = h'_{i+1,j} = 0$, or horizontal stripes if $h'_{i,j} = h'_{i+1,j} = 1$, or "other" if $h'_{i,j} \neq h'_{i+1,j}$.

But if $g$ depends only on $j$, then $h'_{i,j} = g(j) \oplus g(j+1) = h'_{i+1,j}$, so $h'_{i,j} = h'_{i+1,j}$ for all $i$. So each square is either constant ($h' = 0$) or horizontal stripes ($h' = 1$). No alternating squares (good, since $v' = 0$). The constant squares are those where $g(j) = g(j+1)$.

On the boundary, $g$ alternates: $g(1, j) = j \mod 2$. If $g$ depends only on $j$, then $g(i, j) = j \mod 2$ for all $i$. But then $g(j) \neq g(j+1)$ for all $j$, so $h' = 1$ everywhere, and every square is horizontal stripes. No constant squares! So $S = 0$?

Wait, but we also need the boundary conditions on the left and right columns. $g(i, 1) = (i + 2) \mod 2$ and $g(i, 100) = (i + 1) \mod 2$. If $g$ depends only on $j$, then $g(i, 1) = g(1) = 1 \mod 2 = 1$ for all $i$, but the boundary requires $g(i, 1) = (i+2) \mod 2$ which alternates. Contradiction!

So $g$ can't depend only on $j$ (or only on $i$) while satisfying all boundary conditions. The boundary alternates in both directions, so $g$ must change in both directions.

This is the crux of the problem. The boundary forces $g$ to alternate in both horizontal and vertical directions, but we want to avoid having both directions alternate simultaneously in any $2 \times 2$ square (which would be an alternating/checkerboard square in $g$, forbidden).

So we need to "separate" the horizontal and vertical alternation: in most of the board, $g$ alternates in only one direction. But at some point, the direction must switch, and this switch creates "defects" (constant $2 \times 2$ squares, which contribute to $S$).

This is reminiscent of a "domain wall" or "vortex" problem. The boundary conditions create a "topological obstruction" that forces at least one defect.

Let me formalize this. Consider the horizontal transitions $h'_{i,j}$ and vertical transitions $v'_{i,j}$ in the dual. The boundary has $h'_{1,j} = h'_{100,j} = 1$ and $v'_{i,1} = v'_{i,100} = 1$.

We want: for each $2 \times 2$ square, not all four transitions are 1 (no alternating square). Minimize: number of squares where all four transitions are 0 (constant squares).

Since the boundary transitions are all 1, the "alternating" pattern is forced near the boundary. We need to "extinguish" some transitions to 0 to avoid alternating squares.

For a $2 \times 2$ square at $(1, j)$: $h'_{1,j} = 1$. To avoid alternating, need at least one of $h'_{2,j}, v'_{1,j}, v'_{1,j+1}$ to be 0.

For a $2 \times 2$ square at $(i, 1)$: $v'_{i,1} = 1$. To avoid alternating, need at least one of $h'_{i,1}, h'_{i+1,1}, v'_{i,2}$ to be 0.

For the corner square at $(1, 1)$: $h'_{1,1} = 1, v'_{1,1} = 1$. Need at least one of $h'_{2,1}, v'_{1,2}$ to be 0.

Similarly for all four corners.

Now, here's the key topological argument. Consider the "transition field" $(h', v')$ on the grid. The boundary conditions force $h' = 1$ on the top and bottom edges, and $v' = 1$ on the left and right edges.

We want to assign $h'$ and $v'$ in the interior such that:
1. Parity constraint: $h'_{i,j} \oplus h'_{i+1,j} \oplus v'_{i,j} \oplus v'_{i,j+1} = 0$ (this is automatically satisfied since $h'$ and $v'$ come from a real function $g$).
2. No square has all four transitions = 1.
3. Minimize squares with all four transitions = 0.

Actually, the parity constraint is automatically satisfied if $h'$ and $v'$ come from a real $g$. But if we're designing $g$, we need to ensure consistency.

Let me think about this as follows. We want to design $g$ on the $100 \times 100$ grid with alternating boundary, such that no $2 \times 2$ square is alternating, and we minimize constant $2 \times 2$ squares.

Consider the "type" of each $2 \times 2$ square:
- If $h'_{i,j} = 1, h'_{i+1,j} = 1, v'_{i,j} = 1, v'_{i,j+1} = 1$: alternating (forbidden).
- If $h'_{i,j} = 0, h'_{i+1,j} = 0, v'_{i,j} = 0, v'_{i,j+1} = 0$: constant (contributes to $S$).
- Otherwise: "other" (safe).

We want to avoid the first and minimize the second.

Now, think of the transitions as a "flow." The horizontal transitions $h'_{i,j}$ form horizontal "edges" and vertical transitions $v'_{i,j}$ form vertical "edges." A transition of 1 means a "change" across that edge.

The boundary has changes on all four sides. We want to "propagate" these changes inward but avoid having both horizontal and vertical changes in the same square.

One approach: propagate the horizontal changes (from top/bottom) inward, and propagate the vertical changes (from left/right) inward, but keep them in separate regions.

For example:
- In the left part of the board, propagate vertical changes (from left/right boundary) — $g$ alternates vertically.
- In the right part of the board, propagate horizontal changes (from top/bottom boundary) — $g$ alternates horizontally.
- At the boundary between these regions, there's a "defect" where constant squares appear.

But we need to be more precise. Let me think about a specific construction.

Construction: Divide the board into two regions by a vertical line at column $k$. 
- Left region (columns 1 to $k$): $g$ alternates vertically, i.e., $g(i, j) = (i + c_j) \mod 2$ for some constants $c_j$ depending on $j$. This means $h'_{i,j} = 0$ (no horizontal changes) and $v'_{i,j} = 1$ (vertical changes). Each $2 \times 2$ square in this region has $h' = 0, v' = 1$, so it's "vertical stripes" — safe.
- Right region (columns $k+1$ to 100): $g$ alternates horizontally, i.e., $g(i, j) = (j + r_i) \mod 2$ for some constants $r_i$. This means $v'_{i,j} = 0$ and $h'_{i,j} = 1$. Each $2 \times 2$ square is "horizontal stripes" — safe.
- At the boundary (column $k$ to $k+1$), there's a transition where both $h'$ and $v'$ might be nonzero, creating potential issues.

But we need to satisfy the boundary conditions. On the top edge, $g(1, j) = j \mod 2$. In the left region, $g(1, j) = (1 + c_j) \mod 2 = j \mod 2$, so $c_j = (j - 1) \mod 2$. In the right region, $g(1, j) = (j + r_1) \mod 2 = j \mod 2$, so $r_1 = 0$.

On the left edge, $g(i, 1) = (i + 2) \mod 2$. In the left region, $g(i, 1) = (i + c_1) \mod 2 = (i + 2) \mod 2$, so $c_1 = 2 \mod 2 = 0$. But from the top edge, $c_1 = (1 - 1) \mod 2 = 0$. ✓

On the right edge, $g(i, 100) = (i + 1) \mod 2$. In the right region, $g(i, 100) = (100 + r_i) \mod 2 = r_i \mod 2$ (since 100 is even). So $r_i = (i + 1) \mod 2$. 

On the bottom edge, $g(100, j) = (j + 1) \mod 2$. In the right region, $g(100, j) = (j + r_{100}) \mod 2 = (j + 1) \mod 2$, so $r_{100} = 1 \mod 2 = 1$. From the right edge, $r_{100} = (100 + 1) \mod 2 = 1$. ✓

In the left region, on the bottom edge: $g(100, j) = (100 + c_j) \mod 2 = c_j \mod 2$. This should equal $(j + 1) \mod 2$. So $c_j = (j + 1) \mod 2$. But from the top edge, $c_j = (j - 1) \mod 2$. So $(j+1) \mod 2 = (j-1) \mod 2$, which is true since $(j+1) - (j-1) = 2$. ✓ Great, so the left region is consistent.

In the right region, on the top edge: $g(1, j) = (j + r_1) \mod 2 = j \mod 2$. So $r_1 = 0$. From the right edge, $r_1 = (1 + 1) \mod 2 = 0$. ✓

So the left region has $g(i, j) = (i + c_j) \mod 2$ where $c_j = (j+1) \mod 2$ (or equivalently $(j-1) \mod 2$). So $g(i, j) = (i + j + 1) \mod 2$ in the left region. Wait, that's just the standard checkerboard! $g(i,j) = (i + j + 1) \mod 2 = (i + j - 1) \mod 2$. Hmm, but I said the left region has $h' = 0$ (no horizontal changes). Let me check: $h'_{i,j} = g(i,j) \oplus g(i,j+1) = (i + j + 1) \oplus (i + j + 2) \mod 2 = 1$. That's not 0!

I think I made an error. If $g(i, j) = (i + c_j) \mod 2$, then $h'_{i,j} = (i + c_j)
