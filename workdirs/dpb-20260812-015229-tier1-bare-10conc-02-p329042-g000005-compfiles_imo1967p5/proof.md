# IMO 1967 Problem 5 — Solution

## Problem

Consider the sequence $\{c_n\}$, where $c_n = a_1^n + a_2^n + \cdots + a_8^n$, in which $a_1, a_2, \ldots, a_8$ are real numbers, not all equal to zero. Suppose that infinitely many terms of $\{c_n\}$ are equal to zero. Find all natural numbers $n$ such that $c_n = 0$.

## Answer

$$\boxed{c_n = 0 \iff n \text{ is odd.}}$$

That is, the set of natural numbers $n$ with $c_n = 0$ is exactly $\{1, 3, 5, 7, \ldots\}$.

---

## Proof

### Step 1: Even indices never vanish

For any even $n = 2k$ with $k \geq 1$:

$$c_{2k} = \sum_{i=1}^{8} a_i^{2k} = \sum_{i=1}^{8} \left(a_i^2\right)^k.$$

Since each $a_i^2 \geq 0$, every term $\left(a_i^2\right)^k \geq 0$, so $c_{2k} \geq 0$. Moreover, $c_{2k} = 0$ would require every $a_i^2 = 0$, i.e., every $a_i = 0$. But the hypothesis states that not all $a_i$ are zero, so at least one term $\left(a_i^2\right)^k > 0$. Therefore:

$$c_{2k} > 0 \quad \text{for all } k \geq 1. \tag{1}$$

Since all even-indexed terms are strictly positive, **every zero of the sequence must occur at an odd index**. Combined with the hypothesis that infinitely many terms are zero, we conclude that **infinitely many odd-indexed terms $c_{2k+1}$ are zero**.

### Step 2: Rewrite the odd-indexed subsequence

Group the $a_i$ by their distinct absolute values. Let the distinct **nonzero** absolute values among the $a_i$ be

$$r_1 > r_2 > \cdots > r_s > 0.$$

(Any $a_i = 0$ contributes $0$ to $c_n$ for all $n \geq 1$ and can be ignored.)

For each $r_\ell$, let $p_\ell$ be the number of indices $i$ with $a_i = +r_\ell$, and $q_\ell$ the number with $a_i = -r_\ell$. Set $\gamma_\ell = r_\ell^2$ and note $\gamma_1 > \gamma_2 > \cdots > \gamma_s > 0$.

For odd $n = 2k+1$:

$$c_{2k+1} = \sum_{\ell=1}^{s} \left(p_\ell \, r_\ell^{2k+1} + q_\ell \, (-r_\ell)^{2k+1}\right) = \sum_{\ell=1}^{s} (p_\ell - q_\ell)\, r_\ell \cdot \gamma_\ell^k.$$

Define $d_\ell = (p_\ell - q_\ell)\, r_\ell$. Then:

$$c_{2k+1} = \sum_{\ell=1}^{s} d_\ell \, \gamma_\ell^k. \tag{2}$$

### Step 3: Infinitely many zeros force all coefficients to vanish

We claim: if infinitely many $c_{2k+1} = 0$, then $d_\ell = 0$ for every $\ell$.

Suppose for contradiction that not all $d_\ell$ are zero. Let $\ell^*$ be the **largest** index with $d_{\ell^*} \neq 0$. Factor out the leading term from (2):

$$c_{2k+1} = d_{\ell^*}\, \gamma_{\ell^*}^k \left(1 + \sum_{\ell > \ell^*} \frac{d_\ell}{d_{\ell^*}} \left(\frac{\gamma_\ell}{\gamma_{\ell^*}}\right)^k \right).$$

Since $\gamma_\ell < \gamma_{\ell^*}$ for all $\ell > \ell^*$, each ratio $\left(\frac{\gamma_\ell}{\gamma_{\ell^*}}\right)^k \to 0$ as $k \to \infty$. Therefore the parenthetical factor tends to $1$, and in particular exceeds $\frac{1}{2}$ for all sufficiently large $k$. Since $d_{\ell^*} \neq 0$ and $\gamma_{\ell^*} > 0$, we get $c_{2k+1} \neq 0$ for all sufficiently large $k$.

This means only **finitely many** odd-indexed terms are zero—contradicting the fact that infinitely many are zero (established in Step 1). $\quad\Rightarrow\!\Leftarrow$

Therefore $d_\ell = 0$ for every $\ell$, i.e.:

$$p_\ell = q_\ell \quad \text{for all } \ell = 1, \ldots, s. \tag{3}$$

### Step 4: All odd-indexed terms vanish

With $d_\ell = 0$ for all $\ell$, equation (2) gives:

$$c_{2k+1} = 0 \quad \text{for all } k \geq 0. \tag{4}$$

### Step 5: Conclusion

Combining (1) and (4):

- $c_n > 0$ for every **even** $n$ (so $c_n \neq 0$).
- $c_n = 0$ for every **odd** $n$.

Therefore, under the hypothesis that infinitely many terms of $\{c_n\}$ are zero, the set of natural numbers $n$ for which $c_n = 0$ is precisely the set of all **odd** natural numbers:

$$\boxed{n \in \{1, 3, 5, 7, \ldots\}.}$$

**QED.**

---

## Remark on the structure

Condition (3) says: for every nonzero absolute value $r$ appearing among the $a_i$, the number of $a_i$ equal to $+r$ equals the number equal to $-r$. In other words, the nonzero $a_i$ can be partitioned into pairs $(r, -r)$. This is exactly the condition under which all odd power sums vanish—a classical fact. The content of the problem is showing that this is the **only** way to obtain infinitely many zeros, which the leading-term (dominant balance) argument in Step 3 establishes.
