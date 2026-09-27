# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   In a city with $n = 1000$ residents, each resident has at least $k = 300$ acquaintances. A resident will participate in an election if at least one of their acquaintances is a candidate. Two residents, $A$ and $B$, are chosen as candidates for a mayoral election. Let $V$ be the number of residents who participate in the election. What is the minimum possible value of the maximum number of participants $\max_{A, B} V$ that the city can guarantee for some choice of candidates $A$ and $B$?       — 题目文本
#   Following the first solution, we choose an arbitrary resident $A$ as the first candidate. Let $k_A$ be the number of acquaintances of $A$. By the problem statement, $k_A \ge 0.3n$. Let $S$ be the set of residents not acquainted with $A$, so $|S| = n - k_A$. According to the lemma derived in the solution, there exists a resident $B$ who is acquainted with at least $30\%$ of the residents in $S$. The number of participants is the union of the acquaintances of $A$ and $B$. Thus, the number of participants $V \ge k_A + 0.3(n - k_A) = 0.7k_A + 0.3n$. Substituting $k_A \ge 0.3n$ gives $V \ge 0.7(0.3n) + 0.3n = 0.21n + 0.3n = 0.51n$. For $n = 1000$, $0.51 \times 1000 = 510$.  — 标准解答
#   Let me analyze this problem carefully.

We have a city with n=1000 residents. Each resident has at least k=300 acquaintances. A resident participates in an election if at least one of their acquaintances is a candidate. Two residents A and B are chosen as candidates. V is the number of residents who participate.

We want to find: the minimum possible value of max_{A,B} V that the city can guarantee for some choice of candidates A and B.

Let me parse this carefully. The city has a graph structure (acquaintance graph) on 1000 vertices, each vertex has degree at least 300. The city gets to choose the graph (subject to min degree 300), and then we want to guarantee that for SOME choice of candidates A, B, the number of participants V is large. Actually wait, let me re-read.

"What is the minimum possible value of the maximum number of participants max_{A,B} V that the city can guarantee for some choice of candidates A and B?"

So the question is: over all possible acquaintance graphs G with min degree ≥ 300 on 1000 vertices, what is the minimum of max_{A,B} V(G, A, B)?

In other words, the adversary (city) chooses a graph with min degree 300 to minimize the maximum participation. Then we (the candidate chooser) pick A, B to maximize V. The value is min_G max_{A,B} V.

A resident participates if at least one of A or B is their acquaintance. So V = |N(A) ∪ N(B)| where N(X) is the set of acquaintances of X. Note: does A participate? A's acquaintances include B (maybe). Actually, does a resident count themselves? Let me think. A resident participates if at least one of their acquaintances is a candidate. So if A is a candidate, A participates if A has an acquaintance who is a candidate, i.e., if B is an acquaintance of A (or A is an acquaintance of A, but no self-loops). So A participates iff A and B are acquaintances, or more precisely iff A has some acquaintance among {A, B} = iff B ∈ N(A) (since A ∉ N(A)).

Actually, V = number of residents r such that N(r) ∩ {A, B} ≠ ∅ = |{r : A ∈ N(r) or B ∈ N(r)}| = |N(A) ∪ N(B)| where N(A) = {r : A ∈ N(r)} is the set of neighbors of A (the open neighborhood). Since the graph is undirected, N(A) = neighbors of A.

So V = |N(A) ∪ N(B)| = deg(A) + deg(B) - |N(A) ∩ N(B)|.

We want to maximize this over A, B. The adversary wants to minimize this maximum.

To minimize max_{A,B} |N(A) ∪ N(B)|, the adversary wants all neighborhoods to be small (but min degree 300) and to overlap a lot.

The minimum degree is 300, so deg(A) ≥ 300 for all A. So |N(A) ∪ N(B)| ≥ 300 (just from one). But we can do better by choosing A, B with large degree and small overlap.

The adversary wants to make the graph such that for every pair A, B, |N(A) ∪ N(B)| is small.

Let me think about what structure minimizes the maximum of |N(A) ∪ N(B)|.

If the graph is a complete bipartite graph K_{300, 700}: vertices split into parts of size 300 and 700. Each vertex in the 300-part has degree 700, each vertex in the 700-part has degree 300. Min degree = 300. ✓

For two vertices A, B both in the 700-part: N(A) = the 300-part (size 300), N(B) = the 300-part (size 300). So |N(A) ∪ N(B)| = 300.

For A in 700-part, B in 300-part: N(A) = 300-part (size 300), N(B) = 700-part (size 700). |N(A) ∪ N(B)| = 300 + 700 - |N(A) ∩ N(B)|. N(A) ∩ N(B) = (300-part ∩ 700-part) ∪ ... wait. N(A) = 300-part. N(B) = 700-part. These are disjoint parts. So |N(A) ∪ N(B)| = 300 + 700 = 1000. But wait, is B in N(B)? No. Is A in N(A)? No. So N(A) = 300-part (all 300 vertices), N(B) = 700-part (all 700 vertices). Union = all 1000 vertices. So V = 1000.

So in K_{300,700}, max_{A,B} V = 1000 (achieved by picking one from each part). That's bad for the adversary.

So the adversary wants to avoid having a pair whose neighborhoods cover everything.

Let me think differently. The adversary wants to minimize max_{A,B} |N(A) ∪ N(B)|.

Consider a graph that's a union of cliques. Say we partition 1000 vertices into cliques. If we have cliques of size 301 each (min degree 300 within clique), we can fit 3 cliques of 301 = 903, plus one of 97 (but 97 < 301, so min degree would be 96 < 300). So that doesn't work unless all parts are ≥ 301.

1000 / 301 ≈ 3.32. So we can have 3 cliques of 301 = 903, remaining 97 can't form a valid clique. So we need parts of size ≥ 301. With 3 parts: sizes could be 334, 333, 333. Each vertex has degree = part_size - 1 ≥ 332 ≥ 300. ✓

In this graph (3 disjoint cliques), for A, B in the same clique of size s: N(A) ∪ N(B) = the clique minus {A, B} if A, B adjacent (which they are in a clique), so size s - 2... wait. N(A) = clique \ {A}, N(B) = clique \ {B}. Union = clique \ (something). Actually N(A) ∪ N(B) = clique \ {A} ∪ clique \ {B} = clique (since A ∈ N(B) and B ∈ N(A)). So |N(A) ∪ N(B)| = s. Wait, A ∈ N(B) since they're in the same clique and adjacent. So A ∈ N(B) ⊆ N(A) ∪ N(B). Similarly B. So union = entire clique, size s.

For A, B in different cliques: N(A) = clique_A \ {A}, N(B) = clique_B \ {B}. These are disjoint. |N(A) ∪ N(B)| = (s_A - 1) + (s_B - 1) = s_A + s_B - 2.

With cliques of size 334, 333, 333: max is achieved by picking A, B from the two largest cliques: 334 + 333 - 2 = 665. Or from same clique: 334. So max = 665.

Can the adversary do better (lower)? Let's think about the general lower bound.

We want to prove: for any graph G on 1000 vertices with min degree ≥ 300, there exist A, B with |N(A) ∪ N(B)| ≥ some value M, and the adversary can achieve M.

Let me think about the lower bound. We want to show max_{A,B} |N(A) ∪ N(B)| ≥ M for some M, for any such graph.

|N(A) ∪ N(B)| = deg(A) + deg(B) - |N(A) ∩ N(B)|.

To make this large, pick A, B with large degree and small common neighborhood.

Hmm, let me think about an averaging argument. Consider picking A, B uniformly at random. E[|N(A) ∪ N(B)|] = E[deg(A)] + E[deg(B)] - E[|N(A) ∩ N(B)|].

E[|N(A) ∩ N(B)|] = sum over v of P(v ∈ N(A) and v ∈ N(B)) = sum_v (deg(v)/n)^2 (if A, B independent uniform, but A, B distinct... approximately). Actually P(v ∈ N(A)) = deg(v)/n. For independent A, B (with replacement), P(v ∈ N(A) ∩ N(B)) = (deg(v)/n)^2.

So E[|N(A) ∩ N(B)|] ≈ sum_v (deg(v)/n)^2 = (1/n^2) sum_v deg(v)^2.

By Cauchy-Schwarz, sum deg(v)^2 ≥ (sum deg(v))^2 / n = (2m)^2 / n.

Also sum deg(v) ≥ 300 * 1000 = 300000, so 2m ≥ 300000, m ≥ 150000.

E[deg(A)] = 2m/n ≥ 300.

This is getting complicated. Let me think about it more carefully with the specific numbers.

Actually, let me reconsider the problem. The answer might be 600.

Let me think about the lower bound more carefully.

Claim: For any graph on n=1000 vertices with min degree ≥ 300, max_{A,B} |N(A) ∪ N(B)| ≥ 600.

Proof attempt: Pick any vertex A with deg(A) ≥ 300. We want to find B such that |N(A) ∪ N(B)| ≥ 600. |N(A) ∪ N(B)| = deg(A) + deg(B) - |N(A) ∩ N(B)| ≥ 300 + 300 - |N(A) ∩ N(B)| = 600 - |N(A) ∩ N(B)|.

So we need |N(A) ∩ N(B)| to be small. If we can find B with |N(A) ∩ N(B)| = 0, we get 600. But that might not be possible.

Hmm, but we want to maximize, so we want to find B minimizing the overlap with A while having large degree.

Actually, let's think about it as: we want to find A, B maximizing deg(A) + deg(B) - |N(A) ∩ N(B)|.

Let me think about the complement. Let's consider the "non-neighborhood". For vertex v, let M(v) = V \ (N(v) ∪ {v}) = set of non-neighbors of v (excluding v itself). |M(v)| = n - 1 - deg(v) ≤ 999 - 300 = 699.

A resident r does NOT participate iff r is not a neighbor of A and not a neighbor of B, i.e., r ∈ M(A) ∩ M(B) (and r ≠ A, r ≠ B, but A ∈ M(A) is false since A ∉ N(A) but A is excluded from M(A) by definition). Actually M(A) = V \ (N(A) ∪ {A}), so A ∉ M(A). Similarly B ∉ M(B).

Non-participants = {r : r ∉ N(A) and r ∉ N(B)} = M(A) ∩ M(B) (but we need r ≠ A and r ≠ B; since A ∉ M(A), A ∉ M(A) ∩ M(B); similarly B ∉ M(A) ∩ M(B) since B ∉ M(B)). So non-participants = M(A) ∩ M(B), and V = n - |M(A) ∩ M(B)|.

So max_{A,B} V = n - min_{A,B} |M(A) ∩ M(B)| = 1000 - min_{A,B} |M(A) ∩ M(B)|.

The adversary wants to maximize min_{A,B} |M(A) ∩ M(B)|, i.e., make every pair of "non-neighborhoods" have large intersection.

|M(v)| = n - 1 - deg(v) ≤ 699. To maximize the minimum pairwise intersection of the M(v) sets, the adversary wants all M(v) to be large and similar.

If all M(v) have size exactly 699 (i.e., all degrees exactly 300), and they're all the same set of 699 vertices... but can all vertices have the same non-neighborhood? If M(v) = S for all v, where |S| = 699, then each v is non-adjacent to all of S and adjacent to all of V \ (S ∪ {v}). But v ∈ V \ S (since v ∉ M(v) = S). So V \ S has 301 vertices, and they form a clique (each adjacent to all others in V \ S). Each vertex in S is adjacent to... M(v) for v ∈ S would be S \ {v} (since v ∈ S, and v is non-adjacent to all of S \ {v}... wait, let me reconsider).

Hmm, this is getting complicated. Let me think about it as: the graph is determined by degrees and structure. Let me think about what graph maximizes min_{A,B} |M(A) ∩ M(B)|.

If all M(v) are identical sets S of size 699: For v ∈ S: M(v) should be S, but v ∉ M(v), so M(v) = S \ {v}, which has size 698, not 699. Contradiction. So they can't all be identical.

Let me think about the structure where the graph is a clique on 301 vertices plus 699 isolated... no, isolated vertices have degree 0 < 300.

OK here's another approach. Consider the complement graph H. In H, each vertex has degree ≤ 699 (since in G, degree ≥ 300, so in H, degree ≤ 999 - 300 = 699). M(v) in G = N_H(v) ∪ ... wait. M(v) = V \ (N_G(v) ∪ {v}) = N_H(v) where H is the complement graph (without self-loops). Actually in the complement graph H, N_H(v) = V \ ({v} ∪ N_G(v)) = M(v). Yes!

So |M(A) ∩ M(B)| = |N_H(A) ∩ N_H(B)|.

We want to minimize this over A, B (to maximize V). The adversary wants to maximize min_{A,B} |N_H(A) ∩ N_H(B)| where H is a graph on 1000 vertices with max degree ≤ 699.

So the problem becomes: Given a graph H on n=1000 vertices with maximum degree ≤ 699 (= n - 1 - 300 = n - k - 1), find the maximum possible value of min_{A≠B} |N_H(A) ∩ N_H(B)|, and the answer to the original problem is 1000 minus that.

Wait, but we also need A ≠ B (two distinct candidates). Let me assume A ≠ B.

So we want: max_H min_{A≠B} |N_H(A) ∩ N_H(B)| where Δ(H) ≤ 699.

Then answer = 1000 - (that max).

Let me denote d = 699 = n - k - 1. We want to find a graph H on n vertices with max degree ≤ d that maximizes the minimum common neighborhood.

Intuitively, to maximize common neighborhoods, we want H to be as "dense and uniform" as possible. If H is a complete graph on n vertices, every pair has common neighborhood n - 2, but max degree = n - 1 = 999 > 699. Not allowed.

If H is d-regular, then for each pair A, B: |N_H(A) ∩ N_H(B)| = ? In a d-regular graph, |N_H(A) ∩ N_H(B)| depends on whether A, B are adjacent.

If A, B adjacent: |N_H(A) ∩ N_H(B)| = |N_H(A)| + |N_H(B)| - |N_H(A) ∪ N_H(B)|. N_H(A) ∪ N_H(B) ⊆ V \ {A, B}... hmm, actually A ∈ N_H(B) and B ∈ N_H(A) since they're adjacent. So N_H(A) ∪ N_H(B) ⊆ V. |N_H(A) ∪ N_H(B)| = 2d - |N_H(A) ∩ N_H(B)|. Also N_H(A) ∪ N_H(B) ⊆ V, and A ∈ N_H(B) ⊆ union, B ∈ N_H(A) ⊆ union. So the union is a subset of V. The complement of the union in V has size n - |union| = n - 2d + |intersection|.

This is getting circular. Let me think about specific constructions.

Construction 1: H is a complete bipartite graph K_{699, 301}. Max degree = 699 (for vertices in the 301-part) and 301 (for vertices in the 699-part). Max degree = 699 ≤ 699. ✓

For A, B both in the 301-part: N_H(A) = 699-part, N_H(B) = 699-part. |N_H(A) ∩ N_H(B)| = 699.

For A, B both in the 699-part: N_H(A) = 301-part, N_H(B) = 301-part. |intersection| = 301.

For A in 301-part, B in 699-part: N_H(A) = 699-part, N_H(B) = 301-part. |intersection| = 0 (disjoint parts). Wait, but A ∈ 301-part and B ∈ 699-part. N_H(A) = 699-part (since A is connected to all of 699-part). N_H(B) = 301-part. These are disjoint. So |N_H(A) ∩ N_H(B)| = 0.

So min_{A≠B} |N_H(A) ∩ N_H(B)| = 0. That's terrible for the adversary.

Construction 2: H is a union of cliques. To maximize min common neighborhood, we want large cliques. With max degree 699, the largest clique has size 700. We can have one clique of 700 and need to handle the remaining 300 vertices. They need max degree ≤ 699, so they can form a clique of 300 (max degree 299 ≤ 699). 

For A, B in the 700-clique: |N_H(A) ∩ N_H(B)| = 698 (all other vertices in the clique).
For A, B in the 300-clique: |N_H(A) ∩ N_H(B)| = 298.
For A in 700-clique, B in 300-clique: N_H(A) = 700-clique \ {A}, N_H(B) = 300-clique \ {B}. Disjoint. |intersection| = 0.

min = 0. Still bad.

The problem is that for pairs in different components, the common neighborhood is 0.

So the adversary needs H to be connected (or at least have overlapping neighborhoods across all pairs).

Construction 3: H is a complete multipartite graph? Or some other structure?

Let me think about what maximizes min_{A≠B} |N_H(A) ∩ N_H(B)|.

For any two vertices A, B, |N_H(A) ∩ N_H(B)| counts common neighbors. To make this large for all pairs, we want every pair to share many neighbors.

Consider H = complete graph K_{1000} minus a perfect matching (or some regular structure). Max degree = 998. Too high.

We need max degree ≤ 699. So each vertex is missing at least 300 edges (compared to complete graph).

Idea: H is the complement of a 300-regular graph G. Then H has degree 999 - 300 = 699 for every vertex. So H is 699-regular.

In a 699-regular graph H on 1000 vertices, for adjacent A, B: |N_H(A) ∩ N_H(B)| = 699 + 699 - |N_H(A) ∪ N_H(B)|. The union N_H(A) ∪ N_H(B) includes A and B (since adjacent), so |union| ≥ 2. Actually |union| ≤ 1000. So |intersection| ≥ 699 + 699 - 1000 = 398. And for non-adjacent A, B: A ∉ N_H(B), B ∉ N_H(A), so N_H(A) ∪ N_H(B) ⊆ V \ {A, B}, |union| ≤ 998, |intersection| ≥ 699 + 699 - 998 = 400.

So in any 699-regular graph, min_{A≠B} |N_H(A) ∩ N_H(B)| ≥ 398 (for adjacent pairs). Can we achieve exactly 398?

For adjacent A, B: |N_H(A) ∩ N_H(B)| = 1398 - |N_H(A) ∪ N_H(B)|. |N_H(A) ∪ N_H(B)| ≤ 1000. So |intersection| ≥ 398. Equality when N_H(A) ∪ N_H(B) = V, i.e., every vertex is a neighbor of A or B.

For non-adjacent A, B: |intersection| ≥ 400. Equality when N_H(A) ∪ N_H(B) = V \ {A, B}.

So the minimum is at least 398 (achieved by adjacent pairs where the union of neighborhoods is everything).

Can we construct a 699-regular graph where every adjacent pair has N_H(A) ∪ N_H(B) = V? That means for every edge AB, every other vertex is adjacent to A or B. Equivalently, there's no vertex that is non-adjacent to both A and B. In terms of the complement G (300-regular), this means: for every non-edge AB in G (i.e., edge AB in H), there's no vertex adjacent to both A and B in G. I.e., no two non-adjacent vertices in G have a common neighbor. That's a very strong condition.

Hmm, this is getting complicated. Let me think about whether 398 is achievable or if the actual minimum common neighborhood can be higher.

Actually, wait. Let me reconsider. The adversary wants to MAXIMIZE min_{A≠B} |N_H(A) ∩ N_H(B)|. So the adversary wants the minimum common neighborhood to be as large as possible. We showed that in any 699-regular graph, min ≥ 398. But can the adversary do better than 398?

If the adversary uses a 699-regular graph, the minimum is at least 398, and possibly higher if the graph is structured well. But can the adversary make it higher than 398?

For adjacent pairs, the common neighborhood is 1398 - |union|, and |union| ≤ 1000, so common neighborhood ≥ 398. To make it higher, we need |union| < 1000, i.e., some vertex is non-adjacent to both A and B. But that would mean in H, some vertex c is not a neighbor of A and not a neighbor of B. Since A, B are adjacent in H, c ≠ A, B. So c is a non-neighbor of both A and B in H, meaning c is a neighbor of both A and B in G (the complement). 

To maximize the minimum, the adversary wants |union| to be as small as possible for the worst-case pair. But the adversary controls the graph, so they want to make all pairs have large common neighborhood.

Hmm, but actually the adversary wants to maximize the minimum over all pairs. So they want to construct H such that even the worst pair has large common neighborhood.

Let me think about an upper bound on what the adversary can achieve.

Upper bound on min_{A≠B} |N_H(A) ∩ N_H(B)|:

Consider any graph H with max degree ≤ 699. Pick a vertex A with degree d_A ≤ 699. For any other vertex B, |N_H(A) ∩ N_H(B)| ≤ d_A ≤ 699. That's not tight enough.

Let me think about it differently. Consider the vertex A with the smallest degree in H (largest degree in G). Actually, all degrees in H are ≤ 699, and could be less.

Hmm, let me think about a cleaner approach.

Let me reconsider. We have G with min degree ≥ 300. We want max_{A,B} |N_G(A) ∪ N_G(B)|. We showed this equals 1000 - min_{A,B} |N_H(A) ∩ N_H(B)| where H = complement of G, max degree ≤ 699.

So the answer = 1000 - max_H min_{A≠B} |N_H(A) ∩ N_H(B)|.

Let me think about what max_H min_{A≠B} |N_H(A) ∩ N_H(B)| is.

Upper bound: For any H with max degree ≤ 699, consider the pair (A, B) that are adjacent in H (if H has an edge). |N_H(A) ∩ N_H(B)| ≤ min(deg_H(A), deg_H(B)) ≤ 699. Not helpful.

Better approach: Think about a specific vertex v. How many pairs (A, B) have v as a common neighbor? v is a common neighbor of A, B iff A, B ∈ N_H(v). So the number of pairs sharing v as common neighbor is C(deg_H(v), 2). Total over all v: sum_v C(deg_H(v), 2) = sum of common neighborhoods over all pairs = sum_{A<B} |N_H(A) ∩ N_H(B)|.

By convexity, sum_v C(deg_H(v), 2) is maximized when degrees are as unequal as possible, but we have max degree ≤ 699. To maximize the sum, make as many vertices as possible have degree 699.

But we want to maximize the MINIMUM, not the sum. Let me think about it via the average.

Average common neighborhood = [sum_v C(deg_H(v), 2)] / C(n, 2).

If all degrees are 699: sum_v C(699, 2) = 1000 * 699 * 698 / 2. Average = 1000 * 699 * 698 / (2 * 1000 * 999 / 2) = 699 * 698 / 999 = 488302 / 999 ≈ 488.8.

So the average common neighborhood is about 489 when H is 699-regular. The minimum is at most the average, so min ≤ 489 (approximately). But we showed min ≥ 398 for 699-regular. So the answer is between 1000 - 489 = 511 and 1000 - 398 = 602.

