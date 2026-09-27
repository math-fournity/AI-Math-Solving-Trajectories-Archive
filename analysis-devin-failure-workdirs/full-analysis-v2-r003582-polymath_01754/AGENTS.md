# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search. Do NOT read any files.
- All information you need is already in your prompt above. Do NOT read any files.
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
  <problem_id>polymath_01754</problem_id>
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

For every positive integer $ n$ determine the highest value $ C(n)$, such that for every $ n$-tuple $ (a_1,a_2,\ldots,a_n)$ of  pairwise distinct integers

$ (n \plus{} 1)\sum_{j \equal{} 1}^n a_j^2 \minus{} \left(\sum_{j \equal{} 1}^n a_j\right)^2\geq C(n)$

## Standard Solution

To determine the highest value \( C(n) \) such that for every \( n \)-tuple \( (a_1, a_2, \ldots, a_n) \) of pairwise distinct integers, the inequality 

\[
(n + 1) \sum_{j = 1}^n a_j^2 - \left( \sum_{j = 1}^n a_j \right)^2 \geq C(n)
\]

holds, we need to analyze the expression and find its minimum value.

1. **Rewrite the expression:**
   \[
   (n + 1) \sum_{j = 1}^n a_j^2 - \left( \sum_{j = 1}^n a_j \right)^2
   \]

2. **Introduce notation for sums:**
   Let \( S = \sum_{j = 1}^n a_j \) and \( S_2 = \sum_{j = 1}^n a_j^2 \). The expression becomes:
   \[
   (n + 1) S_2 - S^2
   \]

3. **Use the identity for the sum of squares:**
   For pairwise distinct integers \( a_1, a_2, \ldots, a_n \), we can use the identity:
   \[
   S_2 = \sum_{j = 1}^n a_j^2
   \]
   and
   \[
   S = \sum_{j = 1}^n a_j
   \]

4. **Consider the case when \( a_i \) are consecutive integers:**
   The sum of squares \( S_2 \) and the sum \( S \) are minimized when the \( a_i \) are consecutive integers centered around zero.

5. **Case 1: \( n = 2m \) (even):**
   Let \( a_i = -m, -m+1, \ldots, -1, 0, 1, \ldots, m-1 \). Then:
   \[
   S = \sum_{j = -m}^{m-1} j = 0
   \]
   and
   \[
   S_2 = \sum_{j = -m}^{m-1} j^2 = \sum_{j = 1}^{m-1} j^2 + \sum_{j = 1}^{m} j^2 = 2 \sum_{j = 1}^{m-1} j^2 + m^2
   \]
   Using the formula for the sum of squares:
   \[
   \sum_{j = 1}^{k} j^2 = \frac{k(k+1)(2k+1)}{6}
   \]
   we get:
   \[
   S_2 = 2 \cdot \frac{(m-1)m(2m-1)}{6} + m^2 = \frac{(m-1)m(2m-1)}{3} + m^2
   \]

6. **Case 2: \( n = 2m + 1 \) (odd):**
   Let \( a_i = -m, -m+1, \ldots, 0, \ldots, m \). Then:
   \[
   S = \sum_{j = -m}^{m} j = 0
   \]
   and
   \[
   S_2 = \sum_{j = -m}^{m} j^2 = 2 \sum_{j = 1}^{m} j^2 + 0^2 = 2 \cdot \frac{m(m+1)(2m+1)}{6} = \frac{m(m+1)(2m+1)}{3}
   \]

7. **Calculate the minimum value of the expression:**
   For \( n = 2m \):
   \[
   (n + 1) S_2 - S^2 = (2m + 1) \left( \frac{(m-1)m(2m-1)}{3} + m^2 \right)
   \]
   For \( n = 2m + 1 \):
   \[
   (n + 1) S_2 - S^2 = (2m + 2) \left( \frac{m(m+1)(2m+1)}{3} \right)
   \]

8. **Simplify the expressions:**
   For \( n = 2m \):
   \[
   (2m + 1) \left( \frac{(m-1)m(2m-1)}{3} + m^2 \right) = (2m + 1) \left( \frac{2m^3 - m^2 - m + m^2}{3} \right) = (2m + 1) \left( \frac{2m^3 - m}{3} \right)
   \]
   For \( n = 2m + 1 \):
   \[
   (2m + 2) \left( \frac{m(m+1)(2m+1)}{3} \right) = \frac{(2m + 2) m (m+1) (2m+1)}{3}
   \]

9. **Conclusion:**
   The highest value \( C(n) \) is determined by the minimum value of the expression for the given \( n \).

The final answer is \( C(n) = \boxed{n(n-1)} \)

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We need to find the highest value $C(n)$ such that for every $n$-tuple $(a_1, a_2, \ldots, a_n)$ of pairwise distinct integers:
$$(n+1)\sum_{j=1}^n a_j^2 - \left(\sum_{j=1}^n a_j\right)^2 \geq C(n)$$

First, let me understand the expression. The left-hand side is:
$$(n+1)\sum a_j^2 - \left(\sum a_j\right)^2$$

Let me denote $S = \sum a_j$ and $Q = \sum a_j^2$.

So the expression is $(n+1)Q - S^2$.

Let me think about this. We can write:
$$(n+1)Q - S^2 = nQ + Q - S^2 = nQ - (S^2 - Q)$$

Note that $S^2 - Q = \sum_{i \neq j} a_i a_j = 2\sum_{i < j} a_i a_j$.

So $(n+1)Q - S^2 = nQ - 2\sum_{i<j} a_i a_j$.

Hmm, let me think differently. Actually, there's a nice identity:
$$(n+1)\sum a_j^2 - \left(\sum a_j\right)^2 = \sum_{i<j} (a_i - a_j)^2 + \sum a_j^2$$

Wait, let me verify. We know that $\sum_{i<j}(a_i - a_j)^2 = n\sum a_j^2 - \left(\sum a_j\right)^2$.

This is a well-known identity: $n\sum a_i^2 - (\sum a_i)^2 = \sum_{i<j}(a_i-a_j)^2$.

So $(n+1)\sum a_j^2 - (\sum a_j)^2 = \sum_{i<j}(a_i-a_j)^2 + \sum a_j^2$.

That's a nice decomposition but maybe not directly useful.

Since the $a_j$ are pairwise distinct integers, the differences $|a_i - a_j|$ are at least 1 for $i \neq j$.

