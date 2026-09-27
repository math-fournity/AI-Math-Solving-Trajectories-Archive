# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let $n$ be a positive integer with $n \ge 5$. Define $m(n)$ to be the minimum number of edges such that any $n$-vertex simple graph with $m(n)$ edges contains two triangles that share exactly one vertex. Calculate the sum of $m(n)$ for $n = 5, 6, 7, 8, 9, 10$.       — 题目文本
#   The original solution derives that for a given $n \ge 5$, the minimum number of edges required to guarantee two triangles sharing exactly one vertex is $m(n) = \lfloor \frac{n^2}{4} \rfloor + 2$.
We calculate $m(n)$ for $n \in \{5, 6, 7, 8, 9, 10\}$:
- $m(5) = \lfloor 25/4 \rfloor + 2 = 6 + 2 = 8$
- $m(6) = \lfloor 36/4 \rfloor + 2 = 9 + 2 = 11$
- $m(7) = \lfloor 49/4 \rfloor + 2 = 12 + 2 = 14$
- $m(8) = \lfloor 64/4 \rfloor + 2 = 16 + 2 = 18$
- $m(9) = \lfloor 81/4 \rfloor + 2 = 20 + 2 = 22$
- $m(10) = \lfloor 100/4 \rfloor + 2 = 25 + 2 = 27$
The sum is $8 + 11 + 14 + 18 + 22 + 27 = 100$.  — 标准解答
#   Let me analyze this problem carefully.

We need to find $m(n)$, the minimum number of edges such that any $n$-vertex simple graph with $m(n)$ edges contains two triangles that share exactly one vertex.

Two triangles sharing exactly one vertex means a "bowtie" or "butterfly" graph - two triangles with a common vertex but no common edge.

Let me think about this. First, what's the extremal number for avoiding two triangles sharing exactly one vertex?

Let me think about what graphs avoid this configuration. We need to find the maximum number of edges in an $n$-vertex graph that does NOT contain two triangles sharing exactly one vertex.

Two triangles share exactly one vertex = there exist vertices $a, b, c, d$ (with $a$ being the shared vertex) such that $abc$ and $abd$ are both triangles (sharing edge $ab$... wait no).

Wait, let me reconsider. Two triangles sharing exactly one vertex. Triangle 1 = $\{a, b, c\}$, Triangle 2 = $\{a, d, e\}$ where the only common vertex is $a$. So $b, c, d, e$ are all distinct, and the shared vertex is $a$.

Actually, two triangles can share:
- 0 vertices (disjoint)
- 1 vertex (bowtie/butterfly)
- 1 edge (2 vertices shared) - this is a "diamond" or $K_4$ minus an edge

We want to avoid the case of sharing exactly 1 vertex.

So we need: the maximum number of edges in a graph where no two triangles share exactly one vertex.

Let me think about the structure. If two triangles share exactly one vertex $v$, then $v$ is in both triangles. So we need: for every vertex $v$, the triangles containing $v$ must pairwise share at least an edge (i.e., share at least 2 vertices).

Actually, let's think about it differently. Consider the set of all triangles in the graph. We need that no two triangles share exactly one vertex. So any two triangles either share 0 vertices, or share an edge (2 vertices), or are the same triangle.

If two triangles share an edge, they form a $K_4$ minus an edge (diamond). If three triangles all share a common edge, that's $K_4$.

Let me think about the structure of triangle-sharing. Consider the "triangle graph" where vertices are triangles and edges connect triangles sharing an edge. Actually, let me think about which configurations are allowed.

Let me think about this more carefully. Consider a vertex $v$. The triangles through $v$ correspond to edges in $G[N(v)]$ (the subgraph induced by neighbors of $v$). Two triangles through $v$ share exactly one vertex ($v$) iff the corresponding edges in $G[N(v)]$ are disjoint (share no endpoint). Two triangles through $v$ share an edge iff the corresponding edges in $G[N(v)]$ share an endpoint.

So the condition "no two triangles share exactly one vertex" means: for every vertex $v$, the graph $G[N(v)]$ has the property that every two edges share an endpoint. This means $G[N(v)]$ is a star (all edges share a common vertex) or a triangle (three edges, each pair shares an endpoint).

Wait, a graph where every two edges share an endpoint is either a star or a triangle ($K_3$). This is a well-known fact.

So for every vertex $v$, $G[N(v)]$ is either a star or a triangle.

If $G[N(v)]$ is a star with center $u$, then all triangles through $v$ use the edge $vu$... no wait. The triangles through $v$ correspond to edges in $G[N(v)]$. If $G[N(v)]$ is a star centered at $u \in N(v)$, then all edges in $G[N(v)]$ are of the form $\{u, w\}$ for $w \in N(v)$. So all triangles through $v$ are $\{v, u, w\}$ for various $w$. These all share the edge $\{v, u\}$.

If $G[N(v)]$ is a triangle on $\{a, b, c\}$, then the triangles through $v$ are $\{v, a, b\}, \{v, b, c\}, \{v, a, c\}$. These are the triangles of $K_4$ on $\{v, a, b, c\}$. Any two share an edge.

So the condition is: for every vertex $v$, $G[N(v)]$ is a star or a triangle.

Now I need to find the maximum number of edges in such a graph.

Let me think about what graphs satisfy this. 

Case 1: $G[N(v)]$ is a star for all $v$. This means every vertex's neighborhood forms a star. 

Case 2: Some vertices have triangle neighborhoods.

Let me think about specific constructions.

**Construction 1: Complete bipartite graph $K_{a,b}$.** This has no triangles at all, so the condition is vacuously satisfied. Edges = $ab$. With $a + b = n$, max is $\lfloor n^2/4 \rfloor$.

**Construction 2: A graph where we take $K_{a,b}$ and add edges within one part.** Say we take $K_{a,b}$ and add some edges within part $A$ (size $a$). If we add an edge $\{a_1, a_2\}$ within $A$, then for any $b \in B$, we get a triangle $\{a_1, a_2, b\}$. Now consider vertex $b \in B$. Its neighbors are all of $A$. $G[N(b)] = G[A]$. For the condition to hold, $G[A]$ must be a star or triangle. So the edges within $A$ must form a star or triangle.

If $G[A]$ is a star centered at $a_1$ with $k$ edges, then we have $k$ triangles, all through $a_1$ and some $a_i$, sharing the edge $\{a_1, a_i\}$... wait, the triangles are $\{a_1, a_i, b\}$ for each $b \in B$ and each edge $\{a_1, a_i\}$ in the star.

Now check vertex $a_1$: its neighbors include all of $B$ and $\{a_2, \ldots, a_{k+1}\}$ (the leaves of the star). $G[N(a_1)]$ includes the bipartite edges between $B$ and $\{a_2, \ldots\}$, plus... wait, are there edges between $B$ and the $a_i$'s? Yes, since it's $K_{a,b}$, every $a_i$ is connected to every $b_j$. So $G[N(a_1)]$ is a complete bipartite graph $K_{k, b}$ (between $\{a_2, \ldots, a_{k+1}\}$ and $B$). For this to be a star or triangle, we need $K_{k,b}$ to be a star or triangle. $K_{k,b}$ is a star iff $k=1$ or $b=1$. It's a triangle iff $k=2, b=1$ or $k=1, b=2$ (but $K_{1,2}$ is a star, and $K_{2,1}$ is a star; $K_{2,2}$ is a 4-cycle, not a star or triangle). Actually $K_{1,b}$ is a star for any $b$, and $K_{a,1}$ is a star for any $a$. $K_{2,2}$ is a 4-cycle. So we need $k \leq 1$ or $b \leq 1$.

Hmm, this is getting complicated. Let me think differently.

If $b \geq 2$ and $k \geq 2$, then $G[N(a_1)] = K_{k,b}$ with $k, b \geq 2$ contains a 4-cycle, which has two disjoint edges, violating the condition. So if we add a star with $k \geq 2$ edges within $A$, we need $b \leq 1$, which means $B$ has at most 1 vertex, giving very few edges.

So with $b \geq 2$, we can add at most 1 edge within $A$ (star with 1 edge). Let's check: if we add one edge $\{a_1, a_2\}$ within $A$, then:
- For $b \in B$: $G[N(b)] = G[A]$ which has one edge, which is a star (trivially). ✓
- For $a_1$: $N(a_1) = B \cup \{a_2\}$. $G[N(a_1)]$: edges between $B$ and $a_2$ (all of them, since complete bipartite), and no edges within $B$. So $G[N(a_1)] = K_{1, b}$ (star centered at $a_2$). ✓ (as long as this is a star, which it is for any $b$)
- For $a_2$: similarly, $G[N(a_2)] = K_{1, b}$ (star centered at $a_1$). ✓
- For $a_i$ with $i \geq 3$: $N(a_i) = B$. $G[N(a_i)] = G[B]$ which has no edges. ✓

So this works! We get $ab + 1$ edges with $a + b = n$, $a, b \geq 2$.

Can we do better? Can we add edges within both parts?

If we add an edge within $A$ and an edge within $B$, say $\{a_1, a_2\}$ and $\{b_1, b_2\}$. Then we have triangles $\{a_1, a_2, b_j\}$ for all $b_j \in B$ and $\{a_i, b_1, b_2\}$ for all $a_i \in A$. 

Consider vertex $a_1$: triangles through $a_1$ include $\{a_1, a_2, b_j\}$ for all $j$ and $\{a_1, b_1, b_2\}$. Do $\{a_1, a_2, b_3\}$ and $\{a_1, b_1, b_2\}$ share exactly one vertex ($a_1$)? Yes, if $a_2 \neq b_1, b_2$ and $b_3 \neq b_1, b_2$ (assuming $|B| \geq 3$). So this would violate the condition if $|B| \geq 3$.

If $|B| = 2$, then $B = \{b_1, b_2\}$. Triangles through $a_1$: $\{a_1, a_2, b_1\}$, $\{a_1, a_2, b_2\}$, $\{a_1, b_1, b_2\}$. Do $\{a_1, a_2, b_1\}$ and $\{a_1, b_1, b_2\}$ share vertices $a_1$ and $b_1$ — that's 2 vertices, so they share an edge. ✓. Do $\{a_1, a_2, b_2\}$ and $\{a_1, b_1, b_2\}$ share $a_1$ and $b_2$. ✓. Do $\{a_1, a_2, b_1\}$ and $\{a_1, a_2, b_2\}$ share $a_1$ and $a_2$. ✓. So all pairs share an edge. 

But we need to check all vertices. Consider $b_1$: $N(b_1) = A \cup \{b_2\}$. $G[N(b_1)]$: edges within $A$ (just $\{a_1, a_2\}$) and edges between $A$ and $b_2$ (all of them). So $G[N(b_1)]$ has edges $\{a_1, a_2\}$ and $\{a_i, b_2\}$ for all $a_i \in A$. Is this a star or triangle? The edge $\{a_1, a_2\}$ and edge $\{a_3, b_2\}$ (for $a_3 \neq a_1, a_2$, assuming $|A| \geq 3$) are disjoint. So if $|A| \geq 3$, this fails.

If $|A| = 2$, $A = \{a_1, a_2\}$. Then $G[N(b_1)]$ has edges $\{a_1, a_2\}$, $\{a_1, b_2\}$, $\{a_2, b_2\}$. That's a triangle on $\{a_1, a_2, b_2\}$. ✓

So with $|A| = 2, |B| = 2$, $n = 4$, we get $K_4$ which has 6 edges. But we need $n \geq 5$.

OK so for $n \geq 5$, adding edges within both parts seems hard. Let me think about other constructions.

**Construction 3: Take a clique $K_k$ and make the rest independent, with all edges between them.** Actually, let me think about the "friendship graph" or other structures.

Let me reconsider. The condition is that for every vertex $v$, $G[N(v)]$ is a star or triangle.

Let me think about what happens with a clique $K_k$. For a vertex $v$ in $K_k$, $G[N(v)] = K_{k-1}$. This is a star iff $k-1 \leq 2$ (i.e., $k \leq 3$), and a triangle iff $k-1 = 3$ (i.e., $k = 4$). For $k \geq 5$, $K_{k-1}$ is neither a star nor a triangle. So the largest clique we can have is $K_4$.

$K_4$ has 6 edges and 4 vertices. For $n = 4$, this gives 6 edges with no two triangles sharing exactly one vertex (in $K_4$, any two triangles share an edge).

For $n \geq 5$, we can take $K_4$ plus $n-4$ isolated vertices, giving 6 edges. But we can do better.

**Construction 4: $K_4$ plus vertices connected to some of the $K_4$.** Let's say we have $K_4$ on $\{1,2,3,4\}$ and add vertex $5$ connected to some subset.

If vertex 5 is connected to vertices $\{1, 2\}$ of the $K_4$, then we get a triangle $\{1, 2, 5\}$. Now check:
- Vertex 1: $N(1) = \{2, 3, 4, 5\}$. $G[N(1)]$: edges $\{2,3\}, \{2,4\}, \{3,4\}$ (from $K_4$) and $\{2, 5\}$ (since 5 is connected to 2). Is this a star or triangle? We have edges $\{2,3\}, \{2,4\}, \{3,4\}, \{2,5\}$. The edge $\{3,4\}$ and $\{2,5\}$ are disjoint. So this is NOT a star or triangle. ✗

So connecting vertex 5 to 2 vertices of $K_4$ that are adjacent doesn't work (it always fails since all pairs in $K_4$ are adjacent).

What if vertex 5 is connected to just 1 vertex, say vertex 1? Then no new triangles. Check vertex 1: $N(1) = \{2,3,4,5\}$, $G[N(1)] = K_3$ on $\{2,3,4\}$ plus isolated vertex 5. That's a triangle plus an isolated vertex. Is this a star or triangle? No, it's a triangle plus an isolated vertex, which is neither. ✗

Hmm wait, the condition is that $G[N(v)]$ is a star or triangle. A triangle plus an isolated vertex is not a star (it has 3 edges forming a cycle) and not a triangle (it has 4 vertices). So this fails.

What if vertex 5 is connected to all 4 vertices of $K_4$? Then $N(5) = \{1,2,3,4\}$, $G[N(5)] = K_4$, which is not a star or triangle. ✗

What if vertex 5 is connected to 3 vertices of $K_4$, say $\{1,2,3\}$? Then $N(5) = \{1,2,3\}$, $G[N(5)] = K_3$ (triangle). ✓ for vertex 5. But check vertex 1: $N(1) = \{2,3,4,5\}$. $G[N(1)]$: edges among $\{2,3,4\}$ form $K_3$, plus edges between 5 and $\{2,3\}$ (since 5 is connected to 2 and 3). So edges: $\{2,3\}, \{2,4\}, \{3,4\}, \{2,5\}, \{3,5\}$. Is this a star or triangle? Edge $\{2,4\}$ and $\{3,5\}$ are disjoint. ✗

So it seems hard to add vertices to $K_4$.

Let me reconsider. Maybe the optimal construction is the complete bipartite graph plus one edge, or something else.

**Let me reconsider the bipartite + one edge construction.** Take $K_{a,b}$ with $a + b = n$ and add one edge within the larger part. Total edges: $ab + 1$. To maximize, take $a = \lfloor n/2 \rfloor, b = \lceil n/2 \rceil$, giving $\lfloor n^2/4 \rfloor + 1$.

But wait, can we do better with other constructions?

**Construction 5: Take a star $K_{1,n-1}$.** This has $n-1$ edges and no triangles. But $\lfloor n^2/4 \rfloor + 1$ is much larger for $n \geq 5$.

**Construction 6: Complete bipartite $K_{a,b}$ with $a + b = n$.** Edges = $ab \leq \lfloor n^2/4 \rfloor$. No triangles. This is less than $\lfloor n^2/4 \rfloor + 1$.

So the bipartite + one edge gives $\lfloor n^2/4 \rfloor + 1$.

Can we do better? Let me think about whether we can add more edges.

What about taking $K_{a,b}$ and adding a star with 2 edges within part $A$? We showed this requires $b \leq 1$. If $b = 1$, we have $a = n-1$ and the graph is $K_{n-1, 1}$ plus a star within the $n-1$ part. $K_{n-1,1}$ has $n-1$ edges. Adding 2 edges within the large part gives $n+1$ edges total. For $n \geq 5$, $\lfloor n^2/4 \rfloor + 1 \geq 7 > 6 = n+1$ for $n=5$. So this is worse.

What about adding a triangle within part $A$? If $G[A]$ is a triangle on $\{a_1, a_2, a_3\}$, then for vertex $b \in B$, $G[N(b)] = G[A]$ which is a triangle plus possibly isolated vertices. Wait, $G[A]$ is a triangle on 3 vertices plus isolated vertices for the rest of $A$. Is a triangle plus isolated vertices a "star or triangle"? No, it has more than 3 vertices. So this fails unless $|A| = 3$.

If $|A| = 3$ with $G[A] = K_3$ and $|B| = n - 3$. Check vertex $a_1$: $N(a_1) = \{a_2, a_3\} \cup B$. $G[N(a_1)]$: edge $\{a_2, a_3\}$ (from the triangle) and edges between $\{a_2, a_3\}$ and $B$ (all of them, since complete bipartite). So $G[N(a_1)]$ has edges $\{a_2, a_3\}$ and $\{a_2, b_j\}, \{a_3, b_j\}$ for all $b_j \in B$. Is this a star or triangle? If $|B| \geq 2$, edges $\{a_2, b_1\}$ and $\{a_3, b_2\}$ are disjoint. ✗

So this fails for $|B| \geq 2$, i.e., $n \geq 5$.

If $|B| = 1$, $n = 4$, we get $K_4$ again.

If $|B| = 0$, $n = 3$, just $K_3$.

So for $n \geq 5$, the triangle-within-part construction doesn't work with complete bipartite.

**What about non-complete bipartite constructions?** Let me think more broadly.

Let me consider the structure more carefully. The condition is: for every vertex $v$, $G[N(v)]$ is a star or triangle.

Let me think about graphs where every neighborhood is a star. This is related to the concept of "locally star" graphs.

Actually, let me think about this problem from the perspective of known results. The problem asks for the extremal number for the "butterfly" graph (two triangles sharing a vertex). 

The butterfly graph $B$ is two triangles sharing exactly one vertex. The extremal number $\text{ex}(n, B)$ is the maximum number of edges in an $n$-vertex graph with no butterfly.

For the butterfly graph, I recall that the extremal number is $\lfloor n^2/4 \rfloor + 1$ for $n \geq 5$. Wait, let me think more carefully.

Actually, I think the answer might be related to the following. The Turán-type problem for the butterfly (also called the "bowtie") graph.

Let me think about it from the construction side. We have the construction $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ plus one edge, giving $\lfloor n^2/4 \rfloor + 1$ edges. 

Can we do better? Let me think about other constructions.

**Construction 7: Two cliques sharing a vertex.** Take $K_{k}$ and $K_{l}$ sharing exactly one vertex, with $k + l - 1 = n$. But we showed $K_k$ requires $k \leq 4$. So take $K_4$ and $K_4$ sharing a vertex: $n = 7$, edges = $6 + 6 = 12$. Compare with $\lfloor 49/4 \rfloor + 1 = 12 + 1 = 13$. So 12 < 13, the bipartite+1 construction is better.

Take $K_4$ and $K_3$ sharing a vertex: $n = 6$, edges = $6 + 3 = 9$. Compare with $\lfloor 36/4 \rfloor + 1 = 9 + 1 = 10$. Again worse.

**Construction 8: A graph formed by taking a complete bipartite graph and adding a matching within one part.** We showed adding 1 edge works. Adding 2 edges (a matching) within part $A$: for vertex $b \in B$, $G[N(b)] = G[A]$ which has 2 disjoint edges. This is not a star or triangle. ✗ (unless $|B| = 0$).

So we can't add 2 disjoint edges within a part if $|B| \geq 1$.

What about adding 2 edges that share a vertex (a star of 2 edges) within part $A$? We showed this requires $|B| \leq 1$.

So the bipartite + 1 edge construction seems optimal among bipartite-based constructions.

**Can we beat $\lfloor n^2/4 \rfloor + 1$ with a non-bipartite construction?**

Let me think about the problem differently. Let me consider the structure of triangle-free parts.

Actually, let me think about this more carefully using the characterization.

For every vertex $v$, $G[N(v)]$ is a star or triangle.

Let me split vertices into two types:
- Type S: $G[N(v)]$ is a star
- Type T: $G[N(v)]$ is a triangle

If $v$ is Type T, then $|N(v)| = 3$ and $G[N(v)] = K_3$, so $v$ together with its neighbors forms a $K_4$.

If $v$ is Type S, then $G[N(v)]$ is a star. Let $d(v) = |N(v)|$. If $d(v) \leq 1$, the star is trivial (0 or 1 edge). If $d(v) = 2$, the star has at most 1 edge. If $d(v) \geq 2$, the star has a center $u \in N(v)$ and all edges in $G[N(v)]$ go through $u$.

Let me think about the maximum number of edges. 

Let me consider the case where all vertices are Type S (no vertex has a triangle neighborhood). Then for every $v$, $G[N(v)]$ is a star.

If $G$ is triangle-free, then every $G[N(v)]$ is empty (a star with 0 edges), so the condition is satisfied. The maximum triangle-free graph is $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ with $\lfloor n^2/4 \rfloor$ edges.

