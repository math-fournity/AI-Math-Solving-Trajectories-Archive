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
  <problem_id>polymath_01021</problem_id>
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

For non-negative real numbers $x_{1}, x_{2}, \cdots, x_{n}$ satisfying $x_{1}+x_{2}+\cdots+x_{n}=1$. Find the maximum value of $\sum_{j=1}^{n}\left(x_{j}^{4}-x_{j}^{5}\right)$.

## Standard Solution

Solution: Use the adjustment method to explore the maximum value of the sum in the problem.
(i) First, for $x, y > 0$, we compare $(x+y)^{4} - (x+y)^{5} + 0^{4} - 0^{5}$ with $x^{4} - x^{5} + y^{4} - y^{5}$:
$$
\begin{array}{l}
(x+y)^{4} - (x+y)^{5} + 0^{4} - 0^{5} - \left(x^{4} - x^{5} + y^{4} - y^{5}\right) \\
= x y \left(4 x^{2} + 6 x y + 4 y^{2}\right) \\
- x y \left(5 x^{3} + 10 x^{2} y + 10 x y^{2} + 5 y^{3}\right) \\
\geqslant \frac{7}{2} x y \left(x^{2} + 2 x y + y^{2}\right) \\
- 5 x y \left(x^{3} + 3 x^{2} y + 3 x y^{2} + y^{3}\right) \\
= \frac{1}{2} x y (x+y)^{2} [7 - 10(x+y)].
\end{array}
$$

As long as $x, y > 0, x + y > 0$, then, among them, there must be two whose sum $\leqslant \frac{2}{3}0, x + y = 1$.
$$

For this case,
$$
\begin{array}{l}
x^{4} - x^{5} + y^{4} - y^{5} \\
= x^{4}(1 - x) + y^{4}(1 - y) \\
= x y \left(x^{3} + y^{3}\right) \\
= x y \left[(x + y)^{3} - 3 x y (x + y)\right] \\
= x y (1 - 3 x y) \\
= \frac{1}{3} (3 x y) (1 - 3 x y).
\end{array}
$$

When $3 x y = \frac{1}{2}$, the above expression reaches its maximum value:
$$
x^{4} - x^{5} + y^{4} - y^{5} = \frac{1}{6} \left(1 - \frac{1}{2}\right) = \frac{1}{12}.
$$

This is the maximum value sought in the problem. The $x_{1}, x_{2}, \cdots, x_{n}$ that can achieve this maximum value have only two that are not equal to 0. Let $x$ and $y$ represent these two numbers, then
$$
x, y > 0, x + y = 1, x y = \frac{1}{6}.
$$

Solving the quadratic equation $\lambda^{2} - \lambda + \frac{1}{6} = 0$ yields
$$
x = \frac{3 + \sqrt{3}}{6}, y = \frac{3 - \sqrt{3}}{6},
$$

or it can also be $x = \frac{3 - \sqrt{3}}{6}, y = \frac{3 + \sqrt{3}}{6}$.
Verification shows that if $x_{1}, x_{2}, \cdots, x_{n}$ have only these two non-zero numbers, then the sum in the problem indeed reaches the maximum value $\frac{1}{12}$.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We need to find the maximum of $\sum_{j=1}^n (x_j^4 - x_j^5)$ subject to $x_j \geq 0$ and $\sum x_j = 1$.

Let me think about this. The function $f(x) = x^4 - x^5 = x^4(1-x)$ for $x \in [0,1]$.

We want to maximize $\sum f(x_j)$ subject to $\sum x_j = 1$, $x_j \geq 0$.

First, let me understand $f$. $f'(x) = 4x^3 - 5x^4 = x^3(4-5x)$. So $f$ is increasing on $[0, 4/5]$ and decreasing on $[4/5, 1]$. Maximum of $f$ at $x = 4/5$: $f(4/5) = (4/5)^4 (1/5) = 256/3125$.

Now, the question is how to distribute the mass 1 among $n$ variables to maximize the sum.

By Lagrange multipliers / KKT conditions, at an interior optimum, $f'(x_j) = \lambda$ for all $j$ with $x_j > 0$. So all positive $x_j$ take the same value (since $f'$ is not monotone, there could be two values, but let's think more carefully).

Actually $f'(x) = x^3(4-5x)$. This is 0 at $x=0$ and $x=4/5$, positive on $(0,4/5)$, negative on $(4/5,1)$. So $f'$ is not monotone - it increases then decreases. So for a given $\lambda > 0$, there could be two solutions to $f'(x) = \lambda$.

But let me think about whether the maximum is achieved at a symmetric point or at a boundary.

Let me consider: is it better to put all mass in one variable, or split?

Case 1: All mass in one variable. $x_1 = 1$, rest 0. Sum = $f(1) = 1 - 1 = 0$.

Case 2: Two variables equal, $x_1 = x_2 = 1/2$. Sum = $2 \cdot f(1/2) = 2 \cdot (1/16)(1/2) = 2 \cdot 1/32 = 1/16$.

Case 3: $k$ variables equal to $1/k$. Sum = $k \cdot f(1/k) = k \cdot (1/k)^4 (1 - 1/k) = k \cdot \frac{1}{k^4} \cdot \frac{k-1}{k} = \frac{k-1}{k^4}$.

Let me maximize $g(k) = \frac{k-1}{k^4}$ over positive integers $k$.

$g(1) = 0$, $g(2) = 1/16 = 0.0625$, $g(3) = 2/81 \approx 0.0247$, $g(4) = 3/256 \approx 0.0117$.

So among equal splits, $k=2$ gives the maximum.

But we should also consider unequal splits. Let me think about whether we can do better than $1/16$.

Consider two variables $x_1 = a$, $x_2 = 1-a$, rest 0. Maximize $f(a) + f(1-a)$.

$h(a) = a^4(1-a) + (1-a)^4 a = a(1-a)[a^3 + (1-a)^3]$.

Let me compute. $a^3 + (1-a)^3 = (a + (1-a))(a^2 - a(1-a) + (1-a)^2) = 1 \cdot (a^2 - a + a^2 + 1 - 2a + a^2) = 3a^2 - 3a + 1$.

So $h(a) = a(1-a)(3a^2 - 3a + 1)$.

Let $t = a(1-a)$, so $t \in [0, 1/4]$. And $3a^2 - 3a + 1 = 1 - 3a(1-a) = 1 - 3t$.

So $h = t(1 - 3t) = t - 3t^2$.

Maximize: $h'(t) = 1 - 6t = 0 \Rightarrow t = 1/6$.

$h(1/6) = 1/6 - 3/36 = 1/6 - 1/12 = 1/12$.

$1/12 \approx 0.0833 > 1/16 = 0.0625$.

So unequal split with two variables is better! $t = 1/6$ means $a(1-a) = 1/6$, so $a = \frac{1 \pm \sqrt{1 - 4/6}}{2} = \frac{1 \pm \sqrt{1/3}}{2}$.

So $a = \frac{1 + 1/\sqrt{3}}{2}$ or $a = \frac{1 - 1/\sqrt{3}}{2}$.

Now, can we do even better with three variables or more?

Let me think about this more carefully. We need to check if using 3 or more variables (possibly unequal) can beat $1/12$.

Let me consider the general problem. We want to maximize $\sum f(x_j)$ where $f(x) = x^4(1-x)$.

At the optimum, by KKT, for each $x_j > 0$, $f'(x_j) = \lambda$, i.e., $x_j^3(4 - 5x_j) = \lambda$.

Let $\phi(x) = x^3(4-5x)$. This function: $\phi(0) = 0$, $\phi(4/5) = 0$, max at $\phi'(x) = 12x^2 - 20x^3 = 4x^2(3 - 5x) = 0$, so $x = 3/5$. $\phi(3/5) = (27/125)(4 - 3) = 27/125$.

So for $\lambda \in (0, 27/125)$, there are two solutions to $\phi(x) = \lambda$: one in $(0, 3/5)$ and one in $(3/5, 4/5)$.

At the optimum, all positive $x_j$ are either $a$ or $b$ where $\phi(a) = \phi(b) = \lambda$ with $a < 3/5 < b < 4/5$.

So the optimum has some number of $x_j = a$ and some $x_j = b$, with $pa + qb = 1$ where $p$ is the count of $a$'s and $q$ is the count of $b$'s.

We want to maximize $p \cdot f(a) + q \cdot f(b)$.

This is getting complex. Let me think about whether the two-variable solution is actually optimal.

Actually, let me reconsider. The function $f(x) = x^4 - x^5$ is neither convex nor concave on $[0,1]$. Let me check: $f''(x) = 12x^2 - 20x^3 = 4x^2(3 - 5x)$. So $f$ is convex on $[0, 3/5]$ and concave on $[3/5, 1]$.

Since $f$ is convex on $[0, 3/5]$, by Jensen's inequality, for variables in the convex region, splitting decreases the sum. So it's better to concentrate mass in the convex region.

Hmm, but the constraint is $\sum x_j = 1$, and we're on $[0,1]$.

Let me think about this differently. Let me check if three variables can beat $1/12$.

Three variables: try $x_1 = a, x_2 = a, x_3 = 1-2a$ for some $a$.

$S = 2f(a) + f(1-2a)$.

At $a = 1/3$: $S = 3 \cdot f(1/3) = 3 \cdot (1/81)(2/3) = 3 \cdot 2/243 = 6/243 = 2/81 \approx 0.0247$. Much less than $1/12$.

What about unequal three-variable? Let me try $x_1 = 0.6, x_2 = 0.3, x_3 = 0.1$:
$f(0.6) = 0.6^4 \cdot 0.4 = 0.1296 \cdot 0.4 = 0.05184$
$f(0.3) = 0.3^4 \cdot 0.7 = 0.0081 \cdot 0.7 = 0.00567$
$f(0.1) = 0.1^4 \cdot 0.9 = 0.0001 \cdot 0.9 = 0.00009$
Sum $\approx 0.0576$. Less than $1/12 \approx 0.0833$.

Let me try to be more systematic. With two variables, the optimum is $1/12$. Let me verify this is a local max in the full space.

Actually, let me think about whether we can do better than two variables. The key insight: $f$ is convex on $[0, 3/5]$. So if we have multiple small variables (all in the convex region), concentrating them into one would increase the sum. This suggests the optimum uses at most one "small" variable and the rest are "large" (in the concave region).

