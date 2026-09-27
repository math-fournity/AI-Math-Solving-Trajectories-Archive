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
  <problem_id>polymath_03711</problem_id>
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

A party has $2 n$ people attending. If any two people at the party have the same number of friends, then these two people do not have any common friends (friendship is mutual). How many pairs of friends can there be at most in this party?
(Wu Yunjian, contributor)

## Standard Solution

The maximum number of friend pairs sought is $\frac{n(n+1)}{2}$.
We use $2n$ points to represent $2n$ people. If two people are friends, we draw an edge between their corresponding points, and call one point a neighbor of the other. This way, we get a simple graph $G$ with these $2n$ people as the vertex set, satisfying the following condition: if two people have the same number of neighbors, then these two people's neighbor sets have no common elements.

Assume $A$ is the point with the most neighbors in the graph. Let $A$ have $k$ neighbors. We will prove that $k \leqslant n$, and that these $k$ points have neighbor counts of $1, 2, \cdots, k$.

Let the $k$ neighbors of $A$ be $A_{1}, A_{2}, \cdots, A_{k}$. Since $A_{1}, A_{2}, \cdots, A_{k}$ have a common neighbor $A$, the number of neighbors of these points are all different. It is also easy to see that the number of neighbors of these points is at least 1 (all have neighbor $A$) and at most $k$ (since $A$ has the most neighbors), so the number of neighbors of $A_{1}, A_{2}, \cdots, A_{k}$ is a permutation of $1, 2, \cdots, k$.

Without loss of generality, assume $A_{i}$ has exactly $i$ neighbors $(i=1,2, \cdots, k)$. Consider $A_{k}$. At this point, $A_{k}$ has the same number of neighbors as $A$, so they have no common neighbors, meaning $A_{k}$ has no neighbors in $\left\{A_{1}, A_{2}, \cdots, A_{k-1}\right\}$. Therefore, the total number of people
$$
2n \geqslant 1 + k + (k-1) = 2k,
$$

hence $k \leqslant n$.
Let the total number of neighbor pairs be $S$. From the above, $A$'s neighbors $A_{1}, A_{2}, \cdots, A_{k}$ have $1, 2, \cdots, k$ neighbors respectively, corresponding to $1, 2, \cdots, k$ neighbor pairs. Let the $k-1$ neighbors of $A_{k}$ other than $A$ be $B_{1}, B_{2}, \cdots, B_{k-1}$.

For the $2n-2k$ points other than $A, A_{1}, A_{2}, \cdots, A_{k}, B_{1}, B_{2}, \cdots, B_{k-1}$, each point has at most $k$ neighbors, and can produce at most $\frac{k(2n-2k)}{2}$ neighbor pairs. Therefore,
$$
\begin{aligned}
S & \leqslant 1 + 2 + \cdots + k + \frac{k(2n-2k)}{2} = \frac{k(2n-k+1)}{2} \\
& \leqslant \frac{(k+2n-k+1)^2}{8} = \frac{(2n+1)^2}{8} = \frac{4n(n+1)+1}{8}.
\end{aligned}
$$

Since $8 \nmid 4n(n+1)+1$, we have
$$
S \leqslant \left[\frac{4n(n+1)+1}{8}\right] = \frac{n(n+1)}{2}.
$$

Finally, we show that $S$ can achieve $\frac{n(n+1)}{2}$.
Consider the following simple graph with $2n$ points $A_{1}, A_{2}, \cdots, A_{n}, B_{1}, B_{2}, \cdots, B_{n}$ as vertices. When $i \geqslant \left[\frac{k}{2}\right]+1$, the neighbor set of $A_{i}$ is $\left\{B_{i}, A_{n-i+1}, A_{n-i+2}, \cdots, A_{n}\right\} \backslash \left\{A_{i}\right\}$, and the neighbor set of $B_{i}$ is $\left\{A_{i}, B_{n-i+1}, B_{n-i+2}, \cdots, B_{n}\right\} \backslash \left\{B_{i}\right\}$; when $i \leqslant \left[\frac{k}{2}\right]$, the neighbor set of $A_{i}$ is $\left\{A_{n}, A_{n-1}, \cdots, A_{n-i+1}\right\}$, and the neighbor set of $B_{i}$ is $\left\{B_{n}, B_{n-1}, \cdots, B_{n-i+1}\right\}$. At this point, $A_{i}$ and $B_{i}$ each have $i$ neighbors $(i=1,2, \cdots, n)$, and the total number of neighbor pairs $S = \frac{1}{2} \times 2(1+2+\cdots+n) = \frac{n(n+1)}{2}$.
In conclusion, the maximum number of friend pairs sought is $\frac{n(n+1)}{2}$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a party with $2n$ people. The condition: if any two people have the same number of friends, then they have no common friends. Friendship is mutual. We want to maximize the number of pairs of friends (edges in the friendship graph).

So we have a graph $G$ on $2n$ vertices. The condition is: if two vertices $u, v$ have the same degree, then $N(u) \cap N(v) = \emptyset$ (no common neighbors).

We want to maximize the number of edges.

Let me think about this. Let's denote the degree sequence. Vertices with the same degree $d$ form a group. Within each group of degree $d$, no two vertices share a common neighbor.

Let me think about what "no common friends" means. If $u$ and $v$ both have degree $d$ and are in the same group, then $N(u) \cap N(v) = \emptyset$. This means the neighborhoods of all vertices in the same degree group are pairwise disjoint.

