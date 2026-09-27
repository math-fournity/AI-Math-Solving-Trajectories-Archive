# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let $n \geq 3$ be an integer. A labelling of the $n$ vertices, the $n$ sides, and the interior of a regular $n$-gon by $2n + 1$ distinct integers is called memorable if:
(a) Each side has a label that is the arithmetic mean of the labels of its endpoints.
(b) The interior of the $n$-gon has a label that is the arithmetic mean of the labels of all the vertices.

Find the sum of all integers $n$ in the range $3 \leq n \leq 100$ for which there exists a memorable labelling of a regular $n$-gon consisting of $2n + 1$ consecutive integers.       — 题目文本
#   From the original solution, a memorable labelling exists if and only if $n \equiv 0 \pmod{4}$. 
In the range $3 \leq n \leq 100$, the values of $n$ satisfying this condition are $4, 8, 12, \ldots, 100$. 
These values form an arithmetic progression with first term $a=4$, last term $l=100$, and common difference $d=4$. 
The number of terms is $k = \frac{100 - 4}{4} + 1 = 25$. 
The sum of these terms is $\frac{k(a + l)}{2} = \frac{25(4 + 100)}{2} = \frac{25 \times 104}{2} = 25 \times 52 = 1300$.  — 标准解答
#   The problem asks me to solve a math problem directly in the TUI without using any tools or writing files. Let me read the problem carefully.

Problem: Let $n \geq 3$ be an integer. A labelling of the $n$ vertices, the $n$ sides, and the interior of a regular $n$-gon by $2n+1$ distinct integers is called memorable if:
(a) Each side has a label that is the arithmetic mean of the labels of its endpoints.
(b) The interior of the $n$-gon has a label that is the arithmetic mean of the labels of all the vertices.

Find the sum of all integers $n$ in the range $3 \leq n \leq 100$ for which there exists a memorable labelling of a regular $n$-gon consisting of $2n+1$ consecutive integers.

Let me think about this.

We have $2n+1$ consecutive integers. Let's say they are $\{a, a+1, a+2, \ldots, a+2n\}$ for some integer $a$.

The vertices get $n$ labels, the sides get $n$ labels, and the interior gets 1 label. All $2n+1$ distinct.

Condition (a): Each side label = arithmetic mean of its two endpoint (vertex) labels. So if vertices are $v_1, v_2, \ldots, v_n$ (in order around the polygon), then side $i$ (between $v_i$ and $v_{i+1}$, with $v_{n+1} = v_1$) has label $s_i = (v_i + v_{i+1})/2$.

For $s_i$ to be an integer, $v_i + v_{i+1}$ must be even, so $v_i$ and $v_{i+1}$ have the same parity. Since this holds for all consecutive pairs, all vertices have the same parity.

Condition (b): Interior label = arithmetic mean of all vertex labels. So interior = $(v_1 + v_2 + \cdots + v_n)/n$. This must be an integer, so $n | (v_1 + \cdots + v_n)$.

Now, the $2n+1$ consecutive integers are $\{a, a+1, \ldots, a+2n\}$. The sum of all of them is $(2n+1)(2a+2n)/2 = (2n+1)(a+n)$.

The sum of all labels = sum of vertices + sum of sides + interior.

Sum of sides = $\sum_{i=1}^n (v_i + v_{i+1})/2 = \sum_{i=1}^n v_i$ (since each vertex appears in exactly 2 sides, so $\sum (v_i + v_{i+1})/2 = (2\sum v_i)/2 = \sum v_i$).

Wait, let me recompute. $\sum_{i=1}^n s_i = \sum_{i=1}^n (v_i + v_{i+1})/2 = \frac{1}{2}\sum_{i=1}^n (v_i + v_{i+1}) = \frac{1}{2} \cdot 2\sum_{i=1}^n v_i = \sum_{i=1}^n v_i$.

So sum of sides = sum of vertices = $V$ where $V = \sum v_i$.

Interior = $V/n$.

Total sum = $V + V + V/n = 2V + V/n = V(2 + 1/n) = V(2n+1)/n$.

But total sum = $(2n+1)(a+n)$.

So $V(2n+1)/n = (2n+1)(a+n)$, which gives $V/n = a+n$, i.e., $V = n(a+n)$.

So the interior label = $V/n = a+n$, which is the middle of the $2n+1$ consecutive integers! That's elegant.

So the interior must be labeled with $a+n$, the median of the consecutive integers.

Now, all vertices have the same parity. The $2n+1$ consecutive integers $\{a, a+1, \ldots, a+2n\}$ contain either $n+1$ of one parity and $n$ of the other.