The expression $n\sum a_j^2 - (\sum a_j)^2 = \sum_{i<j}(a_i-a_j)^2$ is translation-invariant (shifting all $a_j$ by the same constant doesn't change it). But the full expression $(n+1)\sum a_j^2 - (\sum a_j)^2 = \sum_{i<j}(a_i-a_j)^2 + \sum a_j^2$ is NOT translation invariant because of the $\sum a_j^2$ term.

So to minimize $(n+1)Q - S^2$, we want to minimize $\sum_{i<j}(a_i-a_j)^2 + \sum a_j^2$.

The first part $\sum_{i<j}(a_i-a_j)^2$ is minimized when the $a_j$ are as close together as possible (consecutive integers), and the second part $\sum a_j^2$ is minimized when the values are close to 0.

Let me think about this more carefully. We want to minimize:
$$f(a_1, \ldots, a_n) = (n+1)\sum a_j^2 - \left(\sum a_j\right)^2$$

over all $n$-tuples of pairwise distinct integers.

Let me use the substitution. Let $\bar{a} = \frac{1}{n}\sum a_j$ be the mean. Then:
$$\sum a_j^2 = \sum (a_j - \bar{a})^2 + n\bar{a}^2$$
$$\left(\sum a_j\right)^2 = n^2 \bar{a}^2$$

So:
$$(n+1)\sum a_j^2 - \left(\sum a_j\right)^2 = (n+1)\left(\sum (a_j - \bar{a})^2 + n\bar{a}^2\right) - n^2\bar{a}^2$$
$$= (n+1)\sum (a_j - \bar{a})^2 + n(n+1)\bar{a}^2 - n^2\bar{a}^2$$
$$= (n+1)\sum (a_j - \bar{a})^2 + n\bar{a}^2$$

So we need to minimize:
$$(n+1)\sum (a_j - \bar{a})^2 + n\bar{a}^2$$

The first term depends on the spread of the values, the second on the mean.

Since the $a_j$ are distinct integers, $\sum (a_j - \bar{a})^2$ is minimized when the $a_j$ are consecutive integers. For consecutive integers $a_j = m, m+1, \ldots, m+n-1$, the mean is $\bar{a} = m + \frac{n-1}{2}$, and:
$$\sum (a_j - \bar{a})^2 = \sum_{k=0}^{n-1}\left(k - \frac{n-1}{2}\right)^2 = \frac{n(n^2-1)}{12}$$

This is the minimum variance for $n$ distinct integers.

But we also need to minimize $n\bar{a}^2$, which means we want $\bar{a}$ close to 0.

For consecutive integers $m, m+1, \ldots, m+n-1$, the mean is $m + \frac{n-1}{2}$.

If $n$ is odd, say $n = 2k+1$, then $\frac{n-1}{2} = k$ is an integer, and we can choose $m = -k$ so that $\bar{a} = 0$. The values are $-k, -k+1, \ldots, k$, i.e., $-k, \ldots, 0, \ldots, k$.

If $n$ is even, say $n = 2k$, then $\frac{n-1}{2} = k - \frac{1}{2}$, and the mean is $m + k - \frac{1}{2}$. The closest we can get to 0 is $\bar{a} = \pm\frac{1}{2}$, by choosing $m = -k$ or $m = -k+1$.

Wait, but we should also consider whether non-consecutive integers could give a smaller total. Let me think again.

We want to minimize $(n+1)\sum (a_j - \bar{a})^2 + n\bar{a}^2$.

The key insight: for distinct integers, $\sum (a_j - \bar{a})^2$ is minimized by consecutive integers. But there might be a trade-off where slightly increasing the variance allows a much smaller $\bar{a}^2$.

Actually, let me reconsider. The question is whether we can do better than consecutive integers by choosing a different set of distinct integers that has slightly higher variance but much smaller mean.

Let me think about this more carefully. For distinct integers, the minimum of $\sum (a_j - \bar{a})^2$ is $\frac{n(n^2-1)}{12}$, achieved by consecutive integers. But we're minimizing $(n+1) \cdot \text{variance term} + n \cdot \text{mean}^2$.

If we use consecutive integers centered at 0 (for odd $n$), we get:
- variance term = $\frac{n(n^2-1)}{12}$
- mean = 0
- total = $(n+1) \cdot \frac{n(n^2-1)}{12}$

For even $n$, consecutive integers give mean $= \pm 1/2$:
- variance term = $\frac{n(n^2-1)}{12}$
- mean$^2$ = $1/4$
- total = $(n+1) \cdot \frac{n(n^2-1)}{12} + \frac{n}{4}$

But could we do better with non-consecutive integers? For example, for even $n$, could we choose integers that are not consecutive but have mean exactly 0?

For $n = 2$: consecutive integers $\{m, m+1\}$, mean $= m + 1/2$. The minimum variance for 2 distinct integers is $(a_1 - a_2)^2/2$... wait, let me recompute.

Actually, $\sum (a_j - \bar{a})^2$ for two values $a, b$ is $(a - \bar{a})^2 + (b - \bar{a})^2$ where $\bar{a} = (a+b)/2$. This equals $2 \cdot ((a-b)/2)^2 = (a-b)^2/2$.

For consecutive integers, $|a-b| = 1$, so variance term $= 1/2$.

The expression becomes $(n+1) \cdot 1/2 + n \cdot (1/2)^2 = 3 \cdot 1/2 + 2 \cdot 1/4 = 3/2 + 1/2 = 2$.

But what if we choose $\{-1, 1\}$? Then mean $= 0$, variance term $= (-1)^2 + 1^2 = 2$. Total $= 3 \cdot 2 + 0 = 6$. That's worse.

What about $\{0, 1\}$? Mean $= 1/2$, variance term $= 1/4 + 1/4 = 1/2$. Total $= 3/2 + 2/4 = 3/2 + 1/2 = 2$. Same as $\{-1, 0\}$ (mean $= -1/2$).

What about $\{0, -1\}$? Same by symmetry.

So for $n=2$, the minimum is 2, achieved by consecutive integers.

Let me verify directly: for $n=2$, $a_1, a_2$ distinct integers.
$3(a_1^2 + a_2^2) - (a_1 + a_2)^2 = 3a_1^2 + 3a_2^2 - a_1^2 - 2a_1 a_2 - a_2^2 = 2a_1^2 + 2a_2^2 - 2a_1 a_2 = 2(a_1^2 + a_2^2 - a_1 a_2)$.

$a_1^2 + a_2^2 - a_1 a_2 = (a_1 - a_2)^2/2 + a_1 a_2/2$... hmm, let me just compute directly.

$a_1^2 + a_2^2 - a_1 a_2$. For $a_1 = 0, a_2 = 1$: $0 + 1 - 0 = 1$. So $2 \cdot 1 = 2$.
For $a_1 = -1, a_2 = 0$: $1 + 0 - 0 = 1$. So $2$.
For $a_1 = -1, a_2 = 1$: $1 + 1 + 1 = 3$. So $6$.

So minimum is 2 for $n=2$. Good.

Now let me think about whether non-consecutive integers could ever be better.

Claim: The minimum is always achieved by consecutive integers centered as close to 0 as possible.

Let me think about why. We're minimizing $(n+1)V + n\bar{a}^2$ where $V = \sum(a_j - \bar{a})^2$.

For distinct integers, $V \geq \frac{n(n^2-1)}{12}$ with equality for consecutive integers.

Now, if we use non-consecutive integers, $V$ increases. The question is whether the decrease in $n\bar{a}^2$ can compensate.

For odd $n$: consecutive integers can be centered at 0, so $\bar{a} = 0$ is achievable. Any other configuration has $V > \frac{n(n^2-1)}{12}$ and $\bar{a}^2 \geq 0$, so it's worse. Thus for odd $n$, the minimum is $(n+1) \cdot \frac{n(n^2-1)}{12}$.

For even $n$: consecutive integers give $\bar{a} = \pm 1/2$, so $\bar{a}^2 = 1/4$. The total is $(n+1) \cdot \frac{n(n^2-1)}{12} + n/4$.

Could we do better with non-consecutive integers that have $\bar{a} = 0$? We'd need $V > \frac{n(n^2-1)}{12}$ but $\bar{a} = 0$. The increase in $(n+1)V$ would need to be less than $n/4$.

For $n = 2$: We need two distinct integers with mean 0, i.e., $\{-k, k\}$ for some $k \geq 1$. Then $V = 2k^2$. The total is $3 \cdot 2k^2 = 6k^2 \geq 6 > 2$. So no improvement.

For $n = 4$: Consecutive integers, e.g., $\{-2, -1, 0, 1\}$ or $\{-1, 0, 1, 2\}$. Mean $= \pm 1/2$. $V = \frac{4 \cdot 15}{12} = 5$. Total $= 5 \cdot 5 + 4/4 = 25 + 1 = 26$.

Can we do better with non-consecutive? Try $\{-2, -1, 1, 2\}$: mean $= 0$, $V = 4 + 1 + 1 + 4 = 10$. Total $= 5 \cdot 10 + 0 = 50 > 26$.

Try $\{-1, 0, 1, 2\}$: mean $= 1/2$, $V = 1/4 + 1/4 + 1/4 + 9/4 = 12/4 = 3$... wait, that doesn't seem right.

Let me recompute. $\{-1, 0, 1, 2\}$, mean $= 1/2$.
$V = (-1-1/2)^2 + (0-1/2)^2 + (1-1/2)^2 + (2-1/2)^2 = 9/4 + 1/4 + 1/4 + 9/4 = 20/4 = 5$. Yes, $V = 5$.

Total $= 5 \cdot 5 + 4 \cdot 1/4 = 25 + 1 = 26$.

What about $\{-2, -1, 0, 1\}$? Mean $= -1/2$. Same by symmetry, $V = 5$, total $= 26$.

What about trying to get mean 0 with minimal variance increase? E.g., $\{-2, -1, 0, 3\}$: mean $= 0$, $V = 4 + 1 + 0 + 9 = 14$. Total $= 5 \cdot 14 = 70 > 26$.

Or $\{-1, 0, 0, 1\}$ — not distinct.

It seems like for even $n$, consecutive integers are optimal. Let me try to prove this.

Actually, let me think about this more carefully. The question is: for even $n$, is it ever beneficial to use non-consecutive integers to get $\bar{a} = 0$?

The minimum variance for $n$ distinct integers with mean exactly 0: this is a separate optimization problem. For even $n = 2k$, the optimal set with mean 0 would be $\{-k, -k+1, \ldots, -1, 1, \ldots, k\}$ (excluding 0, symmetric around 0). Wait, that's $2k = n$ integers. Let me compute $V$ for this set.

Actually, for $n = 2k$, the set $\{-k, \ldots, -1, 1, \ldots, k\}$ has mean 0 and:
$V = 2\sum_{j=1}^{k} j^2 = 2 \cdot \frac{k(k+1)(2k+1)}{6} = \frac{k(k+1)(2k+1)}{3}$.

For consecutive integers, $V = \frac{n(n^2-1)}{12} = \frac{2k(4k^2-1)}{12} = \frac{k(4k^2-1)}{6}$.

The total for consecutive: $(n+1) \cdot \frac{k(4k^2-1)}{6} + \frac{n}{4} = (2k+1) \cdot \frac{k(4k^2-1)}{6} + \frac{k}{2}$.

The total for symmetric: $(n+1) \cdot \frac{k(k+1)(2k+1)}{3} = (2k+1) \cdot \frac{k(k+1)(2k+1)}{3}$.

Let's compare for $k=1$ ($n=2$): 
- Consecutive: $3 \cdot \frac{1 \cdot 3}{6} + \frac{1}{2} = 3/2 + 1/2 = 2$.
- Symmetric: $3 \cdot \frac{1 \cdot 2 \cdot 3}{3} = 6$.

For $k=2$ ($n=4$):
- Consecutive: $5 \cdot \frac{2 \cdot 15}{6} + 1 = 5 \cdot 5 + 1 = 26$.
- Symmetric: $5 \cdot \frac{2 \cdot 3 \cdot 5}{3} = 5 \cdot 10 = 50$.

So consecutive is much better. The variance increase from using the symmetric set is too large.

But could there be some other non-consecutive set that does better? Let me think about this more generally.

We want to minimize $(n+1)V + n\bar{a}^2$ where $V = \sum(a_j - \bar{a})^2$ and the $a_j$ are distinct integers.

Let me think of it as: we're choosing $n$ distinct integers to minimize $(n+1)\sum a_j^2 - (\sum a_j)^2$.

Let me think about this differently. Consider the $a_j$ as a set of $n$ distinct integers. We can write the objective as:

$(n+1)\sum a_j^2 - (\sum a_j)^2$

Let's think about what happens when we shift the set. If we replace each $a_j$ by $a_j + t$, then:
- $\sum (a_j+t)^2 = \sum a_j^2 + 2t\sum a_j + nt^2$
- $(\sum(a_j+t))^2 = (\sum a_j + nt)^2 = (\sum a_j)^2 + 2nt\sum a_j + n^2t^2$

So the objective becomes:
$(n+1)(\sum a_j^2 + 2t\sum a_j + nt^2) - (\sum a_j)^2 - 2nt\sum a_j - n^2t^2$
$= (n+1)\sum a_j^2 - (\sum a_j)^2 + 2t(n+1)\sum a_j - 2nt\sum a_j + (n+1)nt^2 - n^2t^2$
$= (n+1)\sum a_j^2 - (\sum a_j)^2 + 2t\sum a_j + nt^2$

So shifting by $t$ changes the objective by $2t\sum a_j + nt^2$.

For a fixed set of differences (i.e., fixed relative positions), the optimal shift minimizes $2t\sum a_j + nt^2$, which gives $t = -\frac{\sum a_j}{n} = -\bar{a}$. But $t$ must be an integer (to keep the $a_j$ as integers). So the optimal shift makes the mean as close to 0 as possible.

This confirms that for any set of distinct integers with fixed relative positions, the optimal translation centers the mean as close to 0 as possible.

Now, the question reduces to: what relative positions (i.e., what set of differences) minimize the objective after optimal centering?

For a set of $n$ distinct integers, after sorting them as $b_1 < b_2 < \ldots < b_n$, the differences $d_i = b_{i+1} - b_i \geq 1$ are positive integers. The "shape" is determined by the differences.

The variance $V = \sum(b_j - \bar{b})^2$ depends only on the shape (the differences), not on the absolute position. And after optimal centering, $\bar{a}^2$ is minimized.

For consecutive integers ($d_i = 1$ for all $i$), $V$ is minimized. Any other shape has larger $V$. Since $\bar{a}^2 \geq 0$ always, and for consecutive integers we can achieve $\bar{a}^2 = 0$ (odd $n$) or $\bar{a}^2 = 1/4$ (even $n$), we need to check if the increase in $V$ from a non-consecutive shape can be offset by a decrease in $\bar{a}^2$.

For odd $n$: consecutive integers achieve $\bar{a} = 0$, so $\bar{a}^2 = 0$ is already minimal. Any other shape has larger $V$ and $\bar{a}^2 \geq 0$, so it's worse. Done.

For even $n$: consecutive integers achieve $\bar{a}^2 = 1/4$. We need to check if any non-consecutive shape with $\bar{a} = 0$ (or $\bar{a}^2 < 1/4$, but since $\bar{a}$ is a half-integer for even $n$ consecutive... wait, actually $\bar{a}$ for even $n$ distinct integers is always a half-integer if the integers are consecutive, but for non-consecutive it could be an integer).

Hmm wait. For even $n$, if we have $n$ distinct integers, the mean $\bar{a} = \frac{\sum a_j}{n}$. For $n$ even, $\sum a_j$ can be any integer, so $\bar{a}$ can be any value of the form $k/n$ for integer $k$. In particular, $\bar{a}$ can be 0 (if $\sum a_j = 0$) or $1/n, 2/n$, etc.

For consecutive integers with even $n$, $\sum a_j = n \cdot m + \frac{n(n-1)}{2}$, and $\bar{a} = m + \frac{n-1}{2}$. Since $n$ is even, $\frac{n-1}{2}$ is a half-integer, so $\bar{a}$ is a half-integer. The closest to 0 is $\pm 1/2$.

But for non-consecutive integers, we could potentially have $\bar{a} = 0$ exactly. The question is whether the increase in $V$ is worth it.

Let me think about this more carefully for even $n$.

For even $n = 2k$, consecutive integers give $V = \frac{n(n^2-1)}{12}$ and $\bar{a}^2 = 1/4$. Total $= (n+1) \cdot \frac{n(n^2-1)}{12} + \frac{n}{4}$.

For a non-consecutive set with $\bar{a} = 0$, we need $V \geq$ some minimum. What's the minimum $V$ for $n = 2k$ distinct integers with mean 0?

The minimum variance set of $n$ distinct integers with mean 0: we want $n$ distinct integers summing to 0 with minimum $\sum a_j^2$.

For $n = 2k$, the optimal set is $\{-k, -k+1, \ldots, -1, 1, \ldots, k\}$ (i.e., $\{-k, \ldots, -1, 1, \ldots, k\}$, excluding 0). Wait, but we could also include 0 and exclude something else.

Actually, to minimize $\sum a_j^2$ subject to $n = 2k$ distinct integers summing to 0, we want the integers as close to 0 as possible. The set $\{-k, -k+1, \ldots, -1, 1, \ldots, k\}$ has $2k$ elements, sums to 0, and $\sum a_j^2 = 2\sum_{j=1}^k j^2 = \frac{k(k+1)(2k+1)}{3}$.

But could we do better? What about $\{-(k-1), \ldots, -1, 0, 1, \ldots, k\}$? This has $2k$ elements (from $-(k-1)$ to $k$), sums to $k$, not 0. So that doesn't work.

What about $\{-k, -(k-1), \ldots, -1, 0, 1, \ldots, (k-1)\}$? This has $2k$ elements (from $-k$ to $k-1$), sums to $-k$, not 0.

So to get mean 0 with $2k$ distinct integers, we need to exclude 0 from a symmetric set, giving $\{-k, \ldots, -1, 1, \ldots, k\}$.

Actually wait, we could also use non-symmetric sets. E.g., for $n=4$: $\{-3, -1, 1, 3\}$ sums to 0, $\sum a_j^2 = 9+1+1+9 = 20$. Or $\{-2, -1, 1, 2\}$ sums to 0, $\sum a_j^2 = 4+1+1+4 = 10$. Or $\{-2, -1, 0, 3\}$ sums to 0, $\sum a_j^2 = 4+1+0+9 = 14$. So $\{-2,-1,1,2\}$ is best among mean-0 sets with $n=4$.

For the mean-0 set, $V = \sum a_j^2$ (since mean is 0). So $V = 10$ for $n=4$.

Compare: consecutive gives $V = 5$, total $= 5 \cdot 5 + 1 = 26$. Mean-0 set gives $V = 10$, total $= 5 \cdot 10 + 0 = 50$. Much worse.

The reason is clear: excluding 0 from the symmetric set increases the variance significantly.

Let me try to prove that for even $n$, consecutive integers are always optimal.

For even $n = 2k$, the objective with consecutive integers (optimally centered) is:
$$T_{\text{cons}} = (n+1) \cdot \frac{n(n^2-1)}{12} + \frac{n}{4}$$

For any other set of distinct integers, either:
1. The set is consecutive but not optimally centered: worse by the centering argument.
2. The set is not consecutive: $V > \frac{n(n^2-1)}{12}$, and even with $\bar{a} = 0$, the total is $(n+1)V > (n+1) \cdot \frac{n(n^2-1)}{12}$. We need $(n+1)V \geq (n+1) \cdot \frac{n(n^2-1)}{12} + \frac{n}{4}$, i.e., $V \geq \frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}$.

