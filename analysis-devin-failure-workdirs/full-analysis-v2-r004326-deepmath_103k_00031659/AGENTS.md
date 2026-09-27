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

- **CONNECTION_ERROR**: The AI didn't really attempt the problem — the thinking is extremely short (< 500 chars), contains API connection errors, garbled text, or has NO mathematical content at all (e.g., only error messages or empty output). This is a technical failure, not a mathematical one. **Important**: If the AI solved a DIFFERENT problem than the one given (wrong problem, misread problem), that is DIRECTION_ERROR, not CONNECTION_ERROR. CONNECTION_ERROR is only for technical failures where no real thinking happened.

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
  <problem_id>deepmath_103k_00031659</problem_id>
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
- If the AI's thinking is too short to analyze (< 500 chars AND no mathematical content), output CONNECTION_ERROR. But if the AI solved a different problem or went in the wrong direction, use DIRECTION_ERROR even if the thinking is short.
- If you cannot determine the turning point type, use "other" and explain in dimension2_explanation

## Problem

Evaluate the integral \( \int_{|z-1|=1}\frac{dz}{z^2-1} \) using the Cauchy Integral Formula.

## Standard Solution

Okay, so I need to evaluate the integral \( \int_{|z-1|=1}\frac{dz}{z^2-1} \) using the Cauchy Integral Formula. Let me start by recalling what the Cauchy Integral Formula is. From what I remember, it states that if a function f is analytic inside and on some simple closed contour C, and z₀ is a point inside C, then the integral of f(z)/(z - z₀) around C is 2πi times f(z₀). But here, my integrand is 1/(z² - 1). Hmm, maybe I need to factor the denominator to see if it can be expressed in a form suitable for applying the Cauchy formula.

The denominator z² - 1 factors into (z - 1)(z + 1). So the integrand becomes 1/[(z - 1)(z + 1)]. Now, the contour of integration is |z - 1| = 1, which is a circle centered at z = 1 with radius 1. Let me visualize that. The center is at 1, radius 1, so this circle goes from 0 to 2 on the real axis. The other singularity in the denominator is at z = -1. Is that point inside the contour? Since the circle is centered at 1 with radius 1, the distance from 1 to -1 is 2, which is greater than the radius 1, so z = -1 is outside the contour. Therefore, only z = 1 is inside the contour.

So, the integrand has two singular points, z = 1 and z = -1, but only z = 1 is inside the contour |z - 1| = 1. Therefore, maybe I can apply the Cauchy Integral Formula here. Let me recall that the formula requires the integrand to be of the form f(z)/(z - z₀), where f(z) is analytic inside and on the contour. Let's see. If I write 1/[(z - 1)(z + 1)] as [1/(z + 1)]/(z - 1), then that's in the form f(z)/(z - z₀), where f(z) = 1/(z + 1) and z₀ = 1. Is f(z) analytic inside and on the contour? Since f(z) = 1/(z + 1) has a singularity at z = -1, which is outside the contour, so yes, f(z) is analytic inside and on the contour |z - 1| = 1. Perfect!

Therefore, by the Cauchy Integral Formula, the integral should be 2πi times f(z₀) = 2πi * f(1). Calculating f(1) is easy: f(1) = 1/(1 + 1) = 1/2. Therefore, the integral is 2πi * (1/2) = πi. So, is that the answer? Wait, let me check.

Alternatively, maybe I should use the Residue Theorem. But since the problem specifically asks to use the Cauchy Integral Formula, let's stick with that. Let me verify my steps again. First, factor the denominator: z² - 1 = (z - 1)(z + 1). Then, express 1/(z² - 1) as [1/(z + 1)]/(z - 1). Then, since z = 1 is inside the contour and z = -1 is outside, f(z) = 1/(z + 1) is analytic on and inside the contour. Applying the Cauchy Integral Formula, which says that ∫_C [f(z)/(z - z₀)] dz = 2πi f(z₀). Here, z₀ = 1, so yes, that gives 2πi * f(1) = 2πi*(1/2) = πi. That seems correct.

Wait, but maybe I made a mistake in splitting the integrand. Let me confirm. Suppose I write 1/(z² - 1) = A/(z - 1) + B/(z + 1) using partial fractions. Then, solving for A and B:

1 = A(z + 1) + B(z - 1). Letting z = 1: 1 = A(2) + B(0) ⇒ A = 1/2. Letting z = -1: 1 = A(0) + B(-2) ⇒ B = -1/2. So, partial fractions decomposition gives (1/2)/(z - 1) - (1/2)/(z + 1). Therefore, the integral becomes (1/2) ∫_{|z-1|=1} [1/(z - 1) - 1/(z + 1)] dz.

Now, integrating term by term. The first integral is (1/2) ∫ 1/(z - 1) dz over |z -1| =1. That's (1/2)*2πi = πi, by the Cauchy Integral Formula with f(z) =1 and z₀=1. The second integral is -(1/2) ∫ 1/(z + 1) dz over |z -1|=1. But z = -1 is outside the contour, so by Cauchy's Theorem, since 1/(z +1) is analytic inside and on the contour, the integral is zero. Therefore, total integral is πi - 0 = πi. So this confirms the previous result. Therefore, the answer should be πi.

Wait, but maybe I should check again if z = -1 is indeed outside the contour. The contour is |z -1| =1. The point z = -1 is at a distance | -1 -1 | = 2 from z=1. Since the radius of the contour is 1, which is less than 2, yes, z = -1 is outside. Therefore, the integral over the second term is zero. Therefore, the answer is πi.

Alternatively, if I try to compute the integral directly using residues. The integrand has poles at z =1 and z=-1. Only z=1 is inside the contour. The residue at z=1 is lim_{z→1} (z -1)*[1/(z² -1)] = lim_{z→1} 1/(z +1) = 1/2. Then, the integral is 2πi*(1/2) = πi. So that's another way to see it, using the Residue Theorem. But since the problem asks for the Cauchy Integral Formula, maybe the first approach is the expected method.

Therefore, after checking through partial fractions, residues, and the direct application of the Cauchy Integral Formula, all methods lead to the same answer of πi. Therefore, I think that's the correct result. I don't see any mistakes in the reasoning, so I think the integral evaluates to πi.

**Final Answer**
The value of the integral is \boxed{\pi i}.
</think>

To evaluate the integral \( \int_{|z-1|=1}\frac{dz}{z^2-1} \) using the Cauchy Integral Formula, we start by factoring the denominator:

\[
\frac{1}{z^2 - 1} = \frac{1}{(z - 1)(z + 1)}
\]

The contour of integration is the circle centered at \( z = 1 \) with radius 1, denoted \( |z - 1| = 1 \). This contour encloses the singularity at \( z = 1 \) but excludes the singularity at \( z = -1 \) (since the distance from 1 to -1 is 2, which is greater than the radius 1).

We rewrite the integrand in a form suitable for applying the Cauchy Integral Formula:

\[
\frac{1}{(z - 1)(z + 1)} = \frac{\frac{1}{z + 1}}{z - 1}
\]

Here, \( f(z) = \frac{1}{z + 1} \) is analytic inside and on the contour because the singularity at \( z = -1 \) is outside the contour. By the Cauchy Integral Formula, we have:

\[
\int_{|z-1|=1} \frac{f(z)}{z - 1} \, dz = 2\pi i f(1)
\]

Substituting \( f(1) = \frac{1}{1 + 1} = \frac{1}{2} \):

\[
2\pi i \cdot \frac{1}{2} = \pi i
\]

To confirm, we use partial fractions decomposition:

\[
\frac{1}{z^2 - 1} = \frac{1}{2} \left( \frac{1}{z - 1} - \frac{1}{z + 1} \right)
\]

Integrating term by term over the contour \( |z - 1| = 1 \):

- The integral of \( \frac{1}{z - 1} \) is \( 2\pi i \), giving \( \frac{1}{2} \cdot 2\pi i = \pi i \).
- The integral of \( \frac{1}{z + 1} \) is 0 because \( z = -1 \) is outside the contour.

Thus, the integral evaluates to \( \pi i \).

Using the Residue Theorem, the residue at \( z = 1 \) is \( \frac{1}{2} \), leading to the same result:

\[
2\pi i \cdot \frac{1}{2} = \pi i
\]

The value of the integral is \boxed{\pi i}.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We need to find the smallest positive real number $c$ such that for any positive reals $x_1, \ldots, x_n$:
$$\frac{1}{n}\sum_{i=1}^n x_i - \sqrt[n]{\prod_{i=1}^n x_i} \leq c \cdot \sum_{1 \leq i < j \leq n} (\sqrt{x_i} - \sqrt{x_j})^2$$

Let me set $y_i = \sqrt{x_i}$, so $x_i = y_i^2$ with $y_i > 0$.

LHS: $\frac{1}{n}\sum y_i^2 - \left(\prod y_i^2\right)^{1/n} = \frac{1}{n}\sum y_i^2 - \left(\prod y_i\right)^{2/n}$

RHS: $c \sum_{i<j} (y_i - y_j)^2$

Note that $\sum_{i<j}(y_i - y_j)^2 = n\sum y_i^2 - (\sum y_i)^2$.

Let me denote $A = \frac{1}{n}\sum y_i^2$ (mean of squares) and $G = (\prod y_i)^{1/n}$ (geometric mean of $y_i$), and $S = \sum y_i$, $Q = \sum y_i^2$.

So LHS $= A - G^2 = \frac{Q}{n} - G^2$.

RHS $= c(nQ - S^2)$.

The inequality is homogeneous of degree 2 in $y$. So we can normalize, e.g., set $G = 1$ (i.e., $\prod y_i = 1$), or set $Q = n$ (i.e., $A = 1$).

Let me set $\prod y_i = 1$, so $G = 1$. Then LHS $= A - 1 = \frac{Q}{n} - 1$.

RHS $= c(nQ - S^2)$.

We need: $\frac{Q}{n} - 1 \leq c(nQ - S^2)$, i.e., $\frac{Q - n}{n} \leq c(nQ - S^2)$.

So $c \geq \frac{Q - n}{n(nQ - S^2)}$.

We want the supremum of $\frac{Q-n}{n(nQ - S^2)}$ over all $y_i > 0$ with $\prod y_i = 1$ and not all equal.

When all $y_i$ equal (all = 1), both numerator and denominator are 0, so we need to look at the limit.

Let me consider the case where $n-1$ variables are equal to some value $a$ and one variable is $b$, with $a^{n-1} b = 1$, so $b = a^{-(n-1)}$.

Actually, let me think about which configuration maximizes the ratio. 

Let me first try the case $n = 2$ to get intuition.

For $n = 2$: $y_1, y_2$ with $y_1 y_2 = 1$. Let $y_1 = t, y_2 = 1/t$.

$Q = t^2 + 1/t^2$, $S = t + 1/t$.

Numerator: $Q - 2 = t^2 + 1/t^2 - 2 = (t - 1/t)^2$.

Denominator: $n(nQ - S^2) = 2(2(t^2+1/t^2) - (t+1/t)^2) = 2(2t^2 + 2/t^2 - t^2 - 2 - 1/t^2) = 2(t^2 + 1/t^2 - 2) = 2(t-1/t)^2$.

So ratio $= \frac{(t-1/t)^2}{2(t-1/t)^2} = \frac{1}{2}$.

So for $n = 2$, $c = 1/2$.

