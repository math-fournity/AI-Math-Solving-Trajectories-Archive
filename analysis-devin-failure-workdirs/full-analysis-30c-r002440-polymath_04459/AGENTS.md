# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Let $n$ be a given positive integer. Alice and Bob play a game. In the beginning, Alice determines an integer polynomial $P(x)$ with degree no more than $n$. Bob doesn’t know $P(x)$, and his goal is to determine whether there exists an integer $k$ such that no integer roots of $P(x) = k$ exist. 

In each round, Bob can choose a constant $c$. Alice will tell Bob an integer $k$, representing the number of integer $t$ such that $P(t) = c$. Bob needs to pay one dollar for each round. Find the minimum cost such that Bob can guarantee to reach his goal.

[i]Proposed by ltf0501[/i]       — 题目文本
#   1. **Claim:**
   There is no \( k \) such that \( P(x) = k \) has no integer solution if and only if \( P(x) = x + c \) or \( P(x) = -x + c \) for some \( c \).

2. **Proof of the Claim:**
   - Suppose \( P(x) = k \) always has an integer solution. Write \( P(x) = a_m x^m + a_{m-1} x^{m-1} + \cdots + a_0 \) with \( a_m > 0 \).
   - Consider the behavior of \( P(x) \) as \( x \to \infty \) and \( x \to -\infty \).

3. **Case 1: \( m \geq 2 \) (even degree polynomial):**
   - \( P(x) \) is bounded below since \( \lim_{x \to \infty} P(x) = \lim_{x \to -\infty} P(x) = \infty \).
   - There exist \( X_+ \) and \( X_- \) such that \( P(x) > 0 \) for \( x > X_+ \) and \( x < X_- \).
   - The interval \([X_-, X_+]\) is compact, and thus \( \{ P(x) \mid x \in [X_-, X_+] \} \) achieves a minimum \( m_0 \).
   - Let \( m = \min\{m_0, 0\} \). Then \( P(x) = \lfloor m \rfloor - 1 \) has no solution, contradicting our hypothesis.

4. **Case 2: \( m \geq 3 \) (odd degree polynomial):**
   - \( P(n) \) when \( n \) is large must skip some integer value in its range.
   - \( \lim_{n \to \infty} P(n+1) - P(n) = \infty \), so there exists \( X_0 \) such that \( P(n+1) - P(n) > 1 \) for \( n > X_0 \).
   - The set \( \{ P(x) \mid x \in (-\infty, X_0] \} \) is bounded above by some \( M \).
   - For \( P(x) > M \) whenever \( x > X_1 \), pick any integer \( n_0 > \max \{ X_0, X_1 \} \).
   - \( P(n) \) must skip the value \( P(n_0) + 1 \).

5. **Conclusion:**
   - The polynomial \( P(x) \) must be of the form \( P(x) = ax + b \) with \( a \neq 0 \).
   - It is easy to see that \( a = \pm 1 \), ending our proof.

6. **Determining the Minimum Cost:**
   - Bob needs to determine whether \( P(x) = k \) has no integer roots.
   - Bob can choose \( c = 0, 1, -1, 2, -2, \ldots, n, -n \) and ask Alice for the number of integer solutions.
   - If Bob finds a \( c \) such that the number of integer solutions is zero, he can conclude that there exists a \( k \) with no integer roots.
   - The minimum number of rounds Bob needs is \( 2n + 1 \) (including zero).

The final answer is \(\boxed{2n + 1}\)  — 标准解答
#   Let me think about this problem carefully.

We have a game where Alice picks an integer polynomial $P(x)$ with degree $\leq n$. Bob wants to determine whether there exists an integer $k$ such that $P(x) = k$ has no integer roots.

In each round, Bob picks a constant $c$, and Alice tells him the number of integer $t$ with $P(t) = c$. Bob pays $1 per round. Find the minimum cost for Bob to guarantee his goal.

Let me think about what Bob needs to determine. Bob wants to know: does there exist an integer $k$ such that $P(x) = k$ has no integer solutions?

Equivalently, Bob wants to know whether the image $P(\mathbb{Z})$ is all of $\mathbb{Z}$ or not. If $P(\mathbb{Z}) \neq \mathbb{Z}$, then there exists an integer $k$ not in the image, so the answer is "yes, such $k$ exists". If $P(\mathbb{Z}) = \mathbb{Z}$, then the answer is "no".

So Bob needs to determine whether $P$ maps $\mathbb{Z}$ surjectively onto $\mathbb{Z}$.

When does an integer polynomial $P$ satisfy $P(\mathbb{Z}) = \mathbb{Z}$? 

For degree 1: $P(x) = ax + b$. This is surjective iff $a = \pm 1$.

For higher degree: A polynomial of degree $\geq 2$ cannot be surjective on $\mathbb{Z}$. Actually, let me think. For degree $\geq 2$, $|P(x)| \to \infty$ as $|x| \to \infty$, but the gaps between consecutive values grow. Actually, for degree $\geq 2$, $P(\mathbb{Z})$ has density 0 in $\mathbb{Z}$, so it's definitely not surjective.

Wait, but actually we need to be more careful. For degree 1, $P(x) = ax + b$ with $a \neq 0$. The image is $a\mathbb{Z} + b$. This equals $\mathbb{Z}$ iff $|a| = 1$.

For degree 0, $P(x) = c$ constant. Image is $\{c\}$, not surjective (assuming we need all integers).

So the question reduces to: Bob needs to determine whether $P(\mathbb{Z}) = \mathbb{Z}$, which happens iff $P(x) = x + b$ or $P(x) = -x + b$ for some integer $b$.

Wait, but degree $\leq n$. If $n = 1$, then $P$ could be degree 0 or 1. If $n \geq 2$, $P$ could be degree 0, 1, or higher.

Actually wait. Let me reconsider. For degree $\geq 2$, is it always true that $P(\mathbb{Z}) \neq \mathbb{Z}$? 

Consider $P(x) = x^2$. Image is $\{0, 1, 4, 9, ...\}$, not surjective. 

Consider $P(x) = x^2 - x = x(x-1)$. Values: $0, 0, 2, 6, 12, ...$. Image is $\{0, 2, 6, 12, 20, ...\}$, not surjective.

For any polynomial of degree $d \geq 2$, $P(n+1) - P(n)$ is a polynomial of degree $d-1 \geq 1$, which goes to $\pm \infty$. So the gaps between consecutive values grow without bound, meaning the image can't be all of $\mathbb{Z}$.

So $P(\mathbb{Z}) = \mathbb{Z}$ iff $P(x) = x + b$ or $P(x) = -x + b$ for some integer $b$.

Now, Bob's goal is to determine whether $P(\mathbb{Z}) = \mathbb{Z}$ (answer: no such $k$ exists) or $P(\mathbb{Z}) \neq \mathbb{Z}$ (answer: yes, such $k$ exists).

Bob queries: for a chosen $c$, Alice returns $|\{t \in \mathbb{Z} : P(t) = c\}|$.

If $P(\mathbb{Z}) = \mathbb{Z}$, i.e., $P(x) = \pm x + b$, then for every $c$, there's exactly one integer $t$ with $P(t) = c$. So the answer is always 1.

If $P(\mathbb{Z}) \neq \mathbb{Z}$, Bob needs to detect this. 

But wait - could there be a non-surjective polynomial where every integer $c$ has at least one preimage? No, that's exactly surjectivity. If $P(\mathbb{Z}) \neq \mathbb{Z}$, there exists some $c$ with 0 preimages.

But Bob doesn't know which $c$ to query. He needs a strategy that works for any $P$.

Let me think about what information Bob gets. When Bob queries $c$, he gets $N(c) = |\{t \in \mathbb{Z} : P(t) = c\}|$.

If $P(x) = \pm x + b$: $N(c) = 1$ for all $c$.

If $P$ is degree 0, say $P(x) = b$: $N(b) = \infty$ (infinitely many $t$), $N(c) = 0$ for $c \neq b$. Wait, but the problem says Alice tells Bob "an integer $k$ representing the number of integer $t$". If there are infinitely many, what does Alice say? 

Hmm, for degree 0, $P(t) = c$ for all $t$ if $c = b$, so infinitely many. The problem says Alice tells an integer $k$. So maybe degree 0 is excluded or handled specially. Actually, the problem says "an integer $k$, representing the number of integer $t$ such that $P(t) = c$". If the count is infinite, this doesn't make sense as an integer. 

Let me re-read: "Alice will tell Bob an integer $k$, representing the number of integer $t$ such that $P(t) = c$."

For degree $\geq 1$, $P(t) = c$ has finitely many solutions (at most degree many), so $k$ is a finite non-negative integer. For degree 0, if $c$ equals the constant, there are infinitely many solutions. So maybe we should assume degree $\geq 1$, or the problem implicitly handles this.

Actually, the problem says "degree no more than $n$", and $n$ is a positive integer. So degree could be 0. But if degree is 0, then $P(x) = c_0$ for some constant, and $P(\mathbb{Z}) = \{c_0\} \neq \mathbb{Z}$ (for $n \geq 1$, there are integers not equal to $c_0$). So the answer would be "yes, such $k$ exists". But the issue is the infinite count.

Let me assume the problem is well-defined and that for degree 0, querying $c = c_0$ gives... hmm. Maybe the problem intends that $k$ can be any integer, and if there are infinitely many, Alice says something. Or maybe we should interpret "number of integer $t$" as possibly being a special value. 

Actually, I think for this problem, we can focus on the case where degree $\geq 1$ since degree 0 is a degenerate case. Or perhaps the problem means that the answer $k$ is the count, and for degree 0 with $c = c_0$, the count is infinite, which Alice would represent as... some large number? This is unclear.

Let me just proceed assuming degree $\geq 1$ is the interesting case, and for degree 0, Bob can easily detect it (e.g., query any $c$ and if the answer is "infinite" or a very large number, he knows it's degree 0).

Actually, let me reconsider. For degree $\geq 1$, the number of integer solutions to $P(t) = c$ is at most $n$ (the degree). So $k \in \{0, 1, 2, ..., n\}$ for degree $\geq 1$.

For degree 0, $P(t) = c_0$ for all $t$. If Bob queries $c_0$, the count is infinite. If he queries $c \neq c_0$, the count is 0. So if Alice must return an integer, and the count is infinite, this is problematic. But if we assume the problem is well-posed, maybe degree 0 is excluded or the infinite count is represented somehow.

Let me just focus on the main question: how many queries does Bob need?

Key insight: Bob wants to distinguish $P(x) = \pm x + b$ (surjective, answer "no") from all other polynomials (non-surjective, answer "yes").

If $P(x) = \pm x + b$, then $N(c) = 1$ for all $c$.

If $P$ is not of this form, Bob needs to find evidence. The evidence would be finding some $c$ with $N(c) \neq 1$ (either 0 or $\geq 2$).

But can Bob always find such $c$ with a bounded number of queries?

For degree 1, $P(x) = ax + b$ with $|a| \geq 2$: $N(c) = 1$ if $a | (c - b)$, and $N(c) = 0$ otherwise. So half the integers (in fact, a fraction $1 - 1/|a|$) have $N(c) = 0$. Bob can query, say, $c = 0$ and $c = 1$. If $P(x) = 2x$, then $N(0) = 1, N(1) = 0$. If $P(x) = 2x + 1$, then $N(0) = 0, N(1) = 1$. If $P(x) = x + b$, then $N(0) = 1, N(1) = 1$.

So with 2 queries, Bob can distinguish $P(x) = x + b$ from $P(x) = 2x + b'$? Not quite - what if $P(x) = 2x$ and Bob queries $c = 0$ and $c = 2$? Both give $N = 1$. So Bob got unlucky.

Hmm, so for degree 1 with $|a| \geq 2$, Bob needs to find a $c$ not divisible by $a$ (in the appropriate sense). But Bob doesn't know $a$.

Let me think about this more carefully. The question is: what's the minimum number of queries to guarantee distinguishing surjective from non-surjective?

For $n = 1$: $P(x) = ax + b$. Surjective iff $|a| = 1$. 

If $|a| = 1$: $N(c) = 1$ for all $c$.
If $|a| \geq 2$: $N(c) = 1$ if $c \equiv b \pmod{a}$, else $N(c) = 0$.
If $a = 0$: degree 0, $N(c_0) = \infty$, $N(c) = 0$ for $c \neq c_0$.

Bob needs to determine if $|a| = 1$ or not.

Strategy: Query $c = 0$. 
- If $N(0) = 0$: not surjective (since surjective would give $N(0) = 1$). Done with 1 query.
- If $N(0) = \infty$: degree 0, not surjective. Done with 1 query.
- If $N(0) = 1$: could be surjective ($|a|=1$) or non-surjective ($|a| \geq 2$ and $a | b$).

If $N(0) = 1$, query $c = 1$.
- If $N(1) = 1$: could still be either. E.g., $P(x) = x$ gives $N(0)=1, N(1)=1$. $P(x) = 2x$ gives $N(0)=1, N(1)=0$. $P(x) = 2x+1$ gives $N(0)=0, N(1)=1$. But what about $P(x) = x + 1$? $N(0) = 1, N(1) = 1$. And $P(x) = 2x$ gives $N(0)=1, N(1)=0$. So if both are 1, it could be $P(x) = x + b$ (surjective) or... is there a non-surjective degree 1 with $N(0) = N(1) = 1$? We need $a | b$ and $a | (1-b)$, i.e., $a | b$ and $a | (1-b)$, so $a | 1$, meaning $|a| = 1$. So if both $N(0) = 1$ and $N(1) = 1$, then $|a| = 1$, surjective!

Wait, that's a key insight. For degree 1: $N(0) = 1$ means $a | b$. $N(1) = 1$ means $a | (1-b)$. Together: $a | b$ and $a | (1-b)$, so $a | (b + (1-b)) = 1$, so $|a| = 1$. 

So for $n = 1$, 2 queries suffice: query $c = 0$ and $c = 1$.
- If either gives $N \neq 1$ (0 or $\infty$): not surjective, answer "yes".
- If both give $N = 1$: surjective, answer "no".

And 1 query is not enough: if Bob queries only $c = 0$ and gets $N(0) = 1$, he can't distinguish $P(x) = x$ (surjective) from $P(x) = 2x$ (non-surjective, $N(0) = 1$).

So for $n = 1$, the answer is 2.

Now for general $n$. The key question is: can Bob always determine surjectivity with a bounded number of queries, and what's that bound?

For degree $\geq 2$, $P$ is never surjective. But Bob needs to detect this. The challenge is that a degree $\geq 2$ polynomial might have $N(c) = 1$ for many values of $c$.

For example, $P(x) = x^2$. $N(0) = 1, N(1) = 2, N(2) = 0, N(4) = 2, ...$. So querying $c = 0$ gives 1, but $c = 1$ gives 2. So 2 queries detect it.

But what about $P(x) = x^2 + x$? $P(0) = 0, P(-1) = 0, P(1) = 2, P(-2) = 2, ...$. So $N(0) = 2, N(1) = 0, N(2) = 2, ...$. Querying $c = 0$ gives 2, immediately detected.

What about a degree 2 polynomial that looks like a degree 1 at specific points? Consider $P(x) = x^2$. $P(0) = 0, P(1) = 1, P(-1) = 1$. So $N(0) = 1, N(1) = 2$. If Bob queries $c = 0$, he gets 1. If he queries $c = 1$, he gets 2. So 2 queries work.

But can we construct a degree 2 polynomial where $N(0) = 1$ and $N(1) = 1$? We need $P(t) = 0$ for exactly one integer $t$, and $P(t) = 1$ for exactly one integer $t$.

$P(x) = x^2$: $N(0) = 1$ (only $x=0$), $N(1) = 2$ ($x = 1, -1$). So $N(1) = 2 \neq 1$.

$P(x) = x^2 + x$: $N(0) = 2$. No good.

$P(x) = x^2 - x$: Same as $x^2 + x$ by substitution. $N(0) = 2$.

$P(x) = 2x^2$: $N(0) = 1, N(1) = 0, N(2) = 0, N(8) = 2$. So $N(0) = 1, N(1) = 0$. Querying $c = 0, 1$ gives $1, 0$. Detected.

$P(x) = x^2 + 1$: $N(0) = 0, N(1) = 1, N(2) = 1, N(5) = 2$. So $N(0) = 0$. Detected immediately.

Hmm, what about $P(x) = x^2 + x + 1$? $P(0) = 1, P(-1) = 1, P(1) = 3, P(-2) = 3$. So $N(0) = 0, N(1) = 2$. Detected.

Let me try to find a degree 2 polynomial with $N(0) = 1$ and $N(1) = 1$.

$P(x) = ax^2 + bx + c$. We need exactly one integer root of $P(x) = 0$ and exactly one integer root of $P(x) = 1$.

For $P(x) = 0$ to have exactly one integer solution, the discriminant $b^2 - 4ac$ must be a perfect square, and $-b \pm \sqrt{b^2-4ac}$ must be divisible by $2a$, with exactly one of the two roots being an integer.

Actually, for a quadratic $ax^2 + bx + c = 0$, if the discriminant is a perfect square $d^2$, the roots are $\frac{-b \pm d}{2a}$. For exactly one integer root, we need exactly one of $\frac{-b+d}{2a}$ and $\frac{-b-d}{2a}$ to be an integer.

This is getting complicated. Let me think differently.

Can we have a degree 2 polynomial $P$ with $P(0) = 0$ and $P(1) = 1$ (so $N(0) \geq 1$ and $N(1) \geq 1$), and moreover $N(0) = 1$ and $N(1) = 1$?

$P(x) = x^2$: $P(0) = 0, P(1) = 1$. $N(0) = 1$ (only $x=0$), $N(1) = 2$ ($x = 1, -1$). So $N(1) = 2$.

$P(x) = x^2 + cx$ for some $c$: $P(0) = 0, P(1) = 1 + c$. For $P(1) = 1$, need $c = 0$, back to $x^2$.

$P(x) = ax^2 + bx + c_0$ with $P(0) = 0 \Rightarrow c_0 = 0$. $P(1) = 1 \Rightarrow a + b = 1$. So $P(x) = ax^2 + (1-a)x = x(ax + 1 - a)$. Roots of $P(x) = 0$: $x = 0$ and $x = (a-1)/a = 1 - 1/a$. For the second root to not be an integer, we need $a \nmid 1$, i.e., $|a| \neq 1$. So for $|a| \geq 2$, $N(0) = 1$ (only $x = 0$).

Roots of $P(x) = 1$: $ax^2 + (1-a)x - 1 = 0$. Discriminant: $(1-a)^2 + 4a = 1 - 2a + a^2 + 4a = a^2 + 2a + 1 = (a+1)^2$. Roots: $\frac{-(1-a) \pm (a+1)}{2a} = \frac{a-1 \pm (a+1)}{2a}$.

So roots are $\frac{a-1+a+1}{2a} = \frac{2a}{2a} = 1$ and $\frac{a-1-a-1}{2a} = \frac{-2}{2a} = \frac{-1}{a}$.

So $P(x) = 1$ has roots $x = 1$ and $x = -1/a$. For $N(1) = 1$, we need $-1/a$ to not be an integer, i.e., $|a| \neq 1$.

So for $|a| \geq 2$: $P(x) = ax^2 + (1-a)x$ has $N(0) = 1$ and $N(1) = 1$!

For example, $P(x) = 2x^2 - x$. $P(0) = 0, P(1) = 1$. $N(0) = 1$ (root $x=0$; other root $x = 1/2$, not integer). $N(1) = 1$ (root $x=1$; other root $x = -1/2$, not integer).

So with queries $c = 0$ and $c = 1$, Bob gets $N(0) = 1, N(1) = 1$, which is the same as a surjective polynomial! So 2 queries are not enough for $n = 2$.

So Bob needs more queries for $n = 2$. Let's see if 3 queries suffice.

Query $c = 0, 1, 2$. For $P(x) = 2x^2 - x$: $P(0) = 0, P(1) = 1, P(2) = 8 - 2 = 6$. So $N(2) = ?$. $2x^2 - x = 2 \Rightarrow 2x^2 - x - 2 = 0$. Discriminant: $1 + 16 = 17$, not a perfect square. So $N(2) = 0$. Detected!

But can we find a degree 2 polynomial with $N(0) = N(1) = N(2) = 1$?

$P(x) = ax^2 + bx + c$ with $P(0) = 0, P(1) = 1, P(2) = 2$. So $c = 0, a + b = 1, 4a + 2b = 2$. From $a + b = 1$ and $4a + 2b = 2$: $4a + 2(1-a) = 2 \Rightarrow 2a + 2 = 2 \Rightarrow a = 0$. So $P(x) = x$, degree 1. 

So there's no degree 2 polynomial passing through $(0,0), (1,1), (2,2)$. The only polynomial of degree $\leq 2$ through these points is $P(x) = x$.

But wait, we need $N(0) = N(1) = N(2) = 1$, not necessarily $P(0) = 0, P(1) = 1, P(2) = 2$. The preimage could be different integers.

Let me reconsider. We need: there exists exactly one integer $t_0$ with $P(t_0) = 0$, exactly one integer $t_1$ with $P(t_1) = 1$, exactly one integer $t_2$ with $P(t_2) = 2$.

For a surjective polynomial $P(x) = x + b$: $t_0 = -b, t_1 = 1-b, t_2 = 2-b$. All distinct, $N(0) = N(1) = N(2) = 1$.

For a non-surjective polynomial, we need to find one where $N(0) = N(1) = N(2) = 1$.

Let's try $P(x) = 2x^2 - x$ again. $N(0) = 1, N(1) = 1, N(2) = 0$. So $N(2) = 0$, detected.

Can we find a degree 2 polynomial with $N(0) = N(1) = N(2) = 1$?

Let me think about this more generally. A degree 2 polynomial $P(x) = ax^2 + bx + c$ with $a \neq 0$. For each value $v$, $P(x) = v$ has at most 2 integer solutions. $N(v) = 1$ means exactly one integer solution.

The image $P(\mathbb{Z})$ for a degree 2 polynomial: as $x \to \pm\infty$, $P(x) \to +\infty$ (if $a > 0$) or $-\infty$ (if $a < 0$). The image is "sparse" for large $|x|$.

Let me try to construct such a polynomial. We need $P$ to take values 0, 1, 2 each at exactly one integer point.

Let's say $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$ with $t_0, t_1, t_2$ integers, and no other integer maps to 0, 1, or 2.

If $t_0, t_1, t_2$ are distinct, then $P$ is determined (degree 2 through 3 points). Let's try $t_0 = 0, t_1 = 1, t_2 = 3$ (not 2, to avoid the linear case).

$P(0) = 0, P(1) = 1, P(3) = 2$. $P(x) = ax^2 + bx$. $a + b = 1, 9a + 3b = 2$. From first: $b = 1 - a$. $9a + 3(1-a) = 2 \Rightarrow 6a + 3 = 2 \Rightarrow a = -1/6$. Not integer.

Try $t_0 = 0, t_1 = 2, t_2 = 3$. $P(0) = 0, P(2) = 1, P(3) = 2$. $P(x) = ax^2 + bx$. $4a + 2b = 1, 9a + 3b = 2$. From first: $b = (1-4a)/2$. $9a + 3(1-4a)/2 = 2 \Rightarrow 18a + 3 - 12a = 4 \Rightarrow 6a = 1 \Rightarrow a = 1/6$. Not integer.

Hmm, it's hard to get integer coefficients. Let me try a different approach.

$P(x) = ax^2 + bx + c$ with integer $a, b, c$, $a \neq 0$. We need $N(0) = N(1) = N(2) = 1$.

For $N(v) = 1$: $ax^2 + bx + (c - v) = 0$ has exactly one integer root. This means the discriminant $b^2 - 4a(c-v)$ is a perfect square, say $d_v^2$, and exactly one of $\frac{-b + d_v}{2a}$ and $\frac{-b - d_v}{2a}$ is an integer.

This is quite constrained. Let me try specific examples.

$P(x) = x^2 + x = x(x+1)$. $P(0) = 0, P(-1) = 0$, so $N(0) = 2$. No good.

$P(x) = x^2 + 2x = x(x+2)$. $P(0) = 0, P(-2) = 0$, $N(0) = 2$. No good.

$P(x) = 2x^2 + 3x + 1 = (2x+1)(x+1)$. $P(-1) = 0, P(0) = 1, P(1) = 6$. $N(0) = 1$ (only $x = -1$, since $x = -1/2$ is not integer). $N(1) = 1$ (only $x = 0$; $2x^2 + 3x = 0 \Rightarrow x(2x+3) = 0 \Rightarrow x = 0$ or $x = -3/2$, so $N(1) = 1$). $N(2) = ?$: $2x^2 + 3x + 1 = 2 \Rightarrow 2x^2 + 3x - 1 = 0$. Discriminant $9 + 8 = 17$, not a perfect square. $N(2) = 0$. Detected at $c = 2$.

Let me try to find one where $N(0) = N(1) = N(2) = 1$.

$P(x) = 2x^2 + 3x + 1$. $N(0) = 1, N(1) = 1, N(2) = 0$. Close but $N(2) = 0$.

What if I shift? $P(x) = 2x^2 + 3x + 1 + k$ for some $k$. Then $N(k) = 1, N(k+1) = 1, N(k+2) = 0$. Bob queries $0, 1, 2$. If $k = 0$, he gets $1, 1, 0$. If $k = -1$, he gets $N(0) = N(1) = 1, N(2) = 1$... wait let me recompute.

$P(x) = 2x^2 + 3x + 1$. Values: $P(-2) = 8 - 6 + 1 = 3, P(-1) = 2 - 3 + 1 = 0, P(0) = 1, P(1) = 6, P(2) = 15$.

So $N(0) = 1$ (from $x = -1$), $N(1) = 1$ (from $x = 0$), $N(2) = 0$, $N(3) = 1$ (from $x = -2$), $N(6) = 1$ (from $x = 1$), etc.

So if Bob queries $c = 0, 1, 2$, he gets $1, 1, 0$. The third query detects it.

Can we find a degree 2 polynomial where $N(0) = N(1) = N(2) = 1$?

Let me think about it differently. For a degree 2 polynomial $P(x) = ax^2 + bx + c$ with $a > 0$, the image $P(\mathbb{Z})$ is a subset of $[P_{\min}, \infty) \cap \mathbb{Z}$ where $P_{\min}$ is the minimum value. For large values, the gaps between consecutive image values grow. So for large enough $c$, $N(c) = 0$. But 0, 1, 2 might all be in the image with unique preimages.

Let me try to be more systematic. I want $P(x) = ax^2 + bx + c$ with:
- $P(x) = 0$ has exactly one integer root
- $P(x) = 1$ has exactly one integer root
- $P(x) = 2$ has exactly one integer root

Let's say the integer roots are $r_0, r_1, r_2$ respectively (with $r_0, r_1, r_2$ not necessarily distinct, but if two are the same, that would mean $P(r) = 0 = 1$, contradiction, so they're distinct).

