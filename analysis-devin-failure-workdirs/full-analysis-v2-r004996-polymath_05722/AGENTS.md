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
  <problem_id>polymath_05722</problem_id>
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

11.9. In the company, there are 100 children, some of whom are friends (friendship is always mutual). It is known that by selecting any child, the remaining 99 children can be divided into 33 groups of three such that in each group, all three are pairwise friends. Find the minimum possible number of pairs of friends.

(S. Berlov, N. Vlasova)

## Standard Solution

Answer: 198.

Solution: Let's translate the problem into the language of graphs, associating each child with a vertex and each friendship with an edge. Then we know that in this graph with 100 vertices, after removing any vertex, the remaining vertices can be divided into 33 triples such that the vertices in each triple are pairwise connected. We need to find the minimum possible number of edges in such a graph.

First, let's construct an example with exactly 198 edges. Divide 99 vertices, except for vertex $A$, into 33 groups of 3 vertices each. Connect the vertices pairwise within each triple; finally, connect $A$ to all other vertices. Then the conditions of the problem are satisfied: if $A$ is removed, the division into triples is already given, and if any other vertex $B$ is removed, in this division, it is sufficient to replace $B$ with $A$. In this described graph, there are a total of $33 \cdot 3 + 99 = 198$ edges.

It remains to prove that this number is the smallest.
We will call a graph on $3k+1$ vertices good if, after removing any vertex, the remaining $3k$ vertices can be divided into $k$ triples that are pairwise connected. We will prove by induction on $k$ that in a good graph on $3k+1$ vertices, there are at least $6k$ edges; for $k=33$, we will get the required estimate. The base case for $k=1$ is simple: since after removing any vertex, the remaining three are pairwise connected, any two vertices must be connected, so the number of edges is $C_{4}^{2}=6$.

Let's prove the inductive step. If from each vertex at least 4 edges come out, the total number of edges is not less than $(3k+1) \cdot 4 / 2 = 2(3k+1)$, which is even more than the required $6k$. Otherwise, there is a vertex $A$ connected to no more than three other vertices. If any vertex other than $A$ is removed, $A$ will end up in some triple, which means it is connected to at least two vertices. If one of these vertices is removed, $A$ will still have at least two adjacent vertices, so there were at least three. Thus, $A$ is connected to exactly three vertices $B, C$, and $D$. Then, when, for example, $B$ is removed, the vertices $A, C$, and $D$ form a triple, so $C$ and $D$ are connected; similarly, we get that $B$, $C$, and $D$ are pairwise connected.

Now, let's remove from our graph the vertices $A, B, C$, and $D$, and add one vertex $X$ connected to all those with whom at least one of the vertices $B, C$, and $D$ was connected. Note that in this case, the number of edges decreases by at least 6 (i.e., by the number of edges between $A, B, C$, and $D$). We will show that the resulting new graph is good; from this, the inductive step will follow, and then in the new graph, there will be at least $6(k-1)$ edges, which means in the original graph, there are at least $6(k-1) + 6 = 6k$ edges.

Suppose some vertex $Y \neq X$ is removed from the new graph. If it is removed from the original graph, the remaining vertices will be divided into triples; let's say, for definiteness, that vertex $A$ ends up in a triple with $B$ and $C$, and vertex $D$ in another triple. Then the new graph can be divided in the same way, placing vertex $X$ in the triple where vertex $D$ was. Finally, if vertex $X$ is removed from the new graph, the same operation can be performed, considering that vertex $D$ is removed from the original graph (then $A, B$, and $C$ will automatically end up in one triple). Thus, the inductive step is proven.

Remark. The provided example is not the only one. The reasoning in the second part of the solution essentially shows that many different optimal examples can be constructed in the following inductive manner. For $k=1$, take 4 vertices and connect all pairs with edges. When transitioning from $k$ to $k+1$, add three vertices $B, C, D$, connect them pairwise with each other, and also connect them all to some already existing vertex $A$.

In such an example, there will always be $6k$ edges, and it will satisfy the conditions of the problem.

Comment. Only the correct answer - 0 points.

Only an example with 198 pairs of friends is provided - 1 point.

Examples with more pairs of friends are not evaluated.

Only the proof that the number of pairs of friends is not less than $198-6$ points.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have 100 children, friendship is mutual. For any child selected, the remaining 99 can be divided into 33 groups of 3, each group being a triangle (pairwise friends). Find minimum number of friend pairs.

Let me think about this carefully.

First, let me understand the condition. For every vertex v, the graph G - v has a perfect triangle-tiling (partition into 33 triangles). This is called "vertex-pan-triangulable" or something similar.

We want to minimize the number of edges.

Let me think about lower bounds and constructions.

The condition: for every vertex v, G - v can be partitioned into triangles.

This is a strong condition. Let me think about what it implies.

First, consider the degree of each vertex. If we remove vertex v, the remaining 99 vertices partition into 33 triangles, so each triangle uses 3 edges. That's 99 edges within those triangles. But these are edges of G not incident to v.

Actually, let me think about it differently. For each vertex v, there's a triangle decomposition of G - v. 

Let me think about a construction. 

Construction idea: Take 4 groups of 25? No, 100 = 4*25. Hmm.

Let me think about the complete graph K_100. That certainly works but has too many edges.

Let me think about smaller cases first to get intuition.

What if we think about it as: the graph is such that removing any vertex leaves a graph with a triangle factor (perfect K_3-tiling).

A graph where every vertex-deleted subgraph has a perfect K_3-factor.

Let me think about the structure. 

One natural construction: partition 100 vertices into groups where within groups everyone is friends, and the triangle factor works out.

If we have a complete tripartite-like structure... Let me think.

Actually, let's think about it. 99 = 33*3. 

Construction 1: Take 3 groups A, B, C of size 33, 33, 34. Make complete tripartite? No wait, we need triangles which need all three pairwise friends, so tripartite gives no triangles.

Let me think again. Triangles need 3 mutually adjacent vertices.

Construction idea: Complete graph on groups. Suppose we partition into groups and make each group a clique, plus some cross edges.

If we make the whole thing a disjoint union of cliques... For removing any vertex to be triangle-factorable, we need each component (after removal) to be triangle-factorable.

If we have a clique of size n, removing one vertex gives clique of size n-1, which is triangle-factorable iff n-1 ≡ 0 mod 3, i.e., n ≡ 1 mod 3.

So disjoint union of cliques each of size ≡ 1 mod 3. 100 = 1 mod 3? 100 = 99+1 = 33*3+1, so 100 ≡ 1 mod 3. So we could have one clique of size 100 (K_100), but that's too many edges. Or we could partition 100 into parts each ≡ 1 mod 3: e.g., 100 = 1+1+...+1 (100 ones) — but a clique of size 1 has 0 edges and removing the vertex leaves 0, which is trivially factorable (empty). But wait, if we have 100 isolated vertices, removing any one leaves 99 isolated vertices, which cannot be partitioned into triangles (no edges). So that fails.

Wait, I need to be careful. The clique of size n: removing a vertex gives K_{n-1}, triangle-factorable iff (n-1) divisible by 3. For n=1, removing gives K_0, trivially factorable. But the issue is the OTHER vertices: when we remove a vertex from a different clique, this clique of size 1 remains as a single vertex, which can't be part of a triangle.

So disjoint union of cliques: when we remove a vertex from clique i, all other cliques must be triangle-factorable on their own (since no cross edges). So every clique except possibly the one we removed from must have size divisible by 3. And the one we removed from must have size ≡ 1 mod 3.

Since this must hold for removing a vertex from ANY clique, every clique must have size ≡ 1 mod 3, AND every other clique must have size ≡ 0 mod 3. Contradiction unless there's only one clique, or... wait.

If there are two cliques of sizes a, b with a+b=100. Remove from clique 1: clique 1 becomes a-1 (need a-1 ≡ 0 mod 3, so a ≡ 1), clique 2 stays b (need b ≡ 0 mod 3). Remove from clique 2: clique 2 becomes b-1 (need b ≡ 1 mod 3), clique 1 stays a (need a ≡ 0 mod 3). So a ≡ 1 and a ≡ 0, contradiction. So two cliques don't work.

So disjoint union of cliques only works with a single clique = K_100. Too many edges.

So we need cross edges to make it work with fewer edges.

Let me think differently. 

Let me think about the problem more carefully. This is a competition problem (Berlov, Vlasova), likely from a Russian olympiad. The answer is probably a specific number.

Let me think about lower bounds.

For each vertex v, G - v has a triangle factor with 33 triangles = 99 edges. These 99 edges are all in G and none incident to v. 

Consider summing over all v. Each edge e = {a,b} is counted in how many of these triangle factors? An edge {a,b} is not incident to v iff v ≠ a, b. So edge {a,b} appears in the triangle factor of G-v for v ∉ {a,b}, i.e., for 98 choices of v. But it doesn't appear in ALL of them—only in those where the particular triangle factor chosen includes {a,b}. We get to choose the triangle factor for each v, so this double-counting argument needs care.

Hmm, but we can choose the triangle factors. Let me think about it as: we need to select, for each v, a triangle factor T_v of G-v. Then count total edges used.

Actually, let's think about a cleaner lower bound.

Claim: every vertex has degree at least some value.

If vertex v has degree d, then when we remove some other vertex u, v must be in a triangle in G-u. So v needs at least 2 neighbors that are adjacent to each other and neither is u, for every u ≠ v. 

Actually, v must be in a triangle in G - u for every u ≠ v. So for every u ≠ v, v has two neighbors a, b (both ≠ u) with a-b edge. 

This means: v's neighborhood N(v) must be such that for every u ≠ v, N(v) \ {u} contains an edge. I.e., N(v) minus any single vertex still contains an edge. 

If |N(v)| = d, then N(v) \ {u} contains an edge for all u. The worst case is u ∈ N(v). So N(v) minus any one of its members still has an edge. This means N(v) is not a star-free... it means the graph induced on N(v) has the property that removing any single vertex leaves at least one edge. 

If N(v) induces a graph with matching number... Actually, the condition is: the induced graph on N(v) has no vertex whose removal makes it edge-free. I.e., no vertex in N(v) is "essential" for all edges. Equivalently, the edge cover... hmm, simpler: the induced graph on N(v) has at least 2 edges that don't share a common endpoint? No.

Actually: removing any single vertex from N(v) leaves at least one edge. This fails iff there's a vertex w in N(v) such that all edges in N(v) are incident to w, i.e., N(v) induces a star centered at w (plus isolated vertices). So the condition is: N(v) does NOT induce a star (a graph where all edges share a common vertex). 

Equivalently, the induced graph on N(v) has at least two edges that are vertex-disjoint, OR... no. A star K_{1,k} has all edges through center. If we remove center, no edges. So condition: induced graph on N(v) is not a star (including not a single edge, which is K_{1,1}, a star). Wait, single edge: removing either endpoint leaves no edge. So single edge is bad. So N(v) must induce a graph where removing any vertex leaves an edge. 

Minimum such: a triangle (3 vertices, 3 edges) works—remove any vertex, left with an edge. Or two disjoint edges (4 vertices)—remove any vertex, left with at least one edge. Or a path of length 2 (3 vertices, 2 edges)—remove middle, no edge left. So P_3 doesn't work. 

