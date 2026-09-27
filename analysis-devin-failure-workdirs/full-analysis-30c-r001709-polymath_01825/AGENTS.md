# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   In a wagon, every $m \geq 3$ people have exactly one common friend. (When $A$ is $B$'s friend, $B$ is also $A$'s friend. No one was considered as his own friend.) Find the number of friends of the person who has the most friends.       — 题目文本
#   1. **Understanding the Problem:**
   We are given a graph where every set of \( m \geq 3 \) people has exactly one common friend. We need to find the number of friends of the person who has the most friends.

2. **Applying the Friendship Theorem:**
   The Friendship Theorem states that if every pair of people in a group has exactly one common friend, then there is one person who is friends with everyone else. This theorem can be extended to the case where every set of \( m \) people has exactly one common friend.

3. **Graph Structure:**
   According to the problem, the graph has a specific structure:
   - There are \( m-1 \) vertices \( x_1, x_2, \ldots, x_{m-1} \), each of which is connected to all other vertices.
   - Every other vertex has exactly one neighbor among \( x_1, x_2, \ldots, x_{m-1} \).

4. **Induction Hypothesis:**
   We use induction on \( m \). Assume the statement is true for all values smaller than \( m \) (for \( m \geq 3 \)).

5. **Base Case:**
   For \( m = 3 \), the graph must have a structure where there are 2 vertices \( x_1 \) and \( x_2 \) connected to all other vertices, and every other vertex has exactly one neighbor among \( x_1 \) and \( x_2 \).

6. **Inductive Step:**
   - Let \( x_1 \) be one of the vertices with maximal degree.
   - Apply the induction hypothesis for \( m-1 \) to the graph induced on the set of neighbors of \( x_1 \).
   - We find neighbors \( x_2, \ldots, x_{m-1} \) of \( x_1 \), each of which is connected to all other neighbors of \( x_1 \).
   - Because of the maximality assumption, the neighbors of \( x_i \) are the neighbors of \( x_1 \) for all \( i = 1, 2, \ldots, m-1 \).

7. **Common Neighbor Argument:**
   - Let \( x \) be a neighbor of \( x_i \) different from all the \( x_i \).
   - Since \( y, x_1, \ldots, x_{m-1} \) have exactly one common neighbor, \( x \) is connected to exactly one other neighbor of \( x_i \).
   - The graph \( G \) induced on the set formed by \( x_i \) and their neighbors has the form described above.

8. **Contradiction Argument:**
   - Suppose we can find a vertex \( y \) not in \( G \).
   - There must be at least one neighbor \( x \) of \( x_i \) different from all \( x_i \); otherwise, \( y, x_i \) can have no common friend.
   - Take such a neighbor \( x \). The vertices \( x_1, \ldots, x_{m-2}, x, y \) have exactly one common friend, and this friend can only be the unique neighbor of \( x_i \) linked to \( x \) (call it \( \bar{x} \)).
   - Repeat the procedure with \( \bar{x} \) instead of \( x \). We find that \( y \) is linked to \( x \) as well.
   - But now \( y, x_i \) have at least two common friends (\( x \) and \( \bar{x} \)), which is a contradiction.

9. **Conclusion:**
   This means that \( x_i \) and their neighbors are all the vertices in the graph, and we have what we wanted.

The final answer is \( \boxed{ m-1 } \).  — 标准解答
#   Let me analyze this problem carefully.

We have a wagon (a finite set of people) where every $m \geq 3$ people have exactly one common friend. We need to find the number of friends of the person who has the most friends.

Let me think about this. We have a graph where vertices are people and edges represent friendship. The condition is: every set of $m$ vertices has exactly one common neighbor (a vertex adjacent to all $m$ of them).

Wait, let me re-read. "Every $m \geq 3$ people have exactly one common friend." So for any subset of $m$ people, there is exactly one person who is a friend of all $m$ of them.

So the condition is: for every $m$-element subset $S$ of vertices, $|\bigcap_{v \in S} N(v)| = 1$, where $N(v)$ is the set of neighbors of $v$.

We need to find the maximum degree.

Let me think about what configurations satisfy this.

First, let's think about small cases. Let's say there are $n$ people total.

Case 1: The "star" or "wheel" type configuration. 

Actually, let me think about this more carefully. Consider a configuration where there's one "hub" person $H$ who is friends with everyone, and the other people form some structure.

If $H$ is friends with everyone, then for any $m$-subset $S$, $H$ is a common friend of $S$ (as long as $H \notin S$). But we need exactly one common friend. So if $S$ doesn't contain $H$, then $H$ is one common friend, and we need no other common friend. If $S$ contains $H$, then we need exactly one common friend of $S$.

Hmm, let me think about specific structures.

**Configuration A: Wheel graph $W_n$.** A central vertex connected to all $n-1$ rim vertices, and the rim forms a cycle. 

For a set of $m$ rim vertices: the center is a common friend. Are there others? A rim vertex $v$ is a common friend of $S$ iff $v$ is adjacent to all vertices in $S$. On the rim, $v$ is adjacent to its two cycle neighbors. So $v$ is a common friend of $S$ (among rim vertices) iff all of $S$ is contained in $N(v) \cap \text{rim} = \{v-1, v+1\}$ (cycle neighbors). So $S \subseteq \{v-1, v+1\}$, meaning $|S| \leq 2$. Since $m \geq 3$, this is impossible. So the only common friend of any $m$ rim vertices is the center. Good, exactly one.

But what if $S$ contains the center? Then we need exactly one common friend of $\{H\} \cup S'$ where $S'$ is $m-1$ rim vertices. A common friend must be adjacent to $H$ (so it's a rim vertex) and adjacent to all of $S'$. A rim vertex $v$ adjacent to all of $S'$ means $S' \subseteq N(v) \cap \text{rim} = \{v-1, v+1\}$. So $|S'| \leq 2$, meaning $m-1 \leq 2$, i.e., $m \leq 3$.

For $m = 3$: $S' = \{v-1, v+1\}$ for some $v$, and $S = \{H, v-1, v+1\}$. The common friend is $v$. Exactly one. Good.

For $m = 4$: $S' = 3$ rim vertices, need a rim vertex adjacent to all 3. But each rim vertex is adjacent to only 2 rim vertices. So no common friend exists. Bad.

So the wheel works only for $m = 3$.

For $m = 3$, the wheel graph $W_n$ (center + cycle of $n-1$) satisfies: every 3 people have exactly one common friend. The center has $n-1$ friends. But $n$ can be anything $\geq 4$. So the answer isn't determined for $m = 3$? 

Wait, but the problem says "find the number of friends of the person who has the most friends." This suggests the answer is a specific number, presumably depending on $m$.

Hmm, let me reconsider. Maybe the problem is asking for the answer in terms of $m$, and it should be the same for all valid configurations.

Wait, for the wheel with $m=3$, the max degree is $n-1$ which varies. So either the wheel doesn't satisfy the condition for all triples, or I'm missing something.

Let me recheck the wheel for $m = 3$ more carefully. Take 3 rim vertices that are not consecutive, say vertices 1, 3, 5 on a cycle of length $\geq 6$. Their common friends: the center is adjacent to all of them. Is any rim vertex adjacent to all of 1, 3, 5? A rim vertex $v$ is adjacent to $v-1$ and $v+1$ on the rim. For $v$ to be adjacent to 1, 3, and 5, we'd need $\{1,3,5\} \subseteq \{v-1, v+1\}$, impossible since $|S|=3 > 2$. So only the center. Good.

Take 3 consecutive rim vertices 1, 2, 3. Common friends: center (adjacent to all). Rim vertex 2 is adjacent to 1 and 3 (its neighbors) but is 2 adjacent to 2? No, no self-loops. So 2 is not a common friend of {1,2,3} since 2 is not its own friend. What about rim vertex adjacent to 1, 2, 3? Vertex 2 is adjacent to 1 and 3 but not to itself. So no. Only the center. Good.

Take {center, 1, 2}. Common friends: must be adjacent to center (so a rim vertex), to 1, and to 2. Rim vertex adjacent to both 1 and 2: vertex 2 is adjacent to 1 (yes, neighbor on cycle) and to 2 (no). Vertex 1 is adjacent to 2 (yes) and to 1 (no). So we need a rim vertex $v$ with $1, 2 \in \{v-1, v+1\}$. That means $v$ is adjacent to both 1 and 2 on the cycle. If the cycle is $...1, 2, 3...$, then vertex 2 is adjacent to 1 and 3, not to 2. Vertex 1 is adjacent to 0 and 2. So vertex 1 is adjacent to 2 but not to 1. Hmm, we need $v$ adjacent to both 1 and 2. $v=1$: adjacent to 2? yes. adjacent to 1? no. $v=2$: adjacent to 1? yes. adjacent to 2? no. $v=0$: adjacent to 1? yes. adjacent to 2? Only if 0 and 2 are cycle-neighbors, which they're not (0 is adjacent to $n-1$ and 1). So no rim vertex is adjacent to both 1 and 2... wait, that can't be right. On a cycle, vertices 1 and 2 are adjacent. A common neighbor of 1 and 2 on the cycle would be a vertex adjacent to both. 1's neighbors on cycle: $n-1, 2$ (wait, no, let me use 0-indexed). 

Let me use a cycle $0, 1, 2, \ldots, k-1$ where $k = n-1$. Neighbors of $i$ on cycle: $(i-1) \bmod k$ and $(i+1) \bmod k$. Plus the center.

Take $S = \{\text{center}, 0, 1\}$. Common friend must be adjacent to center, 0, and 1. Adjacent to center means it's a rim vertex. Adjacent to 0 and 1: vertex $v$ with $0 \in \{v-1, v+1\}$ and $1 \in \{v-1, v+1\} \pmod{k}$. So $v \in \{1, k-1\}$ (adjacent to 0) and $v \in \{0, 2\}$ (adjacent to 1). Intersection: need $v$ in both sets. $\{1, k-1\} \cap \{0, 2\}$. If $k = 3$: $\{1, 2\} \cap \{0, 2\} = \{2\}$. So $v = 2$. If $k \geq 4$: $\{1, k-1\} \cap \{0, 2\} = \emptyset$ (since $k-1 \geq 3 \neq 0, 2$). 

So for $k \geq 4$ (i.e., $n \geq 5$), the triple $\{\text{center}, 0, 1\}$ has only the center as... wait, the center is in $S$, so the center can't be a common friend of itself. So we need a common friend outside $S$. For $k \geq 4$, there's no common friend. That violates the condition!

So the wheel graph only works when $k = 3$, i.e., $n = 4$: the complete graph $K_4$ minus... no, $W_4$ is the center plus a triangle. That's $K_4$! In $K_4$, every 3 vertices have exactly one common friend (the 4th vertex). The max degree is 3.

Hmm wait, $K_4$: 4 vertices, each pair connected. Any 3 vertices: the common friends are vertices adjacent to all 3. The 4th vertex is adjacent to all 3. Any of the 3 vertices themselves? No, a vertex isn't adjacent to itself. So exactly one common friend. Max degree = 3. And $m = 3$.

But can we have other configurations for $m = 3$? Let me think...

Actually, let me reconsider the problem. Maybe the answer is $m$ for all valid $m$.

Let me think about $m = 3$ more carefully. Is $K_4$ the only configuration?

Consider the Petersen graph or other structures... Actually, let me think about this differently.

Let me think about what graphs satisfy: every $m$ vertices have exactly one common neighbor.

**Key insight:** Consider the "friendship graph" / windmill graph. The friendship theorem states: if every pair of vertices has exactly one common neighbor, then there's a vertex adjacent to all others (the "universal friend"). 

Our condition is different: every $m$ vertices have exactly one common neighbor.

Let me think about generalizing. 

Actually, let me think about the complete graph $K_{m+1}$. In $K_{m+1}$, any $m$ vertices have exactly one common neighbor (the remaining vertex). The max degree is $m$. 

Can we do better? Can we have a graph on more than $m+1$ vertices satisfying this?

Let me think about $m = 3$. $K_4$ works with max degree 3. Can we have a graph on 5+ vertices where every 3 vertices have exactly one common neighbor?

Let me try to construct one. Suppose we have vertices $1, 2, 3, 4, 5$. 

Every triple must have exactly one common neighbor. There are $\binom{5}{3} = 10$ triples.

Consider the "windmill"/friendship graph $F_k$: $k$ triangles sharing a common vertex. The universal vertex $u$ is connected to all $2k$ other vertices, and the other vertices are paired up: $a_i, b_i$ with edge $a_i b_i$, and both connected to $u$. So $n = 2k+1$.

In this graph, every pair has exactly one common neighbor (friendship theorem). What about every triple?

Take triple $\{a_i, b_i, a_j\}$ where $i \neq j$. Common neighbors: $u$ is adjacent to all three. $a_i$'s neighbors: $u, b_i$. $b_i$'s neighbors: $u, a_i$. $a_j$'s neighbors: $u, b_j$. Common: $u$. Is there another? $b_j$ is adjacent to $a_j$ and $u$, but not to $a_i$ or $b_i$. So only $u$. Good, exactly one.

Take triple $\{a_i, a_j, a_k\}$ (all from different pairs, $i, j, k$ distinct). Common neighbors: $u$ is adjacent to all. $a_i$'s neighbors: $u, b_i$. $a_j$'s neighbors: $u, b_j$. $a_k$'s neighbors: $u, b_k$. Common: just $u$. Good.

Take triple $\{u, a_i, b_i\}$. Common neighbors: must be adjacent to $u$, $a_i$, $b_i$. Adjacent to $u$: all other vertices. Adjacent to $a_i$: $u, b_i$. Adjacent to $b_i$: $u, a_i$. Common: need adjacent to $u$, $a_i$, $b_i$, and not in the triple. $b_i$ is adjacent to $u$ and $a_i$ but not to $b_i$ (itself). $a_i$ is adjacent to $u$ and $b_i$ but not to $a_i$ (itself). So no vertex outside the triple is adjacent to all three. Wait, that means zero common friends. Bad!

So the friendship graph doesn't work for $m = 3$.

Hmm. So $K_4$ might be the only option for $m = 3$? Let me think more carefully.

Actually, let me think about this more generally. Let me consider the problem from a design theory perspective.

The condition is: for every $m$-subset $S$, $|\bigcap_{v \in S} N(v)| = 1$.

Let $n$ be the total number of vertices. For each vertex $v$, let $d(v) = |N(v)|$ be its degree.

Consider the dual perspective. For each vertex $w$, let $F(w) = \{v : w \in N(v)\} = N(w)$ (since the graph is undirected). So $F(w) = N(w)$ is the set of friends of $w$, which is also the set of vertices that have $w$ as a friend.

The condition says: for every $m$-subset $S$ of vertices, there is exactly one $w$ with $S \subseteq N(w)$.

This is like a covering/packing condition. Think of it as: the collection $\{N(w) : w \in V\}$ is a family of subsets of $V$ such that every $m$-subset of $V$ is contained in exactly one member of the family.

But wait, $w \notin N(w)$ (no self-friendship), so $N(w) \subseteq V \setminus \{w\}$.

So we have a family of subsets $\mathcal{F} = \{N(w) : w \in V\}$ of $V$, where $N(w) \subseteq V \setminus \{w\}$, and every $m$-subset of $V$ is contained in exactly one $N(w)$.

This is related to a combinatorial design. Specifically, this is like a "covering" where every $m$-subset is covered exactly once.

If we think of the $N(w)$ as "blocks" and we want every $m$-subset to be in exactly one block, this is a Steiner system $S(m, k, n)$ where the blocks have varying sizes... no, Steiner systems have constant block size. Here the block sizes can vary.

But actually, the condition is that every $m$-subset is in exactly one block. If all blocks have the same size $k$, this would be a Steiner system $S(m, k, n)$.

But here, the blocks have varying sizes (the degrees vary), and additionally, block $N(w)$ doesn't contain $w$.

Let me count. The number of $m$-subsets is $\binom{n}{m}$. Each block $N(w)$ of size $d(w)$ covers $\binom{d(w)}{m}$ $m$-subsets. So:

$$\sum_{w \in V} \binom{d(w)}{m} = \binom{n}{m}$$

Also, for any $(m-1)$-subset $T$, the number of blocks containing $T$ is the number of common friends of $T$. Let's call this $\lambda(T)$. Then:

$$\sum_{w: T \subseteq N(w)} \binom{d(w) - (m-1)}{1} = \sum_{w: T \subseteq N(w)} (d(w) - m + 1)$$

Hmm, this is getting complicated. Let me think differently.

For any $(m-1)$-subset $T$, and any vertex $v \notin T$, the $m$-subset $T \cup \{v\}$ has exactly one common friend, say $w$. This $w$ is a common friend of $T$ and also a friend of $v$. So $w \in \bigcap_{t \in T} N(t) \cap N(v)$.

Actually, let me think about it this way. For any $(m-1)$-subset $T$, let $C(T) = \bigcap_{t \in T} N(t)$ be the set of common friends of $T$. For each $v \notin T$, $T \cup \{v\}$ has exactly one common friend, which is in $C(T) \cap N(v) \setminus (T \cup \{v\})$... wait, actually the common friend of $T \cup \{v\}$ is in $\bigcap_{t \in T} N(t) \cap N(v) = C(T) \cap N(v)$. And it's not in $T \cup \{v\}$ (since no one is their own friend, and the common friend must be a friend of everyone in the set, so it can't be in the set itself... actually, can it? If $w \in T \cup \{v\}$, then $w$ must be a friend of itself, which is impossible. So the common friend is not in $T \cup \{v\}$.)

So for each $v \notin T$, $|C(T) \cap N(v) \setminus (T \cup \{v\})| = 1$. But actually $C(T)$ already excludes elements of $T$ (since $C(T) = \bigcap_{t \in T} N(t)$ and $t \notin N(t)$, so $t \notin C(T)$). And $v \notin C(T)$ iff $v \notin N(t)$ for some $t \in T$... actually $v$ could be in $C(T)$. Let me be more careful.

$C(T) = \bigcap_{t \in T} N(t)$. This is the set of vertices adjacent to all of $T$. Note that elements of $T$ are not in $C(T)$ (since $t \notin N(t)$). But $v \notin T$ could be in $C(T)$.

For $v \notin T$, the common friend of $T \cup \{v\}$ is the unique element of $C(T) \cap N(v) \setminus \{v\}$ (we need it to not be $v$ itself, since $v \notin N(v)$, so actually $v \notin N(v)$ means $v \notin C(T) \cap N(v)$ automatically... wait, $v \in C(T)$ means $v$ is adjacent to all of $T$, and $v \in N(v)$ is impossible. So $v \notin N(v)$, hence $v \notin C(T) \cap N(v)$. So the common friend of $T \cup \{v\}$ is the unique element of $C(T) \cap N(v)$.)

So for each $v \notin T$, $|C(T) \cap N(v)| = 1$.

Now, this means: the sets $\{N(v) \cap C(T) : v \notin T\}$ each have exactly one element, and moreover, these elements partition... no, different $v$'s could map to the same common friend.

Actually, let me think of it as: $C(T)$ is a set, and for each $v \notin T$, $v$ is adjacent to exactly one element of $C(T)$. Also, elements of $C(T)$: for $w \in C(T)$, $w$ is adjacent to all of $T$, and $w$'s neighbors among $V \setminus T$ include those $v$ for which $w$ is the common friend of $T \cup \{v\}$.

Let $C(T) = \{c_1, c_2, \ldots, c_r\}$. Each $v \notin T$ is adjacent to exactly one $c_i$. So the $c_i$'s partition $V \setminus T$ into groups based on which $c_i$ they're adjacent to (within $C(T)$). But wait, $v$ could be adjacent to $c_i$ and also to other vertices, but the condition is only about adjacency to $C(T)$.

Actually, let me reconsider. For $v \notin T$, $|N(v) \cap C(T)| = 1$. This means each $v \notin T$ has exactly one neighbor in $C(T)$.

Now, what about elements of $C(T)$ themselves? If $c_i \in C(T)$, is $c_i \notin T$ (yes, since $C(T) \cap T = \emptyset$). So $c_i$ also has exactly one neighbor in $C(T)$. So within $C(T)$, each element has exactly one neighbor in $C(T)$. This means the induced subgraph on $C(T)$ is a perfect matching (each vertex has degree exactly 1 within $C(T)$). So $|C(T)| = r$ is even, and the induced subgraph is a matching.

Hmm, interesting. But also, each $c_i \in C(T)$ is adjacent to all of $T$ (by definition of $C(T)$). And each $c_i$ has exactly one neighbor in $C(T)$.

Now, the vertices in $V \setminus T \setminus C(T)$: each is adjacent to exactly one element of $C(T)$.

So the vertices of $C(T)$ partition $V \setminus T$ into "groups": $c_i$ is adjacent to some set of vertices in $V \setminus T$, and each vertex in $V \setminus T$ is adjacent to exactly one $c_i$. But $c_i$ is also in $V \setminus T$, and $c_i$ is adjacent to exactly one other $c_j$ in $C(T)$.

Let me define $A_i = \{v \notin T : v \text{ is adjacent to } c_i\} \setminus \{c_i\}$... hmm, this is getting complicated. Let me try a different approach.

