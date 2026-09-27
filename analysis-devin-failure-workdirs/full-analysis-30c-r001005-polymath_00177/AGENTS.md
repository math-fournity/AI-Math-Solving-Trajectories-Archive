# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Given positive integers $n, k$ with $n \ge 2$, let $c(n, k)$ be the minimum constant such that for any positive integer $m$ and any $kn$-regular graph $G$ with $m$ vertices, there exists a coloring of the vertices of $G$ with $n$ colors such that the number of monochromatic edges is at most $c(n, k)m$.
Calculate the value of $100 \times c(4, 3)$.       — 题目文本
#   The original solution derives the formula $c(n, k) = \frac{n \binom{k}{2} + k}{nk+1}$. 
For $n=4$ and $k=3$:
$\binom{k}{2} = \binom{3}{2} = 3$.
$c(4, 3) = \frac{4(3) + 3}{4(3) + 1} = \frac{12 + 3}{12 + 1} = \frac{15}{13}$.
The problem asks for $100 \times c(4, 3) = 100 \times \frac{15}{13} = \frac{1500}{13}$.  — 标准解答
#   Let me analyze this problem carefully.

We have positive integers $n, k$ with $n \ge 2$. $c(n, k)$ is the minimum constant such that for any positive integer $m$ and any $kn$-regular graph $G$ with $m$ vertices, there exists a coloring of the vertices of $G$ with $n$ colors such that the number of monochromatic edges is at most $c(n, k) m$.

We need to calculate $100 \times c(4, 3)$.

So $n = 4$, $k = 3$, and we're looking at $kn = 12$-regular graphs, coloring with 4 colors, minimizing the maximum number of monochromatic edges (normalized by $m$).

Let me think about this. A $12$-regular graph on $m$ vertices has $6m$ edges. We color with 4 colors and want to minimize monochromatic edges.

For a random coloring with 4 colors, each edge is monochromatic with probability $1/4$, so expected monochromatic edges = $6m/4 = 1.5m$. But we can do better with a good coloring.

Let me think about what the optimal constant is.

For a $d$-regular graph colored with $n$ colors, the question is: what's the minimum (over colorings) of the maximum (over graphs) of the fraction of monochromatic edges?

Actually, let me think about this more carefully. We want:
$$c(n, k) = \sup_{G \text{ kn-regular}} \min_{\text{colorings}} \frac{\text{mono edges}}{m}$$

For a $d$-regular graph with $m$ vertices, total edges = $dm/2$. With $n$ colors, if we have a balanced coloring where each color class has $m/n$ vertices, the number of edges within color classes... 

Let me think about the worst case. Consider a complete graph $K_{d+1}$ which is $d$-regular. For $d = 12$, $K_{13}$ is 12-regular with 13 vertices. 

For $K_{13}$ colored with 4 colors, to minimize monochromatic edges, we want to balance the color classes. With 13 vertices and 4 colors, the most balanced partition is $4, 3, 3, 3$. The number of monochromatic edges is $\binom{4}{2} + 3\binom{3}{2} = 6 + 9 = 15$. So mono edges / $m$ = $15/13$.

But wait, is this the worst case? Let me think more generally.

Actually, let me think about this differently. The key insight is about what graph maximizes the minimum number of monochromatic edges.

For a $d$-regular graph, consider the "defect" or the structure that forces many monochromatic edges.

Let me think about the problem from the perspective of the probabilistic method and extremal cases.

For a $d$-regular graph on $m$ vertices with a proper $n$-coloring, we'd have 0 monochromatic edges. But not all $d$-regular graphs are $n$-colorable. The question is about the worst case over all $kn$-regular graphs.

Let me think about specific constructions. 

Consider a disjoint union of cliques $K_{kn+1}$. Each $K_{kn+1}$ is $kn$-regular. For $n=4, k=3$, these are $K_{13}$'s. As computed, with optimal coloring $4,3,3,3$, we get $15$ monochromatic edges per clique, so $15/13$ per vertex.

But can we do worse? Let me think about other constructions.

Actually, let me think about the problem more carefully. The question is asking for the supremum over all $kn$-regular graphs of the minimum fraction of monochromatic edges.

Let me consider a different approach. Think about a graph that is a disjoint union of copies of $K_{n,n}$ or some bipartite-like structure... no, those would be properly 2-colorable.

The worst case for coloring is when the graph is "far from" being properly colorable. Complete graphs are the natural candidate.

Let me think about whether $K_{kn+1}$ is indeed the worst case, or if there's something worse.

For a $d$-regular graph, the number of monochromatic edges in a coloring is:
$$\sum_{i=1}^{n} e_i$$
where $e_i$ is the number of edges within color class $i$.

If color class $i$ has $s_i$ vertices, then $e_i \leq \binom{s_i}{2}$ (with equality for a clique). But in a $d$-regular graph, the maximum number of edges within a set of $s_i$ vertices is limited.

Hmm, let me think about this differently using a known result.

Actually, I recall that for this type of problem, the answer relates to the concept of "judicious partitions" or the Edwards-Erdős type results.

Let me think about it from the perspective of the following: for a $d$-regular graph, what's the minimum number of monochromatic edges in an $n$-coloring?

There's a classical result that says: every graph with $e$ edges has an $n$-coloring with at most $\frac{e}{n} - \frac{m}{2}\frac{n-1}{n} \cdot \frac{d_{\min}}{...}$... hmm, I don't remember the exact formula.

Let me think about it more carefully from first principles.

For a $d$-regular graph on $m$ vertices with $e = dm/2$ edges, and an $n$-coloring:

The number of monochromatic edges = $e - $ (number of properly colored edges).

We want to maximize properly colored edges, i.e., maximize the number of edges going between different color classes.

If the color classes have sizes $s_1, \ldots, s_n$ with $\sum s_i = m$, then the maximum number of edges between different classes is at most $\sum_{i<j} s_i s_j = \frac{m^2 - \sum s_i^2}{2}$, but this is only achievable if the graph is complete. For a $d$-regular graph, the number of edges is $dm/2$, so the number of properly colored edges is at most $dm/2$ (trivially), and the number of monochromatic edges is at least $0$.

But we want the worst case over graphs. So we want a graph where every coloring has many monochromatic edges.

Let me think about the complete graph $K_{kn+1}$ again. It's $kn$-regular. With $n$ colors and $kn+1$ vertices, the most balanced coloring has classes of size $k+1, k, k, \ldots, k$ (one class of size $k+1$ and $n-1$ classes of size $k$). Wait, $kn + 1 = (k+1) + (n-1)k$, so yes, one class of size $k+1$ and $n-1$ classes of size $k$.

Monochromatic edges = $\binom{k+1}{2} + (n-1)\binom{k}{2} = \frac{k(k+1)}{2} + \frac{(n-1)k(k-1)}{2} = \frac{k}{2}[(k+1) + (n-1)(k-1)] = \frac{k}{2}[k+1 + nk - n - k + 1] = \frac{k}{2}[nk - n + 2] = \frac{k(nk - n + 2)}{2}$.

Per vertex: $\frac{k(nk - n + 2)}{2(kn+1)}$.

For $n=4, k=3$: $\frac{3(12 - 4 + 2)}{2 \cdot 13} = \frac{3 \cdot 10}{26} = \frac{30}{26} = \frac{15}{13}$.

So $c(4,3) \geq 15/13$.

Now, is this the worst case? Or can we find a graph that does worse?

Let me think about other constructions. What about a disjoint union of $K_{kn+1}$'s? That gives the same ratio, $15/13$.

What about other graphs? Let me think about whether we can do worse.

Consider a graph that is a "blow-up" or some other construction. 

Actually, let me think about this more carefully. The question is whether $K_{kn+1}$ (or disjoint unions of it) is the extremal graph.

Let me consider a different type of graph. What about a graph where the chromatic number is high?

For a $d$-regular graph with $d = kn$, the chromatic number is at most $kn + 1$ (by Brooks' theorem, it's at most $kn$ unless the graph is $K_{kn+1}$ or an odd cycle). So most $kn$-regular graphs are $kn$-colorable, but we're coloring with only $n$ colors.

Hmm, let me think about this problem differently. 

Actually, I think the key question is: what is the maximum, over all $kn$-regular graphs $G$ on $m$ vertices, of the minimum number of monochromatic edges in an $n$-coloring, divided by $m$?

Let me think about lower bounds more carefully.

For $K_{kn+1}$: we showed the ratio is $\frac{k(nk-n+2)}{2(kn+1)}$.

Let me consider another construction. Take a complete $n$-partite graph where each part has size $k$, i.e., $K_{k,k,\ldots,k}$ ($n$ parts of size $k$). This graph has $nk$ vertices and is $(n-1)k$-regular. That's not $kn$-regular. 

What about $K_{k+1, k+1, \ldots}$? No, let me think differently.

What about the complete graph $K_{kn+1}$? This seems like the natural extremal case because it's the "most connected" $kn$-regular graph.

But let me think about whether there's a graph that forces even more monochromatic edges.

Consider the following: take $n$ cliques of size $k+1$, and connect them in some way to make the graph $kn$-regular. Each clique $K_{k+1}$ has $k+1$ vertices, each of degree $k$. To make it $kn$-regular, each vertex needs $kn - k = k(n-1)$ more edges going outside its clique. 

If we have $n$ cliques of size $k+1$, total vertices = $n(k+1)$. Each vertex in clique $i$ needs $k(n-1)$ edges to other cliques. The number of edges between different cliques: each clique has $k+1$ vertices, each needing $k(n-1)$ external edges, so total external degree = $n(k+1)k(n-1)$, and external edges = $n(k+1)k(n-1)/2$. The number of pairs of cliques is $\binom{n}{2}$, and between each pair we can have at most $(k+1)^2$ edges. So we need $n(k+1)k(n-1)/2 \leq \binom{n}{2}(k+1)^2 = \frac{n(n-1)(k+1)^2}{2}$, which gives $k \leq k+1$, always true. So this is feasible.

But actually, let me think about whether this construction forces more monochromatic edges.

If we color this graph with $n$ colors, and we want to minimize monochromatic edges... Each clique $K_{k+1}$ needs to be colored. If we use a different color for each clique, then within each clique, all $k+1$ vertices have the same color, giving $\binom{k+1}{2}$ monochromatic edges per clique, total $n\binom{k+1}{2}$. 

But we could also distribute colors within cliques. The optimal coloring would balance things.

Hmm, this is getting complicated. Let me think about whether the answer is indeed $15/13$.

$100 \times 15/13 = 1500/13 \approx 115.38...$. That doesn't seem like a clean answer. Let me reconsider.

Maybe the answer isn't from the complete graph. Let me think about other approaches.

Actually, wait. Let me reconsider the problem. The problem says "for any positive integer $m$ and any $kn$-regular graph $G$ with $m$ vertices." So $c(n,k)$ must work for ALL $m$ and ALL $kn$-regular graphs. The constant $c(n,k)$ is the minimum such constant.

So $c(n,k) = \sup_{m, G} \min_{\text{coloring}} \frac{\text{mono}(G, \text{coloring})}{m}$.

For $K_{13}$ (which is 12-regular, $m=13$), the minimum mono edges is 15, giving ratio $15/13$.

But maybe for other graphs with other values of $m$, the ratio is higher?

Let me think about $m = 2$. A 12-regular graph on 2 vertices would need each vertex to have degree 12, but the maximum degree in a 2-vertex graph is 1. So no 12-regular graph exists on 2 vertices. Similarly, for small $m$, 12-regular graphs might not exist.

A $d$-regular graph on $m$ vertices requires $m \geq d+1$ and $md$ even. For $d = 12$, we need $m \geq 13$ and $12m$ even (always true). So the smallest $m$ is 13, giving $K_{13}$.

For $m = 14$: a 12-regular graph on 14 vertices. The complement is a 1-regular graph on 14 vertices, which is a perfect matching. So $G = K_{14}$ minus a perfect matching. 

For this graph, with 4 colors and 14 vertices, the most balanced coloring is $4, 4, 3, 3$ (or $4, 4, 4, 2$, etc.). Let me compute the minimum monochromatic edges.

$G = K_{14} - M$ where $M$ is a perfect matching (7 edges). Total edges = $\binom{14}{2} - 7 = 91 - 7 = 84 = 12 \cdot 14 / 2$. ✓

For a coloring with class sizes $s_1, s_2, s_3, s_4$ summing to 14, the number of monochromatic edges is:
$$\sum_i \left[\binom{s_i}{2} - \text{(matching edges within class } i)\right]$$

To minimize this, we want to maximize the matching edges within each class (so they get subtracted) and minimize $\sum \binom{s_i}{2}$.

$\sum \binom{s_i}{2}$ is minimized when classes are balanced: $4, 4, 3, 3$ gives $6 + 6 + 3 + 3 = 18$.

Now, the matching edges within each class: we have 7 matching edges. We want to maximize how many of them fall within the same color class. 

With classes of size $4, 4, 3, 3$: a class of size 4 can contain at most 2 matching edges, a class of size 3 can contain at most 1. So maximum matching edges within classes = $2 + 2 + 1 + 1 = 6$. (We need to check if this is achievable.)

If we can place 6 of the 7 matching edges within color classes, then mono edges = $18 - 6 = 12$, ratio = $12/14 = 6/7 \approx 0.857$.

Compare with $K_{13}$: ratio $15/13 \approx 1.154$.

So $K_{13}$ gives a higher ratio. Good.

Let me check $m = 13$ more carefully. $K_{13}$ is the only 12-regular graph on 13 vertices. With 4 colors, balanced partition $4, 3, 3, 3$ gives $\binom{4}{2} + 3\binom{3}{2} = 6 + 9 = 15$ mono edges. Can we do better with an unbalanced partition? $5, 3, 3, 2$: $10 + 3 + 3 + 1 = 17$. Worse. $4, 4, 3, 2$: $6 + 6 + 3 + 1 = 16$. Worse. $7, 2, 2, 2$: $21 + 1 + 1 + 1 = 24$. Much worse. So $4, 3, 3, 3$ is optimal, giving 15.

So for $m = 13$, the ratio is $15/13$.

Now let me think about whether there's a graph on more vertices that gives a higher ratio.

Consider a disjoint union of $K_{13}$'s. If $m$ is a multiple of 13, say $m = 13t$, then the graph is $t$ copies of $K_{13}$. The optimal coloring colors each $K_{13}$ optimally, giving $15t$ mono edges, ratio $15t/(13t) = 15/13$. Same ratio.

What about other graphs? Let me think about whether we can construct a 12-regular graph where every 4-coloring has a higher ratio of monochromatic edges.

Hmm, let me think about this more carefully. The question is essentially about the "maximum over $d$-regular graphs of the minimum monochromatic edges in $n$-coloring."

I think the answer might be related to a theorem by Edwards or Bollobás and Scott about judicious partitions.

Actually, let me think about this from a different angle. There's a result that says:

For any graph $G$ with $m$ vertices and $e$ edges, there exists an $n$-coloring with at most $\frac{e}{n} - \frac{m}{2} \cdot \frac{n-1}{n^2} \cdot \delta$ monochromatic edges... no, I don't think that's right.

Let me think about the probabilistic argument. If we randomly color with $n$ colors, each edge is monochromatic with probability $1/n$. So expected mono edges = $e/n = dm/(2n)$. For $d = kn$, this is $knm/(2n) = km/2$. So $c(n,k) \leq k/2$ by the probabilistic method (there exists a coloring with at most $km/2$ mono edges).

For $n=4, k=3$: $c(4,3) \leq 3/2 = 1.5$.

But we also have the lower bound from $K_{13}$: $c(4,3) \geq 15/13 \approx 1.154$.

Can we improve the upper bound? The probabilistic method gives $k/2$, but maybe we can do better.

Actually, there's a well-known result that improves on the random coloring bound. Let me think...

For a $d$-regular graph, we can use the following approach: if the graph is $n$-colorable, we get 0 mono edges. If not, we need to understand the structure.

Actually, let me think about this problem differently. Let me consider the "fractional" version.

In the fractional version, we assign each vertex a probability distribution over colors. The expected number of monochromatic edges is $\sum_{(u,v) \in E} \sum_i p_{u,i} p_{v,i}$ where $p_{u,i}$ is the probability of vertex $u$ getting color $i$.

For a $d$-regular graph, if we use the uniform distribution ($p_{u,i} = 1/n$ for all $u, i$), we get $e/n = dm/(2n)$ mono edges.

But we can be smarter. If the graph is vertex-transitive, we might use the structure.

Hmm, let me think about whether the answer is exactly $15/13$ or something else.

Let me consider the problem from the perspective of the "max-cut" type results. For 2-coloring ($n=2$), the problem is about max cut. For a $d$-regular graph, the max cut is at least $dm/2 \cdot (1/2 + 1/(2d))$... no, that's not quite right either.

Actually, for $n=2$ (2-coloring), the problem becomes: for a $2k$-regular graph, find the minimum number of monochromatic edges. This is equivalent to maximizing the cut. By Edwards' theorem (or the result that every graph has a cut of size at least $m/4 + \sqrt{m/2 + 1/16}/4 - 1/8$...), or more simply, for a $d$-regular graph, the max cut is at least $dm/4 + m/4$ (I think this is a result by... let me think).

Actually, for $d$-regular graphs, there's a result that the max cut is at least $\frac{d}{2} \cdot \frac{m}{2} + \frac{m}{4}$... I'm not sure. Let me think about the $n=2$ case more carefully.

For $n=2, k$: $2k$-regular graph, 2-coloring. Max cut ≥ ? 

For $K_{2k+1}$ (which is $2k$-regular), the max cut with 2 colors: balanced partition $\lfloor (2k+1)/2 \rfloor, \lceil (2k+1)/2 \rceil = k, k+1$. Cut size = $k(k+1)$. Total edges = $\binom{2k+1}{2} = k(2k+1)$. Mono edges = $k(2k+1) - k(k+1) = k(2k+1 - k - 1) = k^2$. Per vertex: $k^2/(2k+1)$.

For $n=2, k=1$: $K_3$, 2-coloring. Mono = $1$, per vertex = $1/3$. And $c(2,1) = 1/3$? Let me check: $2$-regular graph, 2-coloring. $K_3$ is the worst case? For $C_5$ (2-regular), max cut = 4, mono = 1, per vertex = 1/5. For $K_3$, mono = 1, per vertex = 1/3. So yes, $K_3$ is worse. $c(2,1) = 1/3$.

For $n=2, k=2$: $4$-regular graph, 2-coloring. $K_5$: balanced $2,3$, mono = $\binom{2}{2} + \binom{3}{2} = 1 + 3 = 4$, per vertex = $4/5$. Is there a worse graph? 

Hmm, $100 \times c(2,1) = 100/3 \approx 33.33$. Not clean. $100 \times c(2,2) = 80$. That's clean!

Let me check $n=2, k=3$: $6$-regular, 2-coloring. $K_7$: balanced $3,4$, mono = $3 + 6 = 9$, per vertex = $9/7$. $100 \times 9/7 \approx 128.57$. Not clean.

Hmm, so the answers aren't always clean. Let me reconsider.

Wait, but the problem asks for $100 \times c(4,3)$. If $c(4,3) = 15/13$, then $100 \times 15/13 = 1500/13 \approx 115.38$. Not clean.

Let me reconsider whether $K_{13}$ is really the worst case, or if there's a different graph that gives a clean answer.

Let me think about this differently. Maybe the answer is $k/2 = 3/2$ (the probabilistic bound), giving $100 \times 3/2 = 150$. That's clean!

But is the probabilistic bound tight? Is there a graph where every 4-coloring has exactly $3m/2$ monochromatic edges?

For a random 12-regular graph, the expected mono edges in a random 4-coloring is $3m/2$. But we can do better than random coloring. So the probabilistic bound is an upper bound, and it might not be tight.

Hmm, but maybe for certain graphs, we can't do better than $3m/2$? That seems unlikely since we can always find a coloring at least as good as random.

Actually, the probabilistic method says there EXISTS a coloring with at most $3m/2$ mono edges. But maybe we can always find one with fewer. The question is what the worst case is.

Let me think about this more carefully. 

For a $d$-regular graph, there's a result by Bollobás and Scott (or maybe Edwards) about judicious partitions. Let me think about what's known.

For $n$-coloring of a graph with $e$ edges, the minimum number of monochromatic edges is at most:
$$\frac{e}{n} - \frac{m(n-1)}{2n^2} \cdot d_{\min}$$
... I'm not sure about this formula.

Actually, let me think about a simpler approach. For a $d$-regular graph, consider the following greedy/rounding approach:

1. Start with a fractional coloring (each vertex gets $1/n$ of each color).
2. Round to an integral coloring.

The fractional coloring gives $e/n$ mono edges. The rounding introduces some error.

Actually, let me think about the problem from the LP relaxation perspective. The minimum number of monochromatic edges in an $n$-coloring is related to the minimum over all partitions of $\sum_i e(S_i)$ where $S_1, \ldots, S_n$ is a partition of $V$ and $e(S_i)$ is the number of edges within $S_i$.