Now let me think about general $n$. Let me try the configuration where one variable is large and the rest are 1 (approximately). Actually with the constraint $\prod y_i = 1$, let me set $y_1 = t$ and $y_2 = \cdots = y_n = t^{-1/(n-1)}$.

As $t \to \infty$: $Q \approx t^2$, $S \approx t$, $nQ - S^2 \approx nt^2 - t^2 = (n-1)t^2$.

Ratio $\approx \frac{t^2}{n \cdot (n-1) t^2} = \frac{1}{n(n-1)}$.

Hmm, that gives $1/(n(n-1))$ which for $n=2$ is $1/2$. Good, consistent.

But is this the maximum? Let me try another configuration. Let $k$ variables be large ($= t$) and $n-k$ be small to maintain $\prod = 1$.

Let $y_1 = \cdots = y_k = t$ and $y_{k+1} = \cdots = y_n = t^{-k/(n-k)}$.

As $t \to \infty$: $Q \approx k t^2$, $S \approx k t$, $nQ - S^2 \approx nk t^2 - k^2 t^2 = k(n-k) t^2$.

Ratio $\approx \frac{kt^2}{n \cdot k(n-k) t^2} = \frac{1}{n(n-k)}$.

To maximize, we want $n-k$ small, i.e., $k = n-1$, giving $\frac{1}{n}$.

Wait, that's larger than $1/(n(n-1))$. Let me recheck.

With $k = n-1$: $y_1 = \cdots = y_{n-1} = t$, $y_n = t^{-(n-1)}$.

$Q = (n-1)t^2 + t^{-2(n-1)}$, $S = (n-1)t + t^{-(n-1)}$.

As $t \to \infty$: $Q \approx (n-1)t^2$, $S \approx (n-1)t$.

$nQ - S^2 \approx n(n-1)t^2 - (n-1)^2 t^2 = (n-1)(n - (n-1))t^2 = (n-1)t^2$.

Ratio $\approx \frac{(n-1)t^2}{n \cdot (n-1) t^2} = \frac{1}{n}$.

So this gives $1/n$, which is larger than $1/(n(n-1))$ for $n \geq 2$.

So the supremum is at least $1/n$. Can it be even larger?

Let me try to see if the ratio can exceed $1/n$. Let me consider the general case more carefully.

We want to maximize $R = \frac{Q - n}{n(nQ - S^2)}$ subject to $\prod y_i = 1$.

Equivalently (since the original is homogeneous of degree 2, and we normalized by $G=1$), let's think about it differently. Let me not fix $\prod y_i = 1$ but instead use homogeneity.

The original expression: $\frac{Q/n - G^2}{nQ - S^2}$ where $G = (\prod y_i)^{1/n}$. This is homogeneous of degree 0, so we can normalize freely.

Let me normalize $Q = n$ (so $A = 1$). Then we want to maximize $\frac{1 - G^2}{n^2 - S^2}$, i.e., minimize $G^2$ and maximize $S^2$... actually we want to maximize the ratio $\frac{1-G^2}{n^2 - S^2}$ (note $nQ = n^2$).

With $Q = n$: $S^2 \leq nQ = n^2$ by Cauchy-Schwarz, with equality when all equal. And $G^2 \leq Q/n = 1$ by AM-GM, with equality when all equal.

So both numerator and denominator go to 0 as we approach equality. We need the ratio of the rates.

Let me use a perturbation approach. Set $y_i = 1 + \epsilon_i$ with $\sum \epsilon_i$ small.

$Q = \sum(1+\epsilon_i)^2 = n + 2\sum\epsilon_i + \sum\epsilon_i^2$.

$S = n + \sum\epsilon_i$.

$nQ - S^2 = n(n + 2\sum\epsilon_i + \sum\epsilon_i^2) - (n + \sum\epsilon_i)^2 = n^2 + 2n\sum\epsilon_i + n\sum\epsilon_i^2 - n^2 - 2n\sum\epsilon_i - (\sum\epsilon_i)^2 = n\sum\epsilon_i^2 - (\sum\epsilon_i)^2$.

$G^2 = \left(\prod(1+\epsilon_i)\right)^{2/n}$. 

$\log G = \frac{1}{n}\sum \log(1+\epsilon_i) \approx \frac{1}{n}\sum(\epsilon_i - \epsilon_i^2/2) = \frac{\sum\epsilon_i}{n} - \frac{\sum\epsilon_i^2}{2n}$.

$G^2 = e^{2\log G} \approx e^{\frac{2\sum\epsilon_i}{n} - \frac{\sum\epsilon_i^2}{n}} \approx 1 + \frac{2\sum\epsilon_i}{n} - \frac{\sum\epsilon_i^2}{n} + \frac{1}{2}\left(\frac{2\sum\epsilon_i}{n}\right)^2$.

$= 1 + \frac{2\sum\epsilon_i}{n} - \frac{\sum\epsilon_i^2}{n} + \frac{2(\sum\epsilon_i)^2}{n^2}$.

$1 - G^2 \approx -\frac{2\sum\epsilon_i}{n} + \frac{\sum\epsilon_i^2}{n} - \frac{2(\sum\epsilon_i)^2}{n^2}$.

With $Q = n$ constraint: $2\sum\epsilon_i + \sum\epsilon_i^2 = 0$, so $\sum\epsilon_i = -\frac{\sum\epsilon_i^2}{2}$ (to leading order).

$1 - G^2 \approx -\frac{2}{n}\cdot(-\frac{\sum\epsilon_i^2}{2}) + \frac{\sum\epsilon_i^2}{n} - \frac{2}{n^2}\cdot\frac{(\sum\epsilon_i^2)^2}{4}$

$= \frac{\sum\epsilon_i^2}{n} + \frac{\sum\epsilon_i^2}{n} - O(\epsilon^4) = \frac{2\sum\epsilon_i^2}{n}$.

$n^2 - S^2 = nQ - S^2 = n\sum\epsilon_i^2 - (\sum\epsilon_i)^2 \approx n\sum\epsilon_i^2$.

Ratio $\approx \frac{2\sum\epsilon_i^2/n}{n\sum\epsilon_i^2} = \frac{2}{n^2}$.

Hmm, so the local ratio near equality is $2/n^2$. But we found configurations giving $1/n$. For $n \geq 3$, $1/n > 2/n^2$. So the maximum is not at the equality point but at the boundary (extreme configurations).

So the supremum is at least $1/n$ (from the $k=n-1$ configuration). Let me check if it can be higher.

Let me reconsider. With $k$ variables $= t$ and $n-k$ variables $= t^{-k/(n-k)}$, the ratio as $t\to\infty$ is $\frac{1}{n(n-k)}$. This is maximized when $n-k = 1$, i.e., $k = n-1$, giving $1/n$.

What about non-symmetric configurations? Let me think about whether $1/n$ is indeed the answer.

Actually, let me reconsider the problem. We need to prove:

$$\frac{Q}{n} - G^2 \leq \frac{1}{n}(nQ - S^2)$$

i.e., $\frac{Q}{n} - G^2 \leq Q - \frac{S^2}{n}$

i.e., $-G^2 \leq Q - \frac{Q}{n} - \frac{S^2}{n} = \frac{(n-1)Q}{n} - \frac{S^2}{n}$

i.e., $G^2 \geq \frac{S^2 - (n-1)Q}{n}$

i.e., $nG^2 \geq S^2 - (n-1)Q$

i.e., $S^2 \leq (n-1)Q + nG^2$.

So we need to prove: $\left(\sum y_i\right)^2 \leq (n-1)\sum y_i^2 + n\left(\prod y_i\right)^{2/n}$.

This is a known inequality! Let me verify it.

$\left(\sum y_i\right)^2 = \sum y_i^2 + 2\sum_{i<j} y_i y_j$.

So we need: $\sum y_i^2 + 2\sum_{i<j} y_i y_j \leq (n-1)\sum y_i^2 + nG^2$

i.e., $2\sum_{i<j} y_i y_j \leq (n-2)\sum y_i^2 + nG^2$.

Hmm, let me think about this differently. Actually, this is related to the inequality:

$(\sum y_i)^2 \leq (n-1)\sum y_i^2 + n(\prod y_i)^{2/n}$

Let me check for $n=2$: $(y_1+y_2)^2 \leq y_1^2 + y_2^2 + 2y_1 y_2$. That's equality! So for $n=2$, $c = 1/2$ and the inequality is tight everywhere (not just at extremes). Wait, that means for $n=2$ the ratio is always exactly $1/2$. Let me verify: we showed ratio $= 1/2$ for all $t$. Yes.

For $n = 3$: We need $(y_1+y_2+y_3)^2 \leq 2(y_1^2+y_2^2+y_3^2) + 3(y_1 y_2 y_3)^{2/3}$.

Let me check with $y_1 = y_2 = t, y_3 = t^{-2}$: LHS $= (2t + t^{-2})^2 = 4t^2 + 4t^{-1} + t^{-4}$. RHS $= 2(2t^2 + t^{-4}) + 3(t^2 \cdot t^{-2})^{2/3} = 4t^2 + 2t^{-4} + 3$.

As $t \to \infty$: LHS $\sim 4t^2$, RHS $\sim 4t^2 + 3$. So RHS > LHS. Good.

Let me check the ratio more carefully for this case. $Q = 2t^2 + t^{-4}$, $S = 2t + t^{-2}$, $G^2 = (t \cdot t \cdot t^{-2})^{2/3} = 1$.

$\frac{Q/n - G^2}{nQ - S^2} = \frac{(2t^2+t^{-4})/3 - 1}{3(2t^2+t^{-4}) - (2t+t^{-2})^2}$

$= \frac{2t^2/3 + t^{-4}/3 - 1}{6t^2 + 3t^{-4} - 4t^2 - 4t^{-1} - t^{-4}}$

$= \frac{2t^2/3 - 1 + O(t^{-4})}{2t^2 - 4t^{-1} + 2t^{-4}}$

$\to \frac{2/3}{2} = \frac{1}{3}$ as $t \to \infty$.

So the ratio approaches $1/3 = 1/n$. Good.

Now I need to prove the inequality $(\sum y_i)^2 \leq (n-1)\sum y_i^2 + n(\prod y_i)^{2/n}$ and show that $1/n$ is sharp.

Let me search my memory for this inequality. This looks like it could be related to Cartwright-Field or some refinement of AM-GM.

Actually, let me think about it. We can write:

$(\sum y_i)^2 - (n-1)\sum y_i^2 = \sum y_i^2 + 2\sum_{i<j} y_i y_j - (n-1)\sum y_i^2 = 2\sum_{i<j} y_i y_j - (n-2)\sum y_i^2$.

So we need: $2\sum_{i<j} y_i y_j - (n-2)\sum y_i^2 \leq n G^2$.

Hmm, this is not obviously a standard inequality. Let me try another approach.

Alternative: Let's use the substitution $y_i = G \cdot z_i$ where $\prod z_i = 1$. Then we need $(\sum z_i)^2 \leq (n-1)\sum z_i^2 + n$, with $\prod z_i = 1$.

So we need to prove: for $z_i > 0$ with $\prod z_i = 1$,
$$(\sum z_i)^2 \leq (n-1)\sum z_i^2 + n.$$

Equivalently, $\sum z_i^2 + 2\sum_{i<j} z_i z_j \leq (n-1)\sum z_i^2 + n$, i.e., $2\sum_{i<j} z_i z_j \leq (n-2)\sum z_i^2 + n$.

