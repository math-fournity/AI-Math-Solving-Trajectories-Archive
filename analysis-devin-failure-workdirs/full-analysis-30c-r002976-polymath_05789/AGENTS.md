# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   An augmentation on a graph \( G \) is defined as doing the following:

- Take some set \( D \) of vertices in \( G \), and duplicate each vertex \( v_{i} \in D \) to create a new vertex \( v_{i}^{\prime} \).
- If there's an edge between a pair of vertices \( v_{i}, v_{j} \in D \), create an edge between vertices \( v_{i}^{\prime} \) and \( v_{j}^{\prime} \). If there's an edge between a pair of vertices \( v_{i} \in D, v_{j} \notin D \), you can choose to create an edge between \( v_{i}^{\prime} \) and \( v_{j} \) but do not have to.

A graph is called reachable from \( G \) if it can be created through some sequence of augmentations on \( G \). Some graph \( H \) has \( n \) vertices and satisfies that both \( H \) and the complement of \( H \) are reachable from a complete graph of 2021 vertices. If the maximum and minimum values of \( n \) are \( M \) and \( m \), find \( M+m \).       — 题目文本
#   The maximum is \( 2021^{2} \), and the minimum is \( 2021 + 2020 \).

Notice that the chromatic number of any graph reachable from \( G \) is the same as the chromatic number of \( G \). To show this, let the chromatic number of \( G \) be \( a \), and the chromatic number of some graph \( G^{\prime} \) that is reached by performing an augmentation on \( G \) be \( a^{\prime} \). If every vertex \( v_{i}^{\prime} \) in the augmentation is colored the same color as \( v_{i} \), this creates a valid coloring of \( G^{\prime} \) with \( a \) colors, so \( a \geq a^{\prime} \). Additionally, since \( G \) is a subgraph of \( G^{\prime} \), we have \( a^{\prime} \geq a \), so \( a = a^{\prime} \).

This means \( H \) and the complement of \( H \) have chromatic number 2021. For some coloring of \( H \), consider sets \( S_{1}, S_{2}, \ldots, S_{2021} \) of nodes of \( H \) such that \( S_{i} \) contains nodes of the same color. All nodes in \( S_{i} \) are nonadjacent, so in the complement of \( H \), the nodes in \( S_{i} \) will form a \( K_{\left|S_{i}\right|} \). Since the chromatic number of the complement of \( H \) is 2021, we have \(\left|S_{i}\right| \leq 2021\) for all \( i \), so \( M \leq 2021^{2} \). This is achieved when \( H \) is 2021 copies of a \( K_{2021} \), as \( H \) can be achieved by choosing the original \( K_{2021} \) in \( G \) and duplicating it for 2020 augmentations, where no additional edges are added.

Additionally, we can achieve the complement of \( H \) first by coloring \( G \) using 2021 colors. Whenever we duplicate a node \( v_{i} \) to create \( v_{i}^{\prime} \), we color \( v_{i}^{\prime} \) the same color as \( v_{i} \). Then if we duplicate the original \( K_{2021} \) in \( G \) for 2020 augmentations and add edges between each newly created node and each node of a different color, we will create the complement of \( H \). This gives \( M = 2021^{2} \).

Note that since the complement of \( H \) must contain a \( K_{2021} \), there must be a set of 2021 nodes in \( H \) where no two are adjacent. \( H \) also contains a \( K_{2021} \), and since we can have at most one node of the \( K_{2021} \) in the independent set, we will require an additional 2020 nodes, giving \( m \geq 4041 \). If \( H \) is the graph consisting of a \( K_{2021} \) and 2020 isolated nodes, \( H \) can be achieved by duplicating a single node 2020 times and choosing to add no additional edges. Additionally, the complement of \( H \) can be achieved by duplicating the same node of \( G \) 2020 times and each time adding edges from the duplicated node to every other node in the original \( K_{2021} \). This gives \( m = 4041 \).

We have \( M + m = 4041 + 2021^{2} = 4088482 \).

\(\boxed{4088482}\)  — 标准解答
#   Let me analyze this problem carefully.

We have a complete graph on 2021 vertices, $K_{2021}$. An augmentation operation:
- Pick a set $D$ of vertices, duplicate each $v_i \in D$ to create $v_i'$.
- If there's an edge between $v_i, v_j \in D$, create edge between $v_i', v_j'$.
- If there's an edge between $v_i \in D, v_j \notin D$, we may choose to create edge between $v_i'$ and $v_j$.

A graph is reachable from $G$ if it can be created through some sequence of augmentations on $G$.

We need to find graphs $H$ with $n$ vertices such that both $H$ and $\overline{H}$ (complement of $H$) are reachable from $K_{2021}$. Find max and min $n$, then $M + m$.

Let me think about what graphs are reachable from $K_{2021}$.

Starting from $K_{2021}$ (complete graph on 2021 vertices).

When we do an augmentation on $K_{2021}$: pick $D$, duplicate each vertex in $D$. Since $K_{2021}$ is complete, every pair of vertices in $D$ has an edge, so we create all edges among the duplicates $v_i'$. Also, for each $v_i \in D$ and $v_j \notin D$, there's an edge, so we may choose to create edges between $v_i'$ and $v_j$.

So after one augmentation, the new vertices $v_i'$ form a clique (since all pairs in $D$ are connected). Each new vertex $v_i'$ is connected to some subset of the original vertices not in $D$ (we choose which edges to add). Also, $v_i'$ is not connected to $v_i$ (the original it duplicated) — wait, actually $v_i \in D$, and the rule says edges between $v_i' \in D'$ and $v_j \notin D$. $v_i$ is in $D$, so $v_i$ is not in the "$v_j \notin D$" category. So $v_i'$ is never connected to $v_i$ directly through this rule. Actually, $v_i'$ has no edge to $v_i$ at all (there's no rule creating such an edge).

Wait, let me re-read. The original edges are preserved. The new vertex $v_i'$ is a duplicate. The rules only create edges involving $v_i'$. Edges between $v_i'$ and $v_j$ where $v_j \notin D$ are optional. Edges between $v_i'$ and $v_j'$ where $v_j \in D$ are created if $v_i, v_j$ had an edge. There's no rule for edge between $v_i'$ and $v_i$ (since $v_i \in D$, so $v_i$ is not in the "$\notin D$" set). So $v_i'$ and $v_i$ are never connected.

So in the augmented graph, the duplicates form a clique among themselves, and each duplicate $v_i'$ can be connected to any subset of vertices outside $D$ (but not to any vertex in $D$, including its original $v_i$).

Let me think about what structures are reachable. This is related to "clique-width" or some graph generation notion. Let me think more carefully.

Actually, let me think about this differently. Let me consider what graphs can be built.

Key observation: The operation preserves the property that we can think of the graph as being built up by adding cliques of new vertices, where each new vertex can connect to any subset of "old" vertices that are not its "parent" or in its "generation's $D$".

Hmm, this is getting complex. Let me think about reachability from $K_{2021}$ more carefully.

Let me think about small cases first. What graphs are reachable from $K_n$?

From $K_n$, one augmentation with $D$ of size $k$: we add $k$ new vertices forming a clique. Each new vertex $v_i'$ connects to any subset of the $n - k$ vertices not in $D$. So the new vertices form a clique, and each has edges to a chosen subset of the $n-k$ "untouched" original vertices. The new vertices have no edges to the $k$ original vertices in $D$.

Actually wait - in subsequent augmentations, the "graph" is the current graph, not $K_n$. So the edges among existing vertices are whatever they are. Let me re-read.

"An augmentation on a graph $G$..." - so it's on the current graph. The edges in the current graph determine what edges get created.

So if we do a sequence of augmentations, each step operates on the current graph.

Let me think about what's preserved. 

Let me think about the complement. If $H$ is reachable from $K_{2021}$, what can we say about $\overline{H}$?

Note: $K_{2021}$ has complement $\overline{K_{2021}}$ = empty graph on 2021 vertices. But we need $\overline{H}$ to also be reachable from $K_{2021}$, not from $\overline{K_{2021}}$.

Let me think about what graphs are reachable from $K_n$.

Claim: A graph is reachable from $K_n$ iff it can be obtained by starting with $K_n$ and repeatedly adding a clique of new vertices, where each new vertex is adjacent to an arbitrary subset of existing vertices that are NOT in the current $D$.

Hmm, but in later steps, the graph is no longer complete, so the "if there's an edge between $v_i, v_j \in D$, create edge $v_i', v_j'$" rule means the duplicates only form a clique if $D$ is a clique in the current graph.

This is important! In later augmentations, $D$ might not be a clique, so the duplicates don't necessarily form a clique.

Let me reconsider. The duplicates $v_i'$ for $v_i \in D$ form a graph isomorphic to $G[D]$ (the induced subgraph on $D$). And each $v_i'$ can optionally connect to any $v_j \notin D$ that is adjacent to $v_i$ in the current graph.

Wait, re-reading: "If there's an edge between a pair of vertices $v_i \in D, v_j \notin D$, you can choose to create an edge between $v_i'$ and $v_j$."

So $v_i'$ can connect to $v_j \notin D$ only if $v_i$ is adjacent to $v_j$ in the current graph. So the optional edges from $v_i'$ go to a subset of $N(v_i) \setminus D$ (neighbors of $v_i$ not in $D$).

And the mandatory edges: $v_i' v_j'$ is created iff $v_i v_j$ is an edge and both in $D$.

So the new vertex $v_i'$ "inherits" the adjacency structure of $v_i$ within $D$ (mandatory), and can optionally connect to any subset of $v_i$'s neighbors outside $D$.

This is like a "twin" operation but more general. $v_i'$ is a "partial twin" of $v_i$ - it copies $v_i$'s adjacencies within $D$ and optionally copies some adjacencies outside $D$.

Let me think about this in terms of what graphs are reachable.

Let me think about the problem from the perspective of: what is the maximum and minimum number of vertices $n$ such that there exists a graph $H$ on $n$ vertices with both $H$ and $\overline{H}$ reachable from $K_{2021}$?

First, let's think about what graphs are reachable from $K_{2021}$.

Observation 1: $K_{2021}$ itself is reachable (0 augmentations). So $n = 2021$ works if $\overline{K_{2021}}$ (empty graph on 2021 vertices) is also reachable. Is the empty graph reachable from $K_{2021}$? Starting from $K_{2021}$, can we reach the empty graph? We can only add vertices and edges, never remove them. So we can never remove the original edges of $K_{2021}$. The empty graph on 2021 vertices is NOT reachable because the original 2021 vertices always form a clique.

Wait, but we can add more vertices. The question is about $H$ having $n$ vertices. $H$ doesn't have to be on exactly the original 2021 vertices. We can add vertices through augmentations.

So reachable graphs from $K_{2021}$ always contain $K_{2021}$ as a subgraph (the original 2021 vertices always form a clique, and we never remove edges). We can only add vertices and edges.

So if $H$ is reachable from $K_{2021}$, then $H$ contains a $K_{2021}$ subgraph. Similarly, $\overline{H}$ is reachable from $K_{2021}$, so $\overline{H}$ contains a $K_{2021}$ subgraph, meaning $H$ contains an independent set of size 2021.

So $H$ must contain both a clique of size 2021 and an independent set of size 2021.

Now, the minimum $n$: we need $H$ on $n$ vertices with a clique of size 2021 and an independent set of size 2021. The minimum $n$ for a graph with both a clique and independent set of size $k$ is... well, if the clique and independent set are disjoint, $n \geq 2 \cdot 2021 = 4042$. If they overlap, can they? A clique of size 2021 and an independent set of size 2021 can share at most 1 vertex (since any two vertices in the clique are adjacent, but any two in the independent set are non-adjacent, so the intersection has at most 1 vertex). So $n \geq 2021 + 2021 - 1 = 4041$.

But can we achieve $n = 4041$? That would require the clique and independent set to share exactly 1 vertex. Let's think: we need $H$ reachable from $K_{2021}$ (so $H$ contains $K_{2021}$) and $\overline{H}$ reachable from $K_{2021}$ (so $\overline{H}$ contains $K_{2021}$, i.e., $H$ contains an independent set of size 2021).

But we also need $H$ to actually be reachable, not just contain these structures. Let me think about whether $n = 4041$ is achievable.

Actually, let me think more carefully about what graphs are reachable.

Let me consider: from $K_{2021}$, can we add a single vertex that is an isolated vertex (no edges to anything)? 

In one augmentation, pick $D = \{v\}$ for some vertex $v$. Create $v'$. The mandatory edges: none (since $|D| = 1$, no pairs in $D$). The optional edges: $v'$ can connect to any subset of $N(v) \setminus D = $ all other 2020 vertices (since $K_{2021}$ is complete). So we can choose to connect $v'$ to none of them, making $v'$ isolated. But $v'$ is also not connected to $v$ (since $v \in D$). So yes, $v'$ is an isolated vertex!

So from $K_{2021}$, one augmentation with $D = \{v\}$ and choosing no optional edges gives us $K_{2021}$ plus an isolated vertex. This graph has 2022 vertices.

Can we add more isolated vertices? In the next augmentation, the graph is $K_{2021}$ + isolated vertex $v'$. If we pick $D = \{w\}$ for some $w$ in the $K_{2021}$ part, then $w'$ can optionally connect to any subset of $N(w) \setminus \{w\}$. $N(w)$ includes all other 2020 vertices of the $K_{2021}$ part but NOT $v'$ (since $v'$ is isolated, $w$ is not adjacent to $v'$). So $w'$ can connect to any subset of the other 2020 clique vertices. Choosing none, $w'$ is isolated (not connected to $w$, not connected to any clique vertex, and not connected to $v'$ since $v' \notin N(w)$). 

So we can keep adding isolated vertices one at a time, each time picking $D$ to be a single vertex from the original clique and choosing no optional edges.

Alternatively, we can add many isolated vertices at once: pick $D$ to be a set of $k$ vertices from the clique. The duplicates form a clique (since $D$ is a clique in $K_{2021}$). Wait, that's bad - we want isolated vertices, but the duplicates form a clique among themselves.

So to add $k$ isolated vertices at once, we'd pick $D$ of size $k$, but then the $k$ duplicates form a $K_k$. That's not what we want.

To add isolated vertices, we need to add them one at a time (each time $|D| = 1$). Or... we could add them in a way where the duplicates form a clique, and then in a later step... no, we can't remove edges.

So to get $k$ isolated vertices, we need $k$ augmentations, each adding one isolated vertex. That gives us $K_{2021} \cup \overline{K_k}$ (disjoint union of $K_{2021}$ and $k$ isolated vertices) with $2021 + k$ vertices.

Now, is $K_{2021} \cup \overline{K_k}$ reachable from $K_{2021}$? Yes, by the above argument, adding $k$ isolated vertices one at a time.

Is $\overline{K_{2021} \cup \overline{K_k}}$ reachable from $K_{2021}$?

$\overline{K_{2021} \cup \overline{K_k}} = \overline{K_k} \cup K_{2021}$... wait let me compute. The complement of $K_{2021} \cup \overline{K_k}$ (where the $K_{2021}$ and $\overline{K_k}$ are on disjoint vertex sets with no edges between them): the complement has no edges within the $K_{2021}$ part (becomes independent set), all edges within the $\overline{K_k}$ part (becomes $K_k$), and all edges between the two parts. So $\overline{H} = K_k \vee \overline{K_{2021}}$ (join of $K_k$ and independent set of size 2021), which is $K_{k+2021}$ minus the edges within the 2021 part... no.

Let me be more careful. $H = K_{2021} \cup \overline{K_k}$ on vertex set $A \cup B$ where $|A| = 2021, |B| = k$. Edges of $H$: all edges within $A$, no edges within $B$, no edges between $A$ and $B$.

$\overline{H}$: no edges within $A$, all edges within $B$, all edges between $A$ and $B$. So $\overline{H}$ is the complete bipartite graph $K_{2021, k}$ plus $K_k$ on $B$. Actually it's the join $\overline{K_{2021}} \vee K_k$.

Is this reachable from $K_{2021}$? $\overline{H}$ has $2021 + k$ vertices. It contains an independent set of size 2021 (the set $A$). But for $\overline{H}$ to be reachable from $K_{2021}$, it must contain a $K_{2021}$ subgraph. Does it? The clique number of $\overline{H}$: $B$ is a $K_k$, and each vertex in $B$ is connected to all of $A$. But vertices in $A$ have no edges among themselves. So the maximum clique is: take all of $B$ (size $k$) plus one vertex from $A$ (since every vertex in $A$ is connected to every vertex in $B$, but no two vertices in $A$ are connected). So max clique size is $k + 1$.

For $\overline{H}$ to be reachable from $K_{2021}$, we need $k + 1 \geq 2021$, i.e., $k \geq 2020$. So $n = 2021 + k \geq 2021 + 2020 = 4041$.

And at $k = 2020$, $n = 4041$: $\overline{H}$ has a clique of size 2021 (the set $B$ of size 2020 plus one vertex from $A$). But does $\overline{H}$ actually contain $K_{2021}$ as a subgraph? Yes, take $B \cup \{a\}$ for any $a \in A$: this is a clique of size 2021. But is the entire graph $\overline{H}$ reachable from $K_{2021}$? Just containing $K_{2021}$ as a subgraph is necessary but not sufficient.

Hmm, I need to think about what graphs are actually reachable, not just what contains $K_{2021}$.

Let me reconsider. Let me think about what properties reachable graphs have.

From $K_{2021}$, we can only add vertices and edges. The original 2021 vertices always form a clique. So every reachable graph contains $K_{2021}$ as a subgraph on the original vertices.

But we can also add new vertices with various edge patterns. Let me think about what edge patterns are possible for new vertices.

After one augmentation from $K_{2021}$ with $D \subseteq V(K_{2021})$: the new vertices $D' = \{v' : v \in D\}$ form a clique (since $D$ is a clique in $K_{2021}$). Each $v'$ is adjacent to a chosen subset of $V(K_{2021}) \setminus D$. And $v'$ is not adjacent to any vertex in $D$ (including $v$ itself).

So the new vertices form a clique, and each new vertex $v'$ is non-adjacent to exactly $|D|$ vertices of the original graph (the vertices in $D$), and adjacent to a subset of the remaining $2021 - |D|$ original vertices.

In subsequent augmentations, things get more complex because the graph is no longer complete.

Let me think about this differently. Let me consider the concept more abstractly.

Actually, let me think about what the answer might be and work backwards.

The problem asks for $M + m$ where $M$ is the max and $m$ is the min of $n$.

For the maximum: we want the largest $n$ such that there's a graph $H$ on $n$ vertices with both $H$ and $\overline{H}$ reachable from $K_{2021}$.

Is there an upper bound on $n$? Each augmentation adds at least 1 vertex (we must pick $D$ non-empty, I assume - actually, can $D$ be empty? If $D = \emptyset$, we add 0 vertices, which is a no-op. So effectively $D$ is non-empty). There's no limit on the number of augmentations, so we can add arbitrarily many vertices. But the constraint is that both $H$ and $\overline{H}$ must be reachable.

If $H$ is reachable from $K_{2021}$, $H$ contains $K_{2021}$. If $\overline{H}$ is reachable from $K_{2021}$, $\overline{H}$ contains $K_{2021}$, so $H$ contains $\overline{K_{2021}}$ (independent set of size 2021).

But there's no upper bound from this alone - we can have arbitrarily large graphs with both a large clique and large independent set.

Wait, but maybe there are more constraints from the reachability structure. Let me think again...

Actually, maybe the reachability imposes more structure. Let me think about what graphs are reachable from $K_n$ more carefully.

Let me think about a key invariant. Consider the "non-adjacency" structure. 

Hmm, let me think about this from the perspective of the complement. If $G$ is reachable from $K_n$, what can we say about $\overline{G}$?

The augmentation operation on $G$ in terms of $\overline{G}$: 
- We duplicate vertices in $D$, creating $v_i'$.
- In $G$, $v_i' v_j'$ is an edge iff $v_i v_j$ is an edge (both in $D$). In $\overline{G}$, $v_i' v_j'$ is a non-edge iff $v_i v_j$ is a non-edge, i.e., $v_i' v_j'$ is an edge iff $v_i v_j$ is an edge in $\overline{G}$... wait, let me be careful.

In $G$: $v_i' v_j'$ edge iff $v_i v_j$ edge (for $v_i, v_j \in D$). In $\overline{G}$: $v_i' v_j'$ non-edge iff $v_i v_j$ non-edge in $\overline{G}$... no. $\overline{G}$ has edge $v_i' v_j'$ iff $G$ has non-edge $v_i' v_j'$. $G$ has non-edge $v_i' v_j'$ iff $G$ has non-edge $v_i v_j$ (for $v_i, v_j \in D$). So $\overline{G}$ has edge $v_i' v_j'$ iff $G$ has non-edge $v_i v_j$ iff $\overline{G}$ has edge $v_i v_j$.

So in $\overline{G}$, the duplicates also copy the induced subgraph on $D$! (The duplicates in $\overline{G}$ form the same graph as $G[D]$... wait no. In $\overline{G}$, $v_i' v_j'$ is an edge iff $\overline{G}$ has $v_i v_j$ as an edge. So the duplicates in $\overline{G}$ form a copy of $\overline{G}[D]$.)

For the optional edges: in $G$, $v_i' v_j$ (for $v_i \in D, v_j \notin D$) can be an edge only if $v_i v_j$ is an edge in $G$. In $\overline{G}$, $v_i' v_j$ is a non-edge if $v_i v_j$ is a non-edge in $G$... 

In $\overline{G}$: $v_i' v_j$ edge iff $G$ has $v_i' v_j$ non-edge. $G$ has $v_i' v_j$ non-edge in two cases: (1) $v_i v_j$ is a non-edge in $G$ (then $v_i' v_j$ is forced to be a non-edge), or (2) $v_i v_j$ is an edge in $G$ but we chose not to add $v_i' v_j$.

