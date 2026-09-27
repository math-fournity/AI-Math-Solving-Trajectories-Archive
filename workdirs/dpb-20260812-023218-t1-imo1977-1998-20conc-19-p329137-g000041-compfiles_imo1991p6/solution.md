# IMO 1991 Problem 6 — Solution

## Problem

Given any real number $a > 1$, construct a bounded infinite sequence $x_0, x_1, x_2, \ldots$ of real numbers such that

$$|x_i - x_j| \cdot |i - j|^a \geq 1$$

for every pair of distinct nonnegative integers $i, j$.

---

## Construction

Let $d_k(n) = \lfloor n / 2^k \rfloor \bmod 2 \in \{0, 1\}$ be the $k$-th binary digit of $n$.

Set $\alpha = 2^{-a} \in (0, \tfrac{1}{2})$ and define:

$$\boxed{x_n \;=\; \frac{1 - \alpha}{1 - 2\alpha} \sum_{k=0}^{\infty} d_k(n)\, \alpha^k \;=\; \frac{1 - 2^{-a}}{1 - 2^{1-a}} \sum_{k=0}^{\infty} d_k(n)\, 2^{-ka}.}$$

(Since $n$ is a nonneg integer, only finitely many $d_k(n)$ are nonzero, so the sum is finite.)

**Claim.** The sequence $(x_n)$ is bounded and satisfies $|x_i - x_j| \cdot |i-j|^a \geq 1$ for all $i \neq j$.

---

## Proof

### Key lemma (binary digit separation)

**Lemma.** If $i \neq j$ and $r$ is the **lowest** bit position at which $i$ and $j$ differ, then $|i - j| \geq 2^r$.

*Proof.* Since bits $0, 1, \ldots, r-1$ are identical for $i$ and $j$, we have

$$i - j = \bigl(d_r(i) - d_r(j)\bigr) 2^r + \sum_{k > r} \bigl(d_k(i) - d_k(j)\bigr) 2^k.$$

The first term is $\pm 2^r$. Every term in the sum is a multiple of $2^{r+1}$. Therefore $i - j = 2^r \cdot (\pm 1 + 2m)$ for some integer $m$, so $|i-j| = 2^r \cdot |{\pm 1 + 2m}| \geq 2^r$ (since $\pm 1 + 2m$ is a nonzero odd integer). $\square$

### Notation

Let $v_k = \frac{1-\alpha}{1-2\alpha}\,\alpha^k$ and $T_r = \sum_{k \geq r} v_k = \frac{1-\alpha}{1-2\alpha} \cdot \frac{\alpha^r}{1-\alpha} = \frac{\alpha^r}{1-2\alpha}$.

Note $x_n = \sum_k d_k(n)\, v_k$.

### Boundedness

Since $d_k(n) \in \{0,1\}$ and $v_k > 0$:

$$0 \;\leq\; x_n \;=\; \sum_k d_k(n)\, v_k \;\leq\; \sum_{k=0}^{\infty} v_k \;=\; T_0 \;=\; \frac{1}{1 - 2\alpha} \;=\; \frac{1}{1 - 2^{1-a}}.$$

This is finite because $a > 1 \Rightarrow 2^{1-a} < 1$. So $|x_n| \leq C := \frac{1}{1-2^{1-a}}$ for all $n$.

### Separation property

Let $i \neq j$ and let $r$ be the lowest differing bit. Then $|i - j| \geq 2^r$ by the Lemma, so $\frac{1}{|i-j|^a} \leq \frac{1}{2^{ra}} = \alpha^r$.

Now compute:

$$x_i - x_j = \sum_{k \geq r} \bigl(d_k(i) - d_k(j)\bigr)\, v_k.$$

Split off the $k = r$ term (where $|d_r(i) - d_r(j)| = 1$) from the tail:

$$x_i - x_j = \underbrace{\bigl(d_r(i) - d_r(j)\bigr)}_{\pm 1}\, v_r \;+\; \sum_{k > r} \bigl(d_k(i) - d_k(j)\bigr)\, v_k.$$

By the triangle inequality:

$$|x_i - x_j| \;\geq\; v_r \;-\; \sum_{k > r} |d_k(i) - d_k(j)|\, v_k \;\geq\; v_r \;-\; \sum_{k > r} v_k \;=\; v_r - T_{r+1}.$$

Compute this explicitly:

$$v_r - T_{r+1} = \frac{(1-\alpha)\,\alpha^r}{1-2\alpha} - \frac{\alpha^{r+1}}{1-2\alpha} = \frac{\alpha^r\bigl[(1-\alpha) - \alpha\bigr]}{1-2\alpha} = \frac{\alpha^r(1 - 2\alpha)}{1-2\alpha} = \alpha^r = 2^{-ra}.$$

Therefore:

$$|x_i - x_j| \;\geq\; 2^{-ra} \;\geq\; \frac{1}{|i-j|^a},$$

which gives $|x_i - x_j| \cdot |i-j|^a \geq 1$. $\quad\blacksquare$

---

## Summary

| Quantity | Value |
|---|---|
| Construction | $x_n = \dfrac{1-2^{-a}}{1-2^{1-a}} \displaystyle\sum_{k \ge 0} d_k(n)\, 2^{-ka}$ |
| Bound $C$ | $\dfrac{1}{1-2^{1-a}}$ (finite for $a>1$) |
| Key idea | Binary digits of $n$ as coefficients; weights $v_k \propto 2^{-ka}$ chosen so each weight exceeds the total tail, giving $v_r - T_{r+1} = 2^{-ra}$ exactly |

**Intuition.** The number $x_n$ is the "value" of $n$'s binary expansion read in base $\alpha = 2^{-a}$ (instead of base 2). Two integers that first differ at bit $r$ are at least $2^r$ apart as integers, and their $x$-values differ by at least $\alpha^r = 2^{-ra} = 1/(2^r)^a \geq 1/|i-j|^a$. The weights decay geometrically (ratio $\alpha < 1/2$), so each weight dominates the entire remaining tail — this is what makes the lower bound work — while the total sum $\sum v_k$ converges, giving boundedness.
