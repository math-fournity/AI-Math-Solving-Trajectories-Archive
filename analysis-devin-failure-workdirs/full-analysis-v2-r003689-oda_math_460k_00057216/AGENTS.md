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
  <problem_id>oda_math_460k_00057216</problem_id>
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

Factor $2n^2 + 3n + 1$.

## Standard Solution

<think>Okay, let's see. I need to factor the quadratic expression 2n² + 3n + 1. Hmm, factoring quadratics. Let me remember how that works. The general form is ax² + bx + c, and we need to find two binomials (mn + p)(qn + r) such that when we multiply them out, we get back the original quadratic. 

First, let's look at the coefficient of n², which is 2. So, the first terms of the binomials should multiply to 2n². The possible factors for 2 are 2 and 1, since 2 is prime. So maybe (2n + ...)(n + ...). 

Next, the constant term is 1. The factors of 1 are 1 and 1, or -1 and -1. But since the middle term is positive 3n, and the constant term is positive, both constants in the binomials should be positive. So maybe (2n + 1)(n + 1). Let's check that. 

Multiplying (2n + 1)(n + 1): first, 2n * n = 2n². Then, 2n * 1 = 2n. Then, 1 * n = n. Then, 1 * 1 = 1. Adding those up: 2n² + 2n + n + 1 = 2n² + 3n + 1. Oh, that's exactly the original expression! So that works. 

Wait, let me make sure there are no other possibilities. Let's see, could the factors be (2n + something else)(n + something else)? Let's think. Suppose the constants were different. But 1 only has 1 and 1 as positive factors, so that's the only option. Let's confirm again. (2n + 1)(n + 1) = 2n² + 2n + n + 1 = 2n² + 3n + 1. Yep, that's correct. So the factored form is (2n + 1)(n + 1).
</think>

To factor \(2n^2 + 3n + 1\), we start by looking for two binomials of the form \((an + b)(cn + d)\) such that their product equals the given quadratic expression. 

1. The coefficient of \(n^2\) is 2. The factors of 2 are 2 and 1, so we consider \((2n + \_\_)(n + \_\_)\).
2. The constant term is 1. The factors of 1 are 1 and 1. Since the middle term \(3n\) is positive, both constants should be positive. Thus, we try \((2n + 1)(n + 1)\).

Expanding \((2n + 1)(n + 1)\):
\[
(2n + 1)(n + 1) = 2n \cdot n + 2n \cdot 1 + 1 \cdot n + 1 \cdot 1 = 2n^2 + 2n + n + 1 = 2n^2 + 3n + 1
\]

This matches the original expression. Therefore, the factored form is \((2n + 1)(n + 1)\).

\[
\boxed{(2n + 1)(n + 1)}
\]

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. The oscillator has equation of motion $\ddot{x} + f(x) = 0$ with piecewise linear restoring force.

Let me parse the force definition carefully:
$$f(x) = \begin{cases} -x & |x| \leq a \\ b(x \operatorname{sgn}(x) - a) - a & |x| > a \end{cases}$$

Let me check continuity at $x = a$: 
- From inside: $f(a) = -a$
- From outside: $b(a \cdot 1 - a) - a = b(0) - a = -a$ ✓

At $x = -a$:
- From inside: $f(-a) = -(-a) = a$
- From outside: $b(-a \cdot (-1) - a) - a = b(a - a) - a = -a$

Wait, that gives $-a$ from outside but $a$ from inside. That's a discontinuity! Let me re-read.

Hmm, let me reconsider. $\operatorname{sgn}(x)$: for $x < 0$, $\operatorname{sgn}(x) = -1$. So $x \operatorname{sgn}(x) = x \cdot (-1) = -x$ for $x < 0$... wait no. For $x < 0$, $\operatorname{sgn}(x) = -1$, so $x \operatorname{sgn}(x) = x \cdot (-1) = -x = |x|$.

Actually $x \operatorname{sgn}(x) = |x|$ for all $x \neq 0$. So for $|x| > a$:
$$f(x) = b(|x| - a) - a$$

At $x = a$: $f(a^+) = b(a - a) - a = -a$. From inside $f(a) = -a$. ✓
At $x = -a$: $f(-a^-) = b(a - a) - a = -a$. From inside $f(-a) = -(-a) = a$. 

So there's a discontinuity at $x = -a$: limit from outside is $-a$, value from inside is $a$. That's strange for a "restoring force."

Hmm, let me reconsider. Maybe the formula is meant differently. Perhaps it's $b(x \operatorname{sgn}(x) - a) - a \operatorname{sgn}(x)$? Or perhaps the second case should be interpreted with sign.

Actually, let me reconsider. Maybe the intended reading is that for $x > a$, $f(x) = b(x - a) - a$, and for $x < -a$, $f(x) = b(-x - a) - a$... but that gives $f(x) = b(|x|-a) - a$ which is symmetric and even, so $f(-x) = f(x)$. But then at $x = -a$, $f = -a$ from outside, $f = a$ from inside. Discontinuity.

Wait, maybe I should reconsider the sign convention. For a restoring force, we want $f(x)$ to push back toward origin, so $f(x)$ should have opposite sign to $x$. For $x > 0$, $f(x) < 0$. For $x < 0$, $f(x) > 0$.

Inside region: $f(x) = -x$. For $x > 0$, $f < 0$ ✓. For $x < 0$, $f > 0$ ✓.

Outside region: $f(x) = b(|x| - a) - a$. For $x > a$: $f = b(x-a) - a$. At $x = a$, $f = -a < 0$ ✓ (pushes back). For large $x$, $f > 0$ — that's NOT restoring! That pushes away.

Hmm, that's odd. For $x < -a$: $f = b(|x| - a) - a = b(-x - a) - a$. At $x = -a$, $f = -a < 0$. But for $x < 0$ we want $f > 0$ (restoring). So $f = -a < 0$ pushes further negative — away from origin. Not restoring.

This doesn't look like a restoring force at all in the outer region unless... Let me reconsider. Maybe the formula should be $-b(x \operatorname{sgn}(x) - a) - a \operatorname{sgn}(x)$ or something.

Actually, let me reconsider the problem. This is a classic problem about homoclinic orbits for a piecewise linear oscillator. The homoclinic orbit connects a saddle point to itself. For a homoclinic orbit to exist, there must be a saddle equilibrium.

The equilibria are where $f(x) = 0$:
- Inside: $-x = 0 \Rightarrow x = 0$. At $x=0$, $f = 0$. Linearization: $\ddot{x} + (-x) = 0$... wait $\ddot{x} = -f(x) = x$, so $\ddot{x} = x$, which gives $x = e^{\pm t}$. So $x = 0$ is a saddle! Good, that's the saddle point.

Wait, $\ddot{x} + f(x) = 0$ with $f(x) = -x$ near 0 gives $\ddot{x} - x = 0$, i.e., $\ddot{x} = x$. Solutions $e^{\pm t}$. So origin is a saddle. Homoclinic orbits connect the saddle to itself.

- Outside: $f(x) = b(|x| - a) - a = 0 \Rightarrow |x| = a + a/b = a(1 + 1/b)$. So $x = \pm a(1 + 1/b)$. At these points, $f = 0$. Linearization: for $x > a$, $f(x) = b(x - a) - a = bx - ba - a$, so $f'(x) = b$. $\ddot{x} = -f(x)$, linearized $\ddot{\xi} = -b \xi$, so center (oscillator). For $x < -a$, $f(x) = b(-x - a) - a = -bx - ba - a$, $f'(x) = -b$. $\ddot{\xi} = -(-b)\xi = b\xi$, saddle? Wait.

Hmm, let me redo. For $x < -a$: $f(x) = b(|x| - a) - a = b(-x - a) - a = -bx - ab - a$. $f'(x) = -b$. The equilibrium is at $f(x_0) = 0$: $-bx_0 - ab - a = 0 \Rightarrow x_0 = -(ab + a)/b = -a(1 + 1/b)$. Linearize: $\ddot{\xi} + f'(x_0)\xi = 0 \Rightarrow \ddot{\xi} - b\xi = 0 \Rightarrow \ddot{\xi} = b\xi$. Saddle again.

So both outer equilibria are... for $x > a$ region: $f'(x_0) = b > 0$, $\ddot{\xi} = -b\xi$, center. For $x < -a$ region: $f'(x_0) = -b < 0$, $\ddot{\xi} = b\xi$, saddle.

So we have saddles at $x = 0$ and $x = -a(1+1/b)$, and a center at $x = a(1+1/b)$.

Hmm, this asymmetry is strange. Let me reconsider whether the force is really $b(|x|-a) - a$.

Actually, maybe the problem intends the force to be odd (antisymmetric), which is the natural form for a restoring force. Let me reconsider the formula. Perhaps it's:

$$f(x) = b(x \operatorname{sgn}(x) - a) - a \operatorname{sgn}(x)$$

for $|x| > a$. Then for $x > a$: $f = b(x - a) - a = bx - ab - a$. For $x < -a$: $f = b(-x - a) + a = -bx - ab + a$. 

Check continuity at $x = a$: inside $f = -a$, outside $f = b(a-a) - a = -a$ ✓.
At $x = -a$: inside $f = a$, outside $f = b(a - a) + a = a$ ✓. 

This is continuous and odd! $f(-x) = -f(x)$. This makes much more sense as a restoring force.

For $x > a$: $f = bx - ab - a = bx - a(b+1)$. Equilibrium: $x_0 = a(b+1)/b = a(1 + 1/b)$. $f'(x_0) = b > 0$, so center.
For $x < -a$: $f = -bx - ab + a$. Equilibrium: $x_0 = -a(b+1)/b = -a(1+1/b)$. $f'(x_0) = -b < 0$, saddle... 

wait, $f'(x) = -b$, $\ddot{\xi} = -f'\xi = b\xi$, saddle. Hmm, still asymmetric: center on right, saddle on left.

Hmm, that's still asymmetric. For an odd force, the equilibria should be symmetric: if $x_0$ is an equilibrium, $-x_0$ is too. And the type should be the same since $f'(-x_0) = f'(x_0)$ for odd $f$ (odd function has even derivative). So both should be the same type. Let me recompute.

For odd $f$: $f(x) = b(|x| - a)\operatorname{sgn}(x) - a\operatorname{sgn}(x)$... let me just use the form $f(x) = b(x \operatorname{sgn}(x) - a) - a\operatorname{sgn}(x)$.

For $x > a$: $f = b(x - a) - a$. $f' = b$.
For $x < -a$: $f = b(-x - a) + a$. $f' = -b$.

But for an odd function, $f'(-x) = f'(x)$ (even derivative). At $x = a(1+1/b) > 0$, $f' = b$. At $-a(1+1/b) < 0$, $f' = -b \neq b$. So this is NOT odd! 