Let me try to think about what happens when $T$ is an $(m-1)$-subset and consider the structure.

Actually, let me try small cases computationally (in my head) to get intuition.

**$m = 3$, $n = 4$: $K_4$.** Max degree 3. ✓

**$m = 3$, $n = 5$:** Is there a graph on 5 vertices where every 3 vertices have exactly one common neighbor?

Let the vertices be $1, 2, 3, 4, 5$. We need $\sum \binom{d_i}{3} = \binom{5}{3} = 10$.

Possible degree sequences (with $\sum \binom{d_i}{3} = 10$):
- All degrees 4: $5 \cdot \binom{4}{3} = 5 \cdot 4 = 20 \neq 10$. No.
- Degrees $(4, 4, 4, 4, 0)$: $4 \cdot 4 = 16 \neq 10$. No.
- Degrees $(4, 4, 3, 3, ?)$: $\binom{4}{3} + \binom{4}{3} + \binom{3}{3} + \binom{3}{3} = 4 + 4 + 1 + 1 = 10$. Need 5th vertex degree $d_5$ with $\binom{d_5}{3} = 0$, so $d_5 \leq 2$. Sum of degrees = $4 + 4 + 3 + 3 + d_5 = 14 + d_5$, must be even, so $d_5$ even. $d_5 \in \{0, 2\}$.

If $d_5 = 0$: vertex 5 is isolated. Then any triple containing 5 has no common friend (since 5 has no friends, no one is a friend of 5... wait, common friend of $\{5, a, b\}$ must be adjacent to 5, but 5 has no neighbors). So no common friend. Violates condition. So $d_5 \neq 0$.

If $d_5 = 2$: degrees $(4, 4, 3, 3, 2)$. Sum = 16, even. ✓ But vertex with degree 4 on 5 vertices means adjacent to all others. So vertices 1 and 2 (degree 4) are adjacent to all. Then for any triple $S$ not containing 1 or 2, both 1 and 2 are common friends, giving 2 common friends. But we need exactly 1. So this doesn't work unless every triple contains 1 or 2. With 5 vertices, triple $\{3, 4, 5\}$ doesn't contain 1 or 2. So 2 common friends. Violation.

So no graph on 5 vertices works for $m = 3$.

Let me check $n = 6, m = 3$. $\sum \binom{d_i}{3} = \binom{6}{3} = 20$.

Hmm, this is getting complex. Let me think about it more structurally.

Actually, let me reconsider. Maybe the answer is always $m$, achieved by $K_{m+1}$.

Let me check: is $K_{m+1}$ the unique solution? Or are there others?

For $K_{m+1}$: $n = m+1$, every vertex has degree $m$, every $m$-subset has exactly one common friend (the remaining vertex). Max degree = $m$.

Can we have $n > m+1$? Let me think about $m = 3$ and try $n = 6$ or higher.

Actually, let me think about this more carefully using the structure I derived.

For any $(m-1)$-subset $T$, $C(T) = \bigcap_{t \in T} N(t)$ has the property that the induced subgraph on $C(T)$ is a perfect matching, and every vertex in $V \setminus T$ has exactly one neighbor in $C(T)$.

For $m = 3$, $T$ is a pair $\{a, b\}$. $C(\{a,b\})$ is the set of common friends of $a$ and $b$. By the condition, for every $v \notin \{a, b\}$, $v$ has exactly one neighbor in $C(\{a,b\})$. And the induced subgraph on $C(\{a,b\})$ is a perfect matching.

Now, $|C(\{a,b\})| = $ number of common friends of $a$ and $b$. In $K_4$, $|C(\{a,b\})| = 2$ (the other two vertices), and they form a matching (they're adjacent to each other). ✓

Can we have $|C(\{a,b\})| = 4$ for some pair? Then $C(\{a,b\})$ is a matching of size 2 (4 vertices, 2 edges). And every other vertex has exactly one neighbor in $C(\{a,b\})$.

Let me try to build a graph with $m = 3$ and $n > 4$.

Let me try $n = 6$. Consider vertices $1, 2, 3, 4, 5, 6$.

$\sum \binom{d_i}{3} = \binom{6}{3} = 20$.

One possibility: all degrees equal to $d$. Then $6 \binom{d}{3} = 20$, so $\binom{d}{3} = 20/6$, not integer. So not regular.

Another: degrees $(5, 5, 4, 4, 4, 4)$: $2 \cdot 10 + 4 \cdot 4 = 20 + 16 = 36 \neq 20$.

Degrees $(5, 4, 4, 4, 4, 3)$: $10 + 4 \cdot 4 + 1 = 10 + 16 + 1 = 27 \neq 20$.

Degrees $(4, 4, 4, 4, 4, 4)$: $6 \cdot 4 = 24 \neq 20$.

Degrees $(5, 5, 5, 5, 0, 0)$: $4 \cdot 10 = 40 \neq 20$. And isolated vertices cause problems.

Degrees $(4, 4, 4, 4, 4, 0)$: $5 \cdot 4 = 20$. ✓ But vertex 6 isolated → triples containing 6 have no common friend. ✗

Degrees $(4, 4, 4, 4, 3, 3)$: $4 \cdot 4 + 2 \cdot 1 = 18 \neq 20$.

Degrees $(5, 4, 4, 4, 4, 1)$: $10 + 4 \cdot 4 + 0 = 26 \neq 20$.

Degrees $(5, 5, 4, 4, 2, 0)$: $10 + 10 + 4 + 4 + 0 + 0 = 28 \neq 20$.

Degrees $(5, 5, 3, 3, 3, 3)$: $10 + 10 + 4 \cdot 1 = 24 \neq 20$.

Degrees $(5, 3, 3, 3, 3, 3)$: $10 + 5 \cdot 1 = 15 \neq 20$.

Degrees $(5, 5, 5, 3, 2, 0)$: $30 + 1 = 31 \neq 20$.

Hmm, let me be more systematic. We need $\sum \binom{d_i}{3} = 20$ with $0 \leq d_i \leq 5$ and $\sum d_i$ even.

$\binom{d}{3}$ for $d = 0, 1, 2, 3, 4, 5$: $0, 0, 0, 1, 4, 10$.

We need 6 values from $\{0, 0, 0, 1, 4, 10\}$ summing to 20, with corresponding $d$ values summing to even.

Options:
- $10 + 10 + 0 + 0 + 0 + 0 = 20$: degrees $(5, 5, ?, ?, ?, ?)$ with four degrees $\leq 2$. Sum of degrees $\geq 10$, need even. E.g., $(5, 5, 2, 2, 2, 2)$: sum = 18, even. ✓ But two vertices of degree 5 (adjacent to all) means every triple has at least 2 common friends (both degree-5 vertices). ✗ (Unless the triple contains both, but even then...) Actually if both are in the triple, they need a common friend adjacent to both, which could be unique. But a triple not containing either has 2 common friends. ✗

- $10 + 4 + 4 + 1 + 1 + 0 = 20$: degrees $(5, 4, 4, 3, 3, \leq 2)$. Sum = $5 + 4 + 4 + 3 + 3 + d_6 = 19 + d_6$, need even, so $d_6$ odd. $d_6 \in \{1\}$ (since $\leq 2$ and odd). Sum = 20. ✓ But vertex with degree 5 is adjacent to all. Any triple not containing this vertex has it as a common friend. Need exactly one, so no other common friend. The degree-1 vertex has one friend. If a triple contains the degree-1 vertex, the common friend must be adjacent to it, so must be its unique friend. This is very restrictive.

Let me check: vertex 6 has degree 1, say adjacent to vertex 1. Vertex 1 has degree 5, adjacent to all. Triple $\{6, 2, 3\}$: common friend must be adjacent to 6 (so must be vertex 1), to 2, and to 3. Vertex 1 is adjacent to all, so it's a common friend. Is there another? Any other common friend must be adjacent to 6, but 6's only friend is 1. So only vertex 1. ✓

Triple $\{6, 1, 2\}$: common friend adjacent to 6 (must be 1), but 1 is in the triple. So no common friend from vertex 1's side... wait, the common friend must be adjacent to 6, 1, and 2. Adjacent to 6 means it's vertex 1. But 1 is in the triple, and 1 is not adjacent to itself. So no common friend. ✗!

So this doesn't work. The degree-1 vertex causes problems when it's in a triple with its only friend.

So any vertex with degree $< m-1 = 2$ causes problems? If a vertex $v$ has degree $d(v) < m-1$, then we can find an $(m-1)$-subset of $V \setminus \{v\}$ that doesn't include any friend of $v$... actually, we need to be more careful.

If $v$ has degree $d$ and $d < m-1$: take $T = \{v\} \cup S$ where $S$ is an $(m-1)$-subset of $V \setminus (\{v\} \cup N(v))$. This requires $|V \setminus (\{v\} \cup N(v))| \geq m-1$, i.e., $n - 1 - d \geq m - 1$, i.e., $n \geq m + d$. If this holds, then the common friend of $T$ must be adjacent to $v$, but also adjacent to all of $S$, none of which are friends of $v$. The common friend is in $N(v) \cap \bigcap_{s \in S} N(s)$. This could be non-empty. Hmm, this doesn't immediately give a contradiction.

Actually, the issue is more subtle. Let me think about it differently.

Let me go back to the structural result. For any $(m-1)$-subset $T$, $C(T)$ is a perfect matching, and every $v \notin T$ has exactly one neighbor in $C(T)$.

For $m = 3$, $|T| = 2$. Take $T = \{a, b\}$. $C(T)$ is a perfect matching. Every vertex not in $T$ has exactly one neighbor in $C(T)$.

In $K_4$ with vertices $\{1, 2, 3, 4\}$: $T = \{1, 2\}$, $C(T) = \{3, 4\}$, which is a matching (edge 3-4). Every vertex not in $T$ (i.e., 3, 4) has exactly one neighbor in $C(T)$: 3 is adjacent to 4, 4 is adjacent to 3. ✓

Now suppose $n = 6$ and we try to build such a graph. Take $T = \{1, 2\}$. $C(T) = \{c_1, c_2, c_3, c_4\}$ (must be even, perfect matching). Say matching is $(c_1, c_2), (c_3, c_4)$. Every vertex in $V \setminus \{1, 2\}$ has exactly one neighbor in $C(T)$.

The vertices in $V \setminus \{1, 2\}$ are $\{c_1, c_2, c_3, c_4, v_5\}$ where $v_5$ is the 5th vertex (if $n = 6$, vertices are $1, 2, c_1, c_2, c_3, c_4$... wait that's already 6). So $n = 6$ means $V = \{1, 2, c_1, c_2, c_3, c_4\}$, and $C(T) = \{c_1, c_2, c_3, c_4\}$, $|C(T)| = 4$.

Each $c_i$ has exactly one neighbor in $C(T)$ (the matching partner). Also, each $c_i$ is adjacent to both 1 and 2 (since $c_i \in C(\{1,2\})$).

So $c_1$ is adjacent to: $1, 2, c_2$ (and possibly others, but within $C(T)$ only $c_2$). So $d(c_1) \geq 3$.

Now consider $T' = \{c_1, c_2\}$. They are adjacent (matching partner). $C(T') = $ common friends of $c_1$ and $c_2$. $c_1$ is adjacent to $1, 2, c_2$ (at least). $c_2$ is adjacent to $1, 2, c_1$ (at least). So $1, 2 \in C(T')$. Also, are there others? $c_3, c_4$ are adjacent to each other but are they adjacent to $c_1$ and $c_2$? Within $C(T)$, $c_3$ is only adjacent to $c_4$ (matching). So $c_3$ is not adjacent to $c_1$ or $c_2$ (within $C(T)$, each vertex has exactly one neighbor). So $c_3 \notin C(T')$ and $c_4 \notin C(T')$. So $C(T') \supseteq \{1, 2\}$ and $|C(T')|$ is even (perfect matching). So $|C(T')| \in \{2, 4, \ldots\}$.

If $|C(T')| = 2$, then $C(T') = \{1, 2\}$, and $\{1, 2\}$ must be a matching, i.e., 1 and 2 are adjacent. 

If $|C(T')| = 4$, then there are 2 more common friends, but we said $c_3, c_4 \notin C(T')$. So the only vertices are $\{1, 2, c_1, c_2, c_3, c_4\}$, and $c_1, c_2 \notin C(T')$ (they're in $T'$). So $C(T') \subseteq \{1, 2, c_3, c_4\}$. We need $c_3, c_4$ to be common friends of $c_1, c_2$, meaning $c_3$ adjacent to both $c_1$ and $c_2$. But $c_3$'s only neighbor in $C(T)$ is $c_4$. So $c_3$ is not adjacent to $c_1$ or $c_2$. So $c_3 \notin C(T')$. Similarly $c_4 \notin C(T')$. So $C(T') = \{1, 2\}$, $|C(T')| = 2$. ✓ (matching requires 1-2 edge).

So 1 and 2 must be adjacent. Good.

Now, $C(T') = \{1, 2\}$, and every vertex not in $T' = \{c_1, c_2\}$ has exactly one neighbor in $\{1, 2\}$. The vertices not in $T'$ are $\{1, 2, c_3, c_4\}$. 
- 1's neighbors in $\{1, 2\}$: 1 is not adjacent to itself, so must be adjacent to 2. ✓ (we just established 1-2 edge).
- 2's neighbors in $\{1, 2\}$: adjacent to 1. ✓
- $c_3$'s neighbor in $\{1, 2\}$: exactly one of 1, 2.
- $c_4$'s neighbor in $\{1, 2\}$: exactly one of 1, 2.

Now, recall $c_3, c_4 \in C(\{1, 2\})$, so they're adjacent to both 1 and 2. But we just said $c_3$ has exactly one neighbor in $\{1, 2\}$. Contradiction! $c_3$ is adjacent to both 1 and 2 (since $c_3 \in C(\{1,2\})$), but must have exactly one neighbor in $\{1, 2\}$ (from $C(T')$ condition). 

So $|C(T)| = 4$ with $n = 6$ leads to a contradiction. So $|C(T)| \neq 4$ when $n = 6$.

What about $|C(T)| = 2$? Then $C(\{1,2\}) = \{c_1, c_2\}$, and $V = \{1, 2, c_1, c_2, v_5, v_6\}$. Every vertex not in $\{1, 2\}$ has exactly one neighbor in $\{c_1, c_2\}$. 

$c_1, c_2$ are adjacent to each other (matching) and to both 1 and 2. So $d(c_1) \geq 3$, $d(c_2) \geq 3$.

$v_5$ has exactly one neighbor in $\{c_1, c_2\}$, say $c_1$. $v_6$ has exactly one neighbor in $\{c_1, c_2\}$, say $c_2$ (or $c_1$).

Now consider $T'' = \{c_1, c_2\}$. $C(T'') \supseteq \{1, 2\}$ (since both are adjacent to $c_1$ and $c_2$). $|C(T'')|$ is even. $C(T'') \subseteq V \setminus \{c_1, c_2\} = \{1, 2, v_5, v_6\}$. 

$v_5$ is adjacent to $c_1$ (by assumption) but is $v_5$ adjacent to $c_2$? $v_5$ has exactly one neighbor in $\{c_1, c_2\}$, which is $c_1$. So $v_5$ is not adjacent to $c_2$. So $v_5 \notin C(T'')$. Similarly, if $v_6$'s neighbor in $\{c_1, c_2\}$ is $c_2$, then $v_6$ is not adjacent to $c_1$, so $v_6 \notin C(T'')$. If $v_6$'s neighbor is $c_1$, then $v_6$ is not adjacent to $c_2$, so $v_6 \notin C(T'')$.

So $C(T'') = \{1, 2\}$, $|C(T'')| = 2$. ✓ Matching: 1-2 edge required. So 1 and 2 are adjacent.

Every vertex not in $\{c_1, c_2\}$ has exactly one neighbor in $\{1, 2\}$. Vertices: $\{1, 2, v_5, v_6\}$.
- 1: adjacent to 2 (✓, one neighbor in $\{1,2\}$, which is 2).
- 2: adjacent to 1 (✓).
- $v_5$: exactly one neighbor in $\{1, 2\}$.
- $v_6$: exactly one neighbor in $\{1, 2\}$.

But $v_5$ is not adjacent to 1 or 2? We know $v_5$ is adjacent to $c_1$ (its neighbor in $C(\{1,2\})$). Is $v_5$ adjacent to 1 or 2? $v_5 \notin C(\{1,2\})$ means $v_5$ is not a common friend of 1 and 2, so $v_5$ is not adjacent to at least one of 1, 2. But $v_5$ could be adjacent to one of them.

From $C(T'')$: $v_5$ has exactly one neighbor in $\{1, 2\}$. So $v_5$ is adjacent to exactly one of 1, 2. Say $v_5$ is adjacent to 1 but not 2 (or vice versa).

Similarly $v_6$ is adjacent to exactly one of 1, 2.

Now let's think about what the graph looks like so far:
- 1-2 edge
- $c_1$-$c_2$ edge
- $c_1$ adjacent to 1, 2
- $c_2$ adjacent to 1, 2
- $v_5$ adjacent to $c_1$ (and exactly one of 1, 2)
- $v_6$ adjacent to exactly one of $c_1, c_2$ (and exactly one of 1, 2)

Let me also consider $T = \{1, c_1\}$. $C(\{1, c_1\})$ = common friends of 1 and $c_1$. 1 is adjacent to: 2, $c_1$, $c_2$ (at least), and possibly $v_5, v_6$. $c_1$ is adjacent to: 1, 2, $c_2$ (at least), and possibly $v_5, v_6$.

Common friends of 1 and $c_1$: vertices adjacent to both. 2 is adjacent to 1 (yes) and $c_1$ (yes). $c_2$ is adjacent to 1 (yes) and $c_1$ (yes). So $C(\{1, c_1\}) \supseteq \{2, c_2\}$. 

$|C(\{1, c_1\})|$ is even. $C(\{1, c_1\}) \subseteq V \setminus \{1, c_1\} = \{2, c_2, v_5, v_6\}$.

Is $v_5 \in C(\{1, c_1\})$? $v_5$ is adjacent to $c_1$ (yes). Is $v_5$ adjacent to 1? Depends on our choice. If $v_5$ is adjacent to 1, then $v_5 \in C(\{1, c_1\})$. If not, then $v_5 \notin C(\{1, c_1\})$.

Case A: $v_5$ adjacent to 1. Then $v_5 \in C(\{1, c_1\})$, so $C(\{1, c_1\}) \supseteq \{2, c_2, v_5\}$. But $|C|$ must be even, so $|C| \geq 4$, meaning $v_6 \in C$ too. So $v_6$ adjacent to both 1 and $c_1$. 

But $v_6$'s neighbor in $\{c_1, c_2\}$: if $v_6$ is adjacent to $c_1$, then $v_6$'s neighbor in $\{c_1, c_2\}$ is $c_1$ (exactly one). And $v_6$ adjacent to 1. So $v_6 \in C(\{1, c_1\})$. Then $C(\{1, c_1\}) = \{2, c_2, v_5, v_6\}$, $|C| = 4$. Matching: $(2, c_2)$ and $(v_5, v_6)$ must be edges. So 2-$c_2$ edge and $v_5$-$v_6$ edge.

Also, every vertex not in $\{1, c_1\}$ has exactly one neighbor in $C = \{2, c_2, v_5, v_6\}$. Vertices not in $\{1, c_1\}$: $\{2, c_2, v_5, v_6\}$ (these are the elements of $C$ themselves). Each has exactly one neighbor in $C$ (the matching partner). ✓ (2's neighbor is $c_2$, $c_2$'s neighbor is 2, $v_5$'s neighbor is $v_6$, $v_6$'s neighbor is $v_5$.) ✓

Now, $v_6$ is adjacent to $c_1$ (its neighbor in $\{c_1, c_2\}$). But wait, we said $v_6$'s neighbor in $\{c_1, c_2\}$ is exactly one. If $v_6$ is adjacent to $c_1$, then $v_6$ is not adjacent to $c_2$. Let's check: is $v_6$ adjacent to $c_2$? $v_6 \in C(\{1, c_1\})$ means $v_6$ is adjacent to 1 and $c_1$. $v_6$'s neighbor in $\{c_1, c_2\}$ is $c_1$ (exactly one), so $v_6$ not adjacent to $c_2$. ✓

Now let's also check $v_5$'s neighbor in $\{c_1, c_2\}$: $v_5$ is adjacent to $c_1$ (yes), not to $c_2$ (since exactly one neighbor in $\{c_1, c_2\}$). ✓

Now, $v_5$ is adjacent to 1 (by assumption in Case A). $v_5$'s neighbor in $\{1, 2\}$: exactly one, which is 1. So $v_5$ not adjacent to 2. ✓

$v_6$'s neighbor in $\{1, 2\}$: exactly one. $v_6$ is adjacent to 1 (established). So $v_6$ not adjacent to 2. ✓

Now let me also check $T = \{2, c_1\}$. $C(\{2, c_1\})$ = common friends of 2 and $c_1$. 2 is adjacent to 1, $c_1$, $c_2$ (at least). $c_1$ is adjacent to 1, 2, $c_2$ (at least). Common: 1 (adj to 2 ✓, adj to $c_1$ ✓), $c_2$ (adj to 2 ✓, adj to $c_1$ ✓). So $C \supseteq \{1, c_2\}$. 

