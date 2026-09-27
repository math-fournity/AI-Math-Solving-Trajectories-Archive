# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Find the number of integer triangles $ABC$ (with side lengths $a, b, c$) such that the length of the angle bisector from vertex $A$ is equal to the side length $b$ (where $b = AC$), and the perimeter $a+b+c$ is of the form $10p$ for some prime number $p$.       — 题目文本
#   The condition that the angle bisector $l_a = b$ leads to the relation $a^2c = (c-b)(c+b)^2$. By setting $s=t^2$ and $s-r=k^2$ for coprime $t, k$, we find parameterized sides $a = xk(2t^2 - k^2)$, $b = xt(t^2 - k^2)$, and $c = xt^3$. The perimeter condition $a+b+c = x(k+t)(2t^2-k^2) = 10p$.
The case analysis for $x, k, t$ in the original solution yields three sets of side lengths: $(28, 15, 27)$ where $p=7$, $(267, 280, 343)$ where $p=89$, and $(62, 120, 128)$ where $p=31$. These are the only valid integer triangles satisfying the conditions.  — 标准解答
#   Let me solve this problem. The problem asks for integer triangles ABC with side lengths a, b, c where the angle bisector from vertex A equals side length b (where b = AC), and the perimeter a+b+c is of the form 10p for some prime p.

Let me set up the problem. In triangle ABC, sides are a = BC, b = CA, c = AB. The angle bisector from vertex A divides the opposite side BC into segments proportional to the adjacent sides.

The angle bisector from A has length given by the formula:
$$l_a = \frac{2bc \cos(A/2)}{b+c}$$
or equivalently:
$$l_a^2 = bc\left(1 - \frac{a^2}{(b+c)^2}\right) = \frac{bc((b+c)^2 - a^2)}{(b+c)^2}$$

We want $l_a = b$.

So $l_a^2 = b^2$:
$$\frac{bc((b+c)^2 - a^2)}{(b+c)^2} = b^2$$

$$\frac{c((b+c)^2 - a^2)}{(b+c)^2} = b$$

$$c((b+c)^2 - a^2) = b(b+c)^2$$

$$c(b+c)^2 - ca^2 = b(b+c)^2$$

$$(c-b)(b+c)^2 = ca^2$$

So we need $(c-b)(b+c)^2 = ca^2$.

Let me think about this. We need c > b (since the left side must be positive, as a, b, c > 0 and (b+c)^2 > 0, we need c - b > 0, so c > b).

Let me set $d = c - b > 0$ and $s = b + c$. Then $c = \frac{s+d}{2}$, $b = \frac{s-d}{2}$.

The equation becomes:
$$d \cdot s^2 = \frac{s+d}{2} \cdot a^2$$

$$2ds^2 = (s+d)a^2$$

$$a^2 = \frac{2ds^2}{s+d}$$

For a to be an integer, we need $\frac{2ds^2}{s+d}$ to be a perfect square of a positive integer, and also a must satisfy triangle inequality.

Also, b and c must be positive integers, so s and d must have the same parity (both even or both odd), and s > d > 0.

Triangle inequality: a + b > c, a + c > b, b + c > a.
- b + c > a: s > a, i.e., $s^2 > a^2 = \frac{2ds^2}{s+d}$, so $1 > \frac{2d}{s+d}$, i.e., $s+d > 2d$, i.e., $s > d$. ✓ (already required)
- a + b > c: $a + \frac{s-d}{2} > \frac{s+d}{2}$, so $a > d$.
- a + c > b: $a + \frac{s+d}{2} > \frac{s-d}{2}$, so $a > -d$, always true since a, d > 0.

So we need $a > d = c - b$.

Let me think about this differently. Let me try small values.

Actually, let me think about it more carefully. We have:
$$a^2 = \frac{2ds^2}{s+d}$$

where $d = c - b$, $s = b + c$, $s > d > 0$, $s \equiv d \pmod{2}$, and $a > d$.

The perimeter is $a + b + c = a + s$, and we need $a + s = 10p$ for some prime $p$.

Let me try to find solutions systematically.

Let me set $d$ and $s$ and check.

For $d = 1$: $a^2 = \frac{2s^2}{s+1}$. We need $s+1 | 2s^2$. Since $\gcd(s, s+1) = 1$, we need $s+1 | 2$. So $s+1 \in \{1, 2\}$, meaning $s \in \{0, 1\}$. But $s > d = 1$, so $s \geq 2$. No solution.

Wait, let me redo. $s+1 | 2s^2$. $\gcd(s+1, s) = 1$ so $\gcd(s+1, s^2) = 1$, thus $s+1 | 2$. So $s+1 \in \{1, 2\}$, $s \in \{0, 1\}$. No valid $s$.

For $d = 2$: $a^2 = \frac{4s^2}{s+2}$. Need $s+2 | 4s^2$. $\gcd(s+2, s) = \gcd(2, s)$. 

If $s$ is even, $\gcd(s+2, s) = 2$. Let $s = 2m$. Then $s+2 = 2(m+1)$, $4s^2 = 16m^2$. Need $2(m+1) | 16m^2$, i.e., $(m+1) | 8m^2$. $\gcd(m+1, m) = 1$, so $(m+1) | 8$. $m+1 \in \{1,2,4,8\}$, $m \in \{0,1,3,7\}$, $s \in \{0,2,6,14\}$. Need $s > d = 2$, so $s \in \{6, 14\}$.

- $s = 6, d = 2$: $a^2 = \frac{4 \cdot 36}{8} = 18$. Not a perfect square.
- $s = 14, d = 2$: $a^2 = \frac{4 \cdot 196}{16} = 49$. $a = 7$. Check $a > d$: $7 > 2$ ✓. $b = \frac{14-2}{2} = 6$, $c = \frac{14+2}{2} = 8$. Triangle: $(7, 6, 8)$. Perimeter = $7 + 14 = 21$. $21 = 10p$? $p = 2.1$. Not integer. No.

If $s$ is odd, $\gcd(s+2, s) = 1$. Need $s+2 | 4s^2$, so $s+2 | 4$. $s+2 \in \{1,2,4\}$, $s \in \{-1, 0, 2\}$. Need $s > 2$ and $s$ odd. No.

For $d = 3$: $a^2 = \frac{6s^2}{s+3}$. Need $s+3 | 6s^2$. $\gcd(s+3, s) = \gcd(3, s)$.

If $3 | s$: $s = 3m$, $\gcd(s+3, s) = 3$. $s+3 = 3(m+1)$, $6s^2 = 54m^2$. Need $3(m+1) | 54m^2$, i.e., $(m+1) | 18m^2$. $\gcd(m+1, m) = 1$, so $(m+1) | 18$. $m+1 \in \{1,2,3,6,9,18\}$, $m \in \{0,1,2,5,8,17\}$, $s \in \{0,3,6,15,24,51\}$. Need $s > 3$ and $s \equiv d \pmod{2}$, i.e., $s$ odd. $s \in \{15, 51\}$ (since 6, 24 are even).

- $s = 15, d = 3$: $a^2 = \frac{6 \cdot 225}{18} = 75$. Not a perfect square.
- $s = 51, d = 3$: $a^2 = \frac{6 \cdot 2601}{54} = 289 = 17^2$. $a = 17$. Check $a > d$: $17 > 3$ ✓. $b = \frac{51-3}{2} = 24$, $c = \frac{51+3}{2} = 27$. Triangle: $(17, 24, 27)$. Perimeter = $17 + 51 = 68$. $68 = 10p$? $p = 6.8$. No.

If $3 \nmid s$: $\gcd(s+3, s) = 1$. Need $s+3 | 6$. $s+3 \in \{1,2,3,6\}$, $s \in \{-2,-1,0,3\}$. Need $s > 3$. No.

For $d = 4$: $a^2 = \frac{8s^2}{s+4}$. Need $s+4 | 8s^2$. $\gcd(s+4, s) = \gcd(4, s)$.

Let me think about this more systematically. Let $g = \gcd(s, d)$. Write $s = gS$, $d = gD$ with $\gcd(S, D) = 1$.

Then $a^2 = \frac{2gD \cdot g^2 S^2}{gS + gD} = \frac{2g^2 D S^2}{S + D}$.

So $a^2 = \frac{2g^2 D S^2}{S+D}$ where $\gcd(S, D) = 1$.

For this to be a perfect square, we need $(S+D) | 2g^2 D S^2$. Since $\gcd(S+D, S) | \gcd(S+D, S) = \gcd(D, S) = 1$... wait, $\gcd(S+D, S) = \gcd(D, S) = 1$. So $\gcd(S+D, S^2) = 1$.

Also $\gcd(S+D, D) = \gcd(S, D) = 1$. So $\gcd(S+D, DS^2) = 1$.

Therefore $(S+D) | 2g^2$.

Let $S + D = t$ where $t | 2g^2$.

Then $a^2 = \frac{2g^2 D S^2}{t}$. Since $t | 2g^2$, let $2g^2 = t \cdot k$, so $a^2 = k D S^2$, so $a = S\sqrt{kD}$.

For $a$ to be a positive integer, we need $kD$ to be a perfect square.

Also, $S = t - D$, and we need $S > 0$, $D > 0$, $\gcd(S, D) = 1$, i.e., $\gcd(t-D, D) = 1$, i.e., $\gcd(t, D) = 1$.

And $s > d$ means $gS > gD$, i.e., $S > D$, i.e., $t - D > D$, i.e., $t > 2D$.

And $s \equiv d \pmod{2}$: $gS \equiv gD \pmod{2}$, i.e., $g(S-D) \equiv 0 \pmod{2}$, i.e., $g(S-D)$ even. $S - D = t - 2D$. So $g(t - 2D)$ even.

And $a > d$: $S\sqrt{kD} > gD$, i.e., $(t-D)\sqrt{kD} > gD$.

And perimeter $= a + s = S\sqrt{kD} + gS = S(\sqrt{kD} + g)$. We need this to be $10p$ for prime $p$.

Also, $k = \frac{2g^2}{t}$, so $kD = \frac{2g^2 D}{t}$.

$a = S\sqrt{\frac{2g^2 D}{t}} = \frac{gS\sqrt{2D}}{\sqrt{t}} = \frac{gs\sqrt{2D}}{... }$... hmm, let me just keep $a = S\sqrt{kD}$ where $k = 2g^2/t$.

So $a = S \sqrt{\frac{2g^2 D}{t}}$.

For $a$ to be integer, $\frac{2g^2 D}{t}$ must be a perfect square.

Let me denote $q = \frac{2g^2 D}{t}$. We need $q$ to be a perfect square, and $a = S\sqrt{q}$, so $a = S \cdot m$ where $m = \sqrt{q}$.

Perimeter $= a + s = Sm + gS = S(m + g)$.

We need $S(m + g) = 10p$ for prime $p$.

So $S(m+g) \in \{10 \cdot 2, 10 \cdot 3, 10 \cdot 5, 10 \cdot 7, ...\} = \{20, 30, 50, 70, 110, 130, ...\}$.

Since $S(m+g) = 10p$ and $p$ is prime, the factorizations of $10p = 2 \cdot 5 \cdot p$ give us limited options for $S$ and $m+g$.

The divisors of $10p$ are: $1, 2, 5, 10, p, 2p, 5p, 10p$ (assuming $p \neq 2, 5$; need to handle $p=2$ and $p=5$ separately).

For $p = 2$: $10p = 20 = 2^2 \cdot 5$. Divisors: $1, 2, 4, 5, 10, 20$.
For $p = 5$: $10p = 50 = 2 \cdot 5^2$. Divisors: $1, 2, 5, 10, 25, 50$.
For $p \neq 2, 5$: $10p = 2 \cdot 5 \cdot p$. Divisors: $1, 2, 5, 10, p, 2p, 5p, 10p$.

So $S$ and $m+g$ are complementary divisors of $10p$, with $S \geq 1$ and $m + g \geq 2$ (since $g \geq 1$ and $m \geq 1$).

Actually, $m = \sqrt{q} = \sqrt{\frac{2g^2 D}{t}}$. We need $m$ to be a positive integer. And $g \geq 1$.

Let me think about what constraints we have:
- $g \geq 1$, $D \geq 1$, $S = t - D \geq 1$
- $\gcd(S, D) = \gcd(t, D) = 1$
- $t | 2g^2$
- $t > 2D$ (from $S > D$)
- $q = \frac{2g^2 D}{t}$ is a perfect square, $m = \sqrt{q}$
- $g(t - 2D)$ is even (parity condition)
- $Sm > gD$ (triangle inequality $a > d$)
- $S(m + g) = 10p$ for prime $p$

From $S(m+g) = 10p$ and $S = t - D$:
$(t-D)(m+g) = 10p$.

This is getting complex. Let me try a computational approach mentally, or rather, let me try to enumerate.

Since the perimeter is $10p$, and $p$ is prime, the perimeter is at least 20 (for $p=2$). There's no upper bound stated, so we need to find ALL such triangles. This means there should be finitely many.

Wait, is there an upper bound? The problem says "find the number of integer triangles" — this implies a finite number. Let me think about whether the constraints force finiteness.

From $a^2 = \frac{2ds^2}{s+d}$ and $a > d$ and $a < s$ (triangle inequality), we get $d^2 < \frac{2ds^2}{s+d} < s^2$.

From $a > d$: $\frac{2ds^2}{s+d} > d^2$, so $\frac{2s^2}{s+d} > d$, so $2s^2 > d(s+d) = ds + d^2$, so $2s^2 - ds - d^2 > 0$. Using quadratic formula in $s$: $s > \frac{d + \sqrt{d^2 + 8d^2}}{4} = \frac{d + 3d}{4} = d$. So $s > d$, which we already have. Actually, $2s^2 - ds - d^2 = (2s + d)(s - d) > 0$ when $s > d$. So this is always satisfied.

From $a < s$: $\frac{2ds^2}{s+d} < s^2$, so $\frac{2d}{s+d} < 1$, so $2d < s + d$, so $d < s$. Always satisfied.

So the triangle inequality $a > d$ is automatically satisfied when $s > d$? Let me double check. $a > d$ iff $a^2 > d^2$ iff $\frac{2ds^2}{s+d} > d^2$ iff $\frac{2s^2}{s+d} > d$ iff $2s^2 > d(s+d)$ iff $2s^2 - ds - d^2 > 0$ iff $(2s+d)(s-d) > 0$ iff $s > d$ (since $2s+d > 0$). Yes! So $a > d$ is equivalent to $s > d$, which is already required.

So the only constraints are:
1. $s > d > 0$
2. $s \equiv d \pmod{2}$
3. $a^2 = \frac{2ds^2}{s+d}$ is a perfect square
4. $a + s = 10p$ for prime $p$

Now, is the number of solutions finite? Let's see. From the parametrization, $S(m+g) = 10p$. Since $p$ is prime, $10p$ has a bounded number of divisors, and $S$ and $m+g$ are divisors. But $p$ can be arbitrarily large...

Hmm, but we also need $q = \frac{2g^2 D}{t}$ to be a perfect square, and $t = S + D$, and $t | 2g^2$. So $t \leq 2g^2$. And $S = t - D < t \leq 2g^2$. And $m + g$ divides $10p$ with $S(m+g) = 10p$.

If $S$ is small (bounded by $2g^2$) and $m + g = \frac{10p}{S}$, then as $p$ grows, $m + g$ grows. But $m = \sqrt{\frac{2g^2 D}{t}}$ and $g$ are related... Let me think differently.

Actually, $m + g$ grows with $p$ means either $m$ or $g$ grows. But $g$ is bounded by... no, $g$ is not bounded a priori. Let me think again.

We have $S(m+g) = 10p$. $S = t - D$ where $t | 2g^2$. So $S \leq t - 1 \leq 2g^2 - 1$.

If $g$ is large, $S$ can be large, and $m + g$ can be small. But $m = \sqrt{2g^2 D / t} \geq \sqrt{2g^2 \cdot 1 / (2g^2)} = 1$. And $m + g \geq g + 1$.

So $S(m+g) \geq S(g+1)$. And $S \geq 1$, so $10p \geq g + 1$, meaning $g \leq 10p - 1$. That doesn't bound things.

But also $S \leq 2g^2$ and $m + g \geq g + 1$, so $10p = S(m+g) \leq 2g^2 \cdot (m+g)$. Hmm, this doesn't directly bound $p$.

Let me think about it differently. We have $m = \sqrt{2g^2 D/t}$. And $t = S + D$, $S = 10p/(m+g)$.

Actually, let me try to just enumerate solutions for small perimeters and see if there's a pattern or if the solutions stop.

Let me go back to direct computation. For each prime $p$, perimeter = $10p$, and we need to find integer triangles with $a + b + c = 10p$ and the angle bisector condition.

Let me use the parametrization. We have $a + s = 10p$ where $s = b + c$, and $a^2 = \frac{2ds^2}{s+d}$ where $d = c - b$.

So $a = 10p - s$, and $(10p - s)^2 = \frac{2ds^2}{s+d}$.

$(10p - s)^2(s + d) = 2ds^2$

Let me expand: $(100p^2 - 20ps + s^2)(s + d) = 2ds^2$

$100p^2 s + 100p^2 d - 20ps^2 - 20psd + s^3 + ds^2 = 2ds^2$

$100p^2 s + 100p^2 d - 20ps^2 - 20psd + s^3 + ds^2 - 2ds^2 = 0$

$100p^2 s + 100p^2 d - 20ps^2 - 20psd + s^3 - ds^2 = 0$

$100p^2(s + d) - 20ps(s + d) + s^2(s - d) = 0$

$(s+d)(100p^2 - 20ps) + s^2(s-d) = 0$

$(s+d) \cdot 20p(5p - s) + s^2(s-d) = 0$

Since $s + d > 0$ and $s^2 > 0$:
$20p(5p - s)(s+d) = s^2(d - s) = -s^2(s - d)$

So $20p(s - 5p)(s+d) = s^2(s-d)$.

Since $s > d > 0$, the right side is positive. So we need $s - 5p > 0$, i.e., $s > 5p$.

But $a = 10p - s > 0$ requires $s < 10p$. So $5p < s < 10p$.

Also $a < s$ (triangle inequality $b + c > a$) gives $10p - s < s$, i.e., $s > 5p$. Consistent.

And $a > 0$ gives $s < 10p$.

So $5p < s < 10p$, $0 < d < s$, $s \equiv d \pmod 2$.

From $20p(s - 5p)(s+d) = s^2(s-d)$:

Let me solve for $d$:
$20p(s-5p)s + 20p(s-5p)d = s^3 - s^2 d$

$20p(s-5p)d + s^2 d = s^3 - 20p(s-5p)s$

$d(20p(s-5p) + s^2) = s(s^2 - 20p(s-5p))$

$d = \frac{s(s^2 - 20p(s-5p))}{s^2 + 20p(s-5p)}$

Let me simplify the numerator and denominator.