Let me check: $f(x) = b(x\operatorname{sgn}(x) - a) - a\operatorname{sgn}(x)$. $f(-x) = b((-x)\operatorname{sgn}(-x) - a) - a\operatorname{sgn}(-x) = b((-x)(-1) - a) - a(-1) = b(x - a) + a$. And $-f(x) = -(b(x\operatorname{sgn}(x) - a) - a\operatorname{sgn}(x))$. For $x > 0$: $-f(x) = -(b(x-a) - a) = -b(x-a) + a$. $f(-x) = b(x-a) + a \neq -f(x)$. So not odd. OK.

So the force as literally written ($b(x\operatorname{sgn}(x) - a) - a$ without the $\operatorname{sgn}$ on the last term) is even: $f(-x) = f(x)$. Let me verify: $f(x) = b(|x| - a) - a$. $f(-x) = b(|-x| - a) - a = b(|x| - a) - a = f(x)$. Yes, even function.

An even restoring force is unusual but the problem says what it says. With an even force:
- $f(x) = -x$ for $|x| \leq a$ (this is odd actually, $-(-x) = x$... wait $f(-x) = -(-x) = x = -f(x)$? No. $f(x) = -x$, $f(-x) = -(-x) = x$, $-f(x) = x$. So $f(-x) = -f(x)$, odd.) 

But the outer part is even. So the force is neither odd nor even overall. That's the discontinuity issue at $x = -a$.

At $x = -a$: from inside, $f(-a) = -(-a) = a$. From outside, $f(-a) = b(a - a) - a = -a$. So $f$ jumps from $a$ to $-a$ at $x = -a$. Discontinuity of $2a$.

This is a really weird force. Let me reconsider — maybe I'm misreading and the problem actually has a well-known form. This looks like it could be from Jordan & Smith's "Nonlinear Ordinary Differential Equations" textbook. The homoclinic orbit problem for piecewise linear systems.

Let me reconsider the formula. Perhaps it should be read as: for $|x| > a$,
$$f(x) = b(x \operatorname{sgn}(x) - a) - a \operatorname{sgn}(x)$$

This would make it continuous and the standard form. But as written it's $b(x\operatorname{sgn}(x) - a) - a$.

Hmm, but actually, wait. Let me reconsider. Maybe the problem is stated exactly as in the textbook and the force IS discontinuous or has this specific form, and the homoclinic orbit exists due to the specific structure.

Actually, let me reconsider. With the even force $f(x) = b(|x|-a) - a$ for $|x| > a$:

The potential energy: $V(x) = \int_0^x f(s) ds$.
- For $0 \leq x \leq a$: $V(x) = \int_0^x (-s) ds = -x^2/2$.
- For $x > a$: $V(x) = V(a) + \int_a^x (b(s-a) - a) ds = -a^2/2 + [b(s-a)^2/2 - as]_a^x = -a^2/2 + b(x-a)^2/2 - ax + a^2 = a^2/2 + b(x-a)^2/2 - ax$.

At $x = a$: $V = a^2/2 + 0 - a^2 = -a^2/2$ ✓.

For $x > a$: $V(x) = a^2/2 + b(x-a)^2/2 - ax$. As $x \to \infty$, $V \to +\infty$ (since $b > 0$). 