Is $v_5 \in C(\{2, c_1\})$? $v_5$ adjacent to $c_1$ (yes), $v_5$ adjacent to 2? No (established). So $v_5 \notin C$. 

Is $v_6 \in C(\{2, c_1\})$? $v_6$ adjacent to $c_1$ (yes), $v_6$ adjacent to 2? No (established). So $v_6 \notin C$.

So $C(\{2, c_1\}) = \{1, c_2\}$, $|C| = 2$. ✓ Matching: 1-$c_2$ edge required. So 1 is adjacent to $c_2$. We already knew that ($c_2 \in C(\{1,2\})$ means $c_2$ adjacent to 1). ✓

Every vertex not in $\{2, c_1\}$ has exactly one neighbor in $\{1, c_2\}$. Vertices: $\{1, c_2, v_5, v_6\}$.
- 1: neighbor in $\{1, c_2\}$ is $c_2$ (1 not adj to itself). ✓ (1-$c_2$ edge exists)
- $c_2$: neighbor in $\{1, c_2\}$ is 1. ✓
- $v_5$: exactly one neighbor in $\{1, c_2\}$. $v_5$ adjacent to 1 (yes). $v_5$ adjacent to $c_2$? We need to check. $v_5$'s neighbors so far: $c_1$, 1, $v_6$. Is $v_5$ adjacent to $c_2$? If yes, then $v_5$ has 2 neighbors in $\{1, c_2\}$, violating the condition. If no, then $v_5$ has 1 neighbor in $\{1, c_2\}$ (which is 1). ✓ So $v_5$ not adjacent to $c_2$.
- $v_6$: exactly one neighbor in $\{1, c_2\}$. $v_6$ adjacent to 1 (yes). $v_6$ adjacent to $c_2$? If yes, 2 neighbors, bad. If no, 1 neighbor (1). ✓ So $v_6$ not adjacent to $c_2$.

Good. Now let me also check $T = \{1, c_2\}$. $C(\{1, c_2\})$ = common friends of 1 and $c_2$. 1 adjacent to: 2, $c_1$, $c_2$, $v_5$, $v_6$ (let me track: 1 is adjacent to 2 (yes), $c_1$ (yes, $c_1 \in C(\{1,2\})$), $c_2$ (yes), $v_5$ (yes, Case A), $v_6$ (yes)). So 1 is adjacent to everyone! $d(1) = 5$.

$c_2$ adjacent to: 1, 2, $c_1$ (yes, $c_1$-$c_2$ edge), and... $v_5$? No (just established). $v_6$? No (just established). So $c_2$ adjacent to $\{1, 2, c_1\}$, $d(c_2) = 3$.

$C(\{1, c_2\})$: common friends of 1 and $c_2$. Must be adjacent to both 1 and $c_2$. 1 is adjacent to all, so $C(\{1, c_2\}) = N(c_2) \setminus \{1, c_2\} = \{2, c_1\}$ (since $c_2$ is adjacent to 1, 2, $c_1$, and 1 is in the set $\{1, c_2\}$ so excluded). Wait, $C(\{1, c_2\}) = N(1) \cap N(c_2) \setminus \{1, c_2\}$. $N(1) = \{2, c_1, c_2, v_5, v_6\}$, $N(c_2) = \{1, 2, c_1\}$. Intersection: $\{2, c_1\}$. Remove $\{1, c_2\}$: still $\{2, c_1\}$. So $C(\{1, c_2\}) = \{2, c_1\}$, $|C| = 2$. ✓ Matching: 2-$c_1$ edge. Is 2 adjacent to $c_1$? $c_1 \in C(\{1,2\})$ means $c_1$ adjacent to 2. ✓

Every vertex not in $\{1, c_2\}$ has exactly one neighbor in $\{2, c_1\}$. Vertices: $\{2, c_1, v_5, v_6\}$.
- 2: neighbor in $\{2, c_1\}$ is $c_1$ (2 not adj to itself). 2 adjacent to $c_1$? Yes. ✓
- $c_1$: neighbor in $\{2, c_1\}$ is 2. $c_1$ adjacent to 2? Yes. ✓
- $v_5$: neighbor in $\{2, c_1\}$: $v_5$ adjacent to $c_1$ (yes), $v_5$ adjacent to 2 (no). So one neighbor ($c_1$). ✓
- $v_6$: neighbor in $\{2, c_1\}$: $v_6$ adjacent to $c_1$ (yes), $v_6$ adjacent to 2 (no). So one neighbor ($c_1$). ✓

Now let me check $T = \{v_5, v_6\}$. $v_5$ adjacent to: $c_1$, 1, $v_6$. $v_6$ adjacent to: $c_1$, 1, $v_5$. 

$C(\{v_5, v_6\}) = N(v_5) \cap N(v_6) \setminus \{v_5, v_6\}$. $N(v_5) = \{c_1, 1, v_6\}$, $N(v_6) = \{c_1, 1, v_5\}$. Intersection: $\{c_1, 1\}$. Remove $\{v_5, v_6\}$: $\{c_1, 1\}$. So $C = \{c_1, 1\}$, $|C| = 2$. ✓ Matching: $c_1$-1 edge. $c_1$ adjacent to 1? Yes. ✓

Every vertex not in $\{v_5, v_6\}$ has exactly one neighbor in $\{c_1, 1\}$. Vertices: $\{1, 2, c_1, c_2\}$.
- 1: neighbor in $\{c_1, 1\}$ is $c_1$ (1 not adj to itself). 1 adjacent to $c_1$? Yes. ✓
- $c_1$: neighbor in $\{c_1, 1\}$ is 1. ✓
- 2: neighbor in $\{c_1, 1\}$: 2 adjacent to 1 (yes), 2 adjacent to $c_1$ (yes). That's 2 neighbors! ✗

Contradiction! 2 is adjacent to both 1 and $c_1$, but should have exactly one neighbor in $\{c_1, 1\}$.

So Case A leads to a contradiction. Let me try Case B.

Case B: $v_5$ not adjacent to 1, so $v_5$ adjacent to 2 (its one neighbor in $\{1, 2\}$). And $v_5$ adjacent to $c_1$ (its neighbor in $\{c_1, c_2\}$).

Similarly, $v_6$ has one neighbor in $\{c_1, c_2\}$ and one in $\{1, 2\}$.

Sub-case B1: $v_6$ adjacent to $c_1$ (same as $v_5$) and adjacent to 2.
Sub-case B2: $v_6$ adjacent to $c_2$ and adjacent to... 1 or 2.

Let me try B1: both $v_5, v_6$ adjacent to $c_1$ and 2.

$T = \{1, c_1\}$. $C(\{1, c_1\})$: $N(1) \cap N(c_1) \setminus \{1, c_1\}$. 

$N(1)$: 1 is adjacent to 2, $c_1$, $c_2$ (at least). Is 1 adjacent to $v_5$? No (Case B). $v_6$? Let's say no for now. So $N(1) = \{2, c_1, c_2\}$, $d(1) = 3$.

$N(c_1)$: $c_1$ adjacent to 1, 2, $c_2$, $v_5$, $v_6$. So $d(c_1) = 5$.

$C(\{1, c_1\}) = \{2, c_2, v_5, v_6\} \cap \{2, c_1, c_2\} \setminus \{1, c_1\} = \{2, c_2\}$. $|C| = 2$. ✓ Matching: 2-$c_2$ edge. 2 adjacent to $c_2$? $c_2 \in C(\{1,2\})$ means $c_2$ adjacent to 2. ✓

Every vertex not in $\{1, c_1\}$ has exactly one neighbor in $\{2, c_2\}$. Vertices: $\{2, c_2, v_5, v_6\}$.
- 2: neighbor in $\{2, c_2\}$ is $c_2$. ✓
- $c_2$: neighbor in $\{2, c_2\}$ is 2. ✓
- $v_5$: neighbor in $\{2, c_2\}$: $v_5$ adjacent to 2 (yes), $v_5$ adjacent to $c_2$? If yes, 2 neighbors, bad. If no, 1 neighbor. So $v_5$ not adjacent to $c_2$.
- $v_6$: similarly, $v_6$ adjacent to 2 (yes), not to $c_2$.

Now $T = \{2, c_1\}$. $N(2) \cap N(c_1) \setminus \{2, c_1\}$. $N(2)$: 2 adjacent to 1, $c_1$, $c_2$, $v_5$, $v_6$. $d(2) = 5$. $N(c_1) = \{1, 2, c_2, v_5, v_6\}$. Intersection: $\{1, c_2, v_5, v_6\}$. Remove $\{2, c_1\}$: $\{1, c_2, v_5, v_6\}$. $|C| = 4$. ✓ Matching: need 2 edges among $\{1, c_2, v_5, v_6\}$. 

Every vertex not in $\{2, c_1\}$ has exactly one neighbor in $C = \{1, c_2, v_5, v_6\}$. Vertices: $\{1, c_2, v_5, v_6\}$ (these are the elements of $C$). Each has exactly one neighbor in $C$ (matching partner).

So we need a perfect matching on $\{1, c_2, v_5, v_6\}$. Options:
- $(1, c_2), (v_5, v_6)$: 1-$c_2$ edge (yes, exists), $v_5$-$v_6$ edge (need to add).
- $(1, v_5), (c_2, v_6)$: 1-$v_5$ edge? No (Case B). ✗
- $(1, v_6), (c_2, v_5)$: 1-$v_6$ edge? No. ✗

So matching is $(1, c_2), (v_5, v_6)$. Need $v_5$-$v_6$ edge.

Now $T = \{v_5, v_6\}$. $N(v_5) \cap N(v_6) \setminus \{v_5, v_6\}$. $N(v_5) = \{c_1, 2, v_6\}$, $N(v_6) = \{c_1, 2, v_5\}$. Intersection: $\{c_1, 2\}$. $|C| = 2$. ✓ Matching: $c_1$-2 edge. $c_1$ adjacent to 2? Yes. ✓

Every vertex not in $\{v_5, v_6\}$ has exactly one neighbor in $\{c_1, 2\}$. Vertices: $\{1, 2, c_1, c_2\}$.
- 1: neighbor in $\{c_1, 2\}$: 1 adjacent to $c_1$ (yes), 1 adjacent to 2 (yes). 2 neighbors! ✗

Contradiction again! 1 is adjacent to both $c_1$ and 2.

Hmm. So B1 also fails.

Let me try B2: $v_5$ adjacent to $c_1$ and 2; $v_6$ adjacent to $c_2$ and 1.

$T = \{1, 2\}$. $C(\{1,2\}) = \{c_1, c_2\}$ (established). Every vertex not in $\{1,2\}$ has exactly one neighbor in $\{c_1, c_2\}$.
- $c_1$: adjacent to $c_2$ (matching). ✓
- $c_2$: adjacent to $c_1$. ✓
- $v_5$: adjacent to $c_1$ (yes), not $c_2$. ✓
- $v_6$: adjacent to $c_2$ (yes), not $c_1$. ✓

$T = \{c_1, c_2\}$. $C(\{c_1, c_2\}) \supseteq \{1, 2\}$. $v_5$ adjacent to $c_1$ but not $c_2$, so $v_5 \notin C$. $v_6$ adjacent to $c_2$ but not $c_1$, so $v_6 \notin C$. $C = \{1, 2\}$, $|C| = 2$. ✓ Matching: 1-2 edge. ✓

Every vertex not in $\{c_1, c_2\}$ has exactly one neighbor in $\{1, 2\}$.
- 1: adjacent to 2. ✓
- 2: adjacent to 1. ✓
- $v_5$: adjacent to 2 (yes), adjacent to 1 (no). ✓
- $v_6$: adjacent to 1 (yes), adjacent to 2 (no). ✓

$T = \{1, c_1\}$. $N(1) = \{2, c_1, c_2, v_6\}$ (1 adjacent to 2, $c_1$, $c_2$ (since $c_2 \in C(\{1,2\})$), $v_6$). $d(1) = 4$. $N(c_1) = \{1, 2, c_2, v_5\}$. $d(c_1) = 4$. 

$C(\{1, c_1\}) = N(1) \cap N(c_1) \setminus \{1, c_1\} = \{2, c_2, v_6\} \cap \{2, c_2, v_5\} = \{2, c_2\}$. $|C| = 2$. ✓ Matching: 2-$c_2$ edge. 2 adjacent to $c_2$? $c_2 \in C(\{1,2\})$ means $c_2$ adjacent to 2. ✓

