# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Find the largest real number $k$ for which the inequality
$$(x+y+z)^2-81 \geq k(xy+yz+zx-27)$$
holds true for all $x, y, z > 0$ satisfying
$$xy + yz + zx = xyz.$$       — 题目文本
#   To find the largest real number \( k \) for which the inequality
\[
(x + y + z)^2 - 81 \geq k(xy + yz + zx - 27)
\]
holds true for all \( x, y, z > 0 \) satisfying \( xy + yz + zx = xyz \), we proceed as follows:

First, we consider the case where \( x = y \). The condition \( xy + yz + zx = xyz \) becomes:
\[
x^2 + 2xz = x^2 z \implies z = \frac{x}{x-2} \quad \text{for} \quad x > 2.
\]

Substituting \( x = y \) and \( z = \frac{x}{x-2} \) into the inequality, we need to verify:
\[
\left(2x + \frac{x}{x-2}\right)^2 - 81 \geq k \left( x^2 + 2x \cdot \frac{x}{x-2} - 27 \right).
\]

Simplifying the left-hand side:
\[
2x + \frac{x}{x-2} = \frac{2x(x-2) + x}{x-2} = \frac{2x^2 - 4x + x}{x-2} = \frac{2x^2 - 3x}{x-2}.
\]

Thus,
\[
\left( \frac{2x^2 - 3x}{x-2} \right)^2 - 81.
\]

Simplifying the right-hand side:
\[
x^2 + 2x \cdot \frac{x}{x-2} = x^2 + \frac{2x^2}{x-2} = \frac{x^2(x-2) + 2x^2}{x-2} = \frac{x^3 - 2x^2 + 2x^2}{x-2} = \frac{x^3}{x-2}.
\]

Thus,
\[
\frac{x^3}{x-2} - 27.
\]

The inequality becomes:
\[
\left( \frac{2x^2 - 3x}{x-2} \right)^2 - 81 \geq k \left( \frac{x^3}{x-2} - 27 \right).
\]

Define the function:
\[
f(x) = \frac{\left( \frac{2x^2 - 3x}{x-2} \right)^2 - 81}{\frac{x^3}{x-2} - 27}.
\]

Simplifying the numerator and denominator:
\[
\left( \frac{2x^2 - 3x}{x-2} \right)^2 - 81 = \frac{(2x^2 - 3x)^2 - 81(x-2)^2}{(x-2)^2},
\]
\[
\frac{x^3}{x-2} - 27 = \frac{x^3 - 27(x-2)}{x-2} = \frac{x^3 - 27x + 54}{x-2}.
\]

Thus,
\[
f(x) = \frac{(2x^2 - 3x)^2 - 81(x-2)^2}{(x-2)(x^3 - 27x + 54)}.
\]

Expanding and simplifying:
\[
(2x^2 - 3x)^2 = 4x^4 - 12x^3 + 9x^2,
\]
\[
81(x-2)^2 = 81x^2 - 324x + 324.
\]

Thus,
\[
(2x^2 - 3x)^2 - 81(x-2)^2 = 4x^4 - 12x^3 + 9x^2 - 81x^2 + 324x - 324 = 4x^4 - 12x^3 - 72x^2 + 324x - 324.
\]

Factoring:
\[
4x^4 - 12x^3 - 72x^2 + 324x - 324 = 4(x-3)^2(x^2 + 3x - 9).
\]

Thus,
\[
f(x) = \frac{4(x-3)^2(x^2 + 3x - 9)}{(x-2)(x^3 - 27x + 54)}.
\]

Simplifying further:
\[
x^3 - 27x + 54 = (x-3)(x^2 + 3x - 18).
\]

Thus,
\[
f(x) = \frac{4(x-3)^2(x^2 + 3x - 9)}{(x-2)(x-3)(x^2 + 3x - 18)} = \frac{4(x-3)(x^2 + 3x - 9)}{(x-2)(x^2 + 3x - 18)}.
\]

Evaluating the limit as \( x \to 3 \):
\[
\lim_{x \to 3} f(x) = \frac{4(0)(9 + 9 - 9)}{(1)(9 + 9 - 18)} = \frac{0}{0}.
\]

Using L'Hôpital's Rule:
\[
\lim_{x \to 3} \frac{4(x-3)(x^2 + 3x - 9)}{(x-2)(x^2 + 3x - 18)} = \frac{4(3x^2 - 18)}{(x^2 + 3x - 18) + (x-2)(2x + 3)} = \frac{4(27 - 18)}{9 + 9 - 18 + 1(6 + 3)} = \frac{36}{9} = 4.
\]

Thus, the minimum value of \( f(x) \) is \( \frac{15}{4} \).

Therefore, the largest real number \( k \) is:
\[
\boxed{\frac{15}{4}}.
\]  — 标准解答
#   Let me solve this problem. The constraint says don't use any tools, just think and output the proof in TUI.

Problem: Find the largest real number $k$ such that $(x+y+z)^2 - 81 \geq k(xy+yz+zx-27)$ for all $x,y,z > 0$ with $xy+yz+zx = xyz$.

First, let me check for answer leaks. The problem text doesn't contain any solution or answer. Good.

Let me solve. The constraint is $xy+yz+zx = xyz$. Dividing by $xyz$: $1/x + 1/y + 1/z = 1$.

Let $a = 1/x, b = 1/y, c = 1/z$ with $a,b,c > 0$ and $a+b+c = 1$.

We need $(x+y+z)^2 - 81 \geq k(xy+yz+zx - 27)$.

Note $xy+yz+zx = xyz$, so $xy+yz+zx - 27 = xyz - 27$.

Hmm, let me think about the equality case. By symmetry, likely $x=y=z$. If $x=y=z$, then $3x^2 = x^3$, so $x=3$. Then $x+y+z = 9$, $(x+y+z)^2 = 81$, and $xy+yz+zx = 27$. So both sides are 0 at $x=y=z=3$. This is the equality point where both sides vanish.

So we need to find the largest $k$ such that $(x+y+z)^2 - 81 \geq k(xy+yz+zx - 27)$ for all valid $(x,y,z)$.

Since at $(3,3,3)$ both sides are 0, this is like finding the infimum of the ratio $\frac{(x+y+z)^2 - 81}{xy+yz+zx - 27}$ over the constraint set (where denominator is positive, or handling sign).

Wait, we need the inequality to hold for ALL $x,y,z>0$ with the constraint. The denominator $xy+yz+zx - 27 = xyz - 27$ can be positive or negative.

Let me think. Let $s = x+y+z$, $p = xy+yz+zx = xyz$, $q = xyz = p$ (since $p = q$ on constraint).

Actually $xy+yz+zx = xyz$, so $p = q$ where $p = xy+yz+zx$, $q=xyz$.

The inequality: $s^2 - 81 \geq k(p - 27)$.

At $(3,3,3)$: $s=9, p=27$, both sides 0.

We want the largest $k$ such that $s^2 - 81 \geq k(p-27)$ always.

If $p > 27$ (i.e., $p - 27 > 0$), we need $k \leq \frac{s^2-81}{p-27}$.
If $p < 27$ (i.e., $p - 27 < 0$), we need $k \geq \frac{s^2-81}{p-27}$.

So $k$ must be $\leq$ the infimum of $\frac{s^2-81}{p-27}$ over $p>27$ region, AND $\geq$ the supremum over $p<27$ region.

For the largest $k$, we want $k = \inf_{p>27} \frac{s^2-81}{p-27}$, and we need this to be $\geq \sup_{p<27} \frac{s^2-81}{p-27}$.

Let me compute the ratio near $(3,3,3)$ using Lagrange / Taylor expansion to find the limiting value.

Let's parametrize. Use $a = 1/x, b=1/y, c=1/z$, $a+b+c=1$, $a,b,c>0$.

Then $x = 1/a$ etc. $s = 1/a + 1/b + 1/c$. $p = xy+yz+zx = 1/(ab) + 1/(bc) + 1/(ca) = (a+b+c)/(abc) = 1/(abc)$.

So $p = 1/(abc)$, $s = (ab+bc+ca)/(abc) = (ab+bc+ca) \cdot p$... wait let me recompute. $s = 1/a+1/b+1/c = (bc+ac+ab)/(abc)$. And $p = 1/(abc)$. So $s = (ab+bc+ca) \cdot p$? No: $s = (ab+bc+ca)/(abc) = (ab+bc+ca) \cdot p$. Yes since $p = 1/(abc)$.

Let $u = ab+bc+ca$, $v = abc$. Then $p = 1/v$, $s = u/v = u \cdot p$.

At $(3,3,3)$: $a=b=c=1/3$, $u = 3 \cdot 1/9 = 1/3$, $v = 1/27$, $p = 27$, $s = (1/3)/(1/27) = 9$. Good.

Inequality: $s^2 - 81 \geq k(p - 27)$, i.e., $(u/v)^2 - 81 \geq k(1/v - 27)$.

Multiply by $v^2 > 0$: $u^2 - 81 v^2 \geq k(v - 27 v^2) = kv(1 - 27v)$.

So $u^2 - 81v^2 \geq kv(1-27v)$.

At $(1/3,1/3,1/3)$: $u=1/3, v=1/27$. $u^2 = 1/9$, $81v^2 = 81/729 = 1/9$. LHS = 0. RHS: $kv(1-27v) = k \cdot (1/27)(1-1) = 0$. Good.

Now we need this for all $a,b,c>0$, $a+b+c=1$.

We have $u = ab+bc+ca$, $v = abc$ with $a+b+c=1$.

The constraint region: $a,b,c > 0$, sum 1. The range of $v = abc$: by AM-GM, $v \leq (1/3)^3 = 1/27$, with equality at $a=b=c=1/3$. And $v \to 0$ at boundary. So $v \in (0, 1/27]$.

When $v < 1/27$, $1 - 27v > 0$, so RHS $= kv(1-27v)$, sign depends on $k$.
When $v = 1/27$, RHS = 0.

Hmm, this is getting complex. Let me think about the limiting ratio as we approach $(3,3,3)$.

Consider perturbations. Let $a = 1/3 + \alpha$, $b = 1/3 + \beta$, $c = 1/3 + \gamma$ with $\alpha+\beta+\gamma = 0$ (to maintain sum 1).

$u = ab+bc+ca = (a+b+c)^2/2 - (a^2+b^2+c^2)/2 \cdot ... $ actually $u = ((a+b+c)^2 - (a^2+b^2+c^2))/2 = (1 - (a^2+b^2+c^2))/2$.

$a^2+b^2+c^2 = 3(1/9) + 2(1/3)(\alpha+\beta+\gamma) + (\alpha^2+\beta^2+\gamma^2) = 1/3 + 0 + (\alpha^2+\beta^2+\gamma^2)$.

So $u = (1 - 1/3 - (\alpha^2+\beta^2+\gamma^2))/2 = (2/3 - S_2)/2 = 1/3 - S_2/2$ where $S_2 = \alpha^2+\beta^2+\gamma^2$.

$v = abc = (1/3+\alpha)(1/3+\beta)(1/3+\gamma)$. 
$= 1/27 + (1/9)(\alpha+\beta+\gamma) + (1/3)(\alpha\beta+\beta\gamma+\gamma\alpha) + \alpha\beta\gamma$
$= 1/27 + 0 + (1/3)(\alpha\beta+\beta\gamma+\gamma\alpha) + \alpha\beta\gamma$.

Now $\alpha+\beta+\gamma=0$ implies $\alpha\beta+\beta\gamma+\gamma\alpha = -S_2/2$.

So $v = 1/27 - S_2/6 + \alpha\beta\gamma$.

Let $S_3 = \alpha\beta\gamma$. So $v = 1/27 - S_2/6 + S_3$.

Now compute $u^2 - 81v^2$:
$u = 1/3 - S_2/2$, $u^2 = 1/9 - S_2/3 + S_2^2/4$.
$v = 1/27 - S_2/6 + S_3$, $v^2 = 1/729 - (1/27)(S_2/3 - S_3)\cdot 2$... let me be careful.

$v^2 = (1/27)^2 - 2(1/27)(S_2/6 - S_3) + (S_2/6 - S_3)^2$
$= 1/729 - (1/27)(S_2/3 - 2S_3) + (S_2/6 - S_3)^2$
$= 1/729 - S_2/81 + 2S_3/27 + (S_2/6 - S_3)^2$.

$81 v^2 = 81/729 - 81 \cdot S_2/81 + 81 \cdot 2S_3/27 + 81(S_2/6-S_3)^2$
$= 1/9 - S_2 + 6S_3 + 81(S_2/6 - S_3)^2$.

$u^2 - 81v^2 = (1/9 - S_2/3 + S_2^2/4) - (1/9 - S_2 + 6S_3 + 81(S_2/6-S_3)^2)$
$= -S_2/3 + S_2 + S_2^2/4 - 6S_3 - 81(S_2/6-S_3)^2$
$= 2S_2/3 + S_2^2/4 - 6S_3 - 81(S_2/6-S_3)^2$.

Now RHS: $kv(1-27v)$. $v = 1/27 - S_2/6 + S_3$. $27v = 1 - 27S_2/6 + 27S_3 = 1 - 9S_2/2 + 27S_3$. $1 - 27v = 9S_2/2 - 27S_3$.

$v(1-27v) = (1/27 - S_2/6 + S_3)(9S_2/2 - 27S_3)$.

Leading order (order $S_2$): $(1/27)(9S_2/2) = S_2/6$.

So RHS $\approx k \cdot S_2/6$ at leading order.

LHS leading order: $2S_2/3$ (the $-6S_3$ is order... $S_3$ is cubic in perturbation, $S_2$ is quadratic, so $S_3$ is higher order than $S_2$). Actually $S_2 \sim \epsilon^2$, $S_3 \sim \epsilon^3$. So leading order of LHS is $2S_2/3$.

So at leading order: $2S_2/3 \geq k S_2/6$, giving $k \leq 4$.

So the candidate is $k = 4$. Let me verify this works and is tight.

We need to show $(x+y+z)^2 - 81 \geq 4(xy+yz+zx - 27)$ for all $x,y,z>0$ with $xy+yz+zx=xyz$.

$(x+y+z)^2 - 81 - 4(xy+yz+zx - 27) = x^2+y^2+z^2 + 2(xy+yz+zx) - 81 - 4(xy+yz+zx) + 108$
$= x^2+y^2+z^2 - 2(xy+yz+zx) + 27$
$= (x+y+z)^2 - 4(xy+yz+zx) + 27$... wait let me recompute.

$x^2+y^2+z^2 - 2(xy+yz+zx) + 27$.

Hmm, $x^2+y^2+z^2 - 2(xy+yz+zx) = (x+y+z)^2 - 4(xy+yz+zx)$. Actually $(x+y+z)^2 = x^2+y^2+z^2 + 2(xy+yz+zx)$, so $x^2+y^2+z^2 - 2(xy+yz+zx) = (x+y+z)^2 - 4(xy+yz+zx)$.

So we need to show $x^2+y^2+z^2 - 2(xy+yz+zx) + 27 \geq 0$, i.e., $(x+y+z)^2 - 4(xy+yz+zx) + 27 \geq 0$.

Note $x^2+y^2+z^2 - 2(xy+yz+zx) = (x-y-z)^2 - 4yz$... hmm, or $= (x-y)^2 + (y-z)^2 + (z-x)^2)/... $ no. Actually $x^2+y^2+z^2 - xy - yz - zx = \frac{1}{2}((x-y)^2+(y-z)^2+(z-x)^2)$. So $x^2+y^2+z^2 - 2(xy+yz+zx) = (x^2+y^2+z^2 - xy-yz-zx) - (xy+yz+zx) = \frac{1}{2}\sum(x-y)^2 - (xy+yz+zx)$.

So we need $\frac{1}{2}\sum(x-y)^2 - (xy+yz+zx) + 27 \geq 0$, i.e., $\frac{1}{2}\sum(x-y)^2 + 27 \geq xy+yz+zx = xyz$.

So we need to prove: $xyz \leq 27 + \frac{1}{2}((x-y)^2+(y-z)^2+(z-x)^2)$ given $xy+yz+zx = xyz$, $x,y,z>0$.

Equivalently, $xyz - 27 \leq \frac{1}{2}\sum(x-y)^2$.

Hmm, let me use the $a,b,c$ substitution. $a+b+c=1$, $a,b,c>0$, $x=1/a, y=1/b, z=1/c$.

$xy+yz+zx = xyz$ is automatic. We need to show $x^2+y^2+z^2 - 2(xy+yz+zx) + 27 \geq 0$.

$x^2+y^2+z^2 = 1/a^2 + 1/b^2 + 1/c^2$.
$xy+yz+zx = 1/(ab)+1/(bc)+1/(ca) = (a+b+c)/(abc) = 1/(abc) = 1/v$.

Hmm wait, that's $p = 1/v$. And $x^2+y^2+z^2 = (b^2c^2 + a^2c^2 + a^2b^2)/(a^2b^2c^2) = (u^2 - 2v\cdot 1)/(v^2)$... 

Actually $(ab+bc+ca)^2 = a^2b^2+b^2c^2+c^2a^2 + 2abc(a+b+c) = a^2b^2+b^2c^2+c^2a^2 + 2v$. So $a^2b^2+b^2c^2+c^2a^2 = u^2 - 2v$.

$x^2+y^2+z^2 = (a^2b^2+b^2c^2+c^2a^2)/v^2 = (u^2-2v)/v^2$.

$xy+yz+zx = u/v$ (since $= (a+b+c)/(abc) = 1/v$... wait. $xy = 1/(ab)$, $xy+yz+zx = 1/(ab)+1/(bc)+1/(ca) = (c+a+b)/(abc) = 1/v$. Yes $p = 1/v$.)

Hmm, I said $p = 1/v$ and also $s = u/v$. Let me recheck: $s = x+y+z = 1/a+1/b+1/c = (bc+ac+ab)/(abc) = u/v$. Yes.

So $x^2+y^2+z^2 = s^2 - 2p = u^2/v^2 - 2/v$.

The expression $x^2+y^2+z^2 - 2(xy+yz+zx) + 27 = (u^2/v^2 - 2/v) - 2/v + 27 = u^2/v^2 - 4/v + 27$.

$= (u^2 - 4v + 27v^2)/v^2$.

So we need $u^2 - 4v + 27v^2 \geq 0$ where $u = ab+bc+ca$, $v = abc$, $a+b+c=1$, $a,b,c>0$.

We need to prove $u^2 + 27v^2 \geq 4v$.

Recall $u \geq 3v^{2/3}$... by AM-GM on $ab, bc, ca$: $u = ab+bc+ca \geq 3(abc)^{2/3} = 3v^{2/3}$.

So $u^2 \geq 9v^{4/3}$. We need $9v^{4/3} + 27v^2 \geq 4v$, i.e., $9v^{1/3} + 27v \geq 4$ (dividing by $v > 0$, since $v = abc > 0$... wait $v^{4/3}/v = v^{1/3}$, $v^2/v = v$, $4v/v = 4$). So $9v^{1/3} + 27v \geq 4$.

But $v \leq 1/27$, so $v^{1/3} \leq 1/3$, $9v^{1/3} \leq 3$, $27v \leq 1$. So $9v^{1/3} + 27v \leq 4$ with equality at $v = 1/27$.