The fractional relaxation allows each vertex to be fractionally assigned. The fractional minimum is:
$$\min \sum_{(u,v) \in E} \sum_i x_{u,i} x_{v,i}$$
subject to $\sum_i x_{u,i} = 1$ for all $u$, $x_{u,i} \geq 0$.

For a $d$-regular graph, setting $x_{u,i} = 1/n$ gives $\sum_{(u,v)} \sum_i 1/n^2 = e/n = dm/(2n)$.

But can we do better fractionally? For a vertex-transitive graph, the uniform assignment is optimal by symmetry. For $K_{kn+1}$, the fractional optimum is $e/n = \binom{kn+1}{2}/n = \frac{kn(kn+1)}{2n} = \frac{k(kn+1)}{2}$. Per vertex: $\frac{k(kn+1)}{2(kn+1)} = k/2$.

So the fractional optimum for $K_{kn+1}$ is $k/2$ per vertex. But the integral optimum is $\frac{k(nk-n+2)}{2(kn+1)}$ per vertex (as computed).

For $n=4, k=3$: fractional = $3/2 = 1.5$, integral = $15/13 \approx 1.154$.

So the integrality gap is $15/13$ vs $3/2$. The integral optimum is better than the fractional one? That can't be right. The integral optimum should be at least as large as the fractional optimum.

Wait, I think I made an error. Let me recompute.

For $K_{13}$ with 4 colors:
- Fractional: each vertex gets $1/4$ of each color. Mono edges = $e \cdot (1/4)^2 \cdot 4 = e/4 = 78/4 = 19.5$. Wait, no. $\sum_{(u,v)} \sum_i x_{u,i} x_{v,i} = \sum_{(u,v)} \sum_i (1/4)^2 = e \cdot 4 \cdot (1/16) = e/4 = 78/4 = 19.5$. Per vertex: $19.5/13 = 1.5$.

- Integral (best): 15. Per vertex: $15/13 \approx 1.154$.

So the integral optimum (15) is LESS than the fractional optimum (19.5)? That's impossible! The fractional relaxation should give a lower bound on the integral optimum.

Oh wait, I think I have the direction wrong. The fractional relaxation gives a LOWER bound on the minimum integral solution. So the minimum integral mono edges ≥ minimum fractional mono edges. But 15 < 19.5, which contradicts this.

Let me recheck. The fractional assignment $x_{u,i} = 1/4$ gives 19.5 mono edges. But this is just ONE fractional assignment. The minimum over all fractional assignments could be lower.

For $K_{13}$, can we find a fractional assignment with fewer than 15 mono edges? 

Actually, for $K_n$, the minimum fractional $n$-coloring... hmm, let me think. For $K_{13}$ with 4 colors, the fractional relaxation allows splitting vertices. The minimum of $\sum_{(u,v)} \sum_i x_{u,i} x_{v,i}$ subject to $\sum_i x_{u,i} = 1$.

For $K_{13}$, by symmetry, the optimal fractional solution might not be uniform. Let me think...

Actually, for $K_n$ (complete graph), the minimum number of monochromatic edges in a fractional $k$-coloring is 0 if $k \geq n$ (just assign each vertex a distinct color). For $k < n$, we need to think.

For $K_{13}$ with 4 colors fractionally: we can assign 4 vertices to color 1, 3 to color 2, 3 to color 3, 3 to color 4 (integrally), giving 15. But fractionally, we could do better by splitting.

Actually, the fractional chromatic number of $K_{13}$ is 13, so we need at least 13 colors fractionally to get 0 mono edges. With 4 colors, the fractional minimum is... 

For $K_n$ with $k$ colors, the minimum fractional mono edges: by symmetry, the optimal is to assign each vertex uniformly, $x_{u,i} = 1/k$. This gives $e/k = \binom{n}{2}/k$ mono edges. But can we do better?

For $K_n$, any fractional coloring has $\sum_{(u,v)} \sum_i x_{u,i} x_{v,i} \geq \binom{n}{2}/k$ by... actually, I think for $K_n$, the uniform assignment IS optimal. Here's why: for $K_n$, $\sum_{(u,v)} \sum_i x_{u,i} x_{v,i} = \sum_i \sum_{u \neq v} x_{u,i} x_{v,i} / 2$... wait, let me be more careful.

$\sum_{(u,v) \in E} \sum_i x_{u,i} x_{v,i} = \sum_i \sum_{(u,v) \in E} x_{u,i} x_{v,i}$

For $K_n$, $E$ is all pairs, so $= \sum_i \sum_{u < v} x_{u,i} x_{v,i} = \frac{1}{2} \sum_i \left[ \left(\sum_u x_{u,i}\right)^2 - \sum_u x_{u,i}^2 \right]$.

Let $S_i = \sum_u x_{u,i}$. Then $\sum_i S_i = n$ (since each vertex contributes 1 total). And $\sum_u x_{u,i}^2 \geq S_i^2 / n$ by Cauchy-Schwarz (or QM-AM). Wait, actually $\sum_u x_{u,i}^2 \geq S_i^2 / n$ when there are $n$ terms... no, that's $\sum_u x_{u,i}^2 \geq S_i^2 / n$ by Cauchy-Schwarz (with $n$ variables). Actually, $\sum_u x_{u,i}^2 \geq S_i^2 / n$ is wrong; it should be $\sum_u x_{u,i}^2 \geq S_i^2 / n$ when there are $n$ terms, which is correct by QM-AM: $\frac{\sum x_{u,i}^2}{n} \geq \left(\frac{\sum x_{u,i}}{n}\right)^2 = \frac{S_i^2}{n^2}$, so $\sum x_{u,i}^2 \geq S_i^2 / n$.

So $\sum_{u<v} x_{u,i} x_{v,i} = \frac{S_i^2 - \sum_u x_{u,i}^2}{2} \leq \frac{S_i^2 - S_i^2/n}{2} = \frac{S_i^2 (n-1)}{2n}$.

Thus total mono edges $\leq \frac{n-1}{2n} \sum_i S_i^2$.

By Cauchy-Schwarz, $\sum_i S_i^2 \geq \frac{(\sum_i S_i)^2}{k} = \frac{n^2}{k}$.

So total mono edges $\leq \frac{(n-1) n}{2k}$... wait, that's an upper bound, not a lower bound. Let me redo this.

We have mono edges $= \frac{1}{2} \sum_i (S_i^2 - \sum_u x_{u,i}^2)$.

To minimize this, we want to minimize $\sum_i S_i^2$ and maximize $\sum_i \sum_u x_{u,i}^2$.

$\sum_i S_i^2$ is minimized when $S_i = n/k$ for all $i$, giving $\sum_i S_i^2 = n^2/k$.

$\sum_i \sum_u x_{u,i}^2$ is maximized when each $x_{u,i}$ is as concentrated as possible, i.e., $x_{u,i} \in \{0, 1\}$. But we're doing fractional, so we want to see what's achievable.

If $S_i = n/k$ for all $i$, and we want to maximize $\sum_u \sum_i x_{u,i}^2$, by convexity, we should make each $x_{u,i}$ as extreme as possible. The maximum of $\sum_i x_{u,i}^2$ subject to $\sum_i x_{u,i} = 1, x_{u,i} \geq 0$ is 1 (achieved when one $x_{u,i} = 1$). The minimum is $1/k$ (uniform).

So if we use integral assignments, $\sum_u \sum_i x_{u,i}^2 = n$, and mono edges $= \frac{1}{2}(n^2/k - n) = \frac{n(n-k)}{2k}$.

For $K_{13}$ with $k=4$: $\frac{13 \cdot 9}{8} = \frac{117}{8} = 14.625$.

But wait, with integral assignments and $S_i = 13/4$, which isn't an integer, we can't have exactly $S_i = 13/4$. The closest is $4, 3, 3, 3$, giving $\sum S_i^2 = 16 + 9 + 9 + 9 = 43$, and $\sum x_{u,i}^2 = 13$ (integral). Mono edges $= \frac{43 - 13}{2} = 15$. ✓

With fractional assignments and $S_i = 13/4$: $\sum S_i^2 = 4 \cdot (13/4)^2 = 4 \cdot 169/16 = 169/4 = 42.25$. And $\sum x_{u,i}^2$ can be at most... if we make each vertex's assignment as concentrated as possible while maintaining $S_i = 13/4$... 

Actually, with $S_i = 13/4$ for each $i$, and 13 vertices, the average $x_{u,i} = 1/4$ for each $u, i$. To maximize $\sum x_{u,i}^2$, we'd want some vertices to have $x_{u,i}$ close to 1 and others close to 0, but we need $S_i = 13/4$ for each color.

One approach: assign 4 vertices to be purely color 1, 3 to be purely color 2, 3 purely color 3, 3 purely color 4. But then $S_1 = 4, S_2 = 3, S_3 = 3, S_4 = 3$, not uniform.

To get $S_i = 13/4$ for all $i$ with maximum $\sum x^2$: we could have some vertices purely one color and others split. For example, 1 vertex purely color 1 ($S_1$ contribution 1), and the remaining $13/4 - 1 = 9/4$ comes from other vertices. This is getting complicated.

The point is: the fractional minimum for $K_{13}$ with 4 colors is $\frac{1}{2}(169/4 - \max \sum x^2)$. The maximum $\sum x^2$ with $S_i = 13/4$ is achieved by making assignments as extreme as possible. 

Actually, I realize the fractional minimum might be lower than 15. Let me think about whether we can achieve fewer than 15 mono edges fractionally for $K_{13}$.

With $S_i = 13/4$ and maximizing $\sum x_{u,i}^2$: We can have 3 vertices purely color 1, 3 purely color 2, 3 purely color 3, 3 purely color 4, and 1 vertex split equally: $1/4$ of each color. Then $S_i = 3 + 1/4 = 13/4$ for each $i$. And $\sum x_{u,i}^2 = 12 \cdot 1 + 4 \cdot (1/4)^2 = 12 + 1/4 = 49/4$. Mono edges $= \frac{169/4 - 49/4}{2} = \frac{120/4}{2} = \frac{30}{2} = 15$.

Hmm, same as integral! What if we split more vertices?

2 vertices purely color 1, 2 purely color 2, 2 purely color 3, 2 purely color 4, and 5 vertices each split equally: $S_i = 2 + 5/4 = 13/4$. $\sum x^2 = 8 + 5 \cdot 4 \cdot (1/16) = 8 + 5/4 = 37/4$. Mono $= (169/4 - 37/4)/2 = (132/4)/2 = 33/2 = 16.5$. Worse!

So splitting more makes it worse. The best fractional with $S_i = 13/4$ is to have as many pure assignments as possible: 12 pure + 1 split, giving 15.

What if $S_i$ is not uniform? Let's try $S_1 = 4, S_2 = S_3 = S_4 = 3$ (integral): mono = 15 as computed.

What about $S_1 = 4.5, S_2 = 3, S_3 = 3, S_4 = 2.5$? $\sum S_i^2 = 20.25 + 9 + 9 + 6.25 = 44.5$. To maximize $\sum x^2$: we want as many pure assignments as possible. With $S_1 = 4.5$: 4 pure + 1 half. $S_4 = 2.5$: 2 pure + 1 half. $S_2 = S_3 = 3$: 3 pure each. Total pure: 4 + 3 + 3 + 2 = 12, plus 1 vertex split between colors 1 and 4 (half each). $\sum x^2 = 12 + 2 \cdot (1/2)^2 = 12.5$. Mono $= (44.5 - 12.5)/2 = 16$. Worse.

So it seems like 15 is the minimum for $K_{13}$, both fractionally and integrally. Good.

Now, the key question: is $K_{13}$ (or disjoint unions of it) the worst case for 12-regular graphs with 4-coloring?

Let me think about what other graphs could be worse.

Consider a graph $G$ that is 12-regular on $m$ vertices where $m$ is large. Can the minimum mono edges per vertex exceed $15/13$?

For large $m$, a random 12-regular graph is "locally tree-like" and has good expansion. For such graphs, we might be able to find colorings with very few mono edges (close to 0 if the graph is 4-colorable, which it likely is for large $m$).

But we need to consider the worst case, not random graphs.

Let me think about a different construction. Consider the complete multipartite graph or some algebraic construction.

Actually, let me think about the problem from the perspective of the "fractional chromatic number" and the "vector chromatic number."

Hmm, let me try a different approach. Let me think about what happens with a graph that's a union of $K_{13}$'s but with some cross-edges.

Actually, I think the key insight might be related to the following: for $d$-regular graphs, the worst case for $n$-coloring is the complete graph $K_{d+1}$ (when it exists, i.e., when $d+1$ vertices suffice). This is because $K_{d+1}$ is the "most constrained" $d$-regular graph.

But I should verify this. Let me think about whether there's a theorem that establishes this.

There's a result by Bollobás and Scott on judicious partitions, and results by Edwards on max cuts. Let me think about the specific case.

For 2-coloring of $d$-regular graphs: the minimum number of monochromatic edges (i.e., edges not in the max cut) is at most... 

For $K_{d+1}$ with 2 colors: balanced partition $\lfloor(d+1)/2\rfloor, \lceil(d+1)/2\rceil$. Mono = $\binom{\lfloor(d+1)/2\rfloor}{2} + \binom{\lceil(d+1)/2\rceil}{2}$.

For $d$ even ($d = 2k$): $K_{2k+1}$, partition $k, k+1$. Mono = $\binom{k}{2} + \binom{k+1}{2} = \frac{k(k-1)}{2} + \frac{k(k+1)}{2} = k^2$. Per vertex: $k^2/(2k+1)$.

For $d$ odd ($d = 2k+1$): $K_{2k+2}$, partition $k+1, k+1$. Mono = $2\binom{k+1}{2} = k(k+1)$. Per vertex: $k(k+1)/(2k+2) = k/2$.

There's a classical result (I think by Edwards or Poljak and Turzík) that for any graph with $m$ vertices and $e$ edges, the max cut is at least $e/2 + (m-1)/4$. For a $d$-regular graph, $e = dm/2$, so max cut $\geq dm/4 + (m-1)/4$. Mono edges $\leq dm/2 - dm/4 - (m-1)/4 = dm/4 - (m-1)/4 = (dm - m + 1)/4 = (m(d-1) + 1)/4$.

Per vertex: $\approx (d-1)/4$.

For $d = 2k$ (even): $(2k-1)/4$ per vertex. Compare with $K_{2k+1}$: $k^2/(2k+1)$ per vertex. For $k=1$: $(2-1)/4 = 1/4$ vs $1/3$. So $K_3$ is worse. For $k=2$: $3/4$ vs $4/5$. $K_5$ is worse. For $k=3$: $5/4$ vs $9/7 \approx 1.286$. $K_7$ is worse ($9/7 > 5/4$).

So the Edwards bound gives $(d-1)/4$ per vertex, but $K_{d+1}$ gives a higher ratio. So the Edwards bound is not tight for the worst case.

Hmm, but the Edwards bound is a lower bound on the max cut (upper bound on mono edges). The actual worst case might be higher than the Edwards bound but we need to check if $K_{d+1}$ is the worst case.

For $n = 2$, the worst case for $d$-regular graphs is indeed $K_{d+1}$ (or disjoint unions of it). This is because $K_{d+1}$ has the highest "density" and forces the most monochromatic edges.

Actually, I'm not sure this is proven. Let me think about it differently.

Let me consider the general $n$-coloring case. The question is:

$$c(n, k) = \sup_G \min_{\text{coloring}} \frac{\text{mono}(G)}{m}$$

where the sup is over all $kn$-regular graphs $G$ on $m$ vertices (for any valid $m$).

Claim: $c(n, k) = \frac{k(nk - n + 2)}{2(kn + 1)}$, achieved by $K_{kn+1}$.

For $n = 4, k = 3$: $c(4, 3) = \frac{3(12 - 4 + 2)}{2 \cdot 13} = \frac{30}{26} = \frac{15}{13}$.

$100 \times 15/13 = 1500/13 \approx 115.38$.

This is not a clean number. Let me reconsider whether the answer might be different.

Actually, wait. Let me reconsider the problem. Maybe I need to think about this more carefully.

Let me reconsider: is the worst case really $K_{kn+1}$? Or could there be a graph on more vertices that's worse?

Let me think about a specific example. Consider $n = 4, k = 3$, so 12-regular graphs.

What about $m = 26$? Consider a graph that's two copies of $K_{13}$ with a perfect matching between them (removing one edge from each $K_{13}$ to maintain regularity). Actually, this is getting complicated. Let me think of a cleaner construction.

What about the complete graph $K_{13}$ vs. some other 12-regular graph on more vertices?

Let me think about the "Kneser graph" or some other specific graph.

Actually, let me think about this from the perspective of the following result:

For a $d$-regular graph $G$ on $m$ vertices, the minimum number of monochromatic edges in an $n$-coloring is at most:
$$\frac{dm}{2n} - \frac{m}{2} \cdot \frac{d - n + 1}{n \cdot (kn + 1)}$$

Hmm, I'm just guessing at this point. Let me think more carefully.

Let me consider the following approach. For a $d$-regular graph, consider the eigenvalue approach. The number of monochromatic edges in a coloring is related to the quadratic form of the adjacency matrix.

If we have a coloring $\sigma: V \to [n]$, and we define indicator vectors $\mathbf{1}_i$ for each color class, then the number of monochromatic edges is:
$$\text{mono} = \sum_{i=1}^n \frac{\mathbf{1}_i^T A \mathbf{1}_i}{2}$$

where $A$ is the adjacency matrix. This equals:
$$\frac{1}{2} \sum_i \mathbf{1}_i^T A \mathbf{1}_i = \frac{1}{2} \text{tr}(A \sum_i \mathbf{1}_i \mathbf{1}_i^T)$$

Hmm, this is getting complicated. Let me try a different approach.

Let me think about the problem using the following known result:

**Theorem (Edwards, 1973; improved by various authors):** For any graph $G$ with $m$ vertices and $e$ edges, there exists a bipartition (2-coloring) with at most $\frac{e}{2} - \frac{m-1}{4}$ monochromatic edges.

This generalizes to $n$-colorings. For $n$-colorings, there's a result that says:

**Theorem:** For any graph $G$ with $m$ vertices and $e$ edges, there exists an $n$-coloring with at most $\frac{e}{n} - \frac{m(n-1)}{2n^2}$ monochromatic edges... but I need to check this.

Actually, I think the generalization is:

For $n$-coloring, the minimum number of monochromatic edges is at most $\frac{e}{n} - \frac{m-1}{2n} \cdot \frac{n-1}{n}$... I'm not sure.

Let me try to derive it. For a $d$-regular graph on $m$ vertices, $e = dm/2$.

Random coloring gives $e/n = dm/(2n)$ mono edges in expectation.

Can we always do better? For $n = 2$, Edwards showed we can save at least $(m-1)/4$. For general $n$, the saving might be different.

Let me think about the $n$-coloring version of Edwards' result.

Actually, there's a result by Bollobás and Scott (2004) on judicious partitions, and also a result by Edwards generalized to $n$-colorings.

The generalization I recall is: for any graph with $m$ vertices and $e$ edges, there's an $n$-coloring with at most $\frac{e}{n} - \frac{m-1}{2n}$ monochromatic edges. But I'm not sure if this is correct.

Let me check with $K_3$ ($n=2$): $e = 3, m = 3$. Bound: $3/2 - 2/4 = 3/2 - 1/2 = 1$. Actual minimum: 1. ✓

$K_5$ ($n=2$): $e = 10, m = 5$. Bound: $5 - 4/4 = 5 - 1 = 4$. Actual: 4. ✓

$K_7$ ($n=2$): $e = 21, m = 7$. Bound: $21/2 - 6/4 = 10.5 - 1.5 = 9$. Actual: 9. ✓

So for $n = 2$, the bound $\frac{e}{n} - \frac{m-1}{2n} = \frac{e}{2} - \frac{m-1}{4}$ matches Edwards' bound, and it's tight for complete graphs $K_{2k+1}$.

Now for general $n$: is the bound $\frac{e}{n} - \frac{m-1}{2n}$?

Let me check with $K_{13}$ ($n=4$): $e = 78, m = 13$. Bound: $78/4 - 12/8 = 19.5 - 1.5 = 18$. But actual minimum is 15. So the bound 18 is not tight for $K_{13}$ with 4 colors. The bound is an upper bound, and 15 < 18, so it's consistent but not tight.

Hmm, so the Edwards-type bound for $n$-colorings is not tight for $K_{kn+1}$ when $n > 2$. Let me think about what the tight bound is.

Actually, maybe the bound for $n$-colorings is different. Let me think about this more carefully.

For $n$-coloring, the Edwards bound generalizes to: $\frac{e}{n} - \frac{m-1}{2n} \cdot \frac{n-1}{n}$? Let me check.