Hmm, let me be more precise. For a 699-regular graph H on 1000 vertices:

For adjacent A, B: |N_H(A) ∩ N_H(B)| = 2*699 - |N_H(A) ∪ N_H(B)|. Since A ∈ N_H(B) and B ∈ N_H(A), |N_H(A) ∪ N_H(B)| ≤ 1000. So |intersection| ≥ 398.

For non-adjacent A, B: |N_H(A) ∪ N_H(B)| ≤ 998 (can't include A or B). So |intersection| ≥ 400.

The minimum is achieved by adjacent pairs. Can we make all adjacent pairs have |intersection| = 398? That requires |N_H(A) ∪ N_H(B)| = 1000 for all edges AB, meaning every vertex is a neighbor of A or B (in H) for every edge AB.

Alternatively, can we make the minimum larger? If for every edge AB, there exists some vertex not in N_H(A) ∪ N_H(B), then |intersection| ≥ 399 for that edge. To get min ≥ 399, we need every edge AB to have |N_H(A) ∪ N_H(B)| ≤ 999, i.e., some vertex c is non-adjacent to both A and B in H, i.e., c is adjacent to both A and B in G.

In G (300-regular), for every non-edge AB (edge in H), there exists c adjacent to both A and B in G. This means every pair of non-adjacent vertices in G has a common neighbor. This is related to the graph having diameter 2 (for non-adjacent pairs).

A 300-regular graph on 1000 vertices with diameter 2: does this exist? The Moore bound for diameter 2 and degree 300 is 300^2 + 1 = 90001, much larger than 1000, so it's certainly possible. In fact, a random 300-regular graph on 1000 vertices will have diameter 2 with high probability.

But wait, we need more: for EVERY non-edge AB in G, there's a common neighbor. And we want to maximize the minimum common neighborhood in H, which means for every edge AB in H (non-edge in G), we want |N_H(A) ∩ N_H(B)| to be large, i.e., |N_H(A) ∪ N_H(B)| to be small, i.e., many vertices non-adjacent to both A and B in H, i.e., many common neighbors of A, B in G.

So the adversary (choosing G) wants: for every non-edge AB in G, A and B have many common neighbors in G. Equivalently, in H, for every edge AB, |N_H(A) ∪ N_H(B)| is small.

|N_H(A) ∪ N_H(B)| = 2*699 - |N_H(A) ∩ N_H(B)| for adjacent A, B. And |N_H(A) ∪ N_H(B)| = 1000 - |{c : c ∉ N_H(A), c ∉ N_H(B), c ≠ A, c ≠ B}| - ... hmm wait. Let me recount.

V = {A, B} ∪ (N_H(A) ∪ N_H(B)) ∪ (V \ ({A,B} ∪ N_H(A) ∪ N_H(B))).

Since A ∈ N_H(B) and B ∈ N_H(A) (adjacent), {A, B} ⊆ N_H(A) ∪ N_H(B). So V = (N_H(A) ∪ N_H(B)) ∪ (V \ (N_H(A) ∪ N_H(B))).

|N_H(A) ∪ N_H(B)| = 1000 - |V \ (N_H(A) ∪ N_H(B))|.

V \ (N_H(A) ∪ N_H(B)) = {c : c ∉ N_H(A) and c ∉ N_H(B)} = {c : c is non-adjacent to A in H and non-adjacent to B in H} = {c : c is adjacent to A in G and adjacent to B in G, c ≠ A, c ≠ B} = common neighbors of A, B in G (since A, B are non-adjacent in G, A is not a neighbor of B in G and vice versa, so we don't need to worry about A, B being in this set).

So |V \ (N_H(A) ∪ N_H(B))| = |N_G(A) ∩ N_G(B)| (common neighbors in G, for non-adjacent A, B in G).

So |N_H(A) ∩ N_H(B)| = 1398 - (1000 - |N_G(A) ∩ N_G(B)|) = 398 + |N_G(A) ∩ N_G(B)|.

So for non-adjacent A, B in G (adjacent in H): |N_H(A) ∩ N_H(B)| = 398 + |N_G(A) ∩ N_G(B)|.

For adjacent A, B in G (non-adjacent in H): |N_H(A) ∩ N_H(B)| = 400 + |N_G(A) ∩ N_G(B)| - ... let me redo this.

For non-adjacent A, B in H (adjacent in G): A ∉ N_H(B), B ∉ N_H(A). N_H(A) ∪ N_H(B) ⊆ V \ {A, B}. |N_H(A) ∪ N_H(B)| = |N_H(A)| + |N_H(B)| - |N_H(A) ∩ N_H(B)| = 2*699 - |intersection| (if 699-regular). Also |N_H(A) ∪ N_H(B)| ≤ 998. So |intersection| ≥ 400.

V \ ({A,B} ∪ N_H(A) ∪ N_H(B)) = {c ≠ A, B : c ∉ N_H(A), c ∉ N_H(B)} = {c ≠ A, B : c ∈ N_G(A), c ∈ N_G(B)}. Since A, B adjacent in G, A ∈ N_G(B) and B ∈ N_G(A), but we exclude A, B. So this is |N_G(A) ∩ N_G(B)| - 2 (removing A and B if they're in the intersection; A ∈ N_G(B) so A ∈ N_G(A) ∩ N_G(B)? No, A ∉ N_G(A). So A ∉ N_G(A) ∩ N_G(B). Similarly B ∉ N_G(A) ∩ N_G(B). So the set is just N_G(A) ∩ N_G(B) \ {A, B} = N_G(A) ∩ N_G(B) (since A, B not in it). Wait, A ∈ N_G(B) but A ∉ N_G(A), so A ∉ N_G(A) ∩ N_G(B). Similarly B. So {c ≠ A, B : c ∈ N_G(A) ∩ N_G(B)} = N_G(A) ∩ N_G(B).

So |N_H(A) ∪ N_H(B)| = 998 - |N_G(A) ∩ N_G(B)|. (Since V \ {A, B} has 998 elements, and the union is a subset, with the complement being N_G(A) ∩ N_G(B).)

So |N_H(A) ∩ N_H(B)| = 2*699 - (998 - |N_G(A) ∩ N_G(B)|) = 1398 - 998 + |N_G(A) ∩ N_G(B)| = 400 + |N_G(A) ∩ N_G(B)|.

So:
- For A, B non-adjacent in G (edge in H): |N_H(A) ∩ N_H(B)| = 398 + |N_G(A) ∩ N_G(B)| ≥ 398.
- For A, B adjacent in G (non-edge in H): |N_H(A) ∩ N_H(B)| = 400 + |N_G(A) ∩ N_G(B)| ≥ 400.

The minimum is achieved by non-adjacent pairs in G with the fewest common neighbors. So:

min_{A≠B} |N_H(A) ∩ N_H(B)| = 398 + min_{A,B non-adjacent in G} |N_G(A) ∩ N_G(B)|.

(assuming G is 300-regular, so H is 699-regular).

The adversary wants to maximize this, so they want to maximize min_{non-adjacent A,B in G} |N_G(A) ∩ N_G(B)|.

So the question reduces to: what is the maximum possible value of min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)| over all 300-regular graphs G on 1000 vertices? (Or more generally, graphs with min degree ≥ 300.)

Wait, but I assumed 699-regular H (300-regular G). The adversary might not use a regular graph. Let me reconsider.

Actually, let me reconsider whether the adversary should use a regular graph. If G has min degree ≥ 300 but some vertices have higher degree, then H has lower degree for those vertices, which means |N_H(A) ∩ N_H(B)| could be smaller for pairs involving those vertices. So the adversary probably wants all degrees in H to be as large as possible (all degrees in G as small as possible, i.e., exactly 300). So 300-regular G (699-regular H) is likely optimal for the adversary.

But let me not assume this and think more generally later. For now, assume G is 300-regular.

So we need: max over 300-regular graphs G on 1000 vertices of min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)|.

Let me denote this as μ. Then the answer would be 1000 - 398 - μ = 602 - μ.

Now, what's the maximum possible μ?

For a 300-regular graph on 1000 vertices, consider non-adjacent vertices A, B. |N_G(A) ∩ N_G(B)| = number of common neighbors. 

Upper bound on μ: Consider any vertex A. A has 300 neighbors and 699 non-neighbors (excluding A itself). For each non-neighbor B of A, |N_G(A) ∩ N_G(B)| ≤ 300 (trivially). But we want a better bound.

Sum over all non-adjacent pairs (A, B) of |N_G(A) ∩ N_G(B)| = sum_v (number of non-adjacent pairs both adjacent to v) = sum_v C(deg(v) - ..., 2)... hmm, let me think.

For a fixed vertex v, the number of non-adjacent pairs (A, B) with A, B ∈ N_G(v) is C(deg(v), 2) - (number of edges within N_G(v)). 

This is getting complicated. Let me try a different approach.

Total common neighbors over all pairs = sum_v C(deg(v), 2) = 1000 * C(300, 2) = 1000 * 300 * 299 / 2 = 1000 * 44850 = 44,850,000.

Number of pairs = C(1000, 2) = 499,500.

Average common neighbors = 44,850,000 / 499,500 ≈ 89.79.

So the average common neighborhood (over all pairs) is about 90. The minimum over non-adjacent pairs is at most the average over non-adjacent pairs, which is at most the overall average (roughly). So μ ≤ ~90, giving answer ≥ 602 - 90 = 512.

But wait, this is the average over ALL pairs (including adjacent ones). For adjacent pairs, common neighbors might be different. Let me be more careful.

sum_{all pairs {A,B}} |N_G(A) ∩ N_G(B)| = sum_v C(deg_G(v), 2) = 1000 * C(300,2) = 44,850,000.

This sum is over all pairs. We can split into adjacent and non-adjacent pairs.

Number of edges = 1000 * 300 / 2 = 150,000.
Number of non-adjacent pairs = 499,500 - 150,000 = 349,500.

sum_{adjacent pairs} |N_G(A) ∩ N_G(B)| + sum_{non-adjacent pairs} |N_G(A) ∩ N_G(B)| = 44,850,000.

For adjacent A, B: |N_G(A) ∩ N_G(B)| = |N_G(A)| + |N_G(B)| - |N_G(A) ∪ N_G(B)|. Since A ∈ N_G(B) and B ∈ N_G(A), and N_G(A) ∪ N_G(B) ⊆ V, |N_G(A) ∪ N_G(B)| ≤ 1000. So |N_G(A) ∩ N_G(B)| ≥ 300 + 300 - 1000 = -400, which is trivially true. Not helpful.

Let me think about it differently. For adjacent A, B: |N_G(A) ∩ N_G(B)| counts common neighbors. A is a neighbor of B but A ∉ N_G(A), so A is not a common neighbor. Similarly B. So common neighbors are vertices adjacent to both A and B, excluding A, B.

Hmm, I think the key insight is about the structure. Let me think about what graph maximizes the minimum common neighborhood for non-adjacent pairs.

Consider G = complete bipartite graph K_{300, 700}. This is 300-regular for the 700-part and 700-regular for the 300-part. Not 300-regular overall. Min degree = 300. ✓

For non-adjacent A, B both in the 700-part: N_G(A) = 300-part, N_G(B) = 300-part. |N_G(A) ∩ N_G(B)| = 300.

For non-adjacent A, B both in the 300-part: N_G(A) = 700-part, N_G(B) = 700-part. |intersection| = 700.

For adjacent A (in 700-part), B (in 300-part): they're adjacent, so not a non-adjacent pair.

So min_{non-adjacent} |N_G(A) ∩ N_G(B)| = 300 (for pairs in the 700-part).

But G is not 300-regular. Let me compute the answer for this G directly.

In this G, H = complement = K_{700} ∪ K_{300} (two cliques). Wait, complement of K_{300,700} is K_{300} ∪ K_{700} (cliques on each part). Max degree in H = 699 (for 700-clique) and 299 (for 300-clique). Max degree = 699 ≤ 699. ✓

For A, B in the 700-clique of H (non-adjacent in G, both in 700-part): |N_H(A) ∩ N_H(B)| = 698 (all other vertices in 700-clique). So |N_G(A) ∩ N_G(B)| = |N_H(A) ∩ N_H(B)| - 398 = 698 - 398 = 300. ✓ (matches our calculation).

For A, B in the 300-clique of H (non-adjacent in G, both in 300-part): |N_H(A) ∩ N_H(B)| = 298. So |N_G(A) ∩ N_G(B)| = 298 - 400 = -102?? That can't be right.

Wait, I think my formula was for 699-regular H. H here is not regular. Let me recompute directly.

For A, B in 300-part of G (so in 300-clique of H), non-adjacent in G: N_H(A) = 300-clique \ {A} (size 299), N_H(B) = 300-clique \ {B} (size 299). |N_H(A) ∩ N_H(B)| = 298 (all of 300-clique except A, B).

V = 1000. Non-participants = |N_H(A) ∩ N_H(B)| = 298. So V = 1000 - 298 = 702.

For A, B in 700-part of G (700-clique of H), non-adjacent in G: |N_H(A) ∩ N_H(B)| = 698. V = 1000 - 698 = 302.

For A in 300-part, B in 700-part (adjacent in G, non-adjacent in H): N_H(A) = 300-clique \ {A} (size 299), N_H(B) = 700-clique \ {B} (size 699). |N_H(A) ∩ N_H(B)| = 0 (disjoint). V = 1000 - 0 = 1000.

So max_{A,B} V = 1000 (achieved by cross-part pairs). This is bad for the adversary.

So K_{300,700} gives max V = 1000. The adversary wants to minimize this, so they won't use this.

Let me go back to the 300-regular case and think about what maximizes μ = min_{non-adjacent} |N_G(A) ∩ N_G(B)|.

The key question: what is the maximum μ such that there exists a 300-regular graph on 1000 vertices where every pair of non-adjacent vertices has at least μ common neighbors?

This is related to the concept of "co-degree" or common neighborhood.

Let me think about an upper bound on μ. 

Consider a vertex A with 300 neighbors. The 699 non-neighbors of A each share at least μ common neighbors with A. Each common neighbor of A and B is a neighbor of A. So the 300 neighbors of A are "shared" among the 699 non-neighbors. 

For each neighbor c of A, how many non-neighbors B of A is c adjacent to? c is adjacent to A and to deg(c) - 1 - (number of neighbors of A that c is adjacent to) other vertices. Hmm, this is getting complicated.

Let me use a counting argument. Fix vertex A. sum_{B non-adjacent to A} |N_G(A) ∩ N_G(B)| = sum_{c ∈ N_G(A)} |{B non-adjacent to A : c ∈ N_G(B)}| = sum_{c ∈ N_G(A)} (deg(c) - 1 - |N_G(A) ∩ N_G(c)|).

Wait, c ∈ N_G(A). B is a non-neighbor of A with c ∈ N_G(B). The number of such B is the number of neighbors of c that are non-neighbors of A, which is deg(c) - |N_G(c) ∩ N_G(A)| - [A ∈ N_G(c)? yes, since c ∈ N_G(A) means A ∈ N_G(c)]. So neighbors of c that are non-neighbors of A = deg(c) - |N_G(c) ∩ N_G(A)| (since A is a neighbor of c but A is not a non-neighbor of A, and we're counting non-neighbors of A among neighbors of c). 

Actually: neighbors of c = N_G(c). Among these, some are neighbors of A (i.e., in N_G(A)) and some are non-neighbors of A. |N_G(c) ∩ N_G(A)| = common neighbors of A and c (but A and c are adjacent, so this counts vertices adjacent to both, excluding A and c). The number of neighbors of c that are non-neighbors of A = deg(c) - 1 - |N_G(c) ∩ N_G(A)|. The -1 is for A itself (A is a neighbor of c but A is not a non-neighbor of A; A is A).

Hmm wait. Neighbors of c: N_G(c), which has deg(c) = 300 elements. A ∈ N_G(c). Neighbors of A: N_G(A), 300 elements. c ∈ N_G(A).

Neighbors of c that are non-neighbors of A: {x ∈ N_G(c) : x ∉ N_G(A), x ≠ A}. Since A ∈ N_G(c) but A ∉ N_G(A) (no self-loop) and A is not a "non-neighbor of A" in the sense we want (we want B ≠ A). Actually, non-neighbors of A = V \ (N_G(A) ∪ {A}). So B is a non-neighbor of A iff B ∉ N_G(A) and B ≠ A.

So {x ∈ N_G(c) : x is a non-neighbor of A} = N_G(c) \ (N_G(A) ∪ {A}) = N_G(c) \ N_G(A) (since A ∈ N_G(c) and A ∉ N_G(A), so A is already removed by the set difference with N_G(A)... no. N_G(c) \ N_G(A) removes elements of N_G(A) from N_G(c). A ∈ N_G(c) but A ∉ N_G(A), so A is NOT removed. So N_G(c) \ N_G(A) still contains A. We need to also remove A.)

So {x ∈ N_G(c) : x is a non-neighbor of A} = N_G(c) \ (N_G(A) ∪ {A}) = (N_G(c) \ N_G(A)) \ {A}.

|N_G(c) \ N_G(A)| = deg(c) - |N_G(c) ∩ N_G(A)| = 300 - |N_G(A) ∩ N_G(c)|.

So the count = 300 - |N_G(A) ∩ N_G(c)| - 1 (removing A) = 299 - |N_G(A) ∩ N_G(c)|.

So sum_{B non-adjacent to A} |N_G(A) ∩ N_G(B)| = sum_{c ∈ N_G(A)} (299 - |N_G(A) ∩ N_G(c)|) = 300 * 299 - sum_{c ∈ N_G(A)} |N_G(A) ∩ N_G(c)|.

Now, sum_{c ∈ N_G(A)} |N_G(A) ∩ N_G(c)| = sum_{c ∈ N_G(A)} |{d ∈ N_G(A) : d ∈ N_G(c)}| = sum_{d ∈ N_G(A)} |{c ∈ N_G(A) : d ∈ N_G(c)}| = sum_{d ∈ N_G(A)} |N_G(A) ∩ N_G(d)|.

Wait, that's the same sum. Let me denote S = sum_{c ∈ N_G(A)} |N_G(A) ∩ N_G(c)|. This counts the number of edges within N_G(A) (each edge {c, d} within N_G(A) is counted... hmm, |N_G(A) ∩ N_G(c)| for c ∈ N_G(A) counts neighbors of c that are in N_G(A), which is the number of edges from c to other vertices in N_G(A). So S = 2 * (number of edges within N_G(A)).

Let e_A = number of edges within N_G(A). Then S = 2 * e_A.

So sum_{B non-adjacent to A} |N_G(A) ∩ N_G(B)| = 300 * 299 - 2 * e_A = 89700 - 2 * e_A.

There are 699 non-adjacent vertices B. So the average common neighborhood for non-adjacent pairs involving A is (89700 - 2 * e_A) / 699.

For the minimum to be at least μ, we need (89700 - 2 * e_A) / 699 ≥ μ for all A, roughly (the average being ≥ μ is necessary but not sufficient for the min to be ≥ μ). Actually, we need every individual term to be ≥ μ, so the average is also ≥ μ. So:

89700 - 2 * e_A ≥ 699 * μ for all A.

e_A ≤ (89700 - 699μ) / 2.

Now, sum over all A of e_A = sum_A (edges within N_G(A)) = sum_{edge {c,d}} |{A : c ∈ N_G(A) and d ∈ N_G(A)}| = sum_{edge {c,d}} |N_G(c) ∩ N_G(d)| (common neighbors of c, d, which are adjacent).

Hmm, this is getting complicated. Let me try a different approach.

Let me think about the problem from a higher level. The answer is 1000 - max_H min_{A≠B} |N_H(A) ∩ N_H(B)| where H has max degree ≤ 699.

Let me think about what the optimal H looks like. We want to maximize the minimum common neighborhood. 

Consider H being a "complete multipartite graph" or some structured graph. Actually, let me think about H being a complete bipartite graph plus some edges.

Hmm, let me think about this differently. Let me consider the problem in terms of the original graph G.

We want min_G max_{A,B} |N_G(A) ∪ N_G(B)| where G has min degree ≥ 300 on 1000 vertices.

|N_G(A) ∪ N_G(B)| = 1000 - |M(A) ∩ M(B)| where M(v) = non-neighbors of v (excluding v).

We want to find the G that minimizes max_{A,B} |N_G(A) ∪ N_G(B)|, i.e., maximizes min_{A,B} |M(A) ∩ M(B)|.

|M(v)| = 999 - deg(v) ≤ 699.

To maximize min_{A,B} |M(A) ∩ M(B)|, we want all M(v) to be large (so deg(v) = 300 for all v, making |M(v)| = 699) and to have large pairwise intersections.

By the inclusion-exclusion principle, |M(A) ∩ M(B)| = |M(A)| + |M(B)| - |M(A) ∪ M(B)| ≥ 699 + 699 - 1000 = 398 (since M(A) ∪ M(B) ⊆ V, but actually A ∉ M(A) and B ∉ M(B), so M(A) ∪ M(B) ⊆ V \ ... hmm, A ∉ M(A) but A could be in M(B) if A is a non-neighbor of B. So M(A) ∪ M(B) ⊆ V. So |M(A) ∪ M(B)| ≤ 1000, giving |M(A) ∩ M(B)| ≥ 398.

But can we achieve |M(A) ∩ M(B)| = 398 for all pairs? That requires |M(A) ∪ M(B)| = 1000 for all pairs, i.e., M(A) ∪ M(B) = V for all A, B. This means for every vertex v and every pair A, B, v ∈ M(A) or v ∈ M(B), i.e., v is a non-neighbor of A or a non-neighbor of B.

Equivalently, there's no vertex v that is a neighbor of both A and B, i.e., |N_G(A) ∩ N_G(B)| = 0 for all A, B (well, for all A ≠ B). But that's impossible since each vertex has 300 neighbors and there are 1000 vertices; by pigeonhole, some pair shares a neighbor.

Actually wait, |N_G(A) ∩ N_G(B)| = 0 for all A ≠ B would mean the neighborhoods are pairwise disjoint, but 1000 * 300 = 300000 > 1000, impossible.

So we can't achieve 398 for all pairs. The minimum of |M(A) ∩ M(B)| will be higher than 398.

Let me think about the upper bound on min_{A,B} |M(A) ∩ M(B)| more carefully.

We have |M(A) ∩ M(B)| = 1398 - |M(A) ∪ M(B)|. To minimize this (which is what the "maximizer" of V wants), we maximize |M(A) ∪ M(B)|. The adversary wants to make |M(A) ∪ M(B)| small for all pairs.

|M(A) ∪ M(B)| = |M(A)| + |M(B)| - |M(A) ∩ M(B)|. If all |M(v)| = 699, then |M(A) ∪ M(B)| = 1398 - |M(A) ∩ M(B)|. And |M(A) ∪ M(B)| ≤ 1000, so |M(A) ∩ M(B)| ≥ 398.

Now, |M(A) ∪ M(B)| = 1000 - |{v : v ∉ M(A) and v ∉ M(B)}| = 1000 - |{v : v ∈ N_G(A) ∪ {A} and v ∈ N_G(B) ∪ {B}}|.

{v : v ∈ N_G(A) ∪ {A} and v ∈ N_G(B) ∪ {B}} = (N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}).

If A, B are non-adjacent: A ∉ N_G(B), B ∉ N_G(A). (N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}) = (N_G(A) ∩ N_G(B)) ∪ (N_G(A) ∩ {B}) ∪ ({A} ∩ N_G(B)) ∪ ({A} ∩ {B}). Since A ≠ B, {A} ∩ {B} = ∅. N_G(A) ∩ {B} = ∅ (B ∉ N_G(A)). {A} ∩ N_G(B) = ∅ (A ∉ N_G(B)). So the intersection = N_G(A) ∩ N_G(B).

So |M(A) ∪ M(B)| = 1000 - |N_G(A) ∩ N_G(B)|, and |M(A) ∩ M(B)| = 1398 - 1000 + |N_G(A) ∩ N_G(B)| = 398 + |N_G(A) ∩ N_G(B)|.

If A, B are adjacent: A ∈ N_G(B), B ∈ N_G(A). (N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}) = (N_G(A) ∩ N_G(B)) ∪ (N_G(A) ∩ {B}) ∪ ({A} ∩ N_G(B)) ∪ {A, B}... hmm, let me be more careful. B ∈ N_G(A), so B ∈ N_G(A) ∪ {A}. A ∈ N_G(B), so A ∈ N_G(B) ∪ {B}. So A ∈ (N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}) and B ∈ same. 

