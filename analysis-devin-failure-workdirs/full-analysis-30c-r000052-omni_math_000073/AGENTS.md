# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   In a sports league, each team uses a set of at most $t$ signature colors. A set $S$ of teams is\textit{ color-identifiable} if one can assign each team in $S$ one of their signature colors, such that no team in $S$ is assigned any signature color of a different team in $S$.

For all positive integers $n$ and $t$, determine the maximum integer $g(n, t)$ such that: In any sports league with exactly $n$ distinct colors present over all teams, one can always find a color-identifiable set of size at least $g(n, t)$.       — 题目文本
#   
In a sports league, each team uses a set of at most \( t \) signature colors. A set \( S \) of teams is color-identifiable if one can assign each team in \( S \) one of their signature colors, such that no team in \( S \) is assigned any signature color of a different team in \( S \).

For all positive integers \( n \) and \( t \), we aim to determine the maximum integer \( g(n, t) \) such that in any sports league with exactly \( n \) distinct colors present over all teams, one can always find a color-identifiable set of size at least \( g(n, t) \).

The answer is \( \lceil \frac{n}{t} \rceil \).

To show that the answer cannot be higher, consider the following construction: let team 1 have colors \( 1, 2, 3, \ldots, t \), team 2 have colors \( t+1, t+2, \ldots, 2t \), and so on. Team \( k \) will have colors \( (k-1)t + 1, (k-1)t + 2, \ldots, \min(kt, n) \). This construction results in \( \lceil \frac{n}{t} \rceil \) teams, so \( g(n, t) \leq \lceil \frac{n}{t} \rceil \).

To prove that \( g(n, t) \geq \lceil \frac{n}{t} \rceil \), construct a function \( f(i) \) that maps each color \( i \) to a team such that team \( f(i) \) has \( i \) as a signature color. This function must exist because each color is the signature color of some team. Let \( S \) be the set of teams equal to \( f(i) \) for some \( i \). Construct a bipartite graph with teams in \( S \) as left vertices and colors as right vertices.

There are clearly at least \( n \) edges, one for each color. Since each left vertex (team) has degree at most \( t \), there are at least \( \lceil \frac{n}{t} \rceil \) teams in this set. Furthermore, because \( f \) is surjective from colors to teams, Hall's Marriage Theorem applies, ensuring a perfect matching exists.

Thus, the maximum integer \( g(n, t) \) is:
\[
\boxed{\lceil \frac{n}{t} \rceil}
\]  — 标准解答
#   Let me solve this problem. We have a simple graph with 100 vertices. For each vertex u, there exists a vertex v in N(u) such that N(u) ∩ N(v) = ∅. We need to find the maximum number of edges.

Let me think about this carefully.

The condition: for each vertex u, there exists a neighbor v of u such that N(u) ∩ N(v) = ∅.

Note: N(u) is the open neighborhood. So N(u) ∩ N(v) = ∅ means u and v have no common neighbors. Since v ∈ N(u), we have u ∈ N(v). So u ∈ N(u)? No, u is not in N(u) (open neighborhood). 

Let me reconsider. N(u) is the set of neighbors of u. v ∈ N(u) means v is a neighbor of u. N(u) ∩ N(v) = ∅ means u and v share no common neighbor.

Note that v ∈ N(u) and u ∈ N(v). Is v ∈ N(v)? No (no loops). Is u ∈ N(u)? No. So u ∈ N(v) but u ∉ N(u), and v ∈ N(u) but v ∉ N(v). So the condition N(u) ∩ N(v) = ∅ is about common neighbors other than themselves.

So for each vertex u, there's a neighbor v such that no vertex is adjacent to both u and v. This means the edge uv is not part of any triangle, and moreover, no vertex is adjacent to both endpoints.

This is related to the concept where each vertex has a "private" neighbor with no common neighbors.

Let me think about what structures maximize edges.

Consider a complete bipartite graph K_{50,50}. Each vertex u on one side has all 50 vertices on the other side as neighbors. For any neighbor v, N(u) ∩ N(v) = (other side) ∩ (this side) = ∅. Wait, N(u) = other side (50 vertices), N(v) = this side (50 vertices). So N(u) ∩ N(v) = ∅. Yes! So K_{50,50} satisfies the condition. It has 50*50 = 2500 edges.

Can we do better? Let me think about whether we can add edges within a part.

Actually, let me think more generally. The condition is that each vertex has a neighbor with no common neighbors. 

Let me think about an upper bound. 

Consider the graph. For each vertex u, pick a "witness" neighbor f(u) = v such that N(u) ∩ N(v) = ∅.

Let me think about this differently. Let's consider the structure.

If N(u) ∩ N(v) = ∅ for an edge uv, then deg(u) + deg(v) ≤ n = 100 (since N(u) and N(v) are disjoint subsets of V, and note u ∈ N(v), v ∈ N(u), but u ∉ N(u), v ∉ N(v), so |N(u)| + |N(v)| = deg(u) + deg(v) ≤ 100... wait, N(u) and N(v) are disjoint, and they're subsets of V. N(u) contains v, N(v) contains u. Since N(u) ∩ N(v) = ∅, and both are subsets of the 100 vertices, we have deg(u) + deg(v) ≤ 100.

So for each vertex u, there's a neighbor v with deg(u) + deg(v) ≤ 100.

Now, let's think about maximizing edges. Let d_u = deg(u). The number of edges is (1/2)Σd_u.

We want to maximize Σd_u subject to: for each u, there exists v ∈ N(u) with d_u + d_v ≤ 100.

Hmm, this is a constraint but it's not immediately giving a tight bound.

Let me think about the K_{50,50} example more. Each vertex has degree 50. For each u, any neighbor v has d_u + d_v = 100 ≤ 100. ✓. Total edges = 2500.

Can we beat 2500? Let's try adding an edge within one part of K_{50,50}. Say we add edge between a1, a2 (both in part A). Now a1 has degree 51, a2 has degree 51. 

For a1: we need a neighbor v with N(a1) ∩ N(v) = ∅. a1's neighbors are all 50 vertices in B plus a2. Consider v = a2: N(a1) = B ∪ {a2}, N(a2) = B ∪ {a1}. N(a1) ∩ N(a2) = B, which is not empty. Consider v ∈ B: N(a1) = B ∪ {a2}, N(v) = A (all of A, since v is connected to all of A). N(a1) ∩ N(v) = (B ∪ {a2}) ∩ A = {a2} (since a2 ∈ A). Not empty. So a1 has no valid witness. The condition fails.

So we can't just add edges to K_{50,50}.

Let me think about other constructions. What about a disjoint union of K_{50,50} and some other structure? No, we need exactly 100 vertices.

What about a complete bipartite graph with unequal parts? K_{a,b} with a+b=100. Each vertex in part A (size a) has degree b, each in part B has degree a. For u in A, v in B: d_u + d_v = b + a = 100. ✓. Edges = ab, maximized at a=b=50, giving 2500.

What about non-bipartite constructions? Let me think...

Consider a graph that's a union of cliques. If we have a clique of size k, each vertex has degree k-1 within the clique. For any two vertices u,v in the clique, N(u) ∩ N(v) contains all other k-2 vertices. So if k ≥ 3, no two vertices in the clique have disjoint neighborhoods. If k = 2, it's just an edge, and N(u) ∩ N(v) = ∅ (since they only have each other as neighbors, and u ∉ N(u), v ∉ N(v)). So a matching (disjoint edges) works but gives only 50 edges.

What about combining structures? Let me think about a graph where some vertices have high degree and some have low degree.

Let me consider the following: partition vertices into groups. Within the constraint, try to maximize edges.

Actually, let me think about this more carefully with the degree constraint.

For each u, there exists v ∈ N(u) with d_u + d_v ≤ 100.

Let's order vertices by degree: d_1 ≥ d_2 ≥ ... ≥ d_100.

Consider the vertex with maximum degree, d_1. It has a witness v with d_1 + d_v ≤ 100, so d_v ≤ 100 - d_1.

Now, I want to maximize Σd_i / 2.

Let me think about an upper bound. Consider the witness function f. For each u, f(u) is a neighbor with d_u + d_{f(u)} ≤ 100.

Hmm, but the witness relationship isn't necessarily symmetric or a function in a nice way.

Let me try a different approach. Let me think about what the extremal graph looks like.

Claim: The answer is 2500, achieved by K_{50,50}.

Let me try to prove an upper bound of 2500.

Approach: Let's think about it. For each vertex u, let f(u) be a witness neighbor (N(u) ∩ N(f(u)) = ∅). 

Consider the edges. Each edge uv where v = f(u) contributes to the constraint d_u + d_v ≤ 100.

Hmm, let me think about this differently. 

Let me consider the set of "witness edges" E' = {u f(u) : u ∈ V}. Note that f(u) might not satisfy f(f(u)) = u, so E' is a set of directed edges, but as undirected edges, |E'| could be less than 100.

Actually, let me think about it as: we have a set of edges S (one per vertex, but possibly with repeats) such that for each edge uv in S, d_u + d_v ≤ 100.

Let me try a cleaner approach. 

For each vertex u, choose witness f(u). Consider the sum:
Σ_u (d_u + d_{f(u)}) ≤ 100 · 100 = 10000.

But Σ_u d_{f(u)} is not simply related to Σ d_u because f might not be injective.

Hmm. Let me think differently.

Alternative approach: Let's use the constraint more cleverly.

For each vertex u with degree d_u, there exists a neighbor v with d_v ≤ 100 - d_u. 

Let's partition vertices into "high" (d > 50) and "low" (d ≤ 50). 

If u is high (d_u > 50), then its witness v has d_v < 50, so v is low. Also, v is a neighbor of u.

If u is low (d_u ≤ 50), its witness could be anything with d ≤ 100 - d_u ≥ 50.

Let H = {u : d_u > 50} and L = {u : d_u ≤ 50}. Let |H| = h, |L| = l, h + l = 100.

Each vertex in H must have a neighbor in L (its witness). 

Now, Σ d_u = Σ_{H} d_u + Σ_{L} d_u.

Σ_{L} d_u ≤ 50 · l.

For Σ_{H} d_u: each u ∈ H has d_u ≤ 100 - d_{f(u)} where f(u) ∈ L. 

Hmm, this is getting complicated. Let me think about whether 2500 is actually optimal or if we can do better.

Let me try a construction that might beat 2500.

Consider: Take K_{50,50} (parts A, B). Now, remove some edges and add others to try to increase the total.

Actually, let me think about a different construction. What if we have a graph that's "almost" complete bipartite but with some modifications?

Let me try: Partition into A (size a) and B (size b), a + b = 100. Make it complete bipartite. Then, within A, add a matching (or some edges). 

If we add an edge a1a2 within A, then a1 and a2 now have degree b+1. Their neighborhoods include all of B plus each other. For a1 to have a witness, we need a neighbor v with N(a1) ∩ N(v) = ∅. 

- v ∈ B: N(v) = A (all of A). N(a1) = B ∪ {a2}. N(a1) ∩ N(v) = (B ∪ {a2}) ∩ A = {a2} ≠ ∅. Fails.
- v = a2: N(a2) = B ∪ {a1}. N(a1) ∩ N(a2) = B ≠ ∅. Fails.

So adding any edge within A breaks the condition for the endpoints. Unless we also remove some edges.

What if we remove the edge a1-b1 for some b1? Then a1's neighborhood is (B \ {b1}) ∪ {a2}, degree b. And b1's neighborhood is A \ {a1}, degree a-1.

For a1, witness v = a2: N(a1) = (B\{b1}) ∪ {a2}, N(a2) = B ∪ {a1}. Intersection = B\{b1} ≠ ∅. Still fails.

This is hard to modify. Let me think about completely different constructions.

What about a graph consisting of disjoint complete bipartite graphs? E.g., K_{a1,b1} ∪ K_{a2,b2} ∪ ... with Σ(ai + bi) = 100. Total edges = Σ ai·bi. This is maximized with a single K_{50,50} giving 2500. Splitting reduces the product sum. So disjoint union doesn't help.

What about a graph that's not bipartite? Let me think about odd cycles or other structures.

Consider C5 (5-cycle). Each vertex has degree 2. For vertex u, its neighbors are the two adjacent vertices. N(u) = {two neighbors}. For neighbor v of u, N(v) = {u, v's other neighbor}. N(u) ∩ N(v): u's neighbors are {v, w} where w is u's other neighbor. v's neighbors are {u, x} where x is v's other neighbor. N(u) ∩ N(v) = {v,w} ∩ {u,x}. Since it's a 5-cycle, w ≠ x (as long as the cycle has length ≥ 5). Actually in C5, let vertices be 0,1,2,3,4. N(0) = {1,4}. N(1) = {0,2}. N(0) ∩ N(1) = {1,4} ∩ {0,2} = ∅. ✓. So C5 works, each vertex has 2 edges, 5 vertices, 5 edges. Not great.

Let me think about whether we can have a graph with more than 2500 edges.

Consider a graph on 100 vertices where we try to make degrees as high as possible while satisfying the constraint.

The constraint is: for each u, ∃ v ∈ N(u) with d_u + d_v ≤ 100.

If all degrees are exactly 50, then for each u, any neighbor v works (50+50=100). This is K_{50,50} (or any 50-regular graph where each edge has the property... but actually we need N(u) ∩ N(v) = ∅, not just d_u + d_v ≤ 100).

Wait, I need to be more careful. The condition is N(u) ∩ N(v) = ∅, which implies d_u + d_v ≤ 100, but the converse isn't true. So the degree constraint is necessary but not sufficient.

But for the upper bound, the degree constraint d_u + d_v ≤ 100 (for the witness) is what we can use.

So let me work with: for each u, ∃ v ∈ N(u) with d_u + d_v ≤ 100.

Can we have Σd_u > 5000 (i.e., more than 2500 edges) under this constraint?

Let me try: suppose we have 50 vertices with degree 60 and 50 vertices with degree 40. Σd = 50·60 + 50·40 = 3000 + 2000 = 5000. Edges = 2500. Same.

What about 50 vertices with degree 70 and 50 with degree 30? Σd = 3500 + 1500 = 5000. Same.

What about 40 vertices with degree 80 and 60 with degree 20? Σd = 3200 + 1200 = 4400. Less.

What about 60 vertices with degree 60 and 40 with degree 40? Σd = 3600 + 1600 = 5200. Edges = 2600 > 2500!

But wait, can this actually be realized as a graph satisfying the original condition? Let me check. Each of the 60 high-degree vertices (degree 60) needs a witness with degree ≤ 40. So each high vertex needs at least one neighbor among the low vertices. Each of the 40 low-degree vertices (degree 40) needs a witness with degree ≤ 60, which could be any neighbor.

But we also need the actual neighborhood disjointness condition, not just the degree sum. Let me think about whether such a graph can exist.

Actually, let me first check if the degree-sum constraint alone allows Σd > 5000.

For each u, ∃ v ∈ N(u) with d_u + d_v ≤ 100.

Let H = {u : d_u > 50}, L = {u : d_u ≤ 50}.

Each u ∈ H needs a neighbor in L (since d_u > 50 means d_v < 50 < d_u, so d_v ≤ 100 - d_u < 50, meaning v ∈ L).

Each u ∈ L needs a neighbor v with d_v ≤ 100 - d_u. If d_u ≤ 50, then 100 - d_u ≥ 50, so v could be in H or L.

Now, let's think about the sum. We want to maximize Σd_u.

Let me try to construct a graph with Σd > 5000.

Take h vertices with degree d_H and l = 100 - h vertices with degree d_L, where d_H > 50 and d_L < 50, and h·d_H + l·d_L is maximized.

Constraint: each high vertex needs a low neighbor. Also, the graph must be realizable (degree sequence must be graphical, and the neighborhood condition must hold).

But even just from the degree constraint, let's see: if we have h high vertices each with degree d_H, they need at least one low neighbor each. The low vertices have total degree l·d_L. The edges between H and L are at most l·d_L (since each low vertex has degree d_L, all of which could go to H). We need at least h edges from H to L (one per high vertex). So l·d_L ≥ h, which is easily satisfied.

But we also need: the high vertices have degree d_H, and they need their witness to be a low vertex with disjoint neighborhood. 

Hmm, let me think about this more carefully with a specific construction.

Construction attempt: Let A = {a_1, ..., a_60} (high, target degree 60) and B = {b_1, ..., b_40} (low, target degree 40).

For the condition to hold, each a_i needs a neighbor b_j with N(a_i) ∩ N(b_j) = ∅.

If a_i is connected to all of B (40 edges) and 20 vertices in A, then d(a_i) = 60. 
If b_j is connected to all of A (60 edges), then d(b_j) = 60, not 40.

That doesn't work. Let me think differently.

For N(a_i) ∩ N(b_j) = ∅ where b_j is a neighbor of a_i: a_i's neighbors and b_j's neighbors are disjoint. Since a_i ∈ N(b_j) and b_j ∈ N(a_i), and these are the only "cross" elements. So N(a_i) \ {b_j} and N(b_j) \ {a_i} are disjoint. This means |N(a_i) \ {b_j}| + |N(b_j) \ {a_i}| ≤ 98 (the other 98 vertices). So (d(a_i) - 1) + (d(b_j) - 1) ≤ 98, i.e., d(a_i) + d(b_j) ≤ 100. Same as before.

But the disjointness is stronger. Let me think about a concrete construction.

Let me try: Partition into A (size 60) and B (size 40). 

Connect each a_i to all 40 vertices in B. So d(a_i) ≥ 40 from B. Add 20 more edges from a_i to other vertices in A. So d(a_i) = 60.

Connect each b_j to some vertices. If b_j is connected to all of A, d(b_j) = 60. But we want d(b_j) = 40. So b_j is connected to 40 of the 60 vertices in A. 

For a_i, witness b_j: N(a_i) = B ∪ {20 vertices in A}. N(b_j) = {40 vertices in A}. N(a_i) ∩ N(b_j) = (B ∪ S_i) ∩ T_j where S_i is the 20 A-vertices adjacent to a_i, T_j is the 40 A-vertices adjacent to b_j. Since b_j ∈ B and B ⊆ N(a_i), but b_j ∉ N(b_j). So N(a_i) ∩ N(b_j) = S_i ∩ T_j. For this to be empty, we need S_i ∩ T_j = ∅, i.e., the 20 A-neighbors of a_i are disjoint from the 40 A-neighbors of b_j. But |S_i| + |T_j| = 20 + 40 = 60 = |A|. So S_i and T_j partition A, and a_i ∉ S_i (since a_i isn't adjacent to itself). Also a_i ∈ T_j (since b_j is a neighbor of a_i, meaning a_i is a neighbor of b_j, so a_i ∈ T_j). So T_j contains a_i, and S_i is 20 vertices from A \ {a_i}, and T_j = A \ S_i (40 vertices including a_i). 

So for each a_i, we need a b_j such that:
1. b_j is a neighbor of a_i (a_i ∈ T_j, i.e., b_j is connected to a_i). Since a_i is connected to all of B, this is automatic.
2. S_i ∩ T_j = ∅, i.e., S_i ⊆ A \ T_j = S_i. Wait, that's circular. T_j = A \ S_i means S_i ∩ T_j = ∅. ✓. But we need T_j to be exactly A \ S_i, and T_j must be the neighborhood of b_j within A.

So for each a_i, there must exist b_j whose A-neighborhood is exactly A \ S_i (the complement of a_i's A-neighborhood within A).

Now, different a_i's might have different S_i's, requiring different b_j's. We have 40 b_j's and 60 a_i's. By pigeonhole, some b_j must serve as witness for multiple a_i's. If b_j serves a_i and a_k, then T_j = A \ S_i = A \ S_k, so S_i = S_k. So a_i and a_k have the same A-neighborhood S.

So we can group the a_i's by their A-neighborhood S. For each distinct S, we need at least one b_j with T_j = A \ S. 

The number of distinct S sets is at most 40 (since we have 40 b_j's). Each S has size 20, and there are 60 a_i's distributed among at most 40 groups. So at least 20 groups have 2 or more a_i's, or some other distribution. Actually, we just need at most 40 distinct S sets, and 60 a_i's can be distributed among them.

But also, each b_j has a specific T_j (its A-neighborhood), and these must be distinct if they serve different S's. Actually, multiple b_j's can have the same T_j.

Wait, but b_j also needs its own witness. b_j has degree 40 (its A-neighbors). b_j needs a neighbor v with N(b_j) ∩ N(v) = ∅. 

N(b_j) = T_j (40 vertices in A). For witness v ∈ T_j (a neighbor of b_j in A): N(v) ∩ T_j = ∅. N(v) = B ∪ S_v (since v = a_i for some i, and a_i is connected to all of B plus S_i). N(v) ∩ T_j = (B ∪ S_v) ∩ T_j = S_v ∩ T_j (since B ∩ A = ∅). We need S_v ∩ T_j = ∅, i.e., S_v ⊆ A \ T_j = S_v. Wait, T_j = A \ S_v (from our earlier requirement). So S_v ∩ T_j = S_v ∩ (A \ S_v) = ∅. ✓!

So if b_j's witness is any a_i with S_i = A \ T_j, the condition is automatically satisfied. And we set up T_j = A \ S_i, so this works.

So the construction works as follows:
- Partition A (60 vertices) into groups, each group sharing the same 20-element subset S of A as their A-neighborhood.
- For each distinct S, assign at least one b_j with T_j = A \ S (its A-neighborhood).
- Each a_i is connected to all of B (40 edges) plus its 20 A-neighbors (S_i). Total degree = 60.
- Each b_j is connected to 40 vertices in A (T_j). Total degree = 40.

Wait, but we need each b_j to have degree exactly 40, and b_j is connected only to T_j ⊆ A. So d(b_j) = |T_j| = 40. ✓.

And each a_i has degree 40 (from B) + 20 (from A) = 60. ✓.

Now, the A-edges: each a_i is connected to S_i (20 vertices in A). But these are undirected edges. If a_i is connected to a_k, then a_k is connected to a_i. So if a_i ∈ S_k, then a_k ∈ S_i. The A-edges form a graph where the neighborhoods are the S_i's.

Also, a_i ∉ S_i (no self-loops). And if a_i ∈ S_k then a_k ∈ S_i.

Let me think about the A-edges more carefully. The A-edges form a 20-regular graph on 60 vertices (each a_i has exactly 20 neighbors in A). 

Now, the number of distinct S_i's: we need at most 40 (one b_j per distinct S_i). We have 60 a_i's and 40 b_j's. So at most 40 distinct S_i's.

But actually, we need: for each distinct S, there's a b_j with T_j = A \ S. We have 40 b_j's, so at most 40 distinct S's. With 60 a_i's and at most 40 distinct S's, by pigeonhole, at least 20 a_i's share an S with another. That's fine.

But wait, we also need the b_j's to have the right T_j's. If we have k distinct S's, we need k b_j's with the corresponding T_j's. The remaining 40 - k b_j's can have any T_j (as long as they also satisfy the condition).

Actually, every b_j needs a witness too. b_j's witness is some a_i with S_i = A \ T_j. So for every b_j, A \ T_j must be the S_i of some a_i. In other words, every T_j must be the complement of some S_i.

So the set of T_j's (for j = 1..40) must be a subset of {A \ S_i : i = 1..60}. And the set of distinct S_i's must be a subset of {A \ T_j : j = 1..40}. These are equivalent: the distinct S_i's and the distinct T_j's are complementary pairs.

Let me simplify. Let the distinct S values be S^(1), S^(2), ..., S^(k). Then the distinct T values are A \ S^(1), ..., A \ S^(k). We need k ≤ 40 (since we have 40 b_j's) and k ≤ 60 (since we have 60 a_i's). Also, the 60 a_i's are distributed among k groups, and the 40 b_j's are distributed among k groups.

Now, total edges:
- B-to-A edges: Each a_i connects to all 40 b_j's. That's 60 × 40 = 2400 edges. Wait, but each b_j connects to T_j (40 vertices in A), not all 60. So the B-to-A edges are: for each b_j, |T_j| = 40 edges. Total = 40 × 40 = 1600. But also, each a_i connects to all 40 b_j's, which would be 60 × 40 = 2400. Contradiction!

I think I made an error. Let me reconsider.

If each a_i is connected to all 40 vertices in B, that's 60 × 40 = 2400 B-A edges. But each b_j is connected to only 40 of the 60 A-vertices, giving 40 × 40 = 1600 B-A edges. These must be equal (it's the same set of edges). 2400 ≠ 1600. Contradiction!

So the construction doesn't work as stated. Each a_i can't be connected to all of B if each b_j is only connected to 40 of 60 A-vertices.

Let me reconsider. If a_i is connected to all 40 b_j's, then each b_j is connected to all 60 a_i's, giving d(b_j) ≥ 60. But we wanted d(b_j) = 40. Contradiction.

So I need to revise. Let me not connect each a_i to all of B.

Revised construction: 
- A (60 vertices), B (40 vertices).
- Each a_i has degree 60: some neighbors in A, some in B.
- Each b_j has degree 40: some neighbors in A, some in B.

For a_i's witness b_j: N(a_i) ∩ N(b_j) = ∅, with d(a_i) + d(b_j) = 60 + 40 = 100. ✓ (necessary condition).

Let me try: a_i has 20 neighbors in A and 40 neighbors in B (all of B). Then d(a_i) = 60. b_j has 40 neighbors in A and 0 in B. Then d(b_j) = 40.

B-A edges: 60 × 40 = 2400 (each a_i to all B) vs 40 × 40 = 1600 (each b_j to 40 A-vertices). Still contradictory.

OK so the issue is that if a_i connects to all of B, then b_j connects to all of A. Let me think about this differently.

Let me try: a_i has x neighbors in A and (60 - x) neighbors in B. b_j has y neighbors in A and (40 - y) neighbors in B.

B-A edges: 60(60-x) = 40·y (counting from each side). So 60(60-x) = 40y, i.e., y = (60(60-x))/40 = (3/2)(60-x).

For a_i's witness b_j (a B-neighbor): N(a_i) ∩ N(b_j) = ∅. N(a_i) = S_i (A-neighbors, size x) ∪ B_i (B-neighbors, size 60-x). N(b_j) = T_j (A-neighbors, size y) ∪ U_j (B-neighbors, size 40-y).

N(a_i) ∩ N(b_j) = (S_i ∩ T_j) ∪ (B_i ∩ U_j). For this to be ∅: S_i ∩ T_j = ∅ and B_i ∩ U_j = ∅.

b_j ∈ B_i (since b_j is a neighbor of a_i). And a_i ∈ T_j (since a_i is a neighbor of b_j). 

S_i ∩ T_j = ∅: |S_i| + |T_j| ≤ |A| = 60, so x + y ≤ 60.
B_i ∩ U_j = ∅: |B_i| + |U_j| ≤ |B| = 40, so (60-x) + (40-y) ≤ 40, i.e., 100 - x - y ≤ 40, i.e., x + y ≥ 60.

So x + y = 60 exactly. And y = (3/2)(60-x). So x + (3/2)(60-x) = 60. x + 90 - (3/2)x = 60. -(1/2)x = -30. x = 60. Then y = 0.

If x = 60, then a_i has 60 neighbors in A and 0 in B. But a_i needs a B-neighbor as witness (we said witness is in B). If a_i has no B-neighbors, it can't have a B-witness. So the witness must be an A-neighbor.

Let me reconsider. The witness doesn't have to be in B. Let me allow the witness to be in A.

If a_i's witness is a_k ∈ A: N(a_i) ∩ N(a_k) = ∅. Both a_i and a_k are in A. N(a_i) = S_i ∪ B_i, N(a_k) = S_k ∪ B_k. Need S_i ∩ S_k = ∅ and B_i ∩ B_k = ∅.

|S_i| + |S_k| ≤ 60 and |B_i| + |B_k| ≤ 40. With |S_i| = |S_k| = x and |B_i| = |B_k| = 60-x: 2x ≤ 60 and 2(60-x) ≤ 40. So x ≤ 30 and 60-x ≤ 20, i.e., x ≥ 40. Contradiction (x ≤ 30 and x ≥ 40).

So two A-vertices can't be witnesses for each other if they both have degree 60 with the same split. 

This suggests that having all vertices with degree > 50 is hard. Let me reconsider the problem.

Maybe 2500 is indeed the answer. Let me try to prove it.

Upper bound proof attempt:

For each vertex u, let f(u) be a witness neighbor (N(u) ∩ N(f(u)) = ∅). We know d(u) + d(f(u)) ≤ 100.

Consider the directed graph where each u points to f(u). Each vertex has out-degree 1. The underlying undirected graph has some edges.

Let me think about it differently. Consider the sum:
S = Σ_u d(u) = 2|E|.

We want to show S ≤ 5000, i.e., |E| ≤ 2500.

For each u, d(u) + d(f(u)) ≤ 100. Summing over all u:
Σ_u d(u) + Σ_u d(f(u)) ≤ 10000.

Now, Σ_u d(f(u)) = Σ_v d(v) · |f^{-1}(v)| where |f^{-1}(v)| is the number of u with f(u) = v.

So S + Σ_v d(v) · |f^{-1}(v)| ≤ 10000.

If we could show that Σ_v d(v) · |f^{-1}(v)| ≥ S, then 2S ≤ 10000, S ≤ 5000, |E| ≤ 2500.

Is Σ_v d(v) · |f^{-1}(v)| ≥ Σ_v d(v)? This is equivalent to Σ_v d(v)(|f^{-1}(v)| - 1) ≥ 0, which isn't obviously true.

Hmm. Let me think about this differently.

Actually, let me think about a cleaner approach. 

Key insight: For each vertex u, there's an edge uv (where v = f(u)) such that N(u) ∩ N(v) = ∅. This means uv is an edge and no vertex is adjacent to both u and v. In other words, uv is not contained in any triangle, and moreover, there's no path u-w-v for any w (i.e., no vertex w adjacent to both u and v).

Such an edge is called a "free edge" or an edge with no common neighbors. 

Let me think about the problem from the perspective of the complement graph or some other transformation.

Alternative approach: Let's think about it in terms of the adjacency matrix.

Actually, let me try another approach. Consider the following:

For each vertex u, choose witness f(u). The edge {u, f(u)} has the property that N(u) ∩ N(f(u)) = ∅.

Now, consider the set of witness edges W = {{u, f(u)} : u ∈ V}. Note |W| ≤ 100 (could be less if multiple u's share the same witness edge).

For each witness edge e = {u,v} ∈ W, we have d(u) + d(v) ≤ 100.

Now, I want to bound Σd(u). 

Let me think about which vertices are "covered" by witness edges. Every vertex u is an endpoint of its witness edge {u, f(u)}. So every vertex is covered by at least one witness edge (its own).

Consider the witness edges as a (multi)set of edges. Group vertices by which witness edge covers them. Actually, each vertex u is covered by at least the edge {u, f(u)}.

Let me try a different tactic. Consider the graph G. For each vertex u, let v = f(u). The edge uv has d(u) + d(v) ≤ 100.

Now, consider the edges of G. Each edge xy of G contributes to the degrees of x and y. 

Let me think about it as follows. For each vertex u, we have d(u) + d(f(u)) ≤ 100. Let's write this as d(u) ≤ 100 - d(f(u)).

Sum: Σ d(u) ≤ Σ (100 - d(f(u))) = 10000 - Σ d(f(u)).

So Σ d(u) + Σ d(f(u)) ≤ 10000.

Now, Σ d(f(u)) = Σ_v d(v) · c(v) where c(v) = |{u : f(u) = v}| = in-degree of v in the witness digraph.

Note that Σ c(v) = 100 (each u contributes 1). Also, c(v) ≥ 0.

We have S + Σ_v d(v) c(v) ≤ 10000 where S = Σ d(v).

We want to show S ≤ 5000. This requires Σ d(v) c(v) ≥ S = Σ d(v), i.e., Σ d(v)(c(v) - 1) ≥ 0.

This isn't always true. For example, if high-degree vertices have c(v) = 0 and low-degree vertices have c(v) = 2, then Σ d(v)(c(v)-1) could be negative.

So this approach doesn't directly work. Let me think more.

Let me try a completely different approach.

Approach via induction or via considering the structure.

Actually, let me think about the problem more carefully. Let me consider what happens when we have a vertex of very high degree.

If u has degree d(u), its witness v has d(v) ≤ 100 - d(u). Also, v is a neighbor of u, and N(u) ∩ N(v) = ∅. The d(u) - 1 other neighbors of u (besides v) are all not neighbors of v. And the d(v) - 1 other neighbors of v (besides u) are all not neighbors of u.

So the d(u) - 1 + d(v) - 1 = d(u) + d(v) - 2 ≤ 98 vertices (other neighbors of u and v) are all distinct and are in V \ {u, v}.

Now, let me think about a charging argument or a more clever bound.

Let me try to think about the problem computationally. Let me consider small cases first.

For n vertices (instead of 100), what's the maximum number of edges?

n = 2: One edge. K_2. Each vertex has the other as witness, N(u) ∩ N(v) = ∅. 1 edge. ⌊n²/4⌋ = 1. ✓.

n = 3: K_{1,2} (star). Center has degree 2, leaves have degree 1. For center u, witness v (a leaf): N(u) = {v, w}, N(v) = {u}. N(u) ∩ N(v) = ∅? N(u) = {v, w}, N(v) = {u}. Intersection = ∅. ✓. For leaf v, witness u: N(v) = {u}, N(u) = {v, w}. Intersection = ∅. ✓. For leaf w, witness u: same. ✓. So K_{1,2} works with 2 edges. ⌊9/4⌋ = 2. Can we do 3 edges (K_3)? In K_3, each vertex has degree 2, N(u) = {other two}. N(u) ∩ N(v) = {third vertex} ≠ ∅. So K_3 doesn't work. Max = 2 = ⌊n²/4⌋.

n = 4: K_{2,2} has 4 edges. Each vertex degree 2. N(u) ∩ N(v) = ∅ for any edge uv (since it's bipartite). ✓. Can we do 5 edges? K_4 has 6 edges, K_4 minus one edge has 5. In K_4 - e, say missing edge is {3,4}. Degrees: d(1)=d(2)=3, d(3)=d(4)=2. For vertex 1: N(1) = {2,3,4}. Witness v: N(1) ∩ N(v) = ∅. v=2: N(2)={1,3,4}. N(1)∩N(2) = {3,4} ≠ ∅. v=3: N(3)={1,2}. N(1)∩N(3) = {2} ≠ ∅. v=4: N(4)={1,2}. N(1)∩N(4) = {2} ≠ ∅. So vertex 1 has no witness. Fails. Max = 4 = ⌊16/4⌋.

n = 5: K_{2,3} has 6 edges. ⌊25/4⌋ = 6. Can we do 7? Let me check. Total possible edges = 10. We need to remove at least 3. Hmm, let me think... Actually, let me just conjecture the answer is ⌊n²/4⌋ = 2500 for n = 100.

Let me try to prove that the maximum is ⌊n²/4⌋.

Proof approach: Show that |E(G)| ≤ ⌊n²/4⌋ for any graph G on n vertices satisfying the condition.

This is the same as the Turán-type bound for triangle-free graphs (Mantel's theorem). But our condition is different (stronger in some ways, weaker in others).

Actually, our condition doesn't require the graph to be triangle-free. A graph could have triangles as long as each vertex has at least one "private" neighbor.

Wait, but can a graph with triangles satisfy our condition? Let me think of an example.

Take K_{2,3} (bipartite, 6 edges, 5 vertices) and add an edge within the part of size 2. Now we have 7 edges. The two vertices in the size-2 part are now adjacent. Let's call them a1, a2 and b1, b2, b3.

Edges: a1-b1, a1-b2, a1-b3, a2-b1, a2-b2, a2-b3, a1-a2. 7 edges.

d(a1) = 4, d(a2) = 4, d(b_i) = 2.

For a1: N(a1) = {a2, b1, b2, b3}. Witness? 
- v = a2: N(a2) = {a1, b1, b2, b3}. N(a1) ∩ N(a2) = {b1, b2, b3} ≠ ∅. Fails.
- v = b1: N(b1) = {a1, a2}. N(a1) ∩ N(b1) = {a2} ≠ ∅. Fails.
- v = b2: similar, {a2} ≠ ∅. Fails.
- v = b3: similar. Fails.

So a1 has no witness. The condition fails. So adding an edge within a part of K_{2,3} breaks the condition.

What about a different graph with triangles? Let me think...

Take C_5 plus a chord. C_5 = 0-1-2-3-4-0. Add chord 0-2. Now:
d(0) = 3, d(1) = 2, d(2) = 3, d(3) = 2, d(4) = 2.
N(0) = {1, 2, 4}, N(1) = {0, 2}, N(2) = {0, 1, 3}, N(3) = {2, 4}, N(4) = {0, 3}.

For vertex 0: 
- v=1: N(0)∩N(1) = {1,2,4}∩{0,2} = {2} ≠ ∅. Fails.
- v=2: N(0)∩N(2) = {1,2,4}∩{0,1,3} = {1} ≠ ∅. Fails.
- v=4: N(0)∩N(4) = {1,2,4}∩{0,3} = ∅. ✓!

For vertex 2:
- v=0: N(2)∩N(0) = {0,1,3}∩{1,2,4} = {1} ≠ ∅. Fails.
- v=1: N(2)∩N(1) = {0,1,3}∩{0,2} = {0} ≠ ∅. Fails.
- v=3: N(2)∩N(3) = {0,1,3}∩{2,4} = ∅. ✓!

For vertex 1:
- v=0: N(1)∩N(0) = {0,2}∩{1,2,4} = {2} ≠ ∅. Fails.
- v=2: N(1)∩N(2) = {0,2}∩{0,1,3} = {0} ≠ ∅. Fails.
No witness! Fails.

So vertex 1 has no witness. The condition fails.

Hmm. It seems hard to have triangles. Let me think about whether the condition actually implies triangle-free.

If there's a triangle u-v-w, then for vertex u: is there a witness? u's neighbors include v and w. If v is u's witness, N(u) ∩ N(v) = ∅, but w ∈ N(u) ∩ N(v) (since w is adjacent to both u and v). So v can't be the witness. Similarly w can't be. So u's witness must be some other neighbor x ≠ v, w with N(u) ∩ N(x) = ∅. This is possible if u has a neighbor outside the triangle.

So triangles are allowed as long as each vertex in the triangle has another neighbor with no common neighbors.

Let me try to construct such a graph.

Take a triangle {a, b, c} and a vertex d connected only to a. And vertex e connected only to b. And vertex f connected only to c.

Edges: ab, bc, ac, ad, be, cf. 6 edges, 6 vertices.

d(a) = 3 (b, c, d), d(b) = 3 (a, c, e), d(c) = 3 (a, b, f), d(d) = 1, d(e) = 1, d(f) = 1.

For a: N(a) = {b, c, d}. 
- v = d: N(d) = {a}. N(a) ∩ N(d) = ∅. ✓.

For b: N(b) = {a, c, e}.
- v = e: N(e) = {b}. N(b) ∩ N(e) = ∅. ✓.

For c: N(c) = {a, b, f}.
- v = f: N(f) = {c}. N(c) ∩ N(f) = ∅. ✓.

For d: N(d) = {a}.
- v = a: N(a) = {b, c, d}. N(d) ∩ N(a) = ∅. ✓.

For e: N(e) = {b}.
- v = b: N(b) = {a, c, e}. N(e) ∩ N(b) = ∅. ✓.

For f: N(f) = {c}.
- v = c: N(c) = {a, b, f}. N(f) ∩ N(c) = ∅. ✓.

So this graph with a triangle works! It has 6 edges on 6 vertices. ⌊36/4⌋ = 9. So it's well below the Mantel bound. But it shows triangles are possible.

Can we do better? Let me try to add more edges. 

Take the above and add more connections. Add vertex g connected to d, and vertex h connected to e, etc. This creates a tree-like structure hanging off the triangle. Not great for edge count.

Let me think about this more carefully. The condition allows triangles but requires each vertex to have a "private" neighbor. 

Let me think about the problem differently. Let me consider the following approach:

For each vertex u, let f(u) = v be its witness. Consider the "witness matching" — can we extract a matching from the witness edges?

Actually, let me think about a key structural observation.

Observation: If uv is a witness edge (N(u) ∩ N(v) = ∅), then in the graph, the edge uv is "isolated" in the sense that no other edge shares both endpoints' neighborhoods. 

Let me try a different approach to the upper bound.

Approach: Consider the witness function f. For each u, f(u) is a neighbor with N(u) ∩ N(f(u)) = ∅.

Define a new graph H on V where we connect u to f(u). H is a graph (or multigraph) where each vertex has at least one incident edge (its witness edge). 

The connected components of H are... well, each vertex has out-degree 1 in the directed version. So the structure is a functional graph (each weakly connected component has exactly one cycle).

Hmm, this is getting complicated. Let me try yet another approach.

Approach: Let's try to prove |E| ≤ n²/4 by a direct counting argument.

For each edge e = uv, define w(e) = d(u) + d(v). We know that for each vertex u, there's an incident edge e = u f(u) with w(e) ≤ n.

But other edges might have w(e) > n.

Hmm, let me think about the problem from the perspective of the adjacency matrix and the condition.

The condition N(u) ∩ N(v) = ∅ for edge uv means: for all w ≠ u, v, w is not adjacent to both u and v. In adjacency matrix terms, if A is the adjacency matrix, then (A²)_{uv} = |N(u) ∩ N(v)| = 0 for the witness edge uv. (Since u and v are adjacent, (A²)_{uv} counts the number of common neighbors, which is 0.)

Actually, (A²)_{uv} = Σ_w A_{uw} A_{wv} = |N(u) ∩ N(v)| when u ≠ v. For the witness edge, this is 0.

So the condition is: for each vertex u, there exists v with A_{uv} = 1 and (A²)_{uv} = 0.

This means: for each u, there's a neighbor v such that the edge uv is not in any triangle.

Now, let me think about this. The number of triangles containing edge uv is (A²)_{uv} (when A_{uv} = 1). The condition says each vertex is incident to at least one edge that's in no triangle.

Let T be the set of "triangle-free edges" (edges not in any triangle). The condition says every vertex is incident to at least one edge in T.

So T is an edge cover of the vertices. The minimum size of an edge cover in a graph with n vertices and no isolated vertices is ⌈n/2⌉ (it's a matching plus some extra edges). But T could be larger.

Now, the edges not in T are edges that are in at least one triangle. Let's call these "triangle edges."

Hmm, I'm not sure this directly helps with the bound.

Let me try to think about it from the perspective of the following:

Claim: For any graph satisfying the condition, |E| ≤ ⌊n²/4⌋.

Let me try to prove this by induction on n.

Base case: n = 1, 2, trivial.

Inductive step: Consider a graph G on n vertices satisfying the condition. Pick a vertex u of minimum degree δ. Let v = f(u) be its witness. 

d(u) + d(v) ≤ n. Since d(u) = δ is minimum, d(v) ≥ δ, so 2δ ≤ d(u) + d(v) ≤ n, giving δ ≤ n/2.

Now, remove u and v from G. The remaining graph G' has n - 2 vertices. Does G' satisfy the condition?

Not necessarily. A vertex w in G' might have had u or v as its only witness. So we can't directly apply induction.

Let me think differently.

Actually, let me think about whether the answer might not be 2500. Let me try to construct a graph with more than 2500 edges that satisfies the condition.

Construction idea: Take a complete bipartite graph K_{50,50} and modify it.

Actually, let me think about a different type of construction. What if the graph has a more complex structure?

Consider the following: partition the 100 vertices into groups A_1, A_2, ..., A_k and B_1, B_2, ..., B_k. Connect A_i to B_j for certain pairs (i,j). 

Actually, let me think about a blow-up construction.

Take a "template" graph H on k vertices that satisfies the condition. Replace each vertex i with an independent set of size n_i (Σn_i = 100). Replace each edge ij of H with a complete bipartite graph between the corresponding sets. 

For a vertex u in group i, its neighbors are all vertices in groups j where ij is an edge of H. The neighborhood N(u) is the union of groups j adjacent to i in H. For a witness, u needs a neighbor v in some group j (where ij ∈ E(H)) such that N(u) ∩ N(v) = ∅. N(u) = ∪_{i~k} group_k, N(v) = ∪_{j~k} group_k. N(u) ∩ N(v) = ∪_{k: i~k and j~k} group_k. For this to be ∅, we need no k adjacent to both i and j in H. So ij must be an edge of H with no common neighbor in H. And this must hold for every vertex i in H (each vertex i has a neighbor j in H with N_H(i) ∩ N_H(j) = ∅).

So the template H must also satisfy the condition! And the blow-up preserves the condition.

The number of edges in the blow-up is Σ_{ij ∈ E(H)} n_i · n_j.

To maximize this, we want H to satisfy the condition and the n_i's to be chosen to maximize Σ n_i n_j over edges of H.

If H = K_2 (two vertices, one edge), then the blow-up is K_{a,b} with a + b = 100, and edges = ab ≤ 2500.

If H is a path P_3 (3 vertices, 2 edges: 1-2, 2-3), the blow-up has edges n_1·n_2 + n_2·n_3 = n_2(n_1 + n_3). With n_1 + n_2 + n_3 = 100, this is n_2(100 - n_2), maximized at n_2 = 50, giving 2500. Same.

If H = K_{2,2} (4 vertices, 4 edges), the blow-up has edges n_1·n_3 + n_1·n_4 + n_2·n_3 + n_2·n_4 = (n_1+n_2)(n_3+n_4). With sum 100, maximized at (n_1+n_2) = (n_3+n_4) = 50, giving 2500. Same.

If H = C_5 (5 vertices, 5 edges), the blow-up has edges Σ n_i n_{i+1} (mod 5). By AM-GM or convexity, this is maximized when... it's a quadratic form. For C_5, the maximum of Σ n_i n_{i+1} subject to Σ n_i = 100 is achieved when all n_i = 20, giving 5 · 20 · 20 = 2000. Less than 2500.

If H = K_{a,b} (complete bipartite), the blow-up is also complete bipartite (merging the groups), giving at most 2500.

What if H has more edges? Like H = K_{2,3} (6 edges). Blow-up edges = (n_1+n_2)(n_3+n_4+n_5) ≤ 2500. Same.

It seems like for any bipartite H, the blow-up gives at most 2500 (since it reduces to a complete bipartite graph).

What about non-bipartite H? We showed earlier that a triangle with pendant vertices works. Let's try H = triangle + pendant vertices.

H: vertices 1,2,3 (triangle) + 4 (connected to 1) + 5 (connected to 2) + 6 (connected to 3). 6 vertices, 6 edges. 

Blow-up edges = n_1n_2 + n_1n_3 + n_2n_3 + n_1n_4 + n_2n_5 + n_3n_6.

With Σn_i = 100. Let's optimize. This is a quadratic form. Let me think...

Actually, the blow-up might not give more than 2500 for any template. Let me think about why.

For any graph H satisfying the condition, the blow-up with optimal group sizes gives at most ⌊n²/4⌋ edges. Is this true?

Hmm, consider H with many edges. The blow-up edges are Σ_{ij ∈ E(H)} n_i n_j. This is (1/2) n^T A_H n where A_H is the adjacency matrix of H. The maximum of n^T A_H n subject to Σn_i = n is related to the largest eigenvalue of A_H.

For H = K_2, λ_max = 1, and the max is n²/2 · 1 = n²/2... wait, (1/2) n^T A n with the optimal n. For K_2, A = [[0,1],[1,0]], λ_max = 1. The optimal n is (n/2, n/2), giving (1/2)(n/2)²·2 = n²/4. So edges = n²/4.

For H with λ_max > 1, we might get more. For example, H = K_3 has λ_max = 2. But K_3 doesn't satisfy the condition (as we showed). 

What about H = C_5? λ_max = 2cos(π/5) ≈ 1.618. The blow-up gives (1/2) n² λ_max / k... no, let me be more careful.

The maximum of n^T A n subject to 1^T n = N (where N = 100) is N² λ_max / k if we use the eigenvector... no. The maximum of n^T A n subject to 1^T n = N, n ≥ 0 is N² · (max of x^T A x subject to 1^T x = 1, x ≥ 0). 

For the Perron eigenvector (which is positive for connected graphs), x = v/Σv_i where v is the Perron eigenvector. Then x^T A x = λ_max / (Σv_i)² · v^T v... hmm, this isn't clean.

Actually, the maximum of n^T A n subject to 1^T n = N is N² λ_max if the Perron eigenvector is proportional to 1 (i.e., the graph is regular). For a d-regular graph, λ_max = d, and the optimal is all n_i = N/k, giving n^T A n = (N/k)² · dk = N²d/k. Edges = (1/2)N²d/k = N²d/(2k) = N² · (average degree) / (2k) · k... wait.

For a d-regular graph on k vertices, edges of H = dk/2. Blow-up with all groups size N/k: edges = (N/k)² · dk/2 = N²d/(2k). For this to exceed N²/4, we need d/k > 1/2, i.e., d > k/2, i.e., the graph has more than k²/4 edges, i.e., more than the Mantel bound. But if H satisfies the condition and has more than k²/4 edges, then by induction (or by our conjecture), this is impossible. So if the conjecture holds for H, the blow-up can't exceed N²/4.

But this is circular. Let me think about it differently.

Actually, the blow-up construction might not be the only way to build graphs satisfying the condition. There might be non-blow-up graphs that do better. But from the small cases and the difficulty of beating 2500, I believe the answer is 2500.

Let me try to prove the upper bound directly.

Proof of upper bound:

For each vertex u, let f(u) be a witness neighbor. We have N(u) ∩ N(f(u)) = ∅, hence d(u) + d(f(u)) ≤ n.

Let S = {u ∈ V : d(u) ≤ n/2} (small vertices) and L = {u ∈ V : d(u) > n/2} (large vertices).

For u ∈ L, d(u) > n/2, so d(f(u)) < n/2, meaning f(u) ∈ S. So every large vertex has its witness in S, and in particular, every large vertex has a neighbor in S.

Now, let's count edges. Let e_LL, e_LS, e_SS be the number of edges within L, between L and S, and within S.

|E| = e_LL + e_LS + e_SS.

We have:
- Σ_{u ∈ L} d(u) = 2e_LL + e_LS
- Σ_{u ∈ S} d(u) = 2e_SS + e_LS

Total: Σd(u) = 2(e_LL + e_LS + e_SS) = 2|E|.

Now, for each u ∈ L, d(u) ≤ n - d(f(u)) where f(u) ∈ S. 

Hmm, this is still not giving a clean bound. Let me try another approach.

Let me try the approach of considering the witness edges as a matching-like structure.

For each u, let f(u) be the witness. Consider the multiset of witness edges {u, f(u)}. 

Key idea: Let's find a large matching in the witness edges.

Actually, let me try a direct approach. Let me use the following lemma:

Lemma: If for every vertex u, there's a neighbor v with d(u) + d(v) ≤ n, then |E| ≤ n²/4.

Wait, is this lemma true? Let me check with a potential counterexample.

Consider n = 6. Take K_4 on vertices {1,2,3,4} and connect vertex 5 to vertex 1, vertex 6 to vertex 2. 

d(1) = 4, d(2) = 4, d(3) = 3, d(4) = 3, d(5) = 1, d(6) = 1.

For vertex 1: d(1) = 4. Need neighbor v with d(v) ≤ 2. Neighbors: 2 (d=4), 3 (d=3), 4 (d=3), 5 (d=1). v = 5: d(1) + d(5) = 5 ≤ 6. ✓.
For vertex 2: v = 6, d(2) + d(6) = 5 ≤ 6. ✓.
For vertex 3: d(3) = 3. Need d(v) ≤ 3. v = 1 (d=4, no), v = 2 (d=4, no), v = 4 (d=3, 3+3=6 ≤ 6). ✓.
For vertex 4: v = 3, 3+3=6. ✓.
For vertex 5: v = 1, 1+4=5 ≤ 6. ✓.
For vertex 6: v = 2, 1+4=5 ≤ 6. ✓.

So the degree condition is satisfied. |E| = 6 + 2 = 8. n²/4 = 9. So 8 ≤ 9. ✓.

But does the original condition (N(u) ∩ N(v) = ∅) hold? Let me check.

For vertex 3, witness v = 4: N(3) = {1, 2, 4}, N(4) = {1, 2, 3}. N(3) ∩ N(4) = {1, 2} ≠ ∅. Fails!

So the degree condition is necessary but not sufficient. The original condition is stronger. Good, so the lemma (if true) would give an upper bound, but we need to check if the lemma is actually true.

Let me check: is the lemma "if for every vertex u, there's a neighbor v with d(u) + d(v) ≤ n, then |E| ≤ n²/4" true?

Consider n = 4, K_4 minus one edge. d = (3, 3, 2, 2). For vertex 1 (d=3): need neighbor with d ≤ 1. Neighbors: 2 (d=3), 3 (d=2), 4 (d=2). None has d ≤ 1. So the condition fails. |E| = 5, n²/4 = 4. But the condition doesn't hold, so no contradiction.

Let me try to find a graph where the degree condition holds but |E| > n²/4.

n = 4: n²/4 = 4. Max edges with degree condition: we need each vertex to have a neighbor with degree sum ≤ 4. With 5 edges (K_4 - e), degrees (3,3,2,2), vertex 1 needs neighbor with d ≤ 1, but all neighbors have d ≥ 2. Fails. With 4 edges, e.g., K_{2,2}, degrees all 2, 2+2=4. ✓. |E| = 4 = n²/4.

n = 6: n²/4 = 9. Can we have 10 edges with the degree condition? 10 edges on 6 vertices means average degree 20/6 ≈ 3.33. 

Let me try: degrees (4, 4, 4, 3, 3, 2). Sum = 20, edges = 10. 
Vertex with d=4 needs neighbor with d ≤ 2. Only vertex with d=2. So the d=2 vertex must be adjacent to all three d=4 vertices. But d=2 vertex has only 2 neighbors. Can't be adjacent to 3 vertices. Contradiction. So this degree sequence doesn't work.

Try degrees (4, 4, 3, 3, 3, 3). Sum = 20, edges = 10.
d=4 vertices need neighbor with d ≤ 2. But all other vertices have d ≥ 3. Fails.

Try degrees (5, 3, 3, 3, 3, 3). Sum = 20, edges = 10.
d=5 vertex needs neighbor with d ≤ 1. All neighbors have d ≥ 3. Fails.

Try degrees (4, 4, 4, 4, 2, 2). Sum = 20, edges = 10.
d=4 vertices need neighbor with d ≤ 2. The two d=2 vertices. Each d=4 vertex must be adjacent to at least one d=2 vertex. Two d=2 vertices can be adjacent to at most 4 other vertices total (each has 2 neighbors). So at most 4 of the d=4 vertices can be adjacent to a d=2 vertex. We have 4 d=4 vertices, so each must be adjacent to exactly one d=2 vertex, and the d=2 vertices are adjacent to 2 d=4 vertices each.

Now, the d=2 vertices: each is adjacent to 2 of the 4 d=4 vertices. The d=4 vertices: each is adjacent to 1 d=2 vertex and 3 other d=4 vertices (since d=4, and 1 neighbor is d=2, so 3 more from the other 3 d=4 vertices). So the d=4 vertices form K_4 (each adjacent to all 3 others). 

So the graph is K_4 on {1,2,3,4} plus vertex 5 adjacent to two of {1,2,3,4} and vertex 6 adjacent to two of {1,2,3,4}.

d=2 vertices (5, 6): each needs a neighbor with d ≤ 4. Any neighbor works (d=4, 2+4=6=n). ✓.

d=4 vertices: each needs a neighbor with d ≤ 2. Each is adjacent to one of {5, 6}. ✓.

So the degree condition holds! |E| = 10 > 9 = n²/4.

But does the original condition hold? Let me check with a specific graph.

K_4 on {1,2,3,4}. Vertex 5 adjacent to {1, 2}. Vertex 6 adjacent to {3, 4}.

d(1) = 4 (neighbors: 2, 3, 4, 5). d(2) = 4 (1, 3, 4, 5). d(3) = 4 (1, 2, 4, 6). d(4) = 4 (1, 2, 3, 6). d(5) = 2 (1, 2). d(6) = 2 (3, 4).

For vertex 1: witness v = 5. N(1) = {2, 3, 4, 5}. N(5) = {1, 2}. N(1) ∩ N(5) = {2} ≠ ∅. Fails!

So the original condition fails, even though the degree condition holds. Good, this confirms the original condition is strictly stronger.

So the lemma about the degree condition is FALSE (the degree condition allows |E| > n²/4), but the original condition might still imply |E| ≤ n²/4.

Let me now try to prove the upper bound for the original condition.

Let me think about this more carefully.

For each vertex u, let f(u) be a witness. N(u) ∩ N(f(u)) = ∅.

Key observation: The witness edges form a set of edges where each edge uv has the property that no other vertex is adjacent to both u and v. 

Let me think about the structure of the graph more carefully.

Consider the witness digraph: u → f(u). Each vertex has out-degree 1. 

Let me think about what happens with a vertex u and its witness v = f(u). The edge uv has no common neighbors. So in the graph, removing all edges incident to u or v, the remaining graph on V \ {u, v} has some structure.

Actually, let me try a proof by induction.

Theorem: For a graph G on n vertices satisfying the condition, |E(G)| ≤ ⌊n²/4⌋.

Proof by strong induction on n.

Base cases: n ≤ 2, trivial.

Inductive step: Assume the result for all graphs on fewer than n vertices.

Case 1: There exists a vertex u with d(u) ≤ n/2.

Remove u. The remaining graph G' on n-1 vertices may not satisfy the condition (some vertex might have lost its only witness). 

Hmm, this doesn't work directly. Let me think differently.

Case 2: All vertices have degree > n/2. Then for any u, d(u) > n/2, so d(f(u)) < n/2. Contradiction. So there must exist a vertex with degree ≤ n/2.

Wait, that's not right. If all vertices have degree > n/2, then for each u, d(f(u)) > n/2, so d(u) + d(f(u)) > n. But we need d(u) + d(f(u)) ≤ n. Contradiction. So there must exist a vertex with degree ≤ n/2.

OK so there's always a vertex u with d(u) ≤ n/2. But removing it doesn't preserve the condition.

Let me try a different approach. Let me remove a vertex u and its witness v = f(u).

d(u) + d(v) ≤ n. The edge uv contributes 1 to |E|. The edges incident to u or v: d(u) + d(v) - 1 (subtracting the edge uv counted twice). 

When we remove u and v, we remove d(u) + d(v) - 1 edges. The remaining graph G - {u, v} has n - 2 vertices and |E| - (d(u) + d(v) - 1) edges.

Does G - {u, v} satisfy the condition? Not necessarily. A vertex w in G - {u, v} might have had u or v as its only witness.

But maybe we can choose u and v carefully. 

Hmm, let me think about this differently. Let me try to use a weight function or a clever counting argument.

Alternative approach: Let's use the following strategy. For each edge e = xy, assign a weight. Show that the total weight is bounded.

Actually, let me try the following approach inspired by Mantel's theorem.

Mantel's theorem proof: For each edge uv, d(u) + d(v) ≤ n (in a triangle-free graph). Sum over all edges: Σ_{uv ∈ E} (d(u) + d(v)) = Σ_u d(u)² ≤ n|E|. By Cauchy-Schwarz, (Σd(u))² ≤ n Σd(u)² ≤ n · n|E| = n²|E|. So (2|E|)² ≤ n²|E|, giving 4|E|² ≤ n²|E|, |E| ≤ n²/4.

In our case, we don't have d(u) + d(v) ≤ n for all edges, only for witness edges. So we can't directly apply this.

But maybe we can use a variant. Let me think...

For each vertex u, let f(u) be its witness. We have d(u) + d(f(u)) ≤ n.

Consider the sum Σ_u d(u) · d(f(u)). Hmm, not sure.

Let me try another approach. 

Approach: Partition the vertices based on the witness structure.

For each vertex u, the witness f(u) gives an edge with no common neighbors. Let's think of the witness edges as defining a structure.

Consider the graph W = (V, {u, f(u)} : u ∈ V). W is a graph (possibly with multi-edges) where each vertex has degree ≥ 1.

In W, consider the connected components. Each component has at least 2 vertices (since each vertex has at least one witness edge).

Hmm, I'm going in circles. Let me try a more computational approach.

Let me think about what kinds of graphs can satisfy the condition and have many edges.

From the examples, K_{50,50} gives 2500 edges. The blow-up of any template graph gives at most 2500. Non-blow-up graphs seem hard to construct with more edges.

Let me try to see if there's a non-blow-up construction that beats 2500.

Consider the following: Take K_{50,50} with parts A and B. Now, within A, add a perfect matching (25 edges). This adds 25 edges, giving 2525. But we need to check the condition.

After adding matching edges in A: each a_i ∈ A now has degree 51 (50 from B + 1 from A). For a_i, witness v: 
- v ∈ B: N(a_i) = B ∪ {a_i's match in A}. N(v) = A. N(a_i) ∩ N(v) = (B ∪ {match}) ∩ A = {match} ≠ ∅. Fails.
- v = a_i's match: N(a_i) = B ∪ {match}. N(match) = B ∪ {a_i}. N(a_i) ∩ N(match) = B ≠ ∅. Fails.

So the condition fails for all a_i. We'd need to also remove some edges to compensate.

What if we remove, for each matched pair (a_i, a_j), the edge a_i - b_k for some specific b_k? 

This is getting complicated. Let me try to think about it more carefully.

Actually, let me think about the problem from the perspective of the following key lemma:

Lemma: If G satisfies the condition, then G is "almost" bipartite in some sense.

Hmm, that's vague. Let me try to think about specific structures.

Let me consider the following construction: 

Take a bipartite graph with parts A (50 vertices) and B (50 vertices). It's not complete bipartite but has some edges missing and some edges within parts.

For each a ∈ A, a has a witness b ∈ B with N(a) ∩ N(b) = ∅. This means a and b share no common neighbors. Since a's neighbors are in A ∪ B and b's neighbors are in A ∪ B, and they share none, this is a strong condition.

If the graph is bipartite (no edges within A or within B), then for any edge ab (a ∈ A, b ∈ B), N(a) ⊆ B and N(b) ⊆ A, so N(a) ∩ N(b) = ∅ automatically. So any bipartite graph satisfies the condition (as long as it has no isolated vertices, so each vertex has at least one neighbor to serve as witness).

Wait, is that right? In a bipartite graph with parts A and B, for a ∈ A, N(a) ⊆ B. For b ∈ B, N(b) ⊆ A. So N(a) ∩ N(b) ⊆ B ∩ A = ∅. Yes! So in any bipartite graph (with no isolated vertices), every edge is a witness edge. The condition is automatically satisfied.

So the condition is satisfied by any bipartite graph with minimum degree ≥ 1. The maximum edges in a bipartite graph on 100 vertices is ⌊100²/4⌋ = 2500 (by K_{50,50}).

But the condition also allows non-bipartite graphs. Can a non-bipartite graph satisfying the condition have more than 2500 edges?

From our earlier analysis, adding any edge within a part of K_{50,50} breaks the condition. But maybe a completely different non-bipartite construction works.

Let me think about this. Consider a graph that's "mostly" bipartite but with a few extra edges, and some edges removed to compensate.

Actually, let me think about whether the condition implies the graph is bipartite. We showed a triangle with pendant vertices satisfies the condition, so the graph need not be bipartite. But that graph had few edges.

Conjecture: The maximum number of edges is 2500, achieved by K_{50,50}.

Let me try to prove this. I need to show that any graph satisfying the condition has at most 2500 edges.

Approach: Let me try to show that the condition implies the graph is "close to bipartite" in a way that limits the edge count.

Key insight: In a bipartite graph, every edge is a witness edge. In a non-bipartite graph, some edges are not witness edges (they're in triangles), but every vertex still needs at least one witness edge.

Let me define: A vertex u is "satisfied" if it has a witness neighbor. The condition says all vertices are satisfied.

Let me try the following approach:

For each vertex u, let f(u) be a witness. Consider the set of witness pairs P = {(u, f(u)) : u ∈ V}. 

For each pair (u, v) with v = f(u), we have N(u) ∩ N(v) = ∅, so d(u) + d(v) ≤ n.

Now, I want to bound |E|. Let me try to use the witness pairs to partition the edges.

Hmm, let me try yet another approach. Let me think about the problem in terms of the adjacency matrix.

Let A be the adjacency matrix. The condition is: for each i, there exists j with A_{ij} = 1 and (A²)_{ij} = 0.

The number of edges is (1/2)Σ_{i,j} A_{ij} = (1/2) tr(AJ) where J is the all-ones matrix... actually, |E| = (1/2) Σ_i d(i) = (1/2) 1^T A 1.

We want to maximize 1^T A 1 / 2 subject to: for each i, ∃ j with A_{ij} = 1 and (A²)_{ij} = 0.

This is hard to work with directly. Let me go back to combinatorial arguments.

Let me try the following approach:

For each vertex u, choose a witness f(u). Define a "partner" function. Now, consider the graph G and the partner function.

For each u, the edge {u, f(u)} is triangle-free (no common neighbors). 

Let T be the set of triangle-free edges (edges not in any triangle). Every vertex is incident to at least one edge in T (its witness edge).

The edges in T form a subgraph H of G with no isolated vertices (every vertex has at least one edge in T).

Now, the edges of G \ T are all in some triangle. 

Claim: The edges in G \ T can be charged to the edges in T in a way that bounds the total.

Hmm, this is still vague. Let me try to think about it more concretely.

Actually, let me try a different approach entirely. Let me think about the problem as an optimization problem and try to use Lagrangian methods or linear programming.

Let me think about the dual problem. We want to maximize |E| = (1/2) Σ d(u) subject to: for each u, ∃ v ∈ N(u) with N(u) ∩ N(v) = ∅.

The constraint is hard to linearize. Let me think about relaxations.

Relaxation: For each u, ∃ v ∈ N(u) with d(u) + d(v) ≤ n. (This is a necessary condition.)

We showed this relaxation allows |E| > n²/4 (the K_4 + 2 pendant vertices example). So the relaxation is too weak.

Stronger relaxation: For each u, ∃ v ∈ N(u) with N(u) ∩ N(v) = ∅.

This is the actual condition, which is hard to relax further.

Let me try to think about the problem from the extremal graph theory perspective.

The condition "every vertex has a neighbor with no common neighbors" is related to the concept of "isolated edges" or "independent edges" in the neighborhood graph.

Let me think about the contrapositive: what prevents a graph from having many edges while satisfying the condition?

If a graph has many edges, it's "dense," and dense graphs tend to have many triangles. In a dense graph, most edges are in triangles, so few edges are triangle-free. The condition requires every vertex to be incident to a triangle-free edge, so we need at least n/2 triangle-free edges (forming an edge cover). 

In a graph with n²/4 + ε edges, how many triangle-free edges must there be?

By a result in extremal graph theory, a graph with more than n²/4 edges must contain a triangle (Mantel's theorem). But we need more: we need that not every edge is in a triangle.

Actually, let me think about it this way. Suppose |E| > n²/4. By Mantel's theorem, G contains a triangle. But that's fine; our condition allows triangles.

Let me think about what happens when |E| is close to n²/4 + n/2 or so.

Hmm, let me try a more direct approach. Let me try to prove the bound by considering the structure of witness edges.

Proof attempt:

For each vertex u, let f(u) be a fixed witness. We have N(u) ∩ N(f(u)) = ∅ and d(u) + d(f(u)) ≤ n.

Consider the directed graph D where u → f(u). Each vertex has out-degree 1. The components of D are functional graph components (each has a directed cycle with trees hanging off).

For each directed cycle C = (u_1 → u_2 → ... → u_k → u_1) in D, we have:
- d(u_i) + d(u_{i+1}) ≤ n for each i (since f(u_i) = u_{i+1}).

Wait, actually f(u_i) = u_{i+1} means u_{i+1} is the witness of u_i, so N(u_i) ∩ N(u_{i+1}) = ∅ and d(u_i) + d(u_{i+1}) ≤ n.

For the cycle, summing: Σ_{i=1}^k (d(u_i) + d(u_{i+1})) ≤ kn. This gives 2 Σ_{i=1}^k d(u_i) ≤ kn, so Σ d(u_i) ≤ kn/2.

For trees hanging off the cycle: if u → v where v is on the cycle or in a tree, d(u) + d(v) ≤ n.

This is getting complicated. Let me try a cleaner approach.

Let me try to use the following strategy:

1. Show that we can find a set of vertex-disjoint witness edges (a matching) that covers a large fraction of vertices.
2. Use this matching to bound the total number of edges.

Step 1: Find a matching in the witness edges.

The witness edges form a graph W on V. Each vertex has at least one incident edge in W. By a classical result, any graph with no isolated vertices has a matching of size at least n/2 - o(n)... actually, any graph without isolated vertices has a matching of size ≥ n/2 - (number of odd components)/2... hmm, that's not quite right.

Actually, a classical result says: any graph on n vertices with minimum degree ≥ 1 has a matching of size ≥ n/2 - (number of connected components that are odd cycles with pendant edges)... this is getting complicated.

Let me use a simpler result: any graph on n vertices with no isolated vertices has a matching of size ≥ n/3 (I think). Actually, the correct bound is: a maximal matching has size ≥ n/2 / Δ... no.

Let me think about it differently. A maximal matching in W has the property that every edge in W shares an endpoint with a matching edge. Since every vertex is incident to a W-edge, every vertex is either in the matching or adjacent (in W) to a matching vertex. So the matching is a vertex cover... no, the matching edges' endpoints form a vertex cover of W. So the matching covers all vertices (in the sense that every vertex is either matched or adjacent to a matched vertex in W).

Actually, a maximal matching M in W: every edge of W shares an endpoint with some edge of M. Since every vertex is incident to some edge of W, every vertex is an endpoint of some edge of W, which shares an endpoint with M. So every vertex is either in M or adjacent (in W) to a vertex in M.

Hmm, this means the endpoints of M form a dominating set in W. But I want a matching that covers many vertices.

Let me just use the fact that W has no isolated vertices, so it has a matching of size ≥ n/2 / something. Actually, the minimum maximal matching can be as small as n/3 (for a star graph, the minimum maximal matching has size 1, but n/3 for n=3 gives 1). Hmm, for a star on n vertices, the minimum maximal matching has size 1, which is much less than n/2.

OK, let me not pursue the matching approach. Let me try something else.

Let me try the following direct approach:

For each vertex u, let f(u) be a witness. We have d(u) + d(f(u)) ≤ n.

Sum over all u: Σ d(u) + Σ d(f(u)) ≤ n².

Now, Σ d(f(u)) = Σ_v d(v) · indeg(v) where indeg(v) = |{u : f(u) = v}|.

We have Σ indeg(v) = n. 

So S + Σ_v d(v) · indeg(v) ≤ n² where S = Σ d(v) = 2|E|.

We want to show S ≤ n²/2, i.e., |E| ≤ n²/4.

From the inequality: S ≤ n² - Σ_v d(v) · indeg(v).

For this to give S ≤ n²/2, we need Σ_v d(v) · indeg(v) ≥ n²/2.

By the rearrangement inequality, Σ_v d(v) · indeg(v) is minimized when the largest d(v) is paired with the smallest indeg(v). 

We know Σ indeg(v) = n and indeg(v) ≥ 0. Also, if v has indeg(v) = 0, then no u has f(u) = v, meaning v is not a witness for anyone. But v itself has f(v) = some neighbor, so v has outdeg 1.

Hmm, we can't directly lower-bound Σ d(v) · indeg(v) without more information.

Let me think about what constraints we have on indeg.

If v has high degree d(v), can it have low indeg? indeg(v) is the number of vertices u that chose v as their witness. There's no direct constraint preventing v from having indeg 0.

For example, in K_{50,50}, each vertex has degree 50. We can choose f(u) for each u to be any neighbor. If we choose all f(u) to point to the same vertex v, then indeg(v) = 100 and indeg(others) = 0. Then Σ d(v) indeg(v) = 50 · 100 = 5000 = n²/2. So S + 5000 ≤ 10000, S ≤ 5000, |E| ≤ 2500. ✓.

But if we choose f more spread out, say indeg(v) = 1 for all v, then Σ d(v) indeg(v) = Σ d(v) = S. So S + S ≤ n², S ≤ n²/2, |E| ≤ n²/4. ✓.

If indeg is concentrated on low-degree vertices, Σ d(v) indeg(v) could be small. For example, if all indeg is on vertices with degree 1, Σ d(v) indeg(v) = n · 1 = n. Then S ≤ n² - n, |E| ≤ (n²-n)/2. For n = 100, this is 4950, which is way more than 2500.

But can this actually happen? If all witnesses point to degree-1 vertices, then every vertex u has f(u) = v where d(v) = 1. This means v's only neighbor is u (since d(v) = 1 and u is a neighbor of v). So f(u) = v means v is a pendant vertex attached only to u. And N(u) ∩ N(v) = N(u) ∩ {u} = ∅ (since u ∉ N(u)). ✓. 

But then u has a pendant neighbor v. The edge uv is a witness edge. Now, u has degree d(u) ≤ n - 1 (at most n-1 neighbors). And d(u) + d(v) = d(u) + 1 ≤ n, so d(u) ≤ n - 1. That's always true.

In this scenario, each vertex u has a pendant neighbor. But a pendant vertex has degree 1, so it's the pendant neighbor of only one vertex. So we need at least n pendant vertices, one for each u. But pendant vertices are also vertices in the graph, so if u has pendant v, then v is one of the n vertices, and v also needs a witness. v's only neighbor is u, so f(v) = u. And N(v) ∩ N(u) = {u} ∩ N(u) = ∅ (since u ∉ N(u)). ✓.

So the witness pairs are (u, v) where v is pendant to u. Each pair uses 2 vertices, and we need n/2 pairs. So we have n/2 "center" vertices and n/2 "pendant" vertices. Each center u has a pendant v, and u can have other neighbors too.

The centers can be connected among themselves. Each center u has d(u) = 1 (pendant) + (number of center neighbors). The pendants have d(v) = 1.

For the pendants, the condition is satisfied (witness is the center). For the centers, the witness is the pendant. N(u) ∩ N(v) = N(u) ∩ {u} = ∅ (since u ∉ N(u)). ✓. Wait, N(v) = {u} (v's only neighbor is u). N(u) ∩ {u} = ∅ since u ∉ N(u). ✓.

So the centers can form any graph among themselves! The total edges = (edges among centers) + n/2 (pendant edges).

The centers form a graph on n/2 vertices. To maximize total edges, maximize edges among centers. The maximum is C(n/2, 2) = (n/2)(n/2 - 1)/2.

Total edges = (n/2)(n/2 - 1)/2 + n/2 = n/2 · ((n/2 - 1)/2 + 1) = n/2 · (n/2 + 1)/2 = n(n+2)/8.

For n = 100: 100 · 102 / 8 = 1275. Much less than 2500.

So this construction gives fewer edges. The point is that using pendant witnesses "wastes" vertices.

OK so the bound S + Σ d(v) indeg(v) ≤ n² doesn't directly give S ≤ n²/2 because indeg can be concentrated on low-degree vertices. But in that case, the graph structure is constrained in other ways.

Let me think about this more carefully. The issue is that the algebraic bound is too weak. I need to use the structure of the graph more.

Let me try a different approach. Let me think about the problem in terms of the following:

For each vertex u, let f(u) = v be its witness. The key property is N(u) ∩ N(v) = ∅. This means:
- No neighbor of u (other than v) is a neighbor of v.
- No neighbor of v (other than u) is a neighbor of u.
- Equivalently, the edge uv is "isolated" in the sense that the neighborhoods of u and v are disjoint.

This means that in the graph, the vertices can be partitioned (relative to the edge uv) into:
- {u, v}
- N(u) \ {v} (neighbors of u other than v)
- N(v) \ {u} (neighbors of v other than u)
- R = V \ ({u,v} ∪ N(u) ∪ N(v)) (the rest, not adjacent to either u or v)

And |N(u) \ {v}| + |N(v) \ {u}| + |R| = n - 2, with |N(u) \ {v}| = d(u) - 1, |N(v) \ {u}| = d(v) - 1.

Now, let me think about a proof using the following idea:

For each vertex u, the witness edge {u, f(u)} "separates" the graph. The neighborhoods of u and f(u) are disjoint. 

Let me try to use an averaging argument.

For each vertex u, d(u) + d(f(u)) ≤ n. 

Consider the sum Σ_u (d(u) + d(f(u))) ≤ n².

Now, Σ_u d(u) = 2|E| = S. And Σ_u d(f(u)) = Σ_v d(v) · indeg(v).

So S + Σ_v d(v) · indeg(v) ≤ n².

Now, I need another inequality. Let me think about what other constraints we have.

For each u, f(u) ∈ N(u), so {u, f(u)} is an edge. The witness edges form a subgraph W. Each vertex has at least one incident witness edge.

Consider the sum Σ_u d(f(u))². Hmm, not sure.

Let me try to use the constraint that f(u) ∈ N(u) more carefully.

Since f(u) ∈ N(u), the edge {u, f(u)} exists. So u contributes 1 to d(f(u)). In other words, Σ_u [f(u) = v] ≤ d(v) for each v (the number of u's that point to v is at most d(v), since each such u must be a neighbor of v).

So indeg(v) ≤ d(v) for all v.

This is a key constraint! indeg(v) ≤ d(v).

Now, Σ_v d(v) · indeg(v) ≥ Σ_v d(v) · indeg(v). We want to lower-bound this.

We have: Σ indeg(v) = n, 0 ≤ indeg(v) ≤ d(v), and Σ d(v) = S.

Minimize Σ d(v) · indeg(v) subject to Σ indeg(v) = n, 0 ≤ indeg(v) ≤ d(v).

By the rearrangement inequality, this is minimized when indeg is concentrated on vertices with smallest d(v). But indeg(v) ≤ d(v), so if we concentrate indeg on low-degree vertices, we're limited by their degree.

Let me think about this optimization. Sort vertices by degree: d_1 ≤ d_2 ≤ ... ≤ d_n. We want to minimize Σ d_i · indeg_i subject to Σ indeg_i = n, 0 ≤ indeg_i ≤ d_i.

To minimize, assign indeg to the smallest d_i first, up to their capacity d_i.

If d_1 + d_2 + ... + d_k ≥ n for some k, then we can assign all indeg to the first k vertices. The minimum would be Σ_{i=1}^{k-1} d_i² + d_k · (n - Σ_{i=1}^{k-1} d_i).

But we also have the constraint Σ d_i = S. 

This is getting complicated. Let me try a different approach.

Actually, let me use the constraint indeg(v) ≤ d(v) more directly.

Σ_v d(v) · indeg(v) ≥ Σ_v indeg(v)² (by Cauchy-Schwarz? No, that's the wrong direction.)

Actually, since indeg(v) ≤ d(v), we have d(v) ≥ indeg(v), so d(v) · indeg(v) ≥ indeg(v)². Thus:

Σ_v d(v) · indeg(v) ≥ Σ_v indeg(v)².

By Cauchy-Schwarz: Σ_v indeg(v)² ≥ (Σ_v indeg(v))² / n = n²/n = n.

So Σ_v d(v) · indeg(v) ≥ n. This gives S ≤ n² - n, |E| ≤ (n²-n)/2. For n = 100, this is 4950. Too weak.

But we also have Σ d(v) = S and indeg(v) ≤ d(v). Let me use these together.

We have S + Σ d(v) indeg(v) ≤ n² and Σ d(v) indeg(v) ≥ Σ indeg(v)² ≥ n²/n = n.

This gives S ≤ n² - n. Not strong enough.

Let me try to get a better lower bound on Σ d(v) indeg(v).

We have indeg(v) ≤ d(v) and Σ indeg(v) = n and Σ d(v) = S.

Minimize Σ d(v) indeg(v) subject to these constraints.

Using Lagrange multipliers or by analysis: to minimize Σ d_i · x_i subject to Σ x_i = n, 0 ≤ x_i ≤ d_i, and Σ d_i = S (but the d_i are fixed, not variables).

Given fixed d_i, minimize Σ d_i x_i subject to Σ x_i = n, 0 ≤ x_i ≤ d_i.

This is a linear program. The minimum is achieved by setting x_i = d_i for the smallest d_i's until we reach Σ x_i = n.

Let the vertices be sorted d_1 ≤ d_2 ≤ ... ≤ d_n. Set x_i = d_i for i = 1, ..., k-1, and x_k = n - Σ_{i=1}^{k-1} d_i, where k is such that Σ_{i=1}^{k-1} d_i < n ≤ Σ_{i=1}^k d_i.

The minimum is Σ_{i=1}^{k-1} d_i² + d_k (n - Σ_{i=1}^{k-1} d_i).

Now, we also have Σ_{i=1}^n d_i = S. And we need Σ_{i=1}^k d_i ≥ n (so that we can assign all indeg to the first k vertices).

If S = Σ d_i and we need Σ_{i=1}^k d_i ≥ n, then k ≤ n (obviously). The question is: what's the minimum of Σ_{i=1}^{k-1} d_i² + d_k (n - Σ_{i=1}^{k-1} d_i) given that Σ d_i = S?

This depends on the degree sequence. To minimize Σ d(v) indeg(v), we want the low-degree vertices to have as small degree as possible and absorb all the indeg.

Extreme case: d_1 = d_2 = ... = d_m = 1 (m vertices of degree 1), and the rest have high degree. Then Σ_{i=1}^m d_i = m. If m ≥ n, we can set indeg_i = 1 for i = 1, ..., n, and Σ d_i indeg_i = n · 1 = n. But m ≤ n (only n vertices), and if m = n, all vertices have degree 1, S = n, |E| = n/2. Not interesting.

If m < n, say m vertices have degree 1 and n - m have higher degree. Σ_{i=1}^m d_i = m. We need n - m more indeg from the remaining vertices. The (m+1)-th vertex has degree d_{m+1}. Set indeg_{m+1} = min(d_{m+1}, n - m). If d_{m+1} ≥ n - m, then Σ d_i indeg_i = m · 1 + d_{m+1} · (n - m). 

To minimize this, we want d_{m+1} to be as small as possible. If d_{m+1} = n - m, then Σ d_i indeg_i = m + (n-m)². Hmm.

This is getting very complicated and I'm not sure it leads to a clean bound. Let me try a completely different approach.

Let me go back to thinking about the problem structurally.

Key observation: In any bipartite graph with no isolated vertices, the condition is automatically satisfied (as every edge has N(u) ∩ N(v) = ∅ since neighborhoods are in different parts). The maximum edges in a bipartite graph on n vertices is ⌊n²/4⌋.

For non-bipartite graphs, the condition is more restrictive. The question is whether a non-bipartite graph can satisfy the condition and have more than ⌊n²/4⌋ edges.

Let me think about this. Suppose G is not bipartite. Then G contains an odd cycle. Let C be the shortest odd cycle (which is an induced cycle, i.e., a hole). 

Actually, let me think about a specific non-bipartite construction and count edges.

Construction: Take K_{50,50} and try to add edges while maintaining the condition.

We showed that adding any edge within a part breaks the condition for the endpoints. But what if we also remove some edges?

Specifically: add edge a1-a2 within A, and remove edges a1-b1 and a2-b2 (for specific b1, b2). Now:

d(a1) = 50 - 1 + 1 = 50 (lost b1, gained a2).
d(a2) = 50 - 1 + 1 = 50 (lost b2, gained a1).
d(b1) = 50 - 1 = 49 (lost a1).
d(b2) = 50 - 1 = 49 (lost a2).

For a1: N(a1) = (B \ {b1}) ∪ {a2}. Need witness v with N(a1) ∩ N(v) = ∅.
- v = a2: N(a2) = (B \ {b2}) ∪ {a1}. N(a1) ∩ N(a2) = (B \ {b1, b2}) ≠ ∅ (since |B| = 50 > 2). Fails.
- v ∈ B \ {b1}: say v = b3. N(b3) = A (all of A, since b3 is still connected to all of A). N(a1) ∩ N(b3) = ((B\{b1}) ∪ {a2}) ∩ A = {a2} ≠ ∅. Fails.

So a1 still has no witness. The problem is that a1's neighborhood includes a2 (in A), and any B-vertex's neighborhood includes all of A (including a2).

To fix this, we'd need to also remove a2 from the neighborhoods of all B-vertices that a1 might use as witnesses. But a B-vertex b has N(b) = A (or A minus some vertices). If we remove a2 from N(b), we remove the edge a2-b. But then a2 loses another neighbor.

This cascading effect makes it very hard to add edges within parts while maintaining the condition. It seems like the bipartite structure is essential for maximizing edges.

Let me try to prove that the maximum is ⌊n²/4⌋ by showing that any graph satisfying the condition has at most ⌊n²/4⌋ edges.

Proof approach using the following lemma:

Lemma: If G satisfies the condition, then V can be partitioned into two sets A and B such that |E(G)| ≤ |A| · |B| + (edges within A) + (edges within B), and the edges within A and within B are "limited" in some way.

Hmm, this is vague. Let me try a more concrete approach.

Actually, let me try to prove it by induction, being more careful about the induction step.

Theorem: For any graph G on n vertices satisfying the condition, |E(G)| ≤ ⌊n²/4⌋.

Proof by induction on n.

Base: n = 1: 0 edges, 0 ≤ 0. ✓. n = 2: at most 1 edge, 1 ≤ 1. ✓.

Inductive step: Assume the result for all graphs on fewer than n vertices satisfying the condition.

Let G be a graph on n vertices satisfying the condition. 

Case 1: G has a vertex u with d(u) = 0. Then u has no neighbor, so the condition fails (u needs a neighbor v ∈ N(u), but N(u) = ∅). So G has no isolated vertices.

Case 2: G has a vertex u with d(u) = 1. Let v be the unique neighbor of u. Then f(u) = v (the only choice). N(u) ∩ N(v) = {v} ∩ N(v) = ∅ (since v ∉ N(v)). ✓. 

Now, consider G' = G - u (remove u). G' has n-1 vertices. Does G' satisfy the condition?

For any vertex w ≠ u in G': w had a witness f(w) in G. If f(w) ≠ u, then f(w) is still in G', and N_{G'}(w) ∩ N_{G'}(f(w)) ⊆ N_G(w) ∩ N_G(f(w)) = ∅. ✓.

If f(w) = u, then u was w's witness. But u has degree 1, so N(u) = {v}. For u to be w's witness, w must be a neighbor of u, so w = v. So f(v) = u. Now, in G', v needs a new witness. v's neighbors in G' are N_G(v) \ {u}. We need some v' ∈ N_{G'}(v) with N_{G'}(v) ∩ N_{G'}(v') = ∅.

This might not hold. So G' might not satisfy the condition.

Hmm. So the induction doesn't work directly.

Let me try removing both u and v (the degree-1 vertex and its neighbor).

G'' = G - {u, v}. This has n - 2 vertices. Does G'' satisfy the condition?

For w ∈ G'' with f(w) ∉ {u, v}: the witness is still in G'', and the condition holds. ✓.

For w ∈ G'' with f(w) = u: w must be a neighbor of u, so w = v. But v ∉ G''. So this case doesn't arise.

For w ∈ G'' with f(w) = v: w is a neighbor of v. In G'', w needs a new witness. This might not exist.

So again, G'' might not satisfy the condition.

The induction approach is tricky because removing vertices can break the condition for other vertices.

Let me try a different approach. Instead of induction, let me try a direct counting argument.

Direct approach:

For each vertex u, let f(u) be a witness. We have:
1. f(u) ∈ N(u) (witness is a neighbor)
2. N(u) ∩ N(f(u)) = ∅ (no common neighbors)
3. d(u) + d(f(u)) ≤ n (from 2)

From 1: indeg(v) ≤ d(v) for all v (as argued before).

Now, consider the following. For each vertex u, define g(u) = f(u). We have a function g: V → V with g(u) ∈ N(u) and d(u) + d(g(u)) ≤ n.

Let's think about the edges of G. Each edge e = {u, w} contributes to the degrees of u and w. 

For each vertex u, d(u) ≤ n - d(g(u)). 

Sum: S = Σ d(u) ≤ Σ (n - d(g(u))) = n² - Σ d(g(u)) = n² - Σ_v d(v) · indeg(v).

So S ≤ n² - Σ_v d(v) · indeg(v). ... (*)

Also, S = Σ d(v) and indeg(v) ≤ d(v), Σ indeg(v) = n.

Now, I need another inequality relating S and Σ d(v) indeg(v).

Consider: Σ_v d(v) · indeg(v) = Σ_v d(v) · indeg(v). 

Since indeg(v) ≤ d(v), we have d(v) · indeg(v) ≥ indeg(v) · indeg(v) = indeg(v)². So Σ d(v) indeg(v) ≥ Σ indeg(v)² ≥ n²/n = n (by QM-AM). This gives S ≤ n² - n. Not strong enough.

But we also have S = Σ d(v) ≥
The user wants me to solve the math problem directly. Let me check for answer leaks first.

The problem: Let G be a simple graph with 100 vertices such that for each vertex u, there exists a vertex v ∈ N(u) and N(u) ∩ N(v) = ∅. Find the maximal possible number of edges in G.

No answer leak detected. Let me solve.

So the condition: for every vertex u, there's a neighbor v of u such that u and v have no common neighbor. This means the edge uv is not part of any triangle (since if there were a common neighbor w, then u,v,w form a triangle). Actually N(u) ∩ N(v) = ∅ means no vertex is adjacent to both u and v. In particular, u ∉ N(u) (no self-loops) and v ∉ N(v), but u ∈ N(v) and v ∈ N(u). So the condition N(u) ∩ N(v) = ∅ means no common neighbor, which means edge uv is not in any triangle.

So the condition is: every vertex u is incident to at least one edge that is not in any triangle (i.e., every vertex is incident to at least one "triangle-free edge").

We want to maximize the number of edges.

Let me think. We want a graph on 100 vertices where every vertex has at least one incident edge that's in no triangle, and we maximize edges.

Strategy: To maximize edges, we want most of the graph to be a complete graph (or dense), but each vertex needs at least one "triangle-free" edge.

Idea: Take a complete graph K_{99} on 99 vertices, and add one extra vertex w connected to... hmm. If w is connected to just one vertex of K_{99}, then w has its triangle-free edge (the edge to that vertex, since w has no other neighbors so no common neighbor). But the vertex in K_{99} that w connects to — its edge to w: is it triangle-free? w's only neighbor is that vertex, so N(w) = {that vertex}, and N(that vertex) ∩ N(w) = N(that vertex) ∩ {that vertex}... wait N(w) = {u} where u is the vertex. N(u) ∩ N(w) = N(u) ∩ {u}. But u ∉ N(u) (no self loop), so N(u) ∩ {u} = ∅. Yes! So edge wu is triangle-free. Good for both w and u.

But the other 98 vertices in K_{99}: each needs a triangle-free edge. In K_{99}, every edge is in a triangle (since 99 ≥ 3). So those 98 vertices have no triangle-free edge. Bad.

So we need every vertex to have a triangle-free edge.

Alternative idea: Partition vertices into pairs, each pair connected by an edge, and these edges are triangle-free. Then make the rest as dense as possible.

Consider: take a perfect matching of 50 edges that are all triangle-free, then add as many other edges as possible while keeping those 50 edges triangle-free.

If we have a matching {a_1 b_1, ..., a_50 b_50} that is triangle-free, each edge a_i b_i has no common neighbor. To keep a_i b_i triangle-free, no vertex can be adjacent to both a_i and b_i. 

To maximize total edges: For each pair (a_i, b_i), the constraint is N(a_i) ∩ N(b_i) = ∅ (for the matching edge). We want to maximize edges subject to each pair having disjoint neighborhoods (excluding each other).

Actually let's think of it as: we have 50 pairs. Within each pair, the edge exists. Between pairs, we can add edges freely as long as for each pair (a_i, b_i), no outside vertex is adjacent to both a_i and b_i.

So for each pair i and each pair j (j ≠ i), the vertices a_i, b_i can connect to vertices in pair j, but each vertex in pair j can be adjacent to at most one of {a_i, b_i}.

Hmm, let me think about the structure. Let's denote pairs P_1, ..., P_50. For pair P_i = {a_i, b_i}, the edge a_i b_i is triangle-free, meaning no vertex is adjacent to both a_i and b_i.

Consider the complete graph on 100 vertices has C(100,2) = 4950 edges. We need to remove edges to satisfy constraints.

Actually, let me think differently. Consider the complement or think about a specific construction.

Construction: Take 50 copies of K_2 (edges), and between every two pairs, make it a complete bipartite-ish structure. 

Let me think: For pairs P_i and P_j, we want to maximize edges between them subject to: for pair P_i, no vertex adjacent to both a_i and b_i; for pair P_j, no vertex adjacent to both a_j and b_j.

Between P_i = {a_i, b_i} and P_j = {a_j, b_j}: possible edges are a_i a_j, a_i b_j, b_i a_j, b_i b_j (4 edges). Constraints:
- For P_i's triangle-free edge: a_j can't be adjacent to both a_i and b_i; b_j can't be adjacent to both a_i and b_i.
- For P_j's triangle-free edge: a_i can't be adjacent to both a_j and b_j; b_i can't be adjacent to both a_j and b_j.

So each of a_j, b_j is adjacent to at most one of {a_i, b_i}, and each of a_i, b_i is adjacent to at most one of {a_j, b_j}.

This is like a 2x2 0-1 matrix where each row has at most one 1 and each column has at most one 1. Max number of 1s = 2 (a permutation matrix). So between any two pairs, at most 2 edges.

So total edges = 50 (matching) + C(50,2) * 2 = 50 + 1225 * 2 = 50 + 2450 = 2500.

Can we achieve 2 edges between every pair of pairs? Yes: e.g., connect a_i to a_j and b_i to b_j for all i,j (so a's form a clique and b's form a clique). Then check: edge a_i b_i: is a_j adjacent to both a_i and b_i? a_j adjacent to a_i (yes, in a-clique) and to b_i? b_i is in b-clique, a_j is in a-clique, a_j-b_i not an edge. So a_j not adjacent to b_i. Good. Similarly b_j adjacent to b_i but not a_i. So no common neighbor. Triangle-free confirmed.

So construction: a_1,...,a_50 form K_50, b_1,...,b_50 form K_50, and edges a_i b_i. Total = C(50,2) + C(50,2) + 50 = 1225 + 1225 + 50 = 2500.

Now is 2500 optimal? We need to prove we can't do better.

Let me think about the upper bound. The condition: every vertex has a triangle-free incident edge. 

Hmm, but maybe a non-matching structure does better. Let me think more generally.

Actually, let me reconsider. The constraint is per-vertex: each vertex u has SOME neighbor v with N(u)∩N(v)=∅. It doesn't have to be a matching; multiple vertices could share the same triangle-free edge partner.

Let me think about an upper bound. 

Consider the graph G. For each vertex u, choose one "witness" edge e_u = uv_u that is triangle-free (v_u is a neighbor with no common neighbor). 

A triangle-free edge uv: N(u) ∩ N(v) = ∅. Note deg(u) + deg(v) ≤ n = 100 (since N(u) and N(v) are disjoint subsets of V \ {u,v}... wait, N(u) ⊆ V\{u}, N(v) ⊆ V\{v}, and N(u)∩N(v)=∅. Also v ∈ N(u) and u ∈ N(v). So N(u) and N(v) are disjoint. |N(u)| + |N(v)| ≤ 100 (they're disjoint subsets of the 100 vertices, but v ∈ N(u) and u ∈ N(v), and these are different vertices, so |N(u)|+|N(v)| ≤ 100). So deg(u) + deg(v) ≤ 100 for each triangle-free edge uv.

Now, sum over all vertices: Σ deg(u) = 2|E|. 

For each vertex u, there's a triangle-free edge uv_u with deg(u) + deg(v_u) ≤ 100.

Hmm, let me think about how to bound total edges.

Let S be the set of triangle-free edges. Every vertex is incident to at least one edge in S. 

For each edge e = uv in S, deg(u) + deg(v) ≤ 100.

Sum over edges in S: Σ_{uv ∈ S} (deg(u) + deg(v)) ≤ 100 |S|.

The left side: Σ_{uv ∈ S} (deg(u) + deg(v)) = Σ_u deg(u) * (number of S-edges incident to u) ≥ Σ_u deg(u) * 1 = 2|E| (since each vertex incident to ≥1 S-edge).

Wait, that gives 2|E| ≤ 100 |S|. And |S| ≤ ? Each vertex incident to ≥1 S-edge, so |S| ≥ 50 (S is an edge cover, min edge cover... actually |S| could be as low as 50 if it's a perfect matching, but could be more). This gives 2|E| ≤ 100|S|, not directly useful for upper bound since |S| can be large.

Hmm wait, we want upper bound on |E|. Let me reconsider.

Actually we have 2|E| ≤ Σ_{uv∈S}(deg(u)+deg(v)) ≤ 100|S|. So |E| ≤ 50|S|. To minimize the bound we want |S| small, but |S| ≥ 50. So |E| ≤ 50|S|, and if |S| = 50, |E| ≤ 2500. But if |S| > 50, the bound is weaker. So this only gives |E| ≤ 2500 when |S| = 50.

But maybe we can show |S| = 50 is forced or that the bound still holds. Hmm, not directly.

Let me think differently. Let me reconsider: we need a better argument.

Alternative: Let's think about it as follows. Consider the subgraph H = (V, S) of triangle-free edges that are "used" (we pick a set S of triangle-free edges forming an edge cover). Actually, let me pick S to be a minimal edge cover (each vertex covered, minimal). A minimal edge cover in a graph with no isolated vertices has size n - ν where ν is the matching number... actually for the edge cover, minimum edge cover = n - (max matching). Hmm.

Let me just try: pick a maximum matching M in the graph of triangle-free edges (call this graph T, with vertex set V and edges = triangle-free edges). Every vertex has degree ≥ 1 in T. 

Actually, let me think about whether 2500 is truly the max. Let me consider small cases or other constructions.

Alternative construction: What if we don't use a perfect matching of triangle-free edges but something else?

Consider: one vertex w connected to all others, and... no, w's triangle-free edge: w needs a neighbor v with N(w)∩N(v)=∅. If w is connected to everyone, N(w) = 99 vertices, then v must have N(v) disjoint from N(w), but v ∈ N(w) so N(v) ⊆ N(w) ∪ {w} \ {v}... actually N(v) ⊆ V\{v}, and N(w) = V\{w}. N(v) ∩ N(w): since N(w) = V\{w}, N(v) ∩ N(w) = N(v) \ {w} (if w ∈ N(v)). For this to be ∅, N(v) ⊆ {w}, so deg(v) ≤ 1, meaning v only connected to w. But then v's only neighbor is w, and v needs its own triangle-free edge: v's neighbor is w, N(v)∩N(w) = {w}∩(V\{w})... wait N(v) = {w}, N(w) = V\{w}, intersection = ∅. Good. So edge vw is triangle-free for both. But all other 98 vertices need triangle-free edges too, and they're all connected to w (and possibly each other). If they form a clique among themselves plus w, every edge among them is in a triangle. So they need triangle-free edges, which must go to... vertices with very small degree. This seems to limit things.

Let me just try to verify 2500 is optimal more carefully.

Upper bound attempt: Let M be a maximum matching in the triangle-free-edge graph T. Let |M| = m. The vertices not covered by M form an independent set in T (since M is maximum), so they have no triangle-free edges among themselves. But every vertex has a triangle-free edge, so each uncovered vertex has a triangle-free edge to a covered vertex.

Hmm, this is getting complex. Let me think about the structure more.

Actually, let me reconsider the problem. Let me re-examine if we can beat 2500.

Suppose we have the construction with two K_50's and a matching between them = 2500 edges. Can we add any edge? Adding edge a_i b_j (i≠j): then edge a_i b_i — is it still triangle-free? a_i b_i: common neighbor? a_j is adjacent to a_i (clique) and now b_j is adjacent to a_i (new edge) and b_j adjacent to b_i (clique). Is a_j adjacent to b_i? No. Is b_j adjacent to both a_i and b_i? b_j adjacent to a_i (new edge, yes) and b_j adjacent to b_i (b-clique, yes). So b_j is a common neighbor of a_i and b_i! So edge a_i b_i is no longer triangle-free. Then a_i needs another triangle-free edge, and b_i needs another. This breaks things. So we can't easily add edges.

Let me think about whether a different structure could give more.

What about: three cliques? Say partition into groups. Hmm.

Let me think about the general upper bound more carefully.

Claim: |E| ≤ 2500.

Proof approach: For each vertex u, let f(u) be a chosen neighbor with N(u)∩N(f(u))=∅. Note f(f(u)) might not be u, but the edge u f(u) is triangle-free so actually N(f(u))∩N(u)=∅ too, meaning u is a valid witness for f(u) as well. But f(u) might choose a different witness.

Key fact: for the chosen edge uv (triangle-free), deg(u)+deg(v) ≤ 100.

Consider the directed graph where each u points to f(u). Each vertex has out-degree 1. The underlying edges form a set S (triangle-free edges), and S is an edge cover (every vertex incident to ≥1 edge of S, since u is incident to u f(u)).

Now, Σ_u deg(u) = 2|E|. Also Σ_u deg(f(u)) = Σ_v deg(v) * |f^{-1}(v)|.

We have deg(u) + deg(f(u)) ≤ 100 for all u. Sum over all u:
Σ_u deg(u) + Σ_u deg(f(u)) ≤ 100 n = 10000.
2|E| + Σ_v deg(v)|f^{-1}(v)| ≤ 10000.

Hmm, Σ_v deg(v)|f^{-1}(v)| ≥ ? Not obviously helpful.

Since Σ_u deg(f(u)) = Σ_v deg(v) · indeg(v) where indeg(v) = |f^{-1}(v)| ≥ 0, and Σ_v indeg(v) = n = 100.

By rearrangement, Σ_v deg(v)·indeg(v) ≥ (Σ_v deg(v))(Σ indeg(v))/n ... no wait, that's not right in general. Actually by Chebyshev or rearrangement, if we want a lower bound on Σ deg(v)·indeg(v) given Σ indeg = n, the minimum is when high indeg pairs with low deg. We can't bound it below easily without knowing structure.

Hmm. Let me think differently.

Actually, note that indeg(v) ≥ 1 iff v is in the image of f. The image of f has size ≤ n. Also, if v is not in the image, indeg(v) = 0. 

Let me think about it as: we want to maximize 2|E| = Σ deg(u) subject to: there exists a function f with each u→f(u) a triangle-free edge, deg(u)+deg(f(u)) ≤ 100.

This is like: we have a directed functional graph, and the constraint deg(u)+deg(f(u)) ≤ 100.

To maximize Σ deg(u), we'd want the constraint to be loose. The constraint deg(u)+deg(f(u)) ≤ 100 binds when degrees are high.

If we pair up vertices (f is an involution, perfect matching), then deg(u)+deg(f(u)) ≤ 100 for each pair, and Σ deg = Σ_pairs (deg+deg) ≤ 50 · 100 = 5000, so |E| ≤ 2500. 

But if f is not a perfect matching (some vertex has high indeg), can we do better? Suppose vertex v has indeg k (k vertices point to v). Then deg(v) + deg(u_i) ≤ 100 for each of the k vertices u_i. So deg(u_i) ≤ 100 - deg(v) for each. And v itself points to f(v) with deg(v)+deg(f(v)) ≤ 100.

The total contribution: v contributes deg(v), the k vertices contribute ≤ k(100 - deg(v)), and f(v) is among... hmm, f(v) could be one of the u_i or not.

Let me think of it as: the functional graph of f decomposes into components, each a cycle with trees hanging off. 

For a component, let's compute the max of Σ deg over the component given the constraints.

Consider a cycle C of length ℓ: v_1 → v_2 → ... → v_ℓ → v_1. Constraints: deg(v_i) + deg(v_{i+1}) ≤ 100 for each i. Sum: Σ deg(v_i) + Σ deg(v_{i+1}) = 2 Σ deg(v_i) ≤ 100ℓ, so Σ deg(v_i) ≤ 50ℓ.

Now trees hanging off cycle vertices: say vertex v (on cycle or tree) has children u_1,...,u_k (pointing to v). Each has deg(u_i) + deg(v) ≤ 100, so deg(u_i) ≤ 100 - deg(v). The u_i's might have their own children.

This is like: for a tree rooted at v (with edges pointing toward v, i.e., children point to parent), the constraint is deg(child) + deg(parent) ≤ 100. To maximize Σ deg over the tree, given deg(parent) = d, each child has deg ≤ 100 - d, and then their children have deg ≤ 100 - (100-d) = d, etc. So it alternates.

Let me compute: root v with deg d. Children (level 1): each deg ≤ 100-d. Their children (level 2): deg ≤ d. Level 3: ≤ 100-d. Etc.

If v has k_1 children, each with k_2 children, etc. Total deg sum = d + k_1(100-d) + k_1 k_2 · d + k_1 k_2 k_3 (100-d) + ...

To maximize, we want many vertices. But total vertices = 100. 

Hmm, let me think about whether trees help or hurt compared to pure matching.

Pure 2-cycle (matching pair): 2 vertices, Σ deg ≤ 100, avg 50 per vertex.

Tree: root v (deg d), one child u (deg 100-d). Σ = 100 for 2 vertices. Same as matching. Add a grandchild w (child of u): deg(w) ≤ d. Σ = 100 + d for 3 vertices. Avg = (100+d)/3. If d = 50, avg 50. If d < 50, avg < 50. 

Actually for 3 vertices with root d, child 100-d, grandchild d: Σ = 100 + d. To get Σ = 150 (avg 50), need d = 50. So if d=50, 3 vertices give Σ=150, same avg. If d=50, child deg 50, grandchild deg 50. All 50. That's just all degrees 50, consistent.

Hmm, so it seems like the average degree is at most 50 regardless, giving |E| ≤ 2500. Let me verify this more carefully.

Claim: For any functional graph component (cycle + trees) with the constraint deg(u)+deg(f(u)) ≤ 100, the sum of degrees is at most 50 times the number of vertices.

Proof: Consider the component with vertex set W, |W| = s. The edges of the functional graph form a connected functional graph (one cycle, trees). It's a connected graph on s vertices with s edges (each vertex one out-edge), so it's a tree plus one edge = unicyclic.

Actually, let me use a cleaner argument. The functional graph on W has s vertices and s directed edges (each vertex has outdegree 1). The underlying undirected graph has s edges on s vertices and is connected (one component), so it has exactly s edges and s vertices: it's unicyclic (one cycle, trees attached).

Now, sum the constraint deg(u) + deg(f(u)) ≤ 100 over all u ∈ W:
Σ_{u∈W} deg(u) + Σ_{u∈W} deg(f(u)) ≤ 100s.

The first sum is D = Σ_{u∈W} deg(u). The second sum: Σ_{u∈W} deg(f(u)) = Σ_{v∈W} deg(v) · indeg_W(v) where indeg_W is indegree within the component. 

Hmm, this doesn't directly give D ≤ 50s because the second sum isn't equal to D.

Σ_{u∈W} deg(f(u)): as u ranges over W, f(u) ranges over W (since the component is closed under f). Each v ∈ W appears as f(u) exactly indeg(v) times. So Σ_{u∈W} deg(f(u)) = Σ_{v∈W} deg(v)·indeg(v).

In a functional graph component, Σ indeg(v) = s (total indegree = total outdegree = s). But indeg(v) varies. On the cycle, each vertex has indeg ≥ 1 (from cycle) plus tree contributions. Tree leaves have indeg 0.

So D + Σ_v deg(v)·indeg(v) ≤ 100s.

We want D ≤ 50s. This requires Σ_v deg(v)·indeg(v) ≥ D, i.e., Σ_v deg(v)(indeg(v) - 1) ≥ 0, i.e., Σ_v deg(v)·indeg(v) ≥ Σ_v deg(v).

Is Σ deg(v)·indeg(v) ≥ Σ deg(v)? That's Σ deg(v)(indeg(v)-1) ≥ 0. Not necessarily true! Vertices with indeg 0 (leaves) contribute negatively.

Hmm. So this approach doesn't directly work. Let me reconsider.

Let me think about a potential counterexample. Can we beat 2500?

Consider: vertex v with very high degree, say deg(v) = 99 (connected to all). Then v needs a triangle-free edge to some u with deg(u) ≤ 1 (since deg(v)+deg(u) ≤ 100). So u has degree 1, connected only to v. Now u is covered. But the other 98 vertices each need triangle-free edges. 

Each of the 98 other vertices w: needs a triangle-free edge. w is connected to v (since v connects to all). For w's triangle-free edge to some x: deg(w)+deg(x) ≤ 100 and N(w)∩N(x)=∅. Since w is adjacent to v, and v is adjacent to almost everyone, x must not be adjacent to v (otherwise v ∈ N(w)∩N(x)). So x is not adjacent to v. The only vertex not adjacent to v is u (deg 1, only to v) — wait u IS adjacent to v. So everyone is adjacent to v. Then for any w, any triangle-free partner x must have v ∉ N(x), but everyone is adjacent to v. Contradiction unless x = v, but then edge wv: N(w)∩N(v) must be ∅, but N(v) is huge. So no.

So high-degree vertex doesn't work well. The matching construction seems good.

Let me try to prove the upper bound 2500 rigorously.

Let me use a different approach. Let's define for each vertex u a witness v(u) with uv(u) triangle-free. Consider the graph structure.

Alternative approach using the triangle-free edge cover:

Let T be the set of all triangle-free edges. T forms an edge cover of V (every vertex incident to some edge in T). 

For each triangle-free edge e = uv, deg(u) + deg(v) ≤ 100.

Let M be a maximum matching in T. |M| = m. Since T is an edge cover (no isolated vertices in T), the minimum edge cover has size n - m = 100 - m. But we're using M (maximum matching), not min edge cover.

Vertices covered by M: 2m. Uncovered: 100 - 2m, these form an independent set in T (no T-edge among them, by maximality of M). Each uncovered vertex has T-edges only to covered vertices.

Hmm, let me think about using the matching M directly.

For each edge uv ∈ M: deg(u) + deg(v) ≤ 100. Sum over M: Σ_{uv∈M}(deg(u)+deg(v)) ≤ 100m.

The LHS = Σ_{v covered by M} deg(v) = Σ_{v∈V} deg(v) - Σ_{v not covered} deg(v) = 2|E| - Σ_{uncovered} deg(v).

So 2|E| - Σ_{uncovered} deg(v) ≤ 100m, giving 2|E| ≤ 100m + Σ_{uncovered} deg(v).

Now, uncovered vertices: each has a triangle-free edge to a covered vertex w. For uncovered vertex x with triangle-free edge xw (w covered), deg(x) + deg(w) ≤ 100. Also, w is covered by M, so w is in some matching edge ww'. deg(w) + deg(w') ≤ 100.

Hmm, I want to bound Σ_{uncovered} deg(x). Each uncovered x has deg(x) ≤ 100 - deg(w_x) where w_x is its T-neighbor (covered). 

This is getting complicated. Let me think about whether the answer might not be 2500 and try to find the actual max via a different construction.

Let me reconsider. Maybe we can do better than 2500 with a cleverer structure.

What if we use a structure where some vertices have degree > 50 but compensate with low-degree partners, and the average still exceeds 50?

Consider: take the matching construction (2500) and try to modify. 

Actually, let me reconsider the constraint. The constraint is only that each vertex has AT LEAST ONE triangle-free edge. The rest of the edges can be in triangles.

In the matching construction, the matching edges are triangle-free, and all other edges (within the two cliques) are in triangles. That's fine.

Can we have a graph where some vertices have degree much higher than 50, as long as they have one triangle-free edge to a low-degree vertex?

Example: Take K_{98} (clique on 98 vertices) plus two vertices a, b. Connect a to all 98 vertices of K_{98}, connect b to only one vertex, say a. Wait, let me think.

We need every vertex to have a triangle-free edge. 

Construction attempt: Let's have 49 "low" vertices each paired with a "high" vertex, and 2 extra vertices. Hmm, let me think more carefully.

Let me try: Partition 100 vertices into 50 pairs (a_i, b_i). Make a_1,...,a_50 a clique (K_50). For b_i: connect b_i only to a_i. Then:
- Edge a_i b_i: N(a_i) = {all a_j, j≠i} ∪ {b_i}, N(b_i) = {a_i}. Intersection: N(a_i) ∩ N(b_i) = N(a_i) ∩ {a_i} = ∅ (since a_i ∉ N(a_i)). Triangle-free! Good.
- Each a_i has triangle-free edge a_i b_i. ✓
- Each b_i has triangle-free edge b_i a_i. ✓

Edges: C(50,2) [a-clique] + 50 [a_i b_i] = 1225 + 50 = 1275. That's way less than 2500.

OK so that's worse. The matching construction with two cliques is better because b's also form a clique.

Let me try asymmetric: a's form K_p, b's form K_q with p+q = 100, matching between them (but matching requires p = q = 50). If p ≠ q we can't have a perfect matching. 

What if we don't require a perfect matching of triangle-free edges? Let me think about a construction with two groups of unequal size.

Say group A has p vertices, group B has q = 100 - p vertices. A is a clique, B is a clique. Triangle-free edges: we need each vertex to have one. 

If we add edges between A and B, we need to be careful. In the matching construction, the cross edges a_i b_i are the triangle-free edges, and there are no other cross edges.

What if p = 60, q = 40? We need each of the 100 vertices to have a triangle-free edge. The triangle-free edges must be cross edges (between A and B) or... could be within A or B? Within a clique, every edge is in a triangle (if size ≥ 3). So triangle-free edges must be cross edges, and each must have no common neighbor.

A cross edge a b (a ∈ A, b ∈ B): N(a) ∩ N(b) = ∅. N(a) includes all other A-vertices (clique) and possibly some B-vertices. N(b) includes all other B-vertices and possibly some A-vertices. For N(a)∩N(b) = ∅, no vertex can be adjacent to both a and b. Since a is adjacent to all of A\{a} and b is adjacent to all of B\{b}, we need A\{a} and B\{b} to not be adjacent to the other endpoint. Specifically, no a' ∈ A\{a} is adjacent to b, and no b' ∈ B\{b} is adjacent to a. So b is adjacent to no A-vertex except a, and a is adjacent to no B-vertex except b.

So each triangle-free cross edge ab is "isolated" in the sense that a has no other B-neighbors and b has no other A-neighbors.

Now, each vertex needs at least one triangle-free edge. For a ∈ A, it needs a cross edge to some b ∈ B where a has no other B-neighbor and b has no other A-neighbor. Similarly for b ∈ B.

If a vertex a ∈ A has a triangle-free edge to b, then a has no other B-neighbor. So a's only cross edge is to b. Similarly b's only cross edge is to a. So triangle-free edges form a matching between A and B!

Wait, not exactly a matching: a could have its triangle-free edge to b, but a might have other cross edges that are NOT triangle-free. But we showed that if ab is triangle-free, then a has no other B-neighbor. So a has exactly one cross edge (to b), and it's triangle-free. So a cannot have other cross edges.

Hmm wait, that means if a ∈ A has a triangle-free cross edge to b, then a's only cross edge is ab. But a might need other cross edges for... no, a just needs one triangle-free edge. But other vertices might need a to have cross edges to them. 

Actually, the point is: if a has a triangle-free edge to b, a has no other B-neighbor. So a's degree = (p-1) [from A-clique] + 1 [b] = p. And b's degree = (q-1) + 1 = q.

For this to work for ALL vertices, every a ∈ A needs a triangle-free edge to some b, meaning every a has exactly one B-neighbor. And every b ∈ B needs a triangle-free edge to some a, meaning every b has exactly one A-neighbor. So the cross edges form a perfect matching between A and B, requiring |A| = |B| = 50.

So with the two-clique construction, we must have p = q = 50, giving 2500.

But maybe a non-clique construction does better? Let me think about whether 2500 is truly optimal.

Let me think about a more general upper bound.

General approach: Let's think about what limits us. 

Let me consider the "witness" function f: V → V where f(u) is a neighbor of u with N(u)∩N(f(u))=∅. As noted, deg(u)+deg(f(u)) ≤ 100.

Consider the functional graph of f. It decomposes into components, each with a directed cycle and in-trees.

For a component with vertex set W (|W|=s), let's think about the sum D_W = Σ_{u∈W} deg(u).

The edges of the functional graph within W: each u ∈ W has f(u) ∈ W (closed). The functional graph on W is connected (it's one component). 

Now I'll use a cleverer bound. For each u, deg(u) + deg(f(u)) ≤ 100. 

Sum over u ∈ W: D_W + Σ_{u∈W} deg(f(u)) ≤ 100s.

Now Σ_{u∈W} deg(f(u)) = Σ_{v∈W} deg(v) · indeg(v).

So D_W + Σ_v deg(v)·indeg(v) ≤ 100s, i.e., D_W ≤ 100s - Σ_v deg(v)·indeg(v).

We want to show D_W ≤ 50s, i.e., Σ_v deg(v)·indeg(v) ≥ 50s.

Hmm, is Σ_v deg(v)·indeg(v) ≥ 50s always true? Not obviously.

Let me think about a specific component. Consider a 2-cycle: u ↔ v (f(u)=v, f(v)=u). indeg(u)=1, indeg(v)=1. Σ deg·indeg = deg(u)+deg(v) ≤ 100 = 50·2. So D_W = deg(u)+deg(v) ≤ 100 = 50s. ✓ (tight)

Consider a 3-cycle: u→v→w→u. indeg each =1. Σ deg·indeg = deg(u)+deg(v)+deg(w) = D_W. Constraint: deg(u)+deg(v)≤100, deg(v)+deg(w)≤100, deg(w)+deg(u)≤100. Sum: 2D_W ≤ 300, D_W ≤ 150 = 50·3. ✓

Consider a tree: root v (on cycle or not) with child u (f(u)=v). Say v is on a 2-cycle with v'. indeg(v) = 1 (from v') + 1 (from u) = 2. indeg(u) = 0. indeg(v') = 1.

Σ deg·indeg = deg(v)·2 + deg(v')·1 + deg(u)·0 = 2deg(v) + deg(v').
D_W = deg(v) + deg(v') + deg(u).
Constraints: deg(v)+deg(v') ≤ 100 (cycle edge), deg(u)+deg(v) ≤ 100 (tree edge).
D_W ≤ 100 - deg(v) + deg(v) + deg(u) ... let me just compute.
From constraints: deg(v') ≤ 100 - deg(v), deg(u) ≤ 100 - deg(v).
D_W = deg(v) + deg(v') + deg(u) ≤ deg(v) + (100-deg(v)) + (100-deg(v)) = 200 - deg(v).
For D_W ≤ 150 (= 50·3): need 200 - deg(v) ≤ 150, i.e., deg(v) ≥ 50.

But deg(v) could be < 50! If deg(v) = 10, then D_W ≤ 190 > 150. So the bound D_W ≤ 50s FAILS for this tree component!

Wait, but does that mean we can beat 2500? Let me check: if deg(v) = 10, deg(v') = 90, deg(u) = 90. D_W = 190 for 3 vertices, avg 63.3 > 50. 

But wait, can we actually realize this? We need a graph where v has degree 10, v' has degree 90, u has degree 90, with the triangle-free edges vv' and uv. And the rest of the graph (97 other vertices) also needs to be handled.

Hold on. Let me reconsider. The constraint is deg(u) + deg(f(u)) ≤ 100. If deg(v) = 10, deg(v') = 90, deg(u) = 90: vv' is triangle-free (10+90=100 ✓), uv is triangle-free (90+10=100 ✓). But we also need N(v)∩N(v')=∅ and N(u)∩N(v)=∅.

deg(v) = 10: v is adjacent to v', u, and 8 others. deg(v') = 90: v' adjacent to v and 89 others. N(v)∩N(v') = ∅: the 8 others adjacent to v can't be adjacent to v'. Since v' is adjacent to 89 others (out of 98 non-v vertices), and v is adjacent to u + 8 others = 9 non-v' vertices. N(v) = {v', u, 8 others}, N(v') = {v, 89 others}. N(v)∩N(v') = ({v',u,8others}) ∩ ({v, 89 others}). v' ∉ N(v') (no self-loop), v ∉ N(v). So intersection = {u, 8 others} ∩ {89 others}. For this to be ∅, u and the 8 others must not be in N(v'). So v' is adjacent to 89 vertices, none of which are u or the 8 others. The 89 vertices are from the remaining 100 - 1(v) - 1(v') - 1(u) - 8 = 89 vertices. So v' is adjacent to all 89 of those. OK.

Now N(u)∩N(v) = ∅: N(u) = 90 vertices, N(v) = {v', u, 8 others}. u ∉ N(u). So N(u) ∩ N(v) = N(u) ∩ {v', 8 others} (excluding u since u∉N(u), and v' could be in N(u)). For ∅: v' ∉ N(u) and the 8 others ∉ N(u). 

But v' is adjacent to 89 vertices (all except v, v', u, and the 8 others). Is u adjacent to v'? We need v' ∉ N(u), so u not adjacent to v'. OK. And the 8 others not in N(u). u is adjacent to 90 vertices out of 99. u is not adjacent to v' and not adjacent to the 8 others = 9 vertices not adjacent. But u has degree 90, so u is not adjacent to 9 vertices. ✓ (99 - 90 = 9). 

So u is adjacent to v and 89 others (the same 89 that v' is adjacent to). So u and v' have the same neighborhood (the 89 vertices) plus u is adjacent to v and v' is adjacent to v. 

Now, the 89 vertices: each needs a triangle-free edge. These 89 vertices are adjacent to both u and v'. They form... we need to figure out their adjacencies.

This is getting complex. Let me think about whether this can actually beat 2500.

Total edges so far: deg(v) + deg(v') + deg(u) = 10 + 90 + 90 = 190, but edges counted: vv', uv, v's other 8 edges, v's 89 edges, u's 89 edges. Wait let me recount. 

Edges incident to v: vv', vu, and 8 others = 10 edges.
Edges incident to v': v'v, and 89 to the 89-group = 90 edges (but vv' already counted).
Edges incident to u: uv, and 89 to the 89-group = 90 edges (uv already counted).

Unique edges: vv', vu, 8 (v to 8-group), 89 (v' to 89-group), 89 (u to 89-group). But wait, the 8-group: are they also in the 89-group? No: v is adjacent to v', u, and 8 others. The 8 others are not in the 89-group (since v' is not adjacent to them). So the 8-group is separate from the 89-group. Total vertices: v, v', u, 8-group, 89-group = 1+1+1+8+89 = 100. ✓

Edges so far: 10 (v's edges) + 89 (v' to 89-group, excluding vv') + 89 (u to 89-group, excluding uv) = 10 + 89 + 89 = 188.

Now the 89-group and 8-group need internal edges and triangle-free edges. The 89-group: each vertex is adjacent to u and v'. They need a triangle-free edge. 

The 89-group vertices are adjacent to u and v'. For a vertex x in the 89-group, its triangle-free edge partner y must have N(x)∩N(y)=∅. Since x is adjacent to u and v', y must not be adjacent to u or v'. Who is not adjacent to u or v'? v is not adjacent to u? No, v IS adjacent to u. The 8-group: are they adjacent to u? No (u is not adjacent to the 8-group). Are they adjacent to v'? No (v' is not adjacent to the 8-group). So the 8-group vertices are not adjacent to u or v'. 

So x's triangle-free partner could be in the 8-group. But there are 89 vertices in the 89-group and only 8 in the 8-group. Each 8-group vertex can be a triangle-free partner for multiple 89-group vertices? If x and x' both use the same 8-group vertex w as partner, then edges xw and x'w must both be triangle-free. 

Edge xw: N(x)∩N(w)=∅. N(x) includes u, v', and possibly others. N(w) includes v (since w is in 8-group, adjacent to v) and possibly others. For N(x)∩N(w)=∅: u ∉ N(w) (✓, w not adjacent to u), v' ∉ N(w) (✓), and any other neighbor of x not in N(w), and v ∉ N(x) (is x adjacent to v? x is in 89-group, v is adjacent to only v', u, 8-group. So v not adjacent to x. ✓). Also w's neighbors: w is adjacent to v. Is v ∈ N(x)? No. Other neighbors of w? If w has other neighbors, they must not be in N(x).

This is getting very complicated. Let me step back and think about the problem from a higher level.

Let me reconsider: is the answer 2500 or something else?

Let me think about it from the perspective of the complement graph or known results.

Actually, let me reconsider the tree component analysis. The issue is that a tree component can have average degree > 50. But the question is whether the ENTIRE graph can have average degree > 50.

In the example above, the component {v, v', u} has sum of degrees 190 for 3 vertices. But the 89-group and 8-group vertices also need to be accounted for, and they might have lower average degree.

Let me think about it more carefully with a cleaner model.

Actually, let me reconsider. The key insight might be different. Let me think about the problem as follows:

For each vertex u, choose witness f(u). The edge uf(u) is triangle-free, so deg(u) + deg(f(u)) ≤ n = 100.

Now consider the sum S = Σ_u (deg(u) + deg(f(u))) ≤ 100n = 10000.
S = Σ_u deg(u) + Σ_u deg(f(u)) = 2|E| + Σ_v deg(v)·indeg(v).

So 2|E| + Σ_v deg(v)·indeg(v) ≤ 10000.

Now, Σ_v deg(v)·indeg(v) ≥ 0, so 2|E| ≤ 10000, |E| ≤ 5000. That's trivial (complete graph has 4950).

We need a better bound. The issue is that Σ_v deg(v)·indeg(v) could be small if high-degree vertices have low indeg.

Hmm, but there's a constraint: every vertex has outdeg 1 and the function f maps to neighbors. Let me think about indeg more carefully.

Actually, let me think about a cleaner upper bound argument.

Alternative: Let's not use the functional graph. Instead, consider the set of triangle-free edges T (an edge cover). 

For each triangle-free edge uv, deg(u) + deg(v) ≤ 100.

We want to maximize |E| = (1/2)Σ deg(v).

Consider a minimum edge cover C ⊆ T (minimum number of triangle-free edges covering all vertices). |C| = n - ν_T where ν_T is the maximum matching in T. Since T has a perfect matching iff... well, |C| ≥ n/2 = 50 (since each edge covers 2 vertices). And |C| = 50 iff T has a perfect matching.

For each edge uv ∈ C, deg(u)+deg(v) ≤ 100. Sum over C: Σ_{uv∈C}(deg(u)+deg(v)) ≤ 100|C|.

Each vertex is covered by C. In a minimum edge cover, each vertex is covered exactly once (if a vertex were covered twice, we could remove an edge). Wait, no: in a minimum edge cover, it's not necessarily that each vertex is covered once. Actually, a minimum edge cover can be decomposed as a maximum matching plus additional edges for unmatched vertices, and each unmatched vertex gets one edge to a matched vertex. So matched vertices can be covered 1 or 2 times, unmatched vertices covered once.

Hmm, actually in a minimum edge cover, each vertex is covered at least once, and the cover has n - ν edges. The structure: take a maximum matching M (ν edges, 2ν vertices), then for each of the n - 2ν unmatched vertices, add one edge connecting it to a matched vertex. Total: ν + (n - 2ν) = n - ν edges.

In this structure, each unmatched vertex is covered once, and each matched vertex is covered once (by matching edge) plus possibly more (by edges to unmatched vertices). 

Sum over edges in C of (deg(u)+deg(v)): each matched vertex v appears in its matching edge (contributing deg(v)) and in k_v additional edges (where k_v is the number of unmatched vertices assigned to v), contributing k_v · deg(v). Each unmatched vertex u appears once, contributing deg(u).

So Σ_{uv∈C}(deg(u)+deg(v)) = Σ_{matched v} (1 + k_v) deg(v) + Σ_{unmatched u} deg(u).

And this is ≤ 100|C| = 100(n - ν).

Also, 2|E| = Σ_{matched v} deg(v) + Σ_{unmatched u} deg(u).

So Σ_{matched v} (1+k_v) deg(v) + Σ_{unmatched u} deg(u) ≤ 100(n-ν).
2|E| + Σ_{matched v} k_v deg(v) ≤ 100(n-ν).
2|E| ≤ 100(n-ν) - Σ k_v deg(v).

Since Σ k_v = n - 2ν (total unmatched), and k_v ≥ 0.

To maximize 2|E|, we want Σ k_v deg(v) small and ν large (so n-ν small). 

If ν = 50 (perfect matching), n - ν = 50, k_v = 0 for all, 2|E| ≤ 5000, |E| ≤ 2500. 

If ν < 50, then n - ν > 50, but Σ k_v deg(v) > 0 (since there are unmatched vertices). The question is whether the tradeoff can favor |E| > 2500.

2|E| ≤ 100(n - ν) - Σ k_v deg(v).

With ν = 50 - t (t unmatched-pair count, so n - 2ν = 2t unmatched vertices), n - ν = 50 + t.
Σ k_v = 2t.
2|E| ≤ 100(50 + t) - Σ k_v deg(v) = 5000 + 100t - Σ k_v deg(v).

For |E| > 2500, need 100t > Σ k_v deg(v), i.e., Σ k_v deg(v) < 100t, i.e., average deg of the vertices v (weighted by k_v) < 100. 

Hmm, but deg(v) could be less than 100. In fact, the matched vertices v that have k_v > 0 are adjacent to unmatched vertices via triangle-free edges, so deg(v) + deg(unmatched) ≤ 100, meaning deg(v) ≤ 100 - deg(unmatched) < 100 (if unmatched has deg > 0, which it does since it has at least the triangle-free edge).

But this doesn't immediately give us the bound. Let me think more.

Let me denote the unmatched vertices as u_1, ..., u_{2t} and they're assigned to matched vertices. Each u_j is assigned to some matched vertex v_{a(j)} via a triangle-free edge, with deg(u_j) + deg(v_{a(j)}) ≤ 100.

Σ k_v deg(v) = Σ_j deg(v_{a(j)}).

2|E| ≤ 5000 + 100t - Σ_j deg(v_{a(j)}).

Also, 2|E| = Σ_{matched} deg(v) + Σ_j deg(u_j) + Σ_{other matched not in cover...} wait, all matched vertices are in the matching. Let me re-denote.

Let me split: matched vertices (2ν = 100 - 2t of them) and unmatched (2t of them).
2|E| = Σ_{matched v} deg(v) + Σ_{unmatched u} deg(u).

From the matching edges: for each matching edge vv', deg(v) + deg(v') ≤ 100. Sum: Σ_{matched v} deg(v) ≤ 100ν = 100(50-t) = 5000 - 100t.

From the cover edges for unmatched: deg(u_j) + deg(v_{a(j)}) ≤ 100. Sum: Σ_j deg(u_j) + Σ_j deg(v_{a(j)}) ≤ 100 · 2t = 200t.

So Σ_j deg(u_j) ≤ 200t - Σ_j deg(v_{a(j)}).

2|E| = Σ_{matched} deg(v) + Σ_j deg(u_j) ≤ (5000 - 100t) + (200t - Σ_j deg(v_{a(j)})) = 5000 + 100t - Σ_j deg(v_{a(j)}).

Same as before. Now, Σ_j deg(v_{a(j)}) ≥ ? Each v_{a(j)} is a matched vertex with deg(v_{a(j)}) ≥ 1. But we need a better lower bound.

Note: deg(v_{a(j)}) ≥ deg(u_j) is not necessarily true. But we know deg(v_{a(j)}) ≥ 1 (it has at least the matching edge and the cover edge).

Hmm, we need Σ_j deg(v_{a(j)}) ≥ 100t to get 2|E| ≤ 5000. Is this true?

Σ_j deg(v_{a(j)}) = Σ_v k_v deg(v) where Σ k_v = 2t. We need this ≥ 100t = 50 · 2t. So we need the k_v-weighted average of deg(v) ≥ 50.

Is this guaranteed? Not obviously. A matched vertex v with high k_v could have low degree.

But wait: v is a matched vertex, so it's in a matching edge vv' with deg(v) + deg(v') ≤ 100. Also v has k_v unmatched vertices assigned to it, each via a triangle-free edge, so deg(v) + deg(u_j) ≤ 100 for each. 

Hmm, deg(v) could be small. E.g., deg(v) = 1 (just the matching edge), and v' has deg 99. Then v could be assigned many unmatched vertices? deg(v) + deg(u_j) ≤ 100, so deg(u_j) ≤ 99. But v has degree 1, meaning v is only adjacent to v'. But the triangle-free edge from u_j to v requires u_j adjacent to v. So v must be adjacent to u_j, meaning deg(v) ≥ 1 + k_v. So deg(v) ≥ 1 + k_v.

So if v has k_v unmatched vertices assigned, deg(v) ≥ 1 + k_v (matching edge + k_v cover edges). And deg(v) + deg(v') ≤ 100, deg(v) + deg(u_j) ≤ 100.

So Σ_v k_v deg(v) ≥ Σ_v k_v (1 + k_v) = Σ k_v + Σ k_v^2 = 2t + Σ k_v^2.

By Cauchy-Schwarz, Σ k_v^2 ≥ (Σ k_v)^2 / (number of v with k_v > 0) ≥ (2t)^2 / (2t) = 2t (if all k_v = 1). So Σ k_v deg(v) ≥ 2t + 2t = 4t.

We need Σ k_v deg(v) ≥ 100t. But we only have ≥ 4t. Not enough!

So this approach doesn't prove |E| ≤ 2500. Maybe the answer is NOT 2500?

Let me reconsider. Maybe we can beat 2500. Let me try to construct a graph with more than 2500 edges.

Idea: Use a star-like structure. Take one vertex v connected to many low-degree vertices, and a large clique elsewhere.

Let me try a concrete construction. 

Construction: 
- Take a clique K_{99} on vertices 1,...,99.
- Vertex 0 is connected to vertex 1 only.
- Edge 0-1: N(0) = {1}, N(1) = {0, 2, 3, ..., 99}. N(0)∩N(1) = {1}∩N(1). 1 ∉ N(1), so intersection = ∅. Triangle-free! ✓
- Vertex 0 has triangle-free edge 0-1. ✓
- Vertex 1 has triangle-free edge 1-0. ✓
- Vertices 2,...,99 (98 vertices): each is in K_{99}, every edge in a triangle. They need triangle-free edges, but all their edges are in K_{99} (triangles). No triangle-free edge. ✗

So this fails for 98 vertices. We need to give each of them a triangle-free edge.

Modified construction: 
- Take a clique K_k on k vertices (the "core").
- Have 100 - k "pendant" vertices, each connected to exactly one core vertex via a triangle-free edge.
- Each core vertex can have at most one pendant (because if core vertex c has two pendants p, q, then edges cp and cq: cp is triangle-free requires N(c)∩N(p)=∅. N(p)={c}, so N(c)∩{c}=∅ ✓. Similarly cq. But does c still have a triangle-free edge? c's triangle-free edge could be cp (N(c)∩N(p)=∅ ✓). But wait, we need to check: is cp still triangle-free if c is also adjacent to q? N(p) = {c}, N(c) includes q. N(c)∩N(p) = N(c)∩{c} = ∅. Still triangle-free. ✓. So c can have multiple pendants.

But the pendants: p has triangle-free edge pc ✓. q has triangle-free edge qc ✓. 

Now, the core vertices: each needs a triangle-free edge. If core vertex c has a pendant p, then cp is triangle-free ✓. But if core vertex c has NO pendant, then c needs a triangle-free edge within the core. In a clique K_k (k ≥ 3), no edge is triangle-free. So every core vertex needs a pendant.

So we need at least k pendants, one for each core vertex. Total vertices: k + (number of pendants) ≥ k + k = 2k ≤ 100, so k ≤ 50.

With k = 50: 50 core vertices (K_50), 50 pendants (each connected to one core vertex). Edges: C(50,2) + 50 = 1225 + 50 = 1275. Worse than 2500.

But wait, can pendants have edges among themselves? If pendant p (connected to core vertex c_p) and pendant q (connected to core vertex c_q) are adjacent: does this break triangle-free edges? 

Edge c_p p: N(c_p) ∩ N(p) = ∅. N(p) now includes c_p and q. N(c_p) includes all core vertices and pendants assigned to c_p. For N(c_p)∩N(p) = ∅: q ∉ N(c_p) (i.e., c_p not adjacent to q, which is true if q is a pendant of c_q ≠ c_p and c_p is not adjacent to q). Also c_p ∉ N(p)? No, c_p ∈ N(p) but c_p ∉ N(c_p). And any other neighbor of p must not be in N(c_p).

If we add edges among pendants, we need to be careful. Let me think about making pendants form a clique.

If all 50 pendants form a clique: pendant p (assigned to c_p) has neighbors: c_p and all other 49 pendants. N(p) = {c_p} ∪ {other pendants}. N(c_p) = {other 49 core vertices} ∪ {p} (and possibly other pendants assigned to c_p). 

N(c_p) ∩ N(p): N(c_p) contains other core vertices and p. N(p) contains c_p and other pendants. Intersection: do any core vertices (other than c_p) appear in N(p)? N(p) = {c_p, other pendants}. No core vertices except c_p. And c_p ∉ N(c_p). And p ∈ N(c_p) but p ∉ N(p). So intersection = ∅? Wait, N(c_p) = {core vertices except c_p} ∪ {p} ∪ {other pendants assigned to c_p}. N(p) = {c_p} ∪ {other 49 pendants}. 

Intersection: {core except c_p} ∪ {p} ∪ {assigned pendants} ∩ {c_p} ∪ {49 pendants}. 
- {core except c_p} ∩ {c_p} = ∅, {core except c_p} ∩ {49 pendants} = ∅ (pendants aren't core). 
- {p} ∩ {c_p} = ∅, {p} ∩ {49 pendants} = ∅ (p not in other pendants). 
- {assigned pendants} ∩ {c_p} = ∅, {assigned pendants} ∩ {49 pendants}: if c_p has other pendants assigned, they'd be in the 49 pendants. So intersection includes those!

So if c_p has only one pendant (p), then {assigned pendants} = {p}, and intersection with {49 pendants} = ∅ (since p ∉ {49 other pendants}). So N(c_p) ∩ N(p) = ∅. ✓

So with each core vertex having exactly one pendant, and pendants forming a clique, and core forming a clique:
- Core: K_50, edges = C(50,2) = 1225.
- Pendants: K_50, edges = C(50,2) = 1225.
- Matching: 50 edges.
- Total = 2500. Same as before!

And we already showed cross edges (beyond matching) break triangle-free property. So 2500 again.

But can we do better with a non-clique structure? Let me think about the earlier tree component idea more carefully.

Let me try to construct a graph with > 2500 edges.

Idea: Have some vertices with very high degree (close to 99) paired with very low degree vertices, and a large dense subgraph.

Let me try: 
- 2 vertices a, b with edge ab triangle-free. deg(a) = 99, deg(b) = 1. 
  - a adjacent to all 99 others. b adjacent to only a.
  - N(a) ∩ N(b) = N(a) ∩ {a} = ∅ ✓ (since a ∉ N(a)).
  - a's triangle-free edge: ab ✓. b's triangle-free edge: ba ✓.
- But the other 98 vertices: each is adjacent to a. For vertex w (w ≠ a, b), w needs a triangle-free edge. w is adjacent to a. If w's triangle-free edge is wx, then N(w)∩N(x) = ∅. Since a ∈ N(w), we need a ∉ N(x), so x is not adjacent to a. But a is adjacent to everyone. So x must be... a is adjacent to all 99 others, so everyone is adjacent to a. Thus a ∈ N(x) for all x ≠ a. So no x can be a triangle-free partner for w (since a ∈ N(w) ∩ N(x)). Unless x = a, but then edge wa: N(w)∩N(a) must be ∅, but N(a) is huge. No.

So deg(a) = 99 doesn't work because it "blocks" all other vertices from having triangle-free edges. 

The issue: if a is adjacent to both w and x, then a ∈ N(w) ∩ N(x), so wx can't be triangle-free. So if a vertex a is adjacent to a set S of vertices, no two vertices in S can have a triangle-free edge between them (since a is a common neighbor). Moreover, for w ∈ S, w's triangle-free partner x must satisfy a ∉ N(x), i.e., x ∉ S and x ≠ a. So x must be outside S ∪ {a}.

So if a has high degree, the neighbors of a must find triangle-free partners outside N(a) ∪ {a}. The non-neighbors of a (excluding a itself) are 100 - 1 - deg(a) = 99 - deg(a) vertices.

Each neighbor of a needs a triangle-free partner among the 99 - deg(a) non-neighbors of a. Each non-neighbor x can serve as triangle-free partner for multiple neighbors of a (as long as the edges are triangle-free). But there are constraints.

This is getting complicated. Let me try to think about it computationally for small cases to guess the pattern.

Actually, let me think about the problem differently. Let me consider the general problem: n vertices, each vertex has a triangle-free edge, maximize edges.

For n = 2: only edge is the edge itself, triangle-free. 1 edge. 
For n = 4: two K_2's + ... or K_2 + K_2 with cross edges? Matching construction: two pairs, K_2 + K_2 + 2 cross = 4 edges. Or: K_4 has 6 edges but no triangle-free edge (every edge in triangle). Remove edges to get triangle-free edges. 

For n = 4, matching construction: a1a2, b1b2 (cliques of size 2 = single edges), matching a1b1, a2b2. Edges: 1 + 1 + 2 = 4. But can we do better? K_4 minus one edge = 5 edges. Does every vertex have a triangle-free edge? K_4 - {cd}: vertices a,b,c,d. Edges: ab, ac, ad, bc, bd. (missing cd). 
- a: neighbors b,c,d. Edge ab: N(a)={b,c,d}, N(b)={a,c,d}. Intersection {c,d} ≠ ∅. Edge ac: N(a)∩N(c) = {b,c,d}∩{a,b,d} = {b,d} ≠ ∅. Edge ad: N(a)∩N(d)={b,c,d}∩{a,b,c}={b,c}≠∅. No triangle-free edge for a. ✗.

K_4 minus two edges: say remove cd and one more. K_4 - {cd, bd}: edges ab, ac, ad, bc. 
- a: N(a)={b,c,d}. Edge ab: N(b)={a,c}. N(a)∩N(b)={c}≠∅. Edge ad: N(d)={a}. N(a)∩N(d)={b,c,d}∩{a}=∅ ✓. Triangle-free! 
- b: N(b)={a,c}. Edge bc: N(c)={a,b}. N(b)∩N(c)={a}≠∅. Edge ab: already checked, {c}≠∅. No triangle-free edge for b. ✗.

Hmm. K_4 - {cd, bc}: edges ab, ac, ad, bd. Wait that's the same as before by symmetry.

Let me try C_4 (cycle): edges ab, bc, cd, da. 4 edges. Each edge: ab, N(a)={b,d}, N(b)={a,c}. Intersection ∅ ✓. So every edge is triangle-free. 4 edges. Same as matching construction.

Can we get 5 edges on 4 vertices with the property? K_4 has 6, we need to remove at least 1. K_4 - 1 edge = 5, shown above doesn't work. So max for n=4 is 4 = n²/4. ✓ matches 2500 = 100²/4.

For n = 6: matching construction gives 2 K_3's + matching = 2·3 + 3 = 9 = 36/4. Can we beat 9?

K_6 has 15 edges. We need each vertex to have a triangle-free edge. 

Let me try: K_6 minus some edges. Actually let me think about whether n²/4 is always the answer.

Hmm, let me think about n = 6 more carefully. 

Construction: K_3 on {a1,a2,a3}, K_3 on {b1,b2,b3}, matching a1b1, a2b2, a3b3. Total: 3 + 3 + 3 = 9. Each matching edge is triangle-free (verified as before). ✓

Can we do 10? Let me try adding one more edge to the 9-edge construction, say a1b2. Then a1b1: N(a1) = {a2,a3,b1,b2}, N(b1) = {b2,b3,a1}. Intersection: {a2,a3,b1,b2}∩{b2,b3,a1} = {b2} ≠ ∅. So a1b1 no longer triangle-free. a1 needs another triangle-free edge. a1's edges: a1a2, a1a3, a1b1, a1b2. 
- a1a2: N(a1)∩N(a2). N(a2)={a1,a3,b2}. N(a1)={a2,a3,b1,b2}. Intersection: {a3,b2} ≠ ∅. 
- a1a3: N(a3)={a1,a2,b3}. Intersection with N(a1)={a2,a3,b1,b2}: {a2} ≠ ∅.
- a1b2: N(b2)={b1,b3,a2,a1}. Intersection with N(a1)={a2,a3,b1,b2}: {a2,b1} ≠ ∅.
No triangle-free edge for a1. ✗.

So adding a1b2 breaks it. What about a different 10-edge graph?

Let me try: K_6 minus 5 edges. 15 - 5 = 10. We need to remove edges so every vertex has a triangle-free edge.

Actually, let me think about it differently. The complement of our graph has 15 - |E| edges. For |E| = 10, complement has 5 edges.

A triangle-free edge uv in G means N_G(u) ∩ N_G(v) = ∅, i.e., no w is adjacent to both u and v in G. In complement terms: every w ≠ u,v is non-adjacent to u or non-adjacent to v in G, i.e., w is adjacent to u or v in complement. So in complement, every w ≠ u,v is adjacent to u or v. Plus u and v are non-adjacent in complement (since uv is an edge in G). So in complement, {u,v} is a non-edge, and every other vertex is adjacent to at least one of u,v. This means {u,v} is a dominating set in the complement (dominating every other vertex), and uv is a non-edge.

Hmm, this is an interesting reformulation but might not directly help.

Let me just try to see if 10 is achievable for n = 6 by brute force thinking.

Actually, let me try a different construction for n = 6. Instead of two equal cliques, try unequal.

3 vertices in group A (clique K_3), 3 in group B (clique K_3), but with a different cross structure. We showed cross edges must form a matching (for the two-clique construction). So max is 9.

What about non-clique-based? Let me try: take K_6 and remove a perfect matching (3 edges). 15 - 3 = 12 edges. The removed matching: say remove a1b1, a2b2, a3b3. Remaining: K_6 minus matching = complete tripartite? No, it's K_6 minus 3 disjoint edges.

In K_6 - M (M = perfect matching), does every vertex have a triangle-free edge? Take vertex a1. Its neighbors: a2, a3, b2, b3 (not b1, since a1b1 removed). Edge a1a2: N(a1) = {a2,a3,b2,b3}, N(a2) = {a1,a3,b1,b3}. Intersection: {a3, b3} ≠ ∅. Edge a1b2: N(b2) = {a1,a3,b1,b3}. Intersection with N(a1) = {a2,a3,b2,b3}: {a3,b3} ≠ ∅. Similarly all edges have common neighbors. No triangle-free edge. ✗.

So K_6 - M doesn't work. 

Let me try K_6 minus a star K_{1,3} (remove 3 edges incident to one vertex). Remove a1a2, a1a3, a1b1. 12 edges. Vertex a1: neighbors {b2, b3}. Edge a1b2: N(a1)={b2,b3}, N(b2)={a1,a2,a3,b1,b3}. Intersection: {b3} ≠ ∅. Edge a1b3: N(b3)={a1,a2,a3,b1,b2}. Intersection with N(a1)={b2,b3}: {b2} ≠ ∅. No triangle-free edge for a1. ✗.

Hmm. Let me try removing edges to create triangle-free edges. For an edge to be triangle-free, we need to remove all common neighbors. Edge ab is triangle-free if we remove all edges aw and bw for all w (i.e., no w is adjacent to both). 

For n = 6, to make edge ab triangle-free, for each of the other 4 vertices w, at least one of aw, bw must be removed. That's at least 4 removals (but one removal can cover one w). Actually for each w, remove aw or bw. 4 vertices, 4 removals minimum (each removal covers one w). But if we remove aw, that also helps make other edges triangle-free.

This is like a covering problem. Let me think about it as: we want to select a set of triangle-free edges (forming an edge cover) and remove edges to make them triangle-free, while keeping as many edges as possible.

For the matching construction on n = 6: 3 triangle-free edges (matching), each requiring 4 removals from K_6, but removals can overlap. Total edges = 15 - (removals). Matching construction gives 9, so 6 removals. 

Can we do fewer removals? With 5 removals, 10 edges. Let's see if possible.

3 matching edges a1b1, a2b2, a3b3. For a1b1 triangle-free: for w ∈ {a2,a3,b2,b3}, remove a1w or b1w. For a2b2: w ∈ {a1,a3,b1,b3}, remove a2w or b2w. For a3b3: w ∈ {a1,a2,b1,b2}, remove a3w or b3w.

We need to choose removals to satisfy all three, minimizing total removals. Each removal is one edge.

For a1b1: need to cover {a2,a3,b2,b3}. 
For a2b2: need to cover {a1,a3,b1,b3}.
For a3b3: need to cover {a1,a2,b1,b2}.

A single removal like a1a2 covers: a2 for edge a1b1 (since a1a2 removed, a2 not adjacent to a1, so a2 not common neighbor of a1,b1 ✓), and a1 for edge a2b2 (since a1a2 removed, a1 not adjacent to a2 ✓). So a1a2 removal covers a2 in constraint 1 and a1 in constraint 2. 

Similarly, a removal of edge xy where x is in one pair and y in another covers two constraints.

Let me think of it as a problem on K_{3,3} (the cross edges between pairs). The cross edges are a_i a_j, a_i b_j, b_i a_j, b_i b_j for i ≠ j. There are 3·3·... wait, 3 pairs, cross edges between different pairs: for each pair of pairs (i,j), 4 edges. C(3,2) = 3 pair-pairs, 4 edges each = 12 cross edges. Plus 3 matching edges + within-pair edges (0, since pairs are size 2, no within-pair edges except matching). Wait, in the matching construction for n=6, the "cliques" are K_3 on a's and K_3 on b's. So within-a edges: a1a2, a1a3, a2a3 (3 edges). Within-b: b1b2, b1b3, b2b3 (3 edges). Cross: matching a1b1, a2b2, a3b3 (3 edges). Total: 3+3+3 = 9.

To make a1b1 triangle-free: no common neighbor. a1's neighbors (in full K_6): a2, a3, b1, b2, b3. b1's neighbors: a1, a2, a3, b2, b3. Common: a2, a3, b2, b3. To make triangle-free, remove a1's or b1's edge to each of a2, a3, b2, b3. 

In the matching construction, we remove ALL cross edges except matching. So we remove a1a2? No wait, a1a2 is a within-a edge, kept. We remove a1b2, a1b3, b1a2, b1a3 (cross edges). That's 4 removals for a1b1. But a1a2 and a1a3 are kept (within-a clique), and b1a2 = a2b1 is a cross edge, removed. So common neighbors of a1 and b1: a2 (a1-a2 kept, b1-a2 removed → a2 not common), a3 (similar), b2 (a1-b2 removed), b3 (a1-b3 removed). So no common neighbors. ✓. 4 removals for this edge.

But these removals also help other edges. a1b2 removed helps a2b2 (removes a1 as potential common neighbor of a2,b2). 

Total removals in matching construction: all 12 cross edges minus 3 matching = 9 removals. 15 - 9 = 6... wait that gives 6, not 9. 

Oh wait, I'm confusing myself. K_6 has 15 edges. Matching construction has 9 edges. So 6 removals. The 6 removals are the 9 non-matching cross edges... no. Cross edges: 12 (4 per pair-pair × 3 pair-pairs). Matching: 3. Non-matching cross: 9. But we only remove 6 edges (15 - 9 = 6). 

Hmm, I think I miscounted. In the matching construction, the edges are: within-a (3) + within-b (3) + matching (3) = 9. The removed edges are: cross non-matching = 15 - 9 = 6. But I said there are 9 non-matching cross edges. 12 cross total - 3 matching = 9 non-matching cross. But 15 - 9 = 6. Contradiction. 

Oh I see the issue: 15 total edges = 3 (within-a) + 3 (within-b) + 3 (matching) + 6 (non-matching cross). Wait: within-a = C(3,2) = 3, within-b = 3, cross = 3×3 = 9 (each a to each b), matching = 3 of those 9, non-matching cross = 6. Total = 3 + 3 + 9 = 15. ✓. Kept: 3 + 3 + 3 = 9. Removed: 6 (non-matching cross). ✓.

OK so 6 removals. Can we do 5 removals (10 edges)?

We need 3 triangle-free edges covering all 6 vertices (edge cover, but actually we need every vertex to have a triangle-free edge, so we need an edge cover of triangle-free edges). With 3 matching edges, we need each to be triangle-free. 

For a1b1 triangle-free: remove edges so no common neighbor. Common neighbors of a1,b1 in K_6: {a2,a3,b2,b3}. For each, remove one of the two edges. 4 vertices, but some removals can be shared with other constraints.

For a2b2: common neighbors {a1,a3,b1,b3}. 
For a3b3: common neighbors {a1,a2,b1,b2}.

Let me see if 5 removals suffice. We need to "hit" all common neighbor relationships.

Consider removing: a1b2, a1b3, a2b1, a2b3, a3b1, a3b2. That's 6 removals (all non-matching cross edges). Can we keep one more?

Say we keep a1b2 (don't remove it). Then for a1b1 triangle-free: b2 is a common neighbor if b1-b2 is an edge (yes, within-b clique) and a1-b2 is an edge (yes, we kept it). So b2 is a common neighbor. To fix, remove b1b2 (within-b edge). But removing b1b2 might break b1 or b2's triangle-free edge.

If we remove b1b2 and keep a1b2: 
- a1b1: common neighbors? a2 (a1-a2 yes, b1-a2 = a2b1, removed ✓ not common), a3 (a1-a3 yes, b1-a3 = a3b1, removed ✓), b2 (a1-b2 yes, b1-b2 removed ✓), b3 (a1-b3 removed ✓). No common neighbors. ✓
- a2b2: common neighbors? a1 (a2-a1 yes, b2-a1 = a1b2, kept! so a1 is common if a2-a1 and b2-a1 both edges. a2-a1 yes, b2-a1 = a1b2 yes. Common! ✗.

So a1 is a common neighbor of a2 and b2. To fix, remove a1a2 or a1b2. But we wanted to keep a1b2. Remove a1a2? Then a1's neighbors change. 

This is getting complicated. Let me just try to check computationally whether 10 is possible for n=6.

Actually, let me think about it more cleverly. The question is whether n²/4 is the answer.

Let me consider the problem from the perspective of Turán-type results. 

Actually, I recall a similar problem: "every edge is in at most one triangle" or "every vertex has a pendant edge" type conditions. But this is different.

Let me think about the upper bound more carefully.

Key lemma: For each vertex u, let v be its witness (triangle-free edge uv). Then deg(u) + deg(v) ≤ n.

Now, consider the witness function f. Build the functional graph. 

I want to prove Σ deg(u) ≤ n²/2, i.e., |E| ≤ n²/4.

Let me try a different approach. Consider the graph H on V where we connect u to f(u) for each u (the witness edges). H is a spanning subgraph (edge cover) with each vertex having outdegree 1 (directed) or degree ≥ 1 (undirected).

For each edge uv in H (meaning f(u)=v or f(v)=u), we have deg_G(u) + deg_G(v) ≤ n.

Now, H is a graph (ignoring direction) where every vertex has degree ≥ 1. H has at most n edges (since outdegree 1 gives n directed edges, at most n undirected edges).

Actually, H has exactly n directed edges, so at most n undirected edges (could be fewer if 2-cycles). 

We want to bound Σ_{v} deg_G(v) = 2|E|.

Consider the sum Σ_{u} (deg_G(u) + deg_G(f(u))) ≤ n² (summing deg(u)+deg(f(u)) ≤ n over all n vertices).

Σ_u deg_G(u) + Σ_u deg_G(f(u)) ≤ n².
2|E| + Σ_u deg_G(f(u)) ≤ n².

Now Σ_u deg_G(f(u)) = Σ_v deg_G(v) · indeg(v) where indeg is indegree in the functional graph.

So 2|E| + Σ_v deg_G(v) · indeg(v) ≤ n².

We need to show 2|E| ≤ n²/2, i.e., Σ_v deg_G(v) · indeg(v) ≥ n²/2 - ... hmm, we need 2|E| ≤ n²/2, so Σ_v deg(v)·indeg(v) ≥ n² - n²/2 = n²/2. 

Is Σ_v deg(v)·indeg(v) ≥ n²/2? We have Σ indeg(v) = n. By Cauchy-Schwarz or rearrangement... 

Σ_v deg(v)·indeg(v) ≥ (Σ_v deg(v))(Σ_v indeg(v)) / n = (2|E| · n) / n = 2|E| if deg and indeg are "aligned". But that's not generally true.

Actually, by the rearrangement inequality, Σ deg(v)·indeg(v) is minimized when one is sorted ascending and the other descending. We can't bound it below without more info.

Hmm. Let me try yet another approach.

Let me think about it as an optimization problem. We want to maximize Σ deg(v) subject to:
- There exists f: V → V such that for each u, f(u) ∈ N(u), N(u) ∩ N(f(u)) = ∅.
- Equivalently, deg(u) + deg(f(u)) ≤ n for each u (necessary condition; the disjoint neighborhood condition is stronger but let's use this necessary condition for an upper bound).

So we want to maximize Σ deg(v) subject to: there exists a function f where each u maps to a neighbor, and deg(u) + deg(f(u)) ≤ n.

Wait, but we also need f(u) to be a neighbor, which means the degree sequence must be realizable with the graph structure. Let me just use the necessary condition deg(u) + deg(f(u)) ≤ n and see what upper bound it gives.

This is a pure optimization: given n values deg(1),...,deg(n) and a function f with deg(i) + deg(f(i)) ≤ n for all i, maximize Σ deg(i).

The function f defines a functional graph. To maximize Σ deg, we want to choose f and deg values optimally.

For a 2-cycle (i ↔ j): deg(i) + deg(j) ≤ n. Contribution: ≤ n for 2 vertices.
For a fixed point: deg(i) + deg(i) ≤ n, so deg(i) ≤ n/2. Contribution: ≤ n/2 for 1 vertex. (But fixed point means f(i) = i, i.e., i is its own neighbor, which requires a self-loop. Not allowed in simple graph! So no fixed points.)

For a k-cycle (k ≥ 3): deg(v_i) + deg(v_{i+1}) ≤ n. Sum: 2Σ deg ≤ kn, Σ deg ≤ kn/2. Contribution: ≤ kn/2 for k vertices, avg n/2.

For a tree: root v (in a cycle) with child u: deg(u) + deg(v) ≤ n. If deg(v) = d, deg(u) ≤ n - d. Grandchild w: deg(w) + deg(u) ≤ n, deg(w) ≤ n - deg(u) ≤ d. Etc.

For a path v → u → w (f(v)=u, f(u)=w, and w is in a cycle or has its own f): deg(v)+deg(u) ≤ n, deg(u)+deg(w) ≤ n. So deg(v) ≤ n - deg(u), deg(w) ≤ n - deg(u). Sum deg(v)+deg(u)+deg(w) ≤ (n - deg(u)) + deg(u) + (n - deg(u)) = 2n - deg(u). Maximized when deg(u) is minimized. deg(u) ≥ 1 (at least one edge, to v and w). If deg(u) = 1... but u is adjacent to both v and w (since f(v)=u means v adjacent to u, and f(u)=w means u adjacent to w). So deg(u) ≥ 2. Sum ≤ 2n - 2. For n = 100, that's 198 for 3 vertices, avg 66 > 50.

But wait, can deg(u) = 2 with u adjacent to v and w only? Then deg(v) ≤ 98, deg(w) ≤ 98. Sum = 98 + 2 + 98 = 198. 

But we also need the actual graph to realize these degrees with the triangle-free condition (not just the degree sum condition). The degree sum is necessary but not sufficient. Let me check if this is actually realizable.

Let me try to construct: n = 100. 
- u: adjacent to v and w only. deg(u) = 2.
- v: adjacent to u and 97 others (not w). deg(v) = 98.
- w: adjacent to u and 97 others (not v). deg(w) = 98.
- f(v) = u, f(u) = w. 
  - Edge vu: N(v) ∩ N(u) = ∅. N(u) = {v, w}. N(v) = {u, 97 others}. Intersection: {v,w} ∩ {u, 97 others}. v ∉ N(v), w: is w ∈ N(v)? v not adjacent to w, so w ∉ N(v). So intersection = ∅ ✓ (if the 97 others don't include w, which they don't since v not adjacent to w).
  - Edge uw: N(u) ∩ N(w) = ∅. N(u) = {v, w}. N(w) = {u, 97 others}. Intersection: {v,w} ∩ {u, 97 others}. w ∉ N(w), v: is v ∈ N(w)? w not adjacent to v, so v ∉ N(w). Intersection = ∅ ✓.
- v's witness is u (triangle-free ✓). u's witness is w (triangle-free ✓). w needs a witness too!
- w has deg 98, adjacent to u and 97 others. w's triangle-free edge: needs partner x with deg(x) + deg(w) ≤ 100, so deg(x) ≤ 2. And N(w) ∩ N(x) = ∅. x must be adjacent to w (x ∈ N(w)). x has deg ≤ 2, so x is adjacent to w and at most 1 other. N(x) ⊆ {w, one other}. N(w) = {u, 97 others}. N(w) ∩ N(x): if x's other neighbor is y, then y ∈ N(x) and we need y ∉ N(w). But N(w) has 98 vertices. y ∉ N(w) means y is one of the 2 vertices not adjacent to w: those are v and... w itself (but w ∉ N(w)). So y = v. So x is adjacent to w and v. deg(x) = 2. N(x) = {w, v}. N(w) ∩ N(x) = {u, 97 others} ∩ {w, v} = ∅ (since v ∉ N(w), w ∉ N(w)). ✓!

So x is adjacent to w and v, deg(x) = 2. f(w) = x. Edge wx is triangle-free. ✓.

Now x needs a witness. x is adjacent to w and v. deg(x) = 2. x's triangle-free edge: partner y with deg(y) ≤ 98 and N(x) ∩ N(y) = ∅. N(x) = {w, v}. y must be adjacent to x, so y ∈ {w, v}. 
- y = w: deg(w) = 98, deg(x) + deg(w) = 100 ≤ 100 ✓. N(x) ∩ N(w) = ∅ ✓ (shown above). So f(x) = w. But then x → w → x is a 2-cycle. ✓.

So we have a 2-cycle w ↔ x, and v → u → w. Wait, let me re-examine. f(v) = u, f(u) = w, f(w) = x, f(x) = w. So w → x → w is a 2-cycle, and v → u → w is a tree feeding into the cycle.

Degrees: deg(v) = 98, deg(u) = 2, deg(w) = 98, deg(x) = 2. Sum = 200 for 4 vertices, avg 50. Hmm, same as matching!

Let me see: v and w have high degree (98), u and x have low degree (2). The sum is 200 = 50 × 4. So even though the tree structure allows higher individual sums, the constraint brings the average to 50.

Wait, let me recheck. v → u → w → x → w (cycle). Constraints:
- deg(v) + deg(u) ≤ 100: 98 + 2 = 100 ✓.
- deg(u) + deg(w) ≤ 100: 2 + 98 = 100 ✓.
- deg(w) + deg(x) ≤ 100: 98 + 2 = 100 ✓.
- deg(x) + deg(w) ≤ 100: 2 + 98 = 100 ✓.
Sum = 200 = 50 × 4. 

Can we make the sum higher? deg(v) + deg(u) ≤ 100 and deg(u) + deg(w) ≤ 100. If deg(u) = 2 (minimum, since u adjacent to v and w), then deg(v) ≤ 98, deg(w) ≤ 98. And deg(w) + deg(x) ≤ 100, deg(x) ≥ 2 (adjacent to w and v), so deg(w) ≤ 98. Sum = deg(v) + deg(u) + deg(w) + deg(x) ≤ 98 + 2 + 98 + 2 = 200. Exactly 50 × 4.

What if the tree is longer? v → u → w → x → y → ... Each tree vertex has degree ≥ 2 (adjacent to parent and child in the functional graph), and the constraint alternates. Let me think about a path of length k feeding into a 2-cycle.

Path: v_1 → v_2 → v_3 → ... → v_k → c_1 ↔ c_2 (2-cycle).
Constraints: deg(v_i) + deg(v_{i+1}) ≤ 100, deg(v_k) + deg(c_1) ≤ 100, deg(c_1) + deg(c_2) ≤ 100.
Each v_i (i < k) has degree ≥ 2 (adjacent to v_{i-1} and v_{i+1} in functional graph, meaning edges v_i v_{i+1} and v_{i-1} v_i... wait, f(v_i) = v_{i+1} means v_i is adjacent to v_{i+1}. And f(v_{i-1}) = v_i means v_{i-1} adjacent to v_i. So v_i is adjacent to v_{i-1} and v_{i+1}, deg(v_i) ≥ 2.

Sum of degrees along the path + cycle: this is a path graph of constraints. The constraint graph is a path v_1 - v_2 - ... - v_k - c_1 - c_2 (with c_1 - c_2 being the cycle edge, and also c_2 - c_1 but that's the same constraint).

Actually the constraint graph (where edges represent "deg sum ≤ 100") is: v_1-v_2, v_2-v_3, ..., v_k-c_1, c_1-c_2. This is a path of length k+1 (k+2 vertices). 

Maximizing Σ deg subject to deg(i) + deg(j) ≤ 100 for each edge in this path, and deg(v_i) ≥ 2 for internal vertices, deg(c_1) ≥ 2, deg(c_2) ≥ 1 (adjacent to c_1), deg(v_1) ≥ 1 (adjacent to v_2).

For a path of m vertices with constraints deg(i)+deg(i+1) ≤ 100, the max sum is:
- If m even: 50m (pair up, each pair sums to 100).
- If m odd: 50m (the middle vertex can be 50, others pair up). Actually for odd m, max sum = 50m as well (set all to 50, or alternate 100/0 but with lower bounds).

Wait, for a path of m vertices with deg(i)+deg(i+1) ≤ 100, the max sum is 50m if m is even, and 50m if m is odd (set middle to 50, alternate 0/100 on both sides, but with lower bounds it's slightly less). Actually without lower bounds, for odd m, max = 50m (e.g., m=3: deg1=100, deg2=0, deg3=100, sum=200=50·4... no that's 50·4 not 50·3. Wait m=3: 100+0+100 = 200, but 50·3 = 150. So 200 > 150!

Hmm wait, for a path of 3 vertices with constraints deg1+deg2 ≤ 100, deg2+deg3 ≤ 100: max sum = deg1 + deg2 + deg3. Set deg2 = 0, deg1 = deg3 = 100. Sum = 200. But 50·3 = 150. So 200 > 150!

But we have lower bounds: deg2 ≥ 2 (internal vertex). So deg1 ≤ 98, deg3 ≤ 98, deg2 ≥ 2. Sum ≤ 98 + 2 + 98 = 198. Still > 150.

So a path of 3 vertices can have sum 198, avg 66 > 50! This suggests we might beat n²/4!

But wait, we need to actually realize this in a graph. The degree sum condition is necessary but not sufficient. Let me try to construct a graph realizing this.

Let me try with n = 6. Path: v1 → v2 → v3, with v3 in a 2-cycle with v4. So 4 vertices in this component, and 2 more vertices elsewhere.

Actually, let me think about n = 6 with the path structure.

Component 1: v1 → v2 → v3 ↔ v4 (2-cycle). 4 vertices.
Component 2: v5 ↔ v6 (2-cycle). 2 vertices.

Constraints:
- deg(v1) + deg(v2) ≤ 6, deg(v2) + deg(v3) ≤ 6, deg(v3) + deg(v4) ≤ 6, deg(v5) + deg(v6) ≤ 6.

Lower bounds: deg(v2) ≥ 2, deg(v3) ≥ 2, deg(v4) ≥ 1, deg(v1) ≥ 1, deg(v5) ≥ 1, deg(v6) ≥ 1.

Max sum: 
- v1 + v2 ≤ 6, v2 + v3 ≤ 6, v3 + v4 ≤ 6. With v2 ≥ 2, v3 ≥ 2.
  - Set v2 = 2, v1 = 4, v3 = 4, v4 = 2. Sum = 4+2+4+2 = 12. Or v2 = 2, v1 = 4, v3 = 4, v4 = 2. 
  - Or v2 = 2, v3 = 2, v1 = 4, v4 = 4. Sum = 4+2+2+4 = 12.
  - Max: v1 + v2 + v3 + v4 with v1+v2≤6, v2+v3≤6, v3+v4≤6. Set v2=v3=2: v1≤4, v4≤4, sum ≤ 12. Set v2=2,v3=4: v1≤4,v4≤2, sum ≤ 12. Set v2=4,v3=2: v1≤2,v4≤4, sum ≤ 12. Always 12 = 3·4 = 3·n. Hmm, 12 for 4 vertices, avg 3 = n/2.
- v5 + v6 ≤ 6. Sum ≤ 6, avg 3 = n/2.

Total: 12 + 6 = 18 = 6·3 = n·(n/2) = n²/2. So 2|E| ≤ 18, |E| ≤ 9 = n²/4. 

Interesting! So for n = 6, even with the path structure, we get |E| ≤ 9. The path didn't help because the lower bounds on internal vertices ate up the gain.

Let me recheck for n = 100. Path of 3: v1 → v2 → v3, with v3 in 2-cycle with v4. Constraints: deg(v1)+deg(v2) ≤ 100, deg(v2)+deg(v3) ≤ 100, deg(v3)+deg(v4) ≤ 100. Lower bounds: deg(v2) ≥ 2, deg(v3) ≥ 2.

Max sum of v1+v2+v3+v4: 
Let d2 = deg(v2), d3 = deg(v3). d2 ≥ 2, d3 ≥ 2, d2 + d3 ≤ 100.
v1 ≤ 100 - d2, v4 ≤ 100 - d3.
Sum ≤ (100 - d2) + d2 + d3 + (100 - d3) = 200. 

So sum = 200 regardless of d2, d3 (as long as constraints satisfied). 200 for 4 vertices = 50 × 4. Same as two 2-cycles (each giving 100 for 2 vertices, total 200 for 4).

So the path doesn't help! The sum is always 200 = 50 × 4, same as matching.

Let me verify: two 2-cycles give 100 + 100 = 200 for 4 vertices. Path + 2-cycle gives 200 for 4 vertices. Same!

What about a longer path? v1 → v2 → v3 → v4 → v5 ↔ v6. 6 vertices.
Constraints: d1+d2 ≤ 100, d2+d3 ≤ 100, d3+d4 ≤ 100, d4+d5 ≤ 100, d5+d6 ≤ 100.
Lower bounds: d2 ≥ 2, d3 ≥ 2, d4 ≥ 2, d5 ≥ 2, d1 ≥ 1, d6 ≥ 1.
Sum = d1+d2+d3+d4+d5+d6.
d1 ≤ 100-d2, d6 ≤ 100-d5.
Sum ≤ (100-d2) + d2 + d3 + d4 + d5 + (100-d5) = 200 + d3 + d4.
But d3 + d4 ≤ 100. So sum ≤ 300 = 50 × 6. ✓

And with d3 = d4 = 2 (minimum): sum = 200 + 4 = 204 < 300. With d3 + d4 = 100: sum = 300. But d3 ≥ 2, d4 ≥ 2, d3+d4 ≤ 100, so max d3+d4 = 100 (e.g., d3=50, d4=50). Sum = 300. ✓

So the sum is at most 50 × (number of vertices), regardless of the structure! Let me prove this in general.

Theorem: For any functional graph (each vertex has outdegree 1, no fixed points) on n vertices with the constraint deg(u) + deg(f(u)) ≤ n for all u, and deg(u) ≥ 1 for all u (actually we need deg(u) ≥ outdeg... hmm, let me think about what lower bounds we need).

Actually wait, I showed that even without strong lower bounds, the sum is ≤ 50n. Let me re-examine the path of 3 case (n=100, 4 vertices in component):

d1 + d2 ≤ 100, d2 + d3 ≤ 100, d3 + d4 ≤ 100. Sum = d1+d2+d3+d4.
= (d1+d2) + (d3+d4) ≤ 100 + 100 = 200 = 50·4. 

Oh! It's just pairing: (d1+d2) + (d3+d4) ≤ 100 + 100 = 200. This works because the path has even length (4 vertices), so we can pair them as (1,2) and (3,4), and each pair is constrained.

For a path of odd length, say 3 vertices: d1+d2 ≤ 100, d2+d3 ≤ 100. Sum = d1+d2+d3. 
= (d1+d2) + d3 ≤ 100 + d3. And d3 ≤ 100 - d2 ≤ 100 - 2 = 98 (if d2 ≥ 2). So sum ≤ 198. But 50·3 = 150. So 198 > 150!

But wait, in a functional graph, a path of 3 vertices (v1 → v2 → v3) must have v3 pointing somewhere. If v3 → v1 (3-cycle), then d3+d1 ≤ 100, and sum = d1+d2+d3 with d1+d2 ≤ 100, d2+d3 ≤ 100, d3+d1 ≤ 100. Sum ≤ 150 = 50·3. ✓

If v3 → v4 (continues), then it's a path of 4+, which we showed is ≤ 50·(length).

If v3 → v2 (so v2 ↔ v3 is a 2-cycle, and v1 → v2 is a tree edge), then constraints: d1+d2 ≤ 100, d2+d3 ≤ 100, d3+d2 ≤ 100 (same as d2+d3). So d1+d2 ≤ 100, d2+d3 ≤ 100. Sum = d1+d2+d3. d1 ≤ 100-d2, d3 ≤ 100-d2. Sum ≤ (100-d2) + d2 + (100-d2) = 200 - d2. With d2 ≥ 2 (v2 adjacent to v1 and v3): sum ≤ 198. And 50·3 = 150. So 198 > 150!

But this is a component of 3 vertices. The remaining 97 vertices form other components. The question is whether the total over all components can exceed 50·100 = 5000.

Component of 3 vertices (tree + 2-cycle): sum ≤ 198. 
Remaining 97 vertices: if they form 2-cycles (matching), sum ≤ 50·97... but 97 is odd, so we can't have all 2-cycles. We'd have 48 2-cycles (96 vertices) + 1 component of 1 vertex. But a component of 1 vertex is a fixed point (f(v) = v), which requires a self-loop, not allowed. So the remaining 97 vertices must form components with no fixed points, meaning cycles of length ≥ 2. 97 = 2·48 + 1, so we need at least one cycle of length ≥ 3.

Let me reconsider. The functional graph on 100 vertices with no fixed points decomposes into components, each with a cycle of length ≥ 2.

For a component that is a 2-cycle with trees: let the 2-cycle be a ↔ b, with trees rooted at a and b. 

Let me think about the general component. A component has a cycle of length ℓ ≥ 2, with trees hanging off cycle vertices. Let the component have s vertices.

I want to show: Σ_{v in component} deg(v) ≤ 50s.

For a pure cycle of length ℓ: sum ≤ 50ℓ (shown above, since 2·sum ≤ 100ℓ).

For a 2-cycle with one tree vertex: a ↔ b, c → a (c is child of a). 3 vertices. Constraints: deg(a)+deg(b) ≤ 100, deg(c)+deg(a) ≤ 100. Sum = deg(a)+deg(b)+deg(c) ≤ (100 - deg(a)) + deg(a) + (100 - deg(a)) = 200 - deg(a). With deg(a) ≥ 2 (adjacent to b and c): sum ≤ 198. 50·3 = 150. So 198 > 150!

So this component can have sum 198 > 150. But does this mean the total can exceed 5000?

If we have one such component (3 vertices, sum 198) and the rest (97 vertices) form 2-cycles: 97 is odd, can't form all 2-cycles. We need another odd component. Say another 3-vertex component (sum 198) and 94 vertices in 2-cycles (47 2-cycles, sum 4700). Total: 198 + 198 + 4700 = 5096 > 5000!

Wait, so does this mean |E| can exceed 2500?! Let me check if this is actually realizable.

Hmm, but I need to check that the degree sum condition is not just necessary but the actual graph can be realized. The degree sum ≤ n is necessary for triangle-free edges, but the actual condition (disjoint neighborhoods) is stronger. Let me try to construct such a graph.

Let me try to construct a graph on 100 vertices with > 2500 edges.

Take the component: a ↔ b (2-cycle), c → a (tree edge). 
- f(a) = b, f(b) = a, f(c) = a.
- Triangle-free edges: ab (witness for a and b), ca (witness for c).
- deg(a) + deg(b) ≤ 100, deg(c) + deg(a) ≤ 100.
- For sum 198: deg(a) = 2, deg(b) = 98, deg(c) = 98.

So a has degree 2 (adjacent to b and c), b has degree 98, c has degree 98.

Edge ab triangle-free: N(a) ∩ N(b) = ∅. N(a) = {b, c}. N(b) = 98 vertices including a. N(a) ∩ N(b) = {b, c} ∩ N(b). b ∉ N(b). c ∈ N(b)? If c is adjacent to b, then c ∈ N(b) and c ∈ N(a), so c is common neighbor. So c must NOT be adjacent to b. 

Edge ca triangle-free: N(c) ∩ N(a) = ∅. N(a) = {b, c}. N(c) = 98 vertices including a. N(c) ∩ N(a) = N(c) ∩ {b, c}. c ∉ N(c). b ∈ N(c)? If b is adjacent to c, then b ∈ N(c) and b ∈ N(a), common neighbor. So b must NOT be adjacent to c. ✓ (consistent with above).

So b and c are not adjacent. b has degree 98: adjacent to a and 97 others (not c). c has degree 98: adjacent to a and 97 others (not b). The 97 others for b and 97 others for c: these are from the remaining 97 vertices (vertices other than a, b, c). 

Are the 97 others the same for b and c? If b is adjacent to all 97 and c is adjacent to all 97, then for any vertex w among the 97, w is adjacent to both b and c. 

Now, the 97 remaining vertices each need a triangle-free edge. Each is adjacent to b and c (and possibly others). For vertex w, its triangle-free edge partner x must have N(w) ∩ N(x) = ∅. Since b, c ∈ N(w), x must not be adjacent to b or c. Who is not adjacent to b or c? Only a (since b and c are each adjacent to all 97 others + a). Wait, a is adjacent to b and c. So a IS adjacent to b and c. So there's no vertex that's not adjacent to both b and c (among the relevant vertices).

Hmm, so w's triangle-free partner x must satisfy b ∉ N(x) and c ∉ N(x). The vertices not adjacent to b: only c (and b itself). The vertices not adjacent to c: only b (and c itself). So x must be not adjacent to b AND not adjacent to c. The only vertex not adjacent to b is c, and the        — AI历史解题过程（thinking）
#   omni_math_000073         — 题目ID

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
  <problem_id>omni_math_000073</problem_id>
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

In a sports league, each team uses a set of at most $t$ signature colors. A set $S$ of teams is\textit{ color-identifiable} if one can assign each team in $S$ one of their signature colors, such that no team in $S$ is assigned any signature color of a different team in $S$.

For all positive integers $n$ and $t$, determine the maximum integer $g(n, t)$ such that: In any sports league with exactly $n$ distinct colors present over all teams, one can always find a color-identifiable set of size at least $g(n, t)$.

## Standard Solution


In a sports league, each team uses a set of at most \( t \) signature colors. A set \( S \) of teams is color-identifiable if one can assign each team in \( S \) one of their signature colors, such that no team in \( S \) is assigned any signature color of a different team in \( S \).

For all positive integers \( n \) and \( t \), we aim to determine the maximum integer \( g(n, t) \) such that in any sports league with exactly \( n \) distinct colors present over all teams, one can always find a color-identifiable set of size at least \( g(n, t) \).

The answer is \( \lceil \frac{n}{t} \rceil \).

To show that the answer cannot be higher, consider the following construction: let team 1 have colors \( 1, 2, 3, \ldots, t \), team 2 have colors \( t+1, t+2, \ldots, 2t \), and so on. Team \( k \) will have colors \( (k-1)t + 1, (k-1)t + 2, \ldots, \min(kt, n) \). This construction results in \( \lceil \frac{n}{t} \rceil \) teams, so \( g(n, t) \leq \lceil \frac{n}{t} \rceil \).

To prove that \( g(n, t) \geq \lceil \frac{n}{t} \rceil \), construct a function \( f(i) \) that maps each color \( i \) to a team such that team \( f(i) \) has \( i \) as a signature color. This function must exist because each color is the signature color of some team. Let \( S \) be the set of teams equal to \( f(i) \) for some \( i \). Construct a bipartite graph with teams in \( S \) as left vertices and colors as right vertices.

There are clearly at least \( n \) edges, one for each color. Since each left vertex (team) has degree at most \( t \), there are at least \( \lceil \frac{n}{t} \rceil \) teams in this set. Furthermore, because \( f \) is surjective from colors to teams, Hall's Marriage Theorem applies, ensuring a perfect matching exists.

Thus, the maximum integer \( g(n, t) \) is:
\[
\boxed{\lceil \frac{n}{t} \rceil}
\]

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have a simple graph with 100 vertices. For each vertex u, there exists a vertex v in N(u) such that N(u) ∩ N(v) = ∅. We need to find the maximum number of edges.

Let me think about this carefully.

The condition: for each vertex u, there exists a neighbor v of u such that N(u) ∩ N(v) = ∅.

Note: N(u) is the open neighborhood. So N(u) ∩ N(v) = ∅ means u and v have no common neighbors. Since v ∈ N(u), we have u ∈ N(v). So u ∈ N(u)? No, u is not in N(u) (open neighborhood). 

Let me reconsider. N(u) is the set of neighbors of u. v ∈ N(u) means v is a neighbor of u. N(u) ∩ N(v) = ∅ means u and v share no common neighbor.

Note that v ∈ N(u) and u ∈ N(v). Is v ∈ N(v)? No (no loops). Is u ∈ N(u)? No. So u ∈ N(v) but u ∉ N(u), and v ∈ N(u) but v ∉ N(v). So the condition N(u) ∩ N(v) = ∅ is about common neighbors other than themselves.

So for each vertex u, there's a neighbor v such that no vertex is adjacent to both u and v. This means the edge uv is not part of any triangle, and moreover, no vertex is adjacent to both endpoints.

This is related to the concept where each vertex has a "private" neighbor with no common neighbors.

Let me think about what structures maximize edges.

Consider a complete bipartite graph K_{50,50}. Each vertex u on one side has all 50 vertices on the other side as neighbors. For any neighbor v, N(u) ∩ N(v) = (other side) ∩ (this side) = ∅. Wait, N(u) = other side (50 vertices), N(v) = this side (50 vertices). So N(u) ∩ N(v) = ∅. Yes! So K_{50,50} satisfies the condition. It has 50*50 = 2500 edges.

Can we do better? Let me think about whether we can add edges within a part.

Actually, let me think more generally. The condition is that each vertex has a neighbor with no common neighbors. 

Let me think about an upper bound. 

Consider the graph. For each vertex u, pick a "witness" neighbor f(u) = v such that N(u) ∩ N(v) = ∅.

Let me think about this differently. Let's consider the structure.

If N(u) ∩ N(v) = ∅ for an edge uv, then deg(u) + deg(v) ≤ n = 100 (since N(u) and N(v) are disjoint subsets of V, and note u ∈ N(v), v ∈ N(u), but u ∉ N(u), v ∉ N(v), so |N(u)| + |N(v)| = deg(u) + deg(v) ≤ 100... wait, N(u) and N(v) are disjoint, and they're subsets of V. N(u) contains v, N(v) contains u. Since N(u) ∩ N(v) = ∅, and both are subsets of the 100 vertices, we have deg(u) + deg(v) ≤ 100.

So for each vertex u, there's a neighbor v with deg(u) + deg(v) ≤ 100.

Now, let's think about maximizing edges. Let d_u = deg(u). The number of edges is (1/2)Σd_u.

We want to maximize Σd_u subject to: for each u, there exists v ∈ N(u) with d_u + d_v ≤ 100.

Hmm, this is a constraint but it's not immediately giving a tight bound.

Let me think about the K_{50,50} example more. Each vertex has degree 50. For each u, any neighbor v has d_u + d_v = 100 ≤ 100. ✓. Total edges = 2500.

Can we beat 2500? Let's try adding an edge within one part of K_{50,50}. Say we add edge between a1, a2 (both in part A). Now a1 has degree 51, a2 has degree 51. 

For a1: we need a neighbor v with N(a1) ∩ N(v) = ∅. a1's neighbors are all 50 vertices in B plus a2. Consider v = a2: N(a1) = B ∪ {a2}, N(a2) = B ∪ {a1}. N(a1) ∩ N(a2) = B, which is not empty. Consider v ∈ B: N(a1) = B ∪ {a2}, N(v) = A (all of A, since v is connected to all of A). N(a1) ∩ N(v) = (B ∪ {a2}) ∩ A = {a2} (since a2 ∈ A). Not empty. So a1 has no valid witness. The condition fails.

So we can't just add edges to K_{50,50}.

Let me think about other constructions. What about a disjoint union of K_{50,50} and some other structure? No, we need exactly 100 vertices.

What about a complete bipartite graph with unequal parts? K_{a,b} with a+b=100. Each vertex in part A (size a) has degree b, each in part B has degree a. For u in A, v in B: d_u + d_v = b + a = 100. ✓. Edges = ab, maximized at a=b=50, giving 2500.

What about non-bipartite constructions? Let me think...

Consider a graph that's a union of cliques. If we have a clique of size k, each vertex has degree k-1 within the clique. For any two vertices u,v in the clique, N(u) ∩ N(v) contains all other k-2 vertices. So if k ≥ 3, no two vertices in the clique have disjoint neighborhoods. If k = 2, it's just an edge, and N(u) ∩ N(v) = ∅ (since they only have each other as neighbors, and u ∉ N(u), v ∉ N(v)). So a matching (disjoint edges) works but gives only 50 edges.

What about combining structures? Let me think about a graph where some vertices have high degree and some have low degree.

Let me consider the following: partition vertices into groups. Within the constraint, try to maximize edges.

Actually, let me think about this more carefully with the degree constraint.

For each u, there exists v ∈ N(u) with d_u + d_v ≤ 100.

Let's order vertices by degree: d_1 ≥ d_2 ≥ ... ≥ d_100.

Consider the vertex with maximum degree, d_1. It has a witness v with d_1 + d_v ≤ 100, so d_v ≤ 100 - d_1.

Now, I want to maximize Σd_i / 2.

Let me think about an upper bound. Consider the witness function f. For each u, f(u) is a neighbor with d_u + d_{f(u)} ≤ 100.

Hmm, but the witness relationship isn't necessarily symmetric or a function in a nice way.

Let me try a different approach. Let me think about what the extremal graph looks like.

Claim: The answer is 2500, achieved by K_{50,50}.

Let me try to prove an upper bound of 2500.

Approach: Let's think about it. For each vertex u, let f(u) be a witness neighbor (N(u) ∩ N(f(u)) = ∅). 

Consider the edges. Each edge uv where v = f(u) contributes to the constraint d_u + d_v ≤ 100.

Hmm, let me think about this differently. 

Let me consider the set of "witness edges" E' = {u f(u) : u ∈ V}. Note that f(u) might not satisfy f(f(u)) = u, so E' is a set of directed edges, but as undirected edges, |E'| could be less than 100.

Actually, let me think about it as: we have a set of edges S (one per vertex, but possibly with repeats) such that for each edge uv in S, d_u + d_v ≤ 100.

Let me try a cleaner approach. 

For each vertex u, choose witness f(u). Consider the sum:
Σ_u (d_u + d_{f(u)}) ≤ 100 · 100 = 10000.

But Σ_u d_{f(u)} is not simply related to Σ d_u because f might not be injective.

Hmm. Let me think differently.

Alternative approach: Let's use the constraint more cleverly.

For each vertex u with degree d_u, there exists a neighbor v with d_v ≤ 100 - d_u. 

Let's partition vertices into "high" (d > 50) and "low" (d ≤ 50). 

If u is high (d_u > 50), then its witness v has d_v < 50, so v is low. Also, v is a neighbor of u.

If u is low (d_u ≤ 50), its witness could be anything with d ≤ 100 - d_u ≥ 50.

Let H = {u : d_u > 50} and L = {u : d_u ≤ 50}. Let |H| = h, |L| = l, h + l = 100.

Each vertex in H must have a neighbor in L (its witness). 

Now, Σ d_u = Σ_{H} d_u + Σ_{L} d_u.

Σ_{L} d_u ≤ 50 · l.

For Σ_{H} d_u: each u ∈ H has d_u ≤ 100 - d_{f(u)} where f(u) ∈ L. 

Hmm, this is getting complicated. Let me think about whether 2500 is actually optimal or if we can do better.

Let me try a construction that might beat 2500.

Consider: Take K_{50,50} (parts A, B). Now, remove some edges and add others to try to increase the total.

Actually, let me think about a different construction. What if we have a graph that's "almost" complete bipartite but with some modifications?

Let me try: Partition into A (size a) and B (size b), a + b = 100. Make it complete bipartite. Then, within A, add a matching (or some edges). 

If we add an edge a1a2 within A, then a1 and a2 now have degree b+1. Their neighborhoods include all of B plus each other. For a1 to have a witness, we need a neighbor v with N(a1) ∩ N(v) = ∅. 

- v ∈ B: N(v) = A (all of A). N(a1) = B ∪ {a2}. N(a1) ∩ N(v) = (B ∪ {a2}) ∩ A = {a2} ≠ ∅. Fails.
- v = a2: N(a2) = B ∪ {a1}. N(a1) ∩ N(a2) = B ≠ ∅. Fails.

So adding any edge within A breaks the condition for the endpoints. Unless we also remove some edges.

What if we remove the edge a1-b1 for some b1? Then a1's neighborhood is (B \ {b1}) ∪ {a2}, degree b. And b1's neighborhood is A \ {a1}, degree a-1.

For a1, witness v = a2: N(a1) = (B\{b1}) ∪ {a2}, N(a2) = B ∪ {a1}. Intersection = B\{b1} ≠ ∅. Still fails.

This is hard to modify. Let me think about completely different constructions.

What about a graph consisting of disjoint complete bipartite graphs? E.g., K_{a1,b1} ∪ K_{a2,b2} ∪ ... with Σ(ai + bi) = 100. Total edges = Σ ai·bi. This is maximized with a single K_{50,50} giving 2500. Splitting reduces the product sum. So disjoint union doesn't help.

What about a graph that's not bipartite? Let me think about odd cycles or other structures.

Consider C5 (5-cycle). Each vertex has degree 2. For vertex u, its neighbors are the two adjacent vertices. N(u) = {two neighbors}. For neighbor v of u, N(v) = {u, v's other neighbor}. N(u) ∩ N(v): u's neighbors are {v, w} where w is u's other neighbor. v's neighbors are {u, x} where x is v's other neighbor. N(u) ∩ N(v) = {v,w} ∩ {u,x}. Since it's a 5-cycle, w ≠ x (as long as the cycle has length ≥ 5). Actually in C5, let vertices be 0,1,2,3,4. N(0) = {1,4}. N(1) = {0,2}. N(0) ∩ N(1) = {1,4} ∩ {0,2} = ∅. ✓. So C5 works, each vertex has 2 edges, 5 vertices, 5 edges. Not great.

Let me think about whether we can have a graph with more than 2500 edges.

Consider a graph on 100 vertices where we try to make degrees as high as possible while satisfying the constraint.

The constraint is: for each u, ∃ v ∈ N(u) with d_u + d_v ≤ 100.

If all degrees are exactly 50, then for each u, any neighbor v works (50+50=100). This is K_{50,50} (or any 50-regular graph where each edge has the property... but actually we need N(u) ∩ N(v) = ∅, not just d_u + d_v ≤ 100).

Wait, I need to be more careful. The condition is N(u) ∩ N(v) = ∅, which implies d_u + d_v ≤ 100, but the converse isn't true. So the degree constraint is necessary but not sufficient.

But for the upper bound, the degree constraint d_u + d_v ≤ 100 (for the witness) is what we can use.

So let me work with: for each u, ∃ v ∈ N(u) with d_u + d_v ≤ 100.

Can we have Σd_u > 5000 (i.e., more than 2500 edges) under this constraint?

Let me try: suppose we have 50 vertices with degree 60 and 50 vertices with degree 40. Σd = 50·60 + 50·40 = 3000 + 2000 = 5000. Edges = 2500. Same.

What about 50 vertices with degree 70 and 50 with degree 30? Σd = 3500 + 1500 = 5000. Same.

What about 40 vertices with degree 80 and 60 with degree 20? Σd = 3200 + 1200 = 4400. Less.

What about 60 vertices with degree 60 and 40 with degree 40? Σd = 3600 + 1600 = 5200. Edges = 2600 > 2500!

But wait, can this actually be realized as a graph satisfying the original condition? Let me check. Each of the 60 high-degree vertices (degree 60) needs a witness with degree ≤ 40. So each high vertex needs at least one neighbor among the low vertices. Each of the 40 low-degree vertices (degree 40) needs a witness with degree ≤ 60, which could be any neighbor.

But we also need the actual neighborhood disjointness condition, not just the degree sum. Let me think about whether such a graph can exist.

Actually, let me first check if the degree-sum constraint alone allows Σd > 5000.

For each u, ∃ v ∈ N(u) with d_u + d_v ≤ 100.

Let H = {u : d_u > 50}, L = {u : d_u ≤ 50}.

Each u ∈ H needs a neighbor in L (since d_u > 50 means d_v < 50 < d_u, so d_v ≤ 100 - d_u < 50, meaning v ∈ L).

Each u ∈ L needs a neighbor v with d_v ≤ 100 - d_u. If d_u ≤ 50, then 100 - d_u ≥ 50, so v could be in H or L.

Now, let's think about the sum. We want to maximize Σd_u.

Let me try to construct a graph with Σd > 5000.

Take h vertices with degree d_H and l = 100 - h vertices with degree d_L, where d_H > 50 and d_L < 50, and h·d_H + l·d_L is maximized.

Constraint: each high vertex needs a low neighbor. Also, the graph must be realizable (degree sequence must be graphical, and the neighborhood condition must hold).

But even just from the degree constraint, let's see: if we have h high vertices each with degree d_H, they need at least one low neighbor each. The low vertices have total degree l·d_L. The edges between H and L are at most l·d_L (since each low vertex has degree d_L, all of which could go to H). We need at least h edges from H to L (one per high vertex). So l·d_L ≥ h, which is easily satisfied.

But we also need: the high vertices have degree d_H, and they need their witness to be a low vertex with disjoint neighborhood. 

Hmm, let me think about this more carefully with a specific construction.

Construction attempt: Let A = {a_1, ..., a_60} (high, target degree 60) and B = {b_1, ..., b_40} (low, target degree 40).

For the condition to hold, each a_i needs a neighbor b_j with N(a_i) ∩ N(b_j) = ∅.

If a_i is connected to all of B (40 edges) and 20 vertices in A, then d(a_i) = 60. 
If b_j is connected to all of A (60 edges), then d(b_j) = 60, not 40.

That doesn't work. Let me think differently.

For N(a_i) ∩ N(b_j) = ∅ where b_j is a neighbor of a_i: a_i's neighbors and b_j's neighbors are disjoint. Since a_i ∈ N(b_j) and b_j ∈ N(a_i), and these are the only "cross" elements. So N(a_i) \ {b_j} and N(b_j) \ {a_i} are disjoint. This means |N(a_i) \ {b_j}| + |N(b_j) \ {a_i}| ≤ 98 (the other 98 vertices). So (d(a_i) - 1) + (d(b_j) - 1) ≤ 98, i.e., d(a_i) + d(b_j) ≤ 100. Same as before.

But the disjointness is stronger. Let me think about a concrete construction.

Let me try: Partition into A (size 60) and B (size 40). 

Connect each a_i to all 40 vertices in B. So d(a_i) ≥ 40 from B. Add 20 more edges from a_i to other vertices in A. So d(a_i) = 60.

Connect each b_j to some vertices. If b_j is connected to all of A, d(b_j) = 60. But we want d(b_j) = 40. So b_j is connected to 40 of the 60 vertices in A. 

For a_i, witness b_j: N(a_i) = B ∪ {20 vertices in A}. N(b_j) = {40 vertices in A}. N(a_i) ∩ N(b_j) = (B ∪ S_i) ∩ T_j where S_i is the 20 A-vertices adjacent to a_i, T_j is the 40 A-vertices adjacent to b_j. Since b_j ∈ B and B ⊆ N(a_i), but b_j ∉ N(b_j). So N(a_i) ∩ N(b_j) = S_i ∩ T_j. For this to be empty, we need S_i ∩ T_j = ∅, i.e., the 20 A-neighbors of a_i are disjoint from the 40 A-neighbors of b_j. But |S_i| + |T_j| = 20 + 40 = 60 = |A|. So S_i and T_j partition A, and a_i ∉ S_i (since a_i isn't adjacent to itself). Also a_i ∈ T_j (since b_j is a neighbor of a_i, meaning a_i is a neighbor of b_j, so a_i ∈ T_j). So T_j contains a_i, and S_i is 20 vertices from A \ {a_i}, and T_j = A \ S_i (40 vertices including a_i). 

So for each a_i, we need a b_j such that:
1. b_j is a neighbor of a_i (a_i ∈ T_j, i.e., b_j is connected to a_i). Since a_i is connected to all of B, this is automatic.
2. S_i ∩ T_j = ∅, i.e., S_i ⊆ A \ T_j = S_i. Wait, that's circular. T_j = A \ S_i means S_i ∩ T_j = ∅. ✓. But we need T_j to be exactly A \ S_i, and T_j must be the neighborhood of b_j within A.

So for each a_i, there must exist b_j whose A-neighborhood is exactly A \ S_i (the complement of a_i's A-neighborhood within A).

Now, different a_i's might have different S_i's, requiring different b_j's. We have 40 b_j's and 60 a_i's. By pigeonhole, some b_j must serve as witness for multiple a_i's. If b_j serves a_i and a_k, then T_j = A \ S_i = A \ S_k, so S_i = S_k. So a_i and a_k have the same A-neighborhood S.

So we can group the a_i's by their A-neighborhood S. For each distinct S, we need at least one b_j with T_j = A \ S. 

The number of distinct S sets is at most 40 (since we have 40 b_j's). Each S has size 20, and there are 60 a_i's distributed among at most 40 groups. So at least 20 groups have 2 or more a_i's, or some other distribution. Actually, we just need at most 40 distinct S sets, and 60 a_i's can be distributed among them.

But also, each b_j has a specific T_j (its A-neighborhood), and these must be distinct if they serve different S's. Actually, multiple b_j's can have the same T_j.

Wait, but b_j also needs its own witness. b_j has degree 40 (its A-neighbors). b_j needs a neighbor v with N(b_j) ∩ N(v) = ∅. 

N(b_j) = T_j (40 vertices in A). For witness v ∈ T_j (a neighbor of b_j in A): N(v) ∩ T_j = ∅. N(v) = B ∪ S_v (since v = a_i for some i, and a_i is connected to all of B plus S_i). N(v) ∩ T_j = (B ∪ S_v) ∩ T_j = S_v ∩ T_j (since B ∩ A = ∅). We need S_v ∩ T_j = ∅, i.e., S_v ⊆ A \ T_j = S_v. Wait, T_j = A \ S_v (from our earlier requirement). So S_v ∩ T_j = S_v ∩ (A \ S_v) = ∅. ✓!

So if b_j's witness is any a_i with S_i = A \ T_j, the condition is automatically satisfied. And we set up T_j = A \ S_i, so this works.

So the construction works as follows:
- Partition A (60 vertices) into groups, each group sharing the same 20-element subset S of A as their A-neighborhood.
- For each distinct S, assign at least one b_j with T_j = A \ S (its A-neighborhood).
- Each a_i is connected to all of B (40 edges) plus its 20 A-neighbors (S_i). Total degree = 60.
- Each b_j is connected to 40 vertices in A (T_j). Total degree = 40.

Wait, but we need each b_j to have degree exactly 40, and b_j is connected only to T_j ⊆ A. So d(b_j) = |T_j| = 40. ✓.

And each a_i has degree 40 (from B) + 20 (from A) = 60. ✓.

Now, the A-edges: each a_i is connected to S_i (20 vertices in A). But these are undirected edges. If a_i is connected to a_k, then a_k is connected to a_i. So if a_i ∈ S_k, then a_k ∈ S_i. The A-edges form a graph where the neighborhoods are the S_i's.

Also, a_i ∉ S_i (no self-loops). And if a_i ∈ S_k then a_k ∈ S_i.

Let me think about the A-edges more carefully. The A-edges form a 20-regular graph on 60 vertices (each a_i has exactly 20 neighbors in A). 

Now, the number of distinct S_i's: we need at most 40 (one b_j per distinct S_i). We have 60 a_i's and 40 b_j's. So at most 40 distinct S_i's.

But actually, we need: for each distinct S, there's a b_j with T_j = A \ S. We have 40 b_j's, so at most 40 distinct S's. With 60 a_i's and at most 40 distinct S's, by pigeonhole, at least 20 a_i's share an S with another. That's fine.

But wait, we also need the b_j's to have the right T_j's. If we have k distinct S's, we need k b_j's with the corresponding T_j's. The remaining 40 - k b_j's can have any T_j (as long as they also satisfy the condition).

Actually, every b_j needs a witness too. b_j's witness is some a_i with S_i = A \ T_j. So for every b_j, A \ T_j must be the S_i of some a_i. In other words, every T_j must be the complement of some S_i.

So the set of T_j's (for j = 1..40) must be a subset of {A \ S_i : i = 1..60}. And the set of distinct S_i's must be a subset of {A \ T_j : j = 1..40}. These are equivalent: the distinct S_i's and the distinct T_j's are complementary pairs.

Let me simplify. Let the distinct S values be S^(1), S^(2), ..., S^(k). Then the distinct T values are A \ S^(1), ..., A \ S^(k). We need k ≤ 40 (since we have 40 b_j's) and k ≤ 60 (since we have 60 a_i's). Also, the 60 a_i's are distributed among k groups, and the 40 b_j's are distributed among k groups.

Now, total edges:
- B-to-A edges: Each a_i connects to all 40 b_j's. That's 60 × 40 = 2400 edges. Wait, but each b_j connects to T_j (40 vertices in A), not all 60. So the B-to-A edges are: for each b_j, |T_j| = 40 edges. Total = 40 × 40 = 1600. But also, each a_i connects to all 40 b_j's, which would be 60 × 40 = 2400. Contradiction!

I think I made an error. Let me reconsider.

If each a_i is connected to all 40 vertices in B, that's 60 × 40 = 2400 B-A edges. But each b_j is connected to only 40 of the 60 A-vertices, giving 40 × 40 = 1600 B-A edges. These must be equal (it's the same set of edges). 2400 ≠ 1600. Contradiction!

So the construction doesn't work as stated. Each a_i can't be connected to all of B if each b_j is only connected to 40 of 60 A-vertices.

Let me reconsider. If a_i is connected to all 40 b_j's, then each b_j is connected to all 60 a_i's, giving d(b_j) ≥ 60. But we wanted d(b_j) = 40. Contradiction.

So I need to revise. Let me not connect each a_i to all of B.

Revised construction: 
- A (60 vertices), B (40 vertices).
- Each a_i has degree 60: some neighbors in A, some in B.
- Each b_j has degree 40: some neighbors in A, some in B.

For a_i's witness b_j: N(a_i) ∩ N(b_j) = ∅, with d(a_i) + d(b_j) = 60 + 40 = 100. ✓ (necessary condition).

Let me try: a_i has 20 neighbors in A and 40 neighbors in B (all of B). Then d(a_i) = 60. b_j has 40 neighbors in A and 0 in B. Then d(b_j) = 40.

B-A edges: 60 × 40 = 2400 (each a_i to all B) vs 40 × 40 = 1600 (each b_j to 40 A-vertices). Still contradictory.

OK so the issue is that if a_i connects to all of B, then b_j connects to all of A. Let me think about this differently.

Let me try: a_i has x neighbors in A and (60 - x) neighbors in B. b_j has y neighbors in A and (40 - y) neighbors in B.

B-A edges: 60(60-x) = 40·y (counting from each side). So 60(60-x) = 40y, i.e., y = (60(60-x))/40 = (3/2)(60-x).

For a_i's witness b_j (a B-neighbor): N(a_i) ∩ N(b_j) = ∅. N(a_i) = S_i (A-neighbors, size x) ∪ B_i (B-neighbors, size 60-x). N(b_j) = T_j (A-neighbors, size y) ∪ U_j (B-neighbors, size 40-y).

N(a_i) ∩ N(b_j) = (S_i ∩ T_j) ∪ (B_i ∩ U_j). For this to be ∅: S_i ∩ T_j = ∅ and B_i ∩ U_j = ∅.

b_j ∈ B_i (since b_j is a neighbor of a_i). And a_i ∈ T_j (since a_i is a neighbor of b_j). 

S_i ∩ T_j = ∅: |S_i| + |T_j| ≤ |A| = 60, so x + y ≤ 60.
B_i ∩ U_j = ∅: |B_i| + |U_j| ≤ |B| = 40, so (60-x) + (40-y) ≤ 40, i.e., 100 - x - y ≤ 40, i.e., x + y ≥ 60.

So x + y = 60 exactly. And y = (3/2)(60-x). So x + (3/2)(60-x) = 60. x + 90 - (3/2)x = 60. -(1/2)x = -30. x = 60. Then y = 0.

If x = 60, then a_i has 60 neighbors in A and 0 in B. But a_i needs a B-neighbor as witness (we said witness is in B). If a_i has no B-neighbors, it can't have a B-witness. So the witness must be an A-neighbor.

Let me reconsider. The witness doesn't have to be in B. Let me allow the witness to be in A.

If a_i's witness is a_k ∈ A: N(a_i) ∩ N(a_k) = ∅. Both a_i and a_k are in A. N(a_i) = S_i ∪ B_i, N(a_k) = S_k ∪ B_k. Need S_i ∩ S_k = ∅ and B_i ∩ B_k = ∅.

|S_i| + |S_k| ≤ 60 and |B_i| + |B_k| ≤ 40. With |S_i| = |S_k| = x and |B_i| = |B_k| = 60-x: 2x ≤ 60 and 2(60-x) ≤ 40. So x ≤ 30 and 60-x ≤ 20, i.e., x ≥ 40. Contradiction (x ≤ 30 and x ≥ 40).

So two A-vertices can't be witnesses for each other if they both have degree 60 with the same split. 

This suggests that having all vertices with degree > 50 is hard. Let me reconsider the problem.

Maybe 2500 is indeed the answer. Let me try to prove it.

Upper bound proof attempt:

For each vertex u, let f(u) be a witness neighbor (N(u) ∩ N(f(u)) = ∅). We know d(u) + d(f(u)) ≤ 100.

Consider the directed graph where each u points to f(u). Each vertex has out-degree 1. The underlying undirected graph has some edges.

Let me think about it differently. Consider the sum:
S = Σ_u d(u) = 2|E|.

We want to show S ≤ 5000, i.e., |E| ≤ 2500.

For each u, d(u) + d(f(u)) ≤ 100. Summing over all u:
Σ_u d(u) + Σ_u d(f(u)) ≤ 10000.

Now, Σ_u d(f(u)) = Σ_v d(v) · |f^{-1}(v)| where |f^{-1}(v)| is the number of u with f(u) = v.

So S + Σ_v d(v) · |f^{-1}(v)| ≤ 10000.

If we could show that Σ_v d(v) · |f^{-1}(v)| ≥ S, then 2S ≤ 10000, S ≤ 5000, |E| ≤ 2500.

Is Σ_v d(v) · |f^{-1}(v)| ≥ Σ_v d(v)? This is equivalent to Σ_v d(v)(|f^{-1}(v)| - 1) ≥ 0, which isn't obviously true.

Hmm. Let me think about this differently.

Actually, let me think about a cleaner approach. 

Key insight: For each vertex u, there's an edge uv (where v = f(u)) such that N(u) ∩ N(v) = ∅. This means uv is an edge and no vertex is adjacent to both u and v. In other words, uv is not contained in any triangle, and moreover, there's no path u-w-v for any w (i.e., no vertex w adjacent to both u and v).

Such an edge is called a "free edge" or an edge with no common neighbors. 

Let me think about the problem from the perspective of the complement graph or some other transformation.

Alternative approach: Let's think about it in terms of the adjacency matrix.

Actually, let me try another approach. Consider the following:

For each vertex u, choose witness f(u). The edge {u, f(u)} has the property that N(u) ∩ N(f(u)) = ∅.

Now, consider the set of witness edges W = {{u, f(u)} : u ∈ V}. Note |W| ≤ 100 (could be less if multiple u's share the same witness edge).

For each witness edge e = {u,v} ∈ W, we have d(u) + d(v) ≤ 100.

Now, I want to bound Σd(u). 

Let me think about which vertices are "covered" by witness edges. Every vertex u is an endpoint of its witness edge {u, f(u)}. So every vertex is covered by at least one witness edge (its own).

Consider the witness edges as a (multi)set of edges. Group vertices by which witness edge covers them. Actually, each vertex u is covered by at least the edge {u, f(u)}.

Let me try a different tactic. Consider the graph G. For each vertex u, let v = f(u). The edge uv has d(u) + d(v) ≤ 100.

Now, consider the edges of G. Each edge xy of G contributes to the degrees of x and y. 

Let me think about it as follows. For each vertex u, we have d(u) + d(f(u)) ≤ 100. Let's write this as d(u) ≤ 100 - d(f(u)).

Sum: Σ d(u) ≤ Σ (100 - d(f(u))) = 10000 - Σ d(f(u)).

So Σ d(u) + Σ d(f(u)) ≤ 10000.

Now, Σ d(f(u)) = Σ_v d(v) · c(v) where c(v) = |{u : f(u) = v}| = in-degree of v in the witness digraph.

Note that Σ c(v) = 100 (each u contributes 1). Also, c(v) ≥ 0.

We have S + Σ_v d(v) c(v) ≤ 10000 where S = Σ d(v).

We want to show S ≤ 5000. This requires Σ d(v) c(v) ≥ S = Σ d(v), i.e., Σ d(v)(c(v) - 1) ≥ 0.

This isn't always true. For example, if high-degree vertices have c(v) = 0 and low-degree vertices have c(v) = 2, then Σ d(v)(c(v)-1) could be negative.

So this approach doesn't directly work. Let me think more.

Let me try a completely different approach.

Approach via induction or via considering the structure.

Actually, let me think about the problem more carefully. Let me consider what happens when we have a vertex of very high degree.

If u has degree d(u), its witness v has d(v) ≤ 100 - d(u). Also, v is a neighbor of u, and N(u) ∩ N(v) = ∅. The d(u) - 1 other neighbors of u (besides v) are all not neighbors of v. And the d(v) - 1 other neighbors of v (besides u) are all not neighbors of u.

So the d(u) - 1 + d(v) - 1 = d(u) + d(v) - 2 ≤ 98 vertices (other neighbors of u and v) are all distinct and are in V \ {u, v}.

Now, let me think about a charging argument or a more clever bound.

Let me try to think about the problem computationally. Let me consider small cases first.

For n vertices (instead of 100), what's the maximum number of edges?

n = 2: One edge. K_2. Each vertex has the other as witness, N(u) ∩ N(v) = ∅. 1 edge. ⌊n²/4⌋ = 1. ✓.

n = 3: K_{1,2} (star). Center has degree 2, leaves have degree 1. For center u, witness v (a leaf): N(u) = {v, w}, N(v) = {u}. N(u) ∩ N(v) = ∅? N(u) = {v, w}, N(v) = {u}. Intersection = ∅. ✓. For leaf v, witness u: N(v) = {u}, N(u) = {v, w}. Intersection = ∅. ✓. For leaf w, witness u: same. ✓. So K_{1,2} works with 2 edges. ⌊9/4⌋ = 2. Can we do 3 edges (K_3)? In K_3, each vertex has degree 2, N(u) = {other two}. N(u) ∩ N(v) = {third vertex} ≠ ∅. So K_3 doesn't work. Max = 2 = ⌊n²/4⌋.

n = 4: K_{2,2} has 4 edges. Each vertex degree 2. N(u) ∩ N(v) = ∅ for any edge uv (since it's bipartite). ✓. Can we do 5 edges? K_4 has 6 edges, K_4 minus one edge has 5. In K_4 - e, say missing edge is {3,4}. Degrees: d(1)=d(2)=3, d(3)=d(4)=2. For vertex 1: N(1) = {2,3,4}. Witness v: N(1) ∩ N(v) = ∅. v=2: N(2)={1,3,4}. N(1)∩N(2) = {3,4} ≠ ∅. v=3: N(3)={1,2}. N(1)∩N(3) = {2} ≠ ∅. v=4: N(4)={1,2}. N(1)∩N(4) = {2} ≠ ∅. So vertex 1 has no witness. Fails. Max = 4 = ⌊16/4⌋.

n = 5: K_{2,3} has 6 edges. ⌊25/4⌋ = 6. Can we do 7? Let me check. Total possible edges = 10. We need to remove at least 3. Hmm, let me think... Actually, let me just conjecture the answer is ⌊n²/4⌋ = 2500 for n = 100.

Let me try to prove that the maximum is ⌊n²/4⌋.

Proof approach: Show that |E(G)| ≤ ⌊n²/4⌋ for any graph G on n vertices satisfying the condition.

This is the same as the Turán-type bound for triangle-free graphs (Mantel's theorem). But our condition is different (stronger in some ways, weaker in others).

Actually, our condition doesn't require the graph to be triangle-free. A graph could have triangles as long as each vertex has at least one "private" neighbor.

Wait, but can a graph with triangles satisfy our condition? Let me think of an example.

Take K_{2,3} (bipartite, 6 edges, 5 vertices) and add an edge within the part of size 2. Now we have 7 edges. The two vertices in the size-2 part are now adjacent. Let's call them a1, a2 and b1, b2, b3.

Edges: a1-b1, a1-b2, a1-b3, a2-b1, a2-b2, a2-b3, a1-a2. 7 edges.

d(a1) = 4, d(a2) = 4, d(b_i) = 2.

For a1: N(a1) = {a2, b1, b2, b3}. Witness? 
- v = a2: N(a2) = {a1, b1, b2, b3}. N(a1) ∩ N(a2) = {b1, b2, b3} ≠ ∅. Fails.
- v = b1: N(b1) = {a1, a2}. N(a1) ∩ N(b1) = {a2} ≠ ∅. Fails.
- v = b2: similar, {a2} ≠ ∅. Fails.
- v = b3: similar. Fails.

So a1 has no witness. The condition fails. So adding an edge within a part of K_{2,3} breaks the condition.

What about a different graph with triangles? Let me think...

Take C_5 plus a chord. C_5 = 0-1-2-3-4-0. Add chord 0-2. Now:
d(0) = 3, d(1) = 2, d(2) = 3, d(3) = 2, d(4) = 2.
N(0) = {1, 2, 4}, N(1) = {0, 2}, N(2) = {0, 1, 3}, N(3) = {2, 4}, N(4) = {0, 3}.

For vertex 0: 
- v=1: N(0)∩N(1) = {1,2,4}∩{0,2} = {2} ≠ ∅. Fails.
- v=2: N(0)∩N(2) = {1,2,4}∩{0,1,3} = {1} ≠ ∅. Fails.
- v=4: N(0)∩N(4) = {1,2,4}∩{0,3} = ∅. ✓!

For vertex 2:
- v=0: N(2)∩N(0) = {0,1,3}∩{1,2,4} = {1} ≠ ∅. Fails.
- v=1: N(2)∩N(1) = {0,1,3}∩{0,2} = {0} ≠ ∅. Fails.
- v=3: N(2)∩N(3) = {0,1,3}∩{2,4} = ∅. ✓!

For vertex 1:
- v=0: N(1)∩N(0) = {0,2}∩{1,2,4} = {2} ≠ ∅. Fails.
- v=2: N(1)∩N(2) = {0,2}∩{0,1,3} = {0} ≠ ∅. Fails.
No witness! Fails.

So vertex 1 has no witness. The condition fails.

Hmm. It seems hard to have triangles. Let me think about whether the condition actually implies triangle-free.

If there's a triangle u-v-w, then for vertex u: is there a witness? u's neighbors include v and w. If v is u's witness, N(u) ∩ N(v) = ∅, but w ∈ N(u) ∩ N(v) (since w is adjacent to both u and v). So v can't be the witness. Similarly w can't be. So u's witness must be some other neighbor x ≠ v, w with N(u) ∩ N(x) = ∅. This is possible if u has a neighbor outside the triangle.

So triangles are allowed as long as each vertex in the triangle has another neighbor with no common neighbors.

Let me try to construct such a graph.

Take a triangle {a, b, c} and a vertex d connected only to a. And vertex e connected only to b. And vertex f connected only to c.

Edges: ab, bc, ac, ad, be, cf. 6 edges, 6 vertices.

d(a) = 3 (b, c, d), d(b) = 3 (a, c, e), d(c) = 3 (a, b, f), d(d) = 1, d(e) = 1, d(f) = 1.

For a: N(a) = {b, c, d}. 
- v = d: N(d) = {a}. N(a) ∩ N(d) = ∅. ✓.

For b: N(b) = {a, c, e}.
- v = e: N(e) = {b}. N(b) ∩ N(e) = ∅. ✓.

For c: N(c) = {a, b, f}.
- v = f: N(f) = {c}. N(c) ∩ N(f) = ∅. ✓.

For d: N(d) = {a}.
- v = a: N(a) = {b, c, d}. N(d) ∩ N(a) = ∅. ✓.

For e: N(e) = {b}.
- v = b: N(b) = {a, c, e}. N(e) ∩ N(b) = ∅. ✓.

For f: N(f) = {c}.
- v = c: N(c) = {a, b, f}. N(f) ∩ N(c) = ∅. ✓.

So this graph with a triangle works! It has 6 edges on 6 vertices. ⌊36/4⌋ = 9. So it's well below the Mantel bound. But it shows triangles are possible.

Can we do better? Let me try to add more edges. 

Take the above and add more connections. Add vertex g connected to d, and vertex h connected to e, etc. This creates a tree-like structure hanging off the triangle. Not great for edge count.

Let me think about this more carefully. The condition allows triangles but requires each vertex to have a "private" neighbor. 

Let me think about the problem differently. Let me consider the following approach:

For each vertex u, let f(u) = v be its witness. Consider the "witness matching" — can we extract a matching from the witness edges?

Actually, let me think about a key structural observation.

Observation: If uv is a witness edge (N(u) ∩ N(v) = ∅), then in the graph, the edge uv is "isolated" in the sense that no other edge shares both endpoints' neighborhoods. 

Let me try a different approach to the upper bound.

Approach: Consider the witness function f. For each u, f(u) is a neighbor with N(u) ∩ N(f(u)) = ∅.

Define a new graph H on V where we connect u to f(u). H is a graph (or multigraph) where each vertex has at least one incident edge (its witness edge). 

The connected components of H are... well, each vertex has out-degree 1 in the directed version. So the structure is a functional graph (each weakly connected component has exactly one cycle).

Hmm, this is getting complicated. Let me try yet another approach.

Approach: Let's try to prove |E| ≤ n²/4 by a direct counting argument.

For each edge e = uv, define w(e) = d(u) + d(v). We know that for each vertex u, there's an incident edge e = u f(u) with w(e) ≤ n.

But other edges might have w(e) > n.

Hmm, let me think about the problem from the perspective of the adjacency matrix and the condition.

The condition N(u) ∩ N(v) = ∅ for edge uv means: for all w ≠ u, v, w is not adjacent to both u and v. In adjacency matrix terms, if A is the adjacency matrix, then (A²)_{uv} = |N(u) ∩ N(v)| = 0 for the witness edge uv. (Since u and v are adjacent, (A²)_{uv} counts the number of common neighbors, which is 0.)

Actually, (A²)_{uv} = Σ_w A_{uw} A_{wv} = |N(u) ∩ N(v)| when u ≠ v. For the witness edge, this is 0.

So the condition is: for each vertex u, there exists v with A_{uv} = 1 and (A²)_{uv} = 0.

This means: for each u, there's a neighbor v such that the edge uv is not in any triangle.

Now, let me think about this. The number of triangles containing edge uv is (A²)_{uv} (when A_{uv} = 1). The condition says each vertex is incident to at least one edge that's in no triangle.

Let T be the set of "triangle-free edges" (edges not in any triangle). The condition says every vertex is incident to at least one edge in T.

So T is an edge cover of the vertices. The minimum size of an edge cover in a graph with n vertices and no isolated vertices is ⌈n/2⌉ (it's a matching plus some extra edges). But T could be larger.

Now, the edges not in T are edges that are in at least one triangle. Let's call these "triangle edges."

Hmm, I'm not sure this directly helps with the bound.

Let me try to think about it from the perspective of the following:

Claim: For any graph satisfying the condition, |E| ≤ ⌊n²/4⌋.

Let me try to prove this by induction on n.

Base case: n = 1, 2, trivial.

Inductive step: Consider a graph G on n vertices satisfying the condition. Pick a vertex u of minimum degree δ. Let v = f(u) be its witness. 

d(u) + d(v) ≤ n. Since d(u) = δ is minimum, d(v) ≥ δ, so 2δ ≤ d(u) + d(v) ≤ n, giving δ ≤ n/2.

Now, remove u and v from G. The remaining graph G' has n - 2 vertices. Does G' satisfy the condition?

Not necessarily. A vertex w in G' might have had u or v as its only witness. So we can't directly apply induction.

Let me think differently.

Actually, let me think about whether the answer might not be 2500. Let me try to construct a graph with more than 2500 edges that satisfies the condition.

Construction idea: Take a complete bipartite graph K_{50,50} and modify it.

Actually, let me think about a different type of construction. What if the graph has a more complex structure?

Consider the following: partition the 100 vertices into groups A_1, A_2, ..., A_k and B_1, B_2, ..., B_k. Connect A_i to B_j for certain pairs (i,j). 

Actually, let me think about a blow-up construction.

Take a "template" graph H on k vertices that satisfies the condition. Replace each vertex i with an independent set of size n_i (Σn_i = 100). Replace each edge ij of H with a complete bipartite graph between the corresponding sets. 

For a vertex u in group i, its neighbors are all vertices in groups j where ij is an edge of H. The neighborhood N(u) is the union of groups j adjacent to i in H. For a witness, u needs a neighbor v in some group j (where ij ∈ E(H)) such that N(u) ∩ N(v) = ∅. N(u) = ∪_{i~k} group_k, N(v) = ∪_{j~k} group_k. N(u) ∩ N(v) = ∪_{k: i~k and j~k} group_k. For this to be ∅, we need no k adjacent to both i and j in H. So ij must be an edge of H with no common neighbor in H. And this must hold for every vertex i in H (each vertex i has a neighbor j in H with N_H(i) ∩ N_H(j) = ∅).

So the template H must also satisfy the condition! And the blow-up preserves the condition.

The number of edges in the blow-up is Σ_{ij ∈ E(H)} n_i · n_j.

To maximize this, we want H to satisfy the condition and the n_i's to be chosen to maximize Σ n_i n_j over edges of H.

If H = K_2 (two vertices, one edge), then the blow-up is K_{a,b} with a + b = 100, and edges = ab ≤ 2500.

If H is a path P_3 (3 vertices, 2 edges: 1-2, 2-3), the blow-up has edges n_1·n_2 + n_2·n_3 = n_2(n_1 + n_3). With n_1 + n_2 + n_3 = 100, this is n_2(100 - n_2), maximized at n_2 = 50, giving 2500. Same.

If H = K_{2,2} (4 vertices, 4 edges), the blow-up has edges n_1·n_3 + n_1·n_4 + n_2·n_3 + n_2·n_4 = (n_1+n_2)(n_3+n_4). With sum 100, maximized at (n_1+n_2) = (n_3+n_4) = 50, giving 2500. Same.

If H = C_5 (5 vertices, 5 edges), the blow-up has edges Σ n_i n_{i+1} (mod 5). By AM-GM or convexity, this is maximized when... it's a quadratic form. For C_5, the maximum of Σ n_i n_{i+1} subject to Σ n_i = 100 is achieved when all n_i = 20, giving 5 · 20 · 20 = 2000. Less than 2500.

If H = K_{a,b} (complete bipartite), the blow-up is also complete bipartite (merging the groups), giving at most 2500.

What if H has more edges? Like H = K_{2,3} (6 edges). Blow-up edges = (n_1+n_2)(n_3+n_4+n_5) ≤ 2500. Same.

It seems like for any bipartite H, the blow-up gives at most 2500 (since it reduces to a complete bipartite graph).

What about non-bipartite H? We showed earlier that a triangle with pendant vertices works. Let's try H = triangle + pendant vertices.

H: vertices 1,2,3 (triangle) + 4 (connected to 1) + 5 (connected to 2) + 6 (connected to 3). 6 vertices, 6 edges. 

Blow-up edges = n_1n_2 + n_1n_3 + n_2n_3 + n_1n_4 + n_2n_5 + n_3n_6.

With Σn_i = 100. Let's optimize. This is a quadratic form. Let me think...

Actually, the blow-up might not give more than 2500 for any template. Let me think about why.

For any graph H satisfying the condition, the blow-up with optimal group sizes gives at most ⌊n²/4⌋ edges. Is this true?

Hmm, consider H with many edges. The blow-up edges are Σ_{ij ∈ E(H)} n_i n_j. This is (1/2) n^T A_H n where A_H is the adjacency matrix of H. The maximum of n^T A_H n subject to Σn_i = n is related to the largest eigenvalue of A_H.

For H = K_2, λ_max = 1, and the max is n²/2 · 1 = n²/2... wait, (1/2) n^T A n with the optimal n. For K_2, A = [[0,1],[1,0]], λ_max = 1. The optimal n is (n/2, n/2), giving (1/2)(n/2)²·2 = n²/4. So edges = n²/4.

For H with λ_max > 1, we might get more. For example, H = K_3 has λ_max = 2. But K_3 doesn't satisfy the condition (as we showed). 

What about H = C_5? λ_max = 2cos(π/5) ≈ 1.618. The blow-up gives (1/2) n² λ_max / k... no, let me be more careful.

The maximum of n^T A n subject to 1^T n = N (where N = 100) is N² λ_max / k if we use the eigenvector... no. The maximum of n^T A n subject to 1^T n = N, n ≥ 0 is N² · (max of x^T A x subject to 1^T x = 1, x ≥ 0). 

For the Perron eigenvector (which is positive for connected graphs), x = v/Σv_i where v is the Perron eigenvector. Then x^T A x = λ_max / (Σv_i)² · v^T v... hmm, this isn't clean.

Actually, the maximum of n^T A n subject to 1^T n = N is N² λ_max if the Perron eigenvector is proportional to 1 (i.e., the graph is regular). For a d-regular graph, λ_max = d, and the optimal is all n_i = N/k, giving n^T A n = (N/k)² · dk = N²d/k. Edges = (1/2)N²d/k = N²d/(2k) = N² · (average degree) / (2k) · k... wait.

For a d-regular graph on k vertices, edges of H = dk/2. Blow-up with all groups size N/k: edges = (N/k)² · dk/2 = N²d/(2k). For this to exceed N²/4, we need d/k > 1/2, i.e., d > k/2, i.e., the graph has more than k²/4 edges, i.e., more than the Mantel bound. But if H satisfies the condition and has more than k²/4 edges, then by induction (or by our conjecture), this is impossible. So if the conjecture holds for H, the blow-up can't exceed N²/4.

But this is circular. Let me think about it differently.

Actually, the blow-up construction might not be the only way to build graphs satisfying the condition. There might be non-blow-up graphs that do better. But from the small cases and the difficulty of beating 2500, I believe the answer is 2500.

Let me try to prove the upper bound directly.

Proof of upper bound:

For each vertex u, let f(u) be a witness neighbor. We have N(u) ∩ N(f(u)) = ∅, hence d(u) + d(f(u)) ≤ n.

Let S = {u ∈ V : d(u) ≤ n/2} (small vertices) and L = {u ∈ V : d(u) > n/2} (large vertices).

For u ∈ L, d(u) > n/2, so d(f(u)) < n/2, meaning f(u) ∈ S. So every large vertex has its witness in S, and in particular, every large vertex has a neighbor in S.

Now, let's count edges. Let e_LL, e_LS, e_SS be the number of edges within L, between L and S, and within S.

|E| = e_LL + e_LS + e_SS.

We have:
- Σ_{u ∈ L} d(u) = 2e_LL + e_LS
- Σ_{u ∈ S} d(u) = 2e_SS + e_LS

Total: Σd(u) = 2(e_LL + e_LS + e_SS) = 2|E|.

Now, for each u ∈ L, d(u) ≤ n - d(f(u)) where f(u) ∈ S. 

Hmm, this is still not giving a clean bound. Let me try another approach.

Let me try the approach of considering the witness edges as a matching-like structure.

For each u, let f(u) be the witness. Consider the multiset of witness edges {u, f(u)}. 

Key idea: Let's find a large matching in the witness edges.

Actually, let me try a direct approach. Let me use the following lemma:

Lemma: If for every vertex u, there's a neighbor v with d(u) + d(v) ≤ n, then |E| ≤ n²/4.

Wait, is this lemma true? Let me check with a potential counterexample.

Consider n = 6. Take K_4 on vertices {1,2,3,4} and connect vertex 5 to vertex 1, vertex 6 to vertex 2. 

d(1) = 4, d(2) = 4, d(3) = 3, d(4) = 3, d(5) = 1, d(6) = 1.

For vertex 1: d(1) = 4. Need neighbor v with d(v) ≤ 2. Neighbors: 2 (d=4), 3 (d=3), 4 (d=3), 5 (d=1). v = 5: d(1) + d(5) = 5 ≤ 6. ✓.
For vertex 2: v = 6, d(2) + d(6) = 5 ≤ 6. ✓.
For vertex 3: d(3) = 3. Need d(v) ≤ 3. v = 1 (d=4, no), v = 2 (d=4, no), v = 4 (d=3, 3+3=6 ≤ 6). ✓.
For vertex 4: v = 3, 3+3=6. ✓.
For vertex 5: v = 1, 1+4=5 ≤ 6. ✓.
For vertex 6: v = 2, 1+4=5 ≤ 6. ✓.

So the degree condition is satisfied. |E| = 6 + 2 = 8. n²/4 = 9. So 8 ≤ 9. ✓.

But does the original condition (N(u) ∩ N(v) = ∅) hold? Let me check.

For vertex 3, witness v = 4: N(3) = {1, 2, 4}, N(4) = {1, 2, 3}. N(3) ∩ N(4) = {1, 2} ≠ ∅. Fails!

So the degree condition is necessary but not sufficient. The original condition is stronger. Good, so the lemma (if true) would give an upper bound, but we need to check if the lemma is actually true.

Let me check: is the lemma "if for every vertex u, there's a neighbor v with d(u) + d(v) ≤ n, then |E| ≤ n²/4" true?

Consider n = 4, K_4 minus one edge. d = (3, 3, 2, 2). For vertex 1 (d=3): need neighbor with d ≤ 1. Neighbors: 2 (d=3), 3 (d=2), 4 (d=2). None has d ≤ 1. So the condition fails. |E| = 5, n²/4 = 4. But the condition doesn't hold, so no contradiction.

Let me try to find a graph where the degree condition holds but |E| > n²/4.

n = 4: n²/4 = 4. Max edges with degree condition: we need each vertex to have a neighbor with degree sum ≤ 4. With 5 edges (K_4 - e), degrees (3,3,2,2), vertex 1 needs neighbor with d ≤ 1, but all neighbors have d ≥ 2. Fails. With 4 edges, e.g., K_{2,2}, degrees all 2, 2+2=4. ✓. |E| = 4 = n²/4.

n = 6: n²/4 = 9. Can we have 10 edges with the degree condition? 10 edges on 6 vertices means average degree 20/6 ≈ 3.33. 

Let me try: degrees (4, 4, 4, 3, 3, 2). Sum = 20, edges = 10. 
Vertex with d=4 needs neighbor with d ≤ 2. Only vertex with d=2. So the d=2 vertex must be adjacent to all three d=4 vertices. But d=2 vertex has only 2 neighbors. Can't be adjacent to 3 vertices. Contradiction. So this degree sequence doesn't work.

Try degrees (4, 4, 3, 3, 3, 3). Sum = 20, edges = 10.
d=4 vertices need neighbor with d ≤ 2. But all other vertices have d ≥ 3. Fails.

Try degrees (5, 3, 3, 3, 3, 3). Sum = 20, edges = 10.
d=5 vertex needs neighbor with d ≤ 1. All neighbors have d ≥ 3. Fails.

Try degrees (4, 4, 4, 4, 2, 2). Sum = 20, edges = 10.
d=4 vertices need neighbor with d ≤ 2. The two d=2 vertices. Each d=4 vertex must be adjacent to at least one d=2 vertex. Two d=2 vertices can be adjacent to at most 4 other vertices total (each has 2 neighbors). So at most 4 of the d=4 vertices can be adjacent to a d=2 vertex. We have 4 d=4 vertices, so each must be adjacent to exactly one d=2 vertex, and the d=2 vertices are adjacent to 2 d=4 vertices each.

Now, the d=2 vertices: each is adjacent to 2 of the 4 d=4 vertices. The d=4 vertices: each is adjacent to 1 d=2 vertex and 3 other d=4 vertices (since d=4, and 1 neighbor is d=2, so 3 more from the other 3 d=4 vertices). So the d=4 vertices form K_4 (each adjacent to all 3 others). 

So the graph is K_4 on {1,2,3,4} plus vertex 5 adjacent to two of {1,2,3,4} and vertex 6 adjacent to two of {1,2,3,4}.

d=2 vertices (5, 6): each needs a neighbor with d ≤ 4. Any neighbor works (d=4, 2+4=6=n). ✓.

d=4 vertices: each needs a neighbor with d ≤ 2. Each is adjacent to one of {5, 6}. ✓.

So the degree condition holds! |E| = 10 > 9 = n²/4.

But does the original condition hold? Let me check with a specific graph.

K_4 on {1,2,3,4}. Vertex 5 adjacent to {1, 2}. Vertex 6 adjacent to {3, 4}.

d(1) = 4 (neighbors: 2, 3, 4, 5). d(2) = 4 (1, 3, 4, 5). d(3) = 4 (1, 2, 4, 6). d(4) = 4 (1, 2, 3, 6). d(5) = 2 (1, 2). d(6) = 2 (3, 4).

For vertex 1: witness v = 5. N(1) = {2, 3, 4, 5}. N(5) = {1, 2}. N(1) ∩ N(5) = {2} ≠ ∅. Fails!

So the original condition fails, even though the degree condition holds. Good, this confirms the original condition is strictly stronger.

So the lemma about the degree condition is FALSE (the degree condition allows |E| > n²/4), but the original condition might still imply |E| ≤ n²/4.

Let me now try to prove the upper bound for the original condition.

Let me think about this more carefully.

For each vertex u, let f(u) be a witness. N(u) ∩ N(f(u)) = ∅.

Key observation: The witness edges form a set of edges where each edge uv has the property that no other vertex is adjacent to both u and v. 

Let me think about the structure of the graph more carefully.

Consider the witness digraph: u → f(u). Each vertex has out-degree 1. 

Let me think about what happens with a vertex u and its witness v = f(u). The edge uv has no common neighbors. So in the graph, removing all edges incident to u or v, the remaining graph on V \ {u, v} has some structure.

Actually, let me try a proof by induction.

Theorem: For a graph G on n vertices satisfying the condition, |E(G)| ≤ ⌊n²/4⌋.

Proof by strong induction on n.

Base cases: n ≤ 2, trivial.

Inductive step: Assume the result for all graphs on fewer than n vertices.

Case 1: There exists a vertex u with d(u) ≤ n/2.

Remove u. The remaining graph G' on n-1 vertices may not satisfy the condition (some vertex might have lost its only witness). 

Hmm, this doesn't work directly. Let me think differently.

Case 2: All vertices have degree > n/2. Then for any u, d(u) > n/2, so d(f(u)) < n/2. Contradiction. So there must exist a vertex with degree ≤ n/2.

Wait, that's not right. If all vertices have degree > n/2, then for each u, d(f(u)) > n/2, so d(u) + d(f(u)) > n. But we need d(u) + d(f(u)) ≤ n. Contradiction. So there must exist a vertex with degree ≤ n/2.

OK so there's always a vertex u with d(u) ≤ n/2. But removing it doesn't preserve the condition.

Let me try a different approach. Let me remove a vertex u and its witness v = f(u).

d(u) + d(v) ≤ n. The edge uv contributes 1 to |E|. The edges incident to u or v: d(u) + d(v) - 1 (subtracting the edge uv counted twice). 

When we remove u and v, we remove d(u) + d(v) - 1 edges. The remaining graph G - {u, v} has n - 2 vertices and |E| - (d(u) + d(v) - 1) edges.

Does G - {u, v} satisfy the condition? Not necessarily. A vertex w in G - {u, v} might have had u or v as its only witness.

But maybe we can choose u and v carefully. 

Hmm, let me think about this differently. Let me try to use a weight function or a clever counting argument.

Alternative approach: Let's use the following strategy. For each edge e = xy, assign a weight. Show that the total weight is bounded.

Actually, let me try the following approach inspired by Mantel's theorem.

Mantel's theorem proof: For each edge uv, d(u) + d(v) ≤ n (in a triangle-free graph). Sum over all edges: Σ_{uv ∈ E} (d(u) + d(v)) = Σ_u d(u)² ≤ n|E|. By Cauchy-Schwarz, (Σd(u))² ≤ n Σd(u)² ≤ n · n|E| = n²|E|. So (2|E|)² ≤ n²|E|, giving 4|E|² ≤ n²|E|, |E| ≤ n²/4.

In our case, we don't have d(u) + d(v) ≤ n for all edges, only for witness edges. So we can't directly apply this.

But maybe we can use a variant. Let me think...

For each vertex u, let f(u) be its witness. We have d(u) + d(f(u)) ≤ n.

Consider the sum Σ_u d(u) · d(f(u)). Hmm, not sure.

Let me try another approach. 

Approach: Partition the vertices based on the witness structure.

For each vertex u, the witness f(u) gives an edge with no common neighbors. Let's think of the witness edges as defining a structure.

Consider the graph W = (V, {u, f(u)} : u ∈ V). W is a graph (possibly with multi-edges) where each vertex has degree ≥ 1.

In W, consider the connected components. Each component has at least 2 vertices (since each vertex has at least one witness edge).

Hmm, I'm going in circles. Let me try a more computational approach.

Let me think about what kinds of graphs can satisfy the condition and have many edges.

From the examples, K_{50,50} gives 2500 edges. The blow-up of any template graph gives at most 2500. Non-blow-up graphs seem hard to construct with more edges.

Let me try to see if there's a non-blow-up construction that beats 2500.

Consider the following: Take K_{50,50} with parts A and B. Now, within A, add a perfect matching (25 edges). This adds 25 edges, giving 2525. But we need to check the condition.

After adding matching edges in A: each a_i ∈ A now has degree 51 (50 from B + 1 from A). For a_i, witness v: 
- v ∈ B: N(a_i) = B ∪ {a_i's match in A}. N(v) = A. N(a_i) ∩ N(v) = (B ∪ {match}) ∩ A = {match} ≠ ∅. Fails.
- v = a_i's match: N(a_i) = B ∪ {match}. N(match) = B ∪ {a_i}. N(a_i) ∩ N(match) = B ≠ ∅. Fails.

So the condition fails for all a_i. We'd need to also remove some edges to compensate.

What if we remove, for each matched pair (a_i, a_j), the edge a_i - b_k for some specific b_k? 

This is getting complicated. Let me try to think about it more carefully.

Actually, let me think about the problem from the perspective of the following key lemma:

Lemma: If G satisfies the condition, then G is "almost" bipartite in some sense.

Hmm, that's vague. Let me try to think about specific structures.

Let me consider the following construction: 

Take a bipartite graph with parts A (50 vertices) and B (50 vertices). It's not complete bipartite but has some edges missing and some edges within parts.

For each a ∈ A, a has a witness b ∈ B with N(a) ∩ N(b) = ∅. This means a and b share no common neighbors. Since a's neighbors are in A ∪ B and b's neighbors are in A ∪ B, and they share none, this is a strong condition.

If the graph is bipartite (no edges within A or within B), then for any edge ab (a ∈ A, b ∈ B), N(a) ⊆ B and N(b) ⊆ A, so N(a) ∩ N(b) = ∅ automatically. So any bipartite graph satisfies the condition (as long as it has no isolated vertices, so each vertex has at least one neighbor to serve as witness).

Wait, is that right? In a bipartite graph with parts A and B, for a ∈ A, N(a) ⊆ B. For b ∈ B, N(b) ⊆ A. So N(a) ∩ N(b) ⊆ B ∩ A = ∅. Yes! So in any bipartite graph (with no isolated vertices), every edge is a witness edge. The condition is automatically satisfied.

So the condition is satisfied by any bipartite graph with minimum degree ≥ 1. The maximum edges in a bipartite graph on 100 vertices is ⌊100²/4⌋ = 2500 (by K_{50,50}).

But the condition also allows non-bipartite graphs. Can a non-bipartite graph satisfying the condition have more than 2500 edges?

From our earlier analysis, adding any edge within a part of K_{50,50} breaks the condition. But maybe a completely different non-bipartite construction works.

Let me think about this. Consider a graph that's "mostly" bipartite but with a few extra edges, and some edges removed to compensate.

Actually, let me think about whether the condition implies the graph is bipartite. We showed a triangle with pendant vertices satisfies the condition, so the graph need not be bipartite. But that graph had few edges.

Conjecture: The maximum number of edges is 2500, achieved by K_{50,50}.

Let me try to prove this. I need to show that any graph satisfying the condition has at most 2500 edges.

Approach: Let me try to show that the condition implies the graph is "close to bipartite" in a way that limits the edge count.

Key insight: In a bipartite graph, every edge is a witness edge. In a non-bipartite graph, some edges are not witness edges (they're in triangles), but every vertex still needs at least one witness edge.

Let me define: A vertex u is "satisfied" if it has a witness neighbor. The condition says all vertices are satisfied.

Let me try the following approach:

For each vertex u, let f(u) be a witness. Consider the set of witness pairs P = {(u, f(u)) : u ∈ V}. 

For each pair (u, v) with v = f(u), we have N(u) ∩ N(v) = ∅, so d(u) + d(v) ≤ n.

Now, I want to bound |E|. Let me try to use the witness pairs to partition the edges.

Hmm, let me try yet another approach. Let me think about the problem in terms of the adjacency matrix.

Let A be the adjacency matrix. The condition is: for each i, there exists j with A_{ij} = 1 and (A²)_{ij} = 0.

The number of edges is (1/2)Σ_{i,j} A_{ij} = (1/2) tr(AJ) where J is the all-ones matrix... actually, |E| = (1/2) Σ_i d(i) = (1/2) 1^T A 1.

We want to maximize 1^T A 1 / 2 subject to: for each i, ∃ j with A_{ij} = 1 and (A²)_{ij} = 0.

This is hard to work with directly. Let me go back to combinatorial arguments.

Let me try the following approach:

For each vertex u, choose a witness f(u). Define a "partner" function. Now, consider the graph G and the partner function.

For each u, the edge {u, f(u)} is triangle-free (no common neighbors). 

Let T be the set of triangle-free edges (edges not in any triangle). Every vertex is incident to at least one edge in T (its witness edge).

The edges in T form a subgraph H of G with no isolated vertices (every vertex has at least one edge in T).

Now, the edges of G \ T are all in some triangle. 

Claim: The edges in G \ T can be charged to the edges in T in a way that bounds the total.

Hmm, this is still vague. Let me try to think about it more concretely.

Actually, let me try a different approach entirely. Let me think about the problem as an optimization problem and try to use Lagrangian methods or linear programming.

Let me think about the dual problem. We want to maximize |E| = (1/2) Σ d(u) subject to: for each u, ∃ v ∈ N(u) with N(u) ∩ N(v) = ∅.

The constraint is hard to linearize. Let me think about relaxations.

Relaxation: For each u, ∃ v ∈ N(u) with d(u) + d(v) ≤ n. (This is a necessary condition.)

We showed this relaxation allows |E| > n²/4 (the K_4 + 2 pendant vertices example). So the relaxation is too weak.

Stronger relaxation: For each u, ∃ v ∈ N(u) with N(u) ∩ N(v) = ∅.

This is the actual condition, which is hard to relax further.

Let me try to think about the problem from the extremal graph theory perspective.

The condition "every vertex has a neighbor with no common neighbors" is related to the concept of "isolated edges" or "independent edges" in the neighborhood graph.

Let me think about the contrapositive: what prevents a graph from having many edges while satisfying the condition?

If a graph has many edges, it's "dense," and dense graphs tend to have many triangles. In a dense graph, most edges are in triangles, so few edges are triangle-free. The condition requires every vertex to be incident to a triangle-free edge, so we need at least n/2 triangle-free edges (forming an edge cover). 

In a graph with n²/4 + ε edges, how many triangle-free edges must there be?

By a result in extremal graph theory, a graph with more than n²/4 edges must contain a triangle (Mantel's theorem). But we need more: we need that not every edge is in a triangle.

Actually, let me think about it this way. Suppose |E| > n²/4. By Mantel's theorem, G contains a triangle. But that's fine; our condition allows triangles.

Let me think about what happens when |E| is close to n²/4 + n/2 or so.

Hmm, let me try a more direct approach. Let me try to prove the bound by considering the structure of witness edges.

Proof attempt:

For each vertex u, let f(u) be a fixed witness. We have N(u) ∩ N(f(u)) = ∅ and d(u) + d(f(u)) ≤ n.

Consider the directed graph D where u → f(u). Each vertex has out-degree 1. The components of D are functional graph components (each has a directed cycle with trees hanging off).

For each directed cycle C = (u_1 → u_2 → ... → u_k → u_1) in D, we have:
- d(u_i) + d(u_{i+1}) ≤ n for each i (since f(u_i) = u_{i+1}).

Wait, actually f(u_i) = u_{i+1} means u_{i+1} is the witness of u_i, so N(u_i) ∩ N(u_{i+1}) = ∅ and d(u_i) + d(u_{i+1}) ≤ n.

For the cycle, summing: Σ_{i=1}^k (d(u_i) + d(u_{i+1})) ≤ kn. This gives 2 Σ_{i=1}^k d(u_i) ≤ kn, so Σ d(u_i) ≤ kn/2.

For trees hanging off the cycle: if u → v where v is on the cycle or in a tree, d(u) + d(v) ≤ n.

This is getting complicated. Let me try a cleaner approach.

Let me try to use the following strategy:

1. Show that we can find a set of vertex-disjoint witness edges (a matching) that covers a large fraction of vertices.
2. Use this matching to bound the total number of edges.

Step 1: Find a matching in the witness edges.

The witness edges form a graph W on V. Each vertex has at least one incident edge in W. By a classical result, any graph with no isolated vertices has a matching of size at least n/2 - o(n)... actually, any graph without isolated vertices has a matching of size ≥ n/2 - (number of odd components)/2... hmm, that's not quite right.

Actually, a classical result says: any graph on n vertices with minimum degree ≥ 1 has a matching of size ≥ n/2 - (number of connected components that are odd cycles with pendant edges)... this is getting complicated.

Let me use a simpler result: any graph on n vertices with no isolated vertices has a matching of size ≥ n/3 (I think). Actually, the correct bound is: a maximal matching has size ≥ n/2 / Δ... no.

Let me think about it differently. A maximal matching in W has the property that every edge in W shares an endpoint with a matching edge. Since every vertex is incident to a W-edge, every vertex is either in the matching or adjacent (in W) to a matching vertex. So the matching is a vertex cover... no, the matching edges' endpoints form a vertex cover of W. So the matching covers all vertices (in the sense that every vertex is either matched or adjacent to a matched vertex in W).

Actually, a maximal matching M in W: every edge of W shares an endpoint with some edge of M. Since every vertex is incident to some edge of W, every vertex is an endpoint of some edge of W, which shares an endpoint with M. So every vertex is either in M or adjacent (in W) to a vertex in M.

Hmm, this means the endpoints of M form a dominating set in W. But I want a matching that covers many vertices.

Let me just use the fact that W has no isolated vertices, so it has a matching of size ≥ n/2 / something. Actually, the minimum maximal matching can be as small as n/3 (for a star graph, the minimum maximal matching has size 1, but n/3 for n=3 gives 1). Hmm, for a star on n vertices, the minimum maximal matching has size 1, which is much less than n/2.

OK, let me not pursue the matching approach. Let me try something else.

Let me try the following direct approach:

For each vertex u, let f(u) be a witness. We have d(u) + d(f(u)) ≤ n.

Sum over all u: Σ d(u) + Σ d(f(u)) ≤ n².

Now, Σ d(f(u)) = Σ_v d(v) · indeg(v) where indeg(v) = |{u : f(u) = v}|.

We have Σ indeg(v) = n. 

So S + Σ_v d(v) · indeg(v) ≤ n² where S = Σ d(v) = 2|E|.

We want to show S ≤ n²/2, i.e., |E| ≤ n²/4.

From the inequality: S ≤ n² - Σ_v d(v) · indeg(v).

For this to give S ≤ n²/2, we need Σ_v d(v) · indeg(v) ≥ n²/2.

By the rearrangement inequality, Σ_v d(v) · indeg(v) is minimized when the largest d(v) is paired with the smallest indeg(v). 

We know Σ indeg(v) = n and indeg(v) ≥ 0. Also, if v has indeg(v) = 0, then no u has f(u) = v, meaning v is not a witness for anyone. But v itself has f(v) = some neighbor, so v has outdeg 1.

Hmm, we can't directly lower-bound Σ d(v) · indeg(v) without more information.

Let me think about what constraints we have on indeg.

If v has high degree d(v), can it have low indeg? indeg(v) is the number of vertices u that chose v as their witness. There's no direct constraint preventing v from having indeg 0.

For example, in K_{50,50}, each vertex has degree 50. We can choose f(u) for each u to be any neighbor. If we choose all f(u) to point to the same vertex v, then indeg(v) = 100 and indeg(others) = 0. Then Σ d(v) indeg(v) = 50 · 100 = 5000 = n²/2. So S + 5000 ≤ 10000, S ≤ 5000, |E| ≤ 2500. ✓.

But if we choose f more spread out, say indeg(v) = 1 for all v, then Σ d(v) indeg(v) = Σ d(v) = S. So S + S ≤ n², S ≤ n²/2, |E| ≤ n²/4. ✓.

If indeg is concentrated on low-degree vertices, Σ d(v) indeg(v) could be small. For example, if all indeg is on vertices with degree 1, Σ d(v) indeg(v) = n · 1 = n. Then S ≤ n² - n, |E| ≤ (n²-n)/2. For n = 100, this is 4950, which is way more than 2500.

But can this actually happen? If all witnesses point to degree-1 vertices, then every vertex u has f(u) = v where d(v) = 1. This means v's only neighbor is u (since d(v) = 1 and u is a neighbor of v). So f(u) = v means v is a pendant vertex attached only to u. And N(u) ∩ N(v) = N(u) ∩ {u} = ∅ (since u ∉ N(u)). ✓. 

But then u has a pendant neighbor v. The edge uv is a witness edge. Now, u has degree d(u) ≤ n - 1 (at most n-1 neighbors). And d(u) + d(v) = d(u) + 1 ≤ n, so d(u) ≤ n - 1. That's always true.

In this scenario, each vertex u has a pendant neighbor. But a pendant vertex has degree 1, so it's the pendant neighbor of only one vertex. So we need at least n pendant vertices, one for each u. But pendant vertices are also vertices in the graph, so if u has pendant v, then v is one of the n vertices, and v also needs a witness. v's only neighbor is u, so f(v) = u. And N(v) ∩ N(u) = {u} ∩ N(u) = ∅ (since u ∉ N(u)). ✓.

So the witness pairs are (u, v) where v is pendant to u. Each pair uses 2 vertices, and we need n/2 pairs. So we have n/2 "center" vertices and n/2 "pendant" vertices. Each center u has a pendant v, and u can have other neighbors too.

The centers can be connected among themselves. Each center u has d(u) = 1 (pendant) + (number of center neighbors). The pendants have d(v) = 1.

For the pendants, the condition is satisfied (witness is the center). For the centers, the witness is the pendant. N(u) ∩ N(v) = N(u) ∩ {u} = ∅ (since u ∉ N(u)). ✓. Wait, N(v) = {u} (v's only neighbor is u). N(u) ∩ {u} = ∅ since u ∉ N(u). ✓.

So the centers can form any graph among themselves! The total edges = (edges among centers) + n/2 (pendant edges).

The centers form a graph on n/2 vertices. To maximize total edges, maximize edges among centers. The maximum is C(n/2, 2) = (n/2)(n/2 - 1)/2.

Total edges = (n/2)(n/2 - 1)/2 + n/2 = n/2 · ((n/2 - 1)/2 + 1) = n/2 · (n/2 + 1)/2 = n(n+2)/8.

For n = 100: 100 · 102 / 8 = 1275. Much less than 2500.

So this construction gives fewer edges. The point is that using pendant witnesses "wastes" vertices.

OK so the bound S + Σ d(v) indeg(v) ≤ n² doesn't directly give S ≤ n²/2 because indeg can be concentrated on low-degree vertices. But in that case, the graph structure is constrained in other ways.

Let me think about this more carefully. The issue is that the algebraic bound is too weak. I need to use the structure of the graph more.

Let me try a different approach. Let me think about the problem in terms of the following:

For each vertex u, let f(u) = v be its witness. The key property is N(u) ∩ N(v) = ∅. This means:
- No neighbor of u (other than v) is a neighbor of v.
- No neighbor of v (other than u) is a neighbor of u.
- Equivalently, the edge uv is "isolated" in the sense that the neighborhoods of u and v are disjoint.

This means that in the graph, the vertices can be partitioned (relative to the edge uv) into:
- {u, v}
- N(u) \ {v} (neighbors of u other than v)
- N(v) \ {u} (neighbors of v other than u)
- R = V \ ({u,v} ∪ N(u) ∪ N(v)) (the rest, not adjacent to either u or v)

And |N(u) \ {v}| + |N(v) \ {u}| + |R| = n - 2, with |N(u) \ {v}| = d(u) - 1, |N(v) \ {u}| = d(v) - 1.

Now, let me think about a proof using the following idea:

For each vertex u, the witness edge {u, f(u)} "separates" the graph. The neighborhoods of u and f(u) are disjoint. 

Let me try to use an averaging argument.

For each vertex u, d(u) + d(f(u)) ≤ n. 

Consider the sum Σ_u (d(u) + d(f(u))) ≤ n².

Now, Σ_u d(u) = 2|E| = S. And Σ_u d(f(u)) = Σ_v d(v) · indeg(v).

So S + Σ_v d(v) · indeg(v) ≤ n².

Now, I need another inequality. Let me think about what other constraints we have.

For each u, f(u) ∈ N(u), so {u, f(u)} is an edge. The witness edges form a subgraph W. Each vertex has at least one incident witness edge.

Consider the sum Σ_u d(f(u))². Hmm, not sure.

Let me try to use the constraint that f(u) ∈ N(u) more carefully.

Since f(u) ∈ N(u), the edge {u, f(u)} exists. So u contributes 1 to d(f(u)). In other words, Σ_u [f(u) = v] ≤ d(v) for each v (the number of u's that point to v is at most d(v), since each such u must be a neighbor of v).

So indeg(v) ≤ d(v) for all v.

This is a key constraint! indeg(v) ≤ d(v).

Now, Σ_v d(v) · indeg(v) ≥ Σ_v d(v) · indeg(v). We want to lower-bound this.

We have: Σ indeg(v) = n, 0 ≤ indeg(v) ≤ d(v), and Σ d(v) = S.

Minimize Σ d(v) · indeg(v) subject to Σ indeg(v) = n, 0 ≤ indeg(v) ≤ d(v).

By the rearrangement inequality, this is minimized when indeg is concentrated on vertices with smallest d(v). But indeg(v) ≤ d(v), so if we concentrate indeg on low-degree vertices, we're limited by their degree.

Let me think about this optimization. Sort vertices by degree: d_1 ≤ d_2 ≤ ... ≤ d_n. We want to minimize Σ d_i · indeg_i subject to Σ indeg_i = n, 0 ≤ indeg_i ≤ d_i.

To minimize, assign indeg to the smallest d_i first, up to their capacity d_i.

If d_1 + d_2 + ... + d_k ≥ n for some k, then we can assign all indeg to the first k vertices. The minimum would be Σ_{i=1}^{k-1} d_i² + d_k · (n - Σ_{i=1}^{k-1} d_i).

But we also have the constraint Σ d_i = S. 

This is getting complicated. Let me try a different approach.

Actually, let me use the constraint indeg(v) ≤ d(v) more directly.

Σ_v d(v) · indeg(v) ≥ Σ_v indeg(v)² (by Cauchy-Schwarz? No, that's the wrong direction.)

Actually, since indeg(v) ≤ d(v), we have d(v) ≥ indeg(v), so d(v) · indeg(v) ≥ indeg(v)². Thus:

Σ_v d(v) · indeg(v) ≥ Σ_v indeg(v)².

By Cauchy-Schwarz: Σ_v indeg(v)² ≥ (Σ_v indeg(v))² / n = n²/n = n.

So Σ_v d(v) · indeg(v) ≥ n. This gives S ≤ n² - n, |E| ≤ (n²-n)/2. For n = 100, this is 4950. Too weak.

But we also have Σ d(v) = S and indeg(v) ≤ d(v). Let me use these together.

We have S + Σ d(v) indeg(v) ≤ n² and Σ d(v) indeg(v) ≥ Σ indeg(v)² ≥ n²/n = n.

This gives S ≤ n² - n. Not strong enough.

Let me try to get a better lower bound on Σ d(v) indeg(v).

We have indeg(v) ≤ d(v) and Σ indeg(v) = n and Σ d(v) = S.

Minimize Σ d(v) indeg(v) subject to these constraints.

Using Lagrange multipliers or by analysis: to minimize Σ d_i · x_i subject to Σ x_i = n, 0 ≤ x_i ≤ d_i, and Σ d_i = S (but the d_i are fixed, not variables).

Given fixed d_i, minimize Σ d_i x_i subject to Σ x_i = n, 0 ≤ x_i ≤ d_i.

This is a linear program. The minimum is achieved by setting x_i = d_i for the smallest d_i's until we reach Σ x_i = n.

Let the vertices be sorted d_1 ≤ d_2 ≤ ... ≤ d_n. Set x_i = d_i for i = 1, ..., k-1, and x_k = n - Σ_{i=1}^{k-1} d_i, where k is such that Σ_{i=1}^{k-1} d_i < n ≤ Σ_{i=1}^k d_i.

The minimum is Σ_{i=1}^{k-1} d_i² + d_k (n - Σ_{i=1}^{k-1} d_i).

Now, we also have Σ_{i=1}^n d_i = S. And we need Σ_{i=1}^k d_i ≥ n (so that we can assign all indeg to the first k vertices).

If S = Σ d_i and we need Σ_{i=1}^k d_i ≥ n, then k ≤ n (obviously). The question is: what's the minimum of Σ_{i=1}^{k-1} d_i² + d_k (n - Σ_{i=1}^{k-1} d_i) given that Σ d_i = S?

This depends on the degree sequence. To minimize Σ d(v) indeg(v), we want the low-degree vertices to have as small degree as possible and absorb all the indeg.

Extreme case: d_1 = d_2 = ... = d_m = 1 (m vertices of degree 1), and the rest have high degree. Then Σ_{i=1}^m d_i = m. If m ≥ n, we can set indeg_i = 1 for i = 1, ..., n, and Σ d_i indeg_i = n · 1 = n. But m ≤ n (only n vertices), and if m = n, all vertices have degree 1, S = n, |E| = n/2. Not interesting.

If m < n, say m vertices have degree 1 and n - m have higher degree. Σ_{i=1}^m d_i = m. We need n - m more indeg from the remaining vertices. The (m+1)-th vertex has degree d_{m+1}. Set indeg_{m+1} = min(d_{m+1}, n - m). If d_{m+1} ≥ n - m, then Σ d_i indeg_i = m · 1 + d_{m+1} · (n - m). 

To minimize this, we want d_{m+1} to be as small as possible. If d_{m+1} = n - m, then Σ d_i indeg_i = m + (n-m)². Hmm.

This is getting very complicated and I'm not sure it leads to a clean bound. Let me try a completely different approach.

Let me go back to thinking about the problem structurally.

Key observation: In any bipartite graph with no isolated vertices, the condition is automatically satisfied (as every edge has N(u) ∩ N(v) = ∅ since neighborhoods are in different parts). The maximum edges in a bipartite graph on n vertices is ⌊n²/4⌋.

For non-bipartite graphs, the condition is more restrictive. The question is whether a non-bipartite graph can satisfy the condition and have more than ⌊n²/4⌋ edges.

Let me think about this. Suppose G is not bipartite. Then G contains an odd cycle. Let C be the shortest odd cycle (which is an induced cycle, i.e., a hole). 

Actually, let me think about a specific non-bipartite construction and count edges.

Construction: Take K_{50,50} and try to add edges while maintaining the condition.

We showed that adding any edge within a part breaks the condition for the endpoints. But what if we also remove some edges?

Specifically: add edge a1-a2 within A, and remove edges a1-b1 and a2-b2 (for specific b1, b2). Now:

d(a1) = 50 - 1 + 1 = 50 (lost b1, gained a2).
d(a2) = 50 - 1 + 1 = 50 (lost b2, gained a1).
d(b1) = 50 - 1 = 49 (lost a1).
d(b2) = 50 - 1 = 49 (lost a2).

For a1: N(a1) = (B \ {b1}) ∪ {a2}. Need witness v with N(a1) ∩ N(v) = ∅.
- v = a2: N(a2) = (B \ {b2}) ∪ {a1}. N(a1) ∩ N(a2) = (B \ {b1, b2}) ≠ ∅ (since |B| = 50 > 2). Fails.
- v ∈ B \ {b1}: say v = b3. N(b3) = A (all of A, since b3 is still connected to all of A). N(a1) ∩ N(b3) = ((B\{b1}) ∪ {a2}) ∩ A = {a2} ≠ ∅. Fails.

So a1 still has no witness. The problem is that a1's neighborhood includes a2 (in A), and any B-vertex's neighborhood includes all of A (including a2).

To fix this, we'd need to also remove a2 from the neighborhoods of all B-vertices that a1 might use as witnesses. But a B-vertex b has N(b) = A (or A minus some vertices). If we remove a2 from N(b), we remove the edge a2-b. But then a2 loses another neighbor.

This cascading effect makes it very hard to add edges within parts while maintaining the condition. It seems like the bipartite structure is essential for maximizing edges.

Let me try to prove that the maximum is ⌊n²/4⌋ by showing that any graph satisfying the condition has at most ⌊n²/4⌋ edges.

Proof approach using the following lemma:

Lemma: If G satisfies the condition, then V can be partitioned into two sets A and B such that |E(G)| ≤ |A| · |B| + (edges within A) + (edges within B), and the edges within A and within B are "limited" in some way.

Hmm, this is vague. Let me try a more concrete approach.

Actually, let me try to prove it by induction, being more careful about the induction step.

Theorem: For any graph G on n vertices satisfying the condition, |E(G)| ≤ ⌊n²/4⌋.

Proof by induction on n.

Base: n = 1: 0 edges, 0 ≤ 0. ✓. n = 2: at most 1 edge, 1 ≤ 1. ✓.

Inductive step: Assume the result for all graphs on fewer than n vertices satisfying the condition.

Let G be a graph on n vertices satisfying the condition. 

Case 1: G has a vertex u with d(u) = 0. Then u has no neighbor, so the condition fails (u needs a neighbor v ∈ N(u), but N(u) = ∅). So G has no isolated vertices.

Case 2: G has a vertex u with d(u) = 1. Let v be the unique neighbor of u. Then f(u) = v (the only choice). N(u) ∩ N(v) = {v} ∩ N(v) = ∅ (since v ∉ N(v)). ✓. 

Now, consider G' = G - u (remove u). G' has n-1 vertices. Does G' satisfy the condition?

For any vertex w ≠ u in G': w had a witness f(w) in G. If f(w) ≠ u, then f(w) is still in G', and N_{G'}(w) ∩ N_{G'}(f(w)) ⊆ N_G(w) ∩ N_G(f(w)) = ∅. ✓.

If f(w) = u, then u was w's witness. But u has degree 1, so N(u) = {v}. For u to be w's witness, w must be a neighbor of u, so w = v. So f(v) = u. Now, in G', v needs a new witness. v's neighbors in G' are N_G(v) \ {u}. We need some v' ∈ N_{G'}(v) with N_{G'}(v) ∩ N_{G'}(v') = ∅.

This might not hold. So G' might not satisfy the condition.

Hmm. So the induction doesn't work directly.

Let me try removing both u and v (the degree-1 vertex and its neighbor).

G'' = G - {u, v}. This has n - 2 vertices. Does G'' satisfy the condition?

For w ∈ G'' with f(w) ∉ {u, v}: the witness is still in G'', and the condition holds. ✓.

For w ∈ G'' with f(w) = u: w must be a neighbor of u, so w = v. But v ∉ G''. So this case doesn't arise.

For w ∈ G'' with f(w) = v: w is a neighbor of v. In G'', w needs a new witness. This might not exist.

So again, G'' might not satisfy the condition.

The induction approach is tricky because removing vertices can break the condition for other vertices.

Let me try a different approach. Instead of induction, let me try a direct counting argument.

Direct approach:

For each vertex u, let f(u) be a witness. We have:
1. f(u) ∈ N(u) (witness is a neighbor)
2. N(u) ∩ N(f(u)) = ∅ (no common neighbors)
3. d(u) + d(f(u)) ≤ n (from 2)

From 1: indeg(v) ≤ d(v) for all v (as argued before).

Now, consider the following. For each vertex u, define g(u) = f(u). We have a function g: V → V with g(u) ∈ N(u) and d(u) + d(g(u)) ≤ n.

Let's think about the edges of G. Each edge e = {u, w} contributes to the degrees of u and w. 

For each vertex u, d(u) ≤ n - d(g(u)). 

Sum: S = Σ d(u) ≤ Σ (n - d(g(u))) = n² - Σ d(g(u)) = n² - Σ_v d(v) · indeg(v).

So S ≤ n² - Σ_v d(v) · indeg(v). ... (*)

Also, S = Σ d(v) and indeg(v) ≤ d(v), Σ indeg(v) = n.

Now, I need another inequality relating S and Σ d(v) indeg(v).

Consider: Σ_v d(v) · indeg(v) = Σ_v d(v) · indeg(v). 

Since indeg(v) ≤ d(v), we have d(v) · indeg(v) ≥ indeg(v) · indeg(v) = indeg(v)². So Σ d(v) indeg(v) ≥ Σ indeg(v)² ≥ n²/n = n (by QM-AM). This gives S ≤ n² - n. Not strong enough.

But we also have S = Σ d(v) ≥
The user wants me to solve the math problem directly. Let me check for answer leaks first.

The problem: Let G be a simple graph with 100 vertices such that for each vertex u, there exists a vertex v ∈ N(u) and N(u) ∩ N(v) = ∅. Find the maximal possible number of edges in G.

No answer leak detected. Let me solve.

So the condition: for every vertex u, there's a neighbor v of u such that u and v have no common neighbor. This means the edge uv is not part of any triangle (since if there were a common neighbor w, then u,v,w form a triangle). Actually N(u) ∩ N(v) = ∅ means no vertex is adjacent to both u and v. In particular, u ∉ N(u) (no self-loops) and v ∉ N(v), but u ∈ N(v) and v ∈ N(u). So the condition N(u) ∩ N(v) = ∅ means no common neighbor, which means edge uv is not in any triangle.

So the condition is: every vertex u is incident to at least one edge that is not in any triangle (i.e., every vertex is incident to at least one "triangle-free edge").

We want to maximize the number of edges.

Let me think. We want a graph on 100 vertices where every vertex has at least one incident edge that's in no triangle, and we maximize edges.

Strategy: To maximize edges, we want most of the graph to be a complete graph (or dense), but each vertex needs at least one "triangle-free" edge.

Idea: Take a complete graph K_{99} on 99 vertices, and add one extra vertex w connected to... hmm. If w is connected to just one vertex of K_{99}, then w has its triangle-free edge (the edge to that vertex, since w has no other neighbors so no common neighbor). But the vertex in K_{99} that w connects to — its edge to w: is it triangle-free? w's only neighbor is that vertex, so N(w) = {that vertex}, and N(that vertex) ∩ N(w) = N(that vertex) ∩ {that vertex}... wait N(w) = {u} where u is the vertex. N(u) ∩ N(w) = N(u) ∩ {u}. But u ∉ N(u) (no self loop), so N(u) ∩ {u} = ∅. Yes! So edge wu is triangle-free. Good for both w and u.

But the other 98 vertices in K_{99}: each needs a triangle-free edge. In K_{99}, every edge is in a triangle (since 99 ≥ 3). So those 98 vertices have no triangle-free edge. Bad.

So we need every vertex to have a triangle-free edge.

Alternative idea: Partition vertices into pairs, each pair connected by an edge, and these edges are triangle-free. Then make the rest as dense as possible.

Consider: take a perfect matching of 50 edges that are all triangle-free, then add as many other edges as possible while keeping those 50 edges triangle-free.

If we have a matching {a_1 b_1, ..., a_50 b_50} that is triangle-free, each edge a_i b_i has no common neighbor. To keep a_i b_i triangle-free, no vertex can be adjacent to both a_i and b_i. 

To maximize total edges: For each pair (a_i, b_i), the constraint is N(a_i) ∩ N(b_i) = ∅ (for the matching edge). We want to maximize edges subject to each pair having disjoint neighborhoods (excluding each other).

Actually let's think of it as: we have 50 pairs. Within each pair, the edge exists. Between pairs, we can add edges freely as long as for each pair (a_i, b_i), no outside vertex is adjacent to both a_i and b_i.

So for each pair i and each pair j (j ≠ i), the vertices a_i, b_i can connect to vertices in pair j, but each vertex in pair j can be adjacent to at most one of {a_i, b_i}.

Hmm, let me think about the structure. Let's denote pairs P_1, ..., P_50. For pair P_i = {a_i, b_i}, the edge a_i b_i is triangle-free, meaning no vertex is adjacent to both a_i and b_i.

Consider the complete graph on 100 vertices has C(100,2) = 4950 edges. We need to remove edges to satisfy constraints.

Actually, let me think differently. Consider the complement or think about a specific construction.

Construction: Take 50 copies of K_2 (edges), and between every two pairs, make it a complete bipartite-ish structure. 

Let me think: For pairs P_i and P_j, we want to maximize edges between them subject to: for pair P_i, no vertex adjacent to both a_i and b_i; for pair P_j, no vertex adjacent to both a_j and b_j.

Between P_i = {a_i, b_i} and P_j = {a_j, b_j}: possible edges are a_i a_j, a_i b_j, b_i a_j, b_i b_j (4 edges). Constraints:
- For P_i's triangle-free edge: a_j can't be adjacent to both a_i and b_i; b_j can't be adjacent to both a_i and b_i.
- For P_j's triangle-free edge: a_i can't be adjacent to both a_j and b_j; b_i can't be adjacent to both a_j and b_j.

So each of a_j, b_j is adjacent to at most one of {a_i, b_i}, and each of a_i, b_i is adjacent to at most one of {a_j, b_j}.

This is like a 2x2 0-1 matrix where each row has at most one 1 and each column has at most one 1. Max number of 1s = 2 (a permutation matrix). So between any two pairs, at most 2 edges.

So total edges = 50 (matching) + C(50,2) * 2 = 50 + 1225 * 2 = 50 + 2450 = 2500.

Can we achieve 2 edges between every pair of pairs? Yes: e.g., connect a_i to a_j and b_i to b_j for all i,j (so a's form a clique and b's form a clique). Then check: edge a_i b_i: is a_j adjacent to both a_i and b_i? a_j adjacent to a_i (yes, in a-clique) and to b_i? b_i is in b-clique, a_j is in a-clique, a_j-b_i not an edge. So a_j not adjacent to b_i. Good. Similarly b_j adjacent to b_i but not a_i. So no common neighbor. Triangle-free confirmed.

So construction: a_1,...,a_50 form K_50, b_1,...,b_50 form K_50, and edges a_i b_i. Total = C(50,2) + C(50,2) + 50 = 1225 + 1225 + 50 = 2500.

Now is 2500 optimal? We need to prove we can't do better.

Let me think about the upper bound. The condition: every vertex has a triangle-free incident edge. 

Hmm, but maybe a non-matching structure does better. Let me think more generally.

Actually, let me reconsider. The constraint is per-vertex: each vertex u has SOME neighbor v with N(u)∩N(v)=∅. It doesn't have to be a matching; multiple vertices could share the same triangle-free edge partner.

Let me think about an upper bound. 

Consider the graph G. For each vertex u, choose one "witness" edge e_u = uv_u that is triangle-free (v_u is a neighbor with no common neighbor). 

A triangle-free edge uv: N(u) ∩ N(v) = ∅. Note deg(u) + deg(v) ≤ n = 100 (since N(u) and N(v) are disjoint subsets of V \ {u,v}... wait, N(u) ⊆ V\{u}, N(v) ⊆ V\{v}, and N(u)∩N(v)=∅. Also v ∈ N(u) and u ∈ N(v). So N(u) and N(v) are disjoint. |N(u)| + |N(v)| ≤ 100 (they're disjoint subsets of the 100 vertices, but v ∈ N(u) and u ∈ N(v), and these are different vertices, so |N(u)|+|N(v)| ≤ 100). So deg(u) + deg(v) ≤ 100 for each triangle-free edge uv.

Now, sum over all vertices: Σ deg(u) = 2|E|. 

For each vertex u, there's a triangle-free edge uv_u with deg(u) + deg(v_u) ≤ 100.

Hmm, let me think about how to bound total edges.

Let S be the set of triangle-free edges. Every vertex is incident to at least one edge in S. 

For each edge e = uv in S, deg(u) + deg(v) ≤ 100.

Sum over edges in S: Σ_{uv ∈ S} (deg(u) + deg(v)) ≤ 100 |S|.

The left side: Σ_{uv ∈ S} (deg(u) + deg(v)) = Σ_u deg(u) * (number of S-edges incident to u) ≥ Σ_u deg(u) * 1 = 2|E| (since each vertex incident to ≥1 S-edge).

Wait, that gives 2|E| ≤ 100 |S|. And |S| ≤ ? Each vertex incident to ≥1 S-edge, so |S| ≥ 50 (S is an edge cover, min edge cover... actually |S| could be as low as 50 if it's a perfect matching, but could be more). This gives 2|E| ≤ 100|S|, not directly useful for upper bound since |S| can be large.

Hmm wait, we want upper bound on |E|. Let me reconsider.

Actually we have 2|E| ≤ Σ_{uv∈S}(deg(u)+deg(v)) ≤ 100|S|. So |E| ≤ 50|S|. To minimize the bound we want |S| small, but |S| ≥ 50. So |E| ≤ 50|S|, and if |S| = 50, |E| ≤ 2500. But if |S| > 50, the bound is weaker. So this only gives |E| ≤ 2500 when |S| = 50.

But maybe we can show |S| = 50 is forced or that the bound still holds. Hmm, not directly.

Let me think differently. Let me reconsider: we need a better argument.

Alternative: Let's think about it as follows. Consider the subgraph H = (V, S) of triangle-free edges that are "used" (we pick a set S of triangle-free edges forming an edge cover). Actually, let me pick S to be a minimal edge cover (each vertex covered, minimal). A minimal edge cover in a graph with no isolated vertices has size n - ν where ν is the matching number... actually for the edge cover, minimum edge cover = n - (max matching). Hmm.

Let me just try: pick a maximum matching M in the graph of triangle-free edges (call this graph T, with vertex set V and edges = triangle-free edges). Every vertex has degree ≥ 1 in T. 

Actually, let me think about whether 2500 is truly the max. Let me consider small cases or other constructions.

Alternative construction: What if we don't use a perfect matching of triangle-free edges but something else?

Consider: one vertex w connected to all others, and... no, w's triangle-free edge: w needs a neighbor v with N(w)∩N(v)=∅. If w is connected to everyone, N(w) = 99 vertices, then v must have N(v) disjoint from N(w), but v ∈ N(w) so N(v) ⊆ N(w) ∪ {w} \ {v}... actually N(v) ⊆ V\{v}, and N(w) = V\{w}. N(v) ∩ N(w): since N(w) = V\{w}, N(v) ∩ N(w) = N(v) \ {w} (if w ∈ N(v)). For this to be ∅, N(v) ⊆ {w}, so deg(v) ≤ 1, meaning v only connected to w. But then v's only neighbor is w, and v needs its own triangle-free edge: v's neighbor is w, N(v)∩N(w) = {w}∩(V\{w})... wait N(v) = {w}, N(w) = V\{w}, intersection = ∅. Good. So edge vw is triangle-free for both. But all other 98 vertices need triangle-free edges too, and they're all connected to w (and possibly each other). If they form a clique among themselves plus w, every edge among them is in a triangle. So they need triangle-free edges, which must go to... vertices with very small degree. This seems to limit things.

Let me just try to verify 2500 is optimal more carefully.

Upper bound attempt: Let M be a maximum matching in the triangle-free-edge graph T. Let |M| = m. The vertices not covered by M form an independent set in T (since M is maximum), so they have no triangle-free edges among themselves. But every vertex has a triangle-free edge, so each uncovered vertex has a triangle-free edge to a covered vertex.

Hmm, this is getting complex. Let me think about the structure more.

Actually, let me reconsider the problem. Let me re-examine if we can beat 2500.

Suppose we have the construction with two K_50's and a matching between them = 2500 edges. Can we add any edge? Adding edge a_i b_j (i≠j): then edge a_i b_i — is it still triangle-free? a_i b_i: common neighbor? a_j is adjacent to a_i (clique) and now b_j is adjacent to a_i (new edge) and b_j adjacent to b_i (clique). Is a_j adjacent to b_i? No. Is b_j adjacent to both a_i and b_i? b_j adjacent to a_i (new edge, yes) and b_j adjacent to b_i (b-clique, yes). So b_j is a common neighbor of a_i and b_i! So edge a_i b_i is no longer triangle-free. Then a_i needs another triangle-free edge, and b_i needs another. This breaks things. So we can't easily add edges.

Let me think about whether a different structure could give more.

What about: three cliques? Say partition into groups. Hmm.

Let me think about the general upper bound more carefully.

Claim: |E| ≤ 2500.

Proof approach: For each vertex u, let f(u) be a chosen neighbor with N(u)∩N(f(u))=∅. Note f(f(u)) might not be u, but the edge u f(u) is triangle-free so actually N(f(u))∩N(u)=∅ too, meaning u is a valid witness for f(u) as well. But f(u) might choose a different witness.

Key fact: for the chosen edge uv (triangle-free), deg(u)+deg(v) ≤ 100.

Consider the directed graph where each u points to f(u). Each vertex has out-degree 1. The underlying edges form a set S (triangle-free edges), and S is an edge cover (every vertex incident to ≥1 edge of S, since u is incident to u f(u)).

Now, Σ_u deg(u) = 2|E|. Also Σ_u deg(f(u)) = Σ_v deg(v) * |f^{-1}(v)|.

We have deg(u) + deg(f(u)) ≤ 100 for all u. Sum over all u:
Σ_u deg(u) + Σ_u deg(f(u)) ≤ 100 n = 10000.
2|E| + Σ_v deg(v)|f^{-1}(v)| ≤ 10000.

Hmm, Σ_v deg(v)|f^{-1}(v)| ≥ ? Not obviously helpful.

Since Σ_u deg(f(u)) = Σ_v deg(v) · indeg(v) where indeg(v) = |f^{-1}(v)| ≥ 0, and Σ_v indeg(v) = n = 100.

By rearrangement, Σ_v deg(v)·indeg(v) ≥ (Σ_v deg(v))(Σ indeg(v))/n ... no wait, that's not right in general. Actually by Chebyshev or rearrangement, if we want a lower bound on Σ deg(v)·indeg(v) given Σ indeg = n, the minimum is when high indeg pairs with low deg. We can't bound it below easily without knowing structure.

Hmm. Let me think differently.

Actually, note that indeg(v) ≥ 1 iff v is in the image of f. The image of f has size ≤ n. Also, if v is not in the image, indeg(v) = 0. 

Let me think about it as: we want to maximize 2|E| = Σ deg(u) subject to: there exists a function f with each u→f(u) a triangle-free edge, deg(u)+deg(f(u)) ≤ 100.

This is like: we have a directed functional graph, and the constraint deg(u)+deg(f(u)) ≤ 100.

To maximize Σ deg(u), we'd want the constraint to be loose. The constraint deg(u)+deg(f(u)) ≤ 100 binds when degrees are high.

If we pair up vertices (f is an involution, perfect matching), then deg(u)+deg(f(u)) ≤ 100 for each pair, and Σ deg = Σ_pairs (deg+deg) ≤ 50 · 100 = 5000, so |E| ≤ 2500. 

But if f is not a perfect matching (some vertex has high indeg), can we do better? Suppose vertex v has indeg k (k vertices point to v). Then deg(v) + deg(u_i) ≤ 100 for each of the k vertices u_i. So deg(u_i) ≤ 100 - deg(v) for each. And v itself points to f(v) with deg(v)+deg(f(v)) ≤ 100.

The total contribution: v contributes deg(v), the k vertices contribute ≤ k(100 - deg(v)), and f(v) is among... hmm, f(v) could be one of the u_i or not.

Let me think of it as: the functional graph of f decomposes into components, each a cycle with trees hanging off. 

For a component, let's compute the max of Σ deg over the component given the constraints.

Consider a cycle C of length ℓ: v_1 → v_2 → ... → v_ℓ → v_1. Constraints: deg(v_i) + deg(v_{i+1}) ≤ 100 for each i. Sum: Σ deg(v_i) + Σ deg(v_{i+1}) = 2 Σ deg(v_i) ≤ 100ℓ, so Σ deg(v_i) ≤ 50ℓ.

Now trees hanging off cycle vertices: say vertex v (on cycle or tree) has children u_1,...,u_k (pointing to v). Each has deg(u_i) + deg(v) ≤ 100, so deg(u_i) ≤ 100 - deg(v). The u_i's might have their own children.

This is like: for a tree rooted at v (with edges pointing toward v, i.e., children point to parent), the constraint is deg(child) + deg(parent) ≤ 100. To maximize Σ deg over the tree, given deg(parent) = d, each child has deg ≤ 100 - d, and then their children have deg ≤ 100 - (100-d) = d, etc. So it alternates.

Let me compute: root v with deg d. Children (level 1): each deg ≤ 100-d. Their children (level 2): deg ≤ d. Level 3: ≤ 100-d. Etc.

If v has k_1 children, each with k_2 children, etc. Total deg sum = d + k_1(100-d) + k_1 k_2 · d + k_1 k_2 k_3 (100-d) + ...

To maximize, we want many vertices. But total vertices = 100. 

Hmm, let me think about whether trees help or hurt compared to pure matching.

Pure 2-cycle (matching pair): 2 vertices, Σ deg ≤ 100, avg 50 per vertex.

Tree: root v (deg d), one child u (deg 100-d). Σ = 100 for 2 vertices. Same as matching. Add a grandchild w (child of u): deg(w) ≤ d. Σ = 100 + d for 3 vertices. Avg = (100+d)/3. If d = 50, avg 50. If d < 50, avg < 50. 

Actually for 3 vertices with root d, child 100-d, grandchild d: Σ = 100 + d. To get Σ = 150 (avg 50), need d = 50. So if d=50, 3 vertices give Σ=150, same avg. If d=50, child deg 50, grandchild deg 50. All 50. That's just all degrees 50, consistent.

Hmm, so it seems like the average degree is at most 50 regardless, giving |E| ≤ 2500. Let me verify this more carefully.

Claim: For any functional graph component (cycle + trees) with the constraint deg(u)+deg(f(u)) ≤ 100, the sum of degrees is at most 50 times the number of vertices.

Proof: Consider the component with vertex set W, |W| = s. The edges of the functional graph form a connected functional graph (one cycle, trees). It's a connected graph on s vertices with s edges (each vertex one out-edge), so it's a tree plus one edge = unicyclic.

Actually, let me use a cleaner argument. The functional graph on W has s vertices and s directed edges (each vertex has outdegree 1). The underlying undirected graph has s edges on s vertices and is connected (one component), so it has exactly s edges and s vertices: it's unicyclic (one cycle, trees attached).

Now, sum the constraint deg(u) + deg(f(u)) ≤ 100 over all u ∈ W:
Σ_{u∈W} deg(u) + Σ_{u∈W} deg(f(u)) ≤ 100s.

The first sum is D = Σ_{u∈W} deg(u). The second sum: Σ_{u∈W} deg(f(u)) = Σ_{v∈W} deg(v) · indeg_W(v) where indeg_W is indegree within the component. 

Hmm, this doesn't directly give D ≤ 50s because the second sum isn't equal to D.

Σ_{u∈W} deg(f(u)): as u ranges over W, f(u) ranges over W (since the component is closed under f). Each v ∈ W appears as f(u) exactly indeg(v) times. So Σ_{u∈W} deg(f(u)) = Σ_{v∈W} deg(v)·indeg(v).

In a functional graph component, Σ indeg(v) = s (total indegree = total outdegree = s). But indeg(v) varies. On the cycle, each vertex has indeg ≥ 1 (from cycle) plus tree contributions. Tree leaves have indeg 0.

So D + Σ_v deg(v)·indeg(v) ≤ 100s.

We want D ≤ 50s. This requires Σ_v deg(v)·indeg(v) ≥ D, i.e., Σ_v deg(v)(indeg(v) - 1) ≥ 0, i.e., Σ_v deg(v)·indeg(v) ≥ Σ_v deg(v).

Is Σ deg(v)·indeg(v) ≥ Σ deg(v)? That's Σ deg(v)(indeg(v)-1) ≥ 0. Not necessarily true! Vertices with indeg 0 (leaves) contribute negatively.

Hmm. So this approach doesn't directly work. Let me reconsider.

Let me think about a potential counterexample. Can we beat 2500?

Consider: vertex v with very high degree, say deg(v) = 99 (connected to all). Then v needs a triangle-free edge to some u with deg(u) ≤ 1 (since deg(v)+deg(u) ≤ 100). So u has degree 1, connected only to v. Now u is covered. But the other 98 vertices each need triangle-free edges. 

Each of the 98 other vertices w: needs a triangle-free edge. w is connected to v (since v connects to all). For w's triangle-free edge to some x: deg(w)+deg(x) ≤ 100 and N(w)∩N(x)=∅. Since w is adjacent to v, and v is adjacent to almost everyone, x must not be adjacent to v (otherwise v ∈ N(w)∩N(x)). So x is not adjacent to v. The only vertex not adjacent to v is u (deg 1, only to v) — wait u IS adjacent to v. So everyone is adjacent to v. Then for any w, any triangle-free partner x must have v ∉ N(x), but everyone is adjacent to v. Contradiction unless x = v, but then edge wv: N(w)∩N(v) must be ∅, but N(v) is huge. So no.

So high-degree vertex doesn't work well. The matching construction seems good.

Let me try to prove the upper bound 2500 rigorously.

Let me use a different approach. Let's define for each vertex u a witness v(u) with uv(u) triangle-free. Consider the graph structure.

Alternative approach using the triangle-free edge cover:

Let T be the set of all triangle-free edges. T forms an edge cover of V (every vertex incident to some edge in T). 

For each triangle-free edge e = uv, deg(u) + deg(v) ≤ 100.

Let M be a maximum matching in T. |M| = m. Since T is an edge cover (no isolated vertices in T), the minimum edge cover has size n - m = 100 - m. But we're using M (maximum matching), not min edge cover.

Vertices covered by M: 2m. Uncovered: 100 - 2m, these form an independent set in T (no T-edge among them, by maximality of M). Each uncovered vertex has T-edges only to covered vertices.

Hmm, let me think about using the matching M directly.

For each edge uv ∈ M: deg(u) + deg(v) ≤ 100. Sum over M: Σ_{uv∈M}(deg(u)+deg(v)) ≤ 100m.

The LHS = Σ_{v covered by M} deg(v) = Σ_{v∈V} deg(v) - Σ_{v not covered} deg(v) = 2|E| - Σ_{uncovered} deg(v).

So 2|E| - Σ_{uncovered} deg(v) ≤ 100m, giving 2|E| ≤ 100m + Σ_{uncovered} deg(v).

Now, uncovered vertices: each has a triangle-free edge to a covered vertex w. For uncovered vertex x with triangle-free edge xw (w covered), deg(x) + deg(w) ≤ 100. Also, w is covered by M, so w is in some matching edge ww'. deg(w) + deg(w') ≤ 100.

Hmm, I want to bound Σ_{uncovered} deg(x). Each uncovered x has deg(x) ≤ 100 - deg(w_x) where w_x is its T-neighbor (covered). 

This is getting complicated. Let me think about whether the answer might not be 2500 and try to find the actual max via a different construction.

Let me reconsider. Maybe we can do better than 2500 with a cleverer structure.

What if we use a structure where some vertices have degree > 50 but compensate with low-degree partners, and the average still exceeds 50?

Consider: take the matching construction (2500) and try to modify. 

Actually, let me reconsider the constraint. The constraint is only that each vertex has AT LEAST ONE triangle-free edge. The rest of the edges can be in triangles.

In the matching construction, the matching edges are triangle-free, and all other edges (within the two cliques) are in triangles. That's fine.

Can we have a graph where some vertices have degree much higher than 50, as long as they have one triangle-free edge to a low-degree vertex?

Example: Take K_{98} (clique on 98 vertices) plus two vertices a, b. Connect a to all 98 vertices of K_{98}, connect b to only one vertex, say a. Wait, let me think.

We need every vertex to have a triangle-free edge. 

Construction attempt: Let's have 49 "low" vertices each paired with a "high" vertex, and 2 extra vertices. Hmm, let me think more carefully.

Let me try: Partition 100 vertices into 50 pairs (a_i, b_i). Make a_1,...,a_50 a clique (K_50). For b_i: connect b_i only to a_i. Then:
- Edge a_i b_i: N(a_i) = {all a_j, j≠i} ∪ {b_i}, N(b_i) = {a_i}. Intersection: N(a_i) ∩ N(b_i) = N(a_i) ∩ {a_i} = ∅ (since a_i ∉ N(a_i)). Triangle-free! Good.
- Each a_i has triangle-free edge a_i b_i. ✓
- Each b_i has triangle-free edge b_i a_i. ✓

Edges: C(50,2) [a-clique] + 50 [a_i b_i] = 1225 + 50 = 1275. That's way less than 2500.

OK so that's worse. The matching construction with two cliques is better because b's also form a clique.

Let me try asymmetric: a's form K_p, b's form K_q with p+q = 100, matching between them (but matching requires p = q = 50). If p ≠ q we can't have a perfect matching. 

What if we don't require a perfect matching of triangle-free edges? Let me think about a construction with two groups of unequal size.

Say group A has p vertices, group B has q = 100 - p vertices. A is a clique, B is a clique. Triangle-free edges: we need each vertex to have one. 

If we add edges between A and B, we need to be careful. In the matching construction, the cross edges a_i b_i are the triangle-free edges, and there are no other cross edges.

What if p = 60, q = 40? We need each of the 100 vertices to have a triangle-free edge. The triangle-free edges must be cross edges (between A and B) or... could be within A or B? Within a clique, every edge is in a triangle (if size ≥ 3). So triangle-free edges must be cross edges, and each must have no common neighbor.

A cross edge a b (a ∈ A, b ∈ B): N(a) ∩ N(b) = ∅. N(a) includes all other A-vertices (clique) and possibly some B-vertices. N(b) includes all other B-vertices and possibly some A-vertices. For N(a)∩N(b) = ∅, no vertex can be adjacent to both a and b. Since a is adjacent to all of A\{a} and b is adjacent to all of B\{b}, we need A\{a} and B\{b} to not be adjacent to the other endpoint. Specifically, no a' ∈ A\{a} is adjacent to b, and no b' ∈ B\{b} is adjacent to a. So b is adjacent to no A-vertex except a, and a is adjacent to no B-vertex except b.

So each triangle-free cross edge ab is "isolated" in the sense that a has no other B-neighbors and b has no other A-neighbors.

Now, each vertex needs at least one triangle-free edge. For a ∈ A, it needs a cross edge to some b ∈ B where a has no other B-neighbor and b has no other A-neighbor. Similarly for b ∈ B.

If a vertex a ∈ A has a triangle-free edge to b, then a has no other B-neighbor. So a's only cross edge is to b. Similarly b's only cross edge is to a. So triangle-free edges form a matching between A and B!

Wait, not exactly a matching: a could have its triangle-free edge to b, but a might have other cross edges that are NOT triangle-free. But we showed that if ab is triangle-free, then a has no other B-neighbor. So a has exactly one cross edge (to b), and it's triangle-free. So a cannot have other cross edges.

Hmm wait, that means if a ∈ A has a triangle-free cross edge to b, then a's only cross edge is ab. But a might need other cross edges for... no, a just needs one triangle-free edge. But other vertices might need a to have cross edges to them. 

Actually, the point is: if a has a triangle-free edge to b, a has no other B-neighbor. So a's degree = (p-1) [from A-clique] + 1 [b] = p. And b's degree = (q-1) + 1 = q.

For this to work for ALL vertices, every a ∈ A needs a triangle-free edge to some b, meaning every a has exactly one B-neighbor. And every b ∈ B needs a triangle-free edge to some a, meaning every b has exactly one A-neighbor. So the cross edges form a perfect matching between A and B, requiring |A| = |B| = 50.

So with the two-clique construction, we must have p = q = 50, giving 2500.

But maybe a non-clique construction does better? Let me think about whether 2500 is truly optimal.

Let me think about a more general upper bound.

General approach: Let's think about what limits us. 

Let me consider the "witness" function f: V → V where f(u) is a neighbor of u with N(u)∩N(f(u))=∅. As noted, deg(u)+deg(f(u)) ≤ 100.

Consider the functional graph of f. It decomposes into components, each with a directed cycle and in-trees.

For a component with vertex set W (|W|=s), let's think about the sum D_W = Σ_{u∈W} deg(u).

The edges of the functional graph within W: each u ∈ W has f(u) ∈ W (closed). The functional graph on W is connected (it's one component). 

Now I'll use a cleverer bound. For each u, deg(u) + deg(f(u)) ≤ 100. 

Sum over u ∈ W: D_W + Σ_{u∈W} deg(f(u)) ≤ 100s.

Now Σ_{u∈W} deg(f(u)) = Σ_{v∈W} deg(v) · indeg(v).

So D_W + Σ_v deg(v)·indeg(v) ≤ 100s, i.e., D_W ≤ 100s - Σ_v deg(v)·indeg(v).

We want to show D_W ≤ 50s, i.e., Σ_v deg(v)·indeg(v) ≥ 50s.

Hmm, is Σ_v deg(v)·indeg(v) ≥ 50s always true? Not obviously.

Let me think about a specific component. Consider a 2-cycle: u ↔ v (f(u)=v, f(v)=u). indeg(u)=1, indeg(v)=1. Σ deg·indeg = deg(u)+deg(v) ≤ 100 = 50·2. So D_W = deg(u)+deg(v) ≤ 100 = 50s. ✓ (tight)

Consider a 3-cycle: u→v→w→u. indeg each =1. Σ deg·indeg = deg(u)+deg(v)+deg(w) = D_W. Constraint: deg(u)+deg(v)≤100, deg(v)+deg(w)≤100, deg(w)+deg(u)≤100. Sum: 2D_W ≤ 300, D_W ≤ 150 = 50·3. ✓

Consider a tree: root v (on cycle or not) with child u (f(u)=v). Say v is on a 2-cycle with v'. indeg(v) = 1 (from v') + 1 (from u) = 2. indeg(u) = 0. indeg(v') = 1.

Σ deg·indeg = deg(v)·2 + deg(v')·1 + deg(u)·0 = 2deg(v) + deg(v').
D_W = deg(v) + deg(v') + deg(u).
Constraints: deg(v)+deg(v') ≤ 100 (cycle edge), deg(u)+deg(v) ≤ 100 (tree edge).
D_W ≤ 100 - deg(v) + deg(v) + deg(u) ... let me just compute.
From constraints: deg(v') ≤ 100 - deg(v), deg(u) ≤ 100 - deg(v).
D_W = deg(v) + deg(v') + deg(u) ≤ deg(v) + (100-deg(v)) + (100-deg(v)) = 200 - deg(v).
For D_W ≤ 150 (= 50·3): need 200 - deg(v) ≤ 150, i.e., deg(v) ≥ 50.

But deg(v) could be < 50! If deg(v) = 10, then D_W ≤ 190 > 150. So the bound D_W ≤ 50s FAILS for this tree component!

Wait, but does that mean we can beat 2500? Let me check: if deg(v) = 10, deg(v') = 90, deg(u) = 90. D_W = 190 for 3 vertices, avg 63.3 > 50. 

But wait, can we actually realize this? We need a graph where v has degree 10, v' has degree 90, u has degree 90, with the triangle-free edges vv' and uv. And the rest of the graph (97 other vertices) also needs to be handled.

Hold on. Let me reconsider. The constraint is deg(u) + deg(f(u)) ≤ 100. If deg(v) = 10, deg(v') = 90, deg(u) = 90: vv' is triangle-free (10+90=100 ✓), uv is triangle-free (90+10=100 ✓). But we also need N(v)∩N(v')=∅ and N(u)∩N(v)=∅.

deg(v) = 10: v is adjacent to v', u, and 8 others. deg(v') = 90: v' adjacent to v and 89 others. N(v)∩N(v') = ∅: the 8 others adjacent to v can't be adjacent to v'. Since v' is adjacent to 89 others (out of 98 non-v vertices), and v is adjacent to u + 8 others = 9 non-v' vertices. N(v) = {v', u, 8 others}, N(v') = {v, 89 others}. N(v)∩N(v') = ({v',u,8others}) ∩ ({v, 89 others}). v' ∉ N(v') (no self-loop), v ∉ N(v). So intersection = {u, 8 others} ∩ {89 others}. For this to be ∅, u and the 8 others must not be in N(v'). So v' is adjacent to 89 vertices, none of which are u or the 8 others. The 89 vertices are from the remaining 100 - 1(v) - 1(v') - 1(u) - 8 = 89 vertices. So v' is adjacent to all 89 of those. OK.

Now N(u)∩N(v) = ∅: N(u) = 90 vertices, N(v) = {v', u, 8 others}. u ∉ N(u). So N(u) ∩ N(v) = N(u) ∩ {v', 8 others} (excluding u since u∉N(u), and v' could be in N(u)). For ∅: v' ∉ N(u) and the 8 others ∉ N(u). 

But v' is adjacent to 89 vertices (all except v, v', u, and the 8 others). Is u adjacent to v'? We need v' ∉ N(u), so u not adjacent to v'. OK. And the 8 others not in N(u). u is adjacent to 90 vertices out of 99. u is not adjacent to v' and not adjacent to the 8 others = 9 vertices not adjacent. But u has degree 90, so u is not adjacent to 9 vertices. ✓ (99 - 90 = 9). 

So u is adjacent to v and 89 others (the same 89 that v' is adjacent to). So u and v' have the same neighborhood (the 89 vertices) plus u is adjacent to v and v' is adjacent to v. 

Now, the 89 vertices: each needs a triangle-free edge. These 89 vertices are adjacent to both u and v'. They form... we need to figure out their adjacencies.

This is getting complex. Let me think about whether this can actually beat 2500.

Total edges so far: deg(v) + deg(v') + deg(u) = 10 + 90 + 90 = 190, but edges counted: vv', uv, v's other 8 edges, v's 89 edges, u's 89 edges. Wait let me recount. 

Edges incident to v: vv', vu, and 8 others = 10 edges.
Edges incident to v': v'v, and 89 to the 89-group = 90 edges (but vv' already counted).
Edges incident to u: uv, and 89 to the 89-group = 90 edges (uv already counted).

Unique edges: vv', vu, 8 (v to 8-group), 89 (v' to 89-group), 89 (u to 89-group). But wait, the 8-group: are they also in the 89-group? No: v is adjacent to v', u, and 8 others. The 8 others are not in the 89-group (since v' is not adjacent to them). So the 8-group is separate from the 89-group. Total vertices: v, v', u, 8-group, 89-group = 1+1+1+8+89 = 100. ✓

Edges so far: 10 (v's edges) + 89 (v' to 89-group, excluding vv') + 89 (u to 89-group, excluding uv) = 10 + 89 + 89 = 188.

Now the 89-group and 8-group need internal edges and triangle-free edges. The 89-group: each vertex is adjacent to u and v'. They need a triangle-free edge. 

The 89-group vertices are adjacent to u and v'. For a vertex x in the 89-group, its triangle-free edge partner y must have N(x)∩N(y)=∅. Since x is adjacent to u and v', y must not be adjacent to u or v'. Who is not adjacent to u or v'? v is not adjacent to u? No, v IS adjacent to u. The 8-group: are they adjacent to u? No (u is not adjacent to the 8-group). Are they adjacent to v'? No (v' is not adjacent to the 8-group). So the 8-group vertices are not adjacent to u or v'. 

So x's triangle-free partner could be in the 8-group. But there are 89 vertices in the 89-group and only 8 in the 8-group. Each 8-group vertex can be a triangle-free partner for multiple 89-group vertices? If x and x' both use the same 8-group vertex w as partner, then edges xw and x'w must both be triangle-free. 

Edge xw: N(x)∩N(w)=∅. N(x) includes u, v', and possibly others. N(w) includes v (since w is in 8-group, adjacent to v) and possibly others. For N(x)∩N(w)=∅: u ∉ N(w) (✓, w not adjacent to u), v' ∉ N(w) (✓), and any other neighbor of x not in N(w), and v ∉ N(x) (is x adjacent to v? x is in 89-group, v is adjacent to only v', u, 8-group. So v not adjacent to x. ✓). Also w's neighbors: w is adjacent to v. Is v ∈ N(x)? No. Other neighbors of w? If w has other neighbors, they must not be in N(x).

This is getting very complicated. Let me step back and think about the problem from a higher level.

Let me reconsider: is the answer 2500 or something else?

Let me think about it from the perspective of the complement graph or known results.

Actually, let me reconsider the tree component analysis. The issue is that a tree component can have average degree > 50. But the question is whether the ENTIRE graph can have average degree > 50.

In the example above, the component {v, v', u} has sum of degrees 190 for 3 vertices. But the 89-group and 8-group vertices also need to be accounted for, and they might have lower average degree.

Let me think about it more carefully with a cleaner model.

Actually, let me reconsider. The key insight might be different. Let me think about the problem as follows:

For each vertex u, choose witness f(u). The edge uf(u) is triangle-free, so deg(u) + deg(f(u)) ≤ n = 100.

Now consider the sum S = Σ_u (deg(u) + deg(f(u))) ≤ 100n = 10000.
S = Σ_u deg(u) + Σ_u deg(f(u)) = 2|E| + Σ_v deg(v)·indeg(v).

So 2|E| + Σ_v deg(v)·indeg(v) ≤ 10000.

Now, Σ_v deg(v)·indeg(v) ≥ 0, so 2|E| ≤ 10000, |E| ≤ 5000. That's trivial (complete graph has 4950).

We need a better bound. The issue is that Σ_v deg(v)·indeg(v) could be small if high-degree vertices have low indeg.

Hmm, but there's a constraint: every vertex has outdeg 1 and the function f maps to neighbors. Let me think about indeg more carefully.

Actually, let me think about a cleaner upper bound argument.

Alternative: Let's not use the functional graph. Instead, consider the set of triangle-free edges T (an edge cover). 

For each triangle-free edge uv, deg(u) + deg(v) ≤ 100.

We want to maximize |E| = (1/2)Σ deg(v).

Consider a minimum edge cover C ⊆ T (minimum number of triangle-free edges covering all vertices). |C| = n - ν_T where ν_T is the maximum matching in T. Since T has a perfect matching iff... well, |C| ≥ n/2 = 50 (since each edge covers 2 vertices). And |C| = 50 iff T has a perfect matching.

For each edge uv ∈ C, deg(u)+deg(v) ≤ 100. Sum over C: Σ_{uv∈C}(deg(u)+deg(v)) ≤ 100|C|.

Each vertex is covered by C. In a minimum edge cover, each vertex is covered exactly once (if a vertex were covered twice, we could remove an edge). Wait, no: in a minimum edge cover, it's not necessarily that each vertex is covered once. Actually, a minimum edge cover can be decomposed as a maximum matching plus additional edges for unmatched vertices, and each unmatched vertex gets one edge to a matched vertex. So matched vertices can be covered 1 or 2 times, unmatched vertices covered once.

Hmm, actually in a minimum edge cover, each vertex is covered at least once, and the cover has n - ν edges. The structure: take a maximum matching M (ν edges, 2ν vertices), then for each of the n - 2ν unmatched vertices, add one edge connecting it to a matched vertex. Total: ν + (n - 2ν) = n - ν edges.

In this structure, each unmatched vertex is covered once, and each matched vertex is covered once (by matching edge) plus possibly more (by edges to unmatched vertices). 

Sum over edges in C of (deg(u)+deg(v)): each matched vertex v appears in its matching edge (contributing deg(v)) and in k_v additional edges (where k_v is the number of unmatched vertices assigned to v), contributing k_v · deg(v). Each unmatched vertex u appears once, contributing deg(u).

So Σ_{uv∈C}(deg(u)+deg(v)) = Σ_{matched v} (1 + k_v) deg(v) + Σ_{unmatched u} deg(u).

And this is ≤ 100|C| = 100(n - ν).

Also, 2|E| = Σ_{matched v} deg(v) + Σ_{unmatched u} deg(u).

So Σ_{matched v} (1+k_v) deg(v) + Σ_{unmatched u} deg(u) ≤ 100(n-ν).
2|E| + Σ_{matched v} k_v deg(v) ≤ 100(n-ν).
2|E| ≤ 100(n-ν) - Σ k_v deg(v).

Since Σ k_v = n - 2ν (total unmatched), and k_v ≥ 0.

To maximize 2|E|, we want Σ k_v deg(v) small and ν large (so n-ν small). 

If ν = 50 (perfect matching), n - ν = 50, k_v = 0 for all, 2|E| ≤ 5000, |E| ≤ 2500. 

If ν < 50, then n - ν > 50, but Σ k_v deg(v) > 0 (since there are unmatched vertices). The question is whether the tradeoff can favor |E| > 2500.

2|E| ≤ 100(n - ν) - Σ k_v deg(v).

With ν = 50 - t (t unmatched-pair count, so n - 2ν = 2t unmatched vertices), n - ν = 50 + t.
Σ k_v = 2t.
2|E| ≤ 100(50 + t) - Σ k_v deg(v) = 5000 + 100t - Σ k_v deg(v).

For |E| > 2500, need 100t > Σ k_v deg(v), i.e., Σ k_v deg(v) < 100t, i.e., average deg of the vertices v (weighted by k_v) < 100. 

Hmm, but deg(v) could be less than 100. In fact, the matched vertices v that have k_v > 0 are adjacent to unmatched vertices via triangle-free edges, so deg(v) + deg(unmatched) ≤ 100, meaning deg(v) ≤ 100 - deg(unmatched) < 100 (if unmatched has deg > 0, which it does since it has at least the triangle-free edge).

But this doesn't immediately give us the bound. Let me think more.

Let me denote the unmatched vertices as u_1, ..., u_{2t} and they're assigned to matched vertices. Each u_j is assigned to some matched vertex v_{a(j)} via a triangle-free edge, with deg(u_j) + deg(v_{a(j)}) ≤ 100.

Σ k_v deg(v) = Σ_j deg(v_{a(j)}).

2|E| ≤ 5000 + 100t - Σ_j deg(v_{a(j)}).

Also, 2|E| = Σ_{matched} deg(v) + Σ_j deg(u_j) + Σ_{other matched not in cover...} wait, all matched vertices are in the matching. Let me re-denote.

Let me split: matched vertices (2ν = 100 - 2t of them) and unmatched (2t of them).
2|E| = Σ_{matched v} deg(v) + Σ_{unmatched u} deg(u).

From the matching edges: for each matching edge vv', deg(v) + deg(v') ≤ 100. Sum: Σ_{matched v} deg(v) ≤ 100ν = 100(50-t) = 5000 - 100t.

From the cover edges for unmatched: deg(u_j) + deg(v_{a(j)}) ≤ 100. Sum: Σ_j deg(u_j) + Σ_j deg(v_{a(j)}) ≤ 100 · 2t = 200t.

So Σ_j deg(u_j) ≤ 200t - Σ_j deg(v_{a(j)}).

2|E| = Σ_{matched} deg(v) + Σ_j deg(u_j) ≤ (5000 - 100t) + (200t - Σ_j deg(v_{a(j)})) = 5000 + 100t - Σ_j deg(v_{a(j)}).

Same as before. Now, Σ_j deg(v_{a(j)}) ≥ ? Each v_{a(j)} is a matched vertex with deg(v_{a(j)}) ≥ 1. But we need a better lower bound.

Note: deg(v_{a(j)}) ≥ deg(u_j) is not necessarily true. But we know deg(v_{a(j)}) ≥ 1 (it has at least the matching edge and the cover edge).

Hmm, we need Σ_j deg(v_{a(j)}) ≥ 100t to get 2|E| ≤ 5000. Is this true?

Σ_j deg(v_{a(j)}) = Σ_v k_v deg(v) where Σ k_v = 2t. We need this ≥ 100t = 50 · 2t. So we need the k_v-weighted average of deg(v) ≥ 50.

Is this guaranteed? Not obviously. A matched vertex v with high k_v could have low degree.

But wait: v is a matched vertex, so it's in a matching edge vv' with deg(v) + deg(v') ≤ 100. Also v has k_v unmatched vertices assigned to it, each via a triangle-free edge, so deg(v) + deg(u_j) ≤ 100 for each. 

Hmm, deg(v) could be small. E.g., deg(v) = 1 (just the matching edge), and v' has deg 99. Then v could be assigned many unmatched vertices? deg(v) + deg(u_j) ≤ 100, so deg(u_j) ≤ 99. But v has degree 1, meaning v is only adjacent to v'. But the triangle-free edge from u_j to v requires u_j adjacent to v. So v must be adjacent to u_j, meaning deg(v) ≥ 1 + k_v. So deg(v) ≥ 1 + k_v.

So if v has k_v unmatched vertices assigned, deg(v) ≥ 1 + k_v (matching edge + k_v cover edges). And deg(v) + deg(v') ≤ 100, deg(v) + deg(u_j) ≤ 100.

So Σ_v k_v deg(v) ≥ Σ_v k_v (1 + k_v) = Σ k_v + Σ k_v^2 = 2t + Σ k_v^2.

By Cauchy-Schwarz, Σ k_v^2 ≥ (Σ k_v)^2 / (number of v with k_v > 0) ≥ (2t)^2 / (2t) = 2t (if all k_v = 1). So Σ k_v deg(v) ≥ 2t + 2t = 4t.

We need Σ k_v deg(v) ≥ 100t. But we only have ≥ 4t. Not enough!

So this approach doesn't prove |E| ≤ 2500. Maybe the answer is NOT 2500?

Let me reconsider. Maybe we can beat 2500. Let me try to construct a graph with more than 2500 edges.

Idea: Use a star-like structure. Take one vertex v connected to many low-degree vertices, and a large clique elsewhere.

Let me try a concrete construction. 

Construction: 
- Take a clique K_{99} on vertices 1,...,99.
- Vertex 0 is connected to vertex 1 only.
- Edge 0-1: N(0) = {1}, N(1) = {0, 2, 3, ..., 99}. N(0)∩N(1) = {1}∩N(1). 1 ∉ N(1), so intersection = ∅. Triangle-free! ✓
- Vertex 0 has triangle-free edge 0-1. ✓
- Vertex 1 has triangle-free edge 1-0. ✓
- Vertices 2,...,99 (98 vertices): each is in K_{99}, every edge in a triangle. They need triangle-free edges, but all their edges are in K_{99} (triangles). No triangle-free edge. ✗

So this fails for 98 vertices. We need to give each of them a triangle-free edge.

Modified construction: 
- Take a clique K_k on k vertices (the "core").
- Have 100 - k "pendant" vertices, each connected to exactly one core vertex via a triangle-free edge.
- Each core vertex can have at most one pendant (because if core vertex c has two pendants p, q, then edges cp and cq: cp is triangle-free requires N(c)∩N(p)=∅. N(p)={c}, so N(c)∩{c}=∅ ✓. Similarly cq. But does c still have a triangle-free edge? c's triangle-free edge could be cp (N(c)∩N(p)=∅ ✓). But wait, we need to check: is cp still triangle-free if c is also adjacent to q? N(p) = {c}, N(c) includes q. N(c)∩N(p) = N(c)∩{c} = ∅. Still triangle-free. ✓. So c can have multiple pendants.

But the pendants: p has triangle-free edge pc ✓. q has triangle-free edge qc ✓. 

Now, the core vertices: each needs a triangle-free edge. If core vertex c has a pendant p, then cp is triangle-free ✓. But if core vertex c has NO pendant, then c needs a triangle-free edge within the core. In a clique K_k (k ≥ 3), no edge is triangle-free. So every core vertex needs a pendant.

So we need at least k pendants, one for each core vertex. Total vertices: k + (number of pendants) ≥ k + k = 2k ≤ 100, so k ≤ 50.

With k = 50: 50 core vertices (K_50), 50 pendants (each connected to one core vertex). Edges: C(50,2) + 50 = 1225 + 50 = 1275. Worse than 2500.

But wait, can pendants have edges among themselves? If pendant p (connected to core vertex c_p) and pendant q (connected to core vertex c_q) are adjacent: does this break triangle-free edges? 

Edge c_p p: N(c_p) ∩ N(p) = ∅. N(p) now includes c_p and q. N(c_p) includes all core vertices and pendants assigned to c_p. For N(c_p)∩N(p) = ∅: q ∉ N(c_p) (i.e., c_p not adjacent to q, which is true if q is a pendant of c_q ≠ c_p and c_p is not adjacent to q). Also c_p ∉ N(p)? No, c_p ∈ N(p) but c_p ∉ N(c_p). And any other neighbor of p must not be in N(c_p).

If we add edges among pendants, we need to be careful. Let me think about making pendants form a clique.

If all 50 pendants form a clique: pendant p (assigned to c_p) has neighbors: c_p and all other 49 pendants. N(p) = {c_p} ∪ {other pendants}. N(c_p) = {other 49 core vertices} ∪ {p} (and possibly other pendants assigned to c_p). 

N(c_p) ∩ N(p): N(c_p) contains other core vertices and p. N(p) contains c_p and other pendants. Intersection: do any core vertices (other than c_p) appear in N(p)? N(p) = {c_p, other pendants}. No core vertices except c_p. And c_p ∉ N(c_p). And p ∈ N(c_p) but p ∉ N(p). So intersection = ∅? Wait, N(c_p) = {core vertices except c_p} ∪ {p} ∪ {other pendants assigned to c_p}. N(p) = {c_p} ∪ {other 49 pendants}. 

Intersection: {core except c_p} ∪ {p} ∪ {assigned pendants} ∩ {c_p} ∪ {49 pendants}. 
- {core except c_p} ∩ {c_p} = ∅, {core except c_p} ∩ {49 pendants} = ∅ (pendants aren't core). 
- {p} ∩ {c_p} = ∅, {p} ∩ {49 pendants} = ∅ (p not in other pendants). 
- {assigned pendants} ∩ {c_p} = ∅, {assigned pendants} ∩ {49 pendants}: if c_p has other pendants assigned, they'd be in the 49 pendants. So intersection includes those!

So if c_p has only one pendant (p), then {assigned pendants} = {p}, and intersection with {49 pendants} = ∅ (since p ∉ {49 other pendants}). So N(c_p) ∩ N(p) = ∅. ✓

So with each core vertex having exactly one pendant, and pendants forming a clique, and core forming a clique:
- Core: K_50, edges = C(50,2) = 1225.
- Pendants: K_50, edges = C(50,2) = 1225.
- Matching: 50 edges.
- Total = 2500. Same as before!

And we already showed cross edges (beyond matching) break triangle-free property. So 2500 again.

But can we do better with a non-clique structure? Let me think about the earlier tree component idea more carefully.

Let me try to construct a graph with > 2500 edges.

Idea: Have some vertices with very high degree (close to 99) paired with very low degree vertices, and a large dense subgraph.

Let me try: 
- 2 vertices a, b with edge ab triangle-free. deg(a) = 99, deg(b) = 1. 
  - a adjacent to all 99 others. b adjacent to only a.
  - N(a) ∩ N(b) = N(a) ∩ {a} = ∅ ✓ (since a ∉ N(a)).
  - a's triangle-free edge: ab ✓. b's triangle-free edge: ba ✓.
- But the other 98 vertices: each is adjacent to a. For vertex w (w ≠ a, b), w needs a triangle-free edge. w is adjacent to a. If w's triangle-free edge is wx, then N(w)∩N(x) = ∅. Since a ∈ N(w), we need a ∉ N(x), so x is not adjacent to a. But a is adjacent to everyone. So x must be... a is adjacent to all 99 others, so everyone is adjacent to a. Thus a ∈ N(x) for all x ≠ a. So no x can be a triangle-free partner for w (since a ∈ N(w) ∩ N(x)). Unless x = a, but then edge wa: N(w)∩N(a) must be ∅, but N(a) is huge. No.

So deg(a) = 99 doesn't work because it "blocks" all other vertices from having triangle-free edges. 

The issue: if a is adjacent to both w and x, then a ∈ N(w) ∩ N(x), so wx can't be triangle-free. So if a vertex a is adjacent to a set S of vertices, no two vertices in S can have a triangle-free edge between them (since a is a common neighbor). Moreover, for w ∈ S, w's triangle-free partner x must satisfy a ∉ N(x), i.e., x ∉ S and x ≠ a. So x must be outside S ∪ {a}.

So if a has high degree, the neighbors of a must find triangle-free partners outside N(a) ∪ {a}. The non-neighbors of a (excluding a itself) are 100 - 1 - deg(a) = 99 - deg(a) vertices.

Each neighbor of a needs a triangle-free partner among the 99 - deg(a) non-neighbors of a. Each non-neighbor x can serve as triangle-free partner for multiple neighbors of a (as long as the edges are triangle-free). But there are constraints.

This is getting complicated. Let me try to think about it computationally for small cases to guess the pattern.

Actually, let me think about the problem differently. Let me consider the general problem: n vertices, each vertex has a triangle-free edge, maximize edges.

For n = 2: only edge is the edge itself, triangle-free. 1 edge. 
For n = 4: two K_2's + ... or K_2 + K_2 with cross edges? Matching construction: two pairs, K_2 + K_2 + 2 cross = 4 edges. Or: K_4 has 6 edges but no triangle-free edge (every edge in triangle). Remove edges to get triangle-free edges. 

For n = 4, matching construction: a1a2, b1b2 (cliques of size 2 = single edges), matching a1b1, a2b2. Edges: 1 + 1 + 2 = 4. But can we do better? K_4 minus one edge = 5 edges. Does every vertex have a triangle-free edge? K_4 - {cd}: vertices a,b,c,d. Edges: ab, ac, ad, bc, bd. (missing cd). 
- a: neighbors b,c,d. Edge ab: N(a)={b,c,d}, N(b)={a,c,d}. Intersection {c,d} ≠ ∅. Edge ac: N(a)∩N(c) = {b,c,d}∩{a,b,d} = {b,d} ≠ ∅. Edge ad: N(a)∩N(d)={b,c,d}∩{a,b,c}={b,c}≠∅. No triangle-free edge for a. ✗.

K_4 minus two edges: say remove cd and one more. K_4 - {cd, bd}: edges ab, ac, ad, bc. 
- a: N(a)={b,c,d}. Edge ab: N(b)={a,c}. N(a)∩N(b)={c}≠∅. Edge ad: N(d)={a}. N(a)∩N(d)={b,c,d}∩{a}=∅ ✓. Triangle-free! 
- b: N(b)={a,c}. Edge bc: N(c)={a,b}. N(b)∩N(c)={a}≠∅. Edge ab: already checked, {c}≠∅. No triangle-free edge for b. ✗.

Hmm. K_4 - {cd, bc}: edges ab, ac, ad, bd. Wait that's the same as before by symmetry.

Let me try C_4 (cycle): edges ab, bc, cd, da. 4 edges. Each edge: ab, N(a)={b,d}, N(b)={a,c}. Intersection ∅ ✓. So every edge is triangle-free. 4 edges. Same as matching construction.

Can we get 5 edges on 4 vertices with the property? K_4 has 6, we need to remove at least 1. K_4 - 1 edge = 5, shown above doesn't work. So max for n=4 is 4 = n²/4. ✓ matches 2500 = 100²/4.

For n = 6: matching construction gives 2 K_3's + matching = 2·3 + 3 = 9 = 36/4. Can we beat 9?

K_6 has 15 edges. We need each vertex to have a triangle-free edge. 

Let me try: K_6 minus some edges. Actually let me think about whether n²/4 is always the answer.

Hmm, let me think about n = 6 more carefully. 

Construction: K_3 on {a1,a2,a3}, K_3 on {b1,b2,b3}, matching a1b1, a2b2, a3b3. Total: 3 + 3 + 3 = 9. Each matching edge is triangle-free (verified as before). ✓

Can we do 10? Let me try adding one more edge to the 9-edge construction, say a1b2. Then a1b1: N(a1) = {a2,a3,b1,b2}, N(b1) = {b2,b3,a1}. Intersection: {a2,a3,b1,b2}∩{b2,b3,a1} = {b2} ≠ ∅. So a1b1 no longer triangle-free. a1 needs another triangle-free edge. a1's edges: a1a2, a1a3, a1b1, a1b2. 
- a1a2: N(a1)∩N(a2). N(a2)={a1,a3,b2}. N(a1)={a2,a3,b1,b2}. Intersection: {a3,b2} ≠ ∅. 
- a1a3: N(a3)={a1,a2,b3}. Intersection with N(a1)={a2,a3,b1,b2}: {a2} ≠ ∅.
- a1b2: N(b2)={b1,b3,a2,a1}. Intersection with N(a1)={a2,a3,b1,b2}: {a2,b1} ≠ ∅.
No triangle-free edge for a1. ✗.

So adding a1b2 breaks it. What about a different 10-edge graph?

Let me try: K_6 minus 5 edges. 15 - 5 = 10. We need to remove edges so every vertex has a triangle-free edge.

Actually, let me think about it differently. The complement of our graph has 15 - |E| edges. For |E| = 10, complement has 5 edges.

A triangle-free edge uv in G means N_G(u) ∩ N_G(v) = ∅, i.e., no w is adjacent to both u and v in G. In complement terms: every w ≠ u,v is non-adjacent to u or non-adjacent to v in G, i.e., w is adjacent to u or v in complement. So in complement, every w ≠ u,v is adjacent to u or v. Plus u and v are non-adjacent in complement (since uv is an edge in G). So in complement, {u,v} is a non-edge, and every other vertex is adjacent to at least one of u,v. This means {u,v} is a dominating set in the complement (dominating every other vertex), and uv is a non-edge.

Hmm, this is an interesting reformulation but might not directly help.

Let me just try to see if 10 is achievable for n = 6 by brute force thinking.

Actually, let me try a different construction for n = 6. Instead of two equal cliques, try unequal.

3 vertices in group A (clique K_3), 3 in group B (clique K_3), but with a different cross structure. We showed cross edges must form a matching (for the two-clique construction). So max is 9.

What about non-clique-based? Let me try: take K_6 and remove a perfect matching (3 edges). 15 - 3 = 12 edges. The removed matching: say remove a1b1, a2b2, a3b3. Remaining: K_6 minus matching = complete tripartite? No, it's K_6 minus 3 disjoint edges.

In K_6 - M (M = perfect matching), does every vertex have a triangle-free edge? Take vertex a1. Its neighbors: a2, a3, b2, b3 (not b1, since a1b1 removed). Edge a1a2: N(a1) = {a2,a3,b2,b3}, N(a2) = {a1,a3,b1,b3}. Intersection: {a3, b3} ≠ ∅. Edge a1b2: N(b2) = {a1,a3,b1,b3}. Intersection with N(a1) = {a2,a3,b2,b3}: {a3,b3} ≠ ∅. Similarly all edges have common neighbors. No triangle-free edge. ✗.

So K_6 - M doesn't work. 

Let me try K_6 minus a star K_{1,3} (remove 3 edges incident to one vertex). Remove a1a2, a1a3, a1b1. 12 edges. Vertex a1: neighbors {b2, b3}. Edge a1b2: N(a1)={b2,b3}, N(b2)={a1,a2,a3,b1,b3}. Intersection: {b3} ≠ ∅. Edge a1b3: N(b3)={a1,a2,a3,b1,b2}. Intersection with N(a1)={b2,b3}: {b2} ≠ ∅. No triangle-free edge for a1. ✗.

Hmm. Let me try removing edges to create triangle-free edges. For an edge to be triangle-free, we need to remove all common neighbors. Edge ab is triangle-free if we remove all edges aw and bw for all w (i.e., no w is adjacent to both). 

For n = 6, to make edge ab triangle-free, for each of the other 4 vertices w, at least one of aw, bw must be removed. That's at least 4 removals (but one removal can cover one w). Actually for each w, remove aw or bw. 4 vertices, 4 removals minimum (each removal covers one w). But if we remove aw, that also helps make other edges triangle-free.

This is like a covering problem. Let me think about it as: we want to select a set of triangle-free edges (forming an edge cover) and remove edges to make them triangle-free, while keeping as many edges as possible.

For the matching construction on n = 6: 3 triangle-free edges (matching), each requiring 4 removals from K_6, but removals can overlap. Total edges = 15 - (removals). Matching construction gives 9, so 6 removals. 

Can we do fewer removals? With 5 removals, 10 edges. Let's see if possible.

3 matching edges a1b1, a2b2, a3b3. For a1b1 triangle-free: for w ∈ {a2,a3,b2,b3}, remove a1w or b1w. For a2b2: w ∈ {a1,a3,b1,b3}, remove a2w or b2w. For a3b3: w ∈ {a1,a2,b1,b2}, remove a3w or b3w.

We need to choose removals to satisfy all three, minimizing total removals. Each removal is one edge.

For a1b1: need to cover {a2,a3,b2,b3}. 
For a2b2: need to cover {a1,a3,b1,b3}.
For a3b3: need to cover {a1,a2,b1,b2}.

A single removal like a1a2 covers: a2 for edge a1b1 (since a1a2 removed, a2 not adjacent to a1, so a2 not common neighbor of a1,b1 ✓), and a1 for edge a2b2 (since a1a2 removed, a1 not adjacent to a2 ✓). So a1a2 removal covers a2 in constraint 1 and a1 in constraint 2. 

Similarly, a removal of edge xy where x is in one pair and y in another covers two constraints.

Let me think of it as a problem on K_{3,3} (the cross edges between pairs). The cross edges are a_i a_j, a_i b_j, b_i a_j, b_i b_j for i ≠ j. There are 3·3·... wait, 3 pairs, cross edges between different pairs: for each pair of pairs (i,j), 4 edges. C(3,2) = 3 pair-pairs, 4 edges each = 12 cross edges. Plus 3 matching edges + within-pair edges (0, since pairs are size 2, no within-pair edges except matching). Wait, in the matching construction for n=6, the "cliques" are K_3 on a's and K_3 on b's. So within-a edges: a1a2, a1a3, a2a3 (3 edges). Within-b: b1b2, b1b3, b2b3 (3 edges). Cross: matching a1b1, a2b2, a3b3 (3 edges). Total: 3+3+3 = 9.

To make a1b1 triangle-free: no common neighbor. a1's neighbors (in full K_6): a2, a3, b1, b2, b3. b1's neighbors: a1, a2, a3, b2, b3. Common: a2, a3, b2, b3. To make triangle-free, remove a1's or b1's edge to each of a2, a3, b2, b3. 

In the matching construction, we remove ALL cross edges except matching. So we remove a1a2? No wait, a1a2 is a within-a edge, kept. We remove a1b2, a1b3, b1a2, b1a3 (cross edges). That's 4 removals for a1b1. But a1a2 and a1a3 are kept (within-a clique), and b1a2 = a2b1 is a cross edge, removed. So common neighbors of a1 and b1: a2 (a1-a2 kept, b1-a2 removed → a2 not common), a3 (similar), b2 (a1-b2 removed), b3 (a1-b3 removed). So no common neighbors. ✓. 4 removals for this edge.

But these removals also help other edges. a1b2 removed helps a2b2 (removes a1 as potential common neighbor of a2,b2). 

Total removals in matching construction: all 12 cross edges minus 3 matching = 9 removals. 15 - 9 = 6... wait that gives 6, not 9. 

Oh wait, I'm confusing myself. K_6 has 15 edges. Matching construction has 9 edges. So 6 removals. The 6 removals are the 9 non-matching cross edges... no. Cross edges: 12 (4 per pair-pair × 3 pair-pairs). Matching: 3. Non-matching cross: 9. But we only remove 6 edges (15 - 9 = 6). 

Hmm, I think I miscounted. In the matching construction, the edges are: within-a (3) + within-b (3) + matching (3) = 9. The removed edges are: cross non-matching = 15 - 9 = 6. But I said there are 9 non-matching cross edges. 12 cross total - 3 matching = 9 non-matching cross. But 15 - 9 = 6. Contradiction. 

Oh I see the issue: 15 total edges = 3 (within-a) + 3 (within-b) + 3 (matching) + 6 (non-matching cross). Wait: within-a = C(3,2) = 3, within-b = 3, cross = 3×3 = 9 (each a to each b), matching = 3 of those 9, non-matching cross = 6. Total = 3 + 3 + 9 = 15. ✓. Kept: 3 + 3 + 3 = 9. Removed: 6 (non-matching cross). ✓.

OK so 6 removals. Can we do 5 removals (10 edges)?

We need 3 triangle-free edges covering all 6 vertices (edge cover, but actually we need every vertex to have a triangle-free edge, so we need an edge cover of triangle-free edges). With 3 matching edges, we need each to be triangle-free. 

For a1b1 triangle-free: remove edges so no common neighbor. Common neighbors of a1,b1 in K_6: {a2,a3,b2,b3}. For each, remove one of the two edges. 4 vertices, but some removals can be shared with other constraints.

For a2b2: common neighbors {a1,a3,b1,b3}. 
For a3b3: common neighbors {a1,a2,b1,b2}.

Let me see if 5 removals suffice. We need to "hit" all common neighbor relationships.

Consider removing: a1b2, a1b3, a2b1, a2b3, a3b1, a3b2. That's 6 removals (all non-matching cross edges). Can we keep one more?

Say we keep a1b2 (don't remove it). Then for a1b1 triangle-free: b2 is a common neighbor if b1-b2 is an edge (yes, within-b clique) and a1-b2 is an edge (yes, we kept it). So b2 is a common neighbor. To fix, remove b1b2 (within-b edge). But removing b1b2 might break b1 or b2's triangle-free edge.

If we remove b1b2 and keep a1b2: 
- a1b1: common neighbors? a2 (a1-a2 yes, b1-a2 = a2b1, removed ✓ not common), a3 (a1-a3 yes, b1-a3 = a3b1, removed ✓), b2 (a1-b2 yes, b1-b2 removed ✓), b3 (a1-b3 removed ✓). No common neighbors. ✓
- a2b2: common neighbors? a1 (a2-a1 yes, b2-a1 = a1b2, kept! so a1 is common if a2-a1 and b2-a1 both edges. a2-a1 yes, b2-a1 = a1b2 yes. Common! ✗.

So a1 is a common neighbor of a2 and b2. To fix, remove a1a2 or a1b2. But we wanted to keep a1b2. Remove a1a2? Then a1's neighbors change. 

This is getting complicated. Let me just try to check computationally whether 10 is possible for n=6.

Actually, let me think about it more cleverly. The question is whether n²/4 is the answer.

Let me consider the problem from the perspective of Turán-type results. 

Actually, I recall a similar problem: "every edge is in at most one triangle" or "every vertex has a pendant edge" type conditions. But this is different.

Let me think about the upper bound more carefully.

Key lemma: For each vertex u, let v be its witness (triangle-free edge uv). Then deg(u) + deg(v) ≤ n.

Now, consider the witness function f. Build the functional graph. 

I want to prove Σ deg(u) ≤ n²/2, i.e., |E| ≤ n²/4.

Let me try a different approach. Consider the graph H on V where we connect u to f(u) for each u (the witness edges). H is a spanning subgraph (edge cover) with each vertex having outdegree 1 (directed) or degree ≥ 1 (undirected).

For each edge uv in H (meaning f(u)=v or f(v)=u), we have deg_G(u) + deg_G(v) ≤ n.

Now, H is a graph (ignoring direction) where every vertex has degree ≥ 1. H has at most n edges (since outdegree 1 gives n directed edges, at most n undirected edges).

Actually, H has exactly n directed edges, so at most n undirected edges (could be fewer if 2-cycles). 

We want to bound Σ_{v} deg_G(v) = 2|E|.

Consider the sum Σ_{u} (deg_G(u) + deg_G(f(u))) ≤ n² (summing deg(u)+deg(f(u)) ≤ n over all n vertices).

Σ_u deg_G(u) + Σ_u deg_G(f(u)) ≤ n².
2|E| + Σ_u deg_G(f(u)) ≤ n².

Now Σ_u deg_G(f(u)) = Σ_v deg_G(v) · indeg(v) where indeg is indegree in the functional graph.

So 2|E| + Σ_v deg_G(v) · indeg(v) ≤ n².

We need to show 2|E| ≤ n²/2, i.e., Σ_v deg_G(v) · indeg(v) ≥ n²/2 - ... hmm, we need 2|E| ≤ n²/2, so Σ_v deg(v)·indeg(v) ≥ n² - n²/2 = n²/2. 

Is Σ_v deg(v)·indeg(v) ≥ n²/2? We have Σ indeg(v) = n. By Cauchy-Schwarz or rearrangement... 

Σ_v deg(v)·indeg(v) ≥ (Σ_v deg(v))(Σ_v indeg(v)) / n = (2|E| · n) / n = 2|E| if deg and indeg are "aligned". But that's not generally true.

Actually, by the rearrangement inequality, Σ deg(v)·indeg(v) is minimized when one is sorted ascending and the other descending. We can't bound it below without more info.

Hmm. Let me try yet another approach.

Let me think about it as an optimization problem. We want to maximize Σ deg(v) subject to:
- There exists f: V → V such that for each u, f(u) ∈ N(u), N(u) ∩ N(f(u)) = ∅.
- Equivalently, deg(u) + deg(f(u)) ≤ n for each u (necessary condition; the disjoint neighborhood condition is stronger but let's use this necessary condition for an upper bound).

So we want to maximize Σ deg(v) subject to: there exists a function f where each u maps to a neighbor, and deg(u) + deg(f(u)) ≤ n.

Wait, but we also need f(u) to be a neighbor, which means the degree sequence must be realizable with the graph structure. Let me just use the necessary condition deg(u) + deg(f(u)) ≤ n and see what upper bound it gives.

This is a pure optimization: given n values deg(1),...,deg(n) and a function f with deg(i) + deg(f(i)) ≤ n for all i, maximize Σ deg(i).

The function f defines a functional graph. To maximize Σ deg, we want to choose f and deg values optimally.

For a 2-cycle (i ↔ j): deg(i) + deg(j) ≤ n. Contribution: ≤ n for 2 vertices.
For a fixed point: deg(i) + deg(i) ≤ n, so deg(i) ≤ n/2. Contribution: ≤ n/2 for 1 vertex. (But fixed point means f(i) = i, i.e., i is its own neighbor, which requires a self-loop. Not allowed in simple graph! So no fixed points.)

For a k-cycle (k ≥ 3): deg(v_i) + deg(v_{i+1}) ≤ n. Sum: 2Σ deg ≤ kn, Σ deg ≤ kn/2. Contribution: ≤ kn/2 for k vertices, avg n/2.

For a tree: root v (in a cycle) with child u: deg(u) + deg(v) ≤ n. If deg(v) = d, deg(u) ≤ n - d. Grandchild w: deg(w) + deg(u) ≤ n, deg(w) ≤ n - deg(u) ≤ d. Etc.

For a path v → u → w (f(v)=u, f(u)=w, and w is in a cycle or has its own f): deg(v)+deg(u) ≤ n, deg(u)+deg(w) ≤ n. So deg(v) ≤ n - deg(u), deg(w) ≤ n - deg(u). Sum deg(v)+deg(u)+deg(w) ≤ (n - deg(u)) + deg(u) + (n - deg(u)) = 2n - deg(u). Maximized when deg(u) is minimized. deg(u) ≥ 1 (at least one edge, to v and w). If deg(u) = 1... but u is adjacent to both v and w (since f(v)=u means v adjacent to u, and f(u)=w means u adjacent to w). So deg(u) ≥ 2. Sum ≤ 2n - 2. For n = 100, that's 198 for 3 vertices, avg 66 > 50.

But wait, can deg(u) = 2 with u adjacent to v and w only? Then deg(v) ≤ 98, deg(w) ≤ 98. Sum = 98 + 2 + 98 = 198. 

But we also need the actual graph to realize these degrees with the triangle-free condition (not just the degree sum condition). The degree sum is necessary but not sufficient. Let me check if this is actually realizable.

Let me try to construct: n = 100. 
- u: adjacent to v and w only. deg(u) = 2.
- v: adjacent to u and 97 others (not w). deg(v) = 98.
- w: adjacent to u and 97 others (not v). deg(w) = 98.
- f(v) = u, f(u) = w. 
  - Edge vu: N(v) ∩ N(u) = ∅. N(u) = {v, w}. N(v) = {u, 97 others}. Intersection: {v,w} ∩ {u, 97 others}. v ∉ N(v), w: is w ∈ N(v)? v not adjacent to w, so w ∉ N(v). So intersection = ∅ ✓ (if the 97 others don't include w, which they don't since v not adjacent to w).
  - Edge uw: N(u) ∩ N(w) = ∅. N(u) = {v, w}. N(w) = {u, 97 others}. Intersection: {v,w} ∩ {u, 97 others}. w ∉ N(w), v: is v ∈ N(w)? w not adjacent to v, so v ∉ N(w). Intersection = ∅ ✓.
- v's witness is u (triangle-free ✓). u's witness is w (triangle-free ✓). w needs a witness too!
- w has deg 98, adjacent to u and 97 others. w's triangle-free edge: needs partner x with deg(x) + deg(w) ≤ 100, so deg(x) ≤ 2. And N(w) ∩ N(x) = ∅. x must be adjacent to w (x ∈ N(w)). x has deg ≤ 2, so x is adjacent to w and at most 1 other. N(x) ⊆ {w, one other}. N(w) = {u, 97 others}. N(w) ∩ N(x): if x's other neighbor is y, then y ∈ N(x) and we need y ∉ N(w). But N(w) has 98 vertices. y ∉ N(w) means y is one of the 2 vertices not adjacent to w: those are v and... w itself (but w ∉ N(w)). So y = v. So x is adjacent to w and v. deg(x) = 2. N(x) = {w, v}. N(w) ∩ N(x) = {u, 97 others} ∩ {w, v} = ∅ (since v ∉ N(w), w ∉ N(w)). ✓!

So x is adjacent to w and v, deg(x) = 2. f(w) = x. Edge wx is triangle-free. ✓.

Now x needs a witness. x is adjacent to w and v. deg(x) = 2. x's triangle-free edge: partner y with deg(y) ≤ 98 and N(x) ∩ N(y) = ∅. N(x) = {w, v}. y must be adjacent to x, so y ∈ {w, v}. 
- y = w: deg(w) = 98, deg(x) + deg(w) = 100 ≤ 100 ✓. N(x) ∩ N(w) = ∅ ✓ (shown above). So f(x) = w. But then x → w → x is a 2-cycle. ✓.

So we have a 2-cycle w ↔ x, and v → u → w. Wait, let me re-examine. f(v) = u, f(u) = w, f(w) = x, f(x) = w. So w → x → w is a 2-cycle, and v → u → w is a tree feeding into the cycle.

Degrees: deg(v) = 98, deg(u) = 2, deg(w) = 98, deg(x) = 2. Sum = 200 for 4 vertices, avg 50. Hmm, same as matching!

Let me see: v and w have high degree (98), u and x have low degree (2). The sum is 200 = 50 × 4. So even though the tree structure allows higher individual sums, the constraint brings the average to 50.

Wait, let me recheck. v → u → w → x → w (cycle). Constraints:
- deg(v) + deg(u) ≤ 100: 98 + 2 = 100 ✓.
- deg(u) + deg(w) ≤ 100: 2 + 98 = 100 ✓.
- deg(w) + deg(x) ≤ 100: 98 + 2 = 100 ✓.
- deg(x) + deg(w) ≤ 100: 2 + 98 = 100 ✓.
Sum = 200 = 50 × 4. 

Can we make the sum higher? deg(v) + deg(u) ≤ 100 and deg(u) + deg(w) ≤ 100. If deg(u) = 2 (minimum, since u adjacent to v and w), then deg(v) ≤ 98, deg(w) ≤ 98. And deg(w) + deg(x) ≤ 100, deg(x) ≥ 2 (adjacent to w and v), so deg(w) ≤ 98. Sum = deg(v) + deg(u) + deg(w) + deg(x) ≤ 98 + 2 + 98 + 2 = 200. Exactly 50 × 4.

What if the tree is longer? v → u → w → x → y → ... Each tree vertex has degree ≥ 2 (adjacent to parent and child in the functional graph), and the constraint alternates. Let me think about a path of length k feeding into a 2-cycle.

Path: v_1 → v_2 → v_3 → ... → v_k → c_1 ↔ c_2 (2-cycle).
Constraints: deg(v_i) + deg(v_{i+1}) ≤ 100, deg(v_k) + deg(c_1) ≤ 100, deg(c_1) + deg(c_2) ≤ 100.
Each v_i (i < k) has degree ≥ 2 (adjacent to v_{i-1} and v_{i+1} in functional graph, meaning edges v_i v_{i+1} and v_{i-1} v_i... wait, f(v_i) = v_{i+1} means v_i is adjacent to v_{i+1}. And f(v_{i-1}) = v_i means v_{i-1} adjacent to v_i. So v_i is adjacent to v_{i-1} and v_{i+1}, deg(v_i) ≥ 2.

Sum of degrees along the path + cycle: this is a path graph of constraints. The constraint graph is a path v_1 - v_2 - ... - v_k - c_1 - c_2 (with c_1 - c_2 being the cycle edge, and also c_2 - c_1 but that's the same constraint).

Actually the constraint graph (where edges represent "deg sum ≤ 100") is: v_1-v_2, v_2-v_3, ..., v_k-c_1, c_1-c_2. This is a path of length k+1 (k+2 vertices). 

Maximizing Σ deg subject to deg(i) + deg(j) ≤ 100 for each edge in this path, and deg(v_i) ≥ 2 for internal vertices, deg(c_1) ≥ 2, deg(c_2) ≥ 1 (adjacent to c_1), deg(v_1) ≥ 1 (adjacent to v_2).

For a path of m vertices with constraints deg(i)+deg(i+1) ≤ 100, the max sum is:
- If m even: 50m (pair up, each pair sums to 100).
- If m odd: 50m (the middle vertex can be 50, others pair up). Actually for odd m, max sum = 50m as well (set all to 50, or alternate 100/0 but with lower bounds).

Wait, for a path of m vertices with deg(i)+deg(i+1) ≤ 100, the max sum is 50m if m is even, and 50m if m is odd (set middle to 50, alternate 0/100 on both sides, but with lower bounds it's slightly less). Actually without lower bounds, for odd m, max = 50m (e.g., m=3: deg1=100, deg2=0, deg3=100, sum=200=50·4... no that's 50·4 not 50·3. Wait m=3: 100+0+100 = 200, but 50·3 = 150. So 200 > 150!

Hmm wait, for a path of 3 vertices with constraints deg1+deg2 ≤ 100, deg2+deg3 ≤ 100: max sum = deg1 + deg2 + deg3. Set deg2 = 0, deg1 = deg3 = 100. Sum = 200. But 50·3 = 150. So 200 > 150!

But we have lower bounds: deg2 ≥ 2 (internal vertex). So deg1 ≤ 98, deg3 ≤ 98, deg2 ≥ 2. Sum ≤ 98 + 2 + 98 = 198. Still > 150.

So a path of 3 vertices can have sum 198, avg 66 > 50! This suggests we might beat n²/4!

But wait, we need to actually realize this in a graph. The degree sum condition is necessary but not sufficient. Let me try to construct a graph realizing this.

Let me try with n = 6. Path: v1 → v2 → v3, with v3 in a 2-cycle with v4. So 4 vertices in this component, and 2 more vertices elsewhere.

Actually, let me think about n = 6 with the path structure.

Component 1: v1 → v2 → v3 ↔ v4 (2-cycle). 4 vertices.
Component 2: v5 ↔ v6 (2-cycle). 2 vertices.

Constraints:
- deg(v1) + deg(v2) ≤ 6, deg(v2) + deg(v3) ≤ 6, deg(v3) + deg(v4) ≤ 6, deg(v5) + deg(v6) ≤ 6.

Lower bounds: deg(v2) ≥ 2, deg(v3) ≥ 2, deg(v4) ≥ 1, deg(v1) ≥ 1, deg(v5) ≥ 1, deg(v6) ≥ 1.

Max sum: 
- v1 + v2 ≤ 6, v2 + v3 ≤ 6, v3 + v4 ≤ 6. With v2 ≥ 2, v3 ≥ 2.
  - Set v2 = 2, v1 = 4, v3 = 4, v4 = 2. Sum = 4+2+4+2 = 12. Or v2 = 2, v1 = 4, v3 = 4, v4 = 2. 
  - Or v2 = 2, v3 = 2, v1 = 4, v4 = 4. Sum = 4+2+2+4 = 12.
  - Max: v1 + v2 + v3 + v4 with v1+v2≤6, v2+v3≤6, v3+v4≤6. Set v2=v3=2: v1≤4, v4≤4, sum ≤ 12. Set v2=2,v3=4: v1≤4,v4≤2, sum ≤ 12. Set v2=4,v3=2: v1≤2,v4≤4, sum ≤ 12. Always 12 = 3·4 = 3·n. Hmm, 12 for 4 vertices, avg 3 = n/2.
- v5 + v6 ≤ 6. Sum ≤ 6, avg 3 = n/2.

Total: 12 + 6 = 18 = 6·3 = n·(n/2) = n²/2. So 2|E| ≤ 18, |E| ≤ 9 = n²/4. 

Interesting! So for n = 6, even with the path structure, we get |E| ≤ 9. The path didn't help because the lower bounds on internal vertices ate up the gain.

Let me recheck for n = 100. Path of 3: v1 → v2 → v3, with v3 in 2-cycle with v4. Constraints: deg(v1)+deg(v2) ≤ 100, deg(v2)+deg(v3) ≤ 100, deg(v3)+deg(v4) ≤ 100. Lower bounds: deg(v2) ≥ 2, deg(v3) ≥ 2.

Max sum of v1+v2+v3+v4: 
Let d2 = deg(v2), d3 = deg(v3). d2 ≥ 2, d3 ≥ 2, d2 + d3 ≤ 100.
v1 ≤ 100 - d2, v4 ≤ 100 - d3.
Sum ≤ (100 - d2) + d2 + d3 + (100 - d3) = 200. 

So sum = 200 regardless of d2, d3 (as long as constraints satisfied). 200 for 4 vertices = 50 × 4. Same as two 2-cycles (each giving 100 for 2 vertices, total 200 for 4).

So the path doesn't help! The sum is always 200 = 50 × 4, same as matching.

Let me verify: two 2-cycles give 100 + 100 = 200 for 4 vertices. Path + 2-cycle gives 200 for 4 vertices. Same!

What about a longer path? v1 → v2 → v3 → v4 → v5 ↔ v6. 6 vertices.
Constraints: d1+d2 ≤ 100, d2+d3 ≤ 100, d3+d4 ≤ 100, d4+d5 ≤ 100, d5+d6 ≤ 100.
Lower bounds: d2 ≥ 2, d3 ≥ 2, d4 ≥ 2, d5 ≥ 2, d1 ≥ 1, d6 ≥ 1.
Sum = d1+d2+d3+d4+d5+d6.
d1 ≤ 100-d2, d6 ≤ 100-d5.
Sum ≤ (100-d2) + d2 + d3 + d4 + d5 + (100-d5) = 200 + d3 + d4.
But d3 + d4 ≤ 100. So sum ≤ 300 = 50 × 6. ✓

And with d3 = d4 = 2 (minimum): sum = 200 + 4 = 204 < 300. With d3 + d4 = 100: sum = 300. But d3 ≥ 2, d4 ≥ 2, d3+d4 ≤ 100, so max d3+d4 = 100 (e.g., d3=50, d4=50). Sum = 300. ✓

So the sum is at most 50 × (number of vertices), regardless of the structure! Let me prove this in general.

Theorem: For any functional graph (each vertex has outdegree 1, no fixed points) on n vertices with the constraint deg(u) + deg(f(u)) ≤ n for all u, and deg(u) ≥ 1 for all u (actually we need deg(u) ≥ outdeg... hmm, let me think about what lower bounds we need).

Actually wait, I showed that even without strong lower bounds, the sum is ≤ 50n. Let me re-examine the path of 3 case (n=100, 4 vertices in component):

d1 + d2 ≤ 100, d2 + d3 ≤ 100, d3 + d4 ≤ 100. Sum = d1+d2+d3+d4.
= (d1+d2) + (d3+d4) ≤ 100 + 100 = 200 = 50·4. 

Oh! It's just pairing: (d1+d2) + (d3+d4) ≤ 100 + 100 = 200. This works because the path has even length (4 vertices), so we can pair them as (1,2) and (3,4), and each pair is constrained.

For a path of odd length, say 3 vertices: d1+d2 ≤ 100, d2+d3 ≤ 100. Sum = d1+d2+d3. 
= (d1+d2) + d3 ≤ 100 + d3. And d3 ≤ 100 - d2 ≤ 100 - 2 = 98 (if d2 ≥ 2). So sum ≤ 198. But 50·3 = 150. So 198 > 150!

But wait, in a functional graph, a path of 3 vertices (v1 → v2 → v3) must have v3 pointing somewhere. If v3 → v1 (3-cycle), then d3+d1 ≤ 100, and sum = d1+d2+d3 with d1+d2 ≤ 100, d2+d3 ≤ 100, d3+d1 ≤ 100. Sum ≤ 150 = 50·3. ✓

If v3 → v4 (continues), then it's a path of 4+, which we showed is ≤ 50·(length).

If v3 → v2 (so v2 ↔ v3 is a 2-cycle, and v1 → v2 is a tree edge), then constraints: d1+d2 ≤ 100, d2+d3 ≤ 100, d3+d2 ≤ 100 (same as d2+d3). So d1+d2 ≤ 100, d2+d3 ≤ 100. Sum = d1+d2+d3. d1 ≤ 100-d2, d3 ≤ 100-d2. Sum ≤ (100-d2) + d2 + (100-d2) = 200 - d2. With d2 ≥ 2 (v2 adjacent to v1 and v3): sum ≤ 198. And 50·3 = 150. So 198 > 150!

But this is a component of 3 vertices. The remaining 97 vertices form other components. The question is whether the total over all components can exceed 50·100 = 5000.

Component of 3 vertices (tree + 2-cycle): sum ≤ 198. 
Remaining 97 vertices: if they form 2-cycles (matching), sum ≤ 50·97... but 97 is odd, so we can't have all 2-cycles. We'd have 48 2-cycles (96 vertices) + 1 component of 1 vertex. But a component of 1 vertex is a fixed point (f(v) = v), which requires a self-loop, not allowed. So the remaining 97 vertices must form components with no fixed points, meaning cycles of length ≥ 2. 97 = 2·48 + 1, so we need at least one cycle of length ≥ 3.

Let me reconsider. The functional graph on 100 vertices with no fixed points decomposes into components, each with a cycle of length ≥ 2.

For a component that is a 2-cycle with trees: let the 2-cycle be a ↔ b, with trees rooted at a and b. 

Let me think about the general component. A component has a cycle of length ℓ ≥ 2, with trees hanging off cycle vertices. Let the component have s vertices.

I want to show: Σ_{v in component} deg(v) ≤ 50s.

For a pure cycle of length ℓ: sum ≤ 50ℓ (shown above, since 2·sum ≤ 100ℓ).

For a 2-cycle with one tree vertex: a ↔ b, c → a (c is child of a). 3 vertices. Constraints: deg(a)+deg(b) ≤ 100, deg(c)+deg(a) ≤ 100. Sum = deg(a)+deg(b)+deg(c) ≤ (100 - deg(a)) + deg(a) + (100 - deg(a)) = 200 - deg(a). With deg(a) ≥ 2 (adjacent to b and c): sum ≤ 198. 50·3 = 150. So 198 > 150!

So this component can have sum 198 > 150. But does this mean the total can exceed 5000?

If we have one such component (3 vertices, sum 198) and the rest (97 vertices) form 2-cycles: 97 is odd, can't form all 2-cycles. We need another odd component. Say another 3-vertex component (sum 198) and 94 vertices in 2-cycles (47 2-cycles, sum 4700). Total: 198 + 198 + 4700 = 5096 > 5000!

Wait, so does this mean |E| can exceed 2500?! Let me check if this is actually realizable.

Hmm, but I need to check that the degree sum condition is not just necessary but the actual graph can be realized. The degree sum ≤ n is necessary for triangle-free edges, but the actual condition (disjoint neighborhoods) is stronger. Let me try to construct such a graph.

Let me try to construct a graph on 100 vertices with > 2500 edges.

Take the component: a ↔ b (2-cycle), c → a (tree edge). 
- f(a) = b, f(b) = a, f(c) = a.
- Triangle-free edges: ab (witness for a and b), ca (witness for c).
- deg(a) + deg(b) ≤ 100, deg(c) + deg(a) ≤ 100.
- For sum 198: deg(a) = 2, deg(b) = 98, deg(c) = 98.

So a has degree 2 (adjacent to b and c), b has degree 98, c has degree 98.

Edge ab triangle-free: N(a) ∩ N(b) = ∅. N(a) = {b, c}. N(b) = 98 vertices including a. N(a) ∩ N(b) = {b, c} ∩ N(b). b ∉ N(b). c ∈ N(b)? If c is adjacent to b, then c ∈ N(b) and c ∈ N(a), so c is common neighbor. So c must NOT be adjacent to b. 

Edge ca triangle-free: N(c) ∩ N(a) = ∅. N(a) = {b, c}. N(c) = 98 vertices including a. N(c) ∩ N(a) = N(c) ∩ {b, c}. c ∉ N(c). b ∈ N(c)? If b is adjacent to c, then b ∈ N(c) and b ∈ N(a), common neighbor. So b must NOT be adjacent to c. ✓ (consistent with above).

So b and c are not adjacent. b has degree 98: adjacent to a and 97 others (not c). c has degree 98: adjacent to a and 97 others (not b). The 97 others for b and 97 others for c: these are from the remaining 97 vertices (vertices other than a, b, c). 

Are the 97 others the same for b and c? If b is adjacent to all 97 and c is adjacent to all 97, then for any vertex w among the 97, w is adjacent to both b and c. 

Now, the 97 remaining vertices each need a triangle-free edge. Each is adjacent to b and c (and possibly others). For vertex w, its triangle-free edge partner x must have N(w) ∩ N(x) = ∅. Since b, c ∈ N(w), x must not be adjacent to b or c. Who is not adjacent to b or c? Only a (since b and c are each adjacent to all 97 others + a). Wait, a is adjacent to b and c. So a IS adjacent to b and c. So there's no vertex that's not adjacent to both b and c (among the relevant vertices).

Hmm, so w's triangle-free partner x must satisfy b ∉ N(x) and c ∉ N(x). The vertices not adjacent to b: only c (and b itself). The vertices not adjacent to c: only b (and c itself). So x must be not adjacent to b AND not adjacent to c. The only vertex not adjacent to b is c, and the