But wait, in the two-variable solution, $a = \frac{1 - 1/\sqrt{3}}{2} \approx \frac{1 - 0.577}{2} \approx 0.211$ and $b = \frac{1 + 1/\sqrt{3}}{2} \approx 0.789$.

Both are in $[0, 1]$. $a \approx 0.211 < 3/5 = 0.6$, so $a$ is in the convex region. $b \approx 0.789 > 3/5$, so $b$ is in the concave region.

Now, could we have one small variable $a$ and two large variables $b_1, b_2$ with $a + b_1 + b_2 = 1$?

If $b_1 = b_2 = b$, then $a + 2b = 1$, and we maximize $f(a) + 2f(b)$.

With KKT: $f'(a) = f'(b) = \lambda$, so $\phi(a) = \phi(b)$.

$a^3(4-5a) = b^3(4-5b)$ and $a + 2b = 1$.

This is a system of two equations. Let me try to solve numerically.

From $a = 1 - 2b$:
$(1-2b)^3(4 - 5(1-2b)) = b^3(4-5b)$
$(1-2b)^3(4 - 5 + 10b) = b^3(4-5b)$
$(1-2b)^3(10b - 1) = b^3(4-5b)$

Let me try $b = 0.4$: LHS = $(0.2)^3(3) = 0.008 \cdot 3 = 0.024$. RHS = $(0.064)(2) = 0.128$. Not equal.

$b = 0.35$: LHS = $(0.3)^3(2.5) = 0.027 \cdot 2.5 = 0.0675$. RHS = $(0.042875)(2.25) = 0.0965$. Not equal.

$b = 0.3$: LHS = $(0.4)^3(2) = 0.064 \cdot 2 = 0.128$. RHS = $(0.027)(2.5) = 0.0675$. LHS > RHS.

So between $b = 0.3$ and $b = 0.35$. Let me try $b = 0.325$:
LHS = $(0.35)^3(2.25) = 0.042875 \cdot 2.25 = 0.0965$. RHS = $(0.0343)(2.375) = 0.0815$. LHS > RHS.

$b = 0.34$: LHS = $(0.32)^3(2.4) = 0.032768 \cdot 2.4 = 0.0786$. RHS = $(0.0393)(2.3) = 0.0904$. LHS < RHS.

$b = 0.33$: LHS = $(0.34)^3(2.3) = 0.0393 \cdot 2.3 = 0.0904$. RHS = $(0.0359)(2.35) = 0.0844$. LHS > RHS.

$b = 0.335$: LHS = $(0.33)^3(2.35) = 0.0359 \cdot 2.35 = 0.0844$. RHS = $(0.0376)(2.325) = 0.0874$. LHS < RHS.

So $b \approx 0.332$. Then $a = 1 - 2(0.332) = 0.336$.

Wait, that means $a \approx b \approx 0.333$, which is just the symmetric solution $x_1 = x_2 = x_3 = 1/3$! That gives $2/81 \approx 0.0247$, much less than $1/12$.

Hmm, but there might be another solution where $a$ is small and $b$ is large. Let me reconsider.

The equation $\phi(a) = \phi(b)$ with $a < 3/5 < b$ has solutions where $a$ is small and $b$ is close to $4/5$.

With $a + 2b = 1$, if $b$ is close to $4/5 = 0.8$, then $a = 1 - 1.6 = -0.6 < 0$. Not feasible.

So with two large variables, $b < 0.5$ (since $a = 1 - 2b > 0$ requires $b < 0.5$). But $b$ in the concave region means $b > 0.6$, which contradicts $b < 0.5$. So we can't have two variables in the concave region with a positive remainder.

What about one large and two small? $a_1 + a_2 + b = 1$ with $a_1, a_2 < 3/5 < b$.

If $a_1 = a_2 = a$, then $2a + b = 1$, $b = 1 - 2a$. For $b > 0.6$, need $a < 0.2$.

KKT: $\phi(a) = \phi(b) = \phi(1-2a)$.

$a^3(4-5a) = (1-2a)^3(4-5(1-2a)) = (1-2a)^3(10a-1)$.

For this to be positive, need $a > 0.1$ (so $10a - 1 > 0$) and $a < 0.8$ (so $4-5a > 0$). And $a < 0.2$ for $b > 0.6$.

Try $a = 0.15$: LHS = $(0.15)^3(3.25) = 0.003375 \cdot 3.25 = 0.01097$. RHS = $(0.7)^3(0.5) = 0.343 \cdot 0.5 = 0.1715$. RHS >> LHS.

$a = 0.19$: LHS = $(0.19)^3(3.05) = 0.006859 \cdot 3.05 = 0.0209$. RHS = $(0.62)^3(0.9) = 0.2383 \cdot 0.9 = 0.2145$. Still RHS >> LHS.

The issue is that $\phi$ is much larger for $b$ near $0.6-0.8$ than for small $a$. So $\phi(a) = \phi(b)$ with $a$ small and $b$ large requires $\phi(b)$ to be small, meaning $b$ close to $4/5 = 0.8$. But then $a = (1-b)/2 \approx 0.1$, and $\phi(0.1) = 0.001 \cdot 3.5 = 0.0035$, while $\phi(0.8) = 0$. So we need $b$ slightly less than $0.8$.

$b = 0.79$: $\phi(0.79) = (0.79)^3(4 - 3.95) = 0.493 \cdot 0.05 = 0.0247$. $a = 0.105$. $\phi(0.105) = (0.105)^3(3.475) = 0.001158 \cdot 3.475 = 0.00402$. Not equal.

$b = 0.799$: $\phi(0.799) = (0.799)^3(0.005) = 0.510 \cdot 0.005 = 0.00255$. $a = 0.1005$. $\phi(0.1005) = (0.1005)^3(3.4975) = 0.001015 \cdot 3.4975 = 0.00355$. Getting closer but $\phi(a) > \phi(b)$.

$b = 0.798$: $\phi(0.798) = (0.798)^3(0.01) = 0.508 \cdot 0.01 = 0.00508$. $a = 0.101$. $\phi(0.101) = (0.101)^3(3.495) = 0.00103 \cdot 3.495 = 0.00360$. $\phi(b) > \phi(a)$.

So between $b = 0.798$ and $b = 0.799$. $b \approx 0.7985$, $a \approx 0.10075$.

Sum = $2f(a) + f(b) = 2 \cdot (0.10075)^4 \cdot (0.89925) + (0.7985)^4 \cdot (0.2015)$.

$f(a) = (0.10075)^4 \cdot 0.89925 \approx 0.0000103 \cdot 0.89925 \approx 0.00000926$.
$2f(a) \approx 0.0000185$.

$f(b) = (0.7985)^4 \cdot 0.2015 \approx 0.4066 \cdot 0.2015 \approx 0.0819$.

Sum $\approx 0.0819$. This is less than $1/12 \approx 0.0833$.

So the three-variable case (one large, two small) gives about $0.0819 < 1/12$.

What about one large, one small, and the rest zero? That's the two-variable case, which gives $1/12$.

Let me also check: one large, $k$ small equal variables.

$b + ka = 1$, $\phi(a) = \phi(b)$, maximize $f(b) + k \cdot f(a)$.

As $k$ increases, $a$ decreases (since $b$ is bounded by $4/5$), and $f(a) \sim a^4$ becomes very small. The sum approaches $f(b)$ with $b \to 4/5$, giving $f(4/5) = (4/5)^4(1/5) = 256/3125 \approx 0.0819$.

So as $k \to \infty$, the sum approaches $256/3125 \approx 0.0819 < 1/12$.

And for $k=1$ (two variables), we get $1/12 \approx 0.0833$.

For $k=2$ (three variables), we got $\approx 0.0819$.

So it seems like $k=1$ (two variables) is optimal.

But wait, I should also check the case where all variables are in the convex region (all $< 3/5$). In that case, by convexity, concentrating is better, so the best would be one variable = 1, giving $f(1) = 0$. Not good.

And the case where all are in the concave region (all $> 3/5$). Then $\sum x_j = 1$ with all $x_j > 3/5$ requires $n \geq 2$ but $x_1 + x_2 > 6/5 > 1$. Impossible for $n \geq 2$ unless... wait, for $n = 1$, $x_1 = 1 > 3/5$, but $f(1) = 0$. For $n \geq 2$, can't have all $> 3/5$ since sum would exceed 1.

So the only interesting case is mixed: some in convex, some in concave. And we've seen that one in each (two variables total) gives $1/12$, which beats all other configurations.

Let me also verify: could we have two variables both in the convex region but unequal? By convexity of $f$ on $[0, 3/5]$, $f(a) + f(b) \leq 2f((a+b)/2)$ for $a, b \in [0, 3/5]$. Wait, that's the wrong direction for maximization. Convexity means $f(a) + f(b) \geq 2f((a+b)/2)$, so unequal is better than equal in the convex region. But we also need $a + b \leq 1$.

Actually, for convex $f$, the sum $f(a) + f(b)$ with $a + b = s$ is maximized at the boundary (one of them is 0 or as extreme as possible). So the best with two variables in the convex region is one of them = 0, reducing to one variable.

So the global maximum should be $1/12$.

Let me now verify the two-variable solution more carefully.

We have $h(a) = f(a) + f(1-a) = a(1-a)(1 - 3a(1-a))$ where $t = a(1-a)$.

$h = t(1 - 3t) = t - 3t^2$, maximized at $t = 1/6$, giving $h = 1/6 - 3/36 = 1/6 - 1/12 = 1/12$.

Now I need to prove this is the global maximum, not just over two variables but over all $n$ and all configurations.

Let me think about a clean proof approach.

**Approach**: Show that for any $n$ and any $x_1, \ldots, x_n \geq 0$ with $\sum x_j = 1$, we have $\sum (x_j^4 - x_j^5) \leq 1/12$.

One approach: Find a tangent line / supporting function. We want to find $\alpha, \beta$ such that $f(x) \leq \alpha x + \beta$ for all $x \in [0,1]$, and then $\sum f(x_j) \leq \alpha \sum x_j + n\beta = \alpha + n\beta$. But this depends on $n$, which is bad.

