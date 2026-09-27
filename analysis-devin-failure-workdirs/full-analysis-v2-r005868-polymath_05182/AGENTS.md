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
  <problem_id>polymath_05182</problem_id>
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

Let $n > 2$ be an integer. Consider $n$ points $A_1, A_2, \ldots, A_n$ in space such that no four points are coplanar. Every pair of points $(A_i, A_j)$ is connected by an edge. We color each edge either blue or red such that:
I. For each $i \in \{1, \ldots, n\}$, the number of blue edges incident to $A_i$ is at most 4.
II. For every red edge $A_iA_j$, there exists at least one point $A_k$ ($k \neq i, j$) such that both $A_iA_k$ and $A_jA_k$ are blue.
Find the maximal value of $n$ for which such a coloring exists.

## Standard Solution

The problem can be modeled using a graph where blue edges form a subgraph $G_B$. Condition II implies that every pair of vertices not connected by a blue edge must have a common neighbor in $G_B$. This means the diameter of $G_B$ is at most 2. Condition I states that the maximum degree $\Delta(G_B) \leq 4$.
The number of vertices $n$ in a graph with maximum degree $d$ and diameter 2 is bounded by the Moore bound $n \leq 1 + d + d(d-1)$. For $d=4$, this gives $n \leq 1 + 4 + 12 = 17$.
A Moore graph with $d=4$ and $n=17$ does not exist. Further analysis (as shown in the solution) excludes $n=16$. For $n=15$, such a graph (e.g., the complement of the line graph of $K_6$ or certain configurations of the Hoffman-Singleton graph) can be constructed to satisfy the conditions.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have $n$ points in space, no four coplanar. Every pair connected by an edge, colored blue or red.

Conditions:
I. Each vertex has at most 4 blue edges incident.
II. Every red edge $A_iA_j$ has at least one common blue neighbor (a vertex $A_k$ connected to both by blue edges).

Find maximal $n$.

Let me think about this. The blue graph $G$ has maximum degree 4. The red graph is the complement (restricted to edges not blue). Condition II says: for every red edge (i.e., every non-blue edge), there's a vertex connected to both endpoints by blue edges. In other words, every non-edge of $G$ has a common neighbor in $G$.

So $G$ is a graph on $n$ vertices with maximum degree 4, such that every non-adjacent pair has a common neighbor.

We want to maximize $n$.

The condition "every non-adjacent pair has a common neighbor" is related to the concept where the graph has diameter 2 (every pair is at distance ≤ 2). Actually, diameter 2 means every pair of vertices is at distance ≤ 2, which means every non-adjacent pair has a common neighbor. Yes, exactly. So $G$ has diameter at most 2.

Wait, but we also need diameter exactly... no, diameter ≤ 2 means every pair at distance ≤ 2. Adjacent pairs are at distance 1, non-adjacent pairs need a common neighbor (distance 2). So condition II is exactly: $G$ has diameter ≤ 2.

So we need: a graph on $n$ vertices, max degree 4, diameter ≤ 2. Maximize $n$.

This is the degree-diameter problem! For max degree 4 and diameter 2, the maximum number of vertices is known.

The Moore bound for degree $d$ and diameter $k$: $n \leq 1 + d + d(d-1) + \cdots + d(d-1)^{k-1}$.

For $d = 4, k = 2$: $n \leq 1 + 4 + 4 \cdot 3 = 1 + 4 + 12 = 17$.

But the Moore bound is not always achievable. For degree 4, diameter 2, the Moore bound is 17, but the Moore graph of degree 4, diameter 2 would need to exist. Moore graphs of diameter 2 are exactly the graphs achieving $n = d^2 + 1$. For $d = 4$, $n = 17$.

Moore graphs of diameter 2 exist only for $d = 2$ (5-cycle), $d = 3$ (Petersen graph), $d = 7$ (Hoffman-Singleton graph), and possibly $d = 57$.

So for $d = 4$, there's no Moore graph, meaning $n < 17$.

The degree-diameter problem for $(4, 2)$: the known maximum is... let me think. The largest known graph with degree 4 and diameter 2.

Actually, let me recall. The degree-diameter problem records: for degree 4, diameter 2, the maximum is 15.

Hmm, let me think more carefully. The Moore bound is 17. Since no Moore graph exists for $d=4$, the maximum is at most 16. But is 16 achievable? 

Actually, I recall that for the degree-diameter problem, the value for $(\Delta, D) = (4, 2)$ is 15. Let me verify this reasoning.

Let me think about it differently. We need a graph with max degree 4, diameter 2, on as many vertices as possible.

Let me try to construct one with 15 vertices and prove 16 is impossible, or construct 16.

Actually, let me reconsider. The problem says "no four points are coplanar" — this is just to ensure the geometric configuration is general (so that the graph structure is what matters, not geometric coincidences). Actually, wait — does the geometry matter at all? The conditions are purely graph-theoretic. The "no four coplanar" might be a red herring or ensure that certain geometric configurations don't create issues. Actually, re-reading: the points are in space, edges connect every pair, coloring is on edges. The conditions are purely about the graph. The "no four coplanar" likely ensures we're dealing with a complete graph $K_n$ in general position, but since all pairs are connected, the geometry doesn't affect the graph. So this is purely a graph theory problem.

So the answer is the maximum $n$ for a graph with max degree 4 and diameter 2.

Let me think about whether 15 or 16 is the answer.

The degree-diameter problem: for $\Delta = 4, D = 2$, the known maximum is 15.

Let me try to prove the upper bound and construct the lower bound.

**Upper bound**: Moore bound gives $n \leq 17$. Since no Moore graph exists for $d = 4$, $n \leq 16$.

Can we rule out 16?

Let me think about this more carefully. Suppose $G$ has $n$ vertices, max degree 4, diameter 2.

For any vertex $v$, the number of vertices within distance 2 is at most $1 + 4 + 4 \cdot 3 = 17$. Since diameter is 2, all $n$ vertices are within distance 2 of $v$, so $n \leq 17$.

If $n = 17$, we need a Moore graph, which doesn't exist for $d = 4$.

If $n = 16$, then for every vertex $v$, at least $17 - 16 = 1$ of the "slots" in the BFS tree is wasted. Let me think about what constraints this gives.

Actually, let me think about this differently using the standard approach.

For a graph with $n$ vertices, max degree $\Delta = 4$, diameter 2:

For each vertex $v$, let $d(v)$ be its degree. The number of vertices at distance exactly 1 from $v$ is $d(v)$, and at distance exactly 2 is at most $\sum_{u \sim v} (d(u) - 1)$ (each neighbor $u$ contributes at most $d(u) - 1$ vertices at distance 2, but there could be overlaps). For diameter 2, we need $n \leq 1 + d(v) + \sum_{u \sim v}(d(u)-1)$ for every $v$.

Hmm, this is getting complex. Let me try a different approach.

Let me count the total number of edges and use double counting.

Let $e$ be the number of edges. Since max degree is 4, $2e \leq 4n$, so $e \leq 2n$.

For diameter 2, every pair of non-adjacent vertices has a common neighbor. The number of non-adjacent pairs is $\binom{n}{2} - e$. Each vertex $v$ with degree $d(v)$ is a common neighbor of $\binom{d(v)}{2}$ pairs. So:

$$\binom{n}{2} - e \leq \sum_v \binom{d(v)}{2}$$

We have $\sum_v \binom{d(v)}{2} = \frac{1}{2}\sum_v d(v)^2 - \frac{1}{2}\sum_v d(v) = \frac{1}{2}\sum d(v)^2 - e$.

By convexity, $\sum d(v)^2 \geq \frac{(\sum d(v))^2}{n} = \frac{4e^2}{n}$.

So $\binom{n}{2} - e \leq \frac{1}{2} \cdot \frac{4e^2}{n} - e = \frac{2e^2}{n} - e$.

Thus $\binom{n}{2} \leq \frac{2e^2}{n}$, i.e., $\frac{n(n-1)}{2} \leq \frac{2e^2}{n}$, so $n^2(n-1) \leq 4e^2$.

Since $e \leq 2n$, $4e^2 \leq 16n^2$, so $n^2(n-1) \leq 16n^2$, giving $n - 1 \leq 16$, i.e., $n \leq 17$.

This gives the Moore bound again. To improve, we need to use the fact that max degree is exactly at most 4 (not all vertices can have degree 4 if $n$ is odd, etc.).

Let me be more careful. We have $e \leq 2n$ with equality iff all degrees are 4. If $n$ is odd, then $\sum d(v) = 2e$ is even, and if all degrees are 4, $2e = 4n$, so $e = 2n$, which is fine for any $n$. So parity doesn't immediately help.

Let me try $n = 16$. If all vertices have degree 4, then $e = 32$, and $\sum \binom{d(v)}{2} = 16 \cdot 6 = 96$. The number of non-adjacent pairs is $\binom{16}{2} - 32 = 120 - 32 = 88$. So we need $88 \leq 96$, which is satisfied. But we also need that every non-adjacent pair has at least one common neighbor, and the counting only gives an average. We need to check if the overlaps can be arranged so that every non-adjacent pair is covered.

Actually, the counting argument gives $88 \leq 96$, meaning on average each non-adjacent pair has $96/88 > 1$ common neighbors. So it's not immediately ruled out.

Let me think about whether a 4-regular graph on 16 vertices with diameter 2 exists.

Hmm, actually, I think the answer to the degree-diameter problem for $(4,2)$ is 15. Let me try to recall or derive.

Let me try to rule out $n = 16$ more carefully.

Suppose $G$ is 4-regular on 16 vertices with diameter 2. For any vertex $v$, the 4 neighbors of $v$ together with $v$ account for 5 vertices. The remaining 11 vertices must be at distance 2 from $v$. Each neighbor $u$ of $v$ has 3 other neighbors (besides $v$), so the 4 neighbors contribute at most $4 \times 3 = 12$ vertices at distance 2. We need at least 11, so at most 1 overlap among these distance-2 vertices.

This is quite restrictive. Let me think about the structure.

For vertex $v$ with neighbors $u_1, u_2, u_3, u_4$: the sets $N(u_i) \setminus \{v\}$ have size 3 each, total 12, and their union must have size $\geq 11$ (since 11 vertices are at distance 2). So at most 1 element is in two of these sets (i.e., at most 1 pair of neighbors of $v$ share a common neighbor other than $v$).

This means: for each vertex $v$, at most 1 pair of its neighbors have a common neighbor other than $v$. Equivalently, the number of "triangles through $v$" plus the number of "4-cycles through $v$ where $v$ is not in the 4-cycle but two neighbors of $v$ share a neighbor" ... hmm, let me rephrase.

