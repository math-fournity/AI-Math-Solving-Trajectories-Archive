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
  <problem_id>polymath_05102</problem_id>
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

6. Each cell of a $2011 \times 2011$ grid is labeled with an integer from $1,2, \cdots, 2011^{2}$, such that each number is used exactly once. Now, the left and right boundaries, as well as the top and bottom boundaries of the grid, are considered the same, forming a torus (which can be viewed as the surface of a "doughnut"). Find the largest positive integer $M$ such that for any labeling method, there exist two adjacent cells (cells sharing a common edge) whose numbers differ (the larger minus the smaller) by at least $M$.

【Note】Using coordinates, a cell $(x, y)$ and $\left(x^{\prime}, y^{\prime}\right)$ are adjacent if:
$$
\begin{aligned}
x=x^{\prime}, y-y^{\prime} \equiv \pm 1(\bmod 2011) \\
\text { or } \quad y=y^{\prime}, x-x^{\prime} \equiv \pm 1(\bmod 2011) .
\end{aligned}
$$

## Standard Solution

6. Let $N=2011$.

Consider a general $N \times N$ table.
When $N=2$, the conclusion is obvious, and the required $M=2$. An example is shown in Table 1.
Table 1
\begin{tabular}{|l|l|}
\hline 1 & 2 \\
\hline 3 & 4 \\
\hline
\end{tabular}

When $N \geqslant 3$, first prove:
$M \geqslant 2 N-1$.
Starting from a state where each small square in the table is white, write the numbers $1,2, \cdots$ in the table while coloring the marked squares black. Stop the operation when the following condition is first met: every row or every column has at least two black squares. Let the last number written be $k$.

Before marking $k$, there must be one row and one column with at most one black square.

Assume, when marking $k$, every row has two black squares. At this point, there is at most one row with all black squares. This is because if there are two rows with all black squares, then if $k$ is marked in one of these two rows, each row already had two black squares before (using $N \geqslant 3$); if $k$ is marked in another row, then each column already had two black squares.

Color a black square red if it has an adjacent white square. Since, except for the possible all-black row, each row has two black squares and one white square, each of these rows has at least two red squares. Furthermore, the row adjacent to the possible all-black row must have at least one white square. Therefore, at least one black square in the all-black row is colored red. Thus, the number of red squares is at least $2(N-1)+1=2 N-1$.

Therefore, the smallest number in all red squares is at most $k+1-(2 N-1)$.

When the adjacent white square of this red square is marked (the number marked is at least $k+1$), the difference between these two adjacent squares is at least $2 N-1$.

Since $N=2011$, it is sufficient to construct an example for $N=2 n+1(\geqslant 2)$.
Table 2 provides an example where $M=2 N-1$.
Therefore, the required $M=4021$.
Table 2
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline$(2 n+1)^{2}-2$ & $(2 n+1)^{2}-9$ & $\cdots$ & $\cdots$ & $n(2 n-1)+1$ & $\cdots$ & $\cdots$ & $(2 n+1)^{2}-10$ & $(2 n+1)^{2}-3$ \\
\hline$(2 n+1)^{2}-8$ & $\cdots$ & $\cdots$ & $n(2 n-1)+2$ & $\cdots$ & $n(2 n-1)$ & $\cdots$ & $\cdots$ & $(2 n+1)^{2}-11$ \\
\hline$\vdots$ & $\vdots$ & $\ddots$ & $\vdots$ & $\vdots$ & $\vdots$ & $\ddots$ & $\vdots$ & $\vdots$ \\
\hline$\cdots$ & $2 n^{2}$ & $\cdots$ & 8 & 2 & 6 & $\cdots$ & $2 n(n-1)+2$ & $2 n(n+1)+2$ \\
\hline $2 n^{2}+1$ & $\cdots$ & $\cdots$ & 3 & 1 & 5 & $\cdots$ & $\cdots$ & $2 n(n+1)+1$ \\
\hline$\cdots$ & $2 n^{2}+2$ & $\cdots$ & 10 & 4 & 12 & $\cdots$ & $2 n(n+1)$ & $\cdots$ \\
\hline$\vdots$ & $\vdots$ & $\ddots$ & $\vdots$ & $\vdots$ & $\vdots$ & $\ddots$ & $\vdots$ & $\vdots$ \\
\hline$(2 n+1)^{2}-7$ & $\cdots$ & $\cdots$ & $n(2 n+1)$ & $\cdots$ & $n(2 n+1)+2$ & $\cdots$ & $\cdots$ & $(2 n+1)^{2}-4$ \\
\hline$(2 n+1)^{2}-1$ & $(2 n+1)^{2}-6$ & $\cdots$ & $\cdots$ & $n(2 n+1)+1$ & $\cdots$ & $\cdots$ & $(2 n+1)^{2}-5$ & $(2 n+1)^{2}$ \\
\hline
\end{tabular}

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a 2011×2011 grid on a torus (so wraparound adjacency). Each cell labeled with integers 1 to 2011², each used exactly once. We need to find the largest M such that for ANY labeling, there exist two adjacent cells whose numbers differ by at least M.

Let me denote n = 2011. The grid is n×n on a torus, so it's essentially the toroidal grid graph T_n × T_n. Each vertex has degree 4. Total vertices = n². Labels are 1 to n².

We want: the maximum over all labelings of the minimum... no wait. We want the largest M such that for ANY labeling, there exist two adjacent cells differing by at least M.

So M = min over all labelings of (max difference between adjacent cells).

We want to find this minimum. For each labeling, consider the maximum difference between adjacent cells. We want the minimum of this over all labelings.

So we want to construct a labeling that minimizes the maximum adjacent difference, and find what that minimum is.

This is a classic type of problem. Let me think about it.

Lower bound (constructive): We need to show there's a labeling where all adjacent differences are at most some value D. Then M ≤ D.

Upper bound: We need to show that for any labeling, there exist adjacent cells differing by at least some value D'. Then M ≥ D'.

We want M = the answer.

Let me think about the structure. The toroidal grid n×n has n² vertices and 2n² edges (each vertex degree 4, so 4n²/2 = 2n² edges).

If we want to minimize the maximum edge difference, we want to arrange numbers so that adjacent cells have close values.

One natural approach: think of a Hamiltonian path or cycle on the torus. If we can find a Hamiltonian cycle on the toroidal grid, then we can label cells along the cycle 1, 2, 3, ..., n². Adjacent cells on the cycle differ by 1. But cells not adjacent on the cycle might be adjacent on the grid and have large differences.

Actually, let me think about this differently. 

The key insight for these problems: Consider the set of edges. If we sort all labels, the maximum difference between adjacent cells is at least... hmm.

Let me think about the upper bound first. For any labeling, consider the cells labeled 1 and n². There's a path between them on the torus. The shortest path on the toroidal grid between any two cells has length at most... well, on an n×n torus, the distance between any two cells is at most floor(n/2) + floor(n/2) = n-1 (for odd n) or n (for even n). For n=2011 (odd), the maximum distance is 2*floor(2011/2) = 2*1005 = 2010.

Wait, on a torus, the distance between (x,y) and (x',y') is min(|x-x'|, n-|x-x'|) + min(|y-y'|, n-|y-y'|). The maximum of this is 2*floor(n/2). For n=2011, that's 2*1005 = 2010.

So there's a path of length at most 2010 between the cell with label 1 and the cell with label n² = 2011². Along this path, the total difference is n² - 1 = 2011² - 1. By pigeonhole, some edge on this path has difference at least ceil((n²-1)/2010).

Let me compute: n² - 1 = 2011² - 1 = (2011-1)(2011+1) = 2010 * 2012. So (n²-1)/2010 = 2012. So some edge has difference at least 2012.

So M ≥ 2012.

Now can we achieve M = 2012? We need a labeling where every adjacent pair differs by at most 2012.

Hmm, let me think about whether we can do better on the upper bound or if 2012 is tight.

Actually wait, let me reconsider. The path length is at most 2010, and the total difference is n²-1 = 2010*2012. So the max edge on the path is at least 2012. This gives M ≥ 2012.

But maybe we can get a better lower bound using a different argument. Let me think...

Actually, the question is whether 2012 is achievable. Let me think about the construction.

Consider labeling the torus using a "snake" pattern. Actually, let me think about this more carefully.

Let me consider a different approach. Think of the torus as Z_n × Z_n. We want to assign labels 1 to n² to minimize max adjacent difference.

One idea: Use a linear labeling. Label cell (x, y) as f(x, y) = (ax + by) mod n² or something similar, then add 1. But we need a bijection to {0, 1, ..., n²-1}.

Actually, let me think about the standard approach for this type of problem.

Consider the labeling where we go row by row: cell (x, y) gets label y * n + x + 1 (for x, y in 0..n-1). Then:
- Horizontal neighbors: differ by 1 (except wraparound: (n-1, y) and (0, y) differ by n-1).
- Vertical neighbors: differ by n (except wraparound: (x, n-1) and (x, 0) differ by n² - n - ... let me compute: (n-1)*n + x + 1 vs x + 1, difference = (n-1)*n = n² - n).

So the wraparound differences are n-1 (horizontal) and n²-n (vertical). The max is n² - n = 2011² - 2011 = 2011*2010 = 4042110. That's way too big.

We need a better construction. The key is to handle the wraparound.

Let me think about using a Hamiltonian cycle on the torus. If we have a Hamiltonian cycle and label along it, then edges on the cycle have difference 1, but other edges (the "chords") might be large.

Actually, let me think about this problem from the perspective of the answer being 2012.

We need to construct a labeling of the n×n torus (n=2011) where every adjacent pair differs by at most 2012.

Let me think about what 2012 = n+1 means. 

Hmm, let me think about a different construction. Consider the labeling:
- Cell (x, y) gets label based on a diagonal traversal.

Actually, let me think about this. We want to use the structure of the torus. 

Consider the "diagonal" labeling: label (x, y) as ((x + y) mod n) * n + ((x + 2y) mod n) + 1 or something. The idea is to use a linear map that's a bijection on Z_n × Z_n → Z_n × Z_n, then convert to a number.

Let me think more carefully. We want to find a bijection φ: Z_n × Z_n → {0, 1, ..., n²-1} such that adjacent cells map to values differing by at most n+1.

If we write φ(x, y) = a(x, y) * n + b(x, y) where a, b ∈ {0, ..., n-1}, and (a, b) is a bijection of (x, y), then the value is a*n + b.

For horizontal adjacency: (x, y) and (x+1, y). We need |φ(x+1, y) - φ(x, y)| ≤ n+1 (considering the actual integer difference, not modular).

For vertical adjacency: (x, y) and (x, y+1). Similarly.

Hmm, this is getting complicated. Let me think about it differently.

Let me consider the approach where we think of the torus as having a Hamiltonian cycle that's also a "good" cycle.

