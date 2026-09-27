# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Find the largest value of $k$ such that the following inequality holds for all $x, y, z > 0$ with $xyz = 1$:
\[
\sum_{cyc} \frac{x}{xy+1} + \frac{k}{\sqrt[3]{xy^2 + yz^2 + zx^2}} \ge \frac{3}{2} + \frac{k}{\sqrt[3]{3}}
\]
Let $k_{max}$ be this maximum value. Find $(2 \cdot k_{max})^3$.       — 题目文本
#   To find the largest $k$, we examine the limit of the expression as $x \to \infty$ with $y = 1$ and $z = 1/x$. 
The sum $\sum \frac{x}{xy+1}$ approaches $1 + 1 + 0 = 2$. 
The expression $\sum xy^2$ becomes $x + \frac{1}{x^2} + x$, which approaches $2x$ and thus $\frac{1}{\sqrt[3]{\sum xy^2}}$ approaches 0.
The inequality then requires $2 \ge \frac{3}{2} + \frac{k}{\sqrt[3]{3}}$, which simplifies to $\frac{1}{2} \ge \frac{k}{\sqrt[3]{3}}$, or $k \le \frac{\sqrt[3]{3}}{2}$.
The solution confirms that $k_{max} = \frac{\sqrt[3]{3}}{2}$. 
Therefore, $(2 \cdot k_{max})^3 = (2 \cdot \frac{\sqrt[3]{3}}{2})^3 = (\sqrt[3]{3})^3 = 3$.  — 标准解答
#   Let me analyze this problem carefully.

We need to find the largest $k$ such that for all $x, y, z > 0$ with $xyz = 1$:
$$\sum_{cyc} \frac{x}{xy+1} + \frac{k}{\sqrt[3]{xy^2 + yz^2 + zx^2}} \ge \frac{3}{2} + \frac{k}{\sqrt[3]{3}}$$

Let me first check for answer leaks. The problem statement doesn't contain any solutions, proof sketches, or answer values. Good.

Let me think about this problem. At $x = y = z = 1$, we have $xyz = 1$, and:
- $\sum_{cyc} \frac{x}{xy+1} = \frac{1}{1+1} \cdot 3 = \frac{3}{2}$
- $xy^2 + yz^2 + zx^2 = 1 + 1 + 1 = 3$, so $\sqrt[3]{3}$
- So equality holds at $x = y = z = 1$.

So the inequality is tight at $x = y = z = 1$. We need to find the largest $k$ such that this holds.

Let me rewrite. Let $f(x,y,z) = \sum_{cyc} \frac{x}{xy+1}$ and $g(x,y,z) = \frac{1}{\sqrt[3]{xy^2 + yz^2 + zx^2}}$.

The inequality is $f + k \cdot g \ge \frac{3}{2} + \frac{k}{\sqrt[3]{3}}$.

At $x=y=z=1$: $f = 3/2$, $g = 1/\sqrt[3]{3}$, so equality.

We want the largest $k$ such that $f - 3/2 \ge k(1/\sqrt[3]{3} - g)$ for all $x,y,z > 0$ with $xyz=1$.

Note $g = 1/\sqrt[3]{xy^2 + yz^2 + zx^2}$. By AM-GM, $xy^2 + yz^2 + zx^2 \ge 3\sqrt[3]{xy^2 \cdot yz^2 \cdot zx^2} = 3\sqrt[3]{x^3 y^3 z^3} = 3xyz = 3$. So $xy^2 + yz^2 + zx^2 \ge 3$, meaning $g \le 1/\sqrt[3]{3}$, so $1/\sqrt[3]{3} - g \ge 0$.

So we need $k \le \frac{f - 3/2}{1/\sqrt[3]{3} - g}$ for all points where $g < 1/\sqrt[3]{3}$ (i.e., not at $x=y=z=1$).

So $k_{max} = \inf_{x,y,z: xyz=1, \text{not all equal}} \frac{f - 3/2}{1/\sqrt[3]{3} - g}$.

Wait, but we also need $f - 3/2 \ge 0$ for this to work. Let me check: is $f = \sum_{cyc} \frac{x}{xy+1} \ge 3/2$ always?

With $xyz = 1$, let's substitute. Let $x = a/b, y = b/c, z = c/a$ for some $a, b, c > 0$. Then $xyz = 1$.

$xy = a/c$, $yz = b/a$, $zx = c/b$.

$\frac{x}{xy+1} = \frac{a/b}{a/c + 1} = \frac{a/b \cdot c}{a + c} = \frac{ac}{b(a+c)}$.

Hmm, this is getting complicated. Let me try another substitution.

Actually, let me try the substitution $x = a/b, y = b/c, z = c/a$.

$\sum_{cyc} \frac{x}{xy+1} = \frac{a/b}{a/c+1} + \frac{b/c}{b/a+1} + \frac{c/a}{c/b+1}$

$= \frac{ac}{b(a+c)} + \frac{ab}{c(a+b)} + \frac{bc}{a(b+c)}$

Hmm. Let me try a different approach. Let me check if $f \ge 3/2$.

Actually, let me try $x = t, y = t, z = 1/t^2$ for large $t$.

$xy = t^2$, $yz = 1/t$, $zx = 1/t$.

$f = \frac{t}{t^2+1} + \frac{t}{1/t+1} + \frac{1/t^2}{1/t+1}$

$= \frac{t}{t^2+1} + \frac{t^2}{1+t} + \frac{1}{t^2(1/t+1)} = \frac{t}{t^2+1} + \frac{t^2}{1+t} + \frac{1}{t(1+t)}$

$= \frac{t}{t^2+1} + \frac{t^3 + 1}{t(1+t)} = \frac{t}{t^2+1} + \frac{(t+1)(t^2-t+1)}{t(t+1)} = \frac{t}{t^2+1} + \frac{t^2-t+1}{t}$

$= \frac{t}{t^2+1} + t - 1 + \frac{1}{t}$

For large $t$, this is approximately $t - 1 \to \infty$. So $f \to \infty$, good.

Now $xy^2 + yz^2 + zx^2 = t \cdot t^2 + t \cdot 1/t^4 + 1/t^2 \cdot t^2 = t^3 + 1/t^3 + 1$.

For large $t$, this is approximately $t^3$, so $g \approx 1/t$, and $1/\sqrt[3]{3} - g \to 1/\sqrt[3]{3}$.

So the ratio $\frac{f - 3/2}{1/\sqrt[3]{3} - g} \to \infty$ as $t \to \infty$. So the infimum is not at infinity in this direction.

Let me try near $x = y = z = 1$. Let $x = 1+a, y = 1+b, z = 1+c$ with small perturbations and $xyz = 1$.

Actually, let me use the parametrization $x = e^u, y = e^v, z = e^w$ with $u + v + w = 0$.

At $u = v = w = 0$, we have the equality point. Let me expand to second order.

Let me set $u = s, v = -s, w = 0$ (so $x = e^s, y = e^{-s}, z = 1$).

$xy = 1, yz = e^{-s}, zx = e^s$.

$f = \frac{e^s}{1+1} + \frac{e^{-s}}{e^{-s}+1} + \frac{1}{e^s+1} = \frac{e^s}{2} + \frac{1}{1+e^s} + \frac{1}{e^s+1}$

Wait: $\frac{e^{-s}}{e^{-s}+1} = \frac{1}{1+e^s}$ and $\frac{1}{e^s+1}$.

So $f = \frac{e^s}{2} + \frac{2}{1+e^s}$.

At $s=0$: $f = 1/2 + 1 = 3/2$. Good.

$f' = \frac{e^s}{2} - \frac{2e^s}{(1+e^s)^2}$. At $s=0$: $1/2 - 2/4 = 1/2 - 1/2 = 0$. Good.

$f'' = \frac{e^s}{2} - \frac{2e^s(1+e^s)^2 - 2e^s \cdot 2(1+e^s)e^s}{(1+e^s)^4} = \frac{e^s}{2} - \frac{2e^s(1+e^s) - 4e^{2s}}{(1+e^s)^3}$

At $s=0$: $1/2 - \frac{2 \cdot 2 - 4}{8} = 1/2 - 0 = 1/2$.

Now $g$: $xy^2 + yz^2 + zx^2 = e^s \cdot e^{-2s} + e^{-s} \cdot 1 + 1 \cdot e^{2s} = e^{-s} + e^{-s} + e^{2s} = 2e^{-s} + e^{2s}$.

At $s=0$: $2 + 1 = 3$. Good.

$h(s) = 2e^{-s} + e^{2s}$. $h'(s) = -2e^{-s} + 2e^{2s}$. At $s=0$: $-2 + 2 = 0$. Good.

$h''(s) = 2e^{-s} + 4e^{2s}$. At $s=0$: $2 + 4 = 6$.

So $h(s) \approx 3 + 3s^2$.

$g = h^{-1/3} \approx 3^{-1/3}(1 + s^2)^{-1/3} \approx 3^{-1/3}(1 - s^2/3)$.

So $1/\sqrt[3]{3} - g \approx 3^{-1/3} \cdot s^2/3 = s^2/(3 \cdot 3^{1/3}) = s^2/3^{4/3}$.

And $f - 3/2 \approx s^2/4$.

So the ratio near $s = 0$ is $\frac{s^2/4}{s^2/3^{4/3}} = \frac{3^{4/3}}{4}$.

So $k_{max} \le \frac{3^{4/3}}{4}$.

But wait, I need to check other directions. Let me try $u = s, v = s, w = -2s$ (so $x = e^s, y = e^s, z = e^{-2s}$).

$xy = e^{2s}, yz = e^{-s}, zx = e^{-s}$.

$f = \frac{e^s}{e^{2s}+1} + \frac{e^s}{e^{-s}+1} + \frac{e^{-2s}}{e^{-s}+1}$

$= \frac{e^s}{e^{2s}+1} + \frac{e^{2s}}{1+e^s} + \frac{e^{-s}}{1+e^s}$

$= \frac{e^s}{e^{2s}+1} + \frac{e^{2s}+e^{-s}}{1+e^s}$

At $s=0$: $1/2 + 2/2 = 3/2$. Good.

$f' = \frac{e^s(e^{2s}+1) - e^s \cdot 2e^{2s}}{(e^{2s}+1)^2} + \frac{(2e^{2s}-e^{-s})(1+e^s) - (e^{2s}+e^{-s})e^s}{(1+e^s)^2}$

At $s=0$: First term: $\frac{1 \cdot 2 - 1 \cdot 2}{4} = 0$. Second term: $\frac{(2-1) \cdot 2 - 2 \cdot 1}{4} = \frac{2-2}{4} = 0$. Good.

$f''$: Let me compute each part.

First term: $A(s) = \frac{e^s}{e^{2s}+1}$. $A'(s) = \frac{e^s(1-e^{2s})}{(e^{2s}+1)^2}$.

$A''(s) = \frac{[e^s(1-e^{2s}) - 2e^{3s}](e^{2s}+1)^2 - e^s(1-e^{2s}) \cdot 2(e^{2s}+1) \cdot 2e^{2s}}{(e^{2s}+1)^4}$

At $s=0$: numerator of $A'$ part: $e^s(1-e^{2s}) = 0$ at $s=0$. So $A''(0) = \frac{[1 \cdot (1-1) - 2](4) - 0}{16} = \frac{-2 \cdot 4}{16} = \frac{-8}{16} = -1/2$.

Hmm wait, let me redo. $A'(s) = \frac{e^s - e^{3s}}{(e^{2s}+1)^2}$.

$A''(s) = \frac{(e^s - 3e^{3s})(e^{2s}+1)^2 - (e^s - e^{3s}) \cdot 2(e^{2s}+1)(2e^{2s})}{(e^{2s}+1)^4}$

At $s=0$: $(1-3)(4) - 0 = -8$. Divided by $16$: $-1/2$.

Second term: $B(s) = \frac{e^{2s}+e^{-s}}{1+e^s}$.

$B'(s) = \frac{(2e^{2s}-e^{-s})(1+e^s) - (e^{2s}+e^{-s})e^s}{(1+e^s)^2}$

At $s=0$: $\frac{(2-1)(2) - 2 \cdot 1}{4} = \frac{2-2}{4} = 0$. Good.

$B''(s)$: Let me compute the numerator $N(s) = (2e^{2s}-e^{-s})(1+e^s) - (e^{2s}+e^{-s})e^s$.

$N(s) = 2e^{2s} + 2e^{3s} - e^{-s} - 1 - e^{3s} - 1 = 2e^{2s} + e^{3s} - e^{-s} - 2$.

Wait let me redo: $(2e^{2s}-e^{-s})(1+e^s) = 2e^{2s} + 2e^{3s} - e^{-s} - 1$.

$(e^{2s}+e^{-s})e^s = e^{3s} + 1$.

$N(s) = 2e^{2s} + 2e^{3s} - e^{-s} - 1 - e^{3s} - 1 = 2e^{2s} + e^{3s} - e^{-s} - 2$.

$N'(s) = 4e^{2s} + 3e^{3s} + e^{-s}$. At $s=0$: $4 + 3 + 1 = 8$.

