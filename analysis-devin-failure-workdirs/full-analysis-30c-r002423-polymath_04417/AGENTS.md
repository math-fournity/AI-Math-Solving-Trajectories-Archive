# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   We have a group of $n$ kids. For each pair of kids, at least one has sent a message to the other one. For each kid $A$, among the kids to whom $A$ has sent a message, exactly $25 \%$ have sent a message to $A$. How many possible two-digit values of $n$ are there?       — 题目文本
#   If the number of pairs of kids with two-way communication is $k$, then by the given condition the total number of messages is $4 k+4 k=8 k$. Thus the number of pairs of kids is $\frac{n(n-1)}{2}=7 k$. This is possible only if $n \equiv 0,1 \bmod 7$.

- In order to obtain $n=7 m+1$, arrange the kids in a circle and let each kid send a message to the first $4 m$ kids to its right and hence receive a message from the first $4 m$ kids to its left. Thus there are exactly $m$ kids to which it has both sent and received messages.
- In order to obtain $n=7 m$, let kid $X$ send no messages (and receive from every other kid). Arrange the remaining $7 m-1$ kids in a circle and let each kid on the circle send a message to the first $4 m-1$ kids to its right and hence receive a message from the first $4 m-1$ kids to its left. Thus there are exactly $m$ kids to which it has both sent and received messages.

There are 26 two-digit numbers with remainder 0 or 1 modulo 7 . (All numbers of the form $7 m$ and $7 m+1$ with $2 \leqslant m \leqslant 14$.)

Alternative Solution by PSC. Suppose kid $x_{i}$ sent $4 d_{i}$ messages. (Guaranteed by the conditions to be a multiple of 4.) Then it received $d_{i}$ messages from the kids that it has sent a message to, and another $n-1-4 d_{i}$ messages from the rest of the kids. So it received a total of $n-1-3 d_{i}$ messages. Since the total number of messages sent is equal to the total number of messages received, we must have:

$$
d_{1}+\cdots+d_{n}=\left(n-1-3 d_{1}\right)+\cdots+\left(n-1-3 d_{n}\right)
$$

This gives $7\left(d_{1}+\cdots+d_{n}\right)=n(n-1)$ from which we get $n \equiv 0,1 \bmod 7$ as in the first solution.

We also present an alternative inductive construction (which turns out to be different from the construction in the first solution).

For the case $n \equiv 0 \bmod 7$, we start with a construction for $7 k$ kids, say $x_{1}, \ldots, x_{7 k}$, and another construction with 7 kids, say $y_{1}, \ldots, y_{7}$. We merge them by demanding that in addition, each kid $x_{i}$ sends and receives gifts according to the following table:

| $i \bmod 7$ | Sends | Receives |
| :---: | :---: | :---: |
| 0 | $y_{1}, y_{2}, y_{3}, y_{4}$ | $y_{4}, y_{5}, y_{6}, y_{7}$ |
| 1 | $y_{2}, y_{3}, y_{4}, y_{5}$ | $y_{5}, y_{6}, y_{7}, y_{1}$ |
| 2 | $y_{3}, y_{4}, y_{5}, y_{6}$ | $y_{6}, y_{7}, y_{1}, y_{2}$ |
| 3 | $y_{4}, y_{5}, y_{6}, y_{7}$ | $y_{7}, y_{1}, y_{2}, y_{3}$ |
| 4 | $y_{5}, y_{6}, y_{7}, y_{1}$ | $y_{1}, y_{2}, y_{3}, y_{4}$ |
| 5 | $y_{6}, y_{7}, y_{1}, y_{2}$ | $y_{2}, y_{3}, y_{4}, y_{5}$ |
| 6 | $y_{7}, y_{1}, y_{2}, y_{3}$ | $y_{3}, y_{4}, y_{5}, y_{6}$ |

So each kid $x_{i}$ sends an additional four messages and receives a message from only one of those four additional kids. Also, each kid $y_{j}$ sends an additional $4 k$ messages and receives from exactly $k$ of those additional kids. So this is a valid construction for $7(k+1)$ kids.

For the case $n \equiv 1 \bmod 7$, we start with a construction for $7 k+1$ kids, say $x_{1}, \ldots, x_{7 k+1}$, and we take another 7 kids, say $y_{1}, \ldots, y_{7}$ for which we do not yet mention how they exchange gifts. The kids $x_{1}, \ldots, x_{7 k+1}$ exchange gifts with the kids $y_{1}, \ldots, y_{7}$ according to the previous table. As before, each kid $x_{i}$ satisfies the conditions. We now put $y_{1}, \ldots, y_{7}$ on a circle and demand that each of $y_{1}, \ldots, y_{3}$ sends gifts to the next four kids on the circle and each of $y_{4}, \ldots, y_{7}$ sends gifts to the next three kids on the circle. It is each to check that the condition is satisfied by each $y_{i}$ as well.  — 标准解答
#   Let me solve this problem. We have n kids. For each pair, at least one has sent a message to the other. For each kid A, among the kids A sent messages to, exactly 25% have sent a message back to A.

Let me model this as a directed graph. Each kid is a vertex. For each pair {A,B}, at least one of A→B or B→A exists (could be both - mutual). For each vertex A: let d_out(A) = number of kids A sent messages to. Among these d_out(A) kids, exactly 25% sent a message back to A. So the number of kids B such that both A→B and B→A exist is exactly d_out(A)/4. This means d_out(A) is divisible by 4. Let d_out(A) = 4k_A for some integer k_A. The number of mutual connections from A's perspective is k_A. Let me define: for each ordered pair, we have a directed edge. Let M = number of mutual pairs (unordered pairs where both directions exist). Let S = number of single-direction pairs (unordered pairs where exactly one direction exists). Total unordered pairs = M + S = C(n,2). For each vertex A, d_out(A) = out-degree. The number of mutual neighbors of A (kids B where both A→B and B→A) = k_A = d_out(A)/4.

The number of mutual pairs M = (1/2) * sum over A of k_A = (1/2) * sum d_out(A)/4 = (1/8) * sum d_out(A).

Also, sum d_out(A) = total directed edges = S + 2M (each single pair contributes 1 edge, each mutual contributes 2).

So sum d_out(A) = S + 2M.

And M = (1/8)(S + 2M), so 8M = S + 2M, thus S = 6M.

Total pairs: M + S = M + 6M = 7M = C(n,2) = n(n-1)/2.

So n(n-1)/2 = 7M, meaning n(n-1) = 14M.

So n(n-1) ≡ 0 (mod 14), i.e., 14 | n(n-1).

Since gcd(n, n-1) = 1, we need 2 | n(n-1) (always true) and 7 | n(n-1). So 7 | n or 7 | (n-1), i.e., n ≡ 0 or 1 (mod 7).

Now we also need d_out(A) divisible by 4 for each A, and the structure to be realizable.

Wait, but we need more constraints. The condition is that for each A, exactly 25% of A's out-neighbors have sent a message back. We derived n ≡ 0 or 1 (mod 7) as necessary. But is it sufficient? We need to check that for each such n, there exists a valid configuration.

Let me think about sufficiency. We need to construct, for each n ≡ 0 or 1 (mod 7) with n being a two-digit number (10 ≤ n ≤ 99), a directed graph satisfying the conditions.

Actually, let me think more carefully. We need each vertex to have d_out(A) ≡ 0 (mod 4), and the mutual structure to work out.

Let me think about this differently. Consider the structure where we partition into groups.

Actually, let me think about a concrete construction. Consider a tournament-like structure but with some mutual edges.

Let me think about the problem more carefully. We have a "semi-complete" digraph (for each pair, at least one direction). For each vertex v, out-degree d(v), and the number of vertices u with both v→u and u→v is exactly d(v)/4.

Let me think of a construction. Take n ≡ 0 (mod 7), say n = 7m. Partition the n kids into 7 groups of m each: G_0, G_1, ..., G_6.

Define the edges as follows: for groups G_i and G_j (i ≠ j), if (j - i) mod 7 ∈ {1, 2, 3}, then all edges go from G_i to G_j (i.e., every kid in G_i sends to every kid in G_j). If (j - i) mod 7 ∈ {4, 5, 6}, then all edges go from G_j to G_i.

Within each group G_i, make all edges mutual (every kid sends to every other kid in the same group).

This is like a regular tournament on 7 groups, where the "tournament" is the cyclic tournament on 7 vertices, plus mutual edges within groups.

Now let's check: for a kid A in group G_i:
- Out-neighbors: all kids in G_i (except A itself) = m-1, plus all kids in groups G_j where (j-i) mod 7 ∈ {1,2,3} = 3m.
- So d_out(A) = (m-1) + 3m = 4m - 1.

Hmm, that's 4m - 1, which is not divisible by 4 in general. Let me reconsider.

The mutual neighbors of A: kids B where both A→B and B→A. This happens only within G_i (since between groups, edges are one-directional). So mutual neighbors = m - 1.

We need mutual neighbors = d_out(A)/4 = (4m-1)/4. This requires 4 | (4m-1), which is impossible since 4m-1 ≡ 3 (mod 4).

So this construction doesn't work directly. Let me adjust.

The issue is the within-group edges. Let me try making within-group edges one-directional too, following the cyclic tournament pattern extended.

Actually, let me reconsider. Let me think of the whole thing as a regular tournament on n vertices where n ≡ 0 or 1 (mod 7)... no wait, tournaments don't have mutual edges.

Let me reconsider the problem. We need a mixed graph (some pairs mutual, some single). Let me think about what configurations work.

Let me reconsider. The key equation is n(n-1) = 14M, so M = n(n-1)/14. For M to be a positive integer, we need 14 | n(n-1), giving n ≡ 0 or 1 (mod 7).

But we also need the per-vertex conditions to be satisfiable. Let me think about whether there are additional constraints.

For each vertex A: d_out(A) = 4k_A, and A has exactly k_A mutual neighbors. The sum of k_A over all A = 2M = n(n-1)/7.

The sum of d_out(A) = S + 2M = 6M + 2M = 8M = 8n(n-1)/14 = 4n(n-1)/7.

Average d_out = 4(n-1)/7. Average k = (n-1)/7.

For this to make sense, we need (n-1)/7 to be a non-negative integer on average, but individual vertices can vary.

Actually, let me think about whether we can always construct such a graph when n ≡ 0 or 1 (mod 7).

Case 1: n ≡ 1 (mod 7), say n = 7m + 1.

Consider a regular tournament on n vertices. A regular tournament on n vertices (n odd) has each vertex with out-degree (n-1)/2. But we need mutual edges...

Let me think differently. Let me consider a construction based on a "regular" structure.

Let me try: n = 7m + 1. Take the cyclic group Z_n. For each pair {i, j}, define the edge structure based on the difference d = (j - i) mod n.

In a Paley-like tournament: for n ≡ 1 (mod 7)... hmm, this is getting complicated.

Let me try a different approach. Let me think about small cases and see if the construction works.

For n = 7: M = 7·6/14 = 3. S = 18. Each vertex: average d_out = 4·6/7 = 24/7, which is not an integer. So we can't have all vertices with the same out-degree. But the problem doesn't require regular out-degree.

For n = 7, we need sum d_out = 4·7·6/7 = 24, and sum k_A = 2·3 = 6. Each d_out(A) ≡ 0 (mod 4), so d_out(A) ∈ {0, 4, 8, 12, ...}. With 7 vertices and sum 24, possible distributions: e.g., six vertices with d_out = 4 and one with d_out = 0. Sum = 24. ✓

Then k_A = d_out(A)/4, so six vertices with k=1 and one with k=0. Sum k = 6 = 2M. ✓

Can we realize this? We need 3 mutual pairs and 18 single edges. The vertex with d_out = 0 has no out-edges, so all its edges are incoming (6 incoming single edges). It has k=0, so no mutual edges involving it.

The other 6 vertices each have d_out = 4 and k = 1 (one mutual neighbor). Among the 6 vertices (excluding the special one), there are C(6,2) = 15 pairs. The 3 mutual pairs are among these 6 vertices. Each of the 6 vertices is in exactly 1 mutual pair, so the 3 mutual pairs form a perfect matching on the 6 vertices. ✓

Each of the 6 vertices has d_out = 4. One out-edge goes to its mutual partner. The other 3 out-edges go to... other vertices. Each vertex has 5 possible neighbors among the other 5 non-special vertices, plus the special vertex. The special vertex has no out-edges, so the edge between a non-special vertex and the special vertex is single, directed from non-special to special. So each non-special vertex has 1 out-edge to the special vertex.

So out-edges from a non-special vertex A: 1 to special vertex, 1 to mutual partner, and 2 more to other non-special vertices. Total = 4. ✓

Among the 6 non-special vertices, after removing the 3 mutual pairs, we have 15 - 3 = 12 pairs, each single-direction. Each vertex has 4 other non-special non-partner vertices, and needs 2 out-edges among them. So we need a tournament on 6 vertices (the non-partner edges) where each vertex has out-degree 2. That's a regular tournament on 6 vertices... but 6 is even, so a regular tournament doesn't exist (regular tournaments need odd number of vertices).

Wait, let me recount. Each non-special vertex A has 5 other non-special vertices. One is its mutual partner (1 out-edge). The remaining 4 are connected by single edges. A needs 2 out-edges among these 4. So we need an orientation of K_6 minus a perfect matching where each vertex has out-degree 2. K_6 minus a perfect matching is a 4-regular graph on 6 vertices. We need to orient it so each vertex has out-degree 2, i.e., a regular orientation (Eulerian orientation). This exists for any even-degree regular graph. ✓ (A 4-regular graph has an Eulerian circuit, and orienting along the circuit gives out-degree = in-degree = 2 at each vertex.)

So n = 7 works.

Now, the question is: for which two-digit n (10 ≤ n ≤ 99) with n ≡ 0 or 1 (mod 7) can we construct a valid configuration?

Two-digit values with n ≡ 0 (mod 7): 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98.
Two-digit values with n ≡ 1 (mod 7): 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99.

Wait, let me list them:
n ≡ 0 (mod 7): 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98 → 13 values
n ≡ 1 (mod 7): 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99 → 13 values

Total: 26 values.

But I need to verify that each of these can actually be realized. The necessary condition is n ≡ 0 or 1 (mod 7), but there might be additional constraints from the divisibility by 4 requirement.

