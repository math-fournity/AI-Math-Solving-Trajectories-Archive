# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Among a group of 120 people, some pairs are friends. A weak quartet is a set of four people containing exactly one pair of friends. What is the maximum possible number of weak quartets?       — 题目文本
#   For a graph \( G \) on 120 vertices (representing people), let \( q(G) \) denote the number of weak quartets in \( G \). We aim to find the maximum \( q(G) \).

First, we show that a graph \( G \) with maximal \( q(G) \) can be decomposed into disjoint complete graphs. This is true if any two adjacent vertices \( x \) and \( y \) have the same neighbors, excluding themselves. Consider the graph \( G_x \) obtained by "copying" \( x \) to \( y \) (i.e., for each \( z \neq x, y \), add the edge \( zy \) if \( zx \) is an edge, and delete \( zy \) if \( zx \) is not an edge). Similarly, define \( G_y \) by copying \( y \) to \( x \). We claim that \( 2q(G) \leq q(G_x) + q(G_y) \).

The number of weak quartets containing neither \( x \) nor \( y \) is the same in \( G \), \( G_x \), and \( G_y \). The number containing both \( x \) and \( y \) is not less in \( G_x \) and \( G_y \) than in \( G \). The number containing exactly one of \( x \) and \( y \) in \( G_x \) is at least twice the number in \( G \) containing \( x \) but not \( y \), and similarly for \( G_y \). Thus, for an extremal graph \( G \), we must have \( q(G) = q(G_x) = q(G_y) \). Repeating this process, we obtain an extremal graph consisting of disjoint complete graphs.

Next, suppose the complete graphs in \( G \) have sizes \( a_1, a_2, \ldots, a_n \). Then

\[
q(G) = \sum_{i=1}^{n} \binom{a_i}{2} \sum_{\substack{j<k \\ j, k \neq i}} a_j a_k.
\]

If we fix all \( a_i \) except two, say \( p, q \), with \( p+q = s \) fixed, then for some constants \( C_i \), we have \( q(G) = C_1 + C_2 pq + C_3 \left( \binom{p}{2} + \binom{q}{2} \right) + C_4 \left( q\binom{p}{2} + p\binom{q}{2} \right) = A + Bpq \), where \( A \) and \( B \) depend only on \( s \). Thus, the maximum of \( q(G) \) is attained if \( |p-q| \leq 1 \) or \( pq = 0 \). Therefore, if \( q(G) \) is maximal, any two nonzero \( a_i \)'s differ by at most 1.

Finally, if \( G \) consists of \( n \) disjoint complete graphs, then \( q(G) \) cannot exceed the value obtained if \( a_1 = \cdots = a_n \) (not necessarily integral), which equals

\[
Q_n = \frac{120^2}{n} \binom{120/n}{2} \binom{n-1}{2} = 30 \cdot 120^2 \frac{(n-1)(n-2)(120-n)}{n^3}.
\]

It is easy to check that \( Q_n \) takes its maximum when \( n = 5 \) and \( a_1 = \cdots = a_5 = 24 \), and this maximum equals \( 15 \cdot 23 \cdot 24^3 = 4769280 \).

\(\boxed{4769280}\)  — 标准解答
#   Let me solve this problem. We have 120 people, some pairs are friends. A weak quartet is a set of 4 people containing exactly one pair of friends. We want to maximize the number of weak quartets.

Let me think about this. Let the friendship graph be G on n=120 vertices. A weak quartet is a 4-set with exactly one edge.

Let me count weak quartets by summing over edges. For each edge (u,v), the number of 4-sets containing exactly this one edge (and no other edges among the 4) is: we pick 2 more vertices from the remaining 118, such that neither is adjacent to u or v (within the 4-set), and the two chosen vertices are not adjacent to each other, and neither chosen vertex is adjacent to u or v.

Wait, let me be more careful. A 4-set {a,b,c,d} with exactly one edge, say {a,b}. Then:
- c and d are not adjacent to each other
- c is not adjacent to a, b
- d is not adjacent to a, b
- a,b are adjacent (the one edge)

So for edge (a,b), the number of weak quartets where {a,b} is the unique friend pair = number of ways to choose {c,d} from the remaining 118 vertices such that:
- c,d not adjacent to each other
- c not adjacent to a, c not adjacent to b
- d not adjacent to a, d not adjacent to b

Let me define for edge (a,b): let S = set of vertices (other than a,b) that are not adjacent to a and not adjacent to b. Then we need to choose 2 vertices from S that are not adjacent to each other. The number of such pairs = C(|S|, 2) - (number of edges within S).

So total weak quartets W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

where S_{ab} = vertices not adjacent to a and not adjacent to b (excluding a,b themselves), and e(S_{ab}) is the number of edges within S_{ab}.

This is complex. Let me think about what graph structure maximizes this.

Intuition: To maximize weak quartets, we want many edges, but each edge should have many non-neighbors. There's tension.

Let me think about a complete bipartite graph or a specific structure.

Actually, let me think about a graph that is a complete graph on some subset, or a disjoint union of cliques, or a complete bipartite graph.

Let me consider the graph being a complete bipartite graph K_{a,b} with a+b=120. In K_{a,b}, edges are between the two parts. A 4-set with exactly one edge: pick 1 from part A and 3 from part B? No wait. In K_{a,b}, every vertex in A is adjacent to every vertex in B. So a 4-set with vertices from both parts will have many edges.

If we pick 2 from A and 2 from B: that gives 4 edges (complete bipartite K_{2,2}). Not weak.
If we pick 1 from A and 3 from B: 3 edges. Not weak.
If we pick 4 from A: 0 edges. Not weak.
If we pick 4 from B: 0 edges. Not weak.

So K_{a,b} gives 0 weak quartets. Bad.

Let me think about a graph that is a matching (disjoint edges). If we have m edges forming a matching on 120 vertices (so 2m vertices used, 120-2m isolated). A weak quartet needs exactly one edge. 

For a 4-set to have exactly one edge: it contains exactly one of the matching edges and two other vertices that form no edge. The two other vertices must not form a matching edge, and must not be endpoints of... well, the 4-set contains one matching edge {a,b} and two other vertices c,d. For exactly one edge, c and d must not be adjacent (not a matching edge), and c,d must not be adjacent to a or b. But in a matching, c,d are adjacent to a or b only if they're the partners of a or b, but a,b are partners of each other, so c,d are not adjacent to a,b (unless c or d is a partner, but a's partner is b). So c,d just need to not be a matching edge themselves.

Number of weak quartets = sum over matching edges {a,b} of [C(118, 2) - (number of other matching edges)]

For matching edge {a,b}, the other vertices are 118. Among these 118, the number of matching edges not involving a,b = m-1. So pairs {c,d} that form an edge = m-1. So weak quartets from this edge = C(118,2) - (m-1).

Total = m * [C(118,2) - (m-1)] = m * [6973 - m + 1] = m * (6974 - m).

Maximize: m(6974 - m) is maximized at m = 3487, but m ≤ 60 (matching on 120 vertices). So at m=60: 60 * 6914 = 414840.

Hmm, but can we do better with a different structure?

Let me think about a graph that is a union of a clique and isolated vertices, or something else.

Actually, let me think more carefully. Let me consider a graph where we have a clique of size k and the rest (120-k) are isolated. 

A weak quartet needs exactly one edge. If we pick 4 vertices, the number of edges among them depends on how many are in the clique.

- 4 from clique: C(4,2)=6 edges. Not weak.
- 3 from clique, 1 isolated: C(3,2)=3 edges. Not weak.
- 2 from clique, 2 isolated: 1 edge. Weak! 
- 1 from clique, 3 isolated: 0 edges. Not weak.
- 0 from clique, 4 isolated: 0 edges. Not weak.

So weak quartets = C(k,2) * C(120-k, 2).

Maximize C(k,2)*C(120-k,2) over k. Let f(k) = k(k-1)/2 * (120-k)(119-k)/2.

Let me compute for k around 60. f(k) = k(k-1)(120-k)(119-k)/4.

By symmetry-ish (not exact symmetry due to -1 terms), the max is near k=60.

f(60) = 60*59*60*59/4 = (60*59)^2/4 = (3540)^2/4 = 12531600/4 = 3132900.

Wait let me recompute: 60*59 = 3540. 3540^2 = 12531600. /4 = 3132900.

That's way more than 414840. So the clique + isolated vertices is much better.

Let me check other values. f(k) = k(k-1)(120-k)(119-k)/4.

Let me set g(k) = k(k-1)(120-k)(119-k). Take derivative... or just check around k=60.

g(60) = 60*59*60*59 = 3540*3540 = 12531600.
g(59) = 59*58*61*60 = 59*58*3660 = 3422*3660 = 12524520.
g(61) = 61*60*59*58 = 3660*3422 = 12524520.

So g(60) = 12531600, g(59) = g(61) = 12524520. So k=60 is the max (or very close).

Actually let me be more careful. Let h(k) = k(k-1)(120-k)(119-k). Let's substitute k = 60 + t. Then:
- k = 60+t, k-1 = 59+t, 120-k = 60-t, 119-k = 59-t.
h = (60+t)(59+t)(60-t)(59-t) = [(60+t)(60-t)][(59+t)(59-t)] = (3600-t²)(3481-t²).

Let u = t². h = (3600-u)(3481-u) = 3600*3481 - u(3600+3481) + u² = 12531600 - 7081u + u².

This is minimized at u = 7081/2 = 3540.5, so h is maximized at u=0 (t=0) since the parabola opens upward and the vertex is a minimum... wait no. h = u² - 7081u + 12531600. This is a parabola opening upward, so it has a minimum at u=3540.5. The maximum on the valid range is at the endpoints. But u = t² ≥ 0, and t must be an integer with 60+t between 0 and 120.

At u=0 (t=0): h = 12531600.
At u=1 (t=±1): h = 1 - 7081 + 12531600 = 12524520.

So h decreases as we move away from t=0. The maximum is at t=0, i.e., k=60.

So with a clique of 60 and 60 isolated vertices, we get 12531600/4 = 3132900 weak quartets.

But wait — can we do better with a different graph structure? The clique + isolated is a specific construction. Let me think about whether some other structure does better.

Let me think about the general problem more carefully. 

Total weak quartets W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

where S_{ab} = common non-neighbors of a and b (excluding a,b).

This is hard to optimize directly. Let me think about upper bounds.

Alternative counting: A weak quartet is a 4-set with exactly 1 edge. Let's think about it differently.

Let me count by choosing the edge and the two non-adjacent vertices. For edge e = {a,b}, let d(a) and d(b) be degrees. The number of vertices adjacent to a or b (excluding a,b) is |N(a) ∪ N(b)| - (count a,b if they're in neighborhoods, but they're not since no self-loops, but b ∈ N(a) and a ∈ N(b)). Let me be careful.

N(a) = neighbors of a, not including a. b ∈ N(a) since {a,b} is an edge.
N(b) = neighbors of b, not including b. a ∈ N(b).

Vertices (other than a,b) adjacent to a: |N(a)| - 1 = d(a) - 1 (removing b).
Vertices (other than a,b) adjacent to b: |N(b)| - 1 = d(b) - 1 (removing a).
Vertices (other than a,b) adjacent to a or b: |N(a) ∪ N(b)| - 2 (removing a and b from the union, since a ∈ N(b) and b ∈ N(a)).

|N(a) ∪ N(b)| = d(a) + d(b) - |N(a) ∩ N(b)|.

So vertices adjacent to a or b (excl. a,b) = d(a) + d(b) - |N(a) ∩ N(b)| - 2.

S_{ab} = vertices not adjacent to a and not adjacent to b (excl. a,b) = 118 - [d(a) + d(b) - |N(a) ∩ N(b)| - 2] = 120 - d(a) - d(b) + |N(a) ∩ N(b)|.

So |S_{ab}| = 120 - d(a) - d(b) + |N(a) ∩ N(b)|.

For the clique + isolated construction: clique of size 60. For an edge (a,b) in the clique: d(a) = d(b) = 59, |N(a) ∩ N(b)| = 58 (the other 58 clique members). |S_{ab}| = 120 - 59 - 59 + 58 = 60. And e(S_{ab}) = 0 (S_{ab} is the 60 isolated vertices). So weak quartets per edge = C(60,2) = 1770. Total = C(60,2) * 1770 = 1770 * 1770 = 3132900. ✓.

Now, can we beat this? Let me think about an upper bound.

W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

≤ sum over edges (a,b) of C(|S_{ab}|, 2)

= sum over edges (a,b) of C(120 - d(a) - d(b) + |N(a) ∩ N(b)|, 2)

This is still complex. Let me think about whether the clique + isolated is optimal.

Let me consider a more general structure: a complete multipartite graph or a graph with a clique and some other structure.

Actually, let me think about it differently. Consider a graph with a clique C of size k and the rest being independent set I of size 120-k, with NO edges between C and I. Then:

Weak quartets = C(k,2) * C(120-k, 2) (as computed: 2 from clique, 2 from independent set).

What if we add some edges between C and I, or within I? 

