# Solution

## Answer

$$\boxed{76988}$$

## Key Observation: the $a$–$b$ complementarity

Recall $b_n = \min\{m \ge 1 : a_m \ge n\}$. Since $(a_m)$ is nondecreasing and unbounded, $b_n$ is well-defined for every $n$, and we have the equivalence

$$b_n \le k \iff a_k \ge n. \tag{$\star$}$$

(Both sides say "some term with index $\le k$ reaches $n$"; by monotonicity this reduces to checking $a_k$.)

From $(\star)$, for $k \ge 2$,

$$b_n \ge k \iff a_{k-1} < n,$$

and $b_n \ge 1$ always. Writing $b_n$ as a tail sum of indicators,

$$b_n = \sum_{k=1}^{\infty} \mathbf{1}[b_n \ge k] = 1 + \sum_{j=1}^{\infty} \mathbf{1}[a_j < n] = 1 + \#\{j \ge 1 : a_j < n\}.$$

(The count is finite because $(a_j)$ is unbounded.) Equivalently,

$$b_n - 1 = \#\{j \ge 1 : a_j < n\}, \qquad\text{i.e.}\qquad b_n = \#\{j \ge 1 : a_j < n\} + 1. \tag{1}$$

## Rewriting the $b$-sum

Sum (1) over $n = 1, \ldots, 2026$ and swap the order of summation:

$$\sum_{n=1}^{2026} b_n = 2026 + \sum_{j=1}^{\infty} \sum_{n=1}^{2026} \mathbf{1}[a_j < n] = 2026 + \sum_{j=1}^{\infty} \max(0,\, 2026 - a_j). \tag{2}$$

(The inner count is the number of $n \in \{1,\ldots,2026\}$ with $n > a_j$, which equals $2026 - a_j$ when $a_j < 2026$ and $0$ when $a_j \ge 2026$.)

## Using $a_{37} = 2026$

Because $(a_j)$ is nondecreasing:

- For $j \le 37$: $a_j \le a_{37} = 2026$, so $\max(0, 2026 - a_j) = 2026 - a_j$.
- For $j \ge 38$: $a_j \ge a_{37} = 2026$, so $\max(0, 2026 - a_j) = 0$.

Substituting into (2):

$$\sum_{n=1}^{2026} b_n = 2026 + \sum_{j=1}^{37}(2026 - a_j) + 0.$$

Therefore the full target sum is

$$S = \sum_{j=1}^{37} a_j + \sum_{n=1}^{2026} b_n = \sum_{j=1}^{37} a_j + 2026 + \sum_{j=1}^{37}(2026 - a_j) = 37 \cdot 2026 + 2026 = 38 \cdot 2026.$$

## Computation

$$38 \times 2026 = 38 \times 2000 + 38 \times 26 = 76000 + 988 = 76988.$$

## Attainability

The value is attained by, e.g., $a_1 = \cdots = a_{37} = 2026$ and $a_m = 2026 + (m - 37)$ for $m \ge 38$ (nondecreasing, unbounded, $a_{37} = 2026$). Then $b_n = 1$ for all $1 \le n \le 2026$, giving $S = 37 \cdot 2026 + 2026 \cdot 1 = 76988$.

Since the derivation shows $S = 38 \cdot 2026$ for **every** valid sequence with $a_{37} = 2026$, this is both the maximum and the only possible value.

$$S_{\max} = 38 \cdot 2026 = \boxed{76988}. \qquad \text{QED}$$
