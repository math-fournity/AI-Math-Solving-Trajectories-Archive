# IMO 1994 Problem 6 — Solution

## Problem

Show that there exists a set $A$ of positive integers with the following property: For any infinite set $S$ of primes there exist two positive integers $m \in A$ and $n \notin A$ each of which is a product of $k$ distinct elements of $S$ for some $k \geq 2$.

**Interpretation.** There exists a single $k \geq 2$ such that both $m$ and $n$ are products of exactly $k$ distinct primes from $S$, with $m \in A$ and $n \notin A$. (If each were allowed its own $k$, the problem would be trivial: color by parity of the number of prime factors.)

## Reformulation

We need a 2-coloring (membership in $A$) of all squarefree integers with $\geq 2$ prime factors such that:

> For every infinite set $S$ of primes, there exists $k \geq 2$ such that the products of exactly $k$ distinct primes from $S$ are **not all the same color**.

Equivalently, no infinite set of primes is "monochromatic at every level $k \geq 2$."

## Construction

Enumerate the primes: $p_1 = 2,\; p_2 = 3,\; p_3 = 5,\; p_4 = 7,\; \ldots$

For a squarefree positive integer $n$ with $k \geq 2$ prime factors, write
$$n = p_{i_1}\, p_{i_2} \cdots p_{i_k}, \qquad i_1 < i_2 < \cdots < i_k,$$
so $p_{i_1}$ is the smallest prime factor of $n$ and $i_1$ is its index in the enumeration.

**Define:**
$$\boxed{n \in A \iff \text{bit } (k-2) \text{ of } i_1 \text{ is } 0, \text{ i.e., } \left\lfloor \frac{i_1}{2^{k-2}} \right\rfloor \equiv 0 \pmod{2}.}$$

For all other positive integers (non-squarefree, or with fewer than 2 prime factors), assign them to $A$ or not arbitrarily — this does not affect the argument.

**In words:** the membership of $n$ in $A$ is determined by a single bit of the index of $n$'s smallest prime factor. *Which* bit is used depends on $k = \omega(n)$: level $k$ uses bit $k-2$.

## Proof

**Claim.** For any infinite set $S$ of primes, there exists $k \geq 2$ such that among the products of $k$ distinct primes from $S$, both colors appear.

**Proof.** Let $S$ be an infinite set of primes. Let $I = \{i_1 < i_2 < i_3 < \cdots\}$ be the corresponding set of indices (so $S = \{p_{i_1}, p_{i_2}, p_{i_3}, \ldots\}$). Since $S$ is infinite, $I$ is an infinite set of distinct positive integers.

**Key observation.** There exists a bit position $j \geq 0$ such that not all elements of $I$ have the same value in bit $j$.

*Proof of observation.* Suppose for contradiction that for every $j \geq 0$, all elements of $I$ have the same bit-$j$ value, say $b_j \in \{0,1\}$. Then every element $i \in I$ satisfies $i = \sum_{j \geq 0} b_j \, 2^j$ (a finite sum, since $i$ is a positive integer). This sum is the same for all $i \in I$, so $I$ has at most one element — contradicting $I$ being infinite. $\square$

**Applying the observation.** Let $j \geq 0$ be a bit position that is not constant on $I$. Set $k = j + 2 \geq 2$. At this level, the color of a product $n = p_{a_1} p_{a_2} \cdots p_{a_k}$ (with $a_1 < \cdots < a_k$, all $a_\ell \in I$) depends on bit $j = k-2$ of $a_1$ (the index of the smallest prime factor).

Since bit $j$ is not constant on $I$, there exist indices $\alpha, \beta \in I$ with different bit-$j$ values:
$$\text{bit}_j(\alpha) = 0, \qquad \text{bit}_j(\beta) = 1.$$

Since $I$ is infinite, there are at least $k - 1$ elements of $I$ larger than $\alpha$, so we can form a $k$-element subset of $I$ with $\alpha$ as its smallest element. Similarly for $\beta$. This gives two products:

- $m = p_\alpha \cdot p_{c_2} \cdots p_{c_k}$ with $\alpha < c_2 < \cdots < c_k$, all in $I$. Since $\text{bit}_j(\alpha) = 0$, we have $m \in A$.
- $n = p_\beta \cdot p_{d_2} \cdots p_{d_k}$ with $\beta < d_2 < \cdots < d_k$, all in $I$. Since $\text{bit}_j(\beta) = 1$, we have $n \notin A$.

Both $m$ and $n$ are products of $k = j+2 \geq 2$ distinct primes from $S$, with $m \in A$ and $n \notin A$. $\blacksquare$

## Intuition

The construction exploits a fundamental fact: **an infinite set of distinct positive integers cannot agree on every binary digit** (otherwise all its elements would be equal). By assigning a different bit position to each level $k$, we guarantee that whatever bit the infinite set $S$ "disagrees on," the corresponding level $k$ will detect that disagreement and produce both colors.

The infinite Ramsey theorem tells us that for each *fixed* $k$, some infinite $S$ is monochromatic at level $k$. But our construction ensures that no single $S$ can be monochromatic at *all* levels simultaneously — being monochromatic at level $k$ forces agreement on bit $k-2$, and agreeing on all bits is impossible for an infinite set.

## Verification

The construction was verified computationally on diverse infinite sets (truncated to 20 elements each): all primes, odd-indexed primes, even-indexed primes, indices in various arithmetic progressions ($2 \bmod 4$, $0 \bmod 4$, $0 \bmod 8$, $4 \bmod 8$), powers of 2, Mersenne-type indices, and random indices. In every case, a level $k$ with both colors present was found, matching the theoretical prediction (the first non-constant bit position $j$ gives $k = j+2$).
