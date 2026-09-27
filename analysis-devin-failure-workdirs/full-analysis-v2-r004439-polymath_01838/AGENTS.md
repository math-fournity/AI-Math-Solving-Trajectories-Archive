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
  <problem_id>polymath_01838</problem_id>
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

Let $n \geq 3$ be an integer. Consider an edge-coloring of the complete graph $K_n$ with $c$ colors such that each color forms a connected spanning subgraph of $K_n$. Let $M$ be the maximum value of $c$ such that there exists such a coloring where no triangle in $K_n$ has three edges of three distinct colors. Find $M$.

## Standard Solution

The problem states that if $k \geq 3$ and each of the $k$ colors forms a connected spanning subgraph, there must exist a triangle with three distinct colors (a rainbow triangle). This implies that for a coloring to have no rainbow triangles while each color is connected, the number of colors $c$ must satisfy $c < 3$. For $c=2$, we can easily construct a coloring of $K_n$ (for $n \geq 3$) using two colors such that each color forms a connected spanning subgraph. For example, let color 1 be a Hamiltonian path and color 2 be all other edges. Since $n \geq 3$, the complement of a Hamiltonian path in $K_n$ is also connected. Thus, the maximum such $c$ is 2.

## AI's Thinking (Attempted Solution Process)

The problem asks: Let $n \geq 3$ be an integer. Consider an edge-coloring of the complete graph $K_n$ with $c$ colors such that each color forms a connected spanning subgraph of $K_n$. Let $M$ be the maximum value of $c$ such that there exists such a coloring where no triangle in $K_n$ has three edges of three distinct colors. Find $M$.

Let me think about this carefully.

We have an edge-coloring of $K_n$ with $c$ colors. Each color class forms a connected spanning subgraph (i.e., each color's edges span all $n$ vertices and form a connected graph). No triangle has three edges of three distinct colors (i.e., every triangle uses at most 2 colors).

We want to maximize $c$.

First, let me think about small cases and the structure.

The condition "no triangle has three distinct colors" is a Gallai coloring condition (but Gallai colorings usually don't require the rainbow triangle condition... actually a Gallai coloring is exactly one with no rainbow triangle). So this is a Gallai coloring where additionally each color class is connected and spanning.

Wait, but in a Gallai coloring, the structure is well-known: there's a hierarchical structure. But here we have the additional constraint that each color class is connected and spanning.

Let me think about the constraint that each color is connected and spanning. Each color class must be a connected spanning subgraph, meaning it touches all $n$ vertices and is connected. A connected spanning subgraph has at least $n-1$ edges. So if we have $c$ colors, total edges $\geq c(n-1)$. Total edges in $K_n$ is $\binom{n}{2} = \frac{n(n-1)}{2}$. So $c(n-1) \leq \frac{n(n-1)}{2}$, giving $c \leq \frac{n}{2}$.

So $c \leq \lfloor n/2 \rfloor$.

Now the question is whether this bound is achievable with the no-rainbow-triangle condition.

Let me think about constructions.

For $n = 3$: $K_3$ has 3 edges. Each color must be connected spanning, so each color needs at least 2 edges (a spanning tree on 3 vertices). With 3 edges total, we can have at most 1 color with 2 edges... wait, $c \leq 3/2 = 1.5$, so $c \leq 1$. With $c = 1$, all edges same color, connected, no rainbow triangle. So $M = 1$ for $n = 3$.

Hmm wait, but can we do $c = 1$? Yes. Can we do more? $c \leq 1$ from the bound. So $M(3) = 1$.

For $n = 4$: $c \leq 2$. Can we achieve $c = 2$? We need 2 colors, each connected spanning. $K_4$ has 6 edges. Each color needs at least 3 edges. $2 \times 3 = 6$, so each color is a spanning tree (3 edges). We need to partition $K_4$'s edges into 2 spanning trees, with no rainbow triangle.

$K_4$ can be decomposed into 2 Hamiltonian paths or 2 spanning trees. For example, color 1: edges of a path $1-2-3-4$ (edges 12, 23, 34). Color 2: remaining edges 13, 14, 24. Is color 2 connected? Vertices 1,3,4,2 with edges 13, 14, 24. Vertex 1 connects to 3 and 4, vertex 4 connects to 2. So it's connected (1-3, 1-4, 4-2). Yes, spanning tree.

Now check triangles:
- Triangle 123: edges 12 (c1), 23 (c1), 13 (c2). Two colors. OK.
- Triangle 124: edges 12 (c1), 14 (c2), 24 (c2). Two colors. OK.
- Triangle 134: edges 13 (c2), 14 (c2), 34 (c1). Two colors. OK.
- Triangle 234: edges 23 (c1), 24 (c2), 34 (c1). Two colors. OK.

So $M(4) = 2$.

For $n = 5$: $c \leq 2$. Can we achieve $c = 2$? Need 2 colors each connected spanning, at least 4 edges each, total at least 8, but $K_5$ has 10 edges. So feasible. Need to partition into 2 connected spanning subgraphs with no rainbow triangle.

Actually with only 2 colors, every triangle automatically has at most 2 colors, so the rainbow condition is automatically satisfied! So we just need to partition $K_n$'s edges into 2 connected spanning subgraphs. This is always possible for $n \geq 4$ (we can take a spanning tree for color 1 and the rest for color 2, as long as the rest is connected).

Wait, for $n = 5$, $c = 2$: take a spanning tree (4 edges) for color 1, remaining 6 edges for color 2. Is color 2 connected? The complement of a spanning tree in $K_5$ has 6 edges. For $n \geq 4$, the complement of a spanning tree is connected (since a spanning tree has $n-1$ edges, complement has $\binom{n}{2} - (n-1) = \frac{(n-1)(n-2)}{2}$ edges, and for $n \geq 4$ this is at least 3 and the complement is connected). Actually, let me verify: for $n = 4$, complement of spanning tree has 3 edges. A spanning tree on 4 vertices is a path or star. If it's a path 1-2-3-4, complement edges are 13, 14, 24, which we showed is connected. If it's a star centered at 1 (edges 12, 13, 14), complement is 23, 24, 34, which is a triangle on 2,3,4 — connected but doesn't span vertex 1! So we need to be careful.

So for $n = 4$ with a star spanning tree, color 2 doesn't span. But we found a working decomposition using a path. So we need to choose the spanning tree carefully.

For general $n$ and $c = 2$: we need to partition $K_n$ into 2 connected spanning subgraphs. This is possible for $n \geq 4$ by taking a Hamiltonian path for color 1 (the complement of a Hamiltonian path is connected for $n \geq 4$). Let me verify: Hamiltonian path $1-2-3-\cdots-n$. Complement edges: all non-consecutive pairs. Is this connected? Vertex 1 connects to 3, 4, ..., n. Vertex 2 connects to 4, 5, ..., n. Etc. For $n \geq 4$, vertex 1 connects to vertex 3 (not consecutive), so yes it's connected and spans all vertices.

OK so $c = 2$ is achievable for all $n \geq 4$.

Now the key question: can we achieve $c = \lfloor n/2 \rfloor$?

For $n$ even, $c = n/2$. Each color needs at least $n-1$ edges, total $\geq (n/2)(n-1) = n(n-1)/2 = \binom{n}{2}$. So each color must be exactly a spanning tree, and the decomposition is a tree decomposition of $K_n$ into $n/2$ spanning trees. By Nash-Williams theorem, $K_n$ can be decomposed into $\lceil n/2 \rceil$ spanning trees... wait, let me recall. Nash-Williams says the minimum number of spanning trees needed to cover $K_n$ is $\lceil n/2 \rceil$. Actually, the arboricity of $K_n$ is $\lceil n/2 \rceil$.

Hmm, so for $n$ even, arboricity is $n/2$, and $K_n$ can be decomposed into $n/2$ spanning trees. But we also need the no-rainbow-triangle condition.

For $n$ odd, $c = (n-1)/2$. Each color needs at least $n-1$ edges, total $\geq ((n-1)/2)(n-1) = (n-1)^2/2$. Total edges $= n(n-1)/2$. So we have $n(n-1)/2 - (n-1)^2/2 = (n-1)(n - (n-1))/2 = (n-1)/2$ extra edges to distribute. So it's feasible edge-count-wise.

But the rainbow triangle condition is the real constraint. Let me think about whether $\lfloor n/2 \rfloor$ is always achievable.

Let me think about this more carefully. The condition is a Gallai coloring (no rainbow triangle) where each color class is connected and spanning.

Let me think about the structure of Gallai colorings. A Gallai coloring has a recursive structure: the vertices can be partitioned into non-empty sets $V_1, \ldots, V_k$ (with $k \geq 2$) such that all edges between different parts use at most 2 colors, and edges within each part use colors not used between parts (or something like that). Actually, the Gallai decomposition theorem says: in a Gallai coloring, there exists a non-trivial partition of the vertex set such that between parts, at most 2 colors are used, and within each part, only colors not used between parts are used.

Hmm, this is getting complex. Let me think about specific constructions.

Let me try to construct colorings achieving $c = \lfloor n/2 \rfloor$ for general $n$.

**Construction idea for even $n = 2m$:**

Label vertices $1, 2, \ldots, 2m$. We want $m$ colors, each forming a connected spanning subgraph, with no rainbow triangle.

Idea: Use a "wreath" or "cyclic" construction. 

Actually, let me think about a simpler approach. Consider the vertices arranged in a cycle $1, 2, \ldots, n$. 

Hmm, let me think about this differently. 

Let me consider the case $n = 4$ ($m = 2$) which we solved: $M = 2 = n/2$. ✓

Let me try $n = 6$ ($m = 3$). We want 3 colors, each a spanning tree (since $3 \times 5 = 15 = \binom{6}{2}$). So we need to decompose $K_6$ into 3 spanning trees with no rainbow triangle.

One known decomposition of $K_{2m}$ into $m$ spanning trees: Label vertices $0, 1, \ldots, 2m-1$. For $i = 0, 1, \ldots, m-1$, tree $T_i$ consists of edges $\{j, j+i+1\}$ for $j = 0, 1, \ldots, 2m-1$ (mod $2m$), but this gives a 2-factor (collection of cycles), not a tree. 

Let me think of another approach. 

Actually, let me think about what structures avoid rainbow triangles while having many colors.

Key insight: If we use a "2-coloring between groups" structure, we can have many colors.

Let me try the following construction for even $n = 2m$:

Partition vertices into pairs: $(1,2), (3,4), \ldots, (2m-1, 2m)$.

For each pair $(2i-1, 2i)$, color the edge between them with color $i$.

Now, for edges between different pairs, we need to color them such that:
1. Each color class is connected and spanning.
2. No rainbow triangle.

Hmm, this is getting complicated. Let me think differently.

Let me think about the problem from the perspective of the answer. The bound is $c \leq \lfloor n/2 \rfloor$. The question is whether this is tight.

Let me try to verify for $n = 5$: $c \leq 2$. We showed $c = 2$ works. So $M(5) = 2 = \lfloor 5/2 \rfloor$. ✓

For $n = 6$: $c \leq 3$. Can we achieve $c = 3$?

Let me try to construct a coloring of $K_6$ with 3 colors, each a spanning tree, no rainbow triangle.

$K_6$ has 15 edges. 3 spanning trees, each 5 edges.

Let me try a specific construction. Vertices: 1,2,3,4,5,6.

Consider the "blow-up" approach. Take $K_3$ on vertices $\{a, b, c\}$ where $a = \{1,2\}$, $b = \{3,4\}$, $c = \{5,6\}$.

Color edges between groups using 2 colors (say colors 1 and 2), and edges within groups using color 3.

Within groups: edges 12, 34, 56 all get color 3. Color 3's edges: 12, 34, 56. But this is not connected! Three separate edges.

So this doesn't work directly. We need color 3 to be connected and spanning.

Let me modify: within groups, use color 3, but also assign some inter-group edges to color 3 to make it connected.

Actually, let me think about this more carefully using the Gallai coloring structure.

In a Gallai coloring, there's a hierarchical partition. At the top level, we partition vertices into groups, and between groups we use at most 2 colors. Within groups, we recursively use Gallai colorings with colors disjoint from the inter-group colors (or at least, the inter-group colors don't appear within groups — actually the theorem says the colors used within a part are disjoint from colors used between parts at that level).

Wait, I need to be more careful. The Gallai theorem says: Given a Gallai coloring, there exists a partition of $V$ into $k \geq 2$ non-empty parts such that:
- Between parts, at most 2 colors are used.
- For each part, the colors used on edges within that part are disjoint from the colors used between parts.

So if we use 2 colors between parts, those 2 colors don't appear within any part. The colors within parts are all different from the inter-group colors.

Now, for each color to be connected and spanning, we need:
- The 2 inter-group colors: each must be connected and spanning. The inter-group edges form a 2-colored complete multipartite graph. For each of the 2 colors to be connected and spanning, each color's inter-group edges must connect all groups (and since within-group edges of these colors don't exist, connectivity must come purely from inter-group edges, which means each group must be touched).

