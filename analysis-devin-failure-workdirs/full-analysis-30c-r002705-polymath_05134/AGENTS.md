# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   In a city with 120 underground lines, every station can be reached from any other station with no more than 15 changes. Two stations are considered distant if at least 5 changes are needed to travel between them. What is the maximum number of pairwise distant stations that can exist in this city?       — 题目文本
#   To solve the problem, we need to determine the maximum number of pairwise distant stations in a city with 120 underground lines, where every station can be reached from any other with no more than 15 changes, and two stations are distant if at least 5 changes are required between them.

### Step-by-Step Solution:

1. **Understanding the Problem**:
   - A "change" refers to switching lines when traveling between stations.
   - The distance between two stations is the minimum number of changes required to travel between them.
   - We need a set of stations where each pair is at least 5 changes apart.

2. **Graph Representation**:
   - Model the underground network as a graph where each line is a hyperedge.
   - Stations on the same line can be reached without a change, so their distance is 0.
   - The distance between two stations on different lines is the number of changes (line switches) required.

3. **Key Insight**:
   - To maximize the number of pairwise distant stations, we need to ensure each station is part of its own line and sufficiently far from others.
   - Consider a star-like structure with a central hub and branches radiating out.

4. **Star Structure Analysis**:
   - Each branch is a path of stations connected by lines.
   - For the minimum distance requirement (5 changes), each branch must have a depth of 3 lines:
     - Hub connected to A via line 1.
     - A connected to B via line 2.
     - B connected to C via line 3.
   - Distance between endpoints of two branches: 3 (to hub) + 3 (to the other endpoint) = 6 changes, which meets the requirement.

5. **Calculations**:
   - Each branch uses 3 lines.
   - With 120 lines, the number of branches (and endpoints) is \( \frac{120}{3} = 40 \).

6. **Validation**:
   - This structure ensures all endpoints are pairwise at least 6 changes apart.
   - The diameter of the network is 6, which is within the allowed 15.

### Final Answer:
Thus, the maximum number of pairwise distant stations is \(\boxed{40}\).  — 标准解答
#   Let me analyze this problem carefully.

We have a city with 120 underground lines. Every station can be reached from any other station with no more than 15 changes. Two stations are "distant" if at least 5 changes are needed to travel between them. We need to find the maximum number of pairwise distant stations.

Let me think about this in graph-theoretic terms. We have 120 "lines" and stations. A "change" means switching from one line to another. Let me think about the structure.

Let me model this. Consider a graph where lines are vertices. When two lines share a station, they are connected by an edge. A journey between two stations involves: start on some line, possibly change lines. The number of changes is the number of line switches.

Actually, let me think more carefully. A station is on some set of lines. To travel from station A to station B, you pick a line through A, ride it, possibly change to another line, etc., until you reach a line through B. The number of changes is the number of times you switch lines.

If station A is on line $l_A$ and station B is on line $l_B$, and the shortest path in the "line graph" (where lines are vertices and edges connect lines that share a station) from $l_A$ to $l_B$ has length $d$, then the number of changes needed is $d$ (if $l_A \neq l_B$) or 0 (if $l_A = l_B$).

Wait, actually if A and B are on the same line, 0 changes. If A is on line $l_1$ and B is on line $l_2$ and $l_1, l_2$ share a station, then 1 change. In general, if the shortest path in the line graph from $l_1$ to $l_2$ has $d$ edges, the number of changes is $d$.

So "distant" means the line graph distance between some line of A and some line of B is at least 5. But actually, a station can be on multiple lines. So the number of changes between station A and station B is:
$$\min_{l_A \in L(A), l_B \in L(B)} \text{dist}_{\text{line graph}}(l_A, l_B)$$
where $L(A)$ is the set of lines through station A.

Hmm, but this is getting complex. Let me think about what structure maximizes pairwise distant stations.

The constraint is: every station can be reached from any other with no more than 15 changes. This means the line graph has diameter at most 15 (roughly). Actually, more precisely, for any two stations A, B, $\min_{l_A \in L(A), l_B \in L(B)} \text{dist}(l_A, l_B) \leq 15$.

Two stations are distant if $\min_{l_A \in L(A), l_B \in L(B)} \text{dist}(l_A, l_B) \geq 5$.

We want to maximize the number of pairwise distant stations.

Let me think about this differently. Consider the line graph $G$ with 120 vertices (lines). The diameter of $G$ is at most 15 (since any two stations can be connected with at most 15 changes, and in particular, any two lines can be connected... well, not exactly, because stations might be on specific lines).

Actually, let me reconsider. The condition "every station can be reached from any other station with no more than 15 changes" means that for any two stations A, B:
$$\min_{l_A \in L(A), l_B \in L(B)} d_G(l_A, l_B) \leq 15$$

Now, for a set of pairwise distant stations, for any two stations A, B in this set:
$$\min_{l_A \in L(A), l_B \in L(B)} d_G(l_A, l_B) \geq 5$$

To maximize the number of such stations, we want to design the line graph and station placement.

Let me think about a simpler model. Suppose each station is on exactly one line. Then the number of changes between a station on line $l_1$ and a station on line $l_2$ is $d_G(l_1, l_2)$. The condition becomes: $G$ has diameter at most 15. Distant stations are on lines at distance $\geq 5$ in $G$. We want to maximize the number of lines that are pairwise at distance $\geq 5$.

Wait, but if each station is on one line, then we can have at most one station per line (otherwise two stations on the same line would have distance 0 < 5). So we want to find a set of lines that are pairwise at distance $\geq 5$ in a graph with 120 vertices and diameter $\leq 15$.

Hmm, but we could also have stations on multiple lines. Let me think about whether that helps.

If a station is on multiple lines, say lines $l_1$ and $l_2$, then its "distance" to a station on line $l_3$ is $\min(d(l_1, l_3), d(l_2, l_3))$. So being on multiple lines only makes a station closer to others, which is bad for being distant. So to maximize distant stations, each station should be on exactly one line.

So the problem reduces to: In a graph $G$ with 120 vertices and diameter $\leq 15$, what is the maximum size of a set of vertices that are pairwise at distance $\geq 5$?

Wait, but I need to be more careful. The condition is that every station can reach every other with at most 15 changes. If each station is on one line, this means the line graph has diameter $\leq 15$. But actually, we also need to make sure the graph is connected (which is implied by diameter being finite).

So the problem is: **What is the maximum number of vertices in a graph on 120 vertices with diameter at most 15 such that there exists a set of pairwise distance-$\geq 5$ vertices of that size?**

Hmm wait, actually we want to maximize the size of such a set. We're designing the graph to maximize this. So we want to find the graph on 120 vertices with diameter $\leq 15$ that has the largest possible set of pairwise distance-$\geq 5$ vertices.

Let me think about this. If we have a set $S$ of vertices pairwise at distance $\geq 5$, and the graph has diameter $\leq 15$, then for any two vertices $u, v \in S$, $5 \leq d(u,v) \leq 15$.

Consider the "balls" of radius 2 around each vertex in $S$. Since vertices in $S$ are at distance $\geq 5$, these balls (radius 2) are disjoint. Each ball has at least 1 vertex (the center). But we need to be more careful.

Actually, let me think about it differently. Let's think about what graph structure allows the most pairwise distance-$\geq 5$ vertices while keeping diameter $\leq 15$.

Consider a path graph. If we have a path of 120 vertices, the diameter is 119, which is way more than 15. So a path doesn't work.

Consider a graph that looks like a "spider": a central vertex connected to many paths. But the diameter would be the sum of the two longest paths, which could be large.

Let me think about the Moore bound and related concepts. For a graph with diameter $D$ and maximum degree $\Delta$, the number of vertices is at most $1 + \Delta + \Delta(\Delta-1) + \ldots + \Delta(\Delta-1)^{D-1}$.

But here we want to maximize a specific set. Let me think about the structure differently.

Let me consider a graph that is a "tree-like" structure. Consider a tree where we have a root, and from the root, we have branches. The diameter is the longest path between two leaves.

Actually, let me think about this more carefully using the concept of a "packing."

If we want $k$ vertices pairwise at distance $\geq 5$, and the diameter is $\leq 15$, let me think about what constrains $k$.

Consider the open balls of radius 2 around each of the $k$ vertices. These are disjoint (since pairwise distance $\geq 5 > 2 \cdot 2 = 4$). So the total number of vertices is at least $k$ (just the centers), and at most 120.

But that only gives $k \leq 120$, which is trivial.

Let me think about the diameter constraint. The diameter is $\leq 15$. Consider two vertices $u, v \in S$ with $d(u,v) \geq 5$. There's a path of length $\leq 15$ between them. 

Hmm, let me think about this problem from a different angle. 

Consider a graph $G$ on 120 vertices with diameter $\leq 15$. We want to find the maximum $k$ such that there exist $k$ vertices pairwise at distance $\geq 5$.

Let me think about an extremal construction. 

Consider a "caterpillar" or "comb" structure. Or consider a graph that is a long path with shortcuts.

Actually, let me think about a specific construction. Consider a graph that is a path $v_1, v_2, \ldots, v_{120}$ but with additional edges to reduce the diameter. 

Alternatively, think about it as follows. We want to place $k$ "centers" on a graph of 120 vertices with diameter $\leq 15$, such that any two centers are at distance $\geq 5$.

The key insight: if we have $k$ centers pairwise at distance $\geq 5$, the balls of radius 2 around them are disjoint. Each such ball contains at least 1 vertex. But we also need the diameter to be $\leq 15$.

Let me think about a tree construction. Consider a tree $T$ with 120 vertices and diameter $\leq 15$. In a tree, the distance is unique. We want to maximize the number of vertices pairwise at distance $\geq 5$.

In a tree with diameter $D$, consider a longest path (diameter path) of length $D$. Any vertex is within distance $\lfloor D/2 \rfloor$ of some vertex on this path (the center of the tree).

Hmm, this is getting complicated. Let me think about specific constructions.

**Construction 1: A "star of paths"**

Consider a central vertex $c$. From $c$, we have $m$ paths, each of length $L$. The total number of vertices is $1 + mL$. The diameter is $2L$ (from the end of one path to the end of another). We need $2L \leq 15$, so $L \leq 7$.

On each path of length $L$ (vertices at distances $0, 1, 2, \ldots, L$ from $c$), we can place centers at distance $\geq 5$ from each other. On a path of length $L$ (with $L+1$ vertices), the maximum number of vertices pairwise at distance $\geq 5$ is $\lfloor L/5 \rfloor + 1$.

But we also need centers on different paths to be at distance $\geq 5$. The distance between a vertex at distance $a$ from $c$ on one path and a vertex at distance $b$ from $c$ on another path is $a + b$. So we need $a + b \geq 5$ for centers on different paths.

If we place centers at distance $L$ from $c$ (the ends of paths), then the distance between two such centers is $2L$. We need $2L \geq 5$, so $L \geq 3$. With $L = 7$, $2L = 14 \geq 5$. ✓

On each path of length 7 (8 vertices: $c, v_1, \ldots, v_7$), we can place centers at $v_7$ and... $v_2$ (distance 5 from $v_7$). So 2 centers per path. But wait, $v_2$ on one path and $v_7$ on another path: distance = $2 + 7 = 9 \geq 5$. ✓ And $v_2$ on two different paths: distance = $2 + 2 = 4 < 5$. ✗

So we can't place $v_2$ on multiple paths. Let me reconsider.

If we place centers only at $v_7$ (the end of each path), then each path contributes 1 center, and we need $1 + 7m \leq 120$, so $m \leq 17$. That gives 17 centers. But we might do better.

Alternatively, on each path, place centers at $v_7$ and $v_2$. But $v_2$ on different paths are at distance 4, which is too close. So we can only use $v_2$ on one path. That gives $m + 1$ centers (one $v_2$ plus $m$ endpoints), with $1 + 7m \leq 120$, so $m \leq 17$, giving 18 centers. Not much better.

What if we use paths of different lengths? Or a different structure?

**Construction 2: A path with diameter-reducing edges**

Consider a path $v_1, v_2, \ldots, v_{120}$. Add edges to reduce diameter to $\leq 15$. For instance, connect $v_i$ to $v_{i+8}$ for all valid $i$. This creates a graph where you can "skip" 8 steps at a time. The diameter would be roughly $\lceil 119/8 \rceil = 15$. 

In this graph, what's the distance between $v_i$ and $v_j$? It's roughly $\lceil |i-j|/8 \rceil$ (using the skip edges) but also the path edges give distance $|i-j|$. The actual shortest path uses a combination. With edges of length 1 and length 8, the distance is $\lceil |i-j|/8 \rceil$ if we only use skip edges... no, we need to be more careful.

Actually, with edges $v_i v_{i+1}$ and $v_i v_{i+8}$, the distance from $v_1$ to $v_{120}$ is $\min$ over paths. Using skip edges: $119 = 14 \cdot 8 + 7$, so 14 skips of 8 and 7 steps of 1, total 21 edges. That's too many.

Let me use skip edges of length 15. Connect $v_i$ to $v_{i+15}$. Then the distance from $v_1$ to $v_{120}$ is $\lceil 119/15 \rceil = 8$. But the distance between $v_1$ and $v_2$ is 1 (direct edge). The distance between $v_1$ and $v_{16}$ is 1 (skip edge). The distance between $v_1$ and $v_{17}$ is 2 ($v_1 \to v_{16} \to v_{17}$).

Hmm, but in this graph, the distance between $v_i$ and $v_j$ is roughly $\lceil |i-j|/15 \rceil$ (for large $|i-j|$) or $|i-j|$ (for small $|i-j|$, using path edges). Actually, the shortest path uses a combination of skip-15 edges and path-1 edges. The distance is $\lfloor |i-j|/15 \rfloor + (|i-j| \mod 15)$... no, that's not right either.

With edges of length 1 and length 15, the shortest path from $v_i$ to $v_j$ (with $j > i$) uses as many length-15 edges as possible, then length-1 edges. So the distance is $\lfloor (j-i)/15 \rfloor + ((j-i) \mod 15)$. For $j - i = 119$: $\lfloor 119/15 \rfloor + (119 \mod 15) = 7 + 14 = 21$. That's way more than 15.

OK so this approach of a path with skip edges doesn't easily give diameter 15. Let me think differently.

**Better approach: Think about the problem as a packing problem.**

We have a graph on 120 vertices with diameter $\leq 15$. We want to pack as many vertices as possible such that pairwise distance $\geq 5$.

The balls of radius 2 around the packed vertices are disjoint. So if each ball has size $b$, then $kb \leq 120$, giving $k \leq 120/b$.

But we also need the diameter constraint. The diameter being $\leq 15$ means the graph is "well-connected."

Let me think about what graph maximizes the packing. 

Consider a graph that is a disjoint union of cliques connected by a path-like structure. Actually, the graph must be connected (diameter is finite).

**Key idea: Use a "blow-up" of a path.**

Consider a path $P$ of length $d$ (with $d+1$ vertices). Replace each vertex of $P$ with a clique of size $s$. Connect consecutive cliques with all possible edges (complete bipartite). This gives a graph with $s(d+1)$ vertices. The diameter is $d$ (distance between a vertex in the first clique and a vertex in the last clique). 

We need $s(d+1) = 120$ and $d \leq 15$.

In this graph, the distance between a vertex in clique $i$ and a vertex in clique $j$ is $|i-j|$. So two vertices are at distance $\geq 5$ iff they are in cliques at distance $\geq 5$.

To maximize pairwise distant vertices, we pick one vertex from each clique that is at distance $\geq 5$ from all others. The maximum number of cliques pairwise at distance $\geq 5$ on a path of $d+1$ cliques is $\lfloor d/5 \rfloor + 1$.

Wait, but we can also pick multiple vertices from the same clique - no, vertices in the same clique are at distance 0 (or 1, depending on convention; in a clique, distance is 1 between distinct vertices, 0 to self). Actually, in a clique, all vertices are at distance 1 from each other. So we can pick at most 1 vertex per clique for our distant set.

Hmm wait, actually in the blow-up, vertices in the same clique are at distance... if it's a clique, they're at distance 1. So we can pick at most 1 per clique. And we need the cliques to be at distance $\geq 5$.

On a path of $d+1$ vertices (cliques), the maximum number of vertices pairwise at distance $\geq 5$ is $\lfloor d/5 \rfloor + 1$.

So we want to maximize $\lfloor d/5 \rfloor + 1$ subject to $s(d+1) = 120$, $d \leq 15$, $s \geq 1$.

To maximize $\lfloor d/5 \rfloor + 1$, we want $d$ as large as possible. With $d = 15$, we need $s \cdot 16 = 120$, so $s = 7.5$, not integer. With $d = 14$, $s \cdot 15 = 120$, $s = 8$. Then $\lfloor 14/5 \rfloor + 1 = 2 + 1 = 3$. That's only 3.

With $d = 15$, $s = 7$ (using 112 vertices, wasting 8), $\lfloor 15/5 \rfloor + 1 = 4$. Better but still small.

Hmm, this blow-up approach doesn't seem to give many centers. The issue is that the blow-up "wastes" vertices on making cliques.

**Alternative: Don't blow up. Use a sparse graph.**

If we don't blow up, we have a path of 120 vertices, but the diameter is 119, way too large. We need to add edges to reduce the diameter to 15.

**Key insight: The problem is about the trade-off between diameter and packing.**

Let me think about it as follows. We have $n = 120$ vertices, diameter $D \leq 15$, and we want to pack vertices at pairwise distance $\geq r = 5$.

There's a general bound: in a graph with $n$ vertices and diameter $D$, the maximum packing with pairwise distance $\geq r$ is at most... let me think.

Consider the $k$ packed vertices $v_1, \ldots, v_k$. The balls of radius $\lfloor (r-1)/2 \rfloor = 2$ around them are disjoint. Each ball has at least 1 vertex. So $k \leq n = 120$. That's trivial.

But the diameter constraint adds more. Consider the "metric" on the $k$ vertices. The distance between any two is between 5 and 15. 

Hmm, let me think about a different construction.

**Construction: A tree with a long spine and short branches.**

Consider a "caterpillar": a path (spine) $v_1, \ldots, v_m$ with leaves attached. The diameter is roughly $m$ (if leaves are short). To get diameter $\leq 15$, we need $m \leq 15$ (roughly). But then we only have $\sim 15$ spine vertices, and we can pack $\lfloor 15/5 \rfloor + 1 = 4$ centers on the spine. Plus leaves, but leaves are at distance 1 from the spine, so they don't help much.

This doesn't seem right. Let me reconsider.

Wait, I think I need to reconsider the problem. The diameter is at most 15, meaning the graph is quite "compact." With 120 vertices and diameter 15, the graph is relatively dense or well-structured.

Let me think about the problem from the perspective of metric spaces. We have a finite metric space (from the graph) on 120 points with diameter $\leq 15$. We want to find the maximum number of points pairwise at distance $\geq 5$.

This is a packing problem in metric spaces. The answer depends on the structure of the metric space, which we get to design (subject to being a graph metric with 120 points and diameter $\leq 15$).

**Key question: What graph metric on 120 points with diameter $\leq 15$ maximizes the 5-packing number?**

Let me think about lower and upper bounds.

**Upper bound:** Consider $k$ points pairwise at distance $\geq 5$. The open balls of radius 2 around them are disjoint. In a graph, the ball of radius 2 around a vertex of degree $d$ contains at most $1 + d + d(d-1) = 1 + d^2$ vertices. But we don't know the degree.

Actually, let me think about a different upper bound. Consider the $k$ centers. For each pair, the distance is between 5 and 15. 

Hmm, let me think about a specific construction that might be optimal.

**Construction: Complete bipartite-like structure.**

Actually, let me think about a different approach. Consider a graph that is a "thick path": a sequence of groups $G_0, G_1, \ldots, G_d$ where each group is an independent set, and edges exist only between consecutive groups (complete bipartite between $G_i$ and $G_{i+1}$). 

The diameter is $d$. The distance between a vertex in $G_i$ and a vertex in $G_j$ is $|i-j|$. Two vertices in the same group are at distance 2 (through a common neighbor in $G_{i-1}$ or $G_{i+1}$). Wait, actually, if $G_i$ and $G_{i+1}$ are completely connected, then two vertices in $G_i$ are at distance 2 (going through any vertex in $G_{i-1}$ or $G_{i+1}$). Actually, they might be at distance 2 or might not be connected through a single intermediate. Let me reconsider.

If the graph is: $G_0 - G_1 - \ldots - G_d$ with complete bipartite between consecutive groups, and no edges within groups, then:
- Distance between $u \in G_i$ and $v \in G_j$ ($i < j$): $j - i$ (go through $G_{i+1}, \ldots, G_{j-1}$, but actually you can go directly: $u \to w \in G_{i+1} \to \ldots \to v$, which takes $j - i$ steps).
- Distance between $u, v \in G_i$ ($u \neq v$): 2 (go $u \to w \in G_{i-1} \to v$ or $u \to w \in G_{i+1} \to v$), assuming $i > 0$ and $i < d$. For $i = 0$: distance is 2 (through $G_1$). For $i = d$: distance is 2 (through $G_{d-1}$).