So minimum |N(v)| such that N(v) induces a graph that's not a star: 
- 3 vertices forming a triangle: works, d ≥ 3.
- 4 vertices with two disjoint edges: works, d ≥ 4.
- 3 vertices with 2 edges (P_3): doesn't work.
- Can we do d=3 with a triangle? Yes.

But wait, we also need: for u ∉ N(v) (u not a neighbor of v, u ≠ v), removing u from N(v) (which doesn't contain u) leaves N(v) unchanged, which must contain an edge. And for u ∈ N(v), removing u from N(v) must leave an edge. So overall: N(v) minus any vertex (in N(v)) still has an edge, and N(v) itself has an edge. Combined: N(v) induces a graph that is not a star.

So minimum degree: d(v) ≥ 3 (with N(v) being a triangle). But actually we need more because v must be in a triangle in G-u, and that triangle's other two vertices must also be adjacent. So v, a, b form a triangle, meaning a, b ∈ N(v) and a-b edge, AND v-a, v-b edges (given since a,b ∈ N(v)). So yes, N(v) must contain an edge, and that's the triangle v-a-b. Good.

But this is just for v being IN a triangle. The condition is stronger: ALL 99 vertices in G-u must be covered by triangles. So it's not just about v being in one triangle.

Let me think about the global structure more.

Lower bound approach: Let's count edges. For each vertex v, there's a triangle factor of G-v using 99 edges. 

Let me think about what structures achieve few edges.

Alternative construction idea: Think of 100 = 33·3 + 1. 

Consider the following: Take a "blow-up" type construction. 

Idea: Partition vertices into 34 groups: 33 groups of 3 and 1 group of 1. Make each group of 3 a triangle. The single vertex connects to... hmm.

If we remove the single vertex, the 33 triangles tile perfectly. Good. But if we remove a vertex from one of the triangles, that triangle becomes an edge (2 vertices), and the single vertex is alone. We need to reform: the 2 leftover vertices + single vertex must form a triangle, so they need to all be mutually adjacent. So the single vertex must be adjacent to all vertices in all triangles, and within each triangle's leftover pair they're already adjacent. But also the single vertex must be adjacent to both. And we need the single vertex + 2 leftover to form a triangle. 

So: single vertex s adjacent to everyone. Each group of 3 is a triangle. When we remove a vertex from group i, the remaining 2 from group i pair up with s to form a triangle. The other 32 groups remain as triangles. 

Edges: 33 triangles = 33·3 = 99 edges, plus s connected to all 99 others = 99 edges. Total = 198.

But can we do better? 

Let me check the condition more carefully. When we remove vertex v from group i (a triangle a,b,c, remove a), remaining b,c. We pair b,c with s: need s-b, s-c, b-c edges. b-c is in the triangle, s-b, s-c are the universal edges. Good, forms triangle. Other groups unchanged. 

When we remove s: 33 triangles tile perfectly. Good.

So 198 edges works. Can we do fewer?

Now, the single vertex s has degree 99. That's a lot. Can we reduce?

Alternative: instead of one universal vertex, use a more balanced structure.

Let me think about a different construction. What if we have a "cycle" of groups?

Consider 34 groups, but arranged so that when we remove a vertex from group i, the leftover 2 vertices go to group i+1 or something. This gets complicated.

Let me think about lower bounds more seriously.

Lower bound: Each vertex v, when removed, the remaining has a triangle factor. Consider the degree of v. 

Actually, let me think about it from the perspective of: for each vertex v, v must be in a triangle in G - u for every u ≠ v. As established, N(v) induces a graph that's not a star. So d(v) ≥ 3.

But more importantly, let's think about vertices with small degree.

Let me try to find the answer. Let me think about whether 198 is optimal or if we can do better.

Alternative construction: "Friendship-type" or using a more efficient structure.

Let me think about a construction with fewer edges. 

Consider: 4 groups A, B, C, D. Hmm, 100 = 4·25. 

Let me think about the problem differently. Let me consider the complement. In the complement graph H, an edge means "not friends." The condition is: for every vertex v, G-v has a triangle factor. In terms of H: for every v, the non-edges of G among V\{v} don't prevent a triangle factor. This is hard to express in complement.

Let me think about the problem as a matching/tiling problem.

Another construction idea: 

Take 100 vertices. Arrange them in a "cyclic" structure. Label 0, 1, ..., 99. 

Hmm, let me think about the structure where we have a "universal" clique of size k and the rest in triangles.

Construction 2: Have a clique C of size c, and 33 - (something) triangles. Wait, let me think.

We need 100 vertices. Suppose we have a clique C of size m and t triangles (disjoint from C and each other), with m + 3t = 100. 

When we remove a vertex from C: C becomes m-1 vertices, plus t triangles. We need to tile m-1 + 3t = 99 vertices into triangles. The t triangles are fine. The m-1 vertices of C need to be tiled into triangles using only C-edges (clique, so fine) and possibly mixing with triangle vertices. If m-1 ≡ 0 mod 3, then C minus one vertex tiles into (m-1)/3 triangles. So need m ≡ 1 mod 3.

When we remove a vertex from a triangle T_i: T_i becomes 2 vertices, C stays m, other t-1 triangles stay. Total: m + 2 + 3(t-1) = m + 3t - 1 = 99. We need to tile. The 2 leftover vertices need to form a triangle with someone. They can pair with a vertex from C (if the 2 leftover are adjacent, which they are since T_i was a triangle, and each is adjacent to the C-vertex if C is universal to triangles). So: leftover pair {a,b} + one vertex c from C form a triangle, needing a-c, b-c edges (a-b already there). Then C minus c has m-1 vertices, need m-1 ≡ 0 mod 3, so m ≡ 1 mod 3. And the remaining t-1 triangles are fine.

So: m ≡ 1 mod 3, m + 3t = 100. Edges: C has C(m,2) edges, t triangles have 3t edges, cross edges: every triangle vertex connected to every C vertex = 3t · m edges.

Total = C(m,2) + 3t + 3tm = m(m-1)/2 + 3t + 3tm = m(m-1)/2 + 3t(1+m).

With m + 3t = 100, so 3t = 100 - m.

Total = m(m-1)/2 + (100-m)(1+m) = m(m-1)/2 + (100-m)(m+1).

= m(m-1)/2 + 100m + 100 - m² - m = m(m-1)/2 + 99m + 100 - m².

= (m² - m)/2 + 99m + 100 - m² = m²/2 - m/2 + 99m + 100 - m² = -m²/2 + 98.5m + 100.

Wait let me redo: (m²-m)/2 - m² + 99m + 100 = (m² - m - 2m²)/2 + 99m + 100 = (-m² - m)/2 + 99m + 100 = -m²/2 - m/2 + 99m + 100 = -m²/2 + 97m/2 + 100.

To minimize, take derivative: -m + 97/2 = 0, m = 97/2 = 48.5. Since it's a downward parabola, minimum at the endpoints. m ≡ 1 mod 3, m + 3t = 100, m ≥ 1.

m = 1: total = -1/2 + 97/2 + 100 = 96/2 + 100 = 48 + 100 = 148. Wait, m=1: C is a single vertex, t = 33. This is exactly the first construction! Edges = C(1,2) + 3·33 + 3·33·1 = 0 + 99 + 99 = 198. But my formula gives 148? Let me recheck.

Hmm, with m=1, 3t = 99, t = 33. Total = 1·0/2 + 99·(1+1) = 0 + 99·2 = 198. 

Oh I made an arithmetic error. Let me redo. Total = m(m-1)/2 + (100-m)(m+1).

m=1: 0 + 99·2 = 198. ✓.

m=4: 4·3/2 + 96·5 = 6 + 480 = 486. Worse.

m=97: 97·96/2 + 3·98 = 4656 + 294 = 4950. Much worse.

So in this family, m=1 gives 198, and it increases. So the first construction (198) is best in this family.

But maybe a different family does better. The issue with the above is the cross edges (3tm). 

Let me think about reducing cross edges. Instead of every triangle vertex connecting to every C vertex, maybe we only need each triangle vertex to connect to enough C vertices.

When we remove a vertex from triangle T_i, the 2 leftover need to form a triangle with some C vertex. So each pair of vertices in T_i (there are 3 pairs) needs a common neighbor in C. Actually, when we remove one vertex from T_i, the remaining 2 form a specific pair, and they need a common C-neighbor. There are 3 ways to remove a vertex (giving 3 different pairs), and each pair needs at least one common neighbor in C.

So for each triangle T_i = {a, b, c}: 
- pair {b,c} needs common neighbor in C
- pair {a,c} needs common neighbor in C  
- pair {a,b} needs common neighbor in C

The minimal way: if all of a, b, c connect to a single vertex c0 in C, then all three pairs have c0 as common neighbor. That uses 3 edges per triangle (to c0). But then when we remove a vertex from T_i, we use c0 for the triangle, and C \ {c0} has m-1 vertices needing tiling, m-1 ≡ 0 mod 3.

But wait, different triangles might use different C vertices. If all triangles use the same c0, then when we remove a vertex from T_i, we use c0, and c0 is removed from C-pool. The rest of C (m-1 vertices) tiles into triangles (m ≡ 1 mod 3). The other triangles are fine. 

But what if we remove a vertex from T_i AND we also need... no, we only remove one vertex total. So only one triangle gets disrupted, uses c0, rest fine.

But what if we remove c0 itself? Then C \ {c0} has m-1 vertices, m-1 ≡ 0 mod 3, tiles fine. All t triangles intact. Good.

So: C is a clique of size m ≡ 1 mod 3. Each triangle T_i has all 3 vertices connected to a single "assigned" C vertex c(i). Different triangles can be assigned to different C vertices or the same.

Edges: C(m,2) [clique] + 3t [triangles] + 3t [each triangle's 3 vertices to assigned C vertex] = m(m-1)/2 + 3t + 3t = m(m-1)/2 + 6t.

With m + 3t = 100, 3t = 100 - m, 6t = 2(100-m) = 200 - 2m.

Total = m(m-1)/2 + 200 - 2m = (m² - m)/2 + 200 - 2m = (m² - m - 4m)/2 + 200 = (m² - 5m)/2 + 200.

Minimize: derivative (2m - 5)/2 = 0, m = 2.5. Parabola opens up, so minimum near m = 2.5. m ≡ 1 mod 3: m = 1 or m = 4.

m = 1: (1 - 5)/2 + 200 = -2 + 200 = 198. Same as before (since with m=1, the "assigned" vertex is the only one, so it's the same construction).

m = 4: (16 - 20)/2 + 200 = -2 + 200 = 198. Also 198!

Interesting, m=4 also gives 198. Let me verify: m=4, C = clique of 4, t = 32 triangles. Edges: C(4,2) = 6, triangles = 96, cross = 96. Total = 6 + 96 + 96 = 198. 

When we remove a vertex from C: 3 vertices left in C, form a triangle. 32 triangles intact. Total 33 triangles. ✓.

When we remove a vertex from T_i: 2 leftover, pair with assigned C vertex c(i). C \ {c(i)} has 3 vertices, form a triangle. Other 31 triangles intact. Total: 1 (leftover+c(i)) + 1 (C\c(i)) + 31 = 33. ✓.

When we remove c(i) from C (if c(i) is the assigned vertex of some triangle): C \ {c(i)} = 3 vertices, triangle. All 32 triangles intact. ✓. But wait, what if c(i) is assigned to multiple triangles? Removing c(i) from C: C\{c(i)} = 3 vertices, triangle. All 32 triangles intact (we didn't remove from any triangle). ✓. Good.

So m=4 also gives 198. Same count. Can we do better with a smarter assignment?

The cross edges are 3t = 3 per triangle (to assigned vertex). Can we reduce further? What if a triangle's 3 vertices don't all connect to the same C vertex?

For triangle T_i = {a,b,c}, we need:
- {b,c} has a common neighbor in C
- {a,c} has a common neighbor in C
- {a,b} has a common neighbor in C

Minimal edges: if a connects to c1, b connects to c2, c connects to c3, then {b,c} needs common neighbor: b and c both connect to... b connects to c2, c connects to c3. Common neighbor needs c2 = c3 or some other shared vertex. This is getting complicated.

Actually, the minimum number of edges from T_i to C such that each pair has a common C-neighbor: 

If all three connect to the same vertex: 3 edges.
If a→c1, b→c1, c→c2: {a,b} share c1 ✓, {a,c}: a→c1, c→c2, no common unless c1=c2. {b,c}: b→c1, c→c2, no common. So need c1 = c2, back to 3 edges to same vertex. Or add more edges.

What about a→c1, b→c2, c→c3 with c1, c2, c3 distinct? Then no pair shares a common neighbor. Need more edges. Add a→c2: {a,b} share c2 ✓. Add b→c3: {b,c} share c3 ✓. Add c→c1: {a,c} share c1 ✓. That's 6 edges. Worse.

So 3 edges (all to same vertex) is minimal per triangle. So cross edges ≥ 3t = 3(100-m)/3 = 100 - m.

Total ≥ m(m-1)/2 + 3t + (100-m) = m(m-1)/2 + (100-m) + (100-m) = m(m-1)/2 + 2(100-m).

Wait, I need to recount. The triangle edges are 3t and cross edges are 3t (minimum). So total = C(m,2) + 3t + 3t = C(m,2) + 6t. With 3t = 100-m: C(m,2) + 2(100-m) = m(m-1)/2 + 200 - 2m.

This is minimized at m = 1 or m = 4 (both ≡ 1 mod 3 near m=2.5), giving 198.

Hmm, but maybe we don't need C to be a clique. Let me reconsider.

What if C is not a clique but still tiles into triangles when a vertex is removed? We need: for every vertex w in C, C \ {w} tiles into triangles. So C itself is a graph on m vertices where every vertex-deleted subgraph has a triangle factor. This is the same type of condition but smaller! 

This is recursive. Let f(n) = minimum edges in a graph on n vertices where every vertex-deleted subgraph has a triangle factor (and n ≡ 1 mod 3, since we need n-1 ≡ 0 mod 3).

Wait, but actually the condition on C is slightly different. C needs: for every w in C, C - w has a triangle factor. And C has m vertices with m ≡ 1 mod 3.

So f(m) is the minimum for this sub-problem. And our total is f(m) + 6t where 3t = 100 - m.

f(1) = 0 (single vertex, removing it leaves empty, trivially factorable).
f(4) = ? 4 vertices, removing any leaves 3, must form a triangle. So every 3-subset must be a triangle, meaning all C(4,3) = 4 triples are triangles, so it's K_4 with 6 edges. So f(4) = 6.

So with m=4: f(4) + 6·32 = 6 + 192 = 198. Same.

f(7): 7 vertices, removing any leaves 6 = 2 triangles. This is more interesting. Can we do better than K_7?

For 7 vertices, removing any vertex leaves 6 vertices that tile into 2 triangles. 

Construction for 7: Take the Fano plane? 7 points, 7 lines of 3. Each point is on 3 lines. Removing a point leaves 6 points. The lines not through that point: each point is on 3 lines, total 7 lines, 3 through the point, so 4 lines not through it. But these 4 lines cover 6 points (each line has 3 points, 4 lines, but they overlap). Hmm, we need 2 disjoint triangles covering all 6.

Actually, let me think of the "friendship graph" or other structures.

For 7 vertices: Consider K_7 minus a 7-cycle? Or some other graph.

Actually, let me think about what graph on 7 vertices has the property that every 6-vertex subset tiles into 2 triangles.

The complete graph K_7 works (3060... no, C(7,2) = 21 edges). Can we do with fewer?

Consider the complement: H on 7 vertices. G = K_7 - H. For every vertex v, G - v = K_6 - (H - v) must have a triangle factor (2 disjoint triangles). K_6 has many triangle factors. We need that H - v doesn't destroy all triangle factors. 

A triangle factor of K_6 is a partition into 2 triples. There are 10 such partitions (6!/(3!3!·2!) = 10). H - v removes some edges. We need at least one partition to survive (all 6 edges present).

To maximize H (minimize G), we want H as large as possible such that for every v, some triangle factor of K_6 survives in G-v.

This is getting complex. Let me think about specific constructions.

For 7 vertices, consider the Paley-type or a specific graph. 

Actually, let me think about the "windmill" / friendship graph: 7 vertices, one center connected to all 6 others, and the 6 others form 3 disjoint edges (3 triangles sharing the center). This has 6 + 3 = 9 edges. But removing the center leaves 3 disjoint edges, not triangles. So doesn't work.

Let me try: 7 vertices, two triangles sharing a vertex, plus... no.

Hmm, let me think about this differently. Let me consider the recursive formula:

f(100) ≤ min over m ≡ 1 (mod 3), m | (100-m) ≡ 0 mod 3 [always true since 100 ≡ 1 mod 3] of f(m) + 2(100 - m).

f(1) = 0: 0 + 2·99 = 198.
f(4) = 6: 6 + 2·96 = 198.
f(7) = ?: ? + 2·93 = ? + 186.
f(10) = ?: ? + 2·90 = ? + 180.

If f(7) ≤ 12, then we beat 198. If f(10) ≤ 18, we beat 198. Etc.

So the question is whether f(n) for larger n can be small enough.

Let me figure out f(7). 

For 7 vertices, we need every 6-subset to have a triangle factor. 

Let me try to construct a graph on 7 vertices with few edges.

Construction: Label vertices 0-6. Consider the graph where edges are: all pairs {i, j} with i - j ≡ ±1 (mod 7) [7-cycle, 7 edges] plus all pairs {i,j} with i-j ≡ ±2 (mod 7) [another 7 edges]. Total 14 edges. This is the circulant C_7(1,2), which is the complement of C_7(3) = C_7. So G = K_7 - C_7, with 21 - 7 = 14 edges.

Does every 6-subset tile into 2 triangles? G = K_7 - C_7. Remove vertex v: K_6 - C_6' where C_6' is the path P_6 (the 7-cycle minus one vertex is a path on 6 vertices, but as edges of H, it's the edges of the 7-cycle not incident to v, which form a path on 6 vertices, i.e., 5 edges).

So G - v = K_6 minus a P_6 (path on 6 vertices, 5 edges). We need a triangle factor. K_6 has 15 edges, minus 5 = 10 edges. Need 2 disjoint triangles (6 edges).

The missing edges form a path a-b-c-d-e-f (5 edges). A triangle factor is 2 disjoint triangles. We need to find 2 disjoint triangles in K_6 - P_6.

Triangles in K_6 - P_6: a triangle {x,y,z} is valid iff none of {xy, yz, xz} is an edge of P_6. 

P_6 = a-b-c-d-e-f. Missing edges: ab, bc, cd, de, ef.

We need 2 disjoint triangles covering all 6 vertices. 

Possible triangle factors of K_6: there are 10. Let me list them as partitions of {a,b,c,d,e,f}:
1. {a,b,c},{d,e,f}: check abc: ab missing. ✗
2. {a,b,d},{c,e,f}: abd: ab missing. ✗
3. {a,b,e},{c,d,f}: abe: ab missing. ✗
4. {a,b,f},{c,d,e}: abf: ab missing; cde: cd, de missing. ✗
5. {a,c,d},{b,e,f}: acd: cd missing. ✗
6. {a,c,e},{b,d,f}: ace: all present? ac, ae, ce: none in {ab,bc,cd,de,ef}. ✓. bdf: bd, bf, df: none missing. ✓. So {a,c,e},{b,d,f} works!
7. {a,c,f},{b,d,e}: bde: de missing. ✗
8. {a,d,e},{b,c,f}: ade: de missing. ✗
9. {a,d,f},{b,c,e}: bce: bc missing. ✗
10. {a,e,f},{b,c,d}: bcd: bc, cd missing; aef: ef missing. ✗

So factor 6 works: {a,c,e},{b,d,f}. 

But this is for a specific P_6. Since the graph is vertex-transitive (circulant), removing any vertex gives an isomorphic graph. So it works for all vertices. 

So f(7) ≤ 14. Then total ≤ 14 + 186 = 200. That's worse than 198!

Hmm. So f(7) = 14 gives 200 > 198. Not helpful.

Can we do better than 14 for f(7)? Let me think about lower bounds for f(7).

For 7 vertices, each vertex has degree d. When we remove any other vertex u, vertex v must be in a triangle in G-u. So N(v) minus any vertex still has an edge (as before). So d(v) ≥ 3 and N(v) is not a star.

Sum of degrees ≥ 7·3 = 21, so edges ≥ 21/2 = 10.5, so ≥ 11.

But can we achieve 11 or 12? Let me think.

With 11 edges, sum of degrees = 22, so degrees like 3,3,3,3,3,3,4 (sum 22) or similar.

This is getting complicated. Let me think about whether f(7) can be less than 12, which would give total < 198.

For total < 198 with m=7: need f(7) < 12, i.e., f(7) ≤ 11. 

For total < 198 with m=10: need f(10) < 18, i.e., f(10) ≤ 17.

Hmm, this recursive approach might not easily beat 198. Let me think about whether 198 is actually the answer, or if there's a completely different construction.

Let me reconsider. Maybe the construction doesn't have to be of this "clique + triangles" form.

Let me think about the problem from a different angle.

General construction: We need a graph G on 100 vertices such that for every v, G-v has a K_3-factor.

Let me think about this as a "K_3-factor critical" graph. A graph is called K_3-factor-critical if removing any vertex leaves a graph with a K_3-factor. (This is analogous to factor-critical graphs for perfect matchings.)

There's literature on this. Let me think about what's known.

For perfect matchings, factor-critical graphs: minimum edges for n vertices (n odd) is n-1 (a path? no...). Actually, factor-critical graphs on n vertices have at least n edges? No... A cycle C_n is factor-critical for odd n, with n edges. And it's known that factor-critical graphs have at least n edges (I think). Wait, actually for n=3, K_3 has 3 edges = n. For n=5, C_5 has 5 edges = n. 

For K_3-factor-critical graphs, the minimum might be different.

Let me think about small cases. 

n=4 (≡ 1 mod 3): K_3-factor-critical means removing any vertex leaves 3 vertices that form a triangle. So every 3-subset is a triangle → K_4, 6 edges. f(4) = 6.

n=7: We found 14 edges (K_7 - C_7). Can we do better?

Let me try to find a graph on 7 vertices with fewer edges.

Try 12 edges. Complement has 21 - 12 = 9 edges. For every vertex v, G-v = K_6 - (H-v) must have a K_3-factor. H-v has 9 - deg_H(v) edges on 6 vertices.

We need: for every v, K_6 - (H-v) has a K_3-factor. 

A K_3-factor of K_6 is 2 disjoint triangles. There are 10 such factors. H-v must not hit all of them (must leave at least one intact).

Each factor has 6 edges. H-v hits a factor if it contains at least one of the factor's 6 edges. H-v leaves a factor intact iff none of its edges are in that factor.

So we need: for every v, there exists a factor F such that F ∩ E(H-v) = ∅, i.e., E(H-v) ⊆ complement of F (within K_6). The complement of F in K_6 has 15 - 6 = 9 edges (which is K_{3,3} between the two triples, plus... no. K_6 has 15 edges, F uses 6, remaining 9 form K_{3,3} between the two triples).

So we need E(H-v) ⊆ K_{3,3}(F) for some factor F, i.e., H-v is a subgraph of some K_{3,3} on the 6 vertices.

H-v has 9 - deg_H(v) edges. K_{3,3} has 9 edges. So we need H-v ⊆ K_{3,3}, meaning H-v has at most 9 edges (always true since H has 9 edges total) and H-v is bipartite (subgraph of K_{3,3}).

So the condition is: for every v, H-v is bipartite. 

H-v is bipartite for every v iff H is "vertex-bipartite", i.e., removing any vertex makes it bipartite. This means H has at most one odd cycle that goes through every vertex... actually, H-v bipartite for all v means H is a subgraph of an odd cycle (plus trees attached)? 

A graph where removing any vertex makes it bipartite: this means every odd cycle in H passes through every vertex. If H has two odd cycles, there's a vertex not on one of them (if they don't share all vertices), and removing that vertex leaves the other odd cycle. So all odd cycles must share all vertices. The simplest case: H is a single odd cycle (plus possibly some bipartite parts attached).

If H = C_7 (7-cycle), then H has 7 edges, G = K_7 - C_7 has 14 edges. H-v = P_6, bipartite ✓. This is our construction with 14 edges.

If H = C_7 + one more edge (8 edges), G has 13 edges. H-v: removing v, H-v has 8 - deg_H(v) edges. If the extra edge creates another odd cycle... Let's say H = C_7 + chord {0,3}. Then H has two odd cycles: C_7 and the cycle 0-1-2-3-0 (length 4, even) and 0-3-4-5-6-0 (length 5, odd). So odd cycles are C_7 and 0-3-4-5-6-0. These don't share all vertices (C_7 uses all, but the 5-cycle uses {0,3,4,5,6}, not vertex 1 or 2). Remove vertex 1: H-1 still has the 5-cycle 0-3-4-5-6-0, which is odd. So H-1 is not bipartite. ✗.

So adding any chord to C_7 creates a second odd cycle not through all vertices, breaking the condition. So H must be exactly C_7 (or a subgraph of C_7, but then G has more edges).

Wait, H could be C_7 plus some bipartite edges (edges that don't create odd cycles). But in C_7, every chord creates an odd cycle (since C_7 is odd, any chord splits it into two paths, one of which has odd length, creating an odd cycle). Actually, a chord {i,j} in C_7 splits it into paths of length d and 7-d (where d is the distance). One of d, 7-d is odd and the other even (since 7 is odd). The odd one + chord = even cycle, the even one + chord = odd cycle. So every chord creates an odd cycle of length (even path) + 1 = odd. And this odd cycle doesn't use all 7 vertices (it uses the even path's vertices). So H-v for v not on this odd cycle would still have it. So no chords allowed.

So H = C_7 is the unique maximum (7 edges), giving G = 14 edges. So f(7) = 14.

Hmm wait, but I assumed H has 9 edges (G has 12). Let me reconsider. I was checking if f(7) ≤ 12 is possible. With G having 12 edges, H has 9 edges. The condition is H-v bipartite for all v. But H = C_7 has only 7 edges, and we showed we can't add chords. So H can have at most 7 edges (if H must be C_7 or subgraph). So G has at least 14 edges. f(7) = 14.

Wait, I think I need to be more careful. The condition is: for every v, there EXISTS a factor F such that H-v ⊆ K_{3,3}(F). I said this means H-v is bipartite, but that's not quite right. H-v ⊆ K_{3,3}(F) for some F means H-v is a subgraph of some K_{3,3}, which means H-v is bipartite. Yes, that's correct: a graph is a subgraph of K_{3,3} (on 6 vertices) iff it's bipartite with parts of size ≤ 3. 

Hmm, actually K_{3,3} has specific part sizes 3 and 3. H-v is a subgraph of K_{3,3} iff H-v is bipartite with a bipartition into parts of size 3 and 3. But any bipartite graph on 6 vertices can be embedded in K_{3,3} (just put one part on each side). Wait, not exactly—the bipartition of H-v must have parts of size exactly 3 and 3 (or less, with the rest being isolated). Actually, if H-v is bipartite with parts A, B where |A| ≤ 3 and |B| ≤ 3 and |A|+|B| ≤ 6, then we can embed it in K_{3,3} by extending A and B to size 3. But if H-v is bipartite with parts of size 4 and 2, can we embed it in K_{3,3}? Only if we can re-bipartition. A bipartite graph might have a unique bipartition (if connected). 

Hmm, this is a subtlety. Let me reconsider. H-v ⊆ K_{3,3}(F) means all edges of H-v go between the two triples of F. So the bipartition of H-v (if connected, unique up to swapping) must align with the 3-3 split of F. If H-v is connected and bipartite with parts of size 4 and 2, then it can't be a subgraph of any K_{3,3} (which requires 3-3 split). 

So the condition is: for every v, H-v is bipartite with a bipartition into parts of size 3 and 3 (i.e., H-v is bipartite and has a bipartition with equal parts, or can be re-bipartitioned to 3-3).

Actually, if H-v is bipartite, it might have multiple bipartitions (if disconnected). We need at least one bipartition to be 3-3. 

For H = C_7: H-v = P_6, which is connected, bipartite with parts of size 3 and 3. ✓.

OK so the analysis holds for C_7. And we showed H can't have more than 7 edges (no chords). But what about non-cycle graphs H with more edges?

Could H be, say, a theta graph or something with 8 edges where every H-v is bipartite with 3-3 bipartition?

If H has 8 edges and H-v is bipartite for all v, then H is "vertex-bipartite." As argued, all odd cycles must pass through every vertex. With 7 vertices and 8 edges, H has at least 2 cycles. If both are odd and both pass through all 7 vertices... two Hamiltonian odd cycles sharing all vertices. E.g., C_7 and another C_7 (different ordering). That's 14 edges, too many. 

Two odd cycles through all 7 vertices: each has ≥ 7 edges. If they share some edges, total could be less. But two distinct Hamiltonian cycles share at most... they could share several edges. Minimum total edges for two Hamiltonian cycles: if they share k edges, total = 14 - k. For 8 edges, need k = 6, i.e., they share 6 edges. Two C_7's sharing 6 edges: they differ in 1 edge each. So H = C_7 ∪ {one extra edge} = C_7 + one chord. But we showed chords create smaller odd cycles. 

Specifically, if H = C_7 + chord {0,3}, the odd cycles are C_7 and 0-3-4-5-6-0 (length 5). The 5-cycle doesn't pass through vertices 1, 2. So removing vertex 1 leaves the 5-cycle, making H-1 non-bipartite. ✗.

So indeed, H can't have more than 7 edges if H-v must be bipartite for all v. Hence f(7) = 14, and the recursive bound gives 14 + 186 = 200 > 198.

Hmm, so the recursive approach with m=7 doesn't help. Let me check m=10.

For m=10, we need f(10): graph on 10 vertices, removing any leaves 9 = 3 triangles. 

This is harder to analyze. Let me think about whether the recursive approach can ever beat 198.

The recursive formula: f(100) ≤ f(m) + 2(100 - m) for m | 100, m ≡ 1 mod 3. Wait, m doesn't need to divide 100; we need 100 - m ≡ 0 mod 3, i.e., m ≡ 1 mod 3 (since 100 ≡ 1 mod 3).

f(100) ≤ f(m) + 2(100-m).

For this to beat 198: f(m) + 2(100-m) < 198, i.e., f(m) < 198 - 2(100-m) = 198 - 200 + 2m = 2m - 2.

So need f(m) < 2m - 2, i.e., f(m) ≤ 2m - 3.

f(1) = 0 ≤ 2·1 - 3 = -1? No, 0 > -1. So f(1) = 0 > -1. Doesn't satisfy. (And 0 + 198 = 198, not < 198.)

f(4) = 6 ≤ 2·4 - 3 = 5? No, 6 > 5. Doesn't beat.

f(7) = 14 ≤ 2·7 - 3 = 11? No, 14 > 11.

f(10) ≤ 17? Need to check.

Hmm, it seems like f(m) grows faster than 2m. Let me think about a lower bound for f(n).

Lower bound for f(n): Every vertex has degree ≥ 3 (as shown). So f(n) ≥ 3n/2. For n=10: f(10) ≥ 15. Need f(10) ≤ 17 to beat 198. So it's possible if f(10) is 15, 16, or 17.

But actually the degree ≥ 3 bound might not be tight. Let me think more carefully.

Actually, wait. The degree ≥ 3 bound: we showed N(v) must not be a star. But actually, we need something stronger. When we remove vertex u (u ≠ v), v must be in a triangle in G-u. This means for every u ≠ v, there exist a, b ∈ N(v) \ {u} with ab ∈ E(G). So N(v) \ {u} contains an edge for every u. This means N(v) is not a star (as I said), giving d(v) ≥ 3.

But there's a stronger condition: not only must v be in a triangle, but ALL vertices must be covered. So the condition is global, not just local.

Let me think about a better lower bound.

Actually, let me think about the problem differently. Let me consider the following counting argument.

For each vertex v, let T_v be a triangle factor of G-v (33 triangles). Each T_v uses 99 edges. 

Consider the multiset of all edges used across all T_v (v = 1 to 100). Total count = 100 · 99 = 9900. Each edge {a,b} appears in T_v only if v ∉ {a,b}, so for at most 98 values of v. But actually, an edge might not appear in all T_v for v ∉ {a,b}—it depends on the choice of triangle factors.

To minimize edges, we'd want to reuse edges as much as possible. If every edge appears in all 98 possible T_v's, then number of edges ≥ 9900 / 98 = 101.02..., so ≥ 102. But this is a weak bound.

Hmm, that's not tight. Let me think differently.

Actually, let me reconsider the problem. Maybe the answer is 198, or maybe it's something else entirely.

Let me think about another type of construction that might use fewer edges.

Construction 3: "Cyclic" construction. 

Arrange 100 vertices in a circle. Connect each vertex to its neighbors at distance 1, 2, ..., k (mod 100). This gives a circulant graph. We need: removing any vertex, the remaining 99 tile into 33 triangles.

For a circulant graph C_100(1, 2, ..., k), triangles exist if we can find 3 vertices pairwise within distance k. 

This is hard to make work with few edges. Let me think differently.

Construction 4: "Tripartite-like" but for triangles.

Hmm, triangles need mutual friendship, so we need cliques, not bipartite structures.

Let me think about the problem from the answer's perspective. This is a competition problem, so the answer is likely a clean number. 198 = 2 · 99. Let me see if that's the answer.

Actually, let me reconsider. Let me think about a lower bound of 198.

Lower bound attempt: 

For each vertex v, consider the triangle factor T_v of G-v. Each triangle in T_v has 3 edges. Now, vertex v is not in any triangle of T_v. 

Consider edge e = {a,b}. It can appear in T_v for v ∉ {a,b}. 

Hmm, let me think about a different approach. 

Let me think about the degree sum. For each vertex v, in the triangle factor T_v, each of the 99 other vertices is in exactly one triangle, using 2 edges incident to it (within the triangle). So in T_v, the sum of degrees (within T_v) is 99 · 2 = 198, and there are 99 edges.

Now, sum over all v of |E(T_v)| = 100 · 99 = 9900.

Each edge {a,b} ∈ E(G) contributes to |E(T_v)| for each v such that {a,b} ∈ T_v. Since {a,b} ∈ T_v requires v ∉ {a,b}, edge {a,b} contributes to at most 98 of the T_v's.

So 9900 ≤ |E(G)| · 98, giving |E(G)| ≥ 9900/98 ≈ 101.02, so |E(G)| ≥ 102.

This is weak. The issue is that not every edge can appear in all 98 triangle factors.

Let me think about a stronger bound. 

Consider a specific vertex v with degree d(v). In T_u for u ≠ v, vertex v is in a triangle, so v uses 2 of its edges in T_u. These 2 edges are from N(v). Over all u ≠ v (99 values of u), v is in 99 triangles (one per T_u), each using 2 edges from v. But v only has d(v) edges. Each edge {v,w} can be used in T_u for u ∉ {v,w}, so at most 98 times. 

The 99 triangles (one for each u ≠ v) use 2 · 99 = 198 edge-slots from v's edges. Each of v's d(v) edges can fill at most 98 slots. So d(v) · 98 ≥ 198, giving d(v) ≥ 198/98 ≈ 2.02, so d(v) ≥ 3. Same bound as before.

Let me try yet another approach. 

Think about it this way: for each vertex v, G-v has a K_3-factor. This means G-v has a perfect K_3-tiling. 

A necessary condition for a K_3-tiling: the number of vertices is divisible by 3 (99 = 33·3 ✓), and some connectivity/degree conditions.

Let me think about the structure of K_3-factor-critical graphs.

Actually, let me look at this from the perspective of the Gallai-Edmonds decomposition or similar structure theory, but for K_3-factors.

Hmm, this is getting complicated. Let me try to think about whether 198 is optimal by trying to find a construction with fewer edges.

Let me try a different construction.

Construction 5: "Cycle of triangles."

Arrange 34 groups: G_0, G_1, ..., G_33 where G_0 has 1 vertex and G_1, ..., G_33 have 3 vertices each. 

Make each G_i (i ≥ 1) a triangle. Connect G_0 to all vertices (universal). This is construction 1 with 198 edges.

Alternatively: don't make G_0 universal. Instead, connect G_0 to specific vertices.

When we remove the vertex in G_0: 33 triangles tile perfectly. ✓.

When we remove a vertex from G_i (i ≥ 1): 2 vertices left in G_i, need to form a triangle with someone. G_0's vertex must pair with them. So G_0's vertex must be adjacent to both remaining vertices of G_i. Since any of the 3 vertices could be removed, G_0 must be adjacent to all 3 vertices of each G_i. So G_0 is universal. Back to 198.

So construction 1 is forced if we use this structure. 

What if we use a different structure where the "extra" vertex isn't needed?

Construction 6: No universal vertex. Instead, when we remove a vertex from a triangle, the leftover 2 vertices pair with a vertex from ANOTHER triangle, disrupting it, and so on—a chain reaction.

This is like a "augmenting path" for K_3-factors.

Let me think about this. Consider 33 triangles T_1, ..., T_33 and one extra vertex s. But instead of s being universal, s is connected to specific vertices, and there's a chain structure.

When we remove a vertex from T_1, the 2 leftover need a partner. They take a vertex from T_2, leaving 2 in T_2, who take a vertex from T_3, etc. This is a chain that must terminate.

For this to work, we need a structure where removing any vertex triggers a chain that re-tils everything.

This is essentially the structure of factor-critical graphs (for matchings), generalized to K_3-factors.

For matchings, factor-critical graphs are built from odd cycles and "ear" decompositions. The minimum factor-critical graph on n vertices is C_n (n edges).

For K_3-factors, the analogous structure might give fewer edges.

Let me think about a specific construction.

Construction 7: "Chain of triangles."

Vertices: s, a_1, b_1, c_1, a_2, b_2, c_2, ..., a_33, b_33, c_33. (1 + 99 = 100.)

Edges: 
- Each {a_i, b_i, c_i} is a triangle.
- s is connected to a_1, b_1 (two vertices of T_1).
- For each i, connect c_i to a_{i+1}, b_{i+1} (c_i connects to two vertices of T_{i+1}).
- Also c_33 connects back to s? 

Let me think about what happens when we remove a vertex.

Remove s: 33 triangles tile perfectly. ✓.

Remove a_1: T_1 has b_1, c_1 left. They need a partner. b_1 and c_1 are adjacent (triangle). They can pair with... s? s is adjacent to a_1, b_1. Is s adjacent to c_1? In my setup, s is connected to a_1, b_1 only. So s-c_1 is not an edge. So {b_1, c_1, s} is not a triangle (missing s-c_1). 

Hmm, let me redesign. 

Let me think about this more carefully. I want a structure where removing any vertex from any triangle triggers a chain that re-tils.

Alternative: think of it as a "cycle" of 34 groups (33 triangles + 1 single), where removing from any group causes a shift.

Construction 8: 34 groups in a cycle. G_0 (single vertex s), G_1, ..., G_33 (triangles). 

When we remove a vertex from G_i, the 2 leftover take a vertex from G_{i+1}, leaving 2 in G_{i+1}, which take from G_{i+2}, etc., until we reach G_0 (the single vertex), which gets absorbed.

For this, we need: the 2 leftover from G_i can form a triangle with one vertex from G_{i+1}. So each vertex of G_i must be adjacent to at least one vertex of G_{i+1} (and the two leftover must share a common neighbor in G_{i+1}).

This is getting complex. Let me think about a simpler version.

Actually, let me think about the problem as follows. We have 100 ≡ 1 (mod 3) vertices. We want K_3-factor-critical. 

Let me consider the following construction based on a "cycle" structure:

Take 100 vertices arranged in a cycle v_0, v_1, ..., v_99. Connect v_i to v_{i+1}, v_{i+2} (mod 100) [each vertex connects to next 2]. Also connect v_i to v_{i+3}? 

Hmm, let me think about what edges are needed for triangles. A triangle {v_i, v_j, v_k} needs all three pairwise edges.

Let me try: connect v_i to v_{i+1} and v_{i+2} (mod 100). Then triangles are {v_i, v_{i+1}, v_{i+2}}. These are 100 triangles, each overlapping. Removing v_0, can we tile v_1, ..., v_99? Triangles {v_1,v_2,v_3}, {v_4,v_5,v_6}, ..., {v_97,v_98,v_99}. That's 33 triangles. ✓! And the edges needed: v_i to v_{i+1} (100 edges) and v_i to v_{i+2} (100 edges). Total 200 edges. But wait, do we need v_i to v_{i+2}? Triangle {v_i, v_{i+1}, v_{i+2}} needs edges v_i-v_{i+1}, v_{i+1}-v_{i+2}, v_i-v_{i+2}. The first two are "distance 1" edges, the third is "distance 2." 

But removing v_0, we need triangles {v_1,v_2,v_3}, {v_4,v_5,v_6}, etc. For {v_1,v_2,v_3}: edges v_1-v_2 (dist 1 ✓), v_2-v_3 (dist 1 ✓), v_1-v_3 (dist 2 ✓). Good.

But we also need: removing v_1, can we tile? v_0, v_2, v_3, ..., v_99. Triangles: {v_0, v_2, v_3}? Need v_0-v_2 (dist 2 ✓), v_2-v_3 (dist 1 ✓), v_0-v_3 (dist 3 ✗ if we only have dist 1,2). So {v_0, v_2, v_3} doesn't work.

Alternative tiling after removing v_1: {v_0, v_99, v_98}? v_0-v_99 (dist 1 ✓), v_99-v_98 (dist 1 ✓), v_0-v_98 (dist 2 ✓). ✓! Then {v_2,v_3,v_4}, ..., {v_95,v_96,v_97}. That's 1 + 32 = 33 triangles. ✓!

So removing v_1: {v_0,v_98,v_99}, {v_2,v_3,v_4}, {v_5,v_6,v_7}, ..., {v_95,v_96,v_97}. Let me count: 1 + (97-2+1)/3 = 1 + 96/3 = 1 + 32 = 33. ✓.

Removing v_2: {v_0,v_1,v_99}? v_0-v_1 (dist 1 ✓), v_1-v_99 (dist 2 ✓), v_0-v_99 (dist 1 ✓). ✓! Then {v_3,v_4,v_5}, ..., {v_96,v_97,v_98}. 1 + 32 = 33. ✓.

Removing v_k (general): We can "wrap around" v_k. Take {v_{k-2}, v_{k-1}, v_{k+1}}? Hmm, need to check edges. Actually, let me think about it more carefully.

Removing v_k: we have vertices v_0, ..., v_{k-1}, v_{k+1}, ..., v_99. We need to tile into 33 triangles. 

The idea: the 99 remaining vertices form a "path" (in the cyclic order) of length 99 (with a gap at position k). We can tile this path into 33 consecutive triples, but we need to handle the gap.

If k ≡ 0 mod 3: remove v_k, then {v_{k+1}, v_{k+2}, v_{k+3}}, ..., {v_{k-3}, v_{k-2}, v_{k-1}} (cycling around). Each triple is 3 consecutive vertices, forming a triangle (dist 1, 1, 2 edges). ✓.

If k ≡ 1 mod 3: We need to adjust. Remove v_k. The vertices before k: v_0, ..., v_{k-1} (k vertices). The vertices after: v_{k+1}, ..., v_99 (99-k vertices). k + (99-k) = 99. We need 33 triangles. If k ≡ 1 mod 3, then k-1 ≡ 0 mod 3 and 99-k ≡ 99-1 = 98... 99-k ≡ 2 mod 3. So we can't simply split into two groups of multiples of 3. We need to "bridge" the gap.

Bridge: take one vertex from before and two from after (or vice versa) to form a triangle across the gap. 

Take {v_{k-1}, v_{k+1}, v_{k+2}}: edges v_{k-1}-v_{k+1} (dist 2 ✓), v_{k+1}-v_{k+2} (dist 1 ✓), v_{k-1}-v_{k+2} (dist 3 ✗). Doesn't work (dist 3 not an edge).

Take {v_{k-2}, v_{k-1}, v_{k+1}}: v_{k-2}-v_{k-1} (dist 1 ✓), v_{k-1}-v_{k+1} (dist 2 ✓), v_{k-2}-v_{k+1} (dist 3 ✗). Doesn't work.

Hmm, distance 3 edges are missing. So bridging a single gap with only dist-1 and dist-2 edges is hard.

What if we add dist-3 edges? Then we have 300 edges (dist 1, 2, 3 each contribute 100). That's way more than 198.

What if instead of a cycle, we use a different structure?

Let me reconsider. The cycle construction with dist 1, 2 gives 200 edges, which is close to 198 but not better. And it doesn't even work for all removals (as shown, k ≡ 1 mod 3 is problematic).

Wait, let me re-examine. For k ≡ 1 mod 3, I showed removing v_1 works by using {v_0, v_98, v_99}. Let me re-examine for general k ≡ 1 mod 3.

Remove v_k where k ≡ 1 mod 3. The remaining vertices in cyclic order: v_{k+1}, v_{k+2}, ..., v_99, v_0, v_1, ..., v_{k-1}. This is 99 vertices in a path (linear order, since the cycle is broken at v_k). We need to tile into 33 consecutive triples.

{v_{k+1}, v_{k+2}, v_{k+3}}, {v_{k+4}, v_{k+5}, v_{k+6}}, ..., and the last triple would be {v_{k-3}, v_{k-2}, v_{k-1}}. Let me count: from v_{k+1} to v_{k-1} (cyclically) is 99 vertices. 99/3 = 33 triples. Each triple is 3 consecutive vertices in the cyclic order. 

But are 3 consecutive vertices always a triangle? {v_i, v_{i+1}, v_{i+2}}: edges v_i-v_{i+1} (dist 1 ✓), v_{i+1}-v_{i+2} (dist 1 ✓), v_i-v_{i+2} (dist 2 ✓). Yes! ✓.

So the tiling is: starting from v_{k+1}, take consecutive triples wrapping around to v_{k-1}. This works for any k!

Wait, but I need to check: the triple that "wraps around" the end of the cycle. E.g., if k=1, the triples are {v_2,v_3,v_4}, {v_5,v_6,v_7}, ..., {v_98,v_99,v_0}. The last triple {v_98, v_99, v_0}: v_98-v_99 (dist 1 ✓), v_99-v_0 (dist 1 ✓, since 99 and 0 are adjacent in the cycle), v_98-v_0 (dist 2 ✓, since |98-0| mod 100 = 2). ✓!

So the construction works: C_100 with edges of distance 1 and 2. 200 edges. And it works for all vertex removals.

But 200 > 198. So this isn't better.

Can we remove some edges from this construction? We have 200 edges. We need every triple of consecutive vertices (in the cyclic order after removing any one) to be a triangle. 

The triangles used are: for each k, the 33 triples of consecutive vertices starting from v_{k+1}. Over all k, which triples appear? 

A triple {v_i, v_{i+1}, v_{i+2}} (indices mod 100) is used when we remove v_k and this triple is one of the 33 consecutive triples. This triple is used for removal of v_k iff the triple doesn't contain v_k, i.e., k ∉ {i, i+1, i+2}. So it's used for 97 values of k. But more importantly, is this triple always a triangle? It needs edges v_i-v_{i+1}, v_{i+1}-v_{i+2}, v_i-v_{i+2}.

The edges v_i-v_{i+1} (dist 1) and v_{i+1}-v_{i+2} (dist 1) are in the graph. The edge v_i-v_{i+2} (dist 2) is also in the graph. So all 100 triples of consecutive vertices are triangles. 

But do we need ALL dist-1 and dist-2 edges? 

The dist-1 edges: v_i-v_{i+1} for all i. These are used in many triangles. Each dist-1 edge v_i-v_{i+1} is used in triangles {v_{i-1},v_i,v_{i+1}} and {v_i,v_{i+1},v_{i+2}}. If we remove a dist-1 edge, both these triangles break. But maybe other tilings don't use these specific triangles?

Hmm, this is getting complicated. The point is: with the cyclic tiling strategy, we need all consecutive triples to be triangles, requiring all dist-1 and dist-2 edges, giving 200 edges. 

But maybe we can use a different tiling strategy that requires fewer edges. Let me think...

Actually, let me reconsider the problem. Maybe 198 is the answer, and the construction is the "universal vertex + 33 triangles" one.

Let me try to prove a lower bound of 198.

Lower bound proof attempt:

For each vertex v, let T_v be a K_3-factor of G-v. T_v has 33 triangles, 99 edges.

Consider the sum S = Σ_v |E(T_v)| = 100 · 99 = 9900.

Each edge e = {a,b} appears in T_v only if v ∉ {a,b}. So e appears in at most 98 of the T_v's. But can an edge appear in all 98? 

If edge {a,b} appears in T_v for all v ∉ {a,b}, then for each such v, {a,b} is in a triangle in T_v, say {a,b,c_v}. The triangle {a,b,c_v} requires edges a-b, a-c_v, b-c_v. 

This is possible but requires many triangles containing {a,b}, one for each v (with different c_v, since c_v ≠ v). The c_v's are 98 distinct vertices (c_v ∈ V \ {a,b,v}). Actually, c_v can repeat: if c_v = c_w for v ≠ w, then triangle {a,b,c_v} is used in both T_v and T_w. That's fine.

So edge {a,b} could appear in many T_v's with the same third vertex c. E.g., {a,b,c} appears in T_v for all v ∉ {a,b,c} (95 values). 

So the maximum number of T_v's an edge can appear in is 98 (if for every v ∉ {a,b}, there's a triangle {a,b,c_v} in T_v). 

To get S = 9900 with |E(G)| edges, each appearing at most 98 times: |E(G)| ≥ 9900/98 ≈ 101.02. So |E(G)| ≥ 102. Weak.

Let me think about a better bound. 

Alternative: think about the degree of each vertex.

For vertex v, in each T_u (u ≠ v), v is in a triangle, using 2 edges incident to v. Over 99 values of u, v uses 198 edge-incidences. Each edge {v,w} can be used in T_u for u ∉ {v,w}, at most 98 times. So d(v) · 98 ≥ 198, d(v) ≥ 3. Sum: |E(G)| ≥ 150. Better but still < 198.

Hmm, can I push this further? 

For vertex v, the 99 triangles (one per T_u) each use 2 edges from v. But the triangles are {v, a_u, b_u} where a_u, b_u ∈ N(v) and a_u-b_u is an edge. Also, a_u, b_u ≠ u. 

The 99 triangles use 99 · 2 = 198 edge-incidences from v. Each edge {v,w} is used at most 98 times (for u ∉ {v,w}). But also, each triangle uses a specific edge a_u-b_u in N(v). 

Hmm, let me think about the structure within N(v). For each u ≠ v, there's an edge in N(v) \ {u} (the edge a_u-b_u). So N(v) \ {u} contains an edge for every u. As before, N(v) is not a star.

But I need a stronger bound. Let me think about what happens when d(v) = 3.

If d(v) = 3, N(v) = {a, b, c}. N(v) is not a star, so the induced graph on {a,b,c} has at least 2 edges (not a star means not all edges through one vertex; with 3 vertices, a star is 1 or 2 edges through one vertex; not a star means... actually with 3 vertices, the non-star graphs are: the triangle (3 edges) or... a single edge is a star (K_{1,1}), two edges sharing a vertex is a star (K_{1,2}), two disjoint edges impossible on 3 vertices. So non-star on 3 vertices = triangle (3 edges) or... wait, 0 edges, 1 edge, 2 edges (path) are all stars (or subgraphs of stars). 3 edges (triangle) is not a star. So N(v) must be a triangle, meaning a, b, c are pairwise adjacent.

So if d(v) = 3, then N(v) forms a triangle. The triangle {v, a, b} (or {v, a, c} or {v, b, c}) can be used in T_u for u ∉ {v, a, b}. 

For each u ≠ v, v is in a triangle in T_u. The only triangles containing v are {v,a,b}, {v,a,c}, {v,b,c} (since N(v) = {a,b,c} and they form a triangle). 

For u = a: v must be in a triangle in T_a, not containing a. So the triangle is {v, b, c} (the only one not containing a). ✓ (needs edges v-b, v-c, b-c, all present).
For u = b: triangle is {v, a, c}. ✓.
For u = c: triangle is {v, a, b}. ✓.
For u ∉ {v, a, b, c}: any of the three triangles work.

So d(v) = 3 is feasible from v's perspective. 

Now, if many vertices have degree 3, we might get a low edge count. But the global condition must hold.

Let me think about a construction where many vertices have degree 3.

Construction 9: "Triangular prism" type structure.

Consider the graph where we have 33 triangles T_1, ..., T_33 and one vertex s. s is connected to 2 vertices of each triangle (not all 3). And there are additional edges between triangles.

When we remove s: 33 triangles tile. ✓.

When we remove a vertex from T_i: 2 leftover in T_i. They need a partner. If s is connected to both, {leftover1, leftover2, s} works. But s must be connected to all 3 vertices of T_i (since any could be removed, and the remaining 2 must both connect to s). So s connects to all 3 of each T_i: 99 edges from s. Plus 99 triangle edges. Total 198. Same as before.

Unless the 2 leftover pair with a vertex from another triangle instead of s. Then s doesn't need to connect to all.

Let me explore this. Suppose T_i = {a_i, b_i, c_i}. When we remove a_i, the leftover {b_i, c_i} pairs with some vertex x from another triangle T_j. Then T_j loses x, leaving 2 in T_j, who pair with someone from T_k, etc. This is a chain.

For this to work, we need a "backup" structure. Let me think of a simple case.

Construction 10: Two triangles T_1 = {a,b,c}, T_2 = {d,e,f}, and vertex s. 7 vertices. 

When we remove s: {a,b,c}, {d,e,f}. ✓.
When we remove a: {b,c,?} and {d,e,f}. Need b,c to pair with someone. If b-c-s is a triangle (s-b, s-c edges), then {b,c,s}, {d,e,f}. ✓. Need s-b, s-c edges.
When we remove d: {a,b,c}, {e,f,s}. Need s-e, s-f edges.

So s connects to b, c, e, f (4 edges). Plus triangle edges: ab, ac, bc, de, df, ef (6 edges). Total 10 edges. 

But we also need: when we remove b, {a,c,?} and {d,e,f}. a-c-s triangle? Need s-a, s-c. But s is connected to b, c, e, f, not a. So {a,c,s} needs s-a. Not present. 

So s must connect to a too. Then s connects to a, b, c, e, f (5 edges). When we remove c: {a,b,s}, need s-a, s-b. ✓. When we remove e: {a,b,c}, {d,f,s}, need s-d, s-f. So s connects to d too. s connects to all 6: 6 edges + 6 triangle edges = 12. But that's just the universal construction (s universal to 2 triangles): 6 + 6 + 6 = 18? No wait, 6 (s to all) + 6 (triangles) = 12. 

Hmm, but for 7 vertices, f(7) = 14 (we proved). And 12 < 14? That can't be right. Let me recheck.

Oh wait, 7 vertices: s + 6 = 7. But 7 ≡ 1 mod 3, and we need removing any vertex to leave 6 = 2·3, tileable into 2 triangles. 

With s universal (connected to all 6) and 2 triangles: 6 + 6 = 12 edges. Does this work?

Remove s: 2 triangles. ✓.
Remove a (from T_1): {b,c,s} (s-b, s-c, b-c all edges ✓), {d,e,f}. ✓.
Remove d (from T_2): {a,b,c}, {e,f,s}. ✓.

So 12 edges works for 7 vertices! But I proved f(7) = 14 earlier. Contradiction!

Let me recheck my proof. I claimed f(7) = 14 based on the complement argument. Let me re-examine.

The complement argument: G on 7 vertices, H = complement. For every v, G-v has a K_3-factor. I argued this means H-v is bipartite (subgraph of K_{3,3}).

But with the universal construction: G has 12 edges, H has 21 - 12 = 9 edges. H = complement of (universal s + 2 triangles). 

G edges: s-a, s-b, s-c, s-d, s-e, s-f (6 edges), a-b, a-c, b-c, d-e, d-f, e-f (6 edges). Total 12.

H edges: all pairs not in G. H = {a-d, a-e, a-f, b-d, b-e, b-f, c-d, c-e, c-f} = K_{3,3} between {a,b,c} and {d,e,f}. 9 edges. 

H = K_{3,3}. Is H-v bipartite for every v? 

Remove s: H-s = K_{3,3}, bipartite ✓.
Remove a: H-a = K_{2,3} (between {b,c} and {d,e,f}), bipartite ✓.
Remove d: H-d = K_{3,2}, bipartite ✓.

Yes, all bipartite! And the bipartitions are 3-3 (for s removal) or 2-3 / 3-2 (for others). But we need the bipartition to be 3-3 for the K_{3,3} embedding...

Wait, I think I made an error earlier. Let me re-examine. The condition is: G-v has a K_3-factor. G-v = K_6 - (H-v). A K_3-factor of K_6 is 2 disjoint triangles. H-v must not block all K_3-factors.

I said H-v ⊆ K_{3,3}(F) for some factor F, meaning H-v is a subgraph of some K_{3,3}. But H-v = K_{2,3} (when removing a vertex from one side of K_{3,3}). Is K_{2,3} a subgraph of some K_{3,3} on 6 vertices? 

K_{2,3} has bipartition {2 vertices} and {3 vertices}. To embed in K_{3,3}, we need a 3-3 bipartition. We can put the 2 vertices on one side (add 1 more) and 3 on the other, and the 6th vertex on the side with 2. But the 6th vertex has no edges in H-v (it's isolated), so it can go on either side. So yes, K_{2,3} ⊆ K_{3,3}. ✓.

So my earlier analysis was correct that H-v must be bipartite, but I was wrong that H can have at most 7 edges. H = K_{3,3} has 9 edges and H-v is bipartite for all v. So f(7) ≤ 12.

Wait, but I also proved that H can't have chords of C_7. The issue is I was only considering H = C_7 + chords, but H = K_{3,3} is a completely different graph! K_{3,3} is bipartite, so H-v is always bipartite. 

So my earlier proof was flawed. I was too hasty. Let me redo.

The condition is: for every v, H-v is bipartite (and can be embedded in K_{3,3}, but as we saw, any bipartite graph on 6 vertices can be embedded in K_{3,3} by placing isolated vertices appropriately—wait, is that true?).

Actually, a bipartite graph on 6 vertices with bipartition (A, B) where |A| = 4, |B| = 2: can it be embedded in K_{3,3}? K_{3,3} has bipartition (3, 3). If the graph is connected with bipartition (4, 2), we can't re-bipartition it to (3, 3). So it can't be a subgraph of K_{3,3} (since K_{3,3} subgraphs have bipartition ≤ (3,3)).

Hmm, so the condition is: H-v is bipartite with a bipartition of size (≤3, ≤3). Equivalently, H-v is bipartite and has no bipartition with a part of size > 3. For a connected bipartite graph, the bipartition is unique (up to swap), so we need both parts ≤ 3, i.e., both parts exactly 3 (since they sum to 6). For a disconnected graph, we can choose the side of each component, so we need to be able to balance to (3, 3).

So the condition is: for every v, H-v is bipartite and can be 2-colored with 3 vertices of each color.

For H = K_{3,3}: H-v is K_{2,3} or K_{3,2} (connected, bipartition (2,3) or (3,2)). Both parts ≤ 3. ✓. Can embed in K_{3,3}. 

For H = C_7: H-v = P_6, bipartition (3, 3). ✓.

So both work. And K_{3,3} has 9 edges (G has 12), while C_7 has 7 edges (G has 14). So f(7) ≤ 12.

Can we do better than 12? H with 10 edges (G with 11)?

H on 7 vertices with 10 edges, H-v bipartite with (3,3) bipartition for all v. 

H-v bipartite for all v means H is "vertex-bipartite": every odd cycle passes through every vertex. 

With 10 edges on 7 vertices, H has 10 - 7 + 1 = 4 independent cycles (cyclomatic number 4). If H is bipartite, it has no odd cycles, and H-v is always bipartite. So H could be bipartite with 10 edges!

A bipartite graph on 7 vertices with 10 edges: bipartition (3, 4) or (2, 5) etc. Max edges for (3, 4) is 12. So 10 edges is possible.

But we also need: H-v has a (3,3) bipartition for every v. 

If H is bipartite with parts (A, B) where |A| = 3, |B| = 4. Remove v ∈ B: H-v has parts (3, 3). ✓ (bipartition (A, B\{v})). Remove v ∈ A: H-v has parts (2, 4). Need to re-bipartition to (3, 3). If H-v is connected, bipartition is unique (2, 4), can't do (3, 3). ✗.

So if H is bipartite with parts (3, 4) and connected, removing a vertex from the part of size 3 gives (2, 4), which can't be re-bipartitioned to (3, 3) if connected.

If H-v is disconnected, we might re-bipartition. So we need: for every v ∈ A (|A| = 3), H-v is disconnected (or has a (3,3) bipartition).

This is getting complicated. Let me just check: can H have 10 edges?

H bipartite, parts (3, 4), 10 edges. Remove v from A (size 3): H-v has parts (2, 4), 10 - deg(v) edges. For H-v to have a (3,3) bipartition, H-v must be disconnected (so we can flip some components). 

If every vertex in A has the property that removing it disconnects H... With 3 vertices in A, each removal disconnects. This means A is a "cutset" in some sense. 

Actually, this is getting too complicated for the gain (11 vs 12 edges for f(7), saving 1 edge in the recursive formula, giving 197 instead of 198). Let me step back and think about the big picture.

Let me reconsider the recursive formula. 

f(100) ≤ f(m) + 2(100 - m) for m ≡ 1 mod 3.

With the universal vertex construction: f(m) ≤ 3(m-1)/3 + (m-1) = (m-1) + (m-1) = 2(m-1). Wait, let me recompute.

For the universal vertex construction on m vertices (m ≡ 1 mod 3): 1 universal vertex + (m-1)/3 triangles. Edges = (m-1) [universal to all] + 3·(m-1)/3 [triangles] = (m-1) + (m-1) = 2(m-1).

So f(m) ≤ 2(m-1). Then f(100) ≤ 2(m-1) + 2(100-m) = 2m - 2 + 200 - 2m = 198. 

So the recursive formula with the universal vertex construction always gives 198, regardless of m! That's because the universal vertex construction is "self-similar."

So to beat 198, we need f(m) < 2(m-1) for some m ≡ 1 mod 3.

For m = 7: 2(m-1) = 12. We found f(7) ≤ 12 (universal construction). Can we do f(7) < 12, i.e., f(7) ≤ 11?

For m = 10: 2(m-1) = 18. Can we do f(10) ≤ 17?

For m = 13: 2(m-1) = 24. Can we do f(13) ≤ 23?

Let me focus on f(7). Can we achieve 11 edges?

G on 7 vertices, 11 edges, H = complement with 10 edges. Need: for every v, G-v has a K_3-factor, i.e., H-v is bipartite with (3,3) bipartition.

H has 10 edges on 7 vertices. H-v bipartite for all v: H is vertex-bipartite. 

Case 1: H is bipartite. Parts (a, b) with a + b = 7, a·b ≥ 10. (3,4): 12 ≥ 10 ✓. (2,5): 10 ≥ 10 ✓.

Subcase (3, 4): H bipartite with parts A (size 3), B (size 4), 10 edges. Remove v ∈ A: H-v bipartite (2, 4), need (3,3) re-bipartition. H-v must be disconnected. Remove v ∈ B: H-v bipartite (3, 3). ✓.

So need: for every v ∈ A, H-v is disconnected (or has (3,3) bipartition). 

H-v disconnected: v is a cut vertex. So every vertex in A is a cut vertex of H.

H is bipartite (3, 4) with 10 edges and every vertex in the part of size 3 is a cut vertex.

Let A = {a1, a2, a3}, B = {b1, b2, b3, b4}. Each ai is a cut vertex. 

If a1 is a cut vertex, removing it splits H into at least 2 components. The components are subgraphs of H-v, which is bipartite (2, 4). 

Hmm, let me try to construct such H. 

Let H be: a1 connected to b1, b2, b3, b4 (4 edges). a2 connected to b1, b2 (2 edges). a3 connected to b3, b4 (2 edges). a2 connected to b3? No, that would be... let me think. 

Actually, let me try: 
- a1-b1, a1-b2, a1-b3, a1-b4 (a1 connected to all of B)
- a2-b1, a2-b2 (a2 connected to b1, b2)
- a3-b3, a3-b4 (a3 connected to b3, b4)

Total: 4 + 2 + 2 = 8 edges. Need 10. Add a2-b3, a3-b2? That gives 10.

H edges: a1-b1, a1-b2, a1-b3, a1-b4, a2-b1, a2-b2, a2-b3, a3-b2, a3-b3, a3-b4. 10 edges.

Remove a1: H-a1 has edges a2-b1, a2-b2, a2-b3, a3-b2, a3-b3, a3-b4. Is this connected? a2 connects to b1, b2, b3. a3 connects to b2, b3, b4. So a2-b2-a3 and a2-b3-a3 connect them. b1 only connects to a2, b4 only to a3. So the graph is connected (a2-b1, a2-b2-a3-b4, a2-b3-a3). Bipartition: {a2, a3} and {b1, b2, b3, b4}, sizes 2 and 4. Connected, so unique bipartition (2, 4). Can't re-bipartition to (3, 3). ✗.

So this doesn't work. I need H-a1 to be disconnected.

Let me try: a1 is a cut vertex separating {b1, b2} from {b3, b4} (and a2, a3).

H: a1-b1, a1-b2, a1-b3, a1-b4 (a1 to all B). a2-b1, a2-b2 (a2 to b1, b2). a3-b3, a3-b4 (a3 to b3, b4). 8 edges. Need 10 more... wait, 8 edges, need 10. Add a2-b3 and a3-b2? But then removing a1: a2-b1, a2-b2, a2-b3, a3-b2, a3-b3, a3-b4. Connected (as before). 

To make H-a1 disconnected, a2 and a3 must not share any B-neighbor (other than through a1). So a2 connects to subset of B, a3 connects to disjoint subset. 

a2-b1, a2-b2, a3-b3, a3-b4. Plus a1 to all B: a1-b1, a1-b2, a1-b3, a1-b4. 8 edges. Need 10. Add 2 more edges. But any edge between {a2, b1, b2} and {a3, b3, b4} would connect the two components after removing a1. And edges within {a2, b1, b2} or within {a3, b3, b4} would be within a part (bipartite graph, so no edges within a part). 

So the only edges we can add are a2-b1, a2-b2 (already have), a3-b3, a3-b4 (already have), a1-* (already have all). We can add a2-b3? No, that connects the components. a3-b1? Same. 

So with this structure, max edges = 8 (a1 to all 4 B, a2 to 2 B, a3 to 2 B, with a2 and a3's neighborhoods disjoint). Can't reach 10.

Alternatively, make a2 connect to 3 of B and a3 to 1, but disjoint: a2-b1, a2-b2, a2-b3, a3-b4. Plus a1 to all: 4 + 3 + 1 = 8. Still 8. The constraint is a2 and a3 have disjoint B-neighborhoods, so deg(a2) + deg(a3) ≤ 4. Total edges = deg(a1) + deg(a2) + deg(a3) = 4 + deg(a2) + deg(a3) ≤ 4 + 4 = 8.

So with a1 as cut vertex separating a2's side from a3's side, max 8 edges. Not enough for 10.

What if the cut is different? Removing a1 creates components that don't correspond to a2 vs a3?

H is bipartite (3, 4). Removing a1 (from A side), H-a1 is bipartite (2, 4) with parts {a2, a3} and B. For H-a1 to be disconnected, the 2 vertices a2, a3 must be in different components (or one isolated). 

If a2 and a3 are in different components: a2's component has a2 and some subset of B, a3's component has a3 and the rest. No edges between these components (in H-a1). So in H, the only connection between a2's side and a3's side is through a1. 

As computed, this limits edges to 8. Not enough.

If a2 is isolated in H-a1: a2 has no edges except to a1. So deg(a2) = 1 (only a1-a2... but wait, H is bipartite (3,4), a2 ∈ A, a2's neighbors are in B. If a2 is isolated in H-a1, a2's only neighbor is a1? But a1 ∈ A, and H is bipartite, so a2 can't be adjacent to a1. Contradiction. So a2 can't be isolated in H-a1 (a2's neighbors are all in B, and they're all present in H-a1).

So H-a1 can't have a2 isolated. Similarly for a3. So the only way to disconnect is a2 and a3 in different components, limiting to 8 edges.

So subcase (3, 4) with H bipartite can't reach 10 edges while satisfying the condition. Max is 8, giving G with 13 edges. But we already have f(7) ≤ 12, so 13 is worse.

Subcase (2, 5): H bipartite with parts A (size 2), B (size 5), 10 edges. Max edges = 2·5 = 10. So H = K_{2,5}. 

Remove v ∈ A: H-v = K_{1,5}, bipartite (1, 5). Need (3, 3) bipartition. K_{1,5} is connected, unique bipartition (1, 5). Can't re-bipartition to (3, 3). ✗.

So K_{2,5} doesn't work.

Case 2: H is not bipartite but vertex-bipartite (every odd cycle through every vertex).

H has 10 edges, 7 vertices, not bipartite. H-v bipartite for all v. As argued, all odd cycles pass through all 7 vertices. So every odd cycle is a Hamiltonian cycle (length 7). 

H has a 7-cycle. Plus 3 more edges (10 - 7 = 3). These 3 edges are chords of the 7-cycle or additional structure. But each chord creates a smaller odd cycle (as shown earlier), which doesn't pass through all vertices. So no chords allowed. 

So the 3 extra edges must not create odd cycles. But in a 7-cycle, every chord creates an odd cycle. So the extra edges must be... there are no other edges to add (all pairs are either cycle edges or chords). So H can have at most 7 edges if it contains a 7-cycle and no chords. But we need 10. Contradiction.

Wait, H could have multiple 7-cycles (sharing edges). Two 7-cycles share at least... well, they could share many edges. But the union of two 7-cycles has at most 14 edges and at least 7 edges (if they share 7 edges, they're the same cycle). If they share 6 edges, union has 8 edges. If share 5, union has 9. If share 4, union has 10. 

Two 7-cycles sharing 4 edges: union has 10 edges. Do the extra edges (beyond the first 7-cycle) create smaller odd cycles? The second 7-cycle uses 3 edges not in the first. Each of these 3 edges is a "chord" of the first cycle. Each chord creates a smaller odd cycle. But that smaller odd cycle might be part of the second 7-cycle, which is Hamiltonian. Hmm, but the smaller odd cycle (from one chord) has length < 7, so it doesn't pass through all vertices. 

Wait, let me reconsider. A chord {i, j} of C_7 creates two cycles: one of length d+1 and one of length 7-d+1 = 8-d, where d is the shorter path length. One of these is odd (since 7 is odd, d and 7-d have different parities, so d+1 and 8-d have different parities, one is odd). The odd one has length ≤ 7 (could be 3, 5, or 7). If it's 7, the chord connects antipodal... in C_7, d can be 1, 2, 3. d=3: cycles of length 4 and 5. The odd one is 5. d=2: cycles of length 3 and 6. Odd one is 3. d=1: that's a cycle edge, not a chord.

So every chord creates an odd cycle of length 3 or 5, which doesn't pass through all 7 vertices. So H-v for v not on this odd cycle would still contain it, making H-v non-bipartite. ✗.

So H can't have chords, meaning H with a 7-cycle can have at most 7 edges. Not enough for 10.

So Case 2 is impossible for 10 edges.

Therefore, f(7) > 11, i.e., f(7) ≥ 12. And we have f(7) ≤ 12. So f(7) = 12.

Wait, but I need to double-check that f(7) = 12 is achievable. The universal construction gives 12. And I showed 11 is impossible. But let me also check: is there a non-bipartite H with 9 edges that works?

H with 9 edges, G with 12. H = K_{3,3} (bipartite, 9 edges). We verified this works. ✓.

Could H have 10 edges? We showed no. So f(7) = 12. 

Hmm wait, I think I need to be more careful. Let me re-examine whether H with 9 edges but not K_{3,3} could fail, and whether H with 10 edges is truly impossible.

H with 10 edges: I showed bipartite (3,4) can't reach 10 with the condition, bipartite (2,5) = K_{2,5} fails, and non-bipartite can't have 10 edges. So 10 is impossible. ✓.

But what about H with 9 edges that's not K_{3,3}? It doesn't matter for the lower bound; we just need to show H can't have ≥ 10 edges. Since H with 10 is impossible, H ≤ 9, G ≥ 12. ✓.

So f(7) = 12 = 2(7-1). The universal construction is optimal for n=7.

Now let me check f(10). 2(10-1) = 18. Can we beat 18?

f(10): graph on 10 vertices, removing any leaves 9 = 3 triangles. 

H = complement, 45 - |E(G)| edges. Condition: for every v, G-v = K_9 - (H-v) has a K_3-factor (3 disjoint triangles).

A K_3-factor of K_9 is a partition into 3 triples. There are 9!/(3!^3 · 3!) = 280 such partitions. H-v must not block all of them.

This is much harder to analyze. Let me think about constructions.

Universal construction for n=10: 1 universal + 3 triangles. Edges = 9 + 9 = 18. 

Can we do better? Let me think about H = K_{3,3,3} (complete tripartite, parts of size 3). H has 3·3·3 = 27 edges. G = K_10 - K_{3,3,3} has 45 - 27 = 18 edges. Same as universal.

Hmm. What about H = K_{3,3} ∪ K_4? Wait, that's on 10 vertices. K_{3,3} on 6 vertices (9 edges) + K_4 on 4 vertices (6 edges) = 15 edges. G = 45 - 15 = 30 edges. Worse.

What about H being some clever graph with more edges?

For G-v to have a K_3-factor, H-v must be "K_3-factor-avoidable" in K_9. 

Let me think about the maximum H. 

If H is the complement of the universal construction: G = universal + 3 triangles. H = all edges not in G. G edges: s to all 9 (9 edges) + 3 triangles (9 edges) = 18. H = 45 - 18 = 27 edges. H = K_{3,3,3} (complete tripartite with parts = the 3 triangles). 

Is there H with 28 edges (G with 17) that works?

H-v must allow a K_3-factor in K_9 - (H-v). 

Hmm, this is hard. Let me think about it differently.

For the K_3-factor to exist in G-v = K_9 - (H-v), we need a partition of 9 vertices into 3 triples, each triple having no H-edges (i.e., each triple is a triangle in G). So we need a partition into 3 "independent sets" of H (each of size 3). In other words, H-v must have chromatic number ≤ 3 with a specific 3-coloring where each color class has size 3.

Wait, not exactly. We need a partition into 3 independent sets of size 3 in H-v. This is equivalent to H-v being 3-colorable with a specific equitable coloring (each color class size 3).

Actually, it's a partition of the 9 vertices into 3 sets of 3, each being an independent set in H-v. This is a "3×3 equitable coloring" or more precisely, a "perfect 3-coloring" or "resolution into independent sets."

For H = K_{3,3,3} (tripartite): H-v is still tripartite (with parts 3,3,2 or 3,2,3 etc.). A partition into 3 independent sets of size 3: the tripartition itself gives independent sets, but sizes might not be 3,3,3 after removing v. If v is from part 1 (size 3 → 2), parts are (2, 3, 3). We need 3 independent sets of size 3. The parts of size 3 are already independent sets. The part of size 2 needs one more vertex from another part, but that vertex is adjacent (in H) to vertices in the size-2 part (since H is complete tripartite). So we can't just move a vertex. 

Hmm, actually in K_{3,3,3}, two vertices in different parts are adjacent. So an independent set is contained within one part. After removing v from part 1 (parts become 2, 3, 3), the independent sets of size 3 are exactly parts 2 and 3. The remaining 2 vertices (from part 1) plus 1 more must form an independent set, but any vertex from parts 2 or 3 is adjacent to them. So no independent set of size 3 containing a part-1 vertex and a part-2/3 vertex. So we can't partition into 3 independent sets of size 3. 

Wait, that means the universal construction doesn't work?!

Let me re-examine. G = universal s + 3 triangles T_1, T_2, T_3. Remove v from T_1. G-v: s, 2 vertices from T_1, T_2, T_3. K_3-factor: {s, b, c} (b, c from T_1), T_2, T_3. ✓. This works because s-b, s-c, b-c are all edges in G.

In terms of H: H = K_{3,3,3} with parts T_1, T_2, T_3 (and s is... wait, s is universal in G, so s has no H-edges. s is isolated in H). 

Oh, I mislabeled. H = complement of G. G edges: s to all 9, plus triangle edges within T_1, T_2, T_3. H edges: all edges between different T_i's (no s edges in H). So H = K_{3,3,3} on T_1 ∪ T_2 ∪ T_3, and s is isolated in H. H has 27 edges.

H-v: if v ∈ T_1, H-v = K_{2,3,3} (on T_1\{v}, T_2, T_3) + isolated s. We need a partition of 9 vertices (s + T_1\{v} + T_2 + T_3) into 3 independent sets of size 3 in H-v. 

Independent sets in H-v: s is isolated, so s can be with anyone. T_1\{v} (2 vertices) form an independent set (no H-edges within T_1). T_2 (3 vertices) independent. T_3 (3 vertices) independent. 

Partition: {s, b, c} (s + 2 from T_1\{v}), T_2, T_3. Is {