Actually, let me reconsider the problem. The answer might be exactly n+1 = 2012.

Let me verify the lower bound more carefully and then think about the construction.

Lower bound: For any labeling, consider cells with labels 1 and n². The toroidal distance between them is at most 2⌊n/2⌋ = n-1 (for odd n). So there's a path of length ≤ n-1 = 2010. The total difference along the path is n²-1 = 2010·2012. By pigeonhole, some edge has difference ≥ ⌈(n²-1)/(n-1)⌉ = ⌈(n+1)(n-1)/(n-1)⌉ = n+1 = 2012.

Wait, n²-1 = (n-1)(n+1), and the path length is at most n-1. So the max edge difference is at least (n²-1)/(n-1) = n+1 = 2012. Since n+1 is an integer, M ≥ 2012.

Now for the upper bound, we need to construct a labeling where all adjacent differences are ≤ 2012 = n+1.

Let me think about this construction. 

Idea: Use a Hamiltonian cycle on the torus. The toroidal grid n×n (for odd n) has a Hamiltonian cycle. If we label along the cycle 0, 1, 2, ..., n²-1, then cycle edges have difference 1. The non-cycle edges (each vertex has 2 cycle edges and 2 non-cycle edges) need to be controlled.

Actually, on the torus, each vertex has degree 4. A Hamiltonian cycle uses 2 edges per vertex, leaving 2 edges per vertex as "extra" edges. There are n² extra edges. We need these to also have small differences.

Hmm, this seems hard to control in general. Let me think of a different approach.

Alternative idea: Think of the torus as Z_n × Z_n and use a labeling that's "linear" in some sense.

Let me try: label(x, y) = (y * k + x) mod n² for some k, then add 1. We need this to be a bijection, which requires gcd(k, n) = 1... actually we need the map (x, y) → (y*k + x) mod n² to be a bijection from Z_n × Z_n to Z_{n²}. 

For this to be a bijection, we need: if y₁*k + x₁ ≡ y₂*k + x₂ (mod n²), then x₁ = x₂ and y₁ = y₂. 

If y₁ ≠ y₂, then (y₁ - y₂)*k ≡ x₂ - x₁ (mod n²). Since x₂ - x₁ ∈ {-(n-1), ..., n-1} and (y₁-y₂)*k mod n²... this is getting complicated.

Let me try a specific construction. Consider the "spiral" or "diagonal snake" on the torus.

Actually, let me think about this more carefully with a concrete approach.

Consider the labeling where we traverse the torus in a "knight's move" like pattern. Specifically, consider the map:

φ(x, y) = (x + c*y) mod n, combined with y, to create a snake-like pattern.

Hmm, let me try yet another approach. 

Let me think about what makes the wraparound problematic. In the row-by-row labeling, the issue is the vertical wraparound (top to bottom) creates a huge jump. 

What if we use a "reflected" snake? In a reflected snake (boustrophedon), even rows go left to right, odd rows go right to left. Then:
- Within a row: differences of 1.
- Between rows: the vertical difference is... if row y goes left to right (labels y*n to y*n+n-1) and row y+1 goes right to left (labels (y+1)*n to (y+1)*n+n-1 but reversed), then cell (x, y) has label y*n + x and cell (x, y+1) has label (y+1)*n + (n-1-x). The difference is (y+1)*n + n-1-x - y*n - x = n + n - 1 - 2x = 2n - 1 - 2x. This ranges from 2n-1 (x=0) to 1 (x=n-1). So max vertical difference is 2n-1.

For the wraparound (row n-1 to row 0): row n-1 goes left to right (if n-1 is even, which it is since n=2011 is odd, so n-1=2010 is even), labels (n-1)*n to (n-1)*n+n-1. Row 0 goes left to right, labels 0 to n-1. Cell (x, n-1) has label (n-1)*n + x, cell (x, 0) has label x. Difference = (n-1)*n = n²-n. Still huge.

So the reflected snake doesn't help with the vertical wraparound.

The fundamental issue is the torus topology—any "row-by-row" type labeling will have a big jump at the wraparound.

Let me think about this differently. The key is that on a torus, we can't just do a simple snake. We need a more clever arrangement.

Let me think about the problem in terms of graph theory. We have the toroidal grid graph G. We want to find a labeling (a bijection from V(G) to {1, ..., n²}) that minimizes the maximum edge difference. This is related to the "bandwidth" of the graph, but not exactly—the bandwidth minimizes the maximum edge difference over all labelings, which is exactly what we're computing!

Wait, no. The bandwidth of a graph is min over all labelings of max over all edges of |label(u) - label(v)|. And we're looking for exactly this: the minimum over all labelings of the maximum adjacent difference. So M is the bandwidth of the toroidal grid graph T_n × T_n!

Hmm wait, but actually the problem asks for the largest M such that for ANY labeling, there exist adjacent cells differing by at least M. This is exactly the bandwidth: M = min_labeling max_edge |label(u) - label(v)|.

So we need the bandwidth of the n×n toroidal grid graph (Cartesian product of two cycles C_n).

The bandwidth of the toroidal grid C_n × C_n... let me recall or derive this.

For the path P_n, bandwidth is 1. For the cycle C_n, bandwidth is 2. For the grid P_n × P_n, bandwidth is n. For the toroidal grid C_n × C_n...

The bandwidth of C_m × C_n has been studied. Let me think about what it should be.

For the grid P_n × P_n (no wraparound), the bandwidth is n. This is because we can label row by row (bandwidth n) and we can't do better because the two endpoints of the grid are at distance n-1 apart and... actually the proof that bandwidth ≥ n for P_n × P_n uses the fact that there are n vertices in the first column and n in the last column, and they're connected through paths.

For the torus C_n × C_n, the bandwidth should be larger because of the wraparound.

Let me think about the bandwidth of C_n × C_n.

Upper bound construction: Can we achieve bandwidth n+1?

Consider the following labeling of Z_n × Z_n. Define the label of (x, y) as follows. We use a "diagonal" ordering.

Actually, let me think about a specific construction for odd n.

Consider the labeling: sort cells by (x + y) mod n, and within each diagonal, by x (or some order). 

Diagonal d (where d = (x+y) mod n) contains cells where x + y ≡ d (mod n). There are n cells in each diagonal. There are n diagonals.

If we label diagonal 0 first (n cells), then diagonal 1 (n cells), etc., then:
- Cells in the same diagonal: adjacent if they differ by (1, -1) direction, i.e., (x, y) and (x+1, y-1). These are in the same diagonal. Their labels differ by at most n-1 (within the same diagonal block).
- Cells in adjacent diagonals (d and d+1): adjacent if (x, y) and (x+1, y) or (x, y+1). (x+1, y) is in diagonal d+1, (x, y+1) is in diagonal d+1. So horizontal and vertical edges connect adjacent diagonals. The label difference is between 1 and 2n-1 (roughly).

Hmm, this doesn't immediately give n+1.

Let me think more carefully. Let me try a different approach.

Consider the labeling where we use a Hamiltonian cycle that winds around the torus in a specific way.

On the torus Z_n × Z_n, consider the cycle that goes: (0,0), (1,0), (2,0), ..., (n-1,0), (n-1,1), (0,1), (1,1), ..., wait this doesn't work simply.

Let me think about the "diagonal" Hamiltonian cycle. On Z_n × Z_n with gcd(1, n) = 1, the sequence (0,0), (1,1), (2,2), ..., (n-1, n-1), (0, 0) is a cycle of length n, not n². 

For a Hamiltonian cycle, we can use: (0,0), (1,0), (2,0), ..., (n-1,0), (0,1), (1,1), ..., (n-1,1), (0,2), ... This is the row-by-row snake, which is a Hamiltonian path but on the torus, the endpoints (n-1, n-1) and (0, 0) are not adjacent, so it's not a Hamiltonian cycle.

Actually, on the torus, (n-1, n-1) and (0, 0) are adjacent only if they differ by 1 in one coordinate mod n. (n-1) and 0 differ by 1 mod n (since n-1 ≡ -1, and -1 - 0 = -1 ≡ n-1, but we need ±1 mod n, and n-1 ≡ -1 mod n, so yes, they differ by -1 mod n in both coordinates). But adjacency requires difference in exactly one coordinate. (n-1, n-1) and (0, 0) differ in both coordinates, so they're NOT adjacent. So the row-by-row traversal is not a Hamiltonian cycle on the torus.

Let me think about Hamiltonian cycles on the torus. For odd n, the torus C_n × C_n has a Hamiltonian cycle. One construction: 

Start at (0, 0). Go right to (n-1, 0). Then go up to (n-1, 1). Then go left to (1, 1) [stopping at 1, not 0]. Then go up to (1, 2). Then right to (n-1, 2). Then up to (n-1, 3). Then left to (1, 3). Continue this pattern...

This creates a snake that alternates direction. After processing all rows, we need to connect back. Let me trace this more carefully.

Row 0: (0,0) → (1,0) → ... → (n-1, 0) [going right]
Up to (n-1, 1)
Row 1: (n-1, 1) → (n-2, 1) → ... → (1, 1) [going left, stopping at 1]
Up to (1, 2)
Row 2: (1, 2) → (2, 2) → ... → (n-1, 2) [going right]
Up to (n-1, 3)
Row 3: (n-1, 3) → ... → (1, 3) [going left]
...

So even rows go right (from some start to n-1), odd rows go left (from n-1 down to 1). Wait, but row 0 starts at 0 and goes to n-1, row 1 starts at n-1 and goes to 1, row 2 starts at 1 and goes to n-1, etc.

The cells visited:
- Row 0: x = 0, 1, ..., n-1 (all n cells)
- Row 1: x = n-1, n-2, ..., 1 (n-1 cells, missing x=0)
- Row 2: x = 1, 2, ..., n-1 (n-1 cells, missing x=0)
- Row 3: x = n-1, ..., 1 (n-1 cells, missing x=0)
...

So column x=0 only has cell (0, 0) visited in row 0. All other rows skip x=0. That means n-1 cells in column 0 are unvisited: (0, 1), (0, 2), ..., (0, n-1).

After the snake finishes row n-1 (which goes left from n-1 to 1), we're at (1, n-1). We need to visit the remaining cells (0, 1), (0, 2), ..., (0, n-1) and return to (0, 0).

From (1, n-1), go left to (0, n-1). Then go up (wraparound) to (0, 0). But that only visits (0, n-1) and then (0, 0). We missed (0, 1), ..., (0, n-2).

Hmm, this doesn't quite work. Let me reconsider.

Actually, let me try a different Hamiltonian cycle construction. 

For odd n, consider the cycle that uses steps (1, 0) and (0, 1) in a pattern. Actually, a well-known Hamiltonian cycle on the torus for odd n:

The cycle visits (i, j) in the order determined by starting at (0,0) and repeatedly adding (1, (n-1)/2) mod n. Wait, that gives a cycle of length n if gcd(1, (n-1)/2, n) ... hmm.

Actually, let me think about this differently. A Hamiltonian cycle on Z_n × Z_n exists iff the graph is Hamiltonian, which it is for n ≥ 3 (the toroidal grid is Hamiltonian for n ≥ 3).

But the key question is: can we find a Hamiltonian cycle such that the "chord" edges (the non-cycle edges) also have small differences?

Each vertex has 4 edges. The Hamiltonian cycle uses 2 per vertex. The remaining 2 edges per vertex form a set of n² "extra" edges. We need these to also have difference ≤ n+1.

This seems hard to guarantee in general. Let me think about whether there's a cleaner construction.

Let me try a completely different approach. Instead of a Hamiltonian cycle, let me think about a "space-filling" labeling that respects the torus topology.

Key idea: On the torus Z_n × Z_n, consider the labeling:
φ(x, y) = (n * y + x) for the "unwrapped" version, but then we need to handle wraparound.

The problem with row-by-row is the vertical wraparound: (x, n-1) and (x, 0) differ by n² - n.

What if we interleave? Consider the labeling:
φ(x, y) = n * ((y + x*⌊n/2⌋) mod n) + x

Wait, let me think about this more carefully.

Let me try: φ(x, y) = n * ((y + x * m) mod n) + x, where m is chosen to minimize the maximum adjacent difference.

For horizontal adjacency: (x, y) and (x+1, y).
φ(x, y) = n * ((y + xm) mod n) + x
φ(x+1, y) = n * ((y + (x+1)m) mod n) + x + 1

The difference depends on whether (y + xm) mod n and (y + (x+1)m) mod n wrap around. If no wraparound in the first coordinate: difference = n*m + 1. If wraparound: difference = n*m - n + 1 = n(m-1) + 1.

For vertical adjacency: (x, y) and (x, y+1).
φ(x, y) = n * ((y + xm) mod n) + x
φ(x, y+1) = n * ((y + 1 + xm) mod n) + x

If no wraparound: difference = n. If wraparound: difference = n - n² + ... wait, (y+1+xm) mod n = (y+xm) mod n + 1 if no wrap, or 0 if wrap. So difference = n or -n² + n = -n(n-1). The absolute difference is n or n(n-1).

The vertical wraparound gives n(n-1) which is huge. So this doesn't work either.

The issue is that any "linear" labeling on the torus will have wraparound issues.

Let me think about this problem from a higher level. 

The bandwidth of C_n × C_n. Let me search my memory... I believe the bandwidth of the toroidal grid C_n × C_n is 2n for even n and 2n-1 or n+1 for odd n... I'm not sure. Let me try to derive it.

Actually, let me reconsider. The bandwidth of the n×n grid P_n × P_n is n. The bandwidth of the n×n torus C_n × C_n should be roughly 2n because of the extra wraparound edges.

Wait, but our lower bound gave n+1. Let me re-examine.