The equilibrium at $x = 0$ is a saddle (since $V''(0) = f'(0) = -1 < 0$, potential has max at 0). $V(0) = 0$.

For a homoclinic orbit to the saddle at origin, we need the energy level $E = V(0) = 0$ to have a closed loop connecting the saddle to itself. The energy is $E = \dot{x}^2/2 + V(x) = 0$, so $\dot{x}^2 = -2V(x)$, need $V(x) \leq 0$.

For $0 \leq x \leq a$: $V = -x^2/2 \leq 0$ ✓.
For $x > a$: $V = a^2/2 + b(x-a)^2/2 - ax$. Set $V = 0$: $b(x-a)^2/2 - ax + a^2/2 = 0$, i.e., $b(x-a)^2 - 2ax + a^2 = 0$. Let $u = x - a$: $bu^2 - 2a(u+a) + a^2 = 0 \Rightarrow bu^2 - 2au - 2a^2 + a^2 = 0 \Rightarrow bu^2 - 2au - a^2 = 0$. $u = \frac{2a \pm \sqrt{4a^2 + 4ba^2}}{2b} = \frac{a \pm a\sqrt{1+b}}{b} = \frac{a(1 \pm \sqrt{1+b})}{b}$.

Taking the positive root (since $u = x - a > 0$): $u = \frac{a(1 + \sqrt{1+b})}{b}$. So $x_{\max} = a + \frac{a(1+\sqrt{1+b})}{b} = a\left(1 + \frac{1+\sqrt{1+b}}{b}\right) = a \cdot \frac{b + 1 + \sqrt{1+b}}{b}$.

Note $b + 1 = (1+b)$, so $x_{\max} = a \cdot \frac{(1+b) + \sqrt{1+b}}{b} = \frac{a\sqrt{1+b}(\sqrt{1+b} + 1)}{b}$.

Now for $x < 0$: the force is even, so $f(x) = f(-x)$ for $|x| > a$, but for $|x| \leq a$, $f(x) = -x$ (odd). So the potential is:

For $-a \leq x \leq 0$: $V(x) = \int_0^x f(s) ds = \int_0^x (-s) ds = -x^2/2$. Same as positive side. So $V$ is even? $V(-x) = -(-x)^2/2 = -x^2/2 = V(x)$ for $|x| \leq a$. 

For $x < -a$: $V(x) = V(-a) + \int_{-a}^x f(s) ds$. $V(-a) = -a^2/2$. $f(s) = b(|s| - a) - a = b(-s - a) - a$ for $s < -a$. $\int_{-a}^x (b(-s-a) - a) ds$. Let $t = -s$, $dt = -ds$, when $s = -a$, $t = a$; when $s = x$, $t = -x = |x|$. $\int_{-a}^x (b(-s-a)-a) ds = \int_{a}^{|x|} (b(t-a) - a)(-dt) = -\int_a^{|x|}(b(t-a)-a)dt = -[b(t-a)^2/2 - at]_a^{|x|} = -(b(|x|-a)^2/2 - a|x| + a^2 \cdot ... )$.

Let me just compute: $\int_a^{|x|}(b(t-a)-a)dt = b(|x|-a)^2/2 - a|x| - (0 - a^2) = b(|x|-a)^2/2 - a|x| + a^2$.

So $V(x) = -a^2/2 - (b(|x|-a)^2/2 - a|x| + a^2) = -a^2/2 - b(|x|-a)^2/2 + a|x| - a^2 = a|x| - 3a^2/2 - b(|x|-a)^2/2$.

Hmm, that doesn't match the positive side. For $x > a$: $V(x) = a^2/2 + b(x-a)^2/2 - ax$. For $x < -a$: $V(x) = a|x| - 3a^2/2 - b(|x|-a)^2/2 = -ax - 3a^2/2 - b(|x|-a)^2/2$... 

wait $|x| = -x$ for $x < 0$, so $a|x| = -ax$. $V(x) = -ax - 3a^2/2 - b(|x|-a)^2/2$.

Compare with positive side at $|x|$: $V(|x|) = a^2/2 + b(|x|-a)^2/2 - a|x|$. So $V(-|x|) = -a|x| - 3a^2/2 - b(|x|-a)^2/2 \neq V(|x|)$. The potential is NOT even. This is because the force is even for $|x| > a$ but odd for $|x| \leq a$, creating asymmetry.

This is getting complicated and the discontinuity at $x = -a$ is problematic. Let me reconsider whether the problem might have a different intended reading.

Actually, you know what, I bet this is the classic problem where the force is:
$$f(x) = \begin{cases} -x & |x| \leq a \\ -b\,\operatorname{sgn}(x)(|x| - a) - a\,\operatorname{sgn}(x) & |x| > a \end{cases}$$

or equivalently the force is odd and continuous. Let me look at this differently.

Actually, rethinking: the standard problem from Jordan & Smith (Problem 3.10 or similar) about homoclinic paths with piecewise linear force. The typical setup is:

$$f(x) = \begin{cases} -x & |x| \leq a \\ -b(x - a\,\operatorname{sgn}x) - a\,\operatorname{sgn}x & |x| > a \end{cases}$$

Hmm, let me just try: for $|x| > a$, $f(x) = -b(x - a\operatorname{sgn}x)\operatorname{sgn}x - a\operatorname{sgn}x$... this is getting circular.

Let me try the interpretation that makes the force odd and continuous. The most natural odd continuous extension:

For $|x| > a$: $f(x) = -b\,\operatorname{sgn}(x)(|x| - a) - a\,\operatorname{sgn}(x) = -\operatorname{sgn}(x)[b(|x|-a) + a]$.

Check at $x = a$: $f = -1 \cdot [b(0) + a] = -a$. From inside: $-a$ ✓.
At $x = -a$: $f = -(-1)[b(0) + a] = a$. From inside: $-(-a) = a$ ✓. Continuous!

This is odd: $f(-x) = -\operatorname{sgn}(-x)[b(|-x|-a)+a] = \operatorname{sgn}(x)[b(|x|-a)+a] = -f(x)$ ✓.

For $x > a$: $f(x) = -(b(x-a) + a) = -bx + ab - a$. Equilibrium: $-bx + ab - a = 0 \Rightarrow x = (ab - a)/b = a(b-1)/b = a(1 - 1/b)$. For this to be $> a$, need $1 - 1/b > 1$, i.e., $-1/b > 0$, impossible for $b > 0$. So no equilibrium in $x > a$ region (if $b > 0$). Actually $x_0 = a(b-1)/b$. For $b > 1$, $x_0 > 0$ but is it $> a$? $a(b-1)/b > a \iff (b-1)/b > 1 \iff b-1 > b$, false. So $x_0 < a$ always. So the equilibrium is inside the linear region, not outside. Hmm.

Wait, but we need a saddle point for homoclinic. The origin: $f(x) = -x$, $\ddot{x} = x$, saddle ✓. For homoclinic, we need the energy level of the saddle ($E = 0$) to form a loop.

With this odd force, the potential $V(x) = \int_0^x f(s)ds$:
- $0 \leq x \leq a$: $V = -x^2/2$.
- $x > a$: $V = -a^2/2 + \int_a^x (-bs + ab - a)ds = -a^2/2 + [-bs^2/2 + (ab-a)s]_a^x = -a^2/2 - bx^2/2 + (ab-a)x - (-ba^2/2 + (ab-a)a) = -a^2/2 - bx^2/2 + (ab-a)x + ba^2/2 - a^2 b + a^2$.

Let me simplify: $-a^2/2 + ba^2/2 - a^2 b + a^2 = a^2(-1/2 + b/2 - b + 1) = a^2(1/2 - b/2) = a^2(1-b)/2$.

So $V(x) = a^2(1-b)/2 - bx^2/2 + (ab-a)x$ for $x > a$.

$= -bx^2/2 + a(b-1)x + a^2(1-b)/2$.

As $x \to \infty$, $V \to -\infty$ (since $b > 0$). So the potential decreases without bound for large $|x|$. The energy level $E = 0$: $\dot{x}^2/2 + V = 0 \Rightarrow \dot{x}^2 = -2V$. For the homoclinic, we need $V(x) \leq 0$ for $x$ in some range, and $V = 0$ at the turning point.

$V(0) = 0$ (saddle energy). For $0 < x < a$, $V = -x^2/2 < 0$ ✓. For $x > a$, $V = -bx^2/2 + a(b-1)x + a^2(1-b)/2$. Set $V = 0$: $-bx^2/2 + a(b-1)x + a^2(1-b)/2 = 0$, multiply by $-2$: $bx^2 - 2a(b-1)x - a^2(1-b) = 0$, i.e., $bx^2 - 2a(b-1)x + a^2(b-1) = 0$.

Discriminant: $4a^2(b-1)^2 - 4ba^2(b-1) = 4a^2(b-1)[(b-1) - b] = 4a^2(b-1)(-1) = -4a^2(b-1)$.

For $b > 1$: discriminant $< 0$, no real roots, so $V$ never returns to 0 for $x > a$. Since $V(a) = -a^2/2 < 0$ and $V \to -\infty$, $V < 0$ for all $x > a$. So $\dot{x}^2 = -2V > 0$ for all $x > 0$ — the orbit escapes to infinity. No homoclinic.

For $b < 1$: discriminant $= -4a^2(b-1) = 4a^2(1-b) > 0$. Roots: $x = \frac{2a(b-1) \pm 2a\sqrt{1-b}}{2b} = \frac{a(b-1) \pm a\sqrt{1-b}}{b}$.

Since $b < 1$, $b - 1 < 0$. $\sqrt{1-b} > 0$. The roots are $\frac{a(b-1) \pm a\sqrt{1-b}}{b}$. 

For $b > 0$, both numerator options: $(b-1) + \sqrt{1-b}$ and $(b-1) - \sqrt{1-b}$. Since $b - 1 < 0$ and $\sqrt{1-b} > 0$, the first could be positive or negative. $(b-1) + \sqrt{1-b}$: let $c = 1 - b \in (0,1)$, then $-c + \sqrt{c} = \sqrt{c}(\sqrt{c} \cdot ... )$... $-c + \sqrt{c} = \sqrt{c}(1 - \sqrt{c})$. Since $c \in (0,1)$, $\sqrt{c} \in (0,1)$, so $1 - \sqrt{c} > 0$, thus $-c + \sqrt{c} > 0$. So the $+$ root is positive: $x_+ = \frac{a\sqrt{c}(1-\sqrt{c})}{b} = \frac{a\sqrt{1-b}(1-\sqrt{1-b})}{b} > 0$.

Is $x_+ > a$? Need $\frac{(b-1) + \sqrt{1-b}}{b} > 1$, i.e., $(b-1) + \sqrt{1-b} > b$, i.e., $\sqrt{1-b} > 1$, i.e., $1 - b > 1$, i.e., $b < 0$. False. So $x_+ < a$. That means the root is in the inner region, contradiction (we assumed $x > a$). So actually for $b < 1$, $V$ doesn't cross zero in $x > a$ region either... 

Hmm wait, let me recheck. $V(a) = -a^2/2 < 0$. $V$ for $x > a$ is a downward parabola (coefficient $-b/2 < 0$). So $V$ starts negative at $x = a$ and goes to $-\infty$. It could go up first then down. $V'(x) = -bx + a(b-1) = 0 \Rightarrow x = a(b-1)/b$. For $b < 1$, this is negative, so the vertex is at $x < 0$, meaning for $x > a$, $V$ is decreasing. So $V < V(a) < 0$ for all $x > a$. No crossing. So no homoclinic for this interpretation either (for any $b > 0$).

Hmm. So with the odd continuous force, there's no homoclinic orbit. That can't be right for a problem that asks to "find the homoclinic paths."

Let me go back to the literal even-force interpretation. With the even force, the potential is asymmetric, and maybe a homoclinic exists on one side.

Actually, wait. Let me reconsider. Maybe the force as literally written does create a homoclinic. Let me reconsider the potential for the literal force.

Literal force: $f(x) = -x$ for $|x| \leq a$, $f(x) = b(|x| - a) - a$ for $|x| > a$.

There's a discontinuity at $x = -a$ (jump from $a$ to $-a$). At $x = a$ it's continuous ($-a$ from both sides).

Potential $V(x) = \int_0^x f(s) ds$:
- $0 \leq x \leq a$: $V = -x^2/2$.
- $x > a$: $V = -a^2/2 + \int_a^x (b(s-a) - a) ds = -a^2/2 + b(x-a)^2/2 - a(x - a) = -a^2/2 + b(x-a)^2/2 - ax + a^2 = a^2/2 + b(x-a)^2/2 - ax$.
- $-a \leq x \leq 0$: $V = \int_0^x (-s) ds = -x^2/2$ (same).
- $x < -a$: $V = V(-a) + \int_{-a}^x f(s) ds = -a^2/2 + \int_{-a}^x (b(-s - a) - a) ds$.

$\int_{-a}^x (b(-s-a) - a) ds = \int_{-a}^x (-bs - ab - a) ds = [-bs^2/2 - (ab+a)s]_{-a}^x = -bx^2/2 - (ab+a)x - (-ba^2/2 + (ab+a)a) = -bx^2/2 - (ab+a)x + ba^2/2 - a^2 b - a^2 = -bx^2/2 - (ab+a)x + ba^2/2 - a^2 b - a^2$.

$ba^2/2 - a^2 b = -a^2 b/2$. So $= -bx^2/2 - (ab+a)x - a^2 b/2 - a^2$.

$V(x) = -a^2/2 - bx^2/2 - (ab+a)x - a^2 b/2 - a^2 = -bx^2/2 - (ab+a)x - a^2/2 - a^2 b/2 - a^2 = -bx^2/2 - (ab+a)x - a^2(3 + b)/2$.

Hmm wait let me redo: $-a^2/2 + (-a^2 b/2 - a^2) = -a^2/2 - a^2 b/2 - a^2 = -a^2(1/2 + b/2 + 1) = -a^2(3 + b)/2$.

So for $x < -a$: $V(x) = -bx^2/2 - (ab+a)x - a^2(3+b)/2$.

As $x \to -\infty$: $V \to -\infty$ (dominant term $-bx^2/2 \to -\infty$). 

For $x > a$: $V(x) = b(x-a)^2/2 - ax + a^2/2$. As $x \to +\infty$: $V \to +\infty$ (since $b > 0$). So on the right side, $V$ goes to $+\infty$, meaning there's a turning point. On the left side, $V \to -\infty$, so orbits escape.

$V(0) = 0$ (saddle). For the homoclinic on the right: $E = 0$, $\dot{x}^2 = -2V(x)$. Need $V \leq 0$.

For $0 \leq x \leq a$: $V = -x^2/2 \leq 0$ ✓.
For $x > a$: $V = b(x-a)^2/2 - ax + a^2/2$. Set $V = 0$: $b(x-a)^2 - 2ax + a^2 = 0$. Let $u = x - a$: $bu^2 - 2a(u+a) + a^2 = bu^2 - 2au - 2a^2 + a^2 = bu^2 - 2au - a^2 = 0$. $u = \frac{2a \pm \sqrt{4a^2 + 4ba^2}}{2b} = \frac{a \pm a\sqrt{1+b}}{b} = \frac{a(1 \pm \sqrt{1+b})}{b}$.

Positive root: $u = \frac{a(1 + \sqrt{1+b})}{b}$ (taking $+$ since $\sqrt{1+b} > 1$ for $b > 0$, so $1 + \sqrt{1+b} > 0$; the $-$ root gives $1 - \sqrt{1+b} < 0$, negative $u$, not in $x > a$ region).

So $x_{\max} = a + \frac{a(1 + \sqrt{1+b})}{b} = a \cdot \frac{b + 1 + \sqrt{1+b}}{b}$.

Let me denote $\alpha = \sqrt{1+b}$. Then $x_{\max} = a \cdot \frac{b + 1 + \alpha}{b} = a \cdot \frac{\alpha^2 + \alpha}{b} = \frac{a\alpha(\alpha + 1)}{b}$.

Since $b = \alpha^2 - 1 = (\alpha-1)(\alpha+1)$, we get $x_{\max} = \frac{a\alpha(\alpha+1)}{(\alpha-1)(\alpha+1)} = \frac{a\alpha}{\alpha - 1}$.

So $x_{\max} = \frac{a\sqrt{1+b}}{\sqrt{1+b} - 1}$.

Now the homoclinic orbit on the right side: starts at origin ($x = 0, \dot{x} = 0$), goes right to $x = x_{\max}$, comes back to origin. The orbit in the phase plane:

For $0 \leq x \leq a$ (inner region): $\ddot{x} + (-x) = 0 \Rightarrow \ddot{x} = x$. Energy: $\dot{x}^2/2 - x^2/2 = 0$ (since $V = -x^2/2$ and $E = 0$). So $\dot{x}^2 = x^2$, $\dot{x} = \pm x$. 

The outgoing branch: $\dot{x} = x$ (positive). The returning branch: $\dot{x} = -x$ (negative).

For $x > a$ (outer region): $\ddot{x} + b(x - a) - a = 0 \Rightarrow \ddot{x} = -b(x-a) + a = -bx + ab + a$. Energy: $\dot{x}^2/2 + V(x) = 0$ where $V(x) = b(x-a)^2/2 - ax + a^2/2$. So $\dot{x}^2 = -2V = -b(x-a)^2 + 2ax - a^2 = -b(x-a)^2 + 2a(x - a) + 2a^2 - a^2 = -b(x-a)^2 + 2a(x-a) + a^2$.

Let $u = x - a$: $\dot{x}^2 = -bu^2 + 2au + a^2 = a^2 + 2au - bu^2$.

This is an ellipse in the $(u, \dot{x})$ plane: $bu^2 - 2au + \dot{x}^2 = a^2$, i.e., $b(u - a/b)^2 + \dot{x}^2 = a^2 + a^2/b = a^2(1 + 1/b) = a^2(b+1)/b$.

So $\frac{(u - a/b)^2}{a^2(b+1)/b^2} + \frac{\dot{x}^2}{a^2(b+1)/b} = 1$.

This is an ellipse centered at $u = a/b$ (i.e., $x = a + a/b = a(1 + 1/b)$), with semi-axes $a\sqrt{b+1}/b$ in $u$ and $a\sqrt{(b+1)/b}$ in $\dot{x}$.

The orbit enters the outer region at $x = a$ (i.e., $u = 0$) with $\dot{x} = a$ (from the inner solution $\dot{x} = x = a$). Check: $\dot{x}^2 = a^2 + 0 - 0 = a^2$ ✓.

The orbit reaches $x_{\max}$ where $\dot{x} = 0$: $bu^2 - 2au - a^2 = 0$, $u = \frac{a(1 + \sqrt{1+b})}{b}$ as computed.

So the homoclinic orbit on the right side consists of:
1. Inner outgoing: $\dot{x} = x$ for $0 \leq x \leq a$.
2. Outer: ellipse $\frac{(x - a - a/b)^2}{a^2(b+1)/b^2} + \frac{\dot{x}^2}{a^2(b+1)/b} = 1$ for $a \leq x \leq x_{\max}$.
3. Inner returning: $\dot{x} = -x$ for $0 \leq x \leq a$.

By symmetry of the inner region ($\dot{x} = \pm x$), the returning branch mirrors the outgoing.

Now, is there also a homoclinic on the left side? For $x < 0$, the potential $V(x) = -x^2/2$ for $-a \leq x \leq 0$ (same), and for $x < -a$: $V(x) = -bx^2/2 - (ab+a)x - a^2(3+b)/2$. As $x \to -\infty$, $V \to -\infty$. So $V$ doesn't come back to 0 on the left (it goes to $-\infty$), meaning no turning point, no homoclinic on the left.

Wait, but let me check: is $V$ ever $\leq 0$ for $x < -a$? $V(-a) = -a^2/2 < 0$. And $V \to -\infty$. So $V < 0$ for all $x < -a$, meaning $\dot{x}^2 = -2V > 0$ always — the orbit keeps going left, escaping to $-\infty$. No homoclinic on the left.

But wait — there's a discontinuity at $x = -a$ in the force. The potential has a kink but is continuous (V is the integral, so it's continuous even if f has a jump). Actually, $V$ is continuous at $x = -a$: from inside $V(-a) = -a^2/2$, from outside $V(-a) = -ba^2/2 + (ab+a)a - a^2(3+b)/2 = -ba^2/2 + a^2 b + a^2 - 3a^2/2 - a^2 b/2 = a^2(-b/2 + b + 1 - 3/2 - b/2) = a^2(b - b + 1 - 3/2) = a^2(-1/2) = -a^2/2$ ✓.