- The colors within parts: each must be connected and spanning. But a color used only within one part doesn't span all vertices! So this is a problem.

Wait, this means that in a Gallai coloring, colors used within parts are only used within those parts, so they can't be spanning (unless a part is the whole vertex set, which contradicts the partition).

Hmm, but that's the strict Gallai decomposition. Let me reconsider.

Actually, the Gallai theorem is about the existence of such a partition, but the colors within parts could potentially also be used between parts. Let me re-read the theorem.

The Gallai decomposition theorem: In any Gallai coloring of $K_n$, there exists a non-trivial partition $V = V_1 \cup \cdots \cup V_k$ ($k \geq 2$) such that all edges between different parts use at most 2 colors, and these colors are not used on any edge within any part.

So the inter-group colors (at most 2) are NOT used within any part. The within-part colors are different from inter-group colors. This means within-part colors are only used within parts, so they can't be spanning (unless a part = entire vertex set).

This means: if we have a Gallai coloring where every color is connected and spanning, then the Gallai decomposition must be trivial, i.e., we can't have a non-trivial partition. But the theorem says a non-trivial partition always exists for $n \geq 2$...

Wait, that would mean the only Gallai coloring where every color is spanning is one where all edges between parts use at most 2 colors AND those 2 colors are the only colors (since within-part colors can't be spanning). But then $c \leq 2$.

But we showed $M(4) = 2$ and $M(6)$ might be 3. Let me re-examine.

Hmm, wait. The Gallai theorem applies to colorings with at least 3 colors (or at least, the interesting case is when there are rainbow triangles to avoid). If we have only 2 colors, there are no rainbow triangles trivially, and the Gallai decomposition might not apply in the same way.

Actually, the Gallai theorem says: a coloring has no rainbow triangle if and only if it's a Gallai coloring, which has the recursive partition structure. But if we have only 2 colors, every coloring is automatically a Gallai coloring (no rainbow triangle possible), and the partition structure is trivially satisfied (any partition works since between parts we use at most 2 colors).

So for $c \geq 3$, the Gallai structure applies, and the inter-group colors (at most 2) are not used within parts. The within-part colors are only used within their respective parts, so they can't be spanning.

This means: if $c \geq 3$, we can't have all colors spanning, because the Gallai decomposition forces some colors to be confined to parts.

Wait, but this would mean $M \leq 2$ for all $n$! But we showed $M(4) = 2$ and the bound $c \leq \lfloor n/2 \rfloor$ gives $c \leq 2$ for $n = 4, 5$.

Hmm, but for $n = 6$, the bound gives $c \leq 3$. If the Gallai argument shows $c \leq 2$, then $M(6) = 2$.

Wait, let me re-examine the Gallai theorem more carefully. The theorem says there EXISTS a partition with these properties. It doesn't say every partition has these properties. And the "colors not used within parts" refers to the specific inter-group colors at this level of the decomposition.

Let me re-examine: if we have a Gallai coloring with $c \geq 3$ colors, there exists a non-trivial partition where between parts, at most 2 colors are used, and those 2 colors don't appear within any part.

So the remaining $c - 2$ (or $c - 1$) colors are used only within parts. Since each part is a proper subset of $V$, these colors are not spanning. So they can't be connected and spanning.

Therefore, if every color must be connected and spanning, we can have at most 2 colors that appear between parts, and any color used only within a part can't be spanning. So $c \leq 2$.

But wait, this argument has a subtlety. The Gallai decomposition is recursive. At the top level, we have at most 2 inter-group colors. Within each part, we have a recursive Gallai coloring. The colors within a part could potentially also be used in other parts or between parts at a different level.

Hmm, actually no. The theorem says the inter-group colors at the top level are not used within any part. But colors used within part $V_1$ could also be used within part $V_2$ or between parts at a deeper level. However, they're still not used between the top-level parts, so they're confined to within the top-level parts. A color confined to within top-level parts appears only within $V_1 \cup V_2 \cup \cdots \cup V_k$ but not on any inter-group edge. For this color to be connected and spanning, it would need to connect vertices across different parts, but it has no inter-group edges. So it can only be connected within a single part, meaning it's not spanning (unless $k = 1$, contradiction).

Wait, unless a color appears in multiple parts. Say color $\alpha$ appears within $V_1$ and within $V_2$. Then color $\alpha$'s subgraph has components in $V_1$ and components in $V_2$, but no edges between $V_1$ and $V_2$ (since $\alpha$ is not an inter-group color). So color $\alpha$ is disconnected. Not connected.

So indeed, any color that is not an inter-group color at the top level cannot be connected and spanning. Therefore, all connected-and-spanning colors must be among the at most 2 inter-group colors. So $c \leq 2$.

But wait, this seems to contradict the edge-count bound for large $n$. For $n = 6$, the edge-count bound gives $c \leq 3$, but the Gallai argument gives $c \leq 2$. So $M(6) = 2$?

Hmm, but wait. Let me reconsider. The Gallai decomposition theorem requires the coloring to be a Gallai coloring (no rainbow triangle). If $c \leq 2$, there are no rainbow triangles trivially. If $c \geq 3$, the Gallai theorem applies.

So for $c \geq 3$: Gallai theorem gives a partition with at most 2 inter-group colors, and those are the only colors that can be spanning. So $c \leq 2$, contradiction. Therefore $c \leq 2$.

For $c \leq 2$: no rainbow triangle automatically. We just need both colors to be connected and spanning. This is possible for $n \geq 4$ (as we showed). For $n = 3$, $c = 1$ (since 2 colors each need 2 edges, total 4 > 3 edges).

Wait, for $n = 3$: $c = 2$? Each color needs at least 2 edges (spanning tree on 3 vertices). Total $\geq 4 > 3 = \binom{3}{2}$. So $c \leq 1$. $M(3) = 1$.

For $n \geq 4$: $c = 2$ is achievable (partition $K_n$ into 2 connected spanning subgraphs). $c = 3$ is impossible by Gallai argument. So $M(n) = 2$ for $n \geq 4$.

Wait, but let me double-check the Gallai argument. Is it really true that in a Gallai coloring with $\geq 3$ colors, there's a non-trivial partition where inter-group colors (at most 2) don't appear within parts?

Yes, this is the Gallai decomposition theorem (also known as the Gallai-Edmonds structure theorem for colorings, or simply Gallai's theorem on rainbow-triangle-free colorings).

The theorem (Gyárfás-Simonyi): A coloring of $K_n$ is a Gallai coloring (no rainbow triangle) if and only if there exists a non-trivial partition of the vertices such that between parts, at most 2 colors are used, and no color used between parts is used within any part.

So yes, the argument holds. For $c \geq 3$, we get a non-trivial partition, and only the at most 2 inter-group colors can be spanning. So $c \leq 2$, contradiction.

Therefore $M = 2$ for $n \geq 4$ and $M = 1$ for $n = 3$.

Wait, but the problem says "Let $n \geq 3$ be an integer" and asks to "Find $M$". It seems like they want a single answer. Let me re-read.

"Let $n \geq 3$ be an integer. Consider an edge-coloring of the complete graph $K_n$ with $c$ colors such that each color forms a connected spanning subgraph of $K_n$. Let $M$ be the maximum value of $c$ such that there exists such a coloring where no triangle in $K_n$ has three edges of three distinct colors. Find $M$."

So $M$ depends on $n$. The answer should be a function of $n$.

$M(3) = 1$, $M(n) = 2$ for $n \geq 4$.

Hmm, but let me double-check $n = 3$ more carefully. $K_3$ has 3 edges. With $c = 1$: all edges one color, connected spanning, no rainbow triangle. With $c = 2$: need each color connected spanning, so each needs $\geq 2$ edges, total $\geq 4 > 3$. Impossible. So $M(3) = 1$.

For $n \geq 4$: $M(n) = 2$.

Actually, wait. Let me reconsider whether the problem is asking for a general formula. The answer is:

$$M = \begin{cases} 1 & \text{if } n = 3 \\ 2 & \text{if } n \geq 4 \end{cases}$$

Or maybe they want just $M = 2$ for $n \geq 4$ and note $n = 3$ is special. Let me re-examine.

Actually, I realize I should double-check my Gallai theorem argument more carefully. Let me make sure the theorem is correctly stated and applied.

The Gallai decomposition theorem: If $G$ is a complete graph on $n \geq 2$ vertices with an edge-coloring that contains no rainbow triangle, then there exists a non-trivial partition $\{V_1, \ldots, V_k\}$ of $V(G)$ (with $k \geq 2$) such that:
1. Between any two parts $V_i$ and $V_j$, all edges have the same color (or more generally, at most 2 colors are used between all pairs of parts).
2. The colors used on edges between different parts are at most 2, and these colors are not used on any edge within any part.

Actually, I want to be precise. There are different versions of the theorem. The standard version (see Gyárfás-Simonyi, 2004):

**Theorem (Gallai):** In any Gallai coloring of a complete graph, there exists a non-trivial partition of the vertex set into non-empty parts $V_1, \ldots, V_k$ ($k \geq 2$) such that:
- Between parts, at most two colors are used.
- No color appearing between parts appears within any part.

This is correct. So my argument holds.

Now, the argument: Suppose $c \geq 3$ and all colors are connected and spanning. By Gallai's theorem, there's a non-trivial partition with at most 2 inter-group colors, and these colors don't appear within any part. The remaining $c - |\text{inter-group colors}| \geq c - 2 \geq 1$ colors appear only within parts. 

For any such "within-part" color $\alpha$: $\alpha$ appears only within parts $V_1, \ldots, V_k$ but not on any inter-group edge. Since $k \geq 2$, the vertices in $V_1$ and $V_2$ are not connected by any $\alpha$-colored edge. So the $\alpha$-colored subgraph is disconnected (it has no edges between $V_1$ and $V_2$). This contradicts $\alpha$ being connected and spanning.

Wait, I need to be a bit more careful. Color $\alpha$ might appear within $V_1$ but not within $V_2$. Or it might appear within both. In either case, since $\alpha$ has no inter-group edges, the $\alpha$-subgraph has no edges between different parts. If $\alpha$ appears in at least two different parts, it's clearly disconnected. If $\alpha$ appears in only one part, it doesn't span all vertices. Either way, $\alpha$ is not connected and spanning.

So the contradiction holds. Therefore $c \leq 2$ when we require all colors to be connected and spanning (and no rainbow triangle, which is automatic for $c \leq 2$).

Hmm wait, but actually I need to also handle the case $c = 2$ more carefully. For $c = 2$, the no-rainbow-triangle condition is automatic (any triangle has at most 2 colors). We need both colors to be connected and spanning. 

For $n \geq 4$: We can partition $K_n$'s edges into 2 connected spanning subgraphs. Construction: Take a Hamiltonian path $P = v_1 v_2 \cdots v_n$ (edges $v_i v_{i+1}$ for $i = 1, \ldots, n-1$), color these with color 1. Color all remaining edges with color 2.

Color 1 (the path) is connected and spanning. ✓

Color 2: edges are all non-consecutive pairs. Is this connected? For $n \geq 4$, vertex $v_1$ is connected to $v_3, v_4, \ldots, v_n$ (all non-consecutive to $v_1$, i.e., not $v_2$). So $v_1$ has edges to $v_3, \ldots, v_n$ in color 2. Similarly, $v_2$ connects to $v_4, \ldots, v_n$. And $v_n$ connects to $v_1, \ldots, v_{n-2}$. So color 2 is connected (in fact, it's quite dense). ✓

For $n = 3$: $c = 2$ requires each color to have $\geq 2$ edges (spanning tree on 3 vertices), total $\geq 4 > 3 = \binom{3}{2}$. Impossible. So $M(3) = 1$.

So the answer is:

$$M = \begin{cases} 1 & \text{if } n = 3, \\ 2 & \text{if } n \geq 4. \end{cases}$$

Hmm, but the problem says "Let $n \geq 3$ be an integer" and asks to "Find $M$". This phrasing suggests $M$ might be a single expression in $n$. Let me reconsider whether $M(3) = 1$ fits a pattern.

$\lfloor n/2 \rfloor$ gives: $n=3 \to 1$, $n=4 \to 2$, $n=5 \to 2$, $n=6 \to 3$. But we showed $M(6) = 2 \neq 3$. So it's not $\lfloor n/2 \rfloor$.

Actually, $M = 2$ for $n \geq 4$ and $M = 1$ for $n = 3$. We can write this as $M = \min(2, \lfloor n/2 \rfloor)$ or just state the cases.

Actually, $\min(2, \lfloor n/2 \rfloor)$: $n=3 \to \min(2,1) = 1$, $n=4 \to \min(2,2) = 2$, $n=5 \to \min(2,2) = 2$, $n \geq 4 \to 2$. Yes, that works.

Or we can simply say $M = 2$ for $n \geq 4$ and $M = 1$ for $n = 3$.

Let me write up the proof.

Actually, I want to make sure my application of Gallai's theorem is rigorous. Let me also consider: does Gallai's theorem apply when $c = 2$? If $c = 2$, there are no rainbow triangles, so it's a Gallai coloring. The theorem gives a non-trivial partition with at most 2 inter-group colors. Since $c = 2$, both colors could be inter-group colors, and there are no within-part colors. So the argument doesn't give a contradiction for $c = 2$. Good.

For $c = 3$: Gallai's theorem gives a partition with at most 2 inter-group colors. At least 1 color is a within-part color, which can't be spanning. Contradiction. So $c \leq 2$.

This is clean. Let me write the proof.

Wait, I should also verify: for $c = 2$ and $n \geq 4$, is it always possible? I gave a construction above. Let me verify once more for $n = 4$.

$K_4$, vertices 1,2,3,4. Hamiltonian path 1-2-3-4. Color 1: edges 12, 23, 34. Color 2: edges 13, 14, 24.
- Color 1: path 1-2-3-4, connected, spanning. ✓
- Color 2: edges 13, 14, 24. Vertex 1 connects to 3,4. Vertex 4 connects to 1,2. So 1-3, 1-4, 4-2: connected, spanning. ✓
- No rainbow triangle (only 2 colors). ✓

Great.

Now let me also think about whether there's an issue with the Gallai theorem for $n = 3$ and $c = 2$. For $n = 3$, $c = 2$: we have a triangle with 2 colors. This is a Gallai coloring. The theorem gives a non-trivial partition. For example, partition $\{1\}, \{2,3\}$. Inter-group edge is 12 (one color). Within $\{2,3\}$: edge 23 (another color). So inter-group color doesn't appear within parts. This is consistent. But the issue is just the edge count: 2 colors each need $\geq 2$ edges, total $\geq 4 > 3$.

OK, I'm confident in the answer. Let me write the proof.

Let me also think about whether the problem might have a different intended answer. The problem is from a competition-style setting. The answer $M = 2$ for $n \geq 4$ (and $M = 1$ for $n = 3$) seems clean and the proof is elegant using Gallai's theorem.

Let me write the complete proof.

Proof structure:
1. Upper bound: $M \leq 2$ for $n \geq 4$ (using Gallai's theorem), and $M \leq 1$ for $n = 3$ (edge count).
2. Lower bound: $M \geq 2$ for $n \geq 4$ (construction), and $M \geq 1$ for $n = 3$ (trivial).

For the upper bound with Gallai's theorem, I should state and prove (or at least sketch) the theorem, since this is a self-contained proof.

Actually, for a competition proof, I should either cite Gallai's theorem (if it's well-known enough) or prove the needed special case. Let me prove the needed special case directly.

**Lemma (special case of Gallai's theorem):** If $K_n$ ($n \geq 2$) is edge-colored with no rainbow triangle and at least 3 colors, then there exists a non-trivial partition of the vertices such that at most 2 colors are used between parts, and these colors do not appear within any part.

Actually, for the proof, I can prove a weaker statement that suffices: If $K_n$ is edge-colored with no rainbow triangle and at least 3 colors, then there exist two non-empty disjoint sets $A, B$ with $A \cup B = V$ such that at most 2 colors are used on edges between $A$ and $B$, and these colors don't appear within $A$ or $B$.

Hmm, actually for the proof I need the full partition version. Let me just cite Gallai's theorem and provide a brief proof sketch.

Actually, let me think about whether I can prove the result without the full Gallai theorem, using a simpler argument.

Alternative approach: Suppose we have $c \geq 3$ colors, each connected and spanning, no rainbow triangle. 

Pick any 3 colors, say red, blue, green. Consider the subgraph formed by red edges. It's connected and spanning. Similarly for blue and green.

Consider any triangle. It uses at most 2 colors. 

Hmm, let me think of a more direct argument.

Take any edge $uv$ of color 1 (red). Since color 2 (blue) is connected and spanning, there's a blue path from $u$ to $v$. Let this path be $u = w_0, w_1, \ldots, w_k = v$ with all edges blue. Consider the triangle $u, v, w_1$: edges $uv$ (red), $uw_1$ (blue), $vw_1$ (?). For no rainbow triangle, $vw_1$ must be red or blue.

If $vw_1$ is red: triangle $u, v, w_1$ has colors red, blue, red — OK.
If $vw_1$ is blue: triangle $u, v, w_1$ has colors red, blue, blue — OK.
If $vw_1$ is some other color: rainbow triangle — not allowed.

So $vw_1 \in \{\text{red}, \text{blue}\}$.

This is getting complicated. Let me just use Gallai's theorem. I'll state it and give a proof.

Actually, let me try to prove the key lemma directly.

**Key Lemma:** In an edge-coloring of $K_n$ with no rainbow triangle, if $c \geq 3$ colors are used, then there exists a non-trivial partition of $V$ into parts $V_1, \ldots, V_k$ ($k \geq 2$) such that at most 2 colors appear on edges between different parts, and these colors do not appear on edges within any part.

*Proof sketch:* We proceed by induction on $n$. For $n = 2$, trivial (only 1 edge, so $c \leq 1$, contradiction with $c \geq 3$). 

For the inductive step: Pick a vertex $v$. If the edges incident to $v$ use at most 2 colors, then we can try to partition based on the colors of edges from $v$.

Actually, the standard proof of Gallai's theorem is a bit involved. Let me just state it as a known theorem and use it. In a competition setting, Gallai's theorem is a well-known result.

Hmm, but actually, let me think about whether I can give a simpler self-contained argument for this specific problem.

**Direct argument for $c \leq 2$:**

Suppose for contradiction that $c \geq 3$ and all colors are connected and spanning, with no rainbow triangle.

Pick three colors: $\alpha, \beta, \gamma$. 

Since $\alpha$ is connected and spanning, pick any $\alpha$-edge $uv$. Since $\beta$ is connected and spanning, there exists a $\beta$-path from $u$ to $v$: $u = w_0, w_1, \ldots, w_k = v$ with all edges $\beta$-colored. Since $uv$ is $\alpha$-colored and $k \geq 2$ (because $uv$ is not $\beta$), we have $k \geq 2$.

Consider triangle $\{u, v, w_1\}$: $uv$ is $\alpha$, $uw_1$ is $\beta$, so $vw_1$ must be $\alpha$ or $\beta$.

Consider triangle $\{u, w_1, w_2\}$: $uw_1$ is $\beta$, $w_1 w_2$ is $\beta$, so $uw_2$ can be any color (no constraint from this triangle since two edges are already $\beta$).

Hmm, this approach is getting complicated. Let me try yet another approach.

Actually, let me try to prove the result using the following observation:

**Claim:** If $c \geq 3$ and all colors are connected and spanning, then there exists a rainbow triangle.

*Proof:* Pick any edge $e = uv$ of color 1. Since color 2 is connected and spanning, there's a color-2 path $P$ from $u$ to $v$. Let $P = u = x_0, x_1, \ldots, x_m = v$ with $m \geq 2$ (since $uv$ is color 1, not color 2). 

Now, for each $i = 1, \ldots, m$, consider the edge $vx_i$ (or $ux_i$). 

Consider triangle $\{u, v, x_1\}$: $uv$ is color 1, $ux_1$ is color 2. So $vx_1$ is color 1 or color 2.

Case 1: $vx_1$ is color 1. Then consider triangle $\{v, x_1, x_2\}$: $vx_1$ is color 1, $x_1 x_2$ is color 2. So $vx_2$ is color 1 or color 2.

Subcase 1a: $vx_2$ is color 1. Continue: triangle $\{v, x_2, x_3\}$: $vx_2$ is color 1, $x_2 x_3$ is color 2. So $vx_3$ is color 1 or color 2.

...and so on. If at every step $vx_i$ is color 1, then $vx_m = vv$ which doesn't make sense. Actually $x_m = v$, so $vx_m = vv$ is not an edge. Let me reconsider.

Actually, $x_m = v$, so the last vertex is $v$ itself. Let me reconsider the path. The path is $u = x_0, x_1, \ldots, x_m = v$ with $m \geq 2$. So $x_1, \ldots, x_{m-1}$ are intermediate vertices.

For $i = 1, \ldots, m-1$, consider edge $vx_i$ (connecting $v$ to intermediate vertex $x_i$).

Triangle $\{u, v, x_1\}$: $uv$ color 1, $ux_1$ color 2 ⟹ $vx_1$ ∈ {1, 2}.
Triangle $\{v, x_1, x_2\}$: $x_1 x_2$ color 2, and $vx_1$ ∈ {1, 2}.

If $vx_1$ is color 2: triangle $\{v, x_1, x_2\}$ has $vx_1$ color 2, $x_1 x_2$ color 2, so $vx_2$ can be anything.
If $vx_1$ is color 1: triangle $\{v, x_1, x_2\}$ has $vx_1$ color 1, $x_1 x_2$ color 2, so $vx_2$ ∈ {1, 2}.

This is getting messy. Let me try a different approach.

Let me try to use the following cleaner argument:

**Claim:** In a no-rainbow-triangle coloring of $K_n$ where all $c$ colors are connected and spanning, $c \leq 2$.

**Proof:** Suppose $c \geq 3$. Pick three colors $\alpha, \beta, \gamma$.

Since $\gamma$ is connected and spanning, there exists a $\gamma$-edge $uv$. 

Since $\alpha$ is connected and spanning, there's an $\alpha$-path from $u$ to $v$: $u = p_0, p_1, \ldots, p_a = v$.
Since $\beta$ is connected and spanning, there's a $\beta$-path from $u$ to $v$: $u = q_0, q_1, \ldots, q_b = v$.

Both paths have length $\geq 2$ (since $uv$ is $\gamma$, not $\alpha$ or $\beta$).

Now, consider the $\alpha$-path $P_\alpha$ and the $\beta$-path $P_\beta$. 

Hmm, this is still complicated. Let me just use Gallai's theorem. It's a standard result and the proof is well-known.

Let me write the proof using Gallai's theorem, and include a proof of the theorem (or at least a sketch).

Actually, for a clean competition proof, let me prove the following lemma which is the key ingredient:

**Lemma:** In an edge-coloring of $K_n$ with no rainbow triangle, if there are $\geq 3$ colors, then some color is not connected and spanning.

**Proof of Lemma:** We prove this by induction on $n$.

Base case $n = 3$: With 3 colors on $K_3$, each edge has a distinct color, forming a rainbow triangle. Contradiction. So with no rainbow triangle, $c \leq 2$ on $K_3$, and the lemma is vacuously true (there can't be $\geq 3$ colors).

Wait, that's not quite right. On $K_3$ with no rainbow triangle, we can have at most 2 colors. So $c \geq 3$ is impossible, and the lemma holds vacuously.

Inductive step: Assume the lemma holds for all complete graphs on fewer than $n$ vertices. Consider $K_n$ with no rainbow triangle and $c \geq 3$ colors.

Pick a vertex $v$. Let $C_v$ be the set of colors on edges incident to $v$. 

Case 1: $|C_v| \leq 2$ for some vertex $v$. 

Let the colors incident to $v$ be (at most) $\{a, b\}$. Partition $V \setminus \{v\}$ into $A = \{u : vu \text{ has color } a\}$ and $B = \{u : vu \text{ has color } b\}$ (one of these could be empty if $|C_v| = 1$).

For any $x \in A, y \in B$: triangle $\{v, x, y\}$ has $vx$ color $a$, $vy$ color $b$, so $xy$ must be color $a$ or $b$.

For any $x, x' \in A$: triangle $\{v, x, x'\}$ has $vx, vx'$ both color $a$, so $xx'$ can be any color.

Similarly for $x, x' \in B$.

Now, the colors $\geq 3$ means there's a color $\gamma \notin \{a, b\}$ used somewhere. This color $\gamma$ can only appear on edges within $A$ or within $B$ (not on edges between $A$ and $B$, since those are colored $a$ or $b$, and not on edges incident to $v$).

So color $\gamma$ is confined to within $A$ or within $B$. If $\gamma$ appears only within $A$, then $\gamma$ doesn't touch vertices in $B \cup \{v\}$, so it's not spanning. Similarly if $\gamma$ appears only within $B$.

But wait, $\gamma$ could appear within both $A$ and $B$. In that case, $\gamma$ touches vertices in both $A$ and $B$ but has no edges between $A$ and $B$ (and no edges to $v$). So the $\gamma$-subgraph is disconnected (no $\gamma$-edge connects a vertex in $A$ to a vertex in $B$ or to $v$). So $\gamma$ is not connected and spanning.

Either way, $\gamma$ is not connected and spanning. Done.

Case 2: $|C_v| \geq 3$ for every vertex $v$.

Pick a vertex $v$ and three edges $vu, vw, vx$ of three different colors $a, b, c$ (where $c \notin \{a, b\}$). 

Triangle $\{v, u, w\}$: $vu$ color $a$, $vw$ color $b$, so $uw$ must be $a$ or $b$.
Triangle $\{v, u, x\}$: $vu$ color $a$, $vx$ color $c$, so $ux$ must be $a$ or $c$.
Triangle $\{v, w, x\}$: $vw$ color $b$, $vx$ color $c$, so $wx$ must be $b$ or $c$.

Now consider triangle $\{u, w, x\}$: $uw \in \{a, b\}$, $ux \in \{a, c\}$, $wx \in \{b, c\}$.

For no rainbow triangle, we need at least two of $\{uw, ux, wx\}$ to have the same color.

$uw \in \{a, b\}$, $ux \in \{a, c\}$, $wx \in \{b, c\}$.

If $uw = a$ and $ux = a$: two edges color $a$, OK.
If $uw = a$ and $ux = c$: colors are $a, c, wx$. Need $wx \in \{a, c\}$. But $wx \in \{b, c\}$. So $wx = c$. Colors: $a, c, c$. OK.
If $uw = b$ and $ux = a$: colors are $b, a, wx$. Need $wx \in \{a, b\}$. But $wx \in \{b, c\}$. So $wx = b$. Colors: $b, a, b$. OK.
If $uw = b$ and $ux = c$: colors are $b, c, wx$. Need $wx \in \{b, c\}$. $wx \in \{b, c\}$. So $wx = b$ or $wx = c$. Either works.

So in all cases, the triangle $\{u, w, x\}$ is not rainbow. Good, this is consistent.

But this doesn't immediately give me a contradiction. Let me think more.

Hmm, Case 2 is harder. Let me think about whether Case 2 can actually occur.

In Case 2, every vertex has edges of $\geq 3$ colors. Let me see if this leads to a rainbow triangle.

Pick vertex $v$ with edges $vu$ (color $a$), $vw$ (color $b$), $vx$ (color $c$), all distinct.

From above: $uw \in \{a,b\}$, $ux \in \{a,c\}$, $wx \in \{b,c\}$.

Subcase: $uw = a, ux = a, wx = b$ (say). Then:
- Triangle $\{u, w, x\}$: colors $a, a, b$. OK.

Now, vertex $u$ has edges of $\geq 3$ colors. $uv$ is color $a$, $uw$ is color $a$, $ux$ is color $a$. So $u$ needs edges of $\geq 2$ more colors to other vertices. There exists some vertex $y$ with $uy$ of color $d \neq a$.

Triangle $\{v, u, y\}$: $vu$ color $a$, $uy$ color $d$. So $vy \in \{a, d\}$.
Triangle $\{w, u, y\}$: $wu$ color $a$, $uy$ color $d$. So $wy \in \{a, d\}$.
Triangle $\{x, u, y\}$: $xu$ color $a$, $uy$ color $d$. So $xy \in \{a, d\}$.

Now, $vy \in \{a, d\}$. If $d \neq b$ and $d \neq c$:
  Triangle $\{v, w, y\}$: $vw$ color $b$, $vy \in \{a, d\}$, $wy \in \{a, d\}$.
    If $vy = a, wy = a$: colors $b, a, a$. OK.
    If $vy = a, wy = d$: colors $b, a, d$. Rainbow! ✗ (since $a, b, d$ distinct)
    If $vy = d, wy = a$: colors $b, d, a$. Rainbow! ✗
    If $vy = d, wy = d$: colors $b, d, d$. OK.
  
  So either ($vy = a, wy = a$) or ($vy = d, wy = d$).
  
  Triangle $\{v, x, y\}$: $vx$ color $c$, $vy \in \{a, d\}$, $xy \in \{a, d\}$.
    If $vy = a, xy = a$: colors $c, a, a$. OK.
    If $vy = a, xy = d$: colors $c, a, d$. Rainbow! ✗
    If $vy = d, xy = a$: colors $c, d, a$. Rainbow! ✗
    If $vy = d, xy = d$: colors $c, d, d$. OK.
  
  So either ($vy = a, xy = a$) or ($vy = d, xy = d$).

Combining with the constraint from $\{v, w, y\}$:
  Either ($vy = a, wy = a$) or ($vy = d, wy = d$).
  Either ($vy = a, xy = a$) or ($vy = d, xy = d$).

If $vy = a$: then $wy = a$ and $xy = a$.
If $vy = d$: then $wy = d$ and $xy = d$.

Subcase 2a: $vy = a, wy = a, xy = a$.
  Then $y$ has edges $yu = d, yv = a, yw = a, yx = a$. So far $y$ has colors $\{a, d\}$. For $y$ to have $\geq 3$ colors, there must be another vertex $z$ with $yz$ of color $e \neq a, d$.
  
  This could go on forever. The argument doesn't terminate easily.

Subcase 2b: $vy = d, wy = d, xy = d$.
  Then $y$ has edges $yu = d, yv = d, yw = d, yx = d$. All color $d$ so far. For $\geq 3$ colors, need another vertex with a different color edge to $y$.

This is getting very complicated. The direct approach seems difficult. Let me just use Gallai's theorem.

Let me look up the standard proof of Gallai's theorem to include it.

The standard proof of Gallai's theorem:

**Theorem (Gallai):** In any rainbow-triangle-free edge-coloring of $K_n$ ($n \geq 2$), there exists a non-trivial partition of $V(K_n)$ into non-empty parts $V_1, \ldots, V_k$ ($k \geq 2$) such that:
(i) at most 2 colors are used on edges between different parts, and
(ii) no color used between parts is used within any part.

**Proof:** By induction on $n$. For $n = 2$, the partition $\{v_1\}, \{v_2\}$ works (1 color between parts, no edges within parts).

For $n \geq 3$: If the coloring uses at most 2 colors, any non-trivial partition works (at most 2 colors between parts, and condition (ii) might not hold... hmm, actually condition (ii) says no inter-group color appears within a part. If we use 2 colors and both appear within a part, this fails.)

Hmm, actually the theorem as I stated it might not be exactly right. Let me reconsider.

The precise statement: A Gallai coloring has a "Gallai partition" where between parts, at most 2 colors are used, and for each pair of parts, all edges between them have the same color. Moreover, the colors used between parts are not used within parts.

Wait, I think the correct statement is:

**Gallai's Theorem:** A coloring of $K_n$ has no rainbow triangle if and only if there exists a non-trivial partition $\{V_1, \ldots, V_k\}$ ($k \geq 2$) such that:
- Between any two parts, all edges have the same color.
- At most 2 colors are used between parts in total.
- No color used between parts is used within any part.

Hmm, but the "between any two parts, all edges have the same color" is a stronger condition. Let me check: is this part of the theorem?

Actually, I think the standard Gallai partition has the property that between any two parts, all edges have the same color (this is called a "Gallai partition" or "Gallai's structural theorem"). And at most 2 colors are used between parts.

Let me look at this more carefully. The Gallai partition theorem:

**Theorem:** In every Gallai coloring of $K_n$, there is a non-trivial partition $\{V_1, \ldots, V_k\}$ of the vertices such that:
1. For each pair $i \neq j$, all edges between $V_i$ and $V_j$ have the same color.
2. At most 2 colors are used on edges between different parts.
3. The colors used between parts are not used within any part.

This is the standard form. The proof is by induction.

For the purpose of our problem, we need: if $c \geq 3$, then there's a non-trivial partition where at most 2 colors are inter-group, and these don't appear within parts. The remaining $\geq 1$ colors appear only within parts, hence can't be connected and spanning.

Let me prove the theorem (or at least the part we need) by induction.

**Proof of Gallai's theorem (sketch):**

By induction on $n$. Base case $n = 2$: partition into singletons, 1 color between parts, trivially satisfied.

Inductive step: Consider $K_n$ with a rainbow-triangle-free coloring.

If the coloring uses at most 2 colors, take any non-trivial partition. Between parts, at most 2 colors. But condition 3 might fail. Hmm.

Actually, if the coloring uses at most 2 colors, we can take the partition into singletons. Then between parts, at most 2 colors, and there are no edges within parts (singletons). So condition 3 is trivially satisfied. ✓

If the coloring uses $\geq 3$ colors:

Pick a vertex $v$. Let the colors on edges from $v$ be $C_v$. 

If $|C_v| \leq 2$ for some $v$: Let $C_v = \{a, b\}$ (or $\{a\}$). Partition $V \setminus \{v\}$ by the color of the edge to $v$: $A = \{u : c(vu) = a\}$, $B = \{u : c(vu) = b\}$. 

For $x \in A, y \in B$: triangle $\{v, x, y\}$ has $vx$ color $a$, $vy$ color $b$, so $xy \in \{a, b\}$.

For $x, x' \in A$: triangle $\{v, x, x'\}$ has $vx, vx'$ color $a$, so $xx'$ can be any color.

The partition $\{v\} \cup A \cup B$ (ignoring empty parts) has:
- Between $\{v\}$ and $A$: all color $a$.
- Between $\{v\}$ and $B$: all color $b$.
- Between $A$ and $B$: all edges are color $a$ or $b$ (but not necessarily all the same color).

Hmm, so condition 1 (all edges between two parts have the same color) is satisfied for $\{v\}-A$ and $\{v\}-B$, but not necessarily for $A-B$.

So the partition $\{v\}, A, B$ doesn't immediately give a Gallai partition. But we can refine.

For edges between $A$ and $B$: each is color $a$ or $b$. 

Now, within $A$: the coloring restricted to $A$ is rainbow-triangle-free (inherited). By induction, $A$ has a Gallai partition. Similarly for $B$.

But we need the inter-group colors to not appear within parts. The inter-group colors are $a$ and $b$. Within $A$, there might be edges of color $a$. So if we use the Gallai partition of $A$, the inter-group colors of that partition are different from $a$ and $b$ (by induction, the inter-group colors of the sub-partition don't appear within sub-parts, but $a$ could appear within $A$).

This is getting complicated. The full proof of Gallai's theorem is non-trivial. Let me just cite it.

For the competition proof, I'll state Gallai's theorem and use it. The theorem is well-known in combinatorics.

Actually, let me try a different, more self-contained approach. Instead of the full Gallai theorem, let me prove just what we need.

**What we need:** If $K_n$ is edge-colored with $\geq 3$ colors, no rainbow triangle, and every color is connected and spanning, then contradiction.

**Proof attempt (self-contained):**

Suppose $c \geq 3$ colors, all connected and spanning, no rainbow triangle.

Pick any edge $uv$ of color $\alpha$. Since color $\beta$ ($\beta \neq \alpha$) is connected and spanning, there's a $\beta$-path from $u$ to $v$. Let $P = u, w_1, w_2, \ldots, w_k, v$ be a shortest $\beta$-path from $u$ to $v$ (so $k \geq 1$ and all edges are $\beta$). Since $uv$ is $\alpha \neq \beta$, $k \geq 1$.

If $k = 1$: $P = u, w_1, v$ with $uw_1$ and $w_1 v$ both $\beta$. Triangle $\{u, v, w_1\}$: $uv$ is $\alpha$, $uw_1$ is $\beta$, $w_1 v$ is $\beta$. Two colors. OK. No contradiction yet.

Now, since color $\gamma$ ($\gamma \neq \alpha, \beta$) is connected and spanning, there's a $\gamma$-path from $u$ to $v$. Let $Q = u, z_1, \ldots, v$ be a shortest $\gamma$-path.

Triangle $\{u, v, z_1\}$: $uv$ is $\alpha$, $uz_1$ is $\gamma$. So $vz_1 \in \{\alpha, \gamma\}$.

Triangle $\{u, w_1, z_1\}$: $uw_1$ is $\beta$, $uz_1$ is $\gamma$. So $w_1 z_1 \in \{\beta, \gamma\}$.

Triangle $\{v, w_1, z_1\}$: $vw_1$ is $\beta$, $vz_1 \in \{\alpha, \gamma\}$, $w_1 z_1 \in \{\beta, \gamma\}$.

For no rainbow triangle: the three edges $vw_1 (\beta)$, $vz_1$, $w_1 z_1$ must not all be distinct.

$vw_1 = \beta$. So we need $vz_1 = \beta$ or $w_1 z_1 = \beta$ or $vz_1 = w_1 z_1$.

$vz_1 \in \{\alpha, \gamma\}$, so $vz_1 \neq \beta$. Thus we need $w_1 z_1 = \beta$ or $vz_1 = w_1 z_1$.

If $vz_1 = \alpha$: need $w_1 z_1 = \beta$ or $w_1 z_1 = \alpha$. But $w_1 z_1 \in \{\beta, \gamma\}$. So $w_1 z_1 = \beta$.
If $vz_1 = \gamma$: need $w_1 z_1 = \beta$ or $w_1 z_1 = \gamma$. Both are in $\{\beta, \gamma\}$. ✓

Case A: $vz_1 = \alpha, w_1 z_1 = \beta$.
  Triangle $\{u, v, z_1\}$: $\alpha, \gamma, \alpha$. OK.
  Triangle $\{u, w_1, z_1\}$: $\beta, \gamma, \beta$. OK.
  Triangle $\{v, w_1, z_1\}$: $\beta, \alpha, \beta$. OK.

Case B: $vz_1 = \gamma, w_1 z_1 = \beta$.
  Triangle $\{u, v, z_1\}$: $\alpha, \gamma, \gamma$. OK.
  Triangle $\{u, w_1, z_1\}$: $\beta, \gamma, \beta$. OK.
  Triangle $\{v, w_1, z_1\}$: $\beta, \gamma, \beta$. OK.

Case C: $vz_1 = \gamma, w_1 z_1 = \gamma$.
  Triangle $\{u, v, z_1\}$: $\alpha, \gamma, \gamma$. OK.
  Triangle $\{u, w_1, z_1\}$: $\beta, \gamma, \gamma$. OK.
  Triangle $\{v, w_1, z_1\}$: $\beta, \gamma, \gamma$. OK.

So in all cases, no rainbow triangle, and we don't get a contradiction. The direct approach of looking at a few vertices doesn't easily yield a contradiction.

This suggests that the structure is more global, and Gallai's theorem is really the right tool.

Let me just write the proof using Gallai's theorem. I'll state the theorem and give a brief proof sketch.

Actually, I just realized: maybe I should prove a weaker version that suffices. Here's what I need:

**Lemma:** In a rainbow-triangle-free coloring of $K_n$ with $c \geq 3$ colors, there exist two non-empty disjoint sets $A, B$ with $A \cup B = V$ such that the edges between $A$ and $B$ use at most 2 colors, and these colors do not appear on any edge within $A$ or within $B$.

This is weaker than the full Gallai theorem (which gives a partition into $k \geq 2$ parts with stronger properties). Let me try to prove this weaker version.

**Proof of Lemma:** By induction on $n$.

Base case $n = 2$: Only 1 edge, so $c \leq 1 < 3$. Vacuously true.

For $n \geq 3$: If $c \leq 2$, vacuously true (hypothesis $c \geq 3$ not met).

So assume $c \geq 3$. Pick a vertex $v$.

**Case 1:** $v$ has edges of at most 2 colors. Say colors $a, b$ (or just $a$).

Partition $V \setminus \{v\}$ into $A' = \{u : c(vu) = a\}$ and $B' = \{u : c(vu) = b\}$.

For $x \in A', y \in B'$: $c(xy) \in \{a, b\}$ (from triangle $\{v, x, y\}$).

Now, since $c \geq 3$, there's a color $\gamma \notin \{a, b\}$ used somewhere. This color appears on some edge, which must be within $A'$ or within $B'$ (not incident to $v$, and not between $A'$ and $B'$).

WLOG $\gamma$ appears within $A'$. 

Now I want to find a partition where inter-group colors don't appear within parts. 

Let me set $A = A'$ and $B = B' \cup \{v\}$. Edges between $A$ and $B$: 
- Between $A'$ and $\{v\}$: color $a$.
- Between $A'$ and $B'$: colors in $\{a, b\}$.

So inter-group colors are $\subseteq \{a, b\}$. 

Do $a$ or $b$ appear within $A = A'$? Possibly yes (edges within $A'$ could be color $a$ or $b$ or $\gamma$ or others). So condition (ii) might fail.

Hmm. So this simple partition doesn't work.

Let me try a different approach. Set $A = \{v\} \cup A'$ and $B = B'$. Wait, same issue.

Actually, the issue is that colors $a$ and $b$ might appear within $A'$ or $B'$. The Gallai theorem handles this by recursively partitioning $A'$ and $B'$.

Let me try the inductive approach more carefully.

Within $A'$, the coloring is rainbow-triangle-free. If $A'$ uses $\geq 3$ colors, by induction, $A'$ has a partition $A'_1, \ldots, A'_k$ with inter-group colors $\subseteq \{p, q\}$ not appearing within any $A'_i$. 

But the inter-group colors of the overall partition need to not appear within parts. The overall inter-group colors would be $a, b$ (from edges between $A'$ and $B' \cup \{v\}$). But $a$ might appear within $A'_i$.

This recursive approach is exactly the proof of Gallai's theorem, and it's quite involved. Let me just cite the theorem.

OK let me just write the proof citing Gallai's theorem. This is a standard result in combinatorics, well-known in competition circles.

Let me also handle Case 2 (every vertex has $\geq 3$ colors on incident edges) for completeness, though Gallai's theorem handles both cases.

Actually, I realize that for the proof, I just need to cite Gallai's theorem and apply it. Let me write the proof.

---

**Proof:**

We prove that $M = 1$ for $n = 3$ and $M = 2$ for $n \geq 4$.

**Upper bound.**

*Case $n = 3$:* $K_3$ has 3 edges. Each color class must be connected and spanning, so each uses at least $n - 1 = 2$ edges. With $c$ colors, we need $2c \leq 3$, so $c \leq 1$.

*Case $n \geq 4$:* We show $c \leq 2$. Suppose for contradiction that $c \geq 3$ and all color classes are connected and spanning, with no rainbow triangle.

By Gallai's theorem (see below), there exists a non-trivial partition of $V(K_n)$ into non-empty parts $V_1, \ldots, V_k$ ($k \geq 2$) such that:
1. At most 2 colors are used on edges between different parts.
2. No color used between parts appears on any edge within a part.

Since $c \geq 3$, at least one color $\gamma$ is not used between parts. By property 2, $\gamma$ does not appear within any part either—wait, that's not right. Property 2 says the inter-group colors don't appear within parts. It doesn't say non-inter-group colors don't appear within parts.

Let me re-read: "No color used between parts appears on any edge within a part." So if $\gamma$ is not used between parts, it could still appear within parts. And $\gamma$ appears only within parts (since it's not between parts). So $\gamma$'s edges are all within parts $V_1, \ldots, V_k$.

Since $k \geq 2$, $\gamma$ has no edges between $V_1$ and $V_2$. So the $\gamma$-colored subgraph has no edges connecting $V_1$ to $V_2$. If $\gamma$ appears in both $V_1$ and $V_2$, it's disconnected. If $\gamma$ appears in only one part, it doesn't span all vertices. Either way, $\gamma$ is not connected and spanning. Contradiction.

**Gallai's Theorem** (stated above): In any rainbow-triangle-free edge-coloring of $K_n$ ($n \geq 2$), there exists a non-trivial partition of the vertices into non-empty parts $V_1, \ldots, V_k$ ($k \geq 2$) such that at most 2 colors are used on edges between different parts, and no color used between parts is used on any edge within a part.

*Proof sketch of Gallai's theorem:* By induction on $n$. For $n = 2$, the partition into singletons works. For $n \geq 3$: if some vertex $v$ has incident edges of at most 2 colors $\{a, b\}$, partition $V \setminus \{v\}$ by the color of edges to $v$, then refine each part recursively (using the induction hypothesis on the subgraphs, noting that inter-group colors $a, b$ are excluded from within parts by the triangle condition). If every vertex has incident edges of $\geq 3$ colors, one can show that the partition into singletons satisfies the conditions (since with $\geq 3$ colors at every vertex and no rainbow triangle, the structure forces at most 2 colors globally—a contradiction, so this case reduces to the previous one). $\square$

Hmm, the proof sketch for Gallai's theorem is not quite right, especially the "every vertex has $\geq 3$ colors" case. Let me think about this more carefully.

Actually, in the case where every vertex has $\geq 3$ colors on incident edges, can we still find a non-trivial partition? 

Consider $K_4$ with a Gallai coloring using 3 colors. Is it possible that every vertex has $\geq 3$ colors on incident edges? Each vertex has 3 incident edges. If all 3 are different colors, then for any triangle containing that vertex, we'd need the other two edges to share a color. 

Vertex 1: edges 12 (a), 13 (b), 14 (c). Triangle 123: 12 (a), 13 (b), so 23 ∈ {a, b}. Triangle 124: 12 (a), 14 (c), so 24 ∈ {a, c}. Triangle 134: 13 (b), 14 (c), so 34 ∈ {b, c}.

Now triangle 234: 23 ∈ {a,b}, 24 ∈ {a,c}, 34 ∈ {b,c}. For no rainbow: need two equal.
- 23 = a, 24 = a: OK (234 has colors a, a, 34).
- 23 = a, 24 = c: colors a, c, 34. Need 34 ∈ {a, c}. But 34 ∈ {b, c}. So 34 = c. Colors a, c, c. OK.
- 23 = b, 24 = a: colors b, a, 34. Need 34 ∈ {a, b}. But 34 ∈ {b, c}. So 34 = b. Colors b, a, b. OK.
- 23 = b, 24 = c: colors b, c, 34. Need 34 ∈ {b, c}. 34 ∈ {b, c}. OK either way.

So it's possible. For example: 12=a, 13=b, 14=c, 23=a, 24=a, 34=c. Check: triangle 123: a, b, a ✓. Triangle 124: a, c, a ✓. Triangle 134: b, c, c ✓. Triangle 234: a, a, c ✓.

Now, vertex 2: edges 21 (a), 23 (a), 24 (a). Only 1 color! So vertex 2 doesn't have $\geq 3$ colors.

Let me try to make all vertices have $\geq 3$ colors. With $K_4$ and 3 colors, each vertex has 3 edges. For all 3 to be different colors at every vertex, we need a proper 3-edge-coloring of $K_4$. But $K_4$ has 6 edges and a proper 3-edge-coloring would have each color class being a perfect matching (2 edges). $K_4$ does have a proper 3-edge-coloring: {12, 34}, {13, 24}, {14, 23}. But this gives rainbow triangles! Triangle 123: 12 (color 1), 13 (color 2), 23 (color 3) — rainbow! So this doesn't work.

So for $K_4$ with no rainbow triangle, we can't have all vertices with $\geq 3$ colors. Good.

In general, for a Gallai coloring, it's known that there always exists a vertex with $\leq 2$ colors on incident edges (unless the whole coloring uses $\leq 2$ colors). This is because if every vertex has $\geq 3$ colors, one can find a rainbow triangle. 

Actually, this is a known result: in a Gallai coloring, there exists a vertex with at most 2 colors on its incident edges. This can be proved as follows:

**Claim:** In a Gallai coloring of $K_n$ with $\geq 3$ colors, there exists a vertex with $\leq 2$ colors on incident edges.

*Proof:* Suppose every vertex has $\geq 3$ colors on incident edges. Pick vertex $v$ with edges of colors $a, b, c$ to vertices $u, w, x$ respectively. As shown above, $uw \in \{a,b\}$, $ux \in \{a,c\}$, $wx \in \{b,c\}$, and triangle $uwx$ is not rainbow.

Now, vertex $u$ has $\geq 3$ colors. $uv$ is color $a$. If $uw$ and $ux$ are both color $a$, then $u$ needs $\geq 2$ more colors from other vertices. But actually, let me check: in the example above, we had $uw = a, ux = a$ is possible (with $wx$ being anything in $\{b,c\}$). Then $u$ has only color $a$ on edges to $v, w, x$, so $u$ needs $\geq 2$ more colors from other vertices (if $n \geq 5$).

This is getting complicated. Let me just cite Gallai's theorem without proof.

For the competition, I think citing Gallai's theorem is acceptable (it's a well-known result). But let me also include a proof for completeness, even if sketchy.

Actually, let me try a cleaner approach. Let me prove the following:

**Lemma:** In a rainbow-triangle-free coloring of $K_n$ with $c \geq 3$ colors, there exists a non-trivial partition $V = A \cup B$ (both non-empty) such that at most 2 colors appear on edges between $A$ and $B$, and these colors do not appear within $A$ or $B$.

**Proof:** We prove by induction on $n$ that such a partition exists.

*Base case:* $n = 2$. Only 1 edge, so $c \leq 1 < 3$. Vacuously true.

*Inductive step:* Assume true for all $K_m$ with $m < n$. Consider $K_n$ with $c \geq 3$ colors and no rainbow triangle.

**Subcase 1:** There exists a vertex $v$ with $\leq 2$ colors on incident edges.

Let the colors be $\{a, b\}$ (WLOG). Partition $V \setminus \{v\}$ into $A_0 = \{u : c(vu) = a\}$ and $B_0 = \{u : c(vu) = b\}$ (if only 1 color, one part is empty; handle separately).

For $x \in A_0, y \in B_0$: triangle $\{v, x, y\}$ gives $c(xy) \in \{a, b\}$.

Now, within $A_0$: the coloring is rainbow-triangle-free. If $|A_0| \geq 2$ and $A_0$ uses $\geq 3$ colors, by induction, $A_0$ has a partition $A_0 = P \cup Q$ with inter-group colors $\{p, q\}$ not appearing within $P$ or $Q$.

Similarly for $B_0$.

The key insight: colors $a$ and $b$ might appear within $A_0$ or $B_0$. We need to find a partition where $a$ and $b$ don't appear within parts.

Hmm, this is the crux of the difficulty. The recursive partitioning of $A_0$ gives inter-group colors $\{p, q\}$ that don't appear within sub-parts of $A_0$. But $a$ could appear within $A_0$.

I think the correct approach is:

Consider the partition $\{v\}, A_0, B_0$ (ignoring empty parts). The inter-group colors are:
- $\{v\}$-$A_0$: color $a$.
- $\{v\}$-$B_0$: color $b$.
- $A_0$-$B_0$: colors in $\{a, b\}$.

So inter-group colors $\subseteq \{a, b\}$. But $a$ and $b$ might appear within $A_0$ or $B_0$.

Now, recursively partition $A_0$ and $B_0$. The recursive partition of $A_0$ has inter-group colors that don't appear within sub-parts of $A_0$. But those inter-group colors are specific to $A_0$'s sub-structure.

The full Gallai partition is obtained by recursively partitioning each part until we reach a partition where inter-group colors don't appear within any part. The recursion terminates because the parts get smaller.

But the issue is: at each level of recursion, the inter-group colors of the sub-partition might not be the same as $a, b$. So the overall partition's inter-group colors are the union of inter-group colors at all levels, which could be more than 2.

Hmm, actually, the Gallai theorem says there exists a partition with at most 2 inter-group colors total. The recursive approach I described might give more than 2. So the proof is more subtle.

Let me think about this differently. 

The correct proof of Gallai's theorem uses the following approach:

1. Find a vertex $v$ with $\leq 2$ colors on incident edges (such a vertex always exists in a Gallai coloring with $\geq 3$ colors — this itself needs proof).

2. Partition based on $v$'s incident colors.

3. Show that the inter-group colors (at most 2) don't appear within parts, using the no-rainbow-triangle condition.

Wait, step 3: do $a$ and $b$ appear within $A_0$? 

For $x, x' \in A_0$: triangle $\{v, x, x'\}$ has $vx, vx'$ both color $a$. So $xx'$ can be any color, including $a$.

So yes, $a$ can appear within $A_0$. So the partition $\{v\}, A_0, B_0$ doesn't satisfy condition (ii).

Hmm, so the simple partition doesn't work. The Gallai theorem's proof must be more clever.

Let me look at this from a different angle. 

Actually, I think the correct statement of Gallai's theorem involves a partition where between parts, at most 2 colors are used, and these colors are not used within parts. The proof uses the concept of a "maximal" partition or a specific construction.

Let me try a different approach to the proof. 

**Alternative proof approach:** 

Consider a maximal proper subset $S \subset V$ (with $2 \leq |S| \leq n-1$) such that the set of colors on edges between $S$ and $V \setminus S$ is minimized. 

Actually, let me try yet another approach. Let me use the following:

**Claim:** In a Gallai coloring with $\geq 3$ colors, there exists a non-trivial partition where between parts, at most 2 colors are used and these don't appear within parts.

**Proof:** Consider a maximal set $S$ with $1 \leq |S| < n$ such that the edges between $S$ and $V \setminus S$ use at most 2 colors. Such a set exists: take $S = \{v\}$ for any vertex $v$; the edges from $v$ use at most... well, $v$ could have many colors. Hmm.

OK, I think I'm overcomplicating this. Let me just state Gallai's theorem as a known result and use it. In a competition, this is standard.

Let me also consider: maybe I can prove the result without Gallai's theorem, using a more direct argument.

**Direct proof that $c \leq 2$:**

Suppose $c \geq 3$, all colors connected and spanning, no rainbow triangle.

Consider the color graph: for each color, we have a connected spanning subgraph. 

Pick any edge $e = uv$ of color 1. Since color 2 is connected and spanning, there's a color-2 path from $u$ to $v$. Since color 3 is connected and spanning, there's a color-3 path from $u$ to $v$.

Let $P_2$ be a shortest color-2 path from $u$ to $v$, and $P_3$ be a shortest color-3 path from $u$ to $v$.

$P_2 = u, a_1, a_2, \ldots, a_s, v$ (all edges color 2, $s \geq 1$).
$P_3 = u, b_1, b_2, \ldots, b_t, v$ (all edges color 3, $t \geq 1$).

Consider the first vertices $a_1$ and $b_1$ on these paths.

Triangle $\{u, a_1, b_1\}$: $ua_1$ color 2, $ub_1$ color 3. So $a_1 b_1 \in \{2, 3\}$.

Triangle $\{v, a_1, b_1\}$: $va_1$ is on path $P_2$... wait, $a_1$ is the first vertex after $u$ on $P_2$, so $va_1$ is not necessarily on $P_2$. Let me reconsider.

If $s = 1$: $P_2 = u, a_1, v$ with $ua_1$ and $a_1 v$ both color 2.
If $s \geq 2$: $P_2 = u, a_1, \ldots, a_s, v$.

Let me consider the case $s = 1, t = 1$ first.

$P_2 = u, a, v$ (edges $ua, av$ color 2).
$P_3 = u, b, v$ (edges $ub, bv$ color 3).

Triangle $\{u, a, b\}$: $ua$ color 2, $ub$ color 3. So $ab \in \{2, 3\}$.
Triangle $\{v, a, b\}$: $va$ color 2, $vb$ color 3. So $ab \in \{2, 3\}$. (Same constraint.)

Triangle $\{u, v, a\}$: $uv$ color 1, $ua$ color 2, $va$ color 2. Colors 1, 2, 2. OK.
Triangle $\{u, v, b\}$: $uv$ color 1, $ub$ color 3, $vb$ color 3. Colors 1, 3, 3. OK.

Now, $ab \in \{2, 3\}$. 

Case 1: $ab$ is color 2. Triangle $\{u, a, b\}$: 2, 3, 2. OK. Triangle $\{v, a, b\}$: 2, 3, 2. OK.
Case 2: $ab$ is color 3. Triangle $\{u, a, b\}$: 2, 3, 3. OK. Triangle $\{v, a, b\}$: 2, 3, 3. OK.

No contradiction yet. We have 4 vertices $u, v, a, b$ and the coloring so far is consistent.

Now, color 1 is connected and spanning. The only color-1 edge we know is $uv$. For color 1 to be connected, there must be color-1 edges connecting $a$ and $b$ to the rest. 

Specifically, $a$ must be connected to the color-1 subgraph. Since $a$'s edges to $u, v, b$ are colors 2, 2, and $\{2,3\}$ respectively, $a$ has no color-1 edge to $u, v, b$. So $a$ must have a color-1 edge to some other vertex $w$.

Similarly, $b$ must have a color-1 edge to some vertex (possibly $w$ or another).

If $n = 4$ (vertices $u, v, a, b$ only), then $a$ has no color-1 edge to any vertex, so color 1 is not connected (it only has edge $uv$, and $a, b$ are isolated in color 1). Contradiction!

So for $n = 4$, $c \geq 3$ is impossible. This confirms $M(4) = 2$.

For $n \geq 5$, we need to continue the argument. There exists a vertex $w$ with $aw$ color 1.

Triangle $\{u, a, w\}$: $ua$ color 2, $aw$ color 1. So $uw \in \{1, 2\}$.
Triangle $\{v, a, w\}$: $va$ color 2, $aw$ color 1. So $vw \in \{1, 2\}$.
Triangle $\{b, a, w\}$: $ba \in \{2, 3\}$, $aw$ color 1. So $bw \in \{1, ba\}$.
  If $ba = 2$: $bw \in \{1, 2\}$.
  If $ba = 3$: $bw \in \{1, 3\}$.

Also, triangle $\{u, v, w\}$: $uv$ color 1, $uw \in \{1, 2\}$, $vw \in \{1, 2\}$. For no rainbow: need two of $\{1, uw, vw\}$ equal. Since $uv = 1$: if $uw = 1$ or $vw = 1$, OK. If $uw = 2, vw = 2$: colors 1, 2, 2, OK. So no additional constraint.

This is getting very involved. The argument would need to track many cases and eventually reach a contradiction for all $n$. This is essentially reproving Gallai's theorem in a specific context.

I think the cleanest approach is to cite Gallai's theorem. Let me write the proof that way.

Actually, let me try to prove just the key claim directly:

**Key Claim:** In a rainbow-triangle-free coloring of $K_n$ with $c \geq 3$ colors, not all colors can be connected and spanning.

**Proof:** We prove by induction on $n$.

Base case $n = 3$: $K_3$ has 3 edges. With $c \geq 3$, each edge has a distinct color, forming a rainbow triangle. Contradiction. So $c \leq 2$ and the claim is vacuously true.

Inductive step: Assume the claim for all $K_m$ with $3 \leq m < n$. Consider $K_n$ with $c \geq 3$ colors, no rainbow triangle, and suppose all colors are connected and spanning.

**Step 1:** There exists a vertex $v$ with $\leq 2$ colors on incident edges.

*Proof of Step 1:* Suppose every vertex has $\geq 3$ colors on incident edges. Pick vertex $v$ and three neighbors $u, w, x$ with $c(vu) = a, c(vw) = b, c(vx) = c$ (distinct). As before, $uw \in \{a,b\}, ux \in \{a,c\}, wx \in \{b,c\}$.

Now, vertex $u$ has $\geq 3$ colors on incident edges. $c(uv) = a$. 

If $c(uw) = a$ and $c(ux) = a$: then $u$ has only color $a$ on edges to $v, w, x$. For $\geq 3$ colors, $u$ needs $\geq 2$ more colors on edges to other vertices (so $n \geq 5$). 

If $c(uw) = b$ or $c(ux) = c$ (or both): then $u$ has $\geq 2$ colors on edges to $\{v, w, x\}$. For $\geq 3$ colors, $u$ needs $\geq 1$ more color on edges to other vertices (so $n \geq 5$, unless $u$ already has 3 colors from $\{v, w, x\}$).

If $c(uw) = b, c(ux) = c$: $u$ has colors $a, b, c$ on edges to $v, w, x$. So $u$ has $\geq 3$ colors. ✓ (No need for more vertices.)

In this subcase, $c(uw) = b, c(ux) = c$. Then triangle $uwx$: $uw = b, ux = c, wx \in \{b, c\}$. For no rainbow: $wx = b$ or $wx = c$. ✓

Now, $w$ has $c(wv) = b, c(wu) = b$. So $w$ has color $b$ on edges to $v, u$. $c(wx) \in \{b, c\}$. If $c(wx) = b$: $w$ has only color $b$ on edges to $u, v, x$. Needs $\geq 2$ more colors, so $n \geq 5$. If $c(wx) = c$: $w$ has colors $b, c$ on edges to $u, v, x$. Needs $\geq 1$ more color, so $n \geq 5$ (or $w$ has exactly 2 colors, contradicting $\geq 3$).

Wait, if $c(wx) = c$ and $n = 4$ (only vertices $v, u, w, x$): $w$ has edges $wv (b), wu (b), wx (c)$. Only 2 colors. Contradiction with $\geq 3$.

So for $n = 4$, we can't have all vertices with $\geq 3$ colors. So Step 1 holds for $n = 4$.

For $n \geq 5$, the argument continues but gets complicated. Let me try to prove Step 1 for general $n$.

*Proof of Step 1 (general):* Suppose every vertex has $\geq 3$ colors on incident edges. We'll derive a contradiction by finding a rainbow triangle.

Pick vertex $v$ with edges of colors $a, b, c$ to $u, w, x$. As established: $uw \in \{a,b\}, ux \in \{a,c\}, wx \in \{b,c\}$.

Subcase A: $uw = a, ux = a$. Then $u$ has color $a$ on edges to $v, w, x$. Since $u$ has $\geq 3$ colors, there exist vertices $y, z$ (possibly same) with $c(uy) = d \neq a, c(uz) = e \neq a, d$ (with $d, e$ distinct from each other and from $a$; or $d \neq a$ and $e \neq a, d$).

Actually, $u$ has $\geq 3$ colors, and only color $a$ on edges to $\{v, w, x\}$. So $u$ has $\geq 2$ other colors on edges to $V \setminus \{v, w, x, u\}$. This requires $|V \setminus \{v, w, x, u\}| \geq 1$, i.e., $n \geq 5$.

Let $y$ be a vertex with $c(uy) = d \neq a$.

Triangle $\{v, u, y\}$: $vu = a, uy = d$. So $vy \in \{a, d\}$.
Triangle $\{w, u, y\}$: $wu = a, uy = d$. So $wy \in \{a, d\}$.
Triangle $\{x, u, y\}$: $xu = a, uy = d$. So $xy \in \{a, d\}$.

Now, $vy \in \{a, d\}$.

Triangle $\{v, w, y\}$: $vw = b, vy \in \{a, d\}, wy \in \{a, d\}$.
  If $d \neq b$: for no rainbow, need two of $\{b, vy, wy\}$ equal.
    $b \neq a$ and $b \neq d$ (since $d \neq a$ and $d$ could equal $b$ or not). Wait, I said $d \neq a$, but $d$ could be $b$ or $c$ or a new color.
    
    If $d = b$: $vy \in \{a, b\}, wy \in \{a, b\}$. Triangle $\{v, w, y\}$: $b, vy, wy$. Need two equal. $vw = b$. If $vy = b$ or $wy = b$: OK. If $vy = a, wy = a$: colors $b, a, a$. OK. All fine.
    
    If $d = c$: $vy \in \{a, c\}, wy \in \{a, c\}$. Triangle $\{v, w, y\}$: $b, vy, wy$. Need two equal. $b \neq a, b \neq c$. So need $vy = wy$. Both in $\{a, c\}$. So $vy = wy = a$ or $vy = wy = c$.
    
    If $d \notin \{a, b, c\}$: $vy \in \{a, d\}, wy \in \{a, d\}$. Triangle $\{v, w, y\}$: $b, vy, wy$. $b \neq a, b \neq d$. Need $vy = wy$. So $vy = wy = a$ or $vy = wy = d$.
    
  Triangle $\{v, x, y\}$: $vx = c, vy \in \{a, d\}, xy \in \{a, d\}$.
    If $d \neq c$: need $vy = xy$ (since $c \neq a, c \neq d$). So $vy = xy = a$ or $vy = xy = d$.
    If $d = c$: $vy \in \{a, c\}, xy \in \{a, c\}$. Need two of $\{c, vy, xy\}$ equal. $vx = c$. If $vy = c$ or $xy = c$: OK. If $vy = a, xy = a$: OK. All fine.

This is getting extremely complicated with many cases. I don't think a direct proof is feasible without essentially proving Gallai's theorem.

Let me just cite Gallai's theorem and write the proof. I'll include a proof of Gallai's theorem as well, even if it's a sketch.

Actually, let me look for a cleaner proof of Gallai's theorem. 

Here's a clean proof I recall:

**Gallai's Theorem:** In any rainbow-triangle-free coloring of $K_n$ ($n \geq 2$), there exists a non-trivial partition $\{V_1, \ldots, V_k\}$ ($k \geq 2$) such that:
1. For each pair $i \neq j$, all edges between $V_i$ and $V_j$ have the same color.
2. At most 2 colors are used between parts.
3. No inter-group color appears within any part.

**Proof:** By induction on $n$. 

Base case $n = 2$: Partition $\{\{v_1\}, \{v_2\}\}$. One color between parts, no edges within parts. ✓

Inductive step: Assume for all $K_m$ with $2 \leq m < n$.

If the coloring uses $\leq 2$ colors: Partition into singletons. Between parts, $\leq 2$ colors. No edges within singletons. ✓

If the coloring uses $\geq 3$ colors:

**Claim:** There exists a vertex $v$ with $\leq 2$ colors on incident edges.

*Proof of Claim:* Suppose every vertex has $\geq 3$ colors. Pick $v$ with edges $vu (a), vw (b), vx (c)$, distinct. Then $uw \in \{a,b\}, ux \in \{a,c\}, wx \in \{b,c\}$.

Since $u$ has $\geq 3$ colors and $c(uv) = a$:
- If $c(uw) = a$ and $c(ux) = a$: $u$ needs $\geq 2$ more colors from other vertices.
- If $c(uw) = b$ or $c(ux) = c$: $u$ has $\geq 2$ colors from $\{v,w,x\}$, needs $\geq 1$ more.
- If $c(uw) = b, c(ux) = c$: $u$ has 3 colors from $\{v,w,x\}$.

In the last subcase ($c(uw) = b, c(ux) = c$): Triangle $uwx$ has $uw = b, ux = c, wx \in \{b,c\}$. OK.

Now $w$ has $c(wv) = b, c(wu) = b$. So $w$ has only color $b$ on edges to $u, v$. $c(wx) \in \{b, c\}$.
- If $c(wx) = b$: $w$ has only color $b$ on edges to $u, v, x$. Needs $\geq 2$ more colors.
- If $c(wx) = c$: $w$ has colors $b, c$ on edges to $u, v, x$. Needs $\geq 1$ more color.

If $n = 4$ (only $u, v, w, x$): $w$ has at most 2 colors. Contradiction. So $n \geq 5$.

For $n \geq 5$, $w$ has a neighbor $y \notin \{u, v, x\}$ with $c(wy) = d \notin \{b, c(wx)\}$ (or just $d \neq b$ if $c(wx) = b$).

Hmm, this is still complicated. Let me try a different approach to prove the claim.

*Alternative proof of Claim:* Consider a vertex $v$ that minimizes the number of colors on incident edges. Suppose for contradiction that $v$ has $\geq 3$ colors: $c(vu) = a, c(vw) = b, c(vx) = c$.

As before, $uw \in \{a,b\}, ux \in \{a,c\}, wx \in \{b,c\}$.

Consider vertex $u$. Its incident edges include $uv (a), uw (\in \{a,b\}), ux (\in \{a,c\})$.

If $uw = a, ux = a$: $u$ has only color $a$ on edges to $v, w, x$. By minimality, $u$ has $\geq 3$ colors (same as $v$), so $u$ has $\geq 2$ other colors on edges to other vertices. But also, $u$ has $\leq$ the number of colors $v$ has (by minimality of $v$). Hmm, this doesn't directly help.

Actually, I think the claim that there exists a vertex with $\leq 2$ colors is not trivial and is essentially part of Gallai's theorem. Let me just cite the full theorem.

OK, I'll write the proof citing Gallai's theorem. For the competition, this should be fine. Let me also include a brief proof of Gallai's theorem for completeness, even if not fully rigorous.

Actually, I just found a cleaner approach. Let me prove the result using the following lemma, which I can prove directly:

**Lemma:** In a rainbow-triangle-free coloring of $K_n$ with $c \geq 3$ colors, there exist two non-empty disjoint sets $A, B$ with $A \cup B = V$ such that at most 2 colors appear on edges between $A$ and $B$, and these colors do not appear on edges within $A$ or within $B$.

**Proof of Lemma:** We use induction on $n$. For $n = 2$, trivial (only 1 edge, $c \leq 1$).

For $n \geq 3$: If $c \leq 2$, take $A = \{v_1\}, B = V \setminus \{v_1\}$. Between $A$ and $B$, at most 2 colors (since $c \leq 2$). Within $A$: no edges. Within $B$: might have colors $a, b$. But the inter-group colors are all colors (at most 2), which might appear within $B$. So condition (ii) fails.

Hmm, so for $c \leq 2$, the lemma as stated might not hold. But we only need the lemma for $c \geq 3$.

For $c \geq 3$: 

Pick a vertex $v$ with the minimum number of colors on incident edges. Let $C_v$ be the set of colors on edges from $v$.

**Subcase 1:** $|C_v| \leq 2$. Let $C_v = \{a, b\}$ (or $\{a\}$).

Partition $V \setminus \{v\}$ into $A_0 = \{u : c(vu) = a\}$ and $B_0 = \{u : c(vu) = b\}$.

For $x \in A_0, y \in B_0$: $c(xy) \in \{a, b\}$ (from triangle $\{v, x, y\}$).

Now, since $c \geq 3$, there's a color $\gamma \notin \{a, b\}$ used somewhere. It must be used within $A_0$ or $B_0$ (not on edges incident to $v$, not between $A_0$ and $B_0$).

WLOG $\gamma$ is used within $A_0$ (so $|A_0| \geq 2$).

Now, within $A_0$, the coloring is rainbow-triangle-free. The colors used within $A_0$ include $\gamma$ and possibly $a, b$, and others.

By induction (since $|A_0| < n$), if $A_0$ uses $\geq 3$ colors, there's a partition $A_0 = P \cup Q$ with inter-group colors $\{p, q\}$ not appearing within $P$ or $Q$.

Now, consider the partition of $V$ into $P, Q, B_0 \cup \{v\}$ (or some refinement). The inter-group colors would be:
- $P$-$Q$: $\{p, q\}$.
- $P$-$(B_0 \cup \{v\})$: colors on edges from $P$ to $B_0$ (which are in $\{a, b\}$) and from $P$ to $v$ (color $a$). So $\subseteq \{a, b\}$.
- $Q$-$(B_0 \cup \{v\})$: similarly $\subseteq \{a, b\}$.

Total inter-group colors: $\{p, q\} \cup \{a, b\}$. This could be up to 4 colors. Too many.

So this approach doesn't directly work. The issue is that the recursive partitioning introduces new inter-group colors.

I think the correct proof of Gallai's theorem is more subtle and uses the fact that the inter-group colors at each level are disjoint from colors within parts, and a clever merging argument. Let me try to find the right approach.

Actually, I think the key insight is:

When we partition based on vertex $v$'s colors $\{a, b\}$, the colors $a$ and $b$ might appear within $A_0$ and $B_0$. But we can further partition $A_0$ and $B_0$ recursively. The recursive partition of $A_0$ has inter-group colors that don't appear within sub-parts of $A_0$. If $a$ appears within $A_0$, then $a$ is not an inter-group color of $A_0$'s sub-partition (since inter-group colors don't appear within sub-parts, and $a$ appears within $A_0$, so $a$ is within some sub-part).

Wait, that's not right either. $a$ could be an inter-group color of $A_0$'s sub-partition if $a$ doesn't appear within the sub-parts. But $a$ appears within $A_0$ (by assumption), so $a$ appears within some sub