Let me think about whether there are additional constraints. We need each d_out(A) ≡ 0 (mod 4). The sum of d_out = 4n(n-1)/7. For this to be achievable with each d_out ≡ 0 (mod 4), we need... well, the sum is already divisible by 4 (it's 4 times something). So as long as we can distribute the out-degrees appropriately, it should work.

But we also need 0 ≤ d_out(A) ≤ n-1 for each vertex, and d_out(A) ≡ 0 (mod 4), and the graph structure to be realizable.

Let me think about this more carefully. The average out-degree is 4(n-1)/7. For n = 7m, average = 4(7m-1)/7 = 4m - 4/7. For n = 7m+1, average = 4·7m/7 = 4m.

For n = 7m+1: average out-degree = 4m, which is divisible by 4. So we could try a regular construction where every vertex has d_out = 4m and k = m.

For n = 7m: average out-degree = 4m - 4/7, not an integer. So we can't have all vertices with the same out-degree. We need some variation.

Let me think about the n = 7m+1 case first, as it seems cleaner.

**Case n = 7m + 1:**

We want a regular structure where every vertex has d_out = 4m and k = m (m mutual neighbors).

Consider Z_n = Z_{7m+1}. Define the edge structure using a "difference set" approach.

For each unordered pair {i, j}, let d = (j - i) mod n (taking the representative in {1, 2, ..., n-1}, and also considering n - d). We need to decide: is the edge i→j, j→i, or both?

We want: for each vertex i, exactly 4m out-neighbors and m mutual neighbors.

Think of it as: partition the non-zero residues mod n into "out-differences" D_out (i sends to i+d for d ∈ D_out), "in-differences" D_in (i receives from i+d, i.e., j→i where d = i-j... let me be more careful).

Let me use the standard approach. For vertex i, define:
- Out-neighbors: {i + d mod n : d ∈ D_out} where D_out is a subset of {1, ..., n-1}.
- For the edge between i and j (j = i + d), it's mutual iff both d ∈ D_out and -d ∈ D_out (i.e., n-d ∈ D_out).

Wait, let me set it up properly. We work in Z_n. For each pair {i, j} with difference d = j - i (mod n), we choose one of three options:
1. i → j only (d ∈ D_out, -d ∉ D_out)
2. j → i only (-d ∈ D_out, d ∉ D_out)
3. Both (d ∈ D_out and -d ∈ D_out)

where D_out is the set of "out-differences" and the construction is vertex-transitive: vertex i sends to i + d for all d ∈ D_out.

For this to be well-defined, for each pair {d, -d}, we need to decide. Let's say:
- If d ∈ D_out and -d ∈ D_out: mutual edges for difference d.
- If d ∈ D_out and -d ∉ D_out: edge goes in direction of d (i → i+d).
- If d ∉ D_out and -d ∈ D_out: edge goes in direction of -d.
- If d ∉ D_out and -d ∉ D_out: impossible (no edge), but we need at least one edge per pair.

So we need: for each pair {d, -d} with d ≠ 0, at least one of d, -d is in D_out.

|D_out| = d_out for each vertex = 4m.

Mutual neighbors: for each d ∈ D_out with -d ∈ D_out, vertex i has a mutual edge with i+d. The number of such d is the number of d ∈ D_out with -d ∈ D_out. Since the construction is symmetric, this equals |D_out ∩ (-D_out)|. We need this to be m.

Also, |D_out| = 4m, and D_out ∪ (-D_out) = {1, ..., n-1} \ {d : d ∉ D_out and -d ∉ D_out}. But we need D_out ∪ (-D_out) = {1, ..., n-1} (every pair has at least one edge). So |D_out ∪ (-D_out)| = n - 1 = 7m.

|D_out ∪ (-D_out)| = |D_out| + |-D_out| - |D_out ∩ (-D_out)| = 4m + 4m - m = 7m. ✓

So we need a subset D_out of Z_n \ {0} with:
- |D_out| = 4m
- |D_out ∩ (-D_out)| = m
- D_out ∪ (-D_out) = Z_n \ {0}

The last condition means every non-zero residue is in D_out or its negative is. The second condition means exactly m elements d of D_out have -d also in D_out (these come in pairs {d, -d}, so there are m/2 such pairs if m is even, or... wait).

Hmm, |D_out ∩ (-D_out)| = m. The elements in D_out ∩ (-D_out) are those d where both d and -d are in D_out. These come in pairs {d, -d} (unless d = -d, i.e., d = n/2, which requires n even). For n = 7m+1:
- If m is even, n = 7m+1 is odd, so no self-inverse element. The m elements in D_out ∩ (-D_out) form m/2 pairs. So m must be even.
- If m is odd, n = 7m+1 is even, so n/2 = (7m+1)/2 is an integer. The element n/2 is self-inverse. So D_out ∩ (-D_out) could include n/2 (contributing 1) plus (m-1)/2 pairs. So m can be odd.

Wait, but actually we need to be more careful. Let me reconsider.

The pairs {d, -d} partition Z_n \ {0} into (n-1)/2 pairs if n is odd, or (n-2)/2 pairs plus the singleton {n/2} if n is even.

For n = 7m+1:
- n odd iff m even. Then (n-1)/2 = 7m/2 pairs. We need m elements in D_out ∩ (-D_out), forming m/2 complete pairs (both d and -d in D_out). The remaining 7m/2 - m/2 = 3m pairs have exactly one element in D_out. Total |D_out| = m + 3m = 4m. ✓ Need m even.
- n even iff m odd. Then (n-2)/2 = (7m-1)/2 pairs plus singleton {n/2}. We need m elements in D_out ∩ (-D_out). If n/2 ∈ D_out, it contributes 1 (self-paired). Then we need (m-1)/2 complete pairs. Remaining pairs: (7m-1)/2 - (m-1)/2 = 3m pairs with one element each. Total |D_out| = 1 + (m-1) + 3m = 4m. ✓ Need m odd (and n/2 ∈ D_out).

OR if n/2 ∉ D_out: then we need m/2 complete pairs, requiring m even. But m is odd here, contradiction. So for m odd, we must include n/2 ∈ D_out.

So for n = 7m+1:
- m even: construction possible (need m/2 mutual-difference pairs and 3m single-difference pairs).
- m odd: construction possible (include n/2, plus (m-1)/2 mutual-difference pairs and 3m single-difference pairs).

So it seems like for all m ≥ 1, the construction is possible for n = 7m+1. We just need to verify that we can always choose the right number of pairs.

For m even (n odd): we need to choose m/2 out of 7m/2 pairs to be "mutual" (both directions), and from the remaining 3m pairs, choose one element each for D_out. This is always possible as long as m/2 ≤ 7m/2, which is true for m ≥ 0.

For m odd (n even): include n/2 in D_out, choose (m-1)/2 out of (7m-1)/2 pairs to be mutual, and from remaining 3m pairs choose one each. Always possible.

So for n = 7m+1, the construction works for all m ≥ 1, i.e., n ≥ 8. Since we need two-digit n, n ≥ 10, so all n = 7m+1 with n ≥ 10 work.

Two-digit n ≡ 1 (mod 7): 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99. All work.

**Case n = 7m:**

Average out-degree = 4(7m-1)/7 = 4m - 4/7. Not an integer, so we can't have a regular construction.

We need sum d_out = 4n(n-1)/7 = 4·7m·(7m-1)/7 = 4m(7m-1) = 28m² - 4m.

Each d_out ≡ 0 (mod 4). Sum = 28m² - 4m = 4(7m² - m). So sum/4 = 7m² - m = m(7m-1).

We need n = 7m vertices, each with d_out ≡ 0 (mod 4), summing to 4m(7m-1).

Average d_out = 4m(7m-1)/(7m) = 4(7m-1)/7 = 4m - 4/7.

So some vertices have d_out = 4m and some have d_out = 4m - 4 (or other multiples of 4).

If x vertices have d_out = 4m and (7m - x) have d_out = 4(m-1) = 4m - 4:
Sum = x·4m + (7m-x)·(4m-4) = 4mx + 28m² - 4m·7m + 4x - 28m + 4·7m... let me redo.

Sum = x·4m + (7m-x)·(4m-4) = 4mx + (7m)(4m-4) - x(4m-4) = 4mx + 28m² - 28m - 4mx + 4x = 28m² - 28m + 4x.

We need this = 28m² - 4m. So 28m² - 28m + 4x = 28m² - 4m, giving 4x = 24m, x = 6m.

So 6m vertices with d_out = 4m and m vertices with d_out = 4m - 4 = 4(m-1).

Check: 6m + m = 7m = n. ✓

For the 6m vertices with d_out = 4m: k = m.
For the m vertices with d_out = 4(m-1): k = m-1.

Sum of k = 6m·m + m·(m-1) = 6m² + m² - m = 7m² - m = m(7m-1). And 2M = n(n-1)/7 = 7m(7m-1)/7 = m(7m-1). ✓

Now, can we construct such a graph? This is more complex. Let me think about a construction.

Consider 7 groups: G_0, ..., G_6, each of size m. Use the cyclic tournament structure on the groups (group i beats group j if (j-i) mod 7 ∈ {1,2,3}), and within groups, use a specific structure.

For a vertex in group G_i:
- Out-edges to other groups: 3m (groups G_{i+1}, G_{i+2}, G_{i+3}).
- Out-edges within G_i: need to determine.

For the 6m vertices with d_out = 4m: out-edges within group = 4m - 3m = m. So within a group of m vertices, each of these vertices has m out-edges within the group. But there are only m-1 other vertices in the group! So m out-edges within the group is impossible (max is m-1).

Hmm, that doesn't work. Let me reconsider.

Wait, maybe the within-group edges should be mutual for some and the cross-group edges should also have some mutual ones.

Let me reconsider the construction. Maybe I should allow some cross-group mutual edges.

Actually, let me reconsider. The issue is that with the cyclic tournament on 7 groups, each vertex has 3m out-edges to other groups and needs 4m total (or 4m-4 for some). The within-group contribution is m (or m-4). With m-1 other vertices in the group, m out-edges is too many.

So the pure cyclic tournament approach doesn't directly work for n = 7m. Let me think of another construction.

Alternative: use a different group structure. Let me think about n = 7m where we use a vertex-transitive construction on Z_{7m}.

Hmm, but the average out-degree isn't an integer, so vertex-transitive won't work.

Let me think about this differently. Maybe use a construction based on Z_{7m} but not vertex-transitive.

Actually, let me think about it as follows. Consider Z_{7m} = Z_7 × Z_m (since gcd(7, m) might not be 1, this isn't always a product, but let me think of it as 7 blocks of m consecutive elements).

Actually, let me try a different approach. Let me consider the problem on Z_n where n = 7m, and use a "near-regular" construction.

Let me define D_out as a subset of Z_{7m} \ {0} with |D_out| = 4m for most vertices but adjusted for some.

This is getting complicated. Let me try a different approach entirely.

Let me think about it as a "blow-up" construction. Take the n=7 construction (which we verified works) and blow it up.

For n = 7: we had 6 vertices with d_out = 4, k = 1, and 1 vertex with d_out = 0, k = 0. The 6 vertices form 3 mutual pairs, and the remaining edges among the 6 form a regular tournament on K_6 minus a perfect matching.

To blow up to n = 7m: replace each vertex v with a group of m vertices. Replace each single edge u→v with all m² edges from group(u) to group(v). Replace each mutual edge u↔v with all m² mutual edges between group(u) and group(v). Within each group, we need to define edges.

For a vertex in a group corresponding to a vertex with d_out = 4 in the base:
- Out-edges to other groups: 4m (from the 4 out-edges of the base vertex, each blown up to m).
- Within group: m-1 other vertices. We need total d_out = 4m, so within-group out-edges = 0. But we need at least one edge per pair within the group!

So within each group, we need to orient the complete graph on m vertices. If we make all within-group edges single (tournament), each vertex has some out-degree within the group. This adds to the total out-degree.

For a vertex in a "d_out = 4" group: cross-group out-edges = 4m. Within-group out-edges = some value t (0 ≤ t ≤ m-1). Total d_out = 4m + t. We need this ≡ 0 (mod 4), so t ≡ 0 (mod 4).

For a vertex in the "d_out = 0" group: cross-group out-edges = 0. Within-group out-edges = t. Total d_out = t. Need t ≡ 0 (mod 4).

Also, mutual neighbors: for a vertex in a "d_out = 4, k = 1" group, the cross-group mutual neighbors = m (from the 1 mutual edge blown up). Within-group mutual neighbors = 0 (if within-group is a tournament, no mutual edges). So k = m. We need d_out/4 = (4m + t)/4 = m + t/4. So we need m = m + t/4, giving t = 0.

But t = 0 means no out-edges within the group, which means all within-group edges are incoming for this vertex. But for a pair within the group, at least one direction must exist. If vertex A has t = 0 (no out-edges within group) and vertex B also has t = 0, then the pair {A, B} has no edge. Contradiction.

So the blow-up with tournament within groups doesn't work directly. Let me allow mutual edges within groups.

If within-group edges are all mutual: each vertex has m-1 out-edges within group (all mutual) and m-1 mutual neighbors within group.

For a "d_out = 4" group vertex: cross-group out = 4m, within-group out = m-1. Total d_out = 4m + m - 1 = 5m - 1. Need ≡ 0 (mod 4): 5m - 1 ≡ 0 (mod 4), i.e., m - 1 ≡ 0 (mod 4), m ≡ 1 (mod 4).

Mutual neighbors: cross-group = m, within-group = m-1. Total k = 2m - 1. Need d_out/4 = (5m-1)/4. So 2m - 1 = (5m-1)/4, giving 8m - 4 = 5m - 1, 3m = 3, m = 1. Only works for m = 1 (n = 7).

So that doesn't generalize either. The blow-up approach is too rigid.

Let me think about this more carefully. Maybe I should consider a completely different construction for n = 7m.

Let me try to construct directly for n = 7m using Z_n.

We need 6m vertices with d_out = 4m, k = m, and m vertices with d_out = 4(m-1), k = m-1.

Hmm, actually, the distribution of out-degrees doesn't have to be exactly this. There could be other distributions. Let me think more generally.

We need:
- n = 7m vertices
- Each d_out ≡ 0 (mod 4)
- Sum d_out = 4m(7m-1)
- For each vertex, mutual neighbors = d_out/4
- Sum of mutual neighbors = m(7m-1) = 2M

One approach: use a circulant-like construction but with two types of vertices.

Actually, let me try yet another approach. Let me consider the problem on Z_n where n = 7m and try to find a difference-set-like structure.

Let me partition Z_{7m} \ {0} into pairs {d, -d}. There are (7m-1)/2 pairs if 7m is odd (m odd), or (7m-2)/2 pairs plus {7m/2} if 7m is even (m even).

For a vertex-transitive construction, we'd need all vertices to have the same d_out, but the average isn't an integer, so this is impossible. We need a non-vertex-transitive construction.

Let me try a different approach. Consider the following construction for n = 7m:

Partition the n vertices into 7 groups G_0, ..., G_{6}, each of size m. Use the cyclic tournament on the 7 groups: G_i → G_j if (j - i) mod 7 ∈ {1, 2, 3}, and G_j → G_i if (j - i) mod 7 ∈ {4, 5, 6}.

Between groups G_i and G_j (i ≠ j): all edges go in one direction (no mutual edges between groups).

Within each group G_i: we need to define the edge structure. Each vertex in G_i has 3m out-edges to other groups (from the cyclic tournament). We need total d_out ≡ 0 (mod 4), so within-group out-degree ≡ -3m ≡ 0 (mod 4), i.e., 3m ≡ 0 (mod 4), i.e., m ≡ 0 (mod 4).

If m ≡ 0 (mod 4), say m = 4t, then within-group out-degree needs to be ≡ 0 (mod 4). We can use a regular tournament within each group if m is odd... but m = 4t is even. So we can't have a regular tournament.

Hmm, let me think about this differently. Within each group of size m, we need a semi-complete digraph (at least one edge per pair) where each vertex has out-degree ≡ 0 (mod 4) and the mutual structure satisfies the 25% condition.

Actually wait. The mutual neighbors of a vertex come from both within-group and between-group edges. In this construction, between-group edges are all single-direction (no mutual). So mutual neighbors only come from within-group edges.

For a vertex in G_i with within-group out-degree w and within-group mutual neighbors w/4 (if the within-group structure satisfies the 25% condition):
- Total d_out = 3m + w
- Total k = w/4
- Need k = d_out/4 = (3m + w)/4
- So w/4 = (3m + w)/4, giving 0 = 3m/4, so m = 0. Contradiction!

So the between-group edges can't all be single-direction. We need some mutual edges between groups.

OK let me take a step back and think about this more carefully.

The 25% condition is global: for each vertex, among ALL its out-neighbors, 25% sent a message back. So mutual neighbors / out-degree = 1/4.

If between-group edges are all single, then mutual neighbors = within-group mutual neighbors, and out-degree = 3m + within-group out-degree. The condition becomes:

within-mutual / (3m + within-out) = 1/4

If within-group is also a 25%-structure: within-mutual = within-out / 4. Then:

(within-out / 4) / (3m + within-out) = 1/4
within-out / 4 = (3m + within-out) / 4
within-out = 3m + within-out
0 = 3m

Contradiction again. So we can't have all between-group edges be single.

We need between-group mutual edges. Let me reconsider.

Let me try a construction where between groups, we have a mix of single and mutual edges.

Consider 7 groups of size m. For groups G_i and G_j with (j-i) mod 7 ∈ {1,2,3} (G_i → G_j direction):
- Some edges from G_i to G_j are mutual, some are single (G_i → G_j only).

Let's say a fraction of the m² edges between G_i and G_j are mutual. Specifically, let's say each vertex in G_i has a mutual edge with some vertices in G_j and a single out-edge to the rest.

This is getting complex. Let me try a cleaner approach.

**Clean approach using difference sets on Z_n:**

For n = 7m, consider Z_n. Let me try to find a set D_out ⊂ Z_n \ {0} (not necessarily giving a vertex-transitive graph, but let me first try).

For vertex-transitive: |D_out| = 4m, |D_out ∩ (-D_out)| = m, D_out ∪ (-D_out) = Z_n \ {0}.

|D_out ∪ (-D_out)| = |D_out| + |D_out| - |D_out ∩ (-D_out)| = 4m + 4m - m = 7m = n. But Z_n \ {0} has n - 1 = 7m - 1 elements. So 7m = 7m - 1 is a contradiction.

So vertex-transitive is impossible for n = 7m, confirming our earlier finding.

OK so I need a non-vertex-transitive construction. Let me think about using two types of vertices.

Let me use the structure: Z_n = Z_7 × Z_m (when gcd(7, m) = 1, i.e., m not divisible by 7; but even when it's not a direct product, I can think of elements as (g, h) with g ∈ Z_7, h ∈ Z_m).

Actually, let me just think of the n = 7m vertices as arranged in a 7 × m grid: vertex (i, j) where i ∈ {0,...,6}, j ∈ {0,...,m-1}.

Define the edge structure:
1. Between (i, j) and (i, j') in the same group (same i): make all edges mutual. So each vertex has m-1 mutual neighbors within its group, and m-1 out-edges within its group.

2. Between groups: use the cyclic tournament. (i, j) → (i', j') for all j, j' if (i' - i) mod 7 ∈ {1, 2, 3}. These are single edges.

For vertex (i, j):
- Out-degree: (m-1) [within group] + 3m [to three other groups] = 4m - 1.
- Mutual neighbors: m - 1 [within group].
- Need: mutual / out = 1/4, so (m-1)/(4m-1) = 1/4, giving 4(m-1) = 4m - 1, 4m - 4 = 4m - 1, -4 = -1. Contradiction.

Doesn't work. The within-group mutual edges contribute too much to the ratio.

Let me try: within-group edges are single (tournament), and between-group edges have some mutual ones.

3. Within group i: regular tournament (if m is odd) or some tournament. Each vertex has (m-1)/2 out-edges within group (if m odd, regular tournament).

4. Between groups G_i and G_{i+1} (mod 7): all m² edges are from G_i to G_{i+1}. Some are mutual, some single.

Let me parameterize: for the edge between groups G_i and G_j (where G_i → G_j), let each vertex in G_i have a mutual edge with exactly r vertices in G_j and a single out-edge to (m - r) vertices in G_j.

By symmetry, assume the structure is the same for all groups (cyclic symmetry).

For vertex (i, j):
- Out-degree: (m-1)/2 [within group, if regular tournament] + 3r [mutual to 3 groups] + 3(m-r) [single to 3 groups] = (m-1)/2 + 3m.
  Wait, the out-edges to group G_{i+d} (d ∈ {1,2,3}) are: r mutual + (m-r) single = m out-edges. So total out to other groups = 3m.
  Total out-degree = (m-1)/2 + 3m.

- Mutual neighbors: 0 [within group, tournament] + 3r [from 3 groups] = 3r.

- Need: 3r / ((m-1)/2 + 3m) = 1/4.
  12r = (m-1)/2 + 3m = (m - 1 + 6m)/2 = (7m - 1)/2.
  r = (7m - 1)/24.

For r to be a non-negative integer: 24 | (7m - 1), i.e., 7m ≡ 1 (mod 24), m ≡ 7^{-1} (mod 24). 7 × 7 = 49 = 48 + 1 ≡ 1 (mod 24). So m ≡ 7 (mod 24).

Also need m odd (for regular tournament within group). m ≡ 7 (mod 24) is odd. ✓

And 0 ≤ r ≤ m: r = (7m-1)/24. For m ≥ 1, r ≥ 0. r ≤ m iff 7m - 1 ≤ 24m iff -1 ≤ 17m, true. ✓

So this construction works when m ≡ 7 (mod 24), i.e., m ∈ {7, 31, 55, ...}, giving n = 7m ∈ {49, 217, ...}. Only n = 49 is two-digit.

But this is just one construction. We need constructions for all n = 7m with 10 ≤ 7m ≤ 99, i.e., 2 ≤ m ≤ 14 (m integer), so n ∈ {14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98}.

The above construction only covers n = 49. We need more general constructions.

Let me think more generally. The within-group structure doesn't have to be a regular tournament, and the between-group structure doesn't have to be symmetric across all 3 "out" groups.

Let me generalize. Within each group of size m, use a semi-complete digraph satisfying the 25% condition (recursively, if possible). Between groups, use the cyclic tournament with some mutual edges.

Actually, this recursive approach could work. Let me think about it.

If within each group of size m, we have a valid 25%-structure where each vertex has out-degree w and mutual neighbors w/4, and between groups we add mutual edges:

For vertex (i, j):
- Out-degree: w [within group] + 3m [to 3 out-groups, all out-edges] = w + 3m.
  Wait, but some of the 3m between-group edges might be mutual. Let me say each vertex has r mutual out-edges to each out-group and (m - r) single out-edges.
  Actually, the out-edges to each out-group total m (r mutual + (m-r) single). So total out to other groups = 3m.
  Total out-degree = w + 3m.

- Mutual neighbors: w/4 [within group] + 3r [from 3 out-groups] = w/4 + 3r.

- Need: (w/4 + 3r) / (w + 3m) = 1/4.
  w/4 + 3r = (w + 3m)/4 = w/4 + 3m/4.
  3r = 3m/4.
  r = m/4.

So r = m/4, requiring 4 | m.

And w can be anything (as long as the within-group structure is valid). So if 4 | m and we can find a valid within-group structure of size m, then we can construct for n = 7m.

For 4 | m: n = 7m with m ∈ {4, 8, 12, ...}, giving n ∈ {28, 56, 84, ...}. Two-digit: 28, 56, 84.

But we also need the within-group structure to be valid. The within-group is a 25%-structure on m vertices. By induction, if m ≡ 0 or 1 (mod 7), we can do it. m = 4: 4 mod 7 = 4, not 0 or 1. So we can't directly use a 25%-structure on 4 vertices.

Hmm, but the within-group structure doesn't have to be a 25%-structure. It just needs to be a semi-complete digraph where each vertex has out-degree w (divisible by 4) and w/4 mutual neighbors. Wait, that IS the 25% condition. So the within-group structure must satisfy the 25% condition, which requires m ≡ 0 or 1 (mod 7).

For m = 4: 4 ≡ 4 (mod 7), not valid. So this recursive approach with m = 4 doesn't work.

Let me reconsider. Maybe the within-group structure doesn't need to satisfy the 25% condition by itself. The 25% condition is global. Let me re-derive.

Actually, I already did the derivation correctly. The within-group contributes w out-edges and w/4 mutual neighbors (if within-group is a 25%-structure). But what if within-group is NOT a 25%-structure?

Let me re-derive without assuming within-group is a 25%-structure.

Within group: each vertex has out-degree w_i and mutual neighbors μ_i (within group). These don't have to satisfy μ_i = w_i/4.

Between groups: each vertex has r mutual out-edges to each of 3 out-groups, and (m-r) single out-edges to each. So 3m out-edges to other groups, 3r mutual from other groups.

Total out-degree = w_i + 3m.
Total mutual = μ_i + 3r.

Need: (μ_i + 3r) / (w_i + 3m) = 1/4 for each vertex.
4(μ_i + 3r) = w_i + 3m.
4μ_i + 12r = w_i + 3m.
12r = w_i + 3m - 4μ_i.
r = (w_i + 3m - 4μ_i) / 12.

For r to be the same for all vertices in a group (by symmetry), we need w_i + 3m - 4μ_i to be the same for all vertices in the group, i.e., w_i - 4μ_i is constant.

If within-group is a 25%-structure, w_i - 4μ_i = 0 for all i, so r = 3m/12 = m/4. (As before.)

If within-group is a tournament (no mutual edges, μ_i = 0), then r = (w_i + 3m) / 12. For this to be constant, w_i must be constant, i.e., regular tournament (m odd). Then r = ((m-1)/2 + 3m) / 12 = (7m - 1) / 24. (As before.)

More generally, we can use any within-group semi-complete digraph where w_i - 4μ_i is constant across vertices. Let's call this constant c. Then r = (c + 3m) / 12.

We need r to be a non-negative integer with 0 ≤ r ≤ m.

So we need:
1. 12 | (c + 3m)
2. 0 ≤ r ≤ m, i.e., 0 ≤ (c + 3m)/12 ≤ m, i.e., 0 ≤ c + 3m ≤ 12m, i.e., -3m ≤ c ≤ 9m.
3. There exists a semi-complete digraph on m vertices where each vertex has w_i - 4μ_i = c, with w_i ≡ 0 (mod 4) and 0 ≤ w_i ≤ m-1, 0 ≤ μ_i ≤ w_i, and the structure is realizable.

Wait, actually w_i doesn't need to be divisible by 4 for the within-group structure. The divisibility by 4 is for the total out-degree: w_i + 3m ≡ 0 (mod 4), i.e., w_i ≡ -3m ≡ m (mod 4) (since -3 ≡ 1 mod 4). So w_i ≡ m (mod 4).

And the total mutual = μ_i + 3r = (w_i + 3m)/4, which is automatically an integer if w_i + 3m ≡ 0 (mod 4).

So the constraints on the within-group structure are:
- w_i ≡ m (mod 4) for all i
- w_i - 4μ_i = c for all i (constant)
- 0 ≤ w_i ≤ m - 1
- 0 ≤ μ_i ≤ w_i
- Semi-complete (at least one edge per pair)
- 12 | (c + 3m), 0 ≤ (c + 3m)/12 ≤ m

This is quite flexible. Let me think about what values of c are achievable.

For a tournament on m vertices (μ_i = 0): w_i = c, and w_i ≡ m (mod 4). For a regular tournament (m odd), w_i = (m-1)/2 for all i. So c = (m-1)/2, and we need (m-1)/2 ≡ m (mod 4), i.e., (m-1)/2 - m ≡ 0 (mod 4), i.e., (-m-1)/2 ≡ 0 (mod 4), i.e., (m+1)/2 ≡ 0 (mod 4), i.e., m + 1 ≡ 0 (mod 8), i.e., m ≡ 7 (mod 8). Combined with m odd (for regular tournament), m ≡ 7 (mod 8) is already odd. And r = (c + 3m)/12 = ((m-1)/2 + 3m)/12 = (7m - 1)/24. Need 24 | (7m - 1). 7m ≡ 1 (mod 24). As computed, m ≡ 7 (mod 24). This is a subset of m ≡ 7 (mod 8).

So for m ≡ 7 (mod 24), the regular tournament within groups works. This gives n = 49, 217, ... Only n = 49 is two-digit from n = 7m.

For other values of m, I need different within-group structures.

Let me think about what within-group structures are possible for small m.

For general m, the simplest within-group structure is:
- All edges mutual: w_i = m - 1, μ_i = m - 1. Then c = (m-1) - 4(m-1) = -3(m-1). w_i = m - 1 ≡ m (mod 4)? Need m - 1 ≡ m (mod 4), i.e., -1 ≡ 0 (mod 4). No.

- All edges single (tournament), not necessarily regular: w_i varies, μ_i = 0, c = w_i. Need w_i constant and ≡ m (mod 4). Regular tournament needs m odd. w_i = (m-1)/2. Need (m-1)/2 ≡ m (mod 4). As above, m ≡ 7 (mod 8).

- Mixed structure. Let me think about using a within-group structure where some edges are mutual and some are single.

This is getting quite involved. Let me try a completely different approach to the construction.

**Alternative approach: direct construction on Z_n for n = 7m.**

Let me think of Z_n where n = 7m. Consider the set of "quadratic residue"-like differences.

Actually, let me try to think about this problem from a higher level. The necessary condition is n ≡ 0 or 1 (mod 7). The question is whether this is also sufficient (for two-digit n).

Let me consider the possibility that the answer is simply the count of two-digit n with n ≡ 0 or 1 (mod 7), which is 26. But I need to verify sufficiency.

Let me try to think about constructions more carefully for each case.

**For n ≡ 1 (mod 7):** We showed a vertex-transitive construction works for all n = 7m + 1 ≥ 8. So all two-digit n ≡ 1 (mod 7) work. That's 13 values.

**For n ≡ 0 (mod 7):** We need n = 7m with 2 ≤ m ≤ 14. We need to show each of these works.

Let me try to find constructions for each m from 2 to 14.

For the within-group approach with 7 groups of size m, I need a within-group semi-complete digraph on m vertices with constant c = w_i - 4μ_i, w_i ≡ m (mod 4), and 12 | (c + 3m), 0 ≤ (c+3m)/12 ≤ m.

Let me think about what within-group structures give constant c.

**Option A: Tournament (μ = 0, c = w).** Need regular (w constant), m odd, w = (m-1)/2, w ≡ m (mod 4), 12 | (w + 3m).
- (m-1)/2 ≡ m (mod 4) → m ≡ 7 (mod 8)
- 12 | ((m-1)/2 + 3m) → 24 | (7m - 1) → m ≡ 7 (mod 24)
- Works for m = 7 (n = 49). Next is m = 31 (too big).

**Option B: All mutual within group (w = μ = m-1, c = -3(m-1)).** Need w ≡ m (mod 4): m - 1 ≡ m (mod 4) → -1 ≡ 0 (mod 4). Never works.

**Option C: Some mix.** Let me think about within-group structures where each vertex has the same (w, μ).

For a vertex-transitive within-group structure on m vertices: w constant, μ constant, c = w - 4μ constant. Need w ≡ m (mod 4), 12 | (w - 4μ + 3m), 0 ≤ (w - 4μ + 3m)/12 ≤ m.

For a vertex-transitive semi-complete digraph on m vertices (using Z_m differences): w = |D|, μ = |D ∩ (-D)|, D ∪ (-D) = Z_m \ {0}, so |D| + |D| - |D ∩ (-D)| = m - 1, i.e., 2w - μ = m - 1, so μ = 2w - m + 1.

Then c = w - 4μ = w - 4(2w - m + 1) = w - 8w + 4m - 4 = -7w + 4m - 4.

r = (c + 3m)/12 = (-7w + 4m - 4 + 3m)/12 = (-7w + 7m - 4)/12 = (7(m - w) - 4)/12.

Need 12 | (7(m - w) - 4). Let d = m - w (the "in-degree from within group" minus... actually d = m - 1 - w is the within-group in-degree, but let me just use d = m - w). Wait, w is the within-group out-degree, and m - 1 - w is the within-group in-degree. So d = m - w = 1 + (in-degree within group).

Hmm, let me just compute. We need 12 | (7d - 4) where d = m - w, and w = |D| for some valid difference set D on Z_m.

7d - 4 ≡ 0 (mod 12). 7d ≡ 4 (mod 12). 7^{-1} mod 12: 7 × 7 = 49 = 48 + 1 ≡ 1 (mod 12). So d ≡ 7 × 4 = 28 ≡ 4 (mod 12). So d ≡ 4 (mod 12).

d = m - w. Since w = |D| and D ∪ (-D) = Z_m \ {0}, we have w ≥ (m-1)/2 (at least half the differences). So d = m - w ≤ m - (m-1)/2 = (m+1)/2. Also d ≥ m - (m-1) = 1 (since w ≤ m - 1).

So d ∈ [1, (m+1)/2] and d ≡ 4 (mod 12). So d ∈ {4, 16, 28, ...} with d ≤ (m+1)/2.

For d = 4: m ≥ 2d - 1 = 7. So m ≥ 7. And w = m - 4, μ = 2(m-4) - m + 1 = m - 7.

Need μ ≥ 0: m ≥ 7. ✓
Need w ≤ m - 1: m - 4 ≤ m - 1. ✓
Need w ≥ (m-1)/2: m - 4 ≥ (m-1)/2, 2m - 8 ≥ m - 1, m ≥ 7. ✓

Also need w ≡ m (mod 4): m - 4 ≡ m (mod 4). ✓ (always true since 4 ≡ 0 mod 4).

And r = (7·4 - 4)/12 = 24/12 = 2. Need 0 ≤ r ≤ m: 2 ≤ m. ✓ for m ≥ 7.

So for m ≥ 7, using a vertex-transitive within-group structure with d = 4 (i.e., w = m - 4, μ = m - 7), we get r = 2. This works!

But we need to verify that such a difference set D exists on Z_m with |D| = m - 4 and |D ∩ (-D)| = m - 7.

|D| = m - 4, |D ∩ (-D)| = m - 7, |D ∪ (-D)| = m - 1.
Check: |D| + |D| - |D ∩ (-D)| = 2(m-4) - (m-7) = 2m - 8 - m + 7 = m - 1. ✓

So D ∪ (-D) = Z_m \ {0} (all non-zero elements covered), and |D ∩ (-D)| = m - 7.

The elements NOT in D are: those in (-D) \ D. |(-D) \ D| = |D| - |D ∩ (-D)| = (m-4) - (m-7) = 3. So exactly 3 elements are in -D but not in D, meaning 3 elements are in D but not in -D (by symmetry of the counting), and m - 7 elements are in both.

Wait, let me recount. |D \ (-D)| = |D| - |D ∩ (-D)| = (m-4) - (m-7) = 3. |(-D) \ D| = |-D| - |D ∩ (-D)| = (m-4) - (m-7) = 3. |D ∩ (-D)| = m - 7. Total: 3 + 3 + (m-7) = m - 1. ✓

So we need: 3 elements in D only, 3 elements in -D only (i.e., 3 elements not in D), and m - 7 elements in both.

The 3 elements not in D: these are the elements d such that d ∉ D but -d ∈ D. The 3 elements in D only: d ∈ D but -d ∉ D.

The pairs {d, -d}: there are (m-1)/2 pairs if m odd, or (m-2)/2 pairs + {m/2} if m even.

- "Both" pairs (both d and -d in D): these contribute 2 to |D ∩ (-D)| each. So (m-7)/2 such pairs if m odd, or (m-7-1)/2 = (m-8)/2 such pairs + possibly m/2 if m even and m/2 ∈ D.

Hmm, this is getting complicated. Let me just check: can we always find such a D for m ≥ 7?

The condition is: D ⊂ Z_m \ {0}, |D| = m - 4, D ∪ (-D) = Z_m \ {0}, |D ∩ (-D)| = m - 7.

Equivalently: the complement of D in Z_m \ {0} has size 3, and D ∪ (-D) = Z_m \ {0} means the complement of D is contained in -D, i.e., if d ∉ D then -d ∈ D.

So the 3 elements not in D, call them a, b, c, must satisfy: -a, -b, -c ∈ D. Also, a, b, c ∉ D means -a, -b, -c ∈ D \ (-D) (they're in D but their negatives aren't)... wait, no. -a ∈ D, and a ∉ D. Is -a ∈ -D? -a ∈ -D iff a ∈ D. But a ∉ D, so -a ∉ -D. So -a ∈ D \ (-D). Similarly for b, c.

So -a, -b, -c are the 3 elements in D \ (-D). And a, b, c are the 3 elements in (-D) \ D = complement of D.

Now, |D ∩ (-D)| = m - 7. The "both" elements: Z_m \ {0, ±a, ±b, ±c} (excluding 0 and the 6 elements ±a, ±b, ±c) has size m - 1 - 6 = m - 7. These are all in D ∩ (-D). But wait, what if some of a, b, c are self-inverse (a = -a, i.e., a = m/2)? Then the set {±a, ±b, ±c} has fewer than 6 elements.

Let me assume m is odd for simplicity (no self-inverse elements). Then {±a, ±b, ±c} has 6 elements (assuming a, b, c are distinct and no two are negatives of each other). The remaining m - 7 elements are in D ∩ (-D). We need to put all of them in D (and their negatives too, which they already are since they're in both).

So the construction is:
1. Choose 3 elements a, b, c (with a, b, c, -a, -b, -c all distinct, i.e., no two of a,b,c are equal or negatives).
2. D = (Z_m \ {0, a, b, c}) — i.e., everything except 0, a, b, c.
3. Check: -a, -b, -c ∈ D (since -a ≠ a, b, c as long as -a ∉ {a, b, c}, which is ensured by the distinctness condition). ✓
4. |D| = m - 1 - 3 = m - 4. ✓
5. D ∪ (-D) = Z_m \ {0} ∪ (something)... let me check. -D = Z_m \ {0, -a, -b, -c}. D ∪ (-D) = Z_m \ ({a,b,c} ∩ {-a,-b,-c})... no. D ∪ (-D) = (Z_m \ {0,a,b,c}) ∪ (Z_m \ {0,-a,-b,-c}) = Z_m \ ({a,b,c} ∩ {-a,-b,-c})... no, that's not right either.

D ∪ (-D) = Z_m \ ({0, a, b, c} ∩ {0, -a, -b, -c}). Wait, De Morgan: complement of (D ∪ (-D)) = complement of D ∩ complement of (-D) = {0, a, b, c} ∩ {0, -a, -b, -c} = {0} ∪ ({a,b,c} ∩ {-a,-b,-c}).

If a, b, c, -a, -b, -c are all distinct (and nonzero), then {a,b,c} ∩ {-a,-b,-c} = ∅. So complement of (D ∪ (-D)) = {0}, meaning D ∪ (-D) = Z_m \ {0}. ✓

6. |D ∩ (-D)| = |D| + |-D| - |D ∪ (-D)| = (m-4) + (m-4) - (m-1) = m - 7. ✓

So for m odd, m ≥ 7, we can always find such a D (just pick any 3 elements a, b, c with all of ±a, ±b, ±c distinct and nonzero, which is possible when m ≥ 7 since there are (m-1)/2 ≥ 3 pairs).

For m even, we need to be more careful about the self-inverse element m/2. Let me handle that case.

If m is even, m/2 is self-inverse. We need to decide whether m/2 ∈ D or not.

Case m/2 ∈ D: Then m/2 ∈ D ∩ (-D) (since -m/2 = m/2). So m/2 is a "both" element. We need to choose a, b, c (not in D) from the remaining m - 2 non-self-inverse elements (i.e., (m-2)/2 pairs). We need 3 elements a, b, c with ±a, ±b, ±c all distinct and none equal to m/2. This requires (m-2)/2 ≥ 3, i.e., m ≥ 8.

Case m/2 ∉ D: Then m/2 is one of a, b, c (say a = m/2). Then -a = m/2 = a, so -a ∈ D requires a ∈ D, contradiction. So this doesn't work.

So for m even, m ≥ 8, we include m/2 in D and choose 3 other elements. Then |D| = m - 4 (including m/2 and all but 3 of the other elements). Let me verify: D = (Z_m \ {0}) \ {a, b, c} where a, b, c are 3 non-self-inverse elements. |D| = (m-1) - 3 = m - 4. ✓

D ∪ (-D): complement = {0, a, b, c} ∩ {0, -a, -b, -c}. Since a, b, c are non-self-inverse and ±a, ±b, ±c distinct: complement = {0}. So D ∪ (-D) = Z_m \ {0}. ✓

|D ∩ (-D)|: m/2 ∈ D ∩ (-D). The other elements in D ∩ (-D) are the non-self-inverse elements in both D and -D, which is all non-self-inverse elements except ±a, ±b, ±c. Count: (m - 2) - 6 = m - 8. Plus m/2: total m - 8 + 1 = m - 7. ✓

So for m even, m ≥ 8, the construction also works.

Summary for n = 7m with the within-group vertex-transitive construction (d = 4, r = 2):
- m odd, m ≥ 7: works. n = 49, 63, 77, 91 (m = 7, 9, 11, 13).
- m even, m ≥ 8: works. n = 56, 70, 84, 98 (m = 8, 10, 12, 14).

So this covers n = 49, 56, 63, 70, 77, 84, 91, 98. That's m = 7, 8, 9, 10, 11, 12, 13, 14.

What about m = 2, 3, 4, 5, 6 (n = 14, 21, 28, 35, 42)?

For these small m, the d = 4 construction doesn't work (need m ≥ 7 for odd, m ≥ 8 for even). Let me try other values of d.

d ≡ 4 (mod 12), so d ∈ {4, 16, 28, ...}. For small m, d = 4 requires m ≥ 7. The next value d = 16 requires m ≥ 31. So for m < 7, we can't use the vertex-transitive within-group approach with this d.

But we can use non-vertex-transitive within-group structures, or a completely different construction.

Let me think about alternative constructions for n = 14, 21, 28, 35, 42.

**For n = 14 (m = 2):** 7 groups of 2. Within each group of 2, there's only 1 pair. Options: single edge (tournament, w = 1 or 0) or mutual (w = 1, μ = 1).

Between groups: cyclic tournament, 3 out-groups of 2 each, so 6 out-edges to other groups.

If within-group is mutual (w = 1, μ = 1): total out = 1 + 6 = 7. Need 4 | 7? No, 7 is not divisible by 4. ✗

If within-group is single (w = 1, μ = 0 for one vertex, w = 0, μ = 0 for the other): 
- Vertex with w = 1: total out = 1 + 6 = 7. Not divisible by 4. ✗
- Vertex with w = 0: total out = 0 + 6 = 6. Not divisible by 4. ✗

So the 7-group construction with pure cyclic tournament between groups doesn't work for m = 2. We need mutual edges between groups.

Let me try a different approach for n = 14. Let me use the within-group approach but with mutual edges between groups.

General setup: 7 groups of m. Between groups G_i and G_{i+d} (d ∈ {1,2,3}), edges go from G_i to G_{i+d}. Each vertex in G_i has r mutual out-edges to G_{i+d} and (m - r) single out-edges. (Same r for all d by symmetry.)

Within group: each vertex has out-degree w and mutual μ. (Can vary by vertex.)

Total out = w + 3m. Total mutual = μ + 3r. Need (μ + 3r) / (w + 3m) = 1/4, i.e., 4μ + 12r = w + 3m.

Also need w + 3m ≡ 0 (mod 4), i.e., w ≡ m (mod 4) (since 3m ≡ -m ≡ ... well, w + 3m ≡ 0 (mod 4) means w ≡ -3m ≡ m (mod 4) since -3 ≡ 1 (mod 4)).

For n = 14 (m = 2): w ≡ 2 (mod 4). Since 0 ≤ w ≤ 1 (within group of 2), w ∈ {0, 1}. Neither is ≡ 2 (mod 4). So w + 3m = w + 6, and we need 4 | (w + 6). w = 0: 6, not div by 4. w = 1: 7, not div by 4. w = 2: impossible (max 1).

So the 7-group construction fundamentally doesn't work for m = 2, regardless of r. The issue is that w + 6 must be divisible by 4, but w ∈ {0, 1} gives 6 or 7, neither divisible by 4.

Hmm. So we need a different construction for n = 14. Let me think about this differently.

Maybe the 7-group structure is too restrictive. Let me think about n = 14 directly.

For n = 14: M = 14·13/14 = 13. S = 78 - 13 = 65. Sum d_out = 65 + 26 = 91... wait let me recompute. Sum d_out = S + 2M = 65 + 26 = 91. Hmm, but also sum d_out = 4n(n-1)/7 = 4·14·13/7 = 4·2·13 = 104. Let me recheck.

n(n-1)/14 = 14·13/14 = 13 = M. S = 6M = 78. Total pairs = M + S = 91 = C(14,2) = 91. ✓
Sum d_out = S + 2M = 78 + 26 = 104. ✓ (matches 4·14·13/7 = 104)
Average d_out = 104/14 = 52/7 ≈ 7.43.

Each d_out ≡ 0 (mod 4). Possible d_out values: 0, 4, 8, 12. (Can't be > 13.)

Sum = 104 with 14 vertices, each d_out ∈ {0, 4, 8, 12}:
If x₀ have d_out=0, x₁ have 4, x₂ have 8, x₃ have 12:
x₀ + x₁ + x₂ + x₃ = 14
4x₁ + 8x₂ + 12x₃ = 104, i.e., x₁ + 2x₂ + 3x₃ = 26.

From these: x₀ = 14 - x₁ - x₂ - x₃ and x₁ = 26 - 2x₂ - 3x₃.
x₀ = 14 - (26 - 2x₂ - 3x₃) - x₂ - x₃ = 14 - 26 + 2x₂ + 3x₃ - x₂ - x₃ = -12 + x₂ + 2x₃.
Need x₀ ≥ 0: x₂ + 2x₃ ≥ 12.
Need x₁ ≥ 0: 26 - 2x₂ - 3x₃ ≥ 0, i.e., 2x₂ + 3x₃ ≤ 26.

Many solutions. For example, x₃ = 4, x₂ = 4: x₁ = 26 - 8 - 12 = 6, x₀ = -12 + 4 + 8 = 0. So 0 vertices with d_out=0, 6 with d_out=4, 4 with d_out=8, 4 with d_out=12. Sum = 0 + 24 + 32 + 48 = 104. ✓

Or x₃ = 6, x₂ = 4: x₁ = 26 - 8 - 18 = 0, x₀ = -12 + 4 + 12 = 4. So 4 with d_out=0, 0 with 4, 4 with 8, 6 with 12. Sum = 0 + 0 + 32 + 72 = 104. ✓

The question is whether we can realize any of these with an actual graph. This is a graph realization problem.

Let me think about it differently. Instead of trying to construct explicitly, let me think about whether there's a general existence theorem.

Actually, let me reconsider the problem. Maybe I should think about it as follows:

We have a "semi-complete" digraph (for each pair, at least one direction). The condition is that for each vertex v, if d(v) is the out-degree and m(v) is the number of mutual neighbors, then m(v) = d(v)/4.

Equivalently, d(v) = 4m(v), so d(v) is always a multiple of 4.

Let me think of the graph as follows. For each unordered pair {u, v}, we have either:
- A single edge (one direction), or
- A mutual edge (both directions).

Let's say the mutual edges form a graph G_m (undirected), and the single edges form a tournament T on the remaining pairs.

For each vertex v:
- d(v) = (out-degree in T) + (degree in G_m)
- m(v) = degree in G_m
- Condition: degree in G_m = d(v)/4 = (out-degree in T + degree in G_m) / 4
- So 4 · deg_{G_m}(v) = out-degree_T(v) + deg_{G_m}(v)
- 3 · deg_{G_m}(v) = out-degree_T(v)

So for each vertex v: out-degree in the tournament T = 3 × degree in the mutual graph G_m.

This is a nice reformulation! Let me verify:
- d(v) = out_T(v) + deg_M(v) where out_T is out-degree in tournament, deg_M is degree in mutual graph.
- m(v) = deg_M(v).
- Condition: deg_M(v) = d(v)/4 = (out_T(v) + deg_M(v))/4.
- 4 deg_M = out_T + deg_M → 3 deg_M = out_T. ✓

So the condition is: **for each vertex v, the out-degree of v in the tournament T equals 3 times the degree of v in the mutual graph G_m.**

The tournament T is on the pairs not in G_m. The total number of pairs is C(n,2). The mutual graph G_m has M edges. The tournament T is on C(n,2) - M pairs.

For each vertex v:
- deg_M(v) = degree in G_m
- out_T(v) = 3 · deg_M(v)
- In the tournament T, v plays against n - 1 - deg_M(v) opponents (those not connected to v by a mutual edge). So out_T(v) + in_T(v) = n - 1 - deg_M(v).
- out_T(v) = 3 deg_M(v), so in_T(v) = n - 1 - deg_M(v) - 3 deg_M(v) = n - 1 - 4 deg_M(v).
- Need in_T(v) ≥ 0: deg_M(v) ≤ (n-1)/4.
- Need out_T(v) ≤ n - 1 - deg_M(v): 3 deg_M(v) ≤ n - 1 - deg_M(v), i.e., 4 deg_M(v) ≤ n - 1. Same condition.

Also, sum of out_T over all vertices = number of tournament edges = C(n,2) - M.
Sum of 3 deg_M = 3 · 2M = 6M (since sum of degrees in G_m = 2M).
So C(n,2) - M = 6M, giving C(n,2) = 7M, i.e., M = n(n-1)/14. Same as before.

Now the question becomes: **for which n does there exist an undirected graph G_m on n vertices with M = n(n-1)/14 edges, such that the complement of G_m (on the same vertex set, with C(n,2) - M edges) admits a tournament where each vertex v has out-degree exactly 3 deg_{G_m}(v)?**

The tournament on the complement of G_m: each vertex v has n - 1 - deg_M(v) opponents, and needs out-degree 3 deg_M(v). This requires 3 deg_M(v) ≤ n - 1 - deg_M(v), i.e., deg_M(v) ≤ (n-1)/4.

Also, a tournament on a graph H (where H is the complement of G_m) with specified out-degrees exists iff the out-degree sequence is "tournament-realizable" on H. By a generalization of Landau's theorem, a tournament on a graph H with prescribed out-degrees d(v) exists iff:
- For every subset S of vertices, sum_{v in S} d(v) ≥ C(|S|, 2) - e_H(S) (where e_H(S) is the number of edges of H within S)... actually, this is more subtle.

Actually, the existence of a tournament on a given graph H (orienting each edge of H) with prescribed out-degrees is equivalent to an orientation problem. By the Gale-Ryser / Fulkerson theorem for orientations:

An undirected graph H has an orientation with prescribed out-degrees d(v) iff:
1. sum d(v) = |E(H)|
2. For every subset S ⊆ V, sum_{v ∈ S} d(v) ≥ |E(H[S])| - ... hmm, I need to recall the exact condition.

Actually, the condition for an orientation of graph H with prescribed out-degrees is:
- sum d(v) = |E(H)|
- For every S ⊆ V: sum_{v ∈ S} d(v) ≥ |E(H[S])| (where H[S] is the subgraph induced by S)... no, that's not right either.

The correct condition (by the theorem of Hakimi or Frank): An undirected graph G = (V, E) has an orientation with out-degree d(v) for each v iff:
- sum d(v) = |E|
- For every S ⊆ V: sum_{v ∈ S} d(v) ≥ |E(G[S])| (edges within S must have at least one endpoint in S with positive out-degree... actually no).

Let me think again. In an orientation of G, for a subset S, the edges within S contribute to out-degrees of vertices in S (each edge within S contributes 1 to the out-degree of one vertex in S). Edges from S to V\S contribute to out-degrees of vertices in S (if oriented from S to V\S). So:

sum_{v ∈ S} d(v) = (edges within S oriented from a vertex in S) + (edges from S to V\S oriented from S to V\S)
≥ (edges within S oriented from a vertex in S) ≥ 0

But also:
sum_{v ∈ S} d(v) = |E(G[S])| - (edges within S oriented into S from S, i.e., in-degree within S) + (edges from S to V\S oriented out)

Hmm, this is getting complicated. Let me use the correct theorem.

**Theorem (Hakimi, 1965 / Frank):** An undirected graph G = (V, E) has an orientation with prescribed out-degree function d: V → Z≥0 iff:
1. ∑_v d(v) = |E|
2. For every S ⊆ V: ∑_{v ∈ S} d(v) ≥ |E(G[S])|

Wait, I think the condition is actually:
2. For every S ⊆ V: ∑_{v ∈ S} d(v) ≥ |E(G[S])| - ... no.

Let me think about it from first principles. In an orientation of G, for subset S:
- Each edge within G[S] contributes exactly 1 to ∑_{v ∈ S} out(v) (one endpoint has it as an out-edge).
- Each edge between S and V\S contributes 0 or 1 to ∑_{v ∈ S} out(v) (1 if oriented from S to V\S, 0 otherwise).

So ∑_{v ∈ S} out(v) = |E(G[S])| - (edges within S oriented from V\S... no, edges within S are between vertices in S, so they always contribute 1 to the sum) + (edges from S to V\S oriented from S to V\S).

Wait: ∑_{v ∈ S} out(v) = (number of edges within G[S] oriented out of some v ∈ S, which is all of them since both endpoints are in S, so each contributes 1 to exactly one vertex's out-degree) + (edges from S to V\S oriented from S to V\S).

So ∑_{v ∈ S} out(v) = |E(G[S])| + (edges from S to V\S oriented from S).

Thus ∑_{v ∈ S} out(v) ≥ |E(G[S])|, with equality iff all edges between S and V\S are oriented from V\S to S.

Also, ∑_{v ∈ S} out(v) ≤ |E(G[S])| + |δ(S)| where δ(S) is the set of edges between S and V\S.

So the necessary and sufficient conditions for an orientation with prescribed out-degrees d(v) are:
1. ∑ d(v) = |E|
2. For every S ⊆ V: |E(G[S])| ≤ ∑_{v ∈ S} d(v) ≤ |E(G[S])| + |δ(S)|

The upper bound is equivalent to: ∑_{v ∈ S} d(v) ≤ |E(G[S])| + |δ(S)| = |E(G)| - |E(G[V\S])|, i.e., ∑_{v ∉ S} d(v) ≥ |E(G[V\S])|, which is the same as condition 2 applied to V\S.

So the conditions reduce to:
1. ∑ d(v) = |E|
2. For every S ⊆ V: ∑_{v ∈ S} d(v) ≥ |E(G[S])|

This is the correct condition (it's both necessary and sufficient).

Now, in our problem:
- G = complement of G_m (the mutual graph), i.e., G has C(n,2) - M edges.
- d(v) = 3 deg_{G_m}(v) for each v.
- Need: ∑ d(v) = |E(G)| = C(n,2) - M. Check: ∑ 3 deg_{G_m}(v) = 3 · 2M = 6M = C(n,2) - M (since C(n,2) = 7M). ✓
- Need: for every S ⊆ V, ∑_{v ∈ S} 3 deg_{G_m}(v) ≥ |E(G[S])|.

Now, |E(G[S])| = C(|S|, 2) - |E(G_m[S])| (edges within S in the complement of G_m = all pairs in S minus mutual edges in S).

And ∑_{v ∈ S} 3 deg_{G_m}(v) = 3 · (2|E(G_m[S])| + |δ_{G_m}(S)|) where δ_{G_m}(S) is the number of G_m-edges between S and V\S. (Because sum of degrees in G_m over S = 2|E(G_m[S])| + |δ_{G_m}(S)|.)

So the condition becomes:
3(2|E(G_m[S])| + |δ_{G_m}(S)|) ≥ C(|S|, 2) - |E(G_m[S])|
6|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) - |E(G_m[S])|
7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2)

So we need: **for every S ⊆ V, 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2).**

Note that 7|E(G_m[S])| + 3|δ_{G_m}(S)| = 7|E(G_m[S])| + 3(∑_{v ∈ S} deg_{G_m}(v) - 2|E(G_m[S])|) = 7|E(G_m[S])| + 3∑_{v ∈ S} deg_{G_m}(v) - 6|E(G_m[S])| = |E(G_m[S])| + 3∑_{v ∈ S} deg_{G_m}(v).

Hmm, that doesn't simplify as nicely. Let me just work with: 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2).

The total "weight" is 7|E(G_m)| = 7M = C(n,2) = C(|V|, 2). So for S = V, we get 7M + 0 = C(n,2) = C(|V|,2). ✓ (equality).

For general S, we need 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2).

Note that |E(G_m[S])| + |δ_{G_m}(S)| + |E(G_m[V\S])| = M, and C(|S|,2) + C(n-|S|,2) + |S|(n-|S|) = C(n,2) = 7M.

The condition for S is: 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2).
The condition for V\S is: 7|E(G_m[V\S])| + 3|δ_{G_m}(S)| ≥ C(n-|S|, 2).

Adding: 7(|E(G_m[S])| + |E(G_m[V\S])|) + 6|δ_{G_m}(S)| ≥ C(|S|, 2) + C(n-|S|, 2).
7(M - |δ_{G_m}(S)|) + 6|δ_{G_m}(S)| ≥ C(n,2) - |S|(n-|S|).
7M - 7|δ| + 6|δ| ≥ 7M - |S|(n-|S|).
-|δ| ≥ -|S|(n-|S|).
|δ| ≤ |S|(n-|S|). Always true since δ is a subset of all S × (V\S) pairs.

So the conditions for S and V\S are not redundant; they're both needed.

Now the question is: for which n does there exist a graph G_m on n vertices with M = n(n-1)/14 edges such that for every S ⊆ V, 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2)?

This is a question about the existence of a graph with certain "expansion" properties. The condition says that for every subset S, the mutual edges within S and crossing S must be "dense enough" relative to all pairs within S.

Let me think about what G_m should look like. The condition is easiest to satisfy when G_m is "well-distributed." A random graph or a regular graph with good expansion would work.

Let me consider G_m being a regular graph. If G_m is d-regular, then M = nd/2, so nd/2 = n(n-1)/14, giving d = (n-1)/7. So we need (n-1)/7 to be a non-negative integer, i.e., n ≡ 1 (mod 7). This matches our earlier finding for the vertex-transitive case.

For n ≡ 1 (mod 7), d = (n-1)/7. The condition 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) for a d-regular graph... For a d-regular graph, |δ_{G_m}(S)| = d|S| - 2|E(G_m[S])|. So:

7|E(G_m[S])| + 3(d|S| - 2|E(G_m[S])|) ≥ C(|S|, 2)
7e + 3d|S| - 6e ≥ C(|S|, 2)
e + 3d|S| ≥ C(|S|, 2)
|E(G_m[S])| ≥ C(|S|, 2) - 3d|S| = |S|(|S|-1)/2 - 3d|S| = |S|(|S| - 1 - 6d)/2

With d = (n-1)/7: |E(G_m[S])| ≥ |S|(|S| - 1 - 6(n-1)/7)/2 = |S|(7|S| - 7 - 6n + 6)/14 = |S|(7|S| - 6n - 1)/14.

For |S| ≤ 6n/7 (roughly), the RHS is negative, so the condition is automatically satisfied. For |S| close to n, we need |E(G_m[S])| to be large enough.

For |S| = n (the whole set): |E(G_m[V])| = M = n(n-1)/14, and the RHS is n(7n - 6n - 1)/14 = n(n-1)/14 = M. So equality. ✓

For |S| = n - 1: |E(G_m[S])| ≥ (n-1)(7(n-1) - 6n - 1)/14 = (n-1)(7n - 7 - 6n - 1)/14 = (n-1)(n - 8)/14.

|E(G_m[S])| = M - deg_{G_m}(v) where v is the excluded vertex. If G_m is d-regular, deg(v) = d = (n-1)/7. So |E(G_m[S])| = n(n-1)/14 - (n-1)/7 = (n-1)(n/14 - 1/7) = (n-1)(n - 2)/14.