So $V$ is continuous but has a corner (discontinuous derivative) at $x = -a$.

So the only homoclinic orbit is on the right side. But actually, the problem says "homoclinic paths" (plural). Maybe there are two: one on the right going out and back, which forms a single loop. In the phase plane, a homoclinic orbit is a single closed loop (connecting saddle to itself). The "paths" plural might refer to the two branches (upper and lower) or the parametric equations.

Actually, in the phase plane, the homoclinic orbit consists of two trajectories: one going out (upper half, $\dot{x} > 0$) and one returning (lower half, $\dot{x} < 0$), together forming a loop. Or it could be that the problem expects both a right and left homoclinic. But we showed left doesn't exist with this force.

Hmm, but actually, let me reconsider. The problem says "homoclinic paths" — in many textbooks, a homoclinic orbit is described by its equation in the phase plane, which is a single curve. The plural "paths" might just be the English plural form, or there might be two (left and right).

Given the asymmetry of the force (even in outer region, odd in inner), only the right homoclinic exists. But let me reconsider whether the problem might intend the odd force after all, and I made an error.

Actually, let me reconsider the problem statement once more. The force for $|x| > a$ is $b(x \operatorname{sgn}(x) - a) - a$. Since $x \operatorname{sgn}(x) = |x|$, this is $b(|x| - a) - a$. This is even. The inner force $-x$ is odd. So the overall force is neither odd nor even, with a discontinuity at $x = -a$.

This is a somewhat unusual problem, but let me just go with it. The homoclinic orbit exists on the right side where $V$ has a potential well shape (goes down then up to $+\infty$).

Actually, wait. Let me reconsider. Maybe the problem is from a specific textbook and the intended answer involves both sides. Let me reconsider: perhaps I should interpret $\operatorname{sgn}(x)$ differently, or perhaps the formula means something else.

Another interpretation: maybe for $|x| > a$, the force is $b \cdot x \cdot \operatorname{sgn}(x) - a \cdot \operatorname{sgn}(x) - a$... no, that doesn't parse from the given formula.

Or maybe: $b(x \operatorname{sgn}(x) - a) - a$ where the last $-a$ should be $-a\operatorname{sgn}(x)$. This is a common typo/omission. With $-a\operatorname{sgn}(x)$:

For $x > a$: $f = b(x - a) - a = bx - ab - a$.
For $x < -a$: $f = b(-x - a) + a = -bx - ab + a$.

This is continuous (checked earlier) and the force is... let me check oddness. $f(-x)$ for $x > a$: $f(-x) = b(x - a) + a$ (using $|-x| = x > a$ and $\operatorname{sgn}(-x) = -1$). $-f(x) = -(bx - ab - a) = -bx + ab + a$. These aren't equal, so not odd. But it is continuous.

For $x > a$: $f = bx - ab - a = bx - a(b+1)$. Equilibrium at $x_0 = a(b+1)/b$. $f'(x_0) = b > 0$, center.
For $x < -a$: $f = -bx - ab + a = -bx - a(b-1)$. Equilibrium at $x_0 = -a(b-1)/b = a(1-b)/b$. For $b > 1$, $x_0 < 0$; is $|x_0| > a$? $a(b-1)/b > a \iff (b-1)/b > 1$, false. So $|x_0| < a$, equilibrium is in inner region. For $b < 1$, $x_0 > 0$, also inner. So no equilibrium in $x < -a$ region. $f'(x) = -b < 0$ there, so $\ddot{x} = -f'\xi = b\xi$, saddle-like but no equilibrium in that region.

Potential for $x > a$ (with $-a\operatorname{sgn}(x)$ version): $V = -a^2/2 + \int_a^x (bs - ab - a)ds = -a^2/2 + bs^2/2 - (ab+a)s \big|_a^x = -a^2/2 + bx^2/2 - (ab+a)x - (ba^2/2 - (ab+a)a) = -a^2/2 + bx^2/2 - (ab+a)x - ba^2/2 + a^2 b + a^2 = bx^2/2 - (ab+a)x + a^2/2 + a^2 - a^2/2 = bx^2/2 - (ab+a)x + a^2$.

Hmm, $= bx^2/2 - a(b+1)x + a^2$. As $x \to \infty$, $V \to +\infty$. Set $V = 0$: $bx^2/2 - a(b+1)x + a^2 = 0$, $bx^2 - 2a(b+1)x + 2a^2 = 0$, $x = \frac{2a(b+1) \pm \sqrt{4a^2(b+1)^2 - 8ba^2}}{2b} = \frac{a(b+1) \pm a\sqrt{(b+1)^2 - 2b}}{b} = \frac{a(b+1) \pm a\sqrt{b^2 + 1}}{b}$.

Both roots positive (since $b+1 > \sqrt{b^2+1}$ for $b > 0$: $(b+1)^2 = b^2 + 2b + 1 > b^2 + 1$). The smaller root: $x_1 = \frac{a(b+1) - a\sqrt{b^2+1}}{b}$. Is $x_1 > a$? $\frac{(b+1) - \sqrt{b^2+1}}{b} > 1 \iff (b+1) - \sqrt{b^2+1} > b \iff 1 > \sqrt{b^2+1}$, false for $b > 0$. So $x_1 < a$, not in outer region.

The larger root: $x_2 = \frac{a(b+1) + a\sqrt{b^2+1}}{b} > a$ (clearly). So the turning point is at $x_2$.

For $x < -a$: $V = -a^2/2 + \int_{-a}^x (-bs - ab + a)ds = -a^2/2 + [-bs^2/2 - (ab-a)s]_{-a}^x = -a^2/2 - bx^2/2 - (ab-a)x - (-ba^2/2 + (ab-a)a) = -a^2/2 - bx^2/2 - (ab-a)x + ba^2/2 - a^2 b + a^2 = -bx^2/2 - (ab-a)x + a^2/2 + a^2 - a^2/2 = -bx^2/2 - a(b-1)x + a^2$.

As $x \to -\infty$: $V \to -\infty$. So again, left side escapes, no homoclinic on left.

So regardless of interpretation, only the right side has a homoclinic. The problem asks for "equations of the homoclinic paths" — I think it's asking for the phase plane equations of the homoclinic orbit(s).

Hmm, but actually, with the continuous force (with $-a\operatorname{sgn}(x)$), the potential on the left goes to $-\infty$, so no homoclinic on the left. With the literal even force, same thing. So in either case, only right homoclinic.

But wait — maybe for the continuous odd-ish force, there could be a homoclinic on the left too if the potential turns around. Let me check: for $x < -a$, $V = -bx^2/2 - a(b-1)x + a^2$. This is a downward parabola. $V'(x) = -bx - a(b-1) = 0 \Rightarrow x = -a(b-1)/b$. For $b > 1$, $x = -a(b-1)/b < 0$. Is this $< -a$? $a(b-1)/b > a \iff (b-1)/b > 1$, false. So vertex is in $(-a, 0)$, not in $x < -a$ region. So for $x < -a$, $V$ is decreasing (going left), $V \to -\infty$. No homoclinic on left.

OK so I'm fairly confident: only one homoclinic orbit, on the right side. Let me now write up the solution properly.

Actually, let me reconsider the problem once more. The problem says "Find the equations of the homoclinic paths in the phase plane." The use of "paths" (plural) might refer to the fact that a homoclinic orbit has two halves (upper and lower), or it might be that the textbook considers the orbit as having multiple segments (inner + outer).

Let me also reconsider: maybe the problem is symmetric and I'm wrong about the force. Let me re-examine.

If the force were truly odd and continuous, the potential would be even, and homoclinic orbits would exist on both sides (or neither). We showed neither exists for the odd version. For the even version (literal), only right exists. 

Hmm, but actually, for the odd version, I showed $V \to -\infty$ on both sides, so no homoclinic. For the even version, $V \to +\infty$ on the right (homoclinic exists) and $V \to -\infty$ on the left (no homoclinic). So the even (literal) version is the one that gives a homoclinic. Good, so the literal reading is correct and gives a meaningful problem.