If there are $k$ vertices of degree $d$, their neighborhoods are pairwise disjoint sets, each of size $d$. So the total number of vertices covered by these neighborhoods is $k \cdot d$, and this must be $\leq 2n$ (since there are $2n$ vertices total, though a vertex could be in its own... no, neighborhoods don't include self).

Wait, but also vertices in the group might be friends with each other. If $u$ and $v$ are both degree $d$ and are friends, then $u \in N(v)$ and $v \in N(u)$. But they have no common friends, so $N(u) \cap N(v) = \emptyset$. That's fine, $u \in N(v)$ but $u \notin N(u)$, so no contradiction there.

So the constraint is: for each degree value $d$, if $k_d$ vertices have degree $d$, then their neighborhoods are pairwise disjoint, so $k_d \cdot d \leq 2n$.

Wait, is that right? The neighborhoods are pairwise disjoint subsets of the $2n$ vertices. So $k_d \cdot d \leq 2n$.

Now we want to maximize the total number of edges. The total number of edges is $\frac{1}{2} \sum_v \deg(v) = \frac{1}{2} \sum_d k_d \cdot d$.

Subject to:
- $\sum_d k_d = 2n$ (total vertices)
- For each $d$: $k_d \cdot d \leq 2n$
- $k_d \geq 0$ integers
- $0 \leq d \leq 2n-1$ (degrees range)

And we want to maximize $\frac{1}{2} \sum_d k_d \cdot d$.

Since $k_d \cdot d \leq 2n$ for each $d$, we have $\sum_d k_d \cdot d \leq \sum_d 2n = 2n \cdot |\{d : k_d > 0\}|$.

The number of distinct degree values is at most $2n$ (from $0$ to $2n-1$). But actually, can we have all $2n$ distinct degrees? If all degrees are distinct, then each $k_d = 1$, and the constraint $k_d \cdot d \leq 2n$ becomes $d \leq 2n$, which is always satisfied since $d \leq 2n-1$.

If all degrees are distinct, the degree sequence is a permutation of $\{0, 1, 2, \ldots, 2n-1\}$. But wait, can a graph have degree sequence containing both $0$ and $2n-1$? If a vertex has degree $2n-1$, it's connected to everyone, so no vertex can have degree $0$. So we can't have all $2n$ distinct degrees.

So the maximum number of distinct degrees is $2n - 1$ (we can't have both $0$ and $2n-1$). 

If we use degrees $\{1, 2, \ldots, 2n-1\}$ (all distinct, $2n-1$ values) plus one repeated degree. Wait, we have $2n$ vertices and at most $2n-1$ distinct degree values. So at least one degree value is repeated.

Hmm, let me reconsider. We want to maximize $\sum_d k_d \cdot d$. 

Let me think of it as an optimization problem. We want to maximize $\sum_d k_d \cdot d$ subject to $\sum_d k_d = 2n$ and $k_d \cdot d \leq 2n$ for each $d$.

To maximize, we want to use high degrees. For a degree $d$, we can have at most $\lfloor 2n/d \rfloor$ vertices of that degree, contributing $\lfloor 2n/d \rfloor \cdot d$ to the sum, which is at most $2n$.

So each degree value contributes at most $2n$ to $\sum k_d \cdot d$. The number of degree values we can use is limited by the total number of vertices.

Hmm, this is getting complex. Let me think about small cases first.

**Case $n=1$: $2n = 2$ people.**
Possible graphs: no edge (0 edges) or 1 edge.
- 0 edges: both have degree 0. Same degree, no common friends (vacuously true since no friends). Valid. 0 edges.
- 1 edge: both have degree 1. Same degree. Common friends? $N(u) = \{v\}$, $N(v) = \{u\}$, intersection is empty. Valid. 1 edge.

So max is 1. For $n=1$, answer is 1.

**Case $n=2$: $2n = 4$ people.**
Let me think about what's achievable. 

Total edges in $K_4$ is 6. Can we achieve that? In $K_4$, everyone has degree 3. All same degree. Common friends: any two vertices share 2 common friends. Violates condition. So not $K_4$.

What about 5 edges? That's $K_4$ minus one edge. Degrees: two vertices have degree 2, two have degree 3. The two degree-2 vertices: they are the ones missing the edge between them (or not). Let's say edge $(a,b)$ is missing. Then $\deg(a) = \deg(b) = 2$, $\deg(c) = \deg(d) = 3$. 

Degree-2 group: $\{a, b\}$. $N(a) = \{c, d\}$, $N(b) = \{c, d\}$. Common friends: $\{c, d\}$. Not empty! Violates condition.

What about 4 edges? Let me try different configurations.

Path $P_4$: $a-b-c-d$. Degrees: $\deg(a)=1, \deg(b)=2, \deg(c)=2, \deg(d)=1$. 
Degree-1 group: $\{a, d\}$. $N(a) = \{b\}$, $N(d) = \{c\}$. Common friends: empty. OK.
Degree-2 group: $\{b, c\}$. $N(b) = \{a, c\}$, $N(c) = \{b, d\}$. Common friends: $\{b, c\} \cap... $ wait, $N(b) = \{a, c\}$, $N(c) = \{b, d\}$. Intersection: $\{a,c\} \cap \{b,d\} = \emptyset$. OK!

So $P_4$ works with 3 edges. But can we do better?

Let me try 4 edges. Cycle $C_4$: $a-b-c-d-a$. All degrees 2. $N(a) = \{b,d\}$, $N(b) = \{a,c\}$. Common: empty. $N(a) = \{b,d\}$, $N(c) = \{b,d\}$. Common: $\{b,d\}$. Not empty! Violates.

So $C_4$ doesn't work.

What about a star $K_{1,3}$? Center has degree 3, leaves have degree 1. 
Degree-1 group: 3 vertices. $N$ of each leaf is just the center. All share the center as common friend. Violates.

What about the graph: $a-b, a-c, b-d, c-d$? This is $C_4$ again (just relabeled). Already shown to fail.

What about $a-b, b-c, c-d, a-d$? Also $C_4$.

What about $a-b, a-c, a-d, b-c$? Degrees: $\deg(a)=3, \deg(b)=2, \deg(c)=2, \deg(d)=1$.
Degree-2 group: $\{b,c\}$. $N(b)=\{a,c\}$, $N(c)=\{a,b\}$. Common: $\{a\}$. Not empty. Violates.

What about $a-b, a-c, b-d, c-d, a-d$? 5 edges, already considered similar.

Let me try $a-b, c-d, a-c, b-d$. That's $C_4$ again.

How about $a-b, b-c, c-d$? That's $P_4$, 3 edges.

Let me try to get 4 edges with a different structure. $a-b, b-c, c-d, d-a$ is $C_4$. 

$a-b, a-c, b-d$: degrees 2,2,1,1. Same as some path variant. $N(a)=\{b,c\}$, $N(d)=\{b\}$... wait let me recompute. $a-b, a-c, b-d$. $\deg(a)=2, \deg(b)=2, \deg(c)=1, \deg(d)=1$.
Degree-2: $\{a,b\}$. $N(a)=\{b,c\}$, $N(b)=\{a,d\}$. Common: $\emptyset$. OK.
Degree-1: $\{c,d\}$. $N(c)=\{a\}$, $N(d)=\{b\}$. Common: $\emptyset$. OK.
3 edges, valid.

Add one more edge. $a-b, a-c, b-d, c-d$: $C_4$, fails. $a-b, a-c, b-d, a-d$: $\deg(a)=3, \deg(b)=2, \deg(c)=1, \deg(d)=2$. 
Degree-2: $\{b,d\}$. $N(b)=\{a,d\}$, $N(d)=\{a,b\}$. Common: $\{a\}$. Fails.

$a-b, a-c, b-d, b-c$: $\deg(a)=2, \deg(b)=3, \deg(c)=2, \deg(d)=1$.
Degree-2: $\{a,c\}$. $N(a)=\{b,c\}$, $N(c)=\{a,b\}$. Common: $\{b\}$. Fails.

$a-b, a-c, b-d, c-b$: same as above basically.

Hmm, it seems hard to get 4 edges with 4 vertices. Let me be more systematic.

With 4 edges on 4 vertices, possible degree sequences (partitions of 8 into 4 parts, each 0-3):
- (3,3,1,1): sum=8. Degree-3 group has 2 vertices. $N$ of each has size 3, but they're disjoint subsets of 4 vertices. $3+3=6 > 4$. Impossible (can't have disjoint neighborhoods of size 3 in 4 vertices). Actually wait, the constraint is $k_d \cdot d \leq 2n = 4$. For $d=3, k=2$: $2 \cdot 3 = 6 > 4$. Violates.
- (3,2,2,1): sum=8. Degree-2 group: $k=2, d=2$, $2 \cdot 2 = 4 \leq 4$. OK. But does such a graph exist and satisfy the condition? We need to check. We tried several and they failed. Let me think if it's possible at all.

For degree sequence (3,2,2,1): The vertex of degree 3 is connected to all others. The vertex of degree 1 is connected to only the degree-3 vertex (since the degree-3 vertex is connected to everyone, the degree-1 vertex must be one of its neighbors, and it has only 1 neighbor). So the degree-1 vertex is connected only to the degree-3 vertex. The two degree-2 vertices: each is connected to the degree-3 vertex (since degree-3 is connected to all) and to one other vertex. They can't be connected to the degree-1 vertex (that would give degree-1 vertex degree 2). So they must be connected to each other. So the graph is: degree-3 vertex connected to all, and the two degree-2 vertices connected to each other. 

$N(\text{deg-2 vertex 1}) = \{\text{deg-3}, \text{deg-2 vertex 2}\}$. $N(\text{deg-2 vertex 2}) = \{\text{deg-3}, \text{deg-2 vertex 1}\}$. Common: $\{\text{deg-3}\}$. Not empty. Fails.

- (2,2,2,2): $C_4$ or matching. $C_4$ fails as shown. Two disjoint edges: degrees all 1, not 2. Actually (2,2,2,2) with 4 edges must be $C_4$ (the only 2-regular graph on 4 vertices). Fails.

So for $n=2$, the maximum is 3.

Hmm wait, let me reconsider. Is 3 really the max for $n=2$?

Actually, let me reconsider the matching: two disjoint edges $a-b, c-d$. All degrees 1. Degree-1 group: all 4 vertices. $N(a)=\{b\}, N(b)=\{a\}, N(c)=\{d\}, N(d)=\{c\}$. $N(a) \cap N(c) = \emptyset$. $N(a) \cap N(b) = \emptyset$. All pairwise intersections empty. Valid! 2 edges.

$P_4$: 3 edges, valid as shown. So 3 is achievable.

Can we do 4? We showed all 4-edge graphs on 4 vertices fail. So max for $n=2$ is 3.

For $n=1$: 1. For $n=2$: 3. Pattern might be $\binom{2n}{2}/... $ hmm. $1, 3, ...$

Let me try $n=3$, $2n=6$.

This is getting complicated. Let me think about the upper bound more carefully.

**Upper bound analysis:**

We have $\sum_d k_d \cdot d \leq \sum_d 2n = 2n \cdot m$ where $m$ is the number of distinct degree values. And $\sum_d k_d = 2n$.

The number of distinct degree values $m$ is at most $2n-1$ (can't have both 0 and $2n-1$). But also, for each degree $d$ with $k_d > 0$, we need $k_d \geq 1$ and $k_d \cdot d \leq 2n$.

To maximize $\sum k_d \cdot d$, we want to:
1. Use as many distinct degree values as possible (to get the $2n$ factor multiple times)
2. For each degree value, use $k_d$ as large as possible (up to $\lfloor 2n/d \rfloor$), but also $\sum k_d = 2n$.

This is a knapsack-like problem. Let me think about it differently.

We want to maximize $\sum_d k_d \cdot d$ where:
- $\sum_d k_d = 2n$
- $k_d \cdot d \leq 2n$ for each $d$ with $k_d > 0$
- $k_d$ are non-negative integers
- $d \in \{0, 1, \ldots, 2n-1\}$

For degree $d$, the "efficiency" is: using $k_d$ vertices (consuming $k_d$ from the budget of $2n$ vertices) gives $k_d \cdot d$ edges contribution. The ratio is $d$ (edges per vertex). So higher degrees are more efficient per vertex.

But the constraint $k_d \cdot d \leq 2n$ limits how many vertices we can assign to each degree.

For degree $d$, max $k_d = \lfloor 2n/d \rfloor$, giving contribution $\lfloor 2n/d \rfloor \cdot d \leq 2n$.

So we want to use high-degree values first, fill up to the constraint, then move to lower degrees, until we've used all $2n$ vertices.

Let me think about it greedily. Start with the highest degree $2n-1$. $k_{2n-1} \leq \lfloor 2n/(2n-1) \rfloor = 1$. Contribution: $2n-1$. Uses 1 vertex.

Next degree $2n-2$: $k \leq \lfloor 2n/(2n-2) \rfloor = 1$ (for $n \geq 2$). Contribution: $2n-2$. Uses 1 vertex.

Continue... for degree $d > n$, $\lfloor 2n/d \rfloor = 1$. So each such degree uses 1 vertex and contributes $d$.

Degrees from $n+1$ to $2n-1$: that's $n-1$ degrees, each using 1 vertex, contributing $\sum_{d=n+1}^{2n-1} d$.

For degree $d = n$: $\lfloor 2n/n \rfloor = 2$. Can use 2 vertices, contributing $2n$. Uses 2 vertices.

For degree $d < n$: $\lfloor 2n/d \rfloor \geq 2$.

Hmm, this greedy approach might not give the optimal because we also need the degrees to form a valid graph (graphical sequence) and satisfy the common-neighbor condition. But let me first find the upper bound from the constraint alone, then worry about achievability.

Actually, let me think about this more carefully. The constraint $k_d \cdot d \leq 2n$ is necessary but might not be sufficient. We also need the degree sequence to be graphical and the common-neighbor condition to be satisfiable.

But for an upper bound, the constraint $k_d \cdot d \leq 2n$ is valid. So:

$$\text{edges} = \frac{1}{2} \sum_d k_d \cdot d \leq \frac{1}{2} \sum_d 2n = n \cdot m$$

where $m$ is the number of distinct degree values with $k_d > 0$.

And $m \leq 2n - 1$ (can't have both 0 and $2n-1$). But also $\sum k_d = 2n$ and $k_d \geq 1$ for each used degree, so $m \leq 2n$.

But we also need $k_d \cdot d \leq 2n$. For $d = 0$, $k_0 \cdot 0 = 0 \leq 2n$, always OK, but contributes 0 edges. So using degree 0 is wasteful.

For the upper bound, we want to maximize $m$ (number of distinct degrees) while having $\sum k_d = 2n$ and $k_d \cdot d \leq 2n$.

If all $k_d = 1$ (all degrees distinct), then $m = 2n$ and the constraint is $d \leq 2n$ for each $d$, which is satisfied for $d \leq 2n-1$. But we can't have both 0 and $2n-1$. So $m \leq 2n - 1$ with all distinct.

With $m = 2n - 1$ distinct degrees and all $k_d = 1$ except one $k_d = 2$: uses $(2n-2) \cdot 1 + 2 = 2n$ vertices. The constraint for the doubled degree: $2d \leq 2n$, so $d \leq n$.

To maximize $\sum k_d \cdot d$, we want the doubled degree to be as large as possible, i.e., $d = n$, and the distinct degrees to be the largest possible.

If we use degrees $\{1, 2, \ldots, 2n-1\}$ (all except 0), that's $2n-1$ distinct values, using $2n-1$ vertices with $k_d = 1$. We need 1 more vertex. We can double one degree $d \leq n$. Best to double $d = n$.

Total: $\sum_{d=1}^{2n-1} d + n = \frac{(2n-1)(2n)}{2} + n = n(2n-1) + n = 2n^2$.

Edges: $\frac{1}{2} \cdot 2n^2 = n^2$.

Alternatively, use degrees $\{0, 1, \ldots, 2n-2\}$ (all except $2n-1$), $2n-1$ distinct values. Double one degree $d \leq n$. Best: $d = n$.

Total: $\sum_{d=0}^{2n-2} d + n = \frac{(2n-2)(2n-1)}{2} + n = (n-1)(2n-1) + n = 2n^2 - 3n + 1 + n = 2n^2 - 2n + 1$.

Edges: $\frac{2n^2 - 2n + 1}{2} = n^2 - n + \frac{1}{2}$. Not integer, so this doesn't work directly. Actually the sum of degrees must be even. $\sum_{d=0}^{2n-2} d + n = (2n^2 - 2n + 1) + n = 2n^2 - n + 1$... wait let me recompute.

$\sum_{d=0}^{2n-2} d = \frac{(2n-2)(2n-1)}{2} = (n-1)(2n-1) = 2n^2 - 3n + 1$.

Adding $n$ (doubling degree $n$): $2n^2 - 3n + 1 + n = 2n^2 - 2n + 1$.

This is odd, so not graphical. So this option doesn't work.

Back to the first option: degrees $\{1, 2, \ldots, 2n-1\}$ with degree $n$ doubled. Sum = $2n^2$. Edges = $n^2$.

But wait, can we do better? What if we don't use all degrees from 1 to $2n-1$? What if we use fewer distinct degrees but with higher $k_d$ values?

For example, if we use degree $d$ with $k_d = \lfloor 2n/d \rfloor$, the contribution is $\lfloor 2n/d \rfloor \cdot d \leq 2n$. The number of vertices used is $\lfloor 2n/d \rfloor$. The "efficiency" is contribution per vertex = $d$.

So to maximize total contribution with $\sum k_d = 2n$ vertices, we want to use the highest degrees first (highest efficiency), filling each to its max $k_d$.

Let me try this greedy approach for general $n$.

Start with $d = 2n-1$: $k = 1$, contribution $2n-1$, vertices used 1.
$d = 2n-2$: $k = 1$, contribution $2n-2$, vertices used 1.
...
$d = n+1$: $k = 1$, contribution $n+1$, vertices used 1.

So far: degrees $n+1$ to $2n-1$, that's $n-1$ degrees, $n-1$ vertices, contribution $\sum_{d=n+1}^{2n-1} d = \frac{(n-1)(n+1+2n-1)}{2} = \frac{(n-1)(3n)}{2} = \frac{3n(n-1)}{2}$.

Remaining vertices: $2n - (n-1) = n+1$.

$d = n$: $k = \lfloor 2n/n \rfloor = 2$, contribution $2n$, vertices used 2. Remaining: $n+1-2 = n-1$.

$d = n-1$: $k = \lfloor 2n/(n-1) \rfloor$. For $n \geq 3$, this is $\lfloor 2n/(n-1) \rfloor = \lfloor 2 + 2/(n-1) \rfloor = 2$ (for $n \geq 3$). Contribution $2(n-1)$, vertices used 2. Remaining: $n-3$.

Hmm, this is getting complicated. Let me think about whether the upper bound $n^2$ is achievable.

Actually, let me reconsider. The upper bound from the constraint is:

$\text{edges} \leq n \cdot m$ where $m$ is the number of distinct degree values.

And $m \leq 2n - 1$ (can't have both 0 and $2n-1$). But we also need $\sum k_d = 2n$ with $k_d \geq 1$, so $m \leq 2n$. Combined with the 0 and $2n-1$ constraint, $m \leq 2n-1$.

But also, for each $d$ with $k_d \geq 1$, we need $k_d \cdot d \leq 2n$, so $d \leq 2n$ (always true) and if $k_d \geq 2$ then $d \leq n$.

If $m = 2n - 1$ (all degrees distinct except one pair), the upper bound is $n(2n-1) = 2n^2 - n$ edges. But we showed the actual sum is $2n^2$ (with the specific choice), giving $n^2$ edges. Wait, that's different from $n(2n-1)$.

Oh I see, the bound $\text{edges} \leq n \cdot m$ is not tight because $k_d \cdot d$ might be less than $2n$ for many degrees. Let me re-examine.

The bound is $\sum k_d \cdot d \leq \sum 2n = 2n \cdot m$, so edges $\leq n \cdot m$. With $m = 2n-1$, edges $\leq n(2n-1)$. But the actual maximum sum we computed was $2n^2$, giving edges $= n^2$. And $n^2 \leq n(2n-1) = 2n^2 - n$ for $n \geq 1$. So the bound $n(2n-1)$ is not tight.

The issue is that for high degrees $d > n$, $k_d = 1$ and $k_d \cdot d = d < 2n$. So the constraint $k_d \cdot d \leq 2n$ is not binding for those.

Let me think about this differently. We want to maximize $\sum k_d \cdot d$ subject to:
1. $\sum k_d = 2n$
2. $k_d \cdot d \leq 2n$ for each $d$
3. Can't have both $d=0$ and $d=2n-1$ present (graphical constraint)

Since higher $d$ gives more contribution per vertex, we want to use high degrees. But the constraint limits $k_d$ for each degree.

For $d > n$: $k_d \leq 1$ (since $2d > 2n$). Contribution per vertex: $d$.
For $d = n$: $k_d \leq 2$. Contribution per vertex: $n$.
For $d < n$: $k_d \leq \lfloor 2n/d \rfloor$. Contribution per vertex: $d$.

So the greedy strategy is: use the highest degrees first, each with $k_d = 1$ (for $d > n$), then fill remaining vertices with lower degrees.

Degrees $n+1, n+2, \ldots, 2n-1$: $n-1$ degrees, $n-1$ vertices, contribution $\sum_{d=n+1}^{2n-1} d$.

But we can't use degree $2n-1$ if we also use degree $0$. Since we're not using degree 0 (it contributes nothing), we can use degree $2n-1$.

After using degrees $n+1$ to $2n-1$ ($n-1$ vertices), we have $2n - (n-1) = n+1$ vertices left.

Now for the remaining $n+1$ vertices, we want to maximize contribution using degrees $\leq n$. The best degree is $n$ with $k_n = 2$ (contribution $2n$, 2 vertices). Then $n-1$ vertices left.

Next best: degree $n-1$ with $k = \lfloor 2n/(n-1) \rfloor$. For large $n$, this is 2 or 3.

This is getting complicated. Let me try to see if the answer is $n^2$ by checking small cases.

$n=1$: $n^2 = 1$. We found max = 1. ✓
$n=2$: $n^2 = 4$. But we found max = 3. ✗

So $n^2$ is not the answer for $n=2$. Let me recheck.

For $n=2$, $2n=4$. Using degrees $\{1,2,3\}$ with degree 2 doubled: degrees are $1,2,2,3$. Sum = 8. Edges = 4. But we showed no 4-edge graph on 4 vertices satisfies the condition! So the constraint $k_d \cdot d \leq 2n$ is necessary but not sufficient.

So the upper bound from the constraint alone gives 4, but the actual max is 3. The graphicality and common-neighbor condition impose additional constraints.

Let me reconsider. For $n=2$, the answer is 3. For $n=1$, the answer is 1.

$1, 3, ?$. Could the answer be $\binom{2n-1}{2} / ...$? Or $n(2n-1)/2$? For $n=1$: $1 \cdot 1 / 2 = 0.5$. No.

$3 = \binom{3}{2}$? $1 = \binom{1}{2} = 0$? No.

Hmm, $1, 3$. Could be $n^2 - n + 1$? $n=1: 1, n=2: 3$. Let me check $n=3$: $9-3+1=7$.

Or $2n-1$ choose something... $\binom{2n-1}{2} = (2n-1)(2n-2)/2 = (2n-1)(n-1)$. $n=1: 0, n=2: 3$. Doesn't match $n=1$.

Or maybe $\binom{2n}{2} - \binom{n}{2} = n(2n-1) - n(n-1)/2$... getting complicated.

Let me try $n=3$ more carefully.

$2n = 6$ vertices. We want to maximize edges.

Let me think about what structures work. The condition is: same degree → no common neighbors.

One natural construction: a graph where all degrees are distinct. Then the condition is vacuously satisfied (no two vertices have the same degree). The question is: what's the maximum number of edges in a graph on $2n$ vertices with all distinct degrees?

But we can't have all $2n$ degrees distinct (0 and $2n-1$ can't coexist). So at most $2n-1$ distinct degrees, meaning at least one pair shares a degree.

If we have $2n-1$ distinct degrees (one pair), the degree sequence is $\{0, 1, 2, \ldots, 2n-2\}$ (missing $2n-1$) or $\{1, 2, \ldots, 2n-1\}$ (missing 0), with one degree repeated.

For $\{1, 2, \ldots, 2n-1\}$ with one degree $d$ repeated (where $2d \leq 2n$, so $d \leq n$): sum = $\frac{(2n-1)(2n)}{2} + d = n(2n-1) + d$. Edges = $\frac{n(2n-1) + d}{2}$. To maximize, $d = n$: edges = $\frac{n(2n-1)+n}{2} = \frac{2n^2}{2} = n^2$.

But for $n=2$, this gives 4, and we showed 4 is not achievable. So the constraint is not just about the degree sequence being graphical, but also about the common-neighbor condition.

Let me think about why the degree sequence $\{1,2,2,3\}$ (for $n=2$) doesn't work. The two vertices of degree 2 must have disjoint neighborhoods. Each has 2 neighbors among 4 vertices. Disjoint neighborhoods of size 2 in 4 vertices means they partition the 4 vertices (minus themselves). 

Let the degree-2 vertices be $u$ and $v$. $N(u)$ and $N(v)$ are disjoint, each of size 2. $|N(u) \cup N(v)| = 4$. But $N(u) \cup N(v) \subseteq \{u,v, \text{others}\}$... actually $N(u) \subseteq V \setminus \{u\}$ and $N(v) \subseteq V \setminus \{v\}$. So $N(u) \cup N(v) \subseteq V$, and $|N(u) \cup N(v)| = 4 = |V|$. So $N(u) \cup N(v) = V$.

But $u \notin N(u)$, so $u \in N(v)$ (since $u \in V = N(u) \cup N(v)$ and $u \notin N(u)$). Similarly $v \in N(u)$. So $u$ and $v$ are friends.

Also, the other two vertices (call them $a, b$): $a \in N(u) \cup N(v)$, so $a$ is a friend of $u$ or $v$ (or both, but since disjoint, exactly one). Similarly for $b$.

The degree-3 vertex is friends with everyone. Say $a$ has degree 3. Then $a \in N(u)$ or $a \in N(v)$. WLOG $a \in N(u)$. Then $a$ is friends with $u, v, b$. So $v \in N(a)$ and $u \in N(a)$. 

The degree-1 vertex is $b$, friends with only $a$ (since $a$ has degree 3 and is friends with everyone including $b$). So $N(b) = \{a\}$.

Now $N(u) = \{v, a\}$ (since $u$ has degree 2, friends with $v$ and $a$). $N(v) = \{u, b\}$ (since $v$ has degree 2, friends with $u$ and $b$; $v$ can't be friends with $a$ because $a$ is in $N(u)$ and neighborhoods are disjoint).

Check: $N(u) \cap N(v) = \{v,a\} \cap \{u,b\} = \emptyset$. ✓

But wait, $a$ has degree 3: friends with $u, v, b$. $N(a) = \{u, v, b\}$. And $b$ has degree 1: $N(b) = \{a\}$.

Now check all same-degree pairs:
- Degree 2: $u, v$. $N(u) \cap N(v) = \emptyset$. ✓
- All other degrees are distinct.

So this graph is: $u-v, u-a, v-b, a-v, a-b$. Wait, let me list edges: $u-v, u-a, v-b, a-v, a-b$. That's 5 edges. But the degree sequence should be $1,2,2,3$ with sum 8, so 4 edges. Let me recheck.

$\deg(u) = 2$: friends $v, a$. ✓
$\deg(v) = 2$: friends $u, b$. But I also said $a$ is friends with $v$. That would make $\deg(v) = 3$. Contradiction!

Let me redo. $a$ has degree 3, so $a$ is friends with $u, v, b$. But $v$ has degree 2, and $v$ is friends with $u$ (shown above) and one other. If $a$ is friends with $v$, then $v$'s friends are $u$ and $a$, so $N(v) = \{u, a\}$. But then $N(u) = \{v, a\}$ and $N(v) = \{u, a\}$, and $N(u) \cap N(v) = \{a\} \neq \emptyset$. Violates the condition!

So the issue is: the degree-3 vertex must be friends with both degree-2 vertices (since it's friends with everyone), but then both degree-2 vertices have the degree-3 vertex as a common neighbor. This violates the condition.

So the real constraint is stronger. If a vertex $w$ has degree $2n-1$ (friends with everyone), then any two vertices $u, v$ with the same degree both have $w$ as a neighbor, so $w \in N(u) \cap N(v)$, meaning they have a common friend. This violates the condition unless no two vertices have the same degree. But with $2n$ vertices and at most $2n-1$ distinct degrees (can't have 0 if someone has degree $2n-1$), we must have at least one repeated degree. Contradiction!

So **no vertex can have degree $2n-1$**. This means the maximum degree is at most $2n-2$.

Similarly, if a vertex has degree $2n-2$, it's friends with all but one vertex. If two vertices $u, v$ have the same degree $d$ and both are friends with this degree-$(2n-2)$ vertex, they share a common friend. The degree-$(2n-2)$ vertex is not friends with exactly one vertex $w$. So any two same-degree vertices that are both friends with the degree-$(2n-2)$ vertex share a common friend.

If $u$ and $v$ have the same degree and both are not $w$ (the one non-friend of the high-degree vertex), then they're both friends with the high-degree vertex, sharing a common friend. Unless one of them IS $w$.

So for any degree $d$ that appears more than once, at most one of the vertices with degree $d$ can be a non-friend of the degree-$(2n-2)$ vertex. All others are friends with the high-degree vertex and thus share it as a common friend.

This means: for any repeated degree $d$, at most 2 vertices can have degree $d$ (one is $w$, one is a friend of the high-degree vertex—but wait, if two are friends of the high-degree vertex, they share it). Actually, at most 1 vertex with degree $d$ can be a friend of the high-degree vertex (otherwise two friends share the high-degree vertex as common friend). Plus possibly 1 that is $w$. So $k_d \leq 2$ for any repeated degree, and if $k_d = 2$, one of them must be $w$.

But $w$ is a single vertex, so at most one degree value can have $k_d = 2$ with one being $w$. All other repeated degrees must have $k_d \leq 1$... wait, that means they can't be repeated. So at most one degree is repeated, and $k_d = 2$ for that degree.

Hmm, this is getting complicated. Let me think about it more generally.

**Key insight:** If vertex $w$ has degree $\Delta$, then $w$ is a common friend of any two vertices that are both neighbors of $w$ and have the same degree. So for any degree $d$, at most one vertex of degree $d$ can be a neighbor of $w$ (unless there's only one vertex of degree $d$). The non-neighbors of $w$ (there are $2n - 1 - \Delta$ of them, excluding $w$ itself) can have repeated degrees without $w$ being a common friend.

So the vertices can be split into:
- $w$ itself (degree $\Delta$)
- Neighbors of $w$: $\Delta$ vertices. Among these, all degrees must be distinct (since any two with the same degree share $w$ as common friend).
- Non-neighbors of $w$ (excluding $w$): $2n - 1 - \Delta$ vertices. These can have repeated degrees, but still need to satisfy the condition among themselves and with the neighbors.

Actually, the condition applies globally, not just relative to $w$. Two non-neighbors of $w$ with the same degree still need no common friends (which could be among the neighbors of $w$ or other non-neighbors).

This is quite complex. Let me think about a different approach.

**Approach: Think about the structure more carefully.**

Let me consider the degree classes. For each degree $d$, let $S_d$ be the set of vertices with degree $d$. The condition says: for any $u, v \in S_d$ with $u \neq v$, $N(u) \cap N(v) = \emptyset$.

This means the neighborhoods of vertices in $S_d$ are pairwise disjoint. Since each has $d$ neighbors, $|S_d| \cdot d \leq 2n$ (the neighborhoods are disjoint subsets of the $2n$ vertices).

Now, the total number of edges is $\frac{1}{2} \sum_d |S_d| \cdot d$.

We want to maximize this. The constraint is $|S_d| \cdot d \leq 2n$ for each $d$, and $\sum_d |S_d| = 2n$.

But as we saw, this is not sufficient—we also need graphicality and the actual common-neighbor condition to be realizable.

Let me think about what graphs actually satisfy the condition.

**Construction idea: Complete bipartite-like or specific structures.**

Actually, let me think about a specific construction. Consider a graph where vertices are paired up, and within each pair, the two vertices have the same degree but no common friends.

Hmm, let me think about the "friendship graph" where we have a matching plus some additional structure.

Actually, let me think about this problem from the answer's perspective. For $n=1$: 1, $n=2$: 3. Let me guess the answer might be $\binom{2n}{2} - \binom{n}{2} = \frac{2n(2n-1)}{2} - \frac{n(n-1)}{2} = n(2n-1) - \frac{n(n-1)}{2} = \frac{2n(2n-1) - n(n-1)}{2} = \frac{4n^2 - 2n - n^2 + n}{2} = \frac{3n^2 - n}{2}$.

$n=1: 1, n=2: 5$. But we found 3 for $n=2$. So no.

Let me try $n^2 - 1$? $n=1: 0, n=2: 3$. $n=1$ gives 0 but answer is 1. No.

$\frac{n(2n-1)}{2}$? $n=1: 0.5$. No.

$n(2n-1) - n^2 = n^2 - n$? $n=1: 0, n=2: 2$. No.

$2n - 1$? $n=1: 1, n=2: 3$. Could be! Let me check if this makes sense. $2n-1$ for $n=3$ would be 5.

Hmm, but $2n-1$ seems low. With $2n$ vertices, we should be able to do better than a tree-like structure.

Wait, actually for $n=2$, we got 3 which is $2n-1 = 3$. And for $n=1$, $2n-1 = 1$. Let me think about whether we can do better for $n=3$.

For $n=3$, $2n=6$. Can we get more than 5 edges?

Let me try to construct a graph with 6 vertices and more than 5 edges satisfying the condition.

Consider the complete graph $K_6$ minus some edges. $K_6$ has 15 edges. Way too many.

Let me think about a specific construction. Consider a "friendship graph" or a graph with specific degree structure.

**Construction: Path-like or specific degree sequences.**

For $n=2$, the optimal was $P_4$ (path on 4 vertices) with degree sequence $(1,2,2,1)$. The two degree-1 vertices have disjoint neighborhoods, and the two degree-2 vertices have disjoint neighborhoods.

For $n=3$, let me try $P_6$ (path on 6 vertices): $a-b-c-d-e-f$. Degrees: $(1,2,2,2,2,1)$. 
Degree-1: $\{a, f\}$. $N(a)=\{b\}, N(f)=\{e\}$. Disjoint. ✓
Degree-2: $\{b,c,d,e\}$. $N(b)=\{a,c\}, N(c)=\{b,d\}, N(d)=\{c,e\}, N(e)=\{d,f\}$.
$N(b) \cap N(c) = \{a,c\} \cap \{b,d\} = \emptyset$. ✓
$N(b) \cap N(d) = \{a,c\} \cap \{c,e\} = \{c\}$. ✗

So $P_6$ doesn't work. The degree-2 vertices $b$ and $d$ share common friend $c$.

What about a different graph? Let me think about what degree sequences work.

For the condition to hold, vertices of the same degree need disjoint neighborhoods. This is a strong condition.

**Idea: Use many distinct degrees.** If all degrees are distinct, the condition is vacuously satisfied. With $2n$ vertices, we can have at most $2n-1$ distinct degrees (can't have both 0 and $2n-1$). So one degree must repeat.

If we use degrees $\{1, 2, \ldots, 2n-1\}$ with one degree $d \leq n$ repeated, the sum is $n(2n-1) + d$, and edges = $\frac{n(2n-1)+d}{2}$. With $d = n$: $n^2$ edges.

But we need this to be graphical AND satisfy the common-neighbor condition for the repeated degree.

For $n=2$: degrees $\{1,2,2,3\}$, sum 8, 4 edges. We showed this doesn't work because the degree-3 vertex is friends with both degree-2 vertices, making them share a common friend.

The issue is that high-degree vertices are friends with many people, creating common friends.

**Key constraint:** If a vertex $w$ has high degree, it's a common friend of many pairs. Specifically, any two neighbors of $w$ with the same degree violate the condition. So among the neighbors of $w$, all degrees must be distinct.

More generally: for any vertex $w$, the neighbors of $w$ must all have distinct degrees. (Because if two neighbors $u, v$ of $w$ have the same degree, then $w \in N(u) \cap N(v)$, so they have a common friend.)

Wait, that's a very strong condition! Let me verify: if $u$ and $v$ are both neighbors of $w$ and $\deg(u) = \deg(v)$, then $w \in N(u)$ and $w \in N(v)$, so $w \in N(u) \cap N(v) \neq \emptyset$. This violates the condition. So yes, **all neighbors of any vertex must have distinct degrees**.

This is a key insight! Let me restate: **For every vertex $w$, the degrees of its neighbors are all distinct.**

This means: the number of neighbors of $w$ (which is $\deg(w)$) is at most the number of distinct degree values among all vertices. If there are $m$ distinct degree values, then $\deg(w) \leq m$ for all $w$.

Since the maximum degree is at most $m$, and $m \leq 2n-1$ (at most $2n-1$ distinct values), we get $\Delta \leq 2n-1$. But we also showed $\Delta \leq 2n-2$ (can't have degree $2n-1$). 

But more importantly, $\Delta \leq m$ where $m$ is the number of distinct degrees. And $m \leq 2n - 1$. But also, the degree values range from some $d_{\min}$ to $\Delta$, and there are at most $\Delta - d_{\min} + 1$ possible values. So $m \leq \Delta - d_{\min} + 1 \leq \Delta + 1$.

Combined with $\Delta \leq m$: $\Delta \leq m \leq \Delta + 1$ (roughly). So $m \in \{\Delta, \Delta+1\}$ approximately.

Actually, $m \leq \Delta + 1$ (degrees from 0 to $\Delta$, at most $\Delta + 1$ values). And $\Delta \leq m$. So $\Delta \leq m \leq \Delta + 1$.

If $m = \Delta + 1$: all degrees from 0 to $\Delta$ are present. But if 0 is present, some vertex has no friends, and $\Delta \leq 2n - 2$ (can't be friends with the isolated vertex). Also, if all degrees 0 to $\Delta$ are present, that's $\Delta + 1$ distinct values, using at least $\Delta + 1$ vertices (one per degree). The remaining $2n - \Delta - 1$ vertices must have degrees in $\{0, 1, \ldots, \Delta\}$, creating repeats.

If $m = \Delta$: degrees range over $\Delta$ values, not necessarily 0 to $\Delta$.

This is getting complex. Let me use the constraint $\deg(w) \leq m$ for all $w$, where $m$ is the number of distinct degree values.

The total number of edges is $\frac{1}{2} \sum \deg(v) \leq \frac{1}{2} \cdot 2n \cdot m = n \cdot m$.

And $m \leq 2n - 1$ (can't have both 0 and $2n-1$). But also $\Delta \leq m$, and the degrees range from 0 (or some min) to $\Delta$, so $m \leq \Delta + 1 \leq m + 1$.

If $m = 2n - 1$: edges $\leq n(2n-1)$. But $\Delta \leq m = 2n-1$, and we need $\Delta \leq 2n-2$ (no degree $2n-1$). So $\Delta \leq 2n-2$. With $m = 2n-1$ distinct values and max degree $2n-2$, the degrees must be $\{0, 1, \ldots, 2n-2\}$ (all $2n-1$ values from 0 to $2n-2$). One vertex has degree 0, one has degree 1, ..., one has degree $2n-2$, and one extra vertex has some degree in this range.

But the vertex with degree $2n-2$ is friends with $2n-2$ out of $2n-1$ other vertices. It's not friends with exactly one vertex. That one vertex must be the degree-0 vertex (since the degree-0 vertex has no friends). So the degree-$(2n-2)$ vertex is friends with everyone except the isolated vertex.

Now, the neighbors of the degree-$(2n-2)$ vertex are all vertices except itself and the isolated vertex: $2n-2$ vertices. These must all have distinct degrees (by our key constraint). The degrees of these $2n-2$ vertices are from $\{1, 2, \ldots, 2n-2\}$ (excluding 0, since the isolated vertex is not a neighbor). There are $2n-2$ possible degree values and $2n-2$ neighbors, so they must all have distinct degrees: exactly $\{1, 2, \ldots, 2n-2\}$, each appearing once. But we have $2n$ vertices total: one with degree 0, one with degree $2n-2$, and $2n-2$ neighbors with degrees $1, 2, \ldots, 2n-2$. That's $2n$ vertices, and the degree $2n-2$ appears twice (once for the high-degree vertex and once among the neighbors). Wait, the high-degree vertex has degree $2n-2$, and one of the neighbors also has degree $2n-2$? No, the neighbors have degrees $1, 2, \ldots, 2n-2$, which includes $2n-2$. So there are two vertices of degree $2n-2$: the high-degree vertex itself and one neighbor.

But the high-degree vertex and this neighbor are friends (the neighbor is a neighbor of the high-degree vertex). They have the same degree $2n-2$. Do they have a common friend? The high-degree vertex $w$ has $N(w) = V \setminus \{w, \text{isolated}\}$. The neighbor $u$ with degree $2n-2$ has $N(u) = V \setminus \{u, \text{one other}\}$. 

$N(w) \cap N(u)$: $w$ is friends with all except isolated. $u$ is friends with all except $u$ and one other. If the "one other" that $u$ is not friends with is the isolated vertex, then $N(u) = V \setminus \{u, \text{isolated}\}$, and $N(w) \cap N(u) = V \setminus \{w, u, \text{isolated}\}$, which has $2n - 3$ elements. Not empty (for $n \geq 2$). So they have common friends. Violates the condition!

So $m = 2n-1$ with degrees $\{0, 1, \ldots, 2n-2\}$ doesn't work because the repeated degree $2n-2$ causes a problem.

What if the repeated degree is something else? We have degrees $\{0, 1, \ldots, 2n-2\}$ with $2n$ vertices, so one degree is repeated. The sum of degrees is $\sum_{d=0}^{2n-2} d + d_0 = \frac{(2n-2)(2n-1)}{2} + d_0 = (n-1)(2n-1) + d_0$ where $d_0$ is the repeated degree.

For this to be graphical and satisfy the condition, we need the two vertices of degree $d_0$ to have no common friends.

The vertex of degree $2n-2$ is friends with all except the isolated vertex. So the neighbors of this vertex are $V \setminus \{w, \text{isolated}\}$, and they must have distinct degrees. The degrees of these $2n-2$ neighbors are $\{1, 2, \ldots, 2n-2\} \setminus \{2n-2\} \cup \{d_0\}$... hmm, this is getting complicated.

Wait, I think the key constraint $\deg(w) \leq m$ for all $w$ (where $m$ is the number of distinct degree values) is very powerful. Let me use it directly.

We have $m$ distinct degree values, and every degree is at most $m$. The degree values are a subset of $\{0, 1, \ldots, m\}$ (since max degree $\leq m$). But there are $m$ distinct values from $\{0, 1, \ldots, m\}$, which has $m+1$ elements. So the degree values are $\{0, 1, \ldots, m\} \setminus \{d^*\}$ for some $d^*$, or they could be a different subset.

Actually, the degree values are $m$ distinct values, each between 0 and $m$ (inclusive). So they are a subset of $\{0, 1, \ldots, m\}$ of size $m$. This means exactly one value from $\{0, 1, \ldots, m\}$ is missing.

Now, can we have both 0 and $m$ in the degree values? If 0 is present, there's an isolated vertex. If $m$ is present, there's a vertex of degree $m$. This vertex's $m$ neighbors must have distinct degrees, and there are $m$ distinct degree values, so the neighbors' degrees are exactly all $m$ distinct degree values. But the vertex itself has degree $m$, which is one of the $m$ distinct values. So one neighbor has degree $m$ too. That neighbor and the vertex both have degree $m$ and are friends. Do they share a common friend?

The vertex $w$ of degree $m$ has $m$ neighbors with all $m$ distinct degrees. One neighbor $u$ also has degree $m$. $u$'s neighbors must also have distinct degrees, and $u$ has $m$ neighbors. So $u$'s neighbors also have all $m$ distinct degrees. Now $w \in N(u)$ and $u \in N(w)$. $N(w) \cap N(u)$: both have $m$ neighbors, all with distinct degrees. $N(w)$ contains one vertex of each degree, $N(u)$ contains one vertex of each degree. The vertex of degree $d$ in $N(w)$ and the vertex of degree $d$ in $N(u)$ might or might not be the same. 

If for some degree $d \neq m$, the vertex of degree $d$ in $N(w)$ is the same as in $N(u)$, then that vertex is a common friend. Since there are $m-1$ degrees other than $m$ (which corresponds to $w$ and $u$ themselves), and the vertices of those degrees... hmm, this requires more careful analysis.

Actually, let me think about it differently. The vertex of degree $m$ has $m$ neighbors, one of each degree value. The vertex $u$ of degree $m$ (the neighbor) also has $m$ neighbors, one of each degree value. For degree $d$ (where $d \neq m$), there are exactly 2 vertices of degree $d$ (since we have $2n$ vertices, $m$ distinct degrees, and... wait, not necessarily 2).

Hmm, I need to be more careful. Let me count. We have $2n$ vertices and $m$ distinct degree values. The sum of $k_d$ over all $d$ is $2n$. We need $k_d \cdot d \leq 2n$ for each $d$ (from the disjoint neighborhood condition). And $\deg(w) \leq m$ for all $w$ (from the distinct-neighbor-degrees condition).

Let me think about the maximum of $\sum k_d \cdot d$ subject to:
1. $\sum k_d = 2n$
2. $k_d \cdot d \leq 2n$ for each $d$ (disjoint neighborhoods)
3. $d \leq m$ for all $d$ with $k_d > 0$ (distinct neighbor degrees)
4. $m$ = number of distinct degree values = $|\{d : k_d > 0\}|$
5. Can't have both $d = 0$ and $d = 2n-1$ (but since $d \leq m \leq 2n-1$, and if $d = 2n-1$ then $m \geq 2n-1$, meaning all degrees distinct, but then $k_d = 1$ for all and $\sum k_d = 2n$ requires $m = 2n$, contradiction with $m \leq 2n-1$... actually $m$ could be $2n$ if we have degrees 0 to $2n-1$, but that's impossible graphically. Let me not worry about this edge case.)

From constraint 3: all degrees are at most $m$. From constraint 4: there are $m$ distinct degree values, all $\leq m$. So the degree values are a subset of $\{0, 1, \ldots, m\}$ of size $m$, i.e., $\{0, 1, \ldots, m\} \setminus \{d^*\}$ for some $d^*$.

The maximum degree is $m$ (if $d^* \neq m$) or $m-1$ (if $d^* = m$).

Case 1: $d^* = 0$, degree values are $\{1, 2, \ldots, m\}$. Max degree $m$.
Case 2: $d^* = m$, degree values are $\{0, 1, \ldots, m-1\}$. Max degree $m-1 \leq m$. ✓
Case 3: $d^* \in \{1, \ldots, m-1\}$, degree values include both 0 and $m$. Max degree $m$.

In Case 3, we have both degree 0 and degree $m$. The degree-$m$ vertex has $m$ neighbors with all $m$ distinct degrees. But degree 0 is one of the $m$ distinct values, and the degree-0 vertex has no neighbors, so it can't be a neighbor of the degree-$m$ vertex. So the degree-$m$ vertex has $m$ neighbors, but only $m-1$ distinct degrees are available among non-isolated vertices (excluding degree 0). But we need $m$ neighbors with distinct degrees. Contradiction! (Unless the degree-$m$ vertex is itself degree 0, which is absurd.)

Wait, the degree-$m$ vertex needs $m$ neighbors with distinct degrees. The available degrees for neighbors are the $m$ distinct degree values. But the degree-0 vertex can't be a neighbor (it has no friends, so it's not friends with the degree-$m$ vertex). So the degree-$m$ vertex can only be friends with vertices of degrees in $\{1, \ldots, m\} \setminus \{d^*\} \cup \{m\}$... hmm, let me be more precise.

In Case 3, degree values are $\{0, 1, \ldots, m\} \setminus \{d^*\}$ where $d^* \in \{1, \ldots, m-1\}$. So the degree values include 0 and $m$. The degree-$m$ vertex needs $m$ neighbors with distinct degrees. The degree values are $\{0, 1, \ldots, m\} \setminus \{d^*\}$, which has $m$ values. The degree-0 vertex is not a neighbor (isolated). So the degree-$m$ vertex can have neighbors with degrees from $\{1, \ldots, m\} \setminus \{d^*\}$, which has $m-1$ values. But it needs $m$ neighbors with distinct degrees. $m > m-1$. Contradiction!

So Case 3 is impossible. We're left with:
- Case 1: degree values $\{1, 2, \ldots, m\}$ (no isolated vertex, max degree $m$)
- Case 2: degree values $\{0, 1, \ldots, m-1\}$ (isolated vertex, max degree $m-1$)

**Case 1: degree values $\{1, 2, \ldots, m\}$, max degree $m$.**

The degree-$m$ vertex has $m$ neighbors with distinct degrees from $\{1, 2, \ldots, m\}$. One neighbor has degree $m$ (same as the vertex). So there are at least 2 vertices of degree $m$.

The two degree-$m$ vertices are friends (one is a neighbor of the other). They must have no common friends. $N(w)$ and $N(u)$ (where $w, u$ are the two degree-$m$ vertices) are disjoint. Each has $m$ elements. So $|N(w) \cup N(u)| = 2m \leq 2n$, giving $m \leq n$.

Also, $w$ has $m$ neighbors with all $m$ distinct degrees. $u$ has $m$ neighbors with all $m$ distinct degrees. $N(w) \cap N(u) = \emptyset$. So for each degree $d \in \{1, \ldots, m\}$, there's one vertex of degree $d$ in $N(w)$ and one in $N(u)$. That means $k_d \geq 2$ for each $d$ (one in $N(w)$, one in $N(u)$, and possibly $w$ or $u$ themselves if $d = m$).

For $d = m$: $w \in N(u)$ and $u \in N(w)$. The vertex of degree $m$ in $N(w)$ is $u$, and in $N(u)$ is $w$. So $k_m \geq 2$ (just $w$ and $u$). Could be more.

For $d \neq m$: one vertex of degree $d$ in $N(w)$ and one in $N(u)$. These are different vertices (since $N(w) \cap N(u) = \emptyset$). So $k_d \geq 2$.

Total vertices: $\sum k_d \geq 2m$ (at least 2 per degree). But $\sum k_d = 2n$. So $2m \leq 2n$, i.e., $m \leq n$. (Consistent with what we got before.)

If $m = n$: $\sum k_d = 2n$ and $k_d \geq 2$ for each of the $n$ degrees, so $k_d = 2$ for each $d$. The degree values are $\{1, 2, \ldots, n\}$, each appearing exactly twice.

Sum of degrees: $2 \sum_{d=1}^{n} d = 2 \cdot \frac{n(n+1)}{2} = n(n+1)$. Edges: $\frac{n(n+1)}{2}$.

For $n=1$: $\frac{1 \cdot 2}{2} = 1$. ✓ (matches)
For $n=2$: $\frac{2 \cdot 3}{2} = 3$. ✓ (matches!)

So the answer might be $\frac{n(n+1)}{2}$.

But wait, I need to check if this is achievable and if Case 2 could give more.

**Case 2: degree values $\{0, 1, \ldots, m-1\}$, max degree $m-1$, one isolated vertex.**

The degree-$(m-1)$ vertex has $m-1$ neighbors with distinct degrees from $\{1, \ldots, m-1\}$ (excluding 0, since the isolated vertex can't be a neighbor). There are $m-1$ available degrees and $m-1$ neighbors, so each degree from 1 to $m-1$ appears exactly once among the neighbors.

The degree-$(m-1)$ vertex is not a neighbor of itself, and its degree $m-1$ is one of the degree values. Is there another vertex of degree $m-1$? The neighbors have degrees $1, \ldots, m-1$, so one neighbor has degree $m-1$. So $k_{m-1} \geq 2$.

The two degree-$(m-1)$ vertices are friends. They must have no common friends. $N(w) \cap N(u) = \emptyset$ where $w$ is the degree-$(m-1)$ vertex and $u$ is its neighbor of degree $m-1$.

$|N(w)| = |N(u)| = m-1$. $|N(w) \cup N(u)| = 2(m-1) \leq 2n$ (actually $\leq 2n - 1$ since the isolated vertex is in neither). So $2(m-1) \leq 2n - 1$, giving $m \leq n + 1/2$, so $m \leq n$.

Hmm wait, $N(w) \cup N(u) \subseteq V \setminus \{\text{isolated}\}$, which has $2n - 1$ vertices. And $|N(w) \cup N(u)| = 2(m-1)$ (since disjoint). So $2(m-1) \leq 2n - 1$, giving $m \leq n + 1/2$, i.e., $m \leq n$.

With $m = n$: degree values $\{0, 1, \ldots, n-1\}$, $n$ distinct values, $2n$ vertices.

The degree-$(n-1)$ vertex $w$ has $n-1$ neighbors with degrees $1, \ldots, n-1$ (each once). One neighbor $u$ has degree $n-1$. $N(w) \cap N(u) = \emptyset$, $|N(w)| = |N(u)| = n-1$.

$u$ also has $n-1$ neighbors with distinct degrees from $\{1, \ldots, n-1\}$. The neighbors of $u$ include $w$ (degree $n-1$) and $n-2$ others.

$N(w) = \{u, v_1, \ldots, v_{n-2}\}$ where $v_i$ has degree $i$ (for $i = 1, \ldots, n-2$) and $u$ has degree $n-1$. Wait, I need to be more careful. $w$'s neighbors have degrees $1, 2, \ldots, n-1$, one of each. The one with degree $n-1$ is $u$.

$N(u)$: $u$ has $n-1$ neighbors with distinct degrees from $\{1, \ldots, n-1\}$. One of them is $w$ (degree $n-1$). The others have degrees from $\{1, \ldots, n-2\}$, each appearing once. So $N(u) = \{w, u_1, \ldots, u_{n-2}\}$ where $u_i$ has degree $i$.

$N(w) \cap N(u) = \emptyset$. $N(w) = \{u, w_1, \ldots, w_{n-2}\}$ where $w_i$ has degree $i$. $N(u) = \{w, u_1, \ldots, u_{n-2}\}$ where $u_i$ has degree $i$.

For $N(w) \cap N(u) = \emptyset$: $w_i \neq u_j$ for all $i, j$, and $u \neq w$ (yes), and $w \neq w_i$ (yes, $w \notin N(w)$), and $u \neq u_j$ (yes).

So for each degree $i \in \{1, \ldots, n-2\}$, there are at least 2 vertices: $w_i$ and $u_i$. Plus the degree-0 vertex (isolated), and $w, u$ (degree $n-1$). That's $2 + 2(n-2) + 2 = 2n$ vertices. So $k_i = 2$ for $i = 1, \ldots, n-2$, $k_{n-1} = 2$, $k_0 = 1$. Wait, that's $2(n-2) + 2 + 1 = 2n - 1$. We need $2n$ vertices. So one more vertex. 

Hmm, I think I miscounted. Let me redo. Degree values $\{0, 1, \ldots, n-1\}$, $n$ values. $k_0 + k_1 + \ldots + k_{n-1} = 2n$.

From the structure: $k_0 = 1$ (isolated), $k_{n-1} = 2$ ($w$ and $u$), $k_i = 2$ for $i = 1, \ldots, n-2$ (from $w_i$ and $u_i$). Total: $1 + 2 + 2(n-2) = 2n - 1$. Need 1 more vertex. This extra vertex has some degree $d \in \{0, 1, \ldots, n-1\}$, making $k_d = 3$ (or $k_0 = 2$ if $d = 0$).

If the extra vertex has degree $d$ with $k_d$ becoming 3, we need 3 vertices of degree $d$ with pairwise disjoint neighborhoods. $3d \leq 2n$, so $d \leq 2n/3$.

Sum of degrees: $\sum k_d \cdot d = 0 \cdot k_0 + \sum_{d=1}^{n-2} 2d + 2(n-1) + d_{\text{extra}} = 2 \cdot \frac{(n-2)(n-1)}{2} + 2(n-1) + d_{\text{extra}} = (n-2)(n-1) + 2(n-1) + d_{\text{extra}} = (n-1)(n-2+2) + d_{\text{extra}} = n(n-1) + d_{\text{extra}}$.

Edges: $\frac{n(n-1) + d_{\text{extra}}}{2}$. To maximize, $d_{\text{extra}}$ should be as large as possible, up to $\lfloor 2n/3 \rfloor$.

For $n=2$: $m = n = 2$, degree values $\{0, 1\}$. $k_0 + k_1 = 4$. From structure: $k_0 = 1, k_1 = 2$, total 3, need 1 more. Extra vertex of degree 0 or 1. If degree 1: $k_1 = 3$, need $3 \cdot 1 = 3 \leq 4$. Sum = $3 \cdot 1 = 3$. Edges = 1.5. Not integer. If degree 0: $k_0 = 2, k_1 = 2$. Sum = 2. Edges = 1. That's worse than Case 1's 3.

So Case 2 is worse for $n=2$. Let me check for general $n$.

Case 1 with $m = n$: edges = $\frac{n(n+1)}{2}$.
Case 2 with $m = n$: edges = $\frac{n(n-1) + d_{\text{extra}}}{2} \leq \frac{n(n-1) + \lfloor 2n/3 \rfloor}{2}$.

For large $n$, Case 1 gives $\sim n^2/2$ and Case 2 gives $\sim n^2/2$ too. Let's compare more carefully.

Case 1: $\frac{n(n+1)}{2} = \frac{n^2 + n}{2}$.
Case 2: $\frac{n(n-1) + 2n/3}{2} = \frac{n^2 - n + 2n/3}{2} = \frac{n^2 - n/3}{2} = \frac{n^2}{2} - \frac{n}{6}$.

Case 1 is larger. So Case 1 is better.

But wait, I should also check if $m < n$ could be better in either case, or if there are other configurations.

Actually, let me reconsider. In Case 1, I showed $m \leq n$ and with $m = n$, edges = $\frac{n(n+1)}{2}$. Can we have $m > n$ in some other configuration?

In Case 1, the constraint was $m \leq n$ (from $2m \leq 2n$). In Case 2, $m \leq n$ as well. Are there other cases?

Actually, I think I was too restrictive. Let me reconsider. The constraint $\deg(w) \leq m$ for all $w$ means max degree $\leq m$. But what if the max degree is less than $m$? Then we could have $m$ distinct degree values all less than $m$, which is fine.

Wait, if max degree $\Delta < m$, then the degree values are $m$ distinct values from $\{0, 1, \ldots, \Delta\}$, which has $\Delta + 1 < m + 1$ elements. So $m \leq \Delta + 1 \leq m$, meaning $\Delta = m - 1$ and the degree values are $\{0, 1, \ldots, m-1\}$. This is Case 2!

So the two cases are exhaustive:
- Case 1: max degree $= m$, degree values include $m$ but not 0 (since including both 0 and $m$ is impossible as shown).
- Case 2: max degree $= m - 1$, degree values are $\{0, 1, \ldots, m-1\}$.

And in both cases, $m \leq n$.

Wait, I need to re-examine Case 1 more carefully. In Case 1, degree values are $\{1, 2, \ldots, m\}$ (excluding 0, including $m$). But could the degree values be a different subset of $\{0, 1, \ldots, m\}$ of size $m$ that includes $m$ but not 0? Yes, that's exactly $\{1, 2, \ldots, m\}$ (the only subset of size $m$ from $\{0, 1, \ldots, m\}$ that includes $m$ but not 0).

OK so in Case 1, $m \leq n$ and the best is $m = n$ giving $\frac{n(n+1)}{2}$ edges.

But I haven't verified that Case 1 with $m = n$ is actually achievable! I need to construct such a graph.

**Construction for Case 1, $m = n$:**

Degree values $\{1, 2, \ldots, n\}$, each appearing exactly twice. $2n$ vertices. Sum of degrees $= n(n+1)$, edges $= \frac{n(n+1)}{2}$.

We need: for each degree $d$, the two vertices of degree $d$ have disjoint neighborhoods. And for every vertex, its neighbors have distinct degrees.

Let me think of a construction. Label the vertices as $(d, 0)$ and $(d, 1)$ for $d = 1, \ldots, n$ (two vertices per degree).

We need:
1. $\deg(d, i) = d$ for each $d, i$.
2. $N(d, 0) \cap N(d, 1) = \emptyset$ for each $d$.
3. For each vertex $v$, the degrees of its neighbors are all distinct.

Condition 3 means: for each vertex $v$, its neighbors have distinct degrees, i.e., at most one neighbor of each degree. Since there are $n$ degree values and $\deg(v) \leq n$, this means $v$ has at most one neighbor of each degree.

So the graph is "degree-regular" in the sense that each vertex has at most one friend of each degree. This is like a bipartite-like structure.

Let me think of this as follows. Consider a bipartite graph where on one side we have the "0" copies and on the other the "1" copies. Actually, let me think of it differently.

For each degree $d$, we have two vertices $a_d$ and $b_d$. We need $N(a_d) \cap N(b_d) = \emptyset$.

One natural construction: make the graph bipartite with parts $A = \{a_1, \ldots, a_n\}$ and $B = \{b_1, \ldots, b_n\}$, where all edges go between $A$ and $B$. Then $N(a_d) \subseteq B$ and $N(b_d) \subseteq A$, so $N(a_d) \cap N(b_d) = \emptyset$ automatically (since $A \cap B = \emptyset$). ✓

Now we need $\deg(a_d) = \deg(b_d) = d$ for each $d$. And for each vertex, its neighbors have distinct degrees.

In the bipartite graph, $a_d$'s neighbors are in $B$, and they must have distinct degrees. So $a_d$ is connected to $d$ vertices in $B$, each with a different degree. Similarly for $b_d$.

So we need a bipartite graph between $A = \{a_1, \ldots, a_n\}$ and $B = \{b_1, \ldots, b_n\}$ where:
- $\deg(a_d) = d$ and $\deg(b_d) = d$ for all $d$.
- The neighbors of each $a_d$ have distinct degrees (i.e., $a_d$ is connected to at most one $b_j$ for each $j$).
- The neighbors of each $b_d$ have distinct degrees (i.e., $b_d$ is connected to at most one $a_j$ for each $j$).

The last two conditions are automatically satisfied in a bipartite graph if we think of it as: $a_d$ is connected to $d$ vertices in $B$, and since each $b_j$ has a unique degree $j$, the neighbors of $a_d$ automatically have distinct degrees as long as $a_d$ is connected to at most one vertex of each degree—i.e., at most one $b_j$ for each $j$. But since there's only one $b_j$ for each $j$, this is automatic!

Wait, that's the key. In the bipartite graph, each $b_j$ is the only vertex with degree $j$ in $B$. So $a_d$'s neighbors in $B$ automatically have distinct degrees. Similarly, each $a_j$ is the only vertex with degree $j$ in $A$, so $b_d$'s neighbors in $A$ automatically have distinct degrees.

So we just need a bipartite graph between $A$ and $B$ with $\deg(a_d) = \deg(b_d) = d$ for all $d = 1, \ldots, n$. This is a bipartite graph with degree sequences $(1, 2, \ldots, n)$ on both sides.

By the Gale-Ryser theorem, such a bipartite graph exists if and only if the degree sequence $(1, 2, \ldots, n)$ is bipartite-graphical with itself. The condition is that for all $k$, $\sum_{i=1}^{k} d_i \leq \sum_{i=1}^{n} \min(d_i, k)$ where $d_i$ are sorted in decreasing order.

Degree sequence sorted decreasingly: $(n, n-1, \ldots, 2, 1)$.

For $k = 1$: $n \leq \sum_{i=1}^{n} \min(d_i, 1) = n$. ✓ (equality)
For $k = 2$: $n + (n-1) \leq \sum \min(d_i, 2) = 2 + 2 + \ldots + 2 + 1 = 2(n-1) + 1 = 2n - 1$. Need $2n - 1 \leq 2n - 1$. ✓
For general $k$: $\sum_{i=1}^{k} (n - i + 1) = \sum_{j=n-k+1}^{n} j = \frac{k(2n - k + 1)}{2}$. And $\sum_{i=1}^{n} \min(n - i + 1, k) = \sum_{j=1}^{n} \min(j, k) = \sum_{j=1}^{k} j + \sum_{j=k+1}^{n} k = \frac{k(k+1)}{2} + k(n - k) = \frac{k(k+1) + 2k(n-k)}{2} = \frac{k(k + 1 + 2n - 2k)}{2} = \frac{k(2n - k + 1)}{2}$.

So the LHS equals the RHS for all $k$! The condition is satisfied with equality. So the bipartite graph exists.

In fact, the bipartite graph with degree sequences $(1, 2, \ldots, n)$ on both sides is the "triangular" or "threshold" bipartite graph. One explicit construction: connect $a_i$ to $b_j$ if and only if $i + j \geq n + 1$ (or some similar threshold condition).

Let me verify: if $a_i$ is connected to $b_j$ iff $i + j \geq n + 1$, then $\deg(a_i) = |\{j : i + j \geq n + 1\}| = |\{j : j \geq n + 1 - i\}| = |\{j : n + 1 - i \leq j \leq n\}| = i$. ✓

And $\deg(b_j) = |\{i : i + j \geq n + 1\}| = |\{i : i \geq n + 1 - j\}| = j$. ✓

So the bipartite graph with edges $\{a_i b_j : i + j \geq n + 1\}$ works. The number of edges is $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$.

Now let me verify the original condition:
1. Same degree, no common friends: vertices $a_d$ and $b_d$ both have degree $d$. $N(a_d) \subseteq B$ and $N(b_d) \subseteq A$, so $N(a_d) \cap N(b_d) = \emptyset$. ✓
2. But wait, we also need to check: are there other pairs with the same degree? In this construction, $a_d$ and $b_d$ are the only two vertices of degree $d$. And their neighborhoods are disjoint (one in $B$, one in $A$). ✓

So the construction works and gives $\frac{n(n+1)}{2}$ edges.

Now I need to verify this is optimal. We showed:
- $m \leq n$ (in both cases)
- Case 1 with $m = n$: edges $= \frac{n(n+1)}{2}$
- Case 2 with $m = n$: edges $\leq \frac{n(n-1) + \lfloor 2n/3 \rfloor}{2} < \frac{n(n+1)}{2}$ for $n \geq 2$

But wait, I need to be more careful about the upper bound. Let me re-examine.

In Case 1 with $m = n$: I showed $k_d = 2$ for all $d \in \{1, \ldots, n\}$, giving edges $= \frac{n(n+1)}{2}$. But what if $m < n$? Could we get more edges?

In Case 1 with $m < n$: degree values $\{1, \ldots, m\}$, $m < n$. The constraint $k_d \cdot d \leq 2n$ for each $d$. And $\sum k_d = 2n$.

The max degree is $m$, and each vertex has at most $m$ neighbors with distinct degrees (at most one of each degree). So $\deg(v) \leq m$ for all $v$, which is already given.

Total edges $= \frac{1}{2} \sum k_d \cdot d \leq \frac{1}{2} \sum_{d=1}^{m} 2n = \frac{1}{2} \cdot m \cdot 2n = mn$. But also $\sum k_d = 2n$ and $k_d \geq 2$ (from the structure: each degree needs at least 2 vertices, one in $N(w)$ and one in $N(u)$ where $w, u$ are the degree-$m$ pair). Actually, I'm not sure $k_d \geq 2$ for all $d$ in general.

Hmm, let me reconsider. In Case 1 with general $m$, the degree-$m$ vertex $w$ has $m$ neighbors with distinct degrees $1, \ldots, m$. One neighbor $u$ has degree $m$. $N(w) \cap N(u) = \emptyset$, $|N(w)| = |N(u)| = m$. $u$ also has $m$ neighbors with distinct degrees. So for each degree $d \in \{1, \ldots, m\}$, there's one vertex of degree $d$ in $N(w)$ and one in $N(u)$ (for $d = m$, these are $u \in N(w)$ and $w \in N(u)$). So $k_d \geq 2$ for all $d$.

$\sum k_d = 2n$ and $k_d \geq 2$ for $m$ degrees, so $2m \leq 2n$, $m \leq n$. And the remaining $2n - 2m$ vertices have degrees in $\{1, \ldots, m\}$, increasing some $k_d$ beyond 2.

Edges $= \frac{1}{2} \sum k_d \cdot d$. To maximize, we want to assign the extra $2n - 2m$ vertices to the highest possible degrees. For degree $d$, the constraint is $k_d \cdot d \leq 2n$, so $k_d \leq \lfloor 2n/d \rfloor$.

With $k_d \geq 2$ and $k_d \leq \lfloor 2n/d \rfloor$, the extra capacity for degree $d$ is $\lfloor 2n/d \rfloor - 2$.

For $d = m$: extra capacity $\lfloor 2n/m \rfloor - 2$. For $m = n$, this is $2 - 2 = 0$. For $m < n$, $\lfloor 2n/m \rfloor \geq 3$ (for $m \leq 2n/3$), so extra capacity $\geq 1$.

This is getting complicated. Let me think about whether $m < n$ can beat $m = n$.

With $m = n$: edges $= \frac{n(n+1)}{2}$.

With $m < n$: we have $m$ degree values, each with $k_d \geq 2$, and $2n - 2m$ extra vertices. The total edges is $\frac{1}{2} \sum k_d \cdot d$.

$\sum k_d \cdot d = \sum_{d=1}^{m} k_d \cdot d$. We have $k_d \geq 2$ and $k_d \leq \lfloor 2n/d \rfloor$ and $\sum k_d = 2n$.

To maximize $\sum k_d \cdot d$, assign extra vertices to highest degrees. 

$\sum k_d \cdot d \geq 2 \sum_{d=1}^{m} d = m(m+1)$ (baseline with $k_d = 2$). Plus extra: $(2n - 2m)$ vertices assigned to maximize $\sum d$. Best to assign to degree $m$ (highest), up to capacity $\lfloor 2n/m \rfloor - 2$.

If $2n - 2m \leq \lfloor 2n/m \rfloor - 2$ (enough capacity at degree $m$): extra contribution $= (2n - 2m) \cdot m$. Total $= m(m+1) + (2n - 2m)m = m(m + 1 + 2n - 2m) = m(2n - m + 1)$. Edges $= \frac{m(2n - m + 1)}{2}$.

This is a quadratic in $m$: $f(m) = \frac{m(2n - m + 1)}{2} = \frac{2nm + m - m^2}{2}$. Maximum at $m = n + 1/2$, so $m = n$ gives $f(n) = \frac{n(n+1)}{2}$.

For $m < n$: $f(m) = \frac{m(2n - m + 1)}{2} < \frac{n(n+1)}{2}$ (since $f$ is increasing for $m < n + 1/2$).

But this assumes all extra vertices go to degree $m$. If capacity at degree $m$ is limited, we'd need to use lower degrees, getting even less.

Wait, but I also need to check: is the constraint $k_d \cdot d \leq 2n$ the only constraint, or are there additional constraints from the common-neighbor condition?

The constraint $k_d \cdot d \leq 2n$ comes from the disjoint neighborhood condition. But there might be additional constraints. For instance, if $k_d = 3$, the three vertices of degree $d$ need pairwise disjoint neighborhoods, which is harder to achieve.

Also, I assumed the graph is bipartite in the construction, but the upper bound should hold for any graph.

Let me also check: in the bipartite construction with $m = n$, is the constraint $k_d \cdot d \leq 2n$ satisfied? $k_d = 2, d \leq n$, so $2d \leq 2n$. ✓

And the "distinct neighbor degrees" condition: in the bipartite graph, each $a_d$ has neighbors in $B$ with distinct degrees (since each degree appears once in $B$). ✓

So the construction achieves $\frac{n(n+1)}{2}$ edges, and the upper bound analysis shows this is optimal (since $m \leq n$ and the maximum of $f(m) = \frac{m(2n-m+1)}{2}$ over $m \leq n$ is at $m = n$).

Wait, but I need to be more careful about the upper bound. I showed that in Case 1, $m \leq n$ and the edges are at most $\frac{m(2n - m + 1)}{2} \leq \frac{n(n+1)}{2}$. But I assumed all extra vertices can go to degree $m$, which might not be possible due to the constraint $k_m \cdot m \leq 2n$.

With $m = n$: $k_n \cdot n \leq 2n$ gives $k_n \leq 2$. And we need $k_n \geq 2$, so $k_n = 2$. No extra capacity. All $k_d = 2$. Edges $= \frac{n(n+1)}{2}$. ✓

With $m = n - 1$: $f(n-1) = \frac{(n-1)(2n - n + 1 + 1)}{2} = \frac{(n-1)(n+2)}{2} = \frac{n^2 + n - 2}{2}$. Compare with $\frac{n^2 + n}{2}$. So $f(n-1) = f(n) - 1$. Just 1 less.

But can we actually achieve $f(n-1)$? We need $k_{n-1} \leq \lfloor 2n/(n-1) \rfloor = 2$ (for $n \geq 3$). So $k_{n-1} = 2$, no extra capacity at top degree. Extra vertices go to degree $n-2$: $k_{n-2} \leq \lfloor 2n/(n-2) \rfloor$. For $n \geq 4$, this is 2. So again no extra capacity. Hmm, for high degrees, the capacity is exactly 2.

For $m = n - 1$: degrees $1, \ldots, n-1$, each with $k_d \geq 2$. Total baseline: $2(n-1)$. Extra: $2n - 2(n-1) = 2$ vertices. These need to go to some degree $d$ with $k_d \leq \lfloor 2n/d \rfloor$. For $d = n-1$: $k \leq 2$, already at 2. For $d = n-2$: $k \leq \lfloor 2n/(n-2) \rfloor$. For $n = 4$: $\lfloor 8/2 \rfloor = 4$, so $k_2$ can go up to 4, extra capacity 2. So both extra vertices go to degree 2. $k_2 = 4$.

But then we need 4 vertices of degree 2 with pairwise disjoint neighborhoods. $4 \cdot 2 = 8 = 2n$. So the 4 neighborhoods of size 2 partition the 8 vertices. This is very restrictive.

Also, the "distinct neighbor degrees" condition: each vertex has at most one neighbor of each degree. With $m = n - 1$ distinct degrees, each vertex has degree $\leq n - 1$. A vertex of degree $n - 1$ has $n - 1$ neighbors, one of each degree $1, \ldots, n-1$. This is fine.

But the question is whether such a graph exists and satisfies all conditions. This is harder to verify.

In any case, the upper bound is $\frac{n(n+1)}{2}$ (achieved at $m = n$), and we have a construction achieving it. So the answer is $\frac{n(n+1)}{2}$.

But wait, I should double-check the upper bound more carefully. I claimed that in Case 1, $m \leq n$. Let me re-derive this.

In Case 1: degree values $\{1, \ldots, m\}$, max degree $m$. The degree-$m$ vertex $w$ has $m$ neighbors with distinct degrees (one of each degree $1, \ldots, m$). One neighbor $u$ has degree $m$. $N(w) \cap N(u) = \emptyset$, $|N(w)| = |N(u)| = m$. So $|N(w) \cup N(u)| = 2m \leq 2n$ (they're subsets of the $2n$ vertices). So $m \leq n$.

But what if there are more than 2 vertices of degree $m$? Say $k_m = 3$. Then we have 3 vertices of degree $m$ with pairwise disjoint neighborhoods. $3m \leq 2n$, so $m \leq 2n/3$. This allows $m$ to be at most $2n/3$, which is less than $n$. So having more vertices of the max degree reduces $m$.

What if $k_m = 2$ but there are other degrees with $k_d > 2$? The constraint $k_d \cdot d \leq 2n$ still applies. The key constraint is $2m \leq 2n$ (from the two degree-$m$ vertices), giving $m \leq n$.

So in all sub-cases of Case 1, $m \leq n$. ✓

And the total edges $\leq \frac{n(n+1)}{2}$ as shown. ✓

Now let me also verify Case 2 more carefully to make sure it can't beat $\frac{n(n+1)}{2}$.

In Case 2: degree values $\{0, 1, \ldots, m-1\}$, max degree $m-1$, one isolated vertex. $m \leq n$ (shown earlier).

The degree-$(m-1)$ vertex $w$ has $m-1$ neighbors with distinct degrees $1, \ldots, m-1$. One neighbor $u$ has degree $m-1$. $N(w) \cap N(u) = \emptyset$, $|N(w)| = |N(u)| = m-1$. $|N(w) \cup N(u)| = 2(m-1) \leq 2n - 1$ (excluding the isolated vertex). So $m \leq n + 1/2$, $m \leq n$.

With $m = n$: degree values $\{0, 1, \ldots, n-1\}$. $k_0 = 1$ (isolated), $k_d \geq 2$ for $d = 1, \ldots, n-1$ (from the structure). Total: $1 + 2(n-1) = 2n - 1$. Need 1 more vertex with degree $d \in \{0, \ldots, n-1\}$.

If extra vertex has degree 0: $k_0 = 2$. Two isolated vertices. Sum of degrees $= 2 \sum_{d=1}^{n-1} d = (n-1)n$. Edges $= \frac{n(n-1)}{2} < \frac{n(n+1)}{2}$.

If extra vertex has degree $d \geq 1$: $k_d = 3$. Need $3d \leq 2n$, so $d \leq 2n/3$. Sum of degrees $= 2\sum_{d=1}^{n-1} d + d_{\text{extra}} = n(n-1) + d_{\text{extra}}$. Edges $= \frac{n(n-1) + d_{\text{extra}}}{2} \leq \frac{n(n-1) + 2n/3}{2} = \frac{n^2 - n + 2n/3}{2} = \frac{n^2 - n/3}{2} = \frac{n^2}{2} - \frac{n}{6}$.

Compare with $\frac{n(n+1)}{2} = \frac{n^2 + n}{2}$. The difference is $\frac{n^2 + n}{2} - \frac{n^2 - n/3}{2} = \frac{n + n/3}{2} = \frac{2n}{3}$. So Case 2 is worse by $\frac{2n}{3}$.

So Case 1 with $m = n$ is optimal, giving $\frac{n(n+1)}{2}$ edges.

Let me also verify for $n = 3$: $\frac{3 \cdot 4}{2} = 6$. 

Construction: bipartite graph with $A = \{a_1, a_2, a_3\}$, $B = \{b_1, b_2, b_3\}$. Edges: $a_i b_j$ iff $i + j \geq 4$.
- $a_1 b_3$ (1+3=4 ✓)
- $a_2 b_2$ (2+2=4 ✓), $a_2 b_3$ (2+3=5 ✓)
- $a_3 b_1$ (3+1=4 ✓), $a_3 b_2$ (3+2=5 ✓), $a_3 b_3$ (3+3=6 ✓)

Degrees: $\deg(a_1) = 1, \deg(a_2) = 2, \deg(a_3) = 3, \deg(b_1) = 1, \deg(b_2) = 2, \deg(b_3) = 3$. ✓

Same-degree pairs: $(a_1, b_1)$ both degree 1, $(a_2, b_2)$ both degree 2, $(a_3, b_3)$ both degree 3.
$N(a_1) = \{b_3\}, N(b_1) = \{a_3\}$. Disjoint. ✓
$N(a_2) = \{b_2, b_3\}, N(b_2) = \{a_2, a_3\}$. Disjoint. ✓
$N(a_3) = \{b_1, b_2, b_3\}, N(b_3) = \{a_1, a_2, a_3\}$. Disjoint. ✓

6 edges. ✓

Now let me also verify the upper bound argument is complete. The key steps:

1. **Key lemma**: For any vertex $w$, all neighbors of $w$ have distinct degrees. (Because if two neighbors $u, v$ of $w$ have the same degree, $w$ is their common friend, violating the condition.)

2. **Consequence**: $\deg(w) \leq m$ for all $w$, where $m$ is the number of distinct degree values.

3. **Degree values**: The $m$ distinct degree values are all in $\{0, 1, \ldots, m\}$ (since max degree $\leq m$). So they're a subset of size $m$ from $\{0, \ldots, m\}$, meaning exactly one value from $\{0, \ldots, m\}$ is missing.

4. **Can't have both 0 and $m$**: If 0 and $m$ are both present, the degree-$m$ vertex needs $m$ neighbors with distinct degrees, but the degree-0 vertex can't be a neighbor, leaving only $m-1$ available degrees. Contradiction. So either 0 is missing (Case 1) or $m$ is missing (Case 2).

5. **Case 1** (degree values $\{1, \ldots, m\}$): The degree-$m$ vertex and its degree-$m$ neighbor have disjoint neighborhoods of size $m$ each, so $2m \leq 2n$, giving $m \leq n$.

6. **Case 2** (degree values $\{0, \ldots, m-1\}$): Similar argument gives $m \leq n$.

7. **Upper bound on edges**: In Case 1 with $m \leq n$, edges $\leq \frac{m(2n - m + 1)}{2} \leq \frac{n(n+1)}{2}$ (the function is maximized at $m = n$). In Case 2, edges are even fewer.

8. **Construction**: Bipartite graph with parts $\{a_1, \ldots, a_n\}$ and $\{b_1, \ldots, b_n\}$, edge $a_i b_j$ iff $i + j \geq n + 1$. This gives $\frac{n(n+1)}{2}$ edges and satisfies all conditions.

Wait, I need to be more careful about step 7. Let me re-derive the upper bound for Case 1.

In Case 1, degree values $\{1, \ldots, m\}$, $m \leq n$. We have $k_d \geq 2$ for all $d$ (shown earlier). $\sum k_d = 2n$. $\sum k_d \cdot d \leq \sum_{d=1}^{m} \min(k_d, \lfloor 2n/d \rfloor) \cdot d$.

Actually, the constraint is $k_d \cdot d \leq 2n$ for each $d$. So $k_d \leq \lfloor 2n/d \rfloor$.

$\sum k_d \cdot d \leq \sum_{d=1}^{m} \lfloor 2n/d \rfloor \cdot d \leq \sum_{d=1}^{m} 2n = 2nm$.

But also $\sum k_d = 2n$ and $k_d \geq 2$, so $2m \leq 2n$, $m \leq n$.

The bound $\sum k_d \cdot d \leq 2nm$ gives edges $\leq nm \leq n^2$. But this is weaker than $\frac{n(n+1)}{2}$ for $n \geq 2$ (since $n^2 > \frac{n(n+1)}{2}$ for $n \geq 
