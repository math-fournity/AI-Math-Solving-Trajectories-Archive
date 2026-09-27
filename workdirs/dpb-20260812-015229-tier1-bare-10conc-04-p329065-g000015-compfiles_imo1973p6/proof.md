# IMO 1973 Problem 6 — Solution

## Problem

Let $a_1, a_2, \cdots, a_n$ be $n$ positive numbers, and let $q$ be a given real number such that $0 < q < 1$. Find $n$ numbers $b_1, b_2, \cdots, b_n$ for which

(a) $a_k < b_k$ for $k=1,2,\cdots,n$,

(b) $q < \dfrac{b_{k+1}}{b_k} < \dfrac{1}{q}$ for $k=1,2,\cdots,n-1$,

(c) $b_1+b_2+\cdots+b_n < \dfrac{1+q}{1-q}(a_1+a_2+\cdots+a_n)$.

---

## Construction

Define the **base sequence**

$$B_k \;=\; \max_{1 \le i \le n}\; a_i \, q^{|k-i|}, \qquad k = 1, 2, \ldots, n.$$

Then set

$$\boxed{b_k \;=\; B_k + \epsilon \;=\; \max_{1 \le i \le n}\; a_i \, q^{|k-i|} \;+\; \epsilon}$$

where $\epsilon > 0$ is chosen sufficiently small (to be specified below).

---

## Verification

We first establish three properties of the base sequence $B_k$, then show that the perturbation by $\epsilon$ converts all non-strict inequalities into strict ones.

### Property 1 (Lower bound): $B_k \ge a_k$

Since $i = k$ is among the indices over which the maximum is taken,

$$B_k = \max_i a_i \, q^{|k-i|} \;\ge\; a_k \, q^{|k-k|} = a_k \, q^0 = a_k.$$

### Property 2 (Ratio bound): $q \le \dfrac{B_{k+1}}{B_k} \le \dfrac{1}{q}$

**Lower bound** $B_{k+1} \ge q\, B_k$: Let $i^*$ be an index achieving the maximum for $B_k$, so $B_k = a_{i^*}\, q^{|k - i^*|}$. Then

$$B_{k+1} \;\ge\; a_{i^*}\, q^{|(k+1) - i^*|}.$$

By the triangle inequality, $|(k+1) - i^*| \le |k - i^*| + 1$, so (since $0 < q < 1$):

$$q^{|(k+1) - i^*|} \;\ge\; q^{|k - i^*| + 1} = q \cdot q^{|k - i^*|}.$$

Therefore $B_{k+1} \ge a_{i^*} \cdot q \cdot q^{|k - i^*|} = q\, B_k$.

**Upper bound** $B_{k+1} \le B_k / q$: Let $j^*$ be an index achieving the maximum for $B_{k+1}$, so $B_{k+1} = a_{j^*}\, q^{|(k+1) - j^*|}$. Then

$$B_k \;\ge\; a_{j^*}\, q^{|k - j^*|}.$$

Again $|k - j^*| \le |(k+1) - j^*| + 1$, so $q^{|k - j^*|} \ge q \cdot q^{|(k+1) - j^*|}$, giving

$$B_k \;\ge\; a_{j^*} \cdot q \cdot q^{|(k+1) - j^*|} = q\, B_{k+1},$$

i.e., $B_{k+1} \le B_k / q$. $\quad\blacksquare$

### Property 3 (Sum bound): $\displaystyle\sum_{k=1}^n B_k < \frac{1+q}{1-q} \sum_{i=1}^n a_i$

Using $\max \le \sum$:

$$\sum_{k=1}^n B_k \;=\; \sum_{k=1}^n \max_i a_i\, q^{|k-i|} \;\le\; \sum_{k=1}^n \sum_{i=1}^n a_i\, q^{|k-i|} \;=\; \sum_{i=1}^n a_i \underbrace{\left(\sum_{k=1}^n q^{|k-i|}\right)}_{S_i}.$$

We evaluate $S_i$ in closed form. Splitting the sum at $k = i$:

$$S_i = \sum_{k=1}^{i} q^{i-k} + \sum_{k=i+1}^{n} q^{k-i} = \sum_{j=0}^{i-1} q^j + \sum_{j=1}^{n-i} q^j = \frac{1 - q^i}{1-q} + \frac{q(1 - q^{n-i})}{1-q} = \frac{1 + q - q^i - q^{n-i+1}}{1-q}.$$

Since $0 < q < 1$ and $1 \le i \le n$, both $q^i > 0$ and $q^{n-i+1} > 0$, so

$$S_i = \frac{1 + q - q^i - q^{n-i+1}}{1-q} < \frac{1+q}{1-q}.$$

Since every $a_i > 0$, we conclude

$$\sum_{k=1}^n B_k \;\le\; \sum_{i=1}^n a_i\, S_i \;<\; \sum_{i=1}^n a_i \cdot \frac{1+q}{1-q} = \frac{1+q}{1-q}\sum_{i=1}^n a_i. \quad\blacksquare$$

---

### Choosing $\epsilon$ and verifying strict inequalities

Let

$$\eta \;=\; \frac{1+q}{1-q}\sum_{i=1}^n a_i \;-\; \sum_{k=1}^n B_k \;>\; 0$$

(by Property 3, the slack is strictly positive). Choose

$$0 < \epsilon < \frac{\eta}{n}.$$

Set $b_k = B_k + \epsilon$. We verify the three conditions:

**(a) $a_k < b_k$:** By Property 1, $B_k \ge a_k$, so $b_k = B_k + \epsilon \ge a_k + \epsilon > a_k$. ✓

**(b) $q < \dfrac{b_{k+1}}{b_k} < \dfrac{1}{q}$:**

*Lower bound:* Using $B_{k+1} \ge q\, B_k$ (Property 2):

$$b_{k+1} = B_{k+1} + \epsilon \ge q\, B_k + \epsilon > q\, B_k + q\,\epsilon = q(B_k + \epsilon) = q\, b_k,$$

where the strict inequality $\epsilon > q\,\epsilon$ holds because $q < 1$.

*Upper bound:* Using $B_{k+1} \le B_k / q$ (Property 2):

$$b_{k+1} = B_{k+1} + \epsilon \le \frac{B_k}{q} + \epsilon < \frac{B_k}{q} + \frac{\epsilon}{q} = \frac{B_k + \epsilon}{q} = \frac{b_k}{q},$$

where the strict inequality $\epsilon < \epsilon / q$ holds because $q < 1$. ✓

**(c) $\displaystyle\sum b_k < \frac{1+q}{1-q}\sum a_k$:**

$$\sum_{k=1}^n b_k = \sum_{k=1}^n B_k + n\epsilon < \sum_{k=1}^n B_k + \eta = \frac{1+q}{1-q}\sum_{i=1}^n a_i,$$

where the inequality uses $\epsilon < \eta / n$, i.e., $n\epsilon < \eta$. ✓

---

## Summary

The numbers

$$b_k = \max_{1 \le i \le n} a_i\, q^{|k-i|} + \epsilon, \qquad k = 1, \ldots, n,$$

where $\epsilon > 0$ is any sufficiently small positive number (specifically, $\epsilon < \frac{1}{n}\!\left(\frac{1+q}{1-q}\sum a_i - \sum B_k\right)$), satisfy all three required conditions (a), (b), (c) with strict inequalities.

**Key ideas:**
- The base $B_k = \max_i a_i\, q^{|k-i|}$ is a **geometric envelope** of the sequence $(a_i)$: each $a_i$ "spreads" geometrically in both directions with ratio $q$, and $B_k$ takes the pointwise maximum of all these spreads.
- The ratio condition (b) follows from the triangle inequality: $|(k+1)-i| \le |k-i|+1$, which forces each geometric spread to change by a factor between $q$ and $1/q$ per step.
- The sum condition (c) follows from bounding $\max \le \sum$ and computing the geometric series $\sum_k q^{|k-i|}$, which for **finite** $n$ is strictly less than the infinite sum $\frac{1+q}{1-q}$.
- The additive constant $\epsilon$ converts the non-strict inequalities (a) and (b) into strict ones, using the slack $\eta > 0$ from the already-strict sum condition (c).

$\blacksquare$ — QED