If we add an edge between a vertex in C and a vertex in I: this could create new weak quartets but also destroy some. Let's see. Adding edge (c, i) where c ∈ C, i ∈ I:
- This destroys weak quartets that contained {c, i'} for i' ∈ I (since now c-i' might... no, c-i' is not an edge unless i'=i). Actually, adding edge (c,i) affects quartets containing both c and i. 

Hmm, this is getting complicated. Let me think about it more carefully with a cleaner approach.

Let me consider the complement graph approach. In the complement graph $\bar{G}$, a weak quartet (exactly 1 edge in G) corresponds to a 4-set with exactly 5 edges in $\bar{G}$ (i.e., exactly 1 non-edge in $\bar{G}$, which is exactly 1 edge in G). So a weak quartet in G = a 4-set in $\bar{G}$ with exactly C(4,2)-1 = 5 edges.

Alternatively, let me think about it as: we want to maximize the number of 4-sets with exactly 1 edge.

Let me think about the problem as follows. Let's use the edge-centric count:

W = sum over edges e={a,b} of f(e)

where f(e) = number of 4-sets where {a,b} is the unique edge = number of pairs {c,d} ⊆ S_{ab} with c,d non-adjacent = C(|S_{ab}|, 2) - e(S_{ab}).

Now, I want to find the graph maximizing W. 

Let me think about what happens with two cliques. Say clique of size k and clique of size 120-k, with no edges between them. Then:

A 4-set with exactly 1 edge: 
- 2 from clique 1, 2 from clique 2: 1 + 1 = 2 edges. Not weak.
- 3 from clique 1, 1 from clique 2: 3 edges. Not weak.
- 2 from clique 1, 1 from clique 2, 1 from... wait, there are only two cliques. 
- 4 from clique 1: 6 edges. Not weak.
- 3 from clique 1, 1 from clique 2: C(3,2) = 3 edges. Not weak.
- 2 from clique 1, 2 from clique 2: 1 + 1 = 2 edges. Not weak.

So two cliques give 0 weak quartets. Bad.

What about a clique and an independent set with some edges between them? Let me think about a "split graph" — clique of size k, independent set of size 120-k, and some edges between them.

Let's say we have clique C (size k), independent set I (size m = 120-k), and a bipartite graph B between C and I. 

A 4-set can have vertices from C and I in various combinations. Let me categorize:

Case 1: 2 from C, 2 from I. Edges among them: 1 (from C) + (edges from B between these 2 C-vertices and 2 I-vertices) + 0 (I is independent). For weak quartet, we need exactly 1 edge, so 0 edges from B. So we need both I-vertices to be non-neighbors of both C-vertices in B.

Case 2: 1 from C, 3 from I. Edges: 0 (from C alone) + (edges from B between the 1 C-vertex and 3 I-vertices) + 0. For weak, exactly 1 edge from B, so exactly 1 of the 3 I-vertices is adjacent to the C-vertex.

Case 3: 3 from C, 1 from I. Edges: 3 (from C) + (edges from B). ≥ 3. Not weak.

Case 4: 4 from C: 6 edges. Not weak.
Case 5: 4 from I: 0 edges. Not weak.
Case 6: 0 from C: same as case 5.

So weak quartets come from cases 1 and 2.

W = [Case 1] + [Case 2]

Case 1: Choose 2 from C (C(k,2) ways), 2 from I (C(m,2) ways), such that neither I-vertex is adjacent to either C-vertex. 

Case 2: Choose 1 from C (k ways), 3 from I (C(m,3) ways), such that exactly 1 of the 3 I-vertices is adjacent to the C-vertex.

This is getting complex. Let me think about whether adding edges between C and I can increase W beyond the pure clique+independent case.

In the pure case (no B edges): 
- Case 1: C(k,2) * C(m,2) (all pairs work since no B edges).
- Case 2: 0 (no B edges means 0 edges from B, not 1).

W = C(k,2)*C(m,2), maximized at k=60 giving 3132900.

Now if we add B edges:
- Case 1 decreases (some pairs now have B edges).
- Case 2 increases (now possible to have exactly 1 B edge).

The question is whether the gain from Case 2 can exceed the loss from Case 1.

Let me consider a specific example. Take k=60, m=60. Add a perfect matching between C and I (each c_i connected to exactly one i_j, and each i_j to exactly one c_i). So each C-vertex has 1 B-neighbor, each I-vertex has 1 B-neighbor.

Case 1: Choose 2 from C, 2 from I. The number of "bad" choices (where some B edge exists among the 4) = choices where at least one of the 2 C-vertices is B-matched to one of the 2 I-vertices.

Total Case 1 pairs: C(60,2)*C(60,2) = 1770*1770 = 3132900.
Bad pairs: Let's count. For a fixed pair {c_a, c_b} from C, their B-neighbors are i_a, i_b (distinct since matching). Bad I-pairs: those containing i_a or i_b. Number of I-pairs containing i_a or i_b = C(60,2) - C(58,2) = 1770 - 1653 = 117. (Pairs containing i_a: 59. Containing i_b: 59. Containing both: 1. Total: 59+59-1 = 117.)

So bad Case 1 = C(60,2) * 117 = 1770 * 117 = 207090.
Good Case 1 = 3132900 - 207090 = 2925810.

Case 2: Choose 1 from C (say c_a with B-neighbor i_a), 3 from I. Exactly 1 of the 3 I-vertices is i_a. So we need i_a in the triple and the other 2 from I\{i_a}, and neither of the other 2 is B-matched to c_a (but c_a's only B-match is i_a, so the other 2 just need to not be i_a, which they aren't). So: choose i_a and 2 from the other 59 I-vertices: C(59,2) = 1711. Per C-vertex: 1711. Total Case 2 = 60 * 1711 = 102660.

Total W = 2925810 + 102660 = 3028470.

This is less than 3132900. So adding a matching made it worse.

Let me try a different approach: what if we make B very sparse but strategic? Actually, the loss in Case 1 seems to dominate. Let me check if there's a regime where Case 2 gain dominates.

Actually, let me think about this more carefully. Let me consider the general split graph and try to optimize.

Let me denote the B-graph between C and I. For a C-vertex c, let b(c) = number of B-neighbors (degree in B). For an I-vertex i, let b(i) = number of B-neighbors.

Case 1 contribution: sum over pairs {c_a, c_b} ⊆ C, pairs {i_x, i_y} ⊆ I, such that none of (c_a,i_x), (c_a,i_y), (c_b,i_x), (c_b,i_y) are B-edges.

Case 2 contribution: sum over c ∈ C, triples {i_x, i_y, i_z} ⊆ I, such that exactly one of (c, i_x), (c, i_y), (c, i_z) is a B-edge.

For Case 2, fixing c with b(c) = d: number of triples with exactly 1 B-neighbor of c = d * C(m-d, 2). (Choose 1 from the d B-neighbors, 2 from the m-d non-B-neighbors.)

Case 2 = sum over c ∈ C of b(c) * C(m - b(c), 2).

For Case 1, it's more complex. Let me think about it for a specific structure.

Hmm, this is getting complicated. Let me step back and think about whether the clique + independent set is actually optimal, or if there's a fundamentally different structure that does better.

Let me think about upper bounds. 

Alternative approach: Let's think about the problem in terms of the complement. In $\bar{G}$, a weak quartet corresponds to a 4-set inducing exactly 5 edges (i.e., a 4-set whose complement has exactly 1 edge, meaning the 4-set in $\bar{G}$ is missing exactly 1 edge, i.e., it's a K4 minus one edge).

So we want to maximize the number of 4-sets that induce exactly K4 - e in $\bar{G}$, which is the same as maximizing 4-sets that induce exactly 1 edge in G.

Hmm, let me think about this differently. Let me consider the "clique + independent set" more carefully and see if we can prove it's optimal, or find something better.

Actually, let me consider a different structure: a disjoint union of a clique and some other stuff, or a "threshold graph."

Let me try a different construction: Take a clique of size k and an independent set of size 120-k, but now also consider making the independent set into a sparse graph.

Wait, actually, let me reconsider. What if instead of a clique + independent set, we use a different split?

Let me try: clique C of size k, independent set I of size m = 120-k, and complete bipartite between C and I. This is a "split graph" where C is a clique, I is independent, and all C-I edges exist. This is actually a "threshold graph."

In this case:
- 2 from C, 2 from I: 1 (C edge) + 4 (B edges) = 5 edges. Not weak.
- 1 from C, 3 from I: 0 + 3 (B edges) = 3. Not weak.
- 3 from C, 1 from I: 3 + 3 = 6. Not weak.
- 4 from C: 6. Not weak.
- 4 from I: 0. Not weak.

So 0 weak quartets. Bad.

What about clique C of size k, independent I of size m, and NO edges between them (our original construction)? W = C(k,2)*C(m,2), max at k=60: 3132900.

What if we use a different structure entirely? Let me think about a "blow-up" or other constructions.

Let me try: partition into 3 groups. Group A (size a), Group B (size b), Group C (size c), a+b+c=120. Make A a clique, B and C independent sets, no edges between any groups. Then:

Weak quartets: 2 from A (1 edge), 2 from B∪C (0 edges since B,C independent and no inter-group edges). So W = C(a,2) * C(120-a, 2). Same as before with k=a. No improvement.

What if A is a clique, B is a clique, C is independent, no inter-group edges?
- 2 from A, 2 from B: 1+1 = 2 edges. Not weak.
- 2 from A, 2 from C: 1+0 = 1. Weak!
- 2 from B, 2 from C: 1+0 = 1. Weak!
- 2 from A, 1 from B, 1 from C: 1+1+0 = 2. Not weak.
- 1 from A, 2 from B, 1 from C: 0+1+0 = 1. Weak!
- 1 from A, 1 from B, 2 from C: 0+0+0 = 0. Not weak.
- 3 from A, 1 from C: 3. Not weak.
- etc.

W = C(a,2)*C(c,2) + C(b,2)*C(c,2) + a*C(b,2)*c + ... 

Wait let me be more careful. Let me enumerate all 4-sets with exactly 1 edge.

Groups: A (clique, size a), B (clique, size b), C (independent, size c), a+b+c=120, no inter-group edges.

4-set compositions (x from A, y from B, z from C, x+y+z=4):
- (2,0,2): edges = C(2,2)=1 from A. Weak. Count: C(a,2)*C(c,2).
- (0,2,2): edges = 1 from B. Weak. Count: C(b,2)*C(c,2).
- (2,2,0): edges = 1+1 = 2. Not weak.
- (1,2,1): edges = 0+1+0 = 1. Weak. Count: a*C(b,2)*c.
- (2,1,1): edges = 1+0+0 = 1. Weak. Count: C(a,2)*b*c.
- (1,1,2): edges = 0+0+0 = 0. Not weak.
- (3,0,1): edges = 3. Not weak.
- (0,3,1): edges = 3. Not weak.
- (1,3,0): edges = 3. Not weak.
- (3,1,0): edges = 3+0 = 3. Not weak.
- (0,0,4): 0. Not weak.
- (4,0,0): 6. Not weak.
- (0,4,0): 6. Not weak.
- (1,0,3): 0. Not weak.
- (0,1,3): 0. Not weak.

W = C(a,2)*C(c,2) + C(b,2)*C(c,2) + a*C(b,2)*c + C(a,2)*b*c

= C(c,2)[C(a,2) + C(b,2)] + c[C(a,2)*b + a*C(b,2)]

= C(c,2)[C(a,2) + C(b,2)] + c[C(a,2)*b + a*C(b,2)]

Let me factor. Note C(a,2)*b + a*C(b,2) = ab[(a-1)/2 + (b-1)/2] = ab(a+b-2)/2 = ab(a+b-2)/2.

And C(a,2) + C(b,2) = [a(a-1) + b(b-1)]/2 = [a²+b²-a-b]/2.

Let s = a+b, so c = 120-s. Then:
C(a,2)+C(b,2) = [a²+b²-s]/2 = [(a+b)²-2ab-s]/2 = [s²-2ab-s]/2.
C(a,2)*b + a*C(b,2) = ab(s-2)/2.

W = C(c,2) * [s²-2ab-s]/2 + c * ab(s-2)/2

= (1/2){C(c,2)[s²-s-2ab] + c·ab(s-2)}

Note s²-s = s(s-1). And C(c,2) = c(c-1)/2.

W = (1/2){c(c-1)/2 * [s(s-1)-2ab] + c·ab(s-2)}

= (c/2){(c-1)/2 * [s(s-1)-2ab] + ab(s-2)}

= (c/4){(c-1)[s(s-1)-2ab] + 2ab(s-2)}

= (c/4){(c-1)s(s-1) - 2ab(c-1) + 2ab(s-2)}

= (c/4){(c-1)s(s-1) + 2ab[s-2-c+1]}

= (c/4){(c-1)s(s-1) + 2ab[s-c-1]}

Since c = 120-s: s-c-1 = s-(120-s)-1 = 2s-121.

W = (c/4){(c-1)s(s-1) + 2ab(2s-121)}

Now, for fixed s (and thus c), we want to optimize over a,b with a+b=s. The term involving ab is 2ab(2s-121). 

If 2s-121 > 0, i.e., s > 60.5, i.e., s ≥ 61: we want to maximize ab, so a=b=s/2.
If 2s-121 < 0, i.e., s ≤ 60: we want to minimize ab, so a=1,b=s-1 (or vice versa), giving ab = s-1.
If 2s-121 = 0, i.e., s = 60.5: not integer.

Case s ≤ 60: minimize ab → a=1, b=s-1. Then ab = s-1. But wait, if a=1, then C(a,2)=0, so A is just a single vertex (no clique edges). This effectively reduces to the 2-clique case (just B and C). Let me check: with a=1, b=s-1, c=120-s:

W = (c/4){(c-1)s(s-1) + 2(s-1)(2s-121)}

= (c(s-1)/4){(c-1)s + 2(2s-121)}

= (c(s-1)/4){s(c-1) + 4s - 242}

= (c(s-1)/4){s(c-1+4) - 242}

= (c(s-1)/4){s(c+3) - 242}

With c = 120-s: s(123-s) - 242 = 123s - s² - 242.

W = (c(s-1)/4)(123s - s² - 242) = ((120-s)(s-1)/4)(123s - s² - 242)

Let me maximize this for s ≤ 60. Let me check s=60: c=60.
W = (60*59/4)(123*60 - 3600 - 242) = (885)(7380 - 3600 - 242) = 885 * 3538 = 3131130.

Hmm, that's slightly less than 3132900. Let me double-check. With a=1, b=59, c=60:

W = C(1,2)*C(60,2) + C(59,2)*C(60,2) + 1*C(59,2)*60 + C(1,2)*59*60
= 0 + 1711*1770 + 1711*60 + 0
= 1711*1770 + 1711*60
= 1711*1830
= 3131130.

And the pure clique+independent with k=60: C(60,2)*C(60,2) = 1770*1770 = 3132900.

So 3132900 > 3131130. The 2-group clique+independent is better.

Case s ≥ 61: maximize ab → a=b=s/2 (if s even) or a=(s-1)/2, b=(s+1)/2 (if s odd). Let me try s=62, a=b=31, c=58.

W = (c/4){(c-1)s(s-1) + 2ab(2s-121)}
= (58/4){57*62*61 + 2*961*3}
= 14.5{57*62*61 + 5766}
= 14.5{215094 + 5766}
= 14.5 * 220860
= 3202470.

Wait, that's more than 3132900! Let me double-check.

s=62, a=31, b=31, c=58.

C(a,2) = C(31,2) = 465. C(b,2) = 465. C(c,2) = C(58,2) = 1653.

W = C(a,2)*C(c,2) + C(b,2)*C(c,2) + a*C(b,2)*c + C(a,2)*b*c
= 465*1653 + 465*1653 + 31*465*58 + 465*31*58
= 2*465*1653 + 2*31*465*58
= 2*465*(1653 + 31*58)
= 930*(1653 + 1798)
= 930 * 3451
= 3209430.

Hmm, let me recompute. 31*58 = 1798. 1653 + 1798 = 3451. 930 * 3451 = 3209430.

Wait, that's even higher. Let me recheck my formula.

W = C(a,2)*C(c,2) + C(b,2)*C(c,2) + a*C(b,2)*c + C(a,2)*b*c

With a=b=31, c=58:
C(a,2) = 465, C(b,2) = 465, C(c,2) = 1653.
a*C(b,2)*c = 31*465*58 = 31*465*58. 465*58 = 26970. 31*26970 = 836070.
C(a,2)*b*c = 465*31*58 = same = 836070.
C(a,2)*C(c,2) = 465*1653 = 768645.
C(b,2)*C(c,2) = 465*1653 = 768645.

W = 768645 + 768645 + 836070 + 836070 = 3209430.

So W = 3209430 > 3132900. The 3-group construction is better!

Let me explore more. Let me try to optimize over s and a,b.

For s ≥ 61, with a=b=s/2 (s even), ab = s²/4:

W = (c/4){(c-1)s(s-1) + 2*(s²/4)*(2s-121)}
= (c/4){(c-1)s(s-1) + (s²/2)(2s-121)}
= (c/4){(c-1)s(s-1) + s²(2s-121)/2}

With c = 120-s. Let me compute for several values of s.

s=62, c=58: W = 3209430 (computed above).
s=64, c=56, a=b=32: 
C(32,2)=496, C(56,2)=1540.
W = 2*496*1540 + 2*32*496*56 = 992*1540 + 64*496*56 = 1527680 + 64*27776 = 1527680 + 1777664 = 3305344.

s=66, c=54, a=b=33:
C(33,2)=528, C(54,2)=1431.
W = 2*528*1431 + 2*33*528*54 = 1056*1431 + 66*528*54 = 1511136 + 66*28512 = 1511136 + 1881792 = 3392928.

s=68, c=52, a=b=34:
C(34,2)=561, C(52,2)=1326.
W = 2*561*1326 + 2*34*561*52 = 1122*1326 + 68*561*52 = 1487772 + 68*29172 = 1487772 + 1983696 = 3471468.

s=70, c=50, a=b=35:
C(35,2)=595, C(50,2)=1225.
W = 2*595*1225 + 2*35*595*50 = 1190*1225 + 70*595*50 = 1457750 + 70*29750 = 1457750 + 2082500 = 3540250.

s=72, c=48, a=b=36:
C(36,2)=630, C(48,2)=1128.
W = 2*630*1128 + 2*36*630*48 = 1260*1128 + 72*630*48 = 1421280 + 72*30240 = 1421280 + 2177280 = 3598560.

s=74, c=46, a=b=37:
C(37,2)=666, C(46,2)=1035.
W = 2*666*1035 + 2*37*666*46 = 1332*1035 + 74*666*46 = 1378620 + 74*30636 = 1378620 + 2267064 = 3645684.

s=76, c=44, a=b=38:
C(38,2)=703, C(44,2)=946.
W = 2*703*946 + 2*38*703*44 = 1406*946 + 76*703*44 = 1330076 + 76*30932 = 1330076 + 2350832 = 3680908.

s=78, c=42, a=b=39:
C(39,2)=741, C(42,2)=861.
W = 2*741*861 + 2*39*741*42 = 1482*861 + 78*741*42 = 1276302 + 78*31122 = 1276302 + 2427516 = 3703818.

s=80, c=40, a=b=40:
C(40,2)=780, C(40,2)=780.
W = 2*780*780 + 2*40*780*40 = 2*608400 + 80*780*40 = 1216800 + 2496000 = 3712800.

s=82, c=38, a=b=41:
C(41,2)=820, C(38,2)=703.
W = 2*820*703 + 2*41*820*38 = 1640*703 + 82*820*38 = 1152920 + 82*31160 = 1152920 + 2555120 = 3708040.

s=84, c=36, a=b=42:
C(42,2)=861, C(36,2)=630.
W = 2*861*630 + 2*42*861*36 = 1722*630 + 84*861*36 = 1084860 + 84*30996 = 1084860 + 2603664 = 3688524.

So the maximum seems to be around s=80, giving W = 3712800.

Let me check s=80 more carefully and nearby odd values.

s=79, c=41, a=39, b=40 (to maximize ab with a+b=79, ab = 39*40 = 1560):
C(39,2)=741, C(40,2)=780, C(41,2)=820.
W = 741*820 + 780*820 + 39*780*41 + 741*40*41
= 820*(741+780) + 41*(39*780 + 741*40)
= 820*1521 + 41*(30420 + 29640)
= 1247220 + 41*60060
= 1247220 + 2462460
= 3709680.

s=81, c=39, a=40, b=41 (ab = 40*41 = 1640):
C(40,2)=780, C(41,2)=820, C(39,2)=741.
W = 780*741 + 820*741 + 40*820*39 + 780*41*39
= 741*(780+820) + 39*(40*820 + 780*41)
= 741*1600 + 39*(32800 + 31980)
= 1185600 + 39*64780
= 1185600 + 2526420
= 3712020.

So s=81 gives 3712020, slightly less than s=80's 3712800.

s=80, a=b=40, c=40: W = 3712800.

Let me also check s=80 with unequal a,b. a+b=80, c=40. 
W = (c/4){(c-1)s(s-1) + 2ab(2s-121)}
= (40/4){39*80*79 + 2ab*39}
= 10{39*6320 + 78ab}
= 10{246480 + 78ab}
= 2464800 + 780ab.

Maximize ab with a+b=80: ab ≤ 40*40 = 1600. So W ≤ 2464800 + 780*1600 = 2464800 + 1248000 = 3712800. ✓

So for s=80, the max is at a=b=40, giving 3712800.

Now let me check if s=80 is truly optimal. For even s with a=b=s/2:

W = (c/4){(c-1)s(s-1) + (s²/2)(2s-121)} where c=120-s.

Let me define F(s) = (120-s)/4 * {(119-s)*s*(s-1) + (s²/2)(2s-121)}.

Let me compute more values:
s=78: 3703818
s=80: 3712800
s=82: 3708040

So the peak is at s=80. Let me verify by checking the formula at s=80:
c=40, (c-1)=39, s(s-1)=80*79=6320, s²/2=3200, 2s-121=39.
F(80) = 40/4 * {39*6320 + 3200*39} = 10 * {246480 + 124800} = 10 * 371280 = 3712800. ✓

Now, the question is: can we do even better with more groups? Let me try 4 groups: two cliques A, B and two independent sets... actually, let me think about this more generally.

Let me try 4 groups: A (clique, a), B (clique, b), C (independent, c), D (independent, d), no inter-group edges, a+b+c+d=120.

A weak quartet needs exactly 1 edge. The edge must come from within A or within B. 

If the edge is from A (2 vertices from A), the other 2 must come from B∪C∪D with 0 edges among them. But if any of the other 2 is from B, we need only 1 from B (which gives 0 edges from B since we need 2 for an edge) — wait, if we pick 1 from B, that's 0 edges from B. If we pick 2 from B, that's 1 edge from B, making 2 total. So the other 2 can be: 2 from C∪D (0 edges), or 1 from B and 1 from C∪D (0 edges), or 2 from B (1 edge, total 2, not weak).

Hmm wait, let me reconsider. With 4 groups, the analysis gets more complex. Let me think about whether more groups can help.

Actually, let me reconsider. The 3-group case with two cliques and one independent set gave 3712800. Can 4 groups do better?

Let me try: A (clique, a), B (clique, b), C (independent, c), D (independent, d), a+b+c+d=120, no inter-group edges.

Weak quartets (exactly 1 edge):
The 1 edge comes from A or B.

Edge from A (pick 2 from A): other 2 from B∪C∪D with 0 edges.
- 2 from C: 0 edges. Count: C(a,2)*C(c,2).
- 2 from D: 0 edges. Count: C(a,2)*C(d,2).
- 1 from C, 1 from D: 0 edges. Count: C(a,2)*c*d.
- 1 from B, 1 from C: 0 edges. Count: C(a,2)*b*c.
- 1 from B, 1 from D: 0 edges. Count: C(a,2)*b*d.
- 2 from B: 1 edge. Total 2. Not weak.
- 2 from C∪D but mixing: covered above.

Edge from B (pick 2 from B): other 2 from A∪C∪D with 0 edges.
- 2 from C: C(b,2)*C(c,2).
- 2 from D: C(b,2)*C(d,2).
- 1 from C, 1 from D: C(b,2)*c*d.
- 1 from A, 1 from C: C(b,2)*a*c.
- 1 from A, 1 from D: C(b,2)*a*d.
- 2 from A: 1 edge. Not weak.

So W = [C(a,2) + C(b,2)] * [C(c,2) + C(d,2) + cd] + [C(a,2)*b + C(b,2)*a] * [c + d]

Note C(c,2) + C(d,2) + cd = C(c+d, 2) = C(c+d,2). And c+d = 120-a-b.

Also C(a,2)*b + C(b,2)*a = ab[(a-1)+(b-1)]/2 = ab(a+b-2)/2.

And C(a,2) + C(b,2) = [a(a-1)+b(b-1)]/2 = [a²+b²-a-b]/2 = [(a+b)²-2ab-(a+b)]/2.

Let s = a+b, t = c+d = 120-s.

W = [(s²-2ab-s)/2] * C(t,2) + [ab(s-2)/2] * t

= (1/2){[s²-s-2ab]*C(t,2) + ab(s-2)*t}

= (1/2){[s(s-1)-2ab]*t(t-1)/2 + ab(s-2)*t}

= (t/2){[s(s-1)-2ab]*(t-1)/2 + ab(s-2)}

= (t/4){[s(s-1)-2ab](t-1) + 2ab(s-2)}

= (t/4){s(s-1)(t-1) - 2ab(t-1) + 2ab(s-2)}

= (t/4){s(s-1)(t-1) + 2ab[s-2-t+1]}

= (t/4){s(s-1)(t-1) + 2ab[s-t-1]}

With t = 120-s: s-t-1 = s-(120-s)-1 = 2s-121.

W = (t/4){s(s-1)(t-1) + 2ab(2s-121)}

This is exactly the same formula as the 3-group case! (Where c in the 3-group formula = t here.) So the 4-group case with 2 cliques and 2 independent sets gives the same W as the 3-group case with 2 cliques and 1 independent set (of the same total size). The split of the independent set doesn't matter because C(c,2)+C(d,2)+cd = C(c+d,2).

So we can't do better by splitting the independent set. Good.

Now, what about 3 cliques and 1 independent set? Or more generally, k cliques and 1 independent set?

Let me generalize: k cliques of sizes a_1, ..., a_k and 1 independent set of size c, with sum a_i + c = 120, no inter-group edges.

A weak quartet has exactly 1 edge, which comes from one of the cliques. Say the edge is from clique i (pick 2 from clique i). The other 2 vertices must have 0 edges among them. The other 2 can come from:
- The independent set: 2 from C, 0 edges. Count: C(a_i,2)*C(c,2).
- One from another clique j and one from C: 0 edges. Count: C(a_i,2)*a_j*c.
- One from another clique j and one from another clique l (j≠l): 0 edges. Count: C(a_i,2)*a_j*a_l.
- Two from the same other clique j: 1 edge. Not weak.

So for edge from clique i, the number of valid pairs for the other 2 = C(c,2) + c*(s-a_i) + C(s-a_i, 2) - sum_j C(a_j,2) [where the sum is over j≠i, and s = sum of all a_j].

Wait, let me think again. The other 2 vertices come from (all other cliques ∪ independent set), which has size (120 - a_i). Among these, the number of pairs with 0 edges = total pairs - pairs that form an edge = C(120-a_i, 2) - sum_{j≠i} C(a_j, 2).

Because the only edges among the remaining vertices are within each clique j (j≠i). The independent set has no internal edges, and there are no inter-group edges.

So W = sum_i C(a_i, 2) * [C(120-a_i, 2) - sum_{j≠i} C(a_j, 2)]

Let me denote T = sum_j C(a_j, 2) (total edges in all cliques). Then sum_{j≠i} C(a_j, 2) = T - C(a_i, 2).

W = sum_i C(a_i, 2) * [C(120-a_i, 2) - T + C(a_i, 2)]

= sum_i C(a_i, 2) * C(120-a_i, 2) - T * sum_i C(a_i, 2) + sum_i C(a_i, 2)²

= sum_i C(a_i, 2) * C(120-a_i, 2) - T² + sum_i C(a_i, 2)²

= sum_i C(a_i, 2) * C(120-a_i, 2) - T² + sum_i C(a_i, 2)²

Note T² - sum_i C(a_i,2)² = sum_{i≠j} C(a_i,2)*C(a_j,2) = 2*sum_{i<j} C(a_i,2)*C(a_j,2).

So W = sum_i C(a_i,2)*C(120-a_i,2) - 2*sum_{i<j} C(a_i,2)*C(a_j,2).

Hmm, let me verify with the 2-clique case. k=2, a_1=a, a_2=b, c=120-a-b.

W = C(a,2)*C(120-a,2) + C(b,2)*C(120-b,2) - 2*C(a,2)*C(b,2).

Let me check with a=b=40, c=40:
C(40,2)=780, C(80,2)=3160.
W = 780*3160 + 780*3160 - 2*780*780 = 2*780*3160 - 2*780² = 2*780*(3160-780) = 1560*2380 = 3712800. ✓

Now let me try k=3 cliques. Let a_1=a_2=a_3=40, c=0. But then 120 = 120, c=0. No independent set.

W = 3*C(40,2)*C(80,2) - 2*3*C(40,2)² = 3*780*3160 - 6*780² = 3*2464800 - 6*608400 = 7394400 - 3650400 = 3744000.

Wait, that's more than 3712800! Let me double-check.

3 cliques of size 40, no independent set, no inter-group edges. Total vertices = 120.

A weak quartet: exactly 1 edge. The edge comes from one clique. Say from clique 1: pick 2 from clique 1 (C(40,2)=780 ways), then 2 from the rest (cliques 2 and 3, total 80 vertices) with 0 edges. Pairs from cliques 2∪3 with 0 edges = C(80,2) - C(40,2) - C(40,2) = 3160 - 780 - 780 = 1600. 

So from clique 1: 780 * 1600 = 1248000.
By symmetry, same for cliques 2 and 3.
W = 3 * 1248000 = 3744000.

Yes! 3744000 > 3712800. So 3 cliques of 40 is better!

Let me check the formula: W = 3*780*3160 - 6*780² = 7394400 - 3650400 = 3744000. ✓

Can we do even better? Let me try 4 cliques of size 30, c=0.

C(30,2) = 435, C(90,2) = 4005.
W = 4*435*4005 - 2*6*435² = 4*435*4005 - 12*189225 = 6970860 - 2270700 = 4700160.

Wait, that's way more! Let me double-check.

4 cliques of 30, no inter-group edges, total 120.

Weak quartet: edge from clique i (C(30,2)=435 ways). Other 2 from remaining 90 vertices (cliques j≠i) with 0 edges. Pairs with 0 edges = C(90,2) - 3*C(30,2) = 4005 - 1305 = 2700.

From each clique: 435 * 2700 = 1174500.
W = 4 * 1174500 = 4698000.

Hmm, let me recheck with the formula. 
W = sum_i C(a_i,2)*C(120-a_i,2) - 2*sum_{i<j} C(a_i,2)*C(a_j,2)
= 4*435*4005 - 2*C(4,2)*435² 
= 4*435*4005 - 12*435²
= 4*435*4005 - 12*189225
= 6970860 - 2270700 
= 4700160.

But direct calculation gives 4698000. Let me recheck.

Direct: from clique i, other 2 from 90 vertices with 0 edges = C(90,2) - 3*C(30,2) = 4005 - 3*435 = 4005 - 1305 = 2700. 435*2700 = 1174500. Total = 4*1174500 = 4698000.

Formula: sum_i C(a_i,2)*C(120-a_i,2) = 4*435*C(90,2) = 4*435*4005 = 6970860.
2*sum_{i<j} C(a_i,2)*C(a_j,2) = 2*6*435*435 = 12*189225 = 2270700.
W = 6970860 - 2270700 = 4700160.

There's a discrepancy. Let me recheck the formula derivation.

W = sum_i C(a_i, 2) * [C(120-a_i, 2) - sum_{j≠i} C(a_j, 2)]

= sum_i C(a_i,2)*C(120-a_i,2) - sum_i C(a_i,2)*sum_{j≠i} C(a_j,2)

= sum_i C(a_i,2)*C(120-a_i,2) - sum_i C(a_i,2)*(T - C(a_i,2))

= sum_i C(a_i,2)*C(120-a_i,2) - T*sum_i C(a_i,2) + sum_i C(a_i,2)²

= sum_i C(a_i,2)*C(120-a_i,2) - T² + sum_i C(a_i,2)²

where T = sum_i C(a_i,2).

For 4 cliques of 30: T = 4*435 = 1740.
sum_i C(a_i,2)*C(120-a_i,2) = 4*435*4005 = 6970860.
T² = 1740² = 3027600.
sum_i C(a_i,2)² = 4*435² = 4*189225 = 756900.

W = 6970860 - 3027600 + 756900 = 4700160.

But direct calculation gives 4698000. Let me recheck the direct calculation.

From clique 1: pick 2 from clique 1 (435 ways). Other 2 from vertices in cliques 2,3,4 (90 vertices). Pairs with 0 edges among these 90: total pairs = C(90,2) = 4005. Edges among these 90 = C(30,2)+C(30,2)+C(30,2) = 1305 (edges within clique 2, within clique 3, within clique 4; no inter-clique edges). So 0-edge pairs = 4005 - 1305 = 2700.

435 * 2700 = 1174500. Total = 4 * 1174500 = 4698000.

So there's a discrepancy: formula gives 4700160, direct gives 4698000. Let me find the error.

Ah wait, I think the issue is that C(120-a_i, 2) counts pairs from the remaining 120-a_i vertices, but some of those pairs include vertices from clique i itself! No, 120-a_i excludes clique i. The remaining vertices are from cliques j≠i and the independent set. In this case c=0, so remaining = cliques j≠i, which is 90 vertices. C(90,2) = 4005. ✓

And sum_{j≠i} C(a_j, 2) = 3*435 = 1305. ✓

So W = 4 * 435 * (4005 - 1305) = 4 * 435 * 2700 = 4698000.

Now let me recheck the formula:
sum_i C(a_i,2) * [C(120-a_i,2) - (T - C(a_i,2))]
= sum_i C(a_i,2) * C(120-a_i,2) - sum_i C(a_i,2)*(T - C(a_i,2))
= sum_i C(a_i,2)*C(120-a_i,2) - T*sum_i C(a_i,2) + sum_i C(a_i,2)^2

sum_i C(a_i,2) = T. So:
= sum_i C(a_i,2)*C(120-a_i,2) - T*T + sum_i C(a_i,2)^2
= sum_i C(a_i,2)*C(120-a_i,2) - T^2 + sum_i C(a_i,2)^2

For our case:
= 6970860 - 3027600 + 756900 = 4700160.

But direct = 4698000. Difference = 2160.

Hmm, let me recompute. 6970860 - 3027600 = 3943260. 3943260 + 756900 = 4700160.

Direct: 4 * 435 * 2700. 435*2700 = 1174500. 4*1174500 = 4698000.

4700160 - 4698000 = 2160. 

Let me check: T^2 - sum C(a_i,2)^2 = 3027600 - 756900 = 2270700. And 2*sum_{i<j} C(a_i,2)*C(a_j,2) = 2*6*435^2 = 12*189225 = 2270700. ✓

So W = 6970860 - 2270700 = 4700160 by the "factored" formula, but direct gives 4698000.

Wait, I think I need to recheck. Let me compute directly again, very carefully.

W = sum_{i=1}^{4} C(a_i, 2) * [C(120 - a_i, 2) - sum_{j ≠ i} C(a_j, 2)]

For i=1: C(30,2) * [C(90,2) - (C(30,2) + C(30,2) + C(30,2))] = 435 * [4005 - 1305] = 435 * 2700 = 1174500.

W = 4 * 1174500 = 4698000.

Now the formula:
sum_i C(a_i,2)*C(120-a_i,2) = 4 * 435 * 4005 = 6970860.
T = 4 * 435 = 1740.
sum_i C(a_i,2)*(T - C(a_i,2)) = 4 * 435 * (1740 - 435) = 4 * 435 * 1305 = 2270700.

W = 6970860 - 2270700 = 4700160.

But direct: 4 * 435 * (4005 - 1305) = 4 * 435 * 2700 = 4698000.

And 4 * 435 * 4005 - 4 * 435 * 1305 = 4 * 435 * (4005 - 1305) = 4 * 435 * 2700 = 4698000.

But 4 * 435 * 1305 = 2270700? Let me check: 435 * 1305 = 567675. 4 * 567675 = 2270700. ✓

And 4 * 435 * 4005 = 6970860? 435 * 4005 = 1742175. 4 * 1742175 = 6968700.

Wait! 435 * 4005: 435 * 4000 = 1740000. 435 * 5 = 2175. Total = 1742175. 4 * 1742175 = 6968700.

So sum_i C(a_i,2)*C(120-a_i,2) = 6968700, not 6970860!

I made an arithmetic error. Let me redo:
W = 6968700 - 2270700 = 4698000. ✓

Great, so the formula is correct, I just made an arithmetic error. W = 4698000 for 4 cliques of 30.

Now, 4698000 > 3744000 (3 cliques of 40) > 3712800 (2 cliques of 40 + independent 40) > 3132900 (1 clique of 60 + independent 60).

So more cliques seem better! Let me try 5 cliques of 24, c=0.

C(24,2) = 276, C(96,2) = 4560.
T = 5*276 = 1380.
W = 5*276*4560 - 1380² + 5*276² 
= 5*276*4560 - 1904400 + 5*76176
= 6292800 - 1904400 + 380880
= 4773280.

Direct check: from clique i, 0-edge pairs from other 96 = C(96,2) - 4*C(24,2) = 4560 - 1104 = 3456. 276*3456 = 953856. Total = 5*953856 = 4769280.

Hmm, discrepancy again. Let me recompute.

5*276*4560 = 5*1258560 = 6292800. 
T = 1380, T² = 1904400.
sum C(a_i,2)² = 5*276² = 5*76176 = 380880.
W = 6292800 - 1904400 + 380880 = 4769280. ✓ (I made an error before: 6292800 - 1904400 = 4388400, + 380880 = 4769280.)

Direct: 276 * 3456 = 953856. 5 * 953856 = 4769280. ✓

So 5 cliques of 24: W = 4769280 > 4698000.

Let me try 6 cliques of 20, c=0.
C(20,2) = 190, C(100,2) = 4950.
T = 6*190 = 1140.
W = 6*190*4950 - 1140² + 6*190²
= 6*190*4950 - 1299600 + 6*36100
= 5643000 - 1299600 + 216600
= 4560000.

Direct: 0-edge pairs from other 100 = 4950 - 5*190 = 4950 - 950 = 4000. 190*4000 = 760000. 6*760000 = 4560000. ✓

So 6 cliques of 20: W = 4560000 < 4769280. So 5 cliques was better than 6.

Let me try non-equal cliques. Maybe the optimal isn't equal-sized cliques.

Let me go back and think about this more generally. We have k cliques of sizes a_1, ..., a_k (and possibly an independent set of size c = 120 - sum a_i), no inter-group edges.

W = sum_i C(a_i, 2) * [C(120 - a_i, 2) - (T - C(a_i, 2))]

where T = sum_i C(a_i, 2).

= sum_i C(a_i,2) * [C(120-a_i,2) - T + C(a_i,2)]

Let me think about this as a function of the clique sizes. Let me denote e_i = C(a_i, 2) = a_i(a_i-1)/2 (the number of edges in clique i). And let n_i = a_i (size of clique i).

W = sum_i e_i * [C(120-n_i, 2) - T + e_i]

= sum_i e_i * C(120-n_i, 2) - T² + sum_i e_i²

This is a complex optimization. Let me think about it differently.

Actually, let me consider the general problem. We have a graph G that is a disjoint union of cliques (a "cluster graph"). The weak quartets are 4-sets with exactly 1 edge.

For a cluster graph with cliques of sizes a_1, ..., a_k (sum = 120):

W = sum_i C(a_i, 2) * [C(120 - a_i, 2) - sum_{j≠i} C(a_j, 2)]

Let me think about what happens when we have many small cliques. If all cliques have size 2 (just edges, a matching), then k=60, a_i=2, C(2,2)=1, T=60.

W = sum_i 1 * [C(118, 2) - 59] = 60 * [6973 - 59] = 60 * 6914 = 414840.

That's much less than the clique+independent case. So very small cliques are bad.

If all cliques have size 3, k=40, C(3,2)=3, T=120.
W = 40 * 3 * [C(117,2) - 117] = 120 * [6786 - 117] = 120 * 6669 = 800280.

Still less. Size 4: k=30, C(4,2)=6, T=180.
W = 30 * 6 * [C(116,2) - 174] = 180 * [6670 - 174] = 180 * 6496 = 1169280.

Size 5: k=24, C(5,2)=10, T=240.
W = 24 * 10 * [C(115,2) - 230] = 240 * [6555 - 230] = 240 * 6325 = 1518000.

Size 6: k=20, C(6,2)=15, T=300.
W = 20 * 15 * [C(114,2) - 285] = 300 * [6441 - 285] = 300 * 6156 = 1846800.

Size 8: k=15, C(8,2)=28, T=420.
W = 15 * 28 * [C(112,2) - 392] = 420 * [6216 - 392] = 420 * 5824 = 2446080.

Size 10: k=12, C(10,2)=45, T=540.
W = 12 * 45 * [C(110,2) - 495] = 540 * [5995 - 495] = 540 * 5500 = 2970000.

Size 12: k=10, C(12,2)=66, T=660.
W = 10 * 66 * [C(108,2) - 594] = 660 * [5778 - 594] = 660 * 5184 = 3421440.

Size 15: k=8, C(15,2)=105, T=840.
W = 8 * 105 * [C(105,2) - 735] = 840 * [5460 - 735] = 840 * 4725 = 3969000.

Size 20: k=6, W = 4560000 (computed above).
Size 24: k=5, W = 4769280.
Size 30: k=4, W = 4698000.
Size 40: k=3, W = 3744000.
Size 60: k=2, W = 3132900... wait no, k=2 with a=60,b=60: 

Actually wait, k=2 with a_1=a_2=60: C(60,2)=1770, T=3540.
W = 2 * 1770 * [C(60,2) - 1770] = 3540 * [1770 - 1770] = 0.

That's 0! Because with 2 cliques of 60, a 4-set with 2 from each clique has 2 edges, and any other distribution has 0 or 6 edges. So no weak quartets.

OK so the pattern is: W increases as clique size decreases from 60 to about 24, then decreases again. The maximum among equal-sized cliques is around size 24 (k=5), giving 4769280.

But maybe unequal cliques do better. Let me think about this.

Let me consider the general optimization. We want to maximize:

W = sum_i e_i * [C(120-n_i, 2) - T + e_i]

where e_i = n_i(n_i-1)/2, T = sum e_i.

Let me think about this as follows. For a cluster graph, let me think about what 4-sets give exactly 1 edge. We need 2 vertices from one clique (giving 1 edge) and 2 vertices from outside that clique, with the 2 outside vertices not being in the same clique (so they don't form an edge).

So W = sum_i C(n_i, 2) * [number of ways to pick 2 vertices from outside clique i, not in the same clique]

= sum_i C(n_i, 2) * [C(120-n_i, 2) - sum_{j≠i} C(n_j, 2)]

The "2 vertices from outside, not in same clique" = total pairs from outside - pairs that are in the same clique = C(120-n_i, 2) - sum_{j≠i} C(n_j, 2).

Now, let me think about the continuous relaxation. Let n_i be continuous variables summing to 120. We want to maximize W.

This is a complex combinatorial optimization. Let me try some non-equal configurations.

Let me try k=5 with sizes (30, 30, 20, 20, 20), sum=120.
e: 435, 435, 190, 190, 190. T = 1440.
For i with n_i=30: C(90,2) - (435+190+190+190) = 4005 - 1005 = 3000. Contribution: 435*3000 = 1305000. Two such: 2610000.
For i with n_i=20: C(100,2) - (435+435+190+190) = 4950 - 1250 = 3700. Contribution: 190*3700 = 703000. Three such: 2109000.
W = 2610000 + 2109000 = 4719000.

Less than 4769280 (equal 24s). 

Let me try (25, 25, 25, 25, 20), sum=120.
e: 300, 300, 300, 300, 190. T = 1390.
For n_i=25: C(95,2) - (300+300+300+190) = 4465 - 1090 = 3375. Contribution: 300*3375 = 1012500. Four: 4050000.
For n_i=20: C(100,2) - 4*300 = 4950 - 1200 = 3750. Contribution: 190*3750 = 712500.
W = 4050000 + 712500 = 4762500.

Close to 4769280 but slightly less.

Let me try (24, 24, 24, 24, 24): W = 4769280.

Let me try (25, 25, 25, 25, 20) vs (24, 24, 24, 24, 24). The equal one is better.

Let me try k=4 with (30, 30, 30, 30): W = 4698000.
k=4 with (28, 28, 32, 32): 
e: 378, 378, 496, 496. T = 1748.
For n_i=28: C(92,2) - (378+496+496) = 4186 - 1370 = 2816. Contribution: 378*2816 = 1064208. Two: 2128416.
For n_i=32: C(88,2) - (378+378+496) = 3828 - 1252 = 2576. Contribution: 496*2576 = 1277696. Two: 2555392.
W = 2128416 + 2555392 = 4683808. Less than 4698000.

So equal seems best for fixed k. Let me try to find the optimal k with equal cliques.

For k equal cliques of size n = 120/k (assuming k | 120):
e = n(n-1)/2, T = k*e.
W = k * e * [C(120-n, 2) - (k-1)*e]
= k * e * [C(120-n, 2) - (k-1)*e]

Let me compute for various k (divisors of 120: 1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120):

k=1: n=120, e=7140, T=7140. W = 1*7140*[C(0,2)-0] = 0. (No weak quartets since everything is one clique.)
k=2: n=60, e=1770. W = 2*1770*[C(60,2)-1770] = 3540*0 = 0.
k=3: n=40, e=780. W = 3*780*[C(80,2)-2*780] = 2340*[3160-1560] = 2340*1600 = 3744000.
k=4: n=30, e=435. W = 4*435*[C(90,2)-3*435] = 1740*[4005-1305] = 1740*2700 = 4698000.
k=5: n=24, e=276. W = 5*276*[C(96,2)-4*276] = 1380*[4560-1104] = 1380*3456 = 4769280.
k=6: n=20, e=190. W = 6*190*[C(100,2)-5*190] = 1140*[4950-950] = 1140*4000 = 4560000.
k=8: n=15, e=105. W = 8*105*[C(105,2)-7*105] = 840*[5460-735] = 840*4725 = 3969000.
k=10: n=12, e=66. W = 10*66*[C(108,2)-9*66] = 660*[5778-594] = 660*5184 = 3421440.
k=12: n=10, e=45. W = 12*45*[C(110,2)-11*45] = 540*[5995-495] = 540*5500 = 2970000.
k=15: n=8, e=28. W = 15*28*[C(112,2)-14*28] = 420*[6216-392] = 420*5824 = 2446080.
k=20: n=6, e=15. W = 20*15*[C(114,2)-19*15] = 300*[6441-285] = 300*6156 = 1846800.
k=24: n=5, e=10. W = 24*10*[C(115,2)-23*10] = 240*[6555-230] = 240*6325 = 1518000.
k=30: n=4, e=6. W = 30*6*[C(116,2)-29*6] = 180*[6670-174] = 180*6496 = 1169280.
k=40: n=3, e=3. W = 40*3*[C(117,2)-39*3] = 120*[6786-117] = 120*6669 = 800280.
k=60: n=2, e=1. W = 60*1*[C(118,2)-59*1] = 60*[6973-59] = 60*6914 = 414840.
k=120: n=1, e=0. W = 0.

So the maximum among equal cliques is at k=5, W = 4769280.

But we should also check non-divisor k values and non-equal cliques. Let me try k=5 with slightly unequal sizes.

Let me try k=5 with sizes (25, 25, 24, 23, 23), sum=120.
e: 300, 300, 276, 253, 253. T = 1382.
For n=25: C(95,2) - (300+276+253+253) = 4465 - 1082 = 3383. Contribution: 300*3383 = 1014900. Two: 2029800.
For n=24: C(96,2) - (300+300+253+253) = 4560 - 1106 = 3454. Contribution: 276*3454 = 953304.
For n=23: C(97,2) - (300+300+276+253) = 4656 - 1129 = 3527. Contribution: 253*3527 = 892331. Two: 1784662.
W = 2029800 + 953304 + 1784662 = 4767766.

Slightly less than 4769280.

Let me try (25, 24, 24, 24, 23), sum=120.
e: 300, 276, 276, 276, 253. T = 1381.
For n=25: C(95,2) - (276+276+276+253) = 4465 - 1081 = 3384. Contribution: 300*3384 = 1015200.
For n=24: C(96,2) - (300+276+276+253) = 4560 - 1105 = 3455. Contribution: 276*3455 = 953580. Three: 2860740.
For n=23: C(97,2) - (300+276+276+276) = 4656 - 1128 = 3528. Contribution: 253*3528 = 892584.
W = 1015200 + 2860740 + 892584 = 4768524.

Still less than 4769280.

So equal cliques of size 24 (k=5) seems optimal among cluster graphs. But is the cluster graph the optimal structure?

Let me think about whether a non-cluster graph could do better. 

Actually, let me think about this more carefully. The cluster graph (disjoint union of cliques) might not be optimal. Let me consider other structures.

Let me think about the problem from a different angle. Let me consider the general graph and try to establish an upper bound.

Let me use the edge-centric count again:
W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

where S_{ab} = common non-neighbors of a and b (excluding a,b), |S_{ab}| = 120 - d(a) - d(b) + |N(a) ∩ N(b)|.

For a cluster graph with cliques of sizes n_1, ..., n_k:
- For an edge (a,b) within clique i: d(a) = d(b) = n_i - 1, |N(a) ∩ N(b)| = n_i - 2 (other vertices in clique i).
- |S_{ab}| = 120 - 2(n_i-1) + (n_i-2) = 120 - n_i.
- e(S_{ab}) = sum_{j≠i} C(n_j, 2) (edges in other cliques; S_{ab} consists of all vertices outside clique i).
- C(|S_{ab}|, 2) - e(S_{ab}) = C(120-n_i, 2) - sum_{j≠i} C(n_j, 2). ✓

So W = sum_i C(n_i, 2) * [C(120-n_i, 2) - sum_{j≠i} C(n_j, 2)]. ✓

Now, could a non-cluster graph do better? Let me think about what structure maximizes W.

Intuitively, we want:
1. Many edges (each edge contributes to W).
2. For each edge (a,b), many common non-neighbors (large S_{ab}).
3. Few edges within S_{ab}.

These are in tension: more edges means smaller S_{ab} and more edges within S_{ab}.

The cluster graph is a natural candidate because:
- Edges are concentrated within cliques (many edges).
- For an edge within a clique, S_{ab} = all vertices outside the clique, which is large if the clique is small.
- But edges within S_{ab} = edges in other cliques, which is also significant.

Let me think about whether we can do better by having some non-cluster structure.

Consider modifying the cluster graph: take the optimal cluster graph (5 cliques of 24) and try to add or remove edges to improve W.

If we remove an edge from a clique: we lose the contribution of that edge to W, but we might increase S_{ab} for other edges. Let's see.

Remove edge (a,b) from clique 1 (size 24). Now a and b are no longer adjacent. 

Effect on W:
1. We lose the weak quartets that had (a,b) as the unique edge. Previously: C(96,2) - 4*C(24,2) = 4560 - 1104 = 3456. So we lose 3456 weak quartets.

2. For other edges (c,d) in clique 1: S_{cd} previously included a and b (they were outside clique 1... no, a and b are in clique 1, so they're not in S_{cd} which is outside clique 1). Wait, S_{cd} for edge (c,d) in clique 1 = all vertices outside clique 1 = 96 vertices. Removing edge (a,b) doesn't change S_{cd} for edges in clique 1 (since a,b are in clique 1, not in S_{cd}).

But wait, a and b are in clique 1. For edge (c,d) in clique 1, S_{cd} = vertices not adjacent to c and not adjacent to d, excluding c,d. In the cluster graph, c is adjacent to all of clique 1 (including a,b), so a,b ∉ S_{cd}. After removing edge (a,b), a is still adjacent to c (edge (a,c) still exists in clique 1), so a ∉ S_{cd} still. So S_{cd} is unchanged.

3. For edges (c,d) in other cliques: S_{cd} = vertices outside clique of c,d. a and b are in clique 1, which is outside the clique of c,d. Previously, a and b were in S_{cd} (they're not adjacent to c or d since they're in a different clique). After removing edge (a,b), a and b are still not adjacent to c or d, so they're still in S_{cd}. But now a and b are not adjacent to each other, so the pair {a,b} no longer contributes an edge within S_{cd}. So e(S_{cd}) decreases by 1 (the edge (a,b) is removed from S_{cd}).

So for each edge in other cliques, the contribution increases by 1 (since e(S_{cd}) decreases by 1, so C(|S_{cd}|,2) - e(S_{cd}) increases by 1).

Number of edges in other cliques = 4 * C(24,2) = 4 * 276 = 1104.

So gain from step 3: 1104.
Loss from step 1: 3456.
Net: 1104 - 3456 = -2352. Worse.

What if we add an edge between two cliques? Say add edge (a, x) where a ∈ clique 1, x ∈ clique 2.

Effect:
1. New edge (a,x) contributes: S_{ax} = vertices not adjacent to a and not adjacent to x, excluding a,x. 
   - a is adjacent to: all of clique 1 except a (23 vertices), and now x.
   - x is adjacent to: all of clique 2 except x (23 vertices), and now a.
   - Common non-neighbors of a and x (excl. a,x): vertices not in clique 1, not in clique 2, and not a or x. = 120 - 24 - 24 = 72 vertices (cliques 3,4,5).
   - |S_{ax}| = 72.
   - e(S_{ax}) = 3*C(24,2) = 828.
   - Contribution: C(72,2) - 828 = 2556 - 828 = 1728.

2. For edges (a,b) in clique 1 (b ≠ x, b ∈ clique 1): S_{ab} previously = 96 vertices (outside clique 1). Now x is adjacent to a, so x ∉ S_{ab}. So |S_{ab}| decreases by 1 (from 96 to 95). Also, e(S_{ab}) changes: previously S_{ab} included x and all edges involving x in clique 2 (23 edges). Now x is removed from S_{ab}, so those 23 edges are gone from S_{ab}. But also, the new edge (a,x) doesn't affect e(S_{ab}) since a ∉ S_{ab}.

Wait, let me reconsider. S_{ab} for edge (a,b) in clique 1: vertices not adjacent to a and not adjacent to b, excluding a,b. 

Before adding edge (a,x): a is adjacent to clique 1 \ {a} (23 vertices). b is adjacent to clique 1 \ {b} (23 vertices). So S_{ab} = all vertices except clique 1 = 96 vertices. e(S_{ab}) = sum of edges in cliques 2-5 = 4*276 = 1104.

After adding edge (a,x): a is now also adjacent to x. So S_{ab} = all vertices except clique 1, except x = 95 vertices. e(S_{ab}) = edges in cliques 2-5 minus edges involving x in clique 2 = 1104 - 23 = 1081. (x had 23 edges in clique 2, all removed from S_{ab}.)

New contribution of edge (a,b): C(95,2) - 1081 = 4465 - 1081 = 3384.
Old contribution: C(96,2) - 1104 = 4560 - 1104 = 3456.
Change: 3384 - 3456 = -72.

There are 23 such edges (a,b) with b ∈ clique 1, b ≠ a. Total change: 23 * (-72) = -1656.

3. For edges (x,y) in clique 2 (y ≠ a, y ∈ clique 2): similarly, S_{xy} loses a (since a is now adjacent to x). |S_{xy}| goes from 96 to 95, e(S_{xy}) goes from 1104 to 1104 - 23 = 1081.
Change per edge: C(95,2) - 1081 - (C(96,2) - 1104) = 3384 - 3456 = -72.
23 such edges. Total: 23 * (-72) = -1656.

4. For edges in cliques 3, 4, 5: S doesn't change (a and x are still in S, and they're still not adjacent to vertices in cliques 3,4,5). But now a and x ARE adjacent (new edge), so e(S) increases by 1 for each such edge's S.

Wait, for edge (c,d) in clique 3: S_{cd} = vertices outside clique 3 = 96 vertices (cliques 1,2,4,5). After adding edge (a,x), a and x are now adjacent, and both are in S_{cd} (they're in cliques 1 and 2, outside clique 3). So e(S_{cd}) increases by 1.

Change per edge: -1. Number of edges in cliques 3,4,5: 3*276 = 828. Total: 828 * (-1) = -828.

5. For edges (a,b) in clique 1 where we also need to check: does the new edge (a,x) create any new edges within S_{ab}? a ∉ S_{ab}, so no.

Total change: +1728 (new edge) - 1656 (clique 1 edges) - 1656 (clique 2 edges) - 828 (cliques 3,4,5 edges) = 1728 - 4140 = -2412. Worse.

So adding edges between cliques makes things worse. This suggests the cluster graph is locally optimal.

Let me also check: what about non-cluster graphs that aren't close to cluster graphs?

Actually, let me think about this problem more carefully. Let me consider the possibility that the optimal graph is not a cluster graph.

Let me think about an upper bound. 

W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

≤ sum over edges (a,b) of C(|S_{ab}|, 2)

= sum over edges (a,b) of C(120 - d(a) - d(b) + |N(a) ∩ N(b)|, 2)

This is hard to bound directly. Let me think about a different approach.

Actually, let me think about the problem from the perspective of 4-sets. There are C(120, 4) total 4-sets. Each 4-set has between 0 and 6 edges. We want to maximize the number with exactly 1 edge.

Let X_i = number of 4-sets with exactly i edges. We want to maximize X_1.

We have:
sum X_i = C(120, 4)
sum i*X_i = sum over 4-sets of (number of edges) = C(118, 2) * |E| (each edge is in C(118, 2) 4-sets)
sum C(i, 2) * X_i = sum over 4-sets of C(edges, 2) = sum over pairs of edges of (number of 4-sets containing both)

This gives us moment constraints but the optimization is still complex.

Let me try a different approach. Let me think about whether we can prove the cluster graph with 5 cliques of 24 is optimal, or find something better.

Actually, let me try a different type of construction. What about a "complete multipartite" type structure or a graph with a specific degree sequence?

Hmm, let me try to think about this more carefully using the formula.

For a cluster graph with k equal cliques of size n = 120/k:

W = k * C(n, 2) * [C(120-n, 2) - (k-1)*C(n, 2)]

Let me write this in terms of n (with k = 120/n):

W = (120/n) * n(n-1)/2 * [(120-n)(119-n)/2 - (120/n - 1)*n(n-1)/2]

= 60(n-1) * [(120-n)(119-n)/2 - (120-n)(n-1)/2]

= 60(n-1) * (120-n)/2 * [(119-n) - (n-1)]

= 60(n-1) * (120-n)/2 * (120-2n)

= 60(n-1)(120-n)(120-2n)/2

= 30(n-1)(120-n)(120-2n)

Wait, this requires k = 120/n to be an integer. Let me verify:

For n=24, k=5: W = 30*23*96*72 = 30*23*6912 = 30*158976 = 4769280. ✓
For n=30, k=4: W = 30*29*90*60 = 30*29*5400 = 30*156600 = 4698000. ✓
For n=20, k=6: W = 30*19*100*80 = 30*19*8000 = 30*152000 = 4560000. ✓

So W(n) = 30(n-1)(120-n)(120-2n) for equal cliques.

Let me find the maximum of f(n) = (n-1)(120-n)(120-2n) for real n.

f(n) = (n-1)(120-n)(120-2n)

Let me expand: Let u = n-1, so n = u+1.
f = u(119-u)(118-2u)

Let me take derivative with respect to u:
f(u) = u(119-u)(118-2u) = u[119*118 - 238u - 118u + 2u²] = u[14042 - 356u + 2u²]
= 14042u - 356u² + 2u³

f'(u) = 14042 - 712u + 6u²

Setting f'(u) = 0: 6u² - 712u + 14042 = 0
u = (712 ± sqrt(712² - 4*6*14042)) / (2*6) = (712 ± sqrt(506944 - 337008)) / 12 = (712 ± sqrt(169936)) / 12

sqrt(169936) ≈ 412.2

u = (712 ± 412.2) / 12

u₁ = (712 + 412.2)/12 = 1124.2/12 ≈ 93.7 → n ≈ 94.7 (but then 120-2n < 0, not valid)
u₂ = (712 - 412.2)/12 = 299.8/12 ≈ 24.98 → n ≈ 25.98

So the optimal n ≈ 26. Since we need k = 120/n to be an integer, let's check n=24 (k=5) and n=30 (k=4), and also non-integer k.

Actually, we don't need k to be an integer if we allow unequal cliques! Let me think about this.

If we have k cliques of approximately equal size n ≈ 26, with k ≈ 120/26 ≈ 4.6, we could try 4 cliques of 26 and 1 clique of 16 (sum = 120).

Let me compute: cliques of sizes 26, 26, 26, 26, 16.
e: 325, 325, 325, 325, 120. T = 1420.

For n=26: C(94,2) - (325+325+325+120) = 4371 - 1095 = 3276. Contribution: 325*3276 = 1064700. Four: 4258800.
For n=16: C(104,2) - 4*325 = 5356 - 1300 = 4056. Contribution: 120*4056 = 486720.
W = 4258800 + 486720 = 4745520.

Less than 4769280. Hmm.

Let me try 5 cliques of sizes 26, 26, 26, 26, 16 but that's what I just did. Let me try 5 cliques of 24 (the best so far) vs other 5-clique configurations.

Actually, the continuous optimum is at n ≈ 26, but with 5 cliques, 5*26 = 130 > 120, so we can't have 5 cliques of 26. With 4 cliques of 26 and 1 of 16, we get 4745520 < 4769280.

Let me try 4 cliques of 25 and 1 of 20: sum = 120.
e: 300, 300, 300, 300, 190. T = 1390.
For n=25: C(95,2) - (300+300+300+190) = 4465 - 1090 = 3375. Contribution: 300*3375 = 1012500. Four: 4050000.
For n=20: C(100,2) - 4*300 = 4950 - 1200 = 3750. Contribution: 190*3750 = 712500.
W = 4050000 + 712500 = 4762500. (Computed before, less than 4769280.)

Let me try 5 cliques of sizes 25, 25, 24, 23, 23: computed before, 4767766.

Let me try 5 cliques of 24, 24, 24, 24, 24: 4769280.

Let me try 5 cliques of 25, 25, 25, 23, 22: sum = 120.
e: 300, 300, 300, 253, 231. T = 1384.
For n=25: C(95,2) - (300+300+253+231) = 4465 - 1084 = 3381. Contribution: 300*3381 = 1014300. Three: 3042900.
For n=23: C(97,2) - (300+300+300+231) = 4656 - 1131 = 3525. Contribution: 253*3525 = 891825.
For n=22: C(98,2) - (300+300+300+253) = 4753 - 1153 = 3600. Contribution: 231*3600 = 831600.
W = 3042900 + 891825 + 831600 = 4766325.

Less than 4769280.

It really seems like 5 equal cliques of 24 is the best cluster graph. Let me also check 4 cliques and 6 cliques with unequal sizes to be thorough.

4 cliques: optimal equal is 30 each, W=4698000. Let me try 4 cliques of 28, 28, 32, 32: computed before, 4683808. Worse.

Let me try 4 cliques of 26, 26, 34, 34: 
e: 325, 325, 561, 561. T = 1772.
For n=26: C(94,2) - (325+561+561) = 4371 - 1447 = 2924. Contribution: 325*2924 = 950300. Two: 1900600.
For n=34: C(86,2) - (325+325+561) = 3655 - 1211 = 2444. Contribution: 561*2444 = 1371084. Two: 2742168.
W = 1900600 + 2742168 = 4642768. Worse.

6 cliques: optimal equal is 20 each, W=4560000. Let me try 6 cliques of 22, 22, 22, 18, 18, 18:
e: 231, 231, 231, 153, 153, 153. T = 1152.
For n=22: C(98,2) - (231+231+153+153+153) = 4753 - 921 = 3832. Contribution: 231*3832 = 885192. Three: 2655576.
For n=18: C(102,2) - (231+231+231+153+153) = 5151 - 999 = 4152. Contribution: 153*4152 = 635256. Three: 1905768.
W = 2655576 + 1905768 = 4561344. Slightly better than 4560000 but still way less than 4769280.

So the best cluster graph is 5 cliques of 24, W = 4769280.

Now, the key question: is the cluster graph optimal, or can some other graph structure do better?

Let me think about this more carefully. Let me consider a graph that's not a disjoint union of cliques.

Consider a "blow-up" of a path or cycle. Or consider a graph where we have a clique and the rest is not independent but has some structure.

Actually, let me think about the problem differently. Let me consider the complement graph $\bar{G}$. A weak quartet in G (exactly 1 edge in G) corresponds to a 4-set with exactly 5 edges in $\bar{G}$, i.e., a 4-set that induces        — AI历史解题过程（thinking）
#   polymath_00141         — 题目ID

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
  <problem_id>polymath_00141</problem_id>
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

Among a group of 120 people, some pairs are friends. A weak quartet is a set of four people containing exactly one pair of friends. What is the maximum possible number of weak quartets?

## Standard Solution

For a graph \( G \) on 120 vertices (representing people), let \( q(G) \) denote the number of weak quartets in \( G \). We aim to find the maximum \( q(G) \).

First, we show that a graph \( G \) with maximal \( q(G) \) can be decomposed into disjoint complete graphs. This is true if any two adjacent vertices \( x \) and \( y \) have the same neighbors, excluding themselves. Consider the graph \( G_x \) obtained by "copying" \( x \) to \( y \) (i.e., for each \( z \neq x, y \), add the edge \( zy \) if \( zx \) is an edge, and delete \( zy \) if \( zx \) is not an edge). Similarly, define \( G_y \) by copying \( y \) to \( x \). We claim that \( 2q(G) \leq q(G_x) + q(G_y) \).

The number of weak quartets containing neither \( x \) nor \( y \) is the same in \( G \), \( G_x \), and \( G_y \). The number containing both \( x \) and \( y \) is not less in \( G_x \) and \( G_y \) than in \( G \). The number containing exactly one of \( x \) and \( y \) in \( G_x \) is at least twice the number in \( G \) containing \( x \) but not \( y \), and similarly for \( G_y \). Thus, for an extremal graph \( G \), we must have \( q(G) = q(G_x) = q(G_y) \). Repeating this process, we obtain an extremal graph consisting of disjoint complete graphs.

Next, suppose the complete graphs in \( G \) have sizes \( a_1, a_2, \ldots, a_n \). Then

\[
q(G) = \sum_{i=1}^{n} \binom{a_i}{2} \sum_{\substack{j<k \\ j, k \neq i}} a_j a_k.
\]

If we fix all \( a_i \) except two, say \( p, q \), with \( p+q = s \) fixed, then for some constants \( C_i \), we have \( q(G) = C_1 + C_2 pq + C_3 \left( \binom{p}{2} + \binom{q}{2} \right) + C_4 \left( q\binom{p}{2} + p\binom{q}{2} \right) = A + Bpq \), where \( A \) and \( B \) depend only on \( s \). Thus, the maximum of \( q(G) \) is attained if \( |p-q| \leq 1 \) or \( pq = 0 \). Therefore, if \( q(G) \) is maximal, any two nonzero \( a_i \)'s differ by at most 1.

Finally, if \( G \) consists of \( n \) disjoint complete graphs, then \( q(G) \) cannot exceed the value obtained if \( a_1 = \cdots = a_n \) (not necessarily integral), which equals

\[
Q_n = \frac{120^2}{n} \binom{120/n}{2} \binom{n-1}{2} = 30 \cdot 120^2 \frac{(n-1)(n-2)(120-n)}{n^3}.
\]

It is easy to check that \( Q_n \) takes its maximum when \( n = 5 \) and \( a_1 = \cdots = a_5 = 24 \), and this maximum equals \( 15 \cdot 23 \cdot 24^3 = 4769280 \).

\(\boxed{4769280}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have 120 people, some pairs are friends. A weak quartet is a set of 4 people containing exactly one pair of friends. We want to maximize the number of weak quartets.

Let me think about this. Let the friendship graph be G on n=120 vertices. A weak quartet is a 4-set with exactly one edge.

Let me count weak quartets by summing over edges. For each edge (u,v), the number of 4-sets containing exactly this one edge (and no other edges among the 4) is: we pick 2 more vertices from the remaining 118, such that neither is adjacent to u or v (within the 4-set), and the two chosen vertices are not adjacent to each other, and neither chosen vertex is adjacent to u or v.

Wait, let me be more careful. A 4-set {a,b,c,d} with exactly one edge, say {a,b}. Then:
- c and d are not adjacent to each other
- c is not adjacent to a, b
- d is not adjacent to a, b
- a,b are adjacent (the one edge)

So for edge (a,b), the number of weak quartets where {a,b} is the unique friend pair = number of ways to choose {c,d} from the remaining 118 vertices such that:
- c,d not adjacent to each other
- c not adjacent to a, c not adjacent to b
- d not adjacent to a, d not adjacent to b

Let me define for edge (a,b): let S = set of vertices (other than a,b) that are not adjacent to a and not adjacent to b. Then we need to choose 2 vertices from S that are not adjacent to each other. The number of such pairs = C(|S|, 2) - (number of edges within S).

So total weak quartets W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

where S_{ab} = vertices not adjacent to a and not adjacent to b (excluding a,b themselves), and e(S_{ab}) is the number of edges within S_{ab}.

This is complex. Let me think about what graph structure maximizes this.

Intuition: To maximize weak quartets, we want many edges, but each edge should have many non-neighbors. There's tension.

Let me think about a complete bipartite graph or a specific structure.

Actually, let me think about a graph that is a complete graph on some subset, or a disjoint union of cliques, or a complete bipartite graph.

Let me consider the graph being a complete bipartite graph K_{a,b} with a+b=120. In K_{a,b}, edges are between the two parts. A 4-set with exactly one edge: pick 1 from part A and 3 from part B? No wait. In K_{a,b}, every vertex in A is adjacent to every vertex in B. So a 4-set with vertices from both parts will have many edges.

If we pick 2 from A and 2 from B: that gives 4 edges (complete bipartite K_{2,2}). Not weak.
If we pick 1 from A and 3 from B: 3 edges. Not weak.
If we pick 4 from A: 0 edges. Not weak.
If we pick 4 from B: 0 edges. Not weak.

So K_{a,b} gives 0 weak quartets. Bad.

Let me think about a graph that is a matching (disjoint edges). If we have m edges forming a matching on 120 vertices (so 2m vertices used, 120-2m isolated). A weak quartet needs exactly one edge. 

For a 4-set to have exactly one edge: it contains exactly one of the matching edges and two other vertices that form no edge. The two other vertices must not form a matching edge, and must not be endpoints of... well, the 4-set contains one matching edge {a,b} and two other vertices c,d. For exactly one edge, c and d must not be adjacent (not a matching edge), and c,d must not be adjacent to a or b. But in a matching, c,d are adjacent to a or b only if they're the partners of a or b, but a,b are partners of each other, so c,d are not adjacent to a,b (unless c or d is a partner, but a's partner is b). So c,d just need to not be a matching edge themselves.

Number of weak quartets = sum over matching edges {a,b} of [C(118, 2) - (number of other matching edges)]

For matching edge {a,b}, the other vertices are 118. Among these 118, the number of matching edges not involving a,b = m-1. So pairs {c,d} that form an edge = m-1. So weak quartets from this edge = C(118,2) - (m-1).

Total = m * [C(118,2) - (m-1)] = m * [6973 - m + 1] = m * (6974 - m).

Maximize: m(6974 - m) is maximized at m = 3487, but m ≤ 60 (matching on 120 vertices). So at m=60: 60 * 6914 = 414840.

Hmm, but can we do better with a different structure?

Let me think about a graph that is a union of a clique and isolated vertices, or something else.

Actually, let me think more carefully. Let me consider a graph where we have a clique of size k and the rest (120-k) are isolated. 

A weak quartet needs exactly one edge. If we pick 4 vertices, the number of edges among them depends on how many are in the clique.

- 4 from clique: C(4,2)=6 edges. Not weak.
- 3 from clique, 1 isolated: C(3,2)=3 edges. Not weak.
- 2 from clique, 2 isolated: 1 edge. Weak! 
- 1 from clique, 3 isolated: 0 edges. Not weak.
- 0 from clique, 4 isolated: 0 edges. Not weak.

So weak quartets = C(k,2) * C(120-k, 2).

Maximize C(k,2)*C(120-k,2) over k. Let f(k) = k(k-1)/2 * (120-k)(119-k)/2.

Let me compute for k around 60. f(k) = k(k-1)(120-k)(119-k)/4.

By symmetry-ish (not exact symmetry due to -1 terms), the max is near k=60.

f(60) = 60*59*60*59/4 = (60*59)^2/4 = (3540)^2/4 = 12531600/4 = 3132900.

Wait let me recompute: 60*59 = 3540. 3540^2 = 12531600. /4 = 3132900.

That's way more than 414840. So the clique + isolated vertices is much better.

Let me check other values. f(k) = k(k-1)(120-k)(119-k)/4.

Let me set g(k) = k(k-1)(120-k)(119-k). Take derivative... or just check around k=60.

g(60) = 60*59*60*59 = 3540*3540 = 12531600.
g(59) = 59*58*61*60 = 59*58*3660 = 3422*3660 = 12524520.
g(61) = 61*60*59*58 = 3660*3422 = 12524520.

So g(60) = 12531600, g(59) = g(61) = 12524520. So k=60 is the max (or very close).

Actually let me be more careful. Let h(k) = k(k-1)(120-k)(119-k). Let's substitute k = 60 + t. Then:
- k = 60+t, k-1 = 59+t, 120-k = 60-t, 119-k = 59-t.
h = (60+t)(59+t)(60-t)(59-t) = [(60+t)(60-t)][(59+t)(59-t)] = (3600-t²)(3481-t²).

Let u = t². h = (3600-u)(3481-u) = 3600*3481 - u(3600+3481) + u² = 12531600 - 7081u + u².

This is minimized at u = 7081/2 = 3540.5, so h is maximized at u=0 (t=0) since the parabola opens upward and the vertex is a minimum... wait no. h = u² - 7081u + 12531600. This is a parabola opening upward, so it has a minimum at u=3540.5. The maximum on the valid range is at the endpoints. But u = t² ≥ 0, and t must be an integer with 60+t between 0 and 120.

At u=0 (t=0): h = 12531600.
At u=1 (t=±1): h = 1 - 7081 + 12531600 = 12524520.

So h decreases as we move away from t=0. The maximum is at t=0, i.e., k=60.

So with a clique of 60 and 60 isolated vertices, we get 12531600/4 = 3132900 weak quartets.

But wait — can we do better with a different graph structure? The clique + isolated is a specific construction. Let me think about whether some other structure does better.

Let me think about the general problem more carefully. 

Total weak quartets W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

where S_{ab} = common non-neighbors of a and b (excluding a,b).

This is hard to optimize directly. Let me think about upper bounds.

Alternative counting: A weak quartet is a 4-set with exactly 1 edge. Let's think about it differently.

Let me count by choosing the edge and the two non-adjacent vertices. For edge e = {a,b}, let d(a) and d(b) be degrees. The number of vertices adjacent to a or b (excluding a,b) is |N(a) ∪ N(b)| - (count a,b if they're in neighborhoods, but they're not since no self-loops, but b ∈ N(a) and a ∈ N(b)). Let me be careful.

N(a) = neighbors of a, not including a. b ∈ N(a) since {a,b} is an edge.
N(b) = neighbors of b, not including b. a ∈ N(b).

Vertices (other than a,b) adjacent to a: |N(a)| - 1 = d(a) - 1 (removing b).
Vertices (other than a,b) adjacent to b: |N(b)| - 1 = d(b) - 1 (removing a).
Vertices (other than a,b) adjacent to a or b: |N(a) ∪ N(b)| - 2 (removing a and b from the union, since a ∈ N(b) and b ∈ N(a)).

|N(a) ∪ N(b)| = d(a) + d(b) - |N(a) ∩ N(b)|.

So vertices adjacent to a or b (excl. a,b) = d(a) + d(b) - |N(a) ∩ N(b)| - 2.

S_{ab} = vertices not adjacent to a and not adjacent to b (excl. a,b) = 118 - [d(a) + d(b) - |N(a) ∩ N(b)| - 2] = 120 - d(a) - d(b) + |N(a) ∩ N(b)|.

So |S_{ab}| = 120 - d(a) - d(b) + |N(a) ∩ N(b)|.

For the clique + isolated construction: clique of size 60. For an edge (a,b) in the clique: d(a) = d(b) = 59, |N(a) ∩ N(b)| = 58 (the other 58 clique members). |S_{ab}| = 120 - 59 - 59 + 58 = 60. And e(S_{ab}) = 0 (S_{ab} is the 60 isolated vertices). So weak quartets per edge = C(60,2) = 1770. Total = C(60,2) * 1770 = 1770 * 1770 = 3132900. ✓.

Now, can we beat this? Let me think about an upper bound.

W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

≤ sum over edges (a,b) of C(|S_{ab}|, 2)

= sum over edges (a,b) of C(120 - d(a) - d(b) + |N(a) ∩ N(b)|, 2)

This is still complex. Let me think about whether the clique + isolated is optimal.

Let me consider a more general structure: a complete multipartite graph or a graph with a clique and some other structure.

Actually, let me think about it differently. Consider a graph with a clique C of size k and the rest being independent set I of size 120-k, with NO edges between C and I. Then:

Weak quartets = C(k,2) * C(120-k, 2) (as computed: 2 from clique, 2 from independent set).

What if we add some edges between C and I, or within I? 

If we add an edge between a vertex in C and a vertex in I: this could create new weak quartets but also destroy some. Let's see. Adding edge (c, i) where c ∈ C, i ∈ I:
- This destroys weak quartets that contained {c, i'} for i' ∈ I (since now c-i' might... no, c-i' is not an edge unless i'=i). Actually, adding edge (c,i) affects quartets containing both c and i. 

Hmm, this is getting complicated. Let me think about it more carefully with a cleaner approach.

Let me consider the complement graph approach. In the complement graph $\bar{G}$, a weak quartet (exactly 1 edge in G) corresponds to a 4-set with exactly 5 edges in $\bar{G}$ (i.e., exactly 1 non-edge in $\bar{G}$, which is exactly 1 edge in G). So a weak quartet in G = a 4-set in $\bar{G}$ with exactly C(4,2)-1 = 5 edges.

Alternatively, let me think about it as: we want to maximize the number of 4-sets with exactly 1 edge.

Let me think about the problem as follows. Let's use the edge-centric count:

W = sum over edges e={a,b} of f(e)

where f(e) = number of 4-sets where {a,b} is the unique edge = number of pairs {c,d} ⊆ S_{ab} with c,d non-adjacent = C(|S_{ab}|, 2) - e(S_{ab}).

Now, I want to find the graph maximizing W. 

Let me think about what happens with two cliques. Say clique of size k and clique of size 120-k, with no edges between them. Then:

A 4-set with exactly 1 edge: 
- 2 from clique 1, 2 from clique 2: 1 + 1 = 2 edges. Not weak.
- 3 from clique 1, 1 from clique 2: 3 edges. Not weak.
- 2 from clique 1, 1 from clique 2, 1 from... wait, there are only two cliques. 
- 4 from clique 1: 6 edges. Not weak.
- 3 from clique 1, 1 from clique 2: C(3,2) = 3 edges. Not weak.
- 2 from clique 1, 2 from clique 2: 1 + 1 = 2 edges. Not weak.

So two cliques give 0 weak quartets. Bad.

What about a clique and an independent set with some edges between them? Let me think about a "split graph" — clique of size k, independent set of size 120-k, and some edges between them.

Let's say we have clique C (size k), independent set I (size m = 120-k), and a bipartite graph B between C and I. 

A 4-set can have vertices from C and I in various combinations. Let me categorize:

Case 1: 2 from C, 2 from I. Edges among them: 1 (from C) + (edges from B between these 2 C-vertices and 2 I-vertices) + 0 (I is independent). For weak quartet, we need exactly 1 edge, so 0 edges from B. So we need both I-vertices to be non-neighbors of both C-vertices in B.

Case 2: 1 from C, 3 from I. Edges: 0 (from C alone) + (edges from B between the 1 C-vertex and 3 I-vertices) + 0. For weak, exactly 1 edge from B, so exactly 1 of the 3 I-vertices is adjacent to the C-vertex.

Case 3: 3 from C, 1 from I. Edges: 3 (from C) + (edges from B). ≥ 3. Not weak.

Case 4: 4 from C: 6 edges. Not weak.
Case 5: 4 from I: 0 edges. Not weak.
Case 6: 0 from C: same as case 5.

So weak quartets come from cases 1 and 2.

W = [Case 1] + [Case 2]

Case 1: Choose 2 from C (C(k,2) ways), 2 from I (C(m,2) ways), such that neither I-vertex is adjacent to either C-vertex. 

Case 2: Choose 1 from C (k ways), 3 from I (C(m,3) ways), such that exactly 1 of the 3 I-vertices is adjacent to the C-vertex.

This is getting complex. Let me think about whether adding edges between C and I can increase W beyond the pure clique+independent case.

In the pure case (no B edges): 
- Case 1: C(k,2) * C(m,2) (all pairs work since no B edges).
- Case 2: 0 (no B edges means 0 edges from B, not 1).

W = C(k,2)*C(m,2), maximized at k=60 giving 3132900.

Now if we add B edges:
- Case 1 decreases (some pairs now have B edges).
- Case 2 increases (now possible to have exactly 1 B edge).

The question is whether the gain from Case 2 can exceed the loss from Case 1.

Let me consider a specific example. Take k=60, m=60. Add a perfect matching between C and I (each c_i connected to exactly one i_j, and each i_j to exactly one c_i). So each C-vertex has 1 B-neighbor, each I-vertex has 1 B-neighbor.

Case 1: Choose 2 from C, 2 from I. The number of "bad" choices (where some B edge exists among the 4) = choices where at least one of the 2 C-vertices is B-matched to one of the 2 I-vertices.

Total Case 1 pairs: C(60,2)*C(60,2) = 1770*1770 = 3132900.
Bad pairs: Let's count. For a fixed pair {c_a, c_b} from C, their B-neighbors are i_a, i_b (distinct since matching). Bad I-pairs: those containing i_a or i_b. Number of I-pairs containing i_a or i_b = C(60,2) - C(58,2) = 1770 - 1653 = 117. (Pairs containing i_a: 59. Containing i_b: 59. Containing both: 1. Total: 59+59-1 = 117.)

So bad Case 1 = C(60,2) * 117 = 1770 * 117 = 207090.
Good Case 1 = 3132900 - 207090 = 2925810.

Case 2: Choose 1 from C (say c_a with B-neighbor i_a), 3 from I. Exactly 1 of the 3 I-vertices is i_a. So we need i_a in the triple and the other 2 from I\{i_a}, and neither of the other 2 is B-matched to c_a (but c_a's only B-match is i_a, so the other 2 just need to not be i_a, which they aren't). So: choose i_a and 2 from the other 59 I-vertices: C(59,2) = 1711. Per C-vertex: 1711. Total Case 2 = 60 * 1711 = 102660.

Total W = 2925810 + 102660 = 3028470.

This is less than 3132900. So adding a matching made it worse.

Let me try a different approach: what if we make B very sparse but strategic? Actually, the loss in Case 1 seems to dominate. Let me check if there's a regime where Case 2 gain dominates.

Actually, let me think about this more carefully. Let me consider the general split graph and try to optimize.

Let me denote the B-graph between C and I. For a C-vertex c, let b(c) = number of B-neighbors (degree in B). For an I-vertex i, let b(i) = number of B-neighbors.

Case 1 contribution: sum over pairs {c_a, c_b} ⊆ C, pairs {i_x, i_y} ⊆ I, such that none of (c_a,i_x), (c_a,i_y), (c_b,i_x), (c_b,i_y) are B-edges.

Case 2 contribution: sum over c ∈ C, triples {i_x, i_y, i_z} ⊆ I, such that exactly one of (c, i_x), (c, i_y), (c, i_z) is a B-edge.

For Case 2, fixing c with b(c) = d: number of triples with exactly 1 B-neighbor of c = d * C(m-d, 2). (Choose 1 from the d B-neighbors, 2 from the m-d non-B-neighbors.)

Case 2 = sum over c ∈ C of b(c) * C(m - b(c), 2).

For Case 1, it's more complex. Let me think about it for a specific structure.

Hmm, this is getting complicated. Let me step back and think about whether the clique + independent set is actually optimal, or if there's a fundamentally different structure that does better.

Let me think about upper bounds. 

Alternative approach: Let's think about the problem in terms of the complement. In $\bar{G}$, a weak quartet corresponds to a 4-set inducing exactly 5 edges (i.e., a 4-set whose complement has exactly 1 edge, meaning the 4-set in $\bar{G}$ is missing exactly 1 edge, i.e., it's a K4 minus one edge).

So we want to maximize the number of 4-sets that induce exactly K4 - e in $\bar{G}$, which is the same as maximizing 4-sets that induce exactly 1 edge in G.

Hmm, let me think about this differently. Let me consider the "clique + independent set" more carefully and see if we can prove it's optimal, or find something better.

Actually, let me consider a different structure: a disjoint union of a clique and some other stuff, or a "threshold graph."

Let me try a different construction: Take a clique of size k and an independent set of size 120-k, but now also consider making the independent set into a sparse graph.

Wait, actually, let me reconsider. What if instead of a clique + independent set, we use a different split?

Let me try: clique C of size k, independent set I of size m = 120-k, and complete bipartite between C and I. This is a "split graph" where C is a clique, I is independent, and all C-I edges exist. This is actually a "threshold graph."

In this case:
- 2 from C, 2 from I: 1 (C edge) + 4 (B edges) = 5 edges. Not weak.
- 1 from C, 3 from I: 0 + 3 (B edges) = 3. Not weak.
- 3 from C, 1 from I: 3 + 3 = 6. Not weak.
- 4 from C: 6. Not weak.
- 4 from I: 0. Not weak.

So 0 weak quartets. Bad.

What about clique C of size k, independent I of size m, and NO edges between them (our original construction)? W = C(k,2)*C(m,2), max at k=60: 3132900.

What if we use a different structure entirely? Let me think about a "blow-up" or other constructions.

Let me try: partition into 3 groups. Group A (size a), Group B (size b), Group C (size c), a+b+c=120. Make A a clique, B and C independent sets, no edges between any groups. Then:

Weak quartets: 2 from A (1 edge), 2 from B∪C (0 edges since B,C independent and no inter-group edges). So W = C(a,2) * C(120-a, 2). Same as before with k=a. No improvement.

What if A is a clique, B is a clique, C is independent, no inter-group edges?
- 2 from A, 2 from B: 1+1 = 2 edges. Not weak.
- 2 from A, 2 from C: 1+0 = 1. Weak!
- 2 from B, 2 from C: 1+0 = 1. Weak!
- 2 from A, 1 from B, 1 from C: 1+1+0 = 2. Not weak.
- 1 from A, 2 from B, 1 from C: 0+1+0 = 1. Weak!
- 1 from A, 1 from B, 2 from C: 0+0+0 = 0. Not weak.
- 3 from A, 1 from C: 3. Not weak.
- etc.

W = C(a,2)*C(c,2) + C(b,2)*C(c,2) + a*C(b,2)*c + ... 

Wait let me be more careful. Let me enumerate all 4-sets with exactly 1 edge.

Groups: A (clique, size a), B (clique, size b), C (independent, size c), a+b+c=120, no inter-group edges.

4-set compositions (x from A, y from B, z from C, x+y+z=4):
- (2,0,2): edges = C(2,2)=1 from A. Weak. Count: C(a,2)*C(c,2).
- (0,2,2): edges = 1 from B. Weak. Count: C(b,2)*C(c,2).
- (2,2,0): edges = 1+1 = 2. Not weak.
- (1,2,1): edges = 0+1+0 = 1. Weak. Count: a*C(b,2)*c.
- (2,1,1): edges = 1+0+0 = 1. Weak. Count: C(a,2)*b*c.
- (1,1,2): edges = 0+0+0 = 0. Not weak.
- (3,0,1): edges = 3. Not weak.
- (0,3,1): edges = 3. Not weak.
- (1,3,0): edges = 3. Not weak.
- (3,1,0): edges = 3+0 = 3. Not weak.
- (0,0,4): 0. Not weak.
- (4,0,0): 6. Not weak.
- (0,4,0): 6. Not weak.
- (1,0,3): 0. Not weak.
- (0,1,3): 0. Not weak.

W = C(a,2)*C(c,2) + C(b,2)*C(c,2) + a*C(b,2)*c + C(a,2)*b*c

= C(c,2)[C(a,2) + C(b,2)] + c[C(a,2)*b + a*C(b,2)]

= C(c,2)[C(a,2) + C(b,2)] + c[C(a,2)*b + a*C(b,2)]

Let me factor. Note C(a,2)*b + a*C(b,2) = ab[(a-1)/2 + (b-1)/2] = ab(a+b-2)/2 = ab(a+b-2)/2.

And C(a,2) + C(b,2) = [a(a-1) + b(b-1)]/2 = [a²+b²-a-b]/2.

Let s = a+b, so c = 120-s. Then:
C(a,2)+C(b,2) = [a²+b²-s]/2 = [(a+b)²-2ab-s]/2 = [s²-2ab-s]/2.
C(a,2)*b + a*C(b,2) = ab(s-2)/2.

W = C(c,2) * [s²-2ab-s]/2 + c * ab(s-2)/2

= (1/2){C(c,2)[s²-s-2ab] + c·ab(s-2)}

Note s²-s = s(s-1). And C(c,2) = c(c-1)/2.

W = (1/2){c(c-1)/2 * [s(s-1)-2ab] + c·ab(s-2)}

= (c/2){(c-1)/2 * [s(s-1)-2ab] + ab(s-2)}

= (c/4){(c-1)[s(s-1)-2ab] + 2ab(s-2)}

= (c/4){(c-1)s(s-1) - 2ab(c-1) + 2ab(s-2)}

= (c/4){(c-1)s(s-1) + 2ab[s-2-c+1]}

= (c/4){(c-1)s(s-1) + 2ab[s-c-1]}

Since c = 120-s: s-c-1 = s-(120-s)-1 = 2s-121.

W = (c/4){(c-1)s(s-1) + 2ab(2s-121)}

Now, for fixed s (and thus c), we want to optimize over a,b with a+b=s. The term involving ab is 2ab(2s-121). 

If 2s-121 > 0, i.e., s > 60.5, i.e., s ≥ 61: we want to maximize ab, so a=b=s/2.
If 2s-121 < 0, i.e., s ≤ 60: we want to minimize ab, so a=1,b=s-1 (or vice versa), giving ab = s-1.
If 2s-121 = 0, i.e., s = 60.5: not integer.

Case s ≤ 60: minimize ab → a=1, b=s-1. Then ab = s-1. But wait, if a=1, then C(a,2)=0, so A is just a single vertex (no clique edges). This effectively reduces to the 2-clique case (just B and C). Let me check: with a=1, b=s-1, c=120-s:

W = (c/4){(c-1)s(s-1) + 2(s-1)(2s-121)}

= (c(s-1)/4){(c-1)s + 2(2s-121)}

= (c(s-1)/4){s(c-1) + 4s - 242}

= (c(s-1)/4){s(c-1+4) - 242}

= (c(s-1)/4){s(c+3) - 242}

With c = 120-s: s(123-s) - 242 = 123s - s² - 242.

W = (c(s-1)/4)(123s - s² - 242) = ((120-s)(s-1)/4)(123s - s² - 242)

Let me maximize this for s ≤ 60. Let me check s=60: c=60.
W = (60*59/4)(123*60 - 3600 - 242) = (885)(7380 - 3600 - 242) = 885 * 3538 = 3131130.

Hmm, that's slightly less than 3132900. Let me double-check. With a=1, b=59, c=60:

W = C(1,2)*C(60,2) + C(59,2)*C(60,2) + 1*C(59,2)*60 + C(1,2)*59*60
= 0 + 1711*1770 + 1711*60 + 0
= 1711*1770 + 1711*60
= 1711*1830
= 3131130.

And the pure clique+independent with k=60: C(60,2)*C(60,2) = 1770*1770 = 3132900.

So 3132900 > 3131130. The 2-group clique+independent is better.

Case s ≥ 61: maximize ab → a=b=s/2 (if s even) or a=(s-1)/2, b=(s+1)/2 (if s odd). Let me try s=62, a=b=31, c=58.

W = (c/4){(c-1)s(s-1) + 2ab(2s-121)}
= (58/4){57*62*61 + 2*961*3}
= 14.5{57*62*61 + 5766}
= 14.5{215094 + 5766}
= 14.5 * 220860
= 3202470.

Wait, that's more than 3132900! Let me double-check.

s=62, a=31, b=31, c=58.

C(a,2) = C(31,2) = 465. C(b,2) = 465. C(c,2) = C(58,2) = 1653.

W = C(a,2)*C(c,2) + C(b,2)*C(c,2) + a*C(b,2)*c + C(a,2)*b*c
= 465*1653 + 465*1653 + 31*465*58 + 465*31*58
= 2*465*1653 + 2*31*465*58
= 2*465*(1653 + 31*58)
= 930*(1653 + 1798)
= 930 * 3451
= 3209430.

Hmm, let me recompute. 31*58 = 1798. 1653 + 1798 = 3451. 930 * 3451 = 3209430.

Wait, that's even higher. Let me recheck my formula.

W = C(a,2)*C(c,2) + C(b,2)*C(c,2) + a*C(b,2)*c + C(a,2)*b*c

With a=b=31, c=58:
C(a,2) = 465, C(b,2) = 465, C(c,2) = 1653.
a*C(b,2)*c = 31*465*58 = 31*465*58. 465*58 = 26970. 31*26970 = 836070.
C(a,2)*b*c = 465*31*58 = same = 836070.
C(a,2)*C(c,2) = 465*1653 = 768645.
C(b,2)*C(c,2) = 465*1653 = 768645.

W = 768645 + 768645 + 836070 + 836070 = 3209430.

So W = 3209430 > 3132900. The 3-group construction is better!

Let me explore more. Let me try to optimize over s and a,b.

For s ≥ 61, with a=b=s/2 (s even), ab = s²/4:

W = (c/4){(c-1)s(s-1) + 2*(s²/4)*(2s-121)}
= (c/4){(c-1)s(s-1) + (s²/2)(2s-121)}
= (c/4){(c-1)s(s-1) + s²(2s-121)/2}

With c = 120-s. Let me compute for several values of s.

s=62, c=58: W = 3209430 (computed above).
s=64, c=56, a=b=32: 
C(32,2)=496, C(56,2)=1540.
W = 2*496*1540 + 2*32*496*56 = 992*1540 + 64*496*56 = 1527680 + 64*27776 = 1527680 + 1777664 = 3305344.

s=66, c=54, a=b=33:
C(33,2)=528, C(54,2)=1431.
W = 2*528*1431 + 2*33*528*54 = 1056*1431 + 66*528*54 = 1511136 + 66*28512 = 1511136 + 1881792 = 3392928.

s=68, c=52, a=b=34:
C(34,2)=561, C(52,2)=1326.
W = 2*561*1326 + 2*34*561*52 = 1122*1326 + 68*561*52 = 1487772 + 68*29172 = 1487772 + 1983696 = 3471468.

s=70, c=50, a=b=35:
C(35,2)=595, C(50,2)=1225.
W = 2*595*1225 + 2*35*595*50 = 1190*1225 + 70*595*50 = 1457750 + 70*29750 = 1457750 + 2082500 = 3540250.

s=72, c=48, a=b=36:
C(36,2)=630, C(48,2)=1128.
W = 2*630*1128 + 2*36*630*48 = 1260*1128 + 72*630*48 = 1421280 + 72*30240 = 1421280 + 2177280 = 3598560.

s=74, c=46, a=b=37:
C(37,2)=666, C(46,2)=1035.
W = 2*666*1035 + 2*37*666*46 = 1332*1035 + 74*666*46 = 1378620 + 74*30636 = 1378620 + 2267064 = 3645684.

s=76, c=44, a=b=38:
C(38,2)=703, C(44,2)=946.
W = 2*703*946 + 2*38*703*44 = 1406*946 + 76*703*44 = 1330076 + 76*30932 = 1330076 + 2350832 = 3680908.

s=78, c=42, a=b=39:
C(39,2)=741, C(42,2)=861.
W = 2*741*861 + 2*39*741*42 = 1482*861 + 78*741*42 = 1276302 + 78*31122 = 1276302 + 2427516 = 3703818.

s=80, c=40, a=b=40:
C(40,2)=780, C(40,2)=780.
W = 2*780*780 + 2*40*780*40 = 2*608400 + 80*780*40 = 1216800 + 2496000 = 3712800.

s=82, c=38, a=b=41:
C(41,2)=820, C(38,2)=703.
W = 2*820*703 + 2*41*820*38 = 1640*703 + 82*820*38 = 1152920 + 82*31160 = 1152920 + 2555120 = 3708040.

s=84, c=36, a=b=42:
C(42,2)=861, C(36,2)=630.
W = 2*861*630 + 2*42*861*36 = 1722*630 + 84*861*36 = 1084860 + 84*30996 = 1084860 + 2603664 = 3688524.

So the maximum seems to be around s=80, giving W = 3712800.

Let me check s=80 more carefully and nearby odd values.

s=79, c=41, a=39, b=40 (to maximize ab with a+b=79, ab = 39*40 = 1560):
C(39,2)=741, C(40,2)=780, C(41,2)=820.
W = 741*820 + 780*820 + 39*780*41 + 741*40*41
= 820*(741+780) + 41*(39*780 + 741*40)
= 820*1521 + 41*(30420 + 29640)
= 1247220 + 41*60060
= 1247220 + 2462460
= 3709680.

s=81, c=39, a=40, b=41 (ab = 40*41 = 1640):
C(40,2)=780, C(41,2)=820, C(39,2)=741.
W = 780*741 + 820*741 + 40*820*39 + 780*41*39
= 741*(780+820) + 39*(40*820 + 780*41)
= 741*1600 + 39*(32800 + 31980)
= 1185600 + 39*64780
= 1185600 + 2526420
= 3712020.

So s=81 gives 3712020, slightly less than s=80's 3712800.

s=80, a=b=40, c=40: W = 3712800.

Let me also check s=80 with unequal a,b. a+b=80, c=40. 
W = (c/4){(c-1)s(s-1) + 2ab(2s-121)}
= (40/4){39*80*79 + 2ab*39}
= 10{39*6320 + 78ab}
= 10{246480 + 78ab}
= 2464800 + 780ab.

Maximize ab with a+b=80: ab ≤ 40*40 = 1600. So W ≤ 2464800 + 780*1600 = 2464800 + 1248000 = 3712800. ✓

So for s=80, the max is at a=b=40, giving 3712800.

Now let me check if s=80 is truly optimal. For even s with a=b=s/2:

W = (c/4){(c-1)s(s-1) + (s²/2)(2s-121)} where c=120-s.

Let me define F(s) = (120-s)/4 * {(119-s)*s*(s-1) + (s²/2)(2s-121)}.

Let me compute more values:
s=78: 3703818
s=80: 3712800
s=82: 3708040

So the peak is at s=80. Let me verify by checking the formula at s=80:
c=40, (c-1)=39, s(s-1)=80*79=6320, s²/2=3200, 2s-121=39.
F(80) = 40/4 * {39*6320 + 3200*39} = 10 * {246480 + 124800} = 10 * 371280 = 3712800. ✓

Now, the question is: can we do even better with more groups? Let me try 4 groups: two cliques A, B and two independent sets... actually, let me think about this more generally.

Let me try 4 groups: A (clique, a), B (clique, b), C (independent, c), D (independent, d), no inter-group edges, a+b+c+d=120.

A weak quartet needs exactly 1 edge. The edge must come from within A or within B. 

If the edge is from A (2 vertices from A), the other 2 must come from B∪C∪D with 0 edges among them. But if any of the other 2 is from B, we need only 1 from B (which gives 0 edges from B since we need 2 for an edge) — wait, if we pick 1 from B, that's 0 edges from B. If we pick 2 from B, that's 1 edge from B, making 2 total. So the other 2 can be: 2 from C∪D (0 edges), or 1 from B and 1 from C∪D (0 edges), or 2 from B (1 edge, total 2, not weak).

Hmm wait, let me reconsider. With 4 groups, the analysis gets more complex. Let me think about whether more groups can help.

Actually, let me reconsider. The 3-group case with two cliques and one independent set gave 3712800. Can 4 groups do better?

Let me try: A (clique, a), B (clique, b), C (independent, c), D (independent, d), a+b+c+d=120, no inter-group edges.

Weak quartets (exactly 1 edge):
The 1 edge comes from A or B.

Edge from A (pick 2 from A): other 2 from B∪C∪D with 0 edges.
- 2 from C: 0 edges. Count: C(a,2)*C(c,2).
- 2 from D: 0 edges. Count: C(a,2)*C(d,2).
- 1 from C, 1 from D: 0 edges. Count: C(a,2)*c*d.
- 1 from B, 1 from C: 0 edges. Count: C(a,2)*b*c.
- 1 from B, 1 from D: 0 edges. Count: C(a,2)*b*d.
- 2 from B: 1 edge. Total 2. Not weak.
- 2 from C∪D but mixing: covered above.

Edge from B (pick 2 from B): other 2 from A∪C∪D with 0 edges.
- 2 from C: C(b,2)*C(c,2).
- 2 from D: C(b,2)*C(d,2).
- 1 from C, 1 from D: C(b,2)*c*d.
- 1 from A, 1 from C: C(b,2)*a*c.
- 1 from A, 1 from D: C(b,2)*a*d.
- 2 from A: 1 edge. Not weak.

So W = [C(a,2) + C(b,2)] * [C(c,2) + C(d,2) + cd] + [C(a,2)*b + C(b,2)*a] * [c + d]

Note C(c,2) + C(d,2) + cd = C(c+d, 2) = C(c+d,2). And c+d = 120-a-b.

Also C(a,2)*b + C(b,2)*a = ab[(a-1)+(b-1)]/2 = ab(a+b-2)/2.

And C(a,2) + C(b,2) = [a(a-1)+b(b-1)]/2 = [a²+b²-a-b]/2 = [(a+b)²-2ab-(a+b)]/2.

Let s = a+b, t = c+d = 120-s.

W = [(s²-2ab-s)/2] * C(t,2) + [ab(s-2)/2] * t

= (1/2){[s²-s-2ab]*C(t,2) + ab(s-2)*t}

= (1/2){[s(s-1)-2ab]*t(t-1)/2 + ab(s-2)*t}

= (t/2){[s(s-1)-2ab]*(t-1)/2 + ab(s-2)}

= (t/4){[s(s-1)-2ab](t-1) + 2ab(s-2)}

= (t/4){s(s-1)(t-1) - 2ab(t-1) + 2ab(s-2)}

= (t/4){s(s-1)(t-1) + 2ab[s-2-t+1]}

= (t/4){s(s-1)(t-1) + 2ab[s-t-1]}

With t = 120-s: s-t-1 = s-(120-s)-1 = 2s-121.

W = (t/4){s(s-1)(t-1) + 2ab(2s-121)}

This is exactly the same formula as the 3-group case! (Where c in the 3-group formula = t here.) So the 4-group case with 2 cliques and 2 independent sets gives the same W as the 3-group case with 2 cliques and 1 independent set (of the same total size). The split of the independent set doesn't matter because C(c,2)+C(d,2)+cd = C(c+d,2).

So we can't do better by splitting the independent set. Good.

Now, what about 3 cliques and 1 independent set? Or more generally, k cliques and 1 independent set?

Let me generalize: k cliques of sizes a_1, ..., a_k and 1 independent set of size c, with sum a_i + c = 120, no inter-group edges.

A weak quartet has exactly 1 edge, which comes from one of the cliques. Say the edge is from clique i (pick 2 from clique i). The other 2 vertices must have 0 edges among them. The other 2 can come from:
- The independent set: 2 from C, 0 edges. Count: C(a_i,2)*C(c,2).
- One from another clique j and one from C: 0 edges. Count: C(a_i,2)*a_j*c.
- One from another clique j and one from another clique l (j≠l): 0 edges. Count: C(a_i,2)*a_j*a_l.
- Two from the same other clique j: 1 edge. Not weak.

So for edge from clique i, the number of valid pairs for the other 2 = C(c,2) + c*(s-a_i) + C(s-a_i, 2) - sum_j C(a_j,2) [where the sum is over j≠i, and s = sum of all a_j].

Wait, let me think again. The other 2 vertices come from (all other cliques ∪ independent set), which has size (120 - a_i). Among these, the number of pairs with 0 edges = total pairs - pairs that form an edge = C(120-a_i, 2) - sum_{j≠i} C(a_j, 2).

Because the only edges among the remaining vertices are within each clique j (j≠i). The independent set has no internal edges, and there are no inter-group edges.

So W = sum_i C(a_i, 2) * [C(120-a_i, 2) - sum_{j≠i} C(a_j, 2)]

Let me denote T = sum_j C(a_j, 2) (total edges in all cliques). Then sum_{j≠i} C(a_j, 2) = T - C(a_i, 2).

W = sum_i C(a_i, 2) * [C(120-a_i, 2) - T + C(a_i, 2)]

= sum_i C(a_i, 2) * C(120-a_i, 2) - T * sum_i C(a_i, 2) + sum_i C(a_i, 2)²

= sum_i C(a_i, 2) * C(120-a_i, 2) - T² + sum_i C(a_i, 2)²

= sum_i C(a_i, 2) * C(120-a_i, 2) - T² + sum_i C(a_i, 2)²

Note T² - sum_i C(a_i,2)² = sum_{i≠j} C(a_i,2)*C(a_j,2) = 2*sum_{i<j} C(a_i,2)*C(a_j,2).

So W = sum_i C(a_i,2)*C(120-a_i,2) - 2*sum_{i<j} C(a_i,2)*C(a_j,2).

Hmm, let me verify with the 2-clique case. k=2, a_1=a, a_2=b, c=120-a-b.

W = C(a,2)*C(120-a,2) + C(b,2)*C(120-b,2) - 2*C(a,2)*C(b,2).

Let me check with a=b=40, c=40:
C(40,2)=780, C(80,2)=3160.
W = 780*3160 + 780*3160 - 2*780*780 = 2*780*3160 - 2*780² = 2*780*(3160-780) = 1560*2380 = 3712800. ✓

Now let me try k=3 cliques. Let a_1=a_2=a_3=40, c=0. But then 120 = 120, c=0. No independent set.

W = 3*C(40,2)*C(80,2) - 2*3*C(40,2)² = 3*780*3160 - 6*780² = 3*2464800 - 6*608400 = 7394400 - 3650400 = 3744000.

Wait, that's more than 3712800! Let me double-check.

3 cliques of size 40, no independent set, no inter-group edges. Total vertices = 120.

A weak quartet: exactly 1 edge. The edge comes from one clique. Say from clique 1: pick 2 from clique 1 (C(40,2)=780 ways), then 2 from the rest (cliques 2 and 3, total 80 vertices) with 0 edges. Pairs from cliques 2∪3 with 0 edges = C(80,2) - C(40,2) - C(40,2) = 3160 - 780 - 780 = 1600. 

So from clique 1: 780 * 1600 = 1248000.
By symmetry, same for cliques 2 and 3.
W = 3 * 1248000 = 3744000.

Yes! 3744000 > 3712800. So 3 cliques of 40 is better!

Let me check the formula: W = 3*780*3160 - 6*780² = 7394400 - 3650400 = 3744000. ✓

Can we do even better? Let me try 4 cliques of size 30, c=0.

C(30,2) = 435, C(90,2) = 4005.
W = 4*435*4005 - 2*6*435² = 4*435*4005 - 12*189225 = 6970860 - 2270700 = 4700160.

Wait, that's way more! Let me double-check.

4 cliques of 30, no inter-group edges, total 120.

Weak quartet: edge from clique i (C(30,2)=435 ways). Other 2 from remaining 90 vertices (cliques j≠i) with 0 edges. Pairs with 0 edges = C(90,2) - 3*C(30,2) = 4005 - 1305 = 2700.

From each clique: 435 * 2700 = 1174500.
W = 4 * 1174500 = 4698000.

Hmm, let me recheck with the formula. 
W = sum_i C(a_i,2)*C(120-a_i,2) - 2*sum_{i<j} C(a_i,2)*C(a_j,2)
= 4*435*4005 - 2*C(4,2)*435² 
= 4*435*4005 - 12*435²
= 4*435*4005 - 12*189225
= 6970860 - 2270700 
= 4700160.

But direct calculation gives 4698000. Let me recheck.

Direct: from clique i, other 2 from 90 vertices with 0 edges = C(90,2) - 3*C(30,2) = 4005 - 3*435 = 4005 - 1305 = 2700. 435*2700 = 1174500. Total = 4*1174500 = 4698000.

Formula: sum_i C(a_i,2)*C(120-a_i,2) = 4*435*C(90,2) = 4*435*4005 = 6970860.
2*sum_{i<j} C(a_i,2)*C(a_j,2) = 2*6*435*435 = 12*189225 = 2270700.
W = 6970860 - 2270700 = 4700160.

There's a discrepancy. Let me recheck the formula derivation.

W = sum_i C(a_i, 2) * [C(120-a_i, 2) - sum_{j≠i} C(a_j, 2)]

= sum_i C(a_i,2)*C(120-a_i,2) - sum_i C(a_i,2)*sum_{j≠i} C(a_j,2)

= sum_i C(a_i,2)*C(120-a_i,2) - sum_i C(a_i,2)*(T - C(a_i,2))

= sum_i C(a_i,2)*C(120-a_i,2) - T*sum_i C(a_i,2) + sum_i C(a_i,2)²

= sum_i C(a_i,2)*C(120-a_i,2) - T² + sum_i C(a_i,2)²

where T = sum_i C(a_i,2).

For 4 cliques of 30: T = 4*435 = 1740.
sum_i C(a_i,2)*C(120-a_i,2) = 4*435*4005 = 6970860.
T² = 1740² = 3027600.
sum_i C(a_i,2)² = 4*435² = 4*189225 = 756900.

W = 6970860 - 3027600 + 756900 = 4700160.

But direct calculation gives 4698000. Let me recheck the direct calculation.

From clique 1: pick 2 from clique 1 (435 ways). Other 2 from vertices in cliques 2,3,4 (90 vertices). Pairs with 0 edges among these 90: total pairs = C(90,2) = 4005. Edges among these 90 = C(30,2)+C(30,2)+C(30,2) = 1305 (edges within clique 2, within clique 3, within clique 4; no inter-clique edges). So 0-edge pairs = 4005 - 1305 = 2700.

435 * 2700 = 1174500. Total = 4 * 1174500 = 4698000.

So there's a discrepancy: formula gives 4700160, direct gives 4698000. Let me find the error.

Ah wait, I think the issue is that C(120-a_i, 2) counts pairs from the remaining 120-a_i vertices, but some of those pairs include vertices from clique i itself! No, 120-a_i excludes clique i. The remaining vertices are from cliques j≠i and the independent set. In this case c=0, so remaining = cliques j≠i, which is 90 vertices. C(90,2) = 4005. ✓

And sum_{j≠i} C(a_j, 2) = 3*435 = 1305. ✓

So W = 4 * 435 * (4005 - 1305) = 4 * 435 * 2700 = 4698000.

Now let me recheck the formula:
sum_i C(a_i,2) * [C(120-a_i,2) - (T - C(a_i,2))]
= sum_i C(a_i,2) * C(120-a_i,2) - sum_i C(a_i,2)*(T - C(a_i,2))
= sum_i C(a_i,2)*C(120-a_i,2) - T*sum_i C(a_i,2) + sum_i C(a_i,2)^2

sum_i C(a_i,2) = T. So:
= sum_i C(a_i,2)*C(120-a_i,2) - T*T + sum_i C(a_i,2)^2
= sum_i C(a_i,2)*C(120-a_i,2) - T^2 + sum_i C(a_i,2)^2

For our case:
= 6970860 - 3027600 + 756900 = 4700160.

But direct = 4698000. Difference = 2160.

Hmm, let me recompute. 6970860 - 3027600 = 3943260. 3943260 + 756900 = 4700160.

Direct: 4 * 435 * 2700. 435*2700 = 1174500. 4*1174500 = 4698000.

4700160 - 4698000 = 2160. 

Let me check: T^2 - sum C(a_i,2)^2 = 3027600 - 756900 = 2270700. And 2*sum_{i<j} C(a_i,2)*C(a_j,2) = 2*6*435^2 = 12*189225 = 2270700. ✓

So W = 6970860 - 2270700 = 4700160 by the "factored" formula, but direct gives 4698000.

Wait, I think I need to recheck. Let me compute directly again, very carefully.

W = sum_{i=1}^{4} C(a_i, 2) * [C(120 - a_i, 2) - sum_{j ≠ i} C(a_j, 2)]

For i=1: C(30,2) * [C(90,2) - (C(30,2) + C(30,2) + C(30,2))] = 435 * [4005 - 1305] = 435 * 2700 = 1174500.

W = 4 * 1174500 = 4698000.

Now the formula:
sum_i C(a_i,2)*C(120-a_i,2) = 4 * 435 * 4005 = 6970860.
T = 4 * 435 = 1740.
sum_i C(a_i,2)*(T - C(a_i,2)) = 4 * 435 * (1740 - 435) = 4 * 435 * 1305 = 2270700.

W = 6970860 - 2270700 = 4700160.

But direct: 4 * 435 * (4005 - 1305) = 4 * 435 * 2700 = 4698000.

And 4 * 435 * 4005 - 4 * 435 * 1305 = 4 * 435 * (4005 - 1305) = 4 * 435 * 2700 = 4698000.

But 4 * 435 * 1305 = 2270700? Let me check: 435 * 1305 = 567675. 4 * 567675 = 2270700. ✓

And 4 * 435 * 4005 = 6970860? 435 * 4005 = 1742175. 4 * 1742175 = 6968700.

Wait! 435 * 4005: 435 * 4000 = 1740000. 435 * 5 = 2175. Total = 1742175. 4 * 1742175 = 6968700.

So sum_i C(a_i,2)*C(120-a_i,2) = 6968700, not 6970860!

I made an arithmetic error. Let me redo:
W = 6968700 - 2270700 = 4698000. ✓

Great, so the formula is correct, I just made an arithmetic error. W = 4698000 for 4 cliques of 30.

Now, 4698000 > 3744000 (3 cliques of 40) > 3712800 (2 cliques of 40 + independent 40) > 3132900 (1 clique of 60 + independent 60).

So more cliques seem better! Let me try 5 cliques of 24, c=0.

C(24,2) = 276, C(96,2) = 4560.
T = 5*276 = 1380.
W = 5*276*4560 - 1380² + 5*276² 
= 5*276*4560 - 1904400 + 5*76176
= 6292800 - 1904400 + 380880
= 4773280.

Direct check: from clique i, 0-edge pairs from other 96 = C(96,2) - 4*C(24,2) = 4560 - 1104 = 3456. 276*3456 = 953856. Total = 5*953856 = 4769280.

Hmm, discrepancy again. Let me recompute.

5*276*4560 = 5*1258560 = 6292800. 
T = 1380, T² = 1904400.
sum C(a_i,2)² = 5*276² = 5*76176 = 380880.
W = 6292800 - 1904400 + 380880 = 4769280. ✓ (I made an error before: 6292800 - 1904400 = 4388400, + 380880 = 4769280.)

Direct: 276 * 3456 = 953856. 5 * 953856 = 4769280. ✓

So 5 cliques of 24: W = 4769280 > 4698000.

Let me try 6 cliques of 20, c=0.
C(20,2) = 190, C(100,2) = 4950.
T = 6*190 = 1140.
W = 6*190*4950 - 1140² + 6*190²
= 6*190*4950 - 1299600 + 6*36100
= 5643000 - 1299600 + 216600
= 4560000.

Direct: 0-edge pairs from other 100 = 4950 - 5*190 = 4950 - 950 = 4000. 190*4000 = 760000. 6*760000 = 4560000. ✓

So 6 cliques of 20: W = 4560000 < 4769280. So 5 cliques was better than 6.

Let me try non-equal cliques. Maybe the optimal isn't equal-sized cliques.

Let me go back and think about this more generally. We have k cliques of sizes a_1, ..., a_k (and possibly an independent set of size c = 120 - sum a_i), no inter-group edges.

W = sum_i C(a_i, 2) * [C(120 - a_i, 2) - (T - C(a_i, 2))]

where T = sum_i C(a_i, 2).

= sum_i C(a_i,2) * [C(120-a_i,2) - T + C(a_i,2)]

Let me think about this as a function of the clique sizes. Let me denote e_i = C(a_i, 2) = a_i(a_i-1)/2 (the number of edges in clique i). And let n_i = a_i (size of clique i).

W = sum_i e_i * [C(120-n_i, 2) - T + e_i]

= sum_i e_i * C(120-n_i, 2) - T² + sum_i e_i²

This is a complex optimization. Let me think about it differently.

Actually, let me consider the general problem. We have a graph G that is a disjoint union of cliques (a "cluster graph"). The weak quartets are 4-sets with exactly 1 edge.

For a cluster graph with cliques of sizes a_1, ..., a_k (sum = 120):

W = sum_i C(a_i, 2) * [C(120 - a_i, 2) - sum_{j≠i} C(a_j, 2)]

Let me think about what happens when we have many small cliques. If all cliques have size 2 (just edges, a matching), then k=60, a_i=2, C(2,2)=1, T=60.

W = sum_i 1 * [C(118, 2) - 59] = 60 * [6973 - 59] = 60 * 6914 = 414840.

That's much less than the clique+independent case. So very small cliques are bad.

If all cliques have size 3, k=40, C(3,2)=3, T=120.
W = 40 * 3 * [C(117,2) - 117] = 120 * [6786 - 117] = 120 * 6669 = 800280.

Still less. Size 4: k=30, C(4,2)=6, T=180.
W = 30 * 6 * [C(116,2) - 174] = 180 * [6670 - 174] = 180 * 6496 = 1169280.

Size 5: k=24, C(5,2)=10, T=240.
W = 24 * 10 * [C(115,2) - 230] = 240 * [6555 - 230] = 240 * 6325 = 1518000.

Size 6: k=20, C(6,2)=15, T=300.
W = 20 * 15 * [C(114,2) - 285] = 300 * [6441 - 285] = 300 * 6156 = 1846800.

Size 8: k=15, C(8,2)=28, T=420.
W = 15 * 28 * [C(112,2) - 392] = 420 * [6216 - 392] = 420 * 5824 = 2446080.

Size 10: k=12, C(10,2)=45, T=540.
W = 12 * 45 * [C(110,2) - 495] = 540 * [5995 - 495] = 540 * 5500 = 2970000.

Size 12: k=10, C(12,2)=66, T=660.
W = 10 * 66 * [C(108,2) - 594] = 660 * [5778 - 594] = 660 * 5184 = 3421440.

Size 15: k=8, C(15,2)=105, T=840.
W = 8 * 105 * [C(105,2) - 735] = 840 * [5460 - 735] = 840 * 4725 = 3969000.

Size 20: k=6, W = 4560000 (computed above).
Size 24: k=5, W = 4769280.
Size 30: k=4, W = 4698000.
Size 40: k=3, W = 3744000.
Size 60: k=2, W = 3132900... wait no, k=2 with a=60,b=60: 

Actually wait, k=2 with a_1=a_2=60: C(60,2)=1770, T=3540.
W = 2 * 1770 * [C(60,2) - 1770] = 3540 * [1770 - 1770] = 0.

That's 0! Because with 2 cliques of 60, a 4-set with 2 from each clique has 2 edges, and any other distribution has 0 or 6 edges. So no weak quartets.

OK so the pattern is: W increases as clique size decreases from 60 to about 24, then decreases again. The maximum among equal-sized cliques is around size 24 (k=5), giving 4769280.

But maybe unequal cliques do better. Let me think about this.

Let me consider the general optimization. We want to maximize:

W = sum_i e_i * [C(120-n_i, 2) - T + e_i]

where e_i = n_i(n_i-1)/2, T = sum e_i.

Let me think about this as follows. For a cluster graph, let me think about what 4-sets give exactly 1 edge. We need 2 vertices from one clique (giving 1 edge) and 2 vertices from outside that clique, with the 2 outside vertices not being in the same clique (so they don't form an edge).

So W = sum_i C(n_i, 2) * [number of ways to pick 2 vertices from outside clique i, not in the same clique]

= sum_i C(n_i, 2) * [C(120-n_i, 2) - sum_{j≠i} C(n_j, 2)]

The "2 vertices from outside, not in same clique" = total pairs from outside - pairs that are in the same clique = C(120-n_i, 2) - sum_{j≠i} C(n_j, 2).

Now, let me think about the continuous relaxation. Let n_i be continuous variables summing to 120. We want to maximize W.

This is a complex combinatorial optimization. Let me try some non-equal configurations.

Let me try k=5 with sizes (30, 30, 20, 20, 20), sum=120.
e: 435, 435, 190, 190, 190. T = 1440.
For i with n_i=30: C(90,2) - (435+190+190+190) = 4005 - 1005 = 3000. Contribution: 435*3000 = 1305000. Two such: 2610000.
For i with n_i=20: C(100,2) - (435+435+190+190) = 4950 - 1250 = 3700. Contribution: 190*3700 = 703000. Three such: 2109000.
W = 2610000 + 2109000 = 4719000.

Less than 4769280 (equal 24s). 

Let me try (25, 25, 25, 25, 20), sum=120.
e: 300, 300, 300, 300, 190. T = 1390.
For n_i=25: C(95,2) - (300+300+300+190) = 4465 - 1090 = 3375. Contribution: 300*3375 = 1012500. Four: 4050000.
For n_i=20: C(100,2) - 4*300 = 4950 - 1200 = 3750. Contribution: 190*3750 = 712500.
W = 4050000 + 712500 = 4762500.

Close to 4769280 but slightly less.

Let me try (24, 24, 24, 24, 24): W = 4769280.

Let me try (25, 25, 25, 25, 20) vs (24, 24, 24, 24, 24). The equal one is better.

Let me try k=4 with (30, 30, 30, 30): W = 4698000.
k=4 with (28, 28, 32, 32): 
e: 378, 378, 496, 496. T = 1748.
For n_i=28: C(92,2) - (378+496+496) = 4186 - 1370 = 2816. Contribution: 378*2816 = 1064208. Two: 2128416.
For n_i=32: C(88,2) - (378+378+496) = 3828 - 1252 = 2576. Contribution: 496*2576 = 1277696. Two: 2555392.
W = 2128416 + 2555392 = 4683808. Less than 4698000.

So equal seems best for fixed k. Let me try to find the optimal k with equal cliques.

For k equal cliques of size n = 120/k (assuming k | 120):
e = n(n-1)/2, T = k*e.
W = k * e * [C(120-n, 2) - (k-1)*e]
= k * e * [C(120-n, 2) - (k-1)*e]

Let me compute for various k (divisors of 120: 1,2,3,4,5,6,8,10,12,15,20,24,30,40,60,120):

k=1: n=120, e=7140, T=7140. W = 1*7140*[C(0,2)-0] = 0. (No weak quartets since everything is one clique.)
k=2: n=60, e=1770. W = 2*1770*[C(60,2)-1770] = 3540*0 = 0.
k=3: n=40, e=780. W = 3*780*[C(80,2)-2*780] = 2340*[3160-1560] = 2340*1600 = 3744000.
k=4: n=30, e=435. W = 4*435*[C(90,2)-3*435] = 1740*[4005-1305] = 1740*2700 = 4698000.
k=5: n=24, e=276. W = 5*276*[C(96,2)-4*276] = 1380*[4560-1104] = 1380*3456 = 4769280.
k=6: n=20, e=190. W = 6*190*[C(100,2)-5*190] = 1140*[4950-950] = 1140*4000 = 4560000.
k=8: n=15, e=105. W = 8*105*[C(105,2)-7*105] = 840*[5460-735] = 840*4725 = 3969000.
k=10: n=12, e=66. W = 10*66*[C(108,2)-9*66] = 660*[5778-594] = 660*5184 = 3421440.
k=12: n=10, e=45. W = 12*45*[C(110,2)-11*45] = 540*[5995-495] = 540*5500 = 2970000.
k=15: n=8, e=28. W = 15*28*[C(112,2)-14*28] = 420*[6216-392] = 420*5824 = 2446080.
k=20: n=6, e=15. W = 20*15*[C(114,2)-19*15] = 300*[6441-285] = 300*6156 = 1846800.
k=24: n=5, e=10. W = 24*10*[C(115,2)-23*10] = 240*[6555-230] = 240*6325 = 1518000.
k=30: n=4, e=6. W = 30*6*[C(116,2)-29*6] = 180*[6670-174] = 180*6496 = 1169280.
k=40: n=3, e=3. W = 40*3*[C(117,2)-39*3] = 120*[6786-117] = 120*6669 = 800280.
k=60: n=2, e=1. W = 60*1*[C(118,2)-59*1] = 60*[6973-59] = 60*6914 = 414840.
k=120: n=1, e=0. W = 0.

So the maximum among equal cliques is at k=5, W = 4769280.

But we should also check non-divisor k values and non-equal cliques. Let me try k=5 with slightly unequal sizes.

Let me try k=5 with sizes (25, 25, 24, 23, 23), sum=120.
e: 300, 300, 276, 253, 253. T = 1382.
For n=25: C(95,2) - (300+276+253+253) = 4465 - 1082 = 3383. Contribution: 300*3383 = 1014900. Two: 2029800.
For n=24: C(96,2) - (300+300+253+253) = 4560 - 1106 = 3454. Contribution: 276*3454 = 953304.
For n=23: C(97,2) - (300+300+276+253) = 4656 - 1129 = 3527. Contribution: 253*3527 = 892331. Two: 1784662.
W = 2029800 + 953304 + 1784662 = 4767766.

Slightly less than 4769280.

Let me try (25, 24, 24, 24, 23), sum=120.
e: 300, 276, 276, 276, 253. T = 1381.
For n=25: C(95,2) - (276+276+276+253) = 4465 - 1081 = 3384. Contribution: 300*3384 = 1015200.
For n=24: C(96,2) - (300+276+276+253) = 4560 - 1105 = 3455. Contribution: 276*3455 = 953580. Three: 2860740.
For n=23: C(97,2) - (300+276+276+276) = 4656 - 1128 = 3528. Contribution: 253*3528 = 892584.
W = 1015200 + 2860740 + 892584 = 4768524.

Still less than 4769280.

So equal cliques of size 24 (k=5) seems optimal among cluster graphs. But is the cluster graph the optimal structure?

Let me think about whether a non-cluster graph could do better. 

Actually, let me think about this more carefully. The cluster graph (disjoint union of cliques) might not be optimal. Let me consider other structures.

Let me think about the problem from a different angle. Let me consider the general graph and try to establish an upper bound.

Let me use the edge-centric count again:
W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

where S_{ab} = common non-neighbors of a and b (excluding a,b), |S_{ab}| = 120 - d(a) - d(b) + |N(a) ∩ N(b)|.

For a cluster graph with cliques of sizes n_1, ..., n_k:
- For an edge (a,b) within clique i: d(a) = d(b) = n_i - 1, |N(a) ∩ N(b)| = n_i - 2 (other vertices in clique i).
- |S_{ab}| = 120 - 2(n_i-1) + (n_i-2) = 120 - n_i.
- e(S_{ab}) = sum_{j≠i} C(n_j, 2) (edges in other cliques; S_{ab} consists of all vertices outside clique i).
- C(|S_{ab}|, 2) - e(S_{ab}) = C(120-n_i, 2) - sum_{j≠i} C(n_j, 2). ✓

So W = sum_i C(n_i, 2) * [C(120-n_i, 2) - sum_{j≠i} C(n_j, 2)]. ✓

Now, could a non-cluster graph do better? Let me think about what structure maximizes W.

Intuitively, we want:
1. Many edges (each edge contributes to W).
2. For each edge (a,b), many common non-neighbors (large S_{ab}).
3. Few edges within S_{ab}.

These are in tension: more edges means smaller S_{ab} and more edges within S_{ab}.

The cluster graph is a natural candidate because:
- Edges are concentrated within cliques (many edges).
- For an edge within a clique, S_{ab} = all vertices outside the clique, which is large if the clique is small.
- But edges within S_{ab} = edges in other cliques, which is also significant.

Let me think about whether we can do better by having some non-cluster structure.

Consider modifying the cluster graph: take the optimal cluster graph (5 cliques of 24) and try to add or remove edges to improve W.

If we remove an edge from a clique: we lose the contribution of that edge to W, but we might increase S_{ab} for other edges. Let's see.

Remove edge (a,b) from clique 1 (size 24). Now a and b are no longer adjacent. 

Effect on W:
1. We lose the weak quartets that had (a,b) as the unique edge. Previously: C(96,2) - 4*C(24,2) = 4560 - 1104 = 3456. So we lose 3456 weak quartets.

2. For other edges (c,d) in clique 1: S_{cd} previously included a and b (they were outside clique 1... no, a and b are in clique 1, so they're not in S_{cd} which is outside clique 1). Wait, S_{cd} for edge (c,d) in clique 1 = all vertices outside clique 1 = 96 vertices. Removing edge (a,b) doesn't change S_{cd} for edges in clique 1 (since a,b are in clique 1, not in S_{cd}).

But wait, a and b are in clique 1. For edge (c,d) in clique 1, S_{cd} = vertices not adjacent to c and not adjacent to d, excluding c,d. In the cluster graph, c is adjacent to all of clique 1 (including a,b), so a,b ∉ S_{cd}. After removing edge (a,b), a is still adjacent to c (edge (a,c) still exists in clique 1), so a ∉ S_{cd} still. So S_{cd} is unchanged.

3. For edges (c,d) in other cliques: S_{cd} = vertices outside clique of c,d. a and b are in clique 1, which is outside the clique of c,d. Previously, a and b were in S_{cd} (they're not adjacent to c or d since they're in a different clique). After removing edge (a,b), a and b are still not adjacent to c or d, so they're still in S_{cd}. But now a and b are not adjacent to each other, so the pair {a,b} no longer contributes an edge within S_{cd}. So e(S_{cd}) decreases by 1 (the edge (a,b) is removed from S_{cd}).

So for each edge in other cliques, the contribution increases by 1 (since e(S_{cd}) decreases by 1, so C(|S_{cd}|,2) - e(S_{cd}) increases by 1).

Number of edges in other cliques = 4 * C(24,2) = 4 * 276 = 1104.

So gain from step 3: 1104.
Loss from step 1: 3456.
Net: 1104 - 3456 = -2352. Worse.

What if we add an edge between two cliques? Say add edge (a, x) where a ∈ clique 1, x ∈ clique 2.

Effect:
1. New edge (a,x) contributes: S_{ax} = vertices not adjacent to a and not adjacent to x, excluding a,x. 
   - a is adjacent to: all of clique 1 except a (23 vertices), and now x.
   - x is adjacent to: all of clique 2 except x (23 vertices), and now a.
   - Common non-neighbors of a and x (excl. a,x): vertices not in clique 1, not in clique 2, and not a or x. = 120 - 24 - 24 = 72 vertices (cliques 3,4,5).
   - |S_{ax}| = 72.
   - e(S_{ax}) = 3*C(24,2) = 828.
   - Contribution: C(72,2) - 828 = 2556 - 828 = 1728.

2. For edges (a,b) in clique 1 (b ≠ x, b ∈ clique 1): S_{ab} previously = 96 vertices (outside clique 1). Now x is adjacent to a, so x ∉ S_{ab}. So |S_{ab}| decreases by 1 (from 96 to 95). Also, e(S_{ab}) changes: previously S_{ab} included x and all edges involving x in clique 2 (23 edges). Now x is removed from S_{ab}, so those 23 edges are gone from S_{ab}. But also, the new edge (a,x) doesn't affect e(S_{ab}) since a ∉ S_{ab}.

Wait, let me reconsider. S_{ab} for edge (a,b) in clique 1: vertices not adjacent to a and not adjacent to b, excluding a,b. 

Before adding edge (a,x): a is adjacent to clique 1 \ {a} (23 vertices). b is adjacent to clique 1 \ {b} (23 vertices). So S_{ab} = all vertices except clique 1 = 96 vertices. e(S_{ab}) = sum of edges in cliques 2-5 = 4*276 = 1104.

After adding edge (a,x): a is now also adjacent to x. So S_{ab} = all vertices except clique 1, except x = 95 vertices. e(S_{ab}) = edges in cliques 2-5 minus edges involving x in clique 2 = 1104 - 23 = 1081. (x had 23 edges in clique 2, all removed from S_{ab}.)

New contribution of edge (a,b): C(95,2) - 1081 = 4465 - 1081 = 3384.
Old contribution: C(96,2) - 1104 = 4560 - 1104 = 3456.
Change: 3384 - 3456 = -72.

There are 23 such edges (a,b) with b ∈ clique 1, b ≠ a. Total change: 23 * (-72) = -1656.

3. For edges (x,y) in clique 2 (y ≠ a, y ∈ clique 2): similarly, S_{xy} loses a (since a is now adjacent to x). |S_{xy}| goes from 96 to 95, e(S_{xy}) goes from 1104 to 1104 - 23 = 1081.
Change per edge: C(95,2) - 1081 - (C(96,2) - 1104) = 3384 - 3456 = -72.
23 such edges. Total: 23 * (-72) = -1656.

4. For edges in cliques 3, 4, 5: S doesn't change (a and x are still in S, and they're still not adjacent to vertices in cliques 3,4,5). But now a and x ARE adjacent (new edge), so e(S) increases by 1 for each such edge's S.

Wait, for edge (c,d) in clique 3: S_{cd} = vertices outside clique 3 = 96 vertices (cliques 1,2,4,5). After adding edge (a,x), a and x are now adjacent, and both are in S_{cd} (they're in cliques 1 and 2, outside clique 3). So e(S_{cd}) increases by 1.

Change per edge: -1. Number of edges in cliques 3,4,5: 3*276 = 828. Total: 828 * (-1) = -828.

5. For edges (a,b) in clique 1 where we also need to check: does the new edge (a,x) create any new edges within S_{ab}? a ∉ S_{ab}, so no.

Total change: +1728 (new edge) - 1656 (clique 1 edges) - 1656 (clique 2 edges) - 828 (cliques 3,4,5 edges) = 1728 - 4140 = -2412. Worse.

So adding edges between cliques makes things worse. This suggests the cluster graph is locally optimal.

Let me also check: what about non-cluster graphs that aren't close to cluster graphs?

Actually, let me think about this problem more carefully. Let me consider the possibility that the optimal graph is not a cluster graph.

Let me think about an upper bound. 

W = sum over edges (a,b) of [C(|S_{ab}|, 2) - e(S_{ab})]

≤ sum over edges (a,b) of C(|S_{ab}|, 2)

= sum over edges (a,b) of C(120 - d(a) - d(b) + |N(a) ∩ N(b)|, 2)

This is hard to bound directly. Let me think about a different approach.

Actually, let me think about the problem from the perspective of 4-sets. There are C(120, 4) total 4-sets. Each 4-set has between 0 and 6 edges. We want to maximize the number with exactly 1 edge.

Let X_i = number of 4-sets with exactly i edges. We want to maximize X_1.

We have:
sum X_i = C(120, 4)
sum i*X_i = sum over 4-sets of (number of edges) = C(118, 2) * |E| (each edge is in C(118, 2) 4-sets)
sum C(i, 2) * X_i = sum over 4-sets of C(edges, 2) = sum over pairs of edges of (number of 4-sets containing both)

This gives us moment constraints but the optimization is still complex.

Let me try a different approach. Let me think about whether we can prove the cluster graph with 5 cliques of 24 is optimal, or find something better.

Actually, let me try a different type of construction. What about a "complete multipartite" type structure or a graph with a specific degree sequence?

Hmm, let me try to think about this more carefully using the formula.

For a cluster graph with k equal cliques of size n = 120/k:

W = k * C(n, 2) * [C(120-n, 2) - (k-1)*C(n, 2)]

Let me write this in terms of n (with k = 120/n):

W = (120/n) * n(n-1)/2 * [(120-n)(119-n)/2 - (120/n - 1)*n(n-1)/2]

= 60(n-1) * [(120-n)(119-n)/2 - (120-n)(n-1)/2]

= 60(n-1) * (120-n)/2 * [(119-n) - (n-1)]

= 60(n-1) * (120-n)/2 * (120-2n)

= 60(n-1)(120-n)(120-2n)/2

= 30(n-1)(120-n)(120-2n)

Wait, this requires k = 120/n to be an integer. Let me verify:

For n=24, k=5: W = 30*23*96*72 = 30*23*6912 = 30*158976 = 4769280. ✓
For n=30, k=4: W = 30*29*90*60 = 30*29*5400 = 30*156600 = 4698000. ✓
For n=20, k=6: W = 30*19*100*80 = 30*19*8000 = 30*152000 = 4560000. ✓

So W(n) = 30(n-1)(120-n)(120-2n) for equal cliques.

Let me find the maximum of f(n) = (n-1)(120-n)(120-2n) for real n.

f(n) = (n-1)(120-n)(120-2n)

Let me expand: Let u = n-1, so n = u+1.
f = u(119-u)(118-2u)

Let me take derivative with respect to u:
f(u) = u(119-u)(118-2u) = u[119*118 - 238u - 118u + 2u²] = u[14042 - 356u + 2u²]
= 14042u - 356u² + 2u³

f'(u) = 14042 - 712u + 6u²

Setting f'(u) = 0: 6u² - 712u + 14042 = 0
u = (712 ± sqrt(712² - 4*6*14042)) / (2*6) = (712 ± sqrt(506944 - 337008)) / 12 = (712 ± sqrt(169936)) / 12

sqrt(169936) ≈ 412.2

u = (712 ± 412.2) / 12

u₁ = (712 + 412.2)/12 = 1124.2/12 ≈ 93.7 → n ≈ 94.7 (but then 120-2n < 0, not valid)
u₂ = (712 - 412.2)/12 = 299.8/12 ≈ 24.98 → n ≈ 25.98

So the optimal n ≈ 26. Since we need k = 120/n to be an integer, let's check n=24 (k=5) and n=30 (k=4), and also non-integer k.

Actually, we don't need k to be an integer if we allow unequal cliques! Let me think about this.

If we have k cliques of approximately equal size n ≈ 26, with k ≈ 120/26 ≈ 4.6, we could try 4 cliques of 26 and 1 clique of 16 (sum = 120).

Let me compute: cliques of sizes 26, 26, 26, 26, 16.
e: 325, 325, 325, 325, 120. T = 1420.

For n=26: C(94,2) - (325+325+325+120) = 4371 - 1095 = 3276. Contribution: 325*3276 = 1064700. Four: 4258800.
For n=16: C(104,2) - 4*325 = 5356 - 1300 = 4056. Contribution: 120*4056 = 486720.
W = 4258800 + 486720 = 4745520.

Less than 4769280. Hmm.

Let me try 5 cliques of sizes 26, 26, 26, 26, 16 but that's what I just did. Let me try 5 cliques of 24 (the best so far) vs other 5-clique configurations.

Actually, the continuous optimum is at n ≈ 26, but with 5 cliques, 5*26 = 130 > 120, so we can't have 5 cliques of 26. With 4 cliques of 26 and 1 of 16, we get 4745520 < 4769280.

Let me try 4 cliques of 25 and 1 of 20: sum = 120.
e: 300, 300, 300, 300, 190. T = 1390.
For n=25: C(95,2) - (300+300+300+190) = 4465 - 1090 = 3375. Contribution: 300*3375 = 1012500. Four: 4050000.
For n=20: C(100,2) - 4*300 = 4950 - 1200 = 3750. Contribution: 190*3750 = 712500.
W = 4050000 + 712500 = 4762500. (Computed before, less than 4769280.)

Let me try 5 cliques of sizes 25, 25, 24, 23, 23: computed before, 4767766.

Let me try 5 cliques of 24, 24, 24, 24, 24: 4769280.

Let me try 5 cliques of 25, 25, 25, 23, 22: sum = 120.
e: 300, 300, 300, 253, 231. T = 1384.
For n=25: C(95,2) - (300+300+253+231) = 4465 - 1084 = 3381. Contribution: 300*3381 = 1014300. Three: 3042900.
For n=23: C(97,2) - (300+300+300+231) = 4656 - 1131 = 3525. Contribution: 253*3525 = 891825.
For n=22: C(98,2) - (300+300+300+253) = 4753 - 1153 = 3600. Contribution: 231*3600 = 831600.
W = 3042900 + 891825 + 831600 = 4766325.

Less than 4769280.

It really seems like 5 equal cliques of 24 is the best cluster graph. Let me also check 4 cliques and 6 cliques with unequal sizes to be thorough.

4 cliques: optimal equal is 30 each, W=4698000. Let me try 4 cliques of 28, 28, 32, 32: computed before, 4683808. Worse.

Let me try 4 cliques of 26, 26, 34, 34: 
e: 325, 325, 561, 561. T = 1772.
For n=26: C(94,2) - (325+561+561) = 4371 - 1447 = 2924. Contribution: 325*2924 = 950300. Two: 1900600.
For n=34: C(86,2) - (325+325+561) = 3655 - 1211 = 2444. Contribution: 561*2444 = 1371084. Two: 2742168.
W = 1900600 + 2742168 = 4642768. Worse.

6 cliques: optimal equal is 20 each, W=4560000. Let me try 6 cliques of 22, 22, 22, 18, 18, 18:
e: 231, 231, 231, 153, 153, 153. T = 1152.
For n=22: C(98,2) - (231+231+153+153+153) = 4753 - 921 = 3832. Contribution: 231*3832 = 885192. Three: 2655576.
For n=18: C(102,2) - (231+231+231+153+153) = 5151 - 999 = 4152. Contribution: 153*4152 = 635256. Three: 1905768.
W = 2655576 + 1905768 = 4561344. Slightly better than 4560000 but still way less than 4769280.

So the best cluster graph is 5 cliques of 24, W = 4769280.

Now, the key question: is the cluster graph optimal, or can some other graph structure do better?

Let me think about this more carefully. Let me consider a graph that's not a disjoint union of cliques.

Consider a "blow-up" of a path or cycle. Or consider a graph where we have a clique and the rest is not independent but has some structure.

Actually, let me think about the problem differently. Let me consider the complement graph $\bar{G}$. A weak quartet in G (exactly 1 edge in G) corresponds to a 4-set with exactly 5 edges in $\bar{G}$, i.e., a 4-set that induces
