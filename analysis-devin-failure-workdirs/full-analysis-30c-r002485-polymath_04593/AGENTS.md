# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Given an integer \( n \geq 6 \), find the least integer \( m(n) \) such that for any graph \( G \) with \( n \) vertices and \( m(n) \) edges, there must exist two vertex-disjoint cycles in \( G \).       — 题目文本
#   To determine the least integer \( m(n) \) such that any graph \( G \) with \( n \) vertices and \( m(n) \) edges must contain two vertex-disjoint cycles, we need to understand the maximum number of edges a graph can have without containing two vertex-disjoint cycles.

### Step-by-Step Solution:

1. **Identify the Extremal Graph:**
   - Consider a graph \( G \) with \( n \) vertices. To avoid having two vertex-disjoint cycles, the graph must be structured in such a way that all cycles share at least one common vertex.
   - A known result in extremal graph theory states that the maximum number of edges in an \( n \)-vertex graph without two vertex-disjoint cycles is \( 3n - 6 \).

2. **Constructing the Extremal Graph:**
   - The extremal graph can be constructed by taking a complete graph \( K_5 \) (which has 10 edges) and connecting each of the remaining \( n-5 \) vertices to all 5 vertices of \( K_5 \). This structure ensures that any cycle must include at least one vertex from the \( K_5 \), preventing the formation of two vertex-disjoint cycles.
   - The total number of edges in this graph is \( 10 + 5(n-5) = 5n - 15 \).

3. **Adjusting for \( n \geq 6 \):**
   - For \( n \geq 6 \), the maximum number of edges without two vertex-disjoint cycles is \( 3n - 6 \). This is derived from the structure where all cycles must share a common vertex or a small subset of vertices.

4. **Determine \( m(n) \):**
   - To ensure that any graph with \( m(n) \) edges must contain two vertex-disjoint cycles, we take \( m(n) \) to be one more than the maximum number of edges without two vertex-disjoint cycles.
   - Therefore, \( m(n) = (3n - 6) + 1 = 3n - 5 \).

### Conclusion:
The least integer \( m(n) \) such that any graph \( G \) with \( n \) vertices and \( m(n) \) edges must contain two vertex-disjoint cycles is given by:

\[
\boxed{3n - 5}
\]  — 标准解答
#   The problem asks for the least integer m(n) such that any graph with n vertices and m(n) edges must contain two vertex-disjoint cycles.

This is a classic extremal graph theory problem. Let me think about it.

The answer is m(n) = n+1 for n ≥ 6.

Wait, let me think more carefully. The question is about the minimum number of edges that forces two vertex-disjoint cycles.

Let me recall the Erdős-Pósa type results. Actually, this is a specific result.

The extremal number for two vertex-disjoint cycles: we want the maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles, then m(n) = that + 1.

A graph with no two vertex-disjoint cycles: by the Erdős-Pósa theorem (or more specifically, the structure of graphs without two disjoint cycles), such graphs have a specific structure.

Let me think about what graphs have no two vertex-disjoint cycles.

First, let's think about the maximum number of edges. 

Consider a graph where all cycles share a common vertex. For instance, take a "friendship graph" or a "wheel-like" structure. Actually, let me think about the structure more carefully.

If a graph has no two vertex-disjoint cycles, then by a theorem (this is related to the Erdős-Pósa theorem with k=2), the graph has a small vertex set hitting all cycles... actually no, that's not quite right either.

Let me think about this differently. Let me consider the extremal construction.

Construction: Take a complete graph K_5 on 5 vertices, and attach the remaining n-5 vertices as a tree (or as leaves hanging off). Actually, let me think about what maximizes edges while avoiding two disjoint cycles.

If we have K_5, it has 10 edges. K_5 has no two vertex-disjoint cycles (since any two cycles in K_5 must share a vertex — K_5 has 5 vertices, two disjoint cycles would need at least 6 vertices). 

Now attach n-5 more vertices. To maximize edges, we can connect each new vertex to all 5 vertices of the K_5. But wait, if we connect a new vertex v to two vertices of K_5, then v together with an edge of K_5 forms a triangle, and the remaining 4 vertices of K_5 form a K_4 which contains a cycle. So we'd have two disjoint cycles.

So we can't connect new vertices too freely. Let me think...

If we connect a new vertex v to exactly one vertex of K_5, that's like a pendant. We can build a tree on the n-5 new vertices plus connect them to one vertex of K_5. That gives a tree-like structure attached to K_5.

Actually, let me reconsider. The extremal graph for "no two vertex-disjoint cycles" — let me think about what structure maximizes edges.

Claim: The maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles is n+1, achieved by... hmm, let me think.

Actually wait. Let me reconsider. K_5 has 10 edges and 5 vertices. If n=5, K_5 has no two disjoint cycles. For n ≥ 6, we need to add vertices.

Let me think about n=6. We need m(6) such that any graph on 6 vertices with m(6) edges has two disjoint cycles. 

K_5 plus one vertex: if the 6th vertex connects to 0 vertices of K_5, we have 10 edges, no two disjoint cycles (since only 5 vertices are in cycles). If it connects to 1 vertex, still 11 edges, the 6th vertex is a pendant, no new cycle. If it connects to 2 vertices of K_5, then we get a triangle (v, a, b) where ab is an edge of K_5, and the remaining 3 vertices of K_5 form a triangle. So two disjoint cycles! That's 12 edges.

But can we do better than K_5 + pendant? What about K_4 plus two vertices? K_4 has 6 edges, 4 vertices. Add two vertices each connected to one vertex of K_4: 8 edges. Or connect them to each other and to K_4 in a way that avoids two disjoint cycles.

Hmm, let me think about the general structure.

Theorem (I believe this is a known result): The maximum number of edges in a graph on n ≥ 5 vertices with no two vertex-disjoint cycles is n+1, so m(n) = n+2.

Wait, let me recompute. K_5 has 10 = 5+5 edges. Hmm, that doesn't match n+1.

Let me reconsider. For n=5: K_5 has 10 edges and no two disjoint cycles. So the max for n=5 is at least 10. n+1 = 6, that's way less. So the formula n+1 is wrong.

Let me reconsider the problem. The problem says n ≥ 6.

For n=6: What's the max edges with no two disjoint cycles?

K_5 + 1 isolated vertex: 10 edges, 6 vertices. No two disjoint cycles (only 5 vertices participate in cycles).

K_5 + 1 pendant vertex (connected to one K_5 vertex): 11 edges, 6 vertices. Still no two disjoint cycles.

Can we get 12 edges? If the 6th vertex connects to 2 vertices of K_5, we get two disjoint cycles as I argued. So with K_5-based construction, max is 11.

But maybe there's a different construction with more edges? 

What about K_{3,3}? That has 9 edges, 6 vertices, and contains two disjoint 4-cycles? Actually K_{3,3} — does it have two vertex-disjoint cycles? K_{3,3} has a Hamiltonian cycle (6-cycle). Can we find two disjoint cycles? A 4-cycle uses 4 vertices, leaving 2, not enough for another cycle. Two 3-cycles? K_{3,3} is bipartite, so no odd cycles. So the smallest cycles are 4-cycles. Two 4-cycles need 8 vertices, we only have 6. So K_{3,3} has no two vertex-disjoint cycles! And it has 9 edges.

So K_{3,3} gives 9 edges for n=6, less than K_5 + pendant's 11.

What about other constructions? Take K_4 (4 vertices, 6 edges) and add two vertices. Connect each to all 4 vertices of K_4? That's 6 + 8 = 14 edges but would definitely have two disjoint cycles.

Let me think about the structure of graphs without two disjoint cycles more carefully.

A graph has no two vertex-disjoint cycles if and only if... by the Erdős-Pósa theorem, for k=2, either there's a small set of vertices hitting all cycles, or there are few disjoint cycles. Actually the Erdős-Pósa theorem says there's a function f(k) such that either there are k disjoint cycles or a set of f(k) vertices hitting all cycles. For k=2, f(2) = 3 (I think).

So a graph with no two disjoint cycles either has a feedback vertex set of size ≤ 3 (a set of 3 vertices whose removal makes the graph a forest).

If there's a feedback vertex set S of size ≤ 3, then G - S is a forest. The number of edges is at most C(|S|,2) + |S|*(n-|S|) + (n-|S|-1) = ... wait, let me be more careful.

If |S| = s, then G-S is a forest on n-s vertices, so has at most n-s-1 edges. The edges within S: at most C(s,2). The edges between S and the rest: at most s*(n-s). Total: C(s,2) + s*(n-s) + (n-s-1).

For s=3: C(3,2) + 3*(n-3) + (n-4) = 3 + 3n-9 + n-4 = 4n - 10.

For s=2: C(2,2) + 2*(n-2) + (n-3) = 1 + 2n-4 + n-3 = 3n - 6.

For s=1: 0 + (n-1) + (n-2) = 2n - 3.

For s=0: n-1 (just a forest, but a forest has no cycles at all, so trivially no two disjoint cycles).

So the maximum is achieved at s=3: 4n - 10.

But wait, can we actually achieve 4n-10? We need:
- S is a clique of size 3 (3 edges)
- Every vertex outside S is connected to all 3 vertices of S (3(n-3) edges)
- G-S is a tree on n-3 vertices (n-4 edges)

Total: 3 + 3(n-3) + (n-4) = 3 + 3n - 9 + n - 4 = 4n - 10.

Does this graph have no two vertex-disjoint cycles? Let's check. Any cycle must use at least one vertex of S (since G-S is a forest). Actually, any cycle must use at least one vertex of S. But two cycles could each use one vertex of S (different vertices), and they'd be disjoint if they don't share vertices outside S either.

Wait, let me reconsider. If S = {a, b, c} is a triangle, and every outside vertex is connected to all of a, b, c, and the outside vertices form a tree.

Consider two outside vertices u, v connected by an edge in the tree. Then u-a-v is a path... wait, u and v are both connected to a. So u-a-v-u? No, we need u-v edge (yes, tree edge) and u-a, v-a edges (yes). So {u, v, a} forms a triangle. Similarly {u, v, b} and {u, v, c} form triangles.

Now, can we find two disjoint cycles? Take triangle {u, v, a} and triangle {w, x, b} where w, x are two other outside vertices connected by a tree edge. These are disjoint if {u,v} ∩ {w,x} = ∅ and a ≠ b. 

So if n-3 ≥ 4 (i.e., n ≥ 7), we can find two disjoint tree edges (u,v) and (w,x) that are vertex-disjoint, and form triangles {u,v,a} and {w,x,b} which are disjoint. So this construction fails for n ≥ 7!

For n = 6: n-3 = 3, so G-S is a tree on 3 vertices (a path of length 2, say u-v-w). The tree edges are (u,v) and (v,w). We can form triangle {u,v,a} and triangle {v,w,b} but these share vertex v. Can we form two disjoint cycles? {u,v,a} uses {u,v,a}, remaining vertices are {w, b, c}. Is there a cycle on {w, b, c}? w-b, w-c, b-c are all edges (since b,c ∈ S form a triangle, and w is connected to all of S). So {w, b, c} is a triangle! And {u, v, a} is a triangle. These are disjoint! So for n=6, this construction also has two disjoint cycles.

Hmm, so the s=3 construction doesn't work as I thought. The issue is that even with a feedback vertex set of size 3, we can still have two disjoint cycles.

Let me reconsider. The Erdős-Pósa theorem says: either k disjoint cycles OR a set of f(k) vertices hitting all cycles. The contrapositive: if no k disjoint cycles, then there's a set of f(k) vertices hitting all cycles. For k=2, f(2) = 3 means: if no 2 disjoint cycles, there's a set of ≤ 3 vertices hitting all cycles.

But having a feedback vertex set of size 3 doesn't prevent two disjoint cycles — it's the other direction. The feedback vertex set of size 3 is a consequence of no two disjoint cycles, not equivalent to it.

So the structure is: no two disjoint cycles ⟹ feedback vertex set of size ≤ 3. But the converse isn't true.

So I need to think about this more carefully. The maximum edges is achieved by some graph with no two disjoint cycles, which must have a feedback vertex set of size ≤ 3, but the constraint is stronger.

Let me think about what graphs on n vertices with no two disjoint cycles look like.

Case 1: Feedback vertex set of size 1, say {v}. Then G - v is a forest. Any cycle goes through v. Two cycles through v share v, so they're not vertex-disjoint. So any graph with a feedback vertex set of size 1 has no two vertex-disjoint cycles. Max edges: v connects to all n-1 others (n-1 edges), plus G-v is a tree (n-2 edges). Total: 2n - 3. But we can also add edges within the neighborhood... wait, no. G - v must be a forest. So edges not involving v: at most n-2. Edges involving v: at most n-1. Total: 2n - 3.

But wait, we could also have v not connected to all vertices. The point is G-v is a forest and v can connect to anyone. Max is 2n-3.

Case 2: Feedback vertex set of size 2, say {a, b}. G - {a,b} is a forest. But we need the additional constraint that there are no two disjoint cycles.

If G - {a,b} is a forest on n-2 vertices, cycles must use a or b. A cycle using only a (from {a,b}) and some forest vertices: this requires a path in the forest between two neighbors of a. Similarly for b.

Two disjoint cycles: one using a (not b) and one using b (not a), with disjoint forest vertices. Or one using both a and b, and another using... well, both cycles need to use at least one of {a,b}, and if they're disjoint, one uses a and the other uses b (they can't both use the same vertex).

So: cycle C1 uses a but not b, cycle C2 uses b but not a, and they're vertex-disjoint (including in the forest part).

To prevent this, we need: for any partition of the forest into two parts, it's not the case that both parts contain a cycle through a (resp. b).

Hmm, this is getting complicated. Let me think about specific constructions.

Actually, let me look at this from a different angle. Let me think about what's known.

I recall that the answer to this problem is m(n) = n + 1 for n ≥ 6. Let me verify this.

Wait, but K_5 has 10 edges for n=5, and 10 > 5+1 = 6. So for n=5, the answer would be different. The problem specifies n ≥ 6.

For n=6: Is m(6) = 7? That seems too low. K_5 + isolated vertex has 10 edges and no two disjoint cycles. So m(6) > 10. So m(6) ≠ 7.

Let me reconsider. Maybe the answer is different.

Let me think about the maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles.

For n=6: K_5 + pendant has 11 edges. Can we do 12? As I argued, connecting the 6th vertex to 2 vertices of K_5 creates two disjoint triangles. What about a non-K_5-based construction?

What about K_4 + 2 extra vertices? K_4 has 4 vertices, 6 edges. Add vertex u connected to all 4 K_4 vertices (4 edges), add vertex v connected to all 4 K_4 vertices (4 edges), and u-v edge (1 edge). Total: 6+4+4+1 = 15 edges. But this definitely has two disjoint cycles (e.g., triangle from K_4 and triangle u-v-a for some a in K_4).

Let me be more careful. What about K_4 + 2 pendant vertices? 6 + 2 = 8 edges. Less than 11.

What about two K_3's sharing a vertex? That's 5 vertices, 6 edges. Add a 6th vertex as pendant: 7 edges. Less than 11.

What about K_5 with one edge subdivided? Take K_5, remove edge (a,b), add vertex v connected to a and b. That's 10 - 1 + 2 = 11 edges, 6 vertices. Does this have two disjoint cycles? The cycles in K_5 - {a,b} edge plus v... v-a-c-b-v is a 4-cycle (if a-c, c-b are edges, which they are in K_5). The remaining vertices are {d, e} (the other two K_5 vertices). {d, e} alone can't form a cycle. So no two disjoint cycles here? Let me check more carefully.

Vertices: a, b, c, d, e, v. Edges: all K_5 edges except (a,b), plus (v,a) and (v,b). So edges: (a,c), (a,d), (a,e), (b,c), (b,d), (b,e), (c,d), (c,e), (d,e), (v,a), (v,b). That's 11 edges.

Cycles: {c,d,e} is a triangle. {a,c,d} is a triangle. {v,a,c,b,v} is a 4-cycle (v-a-c-b-v, using edges v-a, a-c, c-b, b-v). 

Can we find two disjoint cycles? Triangle {c,d,e} uses {c,d,e}. Remaining: {a, b, v}. Edges among them: (v,a), (v,b). No (a,b). So {a,b,v} has only 2 edges, no cycle. 

Triangle {a,c,d} uses {a,c,d}. Remaining: {b,e,v}. Edges: (b,e), (v,b). No (v,e). Only 2 edges, no cycle.

4-cycle {v,a,c,b}: uses {v,a,c,b}. Remaining: {d,e}. Edge (d,e). No cycle.

What about 4-cycle {v,a,d,b}? v-a, a-d, d-b, b-v. Yes. Uses {v,a,d,b}. Remaining: {c,e}. Edge (c,e). No cycle.

4-cycle {v,a,e,b}? v-a, a-e, e-b, b-v. Uses {v,a,e,b}. Remaining: {c,d}. Edge (c,d). No cycle.

What about longer cycles? 5-cycle using 5 of 6 vertices, leaving 1 vertex, can't have two disjoint cycles.

So this graph has 11 edges and no two disjoint cycles. Same as K_5 + pendant.

Can we get 12 edges on 6 vertices with no two disjoint cycles? Let me think...

With 12 edges on 6 vertices, the complement has 15 - 12 = 3 edges. 

Hmm, let me think about this more systematically. The complete graph K_6 has 15 edges. We need to remove at least 3 edges (to get 12) and check if two disjoint cycles are forced.

Actually, let me think about it differently. With 6 vertices, two disjoint cycles must be either:
- Two triangles (using all 6 vertices)
- A triangle and a 4-cycle (needs 7 vertices, impossible with 6)
- Two 4-cycles (needs 8 vertices, impossible)

So with 6 vertices, the only way to have two vertex-disjoint cycles is two disjoint triangles partitioning all 6 vertices.

So the question for n=6 is: what's the maximum number of edges in a graph on 6 vertices with no two disjoint triangles (partitioning the vertex set)?

A graph on 6 vertices has no partition into two triangles. The complement has 3 edges (for 12-edge graph). 

Two disjoint triangles partition {1,...,6} into {a,b,c} and {d,e,f}. This requires all 9 edges: 3 within each triangle and... no, just 3+3 = 6 edges (the triangle edges). The two triangles need 6 edges total.

So a 12-edge graph on 6 vertices: does it always contain two disjoint triangles? 

Hmm, not necessarily. Consider K_6 minus a perfect matching (3 edges removed). That's 12 edges. Does it have two disjoint triangles? K_6 minus a perfect matching: vertices 1,2,3,4,5,6 with missing edges (1,2), (3,4), (5,6). 

Triangle {1,3,5}: edges (1,3), (1,5), (3,5) — all present. Triangle {2,4,6}: edges (2,4), (2,6), (4,6) — all present. These are disjoint! So yes, two disjoint triangles.

What about K_6 minus a star (3 edges from one vertex)? Missing edges: (1,2), (1,3), (1,4). 12 edges. Triangle {2,3,4}: edges (2,3),(2,4),(3,4) — present. Triangle {1,5,6}: needs (1,5),(1,6),(5,6) — (1,5) and (1,6) are present (only (1,2),(1,3),(1,4) missing), (5,6) present. So {1,5,6} is a triangle. Disjoint from {2,3,4}. Yes!

What about K_6 minus a path of 3 edges? Missing: (1,2),(2,3),(3,4). 12 edges. Triangle {1,3,5}: (1,3) present, (1,5) present, (3,5) present. Yes. Triangle {2,4,6}: (2,4) present, (2,6) present, (4,6) present. Yes. Disjoint!

What about K_6 minus a triangle? Missing: (1,2),(2,3),(1,3). 12 edges. Triangle {1,4,5}: (1,4),(1,5),(4,5) all present. Triangle {2,3,6}: (2,3) is MISSING. So {2,3,6} is not a triangle. Try {2,4,6}: (2,4),(2,6),(4,6) all present. And {1,3,5}: (1,3) MISSING. Try {3,4,5}: (3,4),(3,5),(4,5) all present. And {1,2,6}: (1,2) MISSING. 

Hmm, let me be more systematic. Missing edges: (1,2), (2,3), (1,3). So vertex 1 is not connected to 2 or 3, and 2 is not connected to 3. 

Triangles containing vertex 1: must use two of {4,5,6}. {1,4,5}, {1,4,6}, {1,5,6} — all are triangles (since 1 is connected to 4,5,6 and those are all mutually connected).

Triangles containing vertex 2 but not 1: must use two of {4,5,6} (since 2 is not connected to 1 or 3). {2,4,5}, {2,4,6}, {2,5,6} — all triangles.

Triangles containing vertex 3 but not 1 or 2: must use two of {4,5,6}. {3,4,5}, {3,4,6}, {3,5,6} — all triangles.

Now, two disjoint triangles partitioning {1,...,6}:
- {1,4,5} and {2,3,6}: {2,3,6} needs (2,3) — missing. No.
- {1,4,6} and {2,3,5}: {2,3,5} needs (2,3) — missing. No.
- {1,5,6} and {2,3,4}: {2,3,4} needs (2,3) — missing. No.
- {2,4,5} and {1,3,6}: {1,3,6} needs (1,3) — missing. No.
- {2,4,6} and {1,3,5}: {1,3,5} needs (1,3) — missing. No.
- {2,5,6} and {1,3,4}: {1,3,4} needs (1,3) — missing. No.
- {3,4,5} and {1,2,6}: {1,2,6} needs (1,2) — missing. No.
- {3,4,6} and {1,2,5}: {1,2,5} needs (1,2) — missing. No.
- {3,5,6} and {1,2,4}: {1,2,4} needs (1,2) — missing. No.

So K_6 minus a triangle (12 edges) has NO two disjoint triangles, hence no two vertex-disjoint cycles! 

So for n=6, we can have 12 edges without two disjoint cycles. Can we have 13?

K_6 minus 2 edges (13 edges). Missing edges: say (1,2) and (1,3). 

Triangles: {2,3,4}, {2,3,5}, {2,3,6} are all triangles. {1,4,5}, {1,4,6}, {1,5,6} are all triangles.