So the question is: for even $n$, what is the minimum $V$ for a non-consecutive set of $n$ distinct integers (with any mean)?

If the set is not consecutive, then at least one gap is $\geq 2$. The minimum $V$ for a non-consecutive set is achieved by taking consecutive integers and increasing one gap by 1 (i.e., shifting one "half" of the set by 1).

Let me think about this. If we have consecutive integers $0, 1, 2, \ldots, n-1$ and we increase one gap, say between position $i$ and $i+1$, making it 2 instead of 1, we get $0, 1, \ldots, i, i+2, i+3, \ldots, n$. The variance of this set...

Actually, this is getting complicated. Let me think about it differently.

The key claim is: for even $n$, the minimum of $(n+1)V + n\bar{a}^2$ over all sets of $n$ distinct integers is achieved by consecutive integers centered as close to 0 as possible.

Let me try to prove this by showing that any non-consecutive set does worse.

Let the sorted distinct integers be $b_1 < b_2 < \ldots < b_n$. Let $d_i = b_{i+1} - b_i \geq 1$.

The variance $V = \sum(b_j - \bar{b})^2$ can be expressed in terms of the gaps. Actually, let me use the identity:

$V = \sum b_j^2 - n\bar{b}^2 = \sum b_j^2 - \frac{(\sum b_j)^2}{n}$

And the objective is $(n+1)V + n\bar{b}^2 = (n+1)\sum b_j^2 - (n+1)\frac{(\sum b_j)^2}{n} + n\bar{b}^2 = (n+1)\sum b_j^2 - \frac{(n+1)}{n}(\sum b_j)^2 + \frac{(\sum b_j)^2}{n} = (n+1)\sum b_j^2 - (\sum b_j)^2$.

OK that's just the original expression, as expected.

Let me think about the problem differently. Let me consider the objective as a function of the sorted values.

Actually, let me try a different approach. Let me use the fact that for distinct integers, we can write $b_j = c + e_j$ where $c$ is some integer and $e_j$ are distinct integers. The objective is translation-sensitive (as we computed), so we need to optimize over both the "shape" and the "position".

Let me fix the shape: let the sorted values be $b_j = s + r_j$ where $r_1 < r_2 < \ldots < r_n$ are fixed distinct non-negative integers with $r_1 = 0$ (we can normalize), and $s$ is an integer shift.

Then $\sum b_j = ns + \sum r_j$ and $\sum b_j^2 = \sum(s + r_j)^2 = ns^2 + 2s\sum r_j + \sum r_j^2$.

Objective $= (n+1)(ns^2 + 2s\sum r_j + \sum r_j^2) - (ns + \sum r_j)^2$
$= (n+1)ns^2 + 2(n+1)s\sum r_j + (n+1)\sum r_j^2 - n^2s^2 - 2ns\sum r_j - (\sum r_j)^2$
$= n s^2 + 2s\sum r_j + (n+1)\sum r_j^2 - (\sum r_j)^2$

Let $R = \sum r_j$ and $Q = \sum r_j^2$. Then:
$= ns^2 + 2Rs + (n+1)Q - R^2$

This is a quadratic in $s$: $ns^2 + 2Rs + [(n+1)Q - R^2]$.

Minimum over real $s$ at $s = -R/n$, giving minimum value $(n+1)Q - R^2 - R^2/n = (n+1)Q - R^2(1 + 1/n) = (n+1)Q - \frac{(n+1)R^2}{n} = (n+1)(Q - R^2/n) = (n+1)V_r$

where $V_r = Q - R^2/n = \sum r_j^2 - (\sum r_j)^2/n$ is the variance of the $r_j$.

Since $s$ must be an integer, the actual minimum is achieved at $s = \text{round}(-R/n)$, and the penalty for non-integer $R/n$ is $n \cdot \{R/n\}^2$ where $\{x\}$ is the distance from $x$ to the nearest integer... actually more precisely, if $s^* = -R/n$ is the real optimum, and $s_0$ is the nearest integer, then the penalty is $n(s_0 - s^*)^2 = n \cdot \text{dist}(R/n, \mathbb{Z})^2$.

So the objective for a given shape $\{r_j\}$ is:
$(n+1)V_r + n \cdot \text{dist}(R/n, \mathbb{Z})^2$

where $V_r = \sum r_j^2 - R^2/n$ is the variance and $R = \sum r_j$.

Now, $V_r$ is translation-invariant (doesn't depend on the absolute position of the $r_j$, only their relative positions). And $R/n \mod 1$ depends on the shape.

For consecutive integers $r_j = 0, 1, \ldots, n-1$:
- $R = n(n-1)/2$
- $R/n = (n-1)/2$
- $V_r = \frac{n(n^2-1)}{12}$
- $\text{dist}(R/n, \mathbb{Z}) = 0$ if $n$ odd, $1/2$ if $n$ even.

So for consecutive integers:
- Odd $n$: objective $= (n+1) \cdot \frac{n(n^2-1)}{12} + 0$
- Even $n$: objective $= (n+1) \cdot \frac{n(n^2-1)}{12} + n/4$

Now, for any other shape, $V_r > \frac{n(n^2-1)}{12}$ (since consecutive integers minimize variance among distinct integers). The question is whether the $\text{dist}$ term can decrease enough to compensate.

For odd $n$: consecutive integers already achieve $\text{dist} = 0$, which is the minimum. So any other shape has $V_r > \frac{n(n^2-1)}{12}$ and $\text{dist} \geq 0$, giving a larger objective. Done.

For even $n$: consecutive integers have $\text{dist} = 1/2$, contributing $n/4$. We need to check if any shape with $\text{dist} = 0$ (i.e., $R \equiv 0 \pmod{n}$) has $V_r < \frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}$.

So the question becomes: for even $n$, what is the minimum $V_r$ over all sets of $n$ distinct non-negative integers $\{r_j\}$ with $r_1 = 0$ and $\sum r_j \equiv 0 \pmod{n}$?

If this minimum is $\geq \frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}$, then consecutive integers are optimal.

Hmm, this is getting complex. Let me try small cases.

$n = 2$: Consecutive $\{0, 1\}$: $V = 1/4 \cdot 2 = 1/2$... wait, $V_r = \sum r_j^2 - R^2/n = 0 + 1 - 1/2 = 1/2$. $\text{dist}(1/2, \mathbb{Z}) = 1/2$. Objective $= 3 \cdot 1/2 + 2 \cdot 1/4 = 3/2 + 1/2 = 2$.