$B''(s) = \frac{N'(s)(1+e^s)^2 - N(s) \cdot 2(1+e^s)e^s}{(1+e^s)^4}$

At $s=0$: $N(0) = 2 + 1 - 1 - 2 = 0$. So $B''(0) = \frac{8 \cdot 4 - 0}{16} = 2$.

So $f''(0) = A''(0) + B''(0) = -1/2 + 2 = 3/2$.

Now $h(s) = xy^2 + yz^2 + zx^2 = e^s \cdot e^{2s} + e^s \cdot e^{-4s} + e^{-2s} \cdot e^{2s} = e^{3s} + e^{-3s} + 1$.

$h(0) = 3$. $h'(0) = 3 - 3 = 0$. $h''(0) = 9 + 9 = 18$.

So $h(s) \approx 3 + 9s^2$.

$g \approx 3^{-1/3}(1 + 3s^2)^{-1/3} \approx 3^{-1/3}(1 - s^2)$.

$1/\sqrt[3]{3} - g \approx 3^{-1/3} s^2 = s^2/3^{1/3}$.

$f - 3/2 \approx (3/2)s^2/2 = 3s^2/4$.

Ratio: $\frac{3s^2/4}{s^2/3^{1/3}} = \frac{3 \cdot 3^{1/3}}{4} = \frac{3^{4/3}}{4}$.

Same ratio! Interesting. So in both directions, the ratio is $3^{4/3}/4$.

Let me try a general direction. Let $u = as, v = bs, w = -(a+b)s$.

Actually, let me think more generally. We have $x = e^{as}, y = e^{bs}, z = e^{-(a+b)s}$.

The key quantities:
- $xy = e^{(a+b)s}$, $yz = e^{-as}$, $zx = e^{-bs}$.

$f = \frac{e^{as}}{e^{(a+b)s}+1} + \frac{e^{bs}}{e^{-as}+1} + \frac{e^{-(a+b)s}}{e^{-bs}+1}$

$= \frac{e^{as}}{e^{(a+b)s}+1} + \frac{e^{(a+b)s}}{e^{as}+1} + \frac{e^{-as}}{e^{bs}+1}$

Hmm wait: $\frac{e^{bs}}{e^{-as}+1} = \frac{e^{bs} \cdot e^{as}}{1+e^{as}} = \frac{e^{(a+b)s}}{1+e^{as}}$.

And $\frac{e^{-(a+b)s}}{e^{-bs}+1} = \frac{e^{-(a+b)s} \cdot e^{bs}}{1+e^{bs}} = \frac{e^{-as}}{1+e^{bs}}$.

So $f = \frac{e^{as}}{e^{(a+b)s}+1} + \frac{e^{(a+b)s}}{e^{as}+1} + \frac{e^{-as}}{e^{bs}+1}$.

This is getting complex. Let me just compute the second-order expansion.

For a general function $F(s)$ with $F(0) = F_0$, $F'(0) = 0$, $F''(0) = F_2$, we have $F(s) \approx F_0 + F_2 s^2/2$.

So $f - 3/2 \approx f_2 s^2/2$ and $1/\sqrt[3]{3} - g \approx g_2 s^2/2$ where $f_2 = f''(0)$ and $g_2 = -g''(0)$ (since $g$ has a max at 0, $g''(0) < 0$).

Wait, $g = h^{-1/3}$, $g' = -\frac{1}{3}h^{-4/3}h'$, $g'' = -\frac{1}{3}h^{-4/3}h'' + \frac{4}{9}h^{-7/3}(h')^2$.

At $s=0$: $h = 3, h' = 0, h'' = h_2$. So $g''(0) = -\frac{1}{3} \cdot 3^{-4/3} \cdot h_2 = -\frac{h_2}{3^{7/3}}$.

So $g_2 = -g''(0) = \frac{h_2}{3^{7/3}}$.

And the ratio is $\frac{f_2/2}{g_2/2} = \frac{f_2}{g_2} = \frac{f_2 \cdot 3^{7/3}}{h_2}$.

Now I need to compute $f_2$ and $h_2$ for a general direction $(a, b, -(a+b))$.

Let me compute $h = xy^2 + yz^2 + zx^2$.

$xy^2 = e^{as} \cdot e^{2bs} = e^{(a+2b)s}$
$yz^2 = e^{bs} \cdot e^{-2(a+b)s} = e^{(-a-b)s}$
$zx^2 = e^{-(a+b)s} \cdot e^{2as} = e^{(a-b)s}$

$h = e^{(a+2b)s} + e^{(-a-b)s} + e^{(a-b)s}$

$h(0) = 3$. $h'(0) = (a+2b) + (-a-b) + (a-b) = a + 2b - a - b + a - b = a$. 

Wait, that should be 0 for the constraint. Hmm, but $u + v + w = a + b - (a+b) = 0$, so the constraint is satisfied. But $h'(0) = a$? That can't be right if we want $h$ to have a critical point at $s=0$.

Wait, actually $h$ doesn't need to have a critical point at $s=0$ in every direction. The AM-GM gives $h \ge 3$ with equality at $x=y=z=1$, so $h$ does have a minimum at $s=0$ for all directions. Let me recheck.

$h'(0) = (a+2b) + (-a-b) + (a-b) = a + 2b - a - b + a - b = a$.

Hmm, that gives $a$, not 0. But that contradicts $h$ having a minimum at $s=0$.

Wait, let me recheck. $h = xy^2 + yz^2 + zx^2$. With $x = e^{as}, y = e^{bs}, z = e^{-(a+b)s}$:

$xy^2 = e^{as} \cdot e^{2bs} = e^{(a+2b)s}$ ✓
$yz^2 = e^{bs} \cdot e^{-2(a+b)s} = e^{(b - 2a - 2b)s} = e^{(-2a-b)s}$

Wait, I made an error. $z = e^{-(a+b)s}$, so $z^2 = e^{-2(a+b)s}$.

$yz^2 = e^{bs} \cdot e^{-2(a+b)s} = e^{(b - 2a - 2b)s} = e^{(-2a - b)s}$.

$zx^2 = e^{-(a+b)s} \cdot e^{2as} = e^{(2a - a - b)s} = e^{(a-b)s}$.

So $h = e^{(a+2b)s} + e^{(-2a-b)s} + e^{(a-b)s}$.

$h'(0) = (a+2b) + (-2a-b) + (a-b) = a + 2b - 2a - b + a - b = 0$. ✓

$h''(0) = (a+2b)^2 + (-2a-b)^2 + (a-b)^2$.

$= (a+2b)^2 + (2a+b)^2 + (a-b)^2$

$= a^2 + 4ab + 4b^2 + 4a^2 + 4ab + b^2 + a^2 - 2ab + b^2$

$= 6a^2 + 6ab + 6b^2 = 6(a^2 + ab + b^2)$.

So $h_2 = 6(a^2 + ab + b^2)$.

Now for $f$. Let me compute $f = \frac{x}{xy+1} + \frac{y}{yz+1} + \frac{z}{zx+1}$.

$\frac{x}{xy+1} = \frac{e^{as}}{e^{(a+b)s}+1}$

$\frac{y}{yz+1} = \frac{e^{bs}}{e^{(-2a-b)s} \cdot ... }$

Wait, $yz = e^{bs} \cdot e^{-(a+b)s} = e^{-as}$.

$\frac{y}{yz+1} = \frac{e^{bs}}{e^{-as}+1} = \frac{e^{(a+b)s}}{1+e^{as}}$

$zx = e^{-(a+b)s} \cdot e^{as} = e^{-bs}$.

$\frac{z}{zx+1} = \frac{e^{-(a+b)s}}{e^{-bs}+1} = \frac{e^{-as}}{1+e^{bs}}$

So $f = \frac{e^{as}}{e^{(a+b)s}+1} + \frac{e^{(a+b)s}}{e^{as}+1} + \frac{e^{-as}}{e^{bs}+1}$.

Let me denote $\alpha = a, \beta = a+b$. Then $b = \beta - \alpha$ and $-(a+b) = -\beta$.

$f = \frac{e^{\alpha s}}{e^{\beta s}+1} + \frac{e^{\beta s}}{e^{\alpha s}+1} + \frac{e^{-\alpha s}}{e^{(\beta-\alpha)s}+1}$

Hmm, this is still complex. Let me compute $f''(0)$ using the formula for $\frac{e^{ps}}{e^{qs}+1}$.

Let $\phi(p,q) = \frac{e^{ps}}{e^{qs}+1}$. At $s=0$: $\phi = 1/2$.

$\phi' = \frac{pe^{ps}(e^{qs}+1) - e^{ps} \cdot qe^{qs}}{(e^{qs}+1)^2} = \frac{e^{ps}(p(e^{qs}+1) - qe^{qs})}{(e^{qs}+1)^2}$

At $s=0$: $\frac{p \cdot 2 - q}{4} = \frac{2p-q}{4}$.

$\phi''$: Let me use the quotient rule on $\phi' = \frac{e^{ps}(p + (p-q)e^{qs})}{(e^{qs}+1)^2}$.

Let $N = e^{ps}(p + (p-q)e^{qs})$ and $D = (e^{qs}+1)^2$.

$N' = pe^{ps}(p + (p-q)e^{qs}) + e^{ps}(p-q)qe^{qs} = e^{ps}[p^2 + p(p-q)e^{qs} + q(p-q)e^{qs}]$

$= e^{ps}[p^2 + (p-q)(p+q)e^{qs}] = e^{ps}[p^2 + (p^2-q^2)e^{qs}]$

At $s=0$: $N(0) = p + (p-q) = 2p - q$. $N'(0) = p^2 + p^2 - q^2 = 2p^2 - q^2$.

$D = (e^{qs}+1)^2$. $D' = 2(e^{qs}+1)qe^{qs}$. At $s=0$: $D(0) = 4$, $D'(0) = 4q$.

$D'' = 2q^2 e^{qs}(e^{qs}+1) + 2q \cdot 2qe^{2qs} = 2q^2 e^{qs}(e^{qs}+1+2e^{qs}) = 2q^2 e^{qs}(1+3e^{qs})$. 

Hmm, let me just compute: $D = (e^{qs}+1)^2$, $D' = 2q e^{qs}(e^{qs}+1)$, $D'' = 2q^2 e^{qs}(e^{qs}+1) + 2q \cdot q e^{2qs} \cdot 2 = 2q^2 e^{qs}(e^{qs}+1) + 4q^2 e^{2qs} = 2q^2 e^{qs}(e^{qs}+1+2e^{qs}) = 2q^2 e^{qs}(1+3e^{qs})$.

At $s=0$: $D''(0) = 2q^2 \cdot 4 = 8q^2$.

$\phi''(0) = \frac{N'(0)D(0) - N(0)D'(0)}{D(0)^2} \cdot$ ... no, $\phi'' = \frac{N'D - ND'}{D^2}$, and

$\phi''(0) = \frac{N''(0)D(0) - N(0)D''(0)}{D(0)^2}$... 

Actually, $(N/D)'' = \frac{N''D - ND''}{D^2} - \frac{2(N'D - ND')D'}{D^3}$... this is getting messy. Let me use the formula:

$(N/D)' = (N'D - ND')/D^2$

$(N/D)'' = \frac{(N''D + N'D' - N'D' - ND'')D^2 - (N'D - ND') \cdot 2DD'}{D^4}$

$= \frac{(N''D - ND'')D - 2(N'D - ND')D'}{D^3}$

At $s=0$:

$= \frac{(N''_0 D_0 - N_0 D''_0)D_0 - 2(N'_0 D_0 - N_0 D'_0)D'_0}{D_0^3}$

I need $N''(0)$. $N = e^{ps}[p^2 + (p^2-q^2)e^{qs}]$.

$N' = pe^{ps}[p^2 + (p^2-q^2)e^{qs}] + e^{ps}(p^2-q^2)qe^{qs}$

$= e^{ps}[p^3 + p(p^2-q^2)e^{qs} + q(p^2-q^2)e^{qs}]$

$= e^{ps}[p^3 + (p^2-q^2)(p+q)e^{qs}]$

$= e^{ps}[p^3 + (p-q)(p+q)^2 e^{qs}]$... wait, $(p^2-q^2)(p+q) = (p-q)(p+q)^2$.

$N'' = pe^{ps}[p^3 + (p^2-q^2)(p+q)e^{qs}] + e^{ps}(p^2-q^2)(p+q)qe^{qs}$

$= e^{ps}[p^4 + p(p^2-q^2)(p+q)e^{qs} + q(p^2-q^2)(p+q)e^{qs}]$

$= e^{ps}[p^4 + (p^2-q^2)(p+q)^2 e^{qs}]$

At $s=0$: $N''(0) = p^4 + (p^2-q^2)(p+q)^2 = p^4 + (p-q)(p+q)^3$.

This is getting really messy. Let me try a different approach - just compute $f''(0)$ for the general case numerically or symbolically.

Actually, let me use a cleaner approach. Let me write $f = \sum \frac{x}{xy+1}$ and compute $\frac{d^2 f}{ds^2}\big|_{s=0}$ using the chain rule with $x = e^{as}, y = e^{bs}, z = e^{-(a+b)s}$.

For a term $\frac{x}{xy+1}$, let $u = x = e^{as}$, $v = xy = e^{(a+b)s}$.

$\frac{d}{ds}\frac{u}{v+1} = \frac{u'(v+1) - uv'}{(v+1)^2}$

At $s=0$: $u=1, v=1, u'=a, v'=a+b$. So $\frac{a \cdot 2 - (a+b)}{4} = \frac{a-b}{4}$.

For the second derivative, let me use the expansion approach. Let $u = 1 + as + \frac{a^2 s^2}{2} + ...$, $v = 1 + (a+b)s + \frac{(a+b)^2 s^2}{2} + ...$

$\frac{u}{v+1} = \frac{1 + as + a^2 s^2/2}{2 + (a+b)s + (a+b)^2 s^2/2}$

$= \frac{1}{2} \cdot \frac{1 + as + a^2 s^2/2}{1 + (a+b)s/2 + (a+b)^2 s^2/4}$

$\approx \frac{1}{2}(1 + as + a^2 s^2/2)(1 - (a+b)s/2 - (a+b)^2 s^2/4 + (a+b)^2 s^2/4)$

Wait, $\frac{1}{1+t} \approx 1 - t + t^2$ where $t = (a+b)s/2 + (a+b)^2 s^2/4$.

$1 - t + t^2 \approx 1 - (a+b)s/2 - (a+b)^2 s^2/4 + (a+b)^2 s^2/4 = 1 - (a+b)s/2$.

Hmm, that's only first order. Let me be more careful.

$t = \frac{(a+b)s}{2} + \frac{(a+b)^2 s^2}{4}$

$t^2 = \frac{(a+b)^2 s^2}{4} + ...$

$\frac{1}{1+t} = 1 - t + t^2 - ... \approx 1 - \frac{(a+b)s}{2} - \frac{(a+b)^2 s^2}{4} + \frac{(a+b)^2 s^2}{4} = 1 - \frac{(a+b)s}{2}$

So $\frac{u}{v+1} \approx \frac{1}{2}(1 + as + \frac{a^2 s^2}{2})(1 - \frac{(a+b)s}{2})$

$= \frac{1}{2}(1 + as + \frac{a^2 s^2}{2} - \frac{(a+b)s}{2} - \frac{a(a+b)s^2}{2})$

$= \frac{1}{2}(1 + \frac{a-b}{2}s + \frac{a^2 - a(a+b)}{2}s^2)$

$= \frac{1}{2}(1 + \frac{a-b}{2}s + \frac{-ab}{2}s^2)$

$= \frac{1}{2} + \frac{a-b}{4}s - \frac{ab}{4}s^2$

So the second-order coefficient of $\frac{x}{xy+1}$ is $-\frac{ab}{4}$, meaning $\frac{d^2}{ds^2}\frac{x}{xy+1}\big|_{s=0} = -\frac{ab}{2}$.

Similarly, for $\frac{y}{yz+1}$: $y = e^{bs}$, $yz = e^{-as}$.

By the same formula with $u = y = e^{bs}$, $v = yz = e^{-as}$, so $p = b, q = -a$ in the expansion.

$\frac{y}{yz+1} \approx \frac{1}{2} + \frac{b-(-a)}{4}s - \frac{b \cdot (-a)}{4}s^2 = \frac{1}{2} + \frac{a+b}{4}s + \frac{ab}{4}s^2$

Second derivative: $\frac{ab}{2}$.

For $\frac{z}{zx+1}$: $z = e^{-(a+b)s}$, $zx = e^{-bs}$.

$p = -(a+b), q = -b$.

$\frac{z}{zx+1} \approx \frac{1}{2} + \frac{-(a+b)-(-b)}{4}s - \frac{(-(a+b))(-b)}{4}s^2 = \frac{1}{2} + \frac{-a}{4}s - \frac{b(a+b)}{4}s^2$

Second derivative: $-\frac{b(a+b)}{2}$.

Total $f''(0) = -\frac{ab}{2} + \frac{ab}{2} - \frac{b(a+b)}{2} = -\frac{b(a+b)}{2}$.

Hmm, that doesn't look symmetric. Let me check with the first direction: $a = 1, b = -1$ (so $u = s, v = -s, w = 0$).

$f''(0) = -\frac{(-1)(1+(-1))}{2} = -\frac{(-1)(0)}{2} = 0$.

But earlier I computed $f''(0) = 1/2$ for this direction! So I made an error.

Let me recheck. For $a = 1, b = -1$: $x = e^s, y = e^{-s}, z = 1$.

$\frac{x}{xy+1} = \frac{e^s}{1+1} = \frac{e^s}{2}$. Second derivative: $\frac{1}{2}$.

Using my formula: $-\frac{ab}{2} = -\frac{1 \cdot (-1)}{2} = \frac{1}{2}$. ✓

$\frac{y}{yz+1} = \frac{e^{-s}}{e^{-s}+1} = \frac{1}{1+e^s}$. Second derivative of $\frac{1}{1+e^s}$ at $s=0$: $\frac{e^s}{(1+e^s)^2}$ first derivative, $\frac{e^s(1+e^s)^2 - e^s \cdot 2(1+e^s)e^s}{(1+e^s)^4} = \frac{e^s(1-e^s)}{(1+e^s)^3}$. At $s=0$: $0$.

Using my formula: $\frac{ab}{2} = \frac{1 \cdot (-1)}{2} = -\frac{1}{2}$.

But the actual second derivative is $0$, not $-1/2$! So my formula is wrong.

Let me recheck the expansion for $\frac{y}{yz+1}$ with $p = b = -1, q = -a = -1$.

$\frac{1}{2} + \frac{p-q}{4}s - \frac{pq}{4}s^2 = \frac{1}{2} + \frac{-1-(-1)}{4}s - \frac{(-1)(-1)}{4}s^2 = \frac{1}{2} - \frac{1}{4}s^2$.

So the second derivative is $-\frac{1}{2}$. But the actual function is $\frac{1}{1+e^s}$, whose second derivative at 0 is 0.

Let me compute $\frac{1}{1+e^s}$ more carefully. $\frac{d}{ds} = \frac{-e^s}{(1+e^s)^2}$. At $s=0$: $-1/4$.

$\frac{d^2}{ds^2} = \frac{-e^s(1+e^s)^2 + e^s \cdot 2(1+e^s)e^s}{(1+e^s)^4} = \frac{e^s(-1+e^s)}{(1+e^s)^3}$. At $s=0$: $\frac{1 \cdot 0}{8} = 0$.

So the second derivative is indeed 0. My expansion formula must be wrong.

Let me redo the expansion. $\frac{u}{v+1}$ where $u = e^{ps}, v = e^{qs}$.

$u = 1 + ps + \frac{p^2 s^2}{2} + ...$

$v + 1 = 2 + qs + \frac{q^2 s^2}{2} + ...$

$\frac{u}{v+1} = \frac{1 + ps + p^2 s^2/2}{2 + qs + q^2 s^2/2}$

$= \frac{1}{2} \cdot \frac{1 + ps + p^2 s^2/2}{1 + qs/2 + q^2 s^2/4}$

Let $t = qs/2 + q^2 s^2/4$.

$\frac{1}{1+t} = 1 - t + t^2 - ... = 1 - qs/2 - q^2 s^2/4 + q^2 s^2/4 + ... = 1 - qs/2 + O(s^3)$

Wait, $t^2 = (qs/2)^2 + ... = q^2 s^2/4 + ...$

$1 - t + t^2 = 1 - qs/2 - q^2 s^2/4 + q^2 s^2/4 = 1 - qs/2$.

So $\frac{1}{1+t} \approx 1 - qs/2$ to second order? That can't be right - we're losing the $s^2$ term.

Let me be more careful. $t = \frac{q}{2}s + \frac{q^2}{4}s^2$.

$t^2 = \frac{q^2}{4}s^2 + O(s^3)$.

$\frac{1}{1+t} = 1 - t + t^2 + O(s^3) = 1 - \frac{q}{2}s - \frac{q^2}{4}s^2 + \frac{q^2}{4}s^2 + O(s^3) = 1 - \frac{q}{2}s + O(s^3)$.

Hmm, so to second order, $\frac{1}{1+t} = 1 - \frac{q}{2}s$. The $s^2$ terms cancel!

So $\frac{u}{v+1} = \frac{1}{2}(1 + ps + \frac{p^2}{2}s^2)(1 - \frac{q}{2}s) + O(s^3)$

$= \frac{1}{2}(1 + ps + \frac{p^2}{2}s^2 - \frac{q}{2}s - \frac{pq}{2}s^2) + O(s^3)$

$= \frac{1}{2}(1 + \frac{2p-q}{2}s + \frac{p^2 - pq}{2}s^2) + O(s^3)$

$= \frac{1}{2} + \frac{2p-q}{4}s + \frac{p(p-q)}{4}s^2 + O(s^3)$

So the second derivative is $\frac{p(p-q)}{2}$.

Let me verify: for $\frac{x}{xy+1}$ with $p = a, q = a+b$: second derivative $= \frac{a(a-(a+b))}{2} = \frac{a(-b)}{2} = -\frac{ab}{2}$.

For $\frac{y}{yz+1}$ with $p = b, q = -a$: second derivative $= \frac{b(b-(-a))}{2} = \frac{b(a+b)}{2}$.

For $\frac{z}{zx+1}$ with $p = -(a+b), q = -b$: second derivative $= \frac{(-(a+b))(-(a+b)-(-b))}{2} = \frac{(-(a+b))(-a)}{2} = \frac{a(a+b)}{2}$.

Total: $f''(0) = -\frac{ab}{2} + \frac{b(a+b)}{2} + \frac{a(a+b)}{2} = \frac{-ab + ab + b^2 + a^2 + ab}{2} = \frac{a^2 + ab + b^2}{2}$.

Let me verify with direction 1: $a = 1, b = -1$. $f''(0) = \frac{1 - 1 + 1}{2} = \frac{1}{2}$. ✓ (matches earlier computation)

Direction 2: $a = 1, b = 1$. $f''(0) = \frac{1 + 1 + 1}{2} = \frac{3}{2}$. ✓ (matches earlier computation)

So $f''(0) = \frac{a^2 + ab + b^2}{2}$ and $h''(0) = 6(a^2 + ab + b^2)$.

The ratio is $\frac{f''(0)}{g_2}$ where $g_2 = \frac{h''(0)}{3^{7/3}} = \frac{6(a^2+ab+b^2)}{3^{7/3}}$.

Ratio $= \frac{(a^2+ab+b^2)/2}{6(a^2+ab+b^2)/3^{7/3}} = \frac{1/2}{6/3^{7/3}} = \frac{3^{7/3}}{12} = \frac{3^{7/3}}{12}$.

$3^{7/3} = 3^2 \cdot 3^{1/3} = 9 \cdot 3^{1/3}$.

$\frac{9 \cdot 3^{1/3}}{12} = \frac{3 \cdot 3^{1/3}}{4} = \frac{3^{4/3}}{4}$.

So the ratio is $\frac{3^{4/3}}{4}$ in every direction! This means the second-order expansion gives the same ratio regardless of direction, which is a strong indication that $k_{max} = \frac{3^{4/3}}{4}$.

But I need to verify this is actually the global minimum of the ratio, not just the local behavior near $x = y = z = 1$.

So the claim is $k_{max} = \frac{3^{4/3}}{4}$, and we need to prove:

$$\sum_{cyc} \frac{x}{xy+1} + \frac{3^{4/3}/4}{\sqrt[3]{xy^2 + yz^2 + zx^2}} \ge \frac{3}{2} + \frac{3^{4/3}/4}{\sqrt[3]{3}}$$

for all $x, y, z > 0$ with $xyz = 1$.

And $(2k_{max})^3 = (2 \cdot \frac{3^{4/3}}{4})^3 = (\frac{3^{4/3}}{2})^3 = \frac{3^4}{8} = \frac{81}{8}$.

Wait, let me double-check: $2 \cdot \frac{3^{4/3}}{4} = \frac{3^{4/3}}{2}$. $(\frac{3^{4/3}}{2})^3 = \frac{3^4}{8} = \frac{81}{8}$.

Now I need to actually prove the inequality. Let me think about this more carefully.

We need to show: $f - 3/2 \ge \frac{3^{4/3}}{4}(\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}})$ where $h = xy^2 + yz^2 + zx^2$ and $f = \sum \frac{x}{xy+1}$.

Note $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}} = \frac{h^{1/3} - 3^{1/3}}{3^{1/3} h^{1/3}} \cdot \frac{1}{???}$

Actually, $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}} = \frac{\sqrt[3]{h} - \sqrt[3]{3}}{\sqrt[3]{3}\sqrt[3]{h}}$.

And $\sqrt[3]{h} - \sqrt[3]{3} = \frac{h - 3}{\sqrt[3]{h^2} + \sqrt[3]{3h} + \sqrt[3]{9}}$.

So $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}} = \frac{h - 3}{\sqrt[3]{3h}(\sqrt[3]{h^2} + \sqrt[3]{3h} + \sqrt[3]{9})}$.

At $h = 3$: denominator $= 3(3 + 3 + 3) = 27$. So $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}} \approx \frac{h-3}{27}$.

And $\frac{3^{4/3}}{4} \cdot \frac{h-3}{27} = \frac{3^{4/3}(h-3)}{108}$.

Also, $h - 3 \approx 6(a^2+ab+b^2)s^2/2 \cdot 2 = ...$. Well, $h - 3 \approx 3(a^2+ab+b^2)s^2$ (from $h''(0) = 6(a^2+ab+b^2)$, so $h - 3 \approx 3(a^2+ab+b^2)s^2$).

And $f - 3/2 \approx \frac{a^2+ab+b^2}{4}s^2$.

So the ratio $\frac{f-3/2}{(1/\sqrt[3]{3} - 1/\sqrt[3]{h})} \approx \frac{(a^2+ab+b^2)s^2/4}{3(a^2+ab+b^2)s^2/27} = \frac{27}{12} = \frac{9}{4}$.

Hmm, that gives $9/4$, not $3^{4/3}/4$. Let me recheck.

Oh wait, I think I need to be more careful. Let me recompute $g_2$.

$g = h^{-1/3}$. $g' = -\frac{1}{3}h^{-4/3}h'$. At $s=0$: $g'(0) = 0$.

$g'' = -\frac{1}{3}(-\frac{4}{3})h^{-7/3}(h')^2 - \frac{1}{3}h^{-4/3}h'' = \frac{4}{9}h^{-7/3}(h')^2 - \frac{1}{3}h^{-4/3}h''$.

At $s=0$: $g''(0) = 0 - \frac{1}{3} \cdot 3^{-4/3} \cdot h''(0) = -\frac{h''(0)}{3^{7/3}}$.

So $g(s) \approx 3^{-1/3} - \frac{h''(0)}{2 \cdot 3^{7/3}} s^2$.

$1/\sqrt[3]{3} - g(s) \approx \frac{h''(0)}{2 \cdot 3^{7/3}} s^2 = \frac{6(a^2+ab+b^2)}{2 \cdot 3^{7/3}} s^2 = \frac{3(a^2+ab+b^2)}{3^{7/3}} s^2$.

And $f - 3/2 \approx \frac{a^2+ab+b^2}{4} s^2$.

Ratio $= \frac{(a^2+ab+b^2)/4}{3(a^2+ab+b^2)/3^{7/3}} = \frac{3^{7/3}}{12} = \frac{3^{7/3}}{12}$.