(N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}) = N_G(A) ∩ N_G(B) ∪ N_G(A) ∩ {B} ∪ {A} ∩ N_G(B) ∪ {A} ∩ {B}.

N_G(A) ∩ {B} = {B} (since B ∈ N_G(A)). {A} ∩ N_G(B) = {A} (since A ∈ N_G(B)). {A} ∩ {B} = ∅.

So the intersection = (N_G(A) ∩ N_G(B)) ∪ {A} ∪ {B}. |intersection| = |N_G(A) ∩ N_G(B)| + 2 (since A, B ∉ N_G(A) ∩ N_G(B) as A ∉ N_G(A), B ∉ N_G(B)).

So |M(A) ∪ M(B)| = 1000 - |N_G(A) ∩ N_G(B)| - 2, and |M(A) ∩ M(B)| = 1398 - (1000 - |N_G(A) ∩ N_G(B)| - 2) = 400 + |N_G(A) ∩ N_G(B)|.

So:
- Non-adjacent A, B: |M(A) ∩ M(B)| = 398 + |N_G(A) ∩ N_G(B)|
- Adjacent A, B: |M(A) ∩ M(B)| = 400 + |N_G(A) ∩ N_G(B)|

The minimum over all pairs is achieved by non-adjacent pairs with the fewest common neighbors. So:

min_{A≠B} |M(A) ∩ M(B)| = 398 + min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)|.

(assuming all degrees are exactly 300; if some degrees are higher, |M(v)| is smaller, which could reduce the intersection further. So the adversary should use 300-regular.)

Wait, but I need to also check: if degrees are not all 300, could the minimum be achieved by a pair involving a high-degree vertex? Let's check. If A has degree d_A > 300, then |M(A)| = 999 - d_A < 699. For non-adjacent A, B: |M(A) ∩ M(B)| = |M(A)| + |M(B)| - |M(A) ∪ M(B)| ≥ (999 - d_A) + (999 - d_B) - 1000 = 998 - d_A - d_B. If d_A = 301, d_B = 300: ≥ 998 - 601 = 397 < 398. So having higher degree vertices could actually decrease the minimum! So the adversary should indeed use 300-regular.

Wait, but that's a lower bound. The actual value could be higher. Let me reconsider. If A has degree 301, |M(A)| = 698. For non-adjacent A, B with d_B = 300, |M(B)| = 699. |M(A) ∩ M(B)| = 698 + 699 - |M(A) ∪ M(B)|. |M(A) ∪ M(B)| ≤ 1000. So |M(A) ∩ M(B)| ≥ 397. This is less than 398. So indeed, having a vertex with degree > 300 could make the minimum smaller. So the adversary should make all degrees exactly 300.

Hmm, but actually the adversary wants to MAXIMIZE the minimum. So they want to avoid having any pair with small intersection. Having a vertex with degree > 300 creates a smaller M(v), which could lead to smaller intersections. So the adversary should use 300-regular.

OK so assuming 300-regular G, the answer is:

1000 - 398 - μ = 602 - μ

where μ = max over 300-regular graphs G on 1000 vertices of min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)|.

Now I need to find μ.

Let me think about upper bounds on μ.

Fix a vertex A. A has 300 neighbors and 699 non-neighbors. For each non-neighbor B, |N_G(A) ∩ N_G(B)| ≥ μ. The common neighbors of A and B are in N_G(A) (300 vertices). Each vertex c ∈ N_G(A) can be a common neighbor of A and multiple non-neighbors B. Specifically, c is a common neighbor of A and B iff B ∈ N_G(c). The number of non-neighbors of A that c is adjacent to is (as computed earlier) 299 - |N_G(A) ∩ N_G(c)|.

So sum_{B non-adjacent to A} |N_G(A) ∩ N_G(B)| = sum_{c ∈ N_G(A)} (299 - |N_G(A) ∩ N_G(c)|) = 300 * 299 - 2 * e_A

where e_A = number of edges within N_G(A).

This sum ≥ 699 * μ (since each of the 699 terms is ≥ μ).

So 300 * 299 - 2 * e_A ≥ 699 * μ, i.e., e_A ≤ (89700 - 699μ) / 2.

Now, sum_A e_A = sum_A (edges within N_G(A)). Each edge {u, v} in G is counted in e_A for each A such that u, v ∈ N_G(A), i.e., A is a common neighbor of u and v. So sum_A e_A = sum_{edge {u,v}} |N_G(u) ∩ N_G(v)|.

For adjacent u, v: |N_G(u) ∩ N_G(v)| = (common neighbors). For the sum, we only count edges {u,v}, so we need |N_G(u) ∩ N_G(v)| for adjacent pairs.

Hmm, let me denote for adjacent u, v: c(u,v) = |N_G(u) ∩ N_G(v)|. Then sum_A e_A = sum_{edges {u,v}} c(u,v).

Also, sum_{edges {u,v}} c(u,v) = sum_{edges {u,v}} |N_G(u) ∩ N_G(v)| = sum_w (number of edges among N_G(w)) = sum_w e_w.

So sum_A e_A = sum_w e_w. That's a tautology. Not helpful directly.

Let me try another approach. Let's bound sum_A e_A from below.

sum_A e_A = sum_w e_w. We want a lower bound. e_w = number of edges within N_G(w). By convexity or other means...

Actually, let me think about the total number of "triangles" or "paths" differently.

sum_A e_A = sum_A (edges in N_G(A)) = number of (A, {u,v}) where {u,v} is an edge and u, v ∈ N_G(A) = number of triangles * 3 + number of "cherries" ... no. Actually, (A, {u,v}) where u, v ∈ N_G(A) and {u,v} is an edge: this is a triangle (A, u, v) if {A,u}, {A,v}, {u,v} are all edges. Since u, v ∈ N_G(A), {A,u} and {A,v} are edges. And {u,v} is an edge. So this is a triangle. Each triangle is counted 3 times (once for each vertex as A). So sum_A e_A = 3 * T where T is the number of triangles.

So e_A = (number of triangles containing A) and sum_A e_A = 3T.

Now, from the constraint e_A ≤ (89700 - 699μ)/2 for all A, we get sum_A e_A ≤ 1000 * (89700 - 699μ)/2 = 500 * (89700 - 699μ) = 44850000 - 349500μ.

So 3T ≤ 44850000 - 349500μ, i.e., T ≤ (44850000 - 349500μ)/3.

But we also need a lower bound on T (or sum e_A) to get an upper bound on μ.

Hmm, is there a lower bound on the number of triangles in a 300-regular graph on 1000 vertices? Not necessarily; the graph could be triangle-free (e.g., bipartite). A 300-regular bipartite graph on 1000 vertices exists (e.g., K_{300, 700} is not regular, but a 300-regular bipartite graph on 500+500 vertices exists). Wait, 300-regular bipartite graph needs each part to have at least 300 vertices. 500 + 500 = 1000, and a 300-regular bipartite graph on 500+500 exists. In this case, T = 0, e_A = 0 for all A.

With e_A = 0: 89700 - 0 ≥ 699μ, so μ ≤ 89700/699 ≈ 128.3. So μ ≤ 128.

But can we achieve μ = 128 with a triangle-free 300-regular graph? In a bipartite 300-regular graph on 500+500, for non-adjacent A, B in the same part: N_G(A) and N_G(B) are both subsets of the other part (size 500). |N_G(A) ∩ N_G(B)| = |N_G(A)| + |N_G(B)| - |N_G(A) ∪ N_G(B)| = 300 + 300 - |N_G(A) ∪ N_G(B)|. Since N_G(A) ∪ N_G(B) ⊆ other part (size 500), |union| ≤ 500. So |intersection| ≥ 100. And |intersection| ≤ 300.

For the minimum to be μ, we need min |N_G(A) ∩ N_G(B)| = μ for non-adjacent pairs. In a bipartite graph, non-adjacent pairs include pairs in the same part and pairs in different parts that are not connected.

For A, B in different parts, non-adjacent: N_G(A) ⊆ part_B, N_G(B) ⊆ part_A. These are in different parts, so N_G(A) ∩ N_G(B) = ∅. So |N_G(A) ∩ N_G(B)| = 0!

So in a bipartite graph, μ = 0 (cross-part non-adjacent pairs have 0 common neighbors). That's terrible.

So bipartite graphs give μ = 0, and the answer would be 602 - 0 = 602. But wait, is 602 achievable? Let me check: with a 300-regular bipartite graph on 500+500, the answer is 1000 - 398 - 0 = 602. But we need to verify that the minimum of |M(A) ∩ M(B)| is indeed 398.

For cross-part non-adjacent A, B: |N_G(A) ∩ N_G(B)| = 0, so |M(A) ∩ M(B)| = 398 + 0 = 398. V = 1000 - 398 = 602.

For same-part non-adjacent A, B: |N_G(A) ∩ N_G(B)| ≥ 100, so |M(A) ∩ M(B)| ≥ 498. V ≤ 502.

For adjacent A, B: |M(A) ∩ M(B)| = 400 + |N_G(A) ∩ N_G(B)|. In bipartite graph, adjacent A, B have N_G(A) ⊆ part_B, N_G(B) ⊆ part_A, so N_G(A) ∩ N_G(B) = ∅. |M(A) ∩ M(B)| = 400. V = 600.

So the minimum |M(A) ∩ M(B)| = 398 (from cross-part non-adjacent pairs), giving max V = 602.

Wait, but adjacent pairs give |M(A) ∩ M(B)| = 400, V = 600. Cross-part non-adjacent give 398, V = 602. Same-part non-adjacent give ≥ 498, V ≤ 502.

So max_{A,B} V = 602 (from cross-part non-adjacent pairs).

But can the adversary do better? Can they find a graph where min_{A,B} |M(A) ∩ M(B)| > 398?

The adversary wants to avoid having any pair with |N_G(A) ∩ N_G(B)| = 0 (for non-adjacent pairs) or small common neighborhoods. In the bipartite case, cross-part non-adjacent pairs have 0 common neighbors, which is the worst.

To avoid this, the adversary needs the graph to not be bipartite, and more generally, to have the property that every pair of non-adjacent vertices has a common neighbor. This is the "diameter 2" property (for the non-adjacent pairs).

But even with diameter 2, the common neighborhood could be just 1, giving |M(A) ∩ M(B)| = 399, V = 601. The adversary wants to maximize the minimum common neighborhood.

So the question is: what is the maximum μ such that there's a 300-regular graph on 1000 vertices where every non-adjacent pair has ≥ μ common neighbors?

And the answer to the original problem is 602 - μ.

Now I need to find μ. Let me think about upper bounds.

From the earlier analysis: for any vertex A, sum_{B non-adj to A} |N_G(A) ∩ N_G(B)| = 89700 - 2*e_A. With 699 non-neighbors, the average is (89700 - 2*e_A)/699. For the minimum to be ≥ μ, we need this average ≥ μ, so 89700 - 2*e_A ≥ 699μ, i.e., e_A ≤ (89700 - 699μ)/2.

Also, e_A ≥ 0, so μ ≤ 89700/699 ≈ 128.3, so μ ≤ 128.

But this is just from one vertex. Can we get a better bound?

Let me think about summing over all vertices. sum_A (89700 - 2*e_A) = 1000 * 89700 - 2 * 3T = 89700000 - 6T. This should be ≥ 1000 * 699 * μ = 699000μ. So 89700000 - 6T ≥ 699000μ, i.e., T ≤ (89700000 - 699000μ)/6 = 14950000 - 116500μ.

We need T ≥ 0, so μ ≤ 14950000/116500 ≈ 128.3. Same bound.

But we might get a better bound by considering the structure more carefully. Let me think about whether μ = 128 is achievable.

Hmm, actually, let me reconsider. The bound μ ≤ 128 comes from e_A ≥ 0. But can we have e_A = 0 for all A (triangle-free) and still have μ = 128?

If e_A = 0 for all A (triangle-free), then for each A, the average common neighborhood with non-neighbors is 89700/699 ≈ 128.3. For the minimum to be 128, we need all 699 non-neighbors to have common neighborhood ≥ 128, with the average being 128.3. So most would be 128 or 129. This seems very tight.

But we also need the graph to be triangle-free AND have every non-adjacent pair with ≥ 128 common neighbors. In a triangle-free graph, if A, B are non-adjacent with common neighbor c, then c is adjacent to both A and B, but A, B are not adjacent (good, no triangle). But N_G(A) and N_G(B) can share many vertices without forming triangles (since A, B are non-adjacent).

Wait, but if c, d are both common neighbors of A, B, and c, d are adjacent, then {A, c, d} might form a triangle if A is adjacent to both c and d (which it is, since c, d ∈ N_G(A)). So if c, d ∈ N_G(A) and {c,d} is an edge, that's a triangle. So in a triangle-free graph, N_G(A) is an independent set for every A. This means e_A = 0 for all A, which is consistent.

So in a triangle-free 300-regular graph, N_G(A) is an independent set of size 300 for every A. This is a strong condition. Such graphs exist (bipartite graphs are triangle-free, but as we saw, bipartite graphs have μ = 0). Are there non-bipartite triangle-free 300-regular graphs on 1000 vertices?

A triangle-free graph that's not bipartite must contain an odd cycle of length ≥ 5. But the key question is whether we can have a triangle-free 300-regular graph on 1000 vertices with μ = 128.

Hmm, this is getting very complicated. Let me step back and think about whether the answer might just be 602.

Actually, let me reconsider the problem. The bipartite construction gives max V = 602. Can the adversary do better, i.e., achieve max V < 602?

For the adversary to do better, they need min_{A,B} |M(A) ∩ M(B)| > 398. This requires for every non-adjacent pair A, B: |N_G(A) ∩ N_G(B)| ≥ 1 (at least), and more generally, they want to maximize the minimum.

But maybe the adversary can't do better than 398, and the answer is 602.

Let me think about whether there's a graph where min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)| ≥ 1, i.e., every non-adjacent pair has a common neighbor. This is equivalent to the graph having diameter ≤ 2 (for non-adjacent pairs, distance exactly 2). 

A 300-regular graph on 1000 vertices with diameter 2: the Moore bound for diameter 2 and degree 300 is 1 + 300 + 300*299 = 1 + 300 + 89700 = 90001. Since 1000 << 90001, such graphs certainly exist. In fact, a random 300-regular graph on 1000 vertices will have diameter 2 w.h.p.

In such a graph, μ ≥ 1, so the answer would be ≤ 601. But can the adversary achieve μ much larger?

Let me think about the trade-off. The adversary wants to maximize μ = min_{non-adjacent} |N_G(A) ∩ N_G(B)|. 

From the constraint e_A ≤ (89700 - 699μ)/2, to have large μ, we need small e_A (few edges within neighborhoods, i.e., few triangles). But we also need the graph to be well-connected so that non-adjacent pairs have many common neighbors.

There's a tension: to have many common neighbors for non-adjacent pairs, the graph should be "expander-like", but to have few triangles, the graph should be "bipartite-like". 

Let me think about a specific construction. Consider a graph G that's the union of two copies of K_{500} (two cliques of size 500), but with some edges removed to make it 300-regular. In K_{500}, each vertex has degree 499. To make it 300-regular, remove 199 edges per vertex. But this is within each clique, so the graph is disconnected (two components). Non-adjacent pairs in different components have 0 common neighbors. μ = 0. Bad.

What about a graph that's "almost" a clique? Like a 300-regular graph that's very dense in terms of common neighborhoods but has few triangles?

Hmm, let me think about this more carefully using the following approach:

For a 300-regular graph G on 1000 vertices, the number of non-adjacent pairs is 349500. The total common neighborhood over non-adjacent pairs is:

sum_{non-adj A,B} |N_G(A) ∩ N_G(B)| = sum_v C(deg(v), 2) - sum_{adj A,B} |N_G(A) ∩ N_G(B)|
= 1000 * C(300,2) - sum_{adj A,B} |N_G(A) ∩ N_G(B)|
= 44850000 - sum_{adj A,B} |N_G(A) ∩ N_G(B)|.

Now, sum_{adj A,B} |N_G(A) ∩ N_G(B)| = 3T (each triangle contributes 1 to the common neighborhood of each of its 3 edges). Wait, for an edge {A,B}, |N_G(A) ∩ N_G(B)| counts common neighbors, which are vertices adjacent to both A and B. Each triangle (A, B, C) where {A,B}, {B,C}, {A,C} are edges contributes C to |N_G(A) ∩ N_G(B)|. So sum over edges of |N_G(A) ∩ N_G(B)| = 3T (each triangle counted 3 times, once for each edge).

So sum_{non-adj A,B} |N_G(A) ∩ N_G(B)| = 44850000 - 3T.

Average over non-adjacent pairs = (44850000 - 3T) / 349500.

For the minimum to be ≥ μ, we need the average ≥ μ:
(44850000 - 3T) / 349500 ≥ μ
44850000 - 3T ≥ 349500μ
T ≤ (44850000 - 349500μ) / 3 = 14950000 - 116500μ.

Since T ≥ 0: μ ≤ 14950000 / 116500 ≈ 128.3. Same bound as before.

But we can also get a lower bound on T. By the Kruskal-Katona theorem or just by the fact that a 300-regular graph on 1000 vertices must have some triangles... actually, it doesn't. A bipartite 300-regular graph has T = 0.