If two neighbors $u_i, u_j$ of $v$ are adjacent, then they share $v$ as a common neighbor, but that doesn't create an overlap in the distance-2 sets (since $v$ is excluded). If $u_i$ and $u_j$ share a neighbor $w \neq v$, then $w$ is in both $N(u_i) \setminus \{v\}$ and $N(u_j) \setminus \{v\}$, creating an overlap.

So the number of overlaps = number of pairs $(i,j)$ such that $u_i$ and $u_j$ have a common neighbor other than $v$. This includes the case where $u_i$ and $u_j$ are adjacent (they share each other as neighbors, but wait, if $u_i$ and $u_j$ are adjacent, then $u_j \in N(u_i)$ and $u_i \in N(u_j)$, but $u_j \notin N(u_i) \setminus \{v\}$ unless... no, $u_j$ is a neighbor of $u_i$ but $u_j \neq v$, so $u_j \in N(u_i) \setminus \{v\}$. Similarly $u_i \in N(u_j) \setminus \{v\}$. So if $u_i$ and $u_j$ are adjacent, $u_j$ is in $N(u_i) \setminus \{v\}$ and $u_i$ is in $N(u_j) \setminus \{v\}$, but these are different elements, so no overlap from this. Unless $u_i$ and $u_j$ share a third common neighbor $w$.)

OK so overlaps come from pairs of neighbors of $v$ that share a common neighbor $w \neq v$. Each such pair contributes at least 1 overlap (the vertex $w$).

We need at most 1 overlap total for each $v$. So for each $v$, at most 1 pair of its neighbors share a common neighbor other than $v$.

Now, let's count the total number of such "bad pairs" across all vertices. A "bad pair" for $v$ is a pair of neighbors of $v$ that share a common neighbor $w \neq v$.

Actually, let me count the number of pairs $(v, \{u_i, u_j\})$ where $u_i, u_j$ are neighbors of $v$ and they share a common neighbor $w \neq v$. 

Hmm, this is getting complicated. Let me try a different approach.

Let me count the number of 4-cycles in the graph. A 4-cycle $v - u_i - w - u_j - v$ corresponds to $u_i, u_j$ being neighbors of $v$ sharing common neighbor $w \neq v$.

The number of such configurations: for each pair of vertices $u_i, u_j$ at distance 2 (with common neighbors), count the common neighbors.

Actually, let me count differently. Let $c(u_i, u_j)$ = number of common neighbors of $u_i$ and $u_j$. For non-adjacent $u_i, u_j$, $c(u_i, u_j) \geq 1$ (diameter 2). For adjacent $u_i, u_j$, $c(u_i, u_j)$ can be 0 or more.

The total $\sum_{\{u_i, u_j\}} c(u_i, u_j) = \sum_v \binom{d(v)}{2} = 16 \cdot 6 = 96$ (for 4-regular on 16 vertices).

The number of pairs is $\binom{16}{2} = 120$. Of these, 32 are edges and 88 are non-edges.

For non-edges, $c \geq 1$, so $\sum_{\text{non-edges}} c \geq 88$.
For edges, $c \geq 0$, so $\sum_{\text{edges}} c \geq 0$.
Total $\geq 88$. We have total $= 96$, so $\sum_{\text{edges}} c \leq 8$ and the "excess" on non-edges is $\leq 8$.

Now, the number of triangles: each triangle contributes 1 to $c$ for each of its 3 edges. So the number of triangles $T$ satisfies $3T \leq \sum_{\text{edges}} c \leq 8$, so $T \leq 2$.

Now, back to the overlap counting. For vertex $v$, the number of overlaps = number of pairs of neighbors of $v$ sharing a common neighbor $\neq v$. 

A pair $\{u_i, u_j\}$ of neighbors of $v$ shares common neighbor $w \neq v$ iff $v, u_i, w, u_j$ form a 4-cycle (or $u_i, u_j$ adjacent and $w$ is another common neighbor, etc.). Actually, $c(u_i, u_j) - [\text{v is common neighbor}]$ = number of common neighbors other than $v$. If $u_i, u_j$ are both neighbors of $v$, then $v$ is a common neighbor, so the number of other common neighbors is $c(u_i, u_j) - 1$.

The number of overlaps for $v$ = $\sum_{\{u_i, u_j\} \subseteq N(v)} \max(0, c(u_i, u_j) - 1)$... no wait. The overlap is: the sets $N(u_i) \setminus \{v\}$ overlap. The total size of union = $\sum |N(u_i) \setminus \{v\}| - \text{overlaps}$. By inclusion-exclusion, overlaps = sum of pairwise intersections - sum of triple intersections + ... 

Actually, the number of overlaps (i.e., $12 - |union|$) = $\sum_{\{i,j\}} |(N(u_i) \setminus \{v\}) \cap (N(u_j) \setminus \{v\})| - \text{higher order}$.

The pairwise intersection $|(N(u_i) \setminus \{v\}) \cap (N(u_j) \setminus \{v\})|$ = number of common neighbors of $u_i, u_j$ other than $v$ = $c(u_i, u_j) - 1$ (since $v$ is a common neighbor).

So the number of overlaps $\geq \sum_{\{u_i, u_j\} \subseteq N(v)} (c(u_i, u_j) - 1)$ (with equality if no triple overlaps, but overlaps $\geq$ this sum since higher order terms are subtracted... actually by inclusion-exclusion, $|union| = \sum |S_i| - \sum |S_i \cap S_j| + \sum |S_i \cap S_j \cap S_k| - ...$, so $12 - |union| = \sum |S_i \cap S_j| - \sum |S_i \cap S_j \cap S_k| + ... \leq \sum |S_i \cap S_j|$).

So overlaps $\leq \sum_{\{u_i,u_j\} \subseteq N(v)} (c(u_i,u_j) - 1)$.

And we need overlaps $\leq 1$ for each $v$ (since $|union| \geq 11$).

Hmm wait, we need $|union| \geq 11$, so overlaps $\leq 12 - 11 = 1$.

And overlaps $\leq \sum (c(u_i,u_j) - 1)$. But overlaps could be less than this sum. So the constraint is overlaps $\leq 1$, which is a constraint on the actual overlaps, not directly on $\sum (c-1)$.

But we also need $|union| \geq 11$, and $|union| \leq 12$ (trivially). Also $|union| = 12 - \text{overlaps}$. 

Actually, I realize the constraint is just that $|union| \geq 11$, i.e., overlaps $\leq 1$. And overlaps $\leq \sum (c(u_i,u_j)-1)$, but overlaps could be much less if there are triple overlaps.

This is getting complicated. Let me try a more computational approach.

Let me think about what graphs on 16 vertices, 4-regular, diameter 2 look like.

Actually, I recall that the answer to the degree-diameter problem for $(4, 2)$ is indeed 15. The graph achieving this is related to the line graph of $K_{3,3}$ or some other construction. Let me think...

Actually, I think the answer might be 15. Let me try to prove $n \leq 15$ and construct a graph on 15 vertices.

**Construction for $n = 15$:**

Consider the graph known as the "Clebsch graph" or similar. Actually, the Clebsch graph has 16 vertices and is 5-regular. Not quite.

Let me think about the Petersen-like constructions. The Petersen graph has 10 vertices, 3-regular, diameter 2.

For degree 4, diameter 2: Let me think of a construction.

One known construction: Take $\mathbb{Z}_3 \times \mathbb{Z}_5 = \mathbb{Z}_{15}$. Connect each vertex $i$ to $i \pm 1, i \pm 4 \pmod{15}$ or some such circulant graph. Let me check if a circulant graph on 15 vertices with degree 4 and diameter 2 exists.

A circulant graph $C_{15}(S)$ where $S = \{a, b, 15-a, 15-b\}$ with $|S| = 4$ (so degree 4). We need diameter 2, meaning every element of $\mathbb{Z}_{15}$ can be written as a sum of at most 2 elements from $S \cup \{0\}$... actually, the distance from 0 to $x$ is the minimum number of elements from $S$ (with signs) that sum to $x$.

We need: $\{0\} \cup S \cup (S + S) = \mathbb{Z}_{15}$, where $S + S = \{s_1 + s_2 : s_1, s_2 \in S\}$ (allowing $s_1 = s_2$).

$|S| = 4$ (but as a set in $\mathbb{Z}_{15}$, $S = \{a, b, -a, -b\}$, so $|S| \leq 4$). $|S+S| \leq 4 \times 4 = 16$ but could be less. We need $1 + 4 + |S+S| \geq 15$, so $|S+S| \geq 10$.

Let me try $S = \{1, 5, 14, 10\}$ (i.e., $\pm 1, \pm 5$). Then $S + S$:
$1+1=2, 1+5=6, 1+14=0, 1+10=11$
$5+5=10, 5+14=4, 5+10=0$
$14+14=13, 14+10=9$
$10+10=5$

So $S+S = \{0, 2, 4, 5, 6, 9, 10, 11, 13\}$. And $S = \{1, 5, 10, 14\}$. So $\{0\} \cup S \cup (S+S) = \{0, 1, 2, 4, 5, 6, 9, 10, 11, 13, 14\}$. That's 11 elements, missing $\{3, 7, 8, 12\}$. Not enough.

Let me try $S = \{\pm 1, \pm 2\} = \{1, 2, 13, 14\}$. $S+S$:
$1+1=2, 1+2=3, 1+13=14, 1+14=0$
$2+2=4, 2+13=0, 2+14=1$
$13+13=11, 13+14=12$
$14+14=13$

$S+S = \{0, 1, 2, 3, 4, 11, 12, 13, 14\}$. $\{0\} \cup S \cup (S+S) = \{0,1,2,3,4,11,12,13,14\}$. Missing $\{5,6,7,8,9,10\}$. Not enough.

Let me try $S = \{\pm 3, \pm 5\} = \{3, 5, 10, 12\}$. $S+S$:
$3+3=6, 3+5=8, 3+10=13, 3+12=0$
$5+5=10, 5+10=0, 5+12=2$
$10+10=5, 10+12=7$
$12+12=9$

$S+S = \{0, 2, 5, 6, 7, 8, 9, 10, 13\}$. $\{0\} \cup S \cup (S+S) = \{0, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13\}$. Missing $\{1, 4, 11, 14\}$. Not enough.

Let me try $S = \{\pm 2, \pm 5\} = \{2, 5, 10, 13\}$. $S+S$:
$2+2=4, 2+5=7, 2+10=12, 2+13=0$
$5+5=10, 5+10=0, 5+13=3$
$10+10=5, 10+13=8$
$13+13=11$