Non-consecutive with $R \equiv 0 \pmod{2}$: $\{0, 2\}$: $R = 2$, $V_r = 0 + 4 - 2 = 2$. $\text{dist}(1, \mathbb{Z}) = 0$. Objective $= 3 \cdot 2 + 0 = 6 > 2$.

$\{0, r\}$ with $r$ even: $V_r = r^2 - r^2/2 = r^2/2$. Objective $= 3r^2/2 \geq 6$ for $r \geq 2$.

So consecutive is better for $n=2$.

$n = 4$: Consecutive $\{0,1,2,3\}$: $R = 6$, $R/n = 3/2$, $V_r = 0+1+4+9 - 36/4 = 14 - 9 = 5$. $\text{dist}(3/2, \mathbb{Z}) = 1/2$. Objective $= 5 \cdot 5 + 4 \cdot 1/4 = 26$.

Non-consecutive with $R \equiv 0 \pmod{4}$: We need $\sum r_j \equiv 0 \pmod 4$.

$\{0, 1, 2, 5\}$: $R = 8$, $V_r = 0+1+4+25 - 64/4 = 30 - 16 = 14$. Objective $= 5 \cdot 14 + 0 = 70$.

$\{0, 1, 3, 4\}$: $R = 8$, $V_r = 0+1+9+16 - 16 = 10$. Objective $= 50$.

$\{0, 2, 3, 3\}$: not distinct.

$\{0, 1, 4, 7\}$: $R = 12$, $V_r = 0+1+16+49 - 36 = 30$. Worse.

What about $\{0, 2, 4, 6\}$: $R = 12$, $V_r = 0+4+16+36 - 36 = 20$. Objective $= 100$.

$\{0, 1, 2, 3\}$ has $R = 6 \equiv 2 \pmod 4$. To get $R \equiv 0 \pmod 4$, we need to increase $R$ by 2 (or decrease by 2, but $r_1 = 0$ is fixed and values are non-negative).

The minimum increase in $V_r$ when we need $R \equiv 0 \pmod 4$ instead of $R \equiv 2 \pmod 4$:

Starting from $\{0,1,2,3\}$ with $R=6$, we need $R \equiv 0 \pmod 4$, so $R \in \{4, 8, 12, \ldots\}$. $R = 4$ would require decreasing by 2, but we can't go below $\{0,1,2,3\}$ in terms of $R$ (it's the minimum for 4 distinct non-negative integers). $R = 8$: we need to increase by 2.

To increase $R$ by 2 from $\{0,1,2,3\}$ with minimal increase in $V_r$: we could change one element. E.g., change 3 to 5: $\{0,1,2,5\}$, $R = 8$, $V_r = 14$. Or change 2 to 4: $\{0,1,3,4\}$, $R = 8$, $V_r = 10$. Or change 0 to 2: $\{1,2,2,3\}$ — not distinct. Or shift: $\{0,1,3,4\}$ is the best, $V_r = 10$.

Objective $= 5 \cdot 10 = 50 > 26$. So consecutive is better.

The increase in $V_r$ is $10 - 5 = 5$, while the savings in the dist term is $4/4 = 1$. So not worth it.

$n = 6$: Consecutive $\{0,1,2,3,4,5\}$: $R = 15$, $R/n = 5/2$, $V_r = \frac{6 \cdot 35}{12} = 17.5$. $\text{dist}(5/2, \mathbb{Z}) = 1/2$. Objective $= 7 \cdot 17.5 + 6/4 = 122.5 + 1.5 = 124$.

Non-consecutive with $R \equiv 0 \pmod 6$: $R = 15 \equiv 3 \pmod 6$. Need $R \equiv 0 \pmod 6$, so $R \in \{12, 18, 24, \ldots\}$. $R = 12$: decrease by 3. $R = 18$: increase by 3.

To increase $R$ by 3 from $\{0,1,2,3,4,5\}$ with minimal $V_r$ increase: change 5 to 8: $\{0,1,2,3,4,8\}$, $R = 18$, $V_r = 0+1+4+9+16+64 - 324/6 = 94 - 54 = 40$. That's a big increase.

Or change 4 to 7: $\{0,1,2,3,5,7\}$, $R = 18$, $V_r = 0+1+4+9+25+49 - 54 = 34$. Still big.

Or change 3 to 6: $\{0,1,2,4,5,6\}$, $R = 18$, $V_r = 0+1+4+16+25+36 - 54 = 28$. 

Or change 0 to 3: $\{1,2,3,3,4,5\}$ — not distinct.

Hmm, what about changing two elements? $\{0,1,2,4,5,6\}$: $R = 18$, $V_r = 28$. Objective $= 7 \cdot 28 = 196 > 124$.

Or decrease $R$ by 3: $\{0,1,2,3,4,2\}$ — not distinct. We need to decrease $R$ by 3 while keeping distinct non-negative integers with $r_1 = 0$. The minimum $R$ for 6 distinct non-negative integers is $0+1+2+3+4+5 = 15$. We can't decrease below this. So $R = 12$ is impossible.

Wait, actually we don't need $r_1 = 0$. We normalized to $r_1 = 0$ for convenience, but the shape is determined by the gaps. Let me reconsider.

Actually, the shape is determined by the relative positions. If we use the set $\{0, 1, 2, 3, 4, 5\}$ (consecutive), $R = 15 \equiv 3 \pmod 6$. To get $R \equiv 0 \pmod 6$, we need a different shape.

But the key point is: for any non-consecutive shape, $V_r > 17.5$, and the increase is at least... let me think about what the minimum $V_r$ is for a non-consecutive shape with $R \equiv 0 \pmod 6$.

The minimum $V_r$ for 6 distinct non-negative integers is 17.5 (consecutive). The next smallest $V_r$ for a non-consecutive set: take $\{0,1,2,3,4,6\}$ (increase the last gap by 1). $R = 16$, $V_r = 0+1+4+9+16+36 - 256/6 = 66 - 42.67 = 23.33$. But $R = 16 \equiv 4 \pmod 6$, not 0.

This is getting complicated. Let me try a different approach to prove the general result.

**General proof approach:**

I'll prove that for any $n$ distinct integers, $(n+1)\sum a_j^2 - (\sum a_j)^2 \geq C(n)$ where:
- $C(n) = \frac{n(n+1)(n^2-1)}{12}$ if $n$ is odd
- $C(n) = \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$ if $n$ is even

And that equality is achieved by consecutive integers centered at 0 (for odd $n$) or as close to 0 as possible (for even $n$).

Let me first verify the formula for small cases.