So $P(r_0) = 0, P(r_1) = 1, P(r_2) = 2$ with $r_0, r_1, r_2$ distinct integers. This gives us 3 equations in 3 unknowns ($a, b, c$), so $P$ is determined.

$P(x) = a(x - r_0)(x - r_2) + \frac{2(x - r_0)}{r_2 - r_0}$... hmm, let me use Lagrange interpolation.

Actually, $P$ is the unique degree $\leq 2$ polynomial through $(r_0, 0), (r_1, 1), (r_2, 2)$. For this to have degree exactly 2, we need $r_0, r_1, r_2$ to not be in arithmetic progression (if they were, $P$ would be linear).

If $r_0, r_1, r_2$ are in arithmetic progression, $P(x) = x - r_0$ (linear, surjective). So for degree 2, we need them not in AP.

Let me try $r_0 = 0, r_1 = 1, r_2 = 3$. Then $P(0) = 0, P(1) = 1, P(3) = 2$.

$P(x) = ax^2 + bx + c$. $c = 0, a + b = 1, 9a + 3b = 2$. $b = 1 - a, 9a + 3 - 3a = 2, 6a = -1, a = -1/6$. Not integer.

Try $r_0 = 0, r_1 = 2, r_2 = 3$. $P(0) = 0, P(2) = 1, P(3) = 2$. $c = 0, 4a + 2b = 1, 9a + 3b = 2$. From first: $b = (1 - 4a)/2$. $9a + 3(1-4a)/2 = 2 \Rightarrow 18a + 3 - 12a = 4 \Rightarrow 6a = 1 \Rightarrow a = 1/6$. Not integer.

Try $r_0 = 0, r_1 = 1, r_2 = -1$. $P(0) = 0, P(1) = 1, P(-1) = 2$. $c = 0, a + b = 1, a - b = 2$. $2a = 3, a = 3/2$. Not integer.

Try $r_0 = 1, r_1 = 0, r_2 = -1$. $P(1) = 0, P(0) = 1, P(-1) = 2$. $c = 1, a + b + 1 = 0, a - b + 1 = 2$. $a + b = -1, a - b = 1$. $a = 0, b = -1$. Linear! $P(x) = -x + 1$. This is surjective.

Try $r_0 = 0, r_1 = 2, r_2 = 5$. $P(0) = 0, P(2) = 1, P(5) = 2$. $c = 0, 4a + 2b = 1, 25a + 5b = 2$. $b = (1-4a)/2, 25a + 5(1-4a)/2 = 2 \Rightarrow 50a + 5 - 20a = 4 \Rightarrow 30a = -1 \Rightarrow a = -1/30$. Not integer.

It seems hard to get integer coefficients. Let me think about why.

For $P(x) = ax^2 + bx + c$ with $P(r_0) = 0, P(r_1) = 1, P(r_2) = 2$:

Using the Lagrange interpolation formula, $a$ is determined by the divided difference:
$a = \frac{1}{(r_0 - r_1)(r_0 - r_2)} \cdot 0 + \frac{1}{(r_1 - r_0)(r_1 - r_2)} \cdot 1 + \frac{1}{(r_2 - r_0)(r_2 - r_1)} \cdot 2$

Hmm, this is getting complicated. Let me think about it differently.

Actually, let me consider the polynomial $Q(x) = P(x) - x$. Then $Q(r_0) = -r_0, Q(r_1) = 1 - r_1, Q(r_2) = 2 - r_2$. If $P$ has degree 2, then $Q$ has degree 2 (since $P$ has degree 2 and we subtract a degree 1 polynomial). $Q$ is a degree 2 polynomial with $Q(r_i) = i - r_i$ for $i = 0, 1, 2$.

Hmm, this doesn't simplify things much.

Let me try a different approach. Instead of trying to construct specific examples, let me think about the general structure.

The question is: for degree $\leq n$, how many queries does Bob need?

Claim: The answer is $n + 1$.

Reasoning: Bob queries $c = 0, 1, 2, \ldots, n$. If all responses are 1, then $P$ is surjective (i.e., $P(x) = \pm x + b$). If any response is not 1, $P$ is not surjective.

Why would this work? If $N(0) = N(1) = \cdots = N(n) = 1$, then there exist integers $t_0, t_1, \ldots, t_n$ with $P(t_i) = i$ for each $i$. Since $P$ has degree $\leq n$, and we have $n + 1$ points $(t_i, i)$, $P$ is the unique polynomial of degree $\leq n$ through these points.

Now, if $t_0, t_1, \ldots, t_n$ are all distinct, then $P$ is determined by these $n+1$ points. But we also know $P(t_i) = i$, so $P$ interpolates the points $(t_0, 0), (t_1, 1), \ldots, (t_n, n)$.

If $t_i = t_j$ for some $i \neq j$, then $P(t_i) = i$ and $P(t_j) = j$ with $t_i = t_j$, contradiction since $i \neq j$. So all $t_i$ are distinct.

Now, the key question: if $P$ is a degree $\leq n$ polynomial with $P(t_i) = i$ for $n+1$ distinct integers $t_0, \ldots, t_n$, and $N(i) = 1$ for each $i$ (meaning $t_i$ is the ONLY integer with $P(t) = i$), does this force $P(x) = x + b$ or $P(x) = -x + b$?

Hmm, not necessarily. The condition $N(i) = 1$ for $i = 0, \ldots, n$ only tells us about $n+1$ specific values. $P$ could be a higher degree polynomial that happens to have unique preimages for these values.

Wait, but I need to think about this more carefully. Let me consider what constraints $N(i) = 1$ for $i = 0, 1, \ldots, n$ places on $P$.

Actually, let me reconsider the problem. The question is about the minimum cost, so we need both an upper bound (a strategy for Bob) and a lower bound (showing Alice can force Bob to use at least that many queries).

Let me think about the upper bound first.

Upper bound strategy: Bob queries $c = 0, 1, \ldots, n$.

Case 1: Some $N(i) \neq 1$ for some $i \in \{0, \ldots, n\}$. Then $P$ is not surjective (since surjective polynomials have $N(c) = 1$ for all $c$). Bob answers "yes, such $k$ exists".

Case 2: $N(i) = 1$ for all $i = 0, \ldots, n$. Bob needs to determine if $P$ is surjective.

In Case 2, there exist distinct integers $t_0, \ldots, t_n$ with $P(t_i) = i$. The polynomial $P$ of degree $\leq n$ is uniquely determined by these $n+1$ points. But Bob doesn't know $t_0, \ldots, t_n$! He only knows that $N(i) = 1$ for each $i$.

Hmm, so Bob doesn't actually know $P$ from the queries. He just knows that each of $0, 1, \ldots, n$ has exactly one preimage. This doesn't uniquely determine $P$.

For example, with $n = 2$: $P(x) = x$ gives $N(0) = N(1) = N(2) = 1$ (surjective). $P(x) = 2x^2 - x$ gives $N(0) = 1, N(1) = 1, N(2) = 0$ (not surjective, detected). But is there a degree 2 polynomial with $N(0) = N(1) = N(2) = 1$ that is not surjective?

From my earlier analysis, it seems hard to construct such a polynomial with integer coefficients. Let me think about whether it's possible.

$P(x) = ax^2 + bx + c$, degree 2, $N(0) = N(1) = N(2) = 1$.

There exist distinct integers $t_0, t_1, t_2$ with $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$.

$P$ is the unique degree $\leq 2$ polynomial through $(t_0, 0), (t_1, 1), (t_2, 2)$.

For $P$ to have degree 2, $t_0, t_1, t_2$ must not be in arithmetic progression. (If in AP, the interpolating polynomial is linear.)

If $t_0, t_1, t_2$ are in AP with common difference $d$, then $P(x) = \frac{1}{d}(x - t_0)$, which is linear. For this to have integer coefficients, $d | 1$, so $d = \pm 1$, giving $P(x) = x - t_0$ or $P(x) = -(x - t_0) = -x + t_0$. These are surjective.

If $t_0, t_1, t_2$ are not in AP, $P$ has degree 2. We need $P$ to have integer coefficients and $N(0) = N(1) = N(2) = 1$.

Let me parametrize. WLOG, by shifting, let $t_0 = 0$. So $P(0) = 0$, meaning $c = 0$. $P(x) = ax^2 + bx$.

$P(t_1) = 1 \Rightarrow at_1^2 + bt_1 = 1 \Rightarrow t_1(at_1 + b) = 1$.

Since $t_1$ is an integer and $at_1 + b$ is an integer, we need $t_1 \cdot (at_1 + b) = 1$. So either $t_1 = 1, at_1 + b = 1$ (i.e., $a + b = 1$) or $t_1 = -1, at_1 + b = -1$ (i.e., $-a + b = -1$, i.e., $b = a - 1$).

Case A: $t_1 = 1, a + b = 1$. Then $P(x) = ax^2 + (1-a)x$.
$P(t_2) = 2 \Rightarrow at_2^2 + (1-a)t_2 = 2 \Rightarrow at_2^2 + t_2 - at_2 = 2 \Rightarrow a(t_2^2 - t_2) + t_2 = 2 \Rightarrow a \cdot t_2(t_2 - 1) = 2 - t_2$.

If $t_2 \neq 0, 1$: $a = \frac{2 - t_2}{t_2(t_2 - 1)}$.

For $a$ to be a nonzero integer, $t_2(t_2 - 1) | (2 - t_2)$.

Let $t_2 = 2$: $a = 0/2 = 0$. Degree 0, not degree 2.
$t_2 = 3$: $a = -1/6$. Not integer.
$t_2 = -1$: $a = 3/2$. Not integer.
$t_2 = 4$: $a = -2/12 = -1/6$. Not integer.
$t_2 = -2$: $a = 4/6 = 2/3$. Not integer.
$t_2 = 5$: $a = -3/20$. Not integer.
$t_2 = -3$: $a = 5/12$. Not integer.

For $|t_2|$ large, $|a| \approx 1/|t_2|$, so $|a| < 1$ for $|t_2| \geq 3$, meaning $a = 0$ is the only integer possibility, but that gives degree $\leq 1$.

So in Case A, there's no degree 2 polynomial with integer coefficients!

Case B: $t_1 = -1, b = a - 1$. $P(x) = ax^2 + (a-1)x$.
$P(t_2) = 2 \Rightarrow at_2^2 + (a-1)t_2 = 2 \Rightarrow a(t_2^2 + t_2) - t_2 = 2 \Rightarrow a \cdot t_2(t_2 + 1) = 2 + t_2$.

If $t_2 \neq 0, -1$: $a = \frac{2 + t_2}{t_2(t_2 + 1)}$.

$t_2 = 1$: $a = 3/2$. Not integer.
$t_2 = 2$: $a = 4/6 = 2/3$. Not integer.
$t_2 = -2$: $a = 0/2 = 0$. Degree 0.
$t_2 = 3$: $a = 5/12$. Not integer.
$t_2 = -3$: $a = -1/6$. Not integer.

Again, no integer solutions with $a \neq 0$.

So with $t_0 = 0$, there's no degree 2 integer polynomial with $N(0) = N(1) = N(2) = 1$ (other than the linear surjective ones).

But wait, I assumed $t_0 = 0$ WLOG by shifting. But shifting $P$ changes it. Let me redo without this assumption.

Actually, the shift argument doesn't work directly because we're looking at specific values 0, 1, 2. Let me redo.

General case: $P(x) = ax^2 + bx + c$, $a \neq 0$, integer coefficients. $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$ with $t_0, t_1, t_2$ distinct integers, and $N(0) = N(1) = N(2) = 1$ (no other integer preimages).

The condition $N(i) = 1$ means: $P(x) = i$ has exactly one integer solution.

For a quadratic $ax^2 + bx + (c - i) = 0$, the discriminant is $\Delta_i = b^2 - 4a(c - i) = b^2 - 4ac + 4ai$.

Let $D = b^2 - 4ac$ (the discriminant of $P(x) = 0$). Then $\Delta_i = D + 4ai$.

For $P(x) = i$ to have integer solutions, $\Delta_i$ must be a perfect square. For exactly one integer solution, we need $\Delta_i = d_i^2$ for some non-negative integer $d_i$, and exactly one of $\frac{-b + d_i}{2a}$ and $\frac{-b - d_i}{2a}$ is an integer.

If $d_i = 0$, then $x = -b/(2a)$ is the only root, and it's an integer iff $2a | b$.

If $d_i > 0$, the two roots are $\frac{-b \pm d_i}{2a}$. For exactly one to be an integer, we need exactly one of $-b + d_i$ and $-b - d_i$ to be divisible by $2a$.

Note: $(-b + d_i) + (-b - d_i) = -2b$ and $(-b + d_i) - (-b - d_i) = 2d_i$. If $2a | (-b + d_i)$, then $-b + d_i \equiv 0 \pmod{2a}$, so $d_i \equiv b \pmod{2a}$. Then $-b - d_i \equiv -2b \pmod{2a}$. For this to be divisible by $2a$, we need $2a | 2b$, i.e., $a | b$.

So: if $a \nmid b$, then for any $d_i > 0$ with $d_i \equiv b \pmod{2a}$, exactly one root is integer. If $a | b$, then both or neither root is integer (depending on whether $d_i \equiv b \pmod{2a}$).

This is getting complex. Let me try a different approach to the problem.

Let me think about what the answer might be and try to prove it.

Conjecture: The answer is $n + 1$.

Upper bound: Bob queries $c = 0, 1, \ldots, n$. If any $N(i) \neq 1$, answer "yes" (non-surjective). If all $N(i) = 1$, answer "no" (surjective).

For this to work, we need: if $P$ is a degree $\leq n$ integer polynomial with $N(0) = N(1) = \cdots = N(n) = 1$, then $P$ is surjective (i.e., $P(x) = \pm x + b$).

Is this true? Let me think...

If $N(i) = 1$ for $i = 0, 1, \ldots, n$, there exist distinct integers $t_0, \ldots, t_n$ with $P(t_i) = i$. The polynomial $P$ of degree $\leq n$ is uniquely determined by these $n+1$ points.

But different choices of $(t_0, \ldots, t_n)$ give different polynomials. Bob doesn't know which $t_i$'s are the preimages, so he doesn't know $P$. The question is whether ALL degree $\leq n$ integer polynomials with $N(0) = \cdots = N(n) = 1$ are surjective.

Hmm, from my analysis above for $n = 2$, it seems like the only degree $\leq 2$ integer polynomials with $N(0) = N(1) = N(2) = 1$ are the linear surjective ones. Let me verify this more carefully.

For $n = 2$: $P(x) = ax^2 + bx + c$ with $N(0) = N(1) = N(2) = 1$.

There exist distinct integers $t_0, t_1, t_2$ with $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$, and no other integer maps to 0, 1, or 2.

