# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   The 34th question: Given an integer $n \geq 4$, find the smallest $\lambda(n)$ such that for any non-negative real numbers $a_{1}, a_{2}, \ldots, a_{n}$ (indices taken modulo $n$), the inequality $\sum_{i=1}^{n}\left\{a_{i}\right\} a_{i+1} \leq \lambda(n)$ always holds.       — 题目文本
#   The 34th question,
Solution: We first prove a lemma: Let the integer $\mathrm{n} \geq 4$, real numbers $r_{i} \in[0,1](1 \leq \mathrm{i} \leq \mathrm{n})$, satisfy $\sum_{i=1}^{n} r_{i}=r$, where $r \in \mathbb{N}$, and $r \leq n-1$, then $\sum_{i=1}^{n} r_{i} r_{i+1} \leq r-\frac{3}{4}$.
Proof of the lemma: If $\mathrm{r}=0$, the conclusion is obviously true. Now assume $\mathrm{r} \in \mathbb{Z}^{+}$.
Let $f\left(r_{1}, r_{2}, \ldots, r_{n}\right)=\sum_{i=1}^{n} r_{i} r_{i+1}$, then $f$ is a continuous function defined on a bounded closed set, so there exists a maximum value $S$.

Without loss of generality, assume that $f$ achieves $S$ at $\left(r_{1}, r_{2}, \ldots, r_{n}\right)$, and that $r_{1}, r_{2}, \ldots, r_{n}$ contain the maximum number of 0s and 1s. We will prove: for any two non-adjacent $r_{i}, r_{j}$ (non-adjacent means $i-j \neq \pm 1 (\bmod n)$), one of $r_{i}, r_{j}$ must be 0 or 1.

In fact, for any two non-adjacent $r_{i}, r_{j}$. Let $t=r_{i}+r_{j}$, and let $x=r_{i}$, then $\sum_{i=1}^{n} r_{i} r_{i+1}$ is a linear function of $x$. Therefore, when $\sum_{i=1}^{n} r_{i} r_{i+1}$ achieves its maximum value, it must be that $x \in \{0, \min \{1, t\}\}$. This indicates that one of $r_{i}, r_{j}$ must be 0 or 1.

The above conclusion shows: among $r_{1}, r_{2}, \ldots, r_{n}$, at most two numbers do not belong to $\{0,1\}$, and these two numbers must be adjacent.
If $r_{1}, r_{2}, \ldots, r_{n}$ are all 0 or 1, then there are exactly $r$ ones, so $\sum_{i=1}^{n} r_{i} r_{i+1} \leq r-1$,
If $r_{1}, r_{2}, \ldots, r_{n}$ have two numbers not in $\{0,1\}$, without loss of generality, let these be $r_{1}, r_{2} \in (0,1)$, then the remaining $n-2$ numbers are all 0 or 1. Thus, $r_{1} + r_{2} = 1$, and among the remaining $n-2$ numbers, there are exactly $r-1$ ones. Therefore, $\sum_{i=1}^{n} r_{i} r_{i+1} \leq r_{1} r_{2} + r_{2} + r - 2 + r_{1} = r - 3 + (1 + r_{1})(1 + r_{2}) \leq r - 3 + \frac{[(1 + r_{1}) + (1 + r_{2})]^2}{4} = r - \frac{3}{4}$.

In summary, the lemma is proved. And it is easy to see that the equality holds only when $r=n-1, r_{1}=r_{2}=\frac{1}{2}, r_{3}=r_{4}=\ldots=r_{n}=1$.
Now let's return to the original problem.
Let $\left[a_{i}\right]=b_{i}, \left\{a_{i}\right\}=r_{i} (1 \leq i \leq n)$, and let $\sum_{i=1}^{n} r_{i}=r$, then $r \in \mathbb{N}$, and $r \leq n-1$. According to the lemma, we have:
$$
\begin{array}{l}
\sum_{i=1}^{n}\left\{a_{i}\right\} a_{i+1}=\sum_{i=1}^{n} r_{i}\left(b_{i+1}+r_{i+1}\right)=\sum_{i=1}^{n} r_{i} b_{i+1}+\sum_{i=1}^{n} r_{i} r_{i+1} \\
\leq \sum_{i=1}^{n} b_{i+1}+\sum_{i=1}^{n} r_{i} r_{i+1} \leq \sum_{i=1}^{n} b_{i+1}+\sum_{i=1}^{n} r_{i}-\frac{3}{4}=n-\frac{3}{4}
\end{array}
$$

On the other hand, we take $a_{1}=\frac{3}{2}+(n-2) \varepsilon, a_{2}=\frac{1}{2}, a_{3}=a_{4}=\ldots=a_{n}=1-\varepsilon$. Then let $\varepsilon \rightarrow 0^{+}$,
then
$$
\sum_{i=1}^{n}\left\{a_{i}\right\} a_{i+1}=\left(\frac{1}{2}+(n-2) \varepsilon\right) \cdot \frac{1}{2}+\frac{1}{2} \cdot(1-\varepsilon)+(n-3)(1-\varepsilon)^{2}+(1-\varepsilon) \cdot\left(\frac{3}{2}+(n-\right.
$$
2) $\varepsilon) \rightarrow n-\frac{3}{4}$
In summary, the minimum value of $\lambda(n)$ is $n-\frac{3}{4}$.  — 标准解答
#   Let me analyze this problem carefully.

We need to find the smallest $\lambda(n)$ such that for any non-negative real numbers $a_1, a_2, \ldots, a_n$ (indices mod $n$), we have:
$$\sum_{i=1}^{n}\{a_i\} a_{i+1} \leq \lambda(n)$$

where $\{a_i\}$ is the fractional part of $a_i$.

Wait, but this can't be bounded unless there's some constraint. If all $a_i$ can be arbitrarily large, then $\{a_i\}$ can be close to 1 and $a_{i+1}$ can be arbitrarily large, so the sum is unbounded.

Let me re-read the problem. "for any non-negative real numbers $a_1, a_2, \ldots, a_n$". Hmm, there must be an additional constraint. Let me think... maybe $\sum a_i = 1$ or something similar? Or maybe the constraint is that $\{a_i\}$ appears and there's a normalization.

Actually, wait. Let me reconsider. Perhaps the problem has a constraint like $\sum a_i = 1$ or $\sum a_i \leq 1$ or the $a_i$ are in $[0,1)$... but the problem says "non-negative real numbers" and uses fractional parts.

Hmm, actually if $a_i$ are non-negative reals with no constraint, the sum is unbounded. So there must be a missing constraint. Let me think about what's standard.

Actually, perhaps the constraint is $\sum a_i = 1$. This is a common type of problem. Let me assume $\sum_{i=1}^n a_i = 1$.

With $\sum a_i = 1$, we want to maximize $\sum \{a_i\} a_{i+1}$.

Since $a_i \geq 0$ and $\sum a_i = 1$, each $a_i \leq 1$, so $\{a_i\} = a_i$ (since $a_i \leq 1$ means $a_i < 2$... wait, $a_i$ could be exactly 1, then $\{a_i\} = 0$).

Actually if $\sum a_i = 1$ and $a_i \geq 0$, then $a_i \in [0,1]$. If $a_i = 1$ for some $i$, then all others are 0, and $\{a_i\} = 0$, so the sum is 0.

If all $a_i < 1$, then $\{a_i\} = a_i$, and the sum becomes $\sum a_i a_{i+1}$.

So the problem reduces to: maximize $\sum a_i a_{i+1}$ subject to $\sum a_i = 1$, $a_i \geq 0$, $a_i < 1$ (but we can take the sup over $a_i \leq 1$).

The maximum of $\sum a_i a_{i+1}$ subject to $\sum a_i = 1$, $a_i \geq 0$ is a known problem. By convexity arguments, the maximum is achieved when all mass is concentrated on two adjacent variables. If $a_1 = a_2 = 1/2$ and rest 0, then $\sum a_i a_{i+1} = a_1 a_2 + a_2 a_3 + \ldots = (1/2)(1/2) = 1/4$.

But wait, can we do better? If we put mass on $a_1 = t, a_2 = 1-t$, the sum is $t(1-t) + (1-t)\cdot 0 + 0 \cdot t = t(1-t)$, maximized at $t = 1/2$ giving $1/4$.

What about three consecutive? $a_1, a_2, a_3$ with $a_1 + a_2 + a_3 = 1$. Sum = $a_1 a_2 + a_2 a_3 + a_3 \cdot 0 + \ldots$. To maximize $a_1 a_2 + a_2 a_3 = a_2(a_1 + a_3) = a_2(1 - a_2)$, maximized at $a_2 = 1/2$ giving $1/4$, with $a_1 + a_3 = 1/2$.

So the maximum is $1/4$ regardless of $n \geq 4$? That seems too simple and doesn't depend on $n$.

Hmm, but the problem asks for $\lambda(n)$ depending on $n$. So maybe my assumption about the constraint is wrong.

Let me reconsider. Maybe the constraint is different. Perhaps $\sum a_i = n$ or $\sum \{a_i\} = 1$ or something else.

Actually, let me reconsider the problem. Maybe there's no sum constraint but rather the $a_i$ are in $[0,1]$? No, then $\{a_i\} = a_i$ and it's the same as maximizing $\sum a_i a_{i+1}$ with $a_i \in [0,1]$, which is unbounded (set all $a_i = 1$, get $n$).

Hmm wait, if $a_i \in [0,1]$, then $\sum a_i a_{i+1} \leq n$ with all $a_i = 1$. But $\{1\} = 0$, so actually $\{a_i\} = a_i$ only if $a_i < 1$. If $a_i = 1$, $\{a_i\} = 0$.

So if $a_i \in [0,1]$, the fractional part $\{a_i\} = a_i$ for $a_i < 1$ and $\{a_i\} = 0$ for $a_i = 1$. The supremum of $\sum \{a_i\} a_{i+1}$ with $a_i \in [0,1]$ would be approached by setting all $a_i$ close to 1 but not equal to 1, giving close to $n$. But that's not achieved, so $\lambda(n) = n$? That also seems odd.

Let me think again about what constraint makes this problem interesting and $n$-dependent.

Actually, maybe the problem is: $\sum a_i = 1$ but the $a_i$ are general non-negative reals (not necessarily $\leq 1$). Then $\{a_i\}$ can differ from $a_i$ when $a_i \geq 1$. But with $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \leq 1$, so $\{a_i\} = a_i$ (except when $a_i = 1$ exactly, where $\{a_i\} = 0$). So the problem is essentially maximize $\sum a_i a_{i+1}$ with $\sum a_i = 1$, $a_i \geq 0$, and the answer is $1/4$ for all $n \geq 3$.

This doesn't depend on $n$, which contradicts the problem asking for $\lambda(n)$.

Let me reconsider. Perhaps the constraint is $\sum a_i^2 = 1$ or $\sum a_i \leq n$ or the $a_i$ are integers... no, they're reals.

Actually, maybe I'm overcomplicating this. Let me re-read: "find the smallest $\lambda(n)$ such that for any non-negative real numbers $a_1, \ldots, a_n$, the inequality $\sum \{a_i\} a_{i+1} \leq \lambda(n)$ always holds."

Without any constraint, this is unbounded. So there MUST be a constraint that I'm missing, or the problem statement is incomplete, or there's a different interpretation.

Wait—maybe the constraint is that $\sum a_i = 1$? But as I showed, that gives $1/4$ for all $n$.

Or maybe $\sum \{a_i\} = 1$? That's an interesting constraint. Then we want to maximize $\sum \{a_i\} a_{i+1}$ subject to $\sum \{a_i\} = 1$ and $a_i \geq 0$.

With $\sum \{a_i\} = 1$, let $f_i = \{a_i\} \in [0,1)$. Then $\sum f_i = 1$ and $a_i = \lfloor a_i \rfloor + f_i$. We want to maximize $\sum f_i a_{i+1} = \sum f_i (\lfloor a_{i+1} \rfloor + f_{i+1})$.

Since $\lfloor a_{i+1} \rfloor$ can be any non-negative integer, this is still unbounded! Unless there's another constraint.

Hmm. Let me think about this differently. Maybe the problem is from a specific competition and has a specific constraint that got lost in translation.

Actually, let me reconsider. Perhaps the problem states that $a_1 + a_2 + \cdots + a_n = 1$ and the answer does depend on $n$ in a way I'm not seeing.

Wait, with $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \in [0,1]$. The only issue is when $a_i = 1$ exactly, $\{a_i\} = 0 \neq a_i$. So the function $\sum \{a_i\} a_{i+1}$ is NOT the same as $\sum a_i a_{i+1}$ when some $a_i = 1$.

But the maximum of $\sum a_i a_{i+1}$ over $\sum a_i = 1$, $a_i \geq 0$ is $1/4$, achieved at $a_1 = a_2 = 1/2$. At this point, $\{a_i\} = a_i$ for all $i$ (since $1/2 < 1$), so $\sum \{a_i\} a_{i+1} = 1/4$ as well.

So $\lambda(n) = 1/4$ for $n \geq 3$? But the problem says $n \geq 4$ and asks for $\lambda(n)$...

Unless the constraint is different. Let me try $\sum a_i = n$ (so average is 1). Then $a_i$ can be larger than 1, and $\{a_i\}$ can differ from $a_i$.

With $\sum a_i = n$, we want to maximize $\sum \{a_i\} a_{i+1}$.

Hmm, this is more interesting. Let me think about small cases.

For $n = 4$, $\sum a_i = 4$. We want to maximize $\{a_1\}a_2 + \{a_2\}a_3 + \{a_3\}a_4 + \{a_4\}a_1$.

If all $a_i = 1$, then $\{a_i\} = 0$ and the sum is 0.

If $a_1 = 1 + \epsilon, a_2 = 1 + \epsilon, a_3 = 1 - \epsilon, a_4 = 1 - \epsilon$ (sum = 4), then $\{a_1\} = \epsilon, \{a_2\} = \epsilon, \{a_3\} = 1 - \epsilon, \{a_4\} = 1 - \epsilon$ (for small $\epsilon > 0$). Sum = $\epsilon(1+\epsilon) + \epsilon(1-\epsilon) + (1-\epsilon)(1-\epsilon) + (1-\epsilon)(1+\epsilon) = \epsilon + \epsilon^2 + \epsilon - \epsilon^2 + 1 - 2\epsilon + \epsilon^2 + 1 - \epsilon^2 = 2$.

Hmm, that gives 2. Let me try to maximize further.

Actually, let me try: $a_1 = 2 - \epsilon, a_2 = 2 - \epsilon, a_3 = \epsilon, a_4 = \epsilon$ (sum = 4). Then $\{a_1\} = 1 - \epsilon, \{a_2\} = 1 - \epsilon, \{a_3\} = \epsilon, \{a_4\} = \epsilon$. Sum = $(1-\epsilon)(2-\epsilon) + (1-\epsilon)\epsilon + \epsilon \cdot \epsilon + \epsilon(2-\epsilon) = (2 - 3\epsilon + \epsilon^2) + (\epsilon - \epsilon^2) + \epsilon^2 + (2\epsilon - \epsilon^2) = 2 - 3\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + \epsilon^2 + 2\epsilon - \epsilon^2 = 2$.

Also 2. Let me try another configuration.