$n = 1$: $C(1) = \frac{1 \cdot 2 \cdot 0}{12} = 0$. The expression is $2a_1^2 - a_1^2 = a_1^2 \geq 1$ (since $a_1$ is a nonzero... wait, $a_1$ is a "pairwise distinct integer" — for $n=1$, any integer is trivially pairwise distinct. So $a_1$ can be 0, giving $a_1^2 = 0$. So $C(1) = 0$. ✓

$n = 2$: $C(2) = \frac{2 \cdot 3 \cdot 3}{12} + \frac{2}{4} = \frac{18}{12} + \frac{1}{2} = \frac{3}{2} + \frac{1}{2} = 2$. ✓ (matches our computation)

$n = 3$: $C(3) = \frac{3 \cdot 4 \cdot 8}{12} = 8$. Let's verify: $\{-1, 0, 1\}$, $\sum a_j^2 = 2$, $\sum a_j = 0$. $4 \cdot 2 - 0 = 8$. ✓

$n = 4$: $C(4) = \frac{4 \cdot 5 \cdot 15}{12} + 1 = 25 + 1 = 26$. ✓ (matches)

$n = 5$: $C(5) = \frac{5 \cdot 6 \cdot 24}{12} = 60$. Verify: $\{-2,-1,0,1,2\}$, $\sum a_j^2 = 10$, $\sum a_j = 0$. $6 \cdot 10 - 0 = 60$. ✓

$n = 6$: $C(6) = \frac{6 \cdot 7 \cdot 35}{12} + \frac{6}{4} = \frac{1470}{12} + \frac{3}{2} = 122.5 + 1.5 = 124$. ✓ (matches)

Great, the formula works. Now let me prove it.

**Proof:**

We want to minimize $F = (n+1)\sum a_j^2 - (\sum a_j)^2$ over all $n$-tuples of pairwise distinct integers.

As derived, $F = (n+1)V + n\bar{a}^2$ where $V = \sum(a_j - \bar{a})^2$ and $\bar{a} = \frac{1}{n}\sum a_j$.

**Step 1: $V \geq \frac{n(n^2-1)}{12}$ for $n$ distinct integers.**

This is a well-known result. For $n$ distinct integers, the variance is minimized when they are consecutive. The variance of $\{0, 1, \ldots, n-1\}$ is $\frac{n^2-1}{12}$, so $V = n \cdot \frac{n^2-1}{12} = \frac{n(n^2-1)}{12}$.

Proof: For sorted distinct integers $b_1 < b_2 < \ldots < b_n$, we have $b_j \geq b_1 + (j-1)$. Setting $c_j = b_j - (j-1)$, we get $c_1 \leq c_2 \leq \ldots \leq c_n$ (non-decreasing, since $b_{j+1} - b_j \geq 1$ means $c_{j+1} = b_{j+1} - j \geq b_j + 1 - j = c_j$). Actually, $c_j$ are non-decreasing integers.

Hmm, the standard proof uses the fact that for distinct real numbers, $\sum(a_j - \bar{a})^2 \geq \sum(j - \bar{j})^2$ where $j = 0, 1, \ldots, n-1$ (after sorting). This follows from the rearrangement/majorization argument.

Let me use a cleaner approach. For sorted $b_1 < \ldots < b_n$ (distinct integers, so $b_{j+1} \geq b_j + 1$), let $b_j = m + j - 1 + e_j$ where $m = b_1$ and $e_j \geq 0$ with $e_1 = 0$ and $e_{j+1} \geq e_j$ (non-decreasing). Then $b_j - \bar{b} = (j - 1 - \frac{n-1}{2}) + (e_j - \bar{e})$ where $\bar{e} = \frac{1}{n}\sum e_j$.

$V = \sum(b_j - \bar{b})^2 = \sum\left[(j-1-\frac{n-1}{2}) + (e_j - \bar{e})\right]^2$
$= \sum(j-1-\frac{n-1}{2})^2 + 2\sum(j-1-\frac{n-1}{2})(e_j - \bar{e}) + \sum(e_j - \bar{e})^2$

The cross term: $\sum(j-1-\frac{n-1}{2})(e_j - \bar{e}) = \sum(j-1-\frac{n-1}{2})e_j$ (since $\sum(j-1-\frac{n-1}{2}) = 0$).

Since $e_j$ is non-decreasing and $(j-1-\frac{n-1}{2})$ is increasing, by Chebyshev's sum inequality, $\frac{1}{n}\sum(j-1-\frac{n-1}{2})e_j \geq \frac{1}{n}\sum(j-1-\frac{n-1}{2}) \cdot \frac{1}{n}\sum e_j = 0$.

So the cross term is $\geq 0$, and $V \geq \sum(j-1-\frac{n-1}{2})^2 + \sum(e_j - \bar{e})^2 \geq \sum(j-1-\frac{n-1}{2})^2 = \frac{n(n^2-1)}{12}$.

Equality when $e_j = 0$ for all $j$ (consecutive integers) and the cross term is 0 (which it is when all $e_j = 0$).

**Step 2: For odd $n$, the minimum of $F$ is $\frac{n(n+1)(n^2-1)}{12}$.**

$F = (n+1)V + n\bar{a}^2 \geq (n+1) \cdot \frac{n(n^2-1)}{12} + n\bar{a}^2 \geq \frac{n(n+1)(n^2-1)}{12}$.

Equality when $V = \frac{n(n^2-1)}{12}$ (consecutive integers) and $\bar{a} = 0$.

For odd $n = 2k+1$, consecutive integers $\{-k, -k+1, \ldots, k\}$ have mean 0 and variance $\frac{n(n^2-1)}{12}$. So equality is achieved. ✓

**Step 3: For even $n$, the minimum of $F$ is $\frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$.**

This is the harder case. We need to show that for even $n$, $F \geq \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$.

$F = (n+1)V + n\bar{a}^2$.

Case 3a: If $V = \frac{n(n^2-1)}{12}$ (consecutive integers), then $\bar{a}$ is a half-integer (since $n$ is even), so $\bar{a}^2 \geq 1/4$, giving $F \geq (n+1) \cdot \frac{n(n^2-1)}{12} + \frac{n}{4}$. Equality when $\bar{a} = \pm 1/2$.

Case 3b: If $V > \frac{n(n^2-1)}{12}$ (non-consecutive), we need to show $F > \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$, i.e., $(n+1)(V - \frac{n(n^2-1)}{12}) + n\bar{a}^2 > \frac{n}{4}$.

Since $V > \frac{n(n^2-1)}{12}$ and $V$ takes values in a discrete set (as the $a_j$ are integers), we need $V - \frac{n(n^2-1)}{12} \geq \delta$ for some $\delta > 0$, and then $(n+1)\delta \geq \frac{n}{4}$ would suffice (since $n\bar{a}^2 \geq 0$).

But this might not hold in general. We need to be more careful.

Let me think about the minimum increase in $V$ when going from consecutive to non-consecutive integers.

For $n$ distinct integers, $V = \frac{n(n^2-1)}{12} + \Delta$ where $\Delta \geq 0$ and $\Delta = 0$ iff consecutive.

When the integers are not consecutive, at least one gap $d_i \geq 2$. The minimum $\Delta$ is achieved by making exactly one gap equal to 2 and the rest equal to 1.

If we take $\{0, 1, \ldots, i, i+2, i+3, \ldots, n\}$ (gap of 2 at position $i$, for $0 \leq i \leq n-2$), the variance is:

$\sum b_j^2 = \sum_{j=0}^{i} j^2 + \sum_{j=i+2}^{n} j^2 = \sum_{j=0}^{n} j^2 - (i+1)^2 = \frac{n(n+1)(2n+1)}{6} - (i+1)^2$

$R = \sum b_j = \sum_{j=0}^{i} j + \sum_{j=i+2}^{n} j = \frac{n(n+1)}{2} - (i+1)$

$V = \sum b_j^2 - R^2/n$

This is getting messy. Let me try a different approach.

Actually, let me think about the problem more carefully. The key insight is:

For even $n$, we need to show that $(n+1)V + n\bar{a}^2 \geq (n+1) \cdot \frac{n(n^2-1)}{12} + \frac{n}{4}$.

Equivalently, $(n+1)\left(V - \frac{n(n^2-1)}{12}\right) + n\left(\bar{a}^2 - \frac{1}{4}\right) \geq 0$.

If $\bar{a}^2 \geq 1/4$, this is immediate since both terms are non-negative.

If $\bar{a}^2 < 1/4$, then $|\bar{a}| < 1/2$. Since $\bar{a} = R/n$ where $R = \sum a_j$ is an integer and $n$ is even, $\bar{a} = R/n$. For $|\bar{a}| < 1/2$, we need $|R| < n/2$, i.e., $|R| \leq n/2 - 1$ (since $R$ is integer and $n/2$ is integer, $|R| \leq n/2 - 1$).

Hmm, but $\bar{a}$ could be 0, $1/n$, $2/n$, etc. For $\bar{a}^2 < 1/4$, we need $|R|/n < 1/2$, i.e., $|R| < n/2$, i.e., $|R| \leq n/2 - 1$.

In this case, we need to show that $V - \frac{n(n^2-1)}{12} \geq \frac{n(1/4 - \bar{a}^2)}{n+1}$.

The worst case is $\bar{a} = 0$ (i.e., $R = 0$), requiring $V - \frac{n(n^2-1)}{12} \geq \frac{n}{4(n+1)}$.

So the question is: for even $n$, what is the minimum variance $V$ of $n$ distinct integers summing to 0?

If this minimum is $\frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}$ or more, we're done.

Let me compute this for small even $n$.

$n = 2$: Distinct integers summing to 0: $\{-k, k\}$, $V = 2k^2 \geq 2$. $\frac{n(n^2-1)}{12} = \frac{2 \cdot 3}{12} = 1/2$. $\frac{n}{4(n+1)} = \frac{2}{12} = 1/6$. So $V - 1/2 \geq 2 - 1/2 = 3/2 \geq 1/6$. ✓

$n = 4$: Distinct integers summing to 0 with min variance: $\{-2, -1, 1, 2\}$, $V = 10$. $\frac{n(n^2-1)}{12} = 5$. $\frac{n}{4(n+1)} = \frac{4}{20} = 1/5$. $V - 5 = 5 \geq 1/5$. ✓

$n = 6$: $\{-3, -2, -1, 1, 2, 3\}$, $V = 2(1+4+9) = 28$. $\frac{n(n^2-1)}{12} = \frac{6 \cdot 35}{12} = 17.5$. $\frac{n}{4(n+1)} = \frac{6}{28} = 3/14 \approx 0.214$. $V - 17.5 = 10.5 \geq 0.214$. ✓

So the gap is huge. The minimum variance for mean-0 distinct integers is much larger than the consecutive variance plus $\frac{n}{4(n+1)}$.

Let me try to prove this in general.

For even $n = 2k$, the minimum variance set of $n$ distinct integers with mean 0 is $\{-k, -k+1, \ldots, -1, 1, \ldots, k\}$ (excluding 0). Its variance is:

$V_0 = 2\sum_{j=1}^{k} j^2 = \frac{k(k+1)(2k+1)}{3}$

The consecutive variance is:
$V_c = \frac{n(n^2-1)}{12} = \frac{2k(4k^2-1)}{12} = \frac{k(4k^2-1)}{6}$

We need $V_0 - V_c \geq \frac{n}{4(n+1)} = \frac{k}{2(2k+1)}$.

$V_0 - V_c = \frac{k(k+1)(2k+1)}{3} - \frac{k(4k^2-1)}{6} = \frac{k}{6}\left[2(k+1)(2k+1) - (4k^2-1)\right]$
$= \frac{k}{6}\left[2(2k^2+3k+1) - 4k^2+1\right] = \frac{k}{6}\left[4k^2+6k+2 - 4k^2+1\right] = \frac{k}{6}(6k+3) = \frac{k(6k+3)}{6} = \frac{k(2k+1)}{2}$

And $\frac{k}{2(2k+1)}$.

So we need $\frac{k(2k+1)}{2} \geq \frac{k}{2(2k+1)}$, i.e., $(2k+1) \geq \frac{1}{2k+1}$, i.e., $(2k+1)^2 \geq 1$, which is true for all $k \geq 0$.

But wait, I need to also verify that $\{-k, \ldots, -1, 1, \ldots, k\}$ is indeed the minimum variance set of $n = 2k$ distinct integers with mean 0. Let me prove this.

**Lemma:** For even $n = 2k$, the minimum of $\sum a_j^2$ over all sets of $2k$ distinct integers summing to 0 is $2\sum_{j=1}^k j^2 = \frac{k(k+1)(2k+1)}{3}$, achieved by $\{-k, \ldots, -1, 1, \ldots, k\}$.

*Proof of Lemma:* We want to minimize $\sum a_j^2$ subject to $\sum a_j = 0$ and the $a_j$ being $2k$ distinct integers.

Since $\sum a_j = 0$, $\sum a_j^2 = V$ (variance equals sum of squares when mean is 0).

The minimum variance for $2k$ distinct integers (without the mean-0 constraint) is $\frac{2k(4k^2-1)}{12}$, achieved by consecutive integers. But consecutive integers with even count have half-integer mean, so they can't sum to 0.

To get mean 0 with $2k$ distinct integers, we need to "symmetrize" the set. The most efficient way is to take the $2k$ integers closest to 0 that sum to 0, which is $\{-k, \ldots, -1, 1, \ldots, k\}$.

More rigorously: let the $2k$ distinct integers be $b_1 < b_2 < \ldots < b_{2k}$ with $\sum b_j = 0$. Since they're distinct and sum to 0, at least one is positive and at least one is negative (unless all are 0, impossible for distinct). 

Actually, let me think about it differently. We want $2k$ distinct integers summing to 0 with minimum $\sum a_j^2$. The optimal strategy is to choose integers as close to 0 as possible. The $2k+1$ integers closest to 0 are $\{-k, \ldots, 0, \ldots, k\}$, but we need only $2k$ of them and they must sum to 0. If we include 0, the remaining $2k-1$ must sum to 0, but $2k-1$ is odd, so we can take $\{-(k-1), \ldots, -1, 0, 1, \ldots, k-1, 0\}$ — no, that has a repeat. 

If we include 0, we need $2k-1$ other distinct integers summing to 0. The minimum sum of squares for $2k-1$ distinct integers summing to 0 is achieved by $\{-(k-1), \ldots, -1, 0, 1, \ldots, k-1\}$ — but that's $2k-1$ integers including 0, and we already have 0. So we'd have two 0s, not distinct.

So we can't include 0 if we want $2k$ distinct integers summing to 0 (well, we can, but then the other $2k-1$ must sum to 0 and be distinct from 0 and each other). Let me reconsider.

If 0 is one of the $2k$ integers, the other $2k-1$ distinct nonzero integers must sum to 0. The minimum $\sum a_j^2$ for $2k-1$ distinct nonzero integers summing to 0: take $\{-(k-1), \ldots, -1, 1, \ldots, k-1, \pm k\}$... hmm, $2k-1$ is odd, so we can't pair them up symmetrically. We'd need something like $\{-(k-1), \ldots, -1, 1, \ldots, k-1, m\}$ where $m = 0$ — but 0 is already taken. So $m$ must be some other integer, and the sum of the rest is 0, so $m$ must be 0, contradiction.