But if we want μ ≥ 1 (every non-adjacent pair has a common neighbor), can we have T = 0? A triangle-free graph with diameter 2: this is possible (e.g., the Petersen graph is triangle-free with diameter 2, but it's small). For 300-regular on 1000 vertices, a triangle-free diameter-2 graph: the Moore bound for triangle-free diameter-2 is 1 + d + d(d-1) = 1 + 300 + 300*299 = 90001 (this is the same as the Moore bound, since triangle-free means no edges among neighbors). Wait, the Moore bound for diameter 2 is 1 + d + d(d-1) = d^2 + 1. For d = 300, that's 90001. So a triangle-free 300-regular graph with diameter 2 can have up to 90001 vertices. Since 1000 < 90001, such a graph could exist.

But does a triangle-free 300-regular graph on 1000 vertices with diameter 2 exist? It's not guaranteed. The existence of Moore graphs (achieving the bound) is rare, but we don't need to achieve the bound; we just need 1000 vertices.

A bipartite graph is triangle-free but has diameter > 2 (cross-part non-adjacent pairs have no common neighbor). A non-bipartite triangle-free graph with diameter 2 would work. 

Consider a graph based on a finite geometry or algebraic construction. For example, a polarity graph of a projective plane. But let me think about simpler constructions.

Actually, let me think about this problem differently. Let me consider the complement graph H (699-regular on 1000 vertices) and think about what structure maximizes min |N_H(A) ∩ N_H(B)|.

We showed min |N_H(A) ∩ N_H(B)| = 398 + μ where μ = min_{non-adj in G} |N_G(A) ∩ N_G(B)|.

The answer is 1000 - 398 - μ = 602 - μ.

So I need to find the maximum μ. Let me think about whether μ can be large.

Consider a strongly regular graph. A strongly regular graph with parameters (n, d, λ, μ) is a d-regular graph on n vertices where adjacent pairs have λ common neighbors and non-adjacent pairs have μ common neighbors.

If G is strongly regular with parameters (1000, 300, λ, μ_srg), then μ = μ_srg. The parameters satisfy:
(n - d - 1) * μ_srg = d * (d - λ - 1)
(1000 - 300 - 1) * μ_srg = 300 * (300 - λ - 1)
699 * μ_srg = 300 * (299 - λ)
μ_srg = 300 * (299 - λ) / 699

For μ_srg to be an integer, 699 | 300 * (299 - λ). 699 = 3 * 233. 300 = 3 * 100. So 233 | 100 * (299 - λ). Since gcd(233, 100) = 1, we need 233 | (299 - λ), so 299 - λ ≡ 0 (mod 233), so λ ≡ 299 (mod 233) ≡ 66 (mod 233). Since 0 ≤ λ ≤ 299, λ = 66 or λ = 66 + 233 = 299.

If λ = 66: μ_srg = 300 * 233 / 699 = 300 * 233 / (3 * 233) = 300/3 = 100. So μ_srg = 100.

If λ = 299: μ_srg = 300 * 0 / 699 = 0. This would mean non-adjacent pairs have 0 common neighbors, which is the bipartite case (λ = 299 means the graph is a union of cliques, but with d = 300 and n = 1000, a clique of size 301... 1000/301 is not integer, so this doesn't directly work).

So a strongly regular graph with parameters (1000, 300, 66, 100) would give μ = 100. Does such a graph exist?

The eigenvalues of a strongly regular graph (1000, 300, 66, 100) can be computed. The eigenvalues are d = 300 and the roots of x^2 + (μ_srg - λ) x + (μ_srg - d) = 0, i.e., x^2 + (100 - 66) x + (100 - 300) = 0, x^2 + 34x - 200 = 0. x = (-34 ± sqrt(1156 + 800))/2 = (-34 ± sqrt(1956))/2 = (-34 ± 44.227)/2. So x1 ≈ 5.11, x2 ≈ -39.11. These are not integers, so the multiplicities might not be integers. Let me check.

For a strongly regular graph, the multiplicities are:
f = (1/2) * (n-1) - (d + (n-1)(λ-μ_srg))/(2*sqrt((λ-μ_srg)^2 + 4(d-μ_srg)))
g = (1/2) * (n-1) + (d + (n-1)(λ-μ_srg))/(2*sqrt((λ-μ_srg)^2 + 4(d-μ_srg)))

(λ - μ_srg)^2 + 4(d - μ_srg) = (66-100)^2 + 4(300-100) = 1156 + 800 = 1956.
sqrt(1956) = 2*sqrt(489) = 2*sqrt(3*163). Not a perfect square. So the eigenvalues are irrational, and the multiplicities would need to be integers, which requires the discriminant to be a perfect square. Since 1956 is not a perfect square, this strongly regular graph does not exist (for a conference graph, the discriminant not being a perfect square is OK, but then n must be specific).

Actually, for a conference graph (where the eigenvalues are not integers), the parameters must satisfy n = 2d + ... hmm, conference graphs have specific parameter relations. Let me not go down this path.

So a strongly regular graph with these exact parameters likely doesn't exist. But the question is about the maximum μ, not necessarily achieved by a strongly regular graph.

Let me think about this more carefully. The key constraint is:

For a 300-regular graph on 1000 vertices, the average common neighborhood over non-adjacent pairs is (44850000 - 3T) / 349500. For the minimum to be large, we want this average to be large, which means T should be small.

If T = 0 (triangle-free), the average is 44850000 / 349500 ≈ 128.3. So μ ≤ 128 (since min ≤ average, and μ must be an integer... well, μ doesn't have to be an integer, but the common neighborhood is an integer).

But can we achieve μ = 128 with a triangle-free graph? We need every non-adjacent pair to have ≥ 128 common neighbors, with the average being 128.3. This means almost all non-adjacent pairs have exactly 128 or 129 common neighbors.

But there's a problem: in a triangle-free graph, for any vertex A, N_G(A) is an independent set. For a non-neighbor B of A, the common neighbors of A and B are in N_G(A) (independent set) and also in N_G(B) (independent set). The common neighbors form a subset of N_G(A) that is also in N_G(B).

In a triangle-free graph, if B is a non-neighbor of A, then N_G(A) ∩ N_G(B) is a set of vertices each adjacent to both A and B. Since the graph is triangle-free, no two vertices in N_G(A) are adjacent (N_G(A) is independent), and similarly for N_G(B). But vertices in N_G(A) ∩ N_G(B) are in both N_G(A) and N_G(B), so they're adjacent to both A and B but not to each other (since they're in N_G(A) which is independent). This is fine.

But here's the issue: can a triangle-free 300-regular graph on 1000 vertices exist where every non-adjacent pair has ≥ 128 common neighbors?

Let me think about the constraints. For vertex A with 300 neighbors (independent set) and 699 non-neighbors. Each non-neighbor B shares ≥ 128 neighbors with A. The 300 neighbors of A are shared among 699 non-neighbors, with each neighbor c being shared with (299 - |N_G(A) ∩ N_G(c)|) non-neighbors. Since the graph is triangle-free, |N_G(A) ∩ N_G(c)| = 0 for c ∈ N_G(A) (because N_G(A) is independent, so c has no neighbors in N_G(A) except... wait, c ∈ N_G(A), and N_G(A) is independent, so c has no neighbors in N_G(A) \ {c}. But c could be adjacent to vertices in N_G(A). No—N_G(A) is independent means no edges within N_G(A). So c has 0 neighbors in N_G(A). So |N_G(A) ∩ N_G(c)| = 0 (since N_G(A) ∩ N_G(c) ⊆ N_G(A), and c has no neighbors in N_G(A), so the intersection is empty). Wait, N_G(A) ∩ N_G(c) = vertices adjacent to both A and c. These vertices are in N_G(A) (adjacent to A) and in N_G(c) (adjacent to c). Since N_G(A) is independent, no vertex in N_G(A) is adjacent to c (which is also in N_G(A)). So N_G(A) ∩ N_G(c) = ∅. So |N_G(A) ∩ N_G(c)| = 0.

So each neighbor c of A is a common neighbor of A and exactly 299 non-neighbors of A (since 299 - 0 = 299). Total: 300 * 299 = 89700. With 699 non-neighbors, average = 89700/699 ≈ 128.3. ✓

For the minimum to be 128, we need each non-neighbor to have at least 128 common neighbors with A, and the total is 89700 = 128 * 699 + 228 = 89700 - 89472 = 228. So 228 non-neighbors have 129 common neighbors and 699 - 228 = 471 have 128. Or some other distribution summing to 89700 with each ≥ 128.

This seems feasible in principle. But does such a graph exist?

This is related to the concept of a "Moore graph" or "near-Moore graph" for diameter 2. A Moore graph with diameter 2 and degree d has n = d^2 + 1 vertices, and every non-adjacent pair has exactly 1 common neighbor. That's the opposite of what we want (we want many common neighbors, not few).

Actually, I think I'm overcomplicating this. Let me reconsider.

We want to maximize μ = min_{non-adjacent} |N_G(A) ∩ N_G(B)|. The constraint is μ ≤ 128 (from the averaging argument with T = 0). But is μ = 128 actually achievable?

Let me think about a specific construction. Consider a graph G on 1000 vertices that's triangle-free and 300-regular, where non-adjacent pairs have many common neighbors.

One approach: take a bipartite graph and add some edges within parts to create common neighbors for cross-part non-adjacent pairs, while maintaining triangle-freeness.

Actually, in a bipartite graph with parts X (500) and Y (500), cross-part non-adjacent pairs (A ∈ X, B ∈ Y, not adjacent) have 0 common neighbors (since N_G(A) ⊆ Y and N_G(B) ⊆ X, disjoint). To fix this, we'd need to add edges within parts, but that creates triangles (if A ∈ X is adjacent to C ∈ X, and both are adjacent to some D ∈ Y, then {A, C, D} is a triangle).

Hmm, so adding edges within parts in a bipartite graph creates triangles. To maintain triangle-freeness, we'd need to ensure that no two adjacent vertices within a part share a neighbor in the other part. This is very restrictive.

Let me think about non-bipartite triangle-free graphs. The Clebsch graph, Petersen graph, etc. are small. For larger graphs, we can use algebraic constructions.

Actually, let me think about this problem from a completely different angle. Maybe the answer is simply 602, achieved by the bipartite construction, and no graph can do better.

Wait, but I showed that if the graph has diameter 2 (every non-adjacent pair has ≥ 1 common neighbor), then μ ≥ 1 and the answer is ≤ 601. So the bipartite construction is NOT optimal for the adversary!

The adversary can do better than the bipartite construction by using a graph with diameter 2. So the answer is less than 602.

Let me reconsider. The adversary wants to minimize max_{A,B} V = 1000 - min_{A,B} |M(A) ∩ M(B)| = 1000 - (398 + μ) = 602 - μ. So the adversary wants to maximize μ.

The question is: what is the maximum μ over all graphs G with min degree ≥ 300 on 1000 vertices?

We've established μ ≤ 128 (from the triangle-free bound, but actually this bound applies to all graphs, not just triangle-free ones—let me recheck).

From the averaging argument: for any 300-regular graph, average common neighborhood over non-adjacent pairs = (44850000 - 3T) / 349500. Since T ≥ 0, this is ≤ 44850000 / 349500 ≈ 128.3. So μ ≤ 128.

But can μ = 128 be achieved? This requires T = 0 (triangle-free) and a very uniform distribution of common neighborhoods.

Actually, wait. Let me reconsider whether the graph needs to be 300-regular. The adversary wants to maximize μ = min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)|. If the graph is not regular, some vertices have higher degree, which means more common neighbors on average but also the formula changes.

Let me reconsider. If G has min degree ≥ 300 but is not regular, the formula for |M(A) ∩ M(B)| changes. Let me redo the analysis for non-regular graphs.

For non-adjacent A, B: |M(A) ∩ M(B)| = |M(A)| + |M(B)| - |M(A) ∪ M(B)|. |M(A)| = 999 - deg(A), |M(B)| = 999 - deg(B). |M(A) ∪ M(B)| ≤ 1000. So |M(A) ∩ M(B)| ≥ 999 - deg(A) + 999 - deg(B) - 1000 = 998 - deg(A) - deg(B).

If deg(A) = deg(B) = 300: ≥ 398.
If deg(A) = 301, deg(B) = 300: ≥ 397.

So having higher degree vertices decreases the lower bound. The adversary wants to maximize the minimum, so they should use 300-regular.

But wait, the actual value of |M(A) ∩ M(B)| could be higher than the lower bound. The lower bound is 998 - deg(A) - deg(B), but the actual value is 998 - deg(A) - deg(B) + |N_G(A) ∩ N_G(B)| (for non-adjacent A, B). So:

|M(A) ∩ M(B)| = (998 - deg(A) - deg(B)) + |N_G(A) ∩ N_G(B)|

for non-adjacent A, B. (Let me verify: |M(A) ∩ M(B)| = |M(A)| + |M(B)| - |M(A) ∪ M(B)| = (999 - d_A) + (999 - d_B) - (1000 - |N_G(A) ∩ N_G(B)|) = 998 - d_A - d_B + |N_G(A) ∩ N_G(B)|. ✓)

For adjacent A, B: |M(A) ∩ M(B)| = (999 - d_A) + (999 - d_B) - (1000 - |N_G(A) ∩ N_G(B)| - 2) = 1000 - d_A - d_B + |N_G(A) ∩ N_G(B)|.

So for non-adjacent: |M(A) ∩ M(B)| = 998 - d_A - d_B + cn(A,B) where cn(A,B) = |N_G(A) ∩ N_G(B)|.
For adjacent: |M(A) ∩ M(B)| = 1000 - d_A - d_B + cn(A,B).

If the graph is 300-regular: non-adjacent: 398 + cn. Adjacent: 400 + cn. The minimum is from non-adjacent pairs: 398 + min_{non-adj} cn = 398 + μ.

If the graph is not regular, say some vertex has degree 301: for a non-adjacent pair (A, B) with d_A = 301, d_B = 300: |M(A) ∩ M(B)| = 397 + cn(A,B). Even if cn(A,B) is large, the base is 397, which is less than 398. So the minimum could be lower.

But cn(A,B) could be larger for higher-degree vertices. If d_A = 301, A has more neighbors, so potentially more common neighbors with B. The question is whether the increase in cn compensates for the decrease in the base.

For a non-adjacent pair (A, B) with d_A = 301, d_B = 300: cn(A,B) ≤ min(d_A, d_B) = 300. So |M(A) ∩ M(B)| ≤ 397 + 300 = 697. And ≥ 397 + 0 = 397. 

For a 300-regular graph, the minimum is 398 + μ. For a graph with some degree-301 vertices, the minimum could be as low as 397 + cn for those pairs. If cn is at least μ + 1 for those pairs, then the minimum is still ≥ 398 + μ. But this requires the higher-degree vertices to have more common neighbors, which might not hold.

I think for simplicity, the adversary should use 300-regular, and the answer is 602 - μ where μ is the maximum min-common-neighborhood for non-adjacent pairs in a 300-regular graph on 1000 vertices.

Now, let me think about whether μ = 128 is achievable. This is the key question.

Actually, let me reconsider the upper bound. I showed μ ≤ 128 using the average over non-adjacent pairs, assuming T = 0. But if T > 0, the bound is even lower. So μ ≤ 128 regardless.

But is μ = 128 achievable? This requires a triangle-free 300-regular graph on 1000 vertices where every non-adjacent pair has ≥ 128 common neighbors.

In such a graph, for each vertex A, the 699 non-neighbors have common neighborhoods summing to 89700, with each ≥ 128. 128 * 699 = 89472, and 89700 - 89472 = 228. So the "excess" is 228, meaning 228 non-neighbors have 129 common neighbors and 471 have 128 (or some other distribution).

This is a very tight constraint. The graph would need to be almost like a "perfect" structure.

Let me think about whether such a graph can exist. Consider the adjacency matrix approach. In a triangle-free d-regular graph, for non-adjacent A, B, cn(A,B) = (A^2)_{A,B} where A is the adjacency matrix. (A^2)_{A,B} = number of walks of length 2 from A to B = cn(A,B) for A ≠ B (since triangle-free means no edge A-B, so all length-2 walks go through common neighbors). For adjacent A, B, (A^2)_{A,B} = cn(A,B) as well, but in a triangle-free graph, cn(A,B) = 0 for adjacent pairs (since a common neighbor would form a triangle).

So in a triangle-free 300-regular graph: A^2 has diagonal entries = 300 (degree), off-diagonal entries = cn(A,B) for non-adjacent pairs and 0 for adjacent pairs. So A^2 = 300I + (matrix of cn values on non-edges).

The eigenvalues of A are 300 (trivial), and others. A^2 has eigenvalue 300^2 = 90000 for the trivial eigenvector, and for other eigenvectors, eigenvalue = (eigenvalue of A)^2.

This is getting quite involved. Let me try a different approach and think about specific constructions.

Construction: Let G be a 300-regular graph on 1000 vertices that's a "blow-up" or algebraic construction.

Consider the following: take Z_1000 (cyclic group of order 1000). Connect vertex i to vertices i ± 1, i ± 2, ..., i ± 150 (a circulant graph). This gives degree 300. Is it triangle-free? No, since i is connected to i+1 and i+2, and i+1 is connected to i+2 (if 1 is in the connection set). So there are triangles.

For a triangle-free circulant graph, we need the connection set S (with S = -S, |S| = 300) to be "sum-free" in the sense that there's no solution to a + b = c with a, b, c ∈ S (mod 1000). This is a Sidon set or sum-free set condition. A sum-free set in Z_1000 of size 300... by the theory of sum-free sets, the maximum size of a sum-free set in Z_n is about n/3. For n = 1000, that's about 333. So a sum-free set of size 150 (giving degree 300 with S = -S) might be possible. But I'm not sure about the common neighborhood properties.

This is getting very complicated. Let me try to think about the problem from a higher level and see if there's a cleaner argument.

Actually, let me reconsider the problem statement. "What is the minimum possible value of the maximum number of participants max_{A,B} V that the city can guarantee for some choice of candidates A and B?"

I interpreted this as: min over graphs G (min degree ≥ 300) of max over A,B of V(G, A, B). The city chooses the graph to minimize the best-case participation.

But maybe the interpretation is different. Let me re-read: "the minimum possible value of the maximum number of participants max_{A,B} V that the city can guarantee for some choice of candidates A and B."

Hmm, "that the city can guarantee for some choice of candidates A and B" — this means the city can guarantee that there EXISTS a choice of A, B with V ≥ (some value). The city wants to guarantee a high value. The "minimum possible value" is over all possible acquaintance structures.

So: min_G max_{A,B} V(G, A, B) where G has min degree ≥ 300 on 1000 vertices. This is what I had.

OK so let me think about this more carefully. Let me consider the possibility that the answer is 600.

If the answer is 600, then the adversary can achieve max V = 600, meaning min |M(A) ∩ M(B)| = 400. For 300-regular G, this means 398 + μ = 400, so μ = 2. Every non-adjacent pair has ≥ 2 common neighbors.

But we showed μ can be up to 128 (in principle). So if μ = 128 is achievable, the answer would be 602 - 128 = 474. That seems too low.

Hmm wait, let me re-examine. If μ = 128, then min |M(A) ∩ M(B)| = 398 + 128 = 526, and max V = 1000 - 526 = 474. The adversary would achieve max V = 474, which is much better (lower) than 602.

But is μ = 128 achievable? Let me think about this more carefully.

Actually, I realize I should think about whether a triangle-free 300-regular graph on 1000 vertices with μ = 128 can exist. The key constraint is that for every vertex A, the 300 neighbors of A form an independent set, and the 699 non-neighbors each share 128 or 129 neighbors with A.

Let me think about the bipartite case more carefully. In a 300-regular bipartite graph on 500+500, for same-part non-adjacent pairs, cn(A,B) = |N_G(A) ∩ N_G(B)| where both neighborhoods are in the other part (size 500). cn(A,B) = 300 + 300 - |N_G(A) ∪ N_G(B)| ≥ 600 - 500 = 100. So μ_same ≥ 100 for same-part pairs. But μ_cross = 0 for cross-part non-adjacent pairs. So overall μ = 0.

To fix the cross-part issue, we need a non-bipartite graph. But non-bipartite triangle-free graphs have odd cycles, which might reduce the common neighborhood for some pairs.

Let me think about a different construction. Consider a graph on 1000 vertices partitioned into groups, with a structured connection pattern.

Actually, let me think about the problem from the perspective of the complement graph H. H is 699-regular on 1000 vertices. We want to maximize min_{A≠B} |N_H(A) ∩ N_H(B)|.

For adjacent A, B in H: |N_H(A) ∩ N_H(B)| = 1398 - |N_H(A) ∪ N_H(B)|. Since A ∈ N_H(B) and B ∈ N_H(A), |N_H(A) ∪ N_H(B)| ≤ 1000. So ≥ 398.

For non-adjacent A, B in H: |N_H(A) ∪ N_H(B)| ≤ 998. So |N_H(A) ∩ N_H(B)| ≥ 400.

The minimum is from adjacent pairs in H (non-adjacent in G). We want to maximize this minimum, i.e., make |N_H(A) ∪ N_H(B)| as small as possible for all adjacent pairs.

|N_H(A) ∪ N_H(B)| = 1000 - |{v : v ∉ N_H(A), v ∉ N_H(B)}| = 1000 - |{v : v ∈ M(A) ∩ M(B) in terms of H}|... wait, I need to be careful. In H, the "non-neighbors" of A (excluding A) are the neighbors of A in G. So {v : v ∉ N_H(A), v ≠ A} = N_G(A) ∪ {A}... no. {v ≠ A : v ∉ N_H(A)} = {v ≠ A : v is not a neighbor of A in H} = {v ≠ A : v is a neighbor of A in G or v = A}... hmm, v ≠ A, so {v ≠ A : v ∉ N_H(A)} = N_G(A) (since the complement of N_H(A) in V \ {A} is N_G(A)).

So {v : v ∉ N_H(A) and v ∉ N_H(B)} = (V \ ({A} ∪ N_H(A))) ∩ (V \ ({B} ∪ N_H(B))) = (N_G(A) ∪ {A}) ∩ ... wait, V \ ({A} ∪ N_H(A)) = {A} ∪ N_G(A)? No. V = {A} ∪ N_H(A) ∪ N_G(A) (where N_G(A) are the neighbors of A in G, which are the non-neighbors of A in H, excluding A). Wait, V \ ({A} ∪ N_H(A)) = N_G(A). Because V = {A} ∪ N_H(A) ∪ N_G(A) (partition: A itself, H-neighbors, G-neighbors). So V \ ({A} ∪ N_H(A)) = N_G(A).

Similarly, V \ ({B} ∪ N_H(B)) = N_G(B).

So {v : v ∉ N_H(A) and v ∉ N_H(B)} = N_G(A) ∩ N_G(B) \ ... hmm, we need v ∉ N_H(A) and v ∉ N_H(B). v ∉ N_H(A) means v ∈ V \ N_H(A) = {A} ∪ N_G(A). v ∉ N_H(B) means v ∈ {B} ∪ N_G(B). So v ∈ ({A} ∪ N_G(A)) ∩ ({B} ∪ N_G(B)).

If A, B are adjacent in H (non-adjacent in G): A ∉ N_G(B), B ∉ N_G(A). So ({A} ∪ N_G(A)) ∩ ({B} ∪ N_G(B)) = (N_G(A) ∩ N_G(B)) ∪ (N_G(A) ∩ {B}) ∪ ({A} ∩ N_G(B)) ∪ ({A} ∩ {B}). N_G(A) ∩ {B} = ∅ (B ∉ N_G(A)). {A} ∩ N_G(B) = ∅ (A ∉ N_G(B)). {A} ∩ {B} = ∅. So = N_G(A) ∩ N_G(B).

So |{v : v ∉ N_H(A) and v ∉ N_H(B)}| = |N_G(A) ∩ N_G(B)| = cn_G(A,B) (common neighbors in G for non-adjacent A, B in G).

|N_H(A) ∪ N_H(B)| = 1000 - cn_G(A,B).

|N_H(A) ∩ N_H(B)| = 1398 - (1000 - cn_G(A,B)) = 398 + cn_G(A,B). ✓ (consistent with before).

So to maximize min |N_H(A) ∩ N_H(B)|, we maximize min over edges in H of (398 + cn_G(A,B)), i.e., maximize min over non-edges in G of cn_G(A,B) = μ.

And the answer is 1000 - (398 + μ) = 602 - μ.

Now, the key question: what is the maximum μ?

Let me think about this more carefully with a focus on finding the exact value.

Upper bound: μ ≤ 128 (from the averaging argument, achieved when T = 0).

But is this tight? Let me think about whether a triangle-free 300-regular graph on 1000 vertices with μ = 128 exists.

Actually, I realize that the bound μ ≤ 128 might not be tight. Let me think about additional constraints.

In a triangle-free 300-regular graph, for each vertex A, N_G(A) is an        — AI历史解题过程（thinking）
#   polymath_00163         — 题目ID

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
  <problem_id>polymath_00163</problem_id>
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

In a city with $n = 1000$ residents, each resident has at least $k = 300$ acquaintances. A resident will participate in an election if at least one of their acquaintances is a candidate. Two residents, $A$ and $B$, are chosen as candidates for a mayoral election. Let $V$ be the number of residents who participate in the election. What is the minimum possible value of the maximum number of participants $\max_{A, B} V$ that the city can guarantee for some choice of candidates $A$ and $B$?

## Standard Solution

Following the first solution, we choose an arbitrary resident $A$ as the first candidate. Let $k_A$ be the number of acquaintances of $A$. By the problem statement, $k_A \ge 0.3n$. Let $S$ be the set of residents not acquainted with $A$, so $|S| = n - k_A$. According to the lemma derived in the solution, there exists a resident $B$ who is acquainted with at least $30\%$ of the residents in $S$. The number of participants is the union of the acquaintances of $A$ and $B$. Thus, the number of participants $V \ge k_A + 0.3(n - k_A) = 0.7k_A + 0.3n$. Substituting $k_A \ge 0.3n$ gives $V \ge 0.7(0.3n) + 0.3n = 0.21n + 0.3n = 0.51n$. For $n = 1000$, $0.51 \times 1000 = 510$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a city with n=1000 residents. Each resident has at least k=300 acquaintances. A resident participates in an election if at least one of their acquaintances is a candidate. Two residents A and B are chosen as candidates. V is the number of residents who participate.

We want to find: the minimum possible value of max_{A,B} V that the city can guarantee for some choice of candidates A and B.

Let me parse this carefully. The city has a graph structure (acquaintance graph) on 1000 vertices, each vertex has degree at least 300. The city gets to choose the graph (subject to min degree 300), and then we want to guarantee that for SOME choice of candidates A, B, the number of participants V is large. Actually wait, let me re-read.

"What is the minimum possible value of the maximum number of participants max_{A,B} V that the city can guarantee for some choice of candidates A and B?"

So the question is: over all possible acquaintance graphs G with min degree ≥ 300 on 1000 vertices, what is the minimum of max_{A,B} V(G, A, B)?

In other words, the adversary (city) chooses a graph with min degree 300 to minimize the maximum participation. Then we (the candidate chooser) pick A, B to maximize V. The value is min_G max_{A,B} V.

A resident participates if at least one of A or B is their acquaintance. So V = |N(A) ∪ N(B)| where N(X) is the set of acquaintances of X. Note: does A participate? A's acquaintances include B (maybe). Actually, does a resident count themselves? Let me think. A resident participates if at least one of their acquaintances is a candidate. So if A is a candidate, A participates if A has an acquaintance who is a candidate, i.e., if B is an acquaintance of A (or A is an acquaintance of A, but no self-loops). So A participates iff A and B are acquaintances, or more precisely iff A has some acquaintance among {A, B} = iff B ∈ N(A) (since A ∉ N(A)).

Actually, V = number of residents r such that N(r) ∩ {A, B} ≠ ∅ = |{r : A ∈ N(r) or B ∈ N(r)}| = |N(A) ∪ N(B)| where N(A) = {r : A ∈ N(r)} is the set of neighbors of A (the open neighborhood). Since the graph is undirected, N(A) = neighbors of A.

So V = |N(A) ∪ N(B)| = deg(A) + deg(B) - |N(A) ∩ N(B)|.

We want to maximize this over A, B. The adversary wants to minimize this maximum.

To minimize max_{A,B} |N(A) ∪ N(B)|, the adversary wants all neighborhoods to be small (but min degree 300) and to overlap a lot.

The minimum degree is 300, so deg(A) ≥ 300 for all A. So |N(A) ∪ N(B)| ≥ 300 (just from one). But we can do better by choosing A, B with large degree and small overlap.

The adversary wants to make the graph such that for every pair A, B, |N(A) ∪ N(B)| is small.

Let me think about what structure minimizes the maximum of |N(A) ∪ N(B)|.

If the graph is a complete bipartite graph K_{300, 700}: vertices split into parts of size 300 and 700. Each vertex in the 300-part has degree 700, each vertex in the 700-part has degree 300. Min degree = 300. ✓

For two vertices A, B both in the 700-part: N(A) = the 300-part (size 300), N(B) = the 300-part (size 300). So |N(A) ∪ N(B)| = 300.

For A in 700-part, B in 300-part: N(A) = 300-part (size 300), N(B) = 700-part (size 700). |N(A) ∪ N(B)| = 300 + 700 - |N(A) ∩ N(B)|. N(A) ∩ N(B) = (300-part ∩ 700-part) ∪ ... wait. N(A) = 300-part. N(B) = 700-part. These are disjoint parts. So |N(A) ∪ N(B)| = 300 + 700 = 1000. But wait, is B in N(B)? No. Is A in N(A)? No. So N(A) = 300-part (all 300 vertices), N(B) = 700-part (all 700 vertices). Union = all 1000 vertices. So V = 1000.

So in K_{300,700}, max_{A,B} V = 1000 (achieved by picking one from each part). That's bad for the adversary.

So the adversary wants to avoid having a pair whose neighborhoods cover everything.

Let me think differently. The adversary wants to minimize max_{A,B} |N(A) ∪ N(B)|.

Consider a graph that's a union of cliques. Say we partition 1000 vertices into cliques. If we have cliques of size 301 each (min degree 300 within clique), we can fit 3 cliques of 301 = 903, plus one of 97 (but 97 < 301, so min degree would be 96 < 300). So that doesn't work unless all parts are ≥ 301.

1000 / 301 ≈ 3.32. So we can have 3 cliques of 301 = 903, remaining 97 can't form a valid clique. So we need parts of size ≥ 301. With 3 parts: sizes could be 334, 333, 333. Each vertex has degree = part_size - 1 ≥ 332 ≥ 300. ✓

In this graph (3 disjoint cliques), for A, B in the same clique of size s: N(A) ∪ N(B) = the clique minus {A, B} if A, B adjacent (which they are in a clique), so size s - 2... wait. N(A) = clique \ {A}, N(B) = clique \ {B}. Union = clique \ (something). Actually N(A) ∪ N(B) = clique \ {A} ∪ clique \ {B} = clique (since A ∈ N(B) and B ∈ N(A)). So |N(A) ∪ N(B)| = s. Wait, A ∈ N(B) since they're in the same clique and adjacent. So A ∈ N(B) ⊆ N(A) ∪ N(B). Similarly B. So union = entire clique, size s.

For A, B in different cliques: N(A) = clique_A \ {A}, N(B) = clique_B \ {B}. These are disjoint. |N(A) ∪ N(B)| = (s_A - 1) + (s_B - 1) = s_A + s_B - 2.

With cliques of size 334, 333, 333: max is achieved by picking A, B from the two largest cliques: 334 + 333 - 2 = 665. Or from same clique: 334. So max = 665.

Can the adversary do better (lower)? Let's think about the general lower bound.

We want to prove: for any graph G on 1000 vertices with min degree ≥ 300, there exist A, B with |N(A) ∪ N(B)| ≥ some value M, and the adversary can achieve M.

Let me think about the lower bound. We want to show max_{A,B} |N(A) ∪ N(B)| ≥ M for some M, for any such graph.

|N(A) ∪ N(B)| = deg(A) + deg(B) - |N(A) ∩ N(B)|.

To make this large, pick A, B with large degree and small common neighborhood.

Hmm, let me think about an averaging argument. Consider picking A, B uniformly at random. E[|N(A) ∪ N(B)|] = E[deg(A)] + E[deg(B)] - E[|N(A) ∩ N(B)|].

E[|N(A) ∩ N(B)|] = sum over v of P(v ∈ N(A) and v ∈ N(B)) = sum_v (deg(v)/n)^2 (if A, B independent uniform, but A, B distinct... approximately). Actually P(v ∈ N(A)) = deg(v)/n. For independent A, B (with replacement), P(v ∈ N(A) ∩ N(B)) = (deg(v)/n)^2.

So E[|N(A) ∩ N(B)|] ≈ sum_v (deg(v)/n)^2 = (1/n^2) sum_v deg(v)^2.

By Cauchy-Schwarz, sum deg(v)^2 ≥ (sum deg(v))^2 / n = (2m)^2 / n.

Also sum deg(v) ≥ 300 * 1000 = 300000, so 2m ≥ 300000, m ≥ 150000.

E[deg(A)] = 2m/n ≥ 300.

This is getting complicated. Let me think about it more carefully with the specific numbers.

Actually, let me reconsider the problem. The answer might be 600.

Let me think about the lower bound more carefully.

Claim: For any graph on n=1000 vertices with min degree ≥ 300, max_{A,B} |N(A) ∪ N(B)| ≥ 600.

Proof attempt: Pick any vertex A with deg(A) ≥ 300. We want to find B such that |N(A) ∪ N(B)| ≥ 600. |N(A) ∪ N(B)| = deg(A) + deg(B) - |N(A) ∩ N(B)| ≥ 300 + 300 - |N(A) ∩ N(B)| = 600 - |N(A) ∩ N(B)|.

So we need |N(A) ∩ N(B)| to be small. If we can find B with |N(A) ∩ N(B)| = 0, we get 600. But that might not be possible.

Hmm, but we want to maximize, so we want to find B minimizing the overlap with A while having large degree.

Actually, let's think about it as: we want to find A, B maximizing deg(A) + deg(B) - |N(A) ∩ N(B)|.

Let me think about the complement. Let's consider the "non-neighborhood". For vertex v, let M(v) = V \ (N(v) ∪ {v}) = set of non-neighbors of v (excluding v itself). |M(v)| = n - 1 - deg(v) ≤ 999 - 300 = 699.

A resident r does NOT participate iff r is not a neighbor of A and not a neighbor of B, i.e., r ∈ M(A) ∩ M(B) (and r ≠ A, r ≠ B, but A ∈ M(A) is false since A ∉ N(A) but A is excluded from M(A) by definition). Actually M(A) = V \ (N(A) ∪ {A}), so A ∉ M(A). Similarly B ∉ M(B).

Non-participants = {r : r ∉ N(A) and r ∉ N(B)} = M(A) ∩ M(B) (but we need r ≠ A and r ≠ B; since A ∉ M(A), A ∉ M(A) ∩ M(B); similarly B ∉ M(A) ∩ M(B) since B ∉ M(B)). So non-participants = M(A) ∩ M(B), and V = n - |M(A) ∩ M(B)|.

So max_{A,B} V = n - min_{A,B} |M(A) ∩ M(B)| = 1000 - min_{A,B} |M(A) ∩ M(B)|.

The adversary wants to maximize min_{A,B} |M(A) ∩ M(B)|, i.e., make every pair of "non-neighborhoods" have large intersection.

|M(v)| = n - 1 - deg(v) ≤ 699. To maximize the minimum pairwise intersection of the M(v) sets, the adversary wants all M(v) to be large and similar.

If all M(v) have size exactly 699 (i.e., all degrees exactly 300), and they're all the same set of 699 vertices... but can all vertices have the same non-neighborhood? If M(v) = S for all v, where |S| = 699, then each v is non-adjacent to all of S and adjacent to all of V \ (S ∪ {v}). But v ∈ V \ S (since v ∉ M(v) = S). So V \ S has 301 vertices, and they form a clique (each adjacent to all others in V \ S). Each vertex in S is adjacent to... M(v) for v ∈ S would be S \ {v} (since v ∈ S, and v is non-adjacent to all of S \ {v}... wait, let me reconsider).

Hmm, this is getting complicated. Let me think about it as: the graph is determined by degrees and structure. Let me think about what graph maximizes min_{A,B} |M(A) ∩ M(B)|.

If all M(v) are identical sets S of size 699: For v ∈ S: M(v) should be S, but v ∉ M(v), so M(v) = S \ {v}, which has size 698, not 699. Contradiction. So they can't all be identical.

Let me think about the structure where the graph is a clique on 301 vertices plus 699 isolated... no, isolated vertices have degree 0 < 300.

OK here's another approach. Consider the complement graph H. In H, each vertex has degree ≤ 699 (since in G, degree ≥ 300, so in H, degree ≤ 999 - 300 = 699). M(v) in G = N_H(v) ∪ ... wait. M(v) = V \ (N_G(v) ∪ {v}) = N_H(v) where H is the complement graph (without self-loops). Actually in the complement graph H, N_H(v) = V \ ({v} ∪ N_G(v)) = M(v). Yes!

So |M(A) ∩ M(B)| = |N_H(A) ∩ N_H(B)|.

We want to minimize this over A, B (to maximize V). The adversary wants to maximize min_{A,B} |N_H(A) ∩ N_H(B)| where H is a graph on 1000 vertices with max degree ≤ 699.

So the problem becomes: Given a graph H on n=1000 vertices with maximum degree ≤ 699 (= n - 1 - 300 = n - k - 1), find the maximum possible value of min_{A≠B} |N_H(A) ∩ N_H(B)|, and the answer to the original problem is 1000 minus that.

Wait, but we also need A ≠ B (two distinct candidates). Let me assume A ≠ B.

So we want: max_H min_{A≠B} |N_H(A) ∩ N_H(B)| where Δ(H) ≤ 699.

Then answer = 1000 - (that max).

Let me denote d = 699 = n - k - 1. We want to find a graph H on n vertices with max degree ≤ d that maximizes the minimum common neighborhood.

Intuitively, to maximize common neighborhoods, we want H to be as "dense and uniform" as possible. If H is a complete graph on n vertices, every pair has common neighborhood n - 2, but max degree = n - 1 = 999 > 699. Not allowed.

If H is d-regular, then for each pair A, B: |N_H(A) ∩ N_H(B)| = ? In a d-regular graph, |N_H(A) ∩ N_H(B)| depends on whether A, B are adjacent.

If A, B adjacent: |N_H(A) ∩ N_H(B)| = |N_H(A)| + |N_H(B)| - |N_H(A) ∪ N_H(B)|. N_H(A) ∪ N_H(B) ⊆ V \ {A, B}... hmm, actually A ∈ N_H(B) and B ∈ N_H(A) since they're adjacent. So N_H(A) ∪ N_H(B) ⊆ V. |N_H(A) ∪ N_H(B)| = 2d - |N_H(A) ∩ N_H(B)|. Also N_H(A) ∪ N_H(B) ⊆ V, and A ∈ N_H(B) ⊆ union, B ∈ N_H(A) ⊆ union. So the union is a subset of V. The complement of the union in V has size n - |union| = n - 2d + |intersection|.

This is getting circular. Let me think about specific constructions.

Construction 1: H is a complete bipartite graph K_{699, 301}. Max degree = 699 (for vertices in the 301-part) and 301 (for vertices in the 699-part). Max degree = 699 ≤ 699. ✓

For A, B both in the 301-part: N_H(A) = 699-part, N_H(B) = 699-part. |N_H(A) ∩ N_H(B)| = 699.

For A, B both in the 699-part: N_H(A) = 301-part, N_H(B) = 301-part. |intersection| = 301.

For A in 301-part, B in 699-part: N_H(A) = 699-part, N_H(B) = 301-part. |intersection| = 0 (disjoint parts). Wait, but A ∈ 301-part and B ∈ 699-part. N_H(A) = 699-part (since A is connected to all of 699-part). N_H(B) = 301-part. These are disjoint. So |N_H(A) ∩ N_H(B)| = 0.

So min_{A≠B} |N_H(A) ∩ N_H(B)| = 0. That's terrible for the adversary.

Construction 2: H is a union of cliques. To maximize min common neighborhood, we want large cliques. With max degree 699, the largest clique has size 700. We can have one clique of 700 and need to handle the remaining 300 vertices. They need max degree ≤ 699, so they can form a clique of 300 (max degree 299 ≤ 699). 

For A, B in the 700-clique: |N_H(A) ∩ N_H(B)| = 698 (all other vertices in the clique).
For A, B in the 300-clique: |N_H(A) ∩ N_H(B)| = 298.
For A in 700-clique, B in 300-clique: N_H(A) = 700-clique \ {A}, N_H(B) = 300-clique \ {B}. Disjoint. |intersection| = 0.

min = 0. Still bad.

The problem is that for pairs in different components, the common neighborhood is 0.

So the adversary needs H to be connected (or at least have overlapping neighborhoods across all pairs).

Construction 3: H is a complete multipartite graph? Or some other structure?

Let me think about what maximizes min_{A≠B} |N_H(A) ∩ N_H(B)|.

For any two vertices A, B, |N_H(A) ∩ N_H(B)| counts common neighbors. To make this large for all pairs, we want every pair to share many neighbors.

Consider H = complete graph K_{1000} minus a perfect matching (or some regular structure). Max degree = 998. Too high.

We need max degree ≤ 699. So each vertex is missing at least 300 edges (compared to complete graph).

Idea: H is the complement of a 300-regular graph G. Then H has degree 999 - 300 = 699 for every vertex. So H is 699-regular.

In a 699-regular graph H on 1000 vertices, for adjacent A, B: |N_H(A) ∩ N_H(B)| = 699 + 699 - |N_H(A) ∪ N_H(B)|. The union N_H(A) ∪ N_H(B) includes A and B (since adjacent), so |union| ≥ 2. Actually |union| ≤ 1000. So |intersection| ≥ 699 + 699 - 1000 = 398. And for non-adjacent A, B: A ∉ N_H(B), B ∉ N_H(A), so N_H(A) ∪ N_H(B) ⊆ V \ {A, B}, |union| ≤ 998, |intersection| ≥ 699 + 699 - 998 = 400.

So in any 699-regular graph, min_{A≠B} |N_H(A) ∩ N_H(B)| ≥ 398 (for adjacent pairs). Can we achieve exactly 398?

For adjacent A, B: |N_H(A) ∩ N_H(B)| = 1398 - |N_H(A) ∪ N_H(B)|. |N_H(A) ∪ N_H(B)| ≤ 1000. So |intersection| ≥ 398. Equality when N_H(A) ∪ N_H(B) = V, i.e., every vertex is a neighbor of A or B.

For non-adjacent A, B: |intersection| ≥ 400. Equality when N_H(A) ∪ N_H(B) = V \ {A, B}.

So the minimum is at least 398 (achieved by adjacent pairs where the union of neighborhoods is everything).

Can we construct a 699-regular graph where every adjacent pair has N_H(A) ∪ N_H(B) = V? That means for every edge AB, every other vertex is adjacent to A or B. Equivalently, there's no vertex that is non-adjacent to both A and B. In terms of the complement G (300-regular), this means: for every non-edge AB in G (i.e., edge AB in H), there's no vertex adjacent to both A and B in G. I.e., no two non-adjacent vertices in G have a common neighbor. That's a very strong condition.

Hmm, this is getting complicated. Let me think about whether 398 is achievable or if the actual minimum common neighborhood can be higher.

Actually, wait. Let me reconsider. The adversary wants to MAXIMIZE min_{A≠B} |N_H(A) ∩ N_H(B)|. So the adversary wants the minimum common neighborhood to be as large as possible. We showed that in any 699-regular graph, min ≥ 398. But can the adversary do better than 398?

If the adversary uses a 699-regular graph, the minimum is at least 398, and possibly higher if the graph is structured well. But can the adversary make it higher than 398?

For adjacent pairs, the common neighborhood is 1398 - |union|, and |union| ≤ 1000, so common neighborhood ≥ 398. To make it higher, we need |union| < 1000, i.e., some vertex is non-adjacent to both A and B. But that would mean in H, some vertex c is not a neighbor of A and not a neighbor of B. Since A, B are adjacent in H, c ≠ A, B. So c is a non-neighbor of both A and B in H, meaning c is a neighbor of both A and B in G (the complement). 

To maximize the minimum, the adversary wants |union| to be as small as possible for the worst-case pair. But the adversary controls the graph, so they want to make all pairs have large common neighborhood.

Hmm, but actually the adversary wants to maximize the minimum over all pairs. So they want to construct H such that even the worst pair has large common neighborhood.

Let me think about an upper bound on what the adversary can achieve.

Upper bound on min_{A≠B} |N_H(A) ∩ N_H(B)|:

Consider any graph H with max degree ≤ 699. Pick a vertex A with degree d_A ≤ 699. For any other vertex B, |N_H(A) ∩ N_H(B)| ≤ d_A ≤ 699. That's not tight enough.

Let me think about it differently. Consider the vertex A with the smallest degree in H (largest degree in G). Actually, all degrees in H are ≤ 699, and could be less.

Hmm, let me think about a cleaner approach.

Let me reconsider. We have G with min degree ≥ 300. We want max_{A,B} |N_G(A) ∪ N_G(B)|. We showed this equals 1000 - min_{A,B} |N_H(A) ∩ N_H(B)| where H = complement of G, max degree ≤ 699.

So the answer = 1000 - max_H min_{A≠B} |N_H(A) ∩ N_H(B)|.

Let me think about what max_H min_{A≠B} |N_H(A) ∩ N_H(B)| is.

Upper bound: For any H with max degree ≤ 699, consider the pair (A, B) that are adjacent in H (if H has an edge). |N_H(A) ∩ N_H(B)| ≤ min(deg_H(A), deg_H(B)) ≤ 699. Not helpful.

Better approach: Think about a specific vertex v. How many pairs (A, B) have v as a common neighbor? v is a common neighbor of A, B iff A, B ∈ N_H(v). So the number of pairs sharing v as common neighbor is C(deg_H(v), 2). Total over all v: sum_v C(deg_H(v), 2) = sum of common neighborhoods over all pairs = sum_{A<B} |N_H(A) ∩ N_H(B)|.

By convexity, sum_v C(deg_H(v), 2) is maximized when degrees are as unequal as possible, but we have max degree ≤ 699. To maximize the sum, make as many vertices as possible have degree 699.

But we want to maximize the MINIMUM, not the sum. Let me think about it via the average.

Average common neighborhood = [sum_v C(deg_H(v), 2)] / C(n, 2).

If all degrees are 699: sum_v C(699, 2) = 1000 * 699 * 698 / 2. Average = 1000 * 699 * 698 / (2 * 1000 * 999 / 2) = 699 * 698 / 999 = 488302 / 999 ≈ 488.8.

So the average common neighborhood is about 489 when H is 699-regular. The minimum is at most the average, so min ≤ 489 (approximately). But we showed min ≥ 398 for 699-regular. So the answer is between 1000 - 489 = 511 and 1000 - 398 = 602.

Hmm, let me be more precise. For a 699-regular graph H on 1000 vertices:

For adjacent A, B: |N_H(A) ∩ N_H(B)| = 2*699 - |N_H(A) ∪ N_H(B)|. Since A ∈ N_H(B) and B ∈ N_H(A), |N_H(A) ∪ N_H(B)| ≤ 1000. So |intersection| ≥ 398.

For non-adjacent A, B: |N_H(A) ∪ N_H(B)| ≤ 998 (can't include A or B). So |intersection| ≥ 400.

The minimum is achieved by adjacent pairs. Can we make all adjacent pairs have |intersection| = 398? That requires |N_H(A) ∪ N_H(B)| = 1000 for all edges AB, meaning every vertex is a neighbor of A or B (in H) for every edge AB.

Alternatively, can we make the minimum larger? If for every edge AB, there exists some vertex not in N_H(A) ∪ N_H(B), then |intersection| ≥ 399 for that edge. To get min ≥ 399, we need every edge AB to have |N_H(A) ∪ N_H(B)| ≤ 999, i.e., some vertex c is non-adjacent to both A and B in H, i.e., c is adjacent to both A and B in G.

In G (300-regular), for every non-edge AB (edge in H), there exists c adjacent to both A and B in G. This means every pair of non-adjacent vertices in G has a common neighbor. This is related to the graph having diameter 2 (for non-adjacent pairs).

A 300-regular graph on 1000 vertices with diameter 2: does this exist? The Moore bound for diameter 2 and degree 300 is 300^2 + 1 = 90001, much larger than 1000, so it's certainly possible. In fact, a random 300-regular graph on 1000 vertices will have diameter 2 with high probability.

But wait, we need more: for EVERY non-edge AB in G, there's a common neighbor. And we want to maximize the minimum common neighborhood in H, which means for every edge AB in H (non-edge in G), we want |N_H(A) ∩ N_H(B)| to be large, i.e., |N_H(A) ∪ N_H(B)| to be small, i.e., many vertices non-adjacent to both A and B in H, i.e., many common neighbors of A, B in G.

So the adversary (choosing G) wants: for every non-edge AB in G, A and B have many common neighbors in G. Equivalently, in H, for every edge AB, |N_H(A) ∪ N_H(B)| is small.

|N_H(A) ∪ N_H(B)| = 2*699 - |N_H(A) ∩ N_H(B)| for adjacent A, B. And |N_H(A) ∪ N_H(B)| = 1000 - |{c : c ∉ N_H(A), c ∉ N_H(B), c ≠ A, c ≠ B}| - ... hmm wait. Let me recount.

V = {A, B} ∪ (N_H(A) ∪ N_H(B)) ∪ (V \ ({A,B} ∪ N_H(A) ∪ N_H(B))).

Since A ∈ N_H(B) and B ∈ N_H(A) (adjacent), {A, B} ⊆ N_H(A) ∪ N_H(B). So V = (N_H(A) ∪ N_H(B)) ∪ (V \ (N_H(A) ∪ N_H(B))).

|N_H(A) ∪ N_H(B)| = 1000 - |V \ (N_H(A) ∪ N_H(B))|.

V \ (N_H(A) ∪ N_H(B)) = {c : c ∉ N_H(A) and c ∉ N_H(B)} = {c : c is non-adjacent to A in H and non-adjacent to B in H} = {c : c is adjacent to A in G and adjacent to B in G, c ≠ A, c ≠ B} = common neighbors of A, B in G (since A, B are non-adjacent in G, A is not a neighbor of B in G and vice versa, so we don't need to worry about A, B being in this set).

So |V \ (N_H(A) ∪ N_H(B))| = |N_G(A) ∩ N_G(B)| (common neighbors in G, for non-adjacent A, B in G).

So |N_H(A) ∩ N_H(B)| = 1398 - (1000 - |N_G(A) ∩ N_G(B)|) = 398 + |N_G(A) ∩ N_G(B)|.

So for non-adjacent A, B in G (adjacent in H): |N_H(A) ∩ N_H(B)| = 398 + |N_G(A) ∩ N_G(B)|.

For adjacent A, B in G (non-adjacent in H): |N_H(A) ∩ N_H(B)| = 400 + |N_G(A) ∩ N_G(B)| - ... let me redo this.

For non-adjacent A, B in H (adjacent in G): A ∉ N_H(B), B ∉ N_H(A). N_H(A) ∪ N_H(B) ⊆ V \ {A, B}. |N_H(A) ∪ N_H(B)| = |N_H(A)| + |N_H(B)| - |N_H(A) ∩ N_H(B)| = 2*699 - |intersection| (if 699-regular). Also |N_H(A) ∪ N_H(B)| ≤ 998. So |intersection| ≥ 400.

V \ ({A,B} ∪ N_H(A) ∪ N_H(B)) = {c ≠ A, B : c ∉ N_H(A), c ∉ N_H(B)} = {c ≠ A, B : c ∈ N_G(A), c ∈ N_G(B)}. Since A, B adjacent in G, A ∈ N_G(B) and B ∈ N_G(A), but we exclude A, B. So this is |N_G(A) ∩ N_G(B)| - 2 (removing A and B if they're in the intersection; A ∈ N_G(B) so A ∈ N_G(A) ∩ N_G(B)? No, A ∉ N_G(A). So A ∉ N_G(A) ∩ N_G(B). Similarly B ∉ N_G(A) ∩ N_G(B). So the set is just N_G(A) ∩ N_G(B) \ {A, B} = N_G(A) ∩ N_G(B) (since A, B not in it). Wait, A ∈ N_G(B) but A ∉ N_G(A), so A ∉ N_G(A) ∩ N_G(B). Similarly B. So {c ≠ A, B : c ∈ N_G(A) ∩ N_G(B)} = N_G(A) ∩ N_G(B).

So |N_H(A) ∪ N_H(B)| = 998 - |N_G(A) ∩ N_G(B)|. (Since V \ {A, B} has 998 elements, and the union is a subset, with the complement being N_G(A) ∩ N_G(B).)

So |N_H(A) ∩ N_H(B)| = 2*699 - (998 - |N_G(A) ∩ N_G(B)|) = 1398 - 998 + |N_G(A) ∩ N_G(B)| = 400 + |N_G(A) ∩ N_G(B)|.

So:
- For A, B non-adjacent in G (edge in H): |N_H(A) ∩ N_H(B)| = 398 + |N_G(A) ∩ N_G(B)| ≥ 398.
- For A, B adjacent in G (non-edge in H): |N_H(A) ∩ N_H(B)| = 400 + |N_G(A) ∩ N_G(B)| ≥ 400.

The minimum is achieved by non-adjacent pairs in G with the fewest common neighbors. So:

min_{A≠B} |N_H(A) ∩ N_H(B)| = 398 + min_{A,B non-adjacent in G} |N_G(A) ∩ N_G(B)|.

(assuming G is 300-regular, so H is 699-regular).

The adversary wants to maximize this, so they want to maximize min_{non-adjacent A,B in G} |N_G(A) ∩ N_G(B)|.

So the question reduces to: what is the maximum possible value of min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)| over all 300-regular graphs G on 1000 vertices? (Or more generally, graphs with min degree ≥ 300.)

Wait, but I assumed 699-regular H (300-regular G). The adversary might not use a regular graph. Let me reconsider.

Actually, let me reconsider whether the adversary should use a regular graph. If G has min degree ≥ 300 but some vertices have higher degree, then H has lower degree for those vertices, which means |N_H(A) ∩ N_H(B)| could be smaller for pairs involving those vertices. So the adversary probably wants all degrees in H to be as large as possible (all degrees in G as small as possible, i.e., exactly 300). So 300-regular G (699-regular H) is likely optimal for the adversary.

But let me not assume this and think more generally later. For now, assume G is 300-regular.

So we need: max over 300-regular graphs G on 1000 vertices of min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)|.

Let me denote this as μ. Then the answer would be 1000 - 398 - μ = 602 - μ.

Now, what's the maximum possible μ?

For a 300-regular graph on 1000 vertices, consider non-adjacent vertices A, B. |N_G(A) ∩ N_G(B)| = number of common neighbors. 

Upper bound on μ: Consider any vertex A. A has 300 neighbors and 699 non-neighbors (excluding A itself). For each non-neighbor B of A, |N_G(A) ∩ N_G(B)| ≤ 300 (trivially). But we want a better bound.

Sum over all non-adjacent pairs (A, B) of |N_G(A) ∩ N_G(B)| = sum_v (number of non-adjacent pairs both adjacent to v) = sum_v C(deg(v) - ..., 2)... hmm, let me think.

For a fixed vertex v, the number of non-adjacent pairs (A, B) with A, B ∈ N_G(v) is C(deg(v), 2) - (number of edges within N_G(v)). 

This is getting complicated. Let me try a different approach.

Total common neighbors over all pairs = sum_v C(deg(v), 2) = 1000 * C(300, 2) = 1000 * 300 * 299 / 2 = 1000 * 44850 = 44,850,000.

Number of pairs = C(1000, 2) = 499,500.

Average common neighbors = 44,850,000 / 499,500 ≈ 89.79.

So the average common neighborhood (over all pairs) is about 90. The minimum over non-adjacent pairs is at most the average over non-adjacent pairs, which is at most the overall average (roughly). So μ ≤ ~90, giving answer ≥ 602 - 90 = 512.

But wait, this is the average over ALL pairs (including adjacent ones). For adjacent pairs, common neighbors might be different. Let me be more careful.

sum_{all pairs {A,B}} |N_G(A) ∩ N_G(B)| = sum_v C(deg_G(v), 2) = 1000 * C(300,2) = 44,850,000.

This sum is over all pairs. We can split into adjacent and non-adjacent pairs.

Number of edges = 1000 * 300 / 2 = 150,000.
Number of non-adjacent pairs = 499,500 - 150,000 = 349,500.

sum_{adjacent pairs} |N_G(A) ∩ N_G(B)| + sum_{non-adjacent pairs} |N_G(A) ∩ N_G(B)| = 44,850,000.

For adjacent A, B: |N_G(A) ∩ N_G(B)| = |N_G(A)| + |N_G(B)| - |N_G(A) ∪ N_G(B)|. Since A ∈ N_G(B) and B ∈ N_G(A), and N_G(A) ∪ N_G(B) ⊆ V, |N_G(A) ∪ N_G(B)| ≤ 1000. So |N_G(A) ∩ N_G(B)| ≥ 300 + 300 - 1000 = -400, which is trivially true. Not helpful.

Let me think about it differently. For adjacent A, B: |N_G(A) ∩ N_G(B)| counts common neighbors. A is a neighbor of B but A ∉ N_G(A), so A is not a common neighbor. Similarly B. So common neighbors are vertices adjacent to both A and B, excluding A, B.

Hmm, I think the key insight is about the structure. Let me think about what graph maximizes the minimum common neighborhood for non-adjacent pairs.

Consider G = complete bipartite graph K_{300, 700}. This is 300-regular for the 700-part and 700-regular for the 300-part. Not 300-regular overall. Min degree = 300. ✓

For non-adjacent A, B both in the 700-part: N_G(A) = 300-part, N_G(B) = 300-part. |N_G(A) ∩ N_G(B)| = 300.

For non-adjacent A, B both in the 300-part: N_G(A) = 700-part, N_G(B) = 700-part. |intersection| = 700.

For adjacent A (in 700-part), B (in 300-part): they're adjacent, so not a non-adjacent pair.

So min_{non-adjacent} |N_G(A) ∩ N_G(B)| = 300 (for pairs in the 700-part).

But G is not 300-regular. Let me compute the answer for this G directly.

In this G, H = complement = K_{700} ∪ K_{300} (two cliques). Wait, complement of K_{300,700} is K_{300} ∪ K_{700} (cliques on each part). Max degree in H = 699 (for 700-clique) and 299 (for 300-clique). Max degree = 699 ≤ 699. ✓

For A, B in the 700-clique of H (non-adjacent in G, both in 700-part): |N_H(A) ∩ N_H(B)| = 698 (all other vertices in 700-clique). So |N_G(A) ∩ N_G(B)| = |N_H(A) ∩ N_H(B)| - 398 = 698 - 398 = 300. ✓ (matches our calculation).

For A, B in the 300-clique of H (non-adjacent in G, both in 300-part): |N_H(A) ∩ N_H(B)| = 298. So |N_G(A) ∩ N_G(B)| = 298 - 400 = -102?? That can't be right.

Wait, I think my formula was for 699-regular H. H here is not regular. Let me recompute directly.

For A, B in 300-part of G (so in 300-clique of H), non-adjacent in G: N_H(A) = 300-clique \ {A} (size 299), N_H(B) = 300-clique \ {B} (size 299). |N_H(A) ∩ N_H(B)| = 298 (all of 300-clique except A, B).

V = 1000. Non-participants = |N_H(A) ∩ N_H(B)| = 298. So V = 1000 - 298 = 702.

For A, B in 700-part of G (700-clique of H), non-adjacent in G: |N_H(A) ∩ N_H(B)| = 698. V = 1000 - 698 = 302.

For A in 300-part, B in 700-part (adjacent in G, non-adjacent in H): N_H(A) = 300-clique \ {A} (size 299), N_H(B) = 700-clique \ {B} (size 699). |N_H(A) ∩ N_H(B)| = 0 (disjoint). V = 1000 - 0 = 1000.

So max_{A,B} V = 1000 (achieved by cross-part pairs). This is bad for the adversary.

So K_{300,700} gives max V = 1000. The adversary wants to minimize this, so they won't use this.

Let me go back to the 300-regular case and think about what maximizes μ = min_{non-adjacent} |N_G(A) ∩ N_G(B)|.

The key question: what is the maximum μ such that there exists a 300-regular graph on 1000 vertices where every pair of non-adjacent vertices has at least μ common neighbors?

This is related to the concept of "co-degree" or common neighborhood.

Let me think about an upper bound on μ. 

Consider a vertex A with 300 neighbors. The 699 non-neighbors of A each share at least μ common neighbors with A. Each common neighbor of A and B is a neighbor of A. So the 300 neighbors of A are "shared" among the 699 non-neighbors. 

For each neighbor c of A, how many non-neighbors B of A is c adjacent to? c is adjacent to A and to deg(c) - 1 - (number of neighbors of A that c is adjacent to) other vertices. Hmm, this is getting complicated.

Let me use a counting argument. Fix vertex A. sum_{B non-adjacent to A} |N_G(A) ∩ N_G(B)| = sum_{c ∈ N_G(A)} |{B non-adjacent to A : c ∈ N_G(B)}| = sum_{c ∈ N_G(A)} (deg(c) - 1 - |N_G(A) ∩ N_G(c)|).

Wait, c ∈ N_G(A). B is a non-neighbor of A with c ∈ N_G(B). The number of such B is the number of neighbors of c that are non-neighbors of A, which is deg(c) - |N_G(c) ∩ N_G(A)| - [A ∈ N_G(c)? yes, since c ∈ N_G(A) means A ∈ N_G(c)]. So neighbors of c that are non-neighbors of A = deg(c) - |N_G(c) ∩ N_G(A)| (since A is a neighbor of c but A is not a non-neighbor of A, and we're counting non-neighbors of A among neighbors of c). 

Actually: neighbors of c = N_G(c). Among these, some are neighbors of A (i.e., in N_G(A)) and some are non-neighbors of A. |N_G(c) ∩ N_G(A)| = common neighbors of A and c (but A and c are adjacent, so this counts vertices adjacent to both, excluding A and c). The number of neighbors of c that are non-neighbors of A = deg(c) - 1 - |N_G(c) ∩ N_G(A)|. The -1 is for A itself (A is a neighbor of c but A is not a non-neighbor of A; A is A).

Hmm wait. Neighbors of c: N_G(c), which has deg(c) = 300 elements. A ∈ N_G(c). Neighbors of A: N_G(A), 300 elements. c ∈ N_G(A).

Neighbors of c that are non-neighbors of A: {x ∈ N_G(c) : x ∉ N_G(A), x ≠ A}. Since A ∈ N_G(c) but A ∉ N_G(A) (no self-loop) and A is not a "non-neighbor of A" in the sense we want (we want B ≠ A). Actually, non-neighbors of A = V \ (N_G(A) ∪ {A}). So B is a non-neighbor of A iff B ∉ N_G(A) and B ≠ A.

So {x ∈ N_G(c) : x is a non-neighbor of A} = N_G(c) \ (N_G(A) ∪ {A}) = N_G(c) \ N_G(A) (since A ∈ N_G(c) and A ∉ N_G(A), so A is already removed by the set difference with N_G(A)... no. N_G(c) \ N_G(A) removes elements of N_G(A) from N_G(c). A ∈ N_G(c) but A ∉ N_G(A), so A is NOT removed. So N_G(c) \ N_G(A) still contains A. We need to also remove A.)

So {x ∈ N_G(c) : x is a non-neighbor of A} = N_G(c) \ (N_G(A) ∪ {A}) = (N_G(c) \ N_G(A)) \ {A}.

|N_G(c) \ N_G(A)| = deg(c) - |N_G(c) ∩ N_G(A)| = 300 - |N_G(A) ∩ N_G(c)|.

So the count = 300 - |N_G(A) ∩ N_G(c)| - 1 (removing A) = 299 - |N_G(A) ∩ N_G(c)|.

So sum_{B non-adjacent to A} |N_G(A) ∩ N_G(B)| = sum_{c ∈ N_G(A)} (299 - |N_G(A) ∩ N_G(c)|) = 300 * 299 - sum_{c ∈ N_G(A)} |N_G(A) ∩ N_G(c)|.

Now, sum_{c ∈ N_G(A)} |N_G(A) ∩ N_G(c)| = sum_{c ∈ N_G(A)} |{d ∈ N_G(A) : d ∈ N_G(c)}| = sum_{d ∈ N_G(A)} |{c ∈ N_G(A) : d ∈ N_G(c)}| = sum_{d ∈ N_G(A)} |N_G(A) ∩ N_G(d)|.

Wait, that's the same sum. Let me denote S = sum_{c ∈ N_G(A)} |N_G(A) ∩ N_G(c)|. This counts the number of edges within N_G(A) (each edge {c, d} within N_G(A) is counted... hmm, |N_G(A) ∩ N_G(c)| for c ∈ N_G(A) counts neighbors of c that are in N_G(A), which is the number of edges from c to other vertices in N_G(A). So S = 2 * (number of edges within N_G(A)).

Let e_A = number of edges within N_G(A). Then S = 2 * e_A.

So sum_{B non-adjacent to A} |N_G(A) ∩ N_G(B)| = 300 * 299 - 2 * e_A = 89700 - 2 * e_A.

There are 699 non-adjacent vertices B. So the average common neighborhood for non-adjacent pairs involving A is (89700 - 2 * e_A) / 699.

For the minimum to be at least μ, we need (89700 - 2 * e_A) / 699 ≥ μ for all A, roughly (the average being ≥ μ is necessary but not sufficient for the min to be ≥ μ). Actually, we need every individual term to be ≥ μ, so the average is also ≥ μ. So:

89700 - 2 * e_A ≥ 699 * μ for all A.

e_A ≤ (89700 - 699μ) / 2.

Now, sum over all A of e_A = sum_A (edges within N_G(A)) = sum_{edge {c,d}} |{A : c ∈ N_G(A) and d ∈ N_G(A)}| = sum_{edge {c,d}} |N_G(c) ∩ N_G(d)| (common neighbors of c, d, which are adjacent).

Hmm, this is getting complicated. Let me try a different approach.

Let me think about the problem from a higher level. The answer is 1000 - max_H min_{A≠B} |N_H(A) ∩ N_H(B)| where H has max degree ≤ 699.

Let me think about what the optimal H looks like. We want to maximize the minimum common neighborhood. 

Consider H being a "complete multipartite graph" or some structured graph. Actually, let me think about H being a complete bipartite graph plus some edges.

Hmm, let me think about this differently. Let me consider the problem in terms of the original graph G.

We want min_G max_{A,B} |N_G(A) ∪ N_G(B)| where G has min degree ≥ 300 on 1000 vertices.

|N_G(A) ∪ N_G(B)| = 1000 - |M(A) ∩ M(B)| where M(v) = non-neighbors of v (excluding v).

We want to find the G that minimizes max_{A,B} |N_G(A) ∪ N_G(B)|, i.e., maximizes min_{A,B} |M(A) ∩ M(B)|.

|M(v)| = 999 - deg(v) ≤ 699.

To maximize min_{A,B} |M(A) ∩ M(B)|, we want all M(v) to be large (so deg(v) = 300 for all v, making |M(v)| = 699) and to have large pairwise intersections.

By the inclusion-exclusion principle, |M(A) ∩ M(B)| = |M(A)| + |M(B)| - |M(A) ∪ M(B)| ≥ 699 + 699 - 1000 = 398 (since M(A) ∪ M(B) ⊆ V, but actually A ∉ M(A) and B ∉ M(B), so M(A) ∪ M(B) ⊆ V \ ... hmm, A ∉ M(A) but A could be in M(B) if A is a non-neighbor of B. So M(A) ∪ M(B) ⊆ V. So |M(A) ∪ M(B)| ≤ 1000, giving |M(A) ∩ M(B)| ≥ 398.

But can we achieve |M(A) ∩ M(B)| = 398 for all pairs? That requires |M(A) ∪ M(B)| = 1000 for all pairs, i.e., M(A) ∪ M(B) = V for all A, B. This means for every vertex v and every pair A, B, v ∈ M(A) or v ∈ M(B), i.e., v is a non-neighbor of A or a non-neighbor of B.

Equivalently, there's no vertex v that is a neighbor of both A and B, i.e., |N_G(A) ∩ N_G(B)| = 0 for all A, B (well, for all A ≠ B). But that's impossible since each vertex has 300 neighbors and there are 1000 vertices; by pigeonhole, some pair shares a neighbor.

Actually wait, |N_G(A) ∩ N_G(B)| = 0 for all A ≠ B would mean the neighborhoods are pairwise disjoint, but 1000 * 300 = 300000 > 1000, impossible.

So we can't achieve 398 for all pairs. The minimum of |M(A) ∩ M(B)| will be higher than 398.

Let me think about the upper bound on min_{A,B} |M(A) ∩ M(B)| more carefully.

We have |M(A) ∩ M(B)| = 1398 - |M(A) ∪ M(B)|. To minimize this (which is what the "maximizer" of V wants), we maximize |M(A) ∪ M(B)|. The adversary wants to make |M(A) ∪ M(B)| small for all pairs.

|M(A) ∪ M(B)| = |M(A)| + |M(B)| - |M(A) ∩ M(B)|. If all |M(v)| = 699, then |M(A) ∪ M(B)| = 1398 - |M(A) ∩ M(B)|. And |M(A) ∪ M(B)| ≤ 1000, so |M(A) ∩ M(B)| ≥ 398.

Now, |M(A) ∪ M(B)| = 1000 - |{v : v ∉ M(A) and v ∉ M(B)}| = 1000 - |{v : v ∈ N_G(A) ∪ {A} and v ∈ N_G(B) ∪ {B}}|.

{v : v ∈ N_G(A) ∪ {A} and v ∈ N_G(B) ∪ {B}} = (N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}).

If A, B are non-adjacent: A ∉ N_G(B), B ∉ N_G(A). (N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}) = (N_G(A) ∩ N_G(B)) ∪ (N_G(A) ∩ {B}) ∪ ({A} ∩ N_G(B)) ∪ ({A} ∩ {B}). Since A ≠ B, {A} ∩ {B} = ∅. N_G(A) ∩ {B} = ∅ (B ∉ N_G(A)). {A} ∩ N_G(B) = ∅ (A ∉ N_G(B)). So the intersection = N_G(A) ∩ N_G(B).

So |M(A) ∪ M(B)| = 1000 - |N_G(A) ∩ N_G(B)|, and |M(A) ∩ M(B)| = 1398 - 1000 + |N_G(A) ∩ N_G(B)| = 398 + |N_G(A) ∩ N_G(B)|.

If A, B are adjacent: A ∈ N_G(B), B ∈ N_G(A). (N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}) = (N_G(A) ∩ N_G(B)) ∪ (N_G(A) ∩ {B}) ∪ ({A} ∩ N_G(B)) ∪ {A, B}... hmm, let me be more careful. B ∈ N_G(A), so B ∈ N_G(A) ∪ {A}. A ∈ N_G(B), so A ∈ N_G(B) ∪ {B}. So A ∈ (N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}) and B ∈ same. 

(N_G(A) ∪ {A}) ∩ (N_G(B) ∪ {B}) = N_G(A) ∩ N_G(B) ∪ N_G(A) ∩ {B} ∪ {A} ∩ N_G(B) ∪ {A} ∩ {B}.

N_G(A) ∩ {B} = {B} (since B ∈ N_G(A)). {A} ∩ N_G(B) = {A} (since A ∈ N_G(B)). {A} ∩ {B} = ∅.

So the intersection = (N_G(A) ∩ N_G(B)) ∪ {A} ∪ {B}. |intersection| = |N_G(A) ∩ N_G(B)| + 2 (since A, B ∉ N_G(A) ∩ N_G(B) as A ∉ N_G(A), B ∉ N_G(B)).

So |M(A) ∪ M(B)| = 1000 - |N_G(A) ∩ N_G(B)| - 2, and |M(A) ∩ M(B)| = 1398 - (1000 - |N_G(A) ∩ N_G(B)| - 2) = 400 + |N_G(A) ∩ N_G(B)|.

So:
- Non-adjacent A, B: |M(A) ∩ M(B)| = 398 + |N_G(A) ∩ N_G(B)|
- Adjacent A, B: |M(A) ∩ M(B)| = 400 + |N_G(A) ∩ N_G(B)|

The minimum over all pairs is achieved by non-adjacent pairs with the fewest common neighbors. So:

min_{A≠B} |M(A) ∩ M(B)| = 398 + min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)|.

