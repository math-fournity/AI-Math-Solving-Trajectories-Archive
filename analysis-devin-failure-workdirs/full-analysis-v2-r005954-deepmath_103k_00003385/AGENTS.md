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
  <problem_id>deepmath_103k_00003385</problem_id>
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

Calculate \( \int_{D} ||\nabla f||^2 \, dA \), where \( f(x,y) = y - x^2 + 1 \) and \( D = \{(x,y) \mid f(x,y) \geq 0, \, y \leq 0\} \). Determine the correct limits of integration and evaluate the integral.

## Standard Solution

Okay, so I need to calculate the integral of the squared norm of the gradient of f over the region D. The function f is given by f(x, y) = y - x² + 1, and the region D is where f(x, y) ≥ 0 and y ≤ 0. Hmm, let me break this down step by step.

First, let's recall that the squared norm of the gradient of f, denoted ||∇f||², is just (∂f/∂x)² + (∂f/∂y)². So I need to compute those partial derivatives first.

Calculating the partial derivatives:

∂f/∂x = derivative of f with respect to x. Since f = y - x² + 1, the derivative with respect to x is -2x.

∂f/∂y = derivative of f with respect to y. Here, the derivative is 1, because the other terms don't involve y.

So ||∇f||² = (-2x)² + (1)² = 4x² + 1.

Therefore, the integral simplifies to the double integral over D of (4x² + 1) dA. Alright, that seems manageable. Now I need to figure out the region D to set up the limits of integration.

The region D is defined by two inequalities: f(x, y) ≥ 0 and y ≤ 0. Let's parse these.

First, f(x, y) ≥ 0 implies y - x² + 1 ≥ 0, which can be rewritten as y ≥ x² - 1. So this is the region above the parabola y = x² - 1.

Second, y ≤ 0, which is the region below or on the x-axis (since y = 0 is the x-axis).

Therefore, the region D is the set of all points (x, y) that lie above the parabola y = x² - 1 and below or on the x-axis. So visually, if I imagine the parabola y = x² - 1, which opens upwards with vertex at (0, -1), and the region y ≤ 0 is everything below the x-axis. The overlap between y ≥ x² -1 and y ≤ 0 would be the area bounded between the parabola and the x-axis.

To find the limits of integration, I need to determine where the parabola y = x² - 1 intersects the x-axis (y=0). Let's set y=0 in the parabola equation:

0 = x² - 1 => x² = 1 => x = ±1.

So the parabola intersects the x-axis at (-1, 0) and (1, 0). Therefore, the region D is bounded between x = -1 and x = 1, and for each x in this interval, y ranges from the parabola y = x² - 1 up to y = 0.

Thus, the integral becomes the double integral over x from -1 to 1, and for each x, y goes from x² - 1 to 0. So we can set up the integral as:

∫_{x=-1}^{1} ∫_{y=x² -1}^{0} (4x² + 1) dy dx.

Wait, but since the integrand (4x² + 1) is independent of y, when we integrate with respect to y, it's just (4x² + 1) multiplied by the length of the interval in y. So the inner integral ∫_{y=x² -1}^{0} (4x² + 1) dy is simply (4x² + 1)*(0 - (x² - 1)) = (4x² + 1)*(1 - x²).

Therefore, the integral simplifies to:

∫_{x=-1}^{1} (4x² + 1)(1 - x²) dx.

Now, I need to compute this single-variable integral. Let me expand the integrand first.

Multiply (4x² + 1)(1 - x²):

First, distribute 4x² over (1 - x²): 4x²*1 - 4x²*x² = 4x² - 4x⁴.

Then distribute 1 over (1 - x²): 1*1 - 1*x² = 1 - x².

Add these together: (4x² - 4x⁴) + (1 - x²) = 4x² - 4x⁴ + 1 - x² = (4x² - x²) + (-4x⁴) + 1 = 3x² - 4x⁴ + 1.

So the integral becomes:

∫_{-1}^{1} (3x² - 4x⁴ + 1) dx.

Now, let's compute this integral term by term.

First, ∫_{-1}^{1} 3x² dx. Since 3x² is even function (symmetric about y-axis), the integral from -1 to 1 is twice the integral from 0 to 1.

But let me just compute it directly.

∫3x² dx = 3*(x³/3) = x³. Evaluated from -1 to 1: (1³ - (-1)³) = 1 - (-1) = 2.

Second term: ∫_{-1}^{1} -4x⁴ dx. Again, x⁴ is even, so the integral from -1 to 1 is twice the integral from 0 to 1.

Compute ∫-4x⁴ dx = -4*(x⁵/5). Evaluated from -1 to 1:

[-4*(1⁵/5 - (-1)⁵/5)] = [-4*(1/5 - (-1)/5)] = [-4*(2/5)] = -8/5.

Wait, but let me check again. Wait, integrating from -1 to 1:

First, antiderivative is -4*(x⁵/5). So plug in x=1: -4*(1/5) = -4/5.

Plug in x=-1: -4*((-1)^5/5) = -4*(-1/5) = 4/5.

So the integral is (-4/5 - 4/5) = -8/5.

Third term: ∫_{-1}^{1} 1 dx = [x]_{-1}^1 = 1 - (-1) = 2.

Adding all three terms together:

2 (from first integral) + (-8/5) (from second) + 2 (from third) = 2 - 8/5 + 2 = (2 + 2) - 8/5 = 4 - 8/5 = 20/5 - 8/5 = 12/5.

So the total integral is 12/5.

Wait, hold on, let me verify that again step by step because sometimes when I compute integrals over symmetric intervals, especially with even and odd functions, there might be a shortcut.

But in this case, the integrand is 3x² -4x⁴ +1. Let's see:

3x² is even, -4x⁴ is even, and 1 is even. So the entire integrand is even. Therefore, the integral from -1 to 1 is twice the integral from 0 to 1.

So maybe compute twice ∫_{0}^{1} (3x² -4x⁴ +1) dx.

Let's do that to check.

Compute ∫(3x² -4x⁴ +1) dx from 0 to1:

Antiderivatives:

3*(x³/3) = x³,

-4*(x⁵/5) = -4x⁵/5,

1*x = x.

So evaluated from 0 to1:

(1³ - 4*1⁵/5 + 1) - (0 -0 +0) = (1 - 4/5 +1) = (2 - 4/5) = (10/5 -4/5) = 6/5.

Then twice that is 12/5. So same result. So that's correct.

Therefore, the value of the integral is 12/5.

Therefore, the answer is 12/5, which as a boxed expression is \boxed{\dfrac{12}{5}}.

But let me just make sure I didn't make any miscalculations.

Wait, when expanding (4x² +1)(1 -x²):

4x²*1 =4x²,

4x²*(-x²)= -4x⁴,

1*1=1,

1*(-x²)= -x².

So combining: 4x² -4x⁴ +1 -x² = (4x² -x²) + (-4x⁴) +1 = 3x² -4x⁴ +1. That's correct.

Then integrating term-wise:

∫3x² dx from -1 to1: 3*(1³/3 - (-1)³/3) = 3*( (1/3 +1/3)) = 3*(2/3) = 2. Correct.

∫-4x⁴ dx from -1 to1: -4*(1⁵/5 - (-1)^5/5) = -4*(1/5 +1/5)= -4*(2/5)= -8/5. Correct.

∫1 dx from -1 to1: 2. Correct.

Total: 2 -8/5 +2 = 4 -8/5 = 12/5. Correct.

Yes, so 12/5 is the right answer.

So, after all these steps, the integral evaluates to 12/5.

**Final Answer**
\boxed{\dfrac{12}{5}}
</think>

To calculate the integral \( \int_{D} ||\nabla f||^2 \, dA \), where \( f(x,y) = y - x^2 + 1 \) and \( D = \{(x,y) \mid f(x,y) \geq 0, \, y \leq 0\} \), we first find the gradient of \( f \):

\[
\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right) = (-2x, 1)
\]

The squared norm of the gradient is:

\[
||\nabla f||^2 = (-2x)^2 + 1^2 = 4x^2 + 1
\]

Next, we determine the region \( D \). The condition \( f(x,y) \geq 0 \) translates to \( y \geq x^2 - 1 \), and \( y \leq 0 \) restricts us to the region below the x-axis. The intersection of these regions is bounded between the parabola \( y = x^2 - 1 \) and the x-axis, with \( x \) ranging from \(-1\) to \( 1 \).

The integral becomes:

\[
\int_{-1}^{1} \int_{x^2 - 1}^{0} (4x^2 + 1) \, dy \, dx
\]

Evaluating the inner integral with respect to \( y \):

\[
\int_{x^2 - 1}^{0} (4x^2 + 1) \, dy = (4x^2 + 1) \left[ 0 - (x^2 - 1) \right] = (4x^2 + 1)(1 - x^2)
\]

Expanding the integrand:

\[
(4x^2 + 1)(1 - x^2) = 4x^2 - 4x^4 + 1 - x^2 = 3x^2 - 4x^4 + 1
\]

Integrating with respect to \( x \):

\[
\int_{-1}^{1} (3x^2 - 4x^4 + 1) \, dx
\]

Since the integrand is even, we can compute twice the integral from 0 to 1:

\[
2 \int_{0}^{1} (3x^2 - 4x^4 + 1) \, dx
\]

Calculating term by term:

\[
2 \left[ \int_{0}^{1} 3x^2 \, dx - \int_{0}^{1} 4x^4 \, dx + \int_{0}^{1} 1 \, dx \right]
\]

\[
= 2 \left[ \left[ x^3 \right]_{0}^{1} - \left[ \frac{4x^5}{5} \right]_{0}^{1} + \left[ x \right]_{0}^{1} \right]
\]

\[
= 2 \left[ (1 - 0) - \left( \frac{4}{5} - 0 \right) + (1 - 0) \right]
\]

\[
= 2 \left[ 1 - \frac{4}{5} + 1 \right] = 2 \left[ 2 - \frac{4}{5} \right] = 2 \left[ \frac{10}{5} - \frac{4}{5} \right] = 2 \left[ \frac{6}{5} \right] = \frac{12}{5}
\]

Thus, the value of the integral is:

\[
\boxed{\dfrac{12}{5}}
\]

## AI's Thinking (Attempted Solution Process)

The problem is about invariant theory. Let me analyze it carefully.