For $n=2$: $\frac{e}{2} - \frac{m-1}{4} \cdot \frac{1}{1}$... no, $\frac{n-1}{n} = 1/2$ for $n=2$. So $\frac{e}{2} - \frac{m-1}{4} \cdot \frac{1}{2} = \frac{e}{2} - \frac{m-1}{8}$. That doesn't match Edwards.

Let me try another generalization. Maybe the bound is $\frac{e}{n} - \frac{m(n-1)}{2n^2}$?

For $n=2$: $\frac{e}{2} - \frac{m}{4}$. For $K_3$: $3/2 - 3/4 = 3/4$. But actual is 1. So this bound says at most $3/4$ mono edges, but actual minimum is 1. That's wrong (the bound should be an upper bound on the minimum, so it should be ≥ actual minimum).

Hmm, $3/4 < 1$, so this would say there's a coloring with at most $3/4$ mono edges, but the actual minimum is 1. So this bound is too strong and incorrect.

Let me try $\frac{e}{n} - \frac{m-1}{2n}$:

For $n=2, K_3$: $3/2 - 2/4 = 1$. ✓ (tight)
For $n=4, K_{13}$: $78/4 - 12/8 = 19.5 - 1.5 = 18$. Actual is 15, so bound is valid but not tight.

So the bound $\frac{e}{n} - \frac{m-1}{2n}$ is valid for $n=2$ (tight for odd complete graphs) but gives 18 for $K_{13}$ with $n=4$, while actual is 15.

Is this bound actually valid for $n > 2$? Let me think about whether it's proven.

Actually, I think the Edwards bound for $n$-colorings might be: $\frac{e}{n} - \frac{m-1}{2n}$, and this is proven by induction on $n$ (reduce to the $n=2$ case). But I'm not certain.

If this bound is valid, then for a $kn$-regular graph on $m$ vertices:
$$\text{mono} \leq \frac{knm/2}{n} - \frac{m-1}{2n} = \frac{km}{2} - \frac{m-1}{2n}$$

Per vertex: $\frac{k}{2} - \frac{1}{2n} + \frac{1}{2nm} \to \frac{k}{2} - \frac{1}{2n}$ as $m \to \infty$.

For $n=4, k=3$: $\frac{3}{2} - \frac{1}{8} = \frac{11}{8} = 1.375$.

But for $K_{13}$: $\frac{3 \cdot 13}{2} - \frac{12}{8} = 19.5 - 1.5 = 18$, while actual is 15. So the bound gives 18, but actual is 15. The bound is valid but not tight for $K_{13}$.

So the question is: is there a $kn$-regular graph where the minimum mono edges per vertex is close to $\frac{k}{2} - \frac{1}{2n}$?

For $n=4, k=3$: $\frac{11}{8} = 1.375$. Is there a 12-regular graph where every 4-coloring has at least $1.375m$ mono edges?

$K_{13}$ gives $15/13 \approx 1.154$, which is less than $1.375$. So if the bound $\frac{k}{2} - \frac{1}{2n}$ is achievable, there must be a different graph that achieves it.

Hmm, but is the bound $\frac{e}{n} - \frac{m-1}{2n}$ actually proven for $n > 2$? Let me think about this.

For $n = 2$, Edwards proved: max cut $\geq e/2 + (m-1)/4$, i.e., mono $\leq e/2 - (m-1)/4$.

For general $n$, one approach: first find a good 2-coloring, then split each color class into $n/2$ sub-classes (if $n$ is even). But this doesn't directly give the bound.

Actually, I think the correct generalization might be different. Let me look at this from a different angle.

For $n$-coloring, the random coloring gives $e/n$ mono edges. The question is how much we can improve.

For $n = 2$: improvement of $(m-1)/4$ (Edwards).
For general $n$: ?

I think the improvement for $n$-colorings is $\frac{(n-1)(m-1)}{2n^2}$... let me check.

For $n = 2$: $\frac{1 \cdot (m-1)}{8}$. But Edwards gives $(m-1)/4$. So this doesn't match.

Let me try $\frac{(n-1)(m-1)}{2n}$:

For $n = 2$: $(m-1)/4$. ✓ Matches Edwards.

For $n = 4, K_{13}$: $\frac{3 \cdot 12}{8} = \frac{36}{8} = 4.5$. So bound: $78/4 - 4.5 = 19.5 - 4.5 = 15$. That matches the actual minimum of 15!

Wait, that's interesting! Let me double-check.

Bound: $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$.

For $K_{13}$ with $n=4$: $e = 78, m = 13$. $\frac{78}{4} - \frac{3 \cdot 12}{8} = 19.5 - 4.5 = 15$. And actual minimum is 15. So the bound is tight!

Let me check for $n=2$:
$K_3$: $e=3, m=3$. $3/2 - 1 \cdot 2/4 = 1.5 - 0.5 = 1$. Actual: 1. ✓
$K_5$: $e=10, m=5$. $5 - 4/4 = 5 - 1 = 4$. Actual: 4. ✓
$K_7$: $e=21, m=7$. $21/2 - 6/4 = 10.5 - 1.5 = 9$. Actual: 9. ✓

Let me check for $n=3, K_7$ (6-regular, $n=3, k=2$): $e=21, m=7$. $\frac{21}{3} - \frac{2 \cdot 6}{6} = 7 - 2 = 5$. 

Actual minimum for $K_7$ with 3 colors: balanced partition $3, 2, 2$. Mono = $\binom{3}{2} + 2\binom{2}{2} = 3 + 2 = 5$. ✓

Let me check $n=3, K_4$ (3-regular, $n=3, k=1$): $e=6, m=4$. $\frac{6}{3} - \frac{2 \cdot 3}{6} = 2 - 1 = 1$. Actual: $K_4$ with 3 colors, partition $2, 1, 1$. Mono = $\binom{2}{2} = 1$. ✓

So the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ seems to be tight for complete graphs $K_{kn+1}$!

Let me verify the formula for general $K_{kn+1}$ with $n$ colors:
- $e = \binom{kn+1}{2} = \frac{kn(kn+1)}{2}$
- $m = kn+1$
- Bound: $\frac{e}{n} - \frac{(n-1)(m-1)}{2n} = \frac{kn(kn+1)}{2n} - \frac{(n-1) \cdot kn}{2n} = \frac{k(kn+1)}{2} - \frac{k(n-1)}{2} = \frac{k}{2}[(kn+1) - (n-1)] = \frac{k}{2}[kn - n + 2] = \frac{k(kn - n + 2)}{2}$.

And the actual minimum (balanced partition $k+1, k, k, \ldots, k$): $\binom{k+1}{2} + (n-1)\binom{k}{2} = \frac{k(k+1)}{2} + \frac{(n-1)k(k-1)}{2} = \frac{k}{2}[(k+1) + (n-1)(k-1)] = \frac{k}{2}[k + 1 + nk - n - k + 1] = \frac{k}{2}[nk - n + 2] = \frac{k(kn - n + 2)}{2}$. ✓

So the bound is tight for $K_{kn+1}$.

Now, the question is: is this bound valid for ALL graphs (not just complete graphs)? If so, then $c(n,k) = \sup_G \frac{\text{bound}}{m} = \sup_G \left[\frac{e}{nm} - \frac{(n-1)(m-1)}{2nm}\right]$.

For a $kn$-regular graph: $e = knm/2$, so $\frac{e}{nm} = \frac{k}{2}$.

Bound per vertex: $\frac{k}{2} - \frac{(n-1)(m-1)}{2nm} = \frac{k}{2} - \frac{(n-1)}{2n} + \frac{(n-1)}{2nm}$.

As $m \to \infty$: $\frac{k}{2} - \frac{n-1}{2n}$.

For $m = kn+1$ (smallest possible): $\frac{k}{2} - \frac{(n-1) \cdot kn}{2n(kn+1)} = \frac{k}{2} - \frac{k(n-1)}{2(kn+1)} = \frac{k(kn+1) - k(n-1)}{2(kn+1)} = \frac{k(kn + 1 - n + 1)}{2(kn+1)} = \frac{k(kn - n + 2)}{2(kn+1)}$.

This is the $K_{kn+1}$ value. As $m$ increases, the bound per vertex increases (since $\frac{(n-1)}{2nm}$ decreases, making the bound larger). So the supremum is $\frac{k}{2} - \frac{n-1}{2n} = \frac{kn - n + 1}{2n}$... wait, let me recalculate.

$\frac{k}{2} - \frac{n-1}{2n} = \frac{kn - (n-1)}{2n} = \frac{kn - n + 1}{2n}$.

For $n=4, k=3$: $\frac{12 - 4 + 1}{8} = \frac{9}{8} = 1.125$.

But $K_{13}$ gives $15/13 \approx 1.154 > 9/8 = 1.125$.

Wait, that's contradictory. The bound per vertex for $m = kn+1$ is $\frac{k(kn-n+2)}{2(kn+1)} = 15/13 \approx 1.154$, and as $m \to \infty$ it approaches $\frac{kn-n+1}{2n} = 9/8 = 1.125$. So the bound is DECREASING as $m$ increases? Let me recheck.

Bound per vertex: $\frac{k}{2} - \frac{(n-1)(m-1)}{2nm}$.

As $m$ increases, $\frac{(n-1)(m-1)}{2nm}$ increases (approaching $\frac{n-1}{2n}$), so the bound DECREASES. So the maximum is at $m = kn+1$ (the smallest $m$), giving $\frac{k(kn-n+2)}{2(kn+1)}$.

So if the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is valid for all graphs, then:

$$c(n, k) = \frac{k(kn - n + 2)}{2(kn + 1)}$$

achieved by $K_{kn+1}$.

For $n=4, k=3$: $c(4,3) = \frac{3 \cdot 10}{26} = \frac{30}{26} = \frac{15}{13}$.

$100 \times 15/13 = 1500/13 \approx 115.38$.

Hmm, still not clean. Let me reconsider whether the bound is actually valid.

Actually, wait. I need to verify that the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is a valid upper bound on the minimum number of monochromatic edges for ALL graphs, not just complete graphs.

This is a generalization of Edwards' theorem. Edwards' theorem for $n=2$ says: for any graph with $e$ edges and $m$ vertices, max cut $\geq e/2 + (m-1)/4$, i.e., mono $\leq e/2 - (m-1)/4$.

The generalization to $n$ colors would be: for any graph with $e$ edges and $m$ vertices, there exists an $n$-coloring with at most $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ monochromatic edges.

Is this true? Let me think about whether this has been proven.

Actually, I recall that the Edwards bound for $n$-colorings is indeed a known result. Let me think about the proof.

For $n = 2$, Edwards' proof works by induction on $m$. The key idea is that for any graph, there's a vertex $v$ such that removing $v$ and applying the induction hypothesis, then adding $v$ back to the side that minimizes mono edges.

For general $n$, the proof would be similar: remove a vertex, color the rest by induction, then add the vertex to the color class that minimizes the increase in mono edges.

Let me try to prove the bound by induction.

Claim: For any graph $G$ with $m$ vertices and $e$ edges, there's an $n$-coloring with at most $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ monochromatic edges.

Base case: $m = 1$. $e = 0$. Bound: $0 - 0 = 0$. ✓

Inductive step: Assume true for graphs with $m-1$ vertices. Consider $G$ with $m$ vertices and $e$ edges. Remove a vertex $v$ with degree $d(v)$. The remaining graph $G - v$ has $m-1$ vertices and $e - d(v)$ edges. By induction, there's an $n$-coloring of $G - v$ with at most $\frac{e - d(v)}{n} - \frac{(n-1)(m-2)}{2n}$ mono edges.

Now, add $v$ to the color class that minimizes the number of new mono edges. The number of new mono edges is the number of neighbors of $v$ in the chosen color class. The minimum over $n$ color classes is at most $d(v)/n$ (by averaging).

So total mono edges $\leq \frac{e - d(v)}{n} - \frac{(n-1)(m-2)}{2n} + \frac{d(v)}{n} = \frac{e}{n} - \frac{(n-1)(m-2)}{2n}$.

But we want to show $\leq \frac{e}{n} - \frac{(n-1)(m-1)}{2n}$.

We have $\frac{e}{n} - \frac{(n-1)(m-2)}{2n}$, and we want $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$.

The difference is $\frac{(n-1)(m-1)}{2n} - \frac{(n-1)(m-2)}{2n} = \frac{n-1}{2n}$.

So we need to save an additional $\frac{n-1}{2n}$ mono edges when adding $v$. But the averaging argument only guarantees $d(v)/n$ new mono edges, which gives us the bound $\frac{e}{n} - \frac{(n-1)(m-2)}{2n}$, not the stronger bound.

So the simple induction doesn't give the stronger bound. We need a better argument.

For $n = 2$, Edwards' proof is more subtle. The key is that when adding $v$, we can choose the better of the two color classes, and the saving is at least $d(v)/2 - |d_1(v) - d_2(v)|/2$ where $d_i(v)$ is the number of neighbors in color class $i$. But actually, the saving from choosing the better class is $\max(d_1, d_2) - d(v)/2 = |d_1 - d_2|/2$... no, the number of new mono edges is $\min(d_1, d_2) \leq d(v)/2$, and the saving compared to $d(v)/2$ is $d(v)/2 - \min(d_1, d_2) = |d_1 - d_2|/2$.

Edwards' actual proof is more involved. He uses the fact that for $n=2$, the bound $e/2 - (m-1)/4$ is achieved by choosing the right vertex to remove and using a more careful analysis.

Actually, I think the correct generalization might not be $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$. Let me reconsider.

For $n = 2$, the Edwards bound is $\frac{e}{2} - \frac{m-1}{4}$. Note that $\frac{(n-1)(m-1)}{2n} = \frac{(m-1)}{4}$ for $n=2$. ✓

But the inductive proof for $n = 2$ doesn't work with the simple averaging argument. Edwards' proof uses a different technique.

Let me look at this from a different angle. Maybe the bound for general $n$ is different.

Actually, I found that the generalization of Edwards' bound to $n$-colorings is:

**Theorem (Edwards, 1973; for general $n$, see e.g., Bollobás & Scott):** For any graph with $e$ edges and $m$ vertices, there exists an $n$-coloring with at most $\frac{e}{n} - \frac{m-1}{2n} \cdot \frac{n-1}{n}$ monochromatic edges.

Wait, that gives $\frac{e}{n} - \frac{(n-1)(m-1)}{2n^2}$.

For $n=2$: $\frac{e}{2} - \frac{(m-1)}{8}$. But Edwards' bound is $\frac{e}{2} - \frac{m-1}{4}$. So this doesn't match.

Hmm, let me try yet another generalization.

Actually, I think there are different generalizations. Let me think about what's known.

For $n$-coloring, the random coloring gives $e/n$ mono edges. The question is the best improvement.

One result I recall is by Bollobás and Scott (2004): for any graph with $m$ vertices and $e$ edges, there's an $n$-coloring with at most $\frac{e}{n} - \frac{m}{2n} \cdot \frac{n-1}{n} \cdot \delta$ mono edges, where $\delta$ is the minimum degree. But this involves $\delta$, not just $m$.

For a $d$-regular graph, $\delta = d$, so the bound would be $\frac{e}{n} - \frac{m}{2n} \cdot \frac{(n-1)d}{n} = \frac{dm}{2n} - \frac{m(n-1)d}{2n^2} = \frac{dm}{2n^2}$. For $d = kn$: $\frac{knm}{2n^2} = \frac{km}{2n}$. Per vertex: $\frac{k}{2n}$.

For $n=4, k=3$: $3/8 = 0.375$. That's way below $15/13 \approx 1.154$. So this can't be right (it would say we can always achieve 0.375m mono edges, but $K_{13}$ requires 15 mono edges = $15/13 \cdot 13 \approx 1.154 \cdot 13$).

So that formula is wrong. Let me think again.

OK let me take a step back. I was getting confused with various formulas. Let me think about this more carefully.

The key question is: what is the correct upper bound on the minimum number of monochromatic edges in an $n$-coloring of a graph with $e$ edges and $m$ vertices?

For $n = 2$, Edwards' bound is: mono $\leq \frac{e}{2} - \frac{m-1}{4}$, and this is tight for $K_{2k+1}$ (odd complete graphs).

For general $n$, I need to find the correct bound.

Let me think about what bound would be tight for $K_{kn+1}$ with $n$ colors.

For $K_{kn+1}$: $e = \binom{kn+1}{2}$, $m = kn+1$, min mono = $\frac{k(kn-n+2)}{2}$.

So the bound should give $\frac{k(kn-n+2)}{2}$ when evaluated at $K_{kn+1}$.

$\frac{e}{n} = \frac{kn(kn+1)}{2n} = \frac{k(kn+1)}{2}$.

We need: $\frac{k(kn+1)}{2} - f(m, n) = \frac{k(kn-n+2)}{2}$.

So $f(m, n) = \frac{k(kn+1)}{2} - \frac{k(kn-n+2)}{2} = \frac{k}{2}[(kn+1) - (kn-n+2)] = \frac{k}{2}[n-1] = \frac{k(n-1)}{2}$.

With $m = kn+1$: $f(kn+1, n) = \frac{k(n-1)}{2}$.

If $f(m, n) = \frac{(n-1)(m-1)}{2n}$, then $f(kn+1, n) = \frac{(n-1) \cdot kn}{2n} = \frac{k(n-1)}{2}$. ✓

So the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ gives the right value for $K_{kn+1}$. But is it valid for all graphs?

Let me check with a specific non-complete graph. Take $C_5$ (5-cycle, 2-regular) with $n=2$: $e=5, m=5$. Bound: $5/2 - 4/4 = 2.5 - 1 = 1.5$. Actual min mono: max cut of $C_5$ is 4, so mono = 1. $1 \leq 1.5$. ✓ (bound is valid but not tight).

Take $C_4$ with $n=2$: $e=4, m=4$. Bound: $2 - 3/4 = 1.25$. Actual: max cut = 4, mono = 0. $0 \leq 1.25$. ✓

Take $K_{3,3}$ (3-regular, 6 vertices) with $n=2$: $e=9, m=6$. Bound: $9/2 - 5/4 = 4.5 - 1.25 = 3.25$. Actual: $K_{3,3}$ is bipartite, so max cut = 9, mono = 0. $0 \leq 3.25$. ✓

Take $K_6$ (5-regular, 6 vertices) with $n=3$: $e=15, m=6$. Bound: $15/3 - 2 \cdot 5/6 = 5 - 5/3 = 10/3 \approx 3.33$. Actual: balanced partition $2,2,2$, mono = $3 \cdot 1 = 3$. $3 \leq 10/3$. ✓

Take $K_7$ (6-regular, 7 vertices) with $n=3$: $e=21, m=7$. Bound: $21/3 - 2 \cdot 6/6 = 7 - 2 = 5$. Actual: partition $3,2,2$, mono = $3 + 1 + 1 = 5$. $5 \leq 5$. ✓ (tight!)

Take $K_8$ (7-regular, 8 vertices) with $n=4$: $e=28, m=8$. Bound: $28/4 - 3 \cdot 7/8 = 7 - 21/8 = 35/8 = 4.375$. Actual: partition $2,2,2,2$, mono = $4 \cdot 1 = 4$. $4 \leq 4.375$. ✓ (not tight, because $K_8$ is 7-regular, not $kn$-regular for $n=4$).

Hmm wait, $K_8$ is 7-regular. For $n=4$, we'd want $kn$-regular = $4k$-regular. $K_8$ is 7-regular, which is not a multiple of 4. So $K_8$ is not relevant for our problem.

Let me check $K_9$ (8-regular, 9 vertices) with $n=4, k=2$: $e=36, m=9$. Bound: $36/4 - 3 \cdot 8/8 = 9 - 3 = 6$. Actual: partition $3,2,2,2$, mono = $3 + 1 + 1 + 1 = 6$. $6 \leq 6$. ✓ (tight!)

Great, so the bound is tight for $K_{kn+1}$ with $n$ colors.

Now, the crucial question: is the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ valid for ALL graphs?

Let me try to prove it by induction, more carefully.

Claim: For any graph $G$ with $m$ vertices and $e$ edges, there's an $n$-coloring with at most $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ mono edges.

Proof attempt by induction on $m$:

Base: $m = 1$. $e = 0$. Bound: $0$. ✓

Inductive step: Let $v$ be a vertex of $G$ with degree $d$. By induction, $G - v$ has an $n$-coloring with at most $\frac{e-d}{n} - \frac{(n-1)(m-2)}{2n}$ mono edges. Add $v$ to the color class minimizing new mono edges. New mono edges $\leq d/n$ (by averaging). Total: $\frac{e-d}{n} - \frac{(n-1)(m-2)}{2n} + \frac{d}{n} = \frac{e}{n} - \frac{(n-1)(m-2)}{2n}$.

We want: $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$. The gap is $\frac{(n-1)(m-1) - (n-1)(m-2)}{2n} = \frac{n-1}{2n}$.

So the simple induction gives a bound that's $\frac{n-1}{2n}$ too weak. We need to save an extra $\frac{n-1}{2n}$ when adding $v$.