Hmm. Let me try $n=3$: $2(z_1 z_2 + z_1 z_3 + z_2 z_3) \leq z_1^2 + z_2^2 + z_3^2 + 3$ with $z_1 z_2 z_3 = 1$.

By AM-GM, $z_1 z_2 + z_1 z_3 + z_2 z_3 \geq 3(z_1 z_2 z_3)^{2/3} = 3$. And $z_1^2 + z_2^2 + z_3^2 \geq 3(z_1 z_2 z_3)^{2/3} = 3$.

So we need $2\sum z_i z_j \leq \sum z_i^2 + 3$. 

Let $a = z_1 z_2, b = z_1 z_3, c = z_2 z_3$. Then $abc = (z_1 z_2 z_3)^2 = 1$ and $z_1^2 = ab/c$, etc.

$2(a+b+c) \leq ab/c + bc/a + ca/b + 3$.

With $abc = 1$, $ab/c = a^2 b^2$, $bc/a = b^2 c^2$, $ca/b = c^2 a^2$. And $a + b + c \geq 3$.

Hmm, this is getting complicated. Let me try a different approach.

Actually, I recall that the inequality $(\sum y_i)^2 \leq (n-1)\sum y_i^2 + n(\prod y_i)^{2/n}$ is known. Let me try to prove it using a clever method.

**Approach via Lagrange multipliers / optimization:**

We want to show that $f(y) = (\sum y_i)^2 - (n-1)\sum y_i^2 - n(\prod y_i)^{2/n} \leq 0$ for all $y_i > 0$.

Since $f$ is homogeneous of degree 2, we can normalize $\prod y_i = 1$. Then $f(y) = (\sum y_i)^2 - (n-1)\sum y_i^2 - n$.

We want to show $(\sum y_i)^2 \leq (n-1)\sum y_i^2 + n$ when $\prod y_i = 1$.

Equivalently, $2\sum_{i<j} y_i y_j \leq (n-2)\sum y_i^2 + n$.

Let $P = \sum_{i<j} y_i y_j$ and $Q = \sum y_i^2$. We need $2P \leq (n-2)Q + n$.

Note $P = \frac{(\sum y_i)^2 - Q}{2}$, so this is $(\sum y_i)^2 - Q \leq (n-2)Q + n$, i.e., $(\sum y_i)^2 \leq (n-1)Q + n$. Circular.

Let me try to use the method of Lagrange multipliers. Maximize $g(y) = (\sum y_i)^2 - (n-1)\sum y_i^2$ subject to $\prod y_i = 1$.

$\frac{\partial g}{\partial y_k} = 2\sum y_i - 2(n-1)y_k = \lambda \frac{1}{y_k} \cdot \prod y_i = \lambda / y_k$ (since $\prod y_i = 1$).

So $y_k(2S - 2(n-1)y_k) = \lambda$ for all $k$, where $S = \sum y_i$.

$2S y_k - 2(n-1)y_k^2 = \lambda$.

This is a quadratic in $y_k$: $2(n-1)y_k^2 - 2S y_k + \lambda = 0$.

So each $y_k$ is a root of $2(n-1)t^2 - 2St + \lambda = 0$. This quadratic has at most 2 roots, so at a critical point, the $y_i$ take at most 2 distinct values.

Say $a$ appears $k$ times and $b$ appears $n-k$ times, with $a^k b^{n-k} = 1$.

$S = ka + (n-k)b$, $Q = ka^2 + (n-k)b^2$.

$g = S^2 - (n-1)Q = (ka+(n-k)b)^2 - (n-1)(ka^2+(n-k)b^2)$.

$= k^2 a^2 + 2k(n-k)ab + (n-k)^2 b^2 - (n-1)ka^2 - (n-1)(n-k)b^2$

$= k(k-(n-1))a^2 + 2k(n-k)ab + (n-k)(n-k-(n-1))b^2$

$= k(k-n+1)a^2 + 2k(n-k)ab + (n-k)(1-k)b^2$

$= k(k-n+1)a^2 + 2k(n-k)ab - (n-k)(k-1)b^2$.

We want to show $g \leq n$ (since $f = g - n \leq 0$).

With $a^k b^{n-k} = 1$, let $b = a^{-k/(n-k)}$. As $a \to \infty$:

If $k < n$: $b \to 0$. $g \approx k(k-n+1)a^2 + 2k(n-k)a \cdot a^{-k/(n-k)} - ...$

The leading term is $k(k-n+1)a^2$ if $k > n-1$... wait, $k \leq n-1$ since $k < n$ and $k \geq 1$.

If $k \leq n-2$: $k - n + 1 \leq -1 < 0$, so $k(k-n+1) < 0$, and $g \to -\infty$. Not a maximum.

If $k = n-1$: $k(k-n+1) = (n-1)(0) = 0$. So the $a^2$ term vanishes!

$g = 0 \cdot a^2 + 2(n-1) \cdot 1 \cdot ab - 1 \cdot (n-2) b^2 = 2(n-1)ab - (n-2)b^2$.

With $b = a^{-(n-1)}$: $g = 2(n-1)a \cdot a^{-(n-1)} - (n-2)a^{-2(n-1)} = 2(n-1)a^{-(n-2)} - (n-2)a^{-2(n-1)}$.

As $a \to \infty$: $g \to 0$ (for $n \geq 3$). As $a \to 0^+$: $b \to \infty$, $g = 2(n-1)ab - (n-2)b^2 \approx -(n-2)b^2 \to -\infty$.

So for $k = n-1$, $g$ achieves a maximum at some finite $a$. Let me find it.

$g = 2(n-1)ab - (n-2)b^2$ where $a^{n-1}b = 1$, so $b = a^{-(n-1)}$.

$g(a) = 2(n-1)a^{-(n-2)} - (n-2)a^{-2(n-1)}$.

$g'(a) = -2(n-1)(n-2)a^{-(n-1)} + 2(n-1)^2(n-2)a^{-2n+1}$

$= 2(n-1)(n-2)[-a^{-(n-1)} + (n-1)a^{-2n+1}]$

$= 2(n-1)(n-2)a^{-(n-1)}[-1 + (n-1)a^{-n}]$.

Setting $g'(a) = 0$: $(n-1)a^{-n} = 1$, so $a = (n-1)^{1/n}$.

Then $b = a^{-(n-1)} = (n-1)^{-(n-1)/n}$.

$g_{\max} = 2(n-1) \cdot (n-1)^{1/n} \cdot (n-1)^{-(n-1)/n} - (n-2)(n-1)^{-2(n-1)/n}$

$= 2(n-1) \cdot (n-1)^{1/n - (n-1)/n} - (n-2)(n-1)^{-2(n-1)/n}$

$1/n - (n-1)/n = (1 - n + 1)/n = (2-n)/n$.

$= 2(n-1) \cdot (n-1)^{(2-n)/n} - (n-2)(n-1)^{-2(n-1)/n}$

$= 2(n-1)^{1 + (2-n)/n} - (n-2)(n-1)^{-2(n-1)/n}$

$1 + (2-n)/n = (n + 2 - n)/n = 2/n$.

$= 2(n-1)^{2/n} - (n-2)(n-1)^{-2(n-1)/n}$.

Note $-2(n-1)/n = -2 + 2/n$, so $(n-1)^{-2(n-1)/n} = (n-1)^{-2+2/n} = (n-1)^{2/n}/(n-1)^2$.

$g_{\max} = 2(n-1)^{2/n} - (n-2)\frac{(n-1)^{2/n}}{(n-1)^2} = (n-1)^{2/n}\left[2 - \frac{n-2}{(n-1)^2}\right]$

$= (n-1)^{2/n} \cdot \frac{2(n-1)^2 - (n-2)}{(n-1)^2} = (n-1)^{2/n} \cdot \frac{2n^2 - 4n + 2 - n + 2}{(n-1)^2}$

$= (n-1)^{2/n} \cdot \frac{2n^2 - 5n + 4}{(n-1)^2}$.

Hmm, let me factor $2n^2 - 5n + 4$. Discriminant: $25 - 32 = -7 < 0$. So it doesn't factor nicely. For $n=3$: $18 - 15 + 4 = 7$. $g_{\max} = 2^{2/3} \cdot 7/4 = 7 \cdot 2^{2/3}/4 = 7 \cdot 2^{-4/3}$.

$7 \cdot 2^{-4/3} \approx 7 / 2.52 \approx 2.78$. And we need $g \leq n = 3$. So $2.78 \leq 3$. ✓

But wait, we also need to check the case $k = 1$ (one variable is $a$, $n-1$ are $b$). By symmetry of the problem (we can relabel), this is the same as $k = n-1$ with $a$ and $b$ swapped. So the maximum is the same.

Actually wait, I need to be more careful. The case $k=1$ means 1 variable equals $a$ and $n-1$ equal $b$. The formula gives:

$g = 1 \cdot (1 - n + 1) a^2 + 2 \cdot 1 \cdot (n-1) ab - (n-1)(1-1)b^2 = (2-n)a^2 + 2(n-1)ab$.

With $ab^{n-1} = 1$, $a = b^{-(n-1)}$.

$g = (2-n)b^{-2(n-1)} + 2(n-1)b^{-(n-1)} \cdot b = (2-n)b^{-2(n-1)} + 2(n-1)b^{-(n-2)}$.

As $b \to \infty$: $g \to 0$ (for $n \geq 3$). As $b \to 0$: $g \to -\infty$ (since $(2-n) < 0$ and $b^{-2(n-1)} \to \infty$).

$g'(b) = (2-n)(-2(n-1))b^{-2n+1} + 2(n-1)(-(n-2))b^{-(n-1)}$

$= -2(n-1)(2-n)b^{-2n+1} - 2(n-1)(n-2)b^{-(n-1)}$

$= 2(n-1)(n-2)b^{-2n+1} - 2(n-1)(n-2)b^{-(n-1)}$

$= 2(n-1)(n-2)b^{-(n-1)}[b^{-(n-1)} - 1] \cdot b^{?}$

Hmm, let me redo: $b^{-2n+1} = b^{-(n-1)} \cdot b^{-n}$. So:

$g'(b) = 2(n-1)(n-2)b^{-(n-1)}[b^{-n} - 1]$.

Wait: $2(n-1)(n-2)b^{-2n+1} - 2(n-1)(n-2)b^{-(n-1)} = 2(n-1)(n-2)[b^{-2n+1} - b^{-(n-1)}] = 2(n-1)(n-2)b^{-(n-1)}[b^{-n} - 1]$.

Setting to 0: $b^{-n} = 1$, so $b = 1$. Then $a = 1$, and $g = 0$. That's the minimum (all equal), not a maximum.

Hmm, so for $k=1$, the only critical point is $b=1$ (all equal) which gives $g=0$. The function goes to $-\infty$ as $b \to 0$ and to $0$ as $b \to \infty$. So the supremum is $0$ (approached but not achieved), which is less than $n$.

Wait, but we also need to check: is there a maximum for $k=1$? The function starts at $-\infty$, increases to $0$ at $b=1$, then... let me check the sign of $g'$ for $b > 1$: $b^{-n} - 1 < 0$, so $g' < 0$. So $g$ is decreasing for $b > 1$. And for $b < 1$: $b^{-n} - 1 > 0$, so $g' > 0$, $g$ is increasing. So $b=1$ is the global maximum with $g = 0$.