(assuming all degrees are exactly 300; if some degrees are higher, |M(v)| is smaller, which could reduce the intersection further. So the adversary should use 300-regular.)

Wait, but I need to also check: if degrees are not all 300, could the minimum be achieved by a pair involving a high-degree vertex? Let's check. If A has degree d_A > 300, then |M(A)| = 999 - d_A < 699. For non-adjacent A, B: |M(A) ∩ M(B)| = |M(A)| + |M(B)| - |M(A) ∪ M(B)| ≥ (999 - d_A) + (999 - d_B) - 1000 = 998 - d_A - d_B. If d_A = 301, d_B = 300: ≥ 998 - 601 = 397 < 398. So having higher degree vertices could actually decrease the minimum! So the adversary should indeed use 300-regular.

Wait, but that's a lower bound. The actual value could be higher. Let me reconsider. If A has degree 301, |M(A)| = 698. For non-adjacent A, B with d_B = 300, |M(B)| = 699. |M(A) ∩ M(B)| = 698 + 699 - |M(A) ∪ M(B)|. |M(A) ∪ M(B)| ≤ 1000. So |M(A) ∩ M(B)| ≥ 397. This is less than 398. So indeed, having a vertex with degree > 300 could make the minimum smaller. So the adversary should make all degrees exactly 300.