Numerator: $s(s^2 - 20ps + 100p^2) = s(s - 10p)^2 = s \cdot a^2$ (since $a = 10p - s$).

Denominator: $s^2 + 20ps - 100p^2 = (s + 10p)^2 - 200p^2$... hmm, let me check: $(s+10p)^2 = s^2 + 20ps + 100p^2$, so $s^2 + 20ps - 100p^2 = (s+10p)^2 - 200p^2$. Not super clean.

Alternatively: $s^2 + 20p(s - 5p) = s^2 + 20ps - 100p^2$.

So $d = \frac{s(10p - s)^2}{s^2 + 20ps - 100p^2} = \frac{sa^2}{s^2 + 20ps - 100p^2}$.

Note $a = 10p - s$, so $s = 10p - a$ and:

$d = \frac{(10p - a) \cdot a^2}{(10p-a)^2 + 20p(10p - a) - 100p^2}$

Denominator: $(10p-a)^2 + 20p(10p-a) - 100p^2 = 100p^2 - 20pa + a^2 + 200p^2 - 20pa - 100p^2 = 200p^2 - 40pa + a^2 = (a - 20p)^2 + 200p^2 - 400p^2$... hmm, let me just compute directly.

$= 100p^2 - 20pa + a^2 + 200p^2 - 20pa - 100p^2 = a^2 - 40pa + 200p^2$

So $d = \frac{(10p - a) \cdot a^2}{a^2 - 40pa + 200p^2}$.

For $d$ to be a positive integer, we need $a^2 - 40pa + 200p^2 > 0$ and $(a^2 - 40pa + 200p^2) | (10p - a) a^2$.

$a^2 - 40pa + 200p^2 > 0$: discriminant $= 1600p^2 - 800p^2 = 800p^2$, roots at $a = \frac{40p \pm \sqrt{800p^2}}{2} = \frac{40p \pm 20p\sqrt{2}}{2} = 20p \pm 10p\sqrt{2}$.

So $a < 20p - 10p\sqrt{2} \approx 20p - 14.14p = 5.86p$ or $a > 20p + 10p\sqrt{2} \approx 34.14p$.

Since $0 < a < 5p$ (from $s > 5p$ and $a = 10p - s < 5p$), we have $a < 5p < 5.86p$, so the denominator is positive. Good.

So we need $0 < a < 5p$ and $d = \frac{(10p-a)a^2}{a^2 - 40pa + 200p^2}$ is a positive integer with $d < s = 10p - a$ and $d \equiv s \pmod{2}$.

Let me substitute $a = kp$ for some rational... actually, let me try specific primes.

For $p = 2$: perimeter = 20. $0 < a < 10$, $5 \cdot 2 = 10 < s < 20$, so $s \in \{11, 12, ..., 19\}$, $a = 20 - s \in \{1, ..., 9\}$.

$d = \frac{(20-a)a^2}{a^2 - 80a + 800}$.

Let me compute for each $a$ from 1 to 9:

$a=1$: $d = \frac{19 \cdot 1}{1 - 80 + 800} = \frac{19}{721}$. Not integer.
$a=2$: $d = \frac{18 \cdot 4}{4 - 160 + 800} = \frac{72}{644} = \frac{18}{161}$. Not integer.
$a=3$: $d = \frac{17 \cdot 9}{9 - 240 + 800} = \frac{153}{569}$. Not integer.
$a=4$: $d = \frac{16 \cdot 16}{16 - 320 + 800} = \frac{256}{496} = \frac{16}{31}$. Not integer.
$a=5$: $d = \frac{15 \cdot 25}{25 - 400 + 800} = \frac{375}{425} = \frac{15}{17}$. Not integer.
$a=6$: $d = \frac{14 \cdot 36}{36 - 480 + 800} = \frac{504}{356} = \frac{126}{89}$. Not integer.
$a=7$: $d = \frac{13 \cdot 49}{49 - 560 + 800} = \frac{637}{289} = \frac{637}{289}$. $289 = 17^2$. $637 = 7 \cdot 91 = 7 \cdot 7 \cdot 13 = 49 \cdot 13$. So $\frac{637}{289} = \frac{49 \cdot 13}{17^2}$. Not integer.
$a=8$: $d = \frac{12 \cdot 64}{64 - 640 + 800} = \frac{768}{224} = \frac{48}{14} = \frac{24}{7}$. Not integer.
$a=9$: $d = \frac{11 \cdot 81}{81 - 720 + 800} = \frac{891}{161}$. $161 = 7 \cdot 23$. $891 = 81 \cdot 11 = 3^4 \cdot 11$. Not divisible by 7 or 23. Not integer.

No solutions for $p = 2$.

For $p = 3$: perimeter = 30. $0 < a < 15$, $s = 30 - a$, $15 < s < 30$.

$d = \frac{(30-a)a^2}{a^2 - 120a + 1800}$.

Let me compute for $a$ from 1 to 14:

$a=1$: $d = \frac{29}{1 - 120 + 1800} = \frac{29}{1681}$. $1681 = 41^2$. Not integer.
$a=2$: $d = \frac{28 \cdot 4}{4 - 240 + 1800} = \frac{112}{1564} = \frac{28}{391}$. $391 = 17 \cdot 23$. Not integer.
$a=3$: $d = \frac{27 \cdot 9}{9 - 360 + 1800} = \frac{243}{1449} = \frac{81}{483} = \frac{27}{161}$. Not integer.
$a=4$: $d = \frac{26 \cdot 16}{16 - 480 + 1800} = \frac{416}{1336} = \frac{52}{167}$. Not integer.
$a=5$: $d = \frac{25 \cdot 25}{25 - 600 + 1800} = \frac{625}{1225} = \frac{25}{49}$. Not integer.
$a=6$: $d = \frac{24 \cdot 36}{36 - 720 + 1800} = \frac{864}{1116} = \frac{72}{93} = \frac{24}{31}$. Not integer.
$a=7$: $d = \frac{23 \cdot 49}{49 - 840 + 1800} = \frac{1127}{1009}$. $1009$ is prime. Not integer.
$a=8$: $d = \frac{22 \cdot 64}{64 - 960 + 1800} = \frac{1408}{904} = \frac{176}{113}$. Not integer.
$a=9$: $d = \frac{21 \cdot 81}{81 - 1080 + 1800} = \frac{1701}{801} = \frac{567}{267} = \frac{189}{89}$. Not integer.
$a=10$: $d = \frac{20 \cdot 100}{100 - 1200 + 1800} = \frac{2000}{700} = \frac{20}{7}$. Not integer.
$a=11$: $d = \frac{19 \cdot 121}{121 - 1320 + 1800} = \frac{2299}{601}$. $601$ is prime. Not integer.
$a=12$: $d = \frac{18 \cdot 144}{144 - 1440 + 1800} = \frac{2592}{504} = \frac{324}{63} = \frac{36}{7}$. Not integer.
$a=13$: $d = \frac{17 \cdot 169}{169 - 1560 + 1800} = \frac{2873}{409}$. $409$ is prime. Not integer.
$a=14$: $d = \frac{16 \cdot 196}{196 - 1680 + 1800} = \frac{3136}{316} = \frac{784}{79}$. Not integer.

No solutions for $p = 3$.

For $p = 5$: perimeter = 50. $0 < a < 25$, $s = 50 - a$.

$d = \frac{(50-a)a^2}{a^2 - 200a + 5000}$.

This is getting tedious. Let me think about whether there's a pattern or a smarter approach.

Let me reconsider the parametrization. We had:

$d = \frac{(10p - a) a^2}{a^2 - 40pa + 200p^2}$

Let me set $a = tp$ where... no, $a$ need not be a multiple of $p$.

Let me try a different substitution. Let $u = a/p$ (rational). Then:
$d = \frac{(10 - u) u^2 p^3}{(u^2 - 40u + 200) p^2} = \frac{(10-u)u^2 p}{u^2 - 40u + 200}$

For $d$ to be an integer, we need $(u^2 - 40u + 200) | (10-u)u^2 p$ where $u = a/p$ is rational.

Hmm, this is still complex. Let me try a slightly different approach.

Going back to: $20p(s-5p)(s+d) = s^2(s-d)$.

Let me set $s = 5p + r$ where $0 < r < 5p$ (so $a = 5p - r$).

$20p \cdot r \cdot (5p + r + d) = (5p + r)^2 (5p + r - d)$

$20pr(5p + r + d) = (5p + r)^2(5p + r - d)$

Let $S = 5p + r = s$. Then:
$20pr(S + d) = S^2(S - d)$
$20prS + 20prd = S^3 - S^2 d$
$d(20pr + S^2) = S^3 - 20prS = S(S^2 - 20pr)$
$d = \frac{S(S^2 - 20pr)}{S^2 + 20pr}$

Note $S = 5p + r$, $S^2 = 25p^2 + 10pr + r^2$.
$S^2 - 20pr = 25p^2 + 10pr + r^2 - 20pr = 25p^2 - 10pr + r^2 = (5p - r)^2 = a^2$.
$S^2 + 20pr = 25p^2 + 10pr + r^2 + 20pr = 25p^2 + 30pr + r^2$.

So $d = \frac{S \cdot a^2}{25p^2 + 30pr + r^2} = \frac{(5p+r)(5p-r)^2}{25p^2 + 30pr + r^2}$.

Let me denote the denominator as $D_0 = 25p^2 + 30pr + r^2$.

So $d = \frac{(5p+r)(5p-r)^2}{25p^2 + 30pr + r^2}$.

For this to be a positive integer, we need $D_0 | (5p+r)(5p-r)^2$.

Note that $D_0 = (5p+r)^2 + 20pr - (5p+r) \cdot ... $ hmm. Let me compute $\gcd(D_0, 5p+r)$ and $\gcd(D_0, 5p-r)$.

$D_0 = 25p^2 + 30pr + r^2$.
$(5p+r)^2 = 25p^2 + 10pr + r^2$.
$D_0 - (5p+r)^2 = 20pr$.

So $\gcd(D_0, 5p+r) = \gcd((5p+r)^2 + 20pr, 5p+r) = \gcd(20pr, 5p+r)$.

Similarly, $(5p-r)^2 = 25p^2 - 10pr + r^2$.
$D_0 - (5p-r)^2 = 40pr$.

So $\gcd(D_0, 5p-r) = \gcd((5p-r)^2 + 40pr, 5p-r) = \gcd(40pr, 5p-r)$.

This is getting complicated. Let me try yet another approach.

Going back to the original equation: $(c-b)(b+c)^2 = ca^2$.

Let $\gcd(a, b, c) = g_0$. Write $a = g_0 \alpha$, $b = g_0 \beta$, $c = g_0 \gamma$ with $\gcd(\alpha, \beta, \gamma) = 1$.

Then $(\gamma - \beta)(\beta + \gamma)^2 = \gamma \alpha^2$ (the $g_0$ cancels).

So we need to find primitive solutions $(\alpha, \beta, \gamma)$ with $\gcd(\alpha, \beta, \gamma) = 1$, $\gamma > \beta > 0$, $\alpha > 0$, satisfying $(\gamma - \beta)(\beta + \gamma)^2 = \gamma \alpha^2$, and then the perimeter is $g_0(\alpha + \beta + \gamma) = 10p$.

So $g_0(\alpha + \beta + \gamma) = 10p$ where $p$ is prime.

Since $p$ is prime, $10p = 2 \cdot 5 \cdot p$, and $g_0 | 10p$, and $(\alpha + \beta + \gamma) | 10p$.

The divisors of $10p$ (for $p \neq 2, 5$) are: $1, 2, 5, 10, p, 2p, 5p, 10p$.

So $\alpha + \beta + \gamma \in \{1, 2, 5, 10, p, 2p, 5p, 10p\}$ and $g_0 = \frac{10p}{\alpha + \beta + \gamma}$.

Since $\alpha, \beta, \gamma \geq 1$ and $\gamma > \beta$, we have $\alpha + \beta + \gamma \geq 1 + 1 + 2 = 4$. So $\alpha + \beta + \gamma \geq 4$.

For $p = 2$: $10p = 20$. Divisors $\geq 4$: $4, 5, 10, 20$. But wait, divisors of 20 are $1, 2, 4, 5, 10, 20$. So $\alpha + \beta + \gamma \in \{4, 5, 10, 20\}$.

For $p = 5$: $10p = 50$. Divisors $\geq 4$: $5, 10, 25, 50$.

For $p \neq 2, 5$: divisors $\geq 4$: $5, 10, p, 2p, 5p, 10p$ (and $4$ if $4 | 10p$, which requires $p = 2$, already handled).

So the primitive perimeter $\sigma = \alpha + \beta + \gamma$ is a divisor of $10p$ that is $\geq 4$.

Now I need to find all primitive solutions $(\alpha, \beta, \gamma)$ to $(\gamma - \beta)(\beta + \gamma)^2 = \gamma \alpha^2$ with $\gamma > \beta > 0$, $\alpha > 0$, $\gcd(\alpha, \beta, \gamma) = 1$.

Let me think about this equation. $(\gamma - \beta)(\beta + \gamma)^2 = \gamma \alpha^2$.

Let me set $\delta = \gamma - \beta > 0$ and $\sigma' = \beta + \gamma$. Then $\gamma = \frac{\sigma' + \delta}{2}$, $\beta = \frac{\sigma' - \delta}{2}$.

$\delta \cdot \sigma'^2 = \frac{\sigma' + \delta}{2} \cdot \alpha^2$

$2\delta \sigma'^2 = (\sigma' + \delta) \alpha^2$

$\alpha^2 = \frac{2\delta \sigma'^2}{\sigma' + \delta}$

This is the same as before with $d \to \delta$, $s \to \sigma'$.

Now, $\gcd(\alpha, \beta, \gamma) = 1$. We have $\beta = \frac{\sigma' - \delta}{2}$, $\gamma = \frac{\sigma' + \delta}{2}$, so $\gcd(\beta, \gamma) | \gcd(\frac{\sigma'-\delta}{2}, \frac{\sigma'+\delta}{2})$. And $\gcd(\frac{\sigma'-\delta}{2}, \frac{\sigma'+\delta}{2}) | \gcd(\sigma', \delta)$ (since their sum is $\sigma'$ and difference is $\delta$).

Actually, $\gcd(\beta, \gamma) | \gcd(\sigma', \delta)$ (since $2\beta = \sigma' - \delta$ and $2\gamma = \sigma' + \delta$, so $\gcd(2\beta, 2\gamma) = 2\gcd(\beta, \gamma)$ and $\gcd(2\beta, 2\gamma) | \gcd(\sigma' - \delta, \sigma' + \delta) | 2\gcd(\sigma', \delta)$... this is getting complicated with the factors of 2.

Let me try a different approach. Let me use the parametrization from before:

$g, D, S, t$ with $t = S + D$, $\gcd(S, D) = 1$, $t | 2g^2$, $q = 2g^2 D / t$ is a perfect square, $m = \sqrt{q}$, $a = Sm$, $s = gS$, $d = gD$.

And $\gcd(\alpha, \beta, \gamma) = 1$ where $\alpha = a/g_0$, etc. But actually, the primitive condition is $\gcd(\alpha, \beta, \gamma) = 1$ where $\alpha = a/g_0$, $\beta = b/g_0$, $\gamma = c/g_0$, and $g_0 = \gcd(a, b, c)$.

Hmm, this is getting quite involved. Let me try to just compute solutions for small perimeters and see if the answer is small.

Let me write $d = \frac{(10p-a)a^2}{a^2 - 40pa + 200p^2}$ and check for each prime $p$ and each valid $a$.

For $p = 5$: perimeter = 50, $0 < a < 25$.

$d = \frac{(50-a)a^2}{a^2 - 200a + 5000}$.

Let me compute the denominator for each $a$ and check divisibility.

$a=1$: num = $49$, den = $1 - 200 + 5000 = 4801$. $4801$ prime? $\sqrt{4801} \approx 69.3$. Check: $4801/7 = 685.86$, $4801/11 = 436.45$, $4801/13 = 369.31$, $4801/17 = 282.41$, $4801/19 = 252.68$, $4801/23 = 208.74$, $4801/29 = 165.55$, $4801/31 = 154.87$, $4801/37 = 129.76$, $4801/41 = 117.1$, $4801/43 = 111.65$, $4801/47 = 102.15$, $4801/53 = 90.58$, $4801/59 = 81.37$, $4801/61 = 78.7$, $4801/67 = 71.66$. So 4801 is prime. $49/4801$ not integer.

This is very tedious. Let me think if there's a smarter way.

Actually, let me reconsider. The equation is $(c-b)(b+c)^2 = ca^2$. Let me think about this as a Diophantine equation.

Let $\gcd(c, a) = h$. Write $c = hC$, $a = hA$ with $\gcd(C, A) = 1$.

Then $(hC - b)(hC + b)^2 = hC \cdot h^2 A^2 = h^3 C A^2$.

$(hC - b)(hC + b)^2 = h^3 C A^2$.

Let me also write $b = hB + r$... no, this doesn't simplify nicely.

Let me try $\gcd(c-b, c)$. Let $c - b = \delta$, so $b = c - \delta$. Then $\delta(2c - \delta)^2 = c a^2$.

$\delta(2c-\delta)^2 = ca^2$.

Let $\gcd(\delta, c) = e$. Write $\delta = e\delta'$, $c = ec'$. Then $e\delta'(2ec' - e\delta')^2 = ec' \cdot a^2$, so $e\delta' \cdot e^2(2c' - \delta')^2 = ec' a^2$, so $e^2 \delta'(2c'-\delta')^2 = c' a^2$.

Since $\gcd(\delta', c') = 1$ (as $\gcd(\delta/e, c/e) = 1$), and $\gcd(\delta', (2c'-\delta')^2)$... $\gcd(\delta', 2c'-\delta') = \gcd(\delta', 2c') = \gcd(\delta', 2)$ (since $\gcd(\delta', c') = 1$).

Case 1: $\delta'$ is odd. Then $\gcd(\delta', (2c'-\delta')^2) = 1$. So $\delta' | a^2$ and $(2c'-\delta')^2 | c' a^2 / \delta'$... hmm, this is still complex.

Let me try yet another approach. Let me use the substitution from the parametrization more carefully.

We had: $a^2 = \frac{2ds^2}{s+d}$ where $d = c - b$, $s = b + c$.

Let $g = \gcd(s, d)$, $s = gS$, $d = gD$, $\gcd(S, D) = 1$.

$a^2 = \frac{2gD \cdot g^2 S^2}{g(S+D)} = \frac{2g^2 DS^2}{S+D}$.

Let $t = S + D$. Then $a^2 = \frac{2g^2 DS^2}{t}$.

For $a$ to be a positive integer, $t | 2g^2 DS^2$. Since $\gcd(t, S) = \gcd(S+D, S) = \gcd(D, S) = 1$ and $\gcd(t, D) = \gcd(S+D, D) = \gcd(S, D) = 1$, we have $\gcd(t, DS^2) = 1$. So $t | 2g^2$.

