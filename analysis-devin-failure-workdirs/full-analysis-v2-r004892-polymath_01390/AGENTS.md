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
  <problem_id>polymath_01390</problem_id>
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

A $100 \times 100$ grid is colored black and white. Each column contains the same number of black cells, while each row contains a different number of black cells. What is the maximum possible number of pairs of adjacent cells of different colors?

## Standard Solution

Let the side length of the table be $2n = 100$ (so $n = 50$), and number the rows from top to bottom and the columns from left to right with numbers from $1$ to $2n$.

In each row, there can be from $0$ to $2n$ black cells. Since the number of black cells in all rows is different, these numbers are all the integers from $0$ to $2n$, except for one (say, except for $k$). Then the total number of black cells is $(0 + 1 + \ldots + 2n) - k = 2n^2 + n - k$. On the other hand, since there are equally many black cells in all columns, the total number of black cells must be divisible by $2n$. Thus, $k = n$, and in all columns, there are $2n^2/(2n) = n$ black cells.

Now let's estimate the number of pairs of adjacent cells of different colors, counting separately the pairs of cells adjacent horizontally and vertically.

If in row $i \leq n-1$ there are $i$ black cells, then they can participate in at most $2i$ horizontal pairs. If in row $i \geq n+1$ there are $i$ black cells, the same reasoning can be applied to the white cells, of which there are $2n - i \leq n-1$. In total, the number of horizontal different-colored pairs is no more than $2 \cdot (2 \cdot 0 + 2 \cdot 1 + \ldots + 2 \cdot (n-1)) = 2n(n-1)$.

Now let's estimate the number of vertical pairs. Consider any row with an even number from $2$ to $2(n-1)$; let it have $i$ black cells. Then either in the row above or in the row below it, the number of black cells is not equal to $100 - i$; hence, one of the vertical pairs involving the cells of our row will be monochromatic. In total, there are at least $n-1$ monochromatic vertical pairs. Since the total number of vertical pairs is $2n(2n-1)$, the number of different-colored pairs among them is no more than $2n(2n-1) - (n-1)$. Thus, the total number of different-colored pairs is no more than $2n(n-1) + (4n^2 - 3n + 1) = 6n^2 - 5n + 1$.

For $n = 50$, this gives $6 \cdot 50^2 - 5 \cdot 50 + 1 = 15000 - 250 + 1 = 14751$.

It remains to provide an example in which this number of pairs is achieved. Draw a diagonal in the $2n \times 2n$ table from the upper left corner to the lower right corner. All cells lying on or below the diagonal are colored black if they are in even rows and white otherwise (coloring "by rows"). All cells lying above the diagonal are colored black if the sum of their row and column numbers is even, and white otherwise ("checkerboard" coloring). In this construction, each column contains exactly $n$ black cells, and each row contains a different number of black cells. All the estimates above are achieved.

