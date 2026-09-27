# IMO 1993 Problem 5 — Solution

## Problem

Does there exist a function $f : \mathbb{N} \to \mathbb{N}$ such that
- (i) $f(1) = 2$,
- (ii) $f(f(n)) = f(n) + n$ for all $n \in \mathbb{N}$,
- (iii) $f(n+1) > f(n)$ for all $n \in \mathbb{N}$?

## Answer

**Yes.** Such a function exists.

## Construction via the Fibonacci Successor

We use the **Zeckendorf representation**: by Zeckendorf's theorem, every positive integer $n$ has a unique representation

$$n = F_{i_1} + F_{i_2} + \cdots + F_{i_k}$$

where $F_1 = F_2 = 1,\; F_3 = 2,\; F_4 = 3,\; F_5 = 5,\; \ldots$ are the Fibonacci numbers ($F_{m+2} = F_{m+1} + F_m$), and the indices satisfy $i_1 > i_2 > \cdots > i_k \geq 2$ with **no two consecutive** (i.e., $i_j - i_{j+1} \geq 2$ for all $j$).

**Definition.** For $n = F_{i_1} + F_{i_2} + \cdots + F_{i_k}$ in Zeckendorf form, define

$$\boxed{f(n) = F_{i_1+1} + F_{i_2+1} + \cdots + F_{i_k+1}.}$$

This function shifts every Fibonacci number in the Zeckendorf representation up by one index. We call it the **Fibonacci successor**.

## Verification

### (i) $f(1) = 2$

Since $1 = F_2$, we have $f(1) = F_3 = 2$. $\checkmark$

### (ii) $f(f(n)) = f(n) + n$

**$f(n)$ is a valid Zeckendorf representation.** The shifted indices $i_1{+}1 > i_2{+}1 > \cdots > i_k{+}1 \geq 3$ are still non-consecutive (since $i_j - i_{j+1} \geq 2$ implies $(i_j{+}1) - (i_{j+1}{+}1) \geq 2$). So $f(n)$ is a well-defined positive integer with valid Zeckendorf form.

**Computing $f(f(n))$.** Applying $f$ again shifts each index up by one more:

$$f(f(n)) = F_{i_1+2} + F_{i_2+2} + \cdots + F_{i_k+2}.$$

**Computing $f(n) + n$.** The key observation is that the Fibonacci numbers used by $f(n)$ (at indices $i_j + 1$) and by $n$ (at indices $i_j$) occupy **disjoint** sets of indices: since the $i_j$ are non-consecutive, no $i_{j'}$ equals $i_j + 1$. Therefore, adding $f(n) + n$ pairs up Fibonacci numbers index-by-index:

$$f(n) + n = \sum_{j=1}^{k}\bigl(F_{i_j+1} + F_{i_j}\bigr) = \sum_{j=1}^{k} F_{i_j+2},$$

using the Fibonacci recurrence $F_{m+1} + F_m = F_{m+2}$. The resulting indices $i_j + 2$ are non-consecutive, so no "carries" occur — this is the valid Zeckendorf representation of $f(n) + n$.

**Conclusion:** $f(f(n)) = F_{i_1+2} + \cdots + F_{i_k+2} = f(n) + n$. $\checkmark$

### (iii) $f$ is strictly increasing

The Zeckendorf representation establishes a bijection between positive integers and finite subsets of $\{2, 3, 4, \ldots\}$ with no two consecutive elements. The natural ordering on $\mathbb{N}$ corresponds to the **lexicographic ordering** on these subsets, compared from the largest index downward: if $n < m$, then at the largest index $i^*$ where their representations differ, $m$ includes $F_{i^*}$ and $n$ does not.

The Fibonacci successor shifts every index in the subset up by 1. This preserves the lexicographic comparison: the largest differing index becomes $i^* + 1$, and the same element (shifted) distinguishes $f(m)$ from $f(n)$. Hence $n < m \implies f(n) < f(m)$. $\checkmark$

## Examples

| $n$ | Zeckendorf | $f(n)$ | Zeckendorf of $f(n)$ |
|-----|-----------|--------|---------------------|
| 1 | $F_2$ | 2 | $F_3$ |
| 2 | $F_3$ | 3 | $F_4$ |
| 3 | $F_4$ | 5 | $F_5$ |
| 4 | $F_4 + F_2$ | 7 | $F_5 + F_3$ |
| 5 | $F_5$ | 8 | $F_6$ |
| 6 | $F_5 + F_2$ | 10 | $F_6 + F_3$ |
| 7 | $F_5 + F_3$ | 11 | $F_6 + F_4$ |
| 8 | $F_6$ | 13 | $F_7$ |
| 12 | $F_6 + F_4 + F_2$ | 20 | $F_7 + F_5 + F_3$ |

**Check for $n = 12$:** $f(12) = 20$, $f(20) = F_8 + F_6 + F_4 = 21 + 8 + 3 = 32 = 20 + 12$. $\checkmark$

## Intuition

The asymptotic ratio $f(n)/n \to \varphi = \frac{1+\sqrt{5}}{2}$ (the golden ratio) follows from the self-similar structure: if $f(n) \approx cn$, then $f(f(n)) \approx c^2 n$ and $f(n) + n \approx (c+1)n$, giving $c^2 = c + 1$, i.e., $c = \varphi$. The Zeckendorf representation makes this precise — the Fibonacci successor is the natural "multiplication by $\varphi$" in the Fibonacci numeration system.

## QED