So for $k=1$, $g \leq 0 < n$. Not interesting.

For $k = n-1$, we found $g_{\max} = (n-1)^{2/n} \cdot \frac{2n^2-5n+4}{(n-1)^2}$.

For $n=3$: $g_{\max} = 2^{2/3} \cdot 7/4 \approx 2.777...$. We need this $\leq 3$. ✓

But is this the global maximum over all configurations? We need to check all possible $k$ from 1 to $n-1$.

For $2 \leq k \leq n-2$ (when $n \geq 4$): the leading coefficient $k(k-n+1) < 0$ (since $k < n-1$), so as $a \to \infty$ or $a \to 0$, $g \to -\infty$. There could be a local maximum.

Actually, I realize this analysis is getting complicated. Let me think about whether there's a cleaner proof.

Let me reconsider. We want to prove:

$$(\sum y_i)^2 \leq (n-1)\sum y_i^2 + n(\prod y_i)^{2/n}.$$

This is equivalent to: the maximum of $(\sum y_i)^2 - (n-1)\sum y_i^2$ subject to $\prod y_i = 1$ is at most $n$.

Let me try a different approach. Consider the function $h(t) = (\sum y_i)^2 - (n-1)\sum y_i^2$ where we set $y_i = e^{t_i}$ with $\sum t_i = 0$ (so $\prod y_i = 1$).

Actually, let me try yet another approach. I'll try to prove the inequality directly.

**Claim:** For $y_1, \ldots, y_n > 0$,
$$(\sum_{i=1}^n y_i)^2 \leq (n-1)\sum_{i=1}^n y_i^2 + n\left(\prod_{i=1}^n y_i\right)^{2/n}.$$

**Proof attempt using Schur-like or Muirhead-like reasoning:**

WLOG $\prod y_i = 1$ (by homogeneity). We need $(\sum y_i)^2 \leq (n-1)\sum y_i^2 + n$.

$\sum y_i^2 + 2\sum_{i<j} y_i y_j \leq (n-1)\sum y_i^2 + n$

$2\sum_{i<j} y_i y_j \leq (n-2)\sum y_i^2 + n$.

Now, by AM-GM, $\sum_{i<j} y_i y_j \geq \binom{n}{2} (\prod y_i)^{2(n-1)/n \cdot 1/\binom{n}{2}}$... hmm, this isn't straightforward.

Let me try the approach of fixing all but two variables and using convexity.

Actually, let me try a completely different approach. Let me use the Cauchy-Schwarz inequality in a clever way.

By Cauchy-Schwarz: $(\sum y_i)^2 \leq n \sum y_i^2$. But that gives $(\sum y_i)^2 \leq n \sum y_i^2$, which is weaker than what we need (we need $(n-1)\sum y_i^2 + nG^2$, and $nG^2 \leq \sum y_i^2$ by AM-GM, so $(n-1)\sum y_i^2 + nG^2 \leq n\sum y_i^2$). So our inequality is stronger than Cauchy-Schwarz.

Let me think about this more carefully. 

**Key idea:** Maybe use the identity/inequality involving power means.

Actually, let me try to prove it by induction on $n$.

Base case $n = 2$: $(y_1 + y_2)^2 = y_1^2 + y_2^2 + 2y_1 y_2 = (2-1)(y_1^2 + y_2^2) + 2(y_1 y_2)^{2/2}$. Equality! ✓

Inductive step: Assume the inequality holds for $n-1$. We want to prove for $n$.

Hmm, induction seems tricky because of the geometric mean term.

Let me try another approach. Consider the inequality as a function of one variable, fixing the rest.

Fix $y_2, \ldots, y_n$ and let $t = y_1$. We need:

$(t + S')^2 \leq (n-1)(t^2 + Q') + n(t \cdot P')^{2/n}$

where $S' = \sum_{i=2}^n y_i$, $Q' = \sum_{i=2}^n y_i^2$, $P' = \prod_{i=2}^n y_i$.

$t^2 + 2tS' + S'^2 \leq (n-1)t^2 + (n-1)Q' + n(tP')^{2/n}$

$2tS' + S'^2 - (n-2)t^2 - (n-1)Q' \leq n t^{2/n} P'^{2/n}$

This is a function of $t$ that we need to show is $\leq 0$ for all $t > 0$. The LHS is a quadratic in $t$ (opening downward since $-(n-2) < 0$ for $n \geq 3$), and the RHS is $t^{2/n}$ times a constant. This doesn't simplify nicely.

Let me try a substitution. Set $y_i = G \cdot u_i$ where $\prod u_i = 1$ and $G = (\prod y_i)^{1/n}$. Then we need $(\sum u_i)^2 \leq (n-1)\sum u_i^2 + n$ with $\prod u_i = 1$.

Let $u_i = e^{z_i}$ with $\sum z_i = 0$. Then we need:

$(\sum e^{z_i})^2 \leq (n-1)\sum e^{2z_i} + n$.

Let $f(z) = (n-1)\sum e^{2z_i} + n - (\sum e^{z_i})^2$. We need $f \geq 0$ when $\sum z_i = 0$.

$f = (n-1)\sum e^{2z_i} + n - \sum e^{2z_i} - 2\sum_{i<j} e^{z_i+z_j} = (n-2)\sum e^{2z_i} + n - 2\sum_{i<j} e^{z_i+z_j}$.

Since $\sum z_i = 0$, $z_i + z_j = -(z_k + z_l + ...)$ for the remaining indices. Not sure this helps directly.

Let me try the tangent line trick. The function $e^{2z}$ is convex, and $e^{z_i + z_j}$... 

Actually, let me try a specific approach. Note that $e^{z_i+z_j} = e^{z_i} e^{z_j}$. And $\sum_{i<j} e^{z_i+z_j} = \frac{(\sum e^{z_i})^2 - \sum e^{2z_i}}{2}$.

So $f = (n-2)\sum e^{2z_i} + n - (\sum e^{z_i})^2 + \sum e^{2z_i} = (n-1)\sum e^{2z_i} + n - (\sum e^{z_i})^2$.

That's circular again.

OK let me try to prove the inequality $(\sum y_i)^2 \leq (n-1)\sum y_i^2 + nG^2$ using the SOS (sum of squares) or Schur inequality approach.

Actually, I just realized: this might be a known result. Let me think about what it's called.

The inequality $nG^2 + (n-1)Q \geq S^2$ where $G$ is the geometric mean, $Q = \sum y_i^2$, $S = \sum y_i$.

This can be rewritten as: $nG^2 \geq S^2 - (n-1)Q = 2\sum_{i<j} y_i y_j - (n-2)Q$.

Hmm, let me try the case $n = 3$ explicitly. We need $3(y_1 y_2 y_3)^{2/3} \geq 2(y_1 y_2 + y_1 y_3 + y_2 y_3) - (y_1^2 + y_2^2 + y_3^2)$.

I.e., $y_1^2 + y_2^2 + y_3^2 + 3(y_1 y_2 y_3)^{2/3} \geq 2(y_1 y_2 + y_1 y_3 + y_2 y_3)$.

Let $a = y_1^{2/3}, b = y_2^{2/3}, c = y_3^{2/3}$. Then $y_i = a_i^{3/2}$... this doesn't simplify.

Let $p = (y_1 y_2 y_3)^{1/3}$. Set $y_i = p \cdot u_i$ with $u_1 u_2 u_3 = 1$. Need $u_1^2 + u_2^2 + u_3^2 + 3 \geq 2(u_1 u_2 + u_1 u_3 + u_2 u_3)$.

$(u_1 - u_2)^2 + (u_1 - u_3)^2 + (u_2 - u_3)^2 = 2(u_1^2 + u_2^2 + u_3^2) - 2(u_1 u_2 + u_1 u_3 + u_2 u_3)$.

So $u_1^2 + u_2^2 + u_3^2 - (u_1 u_2 + u_1 u_3 + u_2 u_3) = \frac{1}{2}\sum(u_i - u_j)^2$.

We need $u_1^2 + u_2^2 + u_3^2 + 3 \geq 2(u_1 u_2 + u_1 u_3 + u_2 u_3)$, i.e., $u_1^2 + u_2^2 + u_3^2 - 2(u_1 u_2 + u_1 u_3 + u_2 u_3) + 3 \geq 0$.

$(u_1^2 + u_2^2 + u_3^2 - u_1 u_2 - u_1 u_3 - u_2 u_3) - (u_1 u_2 + u_1 u_3 + u_2 u_3) + 3 \geq 0$.

$\frac{1}{2}\sum(u_i - u_j)^2 - (u_1 u_2 + u_1 u_3 + u_2 u_3) + 3 \geq 0$.

By AM-GM, $u_1 u_2 + u_1 u_3 + u_2 u_3 \geq 3(u_1 u_2 u_3)^{2/3} = 3$.

So $-(u_1 u_2 + u_1 u_3 + u_2 u_3) + 3 \leq 0$. And $\frac{1}{2}\sum(u_i - u_j)^2 \geq 0$. So we need the first term to dominate.

This doesn't directly work. Let me try a different decomposition.

$u_1^2 + u_2^2 + u_3^2 + 3 - 2(u_1 u_2 + u_1 u_3 + u_2 u_3) = (u_1^2 - 2u_1 u_2 + u_2^2) + (u_3^2 - 2u_3(u_1+u_2) + ... )$

Hmm, let me just try: $= (u_1 + u_2 + u_3)^2 - 4(u_1 u_2 + u_1 u_3 + u_2 u_3) + 3 = ...$. No, $(u_1+u_2+u_3)^2 = u_1^2+u_2^2+u_3^2 + 2(u_1u_2+u_1u_3+u_2u_3)$. So $u_1^2+u_2^2+u_3^2 - 2(u_1u_2+u_1u_3+u_2u_3) = (u_1+u_2+u_3)^2 - 4(u_1u_2+u_1u_3+u_2u_3)$.

Need $(u_1+u_2+u_3)^2 - 4(u_1u_2+u_1u_3+u_2u_3) + 3 \geq 0$ with $u_1 u_2 u_3 = 1$.

Let $s = u_1+u_2+u_3, p = u_1u_2+u_1u_3+u_2u_3, q = u_1u_2u_3 = 1$. Need $s^2 - 4p + 3 \geq 0$.

By Newton's inequalities / Maclaurin: $s^2 \geq 3p$ and $p^2 \geq 3sq = 3s$ (Maclaurin's inequality: $s/3 \geq (p/3)^{1/2} \geq q^{1/3} = 1$, so $p \leq s^2/3$ and $s \geq 3$).

From $p \leq s^2/3$: $s^2 - 4p + 3 \geq s^2 - 4s^2/3 + 3 = -s^2/3 + 3$. This is $\geq 0$ iff $s \leq 3$. But $s \geq 3$, so this only works at $s = 3$.

From $p^2 \geq 3s$: $p \geq \sqrt{3s}$. So $s^2 - 4p + 3 \leq s^2 - 4\sqrt{3s} + 3$. For large $s$, this is positive. But we need a lower bound, not upper.

Hmm, this approach isn't working cleanly for $n=3$. Let me try to use Schur's inequality.

Schur's inequality (for $t = 1$): $u_1(u_1-u_2)(u_1-u_3) + u_2(u_2-u_1)(u_2-u_3) + u_3(u_3-u_1)(u_3-u_2) \geq 0$.