\(\boxed{14751}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. It's a combinatorics problem about a 100×100 grid.

Let me think about it carefully.

We have a 100×100 grid colored black and white. Each column has the same number of black cells. Each row has a different number of black cells. We want to maximize the number of pairs of adjacent cells of different colors.

First, let me check for answer leaks. The problem statement is clean - no solutions, no hints. Good.

Let me think about the problem.

Let's denote the grid as a matrix $A$ where $A_{ij} = 1$ if cell $(i,j)$ is black, 0 if white.

Each column has the same number of black cells. Let's say each column has $k$ black cells. So total black cells = $100k$.

Each row has a different number of black cells. Since there are 100 rows and each row has between 0 and 100 black cells, the row sums must be 100 distinct values from $\{0, 1, 2, ..., 100\}$. So the row sums are 100 distinct values, which means they are exactly 100 of the 101 possible values $\{0, 1, ..., 100\}$.

The total number of black cells = sum of row sums = sum of 100 distinct values from $\{0, 1, ..., 100\}$.

The sum of all 101 values $\{0, 1, ..., 100\}$ is $100 \cdot 101 / 2 = 5050$.

So the total black cells = $5050 - m$ where $m$ is the one value from $\{0, 1, ..., 100\}$ that is NOT a row sum.

Also, total black cells = $100k$, so $100k = 5050 - m$, meaning $m = 5050 - 100k$.

For $m$ to be in $\{0, 1, ..., 100\}$, we need $5050 - 100k \in \{0, 1, ..., 100\}$, so $100k \in \{4950, 4951, ..., 5050\}$, meaning $k \in \{49.5, ..., 50.5\}$, so $k = 50$ and $m = 50$.

Wait, let me reconsider. $100k = 5050 - m$, and $0 \le m \le 100$, so $4950 \le 100k \le 5050$, so $49.5 \le k \le 50.5$, so $k = 50$ and $m = 5050 - 5000 = 50$.

So each column has exactly 50 black cells, and the row sums are $\{0, 1, 2, ..., 100\} \setminus \{50\}$.

Now, we want to maximize the number of adjacent pairs of different colors.

Adjacent pairs can be horizontal (within a row) or vertical (within a column).

Let me think about the total number of "color changes" along rows and columns.

For a row with $r$ black cells, the number of horizontal adjacent pairs of different colors is at most... well, if the black cells are arranged to maximize transitions, the maximum number of transitions in a row of length 100 with $r$ black cells is $2 \min(r, 100-r)$ if $r \neq 50$... wait, let me think more carefully.

Actually, the number of horizontal transitions in a row depends on the arrangement. If a row has $r$ black cells and $100-r$ white cells, the maximum number of adjacent pairs with different colors is $2 \min(r, 100-r)$ if $r \neq 0$ and $r \neq 100$... no wait.

If we arrange the row as alternating as much as possible. The maximum number of transitions (adjacent different pairs) in a binary string of length $n$ with $r$ ones is $2\min(r, n-r)$ if $r \neq n/2$... hmm, actually no.

Let me think again. A binary string of length $n$ with $r$ ones. The number of transitions (positions where adjacent bits differ) is maximized when we alternate as much as possible. 

If $r \leq n-r$ (i.e., $r \leq n/2$), we can arrange as BWBWBW...BWBWW...W, giving $2r$ transitions (if $r < n-r$) or $2r-1$ transitions (if $r = n-r$, but that's when $r = n/2$... actually if $r = n-r$, we can do BWBW...BW which gives $n-1$ transitions).

Wait, let me be more careful. If $r \leq n - r$, the maximum number of transitions is $2r$ if $r < n - r$, and $n - 1$ if $r = n - r$ (i.e., $r = n/2$).

Hmm, actually when $r = n - r = n/2$, we can alternate perfectly: BWBW...BW or WBWB...WB, giving $n-1$ transitions. And $2r = n$, but $n - 1 < n$, so the formula $2r$ doesn't apply when $r = n - r$.

Let me reconsider. The maximum number of transitions in a binary string of length $n$ with $r$ ones:
- If $r = 0$ or $r = n$: 0 transitions.
- If $0 < r < n$: The maximum is $2\min(r, n-r)$ if $r \neq n-r$, and $n-1$ if $r = n-r$.

Wait, when $r = n - r$, $2\min(r, n-r) = 2r = n$, but the actual max is $n - 1$. So the formula is $\min(2\min(r, n-r), n-1)$.

Actually, $2\min(r, n-r) \leq n$ always, and when $r = n-r$, $2\min(r,n-r) = n > n-1$. So the max is $\min(2\min(r, n-r), n-1)$.

But when $r \neq n-r$, $2\min(r, n-r) < n$, so $2\min(r, n-r) \leq n-1$... is that true? If $r < n-r$, then $2r < n$, so $2r \leq n-1$ (since both are integers and $n$ is even... well $n = 100$). If $r < 50$, $2r \leq 98 < 99 = n-1$. If $r = 49$, $2r = 98 < 99$. So yes, when $r \neq 50$, $2\min(r, 100-r) \leq 98 < 99$.

OK so for horizontal transitions, the max per row with $r$ black cells is:
- $2\min(r, 100-r)$ if $r \neq 50$
- $99$ if $r = 50$

But $r = 50$ is excluded from our row sums! So every row has $r \neq 50$, and the max horizontal transitions per row is $2\min(r, 100-r)$.

Now, the row sums are $\{0, 1, 2, ..., 100\} \setminus \{50\}$. The sum of $2\min(r, 100-r)$ over these values:

For $r = 0$: $0$
For $r = 1, 2, ..., 49$: $2r$, sum = $2 \cdot (1+2+...+49) = 2 \cdot 49 \cdot 50 / 2 = 2450$
For $r = 51, 52, ..., 100$: $2(100-r)$, which for $r = 51$ gives $98$, $r = 52$ gives $96$, ..., $r = 100$ gives $0$. Sum = $2(49 + 48 + ... + 0) = 2 \cdot 49 \cdot 50 / 2 = 2450$.
For $r = 50$: excluded.

Total max horizontal transitions = $0 + 2450 + 2450 = 4900$.

But wait, this is the maximum if we can independently optimize each row. But we have the constraint that each column has exactly 50 black cells. So we can't independently optimize rows.

Hmm, this is the key constraint. Let me think about this differently.

Actually, the problem is to maximize the total number of adjacent different-color pairs, which includes both horizontal and vertical adjacencies.

Let me think about this more carefully.

Total adjacent pairs = horizontal pairs + vertical pairs.

Horizontal pairs: pairs $(i,j)$ and $(i,j+1)$ that differ. There are $100 \times 99 = 9900$ horizontal adjacent pairs total.

Vertical pairs: pairs $(i,j)$ and $(i+1,j)$ that differ. There are $99 \times 100 = 9900$ vertical adjacent pairs total.

We want to maximize the number of pairs that differ.

Let me think about an upper bound.

For horizontal pairs: In row $i$ with $r_i$ black cells, the number of horizontal different pairs is at most $2\min(r_i, 100 - r_i)$. As computed, the sum over all rows is at most 4900.

For vertical pairs: In column $j$ with 50 black cells, the number of vertical different pairs is at most $99$ (achieved by perfect alternation, but 50 black and 50 white in a column of 100 can alternate perfectly giving 99 transitions). So the max vertical pairs is $100 \times 99 = 9900$.

But can we achieve both simultaneously? Probably not, since the row constraints and column constraints interact.

Let me think about this differently. Let me consider the total number of "edges" in the grid graph that connect cells of different colors.

Actually, let me think about what arrangement could maximize this.

Let me consider the problem from the perspective of the column constraint. Each column has exactly 50 black cells. To maximize vertical transitions, we want each column to alternate as much as possible. With 50 black and 50 white in a column of 100, perfect alternation gives 99 vertical transitions per column, total 9900.

But if columns alternate perfectly, what do the rows look like? If column $j$ has the pattern BWBW...BW (starting with black), then row $i$ gets black in column $j$ if $i$ is odd (say). If all columns have the same pattern, then each row is either all black or all white, giving 0 horizontal transitions. That's bad.

So there's a trade-off. Let me think about what the optimal arrangement looks like.

Let me consider a different approach. Let's think of the grid as a matrix $A \in \{0,1\}^{100 \times 100}$.

The number of horizontal different pairs in row $i$ is related to the number of "runs" in row $i$. If row $i$ has $t_i$ transitions, then it has $t_i + 1$ runs (assuming $t_i > 0$; if $t_i = 0$, it has 1 run).

Hmm, let me think about this problem differently.

Let me consider the "disagreement" approach. Define $B_{ij} = 2A_{ij} - 1 \in \{-1, +1\}$. Then two adjacent cells differ iff their $B$ values have opposite signs, i.e., $B_{ij} \cdot B_{i'j'} = -1$.

The number of different adjacent pairs = (total adjacent pairs - same-color adjacent pairs) / ... hmm, this might not simplify easily.

Actually, the number of different adjacent pairs = $\frac{1}{2} \sum_{\text{adjacent } (c_1, c_2)} (1 - B_{c_1} B_{c_2})$... no, that's $\frac{1}{2}(E - \sum B_{c_1} B_{c_2})$ where $E$ is the total number of adjacent pairs. But $B_{c_1} B_{c_2} = 1$ if same color, $-1$ if different. So the number of different pairs = $\frac{E - \sum B_{c_1} B_{c_2}}{2}$.

To maximize different pairs, we minimize $\sum B_{c_1} B_{c_2}$.

$\sum B_{c_1} B_{c_2} = \sum_{\text{horizontal}} B_{ij} B_{i,j+1} + \sum_{\text{vertical}} B_{ij} B_{i+1,j}$.

Hmm, this is like minimizing an Ising energy. This is a hard optimization problem in general, but the constraints here are specific.

Let me think about specific constructions.

Construction idea: Let's try to make the grid look like a "staircase" pattern.

Since row sums are $\{0, 1, 2, ..., 49, 51, 52, ..., 100\}$, let's assign row $i$ (for $i = 0, 1, ..., 49$) to have $i$ black cells, and row $i$ (for $i = 50, 51, ..., 99$) to have $i+1$ black cells. So row sums are $0, 1, 2, ..., 49, 51, 52, ..., 100$.

Now, for the column constraint: each column has 50 black cells.

One natural construction: make row $i$ have its black cells in the first $r_i$ columns. Then column $j$ has black cells in all rows $i$ where $r_i \geq j+1$ (0-indexed columns). 

With row sums $0, 1, 2, ..., 49, 51, 52, ..., 100$:
- Column 0 (first column): black in rows with $r_i \geq 1$, i.e., all rows except row 0. That's 99 rows. Not 50.

This doesn't satisfy the column constraint. We need to be smarter.

Let me think about this differently. We need each column to have exactly 50 black cells, and the row sums to be $\{0, 1, ..., 49, 51, ..., 100\}$.

One approach: think of this as a bipartite degree sequence problem. We have a bipartite graph with 100 row-nodes and 100 column-nodes. Row $i$ has degree $r_i$ and each column has degree 50. The Gale-Ryser theorem tells us when such a bipartite graph exists.

The row degree sequence is $\{0, 1, 2, ..., 49, 51, 52, ..., 100\}$ (sorted descending: $100, 99, ..., 51, 49, ..., 1, 0$). The column degree sequence is $(50, 50, ..., 50)$.

By Gale-Ryser, this is realizable iff the row sequence is majorized by the conjugate of the column sequence. The conjugate of $(50, 50, ..., 50)$ (100 times) is: $d^*_j = $ number of columns with degree $\geq j$. Since all columns have degree 50, $d^*_j = 100$ for $j \leq 50$ and $d^*_j = 0$ for $j > 50$. So the conjugate sequence is $(100, 100, ..., 100, 0, 0, ..., 0)$ (50 hundreds and 50 zeros).

The row sequence sorted descending is $(100, 99, 98, ..., 51, 49, 48, ..., 1, 0)$.

Gale-Ryser condition: for each $k$, $\sum_{i=1}^{k} r_i \leq \sum_{i=1}^{k} d^*_i$.

For $k \leq 50$: $\sum_{i=1}^{k} r_i = 100 + 99 + ... + (101-k) = k(201-k)/2$. And $\sum_{i=1}^{k} d^*_i = 100k$. So we need $k(201-k)/2 \leq 100k$, i.e., $(201-k)/2 \leq 100$, i.e., $201-k \leq 200$, i.e., $k \geq 1$. True for all $k \geq 1$.

For $k = 50$: $\sum_{i=1}^{50} r_i = 100 + 99 + ... + 51 = 50 \cdot 151 / 2 = 3775$. $\sum_{i=1}^{50} d^*_i = 5000$. $3775 \leq 5000$. ✓

For $k > 50$: $\sum_{i=1}^{k} d^*_i = 5000$ (since $d^*_i = 0$ for $i > 50$). $\sum_{i=1}^{k} r_i$ = total sum = 5000. So $5000 \leq 5000$. ✓ (with equality for $k = 100$).

So the bipartite graph exists. Good.

Now, among all such bipartite graphs (i.e., all valid colorings), we want to maximize the number of adjacent different-color pairs.

This is a complex optimization. Let me think about upper bounds and then try to construct a matching lower bound.

Upper bound on horizontal transitions: 4900 (as computed).
Upper bound on vertical transitions: 9900 (if all columns alternate perfectly).

But these can't both be achieved simultaneously. Let me think about what trade-offs are possible.

Let me consider a specific construction and count.

Construction: "Staircase with alternating columns."

Actually, let me think about this more carefully. Let me consider the following approach.

Let me think about the vertical transitions first. In column $j$, we have 50 black and 50 white cells. The maximum vertical transitions is 99 (perfect alternation). But the arrangement in each column is constrained by the row sums.

Let me try a different approach. Let me think about what happens if we use a "threshold" construction.

Sort rows by their sum: row 0 has sum 0, row 1 has sum 1, ..., row 49 has sum 49, row 50 has sum 51, ..., row 99 has sum 100.

For the "left-justified" construction (black cells in first $r_i$ columns of row $i$):
- Column $j$ has black cells in rows where $r_i > j$.
- For $j = 0$: rows with $r_i \geq 1$ = all except row 0 = 99 rows. Not 50.

This doesn't work for the column constraint. Let me think of a construction that satisfies the column constraint.

Alternative: "complementary" construction. 

Actually, let me think about this problem from a higher level. The key insight might be that we should think about the problem in terms of the "boundary" between black and white regions.

Let me try a specific construction. Consider the following:

Arrange the rows in order of increasing row sum: $r_0 = 0, r_1 = 1, ..., r_{49} = 49, r_{50} = 51, ..., r_{99} = 100$.

For each row, place the black cells to create a "staircase" pattern, but also interleave to create vertical transitions.

Hmm, this is getting complicated. Let me think about it differently.

Let me consider the problem as follows. We want to maximize:
$$\sum_{i=1}^{100} h_i + \sum_{j=1}^{100} v_j$$
where $h_i$ is the number of horizontal transitions in row $i$ and $v_j$ is the number of vertical transitions in column $j$.

For row $i$ with $r_i$ black cells: $h_i \leq 2\min(r_i, 100-r_i)$.
For column $j$ with 50 black cells: $v_j \leq 99$.

But these are not independent. Let me think about a combined upper bound.

Actually, let me think about a clever construction.

Construction idea: "Checkerboard-like with staircase modification."

Consider a perfect checkerboard pattern: cell $(i,j)$ is black if $i+j$ is even. This gives 50 black cells per column (since 100 is even, each column has 50 black and 50 white). Each row also has 50 black cells. Horizontal transitions: 99 per row, total 9900. Vertical transitions: 99 per column, total 9900. Total: 19800.

But the row sums are all 50, which violates the "different number of black cells per row" constraint. We need to modify this.

The idea: start from the checkerboard and modify it to get the desired row sums while preserving the column sums and maximizing the retained transitions.

In the checkerboard, each row has 50 black cells. We need row sums to be $\{0, 1, ..., 49, 51, ..., 100\}$. So we need to change the number of black cells in each row.

For row $i$ that needs $r_i$ black cells, we need to change $|r_i - 50|$ cells. If $r_i > 50$, we need to turn $r_i - 50$ white cells black. If $r_i < 50$, we need to turn $50 - r_i$ black cells white.

Each change we make will potentially reduce the number of transitions. Let's think about how to minimize the damage.

If we change a cell from its checkerboard color, it might now match its neighbors, reducing transitions. In the checkerboard, every cell differs from all its neighbors. If we flip a cell, it now matches all its neighbors (up to 4), reducing transitions by up to 4 (but edge cells have fewer neighbors).

Actually, flipping a cell in the interior changes its relationship with up to 4 neighbors. Before the flip, all 4 edges were "different." After the flip, all 4 edges become "same." So we lose up to 4 transitions per flip. But if we flip multiple adjacent cells, the effect is more complex.

Hmm, let me think about this more carefully. 

Actually, let me think about it in terms of "runs." In the checkerboard, every row is an alternating sequence of length 100, giving 99 transitions. If we modify row $i$ to have $r_i$ black cells instead of 50, we need to change $|r_i - 50|$ cells.

The key insight: if we change cells in a "block" fashion, we create a contiguous region of same-colored cells, which reduces transitions only at the boundaries of the block.

For example, if in row $i$ (which originally alternates BWBWBW...), we change a contiguous block of cells to all black, we create a region where the pattern is disrupted. The transitions lost are only at the two boundaries of the block.

Wait, but this is getting complicated because we also need to maintain the column constraint.

Let me think about this differently. Let me consider a construction where:
- The grid is mostly a checkerboard.
- We modify it by "shifting" rows to adjust their sums.

Actually, let me think about a cleaner construction.

Construction: "Row-shifted checkerboard."

Consider the checkerboard where cell $(i,j)$ is black iff $i + j \equiv 0 \pmod{2}$. Each row has 50 black cells, each column has 50 black cells.

Now, for row $i$, suppose we want $r_i$ black cells. If $r_i = 50 + d$ (where $d > 0$), we need to add $d$ more black cells. If $r_i = 50 - d$ (where $d > 0$), we need to remove $d$ black cells.

To add black cells to a row while maintaining column sums, we need to remove black cells from other rows in the same columns. This is like a "swap" operation.

This is getting complex. Let me try a different approach entirely.

Let me think about the problem in terms of a specific well-structured construction.

Construction: "Two-block staircase."

Divide the grid into two halves: top 50 rows and bottom 50 rows.

In the top 50 rows, assign row sums $0, 1, 2, ..., 49$.
In the bottom 50 rows, assign row sums $51, 52, ..., 100$.

For the top half (rows with sums $0, 1, ..., 49$): use a left-justified staircase. Row $i$ (for $i = 0, ..., 49$) has black cells in columns $0, 1, ..., i-1$ (so $i$ black cells). 

Column $j$ in the top half has black cells in rows $j+1, j+2, ..., 49$, which is $49 - j$ black cells.

For the bottom half (rows with sums $51, 52, ..., 100$): we need each column to have $50 - (49 - j) = j + 1$ black cells in the bottom half. So column $j$ needs $j + 1$ black cells in the bottom 50 rows.

Bottom half rows have sums $51, 52, ..., 100$. Row $i$ (for $i = 50, ..., 99$) has sum $i + 1$. So row 50 has sum 51, ..., row 99 has sum 100.

For the bottom half, we can use a right-justified staircase. Row $i$ (for $i = 50, ..., 99$) with sum $i + 1$: place black cells in columns $100 - (i+1), ..., 99$, i.e., the last $i + 1$ columns. Wait, that's $i + 1$ black cells. 

Column $j$ in the bottom half: black cells in rows $i$ where $j \geq 100 - (i+1)$, i.e., $i \geq 99 - j$. So rows $99 - j, 100 - j, ..., 99$... wait, let me re-index.

Row $i$ (for $i = 50, ..., 99$) has black cells in columns $99 - (i+1) + 1 = 99 - i$ through $99$... hmm, let me be more careful.

Row $i$ has sum $s_i = i + 1$ (for $i = 50, ..., 99$). Place black cells in the last $s_i$ columns: columns $100 - s_i$ through $99$. So column $j$ is black in row $i$ iff $j \geq 100 - s_i = 100 - (i+1) = 99 - i$, i.e., $i \geq 99 - j$.

For the bottom half (rows 50 to 99), column $j$ has black cells in rows $\max(50, 99-j)$ through $99$.

If $99 - j \geq 50$, i.e., $j \leq 49$: black in rows $99-j$ through $99$, which is $j + 1$ rows. ✓
If $99 - j < 50$, i.e., $j \geq 50$: black in rows $50$ through $99$, which is $50$ rows.

But we need column $j$ to have $j + 1$ black cells in the bottom half. For $j \geq 50$, we get 50, but we need $j + 1 \geq 51$. This doesn't work!

The issue is that for $j \geq 50$, the right-justified staircase gives all 50 rows black, but we need more than 50 black cells in those columns from the bottom half.

Let me reconsider. Total black cells in column $j$: from top half $= 49 - j$ (for $j \leq 49$) or $0$ (for $j \geq 50$). We need total $= 50$.

For $j \leq 49$: need $50 - (49 - j) = j + 1$ from bottom half.
For $j \geq 50$: need $50 - 0 = 50$ from bottom half.

Bottom half has 50 rows with sums $51, 52, ..., 100$. Total = $51 + 52 + ... + 100 = 50 \cdot 151 / 2 = 3775$.

Sum of column needs from bottom half: $\sum_{j=0}^{49} (j+1) + \sum_{j=50}^{99} 50 = (1 + 2 + ... + 50) + 50 \cdot 50 = 1275 + 2500 = 3775$. ✓

So the column needs are consistent. But the right-justified staircase doesn't satisfy them. Let me find a different arrangement for the bottom half.

For the bottom half, we need column $j$ to have:
- $j + 1$ black cells for $j = 0, 1, ..., 49$
- $50$ black cells for $j = 50, 51, ..., 99$

And row $i$ (for $i = 50, ..., 99$) has sum $i + 1$.

This is another bipartite degree sequence problem. The column degrees in the bottom half are $(1, 2, 3, ..., 50, 50, 50, ..., 50)$ and row degrees are $(51, 52, ..., 100)$.

Hmm, this is getting complicated. Let me try a completely different approach.

Let me think about the problem more abstractly.

Alternative approach: Think about the maximum number of transitions in terms of a formula.

Let $a_{ij} \in \{0, 1\}$. The number of horizontal transitions in row $i$ is $\sum_{j=1}^{99} |a_{i,j} - a_{i,j+1}|$. The number of vertical transitions in column $j$ is $\sum_{i=1}^{99} |a_{i,j} - a_{i+1,j}|$.

Total transitions $T = \sum_{i,j} |a_{i,j} - a_{i,j+1}| + \sum_{i,j} |a_{i,j} - a_{i+1,j}|$.

Now, $|a - b| = a + b - 2ab$ for $a, b \in \{0, 1\}$.

So $\sum_{j=1}^{99} |a_{i,j} - a_{i,j+1}| = \sum_{j=1}^{99} (a_{i,j} + a_{i,j+1} - 2a_{i,j}a_{i,j+1})$.

$= a_{i,1} + a_{i,100} + 2\sum_{j=2}^{99} a_{i,j} - 2\sum_{j=1}^{99} a_{i,j}a_{i,j+1}$

$= a_{i,1} + a_{i,100} + 2(r_i - a_{i,1} - a_{i,100}) - 2\sum_{j=1}^{99} a_{i,j}a_{i,j+1}$

Hmm wait, $\sum_{j=1}^{99} (a_{i,j} + a_{i,j+1}) = a_{i,1} + 2(a_{i,2} + ... + a_{i,99}) + a_{i,100} = 2r_i - a_{i,1} - a_{i,100}$.

So horizontal transitions in row $i$ = $2r_i - a_{i,1} - a_{i,100} - 2\sum_{j=1}^{99} a_{i,j}a_{i,j+1}$.

Similarly, vertical transitions in column $j$ = $2 \cdot 50 - a_{1,j} - a_{100,j} - 2\sum_{i=1}^{99} a_{i,j}a_{i+1,j} = 100 - a_{1,j} - a_{100,j} - 2\sum_{i=1}^{99} a_{i,j}a_{i+1,j}$.

Total $T = \sum_i (2r_i - a_{i,1} - a_{i,100}) + \sum_j (100 - a_{1,j} - a_{100,j}) - 2\sum_{i,j} a_{i,j}a_{i,j+1} - 2\sum_{i,j} a_{i,j}a_{i+1,j}$.

$= 2 \cdot 5000 - \sum_i (a_{i,1} + a_{i,100}) + 10000 - \sum_j (a_{1,j} + a_{100,j}) - 2S$

where $S = \sum_{i,j} a_{i,j}a_{i,j+1} + \sum_{i,j} a_{i,j}a_{i+1,j}$ is the total number of adjacent same-color-black pairs.

$T = 20000 - \sum_i (a_{i,1} + a_{i,100}) - \sum_j (a_{1,j} + a_{100,j}) - 2S$.

To maximize $T$, we want to minimize $\sum_i (a_{i,1} + a_{i,100}) + \sum_j (a_{1,j} + a_{100,j}) + 2S$.

Note that $\sum_i (a_{i,1} + a_{i,100}) = $ (number of black cells in column 1) + (number of black cells in column 100) = $50 + 50 = 100$.

Similarly, $\sum_j (a_{1,j} + a_{100,j}) = r_1 + r_{100}$ (the row sums of row 1 and row 100, using 1-indexed).

Wait, I need to be careful with indexing. Let me use 1-indexed. Rows 1 to 100, columns 1 to 100.

$\sum_i (a_{i,1} + a_{i,100}) = c_1 + c_{100} = 50 + 50 = 100$ (each column has 50 black cells).

$\sum_j (a_{1,j} + a_{100,j}) = r_1 + r_{100}$ (row sums of first and last rows).

So $T = 20000 - 100 - (r_1 + r_{100}) - 2S = 19900 - (r_1 + r_{100}) - 2S$.

To maximize $T$, we want to minimize $r_1 + r_{100} + 2S$.

$S$ is the total number of adjacent pairs where both cells are black. $S = S_h + S_v$ where $S_h = \sum_{i=1}^{100}\sum_{j=1}^{99} a_{i,j}a_{i,j+1}$ and $S_v = \sum_{i=1}^{99}\sum_{j=1}^{100} a_{i,j}a_{i+1,j}$.

To minimize $S$, we want to spread out black cells so that few black cells are adjacent to each other.

This is related to the "independence number" type problem. We want to place black cells so that few are adjacent.

But we have constraints: each column has 50 black cells, and row sums are $\{0, 1, ..., 49, 51, ..., 100\}$.

Hmm, let me think about lower bounds on $S$.

For column $j$ with 50 black cells out of 100, the minimum number of vertically adjacent black-black pairs is... if we spread the 50 black cells as far apart as possible, we can place them in positions 1, 3, 5, ..., 99 (every other position). Then no two black cells in the column are vertically adjacent, so $S_v^{(j)} = 0$. This is possible since 50 black cells can be placed in 50 non-adjacent positions out of 100 (exactly every other one).

So potentially $S_v = 0$ if we can arrange each column to have no vertically adjacent black cells. But this requires coordinating with the row sums.

Similarly, for row $i$ with $r_i$ black cells, the minimum number of horizontally adjacent black-black pairs is $\max(0, r_i - \lceil 100/2 \rceil) = \max(0, r_i - 50)$. For $r_i \leq 50$, we can place black cells with no two adjacent, giving $S_h^{(i)} = 0$. For $r_i > 50$, we must have some adjacent black cells. Specifically, with $r_i$ black cells in 100 positions, the minimum number of adjacent black-black pairs is $\max(0, 2r_i - 100 - 1) = \max(0, 2r_i - 101)$... 

wait, let me think again. If we have $r$ black cells in $n$ positions, the minimum number of adjacent black-black pairs is $\max(0, r - \lceil n/2 \rceil)$... no, that's not right either.

If $r \leq \lceil n/2 \rceil$, we can place them with no two adjacent (e.g., in positions 1, 3, 5, ...), so minimum is 0.

If $r > \lceil n/2 \rceil$, we need to place some adjacent. With $n = 100$ and $\lceil n/2 \rceil = 50$: if $r > 50$, we need at least $r - 50$ "extra" black cells beyond what can be placed non-adjacently. Each extra black cell must be adjacent to at least one other black cell. But the minimum number of adjacent pairs is more subtle.

Actually, if we have $r$ black cells in $n$ positions and want to minimize adjacent black-black pairs, we should place them as spread out as possible. The minimum is $\max(0, 2r - n - 1)$ when $r > n/2$... let me verify.

For $n = 100$, $r = 51$: we can place 50 black cells in positions 1, 3, 5, ..., 99 (non-adjacent), and 1 more in any even position, say position 2. This creates 2 adjacent pairs: (1,2) and (2,3). So minimum is 2. And $2 \cdot 51 - 100 - 1 = 1$. That's not right.

Hmm, let me reconsider. With $r = 51$ in $n = 100$: place in positions 1, 2, 4, 6, 8, ..., 100. That's positions 1, 2, and then 49 even positions from 4 to 100. Wait, 4, 6, ..., 100 is 49 positions. Plus 1 and 2 = 51 total. Adjacent pairs: (1,2) only. So minimum is 1.

$2r - n - 1 = 102 - 100 - 1 = 1$. ✓

For $r = 52$: place in 1, 2, 4, 5, 7, 8, 10, 11, ..., or 1, 2, 3, 5, 7, 9, ..., 99. Hmm, let me think. Place in 1, 2, 4, 6, ..., 98, 100. That's 1, 2, and 49 even positions (4, 6, ..., 100) = 51. Need one more. Add 3: now we have 1, 2, 3, 4, 6, 8, ..., 100. Adjacent pairs: (1,2), (2,3), (3,4) = 3. Or: 1, 2, 4, 5, 7, 9, ..., 99. That's 1, 2, 4, 5, and 7, 9, ..., 99 (47 positions) = 51. Need one more. Hmm.

Actually, let me think about it differently. Place black cells in a pattern that minimizes adjacent pairs. The optimal is to place them in "pairs": BB_BB_BB_... where _ is a gap. With $r$ black cells, we have $\lfloor r/2 \rfloor$ pairs and possibly one singleton. Each pair contributes 1 adjacent pair. The pairs need to be separated by at least one gap.

With $r$ black cells forming $\lfloor r/2 \rfloor$ pairs and possibly 1 singleton, we need $\lfloor r/2 \rfloor + (r \mod 2) + \lfloor r/2 \rfloor - 1 = r - 1$... no, this isn't right.

Let me think about it more carefully. We want to place $r$ black cells in $n$ positions to minimize the number of adjacent black-black pairs.

The optimal arrangement is to place the black cells in "blocks" of size 2 (or 1), separated by gaps of size 1. 

If $r \leq n/2$: all singletons, 0 adjacent pairs.
If $r > n/2$: we need $r - n/2$ "extra" cells. Each extra cell turns a singleton into a pair (or extends a pair). 

Actually, think of it as: we have $n$ positions. We can place at most $\lceil n/2 \rceil$ "blocks" (where a block is a maximal run of black cells). If we have $b$ blocks with sizes $s_1, ..., s_b$ (summing to $r$), the number of adjacent pairs is $\sum (s_i - 1) = r - b$. To minimize this, we maximize $b$. The maximum number of blocks is $\min(r, \lceil n/2 \rceil)$ (since blocks must be separated by at least one white cell, and we need $b$ blocks and $b-1$ gaps, so $b + (b-1) \leq n$, giving $b \leq (n+1)/2$; also $b \leq r$).

For $n = 100$: max blocks = $\min(r, 50)$ (since $(100+1)/2 = 50.5$, so $b \leq 50$).

Wait, $b \leq \lfloor (n+1)/2 \rfloor = 50$ for $n = 100$.

So minimum adjacent pairs = $r - \min(r, 50) = \max(0, r - 50)$.

For $r = 51$: min = 1. ✓ (matches our earlier calculation)
For $r = 52$: min = 2.
For $r = 100$: min = 50.

So the minimum horizontal black-black adjacent pairs in row $i$ is $\max(0, r_i - 50)$.

Sum over all rows: $\sum_i \max(0, r_i - 50) = \sum_{r=51}^{100} (r - 50) = 1 + 2 + ... + 50 = 1275$.

So $S_h \geq 1275$.

Similarly, for vertical black-black adjacent pairs: each column has 50 black cells, so minimum is $\max(0, 50 - 50) = 0$ per column. So $S_v \geq 0$.

But can we achieve $S_v = 0$ while also achieving $S_h = 1275$? That's the question.

If $S_v = 0$ and $S_h = 1275$, then $S = 1275$ and $T = 19900 - (r_1 + r_{100}) - 2 \cdot 1275 = 19900 - (r_1 + r_{100}) - 2550 = 17350 - (r_1 + r_{100})$.

To maximize $T$, we minimize $r_1 + r_{100}$. The minimum possible value of $r_1 + r_{100}$ is $0 + 1 = 1$ (if the first and last rows have sums 0 and 1). But wait, we can choose which row is first and which is last. The row sums are $\{0, 1, ..., 49, 51, ..., 100\}$. We can arrange the rows in any order. So we can set $r_1 = 0$ and $r_{100} = 1$, giving $r_1 + r_{100} = 1$.

But wait, can we simultaneously achieve $S_v = 0$, $S_h = 1275$, and $r_1 + r_{100} = 1$? These might not be compatible.

Let me think about whether $S_v = 0$ and $S_h = 1275$ can be achieved simultaneously.

$S_v = 0$ means no two vertically adjacent cells are both black. This means in each column, the 50 black cells are placed in non-adjacent positions. Since there are 100 positions and 50 black cells, the only way to place 50 non-adjacent black cells in 100 positions is to place them in either all even positions or all odd positions (or a subset, but we need exactly 50, so it must be all even or all odd).

Wait, that's not quite right. We need 50 non-adjacent positions out of 100. The maximum number of non-adjacent positions in 100 is 50 (positions 1, 3, 5, ..., 99 or 2, 4, 6, ..., 100). So to have 50 non-adjacent black cells, we must use exactly one of these two patterns: all odd positions or all even positions.

So $S_v = 0$ requires each column to have black cells in either all odd rows or all even rows. This is a very restrictive condition!

If column $j$ has black cells in all odd rows, then rows 1, 3, 5, ..., 99 each have a black cell in column $j$. If column $j$ has black cells in all even rows, then rows 2, 4, 6, ..., 100 each have a black cell in column $j$.

Let's say column $j$ is "odd-type" if it has black cells in odd rows, and "even-type" if it has black cells in even rows. Let $p$ be the number of odd-type columns and $q = 100 - p$ be the number of even-type columns.

Row $i$ (odd) has black cells in all odd-type columns, so $r_i = p$ for all odd $i$.
Row $i$ (even) has black cells in all even-type columns, so $r_i = q$ for all even $i$.

But we need all row sums to be different! With this construction, all odd rows have the same sum $p$ and all even rows have the same sum $q$. This gives at most 2 distinct row sums, not 100. So $S_v = 0$ is incompatible with the row sum constraint (unless we relax it).

So we can't achieve $S_v = 0$. We need to allow some vertical adjacent black-black pairs.

OK so this approach of trying to minimize $S$ directly is complex. Let me think about the problem differently.

Let me reconsider. The formula is:
$$T = 19900 - (r_1 + r_{100}) - 2S$$

where $S = S_h + S_v$ is the total number of adjacent black-black pairs.

We want to minimize $r_1 + r_{100} + 2S_h + 2S_v$.

We know $S_h \geq 1275$ (from the row sum constraints). We need to figure out the minimum of $S_v$ given the constraints.

But $S_h$ and $S_v$ are coupled through the grid structure. Let me think about this more carefully.

Actually, wait. The bound $S_h \geq 1275$ assumes we can independently optimize each row's horizontal arrangement. But the column constraint couples the rows. So the actual minimum of $S_h + S_v$ might be higher.

Let me think about a lower bound on $S = S_h + S_v$.

Hmm, this is getting complicated. Let me try a different approach: construct a specific grid and count the transitions, then try to prove it's optimal.

Let me try the "staircase" construction.

Construction: Order rows by increasing sum: row 1 has sum 0, row 2 has sum 1, ..., row 50 has sum 49, row 51 has sum 51, ..., row 100 has sum 100.

For rows 1 to 50 (sums 0 to 49): place black cells in columns 1 to $r_i$ (left-justified).
For rows 51 to 100 (sums 51 to 100): place black cells in columns $101 - r_i$ to 100 (right-justified).

Wait, let me check the column sums.

Column $j$:
- From rows 1-50: black in row $i$ iff $r_i \geq j$, i.e., $i \geq j$ (since $r_i = i - 1$ for row $i$, so $r_i \geq j$ iff $i - 1 \geq j$ iff $i \geq j + 1$). So black in rows $j+1, j+2, ..., 50$, which is $50 - j$ rows. For $j \leq 49$, this is $50 - j \geq 1$. For $j = 50$, this is 0.

Wait, I need to be more careful. Row $i$ (for $i = 1, ..., 50$) has sum $r_i = i - 1$. Black cells in columns 1 to $i - 1$. So column $j$ is black in row $i$ iff $j \leq i - 1$, i.e., $i \geq j + 1$. So for $j = 1$: rows 2, 3, ..., 50, which is 49 rows. For $j = 2$: rows 3, ..., 50 = 48 rows. ... For $j = 49$: row 50 = 1 row. For $j = 50$: no rows = 0.

- From rows 51-100: row $i$ (for $i = 51, ..., 100$) has sum $r_i = i$ (since row 51 has sum 51, ..., row 100 has sum 100, so $r_i = i$). Wait, let me re-define. Row 51 has sum 51, row 52 has sum 52, ..., row 100 has sum 100. So $r_i = i$ for $i = 51, ..., 100$? No, $r_{51} = 51$, $r_{52} = 52$, ..., $r_{100} = 100$. So $r_i = i$ for $i \geq 51$? $r_{51} = 51 = 51$. Yes.

Right-justified: black cells in columns $101 - r_i$ to 100, i.e., columns $101 - i$ to 100. So column $j$ is black in row $i$ iff $j \geq 101 - i$, i.e., $i \geq 101 - j$. For $j = 100$: $i \geq 1$, so all rows 51-100, which is 50 rows. For $j = 99$: $i \geq 2$, so rows 51-100 (since all $i \geq 51 \geq 2$), 50 rows. Wait, that can't be right.

Hmm, $i \geq 101 - j$. For $j = 100$: $i \geq 1$, all 50 rows (51-100). For $j = 99$: $i \geq 2$, all 50 rows. For $j = 51$: $i \geq 50$, so rows 51-100, all 50 rows. For $j = 50$: $i \geq 51$, so rows 51-100, all 50 rows. For $j = 49$: $i \geq 52$, so rows 52-100 = 49 rows. For $j = 1$: $i \geq 100$, so only row 100 = 1 row.

So column $j$ from bottom half:
- $j \geq 50$: 50 rows
- $j < 50$: $101 - j - 51 + 1 = 51 - j$... wait, $i \geq 101 - j$ and $i \leq 100$, so rows $101-j$ to $100$, but $i \geq 51$, so rows $\max(51, 101-j)$ to $100$.

For $j \leq 50$: $101 - j \geq 51$, so rows $101-j$ to $100$, which is $j$ rows.
For $j \geq 51$: $101 - j \leq 50 < 51$, so rows 51 to 100, which is 50 rows.

So total column $j$:
- $j = 1, ..., 49$: $(50 - j) + j = 50$. ✓
- $j = 50$: $0 + 50 = 50$. ✓
- $j = 51, ..., 100$: $0 + 50 = 50$. ✓

So the column sums are all 50. The construction works.

Now let me count the transitions.

Horizontal transitions:
- Rows 1-50 (left-justified, sums 0 to 49): Row $i$ has black in columns 1 to $i-1$, white in columns $i$ to 100. This is a single transition at the boundary between column $i-1$ and column $i$ (if $i > 1$). For $i = 1$ (sum 0): all white, 0 transitions. For $i = 2, ..., 50$: 1 transition each. Total: 49.

- Rows 51-100 (right-justified, sums 51 to 100): Row $i$ has white in columns 1 to $100 - i$, black in columns $101 - i$ to 100. Single transition at boundary between column $100 - i$ and $101 - i$. For $i = 100$ (sum 100): all black, 0 transitions. For $i = 51, ..., 99$: 1 transition each. Total: 49.

Total horizontal transitions: 49 + 49 = 98.

Vertical transitions:
Column $j$:
- $j = 1, ..., 49$: Black in rows $j+1, ..., 50$ (from top half) and rows $101-j, ..., 100$ (from bottom half). White in rows $1, ..., j$ and rows $51, ..., 100-j$.

So the pattern in column $j$ (from top to bottom) is:
- Rows 1 to $j$: white
- Rows $j+1$ to $50$: black
- Rows $51$ to $100-j$: white
- Rows $101-j$ to $100$: black

Transitions: at row $j$/$j+1$ (white to black): 1. At row $50$/$51$ (black to white): 1. At row $100-j$/$101-j$ (white to black): 1. Total: 3 transitions per column.

For $j = 1$: rows 1 = white, rows 2-50 = black, rows 51-99 = white, row 100 = black. Transitions: (1,2), (50,51), (99,100) = 3.
For $j = 49$: rows 1-49 = white, row 50 = black, row 51 = white, rows 52-100 = black. Transitions: (49,50), (50,51), (51,52) = 3.

- $j = 50$: Black in rows 51-100 (from bottom half), white in rows 1-50. One transition at row 50/51. Total: 1.

- $j = 51, ..., 100$: Black in rows 51-100 (from bottom half) and... from top half, column $j$ for $j \geq 51$: no black cells (since top half rows have at most 49 black cells, all in columns 1-49). So column $j$ for $j \geq 51$: white in rows 1-50, black in rows 51-100. One transition at row 50/51. Total: 1.

Wait, but for $j = 51, ..., 100$, from the bottom half, all 50 rows (51-100) are black. And from the top half, no rows are black. So column $j$ has black in rows 51-100 and white in rows 1-50. One transition.

So vertical transitions:
- $j = 1, ..., 49$: 3 each, total $49 \times 3 = 147$.
- $j = 50, ..., 100$: 1 each, total $51 \times 1 = 51$.

Total vertical transitions: $147 + 51 = 198$.

Total transitions: $98 + 198 = 296$.

That's very low! The staircase construction is bad for maximizing transitions. We need a construction that creates more transitions.

Let me think about better constructions.

The checkerboard gives 19800 transitions but has all row sums equal to 50. We need to perturb it.

Let me think about the perturbation approach more carefully.

Start with checkerboard: $a_{ij} = 1$ iff $i + j$ is even (using 1-indexed, so $i + j$ even means black). Each row has 50 black, each column has 50 black.

We need to change the row sums to $\{0, 1, ..., 49, 51, ..., 100\}$. The total change in row sums is 0 (since total black cells remain 5000).

For row $i$, the current sum is 50. We need to change it to $r_i$. The change is $r_i - 50$.

Rows with $r_i < 50$: need to remove $50 - r_i$ black cells (turn them white).
Rows with $r_i > 50$: need to add $r_i - 50$ black cells (turn them white to black).

To maintain column sums, each column must still have 50 black cells. So if we remove a black cell from column $j$ (in some row), we must add a black cell to column $j$ (in some other row). This is a "swap": in column $j$, turn one row's black to white and another row's white to black.

In the checkerboard, in column $j$, the black cells are in rows where $i + j$ is even, and white cells where $i + j$ is odd. A swap in column $j$ means: pick a black row $i_1$ (where $i_1 + j$ is even) and a white row $i_2$ (where $i_2 + j$ is odd), and swap their colors in column $j$. This changes row $i_1$'s sum by $-1$ and row $i_2$'s sum by $+1$.

So we need to perform a series of swaps to transform all row sums from 50 to the desired values.

The total number of "removals" needed is $\sum_{r_i < 50} (50 - r_i) = (50 + 49 + ... + 1) + (50 - 0) = $ wait, the row sums less than 50 are $0, 1, ..., 49$, so removals = $\sum_{r=0}^{49} (50 - r) = 50 + 49 + ... + 1 = 1275$.

Similarly, additions = $\sum_{r=51}^{100} (r - 50) = 1 + 2 + ... + 50 = 1275$.

So we need 1275 swaps. Each swap changes the color of 2 cells in one column.

Now, how does each swap affect the total number of transitions?

In the checkerboard, every adjacent pair is a "different" pair (19800 transitions). When we swap, we change 2 cells. Each cell has up to 4 neighbors. Changing a cell's color can affect up to 4 adjacent pairs.

Let me think about the effect of a single swap more carefully.

In column $j$, we swap row $i_1$ (was black, now white) and row $i_2$ (was white, now black). 

For row $i_1$, cell $(i_1, j)$ changes from black to white. Its neighbors are $(i_1, j-1)$, $(i_1, j+1)$, $(i_1-1, j)$, $(i_1+1, j)$. In the checkerboard, all neighbors were different (since checkerboard). After the change, cell $(i_1, j)$ is now the same as its neighbors (since it was different before, and now it's flipped). So each of the up to 4 edges incident to $(i_1, j)$ changes from "different" to "same", losing 1 transition each. But wait, the vertical neighbors $(i_1-1, j)$ and $(i_1+1, j)$ might also be affected by the swap if $i_2 = i_1 \pm 1$.

This is getting complicated. Let me think about it differently.

Let me consider the effect on the total transition count when we flip a single cell.

In the checkerboard, flipping cell $(i, j)$ from its checkerboard color to the opposite:
- All edges incident to $(i, j)$ were "different" (transitions). After flipping, they become "same" (not transitions).
- So we lose up to 4 transitions (or fewer if $(i, j)$ is on the boundary).

But if we flip multiple cells, and some of them are adjacent, the effect is different. If two adjacent cells are both flipped, the edge between them was "different" before and is still "different" after (both flipped). So we don't lose that transition.

This is the key insight! If we flip cells in a way that adjacent flipped cells "cancel" each other's effect on the shared edge, we can minimize the loss.

So the strategy is: flip cells in contiguous blocks, so that internal edges of the block are preserved (still transitions), and only boundary edges of the block are lost.

If we flip a contiguous block of $k$ cells in a row, the block has $k-1$ internal horizontal edges (preserved) and 2 boundary horizontal edges (lost). The vertical edges: each cell in the block has 2 vertical neighbors (above and below), and all $2k$ vertical edges are lost (unless the cells above/below are also flipped).

Hmm, this is still complex. Let me think about a specific construction.

Construction idea: "Modified checkerboard with row shifts."

Consider the checkerboard. For each row $i$, we want to change its sum from 50 to $r_i$. 

Idea: In row $i$, flip a contiguous block of cells. If $r_i < 50$, flip $50 - r_i$ black cells to white (choose a contiguous block of black cells). If $r_i > 50$, flip $r_i - 50$ white cells to black (choose a contiguous block of white cells).

But we need to maintain column sums. So the flips must be balanced per column.

This is still complex. Let me try yet another approach.

Let me think about the problem in terms of the formula:
$$T = 19900 - (r_1 + r_{100}) - 2S$$

We want to minimize $r_1 + r_{100} + 2S$.

We can choose the ordering of rows (which row is first, which is last). To minimize $r_1 + r_{100}$, we should put the rows with the smallest sums at the top and bottom. The two smallest sums are 0 and 1, so $r_1 + r_{100} \geq 1$ (we can achieve $r_1 + r_{100} = 1$ by putting sum-0 row first and sum-1 row last, or vice versa).

Actually wait, we can also put sum 0 at both ends? No, each sum appears exactly once. So the minimum is $0 + 1 = 1$.

Now, we need to minimize $S = S_h + S_v$.

$S_h \geq 1275$ (from row sum constraints, as each row with $r_i > 50$ contributes at least $r_i - 50$ to $S_h$).

$S_v \geq 0$.

But as we saw, $S_v = 0$ is very restrictive. Let me think about the minimum of $S_h + S_v$ more carefully.

Actually, let me think about a combined lower bound on $S_h + S_v$.

Consider the "disagreement" with the checkerboard. Define $b_{ij} = a_{ij} \oplus ((i+j) \mod 2)$, where $\oplus$ is XOR. So $b_{ij} = 1$ if cell $(i,j)$ differs from the checkerboard, 0 otherwise. The number of "flipped" cells is $\sum b_{ij}$.

In the checkerboard, $S = 0$ (no two adjacent black cells, since it's a proper 2-coloring). When we flip cells, we create adjacent black-black pairs.

Hmm, this isn't quite right because the checkerboard has no adjacent black-black pairs, but our grid might have a different structure.

Let me think about it differently. Let me use the $B_{ij} = 2a_{ij} - 1 \in \{-1, +1\}$ representation.

The checkerboard has $B_{ij} = (-1)^{i+j}$ (or similar). The "energy" $\sum_{\text{adjacent}} B_{c_1} B_{c_2}$ is minimized (most negative) for the checkerboard, since every adjacent pair has $B_{c_1} B_{c_2} = -1$.

Our formula: $T = \frac{E - \sum B_{c_1} B_{c_2}}{2}$ where $E = 19800$ (total adjacent pairs). So $T = \frac{19800 - \sum B_{c_1} B_{c_2}}{2} = 9900 - \frac{\sum B_{c_1} B_{c_2}}{2}$.

To maximize $T$, we minimize $\sum B_{c_1} B_{c_2}$.

For the checkerboard, $\sum B_{c_1} B_{c_2} = -19800$, giving $T = 9900 + 9900 = 19800$. But the checkerboard doesn't satisfy our row sum constraint.

Now, let's think about what happens when we perturb the checkerboard.

Let $B_{ij} = (-1)^{i+j}(1 - 2b_{ij})$ where $b_{ij} = 1$ if cell $(i,j)$ is flipped from checkerboard. Actually, $B_{ij} = (-1)^{i+j}$ if not flipped, $(-1)^{i+j+1}$ if flipped. So $B_{ij} = (-1)^{i+j}(1 - 2b_{ij})$.

Then $B_{c_1} B_{c_2} = (-1)^{i_1+j_1+i_2+j_2}(1-2b_{c_1})(1-2b_{c_2})$.

For adjacent cells, $(-1)^{i_1+j_1+i_2+j_2} = -1$ (since they differ by 1 in exactly one coordinate). So $B_{c_1} B_{c_2} = -(1-2b_{c_1})(1-2b_{c_2})$.

$\sum_{\text{adjacent}} B_{c_1} B_{c_2} = -\sum_{\text{adjacent}} (1-2b_{c_1})(1-2b_{c_2})$

$= -\sum_{\text{adjacent}} (1 - 2b_{c_1} - 2b_{c_2} + 4b_{c_1}b_{c_2})$

$= -E + 2\sum_{\text{adjacent}} (b_{c_1} + b_{c_2}) - 4\sum_{\text{adjacent}} b_{c_1}b_{c_2}$

$= -19800 + 4\sum_{\text{cells}} b_{ij} \deg(i,j) - 4\sum_{\text{adjacent}} b_{c_1}b_{c_2}$

Wait, $\sum_{\text{adjacent}} (b_{c_1} + b_{c_2}) = \sum_{\text{cells}} b_{ij} \cdot \deg(i,j)$ where $\deg(i,j)$ is the number of adjacent cells (2 for corners, 3 for edges, 4 for interior).

Hmm, this is getting complicated. Let me try a more direct approach.

Let me just try to construct a good solution and compute its transition count.

Construction: "Alternating staircase."

For each row $i$, we want $r_i$ black cells. Arrange the black cells in row $i$ to maximize horizontal transitions, while also trying to maintain vertical transitions.

For a row with $r$ black cells, the maximum horizontal transitions is $2\min(r, 100-r)$ (achieved by alternating as much as possible).

The arrangement that achieves this: if $r \leq 50$, place black cells in positions $1, 3, 5, ..., 2r-1$ (every other, starting from position 1). This gives $2r$ transitions if $r < 50$, and $99$ transitions if $r = 50$ (but $r = 50$ is excluded).

Wait, for $r < 50$: place in positions 1, 3, 5, ..., 2r-1. The row looks like BWBWBW...BW followed by WW...W. The transitions are at positions (1,2), (2,3), (3,4), ..., (2r-1, 2r), which is $2r - 1$... no.

Actually, let me think about this. If $r = 3$ and $n = 10$: place black in positions 1, 3, 5. Row: B W B W B W W W W W. Transitions: (1,2), (2,3), (3,4), (4,5), (5,6) = 5. And $2r = 6$. Hmm, that's $2r - 1 = 5$.

Wait, I think the maximum is $2r$ if we start and end with black, but that requires $r > n/2$... no.

Let me reconsider. For $r$ black cells in $n$ positions, the maximum number of transitions:
- If $r \leq n - r$: we can arrange as BWBWBW...BW (starting with B, alternating), using $r$ black and $r$ white, then the remaining $n - 2r$ white. Transitions: $2r - 1$ (within the alternating part) + 1 (transition from last B to first W of the remaining) = $2r$. Wait, the alternating part BWBW...BW has $r$ B's and $r-1$ W's (if it ends with B) or $r$ B's and $r$ W's (if it ends with W). 

Let me be precise. Arrange as: B W B W ... B W W W ... W, where the alternating part has $r$ B's and $r$ W's (length $2r$), followed by $n - 2r$ W's. The transitions within the alternating part: $2r - 1$. The transition at the boundary (position $2r$ to $2r+1$): W to W, no transition. Total: $2r - 1$.

Alternatively, arrange as: W B W B ... W B W W ... W, with $r$ B's and $r+1$ W's in the alternating part (length $2r + 1$), followed by $n - 2r - 1$ W's. Transitions: $2r$. But this requires $2r + 1 \leq n$, i.e., $r \leq (n-1)/2 = 49.5$, so $r \leq 49$.

Hmm wait, W B W B ... W B W has $r$ B's and $r+1$ W's, length $2r+1$. Transitions: $2r$. Then followed by $n - 2r - 1$ W's, no additional transition. Total: $2r$.

Or: B W B W ... B W B W W ... W, with $r$ B's and $r$ W's, length $2r$, transitions $2r - 1$, then $n - 2r$ W's, no additional transition. Total: $2r - 1$.

Or: W W ... W B W B ... W B, with $n - 2r$ W's, then $r$ B's and $r$ W's alternating (starting with B). Transitions: 1 (W to B at boundary) + $2r - 1$ (within alternating) = $2r$.

So the maximum is $2r$ for $r \leq 49$ (when $n = 100$). For $r = 50$: $2r = 100 > 99 = n - 1$, so the max is $99$ (perfect alternation). But $r = 50$ is excluded.

For $r > 50$: by symmetry (consider white cells instead), the max is $2(100 - r)$ for $r \geq 51$.

So the maximum horizontal transitions per row is $2\min(r, 100 - r)$ for $r \neq 50$.

Sum over all rows: $\sum_{r \in \{0,...,49,51,...,100\}} 2\min(r, 100-r)$.

$= 2\sum_{r=0}^{49} r + 2\sum_{r=51}^{100} (100 - r)$

$= 2 \cdot \frac{49 \cdot 50}{2} + 2 \cdot \sum_{s=0}^{49} s = 2 \cdot 1225 + 2 \cdot 1225 = 4900$.

So the maximum total horizontal transitions (if we could optimize each row independently) is 4900.

Now, for vertical transitions: each column has 50 black cells. The maximum vertical transitions per column is 99 (perfect alternation). Total: 9900.

But can we achieve 4900 horizontal + 9900 vertical = 14800? Probably not, due to the coupling.

Let me think about what's achievable.

Key insight: The vertical transitions depend on the arrangement within each column, which is determined by the row arrangements. If we want maximum vertical transitions, each column should alternate as much as possible. But the row arrangements constrain this.

Let me think about a construction that balances horizontal and vertical transitions.

Construction: "Row-alternating with column balancing."

For each row $i$ with sum $r_i$, arrange the black cells to maximize horizontal transitions: place them in an alternating pattern. Specifically, for $r_i \leq 49$: place black cells in positions $1, 3, 5, ..., 2r_i - 1$ (or some shifted version). For $r_i \geq 51$: place white cells in an alternating pattern.

But we need each column to have 50 black cells. If all rows use the same alternating pattern (black in odd positions), then column $j$ (odd) has black in all rows with $r_i \geq (j+1)/2$, and column $j$ (even) has black in no rows. This doesn't give 50 black cells per column.

We need to shift the alternating patterns across rows to balance the columns.

Let me think about this more carefully.

Alternative construction: For each row $i$, use a "circular shift" of the alternating pattern.

Actually, let me think about a cleaner construction.

Construction: "Interleaved staircase."

Divide the 100 columns into two sets: odd columns and even columns (50 each).

For row $i$ with $r_i \leq 49$: place black cells in the first $r_i$ odd columns (columns 1, 3, 5, ..., 2r_i - 1). This gives $r_i$ black cells, all in odd columns, non-adjacent. Horizontal transitions: $2r_i$ (each black cell creates 2 transitions with its even neighbors, except possibly at the boundary).

Wait, let me reconsider. If black cells are in columns 1, 3, 5, ..., 2r_i - 1 (all odd), and white everywhere else:
- Column 1: B, Column 2: W, Column 3: B, ..., Column 2r_i - 1: B, Column 2r_i: W, ..., Column 100: W.
- Transitions: (1,2), (2,3), (3,4), ..., (2r_i - 1, 2r_i) = 2r_i - 1 transitions. Plus, if $2r_i < 100$, the transition at (2r_i, 2r_i + 1) is W to W, no transition.

Hmm, so $2r_i - 1$ transitions, not $2r_i$. Let me reconsider.

Actually, the pattern B W B W ... B W W W ... W (with $r_i$ B's in positions 1, 3, ..., 2r_i-1) has transitions at (1,2), (2,3), ..., (2r_i-1, 2r_i), which is $2r_i - 1$ transitions. But I said the max was $2r_i$. The difference is because this pattern starts with B. If we start with W: W B W B ... W B W W ... W (with $r_i$ B's in positions 2, 4, ..., 2r_i), transitions at (1,2), (2,3), ..., (2r_i, 2r_i+1), which is $2r_i$ transitions (if $2r_i < 100$).

So the arrangement matters. Let me use the W B W B ... pattern for rows with $r_i \leq 49$ to get $2r_i$ transitions.

For rows with $r_i \geq 51$: by symmetry, use a pattern where white cells alternate. Place white cells in positions 2, 4, ..., 2(100 - r_i), and black everywhere else. This gives $100 - r_i$ white cells in even positions, and $r_i$ black cells. Transitions: $2(100 - r_i)$.

Now, for the column constraint: if all rows with $r_i \leq 49$ use the pattern W B W B ... (black in even positions 2, 4, ..., 2r_i), and all rows with $r_i \geq 51$ use the pattern with white in even positions 2, 4, ..., 2(100-r_i) (black in all other positions including all odd positions and even positions after 2(100-r_i)):

Column $j$ (even, $j = 2k$):
- From rows with $r_i \leq 49$: black iff $j \leq 2r_i$, i.e., $k \leq r_i$, i.e., $r_i \geq k$.
- From rows with $r_i \geq 51$: white iff $j \leq 2(100 - r_i)$, i.e., $k \leq 100 - r_i$, i.e., $r_i \leq 100 - k$. So black iff $r_i > 100 - k$, i.e., $r_i \geq 101 - k$.

Column $j$ (odd, $j = 2k - 1$):
- From rows with $r_i \leq 49$: black iff $j \leq 2r_i$, i.e., $2k - 1 \leq 2r_i$, i.e., $k \leq r_i + 1/2$, i.e., $k \leq r_i$ (since $k$ is integer). So black iff $r_i \geq k$.

Wait, I need to be more careful. For rows with $r_i \leq 49$, the pattern is W B W B ... W B W W ... W, with black in positions 2, 4, ..., 2r_i. So column $j$ is black in this row iff $j$ is even and $j \leq 2r_i$, i.e., $j \in \{2, 4, ..., 2r_i\}$. So only even columns can be black.

For rows with $r_i \geq 51$, the pattern has white in positions 2, 4, ..., 2(100 - r_i) and black everywhere else. So column $j$ is black iff $j$ is odd OR ($j$ is even and $j > 2(100 - r_i)$).

Column $j$ (odd): 
- From rows with $r_i \leq 49$: never black (all black cells are in even columns).
- From rows with $r_i \geq 51$: always black (odd columns are always black in these rows).
So column $j$ (odd) has black cells in all rows with $r_i \geq 51$. There are 50 such rows. So 50 black cells. ✓

Column $j$ (even, $j = 2k$):
- From rows with $r_i \leq 49$: black iff $r_i \geq k$. The rows with $r_i \leq 49$ have sums $0, 1, ..., 49$. The number with $r_i \geq k$ is $50 - k$ (for $k = 1, ..., 49$) or 0 (for $k = 0$, but $k \geq 1$ since $j \geq 2$). Wait, $r_i \in \{0, 1, ..., 49\}$, and we need $r_i \geq k$. For $k = 1$: $r_i \geq 1$, so 49 rows. For $k = 49$: $r_i \geq 49$, so 1 row. For $k = 50$: $r_i \geq 50$, but $r_i \leq 49$, so 0 rows.

- From rows with $r_i \geq 51$: black iff $j > 2(100 - r_i)$, i.e., $2k > 2(100 - r_i)$, i.e., $k > 100 - r_i$, i.e., $r_i > 100 - k$, i.e., $r_i \geq 101 - k$. The rows with $r_i \geq 51$ have sums $51, 52, ..., 100$. The number with $r_i \geq 101 - k$: for $k = 1$: $r_i \geq 100$, 1 row. For $k = 50$: $r_i \geq 51$, 50 rows.

Total for column $2k$: $(50 - k) + (k) = 50$ for $k = 1, ..., 49$ (wait, let me recheck).

For $k = 1$: from top: $50 - 1 = 49$. From bottom: $r_i \geq 100$, so 1 row. Total: 50. ✓
For $k = 49$: from top: $50 - 49 = 1$. From bottom: $r_i \geq 52$, so 49 rows. Total: 50. ✓
For $k = 50$ ($j = 100$): from top: $50 - 50 = 0$. From bottom: $r_i \geq 51$, so 50 rows. Total: 50. ✓

So all columns have 50 black cells. The construction works.

Now let me count the transitions.

Horizontal transitions:
- Rows with $r_i \leq 49$ (using W B W B ... pattern): $2r_i$ transitions each. Sum = $2(0 + 1 + ... + 49) = 2 \cdot 1225 = 2450$.
- Rows with $r_i \geq 51$ (using the complementary pattern): $2(100 - r_i)$ transitions each. Sum = $2(49 + 48 + ... + 0) = 2 \cdot 1225 = 2450$.
Total horizontal: 4900.

Vertical transitions:
- Odd columns ($j = 1, 3, 5, ..., 99$): Black in rows with $r_i \geq 51$ (rows 51-100 in our ordering), white in rows with $r_i \leq 49$ (rows 1-50). So the column is white in rows 1-50 and black in rows 51-100. One transition (at row 50/51). Total for odd columns: $50 \times 1 = 50$.

- Even columns ($j = 2k$): Black in rows with $r_i \geq k$ (from top, rows $k+1$ to 50... wait, I need to be more careful about the row ordering).

Hmm, I assumed rows are ordered by sum: rows 1-50 have sums 0-49, rows 51-100 have sums 51-100. But the vertical pattern depends on the specific row ordering.

Let me re-examine. In this construction:
- Rows 1-50 have sums 0, 1, 2, ..., 49 (row $i$ has sum $i-1$).
- Rows 51-100 have sums 51, 52, ..., 100 (row $i$ has sum $i$).

For even column $j = 2k$:
- From top half (rows 1-50): black in row $i$ iff $r_i \geq k$ iff $i - 1 \geq k$ iff $i \geq k + 1$. So black in rows $k+1, k+2, ..., 50$.
- From bottom half (rows 51-100): black in row $i$ iff $r_i \geq 101 - k$ iff $i \geq 101 - k$. So black in rows $101-k, 101-k+1, ..., 100$ (but also $i \geq 51$, so rows $\max(51, 101-k)$ to 100).

For $k \leq 50$: $101 - k \geq 51$, so black in rows $101-k$ to 100.

So column $2k$ (from top to bottom):
- Rows 1 to $k$: white
- Rows $k+1$ to $50$: black
- Rows $51$ to $100-k$: white
- Rows $101-k$ to $100$: black

Transitions: at row $k$/$k+1$ (W to B): 1. At row $50$/$51$ (B to W): 1. At row $100-k$/$101-k$ (W to B): 1. Total: 3 per even column.

For $k = 50$ ($j = 100$): rows 1-50 white, rows 51-100 black. 1 transition.

So vertical transitions:
- 50 odd columns: 1 each = 50.
- 49 even columns ($k = 1, ..., 49$): 3 each = 147.
- 1 even column ($k = 50$, $j = 100$): 1.
Total vertical: $50 + 147 + 1 = 198$.

Total transitions: $4900 + 198 = 5098$.

That's better than the staircase (296) but still far from the theoretical max of 14800. The issue is that vertical transitions are very low (198 vs. max 9900).

The problem is that in this construction, the odd columns have a huge block of white (rows 1-50) and a huge block of black (rows 51-100), giving only 1 transition.

To improve, we need to interleave the rows better. Instead of grouping all low-sum rows together and all high-sum rows together, we should interleave them.

Let me try a different row ordering.

Construction: "Interleaved rows."

Order the rows so that low-sum and high-sum rows alternate. For example:
- Row 1: sum 0, Row 2: sum 100, Row 3: sum 1, Row 4: sum 99, Row 5: sum 2, Row 6: sum 98, ...

This way, adjacent rows have very different sums, which might create more vertical transitions.

But the horizontal transitions depend on the row arrangement, not the ordering. And the vertical transitions depend on how the patterns in adjacent rows interact.

Let me think about this more carefully.

Actually, the key issue is that in my construction, all low-sum rows use the same pattern (W B W B ... with black in even columns), and all high-sum rows use the complementary pattern (black in all odd columns plus some even columns). This creates a sharp boundary between the two groups.

To improve vertical transitions, I should vary the patterns across rows. For example, some low-sum rows could use the pattern starting with B (black in odd columns), and others starting with W (black in even columns).

But then the column sums might not work out. Let me think about this.

Alternative construction: "Mixed parity."

For each row $i$ with sum $r_i \leq 49$, choose whether to place black cells in odd or even columns. If we place in odd columns: black in positions 1, 3, ..., 2r_i - 1. If in even columns: black in positions 2, 4, ..., 2r_i.

Similarly for rows with $r_i \geq 51$: choose whether to place white cells in odd or even columns.

Let's say $p$ rows with $r_i \leq 49$ use odd-column pattern, and $50 - p$ use even-column pattern.
And $q$ rows with $r_i \geq 51$ use odd-column white pattern (white in odd, black in even and some odd), and $50 - q$ use even-column white pattern.

This is getting complicated. Let me think about it differently.

Actually, let me reconsider the problem. Maybe there's a cleaner way to think about the maximum.

Let me go back to the formula:
$$T = 19900 - (r_1 + r_{100}) - 2S$$

where $S = S_h + S_v$ is the total number of adjacent black-black pairs.

We want to minimize $r_1 + r_{100} + 2(S_h + S_v)$.

We know $r_1 + r_{100} \geq 1$ (minimum is 0 + 1 = 1).
We know $S_h \geq 1275$ (from row constraints).
We know $S_v \geq 0$.

But can we achieve $S_h = 1275$ and $S_v = 0$ simultaneously? As we discussed, $S_v = 0$ requires each column to have black cells in all odd or all even positions, which forces all rows to have the same sum. So no.

What's the minimum of $S_h + S_v$ given the constraints?

Let me think about a lower bound on $S_v$.

$S_v = \sum_{j=1}^{100} \sum_{i=1}^{99} a_{ij} a_{i+1,j}$ = total number of vertically adjacent black-black pairs.

For each column $j$, let $v_j = \sum_{i=1}^{99} a_{ij} a_{i+1,j}$ be the number of vertically adjacent black-black pairs in column $j$. We have $S_v = \sum v_j$.

In column $j$ with 50 black cells, $v_j \geq 0$, and $v_j = 0$ iff the 50 black cells are in non-adjacent positions (all odd or all even).

But the row sums constrain which rows can have black cells in which columns. The question is: what is the minimum total $S_v$ given the row sum and column sum constraints?

This is a complex combinatorial optimization. Let me try to think about it from a different angle.

Let me consider the problem as a transportation/assignment problem and think about what structure minimizes $S_h + S_v$.

Actually, let me try to think about the problem more cleverly.

Key observation: $S_h + S_v$ counts the number of edges in the grid graph where both endpoints are black. This is related to the number of edges in the "black subgraph."

The grid graph has $100 \times 100$ vertices and $2 \times 100 \times 99 = 19800$ edges. The black subgraph has 5000 vertices (black cells) and $S_h + S_v$ edges.

We want to minimize the number of edges in the black subgraph, subject to:
- Each column has 50 black cells.
- Row sums are $\{0, 1, ..., 49, 51, ..., 100\}$.

The minimum number of edges in a subgraph with $n$ vertices in a grid is related to the isoperimetric problem. But here the vertices are constrained.

Hmm, let me think about a lower bound on $S_h + S_v$ using a different approach.

Consider the "discrete Laplacian" or "summation by parts" approach.

For each row $i$, let $r_i$ be the row sum. The number of horizontal black-black pairs in row $i$ is:
$S_h^{(i)} = \sum_{j=1}^{99} a_{ij} a_{i,j+1}$

We know that $S_h^{(i)} \geq \max(0, r_i - 50)$ (as computed earlier).

For the vertical direction, consider the column sums (all 50). The number of vertical black-black pairs in column $j$ is:
$S_v^{(j)} = \sum_{i=1}^{99} a_{ij} a_{i+1,j}$

We know $S_v^{(j)} \geq 0$, but we need a better bound that accounts for the row sum constraints.

Let me think about a combined bound. Consider the "total adjacency" of black cells. Each black cell at position $(i,j)$ has some black neighbors. The total number of black-black adjacencies is $S = S_h + S_v$.

Another approach: think about the "boundary" of the black region. The number of black-white adjacencies is $T = 19800 - 2S$ (wait, no). Actually, $T = $ number of different-color adjacent pairs, and the total adjacent pairs is 19800. The same-color adjacent pairs = black-black + white-white. And $T = 19800 - $ (black-black + white-white).

Hmm, I had $T = 19900 - (r_1 + r_{100}) - 2S$ earlier. Let me re-derive.

$T = \sum_{\text{horizontal}} |a_{ij} - a_{i,j+1}| + \sum_{\text{vertical}} |a_{ij} - a_{i+1,j}|$

$|a - b| = a + b - 2ab$ for $a, b \in \{0, 1\}$.

$\sum_{\text{horizontal}} |a_{ij} - a_{i,j+1}| = \sum_{\text{horizontal}} (a_{ij} + a_{i,j+1} - 2a_{ij}a_{i,j+1})$

$= \sum_{i=1}^{100} (a_{i,1} + 2\sum_{j=2}^{99} a_{ij} + a_{i,100}) - 2S_h$

Wait, $\sum_{j=1}^{99} (a_{ij} + a_{i,j+1}) = a_{i1} + 2a_{i2} + 2a_{i3} + ... + 2a_{i,99} + a_{i,100} = 2r_i - a_{i1} - a_{i,100}$.

So horizontal different pairs = $\sum_i (2r_i - a_{i1} - a_{i,100}) - 2S_h = 2 \cdot 5000 - (c_1 + c_{100}) - 2S_h = 10000 - 100 - 2S_h = 9900 - 2S_h$.

Similarly, vertical different pairs = $\sum_j (2c_j - a_{1j} - a_{100,j}) - 2S_v = 2 \cdot 5000 - (r_1 + r_{100}) - 2S_v = 10000 - (r_1 + r_{100}) - 2S_v$.

Total $T = 9900 - 2S_h + 10000 - (r_1 + r_{100}) - 2S_v = 19900 - (r_1 + r_{100}) - 2(S_h + S_v)$.

OK so $T = 19900 - (r_1 + r_{100}) - 2S$ where $S = S_h + S_v$.

To maximize $T$:
1. Minimize $r_1 + r_{100}$: minimum is 1 (sums 0 and 1 at the ends).
2. Minimize $S = S_h + S_v$.

Now I need to find the minimum of $S_h + S_v$.

$S_h \geq 1275$ (from row constraints).
$S_v \geq ?$ (need to determine, considering row and column constraints).

But $S_h$ and $S_v$ are coupled. Let me think about whether $S_h = 1275$ is achievable while also minimizing $S_v$.

$S_h = 1275$ requires each row to achieve its minimum horizontal black-black pairs: $\max(0, r_i - 50)$ for each row. This means:
- Rows with $r_i \leq 50$: no two black cells are horizontally adjacent. Black cells are placed in non-adjacent positions.
- Rows with $r_i > 50$: exactly $r_i - 50$ horizontal black-black pairs, achieved by placing black cells in a pattern with maximum spread.

For rows with $r_i \leq 49$: black cells in non-adjacent positions. This means black cells are in a subset of $\{1, 3, 5, ..., 99\}$ or $\{2, 4, 6, ..., 100\}$ (or a mix, but non-adjacent). Actually, non-adjacent doesn't require all same parity; it just requires no two consecutive. But with $r_i \leq 49$ black cells in 100 positions, we can always place them non-adjacently.

For rows with $r_i = 50$: excluded.
For rows with $r_i \geq 51$: we need $r_i - 50$ horizontal black-black pairs. The minimum is achieved by placing black cells as spread out as possible, with exactly $r_i - 50$ "extra" black cells that must be adjacent to others.

Now, the question is: given that each row has its black cells arranged to minimize $S_h$, what is the minimum $S_v$?

This is still complex. Let me try to think about specific constructions and compute $S$.

Let me try the construction I had before (all low-sum rows use even-column pattern, all high-sum rows use complementary pattern), but with a better row ordering.

Actually, the row ordering doesn't affect $S_h$ (since $S_h$ only depends on the arrangement within each row). It affects $S_v$ (since $S_v$ depends on the vertical arrangement, which depends on the row ordering).

In my previous construction:
- $S_h = 4900$... wait, no. Let me recompute.

In the "W B W B ..." pattern for row with $r_i$ black cells (in even positions 2, 4, ..., 2r_i): the black cells are in positions 2, 4, ..., 2r_i. These are all non-adjacent (separated by white cells). So $S_h^{(i)} = 0$ for $r_i \leq 49$.

For the complementary pattern (row with $r_i \geq 51$): white cells in positions 2, 4, ..., 2(100 - r_i), black everywhere else. Black cells are in positions 1, 3, 5, ..., 99 (all odd, 50 cells) plus positions 2(100-r_i)+2, 2(100-r_i)+4, ..., 100 (some even cells). The odd positions are non-adjacent. The even black cells are also non-adjacent (they're in even positions). But odd and even positions can be adjacent. Specifically, position $2k-1$ and $2k$ are adjacent. If both are black, that's a black-black pair.

In this pattern, position $2k$ is black iff $2k > 2(100 - r_i)$, i.e., $k > 100 - r_i$, i.e., $k \geq 101 - r_i$. Position $2k - 1$ is always black (odd). So positions $2k - 1$ and $2k$ are both black iff $k \geq 101 - r_i$. The number of such pairs is $r_i - 50$ (since $k$ ranges from $101 - r_i$ to 50, giving $50 - (101 - r_i) + 1 = r_i - 50$ pairs).

Also, positions $2k$ and $2k+1$: both black iff $k \geq 101 - r_i$ (for $2k$) and $2k+1$ is odd (always black). So same count: $r_i - 50$ pairs.

Wait, but I'm double-counting. Let me be more careful.

$S_h^{(i)} = \sum_{j=1}^{99} a_{ij} a_{i,j+1}$.

The row pattern is: B W B W ... B W B B W B B W ... (where the first part is alternating B W, and then at some point it becomes B B W B B W ... or similar).

Actually, let me think about it concretely. For $r_i = 51$: white in positions 2, 4, ..., 98 (49 white cells), black in all other 51 positions (1, 3, 5, ..., 99, 100). 

Row: B W B W B W ... B W B B (positions 1-100: odd positions are B, even positions 2-98 are W, position 100 is B).

Adjacent pairs: (99, 100) = B B, that's 1 black-black pair. All other adjacent pairs are B W or W B. So $S_h^{(i)} = 1 = 51 - 50$. ✓

For $r_i = 52$: white in positions 2, 4, ..., 96 (48 white cells), black in 52 positions (all odd 1-99, plus 98 and 100).

Row: B W B W ... B W B B W B B (positions: odd = B, even 2-96 = W, 98 = B, 100 = B).

Adjacent pairs: (97, 98) = B B, (98, 99) = B B, (99, 100) = B B. That's 3. But $r_i - 50 = 2$. Hmm, that doesn't match.

Wait, let me recount. For $r_i = 52$: $100 - r_i = 48$ white cells in positions 2, 4, ..., 96. Black in positions 1, 3, 5, ..., 99 (50 odd) plus 98, 100 (2 even). Total 52. ✓

Adjacent black-black pairs:
- (97, 98): 97 is odd (B), 98 is B. BB. ✓
- (98, 99): 98 is B, 99 is odd (B). BB. ✓
- (99, 100): 99 is B, 100 is B. BB. ✓

That's 3, but $r_i - 50 = 2$. So $S_h^{(i)} = 3 > 2$. This means the complementary pattern doesn't achieve the minimum $S_h$!

The issue is that the even black cells at positions 98 and 100 are adjacent to odd black cells, creating extra black-black pairs.

Let me reconsider. The minimum $S_h$ for $r_i = 52$ is 2. How to achieve it?

Place 52 black cells in 100 positions with only 2 adjacent black-black pairs. One way: place black in positions 1, 3, 5, ..., 99 (50 non-adjacent) plus 2 more in positions that create minimal extra adjacency. If we add black at positions 100 and 2: 
- Position 100 is adjacent to 99 (B), creating 1 BB pair.
- Position 2 is adjacent to 1 (B) and 3 (B), creating 2 BB pairs.
Total: 3. Not minimal.

If we add at positions 100 and 98:
- 100 adjacent to 99 (B): 1 BB.
- 98 adjacent to 97 (B) and 99 (B): 2 BB.
Total: 3. Not minimal.

If we add at positions 100 and 51:
- 100 adjacent to 99 (B): 1 BB.
- 51 adjacent to 50 (W) and 52 (W): 0 BB.
Total: 1. But we need 2 extra black cells, and we get 1 BB pair. That's less than 2!

Wait, but the minimum is $\max(0, r - 50) = 2$ for $r = 52$. But I just found an arrangement with 1 BB pair. Let me recheck.

With 52 black cells: 50 in odd positions (1, 3, ..., 99) plus 2 in even positions 100 and 51. Position 100 is adjacent to 99 (B): 1 BB. Position 51 is adjacent to 50 (W) and 52 (W): 0 BB. Total BB: 1.

But I claimed the minimum is $r - 50 = 2$. Let me recheck the formula.

The minimum number of adjacent black-black pairs for $r$ black cells in $n$ positions is $\max(0, r - \lceil n/2 \rceil)$... wait, I derived it as $r - \min(r, \lfloor (n+1)/2 \rfloor) = \max(0, r - \lfloor (n+1)/2 \rfloor)$.

For $n = 100$: $\lfloor 101/2 \rfloor = 50$. So minimum is $\max(0, r - 50)$.

For $r = 52$: minimum is 2. But I found an arrangement with 1. Contradiction!

Let me recheck. The formula says: minimum adjacent BB pairs = $r - b_{\max}$ where $b_{\max}$ is the maximum number of blocks. $b_{\max} = \min(r, \lfloor (n+1)/2 \rfloor) = \min(52, 50) = 50$. So minimum = $52 - 50 = 2$.

But in my arrangement: 50 odd positions (all B) plus positions 51 and 100. Let me list the blocks:
- Position 1: B (block 1)
- Position 2: W
- Position 3: B (block 2)
- ...
- Position 49: B (block 25)
- Position 50: W
- Position 51: B (block 26)
- Position 52: W
- Position 53: B (block 27)
- ...
- Position 99: B (block 50)
- Position 100: B (still block 50, since 99 and 100 are adjacent)

So blocks: 50 blocks (positions 1, 3, 5, ..., 97, 99-100). Block 50 is positions 99-100 (size 2), all others are size 1. Number of BB pairs = $\sum (s_i - 1) = 1$ (only block 50 has size 2). So $S_h = 1$.

But the formula says minimum is 2. Where's the error?

Ah, I think the issue is with the formula. Let me re-derive.

We have $r$ black cells in $n$ positions, forming $b$ blocks. The number of BB adjacent pairs is $r - b$ (since each block of size $s$ contributes $s - 1$ pairs, and $\sum s_i = r$, so $\sum (s_i - 1) = r - b$).

To minimize BB pairs, maximize $b$. The maximum $b$ is limited by:
1. $b \leq r$ (each block has at least 1 cell).
2. Blocks must be separated by at least 1 white cell. With $b$ blocks, we need at least $b - 1$ white cells between them, plus possibly white cells at the ends. So $r + (b - 1) \leq n$, giving $b \leq n - r + 1$.

So $b_{\max} = \min(r, n - r + 1)$.

For $n = 100, r = 52$: $b_{\max} = \min(52, 49) = 49$. Minimum BB pairs = $52 - 49 = 3$.

Hmm, but I found an arrangement with 1 BB pair (50 blocks, $52 - 50 = 2$... wait, I said 50 blocks, but let me recount.

In my arrangement: B at positions 1, 3, 5, ..., 99 (50 positions) plus 51 and 100.

Wait, position 51 is already in my list (51 is odd, so it's already B). I can't add it again!

Let me reconsider. The 50 odd positions are 1, 3, 5, ..., 99. I need to add 2 more black cells in even positions. Let me choose positions 2 and 100.

Position 2 is adjacent to 1 (B) and 