Disjoint partition: {1,4,5} and {2,3,6}: (1,4),(1,5),(4,5) present; (2,3),(2,6),(3,6) present. Yes! Two disjoint triangles.

What if missing edges are (1,2) and (3,4)? 
{1,3,5} and {2,4,6}: (1,3) present, (1,5) present, (3,5) present — triangle. (2,4) present, (2,6) present, (4,6) present — triangle. Disjoint! Yes.

What if missing edges are (1,2) and (1,3)? Already checked above, has two disjoint triangles.

It seems like with 13 edges (missing only 2), we always get two disjoint triangles. Let me check the case missing (1,2) and (4,5):
{1,3,4} and {2,5,6}: (1,3) present, (1,4) present, (3,4) present — triangle. (2,5) present, (2,6) present, (5,6) present — triangle. Disjoint! Yes.

Missing (1,2) and (5,6):
{1,3,5} and {2,4,6}: (1,3),(1,5),(3,5) present; (2,4),(2,6),(4,6) present. Disjoint triangles!

It seems like any 13-edge graph on 6 vertices has two disjoint triangles. Let me try to prove this.

With 13 edges, 2 edges missing. The two missing edges involve at most 4 vertices. So at least 2 vertices are "complete" (connected to all others). 

Case 1: The two missing edges share a vertex, say (1,2) and (1,3) missing. Then vertices 4,5,6 are complete. {4,5,6} is a triangle. We need a triangle in {1,2,3}. But (1,2) and (1,3) are missing, so the only possible edge in {1,2,3} is (2,3). Not a triangle. So {4,5,6} and a triangle in {1,2,3} doesn't work. But we can use other partitions: {1,4,5} and {2,3,6}. (1,4),(1,5),(4,5) present; (2,3),(2,6),(3,6) present. Yes, disjoint triangles!

Case 2: The two missing edges are disjoint, say (1,2) and (3,4) missing. Vertices 5,6 are complete. {1,3,5} and {2,4,6}: all edges present. Disjoint triangles!

So in all cases, 13 edges on 6 vertices forces two disjoint triangles. 

So for n=6: max edges without two disjoint cycles is 12, and m(6) = 13.

Hmm wait, but I should double-check that 12 is achievable. I showed K_6 minus a triangle works. Let me also check: is there a 12-edge graph that does have two disjoint cycles? Of course, many do. The question is whether ALL 12-edge graphs have two disjoint cycles, and I showed one that doesn't (K_6 minus a triangle). So m(6) = 13.

Now, 13 = 2*6 + 1. Hmm, or 13 = 6 + 7. Let me think about the pattern.

Actually, let me reconsider. For general n, what's the maximum number of edges in a graph with no two vertex-disjoint cycles?

Let me think about the construction that generalizes K_6 minus a triangle. 

K_6 minus a triangle: Take K_3 on vertices {1,2,3} (but remove all 3 edges of this triangle), and K_3 on vertices {4,5,6} (keep all edges), plus all edges between {1,2,3} and {4,5,6}. So it's K_{3,3} ∪ K_3 (on the second part). Edges: 9 (bipartite) + 3 (triangle) = 12. 

Wait, that's K_{3,3} plus a triangle on one side. The independent set {1,2,3} has no internal edges, and {4,5,6} is a clique. Plus all cross edges.

Does this have two disjoint cycles? Any cycle must use at least 2 vertices from {4,5,6} (since {1,2,3} is independent). Actually, a cycle could use vertices from both sides. A triangle needs at least 2 from the clique side (since the independent side has no edges). Actually, a triangle in this graph: must have at least 2 vertices from {4,5,6} (clique) since {1,2,3} is independent. A triangle with 2 clique vertices and 1 independent vertex: {i, a, b} where i ∈ {1,2,3}, a,b ∈ {4,5,6}. A triangle with 3 clique vertices: {4,5,6}.

Two disjoint triangles: one uses ≥2 clique vertices, the other uses ≥2 clique vertices. But there are only 3 clique vertices, so they can't be disjoint. 

What about a triangle and a 4-cycle? Triangle uses ≥2 from clique, 4-cycle uses ≥2 from clique (a 4-cycle in a bipartite-like graph needs at least 2 from each side, but here the clique side has internal edges). Actually, a 4-cycle could be i-a-j-b-i where i,j ∈ {1,2,3} and a,b ∈ {4,5,6}. This uses 2 clique vertices. A triangle uses ≥2 clique vertices. Total ≥4 clique vertices needed, but only 3 available. So no two disjoint cycles.

Great, so this construction works for n=6 with 12 edges.

Now let me generalize. For general n, consider: take a clique K_k and an independent set I of size n-k, with all edges between them. This is a "split graph." 

Edges: C(k,2) + k*(n-k).

Cycles: any cycle needs at least 2 clique vertices (since I is independent). Two disjoint cycles need at least 4 clique vertices total (2 each). So if k ≤ 3, no two disjoint cycles.

For k=3: edges = 3 + 3*(n-3) = 3n - 6.

For k=2: edges = 1 + 2*(n-2) = 2n - 3.

For k=1: edges = 0 + (n-1) = n - 1.

So the split graph with k=3 gives 3n-6 edges and no two disjoint cycles.

For n=6: 3*6 - 6 = 12. Matches!

But can we do better than the split graph? Let me think...

What if instead of an independent set, we have a forest (or tree) on the non-clique vertices?

Take a clique K_3 = {a,b,c} and a tree T on n-3 vertices, with all edges between K_3 and T. Edges: 3 + 3*(n-3) + (n-4) = 3 + 3n - 9 + n - 4 = 4n - 10.

Does this have two disjoint cycles? A cycle can be:
- Within K_3: triangle {a,b,c}
- Using 2 K_3 vertices and a path in T: e.g., a-u-b-a where u is a T vertex adjacent to both a and b (which it is, since all cross edges exist). So {a,u,b} is a triangle for any u in T.
- Using 1 K_3 vertex and a path in T: a-u-v-a where u-v is a T edge and a is connected to both u and v (yes). So {a,u,v} is a triangle.
- Using 2 K_3 vertices and 2 T vertices: a-u-v-b-a, a 4-cycle.
- Etc.

Two disjoint cycles: {a,b,c} (triangle) and a cycle in T ∪ (remaining). But T is a tree, so no cycle in T alone. A cycle using 1 K_3 vertex: but all K_3 vertices are used by {a,b,c}. So if one cycle is {a,b,c}, the other must be entirely in T, which is impossible (T is a tree).

What about two cycles each using some K_3 vertices? E.g., {a, u, v} (triangle, uses a and T vertices u,v) and {b, w, x} (triangle, uses b and T vertices w,x). These are disjoint if {u,v} ∩ {w,x} = ∅. This requires 4 distinct T vertices. So if n-3 ≥ 4, i.e., n ≥ 7, we can find two disjoint triangles!

So for n ≥ 7, this construction (K_3 + tree with all cross edges) has two disjoint cycles. It only works for n = 6 (where n-3 = 3, so we can't find 4 distinct T vertices, and also can't find two disjoint pairs).

Wait, for n=6, T has 3 vertices. Two disjoint triangles each using 1 K_3 vertex need 4 T vertices, impossible. Two disjoint triangles each using 2 K_3 vertices need 4 K_3 vertices, impossible. One triangle using 3 K_3 vertices ({a,b,c}) and one cycle in T: impossible. One triangle using 2 K_3 vertices (say {a,b,u}) and one cycle using 1 K_3 vertex (say {c, v, w}): {c,v,w} is a triangle if v-w is a T edge. {a,b,u} is a triangle. Disjoint if u ∉ {v,w}. T has 3 vertices, so we can pick u, v, w with v-w a T edge and u different. E.g., T = path 1-2-3. u=3, v=1, w=2. {a,b,3} and {c,1,2}. Both triangles, disjoint! 

Wait, so for n=6, the K_3 + tree construction with 4*6-10 = 14 edges has two disjoint cycles? Let me recheck.

K_3 = {a,b,c}, T = path on {1,2,3} with edges (1,2),(2,3). All cross edges present. Total edges: 3 (K_3) + 9 (cross) + 2 (tree) = 14.

Triangle {a,b,3}: edges (a,b), (a,3), (b,3) — all present. Yes.
Triangle {c,1,2}: edges (c,1), (c,2), (1,2) — all present. Yes.
These are disjoint: {a,b,3} ∩ {c,1,2} = ∅. Yes!

So 14 edges on 6 vertices with two disjoint cycles. But we already knew m(6) = 13, so 14 > 13, consistent.

But the question is: can we beat 3n-6 for general n? The split graph with k=3 gives 3n-6. Can we add some edges to the independent set without creating two disjoint cycles?

If we add one edge to the independent set (making it have one edge), say edge (u,v) in I. Then {a,u,v} is a triangle (a ∈ K_3, u,v ∈ I, edges a-u, a-v, u-v all present). Now, can we find a disjoint cycle? {b,c,w} for any w ∈ I \ {u,v} is a triangle (b-c, b-w, c-w all present). If n-3 ≥ 3, i.e., n ≥ 6, there exists w. So {a,u,v} and {b,c,w} are disjoint triangles. So adding even one edge to I creates two disjoint cycles (for n ≥ 6).

Wait, for n=6: I has 3 vertices. Adding edge (1,2). {a,1,2} is a triangle. {b,c,3} is a triangle. Disjoint. Yes, two disjoint cycles. So we can't add any edge to I for n=6.

What about adding edges within K_3? It's already a clique, so no more edges to add.

What about not having all cross edges? If we remove some cross edges, we lose edges, so that doesn't help.

So for the split graph construction, 3n-6 is the max. But maybe there's a completely different construction?

Let me think about other structures. What about K_4 minus an edge (a "diamond") as the core?

Take a diamond D = K_4 - e on 4 vertices {a,b,c,d} with missing edge (a,b). Edges: 5. Add n-4 vertices as an independent set I with all cross edges to D. Edges: 5 + 4*(n-4). 

Does this have two disjoint cycles? Cycles in D: {a,c,d} (triangle), {b,c,d} (triangle), {a,c,b,d,a} (4-cycle). 

Two disjoint cycles: {a,c,d} and a cycle using b and I vertices. {b, u, v} for u,v ∈ I: but I is independent, so need b-u, b-v, u-v. u-v is not an edge. So {b,u,v} is not a triangle. 

A 4-cycle: b-u-a-v-b? b-u (yes), u-a (yes), a-v (yes), v-b (yes). This is a 4-cycle using {b,u,a,v}. Disjoint from {c,d,...}? {a,c,d} uses a, so not disjoint from the 4-cycle. 

Hmm, let me think differently. {c,d} is an edge. {c,d,u} is a triangle for any u ∈ I (c-u, d-u, c-d all present). {a,b,v} — a-b is not an edge, so not a triangle. {a,v,w} for v,w ∈ I — v-w not an edge. 

So triangles are: {a,c,d}, {b,c,d}, {c,d,u} for u ∈ I, {a,c,u}, {a,d,u}, {b,c,u}, {b,d,u} for u ∈ I. And 4-cycles, etc.

Two disjoint triangles: {a,c,d} and {b,?,?} — need two I vertices with an edge, but I is independent. Or {b,c,u} and {a,d,v} — these share no vertices if u ≠ v. {b,c,u}: b-c, c-u, b-u all present. {a,d,v}: a-d, d-v, a-v all present. Disjoint if u ≠ v and {b,c} ∩ {a,d} = ∅ (yes). So if |I| ≥ 2, i.e., n ≥ 6, we have two disjoint triangles!

So the diamond construction fails for n ≥ 6. For n=6, |I|=2, and {b,c,u} and {a,d,v} with u≠v gives two disjoint triangles.

What if we don't have all cross edges? Then we have fewer edges, not helpful.

Let me try another approach. What about K_5-based constructions for general n?

K_5 on {a,b,c,d,e} with 10 edges. Add n-5 vertices. To avoid two disjoint cycles, we need to be careful.

If we add a vertex v connected to only one K_5 vertex, say a, then v is a pendant. No new cycles through v. We can build a tree on the n-5 new vertices, all connected to a. Edges: 10 + (n-5) [tree edges] + (n-5) [connections to a, but the tree already includes a... wait.

Let me be more precise. Take K_5 on {a,b,c,d,e}. Add a tree T on {a, v_1, ..., v_{n-5}} where a is one vertex of the tree. The tree has n-5 edges (connecting the new vertices to the tree including a). Total edges: 10 + (n-5) = n + 5.

Does this have two disjoint cycles? Any cycle is either within K_5 or uses some tree vertices. A cycle using tree vertices must use at least 2 tree edges (to leave and return to K_5). Actually, a cycle through tree vertices: v_i - ... - v_j - (K_5 path) - v_i. This requires two connections from tree to K_5, but the tree only connects to K_5 through vertex a. So any cycle through tree vertices must pass through a twice, which isn't possible in a simple cycle. 

Wait, actually: the tree is on {a, v_1, ..., v_{n-5}}. The only vertex shared with K_5 is a. So any cycle either is entirely within K_5, or passes through a (entering the tree and coming back). But a cycle passing through a and tree vertices: a - v_i - ... - v_j - a. This is a cycle if there's a path from v_i to v_j in the tree not through a, and both v_i and v_j are connected to a. But in a tree, the path from v_i to v_j is unique. If it doesn't go through a, then a-v_i-...-v_j-a is a cycle. But this cycle uses a and some tree vertices.

Two disjoint cycles: one in K_5 (not using a) and one through a and tree vertices. K_5 - a = K_4 on {b,c,d,e}, which has cycles. So {b,c,d} (triangle) and {a, v_i, ..., v_j, a} (cycle through tree). These are disjoint if the tree cycle doesn't use b,c,d,e (it doesn't, it only uses a and tree vertices). So yes, two disjoint cycles!

So this construction fails. The issue is that K_5 - a still has cycles.

What if we use K_5 but make sure that removing any single vertex from K_5 leaves no cycle? That's impossible since K_5 - v = K_4 which has cycles.

So the K_5-based construction with a tree attached through one vertex doesn't work because K_5 minus that vertex still has cycles.

What if we attach the tree through a vertex whose removal from K_5 leaves a tree? K_5 minus any vertex is K_4, which is not a tree. So this doesn't work.

What if we use a different core? Let me think about what cores work.

We need a graph H such that:
1. H has no two disjoint cycles.
2. We can attach a tree to H through a single vertex v, such that H - v has no cycles (i.e., H - v is a forest).

If H - v is a forest, then any cycle in H passes through v. Attaching a tree through v: any cycle in the new graph either is in H (passes through v) or passes through v and tree vertices. Two disjoint cycles would need to not share v, but all cycles pass through v. So no two disjoint cycles.

H - v is a forest means v is a feedback vertex set of size 1 for H. So H has a feedback vertex set of size 1. The max edges for such H on h vertices: v connects to all h-1 others (h-1 edges), H-v is a tree (h-2 edges). Total: 2h - 3.

Now attach n-h tree vertices through v. Tree edges: n - h (connecting new vertices to the tree on {v, ..., } which already has h-1 vertices from H-v plus v). Wait, let me re-think.

H has h vertices. H - v is a forest on h-1 vertices. We attach n-h new vertices as a tree connected through v. The tree on {v, (h-1 vertices of H-v), (n-h new vertices)} — but H-v is already a forest, not necessarily connected.

Actually, let me think of it differently. The whole graph G has:
- Vertex v connected to all others (n-1 edges).
- G - v is a forest on n-1 vertices (at most n-2 edges).
- Total: at most 2n - 3 edges.

And this graph has no two disjoint cycles (all cycles pass through v). This is the case s=1 from before, giving 2n-3 edges.

But 2n-3 < 3n-6 for n ≥ 4 (since 2n-3 < 3n-6 iff n > 3). So the split graph with k=3 (3n-6 edges) is better.

Can we beat 3n-6? Let me think about other constructions.

What about a graph where the feedback vertex set has size 2, but with additional structure to prevent two disjoint cycles?

Let S = {a, b}. G - S is a forest F on n-2 vertices. All edges between S and F, plus edge (a,b). Edges: 1 + 2*(n-2) + (n-3) = 1 + 2n - 4 + n - 3 = 3n - 6. Same as split graph with k=3!

But does this have two disjoint cycles? A cycle using only a (from S): a-u-v-a where u-v is an F edge. A cycle using only b: b-w-x-b where w-x is an F edge. If we can find two disjoint F edges (u,v) and (w,x), then {a,u,v} and {b,w,x} are disjoint triangles.

F is a forest on n-2 vertices. If n-2 ≥ 4, F has at least... well, F could be a path, which has n-3 edges. Two disjoint edges in a path on 4+ vertices: yes, e.g., edges (1,2) and (3,4) in a path 1-2-3-4. So for n ≥ 6, F has ≥ 4 vertices and we can find two disjoint edges, giving two disjoint triangles.

So this construction fails for n ≥ 6. Unless F is a star (all edges share a common vertex). If F is a star centered at some vertex w, then all F edges share w. Two disjoint F edges: impossible. So {a,u,v} and {b,x,y} would need u-v and x-y to be F edges, but all F edges share w, so {u,v} and {x,y} both contain w, meaning the triangles share w. Not disjoint!

But wait, can we also have cycles using both a and b? Like a-u-b-v-a (4-cycle). And a cycle using only a: a-w-x-a where w-x is an F edge (w-x shares center w with all edges, so w is the center). 

Hmm, let me reconsider. If F is a star on n-2 vertices centered at w, with leaves l_1, ..., l_{n-3}:

Cycles:
- {a, b, u} for any u: triangle (a-b, a-u, b-u all present). 
- {a, w, l_i}: triangle (a-w, a-l_i, w-l_i all present).
- {b, w, l_i}: triangle.
- {a, l_i, l_j}: NOT a triangle (l_i-l_j not an edge).
- {a, b, w}: triangle.
- 4-cycle a-l_i-b-l_j-a: a-l_i, l_i-b, b-l_j, l_j-a. All present. Uses {a, b, l_i, l_j}.
- 4-cycle a-w-b-l_i-a: a-w, w-b, b-l_i, l_i-a. All present. Uses {a, w, b, l_i}.

Two disjoint cycles:
- {a, w, l_i} and {b, l_j, l_k}: {b, l_j, l_k} needs l_j-l_k, not an edge. No.
- {a, b, l_i} and {w, l_j, l_k}: {w, l_j, l_k} needs l_j-l_k, not an edge. But {w, l_j, l_k} — w-l_j and w-l_k are edges, l_j-l_k is not. Not a triangle. No.
- {a, w, l_i} and {b, l_j, ?}: need a cycle on {b} ∪ (some leaves). {b, l_j, l_k} not a triangle. 4-cycle b-l_j-?-l_k-b: need l_j-? and ?-l_k edges, but leaves have no edges between them. The only edges among F vertices are w-l_i. So a cycle through b and F vertices: b-l_i-w-l_j-b (4-cycle, uses b, l_i, w, l_j). Disjoint from {a, l_k, ?}... 

{a, l_k, ?}: need a cycle. {a, l_k, ?} — a-l_k is an edge, but l_k has no F edges except to w. So {a, l_k, w} is a triangle (a-l_k, l_k-w, a-w). But this uses w, which is also used by b-l_i-w-l_j-b. Not disjoint.

Hmm, it seems hard to find two disjoint cycles. Let me think more carefully.

Any cycle in this graph: it uses some subset of {a, b} and some F vertices. F is a star, so F edges are only w-l_i. 

A cycle using F vertices must use w (since F is a star, any path between two leaves goes through w, and a cycle needs to return). Actually, a cycle like a-l_i-b-l_j-a uses l_i and l_j but not w (the path goes a-l_i, l_i-b, b-l_j, l_j-a, using S vertices a,b as intermediaries). So this 4-cycle doesn't use w.

A cycle like a-l_i-w-l_j-a: uses w. 

A cycle like a-w-b-a: triangle using a, b, w.

A cycle like a-l_i-b-a: triangle using a, b, l_i.

OK so cycles not using w: {a, b, l_i} (triangle) and a-l_i-b-l_j-a (4-cycle using a, b, l_i, l_j).

Cycles using w: {a, w, l_i}, {b, w, l_i}, {a, b, w}, a-l_i-w-l_j-a, a-w-b-l_i-a, b-l_i-w-l_j-b, etc.

Two disjoint cycles, neither using w: {a, b, l_i} and ... we need a cycle on the remaining vertices not using a, b, l_i. Remaining: w and other leaves. A cycle on {w, l_j, l_k, ...}: w-l_j and w-l_k are edges, but l_j-l_k is not. So no triangle. A longer cycle: w-l_j-?-l_k-w, but ? must be a or b (to connect l_j to l_k), and a, b are used. So no.

Two disjoint cycles, one using w and one not: The one not using w is {a, b, l_i} or a-l_i-b-l_j-a. The one using w: must not use a, b, l_i (if the first is {a,b,l_i}) or a, b, l_i, l_j (if the first is the 4-cycle).

If first is {a, b, l_i}: second must use w and leaves except l_i, and not a, b. Cycle on {w, l_j, l_k, ...}: w-l_j, w-l_k are edges, but no edges between leaves. Need to form a cycle: w-l_j-?-l_k-w, ? must connect l_j to l_k. Only a or b can do that, but they're excluded. So no cycle.

If first is a-l_i-b-l_j-a (uses a, b, l_i, l_j): second must use w and leaves except l_i, l_j, and not a, b. Same issue: no cycle possible without a or b.

Two disjoint cycles both using w: impossible (they share w).

So this construction (K_2 + star forest with all cross edges) has no two disjoint cycles! And it has 3n-6 edges.

But wait, this is the same count as the split graph. Can we add more edges?

The forest F is a star. Can we add edges to F (making it not a forest) while keeping no two disjoint cycles? If we add edge (l_i, l_j), then {a, l_i, l_j} is a triangle, and {b, w, l_k} is a triangle (for k ≠ i, j). These are disjoint if n-2 ≥ 4, i.e., n ≥ 6 (we need at least 4 F vertices: w, l_i, l_j, l_k). So adding any edge to F creates two disjoint cycles for n ≥ 6.

Can we add edges within S? S = {a, b} already has edge (a,b). Can't add more.