Better: Find a function $g(x) = cx + dx^2$ (or some form) such that $f(x) \leq g(x)$ for all $x \in [0,1]$, and $\sum g(x_j) = c \sum x_j + d \sum x_j^2 \leq c + d \cdot (\text{something})$.

Hmm, this is tricky because we need to use the constraint $\sum x_j = 1$ effectively.

Alternative approach: Show that $f(x) \leq \frac{x}{12}$ for all $x \in [0,1]$? Then $\sum f(x_j) \leq \frac{1}{12} \sum x_j = \frac{1}{12}$.

Wait, is $f(x) \leq x/12$ for all $x \in [0,1]$? $f(x) = x^4(1-x)$. We need $x^4(1-x) \leq x/12$, i.e., $x^3(1-x) \leq 1/12$ for $x \in [0,1]$.

Maximize $x^3(1-x)$: derivative $3x^2(1-x) - x^3 = x^2(3 - 4x) = 0$ at $x = 3/4$. Value: $(3/4)^3(1/4) = 27/256 \approx 0.1055$. And $1/12 \approx 0.0833$.

So $27/256 > 1/12$, meaning $f(x) > x/12$ for some $x$. So this simple bound doesn't work.

Let me try $f(x) \leq ax + bx^2$ for some $a, b$. Then $\sum f(x_j) \leq a + b\sum x_j^2$. And $\sum x_j^2 \leq (\sum x_j)^2 = 1$ (since all $x_j \geq 0$). So $\sum f(x_j) \leq a + b$.

We need $f(x) \leq ax + bx^2$ for all $x \in [0,1]$, and minimize $a + b$.

Or maybe use a different bound on $\sum x_j^2$. By Cauchy-Schwarz, $\sum x_j^2 \geq 1/n$, but that's a lower bound. Upper bound: $\sum x_j^2 \leq 1$ (achieved when one $x_j = 1$).

Hmm, but if we use $\sum x_j^2 \leq 1$, we get $\sum f(x_j) \leq a + b$, and we need to find $a, b$ such that $x^4(1-x) \leq ax + bx^2$ for all $x \in [0,1]$, minimizing $a + b$.

At $x = 0$: $0 \leq 0$. OK.
Dividing by $x$ (for $x > 0$): $x^3(1-x) \leq a + bx$.

We need $x^3(1-x) \leq a + bx$ for all $x \in [0,1]$, minimizing $a + b$.

The function $p(x) = x^3(1-x)$ has max $27/256$ at $x = 3/4$.

We want the line $a + bx$ to be above $p(x)$ on $[0,1]$, minimizing $a + b$.

The optimal line will be tangent to $p(x)$ at some point, or pass through an endpoint.

At $x = 1$: $p(1) = 0$, so $a + b \geq 0$.
At $x = 0$: $p(0) = 0$, so $a \geq 0$.

The tangent at $x = x_0$: $p(x_0) + p'(x_0)(x - x_0) = a + bx$.
So $a = p(x_0) - p'(x_0) x_0$, $b = p'(x_0)$.
$a + b = p(x_0) + p'(x_0)(1 - x_0)$.

$p'(x) = 3x^2 - 4x^3 = x^2(3 - 4x)$.

$a + b = x_0^3(1-x_0) + x_0^2(3-4x_0)(1-x_0) = x_0^2(1-x_0)[x_0 + 3 - 4x_0] = x_0^2(1-x_0)(3 - 3x_0) = 3x_0^2(1-x_0)^2$.

Minimize $3x_0^2(1-x_0)^2$ over $x_0 \in [0,1]$. This is $3[x_0(1-x_0)]^2$, minimized at $x_0 = 0$ or $x_0 = 1$, giving 0. But we need the line to be above $p$ everywhere.

At $x_0 = 0$: $a = 0, b = 0$, line is $0$, but $p(x) > 0$ for $x \in (0,1)$. Not valid.

At $x_0 = 1$: $a = 0, b = -1$, line is $-x$, but $p(x) \geq 0 > -x$ for $x \in (0,1)$... wait, $-x < 0 \leq p(x)$, so the line is below. Not valid.

The issue is that a single tangent line won't work. We need the line to be above $p$ everywhere, which requires it to be a supporting line from above.

For a tangent to be above $p$ everywhere, $p$ must be concave. But $p(x) = x^3(1-x)$ is not concave on all of $[0,1]$.

$p''(x) = 6x - 12x^2 = 6x(1-2x)$. So $p$ is convex on $[0, 1/2]$ and concave on $[1/2, 1]$.

So a tangent at a point in the concave region ($x_0 > 1/2$) will be above $p$ on the concave part but might be below on the convex part.

This approach is getting complicated. Let me try a different strategy.

**Alternative approach**: Directly prove $\sum f(x_j) \leq 1/12$ using the structure of $f$.

Let me try the substitution approach. We showed that for two variables, the max is $1/12$. Let me show that for any $n$ variables, we can reduce to two variables without decreasing the sum.

**Key claim**: If $x_1, x_2, \ldots, x_n \geq 0$ with $\sum x_j = 1$, and $n \geq 3$, then we can find $y_1, \ldots, y_m$ with $m < n$, $y_i \geq 0$, $\sum y_i = 1$, and $\sum f(y_i) \geq \sum f(x_j)$.

If this is true, by induction we reduce to $n = 2$ (or $n = 1$), and the max is $1/12$.

To prove the key claim, it suffices to show: for any $a, b \geq 0$ with $a + b \leq 1$, $f(a) + f(b) \leq f(a+b) + f(0) = f(a+b)$... no wait, that's the wrong direction. We want to merge variables, so we want $f(a) + f(b) \leq f(a+b)$? No, that would mean merging increases the sum, which is what we want for reduction.

But $f(a) + f(b) \leq f(a+b)$ is NOT true in general. For example, $f(0.5) + f(0.5) = 2 \cdot 1/32 = 1/16 > 0 = f(1)$.

So merging doesn't always help. The reduction approach needs to be more careful.

Let me think differently. 

**Another approach**: We want to show $\sum x_j^4(1-x_j) \leq 1/12$.

Note that $1 - x_j = \sum_{i \neq j} x_i$. So $x_j^4(1-x_j) = x_j^4 \sum_{i \neq j} x_i = \sum_{i \neq j} x_i x_j^4$.

So $\sum_j x_j^4(1-x_j) = \sum_j \sum_{i \neq j} x_i x_j^4 = \sum_{i \neq j} x_i x_j^4$.

This is $\sum_{i \neq j} x_i x_j^4$. By symmetry considerations... hmm, this is $\sum_{j} x_j^4 \sum_{i \neq j} x_i = \sum_j x_j^4(1 - x_j)$, which is what we started with.

Let me try yet another approach. Let's use the method of Lagrange multipliers more carefully to identify all critical points, and then compare.

At a critical point of $\sum f(x_j)$ subject to $\sum x_j = 1$, $x_j \geq 0$:
- For $x_j > 0$: $f'(x_j) = \lambda$, i.e., $x_j^3(4 - 5x_j) = \lambda$.
- For $x_j = 0$: $f'(0) = 0 \geq \lambda$ (KKT condition for maximization: $f'(x_j) \leq \lambda$ at boundary $x_j = 0$... actually for maximization with $x_j \geq 0$, the condition is $f'(x_j) = \lambda$ if $x_j > 0$ and $f'(0) \leq \lambda$ if $x_j = 0$).

Wait, let me be careful. We're maximizing $\sum f(x_j)$ subject to $\sum x_j = 1$ and $x_j \geq 0$. The Lagrangian is $L = \sum f(x_j) - \lambda(\sum x_j - 1) + \sum \mu_j x_j$ where $\mu_j \geq 0$.

KKT: $f'(x_j) - \lambda + \mu_j = 0$, $\mu_j x_j = 0$, $\mu_j \geq 0$.

If $x_j > 0$: $\mu_j = 0$, so $f'(x_j) = \lambda$.
If $x_j = 0$: $\mu_j = \lambda - f'(0) = \lambda \geq 0$, so $\lambda \geq 0$.

So $\lambda \geq 0$ and all positive $x_j$ satisfy $f'(x_j) = \lambda$.

Now, $\phi(x) = f'(x) = x^3(4-5x)$. On $[0,1]$: $\phi(0) = 0$, $\phi(4/5) = 0$, $\phi(1) = -1 < 0$. Max at $x = 3/5$: $\phi(3/5) = 27/125$.

For $\lambda \in (0, 27/125)$: two solutions $a(\lambda) \in (0, 3/5)$ and $b(\lambda) \in (3/5, 4/5)$.
For $\lambda = 0$: solutions $x = 0$ and $x = 4/5$.
For $\lambda = 27/125$: one solution $x = 3/5$.

At a critical point, positive $x_j$'s are either $a$ or $b$ (for some $\lambda$). Say $p$ of them are $a$ and $q$ of them are $b$, with $pa + qb = 1$.

The objective is $p \cdot f(a) + q \cdot f(b)$.

Now I need to maximize over all valid $(p, q, \lambda)$.

This is still complex. Let me try to prove the bound $1/12$ directly.

**Direct proof attempt**: 

We want to show $x^4(1-x) \leq \frac{x(1-x)}{12} \cdot g(x)$ for some function that makes things work out... hmm.

Actually, let me try: $f(x) = x^4(1-x) \leq \frac{x(1-x)}{12}$ for all $x \in [0,1]$?

This requires $x^3 \leq 1/12$ for $x \in (0,1)$, which fails for $x > (1/12)^{1/3} \approx 0.437$.

So that doesn't work either.

Let me try a smarter bound. We want to find constants $\alpha, \beta$ such that:
$$f(x) \leq \alpha x + \beta x(1-x) \quad \forall x \in [0,1]$$

Then $\sum f(x_j) \leq \alpha \sum x_j + \beta \sum x_j(1-x_j) = \alpha + \beta(1 - \sum x_j^2)$.

Now $\sum x_j^2 \geq 1/n$ (by QM-AM or Cauchy-Schwarz), but we need an upper bound on $\sum x_j(1-x_j) = 1 - \sum x_j^2$.

$\sum x_j(1-x_j) = 1 - \sum x_j^2 \leq 1 - 1/n$. But this depends on $n$.

Actually, $\sum x_j^2 \geq (\sum x_j)^2/n = 1/n$, so $\sum x_j(1-x_j) \leq 1 - 1/n \leq 1$ (with equality as $n \to \infty$, but $\sum x_j(1-x_j) < 1$ for finite $n$).

