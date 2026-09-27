# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Ten pairwise distinct non-zero real numbers $x_1, x_2, \dots, x_{10}$ are such that for any two distinct indices $i, j \in \{1, \dots, 10\}$, either their sum $x_i + x_j$ or their product $x_i x_j$ is a rational number. Let $S = \{x_1^2, x_2^2, \dots, x_{10}^2\}$. Determine the maximum possible number of irrational values in the set $S$.       — 题目文本
#   The original proof shows that for any such set of ten numbers, the squares of all numbers must be rational. This is proven by considering the relationship between numbers as edges in a graph and applying Ramsey's theorem to find a monochromatic triangle (either a set of three numbers where all pairwise sums are rational, or all pairwise products are rational). In the case of a rational sum triangle, it's shown that all numbers must be rational. In the case of a rational product triangle, it's shown that all squares must be rational. Therefore, all $x_i^2$ are rational, meaning the number of irrational values in $S$ must be 0.  — 标准解答
#   Let me analyze this problem carefully. We have 10 pairwise distinct non-zero real numbers $x_1, \ldots, x_{10}$ such that for any two distinct indices $i, j$, either $x_i + x_j$ or $x_i x_j$ is rational. We need to find the maximum number of irrational values in $S = \{x_1^2, \ldots, x_{10}^2\}$.

Let me think about this carefully.

First, let me understand the structure. For each pair $(i,j)$, at least one of $x_i + x_j$ or $x_i x_j$ is rational.

Let me categorize the $x_i$ values. Let's say $x_i$ is "rational" if $x_i \in \mathbb{Q}$, and "irrational" otherwise.

If $x_i$ and $x_j$ are both rational, then both $x_i + x_j$ and $x_i x_j$ are rational. Fine.

If $x_i$ is rational and $x_j$ is irrational: $x_i + x_j$ is irrational (since $x_j$ is irrational), so we need $x_i x_j$ to be rational. Since $x_i \neq 0$ is rational, $x_i x_j$ rational means $x_j$ is rational, contradiction. So actually, if $x_i$ is rational and $x_j$ is irrational, $x_i x_j$ is irrational, and $x_i + x_j$ is irrational. That's a problem!

Wait, let me reconsider. If $x_i$ is rational (nonzero) and $x_j$ is irrational, then:
- $x_i + x_j$ is irrational
- $x_i x_j$ is irrational (since $x_i \neq 0$ is rational, $x_i x_j$ rational would imply $x_j$ rational)

So neither is rational! This means we cannot have a rational $x_i$ and an irrational $x_j$ in the set simultaneously.

So either all $x_i$ are rational, or all $x_i$ are irrational.

If all are rational, then $S$ has all rational values, so 0 irrational values.

If all are irrational, we need to analyze the constraint more carefully.

So all $x_i$ are irrational, and for each pair, either $x_i + x_j$ or $x_i x_j$ is rational.

Now, $x_i^2$ is irrational iff $x_i$ is not of the form $\pm\sqrt{q}$ for rational $q$... wait, no. $x_i^2$ is irrational means $x_i^2 \notin \mathbb{Q}$.