Need: (n-1)(n-2)/14 ≥ (n-1)(n-8)/14, i.e., n - 2 ≥ n - 8, i.e., 6 ≥ 0. ✓

So for a d-regular G_m with good expansion, the conditions are likely satisfied. But we need to verify this for all subsets, not just large ones.

Actually, for a d-regular graph, the condition |E(G_m[S])| ≥ |S|(7|S| - 6n - 1)/14 is automatically satisfied when 7|S| ≤ 6n + 1, i.e., |S| ≤ (6n+1)/7. For |S| > (6n+1)/7, we need the graph to have enough edges within S.

For a d-regular graph with d = (n-1)/7, the number of edges within S is at least (d|S| - |S|(n-|S|))/2 (by the expander mixing lemma or just by counting: |δ(S)| ≤ |S|(n - |S|), so |E(G_m[S])| = (d|S| - |δ(S)|)/2 ≥ (d|S| - |S|(n-|S|))/2 = |S|(d - n + |S|)/2).

Need: |S|(d - n + |S|)/2 ≥ |S|(7|S| - 6n - 1)/14.
(d - n + |S|)/2 ≥ (7|S| - 6n - 1)/14.
7(d - n + |S|) ≥ 7|S| - 6n - 1.
7d - 7n + 7|S| ≥ 7|S| - 6n - 1.
7d ≥ n - 1.
7 · (n-1)/7 ≥ n - 1.
n - 1 ≥ n - 1. ✓ (equality)

So for ANY d-regular graph G_m with d = (n-1)/7, the condition is satisfied! (The bound from |δ(S)| ≤ |S|(n-|S|) is tight enough.)

Wait, but I used the bound |δ(S)| ≤ |S|(n - |S|), which is the trivial bound (δ(S) is at most all pairs between S and V\S). This gives a lower bound on |E(G_m[S])| that's exactly tight. So the condition is satisfied for any d-regular graph.

But wait, does a d-regular graph on n vertices with d = (n-1)/7 always exist? We need n ≡ 1 (mod 7) (so d is an integer) and d ≤ n - 1 (always true for n ≥ 8) and nd even (n·(n-1)/7 even). Since n ≡ 1 (mod 7), n = 7k + 1, d = k. nd = (7k+1)k. This is even iff k(7k+1) is even, which is true when k is even or 7k+1 is even (i.e., k is odd). So always even. ✓

A d-regular graph on n vertices exists iff 0 ≤ d ≤ n-1 and nd is even. Both conditions are satisfied. ✓

So for n ≡ 1 (mod 7), we can always construct a valid configuration: take any d-regular graph G_m with d = (n-1)/7, and orient the complement with the prescribed out-degrees (which is possible by the Hakimi condition, as we verified).

Wait, but I need to double-check the Hakimi condition more carefully. I showed that the condition 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) is satisfied using the bound |δ_{G_m}(S)| ≤ |S|(n-|S|). But this is the trivial bound, and the calculation showed equality, meaning the condition is just barely satisfied. Let me re-examine.

For a d-regular G_m with d = (n-1)/7:
|E(G_m[S])| = (d|S| - |δ_{G_m}(S)|) / 2

The condition is:
7 · (d|S| - |δ|) / 2 + 3|δ| ≥ C(|S|, 2)
(7d|S| - 7|δ| + 6|δ|) / 2 ≥ |S|(|S|-1)/2
7d|S| - |δ| ≥ |S|(|S|-1)
|δ| ≤ 7d|S| - |S|(|S|-1) = |S|(7d - |S| + 1) = |S|((n-1) - |S| + 1) = |S|(n - |S|)

And |δ_{G_m}(S)| ≤ |S|(n - |S|) is always true (trivially, since δ is a subset of all S × V\S pairs). So the condition is always satisfied. ✓

Great, so for n ≡ 1 (mod 7), any d-regular G_m with d = (n-1)/7 works, and such a graph always exists. So all n ≡ 1 (mod 7) are achievable.

Now for n ≡ 0 (mod 7), n = 7m. We need M = 7m(7m-1)/14 = m(7m-1)/2. For M to be an integer, m(7m-1) must be even. If m is even, yes. If m is odd, 7m-1 is even, so yes. Always integer. ✓

We need a graph G_m on n = 7m vertices with M = m(7m-1)/2 edges, such that for every S, 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2), and the prescribed out-degrees d(v) = 3 deg_{G_m}(v) are achievable (which is the same condition).

G_m doesn't have to be regular. The average degree is 2M/n = 2 · m(7m-1)/2 / (7m) = (7m-1)/7 = m - 1/7. Not an integer, so G_m can't be regular.

Let me think about what G_m should look like for n = 7m. We need the degrees to satisfy: for each v, out_T(v) = 3 deg_{G_m}(v), and out_T(v) + in_T(v) = n - 1 - deg_{G_m}(v), so in_T(v) = n - 1 - 4 deg_{G_m}(v) ≥ 0, i.e., deg_{G_m}(v) ≤ (n-1)/4 = (7m-1)/4.

Also, the tournament is on the complement of G_m, so we need the Hakimi condition.

Let me try a specific construction for G_m. Consider a graph where 6m vertices have degree m and m vertices have degree m - 1. (This matches the out-degree distribution we found earlier: d_out = 4m for 6m vertices and d_out = 4(m-1) for m vertices, since d_out = 4 deg_{G_m} and deg_{G_m} = m or m-1.)

Check: sum of degrees = 6m · m + m · (m-1) = 6m² + m² - m = 7m² - m = m(7m - 1) = 2M. ✓

Check deg ≤ (n-1)/4 = (7m-1)/4: m ≤ (7m-1)/4 iff 4m ≤ 7m - 1 iff 1 ≤ 3m, true for m ≥ 1. And m - 1 ≤ (7m-1)/4 iff 4(m-1) ≤ 7m - 1 iff 4m - 4 ≤ 7m - 1 iff -3 ≤ 3m, true. ✓

Now, does such a graph exist (with 6m vertices of degree m and m vertices of degree m-1) and satisfy the Hakimi condition?

A graph with this degree sequence exists iff the Erdős–Gallai conditions are satisfied. For a degree sequence d_1 ≥ d_2 ≥ ... ≥ d_n, the condition is: for each k, ∑_{i=1}^k d_i ≤ k(k-1) + ∑_{i=k+1}^n min(d_i, k).

Our sequence: m vertices with degree m-1, 6m vertices with degree m. Sorted: m, m, ..., m (6m times), m-1, m-1, ..., m-1 (m times).

For k ≤ 6m: ∑_{i=1}^k d_i = km. RHS = k(k-1) + ∑_{i=k+1}^{7m} min(d_i, k).
- If k ≤ m-1: all remaining have degree ≥ m-1 ≥ k, so min = k. RHS = k(k-1) + (7m - k)k = k(k - 1 + 7m - k) = k(7m - 1). Need km ≤ k(7m - 1), i.e., m ≤ 7m - 1, true. ✓
- If m-1 < k ≤ 6m: the remaining 6m - k vertices have degree m, and m vertices have degree m-1. min(d_i, k) = min(m, k) for the degree-m vertices and min(m-1, k) = m-1 for the degree-(m-1) vertices (since k > m-1).
  - If k < m: min(m, k) = k. RHS = k(k-1) + (6m - k)k + m(m-1) = k(k - 1 + 6m - k) + m(m-1) = k(6m - 1) + m(m-1). Need km ≤ k(6m - 1) + m(m-1), i.e., 0 ≤ k(5m - 1) + m(m-1), true. ✓
  - If k ≥ m: min(m, k) = m. RHS = k(k-1) + (6m - k)m + m(m-1) = k(k-1) + 6m² - km + m² - m = k(k-1) + 7m² - km - m. Need km ≤ k(k-1) + 7m² - km - m, i.e., 2km ≤ k(k-1) + 7m² - m, i.e., 0 ≤ k² - k - 2km + 7m² - m = k² - (2m+1)k + 7m² - m.
  
  This is a quadratic in k: f(k) = k² - (2m+1)k + 7m² - m. Discriminant: (2m+1)² - 4(7m² - m) = 4m² + 4m + 1 - 28m² + 4m = -24m² + 8m + 1. For m ≥ 1, this is -24 + 8 + 1 = -15 < 0. So f(k) > 0 for all k (since the leading coefficient is positive and discriminant is negative). ✓

For k > 6m (i.e., 6m < k ≤ 7m): ∑_{i=1}^k d_i = 6m · m + (k - 6m)(m-1) = 6m² + (k-6m)(m-1). RHS = k(k-1) + ∑_{i=k+1}^{7m} min(d_i, k). The remaining 7m - k vertices all have degree m - 1. min(m-1, k) = m - 1 (since k > 6m ≥ m - 1 for m ≥ 1). RHS = k(k-1) + (7m - k)(m-1).

Need: 6m² + (k-6m)(m-1) ≤ k(k-1) + (7m-k)(m-1).
6m² + (k-6m)(m-1) ≤ k(k-1) + (7m-k)(m-1)
6m² + (k-6m)(m-1) - (7m-k)(m-1) ≤ k(k-1)
6m² + (m-1)(k - 6m - 7m + k) ≤ k(k-1)
6m² + (m-1)(2k - 13m) ≤ k(k-1)
6m² + 2k(m-1) - 13m(m-1) ≤ k² - k
6m² + 2km - 2k - 13m² + 13m ≤ k² - k
-7m² + 13m + 2km - 2k ≤ k² - k
-7m² + 13m + 2km - k ≤ k²
k² - 2km + k + 7m² - 13m ≥ 0
k² - (2m-1)k + 7m² - 13m ≥ 0

Discriminant: (2m-1)² - 4(7m² - 13m) = 4m² - 4m + 1 - 28m² + 52m = -24m² + 48m + 1.
For m = 1: -24 + 48 + 1 = 25 > 0. Roots: k = (1 ± 5)/2, so k = 3 or k = -2. For k ∈ (6m, 7m] = (6, 7], i.e., k = 7: f(7) = 49 - 13·1 + 7 - 13 = 49 - 13 + 7 - 13 = 30 > 0. ✓ (Actually let me recompute: f(7) = 49 - (2-1)·7 + 7 - 13 = 49 - 7 + 7 - 13 = 36 > 0. ✓)

For m = 2: discriminant = -96 + 96 + 1 = 1 > 0. Roots: k = (3 ± 1)/2, so k = 2 or k = 1. For k ∈ (12, 14], i.e., k = 13 or 14: f(13) = 169 - 3·13 + 28 - 26 = 169 - 39 + 28 - 26 = 132 > 0. ✓

For m ≥ 3: discriminant = -24m² + 48m + 1. At m = 3: -216 + 144 + 1 = -71 < 0. So for m ≥ 3, discriminant < 0, and f(k) > 0 for all k. ✓

For m = 1 and m = 2, we verified f(k) > 0 for the relevant k values. ✓

So the Erdős–Gallai conditions are satisfied, and a graph with this degree sequence exists for all m ≥ 1.

Now, does this graph satisfy the Hakimi condition (7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) for all S)?

This is not automatic just from the degree sequence. We need to choose the right graph. Let me think about what graph to use.

Actually, let me think about this more carefully. The Hakimi condition is:
7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) for all S ⊆ V.

Equivalently (using |δ_{G_m}(S)| = ∑_{v ∈ S} deg(v) - 2|E(G_m[S])|):
7|E(G_m[S])| + 3(∑_{v ∈ S} deg(v) - 2|E(G_m[S])|) ≥ C(|S|, 2)
7e + 3D - 6e ≥ C(|S|, 2)
e + 3D ≥ C(|S|, 2)
|E(G_m[S])| + 3∑_{v ∈ S} deg(v) ≥ C(|S|, 2)

where D = ∑_{v ∈ S} deg(v).

So the condition is: |E(G_m[S])| + 3∑_{v ∈ S} deg(v) ≥ C(|S|, 2) = |S|(|S|-1)/2.

