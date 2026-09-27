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
  <problem_id>polymath_00315</problem_id>
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

The country has $n \ge 3$ airports, some pairs of which are connected by bidirectional flights. Every day, the government closes the airport with the strictly highest number of flights going out of it. What is the maximum number of days this can continue?

[i]Proposed by Fedir Yudin[/i]

## Standard Solution

1. **Base Case for \( n = 3 \):**
   - For \( n = 3 \), consider a graph with 3 vertices and 2 edges. The possible configurations are:
     - A triangle (each vertex connected to the other two).
     - A line (one vertex connected to the other two, and those two are not connected to each other).
   - In both cases, removing the vertex with the highest degree (2) leaves a graph with only one edge, and no further removals are possible. Thus, the maximum number of days is 1.

2. **General Case for \( n \ge 4 \):**
   - We need to construct a graph such that the removal process can continue for \( n - 3 \) days.
   - Label the vertices \( v_1, v_2, \ldots, v_n \).
   - Connect \( v_1 \) to \( v_2, v_3, \ldots, v_{n-1} \).
   - Connect \( v_n \) to \( v_2, v_3, \ldots, v_{n-2} \).
   - Continue this pattern until \( v_5 \) is connected to \( v_2, v_3 \).

3. **Verification of the Construction:**
   - Initially, \( v_1 \) has the highest degree and is removed first.
   - After removing \( v_1 \), \( v_n \) has the highest degree and is removed next.
   - This pattern continues with \( v_{n-1}, v_{n-2}, \ldots \) being removed in sequence.
   - Each removal reduces the graph to a smaller graph with the same structure, allowing the process to continue.

4. **Upper Bound for \( n = 4 \):**
   - Suppose we could make two moves. The first move must delete a vertex with degree at least 2.
   - If the first vertex deleted has degree 2, the next deletion must have a vertex with degree 1, which is not possible since the adjacent vertex would also have degree 1.
   - Therefore, the first vertex deleted must have degree 3. After its deletion, all remaining vertices have degrees at most 1, preventing further deletions.

5. **General Upper Bound for \( n > 4 \):**
   - After each move, the problem reduces to a smaller graph with \( n - 1 \) vertices.
   - Thus, we can perform at most \( n - 4 \) moves, leading to a total of \( n - 3 \) moves.

\(\blacksquare\)

The final answer is \( \boxed{ n - 3 } \) for \( n \ge 4 \) and 1 for \( n = 3 \).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have $n \ge 3$ airports, some pairs connected by bidirectional flights. Every day, the government closes the airport with the strictly highest number of flights going out of it. We need to find the maximum number of days this can continue.

First, let me understand the problem. We have a graph $G$ on $n$ vertices. Each day, we remove the vertex with the strictly highest degree. If there's a tie for the highest degree, then there's no "strictly highest" — so the process stops when there's no vertex with strictly highest degree, i.e., when the maximum degree is achieved by at least 2 vertices.

Wait, let me re-read. "Every day, the government closes the airport with the strictly highest number of flights going out of it."

So each day, we look at the current graph, find the vertex with strictly highest degree. If there's a unique vertex with maximum degree, we remove it. The process continues as long as there's a unique maximum-degree vertex. The question is: what's the maximum number of days this can continue?

After removing a vertex, the degrees of its neighbors decrease by 1. So the process can continue if after each removal, there's still a unique maximum degree vertex.