If $G$ has some triangles, then some $G[N(v)]$ is a non-trivial star. 

Let me think about the structure when there are triangles. Suppose $v$ is a vertex with $G[N(v)]$ being a star centered at $u$ with $k \geq 1$ edges. Then the triangles through $v$ are $\{v, u, w_i\}$ for $i = 1, \ldots, k$ where $w_1, \ldots, w_k$ are the leaves. All these triangles share the edge $\{v, u\}$.

Now, consider any other triangle in the graph not through $v$. It must not share exactly one vertex with any triangle through $v$.

This is getting complex. Let me try to think about upper bounds.

**Upper bound approach:** Let $G$ be a graph on $n$ vertices with no butterfly (two triangles sharing exactly one vertex). We want to show $e(G) \leq \lfloor n^2/4 \rfloor + 1$ (or find the correct bound).

Let me think about the triangles in $G$. Consider the "triangle edge-sharing" structure. Define an equivalence relation on triangles: two triangles are related if they share an edge. The transitive closure gives equivalence classes. Within each class, any two triangles share an edge (I need to verify this).

Actually, this isn't quite right. If triangle $T_1$ shares an edge with $T_2$, and $T_2$ shares an edge with $T_3$, do $T_1$ and $T_3$ share an edge? Not necessarily. Consider $K_4$: triangles $\{1,2,3\}$, $\{1,2,4\}$, $\{1,3,4\}$. $\{1,2,3\}$ and $\{1,2,4\}$ share edge $\{1,2\}$. $\{1,2,4\}$ and $\{1,3,4\}$ share edge $\{1,4\}$. $\{1,2,3\}$ and $\{1,3,4\}$ share edge $\{1,3\}$. So in $K_4$, all pairs share an edge. 

But in general? Consider a "book" of triangles sharing a common edge $\{u,v\}$: triangles $\{u,v,w_1\}, \{u,v,w_2\}, \ldots$. Any two share the edge $\{u,v\}$. Now add a triangle $\{u, w_1, w_2\}$. This shares edge $\{u, w_1\}$ with $\{u,v,w_1\}$ and edge $\{u, w_2\}$ with $\{u,v,w_2\}$. But does $\{u, w_1, w_2\}$ share an edge with $\{u, v, w_3\}$? They share only vertex $u$. So this would be a butterfly! Unless $w_3$ doesn't exist, i.e., there are only 2 triangles in the book.

So if we have a book with edge $\{u,v\}$ and $k$ triangles $\{u,v,w_i\}$, and we also have triangle $\{u, w_i, w_j\}$ for some $i \neq j$, then we need that there's no $w_l$ with $l \neq i, j$ (otherwise $\{u, w_i, w_j\}$ and $\{u, v, w_l\}$ share only $u$). So the book has at most 2 pages if there's an extra triangle.

This is getting complicated. Let me try a different approach and think about specific small cases, then look for a pattern.

For $n = 5$: We need $m(5)$. The maximum butterfly-free graph on 5 vertices.

$K_{2,3}$ has 6 edges, no triangles. $K_{2,3}$ + 1 edge within the part of size 3: 7 edges. Let me verify this is butterfly-free.

$K_{2,3}$ on parts $A = \{a_1, a_2\}$, $B = \{b_1, b_2, b_3\}$. Add edge $\{b_1, b_2\}$. Triangles: $\{a_1, b_1, b_2\}$ and $\{a_2, b_1, b_2\}$. These share edge $\{b_1, b_2\}$. No other triangles. So no butterfly. ✓ 7 edges.

Can we get 8 edges on 5 vertices without a butterfly? $\binom{5}{2} = 10$, so 8 edges means removing 2 edges from $K_5$.

$K_5$ has 10 triangles. Removing 2 edges... Let me think. $K_5$ minus 2 edges. If the 2 removed edges are disjoint, say $\{1,2\}$ and $\{3,4\}$, the remaining graph has 8 edges. Triangles: all triples except those containing $\{1,2\}$ or $\{3,4\}$. Triangles containing $\{1,2\}$: $\{1,2,3\}, \{1,2,4\}, \{1,2,5\}$ — removed. Triangles containing $\{3,4\}$: $\{1,3,4\}, \{2,3,4\}, \{3,4,5\}$ — removed. Remaining triangles: $\{1,3,5\}, \{1,4,5\}, \{2,3,5\}, \{2,4,5\}$. That's 4 triangles. Do any two share exactly one vertex? $\{1,3,5\}$ and $\{2,4,5\}$ share only vertex 5. Butterfly! ✗

If the 2 removed edges share a vertex, say $\{1,2\}$ and $\{1,3\}$. Remaining triangles: those not containing $\{1,2\}$ or $\{1,3\}$. Triangles of $K_5$: $\{1,2,3\}, \{1,2,4\}, \{1,2,5\}, \{1,3,4\}, \{1,3,5\}, \{1,4,5\}, \{2,3,4\}, \{2,3,5\}, \{2,4,5\}, \{3,4,5\}$. Removed: $\{1,2,3\}, \{1,2,4\}, \{1,2,5\}, \{1,3,4\}, \{1,3,5\}$. Remaining: $\{1,4,5\}, \{2,3,4\}, \{2,3,5\}, \{2,4,5\}, \{3,4,5\}$. Do any two share exactly one vertex? $\{1,4,5\}$ and $\{2,3,4\}$: share vertex 4 only. Wait, $\{1,4,5\}$ has vertices $1,4,5$ and $\{2,3,4\}$ has $2,3,4$. Common: $\{4\}$. Yes, exactly one vertex. Butterfly! ✗

So 8 edges on 5 vertices always contains a butterfly. Thus $m(5) = 8$? Wait, we need to check: does every 5-vertex graph with 8 edges contain a butterfly? We checked two cases of removing 2 edges from $K_5$ and both had butterflies. But are there other 8-edge graphs not of this form? Every 8-edge graph on 5 vertices is $K_5$ minus 2 edges (since $\binom{5}{2} = 10$). The two removed edges either share a vertex or are disjoint. We checked both cases. So yes, every 8-edge graph on 5 vertices has a butterfly.

But wait, we need $m(5)$ = minimum edges such that ANY graph with that many edges contains a butterfly. So $m(5) = 8$ if every 8-edge graph has a butterfly AND there exists a 7-edge graph without a butterfly. We showed $K_{2,3}$ + 1 edge = 7 edges, no butterfly. So $m(5) = 8$.

Hmm wait, but $\lfloor 25/4 \rfloor + 1 = 6 + 1 = 7$. And we showed 7 edges can be butterfly-free, but 8 edges always has a butterfly. So $m(5) = 8 = \lfloor 25/4 \rfloor + 2$?

Wait, let me recheck. $\lfloor 25/4 \rfloor = 6$. So $\lfloor n^2/4 \rfloor + 1 = 7$. But we need 8 edges to force a butterfly. So $m(5) = 8$.

Hmm, that doesn't match $\lfloor n^2/4 \rfloor + 1$. Let me recheck whether there's a 7-edge graph on 5 vertices without a butterfly. We have $K_{2,3} + \{b_1,b_2\}$ with 7 edges and no butterfly. So the maximum butterfly-free graph has at least 7 edges. And we showed 8 edges always has a butterfly. So $\text{ex}(5, B) = 7$ and $m(5) = 8$.

But $\lfloor 25/4 \rfloor + 1 = 7 = \text{ex}(5, B)$. So $m(5) = \text{ex}(5, B) + 1 = 8$.

OK so $m(n) = \text{ex}(n, B) + 1$ where $B$ is the butterfly. And we need to find $\text{ex}(n, B)$ for $n = 5, \ldots, 10$.

For $n = 5$: $\text{ex}(5, B) = 7$, so $m(5) = 8$.

Now let me check $n = 6$. $\lfloor 36/4 \rfloor + 1 = 9 + 1 = 10$. Is $\text{ex}(6, B) = 10$?

Construction: $K_{3,3}$ + 1 edge = 10 edges. Let me verify no butterfly. Parts $A = \{a_1, a_2, a_3\}$, $B = \{b_1, b_2, b_3\}$, add edge $\{a_1, a_2\}$. Triangles: $\{a_1, a_2, b_1\}, \{a_1, a_2, b_2\}, \{a_1, a_2, b_3\}$. All share edge $\{a_1, a_2\}$. No butterfly. ✓

Can we get 11 edges on 6 vertices without a butterfly? $\binom{6}{2} = 15$, so 11 edges means removing 4 edges from $K_6$.

Hmm, this is harder to check directly. Let me think about whether $\text{ex}(6, B) = 10$ or could be higher.

Actually, let me think about another construction for $n = 6$. Take $K_4$ on $\{1,2,3,4\}$ and connect vertices 5, 6 to some vertices.

We showed that adding a vertex connected to 1 vertex of $K_4$ fails (neighborhood of that vertex becomes triangle + isolated vertex). Adding connected to 2 adjacent vertices of $K_4$ fails. Adding connected to 3 vertices of $K_4$ fails. Adding connected to all 4 fails.

What if we don't use $K_4$? Let me think about other structures.

**Construction: $K_{3,3}$ + 1 edge = 10 edges, no butterfly.** Can we do 11?

Let me try $K_{3,3}$ + 2 edges within one part. Say add $\{a_1, a_2\}$ and $\{a_1, a_3\}$ within $A$. Then for $b \in B$, $G[N(b)] = G[A]$ which has edges $\{a_1, a_2\}, \{a_1, a_3\}$ — a star. ✓ for $b$. For $a_1$: $N(a_1) = \{a_2, a_3\} \cup B$. $G[N(a_1)]$: edges between $\{a_2, a_3\}$ and $B$ (all 6 edges) and edge $\{a_2, a_3\}$? Wait, is $\{a_2, a_3\}$ an edge? We only added $\{a_1, a_2\}$ and $\{a_1, a_3\}$, not $\{a_2, a_3\}$. So $G[N(a_1)]$ has edges $\{a_2, b_j\}$ and $\{a_3, b_j\}$ for $j = 1,2,3$. That's $K_{2,3}$, which has disjoint edges (e.g., $\{a_2, b_1\}$ and $\{a_3, b_2\}$). Not a star or triangle. ✗

So adding 2 edges sharing a vertex within $A$ fails when $|B| \geq 2$.

What about adding 1 edge within $A$ and 1 edge within $B$? Add $\{a_1, a_2\}$ and $\{b_1, b_2\}$. Triangles: $\{a_1, a_2, b_j\}$ for $j = 1,2,3$ and $\{a_i, b_1, b_2\}$ for $i = 1,2,3$. Consider $\{a_1, a_2, b_3\}$ and $\{a_3, b_1, b_2\}$: share no vertex. OK. Consider $\{a_1, a_2, b_1\}$ and $\{a_3, b_1, b_2\}$: share vertex $b_1$ only. Butterfly! ✗

So that doesn't work either.

What about a completely different construction? Let me think...

**Construction: Take $C_5$ (5-cycle) and add a universal vertex.** $C_5$ has 5 edges, universal vertex adds 5 edges, total 10 edges on 6 vertices. The universal vertex $v$ has $N(v) = C_5$. $G[N(v)] = C_5$ which is not a star or triangle. So there exist two triangles through $v$ sharing only $v$. Indeed, $\{v, 1, 2\}$ and $\{v, 3, 4\}$ share only $v$. Butterfly. ✗

**Construction: Take $K_{2,4}$ + 1 edge.** $K_{2,4}$ has 8 edges, + 1 = 9. Less than 10.

**Construction: Take $K_{3,3}$ + 1 edge = 10.** This seems to be the best for $n = 6$.

Let me try to see if 11 edges on 6 vertices must contain a butterfly.

Actually, let me think about this more carefully with the structural characterization.

For a butterfly-free graph, every neighborhood is a star or triangle. Let me count the maximum edges.

Let $G$ be butterfly-free on $n$ vertices. For each vertex $v$, $G[N(v)]$ is a star or triangle.

Let me use a different approach. Let me think about the number of triangles.

If $G$ has no triangles, then $e(G) \leq \lfloor n^2/4 \rfloor$ (Turán/Mantel).

If $G$ has triangles, consider the structure of triangles. In a butterfly-free graph, the triangles can be organized as follows: consider the graph $H$ whose vertices are the triangles of $G$, with two triangles adjacent in $H$ iff they share an edge. The condition is that no two triangles share exactly one vertex. 

Actually, let me think about it as: the set of triangles can be partitioned into "clusters" where within each cluster, all triangles share a common edge, and between clusters, triangles are vertex-disjoint.

Wait, is that true? In $K_4$, the 4 triangles don't all share a common edge. $\{1,2,3\}, \{1,2,4\}, \{1,3,4\}, \{2,3,4\}$. No single edge is in all 4. But any two share an edge. So the "clusters" can be more complex.

Let me think about $K_4$ as a special cluster. In $K_4$, every pair of triangles shares an edge, so no butterfly. $K_4$ has 4 vertices and 6 edges.

For a "book" $B_k$ (k triangles sharing a common edge), we have $k + 2$ vertices and $2k + 1$ edges.

Now, in a butterfly-free graph, can we have both a $K_4$ and a separate book? They need to be vertex-disjoint (otherwise two triangles from different clusters might share exactly one vertex).

Actually, they don't need to be fully vertex-disjoint. Two triangles from different "edge-sharing clusters" must share 0 vertices (not exactly 1). So if triangle $T_1$ is in one cluster and $T_2$ in another, they share 0 vertices.

Hmm, but this is about pairs of triangles, not clusters. Let me think again.

The condition is: for any two triangles, they share 0 or 2+ vertices (not exactly 1).

So if I have a set of triangles where any two share an edge (2+ vertices), that's one "clique" of triangles. And different cliques must be vertex-disjoint.

Wait, not exactly. Two triangles from different cliques must share 0 vertices. But a triangle could potentially be in the "intersection" — no, let me think about this differently.

