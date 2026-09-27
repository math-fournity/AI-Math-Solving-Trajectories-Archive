# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   For nonnegative integers \( p, q, r \), let

\[
f(p, q, r) = (p!)^{p}(q!)^{q}(r!)^{r}
\]

Compute the smallest positive integer \( n \) such that for any triples \((a, b, c)\) and \((x, y, z)\) of nonnegative integers satisfying \( a+b+c=2020 \) and \( x+y+z=n \), \( f(x, y, z) \) is divisible by \( f(a, b, c) \).       — 题目文本
#   The smallest positive integer \( n \) is \( 6052 \).

\(\boxed{6052}\)  — 标准解答
#   Let me solve this problem. I need to find the smallest positive integer n such that for any triples (a,b,c) and (x,y,z) of nonnegative integers with a+b+c=2020 and x+y+z=n, f(x,y,z) is divisible by f(a,b,c).

First, let me check for answer leaks. The problem text doesn't contain any solutions or answer values. Good.

Let me think about this problem carefully.

We have $f(p,q,r) = (p!)^p (q!)^q (r!)^r$.

We need: for ALL triples $(a,b,c)$ with $a+b+c=2020$ and ALL triples $(x,y,z)$ with $x+y+z=n$, $f(x,y,z) \mid$ is divisible by $f(a,b,c)$.

Wait, re-reading: "f(x,y,z) is divisible by f(a,b,c)" means $f(a,b,c) \mid f(x,y,z)$.

So we need: for every $(a,b,c)$ with $a+b+c=2020$ and every $(x,y,z)$ with $x+y+z=n$, $f(a,b,c) \mid f(x,y,z)$.

This means $f(x,y,z)$ must be divisible by $\text{lcm}$ over all $(a,b,c)$ with $a+b+c=2020$ of $f(a,b,c)$, for every $(x,y,z)$ with $x+y+z=n$.

So we need: for every $(x,y,z)$ with $x+y+z=n$, $f(x,y,z)$ is divisible by $L = \text{lcm}_{a+b+c=2020} f(a,b,c)$.

And we want the smallest $n$ such that this holds.

Let me think about the $p$-adic valuation. For a prime $p$, let $v_p(m)$ denote the $p$-adic valuation.

$v_p(f(a,b,c)) = a \cdot v_p(a!) + b \cdot v_p(b!) + c \cdot v_p(c!)$.

We need, for every $(x,y,z)$ with $x+y+z=n$:
$v_p(f(x,y,z)) \geq \max_{a+b+c=2020} v_p(f(a,b,c))$ for every prime $p$.

So for each prime $p$, let $M_p = \max_{a+b+c=2020} [a \cdot v_p(a!) + b \cdot v_p(b!) + c \cdot v_p(c!)]$.

And we need: for every $(x,y,z)$ with $x+y+z=n$, $x \cdot v_p(x!) + y \cdot v_p(y!) + z \cdot v_p(z!) \geq M_p$ for every prime $p$.

The smallest $n$ is the smallest $n$ such that $\min_{x+y+z=n} [x \cdot v_p(x!) + y \cdot v_p(y!) + z \cdot v_p(z!)] \geq M_p$ for all primes $p$.

Let me define $g_p(k) = k \cdot v_p(k!)$ for $k \geq 0$ (with $g_p(0) = 0$).

Then $M_p = \max_{a+b+c=2020} [g_p(a) + g_p(b) + g_p(c)]$.

And we need $\min_{x+y+z=n} [g_p(x) + g_p(y) + g_p(z)] \geq M_p$ for all primes $p$.

So the answer is $n = \max_p n_p$ where $n_p$ is the smallest $n$ such that $\min_{x+y+z=n} [g_p(x)+g_p(y)+g_p(z)] \geq M_p$.

Now, $g_p(k) = k \cdot v_p(k!)$. Note $v_p(k!) = \sum_{i=1}^{k} v_p(i) = \frac{k - s_p(k)}{p-1}$ where $s_p(k)$ is the sum of digits of $k$ in base $p$.

So $g_p(k) = k \cdot \frac{k - s_p(k)}{p-1} = \frac{k^2 - k \cdot s_p(k)}{p-1}$.

This is a complicated function. Let me think about which primes matter.

For $p > 2020$, $v_p(k!) = 0$ for $k \leq 2020$, so $g_p(k) = 0$ for all relevant $k$, and $M_p = 0$. So only primes $p \leq 2020$ matter.

Actually, for $p > 2020$, $v_p(a!) = 0$ for $a \leq 2020$, so $M_p = 0$, and the condition is trivially satisfied. So we only need primes $p \leq 2020$.

Now, the key question: for each prime $p$, what is $M_p$ and what is $n_p$?

Let me think about $M_p$ first. We want to maximize $g_p(a) + g_p(b) + g_p(c)$ subject to $a+b+c = 2020$, $a,b,c \geq 0$.

Since $g_p$ is convex (roughly quadratic), the maximum is achieved at an extreme point: one of $a,b,c$ is as large as possible. So the maximum is $g_p(2020) + g_p(0) + g_p(0) = g_p(2020) = 2020 \cdot v_p(2020!)$.

Wait, is $g_p$ convex? $g_p(k) = k \cdot v_p(k!)$. Let's check: $g_p(k+1) - g_p(k) = (k+1)v_p((k+1)!) - k \cdot v_p(k!) = (k+1)(v_p(k!) + v_p(k+1)) - k \cdot v_p(k!) = v_p(k!) + (k+1)v_p(k+1)$.

The second difference: $[g_p(k+2) - g_p(k+1)] - [g_p(k+1) - g_p(k)] = [v_p((k+1)!) + (k+2)v_p(k+2)] - [v_p(k!) + (k+1)v_p(k+1)]$
$= v_p(k+1) + (k+2)v_p(k+2) - (k+1)v_p(k+1)$
$= v_p(k+1) + (k+2)v_p(k+2) - (k+1)v_p(k+1)$
$= v_p(k+1)(1 - (k+1)) + (k+2)v_p(k+2)$
$= -k \cdot v_p(k+1) + (k+2)v_p(k+2)$.

This isn't always non-negative. For example, if $v_p(k+1) > 0$ and $v_p(k+2) = 0$, this could be negative.

So $g_p$ is not necessarily convex. Let me reconsider.

Actually, let me think more carefully. The function $g_p(k) = k \cdot v_p(k!)$. 

Let me compute $g_p$ for small values to get intuition. Take $p=2$:
- $g_2(0) = 0$
- $g_2(1) = 1 \cdot 0 = 0$
- $g_2(2) = 2 \cdot 1 = 2$
- $g_2(3) = 3 \cdot 1 = 3$
- $g_2(4) = 4 \cdot 3 = 12$
- $g_2(5) = 5 \cdot 3 = 15$
- $g_2(6) = 6 \cdot 4 = 24$
- $g_2(7) = 7 \cdot 4 = 28$
- $g_2(8) = 8 \cdot 7 = 56$

The differences: 0, 2, 1, 9, 3, 9, 4, 28. These are not monotone, so $g_p$ is not convex.

So maximizing $g_p(a) + g_p(b) + g_p(c)$ with $a+b+c=2020$ is not simply putting everything in one variable.

Hmm, this is more complex. Let me think about this differently.

Actually, let me reconsider the structure. We have $g_p(k) = k \cdot v_p(k!)$. 

Note that $v_p(k!)$ counts the number of factors of $p$ in $k!$. And $k \cdot v_p(k!)$ is like summing $v_p(j)$ for each $j$ from 1 to $k$, but multiplied by $k$. Actually:

$g_p(k) = k \cdot \sum_{j=1}^{k} v_p(j) = \sum_{j=1}^{k} k \cdot v_p(j)$.

Alternatively, $g_p(k) = \sum_{j=1}^{k} \sum_{i=1}^{k} v_p(j) = \sum_{i=1}^{k}\sum_{j=1}^{k} v_p(j)$... no that's $k \cdot \sum v_p(j)$ which is the same.

Hmm, let me think of it as $g_p(k) = \sum_{j=1}^{k} v_p(j) \cdot k$. 

Actually, let me think about it differently. $g_p(k) = k \cdot v_p(k!)$. Consider the sum $g_p(a) + g_p(b) + g_p(c)$ where $a+b+c = N = 2020$.

$g_p(a) + g_p(b) + g_p(c) = a \cdot v_p(a!) + b \cdot v_p(b!) + c \cdot v_p(c!)$.

Let me think about what configuration maximizes this. 

Consider the contribution of each factor of $p$ in the factorials. $v_p(a!) = \sum_{j \geq 1} \lfloor a/p^j \rfloor$. So:

$g_p(a) = a \sum_{j \geq 1} \lfloor a/p^j \rfloor$.

For a fixed $j$, the contribution to $g_p(a) + g_p(b) + g_p(c)$ from the $j$-th term is:
$a \lfloor a/p^j \rfloor + b \lfloor b/p^j \rfloor + c \lfloor c/p^j \rfloor$.

Now, $h(x) = x \lfloor x/p^j \rfloor$ is a step function. For $x$ in $[mp^j, (m+1)p^j)$, $h(x) = mx$. This is increasing in $x$ (for fixed $m$), and jumps up at multiples of $p^j$.

To maximize $\sum h(a_i)$ with $\sum a_i = N$, since $h$ is "superadditive-ish" (concave pieces with jumps), the maximum tends to be at extreme points. Let me think...

Actually, $h(x) = x \lfloor x/q \rfloor$ where $q = p^j$. Write $x = mq + r$ with $0 \leq r < q$. Then $h(x) = mx = m(mq+r) = m^2 q + mr$.

Consider two variables $x, y$ with $x + y = S$. Write $x = mq + r$, $y = m'q + r'$. We want to compare $h(x) + h(y)$ vs $h(x+y) + h(0) = h(S)$.

$h(x) + h(y) = m^2 q + mr + m'^2 q + m'r$.
$h(S) = h(x+y)$. Let $S = Mq + R$. Then $h(S) = M(Mq + R) = M^2 q + MR$.