We want to maximize the number of removals. The process stops when either:
1. No vertices remain (but we need at least... well, with 1 vertex left, degree 0, that's the unique max, so it gets removed too? Wait, with 1 vertex, degree 0, that's strictly highest (only one vertex), so it gets removed. With 0 vertices, the process can't continue.
2. There's a tie for maximum degree.

Actually wait, with 2 vertices both having degree 0, that's a tie. With 2 vertices connected by an edge, both have degree 1, that's a tie. So with 2 vertices, we always have a tie (both have the same degree). So the process can continue at most until 2 vertices remain... but actually it could stop earlier due to ties.

Hmm, but actually with 2 vertices, if they're connected, both have degree 1 (tie). If not connected, both have degree 0 (tie). So with 2 vertices, always a tie. So the process stops when we reach 2 vertices (or earlier if a tie occurs).

Wait, but the process stops when there's no strictly highest. So the maximum number of days is at most $n - 2$ (removing vertices until 2 remain, then it stops).

But can we always achieve $n - 2$? We need to construct a graph where at each step, there's a unique maximum degree vertex, and after removing it, the remaining graph still has a unique maximum degree vertex, and this continues for $n - 2$ steps.

Let me think about small cases.

$n = 3$: We want to remove 1 vertex (then 2 remain, tie). Can we have a graph on 3 vertices with a unique max degree vertex?

Vertices $a, b, c$. If we have edges $ab, ac$ (a star centered at $a$), then degrees are $a: 2, b: 1, c: 1$. Unique max is $a$ with degree 2. Remove $a$. Remaining: $b, c$ with no edge, both degree 0, tie. So 1 day. $n - 2 = 1$. ✓

$n = 4$: We want 2 days. Start with 4 vertices, remove one (unique max), then 3 vertices with unique max, remove one, then 2 vertices (tie).

Let's try. Vertices $a, b, c, d$. We need $a$ to be unique max. Say degrees $a: 3, b: 1, c: 1, d: 1$ (star). Remove $a$. Remaining $b, c, d$ with no edges, all degree 0, tie. Only 1 day. Not enough.

Try: $a: 3, b: 2, c: 2, d: 1$. Edges: $a$ connects to all three. $b$ and $c$ need degree 2, so $b$ connects to $a$ and one more, $c$ connects to $a$ and one more. $d$ has degree 1 (connects to $a$). So edges: $ab, ac, ad, bc$. Degrees: $a: 3, b: 2, c: 2, d: 1$. Unique max is $a$. Remove $a$. Remaining: $b, c, d$ with edge $bc$. Degrees: $b: 1, c: 1, d: 0$. Tie between $b$ and $c$. Only 1 day.

Hmm. Let me try another approach. We need after removing $a$, the remaining graph on $b, c, d$ has a unique max.

Try: edges $ab, ac, ad, bc, bd$. Degrees: $a: 3, b: 2, c: 1, d: 1$. Unique max $a$. Remove $a$. Remaining: $b, c, d$ with edges $bc, bd$. Degrees: $b: 2, c: 1, d: 1$. Unique max $b$. Remove $b$. Remaining: $c, d$, no edge, tie. 2 days! $n - 2 = 2$. ✓

So for $n = 4$, we can achieve 2 = $n - 2$.

$n = 5$: Can we achieve 3?

Let me think about this more generally. The answer might be $n - 2$.

Let me try to construct a graph that achieves $n - 2$ for general $n$.

Consider a "path-like" elimination. We want vertices $v_1, v_2, \ldots, v_n$ such that:
- In the original graph, $v_1$ has strictly highest degree.
- After removing $v_1$, $v_2$ has strictly highest degree.
- After removing $v_1, v_2$, $v_3$ has strictly highest degree.
- ... and so on for $n - 2$ steps.

Let me think of a construction. Consider the graph where we have a "dominating path."

Actually, let me think about it differently. Let's label vertices $1, 2, \ldots, n$. Consider the graph where vertex $i$ is connected to all vertices $j > i$ (a transitive tournament, but as an undirected graph, this is just a complete graph... no).

Let me think about the "threshold graph" or "nested" structure.

Consider the following construction: vertices $1, 2, \ldots, n$. Connect $i$ to $j$ if $i + j \leq n + 1$ or something... Let me think more carefully.

Actually, let me think about what happens at each step. When we remove vertex $v_1$ (the unique max degree vertex), the degrees of all neighbors of $v_1$ decrease by 1. For $v_2$ to become the unique max, $v_2$'s degree (after decrement) must be strictly greater than all others.

Let me try a specific construction. Consider the graph on $n$ vertices $\{1, 2, \ldots, n\}$ where we connect $i$ and $j$ ($i < j$) if $i \leq n - j + 1$... this is getting complicated.

Let me try a different approach. Consider the "half graph" or a specific threshold graph.

Let me try: vertex $i$ is connected to vertex $j$ (where $i < j$) if and only if $i + j \leq n + 1$.

For $n = 5$: 
- $1+2=3 \leq 6$ ✓, $1+3=4 \leq 6$ ✓, $1+4=5 \leq 6$ ✓, $1+5=6 \leq 6$ ✓
- $2+3=5 \leq 6$ ✓, $2+4=6 \leq 6$ ✓, $2+5=7 > 6$ ✗
- $3+4=7 > 6$ ✗, $3+5=8 > 6$ ✗
- $4+5=9 > 6$ ✗

Edges: $12, 13, 14, 15, 23, 24$. Degrees: $1: 4, 2: 3, 3: 2, 4: 2, 5: 1$. Unique max is vertex 1 (degree 4). Remove 1. Remaining: $2, 3, 4, 5$ with edges $23, 24$. Degrees: $2: 2, 3: 1, 4: 1, 5: 0$. Unique max is vertex 2 (degree 2). Remove 2. Remaining: $3, 4, 5$ with no edges. Degrees: all 0, tie. Only 2 days, not 3.

Hmm, that doesn't work for $n = 5$.

Let me try a different construction. Maybe a "caterpillar" or something.

Let me think about this more carefully. For $n = 5$, I want 3 days.

Vertices $a, b, c, d, e$. I want to remove $a$, then $b$, then $c$, leaving $d, e$ (tie).

After removing $a, b, c$, the remaining graph on $d, e$ should have a tie (any 2-vertex graph has a tie). So that's automatic.

I need:
1. In the full graph, $a$ has strictly highest degree.
2. After removing $a$, $b$ has strictly highest degree among $\{b, c, d, e\}$.
3. After removing $a, b$, $c$ has strictly highest degree among $\{c, d, e\}$.

Let $G$ be the graph. Let $d_G(v)$ be degree in $G$.

Step 1: $d_G(a) > d_G(v)$ for all $v \neq a$.

After removing $a$, the degree of $v$ in $G - a$ is $d_G(v) - [v \sim a]$.

Step 2: $d_{G-a}(b) > d_{G-a}(v)$ for all $v \in \{c, d, e\}$.

After removing $a, b$, degree of $v$ in $G - a - b$ is $d_{G-a}(v) - [v \sim b] = d_G(v) - [v \sim a] - [v \sim b]$.

Step 3: $d_{G-a-b}(c) > d_{G-a-b}(v)$ for all $v \in \{d, e\}$.

Let me try to construct this. Let me make $a$ connected to everyone: $d_G(a) = 4$. Then $a$ is the unique max if all others have degree $< 4$.

After removing $a$, all degrees decrease by 1 (since $a$ is connected to all). So $d_{G-a}(v) = d_G(v) - 1$ for all $v$.

For step 2, I need $d_{G-a}(b) > d_{G-a}(c), d_{G-a}(d), d_{G-a}(e)$.

Let me make $b$ connected to $c, d, e$ as well (in addition to $a$). So $d_G(b) = 4$... but then $d_G(a) = d_G(b) = 4$, not strictly highest. Bad.

OK so $b$ can't be connected to all of $a, c, d, e$ if $a$ is also connected to all.

Let me try: $a$ connected to $b, c, d, e$ (degree 4). $b$ connected to $a, c, d$ (degree 3). $c$ connected to $a, b$ (degree 2). $d$ connected to $a$ (degree 1). $e$ connected to $a$ (degree 1).

Degrees: $a: 4, b: 3, c: 2, d: 1, e: 1$. Unique max $a$. ✓

Remove $a$. Remaining: $b, c, d, e$ with edges $bc, bd$. Degrees: $b: 2, c: 1, d: 1, e: 0$. Unique max $b$. ✓

Remove $b$. Remaining: $c, d, e$ with no edges. Degrees: all 0, tie. Only 2 days.

I need $c$ to have a strictly higher degree after removing $a$ and $b$. So $c$ needs to be connected to $d$ or $e$.

Let me try: $a$ connected to $b, c, d, e$. $b$ connected to $a, c, d$. $c$ connected to $a, b, d$. $d$ connected to $a, b, c$. $e$ connected to $a$.

Degrees: $a: 4, b: 3, c: 3, d: 3, e: 1$. Unique max $a$. ✓

Remove $a$. Remaining: $b, c, d, e$ with edges $bc, bd, cd$ (triangle on $b, c, d$). Degrees: $b: 2, c: 2, d: 2, e: 0$. Tie among $b, c, d$. Bad.

Let me try: $a$ connected to $b, c, d, e$. $b$ connected to $a, c, d, e$. $c$ connected to $a, b, d$. $d$ connected to $a, b$. $e$ connected to $a, b$.

Degrees: $a: 4, b: 4, ...$. Tie. Bad.

Hmm, this is tricky. Let me think differently.

Let me try: $a$ connected to $b, c, d, e$ (degree 4). $b$ connected to $a, c, d$ (degree 3). $c$ connected to $a, b, d$ (degree 3). Tie between $b$ and $c$. Bad.

OK let me try not making $a$ universal.

$a$ connected to $b, c, d$ (degree 3). $b$ connected to $a, c, d, e$ (degree 4). But then $b$ has higher degree than $a$. Bad.

Let me try: $a$ connected to $b, c, d, e$ (degree 4). $b$ connected to $a, c, d$ (degree 3). $c$ connected to $a, b, e$ (degree 3). Tie $b, c$. Bad.

$a$ connected to $b, c, d, e$ (degree 4). $b$ connected to $a, c, d$ (degree 3). $c$ connected to $a, b$ (degree 2). $d$ connected to $a, b, e$ (degree 3). Tie $b, d$. Bad.

$a$ connected to $b, c, d, e$ (degree 4). $b$ connected to $a, c, d$ (degree 3). $c$ connected to $a, b$ (degree 2). $d$ connected to $a, b$ (degree 2). $e$ connected to $a$ (degree 1).

Degrees: $a: 4, b: 3, c: 2, d: 2, e: 1$. Unique max $a$. ✓

Remove $a$. Remaining: $b, c, d, e$ with edges $bc, bd$. Degrees: $b: 2, c: 1, d: 1, e: 0$. Unique max $b$. ✓

Remove $b$. Remaining: $c, d, e$ with no edges. Tie. 2 days.

The problem is that after removing $a$ and $b$, $c$ has no edges left. I need $c$ to be connected to $d$ or $e$ (not through $a$ or $b$).

Let me try: $a$ connected to $b, c, d, e$. $b$ connected to $a, c, d$. $c$ connected to $a, b, d$. $d$ connected to $a, e$. $e$ connected to $a, d$.

Degrees: $a: 4, b: 3, c: 3, d: 3, e: 2$. Tie $b, c, d$. Bad.

Let me try: $a$ connected to $b, c, d, e$. $b$ connected to $a, c, d, e$. $c$ connected to $a, b, d$. $d$ connected to $a, b$. $e$ connected to $a, b$.

Degrees: $a: 4, b: 4$. Tie. Bad.

Hmm. Let me try a completely different approach.

What if $a$ is not connected to everyone?

$a$ connected to $b, c$ (degree 2). $b$ connected to $a, c, d, e$ (degree 4). $c$ connected to $a, b, d$ (degree 3). $d$ connected to $b, c, e$ (degree 3). $e$ connected to $b, d$ (degree 2).

Degrees: $a: 2, b: 4, c: 3, d: 3, e: 2$. Unique max $b$. But I wanted $a$ to be removed first. Let me relabel.

Remove order: $b, d, c$ (or whatever). Let me just find any valid sequence.

Degrees: $b: 4$ is unique max. Remove $b$. Remaining: $a, c, d, e$ with edges $ac, cd, de$. Degrees: $a: 1, c: 2, d: 2, e: 1$. Tie $c, d$. Only 1 day.

Let me try yet another approach. Let me think about what structure allows long elimination sequences.

Consider a graph where vertex $v_i$ has degree $n - i$ in the original graph, and after removing $v_1, \ldots, v_{i-1}$, vertex $v_i$ has the strictly highest degree.

For this to work, I need the degree sequence to be strictly decreasing: $d(v_1) > d(v_2) > \ldots > d(v_n)$, and after removing $v_1, \ldots, v_{i-1}$, $v_i$ still has strictly highest degree.

But when we remove vertices, the degrees of remaining vertices can only decrease. So if originally $d(v_1) > d(v_2) > \ldots$, after removing $v_1$, $v_2$'s degree might decrease (if $v_2$ was connected to $v_1$), and so might others.

Let me think about a specific construction. Consider the graph on vertices $\{1, 2, \ldots, n\}$ where $i \sim j$ iff $i + j \leq n + 1$.

Wait, I tried this for $n = 5$ and it didn't work well. Let me try a different construction.

What about the graph where $i \sim j$ (for $i < j$) iff $j \leq n - i + 1$? This is the same thing.

Let me try the "anti-threshold" graph: $i \sim j$ iff $i + j > n$.

For $n = 5$: $i + j > 5$.
- $1+5=6 > 5$ ✓, $1+4=5$, not $> 5$ ✗, $1+3=4$ ✗, $1+2=3$ ✗
- $2+4=6 > 5$ ✓, $2+5=7$ ✓, $2+3=5$ ✗
- $3+3$ N/A, $3+4=7$ ✓, $3+5=8$ ✓
- $4+5=9$ ✓

Edges: $15, 24, 25, 34, 35, 45$. Degrees: $1: 1, 2: 2, 3: 2, 4: 3, 5: 4$. Unique max $5$ (degree 4). ✓

Remove $5$. Remaining: $1, 2, 3, 4$ with edges $24, 34$. Degrees: $1: 0, 2: 1, 3: 1, 4: 2$. Unique max $4$ (degree 2). ✓

Remove $4$. Remaining: $1, 2, 3$ with no edges. Degrees: all 0, tie. 2 days. Not 3.

Hmm. Let me try to think about this more carefully for $n = 5$.

I want 3 removals. Let me denote the removal order as $v_1, v_2, v_3$, leaving $v_4, v_5$.

After removing $v_1, v_2, v_3$, the remaining graph on $\{v_4, v_5\}$ has a tie (always true for 2 vertices). So I just need:

1. $v_1$ is unique max degree in $G$.
2. $v_2$ is unique max degree in $G - v_1$.
3. $v_3$ is unique max degree in $G - v_1 - v_2$.

Let me try to build this step by step, working backwards.

After removing $v_1, v_2$: graph on $\{v_3, v_4, v_5\}$. $v_3$ must be unique max. The simplest: $v_3$ connected to $v_4$ (and not $v_5$), $v_4$ not connected to $v_5$. Degrees: $v_3: 1, v_4: 1, v_5: 0$. Tie $v_3, v_4$. Bad.

$v_3$ connected to $v_4$ and $v_5$, $v_4$ not connected to $v_5$. Degrees: $v_3: 2, v_4: 1, v_5: 1$. Unique max $v_3$. ✓

So in $G - v_1 - v_2$, we need edges $v_3 v_4, v_3 v_5$.

Now, in $G - v_1$, the graph on $\{v_2, v_3, v_4, v_5\}$ must have $v_2$ as unique max. The edges in $G - v_1$ include $v_3 v_4, v_3 v_5$ (from above) plus any edges involving $v_2$ and any edges between $v_2$ and others, minus edges to $v_1$.

Wait, I should think of it as: $G$ has some edges. $G - v_1$ is $G$ with $v_1$ removed. $G - v_1 - v_2$ is $G$ with $v_1, v_2$ removed. The edges $v_3 v_4, v_3 v_5$ must be in $G$.

In $G - v_1$, I need $v_2$ to be unique max. Let's say $v_2$ is connected to $v_3, v_4, v_5$ in $G$ (so degree 3 in $G - v_1$, assuming $v_2$ is also connected to $v_1$ in $G$, giving degree 4 in $G$). Then in $G - v_1$, $v_2$ has degree 3, $v_3$ has degree 2 (from $v_3 v_4, v_3 v_5$, plus $v_3 v_2$), $v_4$ has degree 2 (from $v_3 v_4, v_2 v_4$), $v_5$ has degree 2 (from $v_3 v_5, v_2 v_5$). So $v_2: 3, v_3: 2, v_4: 2, v_5: 2$. Unique max $v_2$. ✓

Now in $G$, I need $v_1$ to be unique max. $v_1$'s degree must be strictly greater than all others. Let's see the degrees in $G$:
- $v_1$: connected to $v_2$ (at least). Let's say $v_1$ is connected to $v_2, v_3, v_4, v_5$ (degree 4).
- $v_2$: connected to $v_1, v_3, v_4, v_5$ (degree 4). Tie with $v_1$. Bad.

So $v_1$ can't be connected to all if $v_2$ is also connected to all.

Let me have $v_1$ connected to $v_2, v_3, v_4, v_5$ (degree 4), and $v_2$ connected to $v_1, v_3, v_4$ (degree 3, not connected to $v_5$).

In $G - v_1$: $v_2$ has degree 2 (connected to $v_3, v_4$), $v_3$ has degree 2 (connected to $v_4, v_5$ from before, plus $v_2$), $v_4$ has degree 2 (connected to $v_3, v_2$), $v_5$ has degree 1 (connected to $v_3$). So $v_2: 2, v_3: 2, v_4: 2, v_5: 1$. Tie. Bad.

Let me try $v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4) and $v_1$ connected to $v_2, v_3, v_4, v_5$ (degree 4). Tie. Bad.