Hmm, but we want a bound that's independent of $n$. $\sum x_j(1-x_j) \leq 1$ always (since $\sum x_j^2 \geq 0$). But this gives $\sum f(x_j) \leq \alpha + \beta$, and we'd need to check if we can get $\alpha + \beta = 1/12$ with $f(x) \leq \alpha x + \beta x(1-x)$.

Actually wait. $\sum x_j(1-x_j) = \sum x_j - \sum x_j^2 = 1 - \sum x_j^2$. And $\sum x_j^2 \leq (\sum x_j)^2 = 1$ (since $x_j \geq 0$). So $\sum x_j(1-x_j) \geq 0$. Also $\sum x_j(1-x_j) \leq 1 - 1/n$.

But the upper bound $\sum x_j(1-x_j) \leq 1$ is too loose (it requires all $x_j \to 0$, but then $\sum x_j = 1$ with $n \to \infty$).

Hmm, I think a cleaner approach is needed. Let me try to use the SOS (sum of squares) or direct inequality approach.

**Key inequality to prove**: For $x_1, \ldots, x_n \geq 0$ with $\sum x_j = 1$:
$$\sum_{j=1}^n x_j^4(1 - x_j) \leq \frac{1}{12}$$

Let me try to prove this by showing $f(x) \leq \frac{x}{12} - c \cdot x(x - a)(x - b)$ for some constants, where the extra term sums to something non-negative.

Actually, let me try a completely different approach. Let me use the fact that $f(x) = x^4 - x^5$ and try to bound each power.

By power mean inequality, $\sum x_j^4 \leq (\sum x_j^2)^2$ (since $x_j \geq 0$). And $\sum x_j^2 \leq 1$.

Also $\sum x_j^5 \leq \sum x_j^4 \cdot \max x_j \leq \sum x_j^4$ (since $x_j \leq 1$).

So $\sum f(x_j) = \sum x_j^4 - \sum x_j^5 \leq \sum x_j^4 \leq (\sum x_j^2)^2$.

But this doesn't directly give $1/12$.

Let me try yet another approach. Let me use the Schur-like inequality or SOS.

Actually, let me revisit the problem. We have $\sum f(x_j) = \sum x_j^4(1-x_j) = \sum x_j^4 \sum_{i \neq j} x_i = \sum_{i \neq j} x_i x_j^4$.

So $\sum f(x_j) = \sum_{i \neq j} x_i x_j^4 = \sum_{i < j} (x_i x_j^4 + x_j x_i^4) = \sum_{i < j} x_i x_j (x_j^3 + x_i^3)$.

Now $x_i^3 + x_j^3 = (x_i + x_j)(x_i^2 - x_i x_j + x_j^2)$.

So $\sum f(x_j) = \sum_{i < j} x_i x_j (x_i + x_j)(x_i^2 - x_i x_j + x_j^2)$.

Let $s_{ij} = x_i + x_j$ and $p_{ij} = x_i x_j$. Then $x_i^2 - x_i x_j + x_j^2 = s_{ij}^2 - 3p_{ij}$.

So $\sum f(x_j) = \sum_{i < j} p_{ij} s_{ij} (s_{ij}^2 - 3p_{ij})$.

This is getting complicated. Let me try a more computational approach.

**Approach via tangent line / supporting hyperplane**:

We want to find a function $h(x) = \alpha x + \beta x^2$ such that $f(x) \leq h(x)$ for all $x \in [0,1]$, and then use $\sum h(x_j) = \alpha + \beta \sum x_j^2$.

Since $\sum x_j^2 \leq \max_j x_j \cdot \sum x_j = \max_j x_j \leq 1$, and also $\sum x_j^2 \geq 1/n$...

Actually, this won't give a clean bound. Let me think about what makes the two-variable case optimal.

In the two-variable case, $x_1 + x_2 = 1$, and the maximum is at $x_1 x_2 = 1/6$ (i.e., $t = 1/6$). The value is $t(1-3t) = 1/12$.

Note that $\sum x_j(1-x_j) = 1 - \sum x_j^2$. For two variables, $\sum x_j(1-x_j) = 2x_1 x_2 = 2t$. At the optimum, $2t = 1/3$.

And $\sum f(x_j) = t(1-3t)$. At $t = 1/6$: $1/6 \cdot (1 - 1/2) = 1/6 \cdot 1/2 = 1/12$.

Interesting. So $\sum f(x_j) = t(1-3t)$ where $t = x_1 x_2$ (for two variables). And $\sum x_j(1-x_j) = 2t$.

So $\sum f(x_j) = \frac{S}{2}(1 - \frac{3S}{2})$ where $S = \sum x_j(1-x_j) = 2t$.

$= \frac{S}{2} - \frac{3S^2}{4}$.

Hmm, this is specific to two variables. For general $n$, the relationship between $\sum f(x_j)$ and $\sum x_j(1-x_j)$ is more complex.

Let me try to find a universal bound of the form $f(x) \leq A x(1-x) + B x(1-x) \cdot x$ or something.

Actually, $f(x) = x^4(1-x) = x^3 \cdot x(1-x)$. And $x^3 \leq ?$ on $[0,1]$.

Hmm. Let me try the approach: find the best quadratic upper bound of the form $f(x) \leq ax^2 + bx + c$ such that when summed, we get something useful.

$\sum f(x_j) \leq a \sum x_j^2 + b \sum x_j + nc = a \sum x_j^2 + b + nc$.

This depends on $n$, which is bad.

OK let me try a totally different approach. Let me try to prove the inequality directly using SOS or AM-GM type arguments.

**Claim**: $\sum_{j=1}^n x_j^4(1 - x_j) \leq \frac{1}{12}$ when $\sum x_j = 1$, $x_j \geq 0$.

**Proof idea**: We use the identity $1 - x_j = \sum_{i \neq j} x_i$.

$\sum_j x_j^4(1-x_j) = \sum_{j} x_j^4 \sum_{i \neq j} x_i = \sum_{i \neq j} x_i x_j^4 = \sum_{i < j} (x_i x_j^4 + x_j x_i^4) = \sum_{i<j} x_i x_j(x_i^3 + x_j^3)$.

Now, $x_i^3 + x_j^3 \leq (x_i + x_j)^3$ (since $x_i, x_j \geq 0$, actually $x_i^3 + x_j^3 \leq (x_i + x_j)^3$ because $(x_i+x_j)^3 = x_i^3 + 3x_i^2 x_j + 3x_i x_j^2 + x_j^3 \geq x_i^3 + x_j^3$).

So $\sum f(x_j) \leq \sum_{i<j} x_i x_j (x_i + x_j)^3$.

But I'm not sure this helps directly.

Let me try another substitution. Let $S = \sum x_j(1-x_j) = 1 - \sum x_j^2$. Note $0 \leq S \leq 1 - 1/n < 1$.

We have $\sum f(x_j) = \sum x_j^4(1-x_j) = \sum x_j^3 \cdot x_j(1-x_j)$.

By the constraint, $x_j \leq 1$, so $x_j^3 \leq 1$, giving $\sum f(x_j) \leq \sum x_j(1-x_j) = S \leq 1$. Too loose.

Better: $x_j^3 \leq x_j^2$ (since $x_j \leq 1$), so $\sum f(x_j) \leq \sum x_j^2(1-x_j) = \sum x_j^2 - \sum x_j^3$.

Hmm, still not directly useful.

Let me try to use the method of proving the inequality by finding the right "SOS certificate."

We want: $\frac{1}{12} - \sum x_j^4(1-x_j) \geq 0$ given $\sum x_j = 1$, $x_j \geq 0$.

Substituting $\sum x_j = 1$:

$\frac{1}{12} - \sum x_j^4 + \sum x_j^5 = \frac{(\sum x_j)^4}{12} - \sum x_j^4 + \sum x_j^5$... no, $(\sum x_j)^4 \neq$ simply related.

Hmm. Let me try a specific approach for the two-variable case and then show reduction.

Actually, let me try to prove it by showing that the maximum over all $n$ is achieved at $n = 2$.

**Reduction argument**: Given $n \geq 3$ variables $x_1, \ldots, x_n \geq 0$ with $\sum x_j = 1$, we show we can merge two of them (or set one to 0) without decreasing $\sum f(x_j)$, eventually reducing to $n \leq 2$.

Specifically, we want to show: among any three non-negative variables $a, b, c$ with $a + b + c = s$ (where $s \leq 1$), we can replace them with two variables $a', b'$ with $a' + b' = s$ such that $f(a') + f(b') \geq f(a) + f(b) + f(c)$.

Hmm, but this isn't quite right because we need to account for the rest of the variables too.

Actually, the reduction is: given $x_1, \ldots, x_n$ with $n \geq 3$, pick two variables, say $x_1$ and $x_2$, and replace them with a single variable $x_1 + x_2$ (setting the other to 0). This reduces $n$ by 1. We need $f(x_1 + x_2) \geq f(x_1) + f(x_2)$ for some pair.

But as we noted, this isn't always true. $f(0.5) + f(0.5) > f(1) = 0$.

Alternatively, we can split: given $x_1, \ldots, x_n$, replace two variables $x_1, x_2$ with two new variables $y_1, y_2$ with $y_1 + y_2 = x_1 + x_2$ and $f(y_1) + f(y_2) \geq f(x_1) + f(x_2)$. This keeps $n$ the same but moves toward the optimal two-variable split.

This is essentially saying: for fixed $s = x_1 + x_2$, the maximum of $f(y_1) + f(y_2)$ over $y_1 + y_2 = s$, $y_1, y_2 \geq 0$ is achieved at the optimal split. And we need to show that the optimal split of $s$ gives at least as much as $f(x_1) + f(x_2)$.

Well, that's trivially true by definition of "optimal." But the issue is that the optimal split of $s$ might not be the global optimum.

Let me think about this more carefully. The global problem is: maximize $\sum f(x_j)$ subject to $\sum x_j = 1$, $x_j \geq 0$. 

For any fixed number of nonzero variables $k$ and fixed values, we can optimize the split. But the question is what $k$ is optimal.

Let me parameterize: suppose we use $k$ nonzero variables. We want to maximize $\sum_{j=1}^k f(x_j)$ subject to $\sum x_j = 1$, $x_j > 0$.