Now let me also double-check: is the origin really a saddle? $f(x) = -x$ near 0, $\ddot{x} + (-x) = 0 \Rightarrow \ddot{x} = x$. Characteristic equation $r^2 = 1$, $r = \pm 1$. Yes, saddle. The stable and unstable manifolds are $\dot{x} = -x$ and $\dot{x} = x$ respectively (in the inner region).

The homoclinic orbit: the unstable manifold ($\dot{x} = x$, going right) exits the inner region at $(a, a)$, follows the ellipse in the outer region, reaches the turning point $(x_{\max}, 0)$, comes back along the lower half of the ellipse to $(a, -a)$, then re-enters the inner region following $\dot{x} = -x$ back to the origin (stable manifold).

So the homoclinic orbit is a single closed loop (well, it approaches the origin asymptotically, so it's a loop that takes infinite time to close).

Now let me write the equations clearly.

**Inner region** ($|x| \leq a$):
The orbit satisfies $\dot{x}^2 = x^2$, i.e., $\dot{x} = \pm x$.
- Upper branch (outgoing): $\dot{x} = x$
- Lower branch (returning): $\dot{x} = -x$

**Outer region** ($x > a$):
The orbit satisfies $\dot{x}^2 = -b(x-a)^2 + 2a(x-a) + a^2$, which is the ellipse:
$$b\left(x - a - \frac{a}{b}\right)^2 + \dot{x}^2 = \frac{a^2(b+1)}{b}$$

or equivalently:
$$\frac{\left(x - a\left(1 + \frac{1}{b}\right)\right)^2}{\frac{a^2(b+1)}{b^2}} + \frac{\dot{x}^2}{\frac{a^2(b+1)}{b}} = 1$$

The turning point is at $x_{\max} = \frac{a\sqrt{1+b}}{\sqrt{1+b} - 1}$... 

wait, let me recompute. $u = x - a$, $bu^2 - 2au - a^2 = 0$, $u = \frac{a(1 + \sqrt{1+b})}{b}$. $x_{\max} = a + \frac{a(1+\sqrt{1+b})}{b} = \frac{ab + a + a\sqrt{1+b}}{b} = \frac{a(b + 1 + \sqrt{1+b})}{b}$.

With $\alpha = \sqrt{1+b}$: $x_{\max} = \frac{a(\alpha^2 + \alpha)}{b} = \frac{a\alpha(\alpha + 1)}{(\alpha-1)(\alpha+1)} = \frac{a\alpha}{\alpha - 1} = \frac{a\sqrt{1+b}}{\sqrt{1+b} - 1}$.

The orbit enters the outer region at $(x, \dot{x}) = (a, a)$ and exits at $(a, -a)$.

Let me also express the ellipse more cleanly. The center of the ellipse is at $x = a + a/b = a(b+1)/b$, $\dot{x} = 0$. Semi-axis in $x$: $\frac{a\sqrt{b+1}}{b}$. Semi-axis in $\dot{x}$: $a\sqrt{\frac{b+1}{b}}$.

So the homoclinic path is:

$$\dot{x}^2 = \begin{cases} x^2 & |x| \leq a \\ -b(x-a)^2 + 2a(x-a) + a^2 & x > a \end{cases}$$

Or more explicitly, the ellipse equation for $x > a$:
$$\dot{x}^2 + b\left(x - a - \frac{a}{b}\right)^2 = \frac{a^2(b+1)}{b}$$

Let me verify at $x = a$: $\dot{x}^2 + b(0 - a/b)^2 = \dot{x}^2 + b \cdot a^2/b^2 = \dot{x}^2 + a^2/b$. Set equal to $a^2(b+1)/b = a^2 + a^2/b$. So $\dot{x}^2 = a^2$, $\dot{x} = \pm a$ ✓.

At $x = x_{\max}$: $\dot{x} = 0$, $b(x_{\max} - a - a/b)^2 = a^2(b+1)/b$. $x_{\max} - a - a/b = u_{\max} - a/b$ where $u_{\max} = \frac{a(1+\sqrt{1+b})}{b}$. $u_{\max} - a/b = \frac{a(1+\sqrt{1+b}) - a}{b} = \frac{a\sqrt{1+b}}{b}$. $b \cdot \frac{a^2(1+b)}{b^2} = \frac{a^2(1+b)}{b}$ ✓.

Great, everything checks out. Now let me also think about whether there's a homoclinic on the left side. We established $V \to -\infty$ as $x \to -\infty$, so no. But let me double-check by considering the left unstable manifold.

The unstable manifold going left: $\dot{x} = -x$ for $x < 0$ (since $\dot{x} = x$ is the right-going unstable manifold, $\dot{x} = -x$ with $x < 0$ gives $\dot{x} > 0$... wait).

In the inner region, $\ddot{x} = x$, general solution $x = Ae^t + Be^{-t}$, $\dot{x} = Ae^t - Be^{-t}$. The unstable manifold ($A \neq 0, B = 0$): $x = Ae^t$, $\dot{x} = Ae^t = x$. So $\dot{x} = x$ for the unstable manifold (both $A > 0$ going right and $A < 0$ going left). If $A < 0$, $x < 0$ and $\dot{x} = x < 0$, so the orbit moves left. It reaches $x = -a$ with $\dot{x} = -a$.

In the outer region ($x < -a$): $\ddot{x} = -f(x) = -(b(-x-a) - a) = b(-x-a) - a$... 

wait, $\ddot{x} + f(x) = 0$, so $\ddot{x} = -f(x)$. For $x < -a$, $f(x) = b(-x - a) - a = -bx - ab - a$. $\ddot{x} = bx + ab + a$.

Energy: $E = \dot{x}^2/2 + V(x) = 0$ (homoclinic energy). $V(x) = -bx^2/2 - (ab+a)x - a^2(3+b)/2$ for $x < -a$. $\dot{x}^2 = -2V = bx^2 + 2(ab+a)x + a^2(3+b)$.

At $x = -a$: $\dot{x}^2 = ba^2 - 2a(ab+a) + a^2(3+b) = ba^2 - 2a^2 b - 2a^2 + 3a^2 + a^2 b = a^2(b - 2b + b) + a^2(-2 + 3) = 0 + a^2 = a^2$. So $\dot{x} = \pm a$. The left-going unstable manifold arrives at $x = -a$ with $\dot{x} = -a$ (moving left, $\dot{x} < 0$). ✓ (consistent with $\dot{x} = x = -a$ from inner region).

For $x < -a$: $\dot{x}^2 = bx^2 + 2(ab+a)x + a^2(3+b)$. This is an upward-opening parabola in $x$ (coefficient $b > 0$). As $x \to -\infty$, $\dot{x}^2 \to +\infty$. The discriminant for $\dot{x}^2 = 0$: $4(ab+a)^2 - 4b \cdot a^2(3+b) = 4a^2[(b+1)^2 - b(3+b)] = 4a^2[b^2 + 2b + 1 - 3b - b^2] = 4a^2[1 - b]$.

For $b < 1$: discriminant $> 0$, so $\dot{x}^2 = 0$ has real roots, meaning there's a turning point on the left! The orbit would turn around and come back, forming a homoclinic on the left too!

For $b \geq 1$: discriminant $\leq 0$, $\dot{x}^2 > 0$ always, orbit escapes to $-\infty$. No left homoclinic.

Interesting! So for $b < 1$, there are TWO homoclinic orbits (left and right). For $b \geq 1$, only the right one.

Wait, but I need to check: for $b < 1$, does the left orbit actually turn around and come back to the origin? Let me find the turning point.

$\dot{x}^2 = bx^2 + 2a(b+1)x + a^2(3+b) = 0$. (Note: $ab + a = a(b+1)$.)

$x = \frac{-2a(b+1) \pm \sqrt{4a^2(1-b)}}{2b} = \frac{-a(b+1) \pm a\sqrt{1-b}}{b}$.

Both roots are negative (since $b + 1 > \sqrt{1-b}$ for $b > 0$: $(b+1)^2 = b^2 + 2b + 1 > 1 - b$ for $b > 0$). The more negative root: $x_{\min} = \frac{-a(b+1) - a\sqrt{1-b}}{b}$. Is $x_{\min} < -a$? $\frac{(b+1) + \sqrt{1-b}}{b} > 1 \iff b + 1 + \sqrt{1-b} > b \iff 1 + \sqrt{1-b} > 0$, always true. ✓

The less negative root: $x = \frac{-a(b+1) + a\sqrt{1-b}}{b} = \frac{-a(b+1-\sqrt{1-b})}{b}$. Is this $< -a$? $\frac{b+1-\sqrt{1-b}}{b} > 1 \iff b + 1 - \sqrt{1-b} > b \iff 1 > \sqrt{1-b}$, true for $b > 0$. So both roots are $< -a$ ✓.

So for $b < 1$, the left orbit turns around at $x_{\min}$ and comes back. The left homoclinic exists!

For $b < 1$, the left outer region orbit is also an ellipse:
$\dot{x}^2 = bx^2 + 2a(b+1)x + a^2(3+b) = b(x + a(b+1)/b)^2 + a^2(3+b) - a^2(b+1)^2/b = b(x + a(b+1)/b)^2 + a^2[(3+b) - (b+1)^2/b]$.

$(b+1)^2/b = (b^2 + 2b + 1)/b = b + 2 + 1/b$. $(3 + b) - (b + 2 + 1/b) = 1 - 1/b = (b-1)/b$.

So $\dot{x}^2 = b(x + a(b+1)/b)^2 + a^2(b-1)/b = b(x + a(b+1)/b)^2 - a^2(1-b)/b$.

Rearranging: $\dot{x}^2 - b(x + a(b+1)/b)^2 = -a^2(1-b)/b$, or $b(x + a(b+1)/b)^2 - \dot{x}^2 = a^2(1-b)/b$.

This is a hyperbola, not an ellipse! (Because the sign of $\dot{x}^2$ is negative.) So the left orbit in the outer region is a hyperbola.

Hmm wait, that's because the equilibrium in the left outer region is a saddle (we found $f'(x) = -b < 0$ there). So the level curves near a saddle are hyperbolas. That makes sense.

So for $b < 1$, the left homoclinic exists and the outer portion is a hyperbola. For $b \geq 1$, it doesn't exist.

Hmm, but actually, I need to be more careful. The orbit needs to turn around (reach $\dot{x} = 0$) and then come back. For $b < 1$, $\dot{x}^2 = 0$ at two points $x_{\min,1}$ and $x_{\min,2}$ (both $< -a$). The orbit going left reaches $\dot{x} = 0$ at $x_{\min,2}$ (the less negative one, since the orbit is moving left from $x = -a$). Wait, no. The orbit is at $x = -a$ with $\dot{x} = -a < 0$ (moving left). As $x$ decreases, $\dot{x}^2$ changes. Let me think about which root it hits.

