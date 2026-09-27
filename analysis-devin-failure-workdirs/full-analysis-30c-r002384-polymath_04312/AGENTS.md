# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Given an integer $d \ge 2$ and a circle $\omega$, a finite number of chords are drawn such that each end of each chord is an end of at least $d$ different drawn chords. We assume that chords with a common end intersect. Let $M$ be the maximum possible value such that for any such configuration of chords, there must exist a chord which intersects at least $M$ other chords. 

Find the value of $M$ when $d = 20$.       — 题目文本
#   The problem asks for the minimum possible value of the maximum number of intersections a chord can have. According to the original proof, for any integer $d$, there exists a chord that intersects at least $\lceil d^2/4 \rceil$ other chords if $d$ is even, or a slightly different value if $d$ is odd. Specifically, the proof concludes that for $d=2k$, the number of intersections is at least $k^2$ (as $\lceil (2k)^2/4 \rceil = k^2$). For $d=20$, $k=10$, so the number of intersections is $10^2 = 100$.  — 标准解答
#   Let me solve this problem. We have a circle with chords drawn such that each endpoint of each chord is an endpoint of at least $d$ different drawn chords. Chords with a common endpoint intersect. We need to find the maximum $M$ such that in any such configuration, some chord intersects at least $M$ others.

Let me think about this carefully.

First, let me set up the model. We have a set of points on a circle (the endpoints), and a set of chords (pairs of points). Each point that is used as an endpoint is an endpoint of at least $d$ chords. Two chords intersect if they share an endpoint OR if they cross in the interior of the circle.

Wait, let me re-read: "We assume that chords with a common end intersect." So chords sharing an endpoint count as intersecting. And chords that cross in the interior also intersect. So two chords intersect if they share an endpoint or cross inside the circle.

We want: for any configuration satisfying the degree condition (each used point has degree $\geq d$), there exists a chord intersecting at least $M$ other chords. Find the maximum such $M$ for $d = 20$.

So $M$ is the minimum over all valid configurations of the maximum number of chords intersecting a single chord. We want to find this minimum.

Let me think about this as a graph problem. The vertices are the points on the circle, edges are chords. This is a "circle graph" or more precisely the intersection graph of chords.

Actually, let me think of it differently. We have a graph $G$ whose vertices are points on a circle and whose edges are chords. The condition is: every vertex has degree $\geq d$. Two edges "intersect" if they share a vertex or cross inside the circle.

The intersection graph of the edges (chords) is what we care about. We want the minimum possible maximum degree of this intersection graph, over all such chord configurations.

Let me think about what determines whether two chords cross. If we label the points $1, 2, \ldots, n$ around the circle, two chords $(a,b)$ and $(c,d)$ with $a < b$ and $c < d$ cross iff exactly one of $c, d$ is in the interval $(a, b)$, i.e., $a < c < b < d$ or $c < a < d < b$.

