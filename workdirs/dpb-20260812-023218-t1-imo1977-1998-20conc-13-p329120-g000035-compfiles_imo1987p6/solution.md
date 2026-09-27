# IMO 1987 Problem 6 — Solution

**Problem.** Let $n \ge 2$ be an integer. Prove that if $k^2 + k + n$ is prime for all integers $k$ with $0 \le k \le \sqrt{n/3}$, then $k^2 + k + n$ is prime for all integers $k$ with $0 \le k \le n - 2$.

---

## Setup

Let $f(k) = k^2 + k + n$. We prove the **contrapositive**:

> If $f(k)$ is composite for some integer $k$ with $0 \le k \le n-2$, then $f(k)$ is composite for some integer $k$ with $0 \le k \le \sqrt{n/3}$.

Let $k_0$ be the **smallest** integer in $\{0, 1, \ldots, n-2\}$ such that $f(k_0)$ is composite. We shall prove $k_0 \le \sqrt{n/3}$.

Let $p$ be the **smallest prime factor** of $f(k_0)$.

---

## Case 1: $k_0 = 0$

Then $f(0) = n$ is composite, and $0 \le \sqrt{n/3}$ (since $n \ge 2$). ∎

---

## Case 2: $k_0 \ge 1$

Then $f(0) = n$ is prime (by minimality of $k_0$). Since $n \ge 2$ is prime, $n$ is odd, so $f(k) = k(k+1) + n$ is always odd (as $k(k+1)$ is even). Hence $p \ne 2$, so **$p$ is odd**.

### Key observation: at most one $k \ge 0$ satisfies $f(k) = p$

If $f(k) = p$, then $k^2 + k = p - n$. Since $g(k) = k^2 + k$ is strictly increasing for $k \ge 0$ (as $g(k+1) - g(k) = 2k+2 > 0$), there is **at most one** non-negative integer $k$ with $g(k) = p - n$.

### Counting residues: the roots of $f(k) \equiv 0 \pmod{p}$

Since $p \mid f(k_0)$, we have $k_0^2 + k_0 \equiv -n \pmod{p}$. The congruence $k^2 + k + n \equiv 0 \pmod{p}$ has two roots modulo $p$:

$$k \equiv k_0 \pmod{p} \quad \text{and} \quad k \equiv -k_0 - 1 \pmod{p}.$$

(These are the two roots of $x^2 + x \equiv k_0^2 + k_0 \pmod{p}$, namely $x = k_0$ and $x = -k_0 - 1$.)

Write $k_0 = a + mp$ where $a = k_0 \bmod p$ (so $0 \le a < p$) and $m \ge 0$. Set $b = (-k_0 - 1) \bmod p = p - 1 - a$ (using $p$ odd). Note $a + b = p - 1$.

**Every** integer $k \in \{0, 1, \ldots, k_0 - 1\}$ with $p \mid f(k)$ satisfies, by minimality of $k_0$, that $f(k)$ is prime — hence $f(k) = p$. By the key observation above, there is **at most one** such $k$.

### Counting elements in $\{0, \ldots, k_0-1\}$ with $p \mid f(k)$

These are the integers in $\{0, \ldots, k_0 - 1\}$ congruent to $a$ or $b$ modulo $p$.

- **Residue $a$:** the values $a, a+p, \ldots, a+(m-1)p$ — exactly $m$ of them, all $< k_0 = a + mp$.

- **Residue $b$:** the values $b, b+p, \ldots, b+jp < k_0$. The count depends on whether $a > b$, $a < b$, or $a = b$:
  - If $a > b$: the largest valid $j$ satisfies $b + jp < a + mp$, giving $j \le m$, so $m+1$ values.
  - If $a < b$: similarly $j \le m - 1$, so $m$ values (for $m \ge 1$; for $m = 0$, $b > a = k_0$ so $0$ values).
  - If $a = b$ (i.e., $a = \frac{p-1}{2}$, a double root): only one progression, $m$ values.

**Total count** of $k \in \{0, \ldots, k_0 - 1\}$ with $p \mid f(k)$:

| | $a > b$ | $a < b$ | $a = b$ |
|---|---|---|---|
| $m = 0$ | $0 + 1 = 1$ | $0 + 0 = 0$ | $0$ |
| $m = 1$ | $1 + 2 = 3$ | $1 + 1 = 2$ | $1$ |
| $m \ge 2$ | $\ge 5$ | $\ge 4$ | $\ge 2$ |

Since the count must be $\le 1$, the only viable cases are:

1. **$m = 0$, $a > b$** (count $= 1$),
2. **$m = 0$, $a < b$** (count $= 0$),
3. **$m = 0$, $a = b$** (count $= 0$),
4. **$m = 1$, $a = b$** (count $= 1$).

All other cases are **impossible** (count $\ge 2$, contradicting the key observation).

---

### Subcase 2a: $m = 0$, $a > b$ (i.e., $k_0 < p$ and $k_0 > \frac{p-1}{2}$, so $p \le 2k_0$)

There is exactly one $k = b = p - 1 - k_0 < k_0$ with $f(b) = p$, giving $n = p - b(b+1)$.

Compute $f(k_0)$:
$$f(k_0) = k_0(k_0+1) - b(b+1) + p = p(2k_0 + 2 - p),$$
using $a + b = p - 1$ (a direct expansion verifies this).

Since $p$ is the **smallest** prime factor of $f(k_0) = p \cdot (2k_0 + 2 - p)$, we need $2k_0 + 2 - p \ge p$, i.e., $p \le k_0 + 1$. Combined with $p > k_0$ (from $m = 0$):

$$p = k_0 + 1.$$

Then $b = p - 1 - k_0 = 0$, so $n = p - 0 = k_0 + 1$, giving $k_0 = n - 1 > n - 2$. **This contradicts** $k_0 \le n - 2$. So this subcase is **impossible**.

---

### Subcase 2b: $m = 0$, $a < b$ (i.e., $k_0 < p$ and $k_0 < \frac{p-1}{2}$, so $p > 2k_0 + 1$)

No $k < k_0$ has $p \mid f(k)$. Since $f(k_0)$ is composite with smallest prime factor $p$:

$$f(k_0) = k_0^2 + k_0 + n \ge p^2 > (2k_0 + 1)^2 = 4k_0^2 + 4k_0 + 1.$$

Therefore:
$$n > 3k_0^2 + 3k_0 + 1 > 3k_0^2,$$

so $k_0 < \sqrt{n/3}$, hence $k_0 \le \sqrt{n/3}$. ∎

---

### Subcase 2c: $m = 0$, $a = b$ (i.e., $k_0 = \frac{p-1}{2}$, so $p = 2k_0 + 1$)

No $k < k_0$ has $p \mid f(k)$. Same as Subcase 2b:

$$f(k_0) \ge p^2 = (2k_0 + 1)^2 = 4k_0^2 + 4k_0 + 1,$$

$$n > 3k_0^2, \quad k_0 < \sqrt{n/3}. \quad \square$$

---

### Subcase 2d: $m = 1$, $a = b$ (i.e., $k_0 = \frac{p-1}{2} + p = \frac{3p-1}{2}$)

There is one $k = a = \frac{p-1}{2}$ with $f(a) = p$, giving:

$$n = p - a(a+1) = p - \frac{p-1}{2} \cdot \frac{p+1}{2} = p - \frac{p^2 - 1}{4} = \frac{5 - (p-2)^2}{4}.$$

For $n \ge 2$: $5 - (p-2)^2 \ge 8 \implies (p-2)^2 \le -3$, which is **impossible**. So this subcase cannot occur.

---

## Conclusion

In every possible case:
- $k_0 = 0$: trivially $k_0 \le \sqrt{n/3}$.
- Subcase 2b or 2c: $k_0 < \sqrt{n/3}$.
- Subcases 2a and 2d: impossible.

Therefore $k_0 \le \sqrt{n/3}$, proving the contrapositive. $\blacksquare$