Can we remove some cross edges and add others? We already have all cross edges. 

So 3n-6 seems to be the max for this type of construction. But is there a fundamentally different construction that does better?

Let me think about K_5-based constructions again. For n=6, we found 12 = 3*6-6 edges with the split graph. But we also found K_6 minus a triangle = 12 edges. And K_5 + pendant = 11 edges. So 12 is the max for n=6.

Wait, I should check: is 3n-6 achievable for all n ≥ 6, and is it the maximum?

For n=6: 3*6-6 = 12. We showed 12 is achievable and 13 forces two disjoint cycles. So m(6) = 13 = 3*6-6+1 = 3n-5.

Hmm wait, let me reconsider. m(n) = (max edges without two disjoint cycles) + 1. If max is 3n-6, then m(n) = 3n-5.

But I need to verify that 3n-6 is indeed the maximum for all n ≥ 6, not just n=6.

Let me think about n=7. Split graph with k=3: K_3 + independent set of 4, all cross edges. 3 + 3*4 = 15 = 3*7-6. 

Does this have two disjoint cycles? K_3 = {a,b,c}, I = {1,2,3,4}. Triangles: {a,b,c}, {a,b,i}, {a,c,i}, {b,c,i} for i ∈ I. Two disjoint triangles: {a,b,1} and {c,2,3}? {c,2,3} needs 2-3 edge, but I is independent. No. {a,1,2}? Needs 1-2 edge, no. 

Any triangle uses ≥2 vertices from K_3 (since I is independent). Two disjoint triangles need ≥4 K_3 vertices, but |K_3| = 3. Impossible.

4-cycles: a-1-b-2-a (uses a,b,1,2). Triangle {c,3,4}? Needs 3-4 edge, no. 

Two disjoint cycles: one triangle (uses ≥2 from K_3) and one other cycle. The other cycle uses the remaining ≤1 K_3 vertex and some I vertices. With 1 K_3 vertex and I vertices: need a cycle, but I is independent, so need at least 2 K_3 vertices for a cycle (to connect I vertices). With only 1 K_3 vertex, can't form a cycle. 

What about two 4-cycles? a-1-b-2-a and c-3-?-4-c: need 3-? and ?-4 edges. ? must be a K_3 vertex, but a,b,c are used. No.

So the split graph with k=3 has no two disjoint cycles for any n. Good.

Now, can we beat 3n-6 for n=7? Let me think about whether there's a graph on 7 vertices with 16 edges and no two disjoint cycles.

Hmm, this is getting complex. Let me think about the general theory.

I recall that this is a known result. The maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles is 3n - 6 for n ≥ 6, and thus m(n) = 3n - 5.

Wait, actually I'm not sure about this. Let me think more carefully.

Actually, I think the relevant theorem is by Erdős and Pósa, or perhaps by Dirac. Let me think about the structure.

The key insight: a graph with no two vertex-disjoint cycles has a specific structure. By the Erdős-Pósa theorem (or a direct argument), such a graph has a feedback vertex set of size at most 3. But as we saw, having a feedback vertex set of size 3 doesn't prevent two disjoint cycles. The constraint is stronger.

Let me think about this more carefully using the concept of the "core" of the graph.

Actually, I think the answer might be m(n) = n + 4 for n ≥ 6, or something else. Let me reconsider.

Wait, I think I need to be more careful. Let me reconsider the problem.

The problem is asking for the minimum m such that every graph with n vertices and m edges has two vertex-disjoint cycles. This is the extremal number plus 1.

Let me reconsider. For n=6, I showed the max without two disjoint cycles is 12, so m(6) = 13. And 3*6-5 = 13. So m(n) = 3n-5?

But wait, I should double-check for larger n. Let me think about n=7.

For n=7, the split graph K_3 + I_4 gives 15 = 3*7-6 edges. Can we do 16?

Let me try: K_3 = {a,b,c}, and on the other 4 vertices {1,2,3,4}, instead of an independent set, use a single edge, say (1,2). Edges: 3 (K_3) + 3*4 (cross) + 1 (extra) = 16.

Does this have two disjoint cycles? {a,1,2} is a triangle (a-1, a-2, 1-2). {b,c,3} is a triangle (b-c, b-3, c-3). Disjoint! So 16 edges with two disjoint cycles.

What about a different 16-edge construction? Take the split graph (15 edges) and add an edge within K_3... but K_3 is already complete.

What about a non-split construction? Let me think about K_5 + 2 vertices.

K_5 on {a,b,c,d,e}, 10 edges. Add vertices 1,2. Connect 1 to a, 2 to a (pendants). 12 edges. No two disjoint cycles? K_5 - a = K_4 has cycles. So {b,c,d} (triangle) and a cycle through a, 1, 2: a-1-?-2-a, but 1 and 2 are pendants (only connected to a). No path from 1 to 2 except through a. So no cycle through 1,2. But {b,c,d} is a triangle in K_5, and is there another disjoint cycle? {a,e,1}? a-e is edge, a-1 is edge, e-1 is not edge (1 is pendant to a only). Not a triangle. {a,e,2}? Same issue. So the only cycles are within K_5. K_5 has no two disjoint cycles (5 vertices, two disjoint cycles need 6). So this has 12 edges and no two disjoint cycles. Less than 15.

What if we connect 1 and 2 to more K_5 vertices? Connect 1 to a,b and 2 to a,b. Then 1-a-b-1 is a triangle, and {c,d,e} is a triangle in K_5. Disjoint! So 10 + 4 = 14 edges with two disjoint cycles.

Connect 1 to a only, 2 to a only, and 1-2 edge: 10 + 2 + 1 = 13. Cycles: within K_5, and a-1-2-a (triangle). {b,c,d} and {a,1,2}: disjoint! So 13 edges with two disjoint cycles.

Connect 1 to a only, 2 to b only: 10 + 2 = 12. No cycle through 1 or 2 (pendants). No two disjoint cycles (only K_5 cycles). 12 edges.

Connect 1 to a,b and 2 to c only: 10 + 3 = 13. Triangle 1-a-b-1. {c,d,e} triangle. But 2 is pendant to c. {c,d,e} uses c, and 1-a-b uses a,b. Disjoint? {1,a,b} ∩ {c,d,e} = ∅. Yes! Two disjoint cycles. 13 edges.

So K_5 + 2 pendants (12 edges) is the best K_5-based for n=7, much less than 15.

So the split graph construction (3n-6) seems to be the best. Let me now try to prove that 3n-6 is the maximum.

Theorem: For n ≥ 6, the maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles is 3n - 6.

I need to prove:
1. There exists a graph with 3n-6 edges and no two disjoint cycles (the split graph K_3 + independent set with all cross edges).
2. Every graph with 3n-5 edges has two vertex-disjoint cycles.

Part 1 is done (the split graph).

For part 2, I need to show that any graph on n ≥ 6 vertices with 3n-5 edges has two vertex-disjoint cycles.

Let me think about this. Suppose G has n ≥ 6 vertices, 3n-5 edges, and no two vertex-disjoint cycles. I want to derive a contradiction.