Hmm. The issue is that if $v_1$ is connected to many vertices and $v_2$ is also connected to many, they might tie.

Let me try: $v_1$ connected to $v_2, v_3, v_4, v_5$ (degree 4). $v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). Tie. Need to break this.

What if $v_1$ is connected to $v_2, v_3, v_4, v_5$ and also... wait, max degree is 4 for $n = 5$.

OK so both can have degree at most 4. If both have degree 4, they're both connected to all others, so they tie. We need $v_1$ to have strictly higher degree. So $v_1$ has degree 4 and $v_2$ has degree $\leq 3$.

If $v_1$ has degree 4 (connected to all), and $v_2$ has degree 3, then in $G - v_1$, $v_2$ has degree 2 (lost the edge to $v_1$). For $v_2$ to be unique max in $G - v_1$, all others must have degree $\leq 1$ in $G - v_1$.

In $G - v_1$, the remaining vertices $v_3, v_4, v_5$ have their degrees from $G$ minus 1 (since $v_1$ was connected to all of them). So their degrees in $G - v_1$ are $d_G(v_i) - 1$ for $i = 3, 4, 5$.

For $v_2$ to be unique max in $G - v_1$ with degree 2, we need $d_G(v_i) - 1 \leq 1$, i.e., $d_G(v_i) \leq 2$ for $i = 3, 4, 5$, and at least one must be $< 2$ (actually, all must be $\leq 1$ in $G - v_1$, so $d_G(v_i) \leq 2$). But we also need $v_2$'s degree in $G - v_1$ to be 2, which means $v_2$ is connected to 2 of $\{v_3, v_4, v_5\}$.

And we need $d_G(v_2) = 3$ (connected to $v_1$ and 2 others). And $d_G(v_i) \leq 2$ for $i = 3, 4, 5$.

Now, in $G - v_1 - v_2$, we need $v_3$ to be unique max. The edges among $v_3, v_4, v_5$ in $G$ are whatever they are. We need $v_3$ to have strictly highest degree among $\{v_3, v_4, v_5\}$ using only edges among them.

Let's say $v_2$ is connected to $v_3$ and $v_4$ (not $v_5$). Then $d_G(v_2) = 3$ (edges to $v_1, v_3, v_4$). In $G - v_1$: $v_2$ has degree 2 (edges to $v_3, v_4$).

For $v_3, v_4, v_5$ in $G - v_1$: $d_{G-v_1}(v_3) = d_G(v_3) - 1$, $d_{G-v_1}(v_4) = d_G(v_4) - 1$, $d_{G-v_1}(v_5) = d_G(v_5) - 1$.

We need these to be $\leq 1$ (so $v_2$ with degree 2 is unique max). So $d_G(v_3) \leq 2, d_G(v_4) \leq 2, d_G(v_5) \leq 2$.

$d_G(v_3)$: connected to $v_1$ (degree contribution 1) plus edges to $v_2, v_4, v_5$. Since $v_3 \sim v_2$, that's at least 2. So $d_G(v_3) \geq 2$. For $d_G(v_3) \leq 2$, $v_3$ is connected only to $v_1$ and $v_2$ (not $v_4$ or $v_5$). But then in $G - v_1 - v_2$, $v_3$ has degree 0. We need $v_3$ to be unique max in $G - v_1 - v_2$. If $v_3$ has degree 0, all must have degree $< 0$, impossible. So $v_3$ needs degree $\geq 1$ in $G - v_1 - v_2$, meaning $v_3$ is connected to $v_4$ or $v_5$.

But if $v_3 \sim v_4$, then $d_G(v_3) \geq 3$ (edges to $v_1, v_2, v_4$), violating $d_G(v_3) \leq 2$.

Contradiction! So with $v_1$ having degree 4 (universal), we can't get 3 days for $n = 5$.

What if $v_1$ doesn't have degree 4? Let's say $v_1$ has degree 3.

$v_1$ connected to $v_2, v_3, v_4$ (not $v_5$). $d_G(v_1) = 3$. For $v_1$ to be unique max, all others have degree $\leq 2$.

$v_2$ has degree $\leq 2$. In $G - v_1$, $v_2$'s degree is $d_G(v_2) - 1$ (since $v_2 \sim v_1$) $= \leq 1$. For $v_2$ to be unique max in $G - v_1$, all others in $G - v_1$ must have degree $< v_2$'s degree, so $\leq 0$ if $v_2$ has degree 1, or... if $v_2$ has degree 1 in $G - v_1$, others must have degree 0.

In $G - v_1$: $v_3, v_4$ lose 1 (connected to $v_1$), $v_5$ keeps its degree (not connected to $v_1$).

$v_3$ in $G - v_1$: $d_G(v_3) - 1 \leq 2 - 1 = 1$. $v_4$ in $G - v_1$: $d_G(v_4) - 1 \leq 1$. $v_5$ in $G - v_1$: $d_G(v_5) \leq 2$.

For $v_2$ to be unique max with degree 1, we need $v_3, v_4, v_5$ to all have degree 0 in $G - v_1$. So $d_G(v_3) = 1$ (only connected to $v_1$), $d_G(v_4) = 1$ (only connected to $v_1$), $d_G(v_5) = 0$ (isolated). But then in $G - v_1 - v_2$, all of $v_3, v_4, v_5$ have degree 0, tie. Bad.

If $v_2$ has degree 2 in $G - v_1$ (so $d_G(v_2) = 3$... but we said $d_G(v_2) \leq 2$). Contradiction since $v_1$ is unique max with degree 3 and $v_2$ has degree $\leq 2$.

Hmm wait, $v_2$ has degree $\leq 2$ in $G$ (since $v_1$ is unique max with degree 3). $v_2$ is connected to $v_1$, so in $G - v_1$, $v_2$ has degree $\leq 1$. So $v_2$ can have at most degree 1 in $G - v_1$, meaning $v_2$ is connected to at most 1 of $\{v_3, v_4, v_5\}$.

If $v_2$ has degree 1 in $G - v_1$ (connected to one of $v_3, v_4, v_5$), then for $v_2$ to be unique max, all others have degree 0 in $G - v_1$. As shown, this leads to all-degree-0 in the next step.

If $v_2$ has degree 0 in $G - v_1$, then it's tied with anyone else who has degree 0. Bad.

So with $v_1$ having degree 3 and $n = 5$, we also can't get 3 days.

What about $v_1$ having degree 4 but not being universal? No, degree 4 in a 5-vertex graph means universal.

So for $n = 5$, the maximum might be 2, not 3 = $n - 2$.

Wait, let me reconsider. Maybe I'm missing something. Let me try $v_1$ having degree 3 but not connected to $v_2$.

$v_1$ connected to $v_3, v_4, v_5$ (not $v_2$). $d_G(v_1) = 3$. For $v_1$ to be unique max, $d_G(v_2) \leq 2, d_G(v_3) \leq 2, d_G(v_4) \leq 2, d_G(v_5) \leq 2$.

In $G - v_1$: $v_2$'s degree is $d_G(v_2)$ (unchanged, since $v_2 \not\sim v_1$). $v_3, v_4, v_5$ lose 1 each.

If $d_G(v_2) = 2$, then in $G - v_1$, $v_2$ has degree 2. $v_3$ has degree $d_G(v_3) - 1 \leq 1$, $v_4$ has degree $\leq 1$, $v_5$ has degree $\leq 1$. So $v_2$ is unique max with degree 2. ✓

Now $v_2$ has degree 2 in $G$, connected to 2 of $\{v_3, v_4, v_5\}$ (not $v_1$). Say $v_2 \sim v_3, v_2 \sim v_4$.

In $G - v_1 - v_2$: remaining $v_3, v_4, v_5$. Edges among them: whatever's in $G$ minus edges to $v_1, v_2$.

$v_3$ in $G$: connected to $v_1, v_2$ (at least), so $d_G(v_3) \geq 2$. Since $d_G(v_3) \leq 2$, $v_3$ is connected only to $v_1$ and $v_2$. In $G - v_1 - v_2$: $v_3$ has degree 0.

Similarly $v_4$: connected to $v_1, v_2$, degree 2, in $G - v_1 - v_2$: degree 0.

$v_5$: connected to $v_1$ (at least), $d_G(v_5) \leq 2$. Could be connected to $v_1$ and one more. If $v_5 \sim v_1$ and $v_5 \sim v_3$ (or $v_4$ or $v_2$). If $v_5 \sim v_3$: $d_G(v_5) = 2$, $d_G(v_3) = 3$ (connected to $v_1, v_2, v_5$). But $d_G(v_3) \leq 2$. Contradiction.