Wait, $\{-(k-1), \ldots, -1, 1, \ldots, k-1\}$ has $2(k-1) = 2k-2$ elements summing to 0. We need one more nonzero integer, but adding any nonzero integer breaks the sum. So we can't have $2k-1$ distinct nonzero integers summing to 0 if $2k-1$ is odd... actually, that's not right either. We could have $\{-k, -(k-2), \ldots, -1, 1, \ldots, (k-1)\}$ or something asymmetric.

This is getting complicated. Let me just argue directly.

**Claim:** The minimum $\sum a_j^2$ for $2k$ distinct integers summing to 0 is $\frac{k(k+1)(2k+1)}{3}$, achieved by $\{-k, \ldots, -1, 1, \ldots, k\}$.

*Proof:* Let $S = \{a_1, \ldots, a_{2k}\}$ be $2k$ distinct integers with $\sum a_j = 0$. Let $P = \{a_j : a_j > 0\}$ and $N = \{a_j : a_j < 0\}$ (and possibly $Z = \{a_j : a_j = 0\}$). 

Case 1: $0 \notin S$. Then $|P| + |N| = 2k$. Since $\sum_{P} a_j = -\sum_N a_j = T > 0$, and the elements of $P$ are distinct positive integers, $T \geq 1 + 2 + \ldots + |P| = \frac{|P|(|P|+1)}{2}$. Similarly, $T \geq \frac{|N|(|N|+1)}{2}$.

$\sum a_j^2 = \sum_P a_j^2 + \sum_N a_j^2 \geq \sum_{j=1}^{|P|} j^2 + \sum_{j=1}^{|N|} j^2 = \frac{|P|(|P|+1)(2|P|+1)}{6} + \frac{|N|(|N|+1)(2|N|+1)}{6}$.

With $|P| + |N| = 2k$, this is minimized when $|P| = |N| = k$ (by convexity), giving $\sum a_j^2 \geq 2 \cdot \frac{k(k+1)(2k+1)}{6} = \frac{k(k+1)(2k+1)}{3}$.

Equality when $P = \{1, \ldots, k\}$ and $N = \{-1, \ldots, -k\}$, i.e., $S = \{-k, \ldots, -1, 1, \ldots, k\}$.

Case 2: $0 \in S$. Then $|P| + |N| = 2k - 1$. Similarly, $\sum a_j^2 \geq \frac{|P|(|P|+1)(2|P|+1)}{6} + \frac{|N|(|N|+1)(2|N|+1)}{6}$.

With $|P| + |N| = 2k-1$ (odd), the minimum is at $|P| = k, |N| = k-1$ or $|P| = k-1, |N| = k$:
$\frac{k(k+1)(2k+1)}{6} + \frac{(k-1)k(2k-1)}{6} = \frac{k[(k+1)(2k+1) + (k-1)(2k-1)]}{6} = \frac{k[2k^2+3k+1+2k^2-3k+1]}{6} = \frac{k(4k^2+2)}{6} = \frac{k(2k^2+1)}{3}$.

Compare with Case 1: $\frac{k(k+1)(2k+1)}{3} = \frac{k(2k^2+3k+1)}{3}$.

Case 2 gives $\frac{k(2k^2+1)}{3}$ vs Case 1 gives $\frac{k(2k^2+3k+1)}{3}$. Since $2k^2+1 < 2k^2+3k+1$ for $k \geq 1$, Case 2 is better!

Wait, so including 0 is better? Let me check for $n = 4$ ($k = 2$).

Case 1: $\{-2, -1, 1, 2\}$, $\sum a_j^2 = 4+1+1+4 = 10$. Formula: $\frac{2 \cdot 3 \cdot 5}{3} = 10$. ✓

Case 2: $0 \in S$, $|P| = 2, |N| = 1$: $\{0, 1, 2, -3\}$, $\sum = 0$, $\sum a_j^2 = 0+1+4+9 = 14$. Formula: $\frac{2 \cdot 9}{3} = 6$... that doesn't match.

Hmm, I think I made an error. Let me recompute. For Case 2 with $|P| = k = 2, |N| = k-1 = 1$: the minimum $\sum_P a_j^2 = 1+4 = 5$ and $\sum_N a_j^2 = 1$. Total $= 0 + 5 + 1 = 6$. But the set is $\{0, 1, 2, -1\}$, which sums to $2 \neq 0$!

Ah, I see the issue. The constraint is $\sum a_j = 0$, which means $\sum_P a_j + \sum_N a_j = 0$ (since the 0 contributes nothing). So $\sum_P a_j = -\sum_N a_j = T$. But the minimum $\sum_P a_j^2$ given $\sum_P a_j = T$ and $|P|$ distinct positive integers is NOT simply $\sum_{j=1}^{|P|} j^2$ — that's the minimum when $T = \frac{|P|(|P|+1)}{2}$ (the minimum possible $T$). For larger $T$, the sum of squares is larger.

So my lower bound was wrong. Let me reconsider.

The correct approach: $\sum a_j^2 \geq \sum_{j=1}^{|P|} j^2 + \sum_{j=1}^{|N|} j^2$ only when $T = \frac{|P|(|P|+1)}{2} = \frac{|N|(|N|+1)}{2}$, which requires $|P| = |N|$ (or $|P| = |N| + 1$... no, $\frac{p(p+1)}{2} = \frac{q(q+1)}{2}$ implies $p = q$). So for $|P| \neq |N|$, the constraint $\sum_P a_j = -\sum_N a_j$ forces $T$ to be at least $\max(\frac{|P|(|P|+1)}{2}, \frac{|N|(|N|+1)}{2})$, and the side with smaller cardinality must have larger elements, increasing the sum of squares.

This makes the analysis more complex. Let me just verify numerically for small cases.

$n = 4$ ($k = 2$): 
- Without 0: $\{-2,-1,1,2\}$, $\sum a_j^2 = 10$.
- With 0: need 3 distinct nonzero integers summing to 0. E.g., $\{-1, 0, 1, ?\}$ — need one more, but $\{-1, 0, 1\}$ sums to 0, so the 4th must be 0 — not distinct. So $\{0, a, b, c\}$ with $a+b+c = 0$, distinct nonzero. E.g., $\{0, -1, -2, 3\}$: $\sum a_j^2 = 0+1+4+9 = 14$. Or $\{0, -1, 2, -1\}$ — not distinct. Or $\{0, -2, 1, 1\}$ — not distinct. Or $\{0, -3, 1, 2\}$: $\sum a_j^2 = 0+9+1+4 = 14$. Or $\{0, -1, -3, 4\}$: $0+1+9+16 = 26$.

So with 0, the minimum is 14 > 10. So Case 1 (without 0) is better for $n = 4$.

Let me redo the analysis. For Case 2 ($0 \in S$, $|P| + |N| = 2k-1$), the minimum $\sum a_j^2$ is achieved when $|P|$ and $|N|$ are as balanced as possible, but the constraint $\sum_P a_j = -\sum_N a_j$ means the side with fewer elements needs larger elements.

For $|P| = k, |N| = k-1$: $T = \sum_P a_j = -\sum_N a_j$. The minimum $T$ for $k$ distinct positive integers is $\frac{k(k+1)}{2}$, and the minimum $T$ for $k-1$ distinct negative integers (in absolute value) is $\frac{(k-1)k}{2}$. We need $T \geq \max(\frac{k(k+1)}{2}, \frac{(k-1)k}{2}) = \frac{k(k+1)}{2}$.

With $T = \frac{k(k+1)}{2}$, $P = \{1, \ldots, k\}$ (min sum of squares for this $T$), and $N$ must be $k-1$ distinct negative integers with $\sum |n_j| = \frac{k(k+1)}{2}$. The minimum $\sum n_j^2$ for $k-1$ distinct positive integers summing to $\frac{k(k+1)}{2}$: this is at least $\frac{(k-1)k}{2}$ (the minimum sum), so we need to distribute the excess $\frac{k(k+1)}{2} - \frac{(k-1)k}{2} = k$ among the $k-1$ elements.

This is getting quite involved. Let me just try to prove the main result directly without going through this case analysis.

**Direct proof for even $n$:**

We need to show that for even $n$ and any $n$ distinct integers, $F = (n+1)\sum a_j^2 - (\sum a_j)^2 \geq \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$.

Using $F = (n+1)V + n\bar{a}^2$ where $V = \sum(a_j - \bar{a})^2$:

If $V \geq \frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}$, then $F \geq (n+1)\left(\frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}\right) = \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$. Done.

If $V < \frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}$, then... we need to use the constraint on $\bar{a}$.

Since $V < \frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}$, the integers are "almost consecutive." Let me think about what this implies.

Actually, let me try a completely different approach. Let me use the representation in terms of the sorted values and gaps.

Let $a_1 < a_2 < \ldots < a_n$ be the sorted distinct integers. Write $a_j = a_1 + \sum_{i=1}^{j-1} d_i$ where $d_i = a_{i+1} - a_i \geq 1$ are positive integers (the gaps).

The objective $F = (n+1)\sum a_j^2 - (\sum a_j)^2$ can be written as:

$F = n\sum a_j^2 - 2\sum_{i<j} a_i a_j + \sum a_j^2 = \sum_{i<j}(a_i - a_j)^2 + \sum a_j^2$

Hmm, that's the identity I had before. Let me use:

$F = \sum_{i<j}(a_i - a_j)^2 + \sum a_j^2$

The first term $\sum_{i<j}(a_i - a_j)^2$ depends only on the gaps (translation-invariant), and the second term $\sum a_j^2$ depends on the absolute position.

For the first term: $\sum_{i<j}(a_j - a_i)^2 = \sum_{i<j}\left(\sum_{l=i}^{j-1} d_l\right)^2$.

This is minimized when all $d_l = 1$ (consecutive), giving $\sum_{i<j}(j-i)^2 = \frac{n^2(n^2-1)}{12}$... let me verify. $\sum_{i<j}(j-i)^2 = \sum_{d=1}^{n-1} (n-d) d^2 = \sum_{d=1}^{n-1} (nd^2 - d^3) = n \cdot \frac{(n-1)n(2n-1)}{6} - \left(\frac{(n-1)n}{2}\right)^2 = \frac{n^2(n-1)(2n-1)}{6} - \frac{n^2(n-1)^2}{4} = \frac{n^2(n-1)}{12}\left[2(2n-1) - 3(n-1)\right] = \frac{n^2(n-1)}{12}(4n-2-3n+3) = \frac{n^2(n-1)(n+1)}{12} = \frac{n^2(n^2-1)}{12}$.

So $\sum_{i<j}(a_i - a_j)^2 \geq \frac{n^2(n^2-1)}{12}$ with equality for consecutive integers.

And $F = \sum_{i<j}(a_i - a_j)^2 + \sum a_j^2 \geq \frac{n^2(n^2-1)}{12} + \sum a_j^2$.