Since |E(G_m[S])| ≥ 0, a sufficient condition is 3∑_{v ∈ S} deg(v) ≥ |S|(|S|-1)/2, i.e., the average degree in S is at least (|S|-1        — AI历史解题过程（thinking）
#   polymath_04417         — 题目ID

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
  <problem_id>polymath_04417</problem_id>
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

We have a group of $n$ kids. For each pair of kids, at least one has sent a message to the other one. For each kid $A$, among the kids to whom $A$ has sent a message, exactly $25 \%$ have sent a message to $A$. How many possible two-digit values of $n$ are there?

## Standard Solution

If the number of pairs of kids with two-way communication is $k$, then by the given condition the total number of messages is $4 k+4 k=8 k$. Thus the number of pairs of kids is $\frac{n(n-1)}{2}=7 k$. This is possible only if $n \equiv 0,1 \bmod 7$.

- In order to obtain $n=7 m+1$, arrange the kids in a circle and let each kid send a message to the first $4 m$ kids to its right and hence receive a message from the first $4 m$ kids to its left. Thus there are exactly $m$ kids to which it has both sent and received messages.
- In order to obtain $n=7 m$, let kid $X$ send no messages (and receive from every other kid). Arrange the remaining $7 m-1$ kids in a circle and let each kid on the circle send a message to the first $4 m-1$ kids to its right and hence receive a message from the first $4 m-1$ kids to its left. Thus there are exactly $m$ kids to which it has both sent and received messages.

There are 26 two-digit numbers with remainder 0 or 1 modulo 7 . (All numbers of the form $7 m$ and $7 m+1$ with $2 \leqslant m \leqslant 14$.)

Alternative Solution by PSC. Suppose kid $x_{i}$ sent $4 d_{i}$ messages. (Guaranteed by the conditions to be a multiple of 4.) Then it received $d_{i}$ messages from the kids that it has sent a message to, and another $n-1-4 d_{i}$ messages from the rest of the kids. So it received a total of $n-1-3 d_{i}$ messages. Since the total number of messages sent is equal to the total number of messages received, we must have:

$$
d_{1}+\cdots+d_{n}=\left(n-1-3 d_{1}\right)+\cdots+\left(n-1-3 d_{n}\right)
$$

This gives $7\left(d_{1}+\cdots+d_{n}\right)=n(n-1)$ from which we get $n \equiv 0,1 \bmod 7$ as in the first solution.

We also present an alternative inductive construction (which turns out to be different from the construction in the first solution).

For the case $n \equiv 0 \bmod 7$, we start with a construction for $7 k$ kids, say $x_{1}, \ldots, x_{7 k}$, and another construction with 7 kids, say $y_{1}, \ldots, y_{7}$. We merge them by demanding that in addition, each kid $x_{i}$ sends and receives gifts according to the following table:

| $i \bmod 7$ | Sends | Receives |
| :---: | :---: | :---: |
| 0 | $y_{1}, y_{2}, y_{3}, y_{4}$ | $y_{4}, y_{5}, y_{6}, y_{7}$ |
| 1 | $y_{2}, y_{3}, y_{4}, y_{5}$ | $y_{5}, y_{6}, y_{7}, y_{1}$ |
| 2 | $y_{3}, y_{4}, y_{5}, y_{6}$ | $y_{6}, y_{7}, y_{1}, y_{2}$ |
| 3 | $y_{4}, y_{5}, y_{6}, y_{7}$ | $y_{7}, y_{1}, y_{2}, y_{3}$ |
| 4 | $y_{5}, y_{6}, y_{7}, y_{1}$ | $y_{1}, y_{2}, y_{3}, y_{4}$ |
| 5 | $y_{6}, y_{7}, y_{1}, y_{2}$ | $y_{2}, y_{3}, y_{4}, y_{5}$ |
| 6 | $y_{7}, y_{1}, y_{2}, y_{3}$ | $y_{3}, y_{4}, y_{5}, y_{6}$ |

So each kid $x_{i}$ sends an additional four messages and receives a message from only one of those four additional kids. Also, each kid $y_{j}$ sends an additional $4 k$ messages and receives from exactly $k$ of those additional kids. So this is a valid construction for $7(k+1)$ kids.

For the case $n \equiv 1 \bmod 7$, we start with a construction for $7 k+1$ kids, say $x_{1}, \ldots, x_{7 k+1}$, and we take another 7 kids, say $y_{1}, \ldots, y_{7}$ for which we do not yet mention how they exchange gifts. The kids $x_{1}, \ldots, x_{7 k+1}$ exchange gifts with the kids $y_{1}, \ldots, y_{7}$ according to the previous table. As before, each kid $x_{i}$ satisfies the conditions. We now put $y_{1}, \ldots, y_{7}$ on a circle and demand that each of $y_{1}, \ldots, y_{3}$ sends gifts to the next four kids on the circle and each of $y_{4}, \ldots, y_{7}$ sends gifts to the next three kids on the circle. It is each to check that the condition is satisfied by each $y_{i}$ as well.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have n kids. For each pair, at least one has sent a message to the other. For each kid A, among the kids A sent messages to, exactly 25% have sent a message back to A.

Let me model this as a directed graph. Each kid is a vertex. For each pair {A,B}, at least one of A→B or B→A exists (could be both - mutual). For each vertex A: let d_out(A) = number of kids A sent messages to. Among these d_out(A) kids, exactly 25% sent a message back to A. So the number of kids B such that both A→B and B→A exist is exactly d_out(A)/4. This means d_out(A) is divisible by 4. Let d_out(A) = 4k_A for some integer k_A. The number of mutual connections from A's perspective is k_A. Let me define: for each ordered pair, we have a directed edge. Let M = number of mutual pairs (unordered pairs where both directions exist). Let S = number of single-direction pairs (unordered pairs where exactly one direction exists). Total unordered pairs = M + S = C(n,2). For each vertex A, d_out(A) = out-degree. The number of mutual neighbors of A (kids B where both A→B and B→A) = k_A = d_out(A)/4.

The number of mutual pairs M = (1/2) * sum over A of k_A = (1/2) * sum d_out(A)/4 = (1/8) * sum d_out(A).

Also, sum d_out(A) = total directed edges = S + 2M (each single pair contributes 1 edge, each mutual contributes 2).

So sum d_out(A) = S + 2M.

And M = (1/8)(S + 2M), so 8M = S + 2M, thus S = 6M.

Total pairs: M + S = M + 6M = 7M = C(n,2) = n(n-1)/2.

So n(n-1)/2 = 7M, meaning n(n-1) = 14M.

So n(n-1) ≡ 0 (mod 14), i.e., 14 | n(n-1).

Since gcd(n, n-1) = 1, we need 2 | n(n-1) (always true) and 7 | n(n-1). So 7 | n or 7 | (n-1), i.e., n ≡ 0 or 1 (mod 7).

Now we also need d_out(A) divisible by 4 for each A, and the structure to be realizable.

Wait, but we need more constraints. The condition is that for each A, exactly 25% of A's out-neighbors have sent a message back. We derived n ≡ 0 or 1 (mod 7) as necessary. But is it sufficient? We need to check that for each such n, there exists a valid configuration.

Let me think about sufficiency. We need to construct, for each n ≡ 0 or 1 (mod 7) with n being a two-digit number (10 ≤ n ≤ 99), a directed graph satisfying the conditions.

Actually, let me think more carefully. We need each vertex to have d_out(A) ≡ 0 (mod 4), and the mutual structure to work out.

Let me think about this differently. Consider the structure where we partition into groups.

Actually, let me think about a concrete construction. Consider a tournament-like structure but with some mutual edges.

Let me think about the problem more carefully. We have a "semi-complete" digraph (for each pair, at least one direction). For each vertex v, out-degree d(v), and the number of vertices u with both v→u and u→v is exactly d(v)/4.

Let me think of a construction. Take n ≡ 0 (mod 7), say n = 7m. Partition the n kids into 7 groups of m each: G_0, G_1, ..., G_6.

Define the edges as follows: for groups G_i and G_j (i ≠ j), if (j - i) mod 7 ∈ {1, 2, 3}, then all edges go from G_i to G_j (i.e., every kid in G_i sends to every kid in G_j). If (j - i) mod 7 ∈ {4, 5, 6}, then all edges go from G_j to G_i.

Within each group G_i, make all edges mutual (every kid sends to every other kid in the same group).

This is like a regular tournament on 7 groups, where the "tournament" is the cyclic tournament on 7 vertices, plus mutual edges within groups.

Now let's check: for a kid A in group G_i:
- Out-neighbors: all kids in G_i (except A itself) = m-1, plus all kids in groups G_j where (j-i) mod 7 ∈ {1,2,3} = 3m.
- So d_out(A) = (m-1) + 3m = 4m - 1.

Hmm, that's 4m - 1, which is not divisible by 4 in general. Let me reconsider.

The mutual neighbors of A: kids B where both A→B and B→A. This happens only within G_i (since between groups, edges are one-directional). So mutual neighbors = m - 1.

We need mutual neighbors = d_out(A)/4 = (4m-1)/4. This requires 4 | (4m-1), which is impossible since 4m-1 ≡ 3 (mod 4).

So this construction doesn't work directly. Let me adjust.

The issue is the within-group edges. Let me try making within-group edges one-directional too, following the cyclic tournament pattern extended.

Actually, let me reconsider. Let me think of the whole thing as a regular tournament on n vertices where n ≡ 0 or 1 (mod 7)... no wait, tournaments don't have mutual edges.

Let me reconsider the problem. We need a mixed graph (some pairs mutual, some single). Let me think about what configurations work.

Let me reconsider. The key equation is n(n-1) = 14M, so M = n(n-1)/14. For M to be a positive integer, we need 14 | n(n-1), giving n ≡ 0 or 1 (mod 7).

But we also need the per-vertex conditions to be satisfiable. Let me think about whether there are additional constraints.

For each vertex A: d_out(A) = 4k_A, and A has exactly k_A mutual neighbors. The sum of k_A over all A = 2M = n(n-1)/7.

The sum of d_out(A) = S + 2M = 6M + 2M = 8M = 8n(n-1)/14 = 4n(n-1)/7.

Average d_out = 4(n-1)/7. Average k = (n-1)/7.

For this to make sense, we need (n-1)/7 to be a non-negative integer on average, but individual vertices can vary.

Actually, let me think about whether we can always construct such a graph when n ≡ 0 or 1 (mod 7).

Case 1: n ≡ 1 (mod 7), say n = 7m + 1.

Consider a regular tournament on n vertices. A regular tournament on n vertices (n odd) has each vertex with out-degree (n-1)/2. But we need mutual edges...

Let me think differently. Let me consider a construction based on a "regular" structure.

Let me try: n = 7m + 1. Take the cyclic group Z_n. For each pair {i, j}, define the edge structure based on the difference d = (j - i) mod n.

In a Paley-like tournament: for n ≡ 1 (mod 7)... hmm, this is getting complicated.

Let me try a different approach. Let me think about small cases and see if the construction works.

For n = 7: M = 7·6/14 = 3. S = 18. Each vertex: average d_out = 4·6/7 = 24/7, which is not an integer. So we can't have all vertices with the same out-degree. But the problem doesn't require regular out-degree.

For n = 7, we need sum d_out = 4·7·6/7 = 24, and sum k_A = 2·3 = 6. Each d_out(A) ≡ 0 (mod 4), so d_out(A) ∈ {0, 4, 8, 12, ...}. With 7 vertices and sum 24, possible distributions: e.g., six vertices with d_out = 4 and one with d_out = 0. Sum = 24. ✓

Then k_A = d_out(A)/4, so six vertices with k=1 and one with k=0. Sum k = 6 = 2M. ✓

Can we realize this? We need 3 mutual pairs and 18 single edges. The vertex with d_out = 0 has no out-edges, so all its edges are incoming (6 incoming single edges). It has k=0, so no mutual edges involving it.

The other 6 vertices each have d_out = 4 and k = 1 (one mutual neighbor). Among the 6 vertices (excluding the special one), there are C(6,2) = 15 pairs. The 3 mutual pairs are among these 6 vertices. Each of the 6 vertices is in exactly 1 mutual pair, so the 3 mutual pairs form a perfect matching on the 6 vertices. ✓

Each of the 6 vertices has d_out = 4. One out-edge goes to its mutual partner. The other 3 out-edges go to... other vertices. Each vertex has 5 possible neighbors among the other 5 non-special vertices, plus the special vertex. The special vertex has no out-edges, so the edge between a non-special vertex and the special vertex is single, directed from non-special to special. So each non-special vertex has 1 out-edge to the special vertex.

So out-edges from a non-special vertex A: 1 to special vertex, 1 to mutual partner, and 2 more to other non-special vertices. Total = 4. ✓

Among the 6 non-special vertices, after removing the 3 mutual pairs, we have 15 - 3 = 12 pairs, each single-direction. Each vertex has 4 other non-special non-partner vertices, and needs 2 out-edges among them. So we need a tournament on 6 vertices (the non-partner edges) where each vertex has out-degree 2. That's a regular tournament on 6 vertices... but 6 is even, so a regular tournament doesn't exist (regular tournaments need odd number of vertices).

Wait, let me recount. Each non-special vertex A has 5 other non-special vertices. One is its mutual partner (1 out-edge). The remaining 4 are connected by single edges. A needs 2 out-edges among these 4. So we need an orientation of K_6 minus a perfect matching where each vertex has out-degree 2. K_6 minus a perfect matching is a 4-regular graph on 6 vertices. We need to orient it so each vertex has out-degree 2, i.e., a regular orientation (Eulerian orientation). This exists for any even-degree regular graph. ✓ (A 4-regular graph has an Eulerian circuit, and orienting along the circuit gives out-degree = in-degree = 2 at each vertex.)

So n = 7 works.

Now, the question is: for which two-digit n (10 ≤ n ≤ 99) with n ≡ 0 or 1 (mod 7) can we construct a valid configuration?

Two-digit values with n ≡ 0 (mod 7): 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98.
Two-digit values with n ≡ 1 (mod 7): 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99.

Wait, let me list them:
n ≡ 0 (mod 7): 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98 → 13 values
n ≡ 1 (mod 7): 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99 → 13 values

Total: 26 values.

But I need to verify that each of these can actually be realized. The necessary condition is n ≡ 0 or 1 (mod 7), but there might be additional constraints from the divisibility by 4 requirement.

Let me think about whether there are additional constraints. We need each d_out(A) ≡ 0 (mod 4). The sum of d_out = 4n(n-1)/7. For this to be achievable with each d_out ≡ 0 (mod 4), we need... well, the sum is already divisible by 4 (it's 4 times something). So as long as we can distribute the out-degrees appropriately, it should work.

But we also need 0 ≤ d_out(A) ≤ n-1 for each vertex, and d_out(A) ≡ 0 (mod 4), and the graph structure to be realizable.

Let me think about this more carefully. The average out-degree is 4(n-1)/7. For n = 7m, average = 4(7m-1)/7 = 4m - 4/7. For n = 7m+1, average = 4·7m/7 = 4m.

For n = 7m+1: average out-degree = 4m, which is divisible by 4. So we could try a regular construction where every vertex has d_out = 4m and k = m.

For n = 7m: average out-degree = 4m - 4/7, not an integer. So we can't have all vertices with the same out-degree. We need some variation.

Let me think about the n = 7m+1 case first, as it seems cleaner.

**Case n = 7m + 1:**

We want a regular structure where every vertex has d_out = 4m and k = m (m mutual neighbors).

Consider Z_n = Z_{7m+1}. Define the edge structure using a "difference set" approach.

For each unordered pair {i, j}, let d = (j - i) mod n (taking the representative in {1, 2, ..., n-1}, and also considering n - d). We need to decide: is the edge i→j, j→i, or both?

We want: for each vertex i, exactly 4m out-neighbors and m mutual neighbors.

Think of it as: partition the non-zero residues mod n into "out-differences" D_out (i sends to i+d for d ∈ D_out), "in-differences" D_in (i receives from i+d, i.e., j→i where d = i-j... let me be more careful).

Let me use the standard approach. For vertex i, define:
- Out-neighbors: {i + d mod n : d ∈ D_out} where D_out is a subset of {1, ..., n-1}.
- For the edge between i and j (j = i + d), it's mutual iff both d ∈ D_out and -d ∈ D_out (i.e., n-d ∈ D_out).

Wait, let me set it up properly. We work in Z_n. For each pair {i, j} with difference d = j - i (mod n), we choose one of three options:
1. i → j only (d ∈ D_out, -d ∉ D_out)
2. j → i only (-d ∈ D_out, d ∉ D_out)
3. Both (d ∈ D_out and -d ∈ D_out)

where D_out is the set of "out-differences" and the construction is vertex-transitive: vertex i sends to i + d for all d ∈ D_out.

For this to be well-defined, for each pair {d, -d}, we need to decide. Let's say:
- If d ∈ D_out and -d ∈ D_out: mutual edges for difference d.
- If d ∈ D_out and -d ∉ D_out: edge goes in direction of d (i → i+d).
- If d ∉ D_out and -d ∈ D_out: edge goes in direction of -d.
- If d ∉ D_out and -d ∉ D_out: impossible (no edge), but we need at least one edge per pair.

So we need: for each pair {d, -d} with d ≠ 0, at least one of d, -d is in D_out.

|D_out| = d_out for each vertex = 4m.

Mutual neighbors: for each d ∈ D_out with -d ∈ D_out, vertex i has a mutual edge with i+d. The number of such d is the number of d ∈ D_out with -d ∈ D_out. Since the construction is symmetric, this equals |D_out ∩ (-D_out)|. We need this to be m.

Also, |D_out| = 4m, and D_out ∪ (-D_out) = {1, ..., n-1} \ {d : d ∉ D_out and -d ∉ D_out}. But we need D_out ∪ (-D_out) = {1, ..., n-1} (every pair has at least one edge). So |D_out ∪ (-D_out)| = n - 1 = 7m.

|D_out ∪ (-D_out)| = |D_out| + |-D_out| - |D_out ∩ (-D_out)| = 4m + 4m - m = 7m. ✓

So we need a subset D_out of Z_n \ {0} with:
- |D_out| = 4m
- |D_out ∩ (-D_out)| = m
- D_out ∪ (-D_out) = Z_n \ {0}

The last condition means every non-zero residue is in D_out or its negative is. The second condition means exactly m elements d of D_out have -d also in D_out (these come in pairs {d, -d}, so there are m/2 such pairs if m is even, or... wait).

Hmm, |D_out ∩ (-D_out)| = m. The elements in D_out ∩ (-D_out) are those d where both d and -d are in D_out. These come in pairs {d, -d} (unless d = -d, i.e., d = n/2, which requires n even). For n = 7m+1:
- If m is even, n = 7m+1 is odd, so no self-inverse element. The m elements in D_out ∩ (-D_out) form m/2 pairs. So m must be even.
- If m is odd, n = 7m+1 is even, so n/2 = (7m+1)/2 is an integer. The element n/2 is self-inverse. So D_out ∩ (-D_out) could include n/2 (contributing 1) plus (m-1)/2 pairs. So m can be odd.

Wait, but actually we need to be more careful. Let me reconsider.

The pairs {d, -d} partition Z_n \ {0} into (n-1)/2 pairs if n is odd, or (n-2)/2 pairs plus the singleton {n/2} if n is even.

For n = 7m+1:
- n odd iff m even. Then (n-1)/2 = 7m/2 pairs. We need m elements in D_out ∩ (-D_out), forming m/2 complete pairs (both d and -d in D_out). The remaining 7m/2 - m/2 = 3m pairs have exactly one element in D_out. Total |D_out| = m + 3m = 4m. ✓ Need m even.
- n even iff m odd. Then (n-2)/2 = (7m-1)/2 pairs plus singleton {n/2}. We need m elements in D_out ∩ (-D_out). If n/2 ∈ D_out, it contributes 1 (self-paired). Then we need (m-1)/2 complete pairs. Remaining pairs: (7m-1)/2 - (m-1)/2 = 3m pairs with one element each. Total |D_out| = 1 + (m-1) + 3m = 4m. ✓ Need m odd (and n/2 ∈ D_out).

OR if n/2 ∉ D_out: then we need m/2 complete pairs, requiring m even. But m is odd here, contradiction. So for m odd, we must include n/2 ∈ D_out.

So for n = 7m+1:
- m even: construction possible (need m/2 mutual-difference pairs and 3m single-difference pairs).
- m odd: construction possible (include n/2, plus (m-1)/2 mutual-difference pairs and 3m single-difference pairs).

So it seems like for all m ≥ 1, the construction is possible for n = 7m+1. We just need to verify that we can always choose the right number of pairs.

For m even (n odd): we need to choose m/2 out of 7m/2 pairs to be "mutual" (both directions), and from the remaining 3m pairs, choose one element each for D_out. This is always possible as long as m/2 ≤ 7m/2, which is true for m ≥ 0.

For m odd (n even): include n/2 in D_out, choose (m-1)/2 out of (7m-1)/2 pairs to be mutual, and from remaining 3m pairs choose one each. Always possible.

So for n = 7m+1, the construction works for all m ≥ 1, i.e., n ≥ 8. Since we need two-digit n, n ≥ 10, so all n = 7m+1 with n ≥ 10 work.

Two-digit n ≡ 1 (mod 7): 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99. All work.

**Case n = 7m:**

Average out-degree = 4(7m-1)/7 = 4m - 4/7. Not an integer, so we can't have a regular construction.

We need sum d_out = 4n(n-1)/7 = 4·7m·(7m-1)/7 = 4m(7m-1) = 28m² - 4m.

Each d_out ≡ 0 (mod 4). Sum = 28m² - 4m = 4(7m² - m). So sum/4 = 7m² - m = m(7m-1).

We need n = 7m vertices, each with d_out ≡ 0 (mod 4), summing to 4m(7m-1).

Average d_out = 4m(7m-1)/(7m) = 4(7m-1)/7 = 4m - 4/7.

So some vertices have d_out = 4m and some have d_out = 4m - 4 (or other multiples of 4).

If x vertices have d_out = 4m and (7m - x) have d_out = 4(m-1) = 4m - 4:
Sum = x·4m + (7m-x)·(4m-4) = 4mx + 28m² - 4m·7m + 4x - 28m + 4·7m... let me redo.

Sum = x·4m + (7m-x)·(4m-4) = 4mx + (7m)(4m-4) - x(4m-4) = 4mx + 28m² - 28m - 4mx + 4x = 28m² - 28m + 4x.

We need this = 28m² - 4m. So 28m² - 28m + 4x = 28m² - 4m, giving 4x = 24m, x = 6m.

So 6m vertices with d_out = 4m and m vertices with d_out = 4m - 4 = 4(m-1).

Check: 6m + m = 7m = n. ✓

For the 6m vertices with d_out = 4m: k = m.
For the m vertices with d_out = 4(m-1): k = m-1.

Sum of k = 6m·m + m·(m-1) = 6m² + m² - m = 7m² - m = m(7m-1). And 2M = n(n-1)/7 = 7m(7m-1)/7 = m(7m-1). ✓

Now, can we construct such a graph? This is more complex. Let me think about a construction.

Consider 7 groups: G_0, ..., G_6, each of size m. Use the cyclic tournament structure on the groups (group i beats group j if (j-i) mod 7 ∈ {1,2,3}), and within groups, use a specific structure.

For a vertex in group G_i:
- Out-edges to other groups: 3m (groups G_{i+1}, G_{i+2}, G_{i+3}).
- Out-edges within G_i: need to determine.

For the 6m vertices with d_out = 4m: out-edges within group = 4m - 3m = m. So within a group of m vertices, each of these vertices has m out-edges within the group. But there are only m-1 other vertices in the group! So m out-edges within the group is impossible (max is m-1).

Hmm, that doesn't work. Let me reconsider.

Wait, maybe the within-group edges should be mutual for some and the cross-group edges should also have some mutual ones.

Let me reconsider the construction. Maybe I should allow some cross-group mutual edges.

Actually, let me reconsider. The issue is that with the cyclic tournament on 7 groups, each vertex has 3m out-edges to other groups and needs 4m total (or 4m-4 for some). The within-group contribution is m (or m-4). With m-1 other vertices in the group, m out-edges is too many.

So the pure cyclic tournament approach doesn't directly work for n = 7m. Let me think of another construction.

Alternative: use a different group structure. Let me think about n = 7m where we use a vertex-transitive construction on Z_{7m}.

Hmm, but the average out-degree isn't an integer, so vertex-transitive won't work.

Let me think about this differently. Maybe use a construction based on Z_{7m} but not vertex-transitive.

Actually, let me think about it as follows. Consider Z_{7m} = Z_7 × Z_m (since gcd(7, m) might not be 1, this isn't always a product, but let me think of it as 7 blocks of m consecutive elements).

Actually, let me try a different approach. Let me consider the problem on Z_n where n = 7m, and use a "near-regular" construction.

Let me define D_out as a subset of Z_{7m} \ {0} with |D_out| = 4m for most vertices but adjusted for some.

This is getting complicated. Let me try a different approach entirely.

Let me think about it as a "blow-up" construction. Take the n=7 construction (which we verified works) and blow it up.

For n = 7: we had 6 vertices with d_out = 4, k = 1, and 1 vertex with d_out = 0, k = 0. The 6 vertices form 3 mutual pairs, and the remaining edges among the 6 form a regular tournament on K_6 minus a perfect matching.

To blow up to n = 7m: replace each vertex v with a group of m vertices. Replace each single edge u→v with all m² edges from group(u) to group(v). Replace each mutual edge u↔v with all m² mutual edges between group(u) and group(v). Within each group, we need to define edges.

For a vertex in a group corresponding to a vertex with d_out = 4 in the base:
- Out-edges to other groups: 4m (from the 4 out-edges of the base vertex, each blown up to m).
- Within group: m-1 other vertices. We need total d_out = 4m, so within-group out-edges = 0. But we need at least one edge per pair within the group!

So within each group, we need to orient the complete graph on m vertices. If we make all within-group edges single (tournament), each vertex has some out-degree within the group. This adds to the total out-degree.

For a vertex in a "d_out = 4" group: cross-group out-edges = 4m. Within-group out-edges = some value t (0 ≤ t ≤ m-1). Total d_out = 4m + t. We need this ≡ 0 (mod 4), so t ≡ 0 (mod 4).

For a vertex in the "d_out = 0" group: cross-group out-edges = 0. Within-group out-edges = t. Total d_out = t. Need t ≡ 0 (mod 4).

Also, mutual neighbors: for a vertex in a "d_out = 4, k = 1" group, the cross-group mutual neighbors = m (from the 1 mutual edge blown up). Within-group mutual neighbors = 0 (if within-group is a tournament, no mutual edges). So k = m. We need d_out/4 = (4m + t)/4 = m + t/4. So we need m = m + t/4, giving t = 0.

But t = 0 means no out-edges within the group, which means all within-group edges are incoming for this vertex. But for a pair within the group, at least one direction must exist. If vertex A has t = 0 (no out-edges within group) and vertex B also has t = 0, then the pair {A, B} has no edge. Contradiction.

So the blow-up with tournament within groups doesn't work directly. Let me allow mutual edges within groups.

If within-group edges are all mutual: each vertex has m-1 out-edges within group (all mutual) and m-1 mutual neighbors within group.

For a "d_out = 4" group vertex: cross-group out = 4m, within-group out = m-1. Total d_out = 4m + m - 1 = 5m - 1. Need ≡ 0 (mod 4): 5m - 1 ≡ 0 (mod 4), i.e., m - 1 ≡ 0 (mod 4), m ≡ 1 (mod 4).

Mutual neighbors: cross-group = m, within-group = m-1. Total k = 2m - 1. Need d_out/4 = (5m-1)/4. So 2m - 1 = (5m-1)/4, giving 8m - 4 = 5m - 1, 3m = 3, m = 1. Only works for m = 1 (n = 7).

So that doesn't generalize either. The blow-up approach is too rigid.

Let me think about this more carefully. Maybe I should consider a completely different construction for n = 7m.

Let me try to construct directly for n = 7m using Z_n.

We need 6m vertices with d_out = 4m, k = m, and m vertices with d_out = 4(m-1), k = m-1.

Hmm, actually, the distribution of out-degrees doesn't have to be exactly this. There could be other distributions. Let me think more generally.

We need:
- n = 7m vertices
- Each d_out ≡ 0 (mod 4)
- Sum d_out = 4m(7m-1)
- For each vertex, mutual neighbors = d_out/4
- Sum of mutual neighbors = m(7m-1) = 2M

One approach: use a circulant-like construction but with two types of vertices.

Actually, let me try yet another approach. Let me consider the problem on Z_n where n = 7m and try to find a difference-set-like structure.

Let me partition Z_{7m} \ {0} into pairs {d, -d}. There are (7m-1)/2 pairs if 7m is odd (m odd), or (7m-2)/2 pairs plus {7m/2} if 7m is even (m even).

For a vertex-transitive construction, we'd need all vertices to have the same d_out, but the average isn't an integer, so this is impossible. We need a non-vertex-transitive construction.

Let me try a different approach. Consider the following construction for n = 7m:

Partition the n vertices into 7 groups G_0, ..., G_{6}, each of size m. Use the cyclic tournament on the 7 groups: G_i → G_j if (j - i) mod 7 ∈ {1, 2, 3}, and G_j → G_i if (j - i) mod 7 ∈ {4, 5, 6}.

Between groups G_i and G_j (i ≠ j): all edges go in one direction (no mutual edges between groups).

Within each group G_i: we need to define the edge structure. Each vertex in G_i has 3m out-edges to other groups (from the cyclic tournament). We need total d_out ≡ 0 (mod 4), so within-group out-degree ≡ -3m ≡ 0 (mod 4), i.e., 3m ≡ 0 (mod 4), i.e., m ≡ 0 (mod 4).

If m ≡ 0 (mod 4), say m = 4t, then within-group out-degree needs to be ≡ 0 (mod 4). We can use a regular tournament within each group if m is odd... but m = 4t is even. So we can't have a regular tournament.

Hmm, let me think about this differently. Within each group of size m, we need a semi-complete digraph (at least one edge per pair) where each vertex has out-degree ≡ 0 (mod 4) and the mutual structure satisfies the 25% condition.

Actually wait. The mutual neighbors of a vertex come from both within-group and between-group edges. In this construction, between-group edges are all single-direction (no mutual). So mutual neighbors only come from within-group edges.

For a vertex in G_i with within-group out-degree w and within-group mutual neighbors w/4 (if the within-group structure satisfies the 25% condition):
- Total d_out = 3m + w
- Total k = w/4
- Need k = d_out/4 = (3m + w)/4
- So w/4 = (3m + w)/4, giving 0 = 3m/4, so m = 0. Contradiction!

So the between-group edges can't all be single-direction. We need some mutual edges between groups.

OK let me take a step back and think about this more carefully.

The 25% condition is global: for each vertex, among ALL its out-neighbors, 25% sent a message back. So mutual neighbors / out-degree = 1/4.

If between-group edges are all single, then mutual neighbors = within-group mutual neighbors, and out-degree = 3m + within-group out-degree. The condition becomes:

within-mutual / (3m + within-out) = 1/4

If within-group is also a 25%-structure: within-mutual = within-out / 4. Then:

(within-out / 4) / (3m + within-out) = 1/4
within-out / 4 = (3m + within-out) / 4
within-out = 3m + within-out
0 = 3m

Contradiction again. So we can't have all between-group edges be single.

We need between-group mutual edges. Let me reconsider.

Let me try a construction where between groups, we have a mix of single and mutual edges.

Consider 7 groups of size m. For groups G_i and G_j with (j-i) mod 7 ∈ {1,2,3} (G_i → G_j direction):
- Some edges from G_i to G_j are mutual, some are single (G_i → G_j only).

Let's say a fraction of the m² edges between G_i and G_j are mutual. Specifically, let's say each vertex in G_i has a mutual edge with some vertices in G_j and a single out-edge to the rest.

This is getting complex. Let me try a cleaner approach.

**Clean approach using difference sets on Z_n:**

For n = 7m, consider Z_n. Let me try to find a set D_out ⊂ Z_n \ {0} (not necessarily giving a vertex-transitive graph, but let me first try).

For vertex-transitive: |D_out| = 4m, |D_out ∩ (-D_out)| = m, D_out ∪ (-D_out) = Z_n \ {0}.

|D_out ∪ (-D_out)| = |D_out| + |D_out| - |D_out ∩ (-D_out)| = 4m + 4m - m = 7m = n. But Z_n \ {0} has n - 1 = 7m - 1 elements. So 7m = 7m - 1 is a contradiction.

So vertex-transitive is impossible for n = 7m, confirming our earlier finding.

OK so I need a non-vertex-transitive construction. Let me think about using two types of vertices.

Let me use the structure: Z_n = Z_7 × Z_m (when gcd(7, m) = 1, i.e., m not divisible by 7; but even when it's not a direct product, I can think of elements as (g, h) with g ∈ Z_7, h ∈ Z_m).

Actually, let me just think of the n = 7m vertices as arranged in a 7 × m grid: vertex (i, j) where i ∈ {0,...,6}, j ∈ {0,...,m-1}.

Define the edge structure:
1. Between (i, j) and (i, j') in the same group (same i): make all edges mutual. So each vertex has m-1 mutual neighbors within its group, and m-1 out-edges within its group.

2. Between groups: use the cyclic tournament. (i, j) → (i', j') for all j, j' if (i' - i) mod 7 ∈ {1, 2, 3}. These are single edges.

For vertex (i, j):
- Out-degree: (m-1) [within group] + 3m [to three other groups] = 4m - 1.
- Mutual neighbors: m - 1 [within group].
- Need: mutual / out = 1/4, so (m-1)/(4m-1) = 1/4, giving 4(m-1) = 4m - 1, 4m - 4 = 4m - 1, -4 = -1. Contradiction.

Doesn't work. The within-group mutual edges contribute too much to the ratio.

Let me try: within-group edges are single (tournament), and between-group edges have some mutual ones.

3. Within group i: regular tournament (if m is odd) or some tournament. Each vertex has (m-1)/2 out-edges within group (if m odd, regular tournament).

4. Between groups G_i and G_{i+1} (mod 7): all m² edges are from G_i to G_{i+1}. Some are mutual, some single.

Let me parameterize: for the edge between groups G_i and G_j (where G_i → G_j), let each vertex in G_i have a mutual edge with exactly r vertices in G_j and a single out-edge to (m - r) vertices in G_j.

By symmetry, assume the structure is the same for all groups (cyclic symmetry).

For vertex (i, j):
- Out-degree: (m-1)/2 [within group, if regular tournament] + 3r [mutual to 3 groups] + 3(m-r) [single to 3 groups] = (m-1)/2 + 3m.
  Wait, the out-edges to group G_{i+d} (d ∈ {1,2,3}) are: r mutual + (m-r) single = m out-edges. So total out to other groups = 3m.
  Total out-degree = (m-1)/2 + 3m.

- Mutual neighbors: 0 [within group, tournament] + 3r [from 3 groups] = 3r.

- Need: 3r / ((m-1)/2 + 3m) = 1/4.
  12r = (m-1)/2 + 3m = (m - 1 + 6m)/2 = (7m - 1)/2.
  r = (7m - 1)/24.

For r to be a non-negative integer: 24 | (7m - 1), i.e., 7m ≡ 1 (mod 24), m ≡ 7^{-1} (mod 24). 7 × 7 = 49 = 48 + 1 ≡ 1 (mod 24). So m ≡ 7 (mod 24).

Also need m odd (for regular tournament within group). m ≡ 7 (mod 24) is odd. ✓

And 0 ≤ r ≤ m: r = (7m-1)/24. For m ≥ 1, r ≥ 0. r ≤ m iff 7m - 1 ≤ 24m iff -1 ≤ 17m, true. ✓

So this construction works when m ≡ 7 (mod 24), i.e., m ∈ {7, 31, 55, ...}, giving n = 7m ∈ {49, 217, ...}. Only n = 49 is two-digit.

But this is just one construction. We need constructions for all n = 7m with 10 ≤ 7m ≤ 99, i.e., 2 ≤ m ≤ 14 (m integer), so n ∈ {14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98}.

The above construction only covers n = 49. We need more general constructions.

Let me think more generally. The within-group structure doesn't have to be a regular tournament, and the between-group structure doesn't have to be symmetric across all 3 "out" groups.

Let me generalize. Within each group of size m, use a semi-complete digraph satisfying the 25% condition (recursively, if possible). Between groups, use the cyclic tournament with some mutual edges.

Actually, this recursive approach could work. Let me think about it.

If within each group of size m, we have a valid 25%-structure where each vertex has out-degree w and mutual neighbors w/4, and between groups we add mutual edges:

For vertex (i, j):
- Out-degree: w [within group] + 3m [to 3 out-groups, all out-edges] = w + 3m.
  Wait, but some of the 3m between-group edges might be mutual. Let me say each vertex has r mutual out-edges to each out-group and (m - r) single out-edges.
  Actually, the out-edges to each out-group total m (r mutual + (m-r) single). So total out to other groups = 3m.
  Total out-degree = w + 3m.

- Mutual neighbors: w/4 [within group] + 3r [from 3 out-groups] = w/4 + 3r.

- Need: (w/4 + 3r) / (w + 3m) = 1/4.
  w/4 + 3r = (w + 3m)/4 = w/4 + 3m/4.
  3r = 3m/4.
  r = m/4.

So r = m/4, requiring 4 | m.

And w can be anything (as long as the within-group structure is valid). So if 4 | m and we can find a valid within-group structure of size m, then we can construct for n = 7m.

For 4 | m: n = 7m with m ∈ {4, 8, 12, ...}, giving n ∈ {28, 56, 84, ...}. Two-digit: 28, 56, 84.

But we also need the within-group structure to be valid. The within-group is a 25%-structure on m vertices. By induction, if m ≡ 0 or 1 (mod 7), we can do it. m = 4: 4 mod 7 = 4, not 0 or 1. So we can't directly use a 25%-structure on 4 vertices.

Hmm, but the within-group structure doesn't have to be a 25%-structure. It just needs to be a semi-complete digraph where each vertex has out-degree w (divisible by 4) and w/4 mutual neighbors. Wait, that IS the 25% condition. So the within-group structure must satisfy the 25% condition, which requires m ≡ 0 or 1 (mod 7).

For m = 4: 4 ≡ 4 (mod 7), not valid. So this recursive approach with m = 4 doesn't work.

Let me reconsider. Maybe the within-group structure doesn't need to satisfy the 25% condition by itself. The 25% condition is global. Let me re-derive.

Actually, I already did the derivation correctly. The within-group contributes w out-edges and w/4 mutual neighbors (if within-group is a 25%-structure). But what if within-group is NOT a 25%-structure?

Let me re-derive without assuming within-group is a 25%-structure.

Within group: each vertex has out-degree w_i and mutual neighbors μ_i (within group). These don't have to satisfy μ_i = w_i/4.

Between groups: each vertex has r mutual out-edges to each of 3 out-groups, and (m-r) single out-edges to each. So 3m out-edges to other groups, 3r mutual from other groups.

Total out-degree = w_i + 3m.
Total mutual = μ_i + 3r.

Need: (μ_i + 3r) / (w_i + 3m) = 1/4 for each vertex.
4(μ_i + 3r) = w_i + 3m.
4μ_i + 12r = w_i + 3m.
12r = w_i + 3m - 4μ_i.
r = (w_i + 3m - 4μ_i) / 12.

For r to be the same for all vertices in a group (by symmetry), we need w_i + 3m - 4μ_i to be the same for all vertices in the group, i.e., w_i - 4μ_i is constant.

If within-group is a 25%-structure, w_i - 4μ_i = 0 for all i, so r = 3m/12 = m/4. (As before.)

If within-group is a tournament (no mutual edges, μ_i = 0), then r = (w_i + 3m) / 12. For this to be constant, w_i must be constant, i.e., regular tournament (m odd). Then r = ((m-1)/2 + 3m) / 12 = (7m - 1) / 24. (As before.)

More generally, we can use any within-group semi-complete digraph where w_i - 4μ_i is constant across vertices. Let's call this constant c. Then r = (c + 3m) / 12.

We need r to be a non-negative integer with 0 ≤ r ≤ m.

So we need:
1. 12 | (c + 3m)
2. 0 ≤ r ≤ m, i.e., 0 ≤ (c + 3m)/12 ≤ m, i.e., 0 ≤ c + 3m ≤ 12m, i.e., -3m ≤ c ≤ 9m.
3. There exists a semi-complete digraph on m vertices where each vertex has w_i - 4μ_i = c, with w_i ≡ 0 (mod 4) and 0 ≤ w_i ≤ m-1, 0 ≤ μ_i ≤ w_i, and the structure is realizable.

Wait, actually w_i doesn't need to be divisible by 4 for the within-group structure. The divisibility by 4 is for the total out-degree: w_i + 3m ≡ 0 (mod 4), i.e., w_i ≡ -3m ≡ m (mod 4) (since -3 ≡ 1 mod 4). So w_i ≡ m (mod 4).

And the total mutual = μ_i + 3r = (w_i + 3m)/4, which is automatically an integer if w_i + 3m ≡ 0 (mod 4).

So the constraints on the within-group structure are:
- w_i ≡ m (mod 4) for all i
- w_i - 4μ_i = c for all i (constant)
- 0 ≤ w_i ≤ m - 1
- 0 ≤ μ_i ≤ w_i
- Semi-complete (at least one edge per pair)
- 12 | (c + 3m), 0 ≤ (c + 3m)/12 ≤ m

This is quite flexible. Let me think about what values of c are achievable.

For a tournament on m vertices (μ_i = 0): w_i = c, and w_i ≡ m (mod 4). For a regular tournament (m odd), w_i = (m-1)/2 for all i. So c = (m-1)/2, and we need (m-1)/2 ≡ m (mod 4), i.e., (m-1)/2 - m ≡ 0 (mod 4), i.e., (-m-1)/2 ≡ 0 (mod 4), i.e., (m+1)/2 ≡ 0 (mod 4), i.e., m + 1 ≡ 0 (mod 8), i.e., m ≡ 7 (mod 8). Combined with m odd (for regular tournament), m ≡ 7 (mod 8) is already odd. And r = (c + 3m)/12 = ((m-1)/2 + 3m)/12 = (7m - 1)/24. Need 24 | (7m - 1). 7m ≡ 1 (mod 24). As computed, m ≡ 7 (mod 24). This is a subset of m ≡ 7 (mod 8).

So for m ≡ 7 (mod 24), the regular tournament within groups works. This gives n = 49, 217, ... Only n = 49 is two-digit from n = 7m.

For other values of m, I need different within-group structures.

Let me think about what within-group structures are possible for small m.

For general m, the simplest within-group structure is:
- All edges mutual: w_i = m - 1, μ_i = m - 1. Then c = (m-1) - 4(m-1) = -3(m-1). w_i = m - 1 ≡ m (mod 4)? Need m - 1 ≡ m (mod 4), i.e., -1 ≡ 0 (mod 4). No.

- All edges single (tournament), not necessarily regular: w_i varies, μ_i = 0, c = w_i. Need w_i constant and ≡ m (mod 4). Regular tournament needs m odd. w_i = (m-1)/2. Need (m-1)/2 ≡ m (mod 4). As above, m ≡ 7 (mod 8).

- Mixed structure. Let me think about using a within-group structure where some edges are mutual and some are single.

This is getting quite involved. Let me try a completely different approach to the construction.

**Alternative approach: direct construction on Z_n for n = 7m.**

Let me think of Z_n where n = 7m. Consider the set of "quadratic residue"-like differences.

Actually, let me try to think about this problem from a higher level. The necessary condition is n ≡ 0 or 1 (mod 7). The question is whether this is also sufficient (for two-digit n).

Let me consider the possibility that the answer is simply the count of two-digit n with n ≡ 0 or 1 (mod 7), which is 26. But I need to verify sufficiency.

Let me try to think about constructions more carefully for each case.

**For n ≡ 1 (mod 7):** We showed a vertex-transitive construction works for all n = 7m + 1 ≥ 8. So all two-digit n ≡ 1 (mod 7) work. That's 13 values.

**For n ≡ 0 (mod 7):** We need n = 7m with 2 ≤ m ≤ 14. We need to show each of these works.

Let me try to find constructions for each m from 2 to 14.

For the within-group approach with 7 groups of size m, I need a within-group semi-complete digraph on m vertices with constant c = w_i - 4μ_i, w_i ≡ m (mod 4), and 12 | (c + 3m), 0 ≤ (c+3m)/12 ≤ m.

Let me think about what within-group structures give constant c.

**Option A: Tournament (μ = 0, c = w).** Need regular (w constant), m odd, w = (m-1)/2, w ≡ m (mod 4), 12 | (w + 3m).
- (m-1)/2 ≡ m (mod 4) → m ≡ 7 (mod 8)
- 12 | ((m-1)/2 + 3m) → 24 | (7m - 1) → m ≡ 7 (mod 24)
- Works for m = 7 (n = 49). Next is m = 31 (too big).

**Option B: All mutual within group (w = μ = m-1, c = -3(m-1)).** Need w ≡ m (mod 4): m - 1 ≡ m (mod 4) → -1 ≡ 0 (mod 4). Never works.

**Option C: Some mix.** Let me think about within-group structures where each vertex has the same (w, μ).

For a vertex-transitive within-group structure on m vertices: w constant, μ constant, c = w - 4μ constant. Need w ≡ m (mod 4), 12 | (w - 4μ + 3m), 0 ≤ (w - 4μ + 3m)/12 ≤ m.

For a vertex-transitive semi-complete digraph on m vertices (using Z_m differences): w = |D|, μ = |D ∩ (-D)|, D ∪ (-D) = Z_m \ {0}, so |D| + |D| - |D ∩ (-D)| = m - 1, i.e., 2w - μ = m - 1, so μ = 2w - m + 1.

Then c = w - 4μ = w - 4(2w - m + 1) = w - 8w + 4m - 4 = -7w + 4m - 4.

r = (c + 3m)/12 = (-7w + 4m - 4 + 3m)/12 = (-7w + 7m - 4)/12 = (7(m - w) - 4)/12.

Need 12 | (7(m - w) - 4). Let d = m - w (the "in-degree from within group" minus... actually d = m - 1 - w is the within-group in-degree, but let me just use d = m - w). Wait, w is the within-group out-degree, and m - 1 - w is the within-group in-degree. So d = m - w = 1 + (in-degree within group).

Hmm, let me just compute. We need 12 | (7d - 4) where d = m - w, and w = |D| for some valid difference set D on Z_m.

7d - 4 ≡ 0 (mod 12). 7d ≡ 4 (mod 12). 7^{-1} mod 12: 7 × 7 = 49 = 48 + 1 ≡ 1 (mod 12). So d ≡ 7 × 4 = 28 ≡ 4 (mod 12). So d ≡ 4 (mod 12).

d = m - w. Since w = |D| and D ∪ (-D) = Z_m \ {0}, we have w ≥ (m-1)/2 (at least half the differences). So d = m - w ≤ m - (m-1)/2 = (m+1)/2. Also d ≥ m - (m-1) = 1 (since w ≤ m - 1).

So d ∈ [1, (m+1)/2] and d ≡ 4 (mod 12). So d ∈ {4, 16, 28, ...} with d ≤ (m+1)/2.

For d = 4: m ≥ 2d - 1 = 7. So m ≥ 7. And w = m - 4, μ = 2(m-4) - m + 1 = m - 7.

Need μ ≥ 0: m ≥ 7. ✓
Need w ≤ m - 1: m - 4 ≤ m - 1. ✓
Need w ≥ (m-1)/2: m - 4 ≥ (m-1)/2, 2m - 8 ≥ m - 1, m ≥ 7. ✓

Also need w ≡ m (mod 4): m - 4 ≡ m (mod 4). ✓ (always true since 4 ≡ 0 mod 4).

And r = (7·4 - 4)/12 = 24/12 = 2. Need 0 ≤ r ≤ m: 2 ≤ m. ✓ for m ≥ 7.

So for m ≥ 7, using a vertex-transitive within-group structure with d = 4 (i.e., w = m - 4, μ = m - 7), we get r = 2. This works!

But we need to verify that such a difference set D exists on Z_m with |D| = m - 4 and |D ∩ (-D)| = m - 7.

|D| = m - 4, |D ∩ (-D)| = m - 7, |D ∪ (-D)| = m - 1.
Check: |D| + |D| - |D ∩ (-D)| = 2(m-4) - (m-7) = 2m - 8 - m + 7 = m - 1. ✓

So D ∪ (-D) = Z_m \ {0} (all non-zero elements covered), and |D ∩ (-D)| = m - 7.

The elements NOT in D are: those in (-D) \ D. |(-D) \ D| = |D| - |D ∩ (-D)| = (m-4) - (m-7) = 3. So exactly 3 elements are in -D but not in D, meaning 3 elements are in D but not in -D (by symmetry of the counting), and m - 7 elements are in both.

Wait, let me recount. |D \ (-D)| = |D| - |D ∩ (-D)| = (m-4) - (m-7) = 3. |(-D) \ D| = |-D| - |D ∩ (-D)| = (m-4) - (m-7) = 3. |D ∩ (-D)| = m - 7. Total: 3 + 3 + (m-7) = m - 1. ✓

So we need: 3 elements in D only, 3 elements in -D only (i.e., 3 elements not in D), and m - 7 elements in both.

The 3 elements not in D: these are the elements d such that d ∉ D but -d ∈ D. The 3 elements in D only: d ∈ D but -d ∉ D.

The pairs {d, -d}: there are (m-1)/2 pairs if m odd, or (m-2)/2 pairs + {m/2} if m even.

- "Both" pairs (both d and -d in D): these contribute 2 to |D ∩ (-D)| each. So (m-7)/2 such pairs if m odd, or (m-7-1)/2 = (m-8)/2 such pairs + possibly m/2 if m even and m/2 ∈ D.

Hmm, this is getting complicated. Let me just check: can we always find such a D for m ≥ 7?

The condition is: D ⊂ Z_m \ {0}, |D| = m - 4, D ∪ (-D) = Z_m \ {0}, |D ∩ (-D)| = m - 7.

Equivalently: the complement of D in Z_m \ {0} has size 3, and D ∪ (-D) = Z_m \ {0} means the complement of D is contained in -D, i.e., if d ∉ D then -d ∈ D.

So the 3 elements not in D, call them a, b, c, must satisfy: -a, -b, -c ∈ D. Also, a, b, c ∉ D means -a, -b, -c ∈ D \ (-D) (they're in D but their negatives aren't)... wait, no. -a ∈ D, and a ∉ D. Is -a ∈ -D? -a ∈ -D iff a ∈ D. But a ∉ D, so -a ∉ -D. So -a ∈ D \ (-D). Similarly for b, c.

So -a, -b, -c are the 3 elements in D \ (-D). And a, b, c are the 3 elements in (-D) \ D = complement of D.

Now, |D ∩ (-D)| = m - 7. The "both" elements: Z_m \ {0, ±a, ±b, ±c} (excluding 0 and the 6 elements ±a, ±b, ±c) has size m - 1 - 6 = m - 7. These are all in D ∩ (-D). But wait, what if some of a, b, c are self-inverse (a = -a, i.e., a = m/2)? Then the set {±a, ±b, ±c} has fewer than 6 elements.

Let me assume m is odd for simplicity (no self-inverse elements). Then {±a, ±b, ±c} has 6 elements (assuming a, b, c are distinct and no two are negatives of each other). The remaining m - 7 elements are in D ∩ (-D). We need to put all of them in D (and their negatives too, which they already are since they're in both).

So the construction is:
1. Choose 3 elements a, b, c (with a, b, c, -a, -b, -c all distinct, i.e., no two of a,b,c are equal or negatives).
2. D = (Z_m \ {0, a, b, c}) — i.e., everything except 0, a, b, c.
3. Check: -a, -b, -c ∈ D (since -a ≠ a, b, c as long as -a ∉ {a, b, c}, which is ensured by the distinctness condition). ✓
4. |D| = m - 1 - 3 = m - 4. ✓
5. D ∪ (-D) = Z_m \ {0} ∪ (something)... let me check. -D = Z_m \ {0, -a, -b, -c}. D ∪ (-D) = Z_m \ ({a,b,c} ∩ {-a,-b,-c})... no. D ∪ (-D) = (Z_m \ {0,a,b,c}) ∪ (Z_m \ {0,-a,-b,-c}) = Z_m \ ({a,b,c} ∩ {-a,-b,-c})... no, that's not right either.

D ∪ (-D) = Z_m \ ({0, a, b, c} ∩ {0, -a, -b, -c}). Wait, De Morgan: complement of (D ∪ (-D)) = complement of D ∩ complement of (-D) = {0, a, b, c} ∩ {0, -a, -b, -c} = {0} ∪ ({a,b,c} ∩ {-a,-b,-c}).

If a, b, c, -a, -b, -c are all distinct (and nonzero), then {a,b,c} ∩ {-a,-b,-c} = ∅. So complement of (D ∪ (-D)) = {0}, meaning D ∪ (-D) = Z_m \ {0}. ✓

6. |D ∩ (-D)| = |D| + |-D| - |D ∪ (-D)| = (m-4) + (m-4) - (m-1) = m - 7. ✓

So for m odd, m ≥ 7, we can always find such a D (just pick any 3 elements a, b, c with all of ±a, ±b, ±c distinct and nonzero, which is possible when m ≥ 7 since there are (m-1)/2 ≥ 3 pairs).

For m even, we need to be more careful about the self-inverse element m/2. Let me handle that case.

If m is even, m/2 is self-inverse. We need to decide whether m/2 ∈ D or not.

Case m/2 ∈ D: Then m/2 ∈ D ∩ (-D) (since -m/2 = m/2). So m/2 is a "both" element. We need to choose a, b, c (not in D) from the remaining m - 2 non-self-inverse elements (i.e., (m-2)/2 pairs). We need 3 elements a, b, c with ±a, ±b, ±c all distinct and none equal to m/2. This requires (m-2)/2 ≥ 3, i.e., m ≥ 8.

Case m/2 ∉ D: Then m/2 is one of a, b, c (say a = m/2). Then -a = m/2 = a, so -a ∈ D requires a ∈ D, contradiction. So this doesn't work.

So for m even, m ≥ 8, we include m/2 in D and choose 3 other elements. Then |D| = m - 4 (including m/2 and all but 3 of the other elements). Let me verify: D = (Z_m \ {0}) \ {a, b, c} where a, b, c are 3 non-self-inverse elements. |D| = (m-1) - 3 = m - 4. ✓

D ∪ (-D): complement = {0, a, b, c} ∩ {0, -a, -b, -c}. Since a, b, c are non-self-inverse and ±a, ±b, ±c distinct: complement = {0}. So D ∪ (-D) = Z_m \ {0}. ✓

|D ∩ (-D)|: m/2 ∈ D ∩ (-D). The other elements in D ∩ (-D) are the non-self-inverse elements in both D and -D, which is all non-self-inverse elements except ±a, ±b, ±c. Count: (m - 2) - 6 = m - 8. Plus m/2: total m - 8 + 1 = m - 7. ✓

So for m even, m ≥ 8, the construction also works.

Summary for n = 7m with the within-group vertex-transitive construction (d = 4, r = 2):
- m odd, m ≥ 7: works. n = 49, 63, 77, 91 (m = 7, 9, 11, 13).
- m even, m ≥ 8: works. n = 56, 70, 84, 98 (m = 8, 10, 12, 14).

So this covers n = 49, 56, 63, 70, 77, 84, 91, 98. That's m = 7, 8, 9, 10, 11, 12, 13, 14.

What about m = 2, 3, 4, 5, 6 (n = 14, 21, 28, 35, 42)?

For these small m, the d = 4 construction doesn't work (need m ≥ 7 for odd, m ≥ 8 for even). Let me try other values of d.

d ≡ 4 (mod 12), so d ∈ {4, 16, 28, ...}. For small m, d = 4 requires m ≥ 7. The next value d = 16 requires m ≥ 31. So for m < 7, we can't use the vertex-transitive within-group approach with this d.

But we can use non-vertex-transitive within-group structures, or a completely different construction.

Let me think about alternative constructions for n = 14, 21, 28, 35, 42.

**For n = 14 (m = 2):** 7 groups of 2. Within each group of 2, there's only 1 pair. Options: single edge (tournament, w = 1 or 0) or mutual (w = 1, μ = 1).

Between groups: cyclic tournament, 3 out-groups of 2 each, so 6 out-edges to other groups.

If within-group is mutual (w = 1, μ = 1): total out = 1 + 6 = 7. Need 4 | 7? No, 7 is not divisible by 4. ✗

If within-group is single (w = 1, μ = 0 for one vertex, w = 0, μ = 0 for the other): 
- Vertex with w = 1: total out = 1 + 6 = 7. Not divisible by 4. ✗
- Vertex with w = 0: total out = 0 + 6 = 6. Not divisible by 4. ✗

So the 7-group construction with pure cyclic tournament between groups doesn't work for m = 2. We need mutual edges between groups.

Let me try a different approach for n = 14. Let me use the within-group approach but with mutual edges between groups.

General setup: 7 groups of m. Between groups G_i and G_{i+d} (d ∈ {1,2,3}), edges go from G_i to G_{i+d}. Each vertex in G_i has r mutual out-edges to G_{i+d} and (m - r) single out-edges. (Same r for all d by symmetry.)

Within group: each vertex has out-degree w and mutual μ. (Can vary by vertex.)

Total out = w + 3m. Total mutual = μ + 3r. Need (μ + 3r) / (w + 3m) = 1/4, i.e., 4μ + 12r = w + 3m.

Also need w + 3m ≡ 0 (mod 4), i.e., w ≡ m (mod 4) (since 3m ≡ -m ≡ ... well, w + 3m ≡ 0 (mod 4) means w ≡ -3m ≡ m (mod 4) since -3 ≡ 1 (mod 4)).

For n = 14 (m = 2): w ≡ 2 (mod 4). Since 0 ≤ w ≤ 1 (within group of 2), w ∈ {0, 1}. Neither is ≡ 2 (mod 4). So w + 3m = w + 6, and we need 4 | (w + 6). w = 0: 6, not div by 4. w = 1: 7, not div by 4. w = 2: impossible (max 1).

So the 7-group construction fundamentally doesn't work for m = 2, regardless of r. The issue is that w + 6 must be divisible by 4, but w ∈ {0, 1} gives 6 or 7, neither divisible by 4.

Hmm. So we need a different construction for n = 14. Let me think about this differently.

Maybe the 7-group structure is too restrictive. Let me think about n = 14 directly.

For n = 14: M = 14·13/14 = 13. S = 78 - 13 = 65. Sum d_out = 65 + 26 = 91... wait let me recompute. Sum d_out = S + 2M = 65 + 26 = 91. Hmm, but also sum d_out = 4n(n-1)/7 = 4·14·13/7 = 4·2·13 = 104. Let me recheck.

n(n-1)/14 = 14·13/14 = 13 = M. S = 6M = 78. Total pairs = M + S = 91 = C(14,2) = 91. ✓
Sum d_out = S + 2M = 78 + 26 = 104. ✓ (matches 4·14·13/7 = 104)
Average d_out = 104/14 = 52/7 ≈ 7.43.

Each d_out ≡ 0 (mod 4). Possible d_out values: 0, 4, 8, 12. (Can't be > 13.)

Sum = 104 with 14 vertices, each d_out ∈ {0, 4, 8, 12}:
If x₀ have d_out=0, x₁ have 4, x₂ have 8, x₃ have 12:
x₀ + x₁ + x₂ + x₃ = 14
4x₁ + 8x₂ + 12x₃ = 104, i.e., x₁ + 2x₂ + 3x₃ = 26.

From these: x₀ = 14 - x₁ - x₂ - x₃ and x₁ = 26 - 2x₂ - 3x₃.
x₀ = 14 - (26 - 2x₂ - 3x₃) - x₂ - x₃ = 14 - 26 + 2x₂ + 3x₃ - x₂ - x₃ = -12 + x₂ + 2x₃.
Need x₀ ≥ 0: x₂ + 2x₃ ≥ 12.
Need x₁ ≥ 0: 26 - 2x₂ - 3x₃ ≥ 0, i.e., 2x₂ + 3x₃ ≤ 26.

Many solutions. For example, x₃ = 4, x₂ = 4: x₁ = 26 - 8 - 12 = 6, x₀ = -12 + 4 + 8 = 0. So 0 vertices with d_out=0, 6 with d_out=4, 4 with d_out=8, 4 with d_out=12. Sum = 0 + 24 + 32 + 48 = 104. ✓

Or x₃ = 6, x₂ = 4: x₁ = 26 - 8 - 18 = 0, x₀ = -12 + 4 + 12 = 4. So 4 with d_out=0, 0 with 4, 4 with 8, 6 with 12. Sum = 0 + 0 + 32 + 72 = 104. ✓

The question is whether we can realize any of these with an actual graph. This is a graph realization problem.

Let me think about it differently. Instead of trying to construct explicitly, let me think about whether there's a general existence theorem.

Actually, let me reconsider the problem. Maybe I should think about it as follows:

We have a "semi-complete" digraph (for each pair, at least one direction). The condition is that for each vertex v, if d(v) is the out-degree and m(v) is the number of mutual neighbors, then m(v) = d(v)/4.

Equivalently, d(v) = 4m(v), so d(v) is always a multiple of 4.

Let me think of the graph as follows. For each unordered pair {u, v}, we have either:
- A single edge (one direction), or
- A mutual edge (both directions).

Let's say the mutual edges form a graph G_m (undirected), and the single edges form a tournament T on the remaining pairs.

For each vertex v:
- d(v) = (out-degree in T) + (degree in G_m)
- m(v) = degree in G_m
- Condition: degree in G_m = d(v)/4 = (out-degree in T + degree in G_m) / 4
- So 4 · deg_{G_m}(v) = out-degree_T(v) + deg_{G_m}(v)
- 3 · deg_{G_m}(v) = out-degree_T(v)

So for each vertex v: out-degree in the tournament T = 3 × degree in the mutual graph G_m.

This is a nice reformulation! Let me verify:
- d(v) = out_T(v) + deg_M(v) where out_T is out-degree in tournament, deg_M is degree in mutual graph.
- m(v) = deg_M(v).
- Condition: deg_M(v) = d(v)/4 = (out_T(v) + deg_M(v))/4.
- 4 deg_M = out_T + deg_M → 3 deg_M = out_T. ✓

So the condition is: **for each vertex v, the out-degree of v in the tournament T equals 3 times the degree of v in the mutual graph G_m.**

The tournament T is on the pairs not in G_m. The total number of pairs is C(n,2). The mutual graph G_m has M edges. The tournament T is on C(n,2) - M pairs.

For each vertex v:
- deg_M(v) = degree in G_m
- out_T(v) = 3 · deg_M(v)
- In the tournament T, v plays against n - 1 - deg_M(v) opponents (those not connected to v by a mutual edge). So out_T(v) + in_T(v) = n - 1 - deg_M(v).
- out_T(v) = 3 deg_M(v), so in_T(v) = n - 1 - deg_M(v) - 3 deg_M(v) = n - 1 - 4 deg_M(v).
- Need in_T(v) ≥ 0: deg_M(v) ≤ (n-1)/4.
- Need out_T(v) ≤ n - 1 - deg_M(v): 3 deg_M(v) ≤ n - 1 - deg_M(v), i.e., 4 deg_M(v) ≤ n - 1. Same condition.

Also, sum of out_T over all vertices = number of tournament edges = C(n,2) - M.
Sum of 3 deg_M = 3 · 2M = 6M (since sum of degrees in G_m = 2M).
So C(n,2) - M = 6M, giving C(n,2) = 7M, i.e., M = n(n-1)/14. Same as before.

Now the question becomes: **for which n does there exist an undirected graph G_m on n vertices with M = n(n-1)/14 edges, such that the complement of G_m (on the same vertex set, with C(n,2) - M edges) admits a tournament where each vertex v has out-degree exactly 3 deg_{G_m}(v)?**

The tournament on the complement of G_m: each vertex v has n - 1 - deg_M(v) opponents, and needs out-degree 3 deg_M(v). This requires 3 deg_M(v) ≤ n - 1 - deg_M(v), i.e., deg_M(v) ≤ (n-1)/4.

Also, a tournament on a graph H (where H is the complement of G_m) with specified out-degrees exists iff the out-degree sequence is "tournament-realizable" on H. By a generalization of Landau's theorem, a tournament on a graph H with prescribed out-degrees d(v) exists iff:
- For every subset S of vertices, sum_{v in S} d(v) ≥ C(|S|, 2) - e_H(S) (where e_H(S) is the number of edges of H within S)... actually, this is more subtle.

Actually, the existence of a tournament on a given graph H (orienting each edge of H) with prescribed out-degrees is equivalent to an orientation problem. By the Gale-Ryser / Fulkerson theorem for orientations:

An undirected graph H has an orientation with prescribed out-degrees d(v) iff:
1. sum d(v) = |E(H)|
2. For every subset S ⊆ V, sum_{v ∈ S} d(v) ≥ |E(H[S])| - ... hmm, I need to recall the exact condition.

Actually, the condition for an orientation of graph H with prescribed out-degrees is:
- sum d(v) = |E(H)|
- For every S ⊆ V: sum_{v ∈ S} d(v) ≥ |E(H[S])| (where H[S] is the subgraph induced by S)... no, that's not right either.

The correct condition (by the theorem of Hakimi or Frank): An undirected graph G = (V, E) has an orientation with out-degree d(v) for each v iff:
- sum d(v) = |E|
- For every S ⊆ V: sum_{v ∈ S} d(v) ≥ |E(G[S])| (edges within S must have at least one endpoint in S with positive out-degree... actually no).

Let me think again. In an orientation of G, for a subset S, the edges within S contribute to out-degrees of vertices in S (each edge within S contributes 1 to the out-degree of one vertex in S). Edges from S to V\S contribute to out-degrees of vertices in S (if oriented from S to V\S). So:

sum_{v ∈ S} d(v) = (edges within S oriented from a vertex in S) + (edges from S to V\S oriented from S to V\S)
≥ (edges within S oriented from a vertex in S) ≥ 0

But also:
sum_{v ∈ S} d(v) = |E(G[S])| - (edges within S oriented into S from S, i.e., in-degree within S) + (edges from S to V\S oriented out)

Hmm, this is getting complicated. Let me use the correct theorem.

**Theorem (Hakimi, 1965 / Frank):** An undirected graph G = (V, E) has an orientation with prescribed out-degree function d: V → Z≥0 iff:
1. ∑_v d(v) = |E|
2. For every S ⊆ V: ∑_{v ∈ S} d(v) ≥ |E(G[S])|

Wait, I think the condition is actually:
2. For every S ⊆ V: ∑_{v ∈ S} d(v) ≥ |E(G[S])| - ... no.

Let me think about it from first principles. In an orientation of G, for subset S:
- Each edge within G[S] contributes exactly 1 to ∑_{v ∈ S} out(v) (one endpoint has it as an out-edge).
- Each edge between S and V\S contributes 0 or 1 to ∑_{v ∈ S} out(v) (1 if oriented from S to V\S, 0 otherwise).

So ∑_{v ∈ S} out(v) = |E(G[S])| - (edges within S oriented from V\S... no, edges within S are between vertices in S, so they always contribute 1 to the sum) + (edges from S to V\S oriented from S to V\S).

Wait: ∑_{v ∈ S} out(v) = (number of edges within G[S] oriented out of some v ∈ S, which is all of them since both endpoints are in S, so each contributes 1 to exactly one vertex's out-degree) + (edges from S to V\S oriented from S to V\S).

So ∑_{v ∈ S} out(v) = |E(G[S])| + (edges from S to V\S oriented from S).

Thus ∑_{v ∈ S} out(v) ≥ |E(G[S])|, with equality iff all edges between S and V\S are oriented from V\S to S.

Also, ∑_{v ∈ S} out(v) ≤ |E(G[S])| + |δ(S)| where δ(S) is the set of edges between S and V\S.

So the necessary and sufficient conditions for an orientation with prescribed out-degrees d(v) are:
1. ∑ d(v) = |E|
2. For every S ⊆ V: |E(G[S])| ≤ ∑_{v ∈ S} d(v) ≤ |E(G[S])| + |δ(S)|

The upper bound is equivalent to: ∑_{v ∈ S} d(v) ≤ |E(G[S])| + |δ(S)| = |E(G)| - |E(G[V\S])|, i.e., ∑_{v ∉ S} d(v) ≥ |E(G[V\S])|, which is the same as condition 2 applied to V\S.

So the conditions reduce to:
1. ∑ d(v) = |E|
2. For every S ⊆ V: ∑_{v ∈ S} d(v) ≥ |E(G[S])|

This is the correct condition (it's both necessary and sufficient).

Now, in our problem:
- G = complement of G_m (the mutual graph), i.e., G has C(n,2) - M edges.
- d(v) = 3 deg_{G_m}(v) for each v.
- Need: ∑ d(v) = |E(G)| = C(n,2) - M. Check: ∑ 3 deg_{G_m}(v) = 3 · 2M = 6M = C(n,2) - M (since C(n,2) = 7M). ✓
- Need: for every S ⊆ V, ∑_{v ∈ S} 3 deg_{G_m}(v) ≥ |E(G[S])|.

Now, |E(G[S])| = C(|S|, 2) - |E(G_m[S])| (edges within S in the complement of G_m = all pairs in S minus mutual edges in S).

And ∑_{v ∈ S} 3 deg_{G_m}(v) = 3 · (2|E(G_m[S])| + |δ_{G_m}(S)|) where δ_{G_m}(S) is the number of G_m-edges between S and V\S. (Because sum of degrees in G_m over S = 2|E(G_m[S])| + |δ_{G_m}(S)|.)

So the condition becomes:
3(2|E(G_m[S])| + |δ_{G_m}(S)|) ≥ C(|S|, 2) - |E(G_m[S])|
6|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) - |E(G_m[S])|
7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2)

So we need: **for every S ⊆ V, 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2).**

Note that 7|E(G_m[S])| + 3|δ_{G_m}(S)| = 7|E(G_m[S])| + 3(∑_{v ∈ S} deg_{G_m}(v) - 2|E(G_m[S])|) = 7|E(G_m[S])| + 3∑_{v ∈ S} deg_{G_m}(v) - 6|E(G_m[S])| = |E(G_m[S])| + 3∑_{v ∈ S} deg_{G_m}(v).

Hmm, that doesn't simplify as nicely. Let me just work with: 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2).

The total "weight" is 7|E(G_m)| = 7M = C(n,2) = C(|V|, 2). So for S = V, we get 7M + 0 = C(n,2) = C(|V|,2). ✓ (equality).

For general S, we need 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2).

Note that |E(G_m[S])| + |δ_{G_m}(S)| + |E(G_m[V\S])| = M, and C(|S|,2) + C(n-|S|,2) + |S|(n-|S|) = C(n,2) = 7M.

The condition for S is: 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2).
The condition for V\S is: 7|E(G_m[V\S])| + 3|δ_{G_m}(S)| ≥ C(n-|S|, 2).

Adding: 7(|E(G_m[S])| + |E(G_m[V\S])|) + 6|δ_{G_m}(S)| ≥ C(|S|, 2) + C(n-|S|, 2).
7(M - |δ_{G_m}(S)|) + 6|δ_{G_m}(S)| ≥ C(n,2) - |S|(n-|S|).
7M - 7|δ| + 6|δ| ≥ 7M - |S|(n-|S|).
-|δ| ≥ -|S|(n-|S|).
|δ| ≤ |S|(n-|S|). Always true since δ is a subset of all S × (V\S) pairs.

So the conditions for S and V\S are not redundant; they're both needed.

Now the question is: for which n does there exist a graph G_m on n vertices with M = n(n-1)/14 edges such that for every S ⊆ V, 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2)?

This is a question about the existence of a graph with certain "expansion" properties. The condition says that for every subset S, the mutual edges within S and crossing S must be "dense enough" relative to all pairs within S.

Let me think about what G_m should look like. The condition is easiest to satisfy when G_m is "well-distributed." A random graph or a regular graph with good expansion would work.

Let me consider G_m being a regular graph. If G_m is d-regular, then M = nd/2, so nd/2 = n(n-1)/14, giving d = (n-1)/7. So we need (n-1)/7 to be a non-negative integer, i.e., n ≡ 1 (mod 7). This matches our earlier finding for the vertex-transitive case.

For n ≡ 1 (mod 7), d = (n-1)/7. The condition 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) for a d-regular graph... For a d-regular graph, |δ_{G_m}(S)| = d|S| - 2|E(G_m[S])|. So:

7|E(G_m[S])| + 3(d|S| - 2|E(G_m[S])|) ≥ C(|S|, 2)
7e + 3d|S| - 6e ≥ C(|S|, 2)
e + 3d|S| ≥ C(|S|, 2)
|E(G_m[S])| ≥ C(|S|, 2) - 3d|S| = |S|(|S|-1)/2 - 3d|S| = |S|(|S| - 1 - 6d)/2

With d = (n-1)/7: |E(G_m[S])| ≥ |S|(|S| - 1 - 6(n-1)/7)/2 = |S|(7|S| - 7 - 6n + 6)/14 = |S|(7|S| - 6n - 1)/14.

For |S| ≤ 6n/7 (roughly), the RHS is negative, so the condition is automatically satisfied. For |S| close to n, we need |E(G_m[S])| to be large enough.

For |S| = n (the whole set): |E(G_m[V])| = M = n(n-1)/14, and the RHS is n(7n - 6n - 1)/14 = n(n-1)/14 = M. So equality. ✓

For |S| = n - 1: |E(G_m[S])| ≥ (n-1)(7(n-1) - 6n - 1)/14 = (n-1)(7n - 7 - 6n - 1)/14 = (n-1)(n - 8)/14.

|E(G_m[S])| = M - deg_{G_m}(v) where v is the excluded vertex. If G_m is d-regular, deg(v) = d = (n-1)/7. So |E(G_m[S])| = n(n-1)/14 - (n-1)/7 = (n-1)(n/14 - 1/7) = (n-1)(n - 2)/14.

Need: (n-1)(n-2)/14 ≥ (n-1)(n-8)/14, i.e., n - 2 ≥ n - 8, i.e., 6 ≥ 0. ✓

So for a d-regular G_m with good expansion, the conditions are likely satisfied. But we need to verify this for all subsets, not just large ones.

Actually, for a d-regular graph, the condition |E(G_m[S])| ≥ |S|(7|S| - 6n - 1)/14 is automatically satisfied when 7|S| ≤ 6n + 1, i.e., |S| ≤ (6n+1)/7. For |S| > (6n+1)/7, we need the graph to have enough edges within S.

For a d-regular graph with d = (n-1)/7, the number of edges within S is at least (d|S| - |S|(n-|S|))/2 (by the expander mixing lemma or just by counting: |δ(S)| ≤ |S|(n - |S|), so |E(G_m[S])| = (d|S| - |δ(S)|)/2 ≥ (d|S| - |S|(n-|S|))/2 = |S|(d - n + |S|)/2).

Need: |S|(d - n + |S|)/2 ≥ |S|(7|S| - 6n - 1)/14.
(d - n + |S|)/2 ≥ (7|S| - 6n - 1)/14.
7(d - n + |S|) ≥ 7|S| - 6n - 1.
7d - 7n + 7|S| ≥ 7|S| - 6n - 1.
7d ≥ n - 1.
7 · (n-1)/7 ≥ n - 1.
n - 1 ≥ n - 1. ✓ (equality)

So for ANY d-regular graph G_m with d = (n-1)/7, the condition is satisfied! (The bound from |δ(S)| ≤ |S|(n-|S|) is tight enough.)

Wait, but I used the bound |δ(S)| ≤ |S|(n - |S|), which is the trivial bound (δ(S) is at most all pairs between S and V\S). This gives a lower bound on |E(G_m[S])| that's exactly tight. So the condition is satisfied for any d-regular graph.

But wait, does a d-regular graph on n vertices with d = (n-1)/7 always exist? We need n ≡ 1 (mod 7) (so d is an integer) and d ≤ n - 1 (always true for n ≥ 8) and nd even (n·(n-1)/7 even). Since n ≡ 1 (mod 7), n = 7k + 1, d = k. nd = (7k+1)k. This is even iff k(7k+1) is even, which is true when k is even or 7k+1 is even (i.e., k is odd). So always even. ✓

A d-regular graph on n vertices exists iff 0 ≤ d ≤ n-1 and nd is even. Both conditions are satisfied. ✓

So for n ≡ 1 (mod 7), we can always construct a valid configuration: take any d-regular graph G_m with d = (n-1)/7, and orient the complement with the prescribed out-degrees (which is possible by the Hakimi condition, as we verified).

Wait, but I need to double-check the Hakimi condition more carefully. I showed that the condition 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) is satisfied using the bound |δ_{G_m}(S)| ≤ |S|(n-|S|). But this is the trivial bound, and the calculation showed equality, meaning the condition is just barely satisfied. Let me re-examine.

