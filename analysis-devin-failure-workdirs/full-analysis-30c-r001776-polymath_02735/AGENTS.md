# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let $S = \{s_1, s_2, \dots, s_{10}\}$ be a set of 10 distinct complex numbers such that exactly $10-3=7$ of them are real numbers. Let $N$ be the maximum possible number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$ (meaning $f$ maps $S$ onto itself). Find the value of $N$.       — 题目文本
#   Based on the original solution, any such quadratic polynomial $f$ must have real coefficients because $n \ge 9$. The three non-real complex numbers $z_1, z_2, z_3$ in $S$ must be permuted by $f$. Case (1) where two are conjugates leads to at most one such quadratic polynomial. Case (2) where no two are conjugates leads to at most two possible permutations (3-cycles) and hence at most two polynomials. In either case, the maximum number of such quadratic polynomials is 2.  — 标准解答
#   Let me solve this problem. We have a set $S$ of 10 distinct complex numbers, exactly 7 real and 3 non-real. We need to find the maximum number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$ (i.e., $f$ permutes $S$).

Let me think about this carefully.

A quadratic polynomial $f(z) = az^2 + bz + c$ with $a \neq 0$ maps $S$ to itself as a set. Since $f$ is a function (not necessarily injective on $\mathbb{C}$), $f(S) = S$ means $f$ maps $S$ onto $S$.

Since $|S| = 10$ and $f(S) = S$, $f$ restricted to $S$ is a surjection from $S$ to $S$, hence a bijection (since $S$ is finite). So $f$ permutes the elements of $S$.

Now, a quadratic polynomial is a degree-2 map. The key constraint: $f$ is a permutation of $S$, but $f$ is a degree-2 polynomial.

Let me think about the structure. If $f$ permutes $S$, then for any $s \in S$, the orbit of $s$ under $f$ is a cycle. The cycle structure of the permutation must be compatible with $f$ being a polynomial of degree 2.

Key fact: If $f$ is a polynomial of degree $d$ and $f$ permutes a finite set $S$, then the cycle lengths divide... well, let me think differently.

Actually, let me think about this more carefully. The real numbers and non-real numbers.

