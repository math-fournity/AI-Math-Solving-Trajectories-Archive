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
  <problem_id>polymath_00921</problem_id>
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

Let $k \ge 1$ be an integer. Determine the smallest positive integer $n$ such that some cells on an $n \times n$ board can be painted black so that in each row and in each column there are exactly $k$ black cells, and furthermore, the black cells do not share a side or a vertex with another black square. Let $n(k)$ be this smallest integer. Compute the sum $\sum_{k=1}^{50} n(k)$.

## Standard Solution

The original solution determines that the smallest $n$ for a given $k$ is $n(k) = 2k + 1$. To provide a single numeric answer, we sum these values for $k=1$ to $k=50$:
$\sum_{k=1}^{50} (2k + 1) = 2 \frac{50(51)}{2} + 50 = 2550 + 50 = 2600$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We need to find the smallest positive integer $n$ such that we can place black cells on an $n \times n$ board where:
1. Each row has exactly $k$ black cells
2. Each column has exactly $k$ black cells
3. No two black cells share a side or a vertex (i.e., no two black cells are adjacent horizontally, vertically, or diagonally)

This means any two black cells must be at least distance 2 apart in both row and column (Chebyshev distance ≥ 2, actually they just can't be in adjacent cells including diagonals, so if one black cell is at $(r,c)$, no other black cell can be at $(r',c')$ where $|r-r'| \leq 1$ and $|c-c'| \leq 1$).

Let me think about this. The condition "no two black cells share a side or vertex" means that for any two black cells at positions $(r_1, c_1)$ and $(r_2, c_2)$, we need $|r_1 - r_2| \geq 2$ or $|c_1 - c_2| \geq 2$. Actually more precisely, they can't be adjacent, so we need: NOT ($|r_1-r_2| \leq 1$ AND $|c_1-c_2| \leq 1$) for any two distinct black cells. This means for any two black cells, $|r_1-r_2| \geq 2$ or $|c_1-c_2| \geq 2$.

This is equivalent to saying the black cells form an independent set in the king graph.

Let me think about lower bounds first.

**Lower bound approach:**

Consider the rows. Each row has $k$ black cells. In a single row, the $k$ black cells must be separated by at least one white cell (since they can't share a side). So in a row of length $n$, we need at least $k + (k-1) = 2k-1$ cells. So $n \geq 2k-1$.

But also, consider two consecutive rows. If row $i$ has a black cell at column $c$, then row $i+1$ cannot have a black cell at columns $c-1, c, c+1$. So the black cells in row $i$ "block" certain columns in row $i+1$.

Let me think more carefully. In row $i$, there are $k$ black cells at positions $c_1 < c_2 < \cdots < c_k$. These block columns $c_1-1, c_1, c_1+1, c_2-1, c_2, c_2+1, \ldots, c_k-1, c_k, c_k+1$ in row $i+1$ (and row $i-1$).

Since $c_1 < c_2 < \cdots < c_k$ and consecutive ones differ by at least 2, the blocked columns form a set. The number of blocked columns is at most $3k$ but could be less due to overlaps. The minimum number of blocked columns occurs when the $c_i$ are as close together as possible, i.e., $c_i = c_1 + 2(i-1)$. Then the blocked columns are $c_1-1, c_1, c_1+1, c_1+1, c_1+2, c_1+3, \ldots$ — wait, let me be more careful.

If $c_i = a + 2(i-1)$ for $i = 1, \ldots, k$, then the blocked columns are $\{a+2(i-1)-1, a+2(i-1), a+2(i-1)+1 : i=1,\ldots,k\} = \{a-1, a, a+1, a+1, a+2, a+3, a+3, a+4, a+5, \ldots\}$.

Actually, the blocked set is $\{a-1\} \cup \{a, a+1\} \cup \{a+1, a+2, a+3\} \cup \{a+3, a+4, a+5\} \cup \ldots$

Hmm, let me just compute: for $c_i = a + 2(i-1)$, the blocked columns are:
- $i=1$: $a-1, a, a+1$
- $i=2$: $a+1, a+2, a+3$
- $i=3$: $a+3, a+4, a+5$
- $i=4$: $a+5, a+6, a+7$

So the blocked set is $\{a-1, a, a+1, a+2, a+3, a+4, a+5, \ldots, a+2k-2, a+2k-1\}$, which is $\{a-1, a, a+1, \ldots, a+2k-1\}$, a contiguous block of $2k+1$ columns.

So in the next row, the available columns are those not in this blocked set. If the board has $n$ columns, the number of available columns is $n - (2k+1)$ (if the blocked set fits within the board). For the next row to have $k$ black cells, we need the available columns to support $k$ non-adjacent black cells, which requires at least $2k-1$ available columns.

So $n - (2k+1) \geq 2k-1$, giving $n \geq 4k$.

Wait, but this is only if the blocked set is contiguous and fits within the board. Let me reconsider.

Actually, the blocked set might not be exactly $2k+1$ columns. Let me reconsider. The minimum number of blocked columns is when the black cells are as tightly packed as possible. But we also need to consider that the black cells in the next row need to be placed in the unblocked columns, and they also need to be non-adjacent to each other.

Let me think about this differently. 

Actually, let me think about a pattern. Consider coloring the board like a chessboard but with a period-2 pattern in both directions. Actually, the condition is about king moves, so let me think about it as a coloring problem.

If we use a 2-coloring (checkerboard), black cells on the same color are at least distance 2 apart in Chebyshev distance only if... no, that's not quite right. Two cells of the same color in a checkerboard can be at Chebyshev distance 1 (e.g., $(0,0)$ and $(1,1)$ are the same color but diagonally adjacent).

So we need a finer coloring. If we use a coloring where cell $(r,c)$ gets color based on $(r \mod 2, c \mod 2)$, there are 4 colors. Two cells of the same color have $|r_1-r_2|$ even and $|c_1-c_2|$ even, so they differ by at least 2 in each coordinate if they're different cells. Wait, no — $(0,0)$ and $(0,2)$ have the same color and $|c_1-c_2| = 2 \geq 2$, so they're fine. $(0,0)$ and $(2,0)$ similarly fine. $(0,0)$ and $(2,2)$ also fine. So any two cells of the same color (in this 4-coloring) are at Chebyshev distance $\geq 2$. 

So if we place all black cells on a single color class of this 4-coloring, the non-adjacency condition is automatically satisfied. Each color class has about $n^2/4$ cells. In each row, a color class has about $n/2$ cells (every other column). In each column, about $n/2$ cells.

So if we pick one color class, say cells where $r$ is even and $c$ is even, then in each even row we can place black cells in even columns, and in each odd row we can't place any (since we're restricted to even $r$ and even $c$). But we need every row to have exactly $k$ black cells. So a single color class doesn't work directly.

We need to use multiple color classes but ensure no two black cells from different color classes are adjacent either. But cells from different color classes can be adjacent (e.g., $(0,0)$ color $(0,0)$ and $(0,1)$ color $(0,1)$ are adjacent). So we can't freely mix color classes.

Hmm, let me think about this more carefully.

Actually, the key insight is: the non-adjacency condition (no two black cells at Chebyshev distance 1) means that the black cells form an independent set in the king graph. 

Let me think about what configurations work. 

Consider the pattern where we place black cells at positions $(r, c)$ where $r \equiv 0 \pmod{2}$ and $c$ is in some set, and $r \equiv 1 \pmod{2}$ and $c$ is in a shifted set. But we need to ensure non-adjacency between rows.

Let me think about a specific construction. Consider placing black cells in a "staggered" pattern:
- In even rows (0, 2, 4, ...): place black cells at columns 0, 2, 4, ..., 2(k-1) — that's $k$ cells, needing $n \geq 2k-1$.
- In odd rows (1, 3, 5, ...): place black cells at columns 1, 3, 5, ..., 2k-1 — that's $k$ cells, needing $n \geq 2k$.

But wait, row 0 has black at columns 0, 2, 4, ... and row 1 has black at columns 1, 3, 5, .... Are these non-adjacent? Cell $(0, 0)$ and $(1, 1)$: $|r_1-r_2| = 1$, $|c_1-c_2| = 1$, so they ARE diagonally adjacent. This violates the condition!

So we can't have consecutive rows both with black cells in this staggered pattern. We need to separate rows that have black cells.

What if we use every other row? 
- Rows 0, 2, 4, ...: place black cells
- Rows 1, 3, 5, ...: no black cells

But then odd rows have 0 black cells, not $k$. So this doesn't work either.

So we need every row to have $k$ black cells, but consecutive rows can't have black cells in adjacent columns. Let me think about what's possible.

If row $i$ has black cells at columns $c_1 < c_2 < \cdots < c_k$ (with $c_{j+1} \geq c_j + 2$), then row $i+1$ can have black cells only at columns not in $\{c_j - 1, c_j, c_j + 1 : j = 1, \ldots, k\}$.

Let me think about the problem more carefully with small cases.

**Case $k = 1$:** We need each row and each column to have exactly 1 black cell, and no two black cells adjacent (including diagonally). This is like placing $n$ non-attacking kings on an $n \times n$ board, one per row and one per column. 

For $n = 1$: trivially works. So $n(1) = 1$.

Wait, let me check. $n = 1$, $k = 1$: the single cell is black. Each row (1 row) has 1 black cell. Each column (1 column) has 1 black cell. No adjacency issue. So $n(1) = 1$.

**Case $k = 2$:** Each row and column has exactly 2 black cells, no two adjacent (including diagonally).

Let me try $n = 4$. We need 2 black cells per row and per column, total 8 black cells. The non-adjacency condition is quite restrictive.

In a $4 \times 4$ board, can we do it? Let me try:
- Row 0: columns 0, 2 (or 0, 3 or 1, 3)
- Row 1: must avoid columns adjacent to row 0's black cells.

If row 0 has black at 0, 2: blocked columns for row 1 are {-1,0,1} ∪ {1,2,3} = {0,1,2,3}. So row 1 has no available columns. Doesn't work.

If row 0 has black at 0, 3: blocked columns for row 1 are {-1,0,1} ∪ {2,3,4} = {0,1,2,3}. No available columns. Doesn't work.

If row 0 has black at 1, 3: blocked columns for row 1 are {0,1,2} ∪ {2,3,4} = {0,1,2,3}. No available columns. Doesn't work.

So $n = 4$ doesn't work for $k = 2$.

Let me try $n = 5$. Row 0: black at 0, 2. Blocked for row 1: {0,1,2,3}. Available: {4}. Only 1 column, need 2. 

Row 0: black at 0, 3. Blocked for row 1: {0,1,2,3,4}. Available: none. Worse.

Row 0: black at 0, 4. Blocked for row 1: {0,1,3,4,5}→{0,1,3,4}. Available: {2}. Only 1.

Row 0: black at 1, 4. Blocked for row 1: {0,1,2,3,4,5}→{0,1,2,3,4}. Available: none.

Hmm, $n = 5$ seems hard too. Let me try $n = 6$.

Row 0: black at 0, 2. Blocked for row 1: {0,1,2,3}. Available: {4,5}. Need 2 non-adjacent: only 4 and 5 are adjacent, so can't place 2. 

Row 0: black at 0, 3. Blocked for row 1: {0,1,2,3,4}. Available: {5}. Only 1.

Row 0: black at 0, 4. Blocked for row 1: {0,1,3,4,5}. Available: {2}. Only 1.

Row 0: black at 0, 5. Blocked for row 1: {0,1,4,5,6}→{0,1,4,5}. Available: {2,3}. Adjacent, can't place 2 non-adjacent.

Row 0: black at 1, 4. Blocked for row 1: {0,1,2,3,4,5}. Available: none.

Row 0: black at 1, 5. Blocked for row 1: {0,1,2,4,5,6}→{0,1,2,4,5}. Available: {3}. Only 1.

Row 0: black at 2, 5. Blocked for row 1: {1,2,3,4,5,6}→{1,2,3,4,5}. Available: {0}. Only 1.

So $n = 6$ doesn't work for $k = 2$ either? Let me try $n = 7$.

Row 0: black at 0, 2. Blocked for row 1: {0,1,2,3}. Available: {4,5,6}. Need 2 non-adjacent from {4,5,6}: can pick 4,6. So row 1: black at 4, 6.

Now row 1 has black at 4, 6. Blocked for row 2: {3,4,5,5,6,7}→{3,4,5,6,7}→{3,4,5,6}. Available: {0,1,2}. Need 2 non-adjacent from {0,1,2}: can pick 0,2. So row 2: black at 0, 2.

Row 2 same as row 0. Blocked for row 3: {0,1,2,3}. Available: {4,5,6}. Row 3: black at 4, 6. Same as row 1.

Row 3 same as row 1. Blocked for row 4: {3,4,5,6}. Available: {0,1,2}. Row 4: black at 0, 2.

Row 5: black at 4, 6.
Row 6: black at 0, 2.

Let me check columns:
- Column 0: rows 0, 2, 4, 6 → 4 black cells. Need 2. Too many!

So this pattern gives too many in some columns. We need each column to have exactly 2.

Let me think about this differently. We need a $n \times n$ 0-1 matrix with:
- Each row sum = $k$
- Each column sum = $k$
- No two 1s are at Chebyshev distance 1

This is a combinatorial design problem. Let me think about it as a kind of "independent set" design.

Let me think about the structure more carefully. The condition means that if $(r_1, c_1)$ and $(r_2, c_2)$ are both black, then $|r_1 - r_2| \geq 2$ or $|c_1 - c_2| \geq 2$.

Equivalently, for any $2 \times 2$ sub-board, at most one cell can be black.

Now, consider partitioning the $n \times n$ board into $2 \times 2$ blocks. There are $\lfloor n/2 \rfloor^2$ such blocks (if $n$ is even, exactly $(n/2)^2$). Each block can have at most 1 black cell. So the total number of black cells is at most $\lfloor n/2 \rfloor^2$... wait, that's not quite right because the $2 \times 2$ blocks overlap.

Actually, let me think about it differently. Consider the cells $(r, c)$ where $r$ and $c$ have the same parity (both even or both odd), vs. cells where they have different parity. 

Hmm, let me think about a cleaner approach.

Consider the mapping $(r, c) \to (\lfloor r/2 \rfloor, \lfloor c/2 \rfloor)$. This maps the $n \times n$ board to a $\lceil n/2 \rceil \times \lceil n/2 \rceil$ grid of $2 \times 2$ blocks (with possibly incomplete blocks at the edges). Each $2 \times 2$ block can contain at most 1 black cell (since any two cells in a $2 \times 2$ block are at Chebyshev distance $\leq 1$). 

So the total number of black cells $\leq \lceil n/2 \rceil^2$. But the total number of black cells is $nk$ (since each of $n$ rows has $k$). So $nk \leq \lceil n/2 \rceil^2$.

If $n$ is even: $nk \leq (n/2)^2 = n^2/4$, so $k \leq n/4$, i.e., $n \geq 4k$.
If $n$ is odd: $nk \leq ((n+1)/2)^2 = (n+1)^2/4$, so $k \leq (n+1)^2/(4n)$.

For $n$ odd, $k \leq (n+1)^2/(4n) = (n^2 + 2n + 1)/(4n) = n/4 + 1/2 + 1/(4n)$. So $k \leq \lfloor n/4 + 1/2 + 1/(4n) \rfloor$.

For $n = 4k - 1$ (odd): $k \leq (4k-1)/4 + 1/2 + 1/(4(4k-1)) = k - 1/4 + 1/2 + 1/(16k-4) = k + 1/4 + 1/(16k-4)$. So $k \leq k + \text{something positive}$, which is always true. So $n = 4k - 1$ might work from this bound.

Wait, let me recalculate. For $n = 4k - 1$ (odd):
$\lceil n/2 \rceil = \lceil (4k-1)/2 \rceil = 2k$.
So $nk \leq (2k)^2 = 4k^2$, i.e., $(4k-1)k \leq 4k^2$, i.e., $4k^2 - k \leq 4k^2$, i.e., $-k \leq 0$. Always true.

For $n = 4k - 2$ (even):
$(n/2)^2 = (2k-1)^2 = 4k^2 - 4k + 1$.
$nk = (4k-2)k = 4k^2 - 2k$.
Need $4k^2 - 2k \leq 4k^2 - 4k + 1$, i.e., $2k \leq 1$, i.e., $k \leq 1/2$. So for $k \geq 1$, $n = 4k - 2$ doesn't work.

For $n = 4k - 3$ (odd):
$\lceil n/2 \rceil = \lceil (4k-3)/2 \rceil = 2k - 1$.
$(2k-1)^2 = 4k^2 - 4k + 1$.
$nk = (4k-3)k = 4k^2 - 3k$.
Need $4k^2 - 3k \leq 4k^2 - 4k + 1$, i.e., $k \leq 1$. So only $k = 1$ works.

So from this simple bound:
- For even $n$: need $n \geq 4k$.
- For odd $n$: need $n \geq 4k - 1$ (for $k \geq 2$).

But this is just a necessary condition from the $2 \times 2$ block argument. We also need the row and column sum conditions, which are more restrictive.

Let me think about a better lower bound. 

Actually, let me think about this more carefully. The $2 \times 2$ block argument gives us that the total number of black cells $\leq \lceil n/2 \rceil^2$. But we also need each row to have $k$ and each column to have $k$.

Let me think about a different approach. Consider two consecutive rows, say rows $r$ and $r+1$. The black cells in row $r$ are at columns $c_1, \ldots, c_k$ (with gaps $\geq 2$). The black cells in row $r+1$ are at columns $d_1, \ldots, d_k$ (with gaps $\geq 2$). The non-adjacency between rows means $|c_i - d_j| \geq 2$ for all $i, j$.

So the sets $\{c_1, \ldots, c_k\}$ and $\{d_1, \ldots, d_k\}$ must be "2-separated": every element of one set is at distance $\geq 2$ from every element of the other.

Now, the $c_i$ are $k$ values in $\{0, \ldots, n-1\}$ with gaps $\geq 2$, so they span at least $2k - 1$ columns. The "exclusion zone" around them (columns at distance $\leq 1$) has size at least... well, the $c_i$ with gaps exactly 2 give an exclusion zone of $2k + 1$ consecutive columns (as computed earlier). The $d_j$ must all be outside this exclusion zone and have gaps $\geq 2$.

If the exclusion zone has size $E$, then the available columns have size $n - E$, and we need to place $k$ non-adjacent values in them, requiring $n - E \geq 2k - 1$.

The minimum $E$ is achieved when the $c_i$ are as tightly packed as possible (gaps of 2), giving $E = 2k + 1$. But we also need to account for boundary effects.

Actually, let me think about it more carefully. If $c_1, \ldots, c_k$ are in $\{0, \ldots, n-1\}$ with $c_{i+1} \geq c_i + 2$, the exclusion zone is $\bigcup_i [c_i - 1, c_i + 1]$. 

The size of the exclusion zone is minimized when the $c_i$ are as close together as possible. With $c_{i+1} = c_i + 2$, the exclusion zone is $[c_1 - 1, c_k + 1] = [c_1 - 1, c_1 + 2(k-1) + 1] = [c_1 - 1, c_1 + 2k - 1]$, which has size $2k + 1$.

But this is only the size if the entire interval is within $\{0, \ldots, n-1\}$ (or we count the part within the board). If $c_1 = 0$, the exclusion zone within the board is $[0, 2k-1]$ (since $c_1 - 1 = -1$ is outside), which has size $2k$. If $c_1 = 1$, it's $[0, 2k]$, size $2k+1$. If $c_k = n-1$, the exclusion zone is $[n-1-2(k-1)-1, n-1+1] = [n-2k, n]$, within the board it's $[n-2k, n-1]$, size $2k$.

So the minimum exclusion zone size within the board is $2k$ (achieved when the black cells are pushed to one edge). Then the available columns have size $n - 2k$, and we need $n - 2k \geq 2k - 1$, i.e., $n \geq 4k - 1$.

But wait, we need this for EVERY pair of consecutive rows. And the configuration that minimizes the exclusion zone for one pair might not work for the next pair.

Let me think about whether $n = 4k - 1$ is achievable.

Actually, let me think about a construction. Consider $n = 4k - 1$. 

Hmm, let me think about specific small cases first to get intuition.

**$k = 1, n = 1$:** Works trivially. $n(1) = 1$.

**$k = 2$:** From the bound, $n \geq 4 \cdot 2 - 1 = 7$ (odd) or $n \geq 8$ (even). Let me check if $n = 7$ works.

We need a $7 \times 7$ board with 2 black cells per row and column, no two adjacent (including diagonally).

Let me try to construct one. I'll use the idea of two "interleaved" patterns.

Consider the following approach: think of the board as a $7 \times 7$ grid. We need to place 14 black cells (2 per row, 2 per column).

Let me try:
- Row 0: columns 0, 2
- Row 1: columns 4, 6
- Row 2: columns 0, 2 (same as row 0, but row 1 separates them, so no adjacency issue between rows 0 and 2)
- Row 3: columns 4, 6
- Row 4: columns 0, 2
- Row 5: columns 4, 6
- Row 6: columns 0, 2

Check column sums:
- Col 0: rows 0, 2, 4, 6 → 4 black cells. Need 2. ✗

This doesn't work because columns are unbalanced. We need each column to have exactly 2.

Let me think about this as a bipartite matching / design problem. We need a 0-1 matrix that is $k$-regular (both row and column sums = $k$) and has the non-adjacency property.

Let me think about it as follows. The non-adjacency condition means that in any $2 \times 2$ submatrix, at most one entry is 1. This is equivalent to saying the matrix is a "sparse" matrix with a specific structure.

Actually, I recall that this type of problem is related to "non-attacking kings" on a chessboard. Let me think about the structure.

Consider the "super-cell" approach: group the board into $2 \times 2$ blocks. Each block can have at most 1 black cell. If $n$ is even, we have $(n/2)^2$ blocks, and we need $nk$ black cells, so $nk \leq (n/2)^2$, giving $n \geq 4k$.

If $n$ is odd, say $n = 2m + 1$, we have $m^2$ complete $2 \times 2$ blocks plus some edge cells. The total number of "blocks" (including partial ones) is... actually, let me think about this differently.

For odd $n = 2m+1$, we can partition the board into $m^2$ full $2 \times 2$ blocks, $m$ full $2 \times 1$ blocks (in the last column), $m$ full $1 \times 2$ blocks (in the last row), and 1 single cell (corner). Each $2 \times 2$ block has at most 1 black cell, each $2 \times 1$ or $1 \times 2$ block has at most 1 black cell (since the two cells in a $2 \times 1$ block are vertically adjacent), and the single cell has at most 1. So the total is at most $m^2 + m + m + 1 = (m+1)^2 = \lceil n/2 \rceil^2$.

So for odd $n = 2m+1$: $nk \leq (m+1)^2$, i.e., $(2m+1)k \leq (m+1)^2$.

For $n = 4k - 1 = 2(2k-1) + 1$, so $m = 2k - 1$: $(4k-1)k \leq (2k)^2 = 4k^2$, i.e., $4k^2 - k \leq 4k^2$. True.

For $n = 4k - 3 = 2(2k-2) + 1$, so $m = 2k - 2$: $(4k-3)k \leq (2k-1)^2 = 4k^2 - 4k + 1$, i.e., $4k^2 - 3k \leq 4k^2 - 4k + 1$, i.e., $k \leq 1$. So only works for $k = 1$.

So the block bound gives $n \geq 4k - 1$ for $k \geq 2$ (and $n \geq 1$ for $k = 1$).

But is this bound tight? We also need the row and column sum conditions. Let me think about whether $n = 4k - 1$ is achievable for general $k$.

Let me try to construct a solution for $n = 4k - 1$.

Idea: Use a "cyclic" pattern. Consider the board as $\mathbb{Z}_n \times \mathbb{Z}_n$ (cyclic group). Place black cells at positions $(r, c)$ where $c \equiv f(r) \pmod{n}$ for some function, but we need $k$ cells per row.

Actually, let me think about a different construction. Consider placing black cells at positions $(r, c)$ where $c - r \equiv 2j \pmod{n}$ for $j = 0, 1, \ldots, k-1$, but we need to ensure the non-adjacency condition.

Hmm, this is getting complicated. Let me think about the problem from a higher level.

Let me consider the problem as a graph coloring / independent set problem. The king graph on the $n \times n$ board has vertices = cells and edges between cells at Chebyshev distance 1. We need an independent set that is $k$-regular in the bipartite sense (each row and column has exactly $k$ vertices in the independent set).

The independence number of the king graph on $n \times n$ is $\lceil n/2 \rceil^2$ (achieved by taking every other cell in both directions). We need $nk \leq \lceil n/2 \rceil^2$.

But we also need the regularity condition. Let me think about what patterns achieve both.

**Construction attempt for $n = 4k - 1$:**

Let me try a specific construction. Consider $n = 4k - 1$. Define the black cells as follows:

For each row $r$ (0-indexed), place black cells at columns:
$c \equiv 2r + 2j \pmod{n}$ for $j = 0, 1, \ldots, k-1$.

Wait, but we need the cells within a row to be non-adjacent (gap $\geq 2$), and cells in adjacent rows to be non-adjacent.

Within a row: the columns are $2r, 2r+2, 2r+4, \ldots, 2r+2(k-1) \pmod{n}$. The gaps are 2 (mod $n$), but we need to be careful about wraparound. If $n = 4k - 1$, then $2(k-1) = 2k - 2 < 4k - 1 = n$, so no wraparound within the row if $2r + 2(k-1) < n + 2r$... hmm, this depends on $r$.

Actually, let me not use modular arithmetic and think about it on the actual board.

Let me try a different approach. Think of the $n \times n$ board and place black cells in a "diagonal" pattern.

For $n = 4k - 1$, consider the following: divide the columns into two groups: "even-positioned" and "odd-positioned" (0-indexed). In even rows, use one group; in odd rows, use the other. But we need to be more careful.

Let me try yet another approach. Consider the $n \times n$ board with $n = 4k - 1$. 

Actually, let me try to think about this problem computationally for small $k$ to find the pattern.

**$k = 1$:** $n(1) = 1$ (as shown above).

Wait, actually for $k = 1$, the bound gives $n \geq 4(1) - 3 = 1$ (from the odd case with $k = 1$). And $n = 1$ works. So $n(1) = 1$.

**$k = 2$:** Bound gives $n \geq 7$. Let me try to construct a solution for $n = 7$.

I need a $7 \times 7$ 0-1 matrix with row and column sums = 2, and no two 1s in the same or adjacent $2 \times 2$ block.

Let me try to think of it as two permutation matrices (since row sum = column sum = 2, the matrix is the sum of two permutation matrices, by the Birkhoff-von Neumann theorem). But the non-adjacency condition constrains which permutations we can use.

Actually, the matrix being the sum of two permutation matrices means we can decompose the black cells into two sets, each forming a permutation (one black cell per row and per column). Let's call them $\sigma$ and $\tau$, so black cells are at $(r, \sigma(r))$ and $(r, \tau(r))$ for each row $r$.

The non-adjacency conditions:
1. Within a row: $|\sigma(r) - \tau(r)| \geq 2$ for all $r$.
2. Between adjacent rows: $|\sigma(r) - \sigma(r+1)| \geq 2$, $|\sigma(r) - \tau(r+1)| \geq 2$, $|\tau(r) - \sigma(r+1)| \geq 2$, $|\tau(r) - \tau(r+1)| \geq 2$ for all $r$.

So essentially, all 4 values $\sigma(r), \tau(r), \sigma(r+1), \tau(r+1)$ must be pairwise at distance $\geq 2$.

For $n = 7$, we need two permutations $\sigma, \tau$ of $\{0, 1, \ldots, 6\}$ such that:
- $|\sigma(r) - \tau(r)| \geq 2$ for all $r$
- For consecutive rows $r, r+1$: all of $\sigma(r), \tau(r), \sigma(r+1), \tau(r+1)$ are pairwise at distance $\geq 2$.

This means that in any two consecutive rows, the 4 column positions are pairwise at distance $\geq 2$. In $\{0, \ldots, 6\}$, we need 4 values pairwise at distance $\geq 2$. The minimum span for 4 such values is $0, 2, 4, 6$ (span 6, which is exactly $n - 1 = 6$). So the only option for 4 values in $\{0, \ldots, 6\}$ pairwise at distance $\geq 2$ is $\{0, 2, 4, 6\}$ (or a subset shifted, but the span must be $\geq 6$, and the max span is 6, so it must be exactly $\{0, 2, 4, 6\}$).

Wait, that's not right. We could have $\{0, 2, 4, 6\}$ or $\{0, 2, 5, ?\}$... no, $|5 - 4| = 1$ if we had 4. Let me think again. We need 4 values from $\{0, \ldots, 6\}$ pairwise at distance $\geq 2$. The values must be $a_1 < a_2 < a_3 < a_4$ with $a_{i+1} \geq a_i + 2$. So $a_4 \geq a_1 + 6$. Since $a_4 \leq 6$ and $a_1 \geq 0$, we need $a_1 = 0$ and $a_4 = 6$, and $a_2 = 2, a_3 = 4$. So the only option is $\{0, 2, 4, 6\}$.

This means that for every pair of consecutive rows, the 4 column positions must be exactly $\{0, 2, 4, 6\}$. So each row uses 2 of the 4 values $\{0, 2, 4, 6\}$, and consecutive rows use complementary pairs (since together they must cover all 4).

But we also need each column to have exactly 2 black cells. The columns used are only $\{0, 2, 4, 6\}$, so columns 1, 3, 5 have 0 black cells. This violates the column sum condition!

So $n = 7$ doesn't work for $k = 2$! The bound $n \geq 4k - 1 = 7$ is not tight.

Hmm, so the block bound is necessary but not sufficient. The column sum condition adds more constraints.

Let me reconsider. For $k = 2$, what is the minimum $n$?

Let me try $n = 8$. We need 4 values from $\{0, \ldots, 7\}$ pairwise at distance $\geq 2$ for each pair of consecutive rows. The minimum span is 6, so we have some flexibility: $\{0, 2, 4, 6\}, \{0, 2, 4, 7\}, \{0, 2, 5, 7\}, \{0, 3, 5, 7\}, \{1, 3, 5, 7\}$, etc.

With $n = 8$, we have 8 columns, and we need each to have exactly 2 black cells. Total black cells = 16. If we only use columns $\{0, 2, 4, 6\}$, columns 1, 3, 5, 7 get 0. So we need to use all 8 columns.

Let me try to construct a solution for $n = 8, k = 2$.

I need two permutations $\sigma, \tau$ of $\{0, \ldots, 7\}$ with the non-adjacency conditions.

For consecutive rows, the 4 values must be pairwise at distance $\geq 2$. Let me try:

Row 0: $\sigma(0) = 0, \tau(0) = 3$ (distance 3 ≥ 2 ✓)
Row 1: needs 2 values from $\{0,...,7\} \setminus \{-1,0,1,2,3,4\}$ = $\{5,6,7\}$, pairwise distance ≥ 2. From $\{5,6,7\}$, max 2 values at distance ≥ 2: $\{5,7\}$. So $\sigma(1) = 5, \tau(1) = 7$ (or vice versa).

Row 2: needs 2 values at distance ≥ 2 from all of $\{5, 7\}$, i.e., not in $\{4,5,6,7,8\} \cap \{0,...,7\} = \{4,5,6,7\}$. Available: $\{0,1,2,3\}$. Need 2 at distance ≥ 2: $\{0,2\}, \{0,3\}, \{1,3\}$.

Let me try $\{0, 3\}$: $\sigma(2) = 0, \tau(2) = 3$.

Row 3: needs 2 values at distance ≥ 2 from $\{0, 3\}$, i.e., not in $\{0,1,2,3,4\}$. Available: $\{5,6,7\}$. Need 2 at distance ≥ 2: $\{5,7\}$.

Row 4: same as row 2: $\{0, 3\}$ (or $\{0,2\}$ or $\{1,3\}$).
Row 5: same as row 3: $\{5, 7\}$.
Row 6: $\{0, 3\}$.
Row 7: $\{5, 7\}$.

Now check column sums:
- Col 0: rows 0, 2, 4, 6 → 4. Need 2. ✗

Again, the columns are unbalanced. The issue is that we're alternating between two sets of columns, and each set is used in half the rows, giving 4 black cells per column instead of 2.

We need to vary the column choices more. Let me try:

Row 0: $\{0, 3\}$
Row 1: $\{5, 7\}$
Row 2: $\{1, 4\}$ — wait, need distance ≥ 2 from $\{5, 7\}$: not in $\{4,5,6,7\}$. Available: $\{0,1,2,3\}$. Can't use 4.

Hmm, the available set after row 1 is always $\{0,1,2,3\}$ (or a subset). So rows 0, 2, 4, 6 all draw from $\{0,1,2,3\}$ and rows 1, 3, 5, 7 all draw from $\{5,6,7\}$ (or similar). This creates an imbalance.

The problem is that with $k = 2$ and the tight spacing, consecutive rows force a "split" into two groups of columns, and alternating rows use the same group, leading to column imbalance.

Let me try a different approach. Instead of alternating between two fixed groups, let me try to vary the groups.

Row 0: $\{0, 2\}$
Row 1: $\{4, 6\}$ (distance ≥ 2 from $\{0, 2\}$: not in $\{0,1,2,3\}$, available $\{4,5,6,7\}$, pick $\{4, 6\}$)
Row 2: $\{1, 3\}$ — distance ≥ 2 from $\{4, 6\}$: not in $\{3,4,5,6,7\}$, available $\{0,1,2\}$. Can pick $\{0, 2\}$ but not $\{1, 3\}$ (3 is too close to 4). Actually available is $\{0,1,2\}$, and we need 2 at distance ≥ 2: $\{0, 2\}$.

Hmm, so row 2 must be $\{0, 2\}$ again. Same as row 0. Then row 3 = $\{4, 6\}$ or $\{5, 7\}$, etc.

It seems like with $n = 8$, we're stuck in a pattern where even rows use columns from $\{0,1,2,3\}$ and odd rows use columns from $\{4,5,6,7\}$ (or vice versa). This means columns 0-3 get 4 black cells each and columns 4-7 get 4 each, but we need each to get 2.

Wait, but within the even rows, we can vary which 2 columns we use. Let me try:

Row 0: $\{0, 2\}$
Row 1: $\{4, 6\}$
Row 2: $\{0, 2\}$ — forced (available from $\{0,1,2\}$, must pick $\{0,2\}$)
Row 3: $\{4, 6\}$ or $\{5, 7\}$

If row 3: $\{5, 7\}$:
Row 4: distance ≥ 2 from $\{5, 7\}$: not in $\{4,5,6,7\}$, available $\{0,1,2,3\}$. Pick $\{1, 3\}$.
Row 5: distance ≥ 2 from $\{1, 3\}$: not in $\{0,1,2,3,4\}$, available $\{5,6,7\}$. Pick $\{5, 7\}$.
Row 6: distance ≥ 2 from $\{5, 7\}$: available $\{0,1,2,3\}$. Pick $\{0, 2\}$ or $\{1, 3\}$.
Row 7: ...

Let me track column usage:
Row 0: 0, 2
Row 1: 4, 6
Row 2: 0, 2
Row 3: 5, 7
Row 4: 1, 3
Row 5: 5, 7
Row 6: 0, 2 (let's say)
Row 7: 4, 6 (distance ≥ 2 from {0,2}: available {4,5,6,7}, pick {4,6})

Column counts:
Col 0: rows 0, 2, 6 → 3
Col 1: row 4 → 1
Col 2: rows 0, 2, 6 → 3
Col 3: row 4 → 1
Col 4: rows 1, 7 → 2 ✓
Col 5: rows 3, 5 → 2 ✓
Col 6: rows 1, 7 → 2 ✓
Col 7: rows 3, 5 → 2 ✓

Columns 0, 2 have 3, columns 1, 3 have 1. Not balanced.

Let me try to adjust. We need columns 0-3 to each have exactly 2. Currently 0 has 3, 1 has 1, 2 has 3, 3 has 1.

If I change row 6 to $\{1, 3\}$:
Row 6: 1, 3 (distance ≥ 2 from {5,7}: available {0,1,2,3}, pick {1,3} ✓)
Row 7: distance ≥ 2 from {1,3}: not in {0,1,2,3,4}, available {5,6,7}. Pick {5,7}.

Column counts:
Col 0: rows 0, 2 → 2 ✓
Col 1: rows 4, 6 → 2 ✓
Col 2: rows 0, 2 → 2 ✓
Col 3: rows 4, 6 → 2 ✓
Col 4: rows 1, 7 → wait, row 7 is {5,7} now. Let me recalculate.

Row 0: 0, 2
Row 1: 4, 6
Row 2: 0, 2
Row 3: 5, 7
Row 4: 1, 3
Row 5: 5, 7
Row 6: 1, 3
Row 7: 5, 7 (distance ≥ 2 from {1,3}: available {5,6,7}, pick {5,7})

Column counts:
Col 0: 2 (rows 0, 2) ✓
Col 1: 2 (rows 4, 6) ✓
Col 2: 2 (rows 0, 2) ✓
Col 3: 2 (rows 4, 6) ✓
Col 4: 1 (row 1) ✗
Col 5: 3 (rows 3, 5, 7) ✗
Col 6: 1 (row 1) ✗
Col 7: 3 (rows 3, 5, 7) ✗

Still unbalanced. The issue is that rows 3, 5, 7 all use {5, 7} and row 1 uses {4, 6}.

Let me try varying more:

Row 0: 0, 2
Row 1: 4, 6
Row 2: 0, 2
Row 3: 5, 7
Row 4: 1, 3
Row 5: 4, 6 (distance ≥ 2 from {1,3}: not in {0,1,2,3,4}, available {5,6,7}. Can't pick {4,6} since 4 is excluded!)

Hmm, 4 is at distance 1 from 3, so 4 is excluded. Available from {5,6,7}: need 2 at distance ≥ 2: {5,7}.

So row 5 must be {5,7}. 

Row 6: distance ≥ 2 from {5,7}: available {0,1,2,3}. Pick {0,2} or {1,3}.
Row 7: if row 6 = {0,2}: available {4,5,6,7}, pick {4,6} or {5,7}.
        if row 6 = {1,3}: available {5,6,7}, pick {5,7}.

Let me try:
Row 0: 0, 2
Row 1: 4, 6
Row 2: 1, 3 (wait, distance from row 1 {4,6}: not in {3,4,5,6,7}, available {0,1,2}. Can't pick {1,3} since 3 is excluded.)

So row 2 must be from {0,1,2} with 2 values at distance ≥ 2: {0,2}.

It seems like the even rows are forced to use {0,2} (from available {0,1,2}) after an odd row using {4,6}, or {1,3} (from available {0,1,2,3}) after an odd row using {5,7}.

Wait, let me re-examine. After row 1 = {4,6}, the exclusion zone is {3,4,5,6,7}, so available = {0,1,2}. From {0,1,2}, 2 values at distance ≥ 2: only {0,2}.

After row 3 = {5,7}, the exclusion zone is {4,5,6,7}, so available = {0,1,2,3}. From {0,1,2,3}, 2 values at distance ≥ 2: {0,2}, {0,3}, {1,3}.

So after {4,6}, we're forced to {0,2}. After {5,7}, we have choices: {0,2}, {0,3}, {1,3}.

Similarly, after {0,2}, exclusion = {0,1,2,3}, available = {4,5,6,7}. Choices: {4,6}, {4,7}, {5,7}.
After {0,3}, exclusion = {0,1,2,3,4}, available = {5,6,7}. Choices: {5,7}.
After {1,3}, exclusion = {0,1,2,3,4}, available = {5,6,7}. Choices: {5,7}.

So the transitions are:
- {0,2} → {4,6}, {4,7}, {5,7}
- {0,3} → {5,7}
- {1,3} → {5,7}
- {4,6} → {0,2}
- {4,7} → {0,2} (exclusion = {3,4,5,6,7}, available = {0,1,2}, pick {0,2})
- {5,7} → {0,2}, {0,3}, {1,3}

So the state graph is:
{0,2} → {4,6}, {4,7}, {5,7}
{4,6} → {0,2}
{4,7} → {0,2}
{5,7} → {0,2}, {0,3}, {1,3}
{0,3} → {5,7}
{1,3} → {5,7}

We need a path of length 8 (rows 0-7) that uses each column exactly twice.

Let me denote the states and track column usage. We have 8 rows, each using 2 columns, total 16 column-uses, and each of 8 columns must be used exactly twice.

Let me try:
Row 0: {0,2}
Row 1: {5,7}
Row 2: {1,3}
Row 3: {5,7}
Row 4: {0,2} (from {5,7} → {0,2})
Row 5: {4,6} (from {0,2} → {4,6})
Row 6: {0,2} (from {4,6} → {0,2})
Row 7: {4,7} (from {0,2} → {4,7})

Column counts:
0: rows 0, 4, 6 → 3 ✗

Let me try again:
Row 0: {0,2}
Row 1: {5,7}
Row 2: {0,3}
Row 3: {5,7}
Row 4: {1,3}
Row 5: {5,7}
Row 6: {0,2}
Row 7: {4,6}

Column counts:
0: rows 0, 6 → 2 ✓
1: row 4 → 1 ✗
2: rows 0, 6 → 2 ✓
3: rows 2, 4 → 2 ✓
4: row 7 → 1 ✗
5: rows 1, 3, 5 → 3 ✗
6: row 7 → 1 ✗
7: rows 1, 3, 5 → 3 ✗

Still unbalanced. The problem is that {5,7} appears 3 times.

Let me try to use {5,7} only twice:
Row 0: {0,2}
Row 1: {4,6}
Row 2: {0,2}
Row 3: {5,7}
Row 4: {0,3}
Row 5: {5,7}
Row 6: {1,3}
Row 7: {4,7} (from {1,3} → {5,7} only! Can't go to {4,7}.)

Hmm, {1,3} → only {5,7}. So row 7 must be {5,7}, giving {5,7} three times.

What about:
Row 0: {0,2}
Row 1: {4,7}
Row 2: {0,2}
Row 3: {5,7}
Row 4: {1,3}
Row 5: {5,7}
Row 6: {0,2}
Row 7: {4,6}

Column counts:
0: rows 0, 2, 6 → 3 ✗

Hmm. The issue is that {0,2} keeps appearing. Let me try to minimize {0,2}:

Row 0: {0,3}
Row 1: {5,7}
Row 2: {1,3}
Row 3: {5,7}
Row 4: {0,2}
Row 5: {4,7}
Row 6: {0,2}
Row 7: {4,6}

Column counts:
0: rows 0, 4, 6 → 3 ✗

Still 3 for column 0. The problem is {0,2} and {0,3} both use column 0.

Let me try:
Row 0: {1,3}
Row 1: {5,7}
Row 2: {0,3}
Row 3: {5,7}
Row 4: {0,2}
Row 5: {4,6}
Row 6: {0,2}
Row 7: {4,7}

Column counts:
0: rows 2, 4, 6 → 3 ✗

Still 3 for column 0. The issue is that from {5,7}, the only options are {0,2}, {0,3}, {1,3}, and all of them except {1,3} use column 0. And {1,3} uses column 3.

Let me try to use {1,3} more:
Row 0: {1,3}
Row 1: {5,7}
Row 2: {1,3}
Row 3: {5,7}
Row 4: {0,2}
Row 5: {4,6}
Row 6: {0,2}
Row 7: {4,7}

Column counts:
0: rows 4, 6 → 2 ✓
1: rows 0, 2 → 2 ✓
2: rows 4, 6 → 2 ✓
3: rows 0, 2 → 2 ✓
4: rows 5, 7 → 2 ✓
5: rows 1, 3 → 2 ✓
6: row 5 → 1 ✗
7: rows 1, 3, 7 → 3 ✗

Close! Columns 6 and 7 are off by 1. Row 7 uses {4,7} but should use {4,6} to balance. But {4,6} from {0,2}: yes, {0,2} → {4,6} is valid!

Row 7: {4,6}

Column counts:
0: 2 ✓
1: 2 ✓
2: 2 ✓
3: 2 ✓
4: rows 5, 7 → 2 ✓
5: rows 1, 3 → 2 ✓
6: rows 5, 7 → 2 ✓
7: rows 1, 3 → 2 ✓

All columns have exactly 2! Let me verify the full solution:

Row 0: {1, 3}
Row 1: {5, 7}
Row 2: {1, 3}
Row 3: {5, 7}
Row 4: {0, 2}
Row 5: {4, 6}
Row 6: {0, 2}
Row 7: {4, 6}

Let me verify all adjacency conditions:
- Within each row: gaps are 2 ✓
- Between consecutive rows:
  - Row 0 {1,3} vs Row 1 {5,7}: |1-5|=4, |1-7|=6, |3-5|=2, |3-7|=4. All ≥ 2 ✓
  - Row 1 {5,7} vs Row 2 {1,3}: |5-1|=4, |5-3|=2, |7-1|=6, |7-3|=4. All ≥ 2 ✓
  - Row 2 {1,3} vs Row 3 {5,7}: same as row 0 vs row 1 ✓
  - Row 3 {5,7} vs Row 4 {0,2}: |5-0|=5, |5-2|=3, |7-0|=7, |7-2|=5. All ≥ 2 ✓
  - Row 4 {0,2} vs Row 5 {4,6}: |0-4|=4, |0-6|=6, |2-4|=2, |2-6|=4. All ≥ 2 ✓
  - Row 5 {4,6} vs Row 6 {0,2}: |4-0|=4, |4-2|=2, |6-0|=6, |6-2|=4. All ≥ 2 ✓
  - Row 6 {0,2} vs Row 7 {4,6}: same as row 4 vs row 5 ✓

All conditions satisfied! So $n(2) = 8$? Wait, but I should check if $n = 7$ is truly impossible.

For $n = 7, k = 2$: as I showed earlier, for any two consecutive rows, the 4 column positions must be pairwise at distance ≥ 2. In $\{0,...,6\}$, the only set of 4 values pairwise at distance ≥ 2 is $\{0, 2, 4, 6\}$. So every pair of consecutive rows uses exactly the columns $\{0, 2, 4, 6\}$. This means all black cells are in columns $\{0, 2, 4, 6\}$, and columns 1, 3, 5 have 0 black cells. But we need each column to have exactly 2. Contradiction. So $n = 7$ is impossible.

Therefore $n(2) = 8$.

Now I see the pattern. For $k = 2$, $n(2) = 8 = 4k$.

Let me check $k = 1$: $n(1) = 1$. And $4k = 4$. So $n(1) \neq 4k$. The formula might be different for $k = 1$.

Hmm wait, let me reconsider. For $k = 1$, the bound from the $2 \times 2$ block argument gives $n \geq 1$ (since $n = 1$ works). And $4k - 1 = 3$ for $k = 1$, but $n = 1$ works. So the bound isn't tight for $k = 1$.

Actually, for $k = 1$, we just need a permutation matrix with no two 1s adjacent (including diagonally). This is the problem of placing $n$ non-attacking kings on an $n \times n$ board, one per row and column. 

For $n = 1$: works.
For $n = 2$: we need a permutation of $\{0, 1\}$. Either $(0, 1)$ or $(1, 0)$. In either case, the two kings are at $(0, \sigma(0))$ and $(1, \sigma(1))$, which are in adjacent rows. For $\sigma = (0, 1)$: kings at $(0,0)$ and $(1,1)$, which are diagonally adjacent. For $\sigma = (1, 0)$: kings at $(0,1)$ and $(1,0)$, diagonally adjacent. So $n = 2$ doesn't work.

For $n = 3$: we need a permutation of $\{0, 1, 2\}$ with $|\sigma(r) - \sigma(r+1)| \geq 2$ for $r = 0, 1$. The only permutation with $|\sigma(0) - \sigma(1)| \geq 2$ and $|\sigma(1) - \sigma(2)| \geq 2$: we need $\sigma(0)$ and $\sigma(1)$ to differ by ≥ 2, and $\sigma(1)$ and $\sigma(2)$ to differ by ≥ 2. In $\{0,1,2\}$, pairs at distance ≥ 2: $(0,2)$. So $\sigma(0)$ and $\sigma(2)$ must both be at distance ≥ 2 from $\sigma(1)$. If $\sigma(1) = 1$, then $\sigma(0), \sigma(2) \in \{0, 2\}$ but they must be different (permutation), so $\sigma(0) = 0, \sigma(2) = 2$ or vice versa. Check: $|\sigma(0) - \sigma(1)| = |0 - 1| = 1 < 2$. Doesn't work.

If $\sigma(1) = 0$: $\sigma(0), \sigma(2) \in \{2\}$ (only 2 is at distance ≥ 2 from 0). But we need two different values. Doesn't work.

If $\sigma(1) = 2$: similarly, only 0 is at distance ≥ 2 from 2. Doesn't work.

So $n = 3$ doesn't work for $k = 1$.

For $n = 4$: permutation of $\{0,1,2,3\}$ with $|\sigma(r) - \sigma(r+1)| \geq 2$ for $r = 0, 1, 2$. 

Try $\sigma = (0, 2, 0, ...)$: no, must be a permutation. Try $\sigma = (0, 3, 1, ?)$: $|0-3|=3 ✓, |3-1|=2 ✓$. Need $\sigma(3)$ at distance ≥ 2 from 1, and $\sigma(3) \in \{2\}$ (remaining). $|1-2| = 1 < 2$. Doesn't work.

Try $\sigma = (1, 3, 0, 2)$: $|1-3|=2 ✓, |3-0|=3 ✓, |0-2|=2 ✓$. All good! So $n = 4$ works for $k = 1$.

But wait, $n = 1$ also works. So $n(1) = 1$.

Hmm, but for $k = 1$, $n = 1$ is trivially the minimum. Let me re-examine.

For $k = 1, n = 1$: 1×1 board, 1 black cell. Each row (1 row) has 1 black, each column (1 column) has 1 black. No adjacency issues. ✓

So $n(1) = 1$.

Now, the pattern might be $n(k) = 4k$ for $k \geq 2$ and $n(1) = 1$? Let me check $k = 3$.

For $k = 3$, the block bound gives $n \geq 4 \cdot 3 - 1 = 11$ (odd) or $n \geq 12$ (even). But as we saw with $k = 2$, the column sum condition might force $n$ to be even, specifically $n = 4k$.

Let me think about why $n = 4k - 1$ fails. For $n = 4k - 1$ and two consecutive rows, we need $2k$ column positions pairwise at distance ≥ 2. In $\{0, \ldots, 4k-2\}$, $2k$ values pairwise at distance ≥ 2 need span $\geq 2(2k-1) = 4k - 2 = n - 1$. So the span is exactly $n - 1$, meaning the values must be $\{0, 2, 4, \ldots, 4k-2\}$ (the only set of $2k$ values in $\{0, \ldots, 4k-2\}$ with pairwise distance ≥ 2 and span $4k-2$). This is exactly the even numbers from 0 to $4k-2$.

So for $n = 4k - 1$, every pair of consecutive rows must use exactly the columns $\{0, 2, 4, \ldots, 4k-2\}$. This means all black cells are in even columns, and odd columns have 0 black cells. But we need each column to have $k$ black cells. Contradiction for $k \geq 1$ (since there are $2k-1$ odd columns that need $k$ black cells each but have 0).

So $n = 4k - 1$ is impossible for any $k \geq 1$ (well, for $k = 1$, $n = 3$ uses columns $\{0, 2\}$ and column 1 gets 0, which contradicts needing 1 black cell in column 1).

What about $n = 4k - 2$ (even)? The block bound gives $n \geq 4k$ for even $n$, so $n = 4k - 2$ fails the block bound.

What about other odd values? $n = 4k + 1$? The block bound: $nk \leq \lceil n/2 \rceil^2 = (2k+1)^2 = 4k^2 + 4k + 1$. And $nk = (4k+1)k = 4k^2 + k$. So $4k^2 + k \leq 4k^2 + 4k + 1$, i.e., $0 \leq 3k + 1$. Always true. So $n = 4k + 1$ satisfies the block bound.

But does the column sum condition work? For $n = 4k + 1$ and two consecutive rows, we need $2k$ values in $\{0, \ldots, 4k\}$ pairwise at distance ≥ 2. The minimum span is $4k - 2$, and the maximum span is $4k$. So we have some flexibility.

But we also need $n = 4k$ to work (even). Let me focus on whether $n = 4k$ works.

For $n = 4k$ (even), the block bound gives $nk \leq (n/2)^2 = (2k)^2 = 4k^2$, i.e., $4k \cdot k = 4k^2 \leq 4k^2$. Equality! So the bound is tight, meaning every $2 \times 2$ block must have exactly 1 black cell.

This is a very structured condition. Let me think about what it means.

If $n = 4k$ and every $2 \times 2$ block has exactly 1 black cell, then the black cells form a perfect "transversal" of the $2 \times 2$ blocks. There are $(2k)^2 = 4k^2$ blocks and $4k^2$ black cells, so each block has exactly 1.

Now, within each $2 \times 2$ block (at position $(2i, 2j)$ for $0 \leq i, j < 2k$), we place 1 black cell in one of the 4 positions. But we also need the non-adjacency condition between blocks. Two adjacent blocks (horizontally or vertically) share a boundary, and cells near the boundary might be adjacent.

Let me think about this more carefully. Consider two horizontally adjacent $2 \times 2$ blocks: block $(i, j)$ covering columns $2j, 2j+1$ and block $(i, j+1)$ covering columns $2j+2, 2j+3$. If the black cell in block $(i, j)$ is at column $2j+1$ and the black cell in block $(i, j+1)$ is at column $2j+2$, and they're in the same row, then they're at distance 1 (horizontally adjacent). So we need to avoid this.

Similarly for vertically adjacent blocks.

This is getting complex. Let me think about a specific construction for general $k$.

**Construction for $n = 4k$:**

Based on the $k = 2$ solution I found, let me generalize. The pattern was:
- Rows 0, 2: columns {1, 3} (i.e., odd columns in the first half)
- Rows 1, 3: columns {5, 7} (i.e., odd columns in the second half)
- Rows 4, 6: columns {0, 2} (i.e., even columns in the first half)
- Rows 5, 7: columns {4, 6} (i.e., even columns in the second half)

More generally, for $n = 4k$, I can think of the board as divided into $4$ quadrants of size $2k \times 2k$:
- Q1: rows 0 to $2k-1$, columns 0 to $2k-1$
- Q2: rows 0 to $2k-1$, columns $2k$ to $4k-1$
- Q3: rows $2k$ to $4k-1$, columns 0 to $2k-1$
- Q4: rows $2k$ to $4k-1$, columns $2k$ to $4k-1$

In the $k = 2$ case:
- Rows 0-3 (first half of rows), columns 0-3 (Q1) and 4-7 (Q2)
- Rows 4-7 (second half), columns 0-3 (Q3) and 4-7 (Q4)

The pattern was:
- Rows 0, 2 (even rows in first half): odd columns in Q1 = {1, 3}
- Rows 1, 3 (odd rows in first half): odd columns in Q2 = {5, 7}
- Rows 4, 6 (even rows in second half): even columns in Q3 = {0, 2}
- Rows 5, 7 (odd rows in second half): even columns in Q4 = {4, 6}

Hmm, let me think about this more systematically.

Actually, let me think about the construction differently. Consider the $n = 4k$ board. I want to place $k$ black cells per row and column with the non-adjacency condition.

Here's an idea: use a "block diagonal" type construction. Divide the rows into groups of 2 and columns into groups of 2. In each $2 \times 2$ block, place exactly 1 black cell. The placement within each block determines the row and column sums.

Actually, let me think about it as follows. We have a $2k \times 2k$ grid of $2 \times 2$ blocks. In each block, we place 1 black cell. The row sum condition: each row of the big board has $k$ black cells. Each big row consists of 2 sub-rows (within a pair), and each sub-row has $2k$ blocks. The black cells in a sub-row come from the blocks in that block-row. Each block contributes 0 or 1 black cell to each sub-row (depending on which of the 2 rows within the block the black cell is placed).

This is getting complicated. Let me try a different approach.

**Key insight:** The problem is equivalent to finding a $k$-regular bipartite graph (rows vs. columns) where the edges form an independent set in the king graph. 

Let me think about the problem in terms of a formula. Based on $k = 1$ giving $n = 1$ and $k = 2$ giving $n = 8$, let me check if the pattern is $n(k) = 4k$ for $k \geq 2$ and $n(1) = 1$.

Actually wait, $n(1) = 1$ but $4 \cdot 1 = 4$. So maybe the formula is different. Let me reconsider $k = 1$.

For $k = 1$, we need 1 black cell per row and column, no two adjacent (including diagonally). This is a permutation matrix where consecutive rows have their 1s at distance ≥ 2.

$n = 1$: works (trivially).
$n = 2$: doesn't work (shown above).
$n = 3$: doesn't work (shown above).
$n = 4$: works (shown above, $\sigma = (1, 3, 0, 2)$).

But $n = 1$ works, so $n(1) = 1$.

Hmm, but for $k = 1$, $n = 1$ is a degenerate case. Let me reconsider: for $k = 1$, the constraint is just a permutation with no two consecutive entries differing by ≤ 1. For $n = 1$, there's only one cell, so it trivially works.

So $n(1) = 1$, and for $k \geq 2$, $n(k) = 4k$? Let me verify for $k = 3$.

For $k = 3, n = 12$: I need to construct a $12 \times 12$ board with 3 black cells per row and column, no two adjacent.

Let me try to generalize the $k = 2$ construction. The idea was to use 4 "groups" of rows and columns:

For $k = 2, n = 8$:
- Group A: even rows in first half (rows 0, 2), use odd columns in first half (1, 3)
- Group B: odd rows in first half (rows 1, 3), use odd columns in second half (5, 7)
- Group C: even rows in second half (rows 4, 6), use even columns in first half (0, 2)
- Group D: odd rows in second half (rows 5, 7), use even columns in second half (4, 6)

For general $k$, $n = 4k$:
- First half of rows: rows 0 to $2k-1$
- Second half of rows: rows $2k$ to $4k-1$
- First half of columns: 0 to $2k-1$
- Second half of columns: $2k$ to $4k-1$

Within the first half of rows:
- Even rows (0, 2, 4, ..., $2k-2$): there are $k$ such rows. Use odd columns from first half: 1, 3, 5, ..., $2k-1$. That's $k$ columns. Each such row gets all $k$ of these columns. But then each of these columns gets $k$ black cells (one from each even row in the first half). ✓ for column sum.
- Odd rows (1, 3, 5, ..., $2k-1$): there are $k$ such rows. Use odd columns from second half: $2k+1, 2k+3, ..., 4k-1$. That's $k$ columns. Each such row gets all $k$. Each column gets $k$ black cells. ✓

Within the second half of rows:
- Even rows ($2k, 2k+2, ..., 4k-2$): there are $k$ such rows. Use even columns from first half: 0, 2, 4, ..., $2k-2$. That's $k$ columns. ✓
- Odd rows ($2k+1, 2k+3, ..., 4k-1$): there are $k$ such rows. Use even columns from second half: $2k, 2k+2, ..., 4k-2$. That's $k$ columns. ✓

Now let me check column sums:
- Even columns in first half (0, 2, ..., $2k-2$): used by $k$ even rows in second half. Each gets $k$ uses. ✓
- Odd columns in first half (1, 3, ..., $2k-1$): used by $k$ even rows in first half. Each gets $k$ uses. ✓
- Even columns in second half ($2k, 2k+2, ..., 4k-2$): used by $k$ odd rows in second half. Each gets $k$ uses. ✓
- Odd columns in second half ($2k+1, 2k+3, ..., 4k-1$): used by $k$ odd rows in first half. Each gets $k$ uses. ✓

All column sums = $k$. ✓

Now check non-adjacency:
1. Within a row: columns are 1, 3, 5, ..., $2k-1$ (or similar). Gaps = 2. ✓
2. Between consecutive rows: need to check all pairs.

Let me check the four types of consecutive row pairs:

**Type 1: Even row in first half → Odd row in first half** (e.g., row 0 → row 1)
- Even row uses odd columns from first half: {1, 3, ..., $2k-1$}
- Odd row uses odd columns from second half: {$2k+1, 2k+3, ..., $4k-1$}
- Distance between any column in first set and any in second set: min distance = $2k+1 - (2k-1) = 2$. ✓

**Type 2: Odd row in first half → Even row in first half** (e.g., row 1 → row 2)
- Odd row uses odd columns from second half: {$2k+1, ..., $4k-1$}
- Even row uses odd columns from first half: {1, ..., $2k-1$}
- Min distance = $2k+1 - (2k-1) = 2$. ✓

**Type 3: Last row of first half → First row of second half**
- Last row of first half: if $2k-1$ is odd (which it is for any $k$), it's an odd row using odd columns from second half: {$2k+1, ..., $4k-1$}
- First row of second half: row $2k$, which is even, using even columns from first half: {0, 2, ..., $2k-2$}
- Min distance: $2k+1 - (2k-2) = 3$. ✓

Wait, but I need to be more careful. Let me check row $2k-1$ → row $2k$:
- Row $2k-1$ (odd, first half): columns {$2k+1, 2k+3, ..., 4k-1$}
- Row $2k$ (even, second half): columns {0, 2, ..., $2k-2$}
- Min distance: $\min |c_1 - c_2|$ where $c_1 \in \{2k+1, ..., 4k-1\}$ and $c_2 \in \{0, ..., 2k-2\}$. The closest are $2k+1$ and $2k-2$, distance = 3. ✓

**Type 4: Even row in second half → Odd row in second half** (e.g., row $2k$ → row $2k+1$)
- Even row uses even columns from first half: {0, 2, ..., $2k-2$}
- Odd row uses even columns from second half: {$2k, 2k+2, ..., 4k-2$}
- Min distance: $2k - (2k-2) = 2$. ✓

**Type 5: Odd row in second half → Even row in second half** (e.g., row $2k+1$ → row $2k+2$)
- Odd row uses even columns from second half: {$2k, ..., 4k-2$}
- Even row uses even columns from first half: {0, ..., $2k-2$}
- Min distance: $2k - (2k-2) = 2$. ✓

All consecutive row pairs have minimum column distance ≥ 2. ✓

So the construction works for all $k \geq 2$ with $n = 4k$.

Now I need to verify that $n = 4k - 1$ is impossible for $k \geq 2$ (which I showed above: the column sum condition fails because all black cells must be in even columns).

And I need to check that no odd $n$ between $4k - 1$ and $4k$ works... well, $4k - 1$ is the only odd number in that range, and I showed it fails.

But wait, I should also check that no $n < 4k - 1$ works. The block bound shows $n \geq 4k - 1$ for $k \geq 2$ (odd) or $n \geq 4k$ (even). And $n = 4k - 1$ fails. So for even $n$, $n \geq 4k$, and for odd $n$, $n \geq 4k + 1$ (since $4k - 1$ fails). But $4k + 1 > 4k$, so $n(k) = 4k$ for $k \geq 2$.

Wait, I need to be more careful. The block bound says:
- For even $n$: $n \geq 4k$
- For odd $n$: $n \geq 4k - 1$ (necessary but we showed not sufficient)

So the minimum even $n$ is $4k$, and we showed $n = 4k$ works. The minimum odd $n$ that could work is $4k + 1$ (since $4k - 1$ fails). But $4k + 1 > 4k$, so the overall minimum is $4k$.

Actually, I need to also verify that no odd $n$ with $4k - 1 < n < 4k$ works. But there's no odd integer strictly between $4k - 1$ and $4k$. So the next odd to check would be $4k + 1$, which is larger than $4k$.

Therefore, $n(k) = 4k$ for $k \geq 2$.

For $k = 1$: $n(1) = 1$ (as shown). But wait, does the formula $n(k) = 4k$ give $n(1) = 4$? And we showed $n = 1$ works. So $n(1) = 1 \neq 4 = 4 \cdot 1$.

Hmm, let me re-examine. For $k = 1$:
- $n = 1$ works (trivially).
- The block bound for even $n$: $n \geq 4$. For odd $n$: $n \geq 3$ (i.e., $4 \cdot 1 - 1 = 3$).
- $n = 3$ fails (shown above).
- $n = 1$ works.

So $n(1) = 1$. But $1$ is odd and $1 < 3 = 4 \cdot 1 - 1$. How does this escape the block bound?

For $n = 1$: $\lceil n/2 \rceil^2 = 1$. $nk = 1$. $1 \leq 1$. ✓. So the block bound is satisfied.

For $n = 3$: $\lceil 3/2 \rceil^2 = 4$. $nk = 3$. $3 \leq 4$. ✓. Block bound satisfied, but the column sum condition fails (as I showed).

For $n = 1$: the block bound is tight (1 = 1), and the column sum condition is trivially satisfied (1 row, 1 column, 1 black cell).

So for $k = 1$, $n = 1$ is a special case that works because the board is so small that the constraints are trivially compatible.

Now, what about $k = 1$ and $n = 2$? Block bound: $\lceil 2/2 \rceil^2 = 1$. $nk = 2$. $2 \leq 1$? No! So $n = 2$ fails the block bound.

So for $k = 1$: $n = 1$ works (block bound tight), $n = 2$ fails block bound, $n = 3$ fails column condition, $n = 4$ works. So $n(1) = 1$.

Great. So the answer is:
- $n(1) = 1$
- $n(k) = 4k$ for $k \geq 2$

Now let me compute $\sum_{k=1}^{50} n(k) = 1 + \sum_{k=2}^{50} 4k = 1 + 4 \sum_{k=2}^{50} k = 1 + 4 \left(\frac{50 \cdot 51}{2} - 1\right) = 1 + 4 \cdot (1275 - 1) = 1 + 4 \cdot 1274 = 1 + 5096 = 5097$.

Wait, let me double-check: $\sum_{k=2}^{50} k = \sum_{k=1}^{50} k - 1 = \frac{50 \cdot 51}{2} - 1 = 1275 - 1 = 1274$.

$4 \cdot 1274 = 5096$.

$1 + 5096 = 5097$.

So the answer is $\boxed{5097}$.

But wait, I should double-check my claim that $n = 4k - 1$ is impossible for $k \geq 2$ more carefully, and also verify that $n(1) = 1$ is correct.

**Verification that $n(1) = 1$:**
- $n = 1, k = 1$: 1×1 board, 1 black cell. Row sum = 1 ✓, column sum = 1 ✓, no adjacency issues ✓. So $n(1) = 1$.

**Verification that $n = 4k - 1$ is impossible for $k \geq 2$:**

For $n = 4k - 1$, consider any two consecutive rows. Together they have $2k$ black cells, all in different columns (since within a row, the $k$ black cells are in different columns, and between rows, a column can have at most... well, actually a column can have black cells in both rows, as long as they're not adjacent. But if row $r$ has a black cell at column $c$ and row $r+1$ has a black cell at column $c$, they'd be vertically adjacent, which is not allowed. So the $2k$ black cells in two consecutive rows are all in different columns.)

So the $2k$ black cells in two consecutive rows occupy $2k$ distinct columns, and any two of them are at distance $\geq 2$ (since they're all pairwise non-adjacent). In $\{0, \ldots, 4k-2\}$ (which has $4k - 1$ elements), $2k$ distinct values pairwise at distance $\geq 2$ require a span of at least $2(2k - 1) = 4k - 2$. Since the maximum span is $4k - 2$ (from 0 to $4k - 2$), the values must be exactly $\{0, 2, 4, \ldots, 4k - 2\}$.

This means that for every pair of consecutive rows, all black cells are in even columns. Since this holds for all consecutive pairs (rows 0-1, 1-2, 2-3, ..., $(n-2)$-$(n-1)$), by induction, all black cells in all rows are in even columns. But then odd columns have 0 black cells, contradicting the requirement that each column has $k \geq 2$ black cells (in fact, even $k \geq 1$ would be contradicted since odd columns need $k \geq 1$ black cells).

Wait, actually for $k = 1$: odd columns need 1 black cell, but they have 0. So $n = 3$ fails for $k = 1$ too, which is consistent with what I found.

So $n = 4k - 1$ is impossible for all $k \geq 1$.

**Now, is $n = 4k$ the minimum for $k \geq 2$?**

For even $n < 4k$: the block bound gives $n \geq 4k$, so no even $n < 4k$ works.
For odd $n < 4k$: the largest odd $n < 4k$ is $4k - 1$, which we showed is impossible. The next is $4k - 3$, which fails the block bound for $k \geq 2$ (since $(4k-3)k > ((4k-3+1)/2)^2 = (2k-1)^2$ iff $4k^2 - 3k > 4k^2 - 4k + 1$ iff $k > 1$, which is true for $k \geq 2$).

So for $k \geq 2$, $n(k) = 4k$.

For $k = 1$: $n = 1$ works (special case), so $n(1) = 1$.

**Final computation:**
$$\sum_{k=1}^{50} n(k) = n(1) + \sum_{k=2}^{50} n(k) = 1 + \sum_{k=2}^{50} 4k = 1 + 4\left(\frac{50 \cdot 51}{2} - 1\right) = 1 + 4 \cdot 1274 = 1 + 5096 = 5097.$$

Let me now write up the proof properly.

Actually, let me reconsider whether the construction for $n = 4k$ works for $k = 1$ as well. For $k = 1, n = 4$:
- Even rows in first half (rows 0): odd columns in first half: {1}. So row 0 has black at column 1.
- Odd rows in first half (rows 1): odd columns in second half: {3}. So row 1 has black at column 3.
- Even rows in second half (rows 2): even columns in first half: {0}. So row 2 has black at column 0.
- Odd rows in second half (rows 3): even columns in second half: {2}. So row 3 has black at column 2.

This gives the permutation $(1, 3, 0, 2)$, which I already verified works! So the construction gives $n = 4$ for $k = 1$, but $n = 1$ is smaller and also works.

So the construction works for all $k \geq 1$ with $n = 4k$, but for $k = 1$, $n = 1$ is better.

Now let me also verify: is there any $n$ with $1 < n < 4$ that works for $k = 1$? 
- $n = 2$: block bound gives $2 \leq 1$, fails.
- $n = 3$: shown to fail.

So $n(1) = 1$ is confirmed.

Let me also double-check my construction more carefully for a general $k$. Let me re-examine the non-adjacency between non-consecutive rows. Actually, the non-adjacency condition only applies to cells that share a side or vertex, which means they must be in the same or adjacent rows AND same or adjacent columns. So I only need to check consecutive rows (and within each row). Non-consecutive rows are automatically fine (since $|r_1 - r_2| \geq 2$).

Wait, that's the key point! Two cells at $(r_1, c_1)$ and $(r_2, c_2)$ share a side or vertex iff $|r_1 - r_2| \leq 1$ AND $|c_1 - c_2| \leq 1$. So if $|r_1 - r_2| \geq 2$, they don't share a side or vertex regardless of columns. So I only need to check:
1. Within the same row: $|c_1 - c_2| \geq 2$ (which is guaranteed by the gap of 2 in our construction).
2. Between consecutive rows: $|c_1 - c_2| \geq 2$ for all pairs (which I verified above).

Great, so the construction is correct.

Now let me also think about whether there might be a smaller odd $n$ that works for $k \geq 2$, one that I haven't considered. The block bound for odd $n$ says $n \geq 4k - 1$. I showed $n = 4k - 1$ fails. What about $n = 4k + 1$? That's larger than $4k$, so it doesn't affect the minimum. And all odd $n$ between $4k - 1$ and $4k + 1$... there are none (since $4k$ is even, $4k - 1$ and $4k + 1$ are consecutive odd numbers).

So the minimum is indeed $4k$ for $k \geq 2$.

Let me reconsider the lower bound argument once more to make sure it's airtight.

**Lower bound for $k \geq 2$:**

We need to show $n \geq 4k$.

Case 1: $n$ is even. The $2 \times 2$ block argument: partition the board into $(n/2)^2$ disjoint $2 \times 2$ blocks. Each block contains at most 1 black cell (since any two cells in a $2 \times 2$ block are at Chebyshev distance $\leq 1$). Total black cells = $nk \leq (n/2)^2$, so $k \leq n/4$, i.e., $n \geq 4k$.

Case 2: $n$ is odd. Write $n = 2m + 1$. The block argument: partition into $m^2$ full $2 \times 2$ blocks, $m$ vertical $2 \times 1$ blocks (last column), $m$ horizontal $1 \times 2$ blocks (last row), and 1 single cell. Each block has at most 1 black cell. Total $\leq m^2 + 2m + 1 = (m+1)^2 = \lceil n/2 \rceil^2$. So $nk \leq \lceil n/2 \rceil^2$.

For $n = 4k - 1$: $m = 2k - 1$, bound gives $(4k-1)k \leq (2k)^2 = 4k^2$, i.e., $4k^2 - k \leq 4k^2$. True. So the block bound is satisfied.

But we showed that $n = 4k - 1$ fails due to the column sum condition: all black cells must be in even columns, leaving odd columns empty.

For $n = 4k - 3$ (the next smaller odd): $m = 2k - 2$, bound gives $(4k-3)k \leq (2k-1)^2 = 4k^2 - 4k + 1$, i.e., $4k^2 - 3k \leq 4k^2 - 4k + 1$, i.e., $k \leq 1$. Fails for $k \geq 2$.

So for $k \geq 2$, the smallest feasible odd $n$ from the block bound is $4k - 1$, which fails the column condition. The next odd is $4k + 1 > 4k$. So $n \geq 4k$.

Combined with the construction showing $n = 4k$ works, we get $n(k) = 4k$ for $k \geq 2$.

For $k = 1$: $n = 1$ works, and $n = 2, 3$ don't work (block bound fails for $n = 2$, column condition fails for $n = 3$). So $n(1) = 1$.

**Sum:**
$$\sum_{k=1}^{50} n(k) = 1 + \sum_{k=2}^{50} 4k = 1 + 4\left(\frac{50 \cdot 51}{2} - 1\right) = 1 + 4 \cdot 1274 = 5097.$$

Let me now write the formal proof.

Hmm, actually I want to make sure about the $n = 4k-1$ impossibility argument. Let me re-examine it.

For $n = 4k - 1$ (odd), consider any two consecutive rows $r$ and $r+1$. Row $r$ has $k$ black cells at columns $a_1 < a_2 < \cdots < a_k$ (with $a_{i+1} \geq a_i + 2$), and row $r+1$ has $k$ black cells at columns $b_1 < b_2 < \cdots < b_k$ (with $b_{j+1} \geq b_j + 2$). The non-adjacency between rows requires $|a_i - b_j| \geq 2$ for all $i, j$.

The combined set $\{a_1, \ldots, a_k, b_1, \ldots, b_k\}$ has $2k$ elements (all distinct, since if $a_i = b_j$, then $|a_i - b_j| = 0 < 2$). These $2k$ elements are pairwise at distance $\geq 2$ (within each row by the gap condition, and across rows by the non-adjacency condition).

In $\{0, 1, \ldots, 4k-2\}$ (which has $4k - 1$ elements), $2k$ elements pairwise at distance $\geq 2$ require the minimum element $\geq 0$ and maximum element $\geq 0 + 2(2k - 1) = 4k - 2$. Since the maximum element is at most $4k - 2$, we need the minimum to be 0 and the maximum to be $4k - 2$, and the elements to be exactly $\{0, 2, 4, \ldots, 4k - 2\}$.

This holds for every pair of consecutive rows. In particular, for rows 0 and 1, all black cells are in $\{0, 2, 4, \ldots, 4k-2\}$. For rows 1 and 2, all black cells are in $\{0, 2, 4, \ldots, 4k-2\}$. Since row 1's black cells are in even columns (from the first pair), and row 2's black cells are in even columns (from the second pair), and so on. By induction, all black cells in all rows are in even columns.

But the board has $2k$ even columns (0, 2, ..., $4k-2$) and $2k - 1$ odd columns (1, 3, ..., $4k-3$). The odd columns have 0 black cells, but each column must have $k \geq 2$ black cells. Contradiction.

Actually, for $k = 1$: odd columns must have 1 black cell, but have 0. Also a contradiction. So $n = 4k - 1$ fails for all $k \geq 1$.

This is correct. The argument is airtight.

Now, one more thing: I should verify that for $k \geq 2$, no odd $n$ with $n < 4k$ other than $4k - 1$ could work. The block bound eliminates all odd $n \leq 4k - 3$ for $k \geq 2$. And $n = 4k - 1$ fails by the column argument. So no odd $n < 4k$ works, and $n(k) = 4k$.

The proof is complete. Let me write it up.

Actually, let me reconsider the block bound for odd $n$ more carefully. I claimed that for odd $n = 2m + 1$, the total black cells $\leq (m+1)^2$. Let me verify this partition.

Partition the $n \times n$ board (with $n = 2m + 1$) into:
- $m^2$ blocks of size $2 \times 2$: rows $\{0,1\}, \{2,3\}, \ldots, \{2m-2, 2m-1\}$ × columns $\{0,1\}, \{2,3\}, \ldots, \{2m-2, 2m-1\}$
- $m$ blocks of size $2 \times 1$: rows $\{0,1\}, \{2,3\}, \ldots, \{2m-2, 2m-1\}$ × column $\{2m\}$
- $m$ blocks of size $1 \times 2$: row $\{2m\}$ × columns $\{0,1\}, \{2,3\}, \ldots, \{2m-2, 2m-1\}$
- 1 block of size $1 \times 1$: row $\{2m\}$ × column $\{2m\}$

Each $2 \times 2$ block: at most 1 black cell (any two cells in a $2 \times 2$ block are at Chebyshev distance $\leq 1$).
Each $2 \times 1$ block: at most 1 black cell (the two cells are vertically adjacent).
Each $1 \times 2$ block: at most 1 black cell (the two cells are horizontally adjacent).
The $1 \times 1$ block: at most 1 black cell.

Total: $m^2 + m + m + 1 = (m+1)^2$.

This is correct. And these blocks are disjoint and cover the entire board. So the bound is valid.

For $n = 4k - 3 = 2(2k-2) + 1$, $m = 2k - 2$:
$(m+1)^2 = (2k-1)^2 = 4k^2 - 4k + 1$.
$nk = (4k-3)k = 4k^2 - 3k$.
Need $4k^2 - 3k \leq 4k^2 - 4k + 1$, i.e., $k \leq 1$. Fails for $k \geq 2$. ✓

For $n = 4k - 1 = 2(2k-1) + 1$, $m = 2k - 1$:
$(m+1)^2 = (2k)^2 = 4k^2$.
$nk = (4k-1)k = 4k^2 - k$.
$4k^2 - k \leq 4k^2$. ✓ (but fails column condition)

Everything checks out. The answer is $\boxed{5097}$.

Let me also verify the sum one more time:
$\sum_{k=1}^{50} n(k) = 1 + 4 \cdot 2 + 4 \cdot 3 + \cdots + 4 \cdot 50$
$= 1 + 4(2 + 