For a d-regular G_m with d = (n-1)/7:
|E(G_m[S])| = (d|S| - |δ_{G_m}(S)|) / 2

The condition is:
7 · (d|S| - |δ|) / 2 + 3|δ| ≥ C(|S|, 2)
(7d|S| - 7|δ| + 6|δ|) / 2 ≥ |S|(|S|-1)/2
7d|S| - |δ| ≥ |S|(|S|-1)
|δ| ≤ 7d|S| - |S|(|S|-1) = |S|(7d - |S| + 1) = |S|((n-1) - |S| + 1) = |S|(n - |S|)

And |δ_{G_m}(S)| ≤ |S|(n - |S|) is always true (trivially, since δ is a subset of all S × V\S pairs). So the condition is always satisfied. ✓

Great, so for n ≡ 1 (mod 7), any d-regular G_m with d = (n-1)/7 works, and such a graph always exists. So all n ≡ 1 (mod 7) are achievable.

Now for n ≡ 0 (mod 7), n = 7m. We need M = 7m(7m-1)/14 = m(7m-1)/2. For M to be an integer, m(7m-1) must be even. If m is even, yes. If m is odd, 7m-1 is even, so yes. Always integer. ✓

We need a graph G_m on n = 7m vertices with M = m(7m-1)/2 edges, such that for every S, 7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2), and the prescribed out-degrees d(v) = 3 deg_{G_m}(v) are achievable (which is the same condition).