If $f(z) = az^2 + bz + c$ with complex coefficients. The non-real elements come in conjugate pairs (since exactly 3 non-real... wait, no. The 3 non-real elements don't have to be closed under conjugation. The set $S$ is just 10 distinct complex numbers, 7 real and 3 non-real. The 3 non-real ones could be anything.

Wait, but $f$ has complex coefficients, so $f$ doesn't need to respect conjugation.

Let me reconsider. We want to maximize the number of quadratic polynomials $f$ such that $f(S) = S$. We get to choose $S$ (the 10 numbers, 7 real, 3 non-real) to maximize this count.

So the question is: over all choices of $S$ (7 real, 3 non-real, all distinct), what is the maximum number of quadratic polynomials $f$ with $f(S) = S$?

Let me think about what constraints a quadratic polynomial permutation of $S$ must satisfy.

If $f$ is a quadratic polynomial and $f$ permutes $S$ (a set of 10 points), then $f$ is determined by its values on any 3 points (since a quadratic has 3 coefficients, well 3 complex coefficients $a, b, c$ with $a \neq 0$). Actually, a quadratic is determined by its values at 3 distinct points. So if we know $f(s_1), f(s_2), f(s_3)$ for 3 distinct points, $f$ is uniquely determined.

So the number of quadratic polynomials permuting $S$ is at most the number of permutations of $S$ that can be realized as a quadratic polynomial. Since a quadratic is determined by 3 values, we need the permutation to agree with some quadratic on all 10 points.

Let me think about the cycle structure. If $f$ permutes $S$ and $f$ is a polynomial of degree 2, consider the iterates $f, f^2, f^3, \ldots$. The permutation has some cycle structure.

Key observation: If $f$ has a cycle of length $k$ in $S$, i.e., $f^k(s) = s$ for some $s \in S$, then $f^k(z) - z$ is a polynomial of degree $2^k$ that vanishes at $s$. But $f^k(z) - z$ vanishes at all elements in the cycle of $s$.

Actually, let me think about it differently. Let's consider the functional graph. $f: S \to S$ is a permutation, so it decomposes into cycles.

For a quadratic polynomial, the equation $f(z) = w$ has at most 2 solutions for any $w$. So in the permutation, each element has exactly one preimage (since it's a bijection), but the polynomial $f(z) = w$ has at most 2 solutions in $\mathbb{C}$. So for each $w \in S$, exactly one of the (at most 2) preimages under $f$ is in $S$.

Hmm, this doesn't immediately constrain things much.

Let me think about fixed points. $f(z) = z$ is a quadratic equation (assuming $a \neq 0$), so it has at most 2 solutions. So $f$ has at most 2 fixed points in $S$.

More generally, $f^k(z) = z$ is a polynomial equation of degree $2^k$, so it has at most $2^k$ solutions. The number of elements in $S$ that are in cycles of length dividing $k$ is at most $2^k$.

So the cycle structure of the permutation $f|_S$ must satisfy: the number of elements in cycles of length dividing $k$ is at most $2^k$ for each $k$.

For $k=1$: at most 2 fixed points.
For $k=2$: at most 4 elements in cycles of length 1 or 2.
For $k=3$: at most 8 elements in cycles of length 1, 2, or 3 (well, dividing 3, so 1 or 3). At most 8 elements in cycles of length 1 or 3.
For $k=4$: at most 16 elements in cycles of length dividing 4 (1, 2, 4). Since we only have 10 elements, this is automatically satisfied.

Wait, but we need to be more careful. $f^k(z) = z$ has degree $2^k$, so at most $2^k$ roots. The elements of $S$ in cycles of length dividing $k$ are roots of $f^k(z) - z = 0$. So:

- Cycles of length dividing $k$: total elements $\leq 2^k$.

For 10 elements:
- Fixed points (length 1): $\leq 2$
- Elements in cycles of length 1 or 2: $\leq 4$
- Elements in cycles of length 1 or 3: $\leq 8$
- Elements in cycles of length 1, 2, or 4: $\leq 16$ (no constraint for 10 elements)
- Elements in cycles of length 1 or 5: $\leq 32$ (no constraint)
- Elements in cycles of length 1, 2, 3, or 6: $\leq 64$ (no constraint)

So the constraints are mainly from $k=1, 2, 3$.

Let me enumerate possible cycle structures for a permutation of 10 elements, subject to:
- At most 2 fixed points
- At most 4 elements in cycles of length $\leq 2$
- At most 8 elements in cycles of length 1 or 3

Let me denote the cycle structure. Let $c_k$ = number of cycles of length $k$.

Constraint 1: $c_1 \leq 2$.
Constraint 2: $c_1 + 2c_2 \leq 4$.
Constraint 3: $c_1 + 3c_3 \leq 8$.
Total: $c_1 + 2c_2 + 3c_3 + 4c_4 + 5c_5 + \ldots = 10$.

From constraint 2: $c_1 + 2c_2 \leq 4$, so $2c_2 \leq 4 - c_1 \leq 4$, so $c_2 \leq 2$.

Let me think about what cycle structures are possible. The remaining elements (those not in cycles of length 1, 2, or 3) must be in cycles of length $\geq 4$.

Elements in cycles of length $\geq 4$: $10 - (c_1 + 2c_2 + 3c_3) \geq 10 - (4 + 3c_3)$. 

Hmm, this is getting complicated. Let me think about which cycle structures can actually be realized by a quadratic polynomial, and then count how many distinct quadratic polynomials can permute the same set $S$.

Actually, the question is about maximizing the number of quadratic polynomials $f$ with $f(S) = S$ over all choices of $S$. So we need to find $S$ that is invariant under as many quadratic polynomials as possible.

Let me think about this differently. If $f$ and $g$ are both quadratic polynomials with $f(S) = S$ and $g(S) = S$, what can we say?

If $f$ and $g$ agree on 3 points of $S$, then $f = g$ (since a quadratic is determined by 3 points). So distinct quadratic polynomials permuting $S$ must differ on every set of 3 points, meaning they can agree on at most 2 points of $S$.

The number of quadratic polynomials permuting $S$ is at most... well, each such polynomial is a permutation of $S$, and two distinct ones agree on at most 2 points. 

If we have $m$ quadratic polynomials permuting $S$, each pair agrees on at most 2 points. The total number of "agreements" (pairs $(f, g, s)$ where $f(s) = g(s)$, $f \neq g$, $s \in S$) is at most $\binom{m}{2} \cdot 2 = m(m-1)$.

On the other hand, for each $s \in S$, the values $f_1(s), f_2(s), \ldots, f_m(s)$ are elements of $S$ (since each $f_i$ permutes $S$). The number of agreements at point $s$ is $\sum_{v \in S} \binom{|\{i : f_i(s) = v\}|}{2}$. 

Hmm, this is getting complicated. Let me think about specific constructions.

A key example: Consider $S$ being the set of 10th roots of unity... no, those are all on the unit circle, not 7 real.

Let me think about what sets can be invariant under multiple quadratic polynomials.

Example 1: $f(z) = z^2$. This maps roots of unity to roots of unity. If $S$ consists of 10th roots of unity... but those aren't 7 real.

Example 2: Consider Chebyshev-like maps. $f(z) = z^2 - 2$ maps $[-2, 2]$ to $[-2, 2]$ in some sense (via the substitution $z = 2\cos\theta$, $f(2\cos\theta) = 4\cos^2\theta - 2 = 2\cos(2\theta)$). So if $S = \{2\cos(2\pi k / n) : k = 0, 1, \ldots, n-1\}$, then $f$ permutes $S$ (it's the doubling map mod $n$ on the indices). But these are all real.

We need 7 real and 3 non-real. So we can't use a purely real set.

Let me think about this more carefully. We need to find $S$ with 7 real and 3 non-real elements, and maximize the number of quadratic polynomials permuting $S$.

Let me consider the group of quadratic polynomial symmetries of $S$. If $f$ and $g$ both permute $S$, does $f \circ g$ permute $S$? Yes, but $f \circ g$ is a degree-4 polynomial, not quadratic. So the set of quadratic polynomials permuting $S$ doesn't form a group under composition.

However, if $f$ is a quadratic polynomial permuting $S$, then $f^k$ also permutes $S$ for all $k$, but $f^k$ has degree $2^k$, so only $f^1$ is quadratic.

Let me think about the problem from the perspective of counting. A quadratic polynomial $f(z) = az^2 + bz + c$ is determined by $(a, b, c)$ with $a \neq 0$. The condition $f(S) = S$ means $f$ permutes $S$.

Given that $f$ is determined by 3 points, and $f$ must map $S$ to $S$, we can think of it as: choose a permutation $\sigma$ of $S$, and check if there's a quadratic polynomial realizing $\sigma$ on $S$. The quadratic is determined by any 3 values, so we need the permutation to be consistent with a single quadratic on all 10 points.

Let me think about upper bounds. 

Approach: Consider the real and non-real elements separately.

If $f(z) = az^2 + bz + c$ has complex coefficients, it doesn't preserve the real line in general. But if $a, b, c$ are all real, then $f$ maps real numbers to real numbers and $\bar{z}$ to $\overline{f(z)}$.

Case 1: $f$ has real coefficients. Then $f$ maps the 7 real elements of $S$ to real numbers, so $f$ maps the real part of $S$ to real numbers. Since $f(S) = S$ and $f$ maps reals to reals, $f$ must map the 7 real elements to the 7 real elements (bijectively). And $f$ maps the 3 non-real elements to the 3 non-real elements. But wait, $f$ with real coefficients maps non-real $z$ to $f(z)$, and $\overline{f(z)} = f(\bar{z})$. If $z$ is non-real and $\bar{z} \notin S$, then $f(z)$ could be anything. But $f(z) \in S$ and $f(z)$ is non-real (since if $f(z)$ were real, then $f(\bar{z}) = \overline{f(z)} = f(z)$, but $\bar{z} \neq z$ so $f(\bar{z}) \neq f(z)$ is not necessarily true... wait, $f(\bar{z}) = \overline{f(z)}$, and if $f(z)$ is real then $f(\bar{z}) = f(z)$, meaning $f$ maps both $z$ and $\bar{z}$ to the same value, contradicting injectivity on $S$ (unless $\bar{z} \notin S$).

Hmm, let me be more careful. If $f$ has real coefficients and $f(S) = S$ (bijectively), then:
- $f$ maps the 7 real elements bijectively to the 7 real elements.
- $f$ maps the 3 non-real elements bijectively to the 3 non-real elements.
- For non-real $z \in S$, $f(z)$ is non-real (because if $f(z)$ were real, then $f(\bar{z}) = \overline{f(z)} = f(z)$, but since $f$ is injective on $S$ and $z \neq \bar{z}$, we'd need $\bar{z} \notin S$ for this to not be a contradiction... actually even if $\bar{z} \notin S$, $f(z)$ being real is fine as long as $f(z) \in S$. Wait, but I said $f$ maps non-real elements to non-real elements. Let me re-examine.

If $f$ has real coefficients, $f$ maps $\mathbb{R}$ to $\mathbb{R}$. So the 7 real elements of $S$ map to real numbers. Since $f(S) = S$ and $f$ is injective on $S$, the 7 real elements map to 7 distinct real numbers in $S$, which must be the 7 real elements. So the 3 non-real elements map to the 3 non-real elements. ✓

Case 2: $f$ has non-real coefficients. Then $f$ might map real elements to non-real elements and vice versa.

So we need to count both types.

Let me first think about Case 1 (real coefficients). We need quadratic polynomials with real coefficients that permute a set of 7 real numbers and separately permute a set of 3 non-real numbers.

For the 7 real numbers: $f$ restricted to them is a permutation, and $f$ is a real quadratic. $f(z) = w$ has at most 2 real solutions (or 0 or 1). Since $f$ is a bijection on the 7 real numbers, each real number in $S$ has exactly one preimage in $S$ under $f$, but the equation $f(z) = w$ has at most 2 solutions in $\mathbb{R}$.

The cycle structure on the 7 real elements must satisfy: fixed points $\leq 2$, elements in cycles of length $\leq 2$ is $\leq 4$, etc. (same constraints as before but for 7 elements).

For the 3 non-real elements: $f$ permutes them. $f(z) = w$ has at most 2 solutions in $\mathbb{C}$, so the 3 non-real elements, each has one preimage among the 3 non-real elements. The cycle structure on 3 elements: could be (3), (2,1), (1,1,1). Fixed points $\leq 2$ is fine. Cycles of length $\leq 2$: at most 4, fine for 3 elements.

But wait, there's an additional constraint for real coefficients: if $z$ is non-real and $f(z) = w$, then $f(\bar{z}) = \bar{w}$. If $\bar{z} \notin S$, this doesn't directly constrain things. But the 3 non-real elements: their conjugates may or may not be in $S$.

Actually, the 3 non-real elements of $S$ don't need to be closed under conjugation. But if $f$ has real coefficients, $f$ maps the 3 non-real elements to the 3 non-real elements, and conjugation commutes with $f$. So if $z$ is a non-real element of $S$ and $\bar{z} \in S$, then $f(\bar{z}) = \overline{f(z)}$, so the permutation on non-real elements respects conjugation.

This is getting complex. Let me try a different approach and think about specific constructions.

Let me think about what's the maximum number of quadratic polynomials that can permute a set of 10 points.

Upper bound approach: Each quadratic polynomial permuting $S$ is determined by its values on any 3 points of $S$. Two distinct quadratics agree on at most 2 points (since their difference is a polynomial of degree $\leq 2$, which has at most 2 roots). 

So if we have $m$ quadratics $f_1, \ldots, f_m$ permuting $S$, any two agree on at most 2 points. 

For each point $s \in S$, the values $f_1(s), \ldots, f_m(s)$ are in $S$. The number of pairs $(i, j)$ with $f_i(s) = f_j(s)$ is $\sum_{v \in S} \binom{n_v(s)}{2}$ where $n_v(s) = |\{i : f_i(s) = v\}|$ and $\sum_v n_v(s) = m$.

Total agreements: $\sum_{s \in S} \sum_{v} \binom{n_v(s)}{2} \leq \binom{m}{2} \cdot 2 = m(m-1)$.

Also, $\sum_{s, v} n_v(s) = 10m$ (each $f_i$ maps 10 elements to 10 elements). And $\sum_{s, v} \binom{n_v(s)}{2} = \sum_{s,v} \frac{n_v(s)(n_v(s)-1)}{2}$.

By convexity, for fixed $\sum n_v(s) = m$ at each $s$, the sum $\sum_v \binom{n_v(s)}{2}$ is minimized when all $n_v(s)$ are equal, i.e., $n_v(s) = m/10$ for all $v$. But we want a lower bound on the total agreements to get an upper bound on $m$.

Actually, we have $\sum_{s,v} \binom{n_v(s)}{2} \leq m(m-1)$, and we want to find the maximum $m$.

Hmm, but we also have the constraint that each $f_i$ is a permutation of $S$, so for each $i$, $\{f_i(s) : s \in S\} = S$. This means $\sum_s n_v(s) = m$ for each $v$ (each value $v$ is taken $m$ times total across all $f_i$ and all $s$). Wait no: $\sum_s n_v(s) = |\{(i, s) : f_i(s) = v\}| = \sum_i |\{s : f_i(s) = v\}| = \sum_i 1 = m$ (since each $f_i$ is a bijection, each $v$ is hit exactly once by each $f_i$). So $\sum_s n_v(s) = m$ for each $v$.

So we have a $10 \times 10$ matrix $(n_v(s))$ where:
- Row sums (over $v$): $\sum_v n_v(s) = m$ for each $s$.
- Column sums (over $s$): $\sum_s n_v(s) = m$ for each $v$.
- $\sum_{s,v} \binom{n_v(s)}{2} \leq m(m-1)$.

We want to maximize $m$.

$\sum_{s,v} \binom{n_v(s)}{2} = \frac{1}{2}\sum_{s,v} n_v(s)^2 - \frac{1}{2}\sum_{s,v} n_v(s) = \frac{1}{2}\sum_{s,v} n_v(s)^2 - 5m$.

So $\frac{1}{2}\sum n_v(s)^2 - 5m \leq m(m-1) = m^2 - m$.

$\sum n_v(s)^2 \leq 2m^2 - 2m + 10m = 2m^2 + 8m$.

By Cauchy-Schwarz or convexity, $\sum n_v(s)^2 \geq \frac{(\sum n_v(s))^2}{100} = \frac{(10m)^2}{100} = m^2$.

So $m^2 \leq 2m^2 + 8m$, which gives $0 \leq m^2 + 8m$, always true. Not helpful.

Let me try a different approach. The constraint is that $\sum n_v(s)^2 \leq 2m^2 + 8m$. With row and column sums all equal to $m$, the minimum of $\sum n_v(s)^2$ is achieved when all entries are $m/10$, giving $100 \cdot (m/10)^2 = m^2$. So we need $m^2 \leq 2m^2 + 8m$, i.e., $m \geq -8$, always true.

This approach doesn't give a useful bound. Let me think differently.

Let me think about the problem more concretely. 

Key insight: A quadratic polynomial $f$ that permutes $S$ is a permutation of $S$ whose cycle structure is constrained. Moreover, $f$ is uniquely determined by its action on any 3 elements of $S$.

Let me think about the maximum number of quadratic polynomial permutations of a 10-element set.

Consider the group $G$ of all permutations of $S$ that can be realized as polynomial maps (of any degree) preserving $S$. The quadratic polynomial permutations are a subset.

Actually, let me think about specific examples.

Example: $S = \{0, 1, 2, 3, 4, 5, 6\} \cup \{i, -i, 2i\}$ (7 real, 3 non-real). Can we find quadratic polynomials permuting this?

This seems hard to reason about abstractly. Let me think about the problem from the competition math perspective.

Let me reconsider. The problem says "maximum possible number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$". So we're maximizing over all valid $S$.

Let me think about what structures allow many quadratic symmetries.

If $S$ is invariant under a quadratic $f$, then $f$ generates a cyclic group of permutations of $S$ (via iteration). The order of $f$ as a permutation of $S$ divides... well, $f$ has some order $d$ as a permutation, and $f^d = \text{id}$ on $S$. But $f^d$ is a polynomial of degree $2^d$, and $f^d(z) - z$ has at most $2^d$ roots. Since $f^d$ is the identity on all 10 elements, $f^d(z) - z$ has at least 10 roots, so $2^d \geq 10$, meaning $d \geq 4$.

So any quadratic polynomial permuting $S$ has order at least 4 as a permutation of $S$.

Wait, that's an important constraint. The order $d$ of $f$ (as a permutation of $S$) must satisfy $2^d \geq 10$, so $d \geq 4$.

The cycle structure of $f$ on $S$ must have all cycle lengths dividing $d$, and $\text{lcm}$ of cycle lengths $= d \geq 4$.

Also, from the earlier constraints:
- At most 2 fixed points (cycles of length 1)
- At most 4 elements in cycles of length 1 or 2
- At most 8 elements in cycles of length 1 or 3

And $d \geq 4$.

Let me enumerate possible cycle structures for a permutation of 10 elements with these constraints:

Let me denote the cycle type as a partition of 10.

Constraint: $c_1 \leq 2$, $c_1 + 2c_2 \leq 4$, $c_1 + 3c_3 \leq 8$.

And the order $d = \text{lcm}(\text{cycle lengths}) \geq 4$.

Let me list partitions of 10 satisfying these:

- $c_1 = 0$: No fixed points. $2c_2 \leq 4 \Rightarrow c_2 \leq 2$. $3c_3 \leq 8 \Rightarrow c_3 \leq 2$.
  Remaining elements: $10 - 2c_2 - 3c_3$, must be in cycles of length $\geq 4$.
  
  - $c_2 = 0, c_3 = 0$: 10 elements in cycles of length $\geq 4$. Partitions: (10), (6,4), (5,5), (4,4,2)... wait $c_2=0$. (10), (6,4), (5,5), (4,4,...) but 4+4=8, need 2 more, but $c_2=0$ and $c_1=0$, so need a cycle of length 2, contradiction. So (10), (6,4), (5,5). Also (4,6) same as (6,4). What about (7,3)? No, $c_3=0$. (8,2)? No, $c_2=0$. (9,1)? No, $c_1=0$.
  
  Actually wait, I need to be more careful. Let me just enumerate all partitions of 10 and check constraints.
  
  Partitions of 10:
  - (10): $c_1=0, c_2=0, c_3=0$. ✓ Order = 10 ≥ 4. ✓
  - (9,1): $c_1=1 \leq 2$. ✓ $c_1+2c_2=1 \leq 4$. ✓ $c_1+3c_3=1 \leq 8$. ✓ Order = 9 ≥ 4. ✓
  - (8,2): $c_1=0, c_2=1$. $c_1+2c_2=2 \leq 4$. ✓ Order = 8 ≥ 4. ✓
  - (8,1,1): $c_1=2$. $c_1+2c_2=2 \leq 4$. ✓ Order = 8 ≥ 4. ✓
  - (7,3): $c_3=1$. $c_1+3c_3=3 \leq 8$. ✓ Order = 21 ≥ 4. ✓
  - (7,2,1): $c_1=1, c_2=1$. $c_1+2c_2=3 \leq 4$. ✓ Order = 14 ≥ 4. ✓
  - (7,1,1,1): $c_1=3 > 2$. ✗
  - (6,4): Order = 12 ≥ 4. ✓ $c_1=0, c_2=0, c_3=0$. ✓
  - (6,3,1): $c_1=1, c_3=1$. $c_1+3c_3=4 \leq 8$. ✓ Order = 6 ≥ 4. ✓
  - (6,2,2): $c_2=2$. $c_1+2c_2=4 \leq 4$. ✓ Order = 6 ≥ 4. ✓
  - (6,2,1,1): $c_1=2, c_2=1$. $c_1+2c_2=4 \leq 4$. ✓ Order = 6 ≥ 4. ✓
  - (6,1,1,1,1): $c_1=4 > 2$. ✗
  - (5,5): Order = 5 ≥ 4. ✓
  - (5,4,1): $c_1=1$. Order = 20 ≥ 4. ✓
  - (5,3,2): $c_2=1, c_3=1$. $c_1+2c_2=2 \leq 4$. $c_1+3c_3=3 \leq 8$. ✓ Order = 30 ≥ 4. ✓
  - (5,3,1,1): $c_1=2, c_3=1$. $c_1+3c_3=5 \leq 8$. ✓ Order = 15 ≥ 4. ✓
  - (5,2,2,1): $c_1=1, c_2=2$. $c_1+2c_2=5 > 4$. ✗
  - (5,2,1,1,1): $c_1=3 > 2$. ✗
  - (5,1,1,1,1,1): ✗
  - (4,4,2): $c_2=1$. $c_1+2c_2=2 \leq 4$. ✓ Order = 4 ≥ 4. ✓
  - (4,4,1,1): $c_1=2$. $c_1+2c_2=2 \leq 4$. ✓ Order = 4 ≥ 4. ✓
  - (4,3,3): $c_3=2$. $c_1+3c_3=6 \leq 8$. ✓ Order = 12 ≥ 4. ✓
  - (4,3,2,1): $c_1=1, c_2=1, c_3=1$. $c_1+2c_2=3 \leq 4$. $c_1+3c_3=4 \leq 8$. ✓ Order = 12 ≥ 4. ✓
  - (4,3,1,1,1): $c_1=3 > 2$. ✗
  - (4,2,2,2): $c_2=3$. $c_1+2c_2=6 > 4$. ✗
  - (4,2,2,1,1): $c_1=2, c_2=2$. $c_1+2c_2=6 > 4$. ✗
  - (4,2,1,1,1,1): ✗
  - (4,1,...): ✗ (too many fixed points)
  - (3,3,3,1): $c_1=1, c_3=3$. $c_1+3c_3=10 > 8$. ✗
  - (3,3,2,2): $c_2=2, c_3=2$. $c_1+2c_2=4 \leq 4$. $c_1+3c_3=6 \leq 8$. ✓ Order = 6 ≥ 4. ✓
  - (3,3,2,1,1): $c_1=2, c_2=1, c_3=2$. $c_1+2c_2=4 \leq 4$. $c_1+3c_3=8 \leq 8$. ✓ Order = 6 ≥ 4. ✓
  - (3,3,1,1,1,1): ✗
  - (3,2,2,2,1): $c_1=1, c_2=3$. $c_1+2c_2=7 > 4$. ✗
  - (3,2,2,1,1,1): ✗
  - (3,2,1,...): ✗
  - (3,1,...): ✗
  - (2,2,2,2,2): $c_2=5$. $c_1+2c_2=10 > 4$. ✗
  - (2,2,2,2,1,1): $c_1=2, c_2=4$. $c_1+2c_2=10 > 4$. ✗
  - etc. All with many 2-cycles: ✗
  - (2,2,2,1,1,1,1): ✗
  - (2,2,1,...): ✗
  - (2,1,...): ✗
  - (1,...): ✗

So the valid cycle types are:
(10), (9,1), (8,2), (8,1,1), (7,3), (7,2,1), (6,4), (6,3,1), (6,2,2), (6,2,1,1), (5,5), (5,4,1), (5,3,2), (5,3,1,1), (4,4,2), (4,4,1,1), (4,3,3), (4,3,2,1), (3,3,2,2), (3,3,2,1,1).

That's 20 valid cycle types. But not all of these can necessarily be realized by a quadratic polynomial, and even if they can, we need to count how many distinct quadratic polynomials can simultaneously permute the same set $S$.

This is getting very complicated. Let me think about the problem differently.

Let me think about the structure of the set of quadratic polynomials permuting $S$.

If $f$ and $g$ are quadratic polynomials permuting $S$, consider $h = g \circ f^{-1}$. This is a polynomial map (since $f$ is a bijection on $S$, $f^{-1}$ exists as a function on $S$, but not necessarily as a polynomial). So $h$ is a permutation of $S$ but not necessarily a polynomial.

Alternatively, consider $g \circ f$, which is a degree-4 polynomial permuting $S$.

Let me think about a different approach. 

Key idea: If $f$ is a quadratic polynomial permuting $S$, then $f$ is a permutation of $S$ with order $d \geq 4$. The powers $f, f^2, f^3, \ldots, f^{d-1}$ are all permutations of $S$, but only $f$ is quadratic (the others have higher degree). So each quadratic polynomial gives one permutation.

Now, how many quadratic polynomials can permute the same $S$?

Let me think about small cases first. Suppose $|S| = n$ and we want to maximize the number of quadratic polynomial permutations.

For the problem at hand, $n = 10$ with 7 real and 3 non-real.

Let me think about the problem from the answer's perspective. This is likely a competition problem with a clean answer. Let me think about what structures could give many quadratic symmetries.

Consider the Chebyshev map $T_2(z) = z^2 - 2$. We have $T_2(2\cos\theta) = 2\cos(2\theta)$. If $S_0 = \{2\cos(2\pi k / n) : k = 0, 1, \ldots, n-1\}$, then $T_2$ acts on $S_0$ as the doubling map $k \mapsto 2k \pmod{n}$.

But these are all real. We need 3 non-real elements.

What if we consider a different quadratic map that has both real and non-real periodic points?

Actually, let me think about this differently. Let me consider the general theory.

A quadratic polynomial $f(z) = az^2 + bz + c$ can be conjugated to the form $z^2 + c_0$ by an affine change of variables. So WLOG, we can consider $f(z) = z^2 + c_0$ (by conjugating $S$ appropriately). But different quadratics would require different conjugations, so this only helps for a single quadratic.

Let me think about the problem more carefully.

Suppose we have $m$ quadratic polynomials $f_1, \ldots, f_m$ permuting $S$. Each $f_i$ is a permutation of $S$ with order $\geq 4$. 

Now, the key constraint is the real/non-real split. Let me think about how the real and non-real elements interact.

If $f$ has real coefficients, it preserves the real/non-real split (maps reals to reals, non-reals to non-reals). If $f$ has non-real coefficients, it might mix them.

Let me count separately:
- $m_{\text{real}}$: number of quadratic polynomials with real coefficients permuting $S$.
- $m_{\text{complex}}$: number of quadratic polynomials with non-real coefficients permuting $S$.

$m = m_{\text{real}} + m_{\text{complex}}$.

For $m_{\text{real}}$: $f$ permutes the 7 real elements and the 3 non-real elements separately. The constraint on the 7 real elements: $f$ is a real quadratic permuting 7 real numbers. The constraint on the 3 non-real elements: $f$ permutes 3 non-real numbers (and $f$ has real coefficients, so it respects conjugation if applicable).

For a real quadratic permuting 7 real numbers: the cycle structure on 7 elements must satisfy fixed points $\leq 2$, elements in cycles of length $\leq 2$ is $\leq 4$, order $\geq 4$ (since $2^d \geq 7$ requires $d \geq 3$, but actually $2^3 = 8 \geq 7$, so $d \geq 3$).

Wait, I need to recompute. For 7 elements, $f^d = \text{id}$ on all 7, so $f^d(z) - z$ has at least 7 roots, degree $2^d$, so $2^d \geq 7$, meaning $d \geq 3$.

For 3 non-real elements, $2^d \geq 3$, so $d \geq 2$.

But the order of $f$ as a permutation of all 10 elements is the lcm of the orders on the real and non-real parts. So the overall order $d = \text{lcm}(d_{\text{real}}, d_{\text{non-real}}) \geq 4$ (from the 10-element constraint).

Hmm wait, actually the constraint $2^d \geq 10$ comes from $f^d(z) - z$ having 10 roots. But if $f$ has real coefficients, $f^d$ also has real coefficients, and $f^d(z) - z$ has 10 roots (7 real + 3 non-real). The degree is $2^d$, so $2^d \geq 10$, $d \geq 4$. This is the overall constraint.

But there are also separate constraints: $f^d(z) - z$ restricted to real roots: the 7 real roots are among the roots of $f^d(z) - z$, which has degree $2^d$. So $2^d \geq 7$ is weaker than $2^d \geq 10$.

OK so the overall constraint is $d \geq 4$ regardless.

Let me try to think about this problem from a higher level. 

I think the key insight is that the number of quadratic polynomials permuting $S$ is quite limited, and we need to find the optimal $S$.

Let me consider the following approach: think about the "group" generated by the quadratic polynomial permutations. If $f$ and $g$ are quadratic polynomials permuting $S$, then $f \circ g$ is a degree-4 polynomial permuting $S$, and $g \circ f$ is also degree-4. These might or might not be equal.

If $f \circ g = g \circ f$ (they commute), then the group they generate is abelian. The set of all polynomial permutations of $S$ (of any degree) forms a group, and the quadratic ones are specific elements.

Actually, let me think about a specific construction. 

Consider the set $S = \{\zeta^k : k = 0, 1, \ldots, 9\}$ where $\zeta = e^{2\pi i/10}$, the 10th roots of unity. The map $z \mapsto z^2$ permutes these (it's the doubling map mod 10). But these are not 7 real and 3 non-real; the 10th roots of unity include only 2 real ones ($1$ and $-1$).

What if we use a different set? Let me think...

Consider $S$ consisting of 7 real numbers forming a Chebyshev-type set, plus 3 non-real numbers.

Actually, let me think about the problem differently. Let me consider what happens with the map $z \mapsto z^2 - 2$ on specific sets.

$T(z) = z^2 - 2$. $T(2\cos\theta) = 2\cos(2\theta)$. 

If we take $S_{\text{real}} = \{2\cos(2\pi k/7) : k = 0, 1, \ldots, 6\}$, these are 7 real numbers (well, $2\cos(2\pi \cdot 0/7) = 2$, $2\cos(2\pi/7)$, etc., all distinct). $T$ acts on these as $k \mapsto 2k \pmod 7$. The order of 2 mod 7 is 3 (since $2^1=2, 2^2=4, 2^3=1 \pmod 7$). So $T$ has order 3 on this set. But we need order $\geq 4$ for 10 elements. If we only have 7 elements, order $\geq 3$ suffices ($2^3 = 8 \geq 7$).

But we have 10 elements total. If $T$ has order 3 on the 7 real elements and some order on the 3 non-real elements, the overall order is lcm of the two. For the overall order to be $\geq 4$, we need the non-real part to have order $\geq 4$ (or the lcm to be $\geq 4$).

Hmm, but with 3 non-real elements, the maximum order of a permutation is 3 (a 3-cycle). So the order on non-real elements is at most 3. Then the overall order is lcm(order_real, order_nonreal) = lcm(3, ≤3) ≤ 3 < 4. This violates the constraint!

Wait, this means that if $f$ has real coefficients and permutes 7 real + 3 non-real elements, with order 3 on the real part and order ≤ 3 on the non-real part, the overall order is ≤ 3, but we need order ≥ 4. Contradiction!

So for a real-coefficient quadratic, the order on the 7 real elements must be such that lcm(order_real, order_nonreal) ≥ 4. Since order_nonreal ≤ 3 (only 3 elements), we need order_real ≥ 4.

For 7 real elements with a real quadratic, order ≥ 4 means $2^d \geq 7$ gives $d \geq 3$, but we need $d \geq 4$ from the overall constraint. Actually wait, the constraint is on the overall order. Let me re-examine.

The constraint $2^d \geq 10$ where $d$ is the order of $f$ on all of $S$. If $f$ has order $d_{\text{real}}$ on the 7 real elements and $d_{\text{nonreal}}$ on the 3 non-real elements, then $d = \text{lcm}(d_{\text{real}}, d_{\text{nonreal}})$, and we need $2^d \geq 10$, i.e., $d \geq 4$.

So $\text{lcm}(d_{\text{real}}, d_{\text{nonreal}}) \geq 4$.

Since $d_{\text{nonreal}} \leq 3$ (permutation of 3 elements), we need $d_{\text{real}} \geq 4$.

For 7 real elements, $d_{\text{real}} \geq 4$ and $2^{d_{\text{real}}} \geq 7$ (automatically satisfied for $d_{\text{real}} \geq 4$ since $2^4 = 16 \geq 7$).

Also, the cycle structure on 7 elements with order $\geq 4$: fixed points $\leq 2$, elements in cycles of length $\leq 2$ is $\leq 4$ (from $2^2 = 4$).

Partitions of 7 with order $\geq 4$ and the constraints:
- (7): order 7 ≥ 4. ✓
- (6,1): order 6 ≥ 4. $c_1=1 \leq 2$. ✓
- (5,2): order 10 ≥ 4. $c_2=1$, $c_1+2c_2=2 \leq 4$. ✓
- (5,1,1): order 5 ≥ 4. $c_1=2 \leq 2$. ✓
- (4,3): order 12 ≥ 4. ✓
- (4,2,1): order 4 ≥ 4. $c_1=1, c_2=1$, $c_1+2c_2=3 \leq 4$. ✓
- (4,1,1,1): $c_1=3 > 2$. ✗
- (3,3,1): order 3 < 4. ✗
- (3,2,2): order 6 ≥ 4. $c_2=2$, $c_1+2c_2=4 \leq 4$. ✓
- (3,2,1,1): order 6 ≥ 4. $c_1=2, c_2=1$, $c_1+2c_2=4 \leq 4$. ✓
- (3,1,1,1,1): ✗
- (2,2,2,1): order 2 < 4. ✗
- (2,2,1,1,1): ✗
- etc.

Valid cycle types for 7 real elements: (7), (6,1), (5,2), (5,1,1), (4,3), (4,2,1), (3,2,2), (3,2,1,1).

And for 3 non-real elements with real coefficients: the permutation must respect conjugation. If the 3 non-real elements are $z_1, z_2, z_3$, and some of their conjugates are also in $S$... 

Actually, the 3 non-real elements don't have to be closed under conjugation. But if $f$ has real coefficients, $f(\bar{z}) = \overline{f(z)}$. So if $z \in S$ is non-real and $\bar{z} \in S$, then $f$ maps the pair $\{z, \bar{z}\}$ to $\{f(z), \overline{f(z)}\}$. If $\bar{z} \notin S$, then $f(z)$ is some non-real element of $S$, and $\overline{f(z)} = f(\bar{z})$ which may or may not be in $S$.

The 3 non-real elements: either they form a conjugation-closed set (e.g., $\{z, \bar{z}, w\}$ where $w$ is non-real and $\bar{w} \notin S$, or $\{z, \bar{z}, w, \bar{w}\}$ but that's 4), or they don't.

With 3 non-real elements, the possibilities for conjugation structure:
1. All 3 are self-conjugate: impossible (self-conjugate = real).
2. One conjugate pair $\{z, \bar{z}\}$ and one element $w$ with $\bar{w} \notin S$.
3. No conjugate pairs: all 3 have conjugates outside $S$.

Wait, actually with 3 non-real elements, we can have:
- 1 conjugate pair + 1 unpaired: $\{z, \bar{z}, w\}$ where $\bar{w} \neq z, \bar{z}$ and $\bar{w} \notin S$.
- 0 conjugate pairs: $\{z_1, z_2, z_3\}$ where no $\bar{z}_i$ is in $S$.
- We can't have 1.5 conjugate pairs (3 is odd).

Case 2 (1 conjugate pair): $f$ with real coefficients must map $\{z, \bar{z}\}$ to a conjugate pair in $S$. The only conjugate pair in the non-real part is $\{z, \bar{z}\}$ itself. So $f$ maps $\{z, \bar{z}\}$ to $\{z, \bar{z}\}$ (either $f(z) = z, f(\bar{z}) = \bar{z}$ or $f(z) = \bar{z}, f(\bar{z}) = z$). And $f(w) = w$ (since $w$ is the only remaining non-real element, and $f$ maps non-reals to non-reals). So $w$ is a fixed point.

If $f(z) = z, f(\bar{z}) = \bar{z}$: both $z, \bar{z}$ are fixed. So on non-real elements, $f$ is the identity.
If $f(z) = \bar{z}, f(\bar{z}) = z$: $z, \bar{z}$ form a 2-cycle, $w$ is fixed.

Case 3 (0 conjugate pairs): $f$ maps non-real elements to non-real elements, and conjugation doesn't constrain the permutation (since no conjugate of a non-real element is in $S$). So $f$ can be any permutation of the 3 non-real elements, as long as it's consistent with being a real quadratic.

Wait, but $f$ has real coefficients, so $f(\bar{z_i}) = \overline{f(z_i)}$. Since $\bar{z_i} \notin S$, this doesn't directly constrain the permutation on $S$. But it does mean that $f$ maps $\bar{z_i}$ to $\overline{f(z_i)}$, which is the conjugate of some element of $S$ (since $f(z_i) \in S$). So $\overline{f(z_i)}$ is the conjugate of a non-real element of $S$, which is also non-real and not in $S$ (by assumption). So this is consistent.

OK so in Case 3, the permutation on the 3 non-real elements can be anything (subject to the quadratic constraint).

This is getting very involved. Let me try to think about the problem from a higher level and maybe look for patterns.

Let me consider the possibility that the answer is related to a specific number. Competition problems like this often have answers that are small integers.

Let me think about upper bounds more carefully.

Upper bound via interpolation: A quadratic polynomial is determined by 3 points. If $f$ permutes $S$, then $f$ is determined by $(f(s_1), f(s_2), f(s_3))$ for any 3 distinct $s_1, s_2, s_3 \in S$. The number of possible triples is $10 \cdot 9 \cdot 8 = 720$ (ordered), but many of these won't extend to a valid permutation. The actual number of quadratic polynomial permutations is at most the number of permutations of $S$ consistent with a quadratic, which is at most... well, it's hard to bound this way.

Let me try another approach. Let me think about the problem in terms of the functional equation.

If $f$ is a quadratic polynomial permuting $S$, and $g$ is another quadratic polynomial permuting $S$, then $f$ and $g$ are both permutations of $S$. The composition $g \circ f^{-1}$ is a permutation of $S$ (but $f^{-1}$ is not a polynomial in general).

However, $g \circ f$ is a degree-4 polynomial permuting $S$. And $f \circ g$ is also a degree-4 polynomial permuting $S$. If $f$ and $g$ commute ($f \circ g = g \circ f$), then they generate a cyclic group (if one is a power of the other) or a more complex abelian group.

For quadratic polynomials, commutativity is quite restrictive. Two quadratic polynomials $f(z) = az^2 + bz + c$ and $g(z) = dz^2 + ez + f$ commute (as polynomials, i.e., $f(g(z)) = g(f(z))$ for all $z$) only in very special cases. By a classical result, two polynomials commute iff they share a common iterate, or they are both iterates of a common polynomial, or they are both Chebyshev-like or both monomial-like.

But we don't need $f$ and $g$ to commute as polynomials; we just need them to both permute $S$.

Let me try to think about specific examples.

Example: Let $S = \{0, 1, -1, 2, -2, 3, -3\} \cup \{i, -i, 2i\}$. Can we find quadratic polynomials permuting this?

$f(z) = -z$ is linear, not quadratic. $f(z) = z^2$ maps $0 \to 0, 1 \to 1, -1 \to 1$ (not injective). So $z^2$ doesn't work.

Let me think about Chebyshev maps more carefully.

$T(z) = z^2 - 2$. $T(2) = 2, T(0) = -2, T(-2) = 2$. So $T$ maps $2 \to 2, 0 \to -2, -2 \to 2$. Not injective on $\{0, 2, -2\}$ (both $0$ and $-2$ map to $-2$... wait, $T(0) = -2$ and $T(-2) = 2$. So $0 \to -2 \to 2 \to 2$. So $2$ is a fixed point and $0 \to -2 \to 2$. Not a permutation of $\{0, 2, -2\}$.

Let me use the Chebyshev representation. $T(2\cos\theta) = 2\cos(2\theta)$. For $S = \{2\cos(2\pi k/n) : k = 0, \ldots, n-1\}$, $T$ acts as $k \mapsto 2k \pmod n$.

For $n = 7$: $S = \{2\cos(2\pi k/7) : k = 0, 1, \ldots, 6\} = \{2, 2\cos(2\pi/7), 2\cos(4\pi/7), 2\cos(6\pi/7), 2\cos(8\pi/7), 2\cos(10\pi/7), 2\cos(12\pi/7)\}$. 

Note that $2\cos(2\pi k/7) = 2\cos(2\pi(7-k)/7)$, so actually $S$ has only $\lceil 7/2 \rceil + 1 = 4$ distinct values: $\{2, 2\cos(2\pi/7), 2\cos(4\pi/7), 2\cos(6\pi/7)\}$. That's only 4 distinct real numbers, not 7.

Hmm, so the Chebyshev approach with $n=7$ gives only 4 distinct values. I need 7 distinct real numbers.

For $n$ points to give $n$ distinct values of $2\cos(2\pi k/n)$, we need $k$ and $n-k$ to give different values, which happens only when $k = 0$ or $k = n/2$ (if $n$ is even). So for odd $n$, we get $(n+1)/2$ distinct values, and for even $n$, we get $n/2 + 1$ distinct values.

To get 7 distinct real values, we need $n$ such that $(n+1)/2 \geq 7$ (odd $n$), so $n \geq 13$, or $n/2 + 1 \geq 7$ (even $n$), so $n \geq 12$.

With $n = 13$: $S = \{2\cos(2\pi k/13) : k = 0, 1, \ldots, 12\}$, which has 7 distinct values. $T$ acts as $k \mapsto 2k \pmod{13}$. The order of 2 mod 13 is 12 (since 2 is a primitive root mod 13). So $T$ has order 12 on this set. But wait, the 7 distinct values correspond to orbits under $k \mapsto -k \pmod{13}$ (since $\cos(2\pi k/13) = \cos(2\pi(13-k)/13)$). The map $T$ on the 7 distinct values corresponds to $k \mapsto 2k \pmod{13}$ followed by identifying $k$ with $-k$. So the action on the 7 values is $[k] \mapsto [2k]$ where $[k] = \{k, -k\} \pmod{13}$.

The order of this action: we need $[2^d k] = [k]$, i.e., $2^d k \equiv \pm k \pmod{13}$, i.e., $2^d \equiv \pm 1 \pmod{13}$. $2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 16 \equiv 3, 2^5 = 6, 2^6 = 12 \equiv -1 \pmod{13}$. So $2^6 \equiv -1$, meaning the order of the action on the 7 values is 6. (Since $[2^6 k] = [-k] = [k]$.)

So $T$ has order 6 on the 7 real values. That's $\geq 4$, good.

Now, what about the non-real part? We need 3 non-real elements that are also permuted by $T(z) = z^2 - 2$. 

$T$ has fixed points at $z = 2$ and $z = -1$ (solutions of $z^2 - 2 = z$). The 7 real values include $2$ (which is a fixed point) and $-1$ (which is $2\cos(2\pi \cdot 3/13)$... let me check: $2\cos(6\pi/13) \approx 2 \times 0.568 \approx 1.137$, not $-1$. Hmm.)

Actually, $-1$ is a fixed point of $T$, but is $-1$ in our set $S$? $S = \{2\cos(2\pi k/13) : k = 0, \ldots, 6\}$ (taking one representative from each pair). $2\cos(2\pi/13) \approx 1.77$, $2\cos(4\pi/13) \approx 1.14$, $2\cos(6\pi/13) \approx 0.23$, $2\cos(8\pi/13) \approx -0.71$, $2\cos(10\pi/13) \approx -1.37$, $2\cos(12\pi/13) \approx -1.95$. And $2\cos(0) = 2$. So $-1$ is not in $S$.

OK so the fixed points of $T$ (namely $2$ and $-1$) — only $2$ is in $S$. So $T$ has 1 fixed point in $S$ (the value $2$), and the other 6 real values form cycles under $T$.

The cycle structure of $T$ on the 7 real values: $[0] \mapsto [0]$ (fixed, since $2 \cdot 0 = 0$), and then $[1] \mapsto [2] \mapsto [4] \mapsto [8] = [8] = [-5] = [5] \mapsto [10] = [10] = [-3] = [3] \mapsto [6] \mapsto [12] = [-1] = [1]$. So the cycle is $[1] \to [2] \to [4] \to [5] \to [3] \to [6] \to [1]$, a 6-cycle. So the cycle structure is $(6, 1)$: one 6-cycle and one fixed point.

Now for the non-real part: we need 3 non-real numbers that are permuted by $T(z) = z^2 - 2$. These would be periodic points of $T$ that are non-real.

The periodic points of $T$ of period dividing $d$ are the roots of $T^d(z) = z$, which has degree $2^d$. For $d = 6$ (the order of $T$ on the real part), $T^6(z) - z$ has degree $64$ and 64 roots. The 7 real values are among these roots. The remaining 57 roots are non-real (or real but not in $S$).

We need to find 3 non-real roots of $T^6(z) - z$ that form a single orbit under $T$ (or multiple orbits whose cycle lengths have lcm dividing 6, and the overall order of $T$ on all 10 elements is lcm(6, order on non-real) which should be $\geq 4$, automatically satisfied).

The non-real periodic points of $T$ of period dividing 6: we need to find orbits of $T$ among the non-real roots of $T^6(z) - z$. The cycle lengths must divide 6, so possible lengths are 1, 2, 3, 6. But fixed points of $T$ are $2$ and $-1$ (both real), so no non-real fixed points. 2-cycles: $T(z) = w, T(w) = z$, i.e., $T^2(z) = z$ but $T(z) \neq z$. $T^2(z) - z = (z^2-2)^2 - 2 - z = z^4 - 4z^2 + 2 - z$. This has degree 4, and the roots include the 2 fixed points (2 and -1), so there are 2 more roots, which are the 2-cycle. Let me find them: $z^4 - 4z^2 - z + 2 = (z-2)(z+1)(z^2+z-1)$. The roots of $z^2 + z - 1 = 0$ are $z = (-1 \pm \sqrt{5})/2$, which are real. So the 2-cycle is real. No non-real 2-cycles.

3-cycles: $T^3(z) = z$ but $T(z) \neq z$ and $T^2(z) \neq z$. $T^3(z) - z$ has degree 8. The roots include fixed points (2 roots) and 2-cycle (2 roots), so 4 roots form 3-cycles, giving one 3-cycle (with 3 elements) and... wait, 4 roots can't form a 3-cycle (which needs 3 elements). Let me recompute.

$T^3(z) - z$ has degree 8. Roots: 2 fixed points + 2 elements in 2-cycle + remaining 4 elements. The remaining 4 elements: if they form 3-cycles, we'd need 3 or 6 elements, but we have 4. So they must form something else. Actually, the 4 remaining elements could form a 4-cycle (but 4 doesn't divide 3, contradiction since they're roots of $T^3(z) = z$). Wait, the period must divide 3, so periods are 1 or 3. We have 2 fixed points (period 1) and 2 period-2 elements. But period-2 elements are NOT roots of $T^3(z) = z$ unless their period also divides 3, which it doesn't (2 doesn't divide 3). 

Hmm, I think I'm confusing myself. $T^3(z) = z$ means the period divides 3, so periods 1 or 3. The fixed points (period 1) are roots. The 2-cycle elements have period 2, which doesn't divide 3, so they're NOT roots of $T^3(z) = z$. So $T^3(z) - z$ has 8 roots: 2 fixed points + 6 elements in 3-cycles (two 3-cycles). 

So there are two 3-cycles of $T$, with 6 elements total. Are any of these non-real? The 3-cycles are roots of $(T^3(z) - z) / (T(z) - z)$, which is a degree-6 polynomial. Let me think about whether these are real or complex.

Actually, $T^3(z) - z$ factors as $(z^2 - z - 2) \cdot Q_6(z)$ where $Q_6$ is degree 6 and contains the 3-cycle elements. The fixed points are roots of $z^2 - z - 2 = (z-2)(z+1)$.

For the Chebyshev map $T(z) = z^2 - 2$, the periodic points are $2\cos(2\pi k / (2^d - 1))$ and $2\cos(2\pi k / (2^d + 1))$ for various $d$. These are all real! So all periodic points of $T(z) = z^2 - 2$ are real.

This makes sense because $T$ maps $[-2, 2]$ to $[-2, 2]$ (via the Chebyshev correspondence), and the Julia set of $T$ is the interval $[-2, 2]$. All periodic points are in $[-2, 2]$ and hence real.

So $T(z) = z^2 - 2$ has no non-real periodic points. This means we can't use $T$ to permute a set with non-real elements.

I need a different quadratic map that has non-real periodic points.

Let me consider $f(z) = z^2 + c$ for various $c$. For $c > -2$ (approximately), the Julia set is a fractal and there are non-real periodic points. For $c = -2$, it's the Chebyshev case with all real periodic points. For $c = 0$, $f(z) = z^2$, and the periodic points are roots of unity (on the unit circle, mostly non-real).

$f(z) = z^2$: periodic points of period dividing $d$ are roots of $z^{2^d} = z$, i.e., $z^{2^d - 1} = 1$ or $z = 0$. So the periodic points are $0$ (fixed) and the $(2^d - 1)$th roots of unity.

For $f(z) = z^2$ to permute a set $S$, $S$ must consist of periodic points of $f$. The real periodic points are $0, 1, -1$ (for various periods: $0$ is fixed, $1$ is fixed, $-1$ has period 2). Actually, $-1 \to 1 \to 1$, so $-1$ is not periodic (it's preperiodic). The real periodic points of $z^2$ are just $0$ and $1$ (both fixed). That's only 2 real periodic points, not enough for 7.

So $z^2$ doesn't work either.

Let me think about this differently. We need a quadratic polynomial with at least 7 real periodic points and at least 3 non-real periodic points, all of which are in a single set $S$ that's permuted by $f$.

For $T(z) = z^2 - 2$, all periodic points are real (in $[-2, 2]$). For $f(z) = z^2 + c$ with $c > 1/4$, there are no real periodic points (the real dynamics escape). For $-2 \leq c \leq 1/4$, there are real periodic points.

For $c$ slightly greater than $-2$, the map $z^2 + c$ has a Julia set that's a perturbation of $[-2, 2]$, and there are non-real periodic points near the real axis.

But the key question is: can we find a quadratic with both many real and some non-real periodic points, forming a set invariant under the quadratic?

Actually, I realize we don't need all elements of $S$ to be periodic points of a single quadratic. We need to find $S$ such that multiple quadratics permute $S$. Each quadratic might have different periodic structures.

Let me reconsider the problem. We want to maximize the number of quadratic polynomials $f$ with $f(S) = S$. We choose $S$ optimally.

Let me think about what kinds of sets $S$ can be invariant under multiple quadratic polynomials.

If $f$ and $g$ are both quadratic polynomials permuting $S$, then $f \circ g$ and $g \circ f$ are degree-4 polynomials permuting $S$. If $f \circ g = g \circ f$ (they commute as polynomials), then by Ritt's theorem, they must be related in a specific way (both iterates of a common polynomial, or both Chebyshev, or both monomial-type).

But they don't need to commute as polynomials; they just need to both permute $S$.

Let me think about the problem from the answer perspective. This is likely from a math competition (maybe Putnam or USAMO or similar). Let me think about what the answer might be.

Actually, let me reconsider. The problem says "maximum possible number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$". 

Let me think about affine maps first. An affine map $f(z) = az + b$ permuting $S$ is a symmetry of $S$. The number of affine symmetries can be large (e.g., if $S$ is a regular polygon, the dihedral group). But we're looking at quadratic polynomials, not affine.

A quadratic polynomial $f(z) = az^2 + bz + c$ with $a \neq 0$. This is a degree-2 map.

Let me think about the constraint more carefully. If $f$ permutes $S$ (10 elements), then $f$ is a bijection on $S$. The equation $f(z) = w$ has at most 2 solutions, so each $w \in S$ has at most 2 preimages in $\mathbb{C}$, and exactly 1 in $S$.

Now, consider two quadratic polynomials $f, g$ permuting $S$. The polynomial $f - g$ has degree at most 2, so $f(z) = g(z)$ has at most 2 solutions. So $f$ and $g$ agree on at most 2 elements of $S$.

This means: if we have $m$ quadratic polynomials permuting $S$, any two agree on at most 2 elements.

Now, consider the $m$ polynomials as permutations of $S$. Each permutation $\sigma_i$ is determined by any 3 of its values (since the quadratic is determined by 3 points). Two permutations agree on at most 2 positions.

This is related to the theory of permutation codes or mutually orthogonal structures.

Let me think about this combinatorially. We have $m$ permutations of $\{1, \ldots, 10\}$, any two agreeing in at most 2 positions. What's the maximum $m$?

This is a well-studied problem in combinatorics: permutations with limited agreement. The maximum number of permutations of $n$ elements with pairwise agreement at most $t$ is related to the concept of "permutation arrays" or "permutation codes."

For $n = 10$ and $t = 2$ (at most 2 agreements), the maximum number of permutations is... I don't remember the exact value, but it can be quite large. However, not all such permutations can be realized as quadratic polynomials.

The key additional constraint is that the permutation must be realizable as a quadratic polynomial on the specific set $S$. A quadratic polynomial is determined by 3 parameters, so the space of quadratic polynomials is 3-dimensional (over $\mathbb{C}$). The condition $f(S) = S$ is a strong constraint.

Let me think about it this way: a quadratic polynomial $f(z) = az^2 + bz + c$ is determined by $(a, b, c) \in \mathbb{C}^3$ with $a \neq 0$. The condition $f(S) \subseteq S$ means $f(s_i) \in S$ for each $i$, which gives 10 constraints (each $f(s_i)$ must be one of the 10 elements of $S$). But since $f$ is determined by 3 values, if we specify $f(s_1), f(s_2), f(s_3)$, then $f$ is determined, and we need $f(s_i) \in S$ for $i = 4, \ldots, 10$ as well.

So the number of quadratic polynomials permuting $S$ equals the number of triples $(f(s_1), f(s_2), f(s_3)) \in S^3$ (with $f(s_i)$ distinct, since $f$ is a bijection) such that the resulting quadratic maps all of $S$ into $S$.

The number of such triples is at most $10 \cdot 9 \cdot 8 = 720$, but the actual number is much smaller due to the constraints.

Let me try to think about this problem more carefully with a specific approach.

Approach: Consider the "permutation polynomial" aspect. A quadratic polynomial $f$ permuting $S$ is a permutation polynomial on $S$. The set of all permutation polynomials on $S$ (of any degree) forms a group under composition. The quadratic ones are specific elements.

For a set of $n$ points, the group of permutation polynomials can be at most the symmetric group $S_n$ (if every permutation is a polynomial), but this requires degree up to $n-1$. For quadratics, we're much more restricted.

Let me try to think about the problem by considering the real and complex parts separately and then combining.

Let me consider the following strategy: find $S$ with 7 real and 3 non-real elements such that many quadratics permute $S$.

Strategy 1: Use real quadratics only. A real quadratic permutes the 7 real elements and the 3 non-real elements separately. We need to find a set of 7 real numbers with many real quadratic symmetries, and a set of 3 non-real numbers with compatible real quadratic symmetries.

For 7 real numbers: how many real quadratics can permute a set of 7 real numbers? A real quadratic $f(x) = ax^2 + bx + c$ ($a \neq 0$, $a, b, c \in \mathbb{R}$) permuting a set of 7 real numbers. The cycle structure must have order $\geq 3$ (since $2^d \geq 7$ requires $d \geq 3$). 

Actually, for the overall problem with 10 elements, we need order $\geq 4$. So the real quadratic must have order $\geq 4$ on the 7 real elements (since the non-real part has at most 3 elements, order $\leq 3$, and lcm must be $\geq 4$).

How many real quadratics can permute 7 real numbers with order $\geq 4$?

A real quadratic is determined by 3 real parameters. The condition that it permutes 7 specific real numbers is very restrictive. Given 7 real numbers, how many real quadratics permute them?

If $f$ is a real quadratic permuting $\{x_1, \ldots, x_7\}$, then $f$ is determined by $(f(x_1), f(x_2), f(x_3))$, and we need $f(x_i) \in \{x_1, \ldots, x_7\}$ for all $i$, with $f$ being a bijection.

The number of real quadratics permuting 7 real numbers is at most the number of permutations of 7 elements that can be realized as a real quadratic, which is at most $7 \cdot 6 \cdot 5 = 210$ (choices of 3 images) but actually much less.

Let me think about specific examples.

For the Chebyshev map $T(x) = x^2 - 2$ on $S_7 = \{2\cos(2\pi k/13) : k = 0, \ldots, 6\}$ (7 distinct real values), $T$ permutes $S_7$ with cycle type $(6, 1)$. Are there other real quadratics permuting $S_7$?

The powers of $T$ that are quadratic: only $T$ itself ($T^2$ is degree 4, etc.). So $T$ gives one quadratic.

Are there other quadratics permuting $S_7$? Let me think... If $g$ is another real quadratic permuting $S_7$, then $g$ is a permutation of $S_7$ with order $\geq 3$ (for 7 elements). The cycle structure must be one of the valid types.

This is hard to determine without more specific computation. Let me think about the problem differently.

Let me consider the possibility that the answer is small, like 2, 3, 4, 5, or 6.

Actually, let me reconsider the problem. Maybe I should think about what sets $S$ can be invariant under multiple quadratics, and count more carefully.

Let me think about the group structure. If $f_1, \ldots, f_m$ are quadratic polynomials permuting $S$, consider the group $G$ generated by $f_1, \ldots, f_m$ under composition (as permutations of $S$). This is a subgroup of $S_{10}$. Each $f_i$ is an element of $G$ that happens to be a quadratic polynomial.

The group $G$ acts on $S$, and the quadratic polynomial elements of $G$ are what we're counting.

Now, $G$ is a transitive subgroup of $S_{10}$ (if $S$ is a single orbit) or might have multiple orbits. But since each $f_i$ permutes all of $S$, $G$ acts on $S$ but might not be transitive.

Actually, $G$ might not be transitive. For example, if all $f_i$ preserve the real/non-real split, then $G$ has two orbits: the 7 real and 3 non-real elements.

Let me consider the case where all quadratics have real coefficients. Then $G$ acts separately on the 7 real and 3 non-real elements. The quadratics are elements of $G$ that are quadratic polynomials.

For the 7 real elements, the quadratics induce permutations with specific cycle structures. For the 3 non-real elements, the quadratics induce permutations with specific cycle structures.

The number of quadratics is the number of elements of $G$ that are quadratic polynomials. This is at most $|G|$, but typically much less.

Hmm, I think I need to approach this more concretely. Let me try to construct specific examples and count.

Construction 1: Let $S = \{x_1, \ldots, x_7\} \cup \{z_1, z_2, z_3\}$ where $x_i$ are real and $z_j$ are non-real. Suppose $f(z) = z^2 + c$ (for some real $c$) permutes $S$. Then $f$ permutes the $x_i$ and the $z_j$ separately.

For the $x_i$: $f$ is a real quadratic permuting 7 real numbers. The cycle structure has order $\geq 4$ (as argued above). 

For the $z_j$: $f$ permutes 3 non-real numbers. Since $f$ has real coefficients, $f(\bar{z}) = \overline{f(z)}$. If the $z_j$ include a conjugate pair, say $z_1 = \bar{z_2}$, then $f(z_1) = \overline{f(z_2)}$, so $f$ maps the pair $\{z_1, z_2\}$ to a conjugate pair in $S$. The only conjugate pair among the non-real elements is $\{z_1, z_2\}$, so $f$ maps $\{z_1, z_2\}$ to itself. And $f(z_3) = z_3$ (since $z_3$ is the only remaining non-real element). So $z_3$ is a fixed point, and $\{z_1, z_2\}$ is either fixed or swapped.

If $z_3$ is a fixed point, then $f(z_3) = z_3$, so $z_3^2 + c = z_3$, meaning $c = z_3 - z_3^2$. But $c$ is real and $z_3$ is non-real, so $z_3 - z_3^2$ must be real. If $z_3 = a + bi$ ($b \neq 0$), then $z_3 - z_3^2 = (a + bi) - (a^2 - b^2 + 2abi) = (a - a^2 + b^2) + (b - 2ab)i$. For this to be real, $b(1 - 2a) = 0$, so $a = 1/2$ (since $b \neq 0$). So $z_3 = 1/2 + bi$ for some $b \neq 0$, and $c = 1/2 - (1/4 + b^2) = 1/4 - b^2$.

Then $z_1, z_2$ are a conjugate pair, and $f$ either fixes both or swaps them. If $f$ fixes both, $z_1^2 + c = z_1$ and $z_2^2 + c = z_2$, so both are roots of $z^2 - z + c = 0$, i.e., $z = (1 \pm \sqrt{1 - 4c})/2$. With $c = 1/4 - b^2$, $1 - 4c = 1 - 1 + 4b^2 = 4b^2$, so $z = (1 \pm 2b)/2 = 1/2 \pm b$. But these are real! Contradiction since $z_1, z_2$ are non-real.

So $f$ can't fix both $z_1$ and $z_2$ if they're a conjugate pair and $z_3$ is a fixed point (with $f(z) = z^2 + c$). So $f$ must swap $z_1$ and $z_2$: $f(z_1) = z_2, f(z_2) = z_1$. This means $z_1^2 + c = z_2 = \bar{z_1}$, so $z_1^2 + c = \bar{z_1}$, i.e., $z_1^2 - \bar{z_1} + c = 0$.

With $z_1 = a + bi$ and $c = 1/4 - b_3^2$ (where $z_3 = 1/2 + b_3 i$):
$z_1^2 - \bar{z_1} + c = (a^2 - b^2 + 2abi) - (a - bi) + (1/4 - b_3^2) = (a^2 - b^2 - a + 1/4 - b_3^2) + (2ab + b)i = 0$.

So: $2ab + b = 0 \Rightarrow b(2a + 1) = 0 \Rightarrow a = -1/2$ (since $b \neq 0$).
And: $a^2 - b^2 - a + 1/4 - b_3^2 = 0 \Rightarrow 1/4 - b^2 + 1/2 + 1/4 - b_3^2 = 0 \Rightarrow 1 - b^2 - b_3^2 = 0 \Rightarrow b^2 + b_3^2 = 1$.

So $z_1 = -1/2 + bi$, $z_2 = -1/2 - bi$, $z_3 = 1/2 + b_3 i$ with $b^2 + b_3^2 = 1$, $b, b_3 \neq 0$.

And $c = 1/4 - b_3^2 = 1/4 - (1 - b^2) = b^2 - 3/4$.

So $f(z) = z^2 + b^2 - 3/4$.

Now, $f$ also needs to permute the 7 real elements. The 7 real elements are periodic points of $f$ with appropriate cycle structure.

This gives one quadratic $f$. Can we find others?

If we use a different quadratic $g(z) = dz^2 + ez + h$ (with real coefficients) permuting the same $S$, then $g$ also permutes the 3 non-real elements. By the same argument, $g$ must fix $z_3$ and swap $z_1, z_2$ (or fix all three, but we showed fixing all three leads to a contradiction for the form $z^2 + c$; for a general quadratic, let me re-examine).

Actually, I was too specific. Let me consider general real quadratics $g(z) = \alpha z^2 + \beta z + \gamma$ permuting the 3 non-real elements $\{z_1, z_2, z_3\}$ where $z_1 = \bar{z_2}$ and $z_3$ has $\bar{z_3} \notin S$.

$g$ must map $\{z_1, z_2\}$ to itself (since it's the only conjugate pair) and fix $z_3$. So $g(z_3) = z_3$, meaning $\alpha z_3^2 + \beta z_3 + \gamma = z_3$.

And either $g(z_1) = z_1, g(z_2) = z_2$ (both fixed) or $g(z_1) = z_2, g(z_2) = z_1$ (swapped).

Case A: $g$ fixes all 3 non-real elements. Then $g(z) - z$ has roots $z_1, z_2, z_3$, so $g(z) - z = \alpha(z - z_1)(z - z_2)(z - z_3)/\alpha$... wait, $g(z) - z$ is a quadratic (degree 2 if $\alpha \neq 0$, or degree 1 if $\alpha = 0$). But it has 3 roots $z_1, z_2, z_3$, which is impossible for a degree-2 polynomial (unless $\alpha = 0$, making it degree 1, which can't have 3 roots either). 

Wait, $g(z) - z = \alpha z^2 + (\beta - 1)z + \gamma$, which is degree 2 (if $\alpha \neq 0$) and can have at most 2 roots. But we need 3 roots ($z_1, z_2, z_3$). Contradiction! So $g$ cannot fix all 3 non-real elements.

Case B: $g$ swaps $z_1, z_2$ and fixes $z_3$. Then $g(z_3) = z_3$ (1 root of $g(z) - z$) and $g(z_1) = z_2 \neq z_1$, $g(z_2) = z_1 \neq z_2$. So $g(z) - z$ has exactly 1 root among the non-real elements ($z_3$). The other root of $g(z) - z$ is some other value (possibly real or non-real, but not in $\{z_1, z_2\}$).

So every real quadratic permuting $S$ must swap $z_1, z_2$ and fix $z_3$. This means all real quadratics permuting $S$ agree on the 3 non-real elements: $g(z_1) = z_2, g(z_2) = z_1, g(z_3) = z_3$.

Now, two quadratics that agree on 3 points are identical. So there is at most ONE real quadratic permuting $S$ (in this configuration where the non-real elements include one conjugate pair and one unpaired element).

Wait, that's a key insight! If all real quadratics permuting $S$ must agree on the 3 non-real elements (swap the pair, fix the unpaired one), then any two such quadratics agree on 3 points, hence are identical. So there's at most 1 real quadratic permuting $S$.

Hmm, but this is for the specific configuration where the 3 non-real elements include exactly one conjugate pair. What if the 3 non-real elements have no conjugate pairs (Case 3 from earlier)?

Case 3: No conjugate pairs among the 3 non-real elements. Then $\bar{z_i} \notin S$ for all $i$. A real quadratic $g$ permuting the 3 non-real elements can be any permutation (since conjugation doesn't constrain it). But $g$ has real coefficients, so $g(\bar{z_i}) = \overline{g(z_i)}$. Since $\bar{z_i} \notin S$, this doesn't directly constrain the permutation on $S$.

But wait, $g$ is a real quadratic, so $g(z) - z$ has real coefficients. Its roots are either real or come in conjugate pairs. The fixed points of $g$ among the non-real elements are roots of $g(z) - z$, so they come in conjugate pairs. Since no two non-real elements are conjugates, $g$ can have at most 0 non-real fixed points (a conjugate pair would require 2 non-real elements that are conjugates, but we have no such pair). Wait, actually $g(z) - z$ has degree 2 and real coefficients, so it has 0 or 2 non-real roots (conjugate pair) or 2 real roots. If it has a non-real conjugate pair as roots, those roots are $\bar{}$ of each other, but neither is in $S$ (since no conjugate pair is in $S$). So $g$ has 0 non-real fixed points in $S$.

So $g$ has no fixed points among the 3 non-real elements. The permutation of 3 elements with no fixed points is a 3-cycle. So $g$ acts as a 3-cycle on the non-real elements.

There are two 3-cycles on 3 elements: $(z_1 z_2 z_3)$ and $(z_1 z_3 z_2)$. So there are at most 2 possible actions on the non-real elements. But different quadratics with the same action on the non-real elements would agree on 3 points and hence be identical. So there are at most 2 real quadratics permuting $S$ (one for each 3-cycle).

Wait, but we also need the quadratic to permute the 7 real elements. So the 2 quadratics (corresponding to the two 3-cycles) must also permute the 7 real elements. This might not be possible simultaneously.

Hmm, let me reconsider. If $g_1$ and $g_2$ are two real quadratics permuting $S$, with $g_1$ acting as $(z_1 z_2 z_3)$ and $g_2$ acting as $(z_1 z_3 z_2)$ on the non-real elements, then $g_1$ and $g_2$ agree on 0 of the 3 non-real elements. They could differ on the real elements too. But $g_1$ and $g_2$ are both quadratics, so they agree on at most 2 points total. Since they disagree on all 3 non-real elements, they can agree on at most $2 - 0 = 2$... wait, they already disagree on 3 points, but two quadratics can disagree on all points. The constraint is they agree on at most 2 points, which is satisfied (they agree on 0 non-real points, and could agree on 0, 1, or 2 real points).

So in Case 3, we could have up to 2 real quadratics. But can we actually achieve 2?

Let me think about this. We need two real quadratics $g_1, g_2$ such that:
- Both permute the same 7 real numbers.
- $g_1$ acts as $(z_1 z_2 z_3)$ and $g_2$ acts as $(z_1 z_3 z_2)$ on the 3 non-real numbers.
- The overall order of each $g_i$ on $S$ is $\geq 4$.

For the order: $g_1$ has a 3-cycle on non-real elements, so the order on non-real elements is 3. The order on real elements must be such that lcm(order_real, 3) $\geq 4$, so order_real $\geq 4$. Similarly for $g_2$.

This is getting very involved. Let me step back and think about whether non-real coefficient quadratics could contribute more.

Non-real coefficient quadratics: $f(z) = az^2 + bz + c$ with at least one of $a, b, c$ non-real. Such $f$ can map real elements to non-real elements and vice versa.

If $f$ maps some real element to a non-real element, then $f$ mixes the real and non-real parts. The constraint is that $f$ permutes all 10 elements.

Let me think about how many elements can be "mixed." If $f$ maps $k$ real elements to non-real elements, then $f$ maps $k$ non-real elements to real elements (to maintain the bijection). So $k$ real elements go to non-real, $k$ non-real elements go to real, $7 - k$ real elements stay real, $3 - k$ non-real elements stay non-real. We need $k \leq 3$ (only 3 non-real elements).

For $k = 0$: $f$ preserves the real/non-real split. This is the case of real coefficients (well, not necessarily—$f$ could have non-real coefficients but still map reals to reals, but that's very special). Actually, if $f$ maps all 7 real elements to real numbers, then $f(x) \in \mathbb{R}$ for 7 real values $x$. A quadratic $f(z) = az^2 + bz + c$ with $f(x) \in \mathbb{R}$ for 7 real $x$... if $a = a_1 + a_2 i$, then $f(x) = a_1 x^2 + b_1 x + c_1 + i(a_2 x^2 + b_2 x + c_2)$. For $f(x) \in \mathbb{R}$, we need $a_2 x^2 + b_2 x + c_2 = 0$ for 7 values of $x$. But a quadratic in $x$ has at most 2 real roots, so $a_2 = b_2 = c_2 = 0$, meaning $a, b, c$ are all real. So $k = 0$ implies real coefficients.

For $k \geq 1$: $f$ has non-real coefficients and mixes real and non-real elements.

Let me think about $k = 3$: all 3 non-real elements map to real elements, and 3 real elements map to non-real elements. So $f$ maps 3 real → non-real, 4 real → real, 3 non-real → real, 0 non-real → non-real. So the 3 non-real elements all map to real elements, and 3 of the 7 real elements map to non-real elements.

In this case, the 3 non-real elements of $S$ are mapped to 3 of the 7 real elements, and 3 of the 7 real elements are mapped to the 3 non-real elements. The remaining 4 real elements map to the remaining 4 real elements.

This is a valid permutation structure. The question is whether such a quadratic exists and how many can exist.

Let me think about the constraint on fixed points. $f(z) = z$ has at most 2 solutions. The fixed points could be real or non-real.

OK, I think I need to approach this problem more systematically. Let me think about the maximum number of quadratic polynomial permutations of a 10-element set (without the real/non-real constraint first), and then see how the constraint affects things.

Actually, let me reconsider. The problem is asking for the maximum over all valid $S$. So we need to find the best $S$.

Let me think about the problem from the perspective of the answer. I suspect the answer might be around 3-6.

Let me try to think about upper bounds.

Upper bound argument: 

Each quadratic polynomial permuting $S$ is a permutation of $S$ with order $\geq 4$. Two such quadratics agree on at most 2 elements of $S$.

Consider the $m$ quadratics as permutations $\sigma_1, \ldots, \sigma_m$ of $S = \{1, \ldots, 10\}$. Each $\sigma_i$ has order $\geq 4$, and any two agree in at most 2 positions.

Now, additionally, each $\sigma_i$ must be realizable as a quadratic polynomial on the specific complex numbers in $S$. This is a very strong constraint.

Let me think about the problem differently. Let me consider the "interpolation" approach.

A quadratic $f$ is determined by $f(s_1), f(s_2), f(s_3)$ for any 3 distinct $s_1, s_2, s_3 \in S$. So the number of quadratics permuting $S$ is the number of ordered triples $(v_1, v_2, v_3) \in S^3$ (distinct) such that the interpolating quadratic maps all of $S$ into $S$ bijectively.

The interpolating quadratic for $f(s_i) = v_i$ is:
$f(z) = \sum_{i=1}^{3} v_i \prod_{j \neq i} \frac{z - s_j}{s_i - s_j}$

This is a polynomial of degree $\leq 2$ in $z$ (Lagrange interpolation). For it to be a quadratic (degree exactly 2), we need the leading coefficient to be non-zero.

The condition $f(S) = S$ means $f(s_k) \in S$ for all $k = 1, \ldots, 10$ and $f$ is a bijection on $S$.

This is a system of constraints that's hard to analyze in general.

Let me try a completely different approach. Let me think about the problem using the theory of polynomial automorphisms of finite sets.

A key theorem: If $f$ is a polynomial of degree $d$ permuting a finite set $S$ of $n$ points, then the cycle lengths of $f$ on $S$ divide the order of $f$ as a permutation, and this order $d_{\text{perm}}$ satisfies $d^{d_{\text{perm}}} \geq n$ (since $f^{d_{\text{perm}}}(z) - z$ has degree $d^{d_{\text{perm}}}$ and at least $n$ roots).

For $d = 2, n = 10$: $2^{d_{\text{perm}}} \geq 10$, so $d_{\text{perm}} \geq 4$.

Now, let me think about the structure of the set of quadratic permutations.

Key observation: If $f$ and $g$ are quadratic polynomials permuting $S$, and $f \neq g$, then $f - g$ is a polynomial of degree $\leq 2$ with at most 2 roots. So $f$ and $g$ agree on at most 2 elements of $S$.

Now, consider 3 distinct quadratics $f, g, h$ permuting $S$. Each pair agrees on at most 2 elements. 

Let me think about the "permutation matrix" approach. For each quadratic $f_i$, define the permutation matrix $P_i$ where $(P_i)_{jk} = 1$ if $f_i(s_j) = s_k$. The condition that two quadratics agree on at most 2 elements means $P_i \cdot P_j^T$ has at most 2 ones on the diagonal (i.e., $\text{tr}(P_i P_j^T) \leq 2$).

This is related to the theory of permutation codes with Hamming distance. The Hamming distance between $\sigma_i$ and $\sigma_j$ is $10 - |\{k : \sigma_i(k) = \sigma_j(k)\}| \geq 10 - 2 = 8$.

So we need a set of permutations of 10 elements with pairwise Hamming distance $\geq 8$, and each permutation must be realizable as a quadratic polynomial on $S$.

The maximum size of a permutation code of length 10 with minimum distance 8 is known in coding theory. But the additional constraint of being a quadratic polynomial is much more restrictive.

Let me try yet another approach. Let me think about the problem using the concept of "functional graphs" and "polynomial symmetries."

If $f$ is a quadratic permuting $S$, the functional graph of $f$ on $S$ is a union of cycles (since $f$ is a bijection). The cycle structure is constrained as above.

Now, here's a key idea: if $f$ and $g$ are both quadratics permuting $S$, consider $h = g \circ f^{-1}$ as a permutation of $S$. This is a permutation of $S$ but not necessarily a polynomial. However, $h$ maps $S$ to $S$, and $h = g \circ f^{-1}$ where $f^{-1}$ is the inverse permutation (not polynomial).

Alternatively, $g \circ f$ is a degree-4 polynomial permuting $S$. The set of all polynomial permutations of $S$ (of any degree) forms a group $G$ under composition. The quadratic elements of $G$ are what we're counting.

The group $G$ is a subgroup of $S_{10}$. The quadratic elements are specific elements of $G$.

Now, $G$ is the group of polynomial automorphisms of $S$. For a generic set $S$ of 10 points, $G$ is trivial (only the identity, which is degree 0/1). For special sets, $G$ can be larger.

The question is: what's the maximum number of degree-2 elements in $G$, over all sets $S$ with 7 real and 3 non-real elements?

Let me think about what groups $G$ can arise. $G$ is a subgroup of $S_{10}$ that acts as polynomial automorphisms. The elements of $G$ have specific degrees (as polynomials), and the degree-2 elements are what we want.

For a set of $n$ points, the group of polynomial automorphisms can be at most the symmetric group $S_n$ (if every permutation is a polynomial), but this requires degree up to $n-1$. For quadratics, we're much more restricted.

Let me think about specific groups.

If $G$ is cyclic of order $d$, generated by a quadratic $f$, then the quadratic elements of $G$ are just $\{f\}$ (since $f^k$ has degree $2^k$, which is 2 only for $k = 1$). So a cyclic group gives at most 1 quadratic.

If $G$ is larger, say $G = S_3$ (acting on 3 elements and fixing the other 7), then the degree-2 elements of $G$ are the transpositions and 3-cycles that can be realized as quadratics. But a transposition has order 2, and $2^2 = 4 < 10$, so a transposition can't be a quadratic permuting 10 elements (the order is too small). Similarly, a 3-cycle has order 3, and $2^3 = 8 < 10$, so it can't be a quadratic permuting 10 elements.

Wait, this is the key constraint: every quadratic permuting $S$ must have order $\geq 4$ as a permutation of $S$. So the quadratic elements of $G$ must have order $\geq 4$.

In $S_{10}$, the elements of order $\geq 4$ include: 4-cycles, 5-cycles, 6-cycles, 7-cycles, 8-cycles, 9-cycles, 10-cycles, and products like (4,2), (4,3), (5,2), (5,3), (5,4), (6,2), (6,3), (6,4), (6,5), (7,2), (7,3), etc.

But not all of these can be realized as quadratics (due to the cycle structure constraints from earlier).

Let me think about whether multiple quadratics can permute the same set.

Suppose $f$ and $g$ are quadratics permuting $S$, both of order $\geq 4$. Consider the group $H = \langle f, g \rangle$ (as permutations of $S$). This is a subgroup of $S_{10}$.

If $f$ and $g$ commute (as permutations), then $H$ is abelian. The order of $fg$ is lcm-related to the orders of $f$ and $g$. But $fg$ is a degree-4 polynomial, not quadratic.

If $f$ and $g$ don't commute, $H$ is non-abelian.

The number of quadratic elements in $H$ is what we want to maximize. Each quadratic element has order $\geq 4$ and specific cycle structure constraints.

This is still very abstract. Let me try to think about concrete constructions.

Construction attempt: Let me try to find $S$ with 2 quadratic polynomial permutations.

Let $f(z) = z^2 - 2$ (Chebyshev). As discussed, all periodic points of $f$ are real. So $f$ can only permute real sets. To include non-real elements, I need a different approach.

Let me try $f(z) = \omega z^2$ where $\omega$ is a primitive cube root of unity. Then $f$ maps $z        — AI历史解题过程（thinking）
#   polymath_02735         — 题目ID

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
  <problem_id>polymath_02735</problem_id>
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

Let $S = \{s_1, s_2, \dots, s_{10}\}$ be a set of 10 distinct complex numbers such that exactly $10-3=7$ of them are real numbers. Let $N$ be the maximum possible number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$ (meaning $f$ maps $S$ onto itself). Find the value of $N$.

## Standard Solution

Based on the original solution, any such quadratic polynomial $f$ must have real coefficients because $n \ge 9$. The three non-real complex numbers $z_1, z_2, z_3$ in $S$ must be permuted by $f$. Case (1) where two are conjugates leads to at most one such quadratic polynomial. Case (2) where no two are conjugates leads to at most two possible permutations (3-cycles) and hence at most two polynomials. In either case, the maximum number of such quadratic polynomials is 2.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have a set $S$ of 10 distinct complex numbers, exactly 7 real and 3 non-real. We need to find the maximum number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$ (i.e., $f$ permutes $S$).

Let me think about this carefully.

A quadratic polynomial $f(z) = az^2 + bz + c$ with $a \neq 0$ maps $S$ to itself as a set. Since $f$ is a function (not necessarily injective on $\mathbb{C}$), $f(S) = S$ means $f$ maps $S$ onto $S$.

Since $|S| = 10$ and $f(S) = S$, $f$ restricted to $S$ is a surjection from $S$ to $S$, hence a bijection (since $S$ is finite). So $f$ permutes the elements of $S$.

Now, a quadratic polynomial is a degree-2 map. The key constraint: $f$ is a permutation of $S$, but $f$ is a degree-2 polynomial.

Let me think about the structure. If $f$ permutes $S$, then for any $s \in S$, the orbit of $s$ under $f$ is a cycle. The cycle structure of the permutation must be compatible with $f$ being a polynomial of degree 2.

Key fact: If $f$ is a polynomial of degree $d$ and $f$ permutes a finite set $S$, then the cycle lengths divide... well, let me think differently.

Actually, let me think about this more carefully. The real numbers and non-real numbers.

If $f(z) = az^2 + bz + c$ with complex coefficients. The non-real elements come in conjugate pairs (since exactly 3 non-real... wait, no. The 3 non-real elements don't have to be closed under conjugation. The set $S$ is just 10 distinct complex numbers, 7 real and 3 non-real. The 3 non-real ones could be anything.

Wait, but $f$ has complex coefficients, so $f$ doesn't need to respect conjugation.

Let me reconsider. We want to maximize the number of quadratic polynomials $f$ such that $f(S) = S$. We get to choose $S$ (the 10 numbers, 7 real, 3 non-real) to maximize this count.

So the question is: over all choices of $S$ (7 real, 3 non-real, all distinct), what is the maximum number of quadratic polynomials $f$ with $f(S) = S$?

Let me think about what constraints a quadratic polynomial permutation of $S$ must satisfy.

If $f$ is a quadratic polynomial and $f$ permutes $S$ (a set of 10 points), then $f$ is determined by its values on any 3 points (since a quadratic has 3 coefficients, well 3 complex coefficients $a, b, c$ with $a \neq 0$). Actually, a quadratic is determined by its values at 3 distinct points. So if we know $f(s_1), f(s_2), f(s_3)$ for 3 distinct points, $f$ is uniquely determined.

So the number of quadratic polynomials permuting $S$ is at most the number of permutations of $S$ that can be realized as a quadratic polynomial. Since a quadratic is determined by 3 values, we need the permutation to agree with some quadratic on all 10 points.

Let me think about the cycle structure. If $f$ permutes $S$ and $f$ is a polynomial of degree 2, consider the iterates $f, f^2, f^3, \ldots$. The permutation has some cycle structure.

Key observation: If $f$ has a cycle of length $k$ in $S$, i.e., $f^k(s) = s$ for some $s \in S$, then $f^k(z) - z$ is a polynomial of degree $2^k$ that vanishes at $s$. But $f^k(z) - z$ vanishes at all elements in the cycle of $s$.

Actually, let me think about it differently. Let's consider the functional graph. $f: S \to S$ is a permutation, so it decomposes into cycles.

For a quadratic polynomial, the equation $f(z) = w$ has at most 2 solutions for any $w$. So in the permutation, each element has exactly one preimage (since it's a bijection), but the polynomial $f(z) = w$ has at most 2 solutions in $\mathbb{C}$. So for each $w \in S$, exactly one of the (at most 2) preimages under $f$ is in $S$.

Hmm, this doesn't immediately constrain things much.

Let me think about fixed points. $f(z) = z$ is a quadratic equation (assuming $a \neq 0$), so it has at most 2 solutions. So $f$ has at most 2 fixed points in $S$.

More generally, $f^k(z) = z$ is a polynomial equation of degree $2^k$, so it has at most $2^k$ solutions. The number of elements in $S$ that are in cycles of length dividing $k$ is at most $2^k$.

So the cycle structure of the permutation $f|_S$ must satisfy: the number of elements in cycles of length dividing $k$ is at most $2^k$ for each $k$.

For $k=1$: at most 2 fixed points.
For $k=2$: at most 4 elements in cycles of length 1 or 2.
For $k=3$: at most 8 elements in cycles of length 1, 2, or 3 (well, dividing 3, so 1 or 3). At most 8 elements in cycles of length 1 or 3.
For $k=4$: at most 16 elements in cycles of length dividing 4 (1, 2, 4). Since we only have 10 elements, this is automatically satisfied.

Wait, but we need to be more careful. $f^k(z) = z$ has degree $2^k$, so at most $2^k$ roots. The elements of $S$ in cycles of length dividing $k$ are roots of $f^k(z) - z = 0$. So:

- Cycles of length dividing $k$: total elements $\leq 2^k$.

For 10 elements:
- Fixed points (length 1): $\leq 2$
- Elements in cycles of length 1 or 2: $\leq 4$
- Elements in cycles of length 1 or 3: $\leq 8$
- Elements in cycles of length 1, 2, or 4: $\leq 16$ (no constraint for 10 elements)
- Elements in cycles of length 1 or 5: $\leq 32$ (no constraint)
- Elements in cycles of length 1, 2, 3, or 6: $\leq 64$ (no constraint)

So the constraints are mainly from $k=1, 2, 3$.

Let me enumerate possible cycle structures for a permutation of 10 elements, subject to:
- At most 2 fixed points
- At most 4 elements in cycles of length $\leq 2$
- At most 8 elements in cycles of length 1 or 3

Let me denote the cycle structure. Let $c_k$ = number of cycles of length $k$.

Constraint 1: $c_1 \leq 2$.
Constraint 2: $c_1 + 2c_2 \leq 4$.
Constraint 3: $c_1 + 3c_3 \leq 8$.
Total: $c_1 + 2c_2 + 3c_3 + 4c_4 + 5c_5 + \ldots = 10$.

From constraint 2: $c_1 + 2c_2 \leq 4$, so $2c_2 \leq 4 - c_1 \leq 4$, so $c_2 \leq 2$.

Let me think about what cycle structures are possible. The remaining elements (those not in cycles of length 1, 2, or 3) must be in cycles of length $\geq 4$.

Elements in cycles of length $\geq 4$: $10 - (c_1 + 2c_2 + 3c_3) \geq 10 - (4 + 3c_3)$. 

Hmm, this is getting complicated. Let me think about which cycle structures can actually be realized by a quadratic polynomial, and then count how many distinct quadratic polynomials can permute the same set $S$.

Actually, the question is about maximizing the number of quadratic polynomials $f$ with $f(S) = S$ over all choices of $S$. So we need to find $S$ that is invariant under as many quadratic polynomials as possible.

Let me think about this differently. If $f$ and $g$ are both quadratic polynomials with $f(S) = S$ and $g(S) = S$, what can we say?

If $f$ and $g$ agree on 3 points of $S$, then $f = g$ (since a quadratic is determined by 3 points). So distinct quadratic polynomials permuting $S$ must differ on every set of 3 points, meaning they can agree on at most 2 points of $S$.

The number of quadratic polynomials permuting $S$ is at most... well, each such polynomial is a permutation of $S$, and two distinct ones agree on at most 2 points. 

If we have $m$ quadratic polynomials permuting $S$, each pair agrees on at most 2 points. The total number of "agreements" (pairs $(f, g, s)$ where $f(s) = g(s)$, $f \neq g$, $s \in S$) is at most $\binom{m}{2} \cdot 2 = m(m-1)$.

On the other hand, for each $s \in S$, the values $f_1(s), f_2(s), \ldots, f_m(s)$ are elements of $S$ (since each $f_i$ permutes $S$). The number of agreements at point $s$ is $\sum_{v \in S} \binom{|\{i : f_i(s) = v\}|}{2}$. 

Hmm, this is getting complicated. Let me think about specific constructions.

A key example: Consider $S$ being the set of 10th roots of unity... no, those are all on the unit circle, not 7 real.

Let me think about what sets can be invariant under multiple quadratic polynomials.

Example 1: $f(z) = z^2$. This maps roots of unity to roots of unity. If $S$ consists of 10th roots of unity... but those aren't 7 real.

Example 2: Consider Chebyshev-like maps. $f(z) = z^2 - 2$ maps $[-2, 2]$ to $[-2, 2]$ in some sense (via the substitution $z = 2\cos\theta$, $f(2\cos\theta) = 4\cos^2\theta - 2 = 2\cos(2\theta)$). So if $S = \{2\cos(2\pi k / n) : k = 0, 1, \ldots, n-1\}$, then $f$ permutes $S$ (it's the doubling map mod $n$ on the indices). But these are all real.

We need 7 real and 3 non-real. So we can't use a purely real set.

Let me think about this more carefully. We need to find $S$ with 7 real and 3 non-real elements, and maximize the number of quadratic polynomials permuting $S$.

Let me consider the group of quadratic polynomial symmetries of $S$. If $f$ and $g$ both permute $S$, does $f \circ g$ permute $S$? Yes, but $f \circ g$ is a degree-4 polynomial, not quadratic. So the set of quadratic polynomials permuting $S$ doesn't form a group under composition.

However, if $f$ is a quadratic polynomial permuting $S$, then $f^k$ also permutes $S$ for all $k$, but $f^k$ has degree $2^k$, so only $f^1$ is quadratic.

Let me think about the problem from the perspective of counting. A quadratic polynomial $f(z) = az^2 + bz + c$ is determined by $(a, b, c)$ with $a \neq 0$. The condition $f(S) = S$ means $f$ permutes $S$.

Given that $f$ is determined by 3 points, and $f$ must map $S$ to $S$, we can think of it as: choose a permutation $\sigma$ of $S$, and check if there's a quadratic polynomial realizing $\sigma$ on $S$. The quadratic is determined by any 3 values, so we need the permutation to be consistent with a single quadratic on all 10 points.

Let me think about upper bounds. 

Approach: Consider the real and non-real elements separately.

If $f(z) = az^2 + bz + c$ has complex coefficients, it doesn't preserve the real line in general. But if $a, b, c$ are all real, then $f$ maps real numbers to real numbers and $\bar{z}$ to $\overline{f(z)}$.

Case 1: $f$ has real coefficients. Then $f$ maps the 7 real elements of $S$ to real numbers, so $f$ maps the real part of $S$ to real numbers. Since $f(S) = S$ and $f$ maps reals to reals, $f$ must map the 7 real elements to the 7 real elements (bijectively). And $f$ maps the 3 non-real elements to the 3 non-real elements. But wait, $f$ with real coefficients maps non-real $z$ to $f(z)$, and $\overline{f(z)} = f(\bar{z})$. If $z$ is non-real and $\bar{z} \notin S$, then $f(z)$ could be anything. But $f(z) \in S$ and $f(z)$ is non-real (since if $f(z)$ were real, then $f(\bar{z}) = \overline{f(z)} = f(z)$, but $\bar{z} \neq z$ so $f(\bar{z}) \neq f(z)$ is not necessarily true... wait, $f(\bar{z}) = \overline{f(z)}$, and if $f(z)$ is real then $f(\bar{z}) = f(z)$, meaning $f$ maps both $z$ and $\bar{z}$ to the same value, contradicting injectivity on $S$ (unless $\bar{z} \notin S$).

Hmm, let me be more careful. If $f$ has real coefficients and $f(S) = S$ (bijectively), then:
- $f$ maps the 7 real elements bijectively to the 7 real elements.
- $f$ maps the 3 non-real elements bijectively to the 3 non-real elements.
- For non-real $z \in S$, $f(z)$ is non-real (because if $f(z)$ were real, then $f(\bar{z}) = \overline{f(z)} = f(z)$, but since $f$ is injective on $S$ and $z \neq \bar{z}$, we'd need $\bar{z} \notin S$ for this to not be a contradiction... actually even if $\bar{z} \notin S$, $f(z)$ being real is fine as long as $f(z) \in S$. Wait, but I said $f$ maps non-real elements to non-real elements. Let me re-examine.

If $f$ has real coefficients, $f$ maps $\mathbb{R}$ to $\mathbb{R}$. So the 7 real elements of $S$ map to real numbers. Since $f(S) = S$ and $f$ is injective on $S$, the 7 real elements map to 7 distinct real numbers in $S$, which must be the 7 real elements. So the 3 non-real elements map to the 3 non-real elements. ✓

Case 2: $f$ has non-real coefficients. Then $f$ might map real elements to non-real elements and vice versa.

So we need to count both types.

Let me first think about Case 1 (real coefficients). We need quadratic polynomials with real coefficients that permute a set of 7 real numbers and separately permute a set of 3 non-real numbers.

For the 7 real numbers: $f$ restricted to them is a permutation, and $f$ is a real quadratic. $f(z) = w$ has at most 2 real solutions (or 0 or 1). Since $f$ is a bijection on the 7 real numbers, each real number in $S$ has exactly one preimage in $S$ under $f$, but the equation $f(z) = w$ has at most 2 solutions in $\mathbb{R}$.

The cycle structure on the 7 real elements must satisfy: fixed points $\leq 2$, elements in cycles of length $\leq 2$ is $\leq 4$, etc. (same constraints as before but for 7 elements).

For the 3 non-real elements: $f$ permutes them. $f(z) = w$ has at most 2 solutions in $\mathbb{C}$, so the 3 non-real elements, each has one preimage among the 3 non-real elements. The cycle structure on 3 elements: could be (3), (2,1), (1,1,1). Fixed points $\leq 2$ is fine. Cycles of length $\leq 2$: at most 4, fine for 3 elements.

But wait, there's an additional constraint for real coefficients: if $z$ is non-real and $f(z) = w$, then $f(\bar{z}) = \bar{w}$. If $\bar{z} \notin S$, this doesn't directly constrain things. But the 3 non-real elements: their conjugates may or may not be in $S$.

Actually, the 3 non-real elements of $S$ don't need to be closed under conjugation. But if $f$ has real coefficients, $f$ maps the 3 non-real elements to the 3 non-real elements, and conjugation commutes with $f$. So if $z$ is a non-real element of $S$ and $\bar{z} \in S$, then $f(\bar{z}) = \overline{f(z)}$, so the permutation on non-real elements respects conjugation.

This is getting complex. Let me try a different approach and think about specific constructions.

Let me think about what's the maximum number of quadratic polynomials that can permute a set of 10 points.

Upper bound approach: Each quadratic polynomial permuting $S$ is determined by its values on any 3 points of $S$. Two distinct quadratics agree on at most 2 points (since their difference is a polynomial of degree $\leq 2$, which has at most 2 roots). 

So if we have $m$ quadratics $f_1, \ldots, f_m$ permuting $S$, any two agree on at most 2 points. 

For each point $s \in S$, the values $f_1(s), \ldots, f_m(s)$ are in $S$. The number of pairs $(i, j)$ with $f_i(s) = f_j(s)$ is $\sum_{v \in S} \binom{n_v(s)}{2}$ where $n_v(s) = |\{i : f_i(s) = v\}|$ and $\sum_v n_v(s) = m$.

Total agreements: $\sum_{s \in S} \sum_{v} \binom{n_v(s)}{2} \leq \binom{m}{2} \cdot 2 = m(m-1)$.

Also, $\sum_{s, v} n_v(s) = 10m$ (each $f_i$ maps 10 elements to 10 elements). And $\sum_{s, v} \binom{n_v(s)}{2} = \sum_{s,v} \frac{n_v(s)(n_v(s)-1)}{2}$.

By convexity, for fixed $\sum n_v(s) = m$ at each $s$, the sum $\sum_v \binom{n_v(s)}{2}$ is minimized when all $n_v(s)$ are equal, i.e., $n_v(s) = m/10$ for all $v$. But we want a lower bound on the total agreements to get an upper bound on $m$.

Actually, we have $\sum_{s,v} \binom{n_v(s)}{2} \leq m(m-1)$, and we want to find the maximum $m$.

Hmm, but we also have the constraint that each $f_i$ is a permutation of $S$, so for each $i$, $\{f_i(s) : s \in S\} = S$. This means $\sum_s n_v(s) = m$ for each $v$ (each value $v$ is taken $m$ times total across all $f_i$ and all $s$). Wait no: $\sum_s n_v(s) = |\{(i, s) : f_i(s) = v\}| = \sum_i |\{s : f_i(s) = v\}| = \sum_i 1 = m$ (since each $f_i$ is a bijection, each $v$ is hit exactly once by each $f_i$). So $\sum_s n_v(s) = m$ for each $v$.

So we have a $10 \times 10$ matrix $(n_v(s))$ where:
- Row sums (over $v$): $\sum_v n_v(s) = m$ for each $s$.
- Column sums (over $s$): $\sum_s n_v(s) = m$ for each $v$.
- $\sum_{s,v} \binom{n_v(s)}{2} \leq m(m-1)$.

We want to maximize $m$.

$\sum_{s,v} \binom{n_v(s)}{2} = \frac{1}{2}\sum_{s,v} n_v(s)^2 - \frac{1}{2}\sum_{s,v} n_v(s) = \frac{1}{2}\sum_{s,v} n_v(s)^2 - 5m$.

So $\frac{1}{2}\sum n_v(s)^2 - 5m \leq m(m-1) = m^2 - m$.

$\sum n_v(s)^2 \leq 2m^2 - 2m + 10m = 2m^2 + 8m$.

By Cauchy-Schwarz or convexity, $\sum n_v(s)^2 \geq \frac{(\sum n_v(s))^2}{100} = \frac{(10m)^2}{100} = m^2$.

So $m^2 \leq 2m^2 + 8m$, which gives $0 \leq m^2 + 8m$, always true. Not helpful.

Let me try a different approach. The constraint is that $\sum n_v(s)^2 \leq 2m^2 + 8m$. With row and column sums all equal to $m$, the minimum of $\sum n_v(s)^2$ is achieved when all entries are $m/10$, giving $100 \cdot (m/10)^2 = m^2$. So we need $m^2 \leq 2m^2 + 8m$, i.e., $m \geq -8$, always true.

This approach doesn't give a useful bound. Let me think differently.

Let me think about the problem more concretely. 

Key insight: A quadratic polynomial $f$ that permutes $S$ is a permutation of $S$ whose cycle structure is constrained. Moreover, $f$ is uniquely determined by its action on any 3 elements of $S$.

Let me think about the maximum number of quadratic polynomial permutations of a 10-element set.

Consider the group $G$ of all permutations of $S$ that can be realized as polynomial maps (of any degree) preserving $S$. The quadratic polynomial permutations are a subset.

Actually, let me think about specific examples.

Example: $S = \{0, 1, 2, 3, 4, 5, 6\} \cup \{i, -i, 2i\}$ (7 real, 3 non-real). Can we find quadratic polynomials permuting this?

This seems hard to reason about abstractly. Let me think about the problem from the competition math perspective.

Let me reconsider. The problem says "maximum possible number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$". So we're maximizing over all valid $S$.

Let me think about what structures allow many quadratic symmetries.

If $S$ is invariant under a quadratic $f$, then $f$ generates a cyclic group of permutations of $S$ (via iteration). The order of $f$ as a permutation of $S$ divides... well, $f$ has some order $d$ as a permutation, and $f^d = \text{id}$ on $S$. But $f^d$ is a polynomial of degree $2^d$, and $f^d(z) - z$ has at most $2^d$ roots. Since $f^d$ is the identity on all 10 elements, $f^d(z) - z$ has at least 10 roots, so $2^d \geq 10$, meaning $d \geq 4$.

So any quadratic polynomial permuting $S$ has order at least 4 as a permutation of $S$.

Wait, that's an important constraint. The order $d$ of $f$ (as a permutation of $S$) must satisfy $2^d \geq 10$, so $d \geq 4$.

The cycle structure of $f$ on $S$ must have all cycle lengths dividing $d$, and $\text{lcm}$ of cycle lengths $= d \geq 4$.

Also, from the earlier constraints:
- At most 2 fixed points (cycles of length 1)
- At most 4 elements in cycles of length 1 or 2
- At most 8 elements in cycles of length 1 or 3

And $d \geq 4$.

Let me enumerate possible cycle structures for a permutation of 10 elements with these constraints:

Let me denote the cycle type as a partition of 10.

Constraint: $c_1 \leq 2$, $c_1 + 2c_2 \leq 4$, $c_1 + 3c_3 \leq 8$.

And the order $d = \text{lcm}(\text{cycle lengths}) \geq 4$.

Let me list partitions of 10 satisfying these:

- $c_1 = 0$: No fixed points. $2c_2 \leq 4 \Rightarrow c_2 \leq 2$. $3c_3 \leq 8 \Rightarrow c_3 \leq 2$.
  Remaining elements: $10 - 2c_2 - 3c_3$, must be in cycles of length $\geq 4$.
  
  - $c_2 = 0, c_3 = 0$: 10 elements in cycles of length $\geq 4$. Partitions: (10), (6,4), (5,5), (4,4,2)... wait $c_2=0$. (10), (6,4), (5,5), (4,4,...) but 4+4=8, need 2 more, but $c_2=0$ and $c_1=0$, so need a cycle of length 2, contradiction. So (10), (6,4), (5,5). Also (4,6) same as (6,4). What about (7,3)? No, $c_3=0$. (8,2)? No, $c_2=0$. (9,1)? No, $c_1=0$.
  
  Actually wait, I need to be more careful. Let me just enumerate all partitions of 10 and check constraints.
  
  Partitions of 10:
  - (10): $c_1=0, c_2=0, c_3=0$. ✓ Order = 10 ≥ 4. ✓
  - (9,1): $c_1=1 \leq 2$. ✓ $c_1+2c_2=1 \leq 4$. ✓ $c_1+3c_3=1 \leq 8$. ✓ Order = 9 ≥ 4. ✓
  - (8,2): $c_1=0, c_2=1$. $c_1+2c_2=2 \leq 4$. ✓ Order = 8 ≥ 4. ✓
  - (8,1,1): $c_1=2$. $c_1+2c_2=2 \leq 4$. ✓ Order = 8 ≥ 4. ✓
  - (7,3): $c_3=1$. $c_1+3c_3=3 \leq 8$. ✓ Order = 21 ≥ 4. ✓
  - (7,2,1): $c_1=1, c_2=1$. $c_1+2c_2=3 \leq 4$. ✓ Order = 14 ≥ 4. ✓
  - (7,1,1,1): $c_1=3 > 2$. ✗
  - (6,4): Order = 12 ≥ 4. ✓ $c_1=0, c_2=0, c_3=0$. ✓
  - (6,3,1): $c_1=1, c_3=1$. $c_1+3c_3=4 \leq 8$. ✓ Order = 6 ≥ 4. ✓
  - (6,2,2): $c_2=2$. $c_1+2c_2=4 \leq 4$. ✓ Order = 6 ≥ 4. ✓
  - (6,2,1,1): $c_1=2, c_2=1$. $c_1+2c_2=4 \leq 4$. ✓ Order = 6 ≥ 4. ✓
  - (6,1,1,1,1): $c_1=4 > 2$. ✗
  - (5,5): Order = 5 ≥ 4. ✓
  - (5,4,1): $c_1=1$. Order = 20 ≥ 4. ✓
  - (5,3,2): $c_2=1, c_3=1$. $c_1+2c_2=2 \leq 4$. $c_1+3c_3=3 \leq 8$. ✓ Order = 30 ≥ 4. ✓
  - (5,3,1,1): $c_1=2, c_3=1$. $c_1+3c_3=5 \leq 8$. ✓ Order = 15 ≥ 4. ✓
  - (5,2,2,1): $c_1=1, c_2=2$. $c_1+2c_2=5 > 4$. ✗
  - (5,2,1,1,1): $c_1=3 > 2$. ✗
  - (5,1,1,1,1,1): ✗
  - (4,4,2): $c_2=1$. $c_1+2c_2=2 \leq 4$. ✓ Order = 4 ≥ 4. ✓
  - (4,4,1,1): $c_1=2$. $c_1+2c_2=2 \leq 4$. ✓ Order = 4 ≥ 4. ✓
  - (4,3,3): $c_3=2$. $c_1+3c_3=6 \leq 8$. ✓ Order = 12 ≥ 4. ✓
  - (4,3,2,1): $c_1=1, c_2=1, c_3=1$. $c_1+2c_2=3 \leq 4$. $c_1+3c_3=4 \leq 8$. ✓ Order = 12 ≥ 4. ✓
  - (4,3,1,1,1): $c_1=3 > 2$. ✗
  - (4,2,2,2): $c_2=3$. $c_1+2c_2=6 > 4$. ✗
  - (4,2,2,1,1): $c_1=2, c_2=2$. $c_1+2c_2=6 > 4$. ✗
  - (4,2,1,1,1,1): ✗
  - (4,1,...): ✗ (too many fixed points)
  - (3,3,3,1): $c_1=1, c_3=3$. $c_1+3c_3=10 > 8$. ✗
  - (3,3,2,2): $c_2=2, c_3=2$. $c_1+2c_2=4 \leq 4$. $c_1+3c_3=6 \leq 8$. ✓ Order = 6 ≥ 4. ✓
  - (3,3,2,1,1): $c_1=2, c_2=1, c_3=2$. $c_1+2c_2=4 \leq 4$. $c_1+3c_3=8 \leq 8$. ✓ Order = 6 ≥ 4. ✓
  - (3,3,1,1,1,1): ✗
  - (3,2,2,2,1): $c_1=1, c_2=3$. $c_1+2c_2=7 > 4$. ✗
  - (3,2,2,1,1,1): ✗
  - (3,2,1,...): ✗
  - (3,1,...): ✗
  - (2,2,2,2,2): $c_2=5$. $c_1+2c_2=10 > 4$. ✗
  - (2,2,2,2,1,1): $c_1=2, c_2=4$. $c_1+2c_2=10 > 4$. ✗
  - etc. All with many 2-cycles: ✗
  - (2,2,2,1,1,1,1): ✗
  - (2,2,1,...): ✗
  - (2,1,...): ✗
  - (1,...): ✗

So the valid cycle types are:
(10), (9,1), (8,2), (8,1,1), (7,3), (7,2,1), (6,4), (6,3,1), (6,2,2), (6,2,1,1), (5,5), (5,4,1), (5,3,2), (5,3,1,1), (4,4,2), (4,4,1,1), (4,3,3), (4,3,2,1), (3,3,2,2), (3,3,2,1,1).

That's 20 valid cycle types. But not all of these can necessarily be realized by a quadratic polynomial, and even if they can, we need to count how many distinct quadratic polynomials can simultaneously permute the same set $S$.

This is getting very complicated. Let me think about the problem differently.

Let me think about the structure of the set of quadratic polynomials permuting $S$.

If $f$ and $g$ are quadratic polynomials permuting $S$, consider $h = g \circ f^{-1}$. This is a polynomial map (since $f$ is a bijection on $S$, $f^{-1}$ exists as a function on $S$, but not necessarily as a polynomial). So $h$ is a permutation of $S$ but not necessarily a polynomial.

Alternatively, consider $g \circ f$, which is a degree-4 polynomial permuting $S$.

Let me think about a different approach. 

Key idea: If $f$ is a quadratic polynomial permuting $S$, then $f$ is a permutation of $S$ with order $d \geq 4$. The powers $f, f^2, f^3, \ldots, f^{d-1}$ are all permutations of $S$, but only $f$ is quadratic (the others have higher degree). So each quadratic polynomial gives one permutation.

Now, how many quadratic polynomials can permute the same $S$?

Let me think about small cases first. Suppose $|S| = n$ and we want to maximize the number of quadratic polynomial permutations.

For the problem at hand, $n = 10$ with 7 real and 3 non-real.

Let me think about the problem from the answer's perspective. This is likely a competition problem with a clean answer. Let me think about what structures could give many quadratic symmetries.

Consider the Chebyshev map $T_2(z) = z^2 - 2$. We have $T_2(2\cos\theta) = 2\cos(2\theta)$. If $S_0 = \{2\cos(2\pi k / n) : k = 0, 1, \ldots, n-1\}$, then $T_2$ acts on $S_0$ as the doubling map $k \mapsto 2k \pmod{n}$.

But these are all real. We need 3 non-real elements.

What if we consider a different quadratic map that has both real and non-real periodic points?

Actually, let me think about this differently. Let me consider the general theory.

A quadratic polynomial $f(z) = az^2 + bz + c$ can be conjugated to the form $z^2 + c_0$ by an affine change of variables. So WLOG, we can consider $f(z) = z^2 + c_0$ (by conjugating $S$ appropriately). But different quadratics would require different conjugations, so this only helps for a single quadratic.

Let me think about the problem more carefully.

Suppose we have $m$ quadratic polynomials $f_1, \ldots, f_m$ permuting $S$. Each $f_i$ is a permutation of $S$ with order $\geq 4$. 

Now, the key constraint is the real/non-real split. Let me think about how the real and non-real elements interact.

If $f$ has real coefficients, it preserves the real/non-real split (maps reals to reals, non-reals to non-reals). If $f$ has non-real coefficients, it might mix them.

Let me count separately:
- $m_{\text{real}}$: number of quadratic polynomials with real coefficients permuting $S$.
- $m_{\text{complex}}$: number of quadratic polynomials with non-real coefficients permuting $S$.

$m = m_{\text{real}} + m_{\text{complex}}$.

For $m_{\text{real}}$: $f$ permutes the 7 real elements and the 3 non-real elements separately. The constraint on the 7 real elements: $f$ is a real quadratic permuting 7 real numbers. The constraint on the 3 non-real elements: $f$ permutes 3 non-real numbers (and $f$ has real coefficients, so it respects conjugation if applicable).

For a real quadratic permuting 7 real numbers: the cycle structure on 7 elements must satisfy fixed points $\leq 2$, elements in cycles of length $\leq 2$ is $\leq 4$, order $\geq 4$ (since $2^d \geq 7$ requires $d \geq 3$, but actually $2^3 = 8 \geq 7$, so $d \geq 3$).

Wait, I need to recompute. For 7 elements, $f^d = \text{id}$ on all 7, so $f^d(z) - z$ has at least 7 roots, degree $2^d$, so $2^d \geq 7$, meaning $d \geq 3$.

For 3 non-real elements, $2^d \geq 3$, so $d \geq 2$.

But the order of $f$ as a permutation of all 10 elements is the lcm of the orders on the real and non-real parts. So the overall order $d = \text{lcm}(d_{\text{real}}, d_{\text{non-real}}) \geq 4$ (from the 10-element constraint).

Hmm wait, actually the constraint $2^d \geq 10$ comes from $f^d(z) - z$ having 10 roots. But if $f$ has real coefficients, $f^d$ also has real coefficients, and $f^d(z) - z$ has 10 roots (7 real + 3 non-real). The degree is $2^d$, so $2^d \geq 10$, $d \geq 4$. This is the overall constraint.

But there are also separate constraints: $f^d(z) - z$ restricted to real roots: the 7 real roots are among the roots of $f^d(z) - z$, which has degree $2^d$. So $2^d \geq 7$ is weaker than $2^d \geq 10$.

OK so the overall constraint is $d \geq 4$ regardless.

Let me try to think about this problem from a higher level. 

I think the key insight is that the number of quadratic polynomials permuting $S$ is quite limited, and we need to find the optimal $S$.

Let me consider the following approach: think about the "group" generated by the quadratic polynomial permutations. If $f$ and $g$ are quadratic polynomials permuting $S$, then $f \circ g$ is a degree-4 polynomial permuting $S$, and $g \circ f$ is also degree-4. These might or might not be equal.

If $f \circ g = g \circ f$ (they commute), then the group they generate is abelian. The set of all polynomial permutations of $S$ (of any degree) forms a group, and the quadratic ones are specific elements.

Actually, let me think about a specific construction. 

Consider the set $S = \{\zeta^k : k = 0, 1, \ldots, 9\}$ where $\zeta = e^{2\pi i/10}$, the 10th roots of unity. The map $z \mapsto z^2$ permutes these (it's the doubling map mod 10). But these are not 7 real and 3 non-real; the 10th roots of unity include only 2 real ones ($1$ and $-1$).

What if we use a different set? Let me think...

Consider $S$ consisting of 7 real numbers forming a Chebyshev-type set, plus 3 non-real numbers.

Actually, let me think about the problem differently. Let me consider what happens with the map $z \mapsto z^2 - 2$ on specific sets.

$T(z) = z^2 - 2$. $T(2\cos\theta) = 2\cos(2\theta)$. 

If we take $S_{\text{real}} = \{2\cos(2\pi k/7) : k = 0, 1, \ldots, 6\}$, these are 7 real numbers (well, $2\cos(2\pi \cdot 0/7) = 2$, $2\cos(2\pi/7)$, etc., all distinct). $T$ acts on these as $k \mapsto 2k \pmod 7$. The order of 2 mod 7 is 3 (since $2^1=2, 2^2=4, 2^3=1 \pmod 7$). So $T$ has order 3 on this set. But we need order $\geq 4$ for 10 elements. If we only have 7 elements, order $\geq 3$ suffices ($2^3 = 8 \geq 7$).

But we have 10 elements total. If $T$ has order 3 on the 7 real elements and some order on the 3 non-real elements, the overall order is lcm of the two. For the overall order to be $\geq 4$, we need the non-real part to have order $\geq 4$ (or the lcm to be $\geq 4$).

Hmm, but with 3 non-real elements, the maximum order of a permutation is 3 (a 3-cycle). So the order on non-real elements is at most 3. Then the overall order is lcm(order_real, order_nonreal) = lcm(3, ≤3) ≤ 3 < 4. This violates the constraint!

Wait, this means that if $f$ has real coefficients and permutes 7 real + 3 non-real elements, with order 3 on the real part and order ≤ 3 on the non-real part, the overall order is ≤ 3, but we need order ≥ 4. Contradiction!

So for a real-coefficient quadratic, the order on the 7 real elements must be such that lcm(order_real, order_nonreal) ≥ 4. Since order_nonreal ≤ 3 (only 3 elements), we need order_real ≥ 4.

For 7 real elements with a real quadratic, order ≥ 4 means $2^d \geq 7$ gives $d \geq 3$, but we need $d \geq 4$ from the overall constraint. Actually wait, the constraint is on the overall order. Let me re-examine.

The constraint $2^d \geq 10$ where $d$ is the order of $f$ on all of $S$. If $f$ has order $d_{\text{real}}$ on the 7 real elements and $d_{\text{nonreal}}$ on the 3 non-real elements, then $d = \text{lcm}(d_{\text{real}}, d_{\text{nonreal}})$, and we need $2^d \geq 10$, i.e., $d \geq 4$.

So $\text{lcm}(d_{\text{real}}, d_{\text{nonreal}}) \geq 4$.

Since $d_{\text{nonreal}} \leq 3$ (permutation of 3 elements), we need $d_{\text{real}} \geq 4$.

For 7 real elements, $d_{\text{real}} \geq 4$ and $2^{d_{\text{real}}} \geq 7$ (automatically satisfied for $d_{\text{real}} \geq 4$ since $2^4 = 16 \geq 7$).

Also, the cycle structure on 7 elements with order $\geq 4$: fixed points $\leq 2$, elements in cycles of length $\leq 2$ is $\leq 4$ (from $2^2 = 4$).

Partitions of 7 with order $\geq 4$ and the constraints:
- (7): order 7 ≥ 4. ✓
- (6,1): order 6 ≥ 4. $c_1=1 \leq 2$. ✓
- (5,2): order 10 ≥ 4. $c_2=1$, $c_1+2c_2=2 \leq 4$. ✓
- (5,1,1): order 5 ≥ 4. $c_1=2 \leq 2$. ✓
- (4,3): order 12 ≥ 4. ✓
- (4,2,1): order 4 ≥ 4. $c_1=1, c_2=1$, $c_1+2c_2=3 \leq 4$. ✓
- (4,1,1,1): $c_1=3 > 2$. ✗
- (3,3,1): order 3 < 4. ✗
- (3,2,2): order 6 ≥ 4. $c_2=2$, $c_1+2c_2=4 \leq 4$. ✓
- (3,2,1,1): order 6 ≥ 4. $c_1=2, c_2=1$, $c_1+2c_2=4 \leq 4$. ✓
- (3,1,1,1,1): ✗
- (2,2,2,1): order 2 < 4. ✗
- (2,2,1,1,1): ✗
- etc.

Valid cycle types for 7 real elements: (7), (6,1), (5,2), (5,1,1), (4,3), (4,2,1), (3,2,2), (3,2,1,1).

And for 3 non-real elements with real coefficients: the permutation must respect conjugation. If the 3 non-real elements are $z_1, z_2, z_3$, and some of their conjugates are also in $S$... 

Actually, the 3 non-real elements don't have to be closed under conjugation. But if $f$ has real coefficients, $f(\bar{z}) = \overline{f(z)}$. So if $z \in S$ is non-real and $\bar{z} \in S$, then $f$ maps the pair $\{z, \bar{z}\}$ to $\{f(z), \overline{f(z)}\}$. If $\bar{z} \notin S$, then $f(z)$ is some non-real element of $S$, and $\overline{f(z)} = f(\bar{z})$ which may or may not be in $S$.

The 3 non-real elements: either they form a conjugation-closed set (e.g., $\{z, \bar{z}, w\}$ where $w$ is non-real and $\bar{w} \notin S$, or $\{z, \bar{z}, w, \bar{w}\}$ but that's 4), or they don't.

With 3 non-real elements, the possibilities for conjugation structure:
1. All 3 are self-conjugate: impossible (self-conjugate = real).
2. One conjugate pair $\{z, \bar{z}\}$ and one element $w$ with $\bar{w} \notin S$.
3. No conjugate pairs: all 3 have conjugates outside $S$.

Wait, actually with 3 non-real elements, we can have:
- 1 conjugate pair + 1 unpaired: $\{z, \bar{z}, w\}$ where $\bar{w} \neq z, \bar{z}$ and $\bar{w} \notin S$.
- 0 conjugate pairs: $\{z_1, z_2, z_3\}$ where no $\bar{z}_i$ is in $S$.
- We can't have 1.5 conjugate pairs (3 is odd).

Case 2 (1 conjugate pair): $f$ with real coefficients must map $\{z, \bar{z}\}$ to a conjugate pair in $S$. The only conjugate pair in the non-real part is $\{z, \bar{z}\}$ itself. So $f$ maps $\{z, \bar{z}\}$ to $\{z, \bar{z}\}$ (either $f(z) = z, f(\bar{z}) = \bar{z}$ or $f(z) = \bar{z}, f(\bar{z}) = z$). And $f(w) = w$ (since $w$ is the only remaining non-real element, and $f$ maps non-reals to non-reals). So $w$ is a fixed point.

If $f(z) = z, f(\bar{z}) = \bar{z}$: both $z, \bar{z}$ are fixed. So on non-real elements, $f$ is the identity.
If $f(z) = \bar{z}, f(\bar{z}) = z$: $z, \bar{z}$ form a 2-cycle, $w$ is fixed.

Case 3 (0 conjugate pairs): $f$ maps non-real elements to non-real elements, and conjugation doesn't constrain the permutation (since no conjugate of a non-real element is in $S$). So $f$ can be any permutation of the 3 non-real elements, as long as it's consistent with being a real quadratic.

Wait, but $f$ has real coefficients, so $f(\bar{z_i}) = \overline{f(z_i)}$. Since $\bar{z_i} \notin S$, this doesn't directly constrain the permutation on $S$. But it does mean that $f$ maps $\bar{z_i}$ to $\overline{f(z_i)}$, which is the conjugate of some element of $S$ (since $f(z_i) \in S$). So $\overline{f(z_i)}$ is the conjugate of a non-real element of $S$, which is also non-real and not in $S$ (by assumption). So this is consistent.

OK so in Case 3, the permutation on the 3 non-real elements can be anything (subject to the quadratic constraint).

This is getting very involved. Let me try to think about the problem from a higher level and maybe look for patterns.

Let me consider the possibility that the answer is related to a specific number. Competition problems like this often have answers that are small integers.

Let me think about upper bounds more carefully.

Upper bound via interpolation: A quadratic polynomial is determined by 3 points. If $f$ permutes $S$, then $f$ is determined by $(f(s_1), f(s_2), f(s_3))$ for any 3 distinct $s_1, s_2, s_3 \in S$. The number of possible triples is $10 \cdot 9 \cdot 8 = 720$ (ordered), but many of these won't extend to a valid permutation. The actual number of quadratic polynomial permutations is at most the number of permutations of $S$ consistent with a quadratic, which is at most... well, it's hard to bound this way.

Let me try another approach. Let me think about the problem in terms of the functional equation.

If $f$ is a quadratic polynomial permuting $S$, and $g$ is another quadratic polynomial permuting $S$, then $f$ and $g$ are both permutations of $S$. The composition $g \circ f^{-1}$ is a permutation of $S$ (but $f^{-1}$ is not a polynomial in general).

However, $g \circ f$ is a degree-4 polynomial permuting $S$. And $f \circ g$ is also a degree-4 polynomial permuting $S$. If $f$ and $g$ commute ($f \circ g = g \circ f$), then they generate a cyclic group (if one is a power of the other) or a more complex abelian group.

For quadratic polynomials, commutativity is quite restrictive. Two quadratic polynomials $f(z) = az^2 + bz + c$ and $g(z) = dz^2 + ez + f$ commute (as polynomials, i.e., $f(g(z)) = g(f(z))$ for all $z$) only in very special cases. By a classical result, two polynomials commute iff they share a common iterate, or they are both iterates of a common polynomial, or they are both Chebyshev-like or both monomial-like.

But we don't need $f$ and $g$ to commute as polynomials; we just need them to both permute $S$.

Let me try to think about specific examples.

Example: Let $S = \{0, 1, -1, 2, -2, 3, -3\} \cup \{i, -i, 2i\}$. Can we find quadratic polynomials permuting this?

$f(z) = -z$ is linear, not quadratic. $f(z) = z^2$ maps $0 \to 0, 1 \to 1, -1 \to 1$ (not injective). So $z^2$ doesn't work.

Let me think about Chebyshev maps more carefully.

$T(z) = z^2 - 2$. $T(2) = 2, T(0) = -2, T(-2) = 2$. So $T$ maps $2 \to 2, 0 \to -2, -2 \to 2$. Not injective on $\{0, 2, -2\}$ (both $0$ and $-2$ map to $-2$... wait, $T(0) = -2$ and $T(-2) = 2$. So $0 \to -2 \to 2 \to 2$. So $2$ is a fixed point and $0 \to -2 \to 2$. Not a permutation of $\{0, 2, -2\}$.

Let me use the Chebyshev representation. $T(2\cos\theta) = 2\cos(2\theta)$. For $S = \{2\cos(2\pi k/n) : k = 0, \ldots, n-1\}$, $T$ acts as $k \mapsto 2k \pmod n$.

For $n = 7$: $S = \{2\cos(2\pi k/7) : k = 0, 1, \ldots, 6\} = \{2, 2\cos(2\pi/7), 2\cos(4\pi/7), 2\cos(6\pi/7), 2\cos(8\pi/7), 2\cos(10\pi/7), 2\cos(12\pi/7)\}$. 

Note that $2\cos(2\pi k/7) = 2\cos(2\pi(7-k)/7)$, so actually $S$ has only $\lceil 7/2 \rceil + 1 = 4$ distinct values: $\{2, 2\cos(2\pi/7), 2\cos(4\pi/7), 2\cos(6\pi/7)\}$. That's only 4 distinct real numbers, not 7.

Hmm, so the Chebyshev approach with $n=7$ gives only 4 distinct values. I need 7 distinct real numbers.

For $n$ points to give $n$ distinct values of $2\cos(2\pi k/n)$, we need $k$ and $n-k$ to give different values, which happens only when $k = 0$ or $k = n/2$ (if $n$ is even). So for odd $n$, we get $(n+1)/2$ distinct values, and for even $n$, we get $n/2 + 1$ distinct values.

To get 7 distinct real values, we need $n$ such that $(n+1)/2 \geq 7$ (odd $n$), so $n \geq 13$, or $n/2 + 1 \geq 7$ (even $n$), so $n \geq 12$.

With $n = 13$: $S = \{2\cos(2\pi k/13) : k = 0, 1, \ldots, 12\}$, which has 7 distinct values. $T$ acts as $k \mapsto 2k \pmod{13}$. The order of 2 mod 13 is 12 (since 2 is a primitive root mod 13). So $T$ has order 12 on this set. But wait, the 7 distinct values correspond to orbits under $k \mapsto -k \pmod{13}$ (since $\cos(2\pi k/13) = \cos(2\pi(13-k)/13)$). The map $T$ on the 7 distinct values corresponds to $k \mapsto 2k \pmod{13}$ followed by identifying $k$ with $-k$. So the action on the 7 values is $[k] \mapsto [2k]$ where $[k] = \{k, -k\} \pmod{13}$.

The order of this action: we need $[2^d k] = [k]$, i.e., $2^d k \equiv \pm k \pmod{13}$, i.e., $2^d \equiv \pm 1 \pmod{13}$. $2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 16 \equiv 3, 2^5 = 6, 2^6 = 12 \equiv -1 \pmod{13}$. So $2^6 \equiv -1$, meaning the order of the action on the 7 values is 6. (Since $[2^6 k] = [-k] = [k]$.)

So $T$ has order 6 on the 7 real values. That's $\geq 4$, good.

Now, what about the non-real part? We need 3 non-real elements that are also permuted by $T(z) = z^2 - 2$. 

$T$ has fixed points at $z = 2$ and $z = -1$ (solutions of $z^2 - 2 = z$). The 7 real values include $2$ (which is a fixed point) and $-1$ (which is $2\cos(2\pi \cdot 3/13)$... let me check: $2\cos(6\pi/13) \approx 2 \times 0.568 \approx 1.137$, not $-1$. Hmm.)

Actually, $-1$ is a fixed point of $T$, but is $-1$ in our set $S$? $S = \{2\cos(2\pi k/13) : k = 0, \ldots, 6\}$ (taking one representative from each pair). $2\cos(2\pi/13) \approx 1.77$, $2\cos(4\pi/13) \approx 1.14$, $2\cos(6\pi/13) \approx 0.23$, $2\cos(8\pi/13) \approx -0.71$, $2\cos(10\pi/13) \approx -1.37$, $2\cos(12\pi/13) \approx -1.95$. And $2\cos(0) = 2$. So $-1$ is not in $S$.

OK so the fixed points of $T$ (namely $2$ and $-1$) — only $2$ is in $S$. So $T$ has 1 fixed point in $S$ (the value $2$), and the other 6 real values form cycles under $T$.

The cycle structure of $T$ on the 7 real values: $[0] \mapsto [0]$ (fixed, since $2 \cdot 0 = 0$), and then $[1] \mapsto [2] \mapsto [4] \mapsto [8] = [8] = [-5] = [5] \mapsto [10] = [10] = [-3] = [3] \mapsto [6] \mapsto [12] = [-1] = [1]$. So the cycle is $[1] \to [2] \to [4] \to [5] \to [3] \to [6] \to [1]$, a 6-cycle. So the cycle structure is $(6, 1)$: one 6-cycle and one fixed point.

Now for the non-real part: we need 3 non-real numbers that are permuted by $T(z) = z^2 - 2$. These would be periodic points of $T$ that are non-real.

The periodic points of $T$ of period dividing $d$ are the roots of $T^d(z) = z$, which has degree $2^d$. For $d = 6$ (the order of $T$ on the real part), $T^6(z) - z$ has degree $64$ and 64 roots. The 7 real values are among these roots. The remaining 57 roots are non-real (or real but not in $S$).

We need to find 3 non-real roots of $T^6(z) - z$ that form a single orbit under $T$ (or multiple orbits whose cycle lengths have lcm dividing 6, and the overall order of $T$ on all 10 elements is lcm(6, order on non-real) which should be $\geq 4$, automatically satisfied).

The non-real periodic points of $T$ of period dividing 6: we need to find orbits of $T$ among the non-real roots of $T^6(z) - z$. The cycle lengths must divide 6, so possible lengths are 1, 2, 3, 6. But fixed points of $T$ are $2$ and $-1$ (both real), so no non-real fixed points. 2-cycles: $T(z) = w, T(w) = z$, i.e., $T^2(z) = z$ but $T(z) \neq z$. $T^2(z) - z = (z^2-2)^2 - 2 - z = z^4 - 4z^2 + 2 - z$. This has degree 4, and the roots include the 2 fixed points (2 and -1), so there are 2 more roots, which are the 2-cycle. Let me find them: $z^4 - 4z^2 - z + 2 = (z-2)(z+1)(z^2+z-1)$. The roots of $z^2 + z - 1 = 0$ are $z = (-1 \pm \sqrt{5})/2$, which are real. So the 2-cycle is real. No non-real 2-cycles.

3-cycles: $T^3(z) = z$ but $T(z) \neq z$ and $T^2(z) \neq z$. $T^3(z) - z$ has degree 8. The roots include fixed points (2 roots) and 2-cycle (2 roots), so 4 roots form 3-cycles, giving one 3-cycle (with 3 elements) and... wait, 4 roots can't form a 3-cycle (which needs 3 elements). Let me recompute.

$T^3(z) - z$ has degree 8. Roots: 2 fixed points + 2 elements in 2-cycle + remaining 4 elements. The remaining 4 elements: if they form 3-cycles, we'd need 3 or 6 elements, but we have 4. So they must form something else. Actually, the 4 remaining elements could form a 4-cycle (but 4 doesn't divide 3, contradiction since they're roots of $T^3(z) = z$). Wait, the period must divide 3, so periods are 1 or 3. We have 2 fixed points (period 1) and 2 period-2 elements. But period-2 elements are NOT roots of $T^3(z) = z$ unless their period also divides 3, which it doesn't (2 doesn't divide 3). 

Hmm, I think I'm confusing myself. $T^3(z) = z$ means the period divides 3, so periods 1 or 3. The fixed points (period 1) are roots. The 2-cycle elements have period 2, which doesn't divide 3, so they're NOT roots of $T^3(z) = z$. So $T^3(z) - z$ has 8 roots: 2 fixed points + 6 elements in 3-cycles (two 3-cycles). 

So there are two 3-cycles of $T$, with 6 elements total. Are any of these non-real? The 3-cycles are roots of $(T^3(z) - z) / (T(z) - z)$, which is a degree-6 polynomial. Let me think about whether these are real or complex.

Actually, $T^3(z) - z$ factors as $(z^2 - z - 2) \cdot Q_6(z)$ where $Q_6$ is degree 6 and contains the 3-cycle elements. The fixed points are roots of $z^2 - z - 2 = (z-2)(z+1)$.

For the Chebyshev map $T(z) = z^2 - 2$, the periodic points are $2\cos(2\pi k / (2^d - 1))$ and $2\cos(2\pi k / (2^d + 1))$ for various $d$. These are all real! So all periodic points of $T(z) = z^2 - 2$ are real.

This makes sense because $T$ maps $[-2, 2]$ to $[-2, 2]$ (via the Chebyshev correspondence), and the Julia set of $T$ is the interval $[-2, 2]$. All periodic points are in $[-2, 2]$ and hence real.

So $T(z) = z^2 - 2$ has no non-real periodic points. This means we can't use $T$ to permute a set with non-real elements.

I need a different quadratic map that has non-real periodic points.

Let me consider $f(z) = z^2 + c$ for various $c$. For $c > -2$ (approximately), the Julia set is a fractal and there are non-real periodic points. For $c = -2$, it's the Chebyshev case with all real periodic points. For $c = 0$, $f(z) = z^2$, and the periodic points are roots of unity (on the unit circle, mostly non-real).

$f(z) = z^2$: periodic points of period dividing $d$ are roots of $z^{2^d} = z$, i.e., $z^{2^d - 1} = 1$ or $z = 0$. So the periodic points are $0$ (fixed) and the $(2^d - 1)$th roots of unity.

For $f(z) = z^2$ to permute a set $S$, $S$ must consist of periodic points of $f$. The real periodic points are $0, 1, -1$ (for various periods: $0$ is fixed, $1$ is fixed, $-1$ has period 2). Actually, $-1 \to 1 \to 1$, so $-1$ is not periodic (it's preperiodic). The real periodic points of $z^2$ are just $0$ and $1$ (both fixed). That's only 2 real periodic points, not enough for 7.

So $z^2$ doesn't work either.

Let me think about this differently. We need a quadratic polynomial with at least 7 real periodic points and at least 3 non-real periodic points, all of which are in a single set $S$ that's permuted by $f$.

For $T(z) = z^2 - 2$, all periodic points are real (in $[-2, 2]$). For $f(z) = z^2 + c$ with $c > 1/4$, there are no real periodic points (the real dynamics escape). For $-2 \leq c \leq 1/4$, there are real periodic points.

For $c$ slightly greater than $-2$, the map $z^2 + c$ has a Julia set that's a perturbation of $[-2, 2]$, and there are non-real periodic points near the real axis.

But the key question is: can we find a quadratic with both many real and some non-real periodic points, forming a set invariant under the quadratic?

Actually, I realize we don't need all elements of $S$ to be periodic points of a single quadratic. We need to find $S$ such that multiple quadratics permute $S$. Each quadratic might have different periodic structures.

Let me reconsider the problem. We want to maximize the number of quadratic polynomials $f$ with $f(S) = S$. We choose $S$ optimally.

Let me think about what kinds of sets $S$ can be invariant under multiple quadratic polynomials.

If $f$ and $g$ are both quadratic polynomials permuting $S$, then $f \circ g$ and $g \circ f$ are degree-4 polynomials permuting $S$. If $f \circ g = g \circ f$ (they commute as polynomials), then by Ritt's theorem, they must be related in a specific way (both iterates of a common polynomial, or both Chebyshev, or both monomial-type).

But they don't need to commute as polynomials; they just need to both permute $S$.

Let me think about the problem from the answer perspective. This is likely from a math competition (maybe Putnam or USAMO or similar). Let me think about what the answer might be.

Actually, let me reconsider. The problem says "maximum possible number of quadratic polynomials $f(z)$ with complex coefficients such that $f(S) = S$". 

Let me think about affine maps first. An affine map $f(z) = az + b$ permuting $S$ is a symmetry of $S$. The number of affine symmetries can be large (e.g., if $S$ is a regular polygon, the dihedral group). But we're looking at quadratic polynomials, not affine.

A quadratic polynomial $f(z) = az^2 + bz + c$ with $a \neq 0$. This is a degree-2 map.

Let me think about the constraint more carefully. If $f$ permutes $S$ (10 elements), then $f$ is a bijection on $S$. The equation $f(z) = w$ has at most 2 solutions, so each $w \in S$ has at most 2 preimages in $\mathbb{C}$, and exactly 1 in $S$.

Now, consider two quadratic polynomials $f, g$ permuting $S$. The polynomial $f - g$ has degree at most 2, so $f(z) = g(z)$ has at most 2 solutions. So $f$ and $g$ agree on at most 2 elements of $S$.

This means: if we have $m$ quadratic polynomials permuting $S$, any two agree on at most 2 elements.

Now, consider the $m$ polynomials as permutations of $S$. Each permutation $\sigma_i$ is determined by any 3 of its values (since the quadratic is determined by 3 points). Two permutations agree on at most 2 positions.

This is related to the theory of permutation codes or mutually orthogonal structures.

Let me think about this combinatorially. We have $m$ permutations of $\{1, \ldots, 10\}$, any two agreeing in at most 2 positions. What's the maximum $m$?

This is a well-studied problem in combinatorics: permutations with limited agreement. The maximum number of permutations of $n$ elements with pairwise agreement at most $t$ is related to the concept of "permutation arrays" or "permutation codes."

For $n = 10$ and $t = 2$ (at most 2 agreements), the maximum number of permutations is... I don't remember the exact value, but it can be quite large. However, not all such permutations can be realized as quadratic polynomials.

The key additional constraint is that the permutation must be realizable as a quadratic polynomial on the specific set $S$. A quadratic polynomial is determined by 3 parameters, so the space of quadratic polynomials is 3-dimensional (over $\mathbb{C}$). The condition $f(S) = S$ is a strong constraint.

Let me think about it this way: a quadratic polynomial $f(z) = az^2 + bz + c$ is determined by $(a, b, c) \in \mathbb{C}^3$ with $a \neq 0$. The condition $f(S) \subseteq S$ means $f(s_i) \in S$ for each $i$, which gives 10 constraints (each $f(s_i)$ must be one of the 10 elements of $S$). But since $f$ is determined by 3 values, if we specify $f(s_1), f(s_2), f(s_3)$, then $f$ is determined, and we need $f(s_i) \in S$ for $i = 4, \ldots, 10$ as well.

So the number of quadratic polynomials permuting $S$ equals the number of triples $(f(s_1), f(s_2), f(s_3)) \in S^3$ (with $f(s_i)$ distinct, since $f$ is a bijection) such that the resulting quadratic maps all of $S$ into $S$.

The number of such triples is at most $10 \cdot 9 \cdot 8 = 720$, but the actual number is much smaller due to the constraints.

Let me try to think about this problem more carefully with a specific approach.

Approach: Consider the "permutation polynomial" aspect. A quadratic polynomial $f$ permuting $S$ is a permutation polynomial on $S$. The set of all permutation polynomials on $S$ (of any degree) forms a group under composition. The quadratic ones are specific elements.

For a set of $n$ points, the group of permutation polynomials can be at most the symmetric group $S_n$ (if every permutation is a polynomial), but this requires degree up to $n-1$. For quadratics, we're much more restricted.

Let me try to think about the problem by considering the real and complex parts separately and then combining.

Let me consider the following strategy: find $S$ with 7 real and 3 non-real elements such that many quadratics permute $S$.

Strategy 1: Use real quadratics only. A real quadratic permutes the 7 real elements and the 3 non-real elements separately. We need to find a set of 7 real numbers with many real quadratic symmetries, and a set of 3 non-real numbers with compatible real quadratic symmetries.

For 7 real numbers: how many real quadratics can permute a set of 7 real numbers? A real quadratic $f(x) = ax^2 + bx + c$ ($a \neq 0$, $a, b, c \in \mathbb{R}$) permuting a set of 7 real numbers. The cycle structure must have order $\geq 3$ (since $2^d \geq 7$ requires $d \geq 3$). 

Actually, for the overall problem with 10 elements, we need order $\geq 4$. So the real quadratic must have order $\geq 4$ on the 7 real elements (since the non-real part has at most 3 elements, order $\leq 3$, and lcm must be $\geq 4$).

How many real quadratics can permute 7 real numbers with order $\geq 4$?

A real quadratic is determined by 3 real parameters. The condition that it permutes 7 specific real numbers is very restrictive. Given 7 real numbers, how many real quadratics permute them?

If $f$ is a real quadratic permuting $\{x_1, \ldots, x_7\}$, then $f$ is determined by $(f(x_1), f(x_2), f(x_3))$, and we need $f(x_i) \in \{x_1, \ldots, x_7\}$ for all $i$, with $f$ being a bijection.

The number of real quadratics permuting 7 real numbers is at most the number of permutations of 7 elements that can be realized as a real quadratic, which is at most $7 \cdot 6 \cdot 5 = 210$ (choices of 3 images) but actually much less.

Let me think about specific examples.

For the Chebyshev map $T(x) = x^2 - 2$ on $S_7 = \{2\cos(2\pi k/13) : k = 0, \ldots, 6\}$ (7 distinct real values), $T$ permutes $S_7$ with cycle type $(6, 1)$. Are there other real quadratics permuting $S_7$?

The powers of $T$ that are quadratic: only $T$ itself ($T^2$ is degree 4, etc.). So $T$ gives one quadratic.

Are there other quadratics permuting $S_7$? Let me think... If $g$ is another real quadratic permuting $S_7$, then $g$ is a permutation of $S_7$ with order $\geq 3$ (for 7 elements). The cycle structure must be one of the valid types.

This is hard to determine without more specific computation. Let me think about the problem differently.

Let me consider the possibility that the answer is small, like 2, 3, 4, 5, or 6.

Actually, let me reconsider the problem. Maybe I should think about what sets $S$ can be invariant under multiple quadratics, and count more carefully.

Let me think about the group structure. If $f_1, \ldots, f_m$ are quadratic polynomials permuting $S$, consider the group $G$ generated by $f_1, \ldots, f_m$ under composition (as permutations of $S$). This is a subgroup of $S_{10}$. Each $f_i$ is an element of $G$ that happens to be a quadratic polynomial.

The group $G$ acts on $S$, and the quadratic polynomial elements of $G$ are what we're counting.

Now, $G$ is a transitive subgroup of $S_{10}$ (if $S$ is a single orbit) or might have multiple orbits. But since each $f_i$ permutes all of $S$, $G$ acts on $S$ but might not be transitive.

Actually, $G$ might not be transitive. For example, if all $f_i$ preserve the real/non-real split, then $G$ has two orbits: the 7 real and 3 non-real elements.

Let me consider the case where all quadratics have real coefficients. Then $G$ acts separately on the 7 real and 3 non-real elements. The quadratics are elements of $G$ that are quadratic polynomials.

For the 7 real elements, the quadratics induce permutations with specific cycle structures. For the 3 non-real elements, the quadratics induce permutations with specific cycle structures.

The number of quadratics is the number of elements of $G$ that are quadratic polynomials. This is at most $|G|$, but typically much less.

Hmm, I think I need to approach this more concretely. Let me try to construct specific examples and count.

Construction 1: Let $S = \{x_1, \ldots, x_7\} \cup \{z_1, z_2, z_3\}$ where $x_i$ are real and $z_j$ are non-real. Suppose $f(z) = z^2 + c$ (for some real $c$) permutes $S$. Then $f$ permutes the $x_i$ and the $z_j$ separately.

For the $x_i$: $f$ is a real quadratic permuting 7 real numbers. The cycle structure has order $\geq 4$ (as argued above). 

For the $z_j$: $f$ permutes 3 non-real numbers. Since $f$ has real coefficients, $f(\bar{z}) = \overline{f(z)}$. If the $z_j$ include a conjugate pair, say $z_1 = \bar{z_2}$, then $f(z_1) = \overline{f(z_2)}$, so $f$ maps the pair $\{z_1, z_2\}$ to a conjugate pair in $S$. The only conjugate pair among the non-real elements is $\{z_1, z_2\}$, so $f$ maps $\{z_1, z_2\}$ to itself. And $f(z_3) = z_3$ (since $z_3$ is the only remaining non-real element). So $z_3$ is a fixed point, and $\{z_1, z_2\}$ is either fixed or swapped.

If $z_3$ is a fixed point, then $f(z_3) = z_3$, so $z_3^2 + c = z_3$, meaning $c = z_3 - z_3^2$. But $c$ is real and $z_3$ is non-real, so $z_3 - z_3^2$ must be real. If $z_3 = a + bi$ ($b \neq 0$), then $z_3 - z_3^2 = (a + bi) - (a^2 - b^2 + 2abi) = (a - a^2 + b^2) + (b - 2ab)i$. For this to be real, $b(1 - 2a) = 0$, so $a = 1/2$ (since $b \neq 0$). So $z_3 = 1/2 + bi$ for some $b \neq 0$, and $c = 1/2 - (1/4 + b^2) = 1/4 - b^2$.

Then $z_1, z_2$ are a conjugate pair, and $f$ either fixes both or swaps them. If $f$ fixes both, $z_1^2 + c = z_1$ and $z_2^2 + c = z_2$, so both are roots of $z^2 - z + c = 0$, i.e., $z = (1 \pm \sqrt{1 - 4c})/2$. With $c = 1/4 - b^2$, $1 - 4c = 1 - 1 + 4b^2 = 4b^2$, so $z = (1 \pm 2b)/2 = 1/2 \pm b$. But these are real! Contradiction since $z_1, z_2$ are non-real.

So $f$ can't fix both $z_1$ and $z_2$ if they're a conjugate pair and $z_3$ is a fixed point (with $f(z) = z^2 + c$). So $f$ must swap $z_1$ and $z_2$: $f(z_1) = z_2, f(z_2) = z_1$. This means $z_1^2 + c = z_2 = \bar{z_1}$, so $z_1^2 + c = \bar{z_1}$, i.e., $z_1^2 - \bar{z_1} + c = 0$.

With $z_1 = a + bi$ and $c = 1/4 - b_3^2$ (where $z_3 = 1/2 + b_3 i$):
$z_1^2 - \bar{z_1} + c = (a^2 - b^2 + 2abi) - (a - bi) + (1/4 - b_3^2) = (a^2 - b^2 - a + 1/4 - b_3^2) + (2ab + b)i = 0$.

So: $2ab + b = 0 \Rightarrow b(2a + 1) = 0 \Rightarrow a = -1/2$ (since $b \neq 0$).
And: $a^2 - b^2 - a + 1/4 - b_3^2 = 0 \Rightarrow 1/4 - b^2 + 1/2 + 1/4 - b_3^2 = 0 \Rightarrow 1 - b^2 - b_3^2 = 0 \Rightarrow b^2 + b_3^2 = 1$.

So $z_1 = -1/2 + bi$, $z_2 = -1/2 - bi$, $z_3 = 1/2 + b_3 i$ with $b^2 + b_3^2 = 1$, $b, b_3 \neq 0$.

And $c = 1/4 - b_3^2 = 1/4 - (1 - b^2) = b^2 - 3/4$.

So $f(z) = z^2 + b^2 - 3/4$.

Now, $f$ also needs to permute the 7 real elements. The 7 real elements are periodic points of $f$ with appropriate cycle structure.

This gives one quadratic $f$. Can we find others?

If we use a different quadratic $g(z) = dz^2 + ez + h$ (with real coefficients) permuting the same $S$, then $g$ also permutes the 3 non-real elements. By the same argument, $g$ must fix $z_3$ and swap $z_1, z_2$ (or fix all three, but we showed fixing all three leads to a contradiction for the form $z^2 + c$; for a general quadratic, let me re-examine).

Actually, I was too specific. Let me consider general real quadratics $g(z) = \alpha z^2 + \beta z + \gamma$ permuting the 3 non-real elements $\{z_1, z_2, z_3\}$ where $z_1 = \bar{z_2}$ and $z_3$ has $\bar{z_3} \notin S$.

$g$ must map $\{z_1, z_2\}$ to itself (since it's the only conjugate pair) and fix $z_3$. So $g(z_3) = z_3$, meaning $\alpha z_3^2 + \beta z_3 + \gamma = z_3$.

And either $g(z_1) = z_1, g(z_2) = z_2$ (both fixed) or $g(z_1) = z_2, g(z_2) = z_1$ (swapped).

Case A: $g$ fixes all 3 non-real elements. Then $g(z) - z$ has roots $z_1, z_2, z_3$, so $g(z) - z = \alpha(z - z_1)(z - z_2)(z - z_3)/\alpha$... wait, $g(z) - z$ is a quadratic (degree 2 if $\alpha \neq 0$, or degree 1 if $\alpha = 0$). But it has 3 roots $z_1, z_2, z_3$, which is impossible for a degree-2 polynomial (unless $\alpha = 0$, making it degree 1, which can't have 3 roots either). 

Wait, $g(z) - z = \alpha z^2 + (\beta - 1)z + \gamma$, which is degree 2 (if $\alpha \neq 0$) and can have at most 2 roots. But we need 3 roots ($z_1, z_2, z_3$). Contradiction! So $g$ cannot fix all 3 non-real elements.

Case B: $g$ swaps $z_1, z_2$ and fixes $z_3$. Then $g(z_3) = z_3$ (1 root of $g(z) - z$) and $g(z_1) = z_2 \neq z_1$, $g(z_2) = z_1 \neq z_2$. So $g(z) - z$ has exactly 1 root among the non-real elements ($z_3$). The other root of $g(z) - z$ is some other value (possibly real or non-real, but not in $\{z_1, z_2\}$).

So every real quadratic permuting $S$ must swap $z_1, z_2$ and fix $z_3$. This means all real quadratics permuting $S$ agree on the 3 non-real elements: $g(z_1) = z_2, g(z_2) = z_1, g(z_3) = z_3$.

Now, two quadratics that agree on 3 points are identical. So there is at most ONE real quadratic permuting $S$ (in this configuration where the non-real elements include one conjugate pair and one unpaired element).

Wait, that's a key insight! If all real quadratics permuting $S$ must agree on the 3 non-real elements (swap the pair, fix the unpaired one), then any two such quadratics agree on 3 points, hence are identical. So there's at most 1 real quadratic permuting $S$.

Hmm, but this is for the specific configuration where the 3 non-real elements include exactly one conjugate pair. What if the 3 non-real elements have no conjugate pairs (Case 3 from earlier)?

Case 3: No conjugate pairs among the 3 non-real elements. Then $\bar{z_i} \notin S$ for all $i$. A real quadratic $g$ permuting the 3 non-real elements can be any permutation (since conjugation doesn't constrain it). But $g$ has real coefficients, so $g(\bar{z_i}) = \overline{g(z_i)}$. Since $\bar{z_i} \notin S$, this doesn't directly constrain the permutation on $S$.

But wait, $g$ is a real quadratic, so $g(z) - z$ has real coefficients. Its roots are either real or come in conjugate pairs. The fixed points of $g$ among the non-real elements are roots of $g(z) - z$, so they come in conjugate pairs. Since no two non-real elements are conjugates, $g$ can have at most 0 non-real fixed points (a conjugate pair would require 2 non-real elements that are conjugates, but we have no such pair). Wait, actually $g(z) - z$ has degree 2 and real coefficients, so it has 0 or 2 non-real roots (conjugate pair) or 2 real roots. If it has a non-real conjugate pair as roots, those roots are $\bar{}$ of each other, but neither is in $S$ (since no conjugate pair is in $S$). So $g$ has 0 non-real fixed points in $S$.

So $g$ has no fixed points among the 3 non-real elements. The permutation of 3 elements with no fixed points is a 3-cycle. So $g$ acts as a 3-cycle on the non-real elements.

There are two 3-cycles on 3 elements: $(z_1 z_2 z_3)$ and $(z_1 z_3 z_2)$. So there are at most 2 possible actions on the non-real elements. But different quadratics with the same action on the non-real elements would agree on 3 points and hence be identical. So there are at most 2 real quadratics permuting $S$ (one for each 3-cycle).

Wait, but we also need the quadratic to permute the 7 real elements. So the 2 quadratics (corresponding to the two 3-cycles) must also permute the 7 real elements. This might not be possible simultaneously.

Hmm, let me reconsider. If $g_1$ and $g_2$ are two real quadratics permuting $S$, with $g_1$ acting as $(z_1 z_2 z_3)$ and $g_2$ acting as $(z_1 z_3 z_2)$ on the non-real elements, then $g_1$ and $g_2$ agree on 0 of the 3 non-real elements. They could differ on the real elements too. But $g_1$ and $g_2$ are both quadratics, so they agree on at most 2 points total. Since they disagree on all 3 non-real elements, they can agree on at most $2 - 0 = 2$... wait, they already disagree on 3 points, but two quadratics can disagree on all points. The constraint is they agree on at most 2 points, which is satisfied (they agree on 0 non-real points, and could agree on 0, 1, or 2 real points).

So in Case 3, we could have up to 2 real quadratics. But can we actually achieve 2?

Let me think about this. We need two real quadratics $g_1, g_2$ such that:
- Both permute the same 7 real numbers.
- $g_1$ acts as $(z_1 z_2 z_3)$ and $g_2$ acts as $(z_1 z_3 z_2)$ on the 3 non-real numbers.
- The overall order of each $g_i$ on $S$ is $\geq 4$.

For the order: $g_1$ has a 3-cycle on non-real elements, so the order on non-real elements is 3. The order on real elements must be such that lcm(order_real, 3) $\geq 4$, so order_real $\geq 4$. Similarly for $g_2$.

This is getting very involved. Let me step back and think about whether non-real coefficient quadratics could contribute more.

Non-real coefficient quadratics: $f(z) = az^2 + bz + c$ with at least one of $a, b, c$ non-real. Such $f$ can map real elements to non-real elements and vice versa.

If $f$ maps some real element to a non-real element, then $f$ mixes the real and non-real parts. The constraint is that $f$ permutes all 10 elements.

Let me think about how many elements can be "mixed." If $f$ maps $k$ real elements to non-real elements, then $f$ maps $k$ non-real elements to real elements (to maintain the bijection). So $k$ real elements go to non-real, $k$ non-real elements go to real, $7 - k$ real elements stay real, $3 - k$ non-real elements stay non-real. We need $k \leq 3$ (only 3 non-real elements).

For $k = 0$: $f$ preserves the real/non-real split. This is the case of real coefficients (well, not necessarily—$f$ could have non-real coefficients but still map reals to reals, but that's very special). Actually, if $f$ maps all 7 real elements to real numbers, then $f(x) \in \mathbb{R}$ for 7 real values $x$. A quadratic $f(z) = az^2 + bz + c$ with $f(x) \in \mathbb{R}$ for 7 real $x$... if $a = a_1 + a_2 i$, then $f(x) = a_1 x^2 + b_1 x + c_1 + i(a_2 x^2 + b_2 x + c_2)$. For $f(x) \in \mathbb{R}$, we need $a_2 x^2 + b_2 x + c_2 = 0$ for 7 values of $x$. But a quadratic in $x$ has at most 2 real roots, so $a_2 = b_2 = c_2 = 0$, meaning $a, b, c$ are all real. So $k = 0$ implies real coefficients.

For $k \geq 1$: $f$ has non-real coefficients and mixes real and non-real elements.

Let me think about $k = 3$: all 3 non-real elements map to real elements, and 3 real elements map to non-real elements. So $f$ maps 3 real → non-real, 4 real → real, 3 non-real → real, 0 non-real → non-real. So the 3 non-real elements all map to real elements, and 3 of the 7 real elements map to non-real elements.

In this case, the 3 non-real elements of $S$ are mapped to 3 of the 7 real elements, and 3 of the 7 real elements are mapped to the 3 non-real elements. The remaining 4 real elements map to the remaining 4 real elements.

This is a valid permutation structure. The question is whether such a quadratic exists and how many can exist.

Let me think about the constraint on fixed points. $f(z) = z$ has at most 2 solutions. The fixed points could be real or non-real.

OK, I think I need to approach this problem more systematically. Let me think about the maximum number of quadratic polynomial permutations of a 10-element set (without the real/non-real constraint first), and then see how the constraint affects things.

Actually, let me reconsider. The problem is asking for the maximum over all valid $S$. So we need to find the best $S$.

Let me think about the problem from the perspective of the answer. I suspect the answer might be around 3-6.

Let me try to think about upper bounds.

Upper bound argument: 

Each quadratic polynomial permuting $S$ is a permutation of $S$ with order $\geq 4$. Two such quadratics agree on at most 2 elements of $S$.

Consider the $m$ quadratics as permutations $\sigma_1, \ldots, \sigma_m$ of $S = \{1, \ldots, 10\}$. Each $\sigma_i$ has order $\geq 4$, and any two agree in at most 2 positions.

Now, additionally, each $\sigma_i$ must be realizable as a quadratic polynomial on the specific complex numbers in $S$. This is a very strong constraint.

Let me think about the problem differently. Let me consider the "interpolation" approach.

A quadratic $f$ is determined by $f(s_1), f(s_2), f(s_3)$ for any 3 distinct $s_1, s_2, s_3 \in S$. So the number of quadratics permuting $S$ is the number of ordered triples $(v_1, v_2, v_3) \in S^3$ (distinct) such that the interpolating quadratic maps all of $S$ into $S$ bijectively.

The interpolating quadratic for $f(s_i) = v_i$ is:
$f(z) = \sum_{i=1}^{3} v_i \prod_{j \neq i} \frac{z - s_j}{s_i - s_j}$

This is a polynomial of degree $\leq 2$ in $z$ (Lagrange interpolation). For it to be a quadratic (degree exactly 2), we need the leading coefficient to be non-zero.

The condition $f(S) = S$ means $f(s_k) \in S$ for all $k = 1, \ldots, 10$ and $f$ is a bijection on $S$.

This is a system of constraints that's hard to analyze in general.

Let me try a completely different approach. Let me think about the problem using the theory of polynomial automorphisms of finite sets.

A key theorem: If $f$ is a polynomial of degree $d$ permuting a finite set $S$ of $n$ points, then the cycle lengths of $f$ on $S$ divide the order of $f$ as a permutation, and this order $d_{\text{perm}}$ satisfies $d^{d_{\text{perm}}} \geq n$ (since $f^{d_{\text{perm}}}(z) - z$ has degree $d^{d_{\text{perm}}}$ and at least $n$ roots).

For $d = 2, n = 10$: $2^{d_{\text{perm}}} \geq 10$, so $d_{\text{perm}} \geq 4$.

Now, let me think about the structure of the set of quadratic permutations.

Key observation: If $f$ and $g$ are quadratic polynomials permuting $S$, and $f \neq g$, then $f - g$ is a polynomial of degree $\leq 2$ with at most 2 roots. So $f$ and $g$ agree on at most 2 elements of $S$.

Now, consider 3 distinct quadratics $f, g, h$ permuting $S$. Each pair agrees on at most 2 elements. 

Let me think about the "permutation matrix" approach. For each quadratic $f_i$, define the permutation matrix $P_i$ where $(P_i)_{jk} = 1$ if $f_i(s_j) = s_k$. The condition that two quadratics agree on at most 2 elements means $P_i \cdot P_j^T$ has at most 2 ones on the diagonal (i.e., $\text{tr}(P_i P_j^T) \leq 2$).

This is related to the theory of permutation codes with Hamming distance. The Hamming distance between $\sigma_i$ and $\sigma_j$ is $10 - |\{k : \sigma_i(k) = \sigma_j(k)\}| \geq 10 - 2 = 8$.

So we need a set of permutations of 10 elements with pairwise Hamming distance $\geq 8$, and each permutation must be realizable as a quadratic polynomial on $S$.

The maximum size of a permutation code of length 10 with minimum distance 8 is known in coding theory. But the additional constraint of being a quadratic polynomial is much more restrictive.

Let me try yet another approach. Let me think about the problem using the concept of "functional graphs" and "polynomial symmetries."

If $f$ is a quadratic permuting $S$, the functional graph of $f$ on $S$ is a union of cycles (since $f$ is a bijection). The cycle structure is constrained as above.

Now, here's a key idea: if $f$ and $g$ are both quadratics permuting $S$, consider $h = g \circ f^{-1}$ as a permutation of $S$. This is a permutation of $S$ but not necessarily a polynomial. However, $h$ maps $S$ to $S$, and $h = g \circ f^{-1}$ where $f^{-1}$ is the inverse permutation (not polynomial).

Alternatively, $g \circ f$ is a degree-4 polynomial permuting $S$. The set of all polynomial permutations of $S$ (of any degree) forms a group $G$ under composition. The quadratic elements of $G$ are what we're counting.

The group $G$ is a subgroup of $S_{10}$. The quadratic elements are specific elements of $G$.

Now, $G$ is the group of polynomial automorphisms of $S$. For a generic set $S$ of 10 points, $G$ is trivial (only the identity, which is degree 0/1). For special sets, $G$ can be larger.

The question is: what's the maximum number of degree-2 elements in $G$, over all sets $S$ with 7 real and 3 non-real elements?

Let me think about what groups $G$ can arise. $G$ is a subgroup of $S_{10}$ that acts as polynomial automorphisms. The elements of $G$ have specific degrees (as polynomials), and the degree-2 elements are what we want.

For a set of $n$ points, the group of polynomial automorphisms can be at most the symmetric group $S_n$ (if every permutation is a polynomial), but this requires degree up to $n-1$. For quadratics, we're much more restricted.

Let me think about specific groups.

If $G$ is cyclic of order $d$, generated by a quadratic $f$, then the quadratic elements of $G$ are just $\{f\}$ (since $f^k$ has degree $2^k$, which is 2 only for $k = 1$). So a cyclic group gives at most 1 quadratic.

If $G$ is larger, say $G = S_3$ (acting on 3 elements and fixing the other 7), then the degree-2 elements of $G$ are the transpositions and 3-cycles that can be realized as quadratics. But a transposition has order 2, and $2^2 = 4 < 10$, so a transposition can't be a quadratic permuting 10 elements (the order is too small). Similarly, a 3-cycle has order 3, and $2^3 = 8 < 10$, so it can't be a quadratic permuting 10 elements.

Wait, this is the key constraint: every quadratic permuting $S$ must have order $\geq 4$ as a permutation of $S$. So the quadratic elements of $G$ must have order $\geq 4$.

In $S_{10}$, the elements of order $\geq 4$ include: 4-cycles, 5-cycles, 6-cycles, 7-cycles, 8-cycles, 9-cycles, 10-cycles, and products like (4,2), (4,3), (5,2), (5,3), (5,4), (6,2), (6,3), (6,4), (6,5), (7,2), (7,3), etc.

But not all of these can be realized as quadratics (due to the cycle structure constraints from earlier).

Let me think about whether multiple quadratics can permute the same set.

Suppose $f$ and $g$ are quadratics permuting $S$, both of order $\geq 4$. Consider the group $H = \langle f, g \rangle$ (as permutations of $S$). This is a subgroup of $S_{10}$.

If $f$ and $g$ commute (as permutations), then $H$ is abelian. The order of $fg$ is lcm-related to the orders of $f$ and $g$. But $fg$ is a degree-4 polynomial, not quadratic.

If $f$ and $g$ don't commute, $H$ is non-abelian.

The number of quadratic elements in $H$ is what we want to maximize. Each quadratic element has order $\geq 4$ and specific cycle structure constraints.

This is still very abstract. Let me try to think about concrete constructions.

Construction attempt: Let me try to find $S$ with 2 quadratic polynomial permutations.

Let $f(z) = z^2 - 2$ (Chebyshev). As discussed, all periodic points of $f$ are real. So $f$ can only permute real sets. To include non-real elements, I need a different approach.

Let me try $f(z) = \omega z^2$ where $\omega$ is a primitive cube root of unity. Then $f$ maps $z
