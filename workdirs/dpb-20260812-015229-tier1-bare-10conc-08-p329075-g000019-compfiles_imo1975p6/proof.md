# IMO 1975 Problem 6 — Solution

## Problem

Find all polynomials $P(x,y)$ in two variables such that:

1. **(Homogeneity)** For some positive integer $n$ and all real $t, x, y$: $P(tx, ty) = t^n P(x, y)$.
2. **(Cyclic identity)** For all real $a, b, c$: $P(b+c,\, a) + P(c+a,\, b) + P(a+b,\, c) = 0$.
3. **(Normalization)** $P(1, 0) = 1$.

## Answer

For each positive integer $n \geq 1$, the unique solution is

$$\boxed{P(x, y) = (x - 2y)(x + y)^{\,n-1}}.$$

---

## Proof

### Step 1. Setup and parametrization

Write the homogeneous degree-$n$ polynomial as

$$P(x, y) = \sum_{k=0}^{n} c_k\, x^{n-k} y^k, \qquad c_0 = P(1,0) = 1.$$

Introduce $s = a + b + c$ and define

$$G_s(t) := P(s - t,\; t).$$

Since $P$ is homogeneous of degree $n$, the function $G_s(t)$ is homogeneous of degree $n$ in the pair $(s, t)$, so we may write

$$G_s(t) = \sum_{k=0}^{n} \alpha_k\, s^{n-k}\, t^k$$

for constants $\alpha_0, \ldots, \alpha_n$ (determined by the $c_k$). Note $b + c = s - a$, $c + a = s - b$, $a + b = s - c$, so condition (ii) becomes

$$G_s(a) + G_s(b) + G_s(c) = 0 \quad \text{whenever } a + b + c = s. \tag{$\star$}$$

Setting $c = s - a - b$, this is a polynomial identity in $a, b, s$. Substituting $u = a/s$, $v = b/s$ (and dividing by $s^n$), it becomes the identity in $u, v$:

$$H(u, v) := \sum_{k=0}^{n} \alpha_k\bigl[u^k + v^k + (1 - u - v)^k\bigr] = 0. \tag{$\star\star$}$$

**Initial data.** From $G_s(0) = P(s, 0) = s^n$ we get $\alpha_0 = 1$. From $G_s(s) = P(0, s) = s^n P(0,1)$ and (setting $a = s, b = c = 0$ in $(\star)$) $G_s(s) + 2\,G_s(0) = 0$, i.e. $G_s(s) = -2\,s^n$, we get

$$\sum_{k=0}^{n} \alpha_k = -2. \tag{1}$$

### Step 2. Kill the even-index coefficients ($k \geq 2$)

Specialize $(\star\star)$ at $v = -u$ (so $1 - u - v = 1$):

$$\sum_{k=0}^{n} \alpha_k\bigl[u^k + (-u)^k + 1\bigr] = 0.$$

For **odd** $k$: $u^k + (-u)^k = 0$, contributing $\alpha_k \cdot 1$. For **even** $k$: contributing $\alpha_k(2u^k + 1)$. Hence

$$2\sum_{\substack{k \text{ even}}} \alpha_k\, u^k \;+\; \sum_{k=0}^{n} \alpha_k \;=\; 0 \quad\Longrightarrow\quad \sum_{\substack{k \text{ even}}} \alpha_k\, u^k \;=\; 1,$$

using (1). Since $\alpha_0 = 1$, this forces

$$\alpha_k = 0 \quad \text{for all even } k \geq 2. \tag{2}$$

### Step 3. Kill the odd-index coefficients ($k \geq 3$) and pin down $\alpha_1$

Specialize $(\star\star)$ at $v = 0$ (so $1 - u - v = 1 - u$):

$$\sum_{k=0}^{n} \alpha_k\bigl[u^k + (1-u)^k\bigr] = 0$$

(where the $k=0$ term is $1 + 1 + 1 = 3$, contributing $3\alpha_0$). Using (2) this reduces to

$$3 + \alpha_1 + \sum_{\substack{k \geq 3 \\ k \text{ odd}}} \alpha_k\bigl[u^k + (1-u)^k\bigr] = 0. \tag{3}$$

For **odd** $k$, the polynomial $u^k + (1-u)^k$ has degree $k - 1$ (the leading $u^k$ terms cancel) and constant term $1$ (value at $u=0$). Subtract the constant:

$$u^k + (1-u)^k - 1 \quad \text{has degree } k-1, \quad \text{with leading term } k\, u^{k-1}.$$

The polynomials $\bigl\{u^k + (1-u)^k - 1 : k \text{ odd},\; k \geq 3\bigr\}$ have **distinct degrees** $2, 4, 6, \ldots$, hence are **linearly independent**. Rewriting (3) as

$$\bigl(3 + \alpha_1 + \sum_{\substack{k \geq 3 \\ k \text{ odd}}} \alpha_k\bigr) + \sum_{\substack{k \geq 3 \\ k \text{ odd}}} \alpha_k\bigl[u^k + (1-u)^k - 1\bigr] = 0,$$

linear independence forces every $\alpha_k = 0$ for odd $k \geq 3$, and then the constant part gives

$$3 + \alpha_1 = 0 \quad\Longrightarrow\quad \alpha_1 = -3. \tag{3}$$

### Step 4. Conclusion of uniqueness

Combining all results:

$$\alpha_0 = 1,\quad \alpha_1 = -3,\quad \alpha_k = 0 \;\text{ for all } k \geq 2.$$

Therefore

$$G_s(t) = s^n - 3\,s^{n-1}\, t.$$

Recovering $P$: set $x = s - t$, $y = t$, so $s = x + y$:

$$P(x, y) = (x+y)^n - 3(x+y)^{n-1}\, y = (x+y)^{n-1}\bigl[(x+y) - 3y\bigr] = (x - 2y)(x + y)^{n-1}.$$

### Step 5. Verification

Let $P(x,y) = (x - 2y)(x+y)^{n-1}$.

- **(i) Homogeneity:** degree $1 + (n-1) = n$; $P(tx,ty) = (tx - 2ty)(tx+ty)^{n-1} = t \cdot t^{n-1}(x-2y)(x+y)^{n-1} = t^n P(x,y)$. ✓
- **(iii) Normalization:** $P(1,0) = (1)(1)^{n-1} = 1$. ✓
- **(ii) Cyclic identity:** With $s = a+b+c$,
$$P(b+c, a) = (s - 3a)\,s^{n-1}, \quad P(c+a, b) = (s - 3b)\,s^{n-1}, \quad P(a+b, c) = (s - 3c)\,s^{n-1}.$$
Summing:
$$s^{n-1}\bigl[(s-3a)+(s-3b)+(s-3c)\bigr] = s^{n-1}\bigl[3s - 3(a+b+c)\bigr] = s^{n-1}(3s - 3s) = 0. \quad\checkmark$$

All three conditions are satisfied. $\blacksquare$

---

## Summary

For every positive integer $n \geq 1$, the unique polynomial satisfying all three conditions is

$$P(x, y) = (x - 2y)(x + y)^{n-1}.$$

The proof of uniqueness proceeds by converting condition (ii) into the identity $H(u,v) \equiv 0$, then extracting all coefficients via two specializations: $v = -u$ (which annihilates all even-index coefficients $\alpha_k$ for $k \geq 2$) and $v = 0$ (which, using the linear independence of polynomials of distinct degrees, annihilates all odd-index coefficients $\alpha_k$ for $k \geq 3$ and fixes $\alpha_1 = -3$). The normalization $P(1,0) = 1$ fixes $\alpha_0 = 1$, yielding the unique solution. **QED.**