Write $2g^2 = t \cdot k$. Then $a^2 = kDS^2$, so $a = S\sqrt{kD}$. Need $kD$ to be a perfect square.

Let $kD = m^2$. Then $a = Sm$, and $k = m^2/D$, so $2g^2 = t \cdot m^2/D$, so $2g^2 D = t m^2$, so $t = \frac{2g^2 D}{m^2}$.

For $t$ to be a positive integer, $m^2 | 2g^2 D$.

Also, $S = t - D = \frac{2g^2 D}{m^2} - D = D\left(\frac{2g^2}{m^2} - 1\right) = D \cdot \frac{2g^2 - m^2}{m^2}$.

For $S$ to be a positive integer, $m^2 | D(2g^2 - m^2)$, and $2g^2 > m^2$.

Also $\gcd(S, D) = 1$: $\gcd(D \cdot \frac{2g^2 - m^2}{m^2}, D) = D \cdot \gcd(\frac{2g^2 - m^2}{m^2}, 1)$... wait, this isn't right. $S = D(2g^2 - m^2)/m^2$. For $\gcd(S, D) = 1$, we need $D | 1$... no.

Hmm, let me reconsider. We need $\gcd(S, D) = 1$ where $S = t - D$ and $t = S + D$. So $\gcd(S, D) = \gcd(t - D, D) = \gcd(t, D) = 1$ (since $\gcd(t, D) = \gcd(S+D, D) = \gcd(S, D)$, which is circular).

OK let me just try to be more careful. We have $t | 2g^2$ and $k = 2g^2/t$ and $kD = m^2$. So $m^2 = 2g^2 D / t$.

The perimeter is $a + s = Sm + gS = S(m + g) = 10p$.

So we need $S(m + g) = 10p$ where:
- $g \geq 1$
- $D \geq 1$
- $t = S + D \geq 2$ (since $S \geq 1, D \geq 1$)
- $t | 2g^2$
- $m^2 = 2g^2 D / t$ is a perfect square, $m \geq 1$
- $\gcd(S, D) = 1$
- $S > D$ (equivalent to $s > d$, i.e., $b > 0$)
- $g(S - D) \equiv 0 \pmod{2}$ (parity: $s \equiv d \pmod 2$)
- $S(m + g) = 10p$

And then $a = Sm$, $b = g(S-D)/2$, $c = g(S+D)/2 = gt/2$.

For $b, c$ to be positive integers, we need $g(S-D)$ even and $g(S+D)$ even. Since $S - D$ and $S + D = t$ have the same parity (their difference is $2D$), we need $g \cdot t$ even (equivalently $g(S-D)$ even since $S-D$ and $S+D$ have same parity).

Wait, $S - D$ and $S + D$: $(S+D) - (S-D) = 2D$, so they have the same parity. So $g(S-D)$ even iff $g(S+D)$ even iff $gt$ even. So the parity condition is $gt$ even.

Now, the key equation is $S(m + g) = 10p$ with $p$ prime. The number of solutions depends on how many ways we can factor $10p$ as $S \cdot (m+g)$ and then find valid $g, D, t$.

Let me enumerate. For a given prime $p$, $10p = 2 \cdot 5 \cdot p$ (or $4 \cdot 5$ for $p=2$, $2 \cdot 25$ for $p=5$).

The factorizations $S \times (m+g) = 10p$ with $S \geq 2$ (since $S > D \geq 1$ means $S \geq 2$) and $m + g \geq 2$:

For general prime $p \neq 2, 5$:
$(S, m+g) \in \{(2, 5p), (5, 2p), (10, p), (p, 10), (2p, 5), (5p, 2), (10p, 1)\}$.

But $m + g \geq 2$ (since $m \geq 1, g \geq 1$), so we exclude $(10p, 1)$. Also $S \geq 2$.

So $(S, m+g) \in \{(2, 5p), (5, 2p), (10, p), (p, 10), (2p, 5), (5p, 2)\}$.

For each, we need $m + g = $ given value, $S = $ given value, and we need to find $g, D$ such that:
- $t = S + D$, $D \geq 1$, $D < S$
- $\gcd(S, D) = 1$
- $t | 2g^2$
- $m^2 = 2g^2 D / t$ is a perfect square
- $m = (m+g) - g$
- $gt$ even

Let me handle each case.

**Case $(S, m+g) = (2, 5p)$:**
$S = 2$, $D < 2$ so $D = 1$. $t = 3$. $\gcd(2, 1) = 1$ ✓.
$m + g = 5p$, $m = 5p - g$.
$t | 2g^2$: $3 | 2g^2$, so $3 | g$ (since $\gcd(3, 2) = 1$). Let $g = 3j$.
$m = 5p - 3j$.
$m^2 = 2 \cdot 9j^2 \cdot 1 / 3 = 6j^2$. So $(5p - 3j)^2 = 6j^2$.
$5p - 3j = j\sqrt{6}$ (taking positive root since $m > 0$). But $\sqrt{6}$ is irrational, so no integer solution unless $j = 0$, but $j \geq 1$. No solution.

Wait, I need $m^2 = 6j^2$ and $m = 5p - 3j$. So $(5p-3j)^2 = 6j^2$, i.e., $25p^2 - 30pj + 9j^2 = 6j^2$, i.e., $25p^2 - 30pj + 3j^2 = 0$. Discriminant: $900p^2 - 300p^2 = 600p^2$. $j = \frac{30p \pm \sqrt{600p^2}}{6} = \frac{30p \pm 10p\sqrt{6}}{6} = \frac{5p(3 \pm \sqrt{6})}{3}$. Not rational. No solution.

**Case $(S, m+g) = (5, 2p)$:**
$S = 5$, $D \in \{1, 2, 3, 4\}$ with $\gcd(5, D) = 1$, so $D \in \{1, 2, 3, 4\}$ (all coprime to 5).
$t = S + D \in \{6, 7, 8, 9\}$.
$m + g = 2p$, $m = 2p - g$.
$t | 2g^2$.
$m^2 = 2g^2 D / t$.

Subcase $D = 1, t = 6$: $6 | 2g^2$, so $3 | g^2$, so $3 | g$. $g = 3j$.
$m = 2p - 3j$. $m^2 = 2 \cdot 9j^2 / 6 = 3j^2$. $(2p - 3j)^2 = 3j^2$, $4p^2 - 12pj + 9j^2 = 3j^2$, $4p^2 - 12pj + 6j^2 = 0$, $2p^2 - 6pj + 3j^2 = 0$. Discriminant: $36p^2 - 24p^2 = 12p^2$. $j = \frac{6p \pm 2p\sqrt{3}}{6} = \frac{p(3 \pm \sqrt{3})}{3}$. Not rational. No solution.

Subcase $D = 2, t = 7$: $7 | 2g^2$, so $7 | g$. $g = 7j$.
$m = 2p - 7j$. $m^2 = 2 \cdot 49j^2 \cdot 2 / 7 = 28j^2$. $(2p - 7j)^2 = 28j^2$, $4p^2 - 28pj + 49j^2 = 28j^2$, $4p^2 - 28pj + 21j^2 = 0$. Discriminant: $784p^2 - 336p^2 = 448p^2 = 64 \cdot 7 \cdot p^2$. $\sqrt{448} = 8\sqrt{7}$. $j = \frac{28p \pm 8p\sqrt{7}}{42} = \frac{p(14 \pm 4\sqrt{7})}{21}$. Not rational. No solution.

Subcase $D = 3, t = 8$: $8 | 2g^2$, so $4 | g^2$, so $2 | g$. $g = 2j$.
$m = 2p - 2j$. $m^2 = 2 \cdot 4j^2 \cdot 3 / 8 = 3j^2$. $(2p - 2j)^2 = 3j^2$, $4p^2 - 8pj + 4j^2 = 3j^2$, $4p^2 - 8pj + j^2 = 0$. Discriminant: $64p^2 - 16p^2 = 48p^2$. $j = \frac{8p \pm 4p\sqrt{3}}{2} = 4p \pm 2p\sqrt{3}$. Not rational. No solution.

Subcase $D = 4, t = 9$: $9 | 2g^2$, so $3 | g$. $g = 3j$.
$m = 2p - 3j$. $m^2 = 2 \cdot 9j^2 \cdot 4 / 9 = 8j^2$. $(2p - 3j)^2 = 8j^2$, $4p^2 - 12pj + 9j^2 = 8j^2$, $4p^2 - 12pj + j^2 = 0$. Discriminant: $144p^2 - 16p^2 = 128p^2$. $j = \frac{12p \pm 8p\sqrt{2}}{2} = 6p \pm 4p\sqrt{2}$. Not rational. No solution.

No solutions for $S = 5$.

**Case $(S, m+g) = (10, p)$:**
$S = 10$, $D \in \{1, ..., 9\}$ with $\gcd(10, D) = 1$, so $D \in \{1, 3, 7, 9\}$.
$t = 10 + D \in \{11, 13, 17, 19\}$.
$m + g = p$, $m = p - g$.
$t | 2g^2$.
$m^2 = 2g^2 D / t$.

Subcase $D = 1, t = 11$: $11 | 2g^2$, so $11 | g$. $g = 11j$.
$m = p - 11j$. $m^2 = 2 \cdot 121j^2 / 11 = 22j^2$. $(p - 11j)^2 = 22j^2$, $p^2 - 22pj + 121j^2 = 22j^2$, $p^2 - 22pj + 99j^2 = 0$. Discriminant: $484p^2 - 396p^2 = 88p^2$. $\sqrt{88} = 2\sqrt{22}$. $j = \frac{22p \pm 2p\sqrt{22}}{198} = \frac{p(11 \pm \sqrt{22})}{99}$. Not rational. No solution.

Subcase $D = 3, t = 13$: $13 | 2g^2$, so $13 | g$. $g = 13j$.
$m = p - 13j$. $m^2 = 2 \cdot 169j^2 \cdot 3 / 13 = 78j^2$. $(p - 13j)^2 = 78j^2$, $p^2 - 26pj + 169j^2 = 78j^2$, $p^2 - 26pj + 91j^2 = 0$. Discriminant: $676p^2 - 364p^2 = 312p^2$. $\sqrt{312} = 2\sqrt{78}$. $j = \frac{26p \pm 2p\sqrt{78}}{182} = \frac{p(13 \pm \sqrt{78})}{91}$. Not rational. No solution.

Subcase $D = 7, t = 17$: $17 | 2g^2$, so $17 | g$. $g = 17j$.
$m = p - 17j$. $m^2 = 2 \cdot 289j^2 \cdot 7 / 17 = 238j^2$. $(p - 17j)^2 = 238j^2$, $p^2 - 34pj + 289j^2 = 238j^2$, $p^2 - 34pj + 51j^2 = 0$. Discriminant: $1156p^2 - 204p^2 = 952p^2$. $\sqrt{952} = 2\sqrt{238} = 2\sqrt{238}$. $238 = 2 \cdot 119 = 2 \cdot 7 \cdot 17$. Not a perfect square. $j = \frac{34p \pm 2p\sqrt{238}}{102} = \frac{p(17 \pm \sqrt{238})}{51}$. Not rational. No solution.

Subcase $D = 9, t = 19$: $19 | 2g^2$, so $19 | g$. $g = 19j$.
$m = p - 19j$. $m^2 = 2 \cdot 361j^2 \cdot 9 / 19 = 342j^2$. $(p - 19j)^2 = 342j^2$, $p^2 - 38pj + 361j^2 = 342j^2$, $p^2 - 38pj + 19j^2 = 0$. Discriminant: $1444p^2 - 76p^2 = 1368p^2$. $\sqrt{1368} = \sqrt{4 \cdot 342} = 2\sqrt{342}$. $342 = 2 \cdot 171 = 2 \cdot 9 \cdot 19$. Not a perfect square. Not rational. No solution.

No solutions for $S = 10$.

**Case $(S, m+g) = (p, 10)$:**
$S = p$, $D \in \{1, ..., p-1\}$ with $\gcd(p, D) = 1$ (so $D$ not a multiple of $p$, which is automatic since $D < p$).
$t = p + D$.
$m + g = 10$, $m = 10 - g$, $1 \leq g \leq 9$ (since $m \geq 1$).
$t | 2g^2$.
$m^2 = 2g^2 D / t$.

So $t = p + D$ and $t | 2g^2$. Since $g \leq 9$, $2g^2 \leq 162$. So $t \leq 162$, meaning $p + D \leq 162$, so $p \leq 161$.

Also, $m^2 = 2g^2 D / (p + D)$, and $m = 10 - g$.

$(10 - g)^2 = \frac{2g^2 D}{p + D}$

$(10-g)^2 (p + D) = 2g^2 D$

$(10-g)^2 p + (10-g)^2 D = 2g^2 D$

$(10-g)^2 p = D(2g^2 - (10-g)^2)$

$D = \frac{(10-g)^2 p}{2g^2 - (10-g)^2}$

Let me compute $2g^2 - (10-g)^2$ for each $g$ from 1 to 9:

$g=1$: $2 - 81 = -79$. Negative, so $D < 0$. No.
$g=2$: $8 - 64 = -56$. Negative. No.
$g=3$: $18 - 49 = -31$. Negative. No.
$g=4$: $32 - 36 = -4$. Negative. No.
$g=5$: $50 - 25 = 25$. $D = \frac{25p}{25} = p$. But $D < S = p$, so $D = p$ is not valid (need $D < p$). No.
$g=6$: $72 - 16 = 56$. $D = \frac{16p}{56} = \frac{2p}{7}$. Need $7 | 2p$, so $7 | p$ (since $\gcd(7, 2) = 1$), so $p = 7$. Then $D = 2$. Check: $D < S = 7$ ✓. $\gcd(7, 2) = 1$ ✓. $t = 9$. $t | 2g^2 = 72$: $9 | 72$ ✓. $m = 10 - 6 = 4$. $m^2 = 16$. Check: $2 \cdot 36 \cdot 2 / 9 = 144/9 = 16$ ✓. $gt$ even: $6 \cdot 9 = 54$ even ✓.

So we have a solution! $g = 6$, $D = 2$, $S = 7$, $t = 9$, $m = 4$, $p = 7$.

$a = Sm = 7 \cdot 4 = 28$. $s = gS = 42$. $d = gD = 12$. $b = (s-d)/2 = 15$, $c = (s+d)/2 = 27$.

Triangle: $(a, b, c) = (28, 15, 27)$. Perimeter = $28 + 15 + 27 = 70 = 10 \cdot 7$ ✓.

Let me verify the angle bisector condition. $l_a^2 = bc(1 - a^2/(b+c)^2) = 15 \cdot 27 \cdot (1 - 784/1764) = 405 \cdot (980/1764) = 405 \cdot 245/441 = 405 \cdot 5/9 = 225$. So $l_a = 15 = b$ ✓.

$g=7$: $98 - 9 = 89$. $D = \frac{9p}{89}$. Need $89 | 9p$, so $89 | p$ (since $\gcd(89, 9) = 1$), so $p = 89$. $D = 9$. Check $D < S = 89$ ✓. $\gcd(89, 9) = 1$ ✓. $t = 98$. $t | 2g^2 = 98$: $98 | 98$ ✓. $m = 10 - 7 = 3$. $m^2 = 9$. Check: $2 \cdot 49 \cdot 9 / 98 = 882/98 = 9$ ✓. $gt$ even: $7 \cdot 98 = 686$ even ✓.

Solution! $g = 7$, $D = 9$, $S = 89$, $t = 98$, $m = 3$, $p = 89$.

$a = 89 \cdot 3 = 267$. $s = 7 \cdot 89 = 623$. $d = 7 \cdot 9 = 63$. $b = (623 - 63)/2 = 280$, $c = (623 + 63)/2 = 343$.

Triangle: $(267, 280, 343)$. Perimeter = $267 + 280 + 343 = 890 = 10 \cdot 89$ ✓.

Verify: $l_a^2 = 280 \cdot 343 \cdot (1 - 267^2/623^2)$. $267^2 = 71289$. $623^2 = 388129$. $1 - 71289/388129 = 316840/388129$. $280 \cdot 343 = 96040$. $l_a^2 = 96040 \cdot 316840 / 388129$. Let me check: $316840 / 388129$... $388129 = 623^2$. $316840 = 623^2 - 267^2 = (623-267)(623+267) = 356 \cdot 890$. So $l_a^2 = 96040 \cdot 356 \cdot 890 / 388129$. $96040 = 280 \cdot 343$. $388129 = 623^2$. $890 = 10 \cdot 89$. $356 = 4 \cdot 89$. So $l_a^2 = 280 \cdot 343 \cdot 4 \cdot 89 \cdot 10 \cdot 89 / 623^2 = 280 \cdot 343 \cdot 40 \cdot 89^2 / 623^2$. $623 = 7 \cdot 89$. $623^2 = 49 \cdot 89^2$. So $l_a^2 = 280 \cdot 343 \cdot 40 \cdot 89^2 / (49 \cdot 89^2) = 280 \cdot 343 \cdot 40 / 49 = 280 \cdot 7 \cdot 40 = 78400$. $l_a = 280 = b$ ✓.

$g=8$: $128 - 4 = 124$. $D = \frac{4p}{124} = \frac{p}{31}$. Need $31 | p$, so $p = 31$. $D = 1$. Check $D < S = 31$ ✓. $\gcd(31, 1) = 1$ ✓. $t = 32$. $t | 2g^2 = 128$: $32 | 128$ ✓. $m = 10 - 8 = 2$. $m^2 = 4$. Check: $2 \cdot 64 \cdot 1 / 32 = 128/32 = 4$ ✓. $gt$ even: $8 \cdot 32 = 256$ even ✓.

Solution! $g = 8$, $D = 1$, $S = 31$, $t = 32$, $m = 2$, $p = 31$.

$a = 31 \cdot 2 = 62$. $s = 8 \cdot 31 = 248$. $d = 8 \cdot 1 = 8$. $b = (248-8)/2 = 120$, $c = (248+8)/2 = 128$.

Triangle: $(62, 120, 128)$. Perimeter = $62 + 120 + 128 = 310 = 10 \cdot 31$ ✓.

Verify: $l_a^2 = 120 \cdot 128 \cdot (1 - 62^2/248^2)$. $62^2 = 3844$. $248^2 = 61504$. $3844/61504 = 3844/61504$. $\gcd(3844, 61504)$: $61504 / 3844 = 16$, so $3844 \cdot 16 = 61504$. So $1 - 1/16 = 15/16$. $l_a^2 = 120 \cdot 128 \cdot 15/16 = 120 \cdot 8 \cdot 15 = 14400$. $l_a = 120 = b$ ✓.