So in this graph, the diameter is $d$ (between $G_0$ and $G_d$). We need $d \leq 15$.

For the packing: we want vertices pairwise at distance $\geq 5$. Two vertices in the same group are at distance 2, so we can pick at most 1 per group. Two vertices in groups at distance $\geq 5$ are at distance $\geq 5$. So we need to pick groups that are pairwise at distance $\geq 5$.

On a path of $d+1$ groups, the maximum number of groups pairwise at distance $\geq 5$ is $\lfloor d/5 \rfloor + 1$.

With $d = 15$: $\lfloor 15/5 \rfloor + 1 = 4$. And we need $\sum |G_i| = 120$ with $d + 1 = 16$ groups. We can make each group have $\lceil 120/16 \rceil = 8$ vertices (some 7, some 8). But we only pick 4 vertices (one from each of 4 groups at positions 0, 5, 10, 15).

That gives only 4 centers. Can we do better?

**The issue is that on a path-like structure, the packing is limited by the path length.**

Let me think about whether a non-path-like structure can do better.

**Construction: A "grid" or higher-dimensional structure.**

Consider a 2D grid. If we have an $a \times b$ grid graph, the diameter is $(a-1) + (b-1) = a + b - 2$. We need $a + b - 2 \leq 15$, so $a + b \leq 17$. The number of vertices is $ab \leq 120$.

The distance between $(i_1, j_1)$ and $(i_2, j_2)$ is $|i_1 - i_2| + |j_1 - j_2|$ (Manhattan distance). We want points pairwise at Manhattan distance $\geq 5$.

To maximize the packing, we want to maximize $a$ and $b$ subject to $a + b \leq 17$ and $ab \leq 120$ (actually $ab = 120$ or $\leq 120$). 

With $a + b = 17$: $ab$ is maximized when $a = b = 8.5$, so $a = 8, b = 9$, $ab = 72 \leq 120$. Or $a = 7, b = 10$, $ab = 70$. Or $a = 6, b = 11$, $ab = 66$. Or $a = 5, b = 12$, $ab = 60$.

Actually, we can have $ab \leq 120$, so we could have $a = 8, b = 9$ (72 vertices) or we could use more vertices. But the grid graph has $ab$ vertices, and we need $ab \leq 120$. With $a + b \leq 17$, the maximum $ab$ is $8 \times 9 = 72$, which is less than 120. So we're not using all 120 vertices.

Hmm, but we could add more vertices. Or use a different structure.

Actually, wait. We don't need to use exactly 120 vertices. We need at most 120 vertices (120 lines). Actually, re-reading the problem: "120 underground lines." So there are exactly 120 lines. Each station is on at least one line. But the number of stations is not specified.

Oh wait, I think I've been confusing "lines" and "stations." Let me re-read the problem.

"In a city with 120 underground lines, every station can be reached from any other station with no more than 15 changes. Two stations are considered distant if at least 5 changes are needed to travel between them. What is the maximum number of pairwise distant stations that can exist in this city?"

So there are 120 lines. The number of stations is not fixed. We want to maximize the number of pairwise distant stations.

A "change" is switching lines. So if I'm on line $L_1$ and I switch to line $L_2$, that's 1 change. The number of changes to go from station A to station B is the number of line switches.

Let me reconsider the model. Each station is on some set of lines. The line graph has 120 vertices (lines), with an edge between two lines if they share a station. The number of changes between station A and station B is:
$$\min_{l_A \in L(A), l_B \in L(B)} d_{\text{line graph}}(l_A, l_B)$$
where $d$ is the shortest path distance in the line graph (number of edges = number of changes).

Wait, actually, if A is on line $l_A$ and B is on line $l_B$, and $l_A = l_B$, then 0 changes. If $l_A \neq l_B$ and they share a station, then 1 change (ride $l_A$ to the shared station, switch to $l_B$, ride to B). In general, if the shortest path in the line graph from $l_A$ to $l_B$ has $d$ edges, the number of changes is $d$.

So the number of changes = distance in the line graph.

The condition "every station can reach every other with $\leq 15$ changes" means: for all stations A, B, $\min_{l_A \in L(A), l_B \in L(B)} d(l_A, l_B) \leq 15$.

"Distant" means $\min_{l_A \in L(A), l_B \in L(B)} d(l_A, l_B) \geq 5$.

Now, the line graph has 120 vertices. The number of stations is not fixed. Each station is on some subset of lines. We want to maximize the number of pairwise distant stations.

As I argued before, to maximize distant stations, each station should be on exactly one line (being on more lines only reduces distances). So each station is on exactly one line, and the number of changes between a station on line $l_1$ and a station on line $l_2$ is $d(l_1, l_2)$.

Now, the condition "every station can reach every other with $\leq 15$ changes" becomes: for any two lines $l_1, l_2$ that have stations, $d(l_1, l_2) \leq 15$. If every line has at least one station, this means the line graph has diameter $\leq 15$.