If $v_5 \sim v_4$: same issue, $d_G(v_4) = 3$. Bad.

If $v_5 \sim v_2$: $d_G(v_2) = 3$ (connected to $v_3, v_4, v_5$). But $d_G(v_2) = 2$. Bad.

If $v_5$ is only connected to $v_1$: $d_G(v_5) = 1$. In $G - v_1 - v_2$: $v_5$ has degree 0.

So in $G - v_1 - v_2$: all of $v_3, v_4, v_5$ have degree 0. Tie. 2 days.

Hmm. So for $n = 5$, it seems like we can only get 2 days.

Wait, but maybe I need to consider that $v_1$ doesn't have to be removed first with the highest possible degree. Let me think about this differently.

Actually, let me reconsider. Maybe the answer isn't $n - 2$. Let me think about what the answer could be.

For $n = 3$: max 1 day. ($n - 2 = 1$)
For $n = 4$: max 2 days. ($n - 2 = 2$)
For $n = 5$: max 2 days? Let me verify more carefully.

Actually, let me try harder for $n = 5$. Maybe there's a graph I haven't tried.

Let me try: $v_1$ connected to $v_2, v_3, v_4, v_5$ (degree 4). $v_2$ connected to $v_1, v_3$ (degree 2). $v_3$ connected to $v_1, v_2, v_4, v_5$ (degree 4). Tie $v_1, v_3$. Bad.

$v_1$ connected to $v_2, v_3, v_4, v_5$ (degree 4). $v_2$ connected to $v_1, v_3$ (degree 2). $v_3$ connected to $v_1, v_2, v_4$ (degree 3). $v_4$ connected to $v_1, v_3, v_5$ (degree 3). Tie $v_3, v_4$. Bad.

$v_1$ connected to $v_2, v_3, v_4, v_5$ (degree 4). $v_2$ connected to $v_1, v_3$ (degree 2). $v_3$ connected to $v_1, v_2, v_4$ (degree 3). $v_4$ connected to $v_1, v_3$ (degree 2). $v_5$ connected to $v_1$ (degree 1).

Degrees: $v_1: 4, v_3: 3, v_2: 2, v_4: 2, v_5: 1$. Unique max $v_1$. ✓

Remove $v_1$. Remaining: $v_2, v_3, v_4, v_5$ with edges $v_2 v_3, v_3 v_4$. Degrees: $v_3: 2, v_2: 1, v_4: 1, v_5: 0$. Unique max $v_3$. ✓

Remove $v_3$. Remaining: $v_2, v_4, v_5$ with no edges. Tie. 2 days.

I keep getting 2 for $n = 5$. Let me try to see if 3 is possible by being more creative.

What if the graph is not "star-like"? Let me try a path: $v_1 v_2 v_3 v_4 v_5$.

Degrees: $v_1: 1, v_2: 2, v_3: 2, v_4: 2, v_5: 1$. Tie $v_2, v_3, v_4$. 0 days.

Cycle $C_5$: all degree 2, tie. 0 days.

Complete graph $K_5$: all degree 4, tie. 0 days.

$K_5$ minus one edge, say $v_4 v_5$: degrees $v_1: 4, v_2: 4, v_3: 4, v_4: 3, v_5: 3$. Tie $v_1, v_2, v_3$. 0 days.

$K_5$ minus two edges sharing a vertex, say $v_4 v_5$ and $v_4 v_3$: degrees $v_1: 4, v_2: 4, v_3: 3, v_4: 2, v_5: 3$. Tie $v_1, v_2$. 0 days.

$K_5$ minus edges $v_1 v_2, v_1 v_3$: degrees $v_1: 2, v_2: 3, v_3: 3, v_4: 4, v_5: 4$. Tie $v_4, v_5$. 0 days.

$K_5$ minus edges $v_1 v_2, v_3 v_4$: degrees $v_1: 3, v_2: 3, v_3: 3, v_4: 3, v_5: 4$. Unique max $v_5$. ✓

Remove $v_5$. Remaining: $K_4$ minus edges $v_1 v_2, v_3 v_4$. Degrees: $v_1: 2, v_2: 2, v_3: 2, v_4: 2$. Tie. 1 day.

$K_5$ minus edges $v_1 v_2, v_1 v_3, v_3 v_4$: degrees $v_1: 2, v_2: 3, v_3: 2, v_4: 3, v_5: 4$. Unique max $v_5$. ✓

Remove $v_5$. Remaining: $K_4$ minus $v_1 v_2, v_1 v_3, v_3 v_4$. Degrees: $v_1: 1, v_2: 2, v_3: 1, v_4: 2$. Tie $v_2, v_4$. 1 day.

$K_5$ minus edges $v_1 v_2, v_1 v_3, v_2 v_3$: This makes $\{v_1, v_2, v_3\}$ an independent set. Degrees: $v_1: 2, v_2: 2, v_3: 2, v_4: 4, v_5: 4$. Tie $v_4, v_5$. 0 days.

$K_5$ minus edges $v_1 v_2, v_1 v_3, v_2 v_3, v_4 v_5$: Degrees: $v_1: 2, v_2: 2, v_3: 2, v_4: 3, v_5: 3$. Tie $v_4, v_5$. 0 days.

Hmm, let me try a completely different approach. Let me think about what happens with a "dominating vertex" chain.

Actually, let me try to think about this problem more carefully.

Let me consider the process. At each step, we remove the unique vertex of maximum degree. The process continues as long as there's a unique maximum.

Key insight: when we remove a vertex $v$ of degree $d$, the degrees of $v$'s neighbors decrease by 1. The degrees of non-neighbors stay the same.

Let me think about an upper bound. Consider the sum of all degrees $S = 2|E|$. When we remove a vertex of degree $d$, the sum decreases by $2d$ (we remove $d$ edges, each contributing 2 to the sum... wait, no. We remove $d$ edges, and the sum of degrees decreases by $2d$ since each edge contributes 2 to the sum, and we remove $d$ edges).

Actually, the sum of degrees decreases by $2d$ where $d$ is the degree of the removed vertex. The remaining sum is $S' = S - 2d$.

Hmm, this might not directly give me a bound. Let me think differently.

Let me think about the problem in terms of the degree sequence. At each step, we have a graph with some degree sequence, and we remove the unique maximum.

Let me think about what constraints this places.

Actually, let me try to think about this problem computationally for small $n$ to find the pattern.

For $n = 3$: max 1 day (as shown).
For $n = 4$: max 2 days (as shown).
For $n = 5$: I've been trying and getting 2 days. Let me try even harder.

Let me enumerate more carefully. I want a graph on 5 vertices where I can remove 3 vertices one by one, each being the unique max.

Let me think about it from the perspective of the degree sequence evolution.

Initial: 5 vertices with degrees $d_1 > d_2 \geq d_3 \geq d_4 \geq d_5$ (after sorting, $d_1$ is unique max).

Remove vertex with degree $d_1$. Its neighbors' degrees decrease by 1. Now 4 vertices, need unique max.

Remove that vertex. Now 3 vertices, need unique max.

Remove that vertex. Now 2 vertices, tie (process stops).

So we need 3 successful removals.

Let me think about the degree sequence more carefully. Let the removal order be $v_1, v_2, v_3$.

Let $N(v_i)$ denote the neighborhood of $v_i$ in the original graph $G$.

When we remove $v_1$, the degree of each remaining vertex $u$ becomes $d_G(u) - [u \in N(v_1)]$.

When we then remove $v_2$, the degree of each remaining vertex $u$ (among $\{v_3, v_4, v_5\}$) becomes $d_G(u) - [u \in N(v_1)] - [u \in N(v_2)]$.

For step 1: $d_G(v_1) > d_G(u)$ for all $u \neq v_1$.
For step 2: $d_G(v_2) - [v_2 \in N(v_1)] > d_G(u) - [u \in N(v_1)]$ for all $u \in \{v_3, v_4, v_5\}$.
For step 3: $d_G(v_3) - [v_3 \in N(v_1)] - [v_3 \in N(v_2)] > d_G(u) - [u \in N(v_1)] - [u \in N(v_2)]$ for all $u \in \{v_4, v_5\}$.

Let me denote $a_i = [v_i \in N(v_1)]$ and $b_i = [v_i \in N(v_2)]$ for $i \geq 2$. Also $a_1 = 0$ (not meaningful), and $v_1 \in N(v_2)$ iff $v_2 \in N(v_1)$, so $b_1$... let me be more careful.

Let me use a different notation. Let $x_{ij} = [v_i \sim v_j]$ (1 if edge, 0 if not).

Step 1: $d_G(v_1) = \sum_{j \neq 1} x_{1j} > d_G(v_k) = \sum_{j \neq k} x_{kj}$ for $k = 2, 3, 4, 5$.

Step 2 (in $G - v_1$): $d_{G-v_1}(v_2) = d_G(v_2) - x_{12} > d_{G-v_1}(v_k) = d_G(v_k) - x_{1k}$ for $k = 3, 4, 5$.

Step 3 (in $G - v_1 - v_2$): $d_{G-v_1-v_2}(v_3) = d_G(v_3) - x_{13} - x_{23} > d_{G-v_1-v_2}(v_k) = d_G(v_k) - x_{1k} - x_{2k}$ for $k = 4, 5$.

Let me try to find a solution by considering specific adjacency patterns.

Let me try: $v_1$ connected to $v_2, v_3, v_4$ (not $v_5$). So $x_{12} = x_{13} = x_{14} = 1, x_{15} = 0$.

$d_G(v_1) = 3$. Need $d_G(v_k) \leq 2$ for all $k$.

Step 2: $d_G(v_2) - 1 > d_G(v_k) - x_{1k}$ for $k = 3, 4, 5$.

For $k = 3$: $d_G(v_2) - 1 > d_G(v_3) - 1$, i.e., $d_G(v_2) > d_G(v_3)$.
For $k = 4$: $d_G(v_2) - 1 > d_G(v_4) - 1$, i.e., $d_G(v_2) > d_G(v_4)$.
For $k = 5$: $d_G(v_2) - 1 > d_G(v_5) - 0$, i.e., $d_G(v_2) > d_G(v_5) + 1$.