$g=9$: $162 - 1 = 161$. $D = \frac{p}{161}$. $161 = 7 \cdot 23$. Need $161 | p$, but $p$ is prime and $161$ is not prime. No solution.

So for Case $(S, m+g) = (p, 10)$, we get 3 solutions: $p = 7, 31, 89$.

**Case $(S, m+g) = (2p, 5)$:**
$S = 2p$, $D \in \{1, ..., 2p-1\}$ with $\gcd(2p, D) = 1$ (so $D$ odd and not a multiple of $p$).
$t = 2p + D$.
$m + g = 5$, $m = 5 - g$, $g \in \{1, 2, 3, 4\}$.
$t | 2g^2$.
$m^2 = 2g^2 D / t$.

$2g^2 \leq 32$, so $t \leq 32$, meaning $2p + D \leq 32$. Since $D \geq 1$, $2p \leq 31$, so $p \leq 15.5$, i.e., $p \in \{2, 3, 5, 7, 11, 13\}$ (primes up to 13).

$(5-g)^2 (2p + D) = 2g^2 D$
$(5-g)^2 \cdot 2p + (5-g)^2 D = 2g^2 D$
$(5-g)^2 \cdot 2p = D(2g^2 - (5-g)^2)$
$D = \frac{2p(5-g)^2}{2g^2 - (5-g)^2}$

$g=1$: $2 - 16 = -14$. Negative. No.
$g=2$: $8 - 9 = -1$. Negative. No.
$g=3$: $18 - 4 = 14$. $D = \frac{2p \cdot 4}{14} = \frac{4p}{7}$. Need $7 | 4p$, so $7 | p$, $p = 7$. $D = 4$. Check: $D < S = 14$ ✓. $\gcd(14, 4) = 2 \neq 1$. Fails! No solution.

$g=4$: $32 - 1 = 31$. $D = \frac{2p}{31}$. Need $31 | 2p$, so $p = 31$. But $p \leq 13$ from our bound. No solution.

No solutions for this case.

**Case $(S, m+g) = (5p, 2)$:**
$S = 5p$, $D \in \{1, ..., 5p-1\}$ with $\gcd(5p, D) = 1$.
$t = 5p + D$.
$m + g = 2$, so $m = 1, g = 1$.
$t | 2g^2 = 2$, so $t \in \{1, 2\}$. But $t = 5p + D \geq 5p + 1 \geq 11$. No solution.

Now I also need to handle $p = 2$ and $p = 5$ separately since they have different divisor structures.

**For $p = 2$:** $10p = 20 = 2^2 \cdot 5$. Divisors: $1, 2, 4, 5, 10, 20$.
$(S, m+g)$ with $S \geq 2$, $m+g \geq 2$: $(2, 10), (4, 5), (5, 4), (10, 2), (20, 1)$ [exclude last].

So $(S, m+g) \in \{(2, 10), (4, 5), (5, 4), (10, 2)\}$.

$(S, m+g) = (2, 10)$: $S=2, D=1, t=3$. $m+g=10$, $m=10-g$. $3|2g^2$ so $3|g$, $g=3j$. $m=10-3j$. $m^2 = 2 \cdot 9j^2/3 = 6j^2$. $(10-3j)^2 = 6j^2$, $100 - 60j + 9j^2 = 6j^2$, $3j^2 - 60j + 100 = 0$. Discriminant: $3600 - 1200 = 2400$. $\sqrt{2400} = 20\sqrt{6}$. Not rational. No.

$(S, m+g) = (4, 5)$: $S=4$, $D \in \{1, 3\}$ (coprime to 4). $t \in \{5, 7\}$. $m+g=5$, $m=5-g$, $g \in \{1,2,3,4\}$.

$D=1, t=5$: $5|2g^2$ so $5|g$, $g=5j$. But $g \leq 4$. No.
$D=3, t=7$: $7|2g^2$ so $7|g$, $g=7j$. But $g \leq 4$. No.

$(S, m+g) = (5, 4)$: $S=5$, $D \in \{1,2,3,4\}$. $t \in \{6,7,8,9\}$. $m+g=4$, $m=4-g$, $g \in \{1,2,3\}$.

$D=1, t=6$: $6|2g^2$ so $3|g$, $g=3$. $m=1$. $m^2=1$. Check: $2 \cdot 9 \cdot 1/6 = 3 \neq 1$. No.

Actually wait, let me redo. $m^2 = 2g^2 D/t = 2 \cdot 9 \cdot 1/6 = 3$. But $m = 1$, $m^2 = 1 \neq 3$. No.

$D=2, t=7$: $7|2g^2$ so $7|g$. $g \leq 3$. No.
$D=3, t=8$: $8|2g^2$ so $4|g^2$ so $2|g$. $g=2$. $m=2$. $m^2=4$. Check: $2 \cdot 4 \cdot 3/8 = 3 \neq 4$. No.
$D=4, t=9$: $9|2g^2$ so $3|g$. $g=3$. $m=1$. $m^2=1$. Check: $2 \cdot 9 \cdot 4/9 = 8 \neq 1$. No.

$(S, m+g) = (10, 2)$: $S=10$, $D \in \{1,3,7,9\}$. $t \in \{11,13,17,19\}$. $m+g=2$, $m=1, g=1$. $t|2g^2=2$, so $t \in \{1,2\}$. But $t \geq 11$. No.

No solutions for $p = 2$.

**For $p = 5$:** $10p = 50 = 2 \cdot 5^2$. Divisors: $1, 2, 5, 10, 25, 50$.
$(S, m+g)$ with $S \geq 2$, $m+g \geq 2$: $(2, 25), (5, 10), (10, 5), (25, 2), (50, 1)$ [exclude last].

$(S, m+g) = (2, 25)$: $S=2, D=1, t=3$. $m+g=25$, $m=25-g$. $3|g$, $g=3j$. $m=25-3j$. $m^2=6j^2$. $(25-3j)^2=6j^2$, $625-150j+9j^2=6j^2$, $3j^2-150j+625=0$. Discriminant: $22500-7500=15000$. $\sqrt{15000}=50\sqrt{6}$. Not rational. No.

$(S, m+g) = (5, 10)$: $S=5$, $D \in \{1,2,3,4\}$. $t \in \{6,7,8,9\}$. $m+g=10$, $m=10-g$, $g \in \{1,...,9\}$.

$D=1, t=6$: $6|2g^2$ so $3|g$, $g=3j$. $m=10-3j$. $m^2=2 \cdot 9j^2/6=3j^2$. $(10-3j)^2=3j^2$, $100-60j+9j^2=3j^2$, $6j^2-60j+100=0$, $3j^2-30j+50=0$. Discriminant: $900-600=300$. $\sqrt{300}=10\sqrt{3}$. Not rational. No.

$D=2, t=7$: $7|2g^2$ so $7|g$, $g=7j$. $m=10-7j$. $j=1$: $g=7, m=3$. $m^2=9$. Check: $2 \cdot 49 \cdot 2/7=28$. $9 \neq 28$. No.

$D=3, t=8$: $8|2g^2$ so $4|g^2$ so $2|g$, $g=2j$. $m=10-2j$. $m^2=2 \cdot 4j^2 \cdot 3/8=3j^2$. $(10-2j)^2=3j^2$, $100-40j+4j^2=3j^2$, $j^2-40j+100=0$. Discriminant: $1600-400=1200$. $\sqrt{1200}=20\sqrt{3}$. Not rational. No.

$D=4, t=9$: $9|2g^2$ so $3|g$, $g=3j$. $m=10-3j$. $m^2=2 \cdot 9j^2 \cdot 4/9=8j^2$. $(10-3j)^2=8j^2$, $100-60j+9j^2=8j^2$, $j^2-60j+100=0$. Discriminant: $3600-400=3200$. $\sqrt{3200}=40\sqrt{2}$. Not rational. No.

$(S, m+g) = (10, 5)$: $S=10$, $D \in \{1,3,7,9\}$. $t \in \{11,13,17,19\}$. $m+g=5$, $m=5-g$, $g \in \{1,2,3,4\}$.

$D=1, t=11$: $11|2g^2$ so $11|g$. $g \leq 4$. No.
$D=3, t=13$: $13|g$. No.
$D=7, t=17$: $17|g$. No.
$D=9, t=19$: $19|g$. No.

$(S, m+g) = (25, 2)$: $S=25$, $D \in \{1,...,24\}$, $\gcd(25, D)=1$ so $D$ not multiple of 5. $t=25+D$. $m+g=2$, $m=1, g=1$. $t|2$, so $t \leq 2$. But $t \geq 26$. No.

No solutions for $p = 5$.

Now let me also check: for general $p \neq 2, 5$, I considered cases $(S, m+g) \in \{(2, 5p), (5, 2p), (10, p), (p, 10), (2p, 5), (5p, 2)\}$.

I found solutions only in case $(S, m+g) = (p, 10)$: three solutions with $p = 7, 31, 89$.

Wait, but I should also check if there are solutions where $g_0 > 1$, i.e., the triangle is not primitive. Let me reconsider.

The perimeter is $g_0 \cdot \sigma = 10p$ where $\sigma = \alpha + \beta + \gamma$ is the primitive perimeter and $g_0 = \gcd(a, b, c)$.

In my parametrization, $g$ is $\gcd(s, d) = \gcd(b+c, c-b)$, which is not the same as $g_0 = \gcd(a, b, c)$.

Let me re-examine. I had $a = Sm$, $s = gS$, $d = gD$, so $b = g(S-D)/2$, $c = g(S+D)/2$, $a = Sm$.

$g_0 = \gcd(a, b, c) = \gcd(Sm, g(S-D)/2, g(S+D)/2)$.

The perimeter is $Sm + gS = S(m + g) = 10p$.

So the perimeter is directly $S(m+g)$, and I don't need to separately consider $g_0$. The parametrization already covers all triangles (not just primitive ones), because $g$ in the parametrization is $\gcd(s, d)$, not $\gcd(a, b, c)$.

Wait, but does the parametrization cover ALL integer triangles satisfying the condition? Let me verify.

Given any integer triangle with $l_a = b$, we have $a, b, c$ positive integers, $c > b$ (shown earlier), and $(c-b)(b+c)^2 = ca^2$. Setting $d = c - b$, $s = b + c$, $g = \gcd(s, d)$, $S = s/g$, $D = d/g$, we get the parametrization. And $a^2 = 2ds^2/(s+d) = 2gDS^2/(S+D) \cdot g^2/g = ... $ wait let me recheck.

$a^2 = \frac{2ds^2}{s+d} = \frac{2 \cdot gD \cdot g^2S^2}{g(S+D)} = \frac{2g^2 DS^2}{S+D}$.

With $t = S + D$ and $t | 2g^2$ (shown), $k = 2g^2/t$, $a^2 = kDS^2$, $a = S\sqrt{kD}$, $m = \sqrt{kD}$.

Yes, this covers all solutions. And the perimeter is $a + s = Sm + gS = S(m + g)$. So $S(m+g) = 10p$.

So I need to find all $(S, D, g, m)$ satisfying all the constraints with $S(m+g) = 10p$ for some prime $p$.

I've checked all factorizations of $10p$ for general $p \neq 2, 5$ and for $p = 2, 5$. Let me also verify I haven't missed any factorizations.

For $p \neq 2, 5$: $10p = 2 \cdot 5 \cdot p$. Divisors: $1, 2, 5, 10, p, 2p, 5p, 10p$. With $S \geq 2$ and $m+g \geq 2$:
- $S = 2, m+g = 5p$ ✓ (checked, no solution)
- $S = 5, m+g = 2p$ ✓ (checked, no solution)
- $S = 10, m+g = p$ ✓ (checked, no solution)
- $S = p, m+g = 10$ ✓ (checked, 3 solutions: $p = 7, 31, 89$)
- $S = 2p, m+g = 5$ ✓ (checked, no solution)
- $S = 5p, m+g = 2$ ✓ (checked, no solution)

For $p = 2$: $10p = 20$. Checked all, no solution.
For $p = 5$: $10p = 50$. Checked all, no solution.

So the total count is 3 triangles.

Wait, but I should double-check: are there other factorizations I might have missed? For $p \neq 2, 5$, the divisors of $10p$ are exactly $\{1, 2, 5, 10, p, 2p, 5p, 10p\}$. I've covered all pairs $(S, m+g)$ with $S \geq 2, m+g \geq 2$. Yes, I think that's complete.

But wait — I need to also make sure that within each case, I've found ALL valid $D$ values, not just some. Let me re-examine the case $(S, m+g) = (p, 10)$ more carefully.

In that case, $S = p$, $D$ ranges over $\{1, ..., p-1\}$ with $\gcd(p, D) = 1$ (automatic since $p$ is prime and $D < p$). We derived:

$D = \frac{(10-g)^2 p}{2g^2 - (10-g)^2}$

for $g \in \{1, ..., 9\}$, and we need $2g^2 - (10-g)^2 > 0$ and $D$ to be a positive integer with $D < p$ and $\gcd(p, D) = 1$.

I computed:
- $g=5$: $D = p$, but $D < p$ required. No.
- $g=6$: $D = 2p/7$, need $p = 7$, $D = 2$. ✓
- $g=7$: $D = 9p/89$, need $p = 89$, $D = 9$. ✓
- $g=8$: $D = p/31$, need $p = 31$, $D = 1$. ✓
- $g=9$: $D = p/161$, need $161 | p$, but $161 = 7 \cdot 23$ not prime. No.

For $g = 1, 2, 3, 4$: denominator negative, no solution.

So exactly 3 solutions. But wait, I need to also check the conditions $t | 2g^2$ and $gt$ even for each, which I did above and they all passed.

Let me also verify that $\gcd(S, D) = 1$ for each:
- $p=7, D=2$: $\gcd(7, 2) = 1$ ✓
- $p=31, D=1$: $\gcd(31, 1) = 1$ ✓
- $p=89, D=9$: $\gcd(89, 9) = 1$ ✓ (since 89 is prime and $9 < 89$)

And $D < S$:
- $2 < 7$ ✓
- $1 < 31$ ✓
- $9 < 89$ ✓

All good. So the answer is **3**.

But wait, I want to make sure I haven't missed solutions in the other cases due to not checking all subcases. Let me re-examine case $(S, m+g) = (2p, 5)$ more carefully.

$S = 2p$, $D$ odd, $D$ not multiple of $p$, $1 \leq D < 2p$. $m + g = 5$, $g \in \{1, 2, 3, 4\}$.

$D = \frac{2p(5-g)^2}{2g^2 - (5-g)^2}$

$g=3$: $D = \frac{2p \cdot 4}{14} = \frac{4p}{7}$. Need $7 | p$, $p = 7$. $D = 4$. But $\gcd(2p, D) = \gcd(14, 4) = 2 \neq 1$. Fails.

$g=4$: $D = \frac{2p}{31}$. Need $p = 31$. $D = 2$. But $D$ must be odd (since $\gcd(2p, D) = 1$ requires $D$ odd). $D = 2$ is even. Fails.

So no solutions. ✓

Let me also re-examine case $(S, m+g) = (5, 2p)$ for $p = 2$ and $p = 5$ (which I might have missed).

For $p = 2$: $(S, m+g) = (5, 4)$. Already checked above, no solution.
For $p = 5$: $(S, m+g) = (5, 10)$. Already checked, no solution.

And case $(S, m+g) = (10, p)$ for $p = 2$: $(10, 2)$. Already checked, no solution.
For $p = 5$: $(10, 5)$. Already checked, no solution.

And case $(S, m+g) = (2, 5p)$ for $p = 2$: $(2, 10)$. Checked, no solution.
For $p = 5$: $(2, 25)$. Checked, no solution.

And case $(S, m+g) = (5p, 2)$ for $p = 2$: $(10, 2)$. Checked, no solution.
For $p = 5$: $(25, 2)$. Checked, no solution.

And case $(S, m+g) = (2p, 5)$ for $p = 2$: $(4, 5)$. Checked, no solution.
For $p = 5$: $(10, 5)$. Checked, no solution.

And case $(S, m+g) = (p, 10)$ for $p = 2$: $(2, 10)$. Already covered in $(2, 10)$ case. No solution.
For $p = 5$: $(5, 10)$. Already covered. No solution.

I think I've been thorough. Let me also consider: for $p = 2$, the divisor 4 of 20 gives $(S, m+g) = (4, 5)$, which I checked. And $(S, m+g) = (5, 4)$, also checked.

For $p = 5$, the divisor 25 of 50 gives $(S, m+g) = (25, 2)$, checked. And $(S, m+g) = (2, 25)$, checked.

So the total number of integer triangles is **3**.

Actually, hold on. Let me reconsider whether I need to worry about the case $p = 2$ with the factorization $20 = 4 \times 5$. I had $S = 4, m+g = 5$. Let me recheck.

$S = 4$, $D \in \{1, 3\}$ (coprime to 4). $t \in \{5, 7\}$. $m + g = 5$, $g \in \{1, 2, 3, 4\}$.

$D = 1, t = 5$: $5 | 2g^2$ so $5 | g$. $g = 5$? No, $g \leq 4$. No solution.