Since $M = m + m' + \lfloor (r+r')/q \rfloor$ and $R = (r + r') \mod q$.

If $r + r' < q$: $M = m + m'$, $R = r + r'$.
$h(S) = (m+m')^2 q + (m+m')(r+r') = (m^2 + 2mm' + m'^2)q + mr + mr' + m'r + m'r'$.
$h(x) + h(y) = (m^2 + m'^2)q + mr + m'r'$.
$h(S) - (h(x)+h(y)) = 2mm'q + mr' + m'r \geq 0$.

So $h(S) \geq h(x) + h(y)$ when $r + r' < q$. This means concentrating is better!

If $r + r' \geq q$: $M = m + m' + 1$, $R = r + r' - q$.
$h(S) = (m+m'+1)((m+m'+1)q + r+r'-q) = (m+m'+1)(m+m')q + (m+m'+1)(r+r'-q)$.
$= (m+m'+1)(m+m')q + (m+m'+1)(r+r') - (m+m'+1)q$
$= (m+m')(m+m'+1)q + (m+m'+1)(r+r') - (m+m'+1)q$
$= (m+m')((m+m'+1)-1)q + (m+m'+1)(r+r') - (m+m'+1)q$

Hmm, this is getting messy. Let me just compute:
$h(S) = M^2 q + MR = (m+m'+1)^2 q + (m+m'+1)(r+r'-q)$.

$h(x)+h(y) = (m^2+m'^2)q + mr + m'r'$.

$h(S) - (h(x)+h(y)) = [(m+m'+1)^2 - m^2 - m'^2]q + (m+m'+1)(r+r'-q) - mr - m'r'$
$= [2mm' + 2m + 2m' + 1]q + (m+m'+1)(r+r') - (m+m'+1)q - mr - m'r'$
$= [2mm' + 2m + 2m' + 1 - m - m' - 1]q + (m+m'+1)(r+r') - mr - m'r'$
$= [2mm' + m + m']q + (m+m'+1)(r+r') - mr - m'r'$
$= [2mm' + m + m']q + mr + m'r' + r + r' + mr' + m'r - mr - m'r'$
Wait, let me redo: $(m+m'+1)(r+r') = mr + mr' + m'r + m'r' + r + r'$.
So $(m+m'+1)(r+r') - mr - m'r' = mr' + m'r + r + r'$.

$h(S) - (h(x)+h(y)) = (2mm' + m + m')q + mr' + m'r + r + r'$.

Since $r + r' \geq q$ (in this case), and all terms are non-negative, this is $\geq (2mm'+m+m')q + q = (2mm' + m + m' + 1)q > 0$.

So in both cases, $h(S) \geq h(x) + h(y)$, with equality only when $m = m' = 0$ and $r + r' < q$ (i.e., both $x, y < q$ and $x + y < q$).

This means $h(x) = x\lfloor x/q \rfloor$ is superadditive! So $h(a) + h(b) + h(c) \leq h(a+b+c) = h(N)$.

Therefore, for each $j$, $a\lfloor a/p^j \rfloor + b\lfloor b/p^j \rfloor + c\lfloor c/p^j \rfloor \leq N \lfloor N/p^j \rfloor$ where $N = 2020$.

Summing over $j$: $g_p(a) + g_p(b) + g_p(c) \leq g_p(N) = g_p(2020)$.

So $M_p = g_p(2020) = 2020 \cdot v_p(2020!)$, achieved by $(a,b,c) = (2020, 0, 0)$.

Great, so $M_p = 2020 \cdot v_p(2020!)$ for each prime $p$.

Now, we need: for every $(x,y,z)$ with $x+y+z = n$, $g_p(x) + g_p(y) + g_p(z) \geq M_p = g_p(2020)$ for all primes $p$.

So we need: $\min_{x+y+z=n} [g_p(x) + g_p(y) + g_p(z)] \geq g_p(2020)$ for all primes $p \leq 2020$.

And we want the smallest such $n$.

Now, by the superadditivity we proved, $g_p(x) + g_p(y) + g_p(z) \leq g_p(n)$. So we need $g_p(n) \geq g_p(2020)$, which means $n \geq 2020$ (since $g_p$ is increasing for $p \leq n$... well, $g_p$ is non-decreasing).

But we need the minimum over all triples to be $\geq g_p(2020)$, not just the maximum. So $n$ must be large enough that even the worst-case triple gives enough.

The worst case for $g_p(x) + g_p(y) + g_p(z)$ with $x+y+z=n$ is when the values are as "spread out" as possible in a way that minimizes the sum. Since $g_p$ is superadditive, the minimum of $g_p(x)+g_p(y)+g_p(z)$ with $x+y+z=n$ is achieved when... hmm, superadditivity means $g_p(x)+g_p(y) \leq g_p(x+y)$, so splitting decreases the sum. So the minimum is achieved by splitting as much as possible.

Wait, but we have exactly 3 parts. So the minimum of $g_p(x)+g_p(y)+g_p(z)$ with $x+y+z=n$, $x,y,z \geq 0$ is achieved by making the split as balanced as possible? Or as unbalanced as possible?

Since $g_p$ is superadditive, $g_p(x) + g_p(y) \leq g_p(x+y)$. So to minimize, we want to split. With 3 parts, the most split is $\lfloor n/3 \rfloor, \lfloor n/3 \rfloor, n - 2\lfloor n/3 \rfloor$ or something like that. But actually, superadditivity just says splitting into 2 reduces, and splitting into 3 reduces more. But the exact minimum depends on the structure of $g_p$.

Hmm wait, actually superadditivity says $g_p(a) + g_p(b) \leq g_p(a+b)$. So $g_p(x) + g_p(y) + g_p(z) \leq g_p(x+y) + g_p(z) \leq g_p(x+y+z) = g_p(n)$. The minimum is when we split the most.

But with 3 variables, the "most split" would be roughly equal: $x \approx y \approx z \approx n/3$. But is that right? Let me think again.

Actually, superadditivity means that merging increases the sum. So to minimize, we want to avoid merging, i.e., split as evenly as possible. But the exact minimum depends on $g_p$'s structure.

Actually, let me reconsider. We want to minimize $g_p(x) + g_p(y) + g_p(z)$ subject to $x+y+z = n$. 

Since $g_p$ is superadditive, we know the minimum is at most $g_p(n)$ (achieved by $(n,0,0)$... wait no, that gives $g_p(n) + 0 + 0 = g_p(n)$, which is the maximum by superadditivity). The minimum is achieved by splitting.

Let me think about what splitting does. If we split $n$ into $x$ and $n-x$, the sum changes from $g_p(n)$ to $g_p(x) + g_p(n-x)$. By superadditivity, this is $\leq g_p(n)$. The "loss" is $g_p(n) - g_p(x) - g_p(n-x)$.

To minimize the total, we want to maximize the total loss from splitting. 

Let me think about this more carefully for specific primes.

For large primes $p$ (say $p > n/3$), $v_p(k!) = 0$ for $k < p$ and $v_p(k!) = 1$ for $p \leq k < 2p$, etc. So $g_p(k) = k \cdot v_p(k!) = 0$ for $k < p$, $g_p(k) = k$ for $p \leq k < 2p$, $g_p(k) = 2k$ for $2p \leq k < 3p$, etc.

For $p > 2020$ but $p \leq n$: $g_p(2020) = 0$ (since $2020 < p$). So $M_p = 0$, and the condition is trivially satisfied. Good.

For primes $p$ with $1010 < p \leq 2020$: $v_p(2020!) = 1$ (since $2020 < 2p$ as $p > 1010$). So $g_p(2020) = 2020$.

We need $\min_{x+y+z=n} [g_p(x) + g_p(y) + g_p(z)] \geq 2020$.

For such $p$, $g_p(k) = 0$ if $k < p$, $g_p(k) = k$ if $p \leq k < 2p$, etc.

If $n < 3p$, then we can have at most 2 of $x,y,z$ be $\geq p$. The minimum sum would be achieved by having as few variables $\geq p$ as possible.

If $n \geq 3p$: all three can be $\geq p$, and $g_p(x)+g_p(y)+g_p(z) \geq x+y+z = n$ (if all are $\geq p$ and $< 2p$). But we need to check if we can have all three $< p$: that requires $n < 3p$, i.e., $n \leq 3p - 1$.

If $n < 3p$, we can choose $x = y = z = \lfloor n/3 \rfloor < p$ (if $n/3 < p$), giving $g_p = 0$ for each, total 0 < 2020. So we need $n \geq 3p$.

Wait, but if $n \geq 3p$, can we still have all three $< p$? No, because $x + y + z = n \geq 3p$ and $x, y, z < p$ gives $x+y+z < 3p$, contradiction. So at least one is $\geq p$.

But we need the minimum to be $\geq 2020$. If $n = 3p$, the minimum is achieved at $x = y = z = p$, giving $g_p(p) + g_p(p) + g_p(p) = 3p$. We need $3p \geq 2020$, i.e., $p \geq 674$. But we're considering $p > 1010$, so $3p > 3030 > 2020$. 

But wait, can we do worse? With $n = 3p$, can we have $x = 0, y = 0, z = 3p$? Then $g_p(0) + g_p(0) + g_p(3p) = 3 \cdot 3p = 9p$ (since $v_p((3p)!) = 3$). That's bigger. The minimum at $n = 3p$ is at $x=y=z=p$: $3p$.

Hmm, but actually we could also try $x = p-1, y = p-1, z = p+2$. Then $g_p(p-1) + g_p(p-1) + g_p(p+2) = 0 + 0 + (p+2) = p+2$. That's less than $3p$!

Wait, $p + 2 < 3p$ for $p > 1$. So the minimum is not at $x = y = z = p$.

Let me reconsider. With $n = 3p$, we want to minimize $g_p(x) + g_p(y) + g_p(z)$. We can have two variables just below $p$ (so $g_p = 0$) and one variable $= n - 2(p-1) = 3p - 2p + 2 = p + 2$. Then $g_p(p+2) = p+2$ (since $v_p((p+2)!) = 1$ as $p+2 < 2p$ for $p > 2$).

So the minimum is $p + 2$, not $3p$. We need $p + 2 \geq 2020$, i.e., $p \geq 2018$.

But we're considering primes $p$ with $1010 < p \leq 2020$. The largest such prime is $2017$. For $p = 2017$: $n = 3 \cdot 2017 = 6051$, minimum is $2017 + 2 = 2019 < 2020$. Not enough!

So we need $n > 3p$ for $p = 2017$. Let's figure out the exact requirement.

For a prime $p$ with $1010 < p \leq 2020$, $g_p(2020) = 2020$. We need $\min_{x+y+z=n} [g_p(x)+g_p(y)+g_p(z)] \geq 2020$.

$g_p(k) = k \cdot v_p(k!)$. For $k < p$: $g_p(k) = 0$. For $p \leq k < 2p$: $g_p(k) = k$. For $2p \leq k < 3p$: $g_p(k) = 2k$. Etc.

To minimize $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = n$:
- We want as many variables as possible to be $< p$ (contributing 0).
- At most 2 can be $< p$ (since if all 3 are $< p$, sum $< 3p$).
- If 2 are $< p$ (say $x, y < p$, $x + y \leq 2(p-1) = 2p - 2$), then $z = n - x - y \geq n - 2p + 2$.
  - To minimize, set $x = y = p - 1$ (maximizing $x + y$ to minimize $z$'s contribution... wait, we want to minimize $g_p(z)$, and $g_p(z) = z \cdot v_p(z!)$. If $z < 2p$, $g_p(z) = z$. If $z \geq 2p$, $g_p(z) = 2z$ or more.
  
  Actually, we want to minimize $g_p(z)$. With $z = n - 2(p-1) = n - 2p + 2$:
  - If $z < p$: $g_p(z) = 0$. But $z = n - 2p + 2 < p$ means $n < 3p - 2$. Then all three can be $< p$, and the min is 0. Not useful.
  - If $p \leq z < 2p$: $g_p(z) = z = n - 2p + 2$. This is the case when $3p - 2 \leq n < 4p - 2$.
  - If $2p \leq z < 3p$: $g_p(z) = 2z = 2(n - 2p + 2)$. But maybe it's better to have one of $x, y$ be $\geq p$ instead.

Let me think more carefully. We want to minimize $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = n$.

Case 1: All three $< p$. Requires $n \leq 3(p-1) = 3p - 3$. Sum = 0.

Case 2: Exactly one $\geq p$. Say $z \geq p$, $x, y < p$. Then $x + y \leq 2p - 2$, $z = n - x - y \geq n - 2p + 2$.
- To minimize $g_p(z)$, we want $z$ as small as possible (if $g_p$ is increasing, which it is for $z \geq p$). So set $x + y = 2p - 2$, $z = n - 2p + 2$.
- If $z < 2p$ (i.e., $n < 4p - 2$): $g_p(z) = z = n - 2p + 2$.
- If $2p \leq z < 3p$ (i.e., $4p - 2 \leq n < 5p - 2$): $g_p(z) = 2z = 2(n-2p+2)$.
  - But maybe better to have 2 variables $\geq p$. Let's check.

Case 3: Exactly two $\geq p$. Say $y, z \geq p$, $x < p$. $x \leq p-1$, $y + z = n - x \geq n - p + 1$.
- To minimize $g_p(y) + g_p(z)$, by superadditivity, we want $y, z$ as equal as possible? No, superadditivity says $g_p(y) + g_p(z) \leq g_p(y+z)$, so splitting reduces. So we want $y, z$ as split as possible, i.e., as equal as possible.
- Set $x = p - 1$, $y = z = (n - p + 1)/2$ (if even) or close to it.
- If $y, z < 2p$ (i.e., $(n-p+1)/2 < 2p$, i.e., $n < 5p - 1$): $g_p(y) + g_p(z) = y + z = n - p + 1$.
  - Compare with Case 2: $n - 2p + 2$ vs $n - p + 1$. Case 2 is smaller by $p - 1$. So Case 2 is better.

Case 4: All three $\geq p$. Requires $n \geq 3p$. 
- $g_p(x) + g_p(y) + g_p(z) \geq x + y + z = n$ (if all $< 2p$). This is worse than Case 2.

So the minimum is achieved in Case 2: two variables at $p-1$, one at $n - 2p + 2$, giving $g_p = n - 2p + 2$ (when $p \leq n - 2p + 2 < 2p$, i.e., $3p - 2 \leq n \leq 4p - 3$).

Wait, but I should also consider the case where $z \geq 2p$ in Case 2, and compare with Case 3.

For $n \geq 4p - 2$ (so $z \geq 2p$ in Case 2):
- Case 2: $g_p(z) = 2z = 2(n - 2p + 2)$ (if $z < 3p$, i.e., $n < 5p - 2$).
- Case 3: $g_p(y) + g_p(z) = (n - p + 1)$ (if both $< 2p$, i.e., $n < 5p - 1$).
- Case 2 gives $2n - 4p + 4$, Case 3 gives $n - p + 1$.
- Case 3 < Case 2 iff $n - p + 1 < 2n - 4p + 4$ iff $3p < n + 3$ iff $n > 3p - 3$.
- Since $n \geq 4p - 2 > 3p - 3$, Case 3 is better.

So for $n \geq 4p - 2$, Case 3 is better. In Case 3 with $y, z < 2p$:
- $g_p(y) + g_p(z) = y + z = n - p + 1$ (with $x = p - 1$).
- This requires $y, z \geq p$ and $y, z < 2p$, so $n - p + 1 \geq 2p$ (i.e., $n \geq 3p - 1$) and $(n-p+1)/2 < 2p$ (i.e., $n < 5p - 1$).

For $n \geq 5p - 1$, we'd need to consider further cases. But let me also check: in Case 3, if one of $y, z \geq 2p$:
- Set $x = p-1$, $y = p$, $z = n - 2p + 1$. If $z \geq 2p$ (i.e., $n \geq 4p - 1$): $g_p(y) + g_p(z) = p + 2z = p + 2(n - 2p + 1) = 2n - 3p + 2$.
- Compare with balanced: $n - p + 1$. $n - p + 1 < 2n - 3p + 2$ iff $2p < n + 1$ iff $n > 2p - 1$. True for $n \geq 4p - 1$. So balanced is better.

OK so to summarize for a prime $p$ with $1010 < p \leq 2020$ (so $v_p(2020!) = 1$, $M_p = 2020$):

The minimum of $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = n$ is:
- $0$ if $n \leq 3p - 3$ (all three $< p$)
- $n - 2p + 2$ if $3p - 2 \leq n \leq 4p - 3$ (two at $p-1$, one at $n-2p+2 < 2p$)
- $n - p + 1$ if $4p - 2 \leq n \leq 5p - 2$ (one at $p-1$, two balanced, both $< 2p$)
- ... and so on for larger $n$.

We need this minimum $\geq 2020$.

For the range $3p - 2 \leq n \leq 4p - 3$: need $n - 2p + 2 \geq 2020$, i.e., $n \geq 2p + 2018$.
For the range $4p - 2 \leq n \leq 5p - 2$: need $n - p + 1 \geq 2020$, i.e., $n \geq p + 2019$.

The binding constraint is the first range: $n \geq 2p + 2018$ (and this must be in the range $[3p-2, 4p-3]$, i.e., $2p + 2018 \leq 4p - 3$, i.e., $p \geq 1010.5$, i.e., $p \geq 1011$). Since we're considering $p > 1010$, this works.

But we also need $2p + 2018 \geq 3p - 2$, i.e., $p \leq 2020$. Which is true.

So for prime $p$ with $1010 < p \leq 2020$: $n_p = 2p + 2018$.

The largest such prime is $2017$. So $n_{2017} = 2 \cdot 2017 + 2018 = 4034 + 2018 = 6052$.

Wait, let me double-check. For $p = 2017$: $n_p = 2 \cdot 2017 + 2018 = 6052$. And we need $3p - 2 \leq n_p \leq 4p - 3$: $3 \cdot 2017 - 2 = 6049 \leq 6052 \leq 4 \cdot 2017 - 3 = 8065$. Yes, $6049 \leq 6052 \leq 8065$. ✓

So for $p = 2017$, we need $n \geq 6052$.

Now let me check other primes. For primes $p$ with $673 < p \leq 1010$ (so $v_p(2020!) = 2$, since $2p \leq 2020 < 3p$): $M_p = 2020 \cdot 2 = 4040$.

Hmm wait, $v_p(2020!) = \lfloor 2020/p \rfloor + \lfloor 2020/p^2 \rfloor + \cdots$. For $p > 673$: $\lfloor 2020/p \rfloor = 2$ (since $2p \leq 2020 < 3p$ when $p \leq 1010$ and $p > 673$), and $\lfloor 2020/p^2 \rfloor = 0$ (since $p^2 > 673^2 > 2020$). So $v_p(2020!) = 2$, $M_p = 4040$.

For such $p$, $g_p(k) = k \cdot v_p(k!)$. $v_p(k!) = 0$ for $k < p$, $= 1$ for $p \leq k < 2p$, $= 2$ for $2p \leq k < 3p$.

We need $\min_{x+y+z=n} [g_p(x)+g_p(y)+g_p(z)] \geq 4040$.

Using the same analysis:
- Case 2 (two at $p-1$, one at $z = n - 2p + 2$):
  - If $p \leq z < 2p$: $g_p(z) = z = n - 2p + 2$. Need $\geq 4040$, so $n \geq 2p + 4038$.
  - Check range: $3p - 2 \leq n \leq 4p - 3$, so $2p + 4038 \leq 4p - 3$ iff $p \geq 2020.5$. But $p \leq 1010$, so this doesn't work! The required $n$ is outside this range.

So for $p$ in this range, we need to go to higher cases.

- Case 3 (one at $p-1$, two balanced, both in $[p, 2p)$):
  - $g_p = y + z = n - p + 1$. Need $\geq 4040$, so $n \geq p + 4039$.
  - Range: $4p - 2 \leq n \leq 5p - 2$ (need both $y, z < 2p$). Actually, the range for this case is when $n - p + 1 \geq 2p$ and $(n-p+1)/2 < 2p$, i.e., $n \geq 3p - 1$ and $n < 5p - 1$.
  - Need $p + 4039 \leq 5p - 2$, i.e., $p \geq 1010.25$, i.e., $p \geq 1011$. But $p \leq 1010$, so again outside range!

Hmm. Let me continue to higher cases.

- Case with one at $p-1$, one at $p$, one at $z = n - 2p + 1$:
  - If $2p \leq z < 3p$: $g_p(z) = 2z = 2(n - 2p + 1)$. Total: $p + 2(n - 2p + 1) = 2n - 3p + 2$.
  - Need $2n - 3p + 2 \geq 4040$, i.e., $n \geq (3p + 4038)/2$.
  - Range: $z \geq 2p$ means $n \geq 4p - 1$. $z < 3p$ means $n < 5p - 1$.
  
  Actually wait, I need to be more careful. Let me reconsider.

Let me think about this differently. For a general prime $p$ with $v_p(2020!) = t$ (so $M_p = 2020t$), I need to find the minimum $n$ such that $\min_{x+y+z=n} \sum g_p(x_i) \geq 2020t$.

The function $g_p(k) = k \cdot v_p(k!)$. For $k$ in $[mp, (m+1)p)$, $v_p(k!) = m + v_p(k! \text{ restricted to higher powers})$... actually this is getting complicated because of higher powers of $p$.

Let me simplify by first considering only the contribution from $\lfloor k/p \rfloor$ (the first term in Legendre's formula), and then add corrections for higher powers.

Actually, let me think about this problem from a higher level. The answer is likely determined by the largest prime $\leq 2020$, which is $2017$. Let me check if $n = 6052$ works for all primes.

For $p = 2017$: we showed $n_{2017} = 6052$. Let me verify: with $n = 6052$, the minimum of $g_{2017}(x) + g_{2017}(y) + g_{2017}(z)$ is $6052 - 2 \cdot 2017 + 2 = 6052 - 4034 + 2 = 2020 = M_{2017}$. ✓ (achieved by $(2016, 2016, 2020)$, where $g_{2017}(2016) = 0$, $g_{2017}(2016) = 0$, $g_{2017}(2020) = 2020 \cdot 1 = 2020$).

Now I need to check all other primes $p \leq 2020$ to see if $n = 6052$ suffices.

For a prime $p$, let $t = v_p(2020!)$. We need $\min_{x+y+z=6052} [g_p(x) + g_p(y) + g_p(z)] \geq 2020t$.

The minimum is achieved by making two variables as close to $p-1$ as possible (to have $g_p = 0$) and the third taking the rest. But actually, the optimal strategy to minimize depends on $p$.

Let me think about it. With $n = 6052$, for a prime $p$, the minimum of $g_p(x) + g_p(y) + g_p(z)$ is achieved by:
- Setting two variables to $p - 1$ (so $g_p = 0$ for those), and the third to $n - 2(p-1) = n - 2p + 2$.
- Or some other configuration.

But actually, the minimum might be achieved by a different configuration. Let me think about what minimizes $g_p(x) + g_p(y) + g_p(z)$.

Since $g_p$ is superadditive, splitting reduces the sum. So we want to split as much as possible. But the "splits" that reduce the most are those that cross the "steps" of $g_p$ (i.e., multiples of $p$).

The key insight: $g_p(k) = k \cdot v_p(k!)$. The function $v_p(k!)$ is a step function that increases by 1 at each multiple of $p$, by 1 at each multiple of $p^2$, etc. So $g_p(k)$ has a "kink" at each multiple of $p$.

To minimize $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = n$, we want to "waste" as much as possible just below multiples of $p$ (where $g_p$ is relatively low compared to the linear growth).

The optimal strategy: put two variables just below $p$ (at $p - 1$), and the third takes the rest. This is because the "loss" from superadditivity is maximized when we split at the first step.

Actually, I realize the minimum might not always be two at $p-1$. Let me think more carefully.

For $g_p(k) = k \cdot v_p(k!)$, the function is 0 for $k < p$, then $k$ for $p \leq k < 2p$, then $2k$ for $2p \leq k < 3p$ (ignoring higher powers of $p$ for now), etc.

The "efficiency" $g_p(k)/k = v_p(k!)$ is a step function: 0, 1, 2, 3, ... To minimize $g_p(x) + g_p(y) + g_p(z) = \sum x_i v_p(x_i!)$, we want to minimize the weighted average of $v_p(x_i!)$ with weights $x_i$. So we want as much weight as possible on low $v_p$ values.

The best is to have weight on $v_p = 0$ (i.e., $x_i < p$), but we can have at most 2 variables $< p$ (since $n = 6052$ is large). With 2 variables $< p$ (at $p - 1$ each), the third is $n - 2(p-1) = n - 2p + 2$.

But we could also have 1 variable $< p$ (at $p - 1$) and 2 variables in $[p, 2p)$. The total would be $(p-1) \cdot 0 + y \cdot 1 + z \cdot 1 = y + z = n - p + 1$ (if both in $[p, 2p)$).

Compare: $n - 2p + 2$ (two at $p-1$) vs $n - p + 1$ (one at $p-1$, two in $[p, 2p)$). The first is smaller by $p - 1$. So two at $p-1$ is better, as long as the third variable's $v_p$ doesn't jump too much.

With two at $p-1$, the third is $z = n - 2p + 2$. Its $v_p(z!) = \lfloor z/p \rfloor + \lfloor z/p^2 \rfloor + \cdots$.

$g_p(z) = z \cdot v_p(z!)$.

So the minimum (with this strategy) is $g_p(n - 2p + 2)$.

But is this always the minimum? Could there be a better strategy, like two at $2p - 1$ (with $v_p = 1$) and one taking the rest?

With two at $2p - 1$: $g_p(2p-1) = (2p-1) \cdot 1 = 2p - 1$ each. Third is $n - 2(2p-1) = n - 4p + 2$.
Total: $2(2p-1) + g_p(n - 4p + 2) = 4p - 2 + g_p(n - 4p + 2)$.

Compare with two at $p - 1$: $g_p(n - 2p + 2)$.

For the two-at-$p-1$ strategy: if $z = n - 2p + 2$ is in $[mp, (m+1)p)$, then $g_p(z) = z \cdot (m + \text{higher order terms})$.

For the two-at-$2p-1$ strategy: the third is $n - 4p + 2$, which is smaller, so its $v_p$ might be lower.

This is getting complicated. Let me just compute numerically for the key primes.

Actually, let me step back and think about which primes could be binding. The answer is $n = 6052$ (from $p = 2017$) if all other primes give $n_p \leq 6052$.

For small primes (like $p = 2, 3, 5, \ldots$), $v_p(2020!)$ is large, but $g_p$ grows fast (roughly $k^2/(p-1)$), so the minimum with $n = 6052$ should easily exceed $M_p$.

The critical primes are the large ones, where $v_p(2020!)$ is small (1 or 2) and the "waste" from splitting is significant.

Let me check primes near $1010$ (where $v_p(2020!) = 2$).

For $p = 1009$ (prime, $1009 \cdot 2 = 2018 \leq 2020 < 3027 = 3 \cdot 1009$): $v_p(2020!) = 2$, $M_p = 4040$.

With $n = 6052$, two at $p - 1 = 1008$: $z = 6052 - 2016 = 4036$. $v_{1009}(4036!) = \lfloor 4036/1009 \rfloor + \lfloor 4036/1009^2 \rfloor = 4 + 0 = 4$. So $g_p(z) = 4036 \cdot 4 = 16144 \geq 4040$. ✓

So for $p = 1009$, $n = 6052$ is more than enough.

Let me check $p = 2011$ (prime, $v_p(2020!) = 1$, $M_p = 2020$):
Two at $2010$: $z = 6052 - 4020 = 2032$. $v_{2011}(2032!) = \lfloor 2032/2011 \rfloor = 1$. $g_p(z) = 2032 \cdot 1 = 2032 \geq 2020$. ✓

$p = 2017$: $z = 6052 - 4032 = 2020$. $v_{2017}(2020!) = 1$. $g_p(z) = 2020 \cdot 1 = 2020 = M_p$. ✓ (exactly meets the bound)

$p = 2020$ is not prime. What about primes just below 2017?

$p = 2011$: checked, ✓.
$p = 2017$: exactly meets. ✓.

What about primes between 2017 and 2020? There are none (2018, 2019, 2020 are not prime).

Now let me check: is there a prime $p$ with $v_p(2020!) = 1$ (i.e., $1010 < p \leq 2020$) where $n = 6052$ doesn't work?

For such $p$, two at $p-1$: $z = 6052 - 2(p-1) = 6052 - 2p + 2 = 6054 - 2p$.
$v_p(z!) = \lfloor z/p \rfloor = \lfloor (6054 - 2p)/p \rfloor = \lfloor 6054/p - 2 \rfloor = \lfloor 6054/p \rfloor - 2$.

$g_p(z) = z \cdot v_p(z!) = (6054 - 2p)(\lfloor 6054/p \rfloor - 2)$.

We need this $\geq 2020$.

For $p = 2017$: $\lfloor 6054/2017 \rfloor = 3$. $g_p(z) = (6054 - 4034)(3 - 2) = 2020 \cdot 1 = 2020$. ✓

For $p = 2011$: $\lfloor 6054/2011 \rfloor = 3$. $g_p(z) = (6054 - 4022)(3-2) = 2032 \cdot 1 = 2032 \geq 2020$. ✓

For general $p$ with $1010 < p \leq 2020$: $\lfloor 6054/p \rfloor \geq \lfloor 6054/2020 \rfloor = 2$. Hmm, for $p = 2020$... but 2020 is not prime. For $p = 2017$: $\lfloor 6054/2017 \rfloor = 3$ (since $3 \cdot 2017 = 6051 \leq 6054$). For $p = 2019$ (not prime). For $p$ slightly larger than $2018$: $\lfloor 6054/p \rfloor = 2$ (since $2p > 4036$ and $3p > 6054$ for $p > 2018$).

Wait, $3 \cdot 2017 = 6051 \leq 6054$, so $\lfloor 6054/2017 \rfloor = 3$. But $3 \cdot 2018 = 6054$, so $\lfloor 6054/2018 \rfloor = 3$. And $3 \cdot 2019 = 6057 > 6054$, so $\lfloor 6054/2019 \rfloor = 2$.

For $p = 2017$: $\lfloor 6054/2017 \rfloor = 3$, so $v_p(z!) = 3 - 2 = 1$, $g_p(z) = 2020 \cdot 1 = 2020$. Exactly meets.

But wait, I need to also check: is the two-at-$(p-1)$ strategy actually the minimum? Could there be a worse configuration?

Let me reconsider. For $p = 2017$ and $n = 6052$:

The minimum of $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = 6052$.

$g_{2017}(k) = k \cdot v_{2017}(k!)$. $v_{2017}(k!) = 0$ for $k < 2017$, $= 1$ for $2017 \leq k < 4034$, $= 2$ for $4034 \leq k < 6051$, $= 3$ for $6051 \leq k < 8068$.

(I'm ignoring $p^2 = 2017^2 > 4 \cdot 10^6$, which is way larger than any $k$ we consider.)

So $g_{2017}(k) = 0$ for $k < 2017$, $= k$ for $2017 \leq k < 4034$, $= 2k$ for $4034 \leq k < 6051$, $= 3k$ for $6051 \leq k < 8068$.

To minimize $g(x) + g(y) + g(z)$ with $x + y + z = 6052$:

Strategy A: two at 2016, one at 2020. $g = 0 + 0 + 2020 = 2020$.
Strategy B: one at 2016, two at 2018. $g = 0 + 2018 + 2018 = 4036$.
Strategy C: one at 2016, one at 2017, one at 2019. $g = 0 + 2017 + 2019 = 4036$.
Strategy D: two at 2016, one at 2020. Same as A.
Strategy E: one at 0, one at 2016, one at 4036. $g = 0 + 0 + 2 \cdot 4036 = 8072$.
Strategy F: three at 2017.33... → 2017, 2017, 2018. $g = 2017 + 2017 + 2018 = 6052$.

So strategy A gives 2020, which is the minimum. Any strategy with two variables $< 2017$ and the third $\geq 2017$ gives $g = $ (third variable). The smallest third variable is $6052 - 2 \cdot 2016 = 2020$. So the minimum is 2020. ✓

But wait, could we do even worse with a different split? Like one at 2016, one at 4033, one at 3? $g = 0 + 4033 + 0 = 4033$. That's bigger. Or one at 4033, one at 2016, one at 3: same.

What about one at 4033, one at 2019, one at 0? $g = 4033 + 2019 + 0 = 6052$. Bigger.

What about one at 4034, one at 2016, one at 2? $g = 2 \cdot 4034 + 0 + 0 = 8068$. Bigger.

So indeed the minimum is 2020, achieved by $(2016, 2016, 2020)$ (and permutations). ✓

Now, I also need to verify that for $n = 6051$ (one less), the condition fails. With $n = 6051$ and $p = 2017$:
Two at 2016, one at $6051 - 4032 = 2019$. $g = 0 + 0 + 2019 = 2019 < 2020$. ✗

So $n = 6051$ doesn't work for $p = 2017$. Hence $n \geq 6052$.

Now I need to verify that $n = 6052$ works for ALL primes $p \leq 2020$.

Let me think about which primes could be problematic. The concern is primes where the "waste" from splitting is large relative to $M_p$.

For a prime $p$ with $v_p(2020!) = t$, $M_p = 2020t$. With $n = 6052$ and two at $p-1$:
$z = 6054 - 2p$, $v_p(z!) = \lfloor (6054 - 2p)/p \rfloor + \text{higher order}$.
$g_p(z) = (6054 - 2p) \cdot v_p(z!)$.

We need $(6054 - 2p) \cdot v_p(z!) \geq 2020t$.

But this is just one strategy. The actual minimum might be lower with a different strategy. Let me think about the actual minimum more carefully.

Actually, for the minimum, the best strategy is to put as much weight as possible on $v_p = 0$ (i.e., variables $< p$). With 3 variables and sum $n = 6052$:

- If $n \leq 3(p-1) = 3p - 3$: all three can be $< p$, min = 0. (Not relevant for $p \leq 2020$ since $3 \cdot 2019 = 6057 > 6052$, so for $p \leq 2019$, we might have $3p - 3 \geq 6052$, i.e., $p \geq 2019$... but $2019$ is not prime. For $p = 2017$: $3 \cdot 2016 = 6048 < 6052$, so not all can be $< p$.)

Wait, $3(p-1) = 3p - 3$. For $p = 2017$: $3 \cdot 2016 = 6048 < 6052$. So we can't have all three $< 2017$. Good.

For $p = 2019$ (not prime, but let's check): $3 \cdot 2018 = 6054 \geq 6052$. So all three could be $< 2019$. But 2019 is not prime, so irrelevant.

For primes $p \leq 2017$: $3(p-1) = 3p - 3 \leq 3 \cdot 2016 = 6048 < 6052$. So we can't have all three $< p$. At least one must be $\geq p$.

Now, the minimum with at least one $\geq p$: put two at $p - 1$ (contributing 0), one at $n - 2(p-1) = 6054 - 2p$. This gives $g_p(6054 - 2p)$.

But could a different split give a lower value? For instance, one at $p - 1$, one at $2p - 1$ (contributing $2p - 1$), one at $n - (p-1) - (2p-1) = n - 3p + 2 = 6054 - 3p$.

If $6054 - 3p \geq 0$ (i.e., $p \leq 2018$): $g_p(6054 - 3p)$. If $6054 - 3p < p$ (i.e., $p > 1513.5$): $g_p(6054 - 3p) = 0$ (if $6054 - 3p < p$) or $g_p(6054 - 3p) = 6054 - 3p$ (if $p \leq 6054 - 3p < 2p$).

Total: $(2p - 1) + g_p(6054 - 3p)$.

For $p = 2017$: $6054 - 3 \cdot 2017 = 6054 - 6051 = 3$. $g_p(3) = 0$. Total: $2 \cdot 2017 - 1 + 0 = 4033$. This is bigger than 2020, so strategy A is better (gives lower sum).

What about one at $p - 1$, one at $p - 1$, one at $6054 - 2p$? That's strategy A, giving $g_p(6054 - 2p)$.

For $p = 2017$: $g_p(2020) = 2020$. This is the minimum.

Could we do: one at 0, one at $p - 1$, one at $6053 - p$? $g_p(0) + g_p(p-1) + g_p(6053 - p) = 0 + 0 + g_p(6053 - p)$. For $p = 2017$: $g_p(4036) = 2 \cdot 4036 = 8072$. Bigger.

So for $p = 2017$, the minimum is indeed 2020.

Now let me check a potentially problematic prime. Consider $p$ such that $6054 - 2p$ is just above a multiple of $p$, making $v_p$ jump.

For $p = 2017$: $6054 - 4034 = 2020$. $2020 / 2017 = 1.001...$, so $v_p = 1$. $g_p = 2020$.

What if there's a prime where $6054 - 2p$ is just below a multiple of $p$? Then $v_p$ would be one less.

$6054 - 2p = mp + r$ with $0 \leq r < p$. $m = \lfloor (6054 - 2p)/p \rfloor = \lfloor 6054/p \rfloor - 2$.

For $p$ slightly less than 2017: say $p = 2011$. $6054/2011 = 3.009...$, so $m = 1$. $g_p = (6054 - 4022) \cdot 1 = 2032 \geq 2020$. ✓

For $p = 2003$: $6054/2003 = 3.022...$, $m = 1$. $g_p = (6054 - 4006) \cdot 1 = 2048 \geq 2020$. ✓

For $p$ where $m = 1$ (i.e., $\lfloor 6054/p \rfloor = 3$, i.e., $p \leq 2018$ and $p > 1513$): $g_p = (6054 - 2p) \cdot 1 = 6054 - 2p$. Need $\geq 2020$: $p \leq 2017$. So for $p = 2017$: exactly 2020. For $p \leq 2017$ (and $p > 1513$): $6054 - 2p \geq 6054 - 4034 = 2020$. ✓

But wait, what about primes $p$ with $1513 < p \leq 2017$ and $v_p(2020!) = 1$? We need $p > 1010$ for $v_p(2020!) = 1$. And for $p > 1513$: $\lfloor 6054/p \rfloor = 3$ (since $3 \cdot 1514 = 4542 \leq 6054$ and $4 \cdot 1514 = 6056 > 6054$... wait, $4 \cdot 1513 = 6052 \leq 6054$, so $\lfloor 6054/1513 \rfloor = 4$). Let me recompute.

$\lfloor 6054/p \rfloor = 3$ when $3p \leq 6054 < 4p$, i.e., $1513.5 \leq p \leq 2018$. So for primes $p$ with $1514 \leq p \leq 2017$: $\lfloor 6054/p \rfloor = 3$, $m = 1$, $g_p = 6054 - 2p \geq 6054 - 4034 = 2020$. ✓ (with equality at $p = 2017$).

For primes $p$ with $1010 < p < 1514$: $\lfloor 6054/p \rfloor \geq 4$, so $m \geq 2$, $g_p = (6054 - 2p) \cdot m \geq (6054 - 2p) \cdot 2$. And $6054 - 2p > 6054 - 3028 = 3026$, so $g_p > 6052 \geq 2020$. ✓

But wait, I also need to check that the two-at-$(p-1)$ strategy is actually the minimum for these primes. Let me verify for a prime where $v_p(2020!) = 1$ and $p$ is around 1514.

$p = 1511$ (let me check if it's prime... I'll assume it is for now). $v_p(2020!) = 1$ (since $1511 < 2020 < 2 \cdot 1511 = 3022$). $M_p = 2020$.

Two at 1510: $z = 6054 - 3022 = 3032$. $v_p(3032!) = \lfloor 3032/1511 \rfloor = 2$ (since $2 \cdot 1511 = 3022 \leq 3032 < 4533$). $g_p(z) = 3032 \cdot 2 = 6064 \geq 2020$. ✓

But is this the minimum? Could we do: one at 1510, two at 2271 (= (6052 - 1510)/2)? $g_p(2271) = 2271 \cdot 1 = 2271$ each. Total: $0 + 2271 + 2271 = 4542$. Bigger than 6064? No, $4542 < 6064$. So this is a lower sum!

Wait, that means the two-at-$(p-1)$ strategy is NOT the minimum here! Let me reconsider.

With $n = 6052$, $p = 1511$:
- Strategy A (two at 1510, one at 3032): $g = 0 + 0 + 3032 \cdot 2 = 6064$.
- Strategy B (one at 1510, two balanced at 2271): $g = 0 + 2271 \cdot 1 + 2271 \cdot 1 = 4542$.
- Strategy C (three balanced at ~2017): $g = 2017 + 2017 + 2018 = 6052$ (each has $v_p = 1$).

So strategy B gives 4542, which is less than strategy A's 6064. So the minimum is not always at two-at-$(p-1)$!

Hmm, so I need to be more careful. The minimum depends on the prime.

Let me reconsider. For $p = 1511$ and $n = 6052$:

The minimum of $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = 6052$.

$g_p(k) = 0$ for $k < 1511$, $= k$ for $1511 \leq k < 3022$, $= 2k$ for $3022 \leq k < 4533$, $= 3k$ for $4533 \leq k < 6044$, $= 4k$ for $6044 \leq k$.

To minimize, we want to maximize weight on $v_p = 0$ (i.e., $k < 1511$), then on $v_p = 1$ (i.e., $1511 \leq k < 3022$), etc.

With 3 variables summing to 6052:
- Max weight on $v_p = 0$: two variables at 1510, third at 3032. But 3032 has $v_p = 2$, so $g = 2 \cdot 3032 = 6064$.
- One variable at 1510, two at 2271 (both in $[1511, 3022)$): $g = 0 + 2271 + 2271 = 4542$.
- Zero variables $< 1511$, three at ~2017: $g = 2017 + 2017 + 2018 = 6052$.
- One at 1510, one at 1510, one at 3032: $g = 6064$ (strategy A).
- One at 0, one at 1510, one at 4542: $g = 0 + 0 + 3 \cdot 4542 = 13626$. Worse.

So the minimum is strategy B: 4542. Since $4542 \geq 2020 = M_p$, this is fine. ✓

But this shows I need to be more careful. Let me think about the general minimum.

For a prime $p$ with $v_p(2020!) = 1$ (i.e., $1010 < p \leq 2020$), $M_p = 2020$.

With $n = 6052$, the minimum of $g_p(x) + g_p(y) + g_p(z)$:

The function $g_p(k) = k \cdot v_p(k!)$, where $v_p(k!) = \lfloor k/p \rfloor$ (ignoring higher powers since $p^2 > 10^6$).

So $g_p(k) = k \lfloor k/p \rfloor$.

We want to minimize $\sum k_i \lfloor k_i/p \rfloor$ with $\sum k_i = 6052$, $k_i \geq 0$.

Write $k_i = a_i p + b_i$ with $0 \leq b_i < p$. Then $g_p(k_i) = k_i \cdot a_i = (a_i p + b_i) a_i = a_i^2 p + a_i b_i$.

$\sum k_i = p \sum a_i + \sum b_i = 6052$.

$\sum g_p(k_i) = p \sum a_i^2 + \sum a_i b_i$.

Let $A = \sum a_i$, $B = \sum b_i$. Then $pA + B = 6052$, $0 \leq B \leq 3(p-1) = 3p - 3$.

$\sum g_p(k_i) = p \sum a_i^2 + \sum a_i b_i$.

To minimize, we want to minimize $\sum a_i^2$ and $\sum a_i b_i$.

Given $A = \sum a_i$, $\sum a_i^2$ is minimized when $a_i$ are as equal as possible.

$\sum a_i b_i$: to minimize, we want $b_i$ to be small when $a_i$ is large, and large when $a_i$ is small.

This is a complex optimization. Let me think about it differently.

$A = (6052 - B)/p$. Since $0 \leq B \leq 3p - 3$:
- $A$ ranges from $\lceil (6052 - 3p + 3)/p \rceil$ to $\lfloor 6052/p \rfloor$.

For $p = 2017$: $A$ ranges from $\lceil (6052 - 6048)/2017 \rceil = \lceil 4/2017 \rceil = 1$ to $\lfloor 6052/2017 \rfloor = 2$.

Wait, $6052/2017 = 3.001...$, so $\lfloor 6052/2017 \rfloor = 3$. And $A \geq \lceil (6052 - 3 \cdot 2016)/2017 \rceil = \lceil (6052 - 6048)/2017 \rceil = \lceil 4/2017 \rceil = 1$.

So $A \in \{1, 2, 3\}$.

For $A = 1$: $\sum a_i = 1$, so one $a_i = 1$, others 0. $\sum a_i^2 = 1$. $B = 6052 - 2017 = 4035$. But $B \leq 3p - 3 = 6048$. $4035 \leq 6048$. ✓. $\sum a_i b_i = b_j$ where $j$ is the one with $a_j = 1$. To minimize, set $b_j = 0$ (so $k_j = 2017$), and $b_i = p - 1 = 2016$ for the other two. $B = 0 + 2016 + 2016 = 4032 \neq 4035$. Hmm, $B$ must be 4035 but we can only achieve $B = 4032$ with this setup. 

Wait, I need $B = 6052 - pA = 6052 - 2017 = 4035$. With $a = (1, 0, 0)$, $b_1 + b_2 + b_3 = 4035$, $0 \leq b_i < 2017$. $\sum a_i b_i = b_1$ (since $a_1 = 1$, $a_2 = a_3 = 0$). To minimize, set $b_1 = 0$, $b_2 + b_3 = 4035$. Max $b_2 + b_3 = 2 \cdot 2016 = 4032 < 4035$. Not feasible!

So $A = 1$ is not feasible for $p = 2017$. We need $B = 4035 \leq 3(p-1) = 6048$, which is true, but the constraint is that with $a = (1, 0, 0)$, we need $b_1 < p$ and $b_2, b_3 < p$, and $b_1 + b_2 + b_3 = 4035$. With $b_1 \leq 2016$ and $b_2, b_3 \leq 2016$: max $B = 3 \cdot 2016 = 6048 \geq 4035$. But we also need $k_i = a_i p + b_i \geq 0$, which is automatic.

Actually, $b_1$ can be anything from 0 to 2016. So $b_2 + b_3 = 4035 - b_1$. For this to be feasible: $0 \leq 4035 - b_1 \leq 2 \cdot 2016 = 4032$. So $b_1 \geq 3$. Then $\sum a_i b_i = b_1 \geq 3$.

$\sum g_p = p \cdot 1 + b_1 = 2017 + b_1$. Minimized at $b_1 = 3$: $g = 2020$.

So for $A = 1$, minimum is 2020. This matches our earlier calculation.

For $A = 2$: $\sum a_i = 2$. Could be $(2, 0, 0)$, $(1, 1, 0)$. $B = 6052 - 2 \cdot 2017 = 2018$.
- $(2, 0, 0)$: $\sum a_i^2 = 4$. $\sum a_i b_i = 2b_1$. $b_1 + b_2 + b_3 = 2018$, $b_1 \leq 2016$. $\sum a_i b_i = 2b_1$. Minimize: $b_1 = 0$ (if $b_2 + b_3 = 2018 \leq 4032$, yes). $g = 2017 \cdot 4 + 0 = 8068$.
- $(1, 1, 0)$: $\sum a_i^2 = 2$. $\sum a_i b_i = b_1 + b_2$. $b_1 + b_2 + b_3 = 2018$. Minimize $b_1 + b_2$: set $b_3 = 2016$ (max), $b_1 + b_2 = 2$. $g = 2017 \cdot 2 + 2 = 4036$.

For $A = 3$: $\sum a_i = 3$. $(1, 1, 1)$. $B = 6052 - 3 \cdot 2017 = 1$. $\sum a_i^2 = 3$. $\sum a_i b_i = b_1 + b_2 + b_3 = 1$. $g = 2017 \cdot 3 + 1 = 6052$.

So the overall minimum for $p = 2017$ is $\min(2020, 4036, 6052) = 2020$. ✓

Now, for a general prime $p$ with $v_p(2020!) = 1$ ($1010 < p \leq 2020$), $M_p = 2020$:

The minimum of $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = 6052$ is achieved at $A = 1$ (one variable with $a_i = 1$, two with $a_i = 0$), giving $g = p + b_1$ where $b_1 = 6052 - p - 2(p-1) = 6052 - 3p + 2 = 6054 - 3p$.

Wait, let me redo. With $A = 1$, $B = 6052 - p$. We have $a = (1, 0, 0)$, $b_1 + b_2 + b_3 = 6052 - p$, $0 \leq b_i \leq p - 1$. $\sum a_i b_i = b_1$. Minimize $b_1$: set $b_1 = \max(0, (6052 - p) - 2(p-1)) = \max(0, 6052 - 3p + 2) = \max(0, 6054 - 3p)$.

$g = p + b_1 = p + \max(0, 6054 - 3p)$.

For $p \leq 2018$: $6054 - 3p \geq 6054 - 6054 = 0$, so $b_1 = 6054 - 3p \geq 0$. $g = p + 6054 - 3p = 6054 - 2p$.

For $p = 2017$: $g = 6054 - 4034 = 2020$. ✓
For $p = 2011$: $g = 6054 - 4022 = 2032 \geq 2020$. ✓
For $p = 1511$: $g = 6054 - 3022 = 3032$. But wait, is this the minimum? We need to check $A = 2$ as well.

For $A = 2$, $p = 1511$: $B = 6052 - 3022 = 3030$. With $a = (1, 1, 0)$: $\sum a_i b_i = b_1 + b_2$. Minimize: $b_3 = 1510$, $b_1 + b_2 = 1520$. $g = 1511 \cdot 2 + 1520 = 3022 + 1520 = 4542$.

With $a = (2, 0, 0)$: $\sum a_i b_i = 2b_1$. $b_1 + b_2 + b_3 = 3030$. Min $b_1$: $b_1 = \max(0, 3030 - 3020) = 10$. $g = 1511 \cdot 4 + 20 = 6044 + 20 = 6064$.

So for $A = 2$, min is 4542. For $A = 1$, min is 3032. So overall min is 3032.

But $3032 \geq 2020$. ✓

Hmm, but I need to check: is $A = 1$ always feasible? We need $B = 6052 - p \leq 3(p-1) = 3p - 3$, i.e., $6052 \leq 4p - 3$, i.e., $p \geq 1513.75$, i.e., $p \geq 1514$.

For primes $p$ with $1010 < p < 1514$: $A = 1$ is not feasible (since $B = 6052 - p > 3p - 3$). So we need $A \geq 2$.

For $A = 2$, $p$ with $1010 < p < 1514$: $B = 6052 - 2p$. $B \leq 3p - 3$ iff $6052 \leq 5p - 3$ iff $p \geq 1211$.

For $p \geq 1211$ and $p < 1514$: $A = 2$ is feasible. Min $g$ with $A = 2$, $a = (1,1,0)$: $g = 2p + \max(0, (6052 - 2p) - 2(p-1)) = 2p + \max(0, 6054 - 4p)$.

For $p \geq 1211$: $6054 - 4p \leq 6054 - 4844 = 1210$. So $g = 2p + 6054 - 4p = 6054 - 2p$ (if $6054 - 4p > 0$, i.e., $p < 1513.5$).

For $p = 1213$ (prime): $g = 6054 - 2426 = 3628 \geq 2020$. ✓

For $p$ with $1010 < p < 1211$: $A = 2$ might not be feasible. $B = 6052 - 2p \leq 3p - 3$ iff $p \geq 1211$. So for $p < 1211$, need $A \geq 3$.

For $A = 3$, $a = (1,1,1)$: $B = 6052 - 3p$. $B \leq 3p - 3$ iff $6052 \leq 6p - 3$ iff $p \geq 1009.17$, i.e., $p \geq 1010$. So for $p \geq 1010$, $A = 3$ is feasible.

$g = 3p + B = 3p + 6052 - 3p = 6052$ (since $\sum a_i b_i = B = 6052 - 3p$ and $\sum a_i^2 = 3$).

Wait, $g = p \sum a_i^2 + \sum a_i b_i = 3p + (b_1 + b_2 + b_3) = 3p + (6052 - 3p) = 6052$.

So for $A = 3$, $g = 6052$ regardless of $p$. Since $6052 \geq 2020$, this is fine.

But we need the minimum over all $A$, so we need to check if $A = 3$ gives the minimum for $p < 1211$.

For $p = 1013$ (prime, $1010 < 1013$): $v_p(2020!) = 1$ (since $1013 < 2020 < 2026 = 2 \cdot 1013$). $M_p = 2020$.

$A = 2$: $B = 6052 - 2026 = 4026$. $B \leq 3 \cdot 1012 = 3036$? $4026 > 3036$. Not feasible.
$A = 3$: $g = 6052 \geq 2020$. ✓
$A = 4$: $a = (2, 1, 1)$, $\sum a_i^2 = 6$. $B = 6052 - 4 \cdot 1013 = 2000$. $g = 6 \cdot 1013 + \sum a_i b_i$. Min $\sum a_i b_i$: $b_1$ (with $a_1 = 2$) should be 0, $b_2 + b_3 = 2000$. $\sum a_i b_i = 0 + b_2 + b_3 = 2000$. $g = 6078 + 2000 = 8078$. Bigger than 6052.

So for $p = 1013$, min is 6052 (at $A = 3$). $6052 \geq 2020$. ✓

So for all primes $p$ with $v_p(2020!) = 1$ (i.e., $1010 < p \leq 2020$), the minimum with $n = 6052$ is $\geq 2020$, with equality at $p = 2017$.

Now I need to check primes with $v_p(2020!) \geq 2$.

For primes $p$ with $v_p(2020!) = 2$ (i.e., $673 < p \leq 1010$, since $2p \leq 2020 < 3p$): $M_p = 4040$.

With $n = 6052$, the minimum of $g_p(x) + g_p(y) + g_p(z)$:

Using the framework: $g_p(k) = k \lfloor k/p \rfloor$ (ignoring $p^2$ terms for now; I'll add them later).

$A = \sum a_i$, $B = \sum b_i$, $pA + B = 6052$.

$\sum g_p = p \sum a_i^2 + \sum a_i b_i$.

For $p = 1009$ (prime, $v_p(2020!) = 2$): $M_p = 4040$.

$A$ ranges: $B = 6052 - 1009A$, $0 \leq B \leq 3 \cdot 1008 = 3024$.
$A \geq \lceil (6052 - 3024)/1009 \rceil = \lceil 3028/1009 \rceil = 3$.
$A \leq \lfloor 6052/1009 \rfloor = 5$ (since $6 \cdot 1009 = 6054 > 6052$).

$A = 3$: $a = (1,1,1)$, $B = 6052 - 3027 = 3025$. But $B \leq 3024$. Not feasible! Wait, $3 \cdot 1008 = 3024 < 3025$. So $A = 3$ is not feasible.

$A = 4$: $B = 6052 - 4036 = 2016$. $B \leq 3024$. ✓. $a = (2, 1, 1)$: $\sum a_i^2 = 6$. $\sum a_i b_i = 2b_1 + b_2 + b_3$. Min: $b_1 = 0$, $b_2 + b_3 = 2016$. $\sum a_i b_i = 2016$. $g = 6 \cdot 1009 + 2016 = 6054 + 2016 = 8070$.

$a = (2, 2, 0)$: $\sum a_i^2 = 8$. $B = 2016$. $\sum a_i b_i = 2b_1 + 2b_2$. Min: $b_3 = 1008$ (max), $b_1 + b_2 = 1008$. $\sum a_i b_i = 2 \cdot 1008 = 2016$. $g = 8 \cdot 1009 + 2016 = 8072 + 2016 = 10088$. Bigger.

So $A = 4$, min is 8070. But we should also check higher $A$.

$A = 5$: $B = 6052 - 5045 = 1007$. $a = (2, 2, 1)$: $\sum a_i^2 = 9$. $\sum a_i b_i = 2b_1 + 2b_2 + b_3$. Min: $b_3 = 0$, $b_1 + b_2 = 1007$. $\sum a_i b_i = 2 \cdot 1007 = 2014$. $g = 9 \cdot 1009 + 2014 = 9081 + 2014 = 11095$. Bigger.

$a = (3, 1, 1)$: $\sum a_i^2 = 11$. $\sum a_i b_i = 3b_1 + b_2 + b_3$. Min: $b_1 = 0$, $b_2 + b_3 = 1007$. $\sum a_i b_i = 1007$. $g = 11 \cdot 1009 + 1007 = 11099 + 1007 = 12106$. Bigger.

So the minimum for $p = 1009$ is 8070 (at $A = 4$, $a = (2,1,1)$). $8070 \geq 4040$. ✓

But wait, I ignored the $p^2$ contribution. $v_p(k!) = \lfloor k/p \rfloor + \lfloor k/p^2 \rfloor + \cdots$. For $p = 1009$, $p^2 = 1018081 > 6052$, so $\lfloor k/p^2 \rfloor = 0$ for all $k \leq 6052$. So no correction needed. ✓

Now, for smaller primes, $v_p(2020!)$ is larger, but $g_p$ grows faster (since $v_p(k!)$ is larger for given $k$). Let me check a few.

For $p = 2$: $v_2(2020!) = 2020 - s_2(2020) = 2020 - 8 = 2012$ (where $s_2(2020)$ is the number of 1s in binary representation of 2020; $2020 = 11111100100_2$, which has 7 ones... let me recount: $2020 = 1024 + 512 + 256 + 128 + 64 + 32 + 4 = 11111100100_2$. That's 7 ones. So $v_2(2020!) = 2020 - 7 = 2013$.

Hmm, actually Legendre's formula: $v_p(n!) = (n - s_p(n))/(p-1)$. For $p = 2$: $v_2(2020!) = (2020 - s_2(2020))/1 = 2020 - s_2(2020)$.

$2020$ in binary: $2020 = 1024 + 996 = 1024 + 512 + 484 = 1024 + 512 + 256 + 228 = 1024 + 512 + 256 + 128 + 100 = 1024 + 512 + 256 + 128 + 64 + 36 = 1024 + 512 + 256 + 128 + 64 + 32 + 4 = 11111100100_2$. Count of 1s: 7. So $v_2(2020!) = 2020 - 7 = 2013$.

$M_2 = 2020 \cdot 2013 = 4066260$.

With $n = 6052$: $v_2(6052!) = 6052 - s_2(6052)$. $6052 = 4096 + 1956 = 4096 + 1024 + 932 = 4096 + 1024 + 512 + 420 = 4096 + 1024 + 512 + 256 + 164 = 4096 + 1024 + 512 + 256 + 128 + 36 = 4096 + 1024 + 512 + 256 + 128 + 32 + 4 = 1011110011100_2$. Count of 1s: 8. $v_2(6052!) = 6052 - 8 = 6044$.

$g_2(6052) = 6052 \cdot 6044 = 36586288$.

The minimum of $g_2(x) + g_2(y) + g_2(z)$ with $x + y + z = 6052$ is at most $g_2(6052) = 36586288$ (by superadditivity, the max is at one variable). The minimum is achieved by splitting.

But $M_2 = 4066260$, and even a rough lower bound: with $x = y = z = 6052/3 \approx 2017$, $g_2(2017) \approx 2017 \cdot 2004 \approx 4042068$. Three times that is $\approx 12126204 \geq 4066260$. ✓

Actually, let me be more careful. $g_2(2017) = 2017 \cdot v_2(2017!)$. $v_2(2017!) = 2017 - s_2(2017)$. $2017 = 1024 + 512 + 256 + 128 + 64 + 32 + 1 = 11111100001_2$. $s_2(2017) = 7$. $v_2(2017!) = 2010$. $g_2(2017) = 2017 \cdot 2010 = 4054170$.

With $(x, y, z) = (2017, 2017, 2018)$: $g_2(2017) + g_2(2017) + g_2(2018)$. $v_2(2018!) = 2018 - s_2(2018)$. $2018 = 2017 + 1 = 11111100010_2$. $s_2(2018) = 7$. $v_2(2018!) = 2011$. $g_2(2018) = 2018 \cdot 2011 = 4058198$.

Total: $2 \cdot 4054170 + 4058198 = 8108340 + 4058198 = 12166538 \geq 4066260$. ✓

So $p = 2$ is fine. The minimum is much larger than $M_2$.

In general, for small primes, $g_p$ grows as $k^2/(p-1)$, so with $n = 6052$ and balanced split, the sum is roughly $3 \cdot (n/3)^2 / (p-1) = n^2 / (3(p-1))$, while $M_p \approx 2020 \cdot 2020/(p-1) = 2020^2/(p-1)$. So the ratio is $n^2 / (3 \cdot 2020^2) = 6052^2 / (3 \cdot 2020^2) \approx 36627904 / 12241200 \approx 2.99$. So the minimum is roughly 3 times $M_p$ for small primes. ✓

The binding constraint is from the largest prime $\leq 2020$, which is $2017$.

Let me also check: are there primes $p$ with $v_p(2020!) = 2$ that might be binding?

For $p$ with $673 < p \leq 1010$: $v_p(2020!) = 2$, $M_p = 4040$.

The minimum of $g_p$ with $n = 6052$: using our framework, the minimum is at $A = \lceil (6052 - 3(p-1))/p \rceil$ or nearby.

For $p = 1010$ (not prime, but close): $A \geq \lceil (6052 - 3027)/1010 \rceil = \lceil 3025/1010 \rceil = 3$. $A = 3$: $B = 6052 - 3030 = 3022 \leq 3 \cdot 1009 = 3027$. ✓. $g = 3p + B = 3030 + 3022 = 6052$. But wait, with $a = (1,1,1)$, $\sum a_i b_i = B = 3022$, $g = 3 \cdot 1010 + 3022 = 6052$. Hmm, but $p = 1010$ is not prime. Let me use $p = 1009$.

For $p = 1009$: we computed min = 8070 (at $A = 4$). $8070 \geq 4040$. ✓

For $p = 677$ (prime, $v_p(2020!) = 2$ since $2 \cdot 677 = 1354 \leq 2020 < 2031 = 3 \cdot 677$): $M_p = 4040$.

$A \geq \lceil (6052 - 3 \cdot 676)/677 \rceil = \lceil (6052 - 2028)/677 \rceil = \lceil 4024/677 \rceil = 6$.
$A = 6$: $a = (2, 2, 2)$, $B = 6052 - 6 \cdot 677 = 6052 - 4062 = 1990$. $\sum a_i^2 = 12$. $\sum a_i b_i = 2(b_1 + b_2 + b_3) = 2 \cdot 1990 = 3980$. $g = 12 \cdot 677 + 3980 = 8124 + 3980 = 12104$. 

But maybe $a = (3, 2, 1)$ is better: $\sum a_i^2 = 14$. $\sum a_i b_i = 3b_1 + 2b_2 + b_3$. Min: $b_1 = 0, b_2 = 0, b_3 = 1990$. But $b_3 \leq 676$. $b_3 = 676$, $b_2 = 0$, $b_1 = 0$: $B = 676 \neq 1990$. Need $b_1 + b_2 + b_3 = 1990$ with $b_i \leq 676$. Max $B = 3 \cdot 676 = 2028 \geq 1990$. ✓. Min $\sum a_i b_i$: $b_1 = 0, b_2 = 0, b_3 = 1990$? No, $b_3 \leq 676$. So $b_3 = 676$, $b_2 + b_1 = 1314$. Min $3b_1 + 2b_2$: $b_1 = 0, b_2 = 1314$? $b_2 \leq 676$. $b_2 = 676, b_1 = 638$. $\sum a_i b_i = 3 \cdot 638 + 2 \cdot 676 + 676 = 1914 + 1352 + 676 = 3942$. $g = 14 \cdot 677 + 3942 = 9478 + 3942 = 13420$. Bigger than 12104.

$a = (4, 1, 1)$: $\sum a_i^2 = 18$. $B = 1990$. $\sum a_i b_i = 4b_1 + b_2 + b_3$. Min: $b_1 = 0, b_2 + b_3 = 1990, b_2, b_3 \leq 676$. $b_2 = 676, b_3 = 676$: $b_2 + b_3 = 1352 \neq 1990$. Need $b_1 + b_2 + b_3 = 1990$. $b_1 = 0, b_2 = 676, b_3 = 676$: sum = 1352. Need 638 more. $b_1 = 638$: $\sum a_i b_i = 4 \cdot 638 + 676 + 676 = 2552 + 1352 = 3904$. $g = 18 \cdot 677 + 3904 = 12186 + 3904 = 16090$. Bigger.

So for $p = 677$, min is around 12104 (at $A = 6$, $a = (2,2,2)$). $12104 \geq 4040$. ✓

So primes with $v_p(2020!) = 2$ are fine.

For primes with $v_p(2020!) \geq 3$ (i.e., $p \leq 673$), $M_p = 2020 \cdot v_p(2020!) \leq 2020 \cdot 2020/1 = 4080400$ (very rough). And the minimum $g_p$ sum with $n = 6052$ is roughly $6052^2/(3 \cdot 1) \approx 12208657$ (for $p = 2$), which is much larger. So these are fine.

Let me also check primes with $v_p(2020!) = 3$. These are primes $p$ with $3p \leq 2020 < 4p$, i.e., $505 \leq p \leq 673$. $M_p = 6060$.

For $p = 673$ (prime): $v_p(2020!) = 3$ (since $3 \cdot 673 = 2019 \leq 2020 < 2692 = 4 \cdot 673$). $M_p = 6060$.

$A \geq \lceil (6052 - 3 \cdot 672)/673 \rceil = \lceil (6052 - 2016)/673 \rceil = \lceil 4036/673 \rceil = 6$.
$A = 6$: $a = (2,2,2)$, $B = 6052 - 4038 = 2014$. $g = 12 \cdot 673 + 2 \cdot 2014 = 8076 + 4028 = 12104$. $12104 \geq 6060$. ✓

So all primes with $v_p \geq 3$ are fine.

Let me now also verify that $n = 6051$ fails. We showed for $p = 2017$:
$(x, y, z) = (2016, 2016, 2019)$: $g_{2017}(2016) + g_{2017}(2016) + g_{2017}(2019) = 0 + 0 + 2019 = 2019 < 2020 = M_{2017}$.

And $(a, b, c) = (2020, 0, 0)$: $f(a,b,c) = (2020!)^{2020} \cdot 1 \cdot 1$. $v_{2017}(f(a,b,c)) = 2020 \cdot v_{2017}(2020!) = 2020 \cdot 1 = 2020$.
$v_{2017}(f(x,y,z)) = 2016 \cdot 0 + 2016 \cdot 0 + 2019 \cdot 1 = 2019 < 2020$.

So $f(a,b,c) \nmid f(x,y,z)$. Hence $n = 6051$ doesn't work.

Therefore, the answer is $n = 6052$.

Wait, let me double-check the computation $6052 = 2 \cdot 2017 + 2018$. $2 \cdot 2017 = 4034$. $4034 + 2018 = 6052$. ✓

And $2018 = 2020 - 2$.        — AI历史解题过程（thinking）
#   polymath_05061         — 题目ID

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
  <problem_id>polymath_05061</problem_id>
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

For nonnegative integers \( p, q, r \), let

\[
f(p, q, r) = (p!)^{p}(q!)^{q}(r!)^{r}
\]

Compute the smallest positive integer \( n \) such that for any triples \((a, b, c)\) and \((x, y, z)\) of nonnegative integers satisfying \( a+b+c=2020 \) and \( x+y+z=n \), \( f(x, y, z) \) is divisible by \( f(a, b, c) \).

## Standard Solution

The smallest positive integer \( n \) is \( 6052 \).

\(\boxed{6052}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. I need to find the smallest positive integer n such that for any triples (a,b,c) and (x,y,z) of nonnegative integers with a+b+c=2020 and x+y+z=n, f(x,y,z) is divisible by f(a,b,c).

First, let me check for answer leaks. The problem text doesn't contain any solutions or answer values. Good.

Let me think about this problem carefully.

We have $f(p,q,r) = (p!)^p (q!)^q (r!)^r$.

We need: for ALL triples $(a,b,c)$ with $a+b+c=2020$ and ALL triples $(x,y,z)$ with $x+y+z=n$, $f(x,y,z) \mid$ is divisible by $f(a,b,c)$.

Wait, re-reading: "f(x,y,z) is divisible by f(a,b,c)" means $f(a,b,c) \mid f(x,y,z)$.

So we need: for every $(a,b,c)$ with $a+b+c=2020$ and every $(x,y,z)$ with $x+y+z=n$, $f(a,b,c) \mid f(x,y,z)$.

This means $f(x,y,z)$ must be divisible by $\text{lcm}$ over all $(a,b,c)$ with $a+b+c=2020$ of $f(a,b,c)$, for every $(x,y,z)$ with $x+y+z=n$.

So we need: for every $(x,y,z)$ with $x+y+z=n$, $f(x,y,z)$ is divisible by $L = \text{lcm}_{a+b+c=2020} f(a,b,c)$.

And we want the smallest $n$ such that this holds.

Let me think about the $p$-adic valuation. For a prime $p$, let $v_p(m)$ denote the $p$-adic valuation.

$v_p(f(a,b,c)) = a \cdot v_p(a!) + b \cdot v_p(b!) + c \cdot v_p(c!)$.

We need, for every $(x,y,z)$ with $x+y+z=n$:
$v_p(f(x,y,z)) \geq \max_{a+b+c=2020} v_p(f(a,b,c))$ for every prime $p$.

So for each prime $p$, let $M_p = \max_{a+b+c=2020} [a \cdot v_p(a!) + b \cdot v_p(b!) + c \cdot v_p(c!)]$.

And we need: for every $(x,y,z)$ with $x+y+z=n$, $x \cdot v_p(x!) + y \cdot v_p(y!) + z \cdot v_p(z!) \geq M_p$ for every prime $p$.

The smallest $n$ is the smallest $n$ such that $\min_{x+y+z=n} [x \cdot v_p(x!) + y \cdot v_p(y!) + z \cdot v_p(z!)] \geq M_p$ for all primes $p$.

Let me define $g_p(k) = k \cdot v_p(k!)$ for $k \geq 0$ (with $g_p(0) = 0$).

Then $M_p = \max_{a+b+c=2020} [g_p(a) + g_p(b) + g_p(c)]$.

And we need $\min_{x+y+z=n} [g_p(x) + g_p(y) + g_p(z)] \geq M_p$ for all primes $p$.

So the answer is $n = \max_p n_p$ where $n_p$ is the smallest $n$ such that $\min_{x+y+z=n} [g_p(x)+g_p(y)+g_p(z)] \geq M_p$.

Now, $g_p(k) = k \cdot v_p(k!)$. Note $v_p(k!) = \sum_{i=1}^{k} v_p(i) = \frac{k - s_p(k)}{p-1}$ where $s_p(k)$ is the sum of digits of $k$ in base $p$.

So $g_p(k) = k \cdot \frac{k - s_p(k)}{p-1} = \frac{k^2 - k \cdot s_p(k)}{p-1}$.

This is a complicated function. Let me think about which primes matter.

For $p > 2020$, $v_p(k!) = 0$ for $k \leq 2020$, so $g_p(k) = 0$ for all relevant $k$, and $M_p = 0$. So only primes $p \leq 2020$ matter.

Actually, for $p > 2020$, $v_p(a!) = 0$ for $a \leq 2020$, so $M_p = 0$, and the condition is trivially satisfied. So we only need primes $p \leq 2020$.

Now, the key question: for each prime $p$, what is $M_p$ and what is $n_p$?

Let me think about $M_p$ first. We want to maximize $g_p(a) + g_p(b) + g_p(c)$ subject to $a+b+c = 2020$, $a,b,c \geq 0$.

Since $g_p$ is convex (roughly quadratic), the maximum is achieved at an extreme point: one of $a,b,c$ is as large as possible. So the maximum is $g_p(2020) + g_p(0) + g_p(0) = g_p(2020) = 2020 \cdot v_p(2020!)$.

Wait, is $g_p$ convex? $g_p(k) = k \cdot v_p(k!)$. Let's check: $g_p(k+1) - g_p(k) = (k+1)v_p((k+1)!) - k \cdot v_p(k!) = (k+1)(v_p(k!) + v_p(k+1)) - k \cdot v_p(k!) = v_p(k!) + (k+1)v_p(k+1)$.

The second difference: $[g_p(k+2) - g_p(k+1)] - [g_p(k+1) - g_p(k)] = [v_p((k+1)!) + (k+2)v_p(k+2)] - [v_p(k!) + (k+1)v_p(k+1)]$
$= v_p(k+1) + (k+2)v_p(k+2) - (k+1)v_p(k+1)$
$= v_p(k+1) + (k+2)v_p(k+2) - (k+1)v_p(k+1)$
$= v_p(k+1)(1 - (k+1)) + (k+2)v_p(k+2)$
$= -k \cdot v_p(k+1) + (k+2)v_p(k+2)$.

This isn't always non-negative. For example, if $v_p(k+1) > 0$ and $v_p(k+2) = 0$, this could be negative.

So $g_p$ is not necessarily convex. Let me reconsider.

Actually, let me think more carefully. The function $g_p(k) = k \cdot v_p(k!)$. 

Let me compute $g_p$ for small values to get intuition. Take $p=2$:
- $g_2(0) = 0$
- $g_2(1) = 1 \cdot 0 = 0$
- $g_2(2) = 2 \cdot 1 = 2$
- $g_2(3) = 3 \cdot 1 = 3$
- $g_2(4) = 4 \cdot 3 = 12$
- $g_2(5) = 5 \cdot 3 = 15$
- $g_2(6) = 6 \cdot 4 = 24$
- $g_2(7) = 7 \cdot 4 = 28$
- $g_2(8) = 8 \cdot 7 = 56$

The differences: 0, 2, 1, 9, 3, 9, 4, 28. These are not monotone, so $g_p$ is not convex.

So maximizing $g_p(a) + g_p(b) + g_p(c)$ with $a+b+c=2020$ is not simply putting everything in one variable.

Hmm, this is more complex. Let me think about this differently.

Actually, let me reconsider the structure. We have $g_p(k) = k \cdot v_p(k!)$. 

Note that $v_p(k!)$ counts the number of factors of $p$ in $k!$. And $k \cdot v_p(k!)$ is like summing $v_p(j)$ for each $j$ from 1 to $k$, but multiplied by $k$. Actually:

$g_p(k) = k \cdot \sum_{j=1}^{k} v_p(j) = \sum_{j=1}^{k} k \cdot v_p(j)$.

Alternatively, $g_p(k) = \sum_{j=1}^{k} \sum_{i=1}^{k} v_p(j) = \sum_{i=1}^{k}\sum_{j=1}^{k} v_p(j)$... no that's $k \cdot \sum v_p(j)$ which is the same.

Hmm, let me think of it as $g_p(k) = \sum_{j=1}^{k} v_p(j) \cdot k$. 

Actually, let me think about it differently. $g_p(k) = k \cdot v_p(k!)$. Consider the sum $g_p(a) + g_p(b) + g_p(c)$ where $a+b+c = N = 2020$.

$g_p(a) + g_p(b) + g_p(c) = a \cdot v_p(a!) + b \cdot v_p(b!) + c \cdot v_p(c!)$.

Let me think about what configuration maximizes this. 

Consider the contribution of each factor of $p$ in the factorials. $v_p(a!) = \sum_{j \geq 1} \lfloor a/p^j \rfloor$. So:

$g_p(a) = a \sum_{j \geq 1} \lfloor a/p^j \rfloor$.

For a fixed $j$, the contribution to $g_p(a) + g_p(b) + g_p(c)$ from the $j$-th term is:
$a \lfloor a/p^j \rfloor + b \lfloor b/p^j \rfloor + c \lfloor c/p^j \rfloor$.

Now, $h(x) = x \lfloor x/p^j \rfloor$ is a step function. For $x$ in $[mp^j, (m+1)p^j)$, $h(x) = mx$. This is increasing in $x$ (for fixed $m$), and jumps up at multiples of $p^j$.

To maximize $\sum h(a_i)$ with $\sum a_i = N$, since $h$ is "superadditive-ish" (concave pieces with jumps), the maximum tends to be at extreme points. Let me think...

Actually, $h(x) = x \lfloor x/q \rfloor$ where $q = p^j$. Write $x = mq + r$ with $0 \leq r < q$. Then $h(x) = mx = m(mq+r) = m^2 q + mr$.

Consider two variables $x, y$ with $x + y = S$. Write $x = mq + r$, $y = m'q + r'$. We want to compare $h(x) + h(y)$ vs $h(x+y) + h(0) = h(S)$.

$h(x) + h(y) = m^2 q + mr + m'^2 q + m'r$.
$h(S) = h(x+y)$. Let $S = Mq + R$. Then $h(S) = M(Mq + R) = M^2 q + MR$.

Since $M = m + m' + \lfloor (r+r')/q \rfloor$ and $R = (r + r') \mod q$.

If $r + r' < q$: $M = m + m'$, $R = r + r'$.
$h(S) = (m+m')^2 q + (m+m')(r+r') = (m^2 + 2mm' + m'^2)q + mr + mr' + m'r + m'r'$.
$h(x) + h(y) = (m^2 + m'^2)q + mr + m'r'$.
$h(S) - (h(x)+h(y)) = 2mm'q + mr' + m'r \geq 0$.

So $h(S) \geq h(x) + h(y)$ when $r + r' < q$. This means concentrating is better!

If $r + r' \geq q$: $M = m + m' + 1$, $R = r + r' - q$.
$h(S) = (m+m'+1)((m+m'+1)q + r+r'-q) = (m+m'+1)(m+m')q + (m+m'+1)(r+r'-q)$.
$= (m+m'+1)(m+m')q + (m+m'+1)(r+r') - (m+m'+1)q$
$= (m+m')(m+m'+1)q + (m+m'+1)(r+r') - (m+m'+1)q$
$= (m+m')((m+m'+1)-1)q + (m+m'+1)(r+r') - (m+m'+1)q$

Hmm, this is getting messy. Let me just compute:
$h(S) = M^2 q + MR = (m+m'+1)^2 q + (m+m'+1)(r+r'-q)$.

$h(x)+h(y) = (m^2+m'^2)q + mr + m'r'$.

$h(S) - (h(x)+h(y)) = [(m+m'+1)^2 - m^2 - m'^2]q + (m+m'+1)(r+r'-q) - mr - m'r'$
$= [2mm' + 2m + 2m' + 1]q + (m+m'+1)(r+r') - (m+m'+1)q - mr - m'r'$
$= [2mm' + 2m + 2m' + 1 - m - m' - 1]q + (m+m'+1)(r+r') - mr - m'r'$
$= [2mm' + m + m']q + (m+m'+1)(r+r') - mr - m'r'$
$= [2mm' + m + m']q + mr + m'r' + r + r' + mr' + m'r - mr - m'r'$
Wait, let me redo: $(m+m'+1)(r+r') = mr + mr' + m'r + m'r' + r + r'$.
So $(m+m'+1)(r+r') - mr - m'r' = mr' + m'r + r + r'$.

$h(S) - (h(x)+h(y)) = (2mm' + m + m')q + mr' + m'r + r + r'$.

Since $r + r' \geq q$ (in this case), and all terms are non-negative, this is $\geq (2mm'+m+m')q + q = (2mm' + m + m' + 1)q > 0$.

So in both cases, $h(S) \geq h(x) + h(y)$, with equality only when $m = m' = 0$ and $r + r' < q$ (i.e., both $x, y < q$ and $x + y < q$).

This means $h(x) = x\lfloor x/q \rfloor$ is superadditive! So $h(a) + h(b) + h(c) \leq h(a+b+c) = h(N)$.

Therefore, for each $j$, $a\lfloor a/p^j \rfloor + b\lfloor b/p^j \rfloor + c\lfloor c/p^j \rfloor \leq N \lfloor N/p^j \rfloor$ where $N = 2020$.

Summing over $j$: $g_p(a) + g_p(b) + g_p(c) \leq g_p(N) = g_p(2020)$.

So $M_p = g_p(2020) = 2020 \cdot v_p(2020!)$, achieved by $(a,b,c) = (2020, 0, 0)$.

Great, so $M_p = 2020 \cdot v_p(2020!)$ for each prime $p$.

Now, we need: for every $(x,y,z)$ with $x+y+z = n$, $g_p(x) + g_p(y) + g_p(z) \geq M_p = g_p(2020)$ for all primes $p$.

So we need: $\min_{x+y+z=n} [g_p(x) + g_p(y) + g_p(z)] \geq g_p(2020)$ for all primes $p \leq 2020$.

And we want the smallest such $n$.

Now, by the superadditivity we proved, $g_p(x) + g_p(y) + g_p(z) \leq g_p(n)$. So we need $g_p(n) \geq g_p(2020)$, which means $n \geq 2020$ (since $g_p$ is increasing for $p \leq n$... well, $g_p$ is non-decreasing).

But we need the minimum over all triples to be $\geq g_p(2020)$, not just the maximum. So $n$ must be large enough that even the worst-case triple gives enough.

The worst case for $g_p(x) + g_p(y) + g_p(z)$ with $x+y+z=n$ is when the values are as "spread out" as possible in a way that minimizes the sum. Since $g_p$ is superadditive, the minimum of $g_p(x)+g_p(y)+g_p(z)$ with $x+y+z=n$ is achieved when... hmm, superadditivity means $g_p(x)+g_p(y) \leq g_p(x+y)$, so splitting decreases the sum. So the minimum is achieved by splitting as much as possible.

Wait, but we have exactly 3 parts. So the minimum of $g_p(x)+g_p(y)+g_p(z)$ with $x+y+z=n$, $x,y,z \geq 0$ is achieved by making the split as balanced as possible? Or as unbalanced as possible?

Since $g_p$ is superadditive, $g_p(x) + g_p(y) \leq g_p(x+y)$. So to minimize, we want to split. With 3 parts, the most split is $\lfloor n/3 \rfloor, \lfloor n/3 \rfloor, n - 2\lfloor n/3 \rfloor$ or something like that. But actually, superadditivity just says splitting into 2 reduces, and splitting into 3 reduces more. But the exact minimum depends on the structure of $g_p$.

Hmm wait, actually superadditivity says $g_p(a) + g_p(b) \leq g_p(a+b)$. So $g_p(x) + g_p(y) + g_p(z) \leq g_p(x+y) + g_p(z) \leq g_p(x+y+z) = g_p(n)$. The minimum is when we split the most.

But with 3 variables, the "most split" would be roughly equal: $x \approx y \approx z \approx n/3$. But is that right? Let me think again.

Actually, superadditivity means that merging increases the sum. So to minimize, we want to avoid merging, i.e., split as evenly as possible. But the exact minimum depends on $g_p$'s structure.

Actually, let me reconsider. We want to minimize $g_p(x) + g_p(y) + g_p(z)$ subject to $x+y+z = n$. 

Since $g_p$ is superadditive, we know the minimum is at most $g_p(n)$ (achieved by $(n,0,0)$... wait no, that gives $g_p(n) + 0 + 0 = g_p(n)$, which is the maximum by superadditivity). The minimum is achieved by splitting.

Let me think about what splitting does. If we split $n$ into $x$ and $n-x$, the sum changes from $g_p(n)$ to $g_p(x) + g_p(n-x)$. By superadditivity, this is $\leq g_p(n)$. The "loss" is $g_p(n) - g_p(x) - g_p(n-x)$.

To minimize the total, we want to maximize the total loss from splitting. 

Let me think about this more carefully for specific primes.

For large primes $p$ (say $p > n/3$), $v_p(k!) = 0$ for $k < p$ and $v_p(k!) = 1$ for $p \leq k < 2p$, etc. So $g_p(k) = k \cdot v_p(k!) = 0$ for $k < p$, $g_p(k) = k$ for $p \leq k < 2p$, $g_p(k) = 2k$ for $2p \leq k < 3p$, etc.

For $p > 2020$ but $p \leq n$: $g_p(2020) = 0$ (since $2020 < p$). So $M_p = 0$, and the condition is trivially satisfied. Good.

For primes $p$ with $1010 < p \leq 2020$: $v_p(2020!) = 1$ (since $2020 < 2p$ as $p > 1010$). So $g_p(2020) = 2020$.

We need $\min_{x+y+z=n} [g_p(x) + g_p(y) + g_p(z)] \geq 2020$.

For such $p$, $g_p(k) = 0$ if $k < p$, $g_p(k) = k$ if $p \leq k < 2p$, etc.

If $n < 3p$, then we can have at most 2 of $x,y,z$ be $\geq p$. The minimum sum would be achieved by having as few variables $\geq p$ as possible.

If $n \geq 3p$: all three can be $\geq p$, and $g_p(x)+g_p(y)+g_p(z) \geq x+y+z = n$ (if all are $\geq p$ and $< 2p$). But we need to check if we can have all three $< p$: that requires $n < 3p$, i.e., $n \leq 3p - 1$.

If $n < 3p$, we can choose $x = y = z = \lfloor n/3 \rfloor < p$ (if $n/3 < p$), giving $g_p = 0$ for each, total 0 < 2020. So we need $n \geq 3p$.

Wait, but if $n \geq 3p$, can we still have all three $< p$? No, because $x + y + z = n \geq 3p$ and $x, y, z < p$ gives $x+y+z < 3p$, contradiction. So at least one is $\geq p$.

But we need the minimum to be $\geq 2020$. If $n = 3p$, the minimum is achieved at $x = y = z = p$, giving $g_p(p) + g_p(p) + g_p(p) = 3p$. We need $3p \geq 2020$, i.e., $p \geq 674$. But we're considering $p > 1010$, so $3p > 3030 > 2020$. 

But wait, can we do worse? With $n = 3p$, can we have $x = 0, y = 0, z = 3p$? Then $g_p(0) + g_p(0) + g_p(3p) = 3 \cdot 3p = 9p$ (since $v_p((3p)!) = 3$). That's bigger. The minimum at $n = 3p$ is at $x=y=z=p$: $3p$.

Hmm, but actually we could also try $x = p-1, y = p-1, z = p+2$. Then $g_p(p-1) + g_p(p-1) + g_p(p+2) = 0 + 0 + (p+2) = p+2$. That's less than $3p$!

Wait, $p + 2 < 3p$ for $p > 1$. So the minimum is not at $x = y = z = p$.

Let me reconsider. With $n = 3p$, we want to minimize $g_p(x) + g_p(y) + g_p(z)$. We can have two variables just below $p$ (so $g_p = 0$) and one variable $= n - 2(p-1) = 3p - 2p + 2 = p + 2$. Then $g_p(p+2) = p+2$ (since $v_p((p+2)!) = 1$ as $p+2 < 2p$ for $p > 2$).

So the minimum is $p + 2$, not $3p$. We need $p + 2 \geq 2020$, i.e., $p \geq 2018$.

But we're considering primes $p$ with $1010 < p \leq 2020$. The largest such prime is $2017$. For $p = 2017$: $n = 3 \cdot 2017 = 6051$, minimum is $2017 + 2 = 2019 < 2020$. Not enough!

So we need $n > 3p$ for $p = 2017$. Let's figure out the exact requirement.

For a prime $p$ with $1010 < p \leq 2020$, $g_p(2020) = 2020$. We need $\min_{x+y+z=n} [g_p(x)+g_p(y)+g_p(z)] \geq 2020$.

$g_p(k) = k \cdot v_p(k!)$. For $k < p$: $g_p(k) = 0$. For $p \leq k < 2p$: $g_p(k) = k$. For $2p \leq k < 3p$: $g_p(k) = 2k$. Etc.

To minimize $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = n$:
- We want as many variables as possible to be $< p$ (contributing 0).
- At most 2 can be $< p$ (since if all 3 are $< p$, sum $< 3p$).
- If 2 are $< p$ (say $x, y < p$, $x + y \leq 2(p-1) = 2p - 2$), then $z = n - x - y \geq n - 2p + 2$.
  - To minimize, set $x = y = p - 1$ (maximizing $x + y$ to minimize $z$'s contribution... wait, we want to minimize $g_p(z)$, and $g_p(z) = z \cdot v_p(z!)$. If $z < 2p$, $g_p(z) = z$. If $z \geq 2p$, $g_p(z) = 2z$ or more.
  
  Actually, we want to minimize $g_p(z)$. With $z = n - 2(p-1) = n - 2p + 2$:
  - If $z < p$: $g_p(z) = 0$. But $z = n - 2p + 2 < p$ means $n < 3p - 2$. Then all three can be $< p$, and the min is 0. Not useful.
  - If $p \leq z < 2p$: $g_p(z) = z = n - 2p + 2$. This is the case when $3p - 2 \leq n < 4p - 2$.
  - If $2p \leq z < 3p$: $g_p(z) = 2z = 2(n - 2p + 2)$. But maybe it's better to have one of $x, y$ be $\geq p$ instead.

Let me think more carefully. We want to minimize $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = n$.

Case 1: All three $< p$. Requires $n \leq 3(p-1) = 3p - 3$. Sum = 0.

Case 2: Exactly one $\geq p$. Say $z \geq p$, $x, y < p$. Then $x + y \leq 2p - 2$, $z = n - x - y \geq n - 2p + 2$.
- To minimize $g_p(z)$, we want $z$ as small as possible (if $g_p$ is increasing, which it is for $z \geq p$). So set $x + y = 2p - 2$, $z = n - 2p + 2$.
- If $z < 2p$ (i.e., $n < 4p - 2$): $g_p(z) = z = n - 2p + 2$.
- If $2p \leq z < 3p$ (i.e., $4p - 2 \leq n < 5p - 2$): $g_p(z) = 2z = 2(n-2p+2)$.
  - But maybe better to have 2 variables $\geq p$. Let's check.

Case 3: Exactly two $\geq p$. Say $y, z \geq p$, $x < p$. $x \leq p-1$, $y + z = n - x \geq n - p + 1$.
- To minimize $g_p(y) + g_p(z)$, by superadditivity, we want $y, z$ as equal as possible? No, superadditivity says $g_p(y) + g_p(z) \leq g_p(y+z)$, so splitting reduces. So we want $y, z$ as split as possible, i.e., as equal as possible.
- Set $x = p - 1$, $y = z = (n - p + 1)/2$ (if even) or close to it.
- If $y, z < 2p$ (i.e., $(n-p+1)/2 < 2p$, i.e., $n < 5p - 1$): $g_p(y) + g_p(z) = y + z = n - p + 1$.
  - Compare with Case 2: $n - 2p + 2$ vs $n - p + 1$. Case 2 is smaller by $p - 1$. So Case 2 is better.

Case 4: All three $\geq p$. Requires $n \geq 3p$. 
- $g_p(x) + g_p(y) + g_p(z) \geq x + y + z = n$ (if all $< 2p$). This is worse than Case 2.

So the minimum is achieved in Case 2: two variables at $p-1$, one at $n - 2p + 2$, giving $g_p = n - 2p + 2$ (when $p \leq n - 2p + 2 < 2p$, i.e., $3p - 2 \leq n \leq 4p - 3$).

Wait, but I should also consider the case where $z \geq 2p$ in Case 2, and compare with Case 3.

For $n \geq 4p - 2$ (so $z \geq 2p$ in Case 2):
- Case 2: $g_p(z) = 2z = 2(n - 2p + 2)$ (if $z < 3p$, i.e., $n < 5p - 2$).
- Case 3: $g_p(y) + g_p(z) = (n - p + 1)$ (if both $< 2p$, i.e., $n < 5p - 1$).
- Case 2 gives $2n - 4p + 4$, Case 3 gives $n - p + 1$.
- Case 3 < Case 2 iff $n - p + 1 < 2n - 4p + 4$ iff $3p < n + 3$ iff $n > 3p - 3$.
- Since $n \geq 4p - 2 > 3p - 3$, Case 3 is better.

So for $n \geq 4p - 2$, Case 3 is better. In Case 3 with $y, z < 2p$:
- $g_p(y) + g_p(z) = y + z = n - p + 1$ (with $x = p - 1$).
- This requires $y, z \geq p$ and $y, z < 2p$, so $n - p + 1 \geq 2p$ (i.e., $n \geq 3p - 1$) and $(n-p+1)/2 < 2p$ (i.e., $n < 5p - 1$).

For $n \geq 5p - 1$, we'd need to consider further cases. But let me also check: in Case 3, if one of $y, z \geq 2p$:
- Set $x = p-1$, $y = p$, $z = n - 2p + 1$. If $z \geq 2p$ (i.e., $n \geq 4p - 1$): $g_p(y) + g_p(z) = p + 2z = p + 2(n - 2p + 1) = 2n - 3p + 2$.
- Compare with balanced: $n - p + 1$. $n - p + 1 < 2n - 3p + 2$ iff $2p < n + 1$ iff $n > 2p - 1$. True for $n \geq 4p - 1$. So balanced is better.

OK so to summarize for a prime $p$ with $1010 < p \leq 2020$ (so $v_p(2020!) = 1$, $M_p = 2020$):

The minimum of $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = n$ is:
- $0$ if $n \leq 3p - 3$ (all three $< p$)
- $n - 2p + 2$ if $3p - 2 \leq n \leq 4p - 3$ (two at $p-1$, one at $n-2p+2 < 2p$)
- $n - p + 1$ if $4p - 2 \leq n \leq 5p - 2$ (one at $p-1$, two balanced, both $< 2p$)
- ... and so on for larger $n$.

We need this minimum $\geq 2020$.

For the range $3p - 2 \leq n \leq 4p - 3$: need $n - 2p + 2 \geq 2020$, i.e., $n \geq 2p + 2018$.
For the range $4p - 2 \leq n \leq 5p - 2$: need $n - p + 1 \geq 2020$, i.e., $n \geq p + 2019$.

The binding constraint is the first range: $n \geq 2p + 2018$ (and this must be in the range $[3p-2, 4p-3]$, i.e., $2p + 2018 \leq 4p - 3$, i.e., $p \geq 1010.5$, i.e., $p \geq 1011$). Since we're considering $p > 1010$, this works.

But we also need $2p + 2018 \geq 3p - 2$, i.e., $p \leq 2020$. Which is true.

So for prime $p$ with $1010 < p \leq 2020$: $n_p = 2p + 2018$.

The largest such prime is $2017$. So $n_{2017} = 2 \cdot 2017 + 2018 = 4034 + 2018 = 6052$.

Wait, let me double-check. For $p = 2017$: $n_p = 2 \cdot 2017 + 2018 = 6052$. And we need $3p - 2 \leq n_p \leq 4p - 3$: $3 \cdot 2017 - 2 = 6049 \leq 6052 \leq 4 \cdot 2017 - 3 = 8065$. Yes, $6049 \leq 6052 \leq 8065$. ✓

So for $p = 2017$, we need $n \geq 6052$.

Now let me check other primes. For primes $p$ with $673 < p \leq 1010$ (so $v_p(2020!) = 2$, since $2p \leq 2020 < 3p$): $M_p = 2020 \cdot 2 = 4040$.

Hmm wait, $v_p(2020!) = \lfloor 2020/p \rfloor + \lfloor 2020/p^2 \rfloor + \cdots$. For $p > 673$: $\lfloor 2020/p \rfloor = 2$ (since $2p \leq 2020 < 3p$ when $p \leq 1010$ and $p > 673$), and $\lfloor 2020/p^2 \rfloor = 0$ (since $p^2 > 673^2 > 2020$). So $v_p(2020!) = 2$, $M_p = 4040$.

For such $p$, $g_p(k) = k \cdot v_p(k!)$. $v_p(k!) = 0$ for $k < p$, $= 1$ for $p \leq k < 2p$, $= 2$ for $2p \leq k < 3p$.

We need $\min_{x+y+z=n} [g_p(x)+g_p(y)+g_p(z)] \geq 4040$.

Using the same analysis:
- Case 2 (two at $p-1$, one at $z = n - 2p + 2$):
  - If $p \leq z < 2p$: $g_p(z) = z = n - 2p + 2$. Need $\geq 4040$, so $n \geq 2p + 4038$.
  - Check range: $3p - 2 \leq n \leq 4p - 3$, so $2p + 4038 \leq 4p - 3$ iff $p \geq 2020.5$. But $p \leq 1010$, so this doesn't work! The required $n$ is outside this range.

So for $p$ in this range, we need to go to higher cases.

- Case 3 (one at $p-1$, two balanced, both in $[p, 2p)$):
  - $g_p = y + z = n - p + 1$. Need $\geq 4040$, so $n \geq p + 4039$.
  - Range: $4p - 2 \leq n \leq 5p - 2$ (need both $y, z < 2p$). Actually, the range for this case is when $n - p + 1 \geq 2p$ and $(n-p+1)/2 < 2p$, i.e., $n \geq 3p - 1$ and $n < 5p - 1$.
  - Need $p + 4039 \leq 5p - 2$, i.e., $p \geq 1010.25$, i.e., $p \geq 1011$. But $p \leq 1010$, so again outside range!

Hmm. Let me continue to higher cases.

- Case with one at $p-1$, one at $p$, one at $z = n - 2p + 1$:
  - If $2p \leq z < 3p$: $g_p(z) = 2z = 2(n - 2p + 1)$. Total: $p + 2(n - 2p + 1) = 2n - 3p + 2$.
  - Need $2n - 3p + 2 \geq 4040$, i.e., $n \geq (3p + 4038)/2$.
  - Range: $z \geq 2p$ means $n \geq 4p - 1$. $z < 3p$ means $n < 5p - 1$.
  
  Actually wait, I need to be more careful. Let me reconsider.

Let me think about this differently. For a general prime $p$ with $v_p(2020!) = t$ (so $M_p = 2020t$), I need to find the minimum $n$ such that $\min_{x+y+z=n} \sum g_p(x_i) \geq 2020t$.

The function $g_p(k) = k \cdot v_p(k!)$. For $k$ in $[mp, (m+1)p)$, $v_p(k!) = m + v_p(k! \text{ restricted to higher powers})$... actually this is getting complicated because of higher powers of $p$.

Let me simplify by first considering only the contribution from $\lfloor k/p \rfloor$ (the first term in Legendre's formula), and then add corrections for higher powers.

Actually, let me think about this problem from a higher level. The answer is likely determined by the largest prime $\leq 2020$, which is $2017$. Let me check if $n = 6052$ works for all primes.

For $p = 2017$: we showed $n_{2017} = 6052$. Let me verify: with $n = 6052$, the minimum of $g_{2017}(x) + g_{2017}(y) + g_{2017}(z)$ is $6052 - 2 \cdot 2017 + 2 = 6052 - 4034 + 2 = 2020 = M_{2017}$. ✓ (achieved by $(2016, 2016, 2020)$, where $g_{2017}(2016) = 0$, $g_{2017}(2016) = 0$, $g_{2017}(2020) = 2020 \cdot 1 = 2020$).

Now I need to check all other primes $p \leq 2020$ to see if $n = 6052$ suffices.

For a prime $p$, let $t = v_p(2020!)$. We need $\min_{x+y+z=6052} [g_p(x) + g_p(y) + g_p(z)] \geq 2020t$.

The minimum is achieved by making two variables as close to $p-1$ as possible (to have $g_p = 0$) and the third taking the rest. But actually, the optimal strategy to minimize depends on $p$.

Let me think about it. With $n = 6052$, for a prime $p$, the minimum of $g_p(x) + g_p(y) + g_p(z)$ is achieved by:
- Setting two variables to $p - 1$ (so $g_p = 0$ for those), and the third to $n - 2(p-1) = n - 2p + 2$.
- Or some other configuration.

But actually, the minimum might be achieved by a different configuration. Let me think about what minimizes $g_p(x) + g_p(y) + g_p(z)$.

Since $g_p$ is superadditive, splitting reduces the sum. So we want to split as much as possible. But the "splits" that reduce the most are those that cross the "steps" of $g_p$ (i.e., multiples of $p$).

The key insight: $g_p(k) = k \cdot v_p(k!)$. The function $v_p(k!)$ is a step function that increases by 1 at each multiple of $p$, by 1 at each multiple of $p^2$, etc. So $g_p(k)$ has a "kink" at each multiple of $p$.

To minimize $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = n$, we want to "waste" as much as possible just below multiples of $p$ (where $g_p$ is relatively low compared to the linear growth).

The optimal strategy: put two variables just below $p$ (at $p - 1$), and the third takes the rest. This is because the "loss" from superadditivity is maximized when we split at the first step.

Actually, I realize the minimum might not always be two at $p-1$. Let me think more carefully.

For $g_p(k) = k \cdot v_p(k!)$, the function is 0 for $k < p$, then $k$ for $p \leq k < 2p$, then $2k$ for $2p \leq k < 3p$ (ignoring higher powers of $p$ for now), etc.

The "efficiency" $g_p(k)/k = v_p(k!)$ is a step function: 0, 1, 2, 3, ... To minimize $g_p(x) + g_p(y) + g_p(z) = \sum x_i v_p(x_i!)$, we want to minimize the weighted average of $v_p(x_i!)$ with weights $x_i$. So we want as much weight as possible on low $v_p$ values.

The best is to have weight on $v_p = 0$ (i.e., $x_i < p$), but we can have at most 2 variables $< p$ (since $n = 6052$ is large). With 2 variables $< p$ (at $p - 1$ each), the third is $n - 2(p-1) = n - 2p + 2$.

But we could also have 1 variable $< p$ (at $p - 1$) and 2 variables in $[p, 2p)$. The total would be $(p-1) \cdot 0 + y \cdot 1 + z \cdot 1 = y + z = n - p + 1$ (if both in $[p, 2p)$).

Compare: $n - 2p + 2$ (two at $p-1$) vs $n - p + 1$ (one at $p-1$, two in $[p, 2p)$). The first is smaller by $p - 1$. So two at $p-1$ is better, as long as the third variable's $v_p$ doesn't jump too much.

With two at $p-1$, the third is $z = n - 2p + 2$. Its $v_p(z!) = \lfloor z/p \rfloor + \lfloor z/p^2 \rfloor + \cdots$.

$g_p(z) = z \cdot v_p(z!)$.

So the minimum (with this strategy) is $g_p(n - 2p + 2)$.

But is this always the minimum? Could there be a better strategy, like two at $2p - 1$ (with $v_p = 1$) and one taking the rest?

With two at $2p - 1$: $g_p(2p-1) = (2p-1) \cdot 1 = 2p - 1$ each. Third is $n - 2(2p-1) = n - 4p + 2$.
Total: $2(2p-1) + g_p(n - 4p + 2) = 4p - 2 + g_p(n - 4p + 2)$.

Compare with two at $p - 1$: $g_p(n - 2p + 2)$.

For the two-at-$p-1$ strategy: if $z = n - 2p + 2$ is in $[mp, (m+1)p)$, then $g_p(z) = z \cdot (m + \text{higher order terms})$.

For the two-at-$2p-1$ strategy: the third is $n - 4p + 2$, which is smaller, so its $v_p$ might be lower.

This is getting complicated. Let me just compute numerically for the key primes.

Actually, let me step back and think about which primes could be binding. The answer is $n = 6052$ (from $p = 2017$) if all other primes give $n_p \leq 6052$.

For small primes (like $p = 2, 3, 5, \ldots$), $v_p(2020!)$ is large, but $g_p$ grows fast (roughly $k^2/(p-1)$), so the minimum with $n = 6052$ should easily exceed $M_p$.

The critical primes are the large ones, where $v_p(2020!)$ is small (1 or 2) and the "waste" from splitting is significant.

Let me check primes near $1010$ (where $v_p(2020!) = 2$).

For $p = 1009$ (prime, $1009 \cdot 2 = 2018 \leq 2020 < 3027 = 3 \cdot 1009$): $v_p(2020!) = 2$, $M_p = 4040$.

With $n = 6052$, two at $p - 1 = 1008$: $z = 6052 - 2016 = 4036$. $v_{1009}(4036!) = \lfloor 4036/1009 \rfloor + \lfloor 4036/1009^2 \rfloor = 4 + 0 = 4$. So $g_p(z) = 4036 \cdot 4 = 16144 \geq 4040$. ✓

So for $p = 1009$, $n = 6052$ is more than enough.

Let me check $p = 2011$ (prime, $v_p(2020!) = 1$, $M_p = 2020$):
Two at $2010$: $z = 6052 - 4020 = 2032$. $v_{2011}(2032!) = \lfloor 2032/2011 \rfloor = 1$. $g_p(z) = 2032 \cdot 1 = 2032 \geq 2020$. ✓

$p = 2017$: $z = 6052 - 4032 = 2020$. $v_{2017}(2020!) = 1$. $g_p(z) = 2020 \cdot 1 = 2020 = M_p$. ✓ (exactly meets the bound)

$p = 2020$ is not prime. What about primes just below 2017?

$p = 2011$: checked, ✓.
$p = 2017$: exactly meets. ✓.

What about primes between 2017 and 2020? There are none (2018, 2019, 2020 are not prime).

Now let me check: is there a prime $p$ with $v_p(2020!) = 1$ (i.e., $1010 < p \leq 2020$) where $n = 6052$ doesn't work?

For such $p$, two at $p-1$: $z = 6052 - 2(p-1) = 6052 - 2p + 2 = 6054 - 2p$.
$v_p(z!) = \lfloor z/p \rfloor = \lfloor (6054 - 2p)/p \rfloor = \lfloor 6054/p - 2 \rfloor = \lfloor 6054/p \rfloor - 2$.

$g_p(z) = z \cdot v_p(z!) = (6054 - 2p)(\lfloor 6054/p \rfloor - 2)$.

We need this $\geq 2020$.

For $p = 2017$: $\lfloor 6054/2017 \rfloor = 3$. $g_p(z) = (6054 - 4034)(3 - 2) = 2020 \cdot 1 = 2020$. ✓

For $p = 2011$: $\lfloor 6054/2011 \rfloor = 3$. $g_p(z) = (6054 - 4022)(3-2) = 2032 \cdot 1 = 2032 \geq 2020$. ✓

For general $p$ with $1010 < p \leq 2020$: $\lfloor 6054/p \rfloor \geq \lfloor 6054/2020 \rfloor = 2$. Hmm, for $p = 2020$... but 2020 is not prime. For $p = 2017$: $\lfloor 6054/2017 \rfloor = 3$ (since $3 \cdot 2017 = 6051 \leq 6054$). For $p = 2019$ (not prime). For $p$ slightly larger than $2018$: $\lfloor 6054/p \rfloor = 2$ (since $2p > 4036$ and $3p > 6054$ for $p > 2018$).

Wait, $3 \cdot 2017 = 6051 \leq 6054$, so $\lfloor 6054/2017 \rfloor = 3$. But $3 \cdot 2018 = 6054$, so $\lfloor 6054/2018 \rfloor = 3$. And $3 \cdot 2019 = 6057 > 6054$, so $\lfloor 6054/2019 \rfloor = 2$.

For $p = 2017$: $\lfloor 6054/2017 \rfloor = 3$, so $v_p(z!) = 3 - 2 = 1$, $g_p(z) = 2020 \cdot 1 = 2020$. Exactly meets.

But wait, I need to also check: is the two-at-$(p-1)$ strategy actually the minimum? Could there be a worse configuration?

Let me reconsider. For $p = 2017$ and $n = 6052$:

The minimum of $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = 6052$.

$g_{2017}(k) = k \cdot v_{2017}(k!)$. $v_{2017}(k!) = 0$ for $k < 2017$, $= 1$ for $2017 \leq k < 4034$, $= 2$ for $4034 \leq k < 6051$, $= 3$ for $6051 \leq k < 8068$.

(I'm ignoring $p^2 = 2017^2 > 4 \cdot 10^6$, which is way larger than any $k$ we consider.)

So $g_{2017}(k) = 0$ for $k < 2017$, $= k$ for $2017 \leq k < 4034$, $= 2k$ for $4034 \leq k < 6051$, $= 3k$ for $6051 \leq k < 8068$.

To minimize $g(x) + g(y) + g(z)$ with $x + y + z = 6052$:

Strategy A: two at 2016, one at 2020. $g = 0 + 0 + 2020 = 2020$.
Strategy B: one at 2016, two at 2018. $g = 0 + 2018 + 2018 = 4036$.
Strategy C: one at 2016, one at 2017, one at 2019. $g = 0 + 2017 + 2019 = 4036$.
Strategy D: two at 2016, one at 2020. Same as A.
Strategy E: one at 0, one at 2016, one at 4036. $g = 0 + 0 + 2 \cdot 4036 = 8072$.
Strategy F: three at 2017.33... → 2017, 2017, 2018. $g = 2017 + 2017 + 2018 = 6052$.

So strategy A gives 2020, which is the minimum. Any strategy with two variables $< 2017$ and the third $\geq 2017$ gives $g = $ (third variable). The smallest third variable is $6052 - 2 \cdot 2016 = 2020$. So the minimum is 2020. ✓

But wait, could we do even worse with a different split? Like one at 2016, one at 4033, one at 3? $g = 0 + 4033 + 0 = 4033$. That's bigger. Or one at 4033, one at 2016, one at 3: same.

What about one at 4033, one at 2019, one at 0? $g = 4033 + 2019 + 0 = 6052$. Bigger.

What about one at 4034, one at 2016, one at 2? $g = 2 \cdot 4034 + 0 + 0 = 8068$. Bigger.

So indeed the minimum is 2020, achieved by $(2016, 2016, 2020)$ (and permutations). ✓

Now, I also need to verify that for $n = 6051$ (one less), the condition fails. With $n = 6051$ and $p = 2017$:
Two at 2016, one at $6051 - 4032 = 2019$. $g = 0 + 0 + 2019 = 2019 < 2020$. ✗

So $n = 6051$ doesn't work for $p = 2017$. Hence $n \geq 6052$.

Now I need to verify that $n = 6052$ works for ALL primes $p \leq 2020$.

Let me think about which primes could be problematic. The concern is primes where the "waste" from splitting is large relative to $M_p$.

For a prime $p$ with $v_p(2020!) = t$, $M_p = 2020t$. With $n = 6052$ and two at $p-1$:
$z = 6054 - 2p$, $v_p(z!) = \lfloor (6054 - 2p)/p \rfloor + \text{higher order}$.
$g_p(z) = (6054 - 2p) \cdot v_p(z!)$.

We need $(6054 - 2p) \cdot v_p(z!) \geq 2020t$.

But this is just one strategy. The actual minimum might be lower with a different strategy. Let me think about the actual minimum more carefully.

Actually, for the minimum, the best strategy is to put as much weight as possible on $v_p = 0$ (i.e., variables $< p$). With 3 variables and sum $n = 6052$:

- If $n \leq 3(p-1) = 3p - 3$: all three can be $< p$, min = 0. (Not relevant for $p \leq 2020$ since $3 \cdot 2019 = 6057 > 6052$, so for $p \leq 2019$, we might have $3p - 3 \geq 6052$, i.e., $p \geq 2019$... but $2019$ is not prime. For $p = 2017$: $3 \cdot 2016 = 6048 < 6052$, so not all can be $< p$.)

Wait, $3(p-1) = 3p - 3$. For $p = 2017$: $3 \cdot 2016 = 6048 < 6052$. So we can't have all three $< 2017$. Good.

For $p = 2019$ (not prime, but let's check): $3 \cdot 2018 = 6054 \geq 6052$. So all three could be $< 2019$. But 2019 is not prime, so irrelevant.

For primes $p \leq 2017$: $3(p-1) = 3p - 3 \leq 3 \cdot 2016 = 6048 < 6052$. So we can't have all three $< p$. At least one must be $\geq p$.

Now, the minimum with at least one $\geq p$: put two at $p - 1$ (contributing 0), one at $n - 2(p-1) = 6054 - 2p$. This gives $g_p(6054 - 2p)$.

But could a different split give a lower value? For instance, one at $p - 1$, one at $2p - 1$ (contributing $2p - 1$), one at $n - (p-1) - (2p-1) = n - 3p + 2 = 6054 - 3p$.

If $6054 - 3p \geq 0$ (i.e., $p \leq 2018$): $g_p(6054 - 3p)$. If $6054 - 3p < p$ (i.e., $p > 1513.5$): $g_p(6054 - 3p) = 0$ (if $6054 - 3p < p$) or $g_p(6054 - 3p) = 6054 - 3p$ (if $p \leq 6054 - 3p < 2p$).

Total: $(2p - 1) + g_p(6054 - 3p)$.

For $p = 2017$: $6054 - 3 \cdot 2017 = 6054 - 6051 = 3$. $g_p(3) = 0$. Total: $2 \cdot 2017 - 1 + 0 = 4033$. This is bigger than 2020, so strategy A is better (gives lower sum).

What about one at $p - 1$, one at $p - 1$, one at $6054 - 2p$? That's strategy A, giving $g_p(6054 - 2p)$.

For $p = 2017$: $g_p(2020) = 2020$. This is the minimum.

Could we do: one at 0, one at $p - 1$, one at $6053 - p$? $g_p(0) + g_p(p-1) + g_p(6053 - p) = 0 + 0 + g_p(6053 - p)$. For $p = 2017$: $g_p(4036) = 2 \cdot 4036 = 8072$. Bigger.

So for $p = 2017$, the minimum is indeed 2020.

Now let me check a potentially problematic prime. Consider $p$ such that $6054 - 2p$ is just above a multiple of $p$, making $v_p$ jump.

For $p = 2017$: $6054 - 4034 = 2020$. $2020 / 2017 = 1.001...$, so $v_p = 1$. $g_p = 2020$.

What if there's a prime where $6054 - 2p$ is just below a multiple of $p$? Then $v_p$ would be one less.

$6054 - 2p = mp + r$ with $0 \leq r < p$. $m = \lfloor (6054 - 2p)/p \rfloor = \lfloor 6054/p \rfloor - 2$.

For $p$ slightly less than 2017: say $p = 2011$. $6054/2011 = 3.009...$, so $m = 1$. $g_p = (6054 - 4022) \cdot 1 = 2032 \geq 2020$. ✓

For $p = 2003$: $6054/2003 = 3.022...$, $m = 1$. $g_p = (6054 - 4006) \cdot 1 = 2048 \geq 2020$. ✓

For $p$ where $m = 1$ (i.e., $\lfloor 6054/p \rfloor = 3$, i.e., $p \leq 2018$ and $p > 1513$): $g_p = (6054 - 2p) \cdot 1 = 6054 - 2p$. Need $\geq 2020$: $p \leq 2017$. So for $p = 2017$: exactly 2020. For $p \leq 2017$ (and $p > 1513$): $6054 - 2p \geq 6054 - 4034 = 2020$. ✓

But wait, what about primes $p$ with $1513 < p \leq 2017$ and $v_p(2020!) = 1$? We need $p > 1010$ for $v_p(2020!) = 1$. And for $p > 1513$: $\lfloor 6054/p \rfloor = 3$ (since $3 \cdot 1514 = 4542 \leq 6054$ and $4 \cdot 1514 = 6056 > 6054$... wait, $4 \cdot 1513 = 6052 \leq 6054$, so $\lfloor 6054/1513 \rfloor = 4$). Let me recompute.

$\lfloor 6054/p \rfloor = 3$ when $3p \leq 6054 < 4p$, i.e., $1513.5 \leq p \leq 2018$. So for primes $p$ with $1514 \leq p \leq 2017$: $\lfloor 6054/p \rfloor = 3$, $m = 1$, $g_p = 6054 - 2p \geq 6054 - 4034 = 2020$. ✓ (with equality at $p = 2017$).

For primes $p$ with $1010 < p < 1514$: $\lfloor 6054/p \rfloor \geq 4$, so $m \geq 2$, $g_p = (6054 - 2p) \cdot m \geq (6054 - 2p) \cdot 2$. And $6054 - 2p > 6054 - 3028 = 3026$, so $g_p > 6052 \geq 2020$. ✓

But wait, I also need to check that the two-at-$(p-1)$ strategy is actually the minimum for these primes. Let me verify for a prime where $v_p(2020!) = 1$ and $p$ is around 1514.

$p = 1511$ (let me check if it's prime... I'll assume it is for now). $v_p(2020!) = 1$ (since $1511 < 2020 < 2 \cdot 1511 = 3022$). $M_p = 2020$.

Two at 1510: $z = 6054 - 3022 = 3032$. $v_p(3032!) = \lfloor 3032/1511 \rfloor = 2$ (since $2 \cdot 1511 = 3022 \leq 3032 < 4533$). $g_p(z) = 3032 \cdot 2 = 6064 \geq 2020$. ✓

But is this the minimum? Could we do: one at 1510, two at 2271 (= (6052 - 1510)/2)? $g_p(2271) = 2271 \cdot 1 = 2271$ each. Total: $0 + 2271 + 2271 = 4542$. Bigger than 6064? No, $4542 < 6064$. So this is a lower sum!

Wait, that means the two-at-$(p-1)$ strategy is NOT the minimum here! Let me reconsider.

With $n = 6052$, $p = 1511$:
- Strategy A (two at 1510, one at 3032): $g = 0 + 0 + 3032 \cdot 2 = 6064$.
- Strategy B (one at 1510, two balanced at 2271): $g = 0 + 2271 \cdot 1 + 2271 \cdot 1 = 4542$.
- Strategy C (three balanced at ~2017): $g = 2017 + 2017 + 2018 = 6052$ (each has $v_p = 1$).

So strategy B gives 4542, which is less than strategy A's 6064. So the minimum is not always at two-at-$(p-1)$!

Hmm, so I need to be more careful. The minimum depends on the prime.

Let me reconsider. For $p = 1511$ and $n = 6052$:

The minimum of $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = 6052$.

$g_p(k) = 0$ for $k < 1511$, $= k$ for $1511 \leq k < 3022$, $= 2k$ for $3022 \leq k < 4533$, $= 3k$ for $4533 \leq k < 6044$, $= 4k$ for $6044 \leq k$.

To minimize, we want to maximize weight on $v_p = 0$ (i.e., $k < 1511$), then on $v_p = 1$ (i.e., $1511 \leq k < 3022$), etc.

With 3 variables summing to 6052:
- Max weight on $v_p = 0$: two variables at 1510, third at 3032. But 3032 has $v_p = 2$, so $g = 2 \cdot 3032 = 6064$.
- One variable at 1510, two at 2271 (both in $[1511, 3022)$): $g = 0 + 2271 + 2271 = 4542$.
- Zero variables $< 1511$, three at ~2017: $g = 2017 + 2017 + 2018 = 6052$.
- One at 1510, one at 1510, one at 3032: $g = 6064$ (strategy A).
- One at 0, one at 1510, one at 4542: $g = 0 + 0 + 3 \cdot 4542 = 13626$. Worse.

So the minimum is strategy B: 4542. Since $4542 \geq 2020 = M_p$, this is fine. ✓

But this shows I need to be more careful. Let me think about the general minimum.

For a prime $p$ with $v_p(2020!) = 1$ (i.e., $1010 < p \leq 2020$), $M_p = 2020$.

With $n = 6052$, the minimum of $g_p(x) + g_p(y) + g_p(z)$:

The function $g_p(k) = k \cdot v_p(k!)$, where $v_p(k!) = \lfloor k/p \rfloor$ (ignoring higher powers since $p^2 > 10^6$).

So $g_p(k) = k \lfloor k/p \rfloor$.

We want to minimize $\sum k_i \lfloor k_i/p \rfloor$ with $\sum k_i = 6052$, $k_i \geq 0$.

Write $k_i = a_i p + b_i$ with $0 \leq b_i < p$. Then $g_p(k_i) = k_i \cdot a_i = (a_i p + b_i) a_i = a_i^2 p + a_i b_i$.

$\sum k_i = p \sum a_i + \sum b_i = 6052$.

$\sum g_p(k_i) = p \sum a_i^2 + \sum a_i b_i$.

Let $A = \sum a_i$, $B = \sum b_i$. Then $pA + B = 6052$, $0 \leq B \leq 3(p-1) = 3p - 3$.

$\sum g_p(k_i) = p \sum a_i^2 + \sum a_i b_i$.

To minimize, we want to minimize $\sum a_i^2$ and $\sum a_i b_i$.

Given $A = \sum a_i$, $\sum a_i^2$ is minimized when $a_i$ are as equal as possible.

$\sum a_i b_i$: to minimize, we want $b_i$ to be small when $a_i$ is large, and large when $a_i$ is small.

This is a complex optimization. Let me think about it differently.

$A = (6052 - B)/p$. Since $0 \leq B \leq 3p - 3$:
- $A$ ranges from $\lceil (6052 - 3p + 3)/p \rceil$ to $\lfloor 6052/p \rfloor$.

For $p = 2017$: $A$ ranges from $\lceil (6052 - 6048)/2017 \rceil = \lceil 4/2017 \rceil = 1$ to $\lfloor 6052/2017 \rfloor = 2$.

Wait, $6052/2017 = 3.001...$, so $\lfloor 6052/2017 \rfloor = 3$. And $A \geq \lceil (6052 - 3 \cdot 2016)/2017 \rceil = \lceil (6052 - 6048)/2017 \rceil = \lceil 4/2017 \rceil = 1$.

So $A \in \{1, 2, 3\}$.

For $A = 1$: $\sum a_i = 1$, so one $a_i = 1$, others 0. $\sum a_i^2 = 1$. $B = 6052 - 2017 = 4035$. But $B \leq 3p - 3 = 6048$. $4035 \leq 6048$. ✓. $\sum a_i b_i = b_j$ where $j$ is the one with $a_j = 1$. To minimize, set $b_j = 0$ (so $k_j = 2017$), and $b_i = p - 1 = 2016$ for the other two. $B = 0 + 2016 + 2016 = 4032 \neq 4035$. Hmm, $B$ must be 4035 but we can only achieve $B = 4032$ with this setup. 

Wait, I need $B = 6052 - pA = 6052 - 2017 = 4035$. With $a = (1, 0, 0)$, $b_1 + b_2 + b_3 = 4035$, $0 \leq b_i < 2017$. $\sum a_i b_i = b_1$ (since $a_1 = 1$, $a_2 = a_3 = 0$). To minimize, set $b_1 = 0$, $b_2 + b_3 = 4035$. Max $b_2 + b_3 = 2 \cdot 2016 = 4032 < 4035$. Not feasible!

So $A = 1$ is not feasible for $p = 2017$. We need $B = 4035 \leq 3(p-1) = 6048$, which is true, but the constraint is that with $a = (1, 0, 0)$, we need $b_1 < p$ and $b_2, b_3 < p$, and $b_1 + b_2 + b_3 = 4035$. With $b_1 \leq 2016$ and $b_2, b_3 \leq 2016$: max $B = 3 \cdot 2016 = 6048 \geq 4035$. But we also need $k_i = a_i p + b_i \geq 0$, which is automatic.

Actually, $b_1$ can be anything from 0 to 2016. So $b_2 + b_3 = 4035 - b_1$. For this to be feasible: $0 \leq 4035 - b_1 \leq 2 \cdot 2016 = 4032$. So $b_1 \geq 3$. Then $\sum a_i b_i = b_1 \geq 3$.

$\sum g_p = p \cdot 1 + b_1 = 2017 + b_1$. Minimized at $b_1 = 3$: $g = 2020$.

So for $A = 1$, minimum is 2020. This matches our earlier calculation.

For $A = 2$: $\sum a_i = 2$. Could be $(2, 0, 0)$, $(1, 1, 0)$. $B = 6052 - 2 \cdot 2017 = 2018$.
- $(2, 0, 0)$: $\sum a_i^2 = 4$. $\sum a_i b_i = 2b_1$. $b_1 + b_2 + b_3 = 2018$, $b_1 \leq 2016$. $\sum a_i b_i = 2b_1$. Minimize: $b_1 = 0$ (if $b_2 + b_3 = 2018 \leq 4032$, yes). $g = 2017 \cdot 4 + 0 = 8068$.
- $(1, 1, 0)$: $\sum a_i^2 = 2$. $\sum a_i b_i = b_1 + b_2$. $b_1 + b_2 + b_3 = 2018$. Minimize $b_1 + b_2$: set $b_3 = 2016$ (max), $b_1 + b_2 = 2$. $g = 2017 \cdot 2 + 2 = 4036$.

For $A = 3$: $\sum a_i = 3$. $(1, 1, 1)$. $B = 6052 - 3 \cdot 2017 = 1$. $\sum a_i^2 = 3$. $\sum a_i b_i = b_1 + b_2 + b_3 = 1$. $g = 2017 \cdot 3 + 1 = 6052$.

So the overall minimum for $p = 2017$ is $\min(2020, 4036, 6052) = 2020$. ✓

Now, for a general prime $p$ with $v_p(2020!) = 1$ ($1010 < p \leq 2020$), $M_p = 2020$:

The minimum of $g_p(x) + g_p(y) + g_p(z)$ with $x + y + z = 6052$ is achieved at $A = 1$ (one variable with $a_i = 1$, two with $a_i = 0$), giving $g = p + b_1$ where $b_1 = 6052 - p - 2(p-1) = 6052 - 3p + 2 = 6054 - 3p$.

Wait, let me redo. With $A = 1$, $B = 6052 - p$. We have $a = (1, 0, 0)$, $b_1 + b_2 + b_3 = 6052 - p$, $0 \leq b_i \leq p - 1$. $\sum a_i b_i = b_1$. Minimize $b_1$: set $b_1 = \max(0, (6052 - p) - 2(p-1)) = \max(0, 6052 - 3p + 2) = \max(0, 6054 - 3p)$.

$g = p + b_1 = p + \max(0, 6054 - 3p)$.

For $p \leq 2018$: $6054 - 3p \geq 6054 - 6054 = 0$, so $b_1 = 6054 - 3p \geq 0$. $g = p + 6054 - 3p = 6054 - 2p$.

For $p = 2017$: $g = 6054 - 4034 = 2020$. ✓
For $p = 2011$: $g = 6054 - 4022 = 2032 \geq 2020$. ✓
For $p = 1511$: $g = 6054 - 3022 = 3032$. But wait, is this the minimum? We need to check $A = 2$ as well.

For $A = 2$, $p = 1511$: $B = 6052 - 3022 = 3030$. With $a = (1, 1, 0)$: $\sum a_i b_i = b_1 + b_2$. Minimize: $b_3 = 1510$, $b_1 + b_2 = 1520$. $g = 1511 \cdot 2 + 1520 = 3022 + 1520 = 4542$.

With $a = (2, 0, 0)$: $\sum a_i b_i = 2b_1$. $b_1 + b_2 + b_3 = 3030$. Min $b_1$: $b_1 = \max(0, 3030 - 3020) = 10$. $g = 1511 \cdot 4 + 20 = 6044 + 20 = 6064$.

So for $A = 2$, min is 4542. For $A = 1$, min is 3032. So overall min is 3032.

But $3032 \geq 2020$. ✓

Hmm, but I need to check: is $A = 1$ always feasible? We need $B = 6052 - p \leq 3(p-1) = 3p - 3$, i.e., $6052 \leq 4p - 3$, i.e., $p \geq 1513.75$, i.e., $p \geq 1514$.

For primes $p$ with $1010 < p < 1514$: $A = 1$ is not feasible (since $B = 6052 - p > 3p - 3$). So we need $A \geq 2$.

For $A = 2$, $p$ with $1010 < p < 1514$: $B = 6052 - 2p$. $B \leq 3p - 3$ iff $6052 \leq 5p - 3$ iff $p \geq 1211$.

For $p \geq 1211$ and $p < 1514$: $A = 2$ is feasible. Min $g$ with $A = 2$, $a = (1,1,0)$: $g = 2p + \max(0, (6052 - 2p) - 2(p-1)) = 2p + \max(0, 6054 - 4p)$.

For $p \geq 1211$: $6054 - 4p \leq 6054 - 4844 = 1210$. So $g = 2p + 6054 - 4p = 6054 - 2p$ (if $6054 - 4p > 0$, i.e., $p < 1513.5$).

For $p = 1213$ (prime): $g = 6054 - 2426 = 3628 \geq 2020$. ✓

For $p$ with $1010 < p < 1211$: $A = 2$ might not be feasible. $B = 6052 - 2p \leq 3p - 3$ iff $p \geq 1211$. So for $p < 1211$, need $A \geq 3$.

For $A = 3$, $a = (1,1,1)$: $B = 6052 - 3p$. $B \leq 3p - 3$ iff $6052 \leq 6p - 3$ iff $p \geq 1009.17$, i.e., $p \geq 1010$. So for $p \geq 1010$, $A = 3$ is feasible.

$g = 3p + B = 3p + 6052 - 3p = 6052$ (since $\sum a_i b_i = B = 6052 - 3p$ and $\sum a_i^2 = 3$).

Wait, $g = p \sum a_i^2 + \sum a_i b_i = 3p + (b_1 + b_2 + b_3) = 3p + (6052 - 3p) = 6052$.

So for $A = 3$, $g = 6052$ regardless of $p$. Since $6052 \geq 2020$, this is fine.

But we need the minimum over all $A$, so we need to check if $A = 3$ gives the minimum for $p < 1211$.

For $p = 1013$ (prime, $1010 < 1013$): $v_p(2020!) = 1$ (since $1013 < 2020 < 2026 = 2 \cdot 1013$). $M_p = 2020$.

$A = 2$: $B = 6052 - 2026 = 4026$. $B \leq 3 \cdot 1012 = 3036$? $4026 > 3036$. Not feasible.
$A = 3$: $g = 6052 \geq 2020$. ✓
$A = 4$: $a = (2, 1, 1)$, $\sum a_i^2 = 6$. $B = 6052 - 4 \cdot 1013 = 2000$. $g = 6 \cdot 1013 + \sum a_i b_i$. Min $\sum a_i b_i$: $b_1$ (with $a_1 = 2$) should be 0, $b_2 + b_3 = 2000$. $\sum a_i b_i = 0 + b_2 + b_3 = 2000$. $g = 6078 + 2000 = 8078$. Bigger than 6052.

So for $p = 1013$, min is 6052 (at $A = 3$). $6052 \geq 2020$. ✓

So for all primes $p$ with $v_p(2020!) = 1$ (i.e., $1010 < p \leq 2020$), the minimum with $n = 6052$ is $\geq 2020$, with equality at $p = 2017$.

Now I need to check primes with $v_p(2020!) \geq 2$.

For primes $p$ with $v_p(2020!) = 2$ (i.e., $673 < p \leq 1010$, since $2p \leq 2020 < 3p$): $M_p = 4040$.

With $n = 6052$, the minimum of $g_p(x) + g_p(y) + g_p(z)$:

Using the framework: $g_p(k) = k \lfloor k/p \rfloor$ (ignoring $p^2$ terms for now; I'll add them later).

$A = \sum a_i$, $B = \sum b_i$, $pA + B = 6052$.

$\sum g_p = p \sum a_i^2 + \sum a_i b_i$.

For $p = 1009$ (prime, $v_p(2020!) = 2$): $M_p = 4040$.

$A$ ranges: $B = 6052 - 1009A$, $0 \leq B \leq 3 \cdot 1008 = 3024$.
$A \geq \lceil (6052 - 3024)/1009 \rceil = \lceil 3028/1009 \rceil = 3$.
$A \leq \lfloor 6052/1009 \rfloor = 5$ (since $6 \cdot 1009 = 6054 > 6052$).

$A = 3$: $a = (1,1,1)$, $B = 6052 - 3027 = 3025$. But $B \leq 3024$. Not feasible! Wait, $3 \cdot 1008 = 3024 < 3025$. So $A = 3$ is not feasible.

$A = 4$: $B = 6052 - 4036 = 2016$. $B \leq 3024$. ✓. $a = (2, 1, 1)$: $\sum a_i^2 = 6$. $\sum a_i b_i = 2b_1 + b_2 + b_3$. Min: $b_1 = 0$, $b_2 + b_3 = 2016$. $\sum a_i b_i = 2016$. $g = 6 \cdot 1009 + 2016 = 6054 + 2016 = 8070$.

$a = (2, 2, 0)$: $\sum a_i^2 = 8$. $B = 2016$. $\sum a_i b_i = 2b_1 + 2b_2$. Min: $b_3 = 1008$ (max), $b_1 + b_2 = 1008$. $\sum a_i b_i = 2 \cdot 1008 = 2016$. $g = 8 \cdot 1009 + 2016 = 8072 + 2016 = 10088$. Bigger.

So $A = 4$, min is 8070. But we should also check higher $A$.

$A = 5$: $B = 6052 - 5045 = 1007$. $a = (2, 2, 1)$: $\sum a_i^2 = 9$. $\sum a_i b_i = 2b_1 + 2b_2 + b_3$. Min: $b_3 = 0$, $b_1 + b_2 = 1007$. $\sum a_i b_i = 2 \cdot 1007 = 2014$. $g = 9 \cdot 1009 + 2014 = 9081 + 2014 = 11095$. Bigger.

$a = (3, 1, 1)$: $\sum a_i^2 = 11$. $\sum a_i b_i = 3b_1 + b_2 + b_3$. Min: $b_1 = 0$, $b_2 + b_3 = 1007$. $\sum a_i b_i = 1007$. $g = 11 \cdot 1009 + 1007 = 11099 + 1007 = 12106$. Bigger.

So the minimum for $p = 1009$ is 8070 (at $A = 4$, $a = (2,1,1)$). $8070 \geq 4040$. ✓

But wait, I ignored the $p^2$ contribution. $v_p(k!) = \lfloor k/p \rfloor + \lfloor k/p^2 \rfloor + \cdots$. For $p = 1009$, $p^2 = 1018081 > 6052$, so $\lfloor k/p^2 \rfloor = 0$ for all $k \leq 6052$. So no correction needed. ✓

Now, for smaller primes, $v_p(2020!)$ is larger, but $g_p$ grows faster (since $v_p(k!)$ is larger for given $k$). Let me check a few.

For $p = 2$: $v_2(2020!) = 2020 - s_2(2020) = 2020 - 8 = 2012$ (where $s_2(2020)$ is the number of 1s in binary representation of 2020; $2020 = 11111100100_2$, which has 7 ones... let me recount: $2020 = 1024 + 512 + 256 + 128 + 64 + 32 + 4 = 11111100100_2$. That's 7 ones. So $v_2(2020!) = 2020 - 7 = 2013$.

Hmm, actually Legendre's formula: $v_p(n!) = (n - s_p(n))/(p-1)$. For $p = 2$: $v_2(2020!) = (2020 - s_2(2020))/1 = 2020 - s_2(2020)$.

$2020$ in binary: $2020 = 1024 + 996 = 1024 + 512 + 484 = 1024 + 512 + 256 + 228 = 1024 + 512 + 256 + 128 + 100 = 1024 + 512 + 256 + 128 + 64 + 36 = 1024 + 512 + 256 + 128 + 64 + 32 + 4 = 11111100100_2$. Count of 1s: 7. So $v_2(2020!) = 2020 - 7 = 2013$.

$M_2 = 2020 \cdot 2013 = 4066260$.

With $n = 6052$: $v_2(6052!) = 6052 - s_2(6052)$. $6052 = 4096 + 1956 = 4096 + 1024 + 932 = 4096 + 1024 + 512 + 420 = 4096 + 1024 + 512 + 256 + 164 = 4096 + 1024 + 512 + 256 + 128 + 36 = 4096 + 1024 + 512 + 256 + 128 + 32 + 4 = 1011110011100_2$. Count of 1s: 8. $v_2(6052!) = 6052 - 8 = 6044$.

$g_2(6052) = 6052 \cdot 6044 = 36586288$.

The minimum of $g_2(x) + g_2(y) + g_2(z)$ with $x + y + z = 6052$ is at most $g_2(6052) = 36586288$ (by superadditivity, the max is at one variable). The minimum is achieved by splitting.

But $M_2 = 4066260$, and even a rough lower bound: with $x = y = z = 6052/3 \approx 2017$, $g_2(2017) \approx 2017 \cdot 2004 \approx 4042068$. Three times that is $\approx 12126204 \geq 4066260$. ✓

Actually, let me be more careful. $g_2(2017) = 2017 \cdot v_2(2017!)$. $v_2(2017!) = 2017 - s_2(2017)$. $2017 = 1024 + 512 + 256 + 128 + 64 + 32 + 1 = 11111100001_2$. $s_2(2017) = 7$. $v_2(2017!) = 2010$. $g_2(2017) = 2017 \cdot 2010 = 4054170$.

With $(x, y, z) = (2017, 2017, 2018)$: $g_2(2017) + g_2(2017) + g_2(2018)$. $v_2(2018!) = 2018 - s_2(2018)$. $2018 = 2017 + 1 = 11111100010_2$. $s_2(2018) = 7$. $v_2(2018!) = 2011$. $g_2(2018) = 2018 \cdot 2011 = 4058198$.

Total: $2 \cdot 4054170 + 4058198 = 8108340 + 4058198 = 12166538 \geq 4066260$. ✓

So $p = 2$ is fine. The minimum is much larger than $M_2$.

In general, for small primes, $g_p$ grows as $k^2/(p-1)$, so with $n = 6052$ and balanced split, the sum is roughly $3 \cdot (n/3)^2 / (p-1) = n^2 / (3(p-1))$, while $M_p \approx 2020 \cdot 2020/(p-1) = 2020^2/(p-1)$. So the ratio is $n^2 / (3 \cdot 2020^2) = 6052^2 / (3 \cdot 2020^2) \approx 36627904 / 12241200 \approx 2.99$. So the minimum is roughly 3 times $M_p$ for small primes. ✓

The binding constraint is from the largest prime $\leq 2020$, which is $2017$.

Let me also check: are there primes $p$ with $v_p(2020!) = 2$ that might be binding?

For $p$ with $673 < p \leq 1010$: $v_p(2020!) = 2$, $M_p = 4040$.

The minimum of $g_p$ with $n = 6052$: using our framework, the minimum is at $A = \lceil (6052 - 3(p-1))/p \rceil$ or nearby.

For $p = 1010$ (not prime, but close): $A \geq \lceil (6052 - 3027)/1010 \rceil = \lceil 3025/1010 \rceil = 3$. $A = 3$: $B = 6052 - 3030 = 3022 \leq 3 \cdot 1009 = 3027$. ✓. $g = 3p + B = 3030 + 3022 = 6052$. But wait, with $a = (1,1,1)$, $\sum a_i b_i = B = 3022$, $g = 3 \cdot 1010 + 3022 = 6052$. Hmm, but $p = 1010$ is not prime. Let me use $p = 1009$.

For $p = 1009$: we computed min = 8070 (at $A = 4$). $8070 \geq 4040$. ✓

For $p = 677$ (prime, $v_p(2020!) = 2$ since $2 \cdot 677 = 1354 \leq 2020 < 2031 = 3 \cdot 677$): $M_p = 4040$.

$A \geq \lceil (6052 - 3 \cdot 676)/677 \rceil = \lceil (6052 - 2028)/677 \rceil = \lceil 4024/677 \rceil = 6$.
$A = 6$: $a = (2, 2, 2)$, $B = 6052 - 6 \cdot 677 = 6052 - 4062 = 1990$. $\sum a_i^2 = 12$. $\sum a_i b_i = 2(b_1 + b_2 + b_3) = 2 \cdot 1990 = 3980$. $g = 12 \cdot 677 + 3980 = 8124 + 3980 = 12104$. 

But maybe $a = (3, 2, 1)$ is better: $\sum a_i^2 = 14$. $\sum a_i b_i = 3b_1 + 2b_2 + b_3$. Min: $b_1 = 0, b_2 = 0, b_3 = 1990$. But $b_3 \leq 676$. $b_3 = 676$, $b_2 = 0$, $b_1 = 0$: $B = 676 \neq 1990$. Need $b_1 + b_2 + b_3 = 1990$ with $b_i \leq 676$. Max $B = 3 \cdot 676 = 2028 \geq 1990$. ✓. Min $\sum a_i b_i$: $b_1 = 0, b_2 = 0, b_3 = 1990$? No, $b_3 \leq 676$. So $b_3 = 676$, $b_2 + b_1 = 1314$. Min $3b_1 + 2b_2$: $b_1 = 0, b_2 = 1314$? $b_2 \leq 676$. $b_2 = 676, b_1 = 638$. $\sum a_i b_i = 3 \cdot 638 + 2 \cdot 676 + 676 = 1914 + 1352 + 676 = 3942$. $g = 14 \cdot 677 + 3942 = 9478 + 3942 = 13420$. Bigger than 12104.

$a = (4, 1, 1)$: $\sum a_i^2 = 18$. $B = 1990$. $\sum a_i b_i = 4b_1 + b_2 + b_3$. Min: $b_1 = 0, b_2 + b_3 = 1990, b_2, b_3 \leq 676$. $b_2 = 676, b_3 = 676$: $b_2 + b_3 = 1352 \neq 1990$. Need $b_1 + b_2 + b_3 = 1990$. $b_1 = 0, b_2 = 676, b_3 = 676$: sum = 1352. Need 638 more. $b_1 = 638$: $\sum a_i b_i = 4 \cdot 638 + 676 + 676 = 2552 + 1352 = 3904$. $g = 18 \cdot 677 + 3904 = 12186 + 3904 = 16090$. Bigger.

So for $p = 677$, min is around 12104 (at $A = 6$, $a = (2,2,2)$). $12104 \geq 4040$. ✓

So primes with $v_p(2020!) = 2$ are fine.

For primes with $v_p(2020!) \geq 3$ (i.e., $p \leq 673$), $M_p = 2020 \cdot v_p(2020!) \leq 2020 \cdot 2020/1 = 4080400$ (very rough). And the minimum $g_p$ sum with $n = 6052$ is roughly $6052^2/(3 \cdot 1) \approx 12208657$ (for $p = 2$), which is much larger. So these are fine.

Let me also check primes with $v_p(2020!) = 3$. These are primes $p$ with $3p \leq 2020 < 4p$, i.e., $505 \leq p \leq 673$. $M_p = 6060$.

For $p = 673$ (prime): $v_p(2020!) = 3$ (since $3 \cdot 673 = 2019 \leq 2020 < 2692 = 4 \cdot 673$). $M_p = 6060$.

$A \geq \lceil (6052 - 3 \cdot 672)/673 \rceil = \lceil (6052 - 2016)/673 \rceil = \lceil 4036/673 \rceil = 6$.
$A = 6$: $a = (2,2,2)$, $B = 6052 - 4038 = 2014$. $g = 12 \cdot 673 + 2 \cdot 2014 = 8076 + 4028 = 12104$. $12104 \geq 6060$. ✓

So all primes with $v_p \geq 3$ are fine.

Let me now also verify that $n = 6051$ fails. We showed for $p = 2017$:
$(x, y, z) = (2016, 2016, 2019)$: $g_{2017}(2016) + g_{2017}(2016) + g_{2017}(2019) = 0 + 0 + 2019 = 2019 < 2020 = M_{2017}$.

And $(a, b, c) = (2020, 0, 0)$: $f(a,b,c) = (2020!)^{2020} \cdot 1 \cdot 1$. $v_{2017}(f(a,b,c)) = 2020 \cdot v_{2017}(2020!) = 2020 \cdot 1 = 2020$.
$v_{2017}(f(x,y,z)) = 2016 \cdot 0 + 2016 \cdot 0 + 2019 \cdot 1 = 2019 < 2020$.

So $f(a,b,c) \nmid f(x,y,z)$. Hence $n = 6051$ doesn't work.

Therefore, the answer is $n = 6052$.

Wait, let me double-check the computation $6052 = 2 \cdot 2017 + 2018$. $2 \cdot 2017 = 4034$. $4034 + 2018 = 6052$. ✓

And $2018 = 2020 - 2$.