Let me define a graph $T$ on the triangles of $G$: two triangles are adjacent in $T$ if they share an edge. The butterfly-free condition means: if two triangles are NOT adjacent in $T$ (don't share an edge), they must share 0 vertices (not 1).

So in $T$, non-adjacent triangles are vertex-disjoint. This means: if triangle $T_1$ and $T_2$ share a vertex but not an edge, that's forbidden.

Now, consider the connected components of $T$. Within a component, triangles are connected by edge-sharing. Between components, triangles share no vertices. So each component of $T$ involves a disjoint set of vertices of $G$.

Within a component, what structures are possible? We need that any two triangles in the same component that don't share an edge still share 0 vertices. But they're in the same component, so there's a path of edge-sharing between them. 

Hmm, let me think about small components. A component with 1 triangle: just a triangle, 3 vertices, 3 edges.

A component with 2 triangles sharing an edge: a diamond ($K_4 - e$), 4 vertices, 5 edges.

A component with 3 triangles: 
- All sharing a common edge: book $B_3$, 5 vertices, 7 edges.
- $K_4$: 4 triangles, 4 vertices, 6 edges. Wait, $K_4$ has 4 triangles, not 3.
- Three triangles where $T_1, T_2$ share edge $e_1$, $T_2, T_3$ share edge $e_2$, $T_1, T_3$ share edge $e_3$ or share 0 vertices.

If $T_1, T_3$ share 0 vertices: $T_1 = \{a,b,c\}, T_2 = \{a,b,d\}, T_3 = \{d,e,f\}$ (shares edge $\{a,b\}$ with... no, $T_2$ and $T_3$ share edge, so $T_3$ shares an edge with $T_2 = \{a,b,d\}$. If $T_3 = \{d, e, f\}$, it shares only vertex $d$ with $T_2$, not an edge. So $T_3$ must share an edge with $T_2$. If $T_2 = \{a,b,d\}$, then $T_3$ shares an edge, say $\{a,d\}$: $T_3 = \{a,d,e\}$. Now $T_1 = \{a,b,c\}$ and $T_3 = \{a,d,e\}$ share only vertex $a$. Butterfly! ✗

So we can't have a path of length 2 in $T$ where the endpoints share exactly 1 vertex. The endpoints must share 0 or 2+ vertices.

If $T_1 = \{a,b,c\}, T_2 = \{a,b,d\}, T_3 = \{a,b,e\}$: all share edge $\{a,b\}$. $T_1, T_3$ share edge $\{a,b\}$. ✓ This is a book.

If $T_1 = \{a,b,c\}, T_2 = \{a,b,d\}, T_3 = \{a,c,d\}$: $T_1, T_2$ share $\{a,b\}$. $T_2, T_3$ share $\{a,d\}$. $T_1, T_3$ share $\{a,c\}$. All pairs share an edge. This is part of $K_4$.

If $T_1 = \{a,b,c\}, T_2 = \{a,b,d\}, T_3 = \{b,c,d\}$: $T_1, T_2$ share $\{a,b\}$. $T_2, T_3$ share $\{b,d\}$. $T_1, T_3$ share $\{b,c\}$. All share an edge. Part of $K_4$.

So for 3 triangles in a component, either it's a book (all share a common edge) or part of $K_4$.

For $K_4$ (4 triangles on 4 vertices): all pairs share an edge. ✓

Can we have a component with more than 4 triangles? A book $B_k$ has $k$ triangles, all sharing a common edge, on $k+2$ vertices. That's fine.

Can we have a component that's not a book and not $K_4$? Suppose we have 5 triangles. If they all share a common edge, it's $B_5$. Otherwise, consider $K_4$ plus an extra triangle. $K_4$ on $\{1,2,3,4\}$ has 4 triangles. Add a 5th triangle sharing an edge with one of them, say sharing $\{1,2\}$: the 5th triangle is $\{1,2,5\}$. Now $\{1,2,5\}$ and $\{1,3,4\}$ share only vertex 1. Butterfly! ✗

So we can't extend $K_4$ with more triangles. The only components with more than 4 triangles are books.

What about a component that's a book plus some extra triangles? Book $B_k$ with common edge $\{u,v\}$ and triangles $\{u,v,w_i\}$ for $i = 1, \ldots, k$. Add a triangle $\{u, w_1, w_2\}$. This shares edge $\{u, w_1\}$ with $\{u,v,w_1\}$ and edge $\{u, w_2\}$ with $\{u,v,w_2\}$. But $\{u, w_1, w_2\}$ and $\{u, v, w_3\}$ (for $k \geq 3$) share only vertex $u$. Butterfly! ✗

So if $k \geq 3$, we can't add extra triangles to a book. If $k = 2$, book $B_2$ has triangles $\{u,v,w_1\}, \{u,v,w_2\}$ on 4 vertices. Add $\{u, w_1, w_2\}$: this gives $K_4$ on $\{u,v,w_1,w_2\}$. ✓ (We can add one more triangle $\{v, w_1, w_2\}$ to complete $K_4$.) Can we add a 5th triangle? We showed no.

So the possible triangle components are:
1. Single triangle: 3 vertices, 3 edges (within the component)
2. Diamond ($K_4 - e$): 4 vertices, 5 edges, 2 triangles
3. $K_4$: 4 vertices, 6 edges, 4 triangles
4. Book $B_k$ for $k \geq 3$: $k+2$ vertices, $2k+1$ edges, $k$ triangles

Wait, but these components don't account for all edges between the component vertices. The component is a subgraph of $G$, and there might be additional edges within the component vertices that don't create new triangles.

Hmm, actually, I need to be more careful. The "component" is defined by the triangles, but the vertices of the component might have additional edges between them that don't form triangles (or form triangles that are already counted).

Let me reconsider. Let me think about the vertex set of a triangle component. For a book $B_k$ with edge $\{u,v\}$, the vertex set is $\{u, v, w_1, \ldots, w_k\}$. The edges within this set include $\{u,v\}, \{u,w_i\}, \{v,w_i\}$ for all $i$. Are there edges $\{w_i, w_j\}$? If there were, we'd get a triangle $\{u, w_i, w_j\}$ (since $\{u,w_i\}$ and $\{u,w_j\}$ are edges), which would be a new triangle. As we showed, this creates a butterfly if $k \geq 3$. So for $k \geq 3$, there are no edges between the $w_i$'s.

For $k = 2$ (book $B_2$), we can add edge $\{w_1, w_2\}$ to get $K_4$ (creating 2 more triangles). Or we can leave it as $B_2$ (diamond).

For $K_4$, all edges are present, so no more edges can be added within the 4 vertices.

Now, the key insight: different triangle components use disjoint vertex sets. The remaining vertices (not in any triangle) form a triangle-free subgraph, and edges between different components and non-triangle vertices must be carefully controlled.

Let me think about the overall structure. Let the triangle components be $C_1, \ldots, C_t$ with vertex sets $V_1, \ldots, V_t$ (disjoint). Let $R$ be the remaining vertices (not in any triangle). 

Edges in $G$:
1. Within each $V_i$: edges of the component.
2. Within $R$: triangle-free, so at most $\lfloor |R|^2/4 \rfloor$ edges.
3. Between $V_i$ and $V_j$: any edge here could create triangles. Need to be careful.
4. Between $V_i$ and $R$: any edge here could create triangles.

This is getting complex. Let me think about whether cross-edges can exist.

If there's an edge between $u \in V_i$ and $w \in V_j$ (or $w \in R$), could this create a triangle? A triangle needs 3 edges. If $u$ has a neighbor $u'$ in $V_i$ and $w$ has a neighbor $w'$ in $V_j$ (or $R$), and there are edges $\{u, u'\}$, $\{w, w'\}$, $\{u, w\}$, we need $\{u', w'\}$ to also be an edge for a triangle. But $u'$ and $w'$ are in different components, so $\{u', w'\}$ would be another cross-edge.

Actually, triangles can also form using 2 vertices from one component and 1 from outside, or 1 from each of two components and 1 from $R$, etc.

This is getting very complicated. Let me try a different approach: just compute $m(n)$ for each $n$ from 5 to 10 by finding the extremal number.

Let me think about this more carefully using the following approach: 

**Claim:** $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$ for $n \geq 5$, where $B$ is the butterfly.

Wait, for $n = 5$, we found $\text{ex}(5, B) = 7 = \lfloor 25/4 \rfloor + 1 = 6 + 1 = 7$. ✓

For $n = 6$, the construction gives $10 = \lfloor 36/4 \rfloor + 1 = 9 + 1 = 10$. We need to verify this is optimal.

Let me try to prove the upper bound. Actually, let me think about whether the answer might be different.

Let me consider the problem from the perspective of the Simonovits stability theorem or related results. The butterfly graph $B$ has chromatic number 3 (it's 3-colorable). For 3-chromatic forbidden graphs, the Erdős–Simonovits theorem gives $\text{ex}(n, H) = \frac{n^2}{4} + o(n^2)$ for any 3-chromatic $H$. But the exact value depends on the specific graph.

For the butterfly specifically, I recall that the extremal graph is $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ plus one edge within one part, giving $\lfloor n^2/4 \rfloor + 1$ edges. And this is optimal for $n$ sufficiently large.

But is it optimal for all $n \geq 5$? Let me check $n = 6$ more carefully.

For $n = 6$, can we achieve 11 edges without a butterfly?

Let me try some constructions:
- $K_{3,3}$ + 2 edges: we showed adding 2 edges within one part fails.
- $K_4$ + 2 more vertices with some edges: we showed it's hard to connect to $K_4$.

Let me try: Take $K_4$ on $\{1,2,3,4\}$ (6 edges) and add vertices 5, 6 as an independent set, each connected to all of $\{1,2,3,4\}$. That's $6 + 8 = 14$ edges. But this creates many butterflies. For instance, $\{1,2,3\}$ and $\{1,4,5\}$ share only vertex 1. ✗

What if 5 and 6 are each connected to only 2 vertices of $K_4$? Say 5 connected to $\{1,2\}$ and 6 connected to $\{3,4\}$. Edges: 6 (from $K_4$) + 2 + 2 = 10. Triangles: $\{1,2,5\}$ and $\{3,4,6\}$. These share 0 vertices. ✓ But check: $\{1,2,3\}$ (from $K_4$) and $\{1,2,5\}$ share edge $\{1,2\}$. ✓ $\{1,2,3\}$ and $\{3,4,6\}$ share vertex 3 only. Butterfly! ✗

What if 5 and 6 are connected to the same 2 vertices? Say both connected to $\{1,2\}$. Edges: 6 + 2 + 2 = 10. Triangles: $\{1,2,5\}, \{1,2,6\}$, and the 4 triangles of $K_4$. $\{1,2,5\}$ and $\{3,4,5\}$... wait, is $\{3,4,5\}$ a triangle? 5 is connected to 1 and 2, not 3 or 4. So no. $\{1,2,5\}$ and $\{1,3,4\}$ share vertex 1 only. Butterfly! ✗

So connecting to $K_4$ is really problematic. The triangles in $K_4$ share vertices with everything.

What if we don't use $K_4$? Let me try a different structure.

Take a 5-cycle $\{1,2,3,4,5\}$ and add vertex 6 connected to all 5. Edges: 5 + 5 = 10. Triangles: $\{6, i, i+1\}$ for $i = 1, \ldots, 5$ (mod 5). $\{6,1,2\}$ and $\{6,3,4\}$ share only vertex 6. Butterfly. ✗

Take $K_{3,3}$ + 1 edge = 10. Can we add an 11th edge somewhere?

$K_{3,3}$ on $A = \{a_1, a_2, a_3\}, B = \{b_1, b_2, b_3\}$, plus edge $\{a_1, a_2\}$. Can we add another edge? Options:
- $\{a_1, a_3\}$: star within $A$, but we showed $G[N(a_1)]$ becomes $K_{2,3}$, not a star. ✗
- $\{a_2, a_3\}$: similar. ✗
- $\{b_1, b_2\}$: creates triangles $\{a_i, b_1, b_2\}$ for $i = 1,2,3$. $\{a_1, a_2, b_1\}$ and $\{a_3, b_1, b_2\}$ share $b_1$ only. Butterfly. ✗
- $\{b_1, b_3\}$ or $\{b_2, b_3\}$: similar. ✗

So we can't add an 11th edge to this construction. 

Let me try a completely different 11-edge graph on 6 vertices. 

Actually, let me think about it from the upper bound side. Let me try to prove that $\text{ex}(n, B) \leq \lfloor n^2/4 \rfloor + 1$ for $n \geq 5$.

**Proof attempt:** Let $G$ be a butterfly-free graph on $n$ vertices. We want to show $e(G) \leq \lfloor n^2/4 \rfloor + 1$.

If $G$ is triangle-free, $e(G) \leq \lfloor n^2/4 \rfloor$ by Mantel's theorem. ✓

If $G$ has at least one triangle, consider the structure. Let $T$ be a triangle in $G$ on vertices $\{a, b, c\}$. 

For any vertex $v$ not in $T$, $v$ can be adjacent to at most 2 vertices of $T$ (otherwise, if $v$ is adjacent to all 3, we get 3 new triangles $\{v,a,b\}, \{v,b,c\}, \{v,a,c\}$, and $\{v,a,b\}$ shares only $v$ with $\{a,b,c\}$... wait, $\{v,a,b\}$ and $\{a,b,c\}$ share edge $\{a,b\}$. So they share 2 vertices. That's OK. But $\{v,a,b\}$ and $\{v,b,c\}$ share edge $\{v,b\}$. OK. $\{v,a,b\}$ and $\{v,a,c\}$ share edge $\{v,a\}$. OK. So $v$ adjacent to all 3 of $T$ gives $K_4$, which is fine.

But if $v$ is adjacent to all 3 of $T$, and there's another vertex $w$ adjacent to 2 vertices of $T$, say $\{a, b\}$, then $\{v, a, c\}$ and $\{w, a, b\}$ share only vertex $a$. Butterfly! ✗ (assuming $v \neq w$ and $w$ is not adjacent to $c$).

Hmm, so the constraint is more subtle. Let me think about this differently.

Let me use the structural characterization. For every vertex $v$, $G[N(v)]$ is a star or triangle.

Let me consider the complement approach or an induction approach.

Actually, let me just try to compute the values for $n = 5, 6, 7, 8, 9, 10$ assuming $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$, and then verify.

$n = 5$: $\lfloor 25/4 \rfloor + 1 = 6 + 1 = 7$. $m(5) = 8$.
$n = 6$: $\lfloor 36/4 \rfloor + 1 = 9 + 1 = 10$. $m(6) = 11$.
$n = 7$: $\lfloor 49/4 \rfloor + 1 = 12 + 1 = 13$. $m(7) = 14$.
$n = 8$: $\lfloor 64/4 \rfloor + 1 = 16 + 1 = 17$. $m(8) = 18$.
$n = 9$: $\lfloor 81/4 \rfloor + 1 = 20 + 1 = 21$. $m(9) = 22$.
$n = 10$: $\lfloor 100/4 \rfloor + 1 = 25 + 1 = 26$. $m(10) = 27$.

Sum = 8 + 11 + 14 + 18 + 22 + 27 = 100.

But I need to verify that $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$ for all these $n$.

Let me verify $n = 7$. Construction: $K_{3,4}$ + 1 edge = $12 + 1 = 13$. No butterfly (same argument as before). Can we get 14 edges on 7 vertices without a butterfly?

Let me think about whether there's a better construction for some $n$.

**Alternative construction: $K_4$ on 4 vertices + $K_{\lfloor (n-4)/2 \rfloor, \lceil (n-4)/2 \rceil}$ on the remaining $n-4$ vertices, with no edges between them.** Edges = $6 + \lfloor (n-4)^2/4 \rfloor$. For $n = 7$: $6 + \lfloor 9/4 \rfloor = 6 + 2 = 8$. Worse than 13.

**Alternative: Two disjoint $K_4$'s for $n = 8$.** Edges = $6 + 6 = 12$. Worse than 17.

**Alternative: $K_4$ + complete bipartite on remaining, with some cross-edges.** This seems hard to make work.

Let me also consider: **Book $B_k$ + complete bipartite on remaining.** Book $B_k$ on $k+2$ vertices with $2k+1$ edges, plus $K_{\lfloor (n-k-2)/2 \rfloor, \lceil (n-k-2)/2 \rceil}$ on the remaining $n-k-2$ vertices, no cross-edges. Total: $2k+1 + \lfloor (n-k-2)^2/4 \rfloor$.

For $n = 7, k = 1$: $3 + \lfloor 25/4 \rfloor = 3 + 6 = 9$. Worse than 13.
For $n = 7, k = 2$: $5 + \lfloor 16/4 \rfloor = 5 + 4 = 9$. Worse.
For $n = 7, k = 5$: $11 + \lfloor 0/4 \rfloor = 11$. Worse than 13.

So the bipartite + 1 edge construction seems best.

But wait, can we have cross-edges between a triangle component and the bipartite part? If we have a book $B_1$ (single triangle $\{a,b,c\}$) and a bipartite graph on the remaining vertices, can we add edges between them?

If vertex $d$ (in the bipartite part) is connected to $a$ and $b$, we get triangle $\{a,b,d\}$, which shares edge $\{a,b\}$ with $\{a,b,c\}$. OK. But if another vertex $e$ is connected to $a$ and $c$, we get triangle $\{a,c,e\}$, which shares only vertex $a$ with $\{a,b,d\}$. Butterfly! ✗

So cross-edges are very restricted. Essentially, if we have a triangle $\{a,b,c\}$, any external vertex can be connected to at most 2 vertices of the triangle, and those 2 must be the same pair for all external vertices (to avoid butterflies). So all external vertices connected to the triangle must connect to the same edge, say $\{a,b\}$. This extends the triangle to a book.

So the structure is: we have a book $B_k$ (possibly $k=0$, i.e., no triangles) on some vertex set, and the remaining vertices form a bipartite graph with no edges to the book.

Wait, but can the remaining vertices have edges to the book's "spine" vertices (the two vertices of the common edge)? Let me think...

If we have book $B_k$ with common edge $\{u,v\}$ and pages $w_1, \ldots, w_k$, and an external vertex $x$ connected to $u$ (but not $v$ or any $w_i$), then $x$ doesn't form any triangle with the book. But $x$ might form triangles with other external vertices. As long as those triangles don't share exactly one vertex with the book's triangles, we're fine.

A triangle involving $x$ and two other external vertices $y, z$ would share 0 vertices with the book's triangles (if $y, z$ are also external). ✓

A triangle $\{x, u, y\}$ where $x, y$ are external and $u$ is the book's spine: this shares vertex $u$ with triangle $\{u, v, w_i\}$. If $y \neq v$ and $y \neq w_i$, this is a butterfly! ✗

So external vertices can't be connected to the book's spine vertices (unless they're also connected to $v$, making them part of the book).

Hmm, what if $x$ is connected to both $u$ and $v$? Then $x$ is a page of the book (triangle $\{u,v,x\}$). So $x$ is part of the book.

What if $x$ is connected to $u$ and some $w_i$? Then triangle $\{u, w_i, x\}$ (if $\{u, w_i\}$ is an edge, which it is). This shares edge $\{u, w_i\}$ with $\{u, v, w_i\}$. But it shares only vertex $u$ with $\{u, v, w_j\}$ for $j \neq i$. Butterfly if $k \geq 2$! ✗

So for $k \geq 2$, external vertices can't connect to any book vertex. For $k = 1$ (single triangle), an external vertex $x$ connected to $u$ and $w_1$: triangle $\{u, w_1, x\}$ shares edge $\{u, w_1\}$ with $\{u, v, w_1\}$. The only other triangle is $\{u, v, w_1\}$. So no butterfly. But now we have a new triangle, and we need to check all pairs. $\{u, w_1, x\}$ and $\{u, v, w_1\}$ share edge $\{u, w_1\}$. ✓. But if another external vertex $y$ is connected to $u$ and $v$: triangle $\{u, v, y\}$ shares only $u$ with $\{u, w_1, x\}$. Butterfly! ✗

So for $k = 1$, external vertices can connect to at most one pair of the triangle's vertices, and all must connect to the same pair. This extends the book.

OK so the conclusion is: in a butterfly-free graph, the vertex set can be partitioned into:
1. A book $B_k$ (for some $k \geq 0$; $k = 0$ means no triangles) on $k + 2$ vertices (or 0 vertices if no triangles).
2. A triangle-free graph on the remaining $n - k - 2$ vertices (or $n$ vertices if no triangles).
3. No edges between the book and the triangle-free part.

Wait, but I showed that external vertices can't connect to book vertices (for $k \geq 2$) or can only extend the book (for $k = 1$). So there are truly no edges between the book and the rest.

Hmm, but this isn't quite right either. What if an external vertex is connected to just one book vertex? Say $x$ is connected to $u$ (spine of book) but not to $v$ or any $w_i$. Then $x$ doesn't form a triangle with any book vertices (since it's only connected to $u$, and a triangle needs 2 neighbors of $x$ that are adjacent). So no new triangles involving $x$ and book vertices. ✓

But we need to check: does $x$ being connected to $u$ create issues with the neighborhood condition? $N(u)$ includes $v, w_1, \ldots, w_k, x$, and possibly other external vertices. $G[N(u)]$ must be a star or triangle. The edges in $G[N(u)]$ include $\{v, w_i\}$ for all $i$ (since $v$ is connected to all $w_i$ in the book). If $x$ is connected to some other vertex $y \in N(u)$, that adds an edge. But we need $G[N(u)]$ to remain a star or triangle.

The edges $\{v, w_i\}$ for $i = 1, \ldots, k$ form a star centered at $v$ (in $G[N(u)]$). If $k \geq 3$, this star has $k \geq 3$ edges. Adding $x$ to $N(u)$: if $x$ has no edges to other vertices in $N(u)$, then $G[N(u)]$ is a star (centered at $v$) plus an isolated vertex $x$. But a star plus an isolated vertex is NOT a star or triangle (it has $k + 1$ vertices and $k$ edges, with $k \geq 3$). ✗

So for $k \geq 3$, we can't add $x$ to $N(u)$ without connecting $x$ to $v$ (which would make $x$ a page of the book). 

For $k = 2$: $G[N(u)]$ has edges $\{v, w_1\}, \{v, w_2\}$, a star with 2 edges on 3 vertices. Adding $x$: $G[N(u)]$ has 4 vertices and 2 edges (star + isolated). Not a star (4 vertices) or triangle. ✗

For $k = 1$: $G[N(u)]$ has edge $\{v, w_1\}$, a star with 1 edge on 2 vertices (plus $u$'s other neighbors). Adding $x$: $G[N(u)]$ has vertices $\{v, w_1, x, \ldots\}$ and edge $\{v, w_1\}$ plus any edges involving $x$. If $x$ has no edges to $v$ or $w_1$, then $G[N(u)]$ is a single edge plus isolated vertices. This is a star (with center $v$ or $w_1$) only if there are no other edges. But if $u$ has other neighbors in the external part, and those neighbors have edges among themselves...

This is getting very complicated. Let me try a cleaner approach.

Let me just try to prove the upper bound $\text{ex}(n, B) \leq \lfloor n^2/4 \rfloor + 1$ directly.

**Proof of upper bound:**

Let $G$ be a butterfly-free graph on $n$ vertices with $m$ edges. We want to show $m \leq \lfloor n^2/4 \rfloor + 1$.

If $G$ is triangle-free, $m \leq \lfloor n^2/4 \rfloor \leq \lfloor n^2/4 \rfloor + 1$. ✓

If $G$ has a triangle, let $\Delta$ be the set of triangles. Consider the graph $H$ on the same vertex set where we define a partition based on the triangle structure.

Actually, let me use a different approach. Let me use the following lemma:

**Lemma:** In a butterfly-free graph, if $e$ is an edge that is in at least one triangle, then either:
(a) $e$ is in exactly one triangle, or
(b) $e$ is in multiple triangles, and all triangles in the graph use edges from a single "book" or $K_4$ structure.

Hmm, this isn't precise enough. Let me think differently.

**Key observation:** In a butterfly-free graph, consider any edge $e = \{u, v\}$ that is in $k$ triangles. The $k$ triangles are $\{u, v, w_1\}, \ldots, \{u, v, w_k\}$. Any other triangle $T$ in the graph must share 0 or 2+ vertices with each $\{u, v, w_i\}$.

If $T$ shares 2 vertices with $\{u, v, w_i\}$: either $T$ contains $u$ and $v$ (so $T = \{u, v, w_j\}$, already counted), or $T$ contains $u$ and $w_i$ (so $T = \{u, w_i, x\}$ for some $x$), or $T$ contains $v$ and $w_i$ (so $T = \{v, w_i, x\}$).

If $T = \{u, w_i, x\}$ with $x \neq v$: $T$ shares vertex $u$ with $\{u, v, w_j\}$ for $j \neq i$. If $x \neq w_j$ and $v \neq w_j$ (which is true) and $w_i \neq w_j$ (true) and $x \neq v$ (assumed), then $T$ and $\{u, v, w_j\}$ share only vertex $u$. Butterfly! ✗ (if $k \geq 2$, i.e., there exists $j \neq i$).

So if $k \geq 2$ (edge $\{u,v\}$ is in at least 2 triangles), then no triangle of the form $\{u, w_i, x\}$ with $x \neq v$ can exist. Similarly, no $\{v, w_i, x\}$ with $x \neq u$.

If $k = 1$ (edge $\{u,v\}$ is in exactly 1 triangle $\{u, v, w\}$), then triangles $\{u, w, x\}$ or $\{v, w, x\}$ could exist, but they must not create butterflies with other triangles.

This is still complex. Let me try yet another approach.

**Approach via edge counting:**

Let $G$ be butterfly-free on $n$ vertices. Let $t$ be the number of triangles. 

For each edge $e$, let $t(e)$ be the number of triangles containing $e$. Then $\sum_e t(e) = 3t$.

The condition implies a strong constraint on the triangle structure. Let me think about the "triangle edge" graph: edges that are in at least one triangle.

Let me define $F$ as the subgraph of $G$ consisting of edges that are in at least one triangle. The edges not in $F$ are "triangle-free edges."

**Claim:** $F$ is a union of vertex-disjoint components, each being either a $K_3$, $K_4$, or a book $B_k$ ($k \geq 2$).

Wait, I think I showed this above. The triangle components are:
- Single triangle ($K_3$): 3 vertices, 3 edges
- Diamond ($K_4 - e$): 4 vertices, 5 edges, 2 triangles (book $B_2$)
- $K_4$: 4 vertices, 6 edges, 4 triangles
- Book $B_k$ for $k \geq 3$: $k+2$ vertices, $2k+1$ edges, $k$ triangles

And these components are vertex-disjoint.

Now, the edges of $G$ consist of:
1. Edges within triangle components (the $F$ edges)
2. Edges between different triangle components: must be 0 (since a triangle in one component and a triangle in another are vertex-disjoint, but an edge between components could create a new triangle... actually, an edge between components doesn't necessarily create a triangle. But if it did, the new triangle would share vertices with both components.)

Wait, actually, edges between different triangle components don't necessarily create triangles. An edge $\{u, v\}$ with $u$ in component $C_1$ and $v$ in component $C_2$ is just an edge. It creates a triangle only if there's a common neighbor of $u$ and $v$ that is adjacent to both.

But if such a triangle exists, it would share vertices with triangles in $C_1$ and $C_2$, potentially creating a butterfly.

Let me think about this. Suppose $u \in C_1$, $v \in C_2$, and $w$ is a common neighbor with $\{u,w\}$ and $\{v,w\}$ edges. Then $\{u,v,w\}$ is a triangle. If $C_1$ has a triangle containing $u$, say $\{u, a, b\}$, then $\{u,v,w\}$ and $\{u,a,b\}$ share vertex $u$. If $v,w \notin \{a,b\}$ (which is true since $C_1$ and $C_2$ are vertex-disjoint and $w$ is not in $C_1$... well, $w$ could be in $C_1$ or $C_2$ or neither).

If $w \in C_1$: then $\{u, w\}$ is an edge in $C_1$. The triangle $\{u, v, w\}$ shares edge $\{u, w\}$ with some triangle in $C_1$ (if $\{u, w\}$ is a triangle edge in $C_1$). But it shares only vertex $u$ or $w$ with other triangles in $C_1$.

This is getting too complicated. Let me try to just verify the values computationally for small $n$.

Actually, I can't use tools. Let me think about this more carefully.

Let me try to prove the upper bound more carefully.

**Theorem:** For $n \geq 5$, $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$.

**Lower bound:** $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ plus one edge within the larger part gives $\lfloor n^2/4 \rfloor + 1$ edges and is butterfly-free. ✓

**Upper bound:** Let $G$ be butterfly-free on $n$ vertices with $m$ edges. We show $m \leq \lfloor n^2/4 \rfloor + 1$.

Case 1: $G$ is triangle-free. $m \leq \lfloor n^2/4 \rfloor$. ✓

Case 2: $G$ has at least one triangle. 

Let me use the following approach. Pick any triangle $T = \{a, b, c\}$ in $G$. Partition the remaining $n - 3$ vertices based on their adjacency to $T$:
- $V_0$: vertices adjacent to 0 vertices of $T$
- $V_1$: vertices adjacent to exactly 1 vertex of $T$
- $V_2$: vertices adjacent to exactly 2 vertices of $T$
- $V_3$: vertices adjacent to all 3 vertices of $T$

A vertex in $V_3$ creates 3 triangles with $T$: $\{v, a, b\}, \{v, b, c\}, \{v, a, c\}$. Together with $T$, this is $K_4$ on $\{a, b, c, v\}$. If there are two vertices $v, w \in V_3$, then $\{v, a, b\}$ and $\{w, a, c\}$ share only vertex $a$. Butterfly! ✗ So $|V_3| \leq 1$.

If $|V_3| = 1$, say $V_3 = \{d\}$, we have $K_4$ on $\{a,b,c,d\}$. Now consider any other vertex $x$. If $x$ is adjacent to 2 vertices of $\{a,b,c,d\}$, say $a$ and $b$, then $\{x, a, b\}$ is a triangle. $\{x, a, b\}$ and $\{c, a, d\}$ (a triangle in $K_4$) share only vertex $a$. Butterfly! ✗ (since $x \neq c, d$ and $b \neq c, d$). So $x$ can be adjacent to at most 1 vertex of $\{a,b,c,d\}$.

So with $K_4$: the 4 vertices of $K_4$ have 6 edges among them. Each of the remaining $n - 4$ vertices is adjacent to at most 1 vertex of $K_4$, contributing at most $n - 4$ edges. Among the remaining $n - 4$ vertices, the subgraph is butterfly-free (and triangle-free? not necessarily, but let me think...).

Actually, the remaining $n-4$ vertices could have their own triangles, forming their own triangle components. But by the same argument, those components are vertex-disjoint from $K_4$.

The edges among the remaining $n-4$ vertices: at most $\text{ex}(n-4, B)$ (by induction, if we had an inductive argument). Plus at most $n - 4$ edges to $K_4$.

Total: $6 + (n-4) + \text{ex}(n-4, B) = n + 2 + \text{ex}(n-4, B)$.

If $\text{ex}(n-4, B) = \lfloor (n-4)^2/4 \rfloor + 1$, total = $n + 2 + \lfloor (n-4)^2/4 \rfloor + 1 = n + 3 + \lfloor (n-4)^2/4 \rfloor$.

Compare with $\lfloor n^2/4 \rfloor + 1$:
- $n$ even: $\lfloor n^2/4 \rfloor + 1 = n^2/4 + 1$. $n + 3 + (n-4)^2/4 = n + 3 + (n^2 - 8n + 16)/4 = n + 3 + n^2/4 - 2n + 4 = n^2/4 - n + 7$. We need $n^2/4 - n + 7 \leq n^2/4 + 1$, i.e., $-n + 7 \leq 1$, i.e., $n \geq 6$. ✓ for $n \geq 6$.
- $n$ odd: $\lfloor n^2/4 \rfloor + 1 = (n^2-1)/4 + 1$. $n + 3 + \lfloor (n-4)^2/4 \rfloor$. If $n$ is odd, $n - 4$ is odd, so $\lfloor (n-4)^2/4 \rfloor = ((n-4)^2 - 1)/4 = (n^2 - 8n + 15)/4$. Total: $n + 3 + (n^2 - 8n + 15)/4 = (4n + 12 + n^2 - 8n + 15)/4 = (n^2 - 4n + 27)/4$. We need $(n^2 - 4n + 27)/4 \leq (n^2 - 1)/4 + 1 = (n^2 + 3)/4$. So $n^2 - 4n + 27 \leq n^2 + 3$, i.e., $-4n + 27 \leq 3$, i.e., $n \geq 6$. ✓ for $n \geq 6$.

So the $K_4$ case gives fewer edges than the bipartite+1 construction for $n \geq 6$. For $n = 5$: $K_4$ + 1 remaining vertex, adjacent to at most 1 vertex of $K_4$: $6 + 1 = 7$ edges. Same as $\lfloor 25/4 \rfloor + 1 = 7$. So both constructions give 7 for $n = 5$.

Now let me handle the case $|V_3| = 0$, i.e., no vertex is adjacent to all 3 vertices of $T$.

If $|V_3| = 0$, every vertex outside $T$ is in $V_0, V_1,$ or $V_2$.

A vertex $v \in V_2$ adjacent to, say, $a$ and $b$: creates triangle $\{v, a, b\}$, which shares edge $\{a, b\}$ with $T$. ✓

Now, if $v, w \in V_2$ are both adjacent to $a$ and $b$: triangles $\{v, a, b\}$ and $\{w, a, b\}$ share edge $\{a, b\}$. ✓. But if $v$ is adjacent to $a, b$ and $w$ is adjacent to $a, c$: $\{v, a, b\}$ and $\{w, a, c\}$ share only $a$. Butterfly! ✗

So all vertices in $V_2$ must be adjacent to the same pair of vertices from $T$. WLOG, all $V_2$ vertices are adjacent to $a$ and $b$.

Now, $V_2$ vertices together with $a, b$ form a book $B_{|V_2|+1}$ (the triangle $T$ plus $|V_2|$ more triangles, all sharing edge $\{a, b\}$).

What about $V_1$ and $V_0$ vertices? 

A $V_1$ vertex $x$ adjacent to, say, $a$: $x$ doesn't form a triangle with $T$. But if $x$ is also adjacent to some $v \in V_2$, and $v$ is adjacent to $a$, then $\{x, a, v\}$ is a triangle. This triangle shares vertex $a$ with $\{a, b, c\}$ (triangle $T$). If $x \neq b, c$ and $v \neq b, c$ (true since $v \in V_2$ is adjacent to $a, b$ and $v \neq c$ since $v \notin V_3$), then $\{x, a, v\}$ and $\{a, b, c\}$ share only $a$. Butterfly! ✗

So $V_1$ vertices adjacent to $a$ cannot be adjacent to any $V_2$ vertex. Similarly, $V_1$ vertices adjacent to $b$ cannot be adjacent to any $V_2$ vertex (since $V_2$ vertices are all adjacent to $b$).

What about $V_1$ vertices adjacent to $c$? A vertex $x$ adjacent to only $c$: if $x$ is adjacent to some $v \in V_2$ (which is adjacent to $a, b$), is $\{x, c, v\}$ a triangle? Only if $\{c, v\}$ is an edge. But $v \in V_2$ is adjacent to $a, b$ only (not $c$, since $v \notin V_3$). So $\{c, v\}$ is not an edge. No triangle. ✓

But what if $x$ (adjacent to $c$) is adjacent to $y$ (adjacent to $a$), and $\{x, y\}$ is an edge? Then $\{x, y, c\}$ is not a triangle (since $y$ is not adjacent to $c$). $\{x, y, a\}$ is not a triangle (since $x$ is not adjacent to $a$). So no triangle involving both $x$ and $y$ unless there's a common neighbor.

This is getting very involved. Let me try to bound the total edges more carefully.

Let me set up notation. $T = \{a, b, c\}$, $|V_2| = p$ (all adjacent to $a, b$), $|V_1| = q_1$ (adjacent to $a$ only) + $q_2$ (adjacent to $b$ only) + $q_3$ (adjacent to $c$ only), $|V_0| = r$. $p + q_1 + q_2 + q_3 + r = n - 3$.

Edges:
1. Within $T$: 3
2. Between $T$ and $V_2$: $2p$ (each $V_2$ vertex connects to $a, b$)
3. Between $T$ and $V_1$: $q_1 + q_2 + q_3$ (each connects to one vertex of $T$)
4. Between $T$ and $V_0$: 0
5. Within $V_2 \cup \{a, b\}$: the book has $2p + 1$ edges (edge $\{a,b\}$ plus $2p$ edges to pages). But we already counted $\{a,b\}$ in (1) and the $2p$ edges in (2). Are there edges within $V_2$? If $v, w \in V_2$ and $\{v, w\}$ is an edge, then $\{a, v, w\}$ is a triangle (since $a$ is adjacent to both). This triangle shares vertex $a$ with $\{a, b, c\}$. If $w \neq b, c$ (true), butterfly! ✗ (if $p \geq 1$... wait, $\{a, v, w\}$ and $\{a, b, c\}$ share only $a$ if $v, w \neq b, c$. Since $v, w \in V_2$ and $V_2 \cap T = \emptyset$, yes. So butterfly.) 

So no edges within $V_2$ (if $p \geq 1$). Actually, even if $p = 0$, $V_2$ is empty, so trivially no edges.

Wait, I need to be more careful. If $p \geq 2$ and there's an edge $\{v, w\}$ within $V_2$, then $\{a, v, w\}$ is a triangle. This shares only $a$ with $\{a, b, c\}$. Butterfly. ✗. So no edges within $V_2$.

6. Edges within $V_1$: vertices in $V_1$ adjacent to different vertices of $T$ might have edges between them. Let me think about what's allowed.

Let $A_1 = V_1$ vertices adjacent to $a$, $B_1 = V_1$ vertices adjacent to $b$, $C_1 = V_1$ vertices adjacent to $c$.

Edges within $A_1$: if $x, y \in A_1$ and $\{x, y\}$ is an edge, then $\{a, x, y\}$ is a triangle. This shares only $a$ with $\{a, b, c\}$. Butterfly! ✗ So no edges within $A_1$.

Similarly, no edges within $B_1$ or $C_1$.

Edges between $A_1$ and $B_1$: if $x \in A_1, y \in B_1, \{x, y\}$ edge. Triangle $\{a, x, y\}$? Need $\{a, y\}$ edge, but $y \in B_1$ is adjacent to $b$ only, not $a$. So no. Triangle $\{b, x, y\}$? Need $\{b, x\}$ edge, but $x \in A_1$ is adjacent to $a$ only. No. So $\{x, y\}$ doesn't create a triangle with $T$. ✓

But does $\{x, y\}$ create a triangle with any other triangle? If $p \geq 1$, there's a book triangle $\{a, b, v\}$ for $v \in V_2$. $\{x, y\}$ and $\{a, b, v\}$: $x \in A_1, y \in B_1$, $v \in V_2$. The edge $\{x, y\}$ is not a triangle by itself. But if $x$ is adjacent to $v$ (both in $A_1 \cup V_2$... wait, $v \in V_2$ is adjacent to $a, b$. $x \in A_1$ is adjacent to $a$. If $\{x, v\}$ is an edge, then $\{a, x, v\}$ is a triangle (since $a$ adjacent to both $x$ and $v$). This shares only $a$ with $\{a, b, c\}$. Butterfly! ✗

So $A_1$ vertices cannot be adjacent to $V_2$ vertices. Similarly, $B_1$ vertices cannot be adjacent to $V_2$ vertices.

What about $C_1$ and $V_2$? $x \in C_1$ (adjacent to $c$), $v \in V_2$ (adjacent to $a, b$). If $\{x, v\}$ is an edge: triangle $\{c, x, v\}$? Need $\{c, v\}$ edge, but $v$ is not adjacent to $c$. No. Triangle $\{a, x, v\}$? Need $\{a, x\}$ edge, but $x \in C_1$ is adjacent to $c$ only. No. So $\{x, v\}$ doesn't create a triangle. ✓

But we need to check butterflies with existing triangles. The edge $\{x, v\}$ itself isn't a triangle. But if $x$ and $v$ have a common neighbor $z$ with $\{x, z\}$ and $\{v, z\}$ edges, then $\{x, v, z\}$ is a triangle. If $z = a$: $\{a, x\}$ not an edge. If $z = b$: $\{b, x\}$ not an edge. If $z = c$: $\{c, v\}$ not an edge. If $z \in V_2$: $\{x, z\}$ — $x \in C_1, z \in V_2$. We just said this is OK (no triangle with $T$). But $\{v, z\}$ — both in $V_2$, and we showed no edges within $V_2$. So $z \notin V_2$ (as a neighbor of $v$). If $z \in C_1$: $\{v, z\}$ — $v \in V_2, z \in C_1$, same as $\{x, v\}$ type, OK. But $\{x, z\}$ — both in $C_1$, no edges within $C_1$. So $z \notin C_1$. 

This is getting really complicated. Let me try to simplify by considering the structure more carefully.

Let me define the "book part" as $B = \{a, b\} \cup V_2$ (the book with edge $\{a, b\}$ and $p$ pages), and the "rest" as $R = V_0 \cup V_1 = V_0 \cup A_1 \cup B_1 \cup C_1$.

I've shown:
- No edges within $V_2$
- No edges within $A_1, B_1, C_1$
- No edges between $A_1$ and $V_2$, or $B_1$ and $V_2$
- Edges between $A_1$ and $B_1$ are OK (don't create triangles with $T$)
- Edges between $C_1$ and $V_2$ are OK (don't create triangles with $T$)

What about edges between $A_1$ and $C_1$? $x \in A_1, y \in C_1, \{x, y\}$ edge. Triangle $\{a, x, y\}$? Need $\{a, y\}$, but $y \in C_1$ not adjacent to $a$. No. Triangle $\{c, x, y\}$? Need $\{c, x\}$, but $x \in A_1$ not adjacent to $c$. No. So no triangle with $T$. ✓

But could $\{x, y\}$ create a triangle with a book triangle? If $p \geq 1$, book has triangle $\{a, b, v\}$. $\{x, y\}$ and this triangle: $x \in A_1, y \in C_1, v \in V_2$. For a new triangle involving $\{x, y\}$, need a common neighbor. $a$ is adjacent to $x$ but not $y$. $c$ is adjacent to $y$ but not $x$. $v$ is adjacent to... $v$ is adjacent to $a, b$. Is $v$ adjacent to $x$ or $y$? $v \in V_2, x \in A_1$: we said no edges between $A_1$ and $V_2$. $v \in V_2, y \in C_1$: edges allowed but not assumed. So unless $\{v, y\}$ is an edge, no triangle. And even if $\{v, y\}$ is an edge, the triangle would be $\{y, v, ?\}$ — need a common neighbor of $y$ and $v$ that's adjacent to both. $c$ is adjacent to $y$ but not $v$. $a$ is adjacent to $v$ but not $y$. So no triangle from $\{v, y\}$ alone.

OK so edges between $A_1$ and $C_1$, $B_1$ and $C_1$, $A_1$ and $B_1$ are all OK (don't directly create triangles with $T$ or the book). But they might create triangles among themselves, which could create butterflies.

Let me think about the subgraph on $R = V_0 \cup A_1 \cup B_1 \cup C_1$. This subgraph must itself be butterfly-free (since any butterfly in it is a butterfly in $G$). Also, triangles in this subgraph must not create butterflies with the book triangles.

A triangle in $R$ shares 0 vertices with the book triangles (since $R \cap B = \emptyset$). So triangles in $R$ and book triangles are vertex-disjoint. ✓ No butterfly between them.

So the subgraph on $R$ is butterfly-free, and by induction, has at most $\text{ex}(|R|, B)$ edges.

Now, edges between $R$ and the book $B = \{a, b\} \cup V_2$:
- $A_1$ to $a$: $|A_1|$ edges (already counted as $V_1$-$T$ edges)
- $B_1$ to $b$: $|B_1|$ edges
- $C_1$ to $c$: $|C_1|$ edges
- $C_1$ to $V_2$: at most $|C_1| \cdot |V_2|$ edges (allowed)
- $A_1$ to $V_2$: 0 (forbidden)
- $B_1$ to $V_2$: 0 (forbidden)
- $V_0$ to $B$: 0 (by definition, $V_0$ has no neighbors in $T$; but what about $V_0$ to $V_2$? $V_0$ vertices are not adjacent to $a, b, c$. Can they be adjacent to $V_2$ vertices?)

$V_0$ to $V_2$: $x \in V_0, v \in V_2, \{x, v\}$ edge. Does this create a triangle? $v$ is adjacent to $a, b$. $x$ is adjacent to neither $a, b, c$. So $\{a, v, x\}$? Need $\{a, x\}$, no. $\{b, v, x\}$? Need $\{b, x\}$, no. So no triangle with book. ✓ But $\{x, v\}$ might create triangles with other vertices. If $x$ and $v$ have a common neighbor $z$ adjacent to both: $v$'s neighbors include $a, b$, and possibly $C_1$ and $V_0$ vertices. $x$'s neighbors include $V_0, A_1, B_1, C_1$ vertices (not $a, b, c$). Common neighbor could be in $C_1$ or $V_0$. If $z \in C_1$: $\{v, z\}$ and $\{x, z\}$ edges, and $\{x, v\}$ edge → triangle $\{x, v, z\}$. This triangle shares 0 vertices with book triangles. ✓ (as long as it doesn't create a butterfly with other triangles in $R$).

So $V_0$ to $V_2$ edges are allowed but might create triangles in the subgraph on $R \cup V_2$... this is getting really complex.

Let me try a different, cleaner approach. Let me try to prove the upper bound by induction.

**Induction hypothesis:** $\text{ex}(n, B) \leq \lfloor n^2/4 \rfloor + 1$ for all $n \geq 5$.

Base case $n = 5$: We verified $\text{ex}(5, B) = 7 = \lfloor 25/4 \rfloor + 1$. ✓

Inductive step: Assume $\text{ex}(k, B) \leq \lfloor k^2/4 \rfloor + 1$ for all $5 \leq k < n$. Show for $n$.

Let $G$ be butterfly-free on $n$ vertices with $m$ edges. If triangle-free, $m \leq \lfloor n^2/4 \rfloor$. ✓

If $G$ has a triangle $T = \{a, b, c\}$, I'll use the structure above.

Hmm, the induction is tricky because of the cross-edges. Let me try a different approach.

**Direct counting approach:**

Let $G$ be butterfly-free on $n$ vertices. For each vertex $v$, $G[N(v)]$ is a star or triangle.

Let $d(v)$ be the degree of $v$ and $e(v)$ be the number of edges in $G[N(v)]$ (i.e., the number of triangles through $v$... no, $e(v)$ is the number of edges among neighbors of $v$, which equals the number of triangles through $v$).

If $G[N(v)]$ is a star, $e(v) \leq d(v) - 1$.
If $G[N(v)]$ is a triangle, $e(v) = 3$ and $d(v) = 3$.

The number of triangles $t = \frac{1}{3} \sum_v e(v)$.

Now, $\sum_v d(v) = 2m$ and $\sum_v e(v) = 3t$.

By the Kruskal-Katona or Fisher inequality type arguments... hmm, not sure.

Let me try another approach. Let me use the following:

**Claim:** In a butterfly-free graph, the triangles form a "linear hypergraph" in some sense, and the number of edges is bounded.

Actually, let me try to use the following approach based on the structure.

**Structure theorem:** In a butterfly-free graph $G$, the vertex set can be partitioned into sets $V_1, \ldots, V_k, R$ where:
- Each $V_i$ is the vertex set of a triangle component (book $B_{p_i}$ or $K_4$).
- $R$ is the set of vertices not in any triangle.
- There are no edges between different $V_i$'s.
- The subgraph on $R$ is triangle-free (bipartite).
- Edges between $V_i$ and $R$ are restricted.

Wait, I haven't fully established this. Let me think about whether edges between different triangle components can exist.

If $C_1$ and $C_2$ are two triangle components with vertex sets $V_1, V_2$, and there's an edge $\{u, v\}$ with $u \in V_1, v \in V_2$: this edge doesn't create a triangle by itself. But if there's a vertex $w$ adjacent to both $u$ and $v$, then $\{u, v, w\}$ is a triangle. If $w \in V_1$, this triangle shares vertices with triangles in $C_1$ and $C_2$, potentially creating a butterfly.

If $w \in V_1$ and $w$ is in a triangle with $u$ in $C_1$, say triangle $\{u, w, x\}$: then $\{u, v, w\}$ and $\{u, w, x\}$ share edge $\{u, w\}$. ✓. But $\{u, v, w\}$ and any other triangle in $C_1$ not containing both $u$ and $w$: if $C_1$ is a book with edge $\{u, w\}$... actually, this depends on the structure.

This is really complex. Let me just try to verify the formula $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$ for $n = 5, 6, 7$ by checking that no graph with $\lfloor n^2/4 \rfloor + 2$ edges is butterfly-free.

For $n = 5$: $\lfloor 25/4 \rfloor + 2 = 8$. We showed every 8-edge graph on 5 vertices has a butterfly. ✓

For $n = 6$: $\lfloor 36/4 \rfloor + 2 = 11$. Need to show every 11-edge graph on 6 vertices has a butterfly.        — AI历史解题过程（thinking）
#   polymath_01834         — 题目ID

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
  <problem_id>polymath_01834</problem_id>
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

Let $n$ be a positive integer with $n \ge 5$. Define $m(n)$ to be the minimum number of edges such that any $n$-vertex simple graph with $m(n)$ edges contains two triangles that share exactly one vertex. Calculate the sum of $m(n)$ for $n = 5, 6, 7, 8, 9, 10$.

## Standard Solution

The original solution derives that for a given $n \ge 5$, the minimum number of edges required to guarantee two triangles sharing exactly one vertex is $m(n) = \lfloor \frac{n^2}{4} \rfloor + 2$.
We calculate $m(n)$ for $n \in \{5, 6, 7, 8, 9, 10\}$:
- $m(5) = \lfloor 25/4 \rfloor + 2 = 6 + 2 = 8$
- $m(6) = \lfloor 36/4 \rfloor + 2 = 9 + 2 = 11$
- $m(7) = \lfloor 49/4 \rfloor + 2 = 12 + 2 = 14$
- $m(8) = \lfloor 64/4 \rfloor + 2 = 16 + 2 = 18$
- $m(9) = \lfloor 81/4 \rfloor + 2 = 20 + 2 = 22$
- $m(10) = \lfloor 100/4 \rfloor + 2 = 25 + 2 = 27$
The sum is $8 + 11 + 14 + 18 + 22 + 27 = 100$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We need to find $m(n)$, the minimum number of edges such that any $n$-vertex simple graph with $m(n)$ edges contains two triangles that share exactly one vertex.

Two triangles sharing exactly one vertex means a "bowtie" or "butterfly" graph - two triangles with a common vertex but no common edge.

Let me think about this. First, what's the extremal number for avoiding two triangles sharing exactly one vertex?

Let me think about what graphs avoid this configuration. We need to find the maximum number of edges in an $n$-vertex graph that does NOT contain two triangles sharing exactly one vertex.

Two triangles share exactly one vertex = there exist vertices $a, b, c, d$ (with $a$ being the shared vertex) such that $abc$ and $abd$ are both triangles (sharing edge $ab$... wait no).

Wait, let me reconsider. Two triangles sharing exactly one vertex. Triangle 1 = $\{a, b, c\}$, Triangle 2 = $\{a, d, e\}$ where the only common vertex is $a$. So $b, c, d, e$ are all distinct, and the shared vertex is $a$.

Actually, two triangles can share:
- 0 vertices (disjoint)
- 1 vertex (bowtie/butterfly)
- 1 edge (2 vertices shared) - this is a "diamond" or $K_4$ minus an edge

We want to avoid the case of sharing exactly 1 vertex.

So we need: the maximum number of edges in a graph where no two triangles share exactly one vertex.

Let me think about the structure. If two triangles share exactly one vertex $v$, then $v$ is in both triangles. So we need: for every vertex $v$, the triangles containing $v$ must pairwise share at least an edge (i.e., share at least 2 vertices).

Actually, let's think about it differently. Consider the set of all triangles in the graph. We need that no two triangles share exactly one vertex. So any two triangles either share 0 vertices, or share an edge (2 vertices), or are the same triangle.

If two triangles share an edge, they form a $K_4$ minus an edge (diamond). If three triangles all share a common edge, that's $K_4$.

Let me think about the structure of triangle-sharing. Consider the "triangle graph" where vertices are triangles and edges connect triangles sharing an edge. Actually, let me think about which configurations are allowed.

Let me think about this more carefully. Consider a vertex $v$. The triangles through $v$ correspond to edges in $G[N(v)]$ (the subgraph induced by neighbors of $v$). Two triangles through $v$ share exactly one vertex ($v$) iff the corresponding edges in $G[N(v)]$ are disjoint (share no endpoint). Two triangles through $v$ share an edge iff the corresponding edges in $G[N(v)]$ share an endpoint.

So the condition "no two triangles share exactly one vertex" means: for every vertex $v$, the graph $G[N(v)]$ has the property that every two edges share an endpoint. This means $G[N(v)]$ is a star (all edges share a common vertex) or a triangle (three edges, each pair shares an endpoint).

Wait, a graph where every two edges share an endpoint is either a star or a triangle ($K_3$). This is a well-known fact.

So for every vertex $v$, $G[N(v)]$ is either a star or a triangle.

If $G[N(v)]$ is a star with center $u$, then all triangles through $v$ use the edge $vu$... no wait. The triangles through $v$ correspond to edges in $G[N(v)]$. If $G[N(v)]$ is a star centered at $u \in N(v)$, then all edges in $G[N(v)]$ are of the form $\{u, w\}$ for $w \in N(v)$. So all triangles through $v$ are $\{v, u, w\}$ for various $w$. These all share the edge $\{v, u\}$.

If $G[N(v)]$ is a triangle on $\{a, b, c\}$, then the triangles through $v$ are $\{v, a, b\}, \{v, b, c\}, \{v, a, c\}$. These are the triangles of $K_4$ on $\{v, a, b, c\}$. Any two share an edge.

So the condition is: for every vertex $v$, $G[N(v)]$ is a star or a triangle.

Now I need to find the maximum number of edges in such a graph.

Let me think about what graphs satisfy this. 

Case 1: $G[N(v)]$ is a star for all $v$. This means every vertex's neighborhood forms a star. 

Case 2: Some vertices have triangle neighborhoods.

Let me think about specific constructions.

**Construction 1: Complete bipartite graph $K_{a,b}$.** This has no triangles at all, so the condition is vacuously satisfied. Edges = $ab$. With $a + b = n$, max is $\lfloor n^2/4 \rfloor$.

**Construction 2: A graph where we take $K_{a,b}$ and add edges within one part.** Say we take $K_{a,b}$ and add some edges within part $A$ (size $a$). If we add an edge $\{a_1, a_2\}$ within $A$, then for any $b \in B$, we get a triangle $\{a_1, a_2, b\}$. Now consider vertex $b \in B$. Its neighbors are all of $A$. $G[N(b)] = G[A]$. For the condition to hold, $G[A]$ must be a star or triangle. So the edges within $A$ must form a star or triangle.

If $G[A]$ is a star centered at $a_1$ with $k$ edges, then we have $k$ triangles, all through $a_1$ and some $a_i$, sharing the edge $\{a_1, a_i\}$... wait, the triangles are $\{a_1, a_i, b\}$ for each $b \in B$ and each edge $\{a_1, a_i\}$ in the star.

Now check vertex $a_1$: its neighbors include all of $B$ and $\{a_2, \ldots, a_{k+1}\}$ (the leaves of the star). $G[N(a_1)]$ includes the bipartite edges between $B$ and $\{a_2, \ldots\}$, plus... wait, are there edges between $B$ and the $a_i$'s? Yes, since it's $K_{a,b}$, every $a_i$ is connected to every $b_j$. So $G[N(a_1)]$ is a complete bipartite graph $K_{k, b}$ (between $\{a_2, \ldots, a_{k+1}\}$ and $B$). For this to be a star or triangle, we need $K_{k,b}$ to be a star or triangle. $K_{k,b}$ is a star iff $k=1$ or $b=1$. It's a triangle iff $k=2, b=1$ or $k=1, b=2$ (but $K_{1,2}$ is a star, and $K_{2,1}$ is a star; $K_{2,2}$ is a 4-cycle, not a star or triangle). Actually $K_{1,b}$ is a star for any $b$, and $K_{a,1}$ is a star for any $a$. $K_{2,2}$ is a 4-cycle. So we need $k \leq 1$ or $b \leq 1$.

Hmm, this is getting complicated. Let me think differently.

If $b \geq 2$ and $k \geq 2$, then $G[N(a_1)] = K_{k,b}$ with $k, b \geq 2$ contains a 4-cycle, which has two disjoint edges, violating the condition. So if we add a star with $k \geq 2$ edges within $A$, we need $b \leq 1$, which means $B$ has at most 1 vertex, giving very few edges.

So with $b \geq 2$, we can add at most 1 edge within $A$ (star with 1 edge). Let's check: if we add one edge $\{a_1, a_2\}$ within $A$, then:
- For $b \in B$: $G[N(b)] = G[A]$ which has one edge, which is a star (trivially). ✓
- For $a_1$: $N(a_1) = B \cup \{a_2\}$. $G[N(a_1)]$: edges between $B$ and $a_2$ (all of them, since complete bipartite), and no edges within $B$. So $G[N(a_1)] = K_{1, b}$ (star centered at $a_2$). ✓ (as long as this is a star, which it is for any $b$)
- For $a_2$: similarly, $G[N(a_2)] = K_{1, b}$ (star centered at $a_1$). ✓
- For $a_i$ with $i \geq 3$: $N(a_i) = B$. $G[N(a_i)] = G[B]$ which has no edges. ✓

So this works! We get $ab + 1$ edges with $a + b = n$, $a, b \geq 2$.

Can we do better? Can we add edges within both parts?

If we add an edge within $A$ and an edge within $B$, say $\{a_1, a_2\}$ and $\{b_1, b_2\}$. Then we have triangles $\{a_1, a_2, b_j\}$ for all $b_j \in B$ and $\{a_i, b_1, b_2\}$ for all $a_i \in A$. 

Consider vertex $a_1$: triangles through $a_1$ include $\{a_1, a_2, b_j\}$ for all $j$ and $\{a_1, b_1, b_2\}$. Do $\{a_1, a_2, b_3\}$ and $\{a_1, b_1, b_2\}$ share exactly one vertex ($a_1$)? Yes, if $a_2 \neq b_1, b_2$ and $b_3 \neq b_1, b_2$ (assuming $|B| \geq 3$). So this would violate the condition if $|B| \geq 3$.

If $|B| = 2$, then $B = \{b_1, b_2\}$. Triangles through $a_1$: $\{a_1, a_2, b_1\}$, $\{a_1, a_2, b_2\}$, $\{a_1, b_1, b_2\}$. Do $\{a_1, a_2, b_1\}$ and $\{a_1, b_1, b_2\}$ share vertices $a_1$ and $b_1$ — that's 2 vertices, so they share an edge. ✓. Do $\{a_1, a_2, b_2\}$ and $\{a_1, b_1, b_2\}$ share $a_1$ and $b_2$. ✓. Do $\{a_1, a_2, b_1\}$ and $\{a_1, a_2, b_2\}$ share $a_1$ and $a_2$. ✓. So all pairs share an edge. 

But we need to check all vertices. Consider $b_1$: $N(b_1) = A \cup \{b_2\}$. $G[N(b_1)]$: edges within $A$ (just $\{a_1, a_2\}$) and edges between $A$ and $b_2$ (all of them). So $G[N(b_1)]$ has edges $\{a_1, a_2\}$ and $\{a_i, b_2\}$ for all $a_i \in A$. Is this a star or triangle? The edge $\{a_1, a_2\}$ and edge $\{a_3, b_2\}$ (for $a_3 \neq a_1, a_2$, assuming $|A| \geq 3$) are disjoint. So if $|A| \geq 3$, this fails.

If $|A| = 2$, $A = \{a_1, a_2\}$. Then $G[N(b_1)]$ has edges $\{a_1, a_2\}$, $\{a_1, b_2\}$, $\{a_2, b_2\}$. That's a triangle on $\{a_1, a_2, b_2\}$. ✓

So with $|A| = 2, |B| = 2$, $n = 4$, we get $K_4$ which has 6 edges. But we need $n \geq 5$.

OK so for $n \geq 5$, adding edges within both parts seems hard. Let me think about other constructions.

**Construction 3: Take a clique $K_k$ and make the rest independent, with all edges between them.** Actually, let me think about the "friendship graph" or other structures.

Let me reconsider. The condition is that for every vertex $v$, $G[N(v)]$ is a star or triangle.

Let me think about what happens with a clique $K_k$. For a vertex $v$ in $K_k$, $G[N(v)] = K_{k-1}$. This is a star iff $k-1 \leq 2$ (i.e., $k \leq 3$), and a triangle iff $k-1 = 3$ (i.e., $k = 4$). For $k \geq 5$, $K_{k-1}$ is neither a star nor a triangle. So the largest clique we can have is $K_4$.

$K_4$ has 6 edges and 4 vertices. For $n = 4$, this gives 6 edges with no two triangles sharing exactly one vertex (in $K_4$, any two triangles share an edge).

For $n \geq 5$, we can take $K_4$ plus $n-4$ isolated vertices, giving 6 edges. But we can do better.

**Construction 4: $K_4$ plus vertices connected to some of the $K_4$.** Let's say we have $K_4$ on $\{1,2,3,4\}$ and add vertex $5$ connected to some subset.

If vertex 5 is connected to vertices $\{1, 2\}$ of the $K_4$, then we get a triangle $\{1, 2, 5\}$. Now check:
- Vertex 1: $N(1) = \{2, 3, 4, 5\}$. $G[N(1)]$: edges $\{2,3\}, \{2,4\}, \{3,4\}$ (from $K_4$) and $\{2, 5\}$ (since 5 is connected to 2). Is this a star or triangle? We have edges $\{2,3\}, \{2,4\}, \{3,4\}, \{2,5\}$. The edge $\{3,4\}$ and $\{2,5\}$ are disjoint. So this is NOT a star or triangle. ✗

So connecting vertex 5 to 2 vertices of $K_4$ that are adjacent doesn't work (it always fails since all pairs in $K_4$ are adjacent).

What if vertex 5 is connected to just 1 vertex, say vertex 1? Then no new triangles. Check vertex 1: $N(1) = \{2,3,4,5\}$, $G[N(1)] = K_3$ on $\{2,3,4\}$ plus isolated vertex 5. That's a triangle plus an isolated vertex. Is this a star or triangle? No, it's a triangle plus an isolated vertex, which is neither. ✗

Hmm wait, the condition is that $G[N(v)]$ is a star or triangle. A triangle plus an isolated vertex is not a star (it has 3 edges forming a cycle) and not a triangle (it has 4 vertices). So this fails.

What if vertex 5 is connected to all 4 vertices of $K_4$? Then $N(5) = \{1,2,3,4\}$, $G[N(5)] = K_4$, which is not a star or triangle. ✗

What if vertex 5 is connected to 3 vertices of $K_4$, say $\{1,2,3\}$? Then $N(5) = \{1,2,3\}$, $G[N(5)] = K_3$ (triangle). ✓ for vertex 5. But check vertex 1: $N(1) = \{2,3,4,5\}$. $G[N(1)]$: edges among $\{2,3,4\}$ form $K_3$, plus edges between 5 and $\{2,3\}$ (since 5 is connected to 2 and 3). So edges: $\{2,3\}, \{2,4\}, \{3,4\}, \{2,5\}, \{3,5\}$. Is this a star or triangle? Edge $\{2,4\}$ and $\{3,5\}$ are disjoint. ✗

So it seems hard to add vertices to $K_4$.

Let me reconsider. Maybe the optimal construction is the complete bipartite graph plus one edge, or something else.

**Let me reconsider the bipartite + one edge construction.** Take $K_{a,b}$ with $a + b = n$ and add one edge within the larger part. Total edges: $ab + 1$. To maximize, take $a = \lfloor n/2 \rfloor, b = \lceil n/2 \rceil$, giving $\lfloor n^2/4 \rfloor + 1$.

But wait, can we do better with other constructions?

**Construction 5: Take a star $K_{1,n-1}$.** This has $n-1$ edges and no triangles. But $\lfloor n^2/4 \rfloor + 1$ is much larger for $n \geq 5$.

**Construction 6: Complete bipartite $K_{a,b}$ with $a + b = n$.** Edges = $ab \leq \lfloor n^2/4 \rfloor$. No triangles. This is less than $\lfloor n^2/4 \rfloor + 1$.

So the bipartite + one edge gives $\lfloor n^2/4 \rfloor + 1$.

Can we do better? Let me think about whether we can add more edges.

What about taking $K_{a,b}$ and adding a star with 2 edges within part $A$? We showed this requires $b \leq 1$. If $b = 1$, we have $a = n-1$ and the graph is $K_{n-1, 1}$ plus a star within the $n-1$ part. $K_{n-1,1}$ has $n-1$ edges. Adding 2 edges within the large part gives $n+1$ edges total. For $n \geq 5$, $\lfloor n^2/4 \rfloor + 1 \geq 7 > 6 = n+1$ for $n=5$. So this is worse.

What about adding a triangle within part $A$? If $G[A]$ is a triangle on $\{a_1, a_2, a_3\}$, then for vertex $b \in B$, $G[N(b)] = G[A]$ which is a triangle plus possibly isolated vertices. Wait, $G[A]$ is a triangle on 3 vertices plus isolated vertices for the rest of $A$. Is a triangle plus isolated vertices a "star or triangle"? No, it has more than 3 vertices. So this fails unless $|A| = 3$.

If $|A| = 3$ with $G[A] = K_3$ and $|B| = n - 3$. Check vertex $a_1$: $N(a_1) = \{a_2, a_3\} \cup B$. $G[N(a_1)]$: edge $\{a_2, a_3\}$ (from the triangle) and edges between $\{a_2, a_3\}$ and $B$ (all of them, since complete bipartite). So $G[N(a_1)]$ has edges $\{a_2, a_3\}$ and $\{a_2, b_j\}, \{a_3, b_j\}$ for all $b_j \in B$. Is this a star or triangle? If $|B| \geq 2$, edges $\{a_2, b_1\}$ and $\{a_3, b_2\}$ are disjoint. ✗

So this fails for $|B| \geq 2$, i.e., $n \geq 5$.

If $|B| = 1$, $n = 4$, we get $K_4$ again.

If $|B| = 0$, $n = 3$, just $K_3$.

So for $n \geq 5$, the triangle-within-part construction doesn't work with complete bipartite.

**What about non-complete bipartite constructions?** Let me think more broadly.

Let me consider the structure more carefully. The condition is: for every vertex $v$, $G[N(v)]$ is a star or triangle.

Let me think about graphs where every neighborhood is a star. This is related to the concept of "locally star" graphs.

Actually, let me think about this problem from the perspective of known results. The problem asks for the extremal number for the "butterfly" graph (two triangles sharing a vertex). 

The butterfly graph $B$ is two triangles sharing exactly one vertex. The extremal number $\text{ex}(n, B)$ is the maximum number of edges in an $n$-vertex graph with no butterfly.

For the butterfly graph, I recall that the extremal number is $\lfloor n^2/4 \rfloor + 1$ for $n \geq 5$. Wait, let me think more carefully.

Actually, I think the answer might be related to the following. The Turán-type problem for the butterfly (also called the "bowtie") graph.

Let me think about it from the construction side. We have the construction $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ plus one edge, giving $\lfloor n^2/4 \rfloor + 1$ edges. 

Can we do better? Let me think about other constructions.

**Construction 7: Two cliques sharing a vertex.** Take $K_{k}$ and $K_{l}$ sharing exactly one vertex, with $k + l - 1 = n$. But we showed $K_k$ requires $k \leq 4$. So take $K_4$ and $K_4$ sharing a vertex: $n = 7$, edges = $6 + 6 = 12$. Compare with $\lfloor 49/4 \rfloor + 1 = 12 + 1 = 13$. So 12 < 13, the bipartite+1 construction is better.

Take $K_4$ and $K_3$ sharing a vertex: $n = 6$, edges = $6 + 3 = 9$. Compare with $\lfloor 36/4 \rfloor + 1 = 9 + 1 = 10$. Again worse.

**Construction 8: A graph formed by taking a complete bipartite graph and adding a matching within one part.** We showed adding 1 edge works. Adding 2 edges (a matching) within part $A$: for vertex $b \in B$, $G[N(b)] = G[A]$ which has 2 disjoint edges. This is not a star or triangle. ✗ (unless $|B| = 0$).

So we can't add 2 disjoint edges within a part if $|B| \geq 1$.

What about adding 2 edges that share a vertex (a star of 2 edges) within part $A$? We showed this requires $|B| \leq 1$.

So the bipartite + 1 edge construction seems optimal among bipartite-based constructions.

**Can we beat $\lfloor n^2/4 \rfloor + 1$ with a non-bipartite construction?**

Let me think about the problem differently. Let me consider the structure of triangle-free parts.

Actually, let me think about this more carefully using the characterization.

For every vertex $v$, $G[N(v)]$ is a star or triangle.

Let me split vertices into two types:
- Type S: $G[N(v)]$ is a star
- Type T: $G[N(v)]$ is a triangle

If $v$ is Type T, then $|N(v)| = 3$ and $G[N(v)] = K_3$, so $v$ together with its neighbors forms a $K_4$.

If $v$ is Type S, then $G[N(v)]$ is a star. Let $d(v) = |N(v)|$. If $d(v) \leq 1$, the star is trivial (0 or 1 edge). If $d(v) = 2$, the star has at most 1 edge. If $d(v) \geq 2$, the star has a center $u \in N(v)$ and all edges in $G[N(v)]$ go through $u$.

Let me think about the maximum number of edges. 

Let me consider the case where all vertices are Type S (no vertex has a triangle neighborhood). Then for every $v$, $G[N(v)]$ is a star.

If $G$ is triangle-free, then every $G[N(v)]$ is empty (a star with 0 edges), so the condition is satisfied. The maximum triangle-free graph is $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ with $\lfloor n^2/4 \rfloor$ edges.

If $G$ has some triangles, then some $G[N(v)]$ is a non-trivial star. 

Let me think about the structure when there are triangles. Suppose $v$ is a vertex with $G[N(v)]$ being a star centered at $u$ with $k \geq 1$ edges. Then the triangles through $v$ are $\{v, u, w_i\}$ for $i = 1, \ldots, k$ where $w_1, \ldots, w_k$ are the leaves. All these triangles share the edge $\{v, u\}$.

Now, consider any other triangle in the graph not through $v$. It must not share exactly one vertex with any triangle through $v$.

This is getting complex. Let me try to think about upper bounds.

**Upper bound approach:** Let $G$ be a graph on $n$ vertices with no butterfly (two triangles sharing exactly one vertex). We want to show $e(G) \leq \lfloor n^2/4 \rfloor + 1$ (or find the correct bound).

Let me think about the triangles in $G$. Consider the "triangle edge-sharing" structure. Define an equivalence relation on triangles: two triangles are related if they share an edge. The transitive closure gives equivalence classes. Within each class, any two triangles share an edge (I need to verify this).

Actually, this isn't quite right. If triangle $T_1$ shares an edge with $T_2$, and $T_2$ shares an edge with $T_3$, do $T_1$ and $T_3$ share an edge? Not necessarily. Consider $K_4$: triangles $\{1,2,3\}$, $\{1,2,4\}$, $\{1,3,4\}$. $\{1,2,3\}$ and $\{1,2,4\}$ share edge $\{1,2\}$. $\{1,2,4\}$ and $\{1,3,4\}$ share edge $\{1,4\}$. $\{1,2,3\}$ and $\{1,3,4\}$ share edge $\{1,3\}$. So in $K_4$, all pairs share an edge. 

But in general? Consider a "book" of triangles sharing a common edge $\{u,v\}$: triangles $\{u,v,w_1\}, \{u,v,w_2\}, \ldots$. Any two share the edge $\{u,v\}$. Now add a triangle $\{u, w_1, w_2\}$. This shares edge $\{u, w_1\}$ with $\{u,v,w_1\}$ and edge $\{u, w_2\}$ with $\{u,v,w_2\}$. But does $\{u, w_1, w_2\}$ share an edge with $\{u, v, w_3\}$? They share only vertex $u$. So this would be a butterfly! Unless $w_3$ doesn't exist, i.e., there are only 2 triangles in the book.

So if we have a book with edge $\{u,v\}$ and $k$ triangles $\{u,v,w_i\}$, and we also have triangle $\{u, w_i, w_j\}$ for some $i \neq j$, then we need that there's no $w_l$ with $l \neq i, j$ (otherwise $\{u, w_i, w_j\}$ and $\{u, v, w_l\}$ share only $u$). So the book has at most 2 pages if there's an extra triangle.

This is getting complicated. Let me try a different approach and think about specific small cases, then look for a pattern.

For $n = 5$: We need $m(5)$. The maximum butterfly-free graph on 5 vertices.

$K_{2,3}$ has 6 edges, no triangles. $K_{2,3}$ + 1 edge within the part of size 3: 7 edges. Let me verify this is butterfly-free.

$K_{2,3}$ on parts $A = \{a_1, a_2\}$, $B = \{b_1, b_2, b_3\}$. Add edge $\{b_1, b_2\}$. Triangles: $\{a_1, b_1, b_2\}$ and $\{a_2, b_1, b_2\}$. These share edge $\{b_1, b_2\}$. No other triangles. So no butterfly. ✓ 7 edges.

Can we get 8 edges on 5 vertices without a butterfly? $\binom{5}{2} = 10$, so 8 edges means removing 2 edges from $K_5$.

$K_5$ has 10 triangles. Removing 2 edges... Let me think. $K_5$ minus 2 edges. If the 2 removed edges are disjoint, say $\{1,2\}$ and $\{3,4\}$, the remaining graph has 8 edges. Triangles: all triples except those containing $\{1,2\}$ or $\{3,4\}$. Triangles containing $\{1,2\}$: $\{1,2,3\}, \{1,2,4\}, \{1,2,5\}$ — removed. Triangles containing $\{3,4\}$: $\{1,3,4\}, \{2,3,4\}, \{3,4,5\}$ — removed. Remaining triangles: $\{1,3,5\}, \{1,4,5\}, \{2,3,5\}, \{2,4,5\}$. That's 4 triangles. Do any two share exactly one vertex? $\{1,3,5\}$ and $\{2,4,5\}$ share only vertex 5. Butterfly! ✗

If the 2 removed edges share a vertex, say $\{1,2\}$ and $\{1,3\}$. Remaining triangles: those not containing $\{1,2\}$ or $\{1,3\}$. Triangles of $K_5$: $\{1,2,3\}, \{1,2,4\}, \{1,2,5\}, \{1,3,4\}, \{1,3,5\}, \{1,4,5\}, \{2,3,4\}, \{2,3,5\}, \{2,4,5\}, \{3,4,5\}$. Removed: $\{1,2,3\}, \{1,2,4\}, \{1,2,5\}, \{1,3,4\}, \{1,3,5\}$. Remaining: $\{1,4,5\}, \{2,3,4\}, \{2,3,5\}, \{2,4,5\}, \{3,4,5\}$. Do any two share exactly one vertex? $\{1,4,5\}$ and $\{2,3,4\}$: share vertex 4 only. Wait, $\{1,4,5\}$ has vertices $1,4,5$ and $\{2,3,4\}$ has $2,3,4$. Common: $\{4\}$. Yes, exactly one vertex. Butterfly! ✗

So 8 edges on 5 vertices always contains a butterfly. Thus $m(5) = 8$? Wait, we need to check: does every 5-vertex graph with 8 edges contain a butterfly? We checked two cases of removing 2 edges from $K_5$ and both had butterflies. But are there other 8-edge graphs not of this form? Every 8-edge graph on 5 vertices is $K_5$ minus 2 edges (since $\binom{5}{2} = 10$). The two removed edges either share a vertex or are disjoint. We checked both cases. So yes, every 8-edge graph on 5 vertices has a butterfly.

But wait, we need $m(5)$ = minimum edges such that ANY graph with that many edges contains a butterfly. So $m(5) = 8$ if every 8-edge graph has a butterfly AND there exists a 7-edge graph without a butterfly. We showed $K_{2,3}$ + 1 edge = 7 edges, no butterfly. So $m(5) = 8$.

Hmm wait, but $\lfloor 25/4 \rfloor + 1 = 6 + 1 = 7$. And we showed 7 edges can be butterfly-free, but 8 edges always has a butterfly. So $m(5) = 8 = \lfloor 25/4 \rfloor + 2$?

Wait, let me recheck. $\lfloor 25/4 \rfloor = 6$. So $\lfloor n^2/4 \rfloor + 1 = 7$. But we need 8 edges to force a butterfly. So $m(5) = 8$.

Hmm, that doesn't match $\lfloor n^2/4 \rfloor + 1$. Let me recheck whether there's a 7-edge graph on 5 vertices without a butterfly. We have $K_{2,3} + \{b_1,b_2\}$ with 7 edges and no butterfly. So the maximum butterfly-free graph has at least 7 edges. And we showed 8 edges always has a butterfly. So $\text{ex}(5, B) = 7$ and $m(5) = 8$.

But $\lfloor 25/4 \rfloor + 1 = 7 = \text{ex}(5, B)$. So $m(5) = \text{ex}(5, B) + 1 = 8$.

OK so $m(n) = \text{ex}(n, B) + 1$ where $B$ is the butterfly. And we need to find $\text{ex}(n, B)$ for $n = 5, \ldots, 10$.

For $n = 5$: $\text{ex}(5, B) = 7$, so $m(5) = 8$.

Now let me check $n = 6$. $\lfloor 36/4 \rfloor + 1 = 9 + 1 = 10$. Is $\text{ex}(6, B) = 10$?

Construction: $K_{3,3}$ + 1 edge = 10 edges. Let me verify no butterfly. Parts $A = \{a_1, a_2, a_3\}$, $B = \{b_1, b_2, b_3\}$, add edge $\{a_1, a_2\}$. Triangles: $\{a_1, a_2, b_1\}, \{a_1, a_2, b_2\}, \{a_1, a_2, b_3\}$. All share edge $\{a_1, a_2\}$. No butterfly. ✓

Can we get 11 edges on 6 vertices without a butterfly? $\binom{6}{2} = 15$, so 11 edges means removing 4 edges from $K_6$.

Hmm, this is harder to check directly. Let me think about whether $\text{ex}(6, B) = 10$ or could be higher.

Actually, let me think about another construction for $n = 6$. Take $K_4$ on $\{1,2,3,4\}$ and connect vertices 5, 6 to some vertices.

We showed that adding a vertex connected to 1 vertex of $K_4$ fails (neighborhood of that vertex becomes triangle + isolated vertex). Adding connected to 2 adjacent vertices of $K_4$ fails. Adding connected to 3 vertices of $K_4$ fails. Adding connected to all 4 fails.

What if we don't use $K_4$? Let me think about other structures.

**Construction: $K_{3,3}$ + 1 edge = 10 edges, no butterfly.** Can we do 11?

Let me try $K_{3,3}$ + 2 edges within one part. Say add $\{a_1, a_2\}$ and $\{a_1, a_3\}$ within $A$. Then for $b \in B$, $G[N(b)] = G[A]$ which has edges $\{a_1, a_2\}, \{a_1, a_3\}$ — a star. ✓ for $b$. For $a_1$: $N(a_1) = \{a_2, a_3\} \cup B$. $G[N(a_1)]$: edges between $\{a_2, a_3\}$ and $B$ (all 6 edges) and edge $\{a_2, a_3\}$? Wait, is $\{a_2, a_3\}$ an edge? We only added $\{a_1, a_2\}$ and $\{a_1, a_3\}$, not $\{a_2, a_3\}$. So $G[N(a_1)]$ has edges $\{a_2, b_j\}$ and $\{a_3, b_j\}$ for $j = 1,2,3$. That's $K_{2,3}$, which has disjoint edges (e.g., $\{a_2, b_1\}$ and $\{a_3, b_2\}$). Not a star or triangle. ✗

So adding 2 edges sharing a vertex within $A$ fails when $|B| \geq 2$.

What about adding 1 edge within $A$ and 1 edge within $B$? Add $\{a_1, a_2\}$ and $\{b_1, b_2\}$. Triangles: $\{a_1, a_2, b_j\}$ for $j = 1,2,3$ and $\{a_i, b_1, b_2\}$ for $i = 1,2,3$. Consider $\{a_1, a_2, b_3\}$ and $\{a_3, b_1, b_2\}$: share no vertex. OK. Consider $\{a_1, a_2, b_1\}$ and $\{a_3, b_1, b_2\}$: share vertex $b_1$ only. Butterfly! ✗

So that doesn't work either.

What about a completely different construction? Let me think...

**Construction: Take $C_5$ (5-cycle) and add a universal vertex.** $C_5$ has 5 edges, universal vertex adds 5 edges, total 10 edges on 6 vertices. The universal vertex $v$ has $N(v) = C_5$. $G[N(v)] = C_5$ which is not a star or triangle. So there exist two triangles through $v$ sharing only $v$. Indeed, $\{v, 1, 2\}$ and $\{v, 3, 4\}$ share only $v$. Butterfly. ✗

**Construction: Take $K_{2,4}$ + 1 edge.** $K_{2,4}$ has 8 edges, + 1 = 9. Less than 10.

**Construction: Take $K_{3,3}$ + 1 edge = 10.** This seems to be the best for $n = 6$.

Let me try to see if 11 edges on 6 vertices must contain a butterfly.

Actually, let me think about this more carefully with the structural characterization.

For a butterfly-free graph, every neighborhood is a star or triangle. Let me count the maximum edges.

Let $G$ be butterfly-free on $n$ vertices. For each vertex $v$, $G[N(v)]$ is a star or triangle.

Let me use a different approach. Let me think about the number of triangles.

If $G$ has no triangles, then $e(G) \leq \lfloor n^2/4 \rfloor$ (Turán/Mantel).

If $G$ has triangles, consider the structure of triangles. In a butterfly-free graph, the triangles can be organized as follows: consider the graph $H$ whose vertices are the triangles of $G$, with two triangles adjacent in $H$ iff they share an edge. The condition is that no two triangles share exactly one vertex. 

Actually, let me think about it as: the set of triangles can be partitioned into "clusters" where within each cluster, all triangles share a common edge, and between clusters, triangles are vertex-disjoint.

Wait, is that true? In $K_4$, the 4 triangles don't all share a common edge. $\{1,2,3\}, \{1,2,4\}, \{1,3,4\}, \{2,3,4\}$. No single edge is in all 4. But any two share an edge. So the "clusters" can be more complex.

Let me think about $K_4$ as a special cluster. In $K_4$, every pair of triangles shares an edge, so no butterfly. $K_4$ has 4 vertices and 6 edges.

For a "book" $B_k$ (k triangles sharing a common edge), we have $k + 2$ vertices and $2k + 1$ edges.

Now, in a butterfly-free graph, can we have both a $K_4$ and a separate book? They need to be vertex-disjoint (otherwise two triangles from different clusters might share exactly one vertex).

Actually, they don't need to be fully vertex-disjoint. Two triangles from different "edge-sharing clusters" must share 0 vertices (not exactly 1). So if triangle $T_1$ is in one cluster and $T_2$ in another, they share 0 vertices.

Hmm, but this is about pairs of triangles, not clusters. Let me think again.

The condition is: for any two triangles, they share 0 or 2+ vertices (not exactly 1).

So if I have a set of triangles where any two share an edge (2+ vertices), that's one "clique" of triangles. And different cliques must be vertex-disjoint.

Wait, not exactly. Two triangles from different cliques must share 0 vertices. But a triangle could potentially be in the "intersection" — no, let me think about this differently.

Let me define a graph $T$ on the triangles of $G$: two triangles are adjacent in $T$ if they share an edge. The butterfly-free condition means: if two triangles are NOT adjacent in $T$ (don't share an edge), they must share 0 vertices (not 1).

So in $T$, non-adjacent triangles are vertex-disjoint. This means: if triangle $T_1$ and $T_2$ share a vertex but not an edge, that's forbidden.

Now, consider the connected components of $T$. Within a component, triangles are connected by edge-sharing. Between components, triangles share no vertices. So each component of $T$ involves a disjoint set of vertices of $G$.

Within a component, what structures are possible? We need that any two triangles in the same component that don't share an edge still share 0 vertices. But they're in the same component, so there's a path of edge-sharing between them. 

Hmm, let me think about small components. A component with 1 triangle: just a triangle, 3 vertices, 3 edges.

A component with 2 triangles sharing an edge: a diamond ($K_4 - e$), 4 vertices, 5 edges.

A component with 3 triangles: 
- All sharing a common edge: book $B_3$, 5 vertices, 7 edges.
- $K_4$: 4 triangles, 4 vertices, 6 edges. Wait, $K_4$ has 4 triangles, not 3.
- Three triangles where $T_1, T_2$ share edge $e_1$, $T_2, T_3$ share edge $e_2$, $T_1, T_3$ share edge $e_3$ or share 0 vertices.

If $T_1, T_3$ share 0 vertices: $T_1 = \{a,b,c\}, T_2 = \{a,b,d\}, T_3 = \{d,e,f\}$ (shares edge $\{a,b\}$ with... no, $T_2$ and $T_3$ share edge, so $T_3$ shares an edge with $T_2 = \{a,b,d\}$. If $T_3 = \{d, e, f\}$, it shares only vertex $d$ with $T_2$, not an edge. So $T_3$ must share an edge with $T_2$. If $T_2 = \{a,b,d\}$, then $T_3$ shares an edge, say $\{a,d\}$: $T_3 = \{a,d,e\}$. Now $T_1 = \{a,b,c\}$ and $T_3 = \{a,d,e\}$ share only vertex $a$. Butterfly! ✗

So we can't have a path of length 2 in $T$ where the endpoints share exactly 1 vertex. The endpoints must share 0 or 2+ vertices.

If $T_1 = \{a,b,c\}, T_2 = \{a,b,d\}, T_3 = \{a,b,e\}$: all share edge $\{a,b\}$. $T_1, T_3$ share edge $\{a,b\}$. ✓ This is a book.

If $T_1 = \{a,b,c\}, T_2 = \{a,b,d\}, T_3 = \{a,c,d\}$: $T_1, T_2$ share $\{a,b\}$. $T_2, T_3$ share $\{a,d\}$. $T_1, T_3$ share $\{a,c\}$. All pairs share an edge. This is part of $K_4$.

If $T_1 = \{a,b,c\}, T_2 = \{a,b,d\}, T_3 = \{b,c,d\}$: $T_1, T_2$ share $\{a,b\}$. $T_2, T_3$ share $\{b,d\}$. $T_1, T_3$ share $\{b,c\}$. All share an edge. Part of $K_4$.

So for 3 triangles in a component, either it's a book (all share a common edge) or part of $K_4$.

For $K_4$ (4 triangles on 4 vertices): all pairs share an edge. ✓

Can we have a component with more than 4 triangles? A book $B_k$ has $k$ triangles, all sharing a common edge, on $k+2$ vertices. That's fine.

Can we have a component that's not a book and not $K_4$? Suppose we have 5 triangles. If they all share a common edge, it's $B_5$. Otherwise, consider $K_4$ plus an extra triangle. $K_4$ on $\{1,2,3,4\}$ has 4 triangles. Add a 5th triangle sharing an edge with one of them, say sharing $\{1,2\}$: the 5th triangle is $\{1,2,5\}$. Now $\{1,2,5\}$ and $\{1,3,4\}$ share only vertex 1. Butterfly! ✗

So we can't extend $K_4$ with more triangles. The only components with more than 4 triangles are books.

What about a component that's a book plus some extra triangles? Book $B_k$ with common edge $\{u,v\}$ and triangles $\{u,v,w_i\}$ for $i = 1, \ldots, k$. Add a triangle $\{u, w_1, w_2\}$. This shares edge $\{u, w_1\}$ with $\{u,v,w_1\}$ and edge $\{u, w_2\}$ with $\{u,v,w_2\}$. But $\{u, w_1, w_2\}$ and $\{u, v, w_3\}$ (for $k \geq 3$) share only vertex $u$. Butterfly! ✗

So if $k \geq 3$, we can't add extra triangles to a book. If $k = 2$, book $B_2$ has triangles $\{u,v,w_1\}, \{u,v,w_2\}$ on 4 vertices. Add $\{u, w_1, w_2\}$: this gives $K_4$ on $\{u,v,w_1,w_2\}$. ✓ (We can add one more triangle $\{v, w_1, w_2\}$ to complete $K_4$.) Can we add a 5th triangle? We showed no.

So the possible triangle components are:
1. Single triangle: 3 vertices, 3 edges (within the component)
2. Diamond ($K_4 - e$): 4 vertices, 5 edges, 2 triangles
3. $K_4$: 4 vertices, 6 edges, 4 triangles
4. Book $B_k$ for $k \geq 3$: $k+2$ vertices, $2k+1$ edges, $k$ triangles

Wait, but these components don't account for all edges between the component vertices. The component is a subgraph of $G$, and there might be additional edges within the component vertices that don't create new triangles.

Hmm, actually, I need to be more careful. The "component" is defined by the triangles, but the vertices of the component might have additional edges between them that don't form triangles (or form triangles that are already counted).

Let me reconsider. Let me think about the vertex set of a triangle component. For a book $B_k$ with edge $\{u,v\}$, the vertex set is $\{u, v, w_1, \ldots, w_k\}$. The edges within this set include $\{u,v\}, \{u,w_i\}, \{v,w_i\}$ for all $i$. Are there edges $\{w_i, w_j\}$? If there were, we'd get a triangle $\{u, w_i, w_j\}$ (since $\{u,w_i\}$ and $\{u,w_j\}$ are edges), which would be a new triangle. As we showed, this creates a butterfly if $k \geq 3$. So for $k \geq 3$, there are no edges between the $w_i$'s.

For $k = 2$ (book $B_2$), we can add edge $\{w_1, w_2\}$ to get $K_4$ (creating 2 more triangles). Or we can leave it as $B_2$ (diamond).

For $K_4$, all edges are present, so no more edges can be added within the 4 vertices.

Now, the key insight: different triangle components use disjoint vertex sets. The remaining vertices (not in any triangle) form a triangle-free subgraph, and edges between different components and non-triangle vertices must be carefully controlled.

Let me think about the overall structure. Let the triangle components be $C_1, \ldots, C_t$ with vertex sets $V_1, \ldots, V_t$ (disjoint). Let $R$ be the remaining vertices (not in any triangle). 

Edges in $G$:
1. Within each $V_i$: edges of the component.
2. Within $R$: triangle-free, so at most $\lfloor |R|^2/4 \rfloor$ edges.
3. Between $V_i$ and $V_j$: any edge here could create triangles. Need to be careful.
4. Between $V_i$ and $R$: any edge here could create triangles.

This is getting complex. Let me think about whether cross-edges can exist.

If there's an edge between $u \in V_i$ and $w \in V_j$ (or $w \in R$), could this create a triangle? A triangle needs 3 edges. If $u$ has a neighbor $u'$ in $V_i$ and $w$ has a neighbor $w'$ in $V_j$ (or $R$), and there are edges $\{u, u'\}$, $\{w, w'\}$, $\{u, w\}$, we need $\{u', w'\}$ to also be an edge for a triangle. But $u'$ and $w'$ are in different components, so $\{u', w'\}$ would be another cross-edge.

Actually, triangles can also form using 2 vertices from one component and 1 from outside, or 1 from each of two components and 1 from $R$, etc.

This is getting very complicated. Let me try a different approach: just compute $m(n)$ for each $n$ from 5 to 10 by finding the extremal number.

Let me think about this more carefully using the following approach: 

**Claim:** $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$ for $n \geq 5$, where $B$ is the butterfly.

Wait, for $n = 5$, we found $\text{ex}(5, B) = 7 = \lfloor 25/4 \rfloor + 1 = 6 + 1 = 7$. ✓

For $n = 6$, the construction gives $10 = \lfloor 36/4 \rfloor + 1 = 9 + 1 = 10$. We need to verify this is optimal.

Let me try to prove the upper bound. Actually, let me think about whether the answer might be different.

Let me consider the problem from the perspective of the Simonovits stability theorem or related results. The butterfly graph $B$ has chromatic number 3 (it's 3-colorable). For 3-chromatic forbidden graphs, the Erdős–Simonovits theorem gives $\text{ex}(n, H) = \frac{n^2}{4} + o(n^2)$ for any 3-chromatic $H$. But the exact value depends on the specific graph.

For the butterfly specifically, I recall that the extremal graph is $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ plus one edge within one part, giving $\lfloor n^2/4 \rfloor + 1$ edges. And this is optimal for $n$ sufficiently large.

But is it optimal for all $n \geq 5$? Let me check $n = 6$ more carefully.

For $n = 6$, can we achieve 11 edges without a butterfly?

Let me try some constructions:
- $K_{3,3}$ + 2 edges: we showed adding 2 edges within one part fails.
- $K_4$ + 2 more vertices with some edges: we showed it's hard to connect to $K_4$.

Let me try: Take $K_4$ on $\{1,2,3,4\}$ (6 edges) and add vertices 5, 6 as an independent set, each connected to all of $\{1,2,3,4\}$. That's $6 + 8 = 14$ edges. But this creates many butterflies. For instance, $\{1,2,3\}$ and $\{1,4,5\}$ share only vertex 1. ✗

What if 5 and 6 are each connected to only 2 vertices of $K_4$? Say 5 connected to $\{1,2\}$ and 6 connected to $\{3,4\}$. Edges: 6 (from $K_4$) + 2 + 2 = 10. Triangles: $\{1,2,5\}$ and $\{3,4,6\}$. These share 0 vertices. ✓ But check: $\{1,2,3\}$ (from $K_4$) and $\{1,2,5\}$ share edge $\{1,2\}$. ✓ $\{1,2,3\}$ and $\{3,4,6\}$ share vertex 3 only. Butterfly! ✗

What if 5 and 6 are connected to the same 2 vertices? Say both connected to $\{1,2\}$. Edges: 6 + 2 + 2 = 10. Triangles: $\{1,2,5\}, \{1,2,6\}$, and the 4 triangles of $K_4$. $\{1,2,5\}$ and $\{3,4,5\}$... wait, is $\{3,4,5\}$ a triangle? 5 is connected to 1 and 2, not 3 or 4. So no. $\{1,2,5\}$ and $\{1,3,4\}$ share vertex 1 only. Butterfly! ✗

So connecting to $K_4$ is really problematic. The triangles in $K_4$ share vertices with everything.

What if we don't use $K_4$? Let me try a different structure.

Take a 5-cycle $\{1,2,3,4,5\}$ and add vertex 6 connected to all 5. Edges: 5 + 5 = 10. Triangles: $\{6, i, i+1\}$ for $i = 1, \ldots, 5$ (mod 5). $\{6,1,2\}$ and $\{6,3,4\}$ share only vertex 6. Butterfly. ✗

Take $K_{3,3}$ + 1 edge = 10. Can we add an 11th edge somewhere?

$K_{3,3}$ on $A = \{a_1, a_2, a_3\}, B = \{b_1, b_2, b_3\}$, plus edge $\{a_1, a_2\}$. Can we add another edge? Options:
- $\{a_1, a_3\}$: star within $A$, but we showed $G[N(a_1)]$ becomes $K_{2,3}$, not a star. ✗
- $\{a_2, a_3\}$: similar. ✗
- $\{b_1, b_2\}$: creates triangles $\{a_i, b_1, b_2\}$ for $i = 1,2,3$. $\{a_1, a_2, b_1\}$ and $\{a_3, b_1, b_2\}$ share $b_1$ only. Butterfly. ✗
- $\{b_1, b_3\}$ or $\{b_2, b_3\}$: similar. ✗

So we can't add an 11th edge to this construction. 

Let me try a completely different 11-edge graph on 6 vertices. 

Actually, let me think about it from the upper bound side. Let me try to prove that $\text{ex}(n, B) \leq \lfloor n^2/4 \rfloor + 1$ for $n \geq 5$.

**Proof attempt:** Let $G$ be a butterfly-free graph on $n$ vertices. We want to show $e(G) \leq \lfloor n^2/4 \rfloor + 1$.

If $G$ is triangle-free, $e(G) \leq \lfloor n^2/4 \rfloor$ by Mantel's theorem. ✓

If $G$ has at least one triangle, consider the structure. Let $T$ be a triangle in $G$ on vertices $\{a, b, c\}$. 

For any vertex $v$ not in $T$, $v$ can be adjacent to at most 2 vertices of $T$ (otherwise, if $v$ is adjacent to all 3, we get 3 new triangles $\{v,a,b\}, \{v,b,c\}, \{v,a,c\}$, and $\{v,a,b\}$ shares only $v$ with $\{a,b,c\}$... wait, $\{v,a,b\}$ and $\{a,b,c\}$ share edge $\{a,b\}$. So they share 2 vertices. That's OK. But $\{v,a,b\}$ and $\{v,b,c\}$ share edge $\{v,b\}$. OK. $\{v,a,b\}$ and $\{v,a,c\}$ share edge $\{v,a\}$. OK. So $v$ adjacent to all 3 of $T$ gives $K_4$, which is fine.

But if $v$ is adjacent to all 3 of $T$, and there's another vertex $w$ adjacent to 2 vertices of $T$, say $\{a, b\}$, then $\{v, a, c\}$ and $\{w, a, b\}$ share only vertex $a$. Butterfly! ✗ (assuming $v \neq w$ and $w$ is not adjacent to $c$).

Hmm, so the constraint is more subtle. Let me think about this differently.

Let me use the structural characterization. For every vertex $v$, $G[N(v)]$ is a star or triangle.

Let me consider the complement approach or an induction approach.

Actually, let me just try to compute the values for $n = 5, 6, 7, 8, 9, 10$ assuming $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$, and then verify.

$n = 5$: $\lfloor 25/4 \rfloor + 1 = 6 + 1 = 7$. $m(5) = 8$.
$n = 6$: $\lfloor 36/4 \rfloor + 1 = 9 + 1 = 10$. $m(6) = 11$.
$n = 7$: $\lfloor 49/4 \rfloor + 1 = 12 + 1 = 13$. $m(7) = 14$.
$n = 8$: $\lfloor 64/4 \rfloor + 1 = 16 + 1 = 17$. $m(8) = 18$.
$n = 9$: $\lfloor 81/4 \rfloor + 1 = 20 + 1 = 21$. $m(9) = 22$.
$n = 10$: $\lfloor 100/4 \rfloor + 1 = 25 + 1 = 26$. $m(10) = 27$.

Sum = 8 + 11 + 14 + 18 + 22 + 27 = 100.

But I need to verify that $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$ for all these $n$.

Let me verify $n = 7$. Construction: $K_{3,4}$ + 1 edge = $12 + 1 = 13$. No butterfly (same argument as before). Can we get 14 edges on 7 vertices without a butterfly?

Let me think about whether there's a better construction for some $n$.

**Alternative construction: $K_4$ on 4 vertices + $K_{\lfloor (n-4)/2 \rfloor, \lceil (n-4)/2 \rceil}$ on the remaining $n-4$ vertices, with no edges between them.** Edges = $6 + \lfloor (n-4)^2/4 \rfloor$. For $n = 7$: $6 + \lfloor 9/4 \rfloor = 6 + 2 = 8$. Worse than 13.

**Alternative: Two disjoint $K_4$'s for $n = 8$.** Edges = $6 + 6 = 12$. Worse than 17.

**Alternative: $K_4$ + complete bipartite on remaining, with some cross-edges.** This seems hard to make work.

Let me also consider: **Book $B_k$ + complete bipartite on remaining.** Book $B_k$ on $k+2$ vertices with $2k+1$ edges, plus $K_{\lfloor (n-k-2)/2 \rfloor, \lceil (n-k-2)/2 \rceil}$ on the remaining $n-k-2$ vertices, no cross-edges. Total: $2k+1 + \lfloor (n-k-2)^2/4 \rfloor$.

For $n = 7, k = 1$: $3 + \lfloor 25/4 \rfloor = 3 + 6 = 9$. Worse than 13.
For $n = 7, k = 2$: $5 + \lfloor 16/4 \rfloor = 5 + 4 = 9$. Worse.
For $n = 7, k = 5$: $11 + \lfloor 0/4 \rfloor = 11$. Worse than 13.

So the bipartite + 1 edge construction seems best.

But wait, can we have cross-edges between a triangle component and the bipartite part? If we have a book $B_1$ (single triangle $\{a,b,c\}$) and a bipartite graph on the remaining vertices, can we add edges between them?

If vertex $d$ (in the bipartite part) is connected to $a$ and $b$, we get triangle $\{a,b,d\}$, which shares edge $\{a,b\}$ with $\{a,b,c\}$. OK. But if another vertex $e$ is connected to $a$ and $c$, we get triangle $\{a,c,e\}$, which shares only vertex $a$ with $\{a,b,d\}$. Butterfly! ✗

So cross-edges are very restricted. Essentially, if we have a triangle $\{a,b,c\}$, any external vertex can be connected to at most 2 vertices of the triangle, and those 2 must be the same pair for all external vertices (to avoid butterflies). So all external vertices connected to the triangle must connect to the same edge, say $\{a,b\}$. This extends the triangle to a book.

So the structure is: we have a book $B_k$ (possibly $k=0$, i.e., no triangles) on some vertex set, and the remaining vertices form a bipartite graph with no edges to the book.

Wait, but can the remaining vertices have edges to the book's "spine" vertices (the two vertices of the common edge)? Let me think...

If we have book $B_k$ with common edge $\{u,v\}$ and pages $w_1, \ldots, w_k$, and an external vertex $x$ connected to $u$ (but not $v$ or any $w_i$), then $x$ doesn't form any triangle with the book. But $x$ might form triangles with other external vertices. As long as those triangles don't share exactly one vertex with the book's triangles, we're fine.

A triangle involving $x$ and two other external vertices $y, z$ would share 0 vertices with the book's triangles (if $y, z$ are also external). ✓

A triangle $\{x, u, y\}$ where $x, y$ are external and $u$ is the book's spine: this shares vertex $u$ with triangle $\{u, v, w_i\}$. If $y \neq v$ and $y \neq w_i$, this is a butterfly! ✗

So external vertices can't be connected to the book's spine vertices (unless they're also connected to $v$, making them part of the book).

Hmm, what if $x$ is connected to both $u$ and $v$? Then $x$ is a page of the book (triangle $\{u,v,x\}$). So $x$ is part of the book.

What if $x$ is connected to $u$ and some $w_i$? Then triangle $\{u, w_i, x\}$ (if $\{u, w_i\}$ is an edge, which it is). This shares edge $\{u, w_i\}$ with $\{u, v, w_i\}$. But it shares only vertex $u$ with $\{u, v, w_j\}$ for $j \neq i$. Butterfly if $k \geq 2$! ✗

So for $k \geq 2$, external vertices can't connect to any book vertex. For $k = 1$ (single triangle), an external vertex $x$ connected to $u$ and $w_1$: triangle $\{u, w_1, x\}$ shares edge $\{u, w_1\}$ with $\{u, v, w_1\}$. The only other triangle is $\{u, v, w_1\}$. So no butterfly. But now we have a new triangle, and we need to check all pairs. $\{u, w_1, x\}$ and $\{u, v, w_1\}$ share edge $\{u, w_1\}$. ✓. But if another external vertex $y$ is connected to $u$ and $v$: triangle $\{u, v, y\}$ shares only $u$ with $\{u, w_1, x\}$. Butterfly! ✗

So for $k = 1$, external vertices can connect to at most one pair of the triangle's vertices, and all must connect to the same pair. This extends the book.

OK so the conclusion is: in a butterfly-free graph, the vertex set can be partitioned into:
1. A book $B_k$ (for some $k \geq 0$; $k = 0$ means no triangles) on $k + 2$ vertices (or 0 vertices if no triangles).
2. A triangle-free graph on the remaining $n - k - 2$ vertices (or $n$ vertices if no triangles).
3. No edges between the book and the triangle-free part.

Wait, but I showed that external vertices can't connect to book vertices (for $k \geq 2$) or can only extend the book (for $k = 1$). So there are truly no edges between the book and the rest.

Hmm, but this isn't quite right either. What if an external vertex is connected to just one book vertex? Say $x$ is connected to $u$ (spine of book) but not to $v$ or any $w_i$. Then $x$ doesn't form a triangle with any book vertices (since it's only connected to $u$, and a triangle needs 2 neighbors of $x$ that are adjacent). So no new triangles involving $x$ and book vertices. ✓

But we need to check: does $x$ being connected to $u$ create issues with the neighborhood condition? $N(u)$ includes $v, w_1, \ldots, w_k, x$, and possibly other external vertices. $G[N(u)]$ must be a star or triangle. The edges in $G[N(u)]$ include $\{v, w_i\}$ for all $i$ (since $v$ is connected to all $w_i$ in the book). If $x$ is connected to some other vertex $y \in N(u)$, that adds an edge. But we need $G[N(u)]$ to remain a star or triangle.

The edges $\{v, w_i\}$ for $i = 1, \ldots, k$ form a star centered at $v$ (in $G[N(u)]$). If $k \geq 3$, this star has $k \geq 3$ edges. Adding $x$ to $N(u)$: if $x$ has no edges to other vertices in $N(u)$, then $G[N(u)]$ is a star (centered at $v$) plus an isolated vertex $x$. But a star plus an isolated vertex is NOT a star or triangle (it has $k + 1$ vertices and $k$ edges, with $k \geq 3$). ✗

So for $k \geq 3$, we can't add $x$ to $N(u)$ without connecting $x$ to $v$ (which would make $x$ a page of the book). 

For $k = 2$: $G[N(u)]$ has edges $\{v, w_1\}, \{v, w_2\}$, a star with 2 edges on 3 vertices. Adding $x$: $G[N(u)]$ has 4 vertices and 2 edges (star + isolated). Not a star (4 vertices) or triangle. ✗

For $k = 1$: $G[N(u)]$ has edge $\{v, w_1\}$, a star with 1 edge on 2 vertices (plus $u$'s other neighbors). Adding $x$: $G[N(u)]$ has vertices $\{v, w_1, x, \ldots\}$ and edge $\{v, w_1\}$ plus any edges involving $x$. If $x$ has no edges to $v$ or $w_1$, then $G[N(u)]$ is a single edge plus isolated vertices. This is a star (with center $v$ or $w_1$) only if there are no other edges. But if $u$ has other neighbors in the external part, and those neighbors have edges among themselves...

This is getting very complicated. Let me try a cleaner approach.

Let me just try to prove the upper bound $\text{ex}(n, B) \leq \lfloor n^2/4 \rfloor + 1$ directly.

**Proof of upper bound:**

Let $G$ be a butterfly-free graph on $n$ vertices with $m$ edges. We want to show $m \leq \lfloor n^2/4 \rfloor + 1$.

If $G$ is triangle-free, $m \leq \lfloor n^2/4 \rfloor \leq \lfloor n^2/4 \rfloor + 1$. ✓

If $G$ has a triangle, let $\Delta$ be the set of triangles. Consider the graph $H$ on the same vertex set where we define a partition based on the triangle structure.

Actually, let me use a different approach. Let me use the following lemma:

**Lemma:** In a butterfly-free graph, if $e$ is an edge that is in at least one triangle, then either:
(a) $e$ is in exactly one triangle, or
(b) $e$ is in multiple triangles, and all triangles in the graph use edges from a single "book" or $K_4$ structure.

Hmm, this isn't precise enough. Let me think differently.

**Key observation:** In a butterfly-free graph, consider any edge $e = \{u, v\}$ that is in $k$ triangles. The $k$ triangles are $\{u, v, w_1\}, \ldots, \{u, v, w_k\}$. Any other triangle $T$ in the graph must share 0 or 2+ vertices with each $\{u, v, w_i\}$.

If $T$ shares 2 vertices with $\{u, v, w_i\}$: either $T$ contains $u$ and $v$ (so $T = \{u, v, w_j\}$, already counted), or $T$ contains $u$ and $w_i$ (so $T = \{u, w_i, x\}$ for some $x$), or $T$ contains $v$ and $w_i$ (so $T = \{v, w_i, x\}$).

If $T = \{u, w_i, x\}$ with $x \neq v$: $T$ shares vertex $u$ with $\{u, v, w_j\}$ for $j \neq i$. If $x \neq w_j$ and $v \neq w_j$ (which is true) and $w_i \neq w_j$ (true) and $x \neq v$ (assumed), then $T$ and $\{u, v, w_j\}$ share only vertex $u$. Butterfly! ✗ (if $k \geq 2$, i.e., there exists $j \neq i$).

So if $k \geq 2$ (edge $\{u,v\}$ is in at least 2 triangles), then no triangle of the form $\{u, w_i, x\}$ with $x \neq v$ can exist. Similarly, no $\{v, w_i, x\}$ with $x \neq u$.

If $k = 1$ (edge $\{u,v\}$ is in exactly 1 triangle $\{u, v, w\}$), then triangles $\{u, w, x\}$ or $\{v, w, x\}$ could exist, but they must not create butterflies with other triangles.

This is still complex. Let me try yet another approach.

**Approach via edge counting:**

Let $G$ be butterfly-free on $n$ vertices. Let $t$ be the number of triangles. 

For each edge $e$, let $t(e)$ be the number of triangles containing $e$. Then $\sum_e t(e) = 3t$.

The condition implies a strong constraint on the triangle structure. Let me think about the "triangle edge" graph: edges that are in at least one triangle.

Let me define $F$ as the subgraph of $G$ consisting of edges that are in at least one triangle. The edges not in $F$ are "triangle-free edges."

**Claim:** $F$ is a union of vertex-disjoint components, each being either a $K_3$, $K_4$, or a book $B_k$ ($k \geq 2$).

Wait, I think I showed this above. The triangle components are:
- Single triangle ($K_3$): 3 vertices, 3 edges
- Diamond ($K_4 - e$): 4 vertices, 5 edges, 2 triangles (book $B_2$)
- $K_4$: 4 vertices, 6 edges, 4 triangles
- Book $B_k$ for $k \geq 3$: $k+2$ vertices, $2k+1$ edges, $k$ triangles

And these components are vertex-disjoint.

Now, the edges of $G$ consist of:
1. Edges within triangle components (the $F$ edges)
2. Edges between different triangle components: must be 0 (since a triangle in one component and a triangle in another are vertex-disjoint, but an edge between components could create a new triangle... actually, an edge between components doesn't necessarily create a triangle. But if it did, the new triangle would share vertices with both components.)

Wait, actually, edges between different triangle components don't necessarily create triangles. An edge $\{u, v\}$ with $u$ in component $C_1$ and $v$ in component $C_2$ is just an edge. It creates a triangle only if there's a common neighbor of $u$ and $v$ that is adjacent to both.

But if such a triangle exists, it would share vertices with triangles in $C_1$ and $C_2$, potentially creating a butterfly.

Let me think about this. Suppose $u \in C_1$, $v \in C_2$, and $w$ is a common neighbor with $\{u,w\}$ and $\{v,w\}$ edges. Then $\{u,v,w\}$ is a triangle. If $C_1$ has a triangle containing $u$, say $\{u, a, b\}$, then $\{u,v,w\}$ and $\{u,a,b\}$ share vertex $u$. If $v,w \notin \{a,b\}$ (which is true since $C_1$ and $C_2$ are vertex-disjoint and $w$ is not in $C_1$... well, $w$ could be in $C_1$ or $C_2$ or neither).

If $w \in C_1$: then $\{u, w\}$ is an edge in $C_1$. The triangle $\{u, v, w\}$ shares edge $\{u, w\}$ with some triangle in $C_1$ (if $\{u, w\}$ is a triangle edge in $C_1$). But it shares only vertex $u$ or $w$ with other triangles in $C_1$.

This is getting too complicated. Let me try to just verify the values computationally for small $n$.

Actually, I can't use tools. Let me think about this more carefully.

Let me try to prove the upper bound more carefully.

**Theorem:** For $n \geq 5$, $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$.

**Lower bound:** $K_{\lfloor n/2 \rfloor, \lceil n/2 \rceil}$ plus one edge within the larger part gives $\lfloor n^2/4 \rfloor + 1$ edges and is butterfly-free. ✓

**Upper bound:** Let $G$ be butterfly-free on $n$ vertices with $m$ edges. We show $m \leq \lfloor n^2/4 \rfloor + 1$.

Case 1: $G$ is triangle-free. $m \leq \lfloor n^2/4 \rfloor$. ✓

Case 2: $G$ has at least one triangle. 

Let me use the following approach. Pick any triangle $T = \{a, b, c\}$ in $G$. Partition the remaining $n - 3$ vertices based on their adjacency to $T$:
- $V_0$: vertices adjacent to 0 vertices of $T$
- $V_1$: vertices adjacent to exactly 1 vertex of $T$
- $V_2$: vertices adjacent to exactly 2 vertices of $T$
- $V_3$: vertices adjacent to all 3 vertices of $T$

A vertex in $V_3$ creates 3 triangles with $T$: $\{v, a, b\}, \{v, b, c\}, \{v, a, c\}$. Together with $T$, this is $K_4$ on $\{a, b, c, v\}$. If there are two vertices $v, w \in V_3$, then $\{v, a, b\}$ and $\{w, a, c\}$ share only vertex $a$. Butterfly! ✗ So $|V_3| \leq 1$.

If $|V_3| = 1$, say $V_3 = \{d\}$, we have $K_4$ on $\{a,b,c,d\}$. Now consider any other vertex $x$. If $x$ is adjacent to 2 vertices of $\{a,b,c,d\}$, say $a$ and $b$, then $\{x, a, b\}$ is a triangle. $\{x, a, b\}$ and $\{c, a, d\}$ (a triangle in $K_4$) share only vertex $a$. Butterfly! ✗ (since $x \neq c, d$ and $b \neq c, d$). So $x$ can be adjacent to at most 1 vertex of $\{a,b,c,d\}$.

So with $K_4$: the 4 vertices of $K_4$ have 6 edges among them. Each of the remaining $n - 4$ vertices is adjacent to at most 1 vertex of $K_4$, contributing at most $n - 4$ edges. Among the remaining $n - 4$ vertices, the subgraph is butterfly-free (and triangle-free? not necessarily, but let me think...).

Actually, the remaining $n-4$ vertices could have their own triangles, forming their own triangle components. But by the same argument, those components are vertex-disjoint from $K_4$.

The edges among the remaining $n-4$ vertices: at most $\text{ex}(n-4, B)$ (by induction, if we had an inductive argument). Plus at most $n - 4$ edges to $K_4$.

Total: $6 + (n-4) + \text{ex}(n-4, B) = n + 2 + \text{ex}(n-4, B)$.

If $\text{ex}(n-4, B) = \lfloor (n-4)^2/4 \rfloor + 1$, total = $n + 2 + \lfloor (n-4)^2/4 \rfloor + 1 = n + 3 + \lfloor (n-4)^2/4 \rfloor$.

Compare with $\lfloor n^2/4 \rfloor + 1$:
- $n$ even: $\lfloor n^2/4 \rfloor + 1 = n^2/4 + 1$. $n + 3 + (n-4)^2/4 = n + 3 + (n^2 - 8n + 16)/4 = n + 3 + n^2/4 - 2n + 4 = n^2/4 - n + 7$. We need $n^2/4 - n + 7 \leq n^2/4 + 1$, i.e., $-n + 7 \leq 1$, i.e., $n \geq 6$. ✓ for $n \geq 6$.
- $n$ odd: $\lfloor n^2/4 \rfloor + 1 = (n^2-1)/4 + 1$. $n + 3 + \lfloor (n-4)^2/4 \rfloor$. If $n$ is odd, $n - 4$ is odd, so $\lfloor (n-4)^2/4 \rfloor = ((n-4)^2 - 1)/4 = (n^2 - 8n + 15)/4$. Total: $n + 3 + (n^2 - 8n + 15)/4 = (4n + 12 + n^2 - 8n + 15)/4 = (n^2 - 4n + 27)/4$. We need $(n^2 - 4n + 27)/4 \leq (n^2 - 1)/4 + 1 = (n^2 + 3)/4$. So $n^2 - 4n + 27 \leq n^2 + 3$, i.e., $-4n + 27 \leq 3$, i.e., $n \geq 6$. ✓ for $n \geq 6$.

So the $K_4$ case gives fewer edges than the bipartite+1 construction for $n \geq 6$. For $n = 5$: $K_4$ + 1 remaining vertex, adjacent to at most 1 vertex of $K_4$: $6 + 1 = 7$ edges. Same as $\lfloor 25/4 \rfloor + 1 = 7$. So both constructions give 7 for $n = 5$.

Now let me handle the case $|V_3| = 0$, i.e., no vertex is adjacent to all 3 vertices of $T$.

If $|V_3| = 0$, every vertex outside $T$ is in $V_0, V_1,$ or $V_2$.

A vertex $v \in V_2$ adjacent to, say, $a$ and $b$: creates triangle $\{v, a, b\}$, which shares edge $\{a, b\}$ with $T$. ✓

Now, if $v, w \in V_2$ are both adjacent to $a$ and $b$: triangles $\{v, a, b\}$ and $\{w, a, b\}$ share edge $\{a, b\}$. ✓. But if $v$ is adjacent to $a, b$ and $w$ is adjacent to $a, c$: $\{v, a, b\}$ and $\{w, a, c\}$ share only $a$. Butterfly! ✗

So all vertices in $V_2$ must be adjacent to the same pair of vertices from $T$. WLOG, all $V_2$ vertices are adjacent to $a$ and $b$.

Now, $V_2$ vertices together with $a, b$ form a book $B_{|V_2|+1}$ (the triangle $T$ plus $|V_2|$ more triangles, all sharing edge $\{a, b\}$).

What about $V_1$ and $V_0$ vertices? 

A $V_1$ vertex $x$ adjacent to, say, $a$: $x$ doesn't form a triangle with $T$. But if $x$ is also adjacent to some $v \in V_2$, and $v$ is adjacent to $a$, then $\{x, a, v\}$ is a triangle. This triangle shares vertex $a$ with $\{a, b, c\}$ (triangle $T$). If $x \neq b, c$ and $v \neq b, c$ (true since $v \in V_2$ is adjacent to $a, b$ and $v \neq c$ since $v \notin V_3$), then $\{x, a, v\}$ and $\{a, b, c\}$ share only $a$. Butterfly! ✗

So $V_1$ vertices adjacent to $a$ cannot be adjacent to any $V_2$ vertex. Similarly, $V_1$ vertices adjacent to $b$ cannot be adjacent to any $V_2$ vertex (since $V_2$ vertices are all adjacent to $b$).

What about $V_1$ vertices adjacent to $c$? A vertex $x$ adjacent to only $c$: if $x$ is adjacent to some $v \in V_2$ (which is adjacent to $a, b$), is $\{x, c, v\}$ a triangle? Only if $\{c, v\}$ is an edge. But $v \in V_2$ is adjacent to $a, b$ only (not $c$, since $v \notin V_3$). So $\{c, v\}$ is not an edge. No triangle. ✓

But what if $x$ (adjacent to $c$) is adjacent to $y$ (adjacent to $a$), and $\{x, y\}$ is an edge? Then $\{x, y, c\}$ is not a triangle (since $y$ is not adjacent to $c$). $\{x, y, a\}$ is not a triangle (since $x$ is not adjacent to $a$). So no triangle involving both $x$ and $y$ unless there's a common neighbor.

This is getting very involved. Let me try to bound the total edges more carefully.

Let me set up notation. $T = \{a, b, c\}$, $|V_2| = p$ (all adjacent to $a, b$), $|V_1| = q_1$ (adjacent to $a$ only) + $q_2$ (adjacent to $b$ only) + $q_3$ (adjacent to $c$ only), $|V_0| = r$. $p + q_1 + q_2 + q_3 + r = n - 3$.

Edges:
1. Within $T$: 3
2. Between $T$ and $V_2$: $2p$ (each $V_2$ vertex connects to $a, b$)
3. Between $T$ and $V_1$: $q_1 + q_2 + q_3$ (each connects to one vertex of $T$)
4. Between $T$ and $V_0$: 0
5. Within $V_2 \cup \{a, b\}$: the book has $2p + 1$ edges (edge $\{a,b\}$ plus $2p$ edges to pages). But we already counted $\{a,b\}$ in (1) and the $2p$ edges in (2). Are there edges within $V_2$? If $v, w \in V_2$ and $\{v, w\}$ is an edge, then $\{a, v, w\}$ is a triangle (since $a$ is adjacent to both). This triangle shares vertex $a$ with $\{a, b, c\}$. If $w \neq b, c$ (true), butterfly! ✗ (if $p \geq 1$... wait, $\{a, v, w\}$ and $\{a, b, c\}$ share only $a$ if $v, w \neq b, c$. Since $v, w \in V_2$ and $V_2 \cap T = \emptyset$, yes. So butterfly.) 

So no edges within $V_2$ (if $p \geq 1$). Actually, even if $p = 0$, $V_2$ is empty, so trivially no edges.

Wait, I need to be more careful. If $p \geq 2$ and there's an edge $\{v, w\}$ within $V_2$, then $\{a, v, w\}$ is a triangle. This shares only $a$ with $\{a, b, c\}$. Butterfly. ✗. So no edges within $V_2$.

6. Edges within $V_1$: vertices in $V_1$ adjacent to different vertices of $T$ might have edges between them. Let me think about what's allowed.

Let $A_1 = V_1$ vertices adjacent to $a$, $B_1 = V_1$ vertices adjacent to $b$, $C_1 = V_1$ vertices adjacent to $c$.

Edges within $A_1$: if $x, y \in A_1$ and $\{x, y\}$ is an edge, then $\{a, x, y\}$ is a triangle. This shares only $a$ with $\{a, b, c\}$. Butterfly! ✗ So no edges within $A_1$.

Similarly, no edges within $B_1$ or $C_1$.

Edges between $A_1$ and $B_1$: if $x \in A_1, y \in B_1, \{x, y\}$ edge. Triangle $\{a, x, y\}$? Need $\{a, y\}$ edge, but $y \in B_1$ is adjacent to $b$ only, not $a$. So no. Triangle $\{b, x, y\}$? Need $\{b, x\}$ edge, but $x \in A_1$ is adjacent to $a$ only. No. So $\{x, y\}$ doesn't create a triangle with $T$. ✓

But does $\{x, y\}$ create a triangle with any other triangle? If $p \geq 1$, there's a book triangle $\{a, b, v\}$ for $v \in V_2$. $\{x, y\}$ and $\{a, b, v\}$: $x \in A_1, y \in B_1$, $v \in V_2$. The edge $\{x, y\}$ is not a triangle by itself. But if $x$ is adjacent to $v$ (both in $A_1 \cup V_2$... wait, $v \in V_2$ is adjacent to $a, b$. $x \in A_1$ is adjacent to $a$. If $\{x, v\}$ is an edge, then $\{a, x, v\}$ is a triangle (since $a$ adjacent to both $x$ and $v$). This shares only $a$ with $\{a, b, c\}$. Butterfly! ✗

So $A_1$ vertices cannot be adjacent to $V_2$ vertices. Similarly, $B_1$ vertices cannot be adjacent to $V_2$ vertices.

What about $C_1$ and $V_2$? $x \in C_1$ (adjacent to $c$), $v \in V_2$ (adjacent to $a, b$). If $\{x, v\}$ is an edge: triangle $\{c, x, v\}$? Need $\{c, v\}$ edge, but $v$ is not adjacent to $c$. No. Triangle $\{a, x, v\}$? Need $\{a, x\}$ edge, but $x \in C_1$ is adjacent to $c$ only. No. So $\{x, v\}$ doesn't create a triangle. ✓

But we need to check butterflies with existing triangles. The edge $\{x, v\}$ itself isn't a triangle. But if $x$ and $v$ have a common neighbor $z$ with $\{x, z\}$ and $\{v, z\}$ edges, then $\{x, v, z\}$ is a triangle. If $z = a$: $\{a, x\}$ not an edge. If $z = b$: $\{b, x\}$ not an edge. If $z = c$: $\{c, v\}$ not an edge. If $z \in V_2$: $\{x, z\}$ — $x \in C_1, z \in V_2$. We just said this is OK (no triangle with $T$). But $\{v, z\}$ — both in $V_2$, and we showed no edges within $V_2$. So $z \notin V_2$ (as a neighbor of $v$). If $z \in C_1$: $\{v, z\}$ — $v \in V_2, z \in C_1$, same as $\{x, v\}$ type, OK. But $\{x, z\}$ — both in $C_1$, no edges within $C_1$. So $z \notin C_1$. 

This is getting really complicated. Let me try to simplify by considering the structure more carefully.

Let me define the "book part" as $B = \{a, b\} \cup V_2$ (the book with edge $\{a, b\}$ and $p$ pages), and the "rest" as $R = V_0 \cup V_1 = V_0 \cup A_1 \cup B_1 \cup C_1$.

I've shown:
- No edges within $V_2$
- No edges within $A_1, B_1, C_1$
- No edges between $A_1$ and $V_2$, or $B_1$ and $V_2$
- Edges between $A_1$ and $B_1$ are OK (don't create triangles with $T$)
- Edges between $C_1$ and $V_2$ are OK (don't create triangles with $T$)

What about edges between $A_1$ and $C_1$? $x \in A_1, y \in C_1, \{x, y\}$ edge. Triangle $\{a, x, y\}$? Need $\{a, y\}$, but $y \in C_1$ not adjacent to $a$. No. Triangle $\{c, x, y\}$? Need $\{c, x\}$, but $x \in A_1$ not adjacent to $c$. No. So no triangle with $T$. ✓

But could $\{x, y\}$ create a triangle with a book triangle? If $p \geq 1$, book has triangle $\{a, b, v\}$. $\{x, y\}$ and this triangle: $x \in A_1, y \in C_1, v \in V_2$. For a new triangle involving $\{x, y\}$, need a common neighbor. $a$ is adjacent to $x$ but not $y$. $c$ is adjacent to $y$ but not $x$. $v$ is adjacent to... $v$ is adjacent to $a, b$. Is $v$ adjacent to $x$ or $y$? $v \in V_2, x \in A_1$: we said no edges between $A_1$ and $V_2$. $v \in V_2, y \in C_1$: edges allowed but not assumed. So unless $\{v, y\}$ is an edge, no triangle. And even if $\{v, y\}$ is an edge, the triangle would be $\{y, v, ?\}$ — need a common neighbor of $y$ and $v$ that's adjacent to both. $c$ is adjacent to $y$ but not $v$. $a$ is adjacent to $v$ but not $y$. So no triangle from $\{v, y\}$ alone.

OK so edges between $A_1$ and $C_1$, $B_1$ and $C_1$, $A_1$ and $B_1$ are all OK (don't directly create triangles with $T$ or the book). But they might create triangles among themselves, which could create butterflies.

Let me think about the subgraph on $R = V_0 \cup A_1 \cup B_1 \cup C_1$. This subgraph must itself be butterfly-free (since any butterfly in it is a butterfly in $G$). Also, triangles in this subgraph must not create butterflies with the book triangles.

A triangle in $R$ shares 0 vertices with the book triangles (since $R \cap B = \emptyset$). So triangles in $R$ and book triangles are vertex-disjoint. ✓ No butterfly between them.

So the subgraph on $R$ is butterfly-free, and by induction, has at most $\text{ex}(|R|, B)$ edges.

Now, edges between $R$ and the book $B = \{a, b\} \cup V_2$:
- $A_1$ to $a$: $|A_1|$ edges (already counted as $V_1$-$T$ edges)
- $B_1$ to $b$: $|B_1|$ edges
- $C_1$ to $c$: $|C_1|$ edges
- $C_1$ to $V_2$: at most $|C_1| \cdot |V_2|$ edges (allowed)
- $A_1$ to $V_2$: 0 (forbidden)
- $B_1$ to $V_2$: 0 (forbidden)
- $V_0$ to $B$: 0 (by definition, $V_0$ has no neighbors in $T$; but what about $V_0$ to $V_2$? $V_0$ vertices are not adjacent to $a, b, c$. Can they be adjacent to $V_2$ vertices?)

$V_0$ to $V_2$: $x \in V_0, v \in V_2, \{x, v\}$ edge. Does this create a triangle? $v$ is adjacent to $a, b$. $x$ is adjacent to neither $a, b, c$. So $\{a, v, x\}$? Need $\{a, x\}$, no. $\{b, v, x\}$? Need $\{b, x\}$, no. So no triangle with book. ✓ But $\{x, v\}$ might create triangles with other vertices. If $x$ and $v$ have a common neighbor $z$ adjacent to both: $v$'s neighbors include $a, b$, and possibly $C_1$ and $V_0$ vertices. $x$'s neighbors include $V_0, A_1, B_1, C_1$ vertices (not $a, b, c$). Common neighbor could be in $C_1$ or $V_0$. If $z \in C_1$: $\{v, z\}$ and $\{x, z\}$ edges, and $\{x, v\}$ edge → triangle $\{x, v, z\}$. This triangle shares 0 vertices with book triangles. ✓ (as long as it doesn't create a butterfly with other triangles in $R$).

So $V_0$ to $V_2$ edges are allowed but might create triangles in the subgraph on $R \cup V_2$... this is getting really complex.

Let me try a different, cleaner approach. Let me try to prove the upper bound by induction.

**Induction hypothesis:** $\text{ex}(n, B) \leq \lfloor n^2/4 \rfloor + 1$ for all $n \geq 5$.

Base case $n = 5$: We verified $\text{ex}(5, B) = 7 = \lfloor 25/4 \rfloor + 1$. ✓

Inductive step: Assume $\text{ex}(k, B) \leq \lfloor k^2/4 \rfloor + 1$ for all $5 \leq k < n$. Show for $n$.

Let $G$ be butterfly-free on $n$ vertices with $m$ edges. If triangle-free, $m \leq \lfloor n^2/4 \rfloor$. ✓

If $G$ has a triangle $T = \{a, b, c\}$, I'll use the structure above.

Hmm, the induction is tricky because of the cross-edges. Let me try a different approach.

**Direct counting approach:**

Let $G$ be butterfly-free on $n$ vertices. For each vertex $v$, $G[N(v)]$ is a star or triangle.

Let $d(v)$ be the degree of $v$ and $e(v)$ be the number of edges in $G[N(v)]$ (i.e., the number of triangles through $v$... no, $e(v)$ is the number of edges among neighbors of $v$, which equals the number of triangles through $v$).

If $G[N(v)]$ is a star, $e(v) \leq d(v) - 1$.
If $G[N(v)]$ is a triangle, $e(v) = 3$ and $d(v) = 3$.

The number of triangles $t = \frac{1}{3} \sum_v e(v)$.

Now, $\sum_v d(v) = 2m$ and $\sum_v e(v) = 3t$.

By the Kruskal-Katona or Fisher inequality type arguments... hmm, not sure.

Let me try another approach. Let me use the following:

**Claim:** In a butterfly-free graph, the triangles form a "linear hypergraph" in some sense, and the number of edges is bounded.

Actually, let me try to use the following approach based on the structure.

**Structure theorem:** In a butterfly-free graph $G$, the vertex set can be partitioned into sets $V_1, \ldots, V_k, R$ where:
- Each $V_i$ is the vertex set of a triangle component (book $B_{p_i}$ or $K_4$).
- $R$ is the set of vertices not in any triangle.
- There are no edges between different $V_i$'s.
- The subgraph on $R$ is triangle-free (bipartite).
- Edges between $V_i$ and $R$ are restricted.

Wait, I haven't fully established this. Let me think about whether edges between different triangle components can exist.

If $C_1$ and $C_2$ are two triangle components with vertex sets $V_1, V_2$, and there's an edge $\{u, v\}$ with $u \in V_1, v \in V_2$: this edge doesn't create a triangle by itself. But if there's a vertex $w$ adjacent to both $u$ and $v$, then $\{u, v, w\}$ is a triangle. If $w \in V_1$, this triangle shares vertices with triangles in $C_1$ and $C_2$, potentially creating a butterfly.

If $w \in V_1$ and $w$ is in a triangle with $u$ in $C_1$, say triangle $\{u, w, x\}$: then $\{u, v, w\}$ and $\{u, w, x\}$ share edge $\{u, w\}$. ✓. But $\{u, v, w\}$ and any other triangle in $C_1$ not containing both $u$ and $w$: if $C_1$ is a book with edge $\{u, w\}$... actually, this depends on the structure.

This is really complex. Let me just try to verify the formula $\text{ex}(n, B) = \lfloor n^2/4 \rfloor + 1$ for $n = 5, 6, 7$ by checking that no graph with $\lfloor n^2/4 \rfloor + 2$ edges is butterfly-free.

For $n = 5$: $\lfloor 25/4 \rfloor + 2 = 8$. We showed every 8-edge graph on 5 vertices has a butterfly. ✓

For $n = 6$: $\lfloor 36/4 \rfloor + 2 = 11$. Need to show every 11-edge graph on 6 vertices has a butterfly.