For $n = 2$, Edwards' proof handles this by choosing $v$ carefully (a vertex of minimum degree) and using the fact that the saving from choosing the better color class is at least $\frac{|d_1 - d_2|}{2} \geq \frac{1}{2}$ (since $d_1 + d_2 = d$ and $d_1, d_2$ are integers, $|d_1 - d_2| \geq 1$ when $d$ is odd, or $\geq 0$ when $d$ is even). Actually, Edwards' proof is more subtle.

Hmm, let me think about this differently. Maybe the bound isn't $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ for all graphs, but only for certain graphs (like regular graphs or complete graphs).

Actually, let me reconsider. Maybe the correct bound for general $n$-colorings is different from what I conjectured.

Let me look at this from the perspective of what's known in the literature.

The Edwards bound for $n=2$ is: max cut $\geq \frac{e}{2} + \frac{m-1}{4}$. This is equivalent to: mono $\leq \frac{e}{2} - \frac{m-1}{4}$.

For general $n$, there's a result by Bollobás and Scott (2004), "Judicious partitions of graphs" and related work. Also, there's a result by Edwards himself for $n$-colorings.

Actually, I think the correct generalization is:

For any graph with $e$ edges and $m$ vertices, there's an $n$-coloring with at most $\frac{e}{n} - \frac{m-1}{2n}$ mono edges.

For $n = 2$: $\frac{e}{2} - \frac{m-1}{4}$. ✓ Matches Edwards.

For $K_{13}$ with $n=4$: $\frac{78}{4} - \frac{12}{8} = 19.5 - 1.5 = 18$. But actual is 15. So the bound is 18, not tight.

Hmm, so this bound is valid but not tight for $K_{kn+1}$ when $n > 2$.

But then the question is: is there a graph where the bound $\frac{e}{n} - \frac{m-1}{2n}$ is tight? If so, that graph would be the worst case, not $K_{kn+1}$.

For a $kn$-regular graph on $m$ vertices: bound per vertex = $\frac{k}{2} - \frac{m-1}{2nm} \to \frac{k}{2} - \frac{1}{2n}$ as $m \to \infty$.

For $n=4, k=3$: $\frac{3}{2} - \frac{1}{8} = \frac{11}{8} = 1.375$.

Is there a 12-regular graph where every 4-coloring has at least $\frac{11}{8}m$ mono edges (asymptotically)?

Hmm, I think the bound $\frac{e}{n} - \frac{m-1}{2n}$ might not be tight for $n > 2$. Let me think about what the tight bound is.

Actually, let me reconsider. For $n = 2$, the Edwards bound is tight for $K_{2k+1}$ (odd complete graphs). For $n > 2$, what graph is the extremal case?

Let me think about this more carefully. For $n$-coloring, the problem is to partition vertices into $n$ classes minimizing the total number of intra-class edges.

For $n = 2$, the worst case is $K_{2k+1}$ (odd complete graph), which is $2k$-regular.

For general $n$, is the worst case $K_{kn+1}$ (complete graph on $kn+1$ vertices, which is $kn$-regular)?

For $K_{kn+1}$ with $n$ colors, the min mono is $\frac{k(kn-n+2)}{2}$, and per vertex it's $\frac{k(kn-n+2)}{2(kn+1)}$.

For $n = 2$: $\frac{k(2k - 2 + 2)}{2(2k+1)} = \frac{k \cdot 2k}{2(2k+1)} = \frac{k^2}{2k+1}$. And the Edwards bound per vertex for $K_{2k+1}$ is $\frac{e/2 - (m-1)/4}{m} = \frac{k(2k+1)/2 - k/2}{2k+1} = \frac{k^2}{2k+1}$. ✓ So they match for $n=2$.

For $n = 3, k = 2$: $K_7$, min mono = 5, per vertex = 5/7. Edwards bound ($n=3$): $\frac{e}{3} - \frac{m-1}{6} = \frac{21}{3} - \frac{6}{6} = 7 - 1 = 6$. So bound is 6, actual is 5. Not tight.

So for $n > 2$, the Edwards bound $\frac{e}{n} - \frac{m-1}{2n}$ is NOT tight for $K_{kn+1}$.

This means either:
1. The worst case is $K_{kn+1}$, and the correct bound is $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ (which is tight for $K_{kn+1}$), or
2. The worst case is some other graph, and the Edwards bound $\frac{e}{n} - \frac{m-1}{2n}$ is the correct one (tight for some other graph).

I need to determine which is correct.

Let me think about whether the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is valid for all graphs.

Check: $C_5$ with $n=3$: $e=5, m=5$. Bound: $5/3 - 2 \cdot 4/6 = 5/3 - 4/3 = 1/3$. Actual: $C_5$ with 3 colors, we can properly 3-color it (since $\chi(C_5) = 3$), so mono = 0. $0 \leq 1/3$. ✓

Check: $K_4$ with $n=3$: $e=6, m=4$. Bound: $6/3 - 2 \cdot 3/6 = 2 - 1 = 1$. Actual: partition $2,1,1$, mono = 1. $1 \leq 1$. ✓ (tight!)

Check: $K_5$ with $n=3$: $e=10, m=5$. Bound: $10/3 - 2 \cdot 4/6 = 10/3 - 4/3 = 2$. Actual: partition $2,2,1$, mono = $1 + 1 + 0 = 2$. $2 \leq 2$. ✓ (tight!)

Check: $K_6$ with $n=3$: $e=15, m=6$. Bound: $15/3 - 2 \cdot 5/6 = 5 - 5/3 = 10/3 \approx 3.33$. Actual: partition $2,2,2$, mono = 3. $3 \leq 10/3$. ✓ (not tight, because $K_6$ is 5-regular, not $kn$-regular for $n=3$).

Check: $K_7$ with $n=3$: $e=21, m=7$. Bound: $21/3 - 2 \cdot 6/6 = 7 - 2 = 5$. Actual: 5. ✓ (tight!)

Check: $K_8$ with $n=3$: $e=28, m=8$. Bound: $28/3 - 2 \cdot 7/6 = 28/3 - 7/3 = 7$. Actual: partition $3,3,2$, mono = $3 + 3 + 1 = 7$. $7 \leq 7$. ✓ (tight!)

Interesting! $K_8$ with $n=3$ is also tight. $K_8$ is 7-regular, not $3k$-regular. So the bound is tight for $K_m$ with $n$ colors whenever $m \not\equiv 0 \pmod{n}$... let me check.

For $K_m$ with $n$ colors, the min mono is: partition into classes of size $\lfloor m/n \rfloor$ and $\lceil m/n \rceil$. If $m = qn + r$ with $0 \leq r < n$, then $r$ classes of size $q+1$ and $n-r$ classes of size $q$. Mono = $r\binom{q+1}{2} + (n-r)\binom{q}{2} = \frac{r \cdot q(q+1) + (n-r) \cdot q(q-1)}{2} = \frac{q}{2}[r(q+1) + (n-r)(q-1)] = \frac{q}{2}[rq + r + nq - n - rq + r] = \frac{q}{2}[nq - n + 2r] = \frac{q(nq - n + 2r)}{2}$.

Bound: $\frac{e}{n} - \frac{(n-1)(m-1)}{2n} = \frac{m(m-1)}{2n} - \frac{(n-1)(m-1)}{2n} = \frac{(m-1)(m - n + 1)}{2n}$.

With $m = qn + r$: $\frac{(qn+r-1)(qn+r-n+1)}{2n} = \frac{(qn+r-1)(qn+r-n+1)}{2n}$.

Actual: $\frac{q(nq - n + 2r)}{2} = \frac{q(n(q-1) + 2r)}{2} = \frac{nq(q-1) + 2qr}{2} = \frac{nq^2 - nq + 2qr}{2}$.

Bound: $\frac{(qn+r-1)(qn+r-n+1)}{2n}$. Let me expand: $qn+r-1 = nq + r - 1$ and $qn+r-n+1 = n(q-1) + r + 1$. Product: $(nq + r - 1)(n(q-1) + r + 1) = n^2 q(q-1) + nq(r+1) + n(q-1)(r-1) + (r-1)(r+1) = n^2 q(q-1) + nq(r+1) + n(q-1)(r-1) + r^2 - 1$.

$= n^2 q(q-1) + n[q(r+1) + (q-1)(r-1)] + r^2 - 1$
$= n^2 q(q-1) + n[qr + q + qr - q - r + 1] + r^2 - 1$
$= n^2 q(q-1) + n[2qr - r + 1] + r^2 - 1$
$= n^2 q(q-1) + 2nqr - nr + n + r^2 - 1$

Divided by $2n$: $\frac{nq(q-1)}{2} + qr - \frac{r}{2} + \frac{1}{2} + \frac{r^2 - 1}{2n}$.

$= \frac{nq^2 - nq}{2} + qr - \frac{r}{2} + \frac{1}{2} + \frac{r^2 - 1}{2n}$.

Actual: $\frac{nq^2 - nq + 2qr}{2} = \frac{nq^2 - nq}{2} + qr$.

Difference (bound - actual): $-\frac{r}{2} + \frac{1}{2} + \frac{r^2 - 1}{2n} = \frac{1 - r}{2} + \frac{r^2 - 1}{2n} = \frac{(1-r)}{2} + \frac{(r-1)(r+1)}{2n} = \frac{(1-r)}{2}\left[1 - \frac{r+1}{n}\right] = \frac{(1-r)(n - r - 1)}{2n}$.

For $r = 0$: $\frac{1 \cdot (n-1)}{2n} = \frac{n-1}{2n} > 0$. So bound > actual (not tight).
For $r = 1$: $\frac{0 \cdot (n-2)}{2n} = 0$. So bound = actual (tight!).
For $r > 1$: $(1-r) < 0$ and $(n - r - 1) \geq 0$ (since $r < n$), so difference $\leq 0$. Bound < actual?? That would mean the bound is violated!

Wait, that can't be right. Let me recheck with a specific example.

$K_9$ with $n=4$: $m=9, q=2, r=1$. Actual: $\frac{2(4 \cdot 2 - 4 + 2)}{2} = \frac{2 \cdot 6}{2} = 6$. Bound: $\frac{8 \cdot 6}{8} = 6$. ✓ (tight, $r=1$).

$K_{10}$ with $n=4$: $m=10, q=2, r=2$. Actual: $\frac{2(8 - 4 + 4)}{2} = \frac{2 \cdot 8}{2} = 8$. Bound: $\frac{9 \cdot 7}{8} = \frac{63}{8} = 7.875$. So bound = 7.875 < actual = 8. The bound is violated!

So the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is NOT valid for all graphs! It fails for $K_{10}$ with $n=4$.

This means my conjectured bound is wrong. Let me reconsider.

So for $K_{10}$ with $n=4$: the minimum mono edges is 8 (partition $3,3,2,2$: mono = $3+3+1+1=8$). The bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n} = \frac{45}{4} - \frac{3 \cdot 9}{8} = 11.25 - 3.375 = 7.875 < 8$. So the bound says there should be a coloring with at most 7.875 mono edges, but the actual minimum is 8. Contradiction!

So the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is NOT valid in general. It's only valid for certain graphs (like $K_{kn+1}$ where $r=1$).