$S+S = \{0, 3, 4, 5, 7, 8, 10, 11, 12\}$. $\{0\} \cup S \cup (S+S) = \{0, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13\}$. Missing $\{1, 6, 9, 14\}$. Not enough.

Let me try $S = \{\pm 1, \pm 4\} = \{1, 4, 11, 14\}$. $S+S$:
$1+1=2, 1+4=5, 1+11=12, 1+14=0$
$4+4=8, 4+11=0, 4+14=3$
$11+11=7, 11+14=10$
$14+14=13$

$S+S = \{0, 2, 3, 5, 7, 8, 10, 12, 13\}$. $\{0\} \cup S \cup (S+S) = \{0,1,2,3,4,5,7,8,10,11,12,13,14\}$. Missing $\{6, 9\}$. Close but not enough.

Let me try $S = \{\pm 1, \pm 3\} = \{1, 3, 12, 14\}$. $S+S$:
$1+1=2, 1+3=4, 1+12=13, 1+14=0$
$3+3=6, 3+12=0, 3+14=2$
$12+12=9, 12+14=11$
$14+14=13$

$S+S = \{0, 2, 4, 6, 9, 11, 13\}$. $\{0\} \cup S \cup (S+S) = \{0,1,2,3,4,6,9,11,12,13,14\}$. Missing $\{5,7,8,10\}$. Not enough.

Let me try $S = \{\pm 4, \pm 6\} = \{4, 6, 9, 11\}$. $S+S$:
$4+4=8, 4+6=10, 4+9=13, 4+11=0$
$6+6=12, 6+9=0, 6+11=2$
$9+9=3, 9+11=5$
$11+11=7$

$S+S = \{0, 2, 3, 5, 7, 8, 10, 12, 13\}$. $\{0\} \cup S \cup (S+S) = \{0,2,3,4,5,6,7,8,9,10,11,12,13\}$. Missing $\{1, 14\}$. Close!

Hmm, missing $\{1, 14\} = \{\pm 1\}$. So close.

Let me try $S = \{\pm 4, \pm 7\} = \{4, 7, 8, 11\}$. $S+S$:
$4+4=8, 4+7=11, 4+8=12, 4+11=0$
$7+7=14, 7+8=0, 7+11=3$
$8+8=1, 8+11=4$
$11+11=7$

$S+S = \{0, 1, 3, 4, 7, 8, 11, 12, 14\}$. $\{0\} \cup S \cup (S+S) = \{0,1,3,4,7,8,11,12,14\}$. Missing $\{2,5,6,9,10,13\}$. Not enough.

Let me try $S = \{\pm 2, \pm 7\} = \{2, 7, 8, 13\}$. $S+S$:
$2+2=4, 2+7=9, 2+8=10, 2+13=0$
$7+7=14, 7+8=0, 7+13=5$
$8+8=1, 8+13=6$
$13+13=11$

$S+S = \{0, 1, 4, 5, 6, 9, 10, 11, 14\}$. $\{0\} \cup S \cup (S+S) = \{0,1,2,4,5,6,7,8,9,10,11,13,14\}$. Missing $\{3, 12\}$. Close!

Missing $\{3, 12\} = \{\pm 3\}$.

Hmm, circulant graphs on 15 vertices seem to get close but not quite. Let me try non-circulant constructions.

Actually, let me reconsider. Maybe the answer is not 15. Let me look at this from a different angle.

Let me reconsider the problem. Maybe I should think about it more carefully.

Actually, wait. Let me reconsider whether the answer is 15 or something else. Let me think about known results.

The degree-diameter problem for $(\Delta, D) = (4, 2)$:
- Moore bound: 17
- No Moore graph exists (Moore graphs of diameter 2 exist only for degrees 2, 3, 7, and possibly 57)
- The largest known graph is... 

I believe the answer is 15. Let me try to find a construction.

One approach: Take the line graph of a suitable graph. The line graph $L(K_{3,3})$ has 9 vertices and is 4-regular. Its diameter is 2 (since $K_{3,3}$ has diameter 2 and line graphs of diameter-2 graphs... hmm, not necessarily).

Actually, let me think about this differently. 

Consider the graph $K_{1} + $ (some structure). No, let me think about specific constructions.

**Construction attempt: 15 vertices**

Take three copies of $K_5$ minus a perfect matching? No, that gives degree 3 within each copy.

Let me think about the "cocktail party graph" or other named graphs.

Actually, let me try a different approach. Consider the graph on $\mathbb{F}_2^4 \setminus \{0\}$ (15 vertices) where two vertices are adjacent iff their dot product (or some bilinear form) is 0 or 1.

Hmm, let me think about the Clebsch graph. The Clebsch graph (also called the folded 5-cube) has 16 vertices and is 5-regular. If we remove a perfect matching, we get a 4-regular graph on 16 vertices. Does it have diameter 2?

The Clebsch graph has diameter 2. Removing a perfect matching... the diameter might increase. Let me think.

The Clebsch graph: vertices are $\{0,1\}^4$ (16 vertices). Two vertices are adjacent iff they differ in exactly 1 coordinate OR exactly 4 coordinates (all coordinates). Wait, I need to recall the exact definition.

One definition: vertices are subsets of $\{1,2,3,4,5\}$ of even size (there are $2^4 = 16$ such subsets). Two vertices are adjacent iff their symmetric difference has size 4. The degree of each vertex: $|S|$ has even size, and we need $|S \triangle T| = 4$, so $|T| = |S| + 4 - 2|S \cap T|$... hmm, let me think differently.

Actually, the Clebsch graph can be defined as follows: vertices are $\{0,1\}^4$. Two vertices $u, v$ are adjacent iff $u \oplus v$ has Hamming weight 1 or 4. So each vertex has 4 neighbors at distance 1 (flip one bit) plus 1 neighbor at distance 4 (flip all bits) = degree 5.

If we remove the "flip all bits" edges (which form a perfect matching), we get the 4-dimensional hypercube $Q_4$, which has diameter 4. That's too large.

Alternatively, remove a different perfect matching. But the Clebsch graph is edge-transitive, so removing any perfect matching gives an isomorphic graph.

Hmm, so that doesn't work directly.

Let me think about other constructions.

**Construction using projective planes or other combinatorial designs:**

The Petersen graph (10 vertices, 3-regular, diameter 2) is the complement of the line graph of $K_5$.

For degree 4, diameter 2: 

Let me try the following: Take the graph whose vertices are the 15 points of $PG(3,2)$ (the projective 3-space over $\mathbb{F}_2$, which has $(2^4-1)/(2-1) = 15$ points). Connect two points if they are on a common line... but in $PG(3,2)$, every two points determine a line, so this gives $K_{15}$. Not useful.

Instead, connect two points if they are "close" in some sense. In $PG(3,2)$, each line has 3 points, each point is on 7 lines, there are 35 lines.

Let me try: vertices are the 15 points of $PG(3,2)$. Two points are adjacent iff they are NOT on a common line of some fixed spread. A spread in $PG(3,2)$ is a set of 5 disjoint lines covering all 15 points. If we fix a spread, two points are adjacent iff they are on different lines of the spread. But then each point is adjacent to $15 - 3 = 12$ other points (those not on its line in the spread). That's degree 12, too high.

Let me try the opposite: two points adjacent iff they ARE on the same line of a fixed spread. Each line has 3 points, so each point is adjacent to 2 others. Degree 2, too low.

Let me try a different structure. How about: vertices are the 15 points of $PG(3,2)$, and two points are adjacent iff they differ by a specific vector. Since $PG(3,2)$ points are nonzero vectors in $\mathbb{F}_2^4$, we can define adjacency by $u \oplus v \in S$ for some set $S$ of 4 nonzero vectors. This is essentially a Cayley graph on $\mathbb{F}_2^4 \setminus \{0\}$... but that's not a group.

Actually, $\mathbb{F}_2^4 \setminus \{0\}$ is not a group under XOR. But we can consider the Cayley graph on $\mathbb{F}_2^4$ (including 0) with connection set $S$, and then remove vertex 0. If $S$ has 4 elements and the Cayley graph on $\mathbb{F}_2^4$ has degree 4, removing vertex 0 gives a graph on 15 vertices where the 4 neighbors of 0 now have degree 3.

Hmm, that doesn't give a 4-regular graph. But the problem only requires max degree 4, not exactly 4. So some vertices can have degree 3.

Let me think about this. Take the Cayley graph on $\mathbb{Z}_2^4$ with connection set $S = \{e_1, e_2, e_3, e_4\}$ (the 4 standard basis vectors). This is the 4-cube $Q_4$, which has diameter 4. Too large.

Take $S = \{e_1, e_2, e_3, e_4, e_1+e_2+e_3+e_4\}$. This is the Clebsch graph (degree 5, diameter 2, 16 vertices). If we remove vertex 0, we get 15 vertices, but 4 of them (the basis vectors) lose a neighbor and have degree 4, while the rest have degree 5. But we need max degree 4, so this doesn't work.

What if we use the Clebsch graph and remove a perfect matching to get degree 4, then remove a vertex? The Clebsch graph minus a perfect matching is $Q_4$ (as computed above), which has diameter 4. Not useful.

Let me think differently. Maybe I should use a non-Cayley construction.

**Construction: 15 vertices, degree ≤ 4, diameter 2**

Let me try to build one explicitly. 

Consider 15 vertices arranged as follows. Take a vertex $v$ connected to 4 vertices $a, b, c, d$. Each of $a, b, c, d$ needs to reach the remaining 10 vertices within distance 2 (distance 1 from $a,b,c,d$). Each of $a, b, c, d$ has 3 more edges (degree 4, one used for $v$). So they have $4 \times 3 = 12$ edge-endpoints to distribute among the 10 remaining vertices. We need all 10 to be covered, with at most 2 "wasted" (going to vertices already covered or to each other).

This is tight but might work. Let me try to construct it.

Vertices: $v, a, b, c, d, w_1, \ldots, w_{10}$.

$v$ connects to $a, b, c, d$.
$a$ connects to $v, w_1, w_2, w_3$ (say).
$b$ connects to $v, w_4, w_5, w_6$.
$c$ connects to $v, w_7, w_8, w_9$.
$d$ connects to $v, w_{10}, ?, ?$.

$d$ has 2 more edges. If $d$ connects to two of $w_1, \ldots, w_9$, say $w_1, w_4$, then:
- $w_{10}$ is at distance 2 from $v$ (via $d$). ✓
- All $w_i$ are at distance 2 from $v$. ✓
- But we need all pairs to be at distance ≤ 2.

Now, $w_1, \ldots, w_{10}$ have degree 1 so far (each connected to one of $a,b,c,d$), except $w_1$ and $w_4$ which have degree 2. They can have up to 4 edges total, so each has 2-3 more edges to add.

