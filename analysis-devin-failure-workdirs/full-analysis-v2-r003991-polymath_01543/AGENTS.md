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
  <problem_id>polymath_01543</problem_id>
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

Let $n > 1$ be a positive integer. Each unit square in an $n \times n$ grid of squares is colored either black or white, such that:
- Any two black squares can be connected by a sequence of black squares where every two consecutive squares in the sequence share an edge;
- Any two white squares can be connected by a sequence of white squares where every two consecutive squares in the sequence share an edge;
- Any $2 \times 2$ subgrid contains at least one square of each color.

Let $f(n)$ be the maximum possible value of $|B - W|$, where $B$ is the number of black squares and $W$ is the number of white squares. Find $f(10) + f(11)$.

## Standard Solution

From the original solution, the maximum possible difference between the number of black squares and white squares is $2n+1$ if $n$ is odd, and $2n-2$ if $n$ is even.
For $n=10$ (even), $f(10) = 2(10) - 2 = 18$.
For $n=11$ (odd), $f(11) = 2(11) + 1 = 23$.
Thus, $f(10) + f(11) = 18 + 23 = 41$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have an $n \times n$ grid where each square is black or white. Conditions:
1. Black squares form a connected region (edge-connected).
2. White squares form a connected region.
3. Every $2 \times 2$ subgrid contains at least one square of each color (i.e., no $2 \times 2$ subgrid is monochromatic).

We want to maximize $|B - W|$ where $B$ = number of black, $W$ = number of white.

Let me think about what configurations satisfy these constraints.

First, condition 3 means no $2 \times 2$ block is all the same color. This is a constraint on the coloring.

Condition 1 and 2 require both colors to be connected (edge-connected).

Let me think about small cases and patterns.

A classic pattern: color the grid in a "staircase" or "diagonal" pattern. 

Actually, let me think about what kind of connected colorings avoid monochromatic $2 \times 2$ blocks.

One natural pattern: color row $i$ based on some rule. But if we color entire rows, we need to be careful about $2 \times 2$ blocks.

Consider a "staircase" pattern where we color the grid so that black forms a connected region that's like a thick diagonal band.

Let me think about this differently. The constraint that every $2 \times 2$ has both colors means the coloring has no $2 \times 2$ monochromatic block. This is related to the concept that the coloring is "2D-avoiding" of monochromatic squares.

Let me think about a specific construction. Consider coloring the grid like a "staircase":
- In row $i$ (0-indexed), color columns $0, 1, \ldots, k_i$ black and the rest white, where $k_i$ varies.

For black to be connected and white to be connected, and no $2 \times 2$ monochromatic block...

Actually, let me think about the "staircase" where black is the region below a monotone path.

Consider a path from the top-left to bottom-right that goes right and down. Black = cells on one side, white = cells on the other side. 

Actually, let me think about a simpler construction. Consider the coloring where we have a "staircase" boundary:

Row 0: all black except... no wait.

Let me think about the checkerboard-like patterns but those have $B = W$ roughly.

Let me think about what maximizes $|B-W|$. We want one color to dominate. Say black dominates. We want as many black as possible while:
- White is connected
- Black is connected  
- No $2 \times 2$ is monochromatic

If black dominates, white must be a connected set, and every $2 \times 2$ must contain at least one white square. So white must "hit" every $2 \times 2$ subgrid. Also white must be connected.

The minimum number of white squares such that every $2 \times 2$ subgrid contains at least one white square, AND white is connected, AND black is connected.