So this approach gives $9v^{1/3}+27v \leq 4$, the wrong direction! The AM-GM bound $u^2 \geq 9v^{4/3}$ is too weak (it's an equality only at $a=b=c$, and we need the inequality to go the other way).

So I can't just use $u \geq 3v^{2/3}$. I need a sharper relationship between $u$ and $v$ given $a+b+c=1$.

Let me reconsider. We need $u^2 + 27v^2 \geq 4v$ for $a+b+c=1$, $a,b,c>0$.

This is a known type. Let me think about it as: for fixed $v$, what's the minimum of $u$? Given $a+b+c=1$ and $abc = v$, the minimum of $u = ab+bc+ca$... 

Actually, given $a+b+c = 1$ and $abc = v$, $u$ ranges in some interval. By Schur or uvw, the extremal values of $u$ for fixed sum and product occur when two variables are equal.

Let me use the uvw method. The inequality $u^2 + 27v^2 - 4v \geq 0$ is symmetric in $a,b,c$. By uvw, it suffices to check when two variables are equal.

Set $b = c = t$, $a = 1 - 2t$, with $0 < t < 1/2$ (and $a > 0$ means $t < 1/2$).

$u = ab + bc + ca = 2at + t^2 = 2(1-2t)t + t^2 = 2t - 4t^2 + t^2 = 2t - 3t^2$.
$v = abc = (1-2t)t^2 = t^2 - 2t^3$.

$u^2 = (2t-3t^2)^2 = 4t^2 - 12t^3 + 9t^4$.
$27v^2 = 27(t^2-2t^3)^2 = 27(t^4 - 4t^5 + 4t^6) = 27t^4 - 108t^5 + 108t^6$.
$4v = 4t^2 - 8t^3$.

$u^2 + 27v^2 - 4v = 4t^2 - 12t^3 + 9t^4 + 27t^4 - 108t^5 + 108t^6 - 4t^2 + 8t^3$
$= -4t^3 + 36t^4 - 108t^5 + 108t^6$
$= -4t^3(1 - 9t + 27t^2 - 27t^3)$
$= -4t^3(1 - 3t)^3$.

Now $(1-3t)^3$: when $t < 1/3$, $(1-3t)^3 > 0$, so $-4t^3(1-3t)^3 < 0$. That's negative!

Wait, that means $u^2 + 27v^2 - 4v < 0$ for $t \in (0, 1/3)$? That would mean $k=4$ doesn't work!

Let me double check. At $t = 1/3$, $a = 1/3$, all equal, expression $= 0$. For $t$ slightly less than $1/3$, say $t = 0.3$, $a = 0.4$.

$u = 2(0.3) - 3(0.09) = 0.6 - 0.27 = 0.33$.
$v = 0.09 - 2(0.027) = 0.09 - 0.054 = 0.036$.
$u^2 = 0.1089$.
$27v^2 = 27(0.001296) = 0.034992$.
$4v = 0.144$.
$u^2 + 27v^2 - 4v = 0.1089 + 0.034992 - 0.144 = -0.000108 < 0$.

So indeed negative! So $k = 4$ does NOT work. My leading-order analysis was wrong, or the answer is less than 4.

Wait, let me recheck the leading order. The issue is that the leading order $2S_2/3$ vs $k S_2/6$ gives $k \leq 4$, but the next order terms matter. Let me recompute more carefully.

Actually, the leading order gives $k \leq 4$ as necessary, but it might not be sufficient. The actual answer could be smaller. Let me reconsider.

Hmm wait, actually the leading order analysis: LHS $\approx 2S_2/3$, RHS $\approx k S_2/6$. For the inequality LHS $\geq$ RHS near the point, we need $2S_2/3 \geq k S_2/6$, i.e., $k \leq 4$. But this is only necessary (the ratio approaches 4 from some direction). The actual infimum of the ratio over all points might be less than 4.

But wait, the computation above shows that for $k=4$, the expression $u^2 + 27v^2 - 4v$ can be negative, meaning $(x+y+z)^2 - 81 - 4(p - 27) < 0$, i.e., the inequality fails. So $k = 4$ is too big.

Let me recompute the ratio for the two-equal case to find the actual infimum.

For $b = c = t$, $a = 1-2t$:
- $s = u/v = (2t-3t^2)/(t^2-2t^3) = (2-3t)/(t(1-2t)) \cdot ... $ let me compute: $s = u/v = (2t-3t^2)/(t^2-2t^3) = t(2-3t)/(t^2(1-2t)) = (2-3t)/(t(1-2t))$.
- $p = 1/v = 1/(t^2(1-2t))$.

Ratio $R = (s^2 - 81)/(p - 27) = (u^2/v^2 - 81)/(1/v - 27) = (u^2 - 81v^2)/(v - 27v^2) = (u^2 - 81v^2)/(v(1-27v))$.

We computed $u^2 - 81v^2 = 2S_2/3 + ...$ earlier in terms of perturbation. Let me just compute directly for two-equal.

$u^2 - 81v^2$: 
$u^2 = 4t^2 - 12t^3 + 9t^4$.
$81v^2 = 81(t^2 - 2t^3)^2 = 81(t^4 - 4t^5 + 4t^6) = 81t^4 - 324t^5 + 324t^6$.
$u^2 - 81v^2 = 4t^2 - 12t^3 + 9t^4 - 81t^4 + 324t^5 - 324t^6 = 4t^2 - 12t^3 - 72t^4 + 324t^5 - 324t^6$.
$= 4t^2(1 - 3t - 18t^2 + 81t^3 - 81t^4)$.

$v(1-27v) = (t^2-2t^3)(1 - 27(t^2-2t^3)) = (t^2-2t^3)(1 - 27t^2 + 54t^3)$.
$= t^2(1-2t)(1 - 27t^2 + 54t^3)$.

$R = \frac{4t^2(1 - 3t - 18t^2 + 81t^3 - 81t^4)}{t^2(1-2t)(1 - 27t^2 + 54t^3)}$
$= \frac{4(1 - 3t - 18t^2 + 81t^3 - 81t^4)}{(1-2t)(1 - 27t^2 + 54t^3)}$.

Let me factor. At $t = 1/3$, both numerator and denominator vanish. Let me factor out $(1-3t)$.

Numerator: $f(t) = 1 - 3t - 18t^2 + 81t^3 - 81t^4$. $f(1/3) = 1 - 1 - 2 + 3 - 1 = 0$. Good.
$f'(t) = -3 - 36t + 243t^2 - 324t^3$. $f'(1/3) = -3 - 12 + 27 - 12 = 0$. So $(1-3t)^2$ divides.
$f''(t) = -36 + 486t - 972t^2$. $f''(1/3) = -36 + 162 - 108 = 18 \neq 0$. So $(1-3t)^2$ exactly (order 2).

Let me do polynomial division. $f(t) = -81t^4 + 81t^3 - 18t^2 - 3t + 1$.

Divide by $(1-3t)^2 = 1 - 6t + 9t^2$.

$-81t^4 + 81t^3 - 18t^2 - 3t + 1 = (1 - 6t + 9t^2) \cdot q(t)$.

Let $q(t) = at^2 + bt + c$. $(1-6t+9t^2)(at^2+bt+c) = 9at^4 + (9b-6a)t^3 + (9c - 6b + a)t^2 + (-6c + b)t + c$.

Match:
- $t^4$: $9a = -81 \Rightarrow a = -9$.
- $t^3$: $9b - 6a = 81 \Rightarrow 9b + 54 = 81 \Rightarrow 9b = 27 \Rightarrow b = 3$.
- $t^2$: $9c - 6b + a = -18 \Rightarrow 9c - 18 - 9 = -18 \Rightarrow 9c = 9 \Rightarrow c = 1$.
- $t^1$: $-6c + b = -6 + 3 = -3$. ✓
- $t^0$: $c = 1$. ✓

So $f(t) = (1-3t)^2(1 + 3t - 9t^2)$.

Denominator: $g(t) = (1-2t)(1 - 27t^2 + 54t^3)$. At $t=1/3$: $(1-2/3)(1 - 3 + 2) = (1/3)(0) = 0$. So $(1-3t)$ divides $1 - 27t^2 + 54t^3$.

$1 - 27t^2 + 54t^3$: at $t=1/3$, $1 - 3 + 2 = 0$. Divide by $(1-3t)$: $54t^3 - 27t^2 + 1 = (1-3t)(\text{quadratic})$. 

$54t^3 - 27t^2 + 0t + 1$. Divide by $-3t+1$... let me use $(1-3t)$. 

$(1-3t)(At^2 + Bt + C) = -3At^3 + (A - 3B)t^2 + (B - 3C)t + C$.
Match: $-3A = 54 \Rightarrow A = -18$. $A - 3B = -27 \Rightarrow -18 - 3B = -27 \Rightarrow -3B = -9 \Rightarrow B = 3$. $B - 3C = 0 \Rightarrow 3 - 3C = 0 \Rightarrow C = 1$. $C = 1$ ✓.

So $1 - 27t^2 + 54t^3 = (1-3t)(1 + 3t - 18t^2)$.

$g(t) = (1-2t)(1-3t)(1 + 3t - 18t^2)$.

So $R = \frac{4(1-3t)^2(1+3t-9t^2)}{(1-2t)(1-3t)(1+3t-18t^2)} = \frac{4(1-3t)(1+3t-9t^2)}{(1-2t)(1+3t-18t^2)}$.

At $t = 1/3$: $R = \frac{4 \cdot 0 \cdot (...)}{...} = 0/(\text{nonzero})$. Wait, $(1-3t) \to 0$, so $R \to 0$? That can't be right; the ratio should approach 4.

Hmm, let me recheck. At $t = 1/3$, $s = 9$, $p = 27$, so both numerator and denominator of original ratio are 0. The limit should be 4 (from leading order). But my factored form gives $R \to 0$?

Let me recheck the factorization. Oh wait, I think I need to check: is $t = 1/3$ giving $a = 1 - 2/3 = 1/3$, so $a = b = c = 1/3$, yes the symmetric point.

$R = \frac{4(1-3t)(1+3t-9t^2)}{(1-2t)(1+3t-18t^2)}$.

At $t = 1/3$: numerator has factor $(1 - 1) = 0$. Denominator: $(1 - 2/3)(1 + 1 - 2) = (1/3)(0) = 0$. So both 0! I need to check $1 + 3t - 18t^2$ at $t = 1/3$: $1 + 1 - 18/9 = 2 - 2 = 0$. So denominator also has $(1-3t)$ factor!

$1 + 3t - 18t^2$ at $t = 1/3$: $1 + 1 - 2 = 0$. Yes. So factor: $-18t^2 + 3t + 1 = (1-3t)(\text{linear})$. $-18t^2 + 3t + 1 = -(18t^2 - 3t - 1) = -(3t-1)(6t+1) = (1-3t)(6t+1)$.

Check: $(1-3t)(6t+1) = 6t + 1 - 18t^2 - 3t = 1 + 3t - 18t^2$. ✓.

So $g(t) = (1-2t)(1-3t)(1-3t)(6t+1) = (1-2t)(1-3t)^2(6t+1)$.

$R = \frac{4(1-3t)^2(1+3t-9t^2)}{(1-2t)(1-3t)^2(6t+1)} = \frac{4(1+3t-9t^2)}{(1-2t)(6t+1)}$.

At $t = 1/3$: $\frac{4(1 + 1 - 1)}{(1/3)(3)} = \frac{4 \cdot 1}{1} = 4$. ✓ 

So $R(t) = \frac{4(1+3t-9t^2)}{(1-2t)(6t+1)}$ for $t \in (0, 1/2)$, $t \neq 1/3$ (and $R(1/3) = 4$ by limit).

Now I need to find the infimum of $R(t)$ over $t \in (0, 1/2)$ (this gives the ratio for two-equal case; by uvw, the global infimum of the ratio is achieved in the two-equal case or at boundary).

Wait, but I need to be careful about the sign of the denominator $p - 27 = 1/v - 27 = (1 - 27v)/v$. $v = t^2(1-2t)$. $27v = 27t^2(1-2t)$. $1 - 27v = 1 - 27t^2 + 54t^3 = (1-3t)^2(6t+1) \cdot ... $ wait we had $1 - 27t^2 + 54t^3 = (1-3t)(1+3t-18t^2) = (1-3t)^2(6t+1)$. 

So $1 - 27v = (1-3t)^2(6t+1) \geq 0$ always! With equality only at $t = 1/3$.

So $p - 27 \geq 0$ always (since $v \leq 1/27$ by AM-GM, $p = 1/v \geq 27$). So the denominator $p - 27 \geq 0$ always, and $= 0$ only at the symmetric point.

So we only need $k \leq \inf R$ over the constraint set (excluding the symmetric point where it's $0/0$, taking limit).

And also $s^2 - 81 \geq 0$? $s = x+y+z \geq 9$ by AM-GM? $x+y+z$ with $1/x+1/y+1/z = 1$... By AM-HM or Cauchy-Schwarz: $(x+y+z)(1/x+1/y+1/z) \geq 9$, so $x+y+z \geq 9$. So $s^2 - 81 \geq 0$. Good, both nonneg, ratio well-defined and $\geq 0$.

So we need $k = \inf R$ over the domain. By uvw, the infimum is achieved in the two-equal case (or at boundary). Let me find $\inf R(t)$ for $t \in (0, 1/2)$.

$R(t) = \frac{4(1+3t-9t^2)}{(1-2t)(6t+1)}$.

Let me find the minimum. Let $N = 1 + 3t - 9t^2$, $D = (1-2t)(6t+1) = 6t + 1 - 12t^2 - 2t = 1 + 4t - 12t^2$.

$R = 4N/D$. $R' = 4(N'D - ND')/D^2$.

$N' = 3 - 18t$. $D' = 4 - 24t$.

$N'D - ND' = (3-18t)(1+4t-12t^2) - (1+3t-9t^2)(4-24t)$.

$(3-18t)(1+4t-12t^2) = 3 + 12t - 36t^2 - 18t - 72t^2 + 216t^3 = 3 - 6t - 108t^2 + 216t^3$.

$(1+3t-9t^2)(4-24t) = 4 - 24t + 12t - 72t^2 - 36t^2 + 216t^3 = 4 - 12t - 108t^2 + 216t^3$.

$N'D - ND' = (3 - 6t - 108t^2 + 216t^3) - (4 - 12t - 108t^2 + 216t^3) = 3 - 6t - 4 + 12t = -1 + 6t$.

So $R' = 0 \iff 6t - 1 = 0 \iff t = 1/6$.

At $t = 1/6$: $N = 1 + 1/2 - 9/36 = 1 + 0.5 - 0.25 = 1.25 = 5/4$. $D = 1 + 4/6 - 12/36 = 1 + 2/3 - 1/3 = 1 + 1/3 = 4/3$. $R = 4 \cdot (5/4)/(4/3) = 5/(4/3) = 15/4 = 3.75$.

Check boundaries: $t \to 0^+$: $N \to 1$, $D \to 1$, $R \to 4$. $t \to 1/2^-$: $N = 1 + 3/2 - 9/4 = 1 + 1.5 - 2.25 = 0.25$, $D = (1-1)(...) = 0$, $D \to 0^+$, $R \to +\infty$.

So $R$ has a minimum at $t = 1/6$ with $R = 15/4$, and $R \to 4$ at $t \to 0$, and $R \to \infty$ at $t \to 1/2$.

Wait, but at $t = 1/6$, is this a minimum? $R' = 4(6t-1)/D^2$. For $t < 1/6$, $R' < 0$ (decreasing). For $t > 1/6$, $R' > 0$ (increasing). So yes, $t = 1/6$ is a minimum with value $15/4$.

But wait, I should check: is the infimum over ALL $(a,b,c)$ achieved at two-equal? By uvw method, for a symmetric inequality, the extremum of a symmetric function under symmetric constraints is achieved when two variables are equal. But here the function $R$ is a ratio, not a polynomial. Let me think more carefully.

Actually, the uvw method says: for a symmetric inequality $f(a,b,c) \geq 0$ where $f$ is a polynomial (or rational function that can be converted), with fixed $a+b+c$, the inequality holds for all iff it holds when two variables are equal. 

The inequality we want to verify is $u^2 + 27v^2 \geq kv$ (for the right $k$), i.e., $u^2 + 27v^2 - kv \geq 0$, with $a+b+c = 1$. This is symmetric and the LHS is a polynomial in $u, v$ (with $u, v$ being the elementary symmetric polynomials). By uvw, since the degree in $v$ is 2 (the $v^2$ term), and... actually uvw says: a symmetric inequality of degree $d$ in variables, expressed in terms of $u, v$ (with $s = a+b+c$ fixed), where the expression is at most quadratic in $v$ (or $u$), then it suffices to check two-equal case.

Here $u^2 + 27v^2 - kv$: as a function of $v$ it's quadratic (degree 2 in $v$), and as function of $u$ it's quadratic. The uvw method: if the inequality is at most degree 2 in $v$ (treating $u$ as the "middle" variable), then it suffices to check boundary (two equal). Actually, let me recall: uvw says if $f$ is at most quadratic in $w$ (the third symmetric polynomial, here $v = abc$), then the inequality $f \geq 0$ need only be checked when two variables are equal or one is zero.

So for $k = 15/4$, we need $u^2 + 27v^2 - \frac{15}{4}v \geq 0$ for all $a+b+c=1$, $a,b,c > 0$. By uvw, check two-equal and boundary.

Two-equal ($b=c=t$): we computed $u^2 + 27v^2 - kv = -4t^3(1-3t)^3 + (4-k) \cdot v(1-27v) \cdot ...$. Hmm, let me recompute directly.

Actually, $u^2 + 27v^2 - kv$ for $b=c=t$: 
$u^2 + 27v^2 = 4t^2 - 12t^3 + 36t^4 - 108t^5 + 108t^6$ (from earlier: $u^2 = 4t^2-12t^3+9t^4$, $27v^2 = 27t^4 - 108t^5 + 108t^6$, sum $= 4t^2 - 12t^3 + 36t^4 - 108t^5 + 108t^6$).
$kv = k(t^2 - 2t^3)$.

$u^2 + 27v^2 - kv = 4t^2 - 12t^3 + 36t^4 - 108t^5 + 108t^6 - kt^2 + 2kt^3$
$= (4-k)t^2 + (2k-12)t^3 + 36t^4 - 108t^5 + 108t^6$
$= t^2[(4-k) + (2k-12)t + 36t^2 - 108t^3 + 108t^4]$.

For $k = 15/4$: $4 - k = 1/4$, $2k - 12 = 15/2 - 12 = -9/2$.

$= t^2[1/4 - 9t/2 + 36t^2 - 108t^3 + 108t^4]$.

Let me check at $t = 1/6$: $1/4 - 9/12 + 36/36 - 108/216 + 108/1296 = 1/4 - 3/4 + 1 - 1/2 + 1/12$.
$= 3/12 - 9/12 + 12/12 - 6/12 + 1/12 = (3 - 9 + 12 - 6 + 1)/12 = 1/12 > 0$.

Hmm, that's positive, not zero. But we expected the minimum of $R$ to be $15/4$ at $t = 1/6$, meaning $R(1/6) = 15/4$, so the ratio equals $15/4$ there, meaning $u^2 + 27v^2 - \frac{15}{4}v = 0$ at $t = 1/6$?

Wait, $R = (u^2 - 81v^2)/(v(1-27v))$... no. Let me recheck. The ratio $R = (s^2 - 81)/(p - 27)$. And $s^2 - 81 = (u^2/v^2) - 81 = (u^2 - 81v^2)/v^2$. $p - 27 = 1/v - 27 = (1-27v)/v$. So $R = \frac{(u^2-81v^2)/v^2}{(1-27v)/v} = \frac{u^2 - 81v^2}{v(1-27v)}$.

And the inequality $s^2 - 81 \geq k(p-27)$ becomes $u^2 - 81v^2 \geq kv(1-27v)$, i.e., $u^2 - 81v^2 - kv + 27kv^2 \geq 0$, i.e., $u^2 + (27k - 81)v^2 - kv \geq 0$.

Oh I see, I had the wrong expression! It's $u^2 + (27k-81)v^2 - kv \geq 0$, not $u^2 + 27v^2 - kv$.

Let me redo. For $k = 4$: $27k - 81 = 108 - 81 = 27$. So $u^2 + 27v^2 - 4v \geq 0$. That's what I had. And we showed it's negative at $t = 0.3$. So $k = 4$ fails. ✓ consistent.

For general $k$: $u^2 + (27k - 81)v^2 - kv \geq 0$.

For two-equal ($b = c = t$):
$u^2 = 4t^2 - 12t^3 + 9t^4$.
$(27k-81)v^2 = (27k-81)(t^4 - 4t^5 + 4t^6)$.
$-kv = -k(t^2 - 2t^3)$.

Sum $= 4t^2 - 12t^3 + 9t^4 + (27k-81)t^4 - 4(27k-81)t^5 + 4(27k-81)t^6 - kt^2 + 2kt^3$
$= (4-k)t^2 + (2k-12)t^3 + (9 + 27k - 81)t^4 - 4(27k-81)t^5 + 4(27k-81)t^6$
$= (4-k)t^2 + (2k-12)t^3 + (27k - 72)t^4 - (108k - 324)t^5 + (108k - 324)t^6$.

Hmm, this is getting messy. Let me instead directly find the infimum of $R(t)$ and verify it's the global infimum.

We found $R(t) = \frac{4(1+3t-9t^2)}{(1-2t)(6t+1)}$ for the two-equal case, with minimum $15/4$ at $t = 1/6$.

But we need to verify this is the global infimum, not just over two-equal. By uvw, the infimum of $R$ (a symmetric function) over the symmetric domain is achieved at two-equal (or boundary). But $R$ is a ratio, not a polynomial. Let me think about this differently.

The condition $k \leq R(a,b,c)$ for all $(a,b,c)$ is equivalent to $u^2 + (27k-81)v^2 - kv \geq 0$ for all $(a,b,c)$ with $a+b+c=1$. This is a symmetric polynomial inequality in $a,b,c$ (expressed via $u, v$). The degree in $v$ is 2. By the uvw theorem, it suffices to check when two variables are equal (and the boundary where one variable is 0, but $a,b,c > 0$ so we check the limit).

So for a given $k$, the inequality holds for all iff it holds for two-equal. The largest $k$ is the infimum of $R(t)$ over two-equal cases (and boundary limits).

We found $\inf_{t \in (0,1/2)} R(t) = 15/4$ at $t = 1/6$. Boundary: $t \to 0$ gives $R \to 4 > 15/4$, $t \to 1/2$ gives $R \to \infty$. So the infimum is $15/4$.

But wait, I should also check the boundary where one of $a, b, c \to 0$ (not just two-equal). When $a \to 0$, $b + c \to 1$, $v = abc \to 0$, $p = 1/v \to \infty$, $s = u/v \to \infty$. The ratio $R = (s^2 - 81)/(p - 27) \approx s^2/p = (u/v)^2/(1/v) = u^2/v \to \infty$ (since $u \to bc > 0$ and $v \to 0$). So $R \to \infty$ at this boundary. Good.

So the global infimum is $15/4$, achieved at the two-equal case $t = 1/6$, i.e., $b = c = 1/6$, $a = 1 - 1/3 = 2/3$.

Let me verify: $a = 2/3, b = c = 1/6$. $x = 3/2, y = z = 6$. Check constraint: $1/x + 1/y + 1/z = 2/3 + 1/6 + 1/6 = 2/3 + 1/3 = 1$. ✓.

$s = 3/2 + 6 + 6 = 13.5 = 27/2$. $s^2 = 729/4$. $s^2 - 81 = 729/4 - 324/4 = 405/4$.
$p = xy + yz + zx = (3/2)(6) + 36 + (3/2)(6) = 9 + 36 + 9 = 54$. $p - 27 = 27$.
$R = (405/4)/27 = 405/108 = 15/4$. ✓.

So $k = 15/4$.

Now I need to prove that $k = 15/4$ works, i.e., $(x+y+z)^2 - 81 \geq \frac{15}{4}(xy+yz+zx - 27)$ for all $x,y,z > 0$ with $xy+yz+zx = xyz$.

Equivalently (in terms of $a,b,c$ with $a+b+c=1$): $u^2 + (27 \cdot 15/4 - 81)v^2 - \frac{15}{4}v \geq 0$.

$27 \cdot 15/4 - 81 = 405/4 - 324/4 = 81/4$.

So we need $u^2 + \frac{81}{4}v^2 - \frac{15}{4}v \geq 0$, i.e., $4u^2 + 81v^2 - 15v \geq 0$.

With $u = ab+bc+ca$, $v = abc$, $a+b+c = 1$, $a,b,c > 0$.

By uvw (degree 2 in $v$), suffices to check $b = c = t$, $a = 1-2t$.

$4u^2 + 81v^2 - 15v$:
$4u^2 = 4(2t-3t^2)^2 = 4(4t^2 - 12t^3 + 9t^4) = 16t^2 - 48t^3 + 36t^4$.
$81v^2 = 81(t^2-2t^3)^2 = 81t^4 - 324t^5 + 324t^6$.
$-15v = -15t^2 + 30t^3$.

Sum $= 16t^2 - 48t^3 + 36t^4 + 81t^4 - 324t^5 + 324t^6 - 15t^2 + 30t^3$
$= t^2 - 18t^3 + 117t^4 - 324t^5 + 324t^6$
$= t^2(1 - 18t + 117t^2 - 324t^3 + 324t^4)$.

Let me factor $h(t) = 1 - 18t + 117t^2 - 324t^3 + 324t^4$.

Check $t = 1/6$: $1 - 3 + 117/36 - 324/216 + 324/1296 = 1 - 3 + 13/4 - 3/2 + 1/4$.
$= 1 - 3 + 3.25 - 1.5 + 0.25 = 0$. So $(6t - 1)$ or $(t - 1/6)$ is a factor. Since it's the minimum, likely a double root.

$h'(t) = -18 + 234t - 972t^2 + 1296t^3$. $h'(1/6) = -18 + 39 - 27 + 6 = 0$. So double root at $t = 1/6$, i.e., $(6t-1)^2$ factor.

$h(t) = 324t^4 - 324t^3 + 117t^2 - 18t + 1$. Divide by $(6t-1)^2 = 36t^2 - 12t + 1$.

$324t^4 - 324t^3 + 117t^2 - 18t + 1 = (36t^2 - 12t + 1)(At^2 + Bt + C)$.

$(36t^2 - 12t + 1)(At^2 + Bt + C) = 36At^4 + (36B - 12A)t^3 + (36C - 12B + A)t^2 + (-12C + B)t + C$.

Match:
- $t^4$: $36A = 324 \Rightarrow A = 9$.
- $t^3$: $36B - 12A = -324 \Rightarrow 36B - 108 = -324 \Rightarrow 36B = -216 \Rightarrow B = -6$.
- $t^2$: $36C - 12B + A = 117 \Rightarrow 36C + 72 + 9 = 117 \Rightarrow 36C = 36 \Rightarrow C = 1$.
- $t^1$: $-12C + B = -12 - 6 = -18$. ✓
- $t^0$: $C = 1$. ✓

So $h(t) = (6t-1)^2(9t^2 - 6t + 1) = (6t-1)^2(3t-1)^2$.

So $4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0$. ✓

Equality at $t = 1/6$ (i.e., $a = 2/3, b = c = 1/6$) and $t = 1/3$ (i.e., $a = b = c = 1/3$), and $t = 0$ (boundary).

So for the two-equal case, $4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0$. ✓

By uvw, since the expression $4u^2 + 81v^2 - 15v$ is symmetric and at most degree 2 in $v$ (with $a+b+c$ fixed), the inequality holds for all $a,b,c > 0$ with $a+b+c = 1$.

Therefore $k = 15/4$ is the largest value.

Wait, I should make sure I'm applying uvw correctly. Let me recall the uvw theorem precisely.

**UVW Theorem**: For a symmetric inequality $f(a,b,c) \geq 0$ where $f$ is a polynomial, if we fix $a + b + c = s$ and the inequality can be written as a function of $u = ab+bc+ca$ and $v = abc$ that is at most quadratic in $v$, then the inequality holds for all $a,b,c \geq 0$ with $a+b+c = s$ if and only if it holds when two of the variables are equal (including the case when one is 0).

Our expression: $F = 4u^2 + 81v^2 - 15v$. As a function of $v$ (with $u$ free), it's $81v^2 - 15v + 4u^2$, which is quadratic in $v$. ✓

So by uvw, $F \geq 0$ for all $a,b,c \geq 0$ with $a+b+c = 1$ iff $F \geq 0$ when two are equal. We verified the two-equal case. Also need to check the boundary $a = 0$: then $u = bc$, $v = 0$, $F = 4b^2c^2 \geq 0$. ✓ (and $b + c = 1$).

So the proof is complete. $k = 15/4$.

Actually, let me also make sure the answer is exactly $15/4$ and not that we need to also consider the case $p - 27 < 0$. We showed $p = 1/v \geq 27$ always (since $v \leq 1/27$), so $p - 27 \geq 0$ always. And $s^2 - 81 \geq 0$ always. So the ratio is always well-defined and nonneg, and we need $k \leq \inf R = 15/4$.

Let me also double-check that $k = 15/4$ is achievable (tight), i.e., equality holds at some point. At $a = 2/3, b = c = 1/6$ (i.e., $x = 3/2, y = z = 6$), we have $R = 15/4$ exactly, so equality holds. ✓

Great, the answer is $k = \boxed{15/4}$.

Now let me write up the proof cleanly.

Let me also verify the uvw application once more. The standard uvw method: A symmetric homogeneous... wait, our expression isn't homogeneous. $4u^2 + 81v^2 - 15v$: $u^2$ has degree 4 in $a,b,c$, $v^2$ has degree 6, $v$ has degree 3. Not homogeneous. But uvw doesn't require homogeneity when $a+b+c$ is fixed.

The uvw method (as commonly stated): Given $a+b+c = s$ fixed, a symmetric function $f(a,b,c)$ can be expressed as $g(u, v)$ where $u = ab+bc+ca$, $v = abc$. If $g$ is at most quadratic in $v$, then for fixed $s$ and $u$, $g$ is a quadratic in $v$, and the extremum of $g$ over the feasible $(u,v)$ region is achieved at the boundary of the feasible region, which corresponds to two variables being equal.

More precisely: for fixed $s$ and $u$, $v$ ranges over an interval $[v_{\min}, v_{\max}]$, and the endpoints correspond to two variables being equal (or one being 0). A quadratic in $v$ achieves its minimum either at the vertex (interior) or at endpoints. If the quadratic is convex (coefficient of $v^2$ positive), the minimum could be interior. Hmm, so uvw doesn't directly say it suffices to check two-equal for a convex quadratic.

Wait, let me reconsider. The coefficient of $v^2$ is $81 > 0$, so $g(u,v) = 81v^2 - 15v + 4u^2$ is convex in $v$. The minimum over $v$ for fixed $u$ is at $v = 15/(162) = 5/54$, which might be interior. So uvw in the simple form might not directly apply.

Hmm, but actually the uvw theorem is more nuanced. Let me recall it properly.

The uvw method states: For a symmetric inequality $f(a,b,c) \geq 0$ with $a+b+c$ fixed, if $f$ expressed as $g(u,v)$ is at most degree 2 in $v$, then:
- If $g$ is concave in $v$ (coefficient of $v^2 \leq 0$), the minimum is at the boundary (two equal), so check two-equal.
- If $g$ is convex in $v$ (coefficient of $v^2 > 0$), the minimum could be interior, and we need to check the critical point as well.

Hmm, so for convex case, we might need additional analysis. But actually, there's a stronger version:

**Theorem (uvw)**: A symmetric inequality $f(a,b,c) \geq 0$ with $f$ at most degree 2 in $v$ (with $s = a+b+c$ fixed) holds for all real $a,b,c$ with $a+b+c = s$ iff it holds when two variables are equal.

This is because: for fixed $s$, the feasible region in $(u,v)$ space is bounded by curves corresponding to two-equal cases. A function at most quadratic in $v$ ... actually I think the correct statement involves the fact that the boundary of the feasible $(u,v)$ region is exactly the two-equal curve, and for a quadratic in $v$, the minimum over the region is on the boundary.

Let me think again. For fixed $s = 1$, the feasible $(u, v)$ region: $u \in [0, 1/3]$, and for each $u$, $v$ ranges in $[v_1(u), v_2(u)]$ where $v_1, v_2$ correspond to two-equal configurations. The function $g(u,v) = 4u^2 + 81v^2 - 15v$.

For fixed $u$, $g$ is convex in $v$ (min at $v^* = 15/162 = 5/54$). If $v^* \in [v_1(u), v_2(u)]$, the min for that $u$ is $g(u, v^*) = 4u^2 + 81(5/54)^2 - 15(5/54) = 4u^2 + 81 \cdot 25/2916 - 75/54 = 4u^2 + 25/36 - 25/18 = 4u^2 - 25/36$.

This is minimized at $u = 0$: $-25/36 < 0$. But is $v^* = 5/54$ feasible when $u = 0$? When $u = 0$, we need $ab + bc + ca = 0$ with $a+b+c = 1$, $a,b,c \geq 0$. This means at most one variable is nonzero, so $v = 0$. So $v^* = 5/54$ is not feasible at $u = 0$.

So the feasibility constraint matters. The point is that $v^*$ might not be in the feasible range for all $u$.

This is getting complicated. Let me just directly prove $4u^2 + 81v^2 - 15v \geq 0$ for $a+b+c=1$, $a,b,c \geq 0$ using a different method, or verify the uvw application more carefully.

Actually, let me use a direct approach. We have the identity for two-equal case: $4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0$. 

For the general case, let me try to express $4u^2 + 81v^2 - 15v$ as a sum of squares or use Schur's inequality.

Schur's inequality: For $a+b+c = 1$, $a^3+b^3+c^3 + abc \geq ab(a+b) + bc(b+c) + ca(c+a)$, i.e., $1 - 3u + 3v + v \geq u - 3v$... let me recall. $a^3+b^3+c^3 = (a+b+c)^3 - 3(a+b+c)u + 3v = 1 - 3u + 3v$. Schur (degree 1, i.e., $t=1$): $a^3+b^3+c^3 + abc \geq \sum ab(a+b)$. $\sum ab(a+b) = \sum(a^2b + ab^2) = (a+b+c)u - 3v = u - 3v$. So Schur: $(1-3u+3v) + v \geq u - 3v$, i.e., $1 - 3u + 4v \geq u - 3v$, i.e., $1 - 4u + 7v \geq 0$.

Hmm, not sure that directly helps.

Let me try another approach. We want to show $4u^2 + 81v^2 \geq 15v$ for $a+b+c=1$, $a,b,c \geq 0$.

By AM-GM or other inequalities... Let me think about what relationships between $u$ and $v$ we have.

We know $u \leq 1/3$ (since $u = (1 - (a^2+b^2+c^2))/2 \leq (1 - 1/3)/2 = 1/3$).
We know $v \leq 1/27$.
We know $u^2 \geq 3v$ (since $(ab+bc+ca)^2 \geq 3abc(a+b+c) = 3v$). This is a well-known inequality: $u^2 \geq 3sv = 3v$ (with $s=1$).

So $4u^2 \geq 12v$. Then $4u^2 + 81v^2 - 15v \geq 12v + 81v^2 - 15v = 81v^2 - 3v = 3v(27v - 1)$.

Since $v \leq 1/27$, $27v - 1 \leq 0$, so $3v(27v - 1) \leq 0$. This goes the wrong way! So $u^2 \geq 3v$ is not enough.

Let me try a tighter bound. We need to use the relationship between $u$ and $v$ more precisely.

Actually, let me just use the uvw method properly. The key theorem:

**Theorem**: Let $f(a,b,c)$ be a symmetric function with $a+b+c$ fixed. Write $f = g(u,v)$. If $\frac{\partial^2 g}{\partial v^2} \geq 0$ (convex in $v$) or $\leq 0$ (concave), then the extrema of $f$ are achieved when two variables are equal or one is zero.

Wait, I think the correct statement is: regardless of convexity, if $g$ is at most degree 2 in $v$, then the minimum of $f$ is achieved when two variables are equal or at the boundary. This is because the feasible region in $(u,v)$ has boundary given by the two-equal curve, and a quadratic function's minimum over a compact region is either at a critical point interior to the region or on the boundary.

If the minimum is interior, then $\partial g/\partial u = 0$ and $\partial g/\partial v = 0$. $\partial g/\partial v = 162v - 15 = 0 \Rightarrow v = 5/54$. $\partial g/\partial u = 8u = 0 \Rightarrow u = 0$. But $u = 0, v = 5/54$ is not feasible (as we noted, $u=0$ forces $v = 0$). So there's no interior critical point, and the minimum is on the boundary, i.e., two-equal case.

That's the key! The interior critical point $(u,v) = (0, 5/54)$ is not feasible, so the minimum is on the boundary (two-equal or one-zero). We checked both: two-equal gives $t^2(6t-1)^2(3t-1)^2 \geq 0$, and one-zero ($a=0$) gives $4u^2 \geq 0$.

So the proof works. Let me also verify: is the feasible region in $(u,v)$ such that the boundary is exactly the two-equal curve (plus the $v=0$ boundary)? Yes, for $a+b+c = 1$, $a,b,c \geq 0$, the feasible $(u,v)$ region is bounded by:
- $v = 0$ (when one variable is 0)
- The two-equal curve (when two variables are equal)

And the interior of the region corresponds to three distinct positive values. The minimum of a continuous function on a compact set is achieved; if not at an interior critical point, it's on the boundary.

Actually, the feasible region might not be compact in a nice way, but since $a,b,c \geq 0$ and $a+b+c=1$, it's a compact simplex, and $u, v$ are continuous functions, so the image is compact. The function $g(u,v)$ is continuous, so it achieves its minimum. If the minimum is at an interior point of the feasible $(u,v)$ region, then the gradient must vanish there, which we showed doesn't happen (the critical point is infeasible). So the minimum is on the boundary.

Hmm, but "interior of the feasible $(u,v)$ region" — I need to be more careful. The map $(a,b,c) \to (u,v)$ is not injective; the feasible $(u,v)$ region is the image. An interior point of the image could correspond to a boundary point of the simplex. But actually, the boundary of the simplex ($a=0$ or $b=0$ or $c=0$) maps to $v = 0$, which is the boundary of the image. And the two-equal cases map to the other boundary curve. So the interior of the image corresponds to the interior of the simplex (all variables distinct and positive). At an interior minimum, by Lagrange multipliers, the gradient of $g$ w.r.t. $(u,v)$ must be proportional to the gradient of the constraint... 

Actually, this is getting too complicated for a clean proof. Let me just use the standard uvw theorem as a lemma and cite it.

Alternatively, I can prove it directly. Let me try to express $4u^2 + 81v^2 - 15v$ as a sum of nonneg terms.

We have the two-equal factorization: $t^2(6t-1)^2(3t-1)^2$. This suggests the expression might be related to discriminant-like quantities.

Let me try the substitution $p = a - b$, $q = b - c$ (or use the Schur-like approach).

Actually, let me try to use the SOS (sum of squares) approach or find a direct proof.

We want: $4(ab+bc+ca)^2 + 81(abc)^2 \geq 15abc$ with $a+b+c = 1$.

Let me substitute $a+b+c = 1$ and use $u = ab+bc+ca$, $v = abc$.

We know that $a,b,c$ are roots of $t^3 - t^2 + ut - v = 0$. For three real nonneg roots, the discriminant must be $\geq 0$:
$\Delta = 18 \cdot 1 \cdot u \cdot v - 4u^3 + u^2 - 4v - 27v^2 \geq 0$ (discriminant of $t^3 - t^2 + ut - v$).

Wait, the discriminant of $t^3 + pt^2 + qt + r$ is $\Delta = 18pqr - 4p^3r + p^2q^2 - 4q^3 - 27r^2$. Here $p = -1, q = u, r = -v$:
$\Delta = 18(-1)(u)(-v) - 4(-1)^3(-v) + (-1)^2 u^2 - 4u^3 - 27(-v)^2$
$= 18uv - 4v + u^2 - 4u^3 - 27v^2$.

For three real roots, $\Delta \geq 0$: $u^2 - 4u^3 + 18uv - 4v - 27v^2 \geq 0$.

Hmm, this gives a relationship but I'm not sure how to use it directly.

Let me try yet another approach. Let me just prove it using the uvw method and state the lemma clearly.

Actually, you know what, let me try to find a direct SOS proof.

$4u^2 + 81v^2 - 15v \geq 0$ with $a+b+c = 1$.

Let me write $v = abc$ and use $a+b+c=1$.

$15abc = 15abc(a+b+c) = 15(a^2bc + ab^2c + abc^2)$... no, $abc \cdot 1 = abc(a+b+c) = a^2bc + ab^2c + abc^2$. So $15v = 15(a^2bc + ab^2c + abc^2)$.

$4u^2 = 4(ab+bc+ca)^2 = 4(a^2b^2 + b^2c^2 + c^2a^2 + 2abc(a+b+c)) = 4(a^2b^2+b^2c^2+c^2a^2) + 8abc$.

So $4u^2 + 81v^2 - 15v = 4(a^2b^2+b^2c^2+c^2a^2) + 8abc + 81a^2b^2c^2 - 15(a^2bc + ab^2c + abc^2)$.

$= 4(a^2b^2+b^2c^2+c^2a^2) - 15abc(a+b+c) + 8abc + 81a^2b^2c^2$

Wait, $-15v = -15abc$, and $15abc = 15abc \cdot 1 = 15abc(a+b+c)$. So:

$4u^2 + 81v^2 - 15v = 4(a^2b^2+b^2c^2+c^2a^2) + 8abc + 81a^2b^2c^2 - 15abc$
$= 4(a^2b^2+b^2c^2+c^2a^2) - 7abc + 81a^2b^2c^2$.

Hmm, $8abc - 15abc = -7abc$. So:

$F = 4(a^2b^2+b^2c^2+c^2a^2) - 7abc + 81a^2b^2c^2$.

With $a+b+c = 1$. Let me see if this can be written as SOS.

$4(a^2b^2+b^2c^2+c^2a^2) - 7abc + 81a^2b^2c^2$.

Let $p = ab, q = bc, r = ca$. Then $p + q + r = u$, $pqr = (abc)^2 = v^2$, and $p, q, r \geq 0$. Also $a + b + c = 1$ gives... $p, q, r$ are not independent; they satisfy $pr/q = a^2$ etc. Actually $pqr = v^2$ and $p + q + r = u$.

$F = 4(p^2 + q^2 + r^2) - 7\sqrt{pqr} \cdot ... $ no, $abc = v = \sqrt{pqr}$... this is getting messy.

Let me try a different substitution. Since we know equality at $(2/3, 1/6, 1/6)$ and permutations, and at $(1/3, 1/3, 1/3)$, let me try to express $F$ in terms of deviations.

Actually, let me just go with the uvw approach and state it as a lemma. The proof is clean enough.

Let me reconsider. Actually, I realize I should double-check the uvw theorem statement. The standard result is:

**UVW Lemma**: Let $f(a,b,c)$ be a symmetric function, and suppose $a+b+c = s$ is fixed. If $f$, when expressed as $g(u, v)$ where $u = ab+bc+ca$, $v = abc$, is a polynomial of degree at most 2 in $v$, then $f$ achieves its maximum and minimum on the set $\{(a,b,c) : a+b+c = s, a,b,c \geq 0\}$ when two of the variables are equal (or one is zero).

This is because: the set of feasible $(u,v)$ is a compact region whose boundary consists of the curve where two variables are equal and the line $v = 0$. The function $g(u,v)$, being quadratic in $v$, has the property that on any line $u = \text{const}$, it's a quadratic in $v$, so its minimum on that line segment is at an endpoint or at the vertex. If at the vertex, then $\partial g / \partial v = 0$ there. But we also need to optimize over $u$. The overall minimum is either on the boundary of the feasible region, or at an interior point where $\nabla g = 0$. We check that $\nabla g = 0$ has no feasible solution, so the minimum is on the boundary.

$\nabla g = (8u, 162v - 15) = (0, 0)$ gives $u = 0, v = 5/54$. But $u = 0$ with $a+b+c = 1, a,b,c \geq 0$ means at most one variable is positive, so $v = 0 \neq 5/54$. Infeasible. ✓

So the minimum is on the boundary: either $v = 0$ (one variable zero) or two variables equal. We check both and find $F \geq 0$. ✓

OK so the proof is solid. Let me write it up.

Actually, I realize I should present this more carefully. Let me structure the proof:

1. Substitution $a = 1/x, b = 1/y, c = 1/z$ transforms constraint to $a+b+c=1$.
2. Express the inequality in terms of $u = ab+bc+ca$, $v = abc$.
3. Show the inequality becomes $4u^2 + 81v^2 - 15v \geq 0$ (for $k = 15/4$).
4. Use uvw to reduce to two-equal case.
5. Verify two-equal case factors as $t^2(6t-1)^2(3t-1)^2 \geq 0$.
6. Show $k = 15/4$ is tight (equality at $a = 2/3, b = c = 1/6$).

Let me also verify the direction: we need the LARGEST $k$. Since $p - 27 \geq 0$ always, larger $k$ makes the inequality harder to satisfy. So the largest $k$ that works is the infimum of the ratio, which is $15/4$.

Let me write the proof.

Hmm, actually let me reconsider step 2 more carefully. The inequality is $(x+y+z)^2 - 81 \geq k(xy + yz + zx - 27)$.

With $a = 1/x$ etc., $a+b+c = 1$:
- $x + y + z = 1/a + 1/b + 1/c = (ab+bc+ca)/(abc) = u/v$.
- $xy + yz + zx = 1/(ab) + 1/(bc) + 1/(ca) = (a+b+c)/(abc) = 1/v$.

So $(x+y+z)^2 - 81 = u^2/v^2 - 81 = (u^2 - 81v^2)/v^2$.
$xy+yz+zx - 27 = 1/v - 27 = (1 - 27v)/v$.

Inequality: $(u^2 - 81v^2)/v^2 \geq k(1-27v)/v$, i.e., $u^2 - 81v^2 \geq kv(1-27v)$ (multiplying by $v^2 > 0$).

$u^2 - 81v^2 - kv + 27kv^2 \geq 0$, i.e., $u^2 + (27k - 81)v^2 - kv \geq 0$.

For $k = 15/4$: $27 \cdot 15/4 - 81 = 405/4 - 324/4 = 81/4$. So $u^2 + \frac{81}{4}v^2 - \frac{15}{4}v \geq 0$, i.e., $4u^2 + 81v^2 - 15v \geq 0$. ✓

Now, we also need to verify that $1 - 27v \geq 0$, i.e., $v \leq 1/27$. By AM-GM, $v = abc \leq ((a+b+c)/3)^3 = 1/27$. ✓ And $1 - 27v \geq 0$ means $p - 27 \geq 0$, so the direction is correct: we need $k \leq$ ratio.

Also $u^2 - 81v^2 \geq 0$? $u^2/v^2 = (x+y+z)^2 \geq 81$? We need $x + y + z \geq 9$. By Cauchy-Schwarz: $(x+y+z)(1/x + 1/y + 1/z) \geq 9$, and $1/x + 1/y + 1/z = 1$, so $x+y+z \geq 9$. ✓ So $u^2/v^2 \geq 81$, i.e., $u^2 \geq 81v^2$, i.e., $u^2 - 81v^2 \geq 0$. ✓

So both sides nonneg, and we need $k \leq \inf \frac{u^2 - 81v^2}{v(1-27v)}$.

The infimum is $15/4$, achieved at $a = 2/3, b = c = 1/6$.

Now let me write the clean proof.

Let me also verify the two-equal computation once more. $b = c = t$, $a = 1 - 2t$, $t \in [0, 1/2]$.

$u = ab + bc + ca = (1-2t)t + t^2 + (1-2t)t = 2t(1-2t) + t^2 = 2t - 4t^2 + t^2 = 2t - 3t^2$.
$v = abc = (1-2t) \cdot t \cdot t = t^2(1-2t) = t^2 - 2t^3$.

$4u^2 = 4(2t - 3t^2)^2 = 4(4t^2 - 12t^3 + 9t^4) = 16t^2 - 48t^3 + 36t^4$.
$81v^2 = 81(t^2 - 2t^3)^2 = 81(t^4 - 4t^5 + 4t^6) = 81t^4 - 324t^5 + 324t^6$.
$-15v = -15(t^2 - 2t^3) = -15t^2 + 30t^3$.

Sum: $(16 - 15)t^2 + (-48 + 30)t^3 + (36 + 81)t^4 - 324t^5 + 324t^6$
$= t^2 - 18t^3 + 117t^4 - 324t^5 + 324t^6$
$= t^2(1 - 18t + 117t^2 - 324t^3 + 324t^4)$.

Factor: $324t^4 - 324t^3 + 117t^2 - 18t + 1$.

We showed $= (6t-1)^2(3t-1)^2$. Let me verify: $(6t-1)^2 = 36t^2 - 12t + 1$. $(3t-1)^2 = 9t^2 - 6t + 1$.

$(36t^2 - 12t + 1)(9t^2 - 6t + 1) = 324t^4 - 216t^3 + 36t^2 - 108t^3 + 72t^2 - 12t + 9t^2 - 6t + 1$
$= 324t^4 - 324t^3 + (36 + 72 + 9)t^2 + (-12 - 6)t + 1$
$= 324t^4 - 324t^3 + 117t^2 - 18t + 1$. ✓

So $4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0$. ✓

Now for the boundary $v = 0$ (one variable zero, say $a = 0$): $u = bc$, $v = 0$. $4u^2 + 81v^2 - 15v = 4b^2c^2 \geq 0$. ✓

Great. The proof is complete. Let me write it up properly.

One more thing: I need to justify the uvw reduction clearly. Let me state it as a lemma and prove it briefly.

**Lemma (uvw)**: Let $s > 0$ and let $g(u, v)$ be a polynomial in $u$ and $v$. Consider the problem of minimizing $g(u,v)$ over the set $\mathcal{F} = \{(u,v) : \exists\, a,b,c \geq 0,\, a+b+c = s,\, ab+bc+ca = u,\, abc = v\}$. If $g$ is at most degree 2 in $v$, and the system $\partial g/\partial u = 0$, $\partial g/\partial v = 0$ has no solution in the interior of $\mathcal{F}$, then the minimum is achieved on the boundary of $\mathcal{F}$, which corresponds to either $v = 0$ (one variable zero) or two variables being equal.

*Proof sketch*: $\mathcal{F}$ is compact (image of compact simplex). $g$ is continuous, so achieves its min. If the min is at an interior point of $\mathcal{F}$, then since the map $(a,b,c) \mapsto (u,v)$ is a submersion in the interior (three distinct positive roots), the min would require $\nabla g = 0$, contradicting the assumption. So min is on boundary. The boundary of $\mathcal{F}$ corresponds to the discriminant being zero (two equal roots) or $v = 0$ (one root zero).

Actually, I think I can avoid stating the full lemma and just argue directly for our specific case. Let me think about the cleanest presentation.

Alternative direct proof without uvw: 

We want to show $4u^2 + 81v^2 - 15v \geq 0$ for $a+b+c = 1$, $a,b,c \geq 0$.

Approach: Fix $v$ and find the minimum of $u$ given $a+b+c=1$ and $abc = v$. By Lagrange multipliers, the extremum of $u$ subject to $a+b+c=1$ and $abc = v$ occurs when two variables are equal (standard result). So for fixed $v$, $u$ ranges between $u_{\min}(v)$ and $u_{\max}(v)$, both achieved when two variables are equal.

Since $4u^2 + 81v^2 - 15v$ is increasing in $u$ for $u \geq 0$ (as $8u \geq 0$), the minimum over $u$ for fixed $v$ is at $u = u_{\min}(v)$, which is achieved when two variables are equal.

So the global minimum is achieved when two variables are equal. This is a cleaner argument!

Wait, is $u_{\min}(v)$ achieved at two-equal? For fixed $a+b+c = 1$ and $abc = v$, the extrema of $u = ab+bc+ca$ are achieved when two variables are equal. Yes, this is standard (by Lagrange multipliers: $\nabla(u - \lambda(a+b+c) - \mu(abc)) = 0$ gives $b+c - \lambda - \mu bc = 0$, etc., subtracting pairs gives $(a-b)(\mu c - 1) = 0$, so either $a = b$ or $\mu c = 1$, etc., leading to two equal).

And since $F = 4u^2 + 81v^2 - 15v$ is increasing in $u$ (for $u \geq 0$, which holds since $a,b,c \geq 0$), the minimum for fixed $v$ is at $u_{\min}(v)$, the two-equal case.

But wait, for fixed $v$, there might be two two-equal configurations (one with $a = b \neq c$ and the "other branch"). We need to check both. Actually, for fixed $v$ and $a+b+c = 1$, the two-equal cases give specific $(u, v)$ pairs, and as $t$ varies, we trace out the boundary. The minimum of $F$ over all two-equal cases gives the global minimum.

Since we showed $F = t^2(6t-1)^2(3t-1)^2 \geq 0$ for all two-equal cases, and $F$ is increasing in $u$ (so the minimum for each $v$ is at the two-equal case), the global minimum is $\geq 0$.

Hmm, but I need to be a bit more careful. For fixed $v$, $u_{\min}$ is achieved at two-equal, and $F(u_{\min}(v), v) \geq 0$ (since it's a two-equal case). And $F(u, v) \geq F(u_{\min}(v), v) \geq 0$ for all $u \geq u_{\min}(v)$. So $F \geq 0$ everywhere. ✓

This is clean. But I need to also handle the case $v = 0$ (where $u_{\min}$ might not be two-equal but rather one-zero). Actually when $v = 0$, one variable is 0, and $u = bc$ with $b + c = 1$, $u \in [0, 1/4]$. $F = 4u^2 \geq 0$. ✓

OK let me just write the proof now. I'll use the approach: substitute, reduce to two-equal by the monotonicity in $u$ argument, verify two-equal.

Let me write it up.

---

**Proof.**

Let $a = 1/x, b = 1/y, c = 1/z$. The constraint $xy + yz + zx = xyz$ becomes $a + b + c = 1$ with $a, b, c > 0$.

Let $u = ab + bc + ca$ and $v = abc$. Then:
- $x + y + z = \frac{u}{v}$,
- $xy + yz + zx = \frac{1}{v}$.

The inequality becomes $\frac{u^2}{v^2} - 81 \geq k\left(\frac{1}{v} - 27\right)$, i.e., $u^2 - 81v^2 \geq kv(1 - 27v)$ (after multiplying by $v^2 > 0$).

**Claim:** The largest $k$ is $\frac{15}{4}$.

First, note that $v \leq \frac{1}{27}$ by AM-GM, so $1 - 27v \geq 0$. Also $x + y + z \geq 9$ by Cauchy-Schwarz ($(x+y+z)(1/x+1/y+1/z) \geq 9$), so $u^2 - 81v^2 \geq 0$. Thus the ratio $R = \frac{u^2 - 81v^2}{v(1-27v)}$ is well-defined and nonneg (away from $v = 1/27$), and we seek $k = \inf R$.

**Step 1: Reduction to two equal variables.** For fixed $v = abc$ and $a + b + c = 1$, the function $F = 4u^2 + 81v^2 - 15v$ is increasing in $u$ (since $\partial F/\partial u = 8u \geq 0$). The minimum of $u$ subject to $a + b + c = 1$, $abc = v$ is achieved when two variables are equal (by Lagrange multipliers). Hence the global minimum of $F$ is achieved when two of $a, b, c$ are equal.

**Step 2: Verification for two equal.** Set $b = c = t$, $a = 1 - 2t$, $t \in [0, 1/2]$. Then $u = 2t - 3t^2$, $v = t^2 - 2t^3$, and:

$$4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0.$$

This confirms $k = 15/4$ works.

**Step 3: Tightness.** At $t = 1/6$ (i.e., $a = 2/3, b = c = 1/6$, corresponding to $x = 3/2, y = z = 6$), we have $4u^2 + 81v^2 - 15v = 0$, so equality holds and $k$ cannot exceed $15/4$.

Therefore $k = \frac{15}{4}$.

### PROOF COMPLETE

---

Wait, I need to double-check the reduction argument in Step 1. The issue: for fixed $v$, $F$ is increasing in $u$, so min of $F$ is at min of $u$. Min of $u$ (given constraints) is at two-equal. But does every value of $v$ correspond to a two-equal configuration? 

For $v \in (0, 1/27]$, yes: the two-equal family $b = c = t$, $a = 1-2t$ gives $v = t^2(1-2t)$ which ranges over $(0, 1/27]$ as $t$ ranges over $(0, 1/2)$ (with max $1/27$ at $t = 1/3$). Actually $v = t^2(1-2t)$: at $t = 0$, $v = 0$; at $t = 1/3$, $v = 1/27$; at $t = 1/2$, $v = 0$. So $v$ ranges over $[0, 1/27]$, covering each value (possibly twice). So for each $v \in [0, 1/27]$, there's a two-equal configuration. ✓

And the min of $u$ for fixed $v$ is achieved at one of these two-equal configs. So the argument works.

Actually, I realize there's a subtlety: for a given $v$, there are two two-equal configurations (one with $t < 1/3$ and one with $t > 1/3$, giving different $u$ values). The minimum $u$ is one of them. Since $F$ is increasing in $u$, we want the smaller $u$. But we check $F \geq 0$ for ALL two-equal configs (all $t$), so both branches are covered. ✓

OK the proof is correct. Let me finalize.

Actually, let me reconsider whether the "increasing in $u$" argument fully works. $F = 4u^2 + 81v^2 - 15v$. For fixed $v$, $F$ is a function of $u$ only through $4u^2$, which is increasing for $u \geq 0$ and decreasing for $u \leq 0$. Since $u = ab + bc + ca \geq 0$ (as $a, b, c \geq 0$), $F$ is increasing in $u$. ✓

So for fixed $v$, $\min_u F = F(u_{\min}(v), v)$ where $u_{\min}(v)$ is the minimum of $u$ over the constraint set. And $u_{\min}(v)$ is achieved at a two-equal point. We verify $F \geq 0$ at all two-equal points, so $F(u_{\min}(v), v) \geq 0$ for all $v$, hence $F \geq 0$ everywhere. ✓

The proof is complete and correct. Let me finalize the write-up.

Let me reconsider: I want to make sure the Lagrange multiplier argument for "min of $u$ at fixed $v$ and $a+b+c=1$ is at two-equal" is correct.

We minimize $u = ab + bc + ca$ subject to $a + b + c = 1$ and $abc = v$, with $a, b, c \geq 0$.

Lagrange: $L = ab + bc + ca - \lambda(a + b + c - 1) - \mu(abc - v)$.
$\partial L / \partial a = b + c - \lambda - \mu bc = 0$
$\partial L / \partial b = a + c - \lambda - \mu ac = 0$
$\partial L / \partial c = a + b - \lambda - \mu ab = 0$

Subtract first two: $(b + c) - (a + c) - \mu(bc - ac) = 0 \Rightarrow (b - a)(1 - \mu c) = 0$.
So either $a = b$ or $\mu c = 1$.
Similarly, either $b = c$ or $\mu a = 1$, and either $a = c$ or $\mu b = 1$.

If all three are distinct, then $\mu a = \mu b = \mu c = 1$, so $a = b = c$, contradiction. So at least two are equal. ✓

(At boundary, one variable could be 0, which is the $v = 0$ case, handled separately.)

Great, the proof is rigorous. Let me write the final version.        — AI历史解题过程（thinking）
#   polymath_02876         — 题目ID

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
  <problem_id>polymath_02876</problem_id>
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

Find the largest real number $k$ for which the inequality
$$(x+y+z)^2-81 \geq k(xy+yz+zx-27)$$
holds true for all $x, y, z > 0$ satisfying
$$xy + yz + zx = xyz.$$

## Standard Solution

To find the largest real number \( k \) for which the inequality
\[
(x + y + z)^2 - 81 \geq k(xy + yz + zx - 27)
\]
holds true for all \( x, y, z > 0 \) satisfying \( xy + yz + zx = xyz \), we proceed as follows:

First, we consider the case where \( x = y \). The condition \( xy + yz + zx = xyz \) becomes:
\[
x^2 + 2xz = x^2 z \implies z = \frac{x}{x-2} \quad \text{for} \quad x > 2.
\]

Substituting \( x = y \) and \( z = \frac{x}{x-2} \) into the inequality, we need to verify:
\[
\left(2x + \frac{x}{x-2}\right)^2 - 81 \geq k \left( x^2 + 2x \cdot \frac{x}{x-2} - 27 \right).
\]

Simplifying the left-hand side:
\[
2x + \frac{x}{x-2} = \frac{2x(x-2) + x}{x-2} = \frac{2x^2 - 4x + x}{x-2} = \frac{2x^2 - 3x}{x-2}.
\]

Thus,
\[
\left( \frac{2x^2 - 3x}{x-2} \right)^2 - 81.
\]

Simplifying the right-hand side:
\[
x^2 + 2x \cdot \frac{x}{x-2} = x^2 + \frac{2x^2}{x-2} = \frac{x^2(x-2) + 2x^2}{x-2} = \frac{x^3 - 2x^2 + 2x^2}{x-2} = \frac{x^3}{x-2}.
\]

Thus,
\[
\frac{x^3}{x-2} - 27.
\]

The inequality becomes:
\[
\left( \frac{2x^2 - 3x}{x-2} \right)^2 - 81 \geq k \left( \frac{x^3}{x-2} - 27 \right).
\]

Define the function:
\[
f(x) = \frac{\left( \frac{2x^2 - 3x}{x-2} \right)^2 - 81}{\frac{x^3}{x-2} - 27}.
\]

Simplifying the numerator and denominator:
\[
\left( \frac{2x^2 - 3x}{x-2} \right)^2 - 81 = \frac{(2x^2 - 3x)^2 - 81(x-2)^2}{(x-2)^2},
\]
\[
\frac{x^3}{x-2} - 27 = \frac{x^3 - 27(x-2)}{x-2} = \frac{x^3 - 27x + 54}{x-2}.
\]

Thus,
\[
f(x) = \frac{(2x^2 - 3x)^2 - 81(x-2)^2}{(x-2)(x^3 - 27x + 54)}.
\]

Expanding and simplifying:
\[
(2x^2 - 3x)^2 = 4x^4 - 12x^3 + 9x^2,
\]
\[
81(x-2)^2 = 81x^2 - 324x + 324.
\]

Thus,
\[
(2x^2 - 3x)^2 - 81(x-2)^2 = 4x^4 - 12x^3 + 9x^2 - 81x^2 + 324x - 324 = 4x^4 - 12x^3 - 72x^2 + 324x - 324.
\]

Factoring:
\[
4x^4 - 12x^3 - 72x^2 + 324x - 324 = 4(x-3)^2(x^2 + 3x - 9).
\]

Thus,
\[
f(x) = \frac{4(x-3)^2(x^2 + 3x - 9)}{(x-2)(x^3 - 27x + 54)}.
\]

Simplifying further:
\[
x^3 - 27x + 54 = (x-3)(x^2 + 3x - 18).
\]

Thus,
\[
f(x) = \frac{4(x-3)^2(x^2 + 3x - 9)}{(x-2)(x-3)(x^2 + 3x - 18)} = \frac{4(x-3)(x^2 + 3x - 9)}{(x-2)(x^2 + 3x - 18)}.
\]

Evaluating the limit as \( x \to 3 \):
\[
\lim_{x \to 3} f(x) = \frac{4(0)(9 + 9 - 9)}{(1)(9 + 9 - 18)} = \frac{0}{0}.
\]

Using L'Hôpital's Rule:
\[
\lim_{x \to 3} \frac{4(x-3)(x^2 + 3x - 9)}{(x-2)(x^2 + 3x - 18)} = \frac{4(3x^2 - 18)}{(x^2 + 3x - 18) + (x-2)(2x + 3)} = \frac{4(27 - 18)}{9 + 9 - 18 + 1(6 + 3)} = \frac{36}{9} = 4.
\]

Thus, the minimum value of \( f(x) \) is \( \frac{15}{4} \).

Therefore, the largest real number \( k \) is:
\[
\boxed{\frac{15}{4}}.
\]

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. The constraint says don't use any tools, just think and output the proof in TUI.

Problem: Find the largest real number $k$ such that $(x+y+z)^2 - 81 \geq k(xy+yz+zx-27)$ for all $x,y,z > 0$ with $xy+yz+zx = xyz$.

First, let me check for answer leaks. The problem text doesn't contain any solution or answer. Good.

Let me solve. The constraint is $xy+yz+zx = xyz$. Dividing by $xyz$: $1/x + 1/y + 1/z = 1$.

Let $a = 1/x, b = 1/y, c = 1/z$ with $a,b,c > 0$ and $a+b+c = 1$.

We need $(x+y+z)^2 - 81 \geq k(xy+yz+zx - 27)$.

Note $xy+yz+zx = xyz$, so $xy+yz+zx - 27 = xyz - 27$.

Hmm, let me think about the equality case. By symmetry, likely $x=y=z$. If $x=y=z$, then $3x^2 = x^3$, so $x=3$. Then $x+y+z = 9$, $(x+y+z)^2 = 81$, and $xy+yz+zx = 27$. So both sides are 0 at $x=y=z=3$. This is the equality point where both sides vanish.

So we need to find the largest $k$ such that $(x+y+z)^2 - 81 \geq k(xy+yz+zx - 27)$ for all valid $(x,y,z)$.

Since at $(3,3,3)$ both sides are 0, this is like finding the infimum of the ratio $\frac{(x+y+z)^2 - 81}{xy+yz+zx - 27}$ over the constraint set (where denominator is positive, or handling sign).

Wait, we need the inequality to hold for ALL $x,y,z>0$ with the constraint. The denominator $xy+yz+zx - 27 = xyz - 27$ can be positive or negative.

Let me think. Let $s = x+y+z$, $p = xy+yz+zx = xyz$, $q = xyz = p$ (since $p = q$ on constraint).

Actually $xy+yz+zx = xyz$, so $p = q$ where $p = xy+yz+zx$, $q=xyz$.

The inequality: $s^2 - 81 \geq k(p - 27)$.

At $(3,3,3)$: $s=9, p=27$, both sides 0.

We want the largest $k$ such that $s^2 - 81 \geq k(p-27)$ always.

If $p > 27$ (i.e., $p - 27 > 0$), we need $k \leq \frac{s^2-81}{p-27}$.
If $p < 27$ (i.e., $p - 27 < 0$), we need $k \geq \frac{s^2-81}{p-27}$.

So $k$ must be $\leq$ the infimum of $\frac{s^2-81}{p-27}$ over $p>27$ region, AND $\geq$ the supremum over $p<27$ region.

For the largest $k$, we want $k = \inf_{p>27} \frac{s^2-81}{p-27}$, and we need this to be $\geq \sup_{p<27} \frac{s^2-81}{p-27}$.

Let me compute the ratio near $(3,3,3)$ using Lagrange / Taylor expansion to find the limiting value.

Let's parametrize. Use $a = 1/x, b=1/y, c=1/z$, $a+b+c=1$, $a,b,c>0$.

Then $x = 1/a$ etc. $s = 1/a + 1/b + 1/c$. $p = xy+yz+zx = 1/(ab) + 1/(bc) + 1/(ca) = (a+b+c)/(abc) = 1/(abc)$.

So $p = 1/(abc)$, $s = (ab+bc+ca)/(abc) = (ab+bc+ca) \cdot p$... wait let me recompute. $s = 1/a+1/b+1/c = (bc+ac+ab)/(abc)$. And $p = 1/(abc)$. So $s = (ab+bc+ca) \cdot p$? No: $s = (ab+bc+ca)/(abc) = (ab+bc+ca) \cdot p$. Yes since $p = 1/(abc)$.

Let $u = ab+bc+ca$, $v = abc$. Then $p = 1/v$, $s = u/v = u \cdot p$.

At $(3,3,3)$: $a=b=c=1/3$, $u = 3 \cdot 1/9 = 1/3$, $v = 1/27$, $p = 27$, $s = (1/3)/(1/27) = 9$. Good.

Inequality: $s^2 - 81 \geq k(p - 27)$, i.e., $(u/v)^2 - 81 \geq k(1/v - 27)$.

Multiply by $v^2 > 0$: $u^2 - 81 v^2 \geq k(v - 27 v^2) = kv(1 - 27v)$.

So $u^2 - 81v^2 \geq kv(1-27v)$.

At $(1/3,1/3,1/3)$: $u=1/3, v=1/27$. $u^2 = 1/9$, $81v^2 = 81/729 = 1/9$. LHS = 0. RHS: $kv(1-27v) = k \cdot (1/27)(1-1) = 0$. Good.

Now we need this for all $a,b,c>0$, $a+b+c=1$.

We have $u = ab+bc+ca$, $v = abc$ with $a+b+c=1$.

The constraint region: $a,b,c > 0$, sum 1. The range of $v = abc$: by AM-GM, $v \leq (1/3)^3 = 1/27$, with equality at $a=b=c=1/3$. And $v \to 0$ at boundary. So $v \in (0, 1/27]$.

When $v < 1/27$, $1 - 27v > 0$, so RHS $= kv(1-27v)$, sign depends on $k$.
When $v = 1/27$, RHS = 0.

Hmm, this is getting complex. Let me think about the limiting ratio as we approach $(3,3,3)$.

Consider perturbations. Let $a = 1/3 + \alpha$, $b = 1/3 + \beta$, $c = 1/3 + \gamma$ with $\alpha+\beta+\gamma = 0$ (to maintain sum 1).

$u = ab+bc+ca = (a+b+c)^2/2 - (a^2+b^2+c^2)/2 \cdot ... $ actually $u = ((a+b+c)^2 - (a^2+b^2+c^2))/2 = (1 - (a^2+b^2+c^2))/2$.

$a^2+b^2+c^2 = 3(1/9) + 2(1/3)(\alpha+\beta+\gamma) + (\alpha^2+\beta^2+\gamma^2) = 1/3 + 0 + (\alpha^2+\beta^2+\gamma^2)$.

So $u = (1 - 1/3 - (\alpha^2+\beta^2+\gamma^2))/2 = (2/3 - S_2)/2 = 1/3 - S_2/2$ where $S_2 = \alpha^2+\beta^2+\gamma^2$.

$v = abc = (1/3+\alpha)(1/3+\beta)(1/3+\gamma)$. 
$= 1/27 + (1/9)(\alpha+\beta+\gamma) + (1/3)(\alpha\beta+\beta\gamma+\gamma\alpha) + \alpha\beta\gamma$
$= 1/27 + 0 + (1/3)(\alpha\beta+\beta\gamma+\gamma\alpha) + \alpha\beta\gamma$.

Now $\alpha+\beta+\gamma=0$ implies $\alpha\beta+\beta\gamma+\gamma\alpha = -S_2/2$.

So $v = 1/27 - S_2/6 + \alpha\beta\gamma$.

Let $S_3 = \alpha\beta\gamma$. So $v = 1/27 - S_2/6 + S_3$.

Now compute $u^2 - 81v^2$:
$u = 1/3 - S_2/2$, $u^2 = 1/9 - S_2/3 + S_2^2/4$.
$v = 1/27 - S_2/6 + S_3$, $v^2 = 1/729 - (1/27)(S_2/3 - S_3)\cdot 2$... let me be careful.

$v^2 = (1/27)^2 - 2(1/27)(S_2/6 - S_3) + (S_2/6 - S_3)^2$
$= 1/729 - (1/27)(S_2/3 - 2S_3) + (S_2/6 - S_3)^2$
$= 1/729 - S_2/81 + 2S_3/27 + (S_2/6 - S_3)^2$.

$81 v^2 = 81/729 - 81 \cdot S_2/81 + 81 \cdot 2S_3/27 + 81(S_2/6-S_3)^2$
$= 1/9 - S_2 + 6S_3 + 81(S_2/6 - S_3)^2$.

$u^2 - 81v^2 = (1/9 - S_2/3 + S_2^2/4) - (1/9 - S_2 + 6S_3 + 81(S_2/6-S_3)^2)$
$= -S_2/3 + S_2 + S_2^2/4 - 6S_3 - 81(S_2/6-S_3)^2$
$= 2S_2/3 + S_2^2/4 - 6S_3 - 81(S_2/6-S_3)^2$.

Now RHS: $kv(1-27v)$. $v = 1/27 - S_2/6 + S_3$. $27v = 1 - 27S_2/6 + 27S_3 = 1 - 9S_2/2 + 27S_3$. $1 - 27v = 9S_2/2 - 27S_3$.

$v(1-27v) = (1/27 - S_2/6 + S_3)(9S_2/2 - 27S_3)$.

Leading order (order $S_2$): $(1/27)(9S_2/2) = S_2/6$.

So RHS $\approx k \cdot S_2/6$ at leading order.

LHS leading order: $2S_2/3$ (the $-6S_3$ is order... $S_3$ is cubic in perturbation, $S_2$ is quadratic, so $S_3$ is higher order than $S_2$). Actually $S_2 \sim \epsilon^2$, $S_3 \sim \epsilon^3$. So leading order of LHS is $2S_2/3$.

So at leading order: $2S_2/3 \geq k S_2/6$, giving $k \leq 4$.

So the candidate is $k = 4$. Let me verify this works and is tight.

We need to show $(x+y+z)^2 - 81 \geq 4(xy+yz+zx - 27)$ for all $x,y,z>0$ with $xy+yz+zx=xyz$.

$(x+y+z)^2 - 81 - 4(xy+yz+zx - 27) = x^2+y^2+z^2 + 2(xy+yz+zx) - 81 - 4(xy+yz+zx) + 108$
$= x^2+y^2+z^2 - 2(xy+yz+zx) + 27$
$= (x+y+z)^2 - 4(xy+yz+zx) + 27$... wait let me recompute.

$x^2+y^2+z^2 - 2(xy+yz+zx) + 27$.

Hmm, $x^2+y^2+z^2 - 2(xy+yz+zx) = (x+y+z)^2 - 4(xy+yz+zx)$. Actually $(x+y+z)^2 = x^2+y^2+z^2 + 2(xy+yz+zx)$, so $x^2+y^2+z^2 - 2(xy+yz+zx) = (x+y+z)^2 - 4(xy+yz+zx)$.

So we need to show $x^2+y^2+z^2 - 2(xy+yz+zx) + 27 \geq 0$, i.e., $(x+y+z)^2 - 4(xy+yz+zx) + 27 \geq 0$.

Note $x^2+y^2+z^2 - 2(xy+yz+zx) = (x-y-z)^2 - 4yz$... hmm, or $= (x-y)^2 + (y-z)^2 + (z-x)^2)/... $ no. Actually $x^2+y^2+z^2 - xy - yz - zx = \frac{1}{2}((x-y)^2+(y-z)^2+(z-x)^2)$. So $x^2+y^2+z^2 - 2(xy+yz+zx) = (x^2+y^2+z^2 - xy-yz-zx) - (xy+yz+zx) = \frac{1}{2}\sum(x-y)^2 - (xy+yz+zx)$.

So we need $\frac{1}{2}\sum(x-y)^2 - (xy+yz+zx) + 27 \geq 0$, i.e., $\frac{1}{2}\sum(x-y)^2 + 27 \geq xy+yz+zx = xyz$.

So we need to prove: $xyz \leq 27 + \frac{1}{2}((x-y)^2+(y-z)^2+(z-x)^2)$ given $xy+yz+zx = xyz$, $x,y,z>0$.

Equivalently, $xyz - 27 \leq \frac{1}{2}\sum(x-y)^2$.

Hmm, let me use the $a,b,c$ substitution. $a+b+c=1$, $a,b,c>0$, $x=1/a, y=1/b, z=1/c$.

$xy+yz+zx = xyz$ is automatic. We need to show $x^2+y^2+z^2 - 2(xy+yz+zx) + 27 \geq 0$.

$x^2+y^2+z^2 = 1/a^2 + 1/b^2 + 1/c^2$.
$xy+yz+zx = 1/(ab)+1/(bc)+1/(ca) = (a+b+c)/(abc) = 1/(abc) = 1/v$.

Hmm wait, that's $p = 1/v$. And $x^2+y^2+z^2 = (b^2c^2 + a^2c^2 + a^2b^2)/(a^2b^2c^2) = (u^2 - 2v\cdot 1)/(v^2)$... 

Actually $(ab+bc+ca)^2 = a^2b^2+b^2c^2+c^2a^2 + 2abc(a+b+c) = a^2b^2+b^2c^2+c^2a^2 + 2v$. So $a^2b^2+b^2c^2+c^2a^2 = u^2 - 2v$.

$x^2+y^2+z^2 = (a^2b^2+b^2c^2+c^2a^2)/v^2 = (u^2-2v)/v^2$.

$xy+yz+zx = u/v$ (since $= (a+b+c)/(abc) = 1/v$... wait. $xy = 1/(ab)$, $xy+yz+zx = 1/(ab)+1/(bc)+1/(ca) = (c+a+b)/(abc) = 1/v$. Yes $p = 1/v$.)

Hmm, I said $p = 1/v$ and also $s = u/v$. Let me recheck: $s = x+y+z = 1/a+1/b+1/c = (bc+ac+ab)/(abc) = u/v$. Yes.

So $x^2+y^2+z^2 = s^2 - 2p = u^2/v^2 - 2/v$.

The expression $x^2+y^2+z^2 - 2(xy+yz+zx) + 27 = (u^2/v^2 - 2/v) - 2/v + 27 = u^2/v^2 - 4/v + 27$.

$= (u^2 - 4v + 27v^2)/v^2$.

So we need $u^2 - 4v + 27v^2 \geq 0$ where $u = ab+bc+ca$, $v = abc$, $a+b+c=1$, $a,b,c>0$.

We need to prove $u^2 + 27v^2 \geq 4v$.

Recall $u \geq 3v^{2/3}$... by AM-GM on $ab, bc, ca$: $u = ab+bc+ca \geq 3(abc)^{2/3} = 3v^{2/3}$.

So $u^2 \geq 9v^{4/3}$. We need $9v^{4/3} + 27v^2 \geq 4v$, i.e., $9v^{1/3} + 27v \geq 4$ (dividing by $v > 0$, since $v = abc > 0$... wait $v^{4/3}/v = v^{1/3}$, $v^2/v = v$, $4v/v = 4$). So $9v^{1/3} + 27v \geq 4$.

But $v \leq 1/27$, so $v^{1/3} \leq 1/3$, $9v^{1/3} \leq 3$, $27v \leq 1$. So $9v^{1/3} + 27v \leq 4$ with equality at $v = 1/27$.

So this approach gives $9v^{1/3}+27v \leq 4$, the wrong direction! The AM-GM bound $u^2 \geq 9v^{4/3}$ is too weak (it's an equality only at $a=b=c$, and we need the inequality to go the other way).

So I can't just use $u \geq 3v^{2/3}$. I need a sharper relationship between $u$ and $v$ given $a+b+c=1$.

Let me reconsider. We need $u^2 + 27v^2 \geq 4v$ for $a+b+c=1$, $a,b,c>0$.

This is a known type. Let me think about it as: for fixed $v$, what's the minimum of $u$? Given $a+b+c=1$ and $abc = v$, the minimum of $u = ab+bc+ca$... 

Actually, given $a+b+c = 1$ and $abc = v$, $u$ ranges in some interval. By Schur or uvw, the extremal values of $u$ for fixed sum and product occur when two variables are equal.

Let me use the uvw method. The inequality $u^2 + 27v^2 - 4v \geq 0$ is symmetric in $a,b,c$. By uvw, it suffices to check when two variables are equal.

Set $b = c = t$, $a = 1 - 2t$, with $0 < t < 1/2$ (and $a > 0$ means $t < 1/2$).

$u = ab + bc + ca = 2at + t^2 = 2(1-2t)t + t^2 = 2t - 4t^2 + t^2 = 2t - 3t^2$.
$v = abc = (1-2t)t^2 = t^2 - 2t^3$.

$u^2 = (2t-3t^2)^2 = 4t^2 - 12t^3 + 9t^4$.
$27v^2 = 27(t^2-2t^3)^2 = 27(t^4 - 4t^5 + 4t^6) = 27t^4 - 108t^5 + 108t^6$.
$4v = 4t^2 - 8t^3$.

$u^2 + 27v^2 - 4v = 4t^2 - 12t^3 + 9t^4 + 27t^4 - 108t^5 + 108t^6 - 4t^2 + 8t^3$
$= -4t^3 + 36t^4 - 108t^5 + 108t^6$
$= -4t^3(1 - 9t + 27t^2 - 27t^3)$
$= -4t^3(1 - 3t)^3$.

Now $(1-3t)^3$: when $t < 1/3$, $(1-3t)^3 > 0$, so $-4t^3(1-3t)^3 < 0$. That's negative!

Wait, that means $u^2 + 27v^2 - 4v < 0$ for $t \in (0, 1/3)$? That would mean $k=4$ doesn't work!

Let me double check. At $t = 1/3$, $a = 1/3$, all equal, expression $= 0$. For $t$ slightly less than $1/3$, say $t = 0.3$, $a = 0.4$.

$u = 2(0.3) - 3(0.09) = 0.6 - 0.27 = 0.33$.
$v = 0.09 - 2(0.027) = 0.09 - 0.054 = 0.036$.
$u^2 = 0.1089$.
$27v^2 = 27(0.001296) = 0.034992$.
$4v = 0.144$.
$u^2 + 27v^2 - 4v = 0.1089 + 0.034992 - 0.144 = -0.000108 < 0$.

So indeed negative! So $k = 4$ does NOT work. My leading-order analysis was wrong, or the answer is less than 4.

Wait, let me recheck the leading order. The issue is that the leading order $2S_2/3$ vs $k S_2/6$ gives $k \leq 4$, but the next order terms matter. Let me recompute more carefully.

Actually, the leading order gives $k \leq 4$ as necessary, but it might not be sufficient. The actual answer could be smaller. Let me reconsider.

Hmm wait, actually the leading order analysis: LHS $\approx 2S_2/3$, RHS $\approx k S_2/6$. For the inequality LHS $\geq$ RHS near the point, we need $2S_2/3 \geq k S_2/6$, i.e., $k \leq 4$. But this is only necessary (the ratio approaches 4 from some direction). The actual infimum of the ratio over all points might be less than 4.

But wait, the computation above shows that for $k=4$, the expression $u^2 + 27v^2 - 4v$ can be negative, meaning $(x+y+z)^2 - 81 - 4(p - 27) < 0$, i.e., the inequality fails. So $k = 4$ is too big.

Let me recompute the ratio for the two-equal case to find the actual infimum.

For $b = c = t$, $a = 1-2t$:
- $s = u/v = (2t-3t^2)/(t^2-2t^3) = (2-3t)/(t(1-2t)) \cdot ... $ let me compute: $s = u/v = (2t-3t^2)/(t^2-2t^3) = t(2-3t)/(t^2(1-2t)) = (2-3t)/(t(1-2t))$.
- $p = 1/v = 1/(t^2(1-2t))$.

Ratio $R = (s^2 - 81)/(p - 27) = (u^2/v^2 - 81)/(1/v - 27) = (u^2 - 81v^2)/(v - 27v^2) = (u^2 - 81v^2)/(v(1-27v))$.

We computed $u^2 - 81v^2 = 2S_2/3 + ...$ earlier in terms of perturbation. Let me just compute directly for two-equal.

$u^2 - 81v^2$: 
$u^2 = 4t^2 - 12t^3 + 9t^4$.
$81v^2 = 81(t^2 - 2t^3)^2 = 81(t^4 - 4t^5 + 4t^6) = 81t^4 - 324t^5 + 324t^6$.
$u^2 - 81v^2 = 4t^2 - 12t^3 + 9t^4 - 81t^4 + 324t^5 - 324t^6 = 4t^2 - 12t^3 - 72t^4 + 324t^5 - 324t^6$.
$= 4t^2(1 - 3t - 18t^2 + 81t^3 - 81t^4)$.

$v(1-27v) = (t^2-2t^3)(1 - 27(t^2-2t^3)) = (t^2-2t^3)(1 - 27t^2 + 54t^3)$.
$= t^2(1-2t)(1 - 27t^2 + 54t^3)$.

$R = \frac{4t^2(1 - 3t - 18t^2 + 81t^3 - 81t^4)}{t^2(1-2t)(1 - 27t^2 + 54t^3)}$
$= \frac{4(1 - 3t - 18t^2 + 81t^3 - 81t^4)}{(1-2t)(1 - 27t^2 + 54t^3)}$.

Let me factor. At $t = 1/3$, both numerator and denominator vanish. Let me factor out $(1-3t)$.

Numerator: $f(t) = 1 - 3t - 18t^2 + 81t^3 - 81t^4$. $f(1/3) = 1 - 1 - 2 + 3 - 1 = 0$. Good.
$f'(t) = -3 - 36t + 243t^2 - 324t^3$. $f'(1/3) = -3 - 12 + 27 - 12 = 0$. So $(1-3t)^2$ divides.
$f''(t) = -36 + 486t - 972t^2$. $f''(1/3) = -36 + 162 - 108 = 18 \neq 0$. So $(1-3t)^2$ exactly (order 2).

Let me do polynomial division. $f(t) = -81t^4 + 81t^3 - 18t^2 - 3t + 1$.

Divide by $(1-3t)^2 = 1 - 6t + 9t^2$.

$-81t^4 + 81t^3 - 18t^2 - 3t + 1 = (1 - 6t + 9t^2) \cdot q(t)$.

Let $q(t) = at^2 + bt + c$. $(1-6t+9t^2)(at^2+bt+c) = 9at^4 + (9b-6a)t^3 + (9c - 6b + a)t^2 + (-6c + b)t + c$.

Match:
- $t^4$: $9a = -81 \Rightarrow a = -9$.
- $t^3$: $9b - 6a = 81 \Rightarrow 9b + 54 = 81 \Rightarrow 9b = 27 \Rightarrow b = 3$.
- $t^2$: $9c - 6b + a = -18 \Rightarrow 9c - 18 - 9 = -18 \Rightarrow 9c = 9 \Rightarrow c = 1$.
- $t^1$: $-6c + b = -6 + 3 = -3$. ✓
- $t^0$: $c = 1$. ✓

So $f(t) = (1-3t)^2(1 + 3t - 9t^2)$.

Denominator: $g(t) = (1-2t)(1 - 27t^2 + 54t^3)$. At $t=1/3$: $(1-2/3)(1 - 3 + 2) = (1/3)(0) = 0$. So $(1-3t)$ divides $1 - 27t^2 + 54t^3$.

$1 - 27t^2 + 54t^3$: at $t=1/3$, $1 - 3 + 2 = 0$. Divide by $(1-3t)$: $54t^3 - 27t^2 + 1 = (1-3t)(\text{quadratic})$. 

$54t^3 - 27t^2 + 0t + 1$. Divide by $-3t+1$... let me use $(1-3t)$. 

$(1-3t)(At^2 + Bt + C) = -3At^3 + (A - 3B)t^2 + (B - 3C)t + C$.
Match: $-3A = 54 \Rightarrow A = -18$. $A - 3B = -27 \Rightarrow -18 - 3B = -27 \Rightarrow -3B = -9 \Rightarrow B = 3$. $B - 3C = 0 \Rightarrow 3 - 3C = 0 \Rightarrow C = 1$. $C = 1$ ✓.

So $1 - 27t^2 + 54t^3 = (1-3t)(1 + 3t - 18t^2)$.

$g(t) = (1-2t)(1-3t)(1 + 3t - 18t^2)$.

So $R = \frac{4(1-3t)^2(1+3t-9t^2)}{(1-2t)(1-3t)(1+3t-18t^2)} = \frac{4(1-3t)(1+3t-9t^2)}{(1-2t)(1+3t-18t^2)}$.

At $t = 1/3$: $R = \frac{4 \cdot 0 \cdot (...)}{...} = 0/(\text{nonzero})$. Wait, $(1-3t) \to 0$, so $R \to 0$? That can't be right; the ratio should approach 4.

Hmm, let me recheck. At $t = 1/3$, $s = 9$, $p = 27$, so both numerator and denominator of original ratio are 0. The limit should be 4 (from leading order). But my factored form gives $R \to 0$?

Let me recheck the factorization. Oh wait, I think I need to check: is $t = 1/3$ giving $a = 1 - 2/3 = 1/3$, so $a = b = c = 1/3$, yes the symmetric point.

$R = \frac{4(1-3t)(1+3t-9t^2)}{(1-2t)(1+3t-18t^2)}$.

At $t = 1/3$: numerator has factor $(1 - 1) = 0$. Denominator: $(1 - 2/3)(1 + 1 - 2) = (1/3)(0) = 0$. So both 0! I need to check $1 + 3t - 18t^2$ at $t = 1/3$: $1 + 1 - 18/9 = 2 - 2 = 0$. So denominator also has $(1-3t)$ factor!

$1 + 3t - 18t^2$ at $t = 1/3$: $1 + 1 - 2 = 0$. Yes. So factor: $-18t^2 + 3t + 1 = (1-3t)(\text{linear})$. $-18t^2 + 3t + 1 = -(18t^2 - 3t - 1) = -(3t-1)(6t+1) = (1-3t)(6t+1)$.

Check: $(1-3t)(6t+1) = 6t + 1 - 18t^2 - 3t = 1 + 3t - 18t^2$. ✓.

So $g(t) = (1-2t)(1-3t)(1-3t)(6t+1) = (1-2t)(1-3t)^2(6t+1)$.

$R = \frac{4(1-3t)^2(1+3t-9t^2)}{(1-2t)(1-3t)^2(6t+1)} = \frac{4(1+3t-9t^2)}{(1-2t)(6t+1)}$.

At $t = 1/3$: $\frac{4(1 + 1 - 1)}{(1/3)(3)} = \frac{4 \cdot 1}{1} = 4$. ✓ 

So $R(t) = \frac{4(1+3t-9t^2)}{(1-2t)(6t+1)}$ for $t \in (0, 1/2)$, $t \neq 1/3$ (and $R(1/3) = 4$ by limit).

Now I need to find the infimum of $R(t)$ over $t \in (0, 1/2)$ (this gives the ratio for two-equal case; by uvw, the global infimum of the ratio is achieved in the two-equal case or at boundary).

Wait, but I need to be careful about the sign of the denominator $p - 27 = 1/v - 27 = (1 - 27v)/v$. $v = t^2(1-2t)$. $27v = 27t^2(1-2t)$. $1 - 27v = 1 - 27t^2 + 54t^3 = (1-3t)^2(6t+1) \cdot ... $ wait we had $1 - 27t^2 + 54t^3 = (1-3t)(1+3t-18t^2) = (1-3t)^2(6t+1)$. 

So $1 - 27v = (1-3t)^2(6t+1) \geq 0$ always! With equality only at $t = 1/3$.

So $p - 27 \geq 0$ always (since $v \leq 1/27$ by AM-GM, $p = 1/v \geq 27$). So the denominator $p - 27 \geq 0$ always, and $= 0$ only at the symmetric point.

So we only need $k \leq \inf R$ over the constraint set (excluding the symmetric point where it's $0/0$, taking limit).

And also $s^2 - 81 \geq 0$? $s = x+y+z \geq 9$ by AM-GM? $x+y+z$ with $1/x+1/y+1/z = 1$... By AM-HM or Cauchy-Schwarz: $(x+y+z)(1/x+1/y+1/z) \geq 9$, so $x+y+z \geq 9$. So $s^2 - 81 \geq 0$. Good, both nonneg, ratio well-defined and $\geq 0$.

So we need $k = \inf R$ over the domain. By uvw, the infimum is achieved in the two-equal case (or at boundary). Let me find $\inf R(t)$ for $t \in (0, 1/2)$.

$R(t) = \frac{4(1+3t-9t^2)}{(1-2t)(6t+1)}$.

Let me find the minimum. Let $N = 1 + 3t - 9t^2$, $D = (1-2t)(6t+1) = 6t + 1 - 12t^2 - 2t = 1 + 4t - 12t^2$.

$R = 4N/D$. $R' = 4(N'D - ND')/D^2$.

$N' = 3 - 18t$. $D' = 4 - 24t$.

$N'D - ND' = (3-18t)(1+4t-12t^2) - (1+3t-9t^2)(4-24t)$.

$(3-18t)(1+4t-12t^2) = 3 + 12t - 36t^2 - 18t - 72t^2 + 216t^3 = 3 - 6t - 108t^2 + 216t^3$.

$(1+3t-9t^2)(4-24t) = 4 - 24t + 12t - 72t^2 - 36t^2 + 216t^3 = 4 - 12t - 108t^2 + 216t^3$.

$N'D - ND' = (3 - 6t - 108t^2 + 216t^3) - (4 - 12t - 108t^2 + 216t^3) = 3 - 6t - 4 + 12t = -1 + 6t$.

So $R' = 0 \iff 6t - 1 = 0 \iff t = 1/6$.

At $t = 1/6$: $N = 1 + 1/2 - 9/36 = 1 + 0.5 - 0.25 = 1.25 = 5/4$. $D = 1 + 4/6 - 12/36 = 1 + 2/3 - 1/3 = 1 + 1/3 = 4/3$. $R = 4 \cdot (5/4)/(4/3) = 5/(4/3) = 15/4 = 3.75$.

Check boundaries: $t \to 0^+$: $N \to 1$, $D \to 1$, $R \to 4$. $t \to 1/2^-$: $N = 1 + 3/2 - 9/4 = 1 + 1.5 - 2.25 = 0.25$, $D = (1-1)(...) = 0$, $D \to 0^+$, $R \to +\infty$.

So $R$ has a minimum at $t = 1/6$ with $R = 15/4$, and $R \to 4$ at $t \to 0$, and $R \to \infty$ at $t \to 1/2$.

Wait, but at $t = 1/6$, is this a minimum? $R' = 4(6t-1)/D^2$. For $t < 1/6$, $R' < 0$ (decreasing). For $t > 1/6$, $R' > 0$ (increasing). So yes, $t = 1/6$ is a minimum with value $15/4$.

But wait, I should check: is the infimum over ALL $(a,b,c)$ achieved at two-equal? By uvw method, for a symmetric inequality, the extremum of a symmetric function under symmetric constraints is achieved when two variables are equal. But here the function $R$ is a ratio, not a polynomial. Let me think more carefully.

Actually, the uvw method says: for a symmetric inequality $f(a,b,c) \geq 0$ where $f$ is a polynomial (or rational function that can be converted), with fixed $a+b+c$, the inequality holds for all iff it holds when two variables are equal. 

The inequality we want to verify is $u^2 + 27v^2 \geq kv$ (for the right $k$), i.e., $u^2 + 27v^2 - kv \geq 0$, with $a+b+c = 1$. This is symmetric and the LHS is a polynomial in $u, v$ (with $u, v$ being the elementary symmetric polynomials). By uvw, since the degree in $v$ is 2 (the $v^2$ term), and... actually uvw says: a symmetric inequality of degree $d$ in variables, expressed in terms of $u, v$ (with $s = a+b+c$ fixed), where the expression is at most quadratic in $v$ (or $u$), then it suffices to check two-equal case.

Here $u^2 + 27v^2 - kv$: as a function of $v$ it's quadratic (degree 2 in $v$), and as function of $u$ it's quadratic. The uvw method: if the inequality is at most degree 2 in $v$ (treating $u$ as the "middle" variable), then it suffices to check boundary (two equal). Actually, let me recall: uvw says if $f$ is at most quadratic in $w$ (the third symmetric polynomial, here $v = abc$), then the inequality $f \geq 0$ need only be checked when two variables are equal or one is zero.

So for $k = 15/4$, we need $u^2 + 27v^2 - \frac{15}{4}v \geq 0$ for all $a+b+c=1$, $a,b,c > 0$. By uvw, check two-equal and boundary.

Two-equal ($b=c=t$): we computed $u^2 + 27v^2 - kv = -4t^3(1-3t)^3 + (4-k) \cdot v(1-27v) \cdot ...$. Hmm, let me recompute directly.

Actually, $u^2 + 27v^2 - kv$ for $b=c=t$: 
$u^2 + 27v^2 = 4t^2 - 12t^3 + 36t^4 - 108t^5 + 108t^6$ (from earlier: $u^2 = 4t^2-12t^3+9t^4$, $27v^2 = 27t^4 - 108t^5 + 108t^6$, sum $= 4t^2 - 12t^3 + 36t^4 - 108t^5 + 108t^6$).
$kv = k(t^2 - 2t^3)$.

$u^2 + 27v^2 - kv = 4t^2 - 12t^3 + 36t^4 - 108t^5 + 108t^6 - kt^2 + 2kt^3$
$= (4-k)t^2 + (2k-12)t^3 + 36t^4 - 108t^5 + 108t^6$
$= t^2[(4-k) + (2k-12)t + 36t^2 - 108t^3 + 108t^4]$.

For $k = 15/4$: $4 - k = 1/4$, $2k - 12 = 15/2 - 12 = -9/2$.

$= t^2[1/4 - 9t/2 + 36t^2 - 108t^3 + 108t^4]$.

Let me check at $t = 1/6$: $1/4 - 9/12 + 36/36 - 108/216 + 108/1296 = 1/4 - 3/4 + 1 - 1/2 + 1/12$.
$= 3/12 - 9/12 + 12/12 - 6/12 + 1/12 = (3 - 9 + 12 - 6 + 1)/12 = 1/12 > 0$.

Hmm, that's positive, not zero. But we expected the minimum of $R$ to be $15/4$ at $t = 1/6$, meaning $R(1/6) = 15/4$, so the ratio equals $15/4$ there, meaning $u^2 + 27v^2 - \frac{15}{4}v = 0$ at $t = 1/6$?

Wait, $R = (u^2 - 81v^2)/(v(1-27v))$... no. Let me recheck. The ratio $R = (s^2 - 81)/(p - 27)$. And $s^2 - 81 = (u^2/v^2) - 81 = (u^2 - 81v^2)/v^2$. $p - 27 = 1/v - 27 = (1-27v)/v$. So $R = \frac{(u^2-81v^2)/v^2}{(1-27v)/v} = \frac{u^2 - 81v^2}{v(1-27v)}$.

And the inequality $s^2 - 81 \geq k(p-27)$ becomes $u^2 - 81v^2 \geq kv(1-27v)$, i.e., $u^2 - 81v^2 - kv + 27kv^2 \geq 0$, i.e., $u^2 + (27k - 81)v^2 - kv \geq 0$.

Oh I see, I had the wrong expression! It's $u^2 + (27k-81)v^2 - kv \geq 0$, not $u^2 + 27v^2 - kv$.

Let me redo. For $k = 4$: $27k - 81 = 108 - 81 = 27$. So $u^2 + 27v^2 - 4v \geq 0$. That's what I had. And we showed it's negative at $t = 0.3$. So $k = 4$ fails. ✓ consistent.

For general $k$: $u^2 + (27k - 81)v^2 - kv \geq 0$.

For two-equal ($b = c = t$):
$u^2 = 4t^2 - 12t^3 + 9t^4$.
$(27k-81)v^2 = (27k-81)(t^4 - 4t^5 + 4t^6)$.
$-kv = -k(t^2 - 2t^3)$.

Sum $= 4t^2 - 12t^3 + 9t^4 + (27k-81)t^4 - 4(27k-81)t^5 + 4(27k-81)t^6 - kt^2 + 2kt^3$
$= (4-k)t^2 + (2k-12)t^3 + (9 + 27k - 81)t^4 - 4(27k-81)t^5 + 4(27k-81)t^6$
$= (4-k)t^2 + (2k-12)t^3 + (27k - 72)t^4 - (108k - 324)t^5 + (108k - 324)t^6$.

Hmm, this is getting messy. Let me instead directly find the infimum of $R(t)$ and verify it's the global infimum.

We found $R(t) = \frac{4(1+3t-9t^2)}{(1-2t)(6t+1)}$ for the two-equal case, with minimum $15/4$ at $t = 1/6$.

But we need to verify this is the global infimum, not just over two-equal. By uvw, the infimum of $R$ (a symmetric function) over the symmetric domain is achieved at two-equal (or boundary). But $R$ is a ratio, not a polynomial. Let me think about this differently.

The condition $k \leq R(a,b,c)$ for all $(a,b,c)$ is equivalent to $u^2 + (27k-81)v^2 - kv \geq 0$ for all $(a,b,c)$ with $a+b+c=1$. This is a symmetric polynomial inequality in $a,b,c$ (expressed via $u, v$). The degree in $v$ is 2. By the uvw theorem, it suffices to check when two variables are equal (and the boundary where one variable is 0, but $a,b,c > 0$ so we check the limit).

So for a given $k$, the inequality holds for all iff it holds for two-equal. The largest $k$ is the infimum of $R(t)$ over two-equal cases (and boundary limits).

We found $\inf_{t \in (0,1/2)} R(t) = 15/4$ at $t = 1/6$. Boundary: $t \to 0$ gives $R \to 4 > 15/4$, $t \to 1/2$ gives $R \to \infty$. So the infimum is $15/4$.

But wait, I should also check the boundary where one of $a, b, c \to 0$ (not just two-equal). When $a \to 0$, $b + c \to 1$, $v = abc \to 0$, $p = 1/v \to \infty$, $s = u/v \to \infty$. The ratio $R = (s^2 - 81)/(p - 27) \approx s^2/p = (u/v)^2/(1/v) = u^2/v \to \infty$ (since $u \to bc > 0$ and $v \to 0$). So $R \to \infty$ at this boundary. Good.

So the global infimum is $15/4$, achieved at the two-equal case $t = 1/6$, i.e., $b = c = 1/6$, $a = 1 - 1/3 = 2/3$.

Let me verify: $a = 2/3, b = c = 1/6$. $x = 3/2, y = z = 6$. Check constraint: $1/x + 1/y + 1/z = 2/3 + 1/6 + 1/6 = 2/3 + 1/3 = 1$. ✓.

$s = 3/2 + 6 + 6 = 13.5 = 27/2$. $s^2 = 729/4$. $s^2 - 81 = 729/4 - 324/4 = 405/4$.
$p = xy + yz + zx = (3/2)(6) + 36 + (3/2)(6) = 9 + 36 + 9 = 54$. $p - 27 = 27$.
$R = (405/4)/27 = 405/108 = 15/4$. ✓.

So $k = 15/4$.

Now I need to prove that $k = 15/4$ works, i.e., $(x+y+z)^2 - 81 \geq \frac{15}{4}(xy+yz+zx - 27)$ for all $x,y,z > 0$ with $xy+yz+zx = xyz$.

Equivalently (in terms of $a,b,c$ with $a+b+c=1$): $u^2 + (27 \cdot 15/4 - 81)v^2 - \frac{15}{4}v \geq 0$.

$27 \cdot 15/4 - 81 = 405/4 - 324/4 = 81/4$.

So we need $u^2 + \frac{81}{4}v^2 - \frac{15}{4}v \geq 0$, i.e., $4u^2 + 81v^2 - 15v \geq 0$.

With $u = ab+bc+ca$, $v = abc$, $a+b+c = 1$, $a,b,c > 0$.

By uvw (degree 2 in $v$), suffices to check $b = c = t$, $a = 1-2t$.

$4u^2 + 81v^2 - 15v$:
$4u^2 = 4(2t-3t^2)^2 = 4(4t^2 - 12t^3 + 9t^4) = 16t^2 - 48t^3 + 36t^4$.
$81v^2 = 81(t^2-2t^3)^2 = 81t^4 - 324t^5 + 324t^6$.
$-15v = -15t^2 + 30t^3$.

Sum $= 16t^2 - 48t^3 + 36t^4 + 81t^4 - 324t^5 + 324t^6 - 15t^2 + 30t^3$
$= t^2 - 18t^3 + 117t^4 - 324t^5 + 324t^6$
$= t^2(1 - 18t + 117t^2 - 324t^3 + 324t^4)$.

Let me factor $h(t) = 1 - 18t + 117t^2 - 324t^3 + 324t^4$.

Check $t = 1/6$: $1 - 3 + 117/36 - 324/216 + 324/1296 = 1 - 3 + 13/4 - 3/2 + 1/4$.
$= 1 - 3 + 3.25 - 1.5 + 0.25 = 0$. So $(6t - 1)$ or $(t - 1/6)$ is a factor. Since it's the minimum, likely a double root.

$h'(t) = -18 + 234t - 972t^2 + 1296t^3$. $h'(1/6) = -18 + 39 - 27 + 6 = 0$. So double root at $t = 1/6$, i.e., $(6t-1)^2$ factor.

$h(t) = 324t^4 - 324t^3 + 117t^2 - 18t + 1$. Divide by $(6t-1)^2 = 36t^2 - 12t + 1$.

$324t^4 - 324t^3 + 117t^2 - 18t + 1 = (36t^2 - 12t + 1)(At^2 + Bt + C)$.

$(36t^2 - 12t + 1)(At^2 + Bt + C) = 36At^4 + (36B - 12A)t^3 + (36C - 12B + A)t^2 + (-12C + B)t + C$.

Match:
- $t^4$: $36A = 324 \Rightarrow A = 9$.
- $t^3$: $36B - 12A = -324 \Rightarrow 36B - 108 = -324 \Rightarrow 36B = -216 \Rightarrow B = -6$.
- $t^2$: $36C - 12B + A = 117 \Rightarrow 36C + 72 + 9 = 117 \Rightarrow 36C = 36 \Rightarrow C = 1$.
- $t^1$: $-12C + B = -12 - 6 = -18$. ✓
- $t^0$: $C = 1$. ✓

So $h(t) = (6t-1)^2(9t^2 - 6t + 1) = (6t-1)^2(3t-1)^2$.

So $4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0$. ✓

Equality at $t = 1/6$ (i.e., $a = 2/3, b = c = 1/6$) and $t = 1/3$ (i.e., $a = b = c = 1/3$), and $t = 0$ (boundary).

So for the two-equal case, $4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0$. ✓

By uvw, since the expression $4u^2 + 81v^2 - 15v$ is symmetric and at most degree 2 in $v$ (with $a+b+c$ fixed), the inequality holds for all $a,b,c > 0$ with $a+b+c = 1$.

Therefore $k = 15/4$ is the largest value.

Wait, I should make sure I'm applying uvw correctly. Let me recall the uvw theorem precisely.

**UVW Theorem**: For a symmetric inequality $f(a,b,c) \geq 0$ where $f$ is a polynomial, if we fix $a + b + c = s$ and the inequality can be written as a function of $u = ab+bc+ca$ and $v = abc$ that is at most quadratic in $v$, then the inequality holds for all $a,b,c \geq 0$ with $a+b+c = s$ if and only if it holds when two of the variables are equal (including the case when one is 0).

Our expression: $F = 4u^2 + 81v^2 - 15v$. As a function of $v$ (with $u$ free), it's $81v^2 - 15v + 4u^2$, which is quadratic in $v$. ✓

So by uvw, $F \geq 0$ for all $a,b,c \geq 0$ with $a+b+c = 1$ iff $F \geq 0$ when two are equal. We verified the two-equal case. Also need to check the boundary $a = 0$: then $u = bc$, $v = 0$, $F = 4b^2c^2 \geq 0$. ✓ (and $b + c = 1$).

So the proof is complete. $k = 15/4$.

Actually, let me also make sure the answer is exactly $15/4$ and not that we need to also consider the case $p - 27 < 0$. We showed $p = 1/v \geq 27$ always (since $v \leq 1/27$), so $p - 27 \geq 0$ always. And $s^2 - 81 \geq 0$ always. So the ratio is always well-defined and nonneg, and we need $k \leq \inf R = 15/4$.

Let me also double-check that $k = 15/4$ is achievable (tight), i.e., equality holds at some point. At $a = 2/3, b = c = 1/6$ (i.e., $x = 3/2, y = z = 6$), we have $R = 15/4$ exactly, so equality holds. ✓

Great, the answer is $k = \boxed{15/4}$.

Now let me write up the proof cleanly.

Let me also verify the uvw application once more. The standard uvw method: A symmetric homogeneous... wait, our expression isn't homogeneous. $4u^2 + 81v^2 - 15v$: $u^2$ has degree 4 in $a,b,c$, $v^2$ has degree 6, $v$ has degree 3. Not homogeneous. But uvw doesn't require homogeneity when $a+b+c$ is fixed.

The uvw method (as commonly stated): Given $a+b+c = s$ fixed, a symmetric function $f(a,b,c)$ can be expressed as $g(u, v)$ where $u = ab+bc+ca$, $v = abc$. If $g$ is at most quadratic in $v$, then for fixed $s$ and $u$, $g$ is a quadratic in $v$, and the extremum of $g$ over the feasible $(u,v)$ region is achieved at the boundary of the feasible region, which corresponds to two variables being equal.

More precisely: for fixed $s$ and $u$, $v$ ranges over an interval $[v_{\min}, v_{\max}]$, and the endpoints correspond to two variables being equal (or one being 0). A quadratic in $v$ achieves its minimum either at the vertex (interior) or at endpoints. If the quadratic is convex (coefficient of $v^2$ positive), the minimum could be interior. Hmm, so uvw doesn't directly say it suffices to check two-equal for a convex quadratic.

Wait, let me reconsider. The coefficient of $v^2$ is $81 > 0$, so $g(u,v) = 81v^2 - 15v + 4u^2$ is convex in $v$. The minimum over $v$ for fixed $u$ is at $v = 15/(162) = 5/54$, which might be interior. So uvw in the simple form might not directly apply.

Hmm, but actually the uvw theorem is more nuanced. Let me recall it properly.

The uvw method states: For a symmetric inequality $f(a,b,c) \geq 0$ with $a+b+c$ fixed, if $f$ expressed as $g(u,v)$ is at most degree 2 in $v$, then:
- If $g$ is concave in $v$ (coefficient of $v^2 \leq 0$), the minimum is at the boundary (two equal), so check two-equal.
- If $g$ is convex in $v$ (coefficient of $v^2 > 0$), the minimum could be interior, and we need to check the critical point as well.

Hmm, so for convex case, we might need additional analysis. But actually, there's a stronger version:

**Theorem (uvw)**: A symmetric inequality $f(a,b,c) \geq 0$ with $f$ at most degree 2 in $v$ (with $s = a+b+c$ fixed) holds for all real $a,b,c$ with $a+b+c = s$ iff it holds when two variables are equal.

This is because: for fixed $s$, the feasible region in $(u,v)$ space is bounded by curves corresponding to two-equal cases. A function at most quadratic in $v$ ... actually I think the correct statement involves the fact that the boundary of the feasible $(u,v)$ region is exactly the two-equal curve, and for a quadratic in $v$, the minimum over the region is on the boundary.

Let me think again. For fixed $s = 1$, the feasible $(u, v)$ region: $u \in [0, 1/3]$, and for each $u$, $v$ ranges in $[v_1(u), v_2(u)]$ where $v_1, v_2$ correspond to two-equal configurations. The function $g(u,v) = 4u^2 + 81v^2 - 15v$.

For fixed $u$, $g$ is convex in $v$ (min at $v^* = 15/162 = 5/54$). If $v^* \in [v_1(u), v_2(u)]$, the min for that $u$ is $g(u, v^*) = 4u^2 + 81(5/54)^2 - 15(5/54) = 4u^2 + 81 \cdot 25/2916 - 75/54 = 4u^2 + 25/36 - 25/18 = 4u^2 - 25/36$.

This is minimized at $u = 0$: $-25/36 < 0$. But is $v^* = 5/54$ feasible when $u = 0$? When $u = 0$, we need $ab + bc + ca = 0$ with $a+b+c = 1$, $a,b,c \geq 0$. This means at most one variable is nonzero, so $v = 0$. So $v^* = 5/54$ is not feasible at $u = 0$.

So the feasibility constraint matters. The point is that $v^*$ might not be in the feasible range for all $u$.

This is getting complicated. Let me just directly prove $4u^2 + 81v^2 - 15v \geq 0$ for $a+b+c=1$, $a,b,c \geq 0$ using a different method, or verify the uvw application more carefully.

Actually, let me use a direct approach. We have the identity for two-equal case: $4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0$. 

For the general case, let me try to express $4u^2 + 81v^2 - 15v$ as a sum of squares or use Schur's inequality.

Schur's inequality: For $a+b+c = 1$, $a^3+b^3+c^3 + abc \geq ab(a+b) + bc(b+c) + ca(c+a)$, i.e., $1 - 3u + 3v + v \geq u - 3v$... let me recall. $a^3+b^3+c^3 = (a+b+c)^3 - 3(a+b+c)u + 3v = 1 - 3u + 3v$. Schur (degree 1, i.e., $t=1$): $a^3+b^3+c^3 + abc \geq \sum ab(a+b)$. $\sum ab(a+b) = \sum(a^2b + ab^2) = (a+b+c)u - 3v = u - 3v$. So Schur: $(1-3u+3v) + v \geq u - 3v$, i.e., $1 - 3u + 4v \geq u - 3v$, i.e., $1 - 4u + 7v \geq 0$.

Hmm, not sure that directly helps.

Let me try another approach. We want to show $4u^2 + 81v^2 \geq 15v$ for $a+b+c=1$, $a,b,c \geq 0$.

By AM-GM or other inequalities... Let me think about what relationships between $u$ and $v$ we have.

We know $u \leq 1/3$ (since $u = (1 - (a^2+b^2+c^2))/2 \leq (1 - 1/3)/2 = 1/3$).
We know $v \leq 1/27$.
We know $u^2 \geq 3v$ (since $(ab+bc+ca)^2 \geq 3abc(a+b+c) = 3v$). This is a well-known inequality: $u^2 \geq 3sv = 3v$ (with $s=1$).

So $4u^2 \geq 12v$. Then $4u^2 + 81v^2 - 15v \geq 12v + 81v^2 - 15v = 81v^2 - 3v = 3v(27v - 1)$.

Since $v \leq 1/27$, $27v - 1 \leq 0$, so $3v(27v - 1) \leq 0$. This goes the wrong way! So $u^2 \geq 3v$ is not enough.

Let me try a tighter bound. We need to use the relationship between $u$ and $v$ more precisely.

Actually, let me just use the uvw method properly. The key theorem:

**Theorem**: Let $f(a,b,c)$ be a symmetric function with $a+b+c$ fixed. Write $f = g(u,v)$. If $\frac{\partial^2 g}{\partial v^2} \geq 0$ (convex in $v$) or $\leq 0$ (concave), then the extrema of $f$ are achieved when two variables are equal or one is zero.

Wait, I think the correct statement is: regardless of convexity, if $g$ is at most degree 2 in $v$, then the minimum of $f$ is achieved when two variables are equal or at the boundary. This is because the feasible region in $(u,v)$ has boundary given by the two-equal curve, and a quadratic function's minimum over a compact region is either at a critical point interior to the region or on the boundary.

If the minimum is interior, then $\partial g/\partial u = 0$ and $\partial g/\partial v = 0$. $\partial g/\partial v = 162v - 15 = 0 \Rightarrow v = 5/54$. $\partial g/\partial u = 8u = 0 \Rightarrow u = 0$. But $u = 0, v = 5/54$ is not feasible (as we noted, $u=0$ forces $v = 0$). So there's no interior critical point, and the minimum is on the boundary, i.e., two-equal case.

That's the key! The interior critical point $(u,v) = (0, 5/54)$ is not feasible, so the minimum is on the boundary (two-equal or one-zero). We checked both: two-equal gives $t^2(6t-1)^2(3t-1)^2 \geq 0$, and one-zero ($a=0$) gives $4u^2 \geq 0$.

So the proof works. Let me also verify: is the feasible region in $(u,v)$ such that the boundary is exactly the two-equal curve (plus the $v=0$ boundary)? Yes, for $a+b+c = 1$, $a,b,c \geq 0$, the feasible $(u,v)$ region is bounded by:
- $v = 0$ (when one variable is 0)
- The two-equal curve (when two variables are equal)

And the interior of the region corresponds to three distinct positive values. The minimum of a continuous function on a compact set is achieved; if not at an interior critical point, it's on the boundary.

Actually, the feasible region might not be compact in a nice way, but since $a,b,c \geq 0$ and $a+b+c=1$, it's a compact simplex, and $u, v$ are continuous functions, so the image is compact. The function $g(u,v)$ is continuous, so it achieves its minimum. If the minimum is at an interior point of the feasible $(u,v)$ region, then the gradient must vanish there, which we showed doesn't happen (the critical point is infeasible). So the minimum is on the boundary.

Hmm, but "interior of the feasible $(u,v)$ region" — I need to be more careful. The map $(a,b,c) \to (u,v)$ is not injective; the feasible $(u,v)$ region is the image. An interior point of the image could correspond to a boundary point of the simplex. But actually, the boundary of the simplex ($a=0$ or $b=0$ or $c=0$) maps to $v = 0$, which is the boundary of the image. And the two-equal cases map to the other boundary curve. So the interior of the image corresponds to the interior of the simplex (all variables distinct and positive). At an interior minimum, by Lagrange multipliers, the gradient of $g$ w.r.t. $(u,v)$ must be proportional to the gradient of the constraint... 

Actually, this is getting too complicated for a clean proof. Let me just use the standard uvw theorem as a lemma and cite it.

Alternatively, I can prove it directly. Let me try to express $4u^2 + 81v^2 - 15v$ as a sum of nonneg terms.

We have the two-equal factorization: $t^2(6t-1)^2(3t-1)^2$. This suggests the expression might be related to discriminant-like quantities.

Let me try the substitution $p = a - b$, $q = b - c$ (or use the Schur-like approach).

Actually, let me try to use the SOS (sum of squares) approach or find a direct proof.

We want: $4(ab+bc+ca)^2 + 81(abc)^2 \geq 15abc$ with $a+b+c = 1$.

Let me substitute $a+b+c = 1$ and use $u = ab+bc+ca$, $v = abc$.

We know that $a,b,c$ are roots of $t^3 - t^2 + ut - v = 0$. For three real nonneg roots, the discriminant must be $\geq 0$:
$\Delta = 18 \cdot 1 \cdot u \cdot v - 4u^3 + u^2 - 4v - 27v^2 \geq 0$ (discriminant of $t^3 - t^2 + ut - v$).

Wait, the discriminant of $t^3 + pt^2 + qt + r$ is $\Delta = 18pqr - 4p^3r + p^2q^2 - 4q^3 - 27r^2$. Here $p = -1, q = u, r = -v$:
$\Delta = 18(-1)(u)(-v) - 4(-1)^3(-v) + (-1)^2 u^2 - 4u^3 - 27(-v)^2$
$= 18uv - 4v + u^2 - 4u^3 - 27v^2$.

For three real roots, $\Delta \geq 0$: $u^2 - 4u^3 + 18uv - 4v - 27v^2 \geq 0$.

Hmm, this gives a relationship but I'm not sure how to use it directly.

Let me try yet another approach. Let me just prove it using the uvw method and state the lemma clearly.

Actually, you know what, let me try to find a direct SOS proof.

$4u^2 + 81v^2 - 15v \geq 0$ with $a+b+c = 1$.

Let me write $v = abc$ and use $a+b+c=1$.

$15abc = 15abc(a+b+c) = 15(a^2bc + ab^2c + abc^2)$... no, $abc \cdot 1 = abc(a+b+c) = a^2bc + ab^2c + abc^2$. So $15v = 15(a^2bc + ab^2c + abc^2)$.

$4u^2 = 4(ab+bc+ca)^2 = 4(a^2b^2 + b^2c^2 + c^2a^2 + 2abc(a+b+c)) = 4(a^2b^2+b^2c^2+c^2a^2) + 8abc$.

So $4u^2 + 81v^2 - 15v = 4(a^2b^2+b^2c^2+c^2a^2) + 8abc + 81a^2b^2c^2 - 15(a^2bc + ab^2c + abc^2)$.

$= 4(a^2b^2+b^2c^2+c^2a^2) - 15abc(a+b+c) + 8abc + 81a^2b^2c^2$

Wait, $-15v = -15abc$, and $15abc = 15abc \cdot 1 = 15abc(a+b+c)$. So:

$4u^2 + 81v^2 - 15v = 4(a^2b^2+b^2c^2+c^2a^2) + 8abc + 81a^2b^2c^2 - 15abc$
$= 4(a^2b^2+b^2c^2+c^2a^2) - 7abc + 81a^2b^2c^2$.

Hmm, $8abc - 15abc = -7abc$. So:

$F = 4(a^2b^2+b^2c^2+c^2a^2) - 7abc + 81a^2b^2c^2$.

With $a+b+c = 1$. Let me see if this can be written as SOS.

$4(a^2b^2+b^2c^2+c^2a^2) - 7abc + 81a^2b^2c^2$.

Let $p = ab, q = bc, r = ca$. Then $p + q + r = u$, $pqr = (abc)^2 = v^2$, and $p, q, r \geq 0$. Also $a + b + c = 1$ gives... $p, q, r$ are not independent; they satisfy $pr/q = a^2$ etc. Actually $pqr = v^2$ and $p + q + r = u$.

$F = 4(p^2 + q^2 + r^2) - 7\sqrt{pqr} \cdot ... $ no, $abc = v = \sqrt{pqr}$... this is getting messy.

Let me try a different substitution. Since we know equality at $(2/3, 1/6, 1/6)$ and permutations, and at $(1/3, 1/3, 1/3)$, let me try to express $F$ in terms of deviations.

Actually, let me just go with the uvw approach and state it as a lemma. The proof is clean enough.

Let me reconsider. Actually, I realize I should double-check the uvw theorem statement. The standard result is:

**UVW Lemma**: Let $f(a,b,c)$ be a symmetric function, and suppose $a+b+c = s$ is fixed. If $f$, when expressed as $g(u, v)$ where $u = ab+bc+ca$, $v = abc$, is a polynomial of degree at most 2 in $v$, then $f$ achieves its maximum and minimum on the set $\{(a,b,c) : a+b+c = s, a,b,c \geq 0\}$ when two of the variables are equal (or one is zero).

This is because: the set of feasible $(u,v)$ is a compact region whose boundary consists of the curve where two variables are equal and the line $v = 0$. The function $g(u,v)$, being quadratic in $v$, has the property that on any line $u = \text{const}$, it's a quadratic in $v$, so its minimum on that line segment is at an endpoint or at the vertex. If at the vertex, then $\partial g / \partial v = 0$ there. But we also need to optimize over $u$. The overall minimum is either on the boundary of the feasible region, or at an interior point where $\nabla g = 0$. We check that $\nabla g = 0$ has no feasible solution, so the minimum is on the boundary.

$\nabla g = (8u, 162v - 15) = (0, 0)$ gives $u = 0, v = 5/54$. But $u = 0$ with $a+b+c = 1, a,b,c \geq 0$ means at most one variable is positive, so $v = 0 \neq 5/54$. Infeasible. ✓

So the minimum is on the boundary: either $v = 0$ (one variable zero) or two variables equal. We check both and find $F \geq 0$. ✓

OK so the proof is solid. Let me write it up.

Actually, I realize I should present this more carefully. Let me structure the proof:

1. Substitution $a = 1/x, b = 1/y, c = 1/z$ transforms constraint to $a+b+c=1$.
2. Express the inequality in terms of $u = ab+bc+ca$, $v = abc$.
3. Show the inequality becomes $4u^2 + 81v^2 - 15v \geq 0$ (for $k = 15/4$).
4. Use uvw to reduce to two-equal case.
5. Verify two-equal case factors as $t^2(6t-1)^2(3t-1)^2 \geq 0$.
6. Show $k = 15/4$ is tight (equality at $a = 2/3, b = c = 1/6$).

Let me also verify the direction: we need the LARGEST $k$. Since $p - 27 \geq 0$ always, larger $k$ makes the inequality harder to satisfy. So the largest $k$ that works is the infimum of the ratio, which is $15/4$.

Let me write the proof.

Hmm, actually let me reconsider step 2 more carefully. The inequality is $(x+y+z)^2 - 81 \geq k(xy + yz + zx - 27)$.

With $a = 1/x$ etc., $a+b+c = 1$:
- $x + y + z = 1/a + 1/b + 1/c = (ab+bc+ca)/(abc) = u/v$.
- $xy + yz + zx = 1/(ab) + 1/(bc) + 1/(ca) = (a+b+c)/(abc) = 1/v$.

So $(x+y+z)^2 - 81 = u^2/v^2 - 81 = (u^2 - 81v^2)/v^2$.
$xy+yz+zx - 27 = 1/v - 27 = (1 - 27v)/v$.

Inequality: $(u^2 - 81v^2)/v^2 \geq k(1-27v)/v$, i.e., $u^2 - 81v^2 \geq kv(1-27v)$ (multiplying by $v^2 > 0$).

$u^2 - 81v^2 - kv + 27kv^2 \geq 0$, i.e., $u^2 + (27k - 81)v^2 - kv \geq 0$.

For $k = 15/4$: $27 \cdot 15/4 - 81 = 405/4 - 324/4 = 81/4$. So $u^2 + \frac{81}{4}v^2 - \frac{15}{4}v \geq 0$, i.e., $4u^2 + 81v^2 - 15v \geq 0$. ✓

Now, we also need to verify that $1 - 27v \geq 0$, i.e., $v \leq 1/27$. By AM-GM, $v = abc \leq ((a+b+c)/3)^3 = 1/27$. ✓ And $1 - 27v \geq 0$ means $p - 27 \geq 0$, so the direction is correct: we need $k \leq$ ratio.

Also $u^2 - 81v^2 \geq 0$? $u^2/v^2 = (x+y+z)^2 \geq 81$? We need $x + y + z \geq 9$. By Cauchy-Schwarz: $(x+y+z)(1/x + 1/y + 1/z) \geq 9$, and $1/x + 1/y + 1/z = 1$, so $x+y+z \geq 9$. ✓ So $u^2/v^2 \geq 81$, i.e., $u^2 \geq 81v^2$, i.e., $u^2 - 81v^2 \geq 0$. ✓

So both sides nonneg, and we need $k \leq \inf \frac{u^2 - 81v^2}{v(1-27v)}$.

The infimum is $15/4$, achieved at $a = 2/3, b = c = 1/6$.

Now let me write the clean proof.

Let me also verify the two-equal computation once more. $b = c = t$, $a = 1 - 2t$, $t \in [0, 1/2]$.

$u = ab + bc + ca = (1-2t)t + t^2 + (1-2t)t = 2t(1-2t) + t^2 = 2t - 4t^2 + t^2 = 2t - 3t^2$.
$v = abc = (1-2t) \cdot t \cdot t = t^2(1-2t) = t^2 - 2t^3$.

$4u^2 = 4(2t - 3t^2)^2 = 4(4t^2 - 12t^3 + 9t^4) = 16t^2 - 48t^3 + 36t^4$.
$81v^2 = 81(t^2 - 2t^3)^2 = 81(t^4 - 4t^5 + 4t^6) = 81t^4 - 324t^5 + 324t^6$.
$-15v = -15(t^2 - 2t^3) = -15t^2 + 30t^3$.

Sum: $(16 - 15)t^2 + (-48 + 30)t^3 + (36 + 81)t^4 - 324t^5 + 324t^6$
$= t^2 - 18t^3 + 117t^4 - 324t^5 + 324t^6$
$= t^2(1 - 18t + 117t^2 - 324t^3 + 324t^4)$.

Factor: $324t^4 - 324t^3 + 117t^2 - 18t + 1$.

We showed $= (6t-1)^2(3t-1)^2$. Let me verify: $(6t-1)^2 = 36t^2 - 12t + 1$. $(3t-1)^2 = 9t^2 - 6t + 1$.

$(36t^2 - 12t + 1)(9t^2 - 6t + 1) = 324t^4 - 216t^3 + 36t^2 - 108t^3 + 72t^2 - 12t + 9t^2 - 6t + 1$
$= 324t^4 - 324t^3 + (36 + 72 + 9)t^2 + (-12 - 6)t + 1$
$= 324t^4 - 324t^3 + 117t^2 - 18t + 1$. ✓

So $4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0$. ✓

Now for the boundary $v = 0$ (one variable zero, say $a = 0$): $u = bc$, $v = 0$. $4u^2 + 81v^2 - 15v = 4b^2c^2 \geq 0$. ✓

Great. The proof is complete. Let me write it up properly.

One more thing: I need to justify the uvw reduction clearly. Let me state it as a lemma and prove it briefly.

**Lemma (uvw)**: Let $s > 0$ and let $g(u, v)$ be a polynomial in $u$ and $v$. Consider the problem of minimizing $g(u,v)$ over the set $\mathcal{F} = \{(u,v) : \exists\, a,b,c \geq 0,\, a+b+c = s,\, ab+bc+ca = u,\, abc = v\}$. If $g$ is at most degree 2 in $v$, and the system $\partial g/\partial u = 0$, $\partial g/\partial v = 0$ has no solution in the interior of $\mathcal{F}$, then the minimum is achieved on the boundary of $\mathcal{F}$, which corresponds to either $v = 0$ (one variable zero) or two variables being equal.

*Proof sketch*: $\mathcal{F}$ is compact (image of compact simplex). $g$ is continuous, so achieves its min. If the min is at an interior point of $\mathcal{F}$, then since the map $(a,b,c) \mapsto (u,v)$ is a submersion in the interior (three distinct positive roots), the min would require $\nabla g = 0$, contradicting the assumption. So min is on boundary. The boundary of $\mathcal{F}$ corresponds to the discriminant being zero (two equal roots) or $v = 0$ (one root zero).

Actually, I think I can avoid stating the full lemma and just argue directly for our specific case. Let me think about the cleanest presentation.

Alternative direct proof without uvw: 

We want to show $4u^2 + 81v^2 - 15v \geq 0$ for $a+b+c = 1$, $a,b,c \geq 0$.

Approach: Fix $v$ and find the minimum of $u$ given $a+b+c=1$ and $abc = v$. By Lagrange multipliers, the extremum of $u$ subject to $a+b+c=1$ and $abc = v$ occurs when two variables are equal (standard result). So for fixed $v$, $u$ ranges between $u_{\min}(v)$ and $u_{\max}(v)$, both achieved when two variables are equal.

Since $4u^2 + 81v^2 - 15v$ is increasing in $u$ for $u \geq 0$ (as $8u \geq 0$), the minimum over $u$ for fixed $v$ is at $u = u_{\min}(v)$, which is achieved when two variables are equal.

So the global minimum is achieved when two variables are equal. This is a cleaner argument!

Wait, is $u_{\min}(v)$ achieved at two-equal? For fixed $a+b+c = 1$ and $abc = v$, the extrema of $u = ab+bc+ca$ are achieved when two variables are equal. Yes, this is standard (by Lagrange multipliers: $\nabla(u - \lambda(a+b+c) - \mu(abc)) = 0$ gives $b+c - \lambda - \mu bc = 0$, etc., subtracting pairs gives $(a-b)(\mu c - 1) = 0$, so either $a = b$ or $\mu c = 1$, etc., leading to two equal).

And since $F = 4u^2 + 81v^2 - 15v$ is increasing in $u$ (for $u \geq 0$, which holds since $a,b,c \geq 0$), the minimum for fixed $v$ is at $u_{\min}(v)$, the two-equal case.

But wait, for fixed $v$, there might be two two-equal configurations (one with $a = b \neq c$ and the "other branch"). We need to check both. Actually, for fixed $v$ and $a+b+c = 1$, the two-equal cases give specific $(u, v)$ pairs, and as $t$ varies, we trace out the boundary. The minimum of $F$ over all two-equal cases gives the global minimum.

Since we showed $F = t^2(6t-1)^2(3t-1)^2 \geq 0$ for all two-equal cases, and $F$ is increasing in $u$ (so the minimum for each $v$ is at the two-equal case), the global minimum is $\geq 0$.

Hmm, but I need to be a bit more careful. For fixed $v$, $u_{\min}$ is achieved at two-equal, and $F(u_{\min}(v), v) \geq 0$ (since it's a two-equal case). And $F(u, v) \geq F(u_{\min}(v), v) \geq 0$ for all $u \geq u_{\min}(v)$. So $F \geq 0$ everywhere. ✓

This is clean. But I need to also handle the case $v = 0$ (where $u_{\min}$ might not be two-equal but rather one-zero). Actually when $v = 0$, one variable is 0, and $u = bc$ with $b + c = 1$, $u \in [0, 1/4]$. $F = 4u^2 \geq 0$. ✓

OK let me just write the proof now. I'll use the approach: substitute, reduce to two-equal by the monotonicity in $u$ argument, verify two-equal.

Let me write it up.

---

**Proof.**

Let $a = 1/x, b = 1/y, c = 1/z$. The constraint $xy + yz + zx = xyz$ becomes $a + b + c = 1$ with $a, b, c > 0$.

Let $u = ab + bc + ca$ and $v = abc$. Then:
- $x + y + z = \frac{u}{v}$,
- $xy + yz + zx = \frac{1}{v}$.

The inequality becomes $\frac{u^2}{v^2} - 81 \geq k\left(\frac{1}{v} - 27\right)$, i.e., $u^2 - 81v^2 \geq kv(1 - 27v)$ (after multiplying by $v^2 > 0$).

**Claim:** The largest $k$ is $\frac{15}{4}$.

First, note that $v \leq \frac{1}{27}$ by AM-GM, so $1 - 27v \geq 0$. Also $x + y + z \geq 9$ by Cauchy-Schwarz ($(x+y+z)(1/x+1/y+1/z) \geq 9$), so $u^2 - 81v^2 \geq 0$. Thus the ratio $R = \frac{u^2 - 81v^2}{v(1-27v)}$ is well-defined and nonneg (away from $v = 1/27$), and we seek $k = \inf R$.

**Step 1: Reduction to two equal variables.** For fixed $v = abc$ and $a + b + c = 1$, the function $F = 4u^2 + 81v^2 - 15v$ is increasing in $u$ (since $\partial F/\partial u = 8u \geq 0$). The minimum of $u$ subject to $a + b + c = 1$, $abc = v$ is achieved when two variables are equal (by Lagrange multipliers). Hence the global minimum of $F$ is achieved when two of $a, b, c$ are equal.

**Step 2: Verification for two equal.** Set $b = c = t$, $a = 1 - 2t$, $t \in [0, 1/2]$. Then $u = 2t - 3t^2$, $v = t^2 - 2t^3$, and:

$$4u^2 + 81v^2 - 15v = t^2(6t-1)^2(3t-1)^2 \geq 0.$$

This confirms $k = 15/4$ works.

**Step 3: Tightness.** At $t = 1/6$ (i.e., $a = 2/3, b = c = 1/6$, corresponding to $x = 3/2, y = z = 6$), we have $4u^2 + 81v^2 - 15v = 0$, so equality holds and $k$ cannot exceed $15/4$.

Therefore $k = \frac{15}{4}$.

### PROOF COMPLETE

---

Wait, I need to double-check the reduction argument in Step 1. The issue: for fixed $v$, $F$ is increasing in $u$, so min of $F$ is at min of $u$. Min of $u$ (given constraints) is at two-equal. But does every value of $v$ correspond to a two-equal configuration? 

For $v \in (0, 1/27]$, yes: the two-equal family $b = c = t$, $a = 1-2t$ gives $v = t^2(1-2t)$ which ranges over $(0, 1/27]$ as $t$ ranges over $(0, 1/2)$ (with max $1/27$ at $t = 1/3$). Actually $v = t^2(1-2t)$: at $t = 0$, $v = 0$; at $t = 1/3$, $v = 1/27$; at $t = 1/2$, $v = 0$. So $v$ ranges over $[0, 1/27]$, covering each value (possibly twice). So for each $v \in [0, 1/27]$, there's a two-equal configuration. ✓

And the min of $u$ for fixed $v$ is achieved at one of these two-equal configs. So the argument works.

Actually, I realize there's a subtlety: for a given $v$, there are two two-equal configurations (one with $t < 1/3$ and one with $t > 1/3$, giving different $u$ values). The minimum $u$ is one of them. Since $F$ is increasing in $u$, we want the smaller $u$. But we check $F \geq 0$ for ALL two-equal configs (all $t$), so both branches are covered. ✓

OK the proof is correct. Let me finalize.

Actually, let me reconsider whether the "increasing in $u$" argument fully works. $F = 4u^2 + 81v^2 - 15v$. For fixed $v$, $F$ is a function of $u$ only through $4u^2$, which is increasing for $u \geq 0$ and decreasing for $u \leq 0$. Since $u = ab + bc + ca \geq 0$ (as $a, b, c \geq 0$), $F$ is increasing in $u$. ✓

So for fixed $v$, $\min_u F = F(u_{\min}(v), v)$ where $u_{\min}(v)$ is the minimum of $u$ over the constraint set. And $u_{\min}(v)$ is achieved at a two-equal point. We verify $F \geq 0$ at all two-equal points, so $F(u_{\min}(v), v) \geq 0$ for all $v$, hence $F \geq 0$ everywhere. ✓

The proof is complete and correct. Let me finalize the write-up.

Let me reconsider: I want to make sure the Lagrange multiplier argument for "min of $u$ at fixed $v$ and $a+b+c=1$ is at two-equal" is correct.

We minimize $u = ab + bc + ca$ subject to $a + b + c = 1$ and $abc = v$, with $a, b, c \geq 0$.

Lagrange: $L = ab + bc + ca - \lambda(a + b + c - 1) - \mu(abc - v)$.
$\partial L / \partial a = b + c - \lambda - \mu bc = 0$
$\partial L / \partial b = a + c - \lambda - \mu ac = 0$
$\partial L / \partial c = a + b - \lambda - \mu ab = 0$

Subtract first two: $(b + c) - (a + c) - \mu(bc - ac) = 0 \Rightarrow (b - a)(1 - \mu c) = 0$.
So either $a = b$ or $\mu c = 1$.
Similarly, either $b = c$ or $\mu a = 1$, and either $a = c$ or $\mu b = 1$.

If all three are distinct, then $\mu a = \mu b = \mu c = 1$, so $a = b = c$, contradiction. So at least two are equal. ✓

(At boundary, one variable could be 0, which is the $v = 0$ case, handled separately.)

Great, the proof is rigorous. Let me write the final version.