In $\overline{G}$: $v_i' v_j$ edge iff $G$ has $v_i' v_j$ non-edge. This happens iff either $v_i v_j$ is a non-edge in $G$ (i.e., $\overline{G}$ has $v_i v_j$ edge), or $v_i v_j$ is an edge in $G$ but we chose not to connect (i.e., $\overline{G}$ has $v_i v_j$ non-edge, and we chose to have $\overline{G}$ edge $v_i' v_j$).

So in $\overline{G}$: $v_i' v_j$ (for $v_i \in D, v_j \notin D$) is forced to be an edge if $\overline{G}$ has $v_i v_j$ edge, and can optionally be an edge if $\overline{G}$ has $v_i v_j$ non-edge.

This is exactly the same augmentation rule! The augmentation operation is "self-complementary" in some sense. If we apply an augmentation to $G$ getting $G'$, then $\overline{G'}$ is obtained from $\overline{G}$ by an augmentation with the same $D$ and complementary choices.

So: $G'$ is reachable from $G$ via augmentation with set $D$ and certain edge choices iff $\overline{G'}$ is reachable from $\overline{G}$ via augmentation with set $D$ and complementary edge choices.

This means: $H$ is reachable from $K_{2021}$ iff $\overline{H}$ is reachable from $\overline{K_{2021}}$ (empty graph on 2021 vertices).

So the condition "$H$ and $\overline{H}$ are both reachable from $K_{2021}$" becomes:
- $H$ is reachable from $K_{2021}$
- $\overline{H}$ is reachable from $K_{2021}$, which by the duality means $H$ is reachable from $\overline{K_{2021}}$.

So we need $H$ to be reachable from both $K_{2021}$ and $\overline{K_{2021}}$ (empty graph on 2021 vertices).

Now, what graphs are reachable from $\overline{K_{2021}}$ (empty graph)?

From the empty graph, an augmentation with $D$: the duplicates $v_i'$ form the same induced subgraph as $D$ in the current graph. Since the current graph is empty, $D$ has no edges, so the duplicates have no edges among them. The optional edges: $v_i'$ can connect to $v_j \notin D$ only if $v_i v_j$ is an edge, but there are no edges, so no optional edges. So from the empty graph, we can only add isolated vertices. We can never create any edges!

So the only graph reachable from $\overline{K_{2021}}$ is $\overline{K_n}$ for any $n \geq 2021$ (the empty graph on $n$ vertices).

Wait, that can't be right. Let me re-check.

From $\overline{K_{2021}}$ (empty graph), augmentation with $D$: 
- Duplicates form induced subgraph of $D$, which is empty (no edges in $D$ since graph is empty). So duplicates have no edges among them.
- Optional edges: $v_i'$ can connect to $v_j \notin D$ only if $v_i v_j$ is an edge in current graph. But current graph is empty, so no edges. So no optional edges.

So indeed, from the empty graph, we can only add more isolated vertices. The only reachable graph is the empty graph on $n \geq 2021$ vertices.

So if $H$ is reachable from $\overline{K_{2021}}$, then $H = \overline{K_n}$ (empty graph on $n$ vertices) for some $n \geq 2021$.

And we need $H = \overline{K_n}$ to also be reachable from $K_{2021}$. Is $\overline{K_n}$ reachable from $K_{2021}$?

$\overline{K_n}$ has no edges. But $K_{2021}$ has all edges, and we can never remove edges. So the original 2021 vertices always form a clique. For $\overline{K_n}$ to be reachable, we'd need no edges at all, but the original 2021 vertices have all edges. Contradiction (for $n \geq 2021$).

So there's NO graph $H$ that is reachable from both $K_{2021}$ and $\overline{K_{2021}}$? That would mean no $H$ satisfies the condition, which contradicts the problem asking for $M + m$.

I must have made an error. Let me re-examine the duality.

Let me re-examine: if $G'$ is obtained from $G$ by augmentation, is $\overline{G'}$ obtained from $\overline{G}$ by augmentation?

$G'$ has vertex set $V(G) \cup D'$ where $D' = \{v' : v \in D\}$.

Edges of $G'$:
- All edges of $G$ (on $V(G)$).
- For $v_i, v_j \in D$: edge $v_i' v_j'$ iff edge $v_i v_j$ in $G$.
- For $v_i \in D, v_j \notin D$: edge $v_i' v_j$ optionally, only if edge $v_i v_j$ in $G$.
- No edge $v_i' v_i$.

$\overline{G'}$ has vertex set $V(G) \cup D'$.

Edges of $\overline{G'}$:
- All non-edges of $G$ (on $V(G)$) become edges.
- For $v_i, v_j \in D$: edge $v_i' v_j'$ iff non-edge $v_i v_j$ in $G$, i.e., edge $v_i v_j$ in $\overline{G}$.
- For $v_i \in D, v_j \notin D$: edge $v_i' v_j$ iff non-edge $v_i' v_j$ in $G'$. $v_i' v_j$ is a non-edge in $G'$ if either (a) $v_i v_j$ is a non-edge in $G$ (forced non-edge), or (b) $v_i v_j$ is an edge in $G$ but we chose not to add $v_i' v_j$.
  - In $\overline{G}$: case (a) means $v_i v_j$ is an edge in $\overline{G}$, and $v_i' v_j$ is forced to be an edge in $\overline{G'}$.
  - Case (b) means $v_i v_j$ is a non-edge in $\overline{G}$, and $v_i' v_j$ can optionally be an edge in $\overline{G'}$.
- Edge $v_i' v_i$: in $G'$, $v_i' v_i$ is a non-edge (always). So in $\overline{G'}$, $v_i' v_i$ is always an edge.