Actually, let me think about when $x_i^2$ is rational. $x_i^2$ is rational iff $x_i = \pm\sqrt{q}$ for some positive rational $q$ (or $x_i$ rational, but we've excluded that case). So $x_i^2$ is irrational means $x_i$ is not of the form $\pm\sqrt{q}$ for rational $q > 0$.

We want to maximize the number of $x_i$ with $x_i^2$ irrational.

Let me think about the structure of the set when all $x_i$ are irrational.

For each pair $(i,j)$, either $x_i + x_j \in \mathbb{Q}$ or $x_i x_j \in \mathbb{Q}$.

Let me define a graph on the 10 elements. Color edge $(i,j)$ "sum" if $x_i + x_j \in \mathbb{Q}$, and "product" if $x_i x_j \in \mathbb{Q}$ (and both if both are rational).

Let me think about what structures are possible.

Case 1: $x_i + x_j \in \mathbb{Q}$ for all pairs.
This means all $x_i$ are of the form $q_i + \alpha$ for some fixed irrational $\alpha$ and rational $q_i$. Wait, let me check. If $x_i + x_j \in \mathbb{Q}$ for all $i, j$, then $x_i + x_j = r_{ij} \in \mathbb{Q}$. Then $x_i - x_k = (x_i + x_j) - (x_j + x_k) = r_{ij} - r_{jk} \in \mathbb{Q}$. So all $x_i$ differ by rationals. So $x_i = \alpha + q_i$ for some fixed $\alpha$ (irrational) and rational $q_i$.

Then $x_i^2 = (\alpha + q_i)^2 = \alpha^2 + 2q_i\alpha + q_i^2$. This is rational iff $\alpha^2 + 2q_i\alpha$ is rational, i.e., $\alpha^2 \in \mathbb{Q}$ and $q_i = 0$ (if $\alpha \notin \mathbb{Q}$, then $2q_i\alpha$ is rational only if $q_i = 0$). Wait, $\alpha^2 + 2q_i\alpha$ is rational. If $\alpha^2$ is rational, then $2q_i\alpha$ must be rational, so $q_i = 0$ (since $\alpha$ is irrational). So $x_i^2$ is rational only when $q_i = 0$, i.e., $x_i = \alpha$.

If $\alpha^2$ is irrational, then $x_i^2$ is always irrational (since $\alpha^2 + 2q_i\alpha + q_i^2$ with $\alpha^2$ irrational and $2q_i\alpha$ irrational (for $q_i \neq 0$) or $0$ (for $q_i = 0$)... wait, for $q_i = 0$, $x_i^2 = \alpha^2$ which is irrational. For $q_i \neq 0$, $x_i^2 = \alpha^2 + 2q_i\alpha + q_i^2$. Is this rational? $\alpha^2$ is irrational, $2q_i\alpha$ is irrational, so the sum could be rational if they cancel. But $\alpha^2$ and $2q_i\alpha$ are both irrational; their sum being rational requires $\alpha^2 + 2q_i\alpha \in \mathbb{Q}$, i.e., $\alpha(\alpha + 2q_i) \in \mathbb{Q}$.

Hmm, this is getting complicated. Let me think differently.

Actually, let me think about this more carefully with specific constructions.

Let me consider the case where all pairwise sums are rational. Then $x_i = \alpha + q_i$ with $\alpha$ irrational, $q_i$ distinct rationals (since $x_i$ are distinct). We need $x_i \neq 0$, so $q_i \neq -\alpha$, which is automatically satisfied since $q_i$ is rational and $\alpha$ is irrational.

Now $x_i^2 = \alpha^2 + 2q_i\alpha + q_i^2$. For this to be rational, we need $\alpha^2 + 2q_i\alpha \in \mathbb{Q}$.

If $\alpha^2 \in \mathbb{Q}$ (say $\alpha^2 = c$), then we need $2q_i\alpha \in \mathbb{Q}$, so $q_i = 0$. Only $x_i = \alpha$ has rational square. So at most 1 rational square, meaning at least 9 irrational squares.

If $\alpha^2 \notin \mathbb{Q}$, then we need $\alpha^2 + 2q_i\alpha \in \mathbb{Q}$ for some $q_i$. This means $\alpha$ satisfies $\alpha^2 + 2q_i\alpha - r = 0$ for some rational $r$, i.e., $\alpha = -q_i \pm \sqrt{q_i^2 + r}$. So $\alpha$ is of the form $-q_i + \sqrt{q_i^2 + r}$ where $q_i^2 + r > 0$ and $\sqrt{q_i^2 + r}$ is irrational. Then $\alpha^2 = q_i^2 - 2q_i\sqrt{q_i^2+r} + (q_i^2 + r) = 2q_i^2 + r - 2q_i\sqrt{q_i^2+r}$, which is indeed irrational (if $q_i \neq 0$).

For a given $\alpha$, the values of $q$ for which $\alpha^2 + 2q\alpha \in \mathbb{Q}$ are determined: $\alpha^2 + 2q\alpha = r$ means $q = \frac{r - \alpha^2}{2\alpha}$. Since $\alpha$ is fixed and irrational, $q$ is rational iff $r - \alpha^2$ is a rational multiple of $\alpha$, i.e., $r = \alpha^2 + 2q\alpha$ for rational $q$. But this is circular.

Let me think about it differently. Given $\alpha$ irrational, $\alpha^2 + 2q\alpha \in \mathbb{Q}$ iff $q = \frac{s - \alpha^2}{2\alpha}$ for some $s \in \mathbb{Q}$. For $q$ to be rational, we need $\frac{s - \alpha^2}{2\alpha} \in \mathbb{Q}$, i.e., $s - \alpha^2 = 2q\alpha$ for rational $q$, i.e., $\alpha^2 + 2q\alpha = s \in \mathbb{Q}$. So the set of rational $q$ for which $\alpha^2 + 2q\alpha \in \mathbb{Q}$ is exactly the set of $q$ such that $\alpha^2 + 2q\alpha \in \mathbb{Q}$.

If $\alpha$ is algebraic of degree 2, say $\alpha = a + b\sqrt{d}$ with $a, b$ rational, $b \neq 0$, $d$ square-free, then $\alpha^2 = a^2 + b^2 d + 2ab\sqrt{d}$, and $2q\alpha = 2qa + 2qb\sqrt{d}$. So $\alpha^2 + 2q\alpha = (a^2 + b^2 d + 2qa) + (2ab + 2qb)\sqrt{d}$. This is rational iff $2ab + 2qb = 0$, i.e., $q = -a$. So there's exactly one rational $q$ (namely $q = -a$) for which $\alpha^2 + 2q\alpha$ is rational.

If $\alpha$ is algebraic of degree $> 2$ or transcendental, then $\alpha^2 + 2q\alpha \in \mathbb{Q}$ might have no rational solutions $q$, or it depends.

Actually, for transcendental $\alpha$: $\alpha^2 + 2q\alpha = s$ means $\alpha^2 + 2q\alpha - s = 0$. But $\alpha$ is transcendental, so it can't satisfy any polynomial equation with rational coefficients. So there's no rational $q$ and $s$ with $\alpha^2 + 2q\alpha = s$. So for transcendental $\alpha$, all $x_i^2$ are irrational. That gives 10 irrational values!

Wait, but we need all $x_i$ to be irrational and pairwise distinct, and all pairwise sums rational. With $\alpha$ transcendental and $q_i$ distinct rationals, $x_i = \alpha + q_i$ are all irrational (since $\alpha$ is irrational and $q_i$ rational), pairwise distinct (since $q_i$ distinct), non-zero (since $\alpha$ is irrational and $-q_i$ is rational). And all pairwise sums $x_i + x_j = 2\alpha + q_i + q_j$... wait, that's not rational! $2\alpha$ is irrational.

Oh wait, I made an error. If $x_i + x_j \in \mathbb{Q}$ for all $i, j$, then $x_i = \alpha + q_i$ where $\alpha$ is some fixed value and $q_i$ are rational. But $x_i + x_j = 2\alpha + q_i + q_j$. For this to be rational, $2\alpha$ must be rational, so $\alpha$ is rational. But then all $x_i$ are rational, contradiction.

Hmm, let me redo this. If $x_i + x_j \in \mathbb{Q}$ for all $i \neq j$, then take three indices $i, j, k$. We have $x_i + x_j = r_1$, $x_i + x_k = r_2$, $x_j + x_k = r_3$, all rational. Then $x_i = (r_1 + r_2 - r_3)/2 \in \mathbb{Q}$. So all $x_i$ are rational!

So the case "all pairwise sums rational" forces all $x_i$ to be rational. That's the trivial case.

OK so we can't have all sums rational (unless all are rational). So we need a mix: some pairs have rational sum, some have rational product.

Let me reconsider. We have all $x_i$ irrational. For each pair, either sum or product is rational.

Let me think about what happens with products. If $x_i x_j \in \mathbb{Q}$ for all $i, j$, then $x_i x_j = r_{ij} \in \mathbb{Q}$. Take three indices: $x_1 x_2 = r_{12}$, $x_1 x_3 = r_{13}$, $x_2 x_3 = r_{23}$. Then $x_1^2 = r_{12} r_{13} / r_{23} \in \mathbb{Q}$. So all $x_i^2 \in \mathbb{Q}$, meaning all $x_i = \pm\sqrt{q_i}$ for rational $q_i > 0$.

In this case, all $x_i^2$ are rational, so 0 irrational values. Not what we want.

So we need a mix. Let me think about the structure more carefully.

Let me partition the indices into groups based on the structure. Let me think about what constraints arise.

Consider two elements $x_i, x_j$ with $x_i x_j \in \mathbb{Q}$ (and $x_i + x_j \notin \mathbb{Q}$). And $x_i, x_k$ with $x_i x_k \in \mathbb{Q}$. Then $x_j / x_k = (x_i x_j)/(x_i x_k) \in \mathbb{Q}$. So $x_j = r \cdot x_k$ for some rational $r$.

Now consider $x_j, x_k$: we need $x_j + x_k$ or $x_j x_k$ rational. $x_j x_k = r x_k^2$. If $x_k^2 \in \mathbb{Q}$, then $x_j x_k \in \mathbb{Q}$. If $x_k^2 \notin \mathbb{Q}$, then we need $x_j + x_k = (r+1) x_k \in \mathbb{Q}$, so $x_k \in \mathbb{Q}$, contradiction. So if $x_k^2 \notin \mathbb{Q}$, we need $x_j x_k \in \mathbb{Q}$, which requires $r x_k^2 \in \mathbb{Q}$, i.e., $x_k^2 \in \mathbb{Q}$ (since $r$ is rational and nonzero). Contradiction. So actually, if $x_i x_j$ and $x_i x_k$ are both rational, and $x_k^2 \notin \mathbb{Q}$, then... we get a contradiction?

Wait, let me re-examine. We have $x_j = r x_k$ with $r$ rational. For the pair $(j, k)$: either $x_j + x_k = (r+1)x_k$ is rational, or $x_j x_k = r x_k^2$ is rational. 

If $x_k^2 \notin \mathbb{Q}$: $r x_k^2 \notin \mathbb{Q}$ (since $r \neq 0$ rational). And $(r+1)x_k \in \mathbb{Q}$ requires $x_k \in \mathbb{Q}$ (if $r \neq -1$) or $x_j + x_k = 0$ (if $r = -1$, but then $x_j = -x_k$, so $x_j + x_k = 0 \in \mathbb{Q}$). 

So if $r = -1$, i.e., $x_j = -x_k$, then $x_j + x_k = 0$ is rational. That works!

If $r \neq -1$ and $x_k^2 \notin \mathbb{Q}$: we need $(r+1)x_k \in \mathbb{Q}$, so $x_k \in \mathbb{Q}$, contradiction. So this is impossible.

So: if $x_i x_j, x_i x_k \in \mathbb{Q}$ and $x_k^2 \notin \mathbb{Q}$, then either $x_j = -x_k$ (i.e., $r = -1$) or we have a contradiction.

Interesting. So let me think about this more carefully.

Let me define the "product class" structure. Say $x_i \sim x_j$ if $x_i x_j \in \mathbb{Q}$. This isn't necessarily an equivalence relation, but let me explore.

Actually, let me think about it differently. Let me consider the values $x_i$ and group them.

Let's say a value $x_i$ has $x_i^2 \in \mathbb{Q}$ (call it "type R") or $x_i^2 \notin \mathbb{Q}$ (call it "type I").

For two type I values $x_i, x_j$: We need $x_i + x_j \in \mathbb{Q}$ or $x_i x_j \in \mathbb{Q}$.

If $x_i x_j \in \mathbb{Q}$, say $x_i x_j = r$. Then $x_j = r/x_i$. And $x_j^2 = r^2/x_i^2$. Since $x_i^2 \notin \mathbb{Q}$ and $r \in \mathbb{Q}$, $x_j^2 \notin \mathbb{Q}$. Consistent.

If $x_i + x_j \in \mathbb{Q}$, say $x_i + x_j = s$. Then $x_j = s - x_i$. And $x_j^2 = s^2 - 2sx_i + x_i^2$. For $x_j^2 \notin \mathbb{Q}$: we need $s^2 - 2sx_i + x_i^2 \notin \mathbb{Q}$. Since $x_i^2 \notin \mathbb{Q}$, and $-2sx_i$ is irrational (if $s \neq 0$), the sum $x_i^2 - 2sx_i$ could be rational or irrational. If $s = 0$, then $x_j = -x_i$ and $x_j^2 = x_i^2 \notin \mathbb{Q}$. If $s \neq 0$, it depends.

OK this is getting complex. Let me try to think about specific constructions and find the maximum.

Let me try to construct examples with many irrational squares.

**Construction attempt 1**: All $x_i$ of the form $c \cdot \sqrt{d}$ for various rational $c$ and fixed square-free $d$.

If $x_i = c_i \sqrt{d}$ with $c_i$ rational, $d$ square-free positive integer (not a perfect square), then:
- $x_i x_j = c_i c_j d \in \mathbb{Q}$ for all $i, j$. 
- $x_i^2 = c_i^2 d \notin \mathbb{Q}$ (since $d$ is not a perfect square and $c_i \neq 0$).

So all products are rational, all squares are irrational. We can have 10 distinct values $c_1\sqrt{d}, \ldots, c_{10}\sqrt{d}$ with distinct rational $c_i$. All non-zero. This gives 10 irrational squares!

Wait, but that seems too easy. Let me double-check. $x_i = c_i \sqrt{d}$, $x_j = c_j \sqrt{d}$. $x_i x_j = c_i c_j d$. Since $c_i, c_j$ are rational and $d$ is a positive integer, $c_i c_j d \in \mathbb{Q}$. Yes. And $x_i^2 = c_i^2 d$. Since $d$ is not a perfect square, $c_i^2 d \notin \mathbb{Q}$ (as $c_i \neq 0$). Yes.

So we can achieve 10 irrational values in $S$? That seems like the answer would be 10.

But wait, let me re-read the problem. "Determine the maximum possible number of irrational values in the set $S$." And $S = \{x_1^2, \ldots, x_{10}^2\}$. Note that $S$ is a set, so if some $x_i^2$ are equal, they count once. But in our construction, $x_i^2 = c_i^2 d$ and since $c_i$ are distinct, $c_i^2$ are... well, $c_i^2$ could coincide if $c_i = -c_j$. But we can choose $c_i$ to be distinct positive rationals, so $c_i^2$ are distinct, and $x_i^2$ are all distinct and all irrational. So $|S| = 10$ and all are irrational.

Hmm, but that gives 10, which seems too straightforward for a competition problem. Let me re-read the problem.

"Ten pairwise distinct non-zero real numbers $x_1, x_2, \dots, x_{10}$ are such that for any two distinct indices $i, j \in \{1, \dots, 10\}$, either their sum $x_i + x_j$ or their product $x_i x_j$ is a rational number."

OK so with $x_i = c_i \sqrt{d}$, the product $x_i x_j = c_i c_j d$ is always rational. The sum $x_i + x_j = (c_i + c_j)\sqrt{d}$ is irrational (since $c_i + c_j \neq 0$ if we choose $c_i$ all positive, and $\sqrt{d}$ is irrational). But the condition only requires ONE of sum or product to be rational, and the product is always rational. So this works.

And all $x_i^2 = c_i^2 d$ are irrational and distinct. So the answer is 10?

Wait, but this seems way too easy. Let me reconsider whether I'm missing something. Maybe the problem is asking something subtler.

Hmm, actually, re-reading: "Determine the maximum possible number of irrational values in the set $S$." Since $S$ is a set, the number of irrational values is the number of distinct irrational elements. In our construction, all 10 are distinct and irrational, so the answer is 10.

But this feels too easy for what looks like a competition problem. Let me re-examine.

Actually wait, maybe I need to reconsider. Is the problem perhaps more subtle? Let me re-read once more.

"Ten pairwise distinct non-zero real numbers" — OK.
"for any two distinct indices $i, j$, either their sum $x_i + x_j$ or their product $x_i x_j$ is a rational number" — OK.
"$S = \{x_1^2, x_2^2, \dots, x_{10}^2\}$" — this is a set, so duplicates collapse.
"Determine the maximum possible number of irrational values in the set $S$" — the number of elements of $S$ that are irrational.

With the construction $x_i = c_i \sqrt{d}$, we get 10 distinct irrational squares. So the maximum is at least 10, and since $|S| \leq 10$, the maximum is exactly 10.

Hmm, but I feel like I might be missing something. Let me reconsider whether the problem might have additional constraints I'm not seeing, or whether the answer really is 10.

Actually, wait. Let me reconsider. Maybe the problem is from a competition and the answer is indeed 10, but the proof requires showing both that 10 is achievable and that it's the maximum (which is trivially at most 10). But the construction is simple, so maybe the problem is easier than I think, or maybe I'm misunderstanding something.

Let me re-examine: is there any hidden constraint? "Ten pairwise distinct non-zero real numbers" — yes, $c_i \sqrt{d}$ are pairwise distinct if $c_i$ are distinct, and non-zero if $c_i \neq 0$. "for any two distinct indices, either sum or product is rational" — product is always rational. So the construction works.

Actually, I wonder if the problem is more interesting than I think, and maybe the answer is not 10. Let me reconsider.

Oh wait, maybe I should reconsider whether the problem is asking for the maximum over all valid configurations, or something else. No, it's clearly asking for the maximum number of irrational values in $S$.

With the construction I gave, the answer is 10. Since $S$ has at most 10 elements, 10 is the maximum.

Hmm, but let me reconsider. Maybe there's a subtlety with the set $S$. If some $x_i^2$ values coincide, $S$ could have fewer than 10 elements. But we want to MAXIMIZE the number of irrational values, so we'd want them all distinct and all irrational, which we achieved.

I think the answer is 10. Let me verify once more with a concrete example.

Take $d = 2$. Let $x_i = i\sqrt{2}$ for $i = 1, 2, \ldots, 10$. These are 10 pairwise distinct non-zero reals. For any $i \neq j$, $x_i x_j = ij \cdot 2 = 2ij \in \mathbb{Q}$. And $x_i^2 = 2i^2 \notin \mathbb{Q}$. All $x_i^2$ are distinct (since $i^2$ are distinct for $i = 1, \ldots, 10$). So $S = \{2, 8, 18, 32, 50, 72, 98, 128, 162, 200\}$, all of which are... wait, $2i^2$ for $i = 1, \ldots, 10$: $2, 8, 18, 32, 50, 72, 98, 128, 162, 200$. Are these irrational? $2 \cdot 1 = 2$ is rational! $2 \cdot 4 = 8$ is rational!

Oh no! $x_i^2 = 2i^2$ is always rational! Because $2i^2$ is a rational number (it's an integer). I made an error!

$x_i = i\sqrt{2}$, so $x_i^2 = i^2 \cdot 2 = 2i^2$, which is an integer, hence rational. So all squares are rational. That gives 0 irrational values, not 10.

I see my error now. $x_i = c_i \sqrt{d}$ gives $x_i^2 = c_i^2 d$, which is rational since $c_i$ and $d$ are rational. So all squares are rational. The construction gives 0 irrational squares, not 10.

So I was wrong. Let me reconsider.

If $x_i = c_i \sqrt{d}$, then $x_i^2 = c_i^2 d \in \mathbb{Q}$. So all products being rational forces all squares to be rational (as I showed earlier). So to get irrational squares, we need some pairs to have rational sums instead of rational products.

OK so now the problem is more interesting. Let me restart the analysis.

We have all $x_i$ irrational (as shown, we can't mix rational and irrational). For each pair, either sum or product is rational. We want to maximize the number of $x_i^2$ that are irrational.

Let me think about the structure. Let me consider the graph where we color each edge as "sum" (if $x_i + x_j \in \mathbb{Q}$) or "product" (if $x_i x_j \in \mathbb{Q}$). An edge could be both.

Key observations:
1. If $x_i x_j \in \mathbb{Q}$ and $x_i x_k \in \mathbb{Q}$, then $x_j/x_k \in \mathbb{Q}$, so $x_j = r x_k$ for rational $r$.
2. If $x_i + x_j \in \mathbb{Q}$ and $x_i + x_k \in \mathbb{Q}$, then $x_j - x_k \in \mathbb{Q}$, so $x_j = x_k + s$ for rational $s$.

Let me think about what happens with type I values (those with $x_i^2 \notin \mathbb{Q}$).

Suppose $x_i$ is type I ($x_i^2 \notin \mathbb{Q}$). Consider any other $x_j$.

Case A: $x_i x_j \in \mathbb{Q}$, say $x_i x_j = r$. Then $x_j = r/x_i$, and $x_j^2 = r^2/x_i^2 \notin \mathbb{Q}$ (since $x_i^2 \notin \mathbb{Q}$ and $r \neq 0$). So $x_j$ is also type I.

Case B: $x_i + x_j \in \mathbb{Q}$, say $x_i + x_j = s$. Then $x_j = s - x_i$, and $x_j^2 = s^2 - 2sx_i + x_i^2$. 
- If $s = 0$: $x_j = -x_i$, $x_j^2 = x_i^2 \notin \mathbb{Q}$. Type I.
- If $s \neq 0$: $x_j^2 = x_i^2 - 2sx_i + s^2$. Since $x_i^2 \notin \mathbb{Q}$ and $2sx_i \notin \mathbb{Q}$ (as $s \neq 0$ rational and $x_i$ irrational), the sum $x_i^2 - 2sx_i$ could be rational or irrational. If $x_i^2 - 2sx_i \in \mathbb{Q}$, then $x_j^2 \in \mathbb{Q}$ (type R). Otherwise, $x_j^2 \notin \mathbb{Q}$ (type I).

So a type I value $x_i$ can be connected to a type R value $x_j$ only via a rational sum with $s \neq 0$ and $x_i^2 - 2sx_i \in \mathbb{Q}$.

Now, $x_i^2 - 2sx_i \in \mathbb{Q}$ means $x_i$ satisfies $x_i^2 - 2sx_i - q = 0$ for some $q \in \mathbb{Q}$, i.e., $x_i = s \pm \sqrt{s^2 + q}$. So $x_i$ is of the form $s + \sqrt{m}$ or $s - \sqrt{m}$ where $m = s^2 + q \in \mathbb{Q}$ and $\sqrt{m}$ is irrational (so $m > 0$ and not a perfect square of a rational).

So if $x_i$ is type I and connected to a type R value via rational sum, then $x_i = s \pm \sqrt{m}$ for some rational $s$ and positive rational $m$ (with $\sqrt{m}$ irrational).

In this case, $x_i^2 = s^2 + m \pm 2s\sqrt{m}$. For $x_i^2 \notin \mathbb{Q}$, we need $s \neq 0$ (if $s = 0$, $x_i^2 = m \in \mathbb{Q}$, contradiction with type I). So $s \neq 0$.

And the type R value is $x_j = s - x_i = \mp\sqrt{m}$ (if $x_i = s \pm \sqrt{m}$, then $x_j = s - (s \pm \sqrt{m}) = \mp\sqrt{m}$). So $x_j = \mp\sqrt{m}$, and $x_j^2 = m \in \mathbb{Q}$. Consistent.

So the pair $(x_i, x_j)$ with $x_i = s + \sqrt{m}$, $x_j = -\sqrt{m}$ (or $x_i = s - \sqrt{m}$, $x_j = \sqrt{m}$) has $x_i + x_j = s \in \mathbb{Q}$, $x_i^2 \notin \mathbb{Q}$ (type I), $x_j^2 = m \in \mathbb{Q}$ (type R).

Now, let me think about the overall structure. Let me try to build a configuration with many type I values.

**Approach**: Try to have many type I values that are pairwise connected by rational products.

If $x_i, x_j$ are both type I with $x_i x_j \in \mathbb{Q}$, then as shown, $x_j = r/x_i$ for rational $r$, and $x_j^2 = r^2/x_i^2 \notin \mathbb{Q}$. Good, both stay type I.

Can we have many type I values all pairwise connected by rational products? If $x_i x_j \in \mathbb{Q}$ for all pairs among a set of type I values, then as I showed earlier, this forces all $x_i^2 \in \mathbb{Q}$ (contradiction with type I). Wait, let me recheck.

If $x_i x_j \in \mathbb{Q}$ for all $i, j$ in a subset, take three: $x_1 x_2 = r_{12}$, $x_1 x_3 = r_{13}$, $x_2 x_3 = r_{23}$. Then $x_1^2 = r_{12} r_{13} / r_{23} \in \mathbb{Q}$. So $x_1$ is type R, contradiction.

So among any three type I values, not all three pairwise products can be rational. At least one pair must have a rational sum instead.

So among type I values, we can't have a triangle of all-product edges. By Ramsey theory, this limits the structure.

Let me think about this more carefully. Among the type I values, consider the graph where we connect $i, j$ by a "product edge" if $x_i x_j \in \mathbb{Q}$, and a "sum edge" if $x_i + x_j \in \mathbb{Q}$. Every pair has at least one type of edge (possibly both).

The constraint is: no triangle of all product edges (among type I values). Actually, more precisely, among any three type I values, at least one pair has a rational sum (and possibly also a rational product, but at least the sum is rational).

Hmm wait, actually the constraint is weaker. Among any three type I values, at least one pair must have a rational sum (because if all three pairs had only rational products, we'd get all squares rational, contradiction).

But a pair could have both rational sum and rational product. Let me think about when that happens. If $x_i + x_j = s \in \mathbb{Q}$ and $x_i x_j = r \in \mathbb{Q}$, then $x_i, x_j$ are roots of $t^2 - st + r = 0$, so $x_i, x_j = \frac{s \pm \sqrt{s^2 - 4r}}{2}$. For them to be real and irrational, we need $s^2 - 4r > 0$ and $\sqrt{s^2 - 4r}$ irrational. Then $x_i^2 = \frac{s^2 + (s^2-4r) \pm 2s\sqrt{s^2-4r}}{4} = \frac{2s^2 - 4r \pm 2s\sqrt{s^2-4r}}{4}$. For $x_i^2 \notin \mathbb{Q}$, we need $s \neq 0$.

OK, this is getting complicated. Let me try a different approach and think about specific constructions.

**Construction attempt**: Let me try to have a large set of type I values.

Idea: Use values of the form $x_i = a_i + b_i \sqrt{d}$ where $a_i, b_i$ are rational, $d$ is a fixed square-free positive integer, and $b_i \neq 0$.

Then $x_i + x_j = (a_i + a_j) + (b_i + b_j)\sqrt{d}$. This is rational iff $b_i + b_j = 0$, i.e., $b_j = -b_i$.

And $x_i x_j = (a_i a_j + b_i b_j d) + (a_i b_j + a_j b_i)\sqrt{d}$. This is rational iff $a_i b_j + a_j b_i = 0$, i.e., $a_i b_j = -a_j b_i$, i.e., $a_i/b_i = -a_j/b_j$ (assuming $b_i, b_j \neq 0$), i.e., $a_i/b_i + a_j/b_j = 0$.

And $x_i^2 = (a_i^2 + b_i^2 d) + 2a_i b_i \sqrt{d}$. This is rational iff $a_i b_i = 0$, i.e., $a_i = 0$ (since $b_i \neq 0$). So $x_i^2 \notin \mathbb{Q}$ iff $a_i \neq 0$.

So for type I values (with $a_i \neq 0$), the condition for pair $(i,j)$ is:
- Sum rational: $b_i + b_j = 0$
- Product rational: $a_i/b_i + a_j/b_j = 0$ (equivalently, $a_i b_j + a_j b_i = 0$)

We need at least one of these for each pair.

Let me define $u_i = b_i$ and $v_i = a_i/b_i$ (so $a_i = u_i v_i$). Then:
- Sum rational: $u_i + u_j = 0$, i.e., $u_j = -u_i$
- Product rational: $v_i + v_j = 0$, i.e., $v_j = -v_i$

And type I means $a_i \neq 0$, i.e., $v_i \neq 0$ (since $u_i = b_i \neq 0$).

So we need: for each pair $(i,j)$, either $u_i + u_j = 0$ or $v_i + v_j = 0$.

And we want to maximize the number of pairs $(u_i, v_i)$ with $u_i \neq 0$, $v_i \neq 0$, all $x_i = u_i v_i + u_i \sqrt{d} = u_i(v_i + \sqrt{d})$ distinct and non-zero.

$x_i$ distinct: $u_i(v_i + \sqrt{d}) \neq u_j(v_j + \sqrt{d})$. Since $\sqrt{d}$ is irrational, this means $u_i v_i \neq u_j v_j$ or $u_i \neq u_j$. Actually, $u_i(v_i + \sqrt{d}) = u_j(v_j + \sqrt{d})$ iff $u_i = u_j$ and $u_i v_i = u_j v_j$ (comparing rational and irrational parts). So $x_i = x_j$ iff $u_i = u_j$ and $v_i = v_j$. So we need the pairs $(u_i, v_i)$ to be distinct.

$x_i \neq 0$: $u_i(v_i + \sqrt{d}) \neq 0$. Since $u_i \neq 0$ and $v_i + \sqrt{d} \neq 0$ (as $v_i$ is rational and $\sqrt{d}$ is irrational), this is automatic.

So the problem reduces to: find the maximum number of distinct pairs $(u_i, v_i)$ with $u_i, v_i \in \mathbb{Q} \setminus \{0\}$ such that for each pair $(i,j)$, either $u_i = -u_j$ or $v_i = -v_j$.

This is a clean combinatorial problem! Let me think about it.

We have points $(u_i, v_i)$ in $(\mathbb{Q}^*)^2$ (nonzero rationals). For each pair, either their $u$-coordinates are negatives of each other, or their $v$-coordinates are negatives of each other.

Let me think of this as a graph problem. Consider the "conflict graph" where we connect $i, j$ if neither $u_i = -u_j$ nor $v_i = -v_j$. We need this graph to have no edges, i.e., for every pair, at least one condition holds.

Let me think about what sets of points satisfy this. 

Consider the values $|u_i|$ and $|v_i|$. The condition is: for each pair, either $|u_i| = |u_j|$ (with opposite signs) or $|v_i| = |v_j|$ (with opposite signs).

Actually, more precisely: $u_i = -u_j$ means $|u_i| = |u_j|$ and $\text{sgn}(u_i) \neq \text{sgn}(u_j)$. Similarly for $v$.

Let me group by $|u|$ values and $|v|$ values. 

Let's say we have points with various $|u|$ and $|v|$ values. For two points $(u_i, v_i)$ and $(u_j, v_j)$:
- If $|u_i| \neq |u_j|$ and $|v_i| \neq |v_j|$: neither condition can hold. Bad.
- If $|u_i| = |u_j|$ but $u_i = u_j$ (same sign) and $|v_i| \neq |v_j|$: sum condition fails (need opposite signs), product condition fails. Bad.
- If $|u_i| = |u_j|$ and $u_i = -u_j$ (opposite signs): sum condition holds. Good.
- If $|v_i| = |v_j|$ and $v_i = -v_j$: product condition holds. Good.
- If $|u_i| = |u_j|$, $u_i = u_j$, $|v_i| = |v_j|$, $v_i = -v_j$: product condition holds. Good.
- If $|u_i| = |u_j|$, $u_i = -u_j$, $|v_i| = |v_j|$, $v_i = v_j$: sum condition holds. Good.
- Etc.

So the constraint is: for every pair of points, either (same $|u|$, opposite $u$-sign) or (same $|v|$, opposite $v$-sign).

Let me think about this combinatorially. Let me assign to each point a "row" = $|u_i|$ and "column" = $|v_i|$, and a sign pattern $(\sigma_i, \tau_i)$ where $\sigma_i = \text{sgn}(u_i)$, $\tau_i = \text{sgn}(v_i)$.

For two points in different rows and different columns: neither condition holds. Bad. So all points must share either a row or a column.

This means: the points form a "cross" shape — either all in the same row, or all in the same column, or some in one row and some in one column (forming a cross/L-shape).

Wait, more precisely: for any two points, they must share a row or share a column. This is the condition for a "clique" in the rook's graph. The maximum cliques in a rook's graph are either a full row or a full column. But we can also have a cross: one row plus one column.

Actually, the condition "any two points share a row or column" is exactly the condition for the set to be a clique in the rook's graph. The maximum cliques in a rook's graph $K_{m,n}$ (on an $m \times n$ grid) are: a full row (size $n$) or a full column (size $m$). But we can also have a cross: a row and a column intersecting at one point, giving size $m + n - 1$.

Wait, actually, for a cross (row $r$ union column $c$), any two points in the same row share the row, any two points in the same column share the column, and a point in the row (not at the intersection) and a point in the column (not at the intersection) share... the row point has row $r$ and some column $c'$, the column point has some row $r'$ and column $c$. They share neither row nor column (unless $c' = c$ or $r' = r$, but we said they're not at the intersection). So the cross doesn't work in general!

Hmm, let me reconsider. The condition is: any two points share a row or a column. For a cross (row $r$ ∪ column $c$), take point $(r, c_1)$ and point $(r_1, c)$ where $c_1 \neq c$ and $r_1 \neq r$. These share neither row nor column. So the cross doesn't satisfy the condition.

So the only sets satisfying "any two points share a row or column" are: all in one row, or all in one column. (This is a well-known result.)

Wait, that's not quite right either. What about a set like $\{(1,1), (1,2), (2,1)\}$? Points $(1,1)$ and $(1,2)$ share row 1. Points $(1,1)$ and $(2,1)$ share column 1. Points $(1,2)$ and $(2,1)$ share neither. So this doesn't work.

So indeed, the only sets where every pair shares a row or column are: a single row, or a single column. 

But wait, we also have the sign condition. Even if two points share a row (same $|u|$), we need opposite $u$-signs. And if they share a column (same $|v|$), we need opposite $v$-signs.

**Case 1: All points in the same row (same $|u|$).**
For each pair, we need $u_i = -u_j$ (opposite signs). But if we have 3 or more points, we can't have all pairs with opposite signs (since with 3 points, at least two have the same sign). So at most 2 points in a single row? No wait, we also have the column condition as a fallback.

Hmm, let me reconsider. If all points are in the same row (same $|u| = a$), then for each pair, either $u_i = -u_j$ (opposite $u$-signs) or $v_i = -v_j$ (same $|v|$ and opposite $v$-signs).

So within a row, the condition becomes: for each pair, either opposite $u$-signs or (same $|v|$ and opposite $v$-signs).

Let me split the row into two halves based on $u$-sign: positive $u$ and negative $u$. Any pair within the same half has the same $u$-sign, so they need same $|v|$ and opposite $v$-signs. Any pair across halves has opposite $u$-signs, so the condition is automatically satisfied.

So: within the positive-$u$ half, every pair must have the same $|v|$ and opposite $v$-signs. This means all points in the positive-$u$ half have the same $|v|$, and for each pair, they have opposite $v$-signs. With 3+ points in the positive half, at least two share the same $v$-sign, violating the condition. So at most 2 points in the positive-$u$ half (one with $v > 0$, one with $v < 0$).

Similarly, at most 2 points in the negative-$u$ half.

So at most 4 points in a single row? Wait, but I need to also check cross-half pairs. Cross-half pairs (one positive $u$, one negative $u$) automatically satisfy the condition (opposite $u$-signs). So no additional constraint.

But wait, within the positive-$u$ half, we need all pairs to have the same $|v|$ and opposite $v$-signs. With 2 points, they need the same $|v|$ and opposite $v$-signs. That's fine: $(a, b)$ and $(a, -b)$ for some $a, b > 0$ (using $u = a$, $v = b$ and $u = a$, $v = -b$).

Actually, we could also have just 1 point in the positive half and 1 in the negative half, etc.

So in a single row, the maximum is: 2 in positive-$u$ half (with $v$ and $-v$) + 2 in negative-$u$ half (with $v'$ and $-v'$). But we need all 4 points to be distinct. The 4 points are: $(a, b)$, $(a, -b)$, $(-a, c)$, $(-a, -c)$ for some $b, c > 0$. These are distinct as long as $b \neq c$ or... actually, $(a, b)$ and $(-a, c)$ are always distinct (different $u$-signs). $(a, b)$ and $(a, -b)$ are distinct (different $v$). $(a, b)$ and $(-a, -c)$ are distinct. So all 4 are distinct as long as $b \neq 0$ and $c \neq 0$, which they are.

But wait, I need to check: within the negative-$u$ half, the two points $(-a, c)$ and $(-a, -c)$ need the same $|v|$ (which is $c$) and opposite $v$-signs (which they have). Good.

And cross-half: $(a, b)$ and $(-a, c)$: opposite $u$-signs, condition satisfied. $(a, b)$ and $(-a, -c)$: opposite $u$-signs, satisfied. Etc. All good.

So we can have 4 points in a single row. But can we do better by using multiple rows?

Wait, I showed that all points must be in a single row or single column. So the maximum is either the max for a single row or a single column. By symmetry (swapping $u$ and $v$), they're the same. So the max is 4.

But wait, I think I was too hasty. Let me reconsider whether all points must be in a single row or column.

The condition is: for each pair $(i, j)$, either $|u_i| = |u_j|$ (with opposite signs) or $|v_i| = |v_j|$ (with opposite signs).

Actually, I need to be more careful. The condition is:
- $u_i = -u_j$ (which requires $|u_i| = |u_j|$ and opposite signs), OR
- $v_i = -v_j$ (which requires $|v_i| = |v_j|$ and opposite signs).

So for each pair, at least one of these holds. Let me think about the "row" as $|u|$ and "column" as $|v|$. Two points in different rows and different columns can't satisfy either condition. So for every pair, they must share a row or share a column.

As I argued, this means all points are in a single row or single column. (This is because if we have points in two different rows and two different columns, we can find a pair that shares neither.)

Wait, actually, let me re-examine. Suppose we have points at $(r_1, c_1)$, $(r_1, c_2)$, $(r_2, c_1)$. The pair $(r_1, c_2)$ and $(r_2, c_1)$ shares neither row nor column. So this doesn't work. Hence, all points must be in a single row or single column.

So the maximum number of type I values (in this $\sqrt{d}$ framework) is 4.

But wait, I restricted to values of the form $a + b\sqrt{d}$. Maybe there are other forms that allow more type I values?

Hmm, but actually, the problem doesn't restrict to quadratic irrationals. Let me think about whether we can do better with more general irrationals.

Let me reconsider the general problem. We have all $x_i$ irrational, and for each pair, either $x_i + x_j \in \mathbb{Q}$ or $x_i x_j \in \mathbb{Q}$. We want to maximize the number of $x_i^2 \notin \mathbb{Q}$.

Let me separate the type I values (those with $x_i^2 \notin \mathbb{Q}$) and type R values (those with $x_i^2 \in \mathbb{Q}$).

**Key constraint among type I values**: Among any three type I values, not all three pairwise products can be rational (as this would force all squares to be rational).

But the constraint is actually stronger. Let me think about what graphs are possible.

Among type I values, define a graph $G$ where we put a "product edge" between $i, j$ if $x_i x_j \in \mathbb{Q}$. The constraint is: $G$ is triangle-free (no three mutually connected by product edges).

Wait, is that exactly right? If $x_i x_j, x_i x_k, x_j x_k$ are all rational, then $x_i^2 = (x_i x_j)(x_i x_k)/(x_j x_k) \in \mathbb{Q}$, contradiction. So yes, among type I values, the "product graph" is triangle-free.

By Ramsey theory, $R(3,3) = 6$, so among 6 type I values, there must be a triangle in the product graph or a triangle in the complement (the "sum graph"). But a triangle in the product graph is forbidden. So among 6 type I values, there must be a triangle in the sum graph (three values pairwise connected by rational sums).

But as I showed earlier, if $x_i + x_j, x_i + x_k, x_j + x_k$ are all rational, then all $x_i$ are rational. Contradiction (they're all irrational). So there can't be a triangle in the sum graph either!

Wait, that's a key point. If three values have all pairwise sums rational, they must all be rational. But our values are all irrational. So the sum graph is also triangle-free!

So among type I values, both the product graph and the sum graph are triangle-free. Since every edge is either a product edge or a sum edge (or both), the complete graph on the type I values is the union of two triangle-free graphs.

By Ramsey theory, $R(3,3) = 6$, so we can't have 6 vertices whose complete graph is 2-colored with no monochromatic triangle. So we can have at most 5 type I values.

Wait, let me be more careful. The "product graph" and "sum graph" might share edges (both sum and product rational). Let me think about this.

Actually, let me define it more carefully. For each pair of type I values $(i, j)$, at least one of $x_i + x_j$ or $x_i x_j$ is rational. Color the edge "red" if $x_i x_j \in \mathbb{Q}$ (product rational) and "blue" if $x_i + x_j \in \mathbb{Q}$ (sum rational). An edge can be both red and blue.

The constraint is:
- No all-red triangle (would force all squares rational).
- No all-blue triangle (would force all values rational).

But an edge can be both red and blue. So this isn't a standard 2-coloring. However, we can convert it: for each edge that's both red and blue, assign it one color (say red). Then we get a valid 2-coloring with no all-red triangle and no all-blue triangle. By $R(3,3) = 6$, we can have at most 5 vertices.

Wait, but I need to be careful. If an edge is both red and blue, and I assign it red, then an all-red triangle might appear. Let me think again.

Actually, the constraint is: there's no triangle where all three edges are red (product), and no triangle where all three edges are blue (sum). If an edge is both, it counts as both red and blue. So a triangle with two "both" edges and one "red" edge would be an all-red triangle (since the "both" edges are red). And it would also be an all-blue triangle only if the third edge is also blue.

Hmm, this is a bit subtle. Let me think about it differently.

For each pair, define $P(i,j) = 1$ if $x_i x_j \in \mathbb{Q}$, and $S(i,j) = 1$ if $x_i + x_j \in \mathbb{Q}$. We have $P(i,j) \lor S(i,j) = 1$ for all pairs.

Constraint 1: No triangle with all $P = 1$ (among type I values).
Constraint 2: No triangle with all $S = 1$ (among all values, since it forces rationality).

Now, for a 2-coloring where each edge is red ($P=1, S=0$), blue ($P=0, S=1$), or purple ($P=1, S=1$):
- No triangle with all edges red or purple (i.e., all $P=1$).
- No triangle with all edges blue or purple (i.e., all $S=1$).

If we replace each purple edge with red, we get a 2-coloring (red/blue) with no all-red triangle. If we replace each purple edge with blue, we get a 2-coloring with no all-blue triangle. But we need both simultaneously.

Actually, let me think about it as: we have a graph where each edge is labeled with a nonempty subset of {P, S}. No triangle has all edges containing P, and no triangle has all edges containing S.

For each edge, if it's {P,S} (both), we can choose to "drop" one of the labels. We want to assign each edge a single label (P or S) such that no triangle is all-P and no triangle is all-S. This is exactly a 2-coloring of the complete graph with no monochromatic triangle, which by $R(3,3)=6$ requires at most 5 vertices.

But can we always make such an assignment? If an edge is {P}, we must assign P. If {S}, we must assign S. If {P,S}, we can choose. The question is whether there exists a valid assignment.

Hmm, actually, the constraints are on the original labeling, not on any assignment. Let me think about whether the original constraints directly imply at most 5 type I values.

Consider 6 type I values. For each pair, $P(i,j) \lor S(i,j)$. No triangle has all $P$, no triangle has all $S$.

Consider the graph $G_P$ (edges where $P=1$) and $G_S$ (edges where $S=1$). $G_P \cup G_S = K_n$ (complete graph). $G_P$ is triangle-free and $G_S$ is triangle-free.

Since $G_P$ is triangle-free, by Turán's theorem, $|E(G_P)| \leq n^2/4$ (for $n$ vertices, triangle-free graph has at most $n^2/4$ edges). Similarly for $G_S$. So $|E(G_P)| + |E(G_S)| \leq n^2/2$. But $|E(G_P)| + |E(G_S)| \geq |E(G_P \cup G_S)| = \binom{n}{2} = n(n-1)/2$.

So $n(n-1)/2 \leq n^2/2$, which gives $n-1 \leq n$, always true. Not helpful.

But we also have $G_P \cap G_S$ (edges that are both). Let $a = |E(G_P) \setminus E(G_S)|$, $b = |E(G_S) \setminus E(G_P)|$, $c = |E(G_P) \cap E(G_S)|$. Then $a + b + c = \binom{n}{2}$, $a + c \leq n^2/4$ (triangle-free), $b + c \leq n^2/4$.

Adding: $a + b + 2c \leq n^2/2$. Since $a + b + c = n(n-1)/2$, we get $n(n-1)/2 + c \leq n^2/2$, so $c \leq n/2$.

For $n = 6$: $c \leq 3$, $a + c \leq 9$, $b + c \leq 9$, $a + b + c = 15$. So $a + b \geq 12$, and $a \leq 9, b \leq 9$ (since $c \geq 0$). Also $a + c \leq 9$ and $b + c \leq 9$ with $a + b + c = 15$ gives $c \geq 15 - 9 - 9 = -3$, not helpful. And $a + c \leq 9$ gives $a \leq 9 - c$, $b + c \leq 9$ gives $b \leq 9 - c$, so $a + b + c \leq 18 - c$, i.e., $15 \leq 18 - c$, i.e., $c \leq 3$.

So for $n = 6$, we need $c \leq 3$, $a + c \leq 9$, $b + c \leq 9$, $a + b + c = 15$. This gives $a \geq 15 - 9 - 0 = 6$ (from $b \leq 9$ and $c \geq 0$), etc. It seems numerically possible. So the counting argument doesn't rule out $n = 6$.

Let me try $R(3,3) = 6$ more directly. We have a complete graph on 6 vertices, each edge labeled with a nonempty subset of {P, S}. No all-P triangle, no all-S triangle.

For each edge, choose one label (if both, choose one). This gives a 2-coloring. By $R(3,3) = 6$, there's a monochromatic triangle. If it's all-P, that's a violation. If it's all-S, that's a violation.

But wait—the monochromatic triangle in the 2-coloring might not be a monochromatic triangle in the original labeling. For example, if an edge was {P,S} and we chose S, then in the all-S triangle of the 2-coloring, that edge has $S=1$ in the original, which is fine. But the other edges in the triangle might have been {P} (forced P) and we chose... no, if an edge is {P} only, we must choose P, so it can't be in an all-S triangle.

Let me be more careful. We have edges labeled {P}, {S}, or {P,S}. We want to choose a single label for each {P,S} edge such that the resulting 2-coloring has no monochromatic triangle.

This is exactly the question of whether a "list coloring" of the complete graph avoids monochromatic triangles. By $R(3,3) = 6$, any 2-coloring of $K_6$ has a monochromatic triangle. So no matter how we choose, there will be a monochromatic triangle. If it's all-P, it corresponds to an all-P triangle in the original (since every edge in the triangle has $P=1$—either it was {P} or {P,S} and we chose P). If it's all-S, similarly.

Wait, that's the key. In the 2-coloring, every edge labeled P (whether from {P} or {P,S}→P) has $P=1$ in the original. So an all-P triangle in the 2-coloring is an all-P triangle in the original. Similarly for S. So the 2-coloring has a monochromatic triangle (by $R(3,3)=6$), which is a monochromatic triangle in the original. Contradiction.

So we can have at most 5 type I values! And we need to check that 5 is achievable.

Wait, I need to double-check the claim about all-S triangles. If three type I values have all pairwise sums rational, then they're all rational (as I showed). But they're type I, so irrational. Contradiction. So no all-S triangle among type I values. ✓

And no all-P triangle among type I values (as shown, it forces all squares rational). ✓

So by $R(3,3) = 6$, at most 5 type I values. Now I need to check:
1. Can we achieve 5 type I values?
2. What about type R values? Can we add type R values alongside type I values?

Let me first check if 5 type I values is achievable. I need 5 irrational numbers, all with irrational squares, such that for each pair, either sum or product is rational, and no three have all pairwise products rational, and no three have all pairwise sums rational.

The unique (up to isomorphism) 2-coloring of $K_5$ with no monochromatic triangle is the 5-cycle coloring: color the edges of the 5-cycle one color, and the complementary 5-cycle the other color.

So let's say the "product edges" form a 5-cycle: $x_1 x_2, x_2 x_3, x_3 x_4, x_4 x_5, x_5 x_1$ are rational, and the "sum edges" form the complementary 5-cycle: $x_1 + x_3, x_1 + x_4, x_2 + x_4, x_2 + x_5, x_3 + x_5$ are rational.

Let me try to construct such values. Let me use the $\sqrt{d}$ framework.

Recall: $x_i = u_i(v_i + \sqrt{d})$ where $u_i, v_i$ are rational, $u_i, v_i \neq 0$.
- Product rational: $v_i + v_j = 0$, i.e., $v_j = -v_i$.
- Sum rational: $u_i + u_j = 0$, i.e., $u_j = -u_i$.
- Type I: $v_i \neq 0$ (which we already have).

Wait, I think I had the conditions swapped. Let me recompute.

$x_i = u_i v_i + u_i \sqrt{d}$ where $u_i = b_i$, $v_i = a_i / b_i$, so $a_i = u_i v_i$, $b_i = u_i$.

$x_i x_j = (u_i v_i + u_i \sqrt{d})(u_j v_j + u_j \sqrt{d}) = u_i u_j (v_i v_j + d + (v_i + v_j)\sqrt{d})$.

This is rational iff $v_i + v_j = 0$.

$x_i + x_j = u_i(v_i + \sqrt{d}) + u_j(v_j + \sqrt{d}) = (u_i v_i + u_j v_j) + (u_i + u_j)\sqrt{d}$.

This is rational iff $u_i + u_j = 0$.

$x_i^2 = u_i^2(v_i^2 + d + 2v_i\sqrt{d})$. This is rational iff $v_i = 0$. Since $v_i \neq 0$, $x_i^2$ is irrational. ✓

So:
- Product edge between $i, j$: $v_i = -v_j$.
- Sum edge between $i, j$: $u_i = -u_j$.

For the 5-cycle product graph: $v_1 = -v_2, v_2 = -v_3, v_3 = -v_4, v_4 = -v_5, v_5 = -v_1$.

From $v_1 = -v_2, v_2 = -v_3$: $v_1 = v_3$. From $v_3 = -v_4, v_4 = -v_5$: $v_3 = v_5$. From $v_5 = -v_1$: $v_3 = -v_1$. But $v_1 = v_3$, so $v_1 = -v_1$, so $v_1 = 0$. Contradiction (need $v_i \neq 0$).

So the 5-cycle product graph doesn't work with this framework! The issue is that a 5-cycle has odd length, so going around the cycle, $v_1 = -v_2 = v_3 = -v_4 = v_5 = -v_1$, giving $v_1 = -v_1$, so $v_1 = 0$.

So we can't realize the 5-cycle product graph with this framework. We need a different approach.

Hmm, let me think about whether we can use a different structure. Maybe not all values need to be of the form $a + b\sqrt{d}$.

Actually, let me reconsider. The condition for a "sum edge" is $x_i + x_j \in \mathbb{Q}$, and for a "product edge" is $x_i x_j \in \mathbb{Q}$. I was working in the specific framework of $x_i = a_i + b_i\sqrt{d}$, but maybe there are other constructions.

Let me think about the 5-cycle more carefully. We need 5 type I values with:
- Product edges: $(1,2), (2,3), (3,4), (4,5), (5,1)$ — these have $x_i x_j \in \mathbb{Q}$.
- Sum edges: $(1,3), (1,4), (2,4), (2,5), (3,5)$ — these have $x_i + x_j \in \mathbb{Q}$.

From product edges: $x_1 x_2 = r_1, x_2 x_3 = r_2, x_3 x_4 = r_3, x_4 x_5 = r_4, x_5 x_1 = r_5$ (all rational).

From these: $x_1/x_3 = r_1/r_2$, $x_3/x_5 = r_3/r_4$, $x_5/x_1 = r_5/r_1$... wait, $x_5 x_1 = r_5$, so $x_1/x_5 = r_5/x_5^2$... hmm, let me think differently.

$x_1 x_2 = r_1, x_2 x_3 = r_2 \Rightarrow x_1/x_3 = r_1/r_2 \in \mathbb{Q}$. So $x_1 = q_{13} x_3$ for rational $q_{13} = r_1/r_2$.

Similarly, $x_3 x_4 = r_3, x_4 x_5 = r_4 \Rightarrow x_3/x_5 = r_3/r_4 \in \mathbb{Q}$. So $x_3 = q_{35} x_5$.

And $x_5 x_1 = r_5 \Rightarrow x_5 x_1 = r_5$. With $x_1 = q_{13} x_3 = q_{13} q_{35} x_5$, we get $q_{13} q_{35} x_5^2 = r_5$, so $x_5^2 = r_5 / (q_{13} q_{35}) \in \mathbb{Q}$.

But $x_5$ is type I, so $x_5^2 \notin \mathbb{Q}$. Contradiction!

So the 5-cycle product graph is impossible! Going around an odd cycle of product edges forces a square to be rational.

More generally, any odd cycle of product edges among type I values is impossible. So the product graph must be bipartite (no odd cycles).

Similarly, let me check: can the sum graph have odd cycles? If $x_i + x_j, x_j + x_k, x_k + x_i$ are all rational (a triangle), then all are rational. So no triangle in the sum graph. But what about longer odd cycles?

Consider a 5-cycle in the sum graph: $x_1 + x_2, x_2 + x_3, x_3 + x_4, x_4 + x_5, x_5 + x_1$ all rational. Then $x_1 - x_3 = (x_1 + x_2) - (x_2 + x_3) \in \mathbb{Q}$, $x_3 - x_5 = (x_3 + x_4) - (x_4 + x_5) \in \mathbb{Q}$, $x_5 + x_1 \in \mathbb{Q}$. So $x_1 = x_3 + q_1 = x_5 + q_1 + q_2$ for rational $q_1, q_2$. And $x_5 + x_1 = x_5 + x_5 + q_1 + q_2 = 2x_5 + q_1 + q_2 \in \mathbb{Q}$, so $x_5 \in \mathbb{Q}$. Contradiction.

So odd cycles in the sum graph also force rationality. The sum graph must also be bipartite.

So both the product graph and the sum graph are bipartite (among type I values). Since their union is the complete graph, and both are bipartite...

A bipartite graph on $n$ vertices has at most $n^2/4$ edges. The complete graph has $n(n-1)/2$ edges. If both $G_P$ and $G_S$ are bipartite, and $G_P \cup G_S = K_n$, then:

$n(n-1)/2 \leq |E(G_P)| + |E(G_S)| \leq n^2/4 + n^2/4 = n^2/2$.

So $n(n-1)/2 \leq n^2/2$, giving $n-1 \leq n$, always true. Not helpful.

But we can use a stronger result. If $G_P$ is bipartite with parts $A, B$, and $G_S$ is bipartite with parts $C, D$, then every edge of $K_n$ is in $G_P$ or $G_S$. 

Consider the four sets $A \cap C, A \cap D, B \cap C, B \cap D$. An edge within $A \cap C$ is not in $G_P$ (same part of $G_P$'s bipartition) and not in $G_S$ (same part of $G_S$'s bipartition). So there can be no edge within $A \cap C$, meaning $|A \cap C| \leq 1$. Similarly, $|A \cap D| \leq 1, |B \cap C| \leq 1, |B \cap D| \leq 1$.

So $n = |A \cap C| + |A \cap D| + |B \cap C| + |B \cap D| \leq 4$.

So among type I values, we can have at most 4!

Wait, but I need to be more careful. The bipartitions of $G_P$ and $G_S$ might not be unique (if the graphs are disconnected). Let me think about this.

$G_P$ is bipartite, so it has a 2-coloring (say red/blue) with no monochromatic edges. $G_S$ is bipartite, so it has a 2-coloring (say green/yellow) with no monochromatic edges. Every edge of $K_n$ is in $G_P$ or $G_S$ (or both).

Now, consider the four groups based on the two 2-colorings: (red, green), (red, yellow), (blue, green), (blue, yellow). Within any group, there are no $G_P$-edges (same red/blue color) and no $G_S$-edges (same green/yellow color). So there are no edges at all within any group. Since the graph is complete, each group has at most 1 vertex. So $n \leq 4$.

This is a clean argument! So at most 4 type I values.

Now, can we achieve 4 type I values? And can we add type R values to get more total values?

Let me first check if 4 type I values is achievable. We need $G_P$ and $G_S$ both bipartite, with $G_P \cup G_S = K_4$. The four groups are singletons: one vertex in each of (red, green), (red, yellow), (blue, green), (blue, yellow).

$G_P$ edges: between red and blue, i.e., between {(red,green), (red,yellow)} and {(blue,green), (blue,yellow)}. So edges: (rg, bg), (rg, by), (ry, bg), (ry, by). That's $K_{2,2}$, which is a 4-cycle.

$G_S$ edges: between green and yellow, i.e., between {(red,green), (blue,green)} and {(red,yellow), (blue,yellow)}. So edges: (rg, ry), (rg, by), (bg, ry), (bg, by). Also $K_{2,2}$.

Together: $G_P \cup G_S$ = all 6 edges of $K_4$. ✓

The edges that are in both $G_P$ and $G_S$: (rg, by) and (ry, bg). These are the "diagonal" edges.

So the structure is:
- Vertices: 1=(rg), 2=(ry), 3=(bg), 4=(by).
- Product edges: (1,3), (1,4), (2,3), (2,4) — i.e., $x_1 x_3, x_1 x_4, x_2 x_3, x_2 x_4 \in \mathbb{Q}$.
- Sum edges: (1,2), (1,4), (2,3), (3,4) — i.e., $x_1 + x_2, x_1 + x_4, x_2 + x_3, x_3 + x_4 \in \mathbb{Q}$.
- Both: (1,4) and (2,3).

Let me verify: 
- $G_P$ edges: {1,3}, {1,4}, {2,3}, {2,4}. This is $K_{2,2}$ with parts {1,2} and {3,4}. Bipartite. ✓
- $G_S$ edges: {1,2}, {1,4}, {2,3}, {3,4}. This is $K_{2,2}$ with parts {1,3} and {2,4}. Bipartite. ✓
- Union: all 6 edges. ✓

Now let me construct actual values. Using the $a + b\sqrt{d}$ framework:

- Product edge: $v_i = -v_j$.
- Sum edge: $u_i = -u_j$.

Vertices: 1=(rg), 2=(ry), 3=(bg), 4=(by).

$G_P$ bipartition: {1,2} (red) and {3,4} (blue). Product edges between {1,2} and {3,4}.
$G_S$ bipartition: {1,3} (green) and {2,4} (yellow). Sum edges between {1,3} and {2,4}.

For product edges ($v_i = -v_j$): $v_1 = -v_3, v_1 = -v_4, v_2 = -v_3, v_2 = -v_4$.
From $v_1 = -v_3$ and $v_2 = -v_3$: $v_1 = v_2$. From $v_1 = -v_4$ and $v_2 = -v_4$: $v_1 = v_2$. Consistent. So $v_1 = v_2$ and $v_3 = v_4 = -v_1$.

For sum edges ($u_i = -u_j$): $u_1 = -u_2, u_1 = -u_4, u_2 = -u_3, u_3 = -u_4$.
From $u_1 = -u_2$ and $u_2 = -u_3$: $u_1 = u_3$. From $u_3 = -u_4$ and $u_1 = -u_4$: $u_1 = u_3$. Consistent. So $u_1 = u_3$ and $u_2 = u_4 = -u_1$.

So: $u_1 = u_3 = a$, $u_2 = u_4 = -a$, $v_1 = v_2 = b$, $v_3 = v_4 = -b$.

The four values:
- $x_1 = a(b + \sqrt{d})$
- $x_2 = -a(b + \sqrt{d})$
- $x_3 = a(-b + \sqrt{d}) = a(\sqrt{d} - b)$
- $x_4 = -a(-b + \sqrt{d}) = -a(\sqrt{d} - b) = a(b - \sqrt{d})$

Wait, $x_2 = -a(b + \sqrt{d}) = -x_1$. But the problem requires pairwise distinct non-zero values. $x_2 = -x_1$ is fine (distinct as long as $x_1 \neq 0$, which it is). But let me check all pairs:

$x_1 = a(b + \sqrt{d})$, $x_2 = -a(b + \sqrt{d})$, $x_3 = a(\sqrt{d} - b)$, $x_4 = a(b - \sqrt{d}) = -a(\sqrt{d} - b) = -x_3$.

So $x_1 = -x_2$ and $x_3 = -x_4$. Are $x_1, x_3$ distinct? $x_1 = a(b + \sqrt{d})$, $x_3 = a(\sqrt{d} - b)$. These are equal iff $b + \sqrt{d} = \sqrt{d} - b$, i.e., $b = 0$. But $b \neq 0$ (since $v_i \neq 0$). So $x_1 \neq x_3$. ✓

Are all four distinct? $x_1 \neq x_2$ (since $x_1 \neq 0$), $x_3 \neq x_4$ (since $x_3 \neq 0$), $x_1 \neq x_3$ (shown), $x_1 \neq x_4$ (since $x_1 = -x_4$ would mean $a(b+\sqrt{d}) = -a(\sqrt{d}-b) = a(b-\sqrt{d})$, so $b+\sqrt{d} = b-\sqrt{d}$, so $\sqrt{d} = 0$, impossible). Similarly $x_2 \neq x_3, x_2 \neq x_4$. ✓

All non-zero: $x_i = 0$ would require $b + \sqrt{d} = 0$ or $\sqrt{d} - b = 0$, i.e., $\sqrt{d} = \mp b$, impossible since $\sqrt{d}$ is irrational and $b$ is rational. ✓

All $x_i^2$ irrational: $x_i^2 = a^2(b \pm \sqrt{d})^2 = a^2(b^2 + d \pm 2b\sqrt{d})$. Since $b \neq 0$ and $\sqrt{d}$ is irrational, $2b\sqrt{d}$ is irrational, so $x_i^2$ is irrational. ✓

Now let me verify the conditions:
- $x_1 x_3 = a^2(b+\sqrt{d})(\sqrt{d}-b) = a^2(d - b^2) \in \mathbb{Q}$. ✓
- $x_1 x_4 = a^2(b+\sqrt{d})(b-\sqrt{d}) = a^2(b^2 - d) \in \mathbb{Q}$. ✓
- $x_2 x_3 = (-a)(a)(b+\sqrt{d})(\sqrt{d}-b) = -a^2(d-b^2) \in \mathbb{Q}$. ✓
- $x_2 x_4 = (-a)(a)(b+\sqrt{d})(b-\sqrt{d}) = -a^2(b^2-d) \in \mathbb{Q}$. ✓
- $x_1 + x_2 = a(b+\sqrt{d}) - a(b+\sqrt{d}) = 0 \in \mathbb{Q}$. ✓
- $x_3 + x_4 = a(\sqrt{d}-b) + a(b-\sqrt{d}) = 0 \in \mathbb{Q}$. ✓
- $x_1 + x_4 = a(b+\sqrt{d}) + a(b-\sqrt{d}) = 2ab \in \mathbb{Q}$. ✓
- $x_2 + x_3 = -a(b+\sqrt{d}) + a(\sqrt{d}-b) = -2ab \in \mathbb{Q}$. ✓

All conditions satisfied. So 4 type I values is achievable.

Now, can we add type R values (with $x_i^2 \in \mathbb{Q}$) to the set? We need all 10 values to be pairwise distinct, non-zero, irrational, and for each pair, either sum or product is rational.

Type R values have $x_i^2 \in \mathbb{Q}$, so $x_i = \pm\sqrt{q_i}$ for positive rational $q_i$ (and $x_i$ irrational, so $q_i$ is not a perfect square of a rational).

Let me think about what type R values can coexist with the 4 type I values.

Let me use the specific construction: $d = 2$, $a = 1$, $b = 1$.
- $x_1 = 1 + \sqrt{2}$
- $x_2 = -(1 + \sqrt{2})$
- $x_3 = \sqrt{2} - 1$
- $x_4 = 1 - \sqrt{2} = -(\sqrt{2} - 1)$

Now, consider adding a type R value $y = \sqrt{q}$ (or $-\sqrt{q}$) for some positive rational $q$ (not a perfect square).

For each pair $(y, x_i)$, we need $y + x_i \in \mathbb{Q}$ or $y \cdot x_i \in \mathbb{Q}$.

$y \cdot x_1 = \sqrt{q}(1 + \sqrt{2}) = \sqrt{q} + \sqrt{2q}$. This is rational iff $\sqrt{q} + \sqrt{2q} \in \mathbb{Q}$. If $q = 2k^2$ for rational $k$, then $\sqrt{q} = k\sqrt{2}$ and $\sqrt{2q} = 2k$, so $\sqrt{q} + \sqrt{2q} = k\sqrt{2} + 2k$, which is irrational. Hmm.

Actually, $\sqrt{q} + \sqrt{2q}$ is rational iff both $\sqrt{q}$ and $\sqrt{2q}$ are rational, which happens iff $q$ is a perfect square of a rational and $2q$ is too, i.e., $q = r^2$ and $2q = s^2$ for rationals $r, s$. Then $s^2 = 2r^2$, so $s/r = \sqrt{2}$, impossible for rationals. So $y \cdot x_1$ is never rational (for type R $y$).

$y + x_1 = \sqrt{q} + 1 + \sqrt{2}$. This is rational iff $\sqrt{q} + \sqrt{2}$ is rational. This happens iff $\sqrt{q} = r - \sqrt{2}$ for some rational $r$, i.e., $q = r^2 + 2 - 2r\sqrt{2}$. For $q$ rational, we need $r = 0$, giving $q = 2$. So $y = \sqrt{2}$.

Let me check: $y = \sqrt{2}$, $y + x_1 = \sqrt{2} + 1 + \sqrt{2} = 1 + 2\sqrt{2}$, irrational. Hmm, that's not rational.

Wait, I think I made an error. $\sqrt{q} + \sqrt{2}$ is rational iff $\sqrt{q} = r - \sqrt{2}$ for rational $r$. Then $q = (r - \sqrt{2})^2 = r^2 + 2 - 2r\sqrt{2}$. For $q$ to be rational, $r = 0$, giving $q = 2$ and $\sqrt{q} = \sqrt{2}$. Then $\sqrt{q} + \sqrt{2} = 2\sqrt{2}$, which is irrational. So actually $\sqrt{q} + \sqrt{2}$ is never rational (for $q$ a positive rational that's not a perfect square).

Hmm, so $y + x_1$ is never rational and $y \cdot x_1$ is never rational? That means no type R value can coexist with $x_1$?

Wait, let me reconsider. Maybe I should use a different $d$ or different type I values.

Actually, the issue is that my type I values are of the form $a + b\sqrt{d}$, and a type R value is $\pm\sqrt{q}$. For $y + x_i$ to be rational, we need $\sqrt{q} + a_i + b_i\sqrt{d} \in \mathbb{Q}$, i.e., $\sqrt{q} + b_i\sqrt{d} \in \mathbb{Q}$ (since $a_i$ is rational). This requires $\sqrt{q} = r - b_i\sqrt{d}$ for rational $r$, so $q = r^2 + b_i^2 d - 2rb_i\sqrt{d}$, requiring $r = 0$ (for $q$ rational), so $q = b_i^2 d$ and $\sqrt{q} = |b_i|\sqrt{d}$. Then $\sqrt{q} + b_i\sqrt{d} = (|b_i| + b_i)\sqrt{d}$, which is $2|b_i|\sqrt{d}$ (if $b_i > 0$) or $0$ (if $b_i < 0$). So it's rational only if $b_i < 0$, giving $\sqrt{q} + b_i\sqrt{d} = 0$, i.e., $y = -b_i\sqrt{d} = |b_i|\sqrt{d}$.

So $y + x_i$ is rational only if $y = |b_i|\sqrt{d}$ and $b_i < 0$ (so $y = -b_i\sqrt{d}$), giving $y + x_i = a_i \in \mathbb{Q}$.

For $y \cdot x_i$ to be rational: $y \cdot x_i = \sqrt{q}(a_i + b_i\sqrt{d}) = a_i\sqrt{q} + b_i\sqrt{qd}$. This is rational iff $a_i\sqrt{q} + b_i\sqrt{qd} \in \mathbb{Q}$. If $q = c^2 d$ for rational $c$, then $\sqrt{q} = c\sqrt{d}$ and $\sqrt{qd} = cd$, so $y \cdot x_i = a_i c\sqrt{d} + b_i cd$. This is rational iff $a_i c = 0$, i.e., $a_i = 0$ (since $c \neq 0$). But $a_i \neq 0$ for type I values. So $y \cdot x_i$ is not rational in this case.

If $q \neq c^2 d$ for any rational $c$, then $\sqrt{q}$ and $\sqrt{qd}$ are linearly independent over $\mathbb{Q}$ (assuming $q$ and $d$ are such that $q, d, qd$ are not perfect squares). Then $a_i\sqrt{q} + b_i\sqrt{qd} \in \mathbb{Q}$ requires $a_i = 0$ and $b_i = 0$, impossible.

Hmm, so it seems like for type I values of the form $a + b\sqrt{d}$ with $a \neq 0$, the only type R values that can coexist are those with $y = -b_i\sqrt{d}$ (for the sum to be rational), and these are specific to each $x_i$.

In our construction: $x_1 = 1 + \sqrt{2}$ ($a_1 = 1, b_1 = 1$), $x_2 = -1 - \sqrt{2}$ ($a_2 = -1, b_2 = -1$), $x_3 = -1 + \sqrt{2}$ ($a_3 = -1, b_3 = 1$), $x_4 = 1 - \sqrt{2}$ ($a_4 = 1, b_4 = -1$).

For $y + x_i$ to be rational, we need $y = -b_i\sqrt{d}$ (with $b_i < 0$... actually I think I need to redo this).

$y + x_i = \sqrt{q} + a_i + b_i\sqrt{d}$. For this to be rational, $\sqrt{q} + b_i\sqrt{d} \in \mathbb{Q}$. As computed, this requires $\sqrt{q} = -b_i\sqrt{d}$, i.e., $q = b_i^2 d$ and $y = -b_i\sqrt{d}$ (note: $y = \sqrt{q} = |b_i|\sqrt{d}$, and we need $y = -b_i\sqrt{d}$, so $|b_i| = -b_i$, i.e., $b_i < 0$; if $b_i > 0$, then $y = b_i\sqrt{d} = \sqrt{q}$ and $\sqrt{q} + b_i\sqrt{d} = 2b_i\sqrt{d}$, irrational).

Wait, I think I need to be more careful. $y$ could be $\sqrt{q}$ or $-\sqrt{q}$. Let me write $y = \epsilon\sqrt{q}$ where $\epsilon = \pm 1$.

$y + x_i = \epsilon\sqrt{q} + a_i + b_i\sqrt{d}$. Rational iff $\epsilon\sqrt{q} + b_i\sqrt{d} \in \mathbb{Q}$, iff $\epsilon\sqrt{q} = r - b_i\sqrt{d}$ for rational $r$. Then $q = (r - b_i\sqrt{d})^2/\epsilon^2 = (r - b_i\sqrt{d})^2$ (since $\epsilon^2 = 1$). So $q = r^2 + b_i^2 d - 2rb_i\sqrt{d}$. For $q$ rational, $r = 0$, giving $q = b_i^2 d$ and $\epsilon\sqrt{q} = -b_i\sqrt{d}$, i.e., $y = -b_i\sqrt{d}$.

So $y = -b_i\sqrt{d}$ (and $y^2 = b_i^2 d \in \mathbb{Q}$, so $y$ is type R).

For each $x_i$, the unique type R value that makes $y + x_i$ rational is $y = -b_i\sqrt{d}$.

In our construction:
- $x_1$: $b_1 = 1$, so $y = -\sqrt{2}$.
- $x_2$: $b_2 = -1$, so $y = \sqrt{2}$.
- $x_3$: $b_3 = 1$, so $y = -\sqrt{2}$.
- $x_4$: $b_4 = -1$, so $y = \sqrt{2}$.

So the only type R values that can pair with our type I values (via rational sum) are $\sqrt{2}$ and $-\sqrt{2}$.

Now, can we add both $\sqrt{2}$ and $-\sqrt{2}$ to our set? We need to check all pairs:

- $\sqrt{2}$ and $-\sqrt{2}$: $\sqrt{2} + (-\sqrt{2}) = 0 \in \mathbb{Q}$. ✓
- $\sqrt{2}$ and $x_1 = 1 + \sqrt{2}$: $\sqrt{2} + 1 + \sqrt{2} = 1 + 2\sqrt{2}$, irrational. $\sqrt{2} \cdot (1 + \sqrt{2}) = \sqrt{2} + 2$, irrational. Neither rational! ✗

So $\sqrt{2}$ can't coexist with $x_1$! Because $b_1 = 1 > 0$, and $y = -b_1\sqrt{d} = -\sqrt{2}$, not $\sqrt{2}$.

Let me check $-\sqrt{2}$ with $x_1$: $-\sqrt{2} + 1 + \sqrt{2} = 1 \in \mathbb{Q}$. ✓

And $\sqrt{2}$ with $x_2 = -1 - \sqrt{2}$: $\sqrt{2} + (-1 - \sqrt{2}) = -1 \in \mathbb{Q}$. ✓

$-\sqrt{2}$ with $x_2$: $-\sqrt{2} + (-1 - \sqrt{2}) = -1 - 2\sqrt{2}$, irrational. $(-\sqrt{2})(-1-\sqrt{2}) = \sqrt{2} + 2$, irrational. ✗

So $-\sqrt{2}$ can't coexist with $x_2$.

So we can add $\sqrt{2}$ (pairs with $x_2$ and $x_4$ via sum) or $-\sqrt{2}$ (pairs with $x_1$ and $x_3$ via sum), but not both (since $\sqrt{2}$ doesn't pair with $x_1$ or $x_3$, and $-\sqrt{2}$ doesn't pair with $x_2$ or $x_4$).

Wait, let me recheck. $\sqrt{2}$ with $x_3 = -1 + \sqrt{2}$: $\sqrt{2} + (-1 + \sqrt{2}) = -1 + 2\sqrt{2}$, irrational. $\sqrt{2} \cdot (-1 + \sqrt{2}) = -\sqrt{2} + 2$, irrational. ✗

$\sqrt{2}$ with $x_4 = 1 - \sqrt{2}$: $\sqrt{2} + 1 - \sqrt{2} = 1 \in \mathbb{Q}$. ✓

So $\sqrt{2}$ pairs with $x_2$ and $x_4$ (via sum), but not with $x_1$ or $x_3$.
$-\sqrt{2}$ pairs with $x_1$ and $x_3$ (via sum), but not with $x_2$ or $x_4$.

So we can add at most one of $\{\sqrt{2}, -\sqrt{2}\}$, and it only pairs with 2 of the 4 type I values. We can't add it because it fails to pair with the other 2.

Hmm, so with this specific construction, we can't add any type R value. Let me think about whether a different construction would allow type R values.

Actually, let me think more generally. Suppose we have type I values and want to add a type R value $y$ (with $y^2 \in \mathbb{Q}$, $y$ irrational). For each type I value $x_i$, we need $y + x_i \in \mathbb{Q}$ or $y \cdot x_i \in \mathbb{Q}$.

If $y \cdot x_i \in \mathbb{Q}$, then $x_i = r/y$ for rational $r$, and $x_i^2 = r^2/y^2 = r^2/q \in \mathbb{Q}$ (where $y^2 = q$). But $x_i$ is type I, so $x_i^2 \notin \mathbb{Q}$. Contradiction. So $y \cdot x_i \notin \mathbb{Q}$ for type I $x_i$.

Therefore, for each type I $x_i$, we need $y + x_i \in \mathbb{Q}$. This means $x_i = s_i - y$ for rational $s_i$, i.e., all type I values differ from $-y$ by rationals. So $x_i = -y + q_i$ for rational $q_i$.

But then for two type I values $x_i = -y + q_i$ and $x_j = -y + q_j$:
- $x_i + x_j = -2y + q_i + q_j$. Rational iff $y \in \mathbb{Q}$, contradiction. So $x_i + x_j \notin \mathbb{Q}$ (for $i \neq j$).
- $x_i x_j = (-y + q_i)(-y + q_j) = y^2 - (q_i + q_j)y + q_i q_j = q - (q_i + q_j)y + q_i q_j$ (where $y^2 = q \in \mathbb{Q}$). Rational iff $(q_i + q_j)y \in \mathbb{Q}$, i.e., $q_i + q_j = 0$ (since $y$ is irrational).

So for all pairs of type I values, we need $q_i + q_j = 0$, i.e., $q_j = -q_i$. But with 3+ type I values, we can't have all pairs satisfying $q_i + q_j = 0$ (since $q_1 = -q_2, q_1 = -q_3$ gives $q_2 = q_3$, and then $q_2 + q_3 = 2q_2 \neq 0$ unless $q_2 = 0$, but then $x_2 = -y$, which is type R, contradiction).

So with a type R value in the set, we can have at most 2 type I values!

Let me verify: with 2 type I values $x_1 = -y + q, x_2 = -y - q$ (where $q \neq 0$ rational):
- $x_1 + x_2 = -2y$, irrational. $x_1 x_2 = (-y+q)(-y-q) = y^2 - q^2 = q_0 - q^2 \in \mathbb{Q}$ (where $y^2 = q_0$). ✓
- $x_1^2 = y^2 - 2qy + q^2 = q_0 + q^2 - 2qy$. Irrational (since $y$ irrational, $q \neq 0$). ✓
- $x_2^2 = y^2 + 2qy + q^2 = q_0 + q^2 + 2qy$. Irrational. ✓

And $y + x_1 = q \in \mathbb{Q}$, $y + x_2 = -q \in \mathbb{Q}$. ✓

So with 1 type R value, we can have at most 2 type I values. That gives 2 irrational squares.

Now, can we have multiple type R values? Let's say we have type R values $y_1, \ldots, y_m$ (all with $y_k^2 \in \mathbb{Q}$, all irrational) and type I values $x_1, \ldots, x_p$.

Among type R values: $y_i y_j \in \mathbb{Q}$ (since $y_i^2, y_j^2 \in \mathbb{Q}$ implies $y_i y_j = \pm\sqrt{y_i^2 y_j^2} \in \mathbb{Q}$... wait, no. $y_i y_j = \epsilon_i \sqrt{q_i} \cdot \epsilon_j \sqrt{q_j} = \epsilon_i \epsilon_j \sqrt{q_i q_j}$. This is rational iff $q_i q_j$ is a perfect square of a rational. Not always.

Hmm, so among type R values, we need for each pair either $y_i + y_j \in \mathbb{Q}$ or $y_i y_j \in \mathbb{Q}$.

$y_i = \epsilon_i \sqrt{q_i}$, $y_j = \epsilon_j \sqrt{q_j}$.
$y_i + y_j = \epsilon_i \sqrt{q_i} + \epsilon_j \sqrt{q_j}$. Rational iff $\sqrt{q_i}$ and $\sqrt{q_j}$ are rational multiples of each other and the signs work out. Specifically, if $q_i/q_j = (r/s)^2$ for rationals $r, s$, then $\sqrt{q_i} = (r/s)\sqrt{q_j}$, and $y_i + y_j = (\epsilon_i r/s + \epsilon_j)\sqrt{q_j}$, rational iff $\epsilon_i r/s + \epsilon_j = 0$, i.e., $\epsilon_i r = -\epsilon_j s$.

$y_i y_j = \epsilon_i \epsilon_j \sqrt{q_i q_j}$. Rational iff $q_i q_j$ is a perfect square of a rational.

This is getting complicated. Let me think about the overall problem differently.

We want to maximize the number of type I values (irrational squares). We've shown:
1. Without type R values: at most 4 type I values (and 4 is achievable).
2. With type R values: at most 2 type I values (per type R value? or total?).

Wait, I showed that with ANY type R value in the set, all type I values must be of the form $-y + q_i$, and there can be at most 2 such type I values. But what if there are multiple type R values?

If there are two type R values $y_1, y_2$, then each type I value $x_i$ must satisfy $x_i + y_1 \in \mathbb{Q}$ and $x_i + y_2 \in \mathbb{Q}$ (since $x_i \cdot y_k \notin \mathbb{Q}$ for type I $x_i$ and type R $y_k$). So $x_i = -y_1 + q_i = -y_2 + q_i'$, giving $y_2 - y_1 = q_i - q_i' \in \mathbb{Q}$. So $y_2 - y_1 \in \mathbb{Q}$.

Also, $y_1 + y_2 \in \mathbb{Q}$ or $y_1 y_2 \in \mathbb{Q}$.

If $y_2 - y_1 \in \mathbb{Q}$ and $y_1 + y_2 \in \mathbb{Q}$, then $y_1, y_2 \in \mathbb{Q}$, contradiction. So $y_1 y_2 \in \mathbb{Q}$.

$y_2 = y_1 + r$ for rational $r$, and $y_1 y_2 = y_1(y_1 + r) = y_1^2 + ry_1 = q_1 + ry_1 \in \mathbb{Q}$, so $ry_1 \in \mathbb{Q}$, so $y_1 \in \mathbb{Q}$ (if $r \neq 0$), contradiction. If $r = 0$, $y_1 = y_2$, but they must be distinct        — AI历史解题过程（thinking）
#   polymath_00062         — 题目ID

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
  <problem_id>polymath_00062</problem_id>
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

Ten pairwise distinct non-zero real numbers $x_1, x_2, \dots, x_{10}$ are such that for any two distinct indices $i, j \in \{1, \dots, 10\}$, either their sum $x_i + x_j$ or their product $x_i x_j$ is a rational number. Let $S = \{x_1^2, x_2^2, \dots, x_{10}^2\}$. Determine the maximum possible number of irrational values in the set $S$.

## Standard Solution

The original proof shows that for any such set of ten numbers, the squares of all numbers must be rational. This is proven by considering the relationship between numbers as edges in a graph and applying Ramsey's theorem to find a monochromatic triangle (either a set of three numbers where all pairwise sums are rational, or all pairwise products are rational). In the case of a rational sum triangle, it's shown that all numbers must be rational. In the case of a rational product triangle, it's shown that all squares must be rational. Therefore, all $x_i^2$ are rational, meaning the number of irrational values in $S$ must be 0.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully. We have 10 pairwise distinct non-zero real numbers $x_1, \ldots, x_{10}$ such that for any two distinct indices $i, j$, either $x_i + x_j$ or $x_i x_j$ is rational. We need to find the maximum number of irrational values in $S = \{x_1^2, \ldots, x_{10}^2\}$.

Let me think about this carefully.

First, let me understand the structure. For each pair $(i,j)$, at least one of $x_i + x_j$ or $x_i x_j$ is rational.

Let me categorize the $x_i$ values. Let's say $x_i$ is "rational" if $x_i \in \mathbb{Q}$, and "irrational" otherwise.

If $x_i$ and $x_j$ are both rational, then both $x_i + x_j$ and $x_i x_j$ are rational. Fine.

If $x_i$ is rational and $x_j$ is irrational: $x_i + x_j$ is irrational (since $x_j$ is irrational), so we need $x_i x_j$ to be rational. Since $x_i \neq 0$ is rational, $x_i x_j$ rational means $x_j$ is rational, contradiction. So actually, if $x_i$ is rational and $x_j$ is irrational, $x_i x_j$ is irrational, and $x_i + x_j$ is irrational. That's a problem!

Wait, let me reconsider. If $x_i$ is rational (nonzero) and $x_j$ is irrational, then:
- $x_i + x_j$ is irrational
- $x_i x_j$ is irrational (since $x_i \neq 0$ is rational, $x_i x_j$ rational would imply $x_j$ rational)

So neither is rational! This means we cannot have a rational $x_i$ and an irrational $x_j$ in the set simultaneously.

So either all $x_i$ are rational, or all $x_i$ are irrational.

If all are rational, then $S$ has all rational values, so 0 irrational values.

If all are irrational, we need to analyze the constraint more carefully.

So all $x_i$ are irrational, and for each pair, either $x_i + x_j$ or $x_i x_j$ is rational.

Now, $x_i^2$ is irrational iff $x_i$ is not of the form $\pm\sqrt{q}$ for rational $q$... wait, no. $x_i^2$ is irrational means $x_i^2 \notin \mathbb{Q}$.

Actually, let me think about when $x_i^2$ is rational. $x_i^2$ is rational iff $x_i = \pm\sqrt{q}$ for some positive rational $q$ (or $x_i$ rational, but we've excluded that case). So $x_i^2$ is irrational means $x_i$ is not of the form $\pm\sqrt{q}$ for rational $q > 0$.

We want to maximize the number of $x_i$ with $x_i^2$ irrational.

Let me think about the structure of the set when all $x_i$ are irrational.

For each pair $(i,j)$, either $x_i + x_j \in \mathbb{Q}$ or $x_i x_j \in \mathbb{Q}$.

Let me define a graph on the 10 elements. Color edge $(i,j)$ "sum" if $x_i + x_j \in \mathbb{Q}$, and "product" if $x_i x_j \in \mathbb{Q}$ (and both if both are rational).

Let me think about what structures are possible.

Case 1: $x_i + x_j \in \mathbb{Q}$ for all pairs.
This means all $x_i$ are of the form $q_i + \alpha$ for some fixed irrational $\alpha$ and rational $q_i$. Wait, let me check. If $x_i + x_j \in \mathbb{Q}$ for all $i, j$, then $x_i + x_j = r_{ij} \in \mathbb{Q}$. Then $x_i - x_k = (x_i + x_j) - (x_j + x_k) = r_{ij} - r_{jk} \in \mathbb{Q}$. So all $x_i$ differ by rationals. So $x_i = \alpha + q_i$ for some fixed $\alpha$ (irrational) and rational $q_i$.

Then $x_i^2 = (\alpha + q_i)^2 = \alpha^2 + 2q_i\alpha + q_i^2$. This is rational iff $\alpha^2 + 2q_i\alpha$ is rational, i.e., $\alpha^2 \in \mathbb{Q}$ and $q_i = 0$ (if $\alpha \notin \mathbb{Q}$, then $2q_i\alpha$ is rational only if $q_i = 0$). Wait, $\alpha^2 + 2q_i\alpha$ is rational. If $\alpha^2$ is rational, then $2q_i\alpha$ must be rational, so $q_i = 0$ (since $\alpha$ is irrational). So $x_i^2$ is rational only when $q_i = 0$, i.e., $x_i = \alpha$.

If $\alpha^2$ is irrational, then $x_i^2$ is always irrational (since $\alpha^2 + 2q_i\alpha + q_i^2$ with $\alpha^2$ irrational and $2q_i\alpha$ irrational (for $q_i \neq 0$) or $0$ (for $q_i = 0$)... wait, for $q_i = 0$, $x_i^2 = \alpha^2$ which is irrational. For $q_i \neq 0$, $x_i^2 = \alpha^2 + 2q_i\alpha + q_i^2$. Is this rational? $\alpha^2$ is irrational, $2q_i\alpha$ is irrational, so the sum could be rational if they cancel. But $\alpha^2$ and $2q_i\alpha$ are both irrational; their sum being rational requires $\alpha^2 + 2q_i\alpha \in \mathbb{Q}$, i.e., $\alpha(\alpha + 2q_i) \in \mathbb{Q}$.

Hmm, this is getting complicated. Let me think differently.

Actually, let me think about this more carefully with specific constructions.

Let me consider the case where all pairwise sums are rational. Then $x_i = \alpha + q_i$ with $\alpha$ irrational, $q_i$ distinct rationals (since $x_i$ are distinct). We need $x_i \neq 0$, so $q_i \neq -\alpha$, which is automatically satisfied since $q_i$ is rational and $\alpha$ is irrational.

Now $x_i^2 = \alpha^2 + 2q_i\alpha + q_i^2$. For this to be rational, we need $\alpha^2 + 2q_i\alpha \in \mathbb{Q}$.

If $\alpha^2 \in \mathbb{Q}$ (say $\alpha^2 = c$), then we need $2q_i\alpha \in \mathbb{Q}$, so $q_i = 0$. Only $x_i = \alpha$ has rational square. So at most 1 rational square, meaning at least 9 irrational squares.

If $\alpha^2 \notin \mathbb{Q}$, then we need $\alpha^2 + 2q_i\alpha \in \mathbb{Q}$ for some $q_i$. This means $\alpha$ satisfies $\alpha^2 + 2q_i\alpha - r = 0$ for some rational $r$, i.e., $\alpha = -q_i \pm \sqrt{q_i^2 + r}$. So $\alpha$ is of the form $-q_i + \sqrt{q_i^2 + r}$ where $q_i^2 + r > 0$ and $\sqrt{q_i^2 + r}$ is irrational. Then $\alpha^2 = q_i^2 - 2q_i\sqrt{q_i^2+r} + (q_i^2 + r) = 2q_i^2 + r - 2q_i\sqrt{q_i^2+r}$, which is indeed irrational (if $q_i \neq 0$).

For a given $\alpha$, the values of $q$ for which $\alpha^2 + 2q\alpha \in \mathbb{Q}$ are determined: $\alpha^2 + 2q\alpha = r$ means $q = \frac{r - \alpha^2}{2\alpha}$. Since $\alpha$ is fixed and irrational, $q$ is rational iff $r - \alpha^2$ is a rational multiple of $\alpha$, i.e., $r = \alpha^2 + 2q\alpha$ for rational $q$. But this is circular.

Let me think about it differently. Given $\alpha$ irrational, $\alpha^2 + 2q\alpha \in \mathbb{Q}$ iff $q = \frac{s - \alpha^2}{2\alpha}$ for some $s \in \mathbb{Q}$. For $q$ to be rational, we need $\frac{s - \alpha^2}{2\alpha} \in \mathbb{Q}$, i.e., $s - \alpha^2 = 2q\alpha$ for rational $q$, i.e., $\alpha^2 + 2q\alpha = s \in \mathbb{Q}$. So the set of rational $q$ for which $\alpha^2 + 2q\alpha \in \mathbb{Q}$ is exactly the set of $q$ such that $\alpha^2 + 2q\alpha \in \mathbb{Q}$.

If $\alpha$ is algebraic of degree 2, say $\alpha = a + b\sqrt{d}$ with $a, b$ rational, $b \neq 0$, $d$ square-free, then $\alpha^2 = a^2 + b^2 d + 2ab\sqrt{d}$, and $2q\alpha = 2qa + 2qb\sqrt{d}$. So $\alpha^2 + 2q\alpha = (a^2 + b^2 d + 2qa) + (2ab + 2qb)\sqrt{d}$. This is rational iff $2ab + 2qb = 0$, i.e., $q = -a$. So there's exactly one rational $q$ (namely $q = -a$) for which $\alpha^2 + 2q\alpha$ is rational.

If $\alpha$ is algebraic of degree $> 2$ or transcendental, then $\alpha^2 + 2q\alpha \in \mathbb{Q}$ might have no rational solutions $q$, or it depends.

Actually, for transcendental $\alpha$: $\alpha^2 + 2q\alpha = s$ means $\alpha^2 + 2q\alpha - s = 0$. But $\alpha$ is transcendental, so it can't satisfy any polynomial equation with rational coefficients. So there's no rational $q$ and $s$ with $\alpha^2 + 2q\alpha = s$. So for transcendental $\alpha$, all $x_i^2$ are irrational. That gives 10 irrational values!

Wait, but we need all $x_i$ to be irrational and pairwise distinct, and all pairwise sums rational. With $\alpha$ transcendental and $q_i$ distinct rationals, $x_i = \alpha + q_i$ are all irrational (since $\alpha$ is irrational and $q_i$ rational), pairwise distinct (since $q_i$ distinct), non-zero (since $\alpha$ is irrational and $-q_i$ is rational). And all pairwise sums $x_i + x_j = 2\alpha + q_i + q_j$... wait, that's not rational! $2\alpha$ is irrational.

Oh wait, I made an error. If $x_i + x_j \in \mathbb{Q}$ for all $i, j$, then $x_i = \alpha + q_i$ where $\alpha$ is some fixed value and $q_i$ are rational. But $x_i + x_j = 2\alpha + q_i + q_j$. For this to be rational, $2\alpha$ must be rational, so $\alpha$ is rational. But then all $x_i$ are rational, contradiction.

Hmm, let me redo this. If $x_i + x_j \in \mathbb{Q}$ for all $i \neq j$, then take three indices $i, j, k$. We have $x_i + x_j = r_1$, $x_i + x_k = r_2$, $x_j + x_k = r_3$, all rational. Then $x_i = (r_1 + r_2 - r_3)/2 \in \mathbb{Q}$. So all $x_i$ are rational!

So the case "all pairwise sums rational" forces all $x_i$ to be rational. That's the trivial case.

OK so we can't have all sums rational (unless all are rational). So we need a mix: some pairs have rational sum, some have rational product.

Let me reconsider. We have all $x_i$ irrational. For each pair, either sum or product is rational.

Let me think about what happens with products. If $x_i x_j \in \mathbb{Q}$ for all $i, j$, then $x_i x_j = r_{ij} \in \mathbb{Q}$. Take three indices: $x_1 x_2 = r_{12}$, $x_1 x_3 = r_{13}$, $x_2 x_3 = r_{23}$. Then $x_1^2 = r_{12} r_{13} / r_{23} \in \mathbb{Q}$. So all $x_i^2 \in \mathbb{Q}$, meaning all $x_i = \pm\sqrt{q_i}$ for rational $q_i > 0$.

In this case, all $x_i^2$ are rational, so 0 irrational values. Not what we want.

So we need a mix. Let me think about the structure more carefully.

Let me partition the indices into groups based on the structure. Let me think about what constraints arise.

Consider two elements $x_i, x_j$ with $x_i x_j \in \mathbb{Q}$ (and $x_i + x_j \notin \mathbb{Q}$). And $x_i, x_k$ with $x_i x_k \in \mathbb{Q}$. Then $x_j / x_k = (x_i x_j)/(x_i x_k) \in \mathbb{Q}$. So $x_j = r \cdot x_k$ for some rational $r$.

Now consider $x_j, x_k$: we need $x_j + x_k$ or $x_j x_k$ rational. $x_j x_k = r x_k^2$. If $x_k^2 \in \mathbb{Q}$, then $x_j x_k \in \mathbb{Q}$. If $x_k^2 \notin \mathbb{Q}$, then we need $x_j + x_k = (r+1) x_k \in \mathbb{Q}$, so $x_k \in \mathbb{Q}$, contradiction. So if $x_k^2 \notin \mathbb{Q}$, we need $x_j x_k \in \mathbb{Q}$, which requires $r x_k^2 \in \mathbb{Q}$, i.e., $x_k^2 \in \mathbb{Q}$ (since $r$ is rational and nonzero). Contradiction. So actually, if $x_i x_j$ and $x_i x_k$ are both rational, and $x_k^2 \notin \mathbb{Q}$, then... we get a contradiction?

Wait, let me re-examine. We have $x_j = r x_k$ with $r$ rational. For the pair $(j, k)$: either $x_j + x_k = (r+1)x_k$ is rational, or $x_j x_k = r x_k^2$ is rational. 

If $x_k^2 \notin \mathbb{Q}$: $r x_k^2 \notin \mathbb{Q}$ (since $r \neq 0$ rational). And $(r+1)x_k \in \mathbb{Q}$ requires $x_k \in \mathbb{Q}$ (if $r \neq -1$) or $x_j + x_k = 0$ (if $r = -1$, but then $x_j = -x_k$, so $x_j + x_k = 0 \in \mathbb{Q}$). 

So if $r = -1$, i.e., $x_j = -x_k$, then $x_j + x_k = 0$ is rational. That works!

If $r \neq -1$ and $x_k^2 \notin \mathbb{Q}$: we need $(r+1)x_k \in \mathbb{Q}$, so $x_k \in \mathbb{Q}$, contradiction. So this is impossible.

So: if $x_i x_j, x_i x_k \in \mathbb{Q}$ and $x_k^2 \notin \mathbb{Q}$, then either $x_j = -x_k$ (i.e., $r = -1$) or we have a contradiction.

Interesting. So let me think about this more carefully.

Let me define the "product class" structure. Say $x_i \sim x_j$ if $x_i x_j \in \mathbb{Q}$. This isn't necessarily an equivalence relation, but let me explore.

Actually, let me think about it differently. Let me consider the values $x_i$ and group them.

Let's say a value $x_i$ has $x_i^2 \in \mathbb{Q}$ (call it "type R") or $x_i^2 \notin \mathbb{Q}$ (call it "type I").

For two type I values $x_i, x_j$: We need $x_i + x_j \in \mathbb{Q}$ or $x_i x_j \in \mathbb{Q}$.

If $x_i x_j \in \mathbb{Q}$, say $x_i x_j = r$. Then $x_j = r/x_i$. And $x_j^2 = r^2/x_i^2$. Since $x_i^2 \notin \mathbb{Q}$ and $r \in \mathbb{Q}$, $x_j^2 \notin \mathbb{Q}$. Consistent.

If $x_i + x_j \in \mathbb{Q}$, say $x_i + x_j = s$. Then $x_j = s - x_i$. And $x_j^2 = s^2 - 2sx_i + x_i^2$. For $x_j^2 \notin \mathbb{Q}$: we need $s^2 - 2sx_i + x_i^2 \notin \mathbb{Q}$. Since $x_i^2 \notin \mathbb{Q}$, and $-2sx_i$ is irrational (if $s \neq 0$), the sum $x_i^2 - 2sx_i$ could be rational or irrational. If $s = 0$, then $x_j = -x_i$ and $x_j^2 = x_i^2 \notin \mathbb{Q}$. If $s \neq 0$, it depends.

OK this is getting complex. Let me try to think about specific constructions and find the maximum.

Let me try to construct examples with many irrational squares.

**Construction attempt 1**: All $x_i$ of the form $c \cdot \sqrt{d}$ for various rational $c$ and fixed square-free $d$.

If $x_i = c_i \sqrt{d}$ with $c_i$ rational, $d$ square-free positive integer (not a perfect square), then:
- $x_i x_j = c_i c_j d \in \mathbb{Q}$ for all $i, j$. 
- $x_i^2 = c_i^2 d \notin \mathbb{Q}$ (since $d$ is not a perfect square and $c_i \neq 0$).

So all products are rational, all squares are irrational. We can have 10 distinct values $c_1\sqrt{d}, \ldots, c_{10}\sqrt{d}$ with distinct rational $c_i$. All non-zero. This gives 10 irrational squares!

Wait, but that seems too easy. Let me double-check. $x_i = c_i \sqrt{d}$, $x_j = c_j \sqrt{d}$. $x_i x_j = c_i c_j d$. Since $c_i, c_j$ are rational and $d$ is a positive integer, $c_i c_j d \in \mathbb{Q}$. Yes. And $x_i^2 = c_i^2 d$. Since $d$ is not a perfect square, $c_i^2 d \notin \mathbb{Q}$ (as $c_i \neq 0$). Yes.

So we can achieve 10 irrational values in $S$? That seems like the answer would be 10.

But wait, let me re-read the problem. "Determine the maximum possible number of irrational values in the set $S$." And $S = \{x_1^2, \ldots, x_{10}^2\}$. Note that $S$ is a set, so if some $x_i^2$ are equal, they count once. But in our construction, $x_i^2 = c_i^2 d$ and since $c_i$ are distinct, $c_i^2$ are... well, $c_i^2$ could coincide if $c_i = -c_j$. But we can choose $c_i$ to be distinct positive rationals, so $c_i^2$ are distinct, and $x_i^2$ are all distinct and all irrational. So $|S| = 10$ and all are irrational.

Hmm, but that gives 10, which seems too straightforward for a competition problem. Let me re-read the problem.

"Ten pairwise distinct non-zero real numbers $x_1, x_2, \dots, x_{10}$ are such that for any two distinct indices $i, j \in \{1, \dots, 10\}$, either their sum $x_i + x_j$ or their product $x_i x_j$ is a rational number."

OK so with $x_i = c_i \sqrt{d}$, the product $x_i x_j = c_i c_j d$ is always rational. The sum $x_i + x_j = (c_i + c_j)\sqrt{d}$ is irrational (since $c_i + c_j \neq 0$ if we choose $c_i$ all positive, and $\sqrt{d}$ is irrational). But the condition only requires ONE of sum or product to be rational, and the product is always rational. So this works.

And all $x_i^2 = c_i^2 d$ are irrational and distinct. So the answer is 10?

Wait, but this seems way too easy. Let me reconsider whether I'm missing something. Maybe the problem is asking something subtler.

Hmm, actually, re-reading: "Determine the maximum possible number of irrational values in the set $S$." Since $S$ is a set, the number of irrational values is the number of distinct irrational elements. In our construction, all 10 are distinct and irrational, so the answer is 10.

But this feels too easy for what looks like a competition problem. Let me re-examine.

Actually wait, maybe I need to reconsider. Is the problem perhaps more subtle? Let me re-read once more.

"Ten pairwise distinct non-zero real numbers" — OK.
"for any two distinct indices $i, j$, either their sum $x_i + x_j$ or their product $x_i x_j$ is a rational number" — OK.
"$S = \{x_1^2, x_2^2, \dots, x_{10}^2\}$" — this is a set, so duplicates collapse.
"Determine the maximum possible number of irrational values in the set $S$" — the number of elements of $S$ that are irrational.

With the construction $x_i = c_i \sqrt{d}$, we get 10 distinct irrational squares. So the maximum is at least 10, and since $|S| \leq 10$, the maximum is exactly 10.

Hmm, but I feel like I might be missing something. Let me reconsider whether the problem might have additional constraints I'm not seeing, or whether the answer really is 10.

Actually, wait. Let me reconsider. Maybe the problem is from a competition and the answer is indeed 10, but the proof requires showing both that 10 is achievable and that it's the maximum (which is trivially at most 10). But the construction is simple, so maybe the problem is easier than I think, or maybe I'm misunderstanding something.

Let me re-examine: is there any hidden constraint? "Ten pairwise distinct non-zero real numbers" — yes, $c_i \sqrt{d}$ are pairwise distinct if $c_i$ are distinct, and non-zero if $c_i \neq 0$. "for any two distinct indices, either sum or product is rational" — product is always rational. So the construction works.

Actually, I wonder if the problem is more interesting than I think, and maybe the answer is not 10. Let me reconsider.

Oh wait, maybe I should reconsider whether the problem is asking for the maximum over all valid configurations, or something else. No, it's clearly asking for the maximum number of irrational values in $S$.

With the construction I gave, the answer is 10. Since $S$ has at most 10 elements, 10 is the maximum.

Hmm, but let me reconsider. Maybe there's a subtlety with the set $S$. If some $x_i^2$ values coincide, $S$ could have fewer than 10 elements. But we want to MAXIMIZE the number of irrational values, so we'd want them all distinct and all irrational, which we achieved.

I think the answer is 10. Let me verify once more with a concrete example.

Take $d = 2$. Let $x_i = i\sqrt{2}$ for $i = 1, 2, \ldots, 10$. These are 10 pairwise distinct non-zero reals. For any $i \neq j$, $x_i x_j = ij \cdot 2 = 2ij \in \mathbb{Q}$. And $x_i^2 = 2i^2 \notin \mathbb{Q}$. All $x_i^2$ are distinct (since $i^2$ are distinct for $i = 1, \ldots, 10$). So $S = \{2, 8, 18, 32, 50, 72, 98, 128, 162, 200\}$, all of which are... wait, $2i^2$ for $i = 1, \ldots, 10$: $2, 8, 18, 32, 50, 72, 98, 128, 162, 200$. Are these irrational? $2 \cdot 1 = 2$ is rational! $2 \cdot 4 = 8$ is rational!

Oh no! $x_i^2 = 2i^2$ is always rational! Because $2i^2$ is a rational number (it's an integer). I made an error!

$x_i = i\sqrt{2}$, so $x_i^2 = i^2 \cdot 2 = 2i^2$, which is an integer, hence rational. So all squares are rational. That gives 0 irrational values, not 10.

I see my error now. $x_i = c_i \sqrt{d}$ gives $x_i^2 = c_i^2 d$, which is rational since $c_i$ and $d$ are rational. So all squares are rational. The construction gives 0 irrational squares, not 10.

So I was wrong. Let me reconsider.

If $x_i = c_i \sqrt{d}$, then $x_i^2 = c_i^2 d \in \mathbb{Q}$. So all products being rational forces all squares to be rational (as I showed earlier). So to get irrational squares, we need some pairs to have rational sums instead of rational products.

OK so now the problem is more interesting. Let me restart the analysis.

We have all $x_i$ irrational (as shown, we can't mix rational and irrational). For each pair, either sum or product is rational. We want to maximize the number of $x_i^2$ that are irrational.

Let me think about the structure. Let me consider the graph where we color each edge as "sum" (if $x_i + x_j \in \mathbb{Q}$) or "product" (if $x_i x_j \in \mathbb{Q}$). An edge could be both.

Key observations:
1. If $x_i x_j \in \mathbb{Q}$ and $x_i x_k \in \mathbb{Q}$, then $x_j/x_k \in \mathbb{Q}$, so $x_j = r x_k$ for rational $r$.
2. If $x_i + x_j \in \mathbb{Q}$ and $x_i + x_k \in \mathbb{Q}$, then $x_j - x_k \in \mathbb{Q}$, so $x_j = x_k + s$ for rational $s$.

Let me think about what happens with type I values (those with $x_i^2 \notin \mathbb{Q}$).

Suppose $x_i$ is type I ($x_i^2 \notin \mathbb{Q}$). Consider any other $x_j$.

Case A: $x_i x_j \in \mathbb{Q}$, say $x_i x_j = r$. Then $x_j = r/x_i$, and $x_j^2 = r^2/x_i^2 \notin \mathbb{Q}$ (since $x_i^2 \notin \mathbb{Q}$ and $r \neq 0$). So $x_j$ is also type I.

Case B: $x_i + x_j \in \mathbb{Q}$, say $x_i + x_j = s$. Then $x_j = s - x_i$, and $x_j^2 = s^2 - 2sx_i + x_i^2$. 
- If $s = 0$: $x_j = -x_i$, $x_j^2 = x_i^2 \notin \mathbb{Q}$. Type I.
- If $s \neq 0$: $x_j^2 = x_i^2 - 2sx_i + s^2$. Since $x_i^2 \notin \mathbb{Q}$ and $2sx_i \notin \mathbb{Q}$ (as $s \neq 0$ rational and $x_i$ irrational), the sum $x_i^2 - 2sx_i$ could be rational or irrational. If $x_i^2 - 2sx_i \in \mathbb{Q}$, then $x_j^2 \in \mathbb{Q}$ (type R). Otherwise, $x_j^2 \notin \mathbb{Q}$ (type I).

So a type I value $x_i$ can be connected to a type R value $x_j$ only via a rational sum with $s \neq 0$ and $x_i^2 - 2sx_i \in \mathbb{Q}$.

Now, $x_i^2 - 2sx_i \in \mathbb{Q}$ means $x_i$ satisfies $x_i^2 - 2sx_i - q = 0$ for some $q \in \mathbb{Q}$, i.e., $x_i = s \pm \sqrt{s^2 + q}$. So $x_i$ is of the form $s + \sqrt{m}$ or $s - \sqrt{m}$ where $m = s^2 + q \in \mathbb{Q}$ and $\sqrt{m}$ is irrational (so $m > 0$ and not a perfect square of a rational).

So if $x_i$ is type I and connected to a type R value via rational sum, then $x_i = s \pm \sqrt{m}$ for some rational $s$ and positive rational $m$ (with $\sqrt{m}$ irrational).

In this case, $x_i^2 = s^2 + m \pm 2s\sqrt{m}$. For $x_i^2 \notin \mathbb{Q}$, we need $s \neq 0$ (if $s = 0$, $x_i^2 = m \in \mathbb{Q}$, contradiction with type I). So $s \neq 0$.

And the type R value is $x_j = s - x_i = \mp\sqrt{m}$ (if $x_i = s \pm \sqrt{m}$, then $x_j = s - (s \pm \sqrt{m}) = \mp\sqrt{m}$). So $x_j = \mp\sqrt{m}$, and $x_j^2 = m \in \mathbb{Q}$. Consistent.

So the pair $(x_i, x_j)$ with $x_i = s + \sqrt{m}$, $x_j = -\sqrt{m}$ (or $x_i = s - \sqrt{m}$, $x_j = \sqrt{m}$) has $x_i + x_j = s \in \mathbb{Q}$, $x_i^2 \notin \mathbb{Q}$ (type I), $x_j^2 = m \in \mathbb{Q}$ (type R).

Now, let me think about the overall structure. Let me try to build a configuration with many type I values.

**Approach**: Try to have many type I values that are pairwise connected by rational products.

If $x_i, x_j$ are both type I with $x_i x_j \in \mathbb{Q}$, then as shown, $x_j = r/x_i$ for rational $r$, and $x_j^2 = r^2/x_i^2 \notin \mathbb{Q}$. Good, both stay type I.

Can we have many type I values all pairwise connected by rational products? If $x_i x_j \in \mathbb{Q}$ for all pairs among a set of type I values, then as I showed earlier, this forces all $x_i^2 \in \mathbb{Q}$ (contradiction with type I). Wait, let me recheck.

If $x_i x_j \in \mathbb{Q}$ for all $i, j$ in a subset, take three: $x_1 x_2 = r_{12}$, $x_1 x_3 = r_{13}$, $x_2 x_3 = r_{23}$. Then $x_1^2 = r_{12} r_{13} / r_{23} \in \mathbb{Q}$. So $x_1$ is type R, contradiction.

So among any three type I values, not all three pairwise products can be rational. At least one pair must have a rational sum instead.

So among type I values, we can't have a triangle of all-product edges. By Ramsey theory, this limits the structure.

Let me think about this more carefully. Among the type I values, consider the graph where we connect $i, j$ by a "product edge" if $x_i x_j \in \mathbb{Q}$, and a "sum edge" if $x_i + x_j \in \mathbb{Q}$. Every pair has at least one type of edge (possibly both).

The constraint is: no triangle of all product edges (among type I values). Actually, more precisely, among any three type I values, at least one pair has a rational sum (and possibly also a rational product, but at least the sum is rational).

Hmm wait, actually the constraint is weaker. Among any three type I values, at least one pair must have a rational sum (because if all three pairs had only rational products, we'd get all squares rational, contradiction).

But a pair could have both rational sum and rational product. Let me think about when that happens. If $x_i + x_j = s \in \mathbb{Q}$ and $x_i x_j = r \in \mathbb{Q}$, then $x_i, x_j$ are roots of $t^2 - st + r = 0$, so $x_i, x_j = \frac{s \pm \sqrt{s^2 - 4r}}{2}$. For them to be real and irrational, we need $s^2 - 4r > 0$ and $\sqrt{s^2 - 4r}$ irrational. Then $x_i^2 = \frac{s^2 + (s^2-4r) \pm 2s\sqrt{s^2-4r}}{4} = \frac{2s^2 - 4r \pm 2s\sqrt{s^2-4r}}{4}$. For $x_i^2 \notin \mathbb{Q}$, we need $s \neq 0$.

OK, this is getting complicated. Let me try a different approach and think about specific constructions.

**Construction attempt**: Let me try to have a large set of type I values.

Idea: Use values of the form $x_i = a_i + b_i \sqrt{d}$ where $a_i, b_i$ are rational, $d$ is a fixed square-free positive integer, and $b_i \neq 0$.

Then $x_i + x_j = (a_i + a_j) + (b_i + b_j)\sqrt{d}$. This is rational iff $b_i + b_j = 0$, i.e., $b_j = -b_i$.

And $x_i x_j = (a_i a_j + b_i b_j d) + (a_i b_j + a_j b_i)\sqrt{d}$. This is rational iff $a_i b_j + a_j b_i = 0$, i.e., $a_i b_j = -a_j b_i$, i.e., $a_i/b_i = -a_j/b_j$ (assuming $b_i, b_j \neq 0$), i.e., $a_i/b_i + a_j/b_j = 0$.

And $x_i^2 = (a_i^2 + b_i^2 d) + 2a_i b_i \sqrt{d}$. This is rational iff $a_i b_i = 0$, i.e., $a_i = 0$ (since $b_i \neq 0$). So $x_i^2 \notin \mathbb{Q}$ iff $a_i \neq 0$.

So for type I values (with $a_i \neq 0$), the condition for pair $(i,j)$ is:
- Sum rational: $b_i + b_j = 0$
- Product rational: $a_i/b_i + a_j/b_j = 0$ (equivalently, $a_i b_j + a_j b_i = 0$)

We need at least one of these for each pair.

Let me define $u_i = b_i$ and $v_i = a_i/b_i$ (so $a_i = u_i v_i$). Then:
- Sum rational: $u_i + u_j = 0$, i.e., $u_j = -u_i$
- Product rational: $v_i + v_j = 0$, i.e., $v_j = -v_i$

And type I means $a_i \neq 0$, i.e., $v_i \neq 0$ (since $u_i = b_i \neq 0$).

So we need: for each pair $(i,j)$, either $u_i + u_j = 0$ or $v_i + v_j = 0$.

And we want to maximize the number of pairs $(u_i, v_i)$ with $u_i \neq 0$, $v_i \neq 0$, all $x_i = u_i v_i + u_i \sqrt{d} = u_i(v_i + \sqrt{d})$ distinct and non-zero.

$x_i$ distinct: $u_i(v_i + \sqrt{d}) \neq u_j(v_j + \sqrt{d})$. Since $\sqrt{d}$ is irrational, this means $u_i v_i \neq u_j v_j$ or $u_i \neq u_j$. Actually, $u_i(v_i + \sqrt{d}) = u_j(v_j + \sqrt{d})$ iff $u_i = u_j$ and $u_i v_i = u_j v_j$ (comparing rational and irrational parts). So $x_i = x_j$ iff $u_i = u_j$ and $v_i = v_j$. So we need the pairs $(u_i, v_i)$ to be distinct.

$x_i \neq 0$: $u_i(v_i + \sqrt{d}) \neq 0$. Since $u_i \neq 0$ and $v_i + \sqrt{d} \neq 0$ (as $v_i$ is rational and $\sqrt{d}$ is irrational), this is automatic.

So the problem reduces to: find the maximum number of distinct pairs $(u_i, v_i)$ with $u_i, v_i \in \mathbb{Q} \setminus \{0\}$ such that for each pair $(i,j)$, either $u_i = -u_j$ or $v_i = -v_j$.

This is a clean combinatorial problem! Let me think about it.

We have points $(u_i, v_i)$ in $(\mathbb{Q}^*)^2$ (nonzero rationals). For each pair, either their $u$-coordinates are negatives of each other, or their $v$-coordinates are negatives of each other.

Let me think of this as a graph problem. Consider the "conflict graph" where we connect $i, j$ if neither $u_i = -u_j$ nor $v_i = -v_j$. We need this graph to have no edges, i.e., for every pair, at least one condition holds.

Let me think about what sets of points satisfy this. 

Consider the values $|u_i|$ and $|v_i|$. The condition is: for each pair, either $|u_i| = |u_j|$ (with opposite signs) or $|v_i| = |v_j|$ (with opposite signs).

Actually, more precisely: $u_i = -u_j$ means $|u_i| = |u_j|$ and $\text{sgn}(u_i) \neq \text{sgn}(u_j)$. Similarly for $v$.

Let me group by $|u|$ values and $|v|$ values. 

Let's say we have points with various $|u|$ and $|v|$ values. For two points $(u_i, v_i)$ and $(u_j, v_j)$:
- If $|u_i| \neq |u_j|$ and $|v_i| \neq |v_j|$: neither condition can hold. Bad.
- If $|u_i| = |u_j|$ but $u_i = u_j$ (same sign) and $|v_i| \neq |v_j|$: sum condition fails (need opposite signs), product condition fails. Bad.
- If $|u_i| = |u_j|$ and $u_i = -u_j$ (opposite signs): sum condition holds. Good.
- If $|v_i| = |v_j|$ and $v_i = -v_j$: product condition holds. Good.
- If $|u_i| = |u_j|$, $u_i = u_j$, $|v_i| = |v_j|$, $v_i = -v_j$: product condition holds. Good.
- If $|u_i| = |u_j|$, $u_i = -u_j$, $|v_i| = |v_j|$, $v_i = v_j$: sum condition holds. Good.
- Etc.

So the constraint is: for every pair of points, either (same $|u|$, opposite $u$-sign) or (same $|v|$, opposite $v$-sign).

Let me think about this combinatorially. Let me assign to each point a "row" = $|u_i|$ and "column" = $|v_i|$, and a sign pattern $(\sigma_i, \tau_i)$ where $\sigma_i = \text{sgn}(u_i)$, $\tau_i = \text{sgn}(v_i)$.

For two points in different rows and different columns: neither condition holds. Bad. So all points must share either a row or a column.

This means: the points form a "cross" shape — either all in the same row, or all in the same column, or some in one row and some in one column (forming a cross/L-shape).

Wait, more precisely: for any two points, they must share a row or share a column. This is the condition for a "clique" in the rook's graph. The maximum cliques in a rook's graph are either a full row or a full column. But we can also have a cross: one row plus one column.

Actually, the condition "any two points share a row or column" is exactly the condition for the set to be a clique in the rook's graph. The maximum cliques in a rook's graph $K_{m,n}$ (on an $m \times n$ grid) are: a full row (size $n$) or a full column (size $m$). But we can also have a cross: a row and a column intersecting at one point, giving size $m + n - 1$.

Wait, actually, for a cross (row $r$ union column $c$), any two points in the same row share the row, any two points in the same column share the column, and a point in the row (not at the intersection) and a point in the column (not at the intersection) share... the row point has row $r$ and some column $c'$, the column point has some row $r'$ and column $c$. They share neither row nor column (unless $c' = c$ or $r' = r$, but we said they're not at the intersection). So the cross doesn't work in general!

Hmm, let me reconsider. The condition is: any two points share a row or a column. For a cross (row $r$ ∪ column $c$), take point $(r, c_1)$ and point $(r_1, c)$ where $c_1 \neq c$ and $r_1 \neq r$. These share neither row nor column. So the cross doesn't satisfy the condition.

So the only sets satisfying "any two points share a row or column" are: all in one row, or all in one column. (This is a well-known result.)

Wait, that's not quite right either. What about a set like $\{(1,1), (1,2), (2,1)\}$? Points $(1,1)$ and $(1,2)$ share row 1. Points $(1,1)$ and $(2,1)$ share column 1. Points $(1,2)$ and $(2,1)$ share neither. So this doesn't work.

So indeed, the only sets where every pair shares a row or column are: a single row, or a single column. 

But wait, we also have the sign condition. Even if two points share a row (same $|u|$), we need opposite $u$-signs. And if they share a column (same $|v|$), we need opposite $v$-signs.

**Case 1: All points in the same row (same $|u|$).**
For each pair, we need $u_i = -u_j$ (opposite signs). But if we have 3 or more points, we can't have all pairs with opposite signs (since with 3 points, at least two have the same sign). So at most 2 points in a single row? No wait, we also have the column condition as a fallback.

Hmm, let me reconsider. If all points are in the same row (same $|u| = a$), then for each pair, either $u_i = -u_j$ (opposite $u$-signs) or $v_i = -v_j$ (same $|v|$ and opposite $v$-signs).

So within a row, the condition becomes: for each pair, either opposite $u$-signs or (same $|v|$ and opposite $v$-signs).

Let me split the row into two halves based on $u$-sign: positive $u$ and negative $u$. Any pair within the same half has the same $u$-sign, so they need same $|v|$ and opposite $v$-signs. Any pair across halves has opposite $u$-signs, so the condition is automatically satisfied.

So: within the positive-$u$ half, every pair must have the same $|v|$ and opposite $v$-signs. This means all points in the positive-$u$ half have the same $|v|$, and for each pair, they have opposite $v$-signs. With 3+ points in the positive half, at least two share the same $v$-sign, violating the condition. So at most 2 points in the positive-$u$ half (one with $v > 0$, one with $v < 0$).

Similarly, at most 2 points in the negative-$u$ half.

So at most 4 points in a single row? Wait, but I need to also check cross-half pairs. Cross-half pairs (one positive $u$, one negative $u$) automatically satisfy the condition (opposite $u$-signs). So no additional constraint.

But wait, within the positive-$u$ half, we need all pairs to have the same $|v|$ and opposite $v$-signs. With 2 points, they need the same $|v|$ and opposite $v$-signs. That's fine: $(a, b)$ and $(a, -b)$ for some $a, b > 0$ (using $u = a$, $v = b$ and $u = a$, $v = -b$).

Actually, we could also have just 1 point in the positive half and 1 in the negative half, etc.

So in a single row, the maximum is: 2 in positive-$u$ half (with $v$ and $-v$) + 2 in negative-$u$ half (with $v'$ and $-v'$). But we need all 4 points to be distinct. The 4 points are: $(a, b)$, $(a, -b)$, $(-a, c)$, $(-a, -c)$ for some $b, c > 0$. These are distinct as long as $b \neq c$ or... actually, $(a, b)$ and $(-a, c)$ are always distinct (different $u$-signs). $(a, b)$ and $(a, -b)$ are distinct (different $v$). $(a, b)$ and $(-a, -c)$ are distinct. So all 4 are distinct as long as $b \neq 0$ and $c \neq 0$, which they are.

But wait, I need to check: within the negative-$u$ half, the two points $(-a, c)$ and $(-a, -c)$ need the same $|v|$ (which is $c$) and opposite $v$-signs (which they have). Good.

And cross-half: $(a, b)$ and $(-a, c)$: opposite $u$-signs, condition satisfied. $(a, b)$ and $(-a, -c)$: opposite $u$-signs, satisfied. Etc. All good.

So we can have 4 points in a single row. But can we do better by using multiple rows?

Wait, I showed that all points must be in a single row or single column. So the maximum is either the max for a single row or a single column. By symmetry (swapping $u$ and $v$), they're the same. So the max is 4.

But wait, I think I was too hasty. Let me reconsider whether all points must be in a single row or column.

The condition is: for each pair $(i, j)$, either $|u_i| = |u_j|$ (with opposite signs) or $|v_i| = |v_j|$ (with opposite signs).

Actually, I need to be more careful. The condition is:
- $u_i = -u_j$ (which requires $|u_i| = |u_j|$ and opposite signs), OR
- $v_i = -v_j$ (which requires $|v_i| = |v_j|$ and opposite signs).

So for each pair, at least one of these holds. Let me think about the "row" as $|u|$ and "column" as $|v|$. Two points in different rows and different columns can't satisfy either condition. So for every pair, they must share a row or share a column.

As I argued, this means all points are in a single row or single column. (This is because if we have points in two different rows and two different columns, we can find a pair that shares neither.)

Wait, actually, let me re-examine. Suppose we have points at $(r_1, c_1)$, $(r_1, c_2)$, $(r_2, c_1)$. The pair $(r_1, c_2)$ and $(r_2, c_1)$ shares neither row nor column. So this doesn't work. Hence, all points must be in a single row or single column.

So the maximum number of type I values (in this $\sqrt{d}$ framework) is 4.

But wait, I restricted to values of the form $a + b\sqrt{d}$. Maybe there are other forms that allow more type I values?

Hmm, but actually, the problem doesn't restrict to quadratic irrationals. Let me think about whether we can do better with more general irrationals.

Let me reconsider the general problem. We have all $x_i$ irrational, and for each pair, either $x_i + x_j \in \mathbb{Q}$ or $x_i x_j \in \mathbb{Q}$. We want to maximize the number of $x_i^2 \notin \mathbb{Q}$.

Let me separate the type I values (those with $x_i^2 \notin \mathbb{Q}$) and type R values (those with $x_i^2 \in \mathbb{Q}$).

**Key constraint among type I values**: Among any three type I values, not all three pairwise products can be rational (as this would force all squares to be rational).

But the constraint is actually stronger. Let me think about what graphs are possible.

Among type I values, define a graph $G$ where we put a "product edge" between $i, j$ if $x_i x_j \in \mathbb{Q}$. The constraint is: $G$ is triangle-free (no three mutually connected by product edges).

Wait, is that exactly right? If $x_i x_j, x_i x_k, x_j x_k$ are all rational, then $x_i^2 = (x_i x_j)(x_i x_k)/(x_j x_k) \in \mathbb{Q}$, contradiction. So yes, among type I values, the "product graph" is triangle-free.

By Ramsey theory, $R(3,3) = 6$, so among 6 type I values, there must be a triangle in the product graph or a triangle in the complement (the "sum graph"). But a triangle in the product graph is forbidden. So among 6 type I values, there must be a triangle in the sum graph (three values pairwise connected by rational sums).

But as I showed earlier, if $x_i + x_j, x_i + x_k, x_j + x_k$ are all rational, then all $x_i$ are rational. Contradiction (they're all irrational). So there can't be a triangle in the sum graph either!

Wait, that's a key point. If three values have all pairwise sums rational, they must all be rational. But our values are all irrational. So the sum graph is also triangle-free!

So among type I values, both the product graph and the sum graph are triangle-free. Since every edge is either a product edge or a sum edge (or both), the complete graph on the type I values is the union of two triangle-free graphs.

By Ramsey theory, $R(3,3) = 6$, so we can't have 6 vertices whose complete graph is 2-colored with no monochromatic triangle. So we can have at most 5 type I values.

Wait, let me be more careful. The "product graph" and "sum graph" might share edges (both sum and product rational). Let me think about this.

Actually, let me define it more carefully. For each pair of type I values $(i, j)$, at least one of $x_i + x_j$ or $x_i x_j$ is rational. Color the edge "red" if $x_i x_j \in \mathbb{Q}$ (product rational) and "blue" if $x_i + x_j \in \mathbb{Q}$ (sum rational). An edge can be both red and blue.

The constraint is:
- No all-red triangle (would force all squares rational).
- No all-blue triangle (would force all values rational).

But an edge can be both red and blue. So this isn't a standard 2-coloring. However, we can convert it: for each edge that's both red and blue, assign it one color (say red). Then we get a valid 2-coloring with no all-red triangle and no all-blue triangle. By $R(3,3) = 6$, we can have at most 5 vertices.

Wait, but I need to be careful. If an edge is both red and blue, and I assign it red, then an all-red triangle might appear. Let me think again.

Actually, the constraint is: there's no triangle where all three edges are red (product), and no triangle where all three edges are blue (sum). If an edge is both, it counts as both red and blue. So a triangle with two "both" edges and one "red" edge would be an all-red triangle (since the "both" edges are red). And it would also be an all-blue triangle only if the third edge is also blue.

Hmm, this is a bit subtle. Let me think about it differently.

For each pair, define $P(i,j) = 1$ if $x_i x_j \in \mathbb{Q}$, and $S(i,j) = 1$ if $x_i + x_j \in \mathbb{Q}$. We have $P(i,j) \lor S(i,j) = 1$ for all pairs.

Constraint 1: No triangle with all $P = 1$ (among type I values).
Constraint 2: No triangle with all $S = 1$ (among all values, since it forces rationality).

Now, for a 2-coloring where each edge is red ($P=1, S=0$), blue ($P=0, S=1$), or purple ($P=1, S=1$):
- No triangle with all edges red or purple (i.e., all $P=1$).
- No triangle with all edges blue or purple (i.e., all $S=1$).

If we replace each purple edge with red, we get a 2-coloring (red/blue) with no all-red triangle. If we replace each purple edge with blue, we get a 2-coloring with no all-blue triangle. But we need both simultaneously.

Actually, let me think about it as: we have a graph where each edge is labeled with a nonempty subset of {P, S}. No triangle has all edges containing P, and no triangle has all edges containing S.

For each edge, if it's {P,S} (both), we can choose to "drop" one of the labels. We want to assign each edge a single label (P or S) such that no triangle is all-P and no triangle is all-S. This is exactly a 2-coloring of the complete graph with no monochromatic triangle, which by $R(3,3)=6$ requires at most 5 vertices.

But can we always make such an assignment? If an edge is {P}, we must assign P. If {S}, we must assign S. If {P,S}, we can choose. The question is whether there exists a valid assignment.

Hmm, actually, the constraints are on the original labeling, not on any assignment. Let me think about whether the original constraints directly imply at most 5 type I values.

Consider 6 type I values. For each pair, $P(i,j) \lor S(i,j)$. No triangle has all $P$, no triangle has all $S$.

Consider the graph $G_P$ (edges where $P=1$) and $G_S$ (edges where $S=1$). $G_P \cup G_S = K_n$ (complete graph). $G_P$ is triangle-free and $G_S$ is triangle-free.

Since $G_P$ is triangle-free, by Turán's theorem, $|E(G_P)| \leq n^2/4$ (for $n$ vertices, triangle-free graph has at most $n^2/4$ edges). Similarly for $G_S$. So $|E(G_P)| + |E(G_S)| \leq n^2/2$. But $|E(G_P)| + |E(G_S)| \geq |E(G_P \cup G_S)| = \binom{n}{2} = n(n-1)/2$.

So $n(n-1)/2 \leq n^2/2$, which gives $n-1 \leq n$, always true. Not helpful.

But we also have $G_P \cap G_S$ (edges that are both). Let $a = |E(G_P) \setminus E(G_S)|$, $b = |E(G_S) \setminus E(G_P)|$, $c = |E(G_P) \cap E(G_S)|$. Then $a + b + c = \binom{n}{2}$, $a + c \leq n^2/4$ (triangle-free), $b + c \leq n^2/4$.

Adding: $a + b + 2c \leq n^2/2$. Since $a + b + c = n(n-1)/2$, we get $n(n-1)/2 + c \leq n^2/2$, so $c \leq n/2$.

For $n = 6$: $c \leq 3$, $a + c \leq 9$, $b + c \leq 9$, $a + b + c = 15$. So $a + b \geq 12$, and $a \leq 9, b \leq 9$ (since $c \geq 0$). Also $a + c \leq 9$ and $b + c \leq 9$ with $a + b + c = 15$ gives $c \geq 15 - 9 - 9 = -3$, not helpful. And $a + c \leq 9$ gives $a \leq 9 - c$, $b + c \leq 9$ gives $b \leq 9 - c$, so $a + b + c \leq 18 - c$, i.e., $15 \leq 18 - c$, i.e., $c \leq 3$.

So for $n = 6$, we need $c \leq 3$, $a + c \leq 9$, $b + c \leq 9$, $a + b + c = 15$. This gives $a \geq 15 - 9 - 0 = 6$ (from $b \leq 9$ and $c \geq 0$), etc. It seems numerically possible. So the counting argument doesn't rule out $n = 6$.

Let me try $R(3,3) = 6$ more directly. We have a complete graph on 6 vertices, each edge labeled with a nonempty subset of {P, S}. No all-P triangle, no all-S triangle.

For each edge, choose one label (if both, choose one). This gives a 2-coloring. By $R(3,3) = 6$, there's a monochromatic triangle. If it's all-P, that's a violation. If it's all-S, that's a violation.

But wait—the monochromatic triangle in the 2-coloring might not be a monochromatic triangle in the original labeling. For example, if an edge was {P,S} and we chose S, then in the all-S triangle of the 2-coloring, that edge has $S=1$ in the original, which is fine. But the other edges in the triangle might have been {P} (forced P) and we chose... no, if an edge is {P} only, we must choose P, so it can't be in an all-S triangle.

Let me be more careful. We have edges labeled {P}, {S}, or {P,S}. We want to choose a single label for each {P,S} edge such that the resulting 2-coloring has no monochromatic triangle.

This is exactly the question of whether a "list coloring" of the complete graph avoids monochromatic triangles. By $R(3,3) = 6$, any 2-coloring of $K_6$ has a monochromatic triangle. So no matter how we choose, there will be a monochromatic triangle. If it's all-P, it corresponds to an all-P triangle in the original (since every edge in the triangle has $P=1$—either it was {P} or {P,S} and we chose P). If it's all-S, similarly.

Wait, that's the key. In the 2-coloring, every edge labeled P (whether from {P} or {P,S}→P) has $P=1$ in the original. So an all-P triangle in the 2-coloring is an all-P triangle in the original. Similarly for S. So the 2-coloring has a monochromatic triangle (by $R(3,3)=6$), which is a monochromatic triangle in the original. Contradiction.

So we can have at most 5 type I values! And we need to check that 5 is achievable.

Wait, I need to double-check the claim about all-S triangles. If three type I values have all pairwise sums rational, then they're all rational (as I showed). But they're type I, so irrational. Contradiction. So no all-S triangle among type I values. ✓

And no all-P triangle among type I values (as shown, it forces all squares rational). ✓

So by $R(3,3) = 6$, at most 5 type I values. Now I need to check:
1. Can we achieve 5 type I values?
2. What about type R values? Can we add type R values alongside type I values?

Let me first check if 5 type I values is achievable. I need 5 irrational numbers, all with irrational squares, such that for each pair, either sum or product is rational, and no three have all pairwise products rational, and no three have all pairwise sums rational.

The unique (up to isomorphism) 2-coloring of $K_5$ with no monochromatic triangle is the 5-cycle coloring: color the edges of the 5-cycle one color, and the complementary 5-cycle the other color.

So let's say the "product edges" form a 5-cycle: $x_1 x_2, x_2 x_3, x_3 x_4, x_4 x_5, x_5 x_1$ are rational, and the "sum edges" form the complementary 5-cycle: $x_1 + x_3, x_1 + x_4, x_2 + x_4, x_2 + x_5, x_3 + x_5$ are rational.

Let me try to construct such values. Let me use the $\sqrt{d}$ framework.

Recall: $x_i = u_i(v_i + \sqrt{d})$ where $u_i, v_i$ are rational, $u_i, v_i \neq 0$.
- Product rational: $v_i + v_j = 0$, i.e., $v_j = -v_i$.
- Sum rational: $u_i + u_j = 0$, i.e., $u_j = -u_i$.
- Type I: $v_i \neq 0$ (which we already have).

Wait, I think I had the conditions swapped. Let me recompute.

$x_i = u_i v_i + u_i \sqrt{d}$ where $u_i = b_i$, $v_i = a_i / b_i$, so $a_i = u_i v_i$, $b_i = u_i$.

$x_i x_j = (u_i v_i + u_i \sqrt{d})(u_j v_j + u_j \sqrt{d}) = u_i u_j (v_i v_j + d + (v_i + v_j)\sqrt{d})$.

This is rational iff $v_i + v_j = 0$.

$x_i + x_j = u_i(v_i + \sqrt{d}) + u_j(v_j + \sqrt{d}) = (u_i v_i + u_j v_j) + (u_i + u_j)\sqrt{d}$.

This is rational iff $u_i + u_j = 0$.

$x_i^2 = u_i^2(v_i^2 + d + 2v_i\sqrt{d})$. This is rational iff $v_i = 0$. Since $v_i \neq 0$, $x_i^2$ is irrational. ✓

So:
- Product edge between $i, j$: $v_i = -v_j$.
- Sum edge between $i, j$: $u_i = -u_j$.

For the 5-cycle product graph: $v_1 = -v_2, v_2 = -v_3, v_3 = -v_4, v_4 = -v_5, v_5 = -v_1$.

From $v_1 = -v_2, v_2 = -v_3$: $v_1 = v_3$. From $v_3 = -v_4, v_4 = -v_5$: $v_3 = v_5$. From $v_5 = -v_1$: $v_3 = -v_1$. But $v_1 = v_3$, so $v_1 = -v_1$, so $v_1 = 0$. Contradiction (need $v_i \neq 0$).

So the 5-cycle product graph doesn't work with this framework! The issue is that a 5-cycle has odd length, so going around the cycle, $v_1 = -v_2 = v_3 = -v_4 = v_5 = -v_1$, giving $v_1 = -v_1$, so $v_1 = 0$.

So we can't realize the 5-cycle product graph with this framework. We need a different approach.

Hmm, let me think about whether we can use a different structure. Maybe not all values need to be of the form $a + b\sqrt{d}$.

Actually, let me reconsider. The condition for a "sum edge" is $x_i + x_j \in \mathbb{Q}$, and for a "product edge" is $x_i x_j \in \mathbb{Q}$. I was working in the specific framework of $x_i = a_i + b_i\sqrt{d}$, but maybe there are other constructions.

Let me think about the 5-cycle more carefully. We need 5 type I values with:
- Product edges: $(1,2), (2,3), (3,4), (4,5), (5,1)$ — these have $x_i x_j \in \mathbb{Q}$.
- Sum edges: $(1,3), (1,4), (2,4), (2,5), (3,5)$ — these have $x_i + x_j \in \mathbb{Q}$.

From product edges: $x_1 x_2 = r_1, x_2 x_3 = r_2, x_3 x_4 = r_3, x_4 x_5 = r_4, x_5 x_1 = r_5$ (all rational).

From these: $x_1/x_3 = r_1/r_2$, $x_3/x_5 = r_3/r_4$, $x_5/x_1 = r_5/r_1$... wait, $x_5 x_1 = r_5$, so $x_1/x_5 = r_5/x_5^2$... hmm, let me think differently.

$x_1 x_2 = r_1, x_2 x_3 = r_2 \Rightarrow x_1/x_3 = r_1/r_2 \in \mathbb{Q}$. So $x_1 = q_{13} x_3$ for rational $q_{13} = r_1/r_2$.

Similarly, $x_3 x_4 = r_3, x_4 x_5 = r_4 \Rightarrow x_3/x_5 = r_3/r_4 \in \mathbb{Q}$. So $x_3 = q_{35} x_5$.

And $x_5 x_1 = r_5 \Rightarrow x_5 x_1 = r_5$. With $x_1 = q_{13} x_3 = q_{13} q_{35} x_5$, we get $q_{13} q_{35} x_5^2 = r_5$, so $x_5^2 = r_5 / (q_{13} q_{35}) \in \mathbb{Q}$.

But $x_5$ is type I, so $x_5^2 \notin \mathbb{Q}$. Contradiction!

So the 5-cycle product graph is impossible! Going around an odd cycle of product edges forces a square to be rational.

More generally, any odd cycle of product edges among type I values is impossible. So the product graph must be bipartite (no odd cycles).

Similarly, let me check: can the sum graph have odd cycles? If $x_i + x_j, x_j + x_k, x_k + x_i$ are all rational (a triangle), then all are rational. So no triangle in the sum graph. But what about longer odd cycles?

Consider a 5-cycle in the sum graph: $x_1 + x_2, x_2 + x_3, x_3 + x_4, x_4 + x_5, x_5 + x_1$ all rational. Then $x_1 - x_3 = (x_1 + x_2) - (x_2 + x_3) \in \mathbb{Q}$, $x_3 - x_5 = (x_3 + x_4) - (x_4 + x_5) \in \mathbb{Q}$, $x_5 + x_1 \in \mathbb{Q}$. So $x_1 = x_3 + q_1 = x_5 + q_1 + q_2$ for rational $q_1, q_2$. And $x_5 + x_1 = x_5 + x_5 + q_1 + q_2 = 2x_5 + q_1 + q_2 \in \mathbb{Q}$, so $x_5 \in \mathbb{Q}$. Contradiction.

So odd cycles in the sum graph also force rationality. The sum graph must also be bipartite.

So both the product graph and the sum graph are bipartite (among type I values). Since their union is the complete graph, and both are bipartite...

A bipartite graph on $n$ vertices has at most $n^2/4$ edges. The complete graph has $n(n-1)/2$ edges. If both $G_P$ and $G_S$ are bipartite, and $G_P \cup G_S = K_n$, then:

$n(n-1)/2 \leq |E(G_P)| + |E(G_S)| \leq n^2/4 + n^2/4 = n^2/2$.

So $n(n-1)/2 \leq n^2/2$, giving $n-1 \leq n$, always true. Not helpful.

But we can use a stronger result. If $G_P$ is bipartite with parts $A, B$, and $G_S$ is bipartite with parts $C, D$, then every edge of $K_n$ is in $G_P$ or $G_S$. 

Consider the four sets $A \cap C, A \cap D, B \cap C, B \cap D$. An edge within $A \cap C$ is not in $G_P$ (same part of $G_P$'s bipartition) and not in $G_S$ (same part of $G_S$'s bipartition). So there can be no edge within $A \cap C$, meaning $|A \cap C| \leq 1$. Similarly, $|A \cap D| \leq 1, |B \cap C| \leq 1, |B \cap D| \leq 1$.

So $n = |A \cap C| + |A \cap D| + |B \cap C| + |B \cap D| \leq 4$.

So among type I values, we can have at most 4!

Wait, but I need to be more careful. The bipartitions of $G_P$ and $G_S$ might not be unique (if the graphs are disconnected). Let me think about this.

$G_P$ is bipartite, so it has a 2-coloring (say red/blue) with no monochromatic edges. $G_S$ is bipartite, so it has a 2-coloring (say green/yellow) with no monochromatic edges. Every edge of $K_n$ is in $G_P$ or $G_S$ (or both).

Now, consider the four groups based on the two 2-colorings: (red, green), (red, yellow), (blue, green), (blue, yellow). Within any group, there are no $G_P$-edges (same red/blue color) and no $G_S$-edges (same green/yellow color). So there are no edges at all within any group. Since the graph is complete, each group has at most 1 vertex. So $n \leq 4$.

This is a clean argument! So at most 4 type I values.

Now, can we achieve 4 type I values? And can we add type R values to get more total values?

Let me first check if 4 type I values is achievable. We need $G_P$ and $G_S$ both bipartite, with $G_P \cup G_S = K_4$. The four groups are singletons: one vertex in each of (red, green), (red, yellow), (blue, green), (blue, yellow).

$G_P$ edges: between red and blue, i.e., between {(red,green), (red,yellow)} and {(blue,green), (blue,yellow)}. So edges: (rg, bg), (rg, by), (ry, bg), (ry, by). That's $K_{2,2}$, which is a 4-cycle.

$G_S$ edges: between green and yellow, i.e., between {(red,green), (blue,green)} and {(red,yellow), (blue,yellow)}. So edges: (rg, ry), (rg, by), (bg, ry), (bg, by). Also $K_{2,2}$.

Together: $G_P \cup G_S$ = all 6 edges of $K_4$. ✓

The edges that are in both $G_P$ and $G_S$: (rg, by) and (ry, bg). These are the "diagonal" edges.

So the structure is:
- Vertices: 1=(rg), 2=(ry), 3=(bg), 4=(by).
- Product edges: (1,3), (1,4), (2,3), (2,4) — i.e., $x_1 x_3, x_1 x_4, x_2 x_3, x_2 x_4 \in \mathbb{Q}$.
- Sum edges: (1,2), (1,4), (2,3), (3,4) — i.e., $x_1 + x_2, x_1 + x_4, x_2 + x_3, x_3 + x_4 \in \mathbb{Q}$.
- Both: (1,4) and (2,3).

Let me verify: 
- $G_P$ edges: {1,3}, {1,4}, {2,3}, {2,4}. This is $K_{2,2}$ with parts {1,2} and {3,4}. Bipartite. ✓
- $G_S$ edges: {1,2}, {1,4}, {2,3}, {3,4}. This is $K_{2,2}$ with parts {1,3} and {2,4}. Bipartite. ✓
- Union: all 6 edges. ✓

Now let me construct actual values. Using the $a + b\sqrt{d}$ framework:

- Product edge: $v_i = -v_j$.
- Sum edge: $u_i = -u_j$.

Vertices: 1=(rg), 2=(ry), 3=(bg), 4=(by).

$G_P$ bipartition: {1,2} (red) and {3,4} (blue). Product edges between {1,2} and {3,4}.
$G_S$ bipartition: {1,3} (green) and {2,4} (yellow). Sum edges between {1,3} and {2,4}.

For product edges ($v_i = -v_j$): $v_1 = -v_3, v_1 = -v_4, v_2 = -v_3, v_2 = -v_4$.
From $v_1 = -v_3$ and $v_2 = -v_3$: $v_1 = v_2$. From $v_1 = -v_4$ and $v_2 = -v_4$: $v_1 = v_2$. Consistent. So $v_1 = v_2$ and $v_3 = v_4 = -v_1$.

For sum edges ($u_i = -u_j$): $u_1 = -u_2, u_1 = -u_4, u_2 = -u_3, u_3 = -u_4$.
From $u_1 = -u_2$ and $u_2 = -u_3$: $u_1 = u_3$. From $u_3 = -u_4$ and $u_1 = -u_4$: $u_1 = u_3$. Consistent. So $u_1 = u_3$ and $u_2 = u_4 = -u_1$.

So: $u_1 = u_3 = a$, $u_2 = u_4 = -a$, $v_1 = v_2 = b$, $v_3 = v_4 = -b$.

The four values:
- $x_1 = a(b + \sqrt{d})$
- $x_2 = -a(b + \sqrt{d})$
- $x_3 = a(-b + \sqrt{d}) = a(\sqrt{d} - b)$
- $x_4 = -a(-b + \sqrt{d}) = -a(\sqrt{d} - b) = a(b - \sqrt{d})$

Wait, $x_2 = -a(b + \sqrt{d}) = -x_1$. But the problem requires pairwise distinct non-zero values. $x_2 = -x_1$ is fine (distinct as long as $x_1 \neq 0$, which it is). But let me check all pairs:

$x_1 = a(b + \sqrt{d})$, $x_2 = -a(b + \sqrt{d})$, $x_3 = a(\sqrt{d} - b)$, $x_4 = a(b - \sqrt{d}) = -a(\sqrt{d} - b) = -x_3$.

So $x_1 = -x_2$ and $x_3 = -x_4$. Are $x_1, x_3$ distinct? $x_1 = a(b + \sqrt{d})$, $x_3 = a(\sqrt{d} - b)$. These are equal iff $b + \sqrt{d} = \sqrt{d} - b$, i.e., $b = 0$. But $b \neq 0$ (since $v_i \neq 0$). So $x_1 \neq x_3$. ✓

Are all four distinct? $x_1 \neq x_2$ (since $x_1 \neq 0$), $x_3 \neq x_4$ (since $x_3 \neq 0$), $x_1 \neq x_3$ (shown), $x_1 \neq x_4$ (since $x_1 = -x_4$ would mean $a(b+\sqrt{d}) = -a(\sqrt{d}-b) = a(b-\sqrt{d})$, so $b+\sqrt{d} = b-\sqrt{d}$, so $\sqrt{d} = 0$, impossible). Similarly $x_2 \neq x_3, x_2 \neq x_4$. ✓

All non-zero: $x_i = 0$ would require $b + \sqrt{d} = 0$ or $\sqrt{d} - b = 0$, i.e., $\sqrt{d} = \mp b$, impossible since $\sqrt{d}$ is irrational and $b$ is rational. ✓

All $x_i^2$ irrational: $x_i^2 = a^2(b \pm \sqrt{d})^2 = a^2(b^2 + d \pm 2b\sqrt{d})$. Since $b \neq 0$ and $\sqrt{d}$ is irrational, $2b\sqrt{d}$ is irrational, so $x_i^2$ is irrational. ✓

Now let me verify the conditions:
- $x_1 x_3 = a^2(b+\sqrt{d})(\sqrt{d}-b) = a^2(d - b^2) \in \mathbb{Q}$. ✓
- $x_1 x_4 = a^2(b+\sqrt{d})(b-\sqrt{d}) = a^2(b^2 - d) \in \mathbb{Q}$. ✓
- $x_2 x_3 = (-a)(a)(b+\sqrt{d})(\sqrt{d}-b) = -a^2(d-b^2) \in \mathbb{Q}$. ✓
- $x_2 x_4 = (-a)(a)(b+\sqrt{d})(b-\sqrt{d}) = -a^2(b^2-d) \in \mathbb{Q}$. ✓
- $x_1 + x_2 = a(b+\sqrt{d}) - a(b+\sqrt{d}) = 0 \in \mathbb{Q}$. ✓
- $x_3 + x_4 = a(\sqrt{d}-b) + a(b-\sqrt{d}) = 0 \in \mathbb{Q}$. ✓
- $x_1 + x_4 = a(b+\sqrt{d}) + a(b-\sqrt{d}) = 2ab \in \mathbb{Q}$. ✓
- $x_2 + x_3 = -a(b+\sqrt{d}) + a(\sqrt{d}-b) = -2ab \in \mathbb{Q}$. ✓

All conditions satisfied. So 4 type I values is achievable.

Now, can we add type R values (with $x_i^2 \in \mathbb{Q}$) to the set? We need all 10 values to be pairwise distinct, non-zero, irrational, and for each pair, either sum or product is rational.

Type R values have $x_i^2 \in \mathbb{Q}$, so $x_i = \pm\sqrt{q_i}$ for positive rational $q_i$ (and $x_i$ irrational, so $q_i$ is not a perfect square of a rational).

Let me think about what type R values can coexist with the 4 type I values.

Let me use the specific construction: $d = 2$, $a = 1$, $b = 1$.
- $x_1 = 1 + \sqrt{2}$
- $x_2 = -(1 + \sqrt{2})$
- $x_3 = \sqrt{2} - 1$
- $x_4 = 1 - \sqrt{2} = -(\sqrt{2} - 1)$

Now, consider adding a type R value $y = \sqrt{q}$ (or $-\sqrt{q}$) for some positive rational $q$ (not a perfect square).

For each pair $(y, x_i)$, we need $y + x_i \in \mathbb{Q}$ or $y \cdot x_i \in \mathbb{Q}$.

$y \cdot x_1 = \sqrt{q}(1 + \sqrt{2}) = \sqrt{q} + \sqrt{2q}$. This is rational iff $\sqrt{q} + \sqrt{2q} \in \mathbb{Q}$. If $q = 2k^2$ for rational $k$, then $\sqrt{q} = k\sqrt{2}$ and $\sqrt{2q} = 2k$, so $\sqrt{q} + \sqrt{2q} = k\sqrt{2} + 2k$, which is irrational. Hmm.

Actually, $\sqrt{q} + \sqrt{2q}$ is rational iff both $\sqrt{q}$ and $\sqrt{2q}$ are rational, which happens iff $q$ is a perfect square of a rational and $2q$ is too, i.e., $q = r^2$ and $2q = s^2$ for rationals $r, s$. Then $s^2 = 2r^2$, so $s/r = \sqrt{2}$, impossible for rationals. So $y \cdot x_1$ is never rational (for type R $y$).

$y + x_1 = \sqrt{q} + 1 + \sqrt{2}$. This is rational iff $\sqrt{q} + \sqrt{2}$ is rational. This happens iff $\sqrt{q} = r - \sqrt{2}$ for some rational $r$, i.e., $q = r^2 + 2 - 2r\sqrt{2}$. For $q$ rational, we need $r = 0$, giving $q = 2$. So $y = \sqrt{2}$.

Let me check: $y = \sqrt{2}$, $y + x_1 = \sqrt{2} + 1 + \sqrt{2} = 1 + 2\sqrt{2}$, irrational. Hmm, that's not rational.

Wait, I think I made an error. $\sqrt{q} + \sqrt{2}$ is rational iff $\sqrt{q} = r - \sqrt{2}$ for rational $r$. Then $q = (r - \sqrt{2})^2 = r^2 + 2 - 2r\sqrt{2}$. For $q$ to be rational, $r = 0$, giving $q = 2$ and $\sqrt{q} = \sqrt{2}$. Then $\sqrt{q} + \sqrt{2} = 2\sqrt{2}$, which is irrational. So actually $\sqrt{q} + \sqrt{2}$ is never rational (for $q$ a positive rational that's not a perfect square).

Hmm, so $y + x_1$ is never rational and $y \cdot x_1$ is never rational? That means no type R value can coexist with $x_1$?

Wait, let me reconsider. Maybe I should use a different $d$ or different type I values.

Actually, the issue is that my type I values are of the form $a + b\sqrt{d}$, and a type R value is $\pm\sqrt{q}$. For $y + x_i$ to be rational, we need $\sqrt{q} + a_i + b_i\sqrt{d} \in \mathbb{Q}$, i.e., $\sqrt{q} + b_i\sqrt{d} \in \mathbb{Q}$ (since $a_i$ is rational). This requires $\sqrt{q} = r - b_i\sqrt{d}$ for rational $r$, so $q = r^2 + b_i^2 d - 2rb_i\sqrt{d}$, requiring $r = 0$ (for $q$ rational), so $q = b_i^2 d$ and $\sqrt{q} = |b_i|\sqrt{d}$. Then $\sqrt{q} + b_i\sqrt{d} = (|b_i| + b_i)\sqrt{d}$, which is $2|b_i|\sqrt{d}$ (if $b_i > 0$) or $0$ (if $b_i < 0$). So it's rational only if $b_i < 0$, giving $\sqrt{q} + b_i\sqrt{d} = 0$, i.e., $y = -b_i\sqrt{d} = |b_i|\sqrt{d}$.

So $y + x_i$ is rational only if $y = |b_i|\sqrt{d}$ and $b_i < 0$ (so $y = -b_i\sqrt{d}$), giving $y + x_i = a_i \in \mathbb{Q}$.

For $y \cdot x_i$ to be rational: $y \cdot x_i = \sqrt{q}(a_i + b_i\sqrt{d}) = a_i\sqrt{q} + b_i\sqrt{qd}$. This is rational iff $a_i\sqrt{q} + b_i\sqrt{qd} \in \mathbb{Q}$. If $q = c^2 d$ for rational $c$, then $\sqrt{q} = c\sqrt{d}$ and $\sqrt{qd} = cd$, so $y \cdot x_i = a_i c\sqrt{d} + b_i cd$. This is rational iff $a_i c = 0$, i.e., $a_i = 0$ (since $c \neq 0$). But $a_i \neq 0$ for type I values. So $y \cdot x_i$ is not rational in this case.

If $q \neq c^2 d$ for any rational $c$, then $\sqrt{q}$ and $\sqrt{qd}$ are linearly independent over $\mathbb{Q}$ (assuming $q$ and $d$ are such that $q, d, qd$ are not perfect squares). Then $a_i\sqrt{q} + b_i\sqrt{qd} \in \mathbb{Q}$ requires $a_i = 0$ and $b_i = 0$, impossible.

Hmm, so it seems like for type I values of the form $a + b\sqrt{d}$ with $a \neq 0$, the only type R values that can coexist are those with $y = -b_i\sqrt{d}$ (for the sum to be rational), and these are specific to each $x_i$.

In our construction: $x_1 = 1 + \sqrt{2}$ ($a_1 = 1, b_1 = 1$), $x_2 = -1 - \sqrt{2}$ ($a_2 = -1, b_2 = -1$), $x_3 = -1 + \sqrt{2}$ ($a_3 = -1, b_3 = 1$), $x_4 = 1 - \sqrt{2}$ ($a_4 = 1, b_4 = -1$).

For $y + x_i$ to be rational, we need $y = -b_i\sqrt{d}$ (with $b_i < 0$... actually I think I need to redo this).

$y + x_i = \sqrt{q} + a_i + b_i\sqrt{d}$. For this to be rational, $\sqrt{q} + b_i\sqrt{d} \in \mathbb{Q}$. As computed, this requires $\sqrt{q} = -b_i\sqrt{d}$, i.e., $q = b_i^2 d$ and $y = -b_i\sqrt{d}$ (note: $y = \sqrt{q} = |b_i|\sqrt{d}$, and we need $y = -b_i\sqrt{d}$, so $|b_i| = -b_i$, i.e., $b_i < 0$; if $b_i > 0$, then $y = b_i\sqrt{d} = \sqrt{q}$ and $\sqrt{q} + b_i\sqrt{d} = 2b_i\sqrt{d}$, irrational).

Wait, I think I need to be more careful. $y$ could be $\sqrt{q}$ or $-\sqrt{q}$. Let me write $y = \epsilon\sqrt{q}$ where $\epsilon = \pm 1$.

$y + x_i = \epsilon\sqrt{q} + a_i + b_i\sqrt{d}$. Rational iff $\epsilon\sqrt{q} + b_i\sqrt{d} \in \mathbb{Q}$, iff $\epsilon\sqrt{q} = r - b_i\sqrt{d}$ for rational $r$. Then $q = (r - b_i\sqrt{d})^2/\epsilon^2 = (r - b_i\sqrt{d})^2$ (since $\epsilon^2 = 1$). So $q = r^2 + b_i^2 d - 2rb_i\sqrt{d}$. For $q$ rational, $r = 0$, giving $q = b_i^2 d$ and $\epsilon\sqrt{q} = -b_i\sqrt{d}$, i.e., $y = -b_i\sqrt{d}$.

So $y = -b_i\sqrt{d}$ (and $y^2 = b_i^2 d \in \mathbb{Q}$, so $y$ is type R).

For each $x_i$, the unique type R value that makes $y + x_i$ rational is $y = -b_i\sqrt{d}$.

In our construction:
- $x_1$: $b_1 = 1$, so $y = -\sqrt{2}$.
- $x_2$: $b_2 = -1$, so $y = \sqrt{2}$.
- $x_3$: $b_3 = 1$, so $y = -\sqrt{2}$.
- $x_4$: $b_4 = -1$, so $y = \sqrt{2}$.

So the only type R values that can pair with our type I values (via rational sum) are $\sqrt{2}$ and $-\sqrt{2}$.

Now, can we add both $\sqrt{2}$ and $-\sqrt{2}$ to our set? We need to check all pairs:

- $\sqrt{2}$ and $-\sqrt{2}$: $\sqrt{2} + (-\sqrt{2}) = 0 \in \mathbb{Q}$. ✓
- $\sqrt{2}$ and $x_1 = 1 + \sqrt{2}$: $\sqrt{2} + 1 + \sqrt{2} = 1 + 2\sqrt{2}$, irrational. $\sqrt{2} \cdot (1 + \sqrt{2}) = \sqrt{2} + 2$, irrational. Neither rational! ✗

So $\sqrt{2}$ can't coexist with $x_1$! Because $b_1 = 1 > 0$, and $y = -b_1\sqrt{d} = -\sqrt{2}$, not $\sqrt{2}$.

Let me check $-\sqrt{2}$ with $x_1$: $-\sqrt{2} + 1 + \sqrt{2} = 1 \in \mathbb{Q}$. ✓

And $\sqrt{2}$ with $x_2 = -1 - \sqrt{2}$: $\sqrt{2} + (-1 - \sqrt{2}) = -1 \in \mathbb{Q}$. ✓

$-\sqrt{2}$ with $x_2$: $-\sqrt{2} + (-1 - \sqrt{2}) = -1 - 2\sqrt{2}$, irrational. $(-\sqrt{2})(-1-\sqrt{2}) = \sqrt{2} + 2$, irrational. ✗

So $-\sqrt{2}$ can't coexist with $x_2$.

So we can add $\sqrt{2}$ (pairs with $x_2$ and $x_4$ via sum) or $-\sqrt{2}$ (pairs with $x_1$ and $x_3$ via sum), but not both (since $\sqrt{2}$ doesn't pair with $x_1$ or $x_3$, and $-\sqrt{2}$ doesn't pair with $x_2$ or $x_4$).

Wait, let me recheck. $\sqrt{2}$ with $x_3 = -1 + \sqrt{2}$: $\sqrt{2} + (-1 + \sqrt{2}) = -1 + 2\sqrt{2}$, irrational. $\sqrt{2} \cdot (-1 + \sqrt{2}) = -\sqrt{2} + 2$, irrational. ✗

$\sqrt{2}$ with $x_4 = 1 - \sqrt{2}$: $\sqrt{2} + 1 - \sqrt{2} = 1 \in \mathbb{Q}$. ✓

So $\sqrt{2}$ pairs with $x_2$ and $x_4$ (via sum), but not with $x_1$ or $x_3$.
$-\sqrt{2}$ pairs with $x_1$ and $x_3$ (via sum), but not with $x_2$ or $x_4$.

So we can add at most one of $\{\sqrt{2}, -\sqrt{2}\}$, and it only pairs with 2 of the 4 type I values. We can't add it because it fails to pair with the other 2.

Hmm, so with this specific construction, we can't add any type R value. Let me think about whether a different construction would allow type R values.

Actually, let me think more generally. Suppose we have type I values and want to add a type R value $y$ (with $y^2 \in \mathbb{Q}$, $y$ irrational). For each type I value $x_i$, we need $y + x_i \in \mathbb{Q}$ or $y \cdot x_i \in \mathbb{Q}$.

If $y \cdot x_i \in \mathbb{Q}$, then $x_i = r/y$ for rational $r$, and $x_i^2 = r^2/y^2 = r^2/q \in \mathbb{Q}$ (where $y^2 = q$). But $x_i$ is type I, so $x_i^2 \notin \mathbb{Q}$. Contradiction. So $y \cdot x_i \notin \mathbb{Q}$ for type I $x_i$.

Therefore, for each type I $x_i$, we need $y + x_i \in \mathbb{Q}$. This means $x_i = s_i - y$ for rational $s_i$, i.e., all type I values differ from $-y$ by rationals. So $x_i = -y + q_i$ for rational $q_i$.

But then for two type I values $x_i = -y + q_i$ and $x_j = -y + q_j$:
- $x_i + x_j = -2y + q_i + q_j$. Rational iff $y \in \mathbb{Q}$, contradiction. So $x_i + x_j \notin \mathbb{Q}$ (for $i \neq j$).
- $x_i x_j = (-y + q_i)(-y + q_j) = y^2 - (q_i + q_j)y + q_i q_j = q - (q_i + q_j)y + q_i q_j$ (where $y^2 = q \in \mathbb{Q}$). Rational iff $(q_i + q_j)y \in \mathbb{Q}$, i.e., $q_i + q_j = 0$ (since $y$ is irrational).

So for all pairs of type I values, we need $q_i + q_j = 0$, i.e., $q_j = -q_i$. But with 3+ type I values, we can't have all pairs satisfying $q_i + q_j = 0$ (since $q_1 = -q_2, q_1 = -q_3$ gives $q_2 = q_3$, and then $q_2 + q_3 = 2q_2 \neq 0$ unless $q_2 = 0$, but then $x_2 = -y$, which is type R, contradiction).

So with a type R value in the set, we can have at most 2 type I values!

Let me verify: with 2 type I values $x_1 = -y + q, x_2 = -y - q$ (where $q \neq 0$ rational):
- $x_1 + x_2 = -2y$, irrational. $x_1 x_2 = (-y+q)(-y-q) = y^2 - q^2 = q_0 - q^2 \in \mathbb{Q}$ (where $y^2 = q_0$). ✓
- $x_1^2 = y^2 - 2qy + q^2 = q_0 + q^2 - 2qy$. Irrational (since $y$ irrational, $q \neq 0$). ✓
- $x_2^2 = y^2 + 2qy + q^2 = q_0 + q^2 + 2qy$. Irrational. ✓

And $y + x_1 = q \in \mathbb{Q}$, $y + x_2 = -q \in \mathbb{Q}$. ✓

So with 1 type R value, we can have at most 2 type I values. That gives 2 irrational squares.

Now, can we have multiple type R values? Let's say we have type R values $y_1, \ldots, y_m$ (all with $y_k^2 \in \mathbb{Q}$, all irrational) and type I values $x_1, \ldots, x_p$.

Among type R values: $y_i y_j \in \mathbb{Q}$ (since $y_i^2, y_j^2 \in \mathbb{Q}$ implies $y_i y_j = \pm\sqrt{y_i^2 y_j^2} \in \mathbb{Q}$... wait, no. $y_i y_j = \epsilon_i \sqrt{q_i} \cdot \epsilon_j \sqrt{q_j} = \epsilon_i \epsilon_j \sqrt{q_i q_j}$. This is rational iff $q_i q_j$ is a perfect square of a rational. Not always.

Hmm, so among type R values, we need for each pair either $y_i + y_j \in \mathbb{Q}$ or $y_i y_j \in \mathbb{Q}$.

$y_i = \epsilon_i \sqrt{q_i}$, $y_j = \epsilon_j \sqrt{q_j}$.
$y_i + y_j = \epsilon_i \sqrt{q_i} + \epsilon_j \sqrt{q_j}$. Rational iff $\sqrt{q_i}$ and $\sqrt{q_j}$ are rational multiples of each other and the signs work out. Specifically, if $q_i/q_j = (r/s)^2$ for rationals $r, s$, then $\sqrt{q_i} = (r/s)\sqrt{q_j}$, and $y_i + y_j = (\epsilon_i r/s + \epsilon_j)\sqrt{q_j}$, rational iff $\epsilon_i r/s + \epsilon_j = 0$, i.e., $\epsilon_i r = -\epsilon_j s$.

$y_i y_j = \epsilon_i \epsilon_j \sqrt{q_i q_j}$. Rational iff $q_i q_j$ is a perfect square of a rational.

This is getting complicated. Let me think about the overall problem differently.

We want to maximize the number of type I values (irrational squares). We've shown:
1. Without type R values: at most 4 type I values (and 4 is achievable).
2. With type R values: at most 2 type I values (per type R value? or total?).

Wait, I showed that with ANY type R value in the set, all type I values must be of the form $-y + q_i$, and there can be at most 2 such type I values. But what if there are multiple type R values?

If there are two type R values $y_1, y_2$, then each type I value $x_i$ must satisfy $x_i + y_1 \in \mathbb{Q}$ and $x_i + y_2 \in \mathbb{Q}$ (since $x_i \cdot y_k \notin \mathbb{Q}$ for type I $x_i$ and type R $y_k$). So $x_i = -y_1 + q_i = -y_2 + q_i'$, giving $y_2 - y_1 = q_i - q_i' \in \mathbb{Q}$. So $y_2 - y_1 \in \mathbb{Q}$.

Also, $y_1 + y_2 \in \mathbb{Q}$ or $y_1 y_2 \in \mathbb{Q}$.

If $y_2 - y_1 \in \mathbb{Q}$ and $y_1 + y_2 \in \mathbb{Q}$, then $y_1, y_2 \in \mathbb{Q}$, contradiction. So $y_1 y_2 \in \mathbb{Q}$.

$y_2 = y_1 + r$ for rational $r$, and $y_1 y_2 = y_1(y_1 + r) = y_1^2 + ry_1 = q_1 + ry_1 \in \mathbb{Q}$, so $ry_1 \in \mathbb{Q}$, so $y_1 \in \mathbb{Q}$ (if $r \neq 0$), contradiction. If $r = 0$, $y_1 = y_2$, but they must be distinct
