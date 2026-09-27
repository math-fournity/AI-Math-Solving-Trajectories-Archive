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
  <problem_id>polymath_00347</problem_id>
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

7. Find the smallest natural number $n$, such that in any two-coloring of $K_{n}$ there exist 5 edge-disjoint monochromatic triangles.

## Standard Solution

Solution: $n_{\min }=11$.
(1) When $n \leqslant 10$. We can take a part or all of the following graph, where there do not exist 5 monochromatic triangles without common edges (solid lines represent red, no lines represent blue).
(2) When $n=11$, establish the following three lemmas:
Lemma 1: In a two-coloring of $K_{6}$, there must be two monochromatic triangles.

Lemma 2: In a two-coloring of $K_{7}$, there must be two monochromatic triangles without common edges.

Lemma 3: In a two-coloring of $K_{11}$, there must be two monochromatic triangles with exactly one common vertex.

Lemma 1 is a well-known structure. For the proof of Lemma 2, by Lemma 1, there are two monochromatic triangles. If they have no common edges, the lemma is proved. If they do, assume without loss of generality that $\triangle A_{1} A_{2} A_{3}$ and $\triangle A_{1} A_{2} A_{4}$ are both red triangles. Among them, there must be one different from $\triangle A_{2} A_{3} A_{4}$, which must be without common edges with $\triangle A_{1} A_{2} A_{3}$ or $\triangle A_{1} A_{2} A_{4}$ (drawing a diagram, it is somewhat complex).

Proof of Lemma 3: By Lemma 2, assume there exist monochromatic triangles $\triangle A_{1} A_{2} A_{3}$, $\triangle A_{4} A_{5} A_{6}$, $\triangle A_{7} A_{8} A_{9}$ (using proof by contradiction). Take 7 points $A_{1}, A_{2}, A_{3}, A_{4}, A_{7}, A_{10}, A_{11}$, among which there will be two monochromatic triangles without common edges and no common vertices. Among them, there must be one with a common vertex with $\triangle A_{1} A_{2} A_{3}$, $\triangle A_{4} A_{5} A_{6}$, or $\triangle A_{7} A_{8} A_{9}$, leading to a contradiction!

Next, we prove that $n=11$ satisfies the condition, using proof by contradiction, assume it does not hold.

First, by Lemma 3, we can assume $\triangle A_{1} A_{2} A_{3}$ and $\triangle A_{1} A_{4} A_{5}$ are monochromatic triangles.

Consider the 6 points $A_{6}, A_{7}, A_{8}, A_{9}, A_{10}, A_{11}$. If the edges between them are all the same color, then $\triangle A_{6} A_{7} A_{8}$, $\triangle A_{6} A_{10} A_{11}$, $\triangle A_{8} A_{9} A_{10}$, $\triangle A_{1} A_{2} A_{3}$, and $\triangle A_{1} A_{4} A_{5}$ are 5 monochromatic triangles without common edges, leading to a contradiction!

If there is a monochromatic triangle $T$ that has no common edges with $\triangle A_{1} A_{2} A_{3}$ and $\triangle A_{1} A_{4} A_{5}$, and shares a vertex with at least one of them, assume without loss of generality that $A_{2} \notin T$, $A_{4} \notin T$, $A_{6} \in T$. Consider the 7 points $A_{2}, A_{4}, A_{6}, A_{8}, A_{9}, A_{10}, A_{11}$, among which there are two monochromatic triangles without common edges (assume without loss of generality that $A_{8}, A_{9}, A_{10}, A_{11} \notin T$), leading to a contradiction!

By (1), assume the edges between $A_{6}, A_{7}, A_{8}, A_{9}$ are not all the same color. Among $A_{2}, A_{4}, A_{6}, A_{7}, A_{8}, A_{9}$, there are two monochromatic triangles, and these two triangles do not contain $A_{2}, A_{4}$. Assume without loss of generality that they are $\triangle A_{6} A_{8} A_{9}$ and $\triangle A_{7} A_{8} A_{9}$, and are red, then $A_{6} A_{7}$ is blue. Consider the 6 points $A_{2}, A_{4}, A_{6}, A_{7}, A_{k}, A_{i} (k=8,9; i=10,11)$. Similarly, we get: $A_{i} A_{k}, A_{i} A_{6}, A_{i} A_{7}$ are red.

Similarly, we get $A_{10} A_{11}$ is red. This way, between $A_{6}, A_{7}, A_{8}, A_{8}, A_{10}, A_{11}$, only $A_{6} A_{7}$ is blue. Consider $\triangle A_{1} A_{2} A_{3}$, $\triangle A_{1} A_{4} A_{5}$, $\triangle A_{7} A_{10} A_{11}$, $\triangle A_{8} A_{6} A_{11}$, $\triangle A_{8} A_{9} A_{10}$, a total of 5 monochromatic triangles, leading to a contradiction!
Thus, the assumption is false, $n=11$ satisfies the condition.
In conclusion, $n_{\min }=11$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully. We need to find the smallest natural number $n$ such that in any two-coloring of $K_n$, there exist 5 edge-disjoint monochromatic triangles.

First, let me check for answer leaks in the problem text. The problem is stated cleanly without any solutions or hints. No leak detected.

Now let me think about this problem. This is a Ramsey-type problem about edge-disjoint monochromatic triangles.

Let me think about the structure. We need 5 edge-disjoint monochromatic triangles. Each triangle uses 3 edges, so 5 edge-disjoint triangles use 15 edges total.

The total number of edges in $K_n$ is $\binom{n}{2} = \frac{n(n-1)}{2}$.

Let me think about known results. The classical Ramsey number $R(3,3) = 6$ means any two-coloring of $K_6$ has a monochromatic triangle.

For edge-disjoint monochromatic triangles, we need to find the smallest $n$ such that any two-coloring of $K_n$ contains 5 edge-disjoint monochromatic triangles.

Let me think about this more carefully. 

First, let me consider lower bounds. We need to find a two-coloring of $K_{n-1}$ that does NOT contain 5 edge-disjoint monochromatic triangles.

Let me think about the Turán-type approach. In a two-coloring, each color class is a graph on $n$ vertices. The monochromatic triangles are triangles in either color class.

Actually, let me think about this differently. Let me consider what's known about this type of problem.

For the problem of finding the minimum $n$ such that every 2-coloring of $K_n$ contains $k$ edge-disjoint monochromatic triangles, this is related to the "size Ramsey" or "edge-disjoint" Ramsey problems.

Let me think about small cases first.

For $k=1$: $R(3,3) = 6$, so $n = 6$.
For $k=2$: We need 2 edge-disjoint monochromatic triangles. 

Let me think about the general approach. 

In $K_n$, the total number of edges is $\binom{n}{2}$. Each monochromatic triangle uses 3 edges. If we want 5 edge-disjoint monochromatic triangles, we need at least 15 edges, so $\binom{n}{2} \geq 15$, giving $n \geq 6$ (since $\binom{6}{2} = 15$). But this is a very weak bound.

The key constraint is that the triangles must be monochromatic (all same color) and edge-disjoint.

Let me think about an upper bound approach. 

One approach: Use the fact that in any 2-coloring of $K_n$, there are many monochromatic triangles. The Goodman formula gives the minimum number of monochromatic triangles in a 2-coloring of $K_n$.

Goodman's theorem: The minimum number of monochromatic triangles in any 2-coloring of $K_n$ is:
- For even $n$: $\frac{n(n-2)(n-4)}{24}$
- For odd $n$: $\frac{n(n-1)(n-5)}{24}$

Wait, let me recall this more carefully. Goodman's formula says the minimum number of monochromatic triangles in a 2-coloring of $K_n$ is:

For $n$ even: $\frac{1}{4}\binom{n}{3} - \frac{n}{8}\binom{n/2}{2}$... hmm, let me think again.

Actually, Goodman's theorem states that the minimum number of monochromatic triangles in any 2-coloring of $K_n$ is:

$$M(n) = \begin{cases} \frac{n(n-2)(n-4)}{24} & \text{if } n \text{ is even} \\ \frac{(n-1)(n-3)(n-5)}{24} & \text{if } n \text{ is odd} \end{cases}$$

Wait, I'm not sure about the exact formula. Let me think about it differently.

Goodman (1959) proved that the minimum number of monochromatic triangles in any 2-coloring of $K_n$ is:

For $n$ even: $\frac{n}{4} \cdot \frac{(n-2)^2}{4} \cdot \frac{1}{3}$... I'm getting confused. Let me try to derive it.

Actually, the key result is: the minimum number of monochromatic triangles in any 2-coloring of $K_n$ is achieved by the "balanced" coloring (Turán-type), and equals:

$$M(n) = \binom{n}{3} - \frac{1}{2}\sum_v d_v(n-1-d_v)$$

where $d_v$ is the red degree of vertex $v$. This is minimized when the degrees are as balanced as possible.

For the balanced case where $n$ is even and each vertex has red degree $n/2$:
$$M(n) = \binom{n}{3} - \frac{1}{2} \cdot n \cdot \frac{n}{2} \cdot \frac{n}{2} = \frac{n(n-1)(n-2)}{6} - \frac{n^3}{8}$$

Hmm, let me be more careful. The number of non-monochromatic triangles (triangles with both colors) is:
$$\frac{1}{2}\sum_v d_v \cdot (n-1-d_v)$$

So the number of monochromatic triangles is:
$$\binom{n}{3} - \frac{1}{2}\sum_v d_v(n-1-d_v)$$

To minimize monochromatic triangles, we maximize $\sum_v d_v(n-1-d_v)$. This is maximized when each $d_v = (n-1)/2$.

For $n$ even, $n-1$ is odd, so the best we can do is $d_v \in \{(n-2)/2, n/2\}$, giving $d_v(n-1-d_v) = \frac{n-2}{2} \cdot \frac{n}{2} = \frac{n(n-2)}{4}$.

So $M(n) = \binom{n}{3} - \frac{n}{2} \cdot \frac{n(n-2)}{4} = \frac{n(n-1)(n-2)}{6} - \frac{n^2(n-2)}{8}$

$= \frac{n(n-2)}{2}\left(\frac{n-1}{3} - \frac{n}{4}\right) = \frac{n(n-2)}{2} \cdot \frac{4(n-1) - 3n}{12} = \frac{n(n-2)}{2} \cdot \frac{n-4}{12} = \frac{n(n-2)(n-4)}{24}$

For $n$ odd, $n-1$ is even, so $d_v = (n-1)/2$ exactly, giving $d_v(n-1-d_v) = \left(\frac{n-1}{2}\right)^2$.

$M(n) = \binom{n}{3} - \frac{n}{2} \cdot \left(\frac{n-1}{2}\right)^2 = \frac{n(n-1)(n-2)}{6} - \frac{n(n-1)^2}{8}$

$= \frac{n(n-1)}{2}\left(\frac{n-2}{3} - \frac{n-1}{4}\right) = \frac{n(n-1)}{2} \cdot \frac{4(n-2) - 3(n-1)}{12} = \frac{n(n-1)}{2} \cdot \frac{n-5}{12} = \frac{n(n-1)(n-5)}{24}$

So:
- $n$ even: $M(n) = \frac{n(n-2)(n-4)}{24}$
- $n$ odd: $M(n) = \frac{n(n-1)(n-5)}{24}$

Now, having many monochromatic triangles doesn't directly mean we can find 5 edge-disjoint ones. But it gives us a starting point.

