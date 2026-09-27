# Solution

## Answer

$$\boxed{38 \cdot 2026^3 = 316010795888}$$

## Proof

**Setup and notation.** Let $a_0 = 0$. The sequence $0 = a_0 < a_1 \le a_2 \le \cdots \le a_{37} = 2026$ is nondecreasing with $a_{37} = 2026$. For each positive integer $n$, $b_n = \min\{m \ge 1 : a_m \ge n\}$.

**Key observation: block structure of $b_n$.** For each $k \ge 1$, the values of $n$ satisfying $b_n = k$ are exactly
$$\{n : a_{k-1} < n \le a_k\} = \{a_{k-1}+1, \ldots, a_k\}.$$
This is because $b_n = k$ iff $a_k \ge n$ and $a_{k-1} < n$ (for $k \ge 2$), and $b_n = 1$ iff $a_1 \ge n$ (i.e., $n \le a_1$, matching $a_0 = 0$). If $a_k = a_{k-1}$, this block is empty and no $n$ has $b_n = k$; this is consistent.

Since $a_{37} = 2026$, for every $n \in \{1, \ldots, 2026\}$ we have $a_{37} \ge n$, so $b_n \le 37$. Thus $b_n$ is determined by $a_1, \ldots, a_{37}$, and the blocks $\{a_{k-1}+1, \ldots, a_k\}$ for $k = 1, \ldots, 37$ partition $\{1, \ldots, 2026\}$.

**Telescoping identity.** Note that $3n^2 - 3n + 1 = n^3 - (n-1)^3$, so
$$\sum_{n=a_{k-1}+1}^{a_k} (3n^2 - 3n + 1) = \sum_{n=a_{k-1}+1}^{a_k} \bigl(n^3 - (n-1)^3\bigr) = a_k^3 - a_{k-1}^3.$$

**Rewriting the second sum.** Using the block structure:
$$\sum_{n=1}^{2026} (3n^2 - 3n + 1)\, b_n = \sum_{k=1}^{37} k \sum_{n=a_{k-1}+1}^{a_k} (3n^2 - 3n + 1) = \sum_{k=1}^{37} k\bigl(a_k^3 - a_{k-1}^3\bigr).$$

**Abel summation (summation by parts).** Expanding:
$$\sum_{k=1}^{37} k\, a_k^3 - \sum_{k=1}^{37} k\, a_{k-1}^3 = \sum_{k=1}^{37} k\, a_k^3 - \sum_{k=0}^{36} (k+1)\, a_k^3.$$

Since $a_0 = 0$, the $k=0$ term vanishes, giving:
$$= \sum_{k=1}^{37} k\, a_k^3 - \sum_{k=1}^{36} (k+1)\, a_k^3 = 37\, a_{37}^3 + \sum_{k=1}^{36}\bigl(k - (k+1)\bigr)\, a_k^3 = 37\, a_{37}^3 - \sum_{k=1}^{36} a_k^3.$$

**Combining.** The full expression is:
$$E = \sum_{i=1}^{37} a_i^3 + \left(37\, a_{37}^3 - \sum_{k=1}^{36} a_k^3\right) = a_{37}^3 + \sum_{i=1}^{36} a_i^3 + 37\, a_{37}^3 - \sum_{k=1}^{36} a_k^3 = 38\, a_{37}^3.$$

Since $a_{37} = 2026$:
$$E = 38 \times 2026^3 = 38 \times 8316073576 = 316010795888.$$

**Conclusion.** The expression equals $38 \cdot 2026^3$ for **every** valid sequence satisfying the constraints — the intermediate values $a_1, \ldots, a_{36}$ cancel completely. Therefore the maximum (and only) possible value is:

$$\boxed{316010795888}$$

$\blacksquare$