$3^{7/3} = 3^{2+1/3} = 9 \cdot 3^{1/3}$. $\frac{9 \cdot 3^{1/3}}{12} = \frac{3 \cdot 3^{1/3}}{4} = \frac{3^{4/3}}{4}$.

OK so the ratio is indeed $\frac{3^{4/3}}{4}$, confirming $k_{max} \le \frac{3^{4/3}}{4}$.

Now I need to prove the inequality holds for $k = \frac{3^{4/3}}{4}$.

Let me try to use the substitution $x = a/b, y = b/c, z = c/a$ to simplify.

With $xyz = 1$, let $x = a/b, y = b/c, z = c/a$.

$xy = a/c, yz = b/a, zx = c/b$.

$\frac{x}{xy+1} = \frac{a/b}{a/c+1} = \frac{ac}{b(a+c)}$.

$\frac{y}{yz+1} = \frac{b/c}{b/a+1} = \frac{ab}{c(a+b)}$.

$\frac{z}{zx+1} = \frac{c/a}{c/b+1} = \frac{bc}{a(b+c)}$.

$f = \frac{ac}{b(a+c)} + \frac{ab}{c(a+b)} + \frac{bc}{a(b+c)}$.

$xy^2 = \frac{a}{b} \cdot \frac{b^2}{c^2} = \frac{ab}{c^2}$.

$yz^2 = \frac{b}{c} \cdot \frac{c^2}{a^2} = \frac{bc}{a^2}$.

$zx^2 = \frac{c}{a} \cdot \frac{a^2}{b^2} = \frac{ac}{b^2}$.

$h = \frac{ab}{c^2} + \frac{bc}{a^2} + \frac{ca}{b^2}$.

Hmm, this is the Nesbitt-like form. Let me try $a = b = c = 1$: $f = 1/2 + 1/2 + 1/2 = 3/2$, $h = 1 + 1 + 1 = 3$. ✓

This substitution doesn't seem to simplify things much. Let me try another approach.

Let me try the substitution $p = xy, q = yz, r = zx$. Then $pqr = (xyz)^2 = 1$, and $x = \sqrt{pr/q}, y = \sqrt{pq/r}, z = \sqrt{qr/p}$.

$\frac{x}{xy+1} = \frac{x}{p+1} = \frac{\sqrt{pr/q}}{p+1}$.

This doesn't simplify nicely either.

Let me try yet another approach. Let me use $a = xy, b = yz, c = zx$ with $abc = 1$.

Then $x = \sqrt{ac/b}, y = \sqrt{ab/c}, z = \sqrt{bc/a}$.

$\frac{x}{xy+1} = \frac{\sqrt{ac/b}}{a+1}$, $\frac{y}{yz+1} = \frac{\sqrt{ab/c}}{b+1}$, $\frac{z}{zx+1} = \frac{\sqrt{bc/a}}{c+1}$.

$xy^2 = a \cdot ab/c = a^2b/c$. $yz^2 = b \cdot bc/a = b^2c/a$. $zx^2 = c \cdot ac/b = c^2a/b$.

$h = \frac{a^2b}{c} + \frac{b^2c}{a} + \frac{c^2a}{b}$.

With $abc = 1$, $c = 1/(ab)$, so $\frac{a^2b}{c} = a^3b^2$, $\frac{b^2c}{a} = b^3/a^2 \cdot 1/(ab) = ...$. This is getting messy.

Let me try a completely different approach. Maybe I should try to prove the inequality directly using known inequalities.

The inequality is:
$$\sum_{cyc} \frac{x}{xy+1} - \frac{3}{2} \ge \frac{3^{4/3}}{4}\left(\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{xy^2+yz^2+zx^2}}\right)$$

Let me denote $S = xy^2 + yz^2 + zx^2$ and $T = \sum \frac{x}{xy+1}$.

We know $S \ge 3$ (by AM-GM). We need $T \ge 3/2$ (which we should verify) and the refined inequality.

Actually, let me first check: is $T \ge 3/2$ always true?

With $x = e^{as}, y = e^{bs}, z = e^{-(a+b)s}$, we showed $T''(0) = \frac{a^2+ab+b^2}{2} \ge 0$, so $T$ has a local min at $s=0$. But is it a global min?

Let me check a boundary case. $x \to \infty, y = 1, z = 1/x$. Then $xy = x, yz = 1/x, zx = 1$.

$T = \frac{x}{x+1} + \frac{1}{1/x+1} + \frac{1/x}{1+1} = \frac{x}{x+1} + \frac{x}{x+1} + \frac{1}{2x} = \frac{2x}{x+1} + \frac{1}{2x}$.

As $x \to \infty$: $T \to 2$. As $x \to 0$: $T \to 0 + 0 + \infty = \infty$.

At $x = 1$: $T = 1 + 1/2 + 1/2 = 2$. Wait, that's not $3/2$.

Hmm wait, $x = 1, y = 1, z = 1$: $T = \frac{1}{2} + \frac{1}{2} + \frac{1}{2} = 3/2$. Let me recheck.

$x = 1, y = 1, z = 1$: $xy = 1, yz = 1, zx = 1$. $T = \frac{1}{1+1} + \frac{1}{1+1} + \frac{1}{1+1} = 3/2$. ✓

For $x \to \infty, y = 1, z = 1/x$: $T = \frac{x}{x+1} + \frac{1}{1/x+1} + \frac{1/x}{2}$. 

$\frac{1}{1/x+1} = \frac{x}{1+x}$. So $T = \frac{2x}{x+1} + \frac{1}{2x} \to 2$ as $x \to \infty$.

So $T$ can be larger than $3/2$. The minimum is at $x = y = z = 1$.

OK so the problem reduces to proving the refined inequality. Let me think about whether there's a clean proof.

Let me try to use the tangent line trick or SOS methods.

Actually, let me think about this differently. We want to show:

$$T - \frac{3}{2} \ge \frac{3^{4/3}}{4}\left(\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{S}}\right)$$

where $S = xy^2 + yz^2 + zx^2 \ge 3$.

Let $u = S/3 \ge 1$. Then $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{S}} = \frac{1}{\sqrt[3]{3}}(1 - u^{-1/3})$.

So the RHS is $\frac{3^{4/3}}{4} \cdot \frac{1}{3^{1/3}}(1 - u^{-1/3}) = \frac{3}{4}(1 - u^{-1/3})$.

So we need: $T - 3/2 \ge \frac{3}{4}(1 - (S/3)^{-1/3})$.

Or equivalently: $T \ge \frac{3}{2} + \frac{3}{4}(1 - (S/3)^{-1/3}) = \frac{3}{4}(3 - (S/3)^{-1/3})$... 

Hmm, let me think about this differently. Let me try to find a relationship between $T$ and $S$.

Actually, let me try specific parametric families to check if the ratio is always $\ge 3^{4/3}/4$.

Family 1: $x = t, y = t, z = 1/t^2$.

$xy = t^2, yz = 1/t, zx = 1/t$.

$T = \frac{t}{t^2+1} + \frac{t}{1/t+1} + \frac{1/t^2}{1/t+1} = \frac{t}{t^2+1} + \frac{t^2}{t+1} + \frac{1}{t(t+1)}$

$= \frac{t}{t^2+1} + \frac{t^3+1}{t(t+1)} = \frac{t}{t^2+1} + \frac{t^2-t+1}{t}$

$S = t \cdot t^2 + t \cdot 1/t^4 + 1/t^2 \cdot t^2 = t^3 + 1/t^3 + 1$.

Let me compute the ratio $R = \frac{T - 3/2}{1/3^{1/3} - 1/S^{1/3}}$ for various $t$.

At $t = 1$: $T = 1/2 + 1 = 3/2$, $S = 3$. Ratio is $0/0$, limit is $3^{4/3}/4 \approx 1.0817$... 

$3^{4/3} = 3 \cdot 3^{1/3} \approx 3 \cdot 1.4422 = 4.3267$. $3^{4/3}/4 \approx 1.0817$.

Let me try $t = 2$: 

$T = \frac{2}{5} + \frac{4-2+1}{2} = 0.4 + 1.5 = 1.9$.

$S = 8 + 1/8 + 1 = 9.125$.

$1/3^{1/3} \approx 0.6934$. $1/S^{1/3} = 1/9.125^{1/3}$. $9.125^{1/3} \approx 2.087$. So $1/S^{1/3} \approx 0.479$.

$T - 3/2 = 0.4$. $1/3^{1/3} - 1/S^{1/3} \approx 0.6934 - 0.479 = 0.2144$.

$R \approx 0.4/0.2144 \approx 1.866$.

This is larger than $1.0817$, so the inequality holds here.

Let me try $t$ close to 1, say $t = 1.1$:

$T = \frac{1.1}{1.21+1} + \frac{1.21-1.1+1}{1.1} = \frac{1.1}{2.21} + \frac{1.11}{1.1} = 0.4977 + 1.0091 = 1.5068$.

$S = 1.331 + 1/1.331 + 1 = 1.331 + 0.7513 + 1 = 3.0823$.

$S^{1/3} \approx 1.4553$ (since $1.455^3 \approx 3.081$). $1/S^{1/3} \approx 0.6872$.

$T - 3/2 = 0.0068$. $1/3^{1/3} - 1/S^{1/3} \approx 0.6934 - 0.6872 = 0.0062$.

$R \approx 0.0068/0.0062 \approx 1.097$.

Close to $1.0817$, slightly above. Good.

Let me try another family. $x = t, y = 1, z = 1/t$.

$xy = t, yz = 1/t, zx = 1$.

$T = \frac{t}{t+1} + \frac{1}{1/t+1} + \frac{1/t}{2} = \frac{t}{t+1} + \frac{t}{t+1} + \frac{1}{2t} = \frac{2t}{t+1} + \frac{1}{2t}$.

$S = t \cdot 1 + 1 \cdot 1/t^2 + 1/t \cdot t^2 = t + 1/t^2 + t = 2t + 1/t^2$.

At $t = 1$: $T = 1 + 1/2 = 3/2$, $S = 3$. ✓

$T' = \frac{2}{(t+1)^2} - \frac{1}{2t^2}$. At $t=1$: $2/4 - 1/2 = 0$. ✓

$T'' = -\frac{4}{(t+1)^3} + \frac{1}{t^3}$. At $t=1$: $-4/8 + 1 = 1/2$.

$S' = 2 - 2/t^3$. At $t=1$: $0$. $S'' = 6/t^4$. At $t=1$: $6$.

Ratio: $\frac{T''/2}{S''/(2 \cdot 3^{7/3})} = \frac{1/4}{6/(2 \cdot 3^{7/3})} = \frac{1/4}{3/3^{7/3}} = \frac{3^{7/3}}{12} = \frac{3^{4/3}}{4}$. ✓

Let me try $t = 2$ in this family:

$T = \frac{4}{3} + \frac{1}{4} = 1.5833$.

$S = 4 + 1/4 = 4.25$.

$S^{1/3} \approx 1.6199$. $1/S^{1/3} \approx 0.6173$.

$T - 3/2 = 0.0833$. $1/3^{1/3} - 1/S^{1/3} \approx 0.6934 - 0.6173 = 0.0761$.

$R \approx 0.0833/0.0761 \approx 1.095$.

Close to $1.0817$ but above. Good.

Let me try $t = 0.5$:

$T = \frac{1}{1.5} + 1 = 0.6667 + 1 = 1.6667$.

$S = 1 + 4 = 5$.

$S^{1/3} \approx 1.71$. $1/S^{1/3} \approx 0.5848$.

$T - 3/2 = 0.1667$. $1/3^{1/3} - 1/S^{1/3} \approx 0.6934 - 0.5848 = 0.1086$.

$R \approx 0.1667/0.1086 \approx 1.535$.

Above. Good.

So it seems like the minimum ratio is indeed $3^{4/3}/4$, achieved in the limit as we approach $x = y = z = 1$.

Now I need to prove this rigorously. Let me think about what approach might work.

One approach: Show that $T - 3/2 \ge \frac{3}{4}(1 - (3/S)^{1/3})$ (which is equivalent to our inequality with $k = 3^{4/3}/4$).

Actually, let me rewrite. We need:
$$T - \frac{3}{2} \ge \frac{3}{4}\left(1 - \left(\frac{3}{S}\right)^{1/3}\right)$$

where $S = xy^2 + yz^2 + zx^2 \ge 3$ and $T = \sum \frac{x}{xy+1}$.

Hmm, let me think about whether there's a way to relate $T$ and $S$ more directly.

Actually, let me try a different approach. Let me use the substitution $a = xy, b = yz, c = zx$ with $abc = 1$.

Then $x = \sqrt{ac/b}, y = \sqrt{ab/c}, z = \sqrt{bc/a}$.

$T = \frac{\sqrt{ac/b}}{a+1} + \frac{\sqrt{ab/c}}{b+1} + \frac{\sqrt{bc/a}}{c+1}$.

$S = xy^2 + yz^2 + zx^2$.

$xy^2 = a \cdot y = a\sqrt{ab/c} = a\sqrt{ab/c}$.

Hmm, $y = \sqrt{ab/c}$, so $xy^2 = x \cdot y^2 = \sqrt{ac/b} \cdot ab/c = a\sqrt{ab/c} \cdot \sqrt{ac/b} \cdot ... $

Actually, $xy^2 = (xy) \cdot y = a \cdot \sqrt{ab/c}$.

$yz^2 = (yz) \cdot z = b \cdot \sqrt{bc/a}$.

$zx^2 = (zx) \cdot x = c \cdot \sqrt{ac/b}$.

$S = a\sqrt{ab/c} + b\sqrt{bc/a} + c\sqrt{ac/b}$.

With $abc = 1$: $\sqrt{ab/c} = \sqrt{ab \cdot ab} = ab$ (since $c = 1/(ab)$). Wait, $abc = 1$ so $c = 1/(ab)$, and $ab/c = ab \cdot ab = (ab)^2$, so $\sqrt{ab/c} = ab$.

Similarly, $\sqrt{bc/a} = bc$ and $\sqrt{ac/b} = ac$.

So $S = a \cdot ab + b \cdot bc + c \cdot ac = a^2b + b^2c + c^2a$.

And $T = \frac{ac}{a+1} + \frac{ab}{b+1} + \frac{bc}{c+1}$... 

Wait: $\frac{\sqrt{ac/b}}{a+1} = \frac{ac}{a+1}$ (since $\sqrt{ac/b} = ac$ when $abc = 1$).

Let me verify: $\sqrt{ac/b}$. With $abc = 1$, $b = 1/(ac)$, so $ac/b = ac \cdot ac = (ac)^2$, $\sqrt{ac/b} = ac$. ✓

So $T = \frac{ac}{a+1} + \frac{ab}{b+1} + \frac{bc}{c+1}$ and $S = a^2b + b^2c + c^2a$ with $abc = 1$.

With $abc = 1$, we can write $a = p/q, b = q/r, c = r/p$ for some $p, q, r > 0$. Then:

$ac = r/q \cdot ... $ hmm, $a = p/q, c = r/p$, so $ac = r/q$.

$ab = p/r$, $bc = q/p$.

$T = \frac{r/q}{p/q+1} + \frac{p/r}{q/r+1} + \frac{q/p}{r/p+1} = \frac{r}{p+q} + \frac{p}{q+r} + \frac{q}{r+p}$.

Oh nice! $T = \frac{p}{q+r} + \frac{q}{r+p} + \frac{r}{p+q}$, which is exactly Nesbitt's expression!

And $S = a^2b + b^2c + c^2a = (p/q)^2 (q/r) + (q/r)^2 (r/p) + (r/p)^2 (p/q) = \frac{p^2}{qr} + \frac{q^2}{rp} + \frac{r^2}{pq} = \frac{p^3 + q^3 + r^3}{pqr}$.

So with the substitution $a = xy = p/q, b = yz = q/r, c = zx = r/p$ (and $abc = 1$), we get:

$$T = \sum_{cyc} \frac{p}{q+r}, \quad S = \frac{p^3 + q^3 + r^3}{pqr}$$

And we need to prove:
$$\sum_{cyc} \frac{p}{q+r} - \frac{3}{2} \ge \frac{3}{4}\left(1 - \left(\frac{3pqr}{p^3+q^3+r^3}\right)^{1/3}\right)$$

By Nesbitt's inequality, $\sum \frac{p}{q+r} \ge \frac{3}{2}$, so the LHS is non-negative. ✓

Now, $S = \frac{p^3+q^3+r^3}{pqr}$. By AM-GM, $p^3 + q^3 + r^3 \ge 3pqr$, so $S \ge 3$. ✓

Let me normalize. WLOG $p + q + r = 3$ (homogeneous). Actually, $T$ is homogeneous of degree 0, and $S$ is also homogeneous of degree 0. So we can normalize.

Let $p + q + r = 3$. Then $T = \sum \frac{p}{3-p}$ and $S = \frac{p^3+q^3+r^3}{pqr}$.

We need: $\sum \frac{p}{3-p} - \frac{3}{2} \ge \frac{3}{4}(1 - (3/S)^{1/3})$.

Note $p^3 + q^3 + r^3 = (p+q+r)^3 - 3(p+q+r)(pq+qr+rp) + 3pqr = 27 - 9(pq+qr+rp) + 3pqr$.

Let $\sigma = pq + qr + rp$ and $\pi = pqr$. Then $p^3+q^3+r^3 = 27 - 9\sigma + 3\pi$ and $S = \frac{27-9\sigma+3\pi}{\pi}$.

Also, $\sum \frac{p}{3-p} = \sum \frac{p}{q+r}$. With $p+q+r = 3$:

$\sum \frac{p}{3-p} = \sum \frac{p}{3-p}$.

$\frac{p}{3-p} = \frac{p}{q+r}$. $\sum \frac{p}{q+r} = \frac{p(q+r)(r+p) + q(r+p)(p+q) + r(p+q)(q+r)}{(p+q)(q+r)(r+p)}$... 

Actually, $\sum \frac{p}{q+r} = \frac{p^2+pq+pr + q^2+qr+qp + r^2+rq+rp}{(p+q)(q+r)(r+p)} \cdot ...$

Hmm, let me just use the known formula. $\sum \frac{p}{q+r} = \frac{p(q+r)(p+q) + ... }{...}$... this is getting complicated.

Let me try a different approach. Since both sides are symmetric in $p, q, r$ (wait, is $S$ symmetric? $S = \frac{p^3+q^3+r^3}{pqr}$ is symmetric, and $T = \sum \frac{p}{q+r}$ is symmetric), the problem is symmetric.

By the method of Lagrange multipliers or by the theory of symmetric inequalities, the extremum might occur when two variables are equal. Let me check: set $q = r$, $p + 2q = 3$.

$T = \frac{p}{2q} + \frac{2q}{p+q} = \frac{p}{2q} + \frac{2q}{p+q}$.

With $p = 3 - 2q$: $T = \frac{3-2q}{2q} + \frac{2q}{3-q}$.

$S = \frac{(3-2q)^3 + 2q^3}{(3-2q)q^2}$.

At $q = 1$ (so $p = 1$): $T = 1/2 + 2/2 = 3/2$, $S = 3/1 = 3$. ✓

Let me compute the ratio for $q$ near 1. Let $q = 1 + \epsilon$, $p = 1 - 2\epsilon$.

$T = \frac{1-2\epsilon}{2(1+\epsilon)} + \frac{2(1+\epsilon)}{2-\epsilon}$.

$\frac{1-2\epsilon}{2+2\epsilon} = \frac{1}{2} \cdot \frac{1-2\epsilon}{1+\epsilon} \approx \frac{1}{2}(1-2\epsilon)(1-\epsilon) \approx \frac{1}{2}(1-3\epsilon) = \frac{1}{2} - \frac{3\epsilon}{2}$.

$\frac{2+2\epsilon}{2-\epsilon} = \frac{2(1+\epsilon)}{2-\epsilon} \approx (1+\epsilon)(1+\epsilon/2) \approx 1 + \frac{3\epsilon}{2}$.

$T \approx \frac{1}{2} - \frac{3\epsilon}{2} + 1 + \frac{3\epsilon}{2} = \frac{3}{2}$. 

Hmm, first order cancels. Let me go to second order.

$\frac{1-2\epsilon}{2(1+\epsilon)} = \frac{1}{2}(1-2\epsilon)(1-\epsilon+\epsilon^2) \approx \frac{1}{2}(1 - 3\epsilon + 3\epsilon^2)$.

$\frac{2(1+\epsilon)}{2-\epsilon} = (1+\epsilon)(1+\epsilon/2+\epsilon^2/4) \approx 1 + \frac{3\epsilon}{2} + \frac{3\epsilon^2}{4}$.