We have $R$ a finitely generated $\mathbb{Z}$-algebra with a linear algebraic action of $G(\mathbb{Z})$, where $G$ is a split simply-connected semisimple group. For any prime $p$, consider the map $R^{G(\mathbb{Z})} \otimes \mathbb{F}_p \rightarrow (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$. Is this map necessarily surjective for sufficiently large $p$?

This is a classic question in modular invariant theory / arithmetic invariant theory. The question is about whether reduction modulo $p$ commutes with taking invariants.

Let me think about this carefully.

First, let me understand the setup. $G$ is a split simply-connected semisimple group over $\mathbb{Z}$. $R$ is a finitely generated $\mathbb{Z}$-algebra (so $R = \mathbb{Z}[x_1, \ldots, x_n]/I$ for some ideal $I$). There's a "linear algebraic action" of $G(\mathbb{Z})$ on $R$, meaning $G$ acts on $R$ via algebra automorphisms, and this action comes from a linear action on the generators (i.e., $G$ acts on a finite-dimensional $\mathbb{Z}$-lattice and $R$ is the symmetric algebra or a quotient).

The map in question is the natural map:
$$R^{G(\mathbb{Z})} \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$$

This is the "reduction mod $p$" map on invariants. The question is whether this is surjective for large $p$.

This is related to the work of Seshadri, and more recently to the work of A'Campo, and particularly to the question of whether invariants of reductive groups behave well under reduction modulo $p$.

Key facts:
1. For reductive groups acting on polynomial rings over a field, the ring of invariants is finitely generated (Hilbert, Nagata, Haboush - Haboush's theorem says reductive groups in char $p$ have finitely generated invariants).

2. The question of whether $R^{G(\mathbb{Z})} \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$ is an isomorphism (or at least surjective) for large $p$ is a subtle one.

Let me think about what's known. There's a classical result that for a reductive group $G$ over $\mathbb{Z}$ acting on a finitely generated $\mathbb{Z}$-algebra $R$, the invariants $R^G$ are finitely generated over $\mathbb{Z}$ (Seshadri's theorem). Moreover, there's the question of whether the formation of invariants commutes with base change.

The key issue is: the functor $R \mapsto R^G$ is left exact but not exact in general. The obstruction to surjectivity of $R^{G(\mathbb{Z})} \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$ is related to the higher derived functors of invariants, specifically $H^1(G, R)$.

Actually, let me think more carefully. The map $R^{G(\mathbb{Z})} \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$ being surjective is equivalent to saying that every invariant mod $p$ lifts to an invariant over $\mathbb{Z}$.

This is the question of whether invariant theory commutes with reduction modulo $p$.

There's a well-known result: for a reductive group $G$ over $\mathbb{Z}$ acting on a finitely generated $\mathbb{Z}$-algebra $R$, if $G$ is "geometrically reductive" (which it is, by Haboush's theorem), then $R^G$ is finitely generated, and for large $p$, the formation of invariants commutes with base change.

Actually, let me be more precise. The result I'm thinking of is:

**Theorem (folklore / Seshadri / ...):** Let $G$ be a reductive group over $\mathbb{Z}$ acting on a finitely generated $\mathbb{Z}$-algebra $R$. Then:
1. $R^G$ is finitely generated over $\mathbb{Z}$.
2. For all but finitely many primes $p$, the natural map $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is an isomorphism.

Wait, but the question uses $G(\mathbb{Z})$ and $G(\mathbb{F}_p)$, not $G$ as a group scheme. Let me re-read.

"with a linear algebraic action of $G(\mathbb{Z})$"

Hmm, this says the action is of $G(\mathbb{Z})$, the group of $\mathbb{Z}$-points. But for a linear algebraic action to make sense, we probably need the action to come from an action of the group scheme $G$ on $R$. Let me assume this is the case - the action of $G(\mathbb{Z})$ extends to an action of $G$ as a group scheme over $\mathbb{Z}$.

Actually, the question says "linear algebraic action of $G(\mathbb{Z})$". This is a bit ambiguous. But I think the intended meaning is that $G$ acts on $R$ as a group scheme over $\mathbb{Z}$, and we're looking at the invariants under $G(\mathbb{Z})$ vs $G(\mathbb{F}_p)$.

Wait, but if the action is of the group scheme $G$, then $R^{G(\mathbb{Z})}$ means invariants under the group of $\mathbb{Z}$-points, while $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$ means invariants under the group of $\mathbb{F}_p$-points. These are different from the scheme-theoretic invariants $R^G$ and $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$.

Hmm, this is an important distinction. Let me think about this more carefully.

For a group scheme $G$ acting on $R$, the scheme-theoretic invariants $R^G$ are the elements $r \in R$ such that the coaction $\Delta: R \to R \otimes \mathcal{O}(G)$ sends $r$ to $r \otimes 1$. The invariants under $G(\mathbb{Z})$ are the elements fixed by all $\mathbb{Z}$-points of $G$.

In general, $R^{G(\mathbb{Z})} \supseteq R^G$ (scheme-theoretic invariants are a subset of invariants under all points), and equality holds when $G(\mathbb{Z})$ is Zariski dense in $G$.

For a split simply-connected semisimple group $G$ over $\mathbb{Z}$, $G(\mathbb{Z})$ is indeed Zariski dense in $G$ (this follows from the fact that $G$ is split and simply-connected, so $G(\mathbb{Z})$ is a lattice that is Zariski dense by the Borel density theorem or more elementary arguments for split groups).

So $R^{G(\mathbb{Z})} = R^G$ (scheme-theoretic invariants).

Similarly, over $\mathbb{F}_p$, $G(\mathbb{F}_p)$ is Zariski dense in $G_{\mathbb{F}_p}$ for large $p$ (this is a result that follows from the fact that for a connected reductive group over a finite field, the rational points are Zariski dense - actually this is true for $p$ large enough, or more precisely, $G(\mathbb{F}_p)$ is Zariski dense in $G_{\mathbb{F}_p}$ when $G$ is connected reductive and $p$ is such that $G_{\mathbb{F}_p}$ is connected, which for split simply-connected semisimple groups is always the case).

Wait, actually for a connected reductive group over a finite field $\mathbb{F}_q$, the group $G(\mathbb{F}_q)$ is Zariski dense in $G$. This is a well-known fact. The reason: $G(\mathbb{F}_q)$ generates $G$ as a Zariski closure because... actually, let me think. For $\text{SL}_n$, $\text{SL}_n(\mathbb{F}_q)$ is Zariski dense in $\text{SL}_n$ over $\overline{\mathbb{F}_q}$. This is because $\text{SL}_n(\mathbb{F}_q)$ contains enough elements to generate the coordinate ring. More generally, for any connected reductive group, $G(\mathbb{F}_q)$ is Zariski dense.

So for large $p$, $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)} = (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ (scheme-theoretic invariants).

Now the question reduces to: is $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ surjective for large $p$?

This is the question of whether the formation of invariants commutes with base change for large $p$.

The answer is **yes**, and this is a well-known result. Let me recall the argument.

By Seshadri's theorem, $R^G$ is finitely generated over $\mathbb{Z}$. The key tool is the concept of "geometric reductivity" and the Reynolds operator.

Actually, let me think about this differently. The standard result is:

**Theorem:** Let $G$ be a reductive group over $\mathbb{Z}$ acting on a finitely generated $\mathbb{Z}$-algebra $R$. Then $R^G$ is finitely generated over $\mathbb{Z}$, and there exists a finite set of primes $S$ such that for $p \notin S$, the natural map $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is an isomorphism.

This is essentially proved using the fact that:
1. $G$ is geometrically reductive (Haboush's theorem), so invariants are finitely generated.
2. The Reynolds operator (or more precisely, the fact that for reductive groups, the functor of invariants is exact on rational modules in characteristic 0, and "almost exact" in large characteristic).

Actually, let me be more careful. The exact statement and proof:

In characteristic 0, reductive groups are linearly reductive, meaning the functor of invariants is exact. This gives us that $R^G \otimes \mathbb{Q} = (R \otimes \mathbb{Q})^{G_\mathbb{Q}}$ and more generally invariants commute with base change over $\mathbb{Q}$.

Over $\mathbb{Z}$, the situation is more subtle. The key result is:

**Proposition:** Let $G$ be a reductive group over $\mathbb{Z}$, $R$ a finitely generated $\mathbb{Z}$-algebra with $G$-action. Then:
(a) $R^G$ is finitely generated over $\mathbb{Z}$.
(b) There exists $N$ such that for all primes $p > N$, the map $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is an isomorphism.

The proof of (b) typically goes as follows:

Since $R^G$ is finitely generated over $\mathbb{Z}$, say $R^G = \mathbb{Z}[f_1, \ldots, f_m]$ (as a $\mathbb{Z}$-algebra, it's a quotient of a polynomial ring). Consider the inclusion $R^G \hookrightarrow R$. This gives us $R^G \otimes \mathbb{F}_p \hookrightarrow R \otimes \mathbb{F}_p$ (for $p$ not dividing the torsion, but $R$ is $\mathbb{Z}$-flat if it's a polynomial ring; in general we need to be careful).

Actually, let me think about this more carefully. The issue is that $R$ might have torsion, and $R^G$ might have torsion.

Let me assume $R$ is $\mathbb{Z}$-free (which is the case if $R$ is a polynomial ring over $\mathbb{Z}$, or more generally a symmetric algebra of a free $\mathbb{Z}$-module). This is the typical case for "linear algebraic action."

So let's say $R = \mathbb{Z}[x_1, \ldots, x_n]$ (or a quotient by a $G$-stable ideal, but let's first consider the polynomial case).

The map $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is always injective (for $R$ $\mathbb{Z}$-free and $R^G$ $\mathbb{Z}$-free, or more generally when there's no torsion issue). The question is surjectivity.

Surjectivity means: every $G_{\mathbb{F}_p}$-invariant in $R \otimes \mathbb{F}_p$ lifts to a $G$-invariant in $R$ (mod $p$).

The standard approach uses the Reynolds operator. In characteristic 0, there's a Reynolds operator $\rho: R \otimes \mathbb{Q} \to (R \otimes \mathbb{Q})^{G_\mathbb{Q}}$ which is a $G$-equivariant projection. This operator can be "spread out" over $\mathbb{Z}[1/N]$ for some $N$, meaning there's a map $\rho: R \otimes \mathbb{Z}[1/N] \to (R \otimes \mathbb{Z}[1/N])^G$ that is a $G$-equivariant projection.

For $p \nmid N$, this gives a Reynolds operator in characteristic $p$, which implies that invariants commute with base change.

Wait, but the Reynolds operator in characteristic 0 uses averaging over a compact form of $G$, or equivalently, the unitarian trick (Weyl's trick). This requires dividing by the volume of the compact group, which involves factorials and such. So the Reynolds operator is defined over $\mathbb{Z}[1/N]$ for some $N$ depending on $G$ and the representation.

More precisely: for a representation $V$ of $G$ over $\mathbb{Z}$, the Reynolds operator $\rho_V: V \otimes \mathbb{Q} \to (V \otimes \mathbb{Q})^G$ can be spread out to $\mathbb{Z}[1/N]$ for some $N$. This is because the Reynolds operator is constructed using the Casimir element or by averaging over a maximal compact subgroup, and the denominators that appear are bounded.

Actually, the most standard approach: Since $G$ is reductive over $\mathbb{Q}$, it's linearly reductive over $\mathbb{Q}$, so there's a Reynolds operator $\rho: R_\mathbb{Q} \to R_\mathbb{Q}^G$. This operator is a $\mathbb{Q}$-linear map. Since $R$ is finitely generated over $\mathbb{Z}$, the Reynolds operator can be represented by a matrix with rational entries, and clearing denominators, it's defined over $\mathbb{Z}[1/N]$ for some $N$.

For $p \nmid N$, the Reynolds operator mod $p$ gives a $G_{\mathbb{F}_p}$-equivariant projection $R \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$, which shows that $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}} = \text{im}(\rho \otimes \mathbb{F}_p) = \text{im}(\rho) \otimes \mathbb{F}_p = R^G \otimes \mathbb{F}_p$ (the last equality because $\rho$ is a projection onto $R^G$).

Wait, I need to be more careful. The Reynolds operator $\rho: R \otimes \mathbb{Z}[1/N] \to R \otimes \mathbb{Z}[1/N]$ is a $G$-equivariant idempotent with image $(R \otimes \mathbb{Z}[1/N])^G = R^G \otimes \mathbb{Z}[1/N]$. When we reduce mod $p$ (for $p \nmid N$), we get a $G_{\mathbb{F}_p}$-equivariant idempotent $\bar{\rho}: R \otimes \mathbb{F}_p \to R \otimes \mathbb{F}_p$ with image $\text{im}(\bar{\rho})$.

Now, $\text{im}(\bar{\rho}) \subseteq (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ because $\bar{\rho}$ is $G_{\mathbb{F}_p}$-equivariant and its image consists of fixed points (since $\bar{\rho}$ is a projection onto fixed points... wait, is that true?).

Actually, the Reynolds operator has the property that $\rho(r) = r$ for $r \in R^G$ and $\rho(r) \in R^G$ for all $r$. So $\rho$ is a projection onto $R^G$. When we reduce mod $p$, $\bar{\rho}$ is a projection onto $R^G \otimes \mathbb{F}_p$ (the image of $R^G \otimes \mathbb{F}_p$ under the inclusion into $R \otimes \mathbb{F}_p$). But is $\bar{\rho}$ still a projection onto the invariants?

The key property of the Reynolds operator is: $\rho(g \cdot r) = \rho(r)$ for all $g \in G$, $r \in R$. This means $\rho$ is $G$-invariant as a map (it kills the non-trivial isotypic components). When we reduce mod $p$, $\bar{\rho}(g \cdot r) = \bar{\rho}(r)$ for all $g \in G(\mathbb{F}_p)$, so $\bar{\rho}$ is $G(\mathbb{F}_p)$-invariant. This means $\text{im}(\bar{\rho}) \subseteq (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$.

Also, $\bar{\rho}$ is a projection (idempotent), and its image is $R^G \otimes \mathbb{F}_p$ (since $\rho$ projects onto $R^G$ over $\mathbb{Z}[1/N]$, and tensoring with $\mathbb{F}_p$ preserves the image as long as there's no torsion issue).

Wait, I need to be more careful. $\rho: R \otimes \mathbb{Z}[1/N] \to R \otimes \mathbb{Z}[1/N]$ has image $R^G \otimes \mathbb{Z}[1/N]$. When we tensor with $\mathbb{F}_p$ (for $p \nmid N$), we get $\bar{\rho}: R \otimes \mathbb{F}_p \to R \otimes \mathbb{F}_p$ with image $(R^G \otimes \mathbb{Z}[1/N]) \otimes_{\mathbb{Z}[1/N]} \mathbb{F}_p = R^G \otimes \mathbb{F}_p$.

And we showed $\text{im}(\bar{\rho}) \subseteq (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$.

So $R^G \otimes \mathbb{F}_p \subseteq (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$, which we already knew (this is just the inclusion).

For surjectivity, we need the reverse inclusion. For this, we need $\bar{\rho}$ to be a projection onto $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$, not just onto a subset.

The key property we need: $\bar{\rho}(r) = r$ for all $r \in (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$. If this holds, then $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)} \subseteq \text{im}(\bar{\rho}) = R^G \otimes \mathbb{F}_p$, giving surjectivity.

In characteristic 0, the Reynolds operator satisfies $\rho(r) = r$ for all $G$-invariant $r$. This is because $\rho$ is a projection onto the invariants. But does this property survive reduction mod $p$?

The issue is: an element $r \in R \otimes \mathbb{F}_p$ that is $G(\mathbb{F}_p)$-invariant might not lift to a $G$-invariant element of $R \otimes \mathbb{Z}[1/N]$. If it doesn't, then $\bar{\rho}(r)$ might not equal $r$.

Hmm, so the Reynolds operator approach gives us the inclusion $R^G \otimes \mathbb{F}_p \hookrightarrow (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$ but not necessarily the reverse inclusion.

Let me reconsider. The Reynolds operator $\rho$ over $\mathbb{Q}$ is the unique $G$-equivariant projection onto invariants. It satisfies:
1. $\rho^2 = \rho$ (idempotent)
2. $\rho(g \cdot r) = \rho(r)$ for all $g, r$ ( $G$-invariant)
3. $\rho(r) = r$ for $r \in R^G$ (projection onto invariants)

Properties 1 and 2 are preserved under reduction mod $p$. Property 3 is preserved for elements of $R^G \otimes \mathbb{F}_p$.

But the question is whether $\bar{\rho}$ is a projection onto ALL of $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$.

In characteristic 0, $\rho$ is a projection onto $R_\mathbb{Q}^G$, and every invariant is in the image. In characteristic $p$, the group $G_{\mathbb{F}_p}$ is reductive (geometrically reductive by Haboush) but not linearly reductive (unless $G$ is a torus). So there might not be a Reynolds operator in characteristic $p$.

However, the point is that we're not asking for a Reynolds operator in characteristic $p$; we're asking whether the characteristic 0 Reynolds operator, reduced mod $p$, still captures all invariants.

Let me think about this differently. Consider the exact sequence:
$$0 \to R^G \to R \to R/R^G \to 0$$

Tensoring with $\mathbb{F}_p$:
$$R^G \otimes \mathbb{F}_p \to R \otimes \mathbb{F}_p \to (R/R^G) \otimes \mathbb{F}_p \to 0$$

The invariants $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$ are the kernel of $R \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p) / (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$... this is circular.

Let me think about it using the Reynolds operator more carefully.

Over $\mathbb{Q}$, the Reynolds operator $\rho_\mathbb{Q}: R_\mathbb{Q} \to R_\mathbb{Q}^G$ gives a splitting of the inclusion $R_\mathbb{Q}^G \hookrightarrow R_\mathbb{Q}$. So $R_\mathbb{Q} = R_\mathbb{Q}^G \oplus \ker(\rho_\mathbb{Q})$ as $G$-modules, where $\ker(\rho_\mathbb{Q})$ is the sum of non-trivial isotypic components.

Now, $\rho_\mathbb{Q}$ is defined over $\mathbb{Z}[1/N]$ for some $N$. So over $\mathbb{Z}[1/N]$, we have a splitting:
$$R \otimes \mathbb{Z}[1/N] = (R^G \otimes \mathbb{Z}[1/N]) \oplus \ker(\rho)$$

where $\rho: R \otimes \mathbb{Z}[1/N] \to R^G \otimes \mathbb{Z}[1/N]$ is the Reynolds operator.

Now, for $p \nmid N$, reducing mod $p$:
$$R \otimes \mathbb{F}_p = (R^G \otimes \mathbb{F}_p) \oplus \overline{\ker(\rho)}$$

where $\overline{\ker(\rho)} = \ker(\rho) \otimes \mathbb{F}_p = \ker(\bar{\rho})$.

Now, $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$ is a subspace of $R \otimes \mathbb{F}_p$. We have $R^G \otimes \mathbb{F}_p \subseteq (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$.

The question is: does $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$ have any component in $\ker(\bar{\rho})$?

If $r \in (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$, write $r = r_0 + r_1$ with $r_0 \in R^G \otimes \mathbb{F}_p$ and $r_1 \in \ker(\bar{\rho})$. Then $\bar{\rho}(r) = r_0$. But also, since $r$ is $G(\mathbb{F}_p)$-invariant and $\bar{\rho}$ is $G(\mathbb{F}_p)$-invariant (meaning $\bar{\rho}(g \cdot r) = \bar{\rho}(r)$), we have... hmm, this doesn't directly help.

Actually, let me use the property that $\bar{\rho}(g \cdot r) = \bar{\rho}(r)$ for all $g \in G(\mathbb{F}_p)$. If $r$ is $G(\mathbb{F}_p)$-invariant, then $g \cdot r = r$, so $\bar{\rho}(r) = \bar{\rho}(g \cdot r) = \bar{\rho}(r)$. This is trivially true and doesn't give us new information.

What we need is: $\bar{\rho}(r) = r$ for $r$ invariant. This would follow if $\bar{\rho}$ acts as the identity on invariants. But $\bar{\rho}$ acts as the identity on $R^G \otimes \mathbb{F}_p$ (since $\rho$ acts as identity on $R^G$), but we don't know about other invariants.

So the Reynolds operator approach alone doesn't immediately give surjectivity. We need a more refined argument.

Let me think about this from a different angle. The question is really about whether the formation of invariants commutes with base change for large $p$.

There's a general result in SGA or in the work of Thomason/Trobaugh that for a reductive group $G$ over $\mathbb{Z}$ acting on a finitely generated $\mathbb{Z}$-algebra $R$, the invariants commute with base change for large $p$. But I need to recall the precise statement and proof.

Actually, I think the key result is due to Seshadri and is discussed in various places. Let me think about the proof strategy.

**Strategy:** 
1. Show $R^G$ is finitely generated over $\mathbb{Z}$ (Seshadri's theorem).
2. Show that for large $p$, $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is an isomorphism.

For step 2, the idea is:

Since $R^G$ is finitely generated over $\mathbb{Z}$, we can write $R^G = \mathbb{Z}[f_1, \ldots, f_m]/J$ for some ideal $J$. The $f_i$ are $G$-invariant elements of $R$.

Consider the subalgebra $S = \mathbb{Z}[f_1, \ldots, f_m] \subseteq R$. This is a finitely generated $\mathbb{Z}$-algebra contained in $R^G$.

Over $\mathbb{Q}$, $R_\mathbb{Q}^G = S_\mathbb{Q}$ (since $R^G$ is generated by the $f_i$ over $\mathbb{Q}$, assuming we chose the $f_i$ to generate $R^G \otimes \mathbb{Q}$).

Now, $R$ is a finitely generated $S$-module? No, that's not right in general. $R$ is integral over $R^G$ only if the quotient is finite, which requires the action to have finite quotient.

Hmm, let me think about this differently.

Actually, the standard proof uses the concept of "universally Japanese" rings and the fact that reductive groups are geometrically reductive.

Let me try a different approach. The key fact is:

**Fact:** For a reductive group $G$ over a field $k$ acting on a finitely generated $k$-algebra $A$, if $G$ is geometrically reductive (which is always the case for reductive groups by Haboush's theorem), then $A^G$ is finitely generated.

**Fact:** For a reductive group $G$ over $\mathbb{Z}$ acting on a finitely generated $\mathbb{Z}$-algebra $R$, $R^G$ is finitely generated over $\mathbb{Z}$ (Seshadri).

Now, for the base change question:

**Claim:** For large $p$, $R^G \otimes \mathbb{F}_p \xrightarrow{\sim} (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$.

**Proof sketch:** 
- The map $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is always well-defined and injective (for $R$ torsion-free).
- For surjectivity: Let $A = R^G$ (finitely generated over $\mathbb{Z}$). We have the inclusion $A \hookrightarrow R$. Over $\mathbb{Q}$, $A_\mathbb{Q} = R_\mathbb{Q}^G$ and the Reynolds operator gives a splitting.
- The Reynolds operator $\rho: R_\mathbb{Q} \to A_\mathbb{Q}$ is defined over $\mathbb{Z}[1/N]$ for some $N$.
- For $p \nmid N$, the reduced Reynolds operator $\bar{\rho}: R \otimes \mathbb{F}_p \to A \otimes \mathbb{F}_p$ is a $G_{\mathbb{F}_p}$-equivariant map with $\bar{\rho}|_{A \otimes \mathbb{F}_p} = \text{id}$.
- Now, for any $\bar{r} \in (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$, we have $\bar{\rho}(\bar{r}) \in A \otimes \mathbb{F}_p$ and $\bar{\rho}(\bar{r}) = \bar{\rho}(g \cdot \bar{r})$ for all $g$.
- But we need $\bar{\rho}(\bar{r}) = \bar{r}$. 

Hmm, I keep running into the same issue. Let me think about why $\bar{\rho}(\bar{r}) = \bar{r}$ for invariant $\bar{r}$.

Over $\mathbb{Q}$, $\rho(r) = r$ for $G$-invariant $r$ because $\rho$ is a projection onto invariants: $\rho(r) = r$ and $\rho(r) \in R^G$. The reason is that $\rho$ averages over the group, so for invariant elements, the average is the element itself.

More precisely, the Reynolds operator can be constructed as follows: for a representation $V$ of $G$, $\rho_V: V \to V^G$ is the unique $G$-equivariant map that is the identity on $V^G$. This exists because $G$ is linearly reductive in characteristic 0, so $V = V^G \oplus W$ for some complement $W$, and $\rho_V$ is the projection.

The key property: $\rho_V(v) = v$ for $v \in V^G$. This is built into the construction.

Now, when we reduce mod $p$, $\bar{\rho}_V: V \otimes \mathbb{F}_p \to V \otimes \mathbb{F}_p$ is still a $G$-equivariant idempotent with $\bar{\rho}_V|_{V^G \otimes \mathbb{F}_p} = \text{id}$. But $V^G \otimes \mathbb{F}_p$ might be smaller than $(V \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$.

So the question is: is $\bar{\rho}_V(v) = v$ for $v \in (V \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$?

This is NOT automatic. It would require that the Reynolds operator "sees" all invariants in characteristic $p$, which is related to linear reductivity in characteristic $p$.

But reductive groups in characteristic $p$ are NOT linearly reductive (unless they're tori). So there can be invariants in characteristic $p$ that are not in the image of the Reynolds operator.

Wait, but this would suggest the answer is NO, the map is not necessarily surjective!

Hmm, let me think of a concrete example.

**Example:** Let $G = \text{SL}_2$ acting on $R = \mathbb{Z}[x, y]$ by the standard representation (so $G$ acts on the column vector $(x, y)^T$).

The invariants: $R^{G} = \mathbb{Z}$ (since the only invariant of the standard representation of $\text{SL}_2$ is 0, and constants). Wait, actually for $\text{SL}_2$ acting on $k[x, y]$ by the standard 2-dimensional representation, the invariants are... let me think. The ring $k[x, y]^{\text{SL}_2}$ where $\text{SL}_2$ acts linearly on $(x, y)$. The orbits are: $(0, 0)$ and everything else (since $\text{SL}_2$ acts transitively on nonzero vectors). So the invariants are just the constants. So $R^G = \mathbb{Z}$ and $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)} = \mathbb{F}_p$. The map is $\mathbb{Z} \otimes \mathbb{F}_p = \mathbb{F}_p \to \mathbb{F}_p$, which is an isomorphism. So this example works.

Let me try a more interesting example. Let $G = \text{SL}_2$ acting on $R = \mathbb{Z}[x_1, y_1, x_2, y_2]$ where $\text{SL}_2$ acts on each pair $(x_i, y_i)$ by the standard representation. This is the action on two copies of the standard representation.

The invariants: The ring of invariants $k[x_1, y_1, x_2, y_2]^{\text{SL}_2}$ is generated by the determinant $x_1 y_2 - x_2 y_1$. So $R^G = \mathbb{Z}[x_1 y_2 - x_2 y_1]$.

Over $\mathbb{F}_p$, the invariants $(R \otimes \mathbb{F}_p)^{\text{SL}_2(\mathbb{F}_p)}$ should also be $\mathbb{F}_p[x_1 y_2 - x_2 y_1]$ for large $p$. This is because $\text{SL}_2(\mathbb{F}_p)$ is Zariski dense in $\text{SL}_2$ over $\overline{\mathbb{F}_p}$, so the invariants under $\text{SL}_2(\mathbb{F}_p)$ are the same as the scheme-theoretic invariants.

So the map is $\mathbb{Z}[d] \otimes \mathbb{F}_p = \mathbb{F}_p[d] \to \mathbb{F}_p[d]$, which is an isomorphism. Good.

Now let me think of an example where things might go wrong. The issue with linear reductivity vs geometric reductivity is that in characteristic $p$, there can be invariants that don't lift.

**Classic example of the difference:** Consider $\mathbb{Z}/p\mathbb{Z}$ acting on $k[x]$ by $x \mapsto x + 1$ (in characteristic $p$). The invariants are $k[x^p - x]$. But this is a finite group, not a reductive group.

For reductive groups, the situation is better. Let me think about whether there's an example where the map fails to be surjective.

Actually, I recall now that for reductive groups over $\mathbb{Z}$, the formation of invariants DOES commute with base change for large $p$. This is a theorem that appears in various forms in the literature.

The key insight is that while reductive groups in characteristic $p$ are not linearly reductive, the specific representations that arise from reducing a characteristic 0 representation mod $p$ behave well for large $p$.

Let me try to prove this more carefully.

**Theorem:** Let $G$ be a split reductive group over $\mathbb{Z}$, $R$ a finitely generated $\mathbb{Z}$-algebra that is torsion-free as a $\mathbb{Z}$-module, with a $G$-action. Then there exists $N$ such that for all primes $p > N$, the natural map $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is an isomorphism.

**Proof:**

Step 1: $R^G$ is finitely generated over $\mathbb{Z}$ (Seshadri's theorem, since $G$ is reductive).

Step 2: Let $A = R^G$. We have the inclusion $A \hookrightarrow R$. Over $\mathbb{Q}$, $G_\mathbb{Q}$ is linearly reductive, so there's a Reynolds operator $\rho: R_\mathbb{Q} \to A_\mathbb{Q}$ that is a $G_\mathbb{Q}$-equivariant projection.

Step 3: Since $R$ is finitely generated over $\mathbb{Z}$ and $\rho$ is a $\mathbb{Q}$-linear map, $\rho$ can be spread out: there exists $N$ such that $\rho$ is defined over $\mathbb{Z}[1/N]$, i.e., $\rho: R[1/N] \to A[1/N]$ is a $G$-equivariant projection (where $R[1/N] = R \otimes \mathbb{Z}[1/N]$, etc.).

Step 4: For $p \nmid N$, we have the reduced Reynolds operator $\bar{\rho}: R \otimes \mathbb{F}_p \to A \otimes \mathbb{F}_p$. This is $G_{\mathbb{F}_p}$-equivariant and $\bar{\rho}|_{A \otimes \mathbb{F}_p} = \text{id}$.

Step 5: We need to show $\bar{\rho}$ maps $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ isomorphically to $A \otimes \mathbb{F}_p$, and that $\bar{\rho}(r) = r$ for $r \in (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$.

For this, we use the following key property of the Reynolds operator: $\rho(g \cdot r) = \rho(r)$ for all $g \in G, r \in R[1/N]$. This means $\rho$ is constant on $G$-orbits. Reducing mod $p$: $\bar{\rho}(g \cdot r) = \bar{\rho}(r)$ for all $g \in G(\mathbb{F}_p), r \in R \otimes \mathbb{F}_p$.

Now, if $r \in (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$, then $g \cdot r = r$ for all $g$, so $\bar{\rho}(r) = \bar{\rho}(g \cdot r) = \bar{\rho}(r)$. This is trivially true.

But we also know that $\bar{\rho}(r) \in A \otimes \mathbb{F}_p$ and $\bar{\rho}$ is a projection onto $A \otimes \mathbb{F}_p$. The issue is whether $\bar{\rho}(r) = r$.

Hmm, let me think about this differently. The Reynolds operator $\rho$ satisfies $\rho^2 = \rho$ (idempotent). So $\bar{\rho}^2 = \bar{\rho}$. The image of $\bar{\rho}$ is $A \otimes \mathbb{F}_p$ (since $\rho$ projects onto $A[1/N]$ and we reduce mod $p$). The kernel of $\bar{\rho}$ is the reduction of $\ker(\rho)$.

Now, $R \otimes \mathbb{F}_p = \text{im}(\bar{\rho}) \oplus \ker(\bar{\rho}) = (A \otimes \mathbb{F}_p) \oplus \ker(\bar{\rho})$.

If $r \in (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$, write $r = a + b$ with $a \in A \otimes \mathbb{F}_p$ and $b \in \ker(\bar{\rho})$. Then $\bar{\rho}(r) = a$.

We need to show $b = 0$, i.e., $r = a \in A \otimes \mathbb{F}_p$.

Since $r$ is $G(\mathbb{F}_p)$-invariant and $a$ is $G(\mathbb{F}_p)$-invariant (because $a \in A \otimes \mathbb{F}_p = R^G \otimes \mathbb{F}_p$), we have $b = r - a$ is also $G(\mathbb{F}_p)$-invariant. So $b \in \ker(\bar{\rho}) \cap (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$.

So the question reduces to: is $\ker(\bar{\rho}) \cap (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)} = 0$ for large $p$?

Over $\mathbb{Q}$, $\ker(\rho_\mathbb{Q}) \cap R_\mathbb{Q}^G = 0$ because $\rho_\mathbb{Q}$ is a projection onto $R_\mathbb{Q}^G$, so $\ker(\rho_\mathbb{Q})$ is a complement of $R_\mathbb{Q}^G$.

But in characteristic $p$, there might be new invariants in $\ker(\bar{\rho})$.

This is exactly the issue of linear reductivity vs geometric reductivity. In characteristic $p$, $G_{\mathbb{F}_p}$ is geometrically reductive but not linearly reductive, so there can be invariants that are not captured by the Reynolds operator.

However, the question is whether this actually happens for representations that come from reducing a characteristic 0 representation.

Let me think about a specific example where this fails.

**Example:** Consider $G = \text{SL}_p$ in characteristic $p$. The center of $\text{SL}_p$ in characteristic $p$ is $\mu_p$, which is not reduced. The representation theory of $\text{SL}_p$ in characteristic $p$ is more complicated than in characteristic 0.

But for large $p$ (specifically, $p$ larger than the weights of the representation), the representation theory should be the same.

Actually, I think the key point is the following: for a given representation $V$ of $G$ over $\mathbb{Z}$ (i.e., a $\mathbb{Z}$-free $\mathbb{Z}$-module with $G$-action), the representation $V \otimes \mathbb{F}_p$ has the same character as $V \otimes \mathbb{C}$ for all $p$. For $p$ larger than the weights of $V$ (or more precisely, for $p$ not dividing certain factorials related to the Weyl group), the representation theory of $G_{\mathbb{F}_p}$ on $V \otimes \mathbb{F}_p$ is "the same" as in characteristic 0, meaning the invariant subspaces have the same dimension.

This is related to the "linkage principle" and the behavior of Weyl modules for large $p$.

More precisely, for a split reductive group $G$ over $\mathbb{Z}$ and a representation $V$ that is a Weyl module (which is the case for representations coming from $\mathbb{Z}$), the character of $V \otimes \mathbb{F}_p$ is given by Weyl's character formula for $p$ larger than the weights. And the dimension of the invariant subspace $(V \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ equals $\dim(V \otimes \mathbb{C})^{G_\mathbb{C}}$ for large $p$.

This would give us that $\dim(R^G \otimes \mathbb{F}_p) = \dim((R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}})$ for large $p$ (in each degree), and since we have an injection $R^G \otimes \mathbb{F}_p \hookrightarrow (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$, it would be an isomorphism.

But wait, $R$ is not a single representation; it's a polynomial ring (or a quotient), which is an infinite-dimensional representation (direct sum of finite-dimensional pieces by degree). We need to apply the argument degree by degree.

Let me formalize this. Assume $R = \mathbb{Z}[x_1, \ldots, x_n]$ (polynomial ring) with a linear $G$-action, meaning $G$ acts on the vector space spanned by $x_1, \ldots, x_n$, and this extends to the polynomial ring. Then $R = \bigoplus_{d \geq 0} R_d$ where $R_d$ is the degree-$d$ part, and each $R_d$ is a finite-dimensional $G$-module (a Weyl module, or more precisely, the $d$-th symmetric power of the representation on $R_1$).

For each $d$, $R_d$ is a finite-rank free $\mathbb{Z}$-module with $G$-action. The representation $R_d \otimes \mathbb{C}$ is a representation of $G_\mathbb{C}$, and $R_d \otimes \mathbb{F}_p$ is a representation of $G_{\mathbb{F}_p}$.

For large $p$ (depending on $d$ and the representation), $\dim((R_d \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}) = \dim((R_d \otimes \mathbb{C})^{G_\mathbb{C}}) = \text{rank}((R_d)^G)$.

But we need this for ALL $d$ simultaneously, and $d$ is unbounded. So we can't just pick $p$ large enough for each $d$.

Hmm, this is a problem. The issue is that for each degree $d$, there's a threshold $p_d$ such that for $p > p_d$, the invariants in degree $d$ are correct. But $p_d$ might grow with $d$, so there might not be a single $p$ that works for all degrees.

Wait, but actually, the invariants $R^G$ are finitely generated. So there are finitely many homogeneous invariants $f_1, \ldots, f_m$ that generate $R^G$ as a $\mathbb{Z}$-algebra. Let $D = \max(\deg f_i)$. Then for $d > D$, the invariants in degree $d$ are generated by products of the $f_i$, and their structure is determined by the lower degrees.

Hmm, but this doesn't directly help because the relations between the $f_i$ might also involve higher degrees.

Let me think about this more carefully.

Actually, I think the correct approach is:

1. $R^G$ is finitely generated over $\mathbb{Z}$, say by homogeneous elements $f_1, \ldots, f_m$ of degrees $d_1, \ldots, d_m$.
2. Let $S = \mathbb{Z}[f_1, \ldots, f_m] \subseteq R^G$. Over $\mathbb{Q}$, $S_\mathbb{Q} = R_\mathbb{Q}^G$ (since the $f_i$ generate $R^G$ over $\mathbb{Z}$, hence over $\mathbb{Q}$).
3. The quotient $R^G / S$ is a finitely generated $\mathbb{Z}$-module (since $R^G$ is finitely generated over $\mathbb{Z}$ and $S$ is a subalgebra over which $R^G$ is finite... wait, is $R^G$ finite over $S$?).

Actually, $R^G = S$ if the $f_i$ generate $R^G$ as a $\mathbb{Z}$-algebra. So $R^G = \mathbb{Z}[f_1, \ldots, f_m] / I$ for some ideal $I$ (the relations). But $R^G$ is a subring of $R$ which is torsion-free, so $R^G$ is torsion-free, and $R^G = \mathbb{Z}[f_1, \ldots, f_m] / I$ where $I$ is the ideal of relations.

Hmm, this is getting complicated. Let me try a cleaner approach.

**Clean approach using the Reynolds operator and finite generation:**

Since $R^G$ is finitely generated over $\mathbb{Z}$, let $f_1, \ldots, f_m$ be homogeneous generators. Let $S = \mathbb{Z}[f_1, \ldots, f_m] \subseteq R$. Then $S \subseteq R^G$ and $S \otimes \mathbb{Q} = R^G \otimes \mathbb{Q}$ (the $f_i$ generate $R^G$ over $\mathbb{Q}$).

Now, $R^G / S$ is a finitely generated $\mathbb{Z}$-module (is it? $R^G$ is a finitely generated $S$-module because... actually, $R^G = S$ if the $f_i$ generate $R^G$ as a $\mathbb{Z}$-algebra. But $R^G$ might not equal $S$ as a $\mathbb{Z}$-module; there might be $\mathbb{Z}$-torsion-free elements in $R^G$ that are not in $S$ but become equal over $\mathbb{Q}$.)

Wait, if $f_1, \ldots, f_m$ generate $R^G$ as a $\mathbb{Z}$-algebra, then $R^G = S$ (by definition, $S$ is the $\mathbb{Z}$-subalgebra generated by the $f_i$, which is $R^G$). So $R^G = S$.

OK so $R^G = \mathbb{Z}[f_1, \ldots, f_m]$ (as a $\mathbb{Z}$-algebra, meaning it's the image of the polynomial ring $\mathbb{Z}[T_1, \ldots, T_m]$ under $T_i \mapsto f_i$, so $R^G \cong \mathbb{Z}[T_1, \ldots, T_m] / I$ for some ideal $I$).

Now, the map $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ sends $f_i \otimes 1 \mapsto f_i \otimes 1$ (which is $G_{\mathbb{F}_p}$-invariant since $f_i$ is $G$-invariant).

The image of this map is $\mathbb{F}_p[f_1 \otimes 1, \ldots, f_m \otimes 1] \subseteq (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$.

For surjectivity, we need $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}} = \mathbb{F}_p[f_1 \otimes 1, \ldots, f_m \otimes 1]$.

Now, over $\mathbb{Q}$, $(R \otimes \mathbb{Q})^{G_\mathbb{Q}} = \mathbb{Q}[f_1, \ldots, f_m]$ (since $R^G = \mathbb{Z}[f_1, \ldots, f_m]$ and $R^G \otimes \mathbb{Q} = (R \otimes \mathbb{Q})^{G_\mathbb{Q}}$ by linear reductivity in char 0).

Over $\mathbb{F}_p$, $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is finitely generated (by Haboush's theorem / geometric reductivity). The question is whether it's generated by the reductions of $f_1, \ldots, f_m$.

This is the question of whether the generators of invariants in characteristic 0 reduce to generators in characteristic $p$.

I believe the answer is yes for large $p$, and the proof uses the Reynolds operator in a more subtle way.

Let me try yet another approach. The key is the following:

**Lemma:** Let $V$ be a finite-rank free $\mathbb{Z}$-module with $G$-action (a representation of $G$ over $\mathbb{Z}$). Then for sufficiently large $p$, $\dim_{\mathbb{F}_p} (V \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}} = \text{rank}_{\mathbb{Z}} V^G$.

If this lemma holds, then applying it degree by degree to $R = \bigoplus_d R_d$ and using finite generation of $R^G$, we can conclude.

But the issue is that the "sufficiently large $p$" depends on the representation $V = R_d$, and $d$ is unbounded.

However, for the polynomial ring case, all $R_d$ are symmetric powers of $R_1$, and the representation theory of symmetric powers is well-understood. For $p$ larger than the dimension of $R_1$ (or some bound depending on $G$ and $R_1$), the symmetric powers behave the same in all characteristics.

Actually, I think the correct statement is:

**For a reductive group $G$ over $\mathbb{Z}$ and a representation $V$ on a free $\mathbb{Z}$-module of finite rank, there exists $N$ (depending on $G$ and $V$) such that for $p > N$, the natural map $V^G \otimes \mathbb{F}_p \to (V \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is an isomorphism.**

This is because for large $p$, the representation $V \otimes \mathbb{F}_p$ is "the same" as $V \otimes \mathbb{C}$ in terms of composition factors, and the trivial representation appears with the same multiplicity.

More precisely, for a split reductive group, the Weyl modules $\Delta(\lambda)$ have characters given by Weyl's character formula, and for $p$ larger than the weights of $V$, the module $V \otimes \mathbb{F}_p$ has the same composition factor multiplicities as $V \otimes \mathbb{C}$. In particular, the multiplicity of the trivial representation is the same.

But for the polynomial ring, $V = R_d = \text{Sym}^d(R_1)$, and the weights grow with $d$. So the threshold $p_d$ grows with $d$, and we can't find a single $p$ that works for all $d$.

This seems like a real obstruction. But wait—the invariants are finitely generated, so we don't need to check all degrees independently. We only need to check up to the degrees of the generators and relations.

Let me think about this more carefully.

$R^G = \mathbb{Z}[f_1, \ldots, f_m]$ with $\deg f_i = d_i$. Let $D = \max d_i$. The invariants in degrees $\leq D$ determine all invariants (since higher degree invariants are products of the generators, subject to relations that also have bounded degree).

Actually, the relations also have bounded degree. If $R^G = \mathbb{Z}[T_1, \ldots, T_m]/I$, then $I$ is generated by homogeneous polynomials of some bounded degree $D'$ (by Hilbert's syzygy theorem or Noetherianity). So the structure of $R^G$ is determined by degrees $\leq \max(D, D')$.

Now, for $p$ large enough that the invariants in degrees $\leq \max(D, D')$ are correct (i.e., $R^G_d \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)_d^{G_{\mathbb{F}_p}}$ is an isomorphism for $d \leq \max(D, D')$), the entire invariant ring should be correct.

But wait, this isn't quite right either. The invariants in degree $d > D$ are determined by the generators and relations, but the invariants $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ in degree $d > D$ might have "new" generators that don't come from the characteristic 0 generators.

Hmm, but if $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is generated by elements of degree $\leq D'$ (some bound), and for large $p$ the invariants in degrees $\leq D'$ are all reductions of characteristic 0 invariants, then we're fine.

The question is: is there a uniform bound on the degrees of generators of $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ that's independent of $p$?

For reductive groups, there's a result (due to Fogarty, or derived from the Hochster-Roberts theorem and its refinements) that gives bounds on the degrees of generators. But these bounds might depend on $p$.

Actually, I think there's a cleaner way to see this. Let me use the Reynolds operator approach more carefully.

**Key idea:** The Reynolds operator $\rho: R \otimes \mathbb{Q} \to R^G \otimes \mathbb{Q}$ can be spread out to $\mathbb{Z}[1/N]$. For $p \nmid N$, we have $\bar{\rho}: R \otimes \mathbb{F}_p \to R^G \otimes \mathbb{F}_p$.

Now, $\bar{\rho}$ is $G_{\mathbb{F}_p}$-equivariant and $\bar{\rho}|_{R^G \otimes \mathbb{F}_p} = \text{id}$. Also, $\bar{\rho}(g \cdot r) = \bar{\rho}(r)$ for all $g \in G(\mathbb{F}_p)$ (this is because $\rho(g \cdot r) = \rho(r)$ over $\mathbb{Z}[1/N]$, and this property is preserved under reduction).

Now, let $\bar{r} \in (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$. Then $g \cdot \bar{r} = \bar{r}$ for all $g \in G(\mathbb{F}_p)$, so $\bar{\rho}(\bar{r}) = \bar{\rho}(g \cdot \bar{r}) = \bar{\rho}(\bar{r})$. This is trivially true.

But we also have: $\bar{\rho}(\bar{r}) \in R^G \otimes \mathbb{F}_p$, and $\bar{\rho}(\bar{\rho}(\bar{r})) = \bar{\rho}(\bar{r})$ (idempotent). So $\bar{\rho}(\bar{r})$ is an invariant that's in $R^G \otimes \mathbb{F}_p$.

The question is: is $\bar{r} = \bar{\rho}(\bar{r})$? I.e., is $\bar{r} - \bar{\rho}(\bar{r}) = 0$?

We have $\bar{r} - \bar{\rho}(\bar{r}) \in \ker(\bar{\rho})$ (since $\bar{\rho}(\bar{r} - \bar{\rho}(\bar{r})) = \bar{\rho}(\bar{r}) - \bar{\rho}(\bar{r}) = 0$). And $\bar{r} - \bar{\rho}(\bar{r})$ is $G(\mathbb{F}_p)$-invariant (since both $\bar{r}$ and $\bar{\rho}(\bar{r})$ are).

So $\bar{r} - \bar{\rho}(\bar{r}) \in \ker(\bar{\rho}) \cap (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$.

We need this to be 0. Over $\mathbb{Q}$, $\ker(\rho) \cap R^G_\mathbb{Q} = 0$ (since $\rho$ is a projection onto $R^G_\mathbb{Q}$). But in characteristic $p$, this might not hold.

However, $\ker(\bar{\rho})$ is the reduction of $\ker(\rho) \otimes \mathbb{Z}[1/N]$, and $\ker(\rho) \otimes \mathbb{Q}$ contains no $G$-invariants. So $\ker(\rho) \otimes \mathbb{Q}$ is a $G$-module with no trivial subrepresentation.

For large $p$, $\ker(\rho) \otimes \mathbb{F}_p$ should also have no trivial subrepresentation (as a $G_{\mathbb{F}_p}$-module), because the representation theory is "the same" for large $p$.

But $\ker(\rho)$ is not a finite-rank $\mathbb{Z}$-module; it's a submodule of $R \otimes \mathbb{Z}[1/N]$, which is infinite-dimensional. So we can't directly apply the "large $p$" argument to the whole thing.

However, we can apply it degree by degree. For each degree $d$, $\ker(\rho)_d$ is a finite-rank $\mathbb{Z}[1/N]$-module, and for large $p$ (depending on $d$), $\ker(\rho)_d \otimes \mathbb{F}_p$ has no $G_{\mathbb{F}_p}$-invariants.

The issue is again that the threshold depends on $d$. But since $R^G$ is finitely generated, we only need to worry about degrees up to some bound.

Wait, actually, I think the point is this: we don't need to show that $\ker(\bar{\rho})_d$ has no invariants for ALL $d$. We need to show that the map $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is surjective. This means: every invariant in $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is in the image of $R^G \otimes \mathbb{F}_p$.

If $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is generated by elements of degree $\leq D$ (for some $D$ independent of $p$), and for $p$ large enough, the invariants in degrees $\leq D$ all come from $R^G$, then we're done.

So the question reduces to: is there a uniform bound $D$ on the degrees of generators of $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ that's independent of $p$?

For a reductive group acting on a polynomial ring, the degrees of generators of the invariant ring are bounded by a function of the group and the representation, independent of the characteristic. This is because:

1. By the Hochster-Roberts theorem (and its generalizations), the invariant ring is Cohen-Macaulay (in char 0) or at least has bounded properties.
2. The Hilbert series of the invariant ring is the same in all characteristics (for large $p$), because it's determined by the Molien series / character of the representation, which is independent of $p$.

Actually, the Hilbert series of $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ might NOT be the same as that of $R^G \otimes \mathbb{Q}$ for small $p$, but for large $p$ it should be.

Hmm, let me think about this differently. Let me use the following approach:

**Approach via finite generation and spreading out:**

1. $R^G$ is finitely generated over $\mathbb{Z}$: $R^G = \mathbb{Z}[f_1, \ldots, f_m]$.
2. Let $A = \mathbb{Z}[f_1, \ldots, f_m] = R^G$. We have $A \hookrightarrow R$.
3. Over $\mathbb{Q}$, $A_\mathbb{Q} = (R_\mathbb{Q})^{G_\mathbb{Q}}$ and the quotient $R_\mathbb{Q} / A_\mathbb{Q}$ has no $G$-invariants (by the Reynolds operator).
4. The Reynolds operator $\rho: R_\mathbb{Q} \to A_\mathbb{Q}$ spreads out to $\mathbb{Z}[1/N]$: $\rho: R[1/N] \to A[1/N]$.
5. For $p \nmid N$, $\bar{\rho}: R_p \to A_p$ (where $R_p = R \otimes \mathbb{F}_p$, $A_p = A \otimes \mathbb{F}_p$).
6. $\bar{\rho}$ is $G$-equivariant, $\bar{\rho}^2 = \bar{\rho}$, $\bar{\rho}|_{A_p} = \text{id}$, and $\bar{\rho}(g \cdot r) = \bar{\rho}(r)$ for all $g \in G(\mathbb{F}_p)$.

Now, consider the $G_{\mathbb{F}_p}$-module $M = R_p / A_p$. The Reynolds operator induces a map $\bar{\rho}: M \to 0$ (since $\bar{\rho}$ projects onto $A_p$), so $\bar{\rho}$ is the zero map on $M$. This means $M = \ker(\bar{\rho}) / (A_p \cap \ker(\bar{\rho})) = \ker(\bar{\rho})$ (since $A_p \cap \ker(\bar{\rho}) = 0$ because $\bar{\rho}|_{A_p} = \text{id}$).

So $M = \ker(\bar{\rho})$ as a $G_{\mathbb{F}_p}$-module.

Now, $(R_p)^{G_{\mathbb{F}_p}} / A_p = (R_p)^{G_{\mathbb{F}_p}} / (R_p)^{G_{\mathbb{F}_p}} \cap A_p$... hmm, this isn't quite right because $A_p \subseteq (R_p)^{G_{\mathbb{F}_p}}$.

Let me reconsider. We have the short exact sequence of $G_{\mathbb{F}_p}$-modules:
$$0 \to A_p \to R_p \to M \to 0$$

Taking $G_{\mathbb{F}_p}$-invariants:
$$0 \to A_p^{G_{\mathbb{F}_p}} \to R_p^{G_{\mathbb{F}_p}} \to M^{G_{\mathbb{F}_p}} \to H^1(G_{\mathbb{F}_p}, A_p) \to \cdots$$

Since $A_p \subseteq R_p^G \otimes \mathbb{F}_p \subseteq R_p^{G_{\mathbb{F}_p}}$, we have $A_p^{G_{\mathbb{F}_p}} = A_p$.

So:
$$0 \to A_p \to R_p^{G_{\mathbb{F}_p}} \to M^{G_{\mathbb{F}_p}} \to H^1(G_{\mathbb{F}_p}, A_p) \to \cdots$$

The map $A_p \to R_p^{G_{\mathbb{F}_p}}$ is the inclusion we're studying. It's surjective iff $M^{G_{\mathbb{F}_p}} = 0$ (assuming $H^1$ doesn't interfere, but actually the surjectivity of $A_p \to R_p^{G_{\mathbb{F}_p}}$ is equivalent to $M^{G_{\mathbb{F}_p}} = 0$ from the exact sequence, since the next term would be in $H^1$ which is about extensions, not about the cokernel).

Wait, let me be more careful. The long exact sequence is:
$$0 \to A_p \to R_p^{G_{\mathbb{F}_p}} \to M^{G_{\mathbb{F}_p}} \xrightarrow{\delta} H^1(G_{\mathbb{F}_p}, A_p) \to H^1(G_{\mathbb{F}_p}, R_p) \to \cdots$$

So $R_p^{G_{\mathbb{F}_p}} / A_p = \ker(\delta: M^{G_{\mathbb{F}_p}} \to H^1(G_{\mathbb{F}_p}, A_p))$.

For surjectivity of $A_p \to R_p^{G_{\mathbb{F}_p}}$, we need $R_p^{G_{\mathbb{F}_p}} / A_p = 0$, which means $\ker(\delta) = 0$, i.e., $\delta$ is injective on $M^{G_{\mathbb{F}_p}}$.

A sufficient condition is $M^{G_{\mathbb{F}_p}} = 0$.

Now, $M = \ker(\bar{\rho})$ as a $G_{\mathbb{F}_p}$-module. Over $\mathbb{Q}$, $M_\mathbb{Q} = \ker(\rho_\mathbb{Q})$ has no $G$-invariants (since $\rho_\mathbb{Q}$ is a projection onto $R_\mathbb{Q}^G$). So $M_\mathbb{Q}^G = 0$.

For large $p$, $M \otimes \mathbb{F}_p$ should also have no $G_{\mathbb{F}_p}$-invariants, IF the representation theory is "the same." But $M$ is infinite-dimensional, so we need to be careful.

However, $M$ is a graded module, and in each degree $d$, $M_d$ is a finite-rank free $\mathbb{Z}[1/N]$-module. For each $d$, there exists $p_d$ such that for $p > p_d$, $(M_d \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}} = 0$.

The issue is whether $\sup_d p_d < \infty$.

For the polynomial ring case, $M_d = \ker(\rho)_d$ is a subquotient of $R_d = \text{Sym}^d(R_1)$. The representation $R_d$ is a Weyl module (or a direct sum of Weyl modules), and for $p$ larger than the weights of $R_d$, the representation theory is the same as in characteristic 0.

The weights of $R_d = \text{Sym}^d(R_1)$ grow linearly with $d$ (the highest weight is $d$ times the highest weight of $R_1$). So the threshold $p_d$ grows linearly with $d$, and $\sup_d p_d = \infty$.

This means we can't find a single $p$ that works for all degrees simultaneously, at least not by this naive argument.

But wait—this doesn't mean the result is false. It means the naive approach doesn't work. The actual result might still be true, but requires a more sophisticated argument.

Let me reconsider. The key insight I'm missing might be that $R^G$ is finitely generated, so the structure of the invariant ring is determined by finitely many degrees, and we only need $p$ to be large enough for those degrees.

More precisely: $R^G = \mathbb{Z}[f_1, \ldots, f_m]$ with $\deg f_i \leq D$. The relations among the $f_i$ have degree $\leq D'$. The "Noether number" (bound on degrees of generators) for the invariant ring is $D$.

Now, for the invariant ring $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$, we need to know that it's also generated by elements of degree $\leq D$ (for large $p$). If this is the case, then we only need $p$ to be large enough for degrees $\leq D$, and the threshold $p_D$ is finite.

Is there a uniform bound on the Noether number for invariant rings of reductive groups, independent of the characteristic?

For finite groups, the Noether number is bounded by $|G|$ (Noether's bound), but this depends on the group order, which for $G(\mathbb{F}_p)$ grows with $p$. However, we're taking invariants under the group scheme $G_{\mathbb{F}_p}$ (or equivalently, under $G(\mathbb{F}_p)$ which is Zariski dense), not under the finite group $G(\mathbb{F}_p)$.

For reductive group schemes, there's a result by Fogarty and others that gives bounds on the degrees of generators. But I'm not sure if these bounds are independent of $p$.

Actually, let me think about this from the perspective of the Hilbert series.

The Hilbert series of $R^G \otimes \mathbb{Q} = (R \otimes \mathbb{Q})^{G_\mathbb{Q}}$ is:
$$H(R^G_\mathbb{Q}, t) = \sum_d \dim((R_d \otimes \mathbb{Q})^{G_\mathbb{Q}}) t^d$$

For a reductive group in characteristic 0, this is a rational function (by finite generation). The Hilbert series of $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is:
$$H((R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}, t) = \sum_d \dim((R_d \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}) t^d$$

For large $p$, $\dim((R_d \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}) = \dim((R_d \otimes \mathbb{Q})^{G_\mathbb{Q}})$ for each fixed $d$ (by the representation theory argument). But this doesn't mean the Hilbert series are equal as formal power series, because the threshold $p_d$ grows with $d$.

However, if both Hilbert series are rational functions with the same denominator (which they are, for large $p$, by the structure of the invariant ring), and they agree on infinitely many coefficients (which they do for any fixed $p$ large enough, for all $d$ up to some bound), then... hmm, this doesn't quite work either.

Let me try a completely different approach. I'll use the theory of "good primes" for reductive groups.

**Good primes:** For a reductive group $G$, a prime $p$ is called "good" if $p$ doesn't divide the coefficients of the highest root. For simply-connected semisimple groups, good primes are those for which the representation theory behaves well.

For good primes $p$, the representation theory of $G_{\mathbb{F}_p}$ is closely related to that of $G_\mathbb{C}$. In particular, for a Weyl module $V$ with highest weight $\lambda$, if $p$ is good (and $p$ is larger than the Coxeter number or something like that), then $V \otimes \mathbb{F}_p$ is irreducible (or has the same composition factors as $V \otimes \mathbb{C}$).

But even for good primes, the threshold for "large $p$" depends on the weight $\lambda$, which grows with the degree.

I think the resolution is that we need to use the finite generation of $R^G$ more cleverly.

**Here's the key argument:**

1. $R^G = \mathbb{Z}[f_1, \ldots, f_m]$ is finitely generated, with $f_i$ homogeneous of degrees $d_i \leq D$.
2. Let $S = \mathbb{Z}[T_1, \ldots, T_m]$ and $\phi: S \to R^G$ sending $T_i \mapsto f_i$. Then $R^G = S / \ker(\phi)$.
3. $\ker(\phi)$ is a homogeneous ideal in $S$, finitely generated by homogeneous polynomials of degrees $\leq D'$ (by Noetherianity).
4. Over $\mathbb{Q}$, $(R \otimes \mathbb{Q})^{G_\mathbb{Q}} = R^G \otimes \mathbb{Q} = (S/\ker(\phi)) \otimes \mathbb{Q}$.
5. The map $S \to R$ sending $T_i \mapsto f_i$ has image $R^G \subseteq R$. Over $\mathbb{Q}$, the image is $R_\mathbb{Q}^G$.
6. For each degree $d \leq \max(D, D')$, the map $R^G_d \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)_d^{G_{\mathbb{F}_p}}$ is an isomorphism for $p > p_0$ (where $p_0$ depends on $\max(D, D')$ and the representation).
7. For $d > \max(D, D')$, the invariants in $R^G_d$ are determined by the generators and relations (which are in degrees $\leq \max(D, D')$). Similarly, the invariants in $(R \otimes \mathbb{F}_p)_d^{G_{\mathbb{F}_p}}$ are determined by the generators and relations in degrees $\leq$ some bound.

But step 7 is the problematic one. The invariants in $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ in high degrees might have "new" generators that don't exist in characteristic 0.

Hmm, but actually, if $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is generated by elements of degree $\leq D$ (the same bound as in characteristic 0), then we're fine. The question is whether this is the case.

**Claim:** For large $p$, $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is generated by elements of degree $\leq D$, where $D$ is the Noether number in characteristic 0.

This would follow if the Hilbert series of $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ equals the Hilbert series of $R^G \otimes \mathbb{Q}$ for large $p$ (as formal power series, not just coefficient by coefficient up to some bound).

The Hilbert series of $R^G \otimes \mathbb{Q}$ is a rational function $H(t) = P(t) / Q(t)$. If the Hilbert series of $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is also $H(t)$ for large $p$, then the invariant rings have the same Hilbert series, and since one is a subring of the other, they must be equal.

But why would the Hilbert series be the same? The Hilbert series is determined by the dimensions of the invariant subspaces in each degree, and these dimensions are the multiplicities of the trivial representation in $R_d \otimes \mathbb{F}_p$.

For a Weyl module $V(\lambda)$, the multiplicity of the trivial representation in $V(\lambda) \otimes \mathbb{F}_p$ equals the multiplicity in $V(\lambda) \otimes \mathbb{C}$ for $p$ larger than some bound depending on $\lambda$. But $\lambda$ grows with $d$, so the bound grows with $d$.

However, the multiplicity of the trivial representation in $\text{Sym}^d(V)$ is given by a formula that's a quasi-polynomial in $d$ (by the Molien series / character integration). This formula is independent of $p$ (it's determined by the Weyl group and the representation). For large $p$, the actual multiplicity in characteristic $p$ agrees with this formula.

But "large $p$" depends on $d$... unless the formula is a polynomial (not just a quasi-polynomial) and the agreement holds for all $d$ when $p$ is large enough.

Actually, I think the key fact is:

**For a reductive group $G$ over $\mathbb{Z}$ and a representation $V$ on a free $\mathbb{Z}$-module, the Hilbert series of $\text{Sym}(V)^G$ is the same in all characteristics for sufficiently large $p$.**

This is because the Hilbert series is determined by the character of $V$, which is independent of $p$, and for large $p$, the multiplicity of the trivial representation in $\text{Sym}^d(V) \otimes \mathbb{F}_p$ equals the multiplicity in $\text{Sym}^d(V) \otimes \mathbb{C}$ for ALL $d$ (not just $d$ up to some bound).

Wait, is this true? Let me think about why.

The multiplicity of the trivial representation in $\text{Sym}^d(V)$ is:
$$\dim \text{Hom}_G(\mathbf{1}, \text{Sym}^d(V)) = \frac{1}{|W|} \sum_{w \in W} \epsilon(w) \cdot [\text{something involving the character of } V \text{ at } w]$$

Actually, by the Weyl character formula and the Cauchy identity, the Hilbert series of $\text{Sym}(V)^G$ is:
$$H(t) = \sum_{d} \dim(\text{Sym}^d(V)^G) t^d = \prod_{i} \frac{1}{1 - t^{a_i}} \cdot \prod_j (1 - t^{b_j})$$

or something like that (the exact formula depends on the group and representation). The point is that this is a rational function determined by the root system and the representation, independent of $p$.

For large $p$, the actual Hilbert series of $(\text{Sym}(V) \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ equals this rational function. This is because:

1. The character of $V \otimes \mathbb{F}_p$ is the same as $V \otimes \mathbb{C}$ (since $V$ is defined over $\mathbb{Z}$).
2. For large $p$, the representation $\text{Sym}^d(V) \otimes \mathbb{F}_p$ has the same character as $\text{Sym}^d(V) \otimes \mathbb{C}$.
3. The multiplicity of the trivial representation can be computed from the character by the Weyl integration formula, which is independent of $p$.
4. For large $p$, this computation is valid in characteristic $p$ as well.

The key point is step 4: for large $p$, the representation theory is "the same" in the sense that the multiplicity of the trivial representation in any Weyl module is the same as in characteristic 0. And this holds for ALL weights, not just weights up to some bound, when $p$ is a "good prime" (or more precisely, when $p$ is larger than the Coxeter number).

Actually, I think the precise statement is:

**Theorem (Jantzen, or standard in modular representation theory):** For a split reductive group $G$ over $\mathbb{Z}$, if $p$ is larger than the Coxeter number $h$ of $G$, then for any dominant weight $\lambda$, the Weyl module $\Delta(\lambda) \otimes \mathbb{F}_p$ has the same character as $\Delta(\lambda) \otimes \mathbb{C}$, and the multiplicity of the trivial representation in any module is determined by the character.

More precisely, for $p > h$ (the Coxeter number), the linkage principle simplifies, and the composition factors of Weyl modules are "the same" as in characteristic 0 (in terms of characters). This means the multiplicity of the trivial representation in $\text{Sym}^d(V) \otimes \mathbb{F}_p$ is the same as in $\text{Sym}^d(V) \otimes \mathbb{C}$ for ALL $d$, when $p > h$.

Wait, I don't think this is exactly right. The statement about $p > h$ is about the Steinberg tensor product theorem and the structure of Weyl modules, but it doesn't immediately imply that all multiplicities are the same.

Let me think about this more carefully. The character of $\text{Sym}^d(V) \otimes \mathbb{F}_p$ is the same as $\text{Sym}^d(V) \otimes \mathbb{C}$ for all $p$ (since the character is determined by the formal character, which is defined over $\mathbb{Z}$). The question is whether the multiplicity of the trivial representation in $\text{Sym}^d(V) \otimes \mathbb{F}_p$ equals the multiplicity computed from the character.

In characteristic 0, the multiplicity of the trivial representation in a module $M$ is:
$$\dim M^G = \langle \text{ch}(M), \text{ch}(\mathbf{1}) \rangle = \frac{1}{|W|} \sum_{w \in W} \text{ch}(M)(w \cdot \rho - \rho) \cdot (\text{something})$$

Wait, the multiplicity of the trivial representation in a module with character $\chi$ is given by the inner product:
$$\langle \chi, 1 \rangle = \frac{1}{|W|} \sum_{w \in W} \chi(w)$$

where $\chi(w)$ is the value of the character at the Weyl group element $w$ (more precisely, at the corresponding element of the maximal torus). This is the Weyl integration formula for the trivial representation.

In characteristic $p$, the multiplicity of the trivial representation in a module $M$ is NOT simply given by the character inner product, because the module might not be semisimple. The multiplicity is the dimension of $\text{Hom}_G(\mathbf{1}, M)$, which is the dimension of the invariant subspace.

For a Weyl module $\Delta(\lambda)$ in characteristic $p$, the character is the same as in characteristic 0, but the module might not be irreducible, and the trivial representation might appear as a composition factor even if it doesn't in characteristic 0 (or vice versa).

However, the key point is: $\dim \text{Hom}_G(\mathbf{1}, M) = \dim M^G$ is the dimension of the invariant subspace, which is the multiplicity of the trivial representation as a DIRECT SUMMAND (or more precisely, the dimension of the space of $G$-equivariant maps from $\mathbf{1}$ to $M$).

In characteristic 0, $M$ is semisimple, so $\dim M^G = \langle \text{ch}(M), 1 \rangle$.

In characteristic $p$, $M$ might not be semisimple, so $\dim M^G$ might differ from $\langle \text{ch}(M), 1 \rangle$.

But for $p$ large enough (specifically, $p > h$ where $h$ is the Coxeter number), the representation theory is "close" to characteristic 0, and in particular, $\dim M^G = \langle \text{ch}(M), 1 \rangle$ for Weyl modules $M$.

Actually, I think the precise statement is:

**For $p > h$ (Coxeter number), the Weyl module $\Delta(\lambda) \otimes \mathbb{F}_p$ is irreducible for all dominant weights $\lambda$ with $\lambda$ in the "fundamental alcove" (i.e., $\langle \lambda + \rho, \alpha^\vee \rangle < p$ for all positive coroots $\alpha^\vee$).**

For weights outside the fundamental alcove, the Steinberg tensor product theorem applies, and the structure is more complicated.

But for our purposes, we need the multiplicity of the trivial representation in $\text{Sym}^d(V) \otimes \mathbb{F}_p$ for ALL $d$. As $d$ grows, the weights of $\text{Sym}^d(V)$ grow, and eventually they leave the fundamental alcove. So for large $d$, the representation theory in characteristic $p$ differs from characteristic 0, and the multiplicity of the trivial representation might differ.

This means the Hilbert series of $(R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ might differ from that of $R^G \otimes \mathbb{Q}$ for any fixed $p$, no matter how large.

Wait, but this would mean the map is NOT surjective for any fixed $p$! That can't be right...

Actually, let me reconsider. The Hilbert series being different doesn't necessarily mean the map isn't surjective. The map $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$ is injective (for $R$ torsion-free), and if the Hilbert series of the target is larger than that of the source, then the map is not surjective. But if the Hilbert series are the same, the map is an isomorphism.

So the question is: for large $p$, are the Hilbert series the same?

Let me think about a specific example. Take $G = \text{SL}_2$ and $V = \text{Sym}^2(\mathbb{Z}^2)$ (the 3-dimensional representation). The Coxeter number of $\text{SL}_2$ is 2.

The invariant ring $\mathbb{Z}[x_1, x_2, x_3]^{\text{SL}_2}$ where $\text{SL}_2$ acts on the 3-dimensional representation (which is the adjoint representation). The invariants of the adjoint representation of $\text{SL}_2$ on $\mathfrak{sl}_2$ are generated by the Killing form / trace form, which is a degree 2 invariant. So $R^G = \mathbb{Z}[q]$ where $q$ is a degree 2 element.

Over $\mathbb{F}_p$, the invariants should also be $\mathbb{F}_p[q]$ for all $p$ (since the adjoint representation is well-behaved). So the Hilbert series are the same.

Let me try a more complex example. Take $G = \text{SL}_2$ acting on $V = \text{Sym}^3(\mathbb{Z}^2)$ (the 4-dimensional irreducible representation). The invariant ring $k[x_1, x_2, x_3, x_4]^{\text{SL}_2}$ where $\text{SL}_2$ acts via the 4-dimensional representation.

In characteristic 0, the invariants of $\text{SL}_2$ acting on $\text{Sym}^3$ are known. There's a degree 2 invariant (the discriminant or some bilinear form) and possibly higher degree invariants.

Actually, for $\text{SL}_2$ acting on binary cubics (i.e., $\text{Sym}^3$), the invariant ring is $\mathbb{C}[f_4, f_6]$ where $f_4$ and $f_6$ are invariants of degrees 4 and 6. Wait, let me recall. For binary cubics, the ring of invariants is $\mathbb{C}[\Delta]$ where $\Delta$ is the discriminant of degree 4. Actually, I think there are two invariants: the discriminant of degree 4. Let me look this up in my memory.

For binary forms of degree $n$ (i.e., $\text{Sym}^n$ of the standard representation of $\text{SL}_2$), the invariant ring is:
- $n = 1$: $\mathbb{C}$ (no invariants)
- $n = 2$: $\mathbb{C}[q]$ (degree 2, the determinant)
- $n = 3$: $\mathbb{C}[\Delta]$ (degree 4, the discriminant)
- $n = 4$: $\mathbb{C}[f_2, f_3]$ (degrees 2 and 3)
- etc.

For $n = 3$ (binary cubics), the invariant ring is $\mathbb{C}[\Delta]$ where $\Delta$ has degree 4. So $R^G = \mathbb{Z}[\Delta]$ (assuming $\Delta$ is defined over $\mathbb{Z}$, which it is).

Over $\mathbb{F}_p$, is $(R \otimes \mathbb{F}_p)^{\text{SL}_2} = \mathbb{F}_p[\Delta]$?

For $p = 2$, the representation $\text{Sym}^3 \otimes \mathbb{F}_2$ is not irreducible (it has a composition series with the trivial representation appearing). So there might be additional invariants in characteristic 2.

For $p = 3$, similar issues.

For $p \geq 5$ (or $p > 3 = n$), the representation $\text{Sym}^3 \otimes \mathbb{F}_p$ is irreducible (since $p > n$), and the representation theory is the same as in characteristic 0. So the invariant ring should be $\mathbb{F}_p[\Delta]$.

But what about higher degree invariants? The invariant $\Delta$ has degree 4, and the invariant ring is generated by $\Delta$. For $p > 3$, are there any additional invariants in higher degrees?

If the representation $\text{Sym}^d(\text{Sym}^3) \otimes \mathbb{F}_p$ has the same composition factors as $\text{Sym}^d(\text{Sym}^3) \otimes \mathbb{C}$ for all $d$, then the multiplicity of the trivial representation is the same, and the Hilbert series are the same.

For $p > 3$, is $\text{Sym}^d(\text{Sym}^3) \otimes \mathbb{F}_p$ "the same" as in characteristic 0 for all $d$?

The weights of $\text{Sym}^d(\text{Sym}^3)$ grow with $d$, so for any fixed $p$, eventually the weights exceed $p$ and the representation theory differs. So for any fixed $p$, there might be $d$ large enough that $\text{Sym}^d(\text{Sym}^3) \otimes \mathbb{F}_p$ has different composition factors than in characteristic 0.

But does this affect the multiplicity of the trivial representation? It might or might not.

Hmm, this is getting quite involved. Let me try to think about whether the answer to the original question is YES or NO.

I think the answer is **YES**, the map is surjective for sufficiently large $p$. This is a known result in arithmetic invariant theory.

The key reference is likely the work of Seshadri, or more modern treatments by Alper, or the work on reductive group schemes by Demazure-Gabriel.

Let me try to construct a proof.

**Proof strategy:**

1. Since $G$ is split simply-connected semisimple over $\mathbb{Z}$, $G$ is a reductive group scheme over $\mathbb{Z}$.
2. By Seshadri's theorem, $R^G$ is finitely generated over $\mathbb{Z}$.
3. The key tool: for reductive group schemes, the functor of invariants commutes with base change for "large" primes.

For step 3, the argument is:

- Over $\mathbb{Q}$, $G_\mathbb{Q}$ is linearly reductive, so there's a Reynolds operator $\rho: R_\mathbb{Q} \to R_\mathbb{Q}^G$.
- This Reynolds operator spreads out to $\mathbb{Z}[1/N]$ for some $N$.
- For $p \nmid N$, the reduced Reynolds operator $\bar{\rho}: R_p \to R^G \otimes \mathbb{F}_p$ is a $G_{\mathbb{F}_p}$-equivariant retraction.
- The key property: $\bar{\rho}(g \cdot r) = \bar{\rho}(r)$ for all $g \in G(\mathbb{F}_p)$, $r \in R_p$.
- This means $\bar{\rho}$ factors through the coinvariants: $\bar{\rho}: R_p \to R_p / (g \cdot r - r) \to R^G \otimes \mathbb{F}_p$.
- Wait, that's not quite right. $\bar{\rho}$ kills the augmentation ideal (the ideal generated by $g \cdot r - r$), so $\bar{\rho}$ factors through the coinvariants $R_{p, G(\mathbb{F}_p)}$.
- But $\bar{\rho}$ also maps into the invariants $R^G \otimes \mathbb{F}_p \subseteq R_p^{G(\mathbb{F}_p)}$.
- So we have: $R_p^{G(\mathbb{F}_p)} \xrightarrow{\bar{\rho}} R^G \otimes \mathbb{F}_p \hookrightarrow R_p^{G(\mathbb{F}_p)}$.
- The composition $R^G \otimes \mathbb{F}_p \hookrightarrow R_p^{G(\mathbb{F}_p)} \xrightarrow{\bar{\rho}} R^G \otimes \mathbb{F}_p$ is the identity (since $\bar{\rho}|_{R^G \otimes \mathbb{F}_p} = \text{id}$).
- But the composition $R_p^{G(\mathbb{F}_p)} \xrightarrow{\bar{\rho}} R^G \otimes \mathbb{F}_p \hookrightarrow R_p^{G(\mathbb{F}_p)}$ is $\bar{\rho}$ restricted to $R_p^{G(\mathbb{F}_p)}$, which might not be the identity.

So we have a retraction $\bar{\rho}: R_p^{G(\mathbb{F}_p)} \to R^G \otimes \mathbb{F}_p$ with a section (the inclusion). This means $R_p^{G(\mathbb{F}_p)} = (R^G \otimes \mathbb{F}_p) \oplus \ker(\bar{\rho}|_{R_p^{G(\mathbb{F}_p)}})$.

For surjectivity, we need $\ker(\bar{\rho}|_{R_p^{G(\mathbb{F}_p)}}) = 0$.

As I discussed before, this is equivalent to $\ker(\bar{\rho}) \cap R_p^{G(\mathbb{F}_p)} = 0$, which is equivalent to the non-existence of $G(\mathbb{F}_p)$-invariants in $\ker(\bar{\rho})$.

Over $\mathbb{Q}$, $\ker(\rho_\mathbb{Q})$ has no $G$-invariants. The question is whether this persists mod $p$ for large $p$.

Now, here's the key insight that I was missing: **we don't need to check this for all degrees simultaneously. We use the finite generation of $R^G$ to reduce to a finite check.**

Here's the argument:

- $R^G = \mathbb{Z}[f_1, \ldots, f_m]$ with $f_i$ homogeneous of degrees $d_i$.
- Let $D = \max_i d_i$.
- The Reynolds operator $\rho$ is defined over $\mathbb{Z}[1/N]$.
- For $p \nmid N$, consider the map $\bar{\rho}_d: R_d \otimes \mathbb{F}_p \to R^G_d \otimes \mathbb{F}_p$ for each degree $d$.
- For $d \leq D$, $\ker(\bar{\rho}_d) \cap (R_d \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)} = 0$ for $p > p_0$ (since these are finite-dimensional representations and for large $p$ the representation theory is the same as char 0).
- For $d > D$, any invariant in $R_d \otimes \mathbb{F}_p$ can be written as a polynomial in the generators of $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$. But we don't know the generators of $(R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)}$...

Hmm, this is circular again. Let me try yet another approach.

**Approach via the Cohen-Macaulay property and flatness:**

Actually, I think the cleanest approach is via the theory of reductive group schemes and their invariants, as developed by Alper, Fogarty, etc.

The key result is:

**Theorem (Alper, or Seshadri, or ...):** Let $G$ be a reductive group scheme over a Noetherian ring $A$, acting on a finitely generated $A$-algebra $R$. Then:
(a) $R^G$ is finitely generated over $A$.
(b) If $A$ is a Dedekind domain (or more generally, if $G$ is "tame" over $A$), then the formation of invariants commutes with base change for all but finitely many primes.

Actually, I recall now that the precise result is due to Seshadri and is stated as follows:

**Theorem (Seshadri, 1977):** Let $G$ be a reductive group over a Noetherian ring $A$, acting on a finitely generated $A$-algebra $R$. If $G$ is "geometrically reductive" over $A$, then $R^G$ is finitely generated over $A$. Moreover, if $A = \mathbb{Z}$ and $G$ is split reductive, then for all but finitely many primes $p$, $R^G \otimes \mathbb{F}_p \cong (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$.

The proof of the base change statement uses the Reynolds operator and the fact that for large $p$, the representation theory is "close enough" to characteristic 0.

Let me try to write a complete proof.

**Proof:**

We prove that the map is an isomorphism (hence surjective) for sufficiently large $p$.

**Step 1: Setup and finite generation.**

$G$ is a split simply-connected semisimple group over $\mathbb{Z}$, hence a reductive group scheme over $\mathbb{Z}$. $R$ is a finitely generated $\mathbb{Z}$-algebra with a linear $G$-action. By Seshadri's theorem (geometric reductivity of reductive groups over $\mathbb{Z}$, proved using Haboush's theorem), $R^G$ is finitely generated over $\mathbb{Z}$.

Since $G$ is split and simply-connected, $G(\mathbb{Z})$ is Zariski dense in $G$ (by the Borel density theorem or elementary arguments for split groups). Similarly, for any prime $p$, $G(\mathbb{F}_p)$ is Zariski dense in $G_{\mathbb{F}_p}$ (since $G_{\mathbb{F}_p}$ is connected reductive). Therefore:
$$R^{G(\mathbb{Z})} = R^G, \quad (R \otimes \mathbb{F}_p)^{G(\mathbb{F}_p)} = (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}.$$

So the map in question is $R^G \otimes \mathbb{F}_p \to (R \otimes \mathbb{F}_p)^{G_{\mathbb{F}_p}}$.

**Step 2: Reduction to the polynomial case.**

Since the action is linear, $R$ is a quotient of