Every vertex not in $\{1, c_1\}$ has exactly one neighbor in $\{2, c_2\}$.
- 2: adjacent to $c_2$. ✓
- $c_2$: adjacent to 2. ✓
- $v_5$: adjacent to 2 (yes), adjacent to $c_2$? Need to check. If $v_5$ adjacent to $c_2$, then 2 neighbors, bad. So $v_5$ not adjacent to $c_2$. ✓ (We'll verify this is consistent.)
- $v_6$: adjacent to $c_2$ (yes), adjacent to 2? If yes, 2 neighbors, bad. So $v_6$ not adjacent to 2. ✓

$T = \{2, c_1\}$. $N(2) = \{1, c_1, c_2, v_5\}$. $d(2) = 4$. $N(c_1) = \{1, 2, c_2, v_5\}$. $d(c_1) = 4$.

$C(\{2, c_1\}) = \{1, c_2, v_5\} \cap \{1, c_2, v_5\} \setminus \{2, c_1\} = \{1, c_2, v_5\}$. $|C| = 3$. But $|C|$ must be even! ✗

Contradiction. So B2 also fails for this $T$.

Hmm. So $n = 6, m = 3$ seems impossible. Let me also check $T = \{1, c_2\}$ in B2.

$N(1) = \{2, c_1, c_2, v_6\}$, $N(c_2) = \{1, 2, c_1, v_6\}$. $C(\{1, c_2\}) = \{2, c_1, v_6\} \setminus \{1, c_2\} = \{2, c_1, v_6\}$. $|C| = 3$. Odd! ✗

So B2 fails. And we've shown B1 fails. And Case A fails. So with $|C(\{1,2\})| = 2$ and $n = 6$, we can't make it work either (at least in the cases we tried).

Wait, I think I need to be more careful. In B2, I found $C(\{2, c_1\}) = \{1, c_2, v_5\}$ with $|C| = 3$, which is odd, contradiction. So B2 is ruled out.

In B1, the contradiction was at $T = \{v_5, v_6\}$ where 1 had 2 neighbors in $C = \{c_1, 2\}$.

In Case A, the contradiction was at $T = \{v_5, v_6\}$ where 2 had 2 neighbors in $C = \{c_1, 1\}$.

Hmm, but I haven't tried all sub-cases. In Case B, $v_5$ is adjacent to 2 and $c_1$. $v_6$ could be adjacent to $c_1$ or $c_2$, and to 1 or 2. I tried ($c_1$, 2) [B1] and ($c_2$, 1) [B2]. Let me try ($c_1$, 1) and ($c_2$, 2).

B3: $v_5$ adj to $c_1$, 2. $v_6$ adj to $c_1$, 1.

$T = \{1, 2\}$, $C = \{c_1, c_2\}$. Every vertex not in $\{1,2\}$ has one neighbor in $\{c_1, c_2\}$.
- $v_5$: adj to $c_1$, not $c_2$. ✓
- $v_6$: adj to $c_1$, not $c_2$. ✓

$T = \{c_1, c_2\}$, $C = \{1, 2\}$ (since $v_5, v_6$ not adj to $c_2$). Every vertex not in $\{c_1, c_2\}$ has one neighbor in $\{1, 2\}$.
- $v_5$: adj to 2, not 1. ✓
- $v_6$: adj to 1, not 2. ✓

$T = \{1, c_1\}$. $N(1) = \{2, c_1, c_2, v_6\}$. $N(c_1) = \{1, 2, c_2, v_5, v_6\}$. $d(c_1) = 5$.
$C(\{1, c_1\}) = \{2, c_2, v_6\} \setminus \{1, c_1\} = \{2, c_2, v_6\}$. $|C| = 3$. Odd! ✗

B3 fails.

B4: $v_5$ adj to $c_1$, 2. $v_6$ adj to $c_2$, 2.

$T = \{1, 2\}$, $C = \{c_1, c_2\}$. $v_5$ adj $c_1$, $v_6$ adj $c_2$. ✓

$T = \{c_1, c_2\}$, $C = \{1, 2\}$. $v_5$ adj 2, $v_6$ adj 2. But every vertex not in $\{c_1, c_2\}$ must have exactly one neighbor in $\{1, 2\}$. $v_6$ adj to 2, not 1. ✓ $v_5$ adj to 2, not 1. ✓

$T = \{1, c_1\}$. $N(1) = \{2, c_1, c_2\}$ (1 not adj to $v_5$ or $v_6$). $d(1) = 3$. $N(c_1) = \{1, 2, c_2, v_5\}$. $d(c_1) = 4$.
$C(\{1, c_1\}) = \{2, c_2\}$. $|C| = 2$. ✓ Matching: 2-$c_2$ edge. ✓

Every vertex not in $\{1, c_1\}$ has one neighbor in $\{2, c_2\}$:
- 2: adj $c_2$. ✓
- $c_2$: adj 2. ✓
- $v_5$: adj 2 (yes), adj $c_2$? If yes, 2 neighbors. So $v_5$ not adj $c_2$. ✓
- $v_6$: adj $c_2$ (yes), adj 2 (yes). 2 neighbors! ✗

Contradiction. $v_6$ is adjacent to both 2 and $c_2$.

B4 fails.

So all sub-cases for $n = 6, m = 3$ with $|C(\{1,2\})| = 2$ fail. And $|C(\{1,2\})| = 4$ also failed. So $n = 6$ is impossible for $m = 3$.

This strongly suggests that $K_{m+1}$ is the unique solution, and the answer is $m$.

But let me think about whether there could be larger $n$ that works, or other structures.

Actually, let me think about this more generally. Let me consider the problem for general $m$.

**Claim: The only graph satisfying the condition is $K_{m+1}$, and the answer is $m$.**

Let me try to prove this. Suppose we have a graph $G$ on $n$ vertices where every $m$-subset has exactly one common neighbor.

**Step 1: Show $n \geq m + 1$.** We need at least $m+1$ vertices since we need a common friend for every $m$-subset, and the common friend is not in the subset.

Actually, we need $n \geq m + 1$ since for any $m$-subset, there's a common friend outside it.

**Step 2: Show $n = m + 1$.** 

Suppose $n \geq m + 2$. We'll derive a contradiction.

Consider any $m$-subset $S$. It has a unique common friend $f(S) \notin S$. 

Consider any $(m-1)$-subset $T$. As I showed, $C(T) = \bigcap_{t \in T} N(t)$ forms a perfect matching, and every vertex $v \notin T$ has exactly one neighbor in $C(T)$.

Since $n \geq m + 2$, $|V \setminus T| = n - m + 1 \geq 3$. And $|C(T)| \geq 2$ (it's a perfect matching, so even and $\geq 2$).

Now, consider two vertices $u, v \notin T$ that are matched to the same $c \in C(T)$... wait, no. Each vertex in $V \setminus T$ has exactly one neighbor in $C(T)$, but multiple vertices can share the same neighbor in $C(T)$.

Hmm, let me think differently. 

Let me use a counting argument. We have $\sum_{v} \binom{d(v)}{m} = \binom{n}{m}$.

Also, for any $(m-1)$-subset $T$, $\sum_{v: T \subseteq N(v)} (d(v) - m + 1) = n - m + 1$... wait, let me think about this.

For $(m-1)$-subset $T$, every $v \notin T$ has exactly one neighbor in $C(T)$. The vertices in $C(T)$ are the common friends of $T$, i.e., $\{w : T \subseteq N(w)\}$. For each $v \notin T$, $v$ is adjacent to exactly one element of $C(T)$. 

Now, $\sum_{w \in C(T)} |N(w) \setminus T| = \sum_{w \in C(T)} d(w) - (m-1)$ (since each $w \in C(T)$ is adjacent to all $m-1$ vertices of $T$). But also, $\sum_{w \in C(T)} |N(w) \cap (V \setminus T)| = |V \setminus T| = n - m + 1$ (since each vertex in $V \setminus T$ is adjacent to exactly one $w \in C(T)$, and each $w \in C(T)$ is in $V \setminus T$ and adjacent to exactly one other element of $C(T)$).

Wait, let me be more careful. $V \setminus T$ includes elements of $C(T)$ and elements not in $C(T)$. Each element of $V \setminus T$ has exactly one neighbor in $C(T)$. So:

$\sum_{w \in C(T)} |N(w) \cap (V \setminus T)| = |V \setminus T| = n - m + 1$

But $|N(w) \cap (V \setminus T)| = d(w) - |N(w) \cap T| = d(w) - (m-1)$ (since $w \in C(T)$ means $w$ is adjacent to all of $T$, so $|N(w) \cap T| = m - 1$).

So $\sum_{w \in C(T)} (d(w) - m + 1) = n - m + 1$.

Let $|C(T)| = r$. Then $\sum_{w \in C(T)} d(w) = n - m + 1 + r(m-1) = n - 1 + r(m - 2)$.

Hmm, this is a relation but I'm not sure it directly helps.

Let me try another approach. Let me consider the "dual" structure.

For each vertex $v$, $N(v)$ is a subset of $V \setminus \{v\}$. The condition is that every $m$-subset is contained in exactly one $N(v)$. 

This is exactly the definition of a **Steiner system** $S(m, \cdot, n)$ with variable block sizes, where the blocks are $\{N(v) : v \in V\}$ and block $N(v)$ doesn't contain $v$.

In a Steiner system $S(t, k, n)$ with constant block size $k$, we have Fisher's inequality: $b \geq n$ (number of blocks $\geq$ number of points). Here $b = n$ (one block per vertex), so Fisher's inequality is tight, which happens for symmetric designs.

But our blocks have variable sizes. Let me think about whether we can use a Fisher-type inequality.

Actually, in our case, the number of blocks equals the number of points ($n$), and every $m$-subset is in exactly one block. This is a very strong condition.

Let me think about $m = 2$ first (even though the problem says $m \geq 3$). For $m = 2$: every pair has exactly one common friend. This is the friendship theorem condition (well, almost—the friendship theorem says every pair has exactly one common neighbor, and the conclusion is the windmill graph). The windmill graph $F_k$ has $2k+1$ vertices, and the universal vertex has degree $2k$. So for $m = 2$, the answer would be $2k$ which is unbounded. But the problem says $m \geq 3$.

So the condition for $m \geq 3$ is much more restrictive. Let me think about why.

For $m = 2$, the windmill graph works: every pair has exactly one common friend. But for $m = 3$, we need every triple to have exactly one common friend, which is much stronger.

Let me try to prove $n = m + 1$ for $m \geq 3$.

**Approach: Show that if $n \geq m + 2$, we get a contradiction.**

Suppose $n \geq m + 2$. Take any $m$-subset $S$ with common friend $f = f(S)$. Now, $f \notin S$ and $f$ is adjacent to all of $S$. Consider any $v \in V \setminus (S \cup \{f\})$ (this exists since $n \geq m + 2$).

Consider the $m$-subset $S' = (S \setminus \{s\}) \cup \{v\}$ for some $s \in S$. This has a unique common friend $f' = f(S')$.

$f'$ is adjacent to all of $S \setminus \{s\}$ and to $v$. 

Now, $f$ is adjacent to all of $S \setminus \{s\}$ (since $f$ is adjacent to all of $S$). Is $f$ adjacent to $v$? Not necessarily.

If $f$ is adjacent to $v$, then $f$ is a common friend of $S'$, so $f' = f$ (by uniqueness). But $f$ is not adjacent to $s$... wait, $f$ IS adjacent to $s$ (since $f$ is the common friend of $S$). But $s \notin S'$, so that's fine. $f$ is adjacent to all of $S' = (S \setminus \{s\}) \cup \{v\}$ iff $f$ is adjacent to $v$. If so, $f' = f$.

If $f$ is not adjacent to $v$, then $f' \neq f$, and $f'$ is adjacent to all of $S \setminus \{s\}$ and $v$.

This is getting complicated. Let me try a different approach.

**Approach via the structure of $C(T)$.**

For any $(m-1)$-subset $T$, $C(T)$ is a perfect matching and every $v \notin T$ has exactly one neighbor in $C(T)$.

Let $|C(T)| = 2r$ (even). The matching pairs up $C(T)$ into $r$ pairs. Each $v \notin T$ is adjacent to exactly one element of $C(T)$.

Now, the elements of $C(T)$ themselves are in $V \setminus T$, and each has exactly one neighbor in $C(T)$ (its matching partner). So the $n - m + 1$ vertices in $V \setminus T$ are partitioned by which element of $C(T)$ they're adjacent to. The $2r$ elements of $C(T)$ are each adjacent to their matching partner (within $C(T)$), so they form $r$ pairs. The remaining $n - m + 1 - 2r$ vertices (not in $C(T)$, not in $T$) are each adjacent to exactly one element of $C(T)$.

Now, consider two elements $c, c'$ of $C(T)$ that are matching partners (i.e., adjacent). Consider the $m$-subset $T \cup \{c\}$. Its unique common friend is... the common friend must be adjacent to all of $T$ (so in $C(T)$) and adjacent to $c$. Within $C(T)$, $c$'s only neighbor is $c'$. So the common friend of $T \cup \{c\}$ is $c'$. Similarly, common friend of $T \cup \{c'\}$ is $c$.

Now consider $T \cup \{v\}$ for $v \notin T, v \notin C(T)$. $v$'s unique neighbor in $C(T)$ is some $c_v$. The common friend of $T \cup \{v\}$ is $c_v$.

Now, here's a key observation. Take $T$ to be an $(m-1)$-subset, and consider $c \in C(T)$ with matching partner $c'$. We have $c$ adjacent to all of $T$ and to $c'$. Also, $c$ is adjacent to some vertices outside $T \cup C(T)$ (those $v$ with $c_v = c$).

Now consider a different $(m-1)$-subset $T'$. Let me try to use two different $(m-1)$-subsets to derive constraints.

Actually, let me try a cleaner approach. Let me consider the case $m = 3$ and try to prove $n = 4$ directly, then generalize.

For $m = 3$, $T$ is a pair. $C(T)$ is a perfect matching. Let me pick $T = \{a, b\}$ and $C(T) = \{c_1, c_2, \ldots, c_{2r}\}$ with matching $(c_1, c_2), (c_3, c_4), \ldots$

Every vertex $v \notin \{a, b\}$ has exactly one neighbor in $C(T)$.

Now, $c_1$ is adjacent to $a, b, c_2$, and possibly others. $c_2$ is adjacent to $a, b, c_1$, and possibly others.

Consider $T' = \{a, c_1\}$. $C(T')$ = common friends of $a$ and $c_1$. $a$ is adjacent to all of $C(T)$ (since $C(T) = N(a) \cap N(b)$, so $a$ is adjacent to $c_1, c_2, \ldots$). Wait, $C(T) = N(a) \cap N(b)$, so $c_i \in N(a)$ and $c_i \in N(b)$. So $a$ is adjacent to all $c_i$.

$c_1$ is adjacent to $a, b, c_2$ (at least). 

$C(T') = N(a) \cap N(c_1) \setminus \{a, c_1\}$. $N(a)$ includes $b$ and all $c_i$ (and possibly others). $N(c_1)$ includes $a, b, c_2$ (and possibly others). 

Common: $b$ (in $N(a)$? yes; in $N(c_1)$? yes), $c_2$ (in $N(a)$? yes; in $N(c_1)$? yes). Other $c_i$ ($i \geq 3$): in $N(a)$? yes; in $N(c_1)$? $c_1$'s only neighbor in $C(T)$ is $c_2$, so $c_1$ is not adjacent to $c_i$ for $i \geq 3$. So $c_i \notin C(T')$ for $i \geq 3$.

So $C(T') \supseteq \{b, c_2\}$, and $C(T') \subseteq V \setminus \{a, c_1\}$. The elements of $C(T')$ are common friends of $a$ and $c_1$.

Now, $|C(T')|$ must be even. If $C(T') = \{b, c_2\}$, then $b$ and $c_2$ must be adjacent (matching). 

Are there other elements? Vertices $v \notin T, v \notin C(T)$ (i.e., $v \notin \{a, b, c_1, \ldots, c_{2r}\}$): is $v \in C(T')$? $v \in N(a)$? Not necessarily. $v \in N(c_1)$? $v$'s neighbor in $C(T)$ is some $c_j$. If $c_j = c_1$, then $v$ is adjacent to $c_1$. And if $v$ is also adjacent to $a$, then $v \in C(T')$.

Hmm, this is getting complicated. Let me try to think about it more cleverly.

**Key idea:** Let me show that every pair of vertices is adjacent. If the graph is complete, then $n = m + 1$ (since in $K_n$, every $m$-subset has $n - m$ common friends, and we need exactly 1, so $n = m + 1$).

So I want to show the graph is complete.

Suppose not. Then there exist non-adjacent vertices $a, b$. Consider $T = \{a, b\}$ (for $m = 3$; for general $m$, I'd need $T$ to be an $(m-1)$-subset containing $a$ and $b$, but let me first handle $m = 3$).

$C(\{a, b\}) = N(a) \cap N(b) \setminus \{a, b\}$. Since $a, b$ are not adjacent, $a \notin N(b)$ and $b \notin N(a)$, so $C(\{a, b\}) = N(a) \cap N(b)$.

$|C(\{a, b\})| = 2r$ for some $r \geq 1$ (since it's a perfect matching, and must be non-empty because any triple containing $a, b$ needs a common friend).

Every vertex $v \notin \{a, b\}$ has exactly one neighbor in $C(\{a, b\})$.

Now, $a$ is adjacent to all of $C(\{a, b\})$ (by definition). $b$ is also adjacent to all of $C(\{a, b\})$.

But $a \notin \{a, b\}$... $a$ is in $\{a, b\}$, so the condition "every $v \notin \{a, b\}$ has exactly one neighbor in $C$" applies to vertices other than $a, b$. 

The vertices in $C(\{a, b\})$ are each adjacent to both $a$ and $b$. Within $C$, they form a matching. Each vertex in $C$ has exactly one neighbor in $C$ (its matching partner).

Each vertex $v \notin \{a, b\} \cup C$ has exactly one neighbor in $C$.

Now, consider $c_1 \in C$ with matching partner $c_2 \in C$. $c_1$ is adjacent to $a, b, c_2$. 

Consider the triple $\{a, b, c_1\}$. Common friend: must be adjacent to $a, b, c_1$. In $C$, the only vertex adjacent to $c_1$ is $c_2$. And $c_2$ is adjacent to $a$ and $b$. So $c_2$ is the common friend. ✓ (exactly one, since no other vertex in $C$ is adjacent to $c_1$, and vertices outside $C$ are not adjacent to both $a$ and $b$... wait, are they? A vertex $v \notin \{a, b\} \cup C$ is not in $C = N(a) \cap N(b)$, so $v$ is not adjacent to $a$ or not adjacent to $b$. So $v$ can't be a common friend of $\{a, b, c_1\}$. ✓)

Now consider the triple $\{a, c_1, c_2\}$. Common friend: adjacent to $a, c_1, c_2$. $b$ is adjacent to $a$? No! $a$ and $b$ are not adjacent. So $b$ is not a common friend. 

In $C$: who is adjacent to both $c_1$ and $c_2$? $c_1$'s only neighbor in $C$ is $c_2$, and $c_2$'s only neighbor in $C$ is $c_1$. So no other vertex in $C$ is adjacent to both. $c_1$ and $c_2$ are adjacent to each other, but $c_1$ is not adjacent to itself, and $c_2$ is not adjacent to itself.

Outside $C \cup \{a, b\}$: a vertex $v$ adjacent to $a$ and to both $c_1, c_2$. $v$'s neighbor in $C$ is exactly one of $c_1, c_2$ (say $c_1$). Then $v$ is adjacent to $c_1$ but not $c_2$ (since $v$ has exactly one neighbor in $C$). So $v$ is not adjacent to $c_2$, hence not a common friend.

So the common friend of $\{a, c_1, c_2\}$ must be adjacent to $a, c_1, c_2$. We've ruled out $b$, all of $C \setminus \{c_1, c_2\}$, and all of $V \setminus (C \cup \{a, b\})$. The only remaining candidates are $c_1$ and $c_2$ themselves, but they're in the triple. So there's no common friend! 

This is a contradiction (we need exactly one common friend). 

Wait, let me double-check. The common friend of $\{a, c_1, c_2\}$ must be a vertex $w \notin \{a, c_1, c_2\}$ with $w$ adjacent to $a$, $c_1$, and $c_2$.

- $b$: adjacent to $c_1$ (yes), $c_2$ (yes), $a$ (no, since $a, b$ non-adjacent). ✗
- $c_i \in C, i \geq 3$: adjacent to $a$ (yes), $c_1$ (no, only $c_2$ is adj to $c_1$ in $C$). ✗
- $v \notin C \cup \{a, b\}$: adjacent to $a$? Maybe. Adjacent to $c_1$? Only if $c_1$ is $v$'s neighbor in $C$. Adjacent to $c_2$? Only if $c_2$ is $v$'s neighbor in $C$. But $v$ has exactly one neighbor in $C$, so can't be adjacent to both $c_1$ and $c_2$. ✗

So no common friend exists for $\{a, c_1, c_2\}$. Contradiction!

Therefore, for $m = 3$, there cannot be non-adjacent vertices. The graph must be complete, hence $K_n$ with $n = m + 1 = 4$, and the max degree is $m = 3$.

Now let me generalize to $m \geq 3$.

**General case:** Suppose $G$ is a graph on $n$ vertices where every $m$-subset has exactly one common neighbor. Suppose $n \geq m + 2$ (we want to derive a contradiction, or more precisely, show the graph is complete).

Actually, let me try the same approach. Suppose there exist non-adjacent vertices $a, b$. 

Take an $(m-1)$-subset $T$ containing both $a$ and $b$ (possible since $m - 1 \geq 2$). $T = \{a, b, t_3, \ldots, t_{m-1}\}$.

$C(T) = \bigcap_{t \in T} N(t) \setminus T$. Since $a, b \in T$ and $a, b$ are not adjacent, $C(T) = \bigcap_{t \in T} N(t)$ (since $a \notin N(b)$ and $b \notin N(a)$, elements of $T$ are automatically excluded).

$|C(T)| = 2r$ for some $r \geq 1$. $C(T)$ is a perfect matching. Every $v \notin T$ has exactly one neighbor in $C(T)$.

Take $c_1, c_2 \in C(T)$ that are matching partners (adjacent). Both are adjacent to all of $T$ (including $a$ and $b$).

Now consider the $m$-subset $S = (T \setminus \{b\}) \cup \{c_1\} = \{a, t_3, \ldots, t_{m-1}, c_1\}$. This is an $m$-subset (we removed $b$ and added $c_1$). Its unique common friend $f$ must be adjacent to $a, t_3, \ldots, t_{m-1}, c_1$.

$f$ is adjacent to all of $T \setminus \{b\}$, so $f \in C(T \setminus \{b\})$ (common friends of $T \setminus \{b\}$). Also $f$ is adjacent to $c_1$.

Now, $c_2$ is adjacent to all of $T$ (hence all of $T \setminus \{b\}$) and to $c_1$ (matching partner). So $c_2$ is a common friend of $S$. By uniqueness, $f = c_2$.

Now consider the $m$-subset $S' = (T \setminus \{b\}) \cup \{c_2\} = \{a, t_3, \ldots, t_{m-1}, c_2\}$. By the same argument, its common friend is $c_1$.

Now consider the $m$-subset $S'' = (T \setminus \{a, b\}) \cup \{c_1, c_2\} = \{t_3, \ldots, t_{m-1}, c_1, c_2\}$. This has $m - 2 + 2 = m$ elements. ✓ Its common friend $f''$ must be adjacent to $t_3, \ldots, t_{m-1}, c_1, c_2$.

$f''$ is adjacent to all of $T \setminus \{a, b\} = \{t_3, \ldots, t_{m-1}\}$, and to $c_1$ and $c_2$.

Candidates:
- $a$: adjacent to $t_3, \ldots, t_{m-1}$ (yes, since $a \in T$ and... wait, $a$ is adjacent to $t_i$? $t_i \in T$ and $a \in T$, but we don't know if $a$ is adjacent to $t_i$). Hmm, actually $T$ is just a subset, not a clique. Let me reconsider.

Wait, I think I need to be more careful. $T$ is an $(m-1)$-subset, and $C(T) = \bigcap_{t \in T} N(t)$. The elements of $C(T)$ are adjacent to all elements of $T$. But elements of $T$ are not necessarily adjacent to each other.

So when I consider $S'' = \{t_3, \ldots, t_{m-1}, c_1, c_2\}$, the common friend must be adjacent to $t_3, \ldots, t_{m-1}$ (all of $T \setminus \{a, b\}$) and to $c_1, c_2$.

- $a$: adjacent to $t_3, \ldots, t_{m-1}$? Not necessarily. $a$ is in $T$, but $a$ might not be adjacent to other elements of $T$. Actually, we need $a$ to be adjacent to $t_i$ for $i = 3, \ldots, m-1$. We don't know this.

Hmm, so my approach of taking an arbitrary $(m-1)$-subset $T$ containing $a, b$ doesn't work directly because elements of $T$ might not be adjacent to each other.

Let me reconsider. Let me take $T$ to be an $(m-1)$-subset containing $a$ and $b$ where the other elements are chosen to be adjacent to both $a$ and $b$... but I don't know if such elements exist.

Actually, let me reconsider the $m = 3$ proof. There, $T = \{a, b\}$ and I used the triple $\{a, c_1, c_2\}$ where $c_1, c_2 \in C(\{a, b\})$ are matching partners. The key was that $c_1, c_2$ are both adjacent to $a$ (and $b$), and the common friend of $\{a, c_1, c_2\}$ had to be adjacent to $a, c_1, c_2$, and we showed no such vertex exists.

For general $m$, I need to find an $m$-subset whose common friend doesn't exist. Let me try:

Take $T = \{a, b, t_3, \ldots, t_{m-1}\}$ an $(m-1)$-subset with $a, b \in T$. Let $c_1, c_2 \in C(T)$ be matching partners.

Consider the $m$-subset $S = \{a, t_3, \ldots, t_{m-1}, c_1, c_2\} \setminus \{b\}$... wait, that's $T \setminus \{b\} \cup \{c_1, c_2\}$, which has $(m-1) - 1 + 2 = m$ elements. ✓

The common friend of $S$ must be adjacent to $a, t_3, \ldots, t_{m-1}, c_1, c_2$.

Now, $b$ is adjacent to $t_3, \ldots, t_{m-1}$? Not necessarily (since $T$ is not necessarily a clique).

Hmm, I'm stuck because $T$ is not a clique. Let me think differently.

Actually, in the $m = 3$ case, $T = \{a, b\}$ has only 2 elements, and the key point was that $b$ is not adjacent to $a$. For the triple $\{a, c_1, c_2\}$, we needed a common friend adjacent to $a, c_1, c_2$, and we showed $b$ fails because $b$ is not adjacent to $a$.

For general $m$, let me try the $m$-subset $\{a, c_1, c_2, t_4, \ldots, t_m\}$ where $t_4, \ldots, t_m$ are $m - 3$ additional vertices. But I need these to be chosen carefully.

Actually, let me try a different approach. Let me consider the $m$-subset $S = (T \setminus \{b\}) \cup \{c_1, c_2\}$ where $T = \{a, b, t_3, \ldots, t_{m-1}\}$ and $c_1, c_2 \in C(T)$ are matching partners.

$S = \{a, t_3, \ldots, t_{m-1}, c_1, c_2\}$, $|S| = 1 + (m-3) + 2 = m$. ✓

Common friend $f$ must be adjacent to all of $S$: $a, t_3, \ldots, t_{m-1}, c_1, c_2$.

Now, $f$ is adjacent to $c_1$ and $c_2$. Recall that within $C(T)$, $c_1$'s only neighbor is $c_2$ and vice versa. So if $f \in C(T)$, then $f$ is adjacent to $c_1$ only if $f = c_2$, and adjacent to $c_2$ only if $f = c_1$. But $f$ must be adjacent to both, which is impossible for $f \in C(T) \setminus \{c_1, c_2\}$ (since such $f$ is adjacent to neither $c_1$ nor $c_2$ within $C(T)$). And $f = c_1$ or $c_2$ is impossible since they're in $S$.

So $f \notin C(T)$. Also $f \notin T$ (since $f \notin S$ and $f$ must be adjacent to all of $S$, and elements of $S$ are not adjacent to themselves).

So $f \in V \setminus (T \cup C(T))$ (or $f \in C(T) \setminus \{c_1, c_2\}$, but we ruled that out).

Wait, I said $f \notin C(T)$. Let me re-examine. $f$ must be adjacent to $c_1$ and $c_2$. If $f \in C(T) \setminus \{c_1, c_2\}$, then $f$'s only neighbor in $C(T)$ is its matching partner, which is not $c_1$ or $c_2$ (since $c_1, c_2$ are matched to each other). So $f$ is not adjacent to $c_1$ or $c_2$. ✗

If $f \in V \setminus (T \cup C(T))$: $f$ has exactly one neighbor in $C(T)$, say $c_j$. If $c_j = c_1$, then $f$ is adjacent to $c_1$ but not $c_2$. If $c_j = c_2$, then $f$ is adjacent to $c_2$ but not $c_1$. Either way, $f$ is not adjacent to both $c_1$ and $c_2$. ✗

If $f = b$: $b$ is adjacent to $c_1$ (yes, since $c_1 \in C(T)$ means $c_1 \in N(b)$) and $c_2$ (yes). $b$ is adjacent to $a$? No (by assumption, $a, b$ non-adjacent). $b$ is adjacent to $t_3, \ldots, t_{m-1}$? $b \in T$ and $t_i \in T$, but $b$ might not be adjacent to $t_i$. Actually, $b$ is adjacent to $t_i$ iff $t_i \in N(b)$. We don't know this in general.

Hmm, so the issue is        — AI历史解题过程（thinking）
#   polymath_01825         — 题目ID

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
  <problem_id>polymath_01825</problem_id>
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

In a wagon, every $m \geq 3$ people have exactly one common friend. (When $A$ is $B$'s friend, $B$ is also $A$'s friend. No one was considered as his own friend.) Find the number of friends of the person who has the most friends.

## Standard Solution

1. **Understanding the Problem:**
   We are given a graph where every set of \( m \geq 3 \) people has exactly one common friend. We need to find the number of friends of the person who has the most friends.

2. **Applying the Friendship Theorem:**
   The Friendship Theorem states that if every pair of people in a group has exactly one common friend, then there is one person who is friends with everyone else. This theorem can be extended to the case where every set of \( m \) people has exactly one common friend.

3. **Graph Structure:**
   According to the problem, the graph has a specific structure:
   - There are \( m-1 \) vertices \( x_1, x_2, \ldots, x_{m-1} \), each of which is connected to all other vertices.
   - Every other vertex has exactly one neighbor among \( x_1, x_2, \ldots, x_{m-1} \).

4. **Induction Hypothesis:**
   We use induction on \( m \). Assume the statement is true for all values smaller than \( m \) (for \( m \geq 3 \)).

5. **Base Case:**
   For \( m = 3 \), the graph must have a structure where there are 2 vertices \( x_1 \) and \( x_2 \) connected to all other vertices, and every other vertex has exactly one neighbor among \( x_1 \) and \( x_2 \).

6. **Inductive Step:**
   - Let \( x_1 \) be one of the vertices with maximal degree.
   - Apply the induction hypothesis for \( m-1 \) to the graph induced on the set of neighbors of \( x_1 \).
   - We find neighbors \( x_2, \ldots, x_{m-1} \) of \( x_1 \), each of which is connected to all other neighbors of \( x_1 \).
   - Because of the maximality assumption, the neighbors of \( x_i \) are the neighbors of \( x_1 \) for all \( i = 1, 2, \ldots, m-1 \).

7. **Common Neighbor Argument:**
   - Let \( x \) be a neighbor of \( x_i \) different from all the \( x_i \).
   - Since \( y, x_1, \ldots, x_{m-1} \) have exactly one common neighbor, \( x \) is connected to exactly one other neighbor of \( x_i \).
   - The graph \( G \) induced on the set formed by \( x_i \) and their neighbors has the form described above.

8. **Contradiction Argument:**
   - Suppose we can find a vertex \( y \) not in \( G \).
   - There must be at least one neighbor \( x \) of \( x_i \) different from all \( x_i \); otherwise, \( y, x_i \) can have no common friend.
   - Take such a neighbor \( x \). The vertices \( x_1, \ldots, x_{m-2}, x, y \) have exactly one common friend, and this friend can only be the unique neighbor of \( x_i \) linked to \( x \) (call it \( \bar{x} \)).
   - Repeat the procedure with \( \bar{x} \) instead of \( x \). We find that \( y \) is linked to \( x \) as well.
   - But now \( y, x_i \) have at least two common friends (\( x \) and \( \bar{x} \)), which is a contradiction.

9. **Conclusion:**
   This means that \( x_i \) and their neighbors are all the vertices in the graph, and we have what we wanted.

The final answer is \( \boxed{ m-1 } \).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a wagon (a finite set of people) where every $m \geq 3$ people have exactly one common friend. We need to find the number of friends of the person who has the most friends.

Let me think about this. We have a graph where vertices are people and edges represent friendship. The condition is: every set of $m$ vertices has exactly one common neighbor (a vertex adjacent to all $m$ of them).

Wait, let me re-read. "Every $m \geq 3$ people have exactly one common friend." So for any subset of $m$ people, there is exactly one person who is a friend of all $m$ of them.

So the condition is: for every $m$-element subset $S$ of vertices, $|\bigcap_{v \in S} N(v)| = 1$, where $N(v)$ is the set of neighbors of $v$.

We need to find the maximum degree.

Let me think about what configurations satisfy this.

First, let's think about small cases. Let's say there are $n$ people total.

Case 1: The "star" or "wheel" type configuration. 

Actually, let me think about this more carefully. Consider a configuration where there's one "hub" person $H$ who is friends with everyone, and the other people form some structure.

If $H$ is friends with everyone, then for any $m$-subset $S$, $H$ is a common friend of $S$ (as long as $H \notin S$). But we need exactly one common friend. So if $S$ doesn't contain $H$, then $H$ is one common friend, and we need no other common friend. If $S$ contains $H$, then we need exactly one common friend of $S$.

Hmm, let me think about specific structures.

**Configuration A: Wheel graph $W_n$.** A central vertex connected to all $n-1$ rim vertices, and the rim forms a cycle. 

For a set of $m$ rim vertices: the center is a common friend. Are there others? A rim vertex $v$ is a common friend of $S$ iff $v$ is adjacent to all vertices in $S$. On the rim, $v$ is adjacent to its two cycle neighbors. So $v$ is a common friend of $S$ (among rim vertices) iff all of $S$ is contained in $N(v) \cap \text{rim} = \{v-1, v+1\}$ (cycle neighbors). So $S \subseteq \{v-1, v+1\}$, meaning $|S| \leq 2$. Since $m \geq 3$, this is impossible. So the only common friend of any $m$ rim vertices is the center. Good, exactly one.

But what if $S$ contains the center? Then we need exactly one common friend of $\{H\} \cup S'$ where $S'$ is $m-1$ rim vertices. A common friend must be adjacent to $H$ (so it's a rim vertex) and adjacent to all of $S'$. A rim vertex $v$ adjacent to all of $S'$ means $S' \subseteq N(v) \cap \text{rim} = \{v-1, v+1\}$. So $|S'| \leq 2$, meaning $m-1 \leq 2$, i.e., $m \leq 3$.

For $m = 3$: $S' = \{v-1, v+1\}$ for some $v$, and $S = \{H, v-1, v+1\}$. The common friend is $v$. Exactly one. Good.

For $m = 4$: $S' = 3$ rim vertices, need a rim vertex adjacent to all 3. But each rim vertex is adjacent to only 2 rim vertices. So no common friend exists. Bad.

So the wheel works only for $m = 3$.

For $m = 3$, the wheel graph $W_n$ (center + cycle of $n-1$) satisfies: every 3 people have exactly one common friend. The center has $n-1$ friends. But $n$ can be anything $\geq 4$. So the answer isn't determined for $m = 3$? 

Wait, but the problem says "find the number of friends of the person who has the most friends." This suggests the answer is a specific number, presumably depending on $m$.

Hmm, let me reconsider. Maybe the problem is asking for the answer in terms of $m$, and it should be the same for all valid configurations.

Wait, for the wheel with $m=3$, the max degree is $n-1$ which varies. So either the wheel doesn't satisfy the condition for all triples, or I'm missing something.

Let me recheck the wheel for $m = 3$ more carefully. Take 3 rim vertices that are not consecutive, say vertices 1, 3, 5 on a cycle of length $\geq 6$. Their common friends: the center is adjacent to all of them. Is any rim vertex adjacent to all of 1, 3, 5? A rim vertex $v$ is adjacent to $v-1$ and $v+1$ on the rim. For $v$ to be adjacent to 1, 3, and 5, we'd need $\{1,3,5\} \subseteq \{v-1, v+1\}$, impossible since $|S|=3 > 2$. So only the center. Good.

Take 3 consecutive rim vertices 1, 2, 3. Common friends: center (adjacent to all). Rim vertex 2 is adjacent to 1 and 3 (its neighbors) but is 2 adjacent to 2? No, no self-loops. So 2 is not a common friend of {1,2,3} since 2 is not its own friend. What about rim vertex adjacent to 1, 2, 3? Vertex 2 is adjacent to 1 and 3 but not to itself. So no. Only the center. Good.

Take {center, 1, 2}. Common friends: must be adjacent to center (so a rim vertex), to 1, and to 2. Rim vertex adjacent to both 1 and 2: vertex 2 is adjacent to 1 (yes, neighbor on cycle) and to 2 (no). Vertex 1 is adjacent to 2 (yes) and to 1 (no). So we need a rim vertex $v$ with $1, 2 \in \{v-1, v+1\}$. That means $v$ is adjacent to both 1 and 2 on the cycle. If the cycle is $...1, 2, 3...$, then vertex 2 is adjacent to 1 and 3, not to 2. Vertex 1 is adjacent to 0 and 2. So vertex 1 is adjacent to 2 but not to 1. Hmm, we need $v$ adjacent to both 1 and 2. $v=1$: adjacent to 2? yes. adjacent to 1? no. $v=2$: adjacent to 1? yes. adjacent to 2? no. $v=0$: adjacent to 1? yes. adjacent to 2? Only if 0 and 2 are cycle-neighbors, which they're not (0 is adjacent to $n-1$ and 1). So no rim vertex is adjacent to both 1 and 2... wait, that can't be right. On a cycle, vertices 1 and 2 are adjacent. A common neighbor of 1 and 2 on the cycle would be a vertex adjacent to both. 1's neighbors on cycle: $n-1, 2$ (wait, no, let me use 0-indexed). 

Let me use a cycle $0, 1, 2, \ldots, k-1$ where $k = n-1$. Neighbors of $i$ on cycle: $(i-1) \bmod k$ and $(i+1) \bmod k$. Plus the center.

Take $S = \{\text{center}, 0, 1\}$. Common friend must be adjacent to center, 0, and 1. Adjacent to center means it's a rim vertex. Adjacent to 0 and 1: vertex $v$ with $0 \in \{v-1, v+1\}$ and $1 \in \{v-1, v+1\} \pmod{k}$. So $v \in \{1, k-1\}$ (adjacent to 0) and $v \in \{0, 2\}$ (adjacent to 1). Intersection: need $v$ in both sets. $\{1, k-1\} \cap \{0, 2\}$. If $k = 3$: $\{1, 2\} \cap \{0, 2\} = \{2\}$. So $v = 2$. If $k \geq 4$: $\{1, k-1\} \cap \{0, 2\} = \emptyset$ (since $k-1 \geq 3 \neq 0, 2$). 

So for $k \geq 4$ (i.e., $n \geq 5$), the triple $\{\text{center}, 0, 1\}$ has only the center as... wait, the center is in $S$, so the center can't be a common friend of itself. So we need a common friend outside $S$. For $k \geq 4$, there's no common friend. That violates the condition!

So the wheel graph only works when $k = 3$, i.e., $n = 4$: the complete graph $K_4$ minus... no, $W_4$ is the center plus a triangle. That's $K_4$! In $K_4$, every 3 vertices have exactly one common friend (the 4th vertex). The max degree is 3.

Hmm wait, $K_4$: 4 vertices, each pair connected. Any 3 vertices: the common friends are vertices adjacent to all 3. The 4th vertex is adjacent to all 3. Any of the 3 vertices themselves? No, a vertex isn't adjacent to itself. So exactly one common friend. Max degree = 3. And $m = 3$.

But can we have other configurations for $m = 3$? Let me think...

Actually, let me reconsider the problem. Maybe the answer is $m$ for all valid $m$.

Let me think about $m = 3$ more carefully. Is $K_4$ the only configuration?

Consider the Petersen graph or other structures... Actually, let me think about this differently.

Let me think about what graphs satisfy: every $m$ vertices have exactly one common neighbor.

**Key insight:** Consider the "friendship graph" / windmill graph. The friendship theorem states: if every pair of vertices has exactly one common neighbor, then there's a vertex adjacent to all others (the "universal friend"). 

Our condition is different: every $m$ vertices have exactly one common neighbor.

Let me think about generalizing. 

Actually, let me think about the complete graph $K_{m+1}$. In $K_{m+1}$, any $m$ vertices have exactly one common neighbor (the remaining vertex). The max degree is $m$. 

Can we do better? Can we have a graph on more than $m+1$ vertices satisfying this?

Let me think about $m = 3$. $K_4$ works with max degree 3. Can we have a graph on 5+ vertices where every 3 vertices have exactly one common neighbor?

Let me try to construct one. Suppose we have vertices $1, 2, 3, 4, 5$. 

Every triple must have exactly one common neighbor. There are $\binom{5}{3} = 10$ triples.

Consider the "windmill"/friendship graph $F_k$: $k$ triangles sharing a common vertex. The universal vertex $u$ is connected to all $2k$ other vertices, and the other vertices are paired up: $a_i, b_i$ with edge $a_i b_i$, and both connected to $u$. So $n = 2k+1$.

In this graph, every pair has exactly one common neighbor (friendship theorem). What about every triple?

Take triple $\{a_i, b_i, a_j\}$ where $i \neq j$. Common neighbors: $u$ is adjacent to all three. $a_i$'s neighbors: $u, b_i$. $b_i$'s neighbors: $u, a_i$. $a_j$'s neighbors: $u, b_j$. Common: $u$. Is there another? $b_j$ is adjacent to $a_j$ and $u$, but not to $a_i$ or $b_i$. So only $u$. Good, exactly one.

Take triple $\{a_i, a_j, a_k\}$ (all from different pairs, $i, j, k$ distinct). Common neighbors: $u$ is adjacent to all. $a_i$'s neighbors: $u, b_i$. $a_j$'s neighbors: $u, b_j$. $a_k$'s neighbors: $u, b_k$. Common: just $u$. Good.

Take triple $\{u, a_i, b_i\}$. Common neighbors: must be adjacent to $u$, $a_i$, $b_i$. Adjacent to $u$: all other vertices. Adjacent to $a_i$: $u, b_i$. Adjacent to $b_i$: $u, a_i$. Common: need adjacent to $u$, $a_i$, $b_i$, and not in the triple. $b_i$ is adjacent to $u$ and $a_i$ but not to $b_i$ (itself). $a_i$ is adjacent to $u$ and $b_i$ but not to $a_i$ (itself). So no vertex outside the triple is adjacent to all three. Wait, that means zero common friends. Bad!

So the friendship graph doesn't work for $m = 3$.

Hmm. So $K_4$ might be the only option for $m = 3$? Let me think more carefully.

Actually, let me think about this more generally. Let me consider the problem from a design theory perspective.

The condition is: for every $m$-subset $S$, $|\bigcap_{v \in S} N(v)| = 1$.

Let $n$ be the total number of vertices. For each vertex $v$, let $d(v) = |N(v)|$ be its degree.

Consider the dual perspective. For each vertex $w$, let $F(w) = \{v : w \in N(v)\} = N(w)$ (since the graph is undirected). So $F(w) = N(w)$ is the set of friends of $w$, which is also the set of vertices that have $w$ as a friend.

The condition says: for every $m$-subset $S$ of vertices, there is exactly one $w$ with $S \subseteq N(w)$.

This is like a covering/packing condition. Think of it as: the collection $\{N(w) : w \in V\}$ is a family of subsets of $V$ such that every $m$-subset of $V$ is contained in exactly one member of the family.

But wait, $w \notin N(w)$ (no self-friendship), so $N(w) \subseteq V \setminus \{w\}$.

So we have a family of subsets $\mathcal{F} = \{N(w) : w \in V\}$ of $V$, where $N(w) \subseteq V \setminus \{w\}$, and every $m$-subset of $V$ is contained in exactly one $N(w)$.

This is related to a combinatorial design. Specifically, this is like a "covering" where every $m$-subset is covered exactly once.

If we think of the $N(w)$ as "blocks" and we want every $m$-subset to be in exactly one block, this is a Steiner system $S(m, k, n)$ where the blocks have varying sizes... no, Steiner systems have constant block size. Here the block sizes can vary.

But actually, the condition is that every $m$-subset is in exactly one block. If all blocks have the same size $k$, this would be a Steiner system $S(m, k, n)$.

But here, the blocks have varying sizes (the degrees vary), and additionally, block $N(w)$ doesn't contain $w$.

Let me count. The number of $m$-subsets is $\binom{n}{m}$. Each block $N(w)$ of size $d(w)$ covers $\binom{d(w)}{m}$ $m$-subsets. So:

$$\sum_{w \in V} \binom{d(w)}{m} = \binom{n}{m}$$

Also, for any $(m-1)$-subset $T$, the number of blocks containing $T$ is the number of common friends of $T$. Let's call this $\lambda(T)$. Then:

$$\sum_{w: T \subseteq N(w)} \binom{d(w) - (m-1)}{1} = \sum_{w: T \subseteq N(w)} (d(w) - m + 1)$$

Hmm, this is getting complicated. Let me think differently.

For any $(m-1)$-subset $T$, and any vertex $v \notin T$, the $m$-subset $T \cup \{v\}$ has exactly one common friend, say $w$. This $w$ is a common friend of $T$ and also a friend of $v$. So $w \in \bigcap_{t \in T} N(t) \cap N(v)$.

Actually, let me think about it this way. For any $(m-1)$-subset $T$, let $C(T) = \bigcap_{t \in T} N(t)$ be the set of common friends of $T$. For each $v \notin T$, $T \cup \{v\}$ has exactly one common friend, which is in $C(T) \cap N(v) \setminus (T \cup \{v\})$... wait, actually the common friend of $T \cup \{v\}$ is in $\bigcap_{t \in T} N(t) \cap N(v) = C(T) \cap N(v)$. And it's not in $T \cup \{v\}$ (since no one is their own friend, and the common friend must be a friend of everyone in the set, so it can't be in the set itself... actually, can it? If $w \in T \cup \{v\}$, then $w$ must be a friend of itself, which is impossible. So the common friend is not in $T \cup \{v\}$.)

So for each $v \notin T$, $|C(T) \cap N(v) \setminus (T \cup \{v\})| = 1$. But actually $C(T)$ already excludes elements of $T$ (since $C(T) = \bigcap_{t \in T} N(t)$ and $t \notin N(t)$, so $t \notin C(T)$). And $v \notin C(T)$ iff $v \notin N(t)$ for some $t \in T$... actually $v$ could be in $C(T)$. Let me be more careful.

$C(T) = \bigcap_{t \in T} N(t)$. This is the set of vertices adjacent to all of $T$. Note that elements of $T$ are not in $C(T)$ (since $t \notin N(t)$). But $v \notin T$ could be in $C(T)$.

For $v \notin T$, the common friend of $T \cup \{v\}$ is the unique element of $C(T) \cap N(v) \setminus \{v\}$ (we need it to not be $v$ itself, since $v \notin N(v)$, so actually $v \notin N(v)$ means $v \notin C(T) \cap N(v)$ automatically... wait, $v \in C(T)$ means $v$ is adjacent to all of $T$, and $v \in N(v)$ is impossible. So $v \notin N(v)$, hence $v \notin C(T) \cap N(v)$. So the common friend of $T \cup \{v\}$ is the unique element of $C(T) \cap N(v)$.)

So for each $v \notin T$, $|C(T) \cap N(v)| = 1$.

Now, this means: the sets $\{N(v) \cap C(T) : v \notin T\}$ each have exactly one element, and moreover, these elements partition... no, different $v$'s could map to the same common friend.

Actually, let me think of it as: $C(T)$ is a set, and for each $v \notin T$, $v$ is adjacent to exactly one element of $C(T)$. Also, elements of $C(T)$: for $w \in C(T)$, $w$ is adjacent to all of $T$, and $w$'s neighbors among $V \setminus T$ include those $v$ for which $w$ is the common friend of $T \cup \{v\}$.

Let $C(T) = \{c_1, c_2, \ldots, c_r\}$. Each $v \notin T$ is adjacent to exactly one $c_i$. So the $c_i$'s partition $V \setminus T$ into groups based on which $c_i$ they're adjacent to (within $C(T)$). But wait, $v$ could be adjacent to $c_i$ and also to other vertices, but the condition is only about adjacency to $C(T)$.

Actually, let me reconsider. For $v \notin T$, $|N(v) \cap C(T)| = 1$. This means each $v \notin T$ has exactly one neighbor in $C(T)$.

Now, what about elements of $C(T)$ themselves? If $c_i \in C(T)$, is $c_i \notin T$ (yes, since $C(T) \cap T = \emptyset$). So $c_i$ also has exactly one neighbor in $C(T)$. So within $C(T)$, each element has exactly one neighbor in $C(T)$. This means the induced subgraph on $C(T)$ is a perfect matching (each vertex has degree exactly 1 within $C(T)$). So $|C(T)| = r$ is even, and the induced subgraph is a matching.

Hmm, interesting. But also, each $c_i \in C(T)$ is adjacent to all of $T$ (by definition of $C(T)$). And each $c_i$ has exactly one neighbor in $C(T)$.

Now, the vertices in $V \setminus T \setminus C(T)$: each is adjacent to exactly one element of $C(T)$.

So the vertices of $C(T)$ partition $V \setminus T$ into "groups": $c_i$ is adjacent to some set of vertices in $V \setminus T$, and each vertex in $V \setminus T$ is adjacent to exactly one $c_i$. But $c_i$ is also in $V \setminus T$, and $c_i$ is adjacent to exactly one other $c_j$ in $C(T)$.

Let me define $A_i = \{v \notin T : v \text{ is adjacent to } c_i\} \setminus \{c_i\}$... hmm, this is getting complicated. Let me try a different approach.

Let me try to think about what happens when $T$ is an $(m-1)$-subset and consider the structure.

Actually, let me try small cases computationally (in my head) to get intuition.

**$m = 3$, $n = 4$: $K_4$.** Max degree 3. ✓

**$m = 3$, $n = 5$:** Is there a graph on 5 vertices where every 3 vertices have exactly one common neighbor?

Let the vertices be $1, 2, 3, 4, 5$. We need $\sum \binom{d_i}{3} = \binom{5}{3} = 10$.

Possible degree sequences (with $\sum \binom{d_i}{3} = 10$):
- All degrees 4: $5 \cdot \binom{4}{3} = 5 \cdot 4 = 20 \neq 10$. No.
- Degrees $(4, 4, 4, 4, 0)$: $4 \cdot 4 = 16 \neq 10$. No.
- Degrees $(4, 4, 3, 3, ?)$: $\binom{4}{3} + \binom{4}{3} + \binom{3}{3} + \binom{3}{3} = 4 + 4 + 1 + 1 = 10$. Need 5th vertex degree $d_5$ with $\binom{d_5}{3} = 0$, so $d_5 \leq 2$. Sum of degrees = $4 + 4 + 3 + 3 + d_5 = 14 + d_5$, must be even, so $d_5$ even. $d_5 \in \{0, 2\}$.

If $d_5 = 0$: vertex 5 is isolated. Then any triple containing 5 has no common friend (since 5 has no friends, no one is a friend of 5... wait, common friend of $\{5, a, b\}$ must be adjacent to 5, but 5 has no neighbors). So no common friend. Violates condition. So $d_5 \neq 0$.

If $d_5 = 2$: degrees $(4, 4, 3, 3, 2)$. Sum = 16, even. ✓ But vertex with degree 4 on 5 vertices means adjacent to all others. So vertices 1 and 2 (degree 4) are adjacent to all. Then for any triple $S$ not containing 1 or 2, both 1 and 2 are common friends, giving 2 common friends. But we need exactly 1. So this doesn't work unless every triple contains 1 or 2. With 5 vertices, triple $\{3, 4, 5\}$ doesn't contain 1 or 2. So 2 common friends. Violation.

So no graph on 5 vertices works for $m = 3$.

Let me check $n = 6, m = 3$. $\sum \binom{d_i}{3} = \binom{6}{3} = 20$.

Hmm, this is getting complex. Let me think about it more structurally.

Actually, let me reconsider. Maybe the answer is always $m$, achieved by $K_{m+1}$.

Let me check: is $K_{m+1}$ the unique solution? Or are there others?

For $K_{m+1}$: $n = m+1$, every vertex has degree $m$, every $m$-subset has exactly one common friend (the remaining vertex). Max degree = $m$.

Can we have $n > m+1$? Let me think about $m = 3$ and try $n = 6$ or higher.

Actually, let me think about this more carefully using the structure I derived.

For any $(m-1)$-subset $T$, $C(T) = \bigcap_{t \in T} N(t)$ has the property that the induced subgraph on $C(T)$ is a perfect matching, and every vertex in $V \setminus T$ has exactly one neighbor in $C(T)$.

For $m = 3$, $T$ is a pair $\{a, b\}$. $C(\{a,b\})$ is the set of common friends of $a$ and $b$. By the condition, for every $v \notin \{a, b\}$, $v$ has exactly one neighbor in $C(\{a,b\})$. And the induced subgraph on $C(\{a,b\})$ is a perfect matching.

Now, $|C(\{a,b\})| = $ number of common friends of $a$ and $b$. In $K_4$, $|C(\{a,b\})| = 2$ (the other two vertices), and they form a matching (they're adjacent to each other). ✓

Can we have $|C(\{a,b\})| = 4$ for some pair? Then $C(\{a,b\})$ is a matching of size 2 (4 vertices, 2 edges). And every other vertex has exactly one neighbor in $C(\{a,b\})$.

Let me try to build a graph with $m = 3$ and $n > 4$.

Let me try $n = 6$. Consider vertices $1, 2, 3, 4, 5, 6$.

$\sum \binom{d_i}{3} = \binom{6}{3} = 20$.

One possibility: all degrees equal to $d$. Then $6 \binom{d}{3} = 20$, so $\binom{d}{3} = 20/6$, not integer. So not regular.

Another: degrees $(5, 5, 4, 4, 4, 4)$: $2 \cdot 10 + 4 \cdot 4 = 20 + 16 = 36 \neq 20$.

Degrees $(5, 4, 4, 4, 4, 3)$: $10 + 4 \cdot 4 + 1 = 10 + 16 + 1 = 27 \neq 20$.

Degrees $(4, 4, 4, 4, 4, 4)$: $6 \cdot 4 = 24 \neq 20$.

Degrees $(5, 5, 5, 5, 0, 0)$: $4 \cdot 10 = 40 \neq 20$. And isolated vertices cause problems.

Degrees $(4, 4, 4, 4, 4, 0)$: $5 \cdot 4 = 20$. ✓ But vertex 6 isolated → triples containing 6 have no common friend. ✗

Degrees $(4, 4, 4, 4, 3, 3)$: $4 \cdot 4 + 2 \cdot 1 = 18 \neq 20$.

Degrees $(5, 4, 4, 4, 4, 1)$: $10 + 4 \cdot 4 + 0 = 26 \neq 20$.

Degrees $(5, 5, 4, 4, 2, 0)$: $10 + 10 + 4 + 4 + 0 + 0 = 28 \neq 20$.

Degrees $(5, 5, 3, 3, 3, 3)$: $10 + 10 + 4 \cdot 1 = 24 \neq 20$.

Degrees $(5, 3, 3, 3, 3, 3)$: $10 + 5 \cdot 1 = 15 \neq 20$.

Degrees $(5, 5, 5, 3, 2, 0)$: $30 + 1 = 31 \neq 20$.

Hmm, let me be more systematic. We need $\sum \binom{d_i}{3} = 20$ with $0 \leq d_i \leq 5$ and $\sum d_i$ even.

$\binom{d}{3}$ for $d = 0, 1, 2, 3, 4, 5$: $0, 0, 0, 1, 4, 10$.

We need 6 values from $\{0, 0, 0, 1, 4, 10\}$ summing to 20, with corresponding $d$ values summing to even.

Options:
- $10 + 10 + 0 + 0 + 0 + 0 = 20$: degrees $(5, 5, ?, ?, ?, ?)$ with four degrees $\leq 2$. Sum of degrees $\geq 10$, need even. E.g., $(5, 5, 2, 2, 2, 2)$: sum = 18, even. ✓ But two vertices of degree 5 (adjacent to all) means every triple has at least 2 common friends (both degree-5 vertices). ✗ (Unless the triple contains both, but even then...) Actually if both are in the triple, they need a common friend adjacent to both, which could be unique. But a triple not containing either has 2 common friends. ✗

- $10 + 4 + 4 + 1 + 1 + 0 = 20$: degrees $(5, 4, 4, 3, 3, \leq 2)$. Sum = $5 + 4 + 4 + 3 + 3 + d_6 = 19 + d_6$, need even, so $d_6$ odd. $d_6 \in \{1\}$ (since $\leq 2$ and odd). Sum = 20. ✓ But vertex with degree 5 is adjacent to all. Any triple not containing this vertex has it as a common friend. Need exactly one, so no other common friend. The degree-1 vertex has one friend. If a triple contains the degree-1 vertex, the common friend must be adjacent to it, so must be its unique friend. This is very restrictive.

Let me check: vertex 6 has degree 1, say adjacent to vertex 1. Vertex 1 has degree 5, adjacent to all. Triple $\{6, 2, 3\}$: common friend must be adjacent to 6 (so must be vertex 1), to 2, and to 3. Vertex 1 is adjacent to all, so it's a common friend. Is there another? Any other common friend must be adjacent to 6, but 6's only friend is 1. So only vertex 1. ✓

Triple $\{6, 1, 2\}$: common friend adjacent to 6 (must be 1), but 1 is in the triple. So no common friend from vertex 1's side... wait, the common friend must be adjacent to 6, 1, and 2. Adjacent to 6 means it's vertex 1. But 1 is in the triple, and 1 is not adjacent to itself. So no common friend. ✗!

So this doesn't work. The degree-1 vertex causes problems when it's in a triple with its only friend.

So any vertex with degree $< m-1 = 2$ causes problems? If a vertex $v$ has degree $d(v) < m-1$, then we can find an $(m-1)$-subset of $V \setminus \{v\}$ that doesn't include any friend of $v$... actually, we need to be more careful.

If $v$ has degree $d$ and $d < m-1$: take $T = \{v\} \cup S$ where $S$ is an $(m-1)$-subset of $V \setminus (\{v\} \cup N(v))$. This requires $|V \setminus (\{v\} \cup N(v))| \geq m-1$, i.e., $n - 1 - d \geq m - 1$, i.e., $n \geq m + d$. If this holds, then the common friend of $T$ must be adjacent to $v$, but also adjacent to all of $S$, none of which are friends of $v$. The common friend is in $N(v) \cap \bigcap_{s \in S} N(s)$. This could be non-empty. Hmm, this doesn't immediately give a contradiction.

Actually, the issue is more subtle. Let me think about it differently.

Let me go back to the structural result. For any $(m-1)$-subset $T$, $C(T)$ is a perfect matching, and every $v \notin T$ has exactly one neighbor in $C(T)$.

For $m = 3$, $|T| = 2$. Take $T = \{a, b\}$. $C(T)$ is a perfect matching. Every vertex not in $T$ has exactly one neighbor in $C(T)$.

In $K_4$ with vertices $\{1, 2, 3, 4\}$: $T = \{1, 2\}$, $C(T) = \{3, 4\}$, which is a matching (edge 3-4). Every vertex not in $T$ (i.e., 3, 4) has exactly one neighbor in $C(T)$: 3 is adjacent to 4, 4 is adjacent to 3. ✓

Now suppose $n = 6$ and we try to build such a graph. Take $T = \{1, 2\}$. $C(T) = \{c_1, c_2, c_3, c_4\}$ (must be even, perfect matching). Say matching is $(c_1, c_2), (c_3, c_4)$. Every vertex in $V \setminus \{1, 2\}$ has exactly one neighbor in $C(T)$.

The vertices in $V \setminus \{1, 2\}$ are $\{c_1, c_2, c_3, c_4, v_5\}$ where $v_5$ is the 5th vertex (if $n = 6$, vertices are $1, 2, c_1, c_2, c_3, c_4$... wait that's already 6). So $n = 6$ means $V = \{1, 2, c_1, c_2, c_3, c_4\}$, and $C(T) = \{c_1, c_2, c_3, c_4\}$, $|C(T)| = 4$.

Each $c_i$ has exactly one neighbor in $C(T)$ (the matching partner). Also, each $c_i$ is adjacent to both 1 and 2 (since $c_i \in C(\{1,2\})$).

So $c_1$ is adjacent to: $1, 2, c_2$ (and possibly others, but within $C(T)$ only $c_2$). So $d(c_1) \geq 3$.

Now consider $T' = \{c_1, c_2\}$. They are adjacent (matching partner). $C(T') = $ common friends of $c_1$ and $c_2$. $c_1$ is adjacent to $1, 2, c_2$ (at least). $c_2$ is adjacent to $1, 2, c_1$ (at least). So $1, 2 \in C(T')$. Also, are there others? $c_3, c_4$ are adjacent to each other but are they adjacent to $c_1$ and $c_2$? Within $C(T)$, $c_3$ is only adjacent to $c_4$ (matching). So $c_3$ is not adjacent to $c_1$ or $c_2$ (within $C(T)$, each vertex has exactly one neighbor). So $c_3 \notin C(T')$ and $c_4 \notin C(T')$. So $C(T') \supseteq \{1, 2\}$ and $|C(T')|$ is even (perfect matching). So $|C(T')| \in \{2, 4, \ldots\}$.

If $|C(T')| = 2$, then $C(T') = \{1, 2\}$, and $\{1, 2\}$ must be a matching, i.e., 1 and 2 are adjacent. 

If $|C(T')| = 4$, then there are 2 more common friends, but we said $c_3, c_4 \notin C(T')$. So the only vertices are $\{1, 2, c_1, c_2, c_3, c_4\}$, and $c_1, c_2 \notin C(T')$ (they're in $T'$). So $C(T') \subseteq \{1, 2, c_3, c_4\}$. We need $c_3, c_4$ to be common friends of $c_1, c_2$, meaning $c_3$ adjacent to both $c_1$ and $c_2$. But $c_3$'s only neighbor in $C(T)$ is $c_4$. So $c_3$ is not adjacent to $c_1$ or $c_2$. So $c_3 \notin C(T')$. Similarly $c_4 \notin C(T')$. So $C(T') = \{1, 2\}$, $|C(T')| = 2$. ✓ (matching requires 1-2 edge).

So 1 and 2 must be adjacent. Good.

Now, $C(T') = \{1, 2\}$, and every vertex not in $T' = \{c_1, c_2\}$ has exactly one neighbor in $\{1, 2\}$. The vertices not in $T'$ are $\{1, 2, c_3, c_4\}$. 
- 1's neighbors in $\{1, 2\}$: 1 is not adjacent to itself, so must be adjacent to 2. ✓ (we just established 1-2 edge).
- 2's neighbors in $\{1, 2\}$: adjacent to 1. ✓
- $c_3$'s neighbor in $\{1, 2\}$: exactly one of 1, 2.
- $c_4$'s neighbor in $\{1, 2\}$: exactly one of 1, 2.

Now, recall $c_3, c_4 \in C(\{1, 2\})$, so they're adjacent to both 1 and 2. But we just said $c_3$ has exactly one neighbor in $\{1, 2\}$. Contradiction! $c_3$ is adjacent to both 1 and 2 (since $c_3 \in C(\{1,2\})$), but must have exactly one neighbor in $\{1, 2\}$ (from $C(T')$ condition). 

So $|C(T)| = 4$ with $n = 6$ leads to a contradiction. So $|C(T)| \neq 4$ when $n = 6$.

What about $|C(T)| = 2$? Then $C(\{1,2\}) = \{c_1, c_2\}$, and $V = \{1, 2, c_1, c_2, v_5, v_6\}$. Every vertex not in $\{1, 2\}$ has exactly one neighbor in $\{c_1, c_2\}$. 

$c_1, c_2$ are adjacent to each other (matching) and to both 1 and 2. So $d(c_1) \geq 3$, $d(c_2) \geq 3$.

$v_5$ has exactly one neighbor in $\{c_1, c_2\}$, say $c_1$. $v_6$ has exactly one neighbor in $\{c_1, c_2\}$, say $c_2$ (or $c_1$).

Now consider $T'' = \{c_1, c_2\}$. $C(T'') \supseteq \{1, 2\}$ (since both are adjacent to $c_1$ and $c_2$). $|C(T'')|$ is even. $C(T'') \subseteq V \setminus \{c_1, c_2\} = \{1, 2, v_5, v_6\}$. 

$v_5$ is adjacent to $c_1$ (by assumption) but is $v_5$ adjacent to $c_2$? $v_5$ has exactly one neighbor in $\{c_1, c_2\}$, which is $c_1$. So $v_5$ is not adjacent to $c_2$. So $v_5 \notin C(T'')$. Similarly, if $v_6$'s neighbor in $\{c_1, c_2\}$ is $c_2$, then $v_6$ is not adjacent to $c_1$, so $v_6 \notin C(T'')$. If $v_6$'s neighbor is $c_1$, then $v_6$ is not adjacent to $c_2$, so $v_6 \notin C(T'')$.

So $C(T'') = \{1, 2\}$, $|C(T'')| = 2$. ✓ Matching: 1-2 edge required. So 1 and 2 are adjacent.

Every vertex not in $\{c_1, c_2\}$ has exactly one neighbor in $\{1, 2\}$. Vertices: $\{1, 2, v_5, v_6\}$.
- 1: adjacent to 2 (✓, one neighbor in $\{1,2\}$, which is 2).
- 2: adjacent to 1 (✓).
- $v_5$: exactly one neighbor in $\{1, 2\}$.
- $v_6$: exactly one neighbor in $\{1, 2\}$.

But $v_5$ is not adjacent to 1 or 2? We know $v_5$ is adjacent to $c_1$ (its neighbor in $C(\{1,2\})$). Is $v_5$ adjacent to 1 or 2? $v_5 \notin C(\{1,2\})$ means $v_5$ is not a common friend of 1 and 2, so $v_5$ is not adjacent to at least one of 1, 2. But $v_5$ could be adjacent to one of them.

From $C(T'')$: $v_5$ has exactly one neighbor in $\{1, 2\}$. So $v_5$ is adjacent to exactly one of 1, 2. Say $v_5$ is adjacent to 1 but not 2 (or vice versa).

Similarly $v_6$ is adjacent to exactly one of 1, 2.

Now let's think about what the graph looks like so far:
- 1-2 edge
- $c_1$-$c_2$ edge
- $c_1$ adjacent to 1, 2
- $c_2$ adjacent to 1, 2
- $v_5$ adjacent to $c_1$ (and exactly one of 1, 2)
- $v_6$ adjacent to exactly one of $c_1, c_2$ (and exactly one of 1, 2)

Let me also consider $T = \{1, c_1\}$. $C(\{1, c_1\})$ = common friends of 1 and $c_1$. 1 is adjacent to: 2, $c_1$, $c_2$ (at least), and possibly $v_5, v_6$. $c_1$ is adjacent to: 1, 2, $c_2$ (at least), and possibly $v_5, v_6$.

Common friends of 1 and $c_1$: vertices adjacent to both. 2 is adjacent to 1 (yes) and $c_1$ (yes). $c_2$ is adjacent to 1 (yes) and $c_1$ (yes). So $C(\{1, c_1\}) \supseteq \{2, c_2\}$. 

$|C(\{1, c_1\})|$ is even. $C(\{1, c_1\}) \subseteq V \setminus \{1, c_1\} = \{2, c_2, v_5, v_6\}$.

Is $v_5 \in C(\{1, c_1\})$? $v_5$ is adjacent to $c_1$ (yes). Is $v_5$ adjacent to 1? Depends on our choice. If $v_5$ is adjacent to 1, then $v_5 \in C(\{1, c_1\})$. If not, then $v_5 \notin C(\{1, c_1\})$.

Case A: $v_5$ adjacent to 1. Then $v_5 \in C(\{1, c_1\})$, so $C(\{1, c_1\}) \supseteq \{2, c_2, v_5\}$. But $|C|$ must be even, so $|C| \geq 4$, meaning $v_6 \in C$ too. So $v_6$ adjacent to both 1 and $c_1$. 

But $v_6$'s neighbor in $\{c_1, c_2\}$: if $v_6$ is adjacent to $c_1$, then $v_6$'s neighbor in $\{c_1, c_2\}$ is $c_1$ (exactly one). And $v_6$ adjacent to 1. So $v_6 \in C(\{1, c_1\})$. Then $C(\{1, c_1\}) = \{2, c_2, v_5, v_6\}$, $|C| = 4$. Matching: $(2, c_2)$ and $(v_5, v_6)$ must be edges. So 2-$c_2$ edge and $v_5$-$v_6$ edge.

Also, every vertex not in $\{1, c_1\}$ has exactly one neighbor in $C = \{2, c_2, v_5, v_6\}$. Vertices not in $\{1, c_1\}$: $\{2, c_2, v_5, v_6\}$ (these are the elements of $C$ themselves). Each has exactly one neighbor in $C$ (the matching partner). ✓ (2's neighbor is $c_2$, $c_2$'s neighbor is 2, $v_5$'s neighbor is $v_6$, $v_6$'s neighbor is $v_5$.) ✓

Now, $v_6$ is adjacent to $c_1$ (its neighbor in $\{c_1, c_2\}$). But wait, we said $v_6$'s neighbor in $\{c_1, c_2\}$ is exactly one. If $v_6$ is adjacent to $c_1$, then $v_6$ is not adjacent to $c_2$. Let's check: is $v_6$ adjacent to $c_2$? $v_6 \in C(\{1, c_1\})$ means $v_6$ is adjacent to 1 and $c_1$. $v_6$'s neighbor in $\{c_1, c_2\}$ is $c_1$ (exactly one), so $v_6$ not adjacent to $c_2$. ✓

Now let's also check $v_5$'s neighbor in $\{c_1, c_2\}$: $v_5$ is adjacent to $c_1$ (yes), not to $c_2$ (since exactly one neighbor in $\{c_1, c_2\}$). ✓

Now, $v_5$ is adjacent to 1 (by assumption in Case A). $v_5$'s neighbor in $\{1, 2\}$: exactly one, which is 1. So $v_5$ not adjacent to 2. ✓

$v_6$'s neighbor in $\{1, 2\}$: exactly one. $v_6$ is adjacent to 1 (established). So $v_6$ not adjacent to 2. ✓

Now let me also check $T = \{2, c_1\}$. $C(\{2, c_1\})$ = common friends of 2 and $c_1$. 2 is adjacent to 1, $c_1$, $c_2$ (at least). $c_1$ is adjacent to 1, 2, $c_2$ (at least). Common: 1 (adj to 2 ✓, adj to $c_1$ ✓), $c_2$ (adj to 2 ✓, adj to $c_1$ ✓). So $C \supseteq \{1, c_2\}$. 

Is $v_5 \in C(\{2, c_1\})$? $v_5$ adjacent to $c_1$ (yes), $v_5$ adjacent to 2? No (established). So $v_5 \notin C$. 

Is $v_6 \in C(\{2, c_1\})$? $v_6$ adjacent to $c_1$ (yes), $v_6$ adjacent to 2? No (established). So $v_6 \notin C$.

So $C(\{2, c_1\}) = \{1, c_2\}$, $|C| = 2$. ✓ Matching: 1-$c_2$ edge required. So 1 is adjacent to $c_2$. We already knew that ($c_2 \in C(\{1,2\})$ means $c_2$ adjacent to 1). ✓

Every vertex not in $\{2, c_1\}$ has exactly one neighbor in $\{1, c_2\}$. Vertices: $\{1, c_2, v_5, v_6\}$.
- 1: neighbor in $\{1, c_2\}$ is $c_2$ (1 not adj to itself). ✓ (1-$c_2$ edge exists)
- $c_2$: neighbor in $\{1, c_2\}$ is 1. ✓
- $v_5$: exactly one neighbor in $\{1, c_2\}$. $v_5$ adjacent to 1 (yes). $v_5$ adjacent to $c_2$? We need to check. $v_5$'s neighbors so far: $c_1$, 1, $v_6$. Is $v_5$ adjacent to $c_2$? If yes, then $v_5$ has 2 neighbors in $\{1, c_2\}$, violating the condition. If no, then $v_5$ has 1 neighbor in $\{1, c_2\}$ (which is 1). ✓ So $v_5$ not adjacent to $c_2$.
- $v_6$: exactly one neighbor in $\{1, c_2\}$. $v_6$ adjacent to 1 (yes). $v_6$ adjacent to $c_2$? If yes, 2 neighbors, bad. If no, 1 neighbor (1). ✓ So $v_6$ not adjacent to $c_2$.

Good. Now let me also check $T = \{1, c_2\}$. $C(\{1, c_2\})$ = common friends of 1 and $c_2$. 1 adjacent to: 2, $c_1$, $c_2$, $v_5$, $v_6$ (let me track: 1 is adjacent to 2 (yes), $c_1$ (yes, $c_1 \in C(\{1,2\})$), $c_2$ (yes), $v_5$ (yes, Case A), $v_6$ (yes)). So 1 is adjacent to everyone! $d(1) = 5$.

$c_2$ adjacent to: 1, 2, $c_1$ (yes, $c_1$-$c_2$ edge), and... $v_5$? No (just established). $v_6$? No (just established). So $c_2$ adjacent to $\{1, 2, c_1\}$, $d(c_2) = 3$.

$C(\{1, c_2\})$: common friends of 1 and $c_2$. Must be adjacent to both 1 and $c_2$. 1 is adjacent to all, so $C(\{1, c_2\}) = N(c_2) \setminus \{1, c_2\} = \{2, c_1\}$ (since $c_2$ is adjacent to 1, 2, $c_1$, and 1 is in the set $\{1, c_2\}$ so excluded). Wait, $C(\{1, c_2\}) = N(1) \cap N(c_2) \setminus \{1, c_2\}$. $N(1) = \{2, c_1, c_2, v_5, v_6\}$, $N(c_2) = \{1, 2, c_1\}$. Intersection: $\{2, c_1\}$. Remove $\{1, c_2\}$: still $\{2, c_1\}$. So $C(\{1, c_2\}) = \{2, c_1\}$, $|C| = 2$. ✓ Matching: 2-$c_1$ edge. Is 2 adjacent to $c_1$? $c_1 \in C(\{1,2\})$ means $c_1$ adjacent to 2. ✓

Every vertex not in $\{1, c_2\}$ has exactly one neighbor in $\{2, c_1\}$. Vertices: $\{2, c_1, v_5, v_6\}$.
- 2: neighbor in $\{2, c_1\}$ is $c_1$ (2 not adj to itself). 2 adjacent to $c_1$? Yes. ✓
- $c_1$: neighbor in $\{2, c_1\}$ is 2. $c_1$ adjacent to 2? Yes. ✓
- $v_5$: neighbor in $\{2, c_1\}$: $v_5$ adjacent to $c_1$ (yes), $v_5$ adjacent to 2 (no). So one neighbor ($c_1$). ✓
- $v_6$: neighbor in $\{2, c_1\}$: $v_6$ adjacent to $c_1$ (yes), $v_6$ adjacent to 2 (no). So one neighbor ($c_1$). ✓

Now let me check $T = \{v_5, v_6\}$. $v_5$ adjacent to: $c_1$, 1, $v_6$. $v_6$ adjacent to: $c_1$, 1, $v_5$. 

$C(\{v_5, v_6\}) = N(v_5) \cap N(v_6) \setminus \{v_5, v_6\}$. $N(v_5) = \{c_1, 1, v_6\}$, $N(v_6) = \{c_1, 1, v_5\}$. Intersection: $\{c_1, 1\}$. Remove $\{v_5, v_6\}$: $\{c_1, 1\}$. So $C = \{c_1, 1\}$, $|C| = 2$. ✓ Matching: $c_1$-1 edge. $c_1$ adjacent to 1? Yes. ✓

Every vertex not in $\{v_5, v_6\}$ has exactly one neighbor in $\{c_1, 1\}$. Vertices: $\{1, 2, c_1, c_2\}$.
- 1: neighbor in $\{c_1, 1\}$ is $c_1$ (1 not adj to itself). 1 adjacent to $c_1$? Yes. ✓
- $c_1$: neighbor in $\{c_1, 1\}$ is 1. ✓
- 2: neighbor in $\{c_1, 1\}$: 2 adjacent to 1 (yes), 2 adjacent to $c_1$ (yes). That's 2 neighbors! ✗

Contradiction! 2 is adjacent to both 1 and $c_1$, but should have exactly one neighbor in $\{c_1, 1\}$.

So Case A leads to a contradiction. Let me try Case B.

Case B: $v_5$ not adjacent to 1, so $v_5$ adjacent to 2 (its one neighbor in $\{1, 2\}$). And $v_5$ adjacent to $c_1$ (its neighbor in $\{c_1, c_2\}$).

Similarly, $v_6$ has one neighbor in $\{c_1, c_2\}$ and one in $\{1, 2\}$.

Sub-case B1: $v_6$ adjacent to $c_1$ (same as $v_5$) and adjacent to 2.
Sub-case B2: $v_6$ adjacent to $c_2$ and adjacent to... 1 or 2.

Let me try B1: both $v_5, v_6$ adjacent to $c_1$ and 2.

$T = \{1, c_1\}$. $C(\{1, c_1\})$: $N(1) \cap N(c_1) \setminus \{1, c_1\}$. 

$N(1)$: 1 is adjacent to 2, $c_1$, $c_2$ (at least). Is 1 adjacent to $v_5$? No (Case B). $v_6$? Let's say no for now. So $N(1) = \{2, c_1, c_2\}$, $d(1) = 3$.

$N(c_1)$: $c_1$ adjacent to 1, 2, $c_2$, $v_5$, $v_6$. So $d(c_1) = 5$.

$C(\{1, c_1\}) = \{2, c_2, v_5, v_6\} \cap \{2, c_1, c_2\} \setminus \{1, c_1\} = \{2, c_2\}$. $|C| = 2$. ✓ Matching: 2-$c_2$ edge. 2 adjacent to $c_2$? $c_2 \in C(\{1,2\})$ means $c_2$ adjacent to 2. ✓

Every vertex not in $\{1, c_1\}$ has exactly one neighbor in $\{2, c_2\}$. Vertices: $\{2, c_2, v_5, v_6\}$.
- 2: neighbor in $\{2, c_2\}$ is $c_2$. ✓
- $c_2$: neighbor in $\{2, c_2\}$ is 2. ✓
- $v_5$: neighbor in $\{2, c_2\}$: $v_5$ adjacent to 2 (yes), $v_5$ adjacent to $c_2$? If yes, 2 neighbors, bad. If no, 1 neighbor. So $v_5$ not adjacent to $c_2$.
- $v_6$: similarly, $v_6$ adjacent to 2 (yes), not to $c_2$.

Now $T = \{2, c_1\}$. $N(2) \cap N(c_1) \setminus \{2, c_1\}$. $N(2)$: 2 adjacent to 1, $c_1$, $c_2$, $v_5$, $v_6$. $d(2) = 5$. $N(c_1) = \{1, 2, c_2, v_5, v_6\}$. Intersection: $\{1, c_2, v_5, v_6\}$. Remove $\{2, c_1\}$: $\{1, c_2, v_5, v_6\}$. $|C| = 4$. ✓ Matching: need 2 edges among $\{1, c_2, v_5, v_6\}$. 

Every vertex not in $\{2, c_1\}$ has exactly one neighbor in $C = \{1, c_2, v_5, v_6\}$. Vertices: $\{1, c_2, v_5, v_6\}$ (these are the elements of $C$). Each has exactly one neighbor in $C$ (matching partner).

So we need a perfect matching on $\{1, c_2, v_5, v_6\}$. Options:
- $(1, c_2), (v_5, v_6)$: 1-$c_2$ edge (yes, exists), $v_5$-$v_6$ edge (need to add).
- $(1, v_5), (c_2, v_6)$: 1-$v_5$ edge? No (Case B). ✗
- $(1, v_6), (c_2, v_5)$: 1-$v_6$ edge? No. ✗

So matching is $(1, c_2), (v_5, v_6)$. Need $v_5$-$v_6$ edge.

Now $T = \{v_5, v_6\}$. $N(v_5) \cap N(v_6) \setminus \{v_5, v_6\}$. $N(v_5) = \{c_1, 2, v_6\}$, $N(v_6) = \{c_1, 2, v_5\}$. Intersection: $\{c_1, 2\}$. $|C| = 2$. ✓ Matching: $c_1$-2 edge. $c_1$ adjacent to 2? Yes. ✓

Every vertex not in $\{v_5, v_6\}$ has exactly one neighbor in $\{c_1, 2\}$. Vertices: $\{1, 2, c_1, c_2\}$.
- 1: neighbor in $\{c_1, 2\}$: 1 adjacent to $c_1$ (yes), 1 adjacent to 2 (yes). 2 neighbors! ✗

Contradiction again! 1 is adjacent to both $c_1$ and 2.

Hmm. So B1 also fails.

Let me try B2: $v_5$ adjacent to $c_1$ and 2; $v_6$ adjacent to $c_2$ and 1.

$T = \{1, 2\}$. $C(\{1,2\}) = \{c_1, c_2\}$ (established). Every vertex not in $\{1,2\}$ has exactly one neighbor in $\{c_1, c_2\}$.
- $c_1$: adjacent to $c_2$ (matching). ✓
- $c_2$: adjacent to $c_1$. ✓
- $v_5$: adjacent to $c_1$ (yes), not $c_2$. ✓
- $v_6$: adjacent to $c_2$ (yes), not $c_1$. ✓

$T = \{c_1, c_2\}$. $C(\{c_1, c_2\}) \supseteq \{1, 2\}$. $v_5$ adjacent to $c_1$ but not $c_2$, so $v_5 \notin C$. $v_6$ adjacent to $c_2$ but not $c_1$, so $v_6 \notin C$. $C = \{1, 2\}$, $|C| = 2$. ✓ Matching: 1-2 edge. ✓

Every vertex not in $\{c_1, c_2\}$ has exactly one neighbor in $\{1, 2\}$.
- 1: adjacent to 2. ✓
- 2: adjacent to 1. ✓
- $v_5$: adjacent to 2 (yes), adjacent to 1 (no). ✓
- $v_6$: adjacent to 1 (yes), adjacent to 2 (no). ✓

$T = \{1, c_1\}$. $N(1) = \{2, c_1, c_2, v_6\}$ (1 adjacent to 2, $c_1$, $c_2$ (since $c_2 \in C(\{1,2\})$), $v_6$). $d(1) = 4$. $N(c_1) = \{1, 2, c_2, v_5\}$. $d(c_1) = 4$. 

$C(\{1, c_1\}) = N(1) \cap N(c_1) \setminus \{1, c_1\} = \{2, c_2, v_6\} \cap \{2, c_2, v_5\} = \{2, c_2\}$. $|C| = 2$. ✓ Matching: 2-$c_2$ edge. 2 adjacent to $c_2$? $c_2 \in C(\{1,2\})$ means $c_2$ adjacent to 2. ✓

Every vertex not in $\{1, c_1\}$ has exactly one neighbor in $\{2, c_2\}$.
- 2: adjacent to $c_2$. ✓
- $c_2$: adjacent to 2. ✓
- $v_5$: adjacent to 2 (yes), adjacent to $c_2$? Need to check. If $v_5$ adjacent to $c_2$, then 2 neighbors, bad. So $v_5$ not adjacent to $c_2$. ✓ (We'll verify this is consistent.)
- $v_6$: adjacent to $c_2$ (yes), adjacent to 2? If yes, 2 neighbors, bad. So $v_6$ not adjacent to 2. ✓

$T = \{2, c_1\}$. $N(2) = \{1, c_1, c_2, v_5\}$. $d(2) = 4$. $N(c_1) = \{1, 2, c_2, v_5\}$. $d(c_1) = 4$.

$C(\{2, c_1\}) = \{1, c_2, v_5\} \cap \{1, c_2, v_5\} \setminus \{2, c_1\} = \{1, c_2, v_5\}$. $|C| = 3$. But $|C|$ must be even! ✗

Contradiction. So B2 also fails for this $T$.

Hmm. So $n = 6, m = 3$ seems impossible. Let me also check $T = \{1, c_2\}$ in B2.

$N(1) = \{2, c_1, c_2, v_6\}$, $N(c_2) = \{1, 2, c_1, v_6\}$. $C(\{1, c_2\}) = \{2, c_1, v_6\} \setminus \{1, c_2\} = \{2, c_1, v_6\}$. $|C| = 3$. Odd! ✗

So B2 fails. And we've shown B1 fails. And Case A fails. So with $|C(\{1,2\})| = 2$ and $n = 6$, we can't make it work either (at least in the cases we tried).

Wait, I think I need to be more careful. In B2, I found $C(\{2, c_1\}) = \{1, c_2, v_5\}$ with $|C| = 3$, which is odd, contradiction. So B2 is ruled out.

In B1, the contradiction was at $T = \{v_5, v_6\}$ where 1 had 2 neighbors in $C = \{c_1, 2\}$.

In Case A, the contradiction was at $T = \{v_5, v_6\}$ where 2 had 2 neighbors in $C = \{c_1, 1\}$.

Hmm, but I haven't tried all sub-cases. In Case B, $v_5$ is adjacent to 2 and $c_1$. $v_6$ could be adjacent to $c_1$ or $c_2$, and to 1 or 2. I tried ($c_1$, 2) [B1] and ($c_2$, 1) [B2]. Let me try ($c_1$, 1) and ($c_2$, 2).

B3: $v_5$ adj to $c_1$, 2. $v_6$ adj to $c_1$, 1.

$T = \{1, 2\}$, $C = \{c_1, c_2\}$. Every vertex not in $\{1,2\}$ has one neighbor in $\{c_1, c_2\}$.
- $v_5$: adj to $c_1$, not $c_2$. ✓
- $v_6$: adj to $c_1$, not $c_2$. ✓

$T = \{c_1, c_2\}$, $C = \{1, 2\}$ (since $v_5, v_6$ not adj to $c_2$). Every vertex not in $\{c_1, c_2\}$ has one neighbor in $\{1, 2\}$.
- $v_5$: adj to 2, not 1. ✓
- $v_6$: adj to 1, not 2. ✓

$T = \{1, c_1\}$. $N(1) = \{2, c_1, c_2, v_6\}$. $N(c_1) = \{1, 2, c_2, v_5, v_6\}$. $d(c_1) = 5$.
$C(\{1, c_1\}) = \{2, c_2, v_6\} \setminus \{1, c_1\} = \{2, c_2, v_6\}$. $|C| = 3$. Odd! ✗

B3 fails.

B4: $v_5$ adj to $c_1$, 2. $v_6$ adj to $c_2$, 2.

$T = \{1, 2\}$, $C = \{c_1, c_2\}$. $v_5$ adj $c_1$, $v_6$ adj $c_2$. ✓

$T = \{c_1, c_2\}$, $C = \{1, 2\}$. $v_5$ adj 2, $v_6$ adj 2. But every vertex not in $\{c_1, c_2\}$ must have exactly one neighbor in $\{1, 2\}$. $v_6$ adj to 2, not 1. ✓ $v_5$ adj to 2, not 1. ✓

$T = \{1, c_1\}$. $N(1) = \{2, c_1, c_2\}$ (1 not adj to $v_5$ or $v_6$). $d(1) = 3$. $N(c_1) = \{1, 2, c_2, v_5\}$. $d(c_1) = 4$.
$C(\{1, c_1\}) = \{2, c_2\}$. $|C| = 2$. ✓ Matching: 2-$c_2$ edge. ✓

Every vertex not in $\{1, c_1\}$ has one neighbor in $\{2, c_2\}$:
- 2: adj $c_2$. ✓
- $c_2$: adj 2. ✓
- $v_5$: adj 2 (yes), adj $c_2$? If yes, 2 neighbors. So $v_5$ not adj $c_2$. ✓
- $v_6$: adj $c_2$ (yes), adj 2 (yes). 2 neighbors! ✗

Contradiction. $v_6$ is adjacent to both 2 and $c_2$.

B4 fails.

So all sub-cases for $n = 6, m = 3$ with $|C(\{1,2\})| = 2$ fail. And $|C(\{1,2\})| = 4$ also failed. So $n = 6$ is impossible for $m = 3$.

This strongly suggests that $K_{m+1}$ is the unique solution, and the answer is $m$.

But let me think about whether there could be larger $n$ that works, or other structures.

Actually, let me think about this more generally. Let me consider the problem for general $m$.

**Claim: The only graph satisfying the condition is $K_{m+1}$, and the answer is $m$.**

Let me try to prove this. Suppose we have a graph $G$ on $n$ vertices where every $m$-subset has exactly one common neighbor.

**Step 1: Show $n \geq m + 1$.** We need at least $m+1$ vertices since we need a common friend for every $m$-subset, and the common friend is not in the subset.

Actually, we need $n \geq m + 1$ since for any $m$-subset, there's a common friend outside it.

**Step 2: Show $n = m + 1$.** 

Suppose $n \geq m + 2$. We'll derive a contradiction.

Consider any $m$-subset $S$. It has a unique common friend $f(S) \notin S$. 

Consider any $(m-1)$-subset $T$. As I showed, $C(T) = \bigcap_{t \in T} N(t)$ forms a perfect matching, and every vertex $v \notin T$ has exactly one neighbor in $C(T)$.

Since $n \geq m + 2$, $|V \setminus T| = n - m + 1 \geq 3$. And $|C(T)| \geq 2$ (it's a perfect matching, so even and $\geq 2$).

Now, consider two vertices $u, v \notin T$ that are matched to the same $c \in C(T)$... wait, no. Each vertex in $V \setminus T$ has exactly one neighbor in $C(T)$, but multiple vertices can share the same neighbor in $C(T)$.

Hmm, let me think differently. 

Let me use a counting argument. We have $\sum_{v} \binom{d(v)}{m} = \binom{n}{m}$.

Also, for any $(m-1)$-subset $T$, $\sum_{v: T \subseteq N(v)} (d(v) - m + 1) = n - m + 1$... wait, let me think about this.

For $(m-1)$-subset $T$, every $v \notin T$ has exactly one neighbor in $C(T)$. The vertices in $C(T)$ are the common friends of $T$, i.e., $\{w : T \subseteq N(w)\}$. For each $v \notin T$, $v$ is adjacent to exactly one element of $C(T)$. 

Now, $\sum_{w \in C(T)} |N(w) \setminus T| = \sum_{w \in C(T)} d(w) - (m-1)$ (since each $w \in C(T)$ is adjacent to all $m-1$ vertices of $T$). But also, $\sum_{w \in C(T)} |N(w) \cap (V \setminus T)| = |V \setminus T| = n - m + 1$ (since each vertex in $V \setminus T$ is adjacent to exactly one $w \in C(T)$, and each $w \in C(T)$ is in $V \setminus T$ and adjacent to exactly one other element of $C(T)$).

Wait, let me be more careful. $V \setminus T$ includes elements of $C(T)$ and elements not in $C(T)$. Each element of $V \setminus T$ has exactly one neighbor in $C(T)$. So:

$\sum_{w \in C(T)} |N(w) \cap (V \setminus T)| = |V \setminus T| = n - m + 1$

But $|N(w) \cap (V \setminus T)| = d(w) - |N(w) \cap T| = d(w) - (m-1)$ (since $w \in C(T)$ means $w$ is adjacent to all of $T$, so $|N(w) \cap T| = m - 1$).

So $\sum_{w \in C(T)} (d(w) - m + 1) = n - m + 1$.

Let $|C(T)| = r$. Then $\sum_{w \in C(T)} d(w) = n - m + 1 + r(m-1) = n - 1 + r(m - 2)$.

Hmm, this is a relation but I'm not sure it directly helps.

Let me try another approach. Let me consider the "dual" structure.

For each vertex $v$, $N(v)$ is a subset of $V \setminus \{v\}$. The condition is that every $m$-subset is contained in exactly one $N(v)$. 

This is exactly the definition of a **Steiner system** $S(m, \cdot, n)$ with variable block sizes, where the blocks are $\{N(v) : v \in V\}$ and block $N(v)$ doesn't contain $v$.

In a Steiner system $S(t, k, n)$ with constant block size $k$, we have Fisher's inequality: $b \geq n$ (number of blocks $\geq$ number of points). Here $b = n$ (one block per vertex), so Fisher's inequality is tight, which happens for symmetric designs.

But our blocks have variable sizes. Let me think about whether we can use a Fisher-type inequality.

Actually, in our case, the number of blocks equals the number of points ($n$), and every $m$-subset is in exactly one block. This is a very strong condition.

Let me think about $m = 2$ first (even though the problem says $m \geq 3$). For $m = 2$: every pair has exactly one common friend. This is the friendship theorem condition (well, almost—the friendship theorem says every pair has exactly one common neighbor, and the conclusion is the windmill graph). The windmill graph $F_k$ has $2k+1$ vertices, and the universal vertex has degree $2k$. So for $m = 2$, the answer would be $2k$ which is unbounded. But the problem says $m \geq 3$.

So the condition for $m \geq 3$ is much more restrictive. Let me think about why.

For $m = 2$, the windmill graph works: every pair has exactly one common friend. But for $m = 3$, we need every triple to have exactly one common friend, which is much stronger.

Let me try to prove $n = m + 1$ for $m \geq 3$.

**Approach: Show that if $n \geq m + 2$, we get a contradiction.**

Suppose $n \geq m + 2$. Take any $m$-subset $S$ with common friend $f = f(S)$. Now, $f \notin S$ and $f$ is adjacent to all of $S$. Consider any $v \in V \setminus (S \cup \{f\})$ (this exists since $n \geq m + 2$).

Consider the $m$-subset $S' = (S \setminus \{s\}) \cup \{v\}$ for some $s \in S$. This has a unique common friend $f' = f(S')$.

$f'$ is adjacent to all of $S \setminus \{s\}$ and to $v$. 

Now, $f$ is adjacent to all of $S \setminus \{s\}$ (since $f$ is adjacent to all of $S$). Is $f$ adjacent to $v$? Not necessarily.

If $f$ is adjacent to $v$, then $f$ is a common friend of $S'$, so $f' = f$ (by uniqueness). But $f$ is not adjacent to $s$... wait, $f$ IS adjacent to $s$ (since $f$ is the common friend of $S$). But $s \notin S'$, so that's fine. $f$ is adjacent to all of $S' = (S \setminus \{s\}) \cup \{v\}$ iff $f$ is adjacent to $v$. If so, $f' = f$.

If $f$ is not adjacent to $v$, then $f' \neq f$, and $f'$ is adjacent to all of $S \setminus \{s\}$ and $v$.

This is getting complicated. Let me try a different approach.

**Approach via the structure of $C(T)$.**

For any $(m-1)$-subset $T$, $C(T)$ is a perfect matching and every $v \notin T$ has exactly one neighbor in $C(T)$.

Let $|C(T)| = 2r$ (even). The matching pairs up $C(T)$ into $r$ pairs. Each $v \notin T$ is adjacent to exactly one element of $C(T)$.

Now, the elements of $C(T)$ themselves are in $V \setminus T$, and each has exactly one neighbor in $C(T)$ (its matching partner). So the $n - m + 1$ vertices in $V \setminus T$ are partitioned by which element of $C(T)$ they're adjacent to. The $2r$ elements of $C(T)$ are each adjacent to their matching partner (within $C(T)$), so they form $r$ pairs. The remaining $n - m + 1 - 2r$ vertices (not in $C(T)$, not in $T$) are each adjacent to exactly one element of $C(T)$.

Now, consider two elements $c, c'$ of $C(T)$ that are matching partners (i.e., adjacent). Consider the $m$-subset $T \cup \{c\}$. Its unique common friend is... the common friend must be adjacent to all of $T$ (so in $C(T)$) and adjacent to $c$. Within $C(T)$, $c$'s only neighbor is $c'$. So the common friend of $T \cup \{c\}$ is $c'$. Similarly, common friend of $T \cup \{c'\}$ is $c$.

Now consider $T \cup \{v\}$ for $v \notin T, v \notin C(T)$. $v$'s unique neighbor in $C(T)$ is some $c_v$. The common friend of $T \cup \{v\}$ is $c_v$.

Now, here's a key observation. Take $T$ to be an $(m-1)$-subset, and consider $c \in C(T)$ with matching partner $c'$. We have $c$ adjacent to all of $T$ and to $c'$. Also, $c$ is adjacent to some vertices outside $T \cup C(T)$ (those $v$ with $c_v = c$).

Now consider a different $(m-1)$-subset $T'$. Let me try to use two different $(m-1)$-subsets to derive constraints.

Actually, let me try a cleaner approach. Let me consider the case $m = 3$ and try to prove $n = 4$ directly, then generalize.

For $m = 3$, $T$ is a pair. $C(T)$ is a perfect matching. Let me pick $T = \{a, b\}$ and $C(T) = \{c_1, c_2, \ldots, c_{2r}\}$ with matching $(c_1, c_2), (c_3, c_4), \ldots$

Every vertex $v \notin \{a, b\}$ has exactly one neighbor in $C(T)$.

Now, $c_1$ is adjacent to $a, b, c_2$, and possibly others. $c_2$ is adjacent to $a, b, c_1$, and possibly others.

Consider $T' = \{a, c_1\}$. $C(T')$ = common friends of $a$ and $c_1$. $a$ is adjacent to all of $C(T)$ (since $C(T) = N(a) \cap N(b)$, so $a$ is adjacent to $c_1, c_2, \ldots$). Wait, $C(T) = N(a) \cap N(b)$, so $c_i \in N(a)$ and $c_i \in N(b)$. So $a$ is adjacent to all $c_i$.

$c_1$ is adjacent to $a, b, c_2$ (at least). 

$C(T') = N(a) \cap N(c_1) \setminus \{a, c_1\}$. $N(a)$ includes $b$ and all $c_i$ (and possibly others). $N(c_1)$ includes $a, b, c_2$ (and possibly others). 

Common: $b$ (in $N(a)$? yes; in $N(c_1)$? yes), $c_2$ (in $N(a)$? yes; in $N(c_1)$? yes). Other $c_i$ ($i \geq 3$): in $N(a)$? yes; in $N(c_1)$? $c_1$'s only neighbor in $C(T)$ is $c_2$, so $c_1$ is not adjacent to $c_i$ for $i \geq 3$. So $c_i \notin C(T')$ for $i \geq 3$.

So $C(T') \supseteq \{b, c_2\}$, and $C(T') \subseteq V \setminus \{a, c_1\}$. The elements of $C(T')$ are common friends of $a$ and $c_1$.

Now, $|C(T')|$ must be even. If $C(T') = \{b, c_2\}$, then $b$ and $c_2$ must be adjacent (matching). 

Are there other elements? Vertices $v \notin T, v \notin C(T)$ (i.e., $v \notin \{a, b, c_1, \ldots, c_{2r}\}$): is $v \in C(T')$? $v \in N(a)$? Not necessarily. $v \in N(c_1)$? $v$'s neighbor in $C(T)$ is some $c_j$. If $c_j = c_1$, then $v$ is adjacent to $c_1$. And if $v$ is also adjacent to $a$, then $v \in C(T')$.

Hmm, this is getting complicated. Let me try to think about it more cleverly.

**Key idea:** Let me show that every pair of vertices is adjacent. If the graph is complete, then $n = m + 1$ (since in $K_n$, every $m$-subset has $n - m$ common friends, and we need exactly 1, so $n = m + 1$).

So I want to show the graph is complete.

Suppose not. Then there exist non-adjacent vertices $a, b$. Consider $T = \{a, b\}$ (for $m = 3$; for general $m$, I'd need $T$ to be an $(m-1)$-subset containing $a$ and $b$, but let me first handle $m = 3$).

$C(\{a, b\}) = N(a) \cap N(b) \setminus \{a, b\}$. Since $a, b$ are not adjacent, $a \notin N(b)$ and $b \notin N(a)$, so $C(\{a, b\}) = N(a) \cap N(b)$.

$|C(\{a, b\})| = 2r$ for some $r \geq 1$ (since it's a perfect matching, and must be non-empty because any triple containing $a, b$ needs a common friend).

Every vertex $v \notin \{a, b\}$ has exactly one neighbor in $C(\{a, b\})$.

Now, $a$ is adjacent to all of $C(\{a, b\})$ (by definition). $b$ is also adjacent to all of $C(\{a, b\})$.

But $a \notin \{a, b\}$... $a$ is in $\{a, b\}$, so the condition "every $v \notin \{a, b\}$ has exactly one neighbor in $C$" applies to vertices other than $a, b$. 

The vertices in $C(\{a, b\})$ are each adjacent to both $a$ and $b$. Within $C$, they form a matching. Each vertex in $C$ has exactly one neighbor in $C$ (its matching partner).

Each vertex $v \notin \{a, b\} \cup C$ has exactly one neighbor in $C$.

Now, consider $c_1 \in C$ with matching partner $c_2 \in C$. $c_1$ is adjacent to $a, b, c_2$. 

Consider the triple $\{a, b, c_1\}$. Common friend: must be adjacent to $a, b, c_1$. In $C$, the only vertex adjacent to $c_1$ is $c_2$. And $c_2$ is adjacent to $a$ and $b$. So $c_2$ is the common friend. ✓ (exactly one, since no other vertex in $C$ is adjacent to $c_1$, and vertices outside $C$ are not adjacent to both $a$ and $b$... wait, are they? A vertex $v \notin \{a, b\} \cup C$ is not in $C = N(a) \cap N(b)$, so $v$ is not adjacent to $a$ or not adjacent to $b$. So $v$ can't be a common friend of $\{a, b, c_1\}$. ✓)

Now consider the triple $\{a, c_1, c_2\}$. Common friend: adjacent to $a, c_1, c_2$. $b$ is adjacent to $a$? No! $a$ and $b$ are not adjacent. So $b$ is not a common friend. 

In $C$: who is adjacent to both $c_1$ and $c_2$? $c_1$'s only neighbor in $C$ is $c_2$, and $c_2$'s only neighbor in $C$ is $c_1$. So no other vertex in $C$ is adjacent to both. $c_1$ and $c_2$ are adjacent to each other, but $c_1$ is not adjacent to itself, and $c_2$ is not adjacent to itself.

Outside $C \cup \{a, b\}$: a vertex $v$ adjacent to $a$ and to both $c_1, c_2$. $v$'s neighbor in $C$ is exactly one of $c_1, c_2$ (say $c_1$). Then $v$ is adjacent to $c_1$ but not $c_2$ (since $v$ has exactly one neighbor in $C$). So $v$ is not adjacent to $c_2$, hence not a common friend.

So the common friend of $\{a, c_1, c_2\}$ must be adjacent to $a, c_1, c_2$. We've ruled out $b$, all of $C \setminus \{c_1, c_2\}$, and all of $V \setminus (C \cup \{a, b\})$. The only remaining candidates are $c_1$ and $c_2$ themselves, but they're in the triple. So there's no common friend! 

This is a contradiction (we need exactly one common friend). 

Wait, let me double-check. The common friend of $\{a, c_1, c_2\}$ must be a vertex $w \notin \{a, c_1, c_2\}$ with $w$ adjacent to $a$, $c_1$, and $c_2$.

- $b$: adjacent to $c_1$ (yes), $c_2$ (yes), $a$ (no, since $a, b$ non-adjacent). ✗
- $c_i \in C, i \geq 3$: adjacent to $a$ (yes), $c_1$ (no, only $c_2$ is adj to $c_1$ in $C$). ✗
- $v \notin C \cup \{a, b\}$: adjacent to $a$? Maybe. Adjacent to $c_1$? Only if $c_1$ is $v$'s neighbor in $C$. Adjacent to $c_2$? Only if $c_2$ is $v$'s neighbor in $C$. But $v$ has exactly one neighbor in $C$, so can't be adjacent to both $c_1$ and $c_2$. ✗

So no common friend exists for $\{a, c_1, c_2\}$. Contradiction!

Therefore, for $m = 3$, there cannot be non-adjacent vertices. The graph must be complete, hence $K_n$ with $n = m + 1 = 4$, and the max degree is $m = 3$.

Now let me generalize to $m \geq 3$.

**General case:** Suppose $G$ is a graph on $n$ vertices where every $m$-subset has exactly one common neighbor. Suppose $n \geq m + 2$ (we want to derive a contradiction, or more precisely, show the graph is complete).

Actually, let me try the same approach. Suppose there exist non-adjacent vertices $a, b$. 

Take an $(m-1)$-subset $T$ containing both $a$ and $b$ (possible since $m - 1 \geq 2$). $T = \{a, b, t_3, \ldots, t_{m-1}\}$.

$C(T) = \bigcap_{t \in T} N(t) \setminus T$. Since $a, b \in T$ and $a, b$ are not adjacent, $C(T) = \bigcap_{t \in T} N(t)$ (since $a \notin N(b)$ and $b \notin N(a)$, elements of $T$ are automatically excluded).

$|C(T)| = 2r$ for some $r \geq 1$. $C(T)$ is a perfect matching. Every $v \notin T$ has exactly one neighbor in $C(T)$.

Take $c_1, c_2 \in C(T)$ that are matching partners (adjacent). Both are adjacent to all of $T$ (including $a$ and $b$).

Now consider the $m$-subset $S = (T \setminus \{b\}) \cup \{c_1\} = \{a, t_3, \ldots, t_{m-1}, c_1\}$. This is an $m$-subset (we removed $b$ and added $c_1$). Its unique common friend $f$ must be adjacent to $a, t_3, \ldots, t_{m-1}, c_1$.

$f$ is adjacent to all of $T \setminus \{b\}$, so $f \in C(T \setminus \{b\})$ (common friends of $T \setminus \{b\}$). Also $f$ is adjacent to $c_1$.

Now, $c_2$ is adjacent to all of $T$ (hence all of $T \setminus \{b\}$) and to $c_1$ (matching partner). So $c_2$ is a common friend of $S$. By uniqueness, $f = c_2$.

Now consider the $m$-subset $S' = (T \setminus \{b\}) \cup \{c_2\} = \{a, t_3, \ldots, t_{m-1}, c_2\}$. By the same argument, its common friend is $c_1$.

Now consider the $m$-subset $S'' = (T \setminus \{a, b\}) \cup \{c_1, c_2\} = \{t_3, \ldots, t_{m-1}, c_1, c_2\}$. This has $m - 2 + 2 = m$ elements. ✓ Its common friend $f''$ must be adjacent to $t_3, \ldots, t_{m-1}, c_1, c_2$.

$f''$ is adjacent to all of $T \setminus \{a, b\} = \{t_3, \ldots, t_{m-1}\}$, and to $c_1$ and $c_2$.

Candidates:
- $a$: adjacent to $t_3, \ldots, t_{m-1}$ (yes, since $a \in T$ and... wait, $a$ is adjacent to $t_i$? $t_i \in T$ and $a \in T$, but we don't know if $a$ is adjacent to $t_i$). Hmm, actually $T$ is just a subset, not a clique. Let me reconsider.

Wait, I think I need to be more careful. $T$ is an $(m-1)$-subset, and $C(T) = \bigcap_{t \in T} N(t)$. The elements of $C(T)$ are adjacent to all elements of $T$. But elements of $T$ are not necessarily adjacent to each other.

So when I consider $S'' = \{t_3, \ldots, t_{m-1}, c_1, c_2\}$, the common friend must be adjacent to $t_3, \ldots, t_{m-1}$ (all of $T \setminus \{a, b\}$) and to $c_1, c_2$.

- $a$: adjacent to $t_3, \ldots, t_{m-1}$? Not necessarily. $a$ is in $T$, but $a$ might not be adjacent to other elements of $T$. Actually, we need $a$ to be adjacent to $t_i$ for $i = 3, \ldots, m-1$. We don't know this.

Hmm, so my approach of taking an arbitrary $(m-1)$-subset $T$ containing $a, b$ doesn't work directly because elements of $T$ might not be adjacent to each other.

Let me reconsider. Let me take $T$ to be an $(m-1)$-subset containing $a$ and $b$ where the other elements are chosen to be adjacent to both $a$ and $b$... but I don't know if such elements exist.

Actually, let me reconsider the $m = 3$ proof. There, $T = \{a, b\}$ and I used the triple $\{a, c_1, c_2\}$ where $c_1, c_2 \in C(\{a, b\})$ are matching partners. The key was that $c_1, c_2$ are both adjacent to $a$ (and $b$), and the common friend of $\{a, c_1, c_2\}$ had to be adjacent to $a, c_1, c_2$, and we showed no such vertex exists.

For general $m$, I need to find an $m$-subset whose common friend doesn't exist. Let me try:

Take $T = \{a, b, t_3, \ldots, t_{m-1}\}$ an $(m-1)$-subset with $a, b \in T$. Let $c_1, c_2 \in C(T)$ be matching partners.

Consider the $m$-subset $S = \{a, t_3, \ldots, t_{m-1}, c_1, c_2\} \setminus \{b\}$... wait, that's $T \setminus \{b\} \cup \{c_1, c_2\}$, which has $(m-1) - 1 + 2 = m$ elements. ✓

The common friend of $S$ must be adjacent to $a, t_3, \ldots, t_{m-1}, c_1, c_2$.

Now, $b$ is adjacent to $t_3, \ldots, t_{m-1}$? Not necessarily (since $T$ is not necessarily a clique).

Hmm, I'm stuck because $T$ is not a clique. Let me think differently.

Actually, in the $m = 3$ case, $T = \{a, b\}$ has only 2 elements, and the key point was that $b$ is not adjacent to $a$. For the triple $\{a, c_1, c_2\}$, we needed a common friend adjacent to $a, c_1, c_2$, and we showed $b$ fails because $b$ is not adjacent to $a$.

For general $m$, let me try the $m$-subset $\{a, c_1, c_2, t_4, \ldots, t_m\}$ where $t_4, \ldots, t_m$ are $m - 3$ additional vertices. But I need these to be chosen carefully.

Actually, let me try a different approach. Let me consider the $m$-subset $S = (T \setminus \{b\}) \cup \{c_1, c_2\}$ where $T = \{a, b, t_3, \ldots, t_{m-1}\}$ and $c_1, c_2 \in C(T)$ are matching partners.

$S = \{a, t_3, \ldots, t_{m-1}, c_1, c_2\}$, $|S| = 1 + (m-3) + 2 = m$. ✓

Common friend $f$ must be adjacent to all of $S$: $a, t_3, \ldots, t_{m-1}, c_1, c_2$.

Now, $f$ is adjacent to $c_1$ and $c_2$. Recall that within $C(T)$, $c_1$'s only neighbor is $c_2$ and vice versa. So if $f \in C(T)$, then $f$ is adjacent to $c_1$ only if $f = c_2$, and adjacent to $c_2$ only if $f = c_1$. But $f$ must be adjacent to both, which is impossible for $f \in C(T) \setminus \{c_1, c_2\}$ (since such $f$ is adjacent to neither $c_1$ nor $c_2$ within $C(T)$). And $f = c_1$ or $c_2$ is impossible since they're in $S$.

So $f \notin C(T)$. Also $f \notin T$ (since $f \notin S$ and $f$ must be adjacent to all of $S$, and elements of $S$ are not adjacent to themselves).

So $f \in V \setminus (T \cup C(T))$ (or $f \in C(T) \setminus \{c_1, c_2\}$, but we ruled that out).

Wait, I said $f \notin C(T)$. Let me re-examine. $f$ must be adjacent to $c_1$ and $c_2$. If $f \in C(T) \setminus \{c_1, c_2\}$, then $f$'s only neighbor in $C(T)$ is its matching partner, which is not $c_1$ or $c_2$ (since $c_1, c_2$ are matched to each other). So $f$ is not adjacent to $c_1$ or $c_2$. ✗

If $f \in V \setminus (T \cup C(T))$: $f$ has exactly one neighbor in $C(T)$, say $c_j$. If $c_j = c_1$, then $f$ is adjacent to $c_1$ but not $c_2$. If $c_j = c_2$, then $f$ is adjacent to $c_2$ but not $c_1$. Either way, $f$ is not adjacent to both $c_1$ and $c_2$. ✗

If $f = b$: $b$ is adjacent to $c_1$ (yes, since $c_1 \in C(T)$ means $c_1 \in N(b)$) and $c_2$ (yes). $b$ is adjacent to $a$? No (by assumption, $a, b$ non-adjacent). $b$ is adjacent to $t_3, \ldots, t_{m-1}$? $b \in T$ and $t_i \in T$, but $b$ might not be adjacent to $t_i$. Actually, $b$ is adjacent to $t_i$ iff $t_i \in N(b)$. We don't know this in general.

Hmm, so the issue is