Let me compute $M(n)$ for small values:
- $n=6$: $M(6) = \frac{6 \cdot 4 \cdot 2}{24} = 2$. So any 2-coloring of $K_6$ has at least 2 monochromatic triangles.
- $n=7$: $M(7) = \frac{7 \cdot 6 \cdot 2}{24} = \frac{84}{24} = 3.5$. So at least 4 monochromatic triangles (rounding up since it's an integer).

Wait, $M(7) = \frac{7 \cdot 6 \cdot 2}{24} = \frac{84}{24} = 3.5$. Since the number of monochromatic triangles is an integer, it must be at least 4. But actually, the formula gives the exact minimum, so let me check if it's really 3.5 or if I need to be more careful.

Hmm, actually for $n=7$ (odd), the formula gives $\frac{7 \cdot 6 \cdot 2}{24} = 3.5$. But the number of monochromatic triangles must be an integer. This suggests the formula might not be exactly right, or the minimum is actually 4 (achieved by some coloring), and the formula gives a lower bound that isn't always achieved.

Actually, I think the issue is that for $n$ odd, the formula $\frac{n(n-1)(n-5)}{24}$ might not always give an integer. Let me check: for $n=7$, $\frac{7 \cdot 6 \cdot 2}{24} = \frac{84}{24} = 3.5$. This is not an integer, so the actual minimum must be at least 4.

Let me reconsider. The formula gives the minimum when the coloring is "balanced" (each vertex has red degree $(n-1)/2$). For $n=7$, this means each vertex has red degree 3. The Paley tournament... no, we need a graph. 

Actually, for $n=7$, a balanced 2-coloring where each vertex has red degree 3 would be the complement of the Fano plane or something similar. Let me think...

A 3-regular graph on 7 vertices... but $7 \times 3 = 21$ which is odd, so no 3-regular graph on 7 vertices exists! So we can't have all vertices with degree exactly 3. Some must have degree 2 and some degree 4, or degree 3 and 4, etc.

So for $n=7$, the best we can do is have degrees as close to 3 as possible. With 7 vertices and total degree $2 \times 21 = 42$ (since $K_7$ has 21 edges, split into red and blue, total red degree + total blue degree = $7 \times 6 = 42$), if we want red degrees close to 3, we could have some vertices with red degree 3 and some with red degree 3... but $7 \times 3 = 21$ is odd, impossible. So we need some vertices with degree 2 and some with degree 4 (or other combinations).

If 3 vertices have red degree 2 and 4 have red degree 3: total = $6 + 12 = 18$, need 21. No.
If we have $k$ vertices with degree 2 and $7-k$ with degree 4: $2k + 4(7-k) = 28 - 2k = 21 \Rightarrow k = 3.5$. Not integer.

Hmm, let me think differently. We need $\sum d_v = 2|E_{red}|$. The number of red edges can be anything from 0 to 21. To balance, we want $|E_{red}| \approx 10.5$, so either 10 or 11.

If $|E_{red}| = 10$, $\sum d_v = 20$, average $20/7 \approx 2.86$.
If $|E_{red}| = 11$, $\sum d_v = 22$, average $22/7 \approx 3.14$.

For $|E_{red}| = 11$: degrees could be like 3,3,3,3,3,3,4 (sum = 22). Then:
$\sum d_v(6-d_v) = 6 \times 3 \times 3 + 1 \times 4 \times 2 = 54 + 8 = 62$.
Monochromatic triangles = $\binom{7}{3} - 62/2 = 35 - 31 = 4$.

For $|E_{red}| = 10$: degrees could be like 3,3,3,3,3,3,2 (sum = 20). Then:
$\sum d_v(6-d_v) = 6 \times 3 \times 3 + 1 \times 2 \times 4 = 54 + 8 = 62$.
Monochromatic triangles = $35 - 31 = 4$.

So the minimum for $n=7$ is 4 monochromatic triangles.

OK so let me tabulate:
- $n=6$: $M = 2$
- $n=7$: $M = 4$
- $n=8$: $M(8) = \frac{8 \cdot 6 \cdot 4}{24} = 8$
- $n=9$: $M(9) = \frac{9 \cdot 8 \cdot 4}{24} = 12$
- $n=10$: $M(10) = \frac{10 \cdot 8 \cdot 6}{24} = 20$
- $n=11$: $M(11) = \frac{11 \cdot 10 \cdot 6}{24} = \frac{660}{24} = 27.5$, so at least 28.

Hmm wait, for $n=11$, $\frac{11 \cdot 10 \cdot 6}{24} = \frac{660}{24} = 27.5$. Again not an integer. Let me check: $n=11$ is odd, so we need each vertex to have red degree 5. $11 \times 5 = 55$ is odd, so no 5-regular graph on 11 vertices. So again we can't achieve the balanced case exactly.

Let me reconsider. For $n$ odd, the formula $\frac{n(n-1)(n-5)}{24}$ might not be the exact minimum when it's not an integer. But it serves as a lower bound.

Anyway, the key question is: what is the minimum $n$ such that any 2-coloring of $K_n$ contains 5 edge-disjoint monochromatic triangles?

Having many monochromatic triangles is necessary but not sufficient. We need them to be edge-disjoint.

Let me think about this problem from a different angle. 

One approach is to use the following strategy: find a monochromatic triangle, remove its edges, and repeat. The question is whether we can always do this 5 times.

After removing edges of monochromatic triangles, the remaining graph is still 2-colored (with some edges removed). We need to find a monochromatic triangle in the remaining graph.

Actually, let me think about this more carefully. When we remove the edges of a monochromatic triangle, the remaining graph is a 2-coloring of a subgraph of $K_n$ (not necessarily complete). We need to find another monochromatic triangle in this remaining graph.

This is related to the concept of "Ramsey multiplicity" and "edge-disjoint Ramsey numbers."

Let me think about what's known. The problem of finding edge-disjoint monochromatic subgraphs is studied. For triangles specifically, I recall that the answer might be around $n = 11$ or $n = 12$ or so.

Let me try to work this out more carefully.

**Lower bound construction**: We need to find a 2-coloring of $K_{n-1}$ with at most 4 edge-disjoint monochromatic triangles (i.e., we can't find 5 edge-disjoint ones).

**Upper bound**: We need to show that any 2-coloring of $K_n$ has 5 edge-disjoint monochromatic triangles.

Let me think about the upper bound first. 

One useful tool: if we can find a monochromatic $K_6$, then by $R(3,3) = 6$, it contains a monochromatic triangle. But we need edge-disjoint ones.

Actually, let me think about a greedy approach. Suppose we have a 2-coloring of $K_n$. We find a monochromatic triangle, remove its 3 edges, and repeat. The question is: can we always do this 5 times?

After removing $k$ monochromatic triangles (using $3k$ edges), the remaining graph has $\binom{n}{2} - 3k$ edges. We need to find a monochromatic triangle in this remaining 2-colored graph.

The remaining graph is not complete, so we can't directly apply Ramsey theory. But we can think about it in terms of the original coloring.

Let me think about a different approach. Consider the following:

**Claim**: $n = 11$ works (any 2-coloring of $K_{11}$ has 5 edge-disjoint monochromatic triangles).

Or maybe $n = 12$? Let me think about what $n$ could be.

Actually, let me think about the problem more carefully using a counting argument.

In a 2-coloring of $K_n$, let $T$ be the total number of monochromatic triangles. Each edge is in at most $n-2$ monochromatic triangles (actually, an edge $uv$ is in at most $n-2$ triangles, but a monochromatic triangle containing $uv$ requires the third vertex $w$ such that $uw$ and $vw$ have the same color as $uv$).

If we want to find 5 edge-disjoint monochromatic triangles, we need to find a matching of size 5 in the "triangle-edge" hypergraph (where each triangle is a hyperedge consisting of its 3 edges).

By a greedy argument: if we have $T$ monochromatic triangles and each edge is in at most $D$ of them, then we can find at least $T / D$ edge-disjoint monochromatic triangles... no, that's not quite right. 

Actually, by a greedy argument: each time we pick a monochromatic triangle and remove it, we remove at most $3(n-2)$ other monochromatic triangles (those sharing an edge with the picked one). So we can find at least $T / (3(n-2) + 1)$ edge-disjoint monochromatic triangles.

Wait, more carefully: when we pick a monochromatic triangle, we remove it and all monochromatic triangles sharing an edge with it. Each edge of the picked triangle is in at most $n-2$ monochromatic triangles. So the number of monochromatic triangles removed is at most $1 + 3(n-2) = 3n - 5$. By the greedy algorithm, we can find at least $\lceil T / (3n-5) \rceil$ edge-disjoint monochromatic triangles.

For this to be $\geq 5$, we need $T \geq 5(3n-5) + 1 = 15n - 24$.

Hmm, but this is a very rough bound. Let me see what $n$ gives $M(n) \geq 15n - 24$.

For $n$ even: $\frac{n(n-2)(n-4)}{24} \geq 15n - 24$
$n(n-2)(n-4) \geq 24(15n - 24) = 360n - 576$
$n(n-2)(n-4) \geq 360n - 576$

For $n = 20$: $20 \cdot 18 \cdot 16 = 5760 \geq 7200 - 576 = 6624$. No, $5760 < 6624$.
For $n = 22$: $22 \cdot 20 \cdot 18 = 7920 \geq 7920 - 576 = 7344$. Yes, $7920 \geq 7344$.

So this very rough bound gives $n \leq 22$ or so. But this is way too loose.

Let me think about a better approach. 

Actually, let me think about this problem differently. Let me consider the structure of 2-colorings that minimize the number of edge-disjoint monochromatic triangles.

A key observation: in the "balanced" 2-coloring (which minimizes total monochromatic triangles), the coloring is close to a random coloring or a structured coloring like the Paley graph.

Let me think about specific constructions for lower bounds.

**Construction 1: Two cliques.** Split the vertices into two groups of sizes $\lfloor n/2 \rfloor$ and $\lceil n/2 \rceil$. Color edges within each group red and edges between groups blue. Then:
- Red triangles: $\binom{\lfloor n/2 \rfloor}{3} + \binom{\lceil n/2 \rceil}{3}$
- Blue triangles: 0 (the blue graph is bipartite)

All monochromatic triangles are red, and they're in two disjoint cliques. The edge-disjoint monochromatic triangles are edge-disjoint triangles in $K_{\lfloor n/2 \rfloor}$ and $K_{\lceil n/2 \rceil}$.

The maximum number of edge-disjoint triangles in $K_m$ is $\lfloor \binom{m}{2}/3 \rfloor = \lfloor m(m-1)/6 \rfloor$.

For $n = 10$: groups of 5 and 5. Edge-disjoint triangles in $K_5$: $\lfloor 10/3 \rfloor = 3$. Total: $3 + 3 = 6 \geq 5$. So this construction gives 6 edge-disjoint monochromatic triangles for $n = 10$.

For $n = 9$: groups of 4 and 5. Edge-disjoint triangles in $K_4$: $\lfloor 6/3 \rfloor = 2$. In $K_5$: $\lfloor 10/3 \rfloor = 3$. Total: $2 + 3 = 5 \geq 5$. So this gives 5 for $n = 9$.

For $n = 8$: groups of 4 and 4. Edge-disjoint triangles in $K_4$: $\lfloor 6/3 \rfloor = 2$. Total: $2 + 2 = 4 < 5$. So this construction gives only 4 edge-disjoint monochromatic triangles for $n = 8$.

So the "two cliques" construction shows that $n = 8$ doesn't work (we have a coloring with only 4 edge-disjoint monochromatic triangles). But we need to check if there's a better coloring for $n = 8$ that also has at most 4.

Wait, but we need to check ALL colorings of $K_8$, not just this one. The question is whether EVERY 2-coloring of $K_8$ has 5 edge-disjoint monochromatic triangles. The "two cliques" construction shows one that doesn't, so $n > 8$.

For $n = 9$: the "two cliques" construction gives exactly 5. But we need to check if EVERY 2-coloring of $K_9$ has at least 5. Maybe there's another coloring of $K_9$ with fewer?

Hmm, let me think about other constructions.

**Construction 2: Complete bipartite + complete bipartite.** Actually, this is the same as construction 1 with colors swapped.

**Construction 3: Paley-type or algebraic colorings.** These might give fewer monochromatic triangles but the triangles might be more spread out.

Let me think about $n = 9$ more carefully. We need to check if there's a 2-coloring of $K_9$ with at most 4 edge-disjoint monochromatic triangles.

$K_9$ has $\binom{9}{2} = 36$ edges. Five edge-disjoint triangles use 15 edges. So we need 15 edges to form 5 monochromatic triangles.

The minimum number of monochromatic triangles in $K_9$ is $M(9) = 12$. So there are at least 12 monochromatic triangles. Can we always find 5 edge-disjoint ones among 12+ monochromatic triangles?

Each edge is in at most $n - 2 = 7$ monochromatic triangles. By the greedy argument, we can find at least $\lceil 12 / (3 \cdot 7 + 1) \rceil = \lceil 12/22 \rceil = 1$. That's useless.

Let me think more carefully. The issue is that the greedy bound is very loose. Let me think about the actual structure.

Actually, let me think about this problem from the perspective of known results. This is a competition problem (problem 7), so the answer should be a specific small number.

Let me think about what constructions give lower bounds and what arguments give upper bounds.

**Lower bound (showing $n$ must be at least some value):**
- Two cliques construction: $n = 8$ gives only 4 edge-disjoint monochromatic triangles. So $n \geq 9$.

Can we do better? Is there a coloring of $K_9$ with at most 4 edge-disjoint monochromatic triangles?

Let me think about the "two cliques" coloring for $n = 9$: split into 4 and 5, red within, blue between. Red triangles: $\binom{4}{3} + \binom{5}{3} = 4 + 10 = 14$. Blue triangles: 0. Edge-disjoint red triangles: in $K_4$, we can find 2 edge-disjoint triangles (using all 6 edges). In $K_5$, we can find 3 edge-disjoint triangles (using 9 of 10 edges). Total: 5.

But what if we use a different split or different coloring?

**Alternative for $n = 9$:** Split into 3, 3, 3. Color within each group red, between groups blue. Red triangles: $3 \times 1 = 3$. Blue triangles: 0 (blue is tripartite, which is 3-colorable, so no blue triangles... wait, tripartite graphs can have triangles? No! A tripartite graph has no triangles because a triangle would need 3 vertices all in different parts, but edges only go between parts, so a triangle $abc$ with $a$ in part 1, $b$ in part 2, $c$ in part 3 would need edges $ab$, $bc$, $ac$, all of which are between parts, so yes, this IS a triangle in the blue graph!

Wait, I need to be more careful. If we split into 3 groups of 3 and color edges within groups red and between groups blue, then the blue graph is the complete tripartite graph $K_{3,3,3}$. This graph DOES have triangles: pick one vertex from each part, and all three edges are blue. So blue triangles: $3 \times 3 \times 3 = 27$.

Red triangles: $3 \times \binom{3}{3} = 3$.

Total monochromatic triangles: 30. But how many edge-disjoint ones can we find?

Blue triangles in $K_{3,3,3}$: Each blue triangle uses one vertex from each part. The blue graph has $3 \times 3 \times 3 = 27$ edges between each pair of parts... wait, no. $K_{3,3,3}$ has edges between each pair of parts: $3 \times 3 = 9$ edges for each pair, and 3 pairs, so $27$ blue edges total.

Each blue triangle uses 3 blue edges (one from each pair of parts). The maximum number of edge-disjoint blue triangles is at most $27/3 = 9$. Can we achieve this? Yes, by a Latin square argument: we can decompose $K_{3,3,3}$ into 9 edge-disjoint triangles (this is related to the fact that $K_{n,n,n}$ can be decomposed into $n^2$ triangles when $n$ is... well, for $n=3$, we get 9 triangles).

So this construction gives 9 edge-disjoint monochromatic triangles, which is way more than 5. Not useful for a lower bound.

Let me go back to the two-cliques construction. For $n = 9$, it gives exactly 5. Can we find a coloring of $K_9$ with fewer than 5 edge-disjoint monochromatic triangles?

Let me think about other colorings of $K_9$.

**Coloring with a bipartite blue graph and structured red graph:**

What if the blue graph is bipartite (no blue triangles) and the red graph is designed to have few edge-disjoint triangles?

If blue is bipartite with parts of size $a$ and $b$ ($a + b = 9$), then red consists of $K_a$ and $K_b$ (edges within each part). Red triangles: $\binom{a}{3} + \binom{b}{3}$. Edge-disjoint red triangles: $\lfloor \binom{a}{2}/3 \rfloor + \lfloor \binom{b}{2}/3 \rfloor$ (approximately, since we can decompose cliques into edge-disjoint triangles).

Wait, can we always decompose $K_m$ into $\lfloor \binom{m}{2}/3 \rfloor$ edge-disjoint triangles? 

$K_m$ has $\binom{m}{2} = m(m-1)/2$ edges. Each triangle uses 3 edges. So the maximum number of edge-disjoint triangles is $\lfloor m(m-1)/6 \rfloor$.

For $K_4$: $4 \times 3 / 6 = 2$. $K_4$ has 6 edges, and we can find 2 edge-disjoint triangles (e.g., $\{1,2,3\}$ and $\{1,2,4\}$... no, those share edge 12. Let me think. $\{1,2,3\}$ and $\{1,4,? \}$... $K_4$ has triangles: 123, 124, 134, 234. Edge-disjoint pairs: 123 and 124 share edge 12. 123 and 134 share edge 13. 123 and 234 share edge 23. 124 and 134 share edge 14. 124 and 234 share edge 24. 134 and 234 share edge 34. So no two triangles in $K_4$ are edge-disjoint! 

Wait, that can't be right. $K_4$ has 6 edges and each triangle has 3 edges. Two edge-disjoint triangles would use 6 edges, covering all edges. But in $K_4$, every pair of triangles shares at least one edge. Let me verify: triangles in $K_4$ are $\{1,2,3\}, \{1,2,4\}, \{1,3,4\}, \{2,3,4\}$. 

$\{1,2,3\}$ has edges 12, 13, 23.
$\{2,3,4\}$ has edges 23, 24, 34.
These share edge 23. Not edge-disjoint.

$\{1,2,3\}$ has edges 12, 13, 23.
$\{1,3,4\}$ has edges 13, 14, 34.
Share edge 13.

In fact, in $K_4$, any two triangles share exactly one edge (since any two 3-element subsets of a 4-element set share exactly 2 elements, hence one edge). So the maximum number of edge-disjoint triangles in $K_4$ is 1, not 2!

This changes my calculation. Let me reconsider.

For $K_m$, the maximum number of edge-disjoint triangles is related to the "triangle packing" number. 

For $K_5$: 10 edges. Can we find 3 edge-disjoint triangles (using 9 edges)? Triangles in $K_5$: $\binom{5}{3} = 10$. Let's try: $\{1,2,3\}$ (edges 12,13,23), $\{1,4,5\}$ (edges 14,15,45), $\{2,4,? \}$... we need a triangle using only remaining edges. Remaining edges: 24, 25, 34, 35. Is there a triangle? $\{2,4,5\}$ needs 24, 25, 45 - but 45 is used. $\{3,4,5\}$ needs 34, 35, 45 - 45 used. $\{2,3,4\}$ needs 23 - used. $\{2,3,5\}$ needs 23 - used. So with $\{1,2,3\}$ and $\{1,4,5\}$, we can't find a third edge-disjoint triangle.

Try: $\{1,2,3\}$, $\{3,4,5\}$, $\{1,4,? \}$... remaining edges after 123 and 345: 14, 15, 24, 25, 45... wait, 345 uses 34, 35, 45. So remaining: 12, 13, 23 are used by 123; 34, 35, 45 used by 345. Remaining: 14, 15, 24, 25. No triangle possible (need 3 edges forming a triangle, but we only have 4 edges and they form a 4-cycle 1-4-2-5-1... actually 14, 24, 25, 15 form a 4-cycle 1-4-2-5-1, no triangle).

Try: $\{1,2,4\}$, $\{2,3,5\}$, $\{1,3,? \}$... 124 uses 12, 14, 24. 235 uses 23, 25, 35. Remaining: 13, 15, 34, 45. Triangle? $\{1,3,4\}$ needs 13, 34, 14 - 14 used. $\{1,3,5\}$ needs 13, 35, 15 - 35 used. $\{3,4,5\}$ needs 34, 45, 35 - 35 used. $\{1,4,5\}$ needs 14, 45, 15 - 14 used. No triangle.

Try: $\{1,2,5\}$, $\{2,3,4\}$, ... 125 uses 12, 15, 25. 234 uses 23, 24, 34. Remaining: 13, 14, 35, 45. Triangle? $\{1,3,5\}$ needs 13, 35, 15 - 15 used. $\{1,4,5\}$ needs 14, 45, 15 - 15 used. $\{3,4,5\}$ needs 34, 45, 35 - 34 used. $\{1,3,4\}$ needs 13, 34, 14 - 34 used. No.

Hmm, it seems like we can only find 2 edge-disjoint triangles in $K_5$. Let me verify: $K_5$ has 10 edges. 3 edge-disjoint triangles would use 9 edges, leaving 1 edge. Is this possible?

Actually, I recall that $K_5$ can be decomposed into 2 edge-disjoint 5-cycles (the Petersen graph decomposition), but not into triangles. The maximum number of edge-disjoint triangles in $K_5$ is 2 (using 6 of 10 edges).

Wait, but I showed above that we can find 2 edge-disjoint triangles. Can we find 3? We need 3 triangles using 9 distinct edges out of 10. Each vertex in $K_5$ has degree 4. In 3 edge-disjoint triangles, each vertex is in at most... well, each vertex has degree 4, and each triangle containing a vertex uses 2 of its edges. So each vertex can be in at most 2 triangles. With 5 vertices and 3 triangles (9 vertex-triangle incidences), by pigeonhole some vertex is in at least 2 triangles. That's fine. But each vertex in 2 triangles uses 4 edges, which is all its edges. So a vertex in 2 triangles has all its edges used.

If vertex $v$ is in 2 triangles, those 2 triangles use all 4 edges of $v$, so $v$ can't be in any more triangles. The 2 triangles containing $v$ use 3+3-1 = 5 edges (they share edge through $v$... no, they share vertex $v$ but the triangles are $\{v, a, b\}$ and $\{v, c, d\}$, using edges $va, vb, ab, vc, vd, cd$ = 6 edges. These 6 edges involve all 4 neighbors of $v$ and all 4 edges of $v$.

Now we need a third triangle from the remaining 4 edges. The remaining edges are those not involving $v$ and not $ab$ or $cd$. The remaining edges are: $ac, ad, bc, bd$ (the edges between $\{a,b\}$ and $\{c,d\}$). These form a 4-cycle $a-c-b-d-a$ (or $a-d-b-c-a$). No triangle. So we can't find 3 edge-disjoint triangles in $K_5$.

So the maximum number of edge-disjoint triangles in $K_5$ is 2.

Wait, but what if the two triangles containing $v$ share an edge? Like $\{v, a, b\}$ and $\{v, a, c\}$? Then they share edge $va$, so they're not edge-disjoint. So for edge-disjoint triangles, the two triangles containing $v$ must be $\{v, a, b\}$ and $\{v, c, d\}$ with $\{a,b\} \cap \{c,d\} = \emptyset$.

OK so for $K_5$, max edge-disjoint triangles = 2.

Let me redo the table for max edge-disjoint triangles in $K_m$:
- $K_3$: 1 (3 edges, 1 triangle)
- $K_4$: 1 (6 edges, but any two triangles share an edge)
- $K_5$: 2 (10 edges, can find 2 edge-disjoint, can't find 3 as shown)
- $K_6$: ? (15 edges, max would be 5 if we can decompose into 5 triangles)

For $K_6$: Can we decompose $K_6$ into 5 edge-disjoint triangles? $K_6$ has 15 edges, 5 triangles use 15 edges. This is a triangle decomposition of $K_6$. It's known that $K_n$ can be decomposed into triangles if and only if $n \equiv 1$ or $3 \pmod{6}$. $6 \equiv 0 \pmod{6}$, so $K_6$ CANNOT be decomposed into triangles. The maximum number of edge-disjoint triangles in $K_6$ is 4 (using 12 of 15 edges).

Actually, let me verify. The condition for triangle decomposition of $K_n$ is $n \equiv 1 \pmod{6}$ or $n \equiv 3 \pmod{6}$ (i.e., $n$ is odd and $3 | \binom{n}{2}$, which means $n \equiv 1$ or $3 \pmod 6$).

For $K_6$: $6 \equiv 0 \pmod 6$, so no triangle decomposition. Max edge-disjoint triangles: $\lfloor 15/3 \rfloor = 5$ is the upper bound, but since we can't decompose, it's at most 4. Can we achieve 4? 4 triangles use 12 edges, leaving 3 edges. Let me try:

$K_6$ vertices: 1,2,3,4,5,6.
Triangles: $\{1,2,3\}$ (12,13,23), $\{1,4,5\}$ (14,15,45), $\{2,4,6\}$ (24,26,46), $\{3,5,6\}$ (35,36,56).
Used edges: 12,13,23,14,15,45,24,26,46,35,36,56 = 12 edges.
Remaining: 16,25,34. These form a matching, not a triangle. So 4 edge-disjoint triangles. ✓

Can we get 5? We'd need to use all 15 edges. But $K_6$ can't be decomposed into triangles (since $6 \not\equiv 1,3 \pmod 6$). So max is 4.

Now let me redo the two-cliques construction:
- $n = 8$: split 4+4. Red: $K_4 \cup K_4$. Edge-disjoint red triangles: 1 + 1 = 2. Blue: $K_{4,4}$, bipartite, no blue triangles. Total: 2.

Wait, that's only 2, not 4 as I said before. Let me reconsider.

Hmm, I think I was wrong earlier. Let me recompute.

For the two-cliques construction with $n = 8$, split into 4 and 4:
- Red graph: $K_4 \cup K_4$ (two disjoint $K_4$'s)
- Blue graph: $K_{4,4}$ (complete bipartite)
- Red triangles: $\binom{4}{3} + \binom{4}{3} = 4 + 4 = 8$
- Blue triangles: 0
- Edge-disjoint red triangles: max 1 in each $K_4$, so total 2.

So this gives only 2 edge-disjoint monochromatic triangles. That's even less than 5.

But wait, we can also consider non-clique-based colorings. The two-cliques construction is just one example. We need to find the coloring that MINIMIZES edge-disjoint monochromatic triangles.

Actually, for the lower bound, we just need ONE coloring with fewer than 5 edge-disjoint monochromatic triangles. The two-cliques construction for $n = 8$ gives only 2, so $n \geq 9$.

But can we find a coloring of $K_9$ with fewer than 5? Let me check the two-cliques for $n = 9$:
- Split 4+5: Red: $K_4 \cup K_5$. Edge-disjoint red triangles: 1 + 2 = 3. Blue: $K_{4,5}$, no blue triangles. Total: 3.

So for $n = 9$, the two-cliques construction gives only 3 edge-disjoint monochromatic triangles! That's less than 5.

For $n = 10$: Split 5+5. Red: $K_5 \cup K_5$. Edge-disjoint: 2 + 2 = 4. Still less than 5.

For $n = 11$: Split 5+6. Red: $K_5 \cup K_6$. Edge-disjoint: 2 + 4 = 6. That's ≥ 5.

But wait, for $n = 11$, can we find a different coloring with fewer than 5?

Split 4+7: Red: $K_4 \cup K_7$. Edge-disjoint: 1 + ? in $K_7$. $K_7$ has 21 edges. $7 \equiv 1 \pmod 6$, so $K_7$ CAN be decomposed into triangles! $21/3 = 7$ triangles. So edge-disjoint: 1 + 7 = 8. That's more.

Split 3+8: Red: $K_3 \cup K_8$. $K_3$: 1 triangle. $K_8$: 28 edges. $8 \equiv 2 \pmod 6$, can't decompose. Max edge-disjoint: $\lfloor 28/3 \rfloor = 9$. So 1 + 9 = 10.

Split 5+6: 2 + 4 = 6.

So for $n = 11$, the two-cliques construction gives at least 6 (with the 5+6 split). But maybe there's a different coloring?

What about a 3-partite blue graph? Split into 3 groups, blue between groups, red within.

For $n = 11$, split 4+4+3: Red: $K_4 \cup K_4 \cup K_3$. Edge-disjoint red: 1 + 1 + 1 = 3. Blue: $K_{4,4,3}$ (complete tripartite). Blue triangles: $4 \times 4 \times 3 = 48$. How many edge-disjoint blue triangles?

$K_{4,4,3}$ has edges: $4 \times 4 + 4 \times 3 + 4 \times 3 = 16 + 12 + 12 = 40$ blue edges. Each blue triangle uses 3 edges. Max edge-disjoint: $\lfloor 40/3 \rfloor = 13$. But can we achieve this?

Actually, for complete tripartite $K_{a,b,c}$, the maximum number of edge-disjoint triangles is a well-studied problem. Each triangle uses one vertex from each part. The number of edge-disjoint triangles is limited by the edges between each pair of parts: $ab$, $ac$, $bc$. Each triangle uses one edge from each pair, so the max is $\min(ab, ac, bc)$. For $K_{4,4,3}$: $\min(16, 12, 12) = 12$. And we can achieve 12 by a Latin-square-type argument.

So total edge-disjoint monochromatic: 3 (red) + 12 (blue) = 15. Way more than 5.

Hmm, so the tripartite construction gives many more. The two-cliques (bipartite) construction seems to minimize.

Let me reconsider. For the two-cliques construction, the blue graph is bipartite (no blue triangles), and all monochromatic triangles are red, confined to two cliques. The number of edge-disjoint monochromatic triangles is the sum of edge-disjoint triangles in each clique.

For general $n$ with split $a + b$ ($a \leq b$, $a + b = n$):
- Edge-disjoint monochromatic triangles = $\text{pack}(K_a) + \text{pack}(K_b)$

where $\text{pack}(K_m)$ is the maximum number of edge-disjoint triangles in $K_m$.

Let me compute $\text{pack}(K_m)$ for small $m$:
- $K_1, K_2$: 0
- $K_3$: 1
- $K_4$: 1
- $K_5$: 2
- $K_6$: 4
- $K_7$: 7 (decomposition exists since $7 \equiv 1 \pmod 6$)
- $K_8$: ? $8 \equiv 2 \pmod 6$. $\lfloor 28/3 \rfloor = 9$. But can we achieve 9? 9 triangles use 27 of 28 edges. The remaining edge is a single edge. I think this is possible. Actually, the maximum packing of $K_n$ for $n \equiv 2 \pmod 6$ is $\lfloor \binom{n}{2}/3 \rfloor - 1$... no, let me think again.

The maximum number of edge-disjoint triangles in $K_n$ (the "triangle packing number") is:
- $\lfloor \binom{n}{2}/3 \rfloor$ if $n \not\equiv 5 \pmod 6$... 

Actually, I recall that the maximum triangle packing of $K_n$ is:
$$\text{pack}(K_n) = \begin{cases} \frac{n(n-1)}{6} & \text{if } n \equiv 1, 3 \pmod{6} \\ \frac{n(n-1)}{6} - 1 & \text{if } n \equiv 0, 2 \pmod{6} \\ \frac{n(n-1)-2}{6} & \text{if } n \equiv 4, 5 \pmod{6} \end{cases}$$

Hmm, I'm not sure about the exact formula. Let me think about it differently.

The maximum number of edge-disjoint triangles in $K_n$ is $\lfloor \frac{n}{3} \lfloor \frac{n-1}{2} \rfloor \rfloor$... no, that's not right either.

Let me just compute for small cases:
- $K_3$: 1 (decomposition: 1 triangle)
- $K_4$: 1 (can't do 2 since any two triangles share an edge)
- $K_5$: 2 (shown above)
- $K_6$: 4 (shown above, can't do 5 since $6 \not\equiv 1,3 \pmod 6$)
- $K_7$: 7 (decomposition exists, $7 \equiv 1 \pmod 6$, $21/3 = 7$)

For $K_6$: $\lfloor 15/3 \rfloor = 5$, but we showed max is 4. So the formula isn't just $\lfloor \binom{n}{2}/3 \rfloor$.

The issue is that for triangle decomposition to exist, we need $n \equiv 1$ or $3 \pmod 6$. For other values, we lose at least 1 triangle.

For $K_6$ ($n \equiv 0 \pmod 6$): max = 4 = $\lfloor 15/3 \rfloor - 1 = 5 - 1$.
For $K_5$ ($n \equiv 5 \pmod 6$): max = 2 = $\lfloor 10/3 \rfloor - 1 = 3 - 1$.
For $K_4$ ($n \equiv 4 \pmod 6$): max = 1 = $\lfloor 6/3 \rfloor - 1 = 2 - 1$.

So it seems like for $n \not\equiv 1, 3 \pmod 6$, the max is $\lfloor \binom{n}{2}/3 \rfloor - 1$.

Let me verify for $K_8$ ($n \equiv 2 \pmod 6$): $\lfloor 28/3 \rfloor - 1 = 9 - 1 = 8$. Is this correct? 8 triangles use 24 of 28 edges, leaving 4 edges. I believe this is achievable.

For $K_9$ ($n \equiv 3 \pmod 6$): decomposition exists, $36/3 = 12$.
For $K_{10}$ ($n \equiv 4 \pmod 6$): $\lfloor 45/3 \rfloor - 1 = 15 - 1 = 14$.
For $K_{11}$ ($n \equiv 5 \pmod 6$): $\lfloor 55/3 \rfloor - 1 = 18 - 1 = 17$.
For $K_{12}$ ($n \equiv 0 \pmod 6$): $\lfloor 66/3 \rfloor - 1 = 22 - 1 = 21$.

OK so now let me redo the two-cliques construction:
- $n = 9$, split 4+5: pack($K_4$) + pack($K_5$) = 1 + 2 = 3.
- $n = 10$, split 5+5: 2 + 2 = 4.
- $n = 10$, split 4+6: 1 + 4 = 5.
- $n = 11$, split 5+6: 2 + 4 = 6.
- $n = 11$, split 4+7: 1 + 7 = 8.

So for $n = 10$, the split 5+5 gives only 4 edge-disjoint monochromatic triangles. So $n \geq 11$.

For $n = 11$, the minimum over all splits is... let's check all:
- 1+10: 0 + 14 = 14
- 2+9: 0 + 12 = 12
- 3+8: 1 + 8 = 9
- 4+7: 1 + 7 = 8
- 5+6: 2 + 4 = 6

So the two-cliques construction for $n = 11$ gives at least 6 (with the 5+6 split). But is 6 ≥ 5? Yes! So this construction doesn't give a lower bound less than 5 for $n = 11$.

But wait, we need to check if there's a DIFFERENT coloring of $K_{11}$ (not the two-cliques) that gives fewer than 5 edge-disjoint monochromatic triangles.

Hmm, this is getting complicated. Let me think about whether there are other constructions.

**Other constructions:**

What about a coloring where both colors have triangles, but they're arranged to minimize edge-disjoint packing?

For example, consider a coloring based on a 5-cycle structure. Or a coloring where one color is a sparse graph with few triangles.

Actually, let me think about this differently. The two-cliques construction minimizes the total number of monochromatic triangles (it's the Goodman extremal coloring). But maybe a different coloring has more total monochromatic triangles but fewer edge-disjoint ones.

Hmm, actually the two-cliques construction doesn't necessarily minimize total monochromatic triangles. The Goodman extremal coloring is the one where each vertex has degree as close to $(n-1)/2$ as possible, which for even $n$ is the "half graph" or a specific balanced coloring.

Wait, the two-cliques construction (split into two equal halves, red within, blue between) IS the Goodman extremal for even $n$. For this coloring, each vertex has red degree $n/2 - 1$ (within its clique) and blue degree $n/2$ (to the other clique). So the red degree is $n/2 - 1$ and blue degree is $n/2$, total $n - 1$. The Goodman formula is about $d_v(n-1-d_v)$ which is $(n/2-1)(n/2) = n(n-2)/4$ for each vertex. This matches the balanced case.

But for odd $n$, the two-cliques with split $\lfloor n/2 \rfloor + \lceil n/2 \rceil$ gives red degrees of $\lfloor n/2 \rfloor - 1$ and $\lceil n/2 \rceil - 1$, which are $(n-3)/2$ and $(n-1)/2$. The Goodman formula for odd $n$ requires all degrees to be $(n-1)/2$, which is achieved by a different coloring (not two-cliques).

So for odd $n$, the Goodman extremal coloring is NOT the two-cliques. It's a more balanced coloring where each vertex has red degree $(n-1)/2$.

Let me think about what the Goodman extremal coloring looks like for odd $n$. For $n = 9$, each vertex has red degree 4. This is a 4-regular graph on 9 vertices. An example is the Paley graph on 9 vertices (if it exists) or some other 4-regular graph.

Actually, the Paley graph on 9 vertices: $9 = 3^2$, and the Paley graph is defined for prime powers $q \equiv 1 \pmod 4$. $9 \equiv 1 \pmod 4$, so the Paley graph on 9 vertices exists. It's a 4-regular graph on 9 vertices.

The Paley graph on 9 vertices is actually the $3 \times 3$ rook's graph (or something related). Let me think... The Paley graph on $q$ vertices connects $i$ and $j$ if $i - j$ is a quadratic residue mod $q$. For $q = 9$, the quadratic residues mod 9 are $\{0, 1, 4, 7\}$ (since $1^2 = 1, 2^2 = 4, 3^2 = 0, 4^2 = 7, 5^2 = 7, 6^2 = 0, 7^2 = 4, 8^2 = 1 \pmod 9$). So the quadratic residues are $\{1, 4, 7\}$ (excluding 0). Each vertex has 4 neighbors (since $q - 1 = 8$ and half are residues, but actually for $q = 9$, the multiplicative group has order 8, and the quadratic residues form a subgroup of order 4: $\{1, 4, 7, ...\}$... hmm, this is getting complicated with non-prime moduli).

Let me not worry about the exact structure and instead think about the problem more abstractly.

For the Goodman extremal coloring of $K_9$ (4-regular red graph), the number of monochromatic triangles is $M(9) = 12$. These 12 triangles are split between red and blue. How many edge-disjoint ones can we find?

This is hard to determine without knowing the specific structure. But the key question is: can we find a coloring of $K_9$ (or $K_{10}$, $K_{11}$, etc.) with fewer than 5 edge-disjoint monochromatic triangles?

Let me think about this more carefully. 

Actually, let me reconsider the problem. The two-cliques construction for $n = 10$ (split 5+5) gives 4 edge-disjoint monochromatic triangles. This shows $n \geq 11$.

Now, can we find a coloring of $K_{11}$ with fewer than 5 edge-disjoint monochromatic triangles?

The two-cliques for $n = 11$ (split 5+6) gives 6. But maybe a different coloring gives fewer?

Let me think about a 3-coloring based construction. What if we use a 3-partition?

For $n = 11$, split into 4+4+3, color within parts red, between parts blue. Red: $K_4 \cup K_4 \cup K_3$. Edge-disjoint red: 1 + 1 + 1 = 3. Blue: $K_{4,4,3}$. Blue triangles: $4 \cdot 4 \cdot 3 = 48$. Edge-disjoint blue: $\min(16, 12, 12) = 12$ (achievable). Total: 3 + 12 = 15.

That's way more than 5. The tripartite construction gives too many blue triangles.

What about a different approach? What if we use a coloring where one color has very few triangles?

The minimum number of triangles in a graph with $m$ edges on $n$ vertices is 0 (if the graph is triangle-free). A triangle-free graph on $n$ vertices has at most $\lfloor n^2/4 \rfloor$ edges (Turán's theorem / Mantel's theorem).

So if we make the red graph triangle-free (bipartite), it has at most $\lfloor n^2/4 \rfloor$ edges, and the blue graph has the remaining $\binom{n}{2} - \lfloor n^2/4 \rfloor$ edges. The blue graph is the complement of a bipartite graph, which is two cliques (plus possible edges between them if the bipartite graph isn't complete bipartite).

Wait, if the red graph is bipartite with parts $A$ and $B$, then the blue graph has all edges within $A$ and within $B$ (forming $K_{|A|}$ and $K_{|B|}$), plus possibly some edges between $A$ and $B$ (those not in the red graph). If the red graph is complete bipartite $K_{|A|,|B|}$, then the blue graph is exactly $K_{|A|} \cup K_{|B|}$, which is the two-cliques construction.

If the red graph is a non-complete bipartite graph, then the blue graph has some edges between $A$ and $B$ as well, which could create additional blue triangles. So the two-cliques construction (complete bipartite red) minimizes blue triangles when red is bipartite.

So among all colorings where one color is triangle-free, the two-cliques construction minimizes edge-disjoint monochromatic triangles.

But what if both colors have triangles? Could that lead to fewer edge-disjoint monochromatic triangles?

Intuitively, having triangles in both colors gives more total monochromatic triangles, which should make it easier to find edge-disjoint ones. But it's conceivable that the triangles overlap more.

Let me think about a specific example. Consider $n = 11$ with a coloring that's "almost" two-cliques but with a few edges flipped.

Start with split 5+6 (red within, blue between). This gives 6 edge-disjoint monochromatic triangles (2 from $K_5$, 4 from $K_6$). Now flip one edge from red to blue (say an edge within the $K_5$ part). This removes one red edge and adds one blue edge. The red graph now has one fewer edge in $K_5$, potentially reducing red triangles. The blue graph gains one edge within the $K_5$ part, potentially creating blue triangles (but blue was bipartite, so adding one edge within a part creates at most a few blue triangles).

This doesn't seem to help reduce edge-disjoint monochromatic triangles below 5.

Let me think about this differently. Maybe I should consider the problem from the upper bound side.

**Upper bound approach:** Show that any 2-coloring of $K_n$ (for some specific $n$) contains 5 edge-disjoint monochromatic triangles.

One approach: Use Ramsey-type arguments to find a large monochromatic subgraph, then use triangle packing within that subgraph.

$R(3,3) = 6$: any 2-coloring of $K_6$ has a monochromatic triangle.

If we can find a monochromatic $K_7$ in $K_n$, it contains 7 edge-disjoint monochromatic triangles (since $K_7$ can be decomposed into 7 triangles). So if $n \geq R(7,7)$... but $R(7,7)$ is huge.

Better approach: Find multiple disjoint monochromatic triangles iteratively.

Actually, let me think about a cleaner approach. 

**Key idea:** In any 2-coloring of $K_n$, we can greedily find edge-disjoint monochromatic triangles. After finding $k$ such triangles (using $3k$ edges), we need to find another monochromatic triangle in the remaining graph. The remaining graph has $\binom{n}{2} - 3k$ edges and is 2-colored.

The remaining graph is not complete, so we can't directly apply Ramsey. But we can use the following: if the remaining graph contains a $K_6$ (in the original vertex set, with all 15 edges still present), then it contains a monochromatic triangle.

After removing $3k$ edges, how many edges remain? $\binom{n}{2} - 3k$. For $k = 4$ (after finding 4 triangles), we need to find a 5th. The remaining graph has $\binom{n}{2} - 12$ edges.

We need this remaining graph to contain a monochromatic triangle. A sufficient condition is that it contains a $K_6$ (all 15 edges present). But this is hard to guarantee.

Let me think about a different approach. 

**Approach via monochromatic subgraphs:** 

In any 2-coloring of $K_n$, one color has at least $\lceil \binom{n}{2}/2 \rceil$ edges. Say red has at least $\lceil \binom{n}{2}/2 \rceil$ edges. By Turán's theorem, a graph on $n$ vertices with more than $n^2/4$ edges contains a triangle. So if $\lceil \binom{n}{2}/2 \rceil > n^2/4$, i.e., $\binom{n}{2}/2 > n^2/4$, i.e., $n(n-1)/4 > n^2/4$, i.e., $n-1 > n$, which is false. So this doesn't directly work.

But we can use a stronger result. Kruskal-Katona or similar results give lower bounds on the number of triangles given the number of edges.

Actually, let me think about a completely different approach. Let me consider the problem as a competition problem and think about what the answer might be.

Given that:
- $n = 10$ doesn't work (two-cliques 5+5 gives 4 edge-disjoint monochromatic triangles)
- $n = 11$ might work (two-cliques 5+6 gives 6, but we need to check all colorings)

The answer is likely $n = 11$ or higher. Let me check if $n = 11$ works.

For $n = 11$, we need to show that ANY 2-coloring of $K_{11}$ contains 5 edge-disjoint monochromatic triangles.

$K_{11}$ has $\binom{11}{2} = 55$ edges. Five edge-disjoint triangles use 15 edges.

Goodman's formula: $M(11) = \frac{11 \cdot 10 \cdot 6}{24} = \frac{660}{24} = 27.5$. Since this must be an integer, the minimum is at least 28.

Actually, let me re-examine. For $n = 11$ (odd), the Goodman extremal requires each vertex to have red degree 5. $11 \times 5 = 55$ is odd, so no 5-regular graph on 11 vertices exists. So we can't achieve the balanced case. The best we can do is have some vertices with degree 5 and some with degree 4 or 6.

If 10 vertices have degree 5 and 1 has degree 6: total = $50 + 6 = 56 = 2 \times 28$. So 28 red edges. Then:
$\sum d_v(10 - d_v) = 10 \times 5 \times 5 + 1 \times 6 \times 4 = 250 + 24 = 274$.
Monochromatic triangles = $\binom{11}{3} - 274/2 = 165 - 137 = 28$.

If 10 vertices have degree 5 and 1 has degree 4: total = $50 + 4 = 54 = 2 \times 27$. So 27 red edges.
$\sum d_v(10 - d_v) = 10 \times 5 \times 5 + 1 \times 4 \times 6 = 250 + 24 = 274$.
Monochromatic triangles = $165 - 137 = 28$.

So the minimum is 28 monochromatic triangles in any 2-coloring of $K_{11}$.

Now, with 28 monochromatic triangles, can we always find 5 edge-disjoint ones?

Each edge is in at most $n - 2 = 9$ monochromatic triangles. By the greedy argument, we can find at least $\lceil 28 / (3 \times 9 + 1) \rceil = \lceil 28/28 \rceil = 1$. Still useless.

But the greedy bound is very loose. The actual bound depends on the structure.

Let me think about this more carefully. 

Actually, I think I need to approach this problem differently. Let me think about what happens when we iteratively remove monochromatic triangles.

**Iterative approach:**

Step 1: Find a monochromatic triangle in $K_n$. Remove its 3 edges.
Step 2: Find a monochromatic triangle in the remaining graph. Remove its 3 edges.
...
Step 5: Find a monochromatic triangle in the remaining graph.

After 4 steps, we've removed 12 edges. The remaining graph has $\binom{n}{2} - 12$ edges. We need to find a monochromatic triangle in this remaining 2-colored graph.

The remaining graph is a 2-colored graph on $n$ vertices with $\binom{n}{2} - 12$ edges. We need it to contain a monochromatic triangle.

A 2-colored graph on $n$ vertices with $m$ edges is guaranteed to have a monochromatic triangle if... well, it's guaranteed if it contains a $K_6$ (by $R(3,3) = 6$). But more generally, we can use the following:

**Lemma:** A 2-colored graph on $n$ vertices with no monochromatic triangle has at most ... edges.

This is the "Ramsey-Turán" type problem. A 2-colored graph with no monochromatic triangle means both color classes are triangle-free. Each color class is triangle-free, so each has at most $n^2/4$ edges (Mantel). Total edges at most $n^2/2$. But $\binom{n}{2} = n(n-1)/2 < n^2/2$, so this doesn't help.

Wait, actually, a 2-coloring of $K_n$ with no monochromatic triangle exists only for $n \leq 5$ (since $R(3,3) = 6$). For $n \geq 6$, every 2-coloring of $K_n$ has a monochromatic triangle.

But we're not 2-coloring $K_n$; we're 2-coloring a subgraph of $K_n$ (after removing some edges). The question is: what's the maximum number of edges in a 2-colored graph on $n$ vertices with no monochromatic triangle?

This is the Ramsey-Turán number. Let me think...

A 2-colored graph $G$ on $n$ vertices with no monochromatic triangle means: the red graph is triangle-free AND the blue graph is triangle-free. Both are subgraphs of $G$, and together they partition $E(G)$.

The maximum number of edges in $G$ such that $G$ can be 2-colored with no monochromatic triangle is: we need both color classes to be triangle-free. The maximum is achieved when both color classes are bipartite (or more generally, triangle-free).

If both color classes are bipartite with the same bipartition $(A, B)$, then $G$ is also bipartite, with at most $|A| \cdot |B| \leq n^2/4$ edges.

But the two color classes don't need to have the same bipartition. For example, the red graph could be bipartite with parts $(A, B)$ and the blue graph bipartite with parts $(C, D)$, where these are different partitions.

The maximum number of edges in a graph that can be 2-colored with no monochromatic triangle is known. This is related to the Ramsey number $R(3,3) = 6$. Specifically, a graph $G$ on $n$ vertices has the property that every 2-coloring of $E(G)$ contains a monochromatic triangle if and only if $G$ contains $K_6$ as a (not necessarily induced) subgraph... no, that's not right either. $R(3,3) = 6$ means $K_6$ has this property, but a graph doesn't need to contain $K_6$ to have this property.

Actually, the correct statement is: a graph $G$ has the property that every 2-coloring of $E(G)$ contains a monochromatic triangle if and only if $\alpha(G) < 5$ and $\omega(G) < 5$... no, that's not right.

Let me think again. The Ramsey number $R(3,3) = 6$ means: every graph on 6 vertices has either a triangle or an independent set of size 3. Equivalently, every 2-coloring of $K_6$ has a monochromatic triangle.

For a general graph $G$, every 2-coloring of $E(G)$ has a monochromatic triangle if and only if $G$ is not a subgraph of any 2-colorable-by-triangle-free graph. This is complicated.

Let me take a different approach. Instead of the iterative greedy approach, let me think about the problem more directly.

**Direct approach:**

I want to find the minimum $n$ such that every 2-coloring of $K_n$ contains 5 edge-disjoint monochromatic triangles.

Let me think about what's known in the literature. This is related to the "edge-disjoint Ramsey number" or "size Ramsey number" for triangles.

Actually, I think this might be related to the following concept: the $k$-th Ramsey number for edge-disjoint monochromatic triangles. Let me denote it $R_k(3)$ = minimum $n$ such that every 2-coloring of $K_n$ contains $k$ edge-disjoint monochromatic triangles.

$R_1(3) = R(3,3) = 6$.

For general $k$, I believe $R_k(3)$ has been studied. Let me think about what values are known.

I recall that for edge-disjoint monochromatic triangles, the answer might be $R_k(3) = 3k + 3$ or something like that. Let me check:
- $R_1(3) = 6 = 3 \cdot 1 + 3$. ✓
- $R_2(3) = 9 = 3 \cdot 2 + 3$?
- $R_5(3) = 18 = 3 \cdot 5 + 3$?

Hmm, but I need to verify this. Let me think about whether $R_2(3) = 9$.

For $n = 8$: two-cliques 4+4 gives 1+1 = 2 edge-disjoint monochromatic triangles. So $R_2(3) > 8$.
For $n = 9$: two-cliques 4+5 gives 1+2 = 3 ≥ 2. But is there a coloring of $K_9$ with only 1 edge-disjoint monochromatic triangle?

Hmm, with $M(9) = 12$ monochromatic triangles minimum, it seems hard to have only 1 edge-disjoint one. But I need to check.

Actually, wait. Let me reconsider. The formula $R_k(3) = 3k + 3$ doesn't seem right because for $k = 1$, $R_1(3) = 6 = 3 + 3$, and for $k = 2$, we'd get 9. But let me check if $K_8$ can be 2-colored with only 1 edge-disjoint monochromatic triangle.

For $K_8$, two-cliques 4+4 gives 2 edge-disjoint monochromatic triangles. Can we find a coloring with only 1?

$M(8) = 8$. With 8 monochromatic triangles, can we have only 1 edge-disjoint? That would mean all 8 triangles share edges. Each triangle has 3 edges, so 8 triangles use at most $8 \times 3 = 24$ edge-incidences. If they all share a common edge, they use $1 + 8 \times 2 = 17$ distinct edges. $K_8$ has 28 edges, so this is possible in principle. But can we construct such a coloring?

This seems unlikely. With 8 monochromatic triangles in $K_8$, I'd expect at least 2-3 to be edge-disjoint.

Let me try a different approach. Let me think about the problem as a competition problem and try to find the answer.

Given the structure of the problem (find the smallest $n$), and the constraints, I think the answer might be $n = 11$.

Let me try to prove that $n = 11$ works (every 2-coloring of $K_{11}$ has 5 edge-disjoint monochromatic triangles) and that $n = 10$ doesn't (there's a 2-coloring of $K_{10}$ with at most 4 edge-disjoint monochromatic triangles).

**Lower bound ($n \geq 11$):** The two-cliques construction for $K_{10}$ (split 5+5, red within, blue between) gives 2 + 2 = 4 edge-disjoint monochromatic triangles. So $n \geq 11$.

**Upper bound ($n = 11$ works):** We need to show that every 2-coloring of $K_{11}$ contains 5 edge-disjoint monochromatic triangles.

This is the hard part. Let me think about how to prove this.

One approach: 
1. Find a monochromatic triangle $T_1$.
2. Remove its edges. The remaining graph has 52 edges on 11 vertices.
3. Find a monochromatic triangle $T_2$ in the remaining graph.
4. Remove its edges. 49 edges remain.
5. Continue until we have 5 triangles.

The key question is: after removing 4 monochromatic triangles (12 edges), does the remaining 2-colored graph on 11 vertices with 43 edges always contain a monochromatic triangle?

A 2-colored graph on 11 vertices with 43 edges and no monochromatic triangle: both color classes are triangle-free. Red has $r$ edges, blue has $43 - r$ edges. Both are triangle-free on 11 vertices. By Mantel's theorem, each has at most $\lfloor 11^2/4 \rfloor = 30$ edges. So $r \leq 30$ and $43 - r \leq 30$, giving $r \geq 13$. This is satisfiable (e.g., $r = 20$, blue = 23). So Mantel's theorem alone doesn't rule out a monochromatic-triangle-free 2-coloring of a 43-edge graph on 11 vertices.

But we need to use the fact that the 43-edge graph is a subgraph of $K_{11}$ obtained by removing 12 specific edges (those of 4 edge-disjoint monochromatic triangles). This structure might help.

Hmm, this is getting complicated. Let me think about a different approach.

**Approach via finding a large monochromatic subgraph:**

In any 2-coloring of $K_{11}$, one color has at least $\lceil 55/2 \rceil = 28$ edges. Say red has $\geq 28$ edges. 

By the Kruskal-Katona theorem (or a direct counting argument), a graph on 11 vertices with 28 edges has at least ... triangles. 

Actually, let me use a different result. The number of triangles in a graph with $m$ edges on $n$ vertices is at least $\frac{m(4m - n^2)}{3n}$ (by the Lovász-Simonovits theorem, or a simpler bound). For $m = 28$, $n = 11$: $\frac{28(112 - 121)}{33} = \frac{28 \times (-9)}{33} < 0$. So this bound is useless (it gives a negative number, meaning 28 edges on 11 vertices doesn't guarantee a triangle by this bound).

But we know that any graph on 11 vertices with more than $\lfloor 11^2/4 \rfloor = 30$ edges has a triangle (Mantel). 28 < 30, so 28 edges doesn't guarantee a triangle.

However, we're not just looking for one triangle; we're looking for 5 edge-disjoint monochromatic triangles (in either color). Let me think about this differently.

**Approach via Ramsey on subsets:**

In any 2-coloring of $K_{11}$, consider any 6 vertices. By $R(3,3) = 6$, the induced $K_6$ contains a monochromatic triangle. There are $\binom{11}{6} = 462$ such 6-subsets, each giving at least one monochromatic triangle. But these triangles may overlap heavily.

Let me think about a more structured approach.

**Approach: Find a vertex with high monochromatic degree.**

In a 2-coloring of $K_{11}$, each vertex has 10 incident edges, split into red and blue. By pigeonhole, each vertex has at least 5 edges of one color. Say vertex $v$ has at least 5 red edges, connecting to vertices $S = \{s_1, ..., s_5\}$ (at least 5).

Among $S$ (5 vertices), the edges are 2-colored. By $R(3,3) = 6$, we can't guarantee a monochromatic triangle in $K_5$. But we can say something: if there's a red edge among $S$, say $s_i s_j$ is red, then $\{v, s_i, s_j\}$ is a red triangle. If all edges among $S$ are blue, then $S$ is a blue $K_5$, which contains $\binom{5}{3} = 10$ blue triangles.

So either we find a red triangle through $v$, or $S$ is a blue clique. In the latter case, we have a blue $K_5$ with 10 blue triangles, and we can find 2 edge-disjoint blue triangles in it.

This gives us at least 1 or 2 monochromatic triangles, but we need 5.

Let me think about a more global approach.

**Approach: Use the structure of the coloring.**

Case 1: There exists a vertex $v$ with red degree $\geq 6$ (or blue degree $\geq 6$). WLOG red degree $\geq 6$. Let $S$ be the set of red neighbors, $|S| \geq 6$. Among $S$, by $R(3,3) = 6$, there's a monochromatic triangle. If it's red, we get a red triangle with $v$... no, the monochromatic triangle is within $S$, not necessarily involving $v$.

Actually, let me reconsider. If $v$ has red degree $\geq 6$, let $S$ be 6 red neighbors. Among $S$, there's a monochromatic triangle $T$. If $T$ is red, then $T$ is a red triangle. If $T$ is blue, then $T$ is a blue triangle. Either way, we have a monochromatic triangle within $S$.

But we also have: for any red edge $s_i s_j$ in $S$, $\{v, s_i, s_j\}$ is a red triangle. So if there are red edges in $S$, we get additional red triangles through $v$.

This is getting complicated. Let me try a different, more computational approach.

Actually, let me think about the problem from the perspective of the answer. This is a competition problem, and the answer is likely a clean number. Given the lower bound of 11 (from the two-cliques construction on $K_{10}$), the answer is at least 11. 

Let me check if the answer could be higher. For $n = 11$, the two-cliques 5+6 gives 6 edge-disjoint monochromatic triangles. But is there a different coloring of $K_{11}$ with fewer?

What about a coloring based on the 5-cycle? Or a Paley-type coloring?

For $n = 11$, the Paley graph exists (11 is prime, $11 \equiv 3 \pmod 4$). The Paley graph on 11 vertices is a 5-regular graph. Its complement is also 5-regular. The Paley graph on 11 vertices is self-complementary (since $11 \equiv 3 \pmod 4$, the Paley graph is self-complementary... actually, Paley graphs are self-complementary when $q \equiv 1 \pmod 4$. For $q \equiv 3 \pmod 4$, the Paley graph is a tournament, not a graph. Wait, no.

Paley graph: defined for $q \equiv 1 \pmod 4$ (prime power). For $q \equiv 3 \pmod 4$, the "Paley graph" would be a tournament (directed). So for $q = 11 \equiv 3 \pmod 4$, there's no Paley graph. 

So for $n = 11$, a balanced coloring would have each vertex with red degree 5 (but $11 \times 5 = 55$ is odd, impossible). So the most balanced coloring has some vertices with degree 4 and some with degree 5 (or 5 and 6).

Let me think about a specific balanced coloring of $K_{11}$. Take a 5-regular graph on 10 vertices (say the Petersen graph, which is 3-regular... no, we need 5-regular on 10 vertices, which would be the complement of a 4-regular graph). Actually, $K_{10}$ has degree 9, so a 5-regular graph on 10 vertices exists (e.g., the circulant graph $C_{10}(1,2,3,4,5)$... hmm, that's 10-regular. Let me think. A 5-regular graph on 10 vertices: take the complete graph $K_{10}$ (9-regular) and remove a 4-regular graph. A 4-regular graph on 10 vertices: the Petersen graph is 3-regular, its complement is 6-regular. Hmm.

This is getting too detailed. Let me step back and think about the problem more strategically.

I think the answer is $n = 11$. Let me try to prove it.

**Proof that $n = 11$ works:**

We need to show that every 2-coloring of $K_{11}$ contains 5 edge-disjoint monochromatic triangles.

**Proof that $n = 10$ doesn't work:**

The two-cliques construction (split 5+5, red within, blue between) gives only 4 edge-disjoint monochromatic triangles (2 in each $K_5$).

Now, for the upper bound, let me think about a proof strategy.

**Strategy:** We'll show that in any 2-coloring of $K_{11}$, we can find 5 edge-disjoint monochromatic triangles.

**Key lemma:** In any 2-coloring of $K_{11}$, there are at least 28 monochromatic triangles (Goodman's theorem).

Now, I need to show that among 28+ monochromatic triangles in $K_{11}$, we can always find 5 edge-disjoint ones.

**Approach:** Use the fact that $K_{11}$ has 55 edges, and each edge is in at most 9 monochromatic triangles. If we have 28 monochromatic triangles using at most 55 edges, then by a packing argument...

Actually, let me think about this using a result on hypergraph matchings. We have a 3-uniform hypergraph $H$ on 55 vertices (the edges of $K_{11}$), with 28 hyperedges (the monochromatic triangles). We want a matching of size 5 in $H$.

The maximum degree in $H$ is at most 9 (each edge of $K_{11}$ is in at most 9 monochromatic triangles, since it's in at most $n-2 = 9$ triangles total). By a greedy argument, the matching number is at least $|E(H)| / (3 \Delta(H)) = 28 / 27 > 1$. So we get at least 2, not 5.

But we can do better. The actual structure is more constrained. Let me think about it differently.

**Better approach:** Instead of the generic greedy bound, use the specific structure of the problem.

Let me try to find 5 edge-disjoint monochromatic triangles by considering cases based on the structure of the coloring.

**Case analysis:**

**Case 1: One color class has a vertex of degree $\geq 7$.**

Say vertex $v$ has red degree $\geq 7$. Let $S$ be 7 red neighbors. The induced subgraph on $S$ is a 2-coloring of $K_7$. By Goodman's theorem, it has at least $M(7) = 4$ monochromatic triangles. 

Moreover, any red edge in $S$ gives a red triangle with $v$. The number of red edges in $S$ is at least... well, we don't know. But the red subgraph on $S$ has some edges, and each gives a red triangle with $v$.

Hmm, this is getting complicated. Let me try yet another approach.

**Approach via iterative removal with Ramsey:**

We want to show that we can iteratively find 5 edge-disjoint monochromatic triangles in any 2-coloring of $K_{11}$.

Step 1: By $R(3,3) = 6$, any 6 vertices contain a monochromatic triangle. Find one, call it $T_1$, remove its 3 edges.

Step 2: The remaining graph has 52 edges. Does it contain a monochromatic triangle? We need to find 6 vertices whose induced subgraph is still $K_6$ (all 15 edges present). After removing 3 edges, at most 3 of the $\binom{11}{6} = 462$ six-subsets are affected (those containing all 3 edges of $T_1$... actually, a 6-subset is "affected" if it's missing at least one edge). The 3 edges of $T_1$ form a triangle on 3 vertices. A 6-subset contains all 3 edges iff it contains all 3 vertices of $T_1$. There are $\binom{8}{3} = 56$ such 6-subsets. So $462 - 56 = 406$ six-subsets still have all their edges, and each contains a monochromatic triangle. So we can find $T_2$.

Step 3: After removing 6 edges (two triangles), how many 6-subsets still have all edges? A 6-subset is "complete" (all 15 edges present) iff it doesn't contain any edge from $T_1$ or $T_2$. $T_1$ and $T_2$ are edge-disjoint, so they involve at most 6 vertices (could be fewer if they share vertices). 

If $T_1$ and $T_2$ share a vertex, they involve 5 vertices. A 6-subset avoids all their edges iff it contains none of the 6 edges. The 6 edges are on 5 vertices. A 6-subset that doesn't contain any of these 5 vertices: $\binom{6}{6} = 1$ (the 6 remaining vertices). A 6-subset that contains some but not all of the 5 vertices might still avoid the edges... this is getting complicated.

Let me think about this differently. After removing $k$ edge-disjoint triangles (3k edges), the remaining graph has $55 - 3k$ edges. We need to find a monochromatic triangle in this remaining graph. A sufficient condition is that the remaining graph contains a $K_6$ (complete subgraph on 6 vertices).

The remaining graph misses $3k$ edges. A $K_6$ on vertices $S$ ($|S| = 6$) is present iff none of the $3k$ removed edges has both endpoints in $S$. 

The $3k$ removed edges form $k$ edge-disjoint triangles. Each triangle has 3 vertices. The total number of vertices involved is at most $3k$ (if all triangles are vertex-disjoint) and at least $k + 2$ (if all share 2 vertices... no, edge-disjoint triangles can share at most 1 vertex if they share any).

Wait, two edge-disjoint triangles can share 0 or 1 vertices (they can't share 2 vertices because that would mean they share an edge).

So the $k$ edge-disjoint triangles involve at least $k + 2$ vertices (if they form a "star" of triangles sharing one vertex) and at most $3k$ vertices (if vertex-disjoint).

For a $K_6$ to exist in the remaining graph, we need 6 vertices that don't contain any edge from the removed triangles. The removed edges are on at most $3k$ vertices. If $3k \leq 5$, then there are $11 - 3k \geq 6$ vertices not involved in any removed edge, and these 6 vertices form a $K_6$ in the remaining graph. So for $k \leq 1$ (3 vertices), we're fine.

But for $k = 4$ (12 edges, up to 12 vertices... but we only have 11), we can't guarantee a $K_6$ in the remaining graph.

So this approach only works for the first few steps. We need a different argument for later steps.

Let me think about a more refined approach.

**Refined approach:** 

After removing $k$ edge-disjoint monochromatic triangles, the remaining 2-colored graph on 11 vertices has $55 - 3k$ edges. We need to find a monochromatic triangle in it.

A 2-colored graph on $n$ vertices with no monochromatic triangle can have at most ... edges. This is the Ramsey-Turán problem for $R(3,3)$.

The maximum number of edges in a 2-colored graph on $n$ vertices with no monochromatic triangle is: we need both color classes to be triangle-free. The maximum is achieved when both color classes are bipartite. If both are bipartite with the same partition, the total graph is bipartite with at most $\lfloor n^2/4 \rfloor$ edges. But they can have different partitions.

Actually, the maximum number of edges in a graph $G$ on $n$ vertices such that $G$ can be 2-colored with no monochromatic triangle is the Ramsey-Turán number $RT(n, K_3, K_3, 2)$... I'm not sure of the exact value.

Let me think about it differently. If both the red and blue subgraphs are triangle-free, then both are bipartite (by Mantel's theorem, triangle-free graphs on $n$ vertices have at most $n^2/4$ edges, but they don't have to be bipartite—wait, actually, by Mantel's theorem, a triangle-free graph has at most $n^2/4$ edges, and the extremal case is the complete bipartite graph. But a triangle-free graph doesn't have to be bipartite; it just can't have triangles. For example, $C_5$ is triangle-free but not bipartite.)

OK so both color classes are triangle-free (not necessarily bipartite). The question is: what's the maximum total number of edges?

If the red graph is triangle-free with $r$ edges and the blue graph is triangle-free with $b$ edges, and $r + b = m$ (total edges in $G$), then $r \leq \lfloor n^2/4 \rfloor$ and $b \leq \lfloor n^2/4 \rfloor$, so $m \leq 2\lfloor n^2/4 \rfloor$.

For $n = 11$: $m \leq 2 \times 30 = 60$. But $\binom{11}{2} = 55 < 60$, so this doesn't help. We can't rule out a monochromatic-triangle-free 2-coloring of $K_{11}$... but we know from $R(3,3) = 6$ that $K_6$ always has a monochromatic triangle, so $K_{11}$ certainly does too.

The issue is that after removing edges, the remaining graph might not contain a $K_6$, and a non-complete graph can be 2-colored without monochromatic triangles even on 11 vertices.

So I need a better bound. Let me think about the maximum number of edges in a 2-colored graph on 11 vertices with no monochromatic triangle.

A 2-colored graph with no monochromatic triangle means both color classes are triangle-free. The maximum total edges is when both color classes are as large as possible while being triangle-free.

The maximum edges in a triangle-free graph on 11 vertices is 30 (Mantel). So the maximum total is 60. But we need the two color classes to partition the edge set, so the total is the number of edges in $G$, which can be at most 55 (if $G = K_{11}$). But we know $K_{11}$ can't be 2-colored without monochromatic triangles (since $K_6$ can't).

So the question is: what's the maximum number of edges in a graph $G$ on 11 vertices that CAN be 2-colored without monochromatic triangles?

This is equivalent to: what's the maximum number of edges in a graph $G$ on 11 vertices such that both $G$ and $\bar{G}$ are $K_6$-free... no, that's not right either.

Actually, a graph $G$ can be 2-colored without monochromatic triangles iff $G$ doesn't contain $K_6$ as a subgraph... no, that's not right. $R(3,3) = 6$ means $K_6$ can't be 2-colored without monochromatic triangles, but a graph that doesn't contain $K_6$ might still not be 2-colorable without monochromatic triangles.

The correct characterization: $G$ can be 2-colored without monochromatic triangles iff $G$ is a subgraph of some graph $H$ where $H$ can be 2-colored without monochromatic triangles. The maximum such $H$ on $n$ vertices is the Ramsey graph for $R(3,3)$.

The Ramsey graph for $R(3,3) = 6$ on 5 vertices is $K_5$, which can be 2-colored without monochromatic triangles (the unique such coloring is the 5-cycle in each color). On 11 vertices, the maximum graph that can be 2-colored without monochromatic triangles is... well, it's the complement of the Ramsey graph, or something. This is getting complicated.

Let me look at this from a different angle. The key property is: a 2-edge-colored graph has no monochromatic triangle iff both color classes are triangle-free. The maximum number of edges in such a graph on $n$ vertices is $ex(n, \{K_3, K_3\})$ where the two $K_3$'s are in different colors. This is the same as the maximum of $e(G)$ over all graphs $G$ on $n$ vertices that admit a 2-edge-coloring where both color classes are triangle-free.

I believe this maximum is $\lfloor n^2/4 \rfloor + \lfloor n/2 \rfloor \cdot \lceil n/2 \rceil$... no, I'm just guessing.

Let me think about it constructively. Take a bipartite graph with parts $A$ and $B$ where $|A| = a$, $|B| = b$, $a + b = n$. Color all edges red. Now add some blue edges. The blue edges must form a triangle-free graph. We can add blue edges within $A$ and within $B$ (since the red graph is bipartite, the blue graph is the complement restricted to within parts, plus possibly some cross edges if the red graph isn't complete bipartite).

If the red graph is the complete bipartite graph $K_{a,b}$ (with $ab$ edges), the blue graph is $K_a \cup K_b$ (with $\binom{a}{2} + \binom{b}{2}$ edges). The blue graph has triangles iff $a \geq 3$ or $b \geq 3$. So for the blue graph to be triangle-free, we need $a \leq 2$ and $b \leq 2$, giving $n \leq 4$. Not useful.

So the complete bipartite red graph doesn't work for large $n$. We need a more clever construction.

Alternative: Let the red graph be a triangle-free graph that's not bipartite (like a blow-up of $C_5$), and the blue graph be its complement (also triangle-free). 

A graph and its complement are both triangle-free: such graphs are called "Ramsey graphs" for $(3,3)$. The maximum number of vertices for such a graph is 5 (the 5-cycle $C_5$ and its complement, which is also $C_5$). For $n > 5$, no graph on $n$ vertices has both the graph and its complement triangle-free.

But we're not requiring the graph and its complement to be triangle-free; we're requiring a graph $G$ (not necessarily complete) and a 2-coloring of $G$ where both color classes are triangle-free. This is different.

Let me think about it as follows: we have a graph $G$ on $n$ vertices, and we partition $E(G)$ into red and blue, both triangle-free. The maximum $|E(G)|$ is what we want.

For each vertex $v$, let $d_r(v)$ and $d_b(v)$ be its red and blue degrees. The red neighborhood of $v$ is an independent set in the red graph (otherwise there'd be a red triangle through $v$). Similarly for blue. So $d_r(v) \leq \alpha(G_r)$ and $d_b(v) \leq \alpha(G_b)$... this isn't directly useful.

Let me try a different approach. The number of monochromatic triangles in a 2-coloring of $G$ is:
$$\text{#mono triangles} = \text{#triangles in } G - \frac{1}{2}\sum_v d_r(v) d_b(v)$$

Wait, this formula is for complete graphs. For general graphs, it's:
$$\text{#mono triangles} = \text{#triangles in } G - \text{#non-mono triangles in } G$$

A non-monochromatic triangle has 2 edges of one color and 1 of the other. The number of non-monochromatic triangles is:
$$\frac{1}{2}\sum_v \binom{d_r(v)}{1}\binom{d_b(v)}{1} \cdot [\text{something}]$$

Actually, for a general graph, the number of "cherries" (paths of length 2) at vertex $v$ with one red and one blue edge is $d_r(v) \cdot d_b(v)$. Each non-monochromatic triangle contributes 2 such cherries (one at each of the two vertices where the color changes). So:

$$\text{#non-mono triangles} = \frac{1}{2}\sum_v d_r(v) d_b(v)$$

Wait, that's not right either. A non-monochromatic triangle has vertices $a, b, c$ with, say, $ab$ and $ac$ red, $bc$ blue. The cherry at $a$ has one red and one blue edge... no, the cherry at $a$ has two red edges ($ab$ and $ac$). The cherry at $b$ has one red ($ba$) and one blue ($bc$). The cherry at $c$ has one red ($ca$) and one blue ($cb$). So this non-monochromatic triangle contributes 2 to $\sum_v d_r(v) d_b(v)$ (from vertices $b$ and $c$). So:

$$\text{#non-mono triangles} = \frac{1}{2}\sum_v d_r(v) d_b(v)$$

And:
$$\text{#mono triangles} = \text{#triangles in } G - \frac{1}{2}\sum_v d_r(v) d_b(v)$$

For this to be 0 (no monochromatic triangles), we need:
$$\text{#triangles in } G = \frac{1}{2}\sum_v d_r(v) d_b(v)$$

This is a constraint on the graph and its coloring.

OK, this is getting very complicated. Let me try a completely different approach to the problem.

**New approach: Direct case analysis for $K_{11}$.**

Let me try to prove that every 2-coloring of $K_{11}$ has 5 edge-disjoint monochromatic triangles by considering the structure of the coloring.

**Key observation:** In any 2-coloring of $K_{11}$, there exists a monochromatic triangle. Remove it. The remaining graph has 52 edges on 11 vertices. We need to find 4 more edge-disjoint monochromatic triangles.

After removing 4 triangles (12 edges), the remaining graph has 43 edges. We need to find a monochromatic triangle in a 2-coloring of a 43-edge graph on 11 vertices.

**Claim:** A 2-colored graph on 11 vertices with 43 edges always contains a monochromatic triangle.

**Proof of claim:** Suppose not. Then both color classes are triangle-free. Red has $r$ edges, blue has $43 - r$ edges. Both are triangle-free on 11 vertices, so $r \leq 30$ and $43 - r \leq 30$, giving $13 \leq r \leq 30$.

But we also need the graph $G$ (with 43 edges) to be such that both $G_r$ and $G_b$ are triangle-free. The maximum number of edges in a graph on 11 vertices that can be partitioned into two triangle-free graphs is... 

Well, we need $G_r$ triangle-free and $G_b$ triangle-free, with $G_r \cup G_b = G$ and $G_r \cap G_b = \emptyset$. The maximum $|E(G)|$ is the maximum of $|E(G_r)| + |E(G_b)|$ where both are triangle-free subgraphs of $K_{11}$ and they're edge-disjoint.

This is equivalent to: what's the maximum number of edges in a 2-coloring of a subgraph of $K_{11}$ with no monochromatic triangle?

I claim this maximum is less than 43. Let me try to find the maximum.

If both $G_r$ and $G_b$ are triangle-free, then each is a subgraph of a complete bipartite graph (by Mantel, the extremal triangle-free graph is bipartite, but non-bipartite triangle-free graphs also exist). However, the maximum edges for a triangle-free graph on 11 vertices is 30 (achieved by $K_{5,6}$).

So $|E(G)| \leq 30 + 30 = 60$. But we also need $G_r$ and $G_b$ to be edge-disjoint, so $|E(G)| = |E(G_r)| + |E(G_b)| \leq 55$ (total edges in $K_{11}$). And we need both to be triangle-free.

But can we achieve 43? We need $G_r$ and $G_b$ both triangle-free, edge-disjoint, with total 43 edges. For example, $G_r = K_{5,6}$ (30 edges, bipartite) and $G_b$ = some triangle-free graph with 13 edges on 11 vertices, edge-disjoint from $G_r$. The edges not in $G_r$ are the edges within the part of size 5 and within the part of size 6: $\binom{5}{2} + \binom{6}{2} = 10 + 15 = 25$ edges. So $G_b$ is a subgraph of $K_5 \cup K_6$ with 13 edges. For $G_b$ to be triangle-free, it can't contain a triangle in $K_5$ or $K_6$. A triangle-free subgraph of $K_5$ has at most 6 edges (Mantel: $\lfloor 25/4 \rfloor = 6$), and a triangle-free subgraph of $K_6$ has at most 9 edges (Mantel: $\lfloor 36/4 \rfloor = 9$). So $G_b$ can have at most $6 + 9 = 15$ edges. We need 13, which is $\leq 15$. So yes, we can have $|E(G)| = 30 + 13 = 43$ with both color classes triangle-free!

So the claim is FALSE. A 2-colored graph on 11 vertices with 43 edges CAN be monochromatic-triangle-free.

This means the iterative approach (remove 4 triangles, then find a 5th) doesn't work directly, because after removing 4 triangles, the remaining 43-edge graph might not have a monochromatic triangle.

But wait—the remaining 43-edge graph is not arbitrary; it's obtained by removing 4 specific edge-disjoint monochromatic triangles from a 2-coloring of $K_{11}$. The structure of the removed triangles matters.

Hmm, but the counterexample above shows that a 43-edge graph CAN be 2-colored without monochromatic triangles. The question is whether such a graph can arise as the remainder after removing 4 edge-disjoint monochromatic triangles from a 2-coloring of $K_{11}$.

This is getting very complicated. Let me try a completely different approach.

**Approach: Use known results or a more clever argument.**

Let me reconsider the problem. Maybe the answer is not 11 but something larger.

Let me check $n = 11$ more carefully with the two-cliques construction. We showed that the 5+6 split gives 6 edge-disjoint monochromatic triangles. But what about other colorings?

Actually, let me think about a different lower bound construction. Instead of two cliques, what about a coloring based on a 5-cycle structure?

**Construction: Blow-up of $C_5$.**

Take a 5-cycle $C_5$ on vertices $\{1, 2, 3, 4, 5\}$. Replace each vertex with a group of vertices (a "blow-up"). Color edges within each group red, edges corresponding to cycle edges red, and edges corresponding to non-cycle edges (the complement of $C_5$, which is also $C_5$) blue.

Wait, this is the standard Ramsey coloring. For $C_5$ blow-up, each group has $n/5$ vertices. The red graph is a blow-up of $C_5$ (with cliques within groups), and the blue graph is a blow-up of $\bar{C_5} = C_5$ (with independent sets within groups).

For $n = 10$ (groups of 2): Red graph = blow-up of $C_5$ with groups of 2. Red triangles: within groups ($5 \times 1 = 5$ triangles, one per group of 2... wait, a group of 2 has no triangle). Actually, red triangles can be: (a) within a group (needs group size $\geq 3$), (b) using edges of the $C_5$ blow-up (three consecutive groups, but $C_5$ has no triangle, so no such triangles), (c) mixing within-group and between-group edges.

For groups