OK so I need to rethink. The Edwards bound $\frac{e}{n} - \frac{m-1}{2n}$ is valid (I'll assume this is proven), and it gives 18 for $K_{13}$ with $n=4$, while actual is 15. So the Edwards bound is not tight for $K_{kn+1}$ when $n > 2$.

Now, the question is: what is the actual worst case? Is it $K_{kn+1}$ (giving $15/13$ per vertex for $n=4, k=3$), or is there a graph that's worse?

Let me think about $K_{10}$ with $n=4$. $K_{10}$ is 9-regular, not 12-regular. So it's not relevant for our problem ($n=4, k=3$ requires 12-regular graphs).

For 12-regular graphs, the smallest is $K_{13}$ (13 vertices). The next possible sizes are $m = 14, 15, \ldots$ (any $m \geq 13$ with $12m$ even, which is all $m \geq 13$).

Let me think about whether there's a 12-regular graph on $m > 13$ vertices that has a higher min-mono-per-vertex ratio than $K_{13}$.

For $K_{13}$: ratio = $15/13 \approx 1.1538$.

Let me consider $m = 14$. A 12-regular graph on 14 vertices. The complement is a 1-regular graph on 14 vertices (perfect matching). So $G = K_{14} - M$.

Min mono for $K_{14}$ with 4 colors: partition $4,4,3,3$, mono = $6+6+3+3 = 18$. But we subtract the matching edges within each class. With 7 matching edges, we can place at most 6 within classes (2 in each size-4 class, 1 in each size-3 class). So min mono $\leq 18 - 6 = 12$. Per vertex: $12/14 = 6/7 \approx 0.857$. Much less than $15/13$.

What about $m = 26$? Two copies of $K_{13}$. Min mono = $2 \times 15 = 30$. Per vertex: $30/26 = 15/13$. Same as $K_{13}$.

What about a 12-regular graph on 26 vertices that's not two copies of $K_{13}$? For example, take $K_{26}$ and remove a 13-regular graph. The complement would be 13-regular. 

Actually, let me think about this differently. For a 12-regular graph on $m$ vertices, the min mono per vertex is at most $\frac{k}{2} - \frac{m-1}{2nm}$ (from the Edwards bound). For $n=4, k=3$: $\frac{3}{2} - \frac{m-1}{8m}$. As $m \to \infty$, this approaches $3/2 - 1/8 = 11/8 = 1.375$.

But is the Edwards bound tight? Is there a 12-regular graph where the min mono per vertex approaches $11/8$?

For $n = 2$, the Edwards bound is tight for $K_{2k+1}$ (and disjoint unions). For $n > 2$, I need to think about what graph makes it tight.

Actually, wait. For $n = 2$, the Edwards bound is $\frac{e}{2} - \frac{m-1}{4}$. For $K_{2k+1}$: $\frac{k(2k+1)}{2} - \frac{2k}{4} = \frac{k(2k+1)}{2} - \frac{k}{2} = \frac{k \cdot 2k}{2} = k^2$. And actual is $k^2$. So tight. ✓

For $n = 3$, the Edwards bound is $\frac{e}{3} - \frac{m-1}{6}$. For $K_7$ ($k=2$): $\frac{21}{3} - \frac{6}{6} = 7 - 1 = 6$. Actual is 5. Not tight.

So for $n = 3$, the Edwards bound is not tight for $K_7$. Is it tight for some other graph?

Hmm, let me think about what graph would make the Edwards bound tight for $n = 3$.

For the Edwards bound $\frac{e}{n} - \frac{m-1}{2n}$ to be tight, we need a graph where the min mono equals this value.

For $n = 3$, consider a graph that's a disjoint union of $K_3$'s... no, $K_3$ is 2-regular, not $3k$-regular.

Let me think about this differently. For $n = 2$, the Edwards bound is tight for odd complete graphs. The key property is that $K_{2k+1}$ has chromatic number $2k+1$, which is odd, so it can't be properly 2-colored.

For $n = 3$, what graph has the property that every 3-coloring has many mono edges?

Consider $K_{3k+1}$ (which is $3k$-regular). For $k=2$: $K_7$, min mono = 5, Edwards bound = 6. Not tight.

What about a different graph? Let me think about the Petersen graph or some other specific graph.

Actually, let me think about this more carefully. The Edwards bound for $n$-colorings might not be $\frac{e}{n} - \frac{m-1}{2n}$. Let me look for the correct generalization.

I recall now that the correct generalization of Edwards' bound to $n$-colorings is:

For any graph with $e$ edges and $m$ vertices, there's an $n$-coloring with at most $\frac{e}{n} - \frac{m-1}{2n}$ monochromatic edges.

And this is proven by induction on $n$ (not $m$). The idea is: first find a good 2-coloring (using Edwards' bound), then recursively color each part with $n/2$ colors.

But this only works for $n$ a power of 2. For general $n$, the approach is different.

Actually, I think the correct statement might be:

For any graph with $e$ edges and $m$ vertices, there's an $n$-coloring with at most $\frac{e}{n} - \frac{(n-1)(m-1)}{2n^2}$ monochromatic edges.

Let me check: for $n=2$: $\frac{e}{2} - \frac{(m-1)}{8}$. But Edwards gives $\frac{e}{2} - \frac{m-1}{4}$. So this is weaker. Not the right generalization.

Hmm, let me try another approach. Let me look at the proof of Edwards' theorem and see how it generalizes.

Edwards' theorem ($n=2$): Every graph with $e$ edges and $m$ vertices has a cut of size at least $\frac{e}{2} + \frac{m-1}{4}$.

Proof sketch: By induction on $m$. If $G$ has a vertex $v$ of even degree, remove it, find a good cut of $G-v$, then add $v$ to the side with fewer neighbors. The saving is $d(v)/2$ compared to random, and the induction gives $\frac{e-d(v)}{2} + \frac{m-2}{4}$, so total cut $\geq \frac{e-d(v)}{2} + \frac{m-2}{4} + \frac{d(v)}{2} = \frac{e}{2} + \frac{m-2}{4}$. We need $\frac{m-1}{4}$, so we're short by $\frac{1}{4}$.

If all vertices have odd degree, then $m$ is even (since $\sum d(v) = 2e$ is even, and all $d(v)$ are odd, so $m$ must be even). In this case, we can find a vertex $v$ such that removing it and using a more careful argument gives the extra $\frac{1}{4}$.

Actually, the proof is more subtle. Let me not try to reconstruct it and instead think about the problem from a higher level.

The key question is: for $kn$-regular graphs with $n$-coloring, what is $c(n,k) = \sup_G \min_{\text{coloring}} \frac{\text{mono}}{m}$?

I've established:
1. $K_{kn+1}$ gives a lower bound of $\frac{k(kn-n+2)}{2(kn+1)}$.
2. The Edwards bound (if valid for $n$-colorings) gives an upper bound of $\frac{k}{2} - \frac{m-1}{2nm}$, which is maximized at $m = kn+1$ giving $\frac{k}{2} - \frac{kn}{2n(kn+1)} = \frac{k}{2} - \frac{k}{2(kn+1)} = \frac{k(kn+1) - k}{2(kn+1)} = \frac{k \cdot kn}{2(kn+1)} = \frac{k^2 n}{2(kn+1)}$.

Wait, let me recompute. For $m = kn+1$:
$\frac{k}{2} - \frac{kn}{2n(kn+1)} = \frac{k}{2} - \frac{k}{2(kn+1)} = \frac{k(kn+1) - k}{2(kn+1)} = \frac{k^2 n}{2(kn+1)}$.

For $n=4, k=3$: $\frac{9 \cdot 4}{2 \cdot 13} = \frac{36}{26} = \frac{18}{13} \approx 1.385$.

But the actual value for $K_{13}$ is $15/13 \approx 1.154$. So the Edwards bound gives $18/13$, which is higher than the actual $15/13$. This means the Edwards bound is not tight for $K_{13}$ with $n=4$.

So the question remains: is there a 12-regular graph where the min mono per vertex is higher than $15/13$?

Let me think about this more carefully. The Edwards bound for $n$-colorings gives an upper bound of $\frac{k^2 n}{2(kn+1)}$ for $m = kn+1$. But the actual value for $K_{kn+1}$ is $\frac{k(kn-n+2)}{2(kn+1)}$. The gap is:

$\frac{k^2 n}{2(kn+1)} - \frac{k(kn-n+2)}{2(kn+1)} = \frac{k(kn - kn + n - 2)}{2(kn+1)} = \frac{k(n-2)}{2(kn+1)}$.

For $n = 2$: gap = 0. So the Edwards bound is tight for $n=2$. ✓
For $n > 2$: gap > 0. So the Edwards bound is not tight for $K_{kn+1}$.

This means either:
(a) The Edwards bound is not the correct upper bound for $n$-colorings (maybe the correct bound is tighter), or
(b) There exists a graph (not $K_{kn+1}$) where the min mono per vertex is higher than $15/13$ and approaches the Edwards bound.

Let me think about (b). Is there a 12-regular graph on $m$ vertices where the min mono per vertex is close to $\frac{3}{2} - \frac{1}{8} = \frac{11}{8} = 1.375$?

For large $m$, a random 12-regular graph is likely 4-colorable (since the chromatic number of a random $d$-regular graph is roughly $d/(2\ln d)$, which for $d=12$ is about $12/(2 \cdot 2.48) \approx 2.4$, so likely 3 or 4-colorable). If 4-colorable, min mono = 0.

But we need the worst case, not random graphs. Let me think about specific constructions.

What about a graph that's a "complete multipartite" type or has high chromatic number?

For a 12-regular graph, the chromatic number is at most 13 (by Brooks' theorem, at most 12 unless it's $K_{13}$ or an odd cycle). So the graph could have chromatic number up to 13, but we're coloring with only 4 colors.

Hmm, let me think about the Kneser graph or some other specific graph.

Actually, let me think about this problem differently. Let me consider the "fractional" version more carefully.

For a $d$-regular graph $G$, the minimum number of mon        — AI历史解题过程（thinking）
#   polymath_00177         — 题目ID

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
  <problem_id>polymath_00177</problem_id>
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

Given positive integers $n, k$ with $n \ge 2$, let $c(n, k)$ be the minimum constant such that for any positive integer $m$ and any $kn$-regular graph $G$ with $m$ vertices, there exists a coloring of the vertices of $G$ with $n$ colors such that the number of monochromatic edges is at most $c(n, k)m$.
Calculate the value of $100 \times c(4, 3)$.

## Standard Solution

The original solution derives the formula $c(n, k) = \frac{n \binom{k}{2} + k}{nk+1}$. 
For $n=4$ and $k=3$:
$\binom{k}{2} = \binom{3}{2} = 3$.
$c(4, 3) = \frac{4(3) + 3}{4(3) + 1} = \frac{12 + 3}{12 + 1} = \frac{15}{13}$.
The problem asks for $100 \times c(4, 3) = 100 \times \frac{15}{13} = \frac{1500}{13}$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have positive integers $n, k$ with $n \ge 2$. $c(n, k)$ is the minimum constant such that for any positive integer $m$ and any $kn$-regular graph $G$ with $m$ vertices, there exists a coloring of the vertices of $G$ with $n$ colors such that the number of monochromatic edges is at most $c(n, k) m$.

We need to calculate $100 \times c(4, 3)$.

So $n = 4$, $k = 3$, and we're looking at $kn = 12$-regular graphs, coloring with 4 colors, minimizing the maximum number of monochromatic edges (normalized by $m$).

Let me think about this. A $12$-regular graph on $m$ vertices has $6m$ edges. We color with 4 colors and want to minimize monochromatic edges.

For a random coloring with 4 colors, each edge is monochromatic with probability $1/4$, so expected monochromatic edges = $6m/4 = 1.5m$. But we can do better with a good coloring.

Let me think about what the optimal constant is.

For a $d$-regular graph colored with $n$ colors, the question is: what's the minimum (over colorings) of the maximum (over graphs) of the fraction of monochromatic edges?

Actually, let me think about this more carefully. We want:
$$c(n, k) = \sup_{G \text{ kn-regular}} \min_{\text{colorings}} \frac{\text{mono edges}}{m}$$

For a $d$-regular graph with $m$ vertices, total edges = $dm/2$. With $n$ colors, if we have a balanced coloring where each color class has $m/n$ vertices, the number of edges within color classes... 

Let me think about the worst case. Consider a complete graph $K_{d+1}$ which is $d$-regular. For $d = 12$, $K_{13}$ is 12-regular with 13 vertices. 

For $K_{13}$ colored with 4 colors, to minimize monochromatic edges, we want to balance the color classes. With 13 vertices and 4 colors, the most balanced partition is $4, 3, 3, 3$. The number of monochromatic edges is $\binom{4}{2} + 3\binom{3}{2} = 6 + 9 = 15$. So mono edges / $m$ = $15/13$.

But wait, is this the worst case? Let me think more generally.

Actually, let me think about this differently. The key insight is about what graph maximizes the minimum number of monochromatic edges.

For a $d$-regular graph, consider the "defect" or the structure that forces many monochromatic edges.

Let me think about the problem from the perspective of the probabilistic method and extremal cases.

For a $d$-regular graph on $m$ vertices with a proper $n$-coloring, we'd have 0 monochromatic edges. But not all $d$-regular graphs are $n$-colorable. The question is about the worst case over all $kn$-regular graphs.

Let me think about specific constructions. 

Consider a disjoint union of cliques $K_{kn+1}$. Each $K_{kn+1}$ is $kn$-regular. For $n=4, k=3$, these are $K_{13}$'s. As computed, with optimal coloring $4,3,3,3$, we get $15$ monochromatic edges per clique, so $15/13$ per vertex.

But can we do worse? Let me think about other constructions.

Actually, let me think about the problem more carefully. The question is asking for the supremum over all $kn$-regular graphs of the minimum fraction of monochromatic edges.

Let me consider a different approach. Think about a graph that is a disjoint union of copies of $K_{n,n}$ or some bipartite-like structure... no, those would be properly 2-colorable.

The worst case for coloring is when the graph is "far from" being properly colorable. Complete graphs are the natural candidate.

Let me think about whether $K_{kn+1}$ is indeed the worst case, or if there's something worse.

For a $d$-regular graph, the number of monochromatic edges in a coloring is:
$$\sum_{i=1}^{n} e_i$$
where $e_i$ is the number of edges within color class $i$.

If color class $i$ has $s_i$ vertices, then $e_i \leq \binom{s_i}{2}$ (with equality for a clique). But in a $d$-regular graph, the maximum number of edges within a set of $s_i$ vertices is limited.

Hmm, let me think about this differently using a known result.

Actually, I recall that for this type of problem, the answer relates to the concept of "judicious partitions" or the Edwards-Erdős type results.

Let me think about it from the perspective of the following: for a $d$-regular graph, what's the minimum number of monochromatic edges in an $n$-coloring?

There's a classical result that says: every graph with $e$ edges has an $n$-coloring with at most $\frac{e}{n} - \frac{m}{2}\frac{n-1}{n} \cdot \frac{d_{\min}}{...}$... hmm, I don't remember the exact formula.

Let me think about it more carefully from first principles.

For a $d$-regular graph on $m$ vertices with $e = dm/2$ edges, and an $n$-coloring:

The number of monochromatic edges = $e - $ (number of properly colored edges).

We want to maximize properly colored edges, i.e., maximize the number of edges going between different color classes.

If the color classes have sizes $s_1, \ldots, s_n$ with $\sum s_i = m$, then the maximum number of edges between different classes is at most $\sum_{i<j} s_i s_j = \frac{m^2 - \sum s_i^2}{2}$, but this is only achievable if the graph is complete. For a $d$-regular graph, the number of edges is $dm/2$, so the number of properly colored edges is at most $dm/2$ (trivially), and the number of monochromatic edges is at least $0$.

But we want the worst case over graphs. So we want a graph where every coloring has many monochromatic edges.

Let me think about the complete graph $K_{kn+1}$ again. It's $kn$-regular. With $n$ colors and $kn+1$ vertices, the most balanced coloring has classes of size $k+1, k, k, \ldots, k$ (one class of size $k+1$ and $n-1$ classes of size $k$). Wait, $kn + 1 = (k+1) + (n-1)k$, so yes, one class of size $k+1$ and $n-1$ classes of size $k$.

Monochromatic edges = $\binom{k+1}{2} + (n-1)\binom{k}{2} = \frac{k(k+1)}{2} + \frac{(n-1)k(k-1)}{2} = \frac{k}{2}[(k+1) + (n-1)(k-1)] = \frac{k}{2}[k+1 + nk - n - k + 1] = \frac{k}{2}[nk - n + 2] = \frac{k(nk - n + 2)}{2}$.

Per vertex: $\frac{k(nk - n + 2)}{2(kn+1)}$.

For $n=4, k=3$: $\frac{3(12 - 4 + 2)}{2 \cdot 13} = \frac{3 \cdot 10}{26} = \frac{30}{26} = \frac{15}{13}$.

So $c(4,3) \geq 15/13$.

Now, is this the worst case? Or can we find a graph that does worse?

Let me think about other constructions. What about a disjoint union of $K_{kn+1}$'s? That gives the same ratio, $15/13$.

What about other graphs? Let me think about whether we can do worse.

Consider a graph that is a "blow-up" or some other construction. 

Actually, let me think about this more carefully. The question is whether $K_{kn+1}$ (or disjoint unions of it) is the extremal graph.

Let me consider a different type of graph. What about a graph where the chromatic number is high?

For a $d$-regular graph with $d = kn$, the chromatic number is at most $kn + 1$ (by Brooks' theorem, it's at most $kn$ unless the graph is $K_{kn+1}$ or an odd cycle). So most $kn$-regular graphs are $kn$-colorable, but we're coloring with only $n$ colors.

Hmm, let me think about this problem differently. 

Actually, I think the key question is: what is the maximum, over all $kn$-regular graphs $G$ on $m$ vertices, of the minimum number of monochromatic edges in an $n$-coloring, divided by $m$?

Let me think about lower bounds more carefully.

For $K_{kn+1}$: we showed the ratio is $\frac{k(nk-n+2)}{2(kn+1)}$.

Let me consider another construction. Take a complete $n$-partite graph where each part has size $k$, i.e., $K_{k,k,\ldots,k}$ ($n$ parts of size $k$). This graph has $nk$ vertices and is $(n-1)k$-regular. That's not $kn$-regular. 

What about $K_{k+1, k+1, \ldots}$? No, let me think differently.

What about the complete graph $K_{kn+1}$? This seems like the natural extremal case because it's the "most connected" $kn$-regular graph.

But let me think about whether there's a graph that forces even more monochromatic edges.

Consider the following: take $n$ cliques of size $k+1$, and connect them in some way to make the graph $kn$-regular. Each clique $K_{k+1}$ has $k+1$ vertices, each of degree $k$. To make it $kn$-regular, each vertex needs $kn - k = k(n-1)$ more edges going outside its clique. 

If we have $n$ cliques of size $k+1$, total vertices = $n(k+1)$. Each vertex in clique $i$ needs $k(n-1)$ edges to other cliques. The number of edges between different cliques: each clique has $k+1$ vertices, each needing $k(n-1)$ external edges, so total external degree = $n(k+1)k(n-1)$, and external edges = $n(k+1)k(n-1)/2$. The number of pairs of cliques is $\binom{n}{2}$, and between each pair we can have at most $(k+1)^2$ edges. So we need $n(k+1)k(n-1)/2 \leq \binom{n}{2}(k+1)^2 = \frac{n(n-1)(k+1)^2}{2}$, which gives $k \leq k+1$, always true. So this is feasible.

But actually, let me think about whether this construction forces more monochromatic edges.

If we color this graph with $n$ colors, and we want to minimize monochromatic edges... Each clique $K_{k+1}$ needs to be colored. If we use a different color for each clique, then within each clique, all $k+1$ vertices have the same color, giving $\binom{k+1}{2}$ monochromatic edges per clique, total $n\binom{k+1}{2}$. 

But we could also distribute colors within cliques. The optimal coloring would balance things.

Hmm, this is getting complicated. Let me think about whether the answer is indeed $15/13$.

$100 \times 15/13 = 1500/13 \approx 115.38...$. That doesn't seem like a clean answer. Let me reconsider.

Maybe the answer isn't from the complete graph. Let me think about other approaches.

Actually, wait. Let me reconsider the problem. The problem says "for any positive integer $m$ and any $kn$-regular graph $G$ with $m$ vertices." So $c(n,k)$ must work for ALL $m$ and ALL $kn$-regular graphs. The constant $c(n,k)$ is the minimum such constant.

So $c(n,k) = \sup_{m, G} \min_{\text{coloring}} \frac{\text{mono}(G, \text{coloring})}{m}$.

For $K_{13}$ (which is 12-regular, $m=13$), the minimum mono edges is 15, giving ratio $15/13$.

But maybe for other graphs with other values of $m$, the ratio is higher?

Let me think about $m = 2$. A 12-regular graph on 2 vertices would need each vertex to have degree 12, but the maximum degree in a 2-vertex graph is 1. So no 12-regular graph exists on 2 vertices. Similarly, for small $m$, 12-regular graphs might not exist.

A $d$-regular graph on $m$ vertices requires $m \geq d+1$ and $md$ even. For $d = 12$, we need $m \geq 13$ and $12m$ even (always true). So the smallest $m$ is 13, giving $K_{13}$.

For $m = 14$: a 12-regular graph on 14 vertices. The complement is a 1-regular graph on 14 vertices, which is a perfect matching. So $G = K_{14}$ minus a perfect matching. 

For this graph, with 4 colors and 14 vertices, the most balanced coloring is $4, 4, 3, 3$ (or $4, 4, 4, 2$, etc.). Let me compute the minimum monochromatic edges.

$G = K_{14} - M$ where $M$ is a perfect matching (7 edges). Total edges = $\binom{14}{2} - 7 = 91 - 7 = 84 = 12 \cdot 14 / 2$. ✓

For a coloring with class sizes $s_1, s_2, s_3, s_4$ summing to 14, the number of monochromatic edges is:
$$\sum_i \left[\binom{s_i}{2} - \text{(matching edges within class } i)\right]$$

To minimize this, we want to maximize the matching edges within each class (so they get subtracted) and minimize $\sum \binom{s_i}{2}$.

$\sum \binom{s_i}{2}$ is minimized when classes are balanced: $4, 4, 3, 3$ gives $6 + 6 + 3 + 3 = 18$.

Now, the matching edges within each class: we have 7 matching edges. We want to maximize how many of them fall within the same color class. 

With classes of size $4, 4, 3, 3$: a class of size 4 can contain at most 2 matching edges, a class of size 3 can contain at most 1. So maximum matching edges within classes = $2 + 2 + 1 + 1 = 6$. (We need to check if this is achievable.)

If we can place 6 of the 7 matching edges within color classes, then mono edges = $18 - 6 = 12$, ratio = $12/14 = 6/7 \approx 0.857$.

Compare with $K_{13}$: ratio $15/13 \approx 1.154$.

So $K_{13}$ gives a higher ratio. Good.

Let me check $m = 13$ more carefully. $K_{13}$ is the only 12-regular graph on 13 vertices. With 4 colors, balanced partition $4, 3, 3, 3$ gives $\binom{4}{2} + 3\binom{3}{2} = 6 + 9 = 15$ mono edges. Can we do better with an unbalanced partition? $5, 3, 3, 2$: $10 + 3 + 3 + 1 = 17$. Worse. $4, 4, 3, 2$: $6 + 6 + 3 + 1 = 16$. Worse. $7, 2, 2, 2$: $21 + 1 + 1 + 1 = 24$. Much worse. So $4, 3, 3, 3$ is optimal, giving 15.

So for $m = 13$, the ratio is $15/13$.

Now let me think about whether there's a graph on more vertices that gives a higher ratio.

Consider a disjoint union of $K_{13}$'s. If $m$ is a multiple of 13, say $m = 13t$, then the graph is $t$ copies of $K_{13}$. The optimal coloring colors each $K_{13}$ optimally, giving $15t$ mono edges, ratio $15t/(13t) = 15/13$. Same ratio.

What about other graphs? Let me think about whether we can construct a 12-regular graph where every 4-coloring has a higher ratio of monochromatic edges.

Hmm, let me think about this more carefully. The question is essentially about the "maximum over $d$-regular graphs of the minimum monochromatic edges in $n$-coloring."

I think the answer might be related to a theorem by Edwards or Bollobás and Scott about judicious partitions.

Actually, let me think about this from a different angle. There's a result that says:

For any graph $G$ with $m$ vertices and $e$ edges, there exists an $n$-coloring with at most $\frac{e}{n} - \frac{m}{2} \cdot \frac{n-1}{n^2} \cdot \delta$ monochromatic edges... no, I don't think that's right.

Let me think about the probabilistic argument. If we randomly color with $n$ colors, each edge is monochromatic with probability $1/n$. So expected mono edges = $e/n = dm/(2n)$. For $d = kn$, this is $knm/(2n) = km/2$. So $c(n,k) \leq k/2$ by the probabilistic method (there exists a coloring with at most $km/2$ mono edges).

For $n=4, k=3$: $c(4,3) \leq 3/2 = 1.5$.

But we also have the lower bound from $K_{13}$: $c(4,3) \geq 15/13 \approx 1.154$.

Can we improve the upper bound? The probabilistic method gives $k/2$, but maybe we can do better.

Actually, there's a well-known result that improves on the random coloring bound. Let me think...

For a $d$-regular graph, we can use the following approach: if the graph is $n$-colorable, we get 0 mono edges. If not, we need to understand the structure.

Actually, let me think about this problem differently. Let me consider the "fractional" version.

In the fractional version, we assign each vertex a probability distribution over colors. The expected number of monochromatic edges is $\sum_{(u,v) \in E} \sum_i p_{u,i} p_{v,i}$ where $p_{u,i}$ is the probability of vertex $u$ getting color $i$.

For a $d$-regular graph, if we use the uniform distribution ($p_{u,i} = 1/n$ for all $u, i$), we get $e/n = dm/(2n)$ mono edges.

But we can be smarter. If the graph is vertex-transitive, we might use the structure.

Hmm, let me think about whether the answer is exactly $15/13$ or something else.

Let me consider the problem from the perspective of the "max-cut" type results. For 2-coloring ($n=2$), the problem is about max cut. For a $d$-regular graph, the max cut is at least $dm/2 \cdot (1/2 + 1/(2d))$... no, that's not quite right either.

Actually, for $n=2$ (2-coloring), the problem becomes: for a $2k$-regular graph, find the minimum number of monochromatic edges. This is equivalent to maximizing the cut. By Edwards' theorem (or the result that every graph has a cut of size at least $m/4 + \sqrt{m/2 + 1/16}/4 - 1/8$...), or more simply, for a $d$-regular graph, the max cut is at least $dm/4 + m/4$ (I think this is a result by... let me think).

Actually, for $d$-regular graphs, there's a result that the max cut is at least $\frac{d}{2} \cdot \frac{m}{2} + \frac{m}{4}$... I'm not sure. Let me think about the $n=2$ case more carefully.

For $n=2, k$: $2k$-regular graph, 2-coloring. Max cut ≥ ? 

For $K_{2k+1}$ (which is $2k$-regular), the max cut with 2 colors: balanced partition $\lfloor (2k+1)/2 \rfloor, \lceil (2k+1)/2 \rceil = k, k+1$. Cut size = $k(k+1)$. Total edges = $\binom{2k+1}{2} = k(2k+1)$. Mono edges = $k(2k+1) - k(k+1) = k(2k+1 - k - 1) = k^2$. Per vertex: $k^2/(2k+1)$.

For $n=2, k=1$: $K_3$, 2-coloring. Mono = $1$, per vertex = $1/3$. And $c(2,1) = 1/3$? Let me check: $2$-regular graph, 2-coloring. $K_3$ is the worst case? For $C_5$ (2-regular), max cut = 4, mono = 1, per vertex = 1/5. For $K_3$, mono = 1, per vertex = 1/3. So yes, $K_3$ is worse. $c(2,1) = 1/3$.

For $n=2, k=2$: $4$-regular graph, 2-coloring. $K_5$: balanced $2,3$, mono = $\binom{2}{2} + \binom{3}{2} = 1 + 3 = 4$, per vertex = $4/5$. Is there a worse graph? 

Hmm, $100 \times c(2,1) = 100/3 \approx 33.33$. Not clean. $100 \times c(2,2) = 80$. That's clean!

Let me check $n=2, k=3$: $6$-regular, 2-coloring. $K_7$: balanced $3,4$, mono = $3 + 6 = 9$, per vertex = $9/7$. $100 \times 9/7 \approx 128.57$. Not clean.

Hmm, so the answers aren't always clean. Let me reconsider.

Wait, but the problem asks for $100 \times c(4,3)$. If $c(4,3) = 15/13$, then $100 \times 15/13 = 1500/13 \approx 115.38$. Not clean.

Let me reconsider whether $K_{13}$ is really the worst case, or if there's a different graph that gives a clean answer.

Let me think about this differently. Maybe the answer is $k/2 = 3/2$ (the probabilistic bound), giving $100 \times 3/2 = 150$. That's clean!

But is the probabilistic bound tight? Is there a graph where every 4-coloring has exactly $3m/2$ monochromatic edges?

For a random 12-regular graph, the expected mono edges in a random 4-coloring is $3m/2$. But we can do better than random coloring. So the probabilistic bound is an upper bound, and it might not be tight.

Hmm, but maybe for certain graphs, we can't do better than $3m/2$? That seems unlikely since we can always find a coloring at least as good as random.

Actually, the probabilistic method says there EXISTS a coloring with at most $3m/2$ mono edges. But maybe we can always find one with fewer. The question is what the worst case is.

Let me think about this more carefully. 

For a $d$-regular graph, there's a result by Bollobás and Scott (or maybe Edwards) about judicious partitions. Let me think about what's known.

For $n$-coloring of a graph with $e$ edges, the minimum number of monochromatic edges is at most:
$$\frac{e}{n} - \frac{m(n-1)}{2n^2} \cdot d_{\min}$$
... I'm not sure about this formula.

Actually, let me think about a simpler approach. For a $d$-regular graph, consider the following greedy/rounding approach:

1. Start with a fractional coloring (each vertex gets $1/n$ of each color).
2. Round to an integral coloring.

The fractional coloring gives $e/n$ mono edges. The rounding introduces some error.

Actually, let me think about the problem from the LP relaxation perspective. The minimum number of monochromatic edges in an $n$-coloring is related to the minimum over all partitions of $\sum_i e(S_i)$ where $S_1, \ldots, S_n$ is a partition of $V$ and $e(S_i)$ is the number of edges within $S_i$.

The fractional relaxation allows each vertex to be fractionally assigned. The fractional minimum is:
$$\min \sum_{(u,v) \in E} \sum_i x_{u,i} x_{v,i}$$
subject to $\sum_i x_{u,i} = 1$ for all $u$, $x_{u,i} \geq 0$.

For a $d$-regular graph, setting $x_{u,i} = 1/n$ gives $\sum_{(u,v)} \sum_i 1/n^2 = e/n = dm/(2n)$.

But can we do better fractionally? For a vertex-transitive graph, the uniform assignment is optimal by symmetry. For $K_{kn+1}$, the fractional optimum is $e/n = \binom{kn+1}{2}/n = \frac{kn(kn+1)}{2n} = \frac{k(kn+1)}{2}$. Per vertex: $\frac{k(kn+1)}{2(kn+1)} = k/2$.

So the fractional optimum for $K_{kn+1}$ is $k/2$ per vertex. But the integral optimum is $\frac{k(nk-n+2)}{2(kn+1)}$ per vertex (as computed).

For $n=4, k=3$: fractional = $3/2 = 1.5$, integral = $15/13 \approx 1.154$.

So the integrality gap is $15/13$ vs $3/2$. The integral optimum is better than the fractional one? That can't be right. The integral optimum should be at least as large as the fractional optimum.

Wait, I think I made an error. Let me recompute.

For $K_{13}$ with 4 colors:
- Fractional: each vertex gets $1/4$ of each color. Mono edges = $e \cdot (1/4)^2 \cdot 4 = e/4 = 78/4 = 19.5$. Wait, no. $\sum_{(u,v)} \sum_i x_{u,i} x_{v,i} = \sum_{(u,v)} \sum_i (1/4)^2 = e \cdot 4 \cdot (1/16) = e/4 = 78/4 = 19.5$. Per vertex: $19.5/13 = 1.5$.

- Integral (best): 15. Per vertex: $15/13 \approx 1.154$.

So the integral optimum (15) is LESS than the fractional optimum (19.5)? That's impossible! The fractional relaxation should give a lower bound on the integral optimum.

Oh wait, I think I have the direction wrong. The fractional relaxation gives a LOWER bound on the minimum integral solution. So the minimum integral mono edges ≥ minimum fractional mono edges. But 15 < 19.5, which contradicts this.

Let me recheck. The fractional assignment $x_{u,i} = 1/4$ gives 19.5 mono edges. But this is just ONE fractional assignment. The minimum over all fractional assignments could be lower.

For $K_{13}$, can we find a fractional assignment with fewer than 15 mono edges? 

Actually, for $K_n$, the minimum fractional $n$-coloring... hmm, let me think. For $K_{13}$ with 4 colors, the fractional relaxation allows splitting vertices. The minimum of $\sum_{(u,v)} \sum_i x_{u,i} x_{v,i}$ subject to $\sum_i x_{u,i} = 1$.

For $K_{13}$, by symmetry, the optimal fractional solution might not be uniform. Let me think...

Actually, for $K_n$ (complete graph), the minimum number of monochromatic edges in a fractional $k$-coloring is 0 if $k \geq n$ (just assign each vertex a distinct color). For $k < n$, we need to think.

For $K_{13}$ with 4 colors fractionally: we can assign 4 vertices to color 1, 3 to color 2, 3 to color 3, 3 to color 4 (integrally), giving 15. But fractionally, we could do better by splitting.

Actually, the fractional chromatic number of $K_{13}$ is 13, so we need at least 13 colors fractionally to get 0 mono edges. With 4 colors, the fractional minimum is... 

For $K_n$ with $k$ colors, the minimum fractional mono edges: by symmetry, the optimal is to assign each vertex uniformly, $x_{u,i} = 1/k$. This gives $e/k = \binom{n}{2}/k$ mono edges. But can we do better?

For $K_n$, any fractional coloring has $\sum_{(u,v)} \sum_i x_{u,i} x_{v,i} \geq \binom{n}{2}/k$ by... actually, I think for $K_n$, the uniform assignment IS optimal. Here's why: for $K_n$, $\sum_{(u,v)} \sum_i x_{u,i} x_{v,i} = \sum_i \sum_{u \neq v} x_{u,i} x_{v,i} / 2$... wait, let me be more careful.

$\sum_{(u,v) \in E} \sum_i x_{u,i} x_{v,i} = \sum_i \sum_{(u,v) \in E} x_{u,i} x_{v,i}$

For $K_n$, $E$ is all pairs, so $= \sum_i \sum_{u < v} x_{u,i} x_{v,i} = \frac{1}{2} \sum_i \left[ \left(\sum_u x_{u,i}\right)^2 - \sum_u x_{u,i}^2 \right]$.

Let $S_i = \sum_u x_{u,i}$. Then $\sum_i S_i = n$ (since each vertex contributes 1 total). And $\sum_u x_{u,i}^2 \geq S_i^2 / n$ by Cauchy-Schwarz (or QM-AM). Wait, actually $\sum_u x_{u,i}^2 \geq S_i^2 / n$ when there are $n$ terms... no, that's $\sum_u x_{u,i}^2 \geq S_i^2 / n$ by Cauchy-Schwarz (with $n$ variables). Actually, $\sum_u x_{u,i}^2 \geq S_i^2 / n$ is wrong; it should be $\sum_u x_{u,i}^2 \geq S_i^2 / n$ when there are $n$ terms, which is correct by QM-AM: $\frac{\sum x_{u,i}^2}{n} \geq \left(\frac{\sum x_{u,i}}{n}\right)^2 = \frac{S_i^2}{n^2}$, so $\sum x_{u,i}^2 \geq S_i^2 / n$.

So $\sum_{u<v} x_{u,i} x_{v,i} = \frac{S_i^2 - \sum_u x_{u,i}^2}{2} \leq \frac{S_i^2 - S_i^2/n}{2} = \frac{S_i^2 (n-1)}{2n}$.

Thus total mono edges $\leq \frac{n-1}{2n} \sum_i S_i^2$.

By Cauchy-Schwarz, $\sum_i S_i^2 \geq \frac{(\sum_i S_i)^2}{k} = \frac{n^2}{k}$.

So total mono edges $\leq \frac{(n-1) n}{2k}$... wait, that's an upper bound, not a lower bound. Let me redo this.

We have mono edges $= \frac{1}{2} \sum_i (S_i^2 - \sum_u x_{u,i}^2)$.

To minimize this, we want to minimize $\sum_i S_i^2$ and maximize $\sum_i \sum_u x_{u,i}^2$.

$\sum_i S_i^2$ is minimized when $S_i = n/k$ for all $i$, giving $\sum_i S_i^2 = n^2/k$.

$\sum_i \sum_u x_{u,i}^2$ is maximized when each $x_{u,i}$ is as concentrated as possible, i.e., $x_{u,i} \in \{0, 1\}$. But we're doing fractional, so we want to see what's achievable.

If $S_i = n/k$ for all $i$, and we want to maximize $\sum_u \sum_i x_{u,i}^2$, by convexity, we should make each $x_{u,i}$ as extreme as possible. The maximum of $\sum_i x_{u,i}^2$ subject to $\sum_i x_{u,i} = 1, x_{u,i} \geq 0$ is 1 (achieved when one $x_{u,i} = 1$). The minimum is $1/k$ (uniform).

So if we use integral assignments, $\sum_u \sum_i x_{u,i}^2 = n$, and mono edges $= \frac{1}{2}(n^2/k - n) = \frac{n(n-k)}{2k}$.

For $K_{13}$ with $k=4$: $\frac{13 \cdot 9}{8} = \frac{117}{8} = 14.625$.

But wait, with integral assignments and $S_i = 13/4$, which isn't an integer, we can't have exactly $S_i = 13/4$. The closest is $4, 3, 3, 3$, giving $\sum S_i^2 = 16 + 9 + 9 + 9 = 43$, and $\sum x_{u,i}^2 = 13$ (integral). Mono edges $= \frac{43 - 13}{2} = 15$. ✓

With fractional assignments and $S_i = 13/4$: $\sum S_i^2 = 4 \cdot (13/4)^2 = 4 \cdot 169/16 = 169/4 = 42.25$. And $\sum x_{u,i}^2$ can be at most... if we make each vertex's assignment as concentrated as possible while maintaining $S_i = 13/4$... 

Actually, with $S_i = 13/4$ for each $i$, and 13 vertices, the average $x_{u,i} = 1/4$ for each $u, i$. To maximize $\sum x_{u,i}^2$, we'd want some vertices to have $x_{u,i}$ close to 1 and others close to 0, but we need $S_i = 13/4$ for each color.

One approach: assign 4 vertices to be purely color 1, 3 to be purely color 2, 3 purely color 3, 3 purely color 4. But then $S_1 = 4, S_2 = 3, S_3 = 3, S_4 = 3$, not uniform.

To get $S_i = 13/4$ for all $i$ with maximum $\sum x^2$: we could have some vertices purely one color and others split. For example, 1 vertex purely color 1 ($S_1$ contribution 1), and the remaining $13/4 - 1 = 9/4$ comes from other vertices. This is getting complicated.

The point is: the fractional minimum for $K_{13}$ with 4 colors is $\frac{1}{2}(169/4 - \max \sum x^2)$. The maximum $\sum x^2$ with $S_i = 13/4$ is achieved by making assignments as extreme as possible. 

Actually, I realize the fractional minimum might be lower than 15. Let me think about whether we can achieve fewer than 15 mono edges fractionally for $K_{13}$.

With $S_i = 13/4$ and maximizing $\sum x_{u,i}^2$: We can have 3 vertices purely color 1, 3 purely color 2, 3 purely color 3, 3 purely color 4, and 1 vertex split equally: $1/4$ of each color. Then $S_i = 3 + 1/4 = 13/4$ for each $i$. And $\sum x_{u,i}^2 = 12 \cdot 1 + 4 \cdot (1/4)^2 = 12 + 1/4 = 49/4$. Mono edges $= \frac{169/4 - 49/4}{2} = \frac{120/4}{2} = \frac{30}{2} = 15$.

Hmm, same as integral! What if we split more vertices?

2 vertices purely color 1, 2 purely color 2, 2 purely color 3, 2 purely color 4, and 5 vertices each split equally: $S_i = 2 + 5/4 = 13/4$. $\sum x^2 = 8 + 5 \cdot 4 \cdot (1/16) = 8 + 5/4 = 37/4$. Mono $= (169/4 - 37/4)/2 = (132/4)/2 = 33/2 = 16.5$. Worse!

So splitting more makes it worse. The best fractional with $S_i = 13/4$ is to have as many pure assignments as possible: 12 pure + 1 split, giving 15.

What if $S_i$ is not uniform? Let's try $S_1 = 4, S_2 = S_3 = S_4 = 3$ (integral): mono = 15 as computed.

What about $S_1 = 4.5, S_2 = 3, S_3 = 3, S_4 = 2.5$? $\sum S_i^2 = 20.25 + 9 + 9 + 6.25 = 44.5$. To maximize $\sum x^2$: we want as many pure assignments as possible. With $S_1 = 4.5$: 4 pure + 1 half. $S_4 = 2.5$: 2 pure + 1 half. $S_2 = S_3 = 3$: 3 pure each. Total pure: 4 + 3 + 3 + 2 = 12, plus 1 vertex split between colors 1 and 4 (half each). $\sum x^2 = 12 + 2 \cdot (1/2)^2 = 12.5$. Mono $= (44.5 - 12.5)/2 = 16$. Worse.

So it seems like 15 is the minimum for $K_{13}$, both fractionally and integrally. Good.

Now, the key question: is $K_{13}$ (or disjoint unions of it) the worst case for 12-regular graphs with 4-coloring?

Let me think about what other graphs could be worse.

Consider a graph $G$ that is 12-regular on $m$ vertices where $m$ is large. Can the minimum mono edges per vertex exceed $15/13$?

For large $m$, a random 12-regular graph is "locally tree-like" and has good expansion. For such graphs, we might be able to find colorings with very few mono edges (close to 0 if the graph is 4-colorable, which it likely is for large $m$).

But we need to consider the worst case, not random graphs.

Let me think about a different construction. Consider the complete multipartite graph or some algebraic construction.

Actually, let me think about the problem from the perspective of the "fractional chromatic number" and the "vector chromatic number."

Hmm, let me try a different approach. Let me think about what happens with a graph that's a union of $K_{13}$'s but with some cross-edges.

Actually, I think the key insight might be related to the following: for $d$-regular graphs, the worst case for $n$-coloring is the complete graph $K_{d+1}$ (when it exists, i.e., when $d+1$ vertices suffice). This is because $K_{d+1}$ is the "most constrained" $d$-regular graph.

But I should verify this. Let me think about whether there's a theorem that establishes this.

There's a result by Bollobás and Scott on judicious partitions, and results by Edwards on max cuts. Let me think about the specific case.

For 2-coloring of $d$-regular graphs: the minimum number of monochromatic edges (i.e., edges not in the max cut) is at most... 

For $K_{d+1}$ with 2 colors: balanced partition $\lfloor(d+1)/2\rfloor, \lceil(d+1)/2\rceil$. Mono = $\binom{\lfloor(d+1)/2\rfloor}{2} + \binom{\lceil(d+1)/2\rceil}{2}$.

For $d$ even ($d = 2k$): $K_{2k+1}$, partition $k, k+1$. Mono = $\binom{k}{2} + \binom{k+1}{2} = \frac{k(k-1)}{2} + \frac{k(k+1)}{2} = k^2$. Per vertex: $k^2/(2k+1)$.

For $d$ odd ($d = 2k+1$): $K_{2k+2}$, partition $k+1, k+1$. Mono = $2\binom{k+1}{2} = k(k+1)$. Per vertex: $k(k+1)/(2k+2) = k/2$.

There's a classical result (I think by Edwards or Poljak and Turzík) that for any graph with $m$ vertices and $e$ edges, the max cut is at least $e/2 + (m-1)/4$. For a $d$-regular graph, $e = dm/2$, so max cut $\geq dm/4 + (m-1)/4$. Mono edges $\leq dm/2 - dm/4 - (m-1)/4 = dm/4 - (m-1)/4 = (dm - m + 1)/4 = (m(d-1) + 1)/4$.

Per vertex: $\approx (d-1)/4$.

For $d = 2k$ (even): $(2k-1)/4$ per vertex. Compare with $K_{2k+1}$: $k^2/(2k+1)$ per vertex. For $k=1$: $(2-1)/4 = 1/4$ vs $1/3$. So $K_3$ is worse. For $k=2$: $3/4$ vs $4/5$. $K_5$ is worse. For $k=3$: $5/4$ vs $9/7 \approx 1.286$. $K_7$ is worse ($9/7 > 5/4$).

So the Edwards bound gives $(d-1)/4$ per vertex, but $K_{d+1}$ gives a higher ratio. So the Edwards bound is not tight for the worst case.

Hmm, but the Edwards bound is a lower bound on the max cut (upper bound on mono edges). The actual worst case might be higher than the Edwards bound but we need to check if $K_{d+1}$ is the worst case.

For $n = 2$, the worst case for $d$-regular graphs is indeed $K_{d+1}$ (or disjoint unions of it). This is because $K_{d+1}$ has the highest "density" and forces the most monochromatic edges.

Actually, I'm not sure this is proven. Let me think about it differently.

Let me consider the general $n$-coloring case. The question is:

$$c(n, k) = \sup_G \min_{\text{coloring}} \frac{\text{mono}(G)}{m}$$

where the sup is over all $kn$-regular graphs $G$ on $m$ vertices (for any valid $m$).

Claim: $c(n, k) = \frac{k(nk - n + 2)}{2(kn + 1)}$, achieved by $K_{kn+1}$.

For $n = 4, k = 3$: $c(4, 3) = \frac{3(12 - 4 + 2)}{2 \cdot 13} = \frac{30}{26} = \frac{15}{13}$.

$100 \times 15/13 = 1500/13 \approx 115.38$.

This is not a clean number. Let me reconsider whether the answer might be different.

Actually, wait. Let me reconsider the problem. Maybe I need to think about this more carefully.

Let me reconsider: is the worst case really $K_{kn+1}$? Or could there be a graph on more vertices that's worse?

Let me think about a specific example. Consider $n = 4, k = 3$, so 12-regular graphs.

What about $m = 26$? Consider a graph that's two copies of $K_{13}$ with a perfect matching between them (removing one edge from each $K_{13}$ to maintain regularity). Actually, this is getting complicated. Let me think of a cleaner construction.

What about the complete graph $K_{13}$ vs. some other 12-regular graph on more vertices?

Let me think about the "Kneser graph" or some other specific graph.

Actually, let me think about this from the perspective of the following result:

For a $d$-regular graph $G$ on $m$ vertices, the minimum number of monochromatic edges in an $n$-coloring is at most:
$$\frac{dm}{2n} - \frac{m}{2} \cdot \frac{d - n + 1}{n \cdot (kn + 1)}$$

Hmm, I'm just guessing at this point. Let me think more carefully.

Let me consider the following approach. For a $d$-regular graph, consider the eigenvalue approach. The number of monochromatic edges in a coloring is related to the quadratic form of the adjacency matrix.

If we have a coloring $\sigma: V \to [n]$, and we define indicator vectors $\mathbf{1}_i$ for each color class, then the number of monochromatic edges is:
$$\text{mono} = \sum_{i=1}^n \frac{\mathbf{1}_i^T A \mathbf{1}_i}{2}$$

where $A$ is the adjacency matrix. This equals:
$$\frac{1}{2} \sum_i \mathbf{1}_i^T A \mathbf{1}_i = \frac{1}{2} \text{tr}(A \sum_i \mathbf{1}_i \mathbf{1}_i^T)$$

Hmm, this is getting complicated. Let me try a different approach.

Let me think about the problem using the following known result:

**Theorem (Edwards, 1973; improved by various authors):** For any graph $G$ with $m$ vertices and $e$ edges, there exists a bipartition (2-coloring) with at most $\frac{e}{2} - \frac{m-1}{4}$ monochromatic edges.

This generalizes to $n$-colorings. For $n$-colorings, there's a result that says:

**Theorem:** For any graph $G$ with $m$ vertices and $e$ edges, there exists an $n$-coloring with at most $\frac{e}{n} - \frac{m(n-1)}{2n^2}$ monochromatic edges... but I need to check this.

Actually, I think the generalization is:

For $n$-coloring, the minimum number of monochromatic edges is at most $\frac{e}{n} - \frac{m-1}{2n} \cdot \frac{n-1}{n}$... I'm not sure.

Let me try to derive it. For a $d$-regular graph on $m$ vertices, $e = dm/2$.

Random coloring gives $e/n = dm/(2n)$ mono edges in expectation.

Can we always do better? For $n = 2$, Edwards showed we can save at least $(m-1)/4$. For general $n$, the saving might be different.

Let me think about the $n$-coloring version of Edwards' result.

Actually, there's a result by Bollobás and Scott (2004) on judicious partitions, and also a result by Edwards generalized to $n$-colorings.

The generalization I recall is: for any graph with $m$ vertices and $e$ edges, there's an $n$-coloring with at most $\frac{e}{n} - \frac{m-1}{2n}$ monochromatic edges. But I'm not sure if this is correct.

Let me check with $K_3$ ($n=2$): $e = 3, m = 3$. Bound: $3/2 - 2/4 = 3/2 - 1/2 = 1$. Actual minimum: 1. ✓

$K_5$ ($n=2$): $e = 10, m = 5$. Bound: $5 - 4/4 = 5 - 1 = 4$. Actual: 4. ✓

$K_7$ ($n=2$): $e = 21, m = 7$. Bound: $21/2 - 6/4 = 10.5 - 1.5 = 9$. Actual: 9. ✓

So for $n = 2$, the bound $\frac{e}{n} - \frac{m-1}{2n} = \frac{e}{2} - \frac{m-1}{4}$ matches Edwards' bound, and it's tight for complete graphs $K_{2k+1}$.

Now for general $n$: is the bound $\frac{e}{n} - \frac{m-1}{2n}$?

Let me check with $K_{13}$ ($n=4$): $e = 78, m = 13$. Bound: $78/4 - 12/8 = 19.5 - 1.5 = 18$. But actual minimum is 15. So the bound 18 is not tight for $K_{13}$ with 4 colors. The bound is an upper bound, and 15 < 18, so it's consistent but not tight.

Hmm, so the Edwards-type bound for $n$-colorings is not tight for $K_{kn+1}$ when $n > 2$. Let me think about what the tight bound is.

Actually, maybe the bound for $n$-colorings is different. Let me think about this more carefully.

For $n$-coloring, the Edwards bound generalizes to: $\frac{e}{n} - \frac{m-1}{2n} \cdot \frac{n-1}{n}$? Let me check.

For $n=2$: $\frac{e}{2} - \frac{m-1}{4} \cdot \frac{1}{1}$... no, $\frac{n-1}{n} = 1/2$ for $n=2$. So $\frac{e}{2} - \frac{m-1}{4} \cdot \frac{1}{2} = \frac{e}{2} - \frac{m-1}{8}$. That doesn't match Edwards.

Let me try another generalization. Maybe the bound is $\frac{e}{n} - \frac{m(n-1)}{2n^2}$?

For $n=2$: $\frac{e}{2} - \frac{m}{4}$. For $K_3$: $3/2 - 3/4 = 3/4$. But actual is 1. So this bound says at most $3/4$ mono edges, but actual minimum is 1. That's wrong (the bound should be an upper bound on the minimum, so it should be ≥ actual minimum).

Hmm, $3/4 < 1$, so this would say there's a coloring with at most $3/4$ mono edges, but the actual minimum is 1. So this bound is too strong and incorrect.

Let me try $\frac{e}{n} - \frac{m-1}{2n}$:

For $n=2, K_3$: $3/2 - 2/4 = 1$. ✓ (tight)
For $n=4, K_{13}$: $78/4 - 12/8 = 19.5 - 1.5 = 18$. Actual is 15, so bound is valid but not tight.

So the bound $\frac{e}{n} - \frac{m-1}{2n}$ is valid for $n=2$ (tight for odd complete graphs) but gives 18 for $K_{13}$ with $n=4$, while actual is 15.

Is this bound actually valid for $n > 2$? Let me think about whether it's proven.

Actually, I think the Edwards bound for $n$-colorings might be: $\frac{e}{n} - \frac{m-1}{2n}$, and this is proven by induction on $n$ (reduce to the $n=2$ case). But I'm not certain.

If this bound is valid, then for a $kn$-regular graph on $m$ vertices:
$$\text{mono} \leq \frac{knm/2}{n} - \frac{m-1}{2n} = \frac{km}{2} - \frac{m-1}{2n}$$

Per vertex: $\frac{k}{2} - \frac{1}{2n} + \frac{1}{2nm} \to \frac{k}{2} - \frac{1}{2n}$ as $m \to \infty$.

For $n=4, k=3$: $\frac{3}{2} - \frac{1}{8} = \frac{11}{8} = 1.375$.

But for $K_{13}$: $\frac{3 \cdot 13}{2} - \frac{12}{8} = 19.5 - 1.5 = 18$, while actual is 15. So the bound gives 18, but actual is 15. The bound is valid but not tight for $K_{13}$.

So the question is: is there a $kn$-regular graph where the minimum mono edges per vertex is close to $\frac{k}{2} - \frac{1}{2n}$?

For $n=4, k=3$: $\frac{11}{8} = 1.375$. Is there a 12-regular graph where every 4-coloring has at least $1.375m$ mono edges?

$K_{13}$ gives $15/13 \approx 1.154$, which is less than $1.375$. So if the bound $\frac{k}{2} - \frac{1}{2n}$ is achievable, there must be a different graph that achieves it.

Hmm, but is the bound $\frac{e}{n} - \frac{m-1}{2n}$ actually proven for $n > 2$? Let me think about this.

For $n = 2$, Edwards proved: max cut $\geq e/2 + (m-1)/4$, i.e., mono $\leq e/2 - (m-1)/4$.

For general $n$, one approach: first find a good 2-coloring, then split each color class into $n/2$ sub-classes (if $n$ is even). But this doesn't directly give the bound.

Actually, I think the correct generalization might be different. Let me look at this from a different angle.

For $n$-coloring, the random coloring gives $e/n$ mono edges. The question is how much we can improve.

For $n = 2$: improvement of $(m-1)/4$ (Edwards).
For general $n$: ?

I think the improvement for $n$-colorings is $\frac{(n-1)(m-1)}{2n^2}$... let me check.

For $n = 2$: $\frac{1 \cdot (m-1)}{8}$. But Edwards gives $(m-1)/4$. So this doesn't match.

Let me try $\frac{(n-1)(m-1)}{2n}$:

For $n = 2$: $(m-1)/4$. ✓ Matches Edwards.

For $n = 4, K_{13}$: $\frac{3 \cdot 12}{8} = \frac{36}{8} = 4.5$. So bound: $78/4 - 4.5 = 19.5 - 4.5 = 15$. That matches the actual minimum of 15!

Wait, that's interesting! Let me double-check.

Bound: $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$.

For $K_{13}$ with $n=4$: $e = 78, m = 13$. $\frac{78}{4} - \frac{3 \cdot 12}{8} = 19.5 - 4.5 = 15$. And actual minimum is 15. So the bound is tight!

Let me check for $n=2$:
$K_3$: $e=3, m=3$. $3/2 - 1 \cdot 2/4 = 1.5 - 0.5 = 1$. Actual: 1. ✓
$K_5$: $e=10, m=5$. $5 - 4/4 = 5 - 1 = 4$. Actual: 4. ✓
$K_7$: $e=21, m=7$. $21/2 - 6/4 = 10.5 - 1.5 = 9$. Actual: 9. ✓

Let me check for $n=3, K_7$ (6-regular, $n=3, k=2$): $e=21, m=7$. $\frac{21}{3} - \frac{2 \cdot 6}{6} = 7 - 2 = 5$. 

Actual minimum for $K_7$ with 3 colors: balanced partition $3, 2, 2$. Mono = $\binom{3}{2} + 2\binom{2}{2} = 3 + 2 = 5$. ✓

Let me check $n=3, K_4$ (3-regular, $n=3, k=1$): $e=6, m=4$. $\frac{6}{3} - \frac{2 \cdot 3}{6} = 2 - 1 = 1$. Actual: $K_4$ with 3 colors, partition $2, 1, 1$. Mono = $\binom{2}{2} = 1$. ✓

So the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ seems to be tight for complete graphs $K_{kn+1}$!

Let me verify the formula for general $K_{kn+1}$ with $n$ colors:
- $e = \binom{kn+1}{2} = \frac{kn(kn+1)}{2}$
- $m = kn+1$
- Bound: $\frac{e}{n} - \frac{(n-1)(m-1)}{2n} = \frac{kn(kn+1)}{2n} - \frac{(n-1) \cdot kn}{2n} = \frac{k(kn+1)}{2} - \frac{k(n-1)}{2} = \frac{k}{2}[(kn+1) - (n-1)] = \frac{k}{2}[kn - n + 2] = \frac{k(kn - n + 2)}{2}$.

And the actual minimum (balanced partition $k+1, k, k, \ldots, k$): $\binom{k+1}{2} + (n-1)\binom{k}{2} = \frac{k(k+1)}{2} + \frac{(n-1)k(k-1)}{2} = \frac{k}{2}[(k+1) + (n-1)(k-1)] = \frac{k}{2}[k + 1 + nk - n - k + 1] = \frac{k}{2}[nk - n + 2] = \frac{k(kn - n + 2)}{2}$. ✓

So the bound is tight for $K_{kn+1}$.

Now, the question is: is this bound valid for ALL graphs (not just complete graphs)? If so, then $c(n,k) = \sup_G \frac{\text{bound}}{m} = \sup_G \left[\frac{e}{nm} - \frac{(n-1)(m-1)}{2nm}\right]$.

For a $kn$-regular graph: $e = knm/2$, so $\frac{e}{nm} = \frac{k}{2}$.

Bound per vertex: $\frac{k}{2} - \frac{(n-1)(m-1)}{2nm} = \frac{k}{2} - \frac{(n-1)}{2n} + \frac{(n-1)}{2nm}$.

As $m \to \infty$: $\frac{k}{2} - \frac{n-1}{2n}$.

For $m = kn+1$ (smallest possible): $\frac{k}{2} - \frac{(n-1) \cdot kn}{2n(kn+1)} = \frac{k}{2} - \frac{k(n-1)}{2(kn+1)} = \frac{k(kn+1) - k(n-1)}{2(kn+1)} = \frac{k(kn + 1 - n + 1)}{2(kn+1)} = \frac{k(kn - n + 2)}{2(kn+1)}$.

This is the $K_{kn+1}$ value. As $m$ increases, the bound per vertex increases (since $\frac{(n-1)}{2nm}$ decreases, making the bound larger). So the supremum is $\frac{k}{2} - \frac{n-1}{2n} = \frac{kn - n + 1}{2n}$... wait, let me recalculate.

$\frac{k}{2} - \frac{n-1}{2n} = \frac{kn - (n-1)}{2n} = \frac{kn - n + 1}{2n}$.

For $n=4, k=3$: $\frac{12 - 4 + 1}{8} = \frac{9}{8} = 1.125$.

But $K_{13}$ gives $15/13 \approx 1.154 > 9/8 = 1.125$.

Wait, that's contradictory. The bound per vertex for $m = kn+1$ is $\frac{k(kn-n+2)}{2(kn+1)} = 15/13 \approx 1.154$, and as $m \to \infty$ it approaches $\frac{kn-n+1}{2n} = 9/8 = 1.125$. So the bound is DECREASING as $m$ increases? Let me recheck.

Bound per vertex: $\frac{k}{2} - \frac{(n-1)(m-1)}{2nm}$.

As $m$ increases, $\frac{(n-1)(m-1)}{2nm}$ increases (approaching $\frac{n-1}{2n}$), so the bound DECREASES. So the maximum is at $m = kn+1$ (the smallest $m$), giving $\frac{k(kn-n+2)}{2(kn+1)}$.

So if the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is valid for all graphs, then:

$$c(n, k) = \frac{k(kn - n + 2)}{2(kn + 1)}$$

achieved by $K_{kn+1}$.

For $n=4, k=3$: $c(4,3) = \frac{3 \cdot 10}{26} = \frac{30}{26} = \frac{15}{13}$.

$100 \times 15/13 = 1500/13 \approx 115.38$.

Hmm, still not clean. Let me reconsider whether the bound is actually valid.

Actually, wait. I need to verify that the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is a valid upper bound on the minimum number of monochromatic edges for ALL graphs, not just complete graphs.

This is a generalization of Edwards' theorem. Edwards' theorem for $n=2$ says: for any graph with $e$ edges and $m$ vertices, max cut $\geq e/2 + (m-1)/4$, i.e., mono $\leq e/2 - (m-1)/4$.

The generalization to $n$ colors would be: for any graph with $e$ edges and $m$ vertices, there exists an $n$-coloring with at most $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ monochromatic edges.

Is this true? Let me think about whether this has been proven.

Actually, I recall that the Edwards bound for $n$-colorings is indeed a known result. Let me think about the proof.

For $n = 2$, Edwards' proof works by induction on $m$. The key idea is that for any graph, there's a vertex $v$ such that removing $v$ and applying the induction hypothesis, then adding $v$ back to the side that minimizes mono edges.

For general $n$, the proof would be similar: remove a vertex, color the rest by induction, then add the vertex to the color class that minimizes the increase in mono edges.

Let me try to prove the bound by induction.

Claim: For any graph $G$ with $m$ vertices and $e$ edges, there's an $n$-coloring with at most $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ monochromatic edges.

Base case: $m = 1$. $e = 0$. Bound: $0 - 0 = 0$. ✓

Inductive step: Assume true for graphs with $m-1$ vertices. Consider $G$ with $m$ vertices and $e$ edges. Remove a vertex $v$ with degree $d(v)$. The remaining graph $G - v$ has $m-1$ vertices and $e - d(v)$ edges. By induction, there's an $n$-coloring of $G - v$ with at most $\frac{e - d(v)}{n} - \frac{(n-1)(m-2)}{2n}$ mono edges.

Now, add $v$ to the color class that minimizes the number of new mono edges. The number of new mono edges is the number of neighbors of $v$ in the chosen color class. The minimum over $n$ color classes is at most $d(v)/n$ (by averaging).

So total mono edges $\leq \frac{e - d(v)}{n} - \frac{(n-1)(m-2)}{2n} + \frac{d(v)}{n} = \frac{e}{n} - \frac{(n-1)(m-2)}{2n}$.

But we want to show $\leq \frac{e}{n} - \frac{(n-1)(m-1)}{2n}$.

We have $\frac{e}{n} - \frac{(n-1)(m-2)}{2n}$, and we want $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$.

The difference is $\frac{(n-1)(m-1)}{2n} - \frac{(n-1)(m-2)}{2n} = \frac{n-1}{2n}$.

So we need to save an additional $\frac{n-1}{2n}$ mono edges when adding $v$. But the averaging argument only guarantees $d(v)/n$ new mono edges, which gives us the bound $\frac{e}{n} - \frac{(n-1)(m-2)}{2n}$, not the stronger bound.

So the simple induction doesn't give the stronger bound. We need a better argument.

For $n = 2$, Edwards' proof is more subtle. The key is that when adding $v$, we can choose the better of the two color classes, and the saving is at least $d(v)/2 - |d_1(v) - d_2(v)|/2$ where $d_i(v)$ is the number of neighbors in color class $i$. But actually, the saving from choosing the better class is $\max(d_1, d_2) - d(v)/2 = |d_1 - d_2|/2$... no, the number of new mono edges is $\min(d_1, d_2) \leq d(v)/2$, and the saving compared to $d(v)/2$ is $d(v)/2 - \min(d_1, d_2) = |d_1 - d_2|/2$.

Edwards' actual proof is more involved. He uses the fact that for $n=2$, the bound $e/2 - (m-1)/4$ is achieved by choosing the right vertex to remove and using a more careful analysis.

Actually, I think the correct generalization might not be $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$. Let me reconsider.

For $n = 2$, the Edwards bound is $\frac{e}{2} - \frac{m-1}{4}$. Note that $\frac{(n-1)(m-1)}{2n} = \frac{(m-1)}{4}$ for $n=2$. ✓

But the inductive proof for $n = 2$ doesn't work with the simple averaging argument. Edwards' proof uses a different technique.

Let me look at this from a different angle. Maybe the bound for general $n$ is different.

Actually, I found that the generalization of Edwards' bound to $n$-colorings is:

**Theorem (Edwards, 1973; for general $n$, see e.g., Bollobás & Scott):** For any graph with $e$ edges and $m$ vertices, there exists an $n$-coloring with at most $\frac{e}{n} - \frac{m-1}{2n} \cdot \frac{n-1}{n}$ monochromatic edges.

Wait, that gives $\frac{e}{n} - \frac{(n-1)(m-1)}{2n^2}$.

For $n=2$: $\frac{e}{2} - \frac{(m-1)}{8}$. But Edwards' bound is $\frac{e}{2} - \frac{m-1}{4}$. So this doesn't match.

Hmm, let me try yet another generalization.

Actually, I think there are different generalizations. Let me think about what's known.

For $n$-coloring, the random coloring gives $e/n$ mono edges. The question is the best improvement.

One result I recall is by Bollobás and Scott (2004): for any graph with $m$ vertices and $e$ edges, there's an $n$-coloring with at most $\frac{e}{n} - \frac{m}{2n} \cdot \frac{n-1}{n} \cdot \delta$ mono edges, where $\delta$ is the minimum degree. But this involves $\delta$, not just $m$.

For a $d$-regular graph, $\delta = d$, so the bound would be $\frac{e}{n} - \frac{m}{2n} \cdot \frac{(n-1)d}{n} = \frac{dm}{2n} - \frac{m(n-1)d}{2n^2} = \frac{dm}{2n^2}$. For $d = kn$: $\frac{knm}{2n^2} = \frac{km}{2n}$. Per vertex: $\frac{k}{2n}$.

For $n=4, k=3$: $3/8 = 0.375$. That's way below $15/13 \approx 1.154$. So this can't be right (it would say we can always achieve 0.375m mono edges, but $K_{13}$ requires 15 mono edges = $15/13 \cdot 13 \approx 1.154 \cdot 13$).

So that formula is wrong. Let me think again.

OK let me take a step back. I was getting confused with various formulas. Let me think about this more carefully.

The key question is: what is the correct upper bound on the minimum number of monochromatic edges in an $n$-coloring of a graph with $e$ edges and $m$ vertices?

For $n = 2$, Edwards' bound is: mono $\leq \frac{e}{2} - \frac{m-1}{4}$, and this is tight for $K_{2k+1}$ (odd complete graphs).

For general $n$, I need to find the correct bound.

Let me think about what bound would be tight for $K_{kn+1}$ with $n$ colors.

For $K_{kn+1}$: $e = \binom{kn+1}{2}$, $m = kn+1$, min mono = $\frac{k(kn-n+2)}{2}$.

So the bound should give $\frac{k(kn-n+2)}{2}$ when evaluated at $K_{kn+1}$.

$\frac{e}{n} = \frac{kn(kn+1)}{2n} = \frac{k(kn+1)}{2}$.

We need: $\frac{k(kn+1)}{2} - f(m, n) = \frac{k(kn-n+2)}{2}$.

So $f(m, n) = \frac{k(kn+1)}{2} - \frac{k(kn-n+2)}{2} = \frac{k}{2}[(kn+1) - (kn-n+2)] = \frac{k}{2}[n-1] = \frac{k(n-1)}{2}$.

With $m = kn+1$: $f(kn+1, n) = \frac{k(n-1)}{2}$.

If $f(m, n) = \frac{(n-1)(m-1)}{2n}$, then $f(kn+1, n) = \frac{(n-1) \cdot kn}{2n} = \frac{k(n-1)}{2}$. ✓

So the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ gives the right value for $K_{kn+1}$. But is it valid for all graphs?

Let me check with a specific non-complete graph. Take $C_5$ (5-cycle, 2-regular) with $n=2$: $e=5, m=5$. Bound: $5/2 - 4/4 = 2.5 - 1 = 1.5$. Actual min mono: max cut of $C_5$ is 4, so mono = 1. $1 \leq 1.5$. ✓ (bound is valid but not tight).

Take $C_4$ with $n=2$: $e=4, m=4$. Bound: $2 - 3/4 = 1.25$. Actual: max cut = 4, mono = 0. $0 \leq 1.25$. ✓

Take $K_{3,3}$ (3-regular, 6 vertices) with $n=2$: $e=9, m=6$. Bound: $9/2 - 5/4 = 4.5 - 1.25 = 3.25$. Actual: $K_{3,3}$ is bipartite, so max cut = 9, mono = 0. $0 \leq 3.25$. ✓

Take $K_6$ (5-regular, 6 vertices) with $n=3$: $e=15, m=6$. Bound: $15/3 - 2 \cdot 5/6 = 5 - 5/3 = 10/3 \approx 3.33$. Actual: balanced partition $2,2,2$, mono = $3 \cdot 1 = 3$. $3 \leq 10/3$. ✓

Take $K_7$ (6-regular, 7 vertices) with $n=3$: $e=21, m=7$. Bound: $21/3 - 2 \cdot 6/6 = 7 - 2 = 5$. Actual: partition $3,2,2$, mono = $3 + 1 + 1 = 5$. $5 \leq 5$. ✓ (tight!)

Take $K_8$ (7-regular, 8 vertices) with $n=4$: $e=28, m=8$. Bound: $28/4 - 3 \cdot 7/8 = 7 - 21/8 = 35/8 = 4.375$. Actual: partition $2,2,2,2$, mono = $4 \cdot 1 = 4$. $4 \leq 4.375$. ✓ (not tight, because $K_8$ is 7-regular, not $kn$-regular for $n=4$).

Hmm wait, $K_8$ is 7-regular. For $n=4$, we'd want $kn$-regular = $4k$-regular. $K_8$ is 7-regular, which is not a multiple of 4. So $K_8$ is not relevant for our problem.

Let me check $K_9$ (8-regular, 9 vertices) with $n=4, k=2$: $e=36, m=9$. Bound: $36/4 - 3 \cdot 8/8 = 9 - 3 = 6$. Actual: partition $3,2,2,2$, mono = $3 + 1 + 1 + 1 = 6$. $6 \leq 6$. ✓ (tight!)

Great, so the bound is tight for $K_{kn+1}$ with $n$ colors.

Now, the crucial question: is the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ valid for ALL graphs?

Let me try to prove it by induction, more carefully.

Claim: For any graph $G$ with $m$ vertices and $e$ edges, there's an $n$-coloring with at most $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ mono edges.

Proof attempt by induction on $m$:

Base: $m = 1$. $e = 0$. Bound: $0$. ✓

Inductive step: Let $v$ be a vertex of $G$ with degree $d$. By induction, $G - v$ has an $n$-coloring with at most $\frac{e-d}{n} - \frac{(n-1)(m-2)}{2n}$ mono edges. Add $v$ to the color class minimizing new mono edges. New mono edges $\leq d/n$ (by averaging). Total: $\frac{e-d}{n} - \frac{(n-1)(m-2)}{2n} + \frac{d}{n} = \frac{e}{n} - \frac{(n-1)(m-2)}{2n}$.

We want: $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$. The gap is $\frac{(n-1)(m-1) - (n-1)(m-2)}{2n} = \frac{n-1}{2n}$.

So the simple induction gives a bound that's $\frac{n-1}{2n}$ too weak. We need to save an extra $\frac{n-1}{2n}$ when adding $v$.

For $n = 2$, Edwards' proof handles this by choosing $v$ carefully (a vertex of minimum degree) and using the fact that the saving from choosing the better color class is at least $\frac{|d_1 - d_2|}{2} \geq \frac{1}{2}$ (since $d_1 + d_2 = d$ and $d_1, d_2$ are integers, $|d_1 - d_2| \geq 1$ when $d$ is odd, or $\geq 0$ when $d$ is even). Actually, Edwards' proof is more subtle.

Hmm, let me think about this differently. Maybe the bound isn't $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ for all graphs, but only for certain graphs (like regular graphs or complete graphs).

Actually, let me reconsider. Maybe the correct bound for general $n$-colorings is different from what I conjectured.

Let me look at this from the perspective of what's known in the literature.

The Edwards bound for $n=2$ is: max cut $\geq \frac{e}{2} + \frac{m-1}{4}$. This is equivalent to: mono $\leq \frac{e}{2} - \frac{m-1}{4}$.

For general $n$, there's a result by Bollobás and Scott (2004), "Judicious partitions of graphs" and related work. Also, there's a result by Edwards himself for $n$-colorings.

Actually, I think the correct generalization is:

For any graph with $e$ edges and $m$ vertices, there's an $n$-coloring with at most $\frac{e}{n} - \frac{m-1}{2n}$ mono edges.

For $n = 2$: $\frac{e}{2} - \frac{m-1}{4}$. ✓ Matches Edwards.

For $K_{13}$ with $n=4$: $\frac{78}{4} - \frac{12}{8} = 19.5 - 1.5 = 18$. But actual is 15. So the bound is 18, not tight.

Hmm, so this bound is valid but not tight for $K_{kn+1}$ when $n > 2$.

But then the question is: is there a graph where the bound $\frac{e}{n} - \frac{m-1}{2n}$ is tight? If so, that graph would be the worst case, not $K_{kn+1}$.

For a $kn$-regular graph on $m$ vertices: bound per vertex = $\frac{k}{2} - \frac{m-1}{2nm} \to \frac{k}{2} - \frac{1}{2n}$ as $m \to \infty$.

For $n=4, k=3$: $\frac{3}{2} - \frac{1}{8} = \frac{11}{8} = 1.375$.

Is there a 12-regular graph where every 4-coloring has at least $\frac{11}{8}m$ mono edges (asymptotically)?

Hmm, I think the bound $\frac{e}{n} - \frac{m-1}{2n}$ might not be tight for $n > 2$. Let me think about what the tight bound is.

Actually, let me reconsider. For $n = 2$, the Edwards bound is tight for $K_{2k+1}$ (odd complete graphs). For $n > 2$, what graph is the extremal case?

Let me think about this more carefully. For $n$-coloring, the problem is to partition vertices into $n$ classes minimizing the total number of intra-class edges.

For $n = 2$, the worst case is $K_{2k+1}$ (odd complete graph), which is $2k$-regular.

For general $n$, is the worst case $K_{kn+1}$ (complete graph on $kn+1$ vertices, which is $kn$-regular)?

For $K_{kn+1}$ with $n$ colors, the min mono is $\frac{k(kn-n+2)}{2}$, and per vertex it's $\frac{k(kn-n+2)}{2(kn+1)}$.

For $n = 2$: $\frac{k(2k - 2 + 2)}{2(2k+1)} = \frac{k \cdot 2k}{2(2k+1)} = \frac{k^2}{2k+1}$. And the Edwards bound per vertex for $K_{2k+1}$ is $\frac{e/2 - (m-1)/4}{m} = \frac{k(2k+1)/2 - k/2}{2k+1} = \frac{k^2}{2k+1}$. ✓ So they match for $n=2$.

For $n = 3, k = 2$: $K_7$, min mono = 5, per vertex = 5/7. Edwards bound ($n=3$): $\frac{e}{3} - \frac{m-1}{6} = \frac{21}{3} - \frac{6}{6} = 7 - 1 = 6$. So bound is 6, actual is 5. Not tight.

So for $n > 2$, the Edwards bound $\frac{e}{n} - \frac{m-1}{2n}$ is NOT tight for $K_{kn+1}$.

This means either:
1. The worst case is $K_{kn+1}$, and the correct bound is $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ (which is tight for $K_{kn+1}$), or
2. The worst case is some other graph, and the Edwards bound $\frac{e}{n} - \frac{m-1}{2n}$ is the correct one (tight for some other graph).

I need to determine which is correct.

Let me think about whether the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is valid for all graphs.

Check: $C_5$ with $n=3$: $e=5, m=5$. Bound: $5/3 - 2 \cdot 4/6 = 5/3 - 4/3 = 1/3$. Actual: $C_5$ with 3 colors, we can properly 3-color it (since $\chi(C_5) = 3$), so mono = 0. $0 \leq 1/3$. ✓

Check: $K_4$ with $n=3$: $e=6, m=4$. Bound: $6/3 - 2 \cdot 3/6 = 2 - 1 = 1$. Actual: partition $2,1,1$, mono = 1. $1 \leq 1$. ✓ (tight!)

Check: $K_5$ with $n=3$: $e=10, m=5$. Bound: $10/3 - 2 \cdot 4/6 = 10/3 - 4/3 = 2$. Actual: partition $2,2,1$, mono = $1 + 1 + 0 = 2$. $2 \leq 2$. ✓ (tight!)

Check: $K_6$ with $n=3$: $e=15, m=6$. Bound: $15/3 - 2 \cdot 5/6 = 5 - 5/3 = 10/3 \approx 3.33$. Actual: partition $2,2,2$, mono = 3. $3 \leq 10/3$. ✓ (not tight, because $K_6$ is 5-regular, not $kn$-regular for $n=3$).

Check: $K_7$ with $n=3$: $e=21, m=7$. Bound: $21/3 - 2 \cdot 6/6 = 7 - 2 = 5$. Actual: 5. ✓ (tight!)

Check: $K_8$ with $n=3$: $e=28, m=8$. Bound: $28/3 - 2 \cdot 7/6 = 28/3 - 7/3 = 7$. Actual: partition $3,3,2$, mono = $3 + 3 + 1 = 7$. $7 \leq 7$. ✓ (tight!)

Interesting! $K_8$ with $n=3$ is also tight. $K_8$ is 7-regular, not $3k$-regular. So the bound is tight for $K_m$ with $n$ colors whenever $m \not\equiv 0 \pmod{n}$... let me check.

For $K_m$ with $n$ colors, the min mono is: partition into classes of size $\lfloor m/n \rfloor$ and $\lceil m/n \rceil$. If $m = qn + r$ with $0 \leq r < n$, then $r$ classes of size $q+1$ and $n-r$ classes of size $q$. Mono = $r\binom{q+1}{2} + (n-r)\binom{q}{2} = \frac{r \cdot q(q+1) + (n-r) \cdot q(q-1)}{2} = \frac{q}{2}[r(q+1) + (n-r)(q-1)] = \frac{q}{2}[rq + r + nq - n - rq + r] = \frac{q}{2}[nq - n + 2r] = \frac{q(nq - n + 2r)}{2}$.

Bound: $\frac{e}{n} - \frac{(n-1)(m-1)}{2n} = \frac{m(m-1)}{2n} - \frac{(n-1)(m-1)}{2n} = \frac{(m-1)(m - n + 1)}{2n}$.

With $m = qn + r$: $\frac{(qn+r-1)(qn+r-n+1)}{2n} = \frac{(qn+r-1)(qn+r-n+1)}{2n}$.

Actual: $\frac{q(nq - n + 2r)}{2} = \frac{q(n(q-1) + 2r)}{2} = \frac{nq(q-1) + 2qr}{2} = \frac{nq^2 - nq + 2qr}{2}$.

Bound: $\frac{(qn+r-1)(qn+r-n+1)}{2n}$. Let me expand: $qn+r-1 = nq + r - 1$ and $qn+r-n+1 = n(q-1) + r + 1$. Product: $(nq + r - 1)(n(q-1) + r + 1) = n^2 q(q-1) + nq(r+1) + n(q-1)(r-1) + (r-1)(r+1) = n^2 q(q-1) + nq(r+1) + n(q-1)(r-1) + r^2 - 1$.

$= n^2 q(q-1) + n[q(r+1) + (q-1)(r-1)] + r^2 - 1$
$= n^2 q(q-1) + n[qr + q + qr - q - r + 1] + r^2 - 1$
$= n^2 q(q-1) + n[2qr - r + 1] + r^2 - 1$
$= n^2 q(q-1) + 2nqr - nr + n + r^2 - 1$

Divided by $2n$: $\frac{nq(q-1)}{2} + qr - \frac{r}{2} + \frac{1}{2} + \frac{r^2 - 1}{2n}$.

$= \frac{nq^2 - nq}{2} + qr - \frac{r}{2} + \frac{1}{2} + \frac{r^2 - 1}{2n}$.

Actual: $\frac{nq^2 - nq + 2qr}{2} = \frac{nq^2 - nq}{2} + qr$.

Difference (bound - actual): $-\frac{r}{2} + \frac{1}{2} + \frac{r^2 - 1}{2n} = \frac{1 - r}{2} + \frac{r^2 - 1}{2n} = \frac{(1-r)}{2} + \frac{(r-1)(r+1)}{2n} = \frac{(1-r)}{2}\left[1 - \frac{r+1}{n}\right] = \frac{(1-r)(n - r - 1)}{2n}$.

For $r = 0$: $\frac{1 \cdot (n-1)}{2n} = \frac{n-1}{2n} > 0$. So bound > actual (not tight).
For $r = 1$: $\frac{0 \cdot (n-2)}{2n} = 0$. So bound = actual (tight!).
For $r > 1$: $(1-r) < 0$ and $(n - r - 1) \geq 0$ (since $r < n$), so difference $\leq 0$. Bound < actual?? That would mean the bound is violated!

Wait, that can't be right. Let me recheck with a specific example.

$K_9$ with $n=4$: $m=9, q=2, r=1$. Actual: $\frac{2(4 \cdot 2 - 4 + 2)}{2} = \frac{2 \cdot 6}{2} = 6$. Bound: $\frac{8 \cdot 6}{8} = 6$. ✓ (tight, $r=1$).

$K_{10}$ with $n=4$: $m=10, q=2, r=2$. Actual: $\frac{2(8 - 4 + 4)}{2} = \frac{2 \cdot 8}{2} = 8$. Bound: $\frac{9 \cdot 7}{8} = \frac{63}{8} = 7.875$. So bound = 7.875 < actual = 8. The bound is violated!

So the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is NOT valid for all graphs! It fails for $K_{10}$ with $n=4$.

This means my conjectured bound is wrong. Let me reconsider.

So for $K_{10}$ with $n=4$: the minimum mono edges is 8 (partition $3,3,2,2$: mono = $3+3+1+1=8$). The bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n} = \frac{45}{4} - \frac{3 \cdot 9}{8} = 11.25 - 3.375 = 7.875 < 8$. So the bound says there should be a coloring with at most 7.875 mono edges, but the actual minimum is 8. Contradiction!

So the bound $\frac{e}{n} - \frac{(n-1)(m-1)}{2n}$ is NOT valid in general. It's only valid for certain graphs (like $K_{kn+1}$ where $r=1$).

OK so I need to rethink. The Edwards bound $\frac{e}{n} - \frac{m-1}{2n}$ is valid (I'll assume this is proven), and it gives 18 for $K_{13}$ with $n=4$, while actual is 15. So the Edwards bound is not tight for $K_{kn+1}$ when $n > 2$.

Now, the question is: what is the actual worst case? Is it $K_{kn+1}$ (giving $15/13$ per vertex for $n=4, k=3$), or is there a graph that's worse?

Let me think about $K_{10}$ with $n=4$. $K_{10}$ is 9-regular, not 12-regular. So it's not relevant for our problem ($n=4, k=3$ requires 12-regular graphs).

For 12-regular graphs, the smallest is $K_{13}$ (13 vertices). The next possible sizes are $m = 14, 15, \ldots$ (any $m \geq 13$ with $12m$ even, which is all $m \geq 13$).

Let me think about whether there's a 12-regular graph on $m > 13$ vertices that has a higher min-mono-per-vertex ratio than $K_{13}$.

For $K_{13}$: ratio = $15/13 \approx 1.1538$.

Let me consider $m = 14$. A 12-regular graph on 14 vertices. The complement is a 1-regular graph on 14 vertices (perfect matching). So $G = K_{14} - M$.

Min mono for $K_{14}$ with 4 colors: partition $4,4,3,3$, mono = $6+6+3+3 = 18$. But we subtract the matching edges within each class. With 7 matching edges, we can place at most 6 within classes (2 in each size-4 class, 1 in each size-3 class). So min mono $\leq 18 - 6 = 12$. Per vertex: $12/14 = 6/7 \approx 0.857$. Much less than $15/13$.

What about $m = 26$? Two copies of $K_{13}$. Min mono = $2 \times 15 = 30$. Per vertex: $30/26 = 15/13$. Same as $K_{13}$.

What about a 12-regular graph on 26 vertices that's not two copies of $K_{13}$? For example, take $K_{26}$ and remove a 13-regular graph. The complement would be 13-regular. 

Actually, let me think about this differently. For a 12-regular graph on $m$ vertices, the min mono per vertex is at most $\frac{k}{2} - \frac{m-1}{2nm}$ (from the Edwards bound). For $n=4, k=3$: $\frac{3}{2} - \frac{m-1}{8m}$. As $m \to \infty$, this approaches $3/2 - 1/8 = 11/8 = 1.375$.

But is the Edwards bound tight? Is there a 12-regular graph where the min mono per vertex approaches $11/8$?

For $n = 2$, the Edwards bound is tight for $K_{2k+1}$ (and disjoint unions). For $n > 2$, I need to think about what graph makes it tight.

Actually, wait. For $n = 2$, the Edwards bound is $\frac{e}{2} - \frac{m-1}{4}$. For $K_{2k+1}$: $\frac{k(2k+1)}{2} - \frac{2k}{4} = \frac{k(2k+1)}{2} - \frac{k}{2} = \frac{k \cdot 2k}{2} = k^2$. And actual is $k^2$. So tight. ✓

For $n = 3$, the Edwards bound is $\frac{e}{3} - \frac{m-1}{6}$. For $K_7$ ($k=2$): $\frac{21}{3} - \frac{6}{6} = 7 - 1 = 6$. Actual is 5. Not tight.

So for $n = 3$, the Edwards bound is not tight for $K_7$. Is it tight for some other graph?

Hmm, let me think about what graph would make the Edwards bound tight for $n = 3$.

For the Edwards bound $\frac{e}{n} - \frac{m-1}{2n}$ to be tight, we need a graph where the min mono equals this value.

For $n = 3$, consider a graph that's a disjoint union of $K_3$'s... no, $K_3$ is 2-regular, not $3k$-regular.

Let me think about this differently. For $n = 2$, the Edwards bound is tight for odd complete graphs. The key property is that $K_{2k+1}$ has chromatic number $2k+1$, which is odd, so it can't be properly 2-colored.

For $n = 3$, what graph has the property that every 3-coloring has many mono edges?

Consider $K_{3k+1}$ (which is $3k$-regular). For $k=2$: $K_7$, min mono = 5, Edwards bound = 6. Not tight.

What about a different graph? Let me think about the Petersen graph or some other specific graph.

Actually, let me think about this more carefully. The Edwards bound for $n$-colorings might not be $\frac{e}{n} - \frac{m-1}{2n}$. Let me look for the correct generalization.

I recall now that the correct generalization of Edwards' bound to $n$-colorings is:

For any graph with $e$ edges and $m$ vertices, there's an $n$-coloring with at most $\frac{e}{n} - \frac{m-1}{2n}$ monochromatic edges.

And this is proven by induction on $n$ (not $m$). The idea is: first find a good 2-coloring (using Edwards' bound), then recursively color each part with $n/2$ colors.

But this only works for $n$ a power of 2. For general $n$, the approach is different.

Actually, I think the correct statement might be:

For any graph with $e$ edges and $m$ vertices, there's an $n$-coloring with at most $\frac{e}{n} - \frac{(n-1)(m-1)}{2n^2}$ monochromatic edges.

Let me check: for $n=2$: $\frac{e}{2} - \frac{(m-1)}{8}$. But Edwards gives $\frac{e}{2} - \frac{m-1}{4}$. So this is weaker. Not the right generalization.

Hmm, let me try another approach. Let me look at the proof of Edwards' theorem and see how it generalizes.

Edwards' theorem ($n=2$): Every graph with $e$ edges and $m$ vertices has a cut of size at least $\frac{e}{2} + \frac{m-1}{4}$.

Proof sketch: By induction on $m$. If $G$ has a vertex $v$ of even degree, remove it, find a good cut of $G-v$, then add $v$ to the side with fewer neighbors. The saving is $d(v)/2$ compared to random, and the induction gives $\frac{e-d(v)}{2} + \frac{m-2}{4}$, so total cut $\geq \frac{e-d(v)}{2} + \frac{m-2}{4} + \frac{d(v)}{2} = \frac{e}{2} + \frac{m-2}{4}$. We need $\frac{m-1}{4}$, so we're short by $\frac{1}{4}$.

If all vertices have odd degree, then $m$ is even (since $\sum d(v) = 2e$ is even, and all $d(v)$ are odd, so $m$ must be even). In this case, we can find a vertex $v$ such that removing it and using a more careful argument gives the extra $\frac{1}{4}$.

Actually, the proof is more subtle. Let me not try to reconstruct it and instead think about the problem from a higher level.

The key question is: for $kn$-regular graphs with $n$-coloring, what is $c(n,k) = \sup_G \min_{\text{coloring}} \frac{\text{mono}}{m}$?

I've established:
1. $K_{kn+1}$ gives a lower bound of $\frac{k(kn-n+2)}{2(kn+1)}$.
2. The Edwards bound (if valid for $n$-colorings) gives an upper bound of $\frac{k}{2} - \frac{m-1}{2nm}$, which is maximized at $m = kn+1$ giving $\frac{k}{2} - \frac{kn}{2n(kn+1)} = \frac{k}{2} - \frac{k}{2(kn+1)} = \frac{k(kn+1) - k}{2(kn+1)} = \frac{k \cdot kn}{2(kn+1)} = \frac{k^2 n}{2(kn+1)}$.

Wait, let me recompute. For $m = kn+1$:
$\frac{k}{2} - \frac{kn}{2n(kn+1)} = \frac{k}{2} - \frac{k}{2(kn+1)} = \frac{k(kn+1) - k}{2(kn+1)} = \frac{k^2 n}{2(kn+1)}$.

For $n=4, k=3$: $\frac{9 \cdot 4}{2 \cdot 13} = \frac{36}{26} = \frac{18}{13} \approx 1.385$.

But the actual value for $K_{13}$ is $15/13 \approx 1.154$. So the Edwards bound gives $18/13$, which is higher than the actual $15/13$. This means the Edwards bound is not tight for $K_{13}$ with $n=4$.

So the question remains: is there a 12-regular graph where the min mono per vertex is higher than $15/13$?

Let me think about this more carefully. The Edwards bound for $n$-colorings gives an upper bound of $\frac{k^2 n}{2(kn+1)}$ for $m = kn+1$. But the actual value for $K_{kn+1}$ is $\frac{k(kn-n+2)}{2(kn+1)}$. The gap is:

$\frac{k^2 n}{2(kn+1)} - \frac{k(kn-n+2)}{2(kn+1)} = \frac{k(kn - kn + n - 2)}{2(kn+1)} = \frac{k(n-2)}{2(kn+1)}$.

For $n = 2$: gap = 0. So the Edwards bound is tight for $n=2$. ✓
For $n > 2$: gap > 0. So the Edwards bound is not tight for $K_{kn+1}$.

This means either:
(a) The Edwards bound is not the correct upper bound for $n$-colorings (maybe the correct bound is tighter), or
(b) There exists a graph (not $K_{kn+1}$) where the min mono per vertex is higher than $15/13$ and approaches the Edwards bound.

Let me think about (b). Is there a 12-regular graph on $m$ vertices where the min mono per vertex is close to $\frac{3}{2} - \frac{1}{8} = \frac{11}{8} = 1.375$?

For large $m$, a random 12-regular graph is likely 4-colorable (since the chromatic number of a random $d$-regular graph is roughly $d/(2\ln d)$, which for $d=12$ is about $12/(2 \cdot 2.48) \approx 2.4$, so likely 3 or 4-colorable). If 4-colorable, min mono = 0.

But we need the worst case, not random graphs. Let me think about specific constructions.

What about a graph that's a "complete multipartite" type or has high chromatic number?

For a 12-regular graph, the chromatic number is at most 13 (by Brooks' theorem, at most 12 unless it's $K_{13}$ or an odd cycle). So the graph could have chromatic number up to 13, but we're coloring with only 4 colors.

Hmm, let me think about the Kneser graph or some other specific graph.

Actually, let me think about this problem differently. Let me consider the "fractional" version more carefully.

For a $d$-regular graph $G$, the minimum number of mon