This expands to $u_1^3 + u_2^3 + u_3^3 + u_1 u_2 u_3 \geq u_1^2 u_2 + u_1^2 u_3 + u_2^2 u_1 + u_2^2 u_3 + u_3^2 u_1 + u_3^2 u_2$... actually Schur says $\sum u_i^t(u_i - u_j)(u_i - u_k) \geq 0$ which for $t=1$ gives $\sum u_i^3 + 3u_1u_2u_3 \geq \sum_{sym} u_i^2 u_j$.

Not sure this directly helps.

Let me try a completely different strategy. Maybe I should look for the inequality in the literature or prove it using a known technique.

**Approach: Tangent line trick with convexity.**

We want to show $f(z) = (n-1)\sum e^{2z_i} + n - (\sum e^{z_i})^2 \geq 0$ when $\sum z_i = 0$.

Consider the function $\phi(t) = (n-1)e^{2t} + 1 - (n-1)e^{2t} - ...$. Hmm, this isn't leading anywhere nice.

Let me try yet another approach. 

**Approach: Reduce to two variables using mixing.**

The idea: show that the maximum of $g = (\sum y_i)^2 - (n-1)\sum y_i^2$ subject to $\prod y_i = 1$ is achieved when $n-1$ variables are equal and one is different. Then we computed this maximum and need to show it's $\leq n$.

We showed that at any critical point, the variables take at most 2 distinct values. So we need to check all cases: $k$ variables equal to $a$ and $n-k$ equal to $b$, with $a^k b^{n-k} = 1$.

For $k = n-1$ (or $k = 1$ by symmetry), we computed $g_{\max}$.

For $2 \leq k \leq n-2$, we need to check that the maximum is also $\leq n$.