$T \approx \frac{1}{2} - \frac{3\epsilon}{2} + \frac{3\epsilon^2}{2} + 1 + \frac{3\epsilon}{2} + \frac{3\epsilon^2}{4} = \frac{3}{2} + \frac{9\epsilon^2}{4}$.

$S = \frac{(1-2\epsilon)^3 + 2(1+\epsilon)^3}{(1-2\epsilon)(1+\epsilon)^2}$.

Numerator: $(1-6\epsilon+12\epsilon^2) + 2(1+3\epsilon+3\epsilon^2) = 1-6\epsilon+12\epsilon^2+2+6\epsilon+6\epsilon^2 = 3+18\epsilon^2$.

Denominator: $(1-2\epsilon)(1+2\epsilon+\epsilon^2) = 1+2\epsilon+\epsilon^2-2\epsilon-4\epsilon^2 = 1-3\epsilon^2$.

$S \approx \frac{3+18\epsilon^2}{1-3\epsilon^2} \approx (3+18\epsilon^2)(1+3\epsilon^2) \approx 3 + 27\epsilon^2$.

$S - 3 \approx 27\epsilon^2$.

$1 - (3/S)^{1/3} = 1 - (3/(3+27\epsilon^2))^{1/3} = 1 - (1/(1+9\epsilon^2))^{1/3} \approx 1 - (1-3\epsilon^2) = 3\epsilon^2$.

RHS: $\frac{3}{4} \cdot 3\epsilon^2 = \frac{9\epsilon^2}{4}$.

LHS: $T - 3/2 = \frac{9\epsilon^2}{4}$.

So LHS = RHS to second order! This confirms the tightness.

Now, the fact that equality holds to second order in all directions strongly suggests that $k = 3^{4/3}/4$ is the answer, and the inequality is tight (equality only at $p = q = r$, but the ratio approaches $3^{4/3}/4$ from above in all directions).

Now I need to prove the inequality. Let me think about this.

We need to prove: $\sum \frac{p}{q+r} - \frac{3}{2} \ge \frac{3}{4}(1 - (3/S)^{1/3})$ where $S = \frac{p^3+q^3+r^3}{pqr}$.

Equivalently: $\sum \frac{p}{q+r} \ge \frac{3}{2} + \frac{3}{4}(1 - (3/S)^{1/3}) = \frac{3}{4}(3 - (3/S)^{1/3})$.

Hmm, let me think about using the power mean inequality or Schur's inequality.

Actually, let me try a tangent line approach. We want to show $f(p,q,r) \ge 0$ where 

$f = \sum \frac{p}{q+r} - \frac{3}{2} - \frac{3}{4}(1 - (3/S)^{1/3})$.

Since this is symmetric and homogeneous of degree 0, we can set $p + q + r = 3$ and $p, q, r > 0$.

With this normalization, $S = \frac{p^3+q^3+r^3}{pqr}$ and $T = \sum \frac{p}{3-p}$.

Note $p^3 + q^3 + r^3 = 27 - 9\sigma + 3\pi$ where $\sigma = pq+qr+rp, \pi = pqr$.

$T = \sum \frac{p}{3-p}$. Let me compute this in terms of $\sigma$ and $\pi$.

$\sum \frac{p}{3-p} = \sum \frac{p}{q+r} = \frac{\sum p(p+q)(p+r)}{(p+q)(q+r)(r+p)}$.

Numerator: $\sum p(p+q)(p+r) = \sum p(p^2 + p(q+r) + qr) = \sum p^3 + \sum p^2(q+r) + \sum pqr$.

$= (p^3+q^3+r^3) + (p^2 q + p^2 r + q^2 p + q^2 r + r^2 p + r^2 q) + 3pqr$.

$= (p^3+q^3+r^3) + (p+q+r)(pq+qr+rp) - 3pqr + 3pqr$... 

Wait, $p^2q + p^2r + q^2p + q^2r + r^2p + r^2q = (p+q+r)(pq+qr+rp) - 3pqr$.

So numerator $= (p^3+q^3+r^3) + (p+q+r)(pq+qr+rp) - 3pqr + 3pqr = (p^3+q^3+r^3) + (p+q+r)\sigma$.

With $p+q+r = 3$: numerator $= (27 - 9\sigma + 3\pi) + 3\sigma = 27 - 6\sigma + 3\pi$.

Denominator: $(p+q)(q+r)(r+p) = (p+q+r)(pq+qr+rp) - pqr = 3\sigma - \pi$.

So $T = \frac{27 - 6\sigma + 3\pi}{3\sigma - \pi}$.

And $S = \frac{27 - 9\sigma + 3\pi}{\pi}$.

We need: $\frac{27 - 6\sigma + 3\pi}{3\sigma - \pi} - \frac{3}{2} \ge \frac{3}{4}(1 - (\frac{3\pi}{27-9\sigma+3\pi})^{1/3})$.

LHS: $\frac{2(27-6\sigma+3\pi) - 3(3\sigma-\pi)}{2(3\sigma-\pi)} = \frac{54-12\sigma+6\pi-9\sigma+3\pi}{2(3\sigma-\pi)} = \frac{54-21\sigma+9\pi}{2(3\sigma-\pi)} = \frac{3(18-7\sigma+3\pi)}{2(3\sigma-\pi)}$.

At $p=q=r=1$: $\sigma = 3, \pi = 1$. LHS $= \frac{3(18-21+3)}{2(9-1)} = \frac{3 \cdot 0}{16} = 0$. ✓

Let me denote $u = \sigma, v = \pi$ for convenience. With $p+q+r = 3$, we have $0 < u \le 3$ and $0 < v \le 1$ (by AM-GM), with the constraint that $u^2 \ge 3v$ (Schur-like) and $u \le 3$.

Actually, the constraints on $(u, v)$ for $p, q, r > 0$ with $p+q+r = 3$ are: $0 < u \le 3$, $0 < v \le 1$, and the discriminant condition. But let me not worry about exact constraints for now.

We need: $\frac{3(18-7u+3v)}{2(3u-v)} \ge \frac{3}{4}(1 - (\frac{3v}{27-9u+3v})^{1/3})$.

Simplify: $\frac{2(18-7u+3v)}{3u-v} \ge 1 - (\frac{v}{9-3u+v})^{1/3}$.

Let me denote $w = 9 - 3u + v = \frac{p^3+q^3+r^3}{3}$. Note $w \ge v$ (since $p^3+q^3+r^3 \ge 3pqr$), so $\frac{v}{w} \le 1$.

Also, $18 - 7u + 3v = 18 - 7u + 3v$. And $3u - v = 3u - v$.

At $u = 3, v = 1$: $18 - 21 + 3 = 0$, $9 - 1 = 8$. LHS = 0. And $w = 9 - 9 + 1 = 1$, $v/w = 1$, RHS = 0. ✓

Let me try to express things in terms of $w$ and $v$. We have $w = 9 - 3u + v$, so $u = \frac{9 + v - w}{3}$.

$3u - v = 9 + v - w - v = 9 - w$.

$18 - 7u + 3v = 18 - \frac{7(9+v-w)}{3} + 3v = 18 - \frac{63+7v-7w}{3} + 3v = \frac{54 - 63 - 7v + 7w + 9v}{3} = \frac{-9 + 2v + 7w}{3}$.

So LHS $= \frac{2(-9+2v+7w)/3}{9-w} = \frac{2(-9+2v+7w)}{3(9-w)}$.

RHS $= 1 - (v/w)^{1/3}$.

So we need: $\frac{2(7w + 2v - 9)}{3(9-w)} \ge 1 - (v/w)^{1/3}$.

Note $w \ge v > 0$ and $w \le 9$ (since $u \ge 0$... actually $u > 0$ so $w < 9 + v$, but $w = 9 - 3u + v < 9 + v$). Also $w \ge 1$ (since $w = (p^3+q^3+r^3)/3 \ge (p+q+r)^3/27 \cdot 3 = 1$ by power mean... actually $p^3+q^3+r^3 \ge (p+q+r)^3/9 = 3$ by power mean, so $w \ge 1$).

At $w = 1, v = 1$: LHS $= \frac{2(7+2-9)}{3 \cdot 8} = 0$, RHS $= 1 - 1 = 0$. ✓

Let me set $t = v/w \in (0, 1]$. Then $v = tw$.

LHS $= \frac{2(7w + 2tw - 9)}{3(9-w)} = \frac{2w(7+2t) - 18}{3(9-w)}$.

RHS $= 1 - t^{1/3}$.

We need: $\frac{2w(7+2t) - 18}{3(9-w)} \ge 1 - t^{1/3}$.

$2w(7+2t) - 18 \ge 3(9-w)(1-t^{1/3})$

$2w(7+2t) - 18 \ge 27 - 27t^{1/3} - 3w + 3wt^{1/3}$

$2w(7+2t) + 3w - 3wt^{1/3} \ge 45 - 27t^{1/3}$

$w(14 + 4t + 3 - 3t^{1/3}) \ge 45 - 27t^{1/3}$

$w(17 + 4t - 3t^{1/3}) \ge 45 - 27t^{1/3}$

$w \ge \frac{45 - 27t^{1/3}}{17 + 4t - 3t^{1/3}}$

Now, we need to find the minimum value of $w$ given $t = v/w$. 

Recall $w = (p^3+q^3+r^3)/3$ and $v = pqr$ with $p+q+r = 3$. And $t = v/w = 3pqr/(p^3+q^3+r^3)$.

By AM-GM, $p^3+q^3+r^3 \ge 3pqr$, so $t \le 1$.

We need to find the minimum of $w$ for a given $t$. This is an optimization problem.

Actually, let me think about this differently. We have the constraint that $p, q, r > 0$ with $p + q + r = 3$, and we've expressed everything in terms of $w$ and $t$. The question is: for a given $t \in (0, 1]$, what is the minimum possible $w$?

By the method of Lagrange multipliers (or by the theory of symmetric functions), the extremum of $w = (p^3+q^3+r^3)/3$ subject to $p+q+r = 3$ and $pqr/(p^3+q^3+r^3) = t/3$ (i.e., $v/w = t$) occurs when two of $p, q, r$ are equal.

So let $q = r$, $p + 2q = 3$, $p = 3 - 2q$ with $0 < q < 3/2$.

$w = \frac{(3-2q)^3 + 2q^3}{3}$, $v = (3-2q)q^2$, $t = \frac{3(3-2q)q^2}{(3-2q)^3 + 2q^3}$.

At $q = 1$: $w = 1, v = 1, t = 1$. ✓

As $q \to 0$: $w \to 9, v \to 0, t \to 0$.

As $q \to 3/2$: $p \to 0$, $w \to 2(3/2)^3/3 = 2 \cdot 27/8 / 3 = 9/4$, $v \to 0$, $t \to 0$.

So for a given $t$, the minimum $w$ is achieved at the boundary of the two-equal curve. But actually, for a given $t$, there might be two values of $q$ giving the same $t$, and we want the one with smaller $w$.

This is getting complicated. Let me try a different approach.

Let me go back to the inequality: $w(17 + 4t - 3t^{1/3}) \ge 45 - 27t^{1/3}$ where $t = v/w$.

We need to show this holds for all valid $(w, t)$ coming from $p, q, r > 0$ with $p+q+r=3$.

Since $w \ge 1$ (by power mean) and $t \le 1$, and $17 + 4t - 3t^{1/3} > 0$ for $t \in (0, 1]$ (at $t=1$: $17+4-3 = 18 > 0$), we need:

$w \ge \frac{45 - 27t^{1/3}}{17 + 4t - 3t^{1/3}} := \phi(t)$.

So we need to show $w \ge \phi(t)$ for all valid $(w, t)$.

At $t = 1$: $\phi(1) = \frac{45-27}{17+4-3} = \frac{18}{18} = 1 = w$. ✓ (equality)

So we need $w \ge \phi(t)$, and at $t = 1$ we have equality. 

Now, the question is: is $\phi(t) \le w_{min}(t)$ where $w_{min}(t)$ is the minimum $w$ for a given $t$?

Actually, let me think about this more carefully. The relationship between $w$ and $t$ is constrained by the fact that they come from $p, q, r > 0$ with $p + q + r = 3$. 

Let me parametrize by $q = r$ (two equal). Then $p = 3 - 2q$, and:

$w = \frac{(3-2q)^3 + 2q^3}{3} = \frac{27 - 54q + 36q^2 - 8q^3 + 2q^3}{3} = \frac{27 - 54q + 36q^2 - 6q^3}{3} = 9 - 18q + 12q^2 - 2q^3$.

$v = (3-2q)q^2 = 3q^2 - 2q^3$.

$t = v/w = \frac{3q^2 - 2q^3}{9 - 18q + 12q^2 - 2q^3} = \frac{q^2(3-2q)}{9 - 18q + 12q^2 - 2q^3}$.

At $q = 1$: $t = 1/1 = 1$, $w = 9 - 18 + 12 - 2 = 1$. ✓

Let me compute $dw/dt$ along this curve at $q = 1$.

$dw/dq = -18 + 24q - 6q^2$. At $q=1$: $-18+24-6 = 0$.

$dv/dq = 6q - 6q^2$. At $q=1$: $0$.

$t = v/w$, $dt/dq = (v'w - vw')/w^2$. At $q=1$: $(0 \cdot 1 - 1 \cdot 0)/1 = 0$.

So both $dw/dq$ and $dt/dq$ are 0 at $q=1$. Need second order.

$w'' = 24 - 12q$. At $q=1$: $12$. So $w \approx 1 + 6(q-1)^2$.

$v'' = 6 - 12q$. At $q=1$: $-6$. So $v \approx 1 - 3(q-1)^2$.

$t = v/w \approx (1-3\epsilon^2)/(1+6\epsilon^2) \approx 1 - 9\epsilon^2$.

So $1 - t \approx 9\epsilon^2$ and $w - 1 \approx 6\epsilon^2$. Thus $w - 1 \approx \frac{6}{9}(1-t) = \frac{2}{3}(1-t)$.

Now $\phi(t)$ near $t = 1$: Let $t = 1 - \delta$.

$\phi(t) = \frac{45 - 27t^{1/3}}{17 + 4t - 3t^{1/3}}$.

$t^{1/3} \approx 1 - \delta/3$.

Numerator: $45 - 27(1-\delta/3) = 45 - 27 + 9\delta = 18 + 9\delta$.

Denominator: $17 + 4(1-\delta) - 3(1-\delta/3) = 17 + 4 - 4\delta - 3 + \delta = 18 - 3\delta$.

$\phi \approx \frac{18+9\delta}{18-3\delta} \approx (1+\delta/2)(1+\delta/6) \approx 1 + \frac{2\delta}{3}$.

So $\phi(t) \approx 1 + \frac{2}{3}\delta = 1 + \frac{2}{3}(1-t)$.

And $w \approx 1 + \frac{2}{3}(1-t)$.

So $w \approx \phi(t)$ to second order! This means the inequality $w \ge \phi(t)$ is tight to second order at $t = 1$ along the two-equal curve.

This is very strong evidence that the inequality holds, but I need to prove it rigorously.

Let me try to prove $w \ge \phi(t)$, i.e., $w(17 + 4t - 3t^{1/3}) \ge 45 - 27t^{1/3}$, where $t = v/w = 3pqr/(p^3+q^3+r^3)$ and $w = (p^3+q^3+r^3)/3$.

Substituting $t = v/w$:

$w(17 + 4v/w - 3(v/w)^{1/3}) \ge 45 - 27(v/w)^{1/3}$

$17w + 4v - 3w(v/w)^{1/3} \ge 45 - 27(v/w)^{1/3}$

$17w + 4v - 3w^{2/3}v^{1/3} \ge 45 - 27v^{1/3}w^{-1/3}$

$17w + 4v - 3w^{2/3}v^{1/3} + 27v^{1/3}w^{-1/3} \ge 45$

Let $s = (v/w)^{1/3} = t^{1/3}$. Then $v = s^3 w$ and:

$17w + 4s^3 w - 3w \cdot s + 27s \ge 45$

$w(17 + 4s^3 - 3s) + 27s \ge 45$

$w \ge \frac{45 - 27s}{17 + 4s^3 - 3s}$

where $s = (v/w)^{1/3} \in (0, 1]$.

Now, $w = (p^3+q^3+r^3)/3$ and $v = pqr$ with $p+q+r=3$.

$s^3 = v/w = 3pqr/(p^3+q^3+r^3)$.

By AM-GM, $p^3+q^3+r^3 \ge 3pqr$, so $s^3 \le 1$, i.e., $s \le 1$. ✓

Now I need to show $w \ge \frac{45-27s}{17+4s^3-3s}$ for all valid $(w, s)$.

Note that $17 + 4s^3 - 3s > 0$ for $s \in (0, 1]$ (at $s=0$: 17, at $s=1$: 18).

And $45 - 27s > 0$ for $s \in (0, 1]$ (at $s=1$: 18).

At $s = 1$: $\phi = 18/18 = 1 = w_{min}$. ✓

The key question: for a given $s$, what is the minimum $w$?

We have $w = (p^3+q^3+r^3)/3$ and $s^3 = 3pqr/(p^3+q^3+r^3) = v/w$, so $v = s^3 w$.

With $p+q+r = 3$, $pq+qr+rp = \sigma$, $pqr = v = s^3 w$:

$w = (27 - 9\sigma + 3v)/3 = 9 - 3\sigma + v = 9 - 3\sigma + s^3 w$.

$w(1 - s^3) = 9 - 3\sigma$

$\sigma = \frac{9 - w(1-s^3)}{3} = 3 - \frac{w(1-s^3)}{3}$.

For $p, q, r$ to be real positive with $p+q+r = 3$ and $pq+qr+rp = \sigma$, $pqr = v$, we need the discriminant to be non-negative, and $\sigma \le 3$ (by $(p+q+r)^2 \ge 3\sigma$, i.e., $9 \ge 3\sigma$), and $\sigma > 0$, and $v > 0$.

Also, by Schur's inequality: $p^3+q^3+r^3 + pqr \ge (p+q+r)(pq+qr+rp)$, i.e., $3w + v \ge 3\sigma$, i.e., $3w + s^3 w \ge 3\sigma = 9 - w(1-s^3)$, i.e., $w(3 + s^3 + 1 - s^3) \ge 9$, i.e., $4w \ge 9$, i.e., $w \ge 9/4$.

Wait, that gives $w \ge 9/4$? But at $p=q=r=1$, $w = 1 < 9/4$. Let me recheck.

Schur's inequality (degree 3): $p^3+q^3+r^3 + pqr \ge (p+q+r)(pq+qr+rp)$ for $p, q, r \ge 0$.

At $p=q=r=1$: $3 + 1 = 4 \ge 3 \cdot 3 = 9$? That's $4 \ge 9$, which is false!

Hmm, Schur's inequality is $p^t(p-q)(p-r) + q^t(q-p)(q-r) + r^t(r-p)(r-q) \ge 0$ for $t \ge 0$.

For $t = 1$: $\sum p(p-q)(p-r) \ge 0$, which expands to $p^3+q^3+r^3 + pqr \ge (p+q+r)(pq+qr+rp)$... 

Wait, let me expand $\sum p(p-q)(p-r) = \sum p(p^2 - pr - pq + qr) = \sum (p^3 - p^2r - p^2q + pqr) = (p^3+q^3+r^3) - (p^2q+p^2r+q^2p+q^2r+r^2p+r^2q) + 3pqr$.

$= (p^3+q^3+r^3) - (p+q+r)(pq+qr+rp) + 3pqr + 3pqr$... 

Hmm, $p^2q + p^2r + q^2p + q^2r + r^2p + r^2q = (p+q+r)(pq+qr+rp) - 3pqr$.

So $\sum p(p-q)(p-r) = (p^3+q^3+r^3) - (p+q+r)\sigma + 3pqr + 3pqr = (p^3+q^3+r^3) - (p+q+r)\sigma + 3pqr$.

Wait: $(p^3+q^3+r^3) - [(p+q+r)\sigma - 3pqr] + 3pqr = (p^3+q^3+r^3) - (p+q+r)\sigma + 3pqr + 3pqr$?

No. $\sum p(p-q)(p-r) = \sum (p^3 - p^2q - p^2r + pqr) = (p^3+q^3+r^3) - \sum(p^2q + p^2r) + 3pqr$.

$\sum(p^2q + p^2r) = p^2(q+r) + q^2(p+r) + r^2(p+q) = p^2(3-p) + q^2(3-q) + r^2(3-r) = 3(p^2+q^2+r^2) - (p^3+q^3+r^3)$.

$= 3 \cdot 9 -        — AI历史解题过程（thinking）
#   polymath_01849         — 题目ID

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
  <problem_id>polymath_01849</problem_id>
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