We need: every pair of $w_i, w_j$ either adjacent or sharing a common neighbor. Their common neighbors could be among $\{a,b,c,d\}$ or among other $w_k$.

$w_1$ and $w_2$ share $a$ as common neighbor. ✓
$w_1$ and $w_3$ share $a$. ✓
$w_2$ and $w_3$ share $a$. ✓
$w_4, w_5, w_6$ share $b$. ✓
$w_7, w_8, w_9$ share $c$. ✓
$w_1$ and $w_4$ share $d$ (since $d$ connects to both). ✓

But $w_1$ and $w_5$: $w_1$ is connected to $a, d$; $w_5$ is connected to $b$. Common neighbors? None so far. So we need $w_1$ and $w_5$ to be adjacent, or share a common neighbor among the $w_k$.

This is getting complex. Let me try to think about it more systematically.

Actually, let me just try to check: is the answer 15? Let me try to prove the upper bound $n \leq 15$.

**Upper bound proof attempt:**

Assume $G$ has $n$ vertices, max degree 4, diameter 2. We want to show $n \leq 15$.

We've shown $n \leq 17$ (Moore bound). We need to rule out $n = 16$ and $n = 17$.

$n = 17$: requires a Moore graph, which doesn't exist for degree 4. ✓

$n = 16$: Need to show no 4-regular (or max-degree-4) graph on 16 vertices with diameter 2 exists.

Hmm, but actually, the graph doesn't need to be 4-regular. It just needs max degree 4. So some vertices could have degree < 4. But if $n = 16$ and we want diameter 2 with max degree 4, having lower-degree vertices makes it harder (fewer connections), so intuitively we'd want all degrees to be 4. But let me not assume that.

Let me try to rule out $n = 16$.

For any vertex $v$ with degree $d(v) \leq 4$, the number of vertices at distance $\leq 2$ from $v$ is at most $1 + d(v) + \sum_{u \sim v}(d(u) - 1) \leq 1 + d(v) + d(v) \cdot 3 = 1 + 4d(v)$. For diameter 2, this must be $\geq 16$, so $1 + 4d(v) \geq 16$, giving $d(v) \geq 4$ (since $d(v)$ is an integer, $d(v) \geq 4$). But $d(v) \leq 4$, so $d(v) = 4$ for all $v$.

Wait, that's not quite right. The bound $1 + d(v) + \sum_{u \sim v}(d(u)-1)$ counts the maximum number of distinct vertices at distance $\leq 2$, but there could be overlaps. The actual number is $\leq$ this bound. For diameter 2, we need the actual number $= n = 16$, so $16 \leq 1 + d(v) + \sum_{u \sim v}(d(u)-1)$.

Now, $\sum_{u \sim v}(d(u)-1) \leq d(v) \cdot 3$ (since $d(u) \leq 4$). So $16 \leq 1 + d(v) + 3d(v) = 1 + 4d(v)$, giving $d(v) \geq 15/4 = 3.75$, so $d(v) \geq 4$. Combined with $d(v) \leq 4$, we get $d(v) = 4$ for all $v$.

So if $n = 16$, the graph must be 4-regular. Moreover, for each $v$, $16 \leq 1 + 4 + \sum_{u \sim v}(d(u)-1) = 5 + \sum_{u \sim v} 3 = 5 + 12 = 17$. So we need $16 \leq 17$, which is fine, but it means at most 1 "collision" (overlap) in the BFS from each vertex.

More precisely, for each $v$, the 4 neighbors $u_1, \ldots, u_4$ each have 3 neighbors other than $v$. The 12 vertices $N(u_i) \setminus \{v\}$ (counting with multiplicity) must cover at least 11 distinct vertices (the 11 vertices at distance 2 from $v$). So at most 1 overlap.

An overlap occurs when some vertex $w$ is a neighbor of two different $u_i, u_j$. This means $w, u_i, v, u_j$ form a path, i.e., $u_i$ and $u_j$ share a common neighbor $w \neq v$.

Also, if $u_i$ and $u_j$ are adjacent (for $i \neq j$), then $u_j \in N(u_i) \setminus \{v\}$ and $u_i \in N(u_j) \setminus \{v\}$, but these are different vertices, so this doesn't create an overlap. However, it does "use up" a slot: $u_j$ is one of the 3 neighbors of $u_i$ other than $v$, and $u_j$ is at distance 1 from $v$, not distance 2. So $u_j$ is "wasted" as a distance-2 vertex.

Wait, I need to be more careful. The 12 endpoints $N(u_i) \setminus \{v\}$ include:
- Other neighbors of $v$ (if $u_i$ and $u_j$ are adjacent, then $u_j \in N(u_i) \setminus \{v\}$)
- Vertices at distance 2 from $v$
- $v$ itself is excluded

So the 12 endpoints consist of some neighbors of $v$ (distance 1) and some distance-2 vertices. Let $t_v$ = number of edges among the neighbors of $v$ (i.e., triangles through $v$). Then $t_v$ of the 12 endpoints are neighbors of $v$ (at distance 1), and $12 - t_v$ are potential distance-2 vertices. But there could also be overlaps among the distance-2 vertices.

The number of distinct distance-2 vertices = $12 - t_v - (\text{overlaps among distance-2})$. We need this to be $\geq 11$.

So $12 - t_v - \text{overlaps} \geq 11$, i.e., $t_v + \text{overlaps} \leq 1$.

So for each vertex $v$: either $t_v = 0$ and overlaps $\leq 1$, or $t_v = 1$ and overlaps $= 0$.

$t_v = $ number of triangles through $v$. Overlaps = number of pairs $\{u_i, u_j\} \subseteq N(v)$ that share a common neighbor $w \notin N(v) \cup \{v\}$ (i.e., $w$ is at distance 2 from $v$ and is a common neighbor of $u_i$ and $u_j$).

Wait, I need to be more careful. An "overlap" in the distance-2 sets means a vertex $w$ at distance 2 from $v$ that is a neighbor of two different $u_i, u_j$. The number of such overlaps (counting each $w$ once for each pair it creates) is what matters. But actually, if $w$ is a neighbor of $u_i, u_j, u_k$ (three of them), that's even more overlap.

Let me define: for each $v$, let $o_v$ = number of "wasted" slots = $12 - |\bigcup_i (N(u_i) \setminus \{v\})| - t_v$... no, let me recompute.

$|\bigcup_i (N(u_i) \setminus \{v\})|$ = number of distinct vertices that are neighbors of some $u_i$ and are not $v$. This includes:
- Neighbors of $v$ that are also neighbors of some $u_i$ (these are at distance 1)
- Vertices at distance 2 from $v$

The number of distance-2 vertices = $|\bigcup_i (N(u_i) \setminus \{v\})| - |\{u_j : u_j \in N(u_i) \text{ for some } i \neq j\}|$.

Hmm, this is getting complicated. Let me just use the constraint: $t_v + \text{(extra overlaps)} \leq 1$ where extra overlaps account for distance-2 vertices being shared.

Actually, let me re-derive. The total number of "slots" is 12 (each $u_i$ contributes 3 neighbors other than $v$). These 12 slots are filled with:
- $t_v$ slots are filled with other neighbors of $v$ (each triangle $v-u_i-u_j$ means $u_j$ is in $N(u_i) \setminus \{v\}$, contributing 1 slot; and $u_i$ is in $N(u_j) \setminus \{v\}$, contributing another slot. So each triangle through $v$ uses 2 slots for distance-1 vertices.)

Wait, I think I was wrong. Let me recount. If $u_i$ and $u_j$ are both neighbors of $v$ and they are adjacent, then:
- $u_j \in N(u_i) \setminus \{v\}$ (one slot of $u_i$ is used for $u_j$, which is at distance 1 from $v$)
- $u_i \in N(u_j) \setminus \{v\}$ (one slot of $u_j$ is used for $u_i$, which is at distance 1 from $v$)

So each edge among neighbors of $v$ uses 2 slots for distance-1 vertices. With $t_v$ edges among neighbors, $2t_v$ slots are used for distance-1 vertices.

The remaining $12 - 2t_v$ slots are for distance-2 vertices. If all are distinct, we get $12 - 2t_v$ distance-2 vertices. We need $\geq 11$ distance-2 vertices (since $n = 16 = 1 + 4 + 11$).

So $12 - 2t_v - \text{overlaps} \geq 11$, i.e., $2t_v + \text{overlaps} \leq 1$.

Since $t_v \geq 0$ and overlaps $\geq 0$ are integers, we need $2t_v + \text{overlaps} \leq 1$, which means:
- $t_v = 0$ and overlaps $\leq 1$, OR
- $t_v = 0$ and overlaps $= 0$ (the only possibility since $2t_v \leq 1$ requires $t_v = 0$).

Wait, $2t_v \leq 1$ requires $t_v = 0$. So $t_v = 0$ for all $v$, and overlaps $\leq 1$.

$t_v = 0$ for all $v$ means the graph is triangle-free!

So if $n = 16$, the graph is 4-regular, triangle-free, and for each vertex, at most 1 pair of its neighbors share a common neighbor at distance 2.

A 4-regular triangle-free graph on 16 vertices. The number of edges is 32. By Mantel's theorem, a triangle-free graph on 16 vertices has at most $\lfloor 16^2/4 \rfloor = 64$ edges. So 32 is fine.

Now, "overlaps $\leq 1$ for each $v$": for each $v$, at most 1 pair of its 4 neighbors share a common neighbor $w$ at distance 2 from $v$. 

The number of pairs of neighbors of $v$ is $\binom{4}{2} = 6$. At most 1 of these 6 pairs shares a common neighbor at distance 2.

Now let me count the total number of 4-cycles in the graph. A 4-cycle $v - u_i - w - u_j - v$ corresponds to a pair $\{u_i, u_j\}$ of neighbors of $v$ sharing a common neighbor $w$ at distance 2. The number of such 4-cycles through $v$ is the number of pairs $\{u_i, u_j\}$ with a common neighbor at distance 2, summed over all such $w$... actually, each 4-cycle $v - u_i - w - u_j - v$ is counted once for vertex $v$.

But wait, a 4-cycle $a - b - c - d - a$ is counted 4 times in total (once for each vertex as $v$). Hmm, no. For vertex $a$, the 4-cycle $a - b - c - d - a$ means $b, d$ are neighbors of $a$ sharing common neighbor $c$. So it's counted once for $a$. Similarly for $b$ (neighbors $a, c$ sharing $d$), $c$, $d$. So each 4-cycle is counted 4 times total (once for each vertex).