Hmm, but actually the adversary wants to MAXIMIZE the minimum. So they want to avoid having any pair with small intersection. Having a vertex with degree > 300 creates a smaller M(v), which could lead to smaller intersections. So the adversary should use 300-regular.

OK so assuming 300-regular G, the answer is:

1000 - 398 - μ = 602 - μ

where μ = max over 300-regular graphs G on 1000 vertices of min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)|.

Now I need to find μ.

Let me think about upper bounds on μ.

Fix a vertex A. A has 300 neighbors and 699 non-neighbors. For each non-neighbor B, |N_G(A) ∩ N_G(B)| ≥ μ. The common neighbors of A and B are in N_G(A) (300 vertices). Each vertex c ∈ N_G(A) can be a common neighbor of A and multiple non-neighbors B. Specifically, c is a common neighbor of A and B iff B ∈ N_G(c). The number of non-neighbors of A that c is adjacent to is (as computed earlier) 299 - |N_G(A) ∩ N_G(c)|.

So sum_{B non-adjacent to A} |N_G(A) ∩ N_G(B)| = sum_{c ∈ N_G(A)} (299 - |N_G(A) ∩ N_G(c)|) = 300 * 299 - 2 * e_A

where e_A = number of edges within N_G(A).

This sum ≥ 699 * μ (since each of the 699 terms is ≥ μ).