Find the largest value of $k$ such that the following inequality holds for all $x, y, z > 0$ with $xyz = 1$:
\[
\sum_{cyc} \frac{x}{xy+1} + \frac{k}{\sqrt[3]{xy^2 + yz^2 + zx^2}} \ge \frac{3}{2} + \frac{k}{\sqrt[3]{3}}
\]
Let $k_{max}$ be this maximum value. Find $(2 \cdot k_{max})^3$.

## Standard Solution

To find the largest $k$, we examine the limit of the expression as $x \to \infty$ with $y = 1$ and $z = 1/x$. 
The sum $\sum \frac{x}{xy+1}$ approaches $1 + 1 + 0 = 2$. 
The expression $\sum xy^2$ becomes $x + \frac{1}{x^2} + x$, which approaches $2x$ and thus $\frac{1}{\sqrt[3]{\sum xy^2}}$ approaches 0.
The inequality then requires $2 \ge \frac{3}{2} + \frac{k}{\sqrt[3]{3}}$, which simplifies to $\frac{1}{2} \ge \frac{k}{\sqrt[3]{3}}$, or $k \le \frac{\sqrt[3]{3}}{2}$.
The solution confirms that $k_{max} = \frac{\sqrt[3]{3}}{2}$. 
Therefore, $(2 \cdot k_{max})^3 = (2 \cdot \frac{\sqrt[3]{3}}{2})^3 = (\sqrt[3]{3})^3 = 3$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We need to find the largest $k$ such that for all $x, y, z > 0$ with $xyz = 1$:
$$\sum_{cyc} \frac{x}{xy+1} + \frac{k}{\sqrt[3]{xy^2 + yz^2 + zx^2}} \ge \frac{3}{2} + \frac{k}{\sqrt[3]{3}}$$

Let me first check for answer leaks. The problem statement doesn't contain any solutions, proof sketches, or answer values. Good.

Let me think about this problem. At $x = y = z = 1$, we have $xyz = 1$, and:
- $\sum_{cyc} \frac{x}{xy+1} = \frac{1}{1+1} \cdot 3 = \frac{3}{2}$
- $xy^2 + yz^2 + zx^2 = 1 + 1 + 1 = 3$, so $\sqrt[3]{3}$
- So equality holds at $x = y = z = 1$.

So the inequality is tight at $x = y = z = 1$. We need to find the largest $k$ such that this holds.

Let me rewrite. Let $f(x,y,z) = \sum_{cyc} \frac{x}{xy+1}$ and $g(x,y,z) = \frac{1}{\sqrt[3]{xy^2 + yz^2 + zx^2}}$.

The inequality is $f + k \cdot g \ge \frac{3}{2} + \frac{k}{\sqrt[3]{3}}$.

At $x=y=z=1$: $f = 3/2$, $g = 1/\sqrt[3]{3}$, so equality.

We want the largest $k$ such that $f - 3/2 \ge k(1/\sqrt[3]{3} - g)$ for all $x,y,z > 0$ with $xyz=1$.

Note $g = 1/\sqrt[3]{xy^2 + yz^2 + zx^2}$. By AM-GM, $xy^2 + yz^2 + zx^2 \ge 3\sqrt[3]{xy^2 \cdot yz^2 \cdot zx^2} = 3\sqrt[3]{x^3 y^3 z^3} = 3xyz = 3$. So $xy^2 + yz^2 + zx^2 \ge 3$, meaning $g \le 1/\sqrt[3]{3}$, so $1/\sqrt[3]{3} - g \ge 0$.

So we need $k \le \frac{f - 3/2}{1/\sqrt[3]{3} - g}$ for all points where $g < 1/\sqrt[3]{3}$ (i.e., not at $x=y=z=1$).

So $k_{max} = \inf_{x,y,z: xyz=1, \text{not all equal}} \frac{f - 3/2}{1/\sqrt[3]{3} - g}$.

Wait, but we also need $f - 3/2 \ge 0$ for this to work. Let me check: is $f = \sum_{cyc} \frac{x}{xy+1} \ge 3/2$ always?

With $xyz = 1$, let's substitute. Let $x = a/b, y = b/c, z = c/a$ for some $a, b, c > 0$. Then $xyz = 1$.

$xy = a/c$, $yz = b/a$, $zx = c/b$.

$\frac{x}{xy+1} = \frac{a/b}{a/c + 1} = \frac{a/b \cdot c}{a + c} = \frac{ac}{b(a+c)}$.

Hmm, this is getting complicated. Let me try another substitution.

Actually, let me try the substitution $x = a/b, y = b/c, z = c/a$.

$\sum_{cyc} \frac{x}{xy+1} = \frac{a/b}{a/c+1} + \frac{b/c}{b/a+1} + \frac{c/a}{c/b+1}$

$= \frac{ac}{b(a+c)} + \frac{ab}{c(a+b)} + \frac{bc}{a(b+c)}$

Hmm. Let me try a different approach. Let me check if $f \ge 3/2$.

Actually, let me try $x = t, y = t, z = 1/t^2$ for large $t$.

$xy = t^2$, $yz = 1/t$, $zx = 1/t$.

$f = \frac{t}{t^2+1} + \frac{t}{1/t+1} + \frac{1/t^2}{1/t+1}$

$= \frac{t}{t^2+1} + \frac{t^2}{1+t} + \frac{1}{t^2(1/t+1)} = \frac{t}{t^2+1} + \frac{t^2}{1+t} + \frac{1}{t(1+t)}$

$= \frac{t}{t^2+1} + \frac{t^3 + 1}{t(1+t)} = \frac{t}{t^2+1} + \frac{(t+1)(t^2-t+1)}{t(t+1)} = \frac{t}{t^2+1} + \frac{t^2-t+1}{t}$

$= \frac{t}{t^2+1} + t - 1 + \frac{1}{t}$

For large $t$, this is approximately $t - 1 \to \infty$. So $f \to \infty$, good.

Now $xy^2 + yz^2 + zx^2 = t \cdot t^2 + t \cdot 1/t^4 + 1/t^2 \cdot t^2 = t^3 + 1/t^3 + 1$.

For large $t$, this is approximately $t^3$, so $g \approx 1/t$, and $1/\sqrt[3]{3} - g \to 1/\sqrt[3]{3}$.

So the ratio $\frac{f - 3/2}{1/\sqrt[3]{3} - g} \to \infty$ as $t \to \infty$. So the infimum is not at infinity in this direction.

Let me try near $x = y = z = 1$. Let $x = 1+a, y = 1+b, z = 1+c$ with small perturbations and $xyz = 1$.

Actually, let me use the parametrization $x = e^u, y = e^v, z = e^w$ with $u + v + w = 0$.

At $u = v = w = 0$, we have the equality point. Let me expand to second order.

Let me set $u = s, v = -s, w = 0$ (so $x = e^s, y = e^{-s}, z = 1$).

$xy = 1, yz = e^{-s}, zx = e^s$.

$f = \frac{e^s}{1+1} + \frac{e^{-s}}{e^{-s}+1} + \frac{1}{e^s+1} = \frac{e^s}{2} + \frac{1}{1+e^s} + \frac{1}{e^s+1}$

Wait: $\frac{e^{-s}}{e^{-s}+1} = \frac{1}{1+e^s}$ and $\frac{1}{e^s+1}$.

So $f = \frac{e^s}{2} + \frac{2}{1+e^s}$.

At $s=0$: $f = 1/2 + 1 = 3/2$. Good.

$f' = \frac{e^s}{2} - \frac{2e^s}{(1+e^s)^2}$. At $s=0$: $1/2 - 2/4 = 1/2 - 1/2 = 0$. Good.

$f'' = \frac{e^s}{2} - \frac{2e^s(1+e^s)^2 - 2e^s \cdot 2(1+e^s)e^s}{(1+e^s)^4} = \frac{e^s}{2} - \frac{2e^s(1+e^s) - 4e^{2s}}{(1+e^s)^3}$

At $s=0$: $1/2 - \frac{2 \cdot 2 - 4}{8} = 1/2 - 0 = 1/2$.

Now $g$: $xy^2 + yz^2 + zx^2 = e^s \cdot e^{-2s} + e^{-s} \cdot 1 + 1 \cdot e^{2s} = e^{-s} + e^{-s} + e^{2s} = 2e^{-s} + e^{2s}$.

At $s=0$: $2 + 1 = 3$. Good.

$h(s) = 2e^{-s} + e^{2s}$. $h'(s) = -2e^{-s} + 2e^{2s}$. At $s=0$: $-2 + 2 = 0$. Good.

$h''(s) = 2e^{-s} + 4e^{2s}$. At $s=0$: $2 + 4 = 6$.

So $h(s) \approx 3 + 3s^2$.

$g = h^{-1/3} \approx 3^{-1/3}(1 + s^2)^{-1/3} \approx 3^{-1/3}(1 - s^2/3)$.

So $1/\sqrt[3]{3} - g \approx 3^{-1/3} \cdot s^2/3 = s^2/(3 \cdot 3^{1/3}) = s^2/3^{4/3}$.

And $f - 3/2 \approx s^2/4$.

So the ratio near $s = 0$ is $\frac{s^2/4}{s^2/3^{4/3}} = \frac{3^{4/3}}{4}$.

So $k_{max} \le \frac{3^{4/3}}{4}$.

But wait, I need to check other directions. Let me try $u = s, v = s, w = -2s$ (so $x = e^s, y = e^s, z = e^{-2s}$).

$xy = e^{2s}, yz = e^{-s}, zx = e^{-s}$.

$f = \frac{e^s}{e^{2s}+1} + \frac{e^s}{e^{-s}+1} + \frac{e^{-2s}}{e^{-s}+1}$

$= \frac{e^s}{e^{2s}+1} + \frac{e^{2s}}{1+e^s} + \frac{e^{-s}}{1+e^s}$

$= \frac{e^s}{e^{2s}+1} + \frac{e^{2s}+e^{-s}}{1+e^s}$

At $s=0$: $1/2 + 2/2 = 3/2$. Good.

$f' = \frac{e^s(e^{2s}+1) - e^s \cdot 2e^{2s}}{(e^{2s}+1)^2} + \frac{(2e^{2s}-e^{-s})(1+e^s) - (e^{2s}+e^{-s})e^s}{(1+e^s)^2}$

At $s=0$: First term: $\frac{1 \cdot 2 - 1 \cdot 2}{4} = 0$. Second term: $\frac{(2-1) \cdot 2 - 2 \cdot 1}{4} = \frac{2-2}{4} = 0$. Good.

$f''$: Let me compute each part.

First term: $A(s) = \frac{e^s}{e^{2s}+1}$. $A'(s) = \frac{e^s(1-e^{2s})}{(e^{2s}+1)^2}$.

$A''(s) = \frac{[e^s(1-e^{2s}) - 2e^{3s}](e^{2s}+1)^2 - e^s(1-e^{2s}) \cdot 2(e^{2s}+1) \cdot 2e^{2s}}{(e^{2s}+1)^4}$

At $s=0$: numerator of $A'$ part: $e^s(1-e^{2s}) = 0$ at $s=0$. So $A''(0) = \frac{[1 \cdot (1-1) - 2](4) - 0}{16} = \frac{-2 \cdot 4}{16} = \frac{-8}{16} = -1/2$.

Hmm wait, let me redo. $A'(s) = \frac{e^s - e^{3s}}{(e^{2s}+1)^2}$.

$A''(s) = \frac{(e^s - 3e^{3s})(e^{2s}+1)^2 - (e^s - e^{3s}) \cdot 2(e^{2s}+1)(2e^{2s})}{(e^{2s}+1)^4}$

At $s=0$: $(1-3)(4) - 0 = -8$. Divided by $16$: $-1/2$.

Second term: $B(s) = \frac{e^{2s}+e^{-s}}{1+e^s}$.

$B'(s) = \frac{(2e^{2s}-e^{-s})(1+e^s) - (e^{2s}+e^{-s})e^s}{(1+e^s)^2}$

At $s=0$: $\frac{(2-1)(2) - 2 \cdot 1}{4} = \frac{2-2}{4} = 0$. Good.

$B''(s)$: Let me compute the numerator $N(s) = (2e^{2s}-e^{-s})(1+e^s) - (e^{2s}+e^{-s})e^s$.

$N(s) = 2e^{2s} + 2e^{3s} - e^{-s} - 1 - e^{3s} - 1 = 2e^{2s} + e^{3s} - e^{-s} - 2$.

Wait let me redo: $(2e^{2s}-e^{-s})(1+e^s) = 2e^{2s} + 2e^{3s} - e^{-s} - 1$.

$(e^{2s}+e^{-s})e^s = e^{3s} + 1$.

$N(s) = 2e^{2s} + 2e^{3s} - e^{-s} - 1 - e^{3s} - 1 = 2e^{2s} + e^{3s} - e^{-s} - 2$.

$N'(s) = 4e^{2s} + 3e^{3s} + e^{-s}$. At $s=0$: $4 + 3 + 1 = 8$.