Now, $\sum a_j^2 \geq$ the minimum sum of squares of $n$ distinct integers. But we also have the freedom to choose the gaps, so this lower bound might not be tight.

Hmm, this decomposition doesn't directly help because the two terms are coupled (choosing consecutive integers minimizes the first term but the second term depends on the position).

Let me go back to the approach of proving it for even $n$ by showing that non-consecutive sets can't beat consecutive sets.

**Key Lemma for even $n$:** For even $n$, if $n$ distinct integers are not consecutive, then $V \geq \frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}$.

Actually, I realize this might not be true in general. Let me think of a potential counterexample.

For $n = 4$: $\frac{n}{4(n+1)} = \frac{4}{20} = 0.2$. So we need $V \geq 5.2$ for non-consecutive sets. The minimum $V$ for non-consecutive 4 distinct integers: take $\{0, 1, 2, 4\}$, $V = 0+1+4+16 - 49/4 = 21 - 12.25 = 8.75$. Or $\{0, 1, 3, 4\}$, $V = 0+1+9+16 - 64/4 = 26 - 16 = 10$. Or $\{-1, 0, 1, 3\}$, $V = 1+0+1+9 - 9/4 = 11 - 2.25 = 8.75$.

So the minimum $V$ for non-consecutive 4 distinct integers is 8.75 (achieved by $\{0,1,2,4\}$ or equivalent). And $8.75 \geq 5.2$. ✓

But what about $\{0, 1, 2, 4\}$ with optimal centering? $R = 7$, $\bar{a} = 7/4$, optimal shift $s = -\text{round}(7/4) = -2$, giving $\{-2, -1, 0, 2\}$. $R = -1$, $\bar{a} = -1/4$, $\bar{a}^2 = 1/16$. $V = 8.75$ (translation-invariant). $F = 5 \cdot 8.75 + 4/16 = 43.75 + 0.25 = 44 > 26$. ✓

What about the set $\{0, 1, 2, 4\}$ shifted to have mean 0? We need $s + 7/4 = 0$, so $s = -7/4$, not integer. Closest: $s = -2$, mean $= -1/4$. Or $s = -1$, mean $= 3/4$. So we can't get mean 0 with this shape.

OK so let me try to prove the lemma more carefully.

**Lemma:** For even $n \geq 2$, if $a_1, \ldots, a_n$ are $n$ distinct integers that are not consecutive, then $V = \sum(a_j - \bar{a})^2 \geq \frac{n(n^2-1)}{12} + \frac{n}{4(n+1)}$.

Hmm, actually I'm not sure this is the right lemma. Let me think again.

The real question is: for even $n$, is the minimum of $(n+1)V + n\bar{a}^2$ always achieved by consecutive integers?

Let me try to prove this directly.

**Theorem:** For even $n = 2k$, the minimum of $F = (n+1)\sum a_j^2 - (\sum a_j)^2$ over all $n$-tuples of distinct integers is $\frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$, achieved by consecutive integers centered at $\pm 1/2$.

**Proof:** We've shown $F = (n+1)V + n\bar{a}^2$ where $V \geq \frac{n(n^2-1)}{12}$.

If $V = \frac{n(n^2-1)}{12}$ (consecutive), then $\bar{a}$ is a half-integer (for even $n$), so $\bar{a}^2 \geq 1/4$, giving $F \geq \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$, with equality at $\bar{a} = \pm 1/2$.

If $V > \frac{n(n^2-1)}{12}$, we need to show $F > \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$.

Since $V$ and $\bar{a}$ are determined by integer choices, $V$ takes values in a discrete set. The minimum value of $V$ above $\frac{n(n^2-1)}{12}$ is achieved by the "least non-consecutive" set, which has one gap of 2 and the rest of 1.

Let me compute the minimum $V$ for a non-consecutive set. WLOG, the set is $\{0, 1, \ldots, i, i+2, \ldots, n\}$ (gap of 2 at position $i$, $0 \leq i \leq n-2$). The variance is:

$V = \sum b_j^2 - \frac{(\sum b_j)^2}{n}$