So 300 * 299 - 2 * e_A ≥ 699 * μ, i.e., e_A ≤ (89700 - 699μ) / 2.

Now, sum_A e_A = sum_A (edges within N_G(A)). Each edge {u, v} in G is counted in e_A for each A such that u, v ∈ N_G(A), i.e., A is a common neighbor of u and v. So sum_A e_A = sum_{edge {u,v}} |N_G(u) ∩ N_G(v)|.

For adjacent u, v: |N_G(u) ∩ N_G(v)| = (common neighbors). For the sum, we only count edges {u,v}, so we need |N_G(u) ∩ N_G(v)| for adjacent pairs.

Hmm, let me denote for adjacent u, v: c(u,v) = |N_G(u) ∩ N_G(v)|. Then sum_A e_A = sum_{edges {u,v}} c(u,v).

Also, sum_{edges {u,v}} c(u,v) = sum_{edges {u,v}} |N_G(u) ∩ N_G(v)| = sum_w (number of edges among N_G(w)) = sum_w e_w.

So sum_A e_A = sum_w e_w. That's a tautology. Not helpful directly.

Let me try another approach. Let's bound sum_A e_A from below.

sum_A e_A = sum_w e_w. We want a lower bound. e_w = number of edges within N_G(w). By convexity or other means...

Actually, let me think about the total number of "triangles" or "paths" differently.

sum_A e_A = sum_A (edges in N_G(A)) = number of (A, {u,v}) where {u,v} is an edge and u, v ∈ N_G(A) = number of triangles * 3 + number of "cherries" ... no. Actually, (A, {u,v}) where u, v ∈ N_G(A) and {u,v} is an edge: this is a triangle (A, u, v) if {A,u}, {A,v}, {u,v} are all edges. Since u, v ∈ N_G(A), {A,u} and {A,v} are edges. And {u,v} is an edge. So this is a triangle. Each triangle is counted 3 times (once for each vertex as A). So sum_A e_A = 3 * T where T is the number of triangles.

So e_A = (number of triangles containing A) and sum_A e_A = 3T.

Now, from the constraint e_A ≤ (89700 - 699μ)/2 for all A, we get sum_A e_A ≤ 1000 * (89700 - 699μ)/2 = 500 * (89700 - 699μ) = 44850000 - 349500μ.

So 3T ≤ 44850000 - 349500μ, i.e., T ≤ (44850000 - 349500μ)/3.

But we also need a lower bound on T (or sum e_A) to get an upper bound on μ.

Hmm, is there a lower bound on the number of triangles in a 300-regular graph on 1000 vertices? Not necessarily; the graph could be triangle-free (e.g., bipartite). A 300-regular bipartite graph on 1000 vertices exists (e.g., K_{300, 700} is not regular, but a 300-regular bipartite graph on 500+500 vertices exists). Wait, 300-regular bipartite graph needs each part to have at least 300 vertices. 500 + 500 = 1000, and a 300-regular bipartite graph on 500+500 exists. In this case, T = 0, e_A = 0 for all A.

With e_A = 0: 89700 - 0 ≥ 699μ, so μ ≤ 89700/699 ≈ 128.3. So μ ≤ 128.

But can we achieve μ = 128 with a triangle-free 300-regular graph? In a bipartite 300-regular graph on 500+500, for non-adjacent A, B in the same part: N_G(A) and N_G(B) are both subsets of the other part (size 500). |N_G(A) ∩ N_G(B)| = |N_G(A)| + |N_G(B)| - |N_G(A) ∪ N_G(B)| = 300 + 300 - |N_G(A) ∪ N_G(B)|. Since N_G(A) ∪ N_G(B) ⊆ other part (size 500), |union| ≤ 500. So |intersection| ≥ 100. And |intersection| ≤ 300.

For the minimum to be μ, we need min |N_G(A) ∩ N_G(B)| = μ for non-adjacent pairs. In a bipartite graph, non-adjacent pairs include pairs in the same part and pairs in different parts that are not connected.

For A, B in different parts, non-adjacent: N_G(A) ⊆ part_B, N_G(B) ⊆ part_A. These are in different parts, so N_G(A) ∩ N_G(B) = ∅. So |N_G(A) ∩ N_G(B)| = 0!

So in a bipartite graph, μ = 0 (cross-part non-adjacent pairs have 0 common neighbors). That's terrible.

So bipartite graphs give μ = 0, and the answer would be 602 - 0 = 602. But wait, is 602 achievable? Let me check: with a 300-regular bipartite graph on 500+500, the answer is 1000 - 398 - 0 = 602. But we need to verify that the minimum of |M(A) ∩ M(B)| is indeed 398.

For cross-part non-adjacent A, B: |N_G(A) ∩ N_G(B)| = 0, so |M(A) ∩ M(B)| = 398 + 0 = 398. V = 1000 - 398 = 602.

For same-part non-adjacent A, B: |N_G(A) ∩ N_G(B)| ≥ 100, so |M(A) ∩ M(B)| ≥ 498. V ≤ 502.

For adjacent A, B: |M(A) ∩ M(B)| = 400 + |N_G(A) ∩ N_G(B)|. In bipartite graph, adjacent A, B have N_G(A) ⊆ part_B, N_G(B) ⊆ part_A, so N_G(A) ∩ N_G(B) = ∅. |M(A) ∩ M(B)| = 400. V = 600.

So the minimum |M(A) ∩ M(B)| = 398 (from cross-part non-adjacent pairs), giving max V = 602.

Wait, but adjacent pairs give |M(A) ∩ M(B)| = 400, V = 600. Cross-part non-adjacent give 398, V = 602. Same-part non-adjacent give ≥ 498, V ≤ 502.

So max_{A,B} V = 602 (from cross-part non-adjacent pairs).

But can the adversary do better? Can they find a graph where min_{A,B} |M(A) ∩ M(B)| > 398?

The adversary wants to avoid having any pair with |N_G(A) ∩ N_G(B)| = 0 (for non-adjacent pairs) or small common neighborhoods. In the bipartite case, cross-part non-adjacent pairs have 0 common neighbors, which is the worst.

To avoid this, the adversary needs the graph to not be bipartite, and more generally, to have the property that every pair of non-adjacent vertices has a common neighbor. This is the "diameter 2" property (for the non-adjacent pairs).

But even with diameter 2, the common neighborhood could be just 1, giving |M(A) ∩ M(B)| = 399, V = 601. The adversary wants to maximize the minimum common neighborhood.

So the question is: what is the maximum μ such that there's a 300-regular graph on 1000 vertices where every non-adjacent pair has ≥ μ common neighbors?

And the answer to the original problem is 602 - μ.

Now I need to find μ. Let me think about upper bounds.

From the earlier analysis: for any vertex A, sum_{B non-adj to A} |N_G(A) ∩ N_G(B)| = 89700 - 2*e_A. With 699 non-neighbors, the average is (89700 - 2*e_A)/699. For the minimum to be ≥ μ, we need this average ≥ μ, so 89700 - 2*e_A ≥ 699μ, i.e., e_A ≤ (89700 - 699μ)/2.

Also, e_A ≥ 0, so μ ≤ 89700/699 ≈ 128.3, so μ ≤ 128.

But this is just from one vertex. Can we get a better bound?

Let me think about summing over all vertices. sum_A (89700 - 2*e_A) = 1000 * 89700 - 2 * 3T = 89700000 - 6T. This should be ≥ 1000 * 699 * μ = 699000μ. So 89700000 - 6T ≥ 699000μ, i.e., T ≤ (89700000 - 699000μ)/6 = 14950000 - 116500μ.

We need T ≥ 0, so μ ≤ 14950000/116500 ≈ 128.3. Same bound.

But we might get a better bound by considering the structure more carefully. Let me think about whether μ = 128 is achievable.

Hmm, actually, let me reconsider. The bound μ ≤ 128 comes from e_A ≥ 0. But can we have e_A = 0 for all A (triangle-free) and still have μ = 128?

If e_A = 0 for all A (triangle-free), then for each A, the average common neighborhood with non-neighbors is 89700/699 ≈ 128.3. For the minimum to be 128, we need all 699 non-neighbors to have common neighborhood ≥ 128, with the average being 128.3. So most would be 128 or 129. This seems very tight.

But we also need the graph to be triangle-free AND have every non-adjacent pair with ≥ 128 common neighbors. In a triangle-free graph, if A, B are non-adjacent with common neighbor c, then c is adjacent to both A and B, but A, B are not adjacent (good, no triangle). But N_G(A) and N_G(B) can share many vertices without forming triangles (since A, B are non-adjacent).

Wait, but if c, d are both common neighbors of A, B, and c, d are adjacent, then {A, c, d} might form a triangle if A is adjacent to both c and d (which it is, since c, d ∈ N_G(A)). So if c, d ∈ N_G(A) and {c,d} is an edge, that's a triangle. So in a triangle-free graph, N_G(A) is an independent set for every A. This means e_A = 0 for all A, which is consistent.

So in a triangle-free 300-regular graph, N_G(A) is an independent set of size 300 for every A. This is a strong condition. Such graphs exist (bipartite graphs are triangle-free, but as we saw, bipartite graphs have μ = 0). Are there non-bipartite triangle-free 300-regular graphs on 1000 vertices?

A triangle-free graph that's not bipartite must contain an odd cycle of length ≥ 5. But the key question is whether we can have a triangle-free 300-regular graph on 1000 vertices with μ = 128.

Hmm, this is getting very complicated. Let me step back and think about whether the answer might just be 602.

Actually, let me reconsider the problem. The bipartite construction gives max V = 602. Can the adversary do better, i.e., achieve max V < 602?

For the adversary to do better, they need min_{A,B} |M(A) ∩ M(B)| > 398. This requires for every non-adjacent pair A, B: |N_G(A) ∩ N_G(B)| ≥ 1 (at least), and more generally, they want to maximize the minimum.

But maybe the adversary can't do better than 398, and the answer is 602.

Let me think about whether there's a graph where min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)| ≥ 1, i.e., every non-adjacent pair has a common neighbor. This is equivalent to the graph having diameter ≤ 2 (for non-adjacent pairs, distance exactly 2). 

A 300-regular graph on 1000 vertices with diameter 2: the Moore bound for diameter 2 and degree 300 is 1 + 300 + 300*299 = 1 + 300 + 89700 = 90001. Since 1000 << 90001, such graphs certainly exist. In fact, a random 300-regular graph on 1000 vertices will have diameter 2 w.h.p.

In such a graph, μ ≥ 1, so the answer would be ≤ 601. But can the adversary achieve μ much larger?

Let me think about the trade-off. The adversary wants to maximize μ = min_{non-adjacent} |N_G(A) ∩ N_G(B)|. 

From the constraint e_A ≤ (89700 - 699μ)/2, to have large μ, we need small e_A (few edges within neighborhoods, i.e., few triangles). But we also need the graph to be well-connected so that non-adjacent pairs have many common neighbors.

There's a tension: to have many common neighbors for non-adjacent pairs, the graph should be "expander-like", but to have few triangles, the graph should be "bipartite-like". 

Let me think about a specific construction. Consider a graph G that's the union of two copies of K_{500} (two cliques of size 500), but with some edges removed to make it 300-regular. In K_{500}, each vertex has degree 499. To make it 300-regular, remove 199 edges per vertex. But this is within each clique, so the graph is disconnected (two components). Non-adjacent pairs in different components have 0 common neighbors. μ = 0. Bad.

What about a graph that's "almost" a clique? Like a 300-regular graph that's very dense in terms of common neighborhoods but has few triangles?

Hmm, let me think about this more carefully using the following approach:

For a 300-regular graph G on 1000 vertices, the number of non-adjacent pairs is 349500. The total common neighborhood over non-adjacent pairs is:

sum_{non-adj A,B} |N_G(A) ∩ N_G(B)| = sum_v C(deg(v), 2) - sum_{adj A,B} |N_G(A) ∩ N_G(B)|
= 1000 * C(300,2) - sum_{adj A,B} |N_G(A) ∩ N_G(B)|
= 44850000 - sum_{adj A,B} |N_G(A) ∩ N_G(B)|.

Now, sum_{adj A,B} |N_G(A) ∩ N_G(B)| = 3T (each triangle contributes 1 to the common neighborhood of each of its 3 edges). Wait, for an edge {A,B}, |N_G(A) ∩ N_G(B)| counts common neighbors, which are vertices adjacent to both A and B. Each triangle (A, B, C) where {A,B}, {B,C}, {A,C} are edges contributes C to |N_G(A) ∩ N_G(B)|. So sum over edges of |N_G(A) ∩ N_G(B)| = 3T (each triangle counted 3 times, once for each edge).

So sum_{non-adj A,B} |N_G(A) ∩ N_G(B)| = 44850000 - 3T.

Average over non-adjacent pairs = (44850000 - 3T) / 349500.

For the minimum to be ≥ μ, we need the average ≥ μ:
(44850000 - 3T) / 349500 ≥ μ
44850000 - 3T ≥ 349500μ
T ≤ (44850000 - 349500μ) / 3 = 14950000 - 116500μ.

Since T ≥ 0: μ ≤ 14950000 / 116500 ≈ 128.3. Same bound as before.

But we can also get a lower bound on T. By the Kruskal-Katona theorem or just by the fact that a 300-regular graph on 1000 vertices must have some triangles... actually, it doesn't. A bipartite 300-regular graph has T = 0.