$B''(s) = \frac{N'(s)(1+e^s)^2 - N(s) \cdot 2(1+e^s)e^s}{(1+e^s)^4}$

At $s=0$: $N(0) = 2 + 1 - 1 - 2 = 0$. So $B''(0) = \frac{8 \cdot 4 - 0}{16} = 2$.

So $f''(0) = A''(0) + B''(0) = -1/2 + 2 = 3/2$.

Now $h(s) = xy^2 + yz^2 + zx^2 = e^s \cdot e^{2s} + e^s \cdot e^{-4s} + e^{-2s} \cdot e^{2s} = e^{3s} + e^{-3s} + 1$.

$h(0) = 3$. $h'(0) = 3 - 3 = 0$. $h''(0) = 9 + 9 = 18$.

So $h(s) \approx 3 + 9s^2$.

$g \approx 3^{-1/3}(1 + 3s^2)^{-1/3} \approx 3^{-1/3}(1 - s^2)$.

$1/\sqrt[3]{3} - g \approx 3^{-1/3} s^2 = s^2/3^{1/3}$.

$f - 3/2 \approx (3/2)s^2/2 = 3s^2/4$.

Ratio: $\frac{3s^2/4}{s^2/3^{1/3}} = \frac{3 \cdot 3^{1/3}}{4} = \frac{3^{4/3}}{4}$.

Same ratio! Interesting. So in both directions, the ratio is $3^{4/3}/4$.

Let me try a general direction. Let $u = as, v = bs, w = -(a+b)s$.

Actually, let me think more generally. We have $x = e^{as}, y = e^{bs}, z = e^{-(a+b)s}$.

The key quantities:
- $xy = e^{(a+b)s}$, $yz = e^{-as}$, $zx = e^{-bs}$.

$f = \frac{e^{as}}{e^{(a+b)s}+1} + \frac{e^{bs}}{e^{-as}+1} + \frac{e^{-(a+b)s}}{e^{-bs}+1}$

$= \frac{e^{as}}{e^{(a+b)s}+1} + \frac{e^{(a+b)s}}{e^{as}+1} + \frac{e^{-as}}{e^{bs}+1}$

Hmm wait: $\frac{e^{bs}}{e^{-as}+1} = \frac{e^{bs} \cdot e^{as}}{1+e^{as}} = \frac{e^{(a+b)s}}{1+e^{as}}$.

And $\frac{e^{-(a+b)s}}{e^{-bs}+1} = \frac{e^{-(a+b)s} \cdot e^{bs}}{1+e^{bs}} = \frac{e^{-as}}{1+e^{bs}}$.

So $f = \frac{e^{as}}{e^{(a+b)s}+1} + \frac{e^{(a+b)s}}{e^{as}+1} + \frac{e^{-as}}{e^{bs}+1}$.

This is getting complex. Let me just compute the second-order expansion.

For a general function $F(s)$ with $F(0) = F_0$, $F'(0) = 0$, $F''(0) = F_2$, we have $F(s) \approx F_0 + F_2 s^2/2$.

So $f - 3/2 \approx f_2 s^2/2$ and $1/\sqrt[3]{3} - g \approx g_2 s^2/2$ where $f_2 = f''(0)$ and $g_2 = -g''(0)$ (since $g$ has a max at 0, $g''(0) < 0$).

Wait, $g = h^{-1/3}$, $g' = -\frac{1}{3}h^{-4/3}h'$, $g'' = -\frac{1}{3}h^{-4/3}h'' + \frac{4}{9}h^{-7/3}(h')^2$.

At $s=0$: $h = 3, h' = 0, h'' = h_2$. So $g''(0) = -\frac{1}{3} \cdot 3^{-4/3} \cdot h_2 = -\frac{h_2}{3^{7/3}}$.

So $g_2 = -g''(0) = \frac{h_2}{3^{7/3}}$.

And the ratio is $\frac{f_2/2}{g_2/2} = \frac{f_2}{g_2} = \frac{f_2 \cdot 3^{7/3}}{h_2}$.

Now I need to compute $f_2$ and $h_2$ for a general direction $(a, b, -(a+b))$.

Let me compute $h = xy^2 + yz^2 + zx^2$.

$xy^2 = e^{as} \cdot e^{2bs} = e^{(a+2b)s}$
$yz^2 = e^{bs} \cdot e^{-2(a+b)s} = e^{(-a-b)s}$
$zx^2 = e^{-(a+b)s} \cdot e^{2as} = e^{(a-b)s}$

$h = e^{(a+2b)s} + e^{(-a-b)s} + e^{(a-b)s}$

$h(0) = 3$. $h'(0) = (a+2b) + (-a-b) + (a-b) = a + 2b - a - b + a - b = a$. 

Wait, that should be 0 for the constraint. Hmm, but $u + v + w = a + b - (a+b) = 0$, so the constraint is satisfied. But $h'(0) = a$? That can't be right if we want $h$ to have a critical point at $s=0$.

Wait, actually $h$ doesn't need to have a critical point at $s=0$ in every direction. The AM-GM gives $h \ge 3$ with equality at $x=y=z=1$, so $h$ does have a minimum at $s=0$ for all directions. Let me recheck.

$h'(0) = (a+2b) + (-a-b) + (a-b) = a + 2b - a - b + a - b = a$.

Hmm, that gives $a$, not 0. But that contradicts $h$ having a minimum at $s=0$.

Wait, let me recheck. $h = xy^2 + yz^2 + zx^2$. With $x = e^{as}, y = e^{bs}, z = e^{-(a+b)s}$:

$xy^2 = e^{as} \cdot e^{2bs} = e^{(a+2b)s}$ ✓
$yz^2 = e^{bs} \cdot e^{-2(a+b)s} = e^{(b - 2a - 2b)s} = e^{(-2a-b)s}$

Wait, I made an error. $z = e^{-(a+b)s}$, so $z^2 = e^{-2(a+b)s}$.

$yz^2 = e^{bs} \cdot e^{-2(a+b)s} = e^{(b - 2a - 2b)s} = e^{(-2a - b)s}$.

$zx^2 = e^{-(a+b)s} \cdot e^{2as} = e^{(2a - a - b)s} = e^{(a-b)s}$.

So $h = e^{(a+2b)s} + e^{(-2a-b)s} + e^{(a-b)s}$.

$h'(0) = (a+2b) + (-2a-b) + (a-b) = a + 2b - 2a - b + a - b = 0$. ✓

$h''(0) = (a+2b)^2 + (-2a-b)^2 + (a-b)^2$.

$= (a+2b)^2 + (2a+b)^2 + (a-b)^2$

$= a^2 + 4ab + 4b^2 + 4a^2 + 4ab + b^2 + a^2 - 2ab + b^2$

$= 6a^2 + 6ab + 6b^2 = 6(a^2 + ab + b^2)$.

So $h_2 = 6(a^2 + ab + b^2)$.

Now for $f$. Let me compute $f = \frac{x}{xy+1} + \frac{y}{yz+1} + \frac{z}{zx+1}$.

$\frac{x}{xy+1} = \frac{e^{as}}{e^{(a+b)s}+1}$

$\frac{y}{yz+1} = \frac{e^{bs}}{e^{(-2a-b)s} \cdot ... }$

Wait, $yz = e^{bs} \cdot e^{-(a+b)s} = e^{-as}$.

$\frac{y}{yz+1} = \frac{e^{bs}}{e^{-as}+1} = \frac{e^{(a+b)s}}{1+e^{as}}$

$zx = e^{-(a+b)s} \cdot e^{as} = e^{-bs}$.

$\frac{z}{zx+1} = \frac{e^{-(a+b)s}}{e^{-bs}+1} = \frac{e^{-as}}{1+e^{bs}}$

So $f = \frac{e^{as}}{e^{(a+b)s}+1} + \frac{e^{(a+b)s}}{e^{as}+1} + \frac{e^{-as}}{e^{bs}+1}$.

Let me denote $\alpha = a, \beta = a+b$. Then $b = \beta - \alpha$ and $-(a+b) = -\beta$.

$f = \frac{e^{\alpha s}}{e^{\beta s}+1} + \frac{e^{\beta s}}{e^{\alpha s}+1} + \frac{e^{-\alpha s}}{e^{(\beta-\alpha)s}+1}$

Hmm, this is still complex. Let me compute $f''(0)$ using the formula for $\frac{e^{ps}}{e^{qs}+1}$.

Let $\phi(p,q) = \frac{e^{ps}}{e^{qs}+1}$. At $s=0$: $\phi = 1/2$.

$\phi' = \frac{pe^{ps}(e^{qs}+1) - e^{ps} \cdot qe^{qs}}{(e^{qs}+1)^2} = \frac{e^{ps}(p(e^{qs}+1) - qe^{qs})}{(e^{qs}+1)^2}$

At $s=0$: $\frac{p \cdot 2 - q}{4} = \frac{2p-q}{4}$.

$\phi''$: Let me use the quotient rule on $\phi' = \frac{e^{ps}(p + (p-q)e^{qs})}{(e^{qs}+1)^2}$.

Let $N = e^{ps}(p + (p-q)e^{qs})$ and $D = (e^{qs}+1)^2$.

$N' = pe^{ps}(p + (p-q)e^{qs}) + e^{ps}(p-q)qe^{qs} = e^{ps}[p^2 + p(p-q)e^{qs} + q(p-q)e^{qs}]$

$= e^{ps}[p^2 + (p-q)(p+q)e^{qs}] = e^{ps}[p^2 + (p^2-q^2)e^{qs}]$

At $s=0$: $N(0) = p + (p-q) = 2p - q$. $N'(0) = p^2 + p^2 - q^2 = 2p^2 - q^2$.

$D = (e^{qs}+1)^2$. $D' = 2(e^{qs}+1)qe^{qs}$. At $s=0$: $D(0) = 4$, $D'(0) = 4q$.

$D'' = 2q^2 e^{qs}(e^{qs}+1) + 2q \cdot 2qe^{2qs} = 2q^2 e^{qs}(e^{qs}+1+2e^{qs}) = 2q^2 e^{qs}(1+3e^{qs})$. 

Hmm, let me just compute: $D = (e^{qs}+1)^2$, $D' = 2q e^{qs}(e^{qs}+1)$, $D'' = 2q^2 e^{qs}(e^{qs}+1) + 2q \cdot q e^{2qs} \cdot 2 = 2q^2 e^{qs}(e^{qs}+1) + 4q^2 e^{2qs} = 2q^2 e^{qs}(e^{qs}+1+2e^{qs}) = 2q^2 e^{qs}(1+3e^{qs})$.

At $s=0$: $D''(0) = 2q^2 \cdot 4 = 8q^2$.

$\phi''(0) = \frac{N'(0)D(0) - N(0)D'(0)}{D(0)^2} \cdot$ ... no, $\phi'' = \frac{N'D - ND'}{D^2}$, and

$\phi''(0) = \frac{N''(0)D(0) - N(0)D''(0)}{D(0)^2}$... 

Actually, $(N/D)'' = \frac{N''D - ND''}{D^2} - \frac{2(N'D - ND')D'}{D^3}$... this is getting messy. Let me use the formula:

$(N/D)' = (N'D - ND')/D^2$

$(N/D)'' = \frac{(N''D + N'D' - N'D' - ND'')D^2 - (N'D - ND') \cdot 2DD'}{D^4}$

$= \frac{(N''D - ND'')D - 2(N'D - ND')D'}{D^3}$

At $s=0$:

$= \frac{(N''_0 D_0 - N_0 D''_0)D_0 - 2(N'_0 D_0 - N_0 D'_0)D'_0}{D_0^3}$

I need $N''(0)$. $N = e^{ps}[p^2 + (p^2-q^2)e^{qs}]$.

$N' = pe^{ps}[p^2 + (p^2-q^2)e^{qs}] + e^{ps}(p^2-q^2)qe^{qs}$

$= e^{ps}[p^3 + p(p^2-q^2)e^{qs} + q(p^2-q^2)e^{qs}]$

$= e^{ps}[p^3 + (p^2-q^2)(p+q)e^{qs}]$

$= e^{ps}[p^3 + (p-q)(p+q)^2 e^{qs}]$... wait, $(p^2-q^2)(p+q) = (p-q)(p+q)^2$.

$N'' = pe^{ps}[p^3 + (p^2-q^2)(p+q)e^{qs}] + e^{ps}(p^2-q^2)(p+q)qe^{qs}$

$= e^{ps}[p^4 + p(p^2-q^2)(p+q)e^{qs} + q(p^2-q^2)(p+q)e^{qs}]$

$= e^{ps}[p^4 + (p^2-q^2)(p+q)^2 e^{qs}]$

At $s=0$: $N''(0) = p^4 + (p^2-q^2)(p+q)^2 = p^4 + (p-q)(p+q)^3$.

This is getting really messy. Let me try a different approach - just compute $f''(0)$ for the general case numerically or symbolically.

Actually, let me use a cleaner approach. Let me write $f = \sum \frac{x}{xy+1}$ and compute $\frac{d^2 f}{ds^2}\big|_{s=0}$ using the chain rule with $x = e^{as}, y = e^{bs}, z = e^{-(a+b)s}$.

For a term $\frac{x}{xy+1}$, let $u = x = e^{as}$, $v = xy = e^{(a+b)s}$.

$\frac{d}{ds}\frac{u}{v+1} = \frac{u'(v+1) - uv'}{(v+1)^2}$

At $s=0$: $u=1, v=1, u'=a, v'=a+b$. So $\frac{a \cdot 2 - (a+b)}{4} = \frac{a-b}{4}$.

For the second derivative, let me use the expansion approach. Let $u = 1 + as + \frac{a^2 s^2}{2} + ...$, $v = 1 + (a+b)s + \frac{(a+b)^2 s^2}{2} + ...$

$\frac{u}{v+1} = \frac{1 + as + a^2 s^2/2}{2 + (a+b)s + (a+b)^2 s^2/2}$

$= \frac{1}{2} \cdot \frac{1 + as + a^2 s^2/2}{1 + (a+b)s/2 + (a+b)^2 s^2/4}$

$\approx \frac{1}{2}(1 + as + a^2 s^2/2)(1 - (a+b)s/2 - (a+b)^2 s^2/4 + (a+b)^2 s^2/4)$

Wait, $\frac{1}{1+t} \approx 1 - t + t^2$ where $t = (a+b)s/2 + (a+b)^2 s^2/4$.

$1 - t + t^2 \approx 1 - (a+b)s/2 - (a+b)^2 s^2/4 + (a+b)^2 s^2/4 = 1 - (a+b)s/2$.

Hmm, that's only first order. Let me be more careful.

$t = \frac{(a+b)s}{2} + \frac{(a+b)^2 s^2}{4}$

$t^2 = \frac{(a+b)^2 s^2}{4} + ...$

$\frac{1}{1+t} = 1 - t + t^2 - ... \approx 1 - \frac{(a+b)s}{2} - \frac{(a+b)^2 s^2}{4} + \frac{(a+b)^2 s^2}{4} = 1 - \frac{(a+b)s}{2}$

So $\frac{u}{v+1} \approx \frac{1}{2}(1 + as + \frac{a^2 s^2}{2})(1 - \frac{(a+b)s}{2})$

$= \frac{1}{2}(1 + as + \frac{a^2 s^2}{2} - \frac{(a+b)s}{2} - \frac{a(a+b)s^2}{2})$

$= \frac{1}{2}(1 + \frac{a-b}{2}s + \frac{a^2 - a(a+b)}{2}s^2)$

$= \frac{1}{2}(1 + \frac{a-b}{2}s + \frac{-ab}{2}s^2)$

$= \frac{1}{2} + \frac{a-b}{4}s - \frac{ab}{4}s^2$

So the second-order coefficient of $\frac{x}{xy+1}$ is $-\frac{ab}{4}$, meaning $\frac{d^2}{ds^2}\frac{x}{xy+1}\big|_{s=0} = -\frac{ab}{2}$.

Similarly, for $\frac{y}{yz+1}$: $y = e^{bs}$, $yz = e^{-as}$.

By the same formula with $u = y = e^{bs}$, $v = yz = e^{-as}$, so $p = b, q = -a$ in the expansion.

$\frac{y}{yz+1} \approx \frac{1}{2} + \frac{b-(-a)}{4}s - \frac{b \cdot (-a)}{4}s^2 = \frac{1}{2} + \frac{a+b}{4}s + \frac{ab}{4}s^2$

Second derivative: $\frac{ab}{2}$.

For $\frac{z}{zx+1}$: $z = e^{-(a+b)s}$, $zx = e^{-bs}$.

$p = -(a+b), q = -b$.

$\frac{z}{zx+1} \approx \frac{1}{2} + \frac{-(a+b)-(-b)}{4}s - \frac{(-(a+b))(-b)}{4}s^2 = \frac{1}{2} + \frac{-a}{4}s - \frac{b(a+b)}{4}s^2$

Second derivative: $-\frac{b(a+b)}{2}$.

Total $f''(0) = -\frac{ab}{2} + \frac{ab}{2} - \frac{b(a+b)}{2} = -\frac{b(a+b)}{2}$.

Hmm, that doesn't look symmetric. Let me check with the first direction: $a = 1, b = -1$ (so $u = s, v = -s, w = 0$).

$f''(0) = -\frac{(-1)(1+(-1))}{2} = -\frac{(-1)(0)}{2} = 0$.

But earlier I computed $f''(0) = 1/2$ for this direction! So I made an error.

Let me recheck. For $a = 1, b = -1$: $x = e^s, y = e^{-s}, z = 1$.

$\frac{x}{xy+1} = \frac{e^s}{1+1} = \frac{e^s}{2}$. Second derivative: $\frac{1}{2}$.

Using my formula: $-\frac{ab}{2} = -\frac{1 \cdot (-1)}{2} = \frac{1}{2}$. ✓

$\frac{y}{yz+1} = \frac{e^{-s}}{e^{-s}+1} = \frac{1}{1+e^s}$. Second derivative of $\frac{1}{1+e^s}$ at $s=0$: $\frac{e^s}{(1+e^s)^2}$ first derivative, $\frac{e^s(1+e^s)^2 - e^s \cdot 2(1+e^s)e^s}{(1+e^s)^4} = \frac{e^s(1-e^s)}{(1+e^s)^3}$. At $s=0$: $0$.

Using my formula: $\frac{ab}{2} = \frac{1 \cdot (-1)}{2} = -\frac{1}{2}$.

But the actual second derivative is $0$, not $-1/2$! So my formula is wrong.

Let me recheck the expansion for $\frac{y}{yz+1}$ with $p = b = -1, q = -a = -1$.

$\frac{1}{2} + \frac{p-q}{4}s - \frac{pq}{4}s^2 = \frac{1}{2} + \frac{-1-(-1)}{4}s - \frac{(-1)(-1)}{4}s^2 = \frac{1}{2} - \frac{1}{4}s^2$.

So the second derivative is $-\frac{1}{2}$. But the actual function is $\frac{1}{1+e^s}$, whose second derivative at 0 is 0.

Let me compute $\frac{1}{1+e^s}$ more carefully. $\frac{d}{ds} = \frac{-e^s}{(1+e^s)^2}$. At $s=0$: $-1/4$.

$\frac{d^2}{ds^2} = \frac{-e^s(1+e^s)^2 + e^s \cdot 2(1+e^s)e^s}{(1+e^s)^4} = \frac{e^s(-1+e^s)}{(1+e^s)^3}$. At $s=0$: $\frac{1 \cdot 0}{8} = 0$.

So the second derivative is indeed 0. My expansion formula must be wrong.

Let me redo the expansion. $\frac{u}{v+1}$ where $u = e^{ps}, v = e^{qs}$.

$u = 1 + ps + \frac{p^2 s^2}{2} + ...$

$v + 1 = 2 + qs + \frac{q^2 s^2}{2} + ...$

$\frac{u}{v+1} = \frac{1 + ps + p^2 s^2/2}{2 + qs + q^2 s^2/2}$

$= \frac{1}{2} \cdot \frac{1 + ps + p^2 s^2/2}{1 + qs/2 + q^2 s^2/4}$

Let $t = qs/2 + q^2 s^2/4$.

$\frac{1}{1+t} = 1 - t + t^2 - ... = 1 - qs/2 - q^2 s^2/4 + q^2 s^2/4 + ... = 1 - qs/2 + O(s^3)$

Wait, $t^2 = (qs/2)^2 + ... = q^2 s^2/4 + ...$

$1 - t + t^2 = 1 - qs/2 - q^2 s^2/4 + q^2 s^2/4 = 1 - qs/2$.

So $\frac{1}{1+t} \approx 1 - qs/2$ to second order? That can't be right - we're losing the $s^2$ term.

Let me be more careful. $t = \frac{q}{2}s + \frac{q^2}{4}s^2$.

$t^2 = \frac{q^2}{4}s^2 + O(s^3)$.

$\frac{1}{1+t} = 1 - t + t^2 + O(s^3) = 1 - \frac{q}{2}s - \frac{q^2}{4}s^2 + \frac{q^2}{4}s^2 + O(s^3) = 1 - \frac{q}{2}s + O(s^3)$.

Hmm, so to second order, $\frac{1}{1+t} = 1 - \frac{q}{2}s$. The $s^2$ terms cancel!

So $\frac{u}{v+1} = \frac{1}{2}(1 + ps + \frac{p^2}{2}s^2)(1 - \frac{q}{2}s) + O(s^3)$

$= \frac{1}{2}(1 + ps + \frac{p^2}{2}s^2 - \frac{q}{2}s - \frac{pq}{2}s^2) + O(s^3)$

$= \frac{1}{2}(1 + \frac{2p-q}{2}s + \frac{p^2 - pq}{2}s^2) + O(s^3)$

$= \frac{1}{2} + \frac{2p-q}{4}s + \frac{p(p-q)}{4}s^2 + O(s^3)$

So the second derivative is $\frac{p(p-q)}{2}$.

Let me verify: for $\frac{x}{xy+1}$ with $p = a, q = a+b$: second derivative $= \frac{a(a-(a+b))}{2} = \frac{a(-b)}{2} = -\frac{ab}{2}$.

For $\frac{y}{yz+1}$ with $p = b, q = -a$: second derivative $= \frac{b(b-(-a))}{2} = \frac{b(a+b)}{2}$.

For $\frac{z}{zx+1}$ with $p = -(a+b), q = -b$: second derivative $= \frac{(-(a+b))(-(a+b)-(-b))}{2} = \frac{(-(a+b))(-a)}{2} = \frac{a(a+b)}{2}$.

Total: $f''(0) = -\frac{ab}{2} + \frac{b(a+b)}{2} + \frac{a(a+b)}{2} = \frac{-ab + ab + b^2 + a^2 + ab}{2} = \frac{a^2 + ab + b^2}{2}$.

Let me verify with direction 1: $a = 1, b = -1$. $f''(0) = \frac{1 - 1 + 1}{2} = \frac{1}{2}$. ✓ (matches earlier computation)

Direction 2: $a = 1, b = 1$. $f''(0) = \frac{1 + 1 + 1}{2} = \frac{3}{2}$. ✓ (matches earlier computation)

So $f''(0) = \frac{a^2 + ab + b^2}{2}$ and $h''(0) = 6(a^2 + ab + b^2)$.

The ratio is $\frac{f''(0)}{g_2}$ where $g_2 = \frac{h''(0)}{3^{7/3}} = \frac{6(a^2+ab+b^2)}{3^{7/3}}$.

Ratio $= \frac{(a^2+ab+b^2)/2}{6(a^2+ab+b^2)/3^{7/3}} = \frac{1/2}{6/3^{7/3}} = \frac{3^{7/3}}{12} = \frac{3^{7/3}}{12}$.

$3^{7/3} = 3^2 \cdot 3^{1/3} = 9 \cdot 3^{1/3}$.

$\frac{9 \cdot 3^{1/3}}{12} = \frac{3 \cdot 3^{1/3}}{4} = \frac{3^{4/3}}{4}$.

So the ratio is $\frac{3^{4/3}}{4}$ in every direction! This means the second-order expansion gives the same ratio regardless of direction, which is a strong indication that $k_{max} = \frac{3^{4/3}}{4}$.

But I need to verify this is actually the global minimum of the ratio, not just the local behavior near $x = y = z = 1$.

So the claim is $k_{max} = \frac{3^{4/3}}{4}$, and we need to prove:

$$\sum_{cyc} \frac{x}{xy+1} + \frac{3^{4/3}/4}{\sqrt[3]{xy^2 + yz^2 + zx^2}} \ge \frac{3}{2} + \frac{3^{4/3}/4}{\sqrt[3]{3}}$$

for all $x, y, z > 0$ with $xyz = 1$.

And $(2k_{max})^3 = (2 \cdot \frac{3^{4/3}}{4})^3 = (\frac{3^{4/3}}{2})^3 = \frac{3^4}{8} = \frac{81}{8}$.

Wait, let me double-check: $2 \cdot \frac{3^{4/3}}{4} = \frac{3^{4/3}}{2}$. $(\frac{3^{4/3}}{2})^3 = \frac{3^4}{8} = \frac{81}{8}$.

Now I need to actually prove the inequality. Let me think about this more carefully.

We need to show: $f - 3/2 \ge \frac{3^{4/3}}{4}(\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}})$ where $h = xy^2 + yz^2 + zx^2$ and $f = \sum \frac{x}{xy+1}$.

Note $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}} = \frac{h^{1/3} - 3^{1/3}}{3^{1/3} h^{1/3}} \cdot \frac{1}{???}$

Actually, $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}} = \frac{\sqrt[3]{h} - \sqrt[3]{3}}{\sqrt[3]{3}\sqrt[3]{h}}$.

And $\sqrt[3]{h} - \sqrt[3]{3} = \frac{h - 3}{\sqrt[3]{h^2} + \sqrt[3]{3h} + \sqrt[3]{9}}$.

So $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}} = \frac{h - 3}{\sqrt[3]{3h}(\sqrt[3]{h^2} + \sqrt[3]{3h} + \sqrt[3]{9})}$.

At $h = 3$: denominator $= 3(3 + 3 + 3) = 27$. So $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{h}} \approx \frac{h-3}{27}$.

And $\frac{3^{4/3}}{4} \cdot \frac{h-3}{27} = \frac{3^{4/3}(h-3)}{108}$.

Also, $h - 3 \approx 6(a^2+ab+b^2)s^2/2 \cdot 2 = ...$. Well, $h - 3 \approx 3(a^2+ab+b^2)s^2$ (from $h''(0) = 6(a^2+ab+b^2)$, so $h - 3 \approx 3(a^2+ab+b^2)s^2$).

And $f - 3/2 \approx \frac{a^2+ab+b^2}{4}s^2$.

So the ratio $\frac{f-3/2}{(1/\sqrt[3]{3} - 1/\sqrt[3]{h})} \approx \frac{(a^2+ab+b^2)s^2/4}{3(a^2+ab+b^2)s^2/27} = \frac{27}{12} = \frac{9}{4}$.

Hmm, that gives $9/4$, not $3^{4/3}/4$. Let me recheck.

Oh wait, I think I need to be more careful. Let me recompute $g_2$.

$g = h^{-1/3}$. $g' = -\frac{1}{3}h^{-4/3}h'$. At $s=0$: $g'(0) = 0$.

$g'' = -\frac{1}{3}(-\frac{4}{3})h^{-7/3}(h')^2 - \frac{1}{3}h^{-4/3}h'' = \frac{4}{9}h^{-7/3}(h')^2 - \frac{1}{3}h^{-4/3}h''$.

At $s=0$: $g''(0) = 0 - \frac{1}{3} \cdot 3^{-4/3} \cdot h''(0) = -\frac{h''(0)}{3^{7/3}}$.

So $g(s) \approx 3^{-1/3} - \frac{h''(0)}{2 \cdot 3^{7/3}} s^2$.

$1/\sqrt[3]{3} - g(s) \approx \frac{h''(0)}{2 \cdot 3^{7/3}} s^2 = \frac{6(a^2+ab+b^2)}{2 \cdot 3^{7/3}} s^2 = \frac{3(a^2+ab+b^2)}{3^{7/3}} s^2$.

And $f - 3/2 \approx \frac{a^2+ab+b^2}{4} s^2$.

Ratio $= \frac{(a^2+ab+b^2)/4}{3(a^2+ab+b^2)/3^{7/3}} = \frac{3^{7/3}}{12} = \frac{3^{7/3}}{12}$.