$\sum b_j = \frac{n(n-1)}{2} + 1$ (we added 1 to the sum compared to consecutive, since we replaced $i+1$ with $i+2$... wait, no. The consecutive set is $\{0, 1, \ldots, n-1\}$ with sum $\frac{n(n-1)}{2}$. The non-consecutive set $\{0, 1, \ldots, i, i+2, \ldots, n\}$ has sum $\frac{n(n-1)}{2} + 1$ (we removed $i+1$ and added $i+2$, net change +1). Wait, actually the set is $\{0, 1, \ldots, i, i+2, i+3, \ldots, n\}$, which has $n$ elements (from 0 to $n$ excluding $i+1$). Sum $= \frac{n(n+1)}{2} - (i+1)$.

Hmm, let me be more careful. The consecutive set $\{0, 1, \ldots, n-1\}$ has $n$ elements. If I make one gap equal to 2, I get $\{0, 1, \ldots, i, i+2, i+3, \ldots, n\}$, which has $n$ elements (0 through $n$, excluding $i+1$). Sum $= \frac{n(n+1)}{2} - (i+1)$.

$\sum b_j^2 = \sum_{j=0}^{n} j^2 - (i+1)^2 = \frac{n(n+1)(2n+1)}{6} - (i+1)^2$.

$V = \frac{n(n+1)(2n+1)}{6} - (i+1)^2 - \frac{1}{n}\left(\frac{n(n+1)}{2} - (i+1)\right)^2$.

Let me denote $m = i+1$ (so $1 \leq m \leq n-1$). Then:

$V = \frac{n(n+1)(2n+1)}{6} - m^2 - \frac{1}{n}\left(\frac{n(n+1)}{2} - m\right)^2$

$= \frac{n(n+1)(2n+1)}{6} - m^2 - \frac{1}{n}\left(\frac{n^2(n+1)^2}{4} - n(n+1)m + m^2\right)$

$= \frac{n(n+1)(2n+1)}{6} - m^2 - \frac{n(n+1)^2}{4} + (n+1)m - \frac{m^2}{n}$

$= \frac{n(n+1)(2n+1)}{6} - \frac{n(n+1)^2}{4} + (n+1)m - m^2\left(1 + \frac{1}{n}\right)$

$= \frac{n(n+1)}{12}\left[2(2n+1) - 3(n+1)\right] + (n+1)m - \frac{(n+1)m^2}{n}$

$= \frac{n(n+1)}{12}(4n+2-3n-3) + (n+1)m - \frac{(n+1)m^2}{n}$

$= \frac{n(n+1)(n-1)}{12} + (n+1)m - \frac{(n+1)m^2}{n}$

$= \frac{n(n^2-1)}{12} + (n+1)m\left(1 - \frac{m}{n}\right)$

$= \frac{n(n^2-1)}{12} + \frac{(n+1)m(n-m)}{n}$

So $V = \frac{n(n^2-1)}{12} + \frac{(n+1)m(n-m)}{n}$ where $m = i+1 \in \{1, \ldots, n-1\}$.

The excess is $\Delta V = \frac{(n+1)m(n-m)}{n}$, which is minimized when $m = 1$ or $m = n-1$, giving $\Delta V = \frac{(n+1) \cdot 1 \cdot (n-1)}{n} = \frac{(n+1)(n-1)}{n} = \frac{n^2-1}{n}$.

So the minimum excess for a single-gap-of-2 set is $\frac{n^2-1}{n}$.

Now, for this set, the sum is $R = \frac{n(n+1)}{2} - m$. The mean is $\bar{a}_0 = \frac{R}{n} = \frac{n+1}{2} - \frac{m}{n}$.

After optimal integer centering, the mean becomes $\bar{a} = \bar{a}_0 - s$ where $s$ is the nearest integer to $\bar{a}_0$. So $|\bar{a}| = \text{dist}(\bar{a}_0, \mathbb{Z})$.

$\bar{a}_0 = \frac{n+1}{2} - \frac{m}{n}$. For even $n$, $\frac{n+1}{2}$ is a half-integer. So $\bar{a}_0 = \text{half-integer} - \frac{m}{n}$.

The distance to the nearest integer: $|\bar{a}| = |1/2 - \frac{m}{n}|$ if this is $\leq 1/2$, or $1 - |1/2 - \frac{m}{n}|$ otherwise. Actually, $\text{dist}(\bar{a}_0, \mathbb{Z}) = \text{dist}(1/2 - m/n, \mathbb{Z})$.

For $m/n$ rational, $1/2 - m/n$ could be close to 0 or close to 1/2.

The objective for this set is:
$F = (n+1)V + n\bar{a}^2 = (n+1)\left(\frac{n(n^2-1)}{12} + \frac{(n+1)m(n-m)}{n}\right) + n \cdot \text{dist}\left(\frac{n+1}{2} - \frac{m}{n}, \mathbb{Z}\right)^2$

$= \frac{n(n+1)(n^2-1)}{12} + \frac{(n+1)^2 m(n-m)}{n} + n \cdot \text{dist}\left(\frac{1}{2} - \frac{m}{n}, \mathbb{Z}\right)^2$

We need this to be $\geq \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$, i.e.:

$\frac{(n+1)^2 m(n-m)}{n} + n \cdot \text{dist}\left(\frac{1}{2} - \frac{m}{n}, \mathbb{Z}\right)^2 \geq \frac{n}{4}$

The first term is $\frac{(n+1)^2 m(n-m)}{n} \geq \frac{(n+1)^2 \cdot 1 \cdot (n-1)}{n} = \frac{(n+1)^2(n-1)}{n}$.

For $n \geq 2$, $\frac{(n+1)^2(n-1)}{n} \geq \frac{9 \cdot 1}{2} = 4.5 > \frac{n}{4}$ for $n = 2$. And for larger $n$, the LHS grows much faster. So the inequality holds easily.

But wait, I only considered single-gap-of-2 sets. What about sets with larger gaps or multiple non-1 gaps? Those would have even larger $V$, so the first term would be even larger. So the inequality holds for all non-consecutive sets.

Actually, I need to be more careful. The minimum excess $\Delta V$ for a non-consecutive set is $\frac{n^2-1}{n}$ (single gap of 2). Any other non-consecutive set has $\Delta V \geq \frac{n^2-1}{n}$. And $\frac{(n+1) \cdot (n^2-1)/n}{} $... wait, the first term in the inequality is $(n+1) \cdot \Delta V$, which is $\geq (n+1) \cdot \frac{n^2-1}{n} = \frac{(n+1)(n^2-1)}{n}$.

We need $\frac{(n+1)(n^2-1)}{n} \geq \frac{n}{4}$, i.e., $4(n+1)(n^2-1) \geq n^2$, i.e., $4(n+1)(n-1)(n+1) \geq n^2$... wait, $n^2-1 = (n-1)(n+1)$, so $4(n+1)^2(n-1) \geq n^2$.

For $n = 2$: $4 \cdot 9 \cdot 1 = 36 \geq 4$. ✓
For $n = 4$: $4 \cdot 25 \cdot 3 = 300 \geq 16$. ✓

Clearly true for all $n \geq 2$.

But wait, I need to be more careful. The excess $\Delta V$ for a general non-consecutive set might not be exactly $\frac{(n+1)m(n-m)}{n}$. That formula was for a specific type of non-consecutive set (single gap of 2). For a general non-consecutive set, $\Delta V$ could be different.

Let me reconsider. I showed that for a set with a single gap of 2 at position $m$, $\Delta V = \frac{(n+1)m(n-m)}{n}$. The minimum of this over $m$ is $\frac{(n+1)(n-1)}{n} = \frac{n^2-1}{n}$.

For a general non-consecutive set, the excess $\Delta V$ is at least $\frac{n^2-1}{n}$ (since the single-gap-of-2 set is the "closest" to consecutive). This is because $V$ is a convex function of the gaps, and the minimum non-consecutive configuration is a single gap of 2.

Actually, I should prove this more carefully. Let me think about it.

For sorted distinct integers with gaps $d_1, \ldots, d_{n-1} \geq 1$, the variance $V$ is a function of the gaps. We've shown $V = \frac{n(n^2-1)}{12} + \text{(excess)}$, and the excess is 0 when all $d_i = 1$. The excess is a quadratic form in the "extra gaps" $e_i = d_i - 1 \geq 0$.

For a single $e_i = 1$ (gap of 2 at position $i$, i.e., $m = i+1$), the excess is $\frac{(n+1)m(n-m)}{n}$.

For general $e_i$, the excess is a positive definite quadratic form (since $V$ is minimized at $e_i = 0$). The minimum excess for a nonzero $e$ vector is achieved at a vertex of the simplex, i.e., a single $e_i = 1$, giving excess $\geq \frac{n^2-1}{n}$.

Actually, I need to be more careful. The excess might not be a simple quadratic form in $e_i$ because the mean also changes. Let me think about this differently.

Actually, I already proved in Step 1 that $V \geq \frac{n(n^2-1)}{12}$ with equality iff consecutive, using the Chebyshev inequality argument. And I computed the excess for a single-gap-of-2 set. For a general non-consecutive set, the excess is at least as large as the minimum single-gap excess, because:

The excess $\Delta V = V - \frac{n(n^2-1)}{12}$ is a non-negative quantity that equals 0 only for consecutive integers. For integer-valued gaps, the minimum positive value of $\Delta V$ is achieved by the "closest to consecutive" non-consecutive set, which is a single gap of 2.

But I should verify that $\Delta V$ for a single gap of 2 is indeed the minimum. Let me check: for two gaps of 2 (e.g., $\{0, 2, 4, \ldots\}$), the excess would be larger. And for a single gap of 3, the excess would also be larger. So yes, the minimum excess is $\frac{n^2-1}{n}$.

Hmm, but I computed the excess for a single gap of 2 at position $m$ to be $\frac{(n+1)m(n-m)}{n}$, which is minimized at $m=1$ or $m=n-1$ giving $\frac{n^2-1}{n}$. For $m$ in the middle, the excess is larger. So the minimum excess over all non-consecutive sets is $\frac{n^2-1}{n}$.

Now, for the objective:
$F = \frac{n(n+1)(n^2-1)}{12} + (n+1)\Delta V + n\bar{a}^2$

For a non-consecutive set, $\Delta V \geq \frac{n^2-1}{n}$, so:
$F \geq \frac{n(n+1)(n^2-1)}{12} + (n+1) \cdot \frac{n^2-1}{n} + 0 = \frac{n(n+1)(n^2-1)}{12} + \frac{(n+1)(n^2-1)}{n}$

We need this to be $\geq \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$, i.e., $\frac{(n+1)(n^2-1)}{n} \geq \frac{n}{4}$.

$\frac{(n+1)(n^2-1)}{n} = \frac{(n+1)^2(n-1)}{n} \geq \frac{n}{4}$.

For $n \geq 2$: $\frac{(n+1)^2(n-1)}{n} \geq \frac{9 \cdot 1}{2} = 4.5 \geq \frac{2}{4} = 0.5$. ✓

And for $n \geq 2$, $(n+1)^2(n-1)/n$ grows much faster than $n/4$, so the inequality holds for all even $n \geq 2$.

Wait, but I need to also handle the case where $\bar{a}^2$ is not 0. In the above, I used $\bar{a}^2 \geq 0$, which is fine. The point is that even with $\bar{a} = 0$ (best case for the mean term), the excess in $V$ more than compensates.

So for even $n \geq 2$, any non-consecutive set gives $F > \frac{n(n+1)(n^2-1)}{12} + \frac{n}{4}$, and consecutive integers with $\bar{a} = \pm 1/2$ achieve equality. QED.

Wait, I need to double-check that the minimum excess for a non-consecutive set is indeed $\frac{n^2-1}{n}$. Let me verify for $n = 4$.

$n = 4$, single gap of 2 at $m = 1$: set $\{0, 2, 3, 4\}$, $V = 0+4+9+16 - 81/4 = 29 - 20.25 = 8.75$. $\frac{n(n^2-1)}{12} = 5$. Excess $= 3.75$. $\frac{n^2-1}{n} = \frac{15}{4} = 3.75$. ✓

$m = 2$: set $\{0, 1, 3, 4\}$, $V = 0+1+9+16 - 64/4 = 26 - 16 = 10$. Excess $= 5$. $\frac{(n+1)m(n-m)}{n} = \frac{5 \cdot 2 \cdot 2}{4} = 5$. ✓

So the minimum excess is indeed at $m = 1$ (or $m = 3$), giving $\frac{n^2-1}{n}$.

Great. Now let me also verify that for a set with a gap of 3 (instead of 2), the excess is larger.

$n = 4$, gap of 3 at $m = 1$: set $\{0, 3, 4, 5\}$, $V = 0+9+16+25 - 144/4 = 50 - 36 = 14$. Excess $= 9 > 3.75$. ✓

And for two gaps of 2: set $\{0, 2, 4, 6\}$, $V = 0+4+16+36 - 144/4 = 56 - 36 = 20$. Excess $= 15 > 3.75$. ✓

So the minimum excess is indeed $\frac{n^2-1}{n}$, achieved by a single gap of 2 at the end.

Now, I also need to verify that I haven't missed any non-consecutive configurations. What about sets that aren't of the form "consecutive with one gap increased"? E.g., $\{0, 1, 3, 5\}$ for $n = 4$. This has gaps 1, 2, 2. $V = 0+1+9+25 - 81/4 = 35 - 20.25 = 14.75$. Excess $= 9.75 > 3.75$. ✓

So all non-consecutive sets have excess $\geq \frac{n^2-1}{n}$, and the proof goes through.

Actually, I realize I should prove more rigorously that the minimum excess for any non-consecutive set is $\frac{n^2-1}{n}$. Let me do this.

**Claim:** For $n$ distinct integers that are not consecutive, $V \geq \frac{n(n^2-1)}{12} + \frac{n^2-1}{n}$.

*Proof:* From Step 1, $V = \frac{n(n^2-1)}{12} + \Delta$ where $\Delta = 2\sum_{j=1}^{n}(j-1-\frac{n-1}{2})e_j + \sum(e_j - \bar{e})^2$ and $e_j$ are non-decreasing non-negative integers with $e_1 = 0$ (using the notation from Step 1).

Since the set is not consecutive, not all $e_j = 0$. Since $e_j$ are non-decreasing integers with $e_1 = 0$ and not all zero, there exists some $j$ with $e_j \geq 1$.

The cross term $2\sum(j-1-\frac{n-1}{2})e_j \geq 0$ by Chebyshev's inequality (as shown in Step 1).

The variance term $\sum(e_j - \bar{e})^2 \geq 0$.

So $\Delta \geq 0$, and we need to show $\Delta \geq \frac{n^2-1}{n}$ when not all $e_j = 0$.

Hmm, this isn't immediate. The cross term could be 0 (if $e_j$ is constant, but $e_1 = 0$ so constant means all 0). The variance term is 0 iff all $e_j$ are equal, which means all 0. So for non-zero $e$, at least one of the two terms is positive.

But I need a lower bound on $\Delta$. Let me think about this differently.

Actually, since $e_j$ are non-decreasing integers with $e_1 = 0$ and not all zero, the simplest non-zero case is $e_n = 1$ and all others 0 (i.e., only the last element is shifted by 1). This corresponds to the single gap of 2 at the end ($m = n-1$).

In this case, $\bar{e} = 1/n$, and:
- Cross term: $2\sum(j-1-\frac{n-1}{2})e_j = 2(n-1-\frac{n-1}{2}) \cdot 1 = 2 \cdot \frac{n-1}{2} = n-1$.
- Variance term: $\sum(e_j - \bar{e})^2 = (0 - 1/n)^2 \cdot (n-1) + (1 - 1/n)^2 = \frac{n-1}{n^2} + \frac{(n-1)^2}{n^2} = \frac{n-1 + (n-1)^2}{n^2} = \frac{(n-1)n}{n^2} = \frac{n-1}{n}$.
- $\Delta = (n-1) + \frac{n-1}{n} = \frac{n(n-1) + (n-1)}{n} = \frac{(n-1)(n+1)}{n} = \frac{n^2-1}{n}$. ✓

For $e_j = 1$ for $j = 2, \ldots, n$ (i.e., shift all but the first by 1, corresponding to a gap of 2 at the beginning, $m = 1$):
- $\bar{e} = (n-1)/n$.
- Cross term: $2\sum_{j=2}^{n}(j-1-\frac{n-1}{2}) \cdot 1 = 2\left[\sum_{j=0}^{n-1}(j - \frac{n-1}{2}) - (0 - \frac{n-1}{2})\right] = 2 \cdot \frac{n-1}{2} = n-1$.
- Variance term: $(0 - \frac{n-1}{n})^2 + (n-1)(1 - \frac{n-1}{n})^2 = \frac{(n-1)^2}{n^2} + (n-1) \cdot \frac{1}{n^2} = \frac{(n-1)^2 + (n-1)}{n^2} = \frac{n-1}{n}$.
- $\Delta = (n-1) + \frac{n-1}{n} = \frac{n^2-1}{n}$. ✓ (Same as before, by symmetry.)

For a general non-zero $e$, I need to show $\Delta \geq \frac{n^2-1}{n}$. 

Let me think about this. $\Delta = 2\sum w_j e_j + \sum(e_j - \bar{e})^2$ where $w_j = j - 1 - \frac{n-1}{2}$ (which ranges from $-\frac{n-1}{2}$ to $\frac{n-1}{2}$).

Since $e_j$ is non-decreasing with $e_1 = 0$ and $w_j$ is increasing, by Chebyshev: $\sum w_j e_j \geq \frac{1}{n}