So $d_G(v_2) > d_G(v_3), d_G(v_4)$, and $d_G(v_2) \geq d_G(v_5) + 2$.

Since $d_G(v_2) \leq 2$ (from step 1), we need $d_G(v_5) \leq 0$, so $v_5$ is isolated. And $d_G(v_2) = 2$, $d_G(v_3) \leq 1, d_G(v_4) \leq 1$.

But $v_2$ is connected to $v_1$ (degree contribution 1) and one more vertex. $d_G(v_2) = 2$, so $v_2$ is connected to $v_1$ and one of $\{v_3, v_4, v_5\}$. Since $v_5$ is isolated, $v_2$ is connected to $v_3$ or $v_4$.

Say $v_2 \sim v_3$. Then $d_G(v_3) \geq 2$ (connected to $v_1$ and $v_2$). But $d_G(v_3) \leq 1$. Contradiction.

Say $v_2 \sim v_4$. Then $d_G(v_4) \geq 2$ (connected to $v_1$ and $v_2$). But $d_G(v_4) \leq 1$. Contradiction.

So this doesn't work. Let me try $v_1$ connected to $v_2, v_3, v_5$ (not $v_4$).

$d_G(v_1) = 3$. Need $d_G(v_k) \leq 2$.

Step 2: $d_G(v_2) - 1 > d_G(v_3) - 1$, $d_G(v_2) - 1 > d_G(v_4) - 0$, $d_G(v_2) - 1 > d_G(v_5) - 1$.

So $d_G(v_2) > d_G(v_3), d_G(v_2) > d_G(v_4) + 1, d_G(v_2) > d_G(v_5)$.

$d_G(v_2) \leq 2$, so $d_G(v_4) \leq 0$, $v_4$ isolated. $d_G(v_2) = 2$, $d_G(v_3) \leq 1, d_G(v_5) \leq 1$.

$v_2$ connected to $v_1$ and one of $\{v_3, v_5\}$ (not $v_4$ since $v_4$ is isolated).

Say $v_2 \sim v_3$: $d_G(v_3) \geq 2$ (from $v_1, v_2$). But $\leq 1$. Bad.
Say $v_2 \sim v_5$: $d_G(v_5) \geq 2$ (from $v_1, v_2$). But $\leq 1$. Bad.

Same issue. The problem is that $v_2$ needs degree 2 but is connected to $v_1$, so it needs one more neighbor, but that neighbor is also connected to $v_1$, giving it degree $\geq 2$.

What if $v_1$ is connected to $v_2, v_4, v_5$ (not $v_3$)?

Step 2: $d_G(v_2) - 1 > d_G(v_3) - 0$, $d_G(v_2) - 1 > d_G(v_4) - 1$, $d_G(v_2) - 1 > d_G(v_5) - 1$.

So $d_G(v_2) > d_G(v_3) + 1, d_G(v_2) > d_G(v_4), d_G(v_2) > d_G(v_5)$.

$d_G(v_2) \leq 2$, so $d_G(v_3) \leq 0$, $v_3$ isolated. $d_G(v_2) = 2$, $d_G(v_4) \leq 1, d_G(v_5) \leq 1$.

$v_2$ connected to $v_1$ and one of $\{v_4, v_5\}$ (not $v_3$).

Say $v_2 \sim v_4$: $d_G(v_4) \geq 2$ (from $v_1, v_2$). But $\leq 1$. Bad.
Say $v_2 \sim v_5$: $d_G(v_5) \geq 2$. But $\leq 1$. Bad.

Same issue again!

What if $v_1$ is connected to only 2 vertices? $d_G(v_1) = 2$.

$v_1$ connected to $v_2, v_3$ (not $v_4, v_5$). $d_G(v_1) = 2$. Need $d_G(v_k) \leq 1$ for all $k$.

Step 2: $d_G(v_2) - 1 > d_G(v_3) - 1$, $d_G(v_2) - 1 > d_G(v_4) - 0$, $d_G(v_2) - 1 > d_G(v_5) - 0$.

$d_G(v_2) \leq 1$, so $d_G(v_2) - 1 \leq 0$. Need $d_G(v_3) - 1 < 0$, so $d_G(v_3) = 0$. But $v_3 \sim v_1$, so $d_G(v_3) \geq 1$. Contradiction.

$v_1$ connected to $v_2, v_4$: $d_G(v_1) = 2$. Need $d_G(v_k) \leq 1$.

Step 2: $d_G(v_2) - 1 > d_G(v_3) - 0, d_G(v_2) - 1 > d_G(v_4) - 1, d_G(v_2) - 1 > d_G(v_5) - 0$.

$d_G(v_2) \leq 1$, $d_G(v_2) - 1 \leq 0$. Need $d_G(v_3) < 0$. Impossible.

So $v_1$ with degree 2 doesn't work either.

What about $v_1$ with degree 4 (universal)? We already showed this doesn't work for $n = 5$.

So for $n = 5$, the maximum is 2 days.

Let me check $n = 6$. Can we get more than 2 days?

Actually, let me reconsider. Maybe the answer is $\lfloor n/2 \rfloor - 1$ or something like that. Or maybe $\lfloor (n-1)/2 \rfloor$.

$n = 3$: 1 day. $\lfloor 3/2 \rfloor = 1$. ✓
$n = 4$: 2 days. $\lfloor 4/2 \rfloor = 2$. ✓
$n = 5$: 2 days. $\lfloor 5/2 \rfloor = 2$. ✓

Let me check $n = 6$. If the answer is $\lfloor n/2 \rfloor = 3$, can we achieve 3 days?

Actually, let me think about this more carefully. Let me try to construct a graph for $n = 6$ with 3 days.

Vertices $v_1, \ldots, v_6$. Remove $v_1, v_2, v_3$, leaving $v_4, v_5, v_6$ (tie).

Let me try: $v_1$ connected to $v_2, v_3, v_4, v_5, v_6$ (degree 5, universal). $d_G(v_1) = 5$, unique max if all others have degree $\leq 4$.

$v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). $v_3$ connected to $v_1, v_2, v_4$ (degree 3). $v_4$ connected to $v_1, v_2, v_3, v_5$ (degree 4). Tie $v_2, v_4$. Bad.

Let me try: $v_1$ universal (degree 5). $v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). $v_3$ connected to $v_1, v_2$ (degree 2). $v_4$ connected to $v_1, v_2$ (degree 2). $v_5$ connected to $v_1$ (degree 1). $v_6$ connected to $v_1$ (degree 1).

Degrees: $v_1: 5, v_2: 4, v_3: 2, v_4: 2, v_5: 1, v_6: 1$. Unique max $v_1$. ✓

Remove $v_1$. Remaining: $v_2, v_3, v_4, v_5, v_6$ with edges $v_2 v_3, v_2 v_4$. Degrees: $v_2: 2, v_3: 1, v_4: 1, v_5: 0, v_6: 0$. Unique max $v_2$. ✓

Remove $v_2$. Remaining: $v_3, v_4, v_5, v_6$ with no edges. Tie. 2 days.

I need $v_3$ to have edges to $v_4, v_5$, or $v_6$ in the original graph. But if $v_3 \sim v_4$, then $d_G(v_3) \geq 3$ (from $v_1, v_2, v_4$) and $d_G(v_4) \geq 3$ (from $v_1, v_2, v_3$). But we need $d_G(v_3) \leq 4$ and $d_G(v_4) \leq 4$, which is fine. But we also need $v_2$ to be unique max after removing $v_1$, with degree 4 - 1 = 3.

Let me redo: $v_1$ universal (degree 5). $v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). $v_3$ connected to $v_1, v_2, v_4, v_6$ (degree 4). Tie $v_2, v_3$. Bad.

$v_2$ connected to $v_1, v_3, v_4, v_5, v_6$ (degree 5). Tie with $v_1$. Bad.

Hmm. Let me try $v_1$ not universal.

$v_1$ connected to $v_2, v_3, v_4, v_5$ (not $v_6$). $d_G(v_1) = 4$.

Need $d_G(v_k) \leq 3$ for all $k$.

Step 2: $d_G(v_2) - 1 > d_G(v_3) - 1, d_G(v_2) - 1 > d_G(v_4) - 1, d_G(v_2) - 1 > d_G(v_5) - 1, d_G(v_2) - 1 > d_G(v_6) - 0$.

So $d_G(v_2) > d_G(v_3), d_G(v_2) > d_G(v_4), d_G(v_2) > d_G(v_5), d_G(v_2) > d_G(v_6) + 1$.

$d_G(v_2) \leq 3$, so $d_G(v_6) \leq 1$. $d_G(v_2) = 3$, $d_G(v_3) \leq 2, d_G(v_4) \leq 2, d_G(v_5) \leq 2$.

$v_2$ connected to $v_1$ and 2 more (degree 3). The 2 more are from $\{v_3, v_4, v_5, v_6\}$.

If $v_2 \sim v_3$ and $v_2 \sim v_4$: $d_G(v_3) \geq 2$ (from $v_1, v_2$), $d_G(v_4) \geq 2$ (from $v_1, v_2$). Since $\leq 2$, $v_3$ and $v_4$ are connected only to $v_1$ and $v_2$.

Step 3: In $G - v_1 - v_2$, remaining $v_3, v_4, v_5, v_6$. $v_3$ has degree 0 (only was connected to $v_1, v_2$). $v_4$ has degree 0. $v_5$ has degree $d_G(v_5) - 1$ (connected to $v_1$, not $v_2$). $v_6$ has degree $d_G(v_6)$ (not connected to $v_1$ or $v_2$).

$d_G(v_5) \leq 2$, connected to $v_1$, so $d_G(v_5) - 1 \leq 1$. $d_G(v_6) \leq 1$.

For $v_3$ to be unique max, $v_3$ needs degree $> 0$. But $v_3$ has degree 0. Bad.

If $v_2 \sim v_3$ and $v_2 \sim v_5$: $d_G(v_3) \geq 2$ (from $v_1, v_2$), so $d_G(v_3) = 2$ (only $v_1, v_2$). $d_G(v_5) \geq 2$ (from $v_1, v_2$), so $d_G(v_5) = 2$ (only $v_1, v_2$).