Every $2 \times 2$ subgrid must contain a white square. There are $(n-1)^2$ such subgrids. A single white square can cover up to 4 subgrids (if it's in the interior). 

To hit every $2 \times 2$ subgrid with minimum cells, we could use a pattern like placing white squares on every other cell in a checkerboard on the interior... but we also need white to be connected.

Hmm, let me think about specific constructions.

**Construction 1: Single row of white.**
If we make one entire row white and the rest black. Then:
- White is connected (it's a full row). ✓
- Black is connected (rows above and below the white row are connected through columns... wait, if row $k$ is all white, then rows $0..k-1$ are black and rows $k+1..n-1$ are black. These two black regions are separated by the white row, so they're NOT connected unless $k=0$ or $k=n-1$.

If $k=0$ (top row white, rest black): White is the top row (connected ✓). Black is rows $1..n-1$ (connected ✓). Every $2 \times 2$ subgrid: the ones in rows $0-1$ contain a white (from row 0). The ones entirely in rows $1..n-1$ are all black! So this fails condition 3 for $n > 2$.

So a single row doesn't work for large $n$.

**Construction 2: Staircase.**
Let me think about a staircase pattern. Consider the coloring where cell $(i,j)$ is white if $i + j < n$ and black if $i + j \geq n$ (or some variant). This creates a diagonal boundary.

Wait, but this might create $2 \times 2$ monochromatic blocks away from the boundary.

Actually, the diagonal boundary only helps near the diagonal. Away from it, large regions are monochromatic, creating $2 \times 2$ monochromatic blocks.

So we need the white squares to be spread out enough to hit every $2 \times 2$ block, but also connected.

**Key insight:** White must hit every $2 \times 2$ subgrid. This means in every pair of consecutive rows, and every pair of consecutive columns, there's at least one white cell. 

Equivalently, there's no $2 \times 2$ all-black block. This means the black region has no $2 \times 2$ solid block.

Let me think about this as: the white cells form a "hitting set" for all $2 \times 2$ subgrids, and must be connected, and the complement (black) must also be connected.

**Construction: "Snake" of white cells.**
A connected path of white cells that hits every $2 \times 2$ subgrid. 

Consider a zigzag/snake pattern. For example, in even rows, place white cells at even columns; in odd rows, place white cells at odd columns. This is like a checkerboard but shifted. Wait, that's just a checkerboard, which has $B = W$ (or off by 1).

Hmm, but a checkerboard hits every $2 \times 2$ (each has 2 black, 2 white). But $|B-W| \leq 1$.

We want to minimize white (to maximize black) while keeping white connected and hitting every $2 \times 2$.

**Better construction: "L-shaped" or comb pattern.**

Let me think about a pattern where white forms a "comb" - a horizontal backbone with vertical teeth.

Consider: white cells form a path that snakes through the grid hitting every $2 \times 2$.

Actually, let me think about it more carefully. The condition "every $2 \times 2$ contains a white cell" is equivalent to saying: the white cells form a dominating set for $2 \times 2$ blocks.

One efficient way: place white cells in a "staircase" that goes through the grid. 

Let me think about a specific pattern for even $n$:

Consider white cells at positions where $i$ is even and $j$ is anything... no, that's too many.

Let me think about the "zigzag column" approach. 

Actually, let me think about what patterns give connected white, connected black, and no $2 \times 2$ monochromatic.

**Pattern: Two interleaved staircases.**

Let me try a concrete small example. For $n = 3$:

```
B W B
W W W
B W B
```
Here $B = 4, W = 5$. White is connected (the plus shape). Black: the four corners. Are the four corners connected? $(0,0)$ and $(0,2)$ are not edge-adjacent (they're separated by $(0,1)$ which is white). So black is NOT connected. Fails.

```
B B W
B W W
W W W
```
$B = 3, W = 6$. White is connected. Black: $(0,0), (0,1), (1,0)$ - connected ✓. $2 \times 2$ blocks: top-left has 3B+1W ✓, top-right has 1B+3W ✓, bottom-left has 1B+3W ✓, bottom-right has 0B+4W ✗. Fails.

```
B B W
B W B
W B B
```
$B = 5, W = 4$. Black: $(0,0),(0,1),(1,0),(1,2),(2,1),(2,2)$. Is black connected? $(0,0)-(0,1)$ ✓, $(0,0)-(1,0)$ ✓, $(1,0)-(1,2)$? Not adjacent. $(1,2)-(2,2)$ ✓, $(2,2)-(2,1)$ ✓. But $(1,0)$ and $(1,2)$ are not connected through black. $(0,1)$ and $(2,1)$? $(0,1)-(1,1)$ is white. So we have two components: $\{(0,0),(0,1),(1,0)\}$ and $\{(1,2),(2,1),(2,2)\}$. Not connected. Fails.

Let me try:
```
B W B
B W B
B B B
```
$B = 6, W = 3$. White: $(0,1),(1,1),(2,1)$... wait, $(2,1)$ is B. Let me redo.
$B = 7, W = 2$. White: $(0,1),(1,1)$. Not connected to cover all $2 \times 2$. Bottom $2 \times 2$ blocks are all black. Fails.

This is getting complicated. Let me think more systematically.

**The "staircase band" construction.**

Consider a path from the left side to the right side (or top to bottom) that's one cell wide, and color it white, everything else black. For this to work:
- White (the path) must be connected ✓ (it's a path)
- Black must be connected: the path must not separate the grid into two disconnected parts. A path from top to bottom separates left from right. A path from left to right separates top from bottom. So a path that doesn't go from one side to the opposite side would keep black connected.
- Every $2 \times 2$ must contain a white cell: the path must hit every $2 \times 2$ subgrid.

But a one-cell-wide path that hits every $2 \times 2$ subgrid... that seems hard. A $2 \times 2$ subgrid in the corner far from the path wouldn't be hit.

So a single thin path won't work. We need white to be more spread out.

**Reformulation:** We need a connected set $W$ such that:
1. $W$ hits every $2 \times 2$ subgrid.
2. The complement $B$ is connected.
3. $|W|$ is minimized (to maximize $|B - W| = n^2 - 2|W|$).

Or symmetrically, maximize $|B-W|$ by making one color as large as possible.

**Lower bound on $|W|$:** Every $2 \times 2$ subgrid must contain a white cell. There are $(n-1)^2$ subgrids. Each white cell is in at most 4 subgrids. So $|W| \geq \lceil (n-1)^2 / 4 \rceil$. But we also need connectivity, which likely requires more.

Hmm wait, but we also need $B$ to be connected. If $W$ is too spread out, $B$ might become disconnected.

Let me think about a "comb" pattern:
- One full column of white (say column 0), plus horizontal "teeth" extending from it.

Actually, let me think about the following pattern for the grid. Consider a "staircase" that goes from top-left to bottom-right, but it's a thick staircase.

**Pattern: "Diagonal stripe"**

Color cell $(i,j)$ white if $i + j \equiv 0 \pmod{2}$ and ... no, that's checkerboard again.

Let me think about a different approach. 

**Pattern: White forms a "staircase" of width 1 going from top to bottom, but zigzagging.**

Consider the following for $n = 4$:
```
W B B B
W B B B
W W B B
B W B B
```
White: $(0,0),(1,0),(2,0),(2,1),(3,1)$. Connected ✓. 
Black: everything else. Is black connected? $(0,1)-(0,2)-(0,3)-(1,3)-(2,3)-(3,3)-(3,2)-(2,2)-(1,2)-(1,1)-(0,1)$... let me check: $(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,0),(3,2),(3,3)$. 
$(3,0)$: adjacent to $(2,0)$=W and $(3,1)$=W. So $(3,0)$ is isolated! Black is not connected. Fails.

The problem is that the white path from top to bottom separates the grid.

**Key realization:** If white is a connected path from the top edge to the bottom edge, it separates the grid into left and right parts, disconnecting black. Similarly for left to right.

So white must NOT form a top-to-bottom or left-to-right crossing. But white must hit every $2 \times 2$ subgrid.

Hmm, but if white doesn't cross the grid, how can it hit $2 \times 2$ subgrids in both the top-left and bottom-right corners?

Wait, white doesn't need to be a thin path. It can be a thicker structure.

**Alternative: White is a "frame" or "L-shape".**

Consider white being the first row and first column (an L-shape):
```
W W W W
W B B B
W B B B
W B B B
```
White: first row + first column. Connected ✓. Black: the $(n-1) \times (n-1)$ bottom-right block. Connected ✓.
$2 \times 2$ subgrids: those involving row 0 or column 0 have white. But the bottom-right $2 \times 2$ blocks (entirely in rows $1..n-1$, cols $1..n-1$) are all black! Fails for $n \geq 3$.

So we need white to penetrate into the interior.

**Pattern: "Staircase L" that penetrates.**

What if white is a staircase that goes along the top, then down, then right, then down, etc.?

Consider a "staircase" path from top-left going right then down repeatedly:
```
W W W B B
B B W B B
B B W W W
B B B B B
B B B B B
```
For $n = 5$. White: $(0,0),(0,1),(0,2),(1,2),(2,2),(2,3),(2,4)$. Connected ✓.
Black: everything else. Is it connected? The bottom-left and the area around $(0,3),(0,4),(1,3),(1,4)$... $(0,3)$ is adjacent to $(0,4)$ and $(1,3)$, all black. $(1,3)-(1,4)-(2,4)$? $(2,4)$ is white. $(1,4)-(0,4)$ ✓. $(1,3)-(2,3)$? $(2,3)$ is white. Hmm. $(1,3)-(1,4)-(0,4)$: these are connected. But are they connected to the bottom? $(1,3)$'s neighbors: $(0,3)$=B, $(2,3)$=W, $(1,2)$=W, $(1,4)$=B. So the top-right black region $\{(0,3),(0,4),(1,3),(1,4)\}$ is separated from the bottom black region by the white staircase. Black is disconnected. Fails.

The fundamental issue: a white path that cuts across separates black.

**New idea:** White should be a "tree" or "star" that reaches into all corners but doesn't separate the grid. But hitting every $2 \times 2$ requires being quite spread out...

Actually, wait. Let me reconsider. Maybe we should think about this differently. Instead of minimizing white, maybe the optimal configuration has a specific structure.

**Thinking about it as a graph/cut problem.**

The grid graph is planar. We're partitioning vertices into black and white, both connected, no $2 \times 2$ monochromatic. This is like a connected 2-partition with an additional constraint.

**Let me think about the "stripe" pattern.**

What if we alternate columns? Like columns $0, 1$ white, columns $2, 3$ black, columns $4, 5$ white, etc.?

For $n = 4$: columns 0,1 white, columns 2,3 black.
```
W W B B
W W B B
W W B B
W W B B
```
$2 \times 2$ blocks: the one at rows 0-1, cols 1-2 is $\{W, B, W, B\}$ ✓. But the one at rows 0-1, cols 0-1 is all white ✗. Fails.

What about alternating single columns? Column 0 white, column 1 black, column 2 white, column 3 black:
```
W B W B
W B W B
W B W B
W B W B
```
$2 \times 2$ at rows 0-1, cols 0-1: $\{W,B,W,B\}$ ✓. All $2 \times 2$ have both colors ✓. White: columns 0,2. Connected? Column 0 and column 2 are not adjacent (column 1 is between them). Not connected ✗.

**What about a "thick stripe" with a connector?**

Hmm, let me think about this more carefully.

**The "zigzag" pattern:**

Consider a pattern where white forms a zigzag path that's 2 cells wide. 

Actually, let me think about the problem from the perspective of known competition problems. This looks like it could be from a math olympiad. The answer $f(10) + f(11)$ suggests specific values.

Let me think about what $f(n)$ could be.

**Construction: "Staircase with width 2".**

Consider the anti-diagonal. Color cells white if they're on or near the anti-diagonal, and black otherwise. But we need to be careful.

Let me try a different approach. Consider the coloring where:
- Cell $(i, j)$ is white if $i + j \leq n-1$ (upper-left triangle including anti-diagonal)
- Cell $(i, j)$ is black if $i + j > n-1$ (lower-right triangle)

Wait, this creates a big white triangle and a big black triangle. The $2 \times 2$ blocks near the anti-diagonal have both colors, but blocks far from it are monochromatic. Fails.

**Let me think about the "striped staircase" pattern more carefully.**

What if we use a pattern like:
- Row $i$: columns $0$ to $f(i)$ are one color, and columns $f(i)+1$ to $n-1$ are the other color, where $f(i)$ is a staircase function.

For this to avoid $2 \times 2$ monochromatic blocks, we need $|f(i) - f(i+1)| \leq 1$ for all $i$ (so the boundary shifts by at most 1 between consecutive rows). Actually, let me think about this more carefully.

If row $i$ has black in columns $0..f(i)$ and white in columns $f(i)+1..n-1$:
- A $2 \times 2$ block at rows $i, i+1$ and columns $j, j+1$:
  - If both $j, j+1 \leq f(i)$ and $j, j+1 \leq f(i+1)$: all black. Bad.
  - If both $j, j+1 > f(i)$ and $j, j+1 > f(i+1)$: all white. Bad.
  - Otherwise: mixed. Good.

So we need: for every $j \in \{0, ..., n-2\}$, it's not the case that both $j, j+1 \leq \min(f(i), f(i+1))$ or both $j, j+1 > \max(f(i), f(i+1))$.

The first condition fails when $\min(f(i), f(i+1)) \geq 1$, i.e., there exists $j$ with $j+1 \leq \min(f(i), f(i+1))$, which happens when $\min(f(i), f(i+1)) \geq 1$.

Wait, this means ANY staircase with $f(i) \geq 1$ for consecutive rows will have a $2 \times 2$ all-black block. That's because if $f(i) \geq 1$ and $f(i+1) \geq 1$, then columns 0 and 1 are both black in rows $i$ and $i+1$.

So a simple staircase (one boundary per row) doesn't work unless the boundary is always at position 0 or $n-1$.

Hmm, so we need a more complex pattern. The boundary can't be a simple monotone staircase.

**What if each row has multiple color changes?**

Consider a "brick" or "zigzag" pattern within rows.

Let me think about the following pattern:
- In even rows: cells at even columns are white, odd columns are black.
- In odd rows: cells at odd columns are white, even columns are black.

This is the checkerboard! $B = W = n^2/2$ (for even $n$). Not helpful for maximizing $|B-W|$.

**What about a "shifted" pattern?**

- In even rows: all black except column 0 which is white.
- In odd rows: all white except column 0 which is black.

Wait, let me think... 

- Even row $i$: column 0 = W, rest = B.
- Odd row $i$: column 0 = B, rest = W.

For $n = 4$:
```
W B B B
B W W W
W B B B
B W W W
```
$B = 8, W = 8$. Equal. Not helpful.

$2 \times 2$ at rows 0-1, cols 0-1: $\{W, B, B, W\}$ ✓.
$2 \times 2$ at rows 0-1, cols 1-2: $\{B, B, W, W\}$ ✓.
$2 \times 2$ at rows 1-2, cols 1-2: $\{W, W, B, B\}$ ✓.
All good, but $|B-W| = 0$.

**Let me think about asymmetric patterns.**

What if we have a pattern where one color is much more prevalent? 

Consider:
- Row 0: all white.
- Rows 1 to $n-1$: a pattern that has mostly black but enough white to hit every $2 \times 2$ and keep white connected.

Row 0 all white ensures white is connected to the top. Then in subsequent rows, we need white cells that:
1. Are connected to row 0 (through adjacent white cells).
2. Hit every $2 \times 2$ subgrid in rows $1..n-1$.
3. Keep black connected.

For rows $1..n-1$, the $2 \times 2$ subgrids entirely within rows $1..n-1$ need a white cell. Also $2 \times 2$ subgrids spanning rows $0-1$ already have white from row 0.

So we need white cells in rows $1..n-1$ that hit every $2 \times 2$ subgrid within rows $1..n-1$, i.e., in the $(n-1) \times n$ subgrid.

This is recursive! We need a connected white set in the $(n-1) \times n$ grid that hits every $2 \times 2$ subgrid, and the complement is connected.

Hmm, but this recursion doesn't simplify things much.

**Let me try a specific construction and compute.**

**Construction: "Comb" pattern.**

White = first row (all white) + every other column in subsequent rows.

For $n = 5$:
```
W W W W W
W B W B W
W B W B W
W B W B W
W B W B W
```
White: row 0 (all) + columns 0, 2, 4 in rows 1-4. 
$W = 5 + 3 \times 4 = 17$. $B = 25 - 17 = 8$. $|B - W| = 9$.

Check connectivity: White is connected (row 0 connects all columns, and each column extends down). ✓
Black: columns 1, 3 in rows 1-4. Column 1: $(1,1),(2,1),(3,1),(4,1)$ - connected. Column 3: $(1,3),(2,3),(3,3),(4,3)$ - connected. But column 1 and column 3 are not adjacent (column 2 is white). So black has two components. ✗ Fails!

**Fix: connect the black columns.**

We need to connect the black columns. We could make some cells in column 2 black to bridge.

```
W W W W W
W B W B W
W B B B W
W B W B W
W B W B W
```
Now black: columns 1,3 in rows 1-4, plus $(2,2)$. Column 1 and column 3 are connected through $(2,2)$. ✓
$W = 5 + 3 \times 4 - 1 = 16$. $B = 9$. $|B-W| = 7$.

Check $2 \times 2$:
- Rows 0-1: all have white from row 0. ✓
- Rows 1-2, cols 0-1: $(1,0)=W, (1,1)=B, (2,0)=W, (2,1)=B$. ✓
- Rows 1-2, cols 1-2: $(1,1)=B, (1,2)=W, (2,1)=B, (2,2)=B$. Has W ✓.
- Rows 1-2, cols 2-3: $(1,2)=W, (1,3)=B, (2,2)=B, (2,3)=B$. Has W ✓.
- Rows 1-2, cols 3-4: $(1,3)=B, (1,4)=W, (2,3)=B, (2,4)=W$. ✓
- Rows 2-3, cols 0-1: $(2,0)=W, (2,1)=B, (3,0)=W, (3,1)=B$. ✓
- Rows 2-3, cols 1-2: $(2,1)=B, (2,2)=B, (3,1)=B, (3,2)=W$. Has W ✓.
- Rows 2-3, cols 2-3: $(2,2)=B, (2,3)=B, (3,2)=W, (3,3)=B$. Has W ✓.
- Rows 2-3, cols 3-4: $(2,3)=B, (2,4)=W, (3,3)=B, (3,4)=W$. ✓
- Rows 3-4: similar to rows 1-2 by symmetry. ✓

All good! So for $n = 5$, we get $|B-W| = 7$ with this construction. But is this optimal?

Hmm, but we want to maximize $|B - W|$, so we want to minimize the minority color. In this construction, $B = 9$ is the minority. Can we do better?

Wait, we could also try to make white the minority. Let's think about which is better.

Actually, by symmetry (swapping black and white), $f(n)$ is the same whether we maximize $B - W$ or $W - B$. So $f(n) = \max(|B-W|)$ and we can assume WLOG that $B > W$.

So we want to minimize $W$ (white cells) subject to:
1. White is connected.
2. Black is connected.
3. Every $2 \times 2$ has at least one white.

In the comb construction above, $W = 16$ for $n = 5$. Can we do better?

**Better construction: minimize white.**

Let me think about what's the minimum number of white cells needed.

Every $2 \times 2$ subgrid needs a white cell. There are $(n-1)^2$ subgrids. Each white cell covers at most 4 subgrids. So $|W| \geq \lceil (n-1)^2 / 4 \rceil$.

For $n = 5$: $\lceil 16/4 \rceil = 4$. But we also need connectivity, which requires more.

For $n = 10$: $\lceil 81/4 \rceil = 21$. For $n = 11$: $\lceil 100/4 \rceil = 25$.

But connectivity adds overhead. Let me think about what patterns achieve close to this bound while being connected.

**Optimal-ish pattern: "Staircase path".**

Consider a path of white cells that snakes through the grid, hitting every $2 \times 2$ subgrid. 

A path that goes: right along row 0, down one, left along row 1, down one, right along row 2, etc. (boustrophedon/snake). This path has $n^2$ cells if it covers the whole grid, but we want a shorter path.

Actually, we don't need to cover every cell, just hit every $2 \times 2$. 

A white cell at position $(i, j)$ covers the $2 \times 2$ subgrids with top-left corners at $(i-1, j-1), (i-1, j), (i, j-1), (i, j)$ (those that exist).

To hit every $2 \times 2$ subgrid, we need: for every $i \in \{0, ..., n-2\}, j \in \{0, ..., n-2\}$, at least one of $(i,j), (i,j+1), (i+1,j), (i+1,j+1)$ is white.

This is equivalent to: the white cells form a "dominating set" for the $(n-1) \times (n-1)$ grid of $2 \times 2$ blocks, where each block is dominated by any of its 4 cells.

The minimum such set (without connectivity) is $\lceil (n-1)^2 / 4 \rceil$, achieved by placing white cells at every other position in a grid-like pattern.

But with connectivity, we need more. And we also need black to be connected.

**Let me think about a "staircase" white path.**

Consider a path that goes diagonally: $(0,0), (0,1), (1,1), (1,2), (2,2), (2,3), (3,3), (3,4), ...$

This path has $2(n-1) + 1 = 2n - 1$ cells (for a path from $(0,0)$ to $(n-1, n-1)$ going right-down-right-down...).

Wait, let me count. The path $(0,0) \to (0,1) \to (1,1) \to (1,2) \to (2,2) \to (2,3) \to \cdots \to (n-1, n-1)$. Each step is either right or down, alternating. Total steps: $2(n-1)$, so $2n-1$ cells.

Does this hit every $2 \times 2$ subgrid? Consider the $2 \times 2$ subgrid at rows $i, i+1$ and columns $j, j+1$. The path passes through $(i, j)$ or $(i, j+1)$ or $(i+1, j)$ or $(i+1, j+1)$?

The path goes through $(k, k)$ and $(k, k+1)$ for each $k$. So it hits subgrids where $j = k$ or $j = k-1$ for some $k$ in the right range. But what about subgrids far from the diagonal, like rows 0-1, columns $n-2, n-1$? The path doesn't go near there. So this doesn't hit all $2 \times 2$ subgrids. ✗

**We need the white cells to be spread across the entire grid.**

Let me reconsider. The key tension is:
- White must be spread out (to hit every $2 \times 2$) → needs many cells or a long path.
- White must be connected → the spread-out cells must be linked.
- Black must be connected → white must not separate the grid.

**The "thin snake" pattern:**

Consider a snake/boustrophedon path that covers every other row:
- Row 0: all white (columns 0 to $n-1$).
- Row 1: column 0 white (to connect to row 2).
- Row 2: all white.
- Row 3: column $n-1$ white (to connect to row 4).
- Row 4: all white.
- ...

This gives white in every even row (full) and connectors in odd rows. 

$2 \times 2$ subgrids: any subgrid spanning an even row and the next odd row has white (from the even row). Any subgrid spanning an odd row and the next even row also has white (from the even row). So every $2 \times 2$ has white. ✓

White connectivity: even rows are full white, connected by single-cell bridges in odd rows. ✓

Black connectivity: black is in odd rows (except the bridge cell). Row 1: columns 1 to $n-1$ (if bridge is at column 0). Row 3: columns 0 to $n-2$ (if bridge is at column $n-1$). These black regions in different odd rows are separated by white even rows. So black is disconnected! ✗

The even rows (all white) separate the odd rows from each other. Black is disconnected.

**Fix: don't make even rows fully white.**

What if we make the "snake" thinner? Instead of full rows, use partial rows.

**Pattern: "Thin snake" with width 1 in even rows.**

Hmm, but then it might not hit all $2 \times 2$ subgrids.

Let me think differently. 

**Pattern: "Diagonal stripes of width 1".**

Color $(i, j)$ white if $i + j \equiv 0 \pmod{3}$ (every third anti-diagonal). 

For this to hit every $2 \times 2$: a $2 \times 2$ block at $(i,j)$ contains cells with $i+j$ values $i+j, i+j+1, i+j+1, i+j+2$. So the values are $\{i+j, i+j+1, i+j+2\}$. One of these is $\equiv 0 \pmod 3$. ✓ Every $2 \times 2$ has a white cell.

White cells: those with $i + j \equiv 0 \pmod 3$. About $n^2/3$ cells. But are they connected? Two white cells at $(i,j)$ and $(i',j')$ with $i+j \equiv i'+j' \equiv 0 \pmod 3$. They're adjacent if $|i-i'| + |j-j'| = 1$, which means $i+j$ differs by 1, so they can't both be $\equiv 0 \pmod 3$. So white cells are NOT edge-adjacent to each other! White is totally disconnected. ✗

**Pattern: "Two consecutive anti-diagonals".**

Color $(i,j)$ white if $i + j \equiv 0$ or $1 \pmod{3}$.

Then about $2n^2/3$ cells are white. $2 \times 2$ has values $\{i+j, i+j+1, i+j+2\}$, at least two of which are $\equiv 0$ or $1$. ✓

White connectivity: cells with $i+j \equiv 0$ are adjacent to cells with $i+j \equiv 1$ (differ by 1 in sum). So white is connected. ✓

Black connectivity: cells with $i+j \equiv 2 \pmod 3$. Two such cells are adjacent only if their sums differ by 1, but both are $\equiv 2$, so they can't be adjacent. Black is disconnected! ✗

**Pattern: "Two consecutive anti-diagonals out of every 4".**

Color $(i,j)$ white if $i + j \equiv 0$ or $1 \pmod{4}$.

$2 \times 2$ has sums $\{s, s+1, s+1, s+2\}$ where $s = i+j$. We need at least one $\equiv 0$ or $1 \pmod 4$. The values $s, s+1, s+2$ cover 3 consecutive values mod 4. If $s \equiv 2$: values are $2, 3, 0$. Has 0 ✓. If $s \equiv 3$: values are $3, 0, 1$. Has 0, 1 ✓. If $s \equiv 0$: has 0, 1 ✓. If $s \equiv 1$: has 1, 2. Has 1 ✓. So every $2 \times 2$ has white. ✓

White: $i+j \equiv 0, 1 \pmod 4$. About $n^2/2$ cells. 
Black: $i+j \equiv 2, 3 \pmod 4$. About $n^2/2$ cells.
$|B - W| \approx 0$. Not helpful for maximizing.

White connectivity: 0 and 1 are consecutive, so cells with sum $\equiv 0$ are adjacent to cells with sum $\equiv 1$. ✓
Black connectivity: 2 and 3 are consecutive, so cells with sum $\equiv 2$ are adjacent to cells with sum $\equiv 3$. ✓

But $|B-W|$ is small. We need an asymmetric pattern.

**Asymmetric pattern: 1 white anti-diagonal out of every 3, but with connectors.**

We saw that 1 out of 3 gives disconnected white. What if we use 1 out of 3 but add some connector cells?

Color $(i,j)$ white if $i+j \equiv 0 \pmod 3$, plus some additional cells to connect them.

The cells with $i+j \equiv 0 \pmod 3$ form a "checkerboard-like" pattern where no two are adjacent. To connect them, we need to add cells with $i+j \equiv 1$ or $2 \pmod 3$.

Each white cell (sum $\equiv 0$) has 4 neighbors, all with sum $\equiv 1$ or $2$. To connect two adjacent-in-the-lattice white cells (diagonally adjacent), we need one intermediate cell.

Actually, the cells with $i+j \equiv 0 \pmod 3$ that are diagonally adjacent (differ by $(1,-1)$ or $(-1,1)$) can be connected by adding the cell between them (which has sum $\equiv 0$ as well... no, $(i,j)$ and $(i+1,j-1)$ both have sum $i+j$, and the cells between them are $(i+1, j)$ and $(i, j-1)$, both with sum $i+j-1 \equiv 2 \pmod 3$).

Hmm, this is getting complicated. Let me think about it differently.

**Let me think about the problem more carefully using the structure of the constraints.**

The condition "no $2 \times 2$ monochromatic" means: for every $i, j$, the $2 \times 2$ block at $(i,j)$ has both colors. This is equivalent to saying the coloring has no "solid $2 \times 2$ block" of either color.

Combined with connectivity of both colors, this is quite restrictive.

**Let me think about the "staircase band" construction more carefully.**

Consider a band of white cells that's 2 cells wide, going diagonally across the grid. The band separates the grid into two black regions, but if the band doesn't go all the way across, the black regions might be connected around the band.

Actually, a diagonal band from one corner to the opposite corner would separate the grid. But a band that starts and ends on the same side, or doesn't span the full width/height, might not.

Hmm, let me think about a different approach entirely.

**Approach: Think about the boundary between black and white.**

The boundary between the two colors is a set of edges in the grid graph. Since both colors are connected, the boundary forms a set of cycles and paths. In a planar embedding, the boundary between two connected regions is a single cycle (or path if one region touches the boundary).

Actually, in a grid, if both black and white are connected, the boundary between them is a single path (or cycle). This is because the dual graph of the boundary is connected.

Hmm, this is getting into planar graph theory. Let me think about it differently.

**Let me try to find the answer by considering specific constructions and seeing which gives the maximum.**

**Construction A: "L-shaped white region".**

White = first row + first column. But we saw this fails for $n \geq 3$ because the interior $2 \times 2$ blocks are all black.

**Construction B: "Staircase white path from top-left, not reaching bottom-right".**

White path: $(0,0), (0,1), ..., (0, n-1), (1, n-1), (2, n-1), ..., (n-1, n-1)$.

This is an L-shape: top row + right column. $|W| = 2n - 1$.

$2 \times 2$ blocks: those touching the top row or right column have white. But blocks in the bottom-left interior (rows $1..n-2$, cols $0..n-2$) might be all black. For $n \geq 4$, there's a $2 \times 2$ block at rows 1-2, cols 0-1 that's all black. ✗

**Construction C: "Thick L-shape".**

White = first two rows + first two columns.

$|W| = 2n + 2(n-2) = 4n - 4$.

$2 \times 2$ blocks: those touching the first two rows or first two columns have white. The interior (rows $2..n-1$, cols $2..n-1$) has $2 \times 2$ blocks that are all black if $n \geq 4$. ✗

**Construction D: "Recursive L-shape" / "Staircase of L-shapes".**

What if we use a staircase of L-shapes? Like:
- Rows 0-1: all white.
- Rows 2-3: columns 0-1 white, rest black.
- Rows 4-5: columns 0-1 white, rest black.
- ...

But then the $2 \times 2$ blocks in rows 2-3, cols 2-3 are all black. ✗

**Construction E: "Boustrophedon white path of width 1, but not separating black".**

The issue with the snake/boustrophedon is that full white rows separate black. What if the white path is thinner?

Consider a white path that goes:
- Row 0: columns 0, 1 (just 2 cells).
- Column 1: rows 0, 1, 2.
- Row 2: columns 1, 2.
- Column 2: rows 2, 3, 4.
- Row 4: columns 2, 3.
- ...

This is a staircase going down-right. But it doesn't hit $2 \times 2$ blocks far from the staircase.

I think the fundamental challenge is that hitting every $2 \times 2$ requires white to be spread across the entire grid, but connectivity + not separating black limits how we can spread.

**Let me reconsider the "comb" construction and try to optimize it.**

In the comb construction, we had:
- Row 0: all white.
- Rows 1 to $n-1$: white in every other column (say even columns), black in odd columns.
- Plus a bridge to connect black columns.

The problem was black columns being disconnected. We fixed it with one bridge cell.

Let me generalize. For $n$ even:

Row 0: all white. ($n$ cells)
Rows 1 to $n-1$: white in even columns (0, 2, 4, ..., $n-2$), black in odd columns (1, 3, 5, ..., $n-1$).
Plus bridges to connect black columns.

Black columns: 1, 3, 5, ..., $n-1$. That's $n/2$ columns. They need to be connected. We can connect adjacent black columns by making one cell in the intervening white column black. Each bridge costs 1 white cell (converts it to black).

To connect $n/2$ columns, we need $n/2 - 1$ bridges.

$W = n + (n/2)(n-1) - (n/2 - 1) = n + n(n-1)/2 - n/2 + 1 = n + (n^2 - n - n)/2 + 1 = n + (n^2 - 2n)/2 + 1 = n + n^2/2 - n + 1 = n^2/2 + 1$.

$B = n^2 - W = n^2/2 - 1$.

$|B - W| = 2$.

That's terrible! The comb with every other column gives almost equal counts.

The issue is that using every other column gives $n/2$ white columns, which is too many. We want fewer white columns.

**What if we use fewer white columns but make them thicker?**

Say white columns are 0, $k$, $2k$, etc., with black columns in between. But then $2 \times 2$ blocks entirely within a black region (between two white columns that are far apart) would be all black.

For no $2 \times 2$ all-black: between two consecutive white columns, there can be at most 1 black column. Because if there are 2+ consecutive black columns, a $2 \times 2$ block within them (in 2 consecutive rows) would be all black.

Wait, not exactly. If columns $j$ and $j+1$ are both black (in some row range), and rows $i$ and $i+1$ are both in that range, then the $2 \times 2$ at $(i, j)$ is all black. So we can't have 2 consecutive black columns in any pair of consecutive rows.

But if row 0 is all white, then the $2 \times 2$ blocks in rows 0-1 are fine. The issue is rows 1 onwards. In rows 1 to $n-1$, we can't have 2 consecutive black columns (because any $2 \times 2$ within rows 1 to $n-1$ with 2 consecutive black columns would be all black).

Wait, actually, we CAN have 2 consecutive black columns if there's a white cell in one of those positions in every pair of consecutive rows. Hmm, no. If columns $j$ and $j+1$ are entirely black in rows $1..n-1$, then the $2 \times 2$ at rows 1-2, cols $j, j+1$ is all black. So we need at least one white cell in columns $j$ or $j+1$ in every pair of consecutive rows.

This means: in rows $1..n-1$, for every pair of consecutive columns, at least one of them has a white cell in every pair of consecutive rows. This is getting complicated.

Let me simplify: if we want columns to be mostly one color, the constraint is that no 2 consecutive columns can be all-black in any 2 consecutive rows (within the non-row-0 region).

**Alternative approach: think about it row by row.**

Let me think about the problem differently. Let's consider the coloring as a binary matrix and think about what structures are possible.

**Key insight: the "no $2 \times 2$ monochromatic" condition means the coloring is a "grid coloring with no monochromatic rectangle of size $2 \times 2$".**

This is related to the concept of "avoiding monochromatic $2 \times 2$ subgrids" which appears in combinatorics.

For a binary matrix with no monochromatic $2 \times 2$ subgrid, the matrix must have a specific structure. Let me think about what structures are possible.

If we look at any two consecutive rows, the condition says: for every pair of consecutive columns, the $2 \times 2$ block is not monochromatic. This means: in any two consecutive rows, we can't have two consecutive columns where both rows have the same color.

Equivalently: in two consecutive rows $i$ and $i+1$, for columns $j$ and $j+1$:
- Not all four cells are black: so if row $i$ has black at $j$ and $j+1$, then row $i+1$ must have white at $j$ or $j+1$.
- Not all four cells are white: so if row $i$ has white at $j$ and $j+1$, then row $i+1$ must have black at $j$ or $j+1$.

This is a local constraint between consecutive rows.

**Let me think about a "shifted rows" pattern.**

Consider rows that are shifts of each other. For example:
- Row 0: $B B W B B W B B W ...$ (pattern $BBW$ repeated)
- Row 1: $B W B B W B B W B ...$ (shifted by 1)
- Row 2: $W B B W B B W B B ...$ (shifted by 2)
- Row 3: $B B W B B W B B W ...$ (same as row 0)
- ...

The pattern $BBW$ repeated has 2/3 black, 1/3 white. Shifting by 1 each row.

Check $2 \times 2$: rows 0-1, cols 0-1: $(0,0)=B, (0,1)=B, (1,0)=B, (1,1)=W$. Not monochromatic ✓.
Rows 0-1, cols 1-2: $(0,1)=B, (0,2)=W, (1,1)=W, (1,2)=B$. Not monochromatic ✓.
Rows 0-1, cols 2-3: $(0,2)=W, (0,3)=B, (1,2)=B, (1,3)=B$. Not monochromatic ✓.

Actually, let me check if any $2 \times 2$ is monochromatic. The pattern in row $i$ is: position $j$ is $W$ iff $j \equiv 2 - i \pmod{3}$, i.e., $j + i \equiv 2 \pmod{3}$.

So $(i,j)$ is $W$ iff $i + j \equiv 2 \pmod{3}$.

This is the "1 out of 3 anti-diagonals" pattern! We already considered this. White is disconnected (no two white cells are adjacent). ✗

**What about 2 out of 3?**

$(i,j)$ is $W$ iff $i + j \equiv 1$ or $2 \pmod{3}$. Then $B$ iff $i + j \equiv 0 \pmod{3}$.

$2 \times 2$ at $(i,j)$: sums are $i+j, i+j+1, i+j+2$. These are 3 consecutive values, so one is $\equiv 0 \pmod 3$. So there's always a black cell. And at least one is $\equiv 1$ or $2$, so there's always a white cell. ✓

White: $i+j \equiv 1, 2 \pmod{3}$. About $2n^2/3$ cells. Connected? $1$ and $2$ are consecutive mod 3, so yes. ✓
Black: $i+j \equiv 0 \pmod{3}$. About $n^2/3$ cells. Connected? Two black cells have sums $\equiv 0$, differ by 1 for adjacency → impossible. Disconnected. ✗

Same issue as before. The minority color (1 out of 3) is always disconnected.

**Fundamental tension:** To have both colors connected, we need both to have adjacent cells. In the anti-diagonal pattern, the minority color (every 3rd diagonal) has no adjacent cells. We need to "thicken" the minority color or use a different pattern.

**What if we use a pattern where the minority color forms connected "stripes"?**

Consider: black forms vertical stripes, white forms vertical stripes, alternating. But we need no 2 consecutive columns of the same color (to avoid $2 \times 2$ monochromatic in consecutive rows).

If we alternate single columns: B W B W B W ... Then both are disconnected (columns of the same color aren't adjacent). ✗

If we alternate pairs: BB WW BB WW ... Then $2 \times 2$ within a BB pair (in consecutive rows) is all black. ✗

So pure column patterns don't work. We need to mix rows and columns.

**The "brick wall" pattern:**

Consider a pattern like a brick wall:
- Even rows: $B B W B B W ...$
- Odd rows: $B W B B W B ...$ (shifted by 1)

This is the 2-out-of-3 pattern we already considered. The minority (black, 1/3) is disconnected.

**What about a different ratio?**

Let me think about what ratios are possible with both colors connected and no $2 \times 2$ monochromatic.

**Construction: "Staircase boundary with thick regions".**

Consider a boundary that's a staircase from the top-left to the bottom-right, but the staircase has steps of varying sizes. Black is on one side, white on the other.

For no $2 \times 2$ monochromatic: the staircase must be "fine enough" that no $2 \times 2$ is entirely on one side. This means the staircase can't have steps that are too large.

Specifically, if the staircase goes from $(0, k_0)$ to $(1, k_1)$ to $(2, k_2)$ etc., where $k_i$ is the last black column in row $i$, then:
- No $2 \times 2$ all black: for consecutive rows $i, i+1$, we need that columns $\min(k_i, k_{i+1})$ and $\min(k_i, k_{i+1}) + 1$ are not both black in both rows. This means $\min(k_i, k_{i+1}) < n-1$ and... actually, if $k_i \geq 1$ and $k_{i+1} \geq 1$, then columns 0 and 1 are both black in both rows, giving a $2 \times 2$ all-black block. 

So we need $\min(k_i, k_{i+1}) < 1$, i.e., $\min(k_i, k_{i+1}) = 0$ or $-1$ (meaning at least one of rows $i, i+1$ has no black cells, or black only in column 0).

This is very restrictive! It means in any two consecutive rows, at least one has black only in column 0 (or no black at all). So the staircase can only have black in column 0 for at least every other row.

Similarly, for no $2 \times 2$ all white: in any two consecutive rows, at least one has white only in column $n-1$ (or no white at all). So at least every other row has white only in column $n-1$.

This means the staircase is extremely constrained. Essentially, rows alternate between "almost all white" and "almost all black", or similar.

Wait, let me reconsider. The staircase boundary means row $i$ has black in columns $0..k_i$ and white in columns $k_i+1..n-1$. The no-$2\times2$-monochromatic constraint:

For rows $i, i+1$ and columns $j, j+1$:
- All black iff $j+1 \leq k_i$ and $j+1 \leq k_{i+1}$, i.e., $j \leq \min(k_i, k_{i+1}) - 1$. This exists iff $\min(k_i, k_{i+1}) \geq 1$.
- All white iff $j > k_i$ and $j > k_{i+1}$, i.e., $j \geq \max(k_i, k_{i+1}) + 1$. This exists iff $\max(k_i, k_{i+1}) \leq n-3$.

So the constraints are:
- $\min(k_i, k_{i+1}) \leq 0$ for all $i$ (no all-black $2 \times 2$)
- $\max(k_i, k_{i+1}) \geq n-2$ for all $i$ (no all-white $2 \times 2$)

The first means: for every pair of consecutive rows, at least one has $k_i \leq 0$ (black only in column 0, or no black).
The second means: for every pair of consecutive rows, at least one has $k_i \geq n-2$ (white only in column $n-1$, or no white).

Combining: for every pair of consecutive rows, one has $k \leq 0$ and one has $k \geq n-2$. So the rows must alternate between $k \leq 0$ and $k \geq n-2$.

If $n$ is even, we can have:
- Even rows: $k = 0$ (black only in column 0, rest white). $B = 1, W = n-1$ per row.
- Odd rows: $k = n-2$ (white only in column $n-1$, rest black). $B = n-1, W = 1$ per row.

Total: $B = n/2 \cdot 1 + n/2 \cdot (n-1) = n/2 \cdot n = n^2/2$. $W = n^2/2$. $|B-W| = 0$.

If $n$ is odd:
- Even rows (there are $(n+1)/2$ of them): $k = 0$. $B = 1, W = n-1$.
- Odd rows (there are $(n-1)/2$ of them): $k = n-2$. $B = n-1, W = 1$.

$B = (n+1)/2 \cdot 1 + (n-1)/2 \cdot (n-1) = (n+1)/2 + (n-1)^2/2 = (n+1 + n^2 - 2n + 1)/2 = (n^2 - n + 2)/2$.
$W = n^2 - B = (2n^2 - n^2 + n - 2)/2 = (n^2 + n - 2)/2$.
$|B - W| = |(n^2 - n + 2 - n^2 - n + 2)/2| = |(-2n + 4)/2| = |n - 2| = n - 2$ (for $n > 2$).

Wait, but we also need both colors to be connected! Let me check.

For even $n$, even rows have black only in column 0, odd rows have black in columns 0 to $n-2$. Black in even rows: just $(i, 0)$. Black in odd rows: $(i, 0), (i, 1), ..., (i, n-2)$. 

Is black connected? $(0, 0)$ is adjacent to $(1, 0)$ (which is black). $(1, 0)$ is adjacent to $(2, 0)$ (black). Etc. So all black cells in column 0 form a connected path. And in odd rows, black extends to columns 1, 2, ..., $n-2$, all connected to column 0. So black is connected. ✓

Is white connected? Even rows have white in columns 1 to $n-1$. Odd rows have white only in column $n-1$. White in column $n-1$: all rows have white in column $n-1$ (even rows: columns 1 to $n-1$ include $n-1$; odd rows: column $n-1$). So column $n-1$ is all white, forming a connected path. And even rows have white extending to columns 1, 2, ..., $n-2$, all connected to column $n-1$. So white is connected. ✓

So this staircase construction works and gives $|B - W| = 0$ for even $n$ and $|B - W| = n - 2$ for odd $n$.

But wait, for even $n$, $|B - W| = 0$ is not very good. Can we do better with a non-staircase pattern?

Also, for odd $n$, $|B - W| = n - 2$. For $n = 11$: $|B - W| = 9$.

But we might be able to do better with more complex patterns (not just a single staircase boundary).

**Let me reconsider. The staircase gives $|B-W| = n-2$ for odd $n$ and $0$ for even $n$. Can we do better?**

The staircase is limited because it has a single boundary per row. What if we allow more complex row patterns?

**More general construction: "Alternating thick rows".**

Instead of a staircase, consider:
- Some rows are almost all black (with a few white cells).
- Some rows are almost all white (with a few black cells).
- The rows alternate to avoid $2 \times 2$ monochromatic blocks.

But we need to be more careful. Let me think about what happens with two consecutive rows.

If row $i$ is almost all black and row $i+1$ is almost all black, then a $2 \times 2$ block in columns where both rows are all black would be monochromatic. So we can't have two consecutive "almost all black" rows unless the white cells are placed to hit every $2 \times 2$.

Similarly for two consecutive "almost all white" rows.

So the constraint is: in any two consecutive rows, the white cells (across both rows) must hit every pair of consecutive columns, AND the black cells must hit every pair of consecutive columns.

This means: in any two consecutive rows, there's no pair of consecutive columns that's all black, and no pair that's all white.

For a pair of consecutive rows, think of them as a $2 \times n$ strip. We need: no $2 \times 2$ monochromatic block in this strip. This means: for every $j$, the $2 \times 2$ at columns $j, j+1$ has both colors.

In a $2 \times n$ strip, the condition "no $2 \times 2$ monochromatic" is equivalent to: for every $j$, not all of $(row_i[j], row_i[j+1], row_{i+1}[j], row_{i+1}[j+1])$ are the same.

This is a constraint on consecutive column pairs in the two rows.

**Let me think about the problem as optimizing over all valid colorings.**

This is a combinatorial optimization problem. Let me think about upper bounds.

**Upper bound approach:**

Consider the grid. Every $2 \times 2$ subgrid has both colors. Consider the $n-1$ "row pairs" (rows $0-1, 1-2, \ldots, (n-2)-(n-1)$) and the $n-1$ "column pairs".

For each row pair $(i, i+1)$, define $w_i$ = number of white cells in these two rows, $b_i$ = number of black cells. $w_i + b_i = 2n$.

The no-$2\times2$-monochromatic condition on this row pair means: for every $j \in \{0, \ldots, n-2\}$, the $2 \times 2$ at columns $j, j+1$ has both colors. 

In a $2 \times n$ strip with no monochromatic $2 \times 2$, what's the maximum imbalance? Let me think...

In a $2 \times n$ strip, each column has 2 cells. Let $c_j$ be the number of black cells in column $j$ (0, 1, or 2). The no-monochromatic-$2\times2$ condition means: for every $j$, the pair of columns $j, j+1$ is not all-black (so $c_j + c_{j+1} \leq 3$) and not all-white (so $c_j + c_{j+1} \geq 1$).

So $1 \leq c_j + c_{j+1} \leq 3$ for all $j$.

Since $c_j \in \{0, 1, 2\}$:
- $c_j + c_{j+1} \geq 1$: can't have two consecutive 0s.
- $c_j + c_{j+1} \leq 3$: can't have two consecutive 2s.

So the sequence $c_0, c_1, \ldots, c_{n-1}$ has no two consecutive 0s and no two consecutive 2s.

To maximize black in this strip: maximize $\sum c_j$. The sequence alternates between 2 and at most 1 (since no two consecutive 2s). So the max is $2, 1, 2, 1, \ldots$ giving $\sum = \lceil n/2 \rceil \cdot 2 + \lfloor n/2 \rfloor \cdot 1 = \lceil n/2 \rceil \cdot 2 + \lfloor n/2 \rfloor$.

For even $n$: $n/2 \cdot 2 + n/2 \cdot 1 = n + n/2 = 3n/2$. Out of $2n$ total. So max black = $3n/2$, min white = $n/2$.
For odd $n$: $\lceil n/2 \rceil \cdot 2 + \lfloor n/2 \rfloor = (n+1)/2 \cdot 2 + (n-1)/2 = n+1 + (n-1)/2 = (3n+1)/2$. Out of $2n$.

But this is for a single row pair. The row pairs overlap (row $i$ is in pairs $i-1$ and $i$), so we can't independently optimize each pair.

**Let me think about the global structure differently.**

Actually, let me think about the problem column by column. For each column $j$, let $b_j$ = number of black cells in column $j$. Then $B = \sum b_j$.

The no-$2\times2$-monochromatic condition for the column pair $(j, j+1)$: in the $n \times 2$ strip formed by columns $j, j+1$, no $2 \times 2$ is monochromatic. By the same argument as above, if $r_i$ = number of black cells in row $i$ within these two columns (0, 1, or 2), then no two consecutive $r_i$ are both 0 or both 2.

To maximize $\sum_j b_j$ (total black), we want each column to have as many black cells as possible, but the column-pair constraints limit this.

Hmm, this is still complex because the constraints couple adjacent columns.

**Let me try a different approach: think about the problem as a 1D cellular automaton.**

Consider the coloring row by row. Each row is a binary string of length $n$. The constraint is:
1. No $2 \times 2$ monochromatic: for consecutive rows $i, i+1$, the pair $(row_i, row_{i+1})$ has no monochromatic $2 \times 2$.
2. Both colors connected globally.
3. Maximize $|B - W|$.

The no-$2\times2$-monochromatic constraint is a local constraint between consecutive rows. The connectivity is a global constraint.

**Let me think about what row patterns are compatible.**

Two rows $r$ and $r'$ (binary strings of length $n$) are "compatible" if there's no $j$ such that $r[j] = r[j+1] = r'[j] = r'[j+1]$ (all same color).

Given a row $r$, what rows $r'$ are compatible with it?

If $r$ has a run of black from column $j$ to $j+k$, then $r'$ must have a white cell in every pair of consecutive columns within that run. Specifically, for every $l$ with $j \leq l < j+k$, at least one of $r'[l], r'[l+1]$ is white.

This means $r'$ can't have two consecutive black cells within the run of black in $r$. Similarly, $r'$ can't have two consecutive white cells within a run of white in $r$.

**Optimization approach: think about the "extremal" rows.**

To maximize black, we want most rows to be mostly black. But two consecutive mostly-black rows would have $2 \times 2$ all-black blocks. So we need to alternate "mostly black" rows with rows that break up the black.

**Construction: "Alternating rows with sparse white."**

Consider:
- Even rows: all black except column $n-1$ is white. ($B = n-1, W = 1$ per row)
- Odd rows: all black except columns 0 and $n-1$ are white. ($B = n-2, W = 2$ per row)

Wait, let me check compatibility. Even row: $B B B ... B W$. Odd row: $W B B ... B W$.

$2 \times 2$ at cols 0-1: even row has $B B$, odd row has $W B$. Not monochromatic ✓.
$2 \times 2$ at cols 1-2: even row has $B B$, odd row has $B B$. ALL BLACK ✗!

Fails. The issue is that both rows have black in columns 1 to $n-2$.

**We need the "breaker" rows to break up ALL runs of black in the adjacent rows.**

If an even row is all black (or has a long run of black), the adjacent odd rows must have white cells frequently enough to break every $2 \times 2$.

If even row is all black, then odd row must have no two consecutive black cells (because any two consecutive black cells in the odd row, combined with the all-black even row, give a $2 \times 2$ all-black block). So the odd row must have white in every other cell at least.

Similarly, if even row is all black, the odd row must have no two consecutive white cells (because any two consecutive white cells in the odd row, combined with... wait, the even row is all black, so a $2 \times 2$ with two white cells in the odd row and two black cells in the even row is NOT monochromatic). 

Actually, let me reconsider. If even row is all black:
- $2 \times 2$ at cols $j, j+1$: even row has $B B$, odd row has $r[j], r[j+1]$. This is all-black iff $r[j] = r[j+1] = B$. So we need: no two consecutive black cells in the odd row.
- It's all-white iff even row is all white, which it's not. So no all-white constraint from this pair.

So if even row is all black, odd row must have no two consecutive black cells. The odd row is a binary string with no two consecutive 1s (if 1=black). The maximum number of 1s is $\lceil n/2 \rceil$.

But we also need the pair (odd row, next even row) to be compatible. If the next even row is also all black, then the odd row must have no two consecutive black cells (same constraint). And the odd row must have no two consecutive white cells (to avoid all-white $2 \times 2$ with the next even row... no, the next even row is all black, so all-white is impossible).

Wait, but we also need no all-WHITE $2 \times 2$. If even rows are all black, then $2 \times 2$ blocks spanning an even and odd row can't be all white (even row is black). But $2 \times 2$ blocks spanning two odd rows? No, consecutive rows are (even, odd) or (odd, even), never (odd, odd). So if all even rows are all black, the only constraint is that odd rows have no two consecutive black cells.

But then white is only in odd rows, and odd rows have no two consecutive black cells, meaning white appears at least every other cell. White cells in different odd rows: are they connected? Row 1 and row 3 are separated by row 2 (all black), so white in row 1 is not connected to white in row 3. ✗ White is disconnected.

So we can't have all even rows be all black. We need white to be connected across rows.

**Construction: "Mostly black with a white column".**

What if we have a single column that's all white, and the rest is mostly black?

Column 0: all white. Columns 1 to $n-1$: all black.

$2 \times 2$ at cols 0-1: has white (from column 0) ✓. $2 \times 2$ at cols 1-2: all black ✗ (for $n \geq 3$).

Fails. We need more white spread.

**Construction: "Two white columns, far apart, with a white connector row."**

Columns 0 and $n-1$: all white. A middle row (say row $n/2$): all white. Rest: black.

$2 \times 2$ at cols 1-2 (interior): if both rows are not the middle row, all black ✗.

Fails again. The interior is too wide.

**I think the key insight is that we need white to be spread throughout the grid, not just in a few columns/rows.**

Let me go back to the staircase construction and see if we can improve it.

The staircase gave $|B-W| = n-2$ for odd $n$ and $0$ for even $n$. Let me see if we can do better.

**Improved staircase: "Two staircases".**

What if we have two staircase boundaries instead of one? This could allow more imbalance.

Consider a coloring with two boundaries: one separating black from white in the top part, and another in the bottom part. But this might disconnect one of the colors.

Actually, let me think about a different kind of construction.

**Construction: "Pyramid" pattern.**

Consider a coloring where black forms a "pyramid" or "triangle" shape:
- Row 0: column 0 is black, rest white.
- Row 1: columns 0, 1 are black, rest white.
- ...
- Row $k$: columns 0 to $k$ are black, rest white.
- Row $k+1$: columns 0 to $k-1$ are black, rest white.
- ...
- Row $n-1$: column 0 is black, rest white.

This is a pyramid with peak at row $k$. But we already showed that staircase patterns (single boundary per row) require alternating between $k \leq 0$ and $k \geq n-2$, so this pyramid doesn't satisfy the $2 \times 2$ constraint.

**Let me reconsider the staircase constraint.**

We showed that for a staircase (single boundary per row), the constraints are:
- $\min(k_i, k_{i+1}) \leq 0$ for all $i$.
- $\max(k_i, k_{i+1}) \geq n-2$ for all $i$.

This forces alternation between $k \leq 0$ and $k \geq n-2$. The only freedom is:
- Which rows have $k \leq 0$ and which have $k \geq n-2$.
- The exact values of $k$ (e.g., $k = 0$ vs $k = -1$, or $k = n-2$ vs $k = n-1$).

For the "low" rows ($k \leq 0$): $k = 0$ gives 1 black cell, $k = -1$ gives 0 black cells.
For the "high" rows ($k \geq n-2$): $k = n-2$ gives $n-1$ black cells, $k = n-1$ gives $n$ black cells.

To maximize $B - W$ (maximize black), we want:
- "Low" rows to have $k = 0$ (1 black, $n-1$ white).
- "High" rows to have $k = n-1$ (all black, 0 white).

But we need to check: if a "high" row has $k = n-1$ (all black) and the adjacent "low" row has $k = 0$ (black in column 0 only):
- $\min(k_{high}, k_{low}) = \min(n-1, 0) = 0 \leq 0$ ✓
- $\max(k_{high}, k_{low}) = \max(n-1, 0) = n-1 \geq n-2$ ✓

So this works! Let me compute $B$ and $W$ for this optimized staircase.

For even $n$:
- $n/2$ "low" rows with $k = 0$: $B = 1$ each, total $n/2$.
- $n/2$ "high" rows with $k = n-1$: $B = n$ each, total $n \cdot n/2 = n^2/2$.
- $B = n/2 + n^2/2 = n(n+1)/2$.
- $W = n^2 - B = n^2 - n(n+1)/2 = n(2n - n - 1)/2 = n(n-1)/2$.
- $|B - W| = n(n+1)/2 - n(n-1)/2 = n$.

Wait, that's better than before! Let me recheck.

Previously I had $k = 0$ and $k = n-2$, giving $|B-W| = 0$ for even $n$. Now with $k = 0$ and $k = n-1$, we get $|B-W| = n$.

But wait, I need to check the no-$2\times2$-monochromatic constraint more carefully.

"Low" row: $k = 0$, so black in column 0, white in columns 1 to $n-1$.
"High" row: $k = n-1$, so all black.

$2 \times 2$ at cols 0-1, rows (low, high):
- Low row: $B, W$. High row: $B, B$.
- Block: $\{B, W, B, B\}$. Not monochromatic ✓.

$2 \times 2$ at cols 1-2, rows (low, high):
- Low row: $W, W$. High row: $B, B$.
- Block: $\{W, W, B, B\}$. Not monochromatic ✓.

$2 \times 2$ at cols $j, j+1$ for $j \geq 1$, rows (low, high):
- Low row: $W, W$. High row: $B, B$.
- Not monochromatic ✓.

$2 \times 2$ at cols 0-1, rows (high, low):
- High row: $B, B$. Low row: $B, W$.
- Block: $\{B, B, B, W\}$. Not monochromatic ✓.

$2 \times 2$ at cols 1-2, rows (high, low):
- High row: $B, B$. Low row: $W, W$.
- Not monochromatic ✓.

All good! Now check connectivity.

Black: column 0 is all black (every row has black in column 0). In "high" rows, all columns are black. So black is connected through column 0. ✓

White: "low" rows have white in columns 1 to $n-1$. "High" rows have no white. So white exists only in "low" rows. Are white cells in different "low" rows connected? Row 0 (low) and row 2 (low) are separated by row 1 (high, all black). White in row 0 is not adjacent to white in row 2. ✗ White is disconnected!

So we can't have "high" rows be ALL black. We need at least one white cell in each "high" row to connect white across rows.

**Fix: "high" rows have $k = n-2$ (white in column $n-1$ only).**

"Low" row: $k = 0$ (black in column 0, white in columns 1 to $n-1$).
"High" row: $k = n-2$ (black in columns 0 to $n-2$, white in column $n-1$).

Check $2 \times 2$:
$2 \times 2$ at cols 0-1, rows (low, high):
- Low: $B, W$. High: $B, B$.
- $\{B, W, B, B\}$. ✓

$2 \times 2$ at cols $n-2, n-1$, rows (low, high):
- Low: $W, W$. High: $B, W$.
- $\{W, W, B, W\}$. ✓

$2 \times 2$ at cols $j, j+1$ for $1 \leq j \leq n-3$, rows (low, high):
- Low: $W, W$. High: $B, B$.
- $\{W, W, B, B\}$. ✓

$2 \times 2$ at cols 0-1, rows (high, low):
- High: $B, B$. Low: $B, W$.
- $\{B, B, B, W\}$. ✓

$2 \times 2$ at cols $n-2, n-1$, rows (high, low):
- High: $B, W$. Low: $W, W$.
- $\{B, W, W, W\}$. ✓

$2 \times 2$ at cols $j, j+1$ for $1 \leq j \leq n-3$, rows (high, low):
- High: $B, B$. Low: $W, W$.
- $\{B, B, W, W\}$. ✓

All ✓!

Connectivity:
Black: column 0 is all black (both low and high rows have black in column 0). High rows have black in columns 0 to $n-2$. All connected through column 0. ✓

White: column $n-1$ is all white (both low and high rows have white in column $n-1$). Low rows have white in columns 1 to $n-1$. All connected through column $n-1$. ✓

Now compute $B$ and $W$:

For even $n$:
- $n/2$ "low" rows: $B = 1, W = n-1$ each.
- $n/2$ "high" rows: $B = n-1, W = 1$ each.
- $B = n/2 \cdot 1 + n/2 \cdot (n-1) = n/2 \cdot n = n^2/2$.
- $W = n^2/2$.
- $|B - W| = 0$.

For odd $n$:
- $(n+1)/2$ "low" rows: $B = 1, W = n-1$ each.
- $(n-1)/2$ "high" rows: $B = n-1, W = 1$ each.
- $B = (n+1)/2 + (n-1)/2 \cdot (n-1) = (n+1)/2 + (n-1)^2/2 = (n+1+n^2-2n+1)/2 = (n^2-n+2)/2$.
- $W = (n^2+n-2)/2$.
- $|B-W| = n-2$.

So we're back to $|B-W| = 0$ for even $n$ and $n-2$ for odd $n$. The issue is that to keep white connected, "high" rows need a white cell, which costs.

Can we do better by having a different pattern? Let me think about whether we can have "high" rows with more black and still keep white connected.

**Idea: Instead of alternating every row, use a different pattern.**

What if we have more "high" rows than "low" rows? The constraint is that consecutive rows must alternate between low and high. So we can't have two consecutive high rows or two consecutive low rows.

But what if we have "medium" rows that are neither low nor high?

A "medium" row has $k$ with $1 \leq k \leq n-3$. But then for a medium row adjacent to a low row ($k = 0$):
- $\min(k_{med}, k_{low}) = 0 \leq 0$ ✓
- $\max(k_{med}, k_{low}) = k_{med} \leq n-3 < n-2$ ✗!

So a medium row adjacent to a low row violates the all-white constraint. Similarly, a medium row adjacent to a high row:
- $\min(k_{med}, k_{high}) = k_{med} \geq 1 > 0$ ✗!

So medium rows can't be adjacent to either low or high rows. Two medium rows adjacent to each other:
- $\min(k_1, k_2) \geq 1 > 0$ ✗ (if both $\geq 1$).

So medium rows can't be adjacent to anything! This means the staircase construction only allows low and high rows, and they must alternate.

Wait, I think I was too restrictive. Let me reconsider. A "medium" row with $k = 1$ adjacent to a "low" row with $k = 0$:
- $\min(1, 0) = 0 \leq 0$ ✓
- $\max(1, 0) = 1$. Need $\geq n-2$. For $n \geq 4$, $1 < n-2$ ✗.

So for $n \geq 4$, this fails. For $n = 3$: $\max(1, 0) = 1 \geq 1 = n-2$ ✓. So for $n = 3$, medium rows are possible.

For general $n \geq 4$, the staircase only allows alternating low ($k \leq 0$) and high ($k \geq n-2$) rows. And to maximize imbalance, we use $k = 0$ and $k = n-2$.

But this gives $|B-W| = 0$ for even $n$ and $n-2$ for odd $n$.

**Can we do better with a non-staircase pattern?**

The staircase has a single color boundary per row. What if we allow multiple boundaries per row?

**Construction: "Two boundaries per row".**

Consider a row with black in columns 0 to $a-1$ and columns $b$ to $n-1$, white in columns $a$ to $b-1$. This creates a white "stripe" in the middle of the row.

This is more flexible. Let me think about what constraints this gives.

Actually, this is getting very complex. Let me think about the problem from a higher level.

**Let me think about the problem as a graph theory problem.**

The grid graph $G$ has $n^2$ vertices. We partition vertices into $B$ and $W$, both connected, with no $2 \times 2$ monochromatic subgrid. Maximize $|B| - |W|$.

The no-$2\times2$-monochromatic condition is equivalent to: the "complement" of each color doesn't contain a $2 \times 2$ solid block. 

Actually, let me think about it in terms of the "boundary" between $B$ and $W$.

In a planar graph, if both $B$ and $W$ are connected, the boundary between them is a single simple path (or cycle). In the grid, this boundary is a path in the dual graph.

The no-$2\times2$-monochromatic condition means: the boundary passes through every $2 \times 2$ block. In other words, every $2 \times 2$ block is "cut" by the boundary.

A $2 \times 2$ block is cut by the boundary iff not all 4 cells are the same color. So the boundary must visit every $2 \times 2$ block.

In the dual graph, the $2 \times 2$ blocks correspond to the vertices of the dual of the grid graph (which is also a grid, of size $(n-1) \times (n-1)$). The boundary path must visit every vertex of this dual grid.

Wait, that's not quite right. The boundary is a path in the dual graph, and it must "touch" every $2 \times 2$ block. A $2 \times 2$ block is touched by the boundary if the boundary passes through one of its 4 edges (the edges between the 4 cells of the block).

Hmm, actually, a $2 \times 2$ block has 4 internal edges (the edges between its 4 cells). The boundary passes through the block if it uses at least one of these internal edges. But the boundary could also pass along the outer edges of the block without entering it.

Let me think more carefully. A $2 \times 2$ block at position $(i,j)$ consists of cells $(i,j), (i,j+1), (i+1,j), (i+1,j+1)$. It's monochromatic iff all 4 cells are the same color. The boundary between $B$ and $W$ doesn't pass through any internal edge of this block iff all 4 cells are the same color. So the block is non-monochromatic iff the boundary passes through at least one internal edge of the block.

The internal edges of the block at $(i,j)$ are:
- Horizontal: between $(i,j)$ and $(i,j+1)$, and between $(i+1,j)$ and $(i+1,j+1)$.
- Vertical: between $(i,j)$ and $(i+1,j)$, and between $(i,j+1)$ and $(i+1,j+1)$.

These are 4 edges. In the dual graph, these 4 edges correspond to 4 dual edges that form a cycle around the dual vertex at position $(i+0.5, j+0.5)$.

The boundary path must use at least one of these 4 dual edges for every $2 \times 2$ block. In other words, the boundary path must be incident to every dual vertex (of the $(n-1) \times (n-1)$ dual grid).

So the boundary is a path in the dual graph that is incident to every vertex of the $(n-1) \times (n-1)$ dual grid. This is a path that "dominates" all vertices of the dual grid.

Wait, "incident to every vertex" means the path passes through or adjacent to every vertex. Actually, a dual edge is incident to a dual vertex if it's one of the edges connected to that vertex. The boundary path uses some dual edges. A dual vertex is "covered" if at least one of its incident dual edges is in the boundary path.

So the boundary path must cover all $(n-1)^2$ dual vertices. This is a path in the dual grid graph that is a "dominating path" — every vertex is either on the path or adjacent to a vertex on the path.

Hmm wait, let me reconsider. The dual edges used by the boundary are edges that separate a black cell from a white cell. A dual vertex (corresponding to a $2 \times 2$ block) is covered if at least one of its 4 incident dual edges is in the boundary. This means at least one of the 4 internal edges of the $2 \times 2$ block separates black from white, which means the block is not monochromatic. ✓

So the problem reduces to: find a path in the dual grid graph (of size $(n-1) \times (n-1)$) that dominates all vertices, and the path corresponds to a valid boundary between two connected regions.

The length of the boundary path determines $|B - W|$ in some way. Actually, the relationship between the boundary and $|B - W|$ is not direct. The boundary is a path that separates $B$ from $W$, and $|B - W|$ depends on how much area is on each side.

Hmm, this dual graph approach is interesting but the relationship between the boundary path and $|B - W|$ is not straightforward. Let me think differently.

**Let me try to think about upper bounds more carefully.**

Consider the grid. Every $2 \times 2$ subgrid has both colors. Let's count the number of "color changes" along rows and columns.

For each row $i$, let $r_i$ = number of color changes between consecutive cells (i.e., number of $j$ where cell $(i,j) \neq$ cell $(i,j+1)$). Similarly, for each column $j$, let $c_j$ = number of color changes between consecutive cells.

The total number of color changes is $R + C$ where $R = \sum r_i$ and $C = \sum c_j$.

Each $2 \times 2$ subgrid has both colors, which means... hmm, this doesn't directly give a bound on $R + C$.

Let me think about it differently.

**Approach: Think about the "discrepancy" of the coloring.**

The discrepancy is $|B - W|$. We want to maximize this.

Consider the sum $S = \sum_{i,j} (-1)^{i+j} \cdot x_{ij}$ where $x_{ij} = 1$ if black, $-1$ if white. This is a different quantity.

Actually, let me think about a direct approach.

**Let me try to find the optimal construction by considering the dual problem.**

We want to minimize $W$ (assuming $B > W$) subject to:
1. $W$ is connected.
2. $B$ is connected.
3. Every $2 \times 2$ has at least one white cell.

Condition 3 means $W$ is a "hitting set" for all $2 \times 2$ subgrids. 

The minimum hitting set (without connectivity) for $2 \times 2$ subgrids: place white cells at positions $(2i, 2j)$ for $0 \leq i \leq \lfloor(n-1)/2\rfloor$, $0 \leq j \leq \lfloor(n-1)/2\rfloor$. This gives $\lceil n/2 \rceil^2$ cells... wait, that's not right.

Actually, a white cell at $(i, j)$ covers the $2 \times 2$ subgrids with top-left at $(i-1, j-1), (i-1, j), (i, j-1), (i, j)$. To cover all $(n-1)^2$ subgrids, we can place white cells at positions $(2i+1, 2j+1)$ for $0 \leq i, j$ with $2i+1 \leq n-1$ and $2j+1 \leq n-1$. This gives $\lfloor n/2 \rfloor^2$ cells, each covering 4 subgrids. But the subgrids at the edges might not be covered.

Hmm, let me think more carefully. The subgrids have top-left corners at $(i, j)$ for $0 \leq i \leq n-2, 0 \leq j \leq n-2$. A white cell at $(r, c)$ covers subgrids with top-left at $(r-1, c-1), (r-1, c), (r, c-1), (r, c)$ (those that are valid).

To cover all subgrids with minimum cells, we can use a grid-like placement. Place white cells at $(1, 1), (1, 3), (3, 1), (3, 3), \ldots$, i.e., at odd positions. Each covers 4 subgrids. The number of such cells is $\lfloor n/2 \rfloor^2$ (for $n$ even, $(n/2)^2$; for $n$ odd, $((n-1)/2)^2$).

But this doesn't cover subgrids at the edges. For example, the subgrid at $(0, 0)$ is covered by cells at $(0,0), (0,1), (1,0), (1,1)$. If we place white at $(1,1)$, it covers subgrid $(0,0)$. ✓

The subgrid at $(n-2, n-2)$ is covered by cells at $(n-2,n-2), (n-2,n-1), (n-1,n-2), (n-1,n-1)$. If $n$ is even, the nearest white cell is at $(n-2, n-2)$... but $n-2$ is even, not odd. So we'd need a white cell at $(n-1, n-1)$, which is at an odd position if $n$ is even. ✓

Actually, for $n$ even, placing white at all $(2i+1, 2j+1)$ for $0 \leq i, j \leq n/2 - 1$ gives $(n/2)^2$ cells. Each covers 4 subgrids. Total subgrids covered: up to $4 \cdot (n/2)^2 = n^2$. But there are only $(n-1)^2$ subgrids. Some are covered multiple times. Let me check if all are covered.

Subgrid at $(0, 0)$: covered by white at $(1, 1)$. ✓
Subgrid at $(0, 1)$: covered by white at $(1, 1)$ or $(1, 2)$. $(1, 2)$ is even, not placed. $(1, 1)$ covers subgrid $(0, 0), (0, 1), (1, 0), (1, 1)$. So yes, $(0, 1)$ is covered. ✓
Subgrid at $(n-2, n-2)$: covered by white at $(n-1, n-1)$ (if $n$ even, $n-1$ is odd). ✓

So for $n$ even, $\lfloor n/2 \rfloor^2 = (n/2)^2$ white cells suffice to hit all $2 \times 2$ subgrids. But they're not connected!

For $n = 10$: $(10/2)^2 = 25$ white cells. $B = 100 - 25 = 75$. $|B - W| = 50$. But white is not connected.

To make white connected, we need additional cells. How many?

The white cells are at odd positions $(1,1), (1,3), (1,5), (1,7), (3,1), (3,3), \ldots$ They form a grid with spacing 2. To connect them, we need to add cells between them.

Two adjacent white cells in the grid, say $(1,1)$ and $(1,3)$, are separated by $(1,2)$. Adding $(1,2)$ as white connects them. Similarly for vertical connections.

To connect the $(n/2)^2$ white cells into a connected component, we need to add cells between them. The white cells form a $(n/2) \times (n/2)$ grid (with spacing 2). To make this connected, we need to add horizontal and vertical connectors.

A spanning tree of the $(n/2) \times (n/2)$ grid has $(n/2)^2 - 1$ edges. Each edge requires 1 connector cell. So we need $(n/2)^2 - 1$ additional cells.

Total white: $(n/2)^2 + (n/2)^2 - 1 = 2(n/2)^2 - 1 = n^2/2 - 1$.

$B = n^2 - W = n^2/2 + 1$. $|B - W| = 2$.

That's terrible! The connectors cost too much.

**Better approach: use a path instead of a grid.**

Instead of placing white cells in a grid and connecting them, place them in a path that naturally hits every $2 \times 2$ subgrid.

A path in the grid that hits every $2 \times 2$ subgrid: this is a "dominating path" for the $2 \times 2$ subgrids.

What's the shortest such path? 

A $2 \times 2$ subgrid at $(i,j)$ is hit by any cell in $\{(i,j), (i,j+1), (i+1,j), (i+1,j+1)\}$. A path that visits one cell in each $2 \times 2$ subgrid would work, but cells can cover multiple subgrids.

**The "snake" path:**

Consider a boustrophedon path that covers every other row:
- Row 0: left to right (all $n$ cells).
- Row 1: just the rightmost cell (to connect to row 2).
- Row 2: right to left (all $n$ cells).
- Row 3: just the leftmost cell.
- Row 4: left to right.
- ...

This path visits all cells in even rows and one cell in odd rows. Total cells: $\lceil n/2 \rceil \cdot n + \lfloor n/2 \rfloor \cdot 1 = \lceil n/2 \rceil \cdot n + \lfloor n/2 \rfloor$.

For $n = 10$: $5 \cdot 10 + 5 = 55$ cells. Way too many.

But we don't need to visit ALL cells in even rows. We just need to hit every $2 \times 2$ subgrid. 

A $2 \times 2$ subgrid at rows $i, i+1$ is hit if the path visits any cell in rows $i$ or $i+1$ at a column within the subgrid. If the path covers all of row $i$ (every column), then all subgrids in rows $i, i+1$ and rows $i-1, i$ are hit.

So if we cover every other row fully, all subgrids are hit. That's $\lceil n/2 \rceil \cdot n$ cells. For $n = 10$: $50$ cells. Still too many.

**Can we do better by covering rows partially?**

If we cover row $i$ at columns $0, 2, 4, \ldots$ (every other column), then subgrids at rows $i-1, i$ and $i, i+1$ with even $j$ are hit (by cell $(i, j)$), and subgrids with odd $j$ are hit by cell $(i, j+1)$. So covering every other column in a row hits all subgrids involving that row.

So: cover every other row, and in each covered row, cover every other column. Total: $\lceil n/2 \rceil \cdot \lceil n/2 \rceil$ cells. For $n = 10$: $25$ cells. Same as the grid placement!

But these cells aren't connected. We need to connect them.

**Optimal connected hitting set:**

The question is: what's the minimum connected set of cells that hits every $2 \times 2$ subgrid?

This is related to the concept of a "connected dominating set" in the grid graph, but with a different domination rule (dominating $2 \times 2$ blocks rather than vertices).

Let me think about this more carefully.

**Lower bound on connected hitting set:**

Every $2 \times 2$ subgrid must be hit. There are $(n-1)^2$ subgrids. A connected set of $k$ cells can hit at most... well, each cell hits at most 4 subgrids, but the total is limited by the structure.

A connected set of $k$ cells in a grid can hit at most $4k$ subgrids (each cell hits at most 4). But for a path-like structure, the number of subgrids hit is roughly $2k$ (since adjacent cells share subgrids).

For a path of $k$ cells, the number of distinct $2 \times 2$ subgrids hit is at most $2k + 2$ (approximately), because each new cell in the path adds at most 2 new subgrids (since it shares 2 subgrids with the previous cell).

Wait, that's not quite right. Let me think more carefully.

A cell at $(i, j)$ hits subgrids with top-left at $(i-1, j-1), (i-1, j), (i, j-1), (i, j)$. If the path goes from $(i, j)$ to $(i, j+1)$, the new cell hits subgrids $(i-1, j), (i-1, j+1), (i, j), (i, j+1)$. The subgrids $(i-1, j)$ and $(i, j)$ were already hit by $(i, j)$. So the new subgrids are $(i-1, j+1)$ and $(i, j+1)$: 2 new subgrids.

If the path goes from $(i, j)$ to $(i+1, j)$, the new cell hits $(i, j-1), (i, j), (i+1, j-1), (i+1, j)$. Already hit: $(i, j-1)$ and $(i, j)$. New: $(i+1, j-1)$ and $(i+1, j)$: 2 new subgrids.

So each step in the path adds at most 2 new subgrids. The first cell hits 4 subgrids (or fewer if on the boundary). So a path of $k$ cells hits at most $4 + 2(k-1) = 2k + 2$ subgrids.

We need to hit $(n-1)^2$ subgrids. So $2k + 2 \geq (n-1)^2$, giving $k \geq ((n-1)^2 - 2) / 2 = (n^2 - 2n - 1) / 2$.

For $n = 10$: $k \geq (81 - 2)/2 = 79/2 = 39.5$, so $k \geq 40$.
For $n = 11$: $k \geq (100 - 2)/2 = 49$.

But this is a lower bound for a path. A general connected set (not a path) might do better. A tree-like structure can branch and cover more subgrids.

For a tree of $k$ cells, the number of subgrids hit is at most $4 + 2(k-1) = 2k + 2$ (same as a path, since each new cell in a tree also adds at most 2 new subgrids when attached to an existing cell).

Wait, actually, if a new cell is attached to an existing cell, it shares 2 subgrids with the existing cell (the 2 subgrids that contain both cells). But if the new cell is also adjacent to another existing cell, it might share more. So the bound $2k + 2$ is an upper bound for any connected set.

Actually, let me reconsider. When we add a new cell to a connected set, it's adjacent to at least one existing cell. The new cell hits 4 subgrids, but some are already hit. The number of already-hit subgrids depends on how many existing neighbors the new cell has.

If the new cell has 1 existing neighbor: it shares 2 subgrids with that neighbor, so 2 new subgrids.
If the new cell has 2 existing neighbors (e.g., the cell between two existing cells): it shares 2 subgrids with each, but some overlap. Let's say it shares 3 subgrids total, so 1 new subgrid.
If the new cell has 3 existing neighbors: shares 4 subgrids, 0 new.
If the new cell has 4 existing neighbors: shares 4 subgrids, 0 new.

So to maximize the number of subgrids hit, we want each new cell to have exactly 1 existing neighbor (i.e., the connected set is a path). This gives $2k + 2$ subgrids for $k$ cells.

But wait, for a path, the first cell hits 4 subgrids (if interior), and each subsequent cell adds 2. But the last cell might add fewer if it's on the boundary. Also, the first cell might hit fewer than 4 if on the boundary.

For the lower bound: we need $2k + 2 \geq (n-1)^2$, so $k \geq ((n-1)^2 - 2)/2$.

But we also need the complement (black) to be connected. This adds additional constraints.