Hmm wait, but I should use the formula: $D = \frac{(5-g)^2 \cdot 4}{2g^2 - (5-g)^2}$ (substituting $S = 4$ and $m+g = 5$, so $p$ is replaced by... wait, no. The formula was specific to $S = p$.

Let me redo this case from scratch. $S = 4$, $m + g = 5$, $m = 5 - g$.

$t = S + D = 4 + D$. $t | 2g^2$. $m^2 = 2g^2 D / t$.

$(5-g)^2 = 2g^2 D / (4 + D)$
$(5-g)^2 (4 + D) = 2g^2 D$
$4(5-g)^2 + (5-g)^2 D = 2g^2 D$
$4(5-g)^2 = D(2g^2 - (5-g)^2)$
$D = \frac{4(5-g)^2}{2g^2 - (5-g)^2}$

$g=1$: $D = 4 \cdot 16 / (2 - 16) = 64 / (-14)$. Negative. No.
$g=2$: $D = 4 \cdot 9 / (8 - 9) = 36 / (-1)$. Negative. No.
$g=3$: $D = 4 \cdot 4 / (18 - 4) = 16/14 = 8/7$. Not integer. No.
$g=4$: $D = 4 \cdot 1 / (32 - 1) = 4/31$. Not integer. No.

No solutions. ✓

OK so I'm now confident the answer is 3.

Let me also verify the three triangles are valid (satisfy triangle inequality):
1. $(28, 15, 27)$: $28 < 15 + 27 = 42$ ✓, $15 < 28 + 27 = 55$ ✓, $27 < 28 + 15 = 43$ ✓.
2. $(62, 120, 128)$: $62 < 248$ ✓, $120 < 190$ ✓, $128 < 182$ ✓.
3. $(267, 280, 343)$: $267 < 623$ ✓, $280 < 610$ ✓, $343 < 547$ ✓.

All valid. The answer is **3**.

Now let me write up the proof.        — AI历史解题过程（thinking）
#   polymath_00478         — 题目ID

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
  <problem_id>polymath_00478</problem_id>
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

Find the number of integer triangles $ABC$ (with side lengths $a, b, c$) such that the length of the angle bisector from vertex $A$ is equal to the side length $b$ (where $b = AC$), and the perimeter $a+b+c$ is of the form $10p$ for some prime number $p$.

## Standard Solution

The condition that the angle bisector $l_a = b$ leads to the relation $a^2c = (c-b)(c+b)^2$. By setting $s=t^2$ and $s-r=k^2$ for coprime $t, k$, we find parameterized sides $a = xk(2t^2 - k^2)$, $b = xt(t^2 - k^2)$, and $c = xt^3$. The perimeter condition $a+b+c = x(k+t)(2t^2-k^2) = 10p$.
The case analysis for $x, k, t$ in the original solution yields three sets of side lengths: $(28, 15, 27)$ where $p=7$, $(267, 280, 343)$ where $p=89$, and $(62, 120, 128)$ where $p=31$. These are the only valid integer triangles satisfying the conditions.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. The problem asks for integer triangles ABC with side lengths a, b, c where the angle bisector from vertex A equals side length b (where b = AC), and the perimeter a+b+c is of the form 10p for some prime p.

Let me set up the problem. In triangle ABC, sides are a = BC, b = CA, c = AB. The angle bisector from vertex A divides the opposite side BC into segments proportional to the adjacent sides.

The angle bisector from A has length given by the formula:
$$l_a = \frac{2bc \cos(A/2)}{b+c}$$
or equivalently:
$$l_a^2 = bc\left(1 - \frac{a^2}{(b+c)^2}\right) = \frac{bc((b+c)^2 - a^2)}{(b+c)^2}$$

We want $l_a = b$.

So $l_a^2 = b^2$:
$$\frac{bc((b+c)^2 - a^2)}{(b+c)^2} = b^2$$

$$\frac{c((b+c)^2 - a^2)}{(b+c)^2} = b$$

$$c((b+c)^2 - a^2) = b(b+c)^2$$

$$c(b+c)^2 - ca^2 = b(b+c)^2$$

$$(c-b)(b+c)^2 = ca^2$$

So we need $(c-b)(b+c)^2 = ca^2$.

Let me think about this. We need c > b (since the left side must be positive, as a, b, c > 0 and (b+c)^2 > 0, we need c - b > 0, so c > b).

Let me set $d = c - b > 0$ and $s = b + c$. Then $c = \frac{s+d}{2}$, $b = \frac{s-d}{2}$.

The equation becomes:
$$d \cdot s^2 = \frac{s+d}{2} \cdot a^2$$

$$2ds^2 = (s+d)a^2$$

$$a^2 = \frac{2ds^2}{s+d}$$

For a to be an integer, we need $\frac{2ds^2}{s+d}$ to be a perfect square of a positive integer, and also a must satisfy triangle inequality.

Also, b and c must be positive integers, so s and d must have the same parity (both even or both odd), and s > d > 0.

Triangle inequality: a + b > c, a + c > b, b + c > a.
- b + c > a: s > a, i.e., $s^2 > a^2 = \frac{2ds^2}{s+d}$, so $1 > \frac{2d}{s+d}$, i.e., $s+d > 2d$, i.e., $s > d$. ✓ (already required)
- a + b > c: $a + \frac{s-d}{2} > \frac{s+d}{2}$, so $a > d$.
- a + c > b: $a + \frac{s+d}{2} > \frac{s-d}{2}$, so $a > -d$, always true since a, d > 0.

So we need $a > d = c - b$.

Let me think about this differently. Let me try small values.

Actually, let me think about it more carefully. We have:
$$a^2 = \frac{2ds^2}{s+d}$$

where $d = c - b$, $s = b + c$, $s > d > 0$, $s \equiv d \pmod{2}$, and $a > d$.

The perimeter is $a + b + c = a + s$, and we need $a + s = 10p$ for some prime $p$.

Let me try to find solutions systematically.

Let me set $d$ and $s$ and check.

For $d = 1$: $a^2 = \frac{2s^2}{s+1}$. We need $s+1 | 2s^2$. Since $\gcd(s, s+1) = 1$, we need $s+1 | 2$. So $s+1 \in \{1, 2\}$, meaning $s \in \{0, 1\}$. But $s > d = 1$, so $s \geq 2$. No solution.

Wait, let me redo. $s+1 | 2s^2$. $\gcd(s+1, s) = 1$ so $\gcd(s+1, s^2) = 1$, thus $s+1 | 2$. So $s+1 \in \{1, 2\}$, $s \in \{0, 1\}$. No valid $s$.

For $d = 2$: $a^2 = \frac{4s^2}{s+2}$. Need $s+2 | 4s^2$. $\gcd(s+2, s) = \gcd(2, s)$. 

If $s$ is even, $\gcd(s+2, s) = 2$. Let $s = 2m$. Then $s+2 = 2(m+1)$, $4s^2 = 16m^2$. Need $2(m+1) | 16m^2$, i.e., $(m+1) | 8m^2$. $\gcd(m+1, m) = 1$, so $(m+1) | 8$. $m+1 \in \{1,2,4,8\}$, $m \in \{0,1,3,7\}$, $s \in \{0,2,6,14\}$. Need $s > d = 2$, so $s \in \{6, 14\}$.

- $s = 6, d = 2$: $a^2 = \frac{4 \cdot 36}{8} = 18$. Not a perfect square.
- $s = 14, d = 2$: $a^2 = \frac{4 \cdot 196}{16} = 49$. $a = 7$. Check $a > d$: $7 > 2$ ✓. $b = \frac{14-2}{2} = 6$, $c = \frac{14+2}{2} = 8$. Triangle: $(7, 6, 8)$. Perimeter = $7 + 14 = 21$. $21 = 10p$? $p = 2.1$. Not integer. No.

If $s$ is odd, $\gcd(s+2, s) = 1$. Need $s+2 | 4s^2$, so $s+2 | 4$. $s+2 \in \{1,2,4\}$, $s \in \{-1, 0, 2\}$. Need $s > 2$ and $s$ odd. No.

For $d = 3$: $a^2 = \frac{6s^2}{s+3}$. Need $s+3 | 6s^2$. $\gcd(s+3, s) = \gcd(3, s)$.

If $3 | s$: $s = 3m$, $\gcd(s+3, s) = 3$. $s+3 = 3(m+1)$, $6s^2 = 54m^2$. Need $3(m+1) | 54m^2$, i.e., $(m+1) | 18m^2$. $\gcd(m+1, m) = 1$, so $(m+1) | 18$. $m+1 \in \{1,2,3,6,9,18\}$, $m \in \{0,1,2,5,8,17\}$, $s \in \{0,3,6,15,24,51\}$. Need $s > 3$ and $s \equiv d \pmod{2}$, i.e., $s$ odd. $s \in \{15, 51\}$ (since 6, 24 are even).

- $s = 15, d = 3$: $a^2 = \frac{6 \cdot 225}{18} = 75$. Not a perfect square.
- $s = 51, d = 3$: $a^2 = \frac{6 \cdot 2601}{54} = 289 = 17^2$. $a = 17$. Check $a > d$: $17 > 3$ ✓. $b = \frac{51-3}{2} = 24$, $c = \frac{51+3}{2} = 27$. Triangle: $(17, 24, 27)$. Perimeter = $17 + 51 = 68$. $68 = 10p$? $p = 6.8$. No.

If $3 \nmid s$: $\gcd(s+3, s) = 1$. Need $s+3 | 6$. $s+3 \in \{1,2,3,6\}$, $s \in \{-2,-1,0,3\}$. Need $s > 3$. No.

For $d = 4$: $a^2 = \frac{8s^2}{s+4}$. Need $s+4 | 8s^2$. $\gcd(s+4, s) = \gcd(4, s)$.

Let me think about this more systematically. Let $g = \gcd(s, d)$. Write $s = gS$, $d = gD$ with $\gcd(S, D) = 1$.

Then $a^2 = \frac{2gD \cdot g^2 S^2}{gS + gD} = \frac{2g^2 D S^2}{S + D}$.

So $a^2 = \frac{2g^2 D S^2}{S+D}$ where $\gcd(S, D) = 1$.

For this to be a perfect square, we need $(S+D) | 2g^2 D S^2$. Since $\gcd(S+D, S) | \gcd(S+D, S) = \gcd(D, S) = 1$... wait, $\gcd(S+D, S) = \gcd(D, S) = 1$. So $\gcd(S+D, S^2) = 1$.

Also $\gcd(S+D, D) = \gcd(S, D) = 1$. So $\gcd(S+D, DS^2) = 1$.

Therefore $(S+D) | 2g^2$.

Let $S + D = t$ where $t | 2g^2$.

Then $a^2 = \frac{2g^2 D S^2}{t}$. Since $t | 2g^2$, let $2g^2 = t \cdot k$, so $a^2 = k D S^2$, so $a = S\sqrt{kD}$.

For $a$ to be a positive integer, we need $kD$ to be a perfect square.

Also, $S = t - D$, and we need $S > 0$, $D > 0$, $\gcd(S, D) = 1$, i.e., $\gcd(t-D, D) = 1$, i.e., $\gcd(t, D) = 1$.

And $s > d$ means $gS > gD$, i.e., $S > D$, i.e., $t - D > D$, i.e., $t > 2D$.

And $s \equiv d \pmod{2}$: $gS \equiv gD \pmod{2}$, i.e., $g(S-D) \equiv 0 \pmod{2}$, i.e., $g(S-D)$ even. $S - D = t - 2D$. So $g(t - 2D)$ even.

And $a > d$: $S\sqrt{kD} > gD$, i.e., $(t-D)\sqrt{kD} > gD$.

And perimeter $= a + s = S\sqrt{kD} + gS = S(\sqrt{kD} + g)$. We need this to be $10p$ for prime $p$.

Also, $k = \frac{2g^2}{t}$, so $kD = \frac{2g^2 D}{t}$.

$a = S\sqrt{\frac{2g^2 D}{t}} = \frac{gS\sqrt{2D}}{\sqrt{t}} = \frac{gs\sqrt{2D}}{... }$... hmm, let me just keep $a = S\sqrt{kD}$ where $k = 2g^2/t$.

So $a = S \sqrt{\frac{2g^2 D}{t}}$.

For $a$ to be integer, $\frac{2g^2 D}{t}$ must be a perfect square.

Let me denote $q = \frac{2g^2 D}{t}$. We need $q$ to be a perfect square, and $a = S\sqrt{q}$, so $a = S \cdot m$ where $m = \sqrt{q}$.

Perimeter $= a + s = Sm + gS = S(m + g)$.

We need $S(m + g) = 10p$ for prime $p$.

So $S(m+g) \in \{10 \cdot 2, 10 \cdot 3, 10 \cdot 5, 10 \cdot 7, ...\} = \{20, 30, 50, 70, 110, 130, ...\}$.

Since $S(m+g) = 10p$ and $p$ is prime, the factorizations of $10p = 2 \cdot 5 \cdot p$ give us limited options for $S$ and $m+g$.

The divisors of $10p$ are: $1, 2, 5, 10, p, 2p, 5p, 10p$ (assuming $p \neq 2, 5$; need to handle $p=2$ and $p=5$ separately).

For $p = 2$: $10p = 20 = 2^2 \cdot 5$. Divisors: $1, 2, 4, 5, 10, 20$.
For $p = 5$: $10p = 50 = 2 \cdot 5^2$. Divisors: $1, 2, 5, 10, 25, 50$.
For $p \neq 2, 5$: $10p = 2 \cdot 5 \cdot p$. Divisors: $1, 2, 5, 10, p, 2p, 5p, 10p$.

So $S$ and $m+g$ are complementary divisors of $10p$, with $S \geq 1$ and $m + g \geq 2$ (since $g \geq 1$ and $m \geq 1$).

Actually, $m = \sqrt{q} = \sqrt{\frac{2g^2 D}{t}}$. We need $m$ to be a positive integer. And $g \geq 1$.

Let me think about what constraints we have:
- $g \geq 1$, $D \geq 1$, $S = t - D \geq 1$
- $\gcd(S, D) = \gcd(t, D) = 1$
- $t | 2g^2$
- $t > 2D$ (from $S > D$)
- $q = \frac{2g^2 D}{t}$ is a perfect square, $m = \sqrt{q}$
- $g(t - 2D)$ is even (parity condition)
- $Sm > gD$ (triangle inequality $a > d$)
- $S(m + g) = 10p$ for prime $p$

From $S(m+g) = 10p$ and $S = t - D$:
$(t-D)(m+g) = 10p$.

This is getting complex. Let me try a computational approach mentally, or rather, let me try to enumerate.

Since the perimeter is $10p$, and $p$ is prime, the perimeter is at least 20 (for $p=2$). There's no upper bound stated, so we need to find ALL such triangles. This means there should be finitely many.

Wait, is there an upper bound? The problem says "find the number of integer triangles" — this implies a finite number. Let me think about whether the constraints force finiteness.

From $a^2 = \frac{2ds^2}{s+d}$ and $a > d$ and $a < s$ (triangle inequality), we get $d^2 < \frac{2ds^2}{s+d} < s^2$.

From $a > d$: $\frac{2ds^2}{s+d} > d^2$, so $\frac{2s^2}{s+d} > d$, so $2s^2 > d(s+d) = ds + d^2$, so $2s^2 - ds - d^2 > 0$. Using quadratic formula in $s$: $s > \frac{d + \sqrt{d^2 + 8d^2}}{4} = \frac{d + 3d}{4} = d$. So $s > d$, which we already have. Actually, $2s^2 - ds - d^2 = (2s + d)(s - d) > 0$ when $s > d$. So this is always satisfied.

From $a < s$: $\frac{2ds^2}{s+d} < s^2$, so $\frac{2d}{s+d} < 1$, so $2d < s + d$, so $d < s$. Always satisfied.

So the triangle inequality $a > d$ is automatically satisfied when $s > d$? Let me double check. $a > d$ iff $a^2 > d^2$ iff $\frac{2ds^2}{s+d} > d^2$ iff $\frac{2s^2}{s+d} > d$ iff $2s^2 > d(s+d)$ iff $2s^2 - ds - d^2 > 0$ iff $(2s+d)(s-d) > 0$ iff $s > d$ (since $2s+d > 0$). Yes! So $a > d$ is equivalent to $s > d$, which is already required.

So the only constraints are:
1. $s > d > 0$
2. $s \equiv d \pmod{2}$
3. $a^2 = \frac{2ds^2}{s+d}$ is a perfect square
4. $a + s = 10p$ for prime $p$

Now, is the number of solutions finite? Let's see. From the parametrization, $S(m+g) = 10p$. Since $p$ is prime, $10p$ has a bounded number of divisors, and $S$ and $m+g$ are divisors. But $p$ can be arbitrarily large...

Hmm, but we also need $q = \frac{2g^2 D}{t}$ to be a perfect square, and $t = S + D$, and $t | 2g^2$. So $t \leq 2g^2$. And $S = t - D < t \leq 2g^2$. And $m + g$ divides $10p$ with $S(m+g) = 10p$.

If $S$ is small (bounded by $2g^2$) and $m + g = \frac{10p}{S}$, then as $p$ grows, $m + g$ grows. But $m = \sqrt{\frac{2g^2 D}{t}}$ and $g$ are related... Let me think differently.

Actually, $m + g$ grows with $p$ means either $m$ or $g$ grows. But $g$ is bounded by... no, $g$ is not bounded a priori. Let me think again.

We have $S(m+g) = 10p$. $S = t - D$ where $t | 2g^2$. So $S \leq t - 1 \leq 2g^2 - 1$.

If $g$ is large, $S$ can be large, and $m + g$ can be small. But $m = \sqrt{2g^2 D / t} \geq \sqrt{2g^2 \cdot 1 / (2g^2)} = 1$. And $m + g \geq g + 1$.

So $S(m+g) \geq S(g+1)$. And $S \geq 1$, so $10p \geq g + 1$, meaning $g \leq 10p - 1$. That doesn't bound things.

But also $S \leq 2g^2$ and $m + g \geq g + 1$, so $10p = S(m+g) \leq 2g^2 \cdot (m+g)$. Hmm, this doesn't directly bound $p$.

Let me think about it differently. We have $m = \sqrt{2g^2 D/t}$. And $t = S + D$, $S = 10p/(m+g)$.

Actually, let me try to just enumerate solutions for small perimeters and see if there's a pattern or if the solutions stop.

Let me go back to direct computation. For each prime $p$, perimeter = $10p$, and we need to find integer triangles with $a + b + c = 10p$ and the angle bisector condition.

Let me use the parametrization. We have $a + s = 10p$ where $s = b + c$, and $a^2 = \frac{2ds^2}{s+d}$ where $d = c - b$.

So $a = 10p - s$, and $(10p - s)^2 = \frac{2ds^2}{s+d}$.

$(10p - s)^2(s + d) = 2ds^2$

Let me expand: $(100p^2 - 20ps + s^2)(s + d) = 2ds^2$

$100p^2 s + 100p^2 d - 20ps^2 - 20psd + s^3 + ds^2 = 2ds^2$

$100p^2 s + 100p^2 d - 20ps^2 - 20psd + s^3 + ds^2 - 2ds^2 = 0$

$100p^2 s + 100p^2 d - 20ps^2 - 20psd + s^3 - ds^2 = 0$

$100p^2(s + d) - 20ps(s + d) + s^2(s - d) = 0$

$(s+d)(100p^2 - 20ps) + s^2(s-d) = 0$

$(s+d) \cdot 20p(5p - s) + s^2(s-d) = 0$

Since $s + d > 0$ and $s^2 > 0$:
$20p(5p - s)(s+d) = s^2(d - s) = -s^2(s - d)$

So $20p(s - 5p)(s+d) = s^2(s-d)$.

Since $s > d > 0$, the right side is positive. So we need $s - 5p > 0$, i.e., $s > 5p$.

But $a = 10p - s > 0$ requires $s < 10p$. So $5p < s < 10p$.

Also $a < s$ (triangle inequality $b + c > a$) gives $10p - s < s$, i.e., $s > 5p$. Consistent.

And $a > 0$ gives $s < 10p$.

So $5p < s < 10p$, $0 < d < s$, $s \equiv d \pmod 2$.

From $20p(s - 5p)(s+d) = s^2(s-d)$:

Let me solve for $d$:
$20p(s-5p)s + 20p(s-5p)d = s^3 - s^2 d$

$20p(s-5p)d + s^2 d = s^3 - 20p(s-5p)s$

$d(20p(s-5p) + s^2) = s(s^2 - 20p(s-5p))$

$d = \frac{s(s^2 - 20p(s-5p))}{s^2 + 20p(s-5p)}$

Let me simplify the numerator and denominator.

Numerator: $s(s^2 - 20ps + 100p^2) = s(s - 10p)^2 = s \cdot a^2$ (since $a = 10p - s$).

Denominator: $s^2 + 20ps - 100p^2 = (s + 10p)^2 - 200p^2$... hmm, let me check: $(s+10p)^2 = s^2 + 20ps + 100p^2$, so $s^2 + 20ps - 100p^2 = (s+10p)^2 - 200p^2$. Not super clean.

Alternatively: $s^2 + 20p(s - 5p) = s^2 + 20ps - 100p^2$.

So $d = \frac{s(10p - s)^2}{s^2 + 20ps - 100p^2} = \frac{sa^2}{s^2 + 20ps - 100p^2}$.

Note $a = 10p - s$, so $s = 10p - a$ and:

$d = \frac{(10p - a) \cdot a^2}{(10p-a)^2 + 20p(10p - a) - 100p^2}$

Denominator: $(10p-a)^2 + 20p(10p-a) - 100p^2 = 100p^2 - 20pa + a^2 + 200p^2 - 20pa - 100p^2 = 200p^2 - 40pa + a^2 = (a - 20p)^2 + 200p^2 - 400p^2$... hmm, let me just compute directly.

$= 100p^2 - 20pa + a^2 + 200p^2 - 20pa - 100p^2 = a^2 - 40pa + 200p^2$

So $d = \frac{(10p - a) \cdot a^2}{a^2 - 40pa + 200p^2}$.

For $d$ to be a positive integer, we need $a^2 - 40pa + 200p^2 > 0$ and $(a^2 - 40pa + 200p^2) | (10p - a) a^2$.

$a^2 - 40pa + 200p^2 > 0$: discriminant $= 1600p^2 - 800p^2 = 800p^2$, roots at $a = \frac{40p \pm \sqrt{800p^2}}{2} = \frac{40p \pm 20p\sqrt{2}}{2} = 20p \pm 10p\sqrt{2}$.

So $a < 20p - 10p\sqrt{2} \approx 20p - 14.14p = 5.86p$ or $a > 20p + 10p\sqrt{2} \approx 34.14p$.

Since $0 < a < 5p$ (from $s > 5p$ and $a = 10p - s < 5p$), we have $a < 5p < 5.86p$, so the denominator is positive. Good.

So we need $0 < a < 5p$ and $d = \frac{(10p-a)a^2}{a^2 - 40pa + 200p^2}$ is a positive integer with $d < s = 10p - a$ and $d \equiv s \pmod{2}$.

Let me substitute $a = kp$ for some rational... actually, let me try specific primes.

For $p = 2$: perimeter = 20. $0 < a < 10$, $5 \cdot 2 = 10 < s < 20$, so $s \in \{11, 12, ..., 19\}$, $a = 20 - s \in \{1, ..., 9\}$.

$d = \frac{(20-a)a^2}{a^2 - 80a + 800}$.

Let me compute for each $a$ from 1 to 9:

$a=1$: $d = \frac{19 \cdot 1}{1 - 80 + 800} = \frac{19}{721}$. Not integer.
$a=2$: $d = \frac{18 \cdot 4}{4 - 160 + 800} = \frac{72}{644} = \frac{18}{161}$. Not integer.
$a=3$: $d = \frac{17 \cdot 9}{9 - 240 + 800} = \frac{153}{569}$. Not integer.
$a=4$: $d = \frac{16 \cdot 16}{16 - 320 + 800} = \frac{256}{496} = \frac{16}{31}$. Not integer.
$a=5$: $d = \frac{15 \cdot 25}{25 - 400 + 800} = \frac{375}{425} = \frac{15}{17}$. Not integer.
$a=6$: $d = \frac{14 \cdot 36}{36 - 480 + 800} = \frac{504}{356} = \frac{126}{89}$. Not integer.
$a=7$: $d = \frac{13 \cdot 49}{49 - 560 + 800} = \frac{637}{289} = \frac{637}{289}$. $289 = 17^2$. $637 = 7 \cdot 91 = 7 \cdot 7 \cdot 13 = 49 \cdot 13$. So $\frac{637}{289} = \frac{49 \cdot 13}{17^2}$. Not integer.
$a=8$: $d = \frac{12 \cdot 64}{64 - 640 + 800} = \frac{768}{224} = \frac{48}{14} = \frac{24}{7}$. Not integer.
$a=9$: $d = \frac{11 \cdot 81}{81 - 720 + 800} = \frac{891}{161}$. $161 = 7 \cdot 23$. $891 = 81 \cdot 11 = 3^4 \cdot 11$. Not divisible by 7 or 23. Not integer.

No solutions for $p = 2$.

For $p = 3$: perimeter = 30. $0 < a < 15$, $s = 30 - a$, $15 < s < 30$.

$d = \frac{(30-a)a^2}{a^2 - 120a + 1800}$.

Let me compute for $a$ from 1 to 14:

$a=1$: $d = \frac{29}{1 - 120 + 1800} = \frac{29}{1681}$. $1681 = 41^2$. Not integer.
$a=2$: $d = \frac{28 \cdot 4}{4 - 240 + 1800} = \frac{112}{1564} = \frac{28}{391}$. $391 = 17 \cdot 23$. Not integer.
$a=3$: $d = \frac{27 \cdot 9}{9 - 360 + 1800} = \frac{243}{1449} = \frac{81}{483} = \frac{27}{161}$. Not integer.
$a=4$: $d = \frac{26 \cdot 16}{16 - 480 + 1800} = \frac{416}{1336} = \frac{52}{167}$. Not integer.
$a=5$: $d = \frac{25 \cdot 25}{25 - 600 + 1800} = \frac{625}{1225} = \frac{25}{49}$. Not integer.
$a=6$: $d = \frac{24 \cdot 36}{36 - 720 + 1800} = \frac{864}{1116} = \frac{72}{93} = \frac{24}{31}$. Not integer.
$a=7$: $d = \frac{23 \cdot 49}{49 - 840 + 1800} = \frac{1127}{1009}$. $1009$ is prime. Not integer.
$a=8$: $d = \frac{22 \cdot 64}{64 - 960 + 1800} = \frac{1408}{904} = \frac{176}{113}$. Not integer.
$a=9$: $d = \frac{21 \cdot 81}{81 - 1080 + 1800} = \frac{1701}{801} = \frac{567}{267} = \frac{189}{89}$. Not integer.
$a=10$: $d = \frac{20 \cdot 100}{100 - 1200 + 1800} = \frac{2000}{700} = \frac{20}{7}$. Not integer.
$a=11$: $d = \frac{19 \cdot 121}{121 - 1320 + 1800} = \frac{2299}{601}$. $601$ is prime. Not integer.
$a=12$: $d = \frac{18 \cdot 144}{144 - 1440 + 1800} = \frac{2592}{504} = \frac{324}{63} = \frac{36}{7}$. Not integer.
$a=13$: $d = \frac{17 \cdot 169}{169 - 1560 + 1800} = \frac{2873}{409}$. $409$ is prime. Not integer.
$a=14$: $d = \frac{16 \cdot 196}{196 - 1680 + 1800} = \frac{3136}{316} = \frac{784}{79}$. Not integer.

No solutions for $p = 3$.

For $p = 5$: perimeter = 50. $0 < a < 25$, $s = 50 - a$.

$d = \frac{(50-a)a^2}{a^2 - 200a + 5000}$.

This is getting tedious. Let me think about whether there's a pattern or a smarter approach.

Let me reconsider the parametrization. We had:

$d = \frac{(10p - a) a^2}{a^2 - 40pa + 200p^2}$

Let me set $a = tp$ where... no, $a$ need not be a multiple of $p$.

Let me try a different substitution. Let $u = a/p$ (rational). Then:
$d = \frac{(10 - u) u^2 p^3}{(u^2 - 40u + 200) p^2} = \frac{(10-u)u^2 p}{u^2 - 40u + 200}$

For $d$ to be an integer, we need $(u^2 - 40u + 200) | (10-u)u^2 p$ where $u = a/p$ is rational.

Hmm, this is still complex. Let me try a slightly different approach.

Going back to: $20p(s-5p)(s+d) = s^2(s-d)$.

Let me set $s = 5p + r$ where $0 < r < 5p$ (so $a = 5p - r$).

$20p \cdot r \cdot (5p + r + d) = (5p + r)^2 (5p + r - d)$

$20pr(5p + r + d) = (5p + r)^2(5p + r - d)$

Let $S = 5p + r = s$. Then:
$20pr(S + d) = S^2(S - d)$
$20prS + 20prd = S^3 - S^2 d$
$d(20pr + S^2) = S^3 - 20prS = S(S^2 - 20pr)$
$d = \frac{S(S^2 - 20pr)}{S^2 + 20pr}$

Note $S = 5p + r$, $S^2 = 25p^2 + 10pr + r^2$.
$S^2 - 20pr = 25p^2 + 10pr + r^2 - 20pr = 25p^2 - 10pr + r^2 = (5p - r)^2 = a^2$.
$S^2 + 20pr = 25p^2 + 10pr + r^2 + 20pr = 25p^2 + 30pr + r^2$.

So $d = \frac{S \cdot a^2}{25p^2 + 30pr + r^2} = \frac{(5p+r)(5p-r)^2}{25p^2 + 30pr + r^2}$.

Let me denote the denominator as $D_0 = 25p^2 + 30pr + r^2$.

So $d = \frac{(5p+r)(5p-r)^2}{25p^2 + 30pr + r^2}$.

For this to be a positive integer, we need $D_0 | (5p+r)(5p-r)^2$.

Note that $D_0 = (5p+r)^2 + 20pr - (5p+r) \cdot ... $ hmm. Let me compute $\gcd(D_0, 5p+r)$ and $\gcd(D_0, 5p-r)$.

$D_0 = 25p^2 + 30pr + r^2$.
$(5p+r)^2 = 25p^2 + 10pr + r^2$.
$D_0 - (5p+r)^2 = 20pr$.

So $\gcd(D_0, 5p+r) = \gcd((5p+r)^2 + 20pr, 5p+r) = \gcd(20pr, 5p+r)$.

Similarly, $(5p-r)^2 = 25p^2 - 10pr + r^2$.
$D_0 - (5p-r)^2 = 40pr$.

So $\gcd(D_0, 5p-r) = \gcd((5p-r)^2 + 40pr, 5p-r) = \gcd(40pr, 5p-r)$.

This is getting complicated. Let me try yet another approach.

Going back to the original equation: $(c-b)(b+c)^2 = ca^2$.

Let $\gcd(a, b, c) = g_0$. Write $a = g_0 \alpha$, $b = g_0 \beta$, $c = g_0 \gamma$ with $\gcd(\alpha, \beta, \gamma) = 1$.

Then $(\gamma - \beta)(\beta + \gamma)^2 = \gamma \alpha^2$ (the $g_0$ cancels).

So we need to find primitive solutions $(\alpha, \beta, \gamma)$ with $\gcd(\alpha, \beta, \gamma) = 1$, $\gamma > \beta > 0$, $\alpha > 0$, satisfying $(\gamma - \beta)(\beta + \gamma)^2 = \gamma \alpha^2$, and then the perimeter is $g_0(\alpha + \beta + \gamma) = 10p$.

So $g_0(\alpha + \beta + \gamma) = 10p$ where $p$ is prime.

Since $p$ is prime, $10p = 2 \cdot 5 \cdot p$, and $g_0 | 10p$, and $(\alpha + \beta + \gamma) | 10p$.

The divisors of $10p$ (for $p \neq 2, 5$) are: $1, 2, 5, 10, p, 2p, 5p, 10p$.

So $\alpha + \beta + \gamma \in \{1, 2, 5, 10, p, 2p, 5p, 10p\}$ and $g_0 = \frac{10p}{\alpha + \beta + \gamma}$.

Since $\alpha, \beta, \gamma \geq 1$ and $\gamma > \beta$, we have $\alpha + \beta + \gamma \geq 1 + 1 + 2 = 4$. So $\alpha + \beta + \gamma \geq 4$.

For $p = 2$: $10p = 20$. Divisors $\geq 4$: $4, 5, 10, 20$. But wait, divisors of 20 are $1, 2, 4, 5, 10, 20$. So $\alpha + \beta + \gamma \in \{4, 5, 10, 20\}$.

For $p = 5$: $10p = 50$. Divisors $\geq 4$: $5, 10, 25, 50$.

For $p \neq 2, 5$: divisors $\geq 4$: $5, 10, p, 2p, 5p, 10p$ (and $4$ if $4 | 10p$, which requires $p = 2$, already handled).

So the primitive perimeter $\sigma = \alpha + \beta + \gamma$ is a divisor of $10p$ that is $\geq 4$.

Now I need to find all primitive solutions $(\alpha, \beta, \gamma)$ to $(\gamma - \beta)(\beta + \gamma)^2 = \gamma \alpha^2$ with $\gamma > \beta > 0$, $\alpha > 0$, $\gcd(\alpha, \beta, \gamma) = 1$.

Let me think about this equation. $(\gamma - \beta)(\beta + \gamma)^2 = \gamma \alpha^2$.

Let me set $\delta = \gamma - \beta > 0$ and $\sigma' = \beta + \gamma$. Then $\gamma = \frac{\sigma' + \delta}{2}$, $\beta = \frac{\sigma' - \delta}{2}$.

$\delta \cdot \sigma'^2 = \frac{\sigma' + \delta}{2} \cdot \alpha^2$