So the number of chords that a given chord $(a, b)$ intersects equals:
- (number of chords sharing endpoint $a$ or $b$) + (number of chords crossing $(a,b)$ in the interior) - (chords sharing both endpoints, counted twice, but that's just the chord itself... no).

Actually, let me be careful. A chord $e = (a,b)$ intersects another chord $f$ if:
1. $f$ shares an endpoint with $e$ (i.e., $f$ is incident to $a$ or $b$), OR
2. $f$ crosses $e$ in the interior.

These are mutually exclusive for $f \neq e$ (if $f$ shares an endpoint with $e$, it doesn't cross in the interior; if it crosses in the interior, it doesn't share an endpoint).

So the number of chords intersecting $e = (a,b)$ is:
$$\deg(a) + \deg(b) - 2 + (\text{number of chords crossing } (a,b) \text{ in interior})$$

Wait, $\deg(a)$ counts all chords incident to $a$, including $e$ itself. So chords incident to $a$ other than $e$: $\deg(a) - 1$. Similarly for $b$. But a chord incident to both $a$ and $b$ would be $e$ itself (assuming no multi-edges). So the number of chords sharing an endpoint with $e$ is $(\deg(a) - 1) + (\deg(b) - 1) = \deg(a) + \deg(b) - 2$.

Plus the number of chords crossing $e$ in the interior.

Let me denote by $c(e)$ the number of chords crossing $e$ in the interior. Then the number of chords intersecting $e$ is:
$$I(e) = \deg(a) + \deg(b) - 2 + c(e)$$

Since $\deg(a) \geq d$ and $\deg(b) \geq d$, we have $I(e) \geq 2d - 2 + c(e) \geq 2d - 2$.

So $M \geq 2d - 2$. For $d = 20$, $M \geq 38$.

But can we always achieve $c(e) = 0$ for all chords? That would mean no two chords cross in the interior. This means the chord diagram is "non-crossing" — it's a planar graph on the circle, i.e., a triangulation-like structure or more generally a non-crossing matching/graph.

If we have a non-crossing set of chords where every vertex has degree exactly $d$, then $I(e) = 2d - 2$ for every chord, and $M = 2d - 2$.

But can we construct such a configuration? A non-crossing graph on $n$ points on a circle where every vertex has degree $d$.

A non-crossing graph on $n$ points on a circle is a planar graph. The maximum number of edges in a planar graph on $n$ vertices is $3n - 6$ (for $n \geq 3$). The sum of degrees is $2 \cdot |E| \leq 2(3n-6) = 6n - 12$. If every vertex has degree $\geq d$, then $nd \leq 6n - 12$, so $n(d-6) \leq -12$, which means $d \leq 6$ (for large $n$). Actually for $d \geq 7$, we'd need $n \leq 12/(6-d)$ which is negative, impossible.

Wait, so for $d \geq 7$, we can't have a non-crossing configuration! That means some chords must cross, and $c(e) > 0$ for some chords.

Hmm wait, but actually the problem says "a finite number of chords are drawn such that each end of each chord is an end of at least $d$ different drawn chords." So every endpoint of every chord has degree $\geq d$. We need to find configurations where this holds.

For $d = 20$, we definitely can't have a non-crossing configuration. So we need to think more carefully.

Let me reconsider. The question is: what is the minimum over all valid configurations of the maximum $I(e)$ over all chords $e$?

We showed $I(e) \geq 2d - 2 = 38$ for all $e$. The question is whether we can achieve $I(e) = 38$ for all $e$, or whether we're forced to have some chord with more intersections.

To have $I(e) = 38$ for all $e$, we need $\deg(v) = d = 20$ for all vertices $v$ (so the graph is $d$-regular) and $c(e) = 0$ for all $e$ (non-crossing). But as we showed, a non-crossing $d$-regular graph on a circle requires $d \leq 6$ roughly. So for $d = 20$, this is impossible.

So we need crossings. Let me think about this more carefully.

Let me reconsider the problem. We want to minimize the maximum of $I(e) = \deg(a) + \deg(b) - 2 + c(e)$ over all chords $e = (a,b)$.

Since every vertex has degree $\geq d$, we have $I(e) \geq 2d - 2 + c(e)$.

Now, the total number of crossings. Let $C$ be the total number of crossing pairs. Then $\sum_e c(e) = 2C$ (each crossing pair contributes to $c(e)$ for both chords).

We need to find a lower bound on $\max_e c(e)$ or more precisely on $\max_e I(e)$.

Let me think about this differently. Let's consider the structure more carefully.

Actually, let me think about what configurations look like. We have $n$ points on a circle, and a $d$-regular (or minimum degree $d$) graph whose edges are chords. We want to minimize the maximum number of chords intersecting any single chord.

Let me think about small cases first to get intuition.

For the crossing part: two chords $(a,b)$ and $(c,d)$ cross iff their endpoints alternate around the circle. 

Let me think about a specific construction. Consider $n$ points equally spaced. Connect each point $i$ to points $i+1, i+2, \ldots, i+d/2$ (mod $n$) if $d$ is even. This gives a $d$-regular graph (if $n$ is large enough). But this has lots of crossings.

Actually, let me think about this problem from the perspective of the answer. The answer for $d = 20$ is likely $2d - 2 = 38$ or something related. But we showed that non-crossing is impossible for $d = 20$.

Hmm, let me reconsider. Maybe the answer is larger than $2d - 2$.

Let me think about it from a different angle. Consider the "intersection graph" $H$ of the chords: vertices of $H$ are chords, and two vertices are adjacent iff the corresponding chords intersect. We want to find the minimum possible maximum degree of $H$.

The number of vertices of $H$ is the number of chords, say $m$. The degree of a chord $e = (a,b)$ in $H$ is $I(e) = \deg_G(a) + \deg_G(b) - 2 + c(e)$.

Now, let's think about the total. $\sum_e I(e) = \sum_e (\deg(a_e) + \deg(b_e) - 2) + \sum_e c(e) = \sum_v \deg(v)^2 - 2m + 2C$.

Hmm, this is getting complicated. Let me think about specific constructions.

**Construction 1: Complete graph $K_n$.** 

Take $n$ points and draw all $\binom{n}{2}$ chords. Every vertex has degree $n-1$. For this to satisfy the condition, we need $n - 1 \geq d$, so $n \geq d + 1$.

For a chord $(a,b)$ in $K_n$: $\deg(a) = \deg(b) = n-1$, so $\deg(a) + \deg(b) - 2 = 2n - 4$. The number of chords crossing $(a,b)$: a chord $(c,d)$ crosses $(a,b)$ iff one of $c,d$ is in the arc from $a$ to $b$ and the other is in the arc from $b$ to $a$. If there are $k$ points on one side and $n - 2 - k$ on the other, the number of crossing chords is $k(n-2-k)$. The maximum of $k(n-2-k)$ is $(n-2)^2/4$.

So $I(e) = 2n - 4 + k(n-2-k)$. The maximum over all chords is at least $2n - 4 + (n-2)^2/4$ (achieved by the "diameter" chords). For $n = d + 1 = 21$, this is $2 \cdot 17 + 19^2/4 = 38 + 90.25 = 128.25$, so about 128. That's much larger than 38.

So the complete graph is a bad construction for minimizing the maximum.

**Construction 2: Try to minimize crossings.**

We want a $d$-regular graph on $n$ points on a circle with as few crossings as possible, and with the crossings distributed evenly.

Actually, we don't need $d$-regular; we need minimum degree $\geq d$. But to minimize $I(e)$, we'd want degrees to be exactly $d$.

Let me think about what graph structure minimizes crossings for a given degree sequence on a circle.

A key insight: for points on a circle, the number of crossings is minimized when the graph is "as planar as possible." But for $d = 20$, we can't have a planar graph with minimum degree 20.

The maximum degree of a planar graph is unbounded, but the average degree is at most 6. For minimum degree $d$, we need average degree $\geq d$, so $d \leq 6$ for planar (outerplanar, actually, since all vertices are on the circle).

Wait, all vertices are on the circle, so the graph is an "outerplanar" graph if it's non-crossing. For outerplanar graphs, the maximum number of edges is $2n - 3$ (for $n \geq 2$), so the average degree is at most $2(2n-3)/n = 4 - 6/n < 4$. So for minimum degree $d$, we need $d \leq 3$ (since average degree $< 4$ means some vertex has degree $\leq 3$).

So for $d \geq 4$, we can't even have a non-crossing configuration! For $d = 20$, we definitely need crossings.

OK so let me think about this more carefully. The problem is asking for the answer when $d = 20$. Let me think about what the general answer might be.

Let me consider a different approach. Think of the points on the circle and the chords. For each chord $e = (a,b)$, let $s(e)$ be the number of points strictly inside the arc from $a$ to $b$ (say, the smaller arc, or let's say we go clockwise from $a$ to $b$ and count points in between). Actually, let me define it more carefully.

Label points $1, 2, \ldots, n$ clockwise. For chord $(i, j)$ with $i < j$, let $a = j - i - 1$ (points between $i$ and $j$ clockwise) and $b = n - (j - i + 1) = n - j + i - 1$ (points between $j$ and $i$ clockwise, i.e., the other arc). So $a + b = n - 2$.

The number of chords crossing $(i,j)$ is the number of chords with one endpoint in the arc $\{i+1, \ldots, j-1\}$ and the other in $\{j+1, \ldots, n, 1, \ldots, i-1\}$.

Let me denote the two arcs as $A$ (with $a$ points) and $B$ (with $b$ points), $a + b = n - 2$.

The number of crossing chords $c(e) = e(A, B)$ where $e(A, B)$ is the number of edges between $A$ and $B$ in the graph.

Now, the sum of degrees of vertices in $A$ is $\sum_{v \in A} \deg(v) \geq da$. This sum counts edges within $A$ twice and edges from $A$ to $\{i, j\} \cup B$ once. So:
$$\sum_{v \in A} \deg(v) = 2e(A) + e(A, \{i\}) + e(A, \{j\}) + e(A, B)$$

where $e(A)$ is edges within $A$, $e(A, \{i\})$ is edges from $A$ to $i$, etc.

So $e(A, B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

Similarly, $e(A, B) = \sum_{v \in B} \deg(v) - 2e(B) - e(B, \{i\}) - e(B, \{j\})$.

Now, $e(A, \{i\}) + e(A, \{j\}) + e(B, \{i\}) + e(B, \{j\}) = \deg(i) + \deg(j) - 2$ (subtracting 2 for the edge $(i,j)$ itself, assuming it exists; actually $\deg(i) = e(A, \{i\}) + e(B, \{i\}) + 1$ (the $+1$ for edge to $j$) and similarly $\deg(j) = e(A, \{j\}) + e(B, \{j\}) + 1$, so $e(A, \{i\}) + e(B, \{i\}) + e(A, \{j\}) + e(B, \{j\}) = \deg(i) + \deg(j) - 2$).

Also, $e(A) + e(B) + e(A, B) + e(A, \{i\}) + e(A, \{j\}) + e(B, \{i\}) + e(B, \{j\}) + 1 = m$ (total edges, the $+1$ is for edge $(i,j)$).

From the two expressions for $e(A,B)$:
$$2e(A,B) = \sum_{v \in A} \deg(v) + \sum_{v \in B} \deg(v) - 2e(A) - 2e(B) - (\deg(i) + \deg(j) - 2)$$

$$= \sum_{v \neq i,j} \deg(v) - 2(e(A) + e(B)) - \deg(i) - \deg(j) + 2$$

$$= 2m - \deg(i) - \deg(j) - 2(e(A) + e(B)) - \deg(i) - \deg(j) + 2$$

Wait, $\sum_{v \neq i,j} \deg(v) = 2m - \deg(i) - \deg(j)$. And $e(A) + e(B) = m - e(A,B) - (\deg(i) + \deg(j) - 2) - 1 = m - e(A,B) - \deg(i) - \deg(j) + 1$.

So:
$$2e(A,B) = 2m - \deg(i) - \deg(j) - 2(m - e(A,B) - \deg(i) - \deg(j) + 1) - \deg(i) - \deg(j) + 2$$
$$= 2m - \deg(i) - \deg(j) - 2m + 2e(A,B) + 2\deg(i) + 2\deg(j) - 2 - \deg(i) - \deg(j) + 2$$
$$= 2e(A,B)$$

OK, that's circular (as expected). Let me try a different approach.

From $e(A,B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$:

Since $\sum_{v \in A} \deg(v) \geq da$ and $e(A, \{i\}) + e(A, \{j\}) \leq \deg(i) + \deg(j) - 2$ (actually this is an overcount since some of $i$'s and $j$'s edges go to $B$), and $e(A) \geq 0$:

$$e(A,B) \geq da - e(A, \{i\}) - e(A, \{j\}) \geq da - (\deg(i) - 1) - (\deg(j) - 1) = da - \deg(i) - \deg(j) + 2$$

Hmm, but this could be negative. Let me also use the other side:

$$e(A,B) \geq db - \deg(i) - \deg(j) + 2$$

So $e(A,B) \geq \max(da, db) - \deg(i) - \deg(j) + 2$.

Actually, we can do better. From $e(A,B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A,\{i\}) - e(A,\{j\})$:

We have $e(A,\{i\}) \leq \deg(i) - 1$ and $e(A,\{j\}) \leq \deg(j) - 1$, so $e(A,\{i\}) + e(A,\{j\}) \leq \deg(i) + \deg(j) - 2$.

Also $2e(A) \leq a(a-1)$ (max edges within $A$) but that's not useful for a lower bound.

So $c(e) = e(A,B) \geq da - (\deg(i) + \deg(j) - 2) = da - \deg(i) - \deg(j) + 2$.

And similarly $c(e) \geq db - \deg(i) - \deg(j) + 2$.

So $c(e) \geq \max(a, b) \cdot d - \deg(i) - \deg(j) + 2$.

Since $a + b = n - 2$, $\max(a, b) \geq (n-2)/2$.

If the graph is $d$-regular, $\deg(i) = \deg(j) = d$, so:
$$c(e) \geq \max(a, b) \cdot d - 2d + 2 = d(\max(a,b) - 2) + 2$$

Wait, that doesn't seem right. Let me redo: $c(e) \geq da - 2d + 2 = d(a - 2) + 2$ and $c(e) \geq d(b-2) + 2$.

So $c(e) \geq d(\max(a,b) - 2) + 2 \geq d((n-2)/2 - 2) + 2 = d(n-6)/2 + 2$.

And $I(e) = 2d - 2 + c(e) \geq 2d - 2 + d(\max(a,b) - 2) + 2 = 2d + d(\max(a,b) - 2) = d \cdot \max(a,b)$.

Hmm wait, let me recompute. $I(e) = \deg(i) + \deg(j) - 2 + c(e) = 2d - 2 + c(e)$.

And $c(e) \geq d \cdot \max(a,b) - 2d + 2$.

So $I(e) \geq 2d - 2 + d \cdot \max(a,b) - 2d + 2 = d \cdot \max(a,b)$.

Interesting! So $I(e) \geq d \cdot \max(a, b)$ where $a, b$ are the number of points on each side of the chord.

Since $\max(a, b) \geq (n-2)/2$, we get $I(e) \geq d(n-2)/2$.

But this depends on $n$, which we can choose. To minimize the maximum $I(e)$, we'd want $n$ to be as small as possible. The minimum $n$ for a $d$-regular graph is $n = d + 1$ (complete graph). But then $\max(a, b) \approx (n-2)/2 = (d-1)/2$, giving $I(e) \geq d(d-1)/2$, which for $d = 20$ is $20 \cdot 19 / 2 = 190$. That's way more than 38.

But wait, we don't need $d$-regular. We need minimum degree $\geq d$. And we want to minimize the maximum $I(e)$.

Hmm, but the bound $I(e) \geq d \cdot \max(a,b)$ used $\deg(i) = \deg(j) = d$ (regular). If degrees are higher, the bound on $c(e)$ is weaker (since $c(e) \geq da - \deg(i) - \deg(j) + 2$), but $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq \deg(i) + \deg(j) - 2 + da - \deg(i) - \deg(j) + 2 = da$.

Oh interesting! So regardless of the degrees of $i$ and $j$:
$$I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq \deg(i) + \deg(j) - 2 + (da - \deg(i) - \deg(j) + 2) = da$$

And similarly $I(e) \geq db$.

So $I(e) \geq d \cdot \max(a, b)$.

This is a clean bound! Let me double-check.

$c(e) = e(A, B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

$\sum_{v \in A} \deg(v) \geq d \cdot |A| = da$.

$e(A, \{i\}) + e(A, \{j\}) \leq \deg(i) + \deg(j) - 2$ (since $e(A,\{i\}) \leq \deg(i) - 1$ because at least one edge from $i$ goes to $j$, and similarly for $j$; actually, $e(A, \{i\}) \leq \deg(i) - 1$ only if the edge $(i,j)$ exists, which it does since $e = (i,j)$ is a chord).

Wait, actually $e(A, \{i\})$ is the number of edges from $i$ to vertices in $A$. Since $\deg(i)$ counts all edges from $i$, and one of them goes to $j$, we have $e(A, \{i\}) \leq \deg(i) - 1$. Similarly $e(A, \{j\}) \leq \deg(j) - 1$. So $e(A, \{i\}) + e(A, \{j\}) \leq \deg(i) + \deg(j) - 2$.

And $e(A) \geq 0$.

So $c(e) \geq da - 0 - (\deg(i) + \deg(j) - 2) = da - \deg(i) - \deg(j) + 2$.

Therefore $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq \deg(i) + \deg(j) - 2 + da - \deg(i) - \deg(j) + 2 = da$.

Similarly, using the $B$ side: $I(e) \geq db$.

So $I(e) \geq d \cdot \max(a, b) \geq d \cdot \lceil (n-2)/2 \rceil$.

Now, to minimize this, we want to minimize $n$. What's the minimum $n$?

We need a graph on $n$ vertices (points on a circle) with minimum degree $\geq d$. The minimum $n$ for a simple graph with minimum degree $d$ is $n = d + 1$ (the complete graph $K_{d+1}$).

With $n = d + 1$: $\max(a, b) \geq \lceil (d - 1)/2 \rceil$. For $d = 20$: $\max(a,b) \geq \lceil 19/2 \rceil = 10$. So $I(e) \geq 20 \cdot 10 = 200$.

But wait, can we do better with a larger $n$? No—a larger $n$ makes $\max(a,b)$ larger, which makes the bound worse. So the minimum $n$ gives the best bound.

But wait, is this bound tight? Can we actually achieve $I(e) = d \cdot \max(a,b)$ for all chords?

Let me check with $n = d + 1$, the complete graph $K_{d+1}$. For $d = 20$, $n = 21$. For a chord $(i,j)$, $a + b = 19$. The maximum of $a, b$ is at least 10. For a chord that splits the remaining 19 points into 10 and 9, $\max(a,b) = 10$, so $I(e) \geq 200$.

In $K_{21}$, $I(e) = \deg(i) + \deg(j) - 2 + c(e) = 20 + 20 - 2 + c(e) = 38 + c(e)$. And $c(e) = a \cdot b$ (in the complete graph, every pair of points on opposite sides gives a crossing chord). For $a = 10, b = 9$: $c(e) = 90$. So $I(e) = 38 + 90 = 128$.

But our bound says $I(e) \geq d \cdot \max(a,b) = 20 \cdot 10 = 200$. But we computed $I(e) = 128$. That's a contradiction!

Let me recheck. Oh wait, I think I made an error. Let me recheck the bound.

$c(e) = e(A, B)$. In $K_{21}$, $e(A, B) = |A| \cdot |B| = a \cdot b$. For $a = 10, b = 9$: $c(e) = 90$.

$I(e) = 38 + 90 = 128$.

But the bound says $I(e) \geq da = 20 \cdot 10 = 200$. That's clearly wrong since $128 < 200$.

Let me find the error. 

$c(e) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

In $K_{21}$: $\sum_{v \in A} \deg(v) = 10 \cdot 20 = 200$. $e(A) = \binom{10}{2} = 45$. $e(A, \{i\}) = 10$ (all vertices in $A$ are connected to $i$). $e(A, \{j\}) = 10$.

$c(e) = 200 - 90 - 10 - 10 = 90$. ✓

Now, $e(A, \{i\}) + e(A, \{j\}) = 20$. And $\deg(i) + \deg(j) - 2 = 38$. So $e(A, \{i\}) + e(A, \{j\}) = 20 \leq 38$. ✓

The bound was: $c(e) \geq da - (\deg(i) + \deg(j) - 2) = 200 - 38 = 162$. But actual $c(e) = 90 < 162$. 

The issue is that $e(A, \{i\}) + e(A, \{j\}) = 20$, which is much less than $\deg(i) + \deg(j) - 2 = 38$. The bound $e(A, \{i\}) + e(A, \{j\}) \leq \deg(i) + \deg(j) - 2$ is correct but very loose, because many of $i$'s and $j$'s edges go to $B$, not $A$.

So the bound $I(e) \geq d \cdot \max(a,b)$ is wrong. Let me redo this.

$c(e) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

We have $\sum_{v \in A} \deg(v) \geq da$, $e(A) \geq 0$, $e(A, \{i\}) \geq 0$, $e(A, \{j\}) \geq 0$.

So $c(e) \geq da - 2e(A) - e(A, \{i\}) - e(A, \{j\})$. But we can't bound $e(A, \{i\})$ and $e(A, \{j\})$ from above tightly without more info.

Actually, $e(A, \{i\}) \leq \min(\deg(i) - 1, a)$ and $e(A, \{j\}) \leq \min(\deg(j) - 1, a)$.

So $c(e) \geq da - 2e(A) - \min(\deg(i)-1, a) - \min(\deg(j)-1, a)$.

And $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq \deg(i) + \deg(j) - 2 + da - 2e(A) - \min(\deg(i)-1, a) - \min(\deg(j)-1, a)$.

If $\deg(i) - 1 \leq a$ and $\deg(j) - 1 \leq a$ (which is the case when $a$ is large), then:
$I(e) \geq \deg(i) + \deg(j) - 2 + da - 2e(A) - (\deg(i) - 1) - (\deg(j) - 1) = da - 2e(A)$.

If $e(A) = 0$ (no edges within $A$), then $I(e) \geq da$. But in $K_{21}$, $e(A) = 45 \neq 0$, so this doesn't apply.

OK so the bound depends on $e(A)$, the number of edges within $A$. Let me think about this differently.

Let me try a different approach. Instead of trying to get a universal lower bound, let me think about what configuration minimizes the maximum $I(e)$.

Let me think about the problem from the perspective of the answer. This is a competition problem, and the answer for $d = 20$ is likely a clean expression in $d$.

Let me consider the possibility that the answer is $2d - 2 = 38$. For this to work, we'd need a configuration where every chord has $c(e) = 0$ (no crossings) and $\deg(v) = d$ for all $v$. But we showed this is impossible for $d \geq 4$ (outerplanar graphs have average degree $< 4$).

What about $d^2 - 1$? Or $d(d-1)$? Or $d^2$? Let me think...

Actually, let me reconsider. Maybe the answer involves $d^2$ or $d(d-1)$.

Let me think about a specific construction that might be optimal.

**Construction: $d$-regular graph on $2d$ vertices.**

Consider $2d$ points on a circle. Connect each point to the $d$ nearest points (including both directions). Actually, let me think of a specific good construction.

Hmm, let me think about this more carefully. 

Actually, let me reconsider the problem. The key constraint is that each endpoint has degree $\geq d$. We want to minimize the maximum number of intersections per chord.

Let me think about a "star-like" construction. Suppose we have $d + 1$ points, and one of them (say point 0) is connected to all other $d$ points. Then point 0 has degree $d$, but the other points have degree 1 (from the edge to 0). To get their degree up to $d$, we need more edges.

Actually, let me think about the problem differently. Let me consider the "thrackle" perspective or think about what structure minimizes crossings.

Let me try to think about what happens with $n = 2d$ points.

Consider $2d$ points on a circle, labeled $0, 1, \ldots, 2d-1$. Consider the "antipodal" matching: connect $i$ to $i + d$ for each $i = 0, 1, \ldots, d-1$. This gives $d$ chords, all passing through the center, and they all cross each other. Each point has degree 1. Not enough.

Let me think about a different construction. Consider $n$ points and connect each point to its $d$ nearest neighbors (in terms of circular distance). If $d$ is even, say $d = 2k$, connect each point to the $k$ nearest on each side. This gives a $d$-regular graph.

For this graph, the chord $(i, i+r)$ where $1 \leq r \leq k$ has $a = r - 1$ points on one side and $b = n - r - 1$ on the other. The number of crossings depends on the structure.

This is getting complicated. Let me try to think about the problem from a higher level.

The answer $M$ is the minimum over all valid configurations of the maximum $I(e)$. We need to find both a lower bound (every configuration has a chord with $\geq M$ intersections) and a matching upper bound (there exists a configuration where every chord has $\leq M$ intersections).

Let me think about the lower bound more carefully.

For any chord $e = (i,j)$, $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq 2d - 2 + c(e)$.

So if we can show that some chord must have $c(e) \geq X$, then $M \geq 2d - 2 + X$.

The total number of crossings is $C = \frac{1}{2} \sum_e c(e)$. If we can lower bound $C$ and upper bound the number of chords $m$, then some chord has $c(e) \geq 2C/m$.

But this might not give a tight bound. Let me think differently.

Actually, let me think about a specific chord. Consider the chord that has the most "balanced" split, i.e., $\max(a,b)$ is minimized. For any chord, $\max(a,b) \geq (n-2)/2$. The chord that achieves $\max(a,b) = \lceil (n-2)/2 \rceil$ is one that nearly bisects the circle.

For this chord, $c(e) = e(A, B)$. Now, $\sum_{v \in A} \deg(v) \geq da$ and $\sum_{v \in B} \deg(v) \geq db$. The total degree is $\sum_v \deg(v) \geq dn$, so $m \geq dn/2$.

$e(A, B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

Also, $e(A) + e(A, \{i\}) + e(A, \{j\}) + e(A, B) = $ (edges with at least one endpoint in $A$) $= \sum_{v \in A} \deg(v) - e(A)$. Wait, no. $\sum_{v \in A} \deg(v) = 2e(A) + e(A, \{i\}) + e(A, \{j\}) + e(A, B)$. So $e(A, B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

The number of edges with at least one endpoint in $A$ is $e(A) + e(A, \{i\}) + e(A, \{j\}) + e(A, B) = \sum_{v \in A} \deg(v) - e(A)$.

Hmm, I'm going in circles (no pun intended). Let me try to think about this problem from the answer's perspective.

For competition problems of this type, the answer is often $d^2 - 1$ or $2d - 2$ or $d^2$ or similar. Let me think about which one.

Let me try to construct a configuration where the maximum $I(e)$ is as small as possible, for general $d$.

**Key idea: Use a complete bipartite-like structure or a specific regular graph.**

Let me try $n = 2d$ points, and connect each point to the $d$ points farthest from it (i.e., the $d$ points on the "other side" of the circle). Specifically, label points $0, 1, \ldots, 2d-1$. Connect $i$ to $i+d, i+d+1, \ldots, i+2d-1 \pmod{2d}$... no, that's everything.

Let me try a different approach. Consider $n = 2d$ points. Connect point $i$ to points $i+1, i+2, \ldots, i+d \pmod{2d}$. Wait, that gives degree $d$ for each point. But point $i$ is connected to $i+d$, and point $i+d$ is connected to $i+d+1, \ldots, i+2d = i$, so yes, the edge $(i, i+d)$ is counted from both sides. Actually, let me be more careful.

If we connect $i$ to $i+1, i+2, \ldots, i+d \pmod{2d}$, then each point has degree $d$ (out-degree $d$, but since the graph is undirected, we need to check). Point $i$ is connected to $i+1, \ldots, i+d$. Point $j$ is connected to $j+1, \ldots, j+d$. The edge $(i, j)$ exists iff $j - i \pmod{2d} \in \{1, 2, \ldots, d\}$ or $i - j \pmod{2d} \in \{1, 2, \ldots, d\}$. Since $j - i \pmod{2d} \in \{1, \ldots, d\}$ or $i - j \pmod{2d} \in \{1, \ldots, d\}$, and these are complementary (one is in $\{1, \ldots, d\}$ iff the other is in $\{d, \ldots, 2d-1\}$... wait, if $j - i \equiv r \pmod{2d}$ with $1 \leq r \leq d$, then $i - j \equiv 2d - r \pmod{2d}$ with $d \leq 2d - r \leq 2d - 1$. So the edge exists iff $r \in \{1, \ldots, d\}$, which is the same as $2d - r \in \{d, \ldots, 2d-1\}$. So the condition is: $j - i \pmod{2d} \in \{1, \ldots, d\}$. But this means each ordered pair $(i, j)$ with $j - i \pmod{2d} \in \{1, \ldots, d\}$ gives an edge. The number of such $j$ for each $i$ is $d$. But we're double-counting: edge $(i, j)$ with $j - i \equiv r$ is the same as edge $(j, i)$ with $i - j \equiv 2d - r$. So the degree of each vertex is $d$ (since for each $i$, there are exactly $d$ values of $j$ with $j - i \pmod{2d} \in \{1, \ldots, d\}$, and each gives a unique edge).

Wait, but if $r = d$, then $j - i \equiv d$ and $i - j \equiv d$ (mod $2d$). So the edge $(i, i+d)$ is counted once from $i$'s perspective (with $r = d$) and once from $i+d$'s perspective (with $r = d$). So it's not double-counted in the degree; it's just one edge. So the degree is $d$ for each vertex. Good.

But wait, is this a valid simple graph? The edge $(i, i+d)$ exists. Also, $(i, i+1), (i, i+2), \ldots, (i, i+d)$. And from $i-1$: $(i-1, i), (i-1, i+1), \ldots, (i-1, i+d-1)$. So edge $(i-1, i)$ exists. From $i-d$: $(i-d, i-d+1), \ldots, (i-d, i)$. So edge $(i-d, i)$ exists. So vertex $i$ is connected to $i-d, i-d+1, \ldots, i-1, i+1, \ldots, i+d$. That's $2d$ neighbors, but we said degree is $d$. 

Hmm, I think I'm confusing myself. Let me recount. Vertex $i$ is connected to $j$ iff $j - i \pmod{2d} \in \{1, 2, \ldots, d\}$. So the neighbors of $i$ are $i+1, i+2, \ldots, i+d \pmod{2d}$. That's $d$ neighbors. But also, $j$ is connected to $i$ iff $i - j \pmod{2d} \in \{1, \ldots, d\}$, i.e., $j$ is connected to $i$ iff $j$ is one of $i-1, i-2, \ldots, i-d \pmod{2d}$. So the full neighbor set of $i$ is $\{i+1, \ldots, i+d, i-1, \ldots, i-d\} \pmod{2d}$... no, that's not right either.

The graph is undirected. Edge $(i, j)$ exists iff $j - i \pmod{2d} \in \{1, \ldots, d\}$ OR $i - j \pmod{2d} \in \{1, \ldots, d\}$. Since $j - i \pmod{2d} \in \{1, \ldots, 2d-1\}$ (assuming $i \neq j$), and $\{1, \ldots, d\} \cup \{d, \ldots, 2d-1\} = \{1, \ldots, 2d-1\}$ (with $d$ in both), the edge exists for all $j \neq i$ except when... wait, $\{1, \ldots, d\}$ and $\{d, d+1, \ldots, 2d-1\}$, their union is $\{1, \ldots, 2d-1\}$ with $d$ in both. So for $j - i \equiv r \pmod{2d}$ with $r \in \{1, \ldots, 2d-1\}$, the edge exists iff $r \in \{1, \ldots, d\}$ or $2d - r \in \{1, \ldots, d\}$, i.e., $r \in \{1, \ldots, d\}$ or $r \in \{d, \ldots, 2d-1\}$, which is all $r \in \{1, \ldots, 2d-1\}$. So the graph is complete!

That's because $d \geq n/2 = d$ in this case. So with $n = 2d$ and connecting to $d$ nearest in one direction, we get the complete graph. Not useful.

Let me try $n = 2d + 2$ or larger.

Actually, let me step back and think about this problem more carefully.

I want to find a $d$-regular (or min-degree $d$) graph on $n$ points on a circle that minimizes the maximum $I(e)$.

$I(e) = \deg(i) + \deg(j) - 2 + c(e)$ for chord $e = (i,j)$.

For a $d$-regular graph, $I(e) = 2d - 2 + c(e)$. So we want to minimize $\max_e c(e)$.

$c(e)$ is the number of chords crossing $e$ in the interior. We want a $d$-regular chord diagram that minimizes the maximum number of crossings per chord.

Now, the total number of crossings $C = \frac{1}{2} \sum_e c(e)$. If there are $m = nd/2$ chords, then $\max_e c(e) \geq 2C/m = 2C/(nd/2) = 4C/(nd)$.

So we need to lower bound $C$, the total number of crossings, for a $d$-regular graph on $n$ points on a circle.

There's a formula for the minimum number of crossings in a graph drawn on a circle. This is related to the "circular crossing number" or "convex crossing number."

For a graph $G$ on $n$ vertices with $m$ edges, drawn with vertices on a circle, the minimum number of crossings (over all circular orderings and all graphs with the given degree sequence) is related to the degree sequence.

Actually, there's a result that for a $d$-regular graph on $n$ vertices drawn on a circle, the minimum number of crossings is at least... let me think.

The number of crossings for a specific drawing is $\sum_{\text{crossing pairs}} 1$. For a chord $(i,j)$ with $a$ points on one side and $b$ on the other, $c(e) = e(A, B)$, the number of edges between the two sides.

The total number of crossings is $C = \frac{1}{2} \sum_e e(A_e, B_e)$ where $A_e, B_e$ are the two sides of chord $e$.

Alternatively, $C = \sum_{\text{unordered pairs of edges } \{e, f\}} [\text{$e$ and $f$ cross}]$.

For two edges $e = (i, j)$ and $f = (k, l)$ with $i < j$ and $k < l$, they cross iff $i < k < j < l$ or $k < i < l < j$ (assuming all distinct).

The total number of crossing pairs can be computed as follows. For each 4-element subset $\{a, b, c, d\}$ of vertices with $a < b < c < d$, the pairs of edges that cross are: $(a,c)$ with $(b,d)$ and $(a,d)$ with $(b,c)$. So each 4-subset contributes at most 2 crossings (if both pairs of edges exist).

The total number of 4-subsets is $\binom{n}{4}$. The maximum number of crossings is $2\binom{n}{4}$ (complete graph). For a $d$-regular graph, we need to count how many of these crossing pairs actually exist.

This is getting complex. Let me try a different approach and think about what the answer should be.

Let me consider the problem for small $d$ and try to find a pattern.

**Case $d = 2$:** We need every vertex to have degree $\geq 2$. The minimum $I(e) \geq 2 \cdot 2 - 2 = 2$. Can we achieve $I(e) = 2$ for all chords? We need $c(e) = 0$ for all $e$, i.e., a non-crossing 2-regular graph. A 2-regular non-crossing graph on a circle is a cycle that goes around the circle (the polygon). In this case, each edge (side of the polygon) intersects exactly 2 other edges (its two neighbors in the cycle). So $I(e) = 2$ for all $e$, and $M = 2 = 2d - 2$. ✓

**Case $d = 3$:** We need a non-crossing 3-regular graph (for $I(e) = 4$). But a 3-regular non-crossing graph on a circle is a maximal outerplanar graph, which has $2n - 3$ edges and average degree $< 4$. So a 3-regular outerplanar graph would need $3n/2 = 2n - 3$, giving $n = 6$. $K_4$ minus an edge? No. Let me think: a 3-regular outerplanar graph on 6 vertices. The octahedron graph is 4-regular. A triangular prism is 3-regular on 6 vertices but is it outerplanar? 

Actually, a maximal outerplanar graph on $n$ vertices has $2n - 3$ edges. For 3-regular, we need $3n/2$ edges, so $3n/2 = 2n - 3$ gives $n = 6$. A 3-regular outerplanar graph on 6 vertices: this would be a triangulation of a hexagon. The hexagon triangulated with 3 non-crossing diagonals gives $6 + 3 = 9 = 2 \cdot 6 - 3$ edges. But the degrees would be: each triangulation of a hexagon has some vertices of degree 2 and some of higher degree. Actually, in a maximal outerplanar graph on $n$ vertices, there are always at least 2 vertices of degree 2. So a 3-regular outerplanar graph doesn't exist (for $n \geq 4$).

So for $d = 3$, we can't have a non-crossing configuration. We need some crossings. So $M > 2d - 2 = 4$ for $d = 3$.

Hmm, but wait. We don't need the graph to be exactly $d$-regular. We need minimum degree $\geq d$. And we want to minimize the maximum $I(e)$. Maybe with higher degrees at some vertices, we can reduce crossings?

Actually, higher degrees at endpoints increase $I(e)$ directly (through $\deg(i) + \deg(j) - 2$), but might allow us to reduce crossings. It's a tradeoff.

Let me think about $d = 3$ more carefully. We need min degree 3. The smallest such graph on a circle: $K_4$ has 4 vertices, each of degree 3. With 4 points on a circle, $K_4$ has 6 edges. The two diagonals cross. Each side of the square intersects: 2 adjacent sides + 1 diagonal (the one not sharing an endpoint) = 3. Wait, let me count.

4 points on a circle: 1, 2, 3, 4. Edges: (1,2), (2,3), (3,4), (4,1), (1,3), (2,4). The diagonals (1,3) and (2,4) cross.

For edge (1,2): shares endpoint with (2,3), (4,1), (1,3). Crosses: (3,4)? No, (1,2) and (3,4) don't cross (they're on opposite sides). (2,4)? (1,2) and (2,4) share endpoint 2. So (1,2) intersects (2,3), (4,1), (1,3) by sharing endpoints, and does it cross anything? (1,2) and (3,4): 1 < 2 < 3 < 4, so no crossing. (1,2) and (2,4): share endpoint. (1,2) and (1,3): share endpoint. So $I((1,2)) = 3$.

For edge (1,3): shares endpoint with (1,2), (4,1), (3,4), (1,3) is itself... shares with (1,2), (3,4), (4,1). Crosses (2,4). So $I((1,3)) = 4$.

So the maximum is 4 = $2 \cdot 3 - 2$. So $M = 4$ for $d = 3$? But we said a non-crossing 3-regular graph doesn't exist. The point is that $K_4$ has crossings, but the maximum $I(e)$ is still $2d - 2 = 4$.

Wait, the diagonal (1,3) has $I = 4 = 2 \cdot 3 - 2 + 1$ (one crossing). But the sides have $I = 3 < 4$. So the maximum is 4, which equals $2d - 2$.

Hmm, so even though there are crossings, the maximum $I(e)$ is still $2d - 2$? That's because the sides have fewer intersections (only 3, which is less than $2d - 2 = 4$), and the diagonals have exactly $2d - 2 = 4$.

But the problem asks for the maximum $M$ such that in ANY configuration, some chord has $\geq M$ intersections. So $M$ is the minimum over configurations of the maximum $I(e)$. For $d = 3$, the $K_4$ configuration has max $I(e) = 4$. Can we do better (get max $I(e) < 4$)? We need $I(e) \geq 2d - 2 = 4$ for all $e$ (since $\deg \geq 3$ for all vertices). So no, $M = 4$ for $d = 3$.

Wait, $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq 2d - 2 + c(e) \geq 2d - 2$. So $M \geq 2d - 2$ always. And the question is whether we can achieve max $I(e) = 2d - 2$, which requires $c(e) = 0$ for the chord with maximum $I(e)$, and $\deg = d$ for all vertices.

But we don't need $c(e) = 0$ for ALL chords; we need the MAXIMUM $I(e)$ to be $2d - 2$. This requires that for the chord with the highest $I(e)$, we have $\deg(i) + \deg(j) - 2 + c(e) = 2d - 2$, which means $\deg(i) = \deg(j) = d$ and $c(e) = 0$. But other chords can have higher $I(e)$... no, we want the maximum to be $2d - 2$, so ALL chords must have $I(e) \leq 2d - 2$. Since $I(e) \geq 2d - 2$ for all $e$, this means $I(e) = 2d - 2$ for all $e$, which requires $\deg(v) = d$ for all $v$ and $c(e) = 0$ for all $e$.

So $M = 2d - 2$ iff there exists a non-crossing $d$-regular graph on a circle. This exists iff $d \leq 3$ (for $d = 2$, the polygon; for $d = 3$, we need to check more carefully).

Wait, for $d = 3$, does a non-crossing 3-regular graph on a circle exist? As I argued, a maximal outerplanar graph has at least 2 vertices of degree 2, so a 3-regular outerplanar graph doesn't exist. But $K_4$ on 4 points has crossings (the two diagonals cross). So for $d = 3$, $M > 4$?

But I computed that $K_4$ has max $I(e) = 4 = 2d - 2$. The sides have $I = 3$ and the diagonals have $I = 4$. So the max is 4. But $I(e) \geq 2d - 2 = 4$ for all $e$... wait, the sides have $I = 3 < 4$! How?

Oh, I think I miscounted. Let me recount for $K_4$ on 4 points.

Points: 1, 2, 3, 4 in order on the circle. Edges: (1,2), (2,3), (3,4), (4,1), (1,3), (2,4).

Edge (1,2): $\deg(1) = 3, \deg(2) = 3$. $I = 3 + 3 - 2 + c = 4 + c$. $c$ = number of edges crossing (1,2) in interior. (1,2) has points 0 on one side (between 1 and 2) and points 3, 4 on the other side. An edge crosses (1,2) iff it has one endpoint in $\{3, 4\}$... wait, (1,2) is a side of the square, so there are no points between 1 and 2 (they're adjacent). The arc from 1 to 2 (clockwise) has 0 interior points, and the arc from 2 to 1 (clockwise, i.e., through 3, 4) has 2 interior points. So $a = 0, b = 2$. $c(e) = e(A, B) = e(\emptyset, \{3, 4\}) = 0$. So $I = 4 + 0 = 4$.

I made an error before. Let me recount. $I((1,2)) = \deg(1) + \deg(2) - 2 + c = 3 + 3 - 2 + 0 = 4$. The chords intersecting (1,2) are: (2,3) [shares 2], (4,1) [shares 1], (1,3) [shares 1], (2,4) [shares 2]. That's 4 chords. And (3,4) doesn't intersect (1,2) (no shared endpoint, no crossing). So $I = 4$. ✓

Edge (1,3): $\deg(1) = 3, \deg(3) = 3$. $I = 4 + c$. Arc from 1 to 3 has point 2, arc from 3 to 1 has point 4. $a = 1, b = 1$. $c = e(\{2\}, \{4\}) = 1$ (edge (2,4) exists). So $I = 4 + 1 = 5$.

So the max is 5, not 4! I made an error earlier. Let me recount the intersections of (1,3): shares endpoint with (1,2), (4,1), (3,4), (2,3). That's 4. Plus crosses (2,4). Total 5. ✓

So for $K_4$ with $d = 3$, max $I(e) = 5$. Can we do better with a different configuration?

We need min degree 3. With 4 points, the only option is $K_4$. With more points, we might do better.

Let me try 6 points with a 3-regular graph. Consider the graph: (1,2), (2,3), (3,4), (4,5), (5,6), (6,1) (the hexagon) plus (1,3), (3,5), (5,1) (a triangle on odd vertices) plus... wait, that gives degrees: 1: 3 (edges to 2, 6, 3), 2: 2 (edges to 1, 3), 3: 4 (edges to 2, 4, 1, 5), 4: 2, 5: 4, 6: 2. Not 3-regular.

Let me try the complete bipartite graph $K_{3,3}$ on 6 points. Points 1,2,3 on one side, 4,5,6 on the other. But on a circle, the arrangement matters. Let me place them as 1,4,2,5,3,6 around the circle. Then edges are all pairs between {1,2,3} and {4,5,6}.

This is getting complicated. Let me try to think about the general problem differently.

Actually, let me reconsider. The problem is from a competition (likely ISL or similar), and the answer for $d = 20$ should be a specific number. Let me think about what structural result gives the answer.

Let me reconsider the lower bound. We have $I(e) \geq 2d - 2 + c(e)$. The question is: what is the minimum possible value of $\max_e c(e)$ over all valid configurations?

Actually, more precisely, we want to minimize $\max_e I(e) = \max_e (\deg(i_e) + \deg(j_e) - 2 + c(e))$. Since $\deg \geq d$, this is $\geq \max_e (2d - 2 + c(e)) = 2d - 2 + \max_e c(e)$. So $M \geq 2d - 2 + \min_{\text{config}} \max_e c(e)$.

And we want to find $\min_{\text{config}} \max_e c(e)$, the minimum possible maximum number of crossings per chord.

But wait, we also want to minimize $\deg(i) + \deg(j)$, so we'd want all degrees to be exactly $d$. So the optimal configuration is likely $d$-regular.

So the question reduces to: what is the minimum possible maximum number of crossings per chord, over all $d$-regular graphs on $n$ points on a circle (for any $n$)?

And then $M = 2d - 2 + $ that minimum.

For $d = 3$: we need to find the minimum max crossings per chord in a 3-regular circular graph. In $K_4$, the max crossings per chord is 1 (the diagonals each cross 1 other chord). Can we do better? We need a 3-regular graph with max crossings 0, i.e., non-crossing. But we showed that's impossible. So the minimum max crossings is at least 1. And $K_4$ achieves 1. So $M = 2 \cdot 3 - 2 + 1 = 5$ for $d = 3$.

Hmm, but is there a 3-regular graph on more points with max crossings 0? No, because non-crossing 3-regular outerplanar graphs don't exist. Is there one with max crossings 0? No. So $M = 5$ for $d = 3$.

Wait, but maybe with more points, we can have a 3-regular graph where the max crossings per chord is still 1 but the graph is different? Or maybe with more points, we can reduce the max crossings? No, the max crossings is at least 1 (since non-crossing is impossible), and $K_4$ achieves 1. So $M = 5$ for $d = 3$.

Hmm, but actually, I should check: is there a 3-regular graph on a circle where some chord has 0 crossings but the max is still 1? That doesn't help; we need the max to be 0 for $M = 4$, which is impossible.

OK so for $d = 3$, $M = 5$.

Let me check $d = 2$: $M = 2 \cdot 2 - 2 + 0 = 2$. ✓ (non-crossing 2-regular = polygon, exists).

For $d = 4$: We need a 4-regular graph on a circle. Non-crossing 4-regular outerplanar: impossible (max degree in outerplanar can be high, but average degree $< 4$, so 4-regular is impossible). So we need crossings. What's the minimum max crossings per chord?

With $n = 5$ (complete graph $K_5$, which is 4-regular): Let me compute the max crossings. Points 1,2,3,4,5. Edge (1,3): $a = 1$ (point 2), $b = 2$ (points 4,5). $c = e(\{2\}, \{4,5\}) = 2$ (edges (2,4) and (2,5)). $I = 2 \cdot 4 - 2 + 2 = 8$. Edge (1,4): $a = 2$ (points 2,3), $b = 1$ (point 5). $c = e(\{2,3\}, \{5\}) = 2$. $I = 6 + 2 = 8$. Edge (1,2): $a = 0, b = 3$. $c = 0$. $I = 6$. So max $I = 8$.

Can we do better with more points? Let me try $n = 6$, 4-regular. The complement of a 4-regular graph on 6 vertices is 1-regular (a perfect matching). So a 4-regular graph on 6 vertices is $K_6$ minus a perfect matching.

Let me try: remove edges (1,4), (2,5), (3,6) from $K_6$. The remaining graph is 4-regular. Points 1,2,3,4,5,6 on circle.

Edge (1,2): $a = 0, b = 4$. $c = 0$. $I = 6$. 
Edge (1,3): $a = 1$ (point 2), $b = 3$ (points 4,5,6). $c = e(\{2\}, \{4,5,6\})$. Edges from 2 to {4,5,6}: (2,4), (2,6) (not (2,5) since it's removed). So $c = 2$. $I = 6 + 2 = 8$.
Edge (1,5): $a = 3$ (points 2,3,4), $b = 1$ (point 6). $c = e(\{2,3,4\}, \{6\})$. Edges from 6 to {2,3,4}: (6,2), (6,4) (not (6,3) since removed). $c = 2$. $I = 8$.
Edge (1,6): $a = 4$ (points 2,3,4,5), $b = 0$. $c = 0$. $I = 6$.

So max $I = 8$ for this graph too. Same as $K_5$.

Can we do better? Let me try $n = 8$, 4-regular. Hmm, this is getting complicated. Let me try to think about the general pattern.

For $d = 2$: $M = 2 = 2(2) - 2$.
For $d = 3$: $M = 5 = 2(3) - 2 + 1$.
For $d = 4$: $M = 8 = 2(4) - 2 + 2$? Or is it something else?

If the pattern is $M = 2d - 2 + (d - 2) = 3d - 4$, then for $d = 2$: $2$, $d = 3$: $5$, $d = 4$: $8$, $d = 20$: $56$.

Or if $M = 2d - 2 + \lfloor (d-1)/2 \rfloor$ or something...

Actually, let me think about this more carefully. The minimum max crossings per chord in a $d$-regular circular graph.

Let me think about what determines the crossings. For a $d$-regular graph on $n$ points, the total number of edges is $m = nd/2$. The total number of crossings $C$ depends on the graph structure.

For a chord $(i,j)$ with $a$ points on one side and $b = n - 2 - a$ on the other, $c(e) = e(A, B)$. In a $d$-regular graph, $\sum_{v \in A} \deg(v) = da$, so $e(A, B) = da - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

To minimize $c(e) = e(A, B)$, we want to maximize $2e(A) + e(A, \{i\}) + e(A, \{j\})$, i.e., we want as many edges as possible to stay within $A$ or connect to $i, j$.

The maximum of $e(A)$ is $\binom{a}{2}$ (but limited by the degree constraint). The maximum of $e(A, \{i\})$ is $\min(d - 1, a)$ and $e(A, \{j\})$ is $\min(d - 1, a)$.

So $c(e) \geq da - 2\binom{a}{2} - 2\min(d-1, a) = da - a(a-1) - 2\min(d-1, a)$.

If $a \leq d - 1$: $c(e) \geq da - a(a-1) - 2a = a(d - a + 1 - 2) = a(d - a - 1)$.

If $a \geq d$: $c(e) \geq da - a(a-1) - 2(d-1) = a(d - a + 1) - 2(d-1) = a(d - a + 1) - 2d + 2$.

Hmm, this is getting complicated. Let me think about it differently.

For the chord that most evenly splits the circle, $a \approx b \approx n/2$. For this chord, $c(e) = e(A, B)$. In a $d$-regular graph, $e(A, B) = da - 2e(A) - e(A, \{i\}) - e(A, \{j\})$. With $a \approx n/2$, $e(A) \leq \binom{n/2}{2}$ and $e(A, \{i\}) + e(A, \{j\}) \leq 2(d-1)$. So $c(e) \geq dn/2 - 2 \cdot \binom{n/2}{2} - 2(d-1) = dn/2 - n(n-2)/4 - 2d + 2$.

For this to be non-negative (i.e., for crossings to be unavoidable), we need $dn/2 > n(n-2)/4 + 2d - 2$, roughly $d > n/2 - 2 + 4/n$, i.e., $n < 2d + 4$. So for $n \leq 2d + 3$ or so, crossings are unavoidable for the bisecting chord.

To minimize crossings, we want $n$ to be large (so that the graph is "sparse" relative to the complete graph, and we can avoid crossings). But as $n$ grows, the bisecting chord has $a \approx n/2$ points on each side, and $c(e) = e(A, B) \geq da - a(a-1) - 2(d-1)$ (for $a \geq d$). With $a = n/2$:

$c(e) \geq d \cdot n/2 - (n/2)(n/2 - 1) - 2(d-1) = dn/2 - n^2/4 + n/2 - 2d + 2$.

$= -n^2/4 + n(d+1)/2 - 2d + 2$.

This is a quadratic in $n$ that's negative for large $n$, meaning the bound becomes trivial (negative). The bound is positive when $n^2/4 < n(d+1)/2 - 2d + 2$, i.e., $n^2 - 2n(d+1) + 8d - 8 < 0$, i.e., $n < (d+1) + \sqrt{(d+1)^2 - 8d + 8} = (d+1) + \sqrt{d^2 - 6d + 9} = (d+1) + |d-3|$.

For $d \geq 3$: $n < (d+1) + (d-3) = 2d - 2$. So for $n \leq 2d - 3$, the bisecting chord must have crossings.

For $n \geq 2d - 2$, the bound becomes negative, meaning we might be able to avoid crossings for the bisecting chord. But we need to check all chords, not just the bisecting one.

Hmm, this analysis is for the bisecting chord. For shorter chords (with small $a$), the bound $c(e) \geq a(d - a - 1)$ (for $a \leq d - 1$) applies. This is non-negative for $a \leq d - 1$, and is 0 for $a = 0$ or $a = d - 1$. So short chords (with $a \leq d - 1$) might have 0 crossings if $a = 0$ or $a = d - 1$.

Wait, $c(e) \geq a(d - a - 1)$ for $a \leq d - 1$. This is 0 when $a = 0$ or $a = d - 1$. For $1 \leq a \leq d - 2$, it's positive. So chords with $a = 1, 2, \ldots, d-2$ must have crossings.

But $a$ is the number of points on one side. If $n$ is large, most chords will have large $a$ and $b$, and the bound for large $a$ might be negative (trivial). The binding constraint comes from chords with $a$ close to $d - 1$.

Actually, let me reconsider. For a chord with $a$ points on the short side ($a \leq (n-2)/2$), the bound is:

If $a \leq d - 1$: $c(e) \geq a(d - a - 1)$.
If $a \geq d$: $c(e) \geq a(d - a + 1) - 2(d - 1) = a(d - a + 1) - 2d + 2$.

For $a \leq d - 1$, the maximum of $a(d - a - 1)$ over $a \in \{1, \ldots, d-2\}$ is at $a = (d-1)/2$, giving roughly $(d-1)^2/4$.

So some chord must have $c(e) \geq \max_{a} a(d - a - 1)$. But which chord? We need to show that in any $d$-regular circular graph, there exists a chord with $a$ in the range where the bound is large.

Hmm, but we get to choose the graph. The question is: what is the minimum over all $d$-regular circular graphs of the maximum $c(e)$?

Let me think about this differently. Consider a $d$-regular graph on $n$ points on a circle. For each chord $e$, let $s(e)$ be the number of points on the shorter side (so $s(e) \leq (n-2)/2$).

If $s(e) \leq d - 2$, then $c(e) \geq s(e)(d - s(e) - 1) \geq 1 \cdot (d - 2) = d - 2$ (for $s(e) = 1$). Actually, $s(e)(d - s(e) - 1)$ for $s(e) = 1$ is $d - 2$, for $s(e) = 2$ is $2(d-3)$, etc. The minimum over $s(e) \in \{1, \ldots, d-2\}$ is $d - 2$ (at $s(e) = 1$) or $d - 2$ (at $s(e) = d - 2$). Actually, $a(d - a - 1)$ at $a = 1$ is $d - 2$, at $a = d - 2$ is $(d-2) \cdot 1 = d - 2$. So the minimum is $d - 2$.

So if there exists a chord with $s(e) \leq d - 2$ (and $s(e) \geq 1$), then $c(e) \geq d - 2$.

But can we avoid having any chord with $1 \leq s(e) \leq d - 2$? That would mean every chord has $s(e) = 0$ (adjacent points) or $s(e) \geq d - 1$.

If every chord connects either adjacent points or points that are at least $d$ apart (in terms of the shorter arc), then... Let me think about what this means.

A chord connecting points at circular distance $r$ (shorter arc has $r - 1$ interior points) has $s(e) = r - 1$. So $s(e) = 0$ means $r = 1$ (adjacent), $s(e) \geq d - 1$ means $r \geq d$.

So we'd need a $d$-regular graph where every edge connects either adjacent points or points at distance $\geq d$. 

The "adjacent" edges form a subgraph of the cycle, which is a collection of paths (or the full cycle). Each vertex can have at most 2 adjacent edges. So at most 2 of the $d$ edges at each vertex are "short" (adjacent), and the remaining $d - 2$ (or $d$) must be "long" (distance $\geq d$).

For the long edges (distance $\geq d$), $s(e) \geq d - 1$. For these, if $s(e) = d - 1$, then $c(e) \geq (d-1)(d - (d-1) - 1) = (d-1) \cdot 0 = 0$. So the bound is 0! And for $s(e) \geq d$, we're in the other case.

So if we can construct a $d$-regular graph where every edge has $s(e) = 0$ or $s(e) = d - 1$, then the bound gives $c(e) \geq 0$ for all edges, which is trivially true. We'd need to check if $c(e) = 0$ is achievable.

But can we have a $d$-regular graph with all edges at distance 1 or $d$? Each vertex has at most 2 edges at distance 1 (to its two neighbors) and needs $d - 2$ more edges at distance $d$. But a vertex can have at most 2 edges at distance $d$ (one in each direction). So the maximum degree from distance-1 and distance-$d$ edges is $2 + 2 = 4$. For $d > 4$, this isn't enough.

So for $d > 4$, we can't avoid having edges at distances $2, 3, \ldots, d-1$, which means some edges have $1 \leq s(e) \leq d - 2$, and those have $c(e) \geq d - 2$.

Wait, but we could also use edges at distance $> d$, which have $s(e) > d - 1$. For those, the bound might be different.

Let me reconsider. For an edge at distance $r$ (so $s(e) = r - 1$), with $r - 1 \geq d$ (i.e., $r \geq d + 1$), we're in the case $a \geq d$:

$c(e) \geq a(d - a + 1) - 2d + 2 = (r-1)(d - r + 2) - 2d + 2$.

For $r = d + 1$: $(d)(d - d - 1 + 2) - 2d + 2 = d \cdot 1 - 2d + 2 = 2 - d$. For $d \geq 3$, this is negative, so the bound is trivial.

For $r = d + 2$: $(d+1)(d - d - 2 + 2) - 2d + 2 = (d+1) \cdot 0 - 2d + 2 = 2 - d$. Also negative for $d \geq 3$.

So for edges with $s(e) \geq d$, the bound is trivial (negative). The binding constraints come from edges with $1 \leq s(e) \leq d - 2$.

Now, the question is: in a $d$-regular circular graph, must there exist an edge with $1 \leq s(e) \leq d - 2$?

If $d \leq 4$: We can have all edges at distance 1 or $d$ (as discussed, max degree 4 from these). For $d = 4$, we can have 2 edges at distance 1 and 2 at distance 4, giving degree 4. So no edge with $1 \leq s(e) \leq 2$, and the bound is trivial. We might achieve $c(e) = 0$ for all edges? Let me check.

For $d = 4$, $n = ?$. We need a 4-regular graph with edges at distances 1 and 4. With $n$ points, distance 4 means connecting $i$ to $i + 4$. For this to not coincide with distance 1, we need $n > 5$. Let's try $n = 8$: connect each $i$ to $i \pm 1$ and $i \pm 4 \pmod{8}$. This gives degree 4. The edges at distance 4 are $(i, i+4)$ for $i = 0, 1, 2, 3$ (4 edges, each counted once). The edges at distance 1 are $(i, i+1)$ for $i = 0, \ldots, 7$ (8 edges). Total 12 edges, $8 \cdot 4 / 2 = 16$... wait, that's 12 edges but $8 \cdot 4 / 2 = 16$. Let me recount.

Each vertex $i$ is connected to $i-1, i+1, i-4, i+4 \pmod{8}$. That's 4 neighbors. But $i + 4 \pmod{8}$ and $i - 4 \pmod{8}$ are the same vertex (since $8/2 = 4$). So each vertex has only 3 distinct neighbors: $i-1, i+1, i+4$. That's degree 3, not 4.

So for $n = 8$, distance 4 is the antipodal distance, and each vertex has only 1 antipodal neighbor. So degree from distances 1 and 4 is $2 + 1 = 3$.

For $n = 9$: distance 4 gives $i + 4$ and $i - 4 = i + 5 \pmod{9}$, which are distinct. So degree from distances 1 and 4 is $2 + 2 = 4$. 

$n = 9$, 4-regular, edges at distances 1 and 4. Let me check if this is non-crossing.

An edge at distance 1: $(i, i+1)$. This is a side of the nonagon. No crossings with other sides. Does it cross any distance-4 edge? A distance-4 edge $(j, j+4)$ crosses $(i, i+1)$ iff one of $j, j+4$ is in the arc from $i$ to $i+1$ (which has no interior points) and the other is outside. Since the arc has no interior points, no crossing. So distance-1 edges don't cross anything.

An edge at distance 4: $(i, i+4)$. This has 3 interior points on the short side. It crosses another distance-4 edge $(j, j+4)$ iff the endpoints alternate. 

Let me check: $(0, 4)$ and $(1, 5)$. Order: 0, 1, 4, 5. We need $0 < 1 < 4 < 5$, so $(0,4)$ and $(1,5)$: is $1$ between 0 and 4? Yes. Is 5 between 0 and 4? No. So they cross. 

So the distance-4 edges do cross each other. So this graph is not non-crossing.

Hmm. So even for $d = 4$, we can't avoid crossings. Let me compute the max $c(e)$ for this graph.

$(0, 4)$: short side has points 1, 2, 3. Long side has points 5, 6, 7, 8. $c = e(\{1,2,3\}, \{5,6,7,8\})$. Edges from {1,2,3} to {5,6,7,8}: distance-1 edges: (8, 0) no... let me list all edges.

Distance-1 edges: (0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8), (8,0).
Distance-4 edges: (0,4), (1,5), (2,6), (3,7), (4,8), (5,0), (6,1), (7,2), (8,3). But (0,4) and (4,0) are the same, (1,5) and (5,1) are the same, etc. So distance-4 edges are: (0,4), (1,5), (2,6), (3,7), (4,8), (5,0)=(0,5)... wait, $5 + 4 = 9 \equiv 0$, so (5, 0) is a distance-4 edge, same as (0, 5). But (0, 4) is also distance 4. So vertex 0 has distance-4 edges to 4 and 5. But $|0 - 4| = 4$ and $|0 - 5| = 5$, and the circular distance is $\min(4, 9 - 4) = 4$ and $\min(5, 9 - 5) = 4$. So both are distance 4. OK.

So distance-4 edges: (0,4), (0,5), (1,5), (1,6), (2,6), (2,7), (3,7), (3,8), (4,8). That's 9 edges. Plus 9 distance-1 edges = 18 edges. $9 \cdot 4 / 2 = 18$. ✓

Now, $c((0,4))$: short side $\{1, 2, 3\}$, long side $\{5, 6, 7, 8\}$.
Edges from {1,2,3} to {5,6,7,8}:
- (1,5): yes (distance 4)
- (1,6): yes (distance 4, since $|1-6| = 5$, circular distance $\min(5, 4) = 4$)
- (2,6): yes
- (2,7): yes
- (3,7): yes
- (3,8): yes
- Any distance-1 edges? (1,2) is within {1,2,3}. (3,4) goes to 4, not in {5,6,7,8}. (8,0) goes to 0. No distance-1 edges cross.
So $c((0,4)) = 6$.

$I((0,4)) = 2 \cdot 4 - 2 + 6 = 12$.

That's quite high. Let me check a distance-1 edge: $(0,1)$. Short side has 0 points, long side has 7. $c = 0$. $I = 6$.

So max $I = 12$ for this graph. Compare with $K_5$ which gave max $I = 8$. So $K_5$ is better for $d = 4$.

Hmm, so larger $n$ doesn't always help. Let me reconsider.

For $d = 4$, $K_5$ gives max $I = 8$. Can we do better?

Let me try $n = 6$, 4-regular ($K_6$ minus a perfect matching). I computed max $I = 8$ earlier. Same as $K_5$.

Can we achieve max $I = 7$? That would require max $c(e) = 1$ (since $I = 6 + c$). Is there a 4-regular circular graph with max crossings per chord = 1?

In $K_5$, the max crossings per chord is 2 (for chords at distance 2, like (1,3)). In $K_6$ minus matching, also 2.

Can we find a 4-regular graph with max crossings 1? That seems hard. Let me think about whether it's possible.

A 4-regular graph on $n$ points with max 1 crossing per chord. The total crossings $C \leq m/1 = m$ (since each chord crosses at most 1 other, and each crossing involves 2 chords, $C \leq m/2$). Actually, $C = \frac{1}{2} \sum c(e) \leq \frac{1}{2} \cdot m \cdot 1 = m/2$.

For a 4-regular graph, $m = 2n$. So $C \leq n$. 

The minimum number of crossings for a 4-regular graph on $n$ points on a circle... I don't know this off the top of my head.

Let me try a different approach. Let me think about what the answer should be for general $d$ and then specialize to $d = 20$.

Let me consider the problem from the perspective of the "friendship" or "intersection" structure.

Actually, let me reconsider the problem statement. It says "each end of each chord is an end of at least $d$ different drawn chords." So every endpoint of every chord has degree $\geq d$. And "chords with a common end intersect" — so sharing an endpoint counts as intersecting.

We want the maximum $M$ such that in any such configuration, some chord intersects at least $M$ others.

I've established that $I(e) \geq 2d - 2 + c(e)$ where $c(e)$ is the number of interior crossings. And $M = 2d - 2 + \min_{\text{config}} \max_e c(e)$.

Now I need to find $\min_{\text{config}} \max_e c(e)$.

Let me think about this more carefully. Consider a $d$-regular graph on $n$ points on a circle. For a chord $e = (i, j)$, let $a$ be the number of points on the shorter arc. We showed:

For $a \leq d - 1$: $c(e) \geq a(d - a - 1)$.
For $a \geq d$: $c(e) \geq a(d - a + 1) - 2(d - 1) = a(d - a + 1) - 2d + 2$.

The first bound is maximized at $a = (d-1)/2$, giving $\approx (d-1)^2/4$.
The second bound is maximized at $a = (d+1)/2$, giving $\approx (d+1)^2/4 - 2d + 2 = (d^2 + 2d + 1)/4 - 2d + 2 = (d^2 - 6d + 9)/4 = (d-3)^2/4$.

So the first bound is stronger (for $d \geq 4$). The maximum of $a(d - a - 1)$ for $a \in \{1, \ldots, d-2\}$ is:

If $d$ is odd, $d = 2k + 1$: max at $a = k$, giving $k \cdot k = k^2 = ((d-1)/2)^2$.
If $d$ is even, $d = 2k$: max at $a = k - 1$ or $a = k$, giving $(k-1) \cdot k = k(k-1) = (d/2)(d/2 - 1) = d(d-2)/4$.

But this is the maximum over $a$ of the lower bound for a specific chord. We need to show that in any $d$-regular circular graph, there EXISTS a chord with large $c(e)$.

The key question is: can we choose the graph so that all chords have small $a$ (say $a = 0$ or $a = d - 1$), avoiding the range where the bound is large?

As I discussed, for $d \leq 4$, we can potentially have all edges at distances 1 and $d$ (giving $a = 0$ or $a = d - 1$), but even then, crossings might occur between the distance-$d$ edges.

For $d \geq 5$, we can't have all edges at distances 1 and $d$ (max degree 4 from these), so we must have edges at other distances, including distances 2 through $d - 1$ (giving $a = 1$ through $d - 2$).

But wait, we could also use edges at distance $> d$ (giving $a \geq d$). For those, the bound is weaker. So the question is: can we construct a $d$-regular graph using only edges at distances 1, $d - 1$, $d$, $d + 1$, etc., avoiding distances 2 through $d - 2$?

The available distances are 1, $d - 1$, $d$, $d + 1$, ..., up to $\lfloor n/2 \rfloor$. Each distance $r$ (with $r < n/2$) contributes 2 edges per vertex (to $i + r$ and $i - r$). Distance $n/2$ (if $n$ is even) contributes 1 edge per vertex.

So from distance 1: 2 edges per vertex.
From distance $d - 1$: 2 edges per vertex.
From distance $d$: 2 edges per vertex.
From distance $d + 1$: 2 edges per vertex.
Etc.

To get degree $d$, we need $d$ edges per vertex. Using distance 1 (2 edges) + distance $d - 1$ (2 edges) = 4 edges. We need $d - 4$ more. Using distances $d, d + 1, \ldots$: each gives 2 edges. So we need $\lceil (d - 4)/2 \rceil$ more distances.

For $d = 20$: 2 (dist 1) + 2 (dist 19) + 2 (dist 20) + 2 (dist 21) + ... We need 20 edges, so 10 distances. Using distances 1, 19, 20, 21, 22, 23, 24, 25, 26, 27: that's 10 distances × 2 = 20 edges. But we need $n$ large enough that these distances are all valid (i.e., $27 \leq \lfloor n/2 \rfloor$, so $n \geq 55$).

But wait, we also need to avoid distances 2 through 18 (which give $a = 1$ through 17, where the bound $a(d - a - 1)$ is large). If we only use distances 1 and $\geq 19$, we avoid these.

But the bound for $a \geq d = 20$ (i.e., distance $\geq 21$) is $c(e) \geq a(d - a + 1) - 2d + 2$. For $a = 20$ (distance 21): $20(20 - 20 + 1) - 40 + 2 = 20 - 38 = -18$. Trivial. For $a = 19$ (distance 20): this is $a = d - 1$, so $c(e) \geq 19(20 - 19 - 1) = 0$. Trivial.

So the bounds are all trivial for distances 1, 19, 20, 21, ..., 27. But that doesn't mean $c(e) = 0$; it just means our lower bound is 0. We need to check if the graph is actually non-crossing or has few crossings.

But a graph with edges at distances 1, 19, 20, ..., 27 on $n = 55$ points will have many crossings between the long edges. For example, edges at distance 20 will cross edges at distance 20, 21, etc.

So the lower bound approach isn't giving us the answer directly. We need a better approach.

Let me think about this problem from a completely different angle.

**Reformulation as a graph theory problem.**

We have a graph $G$ on $n$ vertices arranged on a circle, with minimum degree $d$. Two edges are "intersecting" if they share a vertex or cross inside the circle. We want to find the minimum possible maximum degree of the intersection graph of edges.

Let me think about the intersection graph $H$. The vertices of $H$ are the edges of $G$, and two vertices are adjacent iff the corresponding edges intersect. We want to minimize $\Delta(H)$ (maximum degree of $H$).

$\deg_H(e) = I(e) = \deg_G(u) + \deg_G(v) - 2 + c(e)$ for edge $e = uv$.

Now, let me think about a specific construction that might be optimal.

**Construction: $d$-regular graph on $n = 2d$ points, connecting each point to the $d$ points on the opposite side.**

Wait, I already considered this and it gives the complete graph.

**Construction: $d$-regular graph on $n = 2d + 1$ points, connecting each point to the $d$ nearest points on each side... no, that gives degree $2d$.**

Let me think about the "circulant" graph. A circulant graph $C_n(S)$ connects $i$ to $i + s \pmod{n}$ for each $s \in S$. If $S = \{1, 2, \ldots, k\}$, the degree is $2k$ (for $k < n/2$). For $d = 2k$, this gives a $d$-regular graph.

For $d = 20$, $k = 10$, $S = \{1, 2, \ldots, 10\}$, $n$ large. This connects each point to its 10 nearest neighbors on each side.

For this graph, a chord at distance $r$ (for $r \in \{1, \ldots, 10\}$) has $a = r - 1$ points on the short side. $c(e) = e(A, B)$ where $A$ is the short side.

For a chord $(0, r)$ with $r \leq 10$: $A = \{1, \ldots, r-1\}$, $B = \{r+1, \ldots, n-1\}$. $c(e) = $ number of edges from $A$ to $B$.

An edge from $j \in A$ to $l \in B$ exists iff $|j - l| \pmod{n} \in \{1, \ldots, 10\}$, i.e., $l - j \pmod{n} \in \{1, \ldots, 10\}$ or $j - l \pmod{n} \in \{1, \ldots, 10\}$.

For $j \in \{1, \ldots, r-1\}$ and $l \in \{r+1, \ldots, n-1\}$: $l - j$ ranges from $(r+1) - (r-1) = 2$ to $(n-1) - 1 = n - 2$. The edge exists iff $l - j \leq 10$ or $n - (l - j) \leq 10$, i.e., $l - j \leq 10$ or $l - j \geq n - 10$.

For $n$ large (say $n = 100$), the second condition $l - j \geq 90$ is rarely satisfied. So roughly, $c(e) \approx \sum_{j=1}^{r-1} |\{l \in B : l - j \leq 10\}|$.

For $j$ and $l - j \leq 10$: $l \leq j + 10$. Since $l \geq r + 1$ and $j \leq r - 1$: $l$ ranges from $r + 1$ to $j + 10 \leq r + 9$. So $l \in \{r+1, \ldots, r + 9\}$ (at most 9 values, but also $l \leq n - 1$).

Wait, this is getting complicated. Let me just compute for a specific case.

For $d = 20$, $k = 10$, $n = 100$ (say). Chord $(0, 10)$: $a = 9$, $b = 89$. $A = \{1, \ldots, 9\}$, $B = \{11, \ldots, 99\}$.

$c(e) = \sum_{j=1}^{9} |\{l \in B : |j - l| \pmod{100} \leq 10\}|$.

For $j \in \{1, \ldots, 9\}$, $l \in B = \{11, \ldots, 99\}$: $l - j \in \{11 - 9, \ldots, 99 - 1\} = \{2, \ldots, 98\}$. $|j - l| \pmod{100} \leq 10$ iff $l - j \leq 10$ or $l - j \geq 90$.

$l - j \leq 10$: $l \leq j + 10$. Since $l \geq 11$ and $j \leq 9$: $l \in \{11, \ldots, j + 10\}$. For $j = 1$: $l \in \{11\}$, 1 value. For $j = 2$: $l \in \{11, 12\}$, 2 values. ... For $j = 9$: $l \in \{11, \ldots, 19\}$, 9 values.

$l - j \geq 90$: $l \geq j + 90$. Since $j \leq 9$: $l \geq 91$. $l \in \{91, \ldots, 99\}$, 9 values for each $j$ (since $l - j \leq 98 < 100$, and $l - j \geq 90$ gives $l \geq j + 90$, and $l \leq 99$). For $j = 1$: $l \in \{91, \ldots, 99\}$, 9 values. For $j = 9$: $l \in \{99\}$, 1 value.

So $c(e) = \sum_{j=1}^{9} (j + (10 - j)) = \sum_{j=1}^{9} 10 = 90$.

$I(e) = 2 \cdot 20 - 2 + 90 = 128$.

That's a lot. The circulant graph with $n = 100$ is not good.

Let me try a different construction. What about using a small $n$?

For $d = 20$, the smallest $n$ for a 20-regular graph is $n = 21$ (complete graph $K_{21}$). Let me compute the max $I(e)$ for $K_{21}$.

In $K_{21}$, every vertex has degree 20. For a chord $(i, j)$ with $a$ points on one side and $b = 19 - a$ on the other, $c(e) = a \cdot b$ (all pairs across). $I(e) = 38 + ab$.

The maximum of $ab$ for $a + b = 19$ is at $a = 9, b = 10$ (or vice versa): $ab = 90$. So max $I = 38 + 90 = 128$.

For $n = 22$, 20-regular graph: this is $K_{22}$ minus a 1-factor (perfect matching). $m = 22 \cdot 20 / 2 = 220$ edges. For a chord $(i,j)$ with $a$ points on one side, $b = 20 - a$ on the other: $c(e) = e(A, B)$. In $K_{22}$ minus a matching, $e(A, B) = ab - m_{AB}$ where $m_{AB}$ is the number of matching edges between $A$ and $B$. Each matching edge connects two vertices; the number of matching edges with one endpoint in $A$ and one in $B$ is at most $\min(a, b)$.

So $c(e) \geq ab - \min(a, b)$. For $a = 10, b = 10$: $c \geq 100 - 10 =         — AI历史解题过程（thinking）
#   polymath_04312         — 题目ID

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
  <problem_id>polymath_04312</problem_id>
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

Given an integer $d \ge 2$ and a circle $\omega$, a finite number of chords are drawn such that each end of each chord is an end of at least $d$ different drawn chords. We assume that chords with a common end intersect. Let $M$ be the maximum possible value such that for any such configuration of chords, there must exist a chord which intersects at least $M$ other chords. 

Find the value of $M$ when $d = 20$.

## Standard Solution

The problem asks for the minimum possible value of the maximum number of intersections a chord can have. According to the original proof, for any integer $d$, there exists a chord that intersects at least $\lceil d^2/4 \rceil$ other chords if $d$ is even, or a slightly different value if $d$ is odd. Specifically, the proof concludes that for $d=2k$, the number of intersections is at least $k^2$ (as $\lceil (2k)^2/4 \rceil = k^2$). For $d=20$, $k=10$, so the number of intersections is $10^2 = 100$.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have a circle with chords drawn such that each endpoint of each chord is an endpoint of at least $d$ different drawn chords. Chords with a common endpoint intersect. We need to find the maximum $M$ such that in any such configuration, some chord intersects at least $M$ others.

Let me think about this carefully.

First, let me set up the model. We have a set of points on a circle (the endpoints), and a set of chords (pairs of points). Each point that is used as an endpoint is an endpoint of at least $d$ chords. Two chords intersect if they share an endpoint OR if they cross in the interior of the circle.

Wait, let me re-read: "We assume that chords with a common end intersect." So chords sharing an endpoint count as intersecting. And chords that cross in the interior also intersect. So two chords intersect if they share an endpoint or cross inside the circle.

We want: for any configuration satisfying the degree condition (each used point has degree $\geq d$), there exists a chord intersecting at least $M$ other chords. Find the maximum such $M$ for $d = 20$.

So $M$ is the minimum over all valid configurations of the maximum number of chords intersecting a single chord. We want to find this minimum.

Let me think about this as a graph problem. The vertices are the points on the circle, edges are chords. This is a "circle graph" or more precisely the intersection graph of chords.

Actually, let me think of it differently. We have a graph $G$ whose vertices are points on a circle and whose edges are chords. The condition is: every vertex has degree $\geq d$. Two edges "intersect" if they share a vertex or cross inside the circle.

The intersection graph of the edges (chords) is what we care about. We want the minimum possible maximum degree of this intersection graph, over all such chord configurations.

Let me think about what determines whether two chords cross. If we label the points $1, 2, \ldots, n$ around the circle, two chords $(a,b)$ and $(c,d)$ with $a < b$ and $c < d$ cross iff exactly one of $c, d$ is in the interval $(a, b)$, i.e., $a < c < b < d$ or $c < a < d < b$.

So the number of chords that a given chord $(a, b)$ intersects equals:
- (number of chords sharing endpoint $a$ or $b$) + (number of chords crossing $(a,b)$ in the interior) - (chords sharing both endpoints, counted twice, but that's just the chord itself... no).

Actually, let me be careful. A chord $e = (a,b)$ intersects another chord $f$ if:
1. $f$ shares an endpoint with $e$ (i.e., $f$ is incident to $a$ or $b$), OR
2. $f$ crosses $e$ in the interior.

These are mutually exclusive for $f \neq e$ (if $f$ shares an endpoint with $e$, it doesn't cross in the interior; if it crosses in the interior, it doesn't share an endpoint).

So the number of chords intersecting $e = (a,b)$ is:
$$\deg(a) + \deg(b) - 2 + (\text{number of chords crossing } (a,b) \text{ in interior})$$

Wait, $\deg(a)$ counts all chords incident to $a$, including $e$ itself. So chords incident to $a$ other than $e$: $\deg(a) - 1$. Similarly for $b$. But a chord incident to both $a$ and $b$ would be $e$ itself (assuming no multi-edges). So the number of chords sharing an endpoint with $e$ is $(\deg(a) - 1) + (\deg(b) - 1) = \deg(a) + \deg(b) - 2$.

Plus the number of chords crossing $e$ in the interior.

Let me denote by $c(e)$ the number of chords crossing $e$ in the interior. Then the number of chords intersecting $e$ is:
$$I(e) = \deg(a) + \deg(b) - 2 + c(e)$$

Since $\deg(a) \geq d$ and $\deg(b) \geq d$, we have $I(e) \geq 2d - 2 + c(e) \geq 2d - 2$.

So $M \geq 2d - 2$. For $d = 20$, $M \geq 38$.

But can we always achieve $c(e) = 0$ for all chords? That would mean no two chords cross in the interior. This means the chord diagram is "non-crossing" — it's a planar graph on the circle, i.e., a triangulation-like structure or more generally a non-crossing matching/graph.

If we have a non-crossing set of chords where every vertex has degree exactly $d$, then $I(e) = 2d - 2$ for every chord, and $M = 2d - 2$.

But can we construct such a configuration? A non-crossing graph on $n$ points on a circle where every vertex has degree $d$.

A non-crossing graph on $n$ points on a circle is a planar graph. The maximum number of edges in a planar graph on $n$ vertices is $3n - 6$ (for $n \geq 3$). The sum of degrees is $2 \cdot |E| \leq 2(3n-6) = 6n - 12$. If every vertex has degree $\geq d$, then $nd \leq 6n - 12$, so $n(d-6) \leq -12$, which means $d \leq 6$ (for large $n$). Actually for $d \geq 7$, we'd need $n \leq 12/(6-d)$ which is negative, impossible.

Wait, so for $d \geq 7$, we can't have a non-crossing configuration! That means some chords must cross, and $c(e) > 0$ for some chords.

Hmm wait, but actually the problem says "a finite number of chords are drawn such that each end of each chord is an end of at least $d$ different drawn chords." So every endpoint of every chord has degree $\geq d$. We need to find configurations where this holds.

For $d = 20$, we definitely can't have a non-crossing configuration. So we need to think more carefully.

Let me reconsider. The question is: what is the minimum over all valid configurations of the maximum $I(e)$ over all chords $e$?

We showed $I(e) \geq 2d - 2 = 38$ for all $e$. The question is whether we can achieve $I(e) = 38$ for all $e$, or whether we're forced to have some chord with more intersections.

To have $I(e) = 38$ for all $e$, we need $\deg(v) = d = 20$ for all vertices $v$ (so the graph is $d$-regular) and $c(e) = 0$ for all $e$ (non-crossing). But as we showed, a non-crossing $d$-regular graph on a circle requires $d \leq 6$ roughly. So for $d = 20$, this is impossible.

So we need crossings. Let me think about this more carefully.

Let me reconsider the problem. We want to minimize the maximum of $I(e) = \deg(a) + \deg(b) - 2 + c(e)$ over all chords $e = (a,b)$.

Since every vertex has degree $\geq d$, we have $I(e) \geq 2d - 2 + c(e)$.

Now, the total number of crossings. Let $C$ be the total number of crossing pairs. Then $\sum_e c(e) = 2C$ (each crossing pair contributes to $c(e)$ for both chords).

We need to find a lower bound on $\max_e c(e)$ or more precisely on $\max_e I(e)$.

Let me think about this differently. Let's consider the structure more carefully.

Actually, let me think about what configurations look like. We have $n$ points on a circle, and a $d$-regular (or minimum degree $d$) graph whose edges are chords. We want to minimize the maximum number of chords intersecting any single chord.

Let me think about small cases first to get intuition.

For the crossing part: two chords $(a,b)$ and $(c,d)$ cross iff their endpoints alternate around the circle. 

Let me think about a specific construction. Consider $n$ points equally spaced. Connect each point $i$ to points $i+1, i+2, \ldots, i+d/2$ (mod $n$) if $d$ is even. This gives a $d$-regular graph (if $n$ is large enough). But this has lots of crossings.

Actually, let me think about this problem from the perspective of the answer. The answer for $d = 20$ is likely $2d - 2 = 38$ or something related. But we showed that non-crossing is impossible for $d = 20$.

Hmm, let me reconsider. Maybe the answer is larger than $2d - 2$.

Let me think about it from a different angle. Consider the "intersection graph" $H$ of the chords: vertices of $H$ are chords, and two vertices are adjacent iff the corresponding chords intersect. We want to find the minimum possible maximum degree of $H$.

The number of vertices of $H$ is the number of chords, say $m$. The degree of a chord $e = (a,b)$ in $H$ is $I(e) = \deg_G(a) + \deg_G(b) - 2 + c(e)$.

Now, let's think about the total. $\sum_e I(e) = \sum_e (\deg(a_e) + \deg(b_e) - 2) + \sum_e c(e) = \sum_v \deg(v)^2 - 2m + 2C$.

Hmm, this is getting complicated. Let me think about specific constructions.

**Construction 1: Complete graph $K_n$.** 

Take $n$ points and draw all $\binom{n}{2}$ chords. Every vertex has degree $n-1$. For this to satisfy the condition, we need $n - 1 \geq d$, so $n \geq d + 1$.

For a chord $(a,b)$ in $K_n$: $\deg(a) = \deg(b) = n-1$, so $\deg(a) + \deg(b) - 2 = 2n - 4$. The number of chords crossing $(a,b)$: a chord $(c,d)$ crosses $(a,b)$ iff one of $c,d$ is in the arc from $a$ to $b$ and the other is in the arc from $b$ to $a$. If there are $k$ points on one side and $n - 2 - k$ on the other, the number of crossing chords is $k(n-2-k)$. The maximum of $k(n-2-k)$ is $(n-2)^2/4$.

So $I(e) = 2n - 4 + k(n-2-k)$. The maximum over all chords is at least $2n - 4 + (n-2)^2/4$ (achieved by the "diameter" chords). For $n = d + 1 = 21$, this is $2 \cdot 17 + 19^2/4 = 38 + 90.25 = 128.25$, so about 128. That's much larger than 38.

So the complete graph is a bad construction for minimizing the maximum.

**Construction 2: Try to minimize crossings.**

We want a $d$-regular graph on $n$ points on a circle with as few crossings as possible, and with the crossings distributed evenly.

Actually, we don't need $d$-regular; we need minimum degree $\geq d$. But to minimize $I(e)$, we'd want degrees to be exactly $d$.

Let me think about what graph structure minimizes crossings for a given degree sequence on a circle.

A key insight: for points on a circle, the number of crossings is minimized when the graph is "as planar as possible." But for $d = 20$, we can't have a planar graph with minimum degree 20.

The maximum degree of a planar graph is unbounded, but the average degree is at most 6. For minimum degree $d$, we need average degree $\geq d$, so $d \leq 6$ for planar (outerplanar, actually, since all vertices are on the circle).

Wait, all vertices are on the circle, so the graph is an "outerplanar" graph if it's non-crossing. For outerplanar graphs, the maximum number of edges is $2n - 3$ (for $n \geq 2$), so the average degree is at most $2(2n-3)/n = 4 - 6/n < 4$. So for minimum degree $d$, we need $d \leq 3$ (since average degree $< 4$ means some vertex has degree $\leq 3$).

So for $d \geq 4$, we can't even have a non-crossing configuration! For $d = 20$, we definitely need crossings.

OK so let me think about this more carefully. The problem is asking for the answer when $d = 20$. Let me think about what the general answer might be.

Let me consider a different approach. Think of the points on the circle and the chords. For each chord $e = (a,b)$, let $s(e)$ be the number of points strictly inside the arc from $a$ to $b$ (say, the smaller arc, or let's say we go clockwise from $a$ to $b$ and count points in between). Actually, let me define it more carefully.

Label points $1, 2, \ldots, n$ clockwise. For chord $(i, j)$ with $i < j$, let $a = j - i - 1$ (points between $i$ and $j$ clockwise) and $b = n - (j - i + 1) = n - j + i - 1$ (points between $j$ and $i$ clockwise, i.e., the other arc). So $a + b = n - 2$.

The number of chords crossing $(i,j)$ is the number of chords with one endpoint in the arc $\{i+1, \ldots, j-1\}$ and the other in $\{j+1, \ldots, n, 1, \ldots, i-1\}$.

Let me denote the two arcs as $A$ (with $a$ points) and $B$ (with $b$ points), $a + b = n - 2$.

The number of crossing chords $c(e) = e(A, B)$ where $e(A, B)$ is the number of edges between $A$ and $B$ in the graph.

Now, the sum of degrees of vertices in $A$ is $\sum_{v \in A} \deg(v) \geq da$. This sum counts edges within $A$ twice and edges from $A$ to $\{i, j\} \cup B$ once. So:
$$\sum_{v \in A} \deg(v) = 2e(A) + e(A, \{i\}) + e(A, \{j\}) + e(A, B)$$

where $e(A)$ is edges within $A$, $e(A, \{i\})$ is edges from $A$ to $i$, etc.

So $e(A, B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

Similarly, $e(A, B) = \sum_{v \in B} \deg(v) - 2e(B) - e(B, \{i\}) - e(B, \{j\})$.

Now, $e(A, \{i\}) + e(A, \{j\}) + e(B, \{i\}) + e(B, \{j\}) = \deg(i) + \deg(j) - 2$ (subtracting 2 for the edge $(i,j)$ itself, assuming it exists; actually $\deg(i) = e(A, \{i\}) + e(B, \{i\}) + 1$ (the $+1$ for edge to $j$) and similarly $\deg(j) = e(A, \{j\}) + e(B, \{j\}) + 1$, so $e(A, \{i\}) + e(B, \{i\}) + e(A, \{j\}) + e(B, \{j\}) = \deg(i) + \deg(j) - 2$).

Also, $e(A) + e(B) + e(A, B) + e(A, \{i\}) + e(A, \{j\}) + e(B, \{i\}) + e(B, \{j\}) + 1 = m$ (total edges, the $+1$ is for edge $(i,j)$).

From the two expressions for $e(A,B)$:
$$2e(A,B) = \sum_{v \in A} \deg(v) + \sum_{v \in B} \deg(v) - 2e(A) - 2e(B) - (\deg(i) + \deg(j) - 2)$$

$$= \sum_{v \neq i,j} \deg(v) - 2(e(A) + e(B)) - \deg(i) - \deg(j) + 2$$

$$= 2m - \deg(i) - \deg(j) - 2(e(A) + e(B)) - \deg(i) - \deg(j) + 2$$

Wait, $\sum_{v \neq i,j} \deg(v) = 2m - \deg(i) - \deg(j)$. And $e(A) + e(B) = m - e(A,B) - (\deg(i) + \deg(j) - 2) - 1 = m - e(A,B) - \deg(i) - \deg(j) + 1$.

So:
$$2e(A,B) = 2m - \deg(i) - \deg(j) - 2(m - e(A,B) - \deg(i) - \deg(j) + 1) - \deg(i) - \deg(j) + 2$$
$$= 2m - \deg(i) - \deg(j) - 2m + 2e(A,B) + 2\deg(i) + 2\deg(j) - 2 - \deg(i) - \deg(j) + 2$$
$$= 2e(A,B)$$

OK, that's circular (as expected). Let me try a different approach.

From $e(A,B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$:

Since $\sum_{v \in A} \deg(v) \geq da$ and $e(A, \{i\}) + e(A, \{j\}) \leq \deg(i) + \deg(j) - 2$ (actually this is an overcount since some of $i$'s and $j$'s edges go to $B$), and $e(A) \geq 0$:

$$e(A,B) \geq da - e(A, \{i\}) - e(A, \{j\}) \geq da - (\deg(i) - 1) - (\deg(j) - 1) = da - \deg(i) - \deg(j) + 2$$

Hmm, but this could be negative. Let me also use the other side:

$$e(A,B) \geq db - \deg(i) - \deg(j) + 2$$

So $e(A,B) \geq \max(da, db) - \deg(i) - \deg(j) + 2$.

Actually, we can do better. From $e(A,B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A,\{i\}) - e(A,\{j\})$:

We have $e(A,\{i\}) \leq \deg(i) - 1$ and $e(A,\{j\}) \leq \deg(j) - 1$, so $e(A,\{i\}) + e(A,\{j\}) \leq \deg(i) + \deg(j) - 2$.

Also $2e(A) \leq a(a-1)$ (max edges within $A$) but that's not useful for a lower bound.

So $c(e) = e(A,B) \geq da - (\deg(i) + \deg(j) - 2) = da - \deg(i) - \deg(j) + 2$.

And similarly $c(e) \geq db - \deg(i) - \deg(j) + 2$.

So $c(e) \geq \max(a, b) \cdot d - \deg(i) - \deg(j) + 2$.

Since $a + b = n - 2$, $\max(a, b) \geq (n-2)/2$.

If the graph is $d$-regular, $\deg(i) = \deg(j) = d$, so:
$$c(e) \geq \max(a, b) \cdot d - 2d + 2 = d(\max(a,b) - 2) + 2$$

Wait, that doesn't seem right. Let me redo: $c(e) \geq da - 2d + 2 = d(a - 2) + 2$ and $c(e) \geq d(b-2) + 2$.

So $c(e) \geq d(\max(a,b) - 2) + 2 \geq d((n-2)/2 - 2) + 2 = d(n-6)/2 + 2$.

And $I(e) = 2d - 2 + c(e) \geq 2d - 2 + d(\max(a,b) - 2) + 2 = 2d + d(\max(a,b) - 2) = d \cdot \max(a,b)$.

Hmm wait, let me recompute. $I(e) = \deg(i) + \deg(j) - 2 + c(e) = 2d - 2 + c(e)$.

And $c(e) \geq d \cdot \max(a,b) - 2d + 2$.

So $I(e) \geq 2d - 2 + d \cdot \max(a,b) - 2d + 2 = d \cdot \max(a,b)$.

Interesting! So $I(e) \geq d \cdot \max(a, b)$ where $a, b$ are the number of points on each side of the chord.

Since $\max(a, b) \geq (n-2)/2$, we get $I(e) \geq d(n-2)/2$.

But this depends on $n$, which we can choose. To minimize the maximum $I(e)$, we'd want $n$ to be as small as possible. The minimum $n$ for a $d$-regular graph is $n = d + 1$ (complete graph). But then $\max(a, b) \approx (n-2)/2 = (d-1)/2$, giving $I(e) \geq d(d-1)/2$, which for $d = 20$ is $20 \cdot 19 / 2 = 190$. That's way more than 38.

But wait, we don't need $d$-regular. We need minimum degree $\geq d$. And we want to minimize the maximum $I(e)$.

Hmm, but the bound $I(e) \geq d \cdot \max(a,b)$ used $\deg(i) = \deg(j) = d$ (regular). If degrees are higher, the bound on $c(e)$ is weaker (since $c(e) \geq da - \deg(i) - \deg(j) + 2$), but $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq \deg(i) + \deg(j) - 2 + da - \deg(i) - \deg(j) + 2 = da$.

Oh interesting! So regardless of the degrees of $i$ and $j$:
$$I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq \deg(i) + \deg(j) - 2 + (da - \deg(i) - \deg(j) + 2) = da$$

And similarly $I(e) \geq db$.

So $I(e) \geq d \cdot \max(a, b)$.

This is a clean bound! Let me double-check.

$c(e) = e(A, B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

$\sum_{v \in A} \deg(v) \geq d \cdot |A| = da$.

$e(A, \{i\}) + e(A, \{j\}) \leq \deg(i) + \deg(j) - 2$ (since $e(A,\{i\}) \leq \deg(i) - 1$ because at least one edge from $i$ goes to $j$, and similarly for $j$; actually, $e(A, \{i\}) \leq \deg(i) - 1$ only if the edge $(i,j)$ exists, which it does since $e = (i,j)$ is a chord).

Wait, actually $e(A, \{i\})$ is the number of edges from $i$ to vertices in $A$. Since $\deg(i)$ counts all edges from $i$, and one of them goes to $j$, we have $e(A, \{i\}) \leq \deg(i) - 1$. Similarly $e(A, \{j\}) \leq \deg(j) - 1$. So $e(A, \{i\}) + e(A, \{j\}) \leq \deg(i) + \deg(j) - 2$.

And $e(A) \geq 0$.

So $c(e) \geq da - 0 - (\deg(i) + \deg(j) - 2) = da - \deg(i) - \deg(j) + 2$.

Therefore $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq \deg(i) + \deg(j) - 2 + da - \deg(i) - \deg(j) + 2 = da$.

Similarly, using the $B$ side: $I(e) \geq db$.

So $I(e) \geq d \cdot \max(a, b) \geq d \cdot \lceil (n-2)/2 \rceil$.

Now, to minimize this, we want to minimize $n$. What's the minimum $n$?

We need a graph on $n$ vertices (points on a circle) with minimum degree $\geq d$. The minimum $n$ for a simple graph with minimum degree $d$ is $n = d + 1$ (the complete graph $K_{d+1}$).

With $n = d + 1$: $\max(a, b) \geq \lceil (d - 1)/2 \rceil$. For $d = 20$: $\max(a,b) \geq \lceil 19/2 \rceil = 10$. So $I(e) \geq 20 \cdot 10 = 200$.

But wait, can we do better with a larger $n$? No—a larger $n$ makes $\max(a,b)$ larger, which makes the bound worse. So the minimum $n$ gives the best bound.

But wait, is this bound tight? Can we actually achieve $I(e) = d \cdot \max(a,b)$ for all chords?

Let me check with $n = d + 1$, the complete graph $K_{d+1}$. For $d = 20$, $n = 21$. For a chord $(i,j)$, $a + b = 19$. The maximum of $a, b$ is at least 10. For a chord that splits the remaining 19 points into 10 and 9, $\max(a,b) = 10$, so $I(e) \geq 200$.

In $K_{21}$, $I(e) = \deg(i) + \deg(j) - 2 + c(e) = 20 + 20 - 2 + c(e) = 38 + c(e)$. And $c(e) = a \cdot b$ (in the complete graph, every pair of points on opposite sides gives a crossing chord). For $a = 10, b = 9$: $c(e) = 90$. So $I(e) = 38 + 90 = 128$.

But our bound says $I(e) \geq d \cdot \max(a,b) = 20 \cdot 10 = 200$. But we computed $I(e) = 128$. That's a contradiction!

Let me recheck. Oh wait, I think I made an error. Let me recheck the bound.

$c(e) = e(A, B)$. In $K_{21}$, $e(A, B) = |A| \cdot |B| = a \cdot b$. For $a = 10, b = 9$: $c(e) = 90$.

$I(e) = 38 + 90 = 128$.

But the bound says $I(e) \geq da = 20 \cdot 10 = 200$. That's clearly wrong since $128 < 200$.

Let me find the error. 

$c(e) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

In $K_{21}$: $\sum_{v \in A} \deg(v) = 10 \cdot 20 = 200$. $e(A) = \binom{10}{2} = 45$. $e(A, \{i\}) = 10$ (all vertices in $A$ are connected to $i$). $e(A, \{j\}) = 10$.

$c(e) = 200 - 90 - 10 - 10 = 90$. ✓

Now, $e(A, \{i\}) + e(A, \{j\}) = 20$. And $\deg(i) + \deg(j) - 2 = 38$. So $e(A, \{i\}) + e(A, \{j\}) = 20 \leq 38$. ✓

The bound was: $c(e) \geq da - (\deg(i) + \deg(j) - 2) = 200 - 38 = 162$. But actual $c(e) = 90 < 162$. 

The issue is that $e(A, \{i\}) + e(A, \{j\}) = 20$, which is much less than $\deg(i) + \deg(j) - 2 = 38$. The bound $e(A, \{i\}) + e(A, \{j\}) \leq \deg(i) + \deg(j) - 2$ is correct but very loose, because many of $i$'s and $j$'s edges go to $B$, not $A$.

So the bound $I(e) \geq d \cdot \max(a,b)$ is wrong. Let me redo this.

$c(e) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

We have $\sum_{v \in A} \deg(v) \geq da$, $e(A) \geq 0$, $e(A, \{i\}) \geq 0$, $e(A, \{j\}) \geq 0$.

So $c(e) \geq da - 2e(A) - e(A, \{i\}) - e(A, \{j\})$. But we can't bound $e(A, \{i\})$ and $e(A, \{j\})$ from above tightly without more info.

Actually, $e(A, \{i\}) \leq \min(\deg(i) - 1, a)$ and $e(A, \{j\}) \leq \min(\deg(j) - 1, a)$.

So $c(e) \geq da - 2e(A) - \min(\deg(i)-1, a) - \min(\deg(j)-1, a)$.

And $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq \deg(i) + \deg(j) - 2 + da - 2e(A) - \min(\deg(i)-1, a) - \min(\deg(j)-1, a)$.

If $\deg(i) - 1 \leq a$ and $\deg(j) - 1 \leq a$ (which is the case when $a$ is large), then:
$I(e) \geq \deg(i) + \deg(j) - 2 + da - 2e(A) - (\deg(i) - 1) - (\deg(j) - 1) = da - 2e(A)$.

If $e(A) = 0$ (no edges within $A$), then $I(e) \geq da$. But in $K_{21}$, $e(A) = 45 \neq 0$, so this doesn't apply.

OK so the bound depends on $e(A)$, the number of edges within $A$. Let me think about this differently.

Let me try a different approach. Instead of trying to get a universal lower bound, let me think about what configuration minimizes the maximum $I(e)$.

Let me think about the problem from the perspective of the answer. This is a competition problem, and the answer for $d = 20$ is likely a clean expression in $d$.

Let me consider the possibility that the answer is $2d - 2 = 38$. For this to work, we'd need a configuration where every chord has $c(e) = 0$ (no crossings) and $\deg(v) = d$ for all $v$. But we showed this is impossible for $d \geq 4$ (outerplanar graphs have average degree $< 4$).

What about $d^2 - 1$? Or $d(d-1)$? Or $d^2$? Let me think...

Actually, let me reconsider. Maybe the answer involves $d^2$ or $d(d-1)$.

Let me think about a specific construction that might be optimal.

**Construction: $d$-regular graph on $2d$ vertices.**

Consider $2d$ points on a circle. Connect each point to the $d$ nearest points (including both directions). Actually, let me think of a specific good construction.

Hmm, let me think about this more carefully. 

Actually, let me reconsider the problem. The key constraint is that each endpoint has degree $\geq d$. We want to minimize the maximum number of intersections per chord.

Let me think about a "star-like" construction. Suppose we have $d + 1$ points, and one of them (say point 0) is connected to all other $d$ points. Then point 0 has degree $d$, but the other points have degree 1 (from the edge to 0). To get their degree up to $d$, we need more edges.

Actually, let me think about the problem differently. Let me consider the "thrackle" perspective or think about what structure minimizes crossings.

Let me try to think about what happens with $n = 2d$ points.

Consider $2d$ points on a circle, labeled $0, 1, \ldots, 2d-1$. Consider the "antipodal" matching: connect $i$ to $i + d$ for each $i = 0, 1, \ldots, d-1$. This gives $d$ chords, all passing through the center, and they all cross each other. Each point has degree 1. Not enough.

Let me think about a different construction. Consider $n$ points and connect each point to its $d$ nearest neighbors (in terms of circular distance). If $d$ is even, say $d = 2k$, connect each point to the $k$ nearest on each side. This gives a $d$-regular graph.

For this graph, the chord $(i, i+r)$ where $1 \leq r \leq k$ has $a = r - 1$ points on one side and $b = n - r - 1$ on the other. The number of crossings depends on the structure.

This is getting complicated. Let me try to think about the problem from a higher level.

The answer $M$ is the minimum over all valid configurations of the maximum $I(e)$. We need to find both a lower bound (every configuration has a chord with $\geq M$ intersections) and a matching upper bound (there exists a configuration where every chord has $\leq M$ intersections).

Let me think about the lower bound more carefully.

For any chord $e = (i,j)$, $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq 2d - 2 + c(e)$.

So if we can show that some chord must have $c(e) \geq X$, then $M \geq 2d - 2 + X$.

The total number of crossings is $C = \frac{1}{2} \sum_e c(e)$. If we can lower bound $C$ and upper bound the number of chords $m$, then some chord has $c(e) \geq 2C/m$.

But this might not give a tight bound. Let me think differently.

Actually, let me think about a specific chord. Consider the chord that has the most "balanced" split, i.e., $\max(a,b)$ is minimized. For any chord, $\max(a,b) \geq (n-2)/2$. The chord that achieves $\max(a,b) = \lceil (n-2)/2 \rceil$ is one that nearly bisects the circle.

For this chord, $c(e) = e(A, B)$. Now, $\sum_{v \in A} \deg(v) \geq da$ and $\sum_{v \in B} \deg(v) \geq db$. The total degree is $\sum_v \deg(v) \geq dn$, so $m \geq dn/2$.

$e(A, B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

Also, $e(A) + e(A, \{i\}) + e(A, \{j\}) + e(A, B) = $ (edges with at least one endpoint in $A$) $= \sum_{v \in A} \deg(v) - e(A)$. Wait, no. $\sum_{v \in A} \deg(v) = 2e(A) + e(A, \{i\}) + e(A, \{j\}) + e(A, B)$. So $e(A, B) = \sum_{v \in A} \deg(v) - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

The number of edges with at least one endpoint in $A$ is $e(A) + e(A, \{i\}) + e(A, \{j\}) + e(A, B) = \sum_{v \in A} \deg(v) - e(A)$.

Hmm, I'm going in circles (no pun intended). Let me try to think about this problem from the answer's perspective.

For competition problems of this type, the answer is often $d^2 - 1$ or $2d - 2$ or $d^2$ or similar. Let me think about which one.

Let me try to construct a configuration where the maximum $I(e)$ is as small as possible, for general $d$.

**Key idea: Use a complete bipartite-like structure or a specific regular graph.**

Let me try $n = 2d$ points, and connect each point to the $d$ points farthest from it (i.e., the $d$ points on the "other side" of the circle). Specifically, label points $0, 1, \ldots, 2d-1$. Connect $i$ to $i+d, i+d+1, \ldots, i+2d-1 \pmod{2d}$... no, that's everything.

Let me try a different approach. Consider $n = 2d$ points. Connect point $i$ to points $i+1, i+2, \ldots, i+d \pmod{2d}$. Wait, that gives degree $d$ for each point. But point $i$ is connected to $i+d$, and point $i+d$ is connected to $i+d+1, \ldots, i+2d = i$, so yes, the edge $(i, i+d)$ is counted from both sides. Actually, let me be more careful.

If we connect $i$ to $i+1, i+2, \ldots, i+d \pmod{2d}$, then each point has degree $d$ (out-degree $d$, but since the graph is undirected, we need to check). Point $i$ is connected to $i+1, \ldots, i+d$. Point $j$ is connected to $j+1, \ldots, j+d$. The edge $(i, j)$ exists iff $j - i \pmod{2d} \in \{1, 2, \ldots, d\}$ or $i - j \pmod{2d} \in \{1, 2, \ldots, d\}$. Since $j - i \pmod{2d} \in \{1, \ldots, d\}$ or $i - j \pmod{2d} \in \{1, \ldots, d\}$, and these are complementary (one is in $\{1, \ldots, d\}$ iff the other is in $\{d, \ldots, 2d-1\}$... wait, if $j - i \equiv r \pmod{2d}$ with $1 \leq r \leq d$, then $i - j \equiv 2d - r \pmod{2d}$ with $d \leq 2d - r \leq 2d - 1$. So the edge exists iff $r \in \{1, \ldots, d\}$, which is the same as $2d - r \in \{d, \ldots, 2d-1\}$. So the condition is: $j - i \pmod{2d} \in \{1, \ldots, d\}$. But this means each ordered pair $(i, j)$ with $j - i \pmod{2d} \in \{1, \ldots, d\}$ gives an edge. The number of such $j$ for each $i$ is $d$. But we're double-counting: edge $(i, j)$ with $j - i \equiv r$ is the same as edge $(j, i)$ with $i - j \equiv 2d - r$. So the degree of each vertex is $d$ (since for each $i$, there are exactly $d$ values of $j$ with $j - i \pmod{2d} \in \{1, \ldots, d\}$, and each gives a unique edge).

Wait, but if $r = d$, then $j - i \equiv d$ and $i - j \equiv d$ (mod $2d$). So the edge $(i, i+d)$ is counted once from $i$'s perspective (with $r = d$) and once from $i+d$'s perspective (with $r = d$). So it's not double-counted in the degree; it's just one edge. So the degree is $d$ for each vertex. Good.

But wait, is this a valid simple graph? The edge $(i, i+d)$ exists. Also, $(i, i+1), (i, i+2), \ldots, (i, i+d)$. And from $i-1$: $(i-1, i), (i-1, i+1), \ldots, (i-1, i+d-1)$. So edge $(i-1, i)$ exists. From $i-d$: $(i-d, i-d+1), \ldots, (i-d, i)$. So edge $(i-d, i)$ exists. So vertex $i$ is connected to $i-d, i-d+1, \ldots, i-1, i+1, \ldots, i+d$. That's $2d$ neighbors, but we said degree is $d$. 

Hmm, I think I'm confusing myself. Let me recount. Vertex $i$ is connected to $j$ iff $j - i \pmod{2d} \in \{1, 2, \ldots, d\}$. So the neighbors of $i$ are $i+1, i+2, \ldots, i+d \pmod{2d}$. That's $d$ neighbors. But also, $j$ is connected to $i$ iff $i - j \pmod{2d} \in \{1, \ldots, d\}$, i.e., $j$ is connected to $i$ iff $j$ is one of $i-1, i-2, \ldots, i-d \pmod{2d}$. So the full neighbor set of $i$ is $\{i+1, \ldots, i+d, i-1, \ldots, i-d\} \pmod{2d}$... no, that's not right either.

The graph is undirected. Edge $(i, j)$ exists iff $j - i \pmod{2d} \in \{1, \ldots, d\}$ OR $i - j \pmod{2d} \in \{1, \ldots, d\}$. Since $j - i \pmod{2d} \in \{1, \ldots, 2d-1\}$ (assuming $i \neq j$), and $\{1, \ldots, d\} \cup \{d, \ldots, 2d-1\} = \{1, \ldots, 2d-1\}$ (with $d$ in both), the edge exists for all $j \neq i$ except when... wait, $\{1, \ldots, d\}$ and $\{d, d+1, \ldots, 2d-1\}$, their union is $\{1, \ldots, 2d-1\}$ with $d$ in both. So for $j - i \equiv r \pmod{2d}$ with $r \in \{1, \ldots, 2d-1\}$, the edge exists iff $r \in \{1, \ldots, d\}$ or $2d - r \in \{1, \ldots, d\}$, i.e., $r \in \{1, \ldots, d\}$ or $r \in \{d, \ldots, 2d-1\}$, which is all $r \in \{1, \ldots, 2d-1\}$. So the graph is complete!

That's because $d \geq n/2 = d$ in this case. So with $n = 2d$ and connecting to $d$ nearest in one direction, we get the complete graph. Not useful.

Let me try $n = 2d + 2$ or larger.

Actually, let me step back and think about this problem more carefully.

I want to find a $d$-regular (or min-degree $d$) graph on $n$ points on a circle that minimizes the maximum $I(e)$.

$I(e) = \deg(i) + \deg(j) - 2 + c(e)$ for chord $e = (i,j)$.

For a $d$-regular graph, $I(e) = 2d - 2 + c(e)$. So we want to minimize $\max_e c(e)$.

$c(e)$ is the number of chords crossing $e$ in the interior. We want a $d$-regular chord diagram that minimizes the maximum number of crossings per chord.

Now, the total number of crossings $C = \frac{1}{2} \sum_e c(e)$. If there are $m = nd/2$ chords, then $\max_e c(e) \geq 2C/m = 2C/(nd/2) = 4C/(nd)$.

So we need to lower bound $C$, the total number of crossings, for a $d$-regular graph on $n$ points on a circle.

There's a formula for the minimum number of crossings in a graph drawn on a circle. This is related to the "circular crossing number" or "convex crossing number."

For a graph $G$ on $n$ vertices with $m$ edges, drawn with vertices on a circle, the minimum number of crossings (over all circular orderings and all graphs with the given degree sequence) is related to the degree sequence.

Actually, there's a result that for a $d$-regular graph on $n$ vertices drawn on a circle, the minimum number of crossings is at least... let me think.

The number of crossings for a specific drawing is $\sum_{\text{crossing pairs}} 1$. For a chord $(i,j)$ with $a$ points on one side and $b$ on the other, $c(e) = e(A, B)$, the number of edges between the two sides.

The total number of crossings is $C = \frac{1}{2} \sum_e e(A_e, B_e)$ where $A_e, B_e$ are the two sides of chord $e$.

Alternatively, $C = \sum_{\text{unordered pairs of edges } \{e, f\}} [\text{$e$ and $f$ cross}]$.

For two edges $e = (i, j)$ and $f = (k, l)$ with $i < j$ and $k < l$, they cross iff $i < k < j < l$ or $k < i < l < j$ (assuming all distinct).

The total number of crossing pairs can be computed as follows. For each 4-element subset $\{a, b, c, d\}$ of vertices with $a < b < c < d$, the pairs of edges that cross are: $(a,c)$ with $(b,d)$ and $(a,d)$ with $(b,c)$. So each 4-subset contributes at most 2 crossings (if both pairs of edges exist).

The total number of 4-subsets is $\binom{n}{4}$. The maximum number of crossings is $2\binom{n}{4}$ (complete graph). For a $d$-regular graph, we need to count how many of these crossing pairs actually exist.

This is getting complex. Let me try a different approach and think about what the answer should be.

Let me consider the problem for small $d$ and try to find a pattern.

**Case $d = 2$:** We need every vertex to have degree $\geq 2$. The minimum $I(e) \geq 2 \cdot 2 - 2 = 2$. Can we achieve $I(e) = 2$ for all chords? We need $c(e) = 0$ for all $e$, i.e., a non-crossing 2-regular graph. A 2-regular non-crossing graph on a circle is a cycle that goes around the circle (the polygon). In this case, each edge (side of the polygon) intersects exactly 2 other edges (its two neighbors in the cycle). So $I(e) = 2$ for all $e$, and $M = 2 = 2d - 2$. ✓

**Case $d = 3$:** We need a non-crossing 3-regular graph (for $I(e) = 4$). But a 3-regular non-crossing graph on a circle is a maximal outerplanar graph, which has $2n - 3$ edges and average degree $< 4$. So a 3-regular outerplanar graph would need $3n/2 = 2n - 3$, giving $n = 6$. $K_4$ minus an edge? No. Let me think: a 3-regular outerplanar graph on 6 vertices. The octahedron graph is 4-regular. A triangular prism is 3-regular on 6 vertices but is it outerplanar? 

Actually, a maximal outerplanar graph on $n$ vertices has $2n - 3$ edges. For 3-regular, we need $3n/2$ edges, so $3n/2 = 2n - 3$ gives $n = 6$. A 3-regular outerplanar graph on 6 vertices: this would be a triangulation of a hexagon. The hexagon triangulated with 3 non-crossing diagonals gives $6 + 3 = 9 = 2 \cdot 6 - 3$ edges. But the degrees would be: each triangulation of a hexagon has some vertices of degree 2 and some of higher degree. Actually, in a maximal outerplanar graph on $n$ vertices, there are always at least 2 vertices of degree 2. So a 3-regular outerplanar graph doesn't exist (for $n \geq 4$).

So for $d = 3$, we can't have a non-crossing configuration. We need some crossings. So $M > 2d - 2 = 4$ for $d = 3$.

Hmm, but wait. We don't need the graph to be exactly $d$-regular. We need minimum degree $\geq d$. And we want to minimize the maximum $I(e)$. Maybe with higher degrees at some vertices, we can reduce crossings?

Actually, higher degrees at endpoints increase $I(e)$ directly (through $\deg(i) + \deg(j) - 2$), but might allow us to reduce crossings. It's a tradeoff.

Let me think about $d = 3$ more carefully. We need min degree 3. The smallest such graph on a circle: $K_4$ has 4 vertices, each of degree 3. With 4 points on a circle, $K_4$ has 6 edges. The two diagonals cross. Each side of the square intersects: 2 adjacent sides + 1 diagonal (the one not sharing an endpoint) = 3. Wait, let me count.

4 points on a circle: 1, 2, 3, 4. Edges: (1,2), (2,3), (3,4), (4,1), (1,3), (2,4). The diagonals (1,3) and (2,4) cross.

For edge (1,2): shares endpoint with (2,3), (4,1), (1,3). Crosses: (3,4)? No, (1,2) and (3,4) don't cross (they're on opposite sides). (2,4)? (1,2) and (2,4) share endpoint 2. So (1,2) intersects (2,3), (4,1), (1,3) by sharing endpoints, and does it cross anything? (1,2) and (3,4): 1 < 2 < 3 < 4, so no crossing. (1,2) and (2,4): share endpoint. (1,2) and (1,3): share endpoint. So $I((1,2)) = 3$.

For edge (1,3): shares endpoint with (1,2), (4,1), (3,4), (1,3) is itself... shares with (1,2), (3,4), (4,1). Crosses (2,4). So $I((1,3)) = 4$.

So the maximum is 4 = $2 \cdot 3 - 2$. So $M = 4$ for $d = 3$? But we said a non-crossing 3-regular graph doesn't exist. The point is that $K_4$ has crossings, but the maximum $I(e)$ is still $2d - 2 = 4$.

Wait, the diagonal (1,3) has $I = 4 = 2 \cdot 3 - 2 + 1$ (one crossing). But the sides have $I = 3 < 4$. So the maximum is 4, which equals $2d - 2$.

Hmm, so even though there are crossings, the maximum $I(e)$ is still $2d - 2$? That's because the sides have fewer intersections (only 3, which is less than $2d - 2 = 4$), and the diagonals have exactly $2d - 2 = 4$.

But the problem asks for the maximum $M$ such that in ANY configuration, some chord has $\geq M$ intersections. So $M$ is the minimum over configurations of the maximum $I(e)$. For $d = 3$, the $K_4$ configuration has max $I(e) = 4$. Can we do better (get max $I(e) < 4$)? We need $I(e) \geq 2d - 2 = 4$ for all $e$ (since $\deg \geq 3$ for all vertices). So no, $M = 4$ for $d = 3$.

Wait, $I(e) = \deg(i) + \deg(j) - 2 + c(e) \geq 2d - 2 + c(e) \geq 2d - 2$. So $M \geq 2d - 2$ always. And the question is whether we can achieve max $I(e) = 2d - 2$, which requires $c(e) = 0$ for the chord with maximum $I(e)$, and $\deg = d$ for all vertices.

But we don't need $c(e) = 0$ for ALL chords; we need the MAXIMUM $I(e)$ to be $2d - 2$. This requires that for the chord with the highest $I(e)$, we have $\deg(i) + \deg(j) - 2 + c(e) = 2d - 2$, which means $\deg(i) = \deg(j) = d$ and $c(e) = 0$. But other chords can have higher $I(e)$... no, we want the maximum to be $2d - 2$, so ALL chords must have $I(e) \leq 2d - 2$. Since $I(e) \geq 2d - 2$ for all $e$, this means $I(e) = 2d - 2$ for all $e$, which requires $\deg(v) = d$ for all $v$ and $c(e) = 0$ for all $e$.

So $M = 2d - 2$ iff there exists a non-crossing $d$-regular graph on a circle. This exists iff $d \leq 3$ (for $d = 2$, the polygon; for $d = 3$, we need to check more carefully).

Wait, for $d = 3$, does a non-crossing 3-regular graph on a circle exist? As I argued, a maximal outerplanar graph has at least 2 vertices of degree 2, so a 3-regular outerplanar graph doesn't exist. But $K_4$ on 4 points has crossings (the two diagonals cross). So for $d = 3$, $M > 4$?

But I computed that $K_4$ has max $I(e) = 4 = 2d - 2$. The sides have $I = 3$ and the diagonals have $I = 4$. So the max is 4. But $I(e) \geq 2d - 2 = 4$ for all $e$... wait, the sides have $I = 3 < 4$! How?

Oh, I think I miscounted. Let me recount for $K_4$ on 4 points.

Points: 1, 2, 3, 4 in order on the circle. Edges: (1,2), (2,3), (3,4), (4,1), (1,3), (2,4).

Edge (1,2): $\deg(1) = 3, \deg(2) = 3$. $I = 3 + 3 - 2 + c = 4 + c$. $c$ = number of edges crossing (1,2) in interior. (1,2) has points 0 on one side (between 1 and 2) and points 3, 4 on the other side. An edge crosses (1,2) iff it has one endpoint in $\{3, 4\}$... wait, (1,2) is a side of the square, so there are no points between 1 and 2 (they're adjacent). The arc from 1 to 2 (clockwise) has 0 interior points, and the arc from 2 to 1 (clockwise, i.e., through 3, 4) has 2 interior points. So $a = 0, b = 2$. $c(e) = e(A, B) = e(\emptyset, \{3, 4\}) = 0$. So $I = 4 + 0 = 4$.

I made an error before. Let me recount. $I((1,2)) = \deg(1) + \deg(2) - 2 + c = 3 + 3 - 2 + 0 = 4$. The chords intersecting (1,2) are: (2,3) [shares 2], (4,1) [shares 1], (1,3) [shares 1], (2,4) [shares 2]. That's 4 chords. And (3,4) doesn't intersect (1,2) (no shared endpoint, no crossing). So $I = 4$. ✓

Edge (1,3): $\deg(1) = 3, \deg(3) = 3$. $I = 4 + c$. Arc from 1 to 3 has point 2, arc from 3 to 1 has point 4. $a = 1, b = 1$. $c = e(\{2\}, \{4\}) = 1$ (edge (2,4) exists). So $I = 4 + 1 = 5$.

So the max is 5, not 4! I made an error earlier. Let me recount the intersections of (1,3): shares endpoint with (1,2), (4,1), (3,4), (2,3). That's 4. Plus crosses (2,4). Total 5. ✓

So for $K_4$ with $d = 3$, max $I(e) = 5$. Can we do better with a different configuration?

We need min degree 3. With 4 points, the only option is $K_4$. With more points, we might do better.

Let me try 6 points with a 3-regular graph. Consider the graph: (1,2), (2,3), (3,4), (4,5), (5,6), (6,1) (the hexagon) plus (1,3), (3,5), (5,1) (a triangle on odd vertices) plus... wait, that gives degrees: 1: 3 (edges to 2, 6, 3), 2: 2 (edges to 1, 3), 3: 4 (edges to 2, 4, 1, 5), 4: 2, 5: 4, 6: 2. Not 3-regular.

Let me try the complete bipartite graph $K_{3,3}$ on 6 points. Points 1,2,3 on one side, 4,5,6 on the other. But on a circle, the arrangement matters. Let me place them as 1,4,2,5,3,6 around the circle. Then edges are all pairs between {1,2,3} and {4,5,6}.

This is getting complicated. Let me try to think about the general problem differently.

Actually, let me reconsider. The problem is from a competition (likely ISL or similar), and the answer for $d = 20$ should be a specific number. Let me think about what structural result gives the answer.

Let me reconsider the lower bound. We have $I(e) \geq 2d - 2 + c(e)$. The question is: what is the minimum possible value of $\max_e c(e)$ over all valid configurations?

Actually, more precisely, we want to minimize $\max_e I(e) = \max_e (\deg(i_e) + \deg(j_e) - 2 + c(e))$. Since $\deg \geq d$, this is $\geq \max_e (2d - 2 + c(e)) = 2d - 2 + \max_e c(e)$. So $M \geq 2d - 2 + \min_{\text{config}} \max_e c(e)$.

And we want to find $\min_{\text{config}} \max_e c(e)$, the minimum possible maximum number of crossings per chord.

But wait, we also want to minimize $\deg(i) + \deg(j)$, so we'd want all degrees to be exactly $d$. So the optimal configuration is likely $d$-regular.

So the question reduces to: what is the minimum possible maximum number of crossings per chord, over all $d$-regular graphs on $n$ points on a circle (for any $n$)?

And then $M = 2d - 2 + $ that minimum.

For $d = 3$: we need to find the minimum max crossings per chord in a 3-regular circular graph. In $K_4$, the max crossings per chord is 1 (the diagonals each cross 1 other chord). Can we do better? We need a 3-regular graph with max crossings 0, i.e., non-crossing. But we showed that's impossible. So the minimum max crossings is at least 1. And $K_4$ achieves 1. So $M = 2 \cdot 3 - 2 + 1 = 5$ for $d = 3$.

Hmm, but is there a 3-regular graph on more points with max crossings 0? No, because non-crossing 3-regular outerplanar graphs don't exist. Is there one with max crossings 0? No. So $M = 5$ for $d = 3$.

Wait, but maybe with more points, we can have a 3-regular graph where the max crossings per chord is still 1 but the graph is different? Or maybe with more points, we can reduce the max crossings? No, the max crossings is at least 1 (since non-crossing is impossible), and $K_4$ achieves 1. So $M = 5$ for $d = 3$.

Hmm, but actually, I should check: is there a 3-regular graph on a circle where some chord has 0 crossings but the max is still 1? That doesn't help; we need the max to be 0 for $M = 4$, which is impossible.

OK so for $d = 3$, $M = 5$.

Let me check $d = 2$: $M = 2 \cdot 2 - 2 + 0 = 2$. ✓ (non-crossing 2-regular = polygon, exists).

For $d = 4$: We need a 4-regular graph on a circle. Non-crossing 4-regular outerplanar: impossible (max degree in outerplanar can be high, but average degree $< 4$, so 4-regular is impossible). So we need crossings. What's the minimum max crossings per chord?

With $n = 5$ (complete graph $K_5$, which is 4-regular): Let me compute the max crossings. Points 1,2,3,4,5. Edge (1,3): $a = 1$ (point 2), $b = 2$ (points 4,5). $c = e(\{2\}, \{4,5\}) = 2$ (edges (2,4) and (2,5)). $I = 2 \cdot 4 - 2 + 2 = 8$. Edge (1,4): $a = 2$ (points 2,3), $b = 1$ (point 5). $c = e(\{2,3\}, \{5\}) = 2$. $I = 6 + 2 = 8$. Edge (1,2): $a = 0, b = 3$. $c = 0$. $I = 6$. So max $I = 8$.

Can we do better with more points? Let me try $n = 6$, 4-regular. The complement of a 4-regular graph on 6 vertices is 1-regular (a perfect matching). So a 4-regular graph on 6 vertices is $K_6$ minus a perfect matching.

Let me try: remove edges (1,4), (2,5), (3,6) from $K_6$. The remaining graph is 4-regular. Points 1,2,3,4,5,6 on circle.

Edge (1,2): $a = 0, b = 4$. $c = 0$. $I = 6$. 
Edge (1,3): $a = 1$ (point 2), $b = 3$ (points 4,5,6). $c = e(\{2\}, \{4,5,6\})$. Edges from 2 to {4,5,6}: (2,4), (2,6) (not (2,5) since it's removed). So $c = 2$. $I = 6 + 2 = 8$.
Edge (1,5): $a = 3$ (points 2,3,4), $b = 1$ (point 6). $c = e(\{2,3,4\}, \{6\})$. Edges from 6 to {2,3,4}: (6,2), (6,4) (not (6,3) since removed). $c = 2$. $I = 8$.
Edge (1,6): $a = 4$ (points 2,3,4,5), $b = 0$. $c = 0$. $I = 6$.

So max $I = 8$ for this graph too. Same as $K_5$.

Can we do better? Let me try $n = 8$, 4-regular. Hmm, this is getting complicated. Let me try to think about the general pattern.

For $d = 2$: $M = 2 = 2(2) - 2$.
For $d = 3$: $M = 5 = 2(3) - 2 + 1$.
For $d = 4$: $M = 8 = 2(4) - 2 + 2$? Or is it something else?

If the pattern is $M = 2d - 2 + (d - 2) = 3d - 4$, then for $d = 2$: $2$, $d = 3$: $5$, $d = 4$: $8$, $d = 20$: $56$.

Or if $M = 2d - 2 + \lfloor (d-1)/2 \rfloor$ or something...

Actually, let me think about this more carefully. The minimum max crossings per chord in a $d$-regular circular graph.

Let me think about what determines the crossings. For a $d$-regular graph on $n$ points, the total number of edges is $m = nd/2$. The total number of crossings $C$ depends on the graph structure.

For a chord $(i,j)$ with $a$ points on one side and $b = n - 2 - a$ on the other, $c(e) = e(A, B)$. In a $d$-regular graph, $\sum_{v \in A} \deg(v) = da$, so $e(A, B) = da - 2e(A) - e(A, \{i\}) - e(A, \{j\})$.

To minimize $c(e) = e(A, B)$, we want to maximize $2e(A) + e(A, \{i\}) + e(A, \{j\})$, i.e., we want as many edges as possible to stay within $A$ or connect to $i, j$.

The maximum of $e(A)$ is $\binom{a}{2}$ (but limited by the degree constraint). The maximum of $e(A, \{i\})$ is $\min(d - 1, a)$ and $e(A, \{j\})$ is $\min(d - 1, a)$.

So $c(e) \geq da - 2\binom{a}{2} - 2\min(d-1, a) = da - a(a-1) - 2\min(d-1, a)$.

If $a \leq d - 1$: $c(e) \geq da - a(a-1) - 2a = a(d - a + 1 - 2) = a(d - a - 1)$.

If $a \geq d$: $c(e) \geq da - a(a-1) - 2(d-1) = a(d - a + 1) - 2(d-1) = a(d - a + 1) - 2d + 2$.

Hmm, this is getting complicated. Let me think about it differently.

For the chord that most evenly splits the circle, $a \approx b \approx n/2$. For this chord, $c(e) = e(A, B)$. In a $d$-regular graph, $e(A, B) = da - 2e(A) - e(A, \{i\}) - e(A, \{j\})$. With $a \approx n/2$, $e(A) \leq \binom{n/2}{2}$ and $e(A, \{i\}) + e(A, \{j\}) \leq 2(d-1)$. So $c(e) \geq dn/2 - 2 \cdot \binom{n/2}{2} - 2(d-1) = dn/2 - n(n-2)/4 - 2d + 2$.

For this to be non-negative (i.e., for crossings to be unavoidable), we need $dn/2 > n(n-2)/4 + 2d - 2$, roughly $d > n/2 - 2 + 4/n$, i.e., $n < 2d + 4$. So for $n \leq 2d + 3$ or so, crossings are unavoidable for the bisecting chord.

To minimize crossings, we want $n$ to be large (so that the graph is "sparse" relative to the complete graph, and we can avoid crossings). But as $n$ grows, the bisecting chord has $a \approx n/2$ points on each side, and $c(e) = e(A, B) \geq da - a(a-1) - 2(d-1)$ (for $a \geq d$). With $a = n/2$:

$c(e) \geq d \cdot n/2 - (n/2)(n/2 - 1) - 2(d-1) = dn/2 - n^2/4 + n/2 - 2d + 2$.

$= -n^2/4 + n(d+1)/2 - 2d + 2$.

This is a quadratic in $n$ that's negative for large $n$, meaning the bound becomes trivial (negative). The bound is positive when $n^2/4 < n(d+1)/2 - 2d + 2$, i.e., $n^2 - 2n(d+1) + 8d - 8 < 0$, i.e., $n < (d+1) + \sqrt{(d+1)^2 - 8d + 8} = (d+1) + \sqrt{d^2 - 6d + 9} = (d+1) + |d-3|$.

For $d \geq 3$: $n < (d+1) + (d-3) = 2d - 2$. So for $n \leq 2d - 3$, the bisecting chord must have crossings.

For $n \geq 2d - 2$, the bound becomes negative, meaning we might be able to avoid crossings for the bisecting chord. But we need to check all chords, not just the bisecting one.

Hmm, this analysis is for the bisecting chord. For shorter chords (with small $a$), the bound $c(e) \geq a(d - a - 1)$ (for $a \leq d - 1$) applies. This is non-negative for $a \leq d - 1$, and is 0 for $a = 0$ or $a = d - 1$. So short chords (with $a \leq d - 1$) might have 0 crossings if $a = 0$ or $a = d - 1$.

Wait, $c(e) \geq a(d - a - 1)$ for $a \leq d - 1$. This is 0 when $a = 0$ or $a = d - 1$. For $1 \leq a \leq d - 2$, it's positive. So chords with $a = 1, 2, \ldots, d-2$ must have crossings.

But $a$ is the number of points on one side. If $n$ is large, most chords will have large $a$ and $b$, and the bound for large $a$ might be negative (trivial). The binding constraint comes from chords with $a$ close to $d - 1$.

Actually, let me reconsider. For a chord with $a$ points on the short side ($a \leq (n-2)/2$), the bound is:

If $a \leq d - 1$: $c(e) \geq a(d - a - 1)$.
If $a \geq d$: $c(e) \geq a(d - a + 1) - 2(d - 1) = a(d - a + 1) - 2d + 2$.

For $a \leq d - 1$, the maximum of $a(d - a - 1)$ over $a \in \{1, \ldots, d-2\}$ is at $a = (d-1)/2$, giving roughly $(d-1)^2/4$.

So some chord must have $c(e) \geq \max_{a} a(d - a - 1)$. But which chord? We need to show that in any $d$-regular circular graph, there exists a chord with $a$ in the range where the bound is large.

Hmm, but we get to choose the graph. The question is: what is the minimum over all $d$-regular circular graphs of the maximum $c(e)$?

Let me think about this differently. Consider a $d$-regular graph on $n$ points on a circle. For each chord $e$, let $s(e)$ be the number of points on the shorter side (so $s(e) \leq (n-2)/2$).

If $s(e) \leq d - 2$, then $c(e) \geq s(e)(d - s(e) - 1) \geq 1 \cdot (d - 2) = d - 2$ (for $s(e) = 1$). Actually, $s(e)(d - s(e) - 1)$ for $s(e) = 1$ is $d - 2$, for $s(e) = 2$ is $2(d-3)$, etc. The minimum over $s(e) \in \{1, \ldots, d-2\}$ is $d - 2$ (at $s(e) = 1$) or $d - 2$ (at $s(e) = d - 2$). Actually, $a(d - a - 1)$ at $a = 1$ is $d - 2$, at $a = d - 2$ is $(d-2) \cdot 1 = d - 2$. So the minimum is $d - 2$.

So if there exists a chord with $s(e) \leq d - 2$ (and $s(e) \geq 1$), then $c(e) \geq d - 2$.

But can we avoid having any chord with $1 \leq s(e) \leq d - 2$? That would mean every chord has $s(e) = 0$ (adjacent points) or $s(e) \geq d - 1$.

If every chord connects either adjacent points or points that are at least $d$ apart (in terms of the shorter arc), then... Let me think about what this means.

A chord connecting points at circular distance $r$ (shorter arc has $r - 1$ interior points) has $s(e) = r - 1$. So $s(e) = 0$ means $r = 1$ (adjacent), $s(e) \geq d - 1$ means $r \geq d$.

So we'd need a $d$-regular graph where every edge connects either adjacent points or points at distance $\geq d$. 

The "adjacent" edges form a subgraph of the cycle, which is a collection of paths (or the full cycle). Each vertex can have at most 2 adjacent edges. So at most 2 of the $d$ edges at each vertex are "short" (adjacent), and the remaining $d - 2$ (or $d$) must be "long" (distance $\geq d$).

For the long edges (distance $\geq d$), $s(e) \geq d - 1$. For these, if $s(e) = d - 1$, then $c(e) \geq (d-1)(d - (d-1) - 1) = (d-1) \cdot 0 = 0$. So the bound is 0! And for $s(e) \geq d$, we're in the other case.

So if we can construct a $d$-regular graph where every edge has $s(e) = 0$ or $s(e) = d - 1$, then the bound gives $c(e) \geq 0$ for all edges, which is trivially true. We'd need to check if $c(e) = 0$ is achievable.

But can we have a $d$-regular graph with all edges at distance 1 or $d$? Each vertex has at most 2 edges at distance 1 (to its two neighbors) and needs $d - 2$ more edges at distance $d$. But a vertex can have at most 2 edges at distance $d$ (one in each direction). So the maximum degree from distance-1 and distance-$d$ edges is $2 + 2 = 4$. For $d > 4$, this isn't enough.

So for $d > 4$, we can't avoid having edges at distances $2, 3, \ldots, d-1$, which means some edges have $1 \leq s(e) \leq d - 2$, and those have $c(e) \geq d - 2$.

Wait, but we could also use edges at distance $> d$, which have $s(e) > d - 1$. For those, the bound might be different.

Let me reconsider. For an edge at distance $r$ (so $s(e) = r - 1$), with $r - 1 \geq d$ (i.e., $r \geq d + 1$), we're in the case $a \geq d$:

$c(e) \geq a(d - a + 1) - 2d + 2 = (r-1)(d - r + 2) - 2d + 2$.

For $r = d + 1$: $(d)(d - d - 1 + 2) - 2d + 2 = d \cdot 1 - 2d + 2 = 2 - d$. For $d \geq 3$, this is negative, so the bound is trivial.

For $r = d + 2$: $(d+1)(d - d - 2 + 2) - 2d + 2 = (d+1) \cdot 0 - 2d + 2 = 2 - d$. Also negative for $d \geq 3$.

So for edges with $s(e) \geq d$, the bound is trivial (negative). The binding constraints come from edges with $1 \leq s(e) \leq d - 2$.

Now, the question is: in a $d$-regular circular graph, must there exist an edge with $1 \leq s(e) \leq d - 2$?

If $d \leq 4$: We can have all edges at distance 1 or $d$ (as discussed, max degree 4 from these). For $d = 4$, we can have 2 edges at distance 1 and 2 at distance 4, giving degree 4. So no edge with $1 \leq s(e) \leq 2$, and the bound is trivial. We might achieve $c(e) = 0$ for all edges? Let me check.

For $d = 4$, $n = ?$. We need a 4-regular graph with edges at distances 1 and 4. With $n$ points, distance 4 means connecting $i$ to $i + 4$. For this to not coincide with distance 1, we need $n > 5$. Let's try $n = 8$: connect each $i$ to $i \pm 1$ and $i \pm 4 \pmod{8}$. This gives degree 4. The edges at distance 4 are $(i, i+4)$ for $i = 0, 1, 2, 3$ (4 edges, each counted once). The edges at distance 1 are $(i, i+1)$ for $i = 0, \ldots, 7$ (8 edges). Total 12 edges, $8 \cdot 4 / 2 = 16$... wait, that's 12 edges but $8 \cdot 4 / 2 = 16$. Let me recount.

Each vertex $i$ is connected to $i-1, i+1, i-4, i+4 \pmod{8}$. That's 4 neighbors. But $i + 4 \pmod{8}$ and $i - 4 \pmod{8}$ are the same vertex (since $8/2 = 4$). So each vertex has only 3 distinct neighbors: $i-1, i+1, i+4$. That's degree 3, not 4.

So for $n = 8$, distance 4 is the antipodal distance, and each vertex has only 1 antipodal neighbor. So degree from distances 1 and 4 is $2 + 1 = 3$.

For $n = 9$: distance 4 gives $i + 4$ and $i - 4 = i + 5 \pmod{9}$, which are distinct. So degree from distances 1 and 4 is $2 + 2 = 4$. 

$n = 9$, 4-regular, edges at distances 1 and 4. Let me check if this is non-crossing.

An edge at distance 1: $(i, i+1)$. This is a side of the nonagon. No crossings with other sides. Does it cross any distance-4 edge? A distance-4 edge $(j, j+4)$ crosses $(i, i+1)$ iff one of $j, j+4$ is in the arc from $i$ to $i+1$ (which has no interior points) and the other is outside. Since the arc has no interior points, no crossing. So distance-1 edges don't cross anything.

An edge at distance 4: $(i, i+4)$. This has 3 interior points on the short side. It crosses another distance-4 edge $(j, j+4)$ iff the endpoints alternate. 

Let me check: $(0, 4)$ and $(1, 5)$. Order: 0, 1, 4, 5. We need $0 < 1 < 4 < 5$, so $(0,4)$ and $(1,5)$: is $1$ between 0 and 4? Yes. Is 5 between 0 and 4? No. So they cross. 

So the distance-4 edges do cross each other. So this graph is not non-crossing.

Hmm. So even for $d = 4$, we can't avoid crossings. Let me compute the max $c(e)$ for this graph.

$(0, 4)$: short side has points 1, 2, 3. Long side has points 5, 6, 7, 8. $c = e(\{1,2,3\}, \{5,6,7,8\})$. Edges from {1,2,3} to {5,6,7,8}: distance-1 edges: (8, 0) no... let me list all edges.

Distance-1 edges: (0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8), (8,0).
Distance-4 edges: (0,4), (1,5), (2,6), (3,7), (4,8), (5,0), (6,1), (7,2), (8,3). But (0,4) and (4,0) are the same, (1,5) and (5,1) are the same, etc. So distance-4 edges are: (0,4), (1,5), (2,6), (3,7), (4,8), (5,0)=(0,5)... wait, $5 + 4 = 9 \equiv 0$, so (5, 0) is a distance-4 edge, same as (0, 5). But (0, 4) is also distance 4. So vertex 0 has distance-4 edges to 4 and 5. But $|0 - 4| = 4$ and $|0 - 5| = 5$, and the circular distance is $\min(4, 9 - 4) = 4$ and $\min(5, 9 - 5) = 4$. So both are distance 4. OK.

So distance-4 edges: (0,4), (0,5), (1,5), (1,6), (2,6), (2,7), (3,7), (3,8), (4,8). That's 9 edges. Plus 9 distance-1 edges = 18 edges. $9 \cdot 4 / 2 = 18$. ✓

Now, $c((0,4))$: short side $\{1, 2, 3\}$, long side $\{5, 6, 7, 8\}$.
Edges from {1,2,3} to {5,6,7,8}:
- (1,5): yes (distance 4)
- (1,6): yes (distance 4, since $|1-6| = 5$, circular distance $\min(5, 4) = 4$)
- (2,6): yes
- (2,7): yes
- (3,7): yes
- (3,8): yes
- Any distance-1 edges? (1,2) is within {1,2,3}. (3,4) goes to 4, not in {5,6,7,8}. (8,0) goes to 0. No distance-1 edges cross.
So $c((0,4)) = 6$.

$I((0,4)) = 2 \cdot 4 - 2 + 6 = 12$.

That's quite high. Let me check a distance-1 edge: $(0,1)$. Short side has 0 points, long side has 7. $c = 0$. $I = 6$.

So max $I = 12$ for this graph. Compare with $K_5$ which gave max $I = 8$. So $K_5$ is better for $d = 4$.

Hmm, so larger $n$ doesn't always help. Let me reconsider.

For $d = 4$, $K_5$ gives max $I = 8$. Can we do better?

Let me try $n = 6$, 4-regular ($K_6$ minus a perfect matching). I computed max $I = 8$ earlier. Same as $K_5$.

Can we achieve max $I = 7$? That would require max $c(e) = 1$ (since $I = 6 + c$). Is there a 4-regular circular graph with max crossings per chord = 1?

In $K_5$, the max crossings per chord is 2 (for chords at distance 2, like (1,3)). In $K_6$ minus matching, also 2.

Can we find a 4-regular graph with max crossings 1? That seems hard. Let me think about whether it's possible.

A 4-regular graph on $n$ points with max 1 crossing per chord. The total crossings $C \leq m/1 = m$ (since each chord crosses at most 1 other, and each crossing involves 2 chords, $C \leq m/2$). Actually, $C = \frac{1}{2} \sum c(e) \leq \frac{1}{2} \cdot m \cdot 1 = m/2$.

For a 4-regular graph, $m = 2n$. So $C \leq n$. 

The minimum number of crossings for a 4-regular graph on $n$ points on a circle... I don't know this off the top of my head.

Let me try a different approach. Let me think about what the answer should be for general $d$ and then specialize to $d = 20$.

Let me consider the problem from the perspective of the "friendship" or "intersection" structure.

Actually, let me reconsider the problem statement. It says "each end of each chord is an end of at least $d$ different drawn chords." So every endpoint of every chord has degree $\geq d$. And "chords with a common end intersect" — so sharing an endpoint counts as intersecting.

We want the maximum $M$ such that in any such configuration, some chord intersects at least $M$ others.

I've established that $I(e) \geq 2d - 2 + c(e)$ where $c(e)$ is the number of interior crossings. And $M = 2d - 2 + \min_{\text{config}} \max_e c(e)$.

Now I need to find $\min_{\text{config}} \max_e c(e)$.

Let me think about this more carefully. Consider a $d$-regular graph on $n$ points on a circle. For a chord $e = (i, j)$, let $a$ be the number of points on the shorter arc. We showed:

For $a \leq d - 1$: $c(e) \geq a(d - a - 1)$.
For $a \geq d$: $c(e) \geq a(d - a + 1) - 2(d - 1) = a(d - a + 1) - 2d + 2$.

The first bound is maximized at $a = (d-1)/2$, giving $\approx (d-1)^2/4$.
The second bound is maximized at $a = (d+1)/2$, giving $\approx (d+1)^2/4 - 2d + 2 = (d^2 + 2d + 1)/4 - 2d + 2 = (d^2 - 6d + 9)/4 = (d-3)^2/4$.

So the first bound is stronger (for $d \geq 4$). The maximum of $a(d - a - 1)$ for $a \in \{1, \ldots, d-2\}$ is:

If $d$ is odd, $d = 2k + 1$: max at $a = k$, giving $k \cdot k = k^2 = ((d-1)/2)^2$.
If $d$ is even, $d = 2k$: max at $a = k - 1$ or $a = k$, giving $(k-1) \cdot k = k(k-1) = (d/2)(d/2 - 1) = d(d-2)/4$.

But this is the maximum over $a$ of the lower bound for a specific chord. We need to show that in any $d$-regular circular graph, there EXISTS a chord with large $c(e)$.

The key question is: can we choose the graph so that all chords have small $a$ (say $a = 0$ or $a = d - 1$), avoiding the range where the bound is large?

As I discussed, for $d \leq 4$, we can potentially have all edges at distances 1 and $d$ (giving $a = 0$ or $a = d - 1$), but even then, crossings might occur between the distance-$d$ edges.

For $d \geq 5$, we can't have all edges at distances 1 and $d$ (max degree 4 from these), so we must have edges at other distances, including distances 2 through $d - 1$ (giving $a = 1$ through $d - 2$).

But wait, we could also use edges at distance $> d$ (giving $a \geq d$). For those, the bound is weaker. So the question is: can we construct a $d$-regular graph using only edges at distances 1, $d - 1$, $d$, $d + 1$, etc., avoiding distances 2 through $d - 2$?

The available distances are 1, $d - 1$, $d$, $d + 1$, ..., up to $\lfloor n/2 \rfloor$. Each distance $r$ (with $r < n/2$) contributes 2 edges per vertex (to $i + r$ and $i - r$). Distance $n/2$ (if $n$ is even) contributes 1 edge per vertex.

So from distance 1: 2 edges per vertex.
From distance $d - 1$: 2 edges per vertex.
From distance $d$: 2 edges per vertex.
From distance $d + 1$: 2 edges per vertex.
Etc.

To get degree $d$, we need $d$ edges per vertex. Using distance 1 (2 edges) + distance $d - 1$ (2 edges) = 4 edges. We need $d - 4$ more. Using distances $d, d + 1, \ldots$: each gives 2 edges. So we need $\lceil (d - 4)/2 \rceil$ more distances.

For $d = 20$: 2 (dist 1) + 2 (dist 19) + 2 (dist 20) + 2 (dist 21) + ... We need 20 edges, so 10 distances. Using distances 1, 19, 20, 21, 22, 23, 24, 25, 26, 27: that's 10 distances × 2 = 20 edges. But we need $n$ large enough that these distances are all valid (i.e., $27 \leq \lfloor n/2 \rfloor$, so $n \geq 55$).

But wait, we also need to avoid distances 2 through 18 (which give $a = 1$ through 17, where the bound $a(d - a - 1)$ is large). If we only use distances 1 and $\geq 19$, we avoid these.

But the bound for $a \geq d = 20$ (i.e., distance $\geq 21$) is $c(e) \geq a(d - a + 1) - 2d + 2$. For $a = 20$ (distance 21): $20(20 - 20 + 1) - 40 + 2 = 20 - 38 = -18$. Trivial. For $a = 19$ (distance 20): this is $a = d - 1$, so $c(e) \geq 19(20 - 19 - 1) = 0$. Trivial.

So the bounds are all trivial for distances 1, 19, 20, 21, ..., 27. But that doesn't mean $c(e) = 0$; it just means our lower bound is 0. We need to check if the graph is actually non-crossing or has few crossings.

But a graph with edges at distances 1, 19, 20, ..., 27 on $n = 55$ points will have many crossings between the long edges. For example, edges at distance 20 will cross edges at distance 20, 21, etc.

So the lower bound approach isn't giving us the answer directly. We need a better approach.

Let me think about this problem from a completely different angle.

**Reformulation as a graph theory problem.**

We have a graph $G$ on $n$ vertices arranged on a circle, with minimum degree $d$. Two edges are "intersecting" if they share a vertex or cross inside the circle. We want to find the minimum possible maximum degree of the intersection graph of edges.

Let me think about the intersection graph $H$. The vertices of $H$ are the edges of $G$, and two vertices are adjacent iff the corresponding edges intersect. We want to minimize $\Delta(H)$ (maximum degree of $H$).

$\deg_H(e) = I(e) = \deg_G(u) + \deg_G(v) - 2 + c(e)$ for edge $e = uv$.

Now, let me think about a specific construction that might be optimal.

**Construction: $d$-regular graph on $n = 2d$ points, connecting each point to the $d$ points on the opposite side.**

Wait, I already considered this and it gives the complete graph.

**Construction: $d$-regular graph on $n = 2d + 1$ points, connecting each point to the $d$ nearest points on each side... no, that gives degree $2d$.**

Let me think about the "circulant" graph. A circulant graph $C_n(S)$ connects $i$ to $i + s \pmod{n}$ for each $s \in S$. If $S = \{1, 2, \ldots, k\}$, the degree is $2k$ (for $k < n/2$). For $d = 2k$, this gives a $d$-regular graph.

For $d = 20$, $k = 10$, $S = \{1, 2, \ldots, 10\}$, $n$ large. This connects each point to its 10 nearest neighbors on each side.

For this graph, a chord at distance $r$ (for $r \in \{1, \ldots, 10\}$) has $a = r - 1$ points on the short side. $c(e) = e(A, B)$ where $A$ is the short side.

For a chord $(0, r)$ with $r \leq 10$: $A = \{1, \ldots, r-1\}$, $B = \{r+1, \ldots, n-1\}$. $c(e) = $ number of edges from $A$ to $B$.

An edge from $j \in A$ to $l \in B$ exists iff $|j - l| \pmod{n} \in \{1, \ldots, 10\}$, i.e., $l - j \pmod{n} \in \{1, \ldots, 10\}$ or $j - l \pmod{n} \in \{1, \ldots, 10\}$.

For $j \in \{1, \ldots, r-1\}$ and $l \in \{r+1, \ldots, n-1\}$: $l - j$ ranges from $(r+1) - (r-1) = 2$ to $(n-1) - 1 = n - 2$. The edge exists iff $l - j \leq 10$ or $n - (l - j) \leq 10$, i.e., $l - j \leq 10$ or $l - j \geq n - 10$.

For $n$ large (say $n = 100$), the second condition $l - j \geq 90$ is rarely satisfied. So roughly, $c(e) \approx \sum_{j=1}^{r-1} |\{l \in B : l - j \leq 10\}|$.

For $j$ and $l - j \leq 10$: $l \leq j + 10$. Since $l \geq r + 1$ and $j \leq r - 1$: $l$ ranges from $r + 1$ to $j + 10 \leq r + 9$. So $l \in \{r+1, \ldots, r + 9\}$ (at most 9 values, but also $l \leq n - 1$).

Wait, this is getting complicated. Let me just compute for a specific case.

For $d = 20$, $k = 10$, $n = 100$ (say). Chord $(0, 10)$: $a = 9$, $b = 89$. $A = \{1, \ldots, 9\}$, $B = \{11, \ldots, 99\}$.

$c(e) = \sum_{j=1}^{9} |\{l \in B : |j - l| \pmod{100} \leq 10\}|$.

For $j \in \{1, \ldots, 9\}$, $l \in B = \{11, \ldots, 99\}$: $l - j \in \{11 - 9, \ldots, 99 - 1\} = \{2, \ldots, 98\}$. $|j - l| \pmod{100} \leq 10$ iff $l - j \leq 10$ or $l - j \geq 90$.

$l - j \leq 10$: $l \leq j + 10$. Since $l \geq 11$ and $j \leq 9$: $l \in \{11, \ldots, j + 10\}$. For $j = 1$: $l \in \{11\}$, 1 value. For $j = 2$: $l \in \{11, 12\}$, 2 values. ... For $j = 9$: $l \in \{11, \ldots, 19\}$, 9 values.

$l - j \geq 90$: $l \geq j + 90$. Since $j \leq 9$: $l \geq 91$. $l \in \{91, \ldots, 99\}$, 9 values for each $j$ (since $l - j \leq 98 < 100$, and $l - j \geq 90$ gives $l \geq j + 90$, and $l \leq 99$). For $j = 1$: $l \in \{91, \ldots, 99\}$, 9 values. For $j = 9$: $l \in \{99\}$, 1 value.

So $c(e) = \sum_{j=1}^{9} (j + (10 - j)) = \sum_{j=1}^{9} 10 = 90$.

$I(e) = 2 \cdot 20 - 2 + 90 = 128$.

That's a lot. The circulant graph with $n = 100$ is not good.

Let me try a different construction. What about using a small $n$?

For $d = 20$, the smallest $n$ for a 20-regular graph is $n = 21$ (complete graph $K_{21}$). Let me compute the max $I(e)$ for $K_{21}$.

In $K_{21}$, every vertex has degree 20. For a chord $(i, j)$ with $a$ points on one side and $b = 19 - a$ on the other, $c(e) = a \cdot b$ (all pairs across). $I(e) = 38 + ab$.

The maximum of $ab$ for $a + b = 19$ is at $a = 9, b = 10$ (or vice versa): $ab = 90$. So max $I = 38 + 90 = 128$.

For $n = 22$, 20-regular graph: this is $K_{22}$ minus a 1-factor (perfect matching). $m = 22 \cdot 20 / 2 = 220$ edges. For a chord $(i,j)$ with $a$ points on one side, $b = 20 - a$ on the other: $c(e) = e(A, B)$. In $K_{22}$ minus a matching, $e(A, B) = ab - m_{AB}$ where $m_{AB}$ is the number of matching edges between $A$ and $B$. Each matching edge connects two vertices; the number of matching edges with one endpoint in $A$ and one in $B$ is at most $\min(a, b)$.

So $c(e) \geq ab - \min(a, b)$. For $a = 10, b = 10$: $c \geq 100 - 10 = 