By the Erdős-Pósa theorem (k=2 case), G has a feedback vertex set S of size at most 3. (Actually, I need to verify that f(2) = 3 for the Erdős-Pósa theorem. The Erdős-Pósa theorem states that there's a function f(k) such that every graph either contains k vertex-disjoint cycles or has a feedback vertex set of size at most f(k). The bound is f(k) = O(k log k). For k=2, I believe f(2) = 3 or maybe f(2) = 4. Let me think about this directly.)

Actually, let me prove the feedback vertex set bound directly. If G has no two vertex-disjoint cycles, then there's a set S of at most 3 vertices such that G - S is a forest.

Proof: Take any cycle C in G. If C has length ≤ 3, let S = V(C) (at most 3 vertices). Any other cycle must share a vertex with C (since no two disjoint cycles). So removing V(C) kills all cycles, meaning G - V(C) is a forest.

If C has length ≥ 4, take any 3 consecutive vertices of C, say v1, v2, v3. Let S = {v1, v2, v3}. Any cycle D disjoint from S: D is disjoint from {v1, v2, v3} but must share a vertex with C (no two disjoint cycles). So D uses some vertex of C \ {v1, v2, v3}. But D is a cycle in G - S. Hmm, this doesn't immediately show G - S is a forest.

Let me think differently. Take a shortest cycle C in G. If |C| ≤ 3, then V(C) is a feedback vertex set of size ≤ 3 (since any other cycle must intersect C). If |C| ≥ 4, then... hmm, actually any cycle D must share a vertex with C. But D could share a vertex with C that's not in S. So removing S doesn't necessarily kill D.

Let me try a different approach. Take a shortest cycle C. Every other cycle shares a vertex with C. Let S = V(C). Then |S| = |C|, which could be large. That's not helpful.

Better approach: Take a shortest cycle C. |C| = g (girth). Every cycle shares a vertex with C. If g ≤ 3, then S = V(C) has ≤ 3 vertices and G - S is a forest. If g ≥ 4, we need a different argument.

If g ≥ 4: Take any edge e = (u,v) on C. Consider G' = G - {u,v}. Any cycle in G' is a cycle in G not using u or v. It must share a vertex with C. Since it doesn't use u or v, it shares a vertex with C \ {u,v}. So G' still has cycles (potentially). 

Hmm, this is getting complicated. Let me just use the known result. Actually, for k=2, the Erdős-Pósa bound is f(2) = 3. This means: if a graph has no 2 vertex-disjoint cycles, it has a feedback vertex set of size at most 3.

Actually, I think I can prove this directly. Let me try:

Claim: If G has no two vertex-disjoint cycles, then G has a feedback vertex set of size at most 3.

Proof: If G is a forest, done (S = ∅). Otherwise, G has a cycle C. If |C| ≤ 3, let S = V(C). Every cycle intersects C (no two disjoint cycles), so G - S is a forest, and |S| ≤ 3.

If |C| ≥ 4: Since every cycle intersects C, consider the vertices of C: v_1, v_2, ..., v_g (g ≥ 4). Any cycle D in G must contain some v_i. 

Consider G - {v_1, v_2}. Any cycle in G - {v_1, v_2} must contain some v_i for i ≥ 3 (since it must intersect C). So G - {v_1, v_2} might still have cycles, but they all use vertices from {v_3, ..., v_g}.

Now, any cycle in G - {v_1, v_2} must use some v_i (i ≥ 3). Take any such cycle D. D uses some v_i (i ≥ 3). Now, D and C share v_i, so they're not disjoint. But we need to find a feedback vertex set.

Let S = {v_1, v_2, v_3}. Any cycle in G must intersect C. If it intersects C at v_1, v_2, or v_3, then it's killed by S. If it intersects C only at v_4, ..., v_g, then it survives in G - S. But such a cycle D uses some v_j (j ≥ 4) and doesn't use v_1, v_2, v_3. 

Now, C uses v_1, v_2, v_3 (among others). D uses v_j (j ≥ 4) and not v_1, v_2, v_3. But D must intersect C, and it does at v_j. So D and C share v_j. That's fine, they're not disjoint. But I want to show G - S is a forest, which means no cycle survives.

Hmm, this doesn't work. A cycle D that only intersects C at {v_4, ..., v_g} would survive in G - S.

Let me try yet another approach. Take the shortest cycle C = v_1...v_g. Consider any cycle D that doesn't use v_1, v_2, v_3. D must intersect C, so D uses some v_j, j ≥ 4. 

Now, C restricted to {v_4, ..., v_g} is a path v_4-v_5-...-v_g (since C is v_1-v_2-...-v_g-v_1, removing v_1,v_2,v_3 leaves the path v_4-...-v_g, plus the edge v_g-v_1 is gone since v_1 is removed, and v_3-v_4 is gone since v_3 is removed).

D uses v_j (j ≥ 4) and possibly other vertices. D is a cycle in G - {v_1,v_2,v_3}. 

Now, I claim that D together with a subpath of C creates a shorter cycle, contradicting the minimality of C. 

D uses v_j and v_k (two vertices of C, j,k ≥ 4, since D must intersect C and we removed v_1,v_2,v_3 — actually D only needs to intersect C at one vertex, but let me think about whether D must use at least 2 C-vertices).

Actually, D doesn't need to use 2 vertices of C. D could use just v_4 and then other non-C vertices. But D is a cycle, so it's a closed walk. If D uses v_4 and then goes through non-C vertices and comes back to v_4, that's a cycle. This cycle doesn't use any other C vertex.

In that case, consider the cycle C' formed by: the path from v_4 to v_1 along C (v_4-v_3-v_2-v_1), then... hmm, this doesn't directly help.

Let me try a completely different approach. Maybe I should use the following known result:

Theorem (Dirac, 1963 or Erdős-Pósa): A graph with n vertices and no two vertex-disjoint cycles has at most 3n - 6 edges (for n ≥ 6).

Actually, I think this might be a theorem by Dirac or by Erdős. Let me think about whether I can prove it.

Alternative approach: induction on n.

Base case n = 6: We showed max is 12 = 3*6 - 6. ✓

Inductive step: Assume for n-1, max is 3(n-1) - 6 = 3n - 9. Show for n, max is 3n - 6.

Take G on n vertices with no two disjoint cycles. If G has a vertex v of degree ≤ 2, then G - v has n-1 vertices and no two disjoint cycles, so e(G-v) ≤ 3(n-1) - 6 = 3n - 9. Then e(G) ≤ 3n - 9 + 2 = 3n - 7 < 3n - 6. 

So if there's a vertex of degree ≤ 2, we're fine (even stronger). The issue is when all vertices have degree ≥ 3.

If all vertices have degree ≥ 3, then e(G) ≥ 3n/2. And we want to show e(G) ≤ 3n - 6.

Hmm, this doesn't directly help. Let me think about the minimum degree case.

If δ(G) ≥ 3, then G has a cycle. In fact, G has many cycles. The constraint is no two disjoint cycles.

Let me think about the structure. If G has no two disjoint cycles and δ(G) ≥ 3, what can we say?

Take a shortest cycle C. Every cycle intersects C. If |C| = 3, then the 3 vertices of C form a feedback vertex set. G - C is a forest on n-3 vertices with at most n-4 edges. The 3 vertices of C have at most 3 edges among them (it's a triangle) and at most 3*(n-3) edges to the rest. Total: 3 + 3(n-3) + (n-4) = 4n - 10. But we need to account for the constraint that no two disjoint cycles exist, which limits the edges further.

Wait, I showed earlier that with a triangle C and all cross edges and a tree on G-C, we get 4n-10 edges but this has two disjoint cycles for n ≥ 7. So the constraint is more subtle.

Let me think about this differently. With a triangle C = {a,b,c} as feedback vertex set:
- G - C is a forest F on n-3 vertices.
- Edges within C: at most 3 (triangle).
- Edges between C and F: at most 3(n-3).
- Edges within F: at most n-4 (forest).
- Total: at most 3 + 3(n-3) + (n-4) = 4n - 10.

But we need the additional constraint: no two disjoint cycles. As I showed, if F has two disjoint edges and the cross edges are complete, we get two disjoint triangles. So either:
(a) F doesn't have two disjoint edges (F is a star or has ≤ 3 vertices), or
(b) The cross edges are not complete.

Case (a): F is a star on n-3 vertices (center w, leaves l_1,...,l_{n-4}) or n-3 ≤ 3.
- If n-3 ≤ 3 (n ≤ 6): F has at most 2 edges. Total: 3 + 3(n-3) + (n-4) = 4n-10. For n=6: 14. But we showed m(6)=13, so max is 12. So even with n=6, the constraint is tighter.

Hmm wait, for n=6, F has 3 vertices. If F is a path (2 edges), total = 3 + 9 + 2 = 14. But we showed this has two disjoint cycles. If F is a star (2 edges, same as path for 3 vertices), same issue. If F has 1 edge, total = 3 + 9 + 1 = 13. Does this have two disjoint cycles? F = edge (1,2) plus isolated vertex 3. {a,1,2} is a triangle. {b,c,3} is a triangle. Disjoint! So 13 edges with two disjoint cycles. If F has 0 edges, total = 3 + 9 + 0 = 12. This is the split graph, which works.

So for n=6, the constraint forces F to have 0 edges (independent set), giving 12 = 3*6-6.

For n=7: F has 4 vertices. To avoid two disjoint cycles:
- If F is a star (3 edges): total = 3 + 12 + 3 = 18. But does this have two disjoint cycles? Star center w, leaves l1,l2,l3. {a,w,l1} and {b,c,l2}: both triangles, disjoint. Yes! So 18 has two disjoint cycles.
- If F has 2 edges: say (1,2) and (2,3) (a path). {a,1,2} and {b,c,4}: both triangles, disjoint (n-3=4, vertex 4 exists). Yes.
- If F has 1 edge: (1,2). {a,1,2} and {b,c,3}: disjoint triangles. Yes (vertex 3 exists since n-3=4 ≥ 3).
- If F has 0 edges: 3 + 12 + 0 = 15 = 3*7-6. This is the split graph, works.

So for n=7 with complete cross edges, F must be an independent set, giving 3n-6.

But what if the cross edges are not complete? Can we compensate by having more F edges?

Suppose we remove one cross edge, say (a, 1), and add one F edge, say (1,2). Total: 3 + (3(n-3) - 1) + (n-4 + 1) = 3 + 3n-9-1 + n-3 = 4n - 10. Same total. But does this avoid two disjoint cycles?

{a,1,2}: needs a-1 (removed!), so not a triangle. {b,1,2}: b-1, b-2, 1-2 all present. Triangle. {a,c,3}: a-3, c-3, a-c all present. Triangle. Disjoint from {b,1,2}? {b,1,2} ∩ {a,c,3} = ∅. Yes! Two disjoint cycles.

So this doesn't help. The problem is that even if we remove one cross edge from a, we can still form triangles using b or c.

What if we remove all cross edges from a to F? Then a is only connected to b,c. Edges: 3 (triangle) + 2*(n-3) (cross from b,c) + (n-4) (F edges) = 3 + 2n-6 + n-4 = 3n - 7. Less than 3n-6.

And does this avoid two disjoint cycles? Cycles through a: must use b or c (since a only connects to b,c). {a,b,c} is a triangle. a-b-...-c-a: a path from b to c not through a. Cycles through b (not a): b-u-v-b where u-v is an F edge. Cycles through c (not a): similar.

Two disjoint cycles: {a,b,c} and a cycle in F: F is a forest, no cycle. {a,b,x} and {c,y,z}: {a,b,x} needs a-x, but a has no cross edges. So {a,b,x} is only a triangle if x ∈ {c} (already {a,b,c}). So the only triangle using a is {a,b,c}. 

Other triangles: {b,c,u} for u ∈ F (b-u, c-u, b-c all present). {b,u,v} for F edge (u,v). {c,u,v} for F edge (u,v).

Two disjoint cycles: {b,u,v} (F edge u-v) and {a,c,w} — but a-c is edge, a-w is not (no cross edges from a). Not a triangle. {b,u,v} and {c,w,x} — needs F edge w-x disjoint from u-v. If F has two disjoint edges, yes.

So if F has two disjoint edges, we get two disjoint cycles ({b,u,v} and {c,w,x}). If F is a star (no two disjoint edges), then no two disjoint cycles from this. But then F has at most n-4 edges (star on n-3 vertices). Total: 3 + 2(n-3) + (n-4) = 3n - 7. Still less than 3n-6.

What if a connects to some F vertices but not all? Say a connects to k F vertices. Then cross edges: 2(n-3) + k. F edges: at most n-4 (if F is a forest). Total: 3 + 2(n-3) + k + (n-4) = 3n - 7 + k.

To get 3n - 6, we need k = 1. So a connects to exactly 1 F vertex, say vertex 1. Cross edges: 2(n-3) + 1. F edges: n-4. Total: 3 + 2n-6 + 1 + n-4 = 3n - 6.

Does this avoid two disjoint cycles? F is a forest (n-4 edges, so a tree on n-3 vertices). a connects to b, c, and vertex 1.

Cycles: {a,b,c} (triangle). {b,c,u} for u ∈ F (triangle). {b,u,v} for F edge (u,v) (triangle). {c,u,v} for F edge (u,v) (triangle). {a,b,1} (triangle, a-1 is edge). {a,c,1} (triangle). a-1-...-b-a or a-1-...-c-a (longer cycles through a, 1, and F).

Two disjoint cycles: {a,b,1} and {c,u,v} where (u,v) is an F edge not involving 1. If F has an edge not involving 1, then {c,u,v} is a triangle disjoint from {a,b,1}. 

F is a tree on n-3 vertices including vertex 1. If n-3 ≥ 2 (n ≥ 5), F has at least 1 edge. If that edge involves 1, say (1,2), then we need another edge not involving 1. If n-3 ≥ 3 (n ≥ 6), F has at least 2 edges, and at most 1 involves 1 (in a tree, vertex 1 has some degree). If vertex 1 is a leaf, only 1 edge involves it, and the other n-5 edges don't. So for n ≥ 6, there exists an F edge (u,v) not involving 1, and {c,u,v} is a triangle disjoint from {a,b,1}.

So this construction fails for n ≥ 6! The only way to avoid two disjoint cycles is to have no F edges at all (F is independent), which gives the split graph with 3n-6 edges.

Wait, but I assumed F is a tree (n-4 edges). What if F has fewer edges? If F has n-5 edges (one less than a tree), total = 3n-7. Still less.

So it seems like 3n-6 is indeed the maximum, achieved only by the split graph (K_3 + independent set with all cross edges).

But I need to be more rigorous. Let me also consider the case where the feedback vertex set has size 1 or 2 (not 3).

Case s=1: feedback vertex set {v}. Max edges: 2n-3. For n ≥ 6, 2n-3 < 3n-6 iff n > 3. So s=1 gives fewer edges.

Case s=2: feedback vertex set {a,b}. G-{a,b} is a forest F on n-2 vertices. Max edges: 1 + 2(n-2) + (n-3) = 3n-6. Same as s=3! But we need to check the no-two-disjoint-cycles constraint.

With complete cross edges and F a tree: {a,u,v} and {b,w,x} for disjoint F edges (u,v) and (w,x). If F has two disjoint edges (n-2 ≥ 4, n ≥ 6), two disjoint triangles. So F must be a star (no two disjoint edges).

F is a star on n-2 vertices: n-3 edges. Total: 1 + 2(n-2) + (n-3) = 3n-6. Same count!

But does the star construction avoid two disjoint cycles? I analyzed this earlier and found it does (for the K_2 + star case). Let me re-verify.

S = {a,b}, F = star centered at w with leaves l_1,...,l_{n-4}. All cross edges present, edge (a,b) present.

As I analyzed before, any cycle either uses both a and b, or uses exactly one of {a,b} and some F vertices. Two disjoint cycles: one using a (not b) and one using b (not a). The one using a: a-u-...-v-a, needs a path in F. F is a star, so any path between two leaves goes through w. So the cycle is a-l_i-w-l_j-a (4-cycle) or a-w-l_i-a (triangle, using a-w and w-l_i and a-l_i). Similarly for b.

Two disjoint: a-l_i-w-l_j-a and b-l_k-w-l_m-b: both use w. Not disjoint.
a-l_i-a (not a cycle, just back and forth). 
a-w-l_i-a (triangle, uses a, w, l_i) and b-l_j-...-b: b-l_j-w-l_k-b (4-cycle, uses b, l_j, w, l_k). Both use w. Not disjoint.
{a, w, l_i} and {b, l_j, l_k}: {b,l_j,l_k} needs l_j-l_k, not an edge. No.
{a, b, l_i} and {w, l_j, l_k}: {w,l_j,l_k} needs l_j-l_k, not an edge. No.
{a, b, l_i} and {w, l_j, ?}: can't form a cycle without a or b.
{a, b, w} and cycle in F: F is a star (tree), no cycle.

What about {a, b, l_i} (triangle) and a cycle using w and leaves (not a, b, l_i)? Cycle on {w, l_j, l_k, ...} without a,b: need edges between leaves, but there are none. No cycle.

What about 4-cycle a-l_i-b-l_j-a (uses a, b, l_i, l_j) and a cycle on {w, l_k, ...}? Same issue, no cycle without a or b.

So indeed, the K_2 + star construction has no two disjoint cycles and 3n-6 edges. Same as the split graph.

Now, the key question: can we beat 3n-6? We've seen that with s=3 (triangle feedback vertex set), we get at most 3n-6 (split graph). With s=2, we get at most 3n-6 (K_2 + star). With s=1, at most 2n-3 < 3n-6.

But what about graphs where the feedback vertex set has size 3 but is not a triangle? Or graphs with more complex structure?

Let me consider s=3 with S = {a,b,c} not forming a triangle. Say edges in S: (a,b) and (b,c) but not (a,c). Then:
- Edges in S: 2
- Cross edges: at most 3(n-3)
- F edges: at most n-4 (forest)
- Total: 2 + 3(n-3) + (n-4) = 4n - 11

But we need no two disjoint cycles. With all cross edges and F a tree:
{a,b,u} (triangle, a-b, a-u, b-u) and {c,v,w} (triangle, c-v, c-w, v-w F edge). Disjoint if (v,w) is an F edge not involving u. For n ≥ 7, such an edge exists. So this fails.

If F is a star: {a,b,u} and {c,w,l_j} where w is center, l_j a leaf, u a leaf ≠ l_j. {c,w,l_j}: c-w, c-l_j, w-l_j all present. Triangle. {a,b,u}: a-b, a-u, b-u. Triangle. Disjoint if u ≠ w and u ≠ l_j. Since F has n-3 ≥ 4 vertices (n ≥ 7), we can choose u, l_j distinct leaves. So disjoint triangles exist.

For n=6: F has 3 vertices, star has 2 leaves. {a,b,u} and {c,w,l_j}: u and l_j are the 2 leaves, distinct. {c,w,l_j} is a triangle. {a,b,u} is a triangle. Disjoint. So even for n=6, this fails.

So with S not a triangle, we can't achieve 3n-6 without two disjoint cycles (for n ≥ 6). The maximum is less.

What if S has only 2 edges (a path a-b-c) and we don't have all cross edges? We'd need to remove cross edges to prevent two disjoint cycles, losing edges. The total would be less than 3n-6.

So it seems like 3n-6 is the maximum, achieved by:
1. Split graph: K_3 + independent set, all cross edges. (s=3, S is a triangle)
2. K_2 + star, all cross edges, edge in S. (s=2, S is an edge)

Both give 3n-6.

Now I need to prove that 3n-5 edges always force two disjoint cycles. Let me try to prove this by induction.

Theorem: For n ≥ 6, every graph with n vertices and 3n-5 edges has two vertex-disjoint cycles.

Proof by induction on n.

Base case n=6: 3*6-5 = 13 edges. We showed that any 13-edge graph on 6 vertices has two disjoint triangles (hence two disjoint cycles). ✓

Inductive step: Assume the theorem holds for n-1 (n ≥ 7). Let G be a graph on n vertices with 3n-5 edges. Suppose for contradiction G has no two vertex-disjoint cycles.

If G has a vertex v with degree ≤ 2, then G-v has n-1 vertices and at least 3n-5-2 = 3n-7 = 3(n-1)-4 edges. Since 3(n-1)-4 > 3(n-1)-5 (for n ≥ 7, 3(n-1)-4 = 3n-7 > 3n-8 = 3(n-1)-5), by induction G-v has two disjoint cycles, hence G does too. Contradiction.

Wait, 3(n-1)-5 = 3n-8. And 3n-7 > 3n-8. So G-v has ≥ 3n-7 > 3(n-1)-5 edges, so by induction, G-v has two disjoint cycles. ✓

So we may assume δ(G) ≥ 3.

If δ(G) ≥ 3, then every vertex has degree ≥ 3. The sum of degrees is 2(3n-5) = 6n-10. Average degree is (6n-10)/n = 6 - 10/n, which is less than 6 for all n. So there's a vertex of degree ≤ 5.

Hmm, I need a vertex of degree ≤ 2 to make the induction work, but we're in the case δ ≥ 3. Let me think differently.

If δ(G) ≥ 3, I need to show G has two disjoint cycles directly (or derive a contradiction).

Since G has no two disjoint cycles, by the feedback vertex set argument, G has a feedback vertex set S of size ≤ 3. 

Case 1: |S| = 1, S = {v}. G-v is a forest. e(G) ≤ (n-1) + (n-2) = 2n-3. But e(G) = 3n-5 > 2n-3 for n ≥ 3. Contradiction.

Case 2: |S| = 2, S = {a,b}. G-{a,b} is a forest F on n-2 vertices. 
e(G) = e(S) + e(S,F) + e(F) ≤ 1 + 2(n-2) + (n-3) = 3n-6.
But e(G) = 3n-5 > 3n-6. Contradiction.

Wait, but this assumes the maximum is 3n-6, which is what we're trying to prove! The bound e(G) ≤ 1 + 2(n-2) + (n-3) = 3n-6 is just the trivial bound (S has at most 1 edge, cross at most 2(n-2), F at most n-3). This doesn't use the no-two-disjoint-cycles constraint beyond the feedback vertex set.

So: if |S| = 2, e(G) ≤ 3n-6 < 3n-5. Contradiction. ✓

Case 3: |S| = 3, S = {a,b,c}. G-S is a forest F on n-3 vertices.
e(G) = e(S) + e(S,F) + e(F) ≤ 3 + 3(n-3) + (n-4) = 4n-10.
For n ≥ 6, 4n-10 > 3n-5 (since 4n-10 > 3n-5 iff n > 5). So the trivial bound doesn't give a contradiction.

I need to use the no-two-disjoint-cycles constraint more carefully for |S| = 3.

So the hard case is |S| = 3. Let me analyze this.

S = {a,b,c}, G-S is a forest F on n-3 vertices. e(G) = 3n-5.

e(S) ≤ 3, e(S,F) ≤ 3(n-3), e(F) ≤ n-4. Total ≤ 4n-10.

We need e(G) = 3n-5. So 3n-5 ≤ 4n-10, i.e., n ≥ 5. OK for n ≥ 6.

Now, the no-two-disjoint-cycles constraint. Let me think about what restrictions this imposes.

If S is a triangle (e(S) = 3) and all cross edges present (e(S,F) = 3(n-3)):
e(F) = 3n-5 - 3 - 3(n-3) = 3n-5-3-3n+9 = 1. So F has exactly 1 edge.

F has n-3 ≥ 3 vertices and 1 edge, say (u,v). Then {a,u,v} is a triangle (a-u, a-v, u-v). And {b,c,w} for any w ∈ F \ {u,v} is a triangle (b-c, b-w, c-w). If n-3 ≥ 3 (n ≥ 6), there exists w. These are disjoint. Contradiction.

If S is a triangle (e(S) = 3) and e(S,F) = 3(n-3) - 1 (one cross edge missing, say a-u):
e(F) = 3n-5 - 3 - (3n-9-1) = 3n-5-3-3n+10 = 2. F has 2 edges.

F has n-3 ≥ 3 vertices and 2 edges. 

Subcase: F has two edges sharing a vertex (a path u-v-w). {b,u,v} is a triangle (b-u, b-v, u-v). {c,v,w} is a triangle (c-v, c-w, v-w). But these share v. {b,u,v} and {c,w,x}? Need w-x edge, but F only has edges (u,v) and (v,w). No w-x edge. {a,v,w}? a-v is edge, a-w is edge (only a-u is missing), v-w is edge. Triangle! {b,c,u}? b-c, b-u, c-u. Triangle. Disjoint from {a,v,w}? {a,v,w} ∩ {b,c,u} = ∅. Yes! Two disjoint cycles.

Hmm wait, I said a-u is missing. So a is connected to all F vertices except u. So a-v and a-w are present. {a,v,w}: a-v ✓, a-w ✓, v-w ✓ (F edge). Triangle. {b,c,u}: b-c ✓, b-u ✓, c-u ✓. Triangle. Disjoint. Contradiction.

Subcase: F has two disjoint edges (u,v) and (w,x). {a,u,v} — a-u is missing! So not a triangle. {b,u,v}: b-u, b-v, u-v. Triangle. {c,w,x}: c-w, c-x, w-x. Triangle. Disjoint. Contradiction.

So with e(S)=3, e(S,F) = 3(n-3)-1, we still get contradictions.

What if e(S,F) = 3(n-3) - 2 (two cross edges missing)?
e(F) = 3n-5-3-(3n-9-2) = 3n-5-3-3n+11 = 3. F has 3 edges.

This is getting complicated. Let me think about this more systematically.

Let me denote:
- e_S = edges within S (≤ 3)
- e_F = edges within F (≤ n-4, since F is a forest)
- e_cross = edges between S and F (≤ 3(n-3))

e_S + e_F + e_cross = 3n - 5.

The no-two-disjoint-cycles constraint: I need to figure out what combinations of (e_S, e_F, e_cross) are possible.

Key observation: If S is a triangle and there exist two disjoint edges in F, and the cross edges are "complete enough," we get two disjoint triangles.

Let me think about it in terms of what's needed to prevent two disjoint cycles.

With S = {a,b,c} a triangle, F a forest:

Two disjoint cycles can be:
1. Two triangles, each using ≥ 2 S-vertices: impossible (only 3 S-vertices).
2. One triangle using 2 S-vertices + 1 F-vertex, and one triangle using 1 S-vertex + 2 F-vertices (with an F edge): e.g., {a,b,u} and {c,v,w} where (v,w) is an F edge and u ∉ {v,w}.
3. One triangle using 3 S-vertices ({a,b,c}), and one cycle in F: impossible (F is a forest).
4. One triangle using 2 S-vertices + 1 F-vertex, and one cycle using 2 S-vertices + ≥ 2 F-vertices: impossible (need 4 S-vertices).
5. Two cycles each using 1 S-vertex + ≥ 2 F-vertices: e.g., {a,u,v} and {b,w,x} where (u,v) and (w,x) are F edges, disjoint. Need 2 disjoint F edges.
6. One triangle using 3 S-vertices ({a,b,c}) and one triangle using 0 S-vertices: impossible (F is a forest, no triangle).
7. One cycle using 2 S-vertices + ≥ 2 F-vertices, and another using 1 S-vertex + ≥ 2 F-vertices: e.g., a-u-b-v-a (4-cycle, uses a,b,u,v) and {c,w,x} (triangle, uses c,w,x with w-x F edge). Disjoint if {u,v} ∩ {w,x} = ∅.

So the main threats are:
- Type 2: {a,b,u} and {c,v,w} with F edge (v,w), u ∉ {v,w}.
- Type 5: {a,u,v} and {b,w,x} with F edges (u,v) and (w,x), disjoint.
- Type 7: a-u-b-v-a and {c,w,x} with F edges (u,v) (wait, a-u-b-v-a uses a-u, u-b, b-v, v-a, not F edges; it uses cross edges and the a-b edge). Hmm, let me reconsider. a-u-b-v-a: edges a-u (cross), u-b (cross), b-v (cross), v-a (cross). This is a 4-cycle using a, b, u, v. It doesn't need F edges. And {c,w,x} needs F edge (w,x). Disjoint if {u,v} ∩ {w,x} = ∅.

So Type 7: 4-cycle a-u-b-v-a (using cross edges, needs a-b edge) and triangle {c,w,x} (needs F edge w-x and cross edges c-w, c-x). Disjoint if {u,v} ∩ {w,x} = ∅.

To prevent all these, we need strong conditions. Let me think about what conditions on F and the cross edges prevent all types.

This is getting quite involved. Let me try a different approach to the proof.

Alternative approach: Direct proof using the structure.

Let me use the following lemma:

Lemma: If G has no two vertex-disjoint cycles and n ≥ 6 vertices, then e(G) ≤ 3n - 6.

Proof: By induction on n.

Base case n = 6: Verified (max is 12 = 3*6-6).

Inductive step (n ≥ 7): Assume the lemma for all graphs on n-1 vertices. Let G be a graph on n vertices with no two disjoint cycles.

If G has a vertex v with deg(v) ≤ 2: G-v has n-1 vertices, no two disjoint cycles, so e(G-v) ≤ 3(n-1)-6 = 3n-9. Then e(G) ≤ 3n-9+2 = 3n-7 < 3n-6. ✓

If δ(G) ≥ 3: We need to show e(G) ≤ 3n-6.

Since G has no two disjoint cycles, G has a feedback vertex set S with |S| ≤ 3 (I'll prove this below). 

If |S| ≤ 2: e(G) ≤ C(2,2) + 2(n-2) + (n-3) = 1 + 2n-4 + n-3 = 3n-6. ✓ (This is the trivial bound, and it equals 3n-6.)

If |S| = 3: e(G) ≤ 3 + 3(n-3) + (n-4) = 4n-10. This is > 3n-6 for n ≥ 5. So we need the no-two-disjoint-cycles constraint.

Hmm, so the |S| = 3 case is the hard one, and the trivial bound isn't enough. I need to use the structure more carefully.

Let me think about the |S| = 3 case with δ(G) ≥ 3.

S = {a,b,c}, F = G-S is a forest on n-3 vertices. δ(G) ≥ 3 means every vertex has degree ≥ 3.

For a vertex u in F: deg(u) = deg_F(u) + deg_S(u) ≥ 3. deg_F(u) is the degree in the forest, deg_S(u) is the number of S-vertices adjacent to u (0 to 3).

If deg_S(u) = 0: deg_F(u) ≥ 3, but F is a forest, so max degree in F can be high. But a vertex in a forest with degree ≥ 3 is possible. However, if u has deg_S(u) = 0, u is not adjacent to any S vertex. Any cycle through u must be in F, but F is a forest (no cycles). So u is not in any cycle. But δ ≥ 3 and u has no S neighbors, so u has ≥ 3 F-neighbors. 

Actually, if deg_S(u) = 0, then u is only connected to F vertices. Since F is a forest, u is in no cycle. But we need deg(u) ≥ 3, so deg_F(u) ≥ 3. This is possible in a forest (e.g., a star center).

But here's the thing: if deg_S(u) = 0 for some u, then u is not in any cycle. Consider G' = G - u. G' has n-1 vertices and no two disjoint cycles (subgraph of G). By induction, e(G') ≤ 3(n-1)-6 = 3n-9. Then e(G) = e(G') + deg(u) ≤ 3n-9 + deg(u). 

If deg(u) ≤ 3: e(G) ≤ 3n-9+3 = 3n-6. ✓
If deg(u) ≥ 4: e(G) ≤ 3n-9+deg(u), which could exceed 3n-6.

Hmm, but if deg_S(u) = 0 and deg_F(u) ≥ 4, u is a high-degree vertex in the forest F. 

Actually wait, I think I can handle this differently. Let me consider the minimum degree vertex.

Since δ(G) ≥ 3, let v be a vertex of minimum degree d = δ(G) ≥ 3. G - v has n-1 vertices and no two disjoint cycles. By induction, e(G-v) ≤ 3(n-1)-6 = 3n-9. So e(G) ≤ 3n-9 + d.

If d ≤ 3: e(G) ≤ 3n-9+3 = 3n-6. ✓

So the only problematic case is d ≥ 4, i.e., δ(G) ≥ 4.

If δ(G) ≥ 4: sum of degrees ≥ 4n, so e(G) ≥ 2n. And e(G) = 3n-5 (what we're trying to contradict). So 3n-5 ≥ 2n, i.e., n ≥ 5. OK.

With δ(G) ≥ 4 and no two disjoint cycles, feedback vertex set S of size ≤ 3.

For u in F: deg(u) = deg_F(u) + deg_S(u) ≥ 4. Since deg_S(u) ≤ 3, deg_F(u) ≥ 1. So every F vertex has degree ≥ 1 in F, meaning F has no isolated vertices. Since F is a forest with no isolated vertices, F is a union of trees each with ≥ 2 vertices.

Also, deg_S(u) ≥ 4 - deg_F(u). If deg_F(u) = 1 (leaf in F), deg_S(u) ≥ 3, so u is adjacent to all of a, b, c. If deg_F(u) = 2, deg_S(u) ≥ 2.

Now, let me count edges more carefully.

e(G) = e_S + e_cross + e_F.

We want to show e(G) ≤ 3n-6, i.e., e_S + e_cross + e_F ≤ 3n-6.

e_F ≤ n-4 (forest on n-3 vertices, at most n-4 edges). Actually, if F has no isolated vertices and n-3 vertices, F has at least ceil((n-3)/2) edges (each tree has at least 1 edge for 2 vertices). But the upper bound is n-4 (tree).

e_S ≤ 3.
e_cross ≤ 3(n-3).

So e(G) ≤ 3 + 3(n-3) + (n-4) = 4n-10. We need to bring this down to 3n-6, so we need to save n-4 edges from the trivial bound.

The no-two-disjoint-cycles constraint must save us n-4 edges. Let me think about how.

Key constraint: no two disjoint cycles. With S = {a,b,c} and F a forest:

If S is a triangle and all cross edges are present, then any F edge (u,v) creates triangle {a,u,v} (or {b,u,v} or {c,u,v}). Two disjoint F edges create two disjoint triangles (using different S vertices). So F can have at most... well, if F has two disjoint edges, we get two disjoint triangles (Type 5). So F must be a star (matching number 1) or have at most 3 vertices.

If F is a star on n-3 vertices: e_F = n-4. And we need all cross edges present and S a triangle for the max. But then: {a,b,u} (triangle, u a leaf) and {c,w,l} where w is center, l another leaf. {c,w,l}: c-w, c-l, w-l. Triangle. Disjoint from {a,b,u} if u ∉ {w,l}. Since n-3 ≥ 4 (n ≥ 7), there are ≥ 3 leaves, so we can pick u, l distinct. Contradiction!

So for n ≥ 7, even a star F with all cross edges and S a triangle gives two disjoint cycles. The only way to avoid this is to not have all cross edges or not have S as a triangle.

This suggests that for n ≥ 7, the maximum is strictly less than 4n-10, and in fact at most 3n-6.

Let me try to prove this more carefully.

Claim: For n ≥ 6, if G has no two disjoint cycles, |S| = 3 (feedback vertex set), and S is a triangle, then e_cross + e_F ≤ 3(n-3) + 0 = 3(n-3), i.e., e_F = 0 (F is an independent set) when e_cross = 3(n-3) (all cross edges present).

More generally, I want to show e_S + e_cross + e_F ≤ 3n-6.

Let me think about it as: e_S + e_cross + e_F ≤ 3 + e_cross + e_F, and I want this ≤ 3n-6, so e_cross + e_F ≤ 3n-9 = 3(n-3).

Since e_cross ≤ 3(n-3) and e_F ≤ n-4, the sum is at most 3(n-3) + (n-4) = 4n-13. We need this ≤ 3(n-3) = 3n-9, so we need e_F ≤ 3(n-3) - e_cross, i.e., the "missing" cross edges must be at least e_F.

In other words: (missing cross edges) ≥ e_F, i.e., 3(n-3) - e_cross ≥ e_F.

Is this true? Let me think about why.

For each F edge (u,v), to prevent triangle {a,u,v}, at least one of a-u, a-v must be missing. Similarly for b and c. But we don't need to prevent all three triangles {a,u,v}, {b,u,v}, {c,u,v} — we just need to prevent two disjoint cycles.

Hmm, actually, the constraint is more subtle. Let me think about specific cases.

If F has an edge (u,v) and all three cross edges from a, b, c to both u and v are present, then {a,u,v}, {b,u,v}, {c,u,v} are all triangles. Now, {a,u,v} and {b,c,w} (for w ∈ F, w ≠ u,v) are disjoint triangles (if n-3 ≥ 3, i.e., n ≥ 6). So to prevent this, for each F edge (u,v), at least one S-vertex must be missing an edge to u or v.

But that's not quite right either. {a,u,v} and {b,c,w}: we need w to exist (n ≥ 6) and b-w, c-w to be present. If b-w or c-w is missing, this particular pair doesn't work. But we could try {b,u,v} and {a,c,w}, etc.

This is getting very complicated. Let me try a different approach to the proof.

Let me try to prove the upper bound directly, without the feedback vertex set approach.

Direct proof attempt:

The        — AI历史解题过程（thinking）
#   polymath_04593         — 题目ID

# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search.
- All information you need is in this AGENTS.md file.
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
  <problem_id>polymath_04593</problem_id>
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

Given an integer \( n \geq 6 \), find the least integer \( m(n) \) such that for any graph \( G \) with \( n \) vertices and \( m(n) \) edges, there must exist two vertex-disjoint cycles in \( G \).

## Standard Solution

To determine the least integer \( m(n) \) such that any graph \( G \) with \( n \) vertices and \( m(n) \) edges must contain two vertex-disjoint cycles, we need to understand the maximum number of edges a graph can have without containing two vertex-disjoint cycles.

### Step-by-Step Solution:

1. **Identify the Extremal Graph:**
   - Consider a graph \( G \) with \( n \) vertices. To avoid having two vertex-disjoint cycles, the graph must be structured in such a way that all cycles share at least one common vertex.
   - A known result in extremal graph theory states that the maximum number of edges in an \( n \)-vertex graph without two vertex-disjoint cycles is \( 3n - 6 \).

2. **Constructing the Extremal Graph:**
   - The extremal graph can be constructed by taking a complete graph \( K_5 \) (which has 10 edges) and connecting each of the remaining \( n-5 \) vertices to all 5 vertices of \( K_5 \). This structure ensures that any cycle must include at least one vertex from the \( K_5 \), preventing the formation of two vertex-disjoint cycles.
   - The total number of edges in this graph is \( 10 + 5(n-5) = 5n - 15 \).

3. **Adjusting for \( n \geq 6 \):**
   - For \( n \geq 6 \), the maximum number of edges without two vertex-disjoint cycles is \( 3n - 6 \). This is derived from the structure where all cycles must share a common vertex or a small subset of vertices.

4. **Determine \( m(n) \):**
   - To ensure that any graph with \( m(n) \) edges must contain two vertex-disjoint cycles, we take \( m(n) \) to be one more than the maximum number of edges without two vertex-disjoint cycles.
   - Therefore, \( m(n) = (3n - 6) + 1 = 3n - 5 \).

### Conclusion:
The least integer \( m(n) \) such that any graph \( G \) with \( n \) vertices and \( m(n) \) edges must contain two vertex-disjoint cycles is given by:

\[
\boxed{3n - 5}
\]

## AI's Thinking (Attempted Solution Process)

The problem asks for the least integer m(n) such that any graph with n vertices and m(n) edges must contain two vertex-disjoint cycles.

This is a classic extremal graph theory problem. Let me think about it.

The answer is m(n) = n+1 for n ≥ 6.

Wait, let me think more carefully. The question is about the minimum number of edges that forces two vertex-disjoint cycles.

Let me recall the Erdős-Pósa type results. Actually, this is a specific result.

The extremal number for two vertex-disjoint cycles: we want the maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles, then m(n) = that + 1.

A graph with no two vertex-disjoint cycles: by the Erdős-Pósa theorem (or more specifically, the structure of graphs without two disjoint cycles), such graphs have a specific structure.

Let me think about what graphs have no two vertex-disjoint cycles.

First, let's think about the maximum number of edges. 

Consider a graph where all cycles share a common vertex. For instance, take a "friendship graph" or a "wheel-like" structure. Actually, let me think about the structure more carefully.

If a graph has no two vertex-disjoint cycles, then by a theorem (this is related to the Erdős-Pósa theorem with k=2), the graph has a small vertex set hitting all cycles... actually no, that's not quite right either.

Let me think about this differently. Let me consider the extremal construction.

Construction: Take a complete graph K_5 on 5 vertices, and attach the remaining n-5 vertices as a tree (or as leaves hanging off). Actually, let me think about what maximizes edges while avoiding two disjoint cycles.

If we have K_5, it has 10 edges. K_5 has no two vertex-disjoint cycles (since any two cycles in K_5 must share a vertex — K_5 has 5 vertices, two disjoint cycles would need at least 6 vertices). 

Now attach n-5 more vertices. To maximize edges, we can connect each new vertex to all 5 vertices of the K_5. But wait, if we connect a new vertex v to two vertices of K_5, then v together with an edge of K_5 forms a triangle, and the remaining 4 vertices of K_5 form a K_4 which contains a cycle. So we'd have two disjoint cycles.

So we can't connect new vertices too freely. Let me think...

If we connect a new vertex v to exactly one vertex of K_5, that's like a pendant. We can build a tree on the n-5 new vertices plus connect them to one vertex of K_5. That gives a tree-like structure attached to K_5.

Actually, let me reconsider. The extremal graph for "no two vertex-disjoint cycles" — let me think about what structure maximizes edges.

Claim: The maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles is n+1, achieved by... hmm, let me think.

Actually wait. Let me reconsider. K_5 has 10 edges and 5 vertices. If n=5, K_5 has no two disjoint cycles. For n ≥ 6, we need to add vertices.

Let me think about n=6. We need m(6) such that any graph on 6 vertices with m(6) edges has two disjoint cycles. 

K_5 plus one vertex: if the 6th vertex connects to 0 vertices of K_5, we have 10 edges, no two disjoint cycles (since only 5 vertices are in cycles). If it connects to 1 vertex, still 11 edges, the 6th vertex is a pendant, no new cycle. If it connects to 2 vertices of K_5, then we get a triangle (v, a, b) where ab is an edge of K_5, and the remaining 3 vertices of K_5 form a triangle. So two disjoint cycles! That's 12 edges.

But can we do better than K_5 + pendant? What about K_4 plus two vertices? K_4 has 6 edges, 4 vertices. Add two vertices each connected to one vertex of K_4: 8 edges. Or connect them to each other and to K_4 in a way that avoids two disjoint cycles.

Hmm, let me think about the general structure.

Theorem (I believe this is a known result): The maximum number of edges in a graph on n ≥ 5 vertices with no two vertex-disjoint cycles is n+1, so m(n) = n+2.

Wait, let me recompute. K_5 has 10 = 5+5 edges. Hmm, that doesn't match n+1.

Let me reconsider. For n=5: K_5 has 10 edges and no two disjoint cycles. So the max for n=5 is at least 10. n+1 = 6, that's way less. So the formula n+1 is wrong.

Let me reconsider the problem. The problem says n ≥ 6.

For n=6: What's the max edges with no two disjoint cycles?

K_5 + 1 isolated vertex: 10 edges, 6 vertices. No two disjoint cycles (only 5 vertices participate in cycles).

K_5 + 1 pendant vertex (connected to one K_5 vertex): 11 edges, 6 vertices. Still no two disjoint cycles.

Can we get 12 edges? If the 6th vertex connects to 2 vertices of K_5, we get two disjoint cycles as I argued. So with K_5-based construction, max is 11.

But maybe there's a different construction with more edges? 

What about K_{3,3}? That has 9 edges, 6 vertices, and contains two disjoint 4-cycles? Actually K_{3,3} — does it have two vertex-disjoint cycles? K_{3,3} has a Hamiltonian cycle (6-cycle). Can we find two disjoint cycles? A 4-cycle uses 4 vertices, leaving 2, not enough for another cycle. Two 3-cycles? K_{3,3} is bipartite, so no odd cycles. So the smallest cycles are 4-cycles. Two 4-cycles need 8 vertices, we only have 6. So K_{3,3} has no two vertex-disjoint cycles! And it has 9 edges.

So K_{3,3} gives 9 edges for n=6, less than K_5 + pendant's 11.

What about other constructions? Take K_4 (4 vertices, 6 edges) and add two vertices. Connect each to all 4 vertices of K_4? That's 6 + 8 = 14 edges but would definitely have two disjoint cycles.

Let me think about the structure of graphs without two disjoint cycles more carefully.

A graph has no two vertex-disjoint cycles if and only if... by the Erdős-Pósa theorem, for k=2, either there's a small set of vertices hitting all cycles, or there are few disjoint cycles. Actually the Erdős-Pósa theorem says there's a function f(k) such that either there are k disjoint cycles or a set of f(k) vertices hitting all cycles. For k=2, f(2) = 3 (I think).

So a graph with no two disjoint cycles either has a feedback vertex set of size ≤ 3 (a set of 3 vertices whose removal makes the graph a forest).

If there's a feedback vertex set S of size ≤ 3, then G - S is a forest. The number of edges is at most C(|S|,2) + |S|*(n-|S|) + (n-|S|-1) = ... wait, let me be more careful.

If |S| = s, then G-S is a forest on n-s vertices, so has at most n-s-1 edges. The edges within S: at most C(s,2). The edges between S and the rest: at most s*(n-s). Total: C(s,2) + s*(n-s) + (n-s-1).

For s=3: C(3,2) + 3*(n-3) + (n-4) = 3 + 3n-9 + n-4 = 4n - 10.

For s=2: C(2,2) + 2*(n-2) + (n-3) = 1 + 2n-4 + n-3 = 3n - 6.

For s=1: 0 + (n-1) + (n-2) = 2n - 3.

For s=0: n-1 (just a forest, but a forest has no cycles at all, so trivially no two disjoint cycles).

So the maximum is achieved at s=3: 4n - 10.

But wait, can we actually achieve 4n-10? We need:
- S is a clique of size 3 (3 edges)
- Every vertex outside S is connected to all 3 vertices of S (3(n-3) edges)
- G-S is a tree on n-3 vertices (n-4 edges)

Total: 3 + 3(n-3) + (n-4) = 3 + 3n - 9 + n - 4 = 4n - 10.

Does this graph have no two vertex-disjoint cycles? Let's check. Any cycle must use at least one vertex of S (since G-S is a forest). Actually, any cycle must use at least one vertex of S. But two cycles could each use one vertex of S (different vertices), and they'd be disjoint if they don't share vertices outside S either.

Wait, let me reconsider. If S = {a, b, c} is a triangle, and every outside vertex is connected to all of a, b, c, and the outside vertices form a tree.

Consider two outside vertices u, v connected by an edge in the tree. Then u-a-v is a path... wait, u and v are both connected to a. So u-a-v-u? No, we need u-v edge (yes, tree edge) and u-a, v-a edges (yes). So {u, v, a} forms a triangle. Similarly {u, v, b} and {u, v, c} form triangles.

Now, can we find two disjoint cycles? Take triangle {u, v, a} and triangle {w, x, b} where w, x are two other outside vertices connected by a tree edge. These are disjoint if {u,v} ∩ {w,x} = ∅ and a ≠ b. 

So if n-3 ≥ 4 (i.e., n ≥ 7), we can find two disjoint tree edges (u,v) and (w,x) that are vertex-disjoint, and form triangles {u,v,a} and {w,x,b} which are disjoint. So this construction fails for n ≥ 7!

For n = 6: n-3 = 3, so G-S is a tree on 3 vertices (a path of length 2, say u-v-w). The tree edges are (u,v) and (v,w). We can form triangle {u,v,a} and triangle {v,w,b} but these share vertex v. Can we form two disjoint cycles? {u,v,a} uses {u,v,a}, remaining vertices are {w, b, c}. Is there a cycle on {w, b, c}? w-b, w-c, b-c are all edges (since b,c ∈ S form a triangle, and w is connected to all of S). So {w, b, c} is a triangle! And {u, v, a} is a triangle. These are disjoint! So for n=6, this construction also has two disjoint cycles.

Hmm, so the s=3 construction doesn't work as I thought. The issue is that even with a feedback vertex set of size 3, we can still have two disjoint cycles.

Let me reconsider. The Erdős-Pósa theorem says: either k disjoint cycles OR a set of f(k) vertices hitting all cycles. The contrapositive: if no k disjoint cycles, then there's a set of f(k) vertices hitting all cycles. For k=2, f(2) = 3 means: if no 2 disjoint cycles, there's a set of ≤ 3 vertices hitting all cycles.

But having a feedback vertex set of size 3 doesn't prevent two disjoint cycles — it's the other direction. The feedback vertex set of size 3 is a consequence of no two disjoint cycles, not equivalent to it.

So the structure is: no two disjoint cycles ⟹ feedback vertex set of size ≤ 3. But the converse isn't true.

So I need to think about this more carefully. The maximum edges is achieved by some graph with no two disjoint cycles, which must have a feedback vertex set of size ≤ 3, but the constraint is stronger.

Let me think about what graphs on n vertices with no two disjoint cycles look like.

Case 1: Feedback vertex set of size 1, say {v}. Then G - v is a forest. Any cycle goes through v. Two cycles through v share v, so they're not vertex-disjoint. So any graph with a feedback vertex set of size 1 has no two vertex-disjoint cycles. Max edges: v connects to all n-1 others (n-1 edges), plus G-v is a tree (n-2 edges). Total: 2n - 3. But we can also add edges within the neighborhood... wait, no. G - v must be a forest. So edges not involving v: at most n-2. Edges involving v: at most n-1. Total: 2n - 3.

But wait, we could also have v not connected to all vertices. The point is G-v is a forest and v can connect to anyone. Max is 2n-3.

Case 2: Feedback vertex set of size 2, say {a, b}. G - {a,b} is a forest. But we need the additional constraint that there are no two disjoint cycles.

If G - {a,b} is a forest on n-2 vertices, cycles must use a or b. A cycle using only a (from {a,b}) and some forest vertices: this requires a path in the forest between two neighbors of a. Similarly for b.

Two disjoint cycles: one using a (not b) and one using b (not a), with disjoint forest vertices. Or one using both a and b, and another using... well, both cycles need to use at least one of {a,b}, and if they're disjoint, one uses a and the other uses b (they can't both use the same vertex).

So: cycle C1 uses a but not b, cycle C2 uses b but not a, and they're vertex-disjoint (including in the forest part).

To prevent this, we need: for any partition of the forest into two parts, it's not the case that both parts contain a cycle through a (resp. b).

Hmm, this is getting complicated. Let me think about specific constructions.

Actually, let me look at this from a different angle. Let me think about what's known.

I recall that the answer to this problem is m(n) = n + 1 for n ≥ 6. Let me verify this.

Wait, but K_5 has 10 edges for n=5, and 10 > 5+1 = 6. So for n=5, the answer would be different. The problem specifies n ≥ 6.

For n=6: Is m(6) = 7? That seems too low. K_5 + isolated vertex has 10 edges and no two disjoint cycles. So m(6) > 10. So m(6) ≠ 7.

Let me reconsider. Maybe the answer is different.

Let me think about the maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles.

For n=6: K_5 + pendant has 11 edges. Can we do 12? As I argued, connecting the 6th vertex to 2 vertices of K_5 creates two disjoint triangles. What about a non-K_5-based construction?

What about K_4 + 2 extra vertices? K_4 has 4 vertices, 6 edges. Add vertex u connected to all 4 K_4 vertices (4 edges), add vertex v connected to all 4 K_4 vertices (4 edges), and u-v edge (1 edge). Total: 6+4+4+1 = 15 edges. But this definitely has two disjoint cycles (e.g., triangle from K_4 and triangle u-v-a for some a in K_4).

Let me be more careful. What about K_4 + 2 pendant vertices? 6 + 2 = 8 edges. Less than 11.

What about two K_3's sharing a vertex? That's 5 vertices, 6 edges. Add a 6th vertex as pendant: 7 edges. Less than 11.

What about K_5 with one edge subdivided? Take K_5, remove edge (a,b), add vertex v connected to a and b. That's 10 - 1 + 2 = 11 edges, 6 vertices. Does this have two disjoint cycles? The cycles in K_5 - {a,b} edge plus v... v-a-c-b-v is a 4-cycle (if a-c, c-b are edges, which they are in K_5). The remaining vertices are {d, e} (the other two K_5 vertices). {d, e} alone can't form a cycle. So no two disjoint cycles here? Let me check more carefully.

Vertices: a, b, c, d, e, v. Edges: all K_5 edges except (a,b), plus (v,a) and (v,b). So edges: (a,c), (a,d), (a,e), (b,c), (b,d), (b,e), (c,d), (c,e), (d,e), (v,a), (v,b). That's 11 edges.

Cycles: {c,d,e} is a triangle. {a,c,d} is a triangle. {v,a,c,b,v} is a 4-cycle (v-a-c-b-v, using edges v-a, a-c, c-b, b-v). 

Can we find two disjoint cycles? Triangle {c,d,e} uses {c,d,e}. Remaining: {a, b, v}. Edges among them: (v,a), (v,b). No (a,b). So {a,b,v} has only 2 edges, no cycle. 

Triangle {a,c,d} uses {a,c,d}. Remaining: {b,e,v}. Edges: (b,e), (v,b). No (v,e). Only 2 edges, no cycle.

4-cycle {v,a,c,b}: uses {v,a,c,b}. Remaining: {d,e}. Edge (d,e). No cycle.

What about 4-cycle {v,a,d,b}? v-a, a-d, d-b, b-v. Yes. Uses {v,a,d,b}. Remaining: {c,e}. Edge (c,e). No cycle.

4-cycle {v,a,e,b}? v-a, a-e, e-b, b-v. Uses {v,a,e,b}. Remaining: {c,d}. Edge (c,d). No cycle.

What about longer cycles? 5-cycle using 5 of 6 vertices, leaving 1 vertex, can't have two disjoint cycles.

So this graph has 11 edges and no two disjoint cycles. Same as K_5 + pendant.

Can we get 12 edges on 6 vertices with no two disjoint cycles? Let me think...

With 12 edges on 6 vertices, the complement has 15 - 12 = 3 edges. 

Hmm, let me think about this more systematically. The complete graph K_6 has 15 edges. We need to remove at least 3 edges (to get 12) and check if two disjoint cycles are forced.

Actually, let me think about it differently. With 6 vertices, two disjoint cycles must be either:
- Two triangles (using all 6 vertices)
- A triangle and a 4-cycle (needs 7 vertices, impossible with 6)
- Two 4-cycles (needs 8 vertices, impossible)

So with 6 vertices, the only way to have two vertex-disjoint cycles is two disjoint triangles partitioning all 6 vertices.

So the question for n=6 is: what's the maximum number of edges in a graph on 6 vertices with no two disjoint triangles (partitioning the vertex set)?

A graph on 6 vertices has no partition into two triangles. The complement has 3 edges (for 12-edge graph). 

Two disjoint triangles partition {1,...,6} into {a,b,c} and {d,e,f}. This requires all 9 edges: 3 within each triangle and... no, just 3+3 = 6 edges (the triangle edges). The two triangles need 6 edges total.

So a 12-edge graph on 6 vertices: does it always contain two disjoint triangles? 

Hmm, not necessarily. Consider K_6 minus a perfect matching (3 edges removed). That's 12 edges. Does it have two disjoint triangles? K_6 minus a perfect matching: vertices 1,2,3,4,5,6 with missing edges (1,2), (3,4), (5,6). 

Triangle {1,3,5}: edges (1,3), (1,5), (3,5) — all present. Triangle {2,4,6}: edges (2,4), (2,6), (4,6) — all present. These are disjoint! So yes, two disjoint triangles.

What about K_6 minus a star (3 edges from one vertex)? Missing edges: (1,2), (1,3), (1,4). 12 edges. Triangle {2,3,4}: edges (2,3),(2,4),(3,4) — present. Triangle {1,5,6}: needs (1,5),(1,6),(5,6) — (1,5) and (1,6) are present (only (1,2),(1,3),(1,4) missing), (5,6) present. So {1,5,6} is a triangle. Disjoint from {2,3,4}. Yes!

What about K_6 minus a path of 3 edges? Missing: (1,2),(2,3),(3,4). 12 edges. Triangle {1,3,5}: (1,3) present, (1,5) present, (3,5) present. Yes. Triangle {2,4,6}: (2,4) present, (2,6) present, (4,6) present. Yes. Disjoint!

What about K_6 minus a triangle? Missing: (1,2),(2,3),(1,3). 12 edges. Triangle {1,4,5}: (1,4),(1,5),(4,5) all present. Triangle {2,3,6}: (2,3) is MISSING. So {2,3,6} is not a triangle. Try {2,4,6}: (2,4),(2,6),(4,6) all present. And {1,3,5}: (1,3) MISSING. Try {3,4,5}: (3,4),(3,5),(4,5) all present. And {1,2,6}: (1,2) MISSING. 

Hmm, let me be more systematic. Missing edges: (1,2), (2,3), (1,3). So vertex 1 is not connected to 2 or 3, and 2 is not connected to 3. 

Triangles containing vertex 1: must use two of {4,5,6}. {1,4,5}, {1,4,6}, {1,5,6} — all are triangles (since 1 is connected to 4,5,6 and those are all mutually connected).

Triangles containing vertex 2 but not 1: must use two of {4,5,6} (since 2 is not connected to 1 or 3). {2,4,5}, {2,4,6}, {2,5,6} — all triangles.

Triangles containing vertex 3 but not 1 or 2: must use two of {4,5,6}. {3,4,5}, {3,4,6}, {3,5,6} — all triangles.

Now, two disjoint triangles partitioning {1,...,6}:
- {1,4,5} and {2,3,6}: {2,3,6} needs (2,3) — missing. No.
- {1,4,6} and {2,3,5}: {2,3,5} needs (2,3) — missing. No.
- {1,5,6} and {2,3,4}: {2,3,4} needs (2,3) — missing. No.
- {2,4,5} and {1,3,6}: {1,3,6} needs (1,3) — missing. No.
- {2,4,6} and {1,3,5}: {1,3,5} needs (1,3) — missing. No.
- {2,5,6} and {1,3,4}: {1,3,4} needs (1,3) — missing. No.
- {3,4,5} and {1,2,6}: {1,2,6} needs (1,2) — missing. No.
- {3,4,6} and {1,2,5}: {1,2,5} needs (1,2) — missing. No.
- {3,5,6} and {1,2,4}: {1,2,4} needs (1,2) — missing. No.

So K_6 minus a triangle (12 edges) has NO two disjoint triangles, hence no two vertex-disjoint cycles! 

So for n=6, we can have 12 edges without two disjoint cycles. Can we have 13?

K_6 minus 2 edges (13 edges). Missing edges: say (1,2) and (1,3). 

Triangles: {2,3,4}, {2,3,5}, {2,3,6} are all triangles. {1,4,5}, {1,4,6}, {1,5,6} are all triangles.

Disjoint partition: {1,4,5} and {2,3,6}: (1,4),(1,5),(4,5) present; (2,3),(2,6),(3,6) present. Yes! Two disjoint triangles.

What if missing edges are (1,2) and (3,4)? 
{1,3,5} and {2,4,6}: (1,3) present, (1,5) present, (3,5) present — triangle. (2,4) present, (2,6) present, (4,6) present — triangle. Disjoint! Yes.

What if missing edges are (1,2) and (1,3)? Already checked above, has two disjoint triangles.

It seems like with 13 edges (missing only 2), we always get two disjoint triangles. Let me check the case missing (1,2) and (4,5):
{1,3,4} and {2,5,6}: (1,3) present, (1,4) present, (3,4) present — triangle. (2,5) present, (2,6) present, (5,6) present — triangle. Disjoint! Yes.

Missing (1,2) and (5,6):
{1,3,5} and {2,4,6}: (1,3),(1,5),(3,5) present; (2,4),(2,6),(4,6) present. Disjoint triangles!

It seems like any 13-edge graph on 6 vertices has two disjoint triangles. Let me try to prove this.

With 13 edges, 2 edges missing. The two missing edges involve at most 4 vertices. So at least 2 vertices are "complete" (connected to all others). 

Case 1: The two missing edges share a vertex, say (1,2) and (1,3) missing. Then vertices 4,5,6 are complete. {4,5,6} is a triangle. We need a triangle in {1,2,3}. But (1,2) and (1,3) are missing, so the only possible edge in {1,2,3} is (2,3). Not a triangle. So {4,5,6} and a triangle in {1,2,3} doesn't work. But we can use other partitions: {1,4,5} and {2,3,6}. (1,4),(1,5),(4,5) present; (2,3),(2,6),(3,6) present. Yes, disjoint triangles!

Case 2: The two missing edges are disjoint, say (1,2) and (3,4) missing. Vertices 5,6 are complete. {1,3,5} and {2,4,6}: all edges present. Disjoint triangles!

So in all cases, 13 edges on 6 vertices forces two disjoint triangles. 

So for n=6: max edges without two disjoint cycles is 12, and m(6) = 13.

Hmm wait, but I should double-check that 12 is achievable. I showed K_6 minus a triangle works. Let me also check: is there a 12-edge graph that does have two disjoint cycles? Of course, many do. The question is whether ALL 12-edge graphs have two disjoint cycles, and I showed one that doesn't (K_6 minus a triangle). So m(6) = 13.

Now, 13 = 2*6 + 1. Hmm, or 13 = 6 + 7. Let me think about the pattern.

Actually, let me reconsider. For general n, what's the maximum number of edges in a graph with no two vertex-disjoint cycles?

Let me think about the construction that generalizes K_6 minus a triangle. 

K_6 minus a triangle: Take K_3 on vertices {1,2,3} (but remove all 3 edges of this triangle), and K_3 on vertices {4,5,6} (keep all edges), plus all edges between {1,2,3} and {4,5,6}. So it's K_{3,3} ∪ K_3 (on the second part). Edges: 9 (bipartite) + 3 (triangle) = 12. 

Wait, that's K_{3,3} plus a triangle on one side. The independent set {1,2,3} has no internal edges, and {4,5,6} is a clique. Plus all cross edges.

Does this have two disjoint cycles? Any cycle must use at least 2 vertices from {4,5,6} (since {1,2,3} is independent). Actually, a cycle could use vertices from both sides. A triangle needs at least 2 from the clique side (since the independent side has no edges). Actually, a triangle in this graph: must have at least 2 vertices from {4,5,6} (clique) since {1,2,3} is independent. A triangle with 2 clique vertices and 1 independent vertex: {i, a, b} where i ∈ {1,2,3}, a,b ∈ {4,5,6}. A triangle with 3 clique vertices: {4,5,6}.

Two disjoint triangles: one uses ≥2 clique vertices, the other uses ≥2 clique vertices. But there are only 3 clique vertices, so they can't be disjoint. 

What about a triangle and a 4-cycle? Triangle uses ≥2 from clique, 4-cycle uses ≥2 from clique (a 4-cycle in a bipartite-like graph needs at least 2 from each side, but here the clique side has internal edges). Actually, a 4-cycle could be i-a-j-b-i where i,j ∈ {1,2,3} and a,b ∈ {4,5,6}. This uses 2 clique vertices. A triangle uses ≥2 clique vertices. Total ≥4 clique vertices needed, but only 3 available. So no two disjoint cycles.

Great, so this construction works for n=6 with 12 edges.

Now let me generalize. For general n, consider: take a clique K_k and an independent set I of size n-k, with all edges between them. This is a "split graph." 

Edges: C(k,2) + k*(n-k).

Cycles: any cycle needs at least 2 clique vertices (since I is independent). Two disjoint cycles need at least 4 clique vertices total (2 each). So if k ≤ 3, no two disjoint cycles.

For k=3: edges = 3 + 3*(n-3) = 3n - 6.

For k=2: edges = 1 + 2*(n-2) = 2n - 3.

For k=1: edges = 0 + (n-1) = n - 1.

So the split graph with k=3 gives 3n-6 edges and no two disjoint cycles.

For n=6: 3*6 - 6 = 12. Matches!

But can we do better than the split graph? Let me think...

What if instead of an independent set, we have a forest (or tree) on the non-clique vertices?

Take a clique K_3 = {a,b,c} and a tree T on n-3 vertices, with all edges between K_3 and T. Edges: 3 + 3*(n-3) + (n-4) = 3 + 3n - 9 + n - 4 = 4n - 10.

Does this have two disjoint cycles? A cycle can be:
- Within K_3: triangle {a,b,c}
- Using 2 K_3 vertices and a path in T: e.g., a-u-b-a where u is a T vertex adjacent to both a and b (which it is, since all cross edges exist). So {a,u,b} is a triangle for any u in T.
- Using 1 K_3 vertex and a path in T: a-u-v-a where u-v is a T edge and a is connected to both u and v (yes). So {a,u,v} is a triangle.
- Using 2 K_3 vertices and 2 T vertices: a-u-v-b-a, a 4-cycle.
- Etc.

Two disjoint cycles: {a,b,c} (triangle) and a cycle in T ∪ (remaining). But T is a tree, so no cycle in T alone. A cycle using 1 K_3 vertex: but all K_3 vertices are used by {a,b,c}. So if one cycle is {a,b,c}, the other must be entirely in T, which is impossible (T is a tree).

What about two cycles each using some K_3 vertices? E.g., {a, u, v} (triangle, uses a and T vertices u,v) and {b, w, x} (triangle, uses b and T vertices w,x). These are disjoint if {u,v} ∩ {w,x} = ∅. This requires 4 distinct T vertices. So if n-3 ≥ 4, i.e., n ≥ 7, we can find two disjoint triangles!

So for n ≥ 7, this construction (K_3 + tree with all cross edges) has two disjoint cycles. It only works for n = 6 (where n-3 = 3, so we can't find 4 distinct T vertices, and also can't find two disjoint pairs).

Wait, for n=6, T has 3 vertices. Two disjoint triangles each using 1 K_3 vertex need 4 T vertices, impossible. Two disjoint triangles each using 2 K_3 vertices need 4 K_3 vertices, impossible. One triangle using 3 K_3 vertices ({a,b,c}) and one cycle in T: impossible. One triangle using 2 K_3 vertices (say {a,b,u}) and one cycle using 1 K_3 vertex (say {c, v, w}): {c,v,w} is a triangle if v-w is a T edge. {a,b,u} is a triangle. Disjoint if u ∉ {v,w}. T has 3 vertices, so we can pick u, v, w with v-w a T edge and u different. E.g., T = path 1-2-3. u=3, v=1, w=2. {a,b,3} and {c,1,2}. Both triangles, disjoint! 

Wait, so for n=6, the K_3 + tree construction with 4*6-10 = 14 edges has two disjoint cycles? Let me recheck.

K_3 = {a,b,c}, T = path on {1,2,3} with edges (1,2),(2,3). All cross edges present. Total edges: 3 (K_3) + 9 (cross) + 2 (tree) = 14.

Triangle {a,b,3}: edges (a,b), (a,3), (b,3) — all present. Yes.
Triangle {c,1,2}: edges (c,1), (c,2), (1,2) — all present. Yes.
These are disjoint: {a,b,3} ∩ {c,1,2} = ∅. Yes!

So 14 edges on 6 vertices with two disjoint cycles. But we already knew m(6) = 13, so 14 > 13, consistent.

But the question is: can we beat 3n-6 for general n? The split graph with k=3 gives 3n-6. Can we add some edges to the independent set without creating two disjoint cycles?

If we add one edge to the independent set (making it have one edge), say edge (u,v) in I. Then {a,u,v} is a triangle (a ∈ K_3, u,v ∈ I, edges a-u, a-v, u-v all present). Now, can we find a disjoint cycle? {b,c,w} for any w ∈ I \ {u,v} is a triangle (b-c, b-w, c-w all present). If n-3 ≥ 3, i.e., n ≥ 6, there exists w. So {a,u,v} and {b,c,w} are disjoint triangles. So adding even one edge to I creates two disjoint cycles (for n ≥ 6).

Wait, for n=6: I has 3 vertices. Adding edge (1,2). {a,1,2} is a triangle. {b,c,3} is a triangle. Disjoint. Yes, two disjoint cycles. So we can't add any edge to I for n=6.

What about adding edges within K_3? It's already a clique, so no more edges to add.

What about not having all cross edges? If we remove some cross edges, we lose edges, so that doesn't help.

So for the split graph construction, 3n-6 is the max. But maybe there's a completely different construction?

Let me think about other structures. What about K_4 minus an edge (a "diamond") as the core?

Take a diamond D = K_4 - e on 4 vertices {a,b,c,d} with missing edge (a,b). Edges: 5. Add n-4 vertices as an independent set I with all cross edges to D. Edges: 5 + 4*(n-4). 

Does this have two disjoint cycles? Cycles in D: {a,c,d} (triangle), {b,c,d} (triangle), {a,c,b,d,a} (4-cycle). 

Two disjoint cycles: {a,c,d} and a cycle using b and I vertices. {b, u, v} for u,v ∈ I: but I is independent, so need b-u, b-v, u-v. u-v is not an edge. So {b,u,v} is not a triangle. 

A 4-cycle: b-u-a-v-b? b-u (yes), u-a (yes), a-v (yes), v-b (yes). This is a 4-cycle using {b,u,a,v}. Disjoint from {c,d,...}? {a,c,d} uses a, so not disjoint from the 4-cycle. 

Hmm, let me think differently. {c,d} is an edge. {c,d,u} is a triangle for any u ∈ I (c-u, d-u, c-d all present). {a,b,v} — a-b is not an edge, so not a triangle. {a,v,w} for v,w ∈ I — v-w not an edge. 

So triangles are: {a,c,d}, {b,c,d}, {c,d,u} for u ∈ I, {a,c,u}, {a,d,u}, {b,c,u}, {b,d,u} for u ∈ I. And 4-cycles, etc.

Two disjoint triangles: {a,c,d} and {b,?,?} — need two I vertices with an edge, but I is independent. Or {b,c,u} and {a,d,v} — these share no vertices if u ≠ v. {b,c,u}: b-c, c-u, b-u all present. {a,d,v}: a-d, d-v, a-v all present. Disjoint if u ≠ v and {b,c} ∩ {a,d} = ∅ (yes). So if |I| ≥ 2, i.e., n ≥ 6, we have two disjoint triangles!

So the diamond construction fails for n ≥ 6. For n=6, |I|=2, and {b,c,u} and {a,d,v} with u≠v gives two disjoint triangles.

What if we don't have all cross edges? Then we have fewer edges, not helpful.

Let me try another approach. What about K_5-based constructions for general n?

K_5 on {a,b,c,d,e} with 10 edges. Add n-5 vertices. To avoid two disjoint cycles, we need to be careful.

If we add a vertex v connected to only one K_5 vertex, say a, then v is a pendant. No new cycles through v. We can build a tree on the n-5 new vertices, all connected to a. Edges: 10 + (n-5) [tree edges] + (n-5) [connections to a, but the tree already includes a... wait.

Let me be more precise. Take K_5 on {a,b,c,d,e}. Add a tree T on {a, v_1, ..., v_{n-5}} where a is one vertex of the tree. The tree has n-5 edges (connecting the new vertices to the tree including a). Total edges: 10 + (n-5) = n + 5.

Does this have two disjoint cycles? Any cycle is either within K_5 or uses some tree vertices. A cycle using tree vertices must use at least 2 tree edges (to leave and return to K_5). Actually, a cycle through tree vertices: v_i - ... - v_j - (K_5 path) - v_i. This requires two connections from tree to K_5, but the tree only connects to K_5 through vertex a. So any cycle through tree vertices must pass through a twice, which isn't possible in a simple cycle. 

Wait, actually: the tree is on {a, v_1, ..., v_{n-5}}. The only vertex shared with K_5 is a. So any cycle either is entirely within K_5, or passes through a (entering the tree and coming back). But a cycle passing through a and tree vertices: a - v_i - ... - v_j - a. This is a cycle if there's a path from v_i to v_j in the tree not through a, and both v_i and v_j are connected to a. But in a tree, the path from v_i to v_j is unique. If it doesn't go through a, then a-v_i-...-v_j-a is a cycle. But this cycle uses a and some tree vertices.

Two disjoint cycles: one in K_5 (not using a) and one through a and tree vertices. K_5 - a = K_4 on {b,c,d,e}, which has cycles. So {b,c,d} (triangle) and {a, v_i, ..., v_j, a} (cycle through tree). These are disjoint if the tree cycle doesn't use b,c,d,e (it doesn't, it only uses a and tree vertices). So yes, two disjoint cycles!

So this construction fails. The issue is that K_5 - a still has cycles.

What if we use K_5 but make sure that removing any single vertex from K_5 leaves no cycle? That's impossible since K_5 - v = K_4 which has cycles.

So the K_5-based construction with a tree attached through one vertex doesn't work because K_5 minus that vertex still has cycles.

What if we attach the tree through a vertex whose removal from K_5 leaves a tree? K_5 minus any vertex is K_4, which is not a tree. So this doesn't work.

What if we use a different core? Let me think about what cores work.

We need a graph H such that:
1. H has no two disjoint cycles.
2. We can attach a tree to H through a single vertex v, such that H - v has no cycles (i.e., H - v is a forest).

If H - v is a forest, then any cycle in H passes through v. Attaching a tree through v: any cycle in the new graph either is in H (passes through v) or passes through v and tree vertices. Two disjoint cycles would need to not share v, but all cycles pass through v. So no two disjoint cycles.

H - v is a forest means v is a feedback vertex set of size 1 for H. So H has a feedback vertex set of size 1. The max edges for such H on h vertices: v connects to all h-1 others (h-1 edges), H-v is a tree (h-2 edges). Total: 2h - 3.

Now attach n-h tree vertices through v. Tree edges: n - h (connecting new vertices to the tree on {v, ..., } which already has h-1 vertices from H-v plus v). Wait, let me re-think.

H has h vertices. H - v is a forest on h-1 vertices. We attach n-h new vertices as a tree connected through v. The tree on {v, (h-1 vertices of H-v), (n-h new vertices)} — but H-v is already a forest, not necessarily connected.

Actually, let me think of it differently. The whole graph G has:
- Vertex v connected to all others (n-1 edges).
- G - v is a forest on n-1 vertices (at most n-2 edges).
- Total: at most 2n - 3 edges.

And this graph has no two disjoint cycles (all cycles pass through v). This is the case s=1 from before, giving 2n-3 edges.

But 2n-3 < 3n-6 for n ≥ 4 (since 2n-3 < 3n-6 iff n > 3). So the split graph with k=3 (3n-6 edges) is better.

Can we beat 3n-6? Let me think about other constructions.

What about a graph where the feedback vertex set has size 2, but with additional structure to prevent two disjoint cycles?

Let S = {a, b}. G - S is a forest F on n-2 vertices. All edges between S and F, plus edge (a,b). Edges: 1 + 2*(n-2) + (n-3) = 1 + 2n - 4 + n - 3 = 3n - 6. Same as split graph with k=3!

But does this have two disjoint cycles? A cycle using only a (from S): a-u-v-a where u-v is an F edge. A cycle using only b: b-w-x-b where w-x is an F edge. If we can find two disjoint F edges (u,v) and (w,x), then {a,u,v} and {b,w,x} are disjoint triangles.

F is a forest on n-2 vertices. If n-2 ≥ 4, F has at least... well, F could be a path, which has n-3 edges. Two disjoint edges in a path on 4+ vertices: yes, e.g., edges (1,2) and (3,4) in a path 1-2-3-4. So for n ≥ 6, F has ≥ 4 vertices and we can find two disjoint edges, giving two disjoint triangles.

So this construction fails for n ≥ 6. Unless F is a star (all edges share a common vertex). If F is a star centered at some vertex w, then all F edges share w. Two disjoint F edges: impossible. So {a,u,v} and {b,x,y} would need u-v and x-y to be F edges, but all F edges share w, so {u,v} and {x,y} both contain w, meaning the triangles share w. Not disjoint!

But wait, can we also have cycles using both a and b? Like a-u-b-v-a (4-cycle). And a cycle using only a: a-w-x-a where w-x is an F edge (w-x shares center w with all edges, so w is the center). 

Hmm, let me reconsider. If F is a star on n-2 vertices centered at w, with leaves l_1, ..., l_{n-3}:

Cycles:
- {a, b, u} for any u: triangle (a-b, a-u, b-u all present). 
- {a, w, l_i}: triangle (a-w, a-l_i, w-l_i all present).
- {b, w, l_i}: triangle.
- {a, l_i, l_j}: NOT a triangle (l_i-l_j not an edge).
- {a, b, w}: triangle.
- 4-cycle a-l_i-b-l_j-a: a-l_i, l_i-b, b-l_j, l_j-a. All present. Uses {a, b, l_i, l_j}.
- 4-cycle a-w-b-l_i-a: a-w, w-b, b-l_i, l_i-a. All present. Uses {a, w, b, l_i}.

Two disjoint cycles:
- {a, w, l_i} and {b, l_j, l_k}: {b, l_j, l_k} needs l_j-l_k, not an edge. No.
- {a, b, l_i} and {w, l_j, l_k}: {w, l_j, l_k} needs l_j-l_k, not an edge. But {w, l_j, l_k} — w-l_j and w-l_k are edges, l_j-l_k is not. Not a triangle. No.
- {a, w, l_i} and {b, l_j, ?}: need a cycle on {b} ∪ (some leaves). {b, l_j, l_k} not a triangle. 4-cycle b-l_j-?-l_k-b: need l_j-? and ?-l_k edges, but leaves have no edges between them. The only edges among F vertices are w-l_i. So a cycle through b and F vertices: b-l_i-w-l_j-b (4-cycle, uses b, l_i, w, l_j). Disjoint from {a, l_k, ?}... 

{a, l_k, ?}: need a cycle. {a, l_k, ?} — a-l_k is an edge, but l_k has no F edges except to w. So {a, l_k, w} is a triangle (a-l_k, l_k-w, a-w). But this uses w, which is also used by b-l_i-w-l_j-b. Not disjoint.

Hmm, it seems hard to find two disjoint cycles. Let me think more carefully.

Any cycle in this graph: it uses some subset of {a, b} and some F vertices. F is a star, so F edges are only w-l_i. 

A cycle using F vertices must use w (since F is a star, any path between two leaves goes through w, and a cycle needs to return). Actually, a cycle like a-l_i-b-l_j-a uses l_i and l_j but not w (the path goes a-l_i, l_i-b, b-l_j, l_j-a, using S vertices a,b as intermediaries). So this 4-cycle doesn't use w.

A cycle like a-l_i-w-l_j-a: uses w. 

A cycle like a-w-b-a: triangle using a, b, w.

A cycle like a-l_i-b-a: triangle using a, b, l_i.

OK so cycles not using w: {a, b, l_i} (triangle) and a-l_i-b-l_j-a (4-cycle using a, b, l_i, l_j).

Cycles using w: {a, w, l_i}, {b, w, l_i}, {a, b, w}, a-l_i-w-l_j-a, a-w-b-l_i-a, b-l_i-w-l_j-b, etc.

Two disjoint cycles, neither using w: {a, b, l_i} and ... we need a cycle on the remaining vertices not using a, b, l_i. Remaining: w and other leaves. A cycle on {w, l_j, l_k, ...}: w-l_j and w-l_k are edges, but l_j-l_k is not. So no triangle. A longer cycle: w-l_j-?-l_k-w, but ? must be a or b (to connect l_j to l_k), and a, b are used. So no.

Two disjoint cycles, one using w and one not: The one not using w is {a, b, l_i} or a-l_i-b-l_j-a. The one using w: must not use a, b, l_i (if the first is {a,b,l_i}) or a, b, l_i, l_j (if the first is the 4-cycle).

If first is {a, b, l_i}: second must use w and leaves except l_i, and not a, b. Cycle on {w, l_j, l_k, ...}: w-l_j, w-l_k are edges, but no edges between leaves. Need to form a cycle: w-l_j-?-l_k-w, ? must connect l_j to l_k. Only a or b can do that, but they're excluded. So no cycle.

If first is a-l_i-b-l_j-a (uses a, b, l_i, l_j): second must use w and leaves except l_i, l_j, and not a, b. Same issue: no cycle possible without a or b.

Two disjoint cycles both using w: impossible (they share w).

So this construction (K_2 + star forest with all cross edges) has no two disjoint cycles! And it has 3n-6 edges.

But wait, this is the same count as the split graph. Can we add more edges?

The forest F is a star. Can we add edges to F (making it not a forest) while keeping no two disjoint cycles? If we add edge (l_i, l_j), then {a, l_i, l_j} is a triangle, and {b, w, l_k} is a triangle (for k ≠ i, j). These are disjoint if n-2 ≥ 4, i.e., n ≥ 6 (we need at least 4 F vertices: w, l_i, l_j, l_k). So adding any edge to F creates two disjoint cycles for n ≥ 6.

Can we add edges within S? S = {a, b} already has edge (a,b). Can't add more.

Can we remove some cross edges and add others? We already have all cross edges. 

So 3n-6 seems to be the max for this type of construction. But is there a fundamentally different construction that does better?

Let me think about K_5-based constructions again. For n=6, we found 12 = 3*6-6 edges with the split graph. But we also found K_6 minus a triangle = 12 edges. And K_5 + pendant = 11 edges. So 12 is the max for n=6.

Wait, I should check: is 3n-6 achievable for all n ≥ 6, and is it the maximum?

For n=6: 3*6-6 = 12. We showed 12 is achievable and 13 forces two disjoint cycles. So m(6) = 13 = 3*6-6+1 = 3n-5.

Hmm wait, let me reconsider. m(n) = (max edges without two disjoint cycles) + 1. If max is 3n-6, then m(n) = 3n-5.

But I need to verify that 3n-6 is indeed the maximum for all n ≥ 6, not just n=6.

Let me think about n=7. Split graph with k=3: K_3 + independent set of 4, all cross edges. 3 + 3*4 = 15 = 3*7-6. 

Does this have two disjoint cycles? K_3 = {a,b,c}, I = {1,2,3,4}. Triangles: {a,b,c}, {a,b,i}, {a,c,i}, {b,c,i} for i ∈ I. Two disjoint triangles: {a,b,1} and {c,2,3}? {c,2,3} needs 2-3 edge, but I is independent. No. {a,1,2}? Needs 1-2 edge, no. 

Any triangle uses ≥2 vertices from K_3 (since I is independent). Two disjoint triangles need ≥4 K_3 vertices, but |K_3| = 3. Impossible.

4-cycles: a-1-b-2-a (uses a,b,1,2). Triangle {c,3,4}? Needs 3-4 edge, no. 

Two disjoint cycles: one triangle (uses ≥2 from K_3) and one other cycle. The other cycle uses the remaining ≤1 K_3 vertex and some I vertices. With 1 K_3 vertex and I vertices: need a cycle, but I is independent, so need at least 2 K_3 vertices for a cycle (to connect I vertices). With only 1 K_3 vertex, can't form a cycle. 

What about two 4-cycles? a-1-b-2-a and c-3-?-4-c: need 3-? and ?-4 edges. ? must be a K_3 vertex, but a,b,c are used. No.

So the split graph with k=3 has no two disjoint cycles for any n. Good.

Now, can we beat 3n-6 for n=7? Let me think about whether there's a graph on 7 vertices with 16 edges and no two disjoint cycles.

Hmm, this is getting complex. Let me think about the general theory.

I recall that this is a known result. The maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles is 3n - 6 for n ≥ 6, and thus m(n) = 3n - 5.

Wait, actually I'm not sure about this. Let me think more carefully.

Actually, I think the relevant theorem is by Erdős and Pósa, or perhaps by Dirac. Let me think about the structure.

The key insight: a graph with no two vertex-disjoint cycles has a specific structure. By the Erdős-Pósa theorem (or a direct argument), such a graph has a feedback vertex set of size at most 3. But as we saw, having a feedback vertex set of size 3 doesn't prevent two disjoint cycles. The constraint is stronger.

Let me think about this more carefully using the concept of the "core" of the graph.

Actually, I think the answer might be m(n) = n + 4 for n ≥ 6, or something else. Let me reconsider.

Wait, I think I need to be more careful. Let me reconsider the problem.

The problem is asking for the minimum m such that every graph with n vertices and m edges has two vertex-disjoint cycles. This is the extremal number plus 1.

Let me reconsider. For n=6, I showed the max without two disjoint cycles is 12, so m(6) = 13. And 3*6-5 = 13. So m(n) = 3n-5?

But wait, I should double-check for larger n. Let me think about n=7.

For n=7, the split graph K_3 + I_4 gives 15 = 3*7-6 edges. Can we do 16?

Let me try: K_3 = {a,b,c}, and on the other 4 vertices {1,2,3,4}, instead of an independent set, use a single edge, say (1,2). Edges: 3 (K_3) + 3*4 (cross) + 1 (extra) = 16.

Does this have two disjoint cycles? {a,1,2} is a triangle (a-1, a-2, 1-2). {b,c,3} is a triangle (b-c, b-3, c-3). Disjoint! So 16 edges with two disjoint cycles.

What about a different 16-edge construction? Take the split graph (15 edges) and add an edge within K_3... but K_3 is already complete.

What about a non-split construction? Let me think about K_5 + 2 vertices.

K_5 on {a,b,c,d,e}, 10 edges. Add vertices 1,2. Connect 1 to a, 2 to a (pendants). 12 edges. No two disjoint cycles? K_5 - a = K_4 has cycles. So {b,c,d} (triangle) and a cycle through a, 1, 2: a-1-?-2-a, but 1 and 2 are pendants (only connected to a). No path from 1 to 2 except through a. So no cycle through 1,2. But {b,c,d} is a triangle in K_5, and is there another disjoint cycle? {a,e,1}? a-e is edge, a-1 is edge, e-1 is not edge (1 is pendant to a only). Not a triangle. {a,e,2}? Same issue. So the only cycles are within K_5. K_5 has no two disjoint cycles (5 vertices, two disjoint cycles need 6). So this has 12 edges and no two disjoint cycles. Less than 15.

What if we connect 1 and 2 to more K_5 vertices? Connect 1 to a,b and 2 to a,b. Then 1-a-b-1 is a triangle, and {c,d,e} is a triangle in K_5. Disjoint! So 10 + 4 = 14 edges with two disjoint cycles.

Connect 1 to a only, 2 to a only, and 1-2 edge: 10 + 2 + 1 = 13. Cycles: within K_5, and a-1-2-a (triangle). {b,c,d} and {a,1,2}: disjoint! So 13 edges with two disjoint cycles.

Connect 1 to a only, 2 to b only: 10 + 2 = 12. No cycle through 1 or 2 (pendants). No two disjoint cycles (only K_5 cycles). 12 edges.

Connect 1 to a,b and 2 to c only: 10 + 3 = 13. Triangle 1-a-b-1. {c,d,e} triangle. But 2 is pendant to c. {c,d,e} uses c, and 1-a-b uses a,b. Disjoint? {1,a,b} ∩ {c,d,e} = ∅. Yes! Two disjoint cycles. 13 edges.

So K_5 + 2 pendants (12 edges) is the best K_5-based for n=7, much less than 15.

So the split graph construction (3n-6) seems to be the best. Let me now try to prove that 3n-6 is the maximum.

Theorem: For n ≥ 6, the maximum number of edges in a graph on n vertices with no two vertex-disjoint cycles is 3n - 6.

I need to prove:
1. There exists a graph with 3n-6 edges and no two disjoint cycles (the split graph K_3 + independent set with all cross edges).
2. Every graph with 3n-5 edges has two vertex-disjoint cycles.

Part 1 is done (the split graph).

For part 2, I need to show that any graph on n ≥ 6 vertices with 3n-5 edges has two vertex-disjoint cycles.

Let me think about this. Suppose G has n ≥ 6 vertices, 3n-5 edges, and no two vertex-disjoint cycles. I want to derive a contradiction.

By the Erdős-Pósa theorem (k=2 case), G has a feedback vertex set S of size at most 3. (Actually, I need to verify that f(2) = 3 for the Erdős-Pósa theorem. The Erdős-Pósa theorem states that there's a function f(k) such that every graph either contains k vertex-disjoint cycles or has a feedback vertex set of size at most f(k). The bound is f(k) = O(k log k). For k=2, I believe f(2) = 3 or maybe f(2) = 4. Let me think about this directly.)

Actually, let me prove the feedback vertex set bound directly. If G has no two vertex-disjoint cycles, then there's a set S of at most 3 vertices such that G - S is a forest.

Proof: Take any cycle C in G. If C has length ≤ 3, let S = V(C) (at most 3 vertices). Any other cycle must share a vertex with C (since no two disjoint cycles). So removing V(C) kills all cycles, meaning G - V(C) is a forest.

If C has length ≥ 4, take any 3 consecutive vertices of C, say v1, v2, v3. Let S = {v1, v2, v3}. Any cycle D disjoint from S: D is disjoint from {v1, v2, v3} but must share a vertex with C (no two disjoint cycles). So D uses some vertex of C \ {v1, v2, v3}. But D is a cycle in G - S. Hmm, this doesn't immediately show G - S is a forest.

Let me think differently. Take a shortest cycle C in G. If |C| ≤ 3, then V(C) is a feedback vertex set of size ≤ 3 (since any other cycle must intersect C). If |C| ≥ 4, then... hmm, actually any cycle D must share a vertex with C. But D could share a vertex with C that's not in S. So removing S doesn't necessarily kill D.

Let me try a different approach. Take a shortest cycle C. Every other cycle shares a vertex with C. Let S = V(C). Then |S| = |C|, which could be large. That's not helpful.

Better approach: Take a shortest cycle C. |C| = g (girth). Every cycle shares a vertex with C. If g ≤ 3, then S = V(C) has ≤ 3 vertices and G - S is a forest. If g ≥ 4, we need a different argument.

If g ≥ 4: Take any edge e = (u,v) on C. Consider G' = G - {u,v}. Any cycle in G' is a cycle in G not using u or v. It must share a vertex with C. Since it doesn't use u or v, it shares a vertex with C \ {u,v}. So G' still has cycles (potentially). 

Hmm, this is getting complicated. Let me just use the known result. Actually, for k=2, the Erdős-Pósa bound is f(2) = 3. This means: if a graph has no 2 vertex-disjoint cycles, it has a feedback vertex set of size at most 3.

Actually, I think I can prove this directly. Let me try:

Claim: If G has no two vertex-disjoint cycles, then G has a feedback vertex set of size at most 3.

Proof: If G is a forest, done (S = ∅). Otherwise, G has a cycle C. If |C| ≤ 3, let S = V(C). Every cycle intersects C (no two disjoint cycles), so G - S is a forest, and |S| ≤ 3.

If |C| ≥ 4: Since every cycle intersects C, consider the vertices of C: v_1, v_2, ..., v_g (g ≥ 4). Any cycle D in G must contain some v_i. 

Consider G - {v_1, v_2}. Any cycle in G - {v_1, v_2} must contain some v_i for i ≥ 3 (since it must intersect C). So G - {v_1, v_2} might still have cycles, but they all use vertices from {v_3, ..., v_g}.

Now, any cycle in G - {v_1, v_2} must use some v_i (i ≥ 3). Take any such cycle D. D uses some v_i (i ≥ 3). Now, D and C share v_i, so they're not disjoint. But we need to find a feedback vertex set.

Let S = {v_1, v_2, v_3}. Any cycle in G must intersect C. If it intersects C at v_1, v_2, or v_3, then it's killed by S. If it intersects C only at v_4, ..., v_g, then it survives in G - S. But such a cycle D uses some v_j (j ≥ 4) and doesn't use v_1, v_2, v_3. 

Now, C uses v_1, v_2, v_3 (among others). D uses v_j (j ≥ 4) and not v_1, v_2, v_3. But D must intersect C, and it does at v_j. So D and C share v_j. That's fine, they're not disjoint. But I want to show G - S is a forest, which means no cycle survives.

Hmm, this doesn't work. A cycle D that only intersects C at {v_4, ..., v_g} would survive in G - S.

Let me try yet another approach. Take the shortest cycle C = v_1...v_g. Consider any cycle D that doesn't use v_1, v_2, v_3. D must intersect C, so D uses some v_j, j ≥ 4. 

Now, C restricted to {v_4, ..., v_g} is a path v_4-v_5-...-v_g (since C is v_1-v_2-...-v_g-v_1, removing v_1,v_2,v_3 leaves the path v_4-...-v_g, plus the edge v_g-v_1 is gone since v_1 is removed, and v_3-v_4 is gone since v_3 is removed).

D uses v_j (j ≥ 4) and possibly other vertices. D is a cycle in G - {v_1,v_2,v_3}. 

Now, I claim that D together with a subpath of C creates a shorter cycle, contradicting the minimality of C. 

D uses v_j and v_k (two vertices of C, j,k ≥ 4, since D must intersect C and we removed v_1,v_2,v_3 — actually D only needs to intersect C at one vertex, but let me think about whether D must use at least 2 C-vertices).

Actually, D doesn't need to use 2 vertices of C. D could use just v_4 and then other non-C vertices. But D is a cycle, so it's a closed walk. If D uses v_4 and then goes through non-C vertices and comes back to v_4, that's a cycle. This cycle doesn't use any other C vertex.

In that case, consider the cycle C' formed by: the path from v_4 to v_1 along C (v_4-v_3-v_2-v_1), then... hmm, this doesn't directly help.

Let me try a completely different approach. Maybe I should use the following known result:

Theorem (Dirac, 1963 or Erdős-Pósa): A graph with n vertices and no two vertex-disjoint cycles has at most 3n - 6 edges (for n ≥ 6).

Actually, I think this might be a theorem by Dirac or by Erdős. Let me think about whether I can prove it.

Alternative approach: induction on n.

Base case n = 6: We showed max is 12 = 3*6 - 6. ✓

Inductive step: Assume for n-1, max is 3(n-1) - 6 = 3n - 9. Show for n, max is 3n - 6.

Take G on n vertices with no two disjoint cycles. If G has a vertex v of degree ≤ 2, then G - v has n-1 vertices and no two disjoint cycles, so e(G-v) ≤ 3(n-1) - 6 = 3n - 9. Then e(G) ≤ 3n - 9 + 2 = 3n - 7 < 3n - 6. 

So if there's a vertex of degree ≤ 2, we're fine (even stronger). The issue is when all vertices have degree ≥ 3.

If all vertices have degree ≥ 3, then e(G) ≥ 3n/2. And we want to show e(G) ≤ 3n - 6.

Hmm, this doesn't directly help. Let me think about the minimum degree case.

If δ(G) ≥ 3, then G has a cycle. In fact, G has many cycles. The constraint is no two disjoint cycles.

Let me think about the structure. If G has no two disjoint cycles and δ(G) ≥ 3, what can we say?

Take a shortest cycle C. Every cycle intersects C. If |C| = 3, then the 3 vertices of C form a feedback vertex set. G - C is a forest on n-3 vertices with at most n-4 edges. The 3 vertices of C have at most 3 edges among them (it's a triangle) and at most 3*(n-3) edges to the rest. Total: 3 + 3(n-3) + (n-4) = 4n - 10. But we need to account for the constraint that no two disjoint cycles exist, which limits the edges further.

Wait, I showed earlier that with a triangle C and all cross edges and a tree on G-C, we get 4n-10 edges but this has two disjoint cycles for n ≥ 7. So the constraint is more subtle.

Let me think about this differently. With a triangle C = {a,b,c} as feedback vertex set:
- G - C is a forest F on n-3 vertices.
- Edges within C: at most 3 (triangle).
- Edges between C and F: at most 3(n-3).
- Edges within F: at most n-4 (forest).
- Total: at most 3 + 3(n-3) + (n-4) = 4n - 10.

But we need the additional constraint: no two disjoint cycles. As I showed, if F has two disjoint edges and the cross edges are complete, we get two disjoint triangles. So either:
(a) F doesn't have two disjoint edges (F is a star or has ≤ 3 vertices), or
(b) The cross edges are not complete.

Case (a): F is a star on n-3 vertices (center w, leaves l_1,...,l_{n-4}) or n-3 ≤ 3.
- If n-3 ≤ 3 (n ≤ 6): F has at most 2 edges. Total: 3 + 3(n-3) + (n-4) = 4n-10. For n=6: 14. But we showed m(6)=13, so max is 12. So even with n=6, the constraint is tighter.

Hmm wait, for n=6, F has 3 vertices. If F is a path (2 edges), total = 3 + 9 + 2 = 14. But we showed this has two disjoint cycles. If F is a star (2 edges, same as path for 3 vertices), same issue. If F has 1 edge, total = 3 + 9 + 1 = 13. Does this have two disjoint cycles? F = edge (1,2) plus isolated vertex 3. {a,1,2} is a triangle. {b,c,3} is a triangle. Disjoint! So 13 edges with two disjoint cycles. If F has 0 edges, total = 3 + 9 + 0 = 12. This is the split graph, which works.

So for n=6, the constraint forces F to have 0 edges (independent set), giving 12 = 3*6-6.

For n=7: F has 4 vertices. To avoid two disjoint cycles:
- If F is a star (3 edges): total = 3 + 12 + 3 = 18. But does this have two disjoint cycles? Star center w, leaves l1,l2,l3. {a,w,l1} and {b,c,l2}: both triangles, disjoint. Yes! So 18 has two disjoint cycles.
- If F has 2 edges: say (1,2) and (2,3) (a path). {a,1,2} and {b,c,4}: both triangles, disjoint (n-3=4, vertex 4 exists). Yes.
- If F has 1 edge: (1,2). {a,1,2} and {b,c,3}: disjoint triangles. Yes (vertex 3 exists since n-3=4 ≥ 3).
- If F has 0 edges: 3 + 12 + 0 = 15 = 3*7-6. This is the split graph, works.

So for n=7 with complete cross edges, F must be an independent set, giving 3n-6.

But what if the cross edges are not complete? Can we compensate by having more F edges?

Suppose we remove one cross edge, say (a, 1), and add one F edge, say (1,2). Total: 3 + (3(n-3) - 1) + (n-4 + 1) = 3 + 3n-9-1 + n-3 = 4n - 10. Same total. But does this avoid two disjoint cycles?

{a,1,2}: needs a-1 (removed!), so not a triangle. {b,1,2}: b-1, b-2, 1-2 all present. Triangle. {a,c,3}: a-3, c-3, a-c all present. Triangle. Disjoint from {b,1,2}? {b,1,2} ∩ {a,c,3} = ∅. Yes! Two disjoint cycles.

So this doesn't help. The problem is that even if we remove one cross edge from a, we can still form triangles using b or c.

What if we remove all cross edges from a to F? Then a is only connected to b,c. Edges: 3 (triangle) + 2*(n-3) (cross from b,c) + (n-4) (F edges) = 3 + 2n-6 + n-4 = 3n - 7. Less than 3n-6.

And does this avoid two disjoint cycles? Cycles through a: must use b or c (since a only connects to b,c). {a,b,c} is a triangle. a-b-...-c-a: a path from b to c not through a. Cycles through b (not a): b-u-v-b where u-v is an F edge. Cycles through c (not a): similar.

Two disjoint cycles: {a,b,c} and a cycle in F: F is a forest, no cycle. {a,b,x} and {c,y,z}: {a,b,x} needs a-x, but a has no cross edges. So {a,b,x} is only a triangle if x ∈ {c} (already {a,b,c}). So the only triangle using a is {a,b,c}. 

Other triangles: {b,c,u} for u ∈ F (b-u, c-u, b-c all present). {b,u,v} for F edge (u,v). {c,u,v} for F edge (u,v).

Two disjoint cycles: {b,u,v} (F edge u-v) and {a,c,w} — but a-c is edge, a-w is not (no cross edges from a). Not a triangle. {b,u,v} and {c,w,x} — needs F edge w-x disjoint from u-v. If F has two disjoint edges, yes.

So if F has two disjoint edges, we get two disjoint cycles ({b,u,v} and {c,w,x}). If F is a star (no two disjoint edges), then no two disjoint cycles from this. But then F has at most n-4 edges (star on n-3 vertices). Total: 3 + 2(n-3) + (n-4) = 3n - 7. Still less than 3n-6.

What if a connects to some F vertices but not all? Say a connects to k F vertices. Then cross edges: 2(n-3) + k. F edges: at most n-4 (if F is a forest). Total: 3 + 2(n-3) + k + (n-4) = 3n - 7 + k.

To get 3n - 6, we need k = 1. So a connects to exactly 1 F vertex, say vertex 1. Cross edges: 2(n-3) + 1. F edges: n-4. Total: 3 + 2n-6 + 1 + n-4 = 3n - 6.

Does this avoid two disjoint cycles? F is a forest (n-4 edges, so a tree on n-3 vertices). a connects to b, c, and vertex 1.

Cycles: {a,b,c} (triangle). {b,c,u} for u ∈ F (triangle). {b,u,v} for F edge (u,v) (triangle). {c,u,v} for F edge (u,v) (triangle). {a,b,1} (triangle, a-1 is edge). {a,c,1} (triangle). a-1-...-b-a or a-1-...-c-a (longer cycles through a, 1, and F).

Two disjoint cycles: {a,b,1} and {c,u,v} where (u,v) is an F edge not involving 1. If F has an edge not involving 1, then {c,u,v} is a triangle disjoint from {a,b,1}. 

F is a tree on n-3 vertices including vertex 1. If n-3 ≥ 2 (n ≥ 5), F has at least 1 edge. If that edge involves 1, say (1,2), then we need another edge not involving 1. If n-3 ≥ 3 (n ≥ 6), F has at least 2 edges, and at most 1 involves 1 (in a tree, vertex 1 has some degree). If vertex 1 is a leaf, only 1 edge involves it, and the other n-5 edges don't. So for n ≥ 6, there exists an F edge (u,v) not involving 1, and {c,u,v} is a triangle disjoint from {a,b,1}.

So this construction fails for n ≥ 6! The only way to avoid two disjoint cycles is to have no F edges at all (F is independent), which gives the split graph with 3n-6 edges.

Wait, but I assumed F is a tree (n-4 edges). What if F has fewer edges? If F has n-5 edges (one less than a tree), total = 3n-7. Still less.

So it seems like 3n-6 is indeed the maximum, achieved only by the split graph (K_3 + independent set with all cross edges).

But I need to be more rigorous. Let me also consider the case where the feedback vertex set has size 1 or 2 (not 3).

Case s=1: feedback vertex set {v}. Max edges: 2n-3. For n ≥ 6, 2n-3 < 3n-6 iff n > 3. So s=1 gives fewer edges.

Case s=2: feedback vertex set {a,b}. G-{a,b} is a forest F on n-2 vertices. Max edges: 1 + 2(n-2) + (n-3) = 3n-6. Same as s=3! But we need to check the no-two-disjoint-cycles constraint.

With complete cross edges and F a tree: {a,u,v} and {b,w,x} for disjoint F edges (u,v) and (w,x). If F has two disjoint edges (n-2 ≥ 4, n ≥ 6), two disjoint triangles. So F must be a star (no two disjoint edges).

F is a star on n-2 vertices: n-3 edges. Total: 1 + 2(n-2) + (n-3) = 3n-6. Same count!

But does the star construction avoid two disjoint cycles? I analyzed this earlier and found it does (for the K_2 + star case). Let me re-verify.

S = {a,b}, F = star centered at w with leaves l_1,...,l_{n-4}. All cross edges present, edge (a,b) present.

As I analyzed before, any cycle either uses both a and b, or uses exactly one of {a,b} and some F vertices. Two disjoint cycles: one using a (not b) and one using b (not a). The one using a: a-u-...-v-a, needs a path in F. F is a star, so any path between two leaves goes through w. So the cycle is a-l_i-w-l_j-a (4-cycle) or a-w-l_i-a (triangle, using a-w and w-l_i and a-l_i). Similarly for b.

Two disjoint: a-l_i-w-l_j-a and b-l_k-w-l_m-b: both use w. Not disjoint.
a-l_i-a (not a cycle, just back and forth). 
a-w-l_i-a (triangle, uses a, w, l_i) and b-l_j-...-b: b-l_j-w-l_k-b (4-cycle, uses b, l_j, w, l_k). Both use w. Not disjoint.
{a, w, l_i} and {b, l_j, l_k}: {b,l_j,l_k} needs l_j-l_k, not an edge. No.
{a, b, l_i} and {w, l_j, l_k}: {w,l_j,l_k} needs l_j-l_k, not an edge. No.
{a, b, l_i} and {w, l_j, ?}: can't form a cycle without a or b.
{a, b, w} and cycle in F: F is a star (tree), no cycle.

What about {a, b, l_i} (triangle) and a cycle using w and leaves (not a, b, l_i)? Cycle on {w, l_j, l_k, ...} without a,b: need edges between leaves, but there are none. No cycle.

What about 4-cycle a-l_i-b-l_j-a (uses a, b, l_i, l_j) and a cycle on {w, l_k, ...}? Same issue, no cycle without a or b.

So indeed, the K_2 + star construction has no two disjoint cycles and 3n-6 edges. Same as the split graph.

Now, the key question: can we beat 3n-6? We've seen that with s=3 (triangle feedback vertex set), we get at most 3n-6 (split graph). With s=2, we get at most 3n-6 (K_2 + star). With s=1, at most 2n-3 < 3n-6.

But what about graphs where the feedback vertex set has size 3 but is not a triangle? Or graphs with more complex structure?

Let me consider s=3 with S = {a,b,c} not forming a triangle. Say edges in S: (a,b) and (b,c) but not (a,c). Then:
- Edges in S: 2
- Cross edges: at most 3(n-3)
- F edges: at most n-4 (forest)
- Total: 2 + 3(n-3) + (n-4) = 4n - 11

But we need no two disjoint cycles. With all cross edges and F a tree:
{a,b,u} (triangle, a-b, a-u, b-u) and {c,v,w} (triangle, c-v, c-w, v-w F edge). Disjoint if (v,w) is an F edge not involving u. For n ≥ 7, such an edge exists. So this fails.

If F is a star: {a,b,u} and {c,w,l_j} where w is center, l_j a leaf, u a leaf ≠ l_j. {c,w,l_j}: c-w, c-l_j, w-l_j all present. Triangle. {a,b,u}: a-b, a-u, b-u. Triangle. Disjoint if u ≠ w and u ≠ l_j. Since F has n-3 ≥ 4 vertices (n ≥ 7), we can choose u, l_j distinct leaves. So disjoint triangles exist.

For n=6: F has 3 vertices, star has 2 leaves. {a,b,u} and {c,w,l_j}: u and l_j are the 2 leaves, distinct. {c,w,l_j} is a triangle. {a,b,u} is a triangle. Disjoint. So even for n=6, this fails.

So with S not a triangle, we can't achieve 3n-6 without two disjoint cycles (for n ≥ 6). The maximum is less.

What if S has only 2 edges (a path a-b-c) and we don't have all cross edges? We'd need to remove cross edges to prevent two disjoint cycles, losing edges. The total would be less than 3n-6.

So it seems like 3n-6 is the maximum, achieved by:
1. Split graph: K_3 + independent set, all cross edges. (s=3, S is a triangle)
2. K_2 + star, all cross edges, edge in S. (s=2, S is an edge)

Both give 3n-6.

Now I need to prove that 3n-5 edges always force two disjoint cycles. Let me try to prove this by induction.

Theorem: For n ≥ 6, every graph with n vertices and 3n-5 edges has two vertex-disjoint cycles.

Proof by induction on n.

Base case n=6: 3*6-5 = 13 edges. We showed that any 13-edge graph on 6 vertices has two disjoint triangles (hence two disjoint cycles). ✓

Inductive step: Assume the theorem holds for n-1 (n ≥ 7). Let G be a graph on n vertices with 3n-5 edges. Suppose for contradiction G has no two vertex-disjoint cycles.

If G has a vertex v with degree ≤ 2, then G-v has n-1 vertices and at least 3n-5-2 = 3n-7 = 3(n-1)-4 edges. Since 3(n-1)-4 > 3(n-1)-5 (for n ≥ 7, 3(n-1)-4 = 3n-7 > 3n-8 = 3(n-1)-5), by induction G-v has two disjoint cycles, hence G does too. Contradiction.

Wait, 3(n-1)-5 = 3n-8. And 3n-7 > 3n-8. So G-v has ≥ 3n-7 > 3(n-1)-5 edges, so by induction, G-v has two disjoint cycles. ✓

So we may assume δ(G) ≥ 3.

If δ(G) ≥ 3, then every vertex has degree ≥ 3. The sum of degrees is 2(3n-5) = 6n-10. Average degree is (6n-10)/n = 6 - 10/n, which is less than 6 for all n. So there's a vertex of degree ≤ 5.

Hmm, I need a vertex of degree ≤ 2 to make the induction work, but we're in the case δ ≥ 3. Let me think differently.

If δ(G) ≥ 3, I need to show G has two disjoint cycles directly (or derive a contradiction).

Since G has no two disjoint cycles, by the feedback vertex set argument, G has a feedback vertex set S of size ≤ 3. 

Case 1: |S| = 1, S = {v}. G-v is a forest. e(G) ≤ (n-1) + (n-2) = 2n-3. But e(G) = 3n-5 > 2n-3 for n ≥ 3. Contradiction.

Case 2: |S| = 2, S = {a,b}. G-{a,b} is a forest F on n-2 vertices. 
e(G) = e(S) + e(S,F) + e(F) ≤ 1 + 2(n-2) + (n-3) = 3n-6.
But e(G) = 3n-5 > 3n-6. Contradiction.

Wait, but this assumes the maximum is 3n-6, which is what we're trying to prove! The bound e(G) ≤ 1 + 2(n-2) + (n-3) = 3n-6 is just the trivial bound (S has at most 1 edge, cross at most 2(n-2), F at most n-3). This doesn't use the no-two-disjoint-cycles constraint beyond the feedback vertex set.

So: if |S| = 2, e(G) ≤ 3n-6 < 3n-5. Contradiction. ✓

Case 3: |S| = 3, S = {a,b,c}. G-S is a forest F on n-3 vertices.
e(G) = e(S) + e(S,F) + e(F) ≤ 3 + 3(n-3) + (n-4) = 4n-10.
For n ≥ 6, 4n-10 > 3n-5 (since 4n-10 > 3n-5 iff n > 5). So the trivial bound doesn't give a contradiction.

I need to use the no-two-disjoint-cycles constraint more carefully for |S| = 3.

So the hard case is |S| = 3. Let me analyze this.

S = {a,b,c}, G-S is a forest F on n-3 vertices. e(G) = 3n-5.

e(S) ≤ 3, e(S,F) ≤ 3(n-3), e(F) ≤ n-4. Total ≤ 4n-10.

We need e(G) = 3n-5. So 3n-5 ≤ 4n-10, i.e., n ≥ 5. OK for n ≥ 6.

Now, the no-two-disjoint-cycles constraint. Let me think about what restrictions this imposes.

If S is a triangle (e(S) = 3) and all cross edges present (e(S,F) = 3(n-3)):
e(F) = 3n-5 - 3 - 3(n-3) = 3n-5-3-3n+9 = 1. So F has exactly 1 edge.

F has n-3 ≥ 3 vertices and 1 edge, say (u,v). Then {a,u,v} is a triangle (a-u, a-v, u-v). And {b,c,w} for any w ∈ F \ {u,v} is a triangle (b-c, b-w, c-w). If n-3 ≥ 3 (n ≥ 6), there exists w. These are disjoint. Contradiction.

If S is a triangle (e(S) = 3) and e(S,F) = 3(n-3) - 1 (one cross edge missing, say a-u):
e(F) = 3n-5 - 3 - (3n-9-1) = 3n-5-3-3n+10 = 2. F has 2 edges.

F has n-3 ≥ 3 vertices and 2 edges. 

Subcase: F has two edges sharing a vertex (a path u-v-w). {b,u,v} is a triangle (b-u, b-v, u-v). {c,v,w} is a triangle (c-v, c-w, v-w). But these share v. {b,u,v} and {c,w,x}? Need w-x edge, but F only has edges (u,v) and (v,w). No w-x edge. {a,v,w}? a-v is edge, a-w is edge (only a-u is missing), v-w is edge. Triangle! {b,c,u}? b-c, b-u, c-u. Triangle. Disjoint from {a,v,w}? {a,v,w} ∩ {b,c,u} = ∅. Yes! Two disjoint cycles.

Hmm wait, I said a-u is missing. So a is connected to all F vertices except u. So a-v and a-w are present. {a,v,w}: a-v ✓, a-w ✓, v-w ✓ (F edge). Triangle. {b,c,u}: b-c ✓, b-u ✓, c-u ✓. Triangle. Disjoint. Contradiction.

Subcase: F has two disjoint edges (u,v) and (w,x). {a,u,v} — a-u is missing! So not a triangle. {b,u,v}: b-u, b-v, u-v. Triangle. {c,w,x}: c-w, c-x, w-x. Triangle. Disjoint. Contradiction.

So with e(S)=3, e(S,F) = 3(n-3)-1, we still get contradictions.

What if e(S,F) = 3(n-3) - 2 (two cross edges missing)?
e(F) = 3n-5-3-(3n-9-2) = 3n-5-3-3n+11 = 3. F has 3 edges.

This is getting complicated. Let me think about this more systematically.

Let me denote:
- e_S = edges within S (≤ 3)
- e_F = edges within F (≤ n-4, since F is a forest)
- e_cross = edges between S and F (≤ 3(n-3))

e_S + e_F + e_cross = 3n - 5.

The no-two-disjoint-cycles constraint: I need to figure out what combinations of (e_S, e_F, e_cross) are possible.

Key observation: If S is a triangle and there exist two disjoint edges in F, and the cross edges are "complete enough," we get two disjoint triangles.

Let me think about it in terms of what's needed to prevent two disjoint cycles.

With S = {a,b,c} a triangle, F a forest:

Two disjoint cycles can be:
1. Two triangles, each using ≥ 2 S-vertices: impossible (only 3 S-vertices).
2. One triangle using 2 S-vertices + 1 F-vertex, and one triangle using 1 S-vertex + 2 F-vertices (with an F edge): e.g., {a,b,u} and {c,v,w} where (v,w) is an F edge and u ∉ {v,w}.
3. One triangle using 3 S-vertices ({a,b,c}), and one cycle in F: impossible (F is a forest).
4. One triangle using 2 S-vertices + 1 F-vertex, and one cycle using 2 S-vertices + ≥ 2 F-vertices: impossible (need 4 S-vertices).
5. Two cycles each using 1 S-vertex + ≥ 2 F-vertices: e.g., {a,u,v} and {b,w,x} where (u,v) and (w,x) are F edges, disjoint. Need 2 disjoint F edges.
6. One triangle using 3 S-vertices ({a,b,c}) and one triangle using 0 S-vertices: impossible (F is a forest, no triangle).
7. One cycle using 2 S-vertices + ≥ 2 F-vertices, and another using 1 S-vertex + ≥ 2 F-vertices: e.g., a-u-b-v-a (4-cycle, uses a,b,u,v) and {c,w,x} (triangle, uses c,w,x with w-x F edge). Disjoint if {u,v} ∩ {w,x} = ∅.

So the main threats are:
- Type 2: {a,b,u} and {c,v,w} with F edge (v,w), u ∉ {v,w}.
- Type 5: {a,u,v} and {b,w,x} with F edges (u,v) and (w,x), disjoint.
- Type 7: a-u-b-v-a and {c,w,x} with F edges (u,v) (wait, a-u-b-v-a uses a-u, u-b, b-v, v-a, not F edges; it uses cross edges and the a-b edge). Hmm, let me reconsider. a-u-b-v-a: edges a-u (cross), u-b (cross), b-v (cross), v-a (cross). This is a 4-cycle using a, b, u, v. It doesn't need F edges. And {c,w,x} needs F edge (w,x). Disjoint if {u,v} ∩ {w,x} = ∅.

So Type 7: 4-cycle a-u-b-v-a (using cross edges, needs a-b edge) and triangle {c,w,x} (needs F edge w-x and cross edges c-w, c-x). Disjoint if {u,v} ∩ {w,x} = ∅.

To prevent all these, we need strong conditions. Let me think about what conditions on F and the cross edges prevent all types.

This is getting quite involved. Let me try a different approach to the proof.

Alternative approach: Direct proof using the structure.

Let me use the following lemma:

Lemma: If G has no two vertex-disjoint cycles and n ≥ 6 vertices, then e(G) ≤ 3n - 6.

Proof: By induction on n.

Base case n = 6: Verified (max is 12 = 3*6-6).

Inductive step (n ≥ 7): Assume the lemma for all graphs on n-1 vertices. Let G be a graph on n vertices with no two disjoint cycles.

If G has a vertex v with deg(v) ≤ 2: G-v has n-1 vertices, no two disjoint cycles, so e(G-v) ≤ 3(n-1)-6 = 3n-9. Then e(G) ≤ 3n-9+2 = 3n-7 < 3n-6. ✓

If δ(G) ≥ 3: We need to show e(G) ≤ 3n-6.

Since G has no two disjoint cycles, G has a feedback vertex set S with |S| ≤ 3 (I'll prove this below). 

If |S| ≤ 2: e(G) ≤ C(2,2) + 2(n-2) + (n-3) = 1 + 2n-4 + n-3 = 3n-6. ✓ (This is the trivial bound, and it equals 3n-6.)

If |S| = 3: e(G) ≤ 3 + 3(n-3) + (n-4) = 4n-10. This is > 3n-6 for n ≥ 5. So we need the no-two-disjoint-cycles constraint.

Hmm, so the |S| = 3 case is the hard one, and the trivial bound isn't enough. I need to use the structure more carefully.

Let me think about the |S| = 3 case with δ(G) ≥ 3.

S = {a,b,c}, F = G-S is a forest on n-3 vertices. δ(G) ≥ 3 means every vertex has degree ≥ 3.

For a vertex u in F: deg(u) = deg_F(u) + deg_S(u) ≥ 3. deg_F(u) is the degree in the forest, deg_S(u) is the number of S-vertices adjacent to u (0 to 3).

If deg_S(u) = 0: deg_F(u) ≥ 3, but F is a forest, so max degree in F can be high. But a vertex in a forest with degree ≥ 3 is possible. However, if u has deg_S(u) = 0, u is not adjacent to any S vertex. Any cycle through u must be in F, but F is a forest (no cycles). So u is not in any cycle. But δ ≥ 3 and u has no S neighbors, so u has ≥ 3 F-neighbors. 

Actually, if deg_S(u) = 0, then u is only connected to F vertices. Since F is a forest, u is in no cycle. But we need deg(u) ≥ 3, so deg_F(u) ≥ 3. This is possible in a forest (e.g., a star center).

But here's the thing: if deg_S(u) = 0 for some u, then u is not in any cycle. Consider G' = G - u. G' has n-1 vertices and no two disjoint cycles (subgraph of G). By induction, e(G') ≤ 3(n-1)-6 = 3n-9. Then e(G) = e(G') + deg(u) ≤ 3n-9 + deg(u). 

If deg(u) ≤ 3: e(G) ≤ 3n-9+3 = 3n-6. ✓
If deg(u) ≥ 4: e(G) ≤ 3n-9+deg(u), which could exceed 3n-6.

Hmm, but if deg_S(u) = 0 and deg_F(u) ≥ 4, u is a high-degree vertex in the forest F. 

Actually wait, I think I can handle this differently. Let me consider the minimum degree vertex.

Since δ(G) ≥ 3, let v be a vertex of minimum degree d = δ(G) ≥ 3. G - v has n-1 vertices and no two disjoint cycles. By induction, e(G-v) ≤ 3(n-1)-6 = 3n-9. So e(G) ≤ 3n-9 + d.

If d ≤ 3: e(G) ≤ 3n-9+3 = 3n-6. ✓

So the only problematic case is d ≥ 4, i.e., δ(G) ≥ 4.

If δ(G) ≥ 4: sum of degrees ≥ 4n, so e(G) ≥ 2n. And e(G) = 3n-5 (what we're trying to contradict). So 3n-5 ≥ 2n, i.e., n ≥ 5. OK.

With δ(G) ≥ 4 and no two disjoint cycles, feedback vertex set S of size ≤ 3.

For u in F: deg(u) = deg_F(u) + deg_S(u) ≥ 4. Since deg_S(u) ≤ 3, deg_F(u) ≥ 1. So every F vertex has degree ≥ 1 in F, meaning F has no isolated vertices. Since F is a forest with no isolated vertices, F is a union of trees each with ≥ 2 vertices.

Also, deg_S(u) ≥ 4 - deg_F(u). If deg_F(u) = 1 (leaf in F), deg_S(u) ≥ 3, so u is adjacent to all of a, b, c. If deg_F(u) = 2, deg_S(u) ≥ 2.

Now, let me count edges more carefully.

e(G) = e_S + e_cross + e_F.

We want to show e(G) ≤ 3n-6, i.e., e_S + e_cross + e_F ≤ 3n-6.

e_F ≤ n-4 (forest on n-3 vertices, at most n-4 edges). Actually, if F has no isolated vertices and n-3 vertices, F has at least ceil((n-3)/2) edges (each tree has at least 1 edge for 2 vertices). But the upper bound is n-4 (tree).

e_S ≤ 3.
e_cross ≤ 3(n-3).

So e(G) ≤ 3 + 3(n-3) + (n-4) = 4n-10. We need to bring this down to 3n-6, so we need to save n-4 edges from the trivial bound.

The no-two-disjoint-cycles constraint must save us n-4 edges. Let me think about how.

Key constraint: no two disjoint cycles. With S = {a,b,c} and F a forest:

If S is a triangle and all cross edges are present, then any F edge (u,v) creates triangle {a,u,v} (or {b,u,v} or {c,u,v}). Two disjoint F edges create two disjoint triangles (using different S vertices). So F can have at most... well, if F has two disjoint edges, we get two disjoint triangles (Type 5). So F must be a star (matching number 1) or have at most 3 vertices.

If F is a star on n-3 vertices: e_F = n-4. And we need all cross edges present and S a triangle for the max. But then: {a,b,u} (triangle, u a leaf) and {c,w,l} where w is center, l another leaf. {c,w,l}: c-w, c-l, w-l. Triangle. Disjoint from {a,b,u} if u ∉ {w,l}. Since n-3 ≥ 4 (n ≥ 7), there are ≥ 3 leaves, so we can pick u, l distinct. Contradiction!

So for n ≥ 7, even a star F with all cross edges and S a triangle gives two disjoint cycles. The only way to avoid this is to not have all cross edges or not have S as a triangle.

This suggests that for n ≥ 7, the maximum is strictly less than 4n-10, and in fact at most 3n-6.

Let me try to prove this more carefully.

Claim: For n ≥ 6, if G has no two disjoint cycles, |S| = 3 (feedback vertex set), and S is a triangle, then e_cross + e_F ≤ 3(n-3) + 0 = 3(n-3), i.e., e_F = 0 (F is an independent set) when e_cross = 3(n-3) (all cross edges present).

More generally, I want to show e_S + e_cross + e_F ≤ 3n-6.

Let me think about it as: e_S + e_cross + e_F ≤ 3 + e_cross + e_F, and I want this ≤ 3n-6, so e_cross + e_F ≤ 3n-9 = 3(n-3).

Since e_cross ≤ 3(n-3) and e_F ≤ n-4, the sum is at most 3(n-3) + (n-4) = 4n-13. We need this ≤ 3(n-3) = 3n-9, so we need e_F ≤ 3(n-3) - e_cross, i.e., the "missing" cross edges must be at least e_F.

In other words: (missing cross edges) ≥ e_F, i.e., 3(n-3) - e_cross ≥ e_F.

Is this true? Let me think about why.

For each F edge (u,v), to prevent triangle {a,u,v}, at least one of a-u, a-v must be missing. Similarly for b and c. But we don't need to prevent all three triangles {a,u,v}, {b,u,v}, {c,u,v} — we just need to prevent two disjoint cycles.

Hmm, actually, the constraint is more subtle. Let me think about specific cases.

If F has an edge (u,v) and all three cross edges from a, b, c to both u and v are present, then {a,u,v}, {b,u,v}, {c,u,v} are all triangles. Now, {a,u,v} and {b,c,w} (for w ∈ F, w ≠ u,v) are disjoint triangles (if n-3 ≥ 3, i.e., n ≥ 6). So to prevent this, for each F edge (u,v), at least one S-vertex must be missing an edge to u or v.

But that's not quite right either. {a,u,v} and {b,c,w}: we need w to exist (n ≥ 6) and b-w, c-w to be present. If b-w or c-w is missing, this particular pair doesn't work. But we could try {b,u,v} and {a,c,w}, etc.

This is getting very complicated. Let me try a different approach to the proof.

Let me try to prove the upper bound directly, without the feedback vertex set approach.

Direct proof attempt:

The