Step 3: In $G - v_1 - v_2$: $v_3$ degree 0, $v_5$ degree 0. Same issue.

If $v_2 \sim v_3$ and $v_2 \sim v_6$: $d_G(v_3) \geq 2$ (from $v_1, v_2$), $d_G(v_3) = 2$. $d_G(v_6) \geq 1$ (from $v_2$), $d_G(v_6) \leq 1$, so $d_G(v_6) = 1$ (only $v_2$).

Step 3: In $G - v_1 - v_2$: $v_3$ degree 0, $v_4$ degree $d_G(v_4) - 1$ (from $v_1$, not $v_2$), $v_5$ degree $d_G(v_5) - 1$, $v_6$ degree 0.

$d_G(v_4) \leq 2$, so $v_4$ degree in $G - v_1 - v_2 \leq 1$. $d_G(v_5) \leq 2$, so $v_5$ degree $\leq 1$.

For $v_3$ to be unique max, need $v_3$ degree $> 0$. But $v_3$ has degree 0. Bad.

The issue is always the same: $v_3$ is connected to $v_1$ and $v_2$, so after removing both, $v_3$ has no edges.

What if $v_3$ is also connected to $v_4$? Then $d_G(v_3) \geq 3$ (from $v_1, v_2, v_4$). But $d_G(v_3) \leq 2$. Contradiction (when $v_1$ has degree 4 and $v_2$ has degree 3).

What if $v_1$ has degree 5 (universal)? Then $d_G(v_k) \leq 4$.

$v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). $v_3$ connected to $v_1, v_2, v_4, v_6$ (degree 4). Tie $v_2, v_3$. Bad.

$v_2$ connected to $v_1, v_3, v_4, v_5, v_6$ (degree 5). Tie with $v_1$. Bad.

$v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). $v_3$ connected to $v_1, v_2, v_4$ (degree 3). $v_4$ connected to $v_1, v_2, v_3, v_5$ (degree 4). Tie $v_2, v_4$. Bad.

$v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). $v_3$ connected to $v_1, v_2, v_6$ (degree 3). $v_4$ connected to $v_1, v_2$ (degree 2). $v_5$ connected to $v_1, v_2$ (degree 2). $v_6$ connected to $v_1, v_3$ (degree 2).

Degrees: $v_1: 5, v_2: 4, v_3: 3, v_4: 2, v_5: 2, v_6: 2$. Unique max $v_1$. ✓

Remove $v_1$. Remaining: $v_2, v_3, v_4, v_5, v_6$ with edges $v_2 v_3, v_2 v_4, v_2 v_5, v_3 v_6$. Degrees: $v_2: 3, v_3: 2, v_4: 1, v_5: 1, v_6: 1$. Unique max $v_2$. ✓

Remove $v_2$. Remaining: $v_3, v_4, v_5, v_6$ with edge $v_3 v_6$. Degrees: $v_3: 1, v_6: 1, v_4: 0, v_5: 0$. Tie $v_3, v_6$. 2 days.

Close! I need $v_3$ to be strictly higher than $v_6$ after removing $v_1, v_2$. So $v_3$ needs one more edge.

$v_3$ connected to $v_1, v_2, v_6, v_4$ (degree 4). But then $d_G(v_3) = 4 = d_G(v_2)$. Tie. Bad.

$v_3$ connected to $v_1, v_2, v_6, v_5$ (degree 4). Same, tie with $v_2$. Bad.

Hmm. What if $v_2$ has degree 3 instead of 4?

$v_1$ universal (degree 5). $v_2$ connected to $v_1, v_3, v_4$ (degree 3). $v_3$ connected to $v_1, v_2, v_4, v_5, v_6$ (degree 5). But $d_G(v_3) = 5 = d_G(v_1)$. Tie. Bad.

$v_3$ connected to $v_1, v_2, v_4, v_5$ (degree 4). $v_4$ connected to $v_1, v_2, v_3$ (degree 3). Tie $v_2, v_4$. Bad.

$v_3$ connected to $v_1, v_2, v_5, v_6$ (degree 4). $v_4$ connected to $v_1, v_2$ (degree 2). $v_5$ connected to $v_1, v_3$ (degree 2). $v_6$ connected to $v_1, v_3$ (degree 2).

Degrees: $v_1: 5, v_3: 4, v_2: 3, v_4: 2, v_5: 2, v_6: 2$. Unique max $v_1$. ✓

Remove $v_1$. Remaining: $v_2, v_3, v_4, v_5, v_6$ with edges $v_2 v_3, v_2 v_4, v_3 v_5, v_3 v_6$. Degrees: $v_3: 3, v_2: 2, v_4: 1, v_5: 1, v_6: 1$. Unique max $v_3$. ✓

But I wanted to remove $v_2$ second, not $v_3$. The unique max is $v_3$, so $v_3$ gets removed second.

Remove $v_3$. Remaining: $v_2, v_4, v_5, v_6$ with edge $v_2 v_4$. Degrees: $v_2: 1, v_4: 1, v_5: 0, v_6: 0$. Tie $v_2, v_4$. 2 days.

Hmm. Let me try to make $v_3$ have degree 4 but $v_2$ have degree 4 too, with $v_2$ being strictly higher... no, they'd tie.

OK let me try a different approach. Let me not have $v_1$ be universal.

$v_1$ connected to $v_2, v_3, v_4, v_5$ (not $v_6$). $d_G(v_1) = 4$. Need all others $\leq 3$.

$v_2$ connected to $v_1, v_3, v_6$ (degree 3). $v_3$ connected to $v_1, v_2, v_4, v_5, v_6$ (degree 5). Too high. Bad.

$v_3$ connected to $v_1, v_2, v_4, v_6$ (degree 4). Too high ($> 3$). Bad.

$v_3$ connected to $v_1, v_2, v_6$ (degree 3). $v_4$ connected to $v_1, v_3$ (degree 2). $v_5$ connected to $v_1$ (degree 1). $v_6$ connected to $v_2, v_3$ (degree 2).

Degrees: $v_1: 4, v_2: 3, v_3: 3, v_4: 2, v_5: 1, v_6: 2$. Tie $v_2, v_3$. Bad.

$v_2$ connected to $v_1, v_3, v_4, v_6$ (degree 4). Tie with $v_1$. Bad.

$v_2$ connected to $v_1, v_6$ (degree 2). $v_3$ connected to $v_1, v_2, v_4, v_6$ (degree 4). Too high. Bad.

This is getting complicated. Let me try a more systematic approach.

Let me think about what graph structures allow long elimination sequences.

Key observation: when we remove the unique max-degree vertex, its neighbors all lose 1 from their degree. For the next vertex to be the unique max, it needs to "stand out" after this adjustment.

Let me think about a "caterpillar" graph. Consider a path $v_1 - v_2 - v_3 - \ldots - v_k$ with additional pendant vertices.

Actually, let me think about this differently. Let me consider the complement graph or some other transformation.

Alternatively, let me think about the problem in terms of the degree sequence and the "Havel-Hakimi" process. The Havel-Hakimi process removes the vertex of highest degree and decreases the degrees of its neighbors. This is exactly our process (when the max is unique)!

The Havel-Hakimi theorem says a degree sequence is graphical iff after removing the max degree $d_1$ and decreasing the next $d_1$ degrees by 1, the resulting sequence is graphical. But our process is slightly different: we're removing the actual vertex and its edges, not just manipulating the degree sequence.

Actually, our process IS the Havel-Hakimi process on the actual graph. We remove the unique max-degree vertex and decrease neighbors' degrees.

Let me think about this more carefully. The question is: what's the maximum number of steps the Havel-Hakimi-like process can run (where at each step, the max degree is unique)?

Let me think about an upper bound. 

Claim: the answer is $\lfloor n/2 \rfloor - 1$.

Wait, $n = 3$: $\lfloor 3/2 \rfloor - 1 = 0$. But we showed 1 day. So that's wrong.

Let me reconsider. $n = 3$: 1, $n = 4$: 2, $n = 5$: 2 (if my analysis is correct).

Let me try $n = 6$ more carefully, maybe with a computer-like enumeration in my head.

Actually, let me try a very different construction. What about a graph where each vertex $v_i$ is connected to $v_j$ for $j > i$ and $j - i \leq k$ for some $k$? This is a "band" graph.

Or let me try the graph where $v_i \sim v_j$ iff $|i - j| = 1$ (a path) plus some extra edges.

Actually, let me try to think about this problem from a higher level.

The process removes vertices one at a time. At each step, the removed vertex has strictly highest degree. The process stops when the remaining graph has no unique max-degree vertex (i.e., the max degree is achieved by $\geq 2$ vertices).

We want to maximize the number of removals.

Upper bound consideration: After $k$ removals, $n - k$ vertices remain. The process stops when the remaining graph has a tie for max degree. With 2 vertices, there's always a tie. So the process runs for at most $n - 2$ steps. But we've seen that for $n = 5$, we can't achieve $n - 2 = 3$.

Let me think about why. When we remove a vertex $v$ of degree $d$, the sum of degrees decreases by $2d$. The remaining $n-1$ vertices have sum of degrees $S - 2d$. The average degree is $(S - 2d)/(n-1)$.

For the next step, we need a unique max. The unique max must have degree $> $ the average (well, $\geq$ average, but strictly greater than all others).

Hmm, let me think about a potential function or invariant.

Let me consider the following: at each step, the removed vertex has degree $d_i$ (in the current graph). The sum of degrees decreases by $2d_i$. 

For the process to continue, we need the remaining graph to have a unique max-degree vertex.

Let me think about what happens to the degree sequence. Initially, we have degrees $d_1 > d_2 \geq d_3 \geq \ldots \geq d_n$ (sorted, with $d_1$ being the unique max). We remove the vertex with degree $d_1$, and its $d_1$ neighbors each lose 1 from their degree. The new degree sequence (sorted) must have a unique max.

The key constraint is: after removing the max and decreasing $d_1$ of the remaining degrees by 1, the new sequence must have a unique max.