$2\delta \sigma'^2 = (\sigma' + \delta) \alpha^2$

$\alpha^2 = \frac{2\delta \sigma'^2}{\sigma' + \delta}$

This is the same as before with $d \to \delta$, $s \to \sigma'$.

Now, $\gcd(\alpha, \beta, \gamma) = 1$. We have $\beta = \frac{\sigma' - \delta}{2}$, $\gamma = \frac{\sigma' + \delta}{2}$, so $\gcd(\beta, \gamma) | \gcd(\frac{\sigma'-\delta}{2}, \frac{\sigma'+\delta}{2})$. And $\gcd(\frac{\sigma'-\delta}{2}, \frac{\sigma'+\delta}{2}) | \gcd(\sigma', \delta)$ (since their sum is $\sigma'$ and difference is $\delta$).

Actually, $\gcd(\beta, \gamma) | \gcd(\sigma', \delta)$ (since $2\beta = \sigma' - \delta$ and $2\gamma = \sigma' + \delta$, so $\gcd(2\beta, 2\gamma) = 2\gcd(\beta, \gamma)$ and $\gcd(2\beta, 2\gamma) | \gcd(\sigma' - \delta, \sigma' + \delta) | 2\gcd(\sigma', \delta)$... this is getting complicated with the factors of 2.

Let me try a different approach. Let me use the parametrization from before:

$g, D, S, t$ with $t = S + D$, $\gcd(S, D) = 1$, $t | 2g^2$, $q = 2g^2 D / t$ is a perfect square, $m = \sqrt{q}$, $a = Sm$, $s = gS$, $d = gD$.

And $\gcd(\alpha, \beta, \gamma) = 1$ where $\alpha = a/g_0$, etc. But actually, the primitive condition is $\gcd(\alpha, \beta, \gamma) = 1$ where $\alpha = a/g_0$, $\beta = b/g_0$, $\gamma = c/g_0$, and $g_0 = \gcd(a, b, c)$.

Hmm, this is getting quite involved. Let me try to just compute solutions for small perimeters and see if the answer is small.

Let me write $d = \frac{(10p-a)a^2}{a^2 - 40pa + 200p^2}$ and check for each prime $p$ and each valid $a$.

For $p = 5$: perimeter = 50, $0 < a < 25$.

$d = \frac{(50-a)a^2}{a^2 - 200a + 5000}$.

Let me compute the denominator for each $a$ and check divisibility.

$a=1$: num = $49$, den = $1 - 200 + 5000 = 4801$. $4801$ prime? $\sqrt{4801} \approx 69.3$. Check: $4801/7 = 685.86$, $4801/11 = 436.45$, $4801/13 = 369.31$, $4801/17 = 282.41$, $4801/19 = 252.68$, $4801/23 = 208.74$, $4801/29 = 165.55$, $4801/31 = 154.87$, $4801/37 = 129.76$, $4801/41 = 117.1$, $4801/43 = 111.65$, $4801/47 = 102.15$, $4801/53 = 90.58$, $4801/59 = 81.37$, $4801/61 = 78.7$, $4801/67 = 71.66$. So 4801 is prime. $49/4801$ not integer.

This is very tedious. Let me think if there's a smarter way.

Actually, let me reconsider. The equation is $(c-b)(b+c)^2 = ca^2$. Let me think about this as a Diophantine equation.

Let $\gcd(c, a) = h$. Write $c = hC$, $a = hA$ with $\gcd(C, A) = 1$.

Then $(hC - b)(hC + b)^2 = hC \cdot h^2 A^2 = h^3 C A^2$.

$(hC - b)(hC + b)^2 = h^3 C A^2$.

Let me also write $b = hB + r$... no, this doesn't simplify nicely.

Let me try $\gcd(c-b, c)$. Let $c - b = \delta$, so $b = c - \delta$. Then $\delta(2c - \delta)^2 = c a^2$.

$\delta(2c-\delta)^2 = ca^2$.

Let $\gcd(\delta, c) = e$. Write $\delta = e\delta'$, $c = ec'$. Then $e\delta'(2ec' - e\delta')^2 = ec' \cdot a^2$, so $e\delta' \cdot e^2(2c' - \delta')^2 = ec' a^2$, so $e^2 \delta'(2c'-\delta')^2 = c' a^2$.

Since $\gcd(\delta', c') = 1$ (as $\gcd(\delta/e, c/e) = 1$), and $\gcd(\delta', (2c'-\delta')^2)$... $\gcd(\delta', 2c'-\delta') = \gcd(\delta', 2c') = \gcd(\delta', 2)$ (since $\gcd(\delta', c') = 1$).

Case 1: $\delta'$ is odd. Then $\gcd(\delta', (2c'-\delta')^2) = 1$. So $\delta' | a^2$ and $(2c'-\delta')^2 | c' a^2 / \delta'$... hmm, this is still complex.

Let me try yet another approach. Let me use the substitution from the parametrization more carefully.

We had: $a^2 = \frac{2ds^2}{s+d}$ where $d = c - b$, $s = b + c$.

Let $g = \gcd(s, d)$, $s = gS$, $d = gD$, $\gcd(S, D) = 1$.

$a^2 = \frac{2gD \cdot g^2 S^2}{g(S+D)} = \frac{2g^2 DS^2}{S+D}$.

Let $t = S + D$. Then $a^2 = \frac{2g^2 DS^2}{t}$.

For $a$ to be a positive integer, $t | 2g^2 DS^2$. Since $\gcd(t, S) = \gcd(S+D, S) = \gcd(D, S) = 1$ and $\gcd(t, D) = \gcd(S+D, D) = \gcd(S, D) = 1$, we have $\gcd(t, DS^2) = 1$. So $t | 2g^2$.