The total count of "overlap pairs" across all vertices = $\sum_v (\text{number of pairs of neighbors of } v \text{ sharing a distance-2 common neighbor})$.

But this isn't exactly the number of 4-cycles, because a pair $\{u_i, u_j\}$ could share multiple common neighbors at distance 2, and each would be a separate 4-cycle.

Let $f(v)$ = number of 4-cycles through $v$ (where $v$ is one vertex of the 4-cycle). Then $f(v) \leq 1$ for all $v$ (since at most 1 overlap, and each overlap is at least one 4-cycle, but could there be a pair sharing 2 common neighbors? If $u_i, u_j$ share 2 common neighbors $w_1, w_2$ at distance 2 from $v$, that's 2 overlaps, which violates overlaps $\leq 1$. So each overlap is exactly 1, meaning each pair shares at most 1 common neighbor at distance 2, and at most 1 pair does.)

So $f(v) \leq 1$ for all $v$. The total number of 4-cycles $C_4 = \frac{1}{4} \sum_v f(v) \leq \frac{16}{4} = 4$.

Now, let me also count 4-cycles using the common neighbor count. The number of 4-cycles = $\sum_{\{x,y\}} \binom{c(x,y)}{2}$ where the sum is over all pairs $\{x,y\}$ (both edges and non-edges) and $c(x,y)$ is the number of common neighbors.

Wait, a 4-cycle $a - b - c - d - a$ has two "diagonals": $\{a,c\}$ and $\{b,d\}$. The 4-cycle corresponds to $a, c$ having common neighbors $b, d$, i.e., $c(a,c) \geq 2$. Specifically, the number of 4-cycles = $\sum_{\{x,y\}} \binom{c(x,y)}{2}$.

We have $\sum_{\{x,y\}} c(x,y) = \sum_v \binom{d(v)}{2} = 16 \cdot 6 = 96$ (since 4-regular).

The graph is triangle-free, so for edges, $c(x,y) = 0$ (no common neighbors for adjacent vertices in a triangle-free graph). Wait, that's not right. $c(x,y)$ for an edge $xy$ counts common neighbors of $x$ and $y$. In a triangle-free graph, adjacent vertices have no common neighbors (a common neighbor would form a triangle). So $c(x,y) = 0$ for all edges.

So $\sum_{\{x,y\} \text{ non-edge}} c(x,y) = 96$. The number of non-edges is $120 - 32 = 88$. Each non-edge has $c(x,y) \geq 1$ (diameter 2). So $\sum c(x,y) \geq 88$, and $\sum c(x,y) = 96$, so the "excess" is $96 - 88 = 8$.

The number of 4-cycles = $\sum_{\text{non-edges}} \binom{c(x,y)}{2}$. Since $\sum c(x,y) = 96$ over 88 non-edges, and each $c \geq 1$:

$\sum \binom{c}{2} = \sum \frac{c(c-1)}{2} = \frac{1}{2}\sum c^2 - \frac{1}{2}\sum c = \frac{1}{2}\sum c^2 - 48$.

To minimize $\sum \binom{c}{2}$ given $\sum c = 96$ and each $c \geq 1$ over 88 terms: we want to spread the excess as evenly as possible. With 88 terms summing to 96, we have 8 excess. The minimum of $\sum \binom{c}{2}$ is achieved when 8 terms have $c = 2$ and 80 terms have $c = 1$: $\sum \binom{c}{2} = 8 \cdot 1 + 80 \cdot 0 = 8$.

So the number of 4-cycles $\geq 8$. But we showed the number of 4-cycles $\leq 4$. Contradiction!

Therefore $n = 16$ is impossible, and $n \leq 15$.

Wait, let me double-check this. The number of 4-cycles is $\sum_{\{x,y\}} \binom{c(x,y)}{2}$ where the sum is over ALL pairs, not just non-edges. But for edges, $c(x,y) = 0$ (triangle-free), so $\binom{0}{2} = 0$. So the sum is indeed over non-edges only.

And we showed:
- Number of 4-cycles $\leq 4$ (from $f(v) \leq 1$ for all $v$)
- Number of 4-cycles $\geq 8$ (from the counting argument)

Contradiction. So $n = 16$ is impossible.

Therefore $n \leq 15$.

Now I need to construct a graph on 15 vertices with max degree 4 and diameter 2.

**Construction for $n = 15$:**

Let me try the following. Consider the Petersen graph (10 vertices, 3-regular, diameter 2) and add 5 more vertices.

Actually, let me think about a cleaner construction.

Consider the graph $G$ on 15 vertices defined as follows. Take the complete graph $K_6$ and remove a perfect matching (getting the cocktail party graph on 6 vertices, which is 4-regular). This has 6 vertices, degree 4, diameter 2. But we need 15 vertices.

Hmm, let me think about this differently.

Let me try a circulant graph again, but more carefully.

$C_{15}(S)$ with $S = \{1, 4, 11, 14\} = \{\pm 1, \pm 4\}$. We computed: $\{0\} \cup S \cup (S+S) = \{0,1,2,3,4,5,7,8,10,11,12,13,14\}$, missing $\{6, 9\}$.

$S = \{\pm 2, \pm 7\} = \{2, 7, 8, 13\}$: missing $\{3, 12\}$.

$S = \{\pm 4, \pm 6\} = \{4, 6, 9, 11\}$: missing $\{1, 14\}$.

None of the circulant graphs on 15 vertices with degree 4 seem to work. Let me try a non-circulant construction.

**Construction using the line graph of $K_{3,3}$ plus extensions:**

$L(K_{3,3})$ has 9 vertices, is 4-regular, and has diameter 2 (I think). Let me verify: $K_{3,3}$ has 9 edges. Two edges of $K_{3,3}$ are adjacent in the line graph iff they share a vertex. The diameter of $L(K_{3,3})$: two edges $e_1, e_2$ of $K_{3,3}$ are at distance 1 if they share a vertex, distance 2 if they don't share a vertex but there's an edge sharing a vertex with both. In $K_{3,3}$, any two edges either share a vertex or are disjoint. If disjoint, say $e_1 = (a_1, b_1)$ and $e_2 = (a_2, b_2)$, then the edge $(a_1, b_2)$ shares a vertex with both. So diameter is 2. ✓

So $L(K_{3,3})$ is a 4-regular graph on 9 vertices with diameter 2. Can we extend it to 15 vertices?

We need to add 6 more vertices, each with degree $\leq 4$, and maintain diameter 2.

Each new vertex needs to be at distance $\leq 2$ from all 14 other vertices. If a new vertex $w$ has degree $d \leq 4$, it's at distance 1 from $d$ vertices and needs to be at distance 2 from the remaining $14 - d$ vertices (via its neighbors). Each neighbor of $w$ can "cover" at most 3 new vertices (its other neighbors). So $d \cdot 3 \geq 14 - d$, giving $4d \geq 14$, $d \geq 4$. So $d = 4$.

Each new vertex has degree 4 and its 4 neighbors must cover all 10 non-neighbors (each neighbor covers at most 3, so $4 \times 3 = 12 \geq 10$). This is feasible but tight.

This is getting complicated. Let me try a different, cleaner construction.

**Construction: The graph $G$ on $\{0, 1, \ldots, 14\}$ with a specific edge set.**

Let me try a computer-free approach. Consider the following graph:

Take 5 groups of 3 vertices: $\{a_i, b_i, c_i\}$ for $i = 0, 1, 2, 3, 4$ (indices mod 5).

Within each group, form a triangle: $a_i - b_i - c_i - a_i$. (3 edges per group, 15 edges total)
Between groups: connect $a_i$ to $a_{i+1}$ and $a_{i-1}$ (forming a 5-cycle on the $a$'s). Similarly for $b$'s and $c$'s. (5 edges per cycle, 15 edges total)

Total edges: 30. Each vertex has degree 4 (2 within group + 2 between groups). 4-regular on 15 vertices.

Is the diameter 2? Let's check. Take $a_0$ and $b_2$ (different groups, different types).
- $a_0$'s neighbors: $b_0, c_0, a_1, a_4$.
- $b_2$'s neighbors: $a_2, c_2, b_1, b_3$.
- Common neighbors? $a_0$'s neighbors are $\{b_0, c_0, a_1, a_4\}$, $b_2$'s neighbors are $\{a_2, c_2, b_1, b_3\}$. No intersection. So distance > 2.

This doesn't work. The diameter is more than 2.

Let me try a different construction.

**Construction: Generalized Petersen graph or similar.**

The generalized Petersen graph $GP(5, 2)$ is the Petersen graph (10 vertices, 3-regular, diameter 2). Not enough vertices.

$GP(7, 2)$: 14 vertices, 3-regular. Diameter? The generalized Petersen graph $GP(n, k)$ has $2n$ vertices. $GP(7, 2)$ has diameter... I think it's 3 for most cases. Not useful.

Let me try yet another approach.

**Construction: Cayley graph on $\mathbb{Z}_{15}$ with a non-standard connection set.**

We need $S \subseteq \mathbb{Z}_{15} \setminus \{0\}$ with $|S| \leq 4$, $S = -S$ (for undirected), and $\{0\} \cup S \cup (S+S) = \mathbb{Z}_{15}$.

We need $|S| = 4$ (as shown, degree must be 4 for $n = 15$... wait, actually for $n = 15$, the degree doesn't have to be 4 for all vertices. Let me recheck.

For $n = 15$, the constraint is $15 \leq 1 + 4d(v)$, so $d(v) \geq 14/4 = 3.5$, so $d(v) \geq 4$. Since $d(v) \leq 4$, we need $d(v) = 4$ for all $v$. So the graph must be 4-regular.

Wait, that's the same argument as before. $15 \leq 1 + 4d(v)$ gives $d(v) \geq 3.5$, so $d(v) = 4$. So for $n = 15$, the graph is also 4-regular.

Hmm, but the bound $1 + 4d(v)$ assumed all neighbors have degree 4. If some neighbors have degree $< 4$, the bound is even tighter. But we just showed all vertices must have degree 4, so the bound is $1 + 4 \cdot 4 = 17 \geq 15$. OK so it's not as tight for $n = 15$.

For $n = 15$: $1 + d(v) + \sum_{u \sim v}(d(u)-1) = 1 + 4 + 12 = 17 \geq 15$. So we have $17 - 15 = 2$ "slack". This means up to 2 collisions per vertex.

OK so for $n = 15$, the constraints are less tight. Let me go back to trying circulant graphs.

For a circulant graph $C_{15}(S)$ with $|S| = 4$ and $S = -S$, we need $\{0\} \cup S \cup (S+S) = \mathbb{Z}_{15}$, i.e., $S \cup (S+S) \supseteq \mathbb{Z}_{15} \setminus \{0\}$.

$|S| = 4$, $|S+S| \leq 10$ (since $S$ has 4 elements, $S+S$ has at most $4 \times 4 = 16$ elements, but with $S = -S$, many coincide). We need $|S \cup (S+S)| \geq 14$.

Let me be more systematic. $S = \{a, -a, b, -b\}$ with $0 < a < b < 15/2$, so $a \in \{1, \ldots, 7\}$, $b \in \{a+1, \ldots, 7\}$.

$S + S = \{2a, 0, a+b, a-b, -a+b, -a-b, 0, 2b, b-a, -2b\}$... let me just compute $S+S$ for each pair.

$S = \{a, -a, b, -b\}$. $S + S = \{s_1 + s_2 : s_1, s_2 \in S\}$.

The elements: $2a, 0, a+b, a-b, -2a, -a+b, -a-b, 0, 2b, b-a, -b+a, -b-a, -2b, 0, 0$.

Distinct elements (mod 15): $\{0, 2a, -2a, 2b, -2b, a+b, a-b, -a+b, -a-b\}$. Note $a-b = -(b-a)$ and $-a+b = b-a$, so $a-b$ and $-a+b$ are the same up to sign. Also $-a-b = -(a+b)$.

So $S+S = \{0, \pm 2a, \pm 2b, \pm(a+b), \pm(a-b)\}$. That's at most 9 elements (including 0).

$S \cup (S+S) = \{\pm a, \pm b\} \cup \{0, \pm 2a, \pm 2b, \pm(a+b), \pm(a-b)\}$.

We need this to be all of $\mathbb{Z}_{15}$. $\mathbb{Z}_{15}$ has 15 elements. $|S \cup (S+S)| \leq 4 + 9 = 13$ (but there could be overlaps, e.g., $2a = b$ etc.). So $|S \cup (S+S)| \leq 13 < 14$. 

Wait, that means it's impossible! We can cover at most 13 elements (including 0), but we need 14 (all nonzero elements). So no circulant graph on 15 vertices with degree 4 and diameter 2 exists!

Hmm, but that's only for circulant graphs. Non-circulant graphs might work.

Let me reconsider. $|S \cup (S+S)| \leq 4 + 9 = 13$, but we need 15 elements (all of $\mathbb{Z}_{15}$). Even with 0 included, $13 < 15$. So circulant graphs can't work.

OK so I need a non-circulant construction. Let me think more carefully.

**Construction attempt: 15 vertices, 4-regular, diameter 2.**

Let me try the following approach. Consider the complement: a 4-regular graph on 15 vertices has complement that is 10-regular on 15 vertices. The diameter-2 condition on $G$ means: every non-edge of $G$ (i.e., every edge of $\bar{G}$) has a common neighbor in $G$. In terms of $\bar{G}$: for every edge of $\bar{G}$, the two endpoints have a common non-neighbor in $\bar{G}$ (i.e., a vertex not adjacent to either in $\bar{G}$, meaning adjacent to both in $G$).

Hmm, this doesn't simplify things.

Let me try to construct the graph directly.

Idea: Use the structure of $PG(3, 2)$ (projective 3-space over $\mathbb{F}_2$). It has 15 points and 35 lines, each line has 3 points, each point is on 7 lines.

Define $G$ as follows: two points are adjacent iff they are on a common line from a specific set of lines. We need each point to be on exactly 4 lines from this set (degree 4), and the graph to have diameter 2.

A "spread" in $PG(3,2)$ is a set of 5 mutually disjoint lines covering all 15 points. Each point is on exactly 1 line of the spread.

A "1-factorization" type structure: If we take two disjoint spreads, each point is on 2 lines, giving degree $2 \times 2 = 4$ (each line contributes 2 neighbors). Two spreads give 10 lines, each point on 2 lines, degree 4. 

Does this graph have diameter 2? Two points $P, Q$ are at distance 1 if they're on a common line from either spread. They're at distance 2 if there's a point $R$ such that $P, R$ are on a spread line and $Q, R$ are on a spread line.

In a spread, two points are on the same line iff they're in the same "group" of 3. So with two spreads, $P$ and $Q$ are adjacent iff they're in the same group in spread 1 or spread 2.

$P$ is in a group of 3 in spread 1 (say $\{P, P_1, P_2\}$) and a group of 3 in spread 2 (say $\{P, P_3, P_4\}$). $P$'s neighbors: $P_1, P_2, P_3, P_4$ (degree 4). ✓

For diameter 2: $P$ and $Q$ are non-adjacent iff they're in different groups in both spreads. We need a common neighbor: a point $R$ in $P$'s group in some spread and in $Q$'s group in some spread. I.e., $R$ is in $P$'s group in spread 1 and $Q$'s group in spread 2, or in $P$'s group in spread 2 and $Q$'s group in spread 1.

$P$'s group in spread 1: $\{P, P_1, P_2\}$. $Q$'s group in spread 2: $\{Q, Q_3, Q_4\}$. We need $\{P, P_1, P_2\} \cap \{Q, Q_3, Q_4\} \neq \emptyset$ or $\{P, P_3, P_4\} \cap \{Q, Q_1, Q_2\} \neq \emptyset$.

This is not guaranteed for arbitrary spreads. We need the spreads to be chosen carefully.

This is related to the concept of a "Latin square" or "resolvable design." Two spreads in $PG(3,2)$ that are "orthogonal" in some sense.

Actually, $PG(3,2)$ has a resolution into 3 disjoint spreads (a "parallelism" or "resolution"). If we take 2 of the 3 spreads, we get a 4-regular graph. Let me check if it has diameter 2.

With a parallelism (3 disjoint spreads), each pair of points is on exactly one line of $PG(3,2)$, and that line belongs to exactly one spread. So two points are in the same group in exactly one of the 3 spreads.

If we take spreads 1 and 2: $P$ and $Q$ are adjacent iff they're in the same group in spread 1 or spread 2. They're non-adjacent iff they're in the same group only in spread 3 (and different groups in spreads 1 and 2).

For non-adjacent $P, Q$ (same group in spread 3, different in spreads 1 and 2): we need a common neighbor. $P$'s neighbors are the 2 other points in $P$'s spread-1 group and 2 other points in $P$'s spread-2 group. $Q$'s neighbors are similar. A common neighbor $R$ must be in $P$'s group in spread 1 or 2, and in $Q$'s group in spread 1 or 2.

$P$'s spread-1 group: $\{P, A, B\}$. $P$'s spread-2 group: $\{P, C, D\}$. $Q$'s spread-1 group: $\{Q, E, F\}$. $Q$'s spread-2 group: $\{Q, G, H\}$.

Common neighbors: $\{A, B, C, D\} \cap \{E, F, G, H\}$. We need this to be non-empty.

Is this guaranteed? Not obviously. Let me think about the structure more carefully.

In $PG(3,2)$, a parallelism (resolution into 3 spreads) exists. The 15 points can be identified with $\mathbb{F}_2^4 \setminus \{0\}$. A spread is a set of 5 lines covering all points, where a line is $\{x, y, x+y\}$ for linearly independent $x, y$.

A parallelism partitions the 35 lines into 3 spreads of 5 lines each... wait, $3 \times 5 = 15 \neq 35$. That's wrong. A spread has 5 lines, and there are 35 lines total, so a parallelism would need $35/5 = 7$ spreads. But a parallelism in $PG(3,2)$ is a partition of the 35 lines into 7 spreads (each of 5 lines), not 3.

Wait, I'm confusing things. A spread in $PG(3, q)$ is a set of $q^2 + 1$ lines that partition the points. For $q = 2$, that's 5 lines covering 15 points. A parallelism is a partition of all $q^2(q^2+1)(q-1)/... $ hmm, the total number of lines in $PG(3,2)$ is $\frac{(2^4-1)(2^3-1)}{(2^2-1)(2-1)} \cdot ... $ let me just compute: the number of lines in $PG(3,2)$ is $\binom{15}{2}/3 \cdot ... $ no. Each line has 3 points, each pair of points determines a unique line, so the number of lines is $\binom{15}{2}/\binom{3}{2} = 105/3 = 35$. A spread has 5 lines, so a parallelism has $35/5 = 7$ spreads.

So a parallelism in $PG(3,2)$ has 7 spreads. If we take 2 of the 7 spreads, we get a 4-regular graph on 15 vertices. The question is whether it has diameter 2.

Two points $P, Q$ are in the same group (line) in exactly one of the 7 spreads (since the spreads partition all 35 lines, and each pair determines one line). If we use spreads 1 and 2, then $P, Q$ are adjacent iff their line is in spread 1 or spread 2. Non-adjacent iff their line is in one of spreads 3-7.

For non-adjacent $P, Q$: we need a common neighbor. $P$'s neighbors are the 4 points sharing a line with $P$ in spreads 1 or 2. Similarly for $Q$. A common neighbor $R$ shares a line with $P$ in spread 1 or 2, and shares a line with $Q$ in spread 1 or 2.

This is equivalent to: the line $PR$ is in spread 1 or 2, and the line $QR$ is in spread 1 or 2.

$P$ has 2 lines in spread 1 (wait, no—$P$ is on exactly 1 line in each spread, since spreads partition the points). So $P$ is on 1 line in spread 1 and 1 line in spread 2, giving 4 neighbors.

For a common neighbor $R$: $R$ is on $P$'s spread-1 line or $P$'s spread-2 line, AND $R$ is on $Q$'s spread-1 line or $Q$'s spread-2 line.

$P$'s spread-1 line: $L_1(P) = \{P, P_1, P_2\}$.
$P$'s spread-2 line: $L_2(P) = \{P, P_3, P_4\}$.
$Q$'s spread-1 line: $L_1(Q) = \{Q, Q_1, Q_2\}$.
$Q$'s spread-2 line: $L_2(Q) = \{Q, Q_3, Q_4\}$.

Common neighbors: $(L_1(P) \cup L_2(P)) \cap (L_1(Q) \cup L_2(Q)) \setminus \{P, Q\}$.

$= (L_1(P) \cap L_1(Q)) \cup (L_1(P) \cap L_2(Q)) \cup (L_2(P) \cap L_1(Q)) \cup (L_2(P) \cap L_2(Q))$.

Each intersection is either empty or a single point (since two lines in $PG(3,2)$ meet in 0 or 1 points; if they're in the same spread, they're disjoint; if in different spreads, they might meet in 1 point).

$L_1(P)$ and $L_1(Q)$ are in the same spread (spread 1), so they're either the same line (if $P, Q$ are on the same spread-1 line, but then they'd be adjacent) or disjoint. Since $P, Q$ are non-adjacent, $L_1(P) \neq L_1(Q)$, so $L_1(P) \cap L_1(Q) = \emptyset$.

Similarly, $L_2(P) \cap L_2(Q) = \emptyset$.

So common neighbors come from $L_1(P) \cap L_2(Q)$ and $L_2(P) \cap L_1(Q)$, each of which is 0 or 1 point.

We need at least one of these to be non-empty. Is this guaranteed?

$L_1(P) \cap L_2(Q)$: $L_1(P)$ is a line in spread 1, $L_2(Q)$ is a line in spread 2. Two lines from different spreads in $PG(3,2)$ meet in 0 or 1 point. They meet in 1 point iff they're not skew.

In $PG(3,2)$, two lines either meet in 1 point or are skew (meet in 0 points). The number of lines skew to a given line: total lines = 35, lines meeting a given line = (lines through each point of the line) - (the line itself counted 3 times) = $3 \times 7 - 3 \times 1 = 18$... wait, each point is on 7 lines, and the line has 3 points, so lines meeting the given line = $3 \times 7 - 2 \times 1 = 19$ (subtracting 2 because the line itself is counted 3 times, so $3 \times 7 - 2 = 19$). Hmm, let me recount: lines meeting line $L$ = lines through point 1 of $L$ + lines through point 2 + lines through point 3 - 2 × (line $L$ itself, counted 3 times, so subtract 2) = $7 + 7 + 7 - 2 = 19$. No wait, the line $L$ passes through all 3 points, so it's counted 3 times. So lines meeting $L$ (including $L$ itself) = $7 + 7 + 7 - 2 \times 3 + 1 = 21 - 6 + 1 = 16$? I'm getting confused.

Let me use the formula: in $PG(3, q)$, the number of lines meeting a given line is $(q+1)(q^2+1) - 1 = q^3 + q^2 + q$. For $q = 2$: $8 + 4 + 2 = 14$. Plus the line itself = 15. So 14 other lines meet a given line, and $35 - 1 - 14 = 20$ lines are skew to it.

Hmm, let me just directly count. A line $L$ has 3 points. Each point is on 7 lines. The lines through the 3 points of $L$: each point contributes 7 lines, but $L$ is counted 3 times (once for each point). So the number of distinct lines through at least one point of $L$ is $3 \times 7 - 2 \times 1 = 19$ (by inclusion-exclusion: $|A \cup B \cup C| = 3 \times 7 - 3 \times 1 + 1 = 19$, where the pairwise intersections are all $\{L\}$ and the triple intersection is $\{L\}$). So 19 lines meet $L$ (including $L$ itself), and $35 - 19 = 16$ lines are skew to $L$.

OK so 16 out of 34 other lines are skew to $L$. In a parallelism, the 7 spreads partition the 35 lines. Spread 1 has 5 lines (including $L$), so 4 other lines in spread 1 are disjoint from $L$ (they're in the same spread, so disjoint). The remaining 30 lines are in spreads 2-7, 5 per spread. Of these 30, 18 meet $L$ and 12 are skew.

For $L_1(P)$ (a line in spread 1) and $L_2(Q)$ (a line in spread 2): they meet iff $L_2(Q)$ is not skew to $L_1(P)$. Out of 5 lines in spread 2, how many are skew to $L_1(P)$?

In a parallelism, the distribution of skew lines across spreads might vary. This is getting too complicated without explicit computation.

Let me try a completely different approach. Let me just try to construct a 4-regular graph on 15 vertices with diameter 2 by hand or by a known construction.

**Known result:** The $(4, 2)$-cage (smallest 4-regular graph with girth 4... no, that's different).

Actually, let me look at this from the perspective of strongly regular graphs. A strongly regular graph $\text{srg}(n, k, \lambda, \mu)$ has $n$ vertices, degree $k$, every adjacent pair has $\lambda$ common neighbors, every non-adjacent pair has $\mu$ common neighbors. Such a graph has diameter 2 (if $\mu > 0$).

For $k = 4$: $\text{srg}(n, 4, \lambda, \mu)$ with $\mu > 0$. The parameters satisfy $(n - k - 1)\mu = k(k - \lambda - 1)$, so $(n - 5)\mu = 4(3 - \lambda)$.

Possible $(\lambda, \mu)$:
- $\lambda = 0, \mu = 1$: $(n-5) = 12$, $n = 17$. This is the Moore graph, which doesn't exist for $k = 4$.
- $\lambda = 0, \mu = 2$: $2(n-5) = 12$, $n = 11$. $\text{srg}(11, 4, 0, 2)$... does this exist? The complement would be $\text{srg}(11, 6, 3, 4)$. Hmm, I'm not sure if $\text{srg}(11, 4, 0, 2)$ exists.
- $\lambda = 1, \mu = 1$: $(n-5) = 8$, $n = 13$. $\text{srg}(13, 4, 1, 1)$... 
- $\lambda = 1, \mu = 2$: $2(n-5) = 8$, $n = 9$. $\text{srg}(9, 4, 1, 2)$. This is the Paley graph $P(9)$! The Paley graph on 9 vertices: $\text{srg}(9, 4, 1, 2)$. This exists (it's the graph on $\mathbb{F}_9$ where $x \sim y$ iff $x - y$ is a nonzero square). It has diameter 2. ✓ But only 9 vertices.
- $\lambda = 2, \mu = 1$: $(n-5) = 4$, $n = 9$. $\text{srg}(9, 4, 2, 1)$. This is the complement of $\text{srg}(9, 4, 1, 2)$, which is $\text{srg}(9, 4, 2, 1)$. Also 9 vertices.
- $\lambda = 2, \mu = 2$: $2(n-5) = 4$, $n = 7$. $\text{srg}(7, 4, 2, 2)$. This is $K_7$ minus a perfect matching... no, $K_7$ has degree 6. $\text{srg}(7, 4, 2, 2)$: complement is $\text{srg}(7, 2, 0, 1)$... hmm, I think this might not exist or might be trivial.
- $\lambda = 2, \mu = 3$: $3(n-5) = 4$, no integer solution.
- $\lambda = 3, \mu = 1$: $(n-5) = 0$, $n = 5$. $\text{srg}(5, 4, 3, 1) = K_5$. Trivial.
- $\lambda = 3, \mu = 2$: $2(n-5) = 0$, $n = 5$. Same.
- $\lambda = 0, \mu = 3$: $3(n-5) = 12$, $n = 9$. $\text{srg}(9, 4, 0, 3)$. Complement is $\text{srg}(9, 4, 0, 3)$... the complement of $\text{srg}(9, 4, 0, 3)$ is $\text{srg}(9, 4, 3, 0)$... wait, complement parameters: $\text{srg}(n, n-k-1, n-2k+\mu, n-2k+\lambda)$. So complement of $\text{srg}(9, 4, 0, 3)$ is $\text{srg}(9, 4, 9-8+3, 9-8+0) = \text{srg}(9, 4, 4, 1)$. Hmm, $\lambda = 4$ but $k = 4$, so every adjacent pair has 4 common neighbors, meaning every edge is in 4 triangles. For $k = 4$, each vertex has 4 neighbors, and each neighbor shares 4 common neighbors with it, but there are only 4 neighbors total, so all 4 neighbors are common neighbors of any adjacent pair. This means the graph is a union of cliques. $\text{srg}(9, 4, 4, 1)$: if it's a union of cliques, each clique has size 5 (since $k = 4$), but $9/5$ is not an integer. So this doesn't exist. Hence $\text{srg}(9, 4, 0, 3)$ doesn't exist either.

So the strongly regular graphs with $k = 4$ and $\mu > 0$ that exist are:
- $\text{srg}(9, 4, 1, 2)$ (Paley graph $P(9)$), 9 vertices
- $\text{srg}(13, 4, 1, 1)$, 13 vertices (if it exists)
- $\text{srg}(11, 4, 0, 2)$, 11 vertices (if it exists)

Let me check $\text{srg}(13, 4, 1, 1)$: eigenvalues are $\frac{1}{2}((\lambda - \mu) + \sqrt{(\lambda - \mu)^2 + 4(k - \mu)}) = \frac{1}{2}(0 + \sqrt{0 + 12}) = \sqrt{3}$ and $\frac{1}{2}(0 - \sqrt{12}) = -\sqrt{3}$. These are irrational, and the multiplicities must be integers. Multiplicity of $\sqrt{3}$: $\frac{(n-1)(-\mu) - k}{\lambda - \mu - \sqrt{...}}$... the formula is messy. Let me use the standard: multiplicities are $f = \frac{1}{2}\left((n-1) - \frac{2k + (n-1)(\lambda - \mu)}{\sqrt{(\lambda-\mu)^2 + 4(k-\mu)}}\right)$ and $g = n - 1 - f$.

$= \frac{1}{2}\left(12 - \frac{8 + 12 \cdot 0}{\sqrt{12}}\right) = \frac{1}{2}\left(12 - \frac{8}{2\sqrt{3}}\right) = \frac{1}{2}\left(12 - \frac{4}{\sqrt{3}}\right) = 6 - \frac{2}{\sqrt{3}}$.

This is not an integer, so $\text{srg}(13, 4, 1, 1)$ does not exist.

$\text{srg}(11, 4, 0, 2)$: eigenvalues: $\frac{1}{2}(-2 + \sqrt{4 + 16}) = \frac{1}{2}(-2 + \sqrt{20}) = \frac{1}{2}(-2 + 2\sqrt{5}) = -1 + \sqrt{5}$ and $-1 - \sqrt{5}$. Multiplicities: $f = \frac{1}{2}(10 - \frac{8 + 10(-2)}{\sqrt{20}}) = \frac{1}{2}(10 - \frac{-12}{2\sqrt{5}}) = \frac{1}{2}(10 + \frac{6}{\sqrt{5}}) = 5 + \frac{3}{\sqrt{5}}$. Not an integer. So $\text{srg}(11, 4, 0, 2)$ does not exist.

So the only strongly regular graph with $k = 4$, $\mu > 0$, and $n > 9$ would be ones I haven't checked. Let me check more:

- $\lambda = 1, \mu = 3$: $3(n-5) = 8$, no integer $n$.
- $\lambda = 2, \mu = 4$: $4(n-5) = 4$, $n = 6$. $\text{srg}(6, 4, 2, 4)$. But $\mu = 4 > k - \lambda - 1 = 1$... actually $\mu$ can be at most $k$. $\mu = 4 = k$, so every non-adjacent pair has all 4 neighbors as common neighbors. This means the graph is complete multipartite. $K_{2,2,2}$ has $n = 6, k = 4, \lambda = 2, \mu = 4$. Wait, $K_{2,2,2}$: each vertex is adjacent to 4 others (all except its partner), $\lambda = 2$ (two vertices in different parts share 2 common neighbors in the third part), $\mu = 4$ (two vertices in the same part share all 4 neighbors). Yes, $\text{srg}(6, 4, 2, 4) = K_{2,2,2}$. But $n = 6$, too small.

So the largest strongly regular graph with $k = 4$ and diameter 2 is the Paley graph $P(9)$ with 9 vertices. But we're looking for $n = 15$, which is not strongly regular.

So the graph on 15 vertices won't be strongly regular. Let me try to construct it directly.

Let me try a different approach. I'll use a computer-like search by hand.

**Construction: Modified circulant or vertex-transitive graph.**

Since circulant graphs on 15 vertices don't work (as shown), let me try a Cayley graph on a non-cyclic group of order 15. The only group of order 15 is $\mathbb{Z}_{15}$ (since 15 = 3 × 5 and gcd(3,5) = 1, $\mathbb{Z}_{15} \cong \mathbb{Z}_3 \times \mathbb{Z}_5$). So Cayley graphs on groups of order 15 are the same as circulant graphs. No luck.

Let me try a non-vertex-transitive construction.

**Construction: Start with the Paley graph $P(9)$ and extend.**

$P(9)$ is $\text{srg}(9, 4, 1, 2)$: 9 vertices, 4-regular, diameter 2. Add 6 more vertices.

Each new vertex needs degree 4 and must be within distance 2 of all 14 others.

This is complex. Let me try a more explicit construction.

**Construction: The graph $G$ with vertices $\{0, 1, \ldots, 14\}$.**

Let me try to use the structure of $\mathbb{Z}_3 \times \mathbb{Z}_5$. Vertices are $(i, j)$ with $i \in \mathbb{Z}_3, j \in \mathbb{Z}_5$.

Connect $(i, j)$ to $(i, j \pm 1)$ (same row, adjacent columns): this gives a 5-cycle in each row, degree 2.
Connect $(i, j)$ to $(i+1, j)$ and $(i-1, j)$ (same column, adjacent rows): degree 2 more, total 4.

This is the Cartesian product $C_3 \square C_5$ (but $C_3$ is a triangle, not a 3-cycle... well, $C_3 = K_3$). Actually, $C_3 \square C_5$ is the graph on $\mathbb{Z}_3 \times \mathbb{Z}_5$ where $(i,j) \sim (i', j')$ iff ($i = i'$ and $j - j' = \pm 1$) or ($j = j'$ and $i - i' = \pm 1$). This is 4-regular.

Diameter of $C_3 \square C_5$: the distance is $d_{C_3}(i, i') + d_{C_5}(j, j')$. $C_3$ has diameter 1, $C_5$ has diameter 2. So the diameter is $1 + 2 = 3$. Too large.

Let me modify. Instead of connecting to adjacent rows, connect to a different pattern.

Connect $(i, j)$ to $(i+1, j + f(i))$ for some function $f$. This is like a "twisted" product.

Let me try: $(i, j) \sim (i+1, j)$ and $(i, j) \sim (i+1, j+1)$ (mod 3 and 5). So each vertex connects to 2 vertices in the next row and... wait, this gives degree 4 if we also connect to the previous row.

Actually, let me define: $(i, j) \sim (i+1, j)$ and $(i, j) \sim (i-1, j+2)$. Then each vertex has 4 neighbors: $(i+1, j), (i-1, j), (i-1, j+2), (i+1, j-2)$ (the last two from the reverse connections). Wait, I need to be careful about symmetry.

Let me define the connection set in $\mathbb{Z}_3 \times \mathbb{Z}_5$: $S = \{(1,0), (2,0), (0,1), (0,4)\} = \{(\pm 1, 0), (0, \pm 1)\}$. This is the Cartesian product, which we showed has diameter 3.

Let me try $S = \{(1,0), (2,0), (1,1), (2,4)\} = \{(1,0), (-1,0), (1,1), (-1,-1)\}$. Check: $-S = \{(2,0), (1,0), (2,4), (1,1)\} = S$. ✓ (symmetric).

Now, $S + S$: all sums of two elements from $S$:
$(1,0)+(1,0) = (2,0)$
$(1,0)+(2,0) = (0,0)$
$(1,0)+(1,1) = (2,1)$
$(1,0)+(2,4) = (0,4)$
$(2,0)+(2,0) = (1,0)$
$(2,0)+(1,1) = (0,1)$
$(2,0)+(2,4) = (1,4)$
$(1,1)+(1,1) = (2,2)$
$(1,1)+(2,4) = (0,0)$
$(2,4)+(2,4) = (1,3)$

$S + S = \{(0,0), (0,1), (0,4), (1,0), (1,3), (1,4), (2,0), (2,1), (2,2)\}$.

$S \cup (S+S) = \{(0,0), (0,1), (0,4), (1,0), (1,1), (1,3), (1,4), (2,0), (2,1), (2,2), (2,4)\}$.

Missing: $(0,2), (0,3), (1,2), (2,3)$. That's 4 missing elements. Not all covered.

Let me try $S = \{(1,0), (2,0), (1,2), (2,3)\} = \{(1,0), (-1,0), (1,2), (-1,-2)\}$. Check: $-S = \{(2,0), (1,0), (2,3), (1,2)\} = S$. ✓

$S+S$:
$(1,0)+(1,0) = (2,0)$
$(1,0)+(2,0) = (0,0)$
$(1,0)+(1,2) = (2,2)$
$(1,0)+(2,3) = (0,3)$
$(2,0)+(2,0) = (1,0)$
$(2,0)+(1,2) = (0,2)$
$(2,0)+(2,3) = (1,3)$
$(1,2)+(1,2) = (2,4)$
$(1,2)+(2,3) = (0,0)$
$(2,3)+(2,3) = (1,1)$

$S+S = \{(0,0), (0,2), (0,3), (1,0), (1,1), (1,3), (2,0), (2,2), (2,4)\}$.

$S \cup (S+S) = \{(0,0), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3), (2,0), (2,2), (2,3), (2,4)\}$.

Missing: $(0,1), (0,4), (1,4), (2,1)$. 4 missing. Still not enough.

Let me try $S = \{(1,1), (2,4), (1,4), (2,1)\} = \{(1,1), (-1,-1), (1,-1), (-1,1)\}$.

$S+S$:
$(1,1)+(1,1) = (2,2)$
$(1,1)+(2,4) = (0,0)$
$(1,1)+(1,4) = (2,0)$
$(1,1)+(2,1) = (0,2)$
$(2,4)+(2,4) = (1,3)$
$(2,4)+(1,4) = (0,3)$
$(2,4)+(2,1) = (1,0)$
$(1,4)+(1,4) = (2,3)$
$(1,4)+(2,1) = (0,0)$
$(2,1)+(2,1) = (1,2)$

$S+S = \{(0,0), (0,2), (0,3), (1,0), (1,2), (1,3), (2,0), (2,2), (2,3)\}$.

$S \cup (S+S) = \{(0,0), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3), (1,4), (2,0), (2,1), (2,2), (2,3), (2,4)\}$.

Missing: $(0,1), (0,4)$. Only 2 missing! Very close.

$(0,1)$ and $(0,4) = (0,-1)$. These are the elements with first coordinate 0 and second coordinate $\pm 1$.

Hmm, can I tweak the connection set? Let me try $S = \{(1,1), (2,4), (0,1), (0,4)\} = \{(1,1), (-1,-1), (0,1), (0,-1)\}$.

$S+S$:
$(1,1)+(1,1) = (2,2)$
$(1,1)+(2,4) = (0,0)$
$(1,1)+(0,1) = (1,2)$
$(1,1)+(0,4) = (1,0)$
$(2,4)+(2,4) = (1,3)$
$(2,4)+(0,1) = (2,0)$
$(2,4)+(0,4) = (2,3)$
$(0,1)+(0,1) = (0,2)$
$(0,1)+(0,4) = (0,0)$
$(0,4)+(0,4) = (0,3)$

$S+S = \{(0,0), (0,2), (0,3), (1,0), (1,2), (1,3), (2,0), (2,2), (2,3)\}$.

$S \cup (S+S) = \{(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,2), (1,3), (2,0), (2,2), (2,3), (1,1), (2,4)\}$.

Missing: $(1,4), (2,1)$. 2 missing.

Let me try $S = \{(1,1), (2,4), (0,2), (0,3)\} = \{(1,1), (-1,-1), (0,2), (0,-2)\}$.

$S+S$:
$(1,1)+(1,1) = (2,2)$
$(1,1)+(2,4) = (0,0)$
$(1,1)+(0,2) = (1,3)$
$(1,1)+(0,3) = (1,4)$
$(2,4)+(2,4) = (1,3)$
$(2,4)+(0,2) = (2,1)$
$(2,4)+(0,3) = (2,2)$
$(0,2)+(0,2) = (0,4)$
$(0,2)+(0,3) = (0,0)$
$(0,3)+(0,3) = (0,1)$

$S+S = \{(0,0), (0,1), (0,4), (1,3), (1,4), (2,1), (2,2)\}$.

$S \cup (S+S) = \{(0,0), (0,1), (0,2), (0,3), (0,4), (1,1), (1,3), (1,4), (2,1), (2,2), (2,4)\}$.

Missing: $(1,0), (1,2), (2,0), (2,3)$. 4 missing. Worse.

Let me try $S = \{(1,1), (2,4), (1,3), (2,2)\} = \{(1,1), (-1,-1), (1,3), (-1,-3)\}$.

$S+S$:
$(1,1)+(1,1) = (2,2)$
$(1,1)+(2,4) = (0,0)$
$(1,1)+(1,3) = (2,4)$
$(1,1)+(2,2) = (0,3)$
$(2,4)+(2,4) = (1,3)$
$(2,4)+(1,3) = (0,2)$
$(2,4)+(2,2) = (1,1)$
$(1,3)+(1,3) = (2,1)$
$(1,3)+(2,2) = (0,0)$
$(2,2)+(2,2) = (1,4)$

$S+S = \{(0,0), (0,2), (0,3), (1,1), (1,3), (1,4), (2,1), (2,2), (2,4)\}$.

$S \cup (S+S) = \{(0,0), (0,2), (0,3), (1,1), (1,3), (1,4), (2,1), (2,2), (2,4)\} \cup \{(1,1), (2,4), (1,3), (2,2)\}$.

$= \{(0,0), (0,2), (0,3), (1,1), (1,3), (1,4), (2,1), (2,2), (2,4)\}$.

Missing: $(0,