Now, is $\overline{G'}$ obtainable from $\overline{G}$ by an augmentation? In an augmentation of $\overline{G}$ with set $D$:
- Duplicates $v_i'$ form induced subgraph of $D$ in $\overline{G}$: edge $v_i' v_j'$ iff edge $v_i v_j$ in $\overline{G}$. ✓ Matches.
- For $v_i \in D, v_j \notin D$: $v_i' v_j$ edge in the augmentation only if $v_i v_j$ edge in $\overline{G}$, and it's optional. 
  - In $\overline{G'}$: $v_i' v_j$ is forced edge if $v_i v_j$ edge in $\overline{G}$, and optional if $v_i v_j$ non-edge in $\overline{G}$. 
  - This matches! The forced edges correspond to the mandatory part, and the optional edges correspond to the optional part.
- Edge $v_i' v_i$: in an augmentation of $\overline{G}$, $v_i' v_i$ should be a non-edge (since $v_i \in D$, and $v_i'$ is never connected to $v_i$). But in $\overline{G'}$, $v_i' v_i$ is always an edge!

This is the discrepancy! In $\overline{G'}$, $v_i' v_i$ is an edge, but in an augmentation of $\overline{G}$, $v_i' v_i$ would be a non-edge.

So the duality is NOT exact. The issue is the $v_i' v_i$ edge/non-edge.

So my earlier analysis was wrong. Let me reconsider.

In $G'$: $v_i' v_i$ is always a non-edge (for $v_i \in D$).
In $\overline{G'}$: $v_i' v_i$ is always an edge.

In an augmentation of $\overline{G}$ with $D$: $v_i' v_i$ is always a non-edge.

So $\overline{G'}$ has edges $v_i' v_i$ that an augmentation of $\overline{G}$ would not have. The duality breaks because of these "diagonal" edges.

Hmm, so the operation is not self-complementary. Let me reconsider the problem.

OK so let me go back to directly analyzing what graphs are reachable from $K_{2021}$.

Let me think about this more carefully. Let me consider the structure of reachable graphs.

From $K_n$, the first augmentation with $D$ of size $d$: adds $d$ new vertices forming a clique (since $D$ is a clique in $K_n$). Each new vertex $v_i'$ is non-adjacent to the $d$ vertices in $D$ (including $v_i$), and adjacent to a chosen subset of the $n - d$ remaining original vertices.

So after one step, the graph has the original $K_n$ plus a clique $D'$ of size $d$, where each vertex in $D'$ is non-adjacent to all of $D$ and adjacent to some subset of $V \setminus D$.

Key structural property: the new vertices $D'$ are non-adjacent to exactly the set $D$ (among the original vertices). And $D'$ forms a clique.

In the second augmentation, we pick a new $D_2$ from the current graph. The current graph has $n + d$ vertices. $D_2$ can include both original and new vertices. The duplicates $D_2'$ form the induced subgraph of $D_2$ in the current graph.

This is getting complex. Let me think about it differently.

Let me think about what the problem is really asking. We need both $H$ and $\overline{H}$ reachable from $K_{2021}$. Let me think about necessary conditions.

Necessary condition 1: $H$ contains $K_{2021}$ (the original vertices form a clique that's never broken).

Necessary condition 2: $\overline{H}$ contains $K_{2021}$, so $H$ contains an independent set of size 2021.

But there might be more structure. Let me think about what graphs are reachable from $K_n$.

Let me consider the "twin" structure. When we duplicate $v_i$ to get $v_i'$, $v_i'$ is a "twin" of $v_i$ in some sense - it copies $v_i$'s adjacency to $D$ and optionally to $V \setminus D$. But $v_i'$ is not adjacent to $v_i$ itself.

Actually, let me think about a specific important class of reachable graphs.

Claim: From $K_n$, we can reach any graph that contains $K_n$ as a subgraph and where the additional vertices can be added one at a time, each being a "partial twin" of some existing vertex.

Hmm, but we can also add multiple vertices at once, and the duplicates interact.

Let me think about the problem from a higher level. This is a competition problem, so there should be a clean answer.

Let me think about what $M$ and $m$ could be.

For $m$ (minimum): We need $H$ on $n$ vertices, both $H$ and $\overline{H}$ reachable from $K_{2021}$.

$H$ contains $K_{2021}$ (clique of size 2021).
$\overline{H}$ contains $K_{2021}$, so $H$ contains independent set of size 2021.

These two structures (clique and independent set) share at most 1 vertex. So $n \geq 4041$.

Can we achieve $n = 4041$? We need to construct $H$ on 4041 vertices with a clique $C$ of size 2021 and independent set $I$ of size 2021 sharing exactly 1 vertex, such that $H$ is reachable from $K_{2021}$ and $\overline{H}$ is reachable from $K_{2021}$.

Let me try: Let $C$ be the original 2021 vertices (forming $K_{2021}$). We need to add 2020 more vertices forming an independent set, with one of them... wait, we need $|C \cap I| = 1$. So $I$ has 2020 vertices outside $C$ and 1 vertex in $C$.

The 2020 new vertices must form an independent set (along with one vertex from $C$). The new vertices are non-adjacent to each other and non-adjacent to one specific vertex in $C$.

Can we reach such a graph from $K_{2021}$? We need to add 2020 vertices that are pairwise non-adjacent and each non-adjacent to some fixed vertex $c_0 \in C$.

From $K_{2021}$, to add a vertex $v'$ that is non-adjacent to $c_0$: pick $D = \{c_0\}$. Then $v'$ is non-adjacent to $c_0$ (mandatory) and can be adjacent to any subset of the other 2020 vertices. To make $v'$ non-adjacent to other new vertices, we need to be careful.

If we add the 2020 vertices one at a time, each time picking $D = \{c_0\}$: 
- First new vertex $u_1$: $D = \{c_0\}$, $u_1$ non-adjacent to $c_0$, can be adjacent to any of the other 2020 original vertices. Choose to connect $u_1$ to all of them (or some subset).
- Second new vertex $u_2$: $D = \{c_0\}$, $u_2$ non-adjacent to $c_0$, can be adjacent to any subset of $N(c_0) \setminus \{c_0\}$. But $N(c_0)$ in the current graph includes all original vertices except $c_0$... and also $u_1$ if $u_1$ is adjacent to $c_0$. But $u_1$ is NOT adjacent to $c_0$ (we made it non-adjacent). So $c_0$'s neighbors are the other 2020 original vertices (not $u_1$). So $u_2$ can be adjacent to any subset of the 2020 original vertices (other than $c_0$), but NOT to $u_1$ (since $u_1 \notin N(c_0)$).

So $u_2$ is automatically non-adjacent to $u_1$! Because $u_1$ is not a neighbor of $c_0$, and $u_2$ can only connect to neighbors of $c_0$.

Similarly, $u_3$ is non-adjacent to $u_1$ and $u_2$ (since neither is a neighbor of $c_0$). And so on.

So by repeatedly picking $D = \{c_0\}$, each new vertex is automatically non-adjacent to all previously added new vertices (since they're all non-neighbors of $c_0$), and non-adjacent to $c_0$. Each new vertex can be adjacent to any subset of the 2020 original vertices (other than $c_0$).

So we can add 2020 vertices, all non-adjacent to $c_0$ and pairwise non-adjacent, and each adjacent to any chosen subset of $C \setminus \{c_0\}$.

This gives us a graph where:
- $C = \{c_0, c_1, \ldots, c_{2020}\}$ forms $K_{2021}$.
- $U = \{u_1, \ldots, u_{2020}\}$ is an independent set.
- Each $u_i$ is non-adjacent to $c_0$ and adjacent to some subset of $\{c_1, \ldots, c_{2020}\}$.
- $I = \{c_0, u_1, \ldots, u_{2020}\}$ is an independent set of size 2021. ✓

So $H$ is reachable from $K_{2021}$ and contains an independent set of size 2021.

Now, is $\overline{H}$ reachable from $K_{2021}$?

$\overline{H}$: 
- $C$ is an independent set (no edges within $C$).
- $U$ is a clique (all edges within $U$).
- $c_0$ is adjacent to all of $U$ (since $c_0$ is non-adjacent to all $u_i$ in $H$).
- $c_i$ ($i \geq 1$) is adjacent to $u_j$ iff $c_i$ is non-adjacent to $u_j$ in $H$.

For $\overline{H}$ to be reachable from $K_{2021}$, it must contain $K_{2021}$. The clique number of $\overline{H}$: $U$ is a clique of size 2020. $c_0$ is adjacent to all of $U$, so $U \cup \{c_0\}$ is a clique of size 2021. ✓

But we need more than just containing $K_{2021}$ - we need $\overline{H}$ to actually be reachable.

$\overline{H}$ has 4041 vertices. It contains a clique $U \cup \{c_0\}$ of size 2021. The remaining 2020 vertices are $c_1, \ldots, c_{2020}$, which form an independent set in $\overline{H}$ (since they form a clique in $H$). Each $c_i$ is adjacent to some subset of $U$ in $\overline{H}$ (depending on the adjacencies in $H$), and $c_i$ is adjacent to $c_0$ in $\overline{H}$ (since $c_i c_0$ is an edge in $H$, so non-edge in $\overline{H}$)... wait, $c_i c_0$ is an edge in $H$ (both in $C$, which is a clique), so $c_i c_0$ is a non-edge in $\overline{H}$. And $c_i c_j$ for $i, j \geq 1$ is an edge in $H$ (clique), so non-edge in $\overline{H}$.

So in $\overline{H}$:
- $U \cup \{c_0\}$ is a clique of size 2021.
- $\{c_1, \ldots, c_{2020}\}$ is an independent set of size 2020.
- $c_0$ is non-adjacent to $c_i$ for $i \geq 1$.
- $c_i$ is adjacent to $u_j$ iff $c_i$ is non-adjacent to $u_j$ in $H$.

For $\overline{H}$ to be reachable from $K_{2021}$: we need to start with $K_{2021}$ on some 2021 vertices and build up. The natural choice is to start with $K_{2021}$ on $U \cup \{c_0\}$. Then we need to add $c_1, \ldots, c_{2020}$ as new vertices.

In $\overline{H}$, the vertices $c_1, \ldots, c_{2020}$ form an independent set and are non-adjacent to $c_0$. This is exactly the same structure as before! We need to add 2020 vertices that are pairwise non-adjacent and non-adjacent to $c_0$.

By the same argument as before, we can do this by repeatedly picking $D = \{c_0\}$ in augmentations of $\overline{H}$'s construction. Each new vertex $c_i$ would be non-adjacent to $c_0$ and to all previously added $c_j$'s, and can be adjacent to any subset of $U$ (the other 2020 vertices of the original clique, which are neighbors of $c_0$).

The adjacency of $c_i$ to $U$ in $\overline{H}$ is: $c_i$ adjacent to $u_j$ iff $c_i$ non-adjacent to $u_j$ in $H$. In $H$, $c_i$ is adjacent to a chosen subset of $\{c_1, \ldots, c_{2020}\}$... wait, I need to be more careful.

In $H$, the new vertices $u_j$ are each adjacent to a chosen subset of $C \setminus \{c_0\} = \{c_1, \ldots, c_{2020}\}$. Let's say $u_j$ is adjacent to $c_i$ in $H$ iff $j \in S_i$ (some subset). Then in $\overline{H}$, $c_i$ is adjacent to $u_j$ iff $j \notin S_i$.

When building $\overline{H}$ from $K_{2021}$ on $U \cup \{c_0\}$, we add $c_i$ by picking $D = \{c_0\}$, and $c_i$ can be adjacent to any subset of $U$ (the neighbors of $c_0$ in the current graph, which are all of $U$). We need $c_i$ to be adjacent to $\{u_j : j \notin S_i\}$ in $\overline{H}$. Since we can choose any subset, this is fine!

So $\overline{H}$ is reachable from $K_{2021}$! 

Wait, but I need to be more careful. When building $\overline{H}$, the order of adding $c_1, \ldots, c_{2020}$ matters. When we add $c_i$, the current graph has $U \cup \{c_0\}$ plus previously added $c_j$'s. The new vertex $c_i$ (duplicate of $c_0$) can be adjacent to any subset of $N(c_0) \setminus \{c_0\}$ in the current graph. $N(c_0)$ in the current graph includes all of $U$ (since $U \cup \{c_0\}$ is a clique) but NOT any previously added $c_j$ (since they're non-adjacent to $c_0$). So $c_i$ can be adjacent to any subset of $U$, and is automatically non-adjacent to all previously added $c_j$'s. 

So we can choose $c_i$'s adjacency to $U$ to be exactly $\{u_j : j \notin S_i\}$, which matches $\overline{H}$. And $c_i$ is non-adjacent to $c_0$ and to all other $c_j$'s, which also matches $\overline{H}$.

So $\overline{H}$ is reachable from $K_{2021}$. 

Therefore $n = 4041$ is achievable, and $m = 4041$.

Wait, but I should double-check: is $n = 4040$ possible? We need a clique of size 2021 and an independent set of size 2021 in a graph on 4040 vertices. The clique and independent set share at most 1 vertex, so $n \geq 2021 + 2021 - 1 = 4041$. So $n = 4040$ is impossible. Thus $m = 4041$.

Now for $M$ (maximum): Is there an upper bound on $n$?

We need $H$ on $n$ vertices with both $H$ and $\overline{H}$ reachable from $K_{2021}$.

$H$ contains $K_{2021}$ (clique of size 2021 on the original vertices).
$\overline{H}$ contains $K_{2021}$, so $H$ contains independent set of size 2021.

But as I noted, from $K_{2021}$ we can add arbitrarily many vertices (by doing many augmentations). So is $n$ unbounded?

Wait, let me think again. The constraint is that both $H$ and $\overline{H}$ are reachable from $K_{2021}$. 

$H$ reachable from $K_{2021}$: $H$ contains $K_{2021}$ as a subgraph (on the original 2021 vertices), plus additional vertices and edges.

$\overline{H}$ reachable from $K_{2021}$: $\overline{H}$ contains $K_{2021}$ as a subgraph (on some 2021 vertices of $H$), meaning $H$ has an independent set of size 2021.

But there might be more constraints from the reachability structure. Let me think...

Actually, I think the key constraint is more subtle. Let me think about what graphs are reachable from $K_n$.

Let me think about the "non-neighborhood" structure. When we add a vertex $v'$ as a duplicate of $v$ (with $D = \{v\}$), $v'$ is non-adjacent to $v$ and can be adjacent to any subset of $N(v) \setminus \{v\}$. So $v'$'s non-neighbors include $v$ and all non-neighbors of $v$ (since $v'$ can only connect to $v$'s neighbors).

More generally, $v'$'s non-neighborhood contains $v$'s non-neighborhood plus $v$ itself.

This suggests that non-neighborhoods can only grow. Let me formalize this.

Define the "non-neighborhood" of a vertex $u$ as $\bar{N}(u) = V \setminus (N(u) \cup \{u\})$ (the set of vertices non-adjacent to $u$, excluding $u$ itself). Actually, let me include $u$ itself: let $\bar{N}[u] = V \setminus N(u)$ (non-neighbors including $u$).

When we duplicate $v$ to get $v'$ with $D = \{v\}$: $v'$ is non-adjacent to $v$ and to all non-neighbors of $v$ (since $v'$ can only connect to $v$'s neighbors). $v'$ can be adjacent to any subset of $N(v) \setminus \{v\}$... wait, $v'$ can be adjacent to any subset of $N(v) \setminus D = N(v) \setminus \{v\}$. But $v \in N(v)$? In $K_n$, $v$ is not in $N(v)$ (no self-loops). So $N(v) \setminus \{v\} = N(v)$. And $v'$ is non-adjacent to $v$ (since $v \in D$). So $\bar{N}[v'] \supseteq \bar{N}[v] \cup \{v\}$... actually $\bar{N}[v'] = \bar{N}[v] \cup \{v\} \cup (\text{chosen non-neighbors among } N(v))$.

Hmm, this is getting complicated. Let me think about it differently.

Let me think about the problem in terms of a specific structural property.

Consider the relation between a vertex and its duplicate. When $v'$ is created as a duplicate of $v$ (in some augmentation where $v \in D$), $v'$ is non-adjacent to $v$. This non-adjacency is permanent (we never remove edges or non-edges... well, we never remove edges, but non-edges can become edges in later augmentations? No! We only add edges in augmentations, never remove them. And we only add edges involving new vertices. So edges between existing vertices are never changed.

Wait, that's a key point. Once two vertices exist, their adjacency is fixed forever. Augmentations only add new vertices and edges involving those new vertices. Existing edges and non-edges are never changed.

So the graph is built up monotonically: we start with $K_{2021}$ and add vertices one batch at a time, where each batch's edges to existing vertices are determined at creation time and never change.

This means the reachable graphs from $K_{2021}$ are exactly those that can be built by adding vertices in some order, where each vertex $v$ (when added) is a "partial twin" of some existing vertex $u$ (its "parent"), meaning:
- $v$ is non-adjacent to $u$.
- $v$ can be adjacent to any subset of $N(u) \setminus D$ where $D$ is the set being duplicated in this step.
- If multiple vertices are added in the same step, they form the induced subgraph of $D$.

Actually, when adding a batch $D'$ (duplicates of $D$), the new vertices form $G[D]$ (induced subgraph), and each $v_i' \in D'$ is non-adjacent to all of $D$ and can be adjacent to any subset of $N(v_i) \setminus D$.

Hmm, let me think about this more carefully for the case $|D| = 1$. If we always use $|D| = 1$, then each step adds one vertex $v'$ as a duplicate of some existing vertex $v$, where:
- $v'$ is non-adjacent to $v$.
- $v'$ can be adjacent to any subset of $N(v)$ (the neighbors of $v$ in the current graph).
- $v'$ is non-adjacent to all non-neighbors of $v$ (in the current graph).

So $v'$'s adjacency is: non-adjacent to $v$ and all non-neighbors of $v$; adjacent to a chosen subset of $N(v)$.

This means: $\bar{N}[v'] \supseteq \bar{N}[v] \cup \{v\}$, with equality if we connect $v'$ to all of $N(v)$.

And $N[v'] \subseteq N[v] \setminus \{v\} \cup \{v'\}$... hmm, $v'$ is adjacent to a subset of $N(v)$, and $v'$ is not adjacent to $v$. So $N(v') \subseteq N(v)$, and $v' \notin N(v')$ (no self-loops), and $v \notin N(v')$.

Key insight: $N(v') \subseteq N(v)$. The neighborhood of the duplicate is a subset of the neighborhood of the original.

And $\bar{N}[v'] \supseteq \bar{N}[v] \cup \{v\}$. The non-neighborhood (including self) of the duplicate is a superset of the non-neighborhood of the original plus the original.

Now, if we always use $|D| = 1$, we can build any graph where vertices can be ordered $v_1, v_2, \ldots, v_n$ (with $v_1, \ldots, v_{2021}$ being the original clique) such that for each $v_i$ ($i > 2021$), there exists a "parent" $v_j$ with $j < i$ such that $N(v_i) \subseteq N(v_j)$ (in the final graph, since adjacencies are fixed at creation time and never change, $N(v_i)$ in the final graph equals $N(v_i)$ at creation time, which is a subset of $N(v_j)$ at creation time, which equals $N(v_j)$ in the final graph restricted to vertices existing at that time... 

Hmm wait, this isn't quite right because $N(v_j)$ grows over time as more vertices are added. Let me reconsider.

At the time $v_i$ is created (as a duplicate of $v_j$), $v_i$'s neighbors are a subset of $v_j$'s neighbors at that time. After that, new vertices may be added that are adjacent to $v_j$ but not to $v_i$ (or vice versa). So in the final graph, $N(v_i)$ is NOT necessarily a subset of $N(v_j)$.

But among the vertices that existed at the time of $v_i$'s creation, $v_i$'s neighbors are a subset of $v_j$'s neighbors. And $v_i$ is non-adjacent to $v_j$.

For vertices created after $v_i$, their adjacency to $v_i$ and $v_j$ is independent (determined by their own creation).

So the subset relation only holds for vertices existing at creation time. This makes the analysis more complex.

Let me think about this problem differently. Maybe I should think about what structures are forced.

Let me consider the problem from the competition perspective. The answer is $M + m$. We found $m = 4041$. What about $M$?

Let me think about whether $n$ can be arbitrarily large.

Consider building $H$ as follows: Start with $K_{2021}$ on vertices $C = \{c_0, \ldots, c_{2020}\}$. Add 2020 vertices $U = \{u_1, \ldots, u_{2020}\}$ as before (each a duplicate of $c_0$, non-adjacent to $c_0$ and to each other, adjacent to chosen subsets of $C \setminus \{c_0\}$). This gives $n = 4041$.

Can we add more vertices? Let's add another vertex $w$ as a duplicate of some existing vertex. Say $w$ is a duplicate of $u_1$. Then $w$ is non-adjacent to $u_1$, and $w$ can be adjacent to any subset of $N(u_1)$ (at the current time). $N(u_1)$ includes $u_1$'s neighbors among $C \setminus \{c_0\}$ (the chosen subset) and possibly some other $u_j$'s... but $u_j$'s are non-adjacent to $u_1$ (they're all non-adjacent to each other). So $N(u_1) = $ chosen subset of $C \setminus \{c_0\}$.

$w$ is non-adjacent to $u_1$, $c_0$ (since $c_0 \notin N(u_1)$), and all other $u_j$ (since $u_j \notin N(u_1)$). $w$ can be adjacent to any subset of $N(u_1) \subseteq C \setminus \{c_0\}$.

So $w$ is non-adjacent to $c_0$, all of $U$, and adjacent to a subset of $C \setminus \{c_0\}$. This is similar to the $u_i$'s but $w$ is a duplicate of $u_1$ instead of $c_0$.

In $H$, $w$ is non-adjacent to $c_0$ and all $u_j$'s, and adjacent to some subset of $C \setminus \{c_0\}$. So $w$ can be added to the independent set $I = \{c_0, u_1, \ldots, u_{2020}\}$... wait, $w$ is non-adjacent to all of $I$? $w$ is non-adjacent to $c_0$ ✓, non-adjacent to all $u_j$ ✓. But $w$ is adjacent to some subset of $C \setminus \{c_0\}$. The elements of $C \setminus \{c_0\}$ are $c_1, \ldots, c_{2020}$, which are NOT in $I$ (except $c_0$). So $w$ is non-adjacent to all of $I$, meaning $I \cup \{w\}$ is an independent set of size 2022.

But we need $\overline{H}$ to be reachable from $K_{2021}$, which requires $\overline{H}$ to contain $K_{2021}$, i.e., $H$ to contain an independent set of size 2021. Having a larger independent set is fine.

But we also need $\overline{H}$ to be reachable, not just contain $K_{2021}$. Let me check if $\overline{H}$ (with $w$ added) is reachable.

In $\overline{H}$: $w$ is adjacent to $c_0$, all $u_j$'s, and non-adjacent to some subset of $C \setminus \{c_0\}$. 

For $\overline{H}$ to be reachable from $K_{2021}$, we need to build it from $K_{2021}$. The clique in $\overline{H}$ is $U \cup \{c_0\}$ (size 2021). We add $c_1, \ldots, c_{2020}$ and $w$ as new vertices.

In $\overline{H}$, $w$ is adjacent to $c_0$ and all $u_j$'s, and non-adjacent to some $c_i$'s. Can we add $w$ as a duplicate of some vertex in $\overline{H}$'s construction?

If we add $w$ as a duplicate of $u_1$ in $\overline{H}$'s construction: $w$ is non-adjacent to $u_1$, and can be adjacent to any subset of $N(u_1)$ in $\overline{H}$ at that time. In $\overline{H}$, $N(u_1)$ includes $c_0$ and all other $u_j$'s (since $U \cup \{c_0\}$ is a clique) and some $c_i$'s. But $w$ needs to be adjacent to $c_0$ and all $u_j$'s in $\overline{H}$. $w$ is non-adjacent to $u_1$ (its parent), which is fine since $w$ is adjacent to $u_1$ in $\overline{H}$... 

Wait, no. In $\overline{H}$, $w$ IS adjacent to $u_1$ (since $w$ is non-adjacent to $u_1$ in $H$). But if $w$ is a duplicate of $u_1$, then $w$ is non-adjacent to $u_1$. Contradiction!

So $w$ cannot be a duplicate of $u_1$ in $\overline{H}$'s construction. Let me think about what $w$ can be a duplicate of.

In $\overline{H}$, $w$ is adjacent to $c_0$ and all $u_j$. $w$ is non-adjacent to some $c_i$'s. If $w$ is a duplicate of $c_0$ in $\overline{H}$'s construction: $w$ is non-adjacent to $c_0$. But $w$ is adjacent to $c_0$ in $\overline{H}$. Contradiction.

If $w$ is a duplicate of $u_j$ for some $j$: $w$ is non-adjacent to $u_j$. But $w$ is adjacent to all $u_j$ in $\overline{H}$. Contradiction.

If $w$ is a duplicate of $c_i$ for some $i \geq 1$: $w$ is non-adjacent to $c_i$. In $\overline{H}$, $w$ is non-adjacent to some $c_i$'s, so this could work for one of those. $w$ can be adjacent to any subset of $N(c_i)$ in $\overline{H}$ at that time. $N(c_i)$ in $\overline{H}$ includes $c_0$ (is $c_0$ adjacent to $c_i$ in $\overline{H}$? In $H$, $c_0 c_i$ is an edge (both in clique $C$), so in $\overline{H}$, $c_0 c_i$ is a non-edge. So $c_0 \notin N(c_i)$ in $\overline{H}$.) Hmm, so $c_i$'s neighbors in $\overline{H}$ are some subset of $U$ (those $u_j$ that are non-adjacent to $c_i$ in $H$). And $c_i$ is non-adjacent to $c_0$, all other $c_k$'s, and some $u_j$'s.

If $w$ is a duplicate of $c_i$, then $w$ is non-adjacent to $c_i$, and can be adjacent to any subset of $N(c_i) \subseteq U$. But $w$ needs to be adjacent to $c_0$ in $\overline{H}$, and $c_0 \notin N(c_i)$. So $w$ cannot be adjacent to $c_0$. Contradiction.

So $w$ cannot be added as a single-vertex duplicate in $\overline{H}$'s construction. What about multi-vertex $D$?

Hmm, this is getting complicated. Let me think about whether we can add $w$ using a larger $D$.

Actually, maybe I should think about this more carefully. Let me consider what happens when $|D| > 1$.

If $D = \{c_0, u_1\}$ in $\overline{H}$'s construction: we create $c_0'$ and $u_1'$. $c_0' u_1'$ is an edge iff $c_0 u_1$ is an edge in $\overline{H}$. In $\overline{H}$, $c_0$ is adjacent to $u_1$ (since $c_0$ is non-adjacent to $u_1$ in $H$). So $c_0' u_1'$ is an edge.

$c_0'$ is non-adjacent to $c_0$ and $u_1$, and can be adjacent to any subset of $N(c_0) \setminus D = N(c_0) \setminus \{c_0, u_1\}$. In $\overline{H}$, $N(c_0)$ includes all of $U$ (since $U \cup \{c_0\}$ is a clique) and... $c_0$ is non-adjacent to all $c_i$'s in $\overline{H}$. So $N(c_0) = U$. So $c_0'$ can be adjacent to any subset of $U \setminus \{u_1\}$.

$u_1'$ is non-adjacent to $c_0$ and $u_1$, and can be adjacent to any subset of $N(u_1) \setminus D = N(u_1) \setminus \{c_0, u_1\}$. In $\overline{H}$, $N(u_1)$ includes $c_0$ and all other $u_j$'s and some $c_i$'s. So $u_1'$ can be adjacent to any subset of $(U \setminus \{u_1\}) \cup \{c_i : u_1 \text{ adj } c_i \text{ in } \overline{H}\}$.

This is getting very complex. Let me step back and think about the problem more abstractly.

Let me think about what property a graph must have to be reachable from $K_n$, and what property its complement must have.

Actually, let me think about this problem from a different angle. Let me consider the concept of "co-reachable" - both $H$ and $\overline{H}$ reachable from $K_{2021}$.

Key insight: $H$ reachable from $K_{2021}$ means $H$ can be built from $K_{2021}$ by adding vertices, where each new vertex is a "partial twin" of some existing vertex (or part of a batch of twins).

Let me think about the maximum. Can we make $n$ arbitrarily large?

Consider the following construction. Start with $K_{2021}$ on $C = \{c_0, \ldots, c_{2020}\}$. Add vertices $u_1, \ldots, u_{2020}$ as duplicates of $c_0$ (each non-adjacent to $c_0$ and to each other, adjacent to all of $C \setminus \{c_0\}$). Now we have 4041 vertices.

Now add $w_1$ as a duplicate of $u_1$: $w_1$ is non-adjacent to $u_1$, non-adjacent to $c_0$ (since $c_0 \notin N(u_1)$), non-adjacent to all other $u_j$ (since $u_j \notin N(u_1)$), and can be adjacent to any subset of $N(u_1) = C \setminus \{c_0\}$. Choose to connect $w_1$ to all of $C \setminus \{c_0\}$.

So $w_1$ has the same adjacency as $u_1$ (adjacent to all of $C \setminus \{c_0\}$, non-adjacent to $c_0$ and all $u_j$'s), except $w_1$ is also non-adjacent to $u_1$.

Now add $w_2$ as a duplicate of $u_1$: $w_2$ is non-adjacent to $u_1$, and can be adjacent to any subset of $N(u_1)$ at this time. $N(u_1)$ at this time is $C \setminus \{c_0\}$ (same as before, since $w_1$ is not adjacent to $u_1$). $w_2$ is non-adjacent to $c_0$, all $u_j$'s, and $w_1$ (since $w_1 \notin N(u_1)$). Choose to connect $w_2$ to all of $C \setminus \{c_0\}$.

So $w_2$ is non-adjacent to $c_0$, all $u_j$'s, $w_1$, and adjacent to all of $C \setminus \{c_0\}$.

We can keep adding $w_3, w_4, \ldots$ as duplicates of $u_1$, each non-adjacent to all previous $w_k$'s and $u_j$'s and $c_0$, adjacent to all of $C \setminus \{c_0\}$.

So in $H$, we have:
- $C = K_{2021}$ (clique).
- $U \cup W \cup \{c_0\}$ is an independent set (where $W = \{w_1, w_2, \ldots\}$).
- Each $u_j$ and $w_k$ is adjacent to all of $C \setminus \{c_0\}$.

Wait, actually $u_j$'s are adjacent to all of $C \setminus \{c_0\}$ and $w_k$'s are adjacent to all of $C \setminus \{c_0\}$. And $u_j$'s and $w_k$'s are all pairwise non-adjacent. And all are non-adjacent to $c_0$.

So $H$ has a clique $C$ of size 2021 and an independent set $\{c_0\} \cup U \cup W$ of size $1 + 2020 + |W| = 2021 + |W|$.

Now, is $\overline{H}$ reachable from $K_{2021}$?

$\overline{H}$: 
- $C$ is an independent set.
- $\{c_0\} \cup U \cup W$ is a clique (call it $Q$).
- $c_0$ is adjacent to all of $U \cup W$ (non-adjacent in $H$) and non-adjacent to $C \setminus \{c_0\}$ (adjacent in $H$).
- Each $u_j$ and $w_k$ is adjacent to all other elements of $Q$ and non-adjacent to all of $C \setminus \{c_0\}$ (since they're adjacent to all of $C \setminus \{c_0\}$ in $H$).

So $\overline{H}$: $Q$ is a clique of size $2021 + |W|$, $C \setminus \{c_0\}$ is an independent set of size 2020, and there are no edges between $Q$ and $C \setminus \{c_0\}$... wait, let me check. $u_j$ is adjacent to $c_i$ ($i \geq 1$) in $H$, so non-adjacent in $\overline{H}$. $c_0$ is adjacent to $c_i$ ($i \geq 1$) in $H$ (clique), so non-adjacent in $\overline{H}$. So indeed, no edges between $Q$ and $C \setminus \{c_0\}$ in $\overline{H}$.

So $\overline{H} = K_{2021+|W|} \cup \overline{K_{2020}}$ (disjoint union of a clique and independent set, with no edges between them).

For $\overline{H}$ to be reachable from $K_{2021}$: $\overline{H}$ must contain $K_{2021}$ as a subgraph. The clique $Q$ has size $2021 + |W| \geq 2021$. ✓

But is $\overline{H}$ actually reachable? $\overline{H} = K_{2021+|W|} \cup \overline{K_{2020}}$. We need to build this from $K_{2021}$.

Start with $K_{2021}$ on $Q_0 \subseteq Q$ (some 2021 vertices of $Q$). We need to add the remaining $|W|$ vertices of $Q$ and the 2020 vertices of $C \setminus \{c_0\}$.

The remaining $|W|$ vertices of $Q$ need to be adjacent to all of $Q_0$ and to each other (they're in the clique $Q$). Can we add a vertex to a clique as a duplicate of a clique vertex? If $v$ is in the clique and we duplicate $v$ (with $D = \{v\}$), the duplicate $v'$ is non-adjacent to $v$. But we need $v'$ to be adjacent to $v$ (since both are in $Q$, a clique). Contradiction!

So we can't add a vertex to a clique by duplicating a single clique vertex. What about duplicating a non-clique vertex?

If we duplicate a vertex $u$ in $C \setminus \{c_0\}$ (which is an independent set in $\overline{H}$, so $u$ has no neighbors): the duplicate $u'$ is non-adjacent to $u$ and can be adjacent to any subset of $N(u) = \emptyset$. So $u'$ is isolated. Not helpful for adding to the clique.

What about $|D| > 1$? If $D = \{q_1, q_2\}$ where $q_1, q_2 \in Q$ (clique), the duplicates $q_1', q_2'$ form an edge (since $q_1 q_2$ is an edge). $q_1'$ is non-adjacent to $q_1$ and $q_2$, and can be adjacent to any subset of $N(q_1) \setminus D = (Q \setminus \{q_1, q_2\}) \cup \emptyset$ (since $q_1$'s neighbors are $Q \setminus \{q_1\}$, and we remove $q_1, q_2$). So $q_1'$ can be adjacent to any subset of $Q \setminus \{q_1, q_2\}$.

But $q_1'$ is non-adjacent to $q_1$ and $q_2$. For $q_1'$ to be in the clique $Q$, it needs to be adjacent to all of $Q$, including $q_1$ and $q_2$. Contradiction.

So it seems impossible to add a vertex to a clique! Any duplicate is non-adjacent to its original, so it can't be in the same clique as its original.

But wait - we can add vertices to a clique if the clique is the original $K_{2021}$. The original 2021 vertices form a clique, and we can't add to it. But can we form a new, larger clique?

Actually, the duplicates of a clique $D$ form a clique $D'$ (same induced subgraph). And each $v_i' \in D'$ can be adjacent to any subset of $N(v_i) \setminus D$. If $v_i$ is adjacent to some vertex $w \notin D$, then $v_i'$ can be adjacent to $w$. So $D' \cup \{w\}$ could be a clique if all $v_i'$ are adjacent to $w$ and $w$ is adjacent to all $v_i'$ (which it is, since we choose to make $v_i'$ adjacent to $w$).

But $D' \cup D$ is NOT a clique because $v_i'$ is non-adjacent to $v_i$.

So we can grow a clique by duplicating all its members and having the duplicates connect to external vertices, but the new clique $D'$ doesn't include the originals $D$.

Hmm, so the maximum clique in a reachable graph is at most... let me think. The original $K_{2021}$ has clique number 2021. Can we create a larger clique?

If we duplicate all 2021 vertices ($D = V(K_{2021})$), the duplicates form $K_{2021}$ (same induced subgraph). Each duplicate $v_i'$ is non-adjacent to $v_i$ and can be adjacent to any subset of $N(v_i) \setminus D = \emptyset$ (since all vertices are in $D$). So the duplicates form an isolated $K_{2021}$ with no edges to the originals. The graph is $K_{2021} \cup K_{2021}$ (disjoint union of two cliques). Clique number is still 2021.

What if we duplicate a subset? $D \subset V(K_{2021})$, $|D| = d$. Duplicates form $K_d$. Each $v_i'$ can be adjacent to any subset of $V(K_{2021}) \setminus D$ (size $2021 - d$). If we connect all $v_i'$ to all of $V \setminus D$, then $D' \cup (V \setminus D)$ is a clique (since $D'$ is a clique, $V \setminus D$ is a clique, and all edges between them exist). This clique has size $d + (2021 - d) = 2021$. Still 2021.

Can we do better? In the next step, duplicate a subset of $D' \cup (V \setminus D)$... but the same argument applies. The new clique will have size at most 2021.

Wait, actually, let me reconsider. After the first step, we have $V$ (original $K_{2021}$) and $D'$ (clique of size $d$, connected to all of $V \setminus D$, non-adjacent to $D$). The clique $D' \cup (V \setminus D)$ has size 2021.

Now, in the second step, pick $D_2 \subseteq D' \cup (V \setminus D)$, say $|D_2| = d_2$. The duplicates $D_2'$ form a clique of size $d_2$. Each $v_i' \in D_2'$ (for $v_i \in D_2$) can be adjacent to any subset of $N(v_i) \setminus D_2$. Since $v_i \in D' \cup (V \setminus D)$ which is a clique of size 2021, $N(v_i) \supseteq (D' \cup (V \setminus D)) \setminus \{v_i\}$ (size 2020) plus possibly some vertices in $D$ (if $v_i \in V \setminus D$, then $v_i$ is adjacent to all of $V \setminus \{v_i\}$, which includes $D$; if $v_i \in D'$, then $v_i$ is adjacent to $V \setminus D$ but not to $D$).

Case 1: $v_i \in V \setminus D$. Then $N(v_i) = V \setminus \{v_i\} \cup D'$ (all original vertices except $v_i$, plus all duplicates). Actually, $v_i$ is adjacent to all other original vertices (since $V$ is a clique) and to all $v_j' \in D'$ (since we connected all duplicates to all of $V \setminus D$). So $N(v_i) = (V \setminus \{v_i\}) \cup D'$. Size: $2020 + d$.

$v_i' \in D_2'$ can be adjacent to any subset of $N(v_i) \setminus D_2$. If $D_2 \subseteq V \setminus D$, then $N(v_i) \setminus D_2 = (V \setminus \{v_i\} \setminus D_2) \cup D'$. The new clique $D_2' \cup (N(v_i) \setminus D_2)$... hmm, this isn't quite right because the clique includes $D_2'$ and the vertices they're all connected to.

Let me think about it differently. The maximum clique reachable from $K_n$ is $n$. Here's why:

Claim: The clique number of any graph reachable from $K_n$ is exactly $n$ (well, at least $n$ since we start with $K_n$, and at most $n$).

Proof that clique number $\leq n$: Consider any reachable graph $G$. We need to show $\omega(G) \leq n = 2021$.

Hmm, actually I'm not sure this is true. Let me think of a potential counterexample.

From $K_3$ (vertices $a, b, c$): duplicate $D = \{a\}$, get $a'$, connect $a'$ to $b$ and $c$. Now the graph has $K_3$ on $\{a, b, c\}$ and $a'$ adjacent to $b, c$ but not $a$. Clique $\{a', b, c\}$ has size 3. Still 3.

Now duplicate $D_2 = \{a'\}$, get $a''$, connect $a''$ to $b$ and $c$ (neighbors of $a'$). $a''$ is non-adjacent to $a'$ and can be adjacent to $b, c$. Clique $\{a'', b, c\}$ has size 3.

What if we duplicate $D_2 = \{b\}$? Get $b'$, non-adjacent to $b$, can be adjacent to $N(b) \setminus \{b\} = \{a, c, a'\}$. Connect $b'$ to $a, c, a'$. Now $b'$ is adjacent to $a, c, a'$. Is $\{a, c, a', b'\}$ a clique? $a$-$c$: yes. $a$-$a'$: no! $a'$ is non-adjacent to $a$. So not a clique.

$\{c, a', b'\}$: $c$-$a'$: yes. $c$-$b'$: yes. $a'$-$b'$: yes (both in $D_2'$... no, $a' \notin D_2'$. $b' \in D_2'$. $a'$ and $b'$: is there an edge? $b'$ was connected to $a'$ (we chose to connect $b'$ to $a'$). So yes. So $\{c, a', b'\}$ is a clique of size 3.

Can we get a clique of size 4 from $K_3$? Let me try harder.

After step 1: $a, b, c$ form $K_3$. $a'$ adjacent to $b, c$, non-adjacent to $a$.

Step 2: $D_2 = \{a, a'\}$. $a$ and $a'$: non-adjacent. So duplicates $a^*$ and $a'^*$ are non-adjacent to each other. $a^*$ non-adjacent to $a, a'$, can be adjacent to $N(a) \setminus \{a, a'\} = \{b, c\}$. $a'^*$ non-adjacent to $a, a'$, can be adjacent to $N(a') \setminus \{a, a'\} = \{b, c\}$.

So $a^*$ and $a'^*$ are both adjacent to $b, c$ (if we choose), but non-adjacent to each other. Clique $\{a^*, b, c\}$ or $\{a'^*, b, c\}$, size 3.

It really seems like the clique number stays at $n$. Let me try to prove this.

Claim: If $G$ is reachable from $K_n$, then $\omega(G) \leq n$.

Proof attempt: Consider the "origin" of each vertex. The original $n$ vertices are "generation 0". Vertices created in the $k$-th augmentation are "generation $k$". 

When a vertex $v'$ is created as a duplicate of $v$ (in a batch $D$), $v'$ is non-adjacent to all vertices in $D$. In particular, $v'$ is non-adjacent to its "parent" $v$.

Consider a maximum clique $Q$ in $G$. For each vertex in $Q$, consider its generation. Can two vertices of the same generation be in $Q$? If $v_i'$ and $v_j'$ are created in the same batch (duplicates of $v_i$ and $v_j$), they're adjacent iff $v_i v_j$ is an edge. So they can be in a clique together.

Hmm, the generation idea doesn't directly work. Let me think differently.

Alternative approach: Consider a "coloring" or "labeling" of vertices.

Actually, let me think about it in terms of a potential function. Define for each vertex $v$ a set $S(v) \subseteq V(K_n)$ (the original vertices). For original vertices, $S(v_i) = \{v_i\}$. When $v'$ is created as a duplicate of $v$ in a batch $D$, $S(v') = S(v) \setminus S(D)$... no, this doesn't seem right.

Let me try another approach. Let me think about the "non-adjacency" graph (complement) and its chromatic number.

$\omega(G) \leq n$ iff $\chi(\overline{G}) \leq n$ (since $\omega(G) = \chi(\overline{G})$... no, that's not right either. $\omega(G)$ is the clique number of $G$, which equals the independence number $\alpha(\overline{G})$... no. $\omega(G)$ = size of largest clique in $G$ = size of largest independent set in $\overline{G}$ = $\alpha(\overline{G})$. And $\alpha(\overline{G}) \leq \chi(\overline{G})$... this doesn't directly help.

Let me try to directly prove $\omega(G) \leq n$ for reachable $G$.

Induction on the number of augmentations. Base case: $G = K_n$, $\omega = n$. ✓

Inductive step: $G$ is obtained from $G'$ by an augmentation with set $D$. $G$ adds vertices $D' = \{v' : v \in D\}$. We need to show $\omega(G) \leq n$ given $\omega(G') \leq n$.

A clique in $G$ either:
(a) Doesn't include any vertex from $D'$: then it's a clique in $G'$, so size $\leq n$.
(b) Includes some vertices from $D'$.

For (b), let $Q$ be a clique in $G$ including vertices $Q \cap D' = \{v_{i_1}', \ldots, v_{i_k}'\}$ and $Q \setminus D' = R$ (vertices in $G'$).

The vertices $v_{i_1}', \ldots, v_{i_k}'$ form a clique, so $\{v_{i_1}, \ldots, v_{i_k}\}$ form a clique in $G'$ (since duplicates copy the induced subgraph).

Each $v_{i_j}'$ is non-adjacent to all of $D$. So $R \cap D = \emptyset$ (since $R$ is adjacent to all of $Q \cap D'$, but vertices in $D$ are non-adjacent to all of $D'$).

Each $v_{i_j}'$ is adjacent to $r \in R$ only if $v_{i_j}$ is adjacent to $r$ in $G'$ (and $r \notin D$). So for all $r \in R$, $r$ is adjacent to all of $\{v_{i_1}, \ldots, v_{i_k}\}$ in $G'$.

So $\{v_{i_1}, \ldots, v_{i_k}\} \cup R$ is a clique in $G'$ (since $\{v_{i_1}, \ldots, v_{i_k}\}$ is a clique, $R$ is a clique (as a subset of clique $Q$), and every $v_{i_j}$ is adjacent to every $r \in R$).

Therefore $|\{v_{i_1}, \ldots, v_{i_k}\} \cup R| = k + |R| = |Q| \leq \omega(G') \leq n$.

So $\omega(G) \leq n$. ✓

So the clique number of any graph reachable from $K_n$ is at most $n$.

Now, applying this to our problem:
- $H$ reachable from $K_{2021}$: $\omega(H) \leq 2021$.
- $\overline{H}$ reachable from $K_{2021}$: $\omega(\overline{H}) \leq 2021$, i.e., $\alpha(H) \leq 2021$.

So $H$ has $\omega(H) \leq 2021$ and $\alpha(H) \leq 2021$.

By Ramsey theory, $R(2022, 2022) > n$ is needed for such $H$ to exist. But we also need reachability, not just existence.

But the question is about the maximum $n$. We have $\omega(H) \leq 2021$ and $\alpha(H) \leq 2021$. By Ramsey, $R(2022, 2022)$ is the smallest $n$ such that every graph on $n$ vertices has $\omega \geq 2022$ or $\alpha \geq 2022$. So for $n < R(2022, 2022)$, there exist graphs with $\omega \leq 2021$ and $\alpha \leq 2021$.

But we need more: both $H$ and $\overline{H}$ must be reachable. The reachability condition is stronger than just $\omega, \alpha \leq 2021$.

Hmm, but the problem asks for a specific numerical answer, so maybe the maximum is also related to 2021 in a clean way.

Let me think about what other constraints reachability imposes.

We showed $\omega(G) \leq n$ for $G$ reachable from $K_n$. Similarly, the original $n$ vertices always form a clique, so $\omega(G) \geq n$. Thus $\omega(G) = n$ for all $G$ reachable from $K_n$.

Wait, that's not right. $\omega(G) \geq n$ because the original $n$ vertices form a clique. And $\omega(G) \leq n$ by our proof. So $\omega(G) = n$ exactly.

So for $H$ reachable from $K_{2021}$: $\omega(H) = 2021$.
For $\overline{H}$ reachable from $K_{2021}$: $\omega(\overline{H}) = 2021$, so $\alpha(H) = 2021$.

So $H$ has $\omega(H) = 2021$ and $\alpha(H) = 2021$.

Now, by Ramsey theory, $R(2022, 2022)$ is the threshold. For $n \geq R(2022, 2022)$, every graph on $n$ vertices has $\omega \geq 2022$ or $\alpha \geq 2022$. So we need $n < R(2022, 2022)$.

But $R(2022, 2022)$ is a huge number, and the problem expects a clean answer. So maybe the reachability condition is more restrictive than just $\omega = \alpha = 2021$.

Let me think about what other structural properties reachable graphs have.

We showed that for any clique $Q$ in a reachable graph, we can "project" it back to a clique in the previous graph, and ultimately to a clique in $K_n$. This projection maps each duplicate $v'$ to its original $v$. So every clique in $G$ corresponds to a clique of the same size in $K_n$, which has size at most $n$.

More specifically, define a "projection" $\pi$: for original vertices, $\pi(v) = v$. For a duplicate $v'$ created in some augmentation, $\pi(v') = \pi(v)$ where $v$ is the original it duplicated. Then $\pi$ maps every vertex to an original vertex in $K_n$.

The key property: if $v'$ and $w'$ are adjacent in $G$, then $\pi(v')$ and $\pi(w')$ are adjacent in $K_n$ (i.e., $\pi(v') \neq \pi(w')$). Wait, is this true?

Let me check. If $v'$ and $w'$ are both created in the same batch (duplicates of $v$ and $w$), they're adjacent iff $v$ and $w$ are adjacent in the current graph. If $v \neq w$ and they're adjacent, then $\pi(v') = \pi(v) \neq \pi(w) = \pi(w')$ (assuming $\pi$ is injective on the current graph... which it might not be).

Hmm, actually $\pi$ might not be injective. If $v$ was itself a duplicate of some $u$, and $w$ was also a duplicate of $u$ (in a different batch), then $\pi(v) = \pi(w) = u$. And if $v$ and $w$ are adjacent, then $\pi(v) = \pi(w) = u$, so the projection maps an edge to a self-loop, which is not an edge in $K_n$.

So the projection argument doesn't directly work for proving $\omega \leq n$. But we already proved $\omega \leq n$ by induction, so that's fine.

Let me think about other properties. 

Actually, let me think about the structure more carefully. The projection $\pi$ maps each vertex to an original vertex. For a clique $Q$ in $G$, the projection $\pi(Q)$ is a subset of $V(K_n)$. We showed $|Q| \leq n$, but can we say more?

In the inductive proof, we showed that for a clique $Q$ in $G$ (obtained from $G'$ by augmentation with $D$), the "projected" clique $\{v_{i_1}, \ldots, v_{i_k}\} \cup R$ in $G'$ has the same size. By induction, this maps back to a clique of size $|Q|$ in $K_n$.

So every clique in $G$ projects to a clique of the same size in $K_n$, which means $|Q| \leq n$ and the projection is injective on $Q$ (since a clique in $K_n$ has distinct vertices).

So $\pi$ is injective on every clique. Similarly, $\pi$ is injective on every independent set? Let me check.

For independent sets: if $v'$ and $w'$ are non-adjacent in $G$, does $\pi(v') \neq \pi(w')$? Not necessarily. $v'$ and $w'$ could both be duplicates of the same vertex $u$ (in different batches) and non-adjacent to each other.

So the projection is injective on cliques but not necessarily on independent sets.

Now, for our problem: $H$ has $\omega(H) = 2021$ and $\alpha(H) = 2021$. The projection $\pi_H$ (from $H$'s reachability) maps every clique injectively to $V(K_{2021})$, so every clique has size $\leq 2021$. Similarly, the projection $\pi_{\overline{H}}$ (from $\overline{H}$'s reachability) maps every independent set of $H$ (clique of $\overline{H}$) injectively to $V(K_{2021})$, so every independent set has size $\leq 2021$.

Now, can we have $n > 4041$? We need a graph on $n$ vertices with $\omega = \alpha = 2021$ that is reachable (along with its complement) from $K_{2021}$.

Let me think about whether the reachability condition allows $n > 4041$.

Going back to my earlier construction: I had $H$ with $C = K_{2021}$, $U = \{u_1, \ldots, u_{2020}\}$ (independent set, each adjacent to all of $C \setminus \{c_0\}$), and $W = \{w_1, w_2, \ldots\}$ (each a duplicate of $u_1$, non-adjacent to $c_0$, all $u_j$'s, all other $w_k$'s, adjacent to all of $C \setminus \{c_0\}$).

In this $H$:
- $\omega(H) = 2021$ (the clique $C$). Can we find a larger clique? Any clique can include at most one vertex from $\{c_0\} \cup U \cup W$ (since they're pairwise non-adjacent) and at most 2020 vertices from $C \setminus \{c_0\}$... wait, a vertex from $U \cup W$ is adjacent to all of $C \setminus \{c_0\}$ but not to $c_0$. So a clique could be $\{u_j\} \cup (C \setminus \{c_0\})$ of size $1 + 2020 = 2021$. Or $C$ itself of size 2021. So $\omega(H) = 2021$. ✓

- $\alpha(H) = 1 + 2020 + |W| = 2021 + |W|$. But we need $\alpha(H) = 2021$ (since $\overline{H}$ must be reachable from $K_{2021}$, giving $\omega(\overline{H}) = 2021$, i.e., $\alpha(H) = 2021$). So $2021 + |W| \leq 2021$, meaning $|W| = 0$!

So we can't add any $w$ vertices! The independent set is already at size 2021 with just $\{c_0\} \cup U$, and adding any more vertices to the independent set would make $\alpha(H) > 2021$, violating the constraint.

But wait, maybe we can add vertices that are NOT in the independent set. Let me think about adding vertices that are adjacent to some of $U$.

Let me try a different construction. Start with $K_{2021}$ on $C$. Add $U = \{u_1, \ldots, u_{2020}\}$ as before (duplicates of $c_0$, each adjacent to all of $C \setminus \{c_0\}$, pairwise non-adjacent, non-adjacent to $c_0$). Now $I = \{c_0\} \cup U$ is an independent set of size 2021.

Now add a vertex $w$ as a duplicate of $c_1$ (where $c_1 \in C \setminus \{c_0\}$). $w$ is non-adjacent to $c_1$, and can be adjacent to any subset of $N(c_1) \setminus \{c_1\}$. In the current graph, $N(c_1) = (C \setminus \{c_1\}) \cup U$ (since $c_1$ is adjacent to all other original vertices and to all $u_j$'s). So $w$ can be adjacent to any subset of $(C \setminus \{c_1\}) \cup U$, and is non-adjacent to $c_1$.

Let's choose $w$ to be adjacent to all of $(C \setminus \{c_0, c_1\}) \cup U$ and non-adjacent to $c_0$ (we can choose this since $c_0 \in N(c_1) \setminus \{c_1\}$, so we can choose not to connect). Wait, $c_0 \in C \setminus \{c_1\}$, and $c_0 \in N(c_1)$ (since $C$ is a clique). So $c_0 \in N(c_1) \setminus \{c_1\}$, and we can choose whether $w$ is adjacent to $c_0$.

Let's say $w$ is adjacent to $c_0$ and all of $U$, and non-adjacent to $C \setminus \{c_0, c_1\}$... no, let me think about what we need.

We need $\alpha(H) \leq 2021$ and $\omega(H) \leq 2021$.

Currently (before adding $w$), $\alpha(H) = 2021$ (the set $I = \{c_0\} \cup U$) and $\omega(H) = 2021$ (the set $C$).

After adding $w$: 
- $\omega(H)$: any clique containing $w$. $w$ is non-adjacent to $c_1$. So a clique containing $w$ can include at most $C \setminus \{c_1\}$ (size 2020) plus $w$, giving 2021. Or $w$ plus some subset of $U$ (but $U$ is an independent set, so at most one from $U$). So $\omega(H) \leq 2021$. ✓ (as long as $w$ is not adjacent to too many things)

- $\alpha(H)$: any independent set containing $w$. $w$ is non-adjacent to $c_1$ and to whichever vertices we chose not to connect. If $w$ is adjacent to all of $U$, then $w$ can't be in an independent set with any $u_j$. If $w$ is adjacent to $c_0$, then $w$ can't be in an independent set with $c_0$. So the independent set containing $w$ would be $\{w, c_1\} \cup$ (some non-neighbors of $w$ among $C \setminus \{c_0, c_1\}$). 

If $w$ is adjacent to all of $C \setminus \{c_1\}$ and all of $U$, then $w$'s only non-neighbor (among existing vertices) is $c_1$. So the max independent set containing $w$ is $\{w, c_1\}$, size 2. And the max independent set not containing $w$ is still $I = \{c_0\} \cup U$, size 2021. So $\alpha(H) = 2021$. ✓

So with $w$ adjacent to all of $C \setminus \{c_1\}$ and all of $U$, and non-adjacent to $c_1$: $\omega(H) = 2021$ and $\alpha(H) = 2021$. $n = 4042$.

But is $\overline{H}$ reachable from $K_{2021}$?

$\overline{H}$: Let me figure out the structure.
- $C$ is an independent set (was clique in $H$).
- $U$ is a clique (was independent set in $H$).
- $c_0$ is adjacent to all of $U$ (was non-adjacent in $H$) and non-adjacent to $C \setminus \{c_0\}$ (was adjacent in $H$).
- $c_i$ ($i \geq 1$) is adjacent to $u_j$ iff $c_i$ was non-adjacent to $u_j$ in $H$. In $H$, all $c_i$ ($i \geq 1$) are adjacent to all $u_j$. So in $\overline{H}$, no $c_i$ ($i \geq 1$) is adjacent to any $u_j$.
- $w$ in $\overline{H}$: $w$ is adjacent to $c_1$ (non-adjacent in $H$), non-adjacent to $C \setminus \{c_1\}$ (adjacent in $H$), non-adjacent to all $u_j$ (adjacent in $H$).

So in $\overline{H}$:
- $U \cup \{c_0\}$ is a clique of size 2021. ✓ ($\omega(\overline{H}) \geq 2021$)
- $C \setminus \{c_0\}$ is an independent set of size 2020.
- $w$ is adjacent only to $c_1$ (among all other vertices). So $w$ is almost isolated.
- No edges between $U$ and $C \setminus \{c_0\}$.
- $c_0$ is adjacent to all of $U$, non-adjacent to $C \setminus \{c_0\}$ and non-adjacent to $w$.

Is $\overline{H}$ reachable from $K_{2021}$? We need $\omega(\overline{H}) = 2021$ (which we have, the clique $U \cup \{c_0\}$) and we need to build it from $K_{2021}$.

Start with $K_{2021}$ on $U \cup \{c_0\}$. We need to add $C \setminus \{c_0\} = \{c_1, \ldots, c_{2020}\}$ (independent set, non-adjacent to $c_0$ and to $U$) and $w$ (adjacent only to $c_1$).

Adding $c_1, \ldots, c_{2020}$: these form an independent set, non-adjacent to $c_0$ and to $U$. We can add them as duplicates of $c_0$ (as before): each $c_i$ is non-adjacent to $c_0$ and to all previously added $c_j$'s, and can be adjacent to any subset of $U$ (neighbors of $c_0$). We choose to connect each $c_i$ to no vertices in $U$ (since in $\overline{H}$, $c_i$ is non-adjacent to all $u_j$). ✓

Now we need to add $w$, which is adjacent only to $c_1$ (and non-adjacent to everything else). 

$w$ is non-adjacent to $c_0$, all $u_j$, and all $c_j$ ($j \geq 2$). $w$ is adjacent to $c_1$.

Can we add $w$ as a duplicate of some vertex? $w$ is adjacent to $c_1$, so $w$'s parent must have $c_1$ as a neighbor. $c_1$'s neighbors in the current graph: $c_1$ is non-adjacent to $c_0$, all $u_j$, and all $c_j$ ($j \geq 2$). So $c_1$ has NO neighbors. So $c_1$ can't be the parent (since $w$ needs to be adjacent to $c_1$, but $c_1$'s duplicates can only be adjacent to $c_1$'s neighbors, which is empty).

What about $c_0$? $c_0$'s neighbors are $U$ (all $u_j$'s). If $w$ is a duplicate of $c_0$, $w$ is non-adjacent to $c_0$ and can be adjacent to any subset of $U$. But $w$ needs to be adjacent to $c_1$, and $c_1 \notin N(c_0)$ (in the current graph, $c_1$ is non-adjacent to $c_0$). So $w$ can't be adjacent to $c_1$. ✗

What about $u_j$? $u_j$'s neighbors are $U \setminus \{u_j\}$ and $c_0$. If $w$ is a duplicate of $u_j$, $w$ is non-adjacent to $u_j$ and can be adjacent to any subset of $(U \setminus \{u_j\}) \cup \{c_0\}$. But $w$ needs to be adjacent to $c_1$, and $c_1 \notin N(u_j)$. ✗

What about $c_j$ for $j \geq 2$? $c_j$ has no neighbors (like $c_1$). ✗

So $w$ cannot be added as a single-vertex duplicate! What about multi-vertex $D$?

If $D = \{c_0, c_1\}$: $c_0$ and $c_1$ are non-adjacent in the current graph. So duplicates $c_0'$ and $c_1'$ are non-adjacent. $c_0'$ is non-adjacent to $c_0, c_1$, can be adjacent to $N(c_0) \setminus D = U$. $c_1'$ is non-adjacent to $c_0, c_1$, can be adjacent to $N(c_1) \setminus D = \emptyset$. So $c_1'$ is isolated (non-adjacent to everything). Not what we        — AI历史解题过程（thinking）
#   polymath_05789         — 题目ID

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
  <problem_id>polymath_05789</problem_id>
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

An augmentation on a graph \( G \) is defined as doing the following:

- Take some set \( D \) of vertices in \( G \), and duplicate each vertex \( v_{i} \in D \) to create a new vertex \( v_{i}^{\prime} \).
- If there's an edge between a pair of vertices \( v_{i}, v_{j} \in D \), create an edge between vertices \( v_{i}^{\prime} \) and \( v_{j}^{\prime} \). If there's an edge between a pair of vertices \( v_{i} \in D, v_{j} \notin D \), you can choose to create an edge between \( v_{i}^{\prime} \) and \( v_{j} \) but do not have to.

A graph is called reachable from \( G \) if it can be created through some sequence of augmentations on \( G \). Some graph \( H \) has \( n \) vertices and satisfies that both \( H \) and the complement of \( H \) are reachable from a complete graph of 2021 vertices. If the maximum and minimum values of \( n \) are \( M \) and \( m \), find \( M+m \).

## Standard Solution

The maximum is \( 2021^{2} \), and the minimum is \( 2021 + 2020 \).

Notice that the chromatic number of any graph reachable from \( G \) is the same as the chromatic number of \( G \). To show this, let the chromatic number of \( G \) be \( a \), and the chromatic number of some graph \( G^{\prime} \) that is reached by performing an augmentation on \( G \) be \( a^{\prime} \). If every vertex \( v_{i}^{\prime} \) in the augmentation is colored the same color as \( v_{i} \), this creates a valid coloring of \( G^{\prime} \) with \( a \) colors, so \( a \geq a^{\prime} \). Additionally, since \( G \) is a subgraph of \( G^{\prime} \), we have \( a^{\prime} \geq a \), so \( a = a^{\prime} \).

This means \( H \) and the complement of \( H \) have chromatic number 2021. For some coloring of \( H \), consider sets \( S_{1}, S_{2}, \ldots, S_{2021} \) of nodes of \( H \) such that \( S_{i} \) contains nodes of the same color. All nodes in \( S_{i} \) are nonadjacent, so in the complement of \( H \), the nodes in \( S_{i} \) will form a \( K_{\left|S_{i}\right|} \). Since the chromatic number of the complement of \( H \) is 2021, we have \(\left|S_{i}\right| \leq 2021\) for all \( i \), so \( M \leq 2021^{2} \). This is achieved when \( H \) is 2021 copies of a \( K_{2021} \), as \( H \) can be achieved by choosing the original \( K_{2021} \) in \( G \) and duplicating it for 2020 augmentations, where no additional edges are added.

Additionally, we can achieve the complement of \( H \) first by coloring \( G \) using 2021 colors. Whenever we duplicate a node \( v_{i} \) to create \( v_{i}^{\prime} \), we color \( v_{i}^{\prime} \) the same color as \( v_{i} \). Then if we duplicate the original \( K_{2021} \) in \( G \) for 2020 augmentations and add edges between each newly created node and each node of a different color, we will create the complement of \( H \). This gives \( M = 2021^{2} \).

Note that since the complement of \( H \) must contain a \( K_{2021} \), there must be a set of 2021 nodes in \( H \) where no two are adjacent. \( H \) also contains a \( K_{2021} \), and since we can have at most one node of the \( K_{2021} \) in the independent set, we will require an additional 2020 nodes, giving \( m \geq 4041 \). If \( H \) is the graph consisting of a \( K_{2021} \) and 2020 isolated nodes, \( H \) can be achieved by duplicating a single node 2020 times and choosing to add no additional edges. Additionally, the complement of \( H \) can be achieved by duplicating the same node of \( G \) 2020 times and each time adding edges from the duplicated node to every other node in the original \( K_{2021} \). This gives \( m = 4041 \).

We have \( M + m = 4041 + 2021^{2} = 4088482 \).

\(\boxed{4088482}\)

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a complete graph on 2021 vertices, $K_{2021}$. An augmentation operation:
- Pick a set $D$ of vertices, duplicate each $v_i \in D$ to create $v_i'$.
- If there's an edge between $v_i, v_j \in D$, create edge between $v_i', v_j'$.
- If there's an edge between $v_i \in D, v_j \notin D$, we may choose to create edge between $v_i'$ and $v_j$.

A graph is reachable from $G$ if it can be created through some sequence of augmentations on $G$.

We need to find graphs $H$ with $n$ vertices such that both $H$ and $\overline{H}$ (complement of $H$) are reachable from $K_{2021}$. Find max and min $n$, then $M + m$.

Let me think about what graphs are reachable from $K_{2021}$.

Starting from $K_{2021}$ (complete graph on 2021 vertices).

When we do an augmentation on $K_{2021}$: pick $D$, duplicate each vertex in $D$. Since $K_{2021}$ is complete, every pair of vertices in $D$ has an edge, so we create all edges among the duplicates $v_i'$. Also, for each $v_i \in D$ and $v_j \notin D$, there's an edge, so we may choose to create edges between $v_i'$ and $v_j$.

So after one augmentation, the new vertices $v_i'$ form a clique (since all pairs in $D$ are connected). Each new vertex $v_i'$ is connected to some subset of the original vertices not in $D$ (we choose which edges to add). Also, $v_i'$ is not connected to $v_i$ (the original it duplicated) — wait, actually $v_i \in D$, and the rule says edges between $v_i' \in D'$ and $v_j \notin D$. $v_i$ is in $D$, so $v_i$ is not in the "$v_j \notin D$" category. So $v_i'$ is never connected to $v_i$ directly through this rule. Actually, $v_i'$ has no edge to $v_i$ at all (there's no rule creating such an edge).

Wait, let me re-read. The original edges are preserved. The new vertex $v_i'$ is a duplicate. The rules only create edges involving $v_i'$. Edges between $v_i'$ and $v_j$ where $v_j \notin D$ are optional. Edges between $v_i'$ and $v_j'$ where $v_j \in D$ are created if $v_i, v_j$ had an edge. There's no rule for edge between $v_i'$ and $v_i$ (since $v_i \in D$, so $v_i$ is not in the "$\notin D$" set). So $v_i'$ and $v_i$ are never connected.

So in the augmented graph, the duplicates form a clique among themselves, and each duplicate $v_i'$ can be connected to any subset of vertices outside $D$ (but not to any vertex in $D$, including its original $v_i$).

Let me think about what structures are reachable. This is related to "clique-width" or some graph generation notion. Let me think more carefully.

Actually, let me think about this differently. Let me consider what graphs can be built.

Key observation: The operation preserves the property that we can think of the graph as being built up by adding cliques of new vertices, where each new vertex can connect to any subset of "old" vertices that are not its "parent" or in its "generation's $D$".

Hmm, this is getting complex. Let me think about reachability from $K_{2021}$ more carefully.

Let me think about small cases first. What graphs are reachable from $K_n$?

From $K_n$, one augmentation with $D$ of size $k$: we add $k$ new vertices forming a clique. Each new vertex $v_i'$ connects to any subset of the $n - k$ vertices not in $D$. So the new vertices form a clique, and each has edges to a chosen subset of the $n-k$ "untouched" original vertices. The new vertices have no edges to the $k$ original vertices in $D$.

Actually wait - in subsequent augmentations, the "graph" is the current graph, not $K_n$. So the edges among existing vertices are whatever they are. Let me re-read.

"An augmentation on a graph $G$..." - so it's on the current graph. The edges in the current graph determine what edges get created.

So if we do a sequence of augmentations, each step operates on the current graph.

Let me think about what's preserved. 

Let me think about the complement. If $H$ is reachable from $K_{2021}$, what can we say about $\overline{H}$?

Note: $K_{2021}$ has complement $\overline{K_{2021}}$ = empty graph on 2021 vertices. But we need $\overline{H}$ to also be reachable from $K_{2021}$, not from $\overline{K_{2021}}$.

Let me think about what graphs are reachable from $K_n$.

Claim: A graph is reachable from $K_n$ iff it can be obtained by starting with $K_n$ and repeatedly adding a clique of new vertices, where each new vertex is adjacent to an arbitrary subset of existing vertices that are NOT in the current $D$.

Hmm, but in later steps, the graph is no longer complete, so the "if there's an edge between $v_i, v_j \in D$, create edge $v_i', v_j'$" rule means the duplicates only form a clique if $D$ is a clique in the current graph.

This is important! In later augmentations, $D$ might not be a clique, so the duplicates don't necessarily form a clique.

Let me reconsider. The duplicates $v_i'$ for $v_i \in D$ form a graph isomorphic to $G[D]$ (the induced subgraph on $D$). And each $v_i'$ can optionally connect to any $v_j \notin D$ that is adjacent to $v_i$ in the current graph.

Wait, re-reading: "If there's an edge between a pair of vertices $v_i \in D, v_j \notin D$, you can choose to create an edge between $v_i'$ and $v_j$."

So $v_i'$ can connect to $v_j \notin D$ only if $v_i$ is adjacent to $v_j$ in the current graph. So the optional edges from $v_i'$ go to a subset of $N(v_i) \setminus D$ (neighbors of $v_i$ not in $D$).

And the mandatory edges: $v_i' v_j'$ is created iff $v_i v_j$ is an edge and both in $D$.

So the new vertex $v_i'$ "inherits" the adjacency structure of $v_i$ within $D$ (mandatory), and can optionally connect to any subset of $v_i$'s neighbors outside $D$.

This is like a "twin" operation but more general. $v_i'$ is a "partial twin" of $v_i$ - it copies $v_i$'s adjacencies within $D$ and optionally copies some adjacencies outside $D$.

Let me think about this in terms of what graphs are reachable.

Let me think about the problem from the perspective of: what is the maximum and minimum number of vertices $n$ such that there exists a graph $H$ on $n$ vertices with both $H$ and $\overline{H}$ reachable from $K_{2021}$?

First, let's think about what graphs are reachable from $K_{2021}$.

Observation 1: $K_{2021}$ itself is reachable (0 augmentations). So $n = 2021$ works if $\overline{K_{2021}}$ (empty graph on 2021 vertices) is also reachable. Is the empty graph reachable from $K_{2021}$? Starting from $K_{2021}$, can we reach the empty graph? We can only add vertices and edges, never remove them. So we can never remove the original edges of $K_{2021}$. The empty graph on 2021 vertices is NOT reachable because the original 2021 vertices always form a clique.

Wait, but we can add more vertices. The question is about $H$ having $n$ vertices. $H$ doesn't have to be on exactly the original 2021 vertices. We can add vertices through augmentations.

So reachable graphs from $K_{2021}$ always contain $K_{2021}$ as a subgraph (the original 2021 vertices always form a clique, and we never remove edges). We can only add vertices and edges.

So if $H$ is reachable from $K_{2021}$, then $H$ contains a $K_{2021}$ subgraph. Similarly, $\overline{H}$ is reachable from $K_{2021}$, so $\overline{H}$ contains a $K_{2021}$ subgraph, meaning $H$ contains an independent set of size 2021.

So $H$ must contain both a clique of size 2021 and an independent set of size 2021.

Now, the minimum $n$: we need $H$ on $n$ vertices with a clique of size 2021 and an independent set of size 2021. The minimum $n$ for a graph with both a clique and independent set of size $k$ is... well, if the clique and independent set are disjoint, $n \geq 2 \cdot 2021 = 4042$. If they overlap, can they? A clique of size 2021 and an independent set of size 2021 can share at most 1 vertex (since any two vertices in the clique are adjacent, but any two in the independent set are non-adjacent, so the intersection has at most 1 vertex). So $n \geq 2021 + 2021 - 1 = 4041$.

But can we achieve $n = 4041$? That would require the clique and independent set to share exactly 1 vertex. Let's think: we need $H$ reachable from $K_{2021}$ (so $H$ contains $K_{2021}$) and $\overline{H}$ reachable from $K_{2021}$ (so $\overline{H}$ contains $K_{2021}$, i.e., $H$ contains an independent set of size 2021).

But we also need $H$ to actually be reachable, not just contain these structures. Let me think about whether $n = 4041$ is achievable.

Actually, let me think more carefully about what graphs are reachable.

Let me consider: from $K_{2021}$, can we add a single vertex that is an isolated vertex (no edges to anything)? 

In one augmentation, pick $D = \{v\}$ for some vertex $v$. Create $v'$. The mandatory edges: none (since $|D| = 1$, no pairs in $D$). The optional edges: $v'$ can connect to any subset of $N(v) \setminus D = $ all other 2020 vertices (since $K_{2021}$ is complete). So we can choose to connect $v'$ to none of them, making $v'$ isolated. But $v'$ is also not connected to $v$ (since $v \in D$). So yes, $v'$ is an isolated vertex!

So from $K_{2021}$, one augmentation with $D = \{v\}$ and choosing no optional edges gives us $K_{2021}$ plus an isolated vertex. This graph has 2022 vertices.

Can we add more isolated vertices? In the next augmentation, the graph is $K_{2021}$ + isolated vertex $v'$. If we pick $D = \{w\}$ for some $w$ in the $K_{2021}$ part, then $w'$ can optionally connect to any subset of $N(w) \setminus \{w\}$. $N(w)$ includes all other 2020 vertices of the $K_{2021}$ part but NOT $v'$ (since $v'$ is isolated, $w$ is not adjacent to $v'$). So $w'$ can connect to any subset of the other 2020 clique vertices. Choosing none, $w'$ is isolated (not connected to $w$, not connected to any clique vertex, and not connected to $v'$ since $v' \notin N(w)$). 

So we can keep adding isolated vertices one at a time, each time picking $D$ to be a single vertex from the original clique and choosing no optional edges.

Alternatively, we can add many isolated vertices at once: pick $D$ to be a set of $k$ vertices from the clique. The duplicates form a clique (since $D$ is a clique in $K_{2021}$). Wait, that's bad - we want isolated vertices, but the duplicates form a clique among themselves.

So to add $k$ isolated vertices at once, we'd pick $D$ of size $k$, but then the $k$ duplicates form a $K_k$. That's not what we want.

To add isolated vertices, we need to add them one at a time (each time $|D| = 1$). Or... we could add them in a way where the duplicates form a clique, and then in a later step... no, we can't remove edges.

So to get $k$ isolated vertices, we need $k$ augmentations, each adding one isolated vertex. That gives us $K_{2021} \cup \overline{K_k}$ (disjoint union of $K_{2021}$ and $k$ isolated vertices) with $2021 + k$ vertices.

Now, is $K_{2021} \cup \overline{K_k}$ reachable from $K_{2021}$? Yes, by the above argument, adding $k$ isolated vertices one at a time.

Is $\overline{K_{2021} \cup \overline{K_k}}$ reachable from $K_{2021}$?

$\overline{K_{2021} \cup \overline{K_k}} = \overline{K_k} \cup K_{2021}$... wait let me compute. The complement of $K_{2021} \cup \overline{K_k}$ (where the $K_{2021}$ and $\overline{K_k}$ are on disjoint vertex sets with no edges between them): the complement has no edges within the $K_{2021}$ part (becomes independent set), all edges within the $\overline{K_k}$ part (becomes $K_k$), and all edges between the two parts. So $\overline{H} = K_k \vee \overline{K_{2021}}$ (join of $K_k$ and independent set of size 2021), which is $K_{k+2021}$ minus the edges within the 2021 part... no.

Let me be more careful. $H = K_{2021} \cup \overline{K_k}$ on vertex set $A \cup B$ where $|A| = 2021, |B| = k$. Edges of $H$: all edges within $A$, no edges within $B$, no edges between $A$ and $B$.

$\overline{H}$: no edges within $A$, all edges within $B$, all edges between $A$ and $B$. So $\overline{H}$ is the complete bipartite graph $K_{2021, k}$ plus $K_k$ on $B$. Actually it's the join $\overline{K_{2021}} \vee K_k$.

Is this reachable from $K_{2021}$? $\overline{H}$ has $2021 + k$ vertices. It contains an independent set of size 2021 (the set $A$). But for $\overline{H}$ to be reachable from $K_{2021}$, it must contain a $K_{2021}$ subgraph. Does it? The clique number of $\overline{H}$: $B$ is a $K_k$, and each vertex in $B$ is connected to all of $A$. But vertices in $A$ have no edges among themselves. So the maximum clique is: take all of $B$ (size $k$) plus one vertex from $A$ (since every vertex in $A$ is connected to every vertex in $B$, but no two vertices in $A$ are connected). So max clique size is $k + 1$.

For $\overline{H}$ to be reachable from $K_{2021}$, we need $k + 1 \geq 2021$, i.e., $k \geq 2020$. So $n = 2021 + k \geq 2021 + 2020 = 4041$.

And at $k = 2020$, $n = 4041$: $\overline{H}$ has a clique of size 2021 (the set $B$ of size 2020 plus one vertex from $A$). But does $\overline{H}$ actually contain $K_{2021}$ as a subgraph? Yes, take $B \cup \{a\}$ for any $a \in A$: this is a clique of size 2021. But is the entire graph $\overline{H}$ reachable from $K_{2021}$? Just containing $K_{2021}$ as a subgraph is necessary but not sufficient.

Hmm, I need to think about what graphs are actually reachable, not just what contains $K_{2021}$.

Let me reconsider. Let me think about what properties reachable graphs have.

From $K_{2021}$, we can only add vertices and edges. The original 2021 vertices always form a clique. So every reachable graph contains $K_{2021}$ as a subgraph on the original vertices.

But we can also add new vertices with various edge patterns. Let me think about what edge patterns are possible for new vertices.

After one augmentation from $K_{2021}$ with $D \subseteq V(K_{2021})$: the new vertices $D' = \{v' : v \in D\}$ form a clique (since $D$ is a clique in $K_{2021}$). Each $v'$ is adjacent to a chosen subset of $V(K_{2021}) \setminus D$. And $v'$ is not adjacent to any vertex in $D$ (including $v$ itself).

So the new vertices form a clique, and each new vertex $v'$ is non-adjacent to exactly $|D|$ vertices of the original graph (the vertices in $D$), and adjacent to a subset of the remaining $2021 - |D|$ original vertices.

In subsequent augmentations, things get more complex because the graph is no longer complete.

Let me think about this differently. Let me consider the concept more abstractly.

Actually, let me think about what the answer might be and work backwards.

The problem asks for $M + m$ where $M$ is the max and $m$ is the min of $n$.

For the maximum: we want the largest $n$ such that there's a graph $H$ on $n$ vertices with both $H$ and $\overline{H}$ reachable from $K_{2021}$.

Is there an upper bound on $n$? Each augmentation adds at least 1 vertex (we must pick $D$ non-empty, I assume - actually, can $D$ be empty? If $D = \emptyset$, we add 0 vertices, which is a no-op. So effectively $D$ is non-empty). There's no limit on the number of augmentations, so we can add arbitrarily many vertices. But the constraint is that both $H$ and $\overline{H}$ must be reachable.

If $H$ is reachable from $K_{2021}$, $H$ contains $K_{2021}$. If $\overline{H}$ is reachable from $K_{2021}$, $\overline{H}$ contains $K_{2021}$, so $H$ contains $\overline{K_{2021}}$ (independent set of size 2021).

But there's no upper bound from this alone - we can have arbitrarily large graphs with both a large clique and large independent set.

Wait, but maybe there are more constraints from the reachability structure. Let me think again...

Actually, maybe the reachability imposes more structure. Let me think about what graphs are reachable from $K_n$ more carefully.

Let me think about a key invariant. Consider the "non-adjacency" structure. 

Hmm, let me think about this from the perspective of the complement. If $G$ is reachable from $K_n$, what can we say about $\overline{G}$?

The augmentation operation on $G$ in terms of $\overline{G}$: 
- We duplicate vertices in $D$, creating $v_i'$.
- In $G$, $v_i' v_j'$ is an edge iff $v_i v_j$ is an edge (both in $D$). In $\overline{G}$, $v_i' v_j'$ is a non-edge iff $v_i v_j$ is a non-edge, i.e., $v_i' v_j'$ is an edge iff $v_i v_j$ is an edge in $\overline{G}$... wait, let me be careful.

In $G$: $v_i' v_j'$ edge iff $v_i v_j$ edge (for $v_i, v_j \in D$). In $\overline{G}$: $v_i' v_j'$ non-edge iff $v_i v_j$ non-edge in $\overline{G}$... no. $\overline{G}$ has edge $v_i' v_j'$ iff $G$ has non-edge $v_i' v_j'$. $G$ has non-edge $v_i' v_j'$ iff $G$ has non-edge $v_i v_j$ (for $v_i, v_j \in D$). So $\overline{G}$ has edge $v_i' v_j'$ iff $G$ has non-edge $v_i v_j$ iff $\overline{G}$ has edge $v_i v_j$.

So in $\overline{G}$, the duplicates also copy the induced subgraph on $D$! (The duplicates in $\overline{G}$ form the same graph as $G[D]$... wait no. In $\overline{G}$, $v_i' v_j'$ is an edge iff $\overline{G}$ has $v_i v_j$ as an edge. So the duplicates in $\overline{G}$ form a copy of $\overline{G}[D]$.)

For the optional edges: in $G$, $v_i' v_j$ (for $v_i \in D, v_j \notin D$) can be an edge only if $v_i v_j$ is an edge in $G$. In $\overline{G}$, $v_i' v_j$ is a non-edge if $v_i v_j$ is a non-edge in $G$... 

In $\overline{G}$: $v_i' v_j$ edge iff $G$ has $v_i' v_j$ non-edge. $G$ has $v_i' v_j$ non-edge in two cases: (1) $v_i v_j$ is a non-edge in $G$ (then $v_i' v_j$ is forced to be a non-edge), or (2) $v_i v_j$ is an edge in $G$ but we chose not to add $v_i' v_j$.

In $\overline{G}$: $v_i' v_j$ edge iff $G$ has $v_i' v_j$ non-edge. This happens iff either $v_i v_j$ is a non-edge in $G$ (i.e., $\overline{G}$ has $v_i v_j$ edge), or $v_i v_j$ is an edge in $G$ but we chose not to connect (i.e., $\overline{G}$ has $v_i v_j$ non-edge, and we chose to have $\overline{G}$ edge $v_i' v_j$).

So in $\overline{G}$: $v_i' v_j$ (for $v_i \in D, v_j \notin D$) is forced to be an edge if $\overline{G}$ has $v_i v_j$ edge, and can optionally be an edge if $\overline{G}$ has $v_i v_j$ non-edge.

This is exactly the same augmentation rule! The augmentation operation is "self-complementary" in some sense. If we apply an augmentation to $G$ getting $G'$, then $\overline{G'}$ is obtained from $\overline{G}$ by an augmentation with the same $D$ and complementary choices.

So: $G'$ is reachable from $G$ via augmentation with set $D$ and certain edge choices iff $\overline{G'}$ is reachable from $\overline{G}$ via augmentation with set $D$ and complementary edge choices.

This means: $H$ is reachable from $K_{2021}$ iff $\overline{H}$ is reachable from $\overline{K_{2021}}$ (empty graph on 2021 vertices).

So the condition "$H$ and $\overline{H}$ are both reachable from $K_{2021}$" becomes:
- $H$ is reachable from $K_{2021}$
- $\overline{H}$ is reachable from $K_{2021}$, which by the duality means $H$ is reachable from $\overline{K_{2021}}$.

So we need $H$ to be reachable from both $K_{2021}$ and $\overline{K_{2021}}$ (empty graph on 2021 vertices).

Now, what graphs are reachable from $\overline{K_{2021}}$ (empty graph)?

From the empty graph, an augmentation with $D$: the duplicates $v_i'$ form the same induced subgraph as $D$ in the current graph. Since the current graph is empty, $D$ has no edges, so the duplicates have no edges among them. The optional edges: $v_i'$ can connect to $v_j \notin D$ only if $v_i v_j$ is an edge, but there are no edges, so no optional edges. So from the empty graph, we can only add isolated vertices. We can never create any edges!

So the only graph reachable from $\overline{K_{2021}}$ is $\overline{K_n}$ for any $n \geq 2021$ (the empty graph on $n$ vertices).

Wait, that can't be right. Let me re-check.

From $\overline{K_{2021}}$ (empty graph), augmentation with $D$: 
- Duplicates form induced subgraph of $D$, which is empty (no edges in $D$ since graph is empty). So duplicates have no edges among them.
- Optional edges: $v_i'$ can connect to $v_j \notin D$ only if $v_i v_j$ is an edge in current graph. But current graph is empty, so no edges. So no optional edges.

So indeed, from the empty graph, we can only add more isolated vertices. The only reachable graph is the empty graph on $n \geq 2021$ vertices.

So if $H$ is reachable from $\overline{K_{2021}}$, then $H = \overline{K_n}$ (empty graph on $n$ vertices) for some $n \geq 2021$.

And we need $H = \overline{K_n}$ to also be reachable from $K_{2021}$. Is $\overline{K_n}$ reachable from $K_{2021}$?

$\overline{K_n}$ has no edges. But $K_{2021}$ has all edges, and we can never remove edges. So the original 2021 vertices always form a clique. For $\overline{K_n}$ to be reachable, we'd need no edges at all, but the original 2021 vertices have all edges. Contradiction (for $n \geq 2021$).

So there's NO graph $H$ that is reachable from both $K_{2021}$ and $\overline{K_{2021}}$? That would mean no $H$ satisfies the condition, which contradicts the problem asking for $M + m$.

I must have made an error. Let me re-examine the duality.

Let me re-examine: if $G'$ is obtained from $G$ by augmentation, is $\overline{G'}$ obtained from $\overline{G}$ by augmentation?

$G'$ has vertex set $V(G) \cup D'$ where $D' = \{v' : v \in D\}$.

Edges of $G'$:
- All edges of $G$ (on $V(G)$).
- For $v_i, v_j \in D$: edge $v_i' v_j'$ iff edge $v_i v_j$ in $G$.
- For $v_i \in D, v_j \notin D$: edge $v_i' v_j$ optionally, only if edge $v_i v_j$ in $G$.
- No edge $v_i' v_i$.

$\overline{G'}$ has vertex set $V(G) \cup D'$.

Edges of $\overline{G'}$:
- All non-edges of $G$ (on $V(G)$) become edges.
- For $v_i, v_j \in D$: edge $v_i' v_j'$ iff non-edge $v_i v_j$ in $G$, i.e., edge $v_i v_j$ in $\overline{G}$.
- For $v_i \in D, v_j \notin D$: edge $v_i' v_j$ iff non-edge $v_i' v_j$ in $G'$. $v_i' v_j$ is a non-edge in $G'$ if either (a) $v_i v_j$ is a non-edge in $G$ (forced non-edge), or (b) $v_i v_j$ is an edge in $G$ but we chose not to add $v_i' v_j$.
  - In $\overline{G}$: case (a) means $v_i v_j$ is an edge in $\overline{G}$, and $v_i' v_j$ is forced to be an edge in $\overline{G'}$.
  - Case (b) means $v_i v_j$ is a non-edge in $\overline{G}$, and $v_i' v_j$ can optionally be an edge in $\overline{G'}$.
- Edge $v_i' v_i$: in $G'$, $v_i' v_i$ is a non-edge (always). So in $\overline{G'}$, $v_i' v_i$ is always an edge.

Now, is $\overline{G'}$ obtainable from $\overline{G}$ by an augmentation? In an augmentation of $\overline{G}$ with set $D$:
- Duplicates $v_i'$ form induced subgraph of $D$ in $\overline{G}$: edge $v_i' v_j'$ iff edge $v_i v_j$ in $\overline{G}$. ✓ Matches.
- For $v_i \in D, v_j \notin D$: $v_i' v_j$ edge in the augmentation only if $v_i v_j$ edge in $\overline{G}$, and it's optional. 
  - In $\overline{G'}$: $v_i' v_j$ is forced edge if $v_i v_j$ edge in $\overline{G}$, and optional if $v_i v_j$ non-edge in $\overline{G}$. 
  - This matches! The forced edges correspond to the mandatory part, and the optional edges correspond to the optional part.
- Edge $v_i' v_i$: in an augmentation of $\overline{G}$, $v_i' v_i$ should be a non-edge (since $v_i \in D$, and $v_i'$ is never connected to $v_i$). But in $\overline{G'}$, $v_i' v_i$ is always an edge!

This is the discrepancy! In $\overline{G'}$, $v_i' v_i$ is an edge, but in an augmentation of $\overline{G}$, $v_i' v_i$ would be a non-edge.

So the duality is NOT exact. The issue is the $v_i' v_i$ edge/non-edge.

So my earlier analysis was wrong. Let me reconsider.

In $G'$: $v_i' v_i$ is always a non-edge (for $v_i \in D$).
In $\overline{G'}$: $v_i' v_i$ is always an edge.

In an augmentation of $\overline{G}$ with $D$: $v_i' v_i$ is always a non-edge.

So $\overline{G'}$ has edges $v_i' v_i$ that an augmentation of $\overline{G}$ would not have. The duality breaks because of these "diagonal" edges.

Hmm, so the operation is not self-complementary. Let me reconsider the problem.

OK so let me go back to directly analyzing what graphs are reachable from $K_{2021}$.

Let me think about this more carefully. Let me consider the structure of reachable graphs.

From $K_n$, the first augmentation with $D$ of size $d$: adds $d$ new vertices forming a clique (since $D$ is a clique in $K_n$). Each new vertex $v_i'$ is non-adjacent to the $d$ vertices in $D$ (including $v_i$), and adjacent to a chosen subset of the $n - d$ remaining original vertices.

So after one step, the graph has the original $K_n$ plus a clique $D'$ of size $d$, where each vertex in $D'$ is non-adjacent to all of $D$ and adjacent to some subset of $V \setminus D$.

Key structural property: the new vertices $D'$ are non-adjacent to exactly the set $D$ (among the original vertices). And $D'$ forms a clique.

In the second augmentation, we pick a new $D_2$ from the current graph. The current graph has $n + d$ vertices. $D_2$ can include both original and new vertices. The duplicates $D_2'$ form the induced subgraph of $D_2$ in the current graph.

This is getting complex. Let me think about it differently.

Let me think about what the problem is really asking. We need both $H$ and $\overline{H}$ reachable from $K_{2021}$. Let me think about necessary conditions.

Necessary condition 1: $H$ contains $K_{2021}$ (the original vertices form a clique that's never broken).

Necessary condition 2: $\overline{H}$ contains $K_{2021}$, so $H$ contains an independent set of size 2021.

But there might be more structure. Let me think about what graphs are reachable from $K_n$.

Let me consider the "twin" structure. When we duplicate $v_i$ to get $v_i'$, $v_i'$ is a "twin" of $v_i$ in some sense - it copies $v_i$'s adjacency to $D$ and optionally to $V \setminus D$. But $v_i'$ is not adjacent to $v_i$ itself.

Actually, let me think about a specific important class of reachable graphs.

Claim: From $K_n$, we can reach any graph that contains $K_n$ as a subgraph and where the additional vertices can be added one at a time, each being a "partial twin" of some existing vertex.

Hmm, but we can also add multiple vertices at once, and the duplicates interact.

Let me think about the problem from a higher level. This is a competition problem, so there should be a clean answer.

Let me think about what $M$ and $m$ could be.

For $m$ (minimum): We need $H$ on $n$ vertices, both $H$ and $\overline{H}$ reachable from $K_{2021}$.

$H$ contains $K_{2021}$ (clique of size 2021).
$\overline{H}$ contains $K_{2021}$, so $H$ contains independent set of size 2021.

These two structures (clique and independent set) share at most 1 vertex. So $n \geq 4041$.

Can we achieve $n = 4041$? We need to construct $H$ on 4041 vertices with a clique $C$ of size 2021 and independent set $I$ of size 2021 sharing exactly 1 vertex, such that $H$ is reachable from $K_{2021}$ and $\overline{H}$ is reachable from $K_{2021}$.

Let me try: Let $C$ be the original 2021 vertices (forming $K_{2021}$). We need to add 2020 more vertices forming an independent set, with one of them... wait, we need $|C \cap I| = 1$. So $I$ has 2020 vertices outside $C$ and 1 vertex in $C$.

The 2020 new vertices must form an independent set (along with one vertex from $C$). The new vertices are non-adjacent to each other and non-adjacent to one specific vertex in $C$.

Can we reach such a graph from $K_{2021}$? We need to add 2020 vertices that are pairwise non-adjacent and each non-adjacent to some fixed vertex $c_0 \in C$.

From $K_{2021}$, to add a vertex $v'$ that is non-adjacent to $c_0$: pick $D = \{c_0\}$. Then $v'$ is non-adjacent to $c_0$ (mandatory) and can be adjacent to any subset of the other 2020 vertices. To make $v'$ non-adjacent to other new vertices, we need to be careful.

If we add the 2020 vertices one at a time, each time picking $D = \{c_0\}$: 
- First new vertex $u_1$: $D = \{c_0\}$, $u_1$ non-adjacent to $c_0$, can be adjacent to any of the other 2020 original vertices. Choose to connect $u_1$ to all of them (or some subset).
- Second new vertex $u_2$: $D = \{c_0\}$, $u_2$ non-adjacent to $c_0$, can be adjacent to any subset of $N(c_0) \setminus \{c_0\}$. But $N(c_0)$ in the current graph includes all original vertices except $c_0$... and also $u_1$ if $u_1$ is adjacent to $c_0$. But $u_1$ is NOT adjacent to $c_0$ (we made it non-adjacent). So $c_0$'s neighbors are the other 2020 original vertices (not $u_1$). So $u_2$ can be adjacent to any subset of the 2020 original vertices (other than $c_0$), but NOT to $u_1$ (since $u_1 \notin N(c_0)$).

So $u_2$ is automatically non-adjacent to $u_1$! Because $u_1$ is not a neighbor of $c_0$, and $u_2$ can only connect to neighbors of $c_0$.

Similarly, $u_3$ is non-adjacent to $u_1$ and $u_2$ (since neither is a neighbor of $c_0$). And so on.

So by repeatedly picking $D = \{c_0\}$, each new vertex is automatically non-adjacent to all previously added new vertices (since they're all non-neighbors of $c_0$), and non-adjacent to $c_0$. Each new vertex can be adjacent to any subset of the 2020 original vertices (other than $c_0$).

So we can add 2020 vertices, all non-adjacent to $c_0$ and pairwise non-adjacent, and each adjacent to any chosen subset of $C \setminus \{c_0\}$.

This gives us a graph where:
- $C = \{c_0, c_1, \ldots, c_{2020}\}$ forms $K_{2021}$.
- $U = \{u_1, \ldots, u_{2020}\}$ is an independent set.
- Each $u_i$ is non-adjacent to $c_0$ and adjacent to some subset of $\{c_1, \ldots, c_{2020}\}$.
- $I = \{c_0, u_1, \ldots, u_{2020}\}$ is an independent set of size 2021. ✓

So $H$ is reachable from $K_{2021}$ and contains an independent set of size 2021.

Now, is $\overline{H}$ reachable from $K_{2021}$?

$\overline{H}$: 
- $C$ is an independent set (no edges within $C$).
- $U$ is a clique (all edges within $U$).
- $c_0$ is adjacent to all of $U$ (since $c_0$ is non-adjacent to all $u_i$ in $H$).
- $c_i$ ($i \geq 1$) is adjacent to $u_j$ iff $c_i$ is non-adjacent to $u_j$ in $H$.

For $\overline{H}$ to be reachable from $K_{2021}$, it must contain $K_{2021}$. The clique number of $\overline{H}$: $U$ is a clique of size 2020. $c_0$ is adjacent to all of $U$, so $U \cup \{c_0\}$ is a clique of size 2021. ✓

But we need more than just containing $K_{2021}$ - we need $\overline{H}$ to actually be reachable.

$\overline{H}$ has 4041 vertices. It contains a clique $U \cup \{c_0\}$ of size 2021. The remaining 2020 vertices are $c_1, \ldots, c_{2020}$, which form an independent set in $\overline{H}$ (since they form a clique in $H$). Each $c_i$ is adjacent to some subset of $U$ in $\overline{H}$ (depending on the adjacencies in $H$), and $c_i$ is adjacent to $c_0$ in $\overline{H}$ (since $c_i c_0$ is an edge in $H$, so non-edge in $\overline{H}$)... wait, $c_i c_0$ is an edge in $H$ (both in $C$, which is a clique), so $c_i c_0$ is a non-edge in $\overline{H}$. And $c_i c_j$ for $i, j \geq 1$ is an edge in $H$ (clique), so non-edge in $\overline{H}$.

So in $\overline{H}$:
- $U \cup \{c_0\}$ is a clique of size 2021.
- $\{c_1, \ldots, c_{2020}\}$ is an independent set of size 2020.
- $c_0$ is non-adjacent to $c_i$ for $i \geq 1$.
- $c_i$ is adjacent to $u_j$ iff $c_i$ is non-adjacent to $u_j$ in $H$.

For $\overline{H}$ to be reachable from $K_{2021}$: we need to start with $K_{2021}$ on some 2021 vertices and build up. The natural choice is to start with $K_{2021}$ on $U \cup \{c_0\}$. Then we need to add $c_1, \ldots, c_{2020}$ as new vertices.

In $\overline{H}$, the vertices $c_1, \ldots, c_{2020}$ form an independent set and are non-adjacent to $c_0$. This is exactly the same structure as before! We need to add 2020 vertices that are pairwise non-adjacent and non-adjacent to $c_0$.

By the same argument as before, we can do this by repeatedly picking $D = \{c_0\}$ in augmentations of $\overline{H}$'s construction. Each new vertex $c_i$ would be non-adjacent to $c_0$ and to all previously added $c_j$'s, and can be adjacent to any subset of $U$ (the other 2020 vertices of the original clique, which are neighbors of $c_0$).

The adjacency of $c_i$ to $U$ in $\overline{H}$ is: $c_i$ adjacent to $u_j$ iff $c_i$ non-adjacent to $u_j$ in $H$. In $H$, $c_i$ is adjacent to a chosen subset of $\{c_1, \ldots, c_{2020}\}$... wait, I need to be more careful.

In $H$, the new vertices $u_j$ are each adjacent to a chosen subset of $C \setminus \{c_0\} = \{c_1, \ldots, c_{2020}\}$. Let's say $u_j$ is adjacent to $c_i$ in $H$ iff $j \in S_i$ (some subset). Then in $\overline{H}$, $c_i$ is adjacent to $u_j$ iff $j \notin S_i$.

When building $\overline{H}$ from $K_{2021}$ on $U \cup \{c_0\}$, we add $c_i$ by picking $D = \{c_0\}$, and $c_i$ can be adjacent to any subset of $U$ (the neighbors of $c_0$ in the current graph, which are all of $U$). We need $c_i$ to be adjacent to $\{u_j : j \notin S_i\}$ in $\overline{H}$. Since we can choose any subset, this is fine!

So $\overline{H}$ is reachable from $K_{2021}$! 

Wait, but I need to be more careful. When building $\overline{H}$, the order of adding $c_1, \ldots, c_{2020}$ matters. When we add $c_i$, the current graph has $U \cup \{c_0\}$ plus previously added $c_j$'s. The new vertex $c_i$ (duplicate of $c_0$) can be adjacent to any subset of $N(c_0) \setminus \{c_0\}$ in the current graph. $N(c_0)$ in the current graph includes all of $U$ (since $U \cup \{c_0\}$ is a clique) but NOT any previously added $c_j$ (since they're non-adjacent to $c_0$). So $c_i$ can be adjacent to any subset of $U$, and is automatically non-adjacent to all previously added $c_j$'s. 

So we can choose $c_i$'s adjacency to $U$ to be exactly $\{u_j : j \notin S_i\}$, which matches $\overline{H}$. And $c_i$ is non-adjacent to $c_0$ and to all other $c_j$'s, which also matches $\overline{H}$.

So $\overline{H}$ is reachable from $K_{2021}$. 

Therefore $n = 4041$ is achievable, and $m = 4041$.

Wait, but I should double-check: is $n = 4040$ possible? We need a clique of size 2021 and an independent set of size 2021 in a graph on 4040 vertices. The clique and independent set share at most 1 vertex, so $n \geq 2021 + 2021 - 1 = 4041$. So $n = 4040$ is impossible. Thus $m = 4041$.

Now for $M$ (maximum): Is there an upper bound on $n$?

We need $H$ on $n$ vertices with both $H$ and $\overline{H}$ reachable from $K_{2021}$.

$H$ contains $K_{2021}$ (clique of size 2021 on the original vertices).
$\overline{H}$ contains $K_{2021}$, so $H$ contains independent set of size 2021.

But as I noted, from $K_{2021}$ we can add arbitrarily many vertices (by doing many augmentations). So is $n$ unbounded?

Wait, let me think again. The constraint is that both $H$ and $\overline{H}$ are reachable from $K_{2021}$. 

$H$ reachable from $K_{2021}$: $H$ contains $K_{2021}$ as a subgraph (on the original 2021 vertices), plus additional vertices and edges.

$\overline{H}$ reachable from $K_{2021}$: $\overline{H}$ contains $K_{2021}$ as a subgraph (on some 2021 vertices of $H$), meaning $H$ has an independent set of size 2021.

But there might be more constraints from the reachability structure. Let me think...

Actually, I think the key constraint is more subtle. Let me think about what graphs are reachable from $K_n$.

Let me think about the "non-neighborhood" structure. When we add a vertex $v'$ as a duplicate of $v$ (with $D = \{v\}$), $v'$ is non-adjacent to $v$ and can be adjacent to any subset of $N(v) \setminus \{v\}$. So $v'$'s non-neighbors include $v$ and all non-neighbors of $v$ (since $v'$ can only connect to $v$'s neighbors).

More generally, $v'$'s non-neighborhood contains $v$'s non-neighborhood plus $v$ itself.

This suggests that non-neighborhoods can only grow. Let me formalize this.

Define the "non-neighborhood" of a vertex $u$ as $\bar{N}(u) = V \setminus (N(u) \cup \{u\})$ (the set of vertices non-adjacent to $u$, excluding $u$ itself). Actually, let me include $u$ itself: let $\bar{N}[u] = V \setminus N(u)$ (non-neighbors including $u$).

When we duplicate $v$ to get $v'$ with $D = \{v\}$: $v'$ is non-adjacent to $v$ and to all non-neighbors of $v$ (since $v'$ can only connect to $v$'s neighbors). $v'$ can be adjacent to any subset of $N(v) \setminus \{v\}$... wait, $v'$ can be adjacent to any subset of $N(v) \setminus D = N(v) \setminus \{v\}$. But $v \in N(v)$? In $K_n$, $v$ is not in $N(v)$ (no self-loops). So $N(v) \setminus \{v\} = N(v)$. And $v'$ is non-adjacent to $v$ (since $v \in D$). So $\bar{N}[v'] \supseteq \bar{N}[v] \cup \{v\}$... actually $\bar{N}[v'] = \bar{N}[v] \cup \{v\} \cup (\text{chosen non-neighbors among } N(v))$.

Hmm, this is getting complicated. Let me think about it differently.

Let me think about the problem in terms of a specific structural property.

Consider the relation between a vertex and its duplicate. When $v'$ is created as a duplicate of $v$ (in some augmentation where $v \in D$), $v'$ is non-adjacent to $v$. This non-adjacency is permanent (we never remove edges or non-edges... well, we never remove edges, but non-edges can become edges in later augmentations? No! We only add edges in augmentations, never remove them. And we only add edges involving new vertices. So edges between existing vertices are never changed.

Wait, that's a key point. Once two vertices exist, their adjacency is fixed forever. Augmentations only add new vertices and edges involving those new vertices. Existing edges and non-edges are never changed.

So the graph is built up monotonically: we start with $K_{2021}$ and add vertices one batch at a time, where each batch's edges to existing vertices are determined at creation time and never change.

This means the reachable graphs from $K_{2021}$ are exactly those that can be built by adding vertices in some order, where each vertex $v$ (when added) is a "partial twin" of some existing vertex $u$ (its "parent"), meaning:
- $v$ is non-adjacent to $u$.
- $v$ can be adjacent to any subset of $N(u) \setminus D$ where $D$ is the set being duplicated in this step.
- If multiple vertices are added in the same step, they form the induced subgraph of $D$.

Actually, when adding a batch $D'$ (duplicates of $D$), the new vertices form $G[D]$ (induced subgraph), and each $v_i' \in D'$ is non-adjacent to all of $D$ and can be adjacent to any subset of $N(v_i) \setminus D$.

Hmm, let me think about this more carefully for the case $|D| = 1$. If we always use $|D| = 1$, then each step adds one vertex $v'$ as a duplicate of some existing vertex $v$, where:
- $v'$ is non-adjacent to $v$.
- $v'$ can be adjacent to any subset of $N(v)$ (the neighbors of $v$ in the current graph).
- $v'$ is non-adjacent to all non-neighbors of $v$ (in the current graph).

So $v'$'s adjacency is: non-adjacent to $v$ and all non-neighbors of $v$; adjacent to a chosen subset of $N(v)$.

This means: $\bar{N}[v'] \supseteq \bar{N}[v] \cup \{v\}$, with equality if we connect $v'$ to all of $N(v)$.

And $N[v'] \subseteq N[v] \setminus \{v\} \cup \{v'\}$... hmm, $v'$ is adjacent to a subset of $N(v)$, and $v'$ is not adjacent to $v$. So $N(v') \subseteq N(v)$, and $v' \notin N(v')$ (no self-loops), and $v \notin N(v')$.

Key insight: $N(v') \subseteq N(v)$. The neighborhood of the duplicate is a subset of the neighborhood of the original.

And $\bar{N}[v'] \supseteq \bar{N}[v] \cup \{v\}$. The non-neighborhood (including self) of the duplicate is a superset of the non-neighborhood of the original plus the original.

Now, if we always use $|D| = 1$, we can build any graph where vertices can be ordered $v_1, v_2, \ldots, v_n$ (with $v_1, \ldots, v_{2021}$ being the original clique) such that for each $v_i$ ($i > 2021$), there exists a "parent" $v_j$ with $j < i$ such that $N(v_i) \subseteq N(v_j)$ (in the final graph, since adjacencies are fixed at creation time and never change, $N(v_i)$ in the final graph equals $N(v_i)$ at creation time, which is a subset of $N(v_j)$ at creation time, which equals $N(v_j)$ in the final graph restricted to vertices existing at that time... 

Hmm wait, this isn't quite right because $N(v_j)$ grows over time as more vertices are added. Let me reconsider.

At the time $v_i$ is created (as a duplicate of $v_j$), $v_i$'s neighbors are a subset of $v_j$'s neighbors at that time. After that, new vertices may be added that are adjacent to $v_j$ but not to $v_i$ (or vice versa). So in the final graph, $N(v_i)$ is NOT necessarily a subset of $N(v_j)$.

But among the vertices that existed at the time of $v_i$'s creation, $v_i$'s neighbors are a subset of $v_j$'s neighbors. And $v_i$ is non-adjacent to $v_j$.

For vertices created after $v_i$, their adjacency to $v_i$ and $v_j$ is independent (determined by their own creation).

So the subset relation only holds for vertices existing at creation time. This makes the analysis more complex.

Let me think about this problem differently. Maybe I should think about what structures are forced.

Let me consider the problem from the competition perspective. The answer is $M + m$. We found $m = 4041$. What about $M$?

Let me think about whether $n$ can be arbitrarily large.

Consider building $H$ as follows: Start with $K_{2021}$ on vertices $C = \{c_0, \ldots, c_{2020}\}$. Add 2020 vertices $U = \{u_1, \ldots, u_{2020}\}$ as before (each a duplicate of $c_0$, non-adjacent to $c_0$ and to each other, adjacent to chosen subsets of $C \setminus \{c_0\}$). This gives $n = 4041$.

Can we add more vertices? Let's add another vertex $w$ as a duplicate of some existing vertex. Say $w$ is a duplicate of $u_1$. Then $w$ is non-adjacent to $u_1$, and $w$ can be adjacent to any subset of $N(u_1)$ (at the current time). $N(u_1)$ includes $u_1$'s neighbors among $C \setminus \{c_0\}$ (the chosen subset) and possibly some other $u_j$'s... but $u_j$'s are non-adjacent to $u_1$ (they're all non-adjacent to each other). So $N(u_1) = $ chosen subset of $C \setminus \{c_0\}$.

$w$ is non-adjacent to $u_1$, $c_0$ (since $c_0 \notin N(u_1)$), and all other $u_j$ (since $u_j \notin N(u_1)$). $w$ can be adjacent to any subset of $N(u_1) \subseteq C \setminus \{c_0\}$.

So $w$ is non-adjacent to $c_0$, all of $U$, and adjacent to a subset of $C \setminus \{c_0\}$. This is similar to the $u_i$'s but $w$ is a duplicate of $u_1$ instead of $c_0$.

In $H$, $w$ is non-adjacent to $c_0$ and all $u_j$'s, and adjacent to some subset of $C \setminus \{c_0\}$. So $w$ can be added to the independent set $I = \{c_0, u_1, \ldots, u_{2020}\}$... wait, $w$ is non-adjacent to all of $I$? $w$ is non-adjacent to $c_0$ ✓, non-adjacent to all $u_j$ ✓. But $w$ is adjacent to some subset of $C \setminus \{c_0\}$. The elements of $C \setminus \{c_0\}$ are $c_1, \ldots, c_{2020}$, which are NOT in $I$ (except $c_0$). So $w$ is non-adjacent to all of $I$, meaning $I \cup \{w\}$ is an independent set of size 2022.

But we need $\overline{H}$ to be reachable from $K_{2021}$, which requires $\overline{H}$ to contain $K_{2021}$, i.e., $H$ to contain an independent set of size 2021. Having a larger independent set is fine.

But we also need $\overline{H}$ to be reachable, not just contain $K_{2021}$. Let me check if $\overline{H}$ (with $w$ added) is reachable.

In $\overline{H}$: $w$ is adjacent to $c_0$, all $u_j$'s, and non-adjacent to some subset of $C \setminus \{c_0\}$. 

For $\overline{H}$ to be reachable from $K_{2021}$, we need to build it from $K_{2021}$. The clique in $\overline{H}$ is $U \cup \{c_0\}$ (size 2021). We add $c_1, \ldots, c_{2020}$ and $w$ as new vertices.

In $\overline{H}$, $w$ is adjacent to $c_0$ and all $u_j$'s, and non-adjacent to some $c_i$'s. Can we add $w$ as a duplicate of some vertex in $\overline{H}$'s construction?

If we add $w$ as a duplicate of $u_1$ in $\overline{H}$'s construction: $w$ is non-adjacent to $u_1$, and can be adjacent to any subset of $N(u_1)$ in $\overline{H}$ at that time. In $\overline{H}$, $N(u_1)$ includes $c_0$ and all other $u_j$'s (since $U \cup \{c_0\}$ is a clique) and some $c_i$'s. But $w$ needs to be adjacent to $c_0$ and all $u_j$'s in $\overline{H}$. $w$ is non-adjacent to $u_1$ (its parent), which is fine since $w$ is adjacent to $u_1$ in $\overline{H}$... 

Wait, no. In $\overline{H}$, $w$ IS adjacent to $u_1$ (since $w$ is non-adjacent to $u_1$ in $H$). But if $w$ is a duplicate of $u_1$, then $w$ is non-adjacent to $u_1$. Contradiction!

So $w$ cannot be a duplicate of $u_1$ in $\overline{H}$'s construction. Let me think about what $w$ can be a duplicate of.

In $\overline{H}$, $w$ is adjacent to $c_0$ and all $u_j$. $w$ is non-adjacent to some $c_i$'s. If $w$ is a duplicate of $c_0$ in $\overline{H}$'s construction: $w$ is non-adjacent to $c_0$. But $w$ is adjacent to $c_0$ in $\overline{H}$. Contradiction.

If $w$ is a duplicate of $u_j$ for some $j$: $w$ is non-adjacent to $u_j$. But $w$ is adjacent to all $u_j$ in $\overline{H}$. Contradiction.

If $w$ is a duplicate of $c_i$ for some $i \geq 1$: $w$ is non-adjacent to $c_i$. In $\overline{H}$, $w$ is non-adjacent to some $c_i$'s, so this could work for one of those. $w$ can be adjacent to any subset of $N(c_i)$ in $\overline{H}$ at that time. $N(c_i)$ in $\overline{H}$ includes $c_0$ (is $c_0$ adjacent to $c_i$ in $\overline{H}$? In $H$, $c_0 c_i$ is an edge (both in clique $C$), so in $\overline{H}$, $c_0 c_i$ is a non-edge. So $c_0 \notin N(c_i)$ in $\overline{H}$.) Hmm, so $c_i$'s neighbors in $\overline{H}$ are some subset of $U$ (those $u_j$ that are non-adjacent to $c_i$ in $H$). And $c_i$ is non-adjacent to $c_0$, all other $c_k$'s, and some $u_j$'s.

If $w$ is a duplicate of $c_i$, then $w$ is non-adjacent to $c_i$, and can be adjacent to any subset of $N(c_i) \subseteq U$. But $w$ needs to be adjacent to $c_0$ in $\overline{H}$, and $c_0 \notin N(c_i)$. So $w$ cannot be adjacent to $c_0$. Contradiction.

So $w$ cannot be added as a single-vertex duplicate in $\overline{H}$'s construction. What about multi-vertex $D$?

Hmm, this is getting complicated. Let me think about whether we can add $w$ using a larger $D$.

Actually, maybe I should think about this more carefully. Let me consider what happens when $|D| > 1$.

If $D = \{c_0, u_1\}$ in $\overline{H}$'s construction: we create $c_0'$ and $u_1'$. $c_0' u_1'$ is an edge iff $c_0 u_1$ is an edge in $\overline{H}$. In $\overline{H}$, $c_0$ is adjacent to $u_1$ (since $c_0$ is non-adjacent to $u_1$ in $H$). So $c_0' u_1'$ is an edge.

$c_0'$ is non-adjacent to $c_0$ and $u_1$, and can be adjacent to any subset of $N(c_0) \setminus D = N(c_0) \setminus \{c_0, u_1\}$. In $\overline{H}$, $N(c_0)$ includes all of $U$ (since $U \cup \{c_0\}$ is a clique) and... $c_0$ is non-adjacent to all $c_i$'s in $\overline{H}$. So $N(c_0) = U$. So $c_0'$ can be adjacent to any subset of $U \setminus \{u_1\}$.

$u_1'$ is non-adjacent to $c_0$ and $u_1$, and can be adjacent to any subset of $N(u_1) \setminus D = N(u_1) \setminus \{c_0, u_1\}$. In $\overline{H}$, $N(u_1)$ includes $c_0$ and all other $u_j$'s and some $c_i$'s. So $u_1'$ can be adjacent to any subset of $(U \setminus \{u_1\}) \cup \{c_i : u_1 \text{ adj } c_i \text{ in } \overline{H}\}$.

This is getting very complex. Let me step back and think about the problem more abstractly.

Let me think about what property a graph must have to be reachable from $K_n$, and what property its complement must have.

Actually, let me think about this problem from a different angle. Let me consider the concept of "co-reachable" - both $H$ and $\overline{H}$ reachable from $K_{2021}$.

Key insight: $H$ reachable from $K_{2021}$ means $H$ can be built from $K_{2021}$ by adding vertices, where each new vertex is a "partial twin" of some existing vertex (or part of a batch of twins).

Let me think about the maximum. Can we make $n$ arbitrarily large?

Consider the following construction. Start with $K_{2021}$ on $C = \{c_0, \ldots, c_{2020}\}$. Add vertices $u_1, \ldots, u_{2020}$ as duplicates of $c_0$ (each non-adjacent to $c_0$ and to each other, adjacent to all of $C \setminus \{c_0\}$). Now we have 4041 vertices.

Now add $w_1$ as a duplicate of $u_1$: $w_1$ is non-adjacent to $u_1$, non-adjacent to $c_0$ (since $c_0 \notin N(u_1)$), non-adjacent to all other $u_j$ (since $u_j \notin N(u_1)$), and can be adjacent to any subset of $N(u_1) = C \setminus \{c_0\}$. Choose to connect $w_1$ to all of $C \setminus \{c_0\}$.

So $w_1$ has the same adjacency as $u_1$ (adjacent to all of $C \setminus \{c_0\}$, non-adjacent to $c_0$ and all $u_j$'s), except $w_1$ is also non-adjacent to $u_1$.

Now add $w_2$ as a duplicate of $u_1$: $w_2$ is non-adjacent to $u_1$, and can be adjacent to any subset of $N(u_1)$ at this time. $N(u_1)$ at this time is $C \setminus \{c_0\}$ (same as before, since $w_1$ is not adjacent to $u_1$). $w_2$ is non-adjacent to $c_0$, all $u_j$'s, and $w_1$ (since $w_1 \notin N(u_1)$). Choose to connect $w_2$ to all of $C \setminus \{c_0\}$.

So $w_2$ is non-adjacent to $c_0$, all $u_j$'s, $w_1$, and adjacent to all of $C \setminus \{c_0\}$.

We can keep adding $w_3, w_4, \ldots$ as duplicates of $u_1$, each non-adjacent to all previous $w_k$'s and $u_j$'s and $c_0$, adjacent to all of $C \setminus \{c_0\}$.

So in $H$, we have:
- $C = K_{2021}$ (clique).
- $U \cup W \cup \{c_0\}$ is an independent set (where $W = \{w_1, w_2, \ldots\}$).
- Each $u_j$ and $w_k$ is adjacent to all of $C \setminus \{c_0\}$.

Wait, actually $u_j$'s are adjacent to all of $C \setminus \{c_0\}$ and $w_k$'s are adjacent to all of $C \setminus \{c_0\}$. And $u_j$'s and $w_k$'s are all pairwise non-adjacent. And all are non-adjacent to $c_0$.

So $H$ has a clique $C$ of size 2021 and an independent set $\{c_0\} \cup U \cup W$ of size $1 + 2020 + |W| = 2021 + |W|$.

Now, is $\overline{H}$ reachable from $K_{2021}$?

$\overline{H}$: 
- $C$ is an independent set.
- $\{c_0\} \cup U \cup W$ is a clique (call it $Q$).
- $c_0$ is adjacent to all of $U \cup W$ (non-adjacent in $H$) and non-adjacent to $C \setminus \{c_0\}$ (adjacent in $H$).
- Each $u_j$ and $w_k$ is adjacent to all other elements of $Q$ and non-adjacent to all of $C \setminus \{c_0\}$ (since they're adjacent to all of $C \setminus \{c_0\}$ in $H$).

So $\overline{H}$: $Q$ is a clique of size $2021 + |W|$, $C \setminus \{c_0\}$ is an independent set of size 2020, and there are no edges between $Q$ and $C \setminus \{c_0\}$... wait, let me check. $u_j$ is adjacent to $c_i$ ($i \geq 1$) in $H$, so non-adjacent in $\overline{H}$. $c_0$ is adjacent to $c_i$ ($i \geq 1$) in $H$ (clique), so non-adjacent in $\overline{H}$. So indeed, no edges between $Q$ and $C \setminus \{c_0\}$ in $\overline{H}$.

So $\overline{H} = K_{2021+|W|} \cup \overline{K_{2020}}$ (disjoint union of a clique and independent set, with no edges between them).

For $\overline{H}$ to be reachable from $K_{2021}$: $\overline{H}$ must contain $K_{2021}$ as a subgraph. The clique $Q$ has size $2021 + |W| \geq 2021$. ✓

But is $\overline{H}$ actually reachable? $\overline{H} = K_{2021+|W|} \cup \overline{K_{2020}}$. We need to build this from $K_{2021}$.

Start with $K_{2021}$ on $Q_0 \subseteq Q$ (some 2021 vertices of $Q$). We need to add the remaining $|W|$ vertices of $Q$ and the 2020 vertices of $C \setminus \{c_0\}$.

The remaining $|W|$ vertices of $Q$ need to be adjacent to all of $Q_0$ and to each other (they're in the clique $Q$). Can we add a vertex to a clique as a duplicate of a clique vertex? If $v$ is in the clique and we duplicate $v$ (with $D = \{v\}$), the duplicate $v'$ is non-adjacent to $v$. But we need $v'$ to be adjacent to $v$ (since both are in $Q$, a clique). Contradiction!

So we can't add a vertex to a clique by duplicating a single clique vertex. What about duplicating a non-clique vertex?

If we duplicate a vertex $u$ in $C \setminus \{c_0\}$ (which is an independent set in $\overline{H}$, so $u$ has no neighbors): the duplicate $u'$ is non-adjacent to $u$ and can be adjacent to any subset of $N(u) = \emptyset$. So $u'$ is isolated. Not helpful for adding to the clique.

What about $|D| > 1$? If $D = \{q_1, q_2\}$ where $q_1, q_2 \in Q$ (clique), the duplicates $q_1', q_2'$ form an edge (since $q_1 q_2$ is an edge). $q_1'$ is non-adjacent to $q_1$ and $q_2$, and can be adjacent to any subset of $N(q_1) \setminus D = (Q \setminus \{q_1, q_2\}) \cup \emptyset$ (since $q_1$'s neighbors are $Q \setminus \{q_1\}$, and we remove $q_1, q_2$). So $q_1'$ can be adjacent to any subset of $Q \setminus \{q_1, q_2\}$.

But $q_1'$ is non-adjacent to $q_1$ and $q_2$. For $q_1'$ to be in the clique $Q$, it needs to be adjacent to all of $Q$, including $q_1$ and $q_2$. Contradiction.

So it seems impossible to add a vertex to a clique! Any duplicate is non-adjacent to its original, so it can't be in the same clique as its original.

But wait - we can add vertices to a clique if the clique is the original $K_{2021}$. The original 2021 vertices form a clique, and we can't add to it. But can we form a new, larger clique?

Actually, the duplicates of a clique $D$ form a clique $D'$ (same induced subgraph). And each $v_i' \in D'$ can be adjacent to any subset of $N(v_i) \setminus D$. If $v_i$ is adjacent to some vertex $w \notin D$, then $v_i'$ can be adjacent to $w$. So $D' \cup \{w\}$ could be a clique if all $v_i'$ are adjacent to $w$ and $w$ is adjacent to all $v_i'$ (which it is, since we choose to make $v_i'$ adjacent to $w$).

But $D' \cup D$ is NOT a clique because $v_i'$ is non-adjacent to $v_i$.

So we can grow a clique by duplicating all its members and having the duplicates connect to external vertices, but the new clique $D'$ doesn't include the originals $D$.

Hmm, so the maximum clique in a reachable graph is at most... let me think. The original $K_{2021}$ has clique number 2021. Can we create a larger clique?

If we duplicate all 2021 vertices ($D = V(K_{2021})$), the duplicates form $K_{2021}$ (same induced subgraph). Each duplicate $v_i'$ is non-adjacent to $v_i$ and can be adjacent to any subset of $N(v_i) \setminus D = \emptyset$ (since all vertices are in $D$). So the duplicates form an isolated $K_{2021}$ with no edges to the originals. The graph is $K_{2021} \cup K_{2021}$ (disjoint union of two cliques). Clique number is still 2021.

What if we duplicate a subset? $D \subset V(K_{2021})$, $|D| = d$. Duplicates form $K_d$. Each $v_i'$ can be adjacent to any subset of $V(K_{2021}) \setminus D$ (size $2021 - d$). If we connect all $v_i'$ to all of $V \setminus D$, then $D' \cup (V \setminus D)$ is a clique (since $D'$ is a clique, $V \setminus D$ is a clique, and all edges between them exist). This clique has size $d + (2021 - d) = 2021$. Still 2021.

Can we do better? In the next step, duplicate a subset of $D' \cup (V \setminus D)$... but the same argument applies. The new clique will have size at most 2021.

Wait, actually, let me reconsider. After the first step, we have $V$ (original $K_{2021}$) and $D'$ (clique of size $d$, connected to all of $V \setminus D$, non-adjacent to $D$). The clique $D' \cup (V \setminus D)$ has size 2021.

Now, in the second step, pick $D_2 \subseteq D' \cup (V \setminus D)$, say $|D_2| = d_2$. The duplicates $D_2'$ form a clique of size $d_2$. Each $v_i' \in D_2'$ (for $v_i \in D_2$) can be adjacent to any subset of $N(v_i) \setminus D_2$. Since $v_i \in D' \cup (V \setminus D)$ which is a clique of size 2021, $N(v_i) \supseteq (D' \cup (V \setminus D)) \setminus \{v_i\}$ (size 2020) plus possibly some vertices in $D$ (if $v_i \in V \setminus D$, then $v_i$ is adjacent to all of $V \setminus \{v_i\}$, which includes $D$; if $v_i \in D'$, then $v_i$ is adjacent to $V \setminus D$ but not to $D$).

Case 1: $v_i \in V \setminus D$. Then $N(v_i) = V \setminus \{v_i\} \cup D'$ (all original vertices except $v_i$, plus all duplicates). Actually, $v_i$ is adjacent to all other original vertices (since $V$ is a clique) and to all $v_j' \in D'$ (since we connected all duplicates to all of $V \setminus D$). So $N(v_i) = (V \setminus \{v_i\}) \cup D'$. Size: $2020 + d$.

$v_i' \in D_2'$ can be adjacent to any subset of $N(v_i) \setminus D_2$. If $D_2 \subseteq V \setminus D$, then $N(v_i) \setminus D_2 = (V \setminus \{v_i\} \setminus D_2) \cup D'$. The new clique $D_2' \cup (N(v_i) \setminus D_2)$... hmm, this isn't quite right because the clique includes $D_2'$ and the vertices they're all connected to.

Let me think about it differently. The maximum clique reachable from $K_n$ is $n$. Here's why:

Claim: The clique number of any graph reachable from $K_n$ is exactly $n$ (well, at least $n$ since we start with $K_n$, and at most $n$).

Proof that clique number $\leq n$: Consider any reachable graph $G$. We need to show $\omega(G) \leq n = 2021$.

Hmm, actually I'm not sure this is true. Let me think of a potential counterexample.

From $K_3$ (vertices $a, b, c$): duplicate $D = \{a\}$, get $a'$, connect $a'$ to $b$ and $c$. Now the graph has $K_3$ on $\{a, b, c\}$ and $a'$ adjacent to $b, c$ but not $a$. Clique $\{a', b, c\}$ has size 3. Still 3.

Now duplicate $D_2 = \{a'\}$, get $a''$, connect $a''$ to $b$ and $c$ (neighbors of $a'$). $a''$ is non-adjacent to $a'$ and can be adjacent to $b, c$. Clique $\{a'', b, c\}$ has size 3.

What if we duplicate $D_2 = \{b\}$? Get $b'$, non-adjacent to $b$, can be adjacent to $N(b) \setminus \{b\} = \{a, c, a'\}$. Connect $b'$ to $a, c, a'$. Now $b'$ is adjacent to $a, c, a'$. Is $\{a, c, a', b'\}$ a clique? $a$-$c$: yes. $a$-$a'$: no! $a'$ is non-adjacent to $a$. So not a clique.

$\{c, a', b'\}$: $c$-$a'$: yes. $c$-$b'$: yes. $a'$-$b'$: yes (both in $D_2'$... no, $a' \notin D_2'$. $b' \in D_2'$. $a'$ and $b'$: is there an edge? $b'$ was connected to $a'$ (we chose to connect $b'$ to $a'$). So yes. So $\{c, a', b'\}$ is a clique of size 3.

Can we get a clique of size 4 from $K_3$? Let me try harder.

After step 1: $a, b, c$ form $K_3$. $a'$ adjacent to $b, c$, non-adjacent to $a$.

Step 2: $D_2 = \{a, a'\}$. $a$ and $a'$: non-adjacent. So duplicates $a^*$ and $a'^*$ are non-adjacent to each other. $a^*$ non-adjacent to $a, a'$, can be adjacent to $N(a) \setminus \{a, a'\} = \{b, c\}$. $a'^*$ non-adjacent to $a, a'$, can be adjacent to $N(a') \setminus \{a, a'\} = \{b, c\}$.

So $a^*$ and $a'^*$ are both adjacent to $b, c$ (if we choose), but non-adjacent to each other. Clique $\{a^*, b, c\}$ or $\{a'^*, b, c\}$, size 3.

It really seems like the clique number stays at $n$. Let me try to prove this.

Claim: If $G$ is reachable from $K_n$, then $\omega(G) \leq n$.

Proof attempt: Consider the "origin" of each vertex. The original $n$ vertices are "generation 0". Vertices created in the $k$-th augmentation are "generation $k$". 

When a vertex $v'$ is created as a duplicate of $v$ (in a batch $D$), $v'$ is non-adjacent to all vertices in $D$. In particular, $v'$ is non-adjacent to its "parent" $v$.

Consider a maximum clique $Q$ in $G$. For each vertex in $Q$, consider its generation. Can two vertices of the same generation be in $Q$? If $v_i'$ and $v_j'$ are created in the same batch (duplicates of $v_i$ and $v_j$), they're adjacent iff $v_i v_j$ is an edge. So they can be in a clique together.

Hmm, the generation idea doesn't directly work. Let me think differently.

Alternative approach: Consider a "coloring" or "labeling" of vertices.

Actually, let me think about it in terms of a potential function. Define for each vertex $v$ a set $S(v) \subseteq V(K_n)$ (the original vertices). For original vertices, $S(v_i) = \{v_i\}$. When $v'$ is created as a duplicate of $v$ in a batch $D$, $S(v') = S(v) \setminus S(D)$... no, this doesn't seem right.

Let me try another approach. Let me think about the "non-adjacency" graph (complement) and its chromatic number.

$\omega(G) \leq n$ iff $\chi(\overline{G}) \leq n$ (since $\omega(G) = \chi(\overline{G})$... no, that's not right either. $\omega(G)$ is the clique number of $G$, which equals the independence number $\alpha(\overline{G})$... no. $\omega(G)$ = size of largest clique in $G$ = size of largest independent set in $\overline{G}$ = $\alpha(\overline{G})$. And $\alpha(\overline{G}) \leq \chi(\overline{G})$... this doesn't directly help.

Let me try to directly prove $\omega(G) \leq n$ for reachable $G$.

Induction on the number of augmentations. Base case: $G = K_n$, $\omega = n$. ✓

Inductive step: $G$ is obtained from $G'$ by an augmentation with set $D$. $G$ adds vertices $D' = \{v' : v \in D\}$. We need to show $\omega(G) \leq n$ given $\omega(G') \leq n$.

A clique in $G$ either:
(a) Doesn't include any vertex from $D'$: then it's a clique in $G'$, so size $\leq n$.
(b) Includes some vertices from $D'$.

For (b), let $Q$ be a clique in $G$ including vertices $Q \cap D' = \{v_{i_1}', \ldots, v_{i_k}'\}$ and $Q \setminus D' = R$ (vertices in $G'$).

The vertices $v_{i_1}', \ldots, v_{i_k}'$ form a clique, so $\{v_{i_1}, \ldots, v_{i_k}\}$ form a clique in $G'$ (since duplicates copy the induced subgraph).

Each $v_{i_j}'$ is non-adjacent to all of $D$. So $R \cap D = \emptyset$ (since $R$ is adjacent to all of $Q \cap D'$, but vertices in $D$ are non-adjacent to all of $D'$).

Each $v_{i_j}'$ is adjacent to $r \in R$ only if $v_{i_j}$ is adjacent to $r$ in $G'$ (and $r \notin D$). So for all $r \in R$, $r$ is adjacent to all of $\{v_{i_1}, \ldots, v_{i_k}\}$ in $G'$.

So $\{v_{i_1}, \ldots, v_{i_k}\} \cup R$ is a clique in $G'$ (since $\{v_{i_1}, \ldots, v_{i_k}\}$ is a clique, $R$ is a clique (as a subset of clique $Q$), and every $v_{i_j}$ is adjacent to every $r \in R$).

Therefore $|\{v_{i_1}, \ldots, v_{i_k}\} \cup R| = k + |R| = |Q| \leq \omega(G') \leq n$.

So $\omega(G) \leq n$. ✓

So the clique number of any graph reachable from $K_n$ is at most $n$.

Now, applying this to our problem:
- $H$ reachable from $K_{2021}$: $\omega(H) \leq 2021$.
- $\overline{H}$ reachable from $K_{2021}$: $\omega(\overline{H}) \leq 2021$, i.e., $\alpha(H) \leq 2021$.

So $H$ has $\omega(H) \leq 2021$ and $\alpha(H) \leq 2021$.

By Ramsey theory, $R(2022, 2022) > n$ is needed for such $H$ to exist. But we also need reachability, not just existence.

But the question is about the maximum $n$. We have $\omega(H) \leq 2021$ and $\alpha(H) \leq 2021$. By Ramsey, $R(2022, 2022)$ is the smallest $n$ such that every graph on $n$ vertices has $\omega \geq 2022$ or $\alpha \geq 2022$. So for $n < R(2022, 2022)$, there exist graphs with $\omega \leq 2021$ and $\alpha \leq 2021$.

But we need more: both $H$ and $\overline{H}$ must be reachable. The reachability condition is stronger than just $\omega, \alpha \leq 2021$.

Hmm, but the problem asks for a specific numerical answer, so maybe the maximum is also related to 2021 in a clean way.

Let me think about what other constraints reachability imposes.

We showed $\omega(G) \leq n$ for $G$ reachable from $K_n$. Similarly, the original $n$ vertices always form a clique, so $\omega(G) \geq n$. Thus $\omega(G) = n$ for all $G$ reachable from $K_n$.

Wait, that's not right. $\omega(G) \geq n$ because the original $n$ vertices form a clique. And $\omega(G) \leq n$ by our proof. So $\omega(G) = n$ exactly.

So for $H$ reachable from $K_{2021}$: $\omega(H) = 2021$.
For $\overline{H}$ reachable from $K_{2021}$: $\omega(\overline{H}) = 2021$, so $\alpha(H) = 2021$.

So $H$ has $\omega(H) = 2021$ and $\alpha(H) = 2021$.

Now, by Ramsey theory, $R(2022, 2022)$ is the threshold. For $n \geq R(2022, 2022)$, every graph on $n$ vertices has $\omega \geq 2022$ or $\alpha \geq 2022$. So we need $n < R(2022, 2022)$.

But $R(2022, 2022)$ is a huge number, and the problem expects a clean answer. So maybe the reachability condition is more restrictive than just $\omega = \alpha = 2021$.

Let me think about what other structural properties reachable graphs have.

We showed that for any clique $Q$ in a reachable graph, we can "project" it back to a clique in the previous graph, and ultimately to a clique in $K_n$. This projection maps each duplicate $v'$ to its original $v$. So every clique in $G$ corresponds to a clique of the same size in $K_n$, which has size at most $n$.

More specifically, define a "projection" $\pi$: for original vertices, $\pi(v) = v$. For a duplicate $v'$ created in some augmentation, $\pi(v') = \pi(v)$ where $v$ is the original it duplicated. Then $\pi$ maps every vertex to an original vertex in $K_n$.

The key property: if $v'$ and $w'$ are adjacent in $G$, then $\pi(v')$ and $\pi(w')$ are adjacent in $K_n$ (i.e., $\pi(v') \neq \pi(w')$). Wait, is this true?

Let me check. If $v'$ and $w'$ are both created in the same batch (duplicates of $v$ and $w$), they're adjacent iff $v$ and $w$ are adjacent in the current graph. If $v \neq w$ and they're adjacent, then $\pi(v') = \pi(v) \neq \pi(w) = \pi(w')$ (assuming $\pi$ is injective on the current graph... which it might not be).

Hmm, actually $\pi$ might not be injective. If $v$ was itself a duplicate of some $u$, and $w$ was also a duplicate of $u$ (in a different batch), then $\pi(v) = \pi(w) = u$. And if $v$ and $w$ are adjacent, then $\pi(v) = \pi(w) = u$, so the projection maps an edge to a self-loop, which is not an edge in $K_n$.

So the projection argument doesn't directly work for proving $\omega \leq n$. But we already proved $\omega \leq n$ by induction, so that's fine.

Let me think about other properties. 

Actually, let me think about the structure more carefully. The projection $\pi$ maps each vertex to an original vertex. For a clique $Q$ in $G$, the projection $\pi(Q)$ is a subset of $V(K_n)$. We showed $|Q| \leq n$, but can we say more?

In the inductive proof, we showed that for a clique $Q$ in $G$ (obtained from $G'$ by augmentation with $D$), the "projected" clique $\{v_{i_1}, \ldots, v_{i_k}\} \cup R$ in $G'$ has the same size. By induction, this maps back to a clique of size $|Q|$ in $K_n$.

So every clique in $G$ projects to a clique of the same size in $K_n$, which means $|Q| \leq n$ and the projection is injective on $Q$ (since a clique in $K_n$ has distinct vertices).

So $\pi$ is injective on every clique. Similarly, $\pi$ is injective on every independent set? Let me check.

For independent sets: if $v'$ and $w'$ are non-adjacent in $G$, does $\pi(v') \neq \pi(w')$? Not necessarily. $v'$ and $w'$ could both be duplicates of the same vertex $u$ (in different batches) and non-adjacent to each other.

So the projection is injective on cliques but not necessarily on independent sets.

Now, for our problem: $H$ has $\omega(H) = 2021$ and $\alpha(H) = 2021$. The projection $\pi_H$ (from $H$'s reachability) maps every clique injectively to $V(K_{2021})$, so every clique has size $\leq 2021$. Similarly, the projection $\pi_{\overline{H}}$ (from $\overline{H}$'s reachability) maps every independent set of $H$ (clique of $\overline{H}$) injectively to $V(K_{2021})$, so every independent set has size $\leq 2021$.

Now, can we have $n > 4041$? We need a graph on $n$ vertices with $\omega = \alpha = 2021$ that is reachable (along with its complement) from $K_{2021}$.

Let me think about whether the reachability condition allows $n > 4041$.

Going back to my earlier construction: I had $H$ with $C = K_{2021}$, $U = \{u_1, \ldots, u_{2020}\}$ (independent set, each adjacent to all of $C \setminus \{c_0\}$), and $W = \{w_1, w_2, \ldots\}$ (each a duplicate of $u_1$, non-adjacent to $c_0$, all $u_j$'s, all other $w_k$'s, adjacent to all of $C \setminus \{c_0\}$).

In this $H$:
- $\omega(H) = 2021$ (the clique $C$). Can we find a larger clique? Any clique can include at most one vertex from $\{c_0\} \cup U \cup W$ (since they're pairwise non-adjacent) and at most 2020 vertices from $C \setminus \{c_0\}$... wait, a vertex from $U \cup W$ is adjacent to all of $C \setminus \{c_0\}$ but not to $c_0$. So a clique could be $\{u_j\} \cup (C \setminus \{c_0\})$ of size $1 + 2020 = 2021$. Or $C$ itself of size 2021. So $\omega(H) = 2021$. ✓

- $\alpha(H) = 1 + 2020 + |W| = 2021 + |W|$. But we need $\alpha(H) = 2021$ (since $\overline{H}$ must be reachable from $K_{2021}$, giving $\omega(\overline{H}) = 2021$, i.e., $\alpha(H) = 2021$). So $2021 + |W| \leq 2021$, meaning $|W| = 0$!

So we can't add any $w$ vertices! The independent set is already at size 2021 with just $\{c_0\} \cup U$, and adding any more vertices to the independent set would make $\alpha(H) > 2021$, violating the constraint.

But wait, maybe we can add vertices that are NOT in the independent set. Let me think about adding vertices that are adjacent to some of $U$.

Let me try a different construction. Start with $K_{2021}$ on $C$. Add $U = \{u_1, \ldots, u_{2020}\}$ as before (duplicates of $c_0$, each adjacent to all of $C \setminus \{c_0\}$, pairwise non-adjacent, non-adjacent to $c_0$). Now $I = \{c_0\} \cup U$ is an independent set of size 2021.

Now add a vertex $w$ as a duplicate of $c_1$ (where $c_1 \in C \setminus \{c_0\}$). $w$ is non-adjacent to $c_1$, and can be adjacent to any subset of $N(c_1) \setminus \{c_1\}$. In the current graph, $N(c_1) = (C \setminus \{c_1\}) \cup U$ (since $c_1$ is adjacent to all other original vertices and to all $u_j$'s). So $w$ can be adjacent to any subset of $(C \setminus \{c_1\}) \cup U$, and is non-adjacent to $c_1$.

Let's choose $w$ to be adjacent to all of $(C \setminus \{c_0, c_1\}) \cup U$ and non-adjacent to $c_0$ (we can choose this since $c_0 \in N(c_1) \setminus \{c_1\}$, so we can choose not to connect). Wait, $c_0 \in C \setminus \{c_1\}$, and $c_0 \in N(c_1)$ (since $C$ is a clique). So $c_0 \in N(c_1) \setminus \{c_1\}$, and we can choose whether $w$ is adjacent to $c_0$.

Let's say $w$ is adjacent to $c_0$ and all of $U$, and non-adjacent to $C \setminus \{c_0, c_1\}$... no, let me think about what we need.

We need $\alpha(H) \leq 2021$ and $\omega(H) \leq 2021$.

Currently (before adding $w$), $\alpha(H) = 2021$ (the set $I = \{c_0\} \cup U$) and $\omega(H) = 2021$ (the set $C$).

After adding $w$: 
- $\omega(H)$: any clique containing $w$. $w$ is non-adjacent to $c_1$. So a clique containing $w$ can include at most $C \setminus \{c_1\}$ (size 2020) plus $w$, giving 2021. Or $w$ plus some subset of $U$ (but $U$ is an independent set, so at most one from $U$). So $\omega(H) \leq 2021$. ✓ (as long as $w$ is not adjacent to too many things)

- $\alpha(H)$: any independent set containing $w$. $w$ is non-adjacent to $c_1$ and to whichever vertices we chose not to connect. If $w$ is adjacent to all of $U$, then $w$ can't be in an independent set with any $u_j$. If $w$ is adjacent to $c_0$, then $w$ can't be in an independent set with $c_0$. So the independent set containing $w$ would be $\{w, c_1\} \cup$ (some non-neighbors of $w$ among $C \setminus \{c_0, c_1\}$). 

If $w$ is adjacent to all of $C \setminus \{c_1\}$ and all of $U$, then $w$'s only non-neighbor (among existing vertices) is $c_1$. So the max independent set containing $w$ is $\{w, c_1\}$, size 2. And the max independent set not containing $w$ is still $I = \{c_0\} \cup U$, size 2021. So $\alpha(H) = 2021$. ✓

So with $w$ adjacent to all of $C \setminus \{c_1\}$ and all of $U$, and non-adjacent to $c_1$: $\omega(H) = 2021$ and $\alpha(H) = 2021$. $n = 4042$.

But is $\overline{H}$ reachable from $K_{2021}$?

$\overline{H}$: Let me figure out the structure.
- $C$ is an independent set (was clique in $H$).
- $U$ is a clique (was independent set in $H$).
- $c_0$ is adjacent to all of $U$ (was non-adjacent in $H$) and non-adjacent to $C \setminus \{c_0\}$ (was adjacent in $H$).
- $c_i$ ($i \geq 1$) is adjacent to $u_j$ iff $c_i$ was non-adjacent to $u_j$ in $H$. In $H$, all $c_i$ ($i \geq 1$) are adjacent to all $u_j$. So in $\overline{H}$, no $c_i$ ($i \geq 1$) is adjacent to any $u_j$.
- $w$ in $\overline{H}$: $w$ is adjacent to $c_1$ (non-adjacent in $H$), non-adjacent to $C \setminus \{c_1\}$ (adjacent in $H$), non-adjacent to all $u_j$ (adjacent in $H$).

So in $\overline{H}$:
- $U \cup \{c_0\}$ is a clique of size 2021. ✓ ($\omega(\overline{H}) \geq 2021$)
- $C \setminus \{c_0\}$ is an independent set of size 2020.
- $w$ is adjacent only to $c_1$ (among all other vertices). So $w$ is almost isolated.
- No edges between $U$ and $C \setminus \{c_0\}$.
- $c_0$ is adjacent to all of $U$, non-adjacent to $C \setminus \{c_0\}$ and non-adjacent to $w$.

Is $\overline{H}$ reachable from $K_{2021}$? We need $\omega(\overline{H}) = 2021$ (which we have, the clique $U \cup \{c_0\}$) and we need to build it from $K_{2021}$.

Start with $K_{2021}$ on $U \cup \{c_0\}$. We need to add $C \setminus \{c_0\} = \{c_1, \ldots, c_{2020}\}$ (independent set, non-adjacent to $c_0$ and to $U$) and $w$ (adjacent only to $c_1$).

Adding $c_1, \ldots, c_{2020}$: these form an independent set, non-adjacent to $c_0$ and to $U$. We can add them as duplicates of $c_0$ (as before): each $c_i$ is non-adjacent to $c_0$ and to all previously added $c_j$'s, and can be adjacent to any subset of $U$ (neighbors of $c_0$). We choose to connect each $c_i$ to no vertices in $U$ (since in $\overline{H}$, $c_i$ is non-adjacent to all $u_j$). ✓

Now we need to add $w$, which is adjacent only to $c_1$ (and non-adjacent to everything else). 

$w$ is non-adjacent to $c_0$, all $u_j$, and all $c_j$ ($j \geq 2$). $w$ is adjacent to $c_1$.

Can we add $w$ as a duplicate of some vertex? $w$ is adjacent to $c_1$, so $w$'s parent must have $c_1$ as a neighbor. $c_1$'s neighbors in the current graph: $c_1$ is non-adjacent to $c_0$, all $u_j$, and all $c_j$ ($j \geq 2$). So $c_1$ has NO neighbors. So $c_1$ can't be the parent (since $w$ needs to be adjacent to $c_1$, but $c_1$'s duplicates can only be adjacent to $c_1$'s neighbors, which is empty).

What about $c_0$? $c_0$'s neighbors are $U$ (all $u_j$'s). If $w$ is a duplicate of $c_0$, $w$ is non-adjacent to $c_0$ and can be adjacent to any subset of $U$. But $w$ needs to be adjacent to $c_1$, and $c_1 \notin N(c_0)$ (in the current graph, $c_1$ is non-adjacent to $c_0$). So $w$ can't be adjacent to $c_1$. ✗

What about $u_j$? $u_j$'s neighbors are $U \setminus \{u_j\}$ and $c_0$. If $w$ is a duplicate of $u_j$, $w$ is non-adjacent to $u_j$ and can be adjacent to any subset of $(U \setminus \{u_j\}) \cup \{c_0\}$. But $w$ needs to be adjacent to $c_1$, and $c_1 \notin N(u_j)$. ✗

What about $c_j$ for $j \geq 2$? $c_j$ has no neighbors (like $c_1$). ✗

So $w$ cannot be added as a single-vertex duplicate! What about multi-vertex $D$?

If $D = \{c_0, c_1\}$: $c_0$ and $c_1$ are non-adjacent in the current graph. So duplicates $c_0'$ and $c_1'$ are non-adjacent. $c_0'$ is non-adjacent to $c_0, c_1$, can be adjacent to $N(c_0) \setminus D = U$. $c_1'$ is non-adjacent to $c_0, c_1$, can be adjacent to $N(c_1) \setminus D = \emptyset$. So $c_1'$ is isolated (non-adjacent to everything). Not what we