$3^{7/3} = 3^{2+1/3} = 9 \cdot 3^{1/3}$. $\frac{9 \cdot 3^{1/3}}{12} = \frac{3 \cdot 3^{1/3}}{4} = \frac{3^{4/3}}{4}$.

OK so the ratio is indeed $\frac{3^{4/3}}{4}$, confirming $k_{max} \le \frac{3^{4/3}}{4}$.

Now I need to prove the inequality holds for $k = \frac{3^{4/3}}{4}$.

Let me try to use the substitution $x = a/b, y = b/c, z = c/a$ to simplify.

With $xyz = 1$, let $x = a/b, y = b/c, z = c/a$.

$xy = a/c, yz = b/a, zx = c/b$.

$\frac{x}{xy+1} = \frac{a/b}{a/c+1} = \frac{ac}{b(a+c)}$.

$\frac{y}{yz+1} = \frac{b/c}{b/a+1} = \frac{ab}{c(a+b)}$.

$\frac{z}{zx+1} = \frac{c/a}{c/b+1} = \frac{bc}{a(b+c)}$.

$f = \frac{ac}{b(a+c)} + \frac{ab}{c(a+b)} + \frac{bc}{a(b+c)}$.

$xy^2 = \frac{a}{b} \cdot \frac{b^2}{c^2} = \frac{ab}{c^2}$.

$yz^2 = \frac{b}{c} \cdot \frac{c^2}{a^2} = \frac{bc}{a^2}$.

$zx^2 = \frac{c}{a} \cdot \frac{a^2}{b^2} = \frac{ac}{b^2}$.

$h = \frac{ab}{c^2} + \frac{bc}{a^2} + \frac{ca}{b^2}$.

Hmm, this is the Nesbitt-like form. Let me try $a = b = c = 1$: $f = 1/2 + 1/2 + 1/2 = 3/2$, $h = 1 + 1 + 1 = 3$. ✓

This substitution doesn't seem to simplify things much. Let me try another approach.

Let me try the substitution $p = xy, q = yz, r = zx$. Then $pqr = (xyz)^2 = 1$, and $x = \sqrt{pr/q}, y = \sqrt{pq/r}, z = \sqrt{qr/p}$.

$\frac{x}{xy+1} = \frac{x}{p+1} = \frac{\sqrt{pr/q}}{p+1}$.

This doesn't simplify nicely either.

Let me try yet another approach. Let me use $a = xy, b = yz, c = zx$ with $abc = 1$.

Then $x = \sqrt{ac/b}, y = \sqrt{ab/c}, z = \sqrt{bc/a}$.

$\frac{x}{xy+1} = \frac{\sqrt{ac/b}}{a+1}$, $\frac{y}{yz+1} = \frac{\sqrt{ab/c}}{b+1}$, $\frac{z}{zx+1} = \frac{\sqrt{bc/a}}{c+1}$.

$xy^2 = a \cdot ab/c = a^2b/c$. $yz^2 = b \cdot bc/a = b^2c/a$. $zx^2 = c \cdot ac/b = c^2a/b$.

$h = \frac{a^2b}{c} + \frac{b^2c}{a} + \frac{c^2a}{b}$.

With $abc = 1$, $c = 1/(ab)$, so $\frac{a^2b}{c} = a^3b^2$, $\frac{b^2c}{a} = b^3/a^2 \cdot 1/(ab) = ...$. This is getting messy.

Let me try a completely different approach. Maybe I should try to prove the inequality directly using known inequalities.

The inequality is:
$$\sum_{cyc} \frac{x}{xy+1} - \frac{3}{2} \ge \frac{3^{4/3}}{4}\left(\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{xy^2+yz^2+zx^2}}\right)$$

Let me denote $S = xy^2 + yz^2 + zx^2$ and $T = \sum \frac{x}{xy+1}$.

We know $S \ge 3$ (by AM-GM). We need $T \ge 3/2$ (which we should verify) and the refined inequality.

Actually, let me first check: is $T \ge 3/2$ always true?

With $x = e^{as}, y = e^{bs}, z = e^{-(a+b)s}$, we showed $T''(0) = \frac{a^2+ab+b^2}{2} \ge 0$, so $T$ has a local min at $s=0$. But is it a global min?

Let me check a boundary case. $x \to \infty, y = 1, z = 1/x$. Then $xy = x, yz = 1/x, zx = 1$.

$T = \frac{x}{x+1} + \frac{1}{1/x+1} + \frac{1/x}{1+1} = \frac{x}{x+1} + \frac{x}{x+1} + \frac{1}{2x} = \frac{2x}{x+1} + \frac{1}{2x}$.

As $x \to \infty$: $T \to 2$. As $x \to 0$: $T \to 0 + 0 + \infty = \infty$.

At $x = 1$: $T = 1 + 1/2 + 1/2 = 2$. Wait, that's not $3/2$.

Hmm wait, $x = 1, y = 1, z = 1$: $T = \frac{1}{2} + \frac{1}{2} + \frac{1}{2} = 3/2$. Let me recheck.

$x = 1, y = 1, z = 1$: $xy = 1, yz = 1, zx = 1$. $T = \frac{1}{1+1} + \frac{1}{1+1} + \frac{1}{1+1} = 3/2$. ✓

For $x \to \infty, y = 1, z = 1/x$: $T = \frac{x}{x+1} + \frac{1}{1/x+1} + \frac{1/x}{2}$. 

$\frac{1}{1/x+1} = \frac{x}{1+x}$. So $T = \frac{2x}{x+1} + \frac{1}{2x} \to 2$ as $x \to \infty$.

So $T$ can be larger than $3/2$. The minimum is at $x = y = z = 1$.

OK so the problem reduces to proving the refined inequality. Let me think about whether there's a clean proof.

Let me try to use the tangent line trick or SOS methods.

Actually, let me think about this differently. We want to show:

$$T - \frac{3}{2} \ge \frac{3^{4/3}}{4}\left(\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{S}}\right)$$

where $S = xy^2 + yz^2 + zx^2 \ge 3$.

Let $u = S/3 \ge 1$. Then $\frac{1}{\sqrt[3]{3}} - \frac{1}{\sqrt[3]{S}} = \frac{1}{\sqrt[3]{3}}(1 - u^{-1/3})$.

So the RHS is $\frac{3^{4/3}}{4} \cdot \frac{1}{3^{1/3}}(1 - u^{-1/3}) = \frac{3}{4}(1 - u^{-1/3})$.

So we need: $T - 3/2 \ge \frac{3}{4}(1 - (S/3)^{-1/3})$.

Or equivalently: $T \ge \frac{3}{2} + \frac{3}{4}(1 - (S/3)^{-1/3}) = \frac{3}{4}(3 - (S/3)^{-1/3})$... 

Hmm, let me think about this differently. Let me try to find a relationship between $T$ and $S$.

Actually, let me try specific parametric families to check if the ratio is always $\ge 3^{4/3}/4$.

Family 1: $x = t, y = t, z = 1/t^2$.

$xy = t^2, yz = 1/t, zx = 1/t$.

$T = \frac{t}{t^2+1} + \frac{t}{1/t+1} + \frac{1/t^2}{1/t+1} = \frac{t}{t^2+1} + \frac{t^2}{t+1} + \frac{1}{t(t+1)}$

$= \frac{t}{t^2+1} + \frac{t^3+1}{t(t+1)} = \frac{t}{t^2+1} + \frac{t^2-t+1}{t}$

$S = t \cdot t^2 + t \cdot 1/t^4 + 1/t^2 \cdot t^2 = t^3 + 1/t^3 + 1$.

Let me compute the ratio $R = \frac{T - 3/2}{1/3^{1/3} - 1/S^{1/3}}$ for various $t$.

At $t = 1$: $T = 1/2 + 1 = 3/2$, $S = 3$. Ratio is $0/0$, limit is $3^{4/3}/4 \approx 1.0817$... 

$3^{4/3} = 3 \cdot 3^{1/3} \approx 3 \cdot 1.4422 = 4.3267$. $3^{4/3}/4 \approx 1.0817$.

Let me try $t = 2$: 

$T = \frac{2}{5} + \frac{4-2+1}{2} = 0.4 + 1.5 = 1.9$.

$S = 8 + 1/8 + 1 = 9.125$.

$1/3^{1/3} \approx 0.6934$. $1/S^{1/3} = 1/9.125^{1/3}$. $9.125^{1/3} \approx 2.087$. So $1/S^{1/3} \approx 0.479$.

$T - 3/2 = 0.4$. $1/3^{1/3} - 1/S^{1/3} \approx 0.6934 - 0.479 = 0.2144$.

$R \approx 0.4/0.2144 \approx 1.866$.

This is larger than $1.0817$, so the inequality holds here.

Let me try $t$ close to 1, say $t = 1.1$:

$T = \frac{1.1}{1.21+1} + \frac{1.21-1.1+1}{1.1} = \frac{1.1}{2.21} + \frac{1.11}{1.1} = 0.4977 + 1.0091 = 1.5068$.

$S = 1.331 + 1/1.331 + 1 = 1.331 + 0.7513 + 1 = 3.0823$.

$S^{1/3} \approx 1.4553$ (since $1.455^3 \approx 3.081$). $1/S^{1/3} \approx 0.6872$.

$T - 3/2 = 0.0068$. $1/3^{1/3} - 1/S^{1/3} \approx 0.6934 - 0.6872 = 0.0062$.

$R \approx 0.0068/0.0062 \approx 1.097$.

Close to $1.0817$, slightly above. Good.

Let me try another family. $x = t, y = 1, z = 1/t$.

$xy = t, yz = 1/t, zx = 1$.

$T = \frac{t}{t+1} + \frac{1}{1/t+1} + \frac{1/t}{2} = \frac{t}{t+1} + \frac{t}{t+1} + \frac{1}{2t} = \frac{2t}{t+1} + \frac{1}{2t}$.

$S = t \cdot 1 + 1 \cdot 1/t^2 + 1/t \cdot t^2 = t + 1/t^2 + t = 2t + 1/t^2$.

At $t = 1$: $T = 1 + 1/2 = 3/2$, $S = 3$. ✓

$T' = \frac{2}{(t+1)^2} - \frac{1}{2t^2}$. At $t=1$: $2/4 - 1/2 = 0$. ✓

$T'' = -\frac{4}{(t+1)^3} + \frac{1}{t^3}$. At $t=1$: $-4/8 + 1 = 1/2$.

$S' = 2 - 2/t^3$. At $t=1$: $0$. $S'' = 6/t^4$. At $t=1$: $6$.

Ratio: $\frac{T''/2}{S''/(2 \cdot 3^{7/3})} = \frac{1/4}{6/(2 \cdot 3^{7/3})} = \frac{1/4}{3/3^{7/3}} = \frac{3^{7/3}}{12} = \frac{3^{4/3}}{4}$. ✓

Let me try $t = 2$ in this family:

$T = \frac{4}{3} + \frac{1}{4} = 1.5833$.

$S = 4 + 1/4 = 4.25$.

$S^{1/3} \approx 1.6199$. $1/S^{1/3} \approx 0.6173$.

$T - 3/2 = 0.0833$. $1/3^{1/3} - 1/S^{1/3} \approx 0.6934 - 0.6173 = 0.0761$.

$R \approx 0.0833/0.0761 \approx 1.095$.

Close to $1.0817$ but above. Good.

Let me try $t = 0.5$:

$T = \frac{1}{1.5} + 1 = 0.6667 + 1 = 1.6667$.

$S = 1 + 4 = 5$.

$S^{1/3} \approx 1.71$. $1/S^{1/3} \approx 0.5848$.

$T - 3/2 = 0.1667$. $1/3^{1/3} - 1/S^{1/3} \approx 0.6934 - 0.5848 = 0.1086$.

$R \approx 0.1667/0.1086 \approx 1.535$.

Above. Good.

So it seems like the minimum ratio is indeed $3^{4/3}/4$, achieved in the limit as we approach $x = y = z = 1$.

Now I need to prove this rigorously. Let me think about what approach might work.

One approach: Show that $T - 3/2 \ge \frac{3}{4}(1 - (3/S)^{1/3})$ (which is equivalent to our inequality with $k = 3^{4/3}/4$).

Actually, let me rewrite. We need:
$$T - \frac{3}{2} \ge \frac{3}{4}\left(1 - \left(\frac{3}{S}\right)^{1/3}\right)$$

where $S = xy^2 + yz^2 + zx^2 \ge 3$ and $T = \sum \frac{x}{xy+1}$.

Hmm, let me think about whether there's a way to relate $T$ and $S$ more directly.

Actually, let me try a different approach. Let me use the substitution $a = xy, b = yz, c = zx$ with $abc = 1$.

Then $x = \sqrt{ac/b}, y = \sqrt{ab/c}, z = \sqrt{bc/a}$.

$T = \frac{\sqrt{ac/b}}{a+1} + \frac{\sqrt{ab/c}}{b+1} + \frac{\sqrt{bc/a}}{c+1}$.

$S = xy^2 + yz^2 + zx^2$.

$xy^2 = a \cdot y = a\sqrt{ab/c} = a\sqrt{ab/c}$.

Hmm, $y = \sqrt{ab/c}$, so $xy^2 = x \cdot y^2 = \sqrt{ac/b} \cdot ab/c = a\sqrt{ab/c} \cdot \sqrt{ac/b} \cdot ... $

Actually, $xy^2 = (xy) \cdot y = a \cdot \sqrt{ab/c}$.

$yz^2 = (yz) \cdot z = b \cdot \sqrt{bc/a}$.

$zx^2 = (zx) \cdot x = c \cdot \sqrt{ac/b}$.

$S = a\sqrt{ab/c} + b\sqrt{bc/a} + c\sqrt{ac/b}$.

With $abc = 1$: $\sqrt{ab/c} = \sqrt{ab \cdot ab} = ab$ (since $c = 1/(ab)$). Wait, $abc = 1$ so $c = 1/(ab)$, and $ab/c = ab \cdot ab = (ab)^2$, so $\sqrt{ab/c} = ab$.

Similarly, $\sqrt{bc/a} = bc$ and $\sqrt{ac/b} = ac$.

So $S = a \cdot ab + b \cdot bc + c \cdot ac = a^2b + b^2c + c^2a$.

And $T = \frac{ac}{a+1} + \frac{ab}{b+1} + \frac{bc}{c+1}$... 

Wait: $\frac{\sqrt{ac/b}}{a+1} = \frac{ac}{a+1}$ (since $\sqrt{ac/b} = ac$ when $abc = 1$).

Let me verify: $\sqrt{ac/b}$. With $abc = 1$, $b = 1/(ac)$, so $ac/b = ac \cdot ac = (ac)^2$, $\sqrt{ac/b} = ac$. ✓

So $T = \frac{ac}{a+1} + \frac{ab}{b+1} + \frac{bc}{c+1}$ and $S = a^2b + b^2c + c^2a$ with $abc = 1$.

With $abc = 1$, we can write $a = p/q, b = q/r, c = r/p$ for some $p, q, r > 0$. Then:

$ac = r/q \cdot ... $ hmm, $a = p/q, c = r/p$, so $ac = r/q$.

$ab = p/r$, $bc = q/p$.

$T = \frac{r/q}{p/q+1} + \frac{p/r}{q/r+1} + \frac{q/p}{r/p+1} = \frac{r}{p+q} + \frac{p}{q+r} + \frac{q}{r+p}$.

Oh nice! $T = \frac{p}{q+r} + \frac{q}{r+p} + \frac{r}{p+q}$, which is exactly Nesbitt's expression!

And $S = a^2b + b^2c + c^2a = (p/q)^2 (q/r) + (q/r)^2 (r/p) + (r/p)^2 (p/q) = \frac{p^2}{qr} + \frac{q^2}{rp} + \frac{r^2}{pq} = \frac{p^3 + q^3 + r^3}{pqr}$.

So with the substitution $a = xy = p/q, b = yz = q/r, c = zx = r/p$ (and $abc = 1$), we get:

$$T = \sum_{cyc} \frac{p}{q+r}, \quad S = \frac{p^3 + q^3 + r^3}{pqr}$$

And we need to prove:
$$\sum_{cyc} \frac{p}{q+r} - \frac{3}{2} \ge \frac{3}{4}\left(1 - \left(\frac{3pqr}{p^3+q^3+r^3}\right)^{1/3}\right)$$

By Nesbitt's inequality, $\sum \frac{p}{q+r} \ge \frac{3}{2}$, so the LHS is non-negative. ✓

Now, $S = \frac{p^3+q^3+r^3}{pqr}$. By AM-GM, $p^3 + q^3 + r^3 \ge 3pqr$, so $S \ge 3$. ✓

Let me normalize. WLOG $p + q + r = 3$ (homogeneous). Actually, $T$ is homogeneous of degree 0, and $S$ is also homogeneous of degree 0. So we can normalize.

Let $p + q + r = 3$. Then $T = \sum \frac{p}{3-p}$ and $S = \frac{p^3+q^3+r^3}{pqr}$.

We need: $\sum \frac{p}{3-p} - \frac{3}{2} \ge \frac{3}{4}(1 - (3/S)^{1/3})$.

Note $p^3 + q^3 + r^3 = (p+q+r)^3 - 3(p+q+r)(pq+qr+rp) + 3pqr = 27 - 9(pq+qr+rp) + 3pqr$.

Let $\sigma = pq + qr + rp$ and $\pi = pqr$. Then $p^3+q^3+r^3 = 27 - 9\sigma + 3\pi$ and $S = \frac{27-9\sigma+3\pi}{\pi}$.

Also, $\sum \frac{p}{3-p} = \sum \frac{p}{q+r}$. With $p+q+r = 3$:

$\sum \frac{p}{3-p} = \sum \frac{p}{3-p}$.

$\frac{p}{3-p} = \frac{p}{q+r}$. $\sum \frac{p}{q+r} = \frac{p(q+r)(r+p) + q(r+p)(p+q) + r(p+q)(q+r)}{(p+q)(q+r)(r+p)}$... 

Actually, $\sum \frac{p}{q+r} = \frac{p^2+pq+pr + q^2+qr+qp + r^2+rq+rp}{(p+q)(q+r)(r+p)} \cdot ...$

Hmm, let me just use the known formula. $\sum \frac{p}{q+r} = \frac{p(q+r)(p+q) + ... }{...}$... this is getting complicated.

Let me try a different approach. Since both sides are symmetric in $p, q, r$ (wait, is $S$ symmetric? $S = \frac{p^3+q^3+r^3}{pqr}$ is symmetric, and $T = \sum \frac{p}{q+r}$ is symmetric), the problem is symmetric.

By the method of Lagrange multipliers or by the theory of symmetric inequalities, the extremum might occur when two variables are equal. Let me check: set $q = r$, $p + 2q = 3$.

$T = \frac{p}{2q} + \frac{2q}{p+q} = \frac{p}{2q} + \frac{2q}{p+q}$.

With $p = 3 - 2q$: $T = \frac{3-2q}{2q} + \frac{2q}{3-q}$.

$S = \frac{(3-2q)^3 + 2q^3}{(3-2q)q^2}$.

At $q = 1$ (so $p = 1$): $T = 1/2 + 2/2 = 3/2$, $S = 3/1 = 3$. ✓

Let me compute the ratio for $q$ near 1. Let $q = 1 + \epsilon$, $p = 1 - 2\epsilon$.

$T = \frac{1-2\epsilon}{2(1+\epsilon)} + \frac{2(1+\epsilon)}{2-\epsilon}$.

$\frac{1-2\epsilon}{2+2\epsilon} = \frac{1}{2} \cdot \frac{1-2\epsilon}{1+\epsilon} \approx \frac{1}{2}(1-2\epsilon)(1-\epsilon) \approx \frac{1}{2}(1-3\epsilon) = \frac{1}{2} - \frac{3\epsilon}{2}$.

$\frac{2+2\epsilon}{2-\epsilon} = \frac{2(1+\epsilon)}{2-\epsilon} \approx (1+\epsilon)(1+\epsilon/2) \approx 1 + \frac{3\epsilon}{2}$.

$T \approx \frac{1}{2} - \frac{3\epsilon}{2} + 1 + \frac{3\epsilon}{2} = \frac{3}{2}$. 

Hmm, first order cancels. Let me go to second order.

$\frac{1-2\epsilon}{2(1+\epsilon)} = \frac{1}{2}(1-2\epsilon)(1-\epsilon+\epsilon^2) \approx \frac{1}{2}(1 - 3\epsilon + 3\epsilon^2)$.