If $a$ is even: the set has $n+1$ even numbers and $n$ odd numbers (since positions $0, 2, 4, \ldots, 2n$ are even, that's $n+1$ evens).

If $a$ is odd: the set has $n+1$ odd numbers and $n$ even numbers.

The vertices all have the same parity. We need $n$ vertices of the same parity. The sides are averages of two same-parity vertices, so sides have the same parity as vertices. Wait, no: if two vertices are both even, their average is even. If both odd, average is odd. So sides have the same parity as the vertices.

So vertices and sides all have the same parity. That's $2n$ labels of the same parity. But the set of $2n+1$ consecutive integers has at most $n+1$ of any given parity. So we need $2n \leq n+1$, i.e., $n \leq 1$. But $n \geq 3$, contradiction!

Wait, that can't be right. Let me reconsider.

Hmm, wait. The sides have the same parity as the vertices only if the average of two same-parity numbers has that parity. Average of two even numbers: $(2k + 2m)/2 = k+m$, which could be even or odd. Average of two odd numbers: $(2k+1 + 2m+1)/2 = k+m+1$, which could be even or odd.

So I was wrong. The sides don't necessarily have the same parity as the vertices.

Let me reconsider. The vertices all have the same parity. Let's say they're all even (WLOG by shifting). Then each side label = $(v_i + v_{i+1})/2$ which is an integer (since both even), but its parity depends on $v_i/2 + v_{i+1}/2$.

OK so let me think more carefully.

The $2n+1$ consecutive integers are $\{a, a+1, \ldots, a+2n\}$.

Vertices: $n$ values, all same parity.
Sides: $n$ values, each = average of two consecutive vertices.
Interior: $a+n$ (the median).

Since the interior is $a+n$, and all labels are distinct, no vertex or side can equal $a+n$.

Let me think about what parities are available. The set has $n+1$ numbers of parity $p$ (where $p$ = parity of $a$) and $n$ numbers of parity $1-p$.

The vertices are all the same parity. Case 1: vertices all have parity $p$ (the majority parity). Then we use $n$ of the $n+1$ numbers with parity $p$ for vertices. The remaining 1 number with parity $p$ and all $n$ numbers with parity $1-p$ are for sides and interior. But interior = $a+n$. What's the parity of $a+n$? It's $p + n \mod 2 = p \oplus (n \mod 2)$.

Hmm, this is getting complicated. Let me think differently.

Actually, let me think about this more carefully using the structure.

Let me shift so that the consecutive integers are $\{0, 1, 2, \ldots, 2n\}$ (i.e., $a = 0$). Then the interior label is $n$.

Vertices are $n$ distinct values from $\{0, 1, \ldots, 2n\} \setminus \{n\}$, all the same parity. Sides are the remaining $n$ values from $\{0, 1, \ldots, 2n\} \setminus \{n\}$, and each side $s_i = (v_i + v_{i+1})/2$.

The sum condition is automatically satisfied (we derived it). So we need:
1. Choose $n$ vertices from $\{0, 1, \ldots, 2n\} \setminus \{n\}$, all same parity.
2. The remaining $n$ values (sides) must be arrangeable as $(v_i + v_{i+1})/2$ for some cyclic ordering of the vertices.

Actually, condition 2 is: the multiset $\{(v_i + v_{i+1})/2 : i = 1, \ldots, n\}$ (for some ordering) equals the set of remaining $n$ values.

Let me think about the parity constraint more. The set $\{0, 1, \ldots, 2n\} \setminus \{n\}$ has $2n$ elements. Among $\{0, 1, \ldots, 2n\}$, there are $n+1$ even and $n$ odd (if $n$ is such that... wait, $\{0, 1, \ldots, 2n\}$ has $n+1$ even numbers ($0, 2, 4, \ldots, 2n$) and $n$ odd numbers ($1, 3, \ldots, 2n-1$)).

After removing $n$: if $n$ is even, we remove an even number, so we have $n$ even and $n$ odd. If $n$ is odd, we remove an odd number, so we have $n+1$ even and $n-1$ odd.

Case 1: $n$ even. Then $\{0, 1, \ldots, 2n\} \setminus \{n\}$ has $n$ even and $n$ odd. Vertices must be all same parity. If vertices are all even, we use all $n$ even numbers. Then sides are all $n$ odd numbers. If vertices are all odd, we use all $n$ odd numbers, sides are all $n$ even numbers.

Case 2: $n$ odd. Then $\{0, 1, \ldots, 2n\} \setminus \{n\}$ has $n+1$ even and $n-1$ odd. Vertices all same parity. If all even: use $n$ of $n+1$ evens, sides = 1 even + $n-1$ odd. If all odd: need $n$ odd but only $n-1$ available. Impossible.

So when $n$ is odd, vertices must be all even, and we choose $n$ of the $n+1$ even numbers (excluding one even number), and the sides consist of that 1 even number plus all $n-1$ odd numbers.

When $n$ is even, either all-even or all-odd vertices work, and sides are the complementary parity.

This is a complex combinatorial problem. Let me think about small cases and try to find a pattern.

Let me try $n = 3$. Consecutive integers $\{0,1,2,3,4,5,6\}$, interior = 3. $n=3$ is odd, so vertices all even, choose 3 from $\{0, 2, 4, 6\}$ (excluding one). Sides = the excluded even + all odds $\{1, 5\}$.

Options for excluded even: 0, 2, 4, or 6.

If we exclude 0: vertices = $\{2, 4, 6\}$. Sides should be $\{0, 1, 5\}$. We need a cyclic ordering of $\{2, 4, 6\}$ such that the averages give $\{0, 1, 5\}$. Averages of pairs: $(2+4)/2 = 3$, $(4+6)/2 = 5$, $(2+6)/2 = 4$. So possible averages are $\{3, 5, 4\}$. But we need $\{0, 1, 5\}$. No match.

If we exclude 2: vertices = $\{0, 4, 6\}$. Sides = $\{2, 1, 5\}$. Averages: $(0+4)/2 = 2$, $(4+6)/2 = 5$, $(0+6)/2 = 3$. So $\{2, 5, 3\}$. Need $\{1, 2, 5\}$. No match (3 ≠ 1).

If we exclude 4: vertices = $\{0, 2, 6\}$. Sides = $\{4, 1, 5\}$. Averages: $(0+2)/2 = 1$, $(2+6)/2 = 4$, $(0+6)/2 = 3$. So $\{1, 4, 3\}$. Need $\{1, 4, 5\}$. No match (3 ≠ 5).

If we exclude 6: vertices = $\{0, 2, 4\}$. Sides = $\{6, 1, 5\}$. Averages: $(0+2)/2 = 1$, $(2+4)/2 = 3$, $(0+4)/2 = 2$. So $\{1, 3, 2\}$. Need $\{1, 5, 6\}$. No match.

So $n = 3$ doesn't work.

Let me try $n = 4$. Consecutive $\{0,1,...,8\}$, interior = 4. $n=4$ even. 

Option A: vertices all even = $\{0, 2, 4, 6, 8\} \setminus \{4\}$ wait, we need to exclude the interior 4. The even numbers in $\{0,...,8\}$ are $\{0, 2, 4, 6, 8\}$, that's 5. Remove 4 (interior), get $\{0, 2, 6, 8\}$. That's 4 vertices. Sides = all odds = $\{1, 3, 5, 7\}$.

We need a cyclic ordering of $\{0, 2, 6, 8\}$ with averages = $\{1, 3, 5, 7\}$.

Averages of pairs:
- $(0+2)/2 = 1$ ✓
- $(0+6)/2 = 3$ ✓
- $(0+8)/2 = 4$ ✗ (not in sides)
- $(2+6)/2 = 4$ ✗
- $(2+8)/2 = 5$ ✓
- $(6+8)/2 = 7$ ✓

We need a Hamiltonian cycle on $\{0, 2, 6, 8\}$ using edges with averages in $\{1, 3, 5, 7\}$. Valid edges: $(0,2) \to 1$, $(0,6) \to 3$, $(2,8) \to 5$, $(6,8) \to 7$.

So the graph has edges: $0-2$, $0-6$, $2-8$, $6-8$. This is a path $6-0-2-8$ and also $6-8$ and $0-6$. Let me draw: edges are $\{0,2\}, \{0,6\}, \{2,8\}, \{6,8\}$. This is a 4-cycle: $0-2-8-6-0$! Averages: $1, 5, 7, 3$. That's $\{1, 3, 5, 7\}$. ✓

So $n = 4$ works!

Let me try $n = 5$. Consecutive $\{0,...,10\}$, interior = 5. $n=5$ odd, vertices all even from $\{0, 2, 4, 6, 8, 10\} \setminus \{5\}$... wait, 5 is odd, so removing 5 doesn't affect the evens. Even numbers: $\{0, 2, 4, 6, 8, 10\}$, that's 6. Choose 5, exclude 1. Sides = excluded even + all odds from $\{0,...,10\}\setminus\{5\}$ = excluded even + $\{1, 3, 7, 9\}$.

So sides have 5 elements: 1 even + 4 odd. Vertices: 5 even numbers.

Let me try excluding 0: vertices = $\{2, 4, 6, 8, 10\}$, sides = $\{0, 1, 3, 7, 9\}$.

Averages of pairs from vertices:
$(2+4)/2=3$, $(2+6)/2=4$, $(2+8)/2=5$, $(2+10)/2=6$, $(4+6)/2=5$, $(4+8)/2=6$, $(4+10)/2=7$, $(6+8)/2=7$, $(6+10)/2=8$, $(8+10)/2=9$.

We need a Hamiltonian cycle on $\{2,4,6,8,10\}$ with edge averages in $\{0,1,3,7,9\}$. Valid edges (average in $\{0,1,3,7,9\}$):
- avg 3: $(2,4)$
- avg 7: $(4,10)$, $(6,8)$
- avg 9: $(8,10)$
- avg 0: impossible (would need two vertices summing to 0, but min is 2)
- avg 1: impossible (would need sum 2, only $0+2$ but 0 not a vertex)

So valid edges: $\{2,4\}, \{4,10\}, \{6,8\}, \{8,10\}$. This gives a path $2-4-10-8-6$ but we need a cycle. $6$ has degree 1 (only connected to 8), $2$ has degree 1 (only connected to 4). Can't form a cycle. Fail.

Try excluding 2: vertices = $\{0, 4, 6, 8, 10\}$, sides = $\{2, 1, 3, 7, 9\}$.

Averages:
$(0+4)/2=2$, $(0+6)/2=3$, $(0+8)/2=4$, $(0+10)/2=5$, $(4+6)/2=5$, $(4+8)/2=6$, $(4+10)/2=7$, $(6+8)/2=7$, $(6+10)/2=8$, $(8+10)/2=9$.

Valid edges (avg in $\{1,2,3,7,9\}$):
- avg 2: $(0,4)$
- avg 3: $(0,6)$
- avg 7: $(4,10)$, $(6,8)$
- avg 9: $(8,10)$
- avg 1: impossible (need sum 2, only $0+2$ but 2 not vertex)

Edges: $\{0,4\}, \{0,6\}, \{4,10\}, \{6,8\}, \{8,10\}$. 

Graph: $0-4-10-8-6-0$. That's a 5-cycle! Averages: $2, 7, 9, 7, 3$. Wait, that gives $\{2, 7, 9, 7, 3\}$ which has a repeat (7 appears twice). But sides must be distinct. So this doesn't work.

Hmm, the issue is that two edges have the same average. Let me check: $(4,10) \to 7$ and $(6,8) \to 7$. Both give 7. So we can't use both in the cycle. But in the 5-cycle $0-4-10-8-6-0$, we use edge $(4,10)$ and edge $(6,8)$... wait, $8-6$ is an edge, giving avg 7. And $4-10$ giving avg 7. So two sides labeled 7, not allowed.

Can we find a different 5-cycle? The edges are $\{0,4\}, \{0,6\}, \{4,10\}, \{6,8\}, \{8,10\}$. 

Possible cycles: $0-4-10-8-6-0$ (uses all 5 edges, but two give 7). Any other Hamiltonian cycle? $0-6-8-10-4-0$: edges $(0,6)\to 3$, $(6,8)\to 7$, $(8,10)\to 9$, $(10,4)\to 7$, $(4,0)\to 2$. Same problem: 7 appears twice.

So excluding 2 doesn't work because of the duplicate average.

Try excluding 4: vertices = $\{0, 2, 6, 8, 10\}$, sides = $\{4, 1, 3, 7, 9\}$.

Averages:
$(0+2)/2=1$, $(0+6)/2=3$, $(0+8)/2=4$, $(0+10)/2=5$, $(2+6)/2=4$, $(2+8)/2=5$, $(2+10)/2=6$, $(6+8)/2=7$, $(6+10)/2=8$, $(8+10)/2=9$.

Valid edges (avg in $\{1,3,4,7,9\}$):
- avg 1: $(0,2)$
- avg 3: $(0,6)$
- avg 4: $(0,8)$, $(2,6)$
- avg 7: $(6,8)$
- avg 9: $(8,10)$

Edges: $\{0,2\}, \{0,6\}, \{0,8\}, \{2,6\}, \{6,8\}, \{8,10\}$.

We need a Hamiltonian cycle using 5 edges with distinct averages from $\{1,3,4,7,9\}$. Note avg 4 comes from two edges: $(0,8)$ and $(2,6)$. We can use at most one of them (since averages must be distinct).

So we need to pick one of $(0,8)$ or $(2,6)$ for avg 4, and then find a cycle.

If we use $(0,8)$ for avg 4: remaining edges needed for avgs 1,3,7,9: $(0,2)$ for 1, $(0,6)$ for 3, $(6,8)$ for 7, $(8,10)$ for 9. But vertex 0 would have degree 3 (edges to 2, 6, 8). In a cycle, each vertex has degree 2. So we can't use all of $(0,2), (0,6), (0,8)$.

We need to choose 5 edges forming a Hamiltonian cycle with distinct averages. The available edges with their averages:
- $(0,2) \to 1$
- $(0,6) \to 3$
- $(0,8) \to 4$
- $(2,6) \to 4$
- $(6,8) \to 7$
- $(8,10) \to 9$

We must use exactly one of $(0,8), (2,6)$ for avg 4. And we need all 5 averages $\{1,3,4,7,9\}$.

If use $(0,8)$ for 4: need edges for 1,3,7,9 = $(0,2), (0,6), (6,8), (8,10)$. Vertex 0 has degree 3. Not a cycle.

If use $(2,6)$ for 4: need edges for 1,3,7,9 = $(0,2), (0,6), (6,8), (8,10)$. Vertex 0 has degree 2 (edges to 2, 6). Vertex 6 has degree 3 (edges to 0, 2, 8). Not a cycle.

So excluding 4 doesn't work.

Try excluding 6: vertices = $\{0, 2, 4, 8, 10\}$, sides = $\{6, 1, 3, 7, 9\}$.

Averages:
$(0+2)/2=1$, $(0+4)/2=2$, $(0+8)/2=4$, $(0+10)/2=5$, $(2+4)/2=3$, $(2+8)/2=5$, $(2+10)/2=6$, $(4+8)/2=6$, $(4+10)/2=7$, $(8+10)/2=9$.

Valid edges (avg in $\{1,3,6,7,9\}$):
- avg 1: $(0,2)$
- avg 3: $(2,4)$
- avg 6: $(2,10)$, $(4,8)$
- avg 7: $(4,10)$
- avg 9: $(8,10)$

Same structure as before. avg 6 from two edges. 

If use $(2,10)$ for 6: edges = $(0,2), (2,4), (2,10), (4,10), (8,10)$. Vertex 2 has degree 3. Not a cycle.

If use $(4,8)$ for 6: edges = $(0,2), (2,4), (4,8), (4,10), (8,10)$. Vertex 4 has degree 3. Not a cycle.

Doesn't work.

Try excluding 8: vertices = $\{0, 2, 4, 6, 10\}$, sides = $\{8, 1, 3, 7, 9\}$.

Averages:
$(0+2)/2=1$, $(0+4)/2=2$, $(0+6)/2=3$, $(0+10)/2=5$, $(2+4)/2=3$, $(2+6)/2=4$, $(2+10)/2=6$, $(4+6)/2=5$, $(4+10)/2=7$, $(6+10)/2=8$.

Valid edges (avg in $\{1,3,7,8,9\}$):
- avg 1: $(0,2)$
- avg 3: $(0,6)$, $(2,4)$
- avg 7: $(4,10)$
- avg 8: $(6,10)$
- avg 9: impossible (need sum 18, max is $6+10=16$)

avg 9 impossible. Fail.

Try excluding 10: vertices = $\{0, 2, 4, 6, 8\}$, sides = $\{10, 1, 3, 7, 9\}$.

Averages:
$(0+2)/2=1$, $(0+4)/2=2$, $(0+6)/2=3$, $(0+8)/2=4$, $(2+4)/2=3$, $(2+6)/2=4$, $(2+8)/2=5$, $(4+6)/2=5$, $(4+8)/2=6$, $(6+8)/2=7$.

Valid edges (avg in $\{1,3,7,9,10\}$):
- avg 1: $(0,2)$
- avg 3: $(0,6)$, $(2,4)$
- avg 7: $(6,8)$
- avg 9: impossible
- avg 10: impossible

Fail.

So $n = 5$ doesn't work.

Let me try $n = 6$. Consecutive $\{0,...,12\}$, interior = 6. $n=6$ even.

Option A: vertices all even. Even numbers in $\{0,...,12\}$: $\{0,2,4,6,8,10,12\}$, that's 7. Remove 6 (interior): $\{0,2,4,8,10,12\}$, 6 vertices. Sides = all odds = $\{1,3,5,7,9,11\}$.

Averages of pairs:
$(0+2)/2=1$, $(0+4)/2=2$, $(0+8)/2=4$, $(0+10)/2=5$, $(0+12)/2=6$, $(2+4)/2=3$, $(2+8)/2=5$, $(2+10)/2=6$, $(2+12)/2=7$, $(4+8)/2=6$, $(4+10)/2=7$, $(4+12)/2=8$, $(8+10)/2=9$, $(8+12)/2=10$, $(10+12)/2=11$.

Valid edges (avg in $\{1,3,5,7,9,11\}$):
- avg 1: $(0,2)$
- avg 3: $(2,4)$
- avg 5: $(0,10)$, $(2,8)$
- avg 7: $(2,12)$, $(4,10)$
- avg 9: $(8,10)$
- avg 11: $(10,12)$

We need a Hamiltonian cycle on $\{0,2,4,8,10,12\}$ with 6 edges having distinct averages $\{1,3,5,7,9,11\}$.

For avg 5: choose $(0,10)$ or $(2,8)$.
For avg 7: choose $(2,12)$ or $(4,10)$.

Let me try $(0,10)$ for 5 and $(4,10)$ for 7. But then vertex 10 has degree 2 from these two edges. Remaining: avg 1: $(0,2)$, avg 3: $(2,4)$, avg 9: $(8,10)$, avg 11: $(10,12)$. But vertex 10 would have degree 4. No.

Try $(0,10)$ for 5 and $(2,12)$ for 7. Edges: $(0,10), (2,12), (0,2), (2,4), (8,10), (10,12)$. Vertex 0: degree 2 (to 10, 2). Vertex 2: degree 3 (to 12, 0, 4). Not a cycle.

Try $(2,8)$ for 5 and $(4,10)$ for 7. Edges: $(2,8), (4,10), (0,2), (2,4), (8,10), (10,12)$. Vertex 2: degree 3 (to 8, 0, 4). Vertex 10: degree 3 (to 4, 8, 12). Not a cycle.

Try $(2,8)$ for 5 and $(2,12)$ for 7. Edges: $(2,8), (2,12), (0,2), (2,4), (8,10), (10,12)$. Vertex 2: degree 4. No.

Hmm, all combinations for avg 5 and 7 lead to problems. Let me think more carefully.

We need each vertex to have degree exactly 2 in the cycle. Let's think about which edges each vertex can be part of:

- Vertex 0: can connect via avg 1 ($(0,2)$), avg 5 ($(0,10)$), or avg 6 (not in set). So vertex 0 has possible edges: $(0,2) \to 1$, $(0,10) \to 5$.
- Vertex 2: $(0,2) \to 1$, $(2,4) \to 3$, $(2,8) \to 5$, $(2,12) \to 7$.
- Vertex 4: $(2,4) \to 3$, $(4,10) \to 7$.
- Vertex 8: $(2,8) \to 5$, $(8,10) \to 9$.
- Vertex 10: $(0,10) \to 5$, $(4,10) \to 7$, $(8,10) \to 9$, $(10,12) \to 11$.
- Vertex 12: $(2,12) \to 7$, $(10,12) \to 11$.

For a Hamiltonian cycle, each vertex has degree 2. Vertex 0 has only 2 possible edges: $(0,2)$ and $(0,10)$. So both must be used! That means avg 1 uses $(0,2)$ and avg 5 uses $(0,10)$.

Vertex 12 has only 2 possible edges: $(2,12)$ and $(10,12)$. So both must be used! avg 7 uses $(2,12)$ and avg 11 uses $(10,12)$.

Vertex 4 has only 2 possible edges: $(2,4)$ and $(4,10)$. So both must be used! avg 3 uses $(2,4)$ and avg 7 uses $(4,10)$.

But we already assigned avg 7 to $(2,12)$! And avg 7 can only be used once. Contradiction.

So Option A (all even vertices) doesn't work for $n=6$.

Option B: vertices all odd. Odd numbers in $\{0,...,12\}$: $\{1,3,5,7,9,11\}$, that's 6. All are vertices (none is the interior 6). Sides = all even numbers except 6 = $\{0,2,4,8,10,12\}$.

Averages of pairs from $\{1,3,5,7,9,11\}$:
$(1+3)/2=2$, $(1+5)/2=3$, $(1+7)/2=4$, $(1+9)/2=5$, $(1+11)/2=6$, $(3+5)/2=4$, $(3+7)/2=5$, $(3+9)/2=6$, $(3+11)/2=7$, $(5+7)/2=6$, $(5+9)/2=7$, $(5+11)/2=8$, $(7+9)/2=8$, $(7+11)/2=9$, $(9+11)/2=10$.

Valid edges (avg in $\{0,2,4,8,10,12\}$):
- avg 0: impossible
- avg 2: $(1,3)$
- avg 4: $(1,7)$, $(3,5)$
- avg 8: $(5,11)$, $(7,9)$
- avg 10: $(9,11)$
- avg 12: impossible

avg 0 and avg 12 impossible. Fail.

So $n = 6$ doesn't work.

Let me try $n = 7$. Consecutive $\{0,...,14\}$, interior = 7. $n=7$ odd, vertices all even.

Even numbers in $\{0,...,14\}$: $\{0,2,4,6,8,10,12,14\}$, 8 numbers. Remove 7 (interior, odd, doesn't affect). Choose 7 of 8 evens, exclude 1. Sides = excluded even + all odds from $\{0,...,14\}\setminus\{7\}$ = excluded even + $\{1,3,5,9,11,13\}$.

So sides = {excluded even} ∪ {1,3,5,9,11,13}, 7 elements.

This is getting complex. Let me think about this more systematically.

Actually, let me think about what structure is needed. The key insight is:

We need a Hamiltonian cycle on $n$ vertices (all same parity) such that the $n$ edge averages are exactly the $n$ side labels (all distinct).

Let me think about this differently. Let's say the vertices are $v_1, v_2, \ldots, v_n$ in cyclic order. The side labels are $s_i = (v_i + v_{i+1})/2$.

The sum of side labels = sum of vertex labels = $V$. We already know this is satisfied.

Another constraint: the side labels and vertex labels partition $\{0, 1, \ldots, 2n\} \setminus \{n\}$.

Let me think about $n = 4$ which worked. The cycle was $0-2-8-6-0$ (wait, let me recheck). Actually I had vertices $\{0, 2, 6, 8\}$ and the cycle $0-2-8-6-0$ with averages $1, 5, 7, 3$. Sides = $\{1, 3, 5, 7\}$. ✓

Let me try to find a pattern. For $n = 4$, the vertices are $\{0, 2, 6, 8\}$ and the cycle goes $0, 2, 8, 6$. Note that $0, 2$ are close together and $6, 8$ are close together, and the cycle alternates between the two clusters.

Let me think about this problem more carefully. Maybe I should look for which $n$ work by trying to construct solutions.

Let me think about the problem in terms of a graph. We have $n$ vertices with values, and we need a Hamiltonian cycle where edge labels (averages) are all distinct and form a specific set.

Actually, let me think about it differently. Let me consider the problem modulo small numbers or look for structural obstructions.

Let me reconsider. The vertices are all even (when $n$ is odd) or all same parity (when $n$ is even). Let me write vertices as $2a_1, 2a_2, \ldots, 2a_n$ (when all even) where $a_i$ are distinct integers. Then side labels are $a_i + a_{i+1}$.

When all even: vertices = $\{2a_1, \ldots, 2a_n\}$, sides = $\{a_i + a_{i+1}\}$, interior = $n$.

The set $\{0, 1, \ldots, 2n\}$: even numbers are $\{0, 2, \ldots, 2n\}$, i.e., $\{2 \cdot 0, 2 \cdot 1, \ldots, 2 \cdot n\}$. So $a_i \in \{0, 1, \ldots, n\}$.

When $n$ is odd: we choose $n$ of the $n+1$ values $\{0, 1, \ldots, n\}$ for $a_i$ (excluding one, say $a^*$), and the sides are $a_i + a_{i+1}$ which must be the remaining $n$ values from $\{0, 1, \ldots, 2n\} \setminus \{n\}$ that are not even (i.e., the odd values) plus $2a^*$ (the excluded even number).

Wait, let me redo this. The full set is $\{0, 1, \ldots, 2n\}$. Interior = $n$. The remaining $2n$ values are $\{0, 1, \ldots, 2n\} \setminus \{n\}$.

When vertices are all even: vertices = $\{2a_1, \ldots, 2a_n\}$ where $\{a_1, \ldots, a_n\} \subset \{0, 1, \ldots, n\}$, $|a_i| = n$, all distinct. The excluded value from $\{0, \ldots, n\}$ is some $a^*$, so $\{a_1, \ldots, a_n\} = \{0, \ldots, n\} \setminus \{a^*\}$.

The sides are $a_i + a_{i+1}$ (for the cyclic ordering). These must be the $n$ values in $\{0, 1, \ldots, 2n\} \setminus \{n\} \setminus \{2a_1, \ldots, 2a_n\}$.

The even values in $\{0, \ldots, 2n\} \setminus \{n\}$ are $\{0, 2, \ldots, 2n\} \setminus \{n\}$ if $n$ is even, or $\{0, 2, \ldots, 2n\} \setminus \{n\}$ ... hmm, $n$ could be even or odd.

Let me separate cases.

Case $n$ odd: $n$ is odd, so $n$ is not even, meaning $n \notin \{0, 2, 4, \ldots, 2n\}$. The even values in $\{0, \ldots, 2n\} \setminus \{n\}$ are $\{0, 2, 4, \ldots, 2n\}$ (all $n+1$ of them). The odd values are $\{1, 3, \ldots, 2n-1\} \setminus \{n\} = \{1, 3, \ldots, 2n-1\} \setminus \{n\}$. Since $n$ is odd, $n \in \{1, 3, \ldots, 2n-1\}$. So odd values in the remaining set: $\{1, 3, \ldots, 2n-1\} \setminus \{n\}$, which has $n - 1$ elements.

Vertices (all even) = $n$ of the $n+1$ even values. Sides = the remaining 1 even value + all $n-1$ odd values.

In terms of $a_i$: vertices = $\{2a : a \in \{0,\ldots,n\} \setminus \{a^*\}\}$, sides = $\{2a^*\} \cup \{1, 3, \ldots, 2n-1\} \setminus \{n\}$.

The side values $a_i + a_{i+1}$ must equal this set. Note $a_i + a_{i+1}$ ranges from $0$ to $2n$ (since $a_i \in \{0, \ldots, n\}$). The side set has one even value $2a^*$ and $n-1$ odd values. Since $a_i + a_{i+1}$ has the same parity as $a_i + a_{i+1}$... well, $a_i + a_{i+1}$ is even iff $a_i$ and $a_{i+1}$ have the same parity.

So exactly one pair of consecutive $a_i$'s has the same parity (giving the even side $2a^*$), and the rest have different parities (giving odd sides).

Case $n$ even: $n$ is even, so $n \in \{0, 2, \ldots, 2n\}$. Even values in $\{0,\ldots,2n\}\setminus\{n\}$: $\{0, 2, \ldots, 2n\} \setminus \{n\}$, which has $n$ elements. Odd values: $\{1, 3, \ldots, 2n-1\}$, $n$ elements.

Sub-case vertices all even: vertices = $n$ even values = all even values in $\{0,...,2n\}\setminus\{n\}$ = $\{0, 2, \ldots, 2n\} \setminus \{n\}$. In terms of $a_i$: $\{a_1, \ldots, a_n\} = \{0, 1, \ldots, n\} \setminus \{n/2\}$ (since $n = 2 \cdot (n/2)$). Sides = all $n$ odd values = $\{1, 3, \ldots, 2n-1\}$.

So $a_i + a_{i+1}$ must be odd for all $i$, meaning consecutive $a_i$'s alternate in parity. This is possible iff $n$ is even (which it is in this case). And the sums $a_i + a_{i+1}$ must be exactly $\{1, 3, 5, \ldots, 2n-1\}$.

Sub-case vertices all odd: vertices = $\{1, 3, \ldots, 2n-1\}$ (all $n$ odd values). Write $v_i = 2b_i + 1$ where $b_i \in \{0, 1, \ldots, n-1\}$. Side = $(v_i + v_{i+1})/2 = b_i + b_{i+1} + 1$. Sides = $\{0, 2, \ldots, 2n\} \setminus \{n\}$ = $\{0, 2, \ldots, 2n\} \setminus \{n\}$, which are the $n$ even values excluding $n$.

So $b_i + b_{i+1} + 1 \in \{0, 2, \ldots, 2n\} \setminus \{n\}$, i.e., $b_i + b_{i+1} \in \{-1, 1, 3, \ldots, 2n-1\} \setminus \{n-1\}$. But $b_i \geq 0$, so $b_i + b_{i+1} \geq 0$. So $b_i + b_{i+1} \in \{1, 3, 5, \ldots, 2n-1\} \setminus \{n-1\}$. Since $n$ is even, $n-1$ is odd, so $n-1 \in \{1, 3, \ldots, 2n-1\}$. So the target set is $\{1, 3, \ldots, 2n-1\} \setminus \{n-1\}$, which has $n-1$ elements. But we need $n$ sides. Contradiction! Unless... wait, let me recount.

Sides = $\{0, 2, \ldots, 2n\} \setminus \{n\}$. This has $n+1 - 1 = n$ elements. $b_i + b_{i+1} + 1$ ranges over these, so $b_i + b_{i+1}$ ranges over $\{-1, 1, 3, \ldots, 2n-1\} \setminus \{n-1\}$. Since $b_i \geq 0$, $b_i + b_{i+1} \geq 0$, so we need $b_i + b_{i+1} \in \{1, 3, \ldots, 2n-1\} \setminus \{n-1\}$. This set has $n - 1$ elements (since $\{1, 3, \ldots, 2n-1\}$ has $n$ elements and we remove $n-1$). But we need $n$ distinct values. $n > n-1$, so impossible!

Wait, that means when $n$ is even and vertices are all odd, it's impossible. Let me double-check with $n = 4$.

$n = 4$: vertices all odd = $\{1, 3, 5, 7\}$. $b_i \in \{0, 1, 2, 3\}$. Sides = $\{0, 2, 4, 6, 8\} \setminus \{4\} = \{0, 2, 6, 8\}$. $b_i + b_{i+1} + 1 \in \{0, 2, 6, 8\}$, so $b_i + b_{i+1} \in \{-1, 1, 5, 7\}$. Since $b_i \geq 0$, need $b_i + b_{i+1} \in \{1, 5, 7\}$. That's 3 values but we need 4 sides. Indeed impossible.

So for $n$ even, only the all-even vertices sub-case is possible.

Great, so let me focus on the all-even vertices case for all $n$.

For $n$ even: $\{a_1, \ldots, a_n\} = \{0, 1, \ldots, n\} \setminus \{n/2\}$. Sides = $\{a_i + a_{i+1}\} = \{1, 3, 5, \ldots, 2n-1\}$ (all odd numbers from 1 to $2n-1$). Need a Hamiltonian cycle on $\{0, 1, \ldots, n\} \setminus \{n/2\}$ with edge sums being exactly $\{1, 3, 5, \ldots, 2n-1\}$, all distinct.

For $n$ odd: $\{a_1, \ldots, a_n\} = \{0, 1, \ldots, n\} \setminus \{a^*\}$ for some $a^*$. Sides = $\{a_i + a_{i+1}\} = \{2a^*\} \cup (\{1, 3, \ldots, 2n-1\} \setminus \{n\})$. Need a Hamiltonian cycle with these edge sums.

This is now a cleaner formulation. Let me think about necessary conditions.

For $n$ even: We need a cyclic arrangement of $\{0, 1, \ldots, n\} \setminus \{n/2\}$ such that the $n$ consecutive sums are exactly $\{1, 3, 5, \ldots, 2n-1\}$.

The sum of all edge sums = $\sum (a_i + a_{i+1}) = 2\sum a_i = 2 \cdot (\sum_{k=0}^{n} k - n/2) = 2 \cdot (n(n+1)/2 - n/2) = 2 \cdot n^2/2 = n^2$.

Sum of $\{1, 3, \ldots, 2n-1\} = n^2$. ✓ So the sum condition is automatically satisfied.

For $n$ odd: Sum of edge sums = $2\sum a_i = 2(\sum_{k=0}^n k - a^*) = 2(n(n+1)/2 - a^*) = n(n+1) - 2a^*$.

Sum of sides = $2a^* + \sum_{k \in \{1,3,...,2n-1\} \setminus \{n\}} k = 2a^* + (n^2 - n)$.

So $n(n+1) - 2a^* = 2a^* + n^2 - n$, giving $n^2 + n - 2a^* = 2a^* + n^2 - n$, so $2n = 4a^*$, so $a^* = n/2$.

But $n$ is odd, so $n/2$ is not an integer! Contradiction!

Wait, this means for $n$ odd, there's no solution? Let me double-check.

For $n$ odd, $a^* = n/2$ which is not an integer. So there's no valid $a^*$, meaning no memorable labelling exists for odd $n$?

But wait, I need to double-check my derivation. Let me recheck for $n$ odd.

We have $a^* \in \{0, 1, \ldots, n\}$, and $\{a_1, \ldots, a_n\} = \{0, 1, \ldots, n\} \setminus \{a^*\}$.

Sum of edge sums = $2 \sum a_i = 2(n(n+1)/2 - a^*) = n(n+1) - 2a^*$.

The sides are $\{2a^*\} \cup (\{1, 3, \ldots, 2n-1\} \setminus \{n\})$.

Sum of sides = $2a^* + \sum(\{1, 3, \ldots, 2n-1\} \setminus \{n\}) = 2a^* + (n^2 - n)$.

Setting equal: $n(n+1) - 2a^* = 2a^* + n^2 - n$
$n^2 + n - 2a^* = n^2 - n + 2a^*$
$2n = 4a^*$
$a^* = n/2$.

Since $n$ is odd, $a^*$ is not an integer. So no solution exists for odd $n$.

Wait, but I should also check: could the vertices be all odd when $n$ is odd? Earlier I showed that when $n$ is odd, the set $\{0,...,2n\}\setminus\{n\}$ has $n+1$ even and $n-1$ odd values. For all-odd vertices, we need $n$ odd values but only $n-1$ are available. So indeed impossible.

So for odd $n$, no memorable labelling exists. 

Now for even $n$, we need a cyclic arrangement of $\{0, 1, \ldots, n\} \setminus \{n/2\}$ such that consecutive sums are exactly $\{1, 3, 5, \ldots, 2n-1\}$.

Let me think about when this is possible. Let me denote $m = n/2$, so $n = 2m$ and we need a cyclic arrangement of $\{0, 1, \ldots, 2m\} \setminus \{m\}$ with consecutive sums being $\{1, 3, 5, \ldots, 4m-1\}$.

The set $\{0, 1, \ldots, 2m\} \setminus \{m\}$ has $2m$ elements. We need $2m$ consecutive sums, all odd, being $\{1, 3, \ldots, 4m-1\}$.

For consecutive sums to be odd, consecutive elements must have different parities. So the cycle must alternate even and odd. The set $\{0, 1, \ldots, 2m\} \setminus \{m\}$ has:
- Even numbers: $\{0, 2, \ldots, 2m\}$, that's $m+1$ numbers. If $m$ is even, removing $m$ gives $m$ even numbers. If $m$ is odd, $m$ is not even, so still $m+1$ even numbers.
- Odd numbers: $\{1, 3, \ldots, 2m-1\}$, that's $m$ numbers. If $m$ is even, $m$ is not odd, so still $m$ odd numbers. If $m$ is odd, removing $m$ gives $m-1$ odd numbers.

For the cycle to alternate even/odd, we need equal numbers of even and odd elements. So:
- If $m$ even: $m$ even, $m$ odd. ✓
- If $m$ odd: $m+1$ even, $m-1$ odd. $m+1 \neq m-1$ (unless $m = 0$). ✗

So for $m$ odd (i.e., $n = 2m$ with $m$ odd, i.e., $n \equiv 2 \pmod{4}$), the cycle can't alternate, so no solution.

For $m$ even (i.e., $n \equiv 0 \pmod{4}$), we have $m$ even and $m$ odd elements, and we need an alternating cycle with sums $\{1, 3, \ldots, 4m-1\}$.

So necessary conditions so far: $n$ must be divisible by 4.

But is divisibility by 4 sufficient? Let me check $n = 4$ ($m = 2$): we already found it works.

Let me check $n = 8$ ($m = 4$): We need a cyclic arrangement of $\{0,1,2,3,5,6,7,8\}$ (removing 4) with consecutive sums = $\{1,3,5,7,9,11,13,15\}$.

Let me try to construct this. We need alternating even/odd. Even numbers: $\{0, 2, 6, 8\}$. Odd numbers: $\{1, 3, 5, 7\}$.

The cycle alternates: even, odd, even, odd, even, odd, even, odd.

Consecutive sums (even + odd) must be $\{1, 3, 5, 7, 9, 11, 13, 15\}$.

Let me think of it as a bipartite graph: even vertices on one side, odd on the other. Edges connect even $e$ to odd $o$ with label $e + o$. We need a Hamiltonian cycle in this bipartite graph using each label exactly once.

Even vertices: $\{0, 2, 6, 8\}$. Odd vertices: $\{1, 3, 5, 7\}$.

Possible edges (even + odd):
- $0+1=1$, $0+3=3$, $0+5=5$, $0+7=7$
- $2+1=3$, $2+3=5$, $2+5=7$, $2+7=9$
- $6+1=7$, $6+3=9$, $6+5=11$, $6+7=13$
- $8+1=9$, $8+3=11$, $8+5=13$, $8+7=15$

We need to use labels $\{1,3,5,7,9,11,13,15\}$, each exactly once. Each even vertex has degree 2 in the cycle, each odd vertex has degree 2.

Label 1: only $0+1$. So edge $(0,1)$ must be used.
Label 15: only $8+7$. So edge $(8,7)$ must be used.

Label 3: $0+3$ or $2+1$.
Label 5: $0+5$ or $2+3$.
Label 7: $0+7$, $2+5$, or $6+1$.
Label 9: $2+7$, $6+3$, or $8+1$.
Label 11: $6+5$ or $8+3$.
Label 13: $6+7$ or $8+5$.

Vertex 0 already has edge to 1 (label 1). Needs one more edge. Options: $0+3=3$, $0+5=5$, $0+7=7$.
Vertex 8 already has edge to 7 (label 15). Needs one more edge. Options: $8+1=9$, $8+3=11$, $8+5=13$.
Vertex 1 already has edge to 0 (label 1). Needs one more edge. Options: $2+1=3$, $6+1=7$, $8+1=9$.
Vertex 7 already has edge to 8 (label 15). Needs one more edge. Options: $0+7=7$, $2+7=9$, $6+7=13$.

Let me try: vertex 0 connects to 1 (label 1) and 5 (label 5). Vertex 8 connects to 7 (label 15) and 3 (label 11).

Then vertex 1 has edges to 0 (label 1) and needs one more: $2+1=3$, $6+1=7$, $8+1=9$. But 8 already has 2 edges (to 7 and 3). So $8+1$ not available. Options: $2+1=3$ or $6+1=7$.

Vertex 7 has edges to 8 (label 15) and needs one more: $0+7=7$, $2+7=9$, $6+7=13$. But 0 already has 2 edges. So $0+7$ not available. Options: $2+7=9$ or $6+7=13$.

Vertex 5 has edge to 0 (label 5) and needs one more: $2+5=7$, $6+5=11$. But 11 is used by $8+3$. So $6+5=11$ conflicts. Option: $2+5=7$.

Vertex 3 has edge to 8 (label 11) and needs one more: $2+3=5$ (but 5 is used by $0+5$), $6+3=9$. So $6+3=9$.

Now: vertex 5 connects to 0 and 2 (label 7). Vertex 3 connects to 8 and 6 (label 9).
Vertex 2 has edge to 5 (label 7). Needs one more: $2+1=3$, $2+3=5$ (used), $2+7=9$ (used). So $2+1=3$.
Vertex 6 has edge to 3 (label 9). Needs one more: $6+1=7$ (used), $6+5=11$ (used), $6+7=13$. So $6+7=13$.

Now vertex 1 has edges to 0 (label 1) and 2 (label 3). ✓ Degree 2.
Vertex 7 has edges to 8 (label 15) and 6 (label 13). ✓ Degree 2.

Let me verify all labels: 1 (0+1), 5 (0+5), 7 (2+5), 3 (2+1), 11 (8+3), 9 (6+3), 13 (6+7), 15 (8+7). That's $\{1,3,5,7,9,11,13,15\}$. ✓

The cycle: $0 - 1 - 2 - 5 - 0$? No wait, let me trace the cycle.

Edges: $(0,1), (0,5), (2,5), (1,2), (8,3), (6,3), (6,7), (8,7)$.

Starting from 0: $0 - 1 - 2 - 5 - 0$. That's a 4-cycle, not an 8-cycle!

And $8 - 3 - 6 - 7 - 8$. That's another 4-cycle.

We need a single 8-cycle, not two 4-cycles! So this particular assignment doesn't work.

Let me try a different assignment. We need to ensure the graph forms a single cycle, not multiple cycles.

Let me try to be more careful. We need a Hamiltonian cycle in the bipartite graph. Let me think of it as: arrange the even vertices $e_1, e_2, e_3, e_4$ and odd vertices $o_1, o_2, o_3, o_4$ in a cycle $e_1 - o_1 - e_2 - o_2 - e_3 - o_3 - e_4 - o_4 - e_1$.

The sums are $e_1+o_1, e_2+o_1, e_2+o_2, e_3+o_2, e_3+o_3, e_4+o_3, e_4+o_4, e_1+o_4$.

These must be $\{1,3,5,7,9,11,13,15\}$.

Let me try: $e_1=0, o_1=1, e_2=8, o_2=7, e_3=2, o_3=5, e_4=6, o_4=3$.

Sums: $0+1=1, 8+1=9, 8+7=15, 2+7=9$... duplicate 9. No.

Let me try: $e_1=0, o_1=1, e_2=6, o_2=3, e_3=8, o_3=7, e_4=2, o_4=5$.

Sums: $0+1=1, 6+1=7, 6+3=9, 8+3=11, 8+7=15, 2+7=9$... duplicate 9. No.

Let me try: $e_1=0, o_1=1, e_2=6, o_2=5, e_3=2, o_3=7, e_4=8, o_4=3$.

Sums: $0+1=1, 6+1=7, 6+5=11, 2+5=7$... duplicate 7. No.

Let me try: $e_1=0, o_1=3, e_2=2, o_2=5, e_3=6, o_3=7, e_4=8, o_4=1$.

Sums: $0+3=3, 2+3=5, 2+5=7, 6+5=11, 6+7=13, 8+7=15, 8+1=9, 0+1=1$.
Labels: $\{3,5,7,11,13,15,9,1\} = \{1,3,5,7,9,11,13,15\}$. ✓

And the cycle is $0 - 3 - 2 - 5 - 6 - 7 - 8 - 1 - 0$. That's a single 8-cycle! ✓

So $n = 8$ works.

Let me check $n = 12$ ($m = 6$, but $m$ is odd, so $n \equiv 0 \pmod{4}$... wait, $n = 12$, $m = 6$, $m$ is even. $n = 4m' $ where $m' = 3$... hmm let me re-examine.

Wait, I had $n = 2m$ and the condition is $m$ even, i.e., $n \equiv 0 \pmod{4}$. $n = 12$: $m = 6$, which is even. ✓ So $n = 12$ should be feasible.

Actually wait, let me re-examine. $n = 12$, $m = n/2 = 6$. The set is $\{0, 1, \ldots, 12\} \setminus \{6\}$. Even numbers: $\{0, 2, 4, 8, 10, 12\}$ (6 numbers, since we removed 6 which is even). Odd numbers: $\{1, 3, 5, 7, 9, 11\}$ (6 numbers). So 6 even and 6 odd, alternating cycle possible. ✓

Now, the question is: for which multiples of 4 does a solution exist? Let me think about whether $n \equiv 0 \pmod 4$ is both necessary and sufficient.

We've shown:
- $n$ odd: impossible (sum condition gives $a^* = n/2 \notin \mathbb{Z}$)
- $n \equiv 2 \pmod 4$: impossible (can't alternate parities)
- $n \equiv 0 \pmod 4$: necessary conditions satisfied, and we've verified $n = 4$ and $n = 8$ work.

Is $n \equiv 0 \pmod 4$ sufficient? Let me try to construct a general solution.

For $n = 4k$, $m = 2k$. The set is $\{0, 1, \ldots, 4k\} \setminus \{2k\}$. Even numbers: $\{0, 2, \ldots, 4k\} \setminus \{2k\}$, which is $\{0, 2, \ldots, 2k-2, 2k+2, \ldots, 4k\}$, $2k$ numbers. Odd numbers: $\{1, 3, \ldots, 4k-1\}$, $2k$ numbers.

We need an alternating cycle with sums $\{1, 3, 5, \ldots, 8k-1\}$.

Let me think about a construction. Consider the cycle for $n = 8$ ($k = 2$): $0, 3, 2, 5, 6, 7, 8, 1$ (and back to 0). The sums are $3, 5, 7, 11, 13, 15, 9, 1$.

Hmm, let me think about a pattern. For $n = 4$ ($k = 1$): $0, 1, 4, 3$ (and back to 0). Sums: $1, 5, 7, 3$. Wait, let me recheck. The vertices in the $a$-representation are $\{0, 1, 2, 3\}$ (removing $m = 2$). The cycle was $0, 1, 4, 3$... no, wait. For $n = 4$, $m = 2$, the set is $\{0, 1, 3, 4\}$ (removing 2). The cycle I found earlier in the original representation was $0, 2, 8, 6$ which in $a$-representation is $0, 1, 4, 3$. Sums: $0+1=1, 1+4=5, 4+3=7, 3+0=3$. Labels $\{1, 3, 5, 7\}$. ✓

For $n = 8$: cycle in $a$-representation: $0, 3, 2, 5, 6, 7, 8, 1$. Sums: $3, 5, 7, 11, 13, 15, 9, 1$. ✓

Let me see if there's a pattern. For $n = 4$: $0, 1, 4, 3$. For $n = 8$: $0, 3, 2, 5, 6, 7, 8, 1$.

Hmm, let me think about this differently. Maybe I should look for a general construction.

Actually, let me think about it as follows. We have even numbers $E = \{0, 2, \ldots, 2k-2, 2k+2, \ldots, 4k\}$ and odd numbers $O = \{1, 3, \ldots, 4k-1\}$, each of size $2k$. We need a perfect matching-like structure (actually a 2-regular bipartite graph forming a single cycle) where the $4k$ edge sums are exactly $\{1, 3, 5, \ldots, 8k-1\}$.

Let me think of the even numbers as $e_i = 2i$ for $i \in \{0, 1, \ldots, 2k-1, 2k+1, \ldots, 4k\}$... no, that's not right. Let me re-index.

Even numbers: $\{0, 2, 4, \ldots, 2k-2\} \cup \{2k+2, 2k+4, \ldots, 4k\}$. In terms of $a$-values (dividing by 2): $\{0, 1, \ldots, k-1\} \cup \{k+1, k+2, \ldots, 2k\}$.

Odd numbers: $\{1, 3, 5, \ldots, 4k-1\}$. In terms of $b$-values (where odd = $2b+1$, $b = 0, 1, \ldots, 2k-1$): $\{0, 1, \ldots, 2k-1\}$.

Edge sum = even + odd = $2a + (2b+1) = 2(a+b) + 1$. We need these to be $\{1, 3, 5, \ldots, 8k-1\}$, i.e., $a + b \in \{0, 1, 2, \ldots, 4k-1\}$.

So we need a Hamiltonian cycle in the bipartite graph between $A = \{0, 1, \ldots, k-1, k+1, \ldots, 2k\}$ and $B = \{0, 1, \ldots, 2k-1\}$ where edge $(a, b)$ has label $a + b$, and we need all labels $\{0, 1, \ldots, 4k-1\}$ to appear exactly once.

This is equivalent to finding a Hamiltonian cycle in a bipartite graph where the edge labels (sums) form a complete set.

Let me think about this as a graceful labeling or something similar.

Actually, this reminds me of a "Skolem sequence" or "graceful permutation" type problem.

Let me think about it differently. We need to arrange the $A$-values and $B$-values alternately in a cycle: $a_1, b_1, a_2, b_2, \ldots, a_{2k}, b_{2k}, a_1$. The sums $a_i + b_i$ and $a_{i+1} + b_i$ must together form $\{0, 1, \ldots, 4k-1\}$.

Actually, the sums are: $a_1 + b_1, a_2 + b_1, a_2 + b_2, a_3 + b_2, \ldots, a_{2k} + b_{2k}, a_1 + b_{2k}$. These are $4k$ sums that must be $\{0, 1, \ldots, 4k-1\}$.

This is like a "terraces" or "starter" problem in combinatorial design theory.

Let me try to find a pattern by examining the solutions for $k = 1$ and $k = 2$.

$k = 1$ ($n = 4$): $A = \{0, 2\}$, $B = \{0, 1\}$. Cycle: $a = (0, 2)$, $b = (1, 0)$. Sums: $0+1=1, 2+1=3, 2+0=2, 0+0=0$. Labels $\{0,1,2,3\}$. ✓

Wait, but I need to check: the cycle is $0, 1, 2, 0$ (in terms of $a, b$ values). Going back to original: even values $0, 4$ and odd values $3, 1$. Cycle: $0, 3, 4, 1$. Sums (in original): $0+3=3, 4+3=7, 4+1=5, 0+1=1$. Labels $\{1,3,5,7\}$. ✓

$k = 2$ ($n = 8$): $A = \{0, 1, 3, 4\}$, $B = \{0, 1, 2, 3\}$. Cycle: $a = (0, 2, 3, 4)$... wait, $A = \{0, 1, 3, 4\}$ (removing 2). Let me use the cycle $0, 3, 2, 5, 6, 7, 8, 1$ from before. In $a, b$ terms: even values are $0, 6, 4, 8$ (dividing by 2: $0, 3, 2, 4$) and odd values are $7, 5, 15, 1$ (so $b = 3, 2, 7, 0$). Hmm, this is getting confusing.

Let me just try to find a general construction or prove sufficiency.

Actually, let me think about this problem from a higher level. The question asks for the sum of all $n$ in $[3, 100]$ for which a memorable labelling exists. If the answer is "all multiples of 4 in $[3, 100]$", then the sum is $4 + 8 + 12 + \cdots + 100 = 4(1 + 2 + \cdots + 25) = 4 \cdot 325 = 1300$.

But I need to verify that all multiples of 4 work, not just 4 and 8.

Let me try $n = 12$ ($k = 3$). $A = \{0,1,2,4,5,6\}$ (removing 3), $B = \{0,1,2,3,4,5\}$. Need cycle with sums $\{0,1,\ldots,11\}$.

Let me try to construct this. I need to arrange 6 $A$-values and 6 $B$-values alternately.

Let me try: $a = (0, 2, 4, 6, 5, 1)$, $b = (0, 1, 3, 5, 4, 2)$.

Sums: $a_1+b_1 = 0, a_2+b_1 = 2, a_2+b_2 = 3, a_3+b_2 = 5, a_3+b_3 = 7, a_4+b_3 = 9, a_4+b_4 = 11, a_5+b_4 = 10, a_5+b_5 = 9$... duplicate 9. No.

This trial and error is slow. Let me think more systematically.

Actually, let me think about this as follows. We need a permutation $\sigma$ of $A$ and $\tau$ of $B$ such that the $4k$ values $\{\sigma(i) + \tau(i), \sigma(i+1) + \tau(i) : i = 1, \ldots, 2k\}$ (with cyclic indexing) are exactly $\{0, 1, \ldots, 4k-1\}$.

Equivalently, if we write the cycle as $a_1, b_1, a_2, b_2, \ldots, a_{2k}, b_{2k}$, the sums $a_i + b_i$ (for $i = 1, \ldots, 2k$) and $a_{i+1} + b_i$ (for $i = 1, \ldots, 2k$, with $a_{2k+1} = a_1$) must be $\{0, 1, \ldots, 4k-1\}$.

Note that $a_i + b_i$ and $a_{i+1} + b_i$ share $b_i$. Their difference is $a_{i+1} - a_i$.

Hmm, let me think about a different approach. Let me consider the "differences" $d_i = a_{i+1} - a_i$ (cyclically). Then the sums are $a_i + b_i$ and $a_i + d_i + b_i = (a_i + b_i) + d_i$. So the $4k$ sums come in pairs: $s_i$ and $s_i + d_i$ where $s_i = a_i + b_i$.

We need $\{s_i, s_i + d_i : i = 1, \ldots, 2k\} = \{0, 1, \ldots, 4k-1\}$.

Also, the $b$-values are a permutation of $B$, and $b_i = s_i - a_i$. The $a$-values are a permutation of $A$.

This is still complex. Let me try a different approach: look for a constructive pattern.

For $k = 1$: cycle in $(a,b)$ terms: $a = (0, 2), b = (1, 0)$. Sums: $(0+1, 2+1, 2+0, 0+0) = (1, 3, 2, 0)$. All of $\{0,1,2,3\}$. ✓

For $k = 2$: Let me find the $(a,b)$ representation. The cycle was $0, 3, 2, 5, 6, 7, 8, 1$ in the original $a$-representation (where vertices are $2a$). Wait, I need to be more careful.

For $n = 8$, the original vertex values (in the $\{0,...,16\}$ representation) are even numbers. The $a$-values (dividing by 2) are from $\{0, 1, 2, 3, 5, 6, 7, 8\}$ (removing 4). The cycle in $a$-values: $0, 3, 2, 5, 6, 7, 8, 1$.

Now, the even $a$-values are $\{0, 2, 6, 8\}$ and odd $a$-values are $\{1, 3, 5, 7\}$. The cycle alternates: $0$ (even), $3$ (odd), $2$ (even), $5$ (odd), $6$ (even), $7$ (odd), $8$ (even), $1$ (odd). ✓

In the $(a, b)$ representation where $a$ = even $a$-value / 1 (i.e., the even $a$-values themselves) and $b$ = (odd $a$-value - 1)/2:

Even $a$-values: $0, 2, 6, 8$. These are the $A$-set: $\{0, 1, 3, 4\}$ (dividing by 2).
Odd $a$-values: $3, 5, 7, 1$. These correspond to $B$-set: $(3-1)/2 = 1, (5-1)/2 = 2, (7-1)/2 = 3, (1-1)/2 = 0$. So $B$-order: $1, 2, 3, 0$.

The cycle in terms of $(A, B)$: $A_1=0, B_1=1, A_2=1, B_2=2, A_3=3, B_3=3, A_4=4, B_4=0$.

Sums: $A_i + B_i$ and $A_{i+1} + B_i$:
- $A_1 + B_1 = 0 + 1 = 1$
- $A_2 + B_1 = 1 + 1 = 2$
- $A_2 + B_2 = 1 + 2 = 3$
- $A_3 + B_2 = 3 + 2 = 5$
- $A_3 + B_3 = 3 + 3 = 6$
- $A_4 + B_3 = 4 + 3 = 7$
- $A_4 + B_4 = 4 + 0 = 4$
- $A_1 + B_4 = 0 + 0 = 0$

Sums: $\{0, 1, 2, 3, 4, 5, 6, 7\}$. ✓

So the pattern for the $(A, B)$ cycle:
- $k = 1$: $A = (0, 2), B = (1, 0)$. But $A$-set is $\{0, 2\}$... wait, for $k = 1$, $A = \{0, 2\}$ and $B = \{0, 1\}$. Hmm, $A$-values are $\{0, 2\}$ but in the $(a,b)$ rep, $A$ should be $\{0, 1, \ldots, k-1, k+1, \ldots, 2k\} = \{0, 2\}$ for $k = 1$. And $B = \{0, 1, \ldots, 2k-1\} = \{0, 1\}$.

Cycle: $A = (0, 2), B = (1, 0)$.
Sums: $0+1=1, 2+1=3, 2+0=2, 0+0=0$. $\{0,1,2,3\}$. ✓

- $k = 2$: $A = (0, 1, 3, 4), B = (1, 2, 3, 0)$.
Sums: $1, 2, 3, 5, 6, 7, 4, 0$. $\{0,1,2,3,4,5,6,7\}$. ✓

Let me look for a pattern. For $k = 1$: $A = (0, 2), B = (1, 0)$.
For $k = 2$: $A = (0, 1, 3, 4), B = (1, 2, 3, 0)$.

Hmm, let me look at the $A$ sequences: $0, 2$ and $0, 1, 3, 4$. The $B$ sequences: $1, 0$ and $1, 2, 3, 0$.

For $k = 2$, $A = (0, 1, 3, 4)$: this is $\{0, 1, \ldots, 2k\} \setminus \{k\} = \{0, 1, 3, 4\}$ in order but with $k = 2$ removed. And $B = (1, 2, 3, 0)$: this is a cyclic shift of $(0, 1, 2, 3)$.

Let me check if $A = (0, 1, \ldots, k-1, k+1, \ldots, 2k)$ and $B = (1, 2, \ldots, 2k-1, 0)$ works in general.

For general $k$: $A = (0, 1, \ldots, k-1, k+1, k+2, \ldots, 2k)$, $B = (1, 2, \ldots, 2k-1, 0)$.

The $A$ sequence has $2k$ elements: $0, 1, \ldots, k-1, k+1, \ldots, 2k$.
The $B$ sequence has $2k$ elements: $1, 2, \ldots, 2k-1, 0$.

Sums $A_i + B_i$:
- For $i = 1, \ldots, k-1$: $A_i = i-1, B_i = i$. Sum = $2i - 1$.
- For $i = k$: $A_k = k-1, B_k = k$. Sum = $2k - 1$.
- For $i = k+1$: $A_{k+1} = k+1, B_{k+1} = k+1$. Sum = $2k + 2$.
- For $i = k+2, \ldots, 2k-1$: $A_i = i, B_i = i$. Sum = $2i$.
- For $i = 2k$: $A_{2k} = 2k, B_{2k} = 0$. Sum = $2k$.

Wait, let me be more careful. $A = (0, 1, 2, \ldots, k-1, k+1, k+2, \ldots, 2k)$. So:
- $A_1 = 0, A_2 = 1, \ldots, A_k = k-1, A_{k+1} = k+1, A_{k+2} = k+2, \ldots, A_{2k} = 2k$.

$B = (1, 2, 3, \ldots, 2k-1, 0)$. So:
- $B_1 = 1, B_2 = 2, \ldots, B_{2k-1} = 2k-1, B_{2k} = 0$.

Sums $A_i + B_i$:
- $i = 1$: $0 + 1 = 1$
- $i = 2$: $1 + 2 = 3$
- ...
- $i = k$: $(k-1) + k = 2k-1$
- $i = k+1$: $(k+1) + (k+1) = 2k+2$
- $i = k+2$: $(k+2) + (k+2) = 2k+4$
- ...
- $i = 2k-1$: $(2k-1) + (2k-1) = 4k-2$
- $i = 2k$: $2k + 0 = 2k$

So $A_i + B_i$ gives: $\{1, 3, 5, \ldots, 2k-1\} \cup \{2k+2, 2k+4, \ldots, 4k-2\} \cup \{2k\}$.

That's $\{1, 3, \ldots, 2k-1, 2k, 2k+2, 2k+4, \ldots, 4k-2\}$. Missing from $\{0, \ldots, 4k-1\}$: $\{0, 2, 4, \ldots, 2k-2, 2k+1, 2k+3, \ldots, 4k-1\}$.

Now sums $A_{i+1} + B_i$ (with $A_{2k+1} = A_1 = 0$):
- $i = 1$: $A_2 + B_1 = 1 + 1 = 2$
- $i = 2$: $A_3 + B_2 = 2 + 2 = 4$
- ...
- $i = k-1$: $A_k + B_{k-1} = (k-1) + (k-1) = 2k-2$
- $i = k$: $A_{k+1} + B_k = (k+1) + k = 2k+1$
- $i = k+1$: $A_{k+2} + B_{k+1} = (k+2) + (k+1) = 2k+3$
- $i = k+2$: $A_{k+3} + B_{k+2} = (k+3) + (k+2) = 2k+5$
- ...
- $i = 2k-2$: $A_{2k-1} + B_{2k-2} = (2k-1) + (2k-2) = 4k-3$
- $i = 2k-1$: $A_{2k} + B_{2k-1} = 2k + (2k-1) = 4k-1$
- $i = 2k$: $A_1 + B_{2k} = 0 + 0 = 0$

So $A_{i+1} + B_i$ gives: $\{2, 4, 6, \ldots, 2k-2\} \cup \{2k+1, 2k+3, \ldots, 4k-1\} \cup \{0\}$.

That's $\{0, 2, 4, \ldots, 2k-2, 2k+1, 2k+3, \ldots, 4k-1\}$.

Combined with the $A_i + B_i$ sums: $\{1, 3, \ldots, 2k-1, 2k, 2k+2, \ldots, 4k-2\}$.

Total: $\{0, 1, 2, \ldots, 2k-2, 2k-1, 2k, 2k+1, 2k+2, \ldots, 4k-2, 4k-1\} = \{0, 1, \ldots, 4k-1\}$. ✓

So the construction works for all $k$! But wait, I need to check that the $B$ values form a valid permutation (all distinct) and the $A$ values form a valid permutation (all distinct), and that the cycle is a single cycle (not multiple cycles).

$A = (0, 1, \ldots, k-1, k+1, \ldots, 2k)$: these are all distinct, forming the set $\{0, \ldots, 2k\} \setminus \{k\}$. ✓
$B = (1, 2, \ldots, 2k-1, 0)$: these are all distinct, forming $\{0, 1, \ldots, 2k-1\}$. ✓

Now, is the cycle a single Hamiltonian cycle? The cycle in the bipartite graph is $A_1 - B_1 - A_2 - B_2 - \cdots - A_{2k} - B_{2k} - A_1$. This visits all $A$-vertices and all $B$-vertices, so it's a Hamiltonian cycle by construction (as long as all $A_i$ are distinct and all $B_i$ are distinct, which they are).

Wait, but I need to make sure it's actually a single cycle, not that it visits the same vertex twice. Since all $A_i$ are distinct and all $B_i$ are distinct, and the cycle alternates between $A$ and $B$ vertices, it visits each vertex exactly once. So it is a single Hamiltonian cycle. ✓

But wait, I also need to verify that the edge sums are all distinct, which I just did above — they form $\{0, 1, \ldots, 4k-1\}$.

So the construction works for all $k \geq 1$, meaning for all $n = 4k \geq 4$.

Let me also verify that $n$ must be a multiple of 4. We showed:
1. $n$ odd: impossible (sum condition).
2. $n \equiv 2 \pmod{4}$: impossible (parity alternation fails).
3. $n \equiv 0 \pmod{4}$: construction exists.

So the answer is: memorable labellings exist if and only if $n \equiv 0 \pmod{4}$.

The multiples of 4 in $[3, 100]$ are $4, 8, 12, \ldots, 100$. There are $25$ of them. Their sum is $4 \cdot (1 + 2 + \cdots + 25) = 4 \cdot 325 = 1300$.

Wait, but I should double-check the necessity more carefully. Let me re-examine the case $n \equiv 2 \pmod 4$.

For $n$ even, we showed only the all-even vertices case is possible. The set is $\{0, 1, \ldots, n\} \setminus \{n/2\}$, and we need a cyclic arrangement with consecutive sums being $\{1, 3, 5, \ldots, 2n-1\}$ (all odd). For sums to be odd, consecutive elements must have different parities, requiring an alternating cycle. The set $\{0, 1, \ldots, n\} \setminus \{n/2\}$ has:
- $n/2 + 1$ even numbers (from $\{0, 2, \ldots, n\}$) minus 1 if $n/2$ is even, plus...
  
Let me recount. $\{0, 1, \ldots, n\}$ has $\lfloor n/2 \rfloor + 1$ even numbers and $\lceil n/2 \rceil$ odd numbers. For $n$ even: $n/2 + 1$ even and $n/2$ odd. Removing $n/2$: if $n/2$ is even (i.e., $n \equiv 0 \pmod 4$), we get $n/2$ even and $n/2$ odd. If $n/2$ is odd (i.e., $n \equiv 2 \pmod 4$), we get $n/2 + 1$ even and $n/2 - 1$ odd.

For alternating cycle, need equal even and odd: $n/2 = n/2$ (when $n \equiv 0 \pmod 4$) ✓, or $n/2 + 1 = n/2 - 1$ (when $n \equiv 2 \pmod 4$) ✗.

So indeed $n \equiv 2 \pmod 4$ is impossible. ✓

And for $n$ odd, we showed the sum condition requires $a^* = n/2 \notin \mathbb{Z}$, so impossible. ✓

Therefore, the answer is the sum of all multiples of 4 from 4 to 100, which is $4(1 + 2 + \cdots + 25) = 4 \cdot \frac{25 \cdot 26}{2} = 4 \cdot 325 = 1300$.

Let me also verify the construction once more for $k = 1$ ($n = 4$).

$A = (0, 2), B = (1, 0)$. Cycle: $0 - 1 - 2 - 0 - 0$... wait, the cycle is $A_1, B_1, A_2, B_2, A_1 = 0, 1, 2, 0, 0$. Hmm, that doesn't look right. The cycle should be $A_1 - B_1 - A_2 - B_2 - A_1$, which is $0 - 1 - 2 - 0 - 0$. But $B_2 = 0$ and $A_1 = 0$, so the last edge is $B_2 - A_1 = 0 - 0$. But $A$ and $B$ are different sets (bipartite), so $A_1 = 0$ (an $A$-vertex) and $B_2 = 0$ (a $B$-vertex) are different vertices even though they have the same value. In the original problem, the $A$-vertices correspond to even numbers and $B$-vertices to odd numbers, so they're distinct.

Going back to the original: $A$-values $\{0, 2\}$ correspond to even vertex labels $\{0, 4\}$ (multiplying by 2). $B$-values $\{0, 1\}$ correspond to odd vertex labels... wait, no. Let me re-derive.

For $n = 4$ ($k = 1$, $m = 2$): The $a$-values (half of even vertex labels) are from $\{0, 1, 2, 3, 4\} \setminus \{2\} = \{0, 1, 3, 4\}$. The even $a$-values are $\{0, 4\}$ (dividing by 2: $\{0, 2\}$, which is the $A$-set). The odd $a$-values are $\{1, 3\}$ (corresponding to $B = \{0, 1\}$ where $b = (a_{\text{odd}} - 1)/2$).

The cycle in $a$-values: $A_1 = 0, B_1 = 1, A_2 = 2, B_2 = 0$, meaning $a$-values: $0, 1, 4, 3$ (since $A$-value $0 \to a = 0$, $B$-value $1 \to a = 2 \cdot 1 + 1 = 3$... wait, I'm getting confused.

Let me just go back to the direct construction. For $n = 4k$, the vertex labels (in the $\{0, \ldots, 2n\}$ representation) are even numbers $\{0, 2, \ldots, 2n\} \setminus \{n\}$. The $a$-values (dividing by 2) are $\{0, 1, \ldots, n\} \setminus \{n/2\}$.

The cycle in $a$-values is: $A_1, 2B_1 + 1, A_2, 2B_2 + 1, \ldots$ where $A_i$ are even $a$-values and $2B_i + 1$ are odd $a$-values.

Wait, I think I overcomplicated this. Let me just directly verify the construction gives a valid memorable labelling.

For $n = 4k$:
- Vertices (even labels): $2 \cdot a_i$ where $a_i$ ranges over $\{0, 1, \ldots, n\} \setminus \{n/2\}$ in the cyclic order given by the construction.
- The cyclic order of $a$-values: $0, 1, 2, \ldots, k-1, k+1, k+2, \ldots, 2k, 2k+1, 2k+2, \ldots$... 

Hmm wait, I need to be more careful. The $A$-set is $\{0, 1, \ldots, k-1, k+1, \ldots, 2k\}$ (even $a$-values divided by 2... no, the $A$-set IS the even $a$-values, and the $B$-set represents the odd $a$-values).

Actually, I realize I need to be more careful about the mapping. Let me re-derive.

For $n = 4k$, $m = n/2 = 2k$. The $a$-values are $\{0, 1, \ldots, 2k\} \setminus \{k\}$... no wait, $n/2 = 2k$, so the $a$-values are $\{0, 1, \ldots, n\} \setminus \{n/2\} = \{0, 1, \ldots, 4k\} \setminus \{2k\}$.

Hmm, I think I mixed up notation. Let me restart the construction more carefully.

For $n = 4k$:
- Consecutive integers: $\{0, 1, \ldots, 2n\} = \{0, 1, \ldots, 8k\}$.
- Interior label: $n = 4k$.
- Vertices: all even numbers from $\{0, 2, 4, \ldots, 8k\} \setminus \{4k\}$. These are $\{0, 2, \ldots, 4k-2, 4k+2, \ldots, 8k\}$, total $4k$ numbers. Wait, $\{0, 2, \ldots, 8k\}$ has $4k + 1$ numbers, removing $4k$ gives $4k$ numbers. ✓
- Sides: all odd numbers from $\{1, 3, \ldots, 8k-1\}$, total $4k$ numbers. ✓

Now, write vertex labels as $2a_i$ where $a_i \in \{0, 1, \ldots, 4k\} \setminus \{2k\}$. Side labels are $a_i + a_{i+1}$ (since $(2a_i + 2a_{i+1})/2 = a_i + a_{i+1}$). We need $\{a_i + a_{i+1}\} = \{1, 3, 5, \ldots, 8k-1\}$.

For sums to be odd, consecutive $a_i$ must have different parities. The set $\{0, 1, \ldots, 4k\} \setminus \{2k\}$ has:
- Even $a$-values: $\{0, 2, \ldots, 4k\} \setminus \{2k\}$. Since $2k$ is even, this has $2k$ elements.
- Odd $a$-values: $\{1, 3, \ldots, 4k-1\}$. This has $2k$ elements.

So we need an alternating cycle of $2k$ even and $2k$ odd $a$-values.

Even $a$-values: $\{0, 2, \ldots, 2k-2, 2k+2, \ldots, 4k\}$. Let me write these as $2u$ where $u \in \{0, 1, \ldots, k-1, k+1, \ldots, 2k\}$. So the $u$-set is $U = \{0, 1, \ldots, k-1, k+1, \ldots, 2k\}$, $|U| = 2k$.

Odd $a$-values: $\{1, 3, \ldots, 4k-1\}$. Write as $2v + 1$ where $v \in \{0, 1, \ldots, 2k-1\}$. So $V = \{0, 1, \ldots, 2k-1\}$, $|V| = 2k$.

The cycle alternates: $2u_1, 2v_1+1, 2u_2, 2v_2+1, \ldots, 2u_{2k}, 2v_{2k}+1, 2u_1$.

Side sums: $(2u_i + 2v_i + 1) = 2(u_i + v_i) + 1$ and $(2u_{i+1} + 2v_i + 1) = 2(u_{i+1} + v_i) + 1$.

We need $\{2(u_i + v_i) + 1, 2(u_{i+1} + v_i) + 1\} = \{1, 3, \ldots, 8k-1\}$, i.e., $\{u_i + v_i, u_{i+1} + v_i\} = \{0, 1, \ldots, 4k-1\}$.

This is exactly the $(A, B)$ formulation I had before, with $A = U$ and $B = V$.

My construction: $U$-sequence = $(0, 1, \ldots, k-1, k+1, \ldots, 2k)$ and $V$-sequence = $(1, 2, \ldots, 2k-1, 0)$.

I verified that the sums $\{u_i + v_i, u_{i+1} + v_i\}$ give exactly $\{0, 1, \ldots, 4k-1\}$.

And the cycle is a single Hamiltonian cycle since all $u_i$ are distinct and all $v_i$ are distinct.

So the construction is valid for all $k \geq 1$, i.e., all $n = 4k \geq 4$.

Therefore, a memorable labelling exists if and only if $4 | n$.

The multiples of 4 in $[3, 100]$: $4, 8, 12, \ldots, 100$. Count: $\lfloor 100/4 \rfloor = 25$. Sum: $4 \cdot (1 + 2 + \cdots + 25) = 4 \cdot 325 = 1300$.

The answer is $\boxed{1300}$.

Now let me write up the proof properly.        — AI历史解题过程（thinking）
#   polymath_05704         — 题目ID

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
  <problem_id>polymath_05704</problem_id>
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

Let $n \geq 3$ be an integer. A labelling of the $n$ vertices, the $n$ sides, and the interior of a regular $n$-gon by $2n + 1$ distinct integers is called memorable if:
(a) Each side has a label that is the arithmetic mean of the labels of its endpoints.
(b) The interior of the $n$-gon has a label that is the arithmetic mean of the labels of all the vertices.

Find the sum of all integers $n$ in the range $3 \leq n \leq 100$ for which there exists a memorable labelling of a regular $n$-gon consisting of $2n + 1$ consecutive integers.

## Standard Solution

From the original solution, a memorable labelling exists if and only if $n \equiv 0 \pmod{4}$. 
In the range $3 \leq n \leq 100$, the values of $n$ satisfying this condition are $4, 8, 12, \ldots, 100$. 
These values form an arithmetic progression with first term $a=4$, last term $l=100$, and common difference $d=4$. 
The number of terms is $k = \frac{100 - 4}{4} + 1 = 25$. 
The sum of these terms is $\frac{k(a + l)}{2} = \frac{25(4 + 100)}{2} = \frac{25 \times 104}{2} = 25 \times 52 = 1300$.

## AI's Thinking (Attempted Solution Process)

The problem asks me to solve a math problem directly in the TUI without using any tools or writing files. Let me read the problem carefully.

Problem: Let $n \geq 3$ be an integer. A labelling of the $n$ vertices, the $n$ sides, and the interior of a regular $n$-gon by $2n+1$ distinct integers is called memorable if:
(a) Each side has a label that is the arithmetic mean of the labels of its endpoints.
(b) The interior of the $n$-gon has a label that is the arithmetic mean of the labels of all the vertices.

Find the sum of all integers $n$ in the range $3 \leq n \leq 100$ for which there exists a memorable labelling of a regular $n$-gon consisting of $2n+1$ consecutive integers.

Let me think about this.

We have $2n+1$ consecutive integers. Let's say they are $\{a, a+1, a+2, \ldots, a+2n\}$ for some integer $a$.

The vertices get $n$ labels, the sides get $n$ labels, and the interior gets 1 label. All $2n+1$ distinct.

Condition (a): Each side label = arithmetic mean of its two endpoint (vertex) labels. So if vertices are $v_1, v_2, \ldots, v_n$ (in order around the polygon), then side $i$ (between $v_i$ and $v_{i+1}$, with $v_{n+1} = v_1$) has label $s_i = (v_i + v_{i+1})/2$.

For $s_i$ to be an integer, $v_i + v_{i+1}$ must be even, so $v_i$ and $v_{i+1}$ have the same parity. Since this holds for all consecutive pairs, all vertices have the same parity.

Condition (b): Interior label = arithmetic mean of all vertex labels. So interior = $(v_1 + v_2 + \cdots + v_n)/n$. This must be an integer, so $n | (v_1 + \cdots + v_n)$.

Now, the $2n+1$ consecutive integers are $\{a, a+1, \ldots, a+2n\}$. The sum of all of them is $(2n+1)(2a+2n)/2 = (2n+1)(a+n)$.

The sum of all labels = sum of vertices + sum of sides + interior.

Sum of sides = $\sum_{i=1}^n (v_i + v_{i+1})/2 = \sum_{i=1}^n v_i$ (since each vertex appears in exactly 2 sides, so $\sum (v_i + v_{i+1})/2 = (2\sum v_i)/2 = \sum v_i$).

Wait, let me recompute. $\sum_{i=1}^n s_i = \sum_{i=1}^n (v_i + v_{i+1})/2 = \frac{1}{2}\sum_{i=1}^n (v_i + v_{i+1}) = \frac{1}{2} \cdot 2\sum_{i=1}^n v_i = \sum_{i=1}^n v_i$.

So sum of sides = sum of vertices = $V$ where $V = \sum v_i$.

Interior = $V/n$.

Total sum = $V + V + V/n = 2V + V/n = V(2 + 1/n) = V(2n+1)/n$.

But total sum = $(2n+1)(a+n)$.

So $V(2n+1)/n = (2n+1)(a+n)$, which gives $V/n = a+n$, i.e., $V = n(a+n)$.

So the interior label = $V/n = a+n$, which is the middle of the $2n+1$ consecutive integers! That's elegant.

So the interior must be labeled with $a+n$, the median of the consecutive integers.

Now, all vertices have the same parity. The $2n+1$ consecutive integers $\{a, a+1, \ldots, a+2n\}$ contain either $n+1$ of one parity and $n$ of the other.

If $a$ is even: the set has $n+1$ even numbers and $n$ odd numbers (since positions $0, 2, 4, \ldots, 2n$ are even, that's $n+1$ evens).

If $a$ is odd: the set has $n+1$ odd numbers and $n$ even numbers.

The vertices all have the same parity. We need $n$ vertices of the same parity. The sides are averages of two same-parity vertices, so sides have the same parity as vertices. Wait, no: if two vertices are both even, their average is even. If both odd, average is odd. So sides have the same parity as the vertices.

So vertices and sides all have the same parity. That's $2n$ labels of the same parity. But the set of $2n+1$ consecutive integers has at most $n+1$ of any given parity. So we need $2n \leq n+1$, i.e., $n \leq 1$. But $n \geq 3$, contradiction!

Wait, that can't be right. Let me reconsider.

Hmm, wait. The sides have the same parity as the vertices only if the average of two same-parity numbers has that parity. Average of two even numbers: $(2k + 2m)/2 = k+m$, which could be even or odd. Average of two odd numbers: $(2k+1 + 2m+1)/2 = k+m+1$, which could be even or odd.

So I was wrong. The sides don't necessarily have the same parity as the vertices.

Let me reconsider. The vertices all have the same parity. Let's say they're all even (WLOG by shifting). Then each side label = $(v_i + v_{i+1})/2$ which is an integer (since both even), but its parity depends on $v_i/2 + v_{i+1}/2$.

OK so let me think more carefully.

The $2n+1$ consecutive integers are $\{a, a+1, \ldots, a+2n\}$.

Vertices: $n$ values, all same parity.
Sides: $n$ values, each = average of two consecutive vertices.
Interior: $a+n$ (the median).

Since the interior is $a+n$, and all labels are distinct, no vertex or side can equal $a+n$.

Let me think about what parities are available. The set has $n+1$ numbers of parity $p$ (where $p$ = parity of $a$) and $n$ numbers of parity $1-p$.

The vertices are all the same parity. Case 1: vertices all have parity $p$ (the majority parity). Then we use $n$ of the $n+1$ numbers with parity $p$ for vertices. The remaining 1 number with parity $p$ and all $n$ numbers with parity $1-p$ are for sides and interior. But interior = $a+n$. What's the parity of $a+n$? It's $p + n \mod 2 = p \oplus (n \mod 2)$.

Hmm, this is getting complicated. Let me think differently.

Actually, let me think about this more carefully using the structure.

Let me shift so that the consecutive integers are $\{0, 1, 2, \ldots, 2n\}$ (i.e., $a = 0$). Then the interior label is $n$.

Vertices are $n$ distinct values from $\{0, 1, \ldots, 2n\} \setminus \{n\}$, all the same parity. Sides are the remaining $n$ values from $\{0, 1, \ldots, 2n\} \setminus \{n\}$, and each side $s_i = (v_i + v_{i+1})/2$.

The sum condition is automatically satisfied (we derived it). So we need:
1. Choose $n$ vertices from $\{0, 1, \ldots, 2n\} \setminus \{n\}$, all same parity.
2. The remaining $n$ values (sides) must be arrangeable as $(v_i + v_{i+1})/2$ for some cyclic ordering of the vertices.

Actually, condition 2 is: the multiset $\{(v_i + v_{i+1})/2 : i = 1, \ldots, n\}$ (for some ordering) equals the set of remaining $n$ values.

Let me think about the parity constraint more. The set $\{0, 1, \ldots, 2n\} \setminus \{n\}$ has $2n$ elements. Among $\{0, 1, \ldots, 2n\}$, there are $n+1$ even and $n$ odd (if $n$ is such that... wait, $\{0, 1, \ldots, 2n\}$ has $n+1$ even numbers ($0, 2, 4, \ldots, 2n$) and $n$ odd numbers ($1, 3, \ldots, 2n-1$)).

After removing $n$: if $n$ is even, we remove an even number, so we have $n$ even and $n$ odd. If $n$ is odd, we remove an odd number, so we have $n+1$ even and $n-1$ odd.

Case 1: $n$ even. Then $\{0, 1, \ldots, 2n\} \setminus \{n\}$ has $n$ even and $n$ odd. Vertices must be all same parity. If vertices are all even, we use all $n$ even numbers. Then sides are all $n$ odd numbers. If vertices are all odd, we use all $n$ odd numbers, sides are all $n$ even numbers.

Case 2: $n$ odd. Then $\{0, 1, \ldots, 2n\} \setminus \{n\}$ has $n+1$ even and $n-1$ odd. Vertices all same parity. If all even: use $n$ of $n+1$ evens, sides = 1 even + $n-1$ odd. If all odd: need $n$ odd but only $n-1$ available. Impossible.

So when $n$ is odd, vertices must be all even, and we choose $n$ of the $n+1$ even numbers (excluding one even number), and the sides consist of that 1 even number plus all $n-1$ odd numbers.

When $n$ is even, either all-even or all-odd vertices work, and sides are the complementary parity.

This is a complex combinatorial problem. Let me think about small cases and try to find a pattern.

Let me try $n = 3$. Consecutive integers $\{0,1,2,3,4,5,6\}$, interior = 3. $n=3$ is odd, so vertices all even, choose 3 from $\{0, 2, 4, 6\}$ (excluding one). Sides = the excluded even + all odds $\{1, 5\}$.

Options for excluded even: 0, 2, 4, or 6.

If we exclude 0: vertices = $\{2, 4, 6\}$. Sides should be $\{0, 1, 5\}$. We need a cyclic ordering of $\{2, 4, 6\}$ such that the averages give $\{0, 1, 5\}$. Averages of pairs: $(2+4)/2 = 3$, $(4+6)/2 = 5$, $(2+6)/2 = 4$. So possible averages are $\{3, 5, 4\}$. But we need $\{0, 1, 5\}$. No match.

If we exclude 2: vertices = $\{0, 4, 6\}$. Sides = $\{2, 1, 5\}$. Averages: $(0+4)/2 = 2$, $(4+6)/2 = 5$, $(0+6)/2 = 3$. So $\{2, 5, 3\}$. Need $\{1, 2, 5\}$. No match (3 ≠ 1).

If we exclude 4: vertices = $\{0, 2, 6\}$. Sides = $\{4, 1, 5\}$. Averages: $(0+2)/2 = 1$, $(2+6)/2 = 4$, $(0+6)/2 = 3$. So $\{1, 4, 3\}$. Need $\{1, 4, 5\}$. No match (3 ≠ 5).

If we exclude 6: vertices = $\{0, 2, 4\}$. Sides = $\{6, 1, 5\}$. Averages: $(0+2)/2 = 1$, $(2+4)/2 = 3$, $(0+4)/2 = 2$. So $\{1, 3, 2\}$. Need $\{1, 5, 6\}$. No match.

So $n = 3$ doesn't work.

Let me try $n = 4$. Consecutive $\{0,1,...,8\}$, interior = 4. $n=4$ even. 

Option A: vertices all even = $\{0, 2, 4, 6, 8\} \setminus \{4\}$ wait, we need to exclude the interior 4. The even numbers in $\{0,...,8\}$ are $\{0, 2, 4, 6, 8\}$, that's 5. Remove 4 (interior), get $\{0, 2, 6, 8\}$. That's 4 vertices. Sides = all odds = $\{1, 3, 5, 7\}$.

We need a cyclic ordering of $\{0, 2, 6, 8\}$ with averages = $\{1, 3, 5, 7\}$.

Averages of pairs:
- $(0+2)/2 = 1$ ✓
- $(0+6)/2 = 3$ ✓
- $(0+8)/2 = 4$ ✗ (not in sides)
- $(2+6)/2 = 4$ ✗
- $(2+8)/2 = 5$ ✓
- $(6+8)/2 = 7$ ✓

We need a Hamiltonian cycle on $\{0, 2, 6, 8\}$ using edges with averages in $\{1, 3, 5, 7\}$. Valid edges: $(0,2) \to 1$, $(0,6) \to 3$, $(2,8) \to 5$, $(6,8) \to 7$.

So the graph has edges: $0-2$, $0-6$, $2-8$, $6-8$. This is a path $6-0-2-8$ and also $6-8$ and $0-6$. Let me draw: edges are $\{0,2\}, \{0,6\}, \{2,8\}, \{6,8\}$. This is a 4-cycle: $0-2-8-6-0$! Averages: $1, 5, 7, 3$. That's $\{1, 3, 5, 7\}$. ✓

So $n = 4$ works!

Let me try $n = 5$. Consecutive $\{0,...,10\}$, interior = 5. $n=5$ odd, vertices all even from $\{0, 2, 4, 6, 8, 10\} \setminus \{5\}$... wait, 5 is odd, so removing 5 doesn't affect the evens. Even numbers: $\{0, 2, 4, 6, 8, 10\}$, that's 6. Choose 5, exclude 1. Sides = excluded even + all odds from $\{0,...,10\}\setminus\{5\}$ = excluded even + $\{1, 3, 7, 9\}$.

So sides have 5 elements: 1 even + 4 odd. Vertices: 5 even numbers.

Let me try excluding 0: vertices = $\{2, 4, 6, 8, 10\}$, sides = $\{0, 1, 3, 7, 9\}$.

Averages of pairs from vertices:
$(2+4)/2=3$, $(2+6)/2=4$, $(2+8)/2=5$, $(2+10)/2=6$, $(4+6)/2=5$, $(4+8)/2=6$, $(4+10)/2=7$, $(6+8)/2=7$, $(6+10)/2=8$, $(8+10)/2=9$.

We need a Hamiltonian cycle on $\{2,4,6,8,10\}$ with edge averages in $\{0,1,3,7,9\}$. Valid edges (average in $\{0,1,3,7,9\}$):
- avg 3: $(2,4)$
- avg 7: $(4,10)$, $(6,8)$
- avg 9: $(8,10)$
- avg 0: impossible (would need two vertices summing to 0, but min is 2)
- avg 1: impossible (would need sum 2, only $0+2$ but 0 not a vertex)

So valid edges: $\{2,4\}, \{4,10\}, \{6,8\}, \{8,10\}$. This gives a path $2-4-10-8-6$ but we need a cycle. $6$ has degree 1 (only connected to 8), $2$ has degree 1 (only connected to 4). Can't form a cycle. Fail.

Try excluding 2: vertices = $\{0, 4, 6, 8, 10\}$, sides = $\{2, 1, 3, 7, 9\}$.

Averages:
$(0+4)/2=2$, $(0+6)/2=3$, $(0+8)/2=4$, $(0+10)/2=5$, $(4+6)/2=5$, $(4+8)/2=6$, $(4+10)/2=7$, $(6+8)/2=7$, $(6+10)/2=8$, $(8+10)/2=9$.

Valid edges (avg in $\{1,2,3,7,9\}$):
- avg 2: $(0,4)$
- avg 3: $(0,6)$
- avg 7: $(4,10)$, $(6,8)$
- avg 9: $(8,10)$
- avg 1: impossible (need sum 2, only $0+2$ but 2 not vertex)

Edges: $\{0,4\}, \{0,6\}, \{4,10\}, \{6,8\}, \{8,10\}$. 

Graph: $0-4-10-8-6-0$. That's a 5-cycle! Averages: $2, 7, 9, 7, 3$. Wait, that gives $\{2, 7, 9, 7, 3\}$ which has a repeat (7 appears twice). But sides must be distinct. So this doesn't work.

Hmm, the issue is that two edges have the same average. Let me check: $(4,10) \to 7$ and $(6,8) \to 7$. Both give 7. So we can't use both in the cycle. But in the 5-cycle $0-4-10-8-6-0$, we use edge $(4,10)$ and edge $(6,8)$... wait, $8-6$ is an edge, giving avg 7. And $4-10$ giving avg 7. So two sides labeled 7, not allowed.

Can we find a different 5-cycle? The edges are $\{0,4\}, \{0,6\}, \{4,10\}, \{6,8\}, \{8,10\}$. 

Possible cycles: $0-4-10-8-6-0$ (uses all 5 edges, but two give 7). Any other Hamiltonian cycle? $0-6-8-10-4-0$: edges $(0,6)\to 3$, $(6,8)\to 7$, $(8,10)\to 9$, $(10,4)\to 7$, $(4,0)\to 2$. Same problem: 7 appears twice.

So excluding 2 doesn't work because of the duplicate average.

Try excluding 4: vertices = $\{0, 2, 6, 8, 10\}$, sides = $\{4, 1, 3, 7, 9\}$.

Averages:
$(0+2)/2=1$, $(0+6)/2=3$, $(0+8)/2=4$, $(0+10)/2=5$, $(2+6)/2=4$, $(2+8)/2=5$, $(2+10)/2=6$, $(6+8)/2=7$, $(6+10)/2=8$, $(8+10)/2=9$.

Valid edges (avg in $\{1,3,4,7,9\}$):
- avg 1: $(0,2)$
- avg 3: $(0,6)$
- avg 4: $(0,8)$, $(2,6)$
- avg 7: $(6,8)$
- avg 9: $(8,10)$

Edges: $\{0,2\}, \{0,6\}, \{0,8\}, \{2,6\}, \{6,8\}, \{8,10\}$.

We need a Hamiltonian cycle using 5 edges with distinct averages from $\{1,3,4,7,9\}$. Note avg 4 comes from two edges: $(0,8)$ and $(2,6)$. We can use at most one of them (since averages must be distinct).

So we need to pick one of $(0,8)$ or $(2,6)$ for avg 4, and then find a cycle.

If we use $(0,8)$ for avg 4: remaining edges needed for avgs 1,3,7,9: $(0,2)$ for 1, $(0,6)$ for 3, $(6,8)$ for 7, $(8,10)$ for 9. But vertex 0 would have degree 3 (edges to 2, 6, 8). In a cycle, each vertex has degree 2. So we can't use all of $(0,2), (0,6), (0,8)$.

We need to choose 5 edges forming a Hamiltonian cycle with distinct averages. The available edges with their averages:
- $(0,2) \to 1$
- $(0,6) \to 3$
- $(0,8) \to 4$
- $(2,6) \to 4$
- $(6,8) \to 7$
- $(8,10) \to 9$

We must use exactly one of $(0,8), (2,6)$ for avg 4. And we need all 5 averages $\{1,3,4,7,9\}$.

If use $(0,8)$ for 4: need edges for 1,3,7,9 = $(0,2), (0,6), (6,8), (8,10)$. Vertex 0 has degree 3. Not a cycle.

If use $(2,6)$ for 4: need edges for 1,3,7,9 = $(0,2), (0,6), (6,8), (8,10)$. Vertex 0 has degree 2 (edges to 2, 6). Vertex 6 has degree 3 (edges to 0, 2, 8). Not a cycle.

So excluding 4 doesn't work.

Try excluding 6: vertices = $\{0, 2, 4, 8, 10\}$, sides = $\{6, 1, 3, 7, 9\}$.

Averages:
$(0+2)/2=1$, $(0+4)/2=2$, $(0+8)/2=4$, $(0+10)/2=5$, $(2+4)/2=3$, $(2+8)/2=5$, $(2+10)/2=6$, $(4+8)/2=6$, $(4+10)/2=7$, $(8+10)/2=9$.

Valid edges (avg in $\{1,3,6,7,9\}$):
- avg 1: $(0,2)$
- avg 3: $(2,4)$
- avg 6: $(2,10)$, $(4,8)$
- avg 7: $(4,10)$
- avg 9: $(8,10)$

Same structure as before. avg 6 from two edges. 

If use $(2,10)$ for 6: edges = $(0,2), (2,4), (2,10), (4,10), (8,10)$. Vertex 2 has degree 3. Not a cycle.

If use $(4,8)$ for 6: edges = $(0,2), (2,4), (4,8), (4,10), (8,10)$. Vertex 4 has degree 3. Not a cycle.

Doesn't work.

Try excluding 8: vertices = $\{0, 2, 4, 6, 10\}$, sides = $\{8, 1, 3, 7, 9\}$.

Averages:
$(0+2)/2=1$, $(0+4)/2=2$, $(0+6)/2=3$, $(0+10)/2=5$, $(2+4)/2=3$, $(2+6)/2=4$, $(2+10)/2=6$, $(4+6)/2=5$, $(4+10)/2=7$, $(6+10)/2=8$.

Valid edges (avg in $\{1,3,7,8,9\}$):
- avg 1: $(0,2)$
- avg 3: $(0,6)$, $(2,4)$
- avg 7: $(4,10)$
- avg 8: $(6,10)$
- avg 9: impossible (need sum 18, max is $6+10=16$)

avg 9 impossible. Fail.

Try excluding 10: vertices = $\{0, 2, 4, 6, 8\}$, sides = $\{10, 1, 3, 7, 9\}$.

Averages:
$(0+2)/2=1$, $(0+4)/2=2$, $(0+6)/2=3$, $(0+8)/2=4$, $(2+4)/2=3$, $(2+6)/2=4$, $(2+8)/2=5$, $(4+6)/2=5$, $(4+8)/2=6$, $(6+8)/2=7$.

Valid edges (avg in $\{1,3,7,9,10\}$):
- avg 1: $(0,2)$
- avg 3: $(0,6)$, $(2,4)$
- avg 7: $(6,8)$
- avg 9: impossible
- avg 10: impossible

Fail.

So $n = 5$ doesn't work.

Let me try $n = 6$. Consecutive $\{0,...,12\}$, interior = 6. $n=6$ even.

Option A: vertices all even. Even numbers in $\{0,...,12\}$: $\{0,2,4,6,8,10,12\}$, that's 7. Remove 6 (interior): $\{0,2,4,8,10,12\}$, 6 vertices. Sides = all odds = $\{1,3,5,7,9,11\}$.

Averages of pairs:
$(0+2)/2=1$, $(0+4)/2=2$, $(0+8)/2=4$, $(0+10)/2=5$, $(0+12)/2=6$, $(2+4)/2=3$, $(2+8)/2=5$, $(2+10)/2=6$, $(2+12)/2=7$, $(4+8)/2=6$, $(4+10)/2=7$, $(4+12)/2=8$, $(8+10)/2=9$, $(8+12)/2=10$, $(10+12)/2=11$.

Valid edges (avg in $\{1,3,5,7,9,11\}$):
- avg 1: $(0,2)$
- avg 3: $(2,4)$
- avg 5: $(0,10)$, $(2,8)$
- avg 7: $(2,12)$, $(4,10)$
- avg 9: $(8,10)$
- avg 11: $(10,12)$

We need a Hamiltonian cycle on $\{0,2,4,8,10,12\}$ with 6 edges having distinct averages $\{1,3,5,7,9,11\}$.

For avg 5: choose $(0,10)$ or $(2,8)$.
For avg 7: choose $(2,12)$ or $(4,10)$.

Let me try $(0,10)$ for 5 and $(4,10)$ for 7. But then vertex 10 has degree 2 from these two edges. Remaining: avg 1: $(0,2)$, avg 3: $(2,4)$, avg 9: $(8,10)$, avg 11: $(10,12)$. But vertex 10 would have degree 4. No.

Try $(0,10)$ for 5 and $(2,12)$ for 7. Edges: $(0,10), (2,12), (0,2), (2,4), (8,10), (10,12)$. Vertex 0: degree 2 (to 10, 2). Vertex 2: degree 3 (to 12, 0, 4). Not a cycle.

Try $(2,8)$ for 5 and $(4,10)$ for 7. Edges: $(2,8), (4,10), (0,2), (2,4), (8,10), (10,12)$. Vertex 2: degree 3 (to 8, 0, 4). Vertex 10: degree 3 (to 4, 8, 12). Not a cycle.

Try $(2,8)$ for 5 and $(2,12)$ for 7. Edges: $(2,8), (2,12), (0,2), (2,4), (8,10), (10,12)$. Vertex 2: degree 4. No.

Hmm, all combinations for avg 5 and 7 lead to problems. Let me think more carefully.

We need each vertex to have degree exactly 2 in the cycle. Let's think about which edges each vertex can be part of:

- Vertex 0: can connect via avg 1 ($(0,2)$), avg 5 ($(0,10)$), or avg 6 (not in set). So vertex 0 has possible edges: $(0,2) \to 1$, $(0,10) \to 5$.
- Vertex 2: $(0,2) \to 1$, $(2,4) \to 3$, $(2,8) \to 5$, $(2,12) \to 7$.
- Vertex 4: $(2,4) \to 3$, $(4,10) \to 7$.
- Vertex 8: $(2,8) \to 5$, $(8,10) \to 9$.
- Vertex 10: $(0,10) \to 5$, $(4,10) \to 7$, $(8,10) \to 9$, $(10,12) \to 11$.
- Vertex 12: $(2,12) \to 7$, $(10,12) \to 11$.

For a Hamiltonian cycle, each vertex has degree 2. Vertex 0 has only 2 possible edges: $(0,2)$ and $(0,10)$. So both must be used! That means avg 1 uses $(0,2)$ and avg 5 uses $(0,10)$.

Vertex 12 has only 2 possible edges: $(2,12)$ and $(10,12)$. So both must be used! avg 7 uses $(2,12)$ and avg 11 uses $(10,12)$.

Vertex 4 has only 2 possible edges: $(2,4)$ and $(4,10)$. So both must be used! avg 3 uses $(2,4)$ and avg 7 uses $(4,10)$.

But we already assigned avg 7 to $(2,12)$! And avg 7 can only be used once. Contradiction.

So Option A (all even vertices) doesn't work for $n=6$.

Option B: vertices all odd. Odd numbers in $\{0,...,12\}$: $\{1,3,5,7,9,11\}$, that's 6. All are vertices (none is the interior 6). Sides = all even numbers except 6 = $\{0,2,4,8,10,12\}$.

Averages of pairs from $\{1,3,5,7,9,11\}$:
$(1+3)/2=2$, $(1+5)/2=3$, $(1+7)/2=4$, $(1+9)/2=5$, $(1+11)/2=6$, $(3+5)/2=4$, $(3+7)/2=5$, $(3+9)/2=6$, $(3+11)/2=7$, $(5+7)/2=6$, $(5+9)/2=7$, $(5+11)/2=8$, $(7+9)/2=8$, $(7+11)/2=9$, $(9+11)/2=10$.

Valid edges (avg in $\{0,2,4,8,10,12\}$):
- avg 0: impossible
- avg 2: $(1,3)$
- avg 4: $(1,7)$, $(3,5)$
- avg 8: $(5,11)$, $(7,9)$
- avg 10: $(9,11)$
- avg 12: impossible

avg 0 and avg 12 impossible. Fail.

So $n = 6$ doesn't work.

Let me try $n = 7$. Consecutive $\{0,...,14\}$, interior = 7. $n=7$ odd, vertices all even.

Even numbers in $\{0,...,14\}$: $\{0,2,4,6,8,10,12,14\}$, 8 numbers. Remove 7 (interior, odd, doesn't affect). Choose 7 of 8 evens, exclude 1. Sides = excluded even + all odds from $\{0,...,14\}\setminus\{7\}$ = excluded even + $\{1,3,5,9,11,13\}$.

So sides = {excluded even} ∪ {1,3,5,9,11,13}, 7 elements.

This is getting complex. Let me think about this more systematically.

Actually, let me think about what structure is needed. The key insight is:

We need a Hamiltonian cycle on $n$ vertices (all same parity) such that the $n$ edge averages are exactly the $n$ side labels (all distinct).

Let me think about this differently. Let's say the vertices are $v_1, v_2, \ldots, v_n$ in cyclic order. The side labels are $s_i = (v_i + v_{i+1})/2$.

The sum of side labels = sum of vertex labels = $V$. We already know this is satisfied.

Another constraint: the side labels and vertex labels partition $\{0, 1, \ldots, 2n\} \setminus \{n\}$.

Let me think about $n = 4$ which worked. The cycle was $0-2-8-6-0$ (wait, let me recheck). Actually I had vertices $\{0, 2, 6, 8\}$ and the cycle $0-2-8-6-0$ with averages $1, 5, 7, 3$. Sides = $\{1, 3, 5, 7\}$. ✓

Let me try to find a pattern. For $n = 4$, the vertices are $\{0, 2, 6, 8\}$ and the cycle goes $0, 2, 8, 6$. Note that $0, 2$ are close together and $6, 8$ are close together, and the cycle alternates between the two clusters.

Let me think about this problem more carefully. Maybe I should look for which $n$ work by trying to construct solutions.

Let me think about the problem in terms of a graph. We have $n$ vertices with values, and we need a Hamiltonian cycle where edge labels (averages) are all distinct and form a specific set.

Actually, let me think about it differently. Let me consider the problem modulo small numbers or look for structural obstructions.

Let me reconsider. The vertices are all even (when $n$ is odd) or all same parity (when $n$ is even). Let me write vertices as $2a_1, 2a_2, \ldots, 2a_n$ (when all even) where $a_i$ are distinct integers. Then side labels are $a_i + a_{i+1}$.

When all even: vertices = $\{2a_1, \ldots, 2a_n\}$, sides = $\{a_i + a_{i+1}\}$, interior = $n$.

The set $\{0, 1, \ldots, 2n\}$: even numbers are $\{0, 2, \ldots, 2n\}$, i.e., $\{2 \cdot 0, 2 \cdot 1, \ldots, 2 \cdot n\}$. So $a_i \in \{0, 1, \ldots, n\}$.

When $n$ is odd: we choose $n$ of the $n+1$ values $\{0, 1, \ldots, n\}$ for $a_i$ (excluding one, say $a^*$), and the sides are $a_i + a_{i+1}$ which must be the remaining $n$ values from $\{0, 1, \ldots, 2n\} \setminus \{n\}$ that are not even (i.e., the odd values) plus $2a^*$ (the excluded even number).

Wait, let me redo this. The full set is $\{0, 1, \ldots, 2n\}$. Interior = $n$. The remaining $2n$ values are $\{0, 1, \ldots, 2n\} \setminus \{n\}$.

When vertices are all even: vertices = $\{2a_1, \ldots, 2a_n\}$ where $\{a_1, \ldots, a_n\} \subset \{0, 1, \ldots, n\}$, $|a_i| = n$, all distinct. The excluded value from $\{0, \ldots, n\}$ is some $a^*$, so $\{a_1, \ldots, a_n\} = \{0, \ldots, n\} \setminus \{a^*\}$.

The sides are $a_i + a_{i+1}$ (for the cyclic ordering). These must be the $n$ values in $\{0, 1, \ldots, 2n\} \setminus \{n\} \setminus \{2a_1, \ldots, 2a_n\}$.

The even values in $\{0, \ldots, 2n\} \setminus \{n\}$ are $\{0, 2, \ldots, 2n\} \setminus \{n\}$ if $n$ is even, or $\{0, 2, \ldots, 2n\} \setminus \{n\}$ ... hmm, $n$ could be even or odd.

Let me separate cases.

Case $n$ odd: $n$ is odd, so $n$ is not even, meaning $n \notin \{0, 2, 4, \ldots, 2n\}$. The even values in $\{0, \ldots, 2n\} \setminus \{n\}$ are $\{0, 2, 4, \ldots, 2n\}$ (all $n+1$ of them). The odd values are $\{1, 3, \ldots, 2n-1\} \setminus \{n\} = \{1, 3, \ldots, 2n-1\} \setminus \{n\}$. Since $n$ is odd, $n \in \{1, 3, \ldots, 2n-1\}$. So odd values in the remaining set: $\{1, 3, \ldots, 2n-1\} \setminus \{n\}$, which has $n - 1$ elements.

Vertices (all even) = $n$ of the $n+1$ even values. Sides = the remaining 1 even value + all $n-1$ odd values.

In terms of $a_i$: vertices = $\{2a : a \in \{0,\ldots,n\} \setminus \{a^*\}\}$, sides = $\{2a^*\} \cup \{1, 3, \ldots, 2n-1\} \setminus \{n\}$.

The side values $a_i + a_{i+1}$ must equal this set. Note $a_i + a_{i+1}$ ranges from $0$ to $2n$ (since $a_i \in \{0, \ldots, n\}$). The side set has one even value $2a^*$ and $n-1$ odd values. Since $a_i + a_{i+1}$ has the same parity as $a_i + a_{i+1}$... well, $a_i + a_{i+1}$ is even iff $a_i$ and $a_{i+1}$ have the same parity.

So exactly one pair of consecutive $a_i$'s has the same parity (giving the even side $2a^*$), and the rest have different parities (giving odd sides).

Case $n$ even: $n$ is even, so $n \in \{0, 2, \ldots, 2n\}$. Even values in $\{0,\ldots,2n\}\setminus\{n\}$: $\{0, 2, \ldots, 2n\} \setminus \{n\}$, which has $n$ elements. Odd values: $\{1, 3, \ldots, 2n-1\}$, $n$ elements.

Sub-case vertices all even: vertices = $n$ even values = all even values in $\{0,...,2n\}\setminus\{n\}$ = $\{0, 2, \ldots, 2n\} \setminus \{n\}$. In terms of $a_i$: $\{a_1, \ldots, a_n\} = \{0, 1, \ldots, n\} \setminus \{n/2\}$ (since $n = 2 \cdot (n/2)$). Sides = all $n$ odd values = $\{1, 3, \ldots, 2n-1\}$.

So $a_i + a_{i+1}$ must be odd for all $i$, meaning consecutive $a_i$'s alternate in parity. This is possible iff $n$ is even (which it is in this case). And the sums $a_i + a_{i+1}$ must be exactly $\{1, 3, 5, \ldots, 2n-1\}$.

Sub-case vertices all odd: vertices = $\{1, 3, \ldots, 2n-1\}$ (all $n$ odd values). Write $v_i = 2b_i + 1$ where $b_i \in \{0, 1, \ldots, n-1\}$. Side = $(v_i + v_{i+1})/2 = b_i + b_{i+1} + 1$. Sides = $\{0, 2, \ldots, 2n\} \setminus \{n\}$ = $\{0, 2, \ldots, 2n\} \setminus \{n\}$, which are the $n$ even values excluding $n$.

So $b_i + b_{i+1} + 1 \in \{0, 2, \ldots, 2n\} \setminus \{n\}$, i.e., $b_i + b_{i+1} \in \{-1, 1, 3, \ldots, 2n-1\} \setminus \{n-1\}$. But $b_i \geq 0$, so $b_i + b_{i+1} \geq 0$. So $b_i + b_{i+1} \in \{1, 3, 5, \ldots, 2n-1\} \setminus \{n-1\}$. Since $n$ is even, $n-1$ is odd, so $n-1 \in \{1, 3, \ldots, 2n-1\}$. So the target set is $\{1, 3, \ldots, 2n-1\} \setminus \{n-1\}$, which has $n-1$ elements. But we need $n$ sides. Contradiction! Unless... wait, let me recount.

Sides = $\{0, 2, \ldots, 2n\} \setminus \{n\}$. This has $n+1 - 1 = n$ elements. $b_i + b_{i+1} + 1$ ranges over these, so $b_i + b_{i+1}$ ranges over $\{-1, 1, 3, \ldots, 2n-1\} \setminus \{n-1\}$. Since $b_i \geq 0$, $b_i + b_{i+1} \geq 0$, so we need $b_i + b_{i+1} \in \{1, 3, \ldots, 2n-1\} \setminus \{n-1\}$. This set has $n - 1$ elements (since $\{1, 3, \ldots, 2n-1\}$ has $n$ elements and we remove $n-1$). But we need $n$ distinct values. $n > n-1$, so impossible!

Wait, that means when $n$ is even and vertices are all odd, it's impossible. Let me double-check with $n = 4$.

$n = 4$: vertices all odd = $\{1, 3, 5, 7\}$. $b_i \in \{0, 1, 2, 3\}$. Sides = $\{0, 2, 4, 6, 8\} \setminus \{4\} = \{0, 2, 6, 8\}$. $b_i + b_{i+1} + 1 \in \{0, 2, 6, 8\}$, so $b_i + b_{i+1} \in \{-1, 1, 5, 7\}$. Since $b_i \geq 0$, need $b_i + b_{i+1} \in \{1, 5, 7\}$. That's 3 values but we need 4 sides. Indeed impossible.

So for $n$ even, only the all-even vertices sub-case is possible.

Great, so let me focus on the all-even vertices case for all $n$.

For $n$ even: $\{a_1, \ldots, a_n\} = \{0, 1, \ldots, n\} \setminus \{n/2\}$. Sides = $\{a_i + a_{i+1}\} = \{1, 3, 5, \ldots, 2n-1\}$ (all odd numbers from 1 to $2n-1$). Need a Hamiltonian cycle on $\{0, 1, \ldots, n\} \setminus \{n/2\}$ with edge sums being exactly $\{1, 3, 5, \ldots, 2n-1\}$, all distinct.

For $n$ odd: $\{a_1, \ldots, a_n\} = \{0, 1, \ldots, n\} \setminus \{a^*\}$ for some $a^*$. Sides = $\{a_i + a_{i+1}\} = \{2a^*\} \cup (\{1, 3, \ldots, 2n-1\} \setminus \{n\})$. Need a Hamiltonian cycle with these edge sums.

This is now a cleaner formulation. Let me think about necessary conditions.

For $n$ even: We need a cyclic arrangement of $\{0, 1, \ldots, n\} \setminus \{n/2\}$ such that the $n$ consecutive sums are exactly $\{1, 3, 5, \ldots, 2n-1\}$.

The sum of all edge sums = $\sum (a_i + a_{i+1}) = 2\sum a_i = 2 \cdot (\sum_{k=0}^{n} k - n/2) = 2 \cdot (n(n+1)/2 - n/2) = 2 \cdot n^2/2 = n^2$.

Sum of $\{1, 3, \ldots, 2n-1\} = n^2$. ✓ So the sum condition is automatically satisfied.

For $n$ odd: Sum of edge sums = $2\sum a_i = 2(\sum_{k=0}^n k - a^*) = 2(n(n+1)/2 - a^*) = n(n+1) - 2a^*$.

Sum of sides = $2a^* + \sum_{k \in \{1,3,...,2n-1\} \setminus \{n\}} k = 2a^* + (n^2 - n)$.

So $n(n+1) - 2a^* = 2a^* + n^2 - n$, giving $n^2 + n - 2a^* = 2a^* + n^2 - n$, so $2n = 4a^*$, so $a^* = n/2$.

But $n$ is odd, so $n/2$ is not an integer! Contradiction!

Wait, this means for $n$ odd, there's no solution? Let me double-check.

For $n$ odd, $a^* = n/2$ which is not an integer. So there's no valid $a^*$, meaning no memorable labelling exists for odd $n$?

But wait, I need to double-check my derivation. Let me recheck for $n$ odd.

We have $a^* \in \{0, 1, \ldots, n\}$, and $\{a_1, \ldots, a_n\} = \{0, 1, \ldots, n\} \setminus \{a^*\}$.

Sum of edge sums = $2 \sum a_i = 2(n(n+1)/2 - a^*) = n(n+1) - 2a^*$.

The sides are $\{2a^*\} \cup (\{1, 3, \ldots, 2n-1\} \setminus \{n\})$.

Sum of sides = $2a^* + \sum(\{1, 3, \ldots, 2n-1\} \setminus \{n\}) = 2a^* + (n^2 - n)$.

Setting equal: $n(n+1) - 2a^* = 2a^* + n^2 - n$
$n^2 + n - 2a^* = n^2 - n + 2a^*$
$2n = 4a^*$
$a^* = n/2$.

Since $n$ is odd, $a^*$ is not an integer. So no solution exists for odd $n$.

Wait, but I should also check: could the vertices be all odd when $n$ is odd? Earlier I showed that when $n$ is odd, the set $\{0,...,2n\}\setminus\{n\}$ has $n+1$ even and $n-1$ odd values. For all-odd vertices, we need $n$ odd values but only $n-1$ are available. So indeed impossible.

So for odd $n$, no memorable labelling exists. 

Now for even $n$, we need a cyclic arrangement of $\{0, 1, \ldots, n\} \setminus \{n/2\}$ such that consecutive sums are exactly $\{1, 3, 5, \ldots, 2n-1\}$.

Let me think about when this is possible. Let me denote $m = n/2$, so $n = 2m$ and we need a cyclic arrangement of $\{0, 1, \ldots, 2m\} \setminus \{m\}$ with consecutive sums being $\{1, 3, 5, \ldots, 4m-1\}$.

The set $\{0, 1, \ldots, 2m\} \setminus \{m\}$ has $2m$ elements. We need $2m$ consecutive sums, all odd, being $\{1, 3, \ldots, 4m-1\}$.

For consecutive sums to be odd, consecutive elements must have different parities. So the cycle must alternate even and odd. The set $\{0, 1, \ldots, 2m\} \setminus \{m\}$ has:
- Even numbers: $\{0, 2, \ldots, 2m\}$, that's $m+1$ numbers. If $m$ is even, removing $m$ gives $m$ even numbers. If $m$ is odd, $m$ is not even, so still $m+1$ even numbers.
- Odd numbers: $\{1, 3, \ldots, 2m-1\}$, that's $m$ numbers. If $m$ is even, $m$ is not odd, so still $m$ odd numbers. If $m$ is odd, removing $m$ gives $m-1$ odd numbers.

For the cycle to alternate even/odd, we need equal numbers of even and odd elements. So:
- If $m$ even: $m$ even, $m$ odd. ✓
- If $m$ odd: $m+1$ even, $m-1$ odd. $m+1 \neq m-1$ (unless $m = 0$). ✗

So for $m$ odd (i.e., $n = 2m$ with $m$ odd, i.e., $n \equiv 2 \pmod{4}$), the cycle can't alternate, so no solution.

For $m$ even (i.e., $n \equiv 0 \pmod{4}$), we have $m$ even and $m$ odd elements, and we need an alternating cycle with sums $\{1, 3, \ldots, 4m-1\}$.

So necessary conditions so far: $n$ must be divisible by 4.

But is divisibility by 4 sufficient? Let me check $n = 4$ ($m = 2$): we already found it works.

Let me check $n = 8$ ($m = 4$): We need a cyclic arrangement of $\{0,1,2,3,5,6,7,8\}$ (removing 4) with consecutive sums = $\{1,3,5,7,9,11,13,15\}$.

Let me try to construct this. We need alternating even/odd. Even numbers: $\{0, 2, 6, 8\}$. Odd numbers: $\{1, 3, 5, 7\}$.

The cycle alternates: even, odd, even, odd, even, odd, even, odd.

Consecutive sums (even + odd) must be $\{1, 3, 5, 7, 9, 11, 13, 15\}$.

Let me think of it as a bipartite graph: even vertices on one side, odd on the other. Edges connect even $e$ to odd $o$ with label $e + o$. We need a Hamiltonian cycle in this bipartite graph using each label exactly once.

Even vertices: $\{0, 2, 6, 8\}$. Odd vertices: $\{1, 3, 5, 7\}$.

Possible edges (even + odd):
- $0+1=1$, $0+3=3$, $0+5=5$, $0+7=7$
- $2+1=3$, $2+3=5$, $2+5=7$, $2+7=9$
- $6+1=7$, $6+3=9$, $6+5=11$, $6+7=13$
- $8+1=9$, $8+3=11$, $8+5=13$, $8+7=15$

We need to use labels $\{1,3,5,7,9,11,13,15\}$, each exactly once. Each even vertex has degree 2 in the cycle, each odd vertex has degree 2.

Label 1: only $0+1$. So edge $(0,1)$ must be used.
Label 15: only $8+7$. So edge $(8,7)$ must be used.

Label 3: $0+3$ or $2+1$.
Label 5: $0+5$ or $2+3$.
Label 7: $0+7$, $2+5$, or $6+1$.
Label 9: $2+7$, $6+3$, or $8+1$.
Label 11: $6+5$ or $8+3$.
Label 13: $6+7$ or $8+5$.

Vertex 0 already has edge to 1 (label 1). Needs one more edge. Options: $0+3=3$, $0+5=5$, $0+7=7$.
Vertex 8 already has edge to 7 (label 15). Needs one more edge. Options: $8+1=9$, $8+3=11$, $8+5=13$.
Vertex 1 already has edge to 0 (label 1). Needs one more edge. Options: $2+1=3$, $6+1=7$, $8+1=9$.
Vertex 7 already has edge to 8 (label 15). Needs one more edge. Options: $0+7=7$, $2+7=9$, $6+7=13$.

Let me try: vertex 0 connects to 1 (label 1) and 5 (label 5). Vertex 8 connects to 7 (label 15) and 3 (label 11).

Then vertex 1 has edges to 0 (label 1) and needs one more: $2+1=3$, $6+1=7$, $8+1=9$. But 8 already has 2 edges (to 7 and 3). So $8+1$ not available. Options: $2+1=3$ or $6+1=7$.

Vertex 7 has edges to 8 (label 15) and needs one more: $0+7=7$, $2+7=9$, $6+7=13$. But 0 already has 2 edges. So $0+7$ not available. Options: $2+7=9$ or $6+7=13$.

Vertex 5 has edge to 0 (label 5) and needs one more: $2+5=7$, $6+5=11$. But 11 is used by $8+3$. So $6+5=11$ conflicts. Option: $2+5=7$.

Vertex 3 has edge to 8 (label 11) and needs one more: $2+3=5$ (but 5 is used by $0+5$), $6+3=9$. So $6+3=9$.

Now: vertex 5 connects to 0 and 2 (label 7). Vertex 3 connects to 8 and 6 (label 9).
Vertex 2 has edge to 5 (label 7). Needs one more: $2+1=3$, $2+3=5$ (used), $2+7=9$ (used). So $2+1=3$.
Vertex 6 has edge to 3 (label 9). Needs one more: $6+1=7$ (used), $6+5=11$ (used), $6+7=13$. So $6+7=13$.

Now vertex 1 has edges to 0 (label 1) and 2 (label 3). ✓ Degree 2.
Vertex 7 has edges to 8 (label 15) and 6 (label 13). ✓ Degree 2.

Let me verify all labels: 1 (0+1), 5 (0+5), 7 (2+5), 3 (2+1), 11 (8+3), 9 (6+3), 13 (6+7), 15 (8+7). That's $\{1,3,5,7,9,11,13,15\}$. ✓

The cycle: $0 - 1 - 2 - 5 - 0$? No wait, let me trace the cycle.

Edges: $(0,1), (0,5), (2,5), (1,2), (8,3), (6,3), (6,7), (8,7)$.

Starting from 0: $0 - 1 - 2 - 5 - 0$. That's a 4-cycle, not an 8-cycle!

And $8 - 3 - 6 - 7 - 8$. That's another 4-cycle.

We need a single 8-cycle, not two 4-cycles! So this particular assignment doesn't work.

Let me try a different assignment. We need to ensure the graph forms a single cycle, not multiple cycles.

Let me try to be more careful. We need a Hamiltonian cycle in the bipartite graph. Let me think of it as: arrange the even vertices $e_1, e_2, e_3, e_4$ and odd vertices $o_1, o_2, o_3, o_4$ in a cycle $e_1 - o_1 - e_2 - o_2 - e_3 - o_3 - e_4 - o_4 - e_1$.

The sums are $e_1+o_1, e_2+o_1, e_2+o_2, e_3+o_2, e_3+o_3, e_4+o_3, e_4+o_4, e_1+o_4$.

These must be $\{1,3,5,7,9,11,13,15\}$.

Let me try: $e_1=0, o_1=1, e_2=8, o_2=7, e_3=2, o_3=5, e_4=6, o_4=3$.

Sums: $0+1=1, 8+1=9, 8+7=15, 2+7=9$... duplicate 9. No.

Let me try: $e_1=0, o_1=1, e_2=6, o_2=3, e_3=8, o_3=7, e_4=2, o_4=5$.

Sums: $0+1=1, 6+1=7, 6+3=9, 8+3=11, 8+7=15, 2+7=9$... duplicate 9. No.

Let me try: $e_1=0, o_1=1, e_2=6, o_2=5, e_3=2, o_3=7, e_4=8, o_4=3$.

Sums: $0+1=1, 6+1=7, 6+5=11, 2+5=7$... duplicate 7. No.

Let me try: $e_1=0, o_1=3, e_2=2, o_2=5, e_3=6, o_3=7, e_4=8, o_4=1$.

Sums: $0+3=3, 2+3=5, 2+5=7, 6+5=11, 6+7=13, 8+7=15, 8+1=9, 0+1=1$.
Labels: $\{3,5,7,11,13,15,9,1\} = \{1,3,5,7,9,11,13,15\}$. ✓

And the cycle is $0 - 3 - 2 - 5 - 6 - 7 - 8 - 1 - 0$. That's a single 8-cycle! ✓

So $n = 8$ works.

Let me check $n = 12$ ($m = 6$, but $m$ is odd, so $n \equiv 0 \pmod{4}$... wait, $n = 12$, $m = 6$, $m$ is even. $n = 4m' $ where $m' = 3$... hmm let me re-examine.

Wait, I had $n = 2m$ and the condition is $m$ even, i.e., $n \equiv 0 \pmod{4}$. $n = 12$: $m = 6$, which is even. ✓ So $n = 12$ should be feasible.

Actually wait, let me re-examine. $n = 12$, $m = n/2 = 6$. The set is $\{0, 1, \ldots, 12\} \setminus \{6\}$. Even numbers: $\{0, 2, 4, 8, 10, 12\}$ (6 numbers, since we removed 6 which is even). Odd numbers: $\{1, 3, 5, 7, 9, 11\}$ (6 numbers). So 6 even and 6 odd, alternating cycle possible. ✓

Now, the question is: for which multiples of 4 does a solution exist? Let me think about whether $n \equiv 0 \pmod 4$ is both necessary and sufficient.

We've shown:
- $n$ odd: impossible (sum condition gives $a^* = n/2 \notin \mathbb{Z}$)
- $n \equiv 2 \pmod 4$: impossible (can't alternate parities)
- $n \equiv 0 \pmod 4$: necessary conditions satisfied, and we've verified $n = 4$ and $n = 8$ work.

Is $n \equiv 0 \pmod 4$ sufficient? Let me try to construct a general solution.

For $n = 4k$, $m = 2k$. The set is $\{0, 1, \ldots, 4k\} \setminus \{2k\}$. Even numbers: $\{0, 2, \ldots, 4k\} \setminus \{2k\}$, which is $\{0, 2, \ldots, 2k-2, 2k+2, \ldots, 4k\}$, $2k$ numbers. Odd numbers: $\{1, 3, \ldots, 4k-1\}$, $2k$ numbers.

We need an alternating cycle with sums $\{1, 3, 5, \ldots, 8k-1\}$.

Let me think about a construction. Consider the cycle for $n = 8$ ($k = 2$): $0, 3, 2, 5, 6, 7, 8, 1$ (and back to 0). The sums are $3, 5, 7, 11, 13, 15, 9, 1$.

Hmm, let me think about a pattern. For $n = 4$ ($k = 1$): $0, 1, 4, 3$ (and back to 0). Sums: $1, 5, 7, 3$. Wait, let me recheck. The vertices in the $a$-representation are $\{0, 1, 2, 3\}$ (removing $m = 2$). The cycle was $0, 1, 4, 3$... no, wait. For $n = 4$, $m = 2$, the set is $\{0, 1, 3, 4\}$ (removing 2). The cycle I found earlier in the original representation was $0, 2, 8, 6$ which in $a$-representation is $0, 1, 4, 3$. Sums: $0+1=1, 1+4=5, 4+3=7, 3+0=3$. Labels $\{1, 3, 5, 7\}$. ✓

For $n = 8$: cycle in $a$-representation: $0, 3, 2, 5, 6, 7, 8, 1$. Sums: $3, 5, 7, 11, 13, 15, 9, 1$. ✓

Let me see if there's a pattern. For $n = 4$: $0, 1, 4, 3$. For $n = 8$: $0, 3, 2, 5, 6, 7, 8, 1$.

Hmm, let me think about this differently. Maybe I should look for a general construction.

Actually, let me think about it as follows. We have even numbers $E = \{0, 2, \ldots, 2k-2, 2k+2, \ldots, 4k\}$ and odd numbers $O = \{1, 3, \ldots, 4k-1\}$, each of size $2k$. We need a perfect matching-like structure (actually a 2-regular bipartite graph forming a single cycle) where the $4k$ edge sums are exactly $\{1, 3, 5, \ldots, 8k-1\}$.

Let me think of the even numbers as $e_i = 2i$ for $i \in \{0, 1, \ldots, 2k-1, 2k+1, \ldots, 4k\}$... no, that's not right. Let me re-index.

Even numbers: $\{0, 2, 4, \ldots, 2k-2\} \cup \{2k+2, 2k+4, \ldots, 4k\}$. In terms of $a$-values (dividing by 2): $\{0, 1, \ldots, k-1\} \cup \{k+1, k+2, \ldots, 2k\}$.

Odd numbers: $\{1, 3, 5, \ldots, 4k-1\}$. In terms of $b$-values (where odd = $2b+1$, $b = 0, 1, \ldots, 2k-1$): $\{0, 1, \ldots, 2k-1\}$.

Edge sum = even + odd = $2a + (2b+1) = 2(a+b) + 1$. We need these to be $\{1, 3, 5, \ldots, 8k-1\}$, i.e., $a + b \in \{0, 1, 2, \ldots, 4k-1\}$.

So we need a Hamiltonian cycle in the bipartite graph between $A = \{0, 1, \ldots, k-1, k+1, \ldots, 2k\}$ and $B = \{0, 1, \ldots, 2k-1\}$ where edge $(a, b)$ has label $a + b$, and we need all labels $\{0, 1, \ldots, 4k-1\}$ to appear exactly once.

This is equivalent to finding a Hamiltonian cycle in a bipartite graph where the edge labels (sums) form a complete set.

Let me think about this as a graceful labeling or something similar.

Actually, this reminds me of a "Skolem sequence" or "graceful permutation" type problem.

Let me think about it differently. We need to arrange the $A$-values and $B$-values alternately in a cycle: $a_1, b_1, a_2, b_2, \ldots, a_{2k}, b_{2k}, a_1$. The sums $a_i + b_i$ and $a_{i+1} + b_i$ must together form $\{0, 1, \ldots, 4k-1\}$.

Actually, the sums are: $a_1 + b_1, a_2 + b_1, a_2 + b_2, a_3 + b_2, \ldots, a_{2k} + b_{2k}, a_1 + b_{2k}$. These are $4k$ sums that must be $\{0, 1, \ldots, 4k-1\}$.

This is like a "terraces" or "starter" problem in combinatorial design theory.

Let me try to find a pattern by examining the solutions for $k = 1$ and $k = 2$.

$k = 1$ ($n = 4$): $A = \{0, 2\}$, $B = \{0, 1\}$. Cycle: $a = (0, 2)$, $b = (1, 0)$. Sums: $0+1=1, 2+1=3, 2+0=2, 0+0=0$. Labels $\{0,1,2,3\}$. ✓

Wait, but I need to check: the cycle is $0, 1, 2, 0$ (in terms of $a, b$ values). Going back to original: even values $0, 4$ and odd values $3, 1$. Cycle: $0, 3, 4, 1$. Sums (in original): $0+3=3, 4+3=7, 4+1=5, 0+1=1$. Labels $\{1,3,5,7\}$. ✓

$k = 2$ ($n = 8$): $A = \{0, 1, 3, 4\}$, $B = \{0, 1, 2, 3\}$. Cycle: $a = (0, 2, 3, 4)$... wait, $A = \{0, 1, 3, 4\}$ (removing 2). Let me use the cycle $0, 3, 2, 5, 6, 7, 8, 1$ from before. In $a, b$ terms: even values are $0, 6, 4, 8$ (dividing by 2: $0, 3, 2, 4$) and odd values are $7, 5, 15, 1$ (so $b = 3, 2, 7, 0$). Hmm, this is getting confusing.

Let me just try to find a general construction or prove sufficiency.

Actually, let me think about this problem from a higher level. The question asks for the sum of all $n$ in $[3, 100]$ for which a memorable labelling exists. If the answer is "all multiples of 4 in $[3, 100]$", then the sum is $4 + 8 + 12 + \cdots + 100 = 4(1 + 2 + \cdots + 25) = 4 \cdot 325 = 1300$.

But I need to verify that all multiples of 4 work, not just 4 and 8.

Let me try $n = 12$ ($k = 3$). $A = \{0,1,2,4,5,6\}$ (removing 3), $B = \{0,1,2,3,4,5\}$. Need cycle with sums $\{0,1,\ldots,11\}$.

Let me try to construct this. I need to arrange 6 $A$-values and 6 $B$-values alternately.

Let me try: $a = (0, 2, 4, 6, 5, 1)$, $b = (0, 1, 3, 5, 4, 2)$.

Sums: $a_1+b_1 = 0, a_2+b_1 = 2, a_2+b_2 = 3, a_3+b_2 = 5, a_3+b_3 = 7, a_4+b_3 = 9, a_4+b_4 = 11, a_5+b_4 = 10, a_5+b_5 = 9$... duplicate 9. No.

This trial and error is slow. Let me think more systematically.

Actually, let me think about this as follows. We need a permutation $\sigma$ of $A$ and $\tau$ of $B$ such that the $4k$ values $\{\sigma(i) + \tau(i), \sigma(i+1) + \tau(i) : i = 1, \ldots, 2k\}$ (with cyclic indexing) are exactly $\{0, 1, \ldots, 4k-1\}$.

Equivalently, if we write the cycle as $a_1, b_1, a_2, b_2, \ldots, a_{2k}, b_{2k}$, the sums $a_i + b_i$ (for $i = 1, \ldots, 2k$) and $a_{i+1} + b_i$ (for $i = 1, \ldots, 2k$, with $a_{2k+1} = a_1$) must be $\{0, 1, \ldots, 4k-1\}$.

Note that $a_i + b_i$ and $a_{i+1} + b_i$ share $b_i$. Their difference is $a_{i+1} - a_i$.

Hmm, let me think about a different approach. Let me consider the "differences" $d_i = a_{i+1} - a_i$ (cyclically). Then the sums are $a_i + b_i$ and $a_i + d_i + b_i = (a_i + b_i) + d_i$. So the $4k$ sums come in pairs: $s_i$ and $s_i + d_i$ where $s_i = a_i + b_i$.

We need $\{s_i, s_i + d_i : i = 1, \ldots, 2k\} = \{0, 1, \ldots, 4k-1\}$.

Also, the $b$-values are a permutation of $B$, and $b_i = s_i - a_i$. The $a$-values are a permutation of $A$.

This is still complex. Let me try a different approach: look for a constructive pattern.

For $k = 1$: cycle in $(a,b)$ terms: $a = (0, 2), b = (1, 0)$. Sums: $(0+1, 2+1, 2+0, 0+0) = (1, 3, 2, 0)$. All of $\{0,1,2,3\}$. ✓

For $k = 2$: Let me find the $(a,b)$ representation. The cycle was $0, 3, 2, 5, 6, 7, 8, 1$ in the original $a$-representation (where vertices are $2a$). Wait, I need to be more careful.

For $n = 8$, the original vertex values (in the $\{0,...,16\}$ representation) are even numbers. The $a$-values (dividing by 2) are from $\{0, 1, 2, 3, 5, 6, 7, 8\}$ (removing 4). The cycle in $a$-values: $0, 3, 2, 5, 6, 7, 8, 1$.

Now, the even $a$-values are $\{0, 2, 6, 8\}$ and odd $a$-values are $\{1, 3, 5, 7\}$. The cycle alternates: $0$ (even), $3$ (odd), $2$ (even), $5$ (odd), $6$ (even), $7$ (odd), $8$ (even), $1$ (odd). ✓

In the $(a, b)$ representation where $a$ = even $a$-value / 1 (i.e., the even $a$-values themselves) and $b$ = (odd $a$-value - 1)/2:

Even $a$-values: $0, 2, 6, 8$. These are the $A$-set: $\{0, 1, 3, 4\}$ (dividing by 2).
Odd $a$-values: $3, 5, 7, 1$. These correspond to $B$-set: $(3-1)/2 = 1, (5-1)/2 = 2, (7-1)/2 = 3, (1-1)/2 = 0$. So $B$-order: $1, 2, 3, 0$.

The cycle in terms of $(A, B)$: $A_1=0, B_1=1, A_2=1, B_2=2, A_3=3, B_3=3, A_4=4, B_4=0$.

Sums: $A_i + B_i$ and $A_{i+1} + B_i$:
- $A_1 + B_1 = 0 + 1 = 1$
- $A_2 + B_1 = 1 + 1 = 2$
- $A_2 + B_2 = 1 + 2 = 3$
- $A_3 + B_2 = 3 + 2 = 5$
- $A_3 + B_3 = 3 + 3 = 6$
- $A_4 + B_3 = 4 + 3 = 7$
- $A_4 + B_4 = 4 + 0 = 4$
- $A_1 + B_4 = 0 + 0 = 0$

Sums: $\{0, 1, 2, 3, 4, 5, 6, 7\}$. ✓

So the pattern for the $(A, B)$ cycle:
- $k = 1$: $A = (0, 2), B = (1, 0)$. But $A$-set is $\{0, 2\}$... wait, for $k = 1$, $A = \{0, 2\}$ and $B = \{0, 1\}$. Hmm, $A$-values are $\{0, 2\}$ but in the $(a,b)$ rep, $A$ should be $\{0, 1, \ldots, k-1, k+1, \ldots, 2k\} = \{0, 2\}$ for $k = 1$. And $B = \{0, 1, \ldots, 2k-1\} = \{0, 1\}$.

Cycle: $A = (0, 2), B = (1, 0)$.
Sums: $0+1=1, 2+1=3, 2+0=2, 0+0=0$. $\{0,1,2,3\}$. ✓

- $k = 2$: $A = (0, 1, 3, 4), B = (1, 2, 3, 0)$.
Sums: $1, 2, 3, 5, 6, 7, 4, 0$. $\{0,1,2,3,4,5,6,7\}$. ✓

Let me look for a pattern. For $k = 1$: $A = (0, 2), B = (1, 0)$.
For $k = 2$: $A = (0, 1, 3, 4), B = (1, 2, 3, 0)$.

Hmm, let me look at the $A$ sequences: $0, 2$ and $0, 1, 3, 4$. The $B$ sequences: $1, 0$ and $1, 2, 3, 0$.

For $k = 2$, $A = (0, 1, 3, 4)$: this is $\{0, 1, \ldots, 2k\} \setminus \{k\} = \{0, 1, 3, 4\}$ in order but with $k = 2$ removed. And $B = (1, 2, 3, 0)$: this is a cyclic shift of $(0, 1, 2, 3)$.

Let me check if $A = (0, 1, \ldots, k-1, k+1, \ldots, 2k)$ and $B = (1, 2, \ldots, 2k-1, 0)$ works in general.

For general $k$: $A = (0, 1, \ldots, k-1, k+1, k+2, \ldots, 2k)$, $B = (1, 2, \ldots, 2k-1, 0)$.

The $A$ sequence has $2k$ elements: $0, 1, \ldots, k-1, k+1, \ldots, 2k$.
The $B$ sequence has $2k$ elements: $1, 2, \ldots, 2k-1, 0$.

Sums $A_i + B_i$:
- For $i = 1, \ldots, k-1$: $A_i = i-1, B_i = i$. Sum = $2i - 1$.
- For $i = k$: $A_k = k-1, B_k = k$. Sum = $2k - 1$.
- For $i = k+1$: $A_{k+1} = k+1, B_{k+1} = k+1$. Sum = $2k + 2$.
- For $i = k+2, \ldots, 2k-1$: $A_i = i, B_i = i$. Sum = $2i$.
- For $i = 2k$: $A_{2k} = 2k, B_{2k} = 0$. Sum = $2k$.

Wait, let me be more careful. $A = (0, 1, 2, \ldots, k-1, k+1, k+2, \ldots, 2k)$. So:
- $A_1 = 0, A_2 = 1, \ldots, A_k = k-1, A_{k+1} = k+1, A_{k+2} = k+2, \ldots, A_{2k} = 2k$.

$B = (1, 2, 3, \ldots, 2k-1, 0)$. So:
- $B_1 = 1, B_2 = 2, \ldots, B_{2k-1} = 2k-1, B_{2k} = 0$.

Sums $A_i + B_i$:
- $i = 1$: $0 + 1 = 1$
- $i = 2$: $1 + 2 = 3$
- ...
- $i = k$: $(k-1) + k = 2k-1$
- $i = k+1$: $(k+1) + (k+1) = 2k+2$
- $i = k+2$: $(k+2) + (k+2) = 2k+4$
- ...
- $i = 2k-1$: $(2k-1) + (2k-1) = 4k-2$
- $i = 2k$: $2k + 0 = 2k$

So $A_i + B_i$ gives: $\{1, 3, 5, \ldots, 2k-1\} \cup \{2k+2, 2k+4, \ldots, 4k-2\} \cup \{2k\}$.

That's $\{1, 3, \ldots, 2k-1, 2k, 2k+2, 2k+4, \ldots, 4k-2\}$. Missing from $\{0, \ldots, 4k-1\}$: $\{0, 2, 4, \ldots, 2k-2, 2k+1, 2k+3, \ldots, 4k-1\}$.

Now sums $A_{i+1} + B_i$ (with $A_{2k+1} = A_1 = 0$):
- $i = 1$: $A_2 + B_1 = 1 + 1 = 2$
- $i = 2$: $A_3 + B_2 = 2 + 2 = 4$
- ...
- $i = k-1$: $A_k + B_{k-1} = (k-1) + (k-1) = 2k-2$
- $i = k$: $A_{k+1} + B_k = (k+1) + k = 2k+1$
- $i = k+1$: $A_{k+2} + B_{k+1} = (k+2) + (k+1) = 2k+3$
- $i = k+2$: $A_{k+3} + B_{k+2} = (k+3) + (k+2) = 2k+5$
- ...
- $i = 2k-2$: $A_{2k-1} + B_{2k-2} = (2k-1) + (2k-2) = 4k-3$
- $i = 2k-1$: $A_{2k} + B_{2k-1} = 2k + (2k-1) = 4k-1$
- $i = 2k$: $A_1 + B_{2k} = 0 + 0 = 0$

So $A_{i+1} + B_i$ gives: $\{2, 4, 6, \ldots, 2k-2\} \cup \{2k+1, 2k+3, \ldots, 4k-1\} \cup \{0\}$.

That's $\{0, 2, 4, \ldots, 2k-2, 2k+1, 2k+3, \ldots, 4k-1\}$.

Combined with the $A_i + B_i$ sums: $\{1, 3, \ldots, 2k-1, 2k, 2k+2, \ldots, 4k-2\}$.

Total: $\{0, 1, 2, \ldots, 2k-2, 2k-1, 2k, 2k+1, 2k+2, \ldots, 4k-2, 4k-1\} = \{0, 1, \ldots, 4k-1\}$. ✓

So the construction works for all $k$! But wait, I need to check that the $B$ values form a valid permutation (all distinct) and the $A$ values form a valid permutation (all distinct), and that the cycle is a single cycle (not multiple cycles).

$A = (0, 1, \ldots, k-1, k+1, \ldots, 2k)$: these are all distinct, forming the set $\{0, \ldots, 2k\} \setminus \{k\}$. ✓
$B = (1, 2, \ldots, 2k-1, 0)$: these are all distinct, forming $\{0, 1, \ldots, 2k-1\}$. ✓

Now, is the cycle a single Hamiltonian cycle? The cycle in the bipartite graph is $A_1 - B_1 - A_2 - B_2 - \cdots - A_{2k} - B_{2k} - A_1$. This visits all $A$-vertices and all $B$-vertices, so it's a Hamiltonian cycle by construction (as long as all $A_i$ are distinct and all $B_i$ are distinct, which they are).

Wait, but I need to make sure it's actually a single cycle, not that it visits the same vertex twice. Since all $A_i$ are distinct and all $B_i$ are distinct, and the cycle alternates between $A$ and $B$ vertices, it visits each vertex exactly once. So it is a single Hamiltonian cycle. ✓

But wait, I also need to verify that the edge sums are all distinct, which I just did above — they form $\{0, 1, \ldots, 4k-1\}$.

So the construction works for all $k \geq 1$, meaning for all $n = 4k \geq 4$.

Let me also verify that $n$ must be a multiple of 4. We showed:
1. $n$ odd: impossible (sum condition).
2. $n \equiv 2 \pmod{4}$: impossible (parity alternation fails).
3. $n \equiv 0 \pmod{4}$: construction exists.

So the answer is: memorable labellings exist if and only if $n \equiv 0 \pmod{4}$.

The multiples of 4 in $[3, 100]$ are $4, 8, 12, \ldots, 100$. There are $25$ of them. Their sum is $4 \cdot (1 + 2 + \cdots + 25) = 4 \cdot 325 = 1300$.

Wait, but I should double-check the necessity more carefully. Let me re-examine the case $n \equiv 2 \pmod 4$.

For $n$ even, we showed only the all-even vertices case is possible. The set is $\{0, 1, \ldots, n\} \setminus \{n/2\}$, and we need a cyclic arrangement with consecutive sums being $\{1, 3, 5, \ldots, 2n-1\}$ (all odd). For sums to be odd, consecutive elements must have different parities, requiring an alternating cycle. The set $\{0, 1, \ldots, n\} \setminus \{n/2\}$ has:
- $n/2 + 1$ even numbers (from $\{0, 2, \ldots, n\}$) minus 1 if $n/2$ is even, plus...
  
Let me recount. $\{0, 1, \ldots, n\}$ has $\lfloor n/2 \rfloor + 1$ even numbers and $\lceil n/2 \rceil$ odd numbers. For $n$ even: $n/2 + 1$ even and $n/2$ odd. Removing $n/2$: if $n/2$ is even (i.e., $n \equiv 0 \pmod 4$), we get $n/2$ even and $n/2$ odd. If $n/2$ is odd (i.e., $n \equiv 2 \pmod 4$), we get $n/2 + 1$ even and $n/2 - 1$ odd.

For alternating cycle, need equal even and odd: $n/2 = n/2$ (when $n \equiv 0 \pmod 4$) ✓, or $n/2 + 1 = n/2 - 1$ (when $n \equiv 2 \pmod 4$) ✗.

So indeed $n \equiv 2 \pmod 4$ is impossible. ✓

And for $n$ odd, we showed the sum condition requires $a^* = n/2 \notin \mathbb{Z}$, so impossible. ✓

Therefore, the answer is the sum of all multiples of 4 from 4 to 100, which is $4(1 + 2 + \cdots + 25) = 4 \cdot \frac{25 \cdot 26}{2} = 4 \cdot 325 = 1300$.

Let me also verify the construction once more for $k = 1$ ($n = 4$).

$A = (0, 2), B = (1, 0)$. Cycle: $0 - 1 - 2 - 0 - 0$... wait, the cycle is $A_1, B_1, A_2, B_2, A_1 = 0, 1, 2, 0, 0$. Hmm, that doesn't look right. The cycle should be $A_1 - B_1 - A_2 - B_2 - A_1$, which is $0 - 1 - 2 - 0 - 0$. But $B_2 = 0$ and $A_1 = 0$, so the last edge is $B_2 - A_1 = 0 - 0$. But $A$ and $B$ are different sets (bipartite), so $A_1 = 0$ (an $A$-vertex) and $B_2 = 0$ (a $B$-vertex) are different vertices even though they have the same value. In the original problem, the $A$-vertices correspond to even numbers and $B$-vertices to odd numbers, so they're distinct.

Going back to the original: $A$-values $\{0, 2\}$ correspond to even vertex labels $\{0, 4\}$ (multiplying by 2). $B$-values $\{0, 1\}$ correspond to odd vertex labels... wait, no. Let me re-derive.

For $n = 4$ ($k = 1$, $m = 2$): The $a$-values (half of even vertex labels) are from $\{0, 1, 2, 3, 4\} \setminus \{2\} = \{0, 1, 3, 4\}$. The even $a$-values are $\{0, 4\}$ (dividing by 2: $\{0, 2\}$, which is the $A$-set). The odd $a$-values are $\{1, 3\}$ (corresponding to $B = \{0, 1\}$ where $b = (a_{\text{odd}} - 1)/2$).

The cycle in $a$-values: $A_1 = 0, B_1 = 1, A_2 = 2, B_2 = 0$, meaning $a$-values: $0, 1, 4, 3$ (since $A$-value $0 \to a = 0$, $B$-value $1 \to a = 2 \cdot 1 + 1 = 3$... wait, I'm getting confused.

Let me just go back to the direct construction. For $n = 4k$, the vertex labels (in the $\{0, \ldots, 2n\}$ representation) are even numbers $\{0, 2, \ldots, 2n\} \setminus \{n\}$. The $a$-values (dividing by 2) are $\{0, 1, \ldots, n\} \setminus \{n/2\}$.

The cycle in $a$-values is: $A_1, 2B_1 + 1, A_2, 2B_2 + 1, \ldots$ where $A_i$ are even $a$-values and $2B_i + 1$ are odd $a$-values.

Wait, I think I overcomplicated this. Let me just directly verify the construction gives a valid memorable labelling.

For $n = 4k$:
- Vertices (even labels): $2 \cdot a_i$ where $a_i$ ranges over $\{0, 1, \ldots, n\} \setminus \{n/2\}$ in the cyclic order given by the construction.
- The cyclic order of $a$-values: $0, 1, 2, \ldots, k-1, k+1, k+2, \ldots, 2k, 2k+1, 2k+2, \ldots$... 

Hmm wait, I need to be more careful. The $A$-set is $\{0, 1, \ldots, k-1, k+1, \ldots, 2k\}$ (even $a$-values divided by 2... no, the $A$-set IS the even $a$-values, and the $B$-set represents the odd $a$-values).

Actually, I realize I need to be more careful about the mapping. Let me re-derive.

For $n = 4k$, $m = n/2 = 2k$. The $a$-values are $\{0, 1, \ldots, 2k\} \setminus \{k\}$... no wait, $n/2 = 2k$, so the $a$-values are $\{0, 1, \ldots, n\} \setminus \{n/2\} = \{0, 1, \ldots, 4k\} \setminus \{2k\}$.

Hmm, I think I mixed up notation. Let me restart the construction more carefully.

For $n = 4k$:
- Consecutive integers: $\{0, 1, \ldots, 2n\} = \{0, 1, \ldots, 8k\}$.
- Interior label: $n = 4k$.
- Vertices: all even numbers from $\{0, 2, 4, \ldots, 8k\} \setminus \{4k\}$. These are $\{0, 2, \ldots, 4k-2, 4k+2, \ldots, 8k\}$, total $4k$ numbers. Wait, $\{0, 2, \ldots, 8k\}$ has $4k + 1$ numbers, removing $4k$ gives $4k$ numbers. ✓
- Sides: all odd numbers from $\{1, 3, \ldots, 8k-1\}$, total $4k$ numbers. ✓

Now, write vertex labels as $2a_i$ where $a_i \in \{0, 1, \ldots, 4k\} \setminus \{2k\}$. Side labels are $a_i + a_{i+1}$ (since $(2a_i + 2a_{i+1})/2 = a_i + a_{i+1}$). We need $\{a_i + a_{i+1}\} = \{1, 3, 5, \ldots, 8k-1\}$.

For sums to be odd, consecutive $a_i$ must have different parities. The set $\{0, 1, \ldots, 4k\} \setminus \{2k\}$ has:
- Even $a$-values: $\{0, 2, \ldots, 4k\} \setminus \{2k\}$. Since $2k$ is even, this has $2k$ elements.
- Odd $a$-values: $\{1, 3, \ldots, 4k-1\}$. This has $2k$ elements.

So we need an alternating cycle of $2k$ even and $2k$ odd $a$-values.

Even $a$-values: $\{0, 2, \ldots, 2k-2, 2k+2, \ldots, 4k\}$. Let me write these as $2u$ where $u \in \{0, 1, \ldots, k-1, k+1, \ldots, 2k\}$. So the $u$-set is $U = \{0, 1, \ldots, k-1, k+1, \ldots, 2k\}$, $|U| = 2k$.

Odd $a$-values: $\{1, 3, \ldots, 4k-1\}$. Write as $2v + 1$ where $v \in \{0, 1, \ldots, 2k-1\}$. So $V = \{0, 1, \ldots, 2k-1\}$, $|V| = 2k$.

The cycle alternates: $2u_1, 2v_1+1, 2u_2, 2v_2+1, \ldots, 2u_{2k}, 2v_{2k}+1, 2u_1$.

Side sums: $(2u_i + 2v_i + 1) = 2(u_i + v_i) + 1$ and $(2u_{i+1} + 2v_i + 1) = 2(u_{i+1} + v_i) + 1$.

We need $\{2(u_i + v_i) + 1, 2(u_{i+1} + v_i) + 1\} = \{1, 3, \ldots, 8k-1\}$, i.e., $\{u_i + v_i, u_{i+1} + v_i\} = \{0, 1, \ldots, 4k-1\}$.

This is exactly the $(A, B)$ formulation I had before, with $A = U$ and $B = V$.

My construction: $U$-sequence = $(0, 1, \ldots, k-1, k+1, \ldots, 2k)$ and $V$-sequence = $(1, 2, \ldots, 2k-1, 0)$.

I verified that the sums $\{u_i + v_i, u_{i+1} + v_i\}$ give exactly $\{0, 1, \ldots, 4k-1\}$.

And the cycle is a single Hamiltonian cycle since all $u_i$ are distinct and all $v_i$ are distinct.

So the construction is valid for all $k \geq 1$, i.e., all $n = 4k \geq 4$.

Therefore, a memorable labelling exists if and only if $4 | n$.

The multiples of 4 in $[3, 100]$: $4, 8, 12, \ldots, 100$. Count: $\lfloor 100/4 \rfloor = 25$. Sum: $4 \cdot (1 + 2 + \cdots + 25) = 4 \cdot 325 = 1300$.

The answer is $\boxed{1300}$.

Now let me write up the proof properly.