Let me think about the "worst case" for continuing the process. We want the new max to be as large as possible (so it can continue removing).

Actually, let me think about it differently. Let me consider the "potential" $\Phi = \sum_v d(v)^2$ or some other function.

Hmm, let me try a different approach. Let me think about the problem in terms of the complement.

Actually, let me just try to find the pattern by working out more cases.

For $n = 6$, let me try to get 3 days.

I'll try: $v_1$ connected to $v_2, v_3, v_4, v_5, v_6$ (universal, degree 5). $v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). $v_3$ connected to $v_1, v_2, v_4, v_6$ (degree 4). Tie $v_2, v_3$. Bad.

$v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). $v_3$ connected to $v_1, v_2, v_6$ (degree 3). $v_4$ connected to $v_1, v_2$ (degree 2). $v_5$ connected to $v_1, v_2$ (degree 2). $v_6$ connected to $v_1, v_3$ (degree 2).

Degrees: $v_1: 5, v_2: 4, v_3: 3, v_4: 2, v_5: 2, v_6: 2$. Unique max $v_1$. ✓

Remove $v_1$. Remaining: $v_2, v_3, v_4, v_5, v_6$ with edges $v_2 v_3, v_2 v_4, v_2 v_5, v_3 v_6$. Degrees: $v_2: 3, v_3: 2, v_4: 1, v_5: 1, v_6: 1$. Unique max $v_2$. ✓

Remove $v_2$. Remaining: $v_3, v_4, v_5, v_6$ with edge $v_3 v_6$. Degrees: $v_3: 1, v_6: 1, v_4: 0, v_5: 0$. Tie $v_3, v_6$. 2 days.

I need $v_3$ to have strictly more edges than $v_6$ after removing $v_1, v_2$. So $v_3$ needs an edge to $v_4$ or $v_5$ that doesn't go through $v_1$ or $v_2$.

But if $v_3 \sim v_4$, then $d_G(v_3) \geq 4$ (from $v_1, v_2, v_4, v_6$) and $d_G(v_4) \geq 3$ (from $v_1, v_2, v_3$). $d_G(v_3) = 4 = d_G(v_2)$. Tie. Bad.

If $v_3 \sim v_5$: $d_G(v_3) \geq 4$ (from $v_1, v_2, v_5, v_6$). $d_G(v_3) = 4 = d_G(v_2)$. Tie. Bad.

What if $v_2$ has degree 3 instead?

$v_1$ universal (degree 5). $v_2$ connected to $v_1, v_3, v_4$ (degree 3). $v_3$ connected to $v_1, v_2, v_4, v_5, v_6$ (degree 5). Tie with $v_1$. Bad.

$v_3$ connected to $v_1, v_2, v_4, v_5$ (degree 4). $v_4$ connected to $v_1, v_2, v_3$ (degree 3). Tie $v_2, v_4$. Bad.

$v_3$ connected to $v_1, v_2, v_5, v_6$ (degree 4). $v_4$ connected to $v_1, v_2$ (degree 2). $v_5$ connected to $v_1, v_3$ (degree 2). $v_6$ connected to $v_1, v_3$ (degree 2).

Degrees: $v_1: 5, v_3: 4, v_2: 3, v_4: 2, v_5: 2, v_6: 2$. Unique max $v_1$. ✓

Remove $v_1$. Remaining: $v_2, v_3, v_4, v_5, v_6$ with edges $v_2 v_3, v_2 v_4, v_3 v_5, v_3 v_6$. Degrees: $v_3: 3, v_2: 2, v_4: 1, v_5: 1, v_6: 1$. Unique max $v_3$. ✓

Remove $v_3$. Remaining: $v_2, v_4, v_5, v_6$ with edge $v_2 v_4$. Degrees: $v_2: 1, v_4: 1, v_5: 0, v_6: 0$. Tie $v_2, v_4$. 2 days.

Hmm, still 2. The issue is that after removing $v_1$ and $v_3$ (the first two removed), the remaining graph has a tie.

Let me try making $v_2$ have an extra edge.

$v_2$ connected to $v_1, v_3, v_4, v_5$ (degree 4). $v_3$ connected to $v_1, v_2, v_6$ (degree 3). $v_4$ connected to $v_1, v_2$ (degree 2). $v_5$ connected to $v_1, v_2$ (degree 2). $v_6$ connected to $v_1, v_3$ (degree 2).

Degrees: $v_1: 5, v_2: 4, v_3: 3, v_4: 2, v_5: 2, v_6: 2$. Unique max $v_1$. ✓

Remove $v_1$. Remaining: $v_2, v_3, v_4, v_5, v_6$ with edges $v_2 v_3, v_2 v_4, v_2 v_5, v_3 v_6$. Degrees: $v_2: 3, v_3: 2, v_4: 1, v_5: 1, v_6: 1$. Unique max $v_2$. ✓

Remove $v_2$. Remaining: $v_3, v_4, v_5, v_6$ with edge $v_3 v_6$. Degrees: $v_3: 1, v_6: 1, v_4: 0, v_5: 0$. Tie. 2 days.

The problem is always that $v_3$ and $v_6$ are tied after the second removal. I need $v_3$ to have an extra edge to $v_4$ or $v_5$, but that would increase $v_3$'s degree to 4, tying with $v_2$.

What if I increase $v_2$'s degree to 5 (universal)? Then $v_2$ ties with $v_1$. Bad.

What if $v_1$ is not universal?

$v_1$ connected to $v_2, v_3, v_4, v_5$ (not $v_6$). $d_G(v_1) = 4$.

$v_2$ connected to $v_1, v_3, v_4, v_5, v_6$ (degree 5). Too high. Bad.

$v_2$ connected to $v_1, v_3, v_4, v_6$ (degree 4). Tie with $v_1$. Bad.

$v_2$ connected to $v_1, v_3, v_6$ (degree 3). $v_3$ connected to $v_1, v_2, v_4, v_5, v_6$ (degree 5). Too high. Bad.

$v_3$ connected to $v_1, v_2, v_4, v_6$ (degree 4). Tie with $v_1$. Bad.

$v_3$ connected to $v_1, v_2, v_6$ (degree 3). $v_4$ connected to $v_1, v_3$ (degree 2). $v_5$ connected to $v_1$ (degree 1). $v_6$ connected to $v_2, v_3$ (degree 2).

Degrees: $v_1: 4, v_2: 3, v_3: 3, v_4: 2, v_5: 1, v_6: 2$. Tie $v_2, v_3$. Bad.

$v_2$ connected to $v_1, v_3, v_4, v_6$ (degree 4). Tie with $v_1$. Bad.

$v_1$ connected to $v_2, v_3, v_4, v_6$ (not $v_5$). $d_G(v_1) = 4$.

$v_2$ connected to $v_1, v_3, v_5, v_6$ (degree 4). Tie. Bad.

$v_2$ connected to $v_1, v_3, v_5$ (degree 3). $v_3$ connected to $v_1, v_2, v_4, v_5, v_6$ (degree 5). Bad.

$v_3$ connected to $v_1, v_2, v_4, v_6$ (degree 4). Tie. Bad.

$v_3$ connected to $v_1, v_2, v_6$ (degree 3). $v_4$ connected to $v_1, v_3$ (degree 2). $v_5$ connected to $v_2$ (degree 1). $v_6$ connected to $v_1, v_3$ (degree 2).

Degrees: $v_1: 4, v_2: 3, v_3: 3, v_4: 2, v_5: 1, v_6: 2$. Tie $v_2, v_3$. Bad.

Hmm, I keep getting ties. Let me try to be more creative.

$v_1$ connected to $v_2, v_3, v_4, v_5, v_6$ (universal, degree 5). $v_2$ connected to $v_1, v_3, v_4, v_5, v_6$ (degree 5). Tie. Bad.

OK, universal $v_1$ with $v_2$ also universal doesn't work. Let me try $v_1$ universal and $v_2$ with degree 4, but arrange so that after removing $v_1$ and $v_2$, the remaining graph has a unique max.

The issue is that $v_3$ (the third vertex to be removed) needs to have edges to $v_4, v_5, v_6$ that don't go through $v_1$ or $v_2$. But $v_3$'s degree is limited (must be $< d_G(v_2) = 4$ and $< d_G(v_1) = 5$, so $\leq 3$). $v_3$ is connected to $v_1$ and $v_2$ (both universal or near-universal), using up 2 of its 3 edges. So $v_3$ has at most 1 edge to $\{v_4, v_5, v_6\}$, giving it degree 1 in $G - v_1 - v_2$. Meanwhile, the neighbor of $v_3$ in $\{v_4, v_5, v_6\}$ also has degree 1 (from the edge to $v_3$). So we get a tie.

Unless $v_3$ is connected to 2 of $\{v_4, v_5, v_6\}$, but then $d_G(v_3) \geq 4$ (from $v_1, v_2$, and 2 others), tying with $v_2$.

So the constraint is: $v_3$ is connected to $v_1$ and $v_2$ (2 edges), and can have at most $d_G(v_3) - 2$ edges to $\{v_4, v_5, v_6\}$, where $d_G(v_3) \leq d_G(v_2) - 1$. If $d_G(v_2) = 4$, then $d_G(v_3) \leq 3$, so $v_3$ has at most 1 edge to $\{v_4, v_5, v_6\}$.

After removing $v_1, v_2$: $v_3$ has degree 1 (one edge to $\{v_4, v_5, v_6\}$). The vertex it's connected to also has degree $\geq 1$. For $v_3$ to be unique max, that vertex must have degree 0, contradiction.

So with $v_1$ universal and $v_2$ degree 4, we can't get 3 days for $n = 6$.

What if $v_1$ is not universal and $v_2$ is not connected to $v_3$?

$v_1$ connected to $v_2, v_4, v_5, v_6$ (not $v_3$). $d_G(v_1) = 4$. $v_2$ connected to $v_1, v_4, v_5, v_6$ (degree 4). Tie. Bad.