But wait, we could have some lines with no stations. If a line has no station, it still exists in the line graph (it's a vertex) but doesn't host any station. However, it could still serve as an intermediate line for connections. Hmm, but if a line has no stations, can you ride on it? You need to board at a station. If a line has no stations, you can't board it, so it's useless for travel. But it could still be a vertex in the line graph if it shares stations with other lines... but it has no stations, so it doesn't share stations with anyone, so it's isolated. That doesn't help.

Actually, let me reconsider. A line is a route with stations on it. Every line has stations (otherwise it's not really a line). But we get to design the system. We have 120 lines, and we design which stations are on which lines, and which lines share stations.

So the line graph has 120 vertices. We design the edges (by placing stations at intersections of lines). We also design which stations are on which lines (each station is on some subset of lines). We want to maximize the number of pairwise distant stations.

As argued, each station should be on exactly one line. So we place some number of stations, each on a single line. Two stations on the same line are at distance 0 (no changes needed). So for pairwise distant stations, we need at most 1 station per line, and the lines must be pairwise at distance $\geq 5$ in the line graph.

Wait, but we could also have "dummy" stations on lines that are not in our distant set, just to create intersections between lines (i.e., to create edges in the line graph). These dummy stations are on multiple lines (to create edges), but they're not part of our distant set.

So the setup is:
- Line graph $G$ on 120 vertices, which we design.
- We pick a set $S$ of lines, pairwise at distance $\geq 5$ in $G$.
- We place one station on each line in $S$ (on exactly that line).
- We place additional "intersection stations" on pairs of lines to create edges in $G$.
- The diameter of $G$ must be $\leq 15$ (so that any two stations can be connected with $\leq 15$ changes).
- We want to maximize $|S|$.

Wait, but the diameter condition: for any two stations A, B, the number of changes is $\leq 15$. If A is on line $l_A \in S$ and B is on line $l_B \in S$, then $d_G(l_A, l_B) \leq 15$. Since $S$ is a subset of lines, and we need all pairs in $S$ to have $d_G \leq 15$, but also any station (including intersection stations) to any other station. An intersection station on lines $l_1, l_2$ and a station on line $l_3$: the number of changes is $\min(d(l_1, l_3), d(l_2, l_3)) \leq 15$. Since the intersection station is on $l_1$ and $l_2$, and $l_1, l_2$ are adjacent in $G$ (they share a station), $d(l_1, l_3) \leq d(l_2, l_3) + 1$ and vice versa. So if the diameter of $G$ is $\leq 15$, then any station can reach any other with $\leq 15$ changes (since the station is on some line, and the distance in $G$ to any other line is $\leq 15$).

Actually, we need to be a bit more careful. The diameter of $G$ being $\leq 15$ means any two lines are at distance $\leq 15$. Then any two stations (each on at least one line) can be connected with $\leq 15$ changes. ✓

So the problem reduces to: **Design a graph $G$ on 120 vertices with diameter $\leq 15$, and find the maximum $|S|$ where $S$ is a set of vertices pairwise at distance $\geq 5$.**

And we want to maximize $|S|$ over all such graphs $G$.

Now, this is a cleaner problem. Let me think about it.

**Upper bound approach:**

Consider $k$ vertices pairwise at distance $\geq 5$ in a graph on 120 vertices with diameter $\leq 15$. 

The open balls of radius 2 around the $k$ vertices are disjoint. Each ball contains at least 1 vertex (the center). So $k \leq 120$.

But we can get a better bound using the diameter constraint. Consider the $k$ centers $v_1, \ldots, v_k$. For each pair $(v_i, v_j)$, $5 \leq d(v_i, v_j) \leq 15$.

Consider the ball of radius 7 around each center. Since the diameter is $\leq 15$, every vertex is within distance 7 of some center (because for any vertex $u$ and any center $v_i$, $d(u, v_i) \leq 15$, so $d(u, v_i) \leq 15$; but we need $d(u, v_i) \leq 7$ for some $i$).

Hmm, that's not necessarily true. Let me think again. If $u$ is a vertex and $v_1$ is a center, $d(u, v_1) \leq 15$. But we need $d(u, v_i) \leq 7$ for some $i$. This isn't guaranteed.

Let me try a different approach. Consider the balls of radius 2 around the $k$ centers. These are disjoint. The total number of vertices in these balls is $\sum_{i=1}^k |B(v_i, 2)|$. Since the balls are disjoint and contained in the 120 vertices, $\sum |B(v_i, 2)| \leq 120$.

Now, what's the minimum size of $B(v, 2)$? It's at least 1 (just the center). But if the graph has diameter $\leq 15$ and 120 vertices, the graph must be reasonably connected, so balls might be larger.

Actually, the minimum ball size depends on the degree. A vertex of degree 1 has $|B(v, 2)| \geq 1 + 1 + (\text{neighbors of the neighbor}) \geq 3$. A vertex of degree 0 is isolated, but then the graph isn't connected.

Hmm, this approach gives $k \leq 120 / \min |B(v,2)|$, but the minimum ball size could be small.

Let me think about this differently.

**Better upper bound using the diameter:**

Consider the $k$ centers. Pick any center $v_1$. Every other vertex is within distance 15 of $v_1$. The other centers are at distance $\geq 5$ from $v_1$. So the other $k-1$ centers are in the annulus $\{u : 5 \leq d(v_1, u) \leq 15\}$.

Now, the balls of radius 2 around the $k-1$ other centers are disjoint and contained in the annulus $\{u : 3 \leq d(v_1, u) \leq 15\}$ (since a center at distance $\geq 5$ from $v_1$ has its ball of radius 2 at distance $\geq 3$ from $v_1$). Wait, that's not quite right. The ball of radius 2 around a center at distance $d$ from $v_1$ includes vertices at distance $d-2$ to $d+2$ from $v_1$. Since $d \geq 5$, the closest vertex in the ball to $v_1$ is at distance $d - 2 \geq 3$.

But the ball could also extend beyond distance 15 from $v_1$. However, since the diameter is 15, all vertices are within distance 15 of $v_1$. So the ball is contained in $\{u : 3 \leq d(v_1, u) \leq 15\}$.

The number of vertices in this annulus is at most 120 - |B(v_1, 2)|. But this doesn't directly give a good bound.

Let me try yet another approach.

**Approach: Think about it as a metric embedding problem.**

We have $k$ points with pairwise distances in $[5, 15]$. We want to embed them into a graph metric on 120 points with diameter 15. The graph metric must be a valid graph metric (integer distances, triangle inequality, etc.).

The question is: what's the maximum $k$?

**Construction attempt: Use a tree.**

Consider a tree $T$ on 120 vertices with diameter $\leq 15$. We want to maximize the number of vertices pairwise at distance $\geq 5$.

In a tree, the distance is the unique path length. Let's think about what tree maximizes this.

Consider a "star" with a center and many branches. The center is connected to $d$ branches, each of length $L$. The diameter is $2L$. We need $2L \leq 15$, so $L \leq 7$.

The total number of vertices is $1 + dL$ (center + $d$ branches of $L$ vertices each). We need $1 + dL \leq 120$.

Centers at pairwise distance $\geq 5$: 
- Two vertices on the same branch at distance $\geq 5$: on a branch of length $L$, we can place $\lfloor L/5 \rfloor + 1$ vertices pairwise at distance $\geq 5$.
- Two vertices on different branches at distances $a$ and $b$ from the center: distance $= a + b$. Need $a + b \geq 5$.

If we place vertices at the ends of branches (distance $L$ from center), the distance between two such is $2L \geq 5$ iff $L \geq 3$. With $L = 7$, $2L = 14 \geq 5$. ✓

On each branch of length 7 (vertices at distances 1, 2, ..., 7 from center), we can place vertices at distances 7 and 2 (distance 5 apart). But vertices at distance 2 on different branches are at distance 4 from each other, which is < 5. So we can only use distance 2 on one branch.

Alternatively, place vertices at distances 7 and 3 on each branch (distance 4 apart - too close!). Or 7 and 2 (distance 5). 

Let me be more systematic. On a branch of length 7, the vertices are at distances 1, 2, ..., 7 from the center. We want to select a subset pairwise at distance $\geq 5$. On a path of 7 vertices (distances 1-7), the maximum independent set with pairwise distance $\geq 5$ is: {1, 6}, {1, 7}, {2, 7}, {1}, {2}, ..., {7}. The maximum size is 2 (e.g., {1, 6} or {2, 7}).

But we also need cross-branch distances $\geq 5$. If we pick vertex at distance $a$ on one branch and distance $b$ on another, distance $= a + b \geq 5$.

If we pick {2, 7} on each branch: cross-branch, 2+2=4 < 5. ✗
If we pick {7} on each branch: cross-branch, 7+7=14 ≥ 5. ✓. This gives $d$ centers.
If we pick {7} on all branches and {2} on one branch: 2+7=9 ≥ 5, 7+7=14 ≥ 5. ✓. This gives $d + 1$ centers.

With $L = 7$, $d = \lfloor (120 - 1) / 7 \rfloor = \lfloor 119/7 \rfloor = 17$. So $d + 1 = 18$ centers.

Can we do better? What if we use {7, 2} on one branch and {7} on all others? That's $d + 1 = 18$.

What about {7, 2} on one branch, {7, 3} on another? 2+3=5 ≥ 5. ✓. 7+7=14, 7+3=10, 7+2=9, all ≥ 5. ✓. But 3+3=6 ≥ 5 ✓, 3+7=10 ✓. So {7, 3} on another branch: 2+3=5 ✓. So we could have {7, 2} on branch 1, {7, 3} on branch 2, {7} on branches 3-17. That's 2 + 2 + 15 = 19. But wait, 2+3=5 ≥ 5 ✓. And 3+3 would be if we had {3} on two branches, but we only have {3} on one. Let me check all pairs:
- 2 (branch 1) and 3 (branch 2): 2+3=5 ✓
- 2 (branch 1) and 7 (any other): 2+7=9 ✓
- 3 (branch 2) and 7 (any other): 3+7=10 ✓
- 7 and 7 (different branches): 14 ✓

So this works! 19 centers.

Can we push further? {7, 2} on branch 1, {7, 3} on branch 2, {7, 4} on branch 3? 2+4=6 ✓, 3+4=7 ✓. So yes. 20 centers.

{7, 2}, {7, 3}, {7, 4}, {7, 5}? 2+5=7 ✓, 3+5=8 ✓, 4+5=9 ✓. Yes. 21 centers. But wait, on a branch of length 7, can we pick {7, 5}? Distance = 2 < 5. ✗!

So {7, 5} doesn't work on the same branch (distance 2). We need the two vertices on the same branch to be at distance $\geq 5$. On a branch of length 7 (distances 1-7), pairs at distance $\geq 5$: (1,6), (1,7), (2,7). That's it. (2,7) has distance 5, (1,7) has distance 6, (1,6) has distance 5.

So the only 2-element subsets on a branch are {1,6}, {1,7}, {2,7}.

Using {2,7}: the "2" requires all other non-7 vertices to be at distance $\geq 5$ from it, i.e., at distance $\geq 3$ from center on other branches (since 2+3=5).

Using {1,7}: the "1" requires all other non-7 vertices to be at distance $\geq 4$ from center on other branches (since 1+4=5).

Using {1,6}: the "1" requires $\geq 4$, and the "6" requires $\geq -1$ (always satisfied for positive distances). But 6+6=12 ≥ 5, so "6" on multiple branches is fine. But 1+1=2 < 5, so "1" can only be on one branch.

So let's try: {1, 6} on one branch, {6} on all other branches. Cross-branch: 1+6=7 ✓, 6+6=12 ✓. On the same branch: 1 and 6 are at distance 5 ✓. This gives $d + 1$ centers (one "1" plus $d$ "6"s). With $d = 17$: 18 centers.

Or: {2, 7} on one branch, {7} on all others. 2+7=9 ✓, 7+7=14 ✓. $d + 1 = 18$.

Or: {1, 6} on one branch, {6, ?} on another? On a branch, {1, 6} uses distances 1 and 6. On another branch, can we use {6, 1}? 1+1=2 < 5. ✗. Can we use {6, 2}? 6-2=4 < 5. ✗. {6, 3}? 6-3=3 < 5. ✗. So on another branch, we can only use {6} (single vertex) or find another pair.

Hmm wait, I was considering {1, 6} on one branch. The "6" on this branch and "6" on another branch: 6+6=12 ✓. The "1" on this branch and "6" on another: 1+6=7 ✓. The "1" on this branch and "1" on another: 1+1=2 ✗. So "1" can only appear once.

What if we use {6} on all branches? That's $d$ centers. Plus one "1" on one branch: $d + 1$.

What about using "6" on all branches and "1" on one and "2" on one? 1+2=3 < 5 ✗. So "1" and "2" can't coexist on different branches.

What about "6" on all branches, "1" on one, and "4" on one? 1+4=5 ✓. 4+6=10 ✓. 4+4=8 ✓ (if on different branches). So we could have "6" on all $d$ branches, "1" on one branch, "4" on another. But wait, on the branch with "1", we already have "6". On the branch with "4", we already have "6". So the centers are: $d$ copies of "6", plus "1" (on one branch), plus "4" (on another branch). Total: $d + 2$. But we need 1+4=5 ✓ and 4 is at distance 4 from center, and 6 is at distance 6, so on the same branch, 4 and 6 are at distance 2 < 5. ✗!

So "4" and "6" can't be on the same branch. We'd need "4" on a branch without "6". But we want "6" on all branches. Contradiction.

Let me reconsider. Let me use a different branch structure. Some branches have "6" and some have other things.

Actually, let me think about this more carefully. We have $d$ branches, each of length 7. We want to select a set of vertices (each on some branch, at some distance from center) such that:
1. On the same branch, selected vertices are at distance $\geq 5$.
2. On different branches, selected vertices at distances $a$ and $b$ satisfy $a + b \geq 5$.

We want to maximize the total number of selected vertices.

Let's denote the selected vertices by their distance from the center. On branch $i$, we select a set $S_i \subseteq \{1, 2, ..., 7\}$ with pairwise differences $\geq 5$ (condition 1). For any $a \in S_i, b \in S_j$ ($i \neq j$), $a + b \geq 5$ (condition 2).

Condition 1 on a branch of length 7: $S_i$ can have at most 2 elements, and if it has 2, they must be from $\{(1,6), (1,7), (2,7)\}$.

To maximize the total, we want as many branches as possible to have 2 elements. But condition 2 constrains the "small" elements across branches.

If a branch has 2 elements, one of them is "small" (1 or 2) and one is "large" (6 or 7). The small elements across branches must sum to $\geq 5$.

If we use small element 1 on multiple branches: 1+1=2 < 5. ✗. So at most one branch with small element 1.
If we use small element 2 on multiple branches: 2+2=4 < 5. ✗. So at most one branch with small element 2.
If we use 1 on one branch and 2 on another: 1+2=3 < 5. ✗.

So at most one branch can have 2 elements (either {1,6}, {1,7}, or {2,7}). All other branches can have at most 1 element.

Wait, that's not right. Let me reconsider. If one branch has {1, 6} and another has {2, 7}: 1+2=3 < 5. ✗. If one has {1, 7} and another has {2, 7}: 1+2=3 < 5. ✗.

What if one branch has {1, 6} and another has just {7}? 1+7=8 ✓, 6+7=13 ✓. ✓. And another branch with just {7}? 7+7=14 ✓. ✓.

So: one branch with 2 elements, all others with 1 element (the "large" one). The large element should be $\geq 5$ minus the small element. If small is 1, large on other branches $\geq 4$. If small is 2, large on other branches $\geq 3$.

But the "large" element on other branches is a single element, so it can be anything from 1 to 7. But it must be at distance $\geq 5$ from the small element on the special branch. If small is 1, other single elements $\geq 4$. If small is 2, other single elements $\geq 3$.

But also, the single elements on different branches must be pairwise at sum $\geq 5$. If all single elements are 7: 7+7=14 ✓. If all are 3: 3+3=6 ✓ (if small is 2, 2+3=5 ✓). 

So: one branch with {2, 7}, all other branches with {3}. Check: 2+3=5 ✓, 3+3=6 ✓, 2+7=5 ✓ (same branch), 7+3=10 ✓. Total: $2 + (d-1) = d + 1$.

Or: one branch with {2, 7}, all other branches with {7}. Total: $d + 1$.

Or: one branch with {1, 6}, all other branches with {4}. Check: 1+4=5 ✓, 4+4=8 ✓, 1+6=5 ✓, 6+4=10 ✓. Total: $d + 1$.

Can we get $d + 2$? We'd need two branches with 2 elements each. But as shown, the small elements would conflict (1+2=3 < 5, 1+1=2 < 5, 2+2=4 < 5). So at most one branch with 2 elements. Hence max is $d + 1$.

With $d = 17$ (branches of length 7, $1 + 17 \cdot 7 = 120$): $d + 1 = 18$.

But wait, can we do better with a different tree structure? What about branches of different lengths?

**What if we use branches of length 7 and some of length 6?**

With $L = 7$, $d = 17$, $1 + 17 \cdot 7 = 120$. Exactly 120. ✓

What if we use a mix? Say 16 branches of length 7 and 1 branch of length 8? $1 + 16 \cdot 7 + 8 = 1 + 112 + 8 = 121 > 120$. Too many.

16 branches of length 7 and 1 of length 7: same as 17 branches. 

What about a different tree entirely? Not a star?

**Consider a "double star" or a path with branches.**

Let me think about a tree that's a path of length $p$ (the "spine"), with branches hanging off. The diameter would be the longest path, which could be from the end of a branch on one end to the end of a branch on the other end.

This is getting complicated. Let me think about whether 18 is actually the answer, or if we can do better with a non-tree graph.

**Non-tree construction:**

In a non-tree graph, distances can be shorter (more edges = shorter paths), which is bad for packing. But we might be able to use the extra edges to reduce the diameter while maintaining large distances between centers.

Wait, actually, in a tree, the diameter is already determined by the structure. Adding edges can only decrease distances (and thus the diameter), but it also decreases distances between centers, which is bad.

So trees seem optimal for maximizing packing given a diameter constraint. Let me think about whether that's true.

Actually, for a given number of vertices and diameter, a tree might not be optimal. Consider that in a tree, the diameter path "uses up" vertices that could otherwise be used for packing. In a non-tree, we might be able to have a more compact structure.

Hmm, let me think about this differently.

**Reformulation: We want to maximize $k$ such that there exists a graph on 120 vertices with diameter $\leq 15$ and $k$ vertices pairwise at distance $\geq 5$.**

Let me think about the problem as follows. Consider the $k$ centers. Define $f(v) = \min_i d(v, v_i)$ for each vertex $v$ (distance to nearest center). The centers have $f = 0$. The balls of radius 2 around centers are disjoint, so the vertices with $f \leq 2$ number at least $k$ (the centers) and the sets are disjoint.

Now, the vertices with $f \leq 2$ form $k$ disjoint sets. The vertices with $f = 3, 4$ are "between" centers. The vertices with $f \geq 5$ are... wait, can $f$ be $\geq 5$? If the diameter is 15 and we have $k$ centers, a vertex could be far from all centers. But actually, every vertex is within distance 15 of every center (diameter 15), so $f(v) \leq 15$ for all $v$.

Hmm, I don't think this approach leads anywhere quickly. Let me try to think about specific constructions and see if I can beat 18.

**Construction: A path-like graph with "shortcuts".**

Consider a path $v_0, v_1, \ldots, v_{119}$. Add edges $v_i v_{i+1}$ (path edges). The diameter is 119, too large. Add "shortcut" edges to reduce diameter.

But as I computed earlier, it's hard to reduce the diameter to 15 while maintaining large distances between some vertices.

**Construction: A "broom" or "broom-like" structure.**

Actually, let me reconsider the star construction. With $L = 7$ and $d = 17$, we get 18 centers. Can we use $L = 7$ and $d = 17$ but with a different assignment?

Actually, I realize we might be able to do better by not using a star. Let me think about a "caterpillar" graph.

**Caterpillar construction:**

A caterpillar is a path (spine) with leaves attached. Consider a spine $v_0, v_1, \ldots, v_s$ and leaves attached to spine vertices. 

The diameter is at most $s + 2$ (from a leaf on one end to a leaf on the other, going through the spine). We need $s + 2 \leq 15$, so $s \leq 13$.

The total number of vertices is $(s + 1) + \text{(number of leaves)}$. We need this $\leq 120$.

For packing: we want vertices pairwise at distance $\geq 5$. 

Spine vertices at distance $\geq 5$: on a path of length $s = 13$ (14 vertices), we can pick $\lfloor 13/5 \rfloor + 1 = 3$ vertices (e.g., $v_0, v_5, v_{10}$).

Leaves: a leaf attached to $v_i$ is at distance 1 from $v_i$. The distance between a leaf on $v_i$ and a leaf on $v_j$ is $|i-j| + 2$. For this to be $\geq 5$, $|i-j| \geq 3$.

A leaf on $v_i$ and a spine vertex $v_j$: distance $= 1 + |i-j|$. For $\geq 5$, $|i-j| \geq 4$.

This is getting complicated. Let me think about whether the caterpillar can beat 18.

With $s = 13$, we have 14 spine vertices. We can attach leaves to spine vertices. The total is $14 + \text{leaves} \leq 120$, so up to 106 leaves.

If we attach leaves to $v_0, v_3, v_6, v_9, v_{12}$ (every 3rd vertex), with leaves pairwise at distance $\geq 5$: leaf on $v_0$ and leaf on $v_3$: distance $= 3 + 2 = 5$. ✓. Leaf on $v_0$ and leaf on $v_6$: $6 + 2 = 8$. ✓. So we can have one leaf per selected spine vertex, and they're pairwise at distance $\geq 5$.

But we can have multiple leaves on the same spine vertex? No, two leaves on the same spine vertex are at distance 2 (through the spine vertex), which is < 5.

So we can have at most 1 leaf per spine vertex in our packing. With 5 spine vertices selected (every 3rd), we get 5 leaves. Plus possibly some spine vertices.

Spine vertices pairwise at distance $\geq 5$: $v_0, v_5, v_{10}$ (3 vertices). But these are at distance 1 from their leaves, so a spine vertex and a leaf on an adjacent spine vertex might be too close.

This is getting messy. Let me think about it more carefully.

Actually, I think the star construction might be close to optimal, but let me think about whether we can do better.

**General upper bound:**

Consider a graph $G$ on $n = 120$ vertices with diameter $D \leq 15$. Let $S$ be a set of $k$ vertices pairwise at distance $\geq 5$.

Consider the balls $B(v_i, 2)$ for $v_i \in S$. These are disjoint. Let $b_i = |B(v_i, 2)|$. Then $\sum b_i \leq 120$.

Now, consider the "expanded" balls $B(v_i, 7)$. Since the diameter is $\leq 15$, for any vertex $u$ and any center $v_i$, $d(u, v_i) \leq 15$. In particular, every vertex is in $B(v_i, 15)$ for every $i$. But more usefully, every vertex is in $B(v_i, 7)$ for some $i$? Not necessarily.

Hmm, let me think about a covering argument. If the diameter is 15, then for any vertex $u$, $d(u, v_1) \leq 15$. But $u$ might not be within 7 of any center.

Let me try a different approach. Consider the $k$ centers. For each center $v_i$, consider the sphere $S_i = \{u : d(u, v_i) \leq 7\}$. The union of all $S_i$ covers all vertices (since for any $u$, $d(u, v_i) \leq 15 \leq 15$ for all $i$, but we need $d(u, v_i) \leq 7$ for some $i$, which isn't guaranteed).

OK this covering approach doesn't work directly.

**Let me try to think about the problem from the perspective of the "line graph" more carefully.**

Actually, I realize I should think about this more carefully. The line graph has 120 vertices. We design it. We want to maximize the number of vertices pairwise at distance $\geq 5$, subject to diameter $\leq 15$.

This is equivalent to: what is the maximum size of a "5-packing" in a graph on 120 vertices with diameter $\leq 15$?

Let me think about this as an extremal graph theory problem.

**Claim: The answer is 16.**

Hmm, let me think about why. Consider a graph with diameter 15. Take a diametral path $v_0, v_1, \ldots, v_{15}$ (length 15). Every vertex is within distance 7 of some vertex on this path (the midpoint of the path is at distance $\leq 7$ from every vertex on the path, and every vertex in the graph is within distance 7 of the path... is this true?).

Actually, in a graph with diameter 15, every vertex is within distance 15 of $v_0$. But is every vertex within distance 7 of the diametral path? Not necessarily.

Let me think about a specific extremal construction.

**Optimal construction: A "spider" with branches of length 7.**

As computed: star with center, 17 branches of length 7, total 120 vertices, diameter 14. Packing: 18 (one branch with 2 centers, 16 branches with 1 center).

Wait, the diameter is 14 (end of one branch to end of another: $7 + 7 = 14$). We need diameter $\leq 15$, so 14 is fine. ✓

Can we use branches of length 7 and one branch of length 8? $1 + 16 \cdot 7 + 8 = 1 + 112 + 8 = 121 > 120$. No.

What about 16 branches of length 7 and 1 branch of length 7: $1 + 17 \cdot 7 = 120$. ✓. Diameter 14.

What about using the diameter more fully? If we use branches of length 7 and 8: $1 + 16 \cdot 7 + 1 \cdot 8 = 121$. Too many. $1 + 15 \cdot 7 + 1 \cdot 8 = 114$. 6 vertices left. Add another branch of length 6: $114 + 6 = 120$. So 15 branches of length 7, 1 of length 8, 1 of length 6. Diameter = $8 + 7 = 15$. ✓

On the branch of length 8: can pick {3, 8} (distance 5). On branches of length 7: {7} or {2, 7}. On the branch of length 6: {6} or {1, 6}.

Cross-branch distances: 3 (from length-8 branch) + 1 (from length-6 branch) = 4 < 5. ✗. So if we use 3 on the length-8 branch, we can't use 1 on the length-6 branch.

Let me try: length-8 branch: {8} (just the end). Length-7 branches: {7} on each. Length-6 branch: {6}. Cross: 8+7=15, 8+6=14, 7+6=13, 7+7=14. All ≥ 5. ✓. Total: 1 + 15 + 1 = 17. Worse than 18.

Try: length-8 branch: {3, 8}. Length-7 branches: {7} on each. Length-6 branch: {6}. Cross: 3+7=10, 3+6=9, 3+8=5 (same branch), 8+7=15, 8+6=14, 7+6=13, 7+7=14. All ≥ 5. ✓. Total: 2 + 15 + 1 = 18. Same as before.

Try: length-8 branch: {3, 8}. Length-7 branches: {7} on 14, {2, 7} on 1. Length-6 branch: {6}. Cross: 3+2=5 ✓, 2+6=8 ✓, 2+7=9 ✓, 3+6=9 ✓, 3+7=10 ✓, 8+6=14 ✓, 8+7=15 ✓, 7+6=13 ✓, 7+7=14 ✓, 2+8=10 ✓. All ≥ 5. ✓. Total: 2 + 14 + 2 + 1 = 19!

Wait, let me double-check. We have:
- Length-8 branch: vertices at distances 1-8 from center. Selected: {3, 8}.
- One length-7 branch: selected {2, 7}.
- 14 length-7 branches: selected {7} each.
- Length-6 branch: selected {6}.

Cross-branch pairs:
- 3 and 2: 3+2=5 ✓
- 3 and 7: 3+7=10 ✓
- 3 and 6: 3+6=9 ✓
- 8 and 2: 8+2=10 ✓
- 8 and 7: 8+7=15 ✓
- 8 and 6: 8+6=14 ✓
- 2 and 7: 2+7=9 ✓
- 2 and 6: 2+6=8 ✓
- 7 and 6: 7+6=13 ✓
- 7 and 7: 7+7=14 ✓

Same-branch pairs:
- 3 and 8: |8-3|=5 ✓
- 2 and 7: |7-2|=5 ✓

All pairs satisfy distance ≥ 5. ✓

Total centers: 2 + 2 + 14 + 1 = 19. 

Can we push to 20? We'd need another branch with 2 centers. We already have two branches with 2 centers (length-8 with {3,8} and length-7 with {2,7}). The "small" elements are 3 and 2. 3+2=5 ✓. Can we add a third branch with 2 centers?

On a length-7 branch, the 2-center options are {1,6}, {1,7}, {2,7}. The small elements are 1 or 2.
- If small is 1: 1+2=3 < 5 ✗ (conflicts with existing 2). 1+3=4 < 5 ✗ (conflicts with existing 3).
- If small is 2: 2+2=4 < 5 ✗ (conflicts with existing 2). 2+3=5 ✓ (OK with 3).

So we can't add a third 2-center branch because the small element would conflict.

What if we change the configuration? Use {3, 8} on length-8, {3, 8} on... wait, we only have one length-8 branch.

What if we use two length-8 branches? $1 + 2 \cdot 8 + \text{rest} = 1 + 16 + \text{rest} = 17 + \text{rest} \leq 120$. Rest = 103, with length-7 branches: $103 / 7 = 14.7...$, so 14 branches of length 7 (98 vertices) and 5 left over. $17 + 98 + 5 = 120$. The 5 leftover could be a branch of length 5.

Diameter: $8 + 8 = 16 > 15$. ✗! Two branches of length 8 give diameter 16.

So we can't have two branches of length 8. What about one length-8 and one length-7, with the length-7 having 2 centers?

We already did that: 19 centers. Let me see if there's a completely different structure that does better.

**What about a non-star tree?**

Consider a tree where the center is not a single vertex but a path. For example, a path $c_0, c_1, c_2$ (length 2) as the "core," with branches hanging off $c_0, c_1, c_2$.

The diameter would be the longest path between two leaf vertices. If a branch of length $a$ hangs off $c_0$ and a branch of length $b$ hangs off $c_2$, the distance is $a + 2 + b$. For diameter $\leq 15$: $a + b \leq 13$.

This is more flexible but also more complex. Let me think about whether it helps.

Actually, the key constraint is: the diameter is $\leq 15$, and we want to pack centers at pairwise distance $\geq 5$. The star with branches of length 7 gives diameter 14 and packing 18-19. Can we do better?

Let me think about an upper bound.

**Upper bound attempt:**

Consider a graph $G$ on 120 vertices with diameter $\leq 15$. Let $S$ be a set of $k$ vertices pairwise at distance $\geq 5$.

Consider the balls $B(v, 2)$ for $v \in S$. These are disjoint. The total number of vertices in these balls is $\sum_{v \in S} |B(v, 2)| \leq 120$.

Now, I claim that $|B(v, 2)| \geq 3$ for each $v \in S$ (assuming the graph is connected and $v$ is not a leaf of degree 1... actually, $v$ could be a leaf).

Hmm, in the star construction, the centers at the ends of branches are leaves (degree 1). $|B(v, 2)|$ for a leaf at the end of a branch of length 7: the ball of radius 2 includes the leaf, its neighbor, and the neighbor's neighbor. So $|B(v, 2)| = 3$. For a center at distance 2 from the star center (on a branch), $|B(v, 2)|$ includes: $v$, its neighbors (the star center and the next vertex on the branch), and their neighbors. The star center has degree 17, so $|B(v, 2)| \geq 1 + 2 + 16 = 19$ (roughly). 

So the ball sizes vary. The total $\sum |B(v, 2)| \leq 120$ gives $k \leq 120 / \min |B(v, 2)|$. If some centers have small balls (size 3), this gives $k \leq 40$, which is not tight.

Let me think about a better upper bound.

**Upper bound using the diameter:**

Consider the $k$ centers $v_1, \ldots, v_k$. For any two centers $v_i, v_j$, $5 \leq d(v_i, v_j) \leq 15$.

Consider the "metric space" on the $k$ centers. The diameter of this space is $\leq 15$, and the minimum distance is $\geq 5$.

Now, consider the balls of radius 2 in the original graph. These are disjoint. The ball $B(v_i, 2)$ has $|B(v_i, 2)|$ vertices. 

The key observation: the ball $B(v_i, 7)$ must contain all vertices within distance 7 of $v_i$. Since the diameter is $\leq 15$, for any vertex $u$ and any center $v_i$, $d(u, v_i) \leq 15$. But $u$ might not be in $B(v_i, 7)$.

However, consider the following: for any vertex $u$, $u$ is in $B(v_i, 15)$ for all $i$. Also, $u$ is in $B(v_i, 7)$ for some $i$? Not necessarily.

Let me try a volume argument. The ball $B(v_i, 7)$ has some size. The balls $B(v_i, 2)$ are disjoint and contained in $B(v_i, 7)$. The "annulus" $B(v_i, 7) \setminus B(v_i, 2)$ has size $|B(v_i, 7)| - |B(v_i, 2)|$.

Hmm, I don't think this leads to a clean bound without more information about the graph structure.

**Let me try a different approach: think about the problem in terms of the "line graph" and use a known result.**

Actually, let me reconsider the problem. The problem says "120 underground lines" and asks for the "maximum number of pairwise distant stations." I've been assuming each station is on exactly one line, which seems right for maximizing distant stations.

But wait—I should also consider that the line graph might not need to have diameter exactly 15. The condition is that the diameter is $\leq 15$. And we want to maximize the 5-packing.

Let me think about the problem as: what is the maximum $k$ such that there exists a graph on 120 vertices with diameter $\leq 15$ and a 5-packing of size $k$?

**Let me try to construct a graph that achieves more than 19.**

**Idea: Use a graph that is not a tree.**

In a tree, the distance between two vertices is the unique path length. In a non-tree, distances can be shorter. But we want distances between centers to be $\geq 5$, so shorter distances are bad. However, non-tree edges can reduce the diameter without affecting the distances between centers (if the extra edges are between non-center vertices).

Wait, but adding edges can only decrease distances. So if we have a tree with diameter 14 and packing 19, adding edges would decrease the diameter (good, but we're already $\leq 15$) and potentially decrease distances between centers (bad).

So for a given packing, the tree is the best (maximizes distances). And for a given diameter, the tree is also good (it has the largest diameter for a given structure, so it gives the most "room" for packing).

Hmm, but actually, a non-tree might allow a different structure that's better. Let me think...

**Idea: Use a graph with a "hub" structure.**

Consider a graph with a central clique $C$ of size $c$, and $m$ "arms" emanating from the clique. Each arm is a path of length $L$ starting from a vertex in $C$. The diameter is $2L$ (end of one arm to end of another, going through the clique). We need $2L \leq 15$, so $L \leq 7$.

Total vertices: $c + mL \leq 120$ (the clique vertices plus the arm vertices; but the first vertex of each arm is in the clique, so actually $c + m(L-1) \leq 120$? No, let me be more careful.)

Actually, let me model it as: the clique $C$ has $c$ vertices. Each arm is a path of length $L$ (i.e., $L$ edges, $L+1$ vertices including the starting vertex in $C$). So each arm adds $L$ new vertices. Total: $c + mL \leq 120$.

The diameter is $2L$ (end of one arm to end of another). Need $2L \leq 15$, so $L \leq 7$.

Packing: similar to the star case. On each arm (path of length $L$ from the clique), we can place centers. The distance between a center at distance $a$ from the clique (on one arm) and a center at distance $b$ from the clique (on another arm) is $a + b$ (go through the clique). The distance between two centers on the same arm is $|a - b|$.

This is the same as the star case! The clique doesn't help because the distance through the clique is $a + b$, same as through a single center vertex.

So the clique version gives the same packing as the star version. The only difference is that the clique uses more vertices for the center, leaving fewer for arms. So the star (clique of size 1) is better.

**Idea: Use a "path of cliques" (blow-up of a path).**

As I considered earlier: a path of $d+1$ groups, each a clique of size $s$, with complete bipartite between consecutive groups. Diameter $d$, total vertices $s(d+1)$.

With $d = 15$, $s = 8$ (using $8 \times 16 = 128 > 120$). Hmm, $s = 7$, $7 \times 16 = 112 \leq 120$. Or $d = 14$, $s = 8$, $8 \times 15 = 120$. ✓

Packing: pick groups at distance $\geq 5$, one vertex per group. $\lfloor 14/5 \rfloor + 1 = 3$.

That's much worse than 19. The blow-up wastes vertices.

**Idea: Use a graph that's a tree but not a star.**

Consider a "binary tree" of depth $h$. The diameter is $2h$. Need $2h \leq 15$, so $h \leq 7$. A full binary tree of depth 7 has $2^8 - 1 = 255$ vertices, way more than 120. A binary tree of depth 7 with fewer vertices...

Actually, the depth-7 binary tree has too many vertices. Let me think about a "thin" binary tree.

In a binary tree of depth 7, the leaves are at depth 7. The distance between two leaves is at most 14 (through the root). We can pick leaves that are pairwise at distance $\geq 5$. The distance between two leaves is $14 - 2 \cdot \text{LCA depth}$ (where LCA is the lowest common ancestor). For distance $\geq 5$: $14 - 2d \geq 5$, so $d \leq 4.5$, i.e., LCA depth $\leq 4$.

Hmm, this is getting complicated. Let me think about it differently.

**Let me think about the problem as an optimization over trees.**

We want a tree $T$ on 120 vertices with diameter $\leq 15$ that maximizes the 5-packing number.

The 5-packing number of a tree is the maximum number of vertices pairwise at distance $\geq 5$.

For a tree, the packing is related to the structure. Let me think about what tree maximizes this.

**Key insight: In a tree, the 5-packing is maximized by a "subdivision" of a star.**

A star with $d$ branches of length $L$ has:
- Diameter $2L$.
- $1 + dL$ vertices.
- 5-packing: as computed, roughly $d + 1$ (one "extra" center on one branch).

To maximize $d + 1$ with $1 + dL \leq 120$ and $2L \leq 15$:
- $L = 7$: $d \leq 119/7 = 17$, packing $\leq 18$.
- $L = 7$, $d = 17$: packing 18 (or 19 with mixed branch lengths as shown).

Can we do better with $L = 7$ and a different tree structure?

**What about a "double star" (two centers connected by a path, with branches on each)?**

Consider two "hubs" $h_1, h_2$ connected by a path of length $p$. From $h_1$, there are $d_1$ branches of length $L_1$. From $h_2$, there are $d_2$ branches of length $L_2$. The diameter is $L_1 + p + L_2$ (end of a branch on $h_1$ to end of a branch on $h_2$). Need $L_1 + p + L_2 \leq 15$.

Also, the distance between two ends of branches on the same hub is $2L_i$ (through the hub). Need $2L_1 \leq 15$ and $2L_2 \leq 15$.

Total vertices: $1 + d_1 L_1 + p + d_2 L_2$ (hubs are $h_1$ and $h_2$, with $p-1$ intermediate vertices on the path, plus $d_1 L_1 + d_2 L_2$ branch vertices). Wait, let me be more careful. $h_1$ and $h_2$ are connected by a path of length $p$ (so $p+1$ vertices including both hubs). From $h_1$, $d_1$ branches of length $L_1$ (each adding $L_1$ new vertices). From $h_2$, $d_2$ branches of length $L_2$ (each adding $L_2$ new vertices). Total: $(p+1) + d_1 L_1 + d_2 L_2 \leq 120$.

Packing: 
- Centers on branches of $h_1$: pairwise distance $\geq 5$ as before.
- Centers on branches of $h_2$: similarly.
- Cross: a center at distance $a$ from $h_1$ (on a branch of $h_1$) and a center at distance $b$ from $h_2$ (on a branch of $h_2$): distance $= a + p + b$. Need $a + p + b \geq 5$.

If $p \geq 5$, then $a + p + b \geq 5$ always. So the two sides are independent! Each side is like a star with branches of length $L_i$ and diameter $2L_i \leq 15$.

With $p = 5$, $L_1 = L_2 = 5$ (so $L_1 + p + L_2 = 15$ ✓, $2L_1 = 10 \leq 15$ ✓):
- Total: $6 + 5d_1 + 5d_2 \leq 120$, so $d_1 + d_2 \leq 22$.
- Packing on each side: $d_i + 1$ (with the extra center trick).
- Total packing: $(d_1 + 1) + (d_2 + 1) = d_1 + d_2 + 2 \leq 24$.

Wait, that's much better than 19! Let me verify.

With $p = 5$, $L_1 = L_2 = 5$:
- $h_1$ side: $d_1$ branches of length 5. On each branch, we can pick the endpoint (distance 5 from $h_1$). Cross-branch: $5 + 5 = 10 \geq 5$ ✓. On one branch, we can also pick the vertex at distance 0 from $h_1$... wait, $h_1$ is the hub, not on a branch. Let me reconsider.

On a branch of length 5 from $h_1$: vertices at distances 1, 2, 3, 4, 5 from $h_1$. We can pick {5} (the endpoint) or {1, 6}... wait, the branch has length 5, so vertices at distances 1-5. Pairs at distance $\geq 5$: (1, 6) - but 6 doesn't exist. So only single vertices per branch, or... 

Actually, on a path of length 5 (vertices at distances 1, 2, 3, 4, 5 from hub), the maximum 2-element set at distance $\geq 5$ is... distance between distance-1 and distance-5 is 4 < 5. So no 2-element set! We can only pick 1 per branch.

Hmm, so with $L = 5$, each branch contributes at most 1 center. And the "extra center" trick doesn't work because we can't fit 2 centers on a branch of length 5.

So packing on $h_1$ side: $d_1$ (one per branch). Similarly $h_2$ side: $d_2$. Total: $d_1 + d_2 \leq 22$.

But wait, can we also use the path vertices (between $h_1$ and $h_2$) as centers? The path has vertices $h_1, p_1, p_2, p_3, p_4, h_2$ (length 5). A path vertex $p_i$ is at distance $i$ from $h_1$ and $5-i$ from $h_2$. 

A center on a branch of $h_1$ at distance $a$ from $h_1$ and a path vertex at distance $j$ from $h_1$: distance $= a + j$. Need $a + j \geq 5$. If $a = 5$ (endpoint), $j \geq 0$, always ✓. If $a = 1$, $j \geq 4$.

A center on a branch of $h_2$ at distance $b$ from $h_2$ and a path vertex at distance $j$ from $h_1$ (so $5-j$ from $h_2$): distance $= b + (5-j)$. Need $b + 5 - j \geq 5$, so $b \geq j$. If $b = 5$, $j \leq 5$, always ✓.

Two path vertices at distances $j_1, j_2$ from $h_1$: distance $= |j_1 - j_2|$. Need $\geq 5$. On a path of length 5 (6 vertices), max set at pairwise distance $\geq 5$: {0, 5} (i.e., $h_1$ and $h_2$), size 2. But $h_1$ is the hub, and using it as a center: distance to a branch endpoint at distance 5 from $h_1$ is 5 ✓. Distance to a branch endpoint at distance 5 from $h_2$ is $5 + 5 = 10$ ✓.

So we could use $h_1$ and $h_2$ as centers, plus the branch endpoints. But $h_1$ is at distance 0 from itself, and a branch endpoint at distance 5 from $h_1$ is at distance 5 from $h_1$ ✓. And $h_1$ and $h_2$ are at distance 5 ✓.

So: $h_1, h_2$ as centers, plus $d_1$ endpoints on $h_1$'s branches, plus $d_2$ endpoints on $h_2$'s branches. Total: $2 + d_1 + d_2 \leq 2 + 22 = 24$.

But wait, I need to check: $h_1$ and a branch endpoint on $h_1$ at distance 5: distance = 5 ✓. $h_1$ and a branch endpoint on $h_2$ at distance 5: distance = 5 + 5 = 10 ✓. $h_2$ and a branch endpoint on $h_1$: 5 + 5 = 10 ✓. $h_2$ and a branch endpoint on $h_2$: 5 ✓. Two branch endpoints on $h_1$: 5 + 5 = 10 ✓. Two branch endpoints on $h_2$: 10 ✓. Cross: 5 + 5 + 5 = 15 ✓. $h_1$ and $h_2$: 5 ✓.

All pairwise distances $\geq 5$ ✓. Total: $2 + d_1 + d_2 = 2 + 22 = 24$.

That's much better than 19! Let me verify the total vertex count: $(p+1) + d_1 L_1 + d_2 L_2 = 6 + 5 \cdot 11 + 5 \cdot 11 = 6 + 55 + 55 = 116 \leq 120$ ✓. (With $d_1 = d_2 = 11$.)

Actually, $d_1 + d_2 \leq (120 - 6) / 5 = 114 / 5 = 22.8$, so $d_1 + d_2 \leq 22$. With $d_1 = d_2 = 11$: $6 + 55 + 55 = 116$. 4 vertices unused. Could we use them? Add a branch of length 4 to one hub: $d_1 = 12, d_2 = 11$, but one branch has length 4. $6 + 5 \cdot 11 + 4 \cdot 1 + 5 \cdot 11 = 6 + 55 + 4 + 55 = 120$. Wait, that's 12 branches on $h_1$ (11 of length 5, 1 of length 4) and 11 branches on $h_2$ (all length 5). Total: $6 + 59 + 55 = 120$. ✓

On the length-4 branch: endpoint at distance 4 from $h_1$. Distance to $h_1$: 4 < 5. ✗! So we can't use the endpoint of the length-4 branch as a center (too close to $h_1$). 

Hmm, but we could use a different vertex on the length-4 branch. Actually, the only vertex at distance $\geq 5$ from $h_1$ on a branch of length 4 is... none (max distance is 4). So the length-4 branch doesn't contribute a center. But it does use up 4 vertices. Not helpful.

Alternatively, use $d_1 = 11, d_2 = 11$, and 4 unused vertices. Or find a way to use them.

Actually, we could add a branch of length 4 to $h_1$ and use the vertex at distance 4 from $h_1$ on this branch. Its distance to $h_2$ is $4 + 5 = 9 \geq 5$ ✓. Its distance to a branch endpoint on $h_2$ is $4 + 5 + 5 = 14 \geq 5$ ✓. Its distance to a branch endpoint on $h_1$ (at distance 5) is $4 + 5 = 9 \geq 5$ ✓. Its distance to $h_1$ is 4 < 5 ✗.

So if we don't use $h_1$ as a center, we can use the length-4 branch endpoint. Then we have: $d_1 + d_2 + 1$ (the extra from length-4 branch) + 1 (h_2) = 11 + 11 + 1 + 1 = 24. Same as before (we lose $h_1$ but gain the length-4 endpoint).

Or: don't use $h_1$ or $h_2$, but use the length-4 branch endpoint. $d_1 + 1 + d_2 = 11 + 1 + 11 = 23$. Worse.

So 24 seems to be the max with this structure. But can we do even better with a different structure?

**Generalization: "Multi-hub" structure.**

Consider $m$ hubs connected by a path of length $p$ between consecutive hubs. From each hub, branches of length $L$. The diameter is $L + (m-1)p + L = 2L + (m-1)p$. Need $2L + (m-1)p \leq 15$.

If $p \geq 5$, centers on different hubs' branches are automatically at distance $\geq 5$ (since the path between hubs is $\geq 5$). Actually, the distance between a branch endpoint on hub $i$ and a branch endpoint on hub $j$ is $L + |i-j| \cdot p + L = 2L + |i-j| \cdot p$. For $|i-j| = 1$: $2L + p \geq 5$ (easily satisfied). For the same hub: $2L \geq 5$, so $L \geq 3$.

Also, the hub itself can be a center if it's at distance $\geq 5$ from all other centers. The hub is at distance $L$ from its branch endpoints, so $L \geq 5$ for the hub to be a center alongside its branch endpoints. Or $L < 5$ and we don't use the hub.

Let me try $m = 3$ hubs, $p = 5$, $L = 3$. Diameter: $2 \cdot 3 + 2 \cdot 5 = 16 > 15$. ✗.

$m = 3$, $p = 5$, $L = 2$: Diameter $= 4 + 10 = 14 \leq 15$ ✓. But $L = 2$: branch endpoints at distance 2 from hub. Same-hub: $2 + 2 = 4 < 5$ ✗. So we can only pick 1 endpoint per hub. And the hub itself: distance to endpoint = 2 < 5 ✗. So we can pick the hub or one endpoint per hub. 

With $L = 2$, $m = 3$, $p = 5$: total vertices = $(2 \cdot 5 + 1) + 3 \cdot d \cdot 2 = 11 + 6d \leq 120$, $d \leq 18$. Centers: 3 (one per hub, either the hub or an endpoint). Plus, can we use path vertices? Path vertices between hub $i$ and hub $i+1$ at distance $j$ from hub $i$: distance to hub $i$ is $j$, to hub $i+1$ is $5-j$. For a path vertex to be a center, it needs to be at distance $\geq 5$ from all other centers.

This is getting complicated. Let me try to find the optimal structure more systematically.

**Optimization over the multi-hub structure:**

We have $m$ hubs on a path, with spacing $p$ (path length between consecutive hubs). From each hub, $d_i$ branches of length $L$. 

Diameter: $2L + (m-1)p \leq 15$.
Total vertices: $(m-1)p + 1 + L \sum d_i \leq 120$. (The path has $(m-1)p + 1$ vertices, and each branch adds $L$ vertices.)

Centers: 
- If $L \geq 5$: can use hub and endpoints. Each hub contributes $d_i + 1$ centers (endpoints + hub). But hubs on the path are at distance $p$ from each other. Need $p \geq 5$ for hubs to be pairwise at distance $\geq 5$.
  - If $p \geq 5$: all centers across hubs are pairwise at distance $\geq 5$ (hub-to-hub: $p \geq 5$; endpoint-to-endpoint same hub: $2L \geq 10 \geq 5$; endpoint-to-endpoint different hubs: $2L + p \geq 15$; hub-to-endpoint same hub: $L \geq 5$; hub-to-endpoint different hubs: $L + p \geq 10$). Total: $\sum (d_i + 1) = \sum d_i + m$.
  - Constraint: $2L + (m-1)p \leq 15$ and $(m-1)p + 1 + L \sum d_i \leq 120$.
  - Maximize $\sum d_i + m$.
  
  With $L = 5$, $p = 5$: $2 \cdot 5 + (m-1) \cdot 5 \leq 15$, so $10 + 5(m-1) \leq 15$, $5m \leq 10$, $m \leq 2$. So $m = 2$, back to the previous case. Total: $\sum d_i + 2$, with $5 + 1 + 5 \sum d_i \leq 120$, $\sum d_i \leq 22$. Total: 24.

  With $L = 5$, $p = 5$, $m = 2$: as before, 24.

  With $L = 6$, $p = 3$: $12 + 3(m-1) \leq 15$, $3(m-1) \leq 3$, $m \leq 2$. $m = 2$: diameter $= 12 + 3 = 15$ ✓. But $p = 3 < 5$, so hubs are at distance 3 < 5. Can't use both hubs as centers. 
  
  With $p = 3$, hubs at distance 3. If we use hub 1 as a center, hub 2 can't be a center (distance 3 < 5). But endpoints on hub 2 are at distance $6 + 3 = 9$ from hub 1 ✓. So: hub 1 + endpoints on hub 1 ($d_1$) + endpoints on hub 2 ($d_2$). Total: $1 + d_1 + d_2$. Constraint: $3 + 1 + 6(d_1 + d_2) \leq 120$, $d_1 + d_2 \leq 19$. Total: 20. Worse than 24.

  With $L = 7$, $p = 1$: $14 + (m-1) \leq 15$, $m \leq 2$. $m = 2$: diameter 15. $p = 1$: hubs at distance 1. Can use at most one hub. Endpoints on hub 1 at distance 7, endpoints on hub 2 at distance 7, cross: $7 + 1 + 7 = 15$ ✓. Hub 1 + $d_1$ + $d_2$: $1 + d_1 + d_2$. Constraint: $1 + 1 + 7(d_1 + d_2) \leq 120$, $d_1 + d_2 \leq 16$. Total: 17. Worse.

So $L = 5, p = 5, m = 2$ giving 24 seems good. Can we beat it?

**What about $L = 5, p = 5, m = 2$ but also using path vertices as centers?**

The path between hubs has vertices at distances 0, 1, 2, 3, 4, 5 from hub 1 (i.e., hub 1, $p_1, p_2, p_3, p_4$, hub 2). We're already using hub 1 and hub 2 as centers. Can we also use $p_1, p_2, p_3, p_4$?

$p_1$ is at distance 1 from hub 1 < 5 ✗. So no path vertex (other than the hubs) can be a center.

What if we don't use the hubs but use path vertices? $p_0 = $ hub 1, $p_5 = $ hub 2. Path vertices at distances 0-5 from hub 1. Pairwise at distance $\geq 5$: {0, 5} only. So 2 path centers. Plus branch endpoints: $d_1 + d_2$. But a path center at distance 0 (hub 1) and a branch endpoint at distance 5 from hub 1: distance 5 ✓. A path center at distance 5 (hub 2) and a branch endpoint at distance 5 from hub 2: distance 5 ✓. A path center at distance 0 and a branch endpoint at distance 5 from hub 2: distance 10 ✓.

So it's the same: 2 + $d_1 + d_2 = 24$.

**Can we use a longer path between hubs to fit more path centers?**

With $p = 10$, $L = 2$: diameter $= 4 + 10 = 14$ ✓. $m = 2$. Path has 11 vertices. Path centers at pairwise distance $\geq 5$: {0, 5, 10}, size 3. But $L = 2$: branch endpoints at distance 2 from hub. Hub-to-endpoint: 2 < 5 ✗. So can't use hubs and endpoints together. 

If we use path centers {0, 5, 10} (which are hub 1, middle, hub 2): 
- Hub 1 (distance 0) and branch endpoint on hub 1 (distance 2): distance 2 < 5 ✗.
- Middle (distance 5 from hub 1) and branch endpoint on hub 1 (distance 2): distance 7 ✓.
- Middle and branch endpoint on hub 2 (distance 2 from hub 2 = distance 8 from hub 1): distance 3 < 5 ✗.

Hmm, so the middle path vertex is at distance 7 from hub 1's endpoints but distance 3 from hub 2's endpoints. Not good.

Let me try: use path centers {0, 5, 10} and no branch endpoints. Total: 3. Plus, can we add branch endpoints that are far enough from all path centers?

A branch endpoint on hub 1 at distance 2 from hub 1: distance to path center 0 = 2 < 5 ✗. Distance to path center 5 = 7 ✓. Distance to path center 10 = 12 ✓. But distance to 0 is 2, so can't use it.

A branch endpoint on hub 2 at distance 2 from hub 2: distance to path center 10 = 2 < 5 ✗.

So with path centers {0, 5, 10}, we can't use any branch endpoints. Total: 3. Much worse.

What if we use path centers {5} only (the middle)? Then branch endpoints on hub 1 at distance 2: distance to middle = 7 ✓. Branch endpoints on hub 2 at distance 2: distance to middle = 3 < 5 ✗. So only hub 1's endpoints. Total: 1 + $d_1$. With $L = 2$, $p = 10$: $11 + 2d_1 + 2d_2 \leq 120$, $d_1 + d_2 \leq 54$. But we can only use $d_1$ endpoints. $1 + d_1 \leq 1 + 54 = 55$. But we also need the branch endpoints on hub 1 to be pairwise at distance $\geq 5$: $2 + 2 = 4 < 5$ ✗!

So with $L = 2$, branch endpoints on the same hub are at distance 4 < 5. Can only pick 1 per hub. Total: 1 (middle) + 1 (hub 1 endpoint) = 2. Terrible.

OK, so $L = 2$ is bad for packing. We need $L \geq 3$ for same-hub endpoints to be at distance $\geq 5$ (actually $2L \geq 5$, so $L \geq 3$).

With $L = 3$, $p = 9$: diameter $= 6 + 9 = 15$ ✓. $m = 2$. Path: 10 vertices. Same-hub endpoints: $2 \cdot 3 = 6 \geq 5$ ✓. 

Path centers: {0, 5, 9}? 0 and 5: distance 5 ✓. 5 and 9: distance 4 < 5 ✗. {0, 5}: distance 5 ✓. {0, 9}: distance 9 ✓. {0, 5, 9}: 5 and 9 too close. So max 2 path centers: {0, 9} or {0, 5} or {5, 9}.

Using {0, 9} (hubs): hub 1 and endpoint on hub 1 (distance 3): 3 < 5 ✗. So can't use hubs and their own endpoints.

Using {0, 5}: 0 is hub 1, 5 is a path vertex. Hub 1 and endpoint on hub 1: 3 < 5 ✗. Path vertex 5 and endpoint on hub 1 (distance 3 from hub 1): 5 + 3 = 8 ✓. Path vertex 5 and endpoint on hub 2 (distance 3 from hub 2 = distance 12 from hub 1): |12 - 5| = 7 ✓. Hub 1 and endpoint on hub 2: 9 + 3 = 12 ✓. Hub 1 and path vertex 5: 5 ✓.

So: centers = {hub 1, path vertex 5} + endpoints on hub 2 ($d_2$). Check: hub 1 and hub 2 endpoint: 12 ✓. Path vertex 5 and hub 2 endpoint: 7 ✓. Hub 1 and path vertex 5: 5 ✓. Hub 2 endpoints pairwise: 6 ✓.

Total: 2 + $d_2$. Constraint: $10 + 3(d_1 + d_2) \leq 120$, $d_1 + d_2 \leq 36$. But we only use $d_2$, so set $d_1 = 0$: $10 + 3d_2 \leq 120$, $d_2 \leq 36$. Total: 2 + 36 = 38!

Wait, that's way more than 24! Let me double-check.

With $m = 2$ hubs, $p = 9$ (path of length 9 between hubs), $L = 3$ (branches of length 3 on hub 2), $d_1 = 0$ (no branches on hub 1), $d_2 = 36$ (36 branches on hub 2).

Total vertices: $(9 + 1) + 0 \cdot 3 + 36 \cdot 3 = 10 + 108 = 118 \leq 120$ ✓.

Diameter: longest path is from endpoint of a branch on hub 2 to hub 1: $3 + 9 = 12$. Or from hub 1 to hub 2: 9. Or between two endpoints on hub 2: $3 + 3 = 6$. So diameter = 12 ≤ 15 ✓.

Wait, actually, the diameter should be the longest shortest path. The longest path is from hub 1 to an endpoint on hub 2: 9 + 3 = 12. Between two endpoints on hub 2: 6. Between hub 1 and hub 2: 9. So diameter = 12. ✓

Centers: hub        — AI历史解题过程（thinking）
#   polymath_05134         — 题目ID

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
  <problem_id>polymath_05134</problem_id>
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

In a city with 120 underground lines, every station can be reached from any other station with no more than 15 changes. Two stations are considered distant if at least 5 changes are needed to travel between them. What is the maximum number of pairwise distant stations that can exist in this city?

## Standard Solution

To solve the problem, we need to determine the maximum number of pairwise distant stations in a city with 120 underground lines, where every station can be reached from any other with no more than 15 changes, and two stations are distant if at least 5 changes are required between them.

### Step-by-Step Solution:

1. **Understanding the Problem**:
   - A "change" refers to switching lines when traveling between stations.
   - The distance between two stations is the minimum number of changes required to travel between them.
   - We need a set of stations where each pair is at least 5 changes apart.

2. **Graph Representation**:
   - Model the underground network as a graph where each line is a hyperedge.
   - Stations on the same line can be reached without a change, so their distance is 0.
   - The distance between two stations on different lines is the number of changes (line switches) required.

3. **Key Insight**:
   - To maximize the number of pairwise distant stations, we need to ensure each station is part of its own line and sufficiently far from others.
   - Consider a star-like structure with a central hub and branches radiating out.

4. **Star Structure Analysis**:
   - Each branch is a path of stations connected by lines.
   - For the minimum distance requirement (5 changes), each branch must have a depth of 3 lines:
     - Hub connected to A via line 1.
     - A connected to B via line 2.
     - B connected to C via line 3.
   - Distance between endpoints of two branches: 3 (to hub) + 3 (to the other endpoint) = 6 changes, which meets the requirement.

5. **Calculations**:
   - Each branch uses 3 lines.
   - With 120 lines, the number of branches (and endpoints) is \( \frac{120}{3} = 40 \).

6. **Validation**:
   - This structure ensures all endpoints are pairwise at least 6 changes apart.
   - The diameter of the network is 6, which is within the allowed 15.

### Final Answer:
Thus, the maximum number of pairwise distant stations is \(\boxed{40}\).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a city with 120 underground lines. Every station can be reached from any other station with no more than 15 changes. Two stations are "distant" if at least 5 changes are needed to travel between them. We need to find the maximum number of pairwise distant stations.

Let me think about this in graph-theoretic terms. We have 120 "lines" and stations. A "change" means switching from one line to another. Let me think about the structure.

Let me model this. Consider a graph where lines are vertices. When two lines share a station, they are connected by an edge. A journey between two stations involves: start on some line, possibly change lines. The number of changes is the number of line switches.

Actually, let me think more carefully. A station is on some set of lines. To travel from station A to station B, you pick a line through A, ride it, possibly change to another line, etc., until you reach a line through B. The number of changes is the number of times you switch lines.

If station A is on line $l_A$ and station B is on line $l_B$, and the shortest path in the "line graph" (where lines are vertices and edges connect lines that share a station) from $l_A$ to $l_B$ has length $d$, then the number of changes needed is $d$ (if $l_A \neq l_B$) or 0 (if $l_A = l_B$).

Wait, actually if A and B are on the same line, 0 changes. If A is on line $l_1$ and B is on line $l_2$ and $l_1, l_2$ share a station, then 1 change. In general, if the shortest path in the line graph from $l_1$ to $l_2$ has $d$ edges, the number of changes is $d$.

So "distant" means the line graph distance between some line of A and some line of B is at least 5. But actually, a station can be on multiple lines. So the number of changes between station A and station B is:
$$\min_{l_A \in L(A), l_B \in L(B)} \text{dist}_{\text{line graph}}(l_A, l_B)$$
where $L(A)$ is the set of lines through station A.

Hmm, but this is getting complex. Let me think about what structure maximizes pairwise distant stations.

The constraint is: every station can be reached from any other with no more than 15 changes. This means the line graph has diameter at most 15 (roughly). Actually, more precisely, for any two stations A, B, $\min_{l_A \in L(A), l_B \in L(B)} \text{dist}(l_A, l_B) \leq 15$.

Two stations are distant if $\min_{l_A \in L(A), l_B \in L(B)} \text{dist}(l_A, l_B) \geq 5$.

We want to maximize the number of pairwise distant stations.

Let me think about this differently. Consider the line graph $G$ with 120 vertices (lines). The diameter of $G$ is at most 15 (since any two stations can be connected with at most 15 changes, and in particular, any two lines can be connected... well, not exactly, because stations might be on specific lines).

Actually, let me reconsider. The condition "every station can be reached from any other station with no more than 15 changes" means that for any two stations A, B:
$$\min_{l_A \in L(A), l_B \in L(B)} d_G(l_A, l_B) \leq 15$$

Now, for a set of pairwise distant stations, for any two stations A, B in this set:
$$\min_{l_A \in L(A), l_B \in L(B)} d_G(l_A, l_B) \geq 5$$

To maximize the number of such stations, we want to design the line graph and station placement.

Let me think about a simpler model. Suppose each station is on exactly one line. Then the number of changes between a station on line $l_1$ and a station on line $l_2$ is $d_G(l_1, l_2)$. The condition becomes: $G$ has diameter at most 15. Distant stations are on lines at distance $\geq 5$ in $G$. We want to maximize the number of lines that are pairwise at distance $\geq 5$.

Wait, but if each station is on one line, then we can have at most one station per line (otherwise two stations on the same line would have distance 0 < 5). So we want to find a set of lines that are pairwise at distance $\geq 5$ in a graph with 120 vertices and diameter $\leq 15$.

Hmm, but we could also have stations on multiple lines. Let me think about whether that helps.

If a station is on multiple lines, say lines $l_1$ and $l_2$, then its "distance" to a station on line $l_3$ is $\min(d(l_1, l_3), d(l_2, l_3))$. So being on multiple lines only makes a station closer to others, which is bad for being distant. So to maximize distant stations, each station should be on exactly one line.

So the problem reduces to: In a graph $G$ with 120 vertices and diameter $\leq 15$, what is the maximum size of a set of vertices that are pairwise at distance $\geq 5$?

Wait, but I need to be more careful. The condition is that every station can reach every other with at most 15 changes. If each station is on one line, this means the line graph has diameter $\leq 15$. But actually, we also need to make sure the graph is connected (which is implied by diameter being finite).

So the problem is: **What is the maximum number of vertices in a graph on 120 vertices with diameter at most 15 such that there exists a set of pairwise distance-$\geq 5$ vertices of that size?**

Hmm wait, actually we want to maximize the size of such a set. We're designing the graph to maximize this. So we want to find the graph on 120 vertices with diameter $\leq 15$ that has the largest possible set of pairwise distance-$\geq 5$ vertices.

Let me think about this. If we have a set $S$ of vertices pairwise at distance $\geq 5$, and the graph has diameter $\leq 15$, then for any two vertices $u, v \in S$, $5 \leq d(u,v) \leq 15$.

Consider the "balls" of radius 2 around each vertex in $S$. Since vertices in $S$ are at distance $\geq 5$, these balls (radius 2) are disjoint. Each ball has at least 1 vertex (the center). But we need to be more careful.

Actually, let me think about it differently. Let's think about what graph structure allows the most pairwise distance-$\geq 5$ vertices while keeping diameter $\leq 15$.

Consider a path graph. If we have a path of 120 vertices, the diameter is 119, which is way more than 15. So a path doesn't work.

Consider a graph that looks like a "spider": a central vertex connected to many paths. But the diameter would be the sum of the two longest paths, which could be large.

Let me think about the Moore bound and related concepts. For a graph with diameter $D$ and maximum degree $\Delta$, the number of vertices is at most $1 + \Delta + \Delta(\Delta-1) + \ldots + \Delta(\Delta-1)^{D-1}$.

But here we want to maximize a specific set. Let me think about the structure differently.

Let me consider a graph that is a "tree-like" structure. Consider a tree where we have a root, and from the root, we have branches. The diameter is the longest path between two leaves.

Actually, let me think about this more carefully using the concept of a "packing."

If we want $k$ vertices pairwise at distance $\geq 5$, and the diameter is $\leq 15$, let me think about what constrains $k$.

Consider the open balls of radius 2 around each of the $k$ vertices. These are disjoint (since pairwise distance $\geq 5 > 2 \cdot 2 = 4$). So the total number of vertices is at least $k$ (just the centers), and at most 120.

But that only gives $k \leq 120$, which is trivial.

Let me think about the diameter constraint. The diameter is $\leq 15$. Consider two vertices $u, v \in S$ with $d(u,v) \geq 5$. There's a path of length $\leq 15$ between them. 

Hmm, let me think about this problem from a different angle. 

Consider a graph $G$ on 120 vertices with diameter $\leq 15$. We want to find the maximum $k$ such that there exist $k$ vertices pairwise at distance $\geq 5$.

Let me think about an extremal construction. 

Consider a "caterpillar" or "comb" structure. Or consider a graph that is a long path with shortcuts.

Actually, let me think about a specific construction. Consider a graph that is a path $v_1, v_2, \ldots, v_{120}$ but with additional edges to reduce the diameter. 

Alternatively, think about it as follows. We want to place $k$ "centers" on a graph of 120 vertices with diameter $\leq 15$, such that any two centers are at distance $\geq 5$.

The key insight: if we have $k$ centers pairwise at distance $\geq 5$, the balls of radius 2 around them are disjoint. Each such ball contains at least 1 vertex. But we also need the diameter to be $\leq 15$.

Let me think about a tree construction. Consider a tree $T$ with 120 vertices and diameter $\leq 15$. In a tree, the distance is unique. We want to maximize the number of vertices pairwise at distance $\geq 5$.

In a tree with diameter $D$, consider a longest path (diameter path) of length $D$. Any vertex is within distance $\lfloor D/2 \rfloor$ of some vertex on this path (the center of the tree).

Hmm, this is getting complicated. Let me think about specific constructions.

**Construction 1: A "star of paths"**

Consider a central vertex $c$. From $c$, we have $m$ paths, each of length $L$. The total number of vertices is $1 + mL$. The diameter is $2L$ (from the end of one path to the end of another). We need $2L \leq 15$, so $L \leq 7$.

On each path of length $L$ (vertices at distances $0, 1, 2, \ldots, L$ from $c$), we can place centers at distance $\geq 5$ from each other. On a path of length $L$ (with $L+1$ vertices), the maximum number of vertices pairwise at distance $\geq 5$ is $\lfloor L/5 \rfloor + 1$.

But we also need centers on different paths to be at distance $\geq 5$. The distance between a vertex at distance $a$ from $c$ on one path and a vertex at distance $b$ from $c$ on another path is $a + b$. So we need $a + b \geq 5$ for centers on different paths.

If we place centers at distance $L$ from $c$ (the ends of paths), then the distance between two such centers is $2L$. We need $2L \geq 5$, so $L \geq 3$. With $L = 7$, $2L = 14 \geq 5$. ✓

On each path of length 7 (8 vertices: $c, v_1, \ldots, v_7$), we can place centers at $v_7$ and... $v_2$ (distance 5 from $v_7$). So 2 centers per path. But wait, $v_2$ on one path and $v_7$ on another path: distance = $2 + 7 = 9 \geq 5$. ✓ And $v_2$ on two different paths: distance = $2 + 2 = 4 < 5$. ✗

So we can't place $v_2$ on multiple paths. Let me reconsider.

If we place centers only at $v_7$ (the end of each path), then each path contributes 1 center, and we need $1 + 7m \leq 120$, so $m \leq 17$. That gives 17 centers. But we might do better.

Alternatively, on each path, place centers at $v_7$ and $v_2$. But $v_2$ on different paths are at distance 4, which is too close. So we can only use $v_2$ on one path. That gives $m + 1$ centers (one $v_2$ plus $m$ endpoints), with $1 + 7m \leq 120$, so $m \leq 17$, giving 18 centers. Not much better.

What if we use paths of different lengths? Or a different structure?

**Construction 2: A path with diameter-reducing edges**

Consider a path $v_1, v_2, \ldots, v_{120}$. Add edges to reduce diameter to $\leq 15$. For instance, connect $v_i$ to $v_{i+8}$ for all valid $i$. This creates a graph where you can "skip" 8 steps at a time. The diameter would be roughly $\lceil 119/8 \rceil = 15$. 

In this graph, what's the distance between $v_i$ and $v_j$? It's roughly $\lceil |i-j|/8 \rceil$ (using the skip edges) but also the path edges give distance $|i-j|$. The actual shortest path uses a combination. With edges of length 1 and length 8, the distance is $\lceil |i-j|/8 \rceil$ if we only use skip edges... no, we need to be more careful.

Actually, with edges $v_i v_{i+1}$ and $v_i v_{i+8}$, the distance from $v_1$ to $v_{120}$ is $\min$ over paths. Using skip edges: $119 = 14 \cdot 8 + 7$, so 14 skips of 8 and 7 steps of 1, total 21 edges. That's too many.

Let me use skip edges of length 15. Connect $v_i$ to $v_{i+15}$. Then the distance from $v_1$ to $v_{120}$ is $\lceil 119/15 \rceil = 8$. But the distance between $v_1$ and $v_2$ is 1 (direct edge). The distance between $v_1$ and $v_{16}$ is 1 (skip edge). The distance between $v_1$ and $v_{17}$ is 2 ($v_1 \to v_{16} \to v_{17}$).

Hmm, but in this graph, the distance between $v_i$ and $v_j$ is roughly $\lceil |i-j|/15 \rceil$ (for large $|i-j|$) or $|i-j|$ (for small $|i-j|$, using path edges). Actually, the shortest path uses a combination of skip-15 edges and path-1 edges. The distance is $\lfloor |i-j|/15 \rfloor + (|i-j| \mod 15)$... no, that's not right either.

With edges of length 1 and length 15, the shortest path from $v_i$ to $v_j$ (with $j > i$) uses as many length-15 edges as possible, then length-1 edges. So the distance is $\lfloor (j-i)/15 \rfloor + ((j-i) \mod 15)$. For $j - i = 119$: $\lfloor 119/15 \rfloor + (119 \mod 15) = 7 + 14 = 21$. That's way more than 15.

OK so this approach of a path with skip edges doesn't easily give diameter 15. Let me think differently.

**Better approach: Think about the problem as a packing problem.**

We have a graph on 120 vertices with diameter $\leq 15$. We want to pack as many vertices as possible such that pairwise distance $\geq 5$.

The balls of radius 2 around the packed vertices are disjoint. So if each ball has size $b$, then $kb \leq 120$, giving $k \leq 120/b$.

But we also need the diameter constraint. The diameter being $\leq 15$ means the graph is "well-connected."

Let me think about what graph maximizes the packing. 

Consider a graph that is a disjoint union of cliques connected by a path-like structure. Actually, the graph must be connected (diameter is finite).

**Key idea: Use a "blow-up" of a path.**

Consider a path $P$ of length $d$ (with $d+1$ vertices). Replace each vertex of $P$ with a clique of size $s$. Connect consecutive cliques with all possible edges (complete bipartite). This gives a graph with $s(d+1)$ vertices. The diameter is $d$ (distance between a vertex in the first clique and a vertex in the last clique). 

We need $s(d+1) = 120$ and $d \leq 15$.

In this graph, the distance between a vertex in clique $i$ and a vertex in clique $j$ is $|i-j|$. So two vertices are at distance $\geq 5$ iff they are in cliques at distance $\geq 5$.

To maximize pairwise distant vertices, we pick one vertex from each clique that is at distance $\geq 5$ from all others. The maximum number of cliques pairwise at distance $\geq 5$ on a path of $d+1$ cliques is $\lfloor d/5 \rfloor + 1$.

Wait, but we can also pick multiple vertices from the same clique - no, vertices in the same clique are at distance 0 (or 1, depending on convention; in a clique, distance is 1 between distinct vertices, 0 to self). Actually, in a clique, all vertices are at distance 1 from each other. So we can pick at most 1 vertex per clique for our distant set.

Hmm wait, actually in the blow-up, vertices in the same clique are at distance... if it's a clique, they're at distance 1. So we can pick at most 1 per clique. And we need the cliques to be at distance $\geq 5$.

On a path of $d+1$ vertices (cliques), the maximum number of vertices pairwise at distance $\geq 5$ is $\lfloor d/5 \rfloor + 1$.

So we want to maximize $\lfloor d/5 \rfloor + 1$ subject to $s(d+1) = 120$, $d \leq 15$, $s \geq 1$.

To maximize $\lfloor d/5 \rfloor + 1$, we want $d$ as large as possible. With $d = 15$, we need $s \cdot 16 = 120$, so $s = 7.5$, not integer. With $d = 14$, $s \cdot 15 = 120$, $s = 8$. Then $\lfloor 14/5 \rfloor + 1 = 2 + 1 = 3$. That's only 3.

With $d = 15$, $s = 7$ (using 112 vertices, wasting 8), $\lfloor 15/5 \rfloor + 1 = 4$. Better but still small.

Hmm, this blow-up approach doesn't seem to give many centers. The issue is that the blow-up "wastes" vertices on making cliques.

**Alternative: Don't blow up. Use a sparse graph.**

If we don't blow up, we have a path of 120 vertices, but the diameter is 119, way too large. We need to add edges to reduce the diameter to 15.

**Key insight: The problem is about the trade-off between diameter and packing.**

Let me think about it as follows. We have $n = 120$ vertices, diameter $D \leq 15$, and we want to pack vertices at pairwise distance $\geq r = 5$.

There's a general bound: in a graph with $n$ vertices and diameter $D$, the maximum packing with pairwise distance $\geq r$ is at most... let me think.

Consider the $k$ packed vertices $v_1, \ldots, v_k$. The balls of radius $\lfloor (r-1)/2 \rfloor = 2$ around them are disjoint. Each ball has at least 1 vertex. So $k \leq n = 120$. That's trivial.

But the diameter constraint adds more. Consider the "metric" on the $k$ vertices. The distance between any two is between 5 and 15. 

Hmm, let me think about a different construction.

**Construction: A tree with a long spine and short branches.**

Consider a "caterpillar": a path (spine) $v_1, \ldots, v_m$ with leaves attached. The diameter is roughly $m$ (if leaves are short). To get diameter $\leq 15$, we need $m \leq 15$ (roughly). But then we only have $\sim 15$ spine vertices, and we can pack $\lfloor 15/5 \rfloor + 1 = 4$ centers on the spine. Plus leaves, but leaves are at distance 1 from the spine, so they don't help much.

This doesn't seem right. Let me reconsider.

Wait, I think I need to reconsider the problem. The diameter is at most 15, meaning the graph is quite "compact." With 120 vertices and diameter 15, the graph is relatively dense or well-structured.

Let me think about the problem from the perspective of metric spaces. We have a finite metric space (from the graph) on 120 points with diameter $\leq 15$. We want to find the maximum number of points pairwise at distance $\geq 5$.

This is a packing problem in metric spaces. The answer depends on the structure of the metric space, which we get to design (subject to being a graph metric with 120 points and diameter $\leq 15$).

**Key question: What graph metric on 120 points with diameter $\leq 15$ maximizes the 5-packing number?**

Let me think about lower and upper bounds.

**Upper bound:** Consider $k$ points pairwise at distance $\geq 5$. The open balls of radius 2 around them are disjoint. In a graph, the ball of radius 2 around a vertex of degree $d$ contains at most $1 + d + d(d-1) = 1 + d^2$ vertices. But we don't know the degree.

Actually, let me think about a different upper bound. Consider the $k$ centers. For each pair, the distance is between 5 and 15. 

Hmm, let me think about a specific construction that might be optimal.

**Construction: Complete bipartite-like structure.**

Actually, let me think about a different approach. Consider a graph that is a "thick path": a sequence of groups $G_0, G_1, \ldots, G_d$ where each group is an independent set, and edges exist only between consecutive groups (complete bipartite between $G_i$ and $G_{i+1}$). 

The diameter is $d$. The distance between a vertex in $G_i$ and a vertex in $G_j$ is $|i-j|$. Two vertices in the same group are at distance 2 (through a common neighbor in $G_{i-1}$ or $G_{i+1}$). Wait, actually, if $G_i$ and $G_{i+1}$ are completely connected, then two vertices in $G_i$ are at distance 2 (going through any vertex in $G_{i-1}$ or $G_{i+1}$). Actually, they might be at distance 2 or might not be connected through a single intermediate. Let me reconsider.

If the graph is: $G_0 - G_1 - \ldots - G_d$ with complete bipartite between consecutive groups, and no edges within groups, then:
- Distance between $u \in G_i$ and $v \in G_j$ ($i < j$): $j - i$ (go through $G_{i+1}, \ldots, G_{j-1}$, but actually you can go directly: $u \to w \in G_{i+1} \to \ldots \to v$, which takes $j - i$ steps).
- Distance between $u, v \in G_i$ ($u \neq v$): 2 (go $u \to w \in G_{i-1} \to v$ or $u \to w \in G_{i+1} \to v$), assuming $i > 0$ and $i < d$. For $i = 0$: distance is 2 (through $G_1$). For $i = d$: distance is 2 (through $G_{d-1}$).

So in this graph, the diameter is $d$ (between $G_0$ and $G_d$). We need $d \leq 15$.

For the packing: we want vertices pairwise at distance $\geq 5$. Two vertices in the same group are at distance 2, so we can pick at most 1 per group. Two vertices in groups at distance $\geq 5$ are at distance $\geq 5$. So we need to pick groups that are pairwise at distance $\geq 5$.

On a path of $d+1$ groups, the maximum number of groups pairwise at distance $\geq 5$ is $\lfloor d/5 \rfloor + 1$.

With $d = 15$: $\lfloor 15/5 \rfloor + 1 = 4$. And we need $\sum |G_i| = 120$ with $d + 1 = 16$ groups. We can make each group have $\lceil 120/16 \rceil = 8$ vertices (some 7, some 8). But we only pick 4 vertices (one from each of 4 groups at positions 0, 5, 10, 15).

That gives only 4 centers. Can we do better?

**The issue is that on a path-like structure, the packing is limited by the path length.**

Let me think about whether a non-path-like structure can do better.

**Construction: A "grid" or higher-dimensional structure.**

Consider a 2D grid. If we have an $a \times b$ grid graph, the diameter is $(a-1) + (b-1) = a + b - 2$. We need $a + b - 2 \leq 15$, so $a + b \leq 17$. The number of vertices is $ab \leq 120$.

The distance between $(i_1, j_1)$ and $(i_2, j_2)$ is $|i_1 - i_2| + |j_1 - j_2|$ (Manhattan distance). We want points pairwise at Manhattan distance $\geq 5$.

To maximize the packing, we want to maximize $a$ and $b$ subject to $a + b \leq 17$ and $ab \leq 120$ (actually $ab = 120$ or $\leq 120$). 

With $a + b = 17$: $ab$ is maximized when $a = b = 8.5$, so $a = 8, b = 9$, $ab = 72 \leq 120$. Or $a = 7, b = 10$, $ab = 70$. Or $a = 6, b = 11$, $ab = 66$. Or $a = 5, b = 12$, $ab = 60$.

Actually, we can have $ab \leq 120$, so we could have $a = 8, b = 9$ (72 vertices) or we could use more vertices. But the grid graph has $ab$ vertices, and we need $ab \leq 120$. With $a + b \leq 17$, the maximum $ab$ is $8 \times 9 = 72$, which is less than 120. So we're not using all 120 vertices.

Hmm, but we could add more vertices. Or use a different structure.

Actually, wait. We don't need to use exactly 120 vertices. We need at most 120 vertices (120 lines). Actually, re-reading the problem: "120 underground lines." So there are exactly 120 lines. Each station is on at least one line. But the number of stations is not specified.

Oh wait, I think I've been confusing "lines" and "stations." Let me re-read the problem.

"In a city with 120 underground lines, every station can be reached from any other station with no more than 15 changes. Two stations are considered distant if at least 5 changes are needed to travel between them. What is the maximum number of pairwise distant stations that can exist in this city?"

So there are 120 lines. The number of stations is not fixed. We want to maximize the number of pairwise distant stations.

A "change" is switching lines. So if I'm on line $L_1$ and I switch to line $L_2$, that's 1 change. The number of changes to go from station A to station B is the number of line switches.

Let me reconsider the model. Each station is on some set of lines. The line graph has 120 vertices (lines), with an edge between two lines if they share a station. The number of changes between station A and station B is:
$$\min_{l_A \in L(A), l_B \in L(B)} d_{\text{line graph}}(l_A, l_B)$$
where $d$ is the shortest path distance in the line graph (number of edges = number of changes).

Wait, actually, if A is on line $l_A$ and B is on line $l_B$, and $l_A = l_B$, then 0 changes. If $l_A \neq l_B$ and they share a station, then 1 change (ride $l_A$ to the shared station, switch to $l_B$, ride to B). In general, if the shortest path in the line graph from $l_A$ to $l_B$ has $d$ edges, the number of changes is $d$.

So the number of changes = distance in the line graph.

The condition "every station can reach every other with $\leq 15$ changes" means: for all stations A, B, $\min_{l_A \in L(A), l_B \in L(B)} d(l_A, l_B) \leq 15$.

"Distant" means $\min_{l_A \in L(A), l_B \in L(B)} d(l_A, l_B) \geq 5$.

Now, the line graph has 120 vertices. The number of stations is not fixed. Each station is on some subset of lines. We want to maximize the number of pairwise distant stations.

As I argued before, to maximize distant stations, each station should be on exactly one line (being on more lines only reduces distances). So each station is on exactly one line, and the number of changes between a station on line $l_1$ and a station on line $l_2$ is $d(l_1, l_2)$.

Now, the condition "every station can reach every other with $\leq 15$ changes" becomes: for any two lines $l_1, l_2$ that have stations, $d(l_1, l_2) \leq 15$. If every line has at least one station, this means the line graph has diameter $\leq 15$.

But wait, we could have some lines with no stations. If a line has no station, it still exists in the line graph (it's a vertex) but doesn't host any station. However, it could still serve as an intermediate line for connections. Hmm, but if a line has no stations, can you ride on it? You need to board at a station. If a line has no stations, you can't board it, so it's useless for travel. But it could still be a vertex in the line graph if it shares stations with other lines... but it has no stations, so it doesn't share stations with anyone, so it's isolated. That doesn't help.

Actually, let me reconsider. A line is a route with stations on it. Every line has stations (otherwise it's not really a line). But we get to design the system. We have 120 lines, and we design which stations are on which lines, and which lines share stations.

So the line graph has 120 vertices. We design the edges (by placing stations at intersections of lines). We also design which stations are on which lines (each station is on some subset of lines). We want to maximize the number of pairwise distant stations.

As argued, each station should be on exactly one line. So we place some number of stations, each on a single line. Two stations on the same line are at distance 0 (no changes needed). So for pairwise distant stations, we need at most 1 station per line, and the lines must be pairwise at distance $\geq 5$ in the line graph.

Wait, but we could also have "dummy" stations on lines that are not in our distant set, just to create intersections between lines (i.e., to create edges in the line graph). These dummy stations are on multiple lines (to create edges), but they're not part of our distant set.

So the setup is:
- Line graph $G$ on 120 vertices, which we design.
- We pick a set $S$ of lines, pairwise at distance $\geq 5$ in $G$.
- We place one station on each line in $S$ (on exactly that line).
- We place additional "intersection stations" on pairs of lines to create edges in $G$.
- The diameter of $G$ must be $\leq 15$ (so that any two stations can be connected with $\leq 15$ changes).
- We want to maximize $|S|$.

Wait, but the diameter condition: for any two stations A, B, the number of changes is $\leq 15$. If A is on line $l_A \in S$ and B is on line $l_B \in S$, then $d_G(l_A, l_B) \leq 15$. Since $S$ is a subset of lines, and we need all pairs in $S$ to have $d_G \leq 15$, but also any station (including intersection stations) to any other station. An intersection station on lines $l_1, l_2$ and a station on line $l_3$: the number of changes is $\min(d(l_1, l_3), d(l_2, l_3)) \leq 15$. Since the intersection station is on $l_1$ and $l_2$, and $l_1, l_2$ are adjacent in $G$ (they share a station), $d(l_1, l_3) \leq d(l_2, l_3) + 1$ and vice versa. So if the diameter of $G$ is $\leq 15$, then any station can reach any other with $\leq 15$ changes (since the station is on some line, and the distance in $G$ to any other line is $\leq 15$).

Actually, we need to be a bit more careful. The diameter of $G$ being $\leq 15$ means any two lines are at distance $\leq 15$. Then any two stations (each on at least one line) can be connected with $\leq 15$ changes. ✓

So the problem reduces to: **Design a graph $G$ on 120 vertices with diameter $\leq 15$, and find the maximum $|S|$ where $S$ is a set of vertices pairwise at distance $\geq 5$.**

And we want to maximize $|S|$ over all such graphs $G$.

Now, this is a cleaner problem. Let me think about it.

**Upper bound approach:**

Consider $k$ vertices pairwise at distance $\geq 5$ in a graph on 120 vertices with diameter $\leq 15$. 

The open balls of radius 2 around the $k$ vertices are disjoint. Each ball contains at least 1 vertex (the center). So $k \leq 120$.

But we can get a better bound using the diameter constraint. Consider the $k$ centers $v_1, \ldots, v_k$. For each pair $(v_i, v_j)$, $5 \leq d(v_i, v_j) \leq 15$.

Consider the ball of radius 7 around each center. Since the diameter is $\leq 15$, every vertex is within distance 7 of some center (because for any vertex $u$ and any center $v_i$, $d(u, v_i) \leq 15$, so $d(u, v_i) \leq 15$; but we need $d(u, v_i) \leq 7$ for some $i$).

Hmm, that's not necessarily true. Let me think again. If $u$ is a vertex and $v_1$ is a center, $d(u, v_1) \leq 15$. But we need $d(u, v_i) \leq 7$ for some $i$. This isn't guaranteed.

Let me try a different approach. Consider the balls of radius 2 around the $k$ centers. These are disjoint. The total number of vertices in these balls is $\sum_{i=1}^k |B(v_i, 2)|$. Since the balls are disjoint and contained in the 120 vertices, $\sum |B(v_i, 2)| \leq 120$.

Now, what's the minimum size of $B(v, 2)$? It's at least 1 (just the center). But if the graph has diameter $\leq 15$ and 120 vertices, the graph must be reasonably connected, so balls might be larger.

Actually, the minimum ball size depends on the degree. A vertex of degree 1 has $|B(v, 2)| \geq 1 + 1 + (\text{neighbors of the neighbor}) \geq 3$. A vertex of degree 0 is isolated, but then the graph isn't connected.

Hmm, this approach gives $k \leq 120 / \min |B(v,2)|$, but the minimum ball size could be small.

Let me think about this differently.

**Better upper bound using the diameter:**

Consider the $k$ centers. Pick any center $v_1$. Every other vertex is within distance 15 of $v_1$. The other centers are at distance $\geq 5$ from $v_1$. So the other $k-1$ centers are in the annulus $\{u : 5 \leq d(v_1, u) \leq 15\}$.

Now, the balls of radius 2 around the $k-1$ other centers are disjoint and contained in the annulus $\{u : 3 \leq d(v_1, u) \leq 15\}$ (since a center at distance $\geq 5$ from $v_1$ has its ball of radius 2 at distance $\geq 3$ from $v_1$). Wait, that's not quite right. The ball of radius 2 around a center at distance $d$ from $v_1$ includes vertices at distance $d-2$ to $d+2$ from $v_1$. Since $d \geq 5$, the closest vertex in the ball to $v_1$ is at distance $d - 2 \geq 3$.

But the ball could also extend beyond distance 15 from $v_1$. However, since the diameter is 15, all vertices are within distance 15 of $v_1$. So the ball is contained in $\{u : 3 \leq d(v_1, u) \leq 15\}$.

The number of vertices in this annulus is at most 120 - |B(v_1, 2)|. But this doesn't directly give a good bound.

Let me try yet another approach.

**Approach: Think about it as a metric embedding problem.**

We have $k$ points with pairwise distances in $[5, 15]$. We want to embed them into a graph metric on 120 points with diameter 15. The graph metric must be a valid graph metric (integer distances, triangle inequality, etc.).

The question is: what's the maximum $k$?

**Construction attempt: Use a tree.**

Consider a tree $T$ on 120 vertices with diameter $\leq 15$. We want to maximize the number of vertices pairwise at distance $\geq 5$.

In a tree, the distance is the unique path length. Let's think about what tree maximizes this.

Consider a "star" with a center and many branches. The center is connected to $d$ branches, each of length $L$. The diameter is $2L$. We need $2L \leq 15$, so $L \leq 7$.

The total number of vertices is $1 + dL$ (center + $d$ branches of $L$ vertices each). We need $1 + dL \leq 120$.

Centers at pairwise distance $\geq 5$: 
- Two vertices on the same branch at distance $\geq 5$: on a branch of length $L$, we can place $\lfloor L/5 \rfloor + 1$ vertices pairwise at distance $\geq 5$.
- Two vertices on different branches at distances $a$ and $b$ from the center: distance $= a + b$. Need $a + b \geq 5$.

If we place vertices at the ends of branches (distance $L$ from center), the distance between two such is $2L \geq 5$ iff $L \geq 3$. With $L = 7$, $2L = 14 \geq 5$. ✓

On each branch of length 7 (vertices at distances 1, 2, ..., 7 from center), we can place vertices at distances 7 and 2 (distance 5 apart). But vertices at distance 2 on different branches are at distance 4 from each other, which is < 5. So we can only use distance 2 on one branch.

Alternatively, place vertices at distances 7 and 3 on each branch (distance 4 apart - too close!). Or 7 and 2 (distance 5). 

Let me be more systematic. On a branch of length 7, the vertices are at distances 1, 2, ..., 7 from the center. We want to select a subset pairwise at distance $\geq 5$. On a path of 7 vertices (distances 1-7), the maximum independent set with pairwise distance $\geq 5$ is: {1, 6}, {1, 7}, {2, 7}, {1}, {2}, ..., {7}. The maximum size is 2 (e.g., {1, 6} or {2, 7}).

But we also need cross-branch distances $\geq 5$. If we pick vertex at distance $a$ on one branch and distance $b$ on another, distance $= a + b \geq 5$.

If we pick {2, 7} on each branch: cross-branch, 2+2=4 < 5. ✗
If we pick {7} on each branch: cross-branch, 7+7=14 ≥ 5. ✓. This gives $d$ centers.
If we pick {7} on all branches and {2} on one branch: 2+7=9 ≥ 5, 7+7=14 ≥ 5. ✓. This gives $d + 1$ centers.

With $L = 7$, $d = \lfloor (120 - 1) / 7 \rfloor = \lfloor 119/7 \rfloor = 17$. So $d + 1 = 18$ centers.

Can we do better? What if we use {7, 2} on one branch and {7} on all others? That's $d + 1 = 18$.

What about {7, 2} on one branch, {7, 3} on another? 2+3=5 ≥ 5. ✓. 7+7=14, 7+3=10, 7+2=9, all ≥ 5. ✓. But 3+3=6 ≥ 5 ✓, 3+7=10 ✓. So {7, 3} on another branch: 2+3=5 ✓. So we could have {7, 2} on branch 1, {7, 3} on branch 2, {7} on branches 3-17. That's 2 + 2 + 15 = 19. But wait, 2+3=5 ≥ 5 ✓. And 3+3 would be if we had {3} on two branches, but we only have {3} on one. Let me check all pairs:
- 2 (branch 1) and 3 (branch 2): 2+3=5 ✓
- 2 (branch 1) and 7 (any other): 2+7=9 ✓
- 3 (branch 2) and 7 (any other): 3+7=10 ✓
- 7 and 7 (different branches): 14 ✓

So this works! 19 centers.

Can we push further? {7, 2} on branch 1, {7, 3} on branch 2, {7, 4} on branch 3? 2+4=6 ✓, 3+4=7 ✓. So yes. 20 centers.

{7, 2}, {7, 3}, {7, 4}, {7, 5}? 2+5=7 ✓, 3+5=8 ✓, 4+5=9 ✓. Yes. 21 centers. But wait, on a branch of length 7, can we pick {7, 5}? Distance = 2 < 5. ✗!

So {7, 5} doesn't work on the same branch (distance 2). We need the two vertices on the same branch to be at distance $\geq 5$. On a branch of length 7 (distances 1-7), pairs at distance $\geq 5$: (1,6), (1,7), (2,7). That's it. (2,7) has distance 5, (1,7) has distance 6, (1,6) has distance 5.

So the only 2-element subsets on a branch are {1,6}, {1,7}, {2,7}.

Using {2,7}: the "2" requires all other non-7 vertices to be at distance $\geq 5$ from it, i.e., at distance $\geq 3$ from center on other branches (since 2+3=5).

Using {1,7}: the "1" requires all other non-7 vertices to be at distance $\geq 4$ from center on other branches (since 1+4=5).

Using {1,6}: the "1" requires $\geq 4$, and the "6" requires $\geq -1$ (always satisfied for positive distances). But 6+6=12 ≥ 5, so "6" on multiple branches is fine. But 1+1=2 < 5, so "1" can only be on one branch.

So let's try: {1, 6} on one branch, {6} on all other branches. Cross-branch: 1+6=7 ✓, 6+6=12 ✓. On the same branch: 1 and 6 are at distance 5 ✓. This gives $d + 1$ centers (one "1" plus $d$ "6"s). With $d = 17$: 18 centers.

Or: {2, 7} on one branch, {7} on all others. 2+7=9 ✓, 7+7=14 ✓. $d + 1 = 18$.

Or: {1, 6} on one branch, {6, ?} on another? On a branch, {1, 6} uses distances 1 and 6. On another branch, can we use {6, 1}? 1+1=2 < 5. ✗. Can we use {6, 2}? 6-2=4 < 5. ✗. {6, 3}? 6-3=3 < 5. ✗. So on another branch, we can only use {6} (single vertex) or find another pair.

Hmm wait, I was considering {1, 6} on one branch. The "6" on this branch and "6" on another branch: 6+6=12 ✓. The "1" on this branch and "6" on another: 1+6=7 ✓. The "1" on this branch and "1" on another: 1+1=2 ✗. So "1" can only appear once.

What if we use {6} on all branches? That's $d$ centers. Plus one "1" on one branch: $d + 1$.

What about using "6" on all branches and "1" on one and "2" on one? 1+2=3 < 5 ✗. So "1" and "2" can't coexist on different branches.

What about "6" on all branches, "1" on one, and "4" on one? 1+4=5 ✓. 4+6=10 ✓. 4+4=8 ✓ (if on different branches). So we could have "6" on all $d$ branches, "1" on one branch, "4" on another. But wait, on the branch with "1", we already have "6". On the branch with "4", we already have "6". So the centers are: $d$ copies of "6", plus "1" (on one branch), plus "4" (on another branch). Total: $d + 2$. But we need 1+4=5 ✓ and 4 is at distance 4 from center, and 6 is at distance 6, so on the same branch, 4 and 6 are at distance 2 < 5. ✗!

So "4" and "6" can't be on the same branch. We'd need "4" on a branch without "6". But we want "6" on all branches. Contradiction.

Let me reconsider. Let me use a different branch structure. Some branches have "6" and some have other things.

Actually, let me think about this more carefully. We have $d$ branches, each of length 7. We want to select a set of vertices (each on some branch, at some distance from center) such that:
1. On the same branch, selected vertices are at distance $\geq 5$.
2. On different branches, selected vertices at distances $a$ and $b$ satisfy $a + b \geq 5$.

We want to maximize the total number of selected vertices.

Let's denote the selected vertices by their distance from the center. On branch $i$, we select a set $S_i \subseteq \{1, 2, ..., 7\}$ with pairwise differences $\geq 5$ (condition 1). For any $a \in S_i, b \in S_j$ ($i \neq j$), $a + b \geq 5$ (condition 2).

Condition 1 on a branch of length 7: $S_i$ can have at most 2 elements, and if it has 2, they must be from $\{(1,6), (1,7), (2,7)\}$.

To maximize the total, we want as many branches as possible to have 2 elements. But condition 2 constrains the "small" elements across branches.

If a branch has 2 elements, one of them is "small" (1 or 2) and one is "large" (6 or 7). The small elements across branches must sum to $\geq 5$.

If we use small element 1 on multiple branches: 1+1=2 < 5. ✗. So at most one branch with small element 1.
If we use small element 2 on multiple branches: 2+2=4 < 5. ✗. So at most one branch with small element 2.
If we use 1 on one branch and 2 on another: 1+2=3 < 5. ✗.

So at most one branch can have 2 elements (either {1,6}, {1,7}, or {2,7}). All other branches can have at most 1 element.

Wait, that's not right. Let me reconsider. If one branch has {1, 6} and another has {2, 7}: 1+2=3 < 5. ✗. If one has {1, 7} and another has {2, 7}: 1+2=3 < 5. ✗.

What if one branch has {1, 6} and another has just {7}? 1+7=8 ✓, 6+7=13 ✓. ✓. And another branch with just {7}? 7+7=14 ✓. ✓.

So: one branch with 2 elements, all others with 1 element (the "large" one). The large element should be $\geq 5$ minus the small element. If small is 1, large on other branches $\geq 4$. If small is 2, large on other branches $\geq 3$.

But the "large" element on other branches is a single element, so it can be anything from 1 to 7. But it must be at distance $\geq 5$ from the small element on the special branch. If small is 1, other single elements $\geq 4$. If small is 2, other single elements $\geq 3$.

But also, the single elements on different branches must be pairwise at sum $\geq 5$. If all single elements are 7: 7+7=14 ✓. If all are 3: 3+3=6 ✓ (if small is 2, 2+3=5 ✓). 

So: one branch with {2, 7}, all other branches with {3}. Check: 2+3=5 ✓, 3+3=6 ✓, 2+7=5 ✓ (same branch), 7+3=10 ✓. Total: $2 + (d-1) = d + 1$.

Or: one branch with {2, 7}, all other branches with {7}. Total: $d + 1$.

Or: one branch with {1, 6}, all other branches with {4}. Check: 1+4=5 ✓, 4+4=8 ✓, 1+6=5 ✓, 6+4=10 ✓. Total: $d + 1$.

Can we get $d + 2$? We'd need two branches with 2 elements each. But as shown, the small elements would conflict (1+2=3 < 5, 1+1=2 < 5, 2+2=4 < 5). So at most one branch with 2 elements. Hence max is $d + 1$.

With $d = 17$ (branches of length 7, $1 + 17 \cdot 7 = 120$): $d + 1 = 18$.

But wait, can we do better with a different tree structure? What about branches of different lengths?

**What if we use branches of length 7 and some of length 6?**

With $L = 7$, $d = 17$, $1 + 17 \cdot 7 = 120$. Exactly 120. ✓

What if we use a mix? Say 16 branches of length 7 and 1 branch of length 8? $1 + 16 \cdot 7 + 8 = 1 + 112 + 8 = 121 > 120$. Too many.

16 branches of length 7 and 1 of length 7: same as 17 branches. 

What about a different tree entirely? Not a star?

**Consider a "double star" or a path with branches.**

Let me think about a tree that's a path of length $p$ (the "spine"), with branches hanging off. The diameter would be the longest path, which could be from the end of a branch on one end to the end of a branch on the other end.

This is getting complicated. Let me think about whether 18 is actually the answer, or if we can do better with a non-tree graph.

**Non-tree construction:**

In a non-tree graph, distances can be shorter (more edges = shorter paths), which is bad for packing. But we might be able to use the extra edges to reduce the diameter while maintaining large distances between centers.

Wait, actually, in a tree, the diameter is already determined by the structure. Adding edges can only decrease distances (and thus the diameter), but it also decreases distances between centers, which is bad.

So trees seem optimal for maximizing packing given a diameter constraint. Let me think about whether that's true.

Actually, for a given number of vertices and diameter, a tree might not be optimal. Consider that in a tree, the diameter path "uses up" vertices that could otherwise be used for packing. In a non-tree, we might be able to have a more compact structure.

Hmm, let me think about this differently.

**Reformulation: We want to maximize $k$ such that there exists a graph on 120 vertices with diameter $\leq 15$ and $k$ vertices pairwise at distance $\geq 5$.**

Let me think about the problem as follows. Consider the $k$ centers. Define $f(v) = \min_i d(v, v_i)$ for each vertex $v$ (distance to nearest center). The centers have $f = 0$. The balls of radius 2 around centers are disjoint, so the vertices with $f \leq 2$ number at least $k$ (the centers) and the sets are disjoint.

Now, the vertices with $f \leq 2$ form $k$ disjoint sets. The vertices with $f = 3, 4$ are "between" centers. The vertices with $f \geq 5$ are... wait, can $f$ be $\geq 5$? If the diameter is 15 and we have $k$ centers, a vertex could be far from all centers. But actually, every vertex is within distance 15 of every center (diameter 15), so $f(v) \leq 15$ for all $v$.

Hmm, I don't think this approach leads anywhere quickly. Let me try to think about specific constructions and see if I can beat 18.

**Construction: A path-like graph with "shortcuts".**

Consider a path $v_0, v_1, \ldots, v_{119}$. Add edges $v_i v_{i+1}$ (path edges). The diameter is 119, too large. Add "shortcut" edges to reduce diameter.

But as I computed earlier, it's hard to reduce the diameter to 15 while maintaining large distances between some vertices.

**Construction: A "broom" or "broom-like" structure.**

Actually, let me reconsider the star construction. With $L = 7$ and $d = 17$, we get 18 centers. Can we use $L = 7$ and $d = 17$ but with a different assignment?

Actually, I realize we might be able to do better by not using a star. Let me think about a "caterpillar" graph.

**Caterpillar construction:**

A caterpillar is a path (spine) with leaves attached. Consider a spine $v_0, v_1, \ldots, v_s$ and leaves attached to spine vertices. 

The diameter is at most $s + 2$ (from a leaf on one end to a leaf on the other, going through the spine). We need $s + 2 \leq 15$, so $s \leq 13$.

The total number of vertices is $(s + 1) + \text{(number of leaves)}$. We need this $\leq 120$.

For packing: we want vertices pairwise at distance $\geq 5$. 

Spine vertices at distance $\geq 5$: on a path of length $s = 13$ (14 vertices), we can pick $\lfloor 13/5 \rfloor + 1 = 3$ vertices (e.g., $v_0, v_5, v_{10}$).

Leaves: a leaf attached to $v_i$ is at distance 1 from $v_i$. The distance between a leaf on $v_i$ and a leaf on $v_j$ is $|i-j| + 2$. For this to be $\geq 5$, $|i-j| \geq 3$.

A leaf on $v_i$ and a spine vertex $v_j$: distance $= 1 + |i-j|$. For $\geq 5$, $|i-j| \geq 4$.

This is getting complicated. Let me think about whether the caterpillar can beat 18.

With $s = 13$, we have 14 spine vertices. We can attach leaves to spine vertices. The total is $14 + \text{leaves} \leq 120$, so up to 106 leaves.

If we attach leaves to $v_0, v_3, v_6, v_9, v_{12}$ (every 3rd vertex), with leaves pairwise at distance $\geq 5$: leaf on $v_0$ and leaf on $v_3$: distance $= 3 + 2 = 5$. ✓. Leaf on $v_0$ and leaf on $v_6$: $6 + 2 = 8$. ✓. So we can have one leaf per selected spine vertex, and they're pairwise at distance $\geq 5$.

But we can have multiple leaves on the same spine vertex? No, two leaves on the same spine vertex are at distance 2 (through the spine vertex), which is < 5.

So we can have at most 1 leaf per spine vertex in our packing. With 5 spine vertices selected (every 3rd), we get 5 leaves. Plus possibly some spine vertices.

Spine vertices pairwise at distance $\geq 5$: $v_0, v_5, v_{10}$ (3 vertices). But these are at distance 1 from their leaves, so a spine vertex and a leaf on an adjacent spine vertex might be too close.

This is getting messy. Let me think about it more carefully.

Actually, I think the star construction might be close to optimal, but let me think about whether we can do better.

**General upper bound:**

Consider a graph $G$ on $n = 120$ vertices with diameter $D \leq 15$. Let $S$ be a set of $k$ vertices pairwise at distance $\geq 5$.

Consider the balls $B(v_i, 2)$ for $v_i \in S$. These are disjoint. Let $b_i = |B(v_i, 2)|$. Then $\sum b_i \leq 120$.

Now, consider the "expanded" balls $B(v_i, 7)$. Since the diameter is $\leq 15$, for any vertex $u$ and any center $v_i$, $d(u, v_i) \leq 15$. In particular, every vertex is in $B(v_i, 15)$ for every $i$. But more usefully, every vertex is in $B(v_i, 7)$ for some $i$? Not necessarily.

Hmm, let me think about a covering argument. If the diameter is 15, then for any vertex $u$, $d(u, v_1) \leq 15$. But $u$ might not be within 7 of any center.

Let me try a different approach. Consider the $k$ centers. For each center $v_i$, consider the sphere $S_i = \{u : d(u, v_i) \leq 7\}$. The union of all $S_i$ covers all vertices (since for any $u$, $d(u, v_i) \leq 15 \leq 15$ for all $i$, but we need $d(u, v_i) \leq 7$ for some $i$, which isn't guaranteed).

OK this covering approach doesn't work directly.

**Let me try to think about the problem from the perspective of the "line graph" more carefully.**

Actually, I realize I should think about this more carefully. The line graph has 120 vertices. We design it. We want to maximize the number of vertices pairwise at distance $\geq 5$, subject to diameter $\leq 15$.

This is equivalent to: what is the maximum size of a "5-packing" in a graph on 120 vertices with diameter $\leq 15$?

Let me think about this as an extremal graph theory problem.

**Claim: The answer is 16.**

Hmm, let me think about why. Consider a graph with diameter 15. Take a diametral path $v_0, v_1, \ldots, v_{15}$ (length 15). Every vertex is within distance 7 of some vertex on this path (the midpoint of the path is at distance $\leq 7$ from every vertex on the path, and every vertex in the graph is within distance 7 of the path... is this true?).

Actually, in a graph with diameter 15, every vertex is within distance 15 of $v_0$. But is every vertex within distance 7 of the diametral path? Not necessarily.

Let me think about a specific extremal construction.

**Optimal construction: A "spider" with branches of length 7.**

As computed: star with center, 17 branches of length 7, total 120 vertices, diameter 14. Packing: 18 (one branch with 2 centers, 16 branches with 1 center).

Wait, the diameter is 14 (end of one branch to end of another: $7 + 7 = 14$). We need diameter $\leq 15$, so 14 is fine. ✓

Can we use branches of length 7 and one branch of length 8? $1 + 16 \cdot 7 + 8 = 1 + 112 + 8 = 121 > 120$. No.

What about 16 branches of length 7 and 1 branch of length 7: $1 + 17 \cdot 7 = 120$. ✓. Diameter 14.

What about using the diameter more fully? If we use branches of length 7 and 8: $1 + 16 \cdot 7 + 1 \cdot 8 = 121$. Too many. $1 + 15 \cdot 7 + 1 \cdot 8 = 114$. 6 vertices left. Add another branch of length 6: $114 + 6 = 120$. So 15 branches of length 7, 1 of length 8, 1 of length 6. Diameter = $8 + 7 = 15$. ✓

On the branch of length 8: can pick {3, 8} (distance 5). On branches of length 7: {7} or {2, 7}. On the branch of length 6: {6} or {1, 6}.

Cross-branch distances: 3 (from length-8 branch) + 1 (from length-6 branch) = 4 < 5. ✗. So if we use 3 on the length-8 branch, we can't use 1 on the length-6 branch.

Let me try: length-8 branch: {8} (just the end). Length-7 branches: {7} on each. Length-6 branch: {6}. Cross: 8+7=15, 8+6=14, 7+6=13, 7+7=14. All ≥ 5. ✓. Total: 1 + 15 + 1 = 17. Worse than 18.

Try: length-8 branch: {3, 8}. Length-7 branches: {7} on each. Length-6 branch: {6}. Cross: 3+7=10, 3+6=9, 3+8=5 (same branch), 8+7=15, 8+6=14, 7+6=13, 7+7=14. All ≥ 5. ✓. Total: 2 + 15 + 1 = 18. Same as before.

Try: length-8 branch: {3, 8}. Length-7 branches: {7} on 14, {2, 7} on 1. Length-6 branch: {6}. Cross: 3+2=5 ✓, 2+6=8 ✓, 2+7=9 ✓, 3+6=9 ✓, 3+7=10 ✓, 8+6=14 ✓, 8+7=15 ✓, 7+6=13 ✓, 7+7=14 ✓, 2+8=10 ✓. All ≥ 5. ✓. Total: 2 + 14 + 2 + 1 = 19!

Wait, let me double-check. We have:
- Length-8 branch: vertices at distances 1-8 from center. Selected: {3, 8}.
- One length-7 branch: selected {2, 7}.
- 14 length-7 branches: selected {7} each.
- Length-6 branch: selected {6}.

Cross-branch pairs:
- 3 and 2: 3+2=5 ✓
- 3 and 7: 3+7=10 ✓
- 3 and 6: 3+6=9 ✓
- 8 and 2: 8+2=10 ✓
- 8 and 7: 8+7=15 ✓
- 8 and 6: 8+6=14 ✓
- 2 and 7: 2+7=9 ✓
- 2 and 6: 2+6=8 ✓
- 7 and 6: 7+6=13 ✓
- 7 and 7: 7+7=14 ✓

Same-branch pairs:
- 3 and 8: |8-3|=5 ✓
- 2 and 7: |7-2|=5 ✓

All pairs satisfy distance ≥ 5. ✓

Total centers: 2 + 2 + 14 + 1 = 19. 

Can we push to 20? We'd need another branch with 2 centers. We already have two branches with 2 centers (length-8 with {3,8} and length-7 with {2,7}). The "small" elements are 3 and 2. 3+2=5 ✓. Can we add a third branch with 2 centers?

On a length-7 branch, the 2-center options are {1,6}, {1,7}, {2,7}. The small elements are 1 or 2.
- If small is 1: 1+2=3 < 5 ✗ (conflicts with existing 2). 1+3=4 < 5 ✗ (conflicts with existing 3).
- If small is 2: 2+2=4 < 5 ✗ (conflicts with existing 2). 2+3=5 ✓ (OK with 3).

So we can't add a third 2-center branch because the small element would conflict.

What if we change the configuration? Use {3, 8} on length-8, {3, 8} on... wait, we only have one length-8 branch.

What if we use two length-8 branches? $1 + 2 \cdot 8 + \text{rest} = 1 + 16 + \text{rest} = 17 + \text{rest} \leq 120$. Rest = 103, with length-7 branches: $103 / 7 = 14.7...$, so 14 branches of length 7 (98 vertices) and 5 left over. $17 + 98 + 5 = 120$. The 5 leftover could be a branch of length 5.

Diameter: $8 + 8 = 16 > 15$. ✗! Two branches of length 8 give diameter 16.

So we can't have two branches of length 8. What about one length-8 and one length-7, with the length-7 having 2 centers?

We already did that: 19 centers. Let me see if there's a completely different structure that does better.

**What about a non-star tree?**

Consider a tree where the center is not a single vertex but a path. For example, a path $c_0, c_1, c_2$ (length 2) as the "core," with branches hanging off $c_0, c_1, c_2$.

The diameter would be the longest path between two leaf vertices. If a branch of length $a$ hangs off $c_0$ and a branch of length $b$ hangs off $c_2$, the distance is $a + 2 + b$. For diameter $\leq 15$: $a + b \leq 13$.

This is more flexible but also more complex. Let me think about whether it helps.

Actually, the key constraint is: the diameter is $\leq 15$, and we want to pack centers at pairwise distance $\geq 5$. The star with branches of length 7 gives diameter 14 and packing 18-19. Can we do better?

Let me think about an upper bound.

**Upper bound attempt:**

Consider a graph $G$ on 120 vertices with diameter $\leq 15$. Let $S$ be a set of $k$ vertices pairwise at distance $\geq 5$.

Consider the balls $B(v, 2)$ for $v \in S$. These are disjoint. The total number of vertices in these balls is $\sum_{v \in S} |B(v, 2)| \leq 120$.

Now, I claim that $|B(v, 2)| \geq 3$ for each $v \in S$ (assuming the graph is connected and $v$ is not a leaf of degree 1... actually, $v$ could be a leaf).

Hmm, in the star construction, the centers at the ends of branches are leaves (degree 1). $|B(v, 2)|$ for a leaf at the end of a branch of length 7: the ball of radius 2 includes the leaf, its neighbor, and the neighbor's neighbor. So $|B(v, 2)| = 3$. For a center at distance 2 from the star center (on a branch), $|B(v, 2)|$ includes: $v$, its neighbors (the star center and the next vertex on the branch), and their neighbors. The star center has degree 17, so $|B(v, 2)| \geq 1 + 2 + 16 = 19$ (roughly). 

So the ball sizes vary. The total $\sum |B(v, 2)| \leq 120$ gives $k \leq 120 / \min |B(v, 2)|$. If some centers have small balls (size 3), this gives $k \leq 40$, which is not tight.

Let me think about a better upper bound.

**Upper bound using the diameter:**

Consider the $k$ centers $v_1, \ldots, v_k$. For any two centers $v_i, v_j$, $5 \leq d(v_i, v_j) \leq 15$.

Consider the "metric space" on the $k$ centers. The diameter of this space is $\leq 15$, and the minimum distance is $\geq 5$.

Now, consider the balls of radius 2 in the original graph. These are disjoint. The ball $B(v_i, 2)$ has $|B(v_i, 2)|$ vertices. 

The key observation: the ball $B(v_i, 7)$ must contain all vertices within distance 7 of $v_i$. Since the diameter is $\leq 15$, for any vertex $u$ and any center $v_i$, $d(u, v_i) \leq 15$. But $u$ might not be in $B(v_i, 7)$.

However, consider the following: for any vertex $u$, $u$ is in $B(v_i, 15)$ for all $i$. Also, $u$ is in $B(v_i, 7)$ for some $i$? Not necessarily.

Let me try a volume argument. The ball $B(v_i, 7)$ has some size. The balls $B(v_i, 2)$ are disjoint and contained in $B(v_i, 7)$. The "annulus" $B(v_i, 7) \setminus B(v_i, 2)$ has size $|B(v_i, 7)| - |B(v_i, 2)|$.

Hmm, I don't think this leads to a clean bound without more information about the graph structure.

**Let me try a different approach: think about the problem in terms of the "line graph" and use a known result.**

Actually, let me reconsider the problem. The problem says "120 underground lines" and asks for the "maximum number of pairwise distant stations." I've been assuming each station is on exactly one line, which seems right for maximizing distant stations.

But wait—I should also consider that the line graph might not need to have diameter exactly 15. The condition is that the diameter is $\leq 15$. And we want to maximize the 5-packing.

Let me think about the problem as: what is the maximum $k$ such that there exists a graph on 120 vertices with diameter $\leq 15$ and a 5-packing of size $k$?

**Let me try to construct a graph that achieves more than 19.**

**Idea: Use a graph that is not a tree.**

In a tree, the distance between two vertices is the unique path length. In a non-tree, distances can be shorter. But we want distances between centers to be $\geq 5$, so shorter distances are bad. However, non-tree edges can reduce the diameter without affecting the distances between centers (if the extra edges are between non-center vertices).

Wait, but adding edges can only decrease distances. So if we have a tree with diameter 14 and packing 19, adding edges would decrease the diameter (good, but we're already $\leq 15$) and potentially decrease distances between centers (bad).

So for a given packing, the tree is the best (maximizes distances). And for a given diameter, the tree is also good (it has the largest diameter for a given structure, so it gives the most "room" for packing).

Hmm, but actually, a non-tree might allow a different structure that's better. Let me think...

**Idea: Use a graph with a "hub" structure.**

Consider a graph with a central clique $C$ of size $c$, and $m$ "arms" emanating from the clique. Each arm is a path of length $L$ starting from a vertex in $C$. The diameter is $2L$ (end of one arm to end of another, going through the clique). We need $2L \leq 15$, so $L \leq 7$.

Total vertices: $c + mL \leq 120$ (the clique vertices plus the arm vertices; but the first vertex of each arm is in the clique, so actually $c + m(L-1) \leq 120$? No, let me be more careful.)

Actually, let me model it as: the clique $C$ has $c$ vertices. Each arm is a path of length $L$ (i.e., $L$ edges, $L+1$ vertices including the starting vertex in $C$). So each arm adds $L$ new vertices. Total: $c + mL \leq 120$.

The diameter is $2L$ (end of one arm to end of another). Need $2L \leq 15$, so $L \leq 7$.

Packing: similar to the star case. On each arm (path of length $L$ from the clique), we can place centers. The distance between a center at distance $a$ from the clique (on one arm) and a center at distance $b$ from the clique (on another arm) is $a + b$ (go through the clique). The distance between two centers on the same arm is $|a - b|$.

This is the same as the star case! The clique doesn't help because the distance through the clique is $a + b$, same as through a single center vertex.

So the clique version gives the same packing as the star version. The only difference is that the clique uses more vertices for the center, leaving fewer for arms. So the star (clique of size 1) is better.

**Idea: Use a "path of cliques" (blow-up of a path).**

As I considered earlier: a path of $d+1$ groups, each a clique of size $s$, with complete bipartite between consecutive groups. Diameter $d$, total vertices $s(d+1)$.

With $d = 15$, $s = 8$ (using $8 \times 16 = 128 > 120$). Hmm, $s = 7$, $7 \times 16 = 112 \leq 120$. Or $d = 14$, $s = 8$, $8 \times 15 = 120$. ✓

Packing: pick groups at distance $\geq 5$, one vertex per group. $\lfloor 14/5 \rfloor + 1 = 3$.

That's much worse than 19. The blow-up wastes vertices.

**Idea: Use a graph that's a tree but not a star.**

Consider a "binary tree" of depth $h$. The diameter is $2h$. Need $2h \leq 15$, so $h \leq 7$. A full binary tree of depth 7 has $2^8 - 1 = 255$ vertices, way more than 120. A binary tree of depth 7 with fewer vertices...

Actually, the depth-7 binary tree has too many vertices. Let me think about a "thin" binary tree.

In a binary tree of depth 7, the leaves are at depth 7. The distance between two leaves is at most 14 (through the root). We can pick leaves that are pairwise at distance $\geq 5$. The distance between two leaves is $14 - 2 \cdot \text{LCA depth}$ (where LCA is the lowest common ancestor). For distance $\geq 5$: $14 - 2d \geq 5$, so $d \leq 4.5$, i.e., LCA depth $\leq 4$.

Hmm, this is getting complicated. Let me think about it differently.

**Let me think about the problem as an optimization over trees.**

We want a tree $T$ on 120 vertices with diameter $\leq 15$ that maximizes the 5-packing number.

The 5-packing number of a tree is the maximum number of vertices pairwise at distance $\geq 5$.

For a tree, the packing is related to the structure. Let me think about what tree maximizes this.

**Key insight: In a tree, the 5-packing is maximized by a "subdivision" of a star.**

A star with $d$ branches of length $L$ has:
- Diameter $2L$.
- $1 + dL$ vertices.
- 5-packing: as computed, roughly $d + 1$ (one "extra" center on one branch).

To maximize $d + 1$ with $1 + dL \leq 120$ and $2L \leq 15$:
- $L = 7$: $d \leq 119/7 = 17$, packing $\leq 18$.
- $L = 7$, $d = 17$: packing 18 (or 19 with mixed branch lengths as shown).

Can we do better with $L = 7$ and a different tree structure?

**What about a "double star" (two centers connected by a path, with branches on each)?**

Consider two "hubs" $h_1, h_2$ connected by a path of length $p$. From $h_1$, there are $d_1$ branches of length $L_1$. From $h_2$, there are $d_2$ branches of length $L_2$. The diameter is $L_1 + p + L_2$ (end of a branch on $h_1$ to end of a branch on $h_2$). Need $L_1 + p + L_2 \leq 15$.

Also, the distance between two ends of branches on the same hub is $2L_i$ (through the hub). Need $2L_1 \leq 15$ and $2L_2 \leq 15$.

Total vertices: $1 + d_1 L_1 + p + d_2 L_2$ (hubs are $h_1$ and $h_2$, with $p-1$ intermediate vertices on the path, plus $d_1 L_1 + d_2 L_2$ branch vertices). Wait, let me be more careful. $h_1$ and $h_2$ are connected by a path of length $p$ (so $p+1$ vertices including both hubs). From $h_1$, $d_1$ branches of length $L_1$ (each adding $L_1$ new vertices). From $h_2$, $d_2$ branches of length $L_2$ (each adding $L_2$ new vertices). Total: $(p+1) + d_1 L_1 + d_2 L_2 \leq 120$.

Packing: 
- Centers on branches of $h_1$: pairwise distance $\geq 5$ as before.
- Centers on branches of $h_2$: similarly.
- Cross: a center at distance $a$ from $h_1$ (on a branch of $h_1$) and a center at distance $b$ from $h_2$ (on a branch of $h_2$): distance $= a + p + b$. Need $a + p + b \geq 5$.

If $p \geq 5$, then $a + p + b \geq 5$ always. So the two sides are independent! Each side is like a star with branches of length $L_i$ and diameter $2L_i \leq 15$.

With $p = 5$, $L_1 = L_2 = 5$ (so $L_1 + p + L_2 = 15$ ✓, $2L_1 = 10 \leq 15$ ✓):
- Total: $6 + 5d_1 + 5d_2 \leq 120$, so $d_1 + d_2 \leq 22$.
- Packing on each side: $d_i + 1$ (with the extra center trick).
- Total packing: $(d_1 + 1) + (d_2 + 1) = d_1 + d_2 + 2 \leq 24$.

Wait, that's much better than 19! Let me verify.

With $p = 5$, $L_1 = L_2 = 5$:
- $h_1$ side: $d_1$ branches of length 5. On each branch, we can pick the endpoint (distance 5 from $h_1$). Cross-branch: $5 + 5 = 10 \geq 5$ ✓. On one branch, we can also pick the vertex at distance 0 from $h_1$... wait, $h_1$ is the hub, not on a branch. Let me reconsider.

On a branch of length 5 from $h_1$: vertices at distances 1, 2, 3, 4, 5 from $h_1$. We can pick {5} (the endpoint) or {1, 6}... wait, the branch has length 5, so vertices at distances 1-5. Pairs at distance $\geq 5$: (1, 6) - but 6 doesn't exist. So only single vertices per branch, or... 

Actually, on a path of length 5 (vertices at distances 1, 2, 3, 4, 5 from hub), the maximum 2-element set at distance $\geq 5$ is... distance between distance-1 and distance-5 is 4 < 5. So no 2-element set! We can only pick 1 per branch.

Hmm, so with $L = 5$, each branch contributes at most 1 center. And the "extra center" trick doesn't work because we can't fit 2 centers on a branch of length 5.

So packing on $h_1$ side: $d_1$ (one per branch). Similarly $h_2$ side: $d_2$. Total: $d_1 + d_2 \leq 22$.

But wait, can we also use the path vertices (between $h_1$ and $h_2$) as centers? The path has vertices $h_1, p_1, p_2, p_3, p_4, h_2$ (length 5). A path vertex $p_i$ is at distance $i$ from $h_1$ and $5-i$ from $h_2$. 

A center on a branch of $h_1$ at distance $a$ from $h_1$ and a path vertex at distance $j$ from $h_1$: distance $= a + j$. Need $a + j \geq 5$. If $a = 5$ (endpoint), $j \geq 0$, always ✓. If $a = 1$, $j \geq 4$.

A center on a branch of $h_2$ at distance $b$ from $h_2$ and a path vertex at distance $j$ from $h_1$ (so $5-j$ from $h_2$): distance $= b + (5-j)$. Need $b + 5 - j \geq 5$, so $b \geq j$. If $b = 5$, $j \leq 5$, always ✓.

Two path vertices at distances $j_1, j_2$ from $h_1$: distance $= |j_1 - j_2|$. Need $\geq 5$. On a path of length 5 (6 vertices), max set at pairwise distance $\geq 5$: {0, 5} (i.e., $h_1$ and $h_2$), size 2. But $h_1$ is the hub, and using it as a center: distance to a branch endpoint at distance 5 from $h_1$ is 5 ✓. Distance to a branch endpoint at distance 5 from $h_2$ is $5 + 5 = 10$ ✓.

So we could use $h_1$ and $h_2$ as centers, plus the branch endpoints. But $h_1$ is at distance 0 from itself, and a branch endpoint at distance 5 from $h_1$ is at distance 5 from $h_1$ ✓. And $h_1$ and $h_2$ are at distance 5 ✓.

So: $h_1, h_2$ as centers, plus $d_1$ endpoints on $h_1$'s branches, plus $d_2$ endpoints on $h_2$'s branches. Total: $2 + d_1 + d_2 \leq 2 + 22 = 24$.

But wait, I need to check: $h_1$ and a branch endpoint on $h_1$ at distance 5: distance = 5 ✓. $h_1$ and a branch endpoint on $h_2$ at distance 5: distance = 5 + 5 = 10 ✓. $h_2$ and a branch endpoint on $h_1$: 5 + 5 = 10 ✓. $h_2$ and a branch endpoint on $h_2$: 5 ✓. Two branch endpoints on $h_1$: 5 + 5 = 10 ✓. Two branch endpoints on $h_2$: 10 ✓. Cross: 5 + 5 + 5 = 15 ✓. $h_1$ and $h_2$: 5 ✓.

All pairwise distances $\geq 5$ ✓. Total: $2 + d_1 + d_2 = 2 + 22 = 24$.

That's much better than 19! Let me verify the total vertex count: $(p+1) + d_1 L_1 + d_2 L_2 = 6 + 5 \cdot 11 + 5 \cdot 11 = 6 + 55 + 55 = 116 \leq 120$ ✓. (With $d_1 = d_2 = 11$.)

Actually, $d_1 + d_2 \leq (120 - 6) / 5 = 114 / 5 = 22.8$, so $d_1 + d_2 \leq 22$. With $d_1 = d_2 = 11$: $6 + 55 + 55 = 116$. 4 vertices unused. Could we use them? Add a branch of length 4 to one hub: $d_1 = 12, d_2 = 11$, but one branch has length 4. $6 + 5 \cdot 11 + 4 \cdot 1 + 5 \cdot 11 = 6 + 55 + 4 + 55 = 120$. Wait, that's 12 branches on $h_1$ (11 of length 5, 1 of length 4) and 11 branches on $h_2$ (all length 5). Total: $6 + 59 + 55 = 120$. ✓

On the length-4 branch: endpoint at distance 4 from $h_1$. Distance to $h_1$: 4 < 5. ✗! So we can't use the endpoint of the length-4 branch as a center (too close to $h_1$). 

Hmm, but we could use a different vertex on the length-4 branch. Actually, the only vertex at distance $\geq 5$ from $h_1$ on a branch of length 4 is... none (max distance is 4). So the length-4 branch doesn't contribute a center. But it does use up 4 vertices. Not helpful.

Alternatively, use $d_1 = 11, d_2 = 11$, and 4 unused vertices. Or find a way to use them.

Actually, we could add a branch of length 4 to $h_1$ and use the vertex at distance 4 from $h_1$ on this branch. Its distance to $h_2$ is $4 + 5 = 9 \geq 5$ ✓. Its distance to a branch endpoint on $h_2$ is $4 + 5 + 5 = 14 \geq 5$ ✓. Its distance to a branch endpoint on $h_1$ (at distance 5) is $4 + 5 = 9 \geq 5$ ✓. Its distance to $h_1$ is 4 < 5 ✗.

So if we don't use $h_1$ as a center, we can use the length-4 branch endpoint. Then we have: $d_1 + d_2 + 1$ (the extra from length-4 branch) + 1 (h_2) = 11 + 11 + 1 + 1 = 24. Same as before (we lose $h_1$ but gain the length-4 endpoint).

Or: don't use $h_1$ or $h_2$, but use the length-4 branch endpoint. $d_1 + 1 + d_2 = 11 + 1 + 11 = 23$. Worse.

So 24 seems to be the max with this structure. But can we do even better with a different structure?

**Generalization: "Multi-hub" structure.**

Consider $m$ hubs connected by a path of length $p$ between consecutive hubs. From each hub, branches of length $L$. The diameter is $L + (m-1)p + L = 2L + (m-1)p$. Need $2L + (m-1)p \leq 15$.

If $p \geq 5$, centers on different hubs' branches are automatically at distance $\geq 5$ (since the path between hubs is $\geq 5$). Actually, the distance between a branch endpoint on hub $i$ and a branch endpoint on hub $j$ is $L + |i-j| \cdot p + L = 2L + |i-j| \cdot p$. For $|i-j| = 1$: $2L + p \geq 5$ (easily satisfied). For the same hub: $2L \geq 5$, so $L \geq 3$.

Also, the hub itself can be a center if it's at distance $\geq 5$ from all other centers. The hub is at distance $L$ from its branch endpoints, so $L \geq 5$ for the hub to be a center alongside its branch endpoints. Or $L < 5$ and we don't use the hub.

Let me try $m = 3$ hubs, $p = 5$, $L = 3$. Diameter: $2 \cdot 3 + 2 \cdot 5 = 16 > 15$. ✗.

$m = 3$, $p = 5$, $L = 2$: Diameter $= 4 + 10 = 14 \leq 15$ ✓. But $L = 2$: branch endpoints at distance 2 from hub. Same-hub: $2 + 2 = 4 < 5$ ✗. So we can only pick 1 endpoint per hub. And the hub itself: distance to endpoint = 2 < 5 ✗. So we can pick the hub or one endpoint per hub. 

With $L = 2$, $m = 3$, $p = 5$: total vertices = $(2 \cdot 5 + 1) + 3 \cdot d \cdot 2 = 11 + 6d \leq 120$, $d \leq 18$. Centers: 3 (one per hub, either the hub or an endpoint). Plus, can we use path vertices? Path vertices between hub $i$ and hub $i+1$ at distance $j$ from hub $i$: distance to hub $i$ is $j$, to hub $i+1$ is $5-j$. For a path vertex to be a center, it needs to be at distance $\geq 5$ from all other centers.

This is getting complicated. Let me try to find the optimal structure more systematically.

**Optimization over the multi-hub structure:**

We have $m$ hubs on a path, with spacing $p$ (path length between consecutive hubs). From each hub, $d_i$ branches of length $L$. 

Diameter: $2L + (m-1)p \leq 15$.
Total vertices: $(m-1)p + 1 + L \sum d_i \leq 120$. (The path has $(m-1)p + 1$ vertices, and each branch adds $L$ vertices.)

Centers: 
- If $L \geq 5$: can use hub and endpoints. Each hub contributes $d_i + 1$ centers (endpoints + hub). But hubs on the path are at distance $p$ from each other. Need $p \geq 5$ for hubs to be pairwise at distance $\geq 5$.
  - If $p \geq 5$: all centers across hubs are pairwise at distance $\geq 5$ (hub-to-hub: $p \geq 5$; endpoint-to-endpoint same hub: $2L \geq 10 \geq 5$; endpoint-to-endpoint different hubs: $2L + p \geq 15$; hub-to-endpoint same hub: $L \geq 5$; hub-to-endpoint different hubs: $L + p \geq 10$). Total: $\sum (d_i + 1) = \sum d_i + m$.
  - Constraint: $2L + (m-1)p \leq 15$ and $(m-1)p + 1 + L \sum d_i \leq 120$.
  - Maximize $\sum d_i + m$.
  
  With $L = 5$, $p = 5$: $2 \cdot 5 + (m-1) \cdot 5 \leq 15$, so $10 + 5(m-1) \leq 15$, $5m \leq 10$, $m \leq 2$. So $m = 2$, back to the previous case. Total: $\sum d_i + 2$, with $5 + 1 + 5 \sum d_i \leq 120$, $\sum d_i \leq 22$. Total: 24.

  With $L = 5$, $p = 5$, $m = 2$: as before, 24.

  With $L = 6$, $p = 3$: $12 + 3(m-1) \leq 15$, $3(m-1) \leq 3$, $m \leq 2$. $m = 2$: diameter $= 12 + 3 = 15$ ✓. But $p = 3 < 5$, so hubs are at distance 3 < 5. Can't use both hubs as centers. 
  
  With $p = 3$, hubs at distance 3. If we use hub 1 as a center, hub 2 can't be a center (distance 3 < 5). But endpoints on hub 2 are at distance $6 + 3 = 9$ from hub 1 ✓. So: hub 1 + endpoints on hub 1 ($d_1$) + endpoints on hub 2 ($d_2$). Total: $1 + d_1 + d_2$. Constraint: $3 + 1 + 6(d_1 + d_2) \leq 120$, $d_1 + d_2 \leq 19$. Total: 20. Worse than 24.

  With $L = 7$, $p = 1$: $14 + (m-1) \leq 15$, $m \leq 2$. $m = 2$: diameter 15. $p = 1$: hubs at distance 1. Can use at most one hub. Endpoints on hub 1 at distance 7, endpoints on hub 2 at distance 7, cross: $7 + 1 + 7 = 15$ ✓. Hub 1 + $d_1$ + $d_2$: $1 + d_1 + d_2$. Constraint: $1 + 1 + 7(d_1 + d_2) \leq 120$, $d_1 + d_2 \leq 16$. Total: 17. Worse.

So $L = 5, p = 5, m = 2$ giving 24 seems good. Can we beat it?

**What about $L = 5, p = 5, m = 2$ but also using path vertices as centers?**

The path between hubs has vertices at distances 0, 1, 2, 3, 4, 5 from hub 1 (i.e., hub 1, $p_1, p_2, p_3, p_4$, hub 2). We're already using hub 1 and hub 2 as centers. Can we also use $p_1, p_2, p_3, p_4$?

$p_1$ is at distance 1 from hub 1 < 5 ✗. So no path vertex (other than the hubs) can be a center.

What if we don't use the hubs but use path vertices? $p_0 = $ hub 1, $p_5 = $ hub 2. Path vertices at distances 0-5 from hub 1. Pairwise at distance $\geq 5$: {0, 5} only. So 2 path centers. Plus branch endpoints: $d_1 + d_2$. But a path center at distance 0 (hub 1) and a branch endpoint at distance 5 from hub 1: distance 5 ✓. A path center at distance 5 (hub 2) and a branch endpoint at distance 5 from hub 2: distance 5 ✓. A path center at distance 0 and a branch endpoint at distance 5 from hub 2: distance 10 ✓.

So it's the same: 2 + $d_1 + d_2 = 24$.

**Can we use a longer path between hubs to fit more path centers?**

With $p = 10$, $L = 2$: diameter $= 4 + 10 = 14$ ✓. $m = 2$. Path has 11 vertices. Path centers at pairwise distance $\geq 5$: {0, 5, 10}, size 3. But $L = 2$: branch endpoints at distance 2 from hub. Hub-to-endpoint: 2 < 5 ✗. So can't use hubs and endpoints together. 

If we use path centers {0, 5, 10} (which are hub 1, middle, hub 2): 
- Hub 1 (distance 0) and branch endpoint on hub 1 (distance 2): distance 2 < 5 ✗.
- Middle (distance 5 from hub 1) and branch endpoint on hub 1 (distance 2): distance 7 ✓.
- Middle and branch endpoint on hub 2 (distance 2 from hub 2 = distance 8 from hub 1): distance 3 < 5 ✗.

Hmm, so the middle path vertex is at distance 7 from hub 1's endpoints but distance 3 from hub 2's endpoints. Not good.

Let me try: use path centers {0, 5, 10} and no branch endpoints. Total: 3. Plus, can we add branch endpoints that are far enough from all path centers?

A branch endpoint on hub 1 at distance 2 from hub 1: distance to path center 0 = 2 < 5 ✗. Distance to path center 5 = 7 ✓. Distance to path center 10 = 12 ✓. But distance to 0 is 2, so can't use it.

A branch endpoint on hub 2 at distance 2 from hub 2: distance to path center 10 = 2 < 5 ✗.

So with path centers {0, 5, 10}, we can't use any branch endpoints. Total: 3. Much worse.

What if we use path centers {5} only (the middle)? Then branch endpoints on hub 1 at distance 2: distance to middle = 7 ✓. Branch endpoints on hub 2 at distance 2: distance to middle = 3 < 5 ✗. So only hub 1's endpoints. Total: 1 + $d_1$. With $L = 2$, $p = 10$: $11 + 2d_1 + 2d_2 \leq 120$, $d_1 + d_2 \leq 54$. But we can only use $d_1$ endpoints. $1 + d_1 \leq 1 + 54 = 55$. But we also need the branch endpoints on hub 1 to be pairwise at distance $\geq 5$: $2 + 2 = 4 < 5$ ✗!

So with $L = 2$, branch endpoints on the same hub are at distance 4 < 5. Can only pick 1 per hub. Total: 1 (middle) + 1 (hub 1 endpoint) = 2. Terrible.

OK, so $L = 2$ is bad for packing. We need $L \geq 3$ for same-hub endpoints to be at distance $\geq 5$ (actually $2L \geq 5$, so $L \geq 3$).

With $L = 3$, $p = 9$: diameter $= 6 + 9 = 15$ ✓. $m = 2$. Path: 10 vertices. Same-hub endpoints: $2 \cdot 3 = 6 \geq 5$ ✓. 

Path centers: {0, 5, 9}? 0 and 5: distance 5 ✓. 5 and 9: distance 4 < 5 ✗. {0, 5}: distance 5 ✓. {0, 9}: distance 9 ✓. {0, 5, 9}: 5 and 9 too close. So max 2 path centers: {0, 9} or {0, 5} or {5, 9}.

Using {0, 9} (hubs): hub 1 and endpoint on hub 1 (distance 3): 3 < 5 ✗. So can't use hubs and their own endpoints.

Using {0, 5}: 0 is hub 1, 5 is a path vertex. Hub 1 and endpoint on hub 1: 3 < 5 ✗. Path vertex 5 and endpoint on hub 1 (distance 3 from hub 1): 5 + 3 = 8 ✓. Path vertex 5 and endpoint on hub 2 (distance 3 from hub 2 = distance 12 from hub 1): |12 - 5| = 7 ✓. Hub 1 and endpoint on hub 2: 9 + 3 = 12 ✓. Hub 1 and path vertex 5: 5 ✓.

So: centers = {hub 1, path vertex 5} + endpoints on hub 2 ($d_2$). Check: hub 1 and hub 2 endpoint: 12 ✓. Path vertex 5 and hub 2 endpoint: 7 ✓. Hub 1 and path vertex 5: 5 ✓. Hub 2 endpoints pairwise: 6 ✓.

Total: 2 + $d_2$. Constraint: $10 + 3(d_1 + d_2) \leq 120$, $d_1 + d_2 \leq 36$. But we only use $d_2$, so set $d_1 = 0$: $10 + 3d_2 \leq 120$, $d_2 \leq 36$. Total: 2 + 36 = 38!

Wait, that's way more than 24! Let me double-check.

With $m = 2$ hubs, $p = 9$ (path of length 9 between hubs), $L = 3$ (branches of length 3 on hub 2), $d_1 = 0$ (no branches on hub 1), $d_2 = 36$ (36 branches on hub 2).

Total vertices: $(9 + 1) + 0 \cdot 3 + 36 \cdot 3 = 10 + 108 = 118 \leq 120$ ✓.

Diameter: longest path is from endpoint of a branch on hub 2 to hub 1: $3 + 9 = 12$. Or from hub 1 to hub 2: 9. Or between two endpoints on hub 2: $3 + 3 = 6$. So diameter = 12 ≤ 15 ✓.

Wait, actually, the diameter should be the longest shortest path. The longest path is from hub 1 to an endpoint on hub 2: 9 + 3 = 12. Between two endpoints on hub 2: 6. Between hub 1 and hub 2: 9. So diameter = 12. ✓

Centers: hub