$a_1 = 3 - \epsilon, a_2 = 1 + \epsilon, a_3 = \epsilon, a_4 = \epsilon$ (sum = 4). $\{a_1\} = 1 - \epsilon$ (wait, $3 - \epsilon$ has integer part 2, so $\{a_1\} = 1 - \epsilon$). Hmm, $3 - \epsilon = 2 + (1 - \epsilon)$, so $\{a_1\} = 1 - \epsilon$. $\{a_2\} = \epsilon$. $\{a_3\} = \epsilon$. $\{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(1+\epsilon) + \epsilon \cdot \epsilon + \epsilon \cdot \epsilon + \epsilon(3-\epsilon) = (1 - \epsilon^2) + \epsilon^2 + \epsilon^2 + 3\epsilon - \epsilon^2 = 1 + 3\epsilon$.

As $\epsilon \to 0$, this approaches 1. Not as good.

Let me try: $a_1 = 1 - \epsilon, a_2 = 1 - \epsilon, a_3 = 1 - \epsilon, a_4 = 1 + 3\epsilon$ (sum = 4). $\{a_1\} = 1 - \epsilon, \{a_2\} = 1 - \epsilon, \{a_3\} = 1 - \epsilon, \{a_4\} = 3\epsilon$.

Sum = $(1-\epsilon)(1-\epsilon) + (1-\epsilon)(1-\epsilon) + (1-\epsilon)(1+3\epsilon) + 3\epsilon(1-\epsilon)$
$= (1 - 2\epsilon + \epsilon^2) + (1 - 2\epsilon + \epsilon^2) + (1 + 3\epsilon - \epsilon - 3\epsilon^2) + (3\epsilon - 3\epsilon^2)$
$= 1 - 2\epsilon + \epsilon^2 + 1 - 2\epsilon + \epsilon^2 + 1 + 2\epsilon - 3\epsilon^2 + 3\epsilon - 3\epsilon^2$
$= 3 + \epsilon - 4\epsilon^2$.

As $\epsilon \to 0$, approaches 3. Better!

Let me try all $a_i = 1 - \epsilon$ except one: $a_1 = a_2 = a_3 = 1 - \epsilon, a_4 = 1 + 3\epsilon$. Already did this, got approaching 3.

What about $a_1 = a_2 = a_3 = a_4 = 1 - \epsilon$? Sum = $4 - 4\epsilon \neq 4$. Need to adjust.

Let me try: $a_i = 1 - \epsilon$ for all $i$, but then sum = $4(1-\epsilon) = 4 - 4\epsilon$. To make sum = 4, we need to add $4\epsilon$ somewhere. If we add it to $a_4$: $a_4 = 1 + 3\epsilon$, as above.

What if we spread it: $a_1 = a_2 = 1 - \epsilon, a_3 = a_4 = 1 + \epsilon$. Sum = 4. $\{a_1\} = 1 - \epsilon, \{a_2\} = 1 - \epsilon, \{a_3\} = \epsilon, \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(1-\epsilon) + (1-\epsilon)(1+\epsilon) + \epsilon(1+\epsilon) + \epsilon(1-\epsilon)$
$= 1 - 2\epsilon + \epsilon^2 + 1 - \epsilon^2 + \epsilon + \epsilon^2 + \epsilon - \epsilon^2$
$= 2$.

Hmm, that's only 2. The issue is that when $a_i$ crosses an integer, the fractional part drops.

So the key insight is: to maximize, we want as many $a_i$ as possible to have fractional part close to 1 (i.e., $a_i$ just below an integer) and the next $a_{i+1}$ to be large.

With $\sum a_i = n$ and $n = 4$: if $a_1, a_2, a_3$ are just below 1 (fractional part $\approx 1$) and $a_4$ is just above 1 (fractional part $\approx 0$), we get contributions from $\{a_1\}a_2 + \{a_2\}a_3 + \{a_3\}a_4 \approx 1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 = 3$, and $\{a_4\}a_1 \approx 0$.

Can we do better? What if $a_1, a_2, a_3$ are just below 2 (fractional part $\approx 1$) and $a_4$ is large? But $\sum a_i = 4$, so if $a_1, a_2, a_3 \approx 2$, that's already 6 > 4. Not possible.

What about $a_1, a_2$ just below 2, $a_3, a_4$ small? $a_1 = a_2 = 2 - \epsilon, a_3 = a_4 = \epsilon$. Sum = 4. $\{a_1\} = \{a_2\} = 1 - \epsilon, \{a_3\} = \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(2-\epsilon) + (1-\epsilon)\epsilon + \epsilon \cdot \epsilon + \epsilon(2-\epsilon) = 2 - 3\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + \epsilon^2 + 2\epsilon - \epsilon^2 = 2$.

So 2, not as good as 3.

What about $a_1 = 1 - \epsilon, a_2 = 1 - \epsilon, a_3 = 1 - \epsilon, a_4 = 1 + 3\epsilon$? Got $\approx 3$.

Can we get more than 3? What about making some $a_i$ just below 2?

$a_1 = 2 - \epsilon, a_2 = 1 - \epsilon, a_3 = 1 - \epsilon, a_4 = \epsilon$. Sum = 4. $\{a_1\} = 1 - \epsilon, \{a_2\} = 1 - \epsilon, \{a_3\} = 1 - \epsilon, \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(1-\epsilon) + (1-\epsilon)(1-\epsilon) + (1-\epsilon)\epsilon + \epsilon(2-\epsilon)$
$= 1 - 2\epsilon + \epsilon^2 + 1 - 2\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + 2\epsilon - \epsilon^2$
$= 2 - \epsilon$.

Approaches 2. Worse.

$a_1 = 1 - \epsilon, a_2 = 2 - \epsilon, a_3 = 1 - \epsilon, a_4 = \epsilon$. Sum = 4. $\{a_1\} = 1-\epsilon, \{a_2\} = 1-\epsilon, \{a_3\} = 1-\epsilon, \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(2-\epsilon) + (1-\epsilon)(1-\epsilon) + (1-\epsilon)\epsilon + \epsilon(1-\epsilon)$
$= 2 - 3\epsilon + \epsilon^2 + 1 - 2\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + \epsilon - \epsilon^2$
$= 3 - 3\epsilon$.

Approaches 3. Same.

What about $a_1 = 1-\epsilon, a_2 = 1-\epsilon, a_3 = 2-\epsilon, a_4 = \epsilon$? Sum = 4.
$\{a_1\} = 1-\epsilon, \{a_2\} = 1-\epsilon, \{a_3\} = 1-\epsilon, \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(1-\epsilon) + (1-\epsilon)(2-\epsilon) + (1-\epsilon)\epsilon + \epsilon(1-\epsilon)$
$= 1 - 2\epsilon + \epsilon^2 + 2 - 3\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + \epsilon - \epsilon^2$
$= 3 - 3\epsilon$.

Approaches 3.

So for $n = 4$, it seems like the supremum is 3, achieved when 3 of the 4 variables are just below 1 and one is just above 1 (or small).

Actually wait, let me reconsider. With $a_1 = a_2 = a_3 = 1 - \epsilon, a_4 = 1 + 3\epsilon$:

The sum approaches 3 as $\epsilon \to 0$. But can we actually achieve 3? No, because at $\epsilon = 0$, all $a_i = 1$ and $\{a_i\} = 0$. So the supremum is 3 but not achieved.

Hmm, but the problem says "find the smallest $\lambda(n)$ such that the inequality always holds." If the supremum is 3 but not achieved, then $\lambda(4) = 3$ works (since the sum is always strictly less than 3, so $\leq 3$ holds).

Wait, but is the supremum actually 3? Let me check if we can exceed 3.

Let me try a different approach. Let $f_i = \{a_i\}$ and $m_i = \lfloor a_i \rfloor$, so $a_i = m_i + f_i$ with $m_i \geq 0$ integer and $f_i \in [0, 1)$.

$\sum a_i = \sum m_i + \sum f_i = n$.

$\sum \{a_i\} a_{i+1} = \sum f_i (m_{i+1} + f_{i+1}) = \sum f_i m_{i+1} + \sum f_i f_{i+1}$.

We want to maximize this subject to $\sum m_i + \sum f_i = n$, $m_i \geq 0$ integer, $f_i \in [0, 1)$.

Since $f_i < 1$, we have $\sum f_i < n$, so $\sum m_i \geq 1$ (actually $\sum m_i = n - \sum f_i > 0$).

To maximize $\sum f_i m_{i+1}$, we want $f_i$ close to 1 and $m_{i+1}$ large. But $\sum m_i = n - \sum f_i$, and if all $f_i$ are close to 1, $\sum f_i \approx n$, so $\sum m_i \approx 0$, meaning all $m_i \approx 0$. Then $\sum f_i m_{i+1} \approx 0$ and $\sum f_i f_{i+1} \approx n$.

Wait, that's interesting! If all $f_i \to 1$ and all $m_i = 0$, then $\sum f_i \to n$ but $\sum f_i < n$ requires $\sum m_i > 0$. So we need at least one $m_i \geq 1$.

If $m_4 = 1$ and all other $m_i = 0$, with $f_1 = f_2 = f_3 = 1 - \epsilon$ and $f_4 = 1 - 3\epsilon$ (so $\sum f_i = 4 - 6\epsilon$, $\sum m_i = 1$, total = $5 - 6\epsilon$... that's not $n = 4$).

Let me be more careful. $\sum m_i + \sum f_i = n = 4$. If $m_4 = 1$, all other $m_i = 0$, then $\sum f_i = 3$. We need $f_1 + f_2 + f_3 + f_4 = 3$ with $f_i \in [0,1)$.

To maximize $\sum f_i f_{i+1} + \sum f_i m_{i+1}$:
- $\sum f_i m_{i+1} = f_1 \cdot 0 + f_2 \cdot 0 + f_3 \cdot 0 + f_4 \cdot 1 = f_4$ (wait, $m_{i+1}$: $m_2 = 0, m_3 = 0, m_4 = 0, m_1 = 0$... hmm, indices).

Wait, let me be careful with indices. $m_{i+1}$ where indices are mod $n$. So:
- $i=1$: $f_1 \cdot m_2$
- $i=2$: $f_2 \cdot m_3$
- $i=3$: $f_3 \cdot m_4 = f_3 \cdot 1 = f_3$
- $i=4$: $f_4 \cdot m_1 = f_4 \cdot 0 = 0$

So $\sum f_i m_{i+1} = f_3$.

And $\sum f_i f_{i+1} = f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1$.

Total = $f_3 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_3(1 + f_2 + f_4) + f_1 f_2 + f_4 f_1 = f_3(1 + f_2 + f_4) + f_1(f_2 + f_4)$.

With $f_1 + f_2 + f_3 + f_4 = 3$, $f_i \in [0,1)$.

Let $s = f_2 + f_4$ and $f_1 + f_3 = 3 - s$. Then total = $f_3(1 + s) + f_1 \cdot s = f_3 + s(f_1 + f_3) = f_3 + s(3 - s)$.

To maximize: we want $f_3$ large and $s(3-s)$ large. $s(3-s)$ is maximized at $s = 3/2$ giving $9/4$. And $f_3 < 1$. So total $< 1 + 9/4 = 13/4 = 3.25$.

But we need $f_1 + f_3 = 3 - s = 3 - 3/2 = 3/2$, with $f_3 < 1$ and $f_1 < 1$, so $f_1 > 1/2$. And $s = f_2 + f_4 = 3/2$ with $f_2, f_4 < 1$, so both $> 1/2$. This is feasible.

So the total can approach $1 + 9/4 = 13/4$? Let me check more carefully.

With $f_3 \to 1$, $f_1 \to 1/2$, $f_2 \to 3/4$, $f_4 \to 3/4$ (so $s = 3/2$):
Total $\to 1 \cdot (1 + 3/2) + (1/2)(3/2) = 5/2 + 3/4 = 13/4$.

But wait, we need $f_3 < 1$. As $f_3 \to 1^-$, $f_1 \to 1/2^+$ (since $f_1 = 3 - s - f_3 = 3/2 - f_3 \to 1/2$). And $f_1 < 1$ is satisfied. So the supremum is $13/4$.

But can we do even better with different $m_i$ assignments?

Let me try $m_3 = 1$ (instead of $m_4$). Then:
- $i=1$: $f_1 \cdot m_2 = 0$
- $i=2$: $f_2 \cdot m_3 = f_2$
- $i=3$: $f_3 \cdot m_4 = 0$
- $i=4$: $f_4 \cdot m_1 = 0$

Total = $f_2 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_2(1 + f_1 + f_3) + f_4(f_3 + f_1)$.

Same structure by symmetry. So same supremum $13/4$.

What about $m_1 = 1$?
- $i=4$: $f_4 \cdot m_1 = f_4$
- Others: 0

Total = $f_4 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_4(1 + f_3 + f_1) + f_2(f_1 + f_3)$.

Same structure. Supremum $13/4$.

What about $m_2 = 1$?
- $i=1$: $f_1 \cdot m_2 = f_1$
Total = $f_1 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_1(1 + f_2 + f_4) + f_3(f_2 + f_4)$.

Same. Supremum $13/4$.

Now what about $m_4 = 2$? Then $\sum f_i = 2$. 
- $i=3$: $f_3 \cdot m_4 = 2 f_3$

Total = $2f_3 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_3(2 + f_2 + f_4) + f_1(f_2 + f_4)$.

With $f_1 + f_2 + f_3 + f_4 = 2$, $f_i \in [0,1)$.

Let $s = f_2 + f_4$, $f_1 + f_3 = 2 - s$. Total = $f_3(2 + s) + f_1 \cdot s = 2f_3 + s(f_1 + f_3) = 2f_3 + s(2 - s)$.

Maximize: $f_3 < 1$, $s(2-s)$ maximized at $s = 1$ giving $1$. Total $< 2 + 1 = 3$. Less than $13/4 = 3.25$.

What about $m_3 = 1, m_4 = 1$? $\sum f_i = 2$.
- $i=2$: $f_2 \cdot m_3 = f_2$
- $i=3$: $f_3 \cdot m_4 = f_3$

Total = $f_2 + f_3 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1$.

With $\sum f_i = 2$. Let me try $f_2 = f_3 \to 1, f_1 = f_4 \to 0$. Total $\to 1 + 1 + 0 + 1 + 0 + 0 = 3$. Less than $13/4$.

Try $f_1 = f_2 = f_3 = f_4 = 1/2$. Total = $1/2 + 1/2 + 1/4 + 1/4 + 1/4 + 1/4 = 2$. Less.

Try $f_2 \to 1, f_3 \to 1, f_1 + f_4 \to 0$. Total $\to 1 + 1 + 0 + 1 + 0 + 0 = 3$.

What about $m_1 = 1, m_3 = 1$? $\sum f_i = 2$.
- $i=4$: $f_4 \cdot m_1 = f_4$
- $i=2$: $f_2 \cdot m_3 = f_2$

Total = $f_2 + f_4 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1$.

Try $f_2 \to 1, f_4 \to 1, f_1, f_3 \to 0$. Total $\to 1 + 1 + 0 + 0 + 0 + 0 = 2$. Less.

Try $f_1 = f_3 \to 1, f_2 = f_4 \to 0$. Total $\to 0 + 0 + 0 + 0 + 0 + 0 = 0$.

What about $m_1 = 1, m_2 = 1$? $\sum f_i = 2$.
- $i=4$: $f_4 \cdot m_1 = f_4$
- $i=1$: $f_1 \cdot m_2 = f_1$

Total = $f_1 + f_4 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1$.

Try $f_1 \to 1, f_4 \to 1, f_2, f_3 \to 0$. Total $\to 1 + 1 + 0 + 0 + 0 + 0 = 2$.

So the best so far is $13/4$ with one $m_i = 1$ and the rest 0.

Can we do better with $m_4 = 1$ but different $f$ values? Let me re-examine.

With $m_4 = 1$, total = $f_3(1 + f_2 + f_4) + f_1(f_2 + f_4)$, $\sum f_i = 3$.

Let $s = f_2 + f_4$. Total = $f_3(1 + s) + (3 - s - f_3) \cdot s = f_3(1 + s) + 3s - s^2 - f_3 s = f_3 + 3s - s^2$.

So total = $f_3 + 3s - s^2$ where $f_3 < 1$, $s = f_2 + f_4 \in [0, 2)$ (since $f_2, f_4 < 1$), and $f_1 = 3 - s - f_3 \in [0, 1)$, so $f_3 > 2 - s$ and $f_3 < 3 - s$.

To maximize $f_3 + 3s - s^2$: since $f_3 < 1$, we want $f_3 \to 1$. Then total $\to 1 + 3s - s^2$. This is maximized at $s = 3/2$ giving $1 + 9/4 = 13/4$.

Constraints: $f_3 \to 1$ requires $2 - s < 1$, i.e., $s > 1$. And $f_1 = 3 - s - 1 = 2 - s < 1$ requires $s > 1$. And $f_1 \geq 0$ requires $s \leq 2$. And $s < 2$ (since $f_2, f_4 < 1$). So $s \in (1, 2)$, and $s = 3/2$ is feasible.

Also need $f_2, f_4 < 1$ with $f_2 + f_4 = 3/2$, so both in $(1/2, 1)$. Feasible.

So supremum is $13/4$ for $n = 4$.

Hmm wait, but I should also consider whether we can do better by not having exactly one $m_i = 1$. What about $m_4 = 1$ but also considering that maybe having a different structure could help?

Actually, I realize I should think about this more generally. Let me consider the problem for general $n$ with the constraint $\sum a_i = n$.

Hmm, but actually I'm not even sure the constraint is $\sum a_i = n$. Let me reconsider the problem statement.

"Given an integer $n \geq 4$, find the smallest $\lambda(n)$ such that for any non-negative real numbers $a_1, a_2, \ldots, a_n$ (indices taken modulo $n$), the inequality $\sum_{i=1}^{n}\{a_i\} a_{i+1} \leq \lambda(n)$ always holds."

There's no constraint mentioned! This is unbounded without a constraint. So either:
1. The problem is missing a constraint (likely $\sum a_i = 1$ or $\sum a_i = n$).
2. There's a different interpretation.

Given that the answer should depend on $n$ and the problem uses fractional parts, I think the most likely constraint is $\sum a_i = 1$. But as I showed, that gives $1/4$ for all $n \geq 3$.

Unless... the constraint is $\sum a_i = n$? Then for $n = 4$ I got $13/4$.

Actually, wait. Let me reconsider the case $\sum a_i = 1$ more carefully. With $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \in [0, 1]$. The fractional part $\{a_i\} = a_i$ if $a_i < 1$ and $\{a_i\} = 0$ if $a_i = 1$.

So $\sum \{a_i\} a_{i+1} \leq \sum a_i a_{i+1}$, and the maximum of $\sum a_i a_{i+1}$ with $\sum a_i = 1$ is $1/4$ (achieved at two adjacent $a_i = 1/2$). And $\{1/2\} = 1/2$, so the bound $1/4$ is achieved. So $\lambda(n) = 1/4$ for $n \geq 3$.

But the problem asks for $\lambda(n)$ as a function of $n$ with $n \geq 4$, suggesting the answer depends on $n$. So the constraint is probably not $\sum a_i = 1$.

Let me try $\sum a_i = n$. For general $n$:

With one $m_k = 1$ and rest 0, $\sum f_i = n - 1$. The total is:
$f_{k-1} \cdot 1 + \sum f_i f_{i+1}$ (where the $f_{k-1} \cdot 1$ comes from the $m_k$ term, since $a_{k-1}$'s fractional part times $a_k$'s integer part).

Wait, let me be more careful. If $m_k = 1$ and all other $m_i = 0$, then:
$\sum f_i m_{i+1} = f_{k-1} \cdot m_k = f_{k-1}$ (since $m_k = 1$ and all other $m_{i+1} = 0$).

So total = $f_{k-1} + \sum_{i=1}^n f_i f_{i+1}$, with $\sum f_i = n - 1$, $f_i \in [0, 1)$.

We want to maximize $f_{k-1} + \sum f_i f_{i+1}$.

Let me think about this for general $n$. WLOG $k = n$ (by rotation), so we maximize $f_{n-1} + \sum_{i=1}^n f_i f_{i+1}$ with $\sum f_i = n-1$, $f_i \in [0,1)$.

Since $\sum f_i = n - 1$ and $f_i < 1$, we need at least... well, $n$ variables each less than 1 summing to $n-1$. The "deficit" from all being 1 is $\sum (1 - f_i) = n - (n-1) = 1$. So the total deficit is 1.

Let $g_i = 1 - f_i \in (0, 1]$. Then $\sum g_i = 1$ and $f_i = 1 - g_i$.

$\sum f_i f_{i+1} = \sum (1 - g_i)(1 - g_{i+1}) = \sum (1 - g_i - g_{i+1} + g_i g_{i+1}) = n - 2\sum g_i + \sum g_i g_{i+1} = n - 2 + \sum g_i g_{i+1}$.

And $f_{n-1} = 1 - g_{n-1}$.

Total = $(1 - g_{n-1}) + (n - 2) + \sum g_i g_{i+1} = n - 1 - g_{n-1} + \sum g_i g_{i+1}$.

We want to maximize this, i.e., maximize $\sum g_i g_{i+1} - g_{n-1}$ subject to $\sum g_i = 1$, $g_i \in (0, 1]$.

Hmm, this is getting complex. Let me think about it differently.

Actually, let me reconsider. Maybe the constraint is $\sum a_i = 1$ but the problem is more subtle than I thought. Let me re-examine.

With $\sum a_i = 1$, $a_i \geq 0$: the maximum of $\sum \{a_i\} a_{i+1}$ is indeed $1/4$ for $n \geq 3$. For $n = 4$, this is $1/4$. The problem says $n \geq 4$, which is consistent with $n \geq 3$ giving $1/4$.

But the problem asks for $\lambda(n)$, suggesting it depends on $n$. If it's constant $1/4$, that's a valid answer but unusual for a competition problem.

Hmm, let me reconsider. Maybe the problem is asking about $\sum \{a_i\} \cdot a_{i+1}$ where $a_i$ are non-negative integers? No, it says "non-negative real numbers."

Or maybe the problem has a different constraint that I'm not seeing. Let me try the interpretation that there's no constraint but $a_i \in [0, 1)$ (i.e., the $a_i$ are already fractional parts). Then $\{a_i\} = a_i$ and we want to maximize $\sum a_i a_{i+1}$ with $a_i \in [0, 1)$. This is unbounded (approach $n$ by setting all $a_i \to 1$).

OK, I think the most reasonable interpretation given the structure is $\sum a_i = 1$. Let me also consider the possibility that the answer is $\frac{1}{4}\sec^2(\pi/n)$ or $\frac{1}{4\cos^2(\pi/n)}$ or something trigonometric, which is a common form for cyclic optimization problems.

Actually, for the problem of maximizing $\sum a_i a_{i+1}$ subject to $\sum a_i = 1$, $a_i \geq 0$, the answer is $1/4$ for $n \geq 3$ (achieved by concentrating mass on two adjacent variables). But if we add the constraint that all $a_i > 0$ (strictly), the supremum is still $1/4$.

However, there's a related problem: maximize $\sum a_i a_{i+1}$ subject to $\sum a_i^2 = 1$ (or $\sum a_i = 1$ with all $a_i > 0$). The spectral answer involves $\cos(\pi/n)$.

Actually, the maximum of $\sum a_i a_{i+1}$ subject to $\sum a_i^2 = 1$ is $\cos(\pi/n)$ (the largest eigenvalue of the cyclic adjacency matrix). But that's a different constraint.

Let me try the constraint $\sum a_i^2 = 1$. Then we want to maximize $\sum \{a_i\} a_{i+1}$ with $a_i \geq 0$ and $\sum a_i^2 = 1$. Since $a_i \geq 0$ and $\sum a_i^2 = 1$, we have $a_i \leq 1$, so $\{a_i\} = a_i$ (except when $a_i = 1$). So the problem becomes maximize $\sum a_i a_{i+1}$ with $\sum a_i^2 = 1$, $a_i \geq 0$.

The maximum of $\sum a_i a_{i+1}$ with $\sum a_i^2 = 1$ is $\cos(\pi/n)$ (for the cycle graph $C_n$). This is achieved when $a_i \propto \cos(\pi i / n - \pi/(2n))$ or something like that (the eigenvector of the largest eigenvalue).

Wait, but we need $a_i \geq 0$. The eigenvector of the cycle graph's largest eigenvalue $\cos(\pi/n)$ has components $\cos(\pi(i-1)/n + \pi/(2n))$ or similar, which can be negative. So the non-negative constraint might change things.

Hmm, actually for the cycle $C_n$, the adjacency matrix has eigenvalues $2\cos(2\pi k/n)$ for $k = 0, 1, \ldots, n-1$. The largest is $2$ (for $k=0$, eigenvector all 1s). But we're looking at $\sum a_i a_{i+1} = \frac{1}{2} a^T A a$ where $A$ is the adjacency matrix. So maximizing $\frac{1}{2} a^T A a$ subject to $\|a\|^2 = 1$ gives $\frac{1}{2} \cdot 2 = 1$ (with $a = (1/\sqrt{n}, \ldots, 1/\sqrt{n})$). But that's the unconstrained maximum.

With $a_i \geq 0$, the all-positive eigenvector gives $\sum a_i a_{i+1} = n \cdot (1/n) = 1$... wait, $\sum a_i a_{i+1} = \sum (1/\sqrt{n})(1/\sqrt{n}) = n \cdot 1/n = 1$. And $\sum a_i^2 = 1$. So the maximum is 1, achieved at the uniform vector. But that doesn't depend on $n$ either.

Hmm, I think I need to be more careful. $\sum a_i a_{i+1}$ with $\sum a_i^2 = 1$: by Cauchy-Schwarz or spectral methods, $\sum a_i a_{i+1} \leq \frac{1}{2}\sum(a_i^2 + a_{i+1}^2) = \sum a_i^2 = 1$. So the maximum is 1, achieved when $a_i = a_{i+1}$ for all $i$, i.e., all equal. This gives $1$ for all $n$. Not $n$-dependent.

OK so with $\sum a_i^2 = 1$, the answer is $1$ for all $n$. Not interesting.

Let me go back to the $\sum a_i = n$ interpretation. For $n = 4$, I found the supremum is $13/4$. Let me check $n = 5$.

With $m_5 = 1$, rest 0, $\sum f_i = 4$. Total = $f_4 + \sum f_i f_{i+1}$.

Using $g_i = 1 - f_i$, $\sum g_i = 1$:
$\sum f_i f_{i+1} = n - 2 + \sum g_i g_{i+1} = 5 - 2 + \sum g_i g_{i+1} = 3 + \sum g_i g_{i+1}$.
$f_4 = 1 - g_4$.
Total = $1 - g_4 + 3 + \sum g_i g_{i+1} = 4 - g_4 + \sum g_i g_{i+1}$.

Maximize $\sum g_i g_{i+1} - g_4$ with $\sum g_i = 1$, $g_i \in (0, 1]$.

To maximize $\sum g_i g_{i+1}$, we want to concentrate the $g_i$ mass on adjacent pairs. But we also want to minimize $g_4$.

If we set $g_4 \to 0$ and concentrate mass on $g_1, g_2$ (adjacent): $g_1 = g_2 = 1/2$, rest 0. Then $\sum g_i g_{i+1} = g_1 g_2 = 1/4$. Total $= 4 - 0 + 1/4 = 17/4$.

But wait, $g_i > 0$ (since $f_i < 1$). So $g_4 \to 0^+$. And $g_3, g_5 \to 0^+$. So total $\to 4 + 1/4 = 17/4$.

Can we do better? What if we concentrate on $g_4, g_5$? Then $g_4 = 1/2, g_5 = 1/2$. $\sum g_i g_{i+1} = g_4 g_5 = 1/4$. Total $= 4 - 1/2 + 1/4 = 15/4$. Worse because of the $-g_4$ term.

What about $g_1 = 1$, rest $\to 0$? $\sum g_i g_{i+1} \to 0$. Total $\to 4 - 0 + 0 = 4$. Better than $17/4 = 4.25$? No, $4 < 4.25$.

What about $g_3 = g_4 = 1/2$? $\sum g_i g_{i+1} = g_3 g_4 = 1/4$. Total $= 4 - 1/2 + 1/4 = 3.75$. Worse.

So for $n = 5$, with one $m_i = 1$, the best is $17/4$ (concentrating $g$ mass away from index 4 and on an adjacent pair not involving index 4 or its neighbors).

Hmm wait, but I should also consider having more than one $m_i = 1$. Let me think about this differently.

Actually, let me reconsider the whole problem. Maybe the constraint is $\sum a_i = 1$ and the answer is $\frac{1}{4\cos^2(\pi/n)}$ or something like that. Let me think about what happens when we DON'T require $a_i < 1$.

With $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \leq 1$. The only way $\{a_i\} \neq a_i$ is if $a_i = 1$ (then $\{a_i\} = 0$). So $\{a_i\} \leq a_i$ always, and $\sum \{a_i\} a_{i+1} \leq \sum a_i a_{i+1} \leq 1/4$. And $1/4$ is achieved. So $\lambda(n) = 1/4$ for all $n \geq 3$.

This is a valid answer but doesn't depend on $n$. The problem specifically says $n \geq 4$ and asks for $\lambda(n)$, which strongly suggests the answer depends on $n$.

Let me try yet another interpretation: maybe the constraint is $\sum a_i = n$ (or $\sum a_i \leq n$). Let me pursue this.

For general $n$ with $\sum a_i = n$:

The key insight is that we can have some $a_i$ with integer parts, creating a gap between $\{a_i\}$ and $a_i$.

Let me think about the optimal strategy. We want to maximize $\sum f_i a_{i+1} = \sum f_i (m_{i+1} + f_{i+1})$ where $f_i = \{a_i\}$, $m_i = \lfloor a_i \rfloor$, $\sum (m_i + f_i) = n$.

The $\sum f_i f_{i+1}$ part is maximized when all $f_i$ are close to 1 (giving close to $n$). But then $\sum m_i \approx 0$ and the $\sum f_i m_{i+1}$ part is small.

The $\sum f_i m_{i+1}$ part benefits from having large $m_{i+1}$ preceded by $f_i$ close to 1.

Let me think about the trade-off. Suppose we set $k$ of the $m_i$ to be positive. Say $m_{i_1}, \ldots, m_{i_k}$ are positive with values $M_1, \ldots, M_k$, and $\sum M_j = M$ (total integer part). Then $\sum f_i = n - M$.

The $\sum f_i m_{i+1}$ term: for each $j$, if $m_{i_j} = M_j$, then the term $f_{i_j - 1} \cdot M_j$ contributes. So $\sum f_i m_{i+1} = \sum_j f_{i_j - 1} M_j$.

To maximize, we want $f_{i_j - 1}$ close to 1 and $M_j$ large. But $\sum f_i = n - M$ and $f_i < 1$, so we need $n - M < n$, i.e., $M > 0$, and the number of $f_i$ close to 1 is at most $n - M$ (roughly).

This is getting complicated. Let me try a specific strategy for general $n$.

Strategy: Set $m_n = 1$, all other $m_i = 0$. Then $\sum f_i = n - 1$. The total is:
$T = f_{n-1} + \sum_{i=1}^n f_i f_{i+1}$

Using $g_i = 1 - f_i$, $\sum g_i = 1$:
$T = (1 - g_{n-1}) + (n - 2 + \sum g_i g_{i+1}) = n - 1 - g_{n-1} + \sum g_i g_{i+1}$

We want to maximize $\sum g_i g_{i+1} - g_{n-1}$ with $\sum g_i = 1$, $g_i \in (0, 1]$.

The maximum of $\sum g_i g_{i+1}$ with $\sum g_i = 1$ is $1/4$ (concentrate on two adjacent variables). We want to do this while minimizing $g_{n-1}$.

If we concentrate on $g_1 = g_2 = 1/2$ (and $g_{n-1} \to 0$), we get $\sum g_i g_{i+1} = 1/4$ and $g_{n-1} \to 0$. Total $\to n - 1 + 1/4 = n - 3/4$.

For $n = 4$: $4 - 3/4 = 13/4$. ✓
For $n = 5$: $5 - 3/4 = 17/4$. ✓

But can we do better with a different strategy? What if we use $m_n = 2$?

$m_n = 2$, $\sum f_i = n - 2$. Total = $2f_{n-1} + \sum f_i f_{i+1}$.
$g_i = 1 - f_i$, $\sum g_i = 2$.
$\sum f_i f_{i+1} = n - 2 \cdot 2 + \sum g_i g_{i+1} = n - 4 + \sum g_i g_{i+1}$.
Total = $2(1 - g_{n-1}) + n - 4 + \sum g_i g_{i+1} = n - 2 - 2g_{n-1} + \sum g_i g_{i+1}$.

Maximize $\sum g_i g_{i+1} - 2g_{n-1}$ with $\sum g_i = 2$, $g_i \in (0, 1]$.

Max of $\sum g_i g_{i+1}$ with $\sum g_i = 2$: this is like maximizing a quadratic form. With all $g_i$ on two adjacent: $g_1 = g_2 = 1$, $\sum g_i g_{i+1} = 1$. With $g_{n-1} \to 0$: Total $\to n - 2 + 1 = n - 1$.

Compare with $m_n = 1$: $n - 3/4$. For $n \geq 4$, $n - 1 > n - 3/4$? $n - 1 > n - 0.75$ iff $-1 > -0.75$ which is false. So $n - 1 < n - 3/4$. So $m_n = 2$ is worse.

What about $m_n = 1, m_k = 1$ for some $k \neq n$? $\sum f_i = n - 2$.
Total = $f_{n-1} + f_{k-1} + \sum f_i f_{i+1}$.
$g_i = 1 - f_i$, $\sum g_i = 2$.
Total = $(1 - g_{n-1}) + (1 - g_{k-1}) + (n - 4 + \sum g_i g_{i+1}) = n - 2 - g_{n-1} - g_{k-1} + \sum g_i g_{i+1}$.

Maximize $\sum g_i g_{i+1} - g_{n-1} - g_{k-1}$ with $\sum g_i = 2$.

If $k$ is far from $n$, we can set $g_{n-1}, g_{k-1} \to 0$ and concentrate on two adjacent $g$'s. $\sum g_i g_{i+1} \to 1$ (with $g_1 = g_2 = 1$). Total $\to n - 2 + 1 = n - 1$. Same as $m_n = 2$.

What if $k = n - 1$? Then $g_{n-2} + g_{n-2}$... wait, $k - 1 = n - 2$ and $n - 1$. We minimize $g_{n-1} + g_{n-2}$. Concentrate $g$ on $g_1 = g_2 = 1$. Total $\to n - 2 + 1 = n - 1$. Same.

What if $k = 1$? Then $k - 1 = 0 = n$ (mod $n$), so $g_n + g_{n-1}$. We minimize $g_n + g_{n-1}$. Concentrate on $g_2 = g_3 = 1$. $\sum g_i g_{i+1} = g_2 g_3 = 1$. Total $\to n - 2 + 1 = n - 1$. Same.

So with two $m_i = 1$, we get $n - 1$, which is less than $n - 3/4$.

What about $m_n = 1$ but with a different distribution of $g$? Instead of concentrating on two adjacent, what if we spread?

$\sum g_i g_{i+1}$ with $\sum g_i = 1$: the maximum is $1/4$ (two adjacent at $1/2$ each). We can't do better. So the best with $m_n = 1$ is $n - 1 + 1/4 = n - 3/4$ (when $g_{n-1} \to 0$).

But wait, what if we don't set $g_{n-1} \to 0$ but instead find a better trade-off? We have:
$T = n - 1 - g_{n-1} + \sum g_i g_{i+1}$.

If $g_{n-1}$ is part of the adjacent pair, say $g_{n-1} = g_n = 1/2$, then $\sum g_i g_{i+1} = g_{n-1} g_n = 1/4$ and $T = n - 1 - 1/2 + 1/4 = n - 5/4$. Worse.

If $g_{n-1}$ is not in the pair, $g_{n-1} \to 0$ and $\sum g_i g_{i+1} \to 1/4$. $T \to n - 3/4$. Best.

So with one $m_i = 1$, the best is $n - 3/4$.

Now, can we do better with a completely different approach? What if we don't use the integer part at all (all $m_i = 0$)? Then $\sum f_i = n$ but $f_i < 1$ means $\sum f_i < n$, contradiction. So we need at least one $m_i \geq 1$.

What if we use a fractional $m$... no, $m_i$ are integers.

So the question is: what's the optimal number and placement of integer parts?

With $M = \sum m_i$ (total integer part), $\sum f_i = n - M$, and the total is:
$T = \sum f_i m_{i+1} + \sum f_i f_{i+1}$

The second term: $\sum f_i f_{i+1} \leq ?$ with $\sum f_i = n - M$, $f_i < 1$.

Using $g_i = 1 - f_i$, $\sum g_i = M$:
$\sum f_i f_{i+1} = n - 2M + \sum g_i g_{i+1}$.

The first term: $\sum f_i m_{i+1}$. This depends on the placement of $m_i$.

$T = \sum f_i m_{i+1} + n - 2M + \sum g_i g_{i+1}$
$= \sum (1 - g_i) m_{i+1} + n - 2M + \sum g_i g_{i+1}$
$= \sum m_{i+1} - \sum g_i m_{i+1} + n - 2M + \sum g_i g_{i+1}$
$= M - \sum g_i m_{i+1} + n - 2M + \sum g_i g_{i+1}$
$= n - M - \sum g_i m_{i+1} + \sum g_i g_{i+1}$

So $T = n - M + \sum g_i (g_{i+1} - m_{i+1})$.

We want to maximize $T = n - M + \sum g_i (g_{i+1} - m_{i+1})$ with $\sum g_i = M$, $g_i \in (0, 1]$, $m_i \geq 0$ integer, $\sum m_i = M$.

Note that $g_{i+1} - m_{i+1} \leq g_{i+1} \leq 1$ and $g_{i+1} - m_{i+1} \geq -m_{i+1}$.

To maximize, we want $g_{i+1} - m_{i+1}$ to be large where $g_i$ is large. $g_{i+1} - m_{i+1}$ is large when $m_{i+1} = 0$ and $g_{i+1}$ is close to 1, or when $m_{i+1}$ is small.

But we also want $M$ to be small (since $n - M$ decreases with $M$). The minimum $M$ is 1 (since $\sum f_i < n$ requires $M \geq 1$).

With $M = 1$: $T = n - 1 + \sum g_i (g_{i+1} - m_{i+1})$.

If $m_n = 1$, rest 0: $T = n - 1 + \sum g_i g_{i+1} - g_{n-1} \cdot 1 = n - 1 + \sum g_i g_{i+1} - g_{n-1}$.

This is what we had before. Max is $n - 1 + 1/4 = n - 3/4$ (with $g_{n-1} \to 0$, $g_1 = g_2 = 1/2$).

With $M = 2$: $T = n - 2 + \sum g_i (g_{i+1} - m_{i+1})$.

If $m_n = 2$: $T = n - 2 + \sum g_i g_{i+1} - 2g_{n-1}$. Max: $\sum g_i g_{i+1} \leq ?$ with $\sum g_i = 2$.

Max of $\sum g_i g_{i+1}$ with $\sum g_i = 2$, $g_i \in (0, 1]$: concentrate on two adjacent, $g_1 = g_2 = 1$, giving $1$. With $g_{n-1} \to 0$: $T \to n - 2 + 1 = n - 1$. Less than $n - 3/4$.

If $m_n = m_k = 1$: $T = n - 2 + \sum g_i g_{i+1} - g_{n-1} - g_{k-1}$. Max with $g_{n-1}, g_{k-1} \to 0$ and $\sum g_i g_{i+1} \to 1$: $T \to n - 1$. Same.

So $M = 1$ is optimal, giving $T_{\max} = n - 3/4$.

But wait, I need to verify that $\sum g_i g_{i+1}$ can actually reach $1/4$ while $g_{n-1} \to 0$ and $\sum g_i = 1$. Yes: set $g_1 = 1/2, g_2 = 1/2$, all other $g_i \to 0$. Then $\sum g_i g_{i+1} = g_1 g_2 = 1/4$ and $g_{n-1} \to 0$. But we need $g_i > 0$ for all $i$ (since $f_i < 1$). So we set $g_3 = \ldots = g_n = \epsilon$ and $g_1 = 1/2 - (n-2)\epsilon/2$, $g_2 = 1/2 - (n-2)\epsilon/2$. As $\epsilon \to 0$, this works.

Actually wait, I need to be more careful. $\sum g_i = 1$ with $g_1 = g_2 = 1/2 - (n-2)\epsilon/2$ and $g_3 = \ldots = g_n = \epsilon$. Then $\sum g_i = 2(1/2 - (n-2)\epsilon/2) + (n-2)\epsilon = 1 - (n-2)\epsilon + (n-2)\epsilon = 1$. ✓

$\sum g_i g_{i+1} = g_1 g_2 + g_2 g_3 + \ldots + g_n g_1$. As $\epsilon \to 0$: $g_1 g_2 \to 1/4$, other terms $\to 0$. So $\sum g_i g_{i+1} \to 1/4$. ✓

$g_{n-1} = \epsilon \to 0$. ✓

So $T \to n - 1 + 1/4 - 0 = n - 3/4$.

But is this the supremum, or can we do better? Let me think about whether there's a smarter configuration.

What if instead of concentrating $g$ on two adjacent, we use a different pattern? The key formula is:
$T = n - 1 + \sum g_i g_{i+1} - g_{n-1}$ (with $m_n = 1$).

We want to maximize $\sum g_i g_{i+1} - g_{n-1}$ with $\sum g_i = 1$, $g_i \in (0, 1]$.

Let's think of this as: maximize $\sum g_i g_{i+1} - g_{n-1}$.

If we put $g_{n-1} = 0$ (limit), then we maximize $\sum_{i \neq n-1} g_i g_{i+1}$ with $\sum_{i \neq n-1} g_i = 1$. But $g_{n-2} g_{n-1} = 0$ and $g_{n-1} g_n = 0$, so the sum is over the path $1, 2, \ldots, n-2, n$ (with $g_{n-2} g_n$ being a term if $n-2$ and $n$ are adjacent, which they're not in the cycle... wait, in the cycle, $n$ is adjacent to $n-1$ and $1$. So with $g_{n-1} = 0$, the terms are $g_1 g_2, g_2 g_3, \ldots, g_{n-3} g_{n-2}, g_{n-2} \cdot 0, 0 \cdot g_n, g_n g_1$. So the nonzero terms form a path: $g_n g_1, g_1 g_2, \ldots, g_{n-3} g_{n-2}$.

This is a path graph on $n-1$ vertices (vertices $n, 1, 2, \ldots, n-2$). The maximum of $\sum g_i g_{i+1}$ on a path with $\sum g_i = 1$ is $1/4$ (concentrate on any edge). So the max is $1/4$, confirming our result.

So $\lambda(n) = n - 3/4$ for $n \geq 4$? Let me double-check with $n = 4$:

$\lambda(4) = 4 - 3/4 = 13/4 = 3.25$.

Earlier I computed the supremum as $13/4$ for $n = 4$. ✓

But wait, I should also check: is the supremum actually achieved, or just approached? If it's not achieved, then $\lambda(n) = n - 3/4$ works as an upper bound (since the sum is always $< n - 3/4 \leq n - 3/4$). But we need to check that the sum can get arbitrarily close to $n - 3/4$, which it can (as shown above).

Hmm, but actually I need to be more careful. The problem says "the inequality $\leq \lambda(n)$ always holds." If the supremum is $n - 3/4$ and it's not achieved, then $\lambda(n) = n - 3/4$ works (since the sum is always $< n - 3/4$, hence $\leq n - 3/4$). And any $\lambda < n - 3/4$ would fail (since we can get arbitrarily close). So $\lambda(n) = n - 3/4$.

But wait, I assumed the constraint is $\sum a_i = n$. I'm not sure about this. Let me reconsider.

Actually, I just realized: maybe the problem has no constraint and the answer involves the fractional parts in a way that makes it bounded. Let me re-read.

"for any non-negative real numbers $a_1, a_2, \ldots, a_n$"

If there's truly no constraint, the sum $\sum \{a_i\} a_{i+1}$ is unbounded (set $a_1 = 0.5, a_2 = M$ for large $M$, rest 0; then $\{a_1\} a_2 = 0.5M \to \infty$).

So there MUST be a constraint. The most natural one that makes the problem interesting and $n$-dependent is $\sum a_i = n$ (or equivalently, the average is 1).

Actually, wait. I just thought of another possibility. What if the problem is about $a_i \in [0, 1)$ (i.e., the $a_i$ are already in $[0,1)$, so $\{a_i\} = a_i$), and the constraint is $\sum a_i = 1$? Then we're maximizing $\sum a_i a_{i+1}$ with $\sum a_i = 1$, $a_i \in [0, 1)$. The answer is $1/4$ for all $n \geq 3$.

But the problem says "non-negative real numbers," not "numbers in $[0,1)$." And it uses $\{a_i\}$, suggesting the $a_i$ can be larger than 1.

I'll go with $\sum a_i = n$ as the constraint. But actually, I realize I should also consider $\sum a_i = 1$ with $a_i$ being general non-negative reals (not restricted to $[0,1]$). With $\sum a_i = 1$ and $a_i \geq 0$, we still have $a_i \leq 1$, so $\{a_i\} = a_i$ (unless $a_i = 1$). So the answer is $1/4$.

Hmm, but what if the constraint is $\sum a_i = 1$ and the $a_i$ can be any non-negative reals? Then $a_i \in [0, 1]$ and $\{a_i\} = a_i$ for $a_i < 1$, $\{a_i\} = 0$ for $a_i = 1$. The maximum of $\sum \{a_i\} a_{i+1}$ is $1/4$ (achieved at $a_1 = a_2 = 1/2$).

OK so with $\sum a_i = 1$, the answer is $1/4$ regardless of $n$. The problem asks for $\lambda(n)$ with $n \geq 4$, which could just be the constant $1/4$.

But competition problems usually have more interesting answers. Let me think about whether there's a constraint that gives an $n$-dependent answer.

What if the constraint is $\sum a_i^2 = 1$? Then $a_i \in [0, 1]$ and $\{a_i\} = a_i$ (mostly). The maximum of $\sum a_i a_{i+1}$ with $\sum a_i^2 = 1$ is... by the spectral method, $\sum a_i a_{i+1} = \frac{1}{2} a^T A a$ where $A$ is the cycle adjacency matrix. The maximum of $a^T A a$ with $\|a\| = 1$ and $a \geq 0$ is the largest eigenvalue of $A$ restricted to the non-negative orthant. The largest eigenvalue of the cycle adjacency matrix is 2 (eigenvector all 1s), but that gives $\sum a_i a_{i+1} = \frac{1}{2} \cdot 2 = 1$ with $a_i = 1/\sqrt{n}$. So the answer would be 1 for all $n$. Not interesting.

What about $\sum a_i = 1$ with $a_i \geq 0$ and the objective is $\sum \{a_i\} a_{i+1}^2$ or something? No, the problem clearly states $\sum \{a_i\} a_{i+1}$.

Let me try another common constraint: $\prod a_i = 1$ or $\sum a_i \leq n$ or $\max a_i \leq 1$.

If $\max a_i \leq 1$ (i.e., $a_i \in [0, 1]$): then $\{a_i\} = a_i$ for $a_i < 1$ and $\{a_i\} = 0$ for $a_i = 1$. The supremum of $\sum a_i a_{i+1}$ with $a_i \in [0, 1)$ is $n$ (all $a_i \to 1$). But $\{a_i\} = a_i$ when $a_i < 1$, so $\sum \{a_i\} a_{i+1} \to n$. So $\lambda(n) = n$? But that's trivially achieved in the limit.

Hmm, that doesn't seem right either. With $a_i \in [0, 1]$, $\{a_i\} = a_i$ for $a_i < 1$ and $0$ for $a_i = 1$. So $\sum \{a_i\} a_{i+1} < n$ (strictly, since not all can be 1 and have nonzero fractional parts). The supremum is $n$ but not achieved. So $\lambda(n) = n$.

But that's too simple and doesn't really use the fractional part in an interesting way.

OK, I think the most likely constraint, given that the answer should depend on $n$ and involve fractional parts nontrivially, is $\sum a_i = n$. Let me also consider $\sum a_i \leq n$.

With $\sum a_i \leq n$: the maximum is the same as $\sum a_i = n$ (since increasing $a_i$ can only increase the sum, as long as fractional parts don't decrease). Actually, increasing $a_i$ might decrease $\{a_i\}$ (when crossing an integer). So it's not monotone. But the supremum over $\sum a_i \leq n$ should be the same as over $\sum a_i = n$ (we can always adjust).

Let me also consider: maybe the problem is stated correctly without a constraint, but the $a_i$ are assumed to be in $[0, 1)$ (so $\{a_i\} = a_i$), and the constraint is $\sum a_i = 1$. Then the answer is $1/4$ for all $n \geq 3$. The problem says $n \geq 4$ perhaps because for $n = 2$ or $n = 3$ the answer is different.

For $n = 2$: $\sum a_i a_{i+1} = a_1 a_2 + a_2 a_1 = 2a_1 a_2$ with $a_1 + a_2 = 1$. Max at $a_1 = a_2 = 1/2$: $2 \cdot 1/4 = 1/2$.

For $n = 3$: $a_1 a_2 + a_2 a_3 + a_3 a_1$ with $a_1 + a_2 + a_3 = 1$. Max at $a_1 = a_2 = 1/2, a_3 = 0$: $1/4$. Or at $a_1 = a_2 = a_3 = 1/3$: $3 \cdot 1/9 = 1/3 < 1/4$.

Wait, $1/3 < 1/4$? No, $1/3 > 1/4$. So for $n = 3$, the uniform distribution gives $1/3 > 1/4$.

Hmm, so for $n = 3$, the maximum of $\sum a_i a_{i+1}$ with $\sum a_i = 1$ is $1/3$ (at uniform), not $1/4$.

Let me recalculate. For $n = 3$, $\sum a_i a_{i+1} = a_1 a_2 + a_2 a_3 + a_3 a_1$ (since the cycle on 3 vertices is a triangle). With $a_1 + a_2 + a_3 = 1$:
$a_1 a_2 + a_2 a_3 + a_3 a_1 = \frac{(a_1 + a_2 + a_3)^2 - (a_1^2 + a_2^2 + a_3^2)}{2} = \frac{1 - \sum a_i^2}{2}$.

Maximized when $\sum a_i^2$ is minimized, i.e., $a_1 = a_2 = a_3 = 1/3$. Then $\sum a_i a_{i+1} = \frac{1 - 1/3}{2} = 1/3$.

For $n = 4$: $\sum a_i a_{i+1} = a_1 a_2 + a_2 a_3 + a_3 a_4 + a_4 a_1$. With $\sum a_i = 1$:
At uniform $a_i = 1/4$: $4 \cdot 1/16 = 1/4$.
At $a_1 = a_2 = 1/2, a_3 = a_4 = 0$: $1/4 + 0 + 0 + 0 = 1/4$.
At $a_1 = a_3 = 1/2, a_2 = a_4 = 0$: $0 + 0 + 0 + 0 = 0$.

So for $n = 4$, the max is $1/4$.

For $n = 5$: At uniform $a_i = 1/5$: $5 \cdot 1/25 = 1/5$. At $a_1 = a_2 = 1/2$: $1/4$. So $1/4 > 1/5$, and the max is $1/4$.

So for $n \geq 4$, the max of $\sum a_i a_{i+1}$ with $\sum a_i = 1$ is $1/4$ (concentrate on two adjacent). For $n = 3$, it's $1/3$ (uniform). For $n = 2$, it's $1/2$.

So the problem specifies $n \geq 4$ because for $n \geq 4$, the answer is $1/4$ (constant), while for smaller $n$ it's different. This makes sense!

But wait, with $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \leq 1$, so $\{a_i\} = a_i$ (unless $a_i = 1$). The maximum of $\sum \{a_i\} a_{i+1}$ is the same as $\sum a_i a_{i+1}$, which is $1/4$ for $n \geq 4$.

But the problem uses $\{a_i\}$ (fractional part), which is only different from $a_i$ when $a_i \geq 1$. With $\sum a_i = 1$, this never happens (except $a_i = 1$ which gives $\{a_i\} = 0$). So the fractional part is irrelevant, and the problem reduces to maximizing $\sum a_i a_{i+1}$.

This seems too simple for a competition problem. The use of fractional parts suggests the $a_i$ can be larger than 1, which means the constraint is probably $\sum a_i = n$ (or similar).

Let me go with $\sum a_i = n$ and the answer $\lambda(n) = n - \frac{3}{4}$.

Actually wait, I want to double-check this more carefully. Let me verify for $n = 4$ with a concrete near-optimal example.

$n = 4$, $m_4 = 1$, $g_1 = g_2 = 1/2 - \epsilon$, $g_3 = g_4 = \epsilon$ (approximately). Then:
$f_1 = 1/2 + \epsilon, f_2 = 1/2 + \epsilon, f_3 = 1 - \epsilon, f_4 = 1 - \epsilon$.
$a_1 = 0 + f_1 = 1/2 + \epsilon$
$a_2 = 0 + f_2 = 1/2 + \epsilon$
$a_3 = 0 + f_3 = 1 - \epsilon$
$a_4 = 1 + f_4 = 2 - \epsilon$

Check: $\sum a_i = 1/2 + \epsilon + 1/2 + \epsilon + 1 - \epsilon + 2 - \epsilon = 4$. ✓

$\{a_1\} = 1/2 + \epsilon, \{a_2\} = 1/2 + \epsilon, \{a_3\} = 1 - \epsilon, \{a_4\} = 1 - \epsilon$.

$\sum \{a_i\} a_{i+1} = (1/2 + \epsilon)(1/2 + \epsilon) + (1/2 + \epsilon)(1 - \epsilon) + (1 - \epsilon)(2 - \epsilon) + (1 - \epsilon)(1/2 + \epsilon)$

$= 1/4 + \epsilon + \epsilon^2 + 1/2 - \epsilon/2 + \epsilon - \epsilon^2 + 2 - 3\epsilon + \epsilon^2 + 1/2 + \epsilon - \epsilon/2 - \epsilon^2$

Let me compute term by term:
- $(1/2 + \epsilon)(1/2 + \epsilon) = 1/4 + \epsilon + \epsilon^2$
- $(1/2 + \epsilon)(1 - \epsilon) = 1/2 - \epsilon/2 + \epsilon - \epsilon^2 = 1/2 + \epsilon/2 - \epsilon^2$
- $(1 - \epsilon)(2 - \epsilon) = 2 - 3\epsilon + \epsilon^2$
- $(1 - \epsilon)(1/2 + \epsilon) = 1/2 + \epsilon - \epsilon/2 - \epsilon^2 = 1/2 + \epsilon/2 - \epsilon^2$

Sum = $1/4 + \epsilon + \epsilon^2 + 1/2 + \epsilon/2 - \epsilon^2 + 2 - 3\epsilon + \epsilon^2 + 1/2 + \epsilon/2 - \epsilon^2$
$= 1/4 + 1/2 + 2 + 1/2 + \epsilon + \epsilon/2 - 3\epsilon + \epsilon/2 + \epsilon^2 - \epsilon^2 + \epsilon^2 - \epsilon^2$
$= 13/4 + (1 + 1/2 - 3 + 1/2)\epsilon + 0$
$= 13/4 + (-1)\epsilon$
$= 13/4 - \epsilon$

As $\epsilon \to 0$, this approaches $13/4 = 3.25$. ✓

But wait, I need $g_3 = \epsilon$ and $g_4 = \epsilon$, but I said $g_1 = g_2 = 1/2 - \epsilon$ and $g_3 = g_4 = \epsilon$. Then $\sum g_i = 2(1/2 - \epsilon) + 2\epsilon = 1$. ✓ And $g_{n-1} = g_3 = \epsilon \to 0$. ✓

But $g_4 = \epsilon$ means $f_4 = 1 - \epsilon$, and $m_4 = 1$, so $a_4 = 2 - \epsilon$. And $g_3 = \epsilon$ means $f_3 = 1 - \epsilon$, $m_3 = 0$, $a_3 = 1 - \epsilon$.

Hmm, but I need $g_{n-1} = g_3 \to 0$ for the formula to work. In my example, $g_3 = \epsilon \to 0$. ✓

So the sum approaches $13/4$ from below. The supremum is $13/4$ but not achieved. So $\lambda(4) = 13/4$.

For general $n \geq 4$: $\lambda(n) = n - 3/4$.

Hmm wait, but I should double-check that we can't do better. Let me think about whether a different placement of the integer part could help.

With $m_n = 1$, the formula is $T = n - 1 + \sum g_i g_{i+1} - g_{n-1}$.

The key is that we lose $g_{n-1}$ (the $g$ value just before the integer part). What if we place the integer part at a position where the "loss" is smaller?

By symmetry of the cycle, the position of the single integer part doesn't matter—the loss is always $g_{k-1}$ where $k$ is the position. And we can always make $g_{k-1} \to 0$ by concentrating the $g$ mass elsewhere. So the supremum is always $n - 1 + 1/4 = n - 3/4$.

But what if we use a more clever strategy? For instance, what if we don't concentrate $g$ on just two adjacent variables?

The maximum of $\sum g_i g_{i+1}$ with $\sum g_i = 1$ on a cycle of length $n \geq 4$ is $1/4$ (concentrate on one edge). This is because $\sum g_i g_{i+1} \leq \frac{1}{2}\sum g_i(g_{i-1} + g_{i+1}) \leq \frac{1}{2}\sum g_i \cdot \max(g_{i-1} + g_{i+1})$... actually, let me think more carefully.

$\sum g_i g_{i+1} \leq \frac{1}{2} \sum (g_i^2 + g_{i+1}^2)/2 \cdot 2$... no, by AM-GM, $g_i g_{i+1} \leq (g_i + g_{i+1})^2/4$. So $\sum g_i g_{i+1} \leq \sum (g_i + g_{i+1})^2/4$. But this doesn't directly help.

Actually, $\sum g_i g_{i+1} \leq \frac{(\sum g_i)^2}{4}$ when the graph is bipartite (which the cycle is for even $n$). For even $n$, the cycle is bipartite, and $\sum g_i g_{i+1} \leq \frac{(\sum_{\text{odd}} g_i)(\sum_{\text{even}} g_i)}{1} \cdot \ldots$ hmm, not exactly.

For a bipartite graph with parts $A$ and $B$: $\sum_{i \in A, j \in B, ij \in E} g_i g_j \leq (\sum_A g_i)(\sum_B g_j) \leq \frac{(\sum g_i)^2}{4} = 1/4$.

For even $n$, the cycle is bipartite, so $\sum g_i g_{i+1} \leq 1/4$. ✓

For odd $n$, the cycle is not bipartite. But we can still bound it. $\sum g_i g_{i+1} \leq ?$

For odd $n$, the maximum of $\sum g_i g_{i+1}$ with $\sum g_i = 1$, $g_i \geq 0$ is still $1/4$ for $n \geq 5$. Here's why: concentrate on two adjacent vertices, $g_1 = g_2 = 1/2$, rest 0. Then $\sum g_i g_{i+1} = 1/4$. Can we do better?

For $n = 5$: try $g_1 = g_2 = g_3 = 1/3$. $\sum g_i g_{i+1} = g_1 g_2 + g_2 g_3 + g_3 g_4 + g_4 g_5 + g_5 g_1 = 1/9 + 1/9 + 0 + 0 + 0 = 2/9 < 1/4$.

Try $g_1 = a, g_2 = b, g_3 = c$, rest 0, $a + b + c = 1$. $\sum = ab + bc = b(a+c) = b(1-b)$. Max at $b = 1/2$: $1/4$. Same.

So for $n \geq 4$ (both even and odd), the max of $\sum g_i g_{i+1}$ with $\sum g_i = 1$ is $1/4$.

Therefore, $\lambda(n) = n - 3/4$ for all $n \geq 4$.

But wait, I should also consider whether we can do better by NOT using the $g$-concentration strategy. What if we use a different $M$ or different placement?

I showed that with $M = 1$, the supremum is $n - 3/4$. With $M = 2$, it's $n - 1 < n - 3/4$. With $M \geq 2$, the supremum is $n - M + \text{something} \leq n - M + M/4 \cdot \ldots$ hmm, let me think more generally.

With general $M$: $T = n - M + \sum g_i(g_{i+1} - m_{i+1})$.

$\sum g_i(g_{i+1} - m_{i+1}) \leq \sum g_i g_{i+1} \leq M^2/4$ (by the bipartite bound, $\sum g_i g_{i+1} \leq (\sum g_i)^2/4 = M^2/4$ for even $n$; for odd $n \geq 5$, same bound holds as shown).

Wait, actually $\sum g_i g_{i+1} \leq (\sum g_i)^2/4 = M^2/4$ only for bipartite graphs. For non-bipartite (odd cycles), the bound might be different.

For odd $n$: $\sum g_i g_{i+1}$ with $\sum g_i = M$. The maximum is... for $n = 5$, $M = 1$: $1/4$. For $M = 2$: concentrate on two adjacent, $g_1 = g_2 = 1$, $\sum g_i g_{i+1} = 1 = M^2/4 = 1$. ✓

Actually for any $n \geq 4$, $\sum g_i g_{i+1} \leq M^2/4$ (concentrate on one edge). This is because the cycle $C_n$ for $n \geq 4$ has the property that the max of $\sum g_i g_{i+1}$ with $\sum g_i = M$ is $M^2/4$ (put $M/2$ on each of two adjacent vertices).

So $T \leq n - M + M^2/4 - \sum g_i m_{i+1}$.

And $\sum g_i m_{i+1} \geq 0$, so $T \leq n - M + M^2/4$.

Maximize $n - M + M^2/4$ over $M \geq 1$: $f(M) = n - M + M^2/4$, $f'(M) = -1 + M/2 = 0 \Rightarrow M = 2$. $f(2) = n - 2 + 1 = n - 1$. $f(1) = n - 1 + 1/4 = n - 3/4$.

Since $f(1) = n - 3/4 > n - 1 = f(2)$ for all $n$, and $f$ is convex (minimized at $M = 2$), the maximum over $M \geq 1$ is at $M = 1$: $f(1) = n - 3/4$.

But wait, this upper bound $T \leq n - M + M^2/4$ might not be tight because we also have the $-\sum g_i m_{i+1}$ term. Let me reconsider.

$T = n - M + \sum g_i g_{i+1} - \sum g_i m_{i+1}$.

With $M = 1$, $m_k = 1$ for some $k$: $T = n - 1 + \sum g_i g_{i+1} - g_{k-1}$.

We showed the max is $n - 1 + 1/4 = n - 3/4$ (by making $g_{k-1} \to 0$ and concentrating $g$ on an edge not involving $k-1$).

With $M = 2$: we could have $m_k = 2$ or $m_k = m_j = 1$.

Case $m_k = 2$: $T = n - 2 + \sum g_i g_{i+1} - 2g_{k-1}$. Max: $\sum g_i g_{i+1} \leq 1$ (with $\sum g_i = 2$), $g_{k-1} \to 0$: $T \to n - 2 + 1 = n - 1$.

Case $m_k = m_j = 1$ ($k \neq j$): $T = n - 2 + \sum g_i g_{i+1} - g_{k-1} - g_{j-1}$. Max: $\sum g_i g_{i+1} \leq 1$, $g_{k-1}, g_{j-1} \to 0$: $T \to n - 1$.

Both give $n - 1 < n - 3/4$.

For $M \geq 3$: $T \leq n - M + M^2/4$. $f(3) = n - 3 + 9/4 = n - 3/4$. Same as $M = 1$!

But can we achieve $n - 3/4$ with $M = 3$? We need $\sum g_i g_{i+1} = M^2/4 = 9/4$ and $\sum g_i m_{i+1} = 0$.

$\sum g_i g_{i+1} = 9/4$ with $\sum g_i = 3$: concentrate on two adjacent, $g_1 = g_2 = 3/2$. But $g_i \leq 1$! So this is infeasible.

With $g_i \leq 1$: $\sum g_i g_{i+1} \leq ?$ with $\sum g_i = 3$, $g_i \leq 1$.

If $g_1 = g_2 = 1, g_3 = 1$, rest 0: $\sum g_i g_{i+1} = 1 + 1 + 0 + \ldots = 2$ (for $n \geq 5$; the terms $g_1 g_2 + g_2 g_3 = 1 + 1 = 2$).

Actually for $n = 4$: $g_1 = g_2 = g_3 = 1, g_4 = 0$: $\sum = g_1 g_2 + g_2 g_3 + g_3 g_4 + g_4 g_1 = 1 + 1 + 0 + 0 = 2$.

So $\sum g_i g_{i+1} \leq 2$ with $\sum g_i = 3$, $g_i \leq 1$. (Concentrate on a path of 3 vertices.)

$T \leq n - 3 + 2 - \sum g_i m_{i+1} \leq n - 1$. Less than $n - 3/4$.

What about $M = 3$ with $g_1 = g_2 = 1, g_3 = 1$, and $m$ placed so that $\sum g_i m_{i+1} = 0$? We need $m_{i+1} = 0$ whenever $g_i > 0$, i.e., $m_2 = m_3 = m_4 = 0$ (since $g_1, g_2, g_3 > 0$). So $m_1 = 3$ (all integer mass at position 1). Then $\sum g_i m_{i+1} = g_4 \cdot m_1 = 0 \cdot 3 = 0$ (since $g_4 = 0$). But $g_4 = 0$ means $f_4 = 1$, which violates $f_i < 1$.

So we need $g_4 > 0$, meaning $\sum g_i m_{i+1} > 0$ if $m_1 > 0$. Specifically, $\sum g_i m_{i+1} = g_4 \cdot m_1 = g_4 \cdot 3 > 0$.

So $T = n - 3 + 2 - 3g_4 < n - 1$. As $g_4 \to 0$, $T \to n - 1$. Still less than $n - 3/4$.

So $M = 1$ is indeed optimal, giving $\lambda(n) = n - 3/4$.

Hmm, but I realize I should also check: is the bound $\sum g_i g_{i+1} \leq 1/4$ with $\sum g_i = 1$ tight for the cycle? Yes, as shown: $g_1 = g_2 = 1/2$ gives $1/4$.

And we need $g_{k-1} \to 0$ while concentrating on $g_1, g_2$. For $n \geq 4$, we can choose $k$ such that $k - 1 \notin \{1, 2\}$ (i.e., $k \neq 2, 3$). For $n \geq 4$, this is possible. For $n = 4$, $k = 4$ gives $k - 1 = 3 \notin \{1, 2\}$. ✓

So the answer is $\lambda(n) = n - \frac{3}{4}$ for $n \geq 4$.

Wait, but I need to double-check that the supremum is not achieved (so that $\leq$ holds). In our construction, $g_{k-1} = \epsilon > 0$ and the sum is $n - 3/4 - \epsilon < n - 3/4$. As $\epsilon \to 0$, it approaches $n - 3/4$ but never reaches it. So $\sum \{a_i\} a_{i+1} < n - 3/4$ always, hence $\leq n - 3/4$ holds. And for any $\lambda < n - 3/4$, we can find $a_i$ with $\sum \{a_i\} a_{i+1} > \lambda$. So $\lambda(n) = n - 3/4$.

Actually, hold on. I need to verify that the supremum is exactly $n - 3/4$ and not something else. Let me also check: can we achieve exactly $n - 3/4$?

At $\epsilon = 0$: $g_1 = g_2 = 1/2$, $g_3 = g_4 = \ldots = g_n = 0$. But $g_i = 0$ means $f_i = 1$, which is not allowed ($f_i < 1$). So the supremum is not achieved.

But actually, can we have $f_i = 1$? No, because $\{a_i\} \in [0, 1)$. So $f_i < 1$ always, meaning $g_i > 0$ always. The supremum $n - 3/4$ is not achieved, but it's the least upper bound. So $\lambda(n) = n - 3/4$.

Hmm, but I want to make sure I haven't made an error. Let me re-examine the formula.

$T = n - M + \sum g_i(g_{i+1} - m_{i+1})$ where $g_i = 1 - f_i$, $\sum g_i = M$.

With $M = 1$, $m_n = 1$:
$T = n - 1 + \sum g_i g_{i+1} - g_{n-1} \cdot m_n = n - 1 + \sum g_i g_{i+1} - g_{n-1}$.

Wait, $\sum g_i m_{i+1} = g_{n-1} \cdot m_n + \text{other terms with } m_{i+1} = 0 = g_{n-1} \cdot 1 = g_{n-1}$.

So $T = n - 1 + \sum g_i g_{i+1} - g_{n-1}$. ✓

With $g_1 = g_2 = 1/2 - (n-2)\epsilon/2$, $g_3 = \ldots = g_n = \epsilon$:

$\sum g_i = 2(1/2 - (n-2)\epsilon/2) + (n-2)\epsilon = 1 - (n-2)\epsilon + (n-2)\epsilon = 1$. ✓

$\sum g_i g_{i+1} = g_1 g_2 + g_2 g_3 + g_3 g_4 + \ldots + g_{n-1} g_n + g_n g_1$

$= (1/2 - (n-2)\epsilon/2)^2 + (1/2 - (n-2)\epsilon/2)\epsilon + \epsilon^2(n-3) + \epsilon \cdot (1/2 - (n-2)\epsilon/2) + \ldots$

As $\epsilon \to 0$: $\sum g_i g_{i+1} \to 1/4$. $g_{n-1} = \epsilon \to 0$.

$T \to n - 1 + 1/4 = n - 3/4$. ✓

Now let me also verify that we can't exceed $n - 3/4$.

$T = n - 1 + \sum g_i g_{i+1} - g_{n-1} \leq n - 1 + \sum g_i g_{i+1}$.

And $\sum g_i g_{i+1} \leq 1/4$ (with $\sum g_i = 1$ on a cycle of length $\geq 4$).

But we also subtract $g_{n-1} \geq 0$. So $T \leq n - 1 + 1/4 = n - 3/4$.

But this bound might not be tight because to achieve $\sum g_i g_{i+1} = 1/4$, we need $g_1 = g_2 = 1/2$ and all others 0, but then $g_{n-1} = 0$, which is fine (it's the limit). So the bound is tight in the limit.

Actually, I realize I need to be more careful. The bound $\sum g_i g_{i+1} \leq 1        — AI历史解题过程（thinking）
#   polymath_01413         — 题目ID

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
  <problem_id>polymath_01413</problem_id>
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

The 34th question: Given an integer $n \geq 4$, find the smallest $\lambda(n)$ such that for any non-negative real numbers $a_{1}, a_{2}, \ldots, a_{n}$ (indices taken modulo $n$), the inequality $\sum_{i=1}^{n}\left\{a_{i}\right\} a_{i+1} \leq \lambda(n)$ always holds.

## Standard Solution

The 34th question,
Solution: We first prove a lemma: Let the integer $\mathrm{n} \geq 4$, real numbers $r_{i} \in[0,1](1 \leq \mathrm{i} \leq \mathrm{n})$, satisfy $\sum_{i=1}^{n} r_{i}=r$, where $r \in \mathbb{N}$, and $r \leq n-1$, then $\sum_{i=1}^{n} r_{i} r_{i+1} \leq r-\frac{3}{4}$.
Proof of the lemma: If $\mathrm{r}=0$, the conclusion is obviously true. Now assume $\mathrm{r} \in \mathbb{Z}^{+}$.
Let $f\left(r_{1}, r_{2}, \ldots, r_{n}\right)=\sum_{i=1}^{n} r_{i} r_{i+1}$, then $f$ is a continuous function defined on a bounded closed set, so there exists a maximum value $S$.

Without loss of generality, assume that $f$ achieves $S$ at $\left(r_{1}, r_{2}, \ldots, r_{n}\right)$, and that $r_{1}, r_{2}, \ldots, r_{n}$ contain the maximum number of 0s and 1s. We will prove: for any two non-adjacent $r_{i}, r_{j}$ (non-adjacent means $i-j \neq \pm 1 (\bmod n)$), one of $r_{i}, r_{j}$ must be 0 or 1.

In fact, for any two non-adjacent $r_{i}, r_{j}$. Let $t=r_{i}+r_{j}$, and let $x=r_{i}$, then $\sum_{i=1}^{n} r_{i} r_{i+1}$ is a linear function of $x$. Therefore, when $\sum_{i=1}^{n} r_{i} r_{i+1}$ achieves its maximum value, it must be that $x \in \{0, \min \{1, t\}\}$. This indicates that one of $r_{i}, r_{j}$ must be 0 or 1.

The above conclusion shows: among $r_{1}, r_{2}, \ldots, r_{n}$, at most two numbers do not belong to $\{0,1\}$, and these two numbers must be adjacent.
If $r_{1}, r_{2}, \ldots, r_{n}$ are all 0 or 1, then there are exactly $r$ ones, so $\sum_{i=1}^{n} r_{i} r_{i+1} \leq r-1$,
If $r_{1}, r_{2}, \ldots, r_{n}$ have two numbers not in $\{0,1\}$, without loss of generality, let these be $r_{1}, r_{2} \in (0,1)$, then the remaining $n-2$ numbers are all 0 or 1. Thus, $r_{1} + r_{2} = 1$, and among the remaining $n-2$ numbers, there are exactly $r-1$ ones. Therefore, $\sum_{i=1}^{n} r_{i} r_{i+1} \leq r_{1} r_{2} + r_{2} + r - 2 + r_{1} = r - 3 + (1 + r_{1})(1 + r_{2}) \leq r - 3 + \frac{[(1 + r_{1}) + (1 + r_{2})]^2}{4} = r - \frac{3}{4}$.

In summary, the lemma is proved. And it is easy to see that the equality holds only when $r=n-1, r_{1}=r_{2}=\frac{1}{2}, r_{3}=r_{4}=\ldots=r_{n}=1$.
Now let's return to the original problem.
Let $\left[a_{i}\right]=b_{i}, \left\{a_{i}\right\}=r_{i} (1 \leq i \leq n)$, and let $\sum_{i=1}^{n} r_{i}=r$, then $r \in \mathbb{N}$, and $r \leq n-1$. According to the lemma, we have:
$$
\begin{array}{l}
\sum_{i=1}^{n}\left\{a_{i}\right\} a_{i+1}=\sum_{i=1}^{n} r_{i}\left(b_{i+1}+r_{i+1}\right)=\sum_{i=1}^{n} r_{i} b_{i+1}+\sum_{i=1}^{n} r_{i} r_{i+1} \\
\leq \sum_{i=1}^{n} b_{i+1}+\sum_{i=1}^{n} r_{i} r_{i+1} \leq \sum_{i=1}^{n} b_{i+1}+\sum_{i=1}^{n} r_{i}-\frac{3}{4}=n-\frac{3}{4}
\end{array}
$$

On the other hand, we take $a_{1}=\frac{3}{2}+(n-2) \varepsilon, a_{2}=\frac{1}{2}, a_{3}=a_{4}=\ldots=a_{n}=1-\varepsilon$. Then let $\varepsilon \rightarrow 0^{+}$,
then
$$
\sum_{i=1}^{n}\left\{a_{i}\right\} a_{i+1}=\left(\frac{1}{2}+(n-2) \varepsilon\right) \cdot \frac{1}{2}+\frac{1}{2} \cdot(1-\varepsilon)+(n-3)(1-\varepsilon)^{2}+(1-\varepsilon) \cdot\left(\frac{3}{2}+(n-\right.
$$
2) $\varepsilon) \rightarrow n-\frac{3}{4}$
In summary, the minimum value of $\lambda(n)$ is $n-\frac{3}{4}$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We need to find the smallest $\lambda(n)$ such that for any non-negative real numbers $a_1, a_2, \ldots, a_n$ (indices mod $n$), we have:
$$\sum_{i=1}^{n}\{a_i\} a_{i+1} \leq \lambda(n)$$

where $\{a_i\}$ is the fractional part of $a_i$.

Wait, but this can't be bounded unless there's some constraint. If all $a_i$ can be arbitrarily large, then $\{a_i\}$ can be close to 1 and $a_{i+1}$ can be arbitrarily large, so the sum is unbounded.

Let me re-read the problem. "for any non-negative real numbers $a_1, a_2, \ldots, a_n$". Hmm, there must be an additional constraint. Let me think... maybe $\sum a_i = 1$ or something similar? Or maybe the constraint is that $\{a_i\}$ appears and there's a normalization.

Actually, wait. Let me reconsider. Perhaps the problem has a constraint like $\sum a_i = 1$ or $\sum a_i \leq 1$ or the $a_i$ are in $[0,1)$... but the problem says "non-negative real numbers" and uses fractional parts.

Hmm, actually if $a_i$ are non-negative reals with no constraint, the sum is unbounded. So there must be a missing constraint. Let me think about what's standard.

Actually, perhaps the constraint is $\sum a_i = 1$. This is a common type of problem. Let me assume $\sum_{i=1}^n a_i = 1$.

With $\sum a_i = 1$, we want to maximize $\sum \{a_i\} a_{i+1}$.

Since $a_i \geq 0$ and $\sum a_i = 1$, each $a_i \leq 1$, so $\{a_i\} = a_i$ (since $a_i \leq 1$ means $a_i < 2$... wait, $a_i$ could be exactly 1, then $\{a_i\} = 0$).

Actually if $\sum a_i = 1$ and $a_i \geq 0$, then $a_i \in [0,1]$. If $a_i = 1$ for some $i$, then all others are 0, and $\{a_i\} = 0$, so the sum is 0.

If all $a_i < 1$, then $\{a_i\} = a_i$, and the sum becomes $\sum a_i a_{i+1}$.

So the problem reduces to: maximize $\sum a_i a_{i+1}$ subject to $\sum a_i = 1$, $a_i \geq 0$, $a_i < 1$ (but we can take the sup over $a_i \leq 1$).

The maximum of $\sum a_i a_{i+1}$ subject to $\sum a_i = 1$, $a_i \geq 0$ is a known problem. By convexity arguments, the maximum is achieved when all mass is concentrated on two adjacent variables. If $a_1 = a_2 = 1/2$ and rest 0, then $\sum a_i a_{i+1} = a_1 a_2 + a_2 a_3 + \ldots = (1/2)(1/2) = 1/4$.

But wait, can we do better? If we put mass on $a_1 = t, a_2 = 1-t$, the sum is $t(1-t) + (1-t)\cdot 0 + 0 \cdot t = t(1-t)$, maximized at $t = 1/2$ giving $1/4$.

What about three consecutive? $a_1, a_2, a_3$ with $a_1 + a_2 + a_3 = 1$. Sum = $a_1 a_2 + a_2 a_3 + a_3 \cdot 0 + \ldots$. To maximize $a_1 a_2 + a_2 a_3 = a_2(a_1 + a_3) = a_2(1 - a_2)$, maximized at $a_2 = 1/2$ giving $1/4$, with $a_1 + a_3 = 1/2$.

So the maximum is $1/4$ regardless of $n \geq 4$? That seems too simple and doesn't depend on $n$.

Hmm, but the problem asks for $\lambda(n)$ depending on $n$. So maybe my assumption about the constraint is wrong.

Let me reconsider. Maybe the constraint is different. Perhaps $\sum a_i = n$ or $\sum \{a_i\} = 1$ or something else.

Actually, let me reconsider the problem. Maybe there's no sum constraint but rather the $a_i$ are in $[0,1]$? No, then $\{a_i\} = a_i$ and it's the same as maximizing $\sum a_i a_{i+1}$ with $a_i \in [0,1]$, which is unbounded (set all $a_i = 1$, get $n$).

Hmm wait, if $a_i \in [0,1]$, then $\sum a_i a_{i+1} \leq n$ with all $a_i = 1$. But $\{1\} = 0$, so actually $\{a_i\} = a_i$ only if $a_i < 1$. If $a_i = 1$, $\{a_i\} = 0$.

So if $a_i \in [0,1]$, the fractional part $\{a_i\} = a_i$ for $a_i < 1$ and $\{a_i\} = 0$ for $a_i = 1$. The supremum of $\sum \{a_i\} a_{i+1}$ with $a_i \in [0,1]$ would be approached by setting all $a_i$ close to 1 but not equal to 1, giving close to $n$. But that's not achieved, so $\lambda(n) = n$? That also seems odd.

Let me think again about what constraint makes this problem interesting and $n$-dependent.

Actually, maybe the problem is: $\sum a_i = 1$ but the $a_i$ are general non-negative reals (not necessarily $\leq 1$). Then $\{a_i\}$ can differ from $a_i$ when $a_i \geq 1$. But with $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \leq 1$, so $\{a_i\} = a_i$ (except when $a_i = 1$ exactly, where $\{a_i\} = 0$). So the problem is essentially maximize $\sum a_i a_{i+1}$ with $\sum a_i = 1$, $a_i \geq 0$, and the answer is $1/4$ for all $n \geq 3$.

This doesn't depend on $n$, which contradicts the problem asking for $\lambda(n)$.

Let me reconsider. Perhaps the constraint is $\sum a_i^2 = 1$ or $\sum a_i \leq n$ or the $a_i$ are integers... no, they're reals.

Actually, maybe I'm overcomplicating this. Let me re-read: "find the smallest $\lambda(n)$ such that for any non-negative real numbers $a_1, \ldots, a_n$, the inequality $\sum \{a_i\} a_{i+1} \leq \lambda(n)$ always holds."

Without any constraint, this is unbounded. So there MUST be a constraint that I'm missing, or the problem statement is incomplete, or there's a different interpretation.

Wait—maybe the constraint is that $\sum a_i = 1$? But as I showed, that gives $1/4$ for all $n$.

Or maybe $\sum \{a_i\} = 1$? That's an interesting constraint. Then we want to maximize $\sum \{a_i\} a_{i+1}$ subject to $\sum \{a_i\} = 1$ and $a_i \geq 0$.

With $\sum \{a_i\} = 1$, let $f_i = \{a_i\} \in [0,1)$. Then $\sum f_i = 1$ and $a_i = \lfloor a_i \rfloor + f_i$. We want to maximize $\sum f_i a_{i+1} = \sum f_i (\lfloor a_{i+1} \rfloor + f_{i+1})$.

Since $\lfloor a_{i+1} \rfloor$ can be any non-negative integer, this is still unbounded! Unless there's another constraint.

Hmm. Let me think about this differently. Maybe the problem is from a specific competition and has a specific constraint that got lost in translation.

Actually, let me reconsider. Perhaps the problem states that $a_1 + a_2 + \cdots + a_n = 1$ and the answer does depend on $n$ in a way I'm not seeing.

Wait, with $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \in [0,1]$. The only issue is when $a_i = 1$ exactly, $\{a_i\} = 0 \neq a_i$. So the function $\sum \{a_i\} a_{i+1}$ is NOT the same as $\sum a_i a_{i+1}$ when some $a_i = 1$.

But the maximum of $\sum a_i a_{i+1}$ over $\sum a_i = 1$, $a_i \geq 0$ is $1/4$, achieved at $a_1 = a_2 = 1/2$. At this point, $\{a_i\} = a_i$ for all $i$ (since $1/2 < 1$), so $\sum \{a_i\} a_{i+1} = 1/4$ as well.

So $\lambda(n) = 1/4$ for $n \geq 3$? But the problem says $n \geq 4$ and asks for $\lambda(n)$...

Unless the constraint is different. Let me try $\sum a_i = n$ (so average is 1). Then $a_i$ can be larger than 1, and $\{a_i\}$ can differ from $a_i$.

With $\sum a_i = n$, we want to maximize $\sum \{a_i\} a_{i+1}$.

Hmm, this is more interesting. Let me think about small cases.

For $n = 4$, $\sum a_i = 4$. We want to maximize $\{a_1\}a_2 + \{a_2\}a_3 + \{a_3\}a_4 + \{a_4\}a_1$.

If all $a_i = 1$, then $\{a_i\} = 0$ and the sum is 0.

If $a_1 = 1 + \epsilon, a_2 = 1 + \epsilon, a_3 = 1 - \epsilon, a_4 = 1 - \epsilon$ (sum = 4), then $\{a_1\} = \epsilon, \{a_2\} = \epsilon, \{a_3\} = 1 - \epsilon, \{a_4\} = 1 - \epsilon$ (for small $\epsilon > 0$). Sum = $\epsilon(1+\epsilon) + \epsilon(1-\epsilon) + (1-\epsilon)(1-\epsilon) + (1-\epsilon)(1+\epsilon) = \epsilon + \epsilon^2 + \epsilon - \epsilon^2 + 1 - 2\epsilon + \epsilon^2 + 1 - \epsilon^2 = 2$.

Hmm, that gives 2. Let me try to maximize further.

Actually, let me try: $a_1 = 2 - \epsilon, a_2 = 2 - \epsilon, a_3 = \epsilon, a_4 = \epsilon$ (sum = 4). Then $\{a_1\} = 1 - \epsilon, \{a_2\} = 1 - \epsilon, \{a_3\} = \epsilon, \{a_4\} = \epsilon$. Sum = $(1-\epsilon)(2-\epsilon) + (1-\epsilon)\epsilon + \epsilon \cdot \epsilon + \epsilon(2-\epsilon) = (2 - 3\epsilon + \epsilon^2) + (\epsilon - \epsilon^2) + \epsilon^2 + (2\epsilon - \epsilon^2) = 2 - 3\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + \epsilon^2 + 2\epsilon - \epsilon^2 = 2$.

Also 2. Let me try another configuration.

$a_1 = 3 - \epsilon, a_2 = 1 + \epsilon, a_3 = \epsilon, a_4 = \epsilon$ (sum = 4). $\{a_1\} = 1 - \epsilon$ (wait, $3 - \epsilon$ has integer part 2, so $\{a_1\} = 1 - \epsilon$). Hmm, $3 - \epsilon = 2 + (1 - \epsilon)$, so $\{a_1\} = 1 - \epsilon$. $\{a_2\} = \epsilon$. $\{a_3\} = \epsilon$. $\{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(1+\epsilon) + \epsilon \cdot \epsilon + \epsilon \cdot \epsilon + \epsilon(3-\epsilon) = (1 - \epsilon^2) + \epsilon^2 + \epsilon^2 + 3\epsilon - \epsilon^2 = 1 + 3\epsilon$.

As $\epsilon \to 0$, this approaches 1. Not as good.

Let me try: $a_1 = 1 - \epsilon, a_2 = 1 - \epsilon, a_3 = 1 - \epsilon, a_4 = 1 + 3\epsilon$ (sum = 4). $\{a_1\} = 1 - \epsilon, \{a_2\} = 1 - \epsilon, \{a_3\} = 1 - \epsilon, \{a_4\} = 3\epsilon$.

Sum = $(1-\epsilon)(1-\epsilon) + (1-\epsilon)(1-\epsilon) + (1-\epsilon)(1+3\epsilon) + 3\epsilon(1-\epsilon)$
$= (1 - 2\epsilon + \epsilon^2) + (1 - 2\epsilon + \epsilon^2) + (1 + 3\epsilon - \epsilon - 3\epsilon^2) + (3\epsilon - 3\epsilon^2)$
$= 1 - 2\epsilon + \epsilon^2 + 1 - 2\epsilon + \epsilon^2 + 1 + 2\epsilon - 3\epsilon^2 + 3\epsilon - 3\epsilon^2$
$= 3 + \epsilon - 4\epsilon^2$.

As $\epsilon \to 0$, approaches 3. Better!

Let me try all $a_i = 1 - \epsilon$ except one: $a_1 = a_2 = a_3 = 1 - \epsilon, a_4 = 1 + 3\epsilon$. Already did this, got approaching 3.

What about $a_1 = a_2 = a_3 = a_4 = 1 - \epsilon$? Sum = $4 - 4\epsilon \neq 4$. Need to adjust.

Let me try: $a_i = 1 - \epsilon$ for all $i$, but then sum = $4(1-\epsilon) = 4 - 4\epsilon$. To make sum = 4, we need to add $4\epsilon$ somewhere. If we add it to $a_4$: $a_4 = 1 + 3\epsilon$, as above.

What if we spread it: $a_1 = a_2 = 1 - \epsilon, a_3 = a_4 = 1 + \epsilon$. Sum = 4. $\{a_1\} = 1 - \epsilon, \{a_2\} = 1 - \epsilon, \{a_3\} = \epsilon, \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(1-\epsilon) + (1-\epsilon)(1+\epsilon) + \epsilon(1+\epsilon) + \epsilon(1-\epsilon)$
$= 1 - 2\epsilon + \epsilon^2 + 1 - \epsilon^2 + \epsilon + \epsilon^2 + \epsilon - \epsilon^2$
$= 2$.

Hmm, that's only 2. The issue is that when $a_i$ crosses an integer, the fractional part drops.

So the key insight is: to maximize, we want as many $a_i$ as possible to have fractional part close to 1 (i.e., $a_i$ just below an integer) and the next $a_{i+1}$ to be large.

With $\sum a_i = n$ and $n = 4$: if $a_1, a_2, a_3$ are just below 1 (fractional part $\approx 1$) and $a_4$ is just above 1 (fractional part $\approx 0$), we get contributions from $\{a_1\}a_2 + \{a_2\}a_3 + \{a_3\}a_4 \approx 1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 = 3$, and $\{a_4\}a_1 \approx 0$.

Can we do better? What if $a_1, a_2, a_3$ are just below 2 (fractional part $\approx 1$) and $a_4$ is large? But $\sum a_i = 4$, so if $a_1, a_2, a_3 \approx 2$, that's already 6 > 4. Not possible.

What about $a_1, a_2$ just below 2, $a_3, a_4$ small? $a_1 = a_2 = 2 - \epsilon, a_3 = a_4 = \epsilon$. Sum = 4. $\{a_1\} = \{a_2\} = 1 - \epsilon, \{a_3\} = \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(2-\epsilon) + (1-\epsilon)\epsilon + \epsilon \cdot \epsilon + \epsilon(2-\epsilon) = 2 - 3\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + \epsilon^2 + 2\epsilon - \epsilon^2 = 2$.

So 2, not as good as 3.

What about $a_1 = 1 - \epsilon, a_2 = 1 - \epsilon, a_3 = 1 - \epsilon, a_4 = 1 + 3\epsilon$? Got $\approx 3$.

Can we get more than 3? What about making some $a_i$ just below 2?

$a_1 = 2 - \epsilon, a_2 = 1 - \epsilon, a_3 = 1 - \epsilon, a_4 = \epsilon$. Sum = 4. $\{a_1\} = 1 - \epsilon, \{a_2\} = 1 - \epsilon, \{a_3\} = 1 - \epsilon, \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(1-\epsilon) + (1-\epsilon)(1-\epsilon) + (1-\epsilon)\epsilon + \epsilon(2-\epsilon)$
$= 1 - 2\epsilon + \epsilon^2 + 1 - 2\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + 2\epsilon - \epsilon^2$
$= 2 - \epsilon$.

Approaches 2. Worse.

$a_1 = 1 - \epsilon, a_2 = 2 - \epsilon, a_3 = 1 - \epsilon, a_4 = \epsilon$. Sum = 4. $\{a_1\} = 1-\epsilon, \{a_2\} = 1-\epsilon, \{a_3\} = 1-\epsilon, \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(2-\epsilon) + (1-\epsilon)(1-\epsilon) + (1-\epsilon)\epsilon + \epsilon(1-\epsilon)$
$= 2 - 3\epsilon + \epsilon^2 + 1 - 2\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + \epsilon - \epsilon^2$
$= 3 - 3\epsilon$.

Approaches 3. Same.

What about $a_1 = 1-\epsilon, a_2 = 1-\epsilon, a_3 = 2-\epsilon, a_4 = \epsilon$? Sum = 4.
$\{a_1\} = 1-\epsilon, \{a_2\} = 1-\epsilon, \{a_3\} = 1-\epsilon, \{a_4\} = \epsilon$.

Sum = $(1-\epsilon)(1-\epsilon) + (1-\epsilon)(2-\epsilon) + (1-\epsilon)\epsilon + \epsilon(1-\epsilon)$
$= 1 - 2\epsilon + \epsilon^2 + 2 - 3\epsilon + \epsilon^2 + \epsilon - \epsilon^2 + \epsilon - \epsilon^2$
$= 3 - 3\epsilon$.

Approaches 3.

So for $n = 4$, it seems like the supremum is 3, achieved when 3 of the 4 variables are just below 1 and one is just above 1 (or small).

Actually wait, let me reconsider. With $a_1 = a_2 = a_3 = 1 - \epsilon, a_4 = 1 + 3\epsilon$:

The sum approaches 3 as $\epsilon \to 0$. But can we actually achieve 3? No, because at $\epsilon = 0$, all $a_i = 1$ and $\{a_i\} = 0$. So the supremum is 3 but not achieved.

Hmm, but the problem says "find the smallest $\lambda(n)$ such that the inequality always holds." If the supremum is 3 but not achieved, then $\lambda(4) = 3$ works (since the sum is always strictly less than 3, so $\leq 3$ holds).

Wait, but is the supremum actually 3? Let me check if we can exceed 3.

Let me try a different approach. Let $f_i = \{a_i\}$ and $m_i = \lfloor a_i \rfloor$, so $a_i = m_i + f_i$ with $m_i \geq 0$ integer and $f_i \in [0, 1)$.

$\sum a_i = \sum m_i + \sum f_i = n$.

$\sum \{a_i\} a_{i+1} = \sum f_i (m_{i+1} + f_{i+1}) = \sum f_i m_{i+1} + \sum f_i f_{i+1}$.

We want to maximize this subject to $\sum m_i + \sum f_i = n$, $m_i \geq 0$ integer, $f_i \in [0, 1)$.

Since $f_i < 1$, we have $\sum f_i < n$, so $\sum m_i \geq 1$ (actually $\sum m_i = n - \sum f_i > 0$).

To maximize $\sum f_i m_{i+1}$, we want $f_i$ close to 1 and $m_{i+1}$ large. But $\sum m_i = n - \sum f_i$, and if all $f_i$ are close to 1, $\sum f_i \approx n$, so $\sum m_i \approx 0$, meaning all $m_i \approx 0$. Then $\sum f_i m_{i+1} \approx 0$ and $\sum f_i f_{i+1} \approx n$.

Wait, that's interesting! If all $f_i \to 1$ and all $m_i = 0$, then $\sum f_i \to n$ but $\sum f_i < n$ requires $\sum m_i > 0$. So we need at least one $m_i \geq 1$.

If $m_4 = 1$ and all other $m_i = 0$, with $f_1 = f_2 = f_3 = 1 - \epsilon$ and $f_4 = 1 - 3\epsilon$ (so $\sum f_i = 4 - 6\epsilon$, $\sum m_i = 1$, total = $5 - 6\epsilon$... that's not $n = 4$).

Let me be more careful. $\sum m_i + \sum f_i = n = 4$. If $m_4 = 1$, all other $m_i = 0$, then $\sum f_i = 3$. We need $f_1 + f_2 + f_3 + f_4 = 3$ with $f_i \in [0,1)$.

To maximize $\sum f_i f_{i+1} + \sum f_i m_{i+1}$:
- $\sum f_i m_{i+1} = f_1 \cdot 0 + f_2 \cdot 0 + f_3 \cdot 0 + f_4 \cdot 1 = f_4$ (wait, $m_{i+1}$: $m_2 = 0, m_3 = 0, m_4 = 0, m_1 = 0$... hmm, indices).

Wait, let me be careful with indices. $m_{i+1}$ where indices are mod $n$. So:
- $i=1$: $f_1 \cdot m_2$
- $i=2$: $f_2 \cdot m_3$
- $i=3$: $f_3 \cdot m_4 = f_3 \cdot 1 = f_3$
- $i=4$: $f_4 \cdot m_1 = f_4 \cdot 0 = 0$

So $\sum f_i m_{i+1} = f_3$.

And $\sum f_i f_{i+1} = f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1$.

Total = $f_3 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_3(1 + f_2 + f_4) + f_1 f_2 + f_4 f_1 = f_3(1 + f_2 + f_4) + f_1(f_2 + f_4)$.

With $f_1 + f_2 + f_3 + f_4 = 3$, $f_i \in [0,1)$.

Let $s = f_2 + f_4$ and $f_1 + f_3 = 3 - s$. Then total = $f_3(1 + s) + f_1 \cdot s = f_3 + s(f_1 + f_3) = f_3 + s(3 - s)$.

To maximize: we want $f_3$ large and $s(3-s)$ large. $s(3-s)$ is maximized at $s = 3/2$ giving $9/4$. And $f_3 < 1$. So total $< 1 + 9/4 = 13/4 = 3.25$.

But we need $f_1 + f_3 = 3 - s = 3 - 3/2 = 3/2$, with $f_3 < 1$ and $f_1 < 1$, so $f_1 > 1/2$. And $s = f_2 + f_4 = 3/2$ with $f_2, f_4 < 1$, so both $> 1/2$. This is feasible.

So the total can approach $1 + 9/4 = 13/4$? Let me check more carefully.

With $f_3 \to 1$, $f_1 \to 1/2$, $f_2 \to 3/4$, $f_4 \to 3/4$ (so $s = 3/2$):
Total $\to 1 \cdot (1 + 3/2) + (1/2)(3/2) = 5/2 + 3/4 = 13/4$.

But wait, we need $f_3 < 1$. As $f_3 \to 1^-$, $f_1 \to 1/2^+$ (since $f_1 = 3 - s - f_3 = 3/2 - f_3 \to 1/2$). And $f_1 < 1$ is satisfied. So the supremum is $13/4$.

But can we do even better with different $m_i$ assignments?

Let me try $m_3 = 1$ (instead of $m_4$). Then:
- $i=1$: $f_1 \cdot m_2 = 0$
- $i=2$: $f_2 \cdot m_3 = f_2$
- $i=3$: $f_3 \cdot m_4 = 0$
- $i=4$: $f_4 \cdot m_1 = 0$

Total = $f_2 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_2(1 + f_1 + f_3) + f_4(f_3 + f_1)$.

Same structure by symmetry. So same supremum $13/4$.

What about $m_1 = 1$?
- $i=4$: $f_4 \cdot m_1 = f_4$
- Others: 0

Total = $f_4 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_4(1 + f_3 + f_1) + f_2(f_1 + f_3)$.

Same structure. Supremum $13/4$.

What about $m_2 = 1$?
- $i=1$: $f_1 \cdot m_2 = f_1$
Total = $f_1 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_1(1 + f_2 + f_4) + f_3(f_2 + f_4)$.

Same. Supremum $13/4$.

Now what about $m_4 = 2$? Then $\sum f_i = 2$. 
- $i=3$: $f_3 \cdot m_4 = 2 f_3$

Total = $2f_3 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1 = f_3(2 + f_2 + f_4) + f_1(f_2 + f_4)$.

With $f_1 + f_2 + f_3 + f_4 = 2$, $f_i \in [0,1)$.

Let $s = f_2 + f_4$, $f_1 + f_3 = 2 - s$. Total = $f_3(2 + s) + f_1 \cdot s = 2f_3 + s(f_1 + f_3) = 2f_3 + s(2 - s)$.

Maximize: $f_3 < 1$, $s(2-s)$ maximized at $s = 1$ giving $1$. Total $< 2 + 1 = 3$. Less than $13/4 = 3.25$.

What about $m_3 = 1, m_4 = 1$? $\sum f_i = 2$.
- $i=2$: $f_2 \cdot m_3 = f_2$
- $i=3$: $f_3 \cdot m_4 = f_3$

Total = $f_2 + f_3 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1$.

With $\sum f_i = 2$. Let me try $f_2 = f_3 \to 1, f_1 = f_4 \to 0$. Total $\to 1 + 1 + 0 + 1 + 0 + 0 = 3$. Less than $13/4$.

Try $f_1 = f_2 = f_3 = f_4 = 1/2$. Total = $1/2 + 1/2 + 1/4 + 1/4 + 1/4 + 1/4 = 2$. Less.

Try $f_2 \to 1, f_3 \to 1, f_1 + f_4 \to 0$. Total $\to 1 + 1 + 0 + 1 + 0 + 0 = 3$.

What about $m_1 = 1, m_3 = 1$? $\sum f_i = 2$.
- $i=4$: $f_4 \cdot m_1 = f_4$
- $i=2$: $f_2 \cdot m_3 = f_2$

Total = $f_2 + f_4 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1$.

Try $f_2 \to 1, f_4 \to 1, f_1, f_3 \to 0$. Total $\to 1 + 1 + 0 + 0 + 0 + 0 = 2$. Less.

Try $f_1 = f_3 \to 1, f_2 = f_4 \to 0$. Total $\to 0 + 0 + 0 + 0 + 0 + 0 = 0$.

What about $m_1 = 1, m_2 = 1$? $\sum f_i = 2$.
- $i=4$: $f_4 \cdot m_1 = f_4$
- $i=1$: $f_1 \cdot m_2 = f_1$

Total = $f_1 + f_4 + f_1 f_2 + f_2 f_3 + f_3 f_4 + f_4 f_1$.

Try $f_1 \to 1, f_4 \to 1, f_2, f_3 \to 0$. Total $\to 1 + 1 + 0 + 0 + 0 + 0 = 2$.

So the best so far is $13/4$ with one $m_i = 1$ and the rest 0.

Can we do better with $m_4 = 1$ but different $f$ values? Let me re-examine.

With $m_4 = 1$, total = $f_3(1 + f_2 + f_4) + f_1(f_2 + f_4)$, $\sum f_i = 3$.

Let $s = f_2 + f_4$. Total = $f_3(1 + s) + (3 - s - f_3) \cdot s = f_3(1 + s) + 3s - s^2 - f_3 s = f_3 + 3s - s^2$.

So total = $f_3 + 3s - s^2$ where $f_3 < 1$, $s = f_2 + f_4 \in [0, 2)$ (since $f_2, f_4 < 1$), and $f_1 = 3 - s - f_3 \in [0, 1)$, so $f_3 > 2 - s$ and $f_3 < 3 - s$.

To maximize $f_3 + 3s - s^2$: since $f_3 < 1$, we want $f_3 \to 1$. Then total $\to 1 + 3s - s^2$. This is maximized at $s = 3/2$ giving $1 + 9/4 = 13/4$.

Constraints: $f_3 \to 1$ requires $2 - s < 1$, i.e., $s > 1$. And $f_1 = 3 - s - 1 = 2 - s < 1$ requires $s > 1$. And $f_1 \geq 0$ requires $s \leq 2$. And $s < 2$ (since $f_2, f_4 < 1$). So $s \in (1, 2)$, and $s = 3/2$ is feasible.

Also need $f_2, f_4 < 1$ with $f_2 + f_4 = 3/2$, so both in $(1/2, 1)$. Feasible.

So supremum is $13/4$ for $n = 4$.

Hmm wait, but I should also consider whether we can do better by not having exactly one $m_i = 1$. What about $m_4 = 1$ but also considering that maybe having a different structure could help?

Actually, I realize I should think about this more generally. Let me consider the problem for general $n$ with the constraint $\sum a_i = n$.

Hmm, but actually I'm not even sure the constraint is $\sum a_i = n$. Let me reconsider the problem statement.

"Given an integer $n \geq 4$, find the smallest $\lambda(n)$ such that for any non-negative real numbers $a_1, a_2, \ldots, a_n$ (indices taken modulo $n$), the inequality $\sum_{i=1}^{n}\{a_i\} a_{i+1} \leq \lambda(n)$ always holds."

There's no constraint mentioned! This is unbounded without a constraint. So either:
1. The problem is missing a constraint (likely $\sum a_i = 1$ or $\sum a_i = n$).
2. There's a different interpretation.

Given that the answer should depend on $n$ and the problem uses fractional parts, I think the most likely constraint is $\sum a_i = 1$. But as I showed, that gives $1/4$ for all $n \geq 3$.

Unless... the constraint is $\sum a_i = n$? Then for $n = 4$ I got $13/4$.

Actually, wait. Let me reconsider the case $\sum a_i = 1$ more carefully. With $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \in [0, 1]$. The fractional part $\{a_i\} = a_i$ if $a_i < 1$ and $\{a_i\} = 0$ if $a_i = 1$.

So $\sum \{a_i\} a_{i+1} \leq \sum a_i a_{i+1}$, and the maximum of $\sum a_i a_{i+1}$ with $\sum a_i = 1$ is $1/4$ (achieved at two adjacent $a_i = 1/2$). And $\{1/2\} = 1/2$, so the bound $1/4$ is achieved. So $\lambda(n) = 1/4$ for $n \geq 3$.

But the problem asks for $\lambda(n)$ as a function of $n$ with $n \geq 4$, suggesting the answer depends on $n$. So the constraint is probably not $\sum a_i = 1$.

Let me try $\sum a_i = n$. For general $n$:

With one $m_k = 1$ and rest 0, $\sum f_i = n - 1$. The total is:
$f_{k-1} \cdot 1 + \sum f_i f_{i+1}$ (where the $f_{k-1} \cdot 1$ comes from the $m_k$ term, since $a_{k-1}$'s fractional part times $a_k$'s integer part).

Wait, let me be more careful. If $m_k = 1$ and all other $m_i = 0$, then:
$\sum f_i m_{i+1} = f_{k-1} \cdot m_k = f_{k-1}$ (since $m_k = 1$ and all other $m_{i+1} = 0$).

So total = $f_{k-1} + \sum_{i=1}^n f_i f_{i+1}$, with $\sum f_i = n - 1$, $f_i \in [0, 1)$.

We want to maximize $f_{k-1} + \sum f_i f_{i+1}$.

Let me think about this for general $n$. WLOG $k = n$ (by rotation), so we maximize $f_{n-1} + \sum_{i=1}^n f_i f_{i+1}$ with $\sum f_i = n-1$, $f_i \in [0,1)$.

Since $\sum f_i = n - 1$ and $f_i < 1$, we need at least... well, $n$ variables each less than 1 summing to $n-1$. The "deficit" from all being 1 is $\sum (1 - f_i) = n - (n-1) = 1$. So the total deficit is 1.

Let $g_i = 1 - f_i \in (0, 1]$. Then $\sum g_i = 1$ and $f_i = 1 - g_i$.

$\sum f_i f_{i+1} = \sum (1 - g_i)(1 - g_{i+1}) = \sum (1 - g_i - g_{i+1} + g_i g_{i+1}) = n - 2\sum g_i + \sum g_i g_{i+1} = n - 2 + \sum g_i g_{i+1}$.

And $f_{n-1} = 1 - g_{n-1}$.

Total = $(1 - g_{n-1}) + (n - 2) + \sum g_i g_{i+1} = n - 1 - g_{n-1} + \sum g_i g_{i+1}$.

We want to maximize this, i.e., maximize $\sum g_i g_{i+1} - g_{n-1}$ subject to $\sum g_i = 1$, $g_i \in (0, 1]$.

Hmm, this is getting complex. Let me think about it differently.

Actually, let me reconsider. Maybe the constraint is $\sum a_i = 1$ but the problem is more subtle than I thought. Let me re-examine.

With $\sum a_i = 1$, $a_i \geq 0$: the maximum of $\sum \{a_i\} a_{i+1}$ is indeed $1/4$ for $n \geq 3$. For $n = 4$, this is $1/4$. The problem says $n \geq 4$, which is consistent with $n \geq 3$ giving $1/4$.

But the problem asks for $\lambda(n)$, suggesting it depends on $n$. If it's constant $1/4$, that's a valid answer but unusual for a competition problem.

Hmm, let me reconsider. Maybe the problem is asking about $\sum \{a_i\} \cdot a_{i+1}$ where $a_i$ are non-negative integers? No, it says "non-negative real numbers."

Or maybe the problem has a different constraint that I'm not seeing. Let me try the interpretation that there's no constraint but $a_i \in [0, 1)$ (i.e., the $a_i$ are already fractional parts). Then $\{a_i\} = a_i$ and we want to maximize $\sum a_i a_{i+1}$ with $a_i \in [0, 1)$. This is unbounded (approach $n$ by setting all $a_i \to 1$).

OK, I think the most reasonable interpretation given the structure is $\sum a_i = 1$. Let me also consider the possibility that the answer is $\frac{1}{4}\sec^2(\pi/n)$ or $\frac{1}{4\cos^2(\pi/n)}$ or something trigonometric, which is a common form for cyclic optimization problems.

Actually, for the problem of maximizing $\sum a_i a_{i+1}$ subject to $\sum a_i = 1$, $a_i \geq 0$, the answer is $1/4$ for $n \geq 3$ (achieved by concentrating mass on two adjacent variables). But if we add the constraint that all $a_i > 0$ (strictly), the supremum is still $1/4$.

However, there's a related problem: maximize $\sum a_i a_{i+1}$ subject to $\sum a_i^2 = 1$ (or $\sum a_i = 1$ with all $a_i > 0$). The spectral answer involves $\cos(\pi/n)$.

Actually, the maximum of $\sum a_i a_{i+1}$ subject to $\sum a_i^2 = 1$ is $\cos(\pi/n)$ (the largest eigenvalue of the cyclic adjacency matrix). But that's a different constraint.

Let me try the constraint $\sum a_i^2 = 1$. Then we want to maximize $\sum \{a_i\} a_{i+1}$ with $a_i \geq 0$ and $\sum a_i^2 = 1$. Since $a_i \geq 0$ and $\sum a_i^2 = 1$, we have $a_i \leq 1$, so $\{a_i\} = a_i$ (except when $a_i = 1$). So the problem becomes maximize $\sum a_i a_{i+1}$ with $\sum a_i^2 = 1$, $a_i \geq 0$.

The maximum of $\sum a_i a_{i+1}$ with $\sum a_i^2 = 1$ is $\cos(\pi/n)$ (for the cycle graph $C_n$). This is achieved when $a_i \propto \cos(\pi i / n - \pi/(2n))$ or something like that (the eigenvector of the largest eigenvalue).

Wait, but we need $a_i \geq 0$. The eigenvector of the cycle graph's largest eigenvalue $\cos(\pi/n)$ has components $\cos(\pi(i-1)/n + \pi/(2n))$ or similar, which can be negative. So the non-negative constraint might change things.

Hmm, actually for the cycle $C_n$, the adjacency matrix has eigenvalues $2\cos(2\pi k/n)$ for $k = 0, 1, \ldots, n-1$. The largest is $2$ (for $k=0$, eigenvector all 1s). But we're looking at $\sum a_i a_{i+1} = \frac{1}{2} a^T A a$ where $A$ is the adjacency matrix. So maximizing $\frac{1}{2} a^T A a$ subject to $\|a\|^2 = 1$ gives $\frac{1}{2} \cdot 2 = 1$ (with $a = (1/\sqrt{n}, \ldots, 1/\sqrt{n})$). But that's the unconstrained maximum.

With $a_i \geq 0$, the all-positive eigenvector gives $\sum a_i a_{i+1} = n \cdot (1/n) = 1$... wait, $\sum a_i a_{i+1} = \sum (1/\sqrt{n})(1/\sqrt{n}) = n \cdot 1/n = 1$. And $\sum a_i^2 = 1$. So the maximum is 1, achieved at the uniform vector. But that doesn't depend on $n$ either.

Hmm, I think I need to be more careful. $\sum a_i a_{i+1}$ with $\sum a_i^2 = 1$: by Cauchy-Schwarz or spectral methods, $\sum a_i a_{i+1} \leq \frac{1}{2}\sum(a_i^2 + a_{i+1}^2) = \sum a_i^2 = 1$. So the maximum is 1, achieved when $a_i = a_{i+1}$ for all $i$, i.e., all equal. This gives $1$ for all $n$. Not $n$-dependent.

OK so with $\sum a_i^2 = 1$, the answer is $1$ for all $n$. Not interesting.

Let me go back to the $\sum a_i = n$ interpretation. For $n = 4$, I found the supremum is $13/4$. Let me check $n = 5$.

With $m_5 = 1$, rest 0, $\sum f_i = 4$. Total = $f_4 + \sum f_i f_{i+1}$.

Using $g_i = 1 - f_i$, $\sum g_i = 1$:
$\sum f_i f_{i+1} = n - 2 + \sum g_i g_{i+1} = 5 - 2 + \sum g_i g_{i+1} = 3 + \sum g_i g_{i+1}$.
$f_4 = 1 - g_4$.
Total = $1 - g_4 + 3 + \sum g_i g_{i+1} = 4 - g_4 + \sum g_i g_{i+1}$.

Maximize $\sum g_i g_{i+1} - g_4$ with $\sum g_i = 1$, $g_i \in (0, 1]$.

To maximize $\sum g_i g_{i+1}$, we want to concentrate the $g_i$ mass on adjacent pairs. But we also want to minimize $g_4$.

If we set $g_4 \to 0$ and concentrate mass on $g_1, g_2$ (adjacent): $g_1 = g_2 = 1/2$, rest 0. Then $\sum g_i g_{i+1} = g_1 g_2 = 1/4$. Total $= 4 - 0 + 1/4 = 17/4$.

But wait, $g_i > 0$ (since $f_i < 1$). So $g_4 \to 0^+$. And $g_3, g_5 \to 0^+$. So total $\to 4 + 1/4 = 17/4$.

Can we do better? What if we concentrate on $g_4, g_5$? Then $g_4 = 1/2, g_5 = 1/2$. $\sum g_i g_{i+1} = g_4 g_5 = 1/4$. Total $= 4 - 1/2 + 1/4 = 15/4$. Worse because of the $-g_4$ term.

What about $g_1 = 1$, rest $\to 0$? $\sum g_i g_{i+1} \to 0$. Total $\to 4 - 0 + 0 = 4$. Better than $17/4 = 4.25$? No, $4 < 4.25$.

What about $g_3 = g_4 = 1/2$? $\sum g_i g_{i+1} = g_3 g_4 = 1/4$. Total $= 4 - 1/2 + 1/4 = 3.75$. Worse.

So for $n = 5$, with one $m_i = 1$, the best is $17/4$ (concentrating $g$ mass away from index 4 and on an adjacent pair not involving index 4 or its neighbors).

Hmm wait, but I should also consider having more than one $m_i = 1$. Let me think about this differently.

Actually, let me reconsider the whole problem. Maybe the constraint is $\sum a_i = 1$ and the answer is $\frac{1}{4\cos^2(\pi/n)}$ or something like that. Let me think about what happens when we DON'T require $a_i < 1$.

With $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \leq 1$. The only way $\{a_i\} \neq a_i$ is if $a_i = 1$ (then $\{a_i\} = 0$). So $\{a_i\} \leq a_i$ always, and $\sum \{a_i\} a_{i+1} \leq \sum a_i a_{i+1} \leq 1/4$. And $1/4$ is achieved. So $\lambda(n) = 1/4$ for all $n \geq 3$.

This is a valid answer but doesn't depend on $n$. The problem specifically says $n \geq 4$ and asks for $\lambda(n)$, which strongly suggests the answer depends on $n$.

Let me try yet another interpretation: maybe the constraint is $\sum a_i = n$ (or $\sum a_i \leq n$). Let me pursue this.

For general $n$ with $\sum a_i = n$:

The key insight is that we can have some $a_i$ with integer parts, creating a gap between $\{a_i\}$ and $a_i$.

Let me think about the optimal strategy. We want to maximize $\sum f_i a_{i+1} = \sum f_i (m_{i+1} + f_{i+1})$ where $f_i = \{a_i\}$, $m_i = \lfloor a_i \rfloor$, $\sum (m_i + f_i) = n$.

The $\sum f_i f_{i+1}$ part is maximized when all $f_i$ are close to 1 (giving close to $n$). But then $\sum m_i \approx 0$ and the $\sum f_i m_{i+1}$ part is small.

The $\sum f_i m_{i+1}$ part benefits from having large $m_{i+1}$ preceded by $f_i$ close to 1.

Let me think about the trade-off. Suppose we set $k$ of the $m_i$ to be positive. Say $m_{i_1}, \ldots, m_{i_k}$ are positive with values $M_1, \ldots, M_k$, and $\sum M_j = M$ (total integer part). Then $\sum f_i = n - M$.

The $\sum f_i m_{i+1}$ term: for each $j$, if $m_{i_j} = M_j$, then the term $f_{i_j - 1} \cdot M_j$ contributes. So $\sum f_i m_{i+1} = \sum_j f_{i_j - 1} M_j$.

To maximize, we want $f_{i_j - 1}$ close to 1 and $M_j$ large. But $\sum f_i = n - M$ and $f_i < 1$, so we need $n - M < n$, i.e., $M > 0$, and the number of $f_i$ close to 1 is at most $n - M$ (roughly).

This is getting complicated. Let me try a specific strategy for general $n$.

Strategy: Set $m_n = 1$, all other $m_i = 0$. Then $\sum f_i = n - 1$. The total is:
$T = f_{n-1} + \sum_{i=1}^n f_i f_{i+1}$

Using $g_i = 1 - f_i$, $\sum g_i = 1$:
$T = (1 - g_{n-1}) + (n - 2 + \sum g_i g_{i+1}) = n - 1 - g_{n-1} + \sum g_i g_{i+1}$

We want to maximize $\sum g_i g_{i+1} - g_{n-1}$ with $\sum g_i = 1$, $g_i \in (0, 1]$.

The maximum of $\sum g_i g_{i+1}$ with $\sum g_i = 1$ is $1/4$ (concentrate on two adjacent variables). We want to do this while minimizing $g_{n-1}$.

If we concentrate on $g_1 = g_2 = 1/2$ (and $g_{n-1} \to 0$), we get $\sum g_i g_{i+1} = 1/4$ and $g_{n-1} \to 0$. Total $\to n - 1 + 1/4 = n - 3/4$.

For $n = 4$: $4 - 3/4 = 13/4$. ✓
For $n = 5$: $5 - 3/4 = 17/4$. ✓

But can we do better with a different strategy? What if we use $m_n = 2$?

$m_n = 2$, $\sum f_i = n - 2$. Total = $2f_{n-1} + \sum f_i f_{i+1}$.
$g_i = 1 - f_i$, $\sum g_i = 2$.
$\sum f_i f_{i+1} = n - 2 \cdot 2 + \sum g_i g_{i+1} = n - 4 + \sum g_i g_{i+1}$.
Total = $2(1 - g_{n-1}) + n - 4 + \sum g_i g_{i+1} = n - 2 - 2g_{n-1} + \sum g_i g_{i+1}$.

Maximize $\sum g_i g_{i+1} - 2g_{n-1}$ with $\sum g_i = 2$, $g_i \in (0, 1]$.

Max of $\sum g_i g_{i+1}$ with $\sum g_i = 2$: this is like maximizing a quadratic form. With all $g_i$ on two adjacent: $g_1 = g_2 = 1$, $\sum g_i g_{i+1} = 1$. With $g_{n-1} \to 0$: Total $\to n - 2 + 1 = n - 1$.

Compare with $m_n = 1$: $n - 3/4$. For $n \geq 4$, $n - 1 > n - 3/4$? $n - 1 > n - 0.75$ iff $-1 > -0.75$ which is false. So $n - 1 < n - 3/4$. So $m_n = 2$ is worse.

What about $m_n = 1, m_k = 1$ for some $k \neq n$? $\sum f_i = n - 2$.
Total = $f_{n-1} + f_{k-1} + \sum f_i f_{i+1}$.
$g_i = 1 - f_i$, $\sum g_i = 2$.
Total = $(1 - g_{n-1}) + (1 - g_{k-1}) + (n - 4 + \sum g_i g_{i+1}) = n - 2 - g_{n-1} - g_{k-1} + \sum g_i g_{i+1}$.

Maximize $\sum g_i g_{i+1} - g_{n-1} - g_{k-1}$ with $\sum g_i = 2$.

If $k$ is far from $n$, we can set $g_{n-1}, g_{k-1} \to 0$ and concentrate on two adjacent $g$'s. $\sum g_i g_{i+1} \to 1$ (with $g_1 = g_2 = 1$). Total $\to n - 2 + 1 = n - 1$. Same as $m_n = 2$.

What if $k = n - 1$? Then $g_{n-2} + g_{n-2}$... wait, $k - 1 = n - 2$ and $n - 1$. We minimize $g_{n-1} + g_{n-2}$. Concentrate $g$ on $g_1 = g_2 = 1$. Total $\to n - 2 + 1 = n - 1$. Same.

What if $k = 1$? Then $k - 1 = 0 = n$ (mod $n$), so $g_n + g_{n-1}$. We minimize $g_n + g_{n-1}$. Concentrate on $g_2 = g_3 = 1$. $\sum g_i g_{i+1} = g_2 g_3 = 1$. Total $\to n - 2 + 1 = n - 1$. Same.

So with two $m_i = 1$, we get $n - 1$, which is less than $n - 3/4$.

What about $m_n = 1$ but with a different distribution of $g$? Instead of concentrating on two adjacent, what if we spread?

$\sum g_i g_{i+1}$ with $\sum g_i = 1$: the maximum is $1/4$ (two adjacent at $1/2$ each). We can't do better. So the best with $m_n = 1$ is $n - 1 + 1/4 = n - 3/4$ (when $g_{n-1} \to 0$).

But wait, what if we don't set $g_{n-1} \to 0$ but instead find a better trade-off? We have:
$T = n - 1 - g_{n-1} + \sum g_i g_{i+1}$.

If $g_{n-1}$ is part of the adjacent pair, say $g_{n-1} = g_n = 1/2$, then $\sum g_i g_{i+1} = g_{n-1} g_n = 1/4$ and $T = n - 1 - 1/2 + 1/4 = n - 5/4$. Worse.

If $g_{n-1}$ is not in the pair, $g_{n-1} \to 0$ and $\sum g_i g_{i+1} \to 1/4$. $T \to n - 3/4$. Best.

So with one $m_i = 1$, the best is $n - 3/4$.

Now, can we do better with a completely different approach? What if we don't use the integer part at all (all $m_i = 0$)? Then $\sum f_i = n$ but $f_i < 1$ means $\sum f_i < n$, contradiction. So we need at least one $m_i \geq 1$.

What if we use a fractional $m$... no, $m_i$ are integers.

So the question is: what's the optimal number and placement of integer parts?

With $M = \sum m_i$ (total integer part), $\sum f_i = n - M$, and the total is:
$T = \sum f_i m_{i+1} + \sum f_i f_{i+1}$

The second term: $\sum f_i f_{i+1} \leq ?$ with $\sum f_i = n - M$, $f_i < 1$.

Using $g_i = 1 - f_i$, $\sum g_i = M$:
$\sum f_i f_{i+1} = n - 2M + \sum g_i g_{i+1}$.

The first term: $\sum f_i m_{i+1}$. This depends on the placement of $m_i$.

$T = \sum f_i m_{i+1} + n - 2M + \sum g_i g_{i+1}$
$= \sum (1 - g_i) m_{i+1} + n - 2M + \sum g_i g_{i+1}$
$= \sum m_{i+1} - \sum g_i m_{i+1} + n - 2M + \sum g_i g_{i+1}$
$= M - \sum g_i m_{i+1} + n - 2M + \sum g_i g_{i+1}$
$= n - M - \sum g_i m_{i+1} + \sum g_i g_{i+1}$

So $T = n - M + \sum g_i (g_{i+1} - m_{i+1})$.

We want to maximize $T = n - M + \sum g_i (g_{i+1} - m_{i+1})$ with $\sum g_i = M$, $g_i \in (0, 1]$, $m_i \geq 0$ integer, $\sum m_i = M$.

Note that $g_{i+1} - m_{i+1} \leq g_{i+1} \leq 1$ and $g_{i+1} - m_{i+1} \geq -m_{i+1}$.

To maximize, we want $g_{i+1} - m_{i+1}$ to be large where $g_i$ is large. $g_{i+1} - m_{i+1}$ is large when $m_{i+1} = 0$ and $g_{i+1}$ is close to 1, or when $m_{i+1}$ is small.

But we also want $M$ to be small (since $n - M$ decreases with $M$). The minimum $M$ is 1 (since $\sum f_i < n$ requires $M \geq 1$).

With $M = 1$: $T = n - 1 + \sum g_i (g_{i+1} - m_{i+1})$.

If $m_n = 1$, rest 0: $T = n - 1 + \sum g_i g_{i+1} - g_{n-1} \cdot 1 = n - 1 + \sum g_i g_{i+1} - g_{n-1}$.

This is what we had before. Max is $n - 1 + 1/4 = n - 3/4$ (with $g_{n-1} \to 0$, $g_1 = g_2 = 1/2$).

With $M = 2$: $T = n - 2 + \sum g_i (g_{i+1} - m_{i+1})$.

If $m_n = 2$: $T = n - 2 + \sum g_i g_{i+1} - 2g_{n-1}$. Max: $\sum g_i g_{i+1} \leq ?$ with $\sum g_i = 2$.

Max of $\sum g_i g_{i+1}$ with $\sum g_i = 2$, $g_i \in (0, 1]$: concentrate on two adjacent, $g_1 = g_2 = 1$, giving $1$. With $g_{n-1} \to 0$: $T \to n - 2 + 1 = n - 1$. Less than $n - 3/4$.

If $m_n = m_k = 1$: $T = n - 2 + \sum g_i g_{i+1} - g_{n-1} - g_{k-1}$. Max with $g_{n-1}, g_{k-1} \to 0$ and $\sum g_i g_{i+1} \to 1$: $T \to n - 1$. Same.

So $M = 1$ is optimal, giving $T_{\max} = n - 3/4$.

But wait, I need to verify that $\sum g_i g_{i+1}$ can actually reach $1/4$ while $g_{n-1} \to 0$ and $\sum g_i = 1$. Yes: set $g_1 = 1/2, g_2 = 1/2$, all other $g_i \to 0$. Then $\sum g_i g_{i+1} = g_1 g_2 = 1/4$ and $g_{n-1} \to 0$. But we need $g_i > 0$ for all $i$ (since $f_i < 1$). So we set $g_3 = \ldots = g_n = \epsilon$ and $g_1 = 1/2 - (n-2)\epsilon/2$, $g_2 = 1/2 - (n-2)\epsilon/2$. As $\epsilon \to 0$, this works.

Actually wait, I need to be more careful. $\sum g_i = 1$ with $g_1 = g_2 = 1/2 - (n-2)\epsilon/2$ and $g_3 = \ldots = g_n = \epsilon$. Then $\sum g_i = 2(1/2 - (n-2)\epsilon/2) + (n-2)\epsilon = 1 - (n-2)\epsilon + (n-2)\epsilon = 1$. ✓

$\sum g_i g_{i+1} = g_1 g_2 + g_2 g_3 + \ldots + g_n g_1$. As $\epsilon \to 0$: $g_1 g_2 \to 1/4$, other terms $\to 0$. So $\sum g_i g_{i+1} \to 1/4$. ✓

$g_{n-1} = \epsilon \to 0$. ✓

So $T \to n - 1 + 1/4 - 0 = n - 3/4$.

But is this the supremum, or can we do better? Let me think about whether there's a smarter configuration.

What if instead of concentrating $g$ on two adjacent, we use a different pattern? The key formula is:
$T = n - 1 + \sum g_i g_{i+1} - g_{n-1}$ (with $m_n = 1$).

We want to maximize $\sum g_i g_{i+1} - g_{n-1}$ with $\sum g_i = 1$, $g_i \in (0, 1]$.

Let's think of this as: maximize $\sum g_i g_{i+1} - g_{n-1}$.

If we put $g_{n-1} = 0$ (limit), then we maximize $\sum_{i \neq n-1} g_i g_{i+1}$ with $\sum_{i \neq n-1} g_i = 1$. But $g_{n-2} g_{n-1} = 0$ and $g_{n-1} g_n = 0$, so the sum is over the path $1, 2, \ldots, n-2, n$ (with $g_{n-2} g_n$ being a term if $n-2$ and $n$ are adjacent, which they're not in the cycle... wait, in the cycle, $n$ is adjacent to $n-1$ and $1$. So with $g_{n-1} = 0$, the terms are $g_1 g_2, g_2 g_3, \ldots, g_{n-3} g_{n-2}, g_{n-2} \cdot 0, 0 \cdot g_n, g_n g_1$. So the nonzero terms form a path: $g_n g_1, g_1 g_2, \ldots, g_{n-3} g_{n-2}$.

This is a path graph on $n-1$ vertices (vertices $n, 1, 2, \ldots, n-2$). The maximum of $\sum g_i g_{i+1}$ on a path with $\sum g_i = 1$ is $1/4$ (concentrate on any edge). So the max is $1/4$, confirming our result.

So $\lambda(n) = n - 3/4$ for $n \geq 4$? Let me double-check with $n = 4$:

$\lambda(4) = 4 - 3/4 = 13/4 = 3.25$.

Earlier I computed the supremum as $13/4$ for $n = 4$. ✓

But wait, I should also check: is the supremum actually achieved, or just approached? If it's not achieved, then $\lambda(n) = n - 3/4$ works as an upper bound (since the sum is always $< n - 3/4 \leq n - 3/4$). But we need to check that the sum can get arbitrarily close to $n - 3/4$, which it can (as shown above).

Hmm, but actually I need to be more careful. The problem says "the inequality $\leq \lambda(n)$ always holds." If the supremum is $n - 3/4$ and it's not achieved, then $\lambda(n) = n - 3/4$ works (since the sum is always $< n - 3/4$, hence $\leq n - 3/4$). And any $\lambda < n - 3/4$ would fail (since we can get arbitrarily close). So $\lambda(n) = n - 3/4$.

But wait, I assumed the constraint is $\sum a_i = n$. I'm not sure about this. Let me reconsider.

Actually, I just realized: maybe the problem has no constraint and the answer involves the fractional parts in a way that makes it bounded. Let me re-read.

"for any non-negative real numbers $a_1, a_2, \ldots, a_n$"

If there's truly no constraint, the sum $\sum \{a_i\} a_{i+1}$ is unbounded (set $a_1 = 0.5, a_2 = M$ for large $M$, rest 0; then $\{a_1\} a_2 = 0.5M \to \infty$).

So there MUST be a constraint. The most natural one that makes the problem interesting and $n$-dependent is $\sum a_i = n$ (or equivalently, the average is 1).

Actually, wait. I just thought of another possibility. What if the problem is about $a_i \in [0, 1)$ (i.e., the $a_i$ are already in $[0,1)$, so $\{a_i\} = a_i$), and the constraint is $\sum a_i = 1$? Then we're maximizing $\sum a_i a_{i+1}$ with $\sum a_i = 1$, $a_i \in [0, 1)$. The answer is $1/4$ for all $n \geq 3$.

But the problem says "non-negative real numbers," not "numbers in $[0,1)$." And it uses $\{a_i\}$, suggesting the $a_i$ can be larger than 1.

I'll go with $\sum a_i = n$ as the constraint. But actually, I realize I should also consider $\sum a_i = 1$ with $a_i$ being general non-negative reals (not restricted to $[0,1]$). With $\sum a_i = 1$ and $a_i \geq 0$, we still have $a_i \leq 1$, so $\{a_i\} = a_i$ (unless $a_i = 1$). So the answer is $1/4$.

Hmm, but what if the constraint is $\sum a_i = 1$ and the $a_i$ can be any non-negative reals? Then $a_i \in [0, 1]$ and $\{a_i\} = a_i$ for $a_i < 1$, $\{a_i\} = 0$ for $a_i = 1$. The maximum of $\sum \{a_i\} a_{i+1}$ is $1/4$ (achieved at $a_1 = a_2 = 1/2$).

OK so with $\sum a_i = 1$, the answer is $1/4$ regardless of $n$. The problem asks for $\lambda(n)$ with $n \geq 4$, which could just be the constant $1/4$.

But competition problems usually have more interesting answers. Let me think about whether there's a constraint that gives an $n$-dependent answer.

What if the constraint is $\sum a_i^2 = 1$? Then $a_i \in [0, 1]$ and $\{a_i\} = a_i$ (mostly). The maximum of $\sum a_i a_{i+1}$ with $\sum a_i^2 = 1$ is... by the spectral method, $\sum a_i a_{i+1} = \frac{1}{2} a^T A a$ where $A$ is the cycle adjacency matrix. The maximum of $a^T A a$ with $\|a\| = 1$ and $a \geq 0$ is the largest eigenvalue of $A$ restricted to the non-negative orthant. The largest eigenvalue of the cycle adjacency matrix is 2 (eigenvector all 1s), but that gives $\sum a_i a_{i+1} = \frac{1}{2} \cdot 2 = 1$ with $a_i = 1/\sqrt{n}$. So the answer would be 1 for all $n$. Not interesting.

What about $\sum a_i = 1$ with $a_i \geq 0$ and the objective is $\sum \{a_i\} a_{i+1}^2$ or something? No, the problem clearly states $\sum \{a_i\} a_{i+1}$.

Let me try another common constraint: $\prod a_i = 1$ or $\sum a_i \leq n$ or $\max a_i \leq 1$.

If $\max a_i \leq 1$ (i.e., $a_i \in [0, 1]$): then $\{a_i\} = a_i$ for $a_i < 1$ and $\{a_i\} = 0$ for $a_i = 1$. The supremum of $\sum a_i a_{i+1}$ with $a_i \in [0, 1)$ is $n$ (all $a_i \to 1$). But $\{a_i\} = a_i$ when $a_i < 1$, so $\sum \{a_i\} a_{i+1} \to n$. So $\lambda(n) = n$? But that's trivially achieved in the limit.

Hmm, that doesn't seem right either. With $a_i \in [0, 1]$, $\{a_i\} = a_i$ for $a_i < 1$ and $0$ for $a_i = 1$. So $\sum \{a_i\} a_{i+1} < n$ (strictly, since not all can be 1 and have nonzero fractional parts). The supremum is $n$ but not achieved. So $\lambda(n) = n$.

But that's too simple and doesn't really use the fractional part in an interesting way.

OK, I think the most likely constraint, given that the answer should depend on $n$ and involve fractional parts nontrivially, is $\sum a_i = n$. Let me also consider $\sum a_i \leq n$.

With $\sum a_i \leq n$: the maximum is the same as $\sum a_i = n$ (since increasing $a_i$ can only increase the sum, as long as fractional parts don't decrease). Actually, increasing $a_i$ might decrease $\{a_i\}$ (when crossing an integer). So it's not monotone. But the supremum over $\sum a_i \leq n$ should be the same as over $\sum a_i = n$ (we can always adjust).

Let me also consider: maybe the problem is stated correctly without a constraint, but the $a_i$ are assumed to be in $[0, 1)$ (so $\{a_i\} = a_i$), and the constraint is $\sum a_i = 1$. Then the answer is $1/4$ for all $n \geq 3$. The problem says $n \geq 4$ perhaps because for $n = 2$ or $n = 3$ the answer is different.

For $n = 2$: $\sum a_i a_{i+1} = a_1 a_2 + a_2 a_1 = 2a_1 a_2$ with $a_1 + a_2 = 1$. Max at $a_1 = a_2 = 1/2$: $2 \cdot 1/4 = 1/2$.

For $n = 3$: $a_1 a_2 + a_2 a_3 + a_3 a_1$ with $a_1 + a_2 + a_3 = 1$. Max at $a_1 = a_2 = 1/2, a_3 = 0$: $1/4$. Or at $a_1 = a_2 = a_3 = 1/3$: $3 \cdot 1/9 = 1/3 < 1/4$.

Wait, $1/3 < 1/4$? No, $1/3 > 1/4$. So for $n = 3$, the uniform distribution gives $1/3 > 1/4$.

Hmm, so for $n = 3$, the maximum of $\sum a_i a_{i+1}$ with $\sum a_i = 1$ is $1/3$ (at uniform), not $1/4$.

Let me recalculate. For $n = 3$, $\sum a_i a_{i+1} = a_1 a_2 + a_2 a_3 + a_3 a_1$ (since the cycle on 3 vertices is a triangle). With $a_1 + a_2 + a_3 = 1$:
$a_1 a_2 + a_2 a_3 + a_3 a_1 = \frac{(a_1 + a_2 + a_3)^2 - (a_1^2 + a_2^2 + a_3^2)}{2} = \frac{1 - \sum a_i^2}{2}$.

Maximized when $\sum a_i^2$ is minimized, i.e., $a_1 = a_2 = a_3 = 1/3$. Then $\sum a_i a_{i+1} = \frac{1 - 1/3}{2} = 1/3$.

For $n = 4$: $\sum a_i a_{i+1} = a_1 a_2 + a_2 a_3 + a_3 a_4 + a_4 a_1$. With $\sum a_i = 1$:
At uniform $a_i = 1/4$: $4 \cdot 1/16 = 1/4$.
At $a_1 = a_2 = 1/2, a_3 = a_4 = 0$: $1/4 + 0 + 0 + 0 = 1/4$.
At $a_1 = a_3 = 1/2, a_2 = a_4 = 0$: $0 + 0 + 0 + 0 = 0$.

So for $n = 4$, the max is $1/4$.

For $n = 5$: At uniform $a_i = 1/5$: $5 \cdot 1/25 = 1/5$. At $a_1 = a_2 = 1/2$: $1/4$. So $1/4 > 1/5$, and the max is $1/4$.

So for $n \geq 4$, the max of $\sum a_i a_{i+1}$ with $\sum a_i = 1$ is $1/4$ (concentrate on two adjacent). For $n = 3$, it's $1/3$ (uniform). For $n = 2$, it's $1/2$.

So the problem specifies $n \geq 4$ because for $n \geq 4$, the answer is $1/4$ (constant), while for smaller $n$ it's different. This makes sense!

But wait, with $\sum a_i = 1$ and $a_i \geq 0$, we have $a_i \leq 1$, so $\{a_i\} = a_i$ (unless $a_i = 1$). The maximum of $\sum \{a_i\} a_{i+1}$ is the same as $\sum a_i a_{i+1}$, which is $1/4$ for $n \geq 4$.

But the problem uses $\{a_i\}$ (fractional part), which is only different from $a_i$ when $a_i \geq 1$. With $\sum a_i = 1$, this never happens (except $a_i = 1$ which gives $\{a_i\} = 0$). So the fractional part is irrelevant, and the problem reduces to maximizing $\sum a_i a_{i+1}$.

This seems too simple for a competition problem. The use of fractional parts suggests the $a_i$ can be larger than 1, which means the constraint is probably $\sum a_i = n$ (or similar).

Let me go with $\sum a_i = n$ and the answer $\lambda(n) = n - \frac{3}{4}$.

Actually wait, I want to double-check this more carefully. Let me verify for $n = 4$ with a concrete near-optimal example.

$n = 4$, $m_4 = 1$, $g_1 = g_2 = 1/2 - \epsilon$, $g_3 = g_4 = \epsilon$ (approximately). Then:
$f_1 = 1/2 + \epsilon, f_2 = 1/2 + \epsilon, f_3 = 1 - \epsilon, f_4 = 1 - \epsilon$.
$a_1 = 0 + f_1 = 1/2 + \epsilon$
$a_2 = 0 + f_2 = 1/2 + \epsilon$
$a_3 = 0 + f_3 = 1 - \epsilon$
$a_4 = 1 + f_4 = 2 - \epsilon$

Check: $\sum a_i = 1/2 + \epsilon + 1/2 + \epsilon + 1 - \epsilon + 2 - \epsilon = 4$. ✓

$\{a_1\} = 1/2 + \epsilon, \{a_2\} = 1/2 + \epsilon, \{a_3\} = 1 - \epsilon, \{a_4\} = 1 - \epsilon$.

$\sum \{a_i\} a_{i+1} = (1/2 + \epsilon)(1/2 + \epsilon) + (1/2 + \epsilon)(1 - \epsilon) + (1 - \epsilon)(2 - \epsilon) + (1 - \epsilon)(1/2 + \epsilon)$

$= 1/4 + \epsilon + \epsilon^2 + 1/2 - \epsilon/2 + \epsilon - \epsilon^2 + 2 - 3\epsilon + \epsilon^2 + 1/2 + \epsilon - \epsilon/2 - \epsilon^2$

Let me compute term by term:
- $(1/2 + \epsilon)(1/2 + \epsilon) = 1/4 + \epsilon + \epsilon^2$
- $(1/2 + \epsilon)(1 - \epsilon) = 1/2 - \epsilon/2 + \epsilon - \epsilon^2 = 1/2 + \epsilon/2 - \epsilon^2$
- $(1 - \epsilon)(2 - \epsilon) = 2 - 3\epsilon + \epsilon^2$
- $(1 - \epsilon)(1/2 + \epsilon) = 1/2 + \epsilon - \epsilon/2 - \epsilon^2 = 1/2 + \epsilon/2 - \epsilon^2$

Sum = $1/4 + \epsilon + \epsilon^2 + 1/2 + \epsilon/2 - \epsilon^2 + 2 - 3\epsilon + \epsilon^2 + 1/2 + \epsilon/2 - \epsilon^2$
$= 1/4 + 1/2 + 2 + 1/2 + \epsilon + \epsilon/2 - 3\epsilon + \epsilon/2 + \epsilon^2 - \epsilon^2 + \epsilon^2 - \epsilon^2$
$= 13/4 + (1 + 1/2 - 3 + 1/2)\epsilon + 0$
$= 13/4 + (-1)\epsilon$
$= 13/4 - \epsilon$

As $\epsilon \to 0$, this approaches $13/4 = 3.25$. ✓

But wait, I need $g_3 = \epsilon$ and $g_4 = \epsilon$, but I said $g_1 = g_2 = 1/2 - \epsilon$ and $g_3 = g_4 = \epsilon$. Then $\sum g_i = 2(1/2 - \epsilon) + 2\epsilon = 1$. ✓ And $g_{n-1} = g_3 = \epsilon \to 0$. ✓

But $g_4 = \epsilon$ means $f_4 = 1 - \epsilon$, and $m_4 = 1$, so $a_4 = 2 - \epsilon$. And $g_3 = \epsilon$ means $f_3 = 1 - \epsilon$, $m_3 = 0$, $a_3 = 1 - \epsilon$.

Hmm, but I need $g_{n-1} = g_3 \to 0$ for the formula to work. In my example, $g_3 = \epsilon \to 0$. ✓

So the sum approaches $13/4$ from below. The supremum is $13/4$ but not achieved. So $\lambda(4) = 13/4$.

For general $n \geq 4$: $\lambda(n) = n - 3/4$.

Hmm wait, but I should double-check that we can't do better. Let me think about whether a different placement of the integer part could help.

With $m_n = 1$, the formula is $T = n - 1 + \sum g_i g_{i+1} - g_{n-1}$.

The key is that we lose $g_{n-1}$ (the $g$ value just before the integer part). What if we place the integer part at a position where the "loss" is smaller?

By symmetry of the cycle, the position of the single integer part doesn't matter—the loss is always $g_{k-1}$ where $k$ is the position. And we can always make $g_{k-1} \to 0$ by concentrating the $g$ mass elsewhere. So the supremum is always $n - 1 + 1/4 = n - 3/4$.

But what if we use a more clever strategy? For instance, what if we don't concentrate $g$ on just two adjacent variables?

The maximum of $\sum g_i g_{i+1}$ with $\sum g_i = 1$ on a cycle of length $n \geq 4$ is $1/4$ (concentrate on one edge). This is because $\sum g_i g_{i+1} \leq \frac{1}{2}\sum g_i(g_{i-1} + g_{i+1}) \leq \frac{1}{2}\sum g_i \cdot \max(g_{i-1} + g_{i+1})$... actually, let me think more carefully.

$\sum g_i g_{i+1} \leq \frac{1}{2} \sum (g_i^2 + g_{i+1}^2)/2 \cdot 2$... no, by AM-GM, $g_i g_{i+1} \leq (g_i + g_{i+1})^2/4$. So $\sum g_i g_{i+1} \leq \sum (g_i + g_{i+1})^2/4$. But this doesn't directly help.

Actually, $\sum g_i g_{i+1} \leq \frac{(\sum g_i)^2}{4}$ when the graph is bipartite (which the cycle is for even $n$). For even $n$, the cycle is bipartite, and $\sum g_i g_{i+1} \leq \frac{(\sum_{\text{odd}} g_i)(\sum_{\text{even}} g_i)}{1} \cdot \ldots$ hmm, not exactly.

For a bipartite graph with parts $A$ and $B$: $\sum_{i \in A, j \in B, ij \in E} g_i g_j \leq (\sum_A g_i)(\sum_B g_j) \leq \frac{(\sum g_i)^2}{4} = 1/4$.

For even $n$, the cycle is bipartite, so $\sum g_i g_{i+1} \leq 1/4$. ✓

For odd $n$, the cycle is not bipartite. But we can still bound it. $\sum g_i g_{i+1} \leq ?$

For odd $n$, the maximum of $\sum g_i g_{i+1}$ with $\sum g_i = 1$, $g_i \geq 0$ is still $1/4$ for $n \geq 5$. Here's why: concentrate on two adjacent vertices, $g_1 = g_2 = 1/2$, rest 0. Then $\sum g_i g_{i+1} = 1/4$. Can we do better?

For $n = 5$: try $g_1 = g_2 = g_3 = 1/3$. $\sum g_i g_{i+1} = g_1 g_2 + g_2 g_3 + g_3 g_4 + g_4 g_5 + g_5 g_1 = 1/9 + 1/9 + 0 + 0 + 0 = 2/9 < 1/4$.

Try $g_1 = a, g_2 = b, g_3 = c$, rest 0, $a + b + c = 1$. $\sum = ab + bc = b(a+c) = b(1-b)$. Max at $b = 1/2$: $1/4$. Same.

So for $n \geq 4$ (both even and odd), the max of $\sum g_i g_{i+1}$ with $\sum g_i = 1$ is $1/4$.

Therefore, $\lambda(n) = n - 3/4$ for all $n \geq 4$.

But wait, I should also consider whether we can do better by NOT using the $g$-concentration strategy. What if we use a different $M$ or different placement?

I showed that with $M = 1$, the supremum is $n - 3/4$. With $M = 2$, it's $n - 1 < n - 3/4$. With $M \geq 2$, the supremum is $n - M + \text{something} \leq n - M + M/4 \cdot \ldots$ hmm, let me think more generally.

With general $M$: $T = n - M + \sum g_i(g_{i+1} - m_{i+1})$.

$\sum g_i(g_{i+1} - m_{i+1}) \leq \sum g_i g_{i+1} \leq M^2/4$ (by the bipartite bound, $\sum g_i g_{i+1} \leq (\sum g_i)^2/4 = M^2/4$ for even $n$; for odd $n \geq 5$, same bound holds as shown).

Wait, actually $\sum g_i g_{i+1} \leq (\sum g_i)^2/4 = M^2/4$ only for bipartite graphs. For non-bipartite (odd cycles), the bound might be different.

For odd $n$: $\sum g_i g_{i+1}$ with $\sum g_i = M$. The maximum is... for $n = 5$, $M = 1$: $1/4$. For $M = 2$: concentrate on two adjacent, $g_1 = g_2 = 1$, $\sum g_i g_{i+1} = 1 = M^2/4 = 1$. ✓

Actually for any $n \geq 4$, $\sum g_i g_{i+1} \leq M^2/4$ (concentrate on one edge). This is because the cycle $C_n$ for $n \geq 4$ has the property that the max of $\sum g_i g_{i+1}$ with $\sum g_i = M$ is $M^2/4$ (put $M/2$ on each of two adjacent vertices).

So $T \leq n - M + M^2/4 - \sum g_i m_{i+1}$.

And $\sum g_i m_{i+1} \geq 0$, so $T \leq n - M + M^2/4$.

Maximize $n - M + M^2/4$ over $M \geq 1$: $f(M) = n - M + M^2/4$, $f'(M) = -1 + M/2 = 0 \Rightarrow M = 2$. $f(2) = n - 2 + 1 = n - 1$. $f(1) = n - 1 + 1/4 = n - 3/4$.

Since $f(1) = n - 3/4 > n - 1 = f(2)$ for all $n$, and $f$ is convex (minimized at $M = 2$), the maximum over $M \geq 1$ is at $M = 1$: $f(1) = n - 3/4$.

But wait, this upper bound $T \leq n - M + M^2/4$ might not be tight because we also have the $-\sum g_i m_{i+1}$ term. Let me reconsider.

$T = n - M + \sum g_i g_{i+1} - \sum g_i m_{i+1}$.

With $M = 1$, $m_k = 1$ for some $k$: $T = n - 1 + \sum g_i g_{i+1} - g_{k-1}$.

We showed the max is $n - 1 + 1/4 = n - 3/4$ (by making $g_{k-1} \to 0$ and concentrating $g$ on an edge not involving $k-1$).

With $M = 2$: we could have $m_k = 2$ or $m_k = m_j = 1$.

Case $m_k = 2$: $T = n - 2 + \sum g_i g_{i+1} - 2g_{k-1}$. Max: $\sum g_i g_{i+1} \leq 1$ (with $\sum g_i = 2$), $g_{k-1} \to 0$: $T \to n - 2 + 1 = n - 1$.

Case $m_k = m_j = 1$ ($k \neq j$): $T = n - 2 + \sum g_i g_{i+1} - g_{k-1} - g_{j-1}$. Max: $\sum g_i g_{i+1} \leq 1$, $g_{k-1}, g_{j-1} \to 0$: $T \to n - 1$.

Both give $n - 1 < n - 3/4$.

For $M \geq 3$: $T \leq n - M + M^2/4$. $f(3) = n - 3 + 9/4 = n - 3/4$. Same as $M = 1$!

But can we achieve $n - 3/4$ with $M = 3$? We need $\sum g_i g_{i+1} = M^2/4 = 9/4$ and $\sum g_i m_{i+1} = 0$.

$\sum g_i g_{i+1} = 9/4$ with $\sum g_i = 3$: concentrate on two adjacent, $g_1 = g_2 = 3/2$. But $g_i \leq 1$! So this is infeasible.

With $g_i \leq 1$: $\sum g_i g_{i+1} \leq ?$ with $\sum g_i = 3$, $g_i \leq 1$.

If $g_1 = g_2 = 1, g_3 = 1$, rest 0: $\sum g_i g_{i+1} = 1 + 1 + 0 + \ldots = 2$ (for $n \geq 5$; the terms $g_1 g_2 + g_2 g_3 = 1 + 1 = 2$).

Actually for $n = 4$: $g_1 = g_2 = g_3 = 1, g_4 = 0$: $\sum = g_1 g_2 + g_2 g_3 + g_3 g_4 + g_4 g_1 = 1 + 1 + 0 + 0 = 2$.

So $\sum g_i g_{i+1} \leq 2$ with $\sum g_i = 3$, $g_i \leq 1$. (Concentrate on a path of 3 vertices.)

$T \leq n - 3 + 2 - \sum g_i m_{i+1} \leq n - 1$. Less than $n - 3/4$.

What about $M = 3$ with $g_1 = g_2 = 1, g_3 = 1$, and $m$ placed so that $\sum g_i m_{i+1} = 0$? We need $m_{i+1} = 0$ whenever $g_i > 0$, i.e., $m_2 = m_3 = m_4 = 0$ (since $g_1, g_2, g_3 > 0$). So $m_1 = 3$ (all integer mass at position 1). Then $\sum g_i m_{i+1} = g_4 \cdot m_1 = 0 \cdot 3 = 0$ (since $g_4 = 0$). But $g_4 = 0$ means $f_4 = 1$, which violates $f_i < 1$.

So we need $g_4 > 0$, meaning $\sum g_i m_{i+1} > 0$ if $m_1 > 0$. Specifically, $\sum g_i m_{i+1} = g_4 \cdot m_1 = g_4 \cdot 3 > 0$.

So $T = n - 3 + 2 - 3g_4 < n - 1$. As $g_4 \to 0$, $T \to n - 1$. Still less than $n - 3/4$.

So $M = 1$ is indeed optimal, giving $\lambda(n) = n - 3/4$.

Hmm, but I realize I should also check: is the bound $\sum g_i g_{i+1} \leq 1/4$ with $\sum g_i = 1$ tight for the cycle? Yes, as shown: $g_1 = g_2 = 1/2$ gives $1/4$.

And we need $g_{k-1} \to 0$ while concentrating on $g_1, g_2$. For $n \geq 4$, we can choose $k$ such that $k - 1 \notin \{1, 2\}$ (i.e., $k \neq 2, 3$). For $n \geq 4$, this is possible. For $n = 4$, $k = 4$ gives $k - 1 = 3 \notin \{1, 2\}$. ✓

So the answer is $\lambda(n) = n - \frac{3}{4}$ for $n \geq 4$.

Wait, but I need to double-check that the supremum is not achieved (so that $\leq$ holds). In our construction, $g_{k-1} = \epsilon > 0$ and the sum is $n - 3/4 - \epsilon < n - 3/4$. As $\epsilon \to 0$, it approaches $n - 3/4$ but never reaches it. So $\sum \{a_i\} a_{i+1} < n - 3/4$ always, hence $\leq n - 3/4$ holds. And for any $\lambda < n - 3/4$, we can find $a_i$ with $\sum \{a_i\} a_{i+1} > \lambda$. So $\lambda(n) = n - 3/4$.

Actually, hold on. I need to verify that the supremum is exactly $n - 3/4$ and not something else. Let me also check: can we achieve exactly $n - 3/4$?

At $\epsilon = 0$: $g_1 = g_2 = 1/2$, $g_3 = g_4 = \ldots = g_n = 0$. But $g_i = 0$ means $f_i = 1$, which is not allowed ($f_i < 1$). So the supremum is not achieved.

But actually, can we have $f_i = 1$? No, because $\{a_i\} \in [0, 1)$. So $f_i < 1$ always, meaning $g_i > 0$ always. The supremum $n - 3/4$ is not achieved, but it's the least upper bound. So $\lambda(n) = n - 3/4$.

Hmm, but I want to make sure I haven't made an error. Let me re-examine the formula.

$T = n - M + \sum g_i(g_{i+1} - m_{i+1})$ where $g_i = 1 - f_i$, $\sum g_i = M$.

With $M = 1$, $m_n = 1$:
$T = n - 1 + \sum g_i g_{i+1} - g_{n-1} \cdot m_n = n - 1 + \sum g_i g_{i+1} - g_{n-1}$.

Wait, $\sum g_i m_{i+1} = g_{n-1} \cdot m_n + \text{other terms with } m_{i+1} = 0 = g_{n-1} \cdot 1 = g_{n-1}$.

So $T = n - 1 + \sum g_i g_{i+1} - g_{n-1}$. ✓

With $g_1 = g_2 = 1/2 - (n-2)\epsilon/2$, $g_3 = \ldots = g_n = \epsilon$:

$\sum g_i = 2(1/2 - (n-2)\epsilon/2) + (n-2)\epsilon = 1 - (n-2)\epsilon + (n-2)\epsilon = 1$. ✓

$\sum g_i g_{i+1} = g_1 g_2 + g_2 g_3 + g_3 g_4 + \ldots + g_{n-1} g_n + g_n g_1$

$= (1/2 - (n-2)\epsilon/2)^2 + (1/2 - (n-2)\epsilon/2)\epsilon + \epsilon^2(n-3) + \epsilon \cdot (1/2 - (n-2)\epsilon/2) + \ldots$

As $\epsilon \to 0$: $\sum g_i g_{i+1} \to 1/4$. $g_{n-1} = \epsilon \to 0$.

$T \to n - 1 + 1/4 = n - 3/4$. ✓

Now let me also verify that we can't exceed $n - 3/4$.

$T = n - 1 + \sum g_i g_{i+1} - g_{n-1} \leq n - 1 + \sum g_i g_{i+1}$.

And $\sum g_i g_{i+1} \leq 1/4$ (with $\sum g_i = 1$ on a cycle of length $\geq 4$).

But we also subtract $g_{n-1} \geq 0$. So $T \leq n - 1 + 1/4 = n - 3/4$.

But this bound might not be tight because to achieve $\sum g_i g_{i+1} = 1/4$, we need $g_1 = g_2 = 1/2$ and all others 0, but then $g_{n-1} = 0$, which is fine (it's the limit). So the bound is tight in the limit.

Actually, I realize I need to be more careful. The bound $\sum g_i g_{i+1} \leq 1