The lower bound argument: cells with labels 1 and n² are at toroidal distance at most n-1 (for odd n, it's 2⌊n/2⌋ = n-1). Path of length n-1, total difference n²-1 = (n-1)(n+1). Max edge ≥ n+1.

But maybe we can get a better lower bound. The distance argument only uses two specific cells. Maybe using more cells we can get a better bound.

Let me think about a better lower bound. 

Consider the set S of cells with labels 1, 2, ..., k for some k. The "boundary" of S (cells in S adjacent to cells not in S) must be large enough. 

Actually, let me think about isoperimetric arguments. On the torus, the set of k cells with smallest labels has some boundary. The boundary edges connect to cells with larger labels. The maximum label difference across the boundary is at least... 

Hmm, this is getting complicated. Let me think about whether n+1 is actually the answer or if it's larger.

Let me try to construct a labeling with bandwidth n+1 for small cases and see if it works.

For n = 3 (3×3 torus), the answer should be n+1 = 4 if our conjecture is right. Let me try to construct a labeling of the 3×3 torus with max adjacent difference 4.

The 3×3 torus has 9 cells. Labels 1-9. Each cell has 4 neighbors.

Let me try:
```
1 2 3
5 6 4
9 7 8
```

Adjacencies (with wraparound):
Row 0: (0,0)=1, (1,0)=2, (2,0)=3. Horizontal: 1-2=1, 2-3=1, 3-1=2 (wraparound (2,0)-(0,0)).
Row 1: (0,1)=5, (1,1)=6, (2,1)=4. Horizontal: 5-6=1, 6-4=2, 4-5=1 (wraparound).
Row 2: (0,2)=9, (1,2)=7, (2,2)=8. Horizontal: 9-7=2, 7-8=1, 8-9=1 (wraparound).

Vertical:
Col 0: (0,0)=1, (0,1)=5, (0,2)=9. 1-5=4, 5-9=4, 9-1=8 (wraparound (0,2)-(0,0)).

The wraparound 9-1=8 is too big. So this doesn't work.

The problem is always the wraparound. Let me think about how to handle it.

For the 3×3 torus, can we achieve bandwidth 4? Let me try to be more careful.

We need all 18 edges (9 vertices × 4 / 2 = 18 edges) to have difference ≤ 4.

Let me try:
```
1 5 9
2 6 7
3 4 8
```

Horizontal:
Row 0: 1-5=4, 5-9=4, 9-1=8. Bad.

The wraparound in each row is the issue. In a row of 3 cells, the wraparound connects the first and last. If labels are a, b, c, we need |a-b|, |b-c|, |c-a| all ≤ 4. So the range max-min ≤ 4. But we have 3 numbers in a range of 4, so they could be like {1, 3, 5} or {1, 2, 5} etc.

Similarly for columns. So in each row, the 3 labels must span a range of at most 4, and in each column, the 3 labels must span a range of at most 4.

This is quite restrictive. Let me think...

If each row has range ≤ 4 and each column has range ≤ 4, and we have 9 labels total...

Let me try:
```
1 3 5
4 6 2
7 9 8
```
Wait, let me check. Actually let me be systematic.

Row 0: {1, 3, 5}, range 4. ✓
Row 1: {4, 6, 2} = {2, 4, 6}, range 4. ✓
Row 2: {7, 9, 8} = {7, 8, 9}, range 2. ✓

Col 0: {1, 4, 7}, range 6. ✗

Let me try:
```
1 4 2
5 8 6
3 9 7
```

Row 0: {1, 2, 4}, range 3. ✓
Row 1: {5, 6, 8}, range 3. ✓
Row 2: {3, 7, 9}, range 6. ✗

Hmm. This is tricky for n=3. Let me think about whether bandwidth 4 is even achievable for the 3×3 torus.

Actually, maybe the answer isn't n+1. Let me reconsider.

For n=3, the lower bound gives n+1 = 4. But maybe the actual bandwidth is higher.

Let me think about a better lower bound. 

Consider the 3×3 torus. It has 9 vertices and 18 edges. If the bandwidth is B, then for each edge (u, v), |label(u) - label(v)| ≤ B. 

Consider the vertex with label 1. Its 4 neighbors have labels in {2, ..., 9}, all within B of 1, so in {2, ..., B+1}. So at least 4 of the labels 2 through B+1 are used by neighbors of vertex 1. This means B+1 ≥ 5, so B ≥ 4. (This gives the same bound.)

Consider vertices with labels 1 and 9. Distance on 3×3 torus is at most 2 (since 2⌊3/2⌋ = 2). Path of length 2, difference 8, so some edge has difference ≥ 4. Same bound.

Can we get B ≥ 5 for n=3? Let me think...

Consider the vertex with label 5 (the median). Its 4 neighbors must have labels within B of 5, so in {5-B, ..., 5+B} ∩ {1,...,9} = {max(1, 5-B), ..., min(9, 5+B)}. For B=4, this is {1, ..., 9}, so no constraint. Not helpful.

Let me try a different approach. Consider the isoperimetric inequality on the torus.

For the 3×3 torus, consider the set S = {cells with labels 1, 2, 3, 4} (4 cells). The boundary ∂S (edges from S to V\S) has at least some number of edges. On the 3×3 torus, the minimum boundary of a set of 4 cells...

If the 4 cells form a 2×2 square, the boundary is 4*4 - 2*4 = 8 (each of 4 cells has 4 edges, 4 internal edges counted twice, so boundary = 16 - 2*4 = 8). Wait, let me count. A 2×2 square on the 3×3 torus: cells (0,0), (1,0), (0,1), (1,1). Internal edges: (0,0)-(1,0), (0,0)-(0,1), (1,0)-(1,1), (0,1)-(1,1) = 4 internal edges. Total edges from these 4 cells: 4*4 = 16. Boundary = 16 - 2*4 = 8.

If the 4 cells are in a row: (0,0), (1,0), (2,0), and one more. On the 3×3 torus, a row of 3 is a cycle (since wraparound), so (0,0), (1,0), (2,0) form a cycle with 3 internal edges. Adding one more cell, say (0,1): internal edges include the 3 from the row plus (0,0)-(0,1) = 4 internal edges. Boundary = 16 - 8 = 8.

Hmm, for 4 cells on the 3×3 torus, the minimum boundary seems to be 8. Actually, can we do better? What about 4 cells that form a "path" wrapping around? Like (0,0), (1,0), (2,0), (0,1)? That's what I just computed, boundary 8.

What about (0,0), (1,0), (2,0), (1,1)? Internal edges: (0,0)-(1,0), (1,0)-(2,0), (2,0)-(0,0) [wraparound], (1,0)-(1,1) = 4 internal. Boundary = 16 - 8 = 8.

So minimum boundary for 4 cells is 8? Let me check if we can get fewer. What about 4 cells forming a "diagonal"? (0,0), (1,1), (2,2), (0,1)? Internal edges: (0,0)-(0,1), (0,0)-(1,0)... wait (1,0) is not in the set. (0,0)-(2,0)? Not in set. Let me list: cells (0,0), (1,1), (2,2), (0,1).
- (0,0) neighbors: (1,0)✗, (2,0)✗, (0,1)✓, (0,2)✗. 1 internal.
- (1,1) neighbors: (2,1)✗, (0,1)✓, (1,0)✗, (1,2)✗. 1 internal.
- (2,2) neighbors: (0,2)✗, (1,2)✗, (2,0)✗, (2,1)✗. 0 internal.
- (0,1) neighbors: (1,1)✓, (2,1)✗, (0,0)✓, (0,2)✗. 2 internal.
Total internal edges: (0,0)-(0,1), (1,1)-(0,1) = 2. Boundary = 16 - 4 = 12. Worse.

So the minimum boundary for 4 cells on the 3×3 torus is 8 (achieved by a 2×2 block or similar).

Now, the boundary edges connect labels in {1,2,3,4} to labels in {5,6,7,8,9}. There are 8 boundary edges. The differences across these edges are at least 1 (since labels on one side are ≤ 4 and on the other side are ≥ 5). But we want to bound the maximum difference.

The maximum difference across the boundary is at least... well, the labels on the S side are {1,2,3,4} and on the V\S side are {5,6,7,8,9}. The maximum difference is at most 9-1 = 8. But we want a lower bound on the maximum.

Hmm, this approach gives a lower bound on the maximum boundary edge, but it's not immediately clear how to get a good bound.

Let me think about this differently. Let me consider a more refined isoperimetric argument.

Actually, let me reconsider the problem. Maybe the answer is 2n for the torus, not n+1.

For the n×n grid (no wraparound), bandwidth = n. The lower bound proof: consider the two corners (0,0) and (n-1, n-1). They're at distance 2(n-1). Path of length 2(n-1), difference n²-1. Max edge ≥ (n²-1)/(2(n-1)) = (n+1)/2. That gives (n+1)/2, which is weaker than n. So the distance argument alone doesn't give the tight bound for the grid.

The tight bound for the grid uses a different argument. Let me recall: for P_n × P_n, bandwidth = n. The lower bound uses the fact that if we remove the first k labels and the last k labels, the remaining cells form a "separator" that must contain a path from left to right and top to bottom, requiring at least n cells.

More precisely: Let B be the bandwidth. Consider the cells with labels in {k+1, ..., n²-k} for some k. These cells separate the cells with labels ≤ k from those with labels > n²-k. On the n×n grid, any set that separates the "left side" from the "right side" must have at least n cells. But I'm not sure this directly applies.

Actually, the standard proof for bandwidth of P_n × P_n = n goes like this: Consider any labeling. Look at the cell with label 1 and the cell with label n². Any path between them has length at least 2(n-1) (the diameter of the grid). The difference is n²-1. So max edge ≥ (n²-1)/(2(n-1)) ≈ n/2. That's not tight.

The tight proof: Consider the cell with label ⌊n²/2⌋. Its "level" (distance from the nearest corner) is at most... hmm, I don't remember the exact proof.

Let me look at this from a different angle. Let me think about what's known about the bandwidth of C_n × C_n.

Actually, I recall that the bandwidth of the Cartesian product of two cycles C_m × C_n (for m, n ≥ 3) is min(2m, 2n) when m ≠ n, and 2n when m = n. But I'm not confident about this.

Wait, for C_n × C_n, if the bandwidth is 2n, then for n = 2011, the answer would be 4022. But our lower bound only gives n+1 = 2012. Let me check with n = 3: if bandwidth of C_3 × C_3 is 2*3 = 6, is that right?

For the 3×3 torus, can we achieve bandwidth 5? Let me try.

We need all 18 edges to have difference ≤ 5. Each row is a 3-cycle, so the 3 labels in each row must pairwise differ by ≤ 5, meaning the range is ≤ 5. Similarly for columns.

Each row: 3 labels with range ≤ 5. Each column: 3 labels with range ≤ 5.

Let me try:
```
1 4 6
5 8 2
7 3 9
```
Wait, I need to use each label 1-9 exactly once. Let me check: 1,4,6,5,8,2,7,3,9. Yes, all present.

Row 0: {1, 4, 6}, range 5. ✓ (differences: 3, 2, 5)
Row 1: {5, 8, 2} = {2, 5, 8}, range 6. ✗

Let me try:
```
1 5 3
6 2 7
4 8 9
```
Row 0: {1, 3, 5}, range 4. ✓
Row 1: {2, 6, 7}, range 5. ✓
Row 2: {4, 8, 9}, range 5. ✓

Col 0: {1, 6, 4} = {1, 4, 6}, range 5. ✓
Col 1: {5, 2, 8} = {2, 5, 8}, range 6. ✗

Close! Let me adjust.

```
1 5 3
6 4 7
2 8 9
```
Row 0: {1, 3, 5}, range 4. ✓
Row 1: {4, 6, 7}, range 3. ✓
Row 2: {2, 8, 9}, range 7. ✗

Hmm. The issue is that we need to distribute the large and small numbers evenly.

Let me think about it as: we need a 3×3 Latin-square-like arrangement where each row and column has range ≤ 5.

The 9 numbers 1-9. If each row has range ≤ 5, the three numbers in each row span at most 5. If each column has range ≤ 5, similarly.

Let me try to make each row and column have numbers that are "close":

```
1 2 6
3 5 7
4 8 9
```
Row 0: {1, 2, 6}, range 5. ✓
Row 1: {3, 5, 7}, range 4. ✓
Row 2: {4, 8, 9}, range 5. ✓

Col 0: {1, 3, 4}, range 3. ✓
Col 1: {2, 5, 8}, range 6. ✗

```
1 3 6
2 5 8
4 7 9
```
Row 0: {1, 3, 6}, range 5. ✓
Row 1: {2, 5, 8}, range 6. ✗

The problem is that with 9 numbers in 3 rows of range 5, we need the rows to "overlap" in their ranges. Row ranges: if row 1 is {1,...,6}, row 2 is {2,...,7} or similar, row 3 is {4,...,9}. But then columns mix numbers from different ranges.

Let me try a different approach. Think of it as a 3×3 matrix where we want to minimize the max "row range" and "column range".

The optimal arrangement would interleave the numbers. Let me try:

```
1 6 4
7 2 5
3 8 9
```
Row 0: {1, 4, 6}, range 5. ✓
Row 1: {2, 5, 7}, range 5. ✓
Row 2: {3, 8, 9}, range 6. ✗

```
1 6 4
7 2 9
5 8 3
```
Row 0: {1, 4, 6}, range 5. ✓
Row 1: {2, 7, 9}, range 7. ✗

This is getting tedious. Let me think about it more systematically.

For n=3, we need each row (a 3-cycle) to have range ≤ B and each column (a 3-cycle) to have range ≤ B. The minimum B for which this is possible.

If B = 4: each row has 3 numbers with range ≤ 4, so the numbers are in an interval of length 4 (5 consecutive integers). Similarly for columns.

The 9 numbers are 1-9. If we partition them into 3 groups of 3 for rows, each group has range ≤ 4. The groups must cover {1,...,9}. Possible groupings:
- {1,2,3}, {4,5,6}, {7,8,9}: ranges 2, 2, 2. But then columns mix 1-3, 4-6, 7-9, giving column ranges of 6+. ✗
- {1,2,5}, {3,4,6}, {7,8,9}: ranges 4, 3, 2. Columns would mix these. Col with 5, 6, 9: range 4. Col with 1, 3, 7: range 6. ✗
- {1,3,5}, {2,4,6}, {7,8,9}: ranges 4, 4, 2. Col with 5, 6, 9: range 4. Col with 1, 2, 7: range 6. ✗
- {1,4,5}, {2,3,6}, {7,8,9}: Col with 5, 6, 9: range 4. Col with 1, 2, 7: range 6. ✗

The problem is always that 7, 8, 9 are far from 1, 2, 3. If one row has {7, 8, 9} and another has {1, 2, 3}, then any column containing one from each has range ≥ 4. But we also need the third row's numbers to bridge. If the third row has {4, 5, 6}, then columns are like {1, 4, 7} (range 6), {2, 5, 8} (range 6), {3, 6, 9} (range 6). All ranges 6 > 4. ✗

What if no row has {7, 8, 9}? We need to spread out the large numbers.
- {1, 2, 7}, {3, 4, 8}, {5, 6, 9}: Row ranges 6, 5, 4. Already row 0 has range 6 > 4. ✗
- {1, 5, 7}, {2, 4, 8}, {3, 6, 9}: Row ranges 6, 6, 6. ✗

For B = 4, we need each row to have range ≤ 4. The 9 numbers span 8 (from 1 to 9). With 3 rows each of range ≤ 4, the total "coverage" is at most 3*4 = 12 ≥ 8, so it's possible in principle. But the constraint is that the rows partition {1,...,9}.

Each row has 3 numbers in an interval of length 4 (5 consecutive values). The three intervals must cover {1,...,9} and be disjoint in their assigned numbers.

Possible: Row 1 uses {1, 2, 3, 4, 5} (picks 3), Row 2 uses {3, 4, 5, 6, 7} (picks 3), Row 3 uses {5, 6, 7, 8, 9} (picks 3). But they must be disjoint and cover all 9.

Row 1: {1, 2, 5} (from [1,5])
Row 2: {3, 4, 7} (from [3,7])
Row 3: {6, 8, 9} (from [5,9]) — range 3. ✓

Now arrange in columns. We need each column to have range ≤ 4.
Col 0: {1, 3, 6} — range 5. ✗

Row 1: {1, 2, 5}
Row 2: {3, 6, 7}
Row 3: {4, 8, 9}
Col 0: {1, 3, 4} — range 3. ✓
Col 1: {2, 6, 8} — range 6. ✗

Row 1: {1, 4, 5}
Row 2: {2, 3, 7}
Row 3: {6, 8, 9}
Col 0: {1, 2, 6} — range 5. ✗

Row 1: {1, 5, 4} → {1, 4, 5}
Row 2: {3, 6, 7}
Row 3: {2, 8, 9}
Col 0: {1, 3, 2} — range 2. ✓
Col 1: {4, 6, 8} — range 4. ✓
Col 2: {5, 7, 9} — range 4. ✓

Let me check all:
```
1 4 5
3 6 7
2 8 9
```
Row 0: {1, 4, 5}, range 4. ✓
Row 1: {3, 6, 7}, range 4. ✓
Row 2: {2, 8, 9}, range 7. ✗

Oops, row 2 has range 7. I said {2, 8, 9} but that's range 7, not from [5,9]. Let me recheck. 2 is not in [5,9]. So this doesn't satisfy the row constraint.

Let me be more careful. The three rows must partition {1,...,9} and each have range ≤ 4.

Row A: 3 numbers from [1, 5] (range ≤ 4)
Row B: 3 numbers from [a, a+4] for some a
Row C: 3 numbers from [b, b+4] for some b
Together they cover {1, ..., 9}.

The number 9 must be in some row with range ≤ 4, so that row has numbers in [5, 9]. Similarly, 1 must be in a row with numbers in [1, 5].

Case 1: Row containing 9 has 3 numbers from [5, 9]. Row containing 1 has 3 numbers from [1, 5]. The third row has the remaining 3 numbers.

If row 1 takes 3 from [1,5] and row 3 takes 3 from [5,9], they might share 5. The remaining 3 numbers go to row 2.

Row 1: {1, 2, 3} (from [1,5]), Row 3: {5, 6, 7} (from [5,9]) — wait, but then 8 and 9 are left for row 2, plus one more. Row 2: {4, 8, 9} — range 5. ✗

Row 1: {1, 2, 5}, Row 3: {6, 7, 8} — remaining: {3, 4, 9}. Row 2: {3, 4, 9} — range 6. ✗

Row 1: {1, 4, 5}, Row 3: {5, 8, 9} — can't, 5 is in both.

Row 1: {1, 2, 3}, Row 3: {7, 8, 9} — remaining: {4, 5, 6}. Row 2: {4, 5, 6} — range 2. ✓

So: Row 1: {1,2,3}, Row 2: {4,5,6}, Row 3: {7,8,9}. But then columns are {1,4,7}, {2,5,8}, {3,6,9}, all with range 6. ✗

Row 1: {1, 2, 4}, Row 3: {6, 7, 9} — remaining: {3, 5, 8}. Row 2: {3, 5, 8} — range 5. ✗

Row 1: {1, 3, 4}, Row 3: {6, 8, 9} — remaining: {2, 5, 7}. Row 2: {2, 5, 7} — range 5. ✗

Row 1: {1, 3, 5}, Row 3: {5, 7, 9} — share 5. ✗

Row 1: {1, 4, 5}, Row 3: {6, 8, 9} — remaining: {2, 3, 7}. Row 2: {2, 3, 7} — range 5. ✗

Row 1: {1, 2, 5}, Row 3: {6, 8, 9} — remaining: {3, 4, 7}. Row 2: {3, 4, 7} — range 4. ✓

So: Row 1: {1, 2, 5}, Row 2: {3, 4, 7}, Row 3: {6, 8, 9}.
Now arrange columns. We need each column to have range ≤ 4.

Columns are formed by picking one from each row. We need to arrange so that each column's 3 numbers have range ≤ 4.

Row 1: {1, 2, 5}, Row 2: {3, 4, 7}, Row 3: {6, 8, 9}.

Column with 1 (from row 1): needs partners from row 2 and row 3 with all in range 4. So max - min ≤ 4. If 1 is the min, max ≤ 5. From row 3, only 6, 8, 9 are available, all > 5. ✗

So 1 can't be in a column with range ≤ 4 if row 3 has {6, 8, 9}, because 6 - 1 = 5 > 4.

What if we rearrange? The issue is that 1 and 6 (or higher) must be in the same column, and 6 - 1 = 5 > 4.

So with B = 4, we can't have a row with {6, 8, 9} and a row with 1, because they'd need to share a column.

What if 9 is in a row with smaller numbers?

Row 3: {5, 6, 9} (range 4, from [5,9]). Row 1: {1, 2, 3} (from [1,5]). Remaining: {4, 7, 8}. Row 2: {4, 7, 8} — range 4. ✓

Columns: Row 1: {1, 2, 3}, Row 2: {4, 7, 8}, Row 3: {5, 6, 9}.
Column with 1: partners from {4, 7, 8} and {5, 6, 9}. Need range ≤ 4. 1 and 5: range 4. 1 and 6: range 5. ✗ (if 6 is in the same column as 1).

Can we avoid putting 6 in the same column as 1? We need to arrange:
Col A: 1, ?, ?  — from row 2 and row 3. Need max ≤ 5. From row 2: {4} (only 4 ≤ 5, since 7, 8 > 5). From row 3: {5} (only 5 ≤ 5, since 6, 9 > 5). So col A = {1, 4, 5}. Range 4. ✓

Col B: 2, ?, ? — from remaining row 2: {7, 8}, row 3: {6, 9}. Need range ≤ 4. 2 and 6: range 4. 2 and 7: range 5. ✗ (7 or 8 with 2 gives range > 4). So we need 6 with 2. Col B = {2, ?, 6}. From row 2: {7, 8}. 2 and 7: range 5. ✗.

So col B can't have range ≤ 4 if it contains 2 and a number from {7, 8}. 

What if col B = {2, 7, 6}? Range 5. ✗. {2, 8, 6}? Range 6. ✗.

So this doesn't work either. The problem is that 2 is too small to be in a column with 7 or 8.

Hmm, it seems like B = 4 might not be achievable for the 3×3 torus. Let me try B = 5.

With B = 5, each row and column has range ≤ 5.

Row 1: {1, 2, 6}, Row 2: {3, 4, 7}, Row 3: {5, 8, 9}.
Row ranges: 5, 4, 4. ✓

Columns: 
Col A: {1, 3, 5} — range 4. ✓
Col B: {2, 4, 8} — range 6. ✗

Row 1: {1, 2, 6}, Row 2: {3, 5, 7}, Row 3: {4, 8, 9}.
Row ranges: 5, 4, 5. ✓

Col A: {1, 3, 4} — range 3. ✓
Col B: {2, 5, 8} — range 6. ✗

Row 1: {1, 3, 6}, Row 2: {2, 5, 7}, Row 3: {4, 8, 9}.
Row ranges: 5, 5, 5. ✓

Col A: {1, 2, 4} — range 3. ✓
Col B: {3, 5, 8} — range 5. ✓
Col C: {6, 7, 9} — range 3. ✓

All columns have range ≤ 5! Let me verify:

```
1 3 6
2 5 7
4 8 9
```

Row 0: {1, 3, 6}. Differences: |1-3|=2, |3-6|=3, |6-1|=5 (wraparound). Max = 5. ✓
Row 1: {2, 5, 7}. Differences: |2-5|=3, |5-7|=2, |7-2|=5 (wraparound). Max = 5. ✓
Row 2: {4, 8, 9}. Differences: |4-8|=4, |8-9|=1, |9-4|=5 (wraparound). Max = 5. ✓

Col 0: {1, 2, 4}. Differences: |1-2|=1, |2-4|=2, |4-1|=3 (wraparound). Max = 3. ✓
Col 1: {3, 5, 8}. Differences: |3-5|=2, |5-8|=3, |8-3|=5 (wraparound). Max = 5. ✓
Col 2: {6, 7, 9}. Differences: |6-7|=1, |7-9|=2, |9-6|=3 (wraparound). Max = 3. ✓

All differences ≤ 5. So bandwidth ≤ 5 for the 3×3 torus.

Now, is bandwidth 4 achievable? From my attempts above, it seems very hard. Let me try to prove it's impossible.

For B = 4 on the 3×3 torus: each row (3-cycle) has range ≤ 4, each column (3-cycle) has range ≤ 4.

In a 3-cycle with labels a, b, c, the range is max(a,b,c) - min(a,b,c), and all pairwise differences must be ≤ B. For a 3-cycle, the pairwise differences are |a-b|, |b-c|, |c-a|, and the max of these is the range. So range ≤ B = 4.

Now, 9 must be in some row. That row has 3 numbers with range ≤ 4, so all in [5, 9]. Similarly, 1 is in some row with all numbers in [1, 5].

If 1 and 9 are in the same row: range ≥ 8 > 4. ✗. So they're in different rows.

Row containing 9: 3 numbers in [5, 9].
Row containing 1: 3 numbers in [1, 5].
Third row: 3 remaining numbers.

The row containing 9 has numbers from {5, 6, 7, 8, 9}, picking 3. The row containing 1 has numbers from {1, 2, 3, 4, 5}, picking 3. They might share 5.

If they share 5: Row A has 5 and two from {6,7,8,9}, Row B has 5 and two from {1,2,3,4}. But 5 can only be used once. So they can't share 5.

Case 1: Row A (contains 9) = 3 from {5,6,7,8,9}, Row B (contains 1) = 3 from {1,2,3,4,5}, disjoint.

Sub-cases based on whether 5 is in Row A or Row B.

Case 1a: 5 in Row A. Row A: 3 from {5,6,7,8,9} including 9. Row B: 3 from {1,2,3,4} including 1. Third row: remaining 3 from {5,6,7,8,9} ∪ {1,2,3,4} minus what's taken. Wait, total is {1,...,9}. Row A takes 3 from {5,6,7,8,9}, Row B takes 3 from {1,2,3,4}. That's 3+3 = 6 numbers, but {5,6,7,8,9} has 5 and {1,2,3,4} has 4, total 9. Row A takes 3 from 5, Row B takes 3 from 4. Remaining: 2 from {5,6,7,8,9} and 1 from {1,2,3,4} = 3 numbers for the third row.

Third row has 2 numbers from {5,...,9} and 1 from {1,...,4}. Range of third row: at least 5 - 4 = 1, but could be up to 9 - 1 = 8. We need range ≤ 4.

If the third row has a number from {1,...,4} and two from {5,...,9}, the range is at least 5 - 4 = 1 but at most 9 - 1 = 8. For range ≤ 4, we need max - min ≤ 4. If the small number is k (from {1,...,4}) and the large numbers are from {5,...,9}, we need the large numbers ≤ k + 4. So if k = 4, large numbers ≤ 8. If k = 3, large ≤ 7. If k = 2, large ≤ 6. If k = 1, large ≤ 5.

Case 1a, k = 4: Third row has 4 and two from {5, 6, 7, 8} (since ≤ 8). Row B takes 3 from {1, 2, 3} (since 4 is in third row). Row A takes 3 from {5, 6, 7, 8, 9} including 9, minus the two in third row.

Third row: {4, a, b} where a, b ∈ {5, 6, 7, 8}.
Row A: 3 from {5, 6, 7, 8, 9} \ {a, b} ∪ {9}. So Row A = {9, and two from {5,6,7,8}\{a,b}}. 
Row B: {1, 2, 3}.

Now check columns. Each column has one from each row. Row B has {1, 2, 3}. 

Column containing 1: also has one from Row A (from {5,...,9}) and one from third row (from {4, a, b}). Range ≤ 4 means max - min ≤ 4. Min is 1, so max ≤ 5. From Row A, only 5 is ≤ 5. From third row, only 4 is ≤ 5 (since a, b ≥ 5). So column with 1 must be {1, 5, 4}. But 5 must be in Row A. Is 5 in Row A? Row A = {9, and two from {5,6,7,8}\{a,b}}. If 5 ∉ {a, b}, then 5 ∈ Row A. If 5 ∈ {a, b}, then 5 ∉ Row A, and we can't form column {1, 5, 4}.

If 5 ∉ {a, b}: Column with 1 = {1, 5, 4}. ✓. Then 5 is used in this column.
Column with 2: from Row A (remaining: {9, one from {6,7,8}\{a,b}}) and third row (remaining: {a, b}). Range ≤ 4, min is 2, max ≤ 6. From Row A: 9 > 6 ✗, or the one from {6,7,8}: 6 ✓, 7 ✗, 8 ✗. From third row: a, b ∈ {5, 6, 7, 8}, need ≤ 6: only 5 or 6. But 5 is already used (in column with 1). So from third row: 6 (if 6 ∈ {a,b}).

This is getting very complicated. Let me just check: is it possible?

Column with 2 = {2, x, y} where x from Row A \ {5}, y from third row \ {4}. Need max(2, x, y) - 2 ≤ 4, so x, y ≤ 6.

Row A \ {5} = {9, one from {6,7,8}\{a,b}}. For x ≤ 6: x must be 6 (if 6 is in Row A, i.e., 6 ∉ {a,b}) or... 9 > 6. So x = 6, requiring 6 ∈ Row A, i.e., 6 ∉ {a, b}.

Third row \ {4} = {a, b}. For y ≤ 6: y ∈ {5, 6} ∩ {a, b}. Since 5 ∉ {a, b} (we assumed), y = 6. But 6 ∉ {a, b} (just stated). Contradiction! y must be in {a, b} but also = 6 and 6 ∉ {a, b}. ✗

So this case fails.

Case 1a, k = 3: Third row has 3 and two from {5, 6, 7} (since ≤ 3+4 = 7). Row B takes 3 from {1, 2, 4} (since 3 is in third row, and 5 is in Row A). Wait, Row B takes from {1, 2, 3, 4} \ {3} = {1, 2, 4}. So Row B = {1, 2, 4}.

Third row: {3, a, b} where a, b ∈ {5, 6, 7}.
Row A: 3 from {5, 6, 7, 8, 9} \ {a, b} including 9. So Row A = {9, 8, and one from {5,6,7}\{a,b}}.

Column with 1: from Row A and third row. Min = 1, max ≤ 5. From Row A: only 5 (if 5 ∈ Row A, i.e., 5 ∉ {a,b}). From third row: only 3 (since a, b ≥ 5). So column = {1, 5, 3}. Need 5 ∈ Row A.

If 5 ∉ {a, b}: Column with 1 = {1, 5, 3}. ✓
Column with 2: from Row A \ {5} = {9, 8, one from {6,7}\{a,b}} and third row \ {3} = {a, b}. Min = 2, max ≤ 6. From Row A: 9 ✗, 8 ✗, 6 ✓ (if 6 ∈ Row A, i.e., 6 ∉ {a,b}), 7 ✗. From third row: a, b ∈ {5, 6, 7}, need ≤ 6: 5 or 6. But 5 ∉ {a, b}. So 6, but 6 ∉ {a, b}. ✗

Same contradiction.

Case 1a, k = 2: Third row has 2 and two from {5, 6} (since ≤ 6). Row B takes from {1, 3, 4}. Row B = {1, 3, 4}.

Third row: {2, 5, 6} (must be exactly these since only 5, 6 ≤ 6 from {5,...,9}).
Row A: {7, 8, 9} (remaining from {5,...,9}).

Column with 1: from Row A = {7, 8, 9} and third row = {2, 5, 6}. Min = 1, max ≤ 5. From Row A: all ≥ 7 > 5. ✗

Case 1a, k = 1: Third row has 1 and two from {5} (since ≤ 5). Only 5 available. Third row = {1, 5, ?}. Need one more from {5,...,9} with ≤ 5, so 5. But 5 already used. ✗ (Can't have two 5s.)

So Case 1a (5 in Row A) fails completely.

Case 1b: 5 in Row B. Row A: 3 from {6, 7, 8, 9} including 9. Row B: 3 from {1, 2, 3, 4, 5} including 1 and 5. Third row: remaining 3.

Row A: 3 from {6, 7, 8, 9}, range ≤ 4. {6, 7, 8, 9} has range 3, so any 3 from it have range ≤ 3 ≤ 4. ✓
Row B: 3 from {1, 2, 3, 4, 5} including 1 and 5, range ≤ 4. {1, ..., 5} has range 4. So Row B = {1, 5, x} where x ∈ {2, 3, 4}. Range = 4. ✓

Third row: 3 remaining from {1,...,9} \ (Row A ∪ Row B). 
Row A takes 3 from {6,7,8,9}, Row B takes {1, 5, x}. Remaining: {2, 3, 4} \ {x} ∪ ({6,7,8,9} \ Row A). That's 2 + 1 = 3 numbers.

Third row has 2 from {2, 3, 4} and 1 from {6, 7, 8, 9}. Range of third row: at least 6 - 4 = 2, at most 9 - 2 = 7. Need ≤ 4.

If the number from {6,...,9} is m and the two from {2,3,4}\{x} are p, q, then max - min ≤ 4. Max is m, min is min(p, q). So m - min(p,q) ≤ 4.

If min(p, q) = 2: m ≤ 6. So m = 6.
If min(p, q) = 3: m ≤ 7. So m ∈ {6, 7}.
If min(p, q) = 4: m ≤ 8. So m ∈ {6, 7, 8}.

Sub-case: m = 6, min(p,q) = 2. So third row includes 6 and 2. p, q ∈ {2, 3, 4} \ {x}. If 2 ∈ {p, q}, then x ≠ 2, so x ∈ {3, 4}.

Third row: {2, 6, y} where y ∈ {3, 4} \ {x}. Since x ∈ {3, 4}, y is the other one. So third row = {2, 6, y} where {x, y} = {3, 4}.

Row A: 3 from {6, 7, 8, 9} \ {6} = {7, 8, 9}. Row A = {7, 8, 9}.
Row B: {1, 5, x} where x ∈ {3, 4}.
Third row: {2, 6, y} where y is the other of {3, 4}.

Now check columns. Each column has one from each row.

Row A = {7, 8, 9}, Row B = {1, 5, x}, Third row = {2, 6, y}.

Column with 1 (from Row B): from Row A and third row. Min = 1, max ≤ 5. From Row A: all ≥ 7 > 5. ✗

So this fails because 1 can't be in a column with any element of Row A (all ≥ 7).

Sub-case: m = 7, min(p,q) = 3. Third row includes 7 and 3. p, q ∈ {2, 3, 4} \ {x} with min = 3, so 3 ∈ {p, q} and 2 ∉ {p, q}, meaning x = 2. So Row B = {1, 5, 2}. Third row = {3, 7, 4} (p, q = 3, 4). Range = 4. ✓

Row A = {6, 8, 9} (remaining from {6,7,8,9} \ {7}).

Column with 1 (from Row B = {1, 2, 5}): from Row A = {6, 8, 9} and third row = {3, 4, 7}. Min = 1, max ≤ 5. From Row A: all ≥ 6 > 5. ✗

Same problem.

Sub-case: m = 6, min(p,q) = 3. Third row includes 6 and 3. x = 2 (since 2 ∉ {p,q}). Row B = {1, 5, 2}. Third row = {3, 6, 4}. Range = 3. ✓

Row A = {7, 8, 9} (from {6,7,8,9} \ {6}).

Column with 1: from Row A = {7, 8, 9}. All > 5. ✗

Sub-case: m = 6, min(p,q) = 4. Third row includes 6 and 4. x ∈ {2, 3} (since 2, 3 ∉ {p, q} means... wait, p, q ∈ {2, 3, 4} \ {x} with min = 4, so both p, q ≥ 4, meaning {p, q} = {4} — but we need 2 elements. ✗ Impossible since only one element ≥ 4 in {2, 3, 4} \ {x}.

Sub-case: m = 7, min(p,q) = 4. {p, q} ⊆ {4} — only one element. ✗

Sub-case: m = 8, min(p,q) = 4. Same issue. ✗

So in Case 1b, the problem is always that 1 (in Row B) must share a column with an element of Row A (all ≥ 6), giving range ≥ 5 > 4.

Case 2: Row containing 9 and Row containing 1 share the number 5. But each number is used once, so they can't share. Already ruled out.

So for n = 3, B = 4 is impossible! The bandwidth of C_3 × C_3 is 5.

But our lower bound gave n + 1 = 4. So the lower bound is not tight for n = 3, and the actual answer is 5 > 4 = n + 1.

Hmm, so the answer is not n + 1. Let me reconsider.

For n = 3, bandwidth = 5 = 2n - 1.

Let me check n = 2 (but n = 2 is even, and the problem has n = 2011 which is odd, so let me focus on odd n).

Actually wait, let me reconsider the lower bound. For n = 3, the diameter of the 3×3 torus is 2⌊3/2⌋ = 2. The distance between labels 1 and 9 is at most 2. Path of length 2, difference 8, max edge ≥ 4. But actual bandwidth is 5.

Can we get a better lower bound? Let me think...

For n = 3, consider the cell with label 1. Its 4 neighbors have labels in {2, ..., 9}, all within B of 1. So neighbors have labels ≤ 1 + B. For B = 4, neighbors have labels ≤ 5. There are 4 neighbors, so 4 of the labels {2, 3, 4, 5} are used. That's all of them. So the 4 neighbors of cell 1 have labels {2, 3, 4, 5}.

Now consider the cell with label 9. Its 4 neighbors have labels ≥ 9 - B = 5. For B = 4, neighbors have labels ≥ 5. There are 4 neighbors, so 4 of the labels {5, 6, 7, 8} are used. But label 5 is already used (by a neighbor of cell 1, or by cell 1's neighbor). Wait, label 5 is used by some cell. If that cell is a neighbor of cell 1, can it also be a neighbor of cell 9? On the 3×3 torus, two cells share a neighbor only if they're close.

Actually, let me think about this more carefully. Cell 1's neighbors have labels {2, 3, 4, 5}. Cell 9's neighbors have labels from {5, 6, 7, 8}. Label 5 is a neighbor of cell 1. Is label 5 also a neighbor of cell 9? If so, then cell 5 is adjacent to both cell 1 and cell 9. On the 3×3 torus, the distance between cell 1 and cell 9 is at most 2. If they share a neighbor, the distance is exactly 2 (via that neighbor).

But cell 9's neighbors are 4 cells with labels from {5, 6, 7, 8}. If label 5 is a neighbor of cell 9, then cell 9's neighbors include label 5 and three from {6, 7, 8}. That's 4 neighbors: {5, 6, 7, 8}.

If label 5 is NOT a neighbor of cell 9, then cell 9's neighbors are 4 from {6, 7, 8}. But {6, 7, 8} has only 3 elements. ✗ So label 5 must be a neighbor of cell 9.

So cell 5 is adjacent to both cell 1 and cell 9. Now, cell 1's neighbors are {2, 3, 4, 5} and cell 9's neighbors are {5, 6, 7, 8}.

The remaining cells are: cell 1, cell 9, and cells with labels {2, 3, 4, 5, 6, 7, 8}. Cell 5 is adjacent to both 1 and 9.

Now, cell 5 has 4 neighbors. Two of them are cell 1 and cell 9. The other two have labels from {2, 3, 4, 6, 7, 8}. These two neighbors of cell 5 must have labels within B = 4 of 5, so in {1, 2, 3, 4, 5, 6, 7, 8, 9} ∩ [5-4, 5+4] = {1, ..., 9}. That's everything, so no constraint. Not helpful.

Let me think about the structure differently. On the 3×3 torus, cell 1 has 4 neighbors forming a "cross" around it. Cell 9 has 4 neighbors forming a cross around it. These crosses share cell 5.

The 3×3 torus has 9 cells. Cell 1, cell 9, cell 5, and 6 others. The 4 neighbors of cell 1 are {2, 3, 4, 5}. The 4 neighbors of cell 9 are {5, 6, 7, 8}. So cells {2, 3, 4} are neighbors of 1 but not 9, and cells {6, 7, 8} are neighbors of 9 but not 1.

On the 3×3 torus, the 4 neighbors of a cell form a cross (up, down, left, right). If cell 5 is a neighbor of both cell 1 and cell 9, then cells 1 and 9 are at distance 2 through cell 5. 

The 3 non-shared neighbors of cell 1 ({2, 3, 4}) and the 3 non-shared neighbors of cell 9 ({6, 7, 8}) must be arranged on the torus. 

Cell 1 has 4 neighbors: cell 5 and {2, 3, 4}. On the torus, these 4 neighbors are in 4 directions. Cell 5 is in one direction. The other 3 are in the remaining 3 directions.

Similarly, cell 9 has 4 neighbors: cell 5 and {6, 7, 8}.

Now, cell 5 is in one direction from cell 1 and one direction from cell 9. Since cell 5 is adjacent to both, and on the torus, cell 1 and cell 9 are at distance 2, cell 5 is "between" them.

Let me set up coordinates. Say cell 1 is at (0, 0). Its neighbors are (1, 0), (2, 0), (0, 1), (0, 2) (i.e., (±1, 0) and (0, ±1) mod 3). Say cell 5 is at (1, 0). Then cell 9 is at (2, 0) (the neighbor of cell 5 in the same direction, so cell 9 is at distance 2 from cell 1 in the x-direction).

Cell 9 at (2, 0) has neighbors: (0, 0) = cell 1, (1, 0) = cell 5, (2, 1), (2, 2). So cell 9's neighbors are cells 1, 5, and two others with labels from {6, 7, 8}. But we said cell 9's neighbors are {5, 6, 7, 8}, which is 4 cells. But cell 1 is also a neighbor of cell 9! So cell 1 (label 1) is a neighbor of cell 9 (label 9), giving difference 8 > 4. ✗

Wait, that's a contradiction! If cell 1 and cell 9 are at distance 2 on the 3×3 torus, and the torus has diameter 2, then... actually, on the 3×3 torus, the diameter is 2, so any two cells are at distance ≤ 2. But are cells 1 and 9 necessarily at distance 2? They could be at distance 1 (adjacent) or distance 2.

If cells 1 and 9 are adjacent: difference = 8 > B = 4. ✗ So for B = 4, cells 1 and 9 can't be adjacent.

If cells 1 and 9 are at distance 2: they share at least one common neighbor (on the 3×3 torus, two cells at distance 2 share exactly 2 common neighbors if they're in the same row/column, or 1 common neighbor if they're diagonal). Wait, on the 3×3 torus, let me think...

Actually, on the 3×3 torus, every pair of non-adjacent cells is at distance 2. And the 3×3 torus is a strongly regular graph? Let me check. C_3 × C_3 has 9 vertices, each of degree 4. Two adjacent vertices share 0 common neighbors (since it's a Cartesian product of two C_3's, and C_3 has no triangles... wait, C_3 is a triangle, so C_3 × C_3 does have triangles? No, C_3 × C_3 is the Cartesian product. Two vertices (x1, y1) and (x2, y2) are adjacent if x1 = x2 and y1, y2 adjacent in C_3, or y1 = y2 and x1, x2 adjacent in C_3.

If (0,0) and (1,0) are adjacent (same y, x differs by 1 in C_3). Common neighbors: a cell adjacent to both. (0,0)'s neighbors: (1,0), (2,0), (0,1), (0,2). (1,0)'s neighbors: (0,0), (2,0), (1,1), (1,2). Common: (2,0). So they share 1 common neighbor.

If (0,0) and (1,1) are at distance 2 (not adjacent). (0,0)'s neighbors: (1,0), (2,0), (0,1), (0,2). (1,1)'s neighbors: (0,1), (2,1), (1,0), (1,2). Common: (1,0) and (0,1). So they share 2 common neighbors.

OK so on the 3×3 torus, adjacent vertices share 1 common neighbor, and distance-2 vertices share 2 common neighbors.

Now, back to B = 4. Cells 1 and 9 can't be adjacent (difference 8 > 4). So they're at distance 2, sharing 2 common neighbors.

Cell 1's neighbors: {2, 3, 4, 5} (4 cells with labels 2-5).
Cell 9's neighbors: {5, 6, 7, 8} (4 cells with labels 5-8).
Common neighbors: 2 cells. One of them has label 5 (since 5 is in both sets). The other common neighbor has a label in {2, 3, 4} ∩ {6, 7, 8} = ∅. ✗

The second common neighbor must have a label in both {2, 3, 4, 5} and {5, 6, 7, 8}, so in {5}. But we need 2 common neighbors and only label 5 is in the intersection. ✗

So B = 4 is impossible for the 3×3 torus! This confirms bandwidth ≥ 5.

Great, so for n = 3, the bandwidth is 5 = 2n - 1.

Let me check if this generalizes. For odd n, is the bandwidth of C_n × C_n equal to 2n - 1?

Hmm, wait. Let me reconsider. For n = 3, 2n - 1 = 5. For general odd n, the answer might be 2n - 1 or something else.

Let me think about the lower bound more carefully for general n.

Actually, let me reconsider the lower bound argument. For n = 3, the key was that cells 1 and 9 must be at distance 2 (not adjacent), and their neighbor sets must overlap, but the overlap isn't big enough.

For general odd n, let me think about a better lower bound.

Consider the cell with label 1. Its neighbors have labels ≤ 1 + B. So at most B labels (from 2 to B+1) are available for 4 neighbors. This gives B ≥ 4, which is weak.

Let me think about the isoperimetric approach. Consider the set S_k = {cells with labels 1, ..., k}. The edge boundary ∂S_k consists of edges from S_k to V \ S_k. Each such edge has difference at least 1 (since one endpoint has label ≤ k and the other > k). But we want to bound the maximum difference.

Actually, the key insight is: the maximum difference across the boundary is at least (k+1) - k = 1, but we can be smarter. The boundary edges connect labels ≤ k to labels > k. The maximum such difference is at least (max label outside S_k adjacent to S_k) - (min label in S_k adjacent to outside). 

Hmm, this is hard to bound directly. Let me think about a different approach.

Let me consider the "separator" approach. For any labeling with bandwidth B, consider the set of cells with labels in {1, ..., B}. These B cells include the cell with label 1 and all its neighbors (since neighbors have labels ≤ 1 + B). So the cell with label 1 and its 4 neighbors are among the first B+1 labels.

More generally, consider the cells with labels in {1, ..., kB} for integer k. The cell with label 1 is in this set, and so are all cells reachable from cell 1 by a path of length ≤ k (since each edge adds at most B to the label). So the set {cells with labels ≤ kB} contains the ball of radius k around cell 1.

The ball of radius k on the n×n torus has size at most 1 + 4 + 8 + ... + 4k = 1 + 2k(k+1) for small k (when the ball doesn't wrap around). Actually, on the torus, the ball of radius k around a cell has size min(1 + 2k(k+1), n²) for k < n/2.

So we need kB ≥ |ball of radius k|, i.e., kB ≥ 1 + 2k(k+1) for k < n/2. This gives B ≥ (1 + 2k(k+1))/k = 1/k + 2(k+1) = 2k + 2 + 1/k. For large k, this gives B ≥ 2k + 2, so B ≥ 2(n/2) + 2 = n + 2 (approximately). But this isn't tight either.

Hmm wait, let me reconsider. The ball of radius k on the torus: for k ≤ (n-1)/2, the ball doesn't wrap around, and its size is 1 + 4·(1 + 2 + ... + k) = 1 + 4·k(k+1)/2 = 1 + 2k(k+1). For k = (n-1)/2, the ball has size 1 + 2·((n-1)/2)·((n+1)/2) = 1 + (n-1)(n+1)/2 = 1 + (n²-1)/2 = (n²+1)/2.

So we need ((n-1)/2) · B ≥ (n²+1)/2, giving B ≥ (n²+1)/(n-1) = (n²+1)/(n-1). 

(n²+1)/(n-1) = (n²-1+2)/(n-1) = (n+1) + 2/(n-1). For n = 2011, this is 2012 + 2/2010 = 2012.000993..., so B ≥ 2013 (since B is an integer and B ≥ 2012.001).

Wait, that gives B ≥ 2013, not 2012! Let me double-check.

For k = (n-1)/2 = 1005 (with n = 2011):
Ball size = 1 + 2·1005·1006 = 1 + 2·1005·1006.

1005 · 1006 = 1005 · 1000 + 1005 · 6 = 1005000 + 6030 = 1011030.
2 · 1011030 = 2022060.
Ball size = 2022061.

We need 1005 · B ≥ 2022061, so B ≥ 2022061 / 1005 = 2012.94...

So B ≥ 2013.

Hmm, but wait. Let me reconsider whether the ball of radius k is exactly 1 + 2k(k+1) on the torus for k ≤ (n-1)/2.

On the n×n torus, the ball of radius r around a cell is the set of cells at toroidal distance ≤ r. For r ≤ (n-1)/2 (with n odd), the ball doesn't "wrap around" and is a diamond shape. The number of cells at distance exactly d from the center is 4d for d ≥ 1 (and 1 for d = 0). So the ball of radius r has 1 + Σ_{d=1}^{r} 4d = 1 + 4·r(r+1)/2 = 1 + 2r(r+1) cells.

For r = (n-1)/2: 1 + 2·((n-1)/2)·((n+1)/2) = 1 + (n²-1)/2 = (n²+1)/2.

So the ball of radius (n-1)/2 has (n²+1)/2 cells, which is slightly more than half the torus.

Now, the constraint is: the set of cells with labels ≤ L contains the ball of radius r around cell 1, where L = r·B (since each step from cell 1 can increase the label by at most B). More precisely, any cell at distance d from cell 1 has label ≤ 1 + dB. So cells at distance ≤ r have labels ≤ 1 + rB. The number of such cells is |ball(r)|, and they all have labels in {1, ..., 1+rB}. So 1 + rB ≥ |ball(r)|, i.e., rB ≥ |ball(r)| - 1.

For r = (n-1)/2: rB ≥ (n²+1)/2 - 1 = (n²-1)/2. So B ≥ (n²-1)/(2r) = (n²-1)/(n-1) = n+1.

Wait, that gives B ≥ n+1 = 2012, not 2013! Let me recheck.

r = (n-1)/2, |ball(r)| = (n²+1)/2. 
rB ≥ |ball(r)| - 1 = (n²+1)/2 - 1 = (n²-1)/2.
B ≥ (n²-1)/(2r) = (n²-1)/(n-1) = n+1.

So B ≥ n+1 = 2012. OK so the ball argument gives B ≥ n+1, same as the path argument. I made an arithmetic error before. Let me redo:

r = (n-1)/2 = 1005.
|ball(r)| = (n²+1)/2 = (2011² + 1)/2 = (4044121 + 1)/2 = 2022061.
rB ≥ |ball(r)| - 1 = 2022060.
B ≥ 2022060 / 1005 = 2012.0 exactly? Let me check: 1005 · 2012 = 1005 · 2000 + 1005 · 12 = 2010000 + 12060 = 2022060. Yes! So B ≥ 2012 exactly.

So the ball argument gives B ≥ n+1 = 2012, which matches the path argument. But for n = 3, this gives B ≥ 4, while the actual bandwidth is 5. So the ball argument isn't tight.

Let me think about what gives the tighter bound for n = 3.

For n = 3, the argument that worked was: cells 1 and 9 can't be adjacent (diff 8 > 4), so they're at distance 2. Their neighbor sets must overlap in 2 cells (on the 3×3 torus, distance-2 pairs share 2 common neighbors). The overlap requires 2 labels in {2,3,4,5} ∩ {5,6,7,8} = {5}, which has only 1 element. Contradiction.

Can we generalize this? For general n, consider cells 1 and n². They can't be adjacent if n² - 1 > B, i.e., B < n² - 1 (which is always true for reasonable B). So they're at some distance d ≥ 2.

The neighbors of cell 1 have labels ≤ 1 + B, so in {2, ..., B+1}.
The neighbors of cell n² have labels ≥ n² - B, so in {n²-B, ..., n²-1}.

For these neighbor sets to be disjoint (no common neighbor), we need B+1 < n²-B, i.e., 2B < n²-1, i.e., B < (n²-1)/2. For B = n+1 = 2012 and n = 2011, (n²-1)/2 = 2022060, so B = 2012 << 2022060. So the neighbor sets are disjoint.

But on the torus, cells 1 and n² at distance d share some common neighbors. If d = 2, they share common neighbors. But the neighbor label sets are disjoint, so no common neighbor can exist. This means cells 1 and n² can't be at distance 2.

More generally, cells 1 and n² at distance d: a common neighbor of cells 1 and n² would be at distance 1 from both, so it would need a label in {2, ..., B+1} ∩ {n²-B, ..., n²-1}, which is empty for B < (n²-1)/2. So cells 1 and n² have no common neighbors, meaning they're at distance ≥ 3.

But wait, on the n×n torus, the diameter is n-1 (for odd n). So cells 1 and n² are at distance between 3 and n-1.

Hmm, but this doesn't directly give a better bound. Let me think more.

Actually, the constraint is stronger. Not just the neighbors of cell 1, but all cells at distance ≤ r from cell 1 have labels ≤ 1 + rB. And all cells at distance ≤ r from cell n² have labels ≥ n² - rB. For these two balls to be disjoint, we need 1 + rB < n² - rB, i.e., 2rB < n² - 1, i.e., r < (n²-1)/(2B).

For B = n+1: r < (n²-1)/(2(n+1)) = (n-1)/2. So for r = (n-1)/2, the two balls just barely touch (1 + rB = 1 + (n-1)/2 · (n+1) = 1 + (n²-1)/2 = (n²+1)/2, and n² - rB = n² - (n²-1)/2 = (n²+1)/2). So they meet exactly at (n²+1)/2.

The ball of radius (n-1)/2 around cell 1 has (n²+1)/2 cells, all with labels ≤ (n²+1)/2. The ball of radius (n-1)/2 around cell n² has (n²+1)/2 cells, all with labels ≥ (n²+1)/2. Together, these two balls have n²+1 cells, but the torus only has n² cells. So they overlap in at least 1 cell.

The overlap cell has label ≤ (n²+1)/2 (from ball 1) and ≥ (n²+1)/2 (from ball 2), so label = (n²+1)/2. And it's at distance ≤ (n-1)/2 from both cell 1 and cell n².

This is consistent and doesn't give a contradiction. So the ball argument gives exactly B ≥ n+1 and no more.

But for n = 3, we showed B ≥ 5 > 4 = n+1. So there must be a different argument that gives a tighter bound.

Let me revisit the n = 3 case. The key was that cells 1 and 9 must be at distance ≥ 3 (no common neighbors), but the diameter is 2, so they must be at distance ≤ 2. Contradiction! So B = 4 is impossible.

Wait, that's the argument! For n = 3, diameter = 2, but we showed cells 1 and 9 must be at distance ≥ 3 (since their neighbor sets are disjoint). But distance ≥ 3 > diameter = 2 is impossible. So B = 4 doesn't work.

More generally, for any n, cells 1 and n² must be at distance d where the balls of radius ⌊d/2⌋ around them are disjoint. The balls are disjoint iff 2·⌊d/2⌋·B < n² - 1.

But also, d ≤ diameter = n-1 (for odd n). So we need 2·⌊(n-1)/2⌋·B ≥ n² - 1, i.e., (n-1)·B ≥ n² - 1, i.e., B ≥ (n²-1)/(n-1) = n+1.

This is the same bound. The n = 3 case is special because the diameter is exactly 2, and the "no common neighbors" constraint forces distance ≥ 3, which exceeds the diameter.

For n = 3: diameter = 2. Cells 1 and 9 at distance ≤ 2. If distance 1: diff = 8 > B. If distance 2: common neighbors exist, but neighbor sets are disjoint for B < 4 (since {2,...,B+1} ∩ {9-B,...,8} = {2,...,5} ∩ {5,...,8} = {5} for B=4, which has 1 element, but distance-2 pairs share 2 common neighbors). So for B = 4, we need 2 common neighbors but only 1 label is available. Contradiction.

For general n: the issue is more subtle. Let me think about whether the n+1 bound is tight for large n or if there's a better bound.

Actually, let me think about the n = 5 case to get more intuition. For n = 5, n+1 = 6. Is the bandwidth of C_5 × C_5 equal to 6, or is it larger?

The diameter of C_5 × C_5 is 4. Cells 1 and 25 must be at distance ≤ 4. For B = 6, neighbor sets of cells 1 and 25 are {2,...,7} and {19,...,24}, which are disjoint. So cells 1 and 25 have no common neighbors, distance ≥ 3.

At distance 3: balls of radius 1 around each are disjoint (verified). At distance 4: balls of radius 2 around each. Ball of radius 2 has 1 + 2·2·3 = 13 cells. Two such balls have 26 cells total, but torus has 25. So they overlap in at least 1 cell. The overlap cell has label ≤ 1 + 2·6 = 13 and ≥ 25 - 2·6 = 13. So label = 13. This is fine, no contradiction.

At distance 3: balls of radius 1 have 5 cells each, 10 total, no overlap needed. Fine.

So for n = 5, B = 6 might work. Let me try to construct a labeling.

Actually, let me think about this more carefully. For n = 5, can we achieve bandwidth 6?

Hmm, constructing such a labeling is non-trivial. Let me think about the general construction.

Let me consider the following approach. On the n×n torus (n odd), consider the labeling:

φ(x, y) = 1 + ((x + y·m) mod n) + n · ((y + x·k) mod n)

for suitable m, k. But this is complicated.

Let me try a different approach. Consider the "diagonal snake" construction.

On the n×n torus, consider the diagonals D_d = {(x, y) : x + y ≡ d (mod n)} for d = 0, 1, ..., n-1. Each diagonal has n cells. Cells in the same diagonal are connected by edges in the (1, -1) direction (which is NOT a grid edge). Grid edges connect cells in adjacent diagonals: (x, y) and (x+1, y) are in diagonals d and d+1; (x, y) and (x, y+1) are in diagonals d and d+1.

So the torus edges only connect adjacent diagonals (d to d+1 mod n). The diagonal D_d is an independent set (no two cells in the same diagonal are adjacent on the grid).

If we label all cells in D_0 first, then D_1, then ..., D_{n-1}, with labels 1 to n²:
- Edges between D_d and D_{d+1}: the label difference is at most 2n-1 (roughly, since D_d has labels in a block of n and D_{d+1} has labels in the next block of n).
- Edges between D_{n-1} and D_0 (wraparound): this is the problem. D_{n-1} has labels near n² and D_0 has labels near 1, so the difference is about n² - n, which is huge.

So the diagonal ordering has the same wraparound issue.

To fix the wraparound, we need to "interleave" the first and last diagonals somehow.

Alternative: instead of labeling diagonals in order 0, 1, 2, ..., n-1, label them in a different order that minimizes the maximum difference between consecutively-labeled diagonals that are adjacent on the torus.

But on the torus, D_d is adjacent to D_{d-1} and D_{d+1} for all d. So the "diagonal adjacency graph" is a cycle C_n. We need to label the n diagonals (each getting a block of n labels) such that adjacent diagonals in the cycle have close label blocks. This is the bandwidth problem on C_n with "block" labels.

The bandwidth of C_n is 2. So we can order the diagonals such that adjacent diagonals in the cycle have block indices differing by at most 2. Then the label difference between cells in adjacent diagonals is at most 2n + n - 1 = 3n - 1. That's better than n² but still not n+1.

Hmm, this approach gives 3n - 1, not n + 1. Let me think differently.

Let me go back to thinking about what the answer should be.

For n = 3: bandwidth = 5 = 2·3 - 1.
For n = 5: is it 6 = n+1 or 9 = 2n-1?

Let me try to construct a bandwidth-6 labeling for the 5×5 torus.

Actually, let me think about this more carefully using the structure of the problem.

Key idea: Consider the labeling as a bijection f: Z_n × Z_n → {0, 1, ..., n²-1}. We want |f(u) - f(v)| ≤ B for all adjacent u, v.

Equivalently, consider the "level sets" L_i = f^{-1}(i). The constraint is that adjacent cells have levels differing by at most B.

Think of it as: we're embedding the torus into a "line" (the ordering of labels) such that adjacent vertices on the torus are close on the line.

This is exactly the bandwidth problem. Let me look up the bandwidth of C_n × C_n.

I believe the bandwidth of the toroidal grid C_n × C_n is 2n for n even and 2n-1 for n odd. But I'm not sure. Let me try to verify with n = 3.

For n = 3: 2n - 1 = 5. We showed bandwidth = 5. ✓

Let me check if this is consistent with n = 4. For n = 4 (even), bandwidth would be 2n = 8. The 4×4 torus has 16 cells, diameter 4 (2⌊4/2⌋ = 4). Lower bound from path: (n²-1)/diameter = 15/4 = 3.75, so B ≥ 4. That's much less than 8. So if bandwidth is 8, the path bound