If $a = 0$: $P$ is linear, $P(x) = bx + c$. $N(i) = 1$ for $i = 0, 1, 2$ means $b | (i - c)$ for $i = 0, 1, 2$. So $b | c, b | (1-c), b | (2-c)$. Then $b | (1-c - c) = 1 - 2c$ and $b | (2-c - c) = 2 - 2c$ and $b | (2-c - (1-c)) = 1$. So $|b| = 1$, surjective.

If $a \neq 0$: We showed (with $t_0 = 0$ WLOG... but actually we can't assume $t_0 = 0$). Let me redo.

Actually, I realize my earlier analysis was incomplete because I assumed $t_0 = 0$ by "shifting", but shifting the input variable changes the polynomial. Let me redo without that assumption.

$P(x) = ax^2 + bx + c$, $a \neq 0$, integer coefficients. $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$.

$P$ is the unique degree $\leq 2$ polynomial through $(t_0, 0), (t_1, 1), (t_2, 2)$.

By Lagrange interpolation:
$P(x) = 0 \cdot \frac{(x-t_1)(x-t_2)}{(t_0-t_1)(t_0-t_2)} + 1 \cdot \frac{(x-t_0)(x-t_2)}{(t_1-t_0)(t_1-t_2)} + 2 \cdot \frac{(x-t_0)(x-t_1)}{(t_2-t_0)(t_2-t_1)}$

$= \frac{(x-t_0)(x-t_2)}{(t_1-t_0)(t_1-t_2)} + \frac{2(x-t_0)(x-t_1)}{(t_2-t_0)(t_2-t_1)}$

The leading coefficient is:
$a = \frac{1}{(t_1-t_0)(t_1-t_2)} + \frac{2}{(t_2-t_0)(t_2-t_1)}$

$= \frac{1}{(t_1-t_0)(t_1-t_2)} + \frac{2}{(t_2-t_0)(t_2-t_1)}$

Let $u = t_1 - t_0, v = t_2 - t_1$. Then $t_2 - t_0 = u + v$, $t_1 - t_2 = -v$, $t_2 - t_1 = v$.

$a = \frac{1}{u \cdot (-v)} + \frac{2}{(u+v) \cdot v} = \frac{-1}{uv} + \frac{2}{v(u+v)} = \frac{-(u+v) + 2u}{uv(u+v)} = \frac{u - v}{uv(u+v)}$

So $a = \frac{u - v}{uv(u+v)}$ where $u = t_1 - t_0, v = t_2 - t_1$ are nonzero integers with $u + v \neq 0$ (since $t_2 \neq t_0$).

For $a$ to be a nonzero integer, we need $uv(u+v) | (u - v)$.

Note $|uv(u+v)| \geq |u| \cdot |v| \cdot |u+v|$. For $|u|, |v| \geq 1$, $|uv(u+v)| \geq |u+v|$. And $|u - v| \leq |u| + |v|$.

If $|u|, |v| \geq 2$: $|uv(u+v)| \geq 4|u+v| \geq 4 \cdot 2 = 8$ (since $|u+v| \geq 2$ when $|u|, |v| \geq 2$ and they have the same sign, or $|u+v| \geq 1$ if opposite signs). Actually, if $u$ and $v$ have opposite signs, $|u+v|$ could be small.

Let me be more careful. $|uv(u+v)| \leq |u-v|$ is needed.

If $u = v$: $a = 0$, not degree 2.
If $u = -v$: $u + v = 0$, not allowed ($t_2 = t_0$).

Let's try small values:
- $u = 1, v = 2$: $a = (1-2)/(1 \cdot 2 \cdot 3) = -1/6$. Not integer.
- $u = 2, v = 1$: $a = (2-1)/(2 \cdot 1 \cdot 3) = 1/6$. Not integer.
- $u = 1, v = -2$: $a = (1-(-2))/(1 \cdot (-2) \cdot (-1)) = 3/2$. Not integer.
- $u = -1, v = 2$: $a = (-1-2)/((-1) \cdot 2 \cdot 1) = -3/(-2) = 3/2$. Not integer.
- $u = 1, v = 3$: $a = (1-3)/(1 \cdot 3 \cdot 4) = -2/12 = -1/6$. Not integer.
- $u = 1, v = -1$: $u + v = 0$, not allowed.
- $u = 2, v = -1$: $a = (2-(-1))/(2 \cdot (-1) \cdot 1) = 3/(-2) = -3/2$. Not integer.
- $u = 1, v = -3$: $a = (1+3)/(1 \cdot (-3) \cdot (-2)) = 4/6 = 2/3$. Not integer.
- $u = 3, v = -1$: $a = (3+1)/(3 \cdot (-1) \cdot 2) = 4/(-6) = -2/3$. Not integer.
- $u = 2, v = 3$: $a = (2-3)/(2 \cdot 3 \cdot 5) = -1/30$. Not integer.
- $u = 1, v = -4$: $a = 5/(1 \cdot (-4) \cdot (-3)) = 5/12$. Not integer.
- $u = 2, v = -3$: $a = 5/(2 \cdot (-3) \cdot (-1)) = 5/6$. Not integer.
- $u = 3, v = -2$: $a = 5/(3 \cdot (-2) \cdot 1) = -5/6$. Not integer.
- $u = 4, v = -1$: $a = 5/(4 \cdot (-1) \cdot 3) = -5/12$. Not integer.
- $u = 1, v = 4$: $a = -3/(1 \cdot 4 \cdot 5) = -3/20$. Not integer.

It seems like $a$ is never an integer (other than 0) for degree 2. Let me try to prove this.

We need $uv(u+v) | (u-v)$ with $u, v \neq 0$, $u \neq v$, $u \neq -v$.

$|uv(u+v)| \geq |u-v|$ is necessary. 

WLOG assume $|u| \leq |v|$ (by symmetry of swapping $u$ and $v$ and negating... actually it's not symmetric). Let me think again.

Actually, $a = \frac{u-v}{uv(u+v)}$. For this to be a nonzero integer, $|uv(u+v)| \leq |u-v|$.

Since $|u-v| \leq |u| + |v|$ and $|uv(u+v)| \geq |u| \cdot |v| \cdot 1$ (when $|u+v| \geq 1$), we need $|u| \cdot |v| \leq |u| + |v|$.

For $|u|, |v| \geq 1$: $|u| \cdot |v| \leq |u| + |v|$ iff $(|u|-1)(|v|-1) \leq 1$, which means at least one of $|u|, |v|$ is 1, or both are 2.

Case 1: $|u| = 1$ or $|v| = 1$.
Subcase $|u| = 1$: $a = \frac{\pm 1 - v}{\pm 1 \cdot v \cdot (\pm 1 + v)}$. 

If $u = 1$: $a = \frac{1-v}{v(1+v)}$. For $|v| \geq 2$: $|v(1+v)| \geq 2 \cdot 3 = 6 > |1-v| = |v-1| \leq |v|+1$. Actually for $v = 2$: $|a| = 1/6$. For $v = -2$: $|a| = 3/2$. For $v = 3$: $|a| = 2/12 = 1/6$. For $v = -3$: $|a| = 4/6 = 2/3$. For $|v| \geq 3$: $|v(1+v)| \geq 3 \cdot 2 = 6$ (if $v > 0$) or $|v(1+v)| = |v| \cdot |1+v| \geq 3 \cdot 2 = 6$ (if $v \leq -3$, $|1+v| = |v|-1 \geq 2$). And $|1-v| \leq |v| + 1$. So $|a| \leq (|v|+1)/(|v| \cdot (|v|-1))$ for $v \leq -3$, which is $< 1$ for $|v| \geq 3$. For $v \geq 3$: $|a| = (v-1)/(v(v+1)) < 1$.

So for $|u| = 1, |v| \geq 3$: $|a| < 1$, so $a$ can't be a nonzero integer.

For $u = 1, v = 2$: $a = -1/6$. No.
For $u = 1, v = -2$: $a = 3/2$. No.
For $u = -1, v = 2$: $a = (-3)/((-1)(2)(1)) = -3/(-2) = 3/2$. No.
For $u = -1, v = -2$: $a = (1)/((-1)(-2)(-3)) = 1/(-6) = -1/6$. No.

Subcase $|v| = 1$: By similar analysis (or symmetry), same result.

Case 2: $|u| = |v| = 2$.
$u = 2, v = 2$: $a = 0$. No.
$u = 2, v = -2$: $u + v = 0$. Not allowed.
$u = -2, v = 2$: $u + v = 0$. Not allowed.
$u = -2, v = -2$: $a = 0$. No.

So there is NO degree 2 integer polynomial with $N(0) = N(1) = N(2) = 1$ (other than linear surjective ones). 

This means for $n = 2$, querying $c = 0, 1, 2$ suffices: if all three give $N = 1$, then $P$ is linear with $|b| = 1$ (surjective), so answer "no". Otherwise, answer "yes".

And we showed 2 queries don't suffice (the polynomial $P(x) = 2x^2 - x$ has $N(0) = N(1) = 1$ but is not surjective).

Wait, but I need to also check: does $P(x) = 2x^2 - x$ have $N(0) = 1$ and $N(1) = 1$? 

$P(x) = 2x^2 - x = x(2x - 1)$. $P(0) = 0$, and $2x - 1 = 0 \Rightarrow x = 1/2$ (not integer). So $N(0) = 1$. ✓
$P(x) = 1 \Rightarrow 2x^2 - x - 1 = 0 \Rightarrow (2x+1)(x-1) = 0 \Rightarrow x = 1$ or $x = -1/2$. So $N(1) = 1$. ✓
$P(x) = 2 \Rightarrow 2x^2 - x - 2 = 0$. Discriminant $= 1 + 16 = 17$, not a perfect square. $N(2) = 0$. ✓

So with 2 queries ($c = 0, 1$), Bob gets $(1, 1)$, same as surjective. He can't distinguish. With 3 queries ($c = 0, 1, 2$), he gets $(1, 1, 0)$, and the 0 reveals non-surjectivity.

But wait - the lower bound argument needs to be more careful. Bob doesn't have to query $0, 1, 2$. He could query any constants. The question is: what's the minimum number of queries such that for ANY strategy Bob uses with that many queries, he can always determine the answer?

Actually, the problem asks for the minimum cost such that Bob can GUARANTEE reaching his goal. So we need: what's the minimum $m$ such that there EXISTS a strategy for Bob using $m$ queries that always works?

So the upper bound is: there exists a strategy with $m$ queries.
The lower bound is: no strategy with $m - 1$ queries works.

For the upper bound, I've shown that querying $c = 0, 1, \ldots, n$ works if the following is true:

**Claim**: If $P$ is an integer polynomial of degree $\leq n$ with $N(0) = N(1) = \cdots = N(n) = 1$, then $P(x) = x + b$ or $P(x) = -x + b$ for some integer $b$.

For the lower bound, I need to show that with $n$ queries, Alice can fool Bob. That is, for any set of $n$ query values $c_1, \ldots, c_n$, there exist two polynomials $P_1, P_2$ of degree $\leq n$, one surjective and one not, that give the same answers to all $n$ queries.

Hmm, let me think about the lower bound more carefully.

For $n = 1$: 1 query is not enough. Bob queries some $c$. If the answer is 1, it could be $P(x) = x + b$ (surjective) or $P(x) = 2x + b'$ with $2 | (c - b')$ (non-surjective). So Bob can't tell.

For general $n$: With $n$ queries $c_1, \ldots, c_n$, if all answers are 1, Bob can't distinguish surjective from non-surjective. We need to show there's a non-surjective degree $\leq n$ polynomial with $N(c_i) = 1$ for all $i = 1, \ldots, n$.

This is equivalent to: there exist distinct integers $t_1, \ldots, t_n$ with $P(t_i) = c_i$, and $P$ has degree $\leq n$ with integer coefficients, $P$ is not surjective, and $N(c_i) = 1$ for each $i$.

Actually, the lower bound is more subtle. Bob can choose his queries adaptively. So we need to show that for any adaptive strategy using $n$ queries, Alice can respond in a way that leaves Bob uncertain.

Hmm, but actually, the problem is about worst-case guarantee. Bob wants a strategy that works for ALL polynomials. So the lower bound is: for any strategy using $n-1$ queries (even adaptive), there exists a polynomial that fools the strategy.

Let me think about this differently. Consider the information Bob gets. Each query gives him a non-negative integer (the count). If the count is not 1, he immediately knows $P$ is not surjective. The hard case is when all counts are 1.

If all $n$ queries return 1, Bob knows that $n$ specific values each have exactly one preimage. He needs to determine if $P$ is surjective.

The surjective polynomials are $P(x) = x + b$ and $P(x) = -x + b$. For these, every value has exactly one preimage.

A non-surjective polynomial that gives count 1 for $n$ specific values: we need to show such a polynomial exists for any set of $n$ values.

Let me think about this. Given $n$ query values $c_1, \ldots, c_n$ (which Bob might choose adaptively, but let's first consider non-adaptive), we want a non-surjective degree $\leq n$ polynomial $P$ with $N(c_i) = 1$ for all $i$.

Consider $P(x) = x + M \prod_{i=1}^{n} (x - t_i)$ where $t_i$ are chosen so that $P(t_i) = c_i$, i.e., $t_i + 0 = c_i$ (since the product is 0 at $t_i$). So $t_i = c_i$. Then $P(x) = x + M \prod_{i=1}^n (x - c_i)$.

This has degree $n$ (if $M \neq 0$) and $P(c_i) = c_i$ for each $i$. So $N(c_i) \geq 1$.

But we need $N(c_i) = 1$, meaning $c_i$ is the only integer preimage of $c_i$ under $P$.

$P(x) = c_i \Rightarrow x + M \prod_{j=1}^n (x - c_j) = c_i \Rightarrow (x - c_i) + M \prod_{j=1}^n (x - c_j) = 0 \Rightarrow (x - c_i)\left(1 + M \prod_{j \neq i} (x - c_j)\right) = 0$.

So $x = c_i$ or $1 + M \prod_{j \neq i} (x - c_j) = 0$.

The second equation: $M \prod_{j \neq i} (x - c_j) = -1$. Since $M$ is an integer and $\prod_{j \neq i} (x - c_j)$ is an integer for integer $x$, we need $M \cdot (\text{integer}) = -1$, so $M = \pm 1$ and $\prod_{j \neq i} (x - c_j) = \mp 1$.

If $|M| \geq 2$: $M \prod_{j \neq i}(x - c_j) = -1$ has no integer solution (since $|M \cdot \text{integer}| \geq 2$ if the integer is nonzero, and $= 0$ if it's zero). So $N(c_i) = 1$ for all $i$.

And $P(x) = x + M \prod_{j=1}^n (x - c_j)$ with $|M| \geq 2$ has degree $n \geq 2$ (for $n \geq 2$), so it's not surjective.

Wait, but for $n = 1$: $P(x) = x + M(x - c_1) = (1+M)x - Mc_1$. This is degree 1. For $|M| \geq 2$, $|1+M| \geq 3$, so not surjective. And $N(c_1) = 1$ (since $P(c_1) = c_1$ and $P$ is injective as a degree 1 polynomial with nonzero leading coefficient). 

But wait, for degree 1, $P(x) = (1+M)x - Mc_1$. $N(c_1) = 1$ always (since $P$ is linear with nonzero slope, every value in the image has exactly one preimage). But $P$ is not surjective when $|1+M| \geq 2$, i.e., $M \neq 0, -2$. So for $M = 1$: $P(x) = 2x - c_1$, not surjective, $N(c_1) = 1$. Bob queries $c_1$, gets 1, can't distinguish from $P(x) = x + b$ (surjective, also gives 1).

So for $n = 1$: 1 query gives 1, which is consistent with both surjective and non-surjective. Lower bound: 1 query not enough. ✓

For general $n$: Bob makes $n$ queries $c_1, \ldots, c_n$ (possibly adaptive). Alice responds 1 to each. Bob can't distinguish $P(x) = x + b$ (surjective) from $P(x) = x + M \prod (x - c_i)$ with $|M| \geq 2$ (non-surjective, degree $n$, $N(c_i) = 1$ for all $i$).

Wait, but Bob's queries might be adaptive. Let me think about this. If Bob queries adaptively, his second query depends on the first answer. But if Alice always responds 1, Bob's queries are determined (since the response is always 1, the adaptive strategy reduces to a fixed sequence). So the above argument works: after $n$ queries all returning 1, Bob can't distinguish.

But actually, the adaptive case is trickier. Bob might choose $c_2$ based on the answer to $c_1$. If the answer to $c_1$ is not 1, Bob might stop early (he knows it's non-surjective). But for the lower bound, we need to show that Alice can force Bob to need $n+1$ queries. Alice's strategy: always respond 1 (as long as possible). This forces Bob to continue querying. After $n$ queries all returning 1, Bob still can't distinguish, as shown.

But wait, can Alice always respond 1? She needs to have actually chosen a polynomial $P$ beforehand. The game is: Alice first chooses $P$, then Bob makes queries. So Alice can't adaptively choose $P$ based on Bob's queries.

Hmm, this is important. Alice chooses $P$ first, then Bob queries. So for the lower bound, we need: for any Bob strategy (possibly adaptive), there exists a polynomial $P$ (chosen before Bob's queries) that fools Bob.

Since Bob's strategy might be adaptive, his queries depend on previous answers. But Alice has already fixed $P$. So the answers are determined by $P$.

For the lower bound, we need: for any adaptive Bob strategy using $n$ queries, there exist two polynomials $P_1$ (surjective) and $P_2$ (non-surjective) such that Bob gets the same answers from both, and thus can't distinguish.

Since Bob's strategy is adaptive, his queries depend on answers. If $P_1$ and $P_2$ give the same answers to all queries, then Bob's query sequence is the same for both, and he can't distinguish.

So we need: for any possible sequence of $n$ queries (which could be adaptive, but if the answers are all the same, the sequence is determined), there exist $P_1$ surjective and $P_2$ non-surjective giving the same answers.

If all answers are 1: $P_1(x) = x + b$ (for appropriate $b$) gives $N(c) = 1$ for all $c$. $P_2(x) = x + M \prod_{i=1}^n (x - c_i)$ with $|M| \geq 2$ gives $N(c_i) = 1$ for all $i$. Both give the same answers (all 1s). Bob can't distinguish.

But we need to make sure $P_2$ has degree $\leq n$. $P_2(x) = x + M \prod_{i=1}^n (x - c_i)$ has degree $n$ (for $M \neq 0$). ✓

And $P_2$ is not surjective: for $n \geq 2$, degree $\geq 2$ implies not surjective. For $n = 1$, $P_2(x) = (1+M)x - Mc_1$ with $|1+M| \geq 2$ is not surjective. ✓

But wait, there's a subtlety. For the adaptive case, Bob might not query all $n$ values if he gets a non-1 answer early. But for the lower bound, we're showing that Alice can choose a $P_2$ that gives all 1s for the first $n$ queries, forcing Bob to use at least $n+1$ queries.

But Alice chooses $P$ before Bob queries. She doesn't know what Bob will query. However, for the lower bound, we use an adversarial argument: for any Bob strategy, we show there exists a $P$ that forces $n+1$ queries.

Here's the issue: Bob's queries are adaptive and depend on answers. If Alice chooses $P_2(x) = x + M \prod_{i=1}^n (x - c_i)$, this depends on $c_1, \ldots, c_n$, which are Bob's queries. But Alice doesn't know these in advance!

So the lower bound argument needs to be more careful. Let me reconsider.

For a non-adaptive Bob strategy: Bob chooses $c_1, \ldots, c_m$ upfront. Then Alice can choose $P_2$ based on these. But Bob's strategy could be adaptive.

For an adaptive strategy: Bob chooses $c_1$, gets answer, chooses $c_2$ based on answer, etc. Alice has already chosen $P$.

For the lower bound with adaptive strategies: We need to show that for any adaptive strategy with $n$ queries, there's a $P$ that fools Bob.

Key insight: Consider the "all 1s" path. If Alice chooses a surjective $P$ (say $P(x) = x$), Bob gets all 1s. His query sequence is $c_1, c_2(c_1), c_3(c_1, c_2), \ldots$ (determined by the all-1s responses). Call this sequence $c_1^*, c_2^*, \ldots, c_n^*$.

Now, Alice could instead choose $P_2(x) = x + M \prod_{i=1}^n (x - c_i^*)$ with $|M| \geq 2$. This $P_2$ gives $N(c_i^*) = 1$ for all $i$. So Bob gets the same all-1s responses, follows the same query path, and can't distinguish $P(x) = x$ from $P_2$.

But wait, Alice chooses $P$ before Bob starts querying. She doesn't know Bob's strategy. However, for the lower bound, we're showing that for any fixed Bob strategy, there exists a $P$ that fools it. The $P$ can depend on the strategy (since we're proving existence).

More precisely: Fix any Bob strategy $S$ using $n$ queries. Consider the path where all responses are 1. This determines a query sequence $c_1^*, \ldots, c_n^*$ (since the strategy is deterministic and the responses are all 1). Now:
- $P_1(x) = x$ is surjective and gives all 1s.
- $P_2(x) = x + M \prod_{i=1}^n (x - c_i^*)$ with $|M| \geq 2$ is non-surjective and gives all 1s for queries $c_1^*, \ldots, c_n^*$.

Both give the same responses, so Bob can't distinguish. Thus $n$ queries are not enough.

Wait, but I need to be more careful. When Bob queries $c_1^*$ and gets 1 (from $P_2$), he then queries $c_2^*$ (same as in the all-1s path for $P_1$). He gets 1 from $P_2$ as well. And so on. So the query sequence is the same, and all responses are 1 for both $P_1$ and $P_2$. Bob can't distinguish. ✓

But there's another subtlety: Bob might stop early if he gets a non-1 answer. In the all-1s path, he doesn't stop early (since all answers are 1). After $n$ queries, he still can't distinguish. So he needs at least $n+1$ queries.

Actually, I need to also verify that $P_2$ gives $N(c_i^*) = 1$ and not some other value. Let me re-examine.

$P_2(x) = x + M \prod_{j=1}^n (x - c_j^*)$. $P_2(c_i^*) = c_i^* + 0 = c_i^*$. So $c_i^*$ is a preimage of $c_i^*$.

$P_2(x) = c_i^* \Rightarrow x + M \prod_{j=1}^n (x - c_j^*) = c_i^* \Rightarrow (x - c_i^*) + M \prod_{j=1}^n (x - c_j^*) = 0 \Rightarrow (x - c_i^*)\left(1 + M \prod_{j \neq i} (x - c_j^*)\right) = 0$.

So $x = c_i^*$ or $1 + M \prod_{j \neq i} (x - c_j^*) = 0$.

The latter: $M \prod_{j \neq i} (x - c_j^*) = -1$. For integer $x$, $\prod_{j \neq i} (x - c_j^*)$ is an integer. So $M \cdot \text{integer} = -1$, requiring $|M| = 1$ and the product $= \mp 1$. Since $|M| \geq 2$, no integer solution. So $N(c_i^*) = 1$. ✓

Great, so the lower bound is $n + 1$.

Now for the upper bound. I need to show that $n + 1$ queries suffice. The strategy: query $c = 0, 1, \ldots, n$.

If any $N(i) \neq 1$: $P$ is not surjective (since surjective $\Rightarrow$ $N(c) = 1$ for all $c$). Answer "yes".

If all $N(0) = N(1) = \cdots = N(n) = 1$: Need to show $P$ is surjective.

There exist distinct integers $t_0, \ldots, t_n$ with $P(t_i) = i$. $P$ is the unique degree $\leq n$ polynomial through $(t_0, 0), \ldots, (t_n, n)$.

Consider $Q(x) = P(x) - x$. Then $Q(t_i) = i - t_i$ for each $i$. $Q$ has degree $\leq n$.

If $t_i = i + b$ for some constant $b$ (i.e., $t_i = i - c$ for some constant, meaning the $t_i$ are in arithmetic progression with common difference 1), then $Q(t_i) = i - (i + b) = -b$ for all $i$. So $Q$ is constant $-b$, meaning $P(x) = x - b$, surjective.

Similarly, if $t_i = -i + b$, then $Q(t_i) = i - (-i + b) = 2i - b$. $Q$ is linear: $Q(x) = -2x + (b - 2t_0)$... hmm, let me think again. If $t_i = b - i$, then $P(b-i) = i$, so $P(x) = b - x = -x + b$, surjective.

But what if the $t_i$ are not in such a nice pattern? We need to show that if $P$ has degree $\leq n$, integer coefficients, $N(i) = 1$ for $i = 0, \ldots, n$, then $P$ must be $\pm x + b$.

Hmm, but I proved this for $n = 2$ above. Let me think about the general case.

Actually, let me reconsider. The upper bound strategy of querying $0, 1, \ldots, n$ works if and only if: any degree $\leq n$ integer polynomial with $N(0) = \cdots = N(n) = 1$ is surjective.

Is this true for general $n$? Let me think about $n = 3$.

Can we find a degree 3 integer polynomial with $N(0) = N(1) = N(2) = N(3) = 1$ that is not surjective?

Using the same approach: $P(x) = x + M \prod_{i=0}^{3} (x - i)$ would have degree 4, too high. We need degree $\leq 3$.

Let me try $P(x) = x + M(x - 0)(x - 1)(x - 2) = x + Mx(x-1)(x-2)$. This has degree 3. $P(0) = 0, P(1) = 1, P(2) = 2$. $N(0) = ?$: $P(x) = 0 \Rightarrow x(1 + M(x-1)(x-2)) = 0 \Rightarrow x = 0$ or $M(x-1)(x-2) = -1$. For $|M| \geq 2$, no integer solution to the latter. So $N(0) = 1$. Similarly $N(1) = 1, N(2) = 1$.

$N(3) = ?$: $P(3) = 3 + M \cdot 3 \cdot 2 \cdot 1 = 3 + 6M$. For $N(3) = 1$, we need $P(x) = 3$ to have exactly one integer solution. $P(x) = 3 \Rightarrow x + Mx(x-1)(x-2) = 3$. If $M = 1$: $x + x(x-1)(x-2) = 3 \Rightarrow x(1 + (x-1)(x-2)) = 3 \Rightarrow x(x^2 - 3x + 3) = 3 \Rightarrow x^3 - 3x^2 + 3x - 3 = 0 \Rightarrow (x-1)^3 - 2 = 0$. No integer roots. So $N(3) = 0$. Bob queries 3 and gets 0, detects non-surjective.

If $M = -1$: $P(x) = x - x(x-1)(x-2) = x(1 - (x-1)(x-2)) = x(-x^2+3x-1) = -x^3 + 3x^2 - x$. $P(3) = -27 + 27 - 3 = -3$. $N(3) = ?$: $-x^3 + 3x^2 - x = 3 \Rightarrow x^3 - 3x^2 + x + 3 = 0$. Try $x = -1$: $-1 - 3 - 1 + 3 = -2 \neq 0$. $x = 3$: $27 - 27 + 3 + 3 = 6 \neq 0$. $x = 1$: $1 - 3 + 1 + 3 = 2 \neq 0$. No easy integer root. So $N(3) = 0$ probably.

So for this construction, $N(3) = 0$, and Bob detects it with the 4th query. Good.

But can we find a degree 3 polynomial with $N(0) = N(1) = N(2) = N(3) = 1$ that's not surjective?

We need $P(t_i) = i$ for $i = 0, 1, 2, 3$ with distinct integers $t_0, t_1, t_2, t_3$, $P$ has degree $\leq 3$ with integer coefficients, and $N(i) = 1$ for each $i$.

$P$ is determined by 4 points. Let me try to find integer-coefficient degree 3 polynomials through 4 points $(t_0, 0), (t_1, 1), (t_2, 2), (t_3, 3)$ where $t_i$ are distinct integers.

The polynomial $P(x) - x$ vanishes at $t_i$ iff $P(t_i) = t_i$, which is not what we want. Let me think differently.

$Q(x) = P(x) - x$ has $Q(t_i) = i - t_i$. If $t_i = i + b$ for all $i$, then $Q(t_i) = -b$ for all $i$, so $Q$ is constant, $P(x) = x - b$, surjective.

If the $t_i$ are not of this form, $Q$ is non-constant with degree $\leq 3$, and $Q(t_i) = i - t_i$.

For $P$ to have integer coefficients, $Q$ must have integer coefficients (since $P = Q + x$ and $x$ has integer coefficients).

So we need: a degree $\leq 3$ integer polynomial $Q$ with $Q(t_i) = i - t_i$ for 4 distinct integers $t_0, t_1, t_2, t_3$, and $P = Q + x$ has $N(i) = 1$ for $i = 0, 1, 2, 3$.

$N(i) = 1$ means $P(x) = i$ has exactly one integer solution, i.e., $Q(x) + x = i$, i.e., $Q(x) = i - x$ has exactly one integer solution.

Hmm, this is getting complicated. Let me try a different approach to the upper bound.

Alternative approach: Instead of querying $0, 1, \ldots, n$, maybe Bob should use a different strategy.

Actually, let me reconsider. Maybe the answer isn't $n+1$. Let me think about what Bob's goal is more carefully.

Bob wants to determine whether there exists an integer $k$ such that $P(x) = k$ has no integer roots. This is equivalent to: is $P(\mathbb{Z}) \neq \mathbb{Z}$?

Bob's strategy: query values and use the counts to determine the answer.

Key observation: If Bob ever gets a count $\neq 1$, he knows $P$ is not surjective (answer "yes"). If he always gets 1, he needs to determine if $P$ is surjective.

The question is: how many "all 1s" responses does Bob need before he can conclude $P$ is surjective?

If $P$ is surjective ($P(x) = \pm x + b$), every query gives 1.
If $P$ is not surjective, Bob needs to find a query that gives $\neq 1$.

So the question becomes: for a non-surjective degree $\leq n$ polynomial, how many queries does Bob need to find a value $c$ with $N(c) \neq 1$?

Equivalently: what's the maximum number of values $c$ for which a non-surjective degree $\leq n$ polynomial can have $N(c) = 1$?

If a non-surjective polynomial can have $N(c) = 1$ for at most $n$ values, then $n + 1$ queries suffice (by the pigeonhole principle, one of the $n+1$ queries must give $\neq 1$).

But if a non-surjective polynomial can have $N(c) = 1$ for more than $n$ values, then $n + 1$ queries might not suffice.

From the lower bound construction: $P(x) = x + M \prod_{i=1}^n (x - c_i)$ with $|M| \geq 2$ has $N(c_i) = 1$ for $n$ specific values. Can it have $N(c) = 1$ for more values?

$P(x) = c \Rightarrow x + M \prod_{i=1}^n (x - c_i) = c \Rightarrow (x - c) + M \prod_{i=1}^n (x - c_i) = 0$.

If $c \notin \{c_1, \ldots, c_n\}$: $(x - c) + M \prod_{i=1}^n (x - c_i) = 0$. This is a degree $n$ equation. For $N(c) = 1$, we need exactly one integer root.

For $c = c_i$: as shown, $N(c_i) = 1$ (for $|M| \geq 2$).

For other $c$: it depends. The polynomial $(x - c) + M \prod_{i=1}^n (x - c_i)$ has degree $n$. It could have 0, 1, or more integer roots.

So a non-surjective polynomial could potentially have $N(c) = 1$ for many values of $c$, not just $n$.

Hmm, so the upper bound of $n + 1$ might not work with the strategy of querying $0, 1, \ldots, n$.

Wait, but I showed for $n = 2$ that no degree 2 integer polynomial (other than surjective ones) has $N(0) = N(1) = N(2) = 1$. So for $n = 2$, the strategy works. Let me check if this generalizes.

The key claim is: **If $P$ is a degree $\leq n$ integer polynomial with $N(0) = N(1) = \cdots = N(n) = 1$, then $P$ is surjective.**

For $n = 1$: $N(0) = N(1) = 1$ implies $|a| = 1$ (shown above). ✓
For $n = 2$: $N(0) = N(1) = N(2) = 1$ implies $P$ is linear surjective (shown above). ✓

For general $n$: Let me think about this.

If $N(i) = 1$ for $i = 0, 1, \ldots, n$, there exist distinct integers $t_0, \ldots, t_n$ with $P(t_i) = i$. $P$ is the unique degree $\leq n$ polynomial through these $n + 1$ points.

Consider $R(x) = P(x) - x$. Then $R(t_i) = i - t_i$ for each $i$. $R$ has degree $\leq n$.

If $R$ is identically 0, then $P(x) = x$, surjective.
If $R$ is a nonzero constant $c$, then $P(x) = x + c$, surjective.

If $R$ has degree $\geq 1$: $R$ is a degree $\leq n$ polynomial with $R(t_i) = i - t_i$ for $n + 1$ points. 

Now, $P(x) = i$ has exactly one integer solution (namely $t_i$). $P(x) = i \Leftrightarrow R(x) = i - x \Leftrightarrow R(x) + x = i \Leftrightarrow P(x) = i$. So the condition is that $P(x) = i$ has exactly one integer root.

Let me think about the polynomial $S(x) = P(x) - x = R(x)$. We have $S(t_i) = i - t_i$.

Now, consider the polynomial $P(x) - j$ for $j \in \{0, 1, \ldots, n\}$. This has exactly one integer root $t_j$.

$P(x) - j = (x - t_j) \cdot T_j(x)$ where $T_j(x)$ is a polynomial of degree $\leq n - 1$ with no integer roots.

Since $P$ has integer coefficients and $t_j$ is an integer, $T_j(x) = \frac{P(x) - j}{x - t_j}$ has integer coefficients (by the factor theorem, since $P(t_j) = j$ and $P$ has integer coefficients, the quotient has integer coefficients... actually, this is true: if $P$ has integer coefficients and $P(a) = 0$ for integer $a$, then $(x - a) | P(x)$ in $\mathbb{Z}[x]$).

Wait, $P(x) - j$ has integer coefficients and $P(t_j) - j = 0$, so $(x - t_j) | (P(x) - j)$ in $\mathbb{Z}[x]$. So $T_j(x) \in \mathbb{Z}[x]$ with degree $n - 1$ (if $P$ has degree $n$) and no integer roots.

Hmm, this is a strong condition. $T_j$ has no integer roots for each $j = 0, \ldots, n$.

Let me think about what this implies. $P(x) - j = (x - t_j) T_j(x)$ where $T_j \in \mathbb{Z}[x]$, $\deg T_j = n - 1$ (assuming $\deg P = n$), and $T_j$ has no integer roots.

For $j \neq k$: $P(x) - j = (x - t_j) T_j(x)$ and $P(x) - k = (x - t_k) T_k(x)$. Subtracting: $(k - j) = (x - t_j) T_j(x) - (x - t_k) T_k(x)$.

At $x = t_j$: $(k - j) = 0 - (t_j - t_k) T_k(t_j)$, so $T_k(t_j) = \frac{j - k}{t_j - t_k} = \frac{k - j}{t_k - t_j}$.

Since $T_k$ has integer coefficients and $t_j$ is an integer, $T_k(t_j)$ is an integer. So $(t_k - t_j) | (k - j)$.

This must hold for all $j \neq k$ in $\{0, 1, \ldots, n\}$!

So $(t_k - t_j) | (k - j)$ for all $j \neq k$.

This is a very strong divisibility condition. Let me explore it.

Let $d_j = t_j - j$ (the "shift" at position $j$). Then $t_k - t_j = (d_k + k) - (d_j + j) = (d_k - d_j) + (k - j)$.

The condition $(t_k - t_j) | (k - j)$ becomes $((d_k - d_j) + (k - j)) | (k - j)$.

Let $m = k - j$ (nonzero). Then $(d_k - d_j + m) | m$, which means $d_k - d_j + m | m$, i.e., $d_k - d_j | m$ is not quite right. Let me redo.

$(d_k - d_j + m) | m$ means there exists an integer $q$ such that $m = q(d_k - d_j + m)$, so $m(1 - q) = q(d_k - d_j)$, so $m = \frac{q(d_k - d_j)}{1 - q}$ (for $q \neq 1$). Alternatively, $d_k - d_j + m | m$ means $d_k - d_j + m | m - (d_k - d_j + m) = -d_k + d_j$, i.e., $(d_k - d_j + m) | (d_j - d_k)$.

So $(t_k - t_j) | (j - k)$, equivalently $(t_k - t_j) | (k - j)$ (same thing since divisibility ignores sign).

So $|t_k - t_j| \leq |k - j|$ (unless $t_k = t_j$, but they're distinct) OR $t_k - t_j = \pm 1$ and $|k - j| \geq 1$... no, the condition is $(t_k - t_j) | (k - j)$, so $|t_k - t_j| \leq |k - j|$ (when $t_k \neq t_j$).

Wait, that's not quite right. $(t_k - t_j) | (k - j)$ means $|t_k - t_j| \leq |k - j|$ when $k \neq j$ and $t_k \neq t_j$. But also $t_k - t_j$ could be $\pm 1$ and $k - j$ could be anything.

Actually, $(t_k - t_j) | (k-j)$ and $k \neq j$ means $|t_k - t_j| \leq |k - j|$.

So for all $j \neq k$ in $\{0, \ldots, n\}$: $|t_k - t_j| \leq |k - j|$.

This means the map $j \mapsto t_j$ is a function from $\{0, \ldots, n\}$ to $\mathbb{Z}$ that is "1-Lipschitz": $|t_k - t_j| \leq |k - j|$.

Since $j \mapsto t_j$ is 1-Lipschitz and the $t_j$ are distinct, we have $|t_k - t_j| \leq |k - j|$ with equality possible.

If $|t_k - t_j| = |k - j|$ for all $j, k$, then $t_j = \pm j + c$ for some constant $c$, which gives $P(x) = x + c$ or $P(x) = -x + c$, surjective.

If $|t_k - t_j| < |k - j|$ for some $j, k$: Since $|t_k - t_j| \leq |k - j|$ and the $t_j$ are distinct integers, we need $|t_k - t_j| \geq 1$ for $k \neq j$. So $1 \leq |t_k - t_j| \leq |k - j|$.

But can we have $|t_k - t_j| < |k - j|$ for some pair while maintaining the Lipschitz condition for all pairs?

Consider $n = 2$: $t_0, t_1, t_2$ distinct integers with $|t_1 - t_0| \leq 1, |t_2 - t_1| \leq 1, |t_2 - t_0| \leq 2$.

$|t_1 - t_0| \leq 1$ and $t_1 \neq t_0$ means $|t_1 - t_0| = 1$.
$|t_2 - t_1| \leq 1$ and $t_2 \neq t_1$ means $|t_2 - t_1| = 1$.
$|t_2 - t_0| \leq 2$ and $t_2 \neq t_0$ means $|t_2 - t_0| \in \{1, 2\}$.

Since $|t_2 - t_0| = |t_2 - t_1 + t_1 - t_0| \leq |t_2 - t_1| + |t_1 - t_0| = 2$, and $|t_2 - t_0| \geq 1$.

If $|t_2 - t_0| = 2$: then $t_0, t_1, t_2$ are in AP with common difference $\pm 1$, so $t_j = \pm j + c$, surjective.

If $|t_2 - t_0| = 1$: $t_0, t_1, t_2$ are three distinct integers with consecutive differences of absolute value 1, and $|t_2 - t_0| = 1$. But $|t_2 - t_0| = |t_2 - t_1| + |t_1 - t_0|$ only if $t_1$ is between $t_0$ and $t_2$. If $|t_2 - t_0| = 1$ and $|t_1 - t_0| = 1$ and $|t_2 - t_1| = 1$, then $t_0, t_2$ differ by 1, and $t_1$ differs from both by 1. So $t_1$ is at distance 1 from both $t_0$ and $t_2$, but $t_0$ and $t_2$ are at distance 1. This means $t_1 = t_0 \pm 1$ and $t_1 = t_2 \pm 1 = (t_0 \pm 1) \pm 1$. If $t_2 = t_0 + 1$: $t_1 = t_0 + 1 = t_2$ (contradiction) or $t_1 = t_0 - 1$. Then $t_1 = t_0 - 1, t_2 = t_0 + 1$. Check: $|t_1 - t_0| = 1, |t_2 - t_1| = 2$. But we need $|t_2 - t_1| \leq 1$. Contradiction!

If $t_2 = t_0 - 1$: similarly, $t_1 = t_0 + 1$ (then $|t_2 - t_1| = 2 > 1$) or $t_1 = t_0 - 1 = t_2$ (contradiction). So no valid configuration.

So for $n = 2$, the only possibility is $|t_2 - t_0| = 2$, giving $t_j = \pm j + c$, surjective. ✓

For general $n$: The 1-Lipschitz condition $|t_k - t_j| \leq |k - j|$ with all $t_j$ distinct.

Since $|t_k - t_j| \leq |k - j|$ and $t_j$ are distinct, the sequence $t_0, t_1, \ldots, t_n$ has consecutive differences $|t_{j+1} - t_j| \leq 1$ and $\geq 1$ (distinct), so $|t_{j+1} - t_j| = 1$ for all $j$.

So $t_{j+1} = t_j \pm 1$ for each $j$. The sequence is a walk on $\mathbb{Z}$ with steps $\pm 1$.

Now, $|t_k - t_j| \leq |k - j|$ for all $j, k$. Since $|t_k - t_j| \leq \sum_{i=j}^{k-1} |t_{i+1} - t_i| = k - j$ (for $k > j$), this is automatically satisfied with equality when all steps are in the same direction.

But if the walk changes direction (some steps $+1        — AI历史解题过程（thinking）
#   polymath_04459         — 题目ID

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
  <problem_id>polymath_04459</problem_id>
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

Let $n$ be a given positive integer. Alice and Bob play a game. In the beginning, Alice determines an integer polynomial $P(x)$ with degree no more than $n$. Bob doesn’t know $P(x)$, and his goal is to determine whether there exists an integer $k$ such that no integer roots of $P(x) = k$ exist. 

In each round, Bob can choose a constant $c$. Alice will tell Bob an integer $k$, representing the number of integer $t$ such that $P(t) = c$. Bob needs to pay one dollar for each round. Find the minimum cost such that Bob can guarantee to reach his goal.

[i]Proposed by ltf0501[/i]

## Standard Solution

1. **Claim:**
   There is no \( k \) such that \( P(x) = k \) has no integer solution if and only if \( P(x) = x + c \) or \( P(x) = -x + c \) for some \( c \).

2. **Proof of the Claim:**
   - Suppose \( P(x) = k \) always has an integer solution. Write \( P(x) = a_m x^m + a_{m-1} x^{m-1} + \cdots + a_0 \) with \( a_m > 0 \).
   - Consider the behavior of \( P(x) \) as \( x \to \infty \) and \( x \to -\infty \).

3. **Case 1: \( m \geq 2 \) (even degree polynomial):**
   - \( P(x) \) is bounded below since \( \lim_{x \to \infty} P(x) = \lim_{x \to -\infty} P(x) = \infty \).
   - There exist \( X_+ \) and \( X_- \) such that \( P(x) > 0 \) for \( x > X_+ \) and \( x < X_- \).
   - The interval \([X_-, X_+]\) is compact, and thus \( \{ P(x) \mid x \in [X_-, X_+] \} \) achieves a minimum \( m_0 \).
   - Let \( m = \min\{m_0, 0\} \). Then \( P(x) = \lfloor m \rfloor - 1 \) has no solution, contradicting our hypothesis.

4. **Case 2: \( m \geq 3 \) (odd degree polynomial):**
   - \( P(n) \) when \( n \) is large must skip some integer value in its range.
   - \( \lim_{n \to \infty} P(n+1) - P(n) = \infty \), so there exists \( X_0 \) such that \( P(n+1) - P(n) > 1 \) for \( n > X_0 \).
   - The set \( \{ P(x) \mid x \in (-\infty, X_0] \} \) is bounded above by some \( M \).
   - For \( P(x) > M \) whenever \( x > X_1 \), pick any integer \( n_0 > \max \{ X_0, X_1 \} \).
   - \( P(n) \) must skip the value \( P(n_0) + 1 \).

5. **Conclusion:**
   - The polynomial \( P(x) \) must be of the form \( P(x) = ax + b \) with \( a \neq 0 \).
   - It is easy to see that \( a = \pm 1 \), ending our proof.

6. **Determining the Minimum Cost:**
   - Bob needs to determine whether \( P(x) = k \) has no integer roots.
   - Bob can choose \( c = 0, 1, -1, 2, -2, \ldots, n, -n \) and ask Alice for the number of integer solutions.
   - If Bob finds a \( c \) such that the number of integer solutions is zero, he can conclude that there exists a \( k \) with no integer roots.
   - The minimum number of rounds Bob needs is \( 2n + 1 \) (including zero).

The final answer is \(\boxed{2n + 1}\)

## AI's Thinking (Attempted Solution Process)

Let me think about this problem carefully.

We have a game where Alice picks an integer polynomial $P(x)$ with degree $\leq n$. Bob wants to determine whether there exists an integer $k$ such that $P(x) = k$ has no integer roots.

In each round, Bob picks a constant $c$, and Alice tells him the number of integer $t$ with $P(t) = c$. Bob pays $1 per round. Find the minimum cost for Bob to guarantee his goal.

Let me think about what Bob needs to determine. Bob wants to know: does there exist an integer $k$ such that $P(x) = k$ has no integer solutions?

Equivalently, Bob wants to know whether the image $P(\mathbb{Z})$ is all of $\mathbb{Z}$ or not. If $P(\mathbb{Z}) \neq \mathbb{Z}$, then there exists an integer $k$ not in the image, so the answer is "yes, such $k$ exists". If $P(\mathbb{Z}) = \mathbb{Z}$, then the answer is "no".

So Bob needs to determine whether $P$ maps $\mathbb{Z}$ surjectively onto $\mathbb{Z}$.

When does an integer polynomial $P$ satisfy $P(\mathbb{Z}) = \mathbb{Z}$? 

For degree 1: $P(x) = ax + b$. This is surjective iff $a = \pm 1$.

For higher degree: A polynomial of degree $\geq 2$ cannot be surjective on $\mathbb{Z}$. Actually, let me think. For degree $\geq 2$, $|P(x)| \to \infty$ as $|x| \to \infty$, but the gaps between consecutive values grow. Actually, for degree $\geq 2$, $P(\mathbb{Z})$ has density 0 in $\mathbb{Z}$, so it's definitely not surjective.

Wait, but actually we need to be more careful. For degree 1, $P(x) = ax + b$ with $a \neq 0$. The image is $a\mathbb{Z} + b$. This equals $\mathbb{Z}$ iff $|a| = 1$.

For degree 0, $P(x) = c$ constant. Image is $\{c\}$, not surjective (assuming we need all integers).

So the question reduces to: Bob needs to determine whether $P(\mathbb{Z}) = \mathbb{Z}$, which happens iff $P(x) = x + b$ or $P(x) = -x + b$ for some integer $b$.

Wait, but degree $\leq n$. If $n = 1$, then $P$ could be degree 0 or 1. If $n \geq 2$, $P$ could be degree 0, 1, or higher.

Actually wait. Let me reconsider. For degree $\geq 2$, is it always true that $P(\mathbb{Z}) \neq \mathbb{Z}$? 

Consider $P(x) = x^2$. Image is $\{0, 1, 4, 9, ...\}$, not surjective. 

Consider $P(x) = x^2 - x = x(x-1)$. Values: $0, 0, 2, 6, 12, ...$. Image is $\{0, 2, 6, 12, 20, ...\}$, not surjective.

For any polynomial of degree $d \geq 2$, $P(n+1) - P(n)$ is a polynomial of degree $d-1 \geq 1$, which goes to $\pm \infty$. So the gaps between consecutive values grow without bound, meaning the image can't be all of $\mathbb{Z}$.

So $P(\mathbb{Z}) = \mathbb{Z}$ iff $P(x) = x + b$ or $P(x) = -x + b$ for some integer $b$.

Now, Bob's goal is to determine whether $P(\mathbb{Z}) = \mathbb{Z}$ (answer: no such $k$ exists) or $P(\mathbb{Z}) \neq \mathbb{Z}$ (answer: yes, such $k$ exists).

Bob queries: for a chosen $c$, Alice returns $|\{t \in \mathbb{Z} : P(t) = c\}|$.

If $P(\mathbb{Z}) = \mathbb{Z}$, i.e., $P(x) = \pm x + b$, then for every $c$, there's exactly one integer $t$ with $P(t) = c$. So the answer is always 1.

If $P(\mathbb{Z}) \neq \mathbb{Z}$, Bob needs to detect this. 

But wait - could there be a non-surjective polynomial where every integer $c$ has at least one preimage? No, that's exactly surjectivity. If $P(\mathbb{Z}) \neq \mathbb{Z}$, there exists some $c$ with 0 preimages.

But Bob doesn't know which $c$ to query. He needs a strategy that works for any $P$.

Let me think about what information Bob gets. When Bob queries $c$, he gets $N(c) = |\{t \in \mathbb{Z} : P(t) = c\}|$.

If $P(x) = \pm x + b$: $N(c) = 1$ for all $c$.

If $P$ is degree 0, say $P(x) = b$: $N(b) = \infty$ (infinitely many $t$), $N(c) = 0$ for $c \neq b$. Wait, but the problem says Alice tells Bob "an integer $k$ representing the number of integer $t$". If there are infinitely many, what does Alice say? 

Hmm, for degree 0, $P(t) = c$ for all $t$ if $c = b$, so infinitely many. The problem says Alice tells an integer $k$. So maybe degree 0 is excluded or handled specially. Actually, the problem says "an integer $k$, representing the number of integer $t$ such that $P(t) = c$". If the count is infinite, this doesn't make sense as an integer. 

Let me re-read: "Alice will tell Bob an integer $k$, representing the number of integer $t$ such that $P(t) = c$."

For degree $\geq 1$, $P(t) = c$ has finitely many solutions (at most degree many), so $k$ is a finite non-negative integer. For degree 0, if $c$ equals the constant, there are infinitely many solutions. So maybe we should assume degree $\geq 1$, or the problem implicitly handles this.

Actually, the problem says "degree no more than $n$", and $n$ is a positive integer. So degree could be 0. But if degree is 0, then $P(x) = c_0$ for some constant, and $P(\mathbb{Z}) = \{c_0\} \neq \mathbb{Z}$ (for $n \geq 1$, there are integers not equal to $c_0$). So the answer would be "yes, such $k$ exists". But the issue is the infinite count.

Let me assume the problem is well-defined and that for degree 0, querying $c = c_0$ gives... hmm. Maybe the problem intends that $k$ can be any integer, and if there are infinitely many, Alice says something. Or maybe we should interpret "number of integer $t$" as possibly being a special value. 

Actually, I think for this problem, we can focus on the case where degree $\geq 1$ since degree 0 is a degenerate case. Or perhaps the problem means that the answer $k$ is the count, and for degree 0 with $c = c_0$, the count is infinite, which Alice would represent as... some large number? This is unclear.

Let me just proceed assuming degree $\geq 1$ is the interesting case, and for degree 0, Bob can easily detect it (e.g., query any $c$ and if the answer is "infinite" or a very large number, he knows it's degree 0).

Actually, let me reconsider. For degree $\geq 1$, the number of integer solutions to $P(t) = c$ is at most $n$ (the degree). So $k \in \{0, 1, 2, ..., n\}$ for degree $\geq 1$.

For degree 0, $P(t) = c_0$ for all $t$. If Bob queries $c_0$, the count is infinite. If he queries $c \neq c_0$, the count is 0. So if Alice must return an integer, and the count is infinite, this is problematic. But if we assume the problem is well-posed, maybe degree 0 is excluded or the infinite count is represented somehow.

Let me just focus on the main question: how many queries does Bob need?

Key insight: Bob wants to distinguish $P(x) = \pm x + b$ (surjective, answer "no") from all other polynomials (non-surjective, answer "yes").

If $P(x) = \pm x + b$, then $N(c) = 1$ for all $c$.

If $P$ is not of this form, Bob needs to find evidence. The evidence would be finding some $c$ with $N(c) \neq 1$ (either 0 or $\geq 2$).

But can Bob always find such $c$ with a bounded number of queries?

For degree 1, $P(x) = ax + b$ with $|a| \geq 2$: $N(c) = 1$ if $a | (c - b)$, and $N(c) = 0$ otherwise. So half the integers (in fact, a fraction $1 - 1/|a|$) have $N(c) = 0$. Bob can query, say, $c = 0$ and $c = 1$. If $P(x) = 2x$, then $N(0) = 1, N(1) = 0$. If $P(x) = 2x + 1$, then $N(0) = 0, N(1) = 1$. If $P(x) = x + b$, then $N(0) = 1, N(1) = 1$.

So with 2 queries, Bob can distinguish $P(x) = x + b$ from $P(x) = 2x + b'$? Not quite - what if $P(x) = 2x$ and Bob queries $c = 0$ and $c = 2$? Both give $N = 1$. So Bob got unlucky.

Hmm, so for degree 1 with $|a| \geq 2$, Bob needs to find a $c$ not divisible by $a$ (in the appropriate sense). But Bob doesn't know $a$.

Let me think about this more carefully. The question is: what's the minimum number of queries to guarantee distinguishing surjective from non-surjective?

For $n = 1$: $P(x) = ax + b$. Surjective iff $|a| = 1$. 

If $|a| = 1$: $N(c) = 1$ for all $c$.
If $|a| \geq 2$: $N(c) = 1$ if $c \equiv b \pmod{a}$, else $N(c) = 0$.
If $a = 0$: degree 0, $N(c_0) = \infty$, $N(c) = 0$ for $c \neq c_0$.

Bob needs to determine if $|a| = 1$ or not.

Strategy: Query $c = 0$. 
- If $N(0) = 0$: not surjective (since surjective would give $N(0) = 1$). Done with 1 query.
- If $N(0) = \infty$: degree 0, not surjective. Done with 1 query.
- If $N(0) = 1$: could be surjective ($|a|=1$) or non-surjective ($|a| \geq 2$ and $a | b$).

If $N(0) = 1$, query $c = 1$.
- If $N(1) = 1$: could still be either. E.g., $P(x) = x$ gives $N(0)=1, N(1)=1$. $P(x) = 2x$ gives $N(0)=1, N(1)=0$. $P(x) = 2x+1$ gives $N(0)=0, N(1)=1$. But what about $P(x) = x + 1$? $N(0) = 1, N(1) = 1$. And $P(x) = 2x$ gives $N(0)=1, N(1)=0$. So if both are 1, it could be $P(x) = x + b$ (surjective) or... is there a non-surjective degree 1 with $N(0) = N(1) = 1$? We need $a | b$ and $a | (1-b)$, i.e., $a | b$ and $a | (1-b)$, so $a | 1$, meaning $|a| = 1$. So if both $N(0) = 1$ and $N(1) = 1$, then $|a| = 1$, surjective!

Wait, that's a key insight. For degree 1: $N(0) = 1$ means $a | b$. $N(1) = 1$ means $a | (1-b)$. Together: $a | b$ and $a | (1-b)$, so $a | (b + (1-b)) = 1$, so $|a| = 1$. 

So for $n = 1$, 2 queries suffice: query $c = 0$ and $c = 1$.
- If either gives $N \neq 1$ (0 or $\infty$): not surjective, answer "yes".
- If both give $N = 1$: surjective, answer "no".

And 1 query is not enough: if Bob queries only $c = 0$ and gets $N(0) = 1$, he can't distinguish $P(x) = x$ (surjective) from $P(x) = 2x$ (non-surjective, $N(0) = 1$).

So for $n = 1$, the answer is 2.

Now for general $n$. The key question is: can Bob always determine surjectivity with a bounded number of queries, and what's that bound?

For degree $\geq 2$, $P$ is never surjective. But Bob needs to detect this. The challenge is that a degree $\geq 2$ polynomial might have $N(c) = 1$ for many values of $c$.

For example, $P(x) = x^2$. $N(0) = 1, N(1) = 2, N(2) = 0, N(4) = 2, ...$. So querying $c = 0$ gives 1, but $c = 1$ gives 2. So 2 queries detect it.

But what about $P(x) = x^2 + x$? $P(0) = 0, P(-1) = 0, P(1) = 2, P(-2) = 2, ...$. So $N(0) = 2, N(1) = 0, N(2) = 2, ...$. Querying $c = 0$ gives 2, immediately detected.

What about a degree 2 polynomial that looks like a degree 1 at specific points? Consider $P(x) = x^2$. $P(0) = 0, P(1) = 1, P(-1) = 1$. So $N(0) = 1, N(1) = 2$. If Bob queries $c = 0$, he gets 1. If he queries $c = 1$, he gets 2. So 2 queries work.

But can we construct a degree 2 polynomial where $N(0) = 1$ and $N(1) = 1$? We need $P(t) = 0$ for exactly one integer $t$, and $P(t) = 1$ for exactly one integer $t$.

$P(x) = x^2$: $N(0) = 1$ (only $x=0$), $N(1) = 2$ ($x = 1, -1$). So $N(1) = 2 \neq 1$.

$P(x) = x^2 + x$: $N(0) = 2$. No good.

$P(x) = x^2 - x$: Same as $x^2 + x$ by substitution. $N(0) = 2$.

$P(x) = 2x^2$: $N(0) = 1, N(1) = 0, N(2) = 0, N(8) = 2$. So $N(0) = 1, N(1) = 0$. Querying $c = 0, 1$ gives $1, 0$. Detected.

$P(x) = x^2 + 1$: $N(0) = 0, N(1) = 1, N(2) = 1, N(5) = 2$. So $N(0) = 0$. Detected immediately.

Hmm, what about $P(x) = x^2 + x + 1$? $P(0) = 1, P(-1) = 1, P(1) = 3, P(-2) = 3$. So $N(0) = 0, N(1) = 2$. Detected.

Let me try to find a degree 2 polynomial with $N(0) = 1$ and $N(1) = 1$.

$P(x) = ax^2 + bx + c$. We need exactly one integer root of $P(x) = 0$ and exactly one integer root of $P(x) = 1$.

For $P(x) = 0$ to have exactly one integer solution, the discriminant $b^2 - 4ac$ must be a perfect square, and $-b \pm \sqrt{b^2-4ac}$ must be divisible by $2a$, with exactly one of the two roots being an integer.

Actually, for a quadratic $ax^2 + bx + c = 0$, if the discriminant is a perfect square $d^2$, the roots are $\frac{-b \pm d}{2a}$. For exactly one integer root, we need exactly one of $\frac{-b+d}{2a}$ and $\frac{-b-d}{2a}$ to be an integer.

This is getting complicated. Let me think differently.

Can we have a degree 2 polynomial $P$ with $P(0) = 0$ and $P(1) = 1$ (so $N(0) \geq 1$ and $N(1) \geq 1$), and moreover $N(0) = 1$ and $N(1) = 1$?

$P(x) = x^2$: $P(0) = 0, P(1) = 1$. $N(0) = 1$ (only $x=0$), $N(1) = 2$ ($x = 1, -1$). So $N(1) = 2$.

$P(x) = x^2 + cx$ for some $c$: $P(0) = 0, P(1) = 1 + c$. For $P(1) = 1$, need $c = 0$, back to $x^2$.

$P(x) = ax^2 + bx + c_0$ with $P(0) = 0 \Rightarrow c_0 = 0$. $P(1) = 1 \Rightarrow a + b = 1$. So $P(x) = ax^2 + (1-a)x = x(ax + 1 - a)$. Roots of $P(x) = 0$: $x = 0$ and $x = (a-1)/a = 1 - 1/a$. For the second root to not be an integer, we need $a \nmid 1$, i.e., $|a| \neq 1$. So for $|a| \geq 2$, $N(0) = 1$ (only $x = 0$).

Roots of $P(x) = 1$: $ax^2 + (1-a)x - 1 = 0$. Discriminant: $(1-a)^2 + 4a = 1 - 2a + a^2 + 4a = a^2 + 2a + 1 = (a+1)^2$. Roots: $\frac{-(1-a) \pm (a+1)}{2a} = \frac{a-1 \pm (a+1)}{2a}$.

So roots are $\frac{a-1+a+1}{2a} = \frac{2a}{2a} = 1$ and $\frac{a-1-a-1}{2a} = \frac{-2}{2a} = \frac{-1}{a}$.

So $P(x) = 1$ has roots $x = 1$ and $x = -1/a$. For $N(1) = 1$, we need $-1/a$ to not be an integer, i.e., $|a| \neq 1$.

So for $|a| \geq 2$: $P(x) = ax^2 + (1-a)x$ has $N(0) = 1$ and $N(1) = 1$!

For example, $P(x) = 2x^2 - x$. $P(0) = 0, P(1) = 1$. $N(0) = 1$ (root $x=0$; other root $x = 1/2$, not integer). $N(1) = 1$ (root $x=1$; other root $x = -1/2$, not integer).

So with queries $c = 0$ and $c = 1$, Bob gets $N(0) = 1, N(1) = 1$, which is the same as a surjective polynomial! So 2 queries are not enough for $n = 2$.

So Bob needs more queries for $n = 2$. Let's see if 3 queries suffice.

Query $c = 0, 1, 2$. For $P(x) = 2x^2 - x$: $P(0) = 0, P(1) = 1, P(2) = 8 - 2 = 6$. So $N(2) = ?$. $2x^2 - x = 2 \Rightarrow 2x^2 - x - 2 = 0$. Discriminant: $1 + 16 = 17$, not a perfect square. So $N(2) = 0$. Detected!

But can we find a degree 2 polynomial with $N(0) = N(1) = N(2) = 1$?

$P(x) = ax^2 + bx + c$ with $P(0) = 0, P(1) = 1, P(2) = 2$. So $c = 0, a + b = 1, 4a + 2b = 2$. From $a + b = 1$ and $4a + 2b = 2$: $4a + 2(1-a) = 2 \Rightarrow 2a + 2 = 2 \Rightarrow a = 0$. So $P(x) = x$, degree 1. 

So there's no degree 2 polynomial passing through $(0,0), (1,1), (2,2)$. The only polynomial of degree $\leq 2$ through these points is $P(x) = x$.

But wait, we need $N(0) = N(1) = N(2) = 1$, not necessarily $P(0) = 0, P(1) = 1, P(2) = 2$. The preimage could be different integers.

Let me reconsider. We need: there exists exactly one integer $t_0$ with $P(t_0) = 0$, exactly one integer $t_1$ with $P(t_1) = 1$, exactly one integer $t_2$ with $P(t_2) = 2$.

For a surjective polynomial $P(x) = x + b$: $t_0 = -b, t_1 = 1-b, t_2 = 2-b$. All distinct, $N(0) = N(1) = N(2) = 1$.

For a non-surjective polynomial, we need to find one where $N(0) = N(1) = N(2) = 1$.

Let's try $P(x) = 2x^2 - x$ again. $N(0) = 1, N(1) = 1, N(2) = 0$. So $N(2) = 0$, detected.

Can we find a degree 2 polynomial with $N(0) = N(1) = N(2) = 1$?

Let me think about this more generally. A degree 2 polynomial $P(x) = ax^2 + bx + c$ with $a \neq 0$. For each value $v$, $P(x) = v$ has at most 2 integer solutions. $N(v) = 1$ means exactly one integer solution.

The image $P(\mathbb{Z})$ for a degree 2 polynomial: as $x \to \pm\infty$, $P(x) \to +\infty$ (if $a > 0$) or $-\infty$ (if $a < 0$). The image is "sparse" for large $|x|$.

Let me try to construct such a polynomial. We need $P$ to take values 0, 1, 2 each at exactly one integer point.

Let's say $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$ with $t_0, t_1, t_2$ integers, and no other integer maps to 0, 1, or 2.

If $t_0, t_1, t_2$ are distinct, then $P$ is determined (degree 2 through 3 points). Let's try $t_0 = 0, t_1 = 1, t_2 = 3$ (not 2, to avoid the linear case).

$P(0) = 0, P(1) = 1, P(3) = 2$. $P(x) = ax^2 + bx$. $a + b = 1, 9a + 3b = 2$. From first: $b = 1 - a$. $9a + 3(1-a) = 2 \Rightarrow 6a + 3 = 2 \Rightarrow a = -1/6$. Not integer.

Try $t_0 = 0, t_1 = 2, t_2 = 3$. $P(0) = 0, P(2) = 1, P(3) = 2$. $P(x) = ax^2 + bx$. $4a + 2b = 1, 9a + 3b = 2$. From first: $b = (1-4a)/2$. $9a + 3(1-4a)/2 = 2 \Rightarrow 18a + 3 - 12a = 4 \Rightarrow 6a = 1 \Rightarrow a = 1/6$. Not integer.

Hmm, it's hard to get integer coefficients. Let me try a different approach.

$P(x) = ax^2 + bx + c$ with integer $a, b, c$, $a \neq 0$. We need $N(0) = N(1) = N(2) = 1$.

For $N(v) = 1$: $ax^2 + bx + (c - v) = 0$ has exactly one integer root. This means the discriminant $b^2 - 4a(c-v)$ is a perfect square, say $d_v^2$, and exactly one of $\frac{-b + d_v}{2a}$ and $\frac{-b - d_v}{2a}$ is an integer.

This is quite constrained. Let me try specific examples.

$P(x) = x^2 + x = x(x+1)$. $P(0) = 0, P(-1) = 0$, so $N(0) = 2$. No good.

$P(x) = x^2 + 2x = x(x+2)$. $P(0) = 0, P(-2) = 0$, $N(0) = 2$. No good.

$P(x) = 2x^2 + 3x + 1 = (2x+1)(x+1)$. $P(-1) = 0, P(0) = 1, P(1) = 6$. $N(0) = 1$ (only $x = -1$, since $x = -1/2$ is not integer). $N(1) = 1$ (only $x = 0$; $2x^2 + 3x = 0 \Rightarrow x(2x+3) = 0 \Rightarrow x = 0$ or $x = -3/2$, so $N(1) = 1$). $N(2) = ?$: $2x^2 + 3x + 1 = 2 \Rightarrow 2x^2 + 3x - 1 = 0$. Discriminant $9 + 8 = 17$, not a perfect square. $N(2) = 0$. Detected at $c = 2$.

Let me try to find one where $N(0) = N(1) = N(2) = 1$.

$P(x) = 2x^2 + 3x + 1$. $N(0) = 1, N(1) = 1, N(2) = 0$. Close but $N(2) = 0$.

What if I shift? $P(x) = 2x^2 + 3x + 1 + k$ for some $k$. Then $N(k) = 1, N(k+1) = 1, N(k+2) = 0$. Bob queries $0, 1, 2$. If $k = 0$, he gets $1, 1, 0$. If $k = -1$, he gets $N(0) = N(1) = 1, N(2) = 1$... wait let me recompute.

$P(x) = 2x^2 + 3x + 1$. Values: $P(-2) = 8 - 6 + 1 = 3, P(-1) = 2 - 3 + 1 = 0, P(0) = 1, P(1) = 6, P(2) = 15$.

So $N(0) = 1$ (from $x = -1$), $N(1) = 1$ (from $x = 0$), $N(2) = 0$, $N(3) = 1$ (from $x = -2$), $N(6) = 1$ (from $x = 1$), etc.

So if Bob queries $c = 0, 1, 2$, he gets $1, 1, 0$. The third query detects it.

Can we find a degree 2 polynomial where $N(0) = N(1) = N(2) = 1$?

Let me think about it differently. For a degree 2 polynomial $P(x) = ax^2 + bx + c$ with $a > 0$, the image $P(\mathbb{Z})$ is a subset of $[P_{\min}, \infty) \cap \mathbb{Z}$ where $P_{\min}$ is the minimum value. For large values, the gaps between consecutive image values grow. So for large enough $c$, $N(c) = 0$. But 0, 1, 2 might all be in the image with unique preimages.

Let me try to be more systematic. I want $P(x) = ax^2 + bx + c$ with:
- $P(x) = 0$ has exactly one integer root
- $P(x) = 1$ has exactly one integer root
- $P(x) = 2$ has exactly one integer root

Let's say the integer roots are $r_0, r_1, r_2$ respectively (with $r_0, r_1, r_2$ not necessarily distinct, but if two are the same, that would mean $P(r) = 0 = 1$, contradiction, so they're distinct).

So $P(r_0) = 0, P(r_1) = 1, P(r_2) = 2$ with $r_0, r_1, r_2$ distinct integers. This gives us 3 equations in 3 unknowns ($a, b, c$), so $P$ is determined.

$P(x) = a(x - r_0)(x - r_2) + \frac{2(x - r_0)}{r_2 - r_0}$... hmm, let me use Lagrange interpolation.

Actually, $P$ is the unique degree $\leq 2$ polynomial through $(r_0, 0), (r_1, 1), (r_2, 2)$. For this to have degree exactly 2, we need $r_0, r_1, r_2$ to not be in arithmetic progression (if they were, $P$ would be linear).

If $r_0, r_1, r_2$ are in arithmetic progression, $P(x) = x - r_0$ (linear, surjective). So for degree 2, we need them not in AP.

Let me try $r_0 = 0, r_1 = 1, r_2 = 3$. Then $P(0) = 0, P(1) = 1, P(3) = 2$.

$P(x) = ax^2 + bx + c$. $c = 0, a + b = 1, 9a + 3b = 2$. $b = 1 - a, 9a + 3 - 3a = 2, 6a = -1, a = -1/6$. Not integer.

Try $r_0 = 0, r_1 = 2, r_2 = 3$. $P(0) = 0, P(2) = 1, P(3) = 2$. $c = 0, 4a + 2b = 1, 9a + 3b = 2$. From first: $b = (1 - 4a)/2$. $9a + 3(1-4a)/2 = 2 \Rightarrow 18a + 3 - 12a = 4 \Rightarrow 6a = 1 \Rightarrow a = 1/6$. Not integer.

Try $r_0 = 0, r_1 = 1, r_2 = -1$. $P(0) = 0, P(1) = 1, P(-1) = 2$. $c = 0, a + b = 1, a - b = 2$. $2a = 3, a = 3/2$. Not integer.

Try $r_0 = 1, r_1 = 0, r_2 = -1$. $P(1) = 0, P(0) = 1, P(-1) = 2$. $c = 1, a + b + 1 = 0, a - b + 1 = 2$. $a + b = -1, a - b = 1$. $a = 0, b = -1$. Linear! $P(x) = -x + 1$. This is surjective.

Try $r_0 = 0, r_1 = 2, r_2 = 5$. $P(0) = 0, P(2) = 1, P(5) = 2$. $c = 0, 4a + 2b = 1, 25a + 5b = 2$. $b = (1-4a)/2, 25a + 5(1-4a)/2 = 2 \Rightarrow 50a + 5 - 20a = 4 \Rightarrow 30a = -1 \Rightarrow a = -1/30$. Not integer.

It seems hard to get integer coefficients. Let me think about why.

For $P(x) = ax^2 + bx + c$ with $P(r_0) = 0, P(r_1) = 1, P(r_2) = 2$:

Using the Lagrange interpolation formula, $a$ is determined by the divided difference:
$a = \frac{1}{(r_0 - r_1)(r_0 - r_2)} \cdot 0 + \frac{1}{(r_1 - r_0)(r_1 - r_2)} \cdot 1 + \frac{1}{(r_2 - r_0)(r_2 - r_1)} \cdot 2$

Hmm, this is getting complicated. Let me think about it differently.

Actually, let me consider the polynomial $Q(x) = P(x) - x$. Then $Q(r_0) = -r_0, Q(r_1) = 1 - r_1, Q(r_2) = 2 - r_2$. If $P$ has degree 2, then $Q$ has degree 2 (since $P$ has degree 2 and we subtract a degree 1 polynomial). $Q$ is a degree 2 polynomial with $Q(r_i) = i - r_i$ for $i = 0, 1, 2$.

Hmm, this doesn't simplify things much.

Let me try a different approach. Instead of trying to construct specific examples, let me think about the general structure.

The question is: for degree $\leq n$, how many queries does Bob need?

Claim: The answer is $n + 1$.

Reasoning: Bob queries $c = 0, 1, 2, \ldots, n$. If all responses are 1, then $P$ is surjective (i.e., $P(x) = \pm x + b$). If any response is not 1, $P$ is not surjective.

Why would this work? If $N(0) = N(1) = \cdots = N(n) = 1$, then there exist integers $t_0, t_1, \ldots, t_n$ with $P(t_i) = i$ for each $i$. Since $P$ has degree $\leq n$, and we have $n + 1$ points $(t_i, i)$, $P$ is the unique polynomial of degree $\leq n$ through these points.

Now, if $t_0, t_1, \ldots, t_n$ are all distinct, then $P$ is determined by these $n+1$ points. But we also know $P(t_i) = i$, so $P$ interpolates the points $(t_0, 0), (t_1, 1), \ldots, (t_n, n)$.

If $t_i = t_j$ for some $i \neq j$, then $P(t_i) = i$ and $P(t_j) = j$ with $t_i = t_j$, contradiction since $i \neq j$. So all $t_i$ are distinct.

Now, the key question: if $P$ is a degree $\leq n$ polynomial with $P(t_i) = i$ for $n+1$ distinct integers $t_0, \ldots, t_n$, and $N(i) = 1$ for each $i$ (meaning $t_i$ is the ONLY integer with $P(t) = i$), does this force $P(x) = x + b$ or $P(x) = -x + b$?

Hmm, not necessarily. The condition $N(i) = 1$ for $i = 0, \ldots, n$ only tells us about $n+1$ specific values. $P$ could be a higher degree polynomial that happens to have unique preimages for these values.

Wait, but I need to think about this more carefully. Let me consider what constraints $N(i) = 1$ for $i = 0, 1, \ldots, n$ places on $P$.

Actually, let me reconsider the problem. The question is about the minimum cost, so we need both an upper bound (a strategy for Bob) and a lower bound (showing Alice can force Bob to use at least that many queries).

Let me think about the upper bound first.

Upper bound strategy: Bob queries $c = 0, 1, \ldots, n$.

Case 1: Some $N(i) \neq 1$ for some $i \in \{0, \ldots, n\}$. Then $P$ is not surjective (since surjective polynomials have $N(c) = 1$ for all $c$). Bob answers "yes, such $k$ exists".

Case 2: $N(i) = 1$ for all $i = 0, \ldots, n$. Bob needs to determine if $P$ is surjective.

In Case 2, there exist distinct integers $t_0, \ldots, t_n$ with $P(t_i) = i$. The polynomial $P$ of degree $\leq n$ is uniquely determined by these $n+1$ points. But Bob doesn't know $t_0, \ldots, t_n$! He only knows that $N(i) = 1$ for each $i$.

Hmm, so Bob doesn't actually know $P$ from the queries. He just knows that each of $0, 1, \ldots, n$ has exactly one preimage. This doesn't uniquely determine $P$.

For example, with $n = 2$: $P(x) = x$ gives $N(0) = N(1) = N(2) = 1$ (surjective). $P(x) = 2x^2 - x$ gives $N(0) = 1, N(1) = 1, N(2) = 0$ (not surjective, detected). But is there a degree 2 polynomial with $N(0) = N(1) = N(2) = 1$ that is not surjective?

From my earlier analysis, it seems hard to construct such a polynomial with integer coefficients. Let me think about whether it's possible.

$P(x) = ax^2 + bx + c$, degree 2, $N(0) = N(1) = N(2) = 1$.

There exist distinct integers $t_0, t_1, t_2$ with $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$.

$P$ is the unique degree $\leq 2$ polynomial through $(t_0, 0), (t_1, 1), (t_2, 2)$.

For $P$ to have degree 2, $t_0, t_1, t_2$ must not be in arithmetic progression. (If in AP, the interpolating polynomial is linear.)

If $t_0, t_1, t_2$ are in AP with common difference $d$, then $P(x) = \frac{1}{d}(x - t_0)$, which is linear. For this to have integer coefficients, $d | 1$, so $d = \pm 1$, giving $P(x) = x - t_0$ or $P(x) = -(x - t_0) = -x + t_0$. These are surjective.

If $t_0, t_1, t_2$ are not in AP, $P$ has degree 2. We need $P$ to have integer coefficients and $N(0) = N(1) = N(2) = 1$.

Let me parametrize. WLOG, by shifting, let $t_0 = 0$. So $P(0) = 0$, meaning $c = 0$. $P(x) = ax^2 + bx$.

$P(t_1) = 1 \Rightarrow at_1^2 + bt_1 = 1 \Rightarrow t_1(at_1 + b) = 1$.

Since $t_1$ is an integer and $at_1 + b$ is an integer, we need $t_1 \cdot (at_1 + b) = 1$. So either $t_1 = 1, at_1 + b = 1$ (i.e., $a + b = 1$) or $t_1 = -1, at_1 + b = -1$ (i.e., $-a + b = -1$, i.e., $b = a - 1$).

Case A: $t_1 = 1, a + b = 1$. Then $P(x) = ax^2 + (1-a)x$.
$P(t_2) = 2 \Rightarrow at_2^2 + (1-a)t_2 = 2 \Rightarrow at_2^2 + t_2 - at_2 = 2 \Rightarrow a(t_2^2 - t_2) + t_2 = 2 \Rightarrow a \cdot t_2(t_2 - 1) = 2 - t_2$.

If $t_2 \neq 0, 1$: $a = \frac{2 - t_2}{t_2(t_2 - 1)}$.

For $a$ to be a nonzero integer, $t_2(t_2 - 1) | (2 - t_2)$.

Let $t_2 = 2$: $a = 0/2 = 0$. Degree 0, not degree 2.
$t_2 = 3$: $a = -1/6$. Not integer.
$t_2 = -1$: $a = 3/2$. Not integer.
$t_2 = 4$: $a = -2/12 = -1/6$. Not integer.
$t_2 = -2$: $a = 4/6 = 2/3$. Not integer.
$t_2 = 5$: $a = -3/20$. Not integer.
$t_2 = -3$: $a = 5/12$. Not integer.

For $|t_2|$ large, $|a| \approx 1/|t_2|$, so $|a| < 1$ for $|t_2| \geq 3$, meaning $a = 0$ is the only integer possibility, but that gives degree $\leq 1$.

So in Case A, there's no degree 2 polynomial with integer coefficients!

Case B: $t_1 = -1, b = a - 1$. $P(x) = ax^2 + (a-1)x$.
$P(t_2) = 2 \Rightarrow at_2^2 + (a-1)t_2 = 2 \Rightarrow a(t_2^2 + t_2) - t_2 = 2 \Rightarrow a \cdot t_2(t_2 + 1) = 2 + t_2$.

If $t_2 \neq 0, -1$: $a = \frac{2 + t_2}{t_2(t_2 + 1)}$.

$t_2 = 1$: $a = 3/2$. Not integer.
$t_2 = 2$: $a = 4/6 = 2/3$. Not integer.
$t_2 = -2$: $a = 0/2 = 0$. Degree 0.
$t_2 = 3$: $a = 5/12$. Not integer.
$t_2 = -3$: $a = -1/6$. Not integer.

Again, no integer solutions with $a \neq 0$.

So with $t_0 = 0$, there's no degree 2 integer polynomial with $N(0) = N(1) = N(2) = 1$ (other than the linear surjective ones).

But wait, I assumed $t_0 = 0$ WLOG by shifting. But shifting $P$ changes it. Let me redo without this assumption.

Actually, the shift argument doesn't work directly because we're looking at specific values 0, 1, 2. Let me redo.

General case: $P(x) = ax^2 + bx + c$, $a \neq 0$, integer coefficients. $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$ with $t_0, t_1, t_2$ distinct integers, and $N(0) = N(1) = N(2) = 1$ (no other integer preimages).

The condition $N(i) = 1$ means: $P(x) = i$ has exactly one integer solution.

For a quadratic $ax^2 + bx + (c - i) = 0$, the discriminant is $\Delta_i = b^2 - 4a(c - i) = b^2 - 4ac + 4ai$.

Let $D = b^2 - 4ac$ (the discriminant of $P(x) = 0$). Then $\Delta_i = D + 4ai$.

For $P(x) = i$ to have integer solutions, $\Delta_i$ must be a perfect square. For exactly one integer solution, we need $\Delta_i = d_i^2$ for some non-negative integer $d_i$, and exactly one of $\frac{-b + d_i}{2a}$ and $\frac{-b - d_i}{2a}$ is an integer.

If $d_i = 0$, then $x = -b/(2a)$ is the only root, and it's an integer iff $2a | b$.

If $d_i > 0$, the two roots are $\frac{-b \pm d_i}{2a}$. For exactly one to be an integer, we need exactly one of $-b + d_i$ and $-b - d_i$ to be divisible by $2a$.

Note: $(-b + d_i) + (-b - d_i) = -2b$ and $(-b + d_i) - (-b - d_i) = 2d_i$. If $2a | (-b + d_i)$, then $-b + d_i \equiv 0 \pmod{2a}$, so $d_i \equiv b \pmod{2a}$. Then $-b - d_i \equiv -2b \pmod{2a}$. For this to be divisible by $2a$, we need $2a | 2b$, i.e., $a | b$.

So: if $a \nmid b$, then for any $d_i > 0$ with $d_i \equiv b \pmod{2a}$, exactly one root is integer. If $a | b$, then both or neither root is integer (depending on whether $d_i \equiv b \pmod{2a}$).

This is getting complex. Let me try a different approach to the problem.

Let me think about what the answer might be and try to prove it.

Conjecture: The answer is $n + 1$.

Upper bound: Bob queries $c = 0, 1, \ldots, n$. If any $N(i) \neq 1$, answer "yes" (non-surjective). If all $N(i) = 1$, answer "no" (surjective).

For this to work, we need: if $P$ is a degree $\leq n$ integer polynomial with $N(0) = N(1) = \cdots = N(n) = 1$, then $P$ is surjective (i.e., $P(x) = \pm x + b$).

Is this true? Let me think...

If $N(i) = 1$ for $i = 0, 1, \ldots, n$, there exist distinct integers $t_0, \ldots, t_n$ with $P(t_i) = i$. The polynomial $P$ of degree $\leq n$ is uniquely determined by these $n+1$ points.

But different choices of $(t_0, \ldots, t_n)$ give different polynomials. Bob doesn't know which $t_i$'s are the preimages, so he doesn't know $P$. The question is whether ALL degree $\leq n$ integer polynomials with $N(0) = \cdots = N(n) = 1$ are surjective.

Hmm, from my analysis above for $n = 2$, it seems like the only degree $\leq 2$ integer polynomials with $N(0) = N(1) = N(2) = 1$ are the linear surjective ones. Let me verify this more carefully.

For $n = 2$: $P(x) = ax^2 + bx + c$ with $N(0) = N(1) = N(2) = 1$.

There exist distinct integers $t_0, t_1, t_2$ with $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$, and no other integer maps to 0, 1, or 2.

If $a = 0$: $P$ is linear, $P(x) = bx + c$. $N(i) = 1$ for $i = 0, 1, 2$ means $b | (i - c)$ for $i = 0, 1, 2$. So $b | c, b | (1-c), b | (2-c)$. Then $b | (1-c - c) = 1 - 2c$ and $b | (2-c - c) = 2 - 2c$ and $b | (2-c - (1-c)) = 1$. So $|b| = 1$, surjective.

If $a \neq 0$: We showed (with $t_0 = 0$ WLOG... but actually we can't assume $t_0 = 0$). Let me redo.

Actually, I realize my earlier analysis was incomplete because I assumed $t_0 = 0$ by "shifting", but shifting the input variable changes the polynomial. Let me redo without that assumption.

$P(x) = ax^2 + bx + c$, $a \neq 0$, integer coefficients. $P(t_0) = 0, P(t_1) = 1, P(t_2) = 2$.

$P$ is the unique degree $\leq 2$ polynomial through $(t_0, 0), (t_1, 1), (t_2, 2)$.

By Lagrange interpolation:
$P(x) = 0 \cdot \frac{(x-t_1)(x-t_2)}{(t_0-t_1)(t_0-t_2)} + 1 \cdot \frac{(x-t_0)(x-t_2)}{(t_1-t_0)(t_1-t_2)} + 2 \cdot \frac{(x-t_0)(x-t_1)}{(t_2-t_0)(t_2-t_1)}$

$= \frac{(x-t_0)(x-t_2)}{(t_1-t_0)(t_1-t_2)} + \frac{2(x-t_0)(x-t_1)}{(t_2-t_0)(t_2-t_1)}$

The leading coefficient is:
$a = \frac{1}{(t_1-t_0)(t_1-t_2)} + \frac{2}{(t_2-t_0)(t_2-t_1)}$

$= \frac{1}{(t_1-t_0)(t_1-t_2)} + \frac{2}{(t_2-t_0)(t_2-t_1)}$

Let $u = t_1 - t_0, v = t_2 - t_1$. Then $t_2 - t_0 = u + v$, $t_1 - t_2 = -v$, $t_2 - t_1 = v$.

$a = \frac{1}{u \cdot (-v)} + \frac{2}{(u+v) \cdot v} = \frac{-1}{uv} + \frac{2}{v(u+v)} = \frac{-(u+v) + 2u}{uv(u+v)} = \frac{u - v}{uv(u+v)}$

So $a = \frac{u - v}{uv(u+v)}$ where $u = t_1 - t_0, v = t_2 - t_1$ are nonzero integers with $u + v \neq 0$ (since $t_2 \neq t_0$).

For $a$ to be a nonzero integer, we need $uv(u+v) | (u - v)$.

Note $|uv(u+v)| \geq |u| \cdot |v| \cdot |u+v|$. For $|u|, |v| \geq 1$, $|uv(u+v)| \geq |u+v|$. And $|u - v| \leq |u| + |v|$.

If $|u|, |v| \geq 2$: $|uv(u+v)| \geq 4|u+v| \geq 4 \cdot 2 = 8$ (since $|u+v| \geq 2$ when $|u|, |v| \geq 2$ and they have the same sign, or $|u+v| \geq 1$ if opposite signs). Actually, if $u$ and $v$ have opposite signs, $|u+v|$ could be small.

Let me be more careful. $|uv(u+v)| \leq |u-v|$ is needed.

If $u = v$: $a = 0$, not degree 2.
If $u = -v$: $u + v = 0$, not allowed ($t_2 = t_0$).

Let's try small values:
- $u = 1, v = 2$: $a = (1-2)/(1 \cdot 2 \cdot 3) = -1/6$. Not integer.
- $u = 2, v = 1$: $a = (2-1)/(2 \cdot 1 \cdot 3) = 1/6$. Not integer.
- $u = 1, v = -2$: $a = (1-(-2))/(1 \cdot (-2) \cdot (-1)) = 3/2$. Not integer.
- $u = -1, v = 2$: $a = (-1-2)/((-1) \cdot 2 \cdot 1) = -3/(-2) = 3/2$. Not integer.
- $u = 1, v = 3$: $a = (1-3)/(1 \cdot 3 \cdot 4) = -2/12 = -1/6$. Not integer.
- $u = 1, v = -1$: $u + v = 0$, not allowed.
- $u = 2, v = -1$: $a = (2-(-1))/(2 \cdot (-1) \cdot 1) = 3/(-2) = -3/2$. Not integer.
- $u = 1, v = -3$: $a = (1+3)/(1 \cdot (-3) \cdot (-2)) = 4/6 = 2/3$. Not integer.
- $u = 3, v = -1$: $a = (3+1)/(3 \cdot (-1) \cdot 2) = 4/(-6) = -2/3$. Not integer.
- $u = 2, v = 3$: $a = (2-3)/(2 \cdot 3 \cdot 5) = -1/30$. Not integer.
- $u = 1, v = -4$: $a = 5/(1 \cdot (-4) \cdot (-3)) = 5/12$. Not integer.
- $u = 2, v = -3$: $a = 5/(2 \cdot (-3) \cdot (-1)) = 5/6$. Not integer.
- $u = 3, v = -2$: $a = 5/(3 \cdot (-2) \cdot 1) = -5/6$. Not integer.
- $u = 4, v = -1$: $a = 5/(4 \cdot (-1) \cdot 3) = -5/12$. Not integer.
- $u = 1, v = 4$: $a = -3/(1 \cdot 4 \cdot 5) = -3/20$. Not integer.

It seems like $a$ is never an integer (other than 0) for degree 2. Let me try to prove this.

We need $uv(u+v) | (u-v)$ with $u, v \neq 0$, $u \neq v$, $u \neq -v$.

$|uv(u+v)| \geq |u-v|$ is necessary. 

WLOG assume $|u| \leq |v|$ (by symmetry of swapping $u$ and $v$ and negating... actually it's not symmetric). Let me think again.

Actually, $a = \frac{u-v}{uv(u+v)}$. For this to be a nonzero integer, $|uv(u+v)| \leq |u-v|$.

Since $|u-v| \leq |u| + |v|$ and $|uv(u+v)| \geq |u| \cdot |v| \cdot 1$ (when $|u+v| \geq 1$), we need $|u| \cdot |v| \leq |u| + |v|$.

For $|u|, |v| \geq 1$: $|u| \cdot |v| \leq |u| + |v|$ iff $(|u|-1)(|v|-1) \leq 1$, which means at least one of $|u|, |v|$ is 1, or both are 2.

Case 1: $|u| = 1$ or $|v| = 1$.
Subcase $|u| = 1$: $a = \frac{\pm 1 - v}{\pm 1 \cdot v \cdot (\pm 1 + v)}$. 

If $u = 1$: $a = \frac{1-v}{v(1+v)}$. For $|v| \geq 2$: $|v(1+v)| \geq 2 \cdot 3 = 6 > |1-v| = |v-1| \leq |v|+1$. Actually for $v = 2$: $|a| = 1/6$. For $v = -2$: $|a| = 3/2$. For $v = 3$: $|a| = 2/12 = 1/6$. For $v = -3$: $|a| = 4/6 = 2/3$. For $|v| \geq 3$: $|v(1+v)| \geq 3 \cdot 2 = 6$ (if $v > 0$) or $|v(1+v)| = |v| \cdot |1+v| \geq 3 \cdot 2 = 6$ (if $v \leq -3$, $|1+v| = |v|-1 \geq 2$). And $|1-v| \leq |v| + 1$. So $|a| \leq (|v|+1)/(|v| \cdot (|v|-1))$ for $v \leq -3$, which is $< 1$ for $|v| \geq 3$. For $v \geq 3$: $|a| = (v-1)/(v(v+1)) < 1$.

So for $|u| = 1, |v| \geq 3$: $|a| < 1$, so $a$ can't be a nonzero integer.

For $u = 1, v = 2$: $a = -1/6$. No.
For $u = 1, v = -2$: $a = 3/2$. No.
For $u = -1, v = 2$: $a = (-3)/((-1)(2)(1)) = -3/(-2) = 3/2$. No.
For $u = -1, v = -2$: $a = (1)/((-1)(-2)(-3)) = 1/(-6) = -1/6$. No.

Subcase $|v| = 1$: By similar analysis (or symmetry), same result.

Case 2: $|u| = |v| = 2$.
$u = 2, v = 2$: $a = 0$. No.
$u = 2, v = -2$: $u + v = 0$. Not allowed.
$u = -2, v = 2$: $u + v = 0$. Not allowed.
$u = -2, v = -2$: $a = 0$. No.

So there is NO degree 2 integer polynomial with $N(0) = N(1) = N(2) = 1$ (other than linear surjective ones). 

This means for $n = 2$, querying $c = 0, 1, 2$ suffices: if all three give $N = 1$, then $P$ is linear with $|b| = 1$ (surjective), so answer "no". Otherwise, answer "yes".

And we showed 2 queries don't suffice (the polynomial $P(x) = 2x^2 - x$ has $N(0) = N(1) = 1$ but is not surjective).

Wait, but I need to also check: does $P(x) = 2x^2 - x$ have $N(0) = 1$ and $N(1) = 1$? 

$P(x) = 2x^2 - x = x(2x - 1)$. $P(0) = 0$, and $2x - 1 = 0 \Rightarrow x = 1/2$ (not integer). So $N(0) = 1$. ✓
$P(x) = 1 \Rightarrow 2x^2 - x - 1 = 0 \Rightarrow (2x+1)(x-1) = 0 \Rightarrow x = 1$ or $x = -1/2$. So $N(1) = 1$. ✓
$P(x) = 2 \Rightarrow 2x^2 - x - 2 = 0$. Discriminant $= 1 + 16 = 17$, not a perfect square. $N(2) = 0$. ✓

So with 2 queries ($c = 0, 1$), Bob gets $(1, 1)$, same as surjective. He can't distinguish. With 3 queries ($c = 0, 1, 2$), he gets $(1, 1, 0)$, and the 0 reveals non-surjectivity.

But wait - the lower bound argument needs to be more careful. Bob doesn't have to query $0, 1, 2$. He could query any constants. The question is: what's the minimum number of queries such that for ANY strategy Bob uses with that many queries, he can always determine the answer?

Actually, the problem asks for the minimum cost such that Bob can GUARANTEE reaching his goal. So we need: what's the minimum $m$ such that there EXISTS a strategy for Bob using $m$ queries that always works?

So the upper bound is: there exists a strategy with $m$ queries.
The lower bound is: no strategy with $m - 1$ queries works.

For the upper bound, I've shown that querying $c = 0, 1, \ldots, n$ works if the following is true:

**Claim**: If $P$ is an integer polynomial of degree $\leq n$ with $N(0) = N(1) = \cdots = N(n) = 1$, then $P(x) = x + b$ or $P(x) = -x + b$ for some integer $b$.

For the lower bound, I need to show that with $n$ queries, Alice can fool Bob. That is, for any set of $n$ query values $c_1, \ldots, c_n$, there exist two polynomials $P_1, P_2$ of degree $\leq n$, one surjective and one not, that give the same answers to all $n$ queries.

Hmm, let me think about the lower bound more carefully.

For $n = 1$: 1 query is not enough. Bob queries some $c$. If the answer is 1, it could be $P(x) = x + b$ (surjective) or $P(x) = 2x + b'$ with $2 | (c - b')$ (non-surjective). So Bob can't tell.

For general $n$: With $n$ queries $c_1, \ldots, c_n$, if all answers are 1, Bob can't distinguish surjective from non-surjective. We need to show there's a non-surjective degree $\leq n$ polynomial with $N(c_i) = 1$ for all $i = 1, \ldots, n$.

This is equivalent to: there exist distinct integers $t_1, \ldots, t_n$ with $P(t_i) = c_i$, and $P$ has degree $\leq n$ with integer coefficients, $P$ is not surjective, and $N(c_i) = 1$ for each $i$.

Actually, the lower bound is more subtle. Bob can choose his queries adaptively. So we need to show that for any adaptive strategy using $n$ queries, Alice can respond in a way that leaves Bob uncertain.

Hmm, but actually, the problem is about worst-case guarantee. Bob wants a strategy that works for ALL polynomials. So the lower bound is: for any strategy using $n-1$ queries (even adaptive), there exists a polynomial that fools the strategy.

Let me think about this differently. Consider the information Bob gets. Each query gives him a non-negative integer (the count). If the count is not 1, he immediately knows $P$ is not surjective. The hard case is when all counts are 1.

If all $n$ queries return 1, Bob knows that $n$ specific values each have exactly one preimage. He needs to determine if $P$ is surjective.

The surjective polynomials are $P(x) = x + b$ and $P(x) = -x + b$. For these, every value has exactly one preimage.

A non-surjective polynomial that gives count 1 for $n$ specific values: we need to show such a polynomial exists for any set of $n$ values.

Let me think about this. Given $n$ query values $c_1, \ldots, c_n$ (which Bob might choose adaptively, but let's first consider non-adaptive), we want a non-surjective degree $\leq n$ polynomial $P$ with $N(c_i) = 1$ for all $i$.

Consider $P(x) = x + M \prod_{i=1}^{n} (x - t_i)$ where $t_i$ are chosen so that $P(t_i) = c_i$, i.e., $t_i + 0 = c_i$ (since the product is 0 at $t_i$). So $t_i = c_i$. Then $P(x) = x + M \prod_{i=1}^n (x - c_i)$.

This has degree $n$ (if $M \neq 0$) and $P(c_i) = c_i$ for each $i$. So $N(c_i) \geq 1$.

But we need $N(c_i) = 1$, meaning $c_i$ is the only integer preimage of $c_i$ under $P$.

$P(x) = c_i \Rightarrow x + M \prod_{j=1}^n (x - c_j) = c_i \Rightarrow (x - c_i) + M \prod_{j=1}^n (x - c_j) = 0 \Rightarrow (x - c_i)\left(1 + M \prod_{j \neq i} (x - c_j)\right) = 0$.

So $x = c_i$ or $1 + M \prod_{j \neq i} (x - c_j) = 0$.

The second equation: $M \prod_{j \neq i} (x - c_j) = -1$. Since $M$ is an integer and $\prod_{j \neq i} (x - c_j)$ is an integer for integer $x$, we need $M \cdot (\text{integer}) = -1$, so $M = \pm 1$ and $\prod_{j \neq i} (x - c_j) = \mp 1$.

If $|M| \geq 2$: $M \prod_{j \neq i}(x - c_j) = -1$ has no integer solution (since $|M \cdot \text{integer}| \geq 2$ if the integer is nonzero, and $= 0$ if it's zero). So $N(c_i) = 1$ for all $i$.

And $P(x) = x + M \prod_{j=1}^n (x - c_j)$ with $|M| \geq 2$ has degree $n \geq 2$ (for $n \geq 2$), so it's not surjective.

Wait, but for $n = 1$: $P(x) = x + M(x - c_1) = (1+M)x - Mc_1$. This is degree 1. For $|M| \geq 2$, $|1+M| \geq 3$, so not surjective. And $N(c_1) = 1$ (since $P(c_1) = c_1$ and $P$ is injective as a degree 1 polynomial with nonzero leading coefficient). 

But wait, for degree 1, $P(x) = (1+M)x - Mc_1$. $N(c_1) = 1$ always (since $P$ is linear with nonzero slope, every value in the image has exactly one preimage). But $P$ is not surjective when $|1+M| \geq 2$, i.e., $M \neq 0, -2$. So for $M = 1$: $P(x) = 2x - c_1$, not surjective, $N(c_1) = 1$. Bob queries $c_1$, gets 1, can't distinguish from $P(x) = x + b$ (surjective, also gives 1).

So for $n = 1$: 1 query gives 1, which is consistent with both surjective and non-surjective. Lower bound: 1 query not enough. ✓

For general $n$: Bob makes $n$ queries $c_1, \ldots, c_n$ (possibly adaptive). Alice responds 1 to each. Bob can't distinguish $P(x) = x + b$ (surjective) from $P(x) = x + M \prod (x - c_i)$ with $|M| \geq 2$ (non-surjective, degree $n$, $N(c_i) = 1$ for all $i$).

Wait, but Bob's queries might be adaptive. Let me think about this. If Bob queries adaptively, his second query depends on the first answer. But if Alice always responds 1, Bob's queries are determined (since the response is always 1, the adaptive strategy reduces to a fixed sequence). So the above argument works: after $n$ queries all returning 1, Bob can't distinguish.

But actually, the adaptive case is trickier. Bob might choose $c_2$ based on the answer to $c_1$. If the answer to $c_1$ is not 1, Bob might stop early (he knows it's non-surjective). But for the lower bound, we need to show that Alice can force Bob to need $n+1$ queries. Alice's strategy: always respond 1 (as long as possible). This forces Bob to continue querying. After $n$ queries all returning 1, Bob still can't distinguish, as shown.

But wait, can Alice always respond 1? She needs to have actually chosen a polynomial $P$ beforehand. The game is: Alice first chooses $P$, then Bob makes queries. So Alice can't adaptively choose $P$ based on Bob's queries.

Hmm, this is important. Alice chooses $P$ first, then Bob queries. So for the lower bound, we need: for any Bob strategy (possibly adaptive), there exists a polynomial $P$ (chosen before Bob's queries) that fools Bob.

Since Bob's strategy might be adaptive, his queries depend on previous answers. But Alice has already fixed $P$. So the answers are determined by $P$.

For the lower bound, we need: for any adaptive Bob strategy using $n$ queries, there exist two polynomials $P_1$ (surjective) and $P_2$ (non-surjective) such that Bob gets the same answers from both, and thus can't distinguish.

Since Bob's strategy is adaptive, his queries depend on answers. If $P_1$ and $P_2$ give the same answers to all queries, then Bob's query sequence is the same for both, and he can't distinguish.

So we need: for any possible sequence of $n$ queries (which could be adaptive, but if the answers are all the same, the sequence is determined), there exist $P_1$ surjective and $P_2$ non-surjective giving the same answers.

If all answers are 1: $P_1(x) = x + b$ (for appropriate $b$) gives $N(c) = 1$ for all $c$. $P_2(x) = x + M \prod_{i=1}^n (x - c_i)$ with $|M| \geq 2$ gives $N(c_i) = 1$ for all $i$. Both give the same answers (all 1s). Bob can't distinguish.

But we need to make sure $P_2$ has degree $\leq n$. $P_2(x) = x + M \prod_{i=1}^n (x - c_i)$ has degree $n$ (for $M \neq 0$). ✓

And $P_2$ is not surjective: for $n \geq 2$, degree $\geq 2$ implies not surjective. For $n = 1$, $P_2(x) = (1+M)x - Mc_1$ with $|1+M| \geq 2$ is not surjective. ✓

But wait, there's a subtlety. For the adaptive case, Bob might not query all $n$ values if he gets a non-1 answer early. But for the lower bound, we're showing that Alice can choose a $P_2$ that gives all 1s for the first $n$ queries, forcing Bob to use at least $n+1$ queries.

But Alice chooses $P$ before Bob queries. She doesn't know what Bob will query. However, for the lower bound, we use an adversarial argument: for any Bob strategy, we show there exists a $P$ that forces $n+1$ queries.

Here's the issue: Bob's queries are adaptive and depend on answers. If Alice chooses $P_2(x) = x + M \prod_{i=1}^n (x - c_i)$, this depends on $c_1, \ldots, c_n$, which are Bob's queries. But Alice doesn't know these in advance!

So the lower bound argument needs to be more careful. Let me reconsider.

For a non-adaptive Bob strategy: Bob chooses $c_1, \ldots, c_m$ upfront. Then Alice can choose $P_2$ based on these. But Bob's strategy could be adaptive.

For an adaptive strategy: Bob chooses $c_1$, gets answer, chooses $c_2$ based on answer, etc. Alice has already chosen $P$.

For the lower bound with adaptive strategies: We need to show that for any adaptive strategy with $n$ queries, there's a $P$ that fools Bob.

Key insight: Consider the "all 1s" path. If Alice chooses a surjective $P$ (say $P(x) = x$), Bob gets all 1s. His query sequence is $c_1, c_2(c_1), c_3(c_1, c_2), \ldots$ (determined by the all-1s responses). Call this sequence $c_1^*, c_2^*, \ldots, c_n^*$.

Now, Alice could instead choose $P_2(x) = x + M \prod_{i=1}^n (x - c_i^*)$ with $|M| \geq 2$. This $P_2$ gives $N(c_i^*) = 1$ for all $i$. So Bob gets the same all-1s responses, follows the same query path, and can't distinguish $P(x) = x$ from $P_2$.

But wait, Alice chooses $P$ before Bob starts querying. She doesn't know Bob's strategy. However, for the lower bound, we're showing that for any fixed Bob strategy, there exists a $P$ that fools it. The $P$ can depend on the strategy (since we're proving existence).

More precisely: Fix any Bob strategy $S$ using $n$ queries. Consider the path where all responses are 1. This determines a query sequence $c_1^*, \ldots, c_n^*$ (since the strategy is deterministic and the responses are all 1). Now:
- $P_1(x) = x$ is surjective and gives all 1s.
- $P_2(x) = x + M \prod_{i=1}^n (x - c_i^*)$ with $|M| \geq 2$ is non-surjective and gives all 1s for queries $c_1^*, \ldots, c_n^*$.

Both give the same responses, so Bob can't distinguish. Thus $n$ queries are not enough.

Wait, but I need to be more careful. When Bob queries $c_1^*$ and gets 1 (from $P_2$), he then queries $c_2^*$ (same as in the all-1s path for $P_1$). He gets 1 from $P_2$ as well. And so on. So the query sequence is the same, and all responses are 1 for both $P_1$ and $P_2$. Bob can't distinguish. ✓

But there's another subtlety: Bob might stop early if he gets a non-1 answer. In the all-1s path, he doesn't stop early (since all answers are 1). After $n$ queries, he still can't distinguish. So he needs at least $n+1$ queries.

Actually, I need to also verify that $P_2$ gives $N(c_i^*) = 1$ and not some other value. Let me re-examine.

$P_2(x) = x + M \prod_{j=1}^n (x - c_j^*)$. $P_2(c_i^*) = c_i^* + 0 = c_i^*$. So $c_i^*$ is a preimage of $c_i^*$.

$P_2(x) = c_i^* \Rightarrow x + M \prod_{j=1}^n (x - c_j^*) = c_i^* \Rightarrow (x - c_i^*) + M \prod_{j=1}^n (x - c_j^*) = 0 \Rightarrow (x - c_i^*)\left(1 + M \prod_{j \neq i} (x - c_j^*)\right) = 0$.

So $x = c_i^*$ or $1 + M \prod_{j \neq i} (x - c_j^*) = 0$.

The latter: $M \prod_{j \neq i} (x - c_j^*) = -1$. For integer $x$, $\prod_{j \neq i} (x - c_j^*)$ is an integer. So $M \cdot \text{integer} = -1$, requiring $|M| = 1$ and the product $= \mp 1$. Since $|M| \geq 2$, no integer solution. So $N(c_i^*) = 1$. ✓

Great, so the lower bound is $n + 1$.

Now for the upper bound. I need to show that $n + 1$ queries suffice. The strategy: query $c = 0, 1, \ldots, n$.

If any $N(i) \neq 1$: $P$ is not surjective (since surjective $\Rightarrow$ $N(c) = 1$ for all $c$). Answer "yes".

If all $N(0) = N(1) = \cdots = N(n) = 1$: Need to show $P$ is surjective.

There exist distinct integers $t_0, \ldots, t_n$ with $P(t_i) = i$. $P$ is the unique degree $\leq n$ polynomial through $(t_0, 0), \ldots, (t_n, n)$.

Consider $Q(x) = P(x) - x$. Then $Q(t_i) = i - t_i$ for each $i$. $Q$ has degree $\leq n$.

If $t_i = i + b$ for some constant $b$ (i.e., $t_i = i - c$ for some constant, meaning the $t_i$ are in arithmetic progression with common difference 1), then $Q(t_i) = i - (i + b) = -b$ for all $i$. So $Q$ is constant $-b$, meaning $P(x) = x - b$, surjective.

Similarly, if $t_i = -i + b$, then $Q(t_i) = i - (-i + b) = 2i - b$. $Q$ is linear: $Q(x) = -2x + (b - 2t_0)$... hmm, let me think again. If $t_i = b - i$, then $P(b-i) = i$, so $P(x) = b - x = -x + b$, surjective.

But what if the $t_i$ are not in such a nice pattern? We need to show that if $P$ has degree $\leq n$, integer coefficients, $N(i) = 1$ for $i = 0, \ldots, n$, then $P$ must be $\pm x + b$.

Hmm, but I proved this for $n = 2$ above. Let me think about the general case.

Actually, let me reconsider. The upper bound strategy of querying $0, 1, \ldots, n$ works if and only if: any degree $\leq n$ integer polynomial with $N(0) = \cdots = N(n) = 1$ is surjective.

Is this true for general $n$? Let me think about $n = 3$.

Can we find a degree 3 integer polynomial with $N(0) = N(1) = N(2) = N(3) = 1$ that is not surjective?

Using the same approach: $P(x) = x + M \prod_{i=0}^{3} (x - i)$ would have degree 4, too high. We need degree $\leq 3$.

Let me try $P(x) = x + M(x - 0)(x - 1)(x - 2) = x + Mx(x-1)(x-2)$. This has degree 3. $P(0) = 0, P(1) = 1, P(2) = 2$. $N(0) = ?$: $P(x) = 0 \Rightarrow x(1 + M(x-1)(x-2)) = 0 \Rightarrow x = 0$ or $M(x-1)(x-2) = -1$. For $|M| \geq 2$, no integer solution to the latter. So $N(0) = 1$. Similarly $N(1) = 1, N(2) = 1$.

$N(3) = ?$: $P(3) = 3 + M \cdot 3 \cdot 2 \cdot 1 = 3 + 6M$. For $N(3) = 1$, we need $P(x) = 3$ to have exactly one integer solution. $P(x) = 3 \Rightarrow x + Mx(x-1)(x-2) = 3$. If $M = 1$: $x + x(x-1)(x-2) = 3 \Rightarrow x(1 + (x-1)(x-2)) = 3 \Rightarrow x(x^2 - 3x + 3) = 3 \Rightarrow x^3 - 3x^2 + 3x - 3 = 0 \Rightarrow (x-1)^3 - 2 = 0$. No integer roots. So $N(3) = 0$. Bob queries 3 and gets 0, detects non-surjective.

If $M = -1$: $P(x) = x - x(x-1)(x-2) = x(1 - (x-1)(x-2)) = x(-x^2+3x-1) = -x^3 + 3x^2 - x$. $P(3) = -27 + 27 - 3 = -3$. $N(3) = ?$: $-x^3 + 3x^2 - x = 3 \Rightarrow x^3 - 3x^2 + x + 3 = 0$. Try $x = -1$: $-1 - 3 - 1 + 3 = -2 \neq 0$. $x = 3$: $27 - 27 + 3 + 3 = 6 \neq 0$. $x = 1$: $1 - 3 + 1 + 3 = 2 \neq 0$. No easy integer root. So $N(3) = 0$ probably.

So for this construction, $N(3) = 0$, and Bob detects it with the 4th query. Good.

But can we find a degree 3 polynomial with $N(0) = N(1) = N(2) = N(3) = 1$ that's not surjective?

We need $P(t_i) = i$ for $i = 0, 1, 2, 3$ with distinct integers $t_0, t_1, t_2, t_3$, $P$ has degree $\leq 3$ with integer coefficients, and $N(i) = 1$ for each $i$.

$P$ is determined by 4 points. Let me try to find integer-coefficient degree 3 polynomials through 4 points $(t_0, 0), (t_1, 1), (t_2, 2), (t_3, 3)$ where $t_i$ are distinct integers.

The polynomial $P(x) - x$ vanishes at $t_i$ iff $P(t_i) = t_i$, which is not what we want. Let me think differently.

$Q(x) = P(x) - x$ has $Q(t_i) = i - t_i$. If $t_i = i + b$ for all $i$, then $Q(t_i) = -b$ for all $i$, so $Q$ is constant, $P(x) = x - b$, surjective.

If the $t_i$ are not of this form, $Q$ is non-constant with degree $\leq 3$, and $Q(t_i) = i - t_i$.

For $P$ to have integer coefficients, $Q$ must have integer coefficients (since $P = Q + x$ and $x$ has integer coefficients).

So we need: a degree $\leq 3$ integer polynomial $Q$ with $Q(t_i) = i - t_i$ for 4 distinct integers $t_0, t_1, t_2, t_3$, and $P = Q + x$ has $N(i) = 1$ for $i = 0, 1, 2, 3$.

$N(i) = 1$ means $P(x) = i$ has exactly one integer solution, i.e., $Q(x) + x = i$, i.e., $Q(x) = i - x$ has exactly one integer solution.

Hmm, this is getting complicated. Let me try a different approach to the upper bound.

Alternative approach: Instead of querying $0, 1, \ldots, n$, maybe Bob should use a different strategy.

Actually, let me reconsider. Maybe the answer isn't $n+1$. Let me think about what Bob's goal is more carefully.

Bob wants to determine whether there exists an integer $k$ such that $P(x) = k$ has no integer roots. This is equivalent to: is $P(\mathbb{Z}) \neq \mathbb{Z}$?

Bob's strategy: query values and use the counts to determine the answer.

Key observation: If Bob ever gets a count $\neq 1$, he knows $P$ is not surjective (answer "yes"). If he always gets 1, he needs to determine if $P$ is surjective.

The question is: how many "all 1s" responses does Bob need before he can conclude $P$ is surjective?

If $P$ is surjective ($P(x) = \pm x + b$), every query gives 1.
If $P$ is not surjective, Bob needs to find a query that gives $\neq 1$.

So the question becomes: for a non-surjective degree $\leq n$ polynomial, how many queries does Bob need to find a value $c$ with $N(c) \neq 1$?

Equivalently: what's the maximum number of values $c$ for which a non-surjective degree $\leq n$ polynomial can have $N(c) = 1$?

If a non-surjective polynomial can have $N(c) = 1$ for at most $n$ values, then $n + 1$ queries suffice (by the pigeonhole principle, one of the $n+1$ queries must give $\neq 1$).

But if a non-surjective polynomial can have $N(c) = 1$ for more than $n$ values, then $n + 1$ queries might not suffice.

From the lower bound construction: $P(x) = x + M \prod_{i=1}^n (x - c_i)$ with $|M| \geq 2$ has $N(c_i) = 1$ for $n$ specific values. Can it have $N(c) = 1$ for more values?

$P(x) = c \Rightarrow x + M \prod_{i=1}^n (x - c_i) = c \Rightarrow (x - c) + M \prod_{i=1}^n (x - c_i) = 0$.

If $c \notin \{c_1, \ldots, c_n\}$: $(x - c) + M \prod_{i=1}^n (x - c_i) = 0$. This is a degree $n$ equation. For $N(c) = 1$, we need exactly one integer root.

For $c = c_i$: as shown, $N(c_i) = 1$ (for $|M| \geq 2$).

For other $c$: it depends. The polynomial $(x - c) + M \prod_{i=1}^n (x - c_i)$ has degree $n$. It could have 0, 1, or more integer roots.

So a non-surjective polynomial could potentially have $N(c) = 1$ for many values of $c$, not just $n$.

Hmm, so the upper bound of $n + 1$ might not work with the strategy of querying $0, 1, \ldots, n$.

Wait, but I showed for $n = 2$ that no degree 2 integer polynomial (other than surjective ones) has $N(0) = N(1) = N(2) = 1$. So for $n = 2$, the strategy works. Let me check if this generalizes.

The key claim is: **If $P$ is a degree $\leq n$ integer polynomial with $N(0) = N(1) = \cdots = N(n) = 1$, then $P$ is surjective.**

For $n = 1$: $N(0) = N(1) = 1$ implies $|a| = 1$ (shown above). ✓
For $n = 2$: $N(0) = N(1) = N(2) = 1$ implies $P$ is linear surjective (shown above). ✓

For general $n$: Let me think about this.

If $N(i) = 1$ for $i = 0, 1, \ldots, n$, there exist distinct integers $t_0, \ldots, t_n$ with $P(t_i) = i$. $P$ is the unique degree $\leq n$ polynomial through these $n + 1$ points.

Consider $R(x) = P(x) - x$. Then $R(t_i) = i - t_i$ for each $i$. $R$ has degree $\leq n$.

If $R$ is identically 0, then $P(x) = x$, surjective.
If $R$ is a nonzero constant $c$, then $P(x) = x + c$, surjective.

If $R$ has degree $\geq 1$: $R$ is a degree $\leq n$ polynomial with $R(t_i) = i - t_i$ for $n + 1$ points. 

Now, $P(x) = i$ has exactly one integer solution (namely $t_i$). $P(x) = i \Leftrightarrow R(x) = i - x \Leftrightarrow R(x) + x = i \Leftrightarrow P(x) = i$. So the condition is that $P(x) = i$ has exactly one integer root.

Let me think about the polynomial $S(x) = P(x) - x = R(x)$. We have $S(t_i) = i - t_i$.

Now, consider the polynomial $P(x) - j$ for $j \in \{0, 1, \ldots, n\}$. This has exactly one integer root $t_j$.

$P(x) - j = (x - t_j) \cdot T_j(x)$ where $T_j(x)$ is a polynomial of degree $\leq n - 1$ with no integer roots.

Since $P$ has integer coefficients and $t_j$ is an integer, $T_j(x) = \frac{P(x) - j}{x - t_j}$ has integer coefficients (by the factor theorem, since $P(t_j) = j$ and $P$ has integer coefficients, the quotient has integer coefficients... actually, this is true: if $P$ has integer coefficients and $P(a) = 0$ for integer $a$, then $(x - a) | P(x)$ in $\mathbb{Z}[x]$).

Wait, $P(x) - j$ has integer coefficients and $P(t_j) - j = 0$, so $(x - t_j) | (P(x) - j)$ in $\mathbb{Z}[x]$. So $T_j(x) \in \mathbb{Z}[x]$ with degree $n - 1$ (if $P$ has degree $n$) and no integer roots.

Hmm, this is a strong condition. $T_j$ has no integer roots for each $j = 0, \ldots, n$.

Let me think about what this implies. $P(x) - j = (x - t_j) T_j(x)$ where $T_j \in \mathbb{Z}[x]$, $\deg T_j = n - 1$ (assuming $\deg P = n$), and $T_j$ has no integer roots.

For $j \neq k$: $P(x) - j = (x - t_j) T_j(x)$ and $P(x) - k = (x - t_k) T_k(x)$. Subtracting: $(k - j) = (x - t_j) T_j(x) - (x - t_k) T_k(x)$.

At $x = t_j$: $(k - j) = 0 - (t_j - t_k) T_k(t_j)$, so $T_k(t_j) = \frac{j - k}{t_j - t_k} = \frac{k - j}{t_k - t_j}$.

Since $T_k$ has integer coefficients and $t_j$ is an integer, $T_k(t_j)$ is an integer. So $(t_k - t_j) | (k - j)$.

This must hold for all $j \neq k$ in $\{0, 1, \ldots, n\}$!

So $(t_k - t_j) | (k - j)$ for all $j \neq k$.

This is a very strong divisibility condition. Let me explore it.

Let $d_j = t_j - j$ (the "shift" at position $j$). Then $t_k - t_j = (d_k + k) - (d_j + j) = (d_k - d_j) + (k - j)$.

The condition $(t_k - t_j) | (k - j)$ becomes $((d_k - d_j) + (k - j)) | (k - j)$.

Let $m = k - j$ (nonzero). Then $(d_k - d_j + m) | m$, which means $d_k - d_j + m | m$, i.e., $d_k - d_j | m$ is not quite right. Let me redo.

$(d_k - d_j + m) | m$ means there exists an integer $q$ such that $m = q(d_k - d_j + m)$, so $m(1 - q) = q(d_k - d_j)$, so $m = \frac{q(d_k - d_j)}{1 - q}$ (for $q \neq 1$). Alternatively, $d_k - d_j + m | m$ means $d_k - d_j + m | m - (d_k - d_j + m) = -d_k + d_j$, i.e., $(d_k - d_j + m) | (d_j - d_k)$.

So $(t_k - t_j) | (j - k)$, equivalently $(t_k - t_j) | (k - j)$ (same thing since divisibility ignores sign).

So $|t_k - t_j| \leq |k - j|$ (unless $t_k = t_j$, but they're distinct) OR $t_k - t_j = \pm 1$ and $|k - j| \geq 1$... no, the condition is $(t_k - t_j) | (k - j)$, so $|t_k - t_j| \leq |k - j|$ (when $t_k \neq t_j$).

Wait, that's not quite right. $(t_k - t_j) | (k - j)$ means $|t_k - t_j| \leq |k - j|$ when $k \neq j$ and $t_k \neq t_j$. But also $t_k - t_j$ could be $\pm 1$ and $k - j$ could be anything.

Actually, $(t_k - t_j) | (k-j)$ and $k \neq j$ means $|t_k - t_j| \leq |k - j|$.

So for all $j \neq k$ in $\{0, \ldots, n\}$: $|t_k - t_j| \leq |k - j|$.

This means the map $j \mapsto t_j$ is a function from $\{0, \ldots, n\}$ to $\mathbb{Z}$ that is "1-Lipschitz": $|t_k - t_j| \leq |k - j|$.

Since $j \mapsto t_j$ is 1-Lipschitz and the $t_j$ are distinct, we have $|t_k - t_j| \leq |k - j|$ with equality possible.

If $|t_k - t_j| = |k - j|$ for all $j, k$, then $t_j = \pm j + c$ for some constant $c$, which gives $P(x) = x + c$ or $P(x) = -x + c$, surjective.

If $|t_k - t_j| < |k - j|$ for some $j, k$: Since $|t_k - t_j| \leq |k - j|$ and the $t_j$ are distinct integers, we need $|t_k - t_j| \geq 1$ for $k \neq j$. So $1 \leq |t_k - t_j| \leq |k - j|$.

But can we have $|t_k - t_j| < |k - j|$ for some pair while maintaining the Lipschitz condition for all pairs?

Consider $n = 2$: $t_0, t_1, t_2$ distinct integers with $|t_1 - t_0| \leq 1, |t_2 - t_1| \leq 1, |t_2 - t_0| \leq 2$.

$|t_1 - t_0| \leq 1$ and $t_1 \neq t_0$ means $|t_1 - t_0| = 1$.
$|t_2 - t_1| \leq 1$ and $t_2 \neq t_1$ means $|t_2 - t_1| = 1$.
$|t_2 - t_0| \leq 2$ and $t_2 \neq t_0$ means $|t_2 - t_0| \in \{1, 2\}$.

Since $|t_2 - t_0| = |t_2 - t_1 + t_1 - t_0| \leq |t_2 - t_1| + |t_1 - t_0| = 2$, and $|t_2 - t_0| \geq 1$.

If $|t_2 - t_0| = 2$: then $t_0, t_1, t_2$ are in AP with common difference $\pm 1$, so $t_j = \pm j + c$, surjective.

If $|t_2 - t_0| = 1$: $t_0, t_1, t_2$ are three distinct integers with consecutive differences of absolute value 1, and $|t_2 - t_0| = 1$. But $|t_2 - t_0| = |t_2 - t_1| + |t_1 - t_0|$ only if $t_1$ is between $t_0$ and $t_2$. If $|t_2 - t_0| = 1$ and $|t_1 - t_0| = 1$ and $|t_2 - t_1| = 1$, then $t_0, t_2$ differ by 1, and $t_1$ differs from both by 1. So $t_1$ is at distance 1 from both $t_0$ and $t_2$, but $t_0$ and $t_2$ are at distance 1. This means $t_1 = t_0 \pm 1$ and $t_1 = t_2 \pm 1 = (t_0 \pm 1) \pm 1$. If $t_2 = t_0 + 1$: $t_1 = t_0 + 1 = t_2$ (contradiction) or $t_1 = t_0 - 1$. Then $t_1 = t_0 - 1, t_2 = t_0 + 1$. Check: $|t_1 - t_0| = 1, |t_2 - t_1| = 2$. But we need $|t_2 - t_1| \leq 1$. Contradiction!

If $t_2 = t_0 - 1$: similarly, $t_1 = t_0 + 1$ (then $|t_2 - t_1| = 2 > 1$) or $t_1 = t_0 - 1 = t_2$ (contradiction). So no valid configuration.

So for $n = 2$, the only possibility is $|t_2 - t_0| = 2$, giving $t_j = \pm j + c$, surjective. ✓

For general $n$: The 1-Lipschitz condition $|t_k - t_j| \leq |k - j|$ with all $t_j$ distinct.

Since $|t_k - t_j| \leq |k - j|$ and $t_j$ are distinct, the sequence $t_0, t_1, \ldots, t_n$ has consecutive differences $|t_{j+1} - t_j| \leq 1$ and $\geq 1$ (distinct), so $|t_{j+1} - t_j| = 1$ for all $j$.

So $t_{j+1} = t_j \pm 1$ for each $j$. The sequence is a walk on $\mathbb{Z}$ with steps $\pm 1$.

Now, $|t_k - t_j| \leq |k - j|$ for all $j, k$. Since $|t_k - t_j| \leq \sum_{i=j}^{k-1} |t_{i+1} - t_i| = k - j$ (for $k > j$), this is automatically satisfied with equality when all steps are in the same direction.

But if the walk changes direction (some steps $+1