But if we want μ ≥ 1 (every non-adjacent pair has a common neighbor), can we have T = 0? A triangle-free graph with diameter 2: this is possible (e.g., the Petersen graph is triangle-free with diameter 2, but it's small). For 300-regular on 1000 vertices, a triangle-free diameter-2 graph: the Moore bound for triangle-free diameter-2 is 1 + d + d(d-1) = 1 + 300 + 300*299 = 90001 (this is the same as the Moore bound, since triangle-free means no edges among neighbors). Wait, the Moore bound for diameter 2 is 1 + d + d(d-1) = d^2 + 1. For d = 300, that's 90001. So a triangle-free 300-regular graph with diameter 2 can have up to 90001 vertices. Since 1000 < 90001, such a graph could exist.

But does a triangle-free 300-regular graph on 1000 vertices with diameter 2 exist? It's not guaranteed. The existence of Moore graphs (achieving the bound) is rare, but we don't need to achieve the bound; we just need 1000 vertices.

A bipartite graph is triangle-free but has diameter > 2 (cross-part non-adjacent pairs have no common neighbor). A non-bipartite triangle-free graph with diameter 2 would work. 

Consider a graph based on a finite geometry or algebraic construction. For example, a polarity graph of a projective plane. But let me think about simpler constructions.

Actually, let me think about this problem differently. Let me consider the complement graph H (699-regular on 1000 vertices) and think about what structure maximizes min |N_H(A) ∩ N_H(B)|.

We showed min |N_H(A) ∩ N_H(B)| = 398 + μ where μ = min_{non-adj in G} |N_G(A) ∩ N_G(B)|.

The answer is 1000 - 398 - μ = 602 - μ.

So I need to find the maximum μ. Let me think about whether μ can be large.

Consider a strongly regular graph. A strongly regular graph with parameters (n, d, λ, μ) is a d-regular graph on n vertices where adjacent pairs have λ common neighbors and non-adjacent pairs have μ common neighbors.

If G is strongly regular with parameters (1000, 300, λ, μ_srg), then μ = μ_srg. The parameters satisfy:
(n - d - 1) * μ_srg = d * (d - λ - 1)
(1000 - 300 - 1) * μ_srg = 300 * (300 - λ - 1)
699 * μ_srg = 300 * (299 - λ)
μ_srg = 300 * (299 - λ) / 699

For μ_srg to be an integer, 699 | 300 * (299 - λ). 699 = 3 * 233. 300 = 3 * 100. So 233 | 100 * (299 - λ). Since gcd(233, 100) = 1, we need 233 | (299 - λ), so 299 - λ ≡ 0 (mod 233), so λ ≡ 299 (mod 233) ≡ 66 (mod 233). Since 0 ≤ λ ≤ 299, λ = 66 or λ = 66 + 233 = 299.

If λ = 66: μ_srg = 300 * 233 / 699 = 300 * 233 / (3 * 233) = 300/3 = 100. So μ_srg = 100.

If λ = 299: μ_srg = 300 * 0 / 699 = 0. This would mean non-adjacent pairs have 0 common neighbors, which is the bipartite case (λ = 299 means the graph is a union of cliques, but with d = 300 and n = 1000, a clique of size 301... 1000/301 is not integer, so this doesn't directly work).

So a strongly regular graph with parameters (1000, 300, 66, 100) would give μ = 100. Does such a graph exist?

The eigenvalues of a strongly regular graph (1000, 300, 66, 100) can be computed. The eigenvalues are d = 300 and the roots of x^2 + (μ_srg - λ) x + (μ_srg - d) = 0, i.e., x^2 + (100 - 66) x + (100 - 300) = 0, x^2 + 34x - 200 = 0. x = (-34 ± sqrt(1156 + 800))/2 = (-34 ± sqrt(1956))/2 = (-34 ± 44.227)/2. So x1 ≈ 5.11, x2 ≈ -39.11. These are not integers, so the multiplicities might not be integers. Let me check.

For a strongly regular graph, the multiplicities are:
f = (1/2) * (n-1) - (d + (n-1)(λ-μ_srg))/(2*sqrt((λ-μ_srg)^2 + 4(d-μ_srg)))
g = (1/2) * (n-1) + (d + (n-1)(λ-μ_srg))/(2*sqrt((λ-μ_srg)^2 + 4(d-μ_srg)))

(λ - μ_srg)^2 + 4(d - μ_srg) = (66-100)^2 + 4(300-100) = 1156 + 800 = 1956.
sqrt(1956) = 2*sqrt(489) = 2*sqrt(3*163). Not a perfect square. So the eigenvalues are irrational, and the multiplicities would need to be integers, which requires the discriminant to be a perfect square. Since 1956 is not a perfect square, this strongly regular graph does not exist (for a conference graph, the discriminant not being a perfect square is OK, but then n must be specific).

Actually, for a conference graph (where the eigenvalues are not integers), the parameters must satisfy n = 2d + ... hmm, conference graphs have specific parameter relations. Let me not go down this path.

So a strongly regular graph with these exact parameters likely doesn't exist. But the question is about the maximum μ, not necessarily achieved by a strongly regular graph.

Let me think about this more carefully. The key constraint is:

For a 300-regular graph on 1000 vertices, the average common neighborhood over non-adjacent pairs is (44850000 - 3T) / 349500. For the minimum to be large, we want this average to be large, which means T should be small.

If T = 0 (triangle-free), the average is 44850000 / 349500 ≈ 128.3. So μ ≤ 128 (since min ≤ average, and μ must be an integer... well, μ doesn't have to be an integer, but the common neighborhood is an integer).

But can we achieve μ = 128 with a triangle-free graph? We need every non-adjacent pair to have ≥ 128 common neighbors, with the average being 128.3. This means almost all non-adjacent pairs have exactly 128 or 129 common neighbors.

But there's a problem: in a triangle-free graph, for any vertex A, N_G(A) is an independent set. For a non-neighbor B of A, the common neighbors of A and B are in N_G(A) (independent set) and also in N_G(B) (independent set). The common neighbors form a subset of N_G(A) that is also in N_G(B).

In a triangle-free graph, if B is a non-neighbor of A, then N_G(A) ∩ N_G(B) is a set of vertices each adjacent to both A and B. Since the graph is triangle-free, no two vertices in N_G(A) are adjacent (N_G(A) is independent), and similarly for N_G(B). But vertices in N_G(A) ∩ N_G(B) are in both N_G(A) and N_G(B), so they're adjacent to both A and B but not to each other (since they're in N_G(A) which is independent). This is fine.

But here's the issue: can a triangle-free 300-regular graph on 1000 vertices exist where every non-adjacent pair has ≥ 128 common neighbors?

Let me think about the constraints. For vertex A with 300 neighbors (independent set) and 699 non-neighbors. Each non-neighbor B shares ≥ 128 neighbors with A. The 300 neighbors of A are shared among 699 non-neighbors, with each neighbor c being shared with (299 - |N_G(A) ∩ N_G(c)|) non-neighbors. Since the graph is triangle-free, |N_G(A) ∩ N_G(c)| = 0 for c ∈ N_G(A) (because N_G(A) is independent, so c has no neighbors in N_G(A) except... wait, c ∈ N_G(A), and N_G(A) is independent, so c has no neighbors in N_G(A) \ {c}. But c could be adjacent to vertices in N_G(A). No—N_G(A) is independent means no edges within N_G(A). So c has 0 neighbors in N_G(A). So |N_G(A) ∩ N_G(c)| = 0 (since N_G(A) ∩ N_G(c) ⊆ N_G(A), and c has no neighbors in N_G(A), so the intersection is empty). Wait, N_G(A) ∩ N_G(c) = vertices adjacent to both A and c. These vertices are in N_G(A) (adjacent to A) and in N_G(c) (adjacent to c). Since N_G(A) is independent, no vertex in N_G(A) is adjacent to c (which is also in N_G(A)). So N_G(A) ∩ N_G(c) = ∅. So |N_G(A) ∩ N_G(c)| = 0.

So each neighbor c of A is a common neighbor of A and exactly 299 non-neighbors of A (since 299 - 0 = 299). Total: 300 * 299 = 89700. With 699 non-neighbors, average = 89700/699 ≈ 128.3. ✓

For the minimum to be 128, we need each non-neighbor to have at least 128 common neighbors with A, and the total is 89700 = 128 * 699 + 228 = 89700 - 89472 = 228. So 228 non-neighbors have 129 common neighbors and 699 - 228 = 471 have 128. Or some other distribution summing to 89700 with each ≥ 128.

This seems feasible in principle. But does such a graph exist?

This is related to the concept of a "Moore graph" or "near-Moore graph" for diameter 2. A Moore graph with diameter 2 and degree d has n = d^2 + 1 vertices, and every non-adjacent pair has exactly 1 common neighbor. That's the opposite of what we want (we want many common neighbors, not few).

Actually, I think I'm overcomplicating this. Let me reconsider.

We want to maximize μ = min_{non-adjacent} |N_G(A) ∩ N_G(B)|. The constraint is μ ≤ 128 (from the averaging argument with T = 0). But is μ = 128 actually achievable?

Let me think about a specific construction. Consider a graph G on 1000 vertices that's triangle-free and 300-regular, where non-adjacent pairs have many common neighbors.

One approach: take a bipartite graph and add some edges within parts to create common neighbors for cross-part non-adjacent pairs, while maintaining triangle-freeness.

Actually, in a bipartite graph with parts X (500) and Y (500), cross-part non-adjacent pairs (A ∈ X, B ∈ Y, not adjacent) have 0 common neighbors (since N_G(A) ⊆ Y and N_G(B) ⊆ X, disjoint). To fix this, we'd need to add edges within parts, but that creates triangles (if A ∈ X is adjacent to C ∈ X, and both are adjacent to some D ∈ Y, then {A, C, D} is a triangle).

Hmm, so adding edges within parts in a bipartite graph creates triangles. To maintain triangle-freeness, we'd need to ensure that no two adjacent vertices within a part share a neighbor in the other part. This is very restrictive.

Let me think about non-bipartite triangle-free graphs. The Clebsch graph, Petersen graph, etc. are small. For larger graphs, we can use algebraic constructions.

Actually, let me think about this problem from a completely different angle. Maybe the answer is simply 602, achieved by the bipartite construction, and no graph can do better.

Wait, but I showed that if the graph has diameter 2 (every non-adjacent pair has ≥ 1 common neighbor), then μ ≥ 1 and the answer is ≤ 601. So the bipartite construction is NOT optimal for the adversary!

The adversary can do better than the bipartite construction by using a graph with diameter 2. So the answer is less than 602.

Let me reconsider. The adversary wants to minimize max_{A,B} V = 1000 - min_{A,B} |M(A) ∩ M(B)| = 1000 - (398 + μ) = 602 - μ. So the adversary wants to maximize μ.

The question is: what is the maximum μ over all graphs G with min degree ≥ 300 on 1000 vertices?

We've established μ ≤ 128 (from the triangle-free bound, but actually this bound applies to all graphs, not just triangle-free ones—let me recheck).

From the averaging argument: for any 300-regular graph, average common neighborhood over non-adjacent pairs = (44850000 - 3T) / 349500. Since T ≥ 0, this is ≤ 44850000 / 349500 ≈ 128.3. So μ ≤ 128.

But can μ = 128 be achieved? This requires T = 0 (triangle-free) and a very uniform distribution of common neighborhoods.

Actually, wait. Let me reconsider whether the graph needs to be 300-regular. The adversary wants to maximize μ = min_{non-adjacent A,B} |N_G(A) ∩ N_G(B)|. If the graph is not regular, some vertices have higher degree, which means more common neighbors on average but also the formula changes.

Let me reconsider. If G has min degree ≥ 300 but is not regular, the formula for |M(A) ∩ M(B)| changes. Let me redo the analysis for non-regular graphs.

For non-adjacent A, B: |M(A) ∩ M(B)| = |M(A)| + |M(B)| - |M(A) ∪ M(B)|. |M(A)| = 999 - deg(A), |M(B)| = 999 - deg(B). |M(A) ∪ M(B)| ≤ 1000. So |M(A) ∩ M(B)| ≥ 999 - deg(A) + 999 - deg(B) - 1000 = 998 - deg(A) - deg(B).

If deg(A) = deg(B) = 300: ≥ 398.
If deg(A) = 301, deg(B) = 300: ≥ 397.

So having higher degree vertices decreases the lower bound. The adversary wants to maximize the minimum, so they should use 300-regular.

But wait, the actual value of |M(A) ∩ M(B)| could be higher than the lower bound. The lower bound is 998 - deg(A) - deg(B), but the actual value is 998 - deg(A) - deg(B) + |N_G(A) ∩ N_G(B)| (for non-adjacent A, B). So:

|M(A) ∩ M(B)| = (998 - deg(A) - deg(B)) + |N_G(A) ∩ N_G(B)|

for non-adjacent A, B. (Let me verify: |M(A) ∩ M(B)| = |M(A)| + |M(B)| - |M(A) ∪ M(B)| = (999 - d_A) + (999 - d_B) - (1000 - |N_G(A) ∩ N_G(B)|) = 998 - d_A - d_B + |N_G(A) ∩ N_G(B)|. ✓)

For adjacent A, B: |M(A) ∩ M(B)| = (999 - d_A) + (999 - d_B) - (1000 - |N_G(A) ∩ N_G(B)| - 2) = 1000 - d_A - d_B + |N_G(A) ∩ N_G(B)|.

So for non-adjacent: |M(A) ∩ M(B)| = 998 - d_A - d_B + cn(A,B) where cn(A,B) = |N_G(A) ∩ N_G(B)|.
For adjacent: |M(A) ∩ M(B)| = 1000 - d_A - d_B + cn(A,B).

If the graph is 300-regular: non-adjacent: 398 + cn. Adjacent: 400 + cn. The minimum is from non-adjacent pairs: 398 + min_{non-adj} cn = 398 + μ.

If the graph is not regular, say some vertex has degree 301: for a non-adjacent pair (A, B) with d_A = 301, d_B = 300: |M(A) ∩ M(B)| = 397 + cn(A,B). Even if cn(A,B) is large, the base is 397, which is less than 398. So the minimum could be lower.

But cn(A,B) could be larger for higher-degree vertices. If d_A = 301, A has more neighbors, so potentially more common neighbors with B. The question is whether the increase in cn compensates for the decrease in the base.

For a non-adjacent pair (A, B) with d_A = 301, d_B = 300: cn(A,B) ≤ min(d_A, d_B) = 300. So |M(A) ∩ M(B)| ≤ 397 + 300 = 697. And ≥ 397 + 0 = 397. 

For a 300-regular graph, the minimum is 398 + μ. For a graph with some degree-301 vertices, the minimum could be as low as 397 + cn for those pairs. If cn is at least μ + 1 for those pairs, then the minimum is still ≥ 398 + μ. But this requires the higher-degree vertices to have more common neighbors, which might not hold.

I think for simplicity, the adversary should use 300-regular, and the answer is 602 - μ where μ is the maximum min-common-neighborhood for non-adjacent pairs in a 300-regular graph on 1000 vertices.

Now, let me think about whether μ = 128 is achievable. This is the key question.

Actually, let me reconsider the upper bound. I showed μ ≤ 128 using the average over non-adjacent pairs, assuming T = 0. But if T > 0, the bound is even lower. So μ ≤ 128 regardless.

But is μ = 128 achievable? This requires a triangle-free 300-regular graph on 1000 vertices where every non-adjacent pair has ≥ 128 common neighbors.

In such a graph, for each vertex A, the 699 non-neighbors have common neighborhoods summing to 89700, with each ≥ 128. 128 * 699 = 89472, and 89700 - 89472 = 228. So the "excess" is 228, meaning 228 non-neighbors have 129 common neighbors and 471 have 128 (or some other distribution).

This is a very tight constraint. The graph would need to be almost like a "perfect" structure.

Let me think about whether such a graph can exist. Consider the adjacency matrix approach. In a triangle-free d-regular graph, for non-adjacent A, B, cn(A,B) = (A^2)_{A,B} where A is the adjacency matrix. (A^2)_{A,B} = number of walks of length 2 from A to B = cn(A,B) for A ≠ B (since triangle-free means no edge A-B, so all length-2 walks go through common neighbors). For adjacent A, B, (A^2)_{A,B} = cn(A,B) as well, but in a triangle-free graph, cn(A,B) = 0 for adjacent pairs (since a common neighbor would form a triangle).

So in a triangle-free 300-regular graph: A^2 has diagonal entries = 300 (degree), off-diagonal entries = cn(A,B) for non-adjacent pairs and 0 for adjacent pairs. So A^2 = 300I + (matrix of cn values on non-edges).

The eigenvalues of A are 300 (trivial), and others. A^2 has eigenvalue 300^2 = 90000 for the trivial eigenvector, and for other eigenvectors, eigenvalue = (eigenvalue of A)^2.

This is getting quite involved. Let me try a different approach and think about specific constructions.

Construction: Let G be a 300-regular graph on 1000 vertices that's a "blow-up" or algebraic construction.

Consider the following: take Z_1000 (cyclic group of order 1000). Connect vertex i to vertices i ± 1, i ± 2, ..., i ± 150 (a circulant graph). This gives degree 300. Is it triangle-free? No, since i is connected to i+1 and i+2, and i+1 is connected to i+2 (if 1 is in the connection set). So there are triangles.

For a triangle-free circulant graph, we need the connection set S (with S = -S, |S| = 300) to be "sum-free" in the sense that there's no solution to a + b = c with a, b, c ∈ S (mod 1000). This is a Sidon set or sum-free set condition. A sum-free set in Z_1000 of size 300... by the theory of sum-free sets, the maximum size of a sum-free set in Z_n is about n/3. For n = 1000, that's about 333. So a sum-free set of size 150 (giving degree 300 with S = -S) might be possible. But I'm not sure about the common neighborhood properties.

This is getting very complicated. Let me try to think about the problem from a higher level and see if there's a cleaner argument.

Actually, let me reconsider the problem statement. "What is the minimum possible value of the maximum number of participants max_{A,B} V that the city can guarantee for some choice of candidates A and B?"

I interpreted this as: min over graphs G (min degree ≥ 300) of max over A,B of V(G, A, B). The city chooses the graph to minimize the best-case participation.

But maybe the interpretation is different. Let me re-read: "the minimum possible value of the maximum number of participants max_{A,B} V that the city can guarantee for some choice of candidates A and B."

Hmm, "that the city can guarantee for some choice of candidates A and B" — this means the city can guarantee that there EXISTS a choice of A, B with V ≥ (some value). The city wants to guarantee a high value. The "minimum possible value" is over all possible acquaintance structures.

So: min_G max_{A,B} V(G, A, B) where G has min degree ≥ 300 on 1000 vertices. This is what I had.

OK so let me think about this more carefully. Let me consider the possibility that the answer is 600.

If the answer is 600, then the adversary can achieve max V = 600, meaning min |M(A) ∩ M(B)| = 400. For 300-regular G, this means 398 + μ = 400, so μ = 2. Every non-adjacent pair has ≥ 2 common neighbors.

But we showed μ can be up to 128 (in principle). So if μ = 128 is achievable, the answer would be 602 - 128 = 474. That seems too low.

Hmm wait, let me re-examine. If μ = 128, then min |M(A) ∩ M(B)| = 398 + 128 = 526, and max V = 1000 - 526 = 474. The adversary would achieve max V = 474, which is much better (lower) than 602.

But is μ = 128 achievable? Let me think about this more carefully.

Actually, I realize I should think about whether a triangle-free 300-regular graph on 1000 vertices with μ = 128 can exist. The key constraint is that for every vertex A, the 300 neighbors of A form an independent set, and the 699 non-neighbors each share 128 or 129 neighbors with A.

Let me think about the bipartite case more carefully. In a 300-regular bipartite graph on 500+500, for same-part non-adjacent pairs, cn(A,B) = |N_G(A) ∩ N_G(B)| where both neighborhoods are in the other part (size 500). cn(A,B) = 300 + 300 - |N_G(A) ∪ N_G(B)| ≥ 600 - 500 = 100. So μ_same ≥ 100 for same-part pairs. But μ_cross = 0 for cross-part non-adjacent pairs. So overall μ = 0.

To fix the cross-part issue, we need a non-bipartite graph. But non-bipartite triangle-free graphs have odd cycles, which might reduce the common neighborhood for some pairs.

Let me think about a different construction. Consider a graph on 1000 vertices partitioned into groups, with a structured connection pattern.

Actually, let me think about the problem from the perspective of the complement graph H. H is 699-regular on 1000 vertices. We want to maximize min_{A≠B} |N_H(A) ∩ N_H(B)|.

For adjacent A, B in H: |N_H(A) ∩ N_H(B)| = 1398 - |N_H(A) ∪ N_H(B)|. Since A ∈ N_H(B) and B ∈ N_H(A), |N_H(A) ∪ N_H(B)| ≤ 1000. So ≥ 398.

For non-adjacent A, B in H: |N_H(A) ∪ N_H(B)| ≤ 998. So |N_H(A) ∩ N_H(B)| ≥ 400.

The minimum is from adjacent pairs in H (non-adjacent in G). We want to maximize this minimum, i.e., make |N_H(A) ∪ N_H(B)| as small as possible for all adjacent pairs.

|N_H(A) ∪ N_H(B)| = 1000 - |{v : v ∉ N_H(A), v ∉ N_H(B)}| = 1000 - |{v : v ∈ M(A) ∩ M(B) in terms of H}|... wait, I need to be careful. In H, the "non-neighbors" of A (excluding A) are the neighbors of A in G. So {v : v ∉ N_H(A), v ≠ A} = N_G(A) ∪ {A}... no. {v ≠ A : v ∉ N_H(A)} = {v ≠ A : v is not a neighbor of A in H} = {v ≠ A : v is a neighbor of A in G or v = A}... hmm, v ≠ A, so {v ≠ A : v ∉ N_H(A)} = N_G(A) (since the complement of N_H(A) in V \ {A} is N_G(A)).

So {v : v ∉ N_H(A) and v ∉ N_H(B)} = (V \ ({A} ∪ N_H(A))) ∩ (V \ ({B} ∪ N_H(B))) = (N_G(A) ∪ {A}) ∩ ... wait, V \ ({A} ∪ N_H(A)) = {A} ∪ N_G(A)? No. V = {A} ∪ N_H(A) ∪ N_G(A) (where N_G(A) are the neighbors of A in G, which are the non-neighbors of A in H, excluding A). Wait, V \ ({A} ∪ N_H(A)) = N_G(A). Because V = {A} ∪ N_H(A) ∪ N_G(A) (partition: A itself, H-neighbors, G-neighbors). So V \ ({A} ∪ N_H(A)) = N_G(A).

Similarly, V \ ({B} ∪ N_H(B)) = N_G(B).

So {v : v ∉ N_H(A) and v ∉ N_H(B)} = N_G(A) ∩ N_G(B) \ ... hmm, we need v ∉ N_H(A) and v ∉ N_H(B). v ∉ N_H(A) means v ∈ V \ N_H(A) = {A} ∪ N_G(A). v ∉ N_H(B) means v ∈ {B} ∪ N_G(B). So v ∈ ({A} ∪ N_G(A)) ∩ ({B} ∪ N_G(B)).

If A, B are adjacent in H (non-adjacent in G): A ∉ N_G(B), B ∉ N_G(A). So ({A} ∪ N_G(A)) ∩ ({B} ∪ N_G(B)) = (N_G(A) ∩ N_G(B)) ∪ (N_G(A) ∩ {B}) ∪ ({A} ∩ N_G(B)) ∪ ({A} ∩ {B}). N_G(A) ∩ {B} = ∅ (B ∉ N_G(A)). {A} ∩ N_G(B) = ∅ (A ∉ N_G(B)). {A} ∩ {B} = ∅. So = N_G(A) ∩ N_G(B).

So |{v : v ∉ N_H(A) and v ∉ N_H(B)}| = |N_G(A) ∩ N_G(B)| = cn_G(A,B) (common neighbors in G for non-adjacent A, B in G).

|N_H(A) ∪ N_H(B)| = 1000 - cn_G(A,B).

|N_H(A) ∩ N_H(B)| = 1398 - (1000 - cn_G(A,B)) = 398 + cn_G(A,B). ✓ (consistent with before).

So to maximize min |N_H(A) ∩ N_H(B)|, we maximize min over edges in H of (398 + cn_G(A,B)), i.e., maximize min over non-edges in G of cn_G(A,B) = μ.

And the answer is 1000 - (398 + μ) = 602 - μ.

Now, the key question: what is the maximum μ?

Let me think about this more carefully with a focus on finding the exact value.

Upper bound: μ ≤ 128 (from the averaging argument, achieved when T = 0).

But is this tight? Let me think about whether a triangle-free 300-regular graph on 1000 vertices with μ = 128 exists.

Actually, I realize that the bound μ ≤ 128 might not be tight. Let me think about additional constraints.

In a triangle-free 300-regular graph, for each vertex A, N_G(A) is an