G_m doesn't have to be regular. The average degree is 2M/n = 2 · m(7m-1)/2 / (7m) = (7m-1)/7 = m - 1/7. Not an integer, so G_m can't be regular.

Let me think about what G_m should look like for n = 7m. We need the degrees to satisfy: for each v, out_T(v) = 3 deg_{G_m}(v), and out_T(v) + in_T(v) = n - 1 - deg_{G_m}(v), so in_T(v) = n - 1 - 4 deg_{G_m}(v) ≥ 0, i.e., deg_{G_m}(v) ≤ (n-1)/4 = (7m-1)/4.

Also, the tournament is on the complement of G_m, so we need the Hakimi condition.

Let me try a specific construction for G_m. Consider a graph where 6m vertices have degree m and m vertices have degree m - 1. (This matches the out-degree distribution we found earlier: d_out = 4m for 6m vertices and d_out = 4(m-1) for m vertices, since d_out = 4 deg_{G_m} and deg_{G_m} = m or m-1.)

Check: sum of degrees = 6m · m + m · (m-1) = 6m² + m² - m = 7m² - m = m(7m - 1) = 2M. ✓

Check deg ≤ (n-1)/4 = (7m-1)/4: m ≤ (7m-1)/4 iff 4m ≤ 7m - 1 iff 1 ≤ 3m, true for m ≥ 1. And m - 1 ≤ (7m-1)/4 iff 4(m-1) ≤ 7m - 1 iff 4m - 4 ≤ 7m - 1 iff -3 ≤ 3m, true. ✓