$\frac{2(1+\epsilon)}{2-\epsilon} = (1+\epsilon)(1+\epsilon/2+\epsilon^2/4) \approx 1 + \frac{3\epsilon}{2} + \frac{3\epsilon^2}{4}$.

$T \approx \frac{1}{2} - \frac{3\epsilon}{2} + \frac{3\epsilon^2}{2} + 1 + \frac{3\epsilon}{2} + \frac{3\epsilon^2}{4} = \frac{3}{2} + \frac{9\epsilon^2}{4}$.

$S = \frac{(1-2\epsilon)^3 + 2(1+\epsilon)^3}{(1-2\epsilon)(1+\epsilon)^2}$.

Numerator: $(1-6\epsilon+12\epsilon^2) + 2(1+3\epsilon+3\epsilon^2) = 1-6\epsilon+12\epsilon^2+2+6\epsilon+6\epsilon^2 = 3+18\epsilon^2$.

Denominator: $(1-2\epsilon)(1+2\epsilon+\epsilon^2) = 1+2\epsilon+\epsilon^2-2\epsilon-4\epsilon^2 = 1-3\epsilon^2$.

$S \approx \frac{3+18\epsilon^2}{1-3\epsilon^2} \approx (3+18\epsilon^2)(1+3\epsilon^2) \approx 3 + 27\epsilon^2$.

$S - 3 \approx 27\epsilon^2$.

$1 - (3/S)^{1/3} = 1 - (3/(3+27\epsilon^2))^{1/3} = 1 - (1/(1+9\epsilon^2))^{1/3} \approx 1 - (1-3\epsilon^2) = 3\epsilon^2$.

RHS: $\frac{3}{4} \cdot 3\epsilon^2 = \frac{9\epsilon^2}{4}$.

LHS: $T - 3/2 = \frac{9\epsilon^2}{4}$.

So LHS = RHS to second order! This confirms the tightness.

Now, the fact that equality holds to second order in all directions strongly suggests that $k = 3^{4/3}/4$ is the answer, and the inequality is tight (equality only at $p = q = r$, but the ratio approaches $3^{4/3}/4$ from above in all directions).

Now I need to prove the inequality. Let me think about this.

We need to prove: $\sum \frac{p}{q+r} - \frac{3}{2} \ge \frac{3}{4}(1 - (3/S)^{1/3})$ where $S = \frac{p^3+q^3+r^3}{pqr}$.

Equivalently: $\sum \frac{p}{q+r} \ge \frac{3}{2} + \frac{3}{4}(1 - (3/S)^{1/3}) = \frac{3}{4}(3 - (3/S)^{1/3})$.

Hmm, let me think about using the power mean inequality or Schur's inequality.

Actually, let me try a tangent line approach. We want to show $f(p,q,r) \ge 0$ where 

$f = \sum \frac{p}{q+r} - \frac{3}{2} - \frac{3}{4}(1 - (3/S)^{1/3})$.

Since this is symmetric and homogeneous of degree 0, we can set $p + q + r = 3$ and $p, q, r > 0$.

With this normalization, $S = \frac{p^3+q^3+r^3}{pqr}$ and $T = \sum \frac{p}{3-p}$.

Note $p^3 + q^3 + r^3 = 27 - 9\sigma + 3\pi$ where $\sigma = pq+qr+rp, \pi = pqr$.

$T = \sum \frac{p}{3-p}$. Let me compute this in terms of $\sigma$ and $\pi$.

$\sum \frac{p}{3-p} = \sum \frac{p}{q+r} = \frac{\sum p(p+q)(p+r)}{(p+q)(q+r)(r+p)}$.

Numerator: $\sum p(p+q)(p+r) = \sum p(p^2 + p(q+r) + qr) = \sum p^3 + \sum p^2(q+r) + \sum pqr$.

$= (p^3+q^3+r^3) + (p^2 q + p^2 r + q^2 p + q^2 r + r^2 p + r^2 q) + 3pqr$.

$= (p^3+q^3+r^3) + (p+q+r)(pq+qr+rp) - 3pqr + 3pqr$... 

Wait, $p^2q + p^2r + q^2p + q^2r + r^2p + r^2q = (p+q+r)(pq+qr+rp) - 3pqr$.

So numerator $= (p^3+q^3+r^3) + (p+q+r)(pq+qr+rp) - 3pqr + 3pqr = (p^3+q^3+r^3) + (p+q+r)\sigma$.

With $p+q+r = 3$: numerator $= (27 - 9\sigma + 3\pi) + 3\sigma = 27 - 6\sigma + 3\pi$.

Denominator: $(p+q)(q+r)(r+p) = (p+q+r)(pq+qr+rp) - pqr = 3\sigma - \pi$.

So $T = \frac{27 - 6\sigma + 3\pi}{3\sigma - \pi}$.

And $S = \frac{27 - 9\sigma + 3\pi}{\pi}$.

We need: $\frac{27 - 6\sigma + 3\pi}{3\sigma - \pi} - \frac{3}{2} \ge \frac{3}{4}(1 - (\frac{3\pi}{27-9\sigma+3\pi})^{1/3})$.

LHS: $\frac{2(27-6\sigma+3\pi) - 3(3\sigma-\pi)}{2(3\sigma-\pi)} = \frac{54-12\sigma+6\pi-9\sigma+3\pi}{2(3\sigma-\pi)} = \frac{54-21\sigma+9\pi}{2(3\sigma-\pi)} = \frac{3(18-7\sigma+3\pi)}{2(3\sigma-\pi)}$.

At $p=q=r=1$: $\sigma = 3, \pi = 1$. LHS $= \frac{3(18-21+3)}{2(9-1)} = \frac{3 \cdot 0}{16} = 0$. ✓

Let me denote $u = \sigma, v = \pi$ for convenience. With $p+q+r = 3$, we have $0 < u \le 3$ and $0 < v \le 1$ (by AM-GM), with the constraint that $u^2 \ge 3v$ (Schur-like) and $u \le 3$.

Actually, the constraints on $(u, v)$ for $p, q, r > 0$ with $p+q+r = 3$ are: $0 < u \le 3$, $0 < v \le 1$, and the discriminant condition. But let me not worry about exact constraints for now.

We need: $\frac{3(18-7u+3v)}{2(3u-v)} \ge \frac{3}{4}(1 - (\frac{3v}{27-9u+3v})^{1/3})$.

Simplify: $\frac{2(18-7u+3v)}{3u-v} \ge 1 - (\frac{v}{9-3u+v})^{1/3}$.

Let me denote $w = 9 - 3u + v = \frac{p^3+q^3+r^3}{3}$. Note $w \ge v$ (since $p^3+q^3+r^3 \ge 3pqr$), so $\frac{v}{w} \le 1$.

Also, $18 - 7u + 3v = 18 - 7u + 3v$. And $3u - v = 3u - v$.

At $u = 3, v = 1$: $18 - 21 + 3 = 0$, $9 - 1 = 8$. LHS = 0. And $w = 9 - 9 + 1 = 1$, $v/w = 1$, RHS = 0. ✓

Let me try to express things in terms of $w$ and $v$. We have $w = 9 - 3u + v$, so $u = \frac{9 + v - w}{3}$.

$3u - v = 9 + v - w - v = 9 - w$.

$18 - 7u + 3v = 18 - \frac{7(9+v-w)}{3} + 3v = 18 - \frac{63+7v-7w}{3} + 3v = \frac{54 - 63 - 7v + 7w + 9v}{3} = \frac{-9 + 2v + 7w}{3}$.

So LHS $= \frac{2(-9+2v+7w)/3}{9-w} = \frac{2(-9+2v+7w)}{3(9-w)}$.

RHS $= 1 - (v/w)^{1/3}$.

So we need: $\frac{2(7w + 2v - 9)}{3(9-w)} \ge 1 - (v/w)^{1/3}$.

Note $w \ge v > 0$ and $w \le 9$ (since $u \ge 0$... actually $u > 0$ so $w < 9 + v$, but $w = 9 - 3u + v < 9 + v$). Also $w \ge 1$ (since $w = (p^3+q^3+r^3)/3 \ge (p+q+r)^3/27 \cdot 3 = 1$ by power mean... actually $p^3+q^3+r^3 \ge (p+q+r)^3/9 = 3$ by power mean, so $w \ge 1$).

At $w = 1, v = 1$: LHS $= \frac{2(7+2-9)}{3 \cdot 8} = 0$, RHS $= 1 - 1 = 0$. ✓

Let me set $t = v/w \in (0, 1]$. Then $v = tw$.

LHS $= \frac{2(7w + 2tw - 9)}{3(9-w)} = \frac{2w(7+2t) - 18}{3(9-w)}$.

RHS $= 1 - t^{1/3}$.

We need: $\frac{2w(7+2t) - 18}{3(9-w)} \ge 1 - t^{1/3}$.

$2w(7+2t) - 18 \ge 3(9-w)(1-t^{1/3})$

$2w(7+2t) - 18 \ge 27 - 27t^{1/3} - 3w + 3wt^{1/3}$

$2w(7+2t) + 3w - 3wt^{1/3} \ge 45 - 27t^{1/3}$

$w(14 + 4t + 3 - 3t^{1/3}) \ge 45 - 27t^{1/3}$

$w(17 + 4t - 3t^{1/3}) \ge 45 - 27t^{1/3}$

$w \ge \frac{45 - 27t^{1/3}}{17 + 4t - 3t^{1/3}}$

Now, we need to find the minimum value of $w$ given $t = v/w$. 

Recall $w = (p^3+q^3+r^3)/3$ and $v = pqr$ with $p+q+r = 3$. And $t = v/w = 3pqr/(p^3+q^3+r^3)$.

By AM-GM, $p^3+q^3+r^3 \ge 3pqr$, so $t \le 1$.

We need to find the minimum of $w$ for a given $t$. This is an optimization problem.

Actually, let me think about this differently. We have the constraint that $p, q, r > 0$ with $p + q + r = 3$, and we've expressed everything in terms of $w$ and $t$. The question is: for a given $t \in (0, 1]$, what is the minimum possible $w$?

By the method of Lagrange multipliers (or by the theory of symmetric functions), the extremum of $w = (p^3+q^3+r^3)/3$ subject to $p+q+r = 3$ and $pqr/(p^3+q^3+r^3) = t/3$ (i.e., $v/w = t$) occurs when two of $p, q, r$ are equal.

So let $q = r$, $p + 2q = 3$, $p = 3 - 2q$ with $0 < q < 3/2$.

$w = \frac{(3-2q)^3 + 2q^3}{3}$, $v = (3-2q)q^2$, $t = \frac{3(3-2q)q^2}{(3-2q)^3 + 2q^3}$.

At $q = 1$: $w = 1, v = 1, t = 1$. ✓

As $q \to 0$: $w \to 9, v \to 0, t \to 0$.

As $q \to 3/2$: $p \to 0$, $w \to 2(3/2)^3/3 = 2 \cdot 27/8 / 3 = 9/4$, $v \to 0$, $t \to 0$.

So for a given $t$, the minimum $w$ is achieved at the boundary of the two-equal curve. But actually, for a given $t$, there might be two values of $q$ giving the same $t$, and we want the one with smaller $w$.

This is getting complicated. Let me try a different approach.

Let me go back to the inequality: $w(17 + 4t - 3t^{1/3}) \ge 45 - 27t^{1/3}$ where $t = v/w$.

We need to show this holds for all valid $(w, t)$ coming from $p, q, r > 0$ with $p+q+r=3$.

Since $w \ge 1$ (by power mean) and $t \le 1$, and $17 + 4t - 3t^{1/3} > 0$ for $t \in (0, 1]$ (at $t=1$: $17+4-3 = 18 > 0$), we need:

$w \ge \frac{45 - 27t^{1/3}}{17 + 4t - 3t^{1/3}} := \phi(t)$.

So we need to show $w \ge \phi(t)$ for all valid $(w, t)$.

At $t = 1$: $\phi(1) = \frac{45-27}{17+4-3} = \frac{18}{18} = 1 = w$. ✓ (equality)

So we need $w \ge \phi(t)$, and at $t = 1$ we have equality. 

Now, the question is: is $\phi(t) \le w_{min}(t)$ where $w_{min}(t)$ is the minimum $w$ for a given $t$?

Actually, let me think about this more carefully. The relationship between $w$ and $t$ is constrained by the fact that they come from $p, q, r > 0$ with $p + q + r = 3$. 

Let me parametrize by $q = r$ (two equal). Then $p = 3 - 2q$, and:

$w = \frac{(3-2q)^3 + 2q^3}{3} = \frac{27 - 54q + 36q^2 - 8q^3 + 2q^3}{3} = \frac{27 - 54q + 36q^2 - 6q^3}{3} = 9 - 18q + 12q^2 - 2q^3$.

$v = (3-2q)q^2 = 3q^2 - 2q^3$.

$t = v/w = \frac{3q^2 - 2q^3}{9 - 18q + 12q^2 - 2q^3} = \frac{q^2(3-2q)}{9 - 18q + 12q^2 - 2q^3}$.

At $q = 1$: $t = 1/1 = 1$, $w = 9 - 18 + 12 - 2 = 1$. ✓

Let me compute $dw/dt$ along this curve at $q = 1$.

$dw/dq = -18 + 24q - 6q^2$. At $q=1$: $-18+24-6 = 0$.

$dv/dq = 6q - 6q^2$. At $q=1$: $0$.

$t = v/w$, $dt/dq = (v'w - vw')/w^2$. At $q=1$: $(0 \cdot 1 - 1 \cdot 0)/1 = 0$.

So both $dw/dq$ and $dt/dq$ are 0 at $q=1$. Need second order.

$w'' = 24 - 12q$. At $q=1$: $12$. So $w \approx 1 + 6(q-1)^2$.

$v'' = 6 - 12q$. At $q=1$: $-6$. So $v \approx 1 - 3(q-1)^2$.

$t = v/w \approx (1-3\epsilon^2)/(1+6\epsilon^2) \approx 1 - 9\epsilon^2$.

So $1 - t \approx 9\epsilon^2$ and $w - 1 \approx 6\epsilon^2$. Thus $w - 1 \approx \frac{6}{9}(1-t) = \frac{2}{3}(1-t)$.

Now $\phi(t)$ near $t = 1$: Let $t = 1 - \delta$.

$\phi(t) = \frac{45 - 27t^{1/3}}{17 + 4t - 3t^{1/3}}$.

$t^{1/3} \approx 1 - \delta/3$.

Numerator: $45 - 27(1-\delta/3) = 45 - 27 + 9\delta = 18 + 9\delta$.

Denominator: $17 + 4(1-\delta) - 3(1-\delta/3) = 17 + 4 - 4\delta - 3 + \delta = 18 - 3\delta$.

$\phi \approx \frac{18+9\delta}{18-3\delta} \approx (1+\delta/2)(1+\delta/6) \approx 1 + \frac{2\delta}{3}$.

So $\phi(t) \approx 1 + \frac{2}{3}\delta = 1 + \frac{2}{3}(1-t)$.

And $w \approx 1 + \frac{2}{3}(1-t)$.

So $w \approx \phi(t)$ to second order! This means the inequality $w \ge \phi(t)$ is tight to second order at $t = 1$ along the two-equal curve.

This is very strong evidence that the inequality holds, but I need to prove it rigorously.

Let me try to prove $w \ge \phi(t)$, i.e., $w(17 + 4t - 3t^{1/3}) \ge 45 - 27t^{1/3}$, where $t = v/w = 3pqr/(p^3+q^3+r^3)$ and $w = (p^3+q^3+r^3)/3$.

Substituting $t = v/w$:

$w(17 + 4v/w - 3(v/w)^{1/3}) \ge 45 - 27(v/w)^{1/3}$

$17w + 4v - 3w(v/w)^{1/3} \ge 45 - 27(v/w)^{1/3}$

$17w + 4v - 3w^{2/3}v^{1/3} \ge 45 - 27v^{1/3}w^{-1/3}$

$17w + 4v - 3w^{2/3}v^{1/3} + 27v^{1/3}w^{-1/3} \ge 45$

Let $s = (v/w)^{1/3} = t^{1/3}$. Then $v = s^3 w$ and:

$17w + 4s^3 w - 3w \cdot s + 27s \ge 45$

$w(17 + 4s^3 - 3s) + 27s \ge 45$

$w \ge \frac{45 - 27s}{17 + 4s^3 - 3s}$

where $s = (v/w)^{1/3} \in (0, 1]$.

Now, $w = (p^3+q^3+r^3)/3$ and $v = pqr$ with $p+q+r=3$.

$s^3 = v/w = 3pqr/(p^3+q^3+r^3)$.

By AM-GM, $p^3+q^3+r^3 \ge 3pqr$, so $s^3 \le 1$, i.e., $s \le 1$. ✓

Now I need to show $w \ge \frac{45-27s}{17+4s^3-3s}$ for all valid $(w, s)$.

Note that $17 + 4s^3 - 3s > 0$ for $s \in (0, 1]$ (at $s=0$: 17, at $s=1$: 18).

And $45 - 27s > 0$ for $s \in (0, 1]$ (at $s=1$: 18).

At $s = 1$: $\phi = 18/18 = 1 = w_{min}$. ✓

The key question: for a given $s$, what is the minimum $w$?

We have $w = (p^3+q^3+r^3)/3$ and $s^3 = 3pqr/(p^3+q^3+r^3) = v/w$, so $v = s^3 w$.

With $p+q+r = 3$, $pq+qr+rp = \sigma$, $pqr = v = s^3 w$:

$w = (27 - 9\sigma + 3v)/3 = 9 - 3\sigma + v = 9 - 3\sigma + s^3 w$.

$w(1 - s^3) = 9 - 3\sigma$

$\sigma = \frac{9 - w(1-s^3)}{3} = 3 - \frac{w(1-s^3)}{3}$.

For $p, q, r$ to be real positive with $p+q+r = 3$ and $pq+qr+rp = \sigma$, $pqr = v$, we need the discriminant to be non-negative, and $\sigma \le 3$ (by $(p+q+r)^2 \ge 3\sigma$, i.e., $9 \ge 3\sigma$), and $\sigma > 0$, and $v > 0$.

Also, by Schur's inequality: $p^3+q^3+r^3 + pqr \ge (p+q+r)(pq+qr+rp)$, i.e., $3w + v \ge 3\sigma$, i.e., $3w + s^3 w \ge 3\sigma = 9 - w(1-s^3)$, i.e., $w(3 + s^3 + 1 - s^3) \ge 9$, i.e., $4w \ge 9$, i.e., $w \ge 9/4$.

Wait, that gives $w \ge 9/4$? But at $p=q=r=1$, $w = 1 < 9/4$. Let me recheck.

Schur's inequality (degree 3): $p^3+q^3+r^3 + pqr \ge (p+q+r)(pq+qr+rp)$ for $p, q, r \ge 0$.

At $p=q=r=1$: $3 + 1 = 4 \ge 3 \cdot 3 = 9$? That's $4 \ge 9$, which is false!

Hmm, Schur's inequality is $p^t(p-q)(p-r) + q^t(q-p)(q-r) + r^t(r-p)(r-q) \ge 0$ for $t \ge 0$.

For $t = 1$: $\sum p(p-q)(p-r) \ge 0$, which expands to $p^3+q^3+r^3 + pqr \ge (p+q+r)(pq+qr+rp)$... 

Wait, let me expand $\sum p(p-q)(p-r) = \sum p(p^2 - pr - pq + qr) = \sum (p^3 - p^2r - p^2q + pqr) = (p^3+q^3+r^3) - (p^2q+p^2r+q^2p+q^2r+r^2p+r^2q) + 3pqr$.

$= (p^3+q^3+r^3) - (p+q+r)(pq+qr+rp) + 3pqr + 3pqr$... 

Hmm, $p^2q + p^2r + q^2p + q^2r + r^2p + r^2q = (p+q+r)(pq+qr+rp) - 3pqr$.

So $\sum p(p-q)(p-r) = (p^3+q^3+r^3) - (p+q+r)\sigma + 3pqr + 3pqr = (p^3+q^3+r^3) - (p+q+r)\sigma + 3pqr$.

Wait: $(p^3+q^3+r^3) - [(p+q+r)\sigma - 3pqr] + 3pqr = (p^3+q^3+r^3) - (p+q+r)\sigma + 3pqr + 3pqr$?

No. $\sum p(p-q)(p-r) = \sum (p^3 - p^2q - p^2r + pqr) = (p^3+q^3+r^3) - \sum(p^2q + p^2r) + 3pqr$.

$\sum(p^2q + p^2r) = p^2(q+r) + q^2(p+r) + r^2(p+q) = p^2(3-p) + q^2(3-q) + r^2(3-r) = 3(p^2+q^2+r^2) - (p^3+q^3+r^3)$.

$= 3 \cdot 9 -