For $k = 1$: $f(1) = 0$.
For $k = 2$: max is $1/12$ (as computed).
For $k = 3$: we need to check.
For general $k$: we need to check.

For $k = 2$, the optimum is at $x_1 x_2 = 1/6$, $x_1 + x_2 = 1$.

For general $k$, by KKT, all positive $x_j$ satisfy $\phi(x_j) = \lambda$ where $\phi(x) = x^3(4-5x)$. Since $\phi$ is not monotone, there can be at most two distinct values among the $x_j$'s: $a$ and $b$ with $a < 3/5 < b$.

So the optimum for $k$ variables has $p$ copies of $a$ and $q = k - p$ copies of $b$, with $pa + qb = 1$ and $\phi(a) = \phi(b)$.

The objective is $p \cdot f(a) + q \cdot f(b)$.

Let me denote $F(p, q) = p \cdot f(a) + q \cdot f(b)$ where $a, b$ are determined by $pa + qb = 1$ and $\phi(a) = \phi(b)$.

For $p = 1, q = 1$ ($k = 2$): $a + b = 1$, $\phi(a) = \phi(b)$. We found $a(1-a) = 1/6$, giving $F = 1/12$.

For $p = 1, q = 0$ ($k = 1$): $a = 1$, $F = f(1) = 0$.

For $p = 0, q = 1$ ($k = 1$): $b = 1$, $F = f(1) = 0$.

For $p = 2, q = 0$ ($k = 2$, both equal): $a = 1/2$, $F = 2f(1/2) = 1/16$.

For $p = 0, q = 2$ ($k = 2$, both equal): $b = 1/2$, but $\phi(1/2) = (1/8)(3/2) = 3/16$. This is a valid critical point only if both are $b = 1/2$, but $1/2 < 3/5$, so this is actually in the convex region. $F = 2f(1/2) = 1/16$. Same as above.

For $p = 1, q = 2$ ($k = 3$): $a + 2b = 1$, $\phi(a) = \phi(b)$. We computed this gives approximately $F \approx 0.0819$.

For $p = 2, q = 1$ ($k = 3$): $2a + b = 1$, $\phi(a) = \phi(b)$. Let me compute.

$b = 1 - 2a$, $\phi(a) = \phi(1-2a)$.
$a^3(4-5a) = (1-2a)^3(4-5(1-2a)) = (1-2a)^3(10a-1)$.

For $b > 3/5$: $1 - 2a > 3/5 \Rightarrow a < 1/5$. And $b < 4/5$: $a > 1/10$.

$a = 0.15$: LHS = $0.003375 \cdot 3.25 = 0.01097$. RHS = $0.7^3 \cdot 0.5 = 0.1715$. RHS >> LHS.

$a = 0.12$: LHS = $0.001728 \cdot 3.4 = 0.005875$. RHS = $0.76^3 \cdot 0.2 = 0.438976 \cdot 0.2 = 0.0878$. Still RHS >> LHS.

$a = 0.105$: LHS = $0.001158 \cdot 3.475 = 0.00402$. RHS = $0.79^3 \cdot 0.05 = 0.493039 \cdot 0.05 = 0.02465$. Still RHS > LHS.

$a = 0.101$: LHS = $0.001031 \cdot 3.495 = 0.003603$. RHS = $0.798^3 \cdot 0.01 = 0.508 \cdot 0.01 = 0.00508$. RHS > LHS.

$a = 0.1005$: LHS = $0.001015 \cdot 3.4975 = 0.003550$. RHS = $0.799^3 \cdot 0.005 = 0.510 \cdot 0.005 = 0.002550$. LHS > RHS.

So $a \approx 0.1008$. $b \approx 0.7984$.

$F = 2f(a) + f(b) = 2 \cdot (0.1008)^4 \cdot 0.8992 + (0.7984)^4 \cdot 0.2016$.

$f(a) \approx 0.0000103 \cdot 0.8992 \approx 0.00000927$. $2f(a) \approx 0.0000185$.
$f(b) \approx 0.4065 \cdot 0.2016 \approx 0.08195$.
$F \approx 0.08197$.