Write $2g^2 = t \cdot k$. Then $a^2 = kDS^2$, so $a = S\sqrt{kD}$. Need $kD$ to be a perfect square.

Let $kD = m^2$. Then $a = Sm$, and $k = m^2/D$, so $2g^2 = t \cdot m^2/D$, so $2g^2 D = t m^2$, so $t = \frac{2g^2 D}{m^2}$.

For $t$ to be a positive integer, $m^2 | 2g^2 D$.

Also, $S = t - D = \frac{2g^2 D}{m^2} - D = D\left(\frac{2g^2}{m^2} - 1\right) = D \cdot \frac{2g^2 - m^2}{m^2}$.

For $S$ to be a positive integer, $m^2 | D(2g^2 - m^2)$, and $2g^2 > m^2$.

Also $\gcd(S, D) = 1$: $\gcd(D \cdot \frac{2g^2 - m^2}{m^2}, D) = D \cdot \gcd(\frac{2g^2 - m^2}{m^2}, 1)$... wait, this isn't right. $S = D(2g^2 - m^2)/m^2$. For $\gcd(S, D) = 1$, we need $D | 1$... no.

Hmm, let me reconsider. We need $\gcd(S, D) = 1$ where $S = t - D$ and $t = S + D$. So $\gcd(S, D) = \gcd(t - D, D) = \gcd(t, D) = 1$ (since $\gcd(t, D) = \gcd(S+D, D) = \gcd(S, D)$, which is circular).

OK let me just try to be more careful. We have $t | 2g^2$ and $k = 2g^2/t$ and $kD = m^2$. So $m^2 = 2g^2 D / t$.

The perimeter is $a + s = Sm + gS = S(m + g) = 10p$.

So we need $S(m + g) = 10p$ where:
- $g \geq 1$
- $D \geq 1$
- $t = S + D \geq 2$ (since $S \geq 1, D \geq 1$)
- $t | 2g^2$
- $m^2 = 2g^2 D / t$ is a perfect square, $m \geq 1$
- $\gcd(S, D) = 1$
- $S > D$ (equivalent to $s > d$, i.e., $b > 0$)
- $g(S - D) \equiv 0 \pmod{2}$ (parity: $s \equiv d \pmod 2$)
- $S(m + g) = 10p$

And then $a = Sm$, $b = g(S-D)/2$, $c = g(S+D)/2 = gt/2$.

For $b, c$ to be positive integers, we need $g(S-D)$ even and $g(S+D)$ even. Since $S - D$ and $S + D = t$ have the same parity (their difference is $2D$), we need $g \cdot t$ even (equivalently $g(S-D)$ even since $S-D$ and $S+D$ have same parity).

Wait, $S - D$ and $S + D$: $(S+D) - (S-D) = 2D$, so they have the same parity. So $g(S-D)$ even iff $g(S+D)$ even iff $gt$ even. So the parity condition is $gt$ even.

Now, the key equation is $S(m + g) = 10p$ with $p$ prime. The number of solutions depends on how many ways we can factor $10p$ as $S \cdot (m+g)$ and then find valid $g, D, t$.

Let me enumerate. For a given prime $p$, $10p = 2 \cdot 5 \cdot p$ (or $4 \cdot 5$ for $p=2$, $2 \cdot 25$ for $p=5$).

The factorizations $S \times (m+g) = 10p$ with $S \geq 2$ (since $S > D \geq 1$ means $S \geq 2$) and $m + g \geq 2$:

For general prime $p \neq 2, 5$:
$(S, m+g) \in \{(2, 5p), (5, 2p), (10, p), (p, 10), (2p, 5), (5p, 2), (10p, 1)\}$.

But $m + g \geq 2$ (since $m \geq 1, g \geq 1$), so we exclude $(10p, 1)$. Also $S \geq 2$.

So $(S, m+g) \in \{(2, 5p), (5, 2p), (10, p), (p, 10), (2p, 5), (5p, 2)\}$.

For each, we need $m + g = $ given value, $S = $ given value, and we need to find $g, D$ such that:
- $t = S + D$, $D \geq 1$, $D < S$
- $\gcd(S, D) = 1$
- $t | 2g^2$
- $m^2 = 2g^2 D / t$ is a perfect square
- $m = (m+g) - g$
- $gt$ even

Let me handle each case.

**Case $(S, m+g) = (2, 5p)$:**
$S = 2$, $D < 2$ so $D = 1$. $t = 3$. $\gcd(2, 1) = 1$ ✓.
$m + g = 5p$, $m = 5p - g$.
$t | 2g^2$: $3 | 2g^2$, so $3 | g$ (since $\gcd(3, 2) = 1$). Let $g = 3j$.
$m = 5p - 3j$.
$m^2 = 2 \cdot 9j^2 \cdot 1 / 3 = 6j^2$. So $(5p - 3j)^2 = 6j^2$.
$5p - 3j = j\sqrt{6}$ (taking positive root since $m > 0$). But $\sqrt{6}$ is irrational, so no integer solution unless $j = 0$, but $j \geq 1$. No solution.

Wait, I need $m^2 = 6j^2$ and $m = 5p - 3j$. So $(5p-3j)^2 = 6j^2$, i.e., $25p^2 - 30pj + 9j^2 = 6j^2$, i.e., $25p^2 - 30pj + 3j^2 = 0$. Discriminant: $900p^2 - 300p^2 = 600p^2$. $j = \frac{30p \pm \sqrt{600p^2}}{6} = \frac{30p \pm 10p\sqrt{6}}{6} = \frac{5p(3 \pm \sqrt{6})}{3}$. Not rational. No solution.

**Case $(S, m+g) = (5, 2p)$:**
$S = 5$, $D \in \{1, 2, 3, 4\}$ with $\gcd(5, D) = 1$, so $D \in \{1, 2, 3, 4\}$ (all coprime to 5).
$t = S + D \in \{6, 7, 8, 9\}$.
$m + g = 2p$, $m = 2p - g$.
$t | 2g^2$.
$m^2 = 2g^2 D / t$.

Subcase $D = 1, t = 6$: $6 | 2g^2$, so $3 | g^2$, so $3 | g$. $g = 3j$.
$m = 2p - 3j$. $m^2 = 2 \cdot 9j^2 / 6 = 3j^2$. $(2p - 3j)^2 = 3j^2$, $4p^2 - 12pj + 9j^2 = 3j^2$, $4p^2 - 12pj + 6j^2 = 0$, $2p^2 - 6pj + 3j^2 = 0$. Discriminant: $36p^2 - 24p^2 = 12p^2$. $j = \frac{6p \pm 2p\sqrt{3}}{6} = \frac{p(3 \pm \sqrt{3})}{3}$. Not rational. No solution.

Subcase $D = 2, t = 7$: $7 | 2g^2$, so $7 | g$. $g = 7j$.
$m = 2p - 7j$. $m^2 = 2 \cdot 49j^2 \cdot 2 / 7 = 28j^2$. $(2p - 7j)^2 = 28j^2$, $4p^2 - 28pj + 49j^2 = 28j^2$, $4p^2 - 28pj + 21j^2 = 0$. Discriminant: $784p^2 - 336p^2 = 448p^2 = 64 \cdot 7 \cdot p^2$. $\sqrt{448} = 8\sqrt{7}$. $j = \frac{28p \pm 8p\sqrt{7}}{42} = \frac{p(14 \pm 4\sqrt{7})}{21}$. Not rational. No solution.

Subcase $D = 3, t = 8$: $8 | 2g^2$, so $4 | g^2$, so $2 | g$. $g = 2j$.
$m = 2p - 2j$. $m^2 = 2 \cdot 4j^2 \cdot 3 / 8 = 3j^2$. $(2p - 2j)^2 = 3j^2$, $4p^2 - 8pj + 4j^2 = 3j^2$, $4p^2 - 8pj + j^2 = 0$. Discriminant: $64p^2 - 16p^2 = 48p^2$. $j = \frac{8p \pm 4p\sqrt{3}}{2} = 4p \pm 2p\sqrt{3}$. Not rational. No solution.

Subcase $D = 4, t = 9$: $9 | 2g^2$, so $3 | g$. $g = 3j$.
$m = 2p - 3j$. $m^2 = 2 \cdot 9j^2 \cdot 4 / 9 = 8j^2$. $(2p - 3j)^2 = 8j^2$, $4p^2 - 12pj + 9j^2 = 8j^2$, $4p^2 - 12pj + j^2 = 0$. Discriminant: $144p^2 - 16p^2 = 128p^2$. $j = \frac{12p \pm 8p\sqrt{2}}{2} = 6p \pm 4p\sqrt{2}$. Not rational. No solution.

No solutions for $S = 5$.

**Case $(S, m+g) = (10, p)$:**
$S = 10$, $D \in \{1, ..., 9\}$ with $\gcd(10, D) = 1$, so $D \in \{1, 3, 7, 9\}$.
$t = 10 + D \in \{11, 13, 17, 19\}$.
$m + g = p$, $m = p - g$.
$t | 2g^2$.
$m^2 = 2g^2 D / t$.

Subcase $D = 1, t = 11$: $11 | 2g^2$, so $11 | g$. $g = 11j$.
$m = p - 11j$. $m^2 = 2 \cdot 121j^2 / 11 = 22j^2$. $(p - 11j)^2 = 22j^2$, $p^2 - 22pj + 121j^2 = 22j^2$, $p^2 - 22pj + 99j^2 = 0$. Discriminant: $484p^2 - 396p^2 = 88p^2$. $\sqrt{88} = 2\sqrt{22}$. $j = \frac{22p \pm 2p\sqrt{22}}{198} = \frac{p(11 \pm \sqrt{22})}{99}$. Not rational. No solution.

Subcase $D = 3, t = 13$: $13 | 2g^2$, so $13 | g$. $g = 13j$.
$m = p - 13j$. $m^2 = 2 \cdot 169j^2 \cdot 3 / 13 = 78j^2$. $(p - 13j)^2 = 78j^2$, $p^2 - 26pj + 169j^2 = 78j^2$, $p^2 - 26pj + 91j^2 = 0$. Discriminant: $676p^2 - 364p^2 = 312p^2$. $\sqrt{312} = 2\sqrt{78}$. $j = \frac{26p \pm 2p\sqrt{78}}{182} = \frac{p(13 \pm \sqrt{78})}{91}$. Not rational. No solution.

Subcase $D = 7, t = 17$: $17 | 2g^2$, so $17 | g$. $g = 17j$.
$m = p - 17j$. $m^2 = 2 \cdot 289j^2 \cdot 7 / 17 = 238j^2$. $(p - 17j)^2 = 238j^2$, $p^2 - 34pj + 289j^2 = 238j^2$, $p^2 - 34pj + 51j^2 = 0$. Discriminant: $1156p^2 - 204p^2 = 952p^2$. $\sqrt{952} = 2\sqrt{238} = 2\sqrt{238}$. $238 = 2 \cdot 119 = 2 \cdot 7 \cdot 17$. Not a perfect square. $j = \frac{34p \pm 2p\sqrt{238}}{102} = \frac{p(17 \pm \sqrt{238})}{51}$. Not rational. No solution.

Subcase $D = 9, t = 19$: $19 | 2g^2$, so $19 | g$. $g = 19j$.
$m = p - 19j$. $m^2 = 2 \cdot 361j^2 \cdot 9 / 19 = 342j^2$. $(p - 19j)^2 = 342j^2$, $p^2 - 38pj + 361j^2 = 342j^2$, $p^2 - 38pj + 19j^2 = 0$. Discriminant: $1444p^2 - 76p^2 = 1368p^2$. $\sqrt{1368} = \sqrt{4 \cdot 342} = 2\sqrt{342}$. $342 = 2 \cdot 171 = 2 \cdot 9 \cdot 19$. Not a perfect square. Not rational. No solution.

No solutions for $S = 10$.

**Case $(S, m+g) = (p, 10)$:**
$S = p$, $D \in \{1, ..., p-1\}$ with $\gcd(p, D) = 1$ (so $D$ not a multiple of $p$, which is automatic since $D < p$).
$t = p + D$.
$m + g = 10$, $m = 10 - g$, $1 \leq g \leq 9$ (since $m \geq 1$).
$t | 2g^2$.
$m^2 = 2g^2 D / t$.

So $t = p + D$ and $t | 2g^2$. Since $g \leq 9$, $2g^2 \leq 162$. So $t \leq 162$, meaning $p + D \leq 162$, so $p \leq 161$.

Also, $m^2 = 2g^2 D / (p + D)$, and $m = 10 - g$.

$(10 - g)^2 = \frac{2g^2 D}{p + D}$

$(10-g)^2 (p + D) = 2g^2 D$

$(10-g)^2 p + (10-g)^2 D = 2g^2 D$

$(10-g)^2 p = D(2g^2 - (10-g)^2)$

$D = \frac{(10-g)^2 p}{2g^2 - (10-g)^2}$

Let me compute $2g^2 - (10-g)^2$ for each $g$ from 1 to 9:

$g=1$: $2 - 81 = -79$. Negative, so $D < 0$. No.
$g=2$: $8 - 64 = -56$. Negative. No.
$g=3$: $18 - 49 = -31$. Negative. No.
$g=4$: $32 - 36 = -4$. Negative. No.
$g=5$: $50 - 25 = 25$. $D = \frac{25p}{25} = p$. But $D < S = p$, so $D = p$ is not valid (need $D < p$). No.
$g=6$: $72 - 16 = 56$. $D = \frac{16p}{56} = \frac{2p}{7}$. Need $7 | 2p$, so $7 | p$ (since $\gcd(7, 2) = 1$), so $p = 7$. Then $D = 2$. Check: $D < S = 7$ ✓. $\gcd(7, 2) = 1$ ✓. $t = 9$. $t | 2g^2 = 72$: $9 | 72$ ✓. $m = 10 - 6 = 4$. $m^2 = 16$. Check: $2 \cdot 36 \cdot 2 / 9 = 144/9 = 16$ ✓. $gt$ even: $6 \cdot 9 = 54$ even ✓.

So we have a solution! $g = 6$, $D = 2$, $S = 7$, $t = 9$, $m = 4$, $p = 7$.

$a = Sm = 7 \cdot 4 = 28$. $s = gS = 42$. $d = gD = 12$. $b = (s-d)/2 = 15$, $c = (s+d)/2 = 27$.

Triangle: $(a, b, c) = (28, 15, 27)$. Perimeter = $28 + 15 + 27 = 70 = 10 \cdot 7$ ✓.

Let me verify the angle bisector condition. $l_a^2 = bc(1 - a^2/(b+c)^2) = 15 \cdot 27 \cdot (1 - 784/1764) = 405 \cdot (980/1764) = 405 \cdot 245/441 = 405 \cdot 5/9 = 225$. So $l_a = 15 = b$ ✓.

$g=7$: $98 - 9 = 89$. $D = \frac{9p}{89}$. Need $89 | 9p$, so $89 | p$ (since $\gcd(89, 9) = 1$), so $p = 89$. $D = 9$. Check $D < S = 89$ ✓. $\gcd(89, 9) = 1$ ✓. $t = 98$. $t | 2g^2 = 98$: $98 | 98$ ✓. $m = 10 - 7 = 3$. $m^2 = 9$. Check: $2 \cdot 49 \cdot 9 / 98 = 882/98 = 9$ ✓. $gt$ even: $7 \cdot 98 = 686$ even ✓.

Solution! $g = 7$, $D = 9$, $S = 89$, $t = 98$, $m = 3$, $p = 89$.

$a = 89 \cdot 3 = 267$. $s = 7 \cdot 89 = 623$. $d = 7 \cdot 9 = 63$. $b = (623 - 63)/2 = 280$, $c = (623 + 63)/2 = 343$.

Triangle: $(267, 280, 343)$. Perimeter = $267 + 280 + 343 = 890 = 10 \cdot 89$ ✓.

Verify: $l_a^2 = 280 \cdot 343 \cdot (1 - 267^2/623^2)$. $267^2 = 71289$. $623^2 = 388129$. $1 - 71289/388129 = 316840/388129$. $280 \cdot 343 = 96040$. $l_a^2 = 96040 \cdot 316840 / 388129$. Let me check: $316840 / 388129$... $388129 = 623^2$. $316840 = 623^2 - 267^2 = (623-267)(623+267) = 356 \cdot 890$. So $l_a^2 = 96040 \cdot 356 \cdot 890 / 388129$. $96040 = 280 \cdot 343$. $388129 = 623^2$. $890 = 10 \cdot 89$. $356 = 4 \cdot 89$. So $l_a^2 = 280 \cdot 343 \cdot 4 \cdot 89 \cdot 10 \cdot 89 / 623^2 = 280 \cdot 343 \cdot 40 \cdot 89^2 / 623^2$. $623 = 7 \cdot 89$. $623^2 = 49 \cdot 89^2$. So $l_a^2 = 280 \cdot 343 \cdot 40 \cdot 89^2 / (49 \cdot 89^2) = 280 \cdot 343 \cdot 40 / 49 = 280 \cdot 7 \cdot 40 = 78400$. $l_a = 280 = b$ ✓.

$g=8$: $128 - 4 = 124$. $D = \frac{4p}{124} = \frac{p}{31}$. Need $31 | p$, so $p = 31$. $D = 1$. Check $D < S = 31$ ✓. $\gcd(31, 1) = 1$ ✓. $t = 32$. $t | 2g^2 = 128$: $32 | 128$ ✓. $m = 10 - 8 = 2$. $m^2 = 4$. Check: $2 \cdot 64 \cdot 1 / 32 = 128/32 = 4$ ✓. $gt$ even: $8 \cdot 32 = 256$ even ✓.

Solution! $g = 8$, $D = 1$, $S = 31$, $t = 32$, $m = 2$, $p = 31$.

$a = 31 \cdot 2 = 62$. $s = 8 \cdot 31 = 248$. $d = 8 \cdot 1 = 8$. $b = (248-8)/2 = 120$, $c = (248+8)/2 = 128$.

Triangle: $(62, 120, 128)$. Perimeter = $62 + 120 + 128 = 310 = 10 \cdot 31$ ✓.

Verify: $l_a^2 = 120 \cdot 128 \cdot (1 - 62^2/248^2)$. $62^2 = 3844$. $248^2 = 61504$. $3844/61504 = 3844/61504$. $\gcd(3844, 61504)$: $61504 / 3844 = 16$, so $3844 \cdot 16 = 61504$. So $1 - 1/16 = 15/16$. $l_a^2 = 120 \cdot 128 \cdot 15/16 = 120 \cdot 8 \cdot 15 = 14400$. $l_a = 120 = b$ ✓.