$v_2$ connected to $v_1, v_4, v_5$ (degree 3). $v_3$ connected to $v_4, v_5, v_6$ (degree 3, not connected to $v_1$ or $v_2$). $v_4$ connected to $v_1, v_2, v_3$ (degree 3). Tie $v_2, v_3, v_4$. Bad.

$v_3$ connected to $v_4, v_6$ (degree 2). $v_4$ connected to $v_1, v_2, v_3$ (degree 3). $v_5$ connected to $v_1, v_2$ (degree 2). $v_6$ connected to $v_1, v_3$ (degree 2).

Degrees: $v_1: 4, v_2: 3, v_4: 3, v_3: 2, v_5: 2, v_6: 2$. Tie $v_2, v_4$. Bad.

$v_4$ connected to $v_1, v_3$ (degree 2). $v_2$ connected to $v_1, v_4, v_5$ (degree 3). $v_3$ connected to $v_4, v_5, v_6$ (degree 3). Tie $v_2, v_3$. Bad.

$v_3$ connected to $v_4, v_6$ (degree 2). $v_2$ connected to $v_1, v_5, v_6$ (degree 3). $v_4$ connected to $v_1, v_3$ (degree 2). $v_5$ connected to $v_1, v_2$ (degree 2). $v_6$ connected to $v_1, v_2, v_3$ (degree 3). Tie $v_2, v_6$. Bad.

This is really hard. Let me try a completely different structure.

What about a graph where the degrees are $n-1, n-2, n-3, \ldots$? This is a "threshold graph" with degree sequence $n-1, n-2, \ldots, 1, 0$. But this is only possible for specific $n$ (it's the degree sequence of a specific graph).

Actually, the degree sequence $n-1, n-2, \ldots, 1, 0$ is graphical (it's the "half graph" or "threshold graph" $T_n$). In this graph, vertex $i$ is connected to vertex $j$ iff $i + j \geq n + 1$ (or some similar condition).

Wait, let me think about this. The threshold graph with degree sequence $n-1, n-2, \ldots, 1, 0$ is constructed by: start with one vertex, then alternately add dominating and isolated vertices.

For $n = 5$: degree sequence $4, 3, 2, 1, 0$. This is the graph where vertex 1 is connected to all (degree 4), vertex 2 is connected to vertex 1 (degree 1)... no, that gives degrees $4, 1, ...$. Let me think again.

The threshold graph with degrees $4, 3, 2, 1, 0$ for $n = 5$: 

Vertex with degree 4: connected to all 4 others.
Vertex with degree 0: connected to no one.
Vertex with degree 3: connected to 3 others. Since the degree-4 vertex is connected to everyone, this vertex is connected to the degree-4 vertex and 2 others (not the degree-0 vertex).
Vertex with degree 1: connected to 1 other. Must be the degree-4 vertex.
Vertex with degree 2: connected to 2 others. Must be the degree-4 vertex and the degree-3 vertex.

So: $v_1$ (deg 4) $\sim v_2, v_3, v_4, v_5$. $v_2$ (deg 3) $\sim v_1, v_3, v_4$. $v_3$ (deg 2) $\sim v_1, v_2$. $v_4$ (deg 1) $\sim v_1$. $v_5$ (deg 0): isolated.

Check: $d(v_1) = 4, d(v_2) = 3, d(v_3) = 2, d(v_4) = 1, d(v_5) = 0$. ✓

Remove $v_1$ (unique max, degree 4). Remaining: $v_2, v_3, v_4, v_5$ with edges $v_2 v_3, v_2 v_4$. Degrees: $v_2: 2, v_3: 1, v_4: 1, v_5: 0$. Unique max $v_2$. ✓

Remove $v_2$. Remaining: $v_3, v_4, v_5$ with no edges. Tie. 2 days.

Same as before. The threshold graph gives 2 days for $n = 5$.

Now, the key question: is 2 the maximum for $n = 5$? Let me think about whether 3 is ever possible.

For 3 days with $n = 5$, we need to remove 3 vertices, each being the unique max. After 3 removals, 2 vertices remain (tie, process stops).

Let me think about this more carefully. Let the removal order be $u_1, u_2, u_3$.

In $G$: $u_1$ is unique max.
In $G - u_1$: $u_2$ is unique max.
In $G - u_1 - u_2$: $u_3$ is unique max (among 3 vertices).

In $G - u_1 - u_2$: 3 vertices $u_3, u_4, u_5$. $u_3$ is unique max. The possible degree sequences (sorted) for 3 vertices with unique max:
- $2, 1, 1$: $u_3$ connected to both, $u_4 \sim u_5$ no. Degrees: $u_3: 2, u_4: 1, u_5: 1$. Unique max $u_3$. ✓
- $2, 1, 0$: $u_3$ connected to both, no other edge. Degrees: $u_3: 2, u_4: 1, u_5: 1$. Wait, that's $2, 1, 1$. 
  Actually: $u_3 \sim u_4, u_3 \sim u_5, u_4 \not\sim u_5$: degrees $2, 1, 1$. Unique max.
  $u_3 \sim u_4, u_3 \not\sim u_5, u_4 \sim u_5$: degrees $1, 2, 1$. $u_4$ is max, not $u_3$.
  $u_3 \sim u_4, u_3 \not\sim u_5, u_4 \not\sim u_5$: degrees $1, 1, 0$. Tie $u_3, u_4$.
  $u_3 \sim u_5, u_3 \not\sim u_4, u_4 \not\sim u_5$: degrees $1, 0, 1$. Tie $u_3, u_5$.
  $u_3 \sim u_5, u_3 \not\sim u_4, u_4 \sim u_5$: degrees $1, 1, 2$. $u_5$ is max.
  All three connected: degrees $2, 2, 2$. Tie.
  $u_3 \sim u_4, u_3 \sim u_5, u_4 \sim u_5$: degrees $2, 2, 2$. Tie.

So the only way $u_3$ is unique max in a 3-vertex graph is if $u_3$ is connected to both $u_4$ and $u_5$, and $u_4 \not\sim u_5$. Degrees: $u_3: 2, u_4: 1, u_5: 1$.

So in $G - u_1 - u_2$, we need edges $u_3 u_4$ and $u_3 u_5$, and no edge $u_4 u_5$.

These edges must be in $G$ (they're not affected by removing $u_1, u_2$ as long as they don't involve $u_1$ or $u_2$).

Now, in $G - u_1$: $u_2$ is unique max among $\{u_2, u_3, u_4, u_5\}$.

$d_{G-u_1}(u_2) > d_{G-u_1}(u_3), d_{G-u_1}(u_4), d_{G-u_1}(u_5)$.

$d_{G-u_1}(u_3) = d_G(u_3) - [u_3 \sim u_1]$. Since $u_3 \sim u_4$ and $u_3 \sim u_5$ in $G$, $d_G(u_3) \geq 2 + [u_3 \sim u_1] + [u_3 \sim u_2]$.

In $G - u_1 - u_2$, $u_3$ has degree 2 (edges to $u_4, u_5$). So $d_G(u_3) = 2 + [u_3 \sim u_1] + [u_3 \sim u_2]$.

Similarly, $d_G(u_4) = 1 + [u_4 \sim u_1] + [u_4 \sim u_2]$ (since $u_4$ has degree 1 in $G - u_1 - u_2$, from edge $u_3 u_4$).

$d_G(u_5) = 1 + [u_5 \sim u_1] + [u_5 \sim u_2]$.

$d_G(u_2) = [u_2 \sim u_1] + [u_2 \sim u_3] + [u_2 \sim u_4] + [u_2 \sim u_5]$.

$d_{G-u_1}(u_2) = d_G(u_2) - [u_2 \sim u_1] = [u_2 \sim u_3] + [u_2 \sim u_4] + [u_2 \sim u_5]$.

$d_{G-u_1}(u_3) = d_G(u_3) - [u_3 \sim u_1] = 2 + [u_3 \sim u_2]$.

$d_{G-u_1}(u_4) = d_G(u_4) - [u_4 \sim u_1] = 1 + [u_4 \sim u_2]$.

$d_{G-u_1}(u_5) = d_G(u_5) - [u_5 \sim u_1] = 1 + [u_5 \sim u_2]$.

For $u_2$ to be unique max in $G - u_1$:

$[u_2 \sim u_3] + [u_2 \sim u_4] + [u_2 \sim u_5] > 2 + [u_3 \sim u_2]$
$[u_2 \sim u_4] + [u_2 \sim u_5] > 2$ (since $[u_2 \sim u_3]$ cancels with $[u_3 \sim u_2]$)

So $[u_2 \sim u_4] + [u_2 \sim u_5] > 2$, meaning both $u_2 \sim u_4$ and $u_2 \sim u_5$ (sum = 2... wait, $> 2$ means $\geq 3$, but max is 2). 

Wait, $[u_2 \sim u_4] + [u_2 \sim u_5] > 2$. But each is 0 or 1, so the sum is at most 2. $> 2$ is impossible!

So we need $[u_2 \sim u_4] + [u_2 \sim u_5] > 2$, which is impossible. This means 3 days is impossible for $n = 5$!

Wait, let me double-check. We need:

$d_{G-u_1}(u_2) > d_{G-u_1}(u_3)$

$[u_2 \sim u_3] + [u_2 \sim u_4] + [u_2 \sim u_5] > 2 + [u_3 \sim u_2]$

Since $[u_2 \sim u_3] = [u_3 \sim u_2]$, this simplifies to:

$[u_2 \sim u_4] + [u_2 \sim u_5] > 2$

Which is impossible since each term is at most 1.

So for $n = 5$, 3 days is impossible, and the maximum is 2.

This is a key insight! Let me see if this generalizes.

The constraint is: in $G - u_1 - u_2$, $u_3$ has degree 2 (connected to $u_4, u_5$). In $G - u_1$, $u_3$ has degree $2 + [u_3 \sim u_2]$. For $u_2$ to beat $u_3$ in $G - u_1$, $u_2$ needs degree $> 2 + [u_3 \sim u_2]$ in $G - u_1$. But $u_2$'s degree in $G - u_1$ is at most 3 (connected to $u_3, u_4, u_5$). If $u_2 \