This is the same as the $p=1, q=2$ case (by symmetry of the equation, just swapping $a$ and $b$ roles). Actually no, $p=2, q=1$ means 2 small and 1 large, while $p=1, q=2$ means 1 small and 2 large. But 2 large would require $2b < 1$, i.e., $b < 1/2$, contradicting $b > 3/5$. So $p=1, q=2$ is infeasible (can't have 2 variables in the concave region with sum 1). 

So for $k = 3$, the only mixed critical point is $p = 2, q = 1$ (2 small, 1 large), giving $F \approx 0.082 < 1/12$.

And the symmetric critical point ($p = 3, q = 0$, all equal to $1/3$) gives $F = 2/81 \approx 0.0247$.

So for $k = 3$, the max is $\approx 0.082 < 1/12$.

For larger $k$, the analysis is similar: we can have at most 1 variable in the concave region (since 2 would require sum > 6/5 > 1), so $q \leq 1$. With $q = 1$ and $p = k-1$:

$(k-1)a + b = 1$, $\phi(a) = \phi(b)$, $F = (k-1)f(a) + f(b)$.

As $k$ increases, $a \to 0$ and $b \to 1$... wait, $b < 4/5$, so $(k-1)a = 1 - b > 1/5$, meaning $a > \frac{1}{5(k-1)}$. As $k \to \infty$, $a \to 0$ and $b \to 1$... no, $b < 4/5$. Actually $b$ is determined by $\phi(b) = \phi(a)$, and as $a \to 0$, $\phi(a) \to 0$, so $\phi(b) \to 0$, meaning $b \to 4/5$ (the other root of $\phi = 0$ besides 0).

So as $k \to \infty$: $b \to 4/5$, $a \to 0$, $(k-1)a \to 1/5$.

$F \to f(4/5) + (k-1) \cdot f(a)$ where $a \to 0$ and $(k-1) \to \infty$ but $(k-1)a \to 1/5$.

$f(a) \approx a^4$ for small $a$, so $(k-1) f(a) \approx (k-1) a^4 = \frac{((k-1)a)^4}{(k-1)^3} \to 0$ as $k \to \infty$.

So $F \to f(4/5) = (4/5)^4 (1/5) = 256/3125 \approx 0.08192$.

And for $k = 2$: $F = 1/12 \approx 0.08333$.
For $k = 3$: $F \approx 0.08197$.
For $k \to \infty$: $F \to 0.08192$.

So $k = 2$ gives the maximum, and the maximum is $1/12$.

Now I need to prove this rigorously. Let me prove that for all $k \geq 2$ and all configurations, $\sum f(x_j) \leq 1/12$.

**Proof strategy**: Show that $f(x) \leq \frac{x(1-x)}{12} + \frac{x^2(1-x)^2}{4}$ or some similar bound that, when summed, gives $\leq 1/12$.

Actually, let me try to find a bound of the form $f(x) \leq \alpha \cdot x(1-x)$ for all $x \in [0,1]$, and then use $\sum x_j(1-x_j) \leq$ something.

$f(x) / (x(1-x)) = x^3$ for $x \in (0,1)$. This is unbounded as $x \to 1$. So no constant $\alpha$ works.

What about $f(x) \leq \alpha \cdot x(1-x) + \beta \cdot x^2(1-x)^2$?

$f(x) = x^4(1-x)$, $x(1-x) = x - x^2$, $x^2(1-x)^2 = x^2 - 2x^3 + x^4$.

$\alpha(x - x^2) + \beta(x^2 - 2x^3 + x^4) = \alpha x + (\beta - \alpha) x^2 - 2\beta x^3 + \beta x^4$.

We need $x^4 - x^5 \leq \alpha x + (\beta - \alpha) x^2 - 2\beta x^3 + \beta x^4$ for all $x \in [0,1]$.

$0 \leq \alpha x + (\beta - \alpha) x^2 - 2\beta x^3 + (\beta - 1) x^4 + x^5$.

This is a polynomial inequality on $[0,1]$. We want to find $\alpha, \beta$ such that this holds, and then $\sum f(x_j) \leq \alpha \sum x_j(1-x_j) + \beta \sum x_j^2(1-x_j)^2$.

Now, $\sum x_j(1-x_j) = 1 - \sum x_j^2$ and $\sum x_j^2(1-x_j)^2 = \sum x_j^2 - 2\sum x_j^3 + \sum x_j^4$.

This is getting complicated. Let me try a different approach entirely.

**Approach: Prove the inequality $\sum x_j^4(1-x_j) \leq 1/12$ using the SOS method with the constraint $\sum x_j = 1$.**

We want to show: $\frac{1}{12} - \sum x_j^4(1-x_j) \geq 0$ when $\sum x_j = 1$, $x_j \geq 0$.

Using $\sum x_j = 1$, we can write $\frac{1}{12} = \frac{(\sum x_j)^2}{12}$... hmm, or use $\frac{1}{12} = \frac{1}{12}(\sum x_j)^k$ for appropriate $k$.

Actually, let me try to prove it for $n = 2$ first and then show reduction.

For $n = 2$: $x + y = 1$, $x, y \geq 0$. We showed $f(x) + f(y) = t(1-3t)$ where $t = xy \in [0, 1/4]$. The function $t - 3t^2$ has max at $t = 1/6$ with value $1/12$. Since $1/6 < 1/4$, this is achievable. And $t - 3t^2 \leq 1/12$ for all $t$ (since the max of $t - 3t^2$ is $1/12$). So for $n = 2$, $\sum f \leq 1/12$. ✓

For general $n$: We need to show $\sum f(x_j) \leq 1/12$.

**Key lemma**: For any $a, b \geq 0$ with $a + b \leq 1$, $f(a) + f(b) \leq f(a+b) + \frac{(a+b)a b}{6} \cdot 3$... hmm, I'm not finding the right form.

Let me try to prove: for $a, b \geq 0$ with $s = a + b \leq 1$:
$$f(a) + f(b) \leq f(s) + s \cdot g(a, b)$$
where $g$ is something that helps.

Actually, let me try: $f(a) + f(b) \leq f(a + b) + \frac{ab(a+b)}{6}$... let me check.

$f(a) + f(b) = a^4(1-a) + b^4(1-b)$.
$f(a+b) = (a+b)^4(1-a-b)$.
$f(a+b) - f(a) - f(b) = (a+b)^4(1-a-b) - a^4(1-a) - b^4(1-b)$.

Let me expand with $s = a+b$, $p = ab$:
$a^4 + b^4 = s^4 - 4s^2 p + 2p^2$.
$a^5 + b^5 = s^5 - 5s^3 p + 5sp^2$.

$f(a) + f(b) = (a^4 + b^4) - (a^5 + b^5) = (s^4 - 4s^2 p + 2p^2) - (s^5 - 5s^3 p + 5sp^2)$
$= s^4(1-s) - 4s^2 p + 5s^3 p + 2p^2 - 5sp^2$
$= f(s) + p(-4s^2 + 5s^3) + p^2(2 - 5s)$
$= f(s) + ps^2(5s - 4) + p^2(2 - 5s)$.

So $f(a) + f(b) = f(s) + ps^2(5s-4) + p^2(2-5s)$ where $s = a+b$, $p = ab$.

For $s \leq 4/5$: $5s - 4 \leq 0$, so $ps^2(5s-4) \leq 0$. And $2 - 5s \geq 0$ (for $s \leq 2/5$) or $2 - 5s < 0$ (for $s > 2/5$).

Case $s \leq 2/5$: Both $ps^2(5s-4) \leq 0$ and $p^2(2-5s) \geq 0$. So $f(a) + f(b) = f(s) + (\text{negative}) + (\text{positive})$. Unclear.

Case $2/5 < s \leq 4/5$: $ps^2(5s-4) \leq 0$ (since $5s - 4 \leq 0$) and $p^2(2-5s) \leq 0$ (since $2 - 5s < 0$). So $f(a) + f(b) \leq f(s)$. This means merging increases the sum!

Case $s > 4/5$: $5s - 4 > 0$ and $2 - 5s < 0$. So $ps^2(5s-4) \geq 0$ and $p^2(2-5s) \leq 0$. Unclear.

So for $2/5 < s \leq 4/5$, merging two variables into one increases the sum. This is useful!

Now, in our problem, $\sum x_j = 1$. If we have $n \geq 3$ variables, can we always find two whose sum is in $(2/5, 4/5]$?

If all pairs have sum $> 4/5$, then any two variables sum to $> 4/5$. With $n \geq 3$, the two smallest variables $x_{(1)} + x_{(2)} \leq 2/3 < 4/5$... wait, $2/3 \approx 0.667 < 0.8 = 4/5$. So $x_{(1)} + x_{(2)} \leq 2/3 < 4/5$. But we also need $x_{(1)} + x_{(2)} > 2/5 = 0.4$.

If $x_{(1)} + x_{(2)} \leq 2/5$, then the remaining $n - 2$ variables sum to $\geq 3/5$. But $x_{(1)} \leq x_{(2)} \leq \ldots$, so $x_{(3)} \geq x_{(2)} \geq x_{(1)}$, and $x_{(1)} + x_{(2)} \leq 2/5$ means $x_{(2)} \leq 1/5$ (since $x_{(1)} \leq x_{(2)}$). Then all variables $\leq 1/5$... no, $x_{(3)}$ could be large.

Hmm, this is getting complicated. Let me think about whether we can always reduce.

Actually, the key insight is: for $s \in (2/5, 4/5]$, merging is beneficial. For $s \leq 2/5$ or $s > 4/5$, it's not clear.

But we can also split. For $s > 4/5$, we might want to split a large variable.

Let me think about this differently. The maximum is at $n = 2$ with $x_1 + x_2 = 1$ and $x_1 x_2 = 1/6$. The two values are $a = \frac{1 - 1/\sqrt{3}}{2} \approx 0.211$ and $b = \frac{1 + 1/\sqrt{3}}{2} \approx 0.789$.

Note $a \approx 0.211 < 2/5 = 0.4$ and $b \approx 0.789 \in (2/5, 4/5]$. So $b$ is in the "merging is beneficial" range, and $a$ is not.

Let me try a cleaner approach. I'll prove the inequality by finding a suitable upper bound.

**Approach: Find $\alpha, \beta$ such that $f(x) \leq \alpha x + \beta x^2$ for all $x \in [0,1]$, and $\alpha + \beta \cdot (\text{max of } \sum x_j^2) = 1/12$.**

We have $\sum x_j^2 \leq \max_j x_j \leq 1$. But also $\sum x_j^2 \geq 1/n$.

Actually, we need an upper bound on $\alpha + \beta \sum x_j^2$. If $\beta < 0$, then $\alpha + \beta \sum x_j^2 \leq \alpha + \beta / n$ (using $\sum x_j^2 \geq 1/n$). But this depends on $n$.

If $\beta > 0$, then $\alpha + \beta \sum x_j^2 \leq \alpha + \beta$ (using $\sum x_j^2 \leq 1$). So we need $\alpha + \beta = 1/12$ and $f(x) \leq \alpha x + \beta x^2$ for all $x \in [0,1]$.

With $\beta = 1/12 - \alpha$, we need $x^4(1-x) \leq \alpha x + (1/12 - \alpha) x^2$ for all $x \in [0,1]$.

Dividing by $x$ (for $x > 0$): $x^3(1-x) \leq \alpha + (1/12 - \alpha) x$.

Let $h(x) = x^3(1-x) = x^3 - x^4$. We need $h(x) \leq \alpha + (1/12 - \alpha) x$ for all $x \in [0,1]$.

$h(0) = 0 \leq \alpha$. So $\alpha \geq 0$.
$h(1) = 0 \leq \alpha + (1/12 - \alpha) = 1/12$. ✓

The line $\ell(x) = \alpha + (1/12 - \alpha) x$ must be above $h(x)$ on $[0,1]$.

$h$ has max $27/256 \approx 0.1055$ at $x = 3/4$.

$\ell(3/4) = \alpha + (1/12 - \alpha)(3/4) = \alpha(1 - 3/4) + (1/12)(3/4) = \alpha/4 + 1/16$.

We need $\alpha/4 + 1/16 \geq 27/256$, i.e., $\alpha/4 \geq 27/256 - 16/256 = 11/256$, i.e., $\alpha \geq 11/64$.

With $\alpha = 11/64$, $\beta = 1/12 - 11/64 = (64 - 132)/(12 \cdot 64) = -68/768 = -17/192$.

So $\beta < 0$! This means $\sum f(x_j) \leq \alpha + \beta \sum x_j^2 \leq \alpha + \beta \cdot (1/n)$ (since $\beta < 0$ and $\sum x_j^2 \geq 1/n$).

$\alpha + \beta/n = 11/64 - 17/(192n)$. For $n = 1$: $11/64 - 17/192 = 33/192 - 17/192 = 16/192 = 1/12$. ✓
For $n = 2$: $11/64 - 17/384 = 66/384 - 17/384 = 49/384 \approx 0.1276 > 1/12$. ✗

So this bound gives $49/384$ for $n = 2$, which is larger than $1/12$. Not tight enough.

The issue is that the linear-quadratic bound is too loose. Let me try a cubic bound.

$f(x) \leq \alpha x + \beta x^2 + \gamma x^3$ with $\alpha + \beta + \gamma = 1/12$ (using $\sum x_j^3 \leq 1$ and $\sum x_j^2 \leq 1$).

Actually, $\sum x_j^3 \leq (\sum x_j^2)(\max x_j) \leq \sum x_j^2 \leq 1$. And $\sum x_j^3 \leq \sum x_j^2 \leq 1$.

If $\gamma < 0$: $\sum f(x_j) \leq \alpha + \beta \sum x_j^2 + \gamma \sum x_j^3 \leq \alpha + \beta + \gamma$ (if $\beta > 0, \gamma < 0$, using $\sum x_j^2 \leq 1$ and $\sum x_j^3 \geq 0$... no, $\gamma < 0$ means we need lower bound on $\sum x_j^3$).

This is getting complicated. Let me try a completely different approach.

**Approach: Use the concave envelope / convexity argument directly.**

We showed that for $s = a + b \in (2/5, 4/5]$, $f(a) + f(b) \leq f(s)$, i.e., merging is beneficial.

Also, $f(a) + f(b) = f(s) + ps^2(5s-4) + p^2(2-5s)$ where $p = ab$.

For $s \in (2/5, 4/5]$: $5s - 4 \leq 0$ and $2 - 5s < 0$, so both terms are $\leq 0$, confirming $f(a) + f(b) \leq f(s)$.

For $s \leq 2/5$: $5s - 4 < 0$ and $2 - 5s \geq 0$. So $f(a) + f(b) = f(s) + ps^2(5s-4) + p^2(2-5s)$. The first extra term is negative, the second is non-negative. The net effect depends on $p$.

For $s > 4/5$: $5s - 4 > 0$ and $2 - 5s < 0$. So the first extra term is positive, the second is negative.

Now, here's my strategy for the proof:

**Step 1**: Show that the maximum is achieved at a critical point (by compactness).

**Step 2**: At any critical point, all positive $x_j$ take at most two distinct values $a$ and $b$ with $\phi(a) = \phi(b)$.

**Step 3**: Show that the optimal critical point has exactly 2 positive variables (one $a$ and one $b$), and compute the value $1/12$.

For Step 3, I need to show that having more than 2 positive variables doesn't help. 

Let me think about this more carefully. At a critical point with $p$ copies of $a$ and $q$ copies of $b$ ($p + q = k$, $pa + qb = 1$, $\phi(a) = \phi(b) = \lambda$):

$F = p \cdot f(a) + q \cdot f(b)$.

We need to show $F \leq 1/12$ for all valid $(p, q, a, b)$.

Since $q \leq 1$ (at most one variable can be $> 3/5$ because $2 \cdot 3/5 = 6/5 > 1$), we have $q \in \{0, 1\}$.

Case $q = 0$: All $k$ variables equal to $a = 1/k$. $F = k \cdot f(1/k) = k \cdot (1/k)^4(1 - 1/k) = (k-1)/k^4$. 

$g(k) = (k-1)/k^4$. $g(1) = 0$, $g(2) = 1/16$, $g(3) = 2/81$, etc. Max at $k = 2$: $g(2) = 1/16 < 1/12$. ✓

Case $q = 1$, $p = k - 1 \geq 1$: $(k-1)a + b = 1$, $\phi(a) = \phi(b)$, $a < 3/5 < b < 4/5$.

$F = (k-1) f(a) + f(b)$.

For $k = 2$ ($p = 1, q = 1$): $a + b = 1$, $\phi(a) = \phi(b)$. We showed $F = 1/12$.

For $k \geq 3$ ($p \geq 2, q = 1$): We need to show $F < 1/12$.

Let me try to prove this. With $p = k-1$ copies of $a$ and 1 copy of $b$:

$(k-1)a + b = 1$, so $b = 1 - (k-1)a$.
$\phi(a) = \phi(b)$: $a^3(4-5a) = b^3(4-5b)$.

$F = (k-1) a^4(1-a) + b^4(1-b)$.

Since $b = 1 - (k-1)a$ and $1 - b = (k-1)a$:
$F = (k-1) a^4(1-a) + (1-(k-1)a)^4 (k-1)a = (k-1)a [a^3(1-a) + (1-(k-1)a)^4]$.

Hmm, this is complex. Let me try a different approach to prove the bound.

**Approach: Prove $\sum f(x_j) \leq 1/12$ by a direct inequality.**

Let me try to find a function $g(x)$ such that $f(x) \leq g(x)$ for all $x \in [0,1]$, and $\sum g(x_j) \leq 1/12$ when $\sum x_j = 1$.

The natural candidate is $g(x) = cx(1-x)$ for some $c$, but $f(x)/(x(1-x)) = x^3$ which is unbounded.

What about $g(x) = cx(1-x)(1 - dx)$ for some $c, d$? Then $\sum g(x_j) = c \sum x_j(1-x_j)(1-dx_j) = c[\sum x_j - (1+d)\sum x_j^2 + d \sum x_j^3]$.

$= c[1 - (1+d) S_2 + d S_3]$ where $S_2 = \sum x_j^2$, $S_3 = \sum x_j^3$.

We need this to be $\leq 1/12$ for all valid $(S_2, S_3)$. And $f(x) \leq g(x)$ for all $x$.

$f(x) = x^4(1-x) = x^4 - x^5$.
$g(x) = cx(1-x)(1-dx) = c(x - (1+d)x^2 + dx^3)$.

We need $x^4 - x^5 \leq c(x - (1+d)x^2 + dx^3)$ for all $x \in [0,1]$.

Dividing by $x$ (for $x > 0$): $x^3 - x^4 \leq c(1 - (1+d)x + dx^2) = c(1-x)(1-dx/(1-x) \cdot ...)$... hmm, let me just write it as $x^3(1-x) \leq c(1 - (1+d)x + dx^2)$.

Note $1 - (1+d)x + dx^2 = (1-x)(1-dx)$. So we need $x^3(1-x) \leq c(1-x)(1-dx)$, i.e., $x^3 \leq c(1-dx)$ for $x \in [0,1)$ (and by continuity, $x \in [0,1]$).

So we need $x^3 \leq c(1 - dx)$ for all $x \in [0,1]$.

If $d \geq 0$: $c(1-dx) \geq c(1-d)$ for $x \in [0,1]$. We need $x^3 \leq c(1-dx)$, i.e., $c \geq \frac{x^3}{1-dx}$.

If $d < 1$: $1 - dx > 0$ for $x \in [0,1]$, so we need $c \geq \max_{x \in [0,1]} \frac{x^3}{1-dx}$.

Let $r(x) = \frac{x^3}{1-dx}$. $r'(x) = \frac{3x^2(1-dx) + dx^3}{(1-dx)^2} = \frac{x^2(3 - 2dx)}{(1-dx)^2}$.

$r'(x) = 0$ at $x = 0$ or $x = \frac{3}{2d}$ (if $d > 0$ and $\frac{3}{2d} \leq 1$, i.e., $d \geq 3/2$).

If $0 < d < 3/2$: $r'(x) > 0$ for $x \in (0,1]$, so max at $x = 1$: $r(1) = \frac{1}{1-d}$. So $c \geq \frac{1}{1-d}$.

If $d \geq 3/2$: max at $x = \frac{3}{2d}$: $r(3/(2d)) = \frac{(3/(2d))^3}{1 - d \cdot 3/(2d)} = \frac{27/(8d^3)}{1 - 3/2} = \frac{27/(8d^3)}{-1/2} = -\frac{27}{4d^3}$. But this is negative, which means $1 - dx < 0$ at this point, so $r$ is negative. We need $d < 1$ for $1 - dx > 0$ on $[0,1]$.

Wait, I assumed $d < 1$ above. Let me reconsider.

If $d < 1$: $1 - dx > 0$ for $x \in [0,1]$. Max of $r(x) = x^3/(1-dx)$ on $[0,1]$:
- If $d \leq 3/2$ (which includes $d < 1$): $r$ is increasing on $[0,1]$, max at $x=1$: $r(1) = 1/(1-d)$.
- So $c \geq 1/(1-d)$.

With $c = 1/(1-d)$, we have $f(x) \leq g(x) = \frac{x(1-x)(1-dx)}{1-d}$.

Now, $\sum g(x_j) = \frac{1}{1-d} \sum x_j(1-x_j)(1-dx_j) = \frac{1}{1-d}[1 - (1+d)S_2 + d S_3]$.

We need to maximize $1 - (1+d)S_2 + dS_3$ subject to $\sum x_j = 1$, $x_j \geq 0$.

Note $S_3 \leq S_2$ (since $x_j \leq 1$) and $S_3 \geq S_2^2$ (by power mean... actually $S_3 \geq S_2^2 / S_1 = S_2^2$ by Cauchy-Schwarz: $(\sum x_j^2)^2 \leq (\sum x_j)(\sum x_j^3) = S_3$). Wait, that gives $S_3 \geq S_2^2$.

Also $S_2 \geq 1/n$ and $S_2 \leq 1$.

We want to maximize $h = 1 - (1+d)S_2 + dS_3$. 

If $d > 0$: $h$ increases with $S_3$ and decreases with $S_2$. Since $S_3 \leq S_2$ (because $x_j^3 \leq x_j^2$ for $x_j \in [0,1]$), we have $h \leq 1 - (1+d)S_2 + dS_2 = 1 - S_2 \leq 1 - 1/n$.

So $\sum g(x_j) \leq \frac{1 - 1/n}{1-d}$. For this to be $\leq 1/12$, we need $\frac{1 - 1/n}{1-d} \leq 1/12$, i.e., $1 - d \geq 12(1 - 1/n)$, i.e., $d \leq 1 - 12 + 12/n = -11 + 12/n$. For $n = 2$: $d \leq -5$. For $n = 3$: $d \leq -7$. These are very negative, and we assumed $d < 1$ but also need $d$ such that the bound works.

With $d < 0$ (say $d = -5$ for $n = 2$): $c = 1/(1-(-5)) = 1/6$. $g(x) = \frac{x(1-x)(1+5x)}{6}$.

$\sum g(x_j) = \frac{1}{6}[1 - (1+(-5))S_2 + (-5)S_3] = \frac{1}{6}[1 + 4S_2 - 5S_3]$.

For $n = 2$: $S_2 = x^2 + (1-x)^2 = 1 - 2x(1-x)$, $S_3 = x^3 + (1-x)^3 = 1 - 3x(1-x)$.

$\sum g = \frac{1}{6}[1 + 4(1-2t) - 5(1-3t)] = \frac{1}{6}[1 + 4 - 8t - 5 + 15t] = \frac{1}{6}[7t] = \frac{7t}{6}$ where $t = x(1-x)$.

Max at $t = 1/4$: $7/24 \approx 0.292$. Way more than $1/12$. So this bound is too loose.

The problem is that $g(x) \geq f(x)$ is too loose when $d$ is very negative.

I think the issue is that a simple polynomial bound won't work cleanly. Let me try a different strategy.

**Strategy: Prove the result by first handling $n = 2$, then showing that for $n \geq 3$, the sum is at most the $n = 2$ maximum.**

For $n = 2$: Already proved, max is $1/12$.

For $n \geq 3$: We use the merging lemma. We showed that for $s = a + b \in (2/5, 4/5]$, $f(a) + f(b) \leq f(s)$. So if we can find two variables whose sum is in $(2/5, 4/5]$, we can merge them and increase the sum, reducing to $n-1$ variables.

**Claim**: For $n \geq 3$ with $\sum x_j = 1$, $x_j \geq 0$, there exist two variables whose sum is in $(2/5, 4/5]$.

Proof: Order $x_1 \leq x_2 \leq \ldots \leq x_n$. Consider $x_1 + x_2$ (smallest pair sum) and $x_{n-1} + x_n$ (largest pair sum).

$x_1 + x_2 \leq 2/n \leq 2/3$ (for $n \geq 3$). And $x_{n-1} + x_n \geq 2/n$.

If $x_1 + x_2 > 2/5$: then $x_1 + x_2 \in (2/5, 2/3] \subseteq (2/5, 4/5]$. Done.

If $x_1 + x_2 \leq 2/5$: Then $x_3 + \ldots + x_n \geq 3/5$. Consider $x_{n-1} + x_n$. We have $x_{n-1} + x_n \geq 2(x_3 + \ldots + x_n)/(n-2) \geq 2 \cdot 3/5 / (n-2) = 6/(5(n-2))$.

For $n = 3$: $x_2 + x_3 = 1 - x_1 \geq 1 - 1/3 = 2/3$ (since $x_1 \leq 1/3$ as $x_1 \leq x_2 \leq x_3$ and $x_1 + x_2 + x_3 = 1$). And $x_2 + x_3 \leq 1$ (since $x_1 \geq 0$). But we need $x_2 + x_3 \leq 4/5$, which requires $x_1 \geq 1/5$.

If $x_1 < 1/5$: $x_2 + x_3 > 4/5$. Can we merge $x_1$ with $x_2$? $x_1 + x_2 \leq 2/5$ (by assumption). So $x_1 + x_2 \leq 2/5$, which is NOT in $(2/5, 4/5]$.

Hmm, so if $x_1 + x_2 \leq 2/5$ and $x_2 + x_3 > 4/5$, we can't directly merge any pair.

In this case, $x_1 \leq 1/5$ and $x_2 + x_3 > 4/5$, $x_1 + x_2 \leq 2/5$.

Let me consider merging $x_1$ and $x_3$: $x_1 + x_3$. We have $x_1 + x_3 = 1 - x_2$. And $x_2 \leq x_3$, $x_1 + x_2 \leq 2/5$ so $x_2 \leq 2/5 - x_1$. Also $x_2 + x_3 > 4/5$ so $x_3 > 4/5 - x_2 \geq 4/5 - (2/5 - x_1) = 2/5 + x_1$.

$x_1 + x_3 > x_1 + 2/5 + x_1 = 2/5 + 2x_1$. And $x_1 + x_3 = 1 - x_2 < 1 - 0 = 1$.

$x_1 + x_3 = 1 - x_2$. Since $x_2 \geq x_1 \geq 0$ and $x_1 + x_2 \leq 2/5$: $x_2 \leq 2/5$, so $x_1 + x_3 \geq 3/5$. And $x_2 \geq x_1$, $x_2 \geq (x_1 + x_2)/2 \geq 0$... Actually $x_2 \geq x_1$ and $x_1 + x_2 \leq 2/5$ means $x_2 \leq 2/5$ (since $x_1 \geq 0$). So $x_1 + x_3 = 1 - x_2 \geq 3/5$.

And $x_1 + x_3 = 1 - x_2 \leq 1 - x_1$ (since $x_2 \geq x_1$). With $x_1 \leq 1/5$: $x_1 + x_3 \leq 1 - 0 = 1$. But we need $\leq 4/5$: $x_1 + x_3 \leq 4/5$ iff $x_2 \geq 1/5$.

If $x_2 \geq 1/5$: $x_1 + x_3 = 1 - x_2 \leq 4/5$ and $x_1 + x_3 \geq 3/5 > 2/5$. So $x_1 + x_3 \in (2/5, 4/5]$. Done!

If $x_2 < 1/5$: Then $x_1 \leq x_2 < 1/5$, so $x_1 + x_2 < 2/5$ (consistent). And $x_3 = 1 - x_1 - x_2 > 1 - 2/5 = 3/5$.

Now $x_3 > 3/5$ and $x_1, x_2 < 1/5$. We can try merging $x_1$ and $x_2$: $x_1 + x_2 < 2/5$, not in the range.

We can try merging $x_1$ and $x_3$: $x_1 + x_3 = 1 - x_2 > 4/5$ (since $x_2 < 1/5$). Not in the range.

We can try merging $x_2$ and $x_3$: $x_2 + x_3 = 1 - x_1 > 4/5$ (since $x_1 < 1/5$). Not in the range.

So for $n = 3$ with $x_1 \leq x_2 < 1/5 < 3/5 < x_3$, no pair has sum in $(2/5, 4/5]$.

In this case, we need a different argument. Let me handle this case directly.

With $x_1, x_2 < 1/5$ and $x_3 > 3/5$, $x_1 + x_2 + x_3 = 1$:

$f(x_1) + f(x_2) + f(x_3) = x_1^4(1-x_1) + x_2^4(1-x_2) + x_3^4(1-x_3)$.

Since $x_1, x_2 < 1/5$: $x_1^4 < (1/5)^4 = 1/625$ and $1 - x_1 > 4/5$. So $f(x_1) < 1/625 \cdot 1 = 1/625$. Similarly $f(x_2) < 1/625$.

$f(x_3) = x_3^4(1-x_3)$. With $x_3 > 3/5$, $1 - x_3 < 2/5$, and $x_3 < 1$ (since $x_1, x_2 > 0$... well, $x_1, x_2 \geq 0$).

Actually, let me be more precise. $x_3 = 1 - x_1 - x_2$ where $x_1 + x_2 < 2/5$, so $x_3 > 3/5$.

$f(x_3) = x_3^4(1-x_3) = x_3^4(x_1 + x_2)$.

Let $s = x_1 + x_2$, so $x_3 = 1 - s$, $s < 2/5$.

$f(x_3) = (1-s)^4 \cdot s$.

$f(x_1) + f(x_2) \leq f(s) + ps^2(5s-4) + p^2(2-5s)$ where $p = x_1 x_2 \leq s^2/4$.

Since $s < 2/5$: $5s - 4 < 0$ and $2 - 5s > 0$. So:

$f(x_1) + f(x_2) = f(s) + ps^2(5s-4) + p^2(2-5s) \leq f(s) + p^2(2-5s)$ (dropping the negative term).

$\leq f(s) + (s^2/4)^2 (2-5s) = f(s) + \frac{s^4(2-5s)}{16}$ (using $p \leq s^2/4$).

So $\sum f \leq f(s) + \frac{s^4(2-5s)}{16} + f(1-s) = f(s) + f(1-s) + \frac{s^4(2-5s)}{16}$.

Now, $f(s) + f(1-s) = s(1-s)(1 - 3s(1-s))$ (from our earlier computation with $t = s(1-s)$).

And the extra term is $\frac{s^4(2-5s)}{16} \geq 0$ (since $s < 2/5$ means $2 - 5s > 0$).

So $\sum f \leq f(s) + f(1-s) + \frac{s^4(2-5s)}{16}$.

We know $f(s) + f(1-s) \leq 1/12$ (from the $n=2$ result). But the extra term is positive, so this bound exceeds $1/12$.

Hmm, so this approach doesn't directly work. The extra term from not merging $x_1, x_2$ can push the sum above $1/12$... but we know from our numerical computation that it doesn't.

Let me be more precise. We have:

$\sum f = f(x_1) + f(x_2) + f(1-s)$ where $s = x_1 + x_2$.

$f(x_1) + f(x_2) = f(s) + ps^2(5s-4) + p^2(2-5s)$ where $p = x_1 x_2$.

So $\sum f = f(s) + f(1-s) + ps^2(5s-4) + p^2(2-5s)$.

$= s(1-s)(1-3s(1-s)) + ps^2(5s-4) + p^2(2-5s)$.

Let $t = s(1-s)$. Then:

$\sum f = t(1-3t) + ps^2(5s-4) + p^2(2-5s)$.

For $s < 2/5$: $5s - 4 < 0$, so $ps^2(5s-4) \leq 0$. And $2 - 5s > 0$, so $p^2(2-5s) \geq 0$.

We need to show $\sum f \leq 1/12$, i.e.,

$t(1-3t) + ps^2(5s-4) + p^2(2-5s) \leq 1/12$.

Since $t(1-3t) \leq 1/12$ (with equality at $t = 1/6$), we need:

$ps^2(5s-4) + p^2(2-5s) \leq 1/12 - t(1-3t)$.

The RHS is $1/12 - t + 3t^2 = 3(t - 1/6)^2 \geq 0$.

So we need: $ps^2(5s-4) + p^2(2-5s) \leq 3(t - 1/6)^2$ where $t = s(1-s)$, $p = x_1 x_2$, $s = x_1 + x_2$.

The LHS: $ps^2(5s-4) + p^2(2-5s) = p[s^2(5s-4) + p(2-5s)]$.

Since $5s - 4 < 0$ and $2 - 5s > 0$ (for $s < 2/5$):

$= p[-s^2(4-5s) + p(2-5s)]$.

For this to be $\leq 3(t-1/6)^2$, we need... this is getting quite involved. Let me try a specific approach.

Actually, maybe I should try to prove the whole thing differently. Let me try the "smoothing" / "mixing variables" approach.

**Mixing variables approach**: 

We want to show that the maximum of $\sum f(x_j)$ subject to $\sum x_j = 1$, $x_j \geq 0$ is $1/12$.

The idea: at the maximum, we can't have three or more positive variables, because we can always improve by adjusting.

**Lemma**: If $x_1, x_2, x_3 > 0$ with $x_1 + x_2 + x_3 = s \leq 1$, then there exist $y_1, y_2 \geq 0$ with $y_1 + y_2 = s$ such that $f(y_1) + f(y_2) > f(x_1) + f(x_2) + f(x_3)$.

Wait, this is too strong. We need $\geq$ not $>$, and we need to handle the case where one of the $y_i$ could be 0.

Actually, the claim should be: $f(x_1) + f(x_2) + f(x_3) \leq \max_{y_1 + y_2 = s, y_i \geq 0} [f(y_1) + f(y_2)]$.

This would mean: using 3 variables with sum $s$ is no better than using 2 variables with sum $s$.

If this is true, then by induction, using $n$ variables is no better than using 2 variables, and we're done.

So the key lemma is: **For $a, b, c \geq 0$ with $a + b + c = s$, $f(a) + f(b) + f(c) \leq \max_{y_1 + y_2 = s} [f(y_1) + f(y_2)]$.**

Equivalently, $f(a) + f(b) + f(c) \leq \max_{0 \leq u \leq s} [f(u) + f(s-u)]$.

The RHS is $M(s) := \max_{0 \leq u \leq s} [f(u) + f(s-u)]$.

From our earlier analysis, $f(u) + f(s-u) = f(s) + p_u s^2(5s-4) + p_u^2(2-5s)$ where $p_u = u(s-u)$.

For $s \leq 2/5$: $5s - 4 < 0$, $2 - 5s > 0$. So $f(u) + f(s-u) = f(s) - |5s-4| s^2 p_u + (2-5s) p_u^2$.

This is a quadratic in $p_u$: $(2-5s) p_u^2 - (4-5s) s^2 p_u + f(s)$.

Since $2 - 5s > 0$, this is a upward-opening parabola in $p_u$, so it's maximized at the endpoints of $p_u$'s range. $p_u = u(s-u) \in [0, s^2/4]$.

At $p_u = 0$ (i.e., $u = 0$ or $u = s$): value $= f(s) = f(0) + f(s)$. 
At $p_u = s^2/4$ (i.e., $u = s/2$): value $= f(s/2) + f(s/2) = 2f(s/2)$.

So $M(s) = \max(f(s), 2f(s/2))$ for $s \leq 2/5$.

$f(s) = s^4(1-s)$, $2f(s/2) = 2 \cdot (s/2)^4(1 - s/2) = \frac{s^4(2-s)}{16}$.

$f(s) / (2f(s/2)) = \frac{s^4(1-s)}{s^4(2-s)/16} = \frac{16(1-s)}{2-s}$.

For $s \leq 2/5$: $\frac{16(1-s)}{2-s} \geq \frac{16 \cdot 3/5}{2} = \frac{48/5}{2} = 4.8 > 1$. So $f(s) > 2f(s/2