$g=9$: $162 - 1 = 161$. $D = \frac{p}{161}$. $161 = 7 \cdot 23$. Need $161 | p$, but $p$ is prime and $161$ is not prime. No solution.

So for Case $(S, m+g) = (p, 10)$, we get 3 solutions: $p = 7, 31, 89$.

**Case $(S, m+g) = (2p, 5)$:**
$S = 2p$, $D \in \{1, ..., 2p-1\}$ with $\gcd(2p, D) = 1$ (so $D$ odd and not a multiple of $p$).
$t = 2p + D$.
$m + g = 5$, $m = 5 - g$, $g \in \{1, 2, 3, 4\}$.
$t | 2g^2$.
$m^2 = 2g^2 D / t$.

$2g^2 \leq 32$, so $t \leq 32$, meaning $2p + D \leq 32$. Since $D \geq 1$, $2p \leq 31$, so $p \leq 15.5$, i.e., $p \in \{2, 3, 5, 7, 11, 13\}$ (primes up to 13).

$(5-g)^2 (2p + D) = 2g^2 D$
$(5-g)^2 \cdot 2p + (5-g)^2 D = 2g^2 D$
$(5-g)^2 \cdot 2p = D(2g^2 - (5-g)^2)$
$D = \frac{2p(5-g)^2}{2g^2 - (5-g)^2}$

$g=1$: $2 - 16 = -14$. Negative. No.
$g=2$: $8 - 9 = -1$. Negative. No.
$g=3$: $18 - 4 = 14$. $D = \frac{2p \cdot 4}{14} = \frac{4p}{7}$. Need $7 | 4p$, so $7 | p$, $p = 7$. $D = 4$. Check: $D < S = 14$ ✓. $\gcd(14, 4) = 2 \neq 1$. Fails! No solution.

$g=4$: $32 - 1 = 31$. $D = \frac{2p}{31}$. Need $31 | 2p$, so $p = 31$. But $p \leq 13$ from our bound. No solution.

No solutions for this case.

**Case $(S, m+g) = (5p, 2)$:**
$S = 5p$, $D \in \{1, ..., 5p-1\}$ with $\gcd(5p, D) = 1$.
$t = 5p + D$.
$m + g = 2$, so $m = 1, g = 1$.
$t | 2g^2 = 2$, so $t \in \{1, 2\}$. But $t = 5p + D \geq 5p + 1 \geq 11$. No solution.

Now I also need to handle $p = 2$ and $p = 5$ separately since they have different divisor structures.

**For $p = 2$:** $10p = 20 = 2^2 \cdot 5$. Divisors: $1, 2, 4, 5, 10, 20$.
$(S, m+g)$ with $S \geq 2$, $m+g \geq 2$: $(2, 10), (4, 5), (5, 4), (10, 2), (20, 1)$ [exclude last].

So $(S, m+g) \in \{(2, 10), (4, 5), (5, 4), (10, 2)\}$.

$(S, m+g) = (2, 10)$: $S=2, D=1, t=3$. $m+g=10$, $m=10-g$. $3|2g^2$ so $3|g$, $g=3j$. $m=10-3j$. $m^2 = 2 \cdot 9j^2/3 = 6j^2$. $(10-3j)^2 = 6j^2$, $100 - 60j + 9j^2 = 6j^2$, $3j^2 - 60j + 100 = 0$. Discriminant: $3600 - 1200 = 2400$. $\sqrt{2400} = 20\sqrt{6}$. Not rational. No.

$(S, m+g) = (4, 5)$: $S=4$, $D \in \{1, 3\}$ (coprime to 4). $t \in \{5, 7\}$. $m+g=5$, $m=5-g$, $g \in \{1,2,3,4\}$.

$D=1, t=5$: $5|2g^2$ so $5|g$, $g=5j$. But $g \leq 4$. No.
$D=3, t=7$: $7|2g^2$ so $7|g$, $g=7j$. But $g \leq 4$. No.

$(S, m+g) = (5, 4)$: $S=5$, $D \in \{1,2,3,4\}$. $t \in \{6,7,8,9\}$. $m+g=4$, $m=4-g$, $g \in \{1,2,3\}$.

$D=1, t=6$: $6|2g^2$ so $3|g$, $g=3$. $m=1$. $m^2=1$. Check: $2 \cdot 9 \cdot 1/6 = 3 \neq 1$. No.

Actually wait, let me redo. $m^2 = 2g^2 D/t = 2 \cdot 9 \cdot 1/6 = 3$. But $m = 1$, $m^2 = 1 \neq 3$. No.

$D=2, t=7$: $7|2g^2$ so $7|g$. $g \leq 3$. No.
$D=3, t=8$: $8|2g^2$ so $4|g^2$ so $2|g$. $g=2$. $m=2$. $m^2=4$. Check: $2 \cdot 4 \cdot 3/8 = 3 \neq 4$. No.
$D=4, t=9$: $9|2g^2$ so $3|g$. $g=3$. $m=1$. $m^2=1$. Check: $2 \cdot 9 \cdot 4/9 = 8 \neq 1$. No.

$(S, m+g) = (10, 2)$: $S=10$, $D \in \{1,3,7,9\}$. $t \in \{11,13,17,19\}$. $m+g=2$, $m=1, g=1$. $t|2g^2=2$, so $t \in \{1,2\}$. But $t \geq 11$. No.

No solutions for $p = 2$.

**For $p = 5$:** $10p = 50 = 2 \cdot 5^2$. Divisors: $1, 2, 5, 10, 25, 50$.
$(S, m+g)$ with $S \geq 2$, $m+g \geq 2$: $(2, 25), (5, 10), (10, 5), (25, 2), (50, 1)$ [exclude last].

$(S, m+g) = (2, 25)$: $S=2, D=1, t=3$. $m+g=25$, $m=25-g$. $3|g$, $g=3j$. $m=25-3j$. $m^2=6j^2$. $(25-3j)^2=6j^2$, $625-150j+9j^2=6j^2$, $3j^2-150j+625=0$. Discriminant: $22500-7500=15000$. $\sqrt{15000}=50\sqrt{6}$. Not rational. No.

$(S, m+g) = (5, 10)$: $S=5$, $D \in \{1,2,3,4\}$. $t \in \{6,7,8,9\}$. $m+g=10$, $m=10-g$, $g \in \{1,...,9\}$.

$D=1, t=6$: $6|2g^2$ so $3|g$, $g=3j$. $m=10-3j$. $m^2=2 \cdot 9j^2/6=3j^2$. $(10-3j)^2=3j^2$, $100-60j+9j^2=3j^2$, $6j^2-60j+100=0$, $3j^2-30j+50=0$. Discriminant: $900-600=300$. $\sqrt{300}=10\sqrt{3}$. Not rational. No.

$D=2, t=7$: $7|2g^2$ so $7|g$, $g=7j$. $m=10-7j$. $j=1$: $g=7, m=3$. $m^2=9$. Check: $2 \cdot 49 \cdot 2/7=28$. $9 \neq 28$. No.

$D=3, t=8$: $8|2g^2$ so $4|g^2$ so $2|g$, $g=2j$. $m=10-2j$. $m^2=2 \cdot 4j^2 \cdot 3/8=3j^2$. $(10-2j)^2=3j^2$, $100-40j+4j^2=3j^2$, $j^2-40j+100=0$. Discriminant: $1600-400=1200$. $\sqrt{1200}=20\sqrt{3}$. Not rational. No.

$D=4, t=9$: $9|2g^2$ so $3|g$, $g=3j$. $m=10-3j$. $m^2=2 \cdot 9j^2 \cdot 4/9=8j^2$. $(10-3j)^2=8j^2$, $100-60j+9j^2=8j^2$, $j^2-60j+100=0$. Discriminant: $3600-400=3200$. $\sqrt{3200}=40\sqrt{2}$. Not rational. No.

$(S, m+g) = (10, 5)$: $S=10$, $D \in \{1,3,7,9\}$. $t \in \{11,13,17,19\}$. $m+g=5$, $m=5-g$, $g \in \{1,2,3,4\}$.

$D=1, t=11$: $11|2g^2$ so $11|g$. $g \leq 4$. No.
$D=3, t=13$: $13|g$. No.
$D=7, t=17$: $17|g$. No.
$D=9, t=19$: $19|g$. No.

$(S, m+g) = (25, 2)$: $S=25$, $D \in \{1,...,24\}$, $\gcd(25, D)=1$ so $D$ not multiple of 5. $t=25+D$. $m+g=2$, $m=1, g=1$. $t|2$, so $t \leq 2$. But $t \geq 26$. No.

No solutions for $p = 5$.

Now let me also check: for general $p \neq 2, 5$, I considered cases $(S, m+g) \in \{(2, 5p), (5, 2p), (10, p), (p, 10), (2p, 5), (5p, 2)\}$.

I found solutions only in case $(S, m+g) = (p, 10)$: three solutions with $p = 7, 31, 89$.

Wait, but I should also check if there are solutions where $g_0 > 1$, i.e., the triangle is not primitive. Let me reconsider.

The perimeter is $g_0 \cdot \sigma = 10p$ where $\sigma = \alpha + \beta + \gamma$ is the primitive perimeter and $g_0 = \gcd(a, b, c)$.

In my parametrization, $g$ is $\gcd(s, d) = \gcd(b+c, c-b)$, which is not the same as $g_0 = \gcd(a, b, c)$.

Let me re-examine. I had $a = Sm$, $s = gS$, $d = gD$, so $b = g(S-D)/2$, $c = g(S+D)/2$, $a = Sm$.

$g_0 = \gcd(a, b, c) = \gcd(Sm, g(S-D)/2, g(S+D)/2)$.

The perimeter is $Sm + gS = S(m + g) = 10p$.

So the perimeter is directly $S(m+g)$, and I don't need to separately consider $g_0$. The parametrization already covers all triangles (not just primitive ones), because $g$ in the parametrization is $\gcd(s, d)$, not $\gcd(a, b, c)$.

Wait, but does the parametrization cover ALL integer triangles satisfying the condition? Let me verify.

Given any integer triangle with $l_a = b$, we have $a, b, c$ positive integers, $c > b$ (shown earlier), and $(c-b)(b+c)^2 = ca^2$. Setting $d = c - b$, $s = b + c$, $g = \gcd(s, d)$, $S = s/g$, $D = d/g$, we get the parametrization. And $a^2 = 2ds^2/(s+d) = 2gDS^2/(S+D) \cdot g^2/g = ... $ wait let me recheck.

$a^2 = \frac{2ds^2}{s+d} = \frac{2 \cdot gD \cdot g^2S^2}{g(S+D)} = \frac{2g^2 DS^2}{S+D}$.

With $t = S + D$ and $t | 2g^2$ (shown), $k = 2g^2/t$, $a^2 = kDS^2$, $a = S\sqrt{kD}$, $m = \sqrt{kD}$.

Yes, this covers all solutions. And the perimeter is $a + s = Sm + gS = S(m + g)$. So $S(m+g) = 10p$.

So I need to find all $(S, D, g, m)$ satisfying all the constraints with $S(m+g) = 10p$ for some prime $p$.

I've checked all factorizations of $10p$ for general $p \neq 2, 5$ and for $p = 2, 5$. Let me also verify I haven't missed any factorizations.

For $p \neq 2, 5$: $10p = 2 \cdot 5 \cdot p$. Divisors: $1, 2, 5, 10, p, 2p, 5p, 10p$. With $S \geq 2$ and $m+g \geq 2$:
- $S = 2, m+g = 5p$ ✓ (checked, no solution)
- $S = 5, m+g = 2p$ ✓ (checked, no solution)
- $S = 10, m+g = p$ ✓ (checked, no solution)
- $S = p, m+g = 10$ ✓ (checked, 3 solutions: $p = 7, 31, 89$)
- $S = 2p, m+g = 5$ ✓ (checked, no solution)
- $S = 5p, m+g = 2$ ✓ (checked, no solution)

For $p = 2$: $10p = 20$. Checked all, no solution.
For $p = 5$: $10p = 50$. Checked all, no solution.

So the total count is 3 triangles.

Wait, but I should double-check: are there other factorizations I might have missed? For $p \neq 2, 5$, the divisors of $10p$ are exactly $\{1, 2, 5, 10, p, 2p, 5p, 10p\}$. I've covered all pairs $(S, m+g)$ with $S \geq 2, m+g \geq 2$. Yes, I think that's complete.

But wait — I need to also make sure that within each case, I've found ALL valid $D$ values, not just some. Let me re-examine the case $(S, m+g) = (p, 10)$ more carefully.

In that case, $S = p$, $D$ ranges over $\{1, ..., p-1\}$ with $\gcd(p, D) = 1$ (automatic since $p$ is prime and $D < p$). We derived:

$D = \frac{(10-g)^2 p}{2g^2 - (10-g)^2}$

for $g \in \{1, ..., 9\}$, and we need $2g^2 - (10-g)^2 > 0$ and $D$ to be a positive integer with $D < p$ and $\gcd(p, D) = 1$.

I computed:
- $g=5$: $D = p$, but $D < p$ required. No.
- $g=6$: $D = 2p/7$, need $p = 7$, $D = 2$. ✓
- $g=7$: $D = 9p/89$, need $p = 89$, $D = 9$. ✓
- $g=8$: $D = p/31$, need $p = 31$, $D = 1$. ✓
- $g=9$: $D = p/161$, need $161 | p$, but $161 = 7 \cdot 23$ not prime. No.

For $g = 1, 2, 3, 4$: denominator negative, no solution.

So exactly 3 solutions. But wait, I need to also check the conditions $t | 2g^2$ and $gt$ even for each, which I did above and they all passed.

Let me also verify that $\gcd(S, D) = 1$ for each:
- $p=7, D=2$: $\gcd(7, 2) = 1$ ✓
- $p=31, D=1$: $\gcd(31, 1) = 1$ ✓
- $p=89, D=9$: $\gcd(89, 9) = 1$ ✓ (since 89 is prime and $9 < 89$)

And $D < S$:
- $2 < 7$ ✓
- $1 < 31$ ✓
- $9 < 89$ ✓

All good. So the answer is **3**.

But wait, I want to make sure I haven't missed solutions in the other cases due to not checking all subcases. Let me re-examine case $(S, m+g) = (2p, 5)$ more carefully.

$S = 2p$, $D$ odd, $D$ not multiple of $p$, $1 \leq D < 2p$. $m + g = 5$, $g \in \{1, 2, 3, 4\}$.

$D = \frac{2p(5-g)^2}{2g^2 - (5-g)^2}$

$g=3$: $D = \frac{2p \cdot 4}{14} = \frac{4p}{7}$. Need $7 | p$, $p = 7$. $D = 4$. But $\gcd(2p, D) = \gcd(14, 4) = 2 \neq 1$. Fails.

$g=4$: $D = \frac{2p}{31}$. Need $p = 31$. $D = 2$. But $D$ must be odd (since $\gcd(2p, D) = 1$ requires $D$ odd). $D = 2$ is even. Fails.

So no solutions. ✓

Let me also re-examine case $(S, m+g) = (5, 2p)$ for $p = 2$ and $p = 5$ (which I might have missed).

For $p = 2$: $(S, m+g) = (5, 4)$. Already checked above, no solution.
For $p = 5$: $(S, m+g) = (5, 10)$. Already checked, no solution.

And case $(S, m+g) = (10, p)$ for $p = 2$: $(10, 2)$. Already checked, no solution.
For $p = 5$: $(10, 5)$. Already checked, no solution.

And case $(S, m+g) = (2, 5p)$ for $p = 2$: $(2, 10)$. Checked, no solution.
For $p = 5$: $(2, 25)$. Checked, no solution.

And case $(S, m+g) = (5p, 2)$ for $p = 2$: $(10, 2)$. Checked, no solution.
For $p = 5$: $(25, 2)$. Checked, no solution.

And case $(S, m+g) = (2p, 5)$ for $p = 2$: $(4, 5)$. Checked, no solution.
For $p = 5$: $(10, 5)$. Checked, no solution.

And case $(S, m+g) = (p, 10)$ for $p = 2$: $(2, 10)$. Already covered in $(2, 10)$ case. No solution.
For $p = 5$: $(5, 10)$. Already covered. No solution.

I think I've been thorough. Let me also consider: for $p = 2$, the divisor 4 of 20 gives $(S, m+g) = (4, 5)$, which I checked. And $(S, m+g) = (5, 4)$, also checked.

For $p = 5$, the divisor 25 of 50 gives $(S, m+g) = (25, 2)$, checked. And $(S, m+g) = (2, 25)$, checked.

So the total number of integer triangles is **3**.

Actually, hold on. Let me reconsider whether I need to worry about the case $p = 2$ with the factorization $20 = 4 \times 5$. I had $S = 4, m+g = 5$. Let me recheck.

$S = 4$, $D \in \{1, 3\}$ (coprime to 4). $t \in \{5, 7\}$. $m + g = 5$, $g \in \{1, 2, 3, 4\}$.

$D = 1, t = 5$: $5 | 2g^2$ so $5 | g$. $g = 5$? No, $g \leq 4$. No solution.

Hmm wait, but I should use the formula: $D = \frac{(5-g)^2 \cdot 4}{2g^2 - (5-g)^2}$ (substituting $S = 4$ and $m+g = 5$, so $p$ is replaced by... wait, no. The formula was specific to $S = p$.

Let me redo this case from scratch. $S = 4$, $m + g = 5$, $m = 5 - g$.

$t = S + D = 4 + D$. $t | 2g^2$. $m^2 = 2g^2 D / t$.

$(5-g)^2 = 2g^2 D / (4 + D)$
$(5-g)^2 (4 + D) = 2g^2 D$
$4(5-g)^2 + (5-g)^2 D = 2g^2 D$
$4(5-g)^2 = D(2g^2 - (5-g)^2)$
$D = \frac{4(5-g)^2}{2g^2 - (5-g)^2}$

$g=1$: $D = 4 \cdot 16 / (2 - 16) = 64 / (-14)$. Negative. No.
$g=2$: $D = 4 \cdot 9 / (8 - 9) = 36 / (-1)$. Negative. No.
$g=3$: $D = 4 \cdot 4 / (18 - 4) = 16/14 = 8/7$. Not integer. No.
$g=4$: $D = 4 \cdot 1 / (32 - 1) = 4/31$. Not integer. No.

No solutions. ✓

OK so I'm now confident the answer is 3.

Let me also verify the three triangles are valid (satisfy triangle inequality):
1. $(28, 15, 27)$: $28 < 15 + 27 = 42$ ✓, $15 < 28 + 27 = 55$ ✓, $27 < 28 + 15 = 43$ ✓.
2. $(62, 120, 128)$: $62 < 248$ ✓, $120 < 190$ ✓, $128 < 182$ ✓.
3. $(267, 280, 343)$: $267 < 623$ ✓, $280 < 610$ ✓, $343 < 547$ ✓.

All valid. The answer is **3**.

Now let me write up the proof.