Now, does such a graph exist (with 6m vertices of degree m and m vertices of degree m-1) and satisfy the Hakimi condition?

A graph with this degree sequence exists iff the Erdős–Gallai conditions are satisfied. For a degree sequence d_1 ≥ d_2 ≥ ... ≥ d_n, the condition is: for each k, ∑_{i=1}^k d_i ≤ k(k-1) + ∑_{i=k+1}^n min(d_i, k).

Our sequence: m vertices with degree m-1, 6m vertices with degree m. Sorted: m, m, ..., m (6m times), m-1, m-1, ..., m-1 (m times).

For k ≤ 6m: ∑_{i=1}^k d_i = km. RHS = k(k-1) + ∑_{i=k+1}^{7m} min(d_i, k).
- If k ≤ m-1: all remaining have degree ≥ m-1 ≥ k, so min = k. RHS = k(k-1) + (7m - k)k = k(k - 1 + 7m - k) = k(7m - 1). Need km ≤ k(7m - 1), i.e., m ≤ 7m - 1, true. ✓
- If m-1 < k ≤ 6m: the remaining 6m - k vertices have degree m, and m vertices have degree m-1. min(d_i, k) = min(m, k) for the degree-m vertices and min(m-1, k) = m-1 for the degree-(m-1) vertices (since k > m-1).
  - If k < m: min(m, k) = k. RHS = k(k-1) + (6m - k)k + m(m-1) = k(k - 1 + 6m - k) + m(m-1) = k(6m - 1) + m(m-1). Need km ≤ k(6m - 1) + m(m-1), i.e., 0 ≤ k(5m - 1) + m(m-1), true. ✓
  - If k ≥ m: min(m, k) = m. RHS = k(k-1) + (6m - k)m + m(m-1) = k(k-1) + 6m² - km + m² - m = k(k-1) + 7m² - km - m. Need km ≤ k(k-1) + 7m² - km - m, i.e., 2km ≤ k(k-1) + 7m² - m, i.e., 0 ≤ k² - k - 2km + 7m² - m = k² - (2m+1)k + 7m² - m.
  
  This is a quadratic in k: f(k) = k² - (2m+1)k + 7m² - m. Discriminant: (2m+1)² - 4(7m² - m) = 4m² + 4m + 1 - 28m² + 4m = -24m² + 8m + 1. For m ≥ 1, this is -24 + 8 + 1 = -15 < 0. So f(k) > 0 for all k (since the leading coefficient is positive and discriminant is negative). ✓

For k > 6m (i.e., 6m < k ≤ 7m): ∑_{i=1}^k d_i = 6m · m + (k - 6m)(m-1) = 6m² + (k-6m)(m-1). RHS = k(k-1) + ∑_{i=k+1}^{7m} min(d_i, k). The remaining 7m - k vertices all have degree m - 1. min(m-1, k) = m - 1 (since k > 6m ≥ m - 1 for m ≥ 1). RHS = k(k-1) + (7m - k)(m-1).

Need: 6m² + (k-6m)(m-1) ≤ k(k-1) + (7m-k)(m-1).
6m² + (k-6m)(m-1) ≤ k(k-1) + (7m-k)(m-1)
6m² + (k-6m)(m-1) - (7m-k)(m-1) ≤ k(k-1)
6m² + (m-1)(k - 6m - 7m + k) ≤ k(k-1)
6m² + (m-1)(2k - 13m) ≤ k(k-1)
6m² + 2k(m-1) - 13m(m-1) ≤ k² - k
6m² + 2km - 2k - 13m² + 13m ≤ k² - k
-7m² + 13m + 2km - 2k ≤ k² - k
-7m² + 13m + 2km - k ≤ k²
k² - 2km + k + 7m² - 13m ≥ 0
k² - (2m-1)k + 7m² - 13m ≥ 0

Discriminant: (2m-1)² - 4(7m² - 13m) = 4m² - 4m + 1 - 28m² + 52m = -24m² + 48m + 1.
For m = 1: -24 + 48 + 1 = 25 > 0. Roots: k = (1 ± 5)/2, so k = 3 or k = -2. For k ∈ (6m, 7m] = (6, 7], i.e., k = 7: f(7) = 49 - 13·1 + 7 - 13 = 49 - 13 + 7 - 13 = 30 > 0. ✓ (Actually let me recompute: f(7) = 49 - (2-1)·7 + 7 - 13 = 49 - 7 + 7 - 13 = 36 > 0. ✓)

For m = 2: discriminant = -96 + 96 + 1 = 1 > 0. Roots: k = (3 ± 1)/2, so k = 2 or k = 1. For k ∈ (12, 14], i.e., k = 13 or 14: f(13) = 169 - 3·13 + 28 - 26 = 169 - 39 + 28 - 26 = 132 > 0. ✓

For m ≥ 3: discriminant = -24m² + 48m + 1. At m = 3: -216 + 144 + 1 = -71 < 0. So for m ≥ 3, discriminant < 0, and f(k) > 0 for all k. ✓

For m = 1 and m = 2, we verified f(k) > 0 for the relevant k values. ✓

So the Erdős–Gallai conditions are satisfied, and a graph with this degree sequence exists for all m ≥ 1.

Now, does this graph satisfy the Hakimi condition (7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) for all S)?

This is not automatic just from the degree sequence. We need to choose the right graph. Let me think about what graph to use.

Actually, let me think about this more carefully. The Hakimi condition is:
7|E(G_m[S])| + 3|δ_{G_m}(S)| ≥ C(|S|, 2) for all S ⊆ V.

Equivalently (using |δ_{G_m}(S)| = ∑_{v ∈ S} deg(v) - 2|E(G_m[S])|):
7|E(G_m[S])| + 3(∑_{v ∈ S} deg(v) - 2|E(G_m[S])|) ≥ C(|S|, 2)
7e + 3D - 6e ≥ C(|S|, 2)
e + 3D ≥ C(|S|, 2)
|E(G_m[S])| + 3∑_{v ∈ S} deg(v) ≥ C(|S|, 2)

where D = ∑_{v ∈ S} deg(v).

So the condition is: |E(G_m[S])| + 3∑_{v ∈ S} deg(v) ≥ C(|S|, 2) = |S|(|S|-1)/2.

Since |E(G_m[S])| ≥ 0, a sufficient condition is 3∑_{v ∈ S} deg(v) ≥ |S|(|S|-1)/2, i.e., the average degree in S is at least (|S|-1