Actually, let me reconsider. The function $g$ is continuous on the set $\{y: \prod y_i = 1, y_i > 0\}$, which is not compact. But $g \to -\infty$ as any $y_i \to 0$ or $\infty$ (when $n \geq 3$ and we're not in the $k=n-1$ or $k=1$ case). Wait, actually for $k = n-1$, we showed $g \to 0$ as $a \to \infty$, not $-\infty$. So the supremum might not be achieved.

Hmm, let me reconsider the boundary behavior more carefully.

For general $k$ (with $a \to \infty$, $b = a^{-k/(n-k)} \to 0$):

$g = k(k-n+1)a^2 + 2k(n-k)ab - (n-k)(k-1)b^2$.

As $a \to \infty$: 
- If $k = n-1$: $k(k-n+1) = 0$, and $ab = a \cdot a^{-(n-1)/(1)} = a^{1-(n-1)} = a^{-(n-2)} \to 0$ (for $n \geq 3$). And $b^2 = a^{-2(n-1)} \to 0$. So $g \to 0$.
- If $k \leq n-2$: $k(k-n+1) < 0$, so $g \to -\infty$.

As $a \to 0$ (so $b \to \infty$):
- $g \approx -(n-k)(k-1)b^2$. If $k \geq 2$, this is $\to -\infty$. If $k = 1$, $g \approx 0 + 2(n-1)ab \to 0$... wait, $k=1$: $g = (2-n)a^2 + 2(n-1)ab - 0 = (2-n)a^2 + 2(n-1)ab$. As $a \to 0, b \to \infty$: $ab = a \cdot a^{-1/(n-1)} = a^{(n-2)/(n-1)} \to 0$. And $a^2 \to 0$. So $g \to 0$.

So for $k=1$ and $k=n-1$, $g \to 0$ at the boundary, and the maximum is achieved at an interior point.
For $2 \leq k \leq n-2$, $g \to -\infty$ at both boundaries, so the maximum is achieved at an interior critical point.

By the Lagrange multiplier analysis, interior critical points have at most 2 distinct values. So we need to find the maximum of $g$ over all $(k, a)$ with $1 \leq k \leq n-1$.

For $k = 1$: we showed the only critical point is $a = b = 1$ (all equal), $g = 0$. And $g \to 0$ at boundary. So $\sup g = 0$ (achieved at the limit, or at all-equal). Actually wait, is $g$ always $\leq 0$ for $k=1$? We showed $g$ increases to $0$ at $b=1$ then decreases. So yes, $g \leq 0$ for $k = 1$.

For $k = n-1$: by symmetry (swap $a \leftrightarrow b$, $k \leftrightarrow n-k$), this is the same as $k=1$ with roles reversed. Wait, no. $k = n-1$ means $n-1$ variables are $a$ and 1 is $b$. This is different from $k = 1$.

Let me recompute for $k = n-1$. We have $n-1$ variables $= a$ and 1 variable $= b = a^{-(n-1)}$.

$g = (n-1)((n-1) - (n-1))a^2 + ... $. Wait, let me use the formula:

$g = k(k-n+1)a^2 + 2k(n-k)ab - (n-k)(k-1)b^2$ with $k = n-1$:

$= (n-1)(n-1-n+1)a^2 + 2(n-1)(1)ab - (1)(n-2)b^2$

$= (n-1)(0)a^2 + 2(n-1)ab - (n-2)b^2$

$= 2(n-1)ab - (n-2)b^2$.

With $b = a^{-(n-1)}$:

$g(a) = 2(n-1)a^{-(n-2)} - (n-2)a^{-2(n-1)}$.

We found the maximum at $a = (n-1)^{1/n}$, giving:

$g_{\max} = (n-1)^{2/n} \cdot \frac{2n^2 - 5n + 4}{(n-1)^2}$.

We need to show this is $\leq n$.

For $n = 3$: $g_{\max} = 2^{2/3} \cdot 7/4 \approx 2.777 \leq 3$. ✓

For $n = 4$: $g_{\max} = 3^{1/2} \cdot (32-20+4)/9 = \sqrt{3} \cdot 16/9 \approx 1.732 \cdot 1.778 \approx 3.079$. Is this $\leq 4$? Yes. ✓

For large $n$: $(n-1)^{2/n} \to 1$, and $\frac{2n^2-5n+4}{(n-1)^2} \to 2$. So $g_{\max} \to 2 < n$. ✓

So for all $n \geq 3$, $g_{\max} < n$. But wait, I also need to check the cases $2 \leq k \leq n-2$ for $n \geq 4$.

For $2 \leq k \leq n-2$, the maximum is at an interior critical point. Let me compute it.

$g = k(k-n+1)a^2 + 2k(n-k)ab - (n-k)(k-1)b^2$ with $a^k b^{n-k} = 1$, so $b = a^{-k/(n-k)}$.

$g(a) = k(k-n+1)a^2 + 2k(n-k)a^{1-k/(n-k)} \cdot a^{k/(n-k)} ... $

Wait, $ab = a \cdot a^{-k/(n-k)} = a^{1 - k/(n-k)} = a^{(n-2k)/(n-k)}$.

$b^2 = a^{-2k/(n-k)}$.

$g(a) = k(k-n+1)a^2 + 2k(n-k)a^{(n-2k)/(n-k)} - (n-k)(k-1)a^{-2k/(n-k)}$.

$g'(a) = 2k(k-n+1)a + 2k(n-k)\frac{n-2k}{n-k}a^{(n-2k)/(n-k)-1} + (n-k)(k-1)\frac{2k}{n-k}a^{-2k/(n-k)-1}$

$= 2k(k-n+1)a + 2k(n-2k)a^{(2k-n+n-2k)/(n-k)} \cdot ... $

Hmm, let me be more careful. $\frac{d}{da}a^{(n-2k)/(n-k)} = \frac{n-2k}{n-k} a^{(n-2k)/(n-k) - 1} = \frac{n-2k}{n-k} a^{(2k-n)/(n-k) \cdot (-1) + ...}$

Actually $(n-2k)/(n-k) - 1 = (n-2k-(n-k))/(n-k) = -k/(n-k)$.

So $g'(a) = 2k(k-n+1)a + 2k(n-2k) \cdot a^{-k/(n-k)} + 2k(k-1) a^{-2k/(n-k)-1}$.

Hmm wait, let me redo the last term. $\frac{d}{da}[-(n-k)(k-1)a^{-2k/(n-k)}] = -(n-k)(k-1) \cdot \frac{-2k}{n-k} a^{-2k/(n-k)-1} = 2k(k-1) a^{-2k/(n-k)-1}$.

And $-2k/(n-k) - 1 = (-2k - n + k)/(n-k) = (-k-n)/(n-k) = -(n+k)/(n-k)$.

So $g'(a) = 2k(k-n+1)a + 2k(n-2k) a^{-k/(n-k)} + 2k(k-1) a^{-(n+k)/(n-k)}$.

Setting $g'(a) = 0$ and dividing by $2k$:

$(k-n+1)a + (n-2k) a^{-k/(n-k)} + (k-1) a^{-(n+k)/(n-k)} = 0$.

Multiply by $a^{(n+k)/(n-k)}$ (which is positive):

$(k-n+1) a^{1+(n+k)/(n-k)} + (n-2k) a^{(n+k)/(n-k) - k/(n-k)} + (k-1) = 0$.

$1 + (n+k)/(n-k) = (n-k+n+k)/(n-k) = 2n/(n-k)$.

$(n+k)/(n-k) - k/(n-k) = n/(n-k)$.

So: $(k-n+1) a^{2n/(n-k)} + (n-2k) a^{n/(n-k)} + (k-1) = 0$.

Let $w = a^{n/(n-k)}$ (so $w > 0$):

$(k-n+1) w^2 + (n-2k) w + (k-1) = 0$.

Note $k - n + 1 = -(n-k-1)$, so:

$-(n-k-1) w^2 + (n-2k) w + (k-1) = 0$.

$(n-k-1) w^2 - (n-2k) w - (k-1) = 0$.

Discriminant: $(n-2k)^2 + 4(n-k-1)(k-1)$.

$= n^2 - 4nk + 4k^2 + 4(nk - n - k^2 + k + k - 1)$

Hmm, let me expand $4(n-k-1)(k-1) = 4(nk - n - k^2 + k - k + 1) = 4(nk - n - k^2 + 1)$.

$= 4nk - 4n - 4k^2 + 4$.

Total: $n^2 - 4nk + 4k^2 + 4nk - 4n - 4k^2 + 4 = n^2 - 4n + 4 = (n-2)^2$.

So discriminant $= (n-2)^2$, and $w = \frac{(n-2k) \pm (n-2)}{2(n-k-1)}$.

$w_1 = \frac{n-2k+n-2}{2(n-k-1)} = \frac{2n-2k-2}{2(n-k-1)} = \frac{2(n-k-1)}{2(n-k-1)} = 1$.

$w_2 = \frac{n-2k-(n-2)}{2(n-k-1)} = \frac{-2k+2}{2(n-k-1)} = \frac{-(k-1)}{n-k-1}$.

Since $k \geq 2$, $k - 1 \geq 1 > 0$, and $n - k - 1 \geq 1 > 0$ (since $k \leq n-2$), so $w_2 < 0$. Not valid since $w > 0$.

So the only critical point is $w = 1$, i.e., $a^{n/(n-k)} = 1$, i.e., $a = 1$, which means $b = 1$ (all equal), and $g = 0$.

So for $2 \leq k \leq n-2$, the only interior critical point is all-equal with $g = 0$, and $g \to -\infty$ at the boundary. So $g \leq 0$ in these cases.

For $k = 1$: $g \leq 0$ (shown above).
For $k = n-1$: $g$ achieves a positive maximum $g_{\max}$.

So the global maximum of $g$ over all configurations is $g_{\max}$ (from $k = n-1$), and we need to show $g_{\max} \leq n$.

Wait, but I should also check: is the maximum for $k = n-1$ really the global max? What about non-critical-point configurations? Since $g$ is continuous and goes to $0$ or $-\infty$ at the boundary, and the only interior critical points give $g = 0$ (for $k \neq n-1, 1$) or $g_{\max}$ (for $k = n-1$) or $g \leq 0$ (for $k = 1$), the global supremum is $\max(0, g_{\max}) = g_{\max}$ (assuming $g_{\max} > 0$).

Actually, I need to be more careful. The Lagrange multiplier analysis shows that at any critical point, the variables take at most 2 values. But the set $\{y: \prod y_i = 1\}$ is not compact, so the maximum might not be achieved. However, we showed that $g \to 0$ or $-\infty$ at the boundary, so if $g_{\max} > 0$, the maximum is achieved at an interior point, which must be a critical point, which must have at most 2 distinct values.

So the global maximum is indeed $g_{\max}$ from the $k = n-1$ case (or $k = 1$ by symmetry, but we showed $k = 1$ gives $g \leq 0$).

Wait, $k = 1$ and $k = n-1$ are different cases. $k = n-1$ means $n-1$ variables are equal (to $a$) and 1 is different (to $b$). $k = 1$ means 1 variable is $a$ and $n-1$ are $b$. These are actually the same up to relabeling $a \leftrightarrow b$! So why did we get different results?

For $k = 1$: $g = (2-n)a^2 + 2(n-1)ab$, with $ab^{n-1} = 1$, $a = b^{-(n-1)}$.
$g = (2-n)b^{-2(n-1)} + 2(n-1)b^{-(n-2)}$.

For $k = n-1$: $g = 2(n-1)ab - (n-2)b^2$, with $a^{n-1}b = 1$, $b = a^{-(n-1)}$.
$g = 2(n-1)a^{-(n-2)} - (n-2)a^{-2(n-1)}$.

These are the same function with $a$ and $b$ swapped! In the $k=1$ case, the "single" variable is $a = b^{-(n-1)}$ and the "repeated" variable is $b$. In the $k = n-1$ case, the "repeated" variable is $a$ and the "single" variable is $b = a^{-(n-1)}$.

So if we let $t$ be the repeated variable and $s$ be the single variable (with $t^{n-1} s = 1$), then:

$g = 2(n-1)ts - (n-2)s^2$ (from $k = n-1$ with $a = t, b = s$).

Or from $k = 1$ with $b = t, a = s$: $g = (2-n)s^2 + 2(n-1)st = 2(n-1)st - (n-2)s^2$. Same thing!

So they're the same. The discrepancy in my earlier analysis was that for $k = 1$, I was parameterizing by $b$ (the repeated variable) and found the critical point at $b = 1$. But let me recheck.

For $k = 1$: $g(b) = (2-n)b^{-2(n-1)} + 2(n-1)b^{-(n-2)}$.

$g'(b) = (2-n)(-2(n-1))b^{-2n+1} + 2(n-1)(-(n-2))b^{-(n-1)}$

$= 2(n-1)(n-2)b^{-2n+1} - 2(n-1)(n-2)b^{-(n-1)}$

$= 2(n-1)(n-2)[b^{-2n+1} - b^{-(n-1)}]$

$= 2(n-1)(n-2)b^{-(n-1)}[b^{-n} - 1]$.

Critical point: $b^{-n} = 1 \Rightarrow b = 1$. But wait, I need to check: is this a maximum or minimum?

For $b < 1$: $b^{-n} > 1$, so $g' > 0$ (increasing).
For $b > 1$: $b^{-n} < 1$, so $g' < 0$ (decreasing).

So $b = 1$ is a maximum with $g(1) = (2-n) + 2(n-1) = 2n - 2 - n + 2 = n$.

Wait!! $g(1) = (2-n) \cdot 1 + 2(n-1) \cdot 1 = 2 - n + 2n - 2 = n$.

So $g_{\max} = n$ for $k = 1$ (and equivalently $k = n-1$)!! 

But earlier for $k = n-1$, I computed $g_{\max} = (n-1)^{2/n} \cdot \frac{2n^2-5n+4}{(n-1)^2}$, which for $n = 3$ gave $\approx 2.777 < 3$.

There's a contradiction. Let me recheck.

For $k = n-1$: $g(a) = 2(n-1)a^{-(n-2)} - (n-2)a^{-2(n-1)}$.

$g(1) = 2(n-1) - (n-2) = 2n - 2 - n + 2 = n$.

So $g(1) = n$ as well! But I found the critical point at $a = (n-1)^{1/n}$, not $a = 1$.

Let me recheck the derivative. $g'(a) = 2(n-1)(-(n-2))a^{-(n-1)} - (n-2)(-2(n-1))a^{-2n+1}$

$= -2(n-1)(n-2)a^{-(n-1)} + 2(n-1)(n-2)a^{-2n+1}$

$= 2(n-1)(n-2)[-a^{-(n-1)} + a^{-2n+1}]$

$= 2(n-1)(n-2)a^{-(n-1)}[-1 + a^{-n}]$.

Critical point: $a^{-n} = 1 \Rightarrow a = 1$.

So the critical point IS $a = 1$, not $a = (n-1)^{1/n}$! I made an error earlier. Let me see where.

Earlier I wrote: $g'(a) = 2(n-1)(n-2)a^{-(n-1)}[-1 + (n-1)a^{-n}]$.

The factor $(n-1)$ shouldn't be there. Let me recompute.

$g(a) = 2(n-1)a^{-(n-2)} - (n-2)a^{-2(n-1)}$.

$\frac{d}{da}[2(n-1)a^{-(n-2)}] = 2(n-1) \cdot (-(n-2)) \cdot a^{-(n-1)} = -2(n-1)(n-2)a^{-(n-1)}$.

$\frac{d}{da}[-(n-2)a^{-2(n-1)}] = -(n-2) \cdot (-2(n-1)) \cdot a^{-2(n-1)-1} = 2(n-1)(n-2)a^{-2n+1}$.

$g'(a) = -2(n-1)(n-2)a^{-(n-1)} + 2(n-1)(n-2)a^{-2n+1} = 2(n-1)(n-2)[-a^{-(n-1)} + a^{-2n+1}]$.

$= 2(n-1)(n-2)a^{-(n-1)}[-1 + a^{-n}]$.

So $g'(a) = 0 \iff a^{-n} = 1 \iff a = 1$.

I made an arithmetic error earlier when I wrote $(n-1)a^{-n}$ instead of $a^{-n}$. The correct critical point is $a = 1$, giving $g(1) = n$.

So $g_{\max} = n$, achieved at $a = b = 1$ (all variables equal). But at all-equal, $g = n$ and the original expression has $0/0$ form...

Wait, if all $y_i = 1$, then $G = 1$, $Q = n$, $S = n$. $g = S^2 - (n-1)Q = n^2 - n(n-1) = n^2 - n^2 + n = n$. And $f = g - n = 0$. So the inequality $f \geq 0$ holds with equality at all-equal.

But the ratio $R = \frac{Q/n - G^2}{nQ - S^2} = \frac{1 - 1}{n \cdot n - n^2} = 0/0$. So at all-equal, the ratio is indeterminate, and we need the limit.

So the inequality $(\sum y_i)^2 \leq (n-1)\sum y_i^2 + nG^2$ holds (with $g \leq n$), and equality holds when all $y_i$ are equal. This means $c = 1/n$ makes the inequality hold, but we need to check if $c = 1/n$ is the smallest such constant, i.e., if the ratio can get arbitrarily close to $1/n$.

From our earlier analysis, as $t \to \infty$ with $k = n-1$ variables equal to $t$ and one equal to $t^{-(n-1)}$:

$R \to \frac{1}{n}$.

So the supremum of the ratio is $1/n$, and it's approached but not achieved (at finite configurations). Thus $c = 1/n$ is the answer.

But wait, I need to verify that $g \leq n$ for ALL configurations, not just the 2-value ones. The Lagrange multiplier argument shows that the maximum of $g$ on $\{y: \prod y_i = 1\}$ is achieved at a critical point (since $g \to 0$ or $-\infty$ at the boundary, and $g = n > 0$ at the all-equal point, so the max is achieved). At the critical point, variables take at most 2 values. We checked all such cases and found $g \leq n$ with equality at all-equal.

Actually, I need to be more careful. The maximum of $g$ is $n$, achieved at all-equal. But is this really the maximum? Let me verify with a specific example for $n = 3$.

$y_1 = y_2 = 2, y_3 = 1/4$ (so $\prod = 1$). $S = 4.25, Q = 8 + 1/16 = 8.0625$.
$g = S^2 - 2Q = 18.0625 - 16.125 = 1.9375 < 3$. ✓

$y_1 = 1, y_2 = 1, y_3 = 1$: $g = 9 - 6 = 3 = n$. ✓

$y_1 = 3, y_2 = 3, y_3 = 1/9$: $S = 6 + 1/9, Q = 18 + 1/81$. $g = (6+1/9)^2 - 2(18+1/81) = 36 + 12/9 + 1/81 - 36 - 2/81 = 4/3 + 1/81 - 2/81 = 4/3 - 1/81 = 108/81 - 1/81 = 107/81 \approx 1.32 < 3$. ✓

So indeed $g \leq n$ with equality at all-equal. 

Now, the key question: is $c = 1/n$ the smallest constant? We showed the ratio $R \to 1/n$ as $t \to \infty$ in the $k = n-1$ configuration. So yes, $c = 1/n$ is the infimum of valid constants, and since the inequality holds with $c = 1/n$, it's the minimum.

Wait, I need to double-check that the inequality actually holds with $c = 1/n$, i.e., that $g \leq n$ for all configurations. Let me make the argument rigorous.

**Rigorous proof that $g \leq n$:**

We want to show $(\sum y_i)^2 \leq (n-1)\sum y_i^2 + n(\prod y_i)^{2/n}$ for all $y_i > 0$.

By homogeneity (degree 2), WLOG $\prod y_i = 1$. Need $(\sum y_i)^2 \leq (n-1)\sum y_i^2 + n$.

Define $h(y) = (n-1)\sum y_i^2 + n - (\sum y_i)^2$ on the set $\Omega = \{y \in \mathbb{R}_{>0}^n : \prod y_i = 1\}$.

We want $h \geq 0$ on $\Omega$.

$h = (n-2)\sum y_i^2 + n - 2\sum_{i<j} y_i y_j$.

**Case $n = 2$:** $h = 0 \cdot (y_1^2 + y_2^2) + 2 - 2y_1 y_2 = 2(1 - y_1 y_2) = 0$ since $y_1 y_2 = 1$. So $h = 0$ always. ✓

**Case $n \geq 3$:** 

The set $\Omega$ is a smooth manifold. The function $h$ is continuous on $\Omega$. 

Claim: $h(y) \to +\infty$ as $y \to \partial \Omega$ (i.e., as some $y_i \to 0$ or $\infty$).

If some $y_i \to \infty$ and others adjust to keep $\prod = 1$: WLOG $y_1 \to \infty$. Then $\sum y_i^2 \geq y_1^2 \to \infty$ and $(\sum y_i)^2 \leq (n \max y_i)^2$. More precisely, if $y_1 \to \infty$, then $\sum y_i^2 \geq y_1^2$ and $(\sum y_i)^2 \leq n \sum y_i^2$ (Cauchy-Schwarz), so $h \geq (n-1)\sum y_i^2 + n - n\sum y_i^2 = n - \sum y_i^2 \to -\infty$.

Hmm, that goes the wrong way. Let me think again.

Actually, $h = (n-1)Q + n - S^2$ where $Q = \sum y_i^2, S = \sum y_i$. By Cauchy-Schwarz, $S^2 \leq nQ$, so $h \geq (n-1)Q + n - nQ = n - Q$. If $Q \to \infty$, this goes to $-\infty$. So $h$ can be negative for large $Q$?

But we're trying to prove $h \geq 0$! Let me check with a specific example.

$n = 3, y_1 = 10, y_2 = 10, y_3 = 1/100$ (so $\prod = 1$). $Q = 200 + 0.0001 = 200.0001$, $S = 20.01$.
$h = 2 \cdot 200.0001 + 3 - 20.01^2 = 400.0002 + 3 - 400.4001 = 2.6001 > 0$. ✓

$n = 3, y_1 = 100, y_2 = 100, y_3 = 1/10000$. $Q = 20000 + 10^{-8}$, $S = 200.0001$.
$h = 2 \cdot 20000 + 3 - 200.0001^2 = 40000 + 3 - 40000.04 = 2.96 > 0$. ✓

So $h > 0$ in these cases. The Cauchy-Schwarz bound is too loose.

Let me try $y_1 = 100, y_2 = 1, y_3 = 1/100$ (so $\prod = 1$). $Q = 10000 + 1 + 0.0001 = 10001.0001$, $S = 101.01$.
$h = 2 \cdot 10001.0001 + 3 - 101.01^2 = 20002.0002 + 3 - 10203.0201 = 9801.98 > 0$. ✓

What about $y_1 = t, y_2 = t, y_3 = t^{-2}$ for large $t$? $Q = 2t^2 + t^{-4}$, $S = 2t + t^{-2}$.
$h = 2(2t^2 + t^{-4}) + 3 - (2t + t^{-2})^2 = 4t^2 + 2t^{-4} + 3 - 4t^2 - 4t^{-1} - t^{-4} = t^{-4} + 3 - 4t^{-1}$.
As $t \to \infty$: $h \to 3 > 0$. ✓

And $h = 3 - 4/t + 1/t^4$, which for $t = 1$ gives $h = 3 - 4 + 1 = 0$. For $t > 1$, $h > 0$ (since $3 - 4/t + 1/t^4 > 3 - 4/t > 0$ for $t > 4/3$; for $1 < t < 4/3$, need to check more carefully, but $h(1) = 0$ and $h'(1) = 4 - 4 = 0$ and $h''(1) = ... > 0$ probably).

OK so it seems like $h \geq 0$ always, with equality only at all-equal. Let me try to prove this properly.

**Proof strategy:** Show that $h$ achieves its minimum on $\Omega$ at the all-equal point, where $h = 0$.

Since $\Omega$ is not compact, we need to show $h \to +\infty$ or at least $h$ is bounded below as we go to the boundary. But from the examples, $h$ seems to approach a positive constant, not $+\infty$. So the infimum might be $0$, achieved at all-equal.

Actually, the all-equal point IS in $\Omega$ (it's $y_i = 1$ for all $i$), and $h = 0$ there. So if $h \geq 0$ everywhere, the minimum is $0$ at all-equal.

To prove $h \geq 0$, I'll use the method of Lagrange multipliers to find all critical points of $h$ on $\Omega$ and show $h \geq 0$ at each, plus check the boundary behavior.

At a critical point of $h$ on $\Omega$: $\nabla h = \lambda \nabla(\prod y_i)$, i.e., $\frac{\partial h}{\partial y_k} = \lambda \prod_{i \neq k} y_i = \lambda / y_k$ (since $\prod y_i = 1$).

$\frac{\partial h}{\partial y_k} = 2(n-1)y_k - 2S = \lambda / y_k$.

$2(n-1)y_k^2 - 2S y_k = \lambda$ for all $k$.

So each $y_k$ is a root of $2(n-1)t^2 - 2St - \lambda = 0$. At most 2 distinct values.

If all equal: $y_k = 1$, $h = 0$.

If two distinct values $a$ (multiplicity $k$) and $b$ (multiplicity $n-k$), $a^k b^{n-k} = 1$:

$h = (n-1)(ka^2 + (n-k)b^2) + n - (ka + (n-k)b)^2$.

$= (n-1)ka^2 + (n-1)(n-k)b^2 + n - k^2 a^2 - 2k(n-k)ab - (n-k)^2 b^2$

$= k(n-1-k)a^2 + (n-k)(n-1-(n-k))b^2 + n - 2k(n-k)ab$

$= k(n-1-k)a^2 + (n-k)(k-1)b^2 + n - 2k(n-k)ab$.

Note $n - 1 - k = (n-k) - 1$ and $k - 1$. So:

$h = k(n-k-1)a^2 + (n-k)(k-1)b^2 + n - 2k(n-k)ab$.

Hmm, let me factor. Let $\alpha = k, \beta = n-k$. Then:

$h = \alpha(\beta - 1)a^2 + \beta(\alpha - 1)b^2 + n - 2\alpha\beta ab$.

$= \alpha\beta a^2 - \alpha a^2 + \alpha\beta b^2 - \beta b^2 + n - 2\alpha\beta ab$

$= \alpha\beta(a^2 - 2ab + b^2) - \alpha a^2 - \beta b^2 + n$

$= \alpha\beta(a-b)^2 - \alpha a^2 - \beta b^2 + n$.

With $a^\alpha b^\beta = 1$ (where $\alpha + \beta = n$).

So $h = \alpha\beta(a-b)^2 - \alpha a^2 - \beta b^2 + n$.

$= \alpha\beta(a-b)^2 + n - \alpha a^2 - \beta b^2$.

Hmm, this can be rewritten. Note $\alpha a^2 + \beta b^2 = Q$ and $n = \alpha + \beta$.

$h = \alpha\beta(a-b)^2 + \alpha + \beta - \alpha a^2 - \beta b^2 = \alpha(1 - a^2) + \beta(1 - b^2) + \alpha\beta(a-b)^2$.

$= \alpha(1-a)(1+a) + \beta(1-b)(1+b) + \alpha\beta(a-b)^2$.

With $a^\alpha b^\beta = 1$.

This is still complex. Let me try specific cases.

**Case $k = 1$ ($\alpha = 1, \beta = n-1$):** $ab^{n-1} = 1$.

$h = (n-1)(a-b)^2 + n - a^2 - (n-1)b^2$

$= (n-1)(a^2 - 2ab + b^2) + n - a^2 - (n-1)b^2$

$= (n-1)a^2 - 2(n-1)ab + (n-1)b^2 + n - a^2 - (n-1)b^2$

$= (n-2)a^2 - 2(n-1)ab + n$.

With $a = b^{-(n-1)}$:

$h = (n-2)b^{-2(n-1)} - 2(n-1)b^{-(n-2)} + n$.

At $b = 1$: $h = (n-2) - 2(n-1) + n = n - 2 - 2n + 2 + n = 0$. ✓

$h'(b) = (n-2)(-2(n-1))b^{-2n+1} - 2(n-1)(-(n-2))b^{-(n-1)}$

$= -2(n-1)(n-2)b^{-2n+1} + 2(n-1)(n-2)b^{-(n-1)}$

$= 2(n-1)(n-2)b^{-(n-1)}[1 - b^{-n}]$... 

wait: $-2n+1 = -(2n-1)$ and $-(n-1)$. $b^{-2n+1} = b^{-(n-1)} \cdot b^{-n}$. So:

$h'(b) = 2(n-1)(n-2)b^{-(n-1)}[-b^{-n} + 1] = 2(n-1)(n-2)b^{-(n-1)}[1 - b^{-n}]$.

For $b > 1$: $b^{-n} < 1$, so $h' > 0$ (increasing). For $b < 1$: $b^{-n} > 1$, so $h' < 0$ (decreasing).

So $b = 1$ is a minimum with $h = 0$. For $b \neq 1$, $h > 0$. ✓

**Case $k = n-1$ ($\alpha = n-1, \beta = 1$):** By symmetry (swap $a \leftrightarrow b$, $\alpha \leftrightarrow \beta$), same result: $h \geq 0$ with equality at $a = b = 1$.

**Case $2 \leq k \leq n-2$ ($\alpha, \beta \geq 2$):** We showed the only critical point is $a = b = 1$ (i.e., $w = 1$). At this point $h = 0$. And $h \to +\infty$ as $a \to 0$ or $a \to \infty$ (since the dominant terms $(n-2)Q$ grow faster than $S^2$... actually let me check).

As $a \to \infty$ (with $b = a^{-\alpha/\beta} \to 0$): $h \approx \alpha(\beta-1)a^2 + n - \alpha a^2 = \alpha(\beta - 2)a^2 + n$. If $\beta \geq 2$ (i.e., $k \leq n-2$), then $\beta - 1 \geq 1$ and $\alpha(\beta-1) - \alpha = \alpha(\beta - 2) \geq 0$. If $\beta = 2$ ($k = n-2$): $h \to n > 0$. If $\beta > 2$: $h \to +\infty$.

As $a \to 0$ (with $b \to \infty$): $h \approx \beta(\alpha - 1)b^2 + n - \beta b^2 = \beta(\alpha - 2)b^2 + n$. If $\alpha \geq 2$ (i.e., $k \geq 2$), similarly $h \to n$ or $+\infty$.

So for $2 \leq k \leq n-2$, $h \to +\infty$ or $n > 0$ at the boundary, and the only critical point is $a = b = 1$ with $h = 0$. So $h \geq 0$ with equality at all-equal. ✓

**Summary for critical points:** In all cases ($k = 1, n-1$, or $2 \leq k \leq n-2$), $h \geq 0$ at critical points, with equality only at all-equal.

**Boundary behavior:** As any $y_i \to 0$ or $\infty$ (on $\Omega$), we need $h$ not to go to $-\infty$. From the 2-value analysis, $h \to 0^+$ or $+\infty$ at the boundary. But we need to check general configurations too.

Actually, the argument is: $h$ is continuous on $\Omega$, $h = 0$ at the all-equal point, and $h > 0$ at all other critical points. If $h$ were negative somewhere, then since $h \to 0^+$ or $+\infty$ at the boundary (need to verify), $h$ would achieve a negative minimum at an interior critical point, contradicting $h \geq 0$ at all critical points.

But I need to verify the boundary behavior for general (not just 2-value) configurations. Let me think about this.

If $\max y_i / \min y_i \to \infty$ on $\Omega$, what happens to $h$?

WLOG $y_1 \geq y_2 \geq \cdots \geq y_n > 0$ with $\prod y_i = 1$ and $y_1 / y_n \to \infty$.

$h = (n-1)Q + n - S^2 = (n-2)Q + n - 2P$ where $P = \sum_{i<j} y_i y_j$.

$S^2 = Q + 2P$, so $h = (n-1)Q + n - Q - 2P = (n-2)Q + n - 2P$.

We need to show $h \not\to -\infty$, i.e., $(n-2)Q - 2P$ is bounded below.

$(n-2)Q - 2P = (n-2)\sum y_i^2 - 2\sum_{i<j} y_i y_j = \sum y_i^2 \cdot (n-2) - 2\sum_{i<j} y_i y_j$.

$= (n-2)\sum y_i^2 - [(\sum y_i)^2 - \sum y_i^2] = (n-1)\sum y_i^2 - (\sum y_i)^2$.

So $h = (n-1)Q - S^2 + n$. And $(n-1)Q - S^2 = (n-1)Q - S^2$.

By Cauchy-Schwarz, $S^2 \leq nQ$, so $(n-1)Q - S^2 \geq (n-1)Q - nQ = -Q$. So $h \geq n - Q$, which goes to $-\infty$ if $Q \to \infty$. Not helpful.

But we also have $S^2 \geq Q$ (since $S^2 = Q + 2P \geq Q$), so $(n-1)Q - S^2 \leq (n-2)Q$.

Hmm, I need a better bound. Let me think about this differently.

Actually, I think the key insight is that we don't need to check the boundary for general configurations. The argument is:

1. $h$ is continuous on $\Omega$.
2. $h = 0$ at the all-equal point.
3. At every critical point of $h$ on $\Omega$, $h \geq 0$ (shown above).
4. If $h < 0$ somewhere, then $h$ achieves a negative minimum at some point in $\Omega$ (since $\Omega$ is connected and $h = 0$ at all-equal, the sublevel set $\{h \leq h_0\}$ for $h_0 < 0$ is bounded away from the all-equal point; but is it compact?).

The issue is that $\Omega$ is not compact, so the minimum might not be achieved. But if $h \to +\infty$ or to a positive limit at the boundary, then the sublevel set $\{h \leq 0\}$ is compact, and the minimum is achieved.

So I need to show $h$ is bounded below (by something $\geq 0$) at the boundary of $\Omega$.

Let me try to show $h \geq 0$ directly, without the optimization argument.

**Direct proof attempt:**

We want $(\sum y_i)^2 \leq (n-1)\sum y_i^2 + nG^2$ where $G = (\prod y_i)^{1/n}$.

Equivalently, $nG^2 \geq (\sum y_i)^2 - (n-1)\sum y_i^2 = 2\sum_{i<j} y_i y_j - (n-2)\sum y_i^2$.

Let me try to use the AM-GM inequality on the RHS.

$2\sum_{i<j} y_i y_j - (n-2)\sum y_i^2 = \sum_{i<j} (2y_i y_j - \frac{n-2}{n-1} \cdot \frac{(n-1)}{...})$. This doesn't factor nicely.

Let me try a different approach. Consider the function $\phi(y) = \log(\text{LHS}/\text{RHS})$ or use the weighted AM-GM.

Actually, let me try the **SOS approach** for $n = 3$ and see if it generalizes.

For $n = 3$: $h = y_1^2 + y_2^2 + y_3^2 + 3G^2 - 2(y_1 y_2 + y_1 y_3 + y_2 y_3)$ where $G = (y_1 y_2 y_3)^{1/3}$.

With $G = 1$ (i.e., $y_1 y_2 y_3 = 1$): $h = y_1^2 + y_2^2 + y_3^2 + 3 - 2(y_1 y_2 + y_1 y_3 + y_2 y_3)$.

$= (y_1 - y_2)^2 + (y_1 - y_3)^2 + (y_2 - y_3)^2 - (y_1 y_2 + y_1 y_3 + y_2 y_3) + 3$... 

no: $(y_1-y_2)^2 + (y_1-y_3)^2 + (y_2-y_3)^2 = 2(y_1^2+y_2^2+y_3^2) - 2(y_1y_2+y_1y_3+y_2y_3) = 2Q - 2P$.

So $h = Q + 3 - 2P = (2Q - 2P) - Q + 3 = \sum(y_i - y_j)^2 - Q + 3$.

Need $\sum(y_i - y_j)^2 + 3 \geq Q = y_1^2 + y_2^2 + y_3^2$ with $y_1 y_2 y_3 = 1$.

By AM-GM, $y_1^2 + y_2^2 + y_3^2 \geq 3$. And $\sum(y_i - y_j)^2 \geq 0$. But we need $\sum(y_i-y_j)^2 \geq Q - 3$, which isn't obvious.

Hmm. Let me try yet another approach.

**Approach using the inequality between power sums:**

We want to show $S^2 \leq (n-1)Q + nG^2$.

Consider the polynomial $p(t) = \prod(t - y_i) = t^n - S_1 t^{n-1} + S_2 t^{n-2} - \cdots$ where $S_k$ are elementary symmetric polynomials.

We have $S_1 = \sum y_i = S$, $S_2 = \sum_{i<j} y_i y_j = P$, and $S_n = \prod y_i = G^n$.

$S^2 = S_1^2 = Q + 2S_2 = Q + 2P$.

So we need $Q + 2P \leq (n-1)Q + nG^2$, i.e., $2P \leq (n-2)Q + nG^2$.

By Maclaurin's inequality: $S_2 / \binom{n}{2} \leq (S_1/n)^2$, i.e., $P \leq \frac{n-1}{2n} S^2$. And $S_1/n \geq G$, i.e., $S \geq nG$.

Also, $Q \geq S^2/n$ (Cauchy-Schwarz) and $Q \geq nG^2$ (AM-GM on $y_i^2$).

From $P \leq \frac{n-1}{2n} S^2$ and $S^2 = Q + 2P$:

$P \leq \frac{n-1}{2n}(Q + 2P) \Rightarrow P \leq \frac{(n-1)Q}{2n} + \frac{(n-1)P}{n} \Rightarrow P(1 - \frac{n-1}{n}) \leq \frac{(n-1)Q}{2n} \Rightarrow \frac{P}{n} \leq \frac{(n-1)Q}{2n} \Rightarrow P \leq \frac{(n-1)Q}{2}$.

So $2P \leq (n-1)Q$. We need $2P \leq (n-2)Q + nG^2$. Since $(n-1)Q \leq (n-2)Q + nG^2$ iff $Q \leq nG^2$, which is FALSE (AM-GM gives $Q \geq nG^2$). So Maclaurin alone isn't enough.

We need a tighter bound on $P$ that incorporates $G$.

**Approach: Use Schur's inequality.**

Schur's inequality (degree $t$): $\sum y_i^t(y_i - y_j)(y_i - y_k) \geq 0$ for $t \geq 0$.

For $n = 3$ and $t = 2$: $\sum y_i^2(y_i - y_j)(y_i - y_k) \geq 0$, which gives $\sum y_i^4 + y_1 y_2 y_3 \sum y_i \geq \sum_{sym} y_i^3 y_j$.

Not sure this helps directly.

Let me try a completely different approach to prove the inequality.

**Approach: Induction on $n$.**

For $n = 2$: equality, as shown.

Assume the inequality holds for $n-1$: $(\sum_{i=1}^{n-1} y_i)^2 \leq (n-2)\sum_{i=1}^{n-1} y_i^2 + (n-1)(\prod_{i=1}^{n-1} y_i)^{2/(n-1)}$.

We want to prove for $n$. Let $y_n = t$ and $S' = \sum_{i=1}^{n-1} y_i$, $Q' = \sum_{i=1}^{n-1} y_i^2$, $P' = \prod_{i=1}^{n-1} y_i$.

$(S' + t)^2 \leq (n-1)(Q' + t^2) + n(P' \cdot t)^{2/n}$.

$S'^2 + 2S't + t^2 \leq (n-1)Q' + (n-1)t^2 + n(P't)^{2/n}$.

$S'^2 + 2S't \leq (n-1)Q' + (n-2)t^2 + n(P't)^{2/n}$.

By induction: $S'^2 \leq (n-2)Q' + (n-1)(P')^{2/(n-1)}$.

So it suffices to show: $(n-2)Q' + (n-1)(P')^{2/(n-1)} + 2S't \leq (n-1)Q' + (n-2)t^2 + n(P't)^{2/n}$.

i.e., $(n-1)(P')^{2/(n-1)} + 2S't \leq Q' + (n-2)t^2 + n(P't)^{2/n}$.

This doesn't seem to simplify nicely either.

**Approach: Use the weighted power mean inequality or a direct convexity argument.**

Let me try to prove the inequality $h \geq 0$ by showing it's a sum of non-negative terms.

$h = (n-1)Q + nG^2 - S^2 = (n-2)Q + nG^2 - 2P$.

$= \sum_i (n-2) y_i^2 + nG^2 - 2\sum_{i<j} y_i y_j$.

$= \sum_{i<j} [(n-2)\frac{y_i^2 + y_j^2}{n-1} \cdot (n-1) / \binom{n}{2} \cdot ...]$

Hmm, let me try: $(n-2)Q = (n-2)\sum y_i^2$. And $2P = 2\sum_{i<j} y_i y_j = \sum_{i<j} 2y_i y_j$.

$(n-2)Q - 2P = \sum_{i<j} [(n-2)\frac{y_i^2 + y_j^2}{n-1} - 2y_i y_j] \cdot \frac{n-1}{?}$... 

Actually, $\sum_{i<j} (y_i^2 + y_j^2) = (n-1)Q$ (each $y_i^2$ appears in $n-1$ pairs). So $(n-2)Q = \frac{n-2}{n-1} \sum_{i<j} (y_i^2 + y_j^2)$.

$(n-2)Q - 2P = \sum_{i<j} [\frac{n-2}{n-1}(y_i^2 + y_j^2) - 2y_i y_j] = \sum_{i<j} \frac{(n-2)(y_i^2 + y_j^2) - 2(n-1)y_i y_j}{n-1}$.

$= \frac{1}{n-1}\sum_{i<j} [(n-2)y_i^2 - 2(n-1)y_i y_j + (n-2)y_j^2]$

$= \frac{1}{n-1}\sum_{i<j} [(n-2)(y_i^2 + y_j^2) - 2(n-1)y_i y_j]$.

The expression in brackets: $(n-2)(y_i^2 + y_j^2) - 2(n-1)y_i y_j = (n-2)y_i^2 - 2(n-1)y_i y_j + (n-2)y_j^2$.

Discriminant (as quadratic in $y_i$): $4(n-1)^2 y_j^2 - 4(n-2)^2 y_j^2 = 4y_j^2[(n-1)^2 - (n-2)^2] = 4y_j^2(2n-3)$.

So this quadratic has real roots and can be negative. So this decomposition doesn't give non-negative terms.

Let me try another decomposition. We need $h = (n-2)Q + nG^2 - 2P \geq 0$.

$2P = S^2 - Q$, so $h = (n-1)Q + nG^2 - S^2$.

Let me use the substitution $y_i = G(1 + \epsilon_i)$ where $\sum \epsilon_i$ is not necessarily 0 but $\prod(1+\epsilon_i) = 1$.

Hmm, this is getting complicated. Let me try a more computational approach.

**Approach: Prove using the tangent line trick.**

We want to show $nG^2 \geq S^2 - (n-1)Q$, i.e., $n(\prod y_i)^{2/n} \geq (\sum y_i)^2 - (n-1)\sum y_i^2$.

The RHS $= 2\sum_{i<j} y_i y_j - (n-2)\sum y_i^2$.

Consider the function $F(y) = n(\prod y_i)^{2/n} - 2\sum_{i<j} y_i y_j + (