At $x = -a$: $\dot{x}^2 = a^2 > 0$. As $x$ decreases from $-a$, $\dot{x}^2 = bx^2 + 2a(b+1)x + a^2(3+b)$. The parabola opens upward (in $x$), with vertex at $x = -a(b+1)/b$. The vertex value is $a^2(1-b)/b \cdot (-1) \cdot ... $ let me compute: at $x = -a(b+1)/b$, $\dot{x}^2 = a^2(b-1)/b < 0$ for $b < 1$. So $\dot{x}^2$ is negative at the vertex, meaning the parabola dips below zero between the two roots. The orbit moving left from $x = -a$ will hit $\dot{x} = 0$ at the larger root (less negative), $x_{\text{turn}} = \frac{-a(b+1) + a\sqrt{1-b}}{b}$.

Wait, but $\dot{x}^2$ must be non-negative for the orbit to exist. Between the two roots, $\dot{x}^2 < 0$, which is forbidden. So the orbit exists for $x \geq x_{\text{turn}}$ (where $x_{\text{turn}}$ is the larger root) and for $x \leq x_{\text{min}}$ (the smaller root), but not between. Since the orbit starts at $x = -a$ (which is $> x_{\text{turn}}$ since $x_{\text{turn}} < -a$), it moves left and hits $x_{\text{turn}}$ where $\dot{x} = 0$, then turns around and comes back. So yes, the left homoclinic exists for $b < 1$.

But actually, I realize this is getting very involved. The problem likely expects the answer for general $a, b > 0$, and the homoclinic on the right always exists. Let me also check: does the right homoclinic always exist (for all $b > 0$)?

Right side: $V(x) = b(x-a)^2/2 - ax + a^2/2$ for $x > a$. $V(a) = -a^2/2 < 0$. $V \to +\infty$ as $x \to +\infty$. So $V$ crosses zero exactly once for $x > a$ (since it's a upward parabola with $V(a) < 0$). So yes, the right homoclinic always exists for all $b > 0$.

For the left side, it exists only for $b < 1$.

Hmm, but the problem says "Find the equations of the homoclinic paths" without specifying conditions on $b$. Maybe the problem expects just the right homoclinic (which always exists), or maybe it expects both with the condition $b < 1$ for the left.

Actually, let me reconsider. I think this problem is from Jordan & Smith, and the standard answer gives the right homoclinic. Let me also reconsider whether the left one truly exists or if I'm making an error with the discontinuous force.

The discontinuity at $x = -a$: the force jumps from $f(-a^-) = a$ (from inside, $f = -(-a) = a$) to $f(-a^+) = -a$ (from outside). Wait, I need to be careful about direction. As $x$ decreases through $-a$:
- Just above $-a$ (i.e., $x \to -a^+$, $|x| < a$): $f = -x \to a$.
- Just below $-a$ (i.e., $x \to -a^-$, $|x| > a$): $f = b(|x| - a) - a \to b(0) - a = -a$.

So $f$ jumps from $a$ to $-a$ as $x$ crosses $-a$ going left. The acceleration $\ddot{x} = -f$ jumps from $-a$ to $a$. This is a discontinuity but the orbit can still be pieced together (the velocity is continuous, only acceleration jumps).

OK so the left homoclinic for $b < 1$ is valid despite the force discontinuity. The orbit is continuous and piecewise smooth.

Let me now write up the complete solution. I'll present both homoclinic orbits.

Actually, let me reconsider whether the problem is really asking about this specific (somewhat unusual) force, or if I'm overcomplicating it. Let me re-read the problem.

"An oscillator has an equation of motion given by $\ddot{x} + f(x) = 0$, where $f(x)$ is a piecewise linear restoring force defined by
$$f(x) = \begin{cases} -x & |x| \leq a \\ b(x \operatorname{sgn}(x) - a) - a & |x| > a \end{cases}$$
where $a, b > 0$. Find the equations of the homoclinic paths in the phase plane."

OK so the problem is clear. The force is as written. Let me just solve it.

The equilibria: $f(x) = 0$.
- Inside: $x = 0$. Saddle (since $\ddot{x} = x$).
- Outside ($x > a$): $b(x - a) - a = 0 \Rightarrow x = a + a/b = a(b+1)/b$. $f' = b > 0$, center.
- Outside ($x < -a$): $b(-x - a) - a = 0 \Rightarrow -x = a + a/b \Rightarrow x = -a(b+1)/b$. $f' = -b < 0$, saddle.

Wait, so there's another saddle at $x = -a(b+1)/b$! Let me check: $f(x) = b(-x - a) - a = -bx - ab - a$. $f = 0$: $x = -(ab + a)/b = -a(b+1)/b$. And $|x| = a(b+1)/b > a$ (since $(b+1)/b > 1$). ✓. $f'(x) = -b < 0$, so $\ddot{x} = -f'\xi = b\xi$, saddle.

So there are two saddles: at $x = 0$ and at $x = -a(b+1)/b$, and one center at $x = a(b+1)/b$.

The homoclinic paths connect a saddle to itself. The saddle at $x = 0$ has a homoclinic on the right (always exists). The saddle at $x = -a(b+1)/b$ might have homoclinic orbits too.

Hmm, this is getting complex. Let me focus on what the problem is asking. "Find the equations of the homoclinic paths" — I think the main one is the homoclinic to the origin.

Actually, for the saddle at $x_s = -a(b+1)/b$, the energy is $E_s = V(x_s)$. Let me compute.

$V(x_s) = -bx_s^2/2 - (ab+a)x_s - a^2(3+b)/2$ (using the $x < -a$ formula).

$x_s = -a(b+1)/b$. $x_s^2 = a^2(b+1)^2/b^2$.

$V(x_s) = -b \cdot a^2(b+1)^2/(2b^2) - a(b+1) \cdot (-a(b+1)/b) - a^2(3+b)/2$
$= -a^2(b+1)^2/(2b) + a^2(b+1)^2/b - a^2(3+b)/2$
$= a^2(b+1)^2/(2b) - a^2(3+b)/2$
$= \frac{a^2}{2}\left[\frac{(b+1)^2}{b} - (3+b)\right]$
$= \frac{a^2}{2}\left[\frac{b^2 + 2b + 1 - b(3+b)}{b}\right]$
$= \frac{a^2}{2} \cdot \frac{b^2 + 2b + 1 - 3b - b^2}{b}$
$= \frac{a^2}{2} \cdot \frac{1 - b}{b}$
$= \frac{a^2(1-b)}{2b}$.

For $b < 1$: $V(x_s) > 0$. For $b > 1$: $V(x_s) < 0$. For $b = 1$: $V(x_s) = 0$ (same energy as origin saddle).

This is interesting. For $b = 1$, both saddles have the same energy $E = 0$, which means there could be a heteroclinic connection between them.

This is getting quite involved. I think the problem is primarily asking for the homoclinic orbit to the origin (the saddle at $x = 0$), which is the most natural one. Let me present that.

Actually, I realize I should also check: does the right homoclinic to the origin always exist? We need $V(x) \leq 0$ for $0 \leq x \leq x_{\max}$ with $V(x_{\max}) = 0$ and $V(0) = 0$. We showed $V < 0$ for $0 < x < x_{\max}$ (since $V = -x^2/2 < 0$ for $0 < x \leq a$, and $V$ is an upward parabola for $x > a$ with $V(a) < 0$ and one positive root). So yes, always exists. ✓

Now, the left side from the origin: the unstable manifold going left reaches $x = -a$ with $\dot{x} = -a$. In the outer region, the energy is $E = 0$. $\dot{x}^2 = -2V(x) = bx^2 + 2a(b+1)x + a^2(3+b)$. 

For this to have a turning point ($\dot{x} = 0$), need $bx^2 + 2a(b+1)x + a^2(3+b) = 0$ to have real roots, which requires $b < 1$ (discriminant $= 4a^2(1-b) > 0$).

So:
- For $b < 1$: the left branch of the unstable manifold turns around and returns to the origin, forming a second homoclinic orbit (on the left).
- For $b \geq 1$: the left branch escapes to $-\infty$, no left homoclinic.

But also, for $b < 1$, there's the other saddle at $x_s = -a(b+1)/b$ with $V(x_s) > 0$. The homoclinic to that saddle would be at energy $E = V(x_s) > 0$. This might create additional structure. But I think the problem is asking about the homoclinic to the origin.

Let me also reconsider: for $b \geq 1$, is there a homoclinic to the left saddle at $x_s$? $V(x_s) = a^2(1-b)/(2b) < 0$ for $b > 1$. The homoclinic energy is $E = V(x_s) < 0$. We'd need $V(x) \leq V(x_s)$ near $x_s$ with $V$ returning to $V(x_s)$. Since $x_s$ is a saddle (local max of $V$), $V(x_s)$ is a local maximum, so $V \leq V(x_s)$ nearby. The question is whether the level set $E = V(x_s)$ forms a closed loop. This requires checking if $V$ comes back up to $V(x_s)$ somewhere. This is getting very complicated.

I think the problem is asking for the homoclinic to the origin, which is the standard one. Let me present the solution.

Let me write up the solution cleanly.

**Solution:**

The system is $\ddot{x} + f(x) = 0$, which we write as $\dot{x} = y$, $\dot{y} = -f(x)$.

The energy (conserved quantity) is $E = \frac{1}{2}y^2 + V(x)$ where $V(x) = \int_0^x f(s)\,ds$.

**Potential:**
- For $|x| \leq a$: $V(x) = -\frac{x^2}{2}$
- For $x > a$: $V(x) = \frac{b(x-a)^2}{2} - ax + \frac{a^2}{2}$
- For $x < -a$: $V(x) = -\frac{bx^2}{2} - a(b+1)x - \frac{a^2(3+b)}{2}$

**Equilibrium at origin:** $f(0) = 0$, and $\ddot{x} = x$ (saddle). $V(0) = 0$.

**Homoclinic orbit to origin** (right side, exists for all $b > 0$):

The homoclinic orbit is at energy $E = 0$, so $y^2 = -2V(x)$.

For $0 \leq x \leq a$: $y^2 = x^2$, i.e., $y = \pm x$.

For $x > a$: $y^2 = -b(x-a)^2 + 2ax - a^2 = -b(x-a)^2 + 2a(x-a) + a^2$.

This can be written as:
$$b\left(x - a - \frac{a}{b}\right)^2 + y^2 = \frac{a^2(b+1)}{b}$$

This is an ellipse in the $(x, y)$ plane, centered at $\left(a + \frac{a}{b}, 0\right) = \left(\frac{a(b+1)}{b}, 0\right)$.

The orbit exits the inner region at $(a, a)$, follows the upper half of the ellipse to the turning point $\left(\frac{a\sqrt{1+b}}{\sqrt{1+b}-1}, 0\right)$... 

hmm wait, let me recompute the turning point. $y = 0$: $b(x - a - a/b)^2 = a^2(b+1)/b$, so $x - a - a/b = \pm a\sqrt{(b+1)/b} \cdot ... $

Actually: $x - a - a/b = \pm \frac{a\sqrt{b+1}}{\sqrt{b}} \cdot \frac{1}{\sqrt{b}}$... let me just solve directly.

$b(x - a - a/b)^2 = a^2(b+1)/b$
$(x - a - a/b)^2 = a^2(b+1)/b^2$
$x - a - a/b = \pm \frac{a\sqrt{b+1}}{b}$
$x = a + a/b \pm \frac{a\sqrt{b+1}}{b} = \frac{ab + a \pm a\sqrt{b+1}}{b} = \frac{a(b + 1 \pm \sqrt{b+1})}{b}$.

The larger value (turning point): $x_{\max} = \frac{a(b + 1 + \sqrt{b+1})}{b} = \frac{a\sqrt{b+1}(\sqrt{b+1} + 1)}{b}$.

With $\alpha = \sqrt{b+1}$, $b = \alpha^2 - 1 = (\alpha-1)(\alpha+1)$: $x_{\max} = \frac{a\alpha(\alpha+1)}{(\alpha-1)(\alpha+1)} = \frac{a\alpha}{\alpha - 1} = \frac{a\sqrt{b+1}}{\sqrt{b+1} - 1}$.

The smaller value: $x = \frac{a(b + 1 - \sqrt{b+1})}{b} = \frac{a\sqrt{b+1}(\sqrt{b+1} - 1)}{(\sqrt{b+1}-1)(\sqrt{b+1}+1)} = \frac{a\sqrt{b+1}}{\sqrt{b+1}+1}$. Is this $> a$? $\frac{\sqrt{b+1}}{\sqrt{b+1}+1} > 1$? No, since $\sqrt{b+1} < \sqrt{b+1} + 1$. So this root is $< a$, not in the outer region. So only the larger root is the physical turning point. ✓

The orbit then returns along the lower half of the ellipse to $(a, -a)$, and re-enters the inner region with $y = -x$ back to the origin.

So the **right homoclinic path** is:

$$y^2 = \begin{cases} x^2 & 0 \leq |x| \leq a \\[6pt] -b(x-a)^2 + 2a(x-a) + a^2 & x > a \end{cases}$$

or equivalently, for $x > a$:
$$b\!\left(x - \frac{a(b+1)}{b}\right)^{\!2} + y^2 = \frac{a^2(b+1)}{b}$$

**Left homoclinic orbit** (exists only for $0 < b < 1$):

For $x < -a$, $y^2 = -2V(x) = bx^2 + 2a(b+1)x + a^2(3+b)$.

This has real zeros (turning points) when the discriminant $4a^2(1-b) > 0$, i.e., $b < 1$.

The orbit exits the inner region at $(-a, -a)$ (moving left), follows the curve $y^2 = bx^2 + 2a(b+1)x + a^2(3+b)$ to the turning point, and returns to $(-a, a)$, then back to origin via $y = -x$ (i.e., $y = |x|$ for $x < 0$... 

wait, $y = -x$ for $-a \leq x \leq 0$: if $x < 0$, $y = -x > 0$, so the returning branch has $y > 0$).

The left outer curve can be written as:
$$b\!\left(x + \frac{a(b+1)}{b}\right)^{\!2} - y^2 = \frac{a^2(1-b)}{b}$$

This is a hyperbola centered at $\left(-\frac{a(b+1)}{b}, 0\right)$.

The turning point (where $y = 0$): $x = \frac{-a(b+1) + a\sqrt{1-b}}{b}$ (the less negative root, which the orbit reaches first going left from $x = -a$).

Hmm wait, I need to check which root. Going left from $x = -a$ with $y < 0$, $x$ decreases. The two roots are $x_1 = \frac{-a(b+1) + a\sqrt{1-b}}{b}$ and $x_2 = \frac{-a(b+1) - a\sqrt{1-b}}{b}$, with $x_1 > x_2$ (both $< -a$). The orbit moving left from $-a$ first reaches $x_1$ (the larger one, closer to $-a$). At $x_1$, $y = 0$, the orbit turns around. So $x_{\min} = x_1 = \frac{-a(b+1) + a\sqrt{1-b}}{b} = \frac{a(\sqrt{1-b} - b - 1)}{b}$.

Hmm, but actually, I need to verify that $x_1 < -a$ (so the orbit reaches the turning point in the outer region). We checked: $\frac{b+1-\sqrt{1-b}}{b} > 1$ for $b > 0$, so $|x_1| = \frac{a(b+1-\sqrt{1-b})}{b} > a$, thus $x_1 < -a$ ✓.

So the **left homoclinic path** (for $0 < b < 1$) is:

$$y^2 = \begin{cases} x^2 & |x| \leq a \\[6pt] bx^2 + 2a(b+1)x + a^2(3+b) & x < -a \end{cases}$$

or for $x < -a$:
$$b\!\left(x + \frac{a(b+1)}{b}\right)^{\!2} - y^2 = \frac{a^2(1-b)}{b}$$

Now, let me also think about whether the problem expects me to note the condition $b < 1$ for the left homoclinic, or whether the problem is designed so that both exist for all $b > 0$.

Given the problem says "where $a, b > 0$" without further restriction, and asks for "the homoclinic paths" (plural), I think:
1. The right homoclinic always exists (for all $b > 0$).
2. The left homoclinic exists only for $0 < b < 1$.

But maybe the problem expects both to always exist, which would mean I have an error. Let me double-check the right side.

Right side: $V(x) = b(x-a)^2/2 - ax + a^2/2$ for $x > a$. $V(a) = 0 - a^2 + a^2/2 = -a^2/2 < 0$. $V \to +\infty$. So $V$ crosses 0 once for $x > a$. The homoclinic exists. ✓ for all $b > 0$.

Left side: $V(x) = -bx^2/2 - a(b+1)x - a^2(3+b)/2$ for $x < -a$. $V(-a) = -ba^2/2 + a^2(b+1) - a^2(3+b)/2 = a^2[-b/2 + b + 1 - 3/2 - b/2] = a^2[-b + b + 1 - 3/2] = -a^2/2 < 0$. $V \to -\infty$ as $x \to -\infty$. So $V$ starts at $-a^2/2$ at $x = -a$ and goes to $-\infty$. Does it ever come back up to 0? $V'(x) = -bx - a(b+1) = 0 \Rightarrow x = -a(b+1)/b$. This is the vertex. $V$ at vertex $= a^2(1-b)/(2b)$ (computed earlier as $V(x_s)$). For $b < 1$, this is $> 0$, so $V$ goes up from $-a^2/2$ to a positive max, then back down to $-\infty$. So $V$ crosses 0 twice for $x < -a$ when $b < 1$. The homoclinic exists. For $b \geq 1$, $V$ at vertex $\leq 0$, so $V < 0$ always for $x < -a$, no crossing, no homoclinic.

So my analysis is correct. The left homoclinic exists only for $b < 1$.

Hmm, but the problem says "Find the equations of the homoclinic paths" without mentioning any condition. Maybe the problem expects the answer to include the condition, or maybe it's from a context where $b < 1$ is assumed. Or maybe the problem only expects the right homoclinic.

Actually, I just realized: maybe the problem is designed so that there's always a homoclinic on the right, and for $b < 1$ there's an additional one on the left. The "paths" plural might refer to the two branches (upper and lower) of the single right homoclinic, or to the parametric equations.

I'll present the complete solution: the right homoclinic (always exists) and the left homoclinic (for $b < 1$), clearly stating the conditions.

Let me also present the equations more cleanly. The homoclinic orbit to the origin at energy $E = 0$:

The orbit in the phase plane is given by $y^2 = -2V(x)$ where $V$ is the potential, and the orbit is the closed loop through the origin.

**Right homoclinic** (exists for all $a, b > 0$):

$$\dot{x}^2 = \begin{cases} x^2 & 0 \leq x \leq a \\ a^2 + 2a(x-a) - b(x-a)^2 & x \geq a \end{cases}$$

with $\dot{x} > 0$ on the outward journey and $\dot{x} < 0$ on the return.

The outer portion is the ellipse:
$$\frac{\left(x - \frac{a(b+1)}{b}\right)^2}{\frac{a^2(b+1)}{b^2}} + \frac{\dot{x}^2}{\frac{a^2(b+1)}{b}} = 1, \quad x \geq a$$

**Left homoclinic** (exists for $0 < b < 1$):

$$\dot{x}^2 = \begin{cases} x^2 & -a \leq x \leq 0 \\ a^2 - 2a(x+a) - b(x+a)^2 + 4a^2\cdot\frac{... }{...} & x \leq -a \end{cases}$$

Hmm, let me just express the left outer part directly.

For $x \leq -a$: $\dot{x}^2 = bx^2 + 2a(b+1)x + a^2(3+b)$.

Let me verify at $x = -a$: $\dot{x}^2 = ba^2 - 2a^2(b+1) + a^2(3+b) = a^2[b - 2b - 2 + 3 + b] = a^2 \cdot 1 = a^2$ ✓.

The hyperbola form: $b(x + a(b+1)/b)^2 - \dot{x}^2 = a^2(1-b)/b$.

OK let me now write the final answer. I'll be thorough but clear.

Actually, I want to double-check my potential computation for $x < -a$ once more, since it's crucial.

$V(x) = \int_0^x f(s) ds$. For $x < -a$, we split: $V(x) = \int_0^{-a} f(s) ds + \int_{-a}^x f(s) ds$.

$\int_0^{-a} (-s) ds = [-s^2/2]_0^{-a} = -a^2/2$.

$\int_{-a}^x (b(-s-a) - a) ds = \int_{-a}^x (-bs - ab - a) ds = [-bs^2/2 - (ab+a)s]_{-a}^x$
$= (-bx^2/2 - (ab+a)x) - (-b(-a)^2/2 - (ab+a)(-a))$
$= (-bx^2/2 - (ab+a)x) - (-ba^2/2 + (ab+a)a)$
$= -bx^2/2 - (ab+a)x + ba^2/2 - a^2 b - a^2$
$= -bx^2/2 - (ab+a)x + a^2(b/2 - b - 1)$
$= -bx^2/2 - (ab+a)x + a^2(-b/2 - 1)$
$= -bx^2/2 - (ab+a)x - a^2(b+2)/2$.

So $V(x) = -a^2/2 - bx^2/2 - (ab+a)x - a^2(b+2)/2 = -bx^2/2 - (ab+a)x - a^2(1 + (b+2)/2) = -bx^2/2 - (ab+a)x - a^2(b+3)/2$.

Wait, $-a^2/2 - a^2(b+2)/2 = -a^2(1 + b + 2)/2 = -a^2(b+3)/2$. ✓. So $V(x) = -bx^2/2 - a(b+1)x - a^2(b+3)/2$ for $x < -a$.

Then $-2V(x) = bx^2 + 2a(b+1)x + a^2(b+3)$. ✓ (matches what I had, with $3+b = b+3$).

Good. Now let me also verify the hyperbola form:
$bx^2 + 2a(b+1)x + a^2(b+3) = b(x + a(b+1)/b)^2 - a^2(b+1)^2/b + a^2(b+3)$
$= b(x + a(b+1)/b)^2 + a^2[(b+3) - (b+1)^2/b]$
$= b(x + a(b+1)/b)^2 + a^2[(b^2+3b - b^2 - 2b - 1)/b]$
$= b(x + a(b+1)/b)^2 + a^2[(b - 1)/b]$
$= b(x + a(b+1)/b)^2 - a^2(1-b)/b$.

So $\dot{x}^2 = b(x + a(b+1)/b)^2 - a^2(1-b)/b$, i.e., $b(x + a(b+1)/b)^2 - \dot{x}^2 = a^2(1-b)/b$. ✓

For $b < 1$: RHS $> 0$, hyperbola opening left-right. The orbit exists where $\dot{x}^2 \geq 0$, i.e., $b(x + a(b+1)/b)^2 \geq a^2(1-b)/b$, i.e., $|x + a(b+1)/b| \geq \frac{a\sqrt{1-b}}{b}$. The two branches of the hyperbola correspond to $x \leq -a(b+1)/b - a\sqrt{1-b}/b$ and $x \geq -a(b+1)/b + a\sqrt{1-b}/b$. The orbit from $x = -a$ (which is $> -a(b+1)/b + a\sqrt{1-b}/b$ since $-a > -a(b+1-\sqrt{1-b})/b$... 

let me check: $-a > -a(b+1-\sqrt{1-b})/b$? This is $a < a(b+1-\sqrt{1-b})/b$, i.e., $b < b+1-\sqrt{1-b}$, i.e., $0 < 1-\sqrt{1-b}$, true for $b > 0$. So $-a$ is in the right branch of the hyperbola ($x > -a(b+1)/b + a\sqrt{1-b}/b$). The orbit goes left from $-a$ to the vertex of this branch at $x = -a(b+1)/b + a\sqrt{1-b}/b = \frac{-a(b+1) + a\sqrt{1-b}}{b} = \frac{a(\sqrt{1-b} - b - 1)}{b}$, where $\dot{x} = 0$. Then turns around. ✓

OK, I'm confident in the solution. Let me write it up.

One more thing: I should present the equations of the homoclinic paths. The "equations" in the phase plane are the relations between $x$ and $\dot{x}$ (or $y = \dot{x}$).

Let me write the final solution.

Actually, I want to also present this more cleanly. Let me use $y = \dot{x}$.

The homoclinic orbits to the saddle at the origin exist at energy $E = 0$, i.e., $\frac{1}{2}y^2 + V(x) = 0$, or $y^2 = -2V(x)$.

**Right homoclinic orbit** (exists for all $a, b > 0$):

The orbit leaves the origin along the unstable manifold $y = x$ ($x > 0$), reaches $(a, a)$, then follows the ellipse in the outer region to the turning point, and returns symmetrically.

Phase plane equation:
- For $0 \leq x \leq a$: $y = \pm x$ (upper: $y = x$, lower: $y = -x$)
- For $a \leq x \leq x_{\max}$: $b\!\left(x - \frac{a(1+b)}{b}\right)^2 + y^2 = \frac{a^2(1+b)}{b}$

where $x_{\max} = \frac{a\sqrt{1+b}}{\sqrt{1+b}-1} = \frac{a(1+b+\sqrt{1+b})}{b}$.

**Left homoclinic orbit** (exists for $0 < b < 1$):

The orbit leaves the origin along $y = x$ ($x < 0$, so $y < 0$, moving left), reaches $(-a, -a)$, then follows the hyperbola in the outer region to the turning point, and returns.

Phase plane equation:
- For $-a \leq x \leq 0$: $y = \pm x$ (upper: $y = -x$, lower: $y = x$)

Wait, I need to be careful. For $x < 0$, $y = x$ gives $y < 0$ (lower half, moving left). $y = -x$ gives $y > 0$ (upper half, moving right, returning). So:
- Outgoing (lower): $y = x$ for $-a \leq x \leq 0$
- Returning (upper): $y = -x$ for $-a \leq x \leq 0$

- For $x_{\min} \leq x \leq -a$: $b\!\left(x + \frac{a(1+b)}{b}\right)^2 - y^2 = \frac{a^2(1-b)}{b}$

where $x_{\min} = \frac{a(\sqrt{1-b} - 1 - b)}{b} = \frac{-a(1+b-\sqrt{1-b})}{b}$.

Let me now write the complete proof.

Hmm, actually, I want to reconsider whether the problem might have a simpler intended answer. Let me reconsider the force definition.

Looking at it again: $b(x \operatorname{sgn}(x) - a) - a$. For $x > a$: $b(x - a) - a = bx - ab - a$. For $x < -a$: $b(-x - a) - a = -bx - ab - a$.

Hmm, for $x < -a$: $f(x) = -bx - ab - a$. At $x = -a$: $f = ba - ab - a = -a$. From inside: $f(-a) = a$. Discontinuity.

But you know, maybe the problem is intentionally discontinuous, or maybe it's a typo. In any case, I'll solve it as stated.

Actually, I just want to double-check one thing: is the origin really the saddle that the homoclinic connects to? Yes: $f(0) = 0$, $\ddot{x} = -f(x) = x$ near 0, so eigenvalues $\pm 1$, saddle. The homoclinic orbit connects the saddle to itself.

Let me also note: the center at $x = a(1+b)/b$ is inside the right homoclinic orbit (it's the center of the ellipse). The center is surrounded by periodic orbits inside the homoclinic loop.

OK, I'm confident. Let me write the solution.

Wait, one more consideration. The problem says "homoclinic paths" (plural). In the phase plane, a homoclinic orbit to the origin on the right side is one path. If $b < 1$, there's another on the left. So "paths" could refer to:
1. Two paths: right and left (for $b < 1$)
2. One path with two branches (upper and lower)

I think the problem likely expects both (for the general case, or noting the condition). Let me present both.

Actually, I just realized I should double-check: for $b \geq 1$, the left unstable manifold escapes to $-\infty$. But does it perhaps connect to the other saddle at $x_s = -a(b+1)/b$? That would be a heteroclinic orbit, not homoclinic. For $b = 1$, $V(x_s) = 0 = V(0)$, so both saddles are at the same energy. The left unstable manifold of the origin (at $E = 0$) would reach the other saddle (also at $E = 0$) — that's a heteroclinic connection! For $b > 1$, $V(x_s) < 0$, so the origin's left manifold (at $E = 0$) passes over the other saddle (which is at lower energy) and escapes. For $b < 1$, $V(x_s) > 0$, the origin's left manifold (at $E = 0$) can't reach the other saddle (higher energy) and turns back — homoclinic.

This is a nice bifurcation picture: as $b$ increases through 1, the left homoclinic breaks into a heteroclinic connection (at $b = 1$) and then escapes ($b > 1$).

But the problem asks for homoclinic paths, so I'll focus on those.

Let me write the final answer now. I'll be comprehensive but clear.

Let me reconsider the form of the answer. I think the cleanest way to present it:

The homoclinic orbits to the saddle at the origin are at energy $E = 0$:

$$\dot{x}^2 = -2V(x)$$

where $V$ is the potential. The explicit equations:

**For the right homoclinic (all $b > 0$):**

$$\dot{x}^2 = \begin{cases} x^2 & 0 \leq x \leq a \\ a^2 + 2a(x-a) - b(x-a)^2 & x \geq a \end{cases}$$

The outer part is the ellipse $b\left(x - \frac{a(b+1)}{b}\right)^2 + \dot{x}^2 = \frac{a^2(b+1)}{b}$.

**For the left homoclinic ($0 < b < 1$):**

$$\dot{x}^2 = \begin{cases} x^2 & -a \leq x \leq 0 \\ a^2 - 2a(x+a) - b(x+a)^2 + \ldots & x \leq -a \end{cases}$$

Hmm, let me express the left outer part in terms of $x + a$ to make it parallel to the right side.

For $x \leq -a$, let $v = -(x+a) = -x - a \geq 0$ (so $x = -a - v$). Then:
$\dot{x}^2 = bx^2 + 2a(b+1)x + a^2(b+3)$
$= b(-a-v)^2 + 2a(b+1)(-a-v) + a^2(b+3)$
$= b(a+v)^2 - 2a(b+1)(a+v) + a^2(b+3)$
$= b(a^2 + 2av + v^2) - 2a^2(b+1) - 2a(b+1)v + a^2(b+3)$
$= ba^2 + 2abv + bv^2 - 2a^2 b - 2a^2 - 2abv - 2av + a^2 b + 3a^2$
$= bv^2 - 2av + (ba^2 - 2a^2 b + a^2 b) + (-2a^2 + 3a^2)$
$= bv^2 - 2av + 0 + a^2$
$= a^2 - 2av + bv^2$
$= a^2 - 2a(-x-a) + b(-x-a)^2$

Wait, that's $a^2 - 2a v + b v^2$ where $v = -x - a = |x| - a$ (since $x < -a$, $|x| = -x$, $|x| - a = -x - a = v$).

So $\dot{x}^2 = a^2 - 2a(|x|-a) + b(|x|-a)^2$ for $x \leq -a$.

Compare with the right side: $\dot{x}^2 = a^2 + 2a(x-a) - b(x-a)^2 = a^2 + 2a(|x|-a) - b(|x|-a)^2$ for $x \geq a$.

So the right side has $+2a(|x|-a) - b(|x|-a)^2$ and the left has $-2a(|x|-a) + b(|x|-a)^2$. They're negatives of each other (in the quadratic part). This asymmetry is due to the force being even (not odd) in the outer region.

Interesting. So the left outer orbit: $\dot{x}^2 = a^2 - 2a(|x|-a) + b(|x|-a)^2$. For this to have a turning point ($\dot{x} = 0$): $b(|x|-a)^
