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
  <problem_id>deepmath_103k_00003128</problem_id>
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

Evaluate the limit: \[ \lim_{n \to \infty} n \int_2^e (\ln x)^n \, dx. \]

## Standard Solution

Okay, so I need to evaluate the limit as n approaches infinity of n times the integral from 2 to e of (ln x)^n dx. Hmm, that looks a bit intimidating at first glance, but let's break it down step by step.

First, let me understand the components here. The integral is of (ln x)^n from 2 to e, and then we're multiplying that by n and taking the limit as n goes to infinity. So, as n becomes very large, the behavior of the integrand (ln x)^n will be crucial. Since we're dealing with an integral raised to the power of n, I suspect that the majority of the contribution to the integral will come from regions where ln x is as large as possible. Because when you raise a number greater than 1 to a large power, it grows exponentially, and if it's less than 1, it decays exponentially. So, near the upper limit of integration, which is e, since ln e = 1, and near the lower limit, ln 2 is approximately 0.693, which is less than 1. Therefore, (ln x)^n will be maximized at x = e, where it's 1, and will be much smaller elsewhere, especially near x = 2.

But wait, at x = e, ln x is exactly 1, and to the left of that, like near x slightly less than e, ln x is slightly less than 1, so (ln x)^n will decay exponentially as n increases. But since we're multiplying the integral by n, maybe there's a balance here where the integral itself is decaying, but n is growing, so the product might approach a finite limit.

This reminds me of some limit problems where you have an integral that concentrates around a point as n increases, and you approximate it using Laplace's method or the method of dominated contributions. Laplace's method is used to approximate integrals of the form ∫ e^{n f(x)} dx, where the main contribution comes from the vicinity of the maximum of f(x). But here, instead of an exponential, we have (ln x)^n. Maybe we can write it as e^{n ln(ln x)}? Let's check.

Yes, indeed: (ln x)^n = e^{n ln(ln x)}. So, if we set f(x) = ln(ln x), then the integral becomes ∫ from 2 to e of e^{n f(x)} dx. The function f(x) = ln(ln x). Let's see where this f(x) is maximized. The maximum of f(x) occurs where its derivative is zero.

f'(x) = derivative of ln(ln x) with respect to x is 1/(ln x) * 1/x. So f'(x) = 1/(x ln x). Wait, so setting f'(x) = 0 would require 1/(x ln x) = 0, which never happens. That means that f(x) doesn't have critical points in the interval (2, e). Therefore, the maximum of f(x) on [2, e] must occur at one of the endpoints.

Let me check the values at the endpoints. At x = e, ln x = 1, so f(e) = ln(1) = 0. At x = 2, ln 2 ≈ 0.693, so f(2) = ln(ln 2) ≈ ln(0.693) ≈ -0.366. So, actually, f(x) is maximized at x = e, where it's 0, and minimized at x = 2. Therefore, the maximum of f(x) is at x = e. So according to Laplace's method, the integral ∫ from 2 to e of e^{n f(x)} dx ≈ e^{n f(e)} * something. But f(e) = 0, so e^{n f(e)} = 1. But since the maximum is at the endpoint, Laplace's method would need to consider the contribution near x = e.

Wait, but in Laplace's method, when the maximum is at an endpoint, the integral is approximated by considering the contribution near that endpoint. The standard result is that if the maximum is at the upper limit, say x = b, and f(x) has a derivative at x = b which is negative (since it's decreasing as we move left from b), then the integral is approximately e^{n f(b)} * (something involving 1/n). But since f(b) = 0 here, and the integral is multiplied by n, maybe this will give a finite limit.

Alternatively, maybe substitution would work here. Let me try a substitution to make the integral more manageable.

Let’s set t = ln x. Then when x = 2, t = ln 2, and when x = e, t = 1. Also, dx = e^t dt. So the integral becomes ∫_{ln 2}^1 t^n e^t dt. Then the original expression is n * ∫_{ln 2}^1 t^n e^t dt. So, we have n times the integral from ln 2 to 1 of t^n e^t dt.

So, the problem reduces to evaluating the limit as n approaches infinity of n times ∫_{ln 2}^1 t^n e^t dt. Since ln 2 is approximately 0.693, which is less than 1. So we have an integral from a number less than 1 to 1 of t^n e^t dt. As n becomes large, t^n will be sharply peaked near t = 1, because for t < 1, t^n tends to zero exponentially. Therefore, the integral is dominated by the contribution near t = 1. So, we can approximate the integral by expanding the integrand around t = 1.

Let me make a substitution to zoom in near t = 1. Let’s set t = 1 - s/n, where s is a new variable. As n tends to infinity, s will be of order 1, and t approaches 1 from below. Then, dt = -ds/n. Changing variables:

When t = 1, s = 0; when t = ln 2, s = n(1 - ln 2). But as n approaches infinity, s becomes very large here, but since t^n e^t is exponentially small for t away from 1, the contribution from the lower limit will be negligible. Therefore, we can extend the lower limit to infinity, introducing an exponentially small error. So the integral becomes approximately ∫_{0}^{\infty} (1 - s/n)^n e^{1 - s/n} * (ds/n). Let's write this out:

∫_{0}^{\infty} (1 - s/n)^n e^{1 - s/n} * (ds/n).

First, note that (1 - s/n)^n ≈ e^{-s} as n tends to infinity (since lim_{n→∞} (1 - s/n)^n = e^{-s}). Also, e^{1 - s/n} ≈ e^1 * e^{-s/n} ≈ e * (1 - s/n). Therefore, the integrand approximates to e * e^{-s} * (1 - s/n) * (1 - s/n) ≈ e * e^{-s} * (1 - 2s/n). But since we're taking the limit as n goes to infinity, the terms with 1/n will vanish. Therefore, the integrand is approximately e * e^{-s} and the integral becomes e/n ∫_{0}^{\infty} e^{-s} ds. The integral of e^{-s} from 0 to ∞ is 1, so the integral approximates to e/n * 1 = e/n. Therefore, the original expression n * ∫_{ln 2}^1 t^n e^t dt ≈ n * (e/n) = e. But wait, that would suggest the limit is e. However, this seems maybe too straightforward. Let me check my substitution again.

Wait, actually, when changing variables to s = n(1 - t), so t = 1 - s/n, then dt = -ds/n, and the integral becomes:

∫_{ln 2}^1 t^n e^t dt = ∫_{0}^{n(1 - ln 2)} (1 - s/n)^n e^{1 - s/n} (ds/n).

But as n approaches infinity, n(1 - ln 2) approaches infinity since 1 - ln 2 ≈ 0.306, so multiplied by n gives a large upper limit. But since the integrand decays exponentially as s increases, the integral over [0, ∞) is a good approximation. So, as n → ∞, we can replace the upper limit with ∞ and approximate (1 - s/n)^n as e^{-s}, and e^{1 - s/n} as e * e^{-s/n} ≈ e*(1 - s/n). Therefore, the integrand is approximately e * e^{-s} * (1 - s/n) / n. Wait, no, hold on: the substitution gives:

(1 - s/n)^n ≈ e^{-s}

e^{1 - s/n} ≈ e * e^{-s/n} ≈ e * (1 - s/n + (s/n)^2/2 - ... )

But expanding e^{-s/n} as a Taylor series, it's 1 - s/n + (s^2)/(2n^2) - ..., so multiplied by e gives e*(1 - s/n + ...).

Therefore, the integrand becomes approximately e * e^{-s} * (1 - s/n) * (ds/n). But when we multiply this out, we get e * e^{-s} (1 - s/n) ds /n. However, when we multiply by n (from the original limit expression), it becomes e * ∫_{0}^{\infty} e^{-s} (1 - s/n) ds. But as n approaches infinity, the term s/n becomes negligible, so we get e * ∫_{0}^{\infty} e^{-s} ds = e*1 = e. Therefore, the limit is e.

Wait, but this seems conflicting with my initial steps. Let me check again:

Original expression: limit as n→∞ of n * ∫_{ln2}^1 t^n e^t dt.

We substitute t = 1 - s/n, so dt = -ds/n. Then the integral becomes:

∫_{s=0}^{s=n(1 - ln2)} (1 - s/n)^n e^{1 - s/n} * (ds/n)

= (e/n) ∫_{0}^{n(1 - ln2)} (1 - s/n)^n e^{-s/n} ds.

Now, as n→∞, (1 - s/n)^n ≈ e^{-s}, and e^{-s/n} ≈ 1 - s/n. So:

≈ (e/n) ∫_{0}^{\infty} e^{-s} (1 - s/n) ds.

But when we multiply by n:

n * (e/n) ∫_{0}^{\infty} e^{-s} (1 - s/n) ds = e ∫_{0}^{\infty} e^{-s} (1 - s/n) ds.

But as n→∞, the term with s/n goes to zero, so the integral becomes e ∫_{0}^{\infty} e^{-s} ds = e*1 = e.

Therefore, the limit is e. But I need to verify this because sometimes when you do these substitutions, constants can be tricky.

Alternatively, let's consider integrating by parts. Let me try integrating ∫ t^n e^t dt. Let’s set u = t^n, dv = e^t dt. Then du = n t^{n-1} dt, v = e^t. So integration by parts gives:

uv |_{ln2}^1 - ∫_{ln2}^1 v du

= [t^n e^t]_{ln2}^1 - n ∫_{ln2}^1 t^{n-1} e^t dt.

Evaluating the boundary terms:

At t=1: 1^n e^1 = e.

At t=ln2: (ln2)^n e^{ln2} = (ln2)^n * 2.

So the boundary term is e - 2(ln2)^n.

Therefore, the integral becomes:

e - 2(ln2)^n - n ∫_{ln2}^1 t^{n-1} e^t dt.

Wait, but the original integral is ∫ t^n e^t dt. Let me denote I_n = ∫_{ln2}^1 t^n e^t dt. Then the integration by parts gives:

I_n = e - 2(ln2)^n - n I_{n-1}.

But we can write this as:

I_n = e - 2(ln2)^n - n I_{n-1}

Hmm, this recursion might be useful. Let's see.

But we are interested in n I_n. Let's denote J_n = n I_n. Then, from the above equation:

I_n = e - 2(ln2)^n - J_{n-1}

Therefore, multiplying both sides by n:

n I_n = n e - 2 n (ln2)^n - n J_{n-1}

But J_n = n I_n, so:

J_n = n e - 2 n (ln2)^n - n J_{n-1}

Hmm, this seems a bit complicated. Let me check if this is leading anywhere.

But perhaps we can find a relation between J_n and J_{n-1}. Wait, but J_{n} = n I_n, and J_{n-1} = (n-1) I_{n-1}. So:

From the equation above:

J_n = n e - 2 n (ln2)^n - n J_{n-1}/(n - 1)

This seems more complex. Maybe not the best approach.

Alternatively, let's consider that for large n, the integral I_n is dominated near t=1. So, let's expand e^t around t=1. Let’s set t = 1 - s, where s is small. Then, e^t = e^{1 - s} = e e^{-s} ≈ e (1 - s + s^2/2 - ...). Then, t^n = (1 - s)^n ≈ e^{-n s} (using the approximation (1 - s)^n ≈ e^{-n s} for small s). So, the integral becomes approximately:

∫_{s=0}^{s=1 - ln2} e^{-n s} e (1 - s + ...) ds.

Since ln2 ≈ 0.693, 1 - ln2 ≈ 0.307. So the upper limit is 0.307, but for large n, the integral is dominated by s near 0. Therefore, we can extend the upper limit to infinity with negligible error. Thus:

I_n ≈ e ∫_{0}^{\infty} e^{-n s} (1 - s) ds = e [ ∫_{0}^{\infty} e^{-n s} ds - ∫_{0}^{\infty} s e^{-n s} ds ]

Compute these integrals:

First integral: ∫_{0}^{\infty} e^{-n s} ds = 1/n.

Second integral: ∫_{0}^{\infty} s e^{-n s} ds = 1/n^2.

Therefore, I_n ≈ e [1/n - 1/n^2] = e/n (1 - 1/n).

Thus, multiplying by n:

n I_n ≈ e (1 - 1/n) → e as n → ∞.

Therefore, the limit is e.

But wait, this is the same result as before. So, according to both substitution methods and the integration by parts approach (with the approximation), the limit is e.

But let me verify with a concrete example. Let’s take n=1000. Then, the integral from ln2 to 1 of t^1000 e^t dt is approximately e/(1000) (1 - 1/1000) ≈ e/1000 * 0.999 ≈ e/1000. Then, multiplying by n=1000 gives approximately e. So this seems to hold.

Alternatively, if I consider the substitution u = n(1 - t), which is similar to the previous substitution. Let’s set u = n(1 - t), so t = 1 - u/n, dt = -du/n. Then, when t=1, u=0; when t=ln2, u = n(1 - ln2). Therefore, the integral becomes:

∫_{ln2}^1 t^n e^t dt = ∫_{0}^{n(1 - ln2)} (1 - u/n)^n e^{1 - u/n} (du/n).

Again, as n approaches infinity, (1 - u/n)^n ≈ e^{-u}, e^{1 - u/n} ≈ e, so the integral ≈ ∫_{0}^{\infty} e^{-u} e (du/n) = e/n. Then, multiplying by n gives e. So that's consistent.

Therefore, after multiple approaches, the conclusion is that the limit is e.

But let me check if there's a possible mistake here. For example, in expanding e^{-s/n} as 1 - s/n, but in reality, e^{-s/n} = 1 - s/n + (s/n)^2/2! - ... So when we multiply by (1 - s/n)^n ≈ e^{-s}, we get e^{-s}*(1 - s/n + ...). But when we expand (1 - s/n)^n e^{-s/n} e, is that exactly e^{1 - s}?

Wait, if we take t = 1 - s/n, then:

t^n = (1 - s/n)^n ≈ e^{-s}

and e^{t} = e^{1 - s/n} = e * e^{-s/n}

Therefore, the product t^n e^t ≈ e * e^{-s} e^{-s/n} ≈ e * e^{-s} (1 - s/n)

But since e^{-s/n} ≈ 1 - s/n for large n.

So, the integrand is approximately e * e^{-s} (1 - s/n), and when we integrate over s from 0 to ∞, and multiply by n, we get:

n * (e /n) ∫_{0}^\infty e^{-s} (1 - s/n) ds ≈ e ∫_{0}^\infty e^{-s} ds - (e/n) ∫_{0}^\infty s e^{-s} ds

But the first integral is e*1 = e, and the second term is (e/n)*1 = e/n, which tends to zero as n→∞. Therefore, the limit is indeed e.

Therefore, after careful consideration and multiple methods, I'm confident that the limit is e.

**Final Answer**
\boxed{e}
</think>

To evaluate the limit \(\lim_{n \to \infty} n \int_2^e (\ln x)^n \, dx\), we start by transforming the integral using the substitution \(t = \ln x\). This changes the integral bounds from \(x = 2\) to \(x = e\) into \(t = \ln 2\) to \(t = 1\), and the integral becomes:

\[
\int_{\ln 2}^1 t^n e^t \, dt
\]

Thus, the original expression becomes:

\[
\lim_{n \to \infty} n \int_{\ln 2}^1 t^n e^t \, dt
\]

For large \(n\), the integrand \(t^n e^t\) is sharply peaked near \(t = 1\) because \(t^n\) decays exponentially for \(t < 1\). We approximate the integral near \(t = 1\) by substituting \(t = 1 - \frac{s}{n}\), which gives \(dt = -\frac{ds}{n}\). The integral then transforms to:

\[
\int_{0}^{\infty} \left(1 - \frac{s}{n}\right)^n e^{1 - \frac{s}{n}} \frac{ds}{n}
\]

Using the approximations \(\left(1 - \frac{s}{n}\right)^n \approx e^{-s}\) and \(e^{1 - \frac{s}{n}} \approx e \left(1 - \frac{s}{n}\right)\) for large \(n\), the integrand simplifies to:

\[
e \cdot e^{-s} \left(1 - \frac{s}{n}\right) \frac{ds}{n}
\]

The integral then becomes:

\[
\frac{e}{n} \int_{0}^{\infty} e^{-s} \left(1 - \frac{s}{n}\right) ds
\]

As \(n \to \infty\), the term \(\frac{s}{n}\) becomes negligible, and the integral simplifies to:

\[
\frac{e}{n} \int_{0}^{\infty} e^{-s} \, ds = \frac{e}{n} \cdot 1 = \frac{e}{n}
\]

Multiplying by \(n\) gives:

\[
n \cdot \frac{e}{n} = e
\]

Thus, the limit is:

\[
\boxed{e}
\]

## AI's Thinking (Attempted Solution Process)

The problem is a math problem from AGENTS.md. Let me read it carefully.

The problem: Let X be a normal, projective complex variety with at worst rational singularities, and let π: Y → X be the resolution of singularities obtained by blowing up the singular points. Determine if R^1 π_* Z = 0 when X is of dimension 3.

Let me check for answer leaks. The problem statement doesn't contain any solution or answer hints. It's a clean problem statement.

Now let me think about this problem.

We have X a normal projective complex variety with rational singularities, dim 3. π: Y → X is the resolution obtained by blowing up the singular points. We need to determine if R^1 π_* Z = 0.

Key facts:
- Rational singularities: A singularity is rational if for a resolution f: Y' → X, R^i f_* O_{Y'} = 0 for i > 0.
- The question is about R^1 π_* Z (constant sheaf Z), not coherent sheaves.

For rational singularities, we know that R^i π_* O_Y = 0 for i > 0. But the question is about the constant sheaf Z.

Let me think about the relationship between R^i π_* Z and the topology of the singularities.

The sheaf R^i π_* Z is related to the cohomology of the fibers. For a point x ∈ X, the stalk (R^i π_* Z)_x is related to H^i(π^{-1}(x), Z) (the cohomology of the fiber over x, in the appropriate sense - actually the limit over neighborhoods).

For a resolution obtained by blowing up singular points, the exceptional fiber over a singular point x is some variety E_x.

The question is whether R^1 π_* Z = 0, i.e., whether H^1 of the fibers vanish.

For rational singularities in dimension 3, what do we know about the exceptional fibers?

A rational singularity has the property that the geometric genus p_g = 0, and more generally R^i f_* O = 0 for i > 0.

For surface rational singularities (dim 2), the exceptional divisor is a tree of P^1's, and the intersection matrix is negative definite. The exceptional fiber is simply connected (a tree of P^1's is simply connected), so H^1(E, Z) = 0. So for surfaces, R^1 π_* Z = 0.

But in dimension 3, the situation is different. Rational singularities in dimension 3 can have exceptional fibers that are not simply connected.

Actually, let me think more carefully. The question is specifically about the resolution obtained by "blowing up the singular points." This is a specific resolution.

Hmm, but actually the question is asking whether R^1 π_* Z = 0 always, or whether it can be nonzero.

Let me think about examples. Consider a 3-dimensional rational singularity where the exceptional fiber has nontrivial H^1.

For instance, consider a cone over a rational surface. If X is the cone over a surface S, then the resolution is the total space of O_S(-1) (or rather, blowing up the vertex gives the total space of the line bundle O_S(-D) for some ample D).

Actually, let me think about the cone over a rational surface. Let S be a smooth rational surface (e.g., P^2), and let L be an ample line bundle on S. The cone over (S, L) is the affine cone, which has an isolated singularity at the vertex. The resolution is obtained by blowing up the vertex, giving the total space of L^{-1} (or the line bundle O_S(-D) where L = O_S(D)).

The exceptional fiber is S itself. So H^1(E, Z) = H^1(S, Z).

If S = P^2, then H^1(P^2, Z) = 0, so R^1 π_* Z = 0 at that point.

But if S is a rational surface with H^1(S, Z) ≠ 0... wait, can a rational surface have H^1 ≠ 0? A rational surface has q = p_g = 0, so H^1(S, O_S) = 0. But H^1(S, Z) could still be nonzero due to torsion! Actually, for a smooth rational surface, H^1(S, Z) = 0 because b_1 = 2q = 0 and there's no torsion in H^1 for simply connected... wait, rational surfaces are not necessarily simply connected. Actually, rational surfaces are birational to P^2, and P^2 is simply connected. Birational smooth projective surfaces have the same fundamental group (for surfaces, π_1 is a birational invariant). So rational surfaces are simply connected, hence H^1(S, Z) = 0.

Hmm, so for cones over rational surfaces, H^1 of the exceptional fiber is 0.

Let me think of other examples. What about a 3-fold singularity whose exceptional fiber is a curve or has components with H^1 ≠ 0?

Actually, let me reconsider. The question says "blowing up the singular points." If X has isolated singularities, blowing up the singular points gives a resolution (assuming rational singularities are isolated? No, rational singularities need not be isolated in general, but the problem says "blowing up the singular points" which suggests isolated singularities).

Wait, actually, for the blow-up of a singular point to give a resolution, we typically need the singularities to be isolated. If X has isolated singularities, blowing up each singular point might give a resolution (or might need further blow-ups).

The problem states that π: Y → X is "the resolution of singularities obtained by blowing up the singular points." So we're told that this blow-up gives a resolution.

Now, for a 3-dimensional isolated rational singularity, the exceptional fiber E of the resolution is a surface (or a union of surfaces). The question is whether H^1(E, Z) = 0.

Actually, I recall that for rational singularities, there's a result relating R^i π_* Z to the local fundamental group of the singularity.

Specifically, there's the following: For an isolated singularity x ∈ X of dimension n, with resolution π: Y → X and exceptional fiber E = π^{-1}(x), we have:
- R^0 π_* Z = Z (since π_* Z = Z for a resolution with connected fibers)
- R^i π_* Z is supported at the singular points for i > 0 (since π is an isomorphism away from singular points)
- The stalk (R^i π_* Z)_x is related to H^i(E, Z) (more precisely, it's H^i(E, Z) by proper base change, since for isolated singularities the fiber over x is E).

Wait, actually by proper base change, for a point x, (R^i π_* Z)_x ⊗ Z_x ≅ H^i(π^{-1}(x), Z) = H^i(E, Z). But the stalk is not exactly H^i(E, Z); it's the inverse limit over neighborhoods. However, for isolated singularities, by the Vietoris-Begle theorem or similar, the stalk of R^i π_* Z at x is H^i(E, Z) (this is a consequence of the fact that the neighborhood deformation retracts appropriately, or more precisely by the local cohomology / proper base change).

Actually, let me be more careful. The proper base change theorem says that for a geometric point x̄ over x, (R^i π_* Z)_x̄ = H^i(Y ×_X x̄, Z). For a closed point x with isolated singularity, the fiber Y ×_X x = E, and the geometric fiber is also E (over C). So (R^i π_* Z)_x = H^i(E, Z).

So R^1 π_* Z = 0 if and only if H^1(E, Z) = 0 for every exceptional fiber E.

Now, the question is: for a 3-dimensional rational singularity, is H^1(E, Z) = 0?

I believe the answer is NO in general. There exist 3-dimensional rational singularities where the exceptional fiber has nontrivial H^1.

Let me think of a concrete example. Consider a small resolution vs. a full resolution... Actually, let me think about this differently.

Consider the cone over a rational curve in P^3. Wait, that would give a surface singularity, not a 3-fold.

Let me think about 3-dimensional rational singularities more carefully.

One important class: quotient singularities. A quotient singularity C^3/G for a finite subgroup G ⊂ GL(3, C) is a rational singularity (this is a theorem of Viehweg, I believe, or it follows from the Boutot theorem: rational singularities are preserved under taking invariants by reductive groups).

For a quotient singularity C^3/G, the resolution is more complicated. But the link of the singularity is S^5/G, and the exceptional fiber of the minimal resolution...

Actually, let me think about this more carefully using the topology.

For an isolated singularity, the local fundamental group π_1^{loc}(x, X) is the fundamental group of the link L. There's a long exact sequence relating the cohomology of E, the link L, and the singularity.

The key relationship: For a resolution π: Y → X of an isolated singularity with exceptional fiber E, and link L (the boundary of a small neighborhood), we have:
- Y is a manifold with boundary L (locally)
- E is a deformation retract of a neighborhood in Y

The long exact sequence of the pair (Y, L) and the fact that E is a retract gives:
... → H^i(Y, L) → H^i(Y) → H^i(L) → H^{i+1}(Y, L) → ...

And by excision, H^i(Y, L) ≅ H^i_c(Y \ L) = H^i_c(Y \ E) (since Y \ L ≅ Y \ E locally... hmm, this isn't quite right).

Let me use a different approach. Consider a small contractible neighborhood U of x in X. Then π^{-1}(U) = V is a neighborhood of E in Y, and V deformation retracts to E. The boundary of V is the link L.

We have the long exact sequence of the pair (V, L):
... → H^i(V, L) → H^i(V) → H^i(L) → H^{i+1}(V, L) → ...

Since V deformation retracts to E, H^i(V) = H^i(E). By excision, H^i(V, L) = H^i(U, U \ {x}) = H^{i+1}_{x}(U) (local cohomology). Since U is contractible (as X has rational singularities... wait, is U contractible?).

Hmm, U is a small neighborhood of x in X. X is normal, so U is contractible if the singularity is rational? Not necessarily. Actually, for a cone over a projective variety, the cone is contractible. But in general, a small analytic neighborhood of an isolated singularity need not be contractible.

Actually, for an isolated singularity, a small enough Stein neighborhood is contractible if and only if the link is a homology sphere (by the long exact sequence). This is not always the case.

Let me think about this differently. The question is whether R^1 π_* Z = 0 for 3-dimensional rational singularities.

I recall that there's a result by Steenbrink and others relating the vanishing of R^i π_* Z to the topology of rational singularities.

Key fact: For rational singularities, R^i π_* O_Y = 0 for i > 0. By the exponential sequence and Hodge theory, this gives information about R^i π_* Z.

From the exponential sequence 0 → Z → O_Y → O_Y^* → 0, we get:
... → R^i π_* Z → R^i π_* O_Y → R^i π_* O_Y^* → R^{i+1} π_* Z → ...

For i = 1: R^1 π_* Z → R^1 π_* O_Y → R^1 π_* O_Y^* → R^2 π_* Z → R^2 π_* O_Y

Since R^1 π_* O_Y = 0 (rational singularities) and R^2 π_* O_Y = 0 (rational singularities), we get:
0 → R^1 π_* O_Y^* → R^2 π_* Z → 0

So R^1 π_* O_Y^* ≅ R^2 π_* Z. This doesn't directly tell us about R^1 π_* Z.

For i = 0: 0 → π_* Z → π_* O_Y → π_* O_Y^* → R^1 π_* Z → R^1 π_* O_Y → ...

Since π_* Z = Z (connected fibers), π_* O_Y = O_X (normal + connected fibers, by Zariski's main theorem / Grauert), and R^1 π_* O_Y = 0:
0 → Z → O_X → π_* O_Y^* → R^1 π_* Z → 0

So we have an exact sequence: O_X / Z → π_* O_Y^* → R^1 π_* Z → 0.

Hmm, this is getting complicated. Let me think about whether R^1 π_* Z can be nonzero.

Actually, I think the key insight is this: R^1 π_* Z is related to the local fundamental group of the singularity. Specifically, for an isolated singularity, the stalk of R^1 π_* Z at x is H^1(E, Z), and there's a relationship between H^1(E, Z) and the fundamental group of the link.

From the long exact sequence of the pair (V, L) where V retracts to E:
... → H^1(V, L) → H^1(E) → H^1(L) → H^2(V, L) → H^2(E) → H^2(L) → ...

And H^i(V, L) = H^i_c(V \ L) by... no. H^i(V, L) relates to local cohomology.

Actually, let me use the Gysin sequence or the long exact sequence more carefully.

We have V is a manifold with boundary L, and E ⊂ V is a deformation retract. So H^i(V) = H^i(E) and H^i(V, L) = H^i(V, ∂V).

By Poincaré-Lefschetz duality (V is an oriented manifold of real dimension 6 = 2·3):
H^i(V, L) = H_{6-i}(V)

And H_{6-i}(V) = H_{6-i}(E) (since V retracts to E).

So H^i(V, L) = H_{6-i}(E).

The long exact sequence becomes:
... → H_{6-1}(E) → H^1(E) → H^1(L) → H_{6-2}(E) → H^2(E) → H^2(L) → H_{6-3}(E) → ...

i.e., ... → H_5(E) → H^1(E) → H^1(L) → H_4(E) → H^2(E) → H^2(L) → H_3(E) → ...

Now, E is a complex surface (or union of surfaces) in a 3-fold. So E has real dimension 4. Thus H_5(E) = 0 and H_4(E) = H_4(E) (could be nonzero if E has multiple components, as H_4(E) = ⊕ Z for each connected component... wait, H_4 of a complex surface is Z if connected, or Z^k if k components).

Actually, H_5(E) = 0 since E is a complex surface (real dim 4, so H_5 = 0).

So: 0 → H^1(E) → H^1(L) → H_4(E) → H^2(E) → H^2(L) → H_3(E) → H^3(E) → H^3(L) → H_2(E) → ...

Wait, let me redo this. The long exact sequence of (V, L):
... → H^i(V, L) → H^i(V) → H^i(L) → H^{i+1}(V, L) → ...

With H^i(V) = H^i(E) and H^i(V, L) = H_{6-i}(E):

For i = 0: H_6(E) → H^0(E) → H^0(L) → H_5(E)
For i = 1: H_5(E) → H^1(E) → H^1(L) → H_4(E)
For i = 2: H_4(E) → H^2(E) → H^2(L) → H_3(E)
For i = 3: H_3(E) → H^3(E) → H^3(L) → H_2(E)

Since E is a complex surface (real dim 4): H_6(E) = 0, H_5(E) = 0.

So:
- i=0: 0 → H^0(E) → H^0(L) → 0, so H^0(E) ≅ H^0(L) (both connected, this is fine)
- i=1: 0 → H^1(E) → H^1(L) → H_4(E) → ...
- i=2: H_4(E) → H^2(E) → H^2(L) → H_3(E) → ...
- i=3: H_3(E) → H^3(E) → H^3(L) → H_2(E) → ...

So H^1(E) injects into H^1(L). And H^1(L) is related to the abelianization of π_1(L), the local fundamental group.

Now, for rational singularities, what do we know about the local fundamental group?

Theorem (Kollár?): For rational singularities, the local fundamental group is finite. Actually, I think the result is:

For rational singularities in dimension ≥ 3, the local fundamental group is finite (this is a theorem, possibly due to Kollár or Takayama).

Actually, more precisely, I recall that for 3-dimensional rational singularities, the local fundamental group can be nontrivial (and even infinite in some cases?).

Hmm wait. Let me reconsider. There's a theorem by Kollár that for rational singularities of dimension ≥ 3, the local fundamental group is finite. But actually, I think the result might be more nuanced.

Actually, I think the relevant result is:

Theorem (Xu, or Takayama, or Kollár): For a 3-dimensional rational singularity, the local fundamental group π_1(L) is finite.

If π_1(L) is finite, then H^1(L, Z) = Hom(π_1(L), Z) = 0 (since π_1(L) is finite, there are no nontrivial homomorphisms to Z).

So H^1(L, Z) = 0, and since H^1(E, Z) injects into H^1(L, Z) = 0, we get H^1(E, Z) = 0.

Therefore R^1 π_* Z = 0.

Wait, but I need to be more careful. Is it true that for 3-dimensional rational singularities, the local fundamental group is finite?

Let me recall the precise results:

1. For surface rational singularities (dim 2), the link is a rational homology sphere (Brieskorn, Artin-Verdier). In particular, H^1(L, Z) = 0, so H^1(E, Z) = 0.

2. For 3-dimensional rational singularities, the situation is more complex. There's a result by Kollár (in "Shafarevich maps and plurigenera") that for rational singularities of dimension n ≥ 3, the local fundamental group is finite. But I'm not 100% sure about this.

Actually, let me reconsider. I think the result is:

- For rational singularities, the local fundamental group is finite in dimension ≥ 3 (Kollár).
- But actually, there might be a counterexample or the result might require additional hypotheses.

Hmm, let me think about this more carefully. Actually, I recall that there are examples of 3-dimensional rational singularities with infinite local fundamental group. Let me think...

No wait. Actually, the key theorem I'm thinking of is:

Theorem (Kollár, "Shafarevich Maps", 1995): If X has rational singularities and dim X ≥ 3, then π_1^{loc}(x, X) is finite for every singular point x.

But I also recall that this might not be exactly right. Let me think about whether there are counterexamples.

Actually, I think the correct statement involves the notion of "rational chain connectedness" or something similar. Let me reconsider.

Hmm, actually, I think the result might be:

For a 3-fold with rational singularities, the local fundamental group at each point is finite.

This is stated in Kollár's work. If this is true, then H^1(L, Z) = 0 for the link L, and by the injection H^1(E, Z) ↪ H^1(L, Z), we get H^1(E, Z) = 0, hence R^1 π_* Z = 0.

But wait, I should double-check whether this theorem is actually correct, because I'm not entirely sure.

Actually, let me reconsider the problem from a different angle. The problem asks to "determine if R^1 π_* Z = 0 when X is of dimension 3." This phrasing suggests that the answer is either "yes, it's always 0" or "no, it's not always 0."

Given the structure of the problem (rational singularities, dimension 3, blowing up singular points), and the fact that for surfaces (dimension 2) the answer is known to be yes (R^1 π_* Z = 0), the question is asking whether this extends to dimension 3.

I believe the answer is YES, R^1 π_* Z = 0, based on the following argument:

1. For rational singularities, R^i π_* O_Y = 0 for i > 0.
2. The exponential sequence gives information relating R^i π_* Z to R^i π_* O_Y.
3. For 3-dimensional rational singularities, the local fundamental group is finite (Kollár's theorem), which implies H^1 of the link is 0, which implies H^1 of the exceptional fiber is 0.

But actually, I want to be more careful about step 3. Let me think about whether Kollár's theorem is exactly as I stated.

Actually, I now recall more precisely. The relevant result is:

Theorem (Kollár): Let X be a variety with rational singularities of dimension n. If n ≥ 3, then for any point x ∈ X, the local fundamental group π_1^{loc}(x, X) is finite.

This is Theorem 7.8 in Kollár's "Shafarevich Maps and Plurigenera" or similar. The proof uses the fact that for rational singularities, the exceptional fiber is rationally chain connected (or something similar), which implies the fundamental group is finite.

Actually, I think the precise statement might be about the fundamental group of the exceptional fiber E rather than the link L. Let me reconsider.

If E is rationally chain connected (which follows from rational singularities in some sense), then π_1(E) is finite (by Kollár's theorem on rationally chain connected varieties). But we need H^1(E, Z) = 0, which follows from π_1(E) being finite.

Wait, but is E rationally chain connected? For a resolution of a rational singularity, the exceptional fiber might not be rationally chain connected in general.

Hmm, let me think about this differently. Let me consider the relationship more carefully.

Actually, I think the key result is more directly about the local fundamental group. Let me look at this from the perspective of the long exact sequence.

We have the exact sequence:
0 → H^1(E, Z) → H^1(L, Z) → H_4(E, Z) → H^2(E, Z) → ...

If we can show H^1(L, Z) = 0, then H^1(E, Z) = 0.

H^1(L, Z) = Hom(H_1(L, Z), Z) = Hom(π_1(L)^{ab}, Z).

If π_1(L) is finite, then H^1(L, Z) = 0.

So the question reduces to: is π_1(L) finite for 3-dimensional rational singularities?

I believe the answer is yes, based on Kollár's work. The argument goes roughly as follows:

For a rational singularity, the resolution π: Y → X has R^i π_* O_Y = 0 for i > 0. This implies that the exceptional fiber E has H^i(E, O_E) = 0 for i > 0 (by the theorem on formal functions, or more precisely, the completion of R^i π_* O_Y at x is H^i(E, O_E) ⊕ higher order terms, and the vanishing of R^i π_* O_Y implies the vanishing of H^i(E, O_E) ⊗ O_{X,x}/m^n for all n, which by the theorem on formal functions gives H^i(Ê, O_Ê) = 0 where Ê is the formal completion).

Wait, actually the theorem on formal functions says (R^i π_* O_Y)^∧_x = lim H^i(E_n, O_{E_n}) where E_n is the n-th infinitesimal neighborhood. For rational singularities, R^i π_* O_Y = 0, so H^i(E_n, O_{E_n}) = 0 for all n and i > 0. In particular, H^i(E, O_E) = 0 for i > 0 (taking n=1).

So for the exceptional fiber E (a complex surface in the 3-fold case), we have H^i(E, O_E) = 0 for i > 0. This means:
- H^1(E, O_E) = 0: the irregularity q(E) = 0
- H^2(E, O_E) = 0: the geometric genus p_g(E) = 0

Now, by Hodge theory, H^1(E, C) = H^1(E, O_E) ⊕ H^0(E, Ω^1_E) = 0 (since H^1(E, O_E) = 0 and by Hodge symmetry H^0(E, Ω^1_E) = H^1(E, O_E) = 0... wait, that's for smooth varieties).

Hmm, E might not be smooth. E is the exceptional fiber, which could be a divisor with normal crossings or more generally a reduced scheme.

Let me be more careful. The exceptional fiber E = π^{-1}(x)_{red} is a reduced divisor in the smooth 3-fold Y. If π is obtained by a single blow-up of an isolated singular point, then E is the exceptional divisor of the blow-up, which is a projective surface (possibly singular, but let's assume it's the reduced exceptional divisor).

Actually, for the blow-up of a point in a 3-fold, the exceptional divisor is P^2 if the point is smooth. For a singular point, the exceptional divisor could be different.

Hmm, but the problem says π is the resolution obtained by blowing up the singular points. So if X has isolated singularities and blowing them up resolves the singularities, then E is the exceptional divisor of the blow-up.

For the blow-up of an isolated singular point in a 3-fold, the exceptional divisor E is a surface in P^2-bundle... no, it's the projectivized tangent cone. E = P(T_x X) where T_x X is the tangent cone at x.

Now, H^1(E, O_E) = 0 (from rational singularities). But does this imply H^1(E, Z) = 0?

If E is smooth, then by Hodge decomposition, H^1(E, C) = H^{1,0}(E) ⊕ H^{0,1}(E) = H^0(E, Ω^1) ⊕ H^1(E, O_E) = 0. So H^1(E, Z) = 0 (as a free abelian group, but there could be torsion).

But E might not be smooth, and even if H^1(E, C) = 0, there could be torsion in H^1(E, Z).

Actually, for any topological space, H^1(E, Z) is torsion-free (since H^1 = Hom(H_1, Z) and Hom into Z kills torsion). Wait, that's not right. H^1(E, Z) = Hom(H_1(E, Z), Z) by universal coefficients (since Ext(H_0, Z) = 0). And Hom of any abelian group into Z is torsion-free. So H^1(E, Z) is always torsion-free.

So if H^1(E, C) = 0, then H^1(E, Z) ⊗ C = 0, and since H^1(E, Z) is torsion-free, H^1(E, Z) = 0.

But wait, H^1(E, C) = 0 requires E to be smooth (for Hodge decomposition) or at least we need some version of Hodge theory for singular varieties.

For a singular projective variety E, we can use the fact that H^1(E, C) = H^1(E^{sm}, C) where E^{sm} is a resolution... no, that's not right either.

Actually, for any projective variety E (possibly singular), we have the Hodge-to-de Rham spectral sequence, and H^1(E, C) can be computed using Deligne's Hodge theory for singular varieties. But the relationship between H^1(E, O_E) and H^1(E, C) is more subtle for singular varieties.

Let me use a different approach. Let's use the fact that for the reduced exceptional divisor E, we can consider its normalization or a resolution of singularities of E.

Actually, let me step back and think about this more carefully using the exponential sequence and the formal function theorem.

From the exponential sequence on Y: 0 → Z → O_Y → O_Y^* → 0, applying Rπ_*:

R^0 π_* Z → R^0 π_* O_Y → R^0 π_* O_Y^* → R^1 π_* Z → R^1 π_* O_Y → ...

Since R^1 π_* O_Y = 0 (rational singularities), we get:
... → R^0 π_* O_Y^* → R^1 π_* Z → 0

So R^1 π_* Z is a quotient of π_* O_Y^*. Now, π_* O_Y = O_X (since X is normal and π has connected fibers). The map O_X → π_* O_Y^* sends a function to an invertible function. The kernel is the constant functions Z.

Hmm, this gives us R^1 π_* Z ≅ π_* O_Y^* / (O_X / Z) ... this is getting complicated. Let me think about whether this can be nonzero.

Actually, let me think about it locally. At a smooth point of X, π is an isomorphism, so R^1 π_* Z = 0 there. At a singular point x, the stalk (R^1 π_* Z)_x = H^1(E, Z) (by proper base change, as I argued before).

So the question is purely local: is H^1(E, Z) = 0 for the exceptional fiber of the resolution of a 3-dimensional rational singularity?

Now, I claimed that H^1(E, O_E) = 0 (from the theorem on formal functions and rational singularities). Let me see if I can use this to conclude H^1(E, Z) = 0.

If E is a reduced projective surface (possibly singular), and H^1(E, O_E) = 0, can we conclude H^1(E, Z) = 0?

Consider the exponential sequence on E: 0 → Z → O_E → O_E^* → 0.

H^1(E, Z) → H^1(E, O_E) → H^1(E, O_E^*) → H^2(E, Z) → H^2(E, O_E)

Since H^1(E, O_E) = 0: H^1(E, Z) → 0, so the map H^1(E, Z) → H^1(E, O_E) is the zero map, which means H^1(E, Z) maps to 0, but this doesn't tell us H^1(E, Z) = 0. The map H^1(E, Z) → H^1(E, O_E) is the map from singular cohomology to sheaf cohomology, which is the natural map H^1(E, Z) → H^1(E, O_E) = H^1(E, C)/F^1 (roughly). If H^1(E, O_E) = 0, this map is automatically zero, but H^1(E, Z) could still be nonzero (it would just map to zero).

So the vanishing of H^1(E, O_E) alone doesn't imply H^1(E, Z) = 0.

Hmm, so I need a different approach. Let me reconsider.

Actually, for E a reduced projective variety, we can use Deligne's Hodge theory. For any projective variety E (possibly singular), H^1(E, C) has a Hodge structure, and H^1(E, O_E) is the (0,1) part of H^1(E, C) (this is true for normal varieties, and more generally for varieties with rational singularities... but E itself might not have rational singularities).

Actually, for any projective variety E, the Hodge-to-de Rham spectral sequence gives:
E_1^{p,q} = H^q(E, Ω^p_E) ⇒ H^{p+q}(E, C)

where Ω^p_E are the Kähler differentials. For p=0, q=1: H^1(E, O_E) = H^1(E, Ω^0_E).

But for singular varieties, the Hodge-to-de Rham spectral sequence might not degenerate at E_1, and the relationship between H^1(E, O_E) and H^1(E, C) is more complicated.

Let me try yet another approach. Let me use the normalization.

Let ν: Ẽ → E be the normalization of E. Then we have:
0 → O_E → ν_* O_Ẽ → Q → 0 (where Q is supported on the singular locus of E)

Taking H^1: H^1(E, O_E) → H^1(E, ν_* O_Ẽ) → H^1(E, Q) → H^2(E, O_E)

H^1(E, ν_* O_Ẽ) = H^1(Ẽ, O_Ẽ).

If H^1(E, O_E) = 0 and H^2(E, O_E) = 0 (which we have from rational singularities), then:
0 → H^1(Ẽ, O_Ẽ) → H^1(E, Q) → 0

So H^1(Ẽ, O_Ẽ) ≅ H^1(E, Q). This doesn't directly help.

Hmm, let me try to think about this problem from the perspective of known results.

I recall that there's a result that says: for a rational singularity of dimension n, R^i π_* Z = 0 for 0 < i < n-1. Or something like that.

Actually, I think the relevant result might be related to the following:

For a rational singularity, the local intersection cohomology agrees with the local cohomology. More precisely, if X has rational singularities, then the natural map from the cohomology of the resolution to the intersection cohomology is an isomorphism (in some range).

Specifically, for a variety with rational singularities, IC_X = π_* C_Y[dim X] (in the derived category, up to shift). This is because rational singularities are rational homology manifolds... no, that's not quite right.

Actually, the key result is:

Theorem: If X has rational singularities, then X is a rational homology manifold, i.e., for all x ∈ X, H^i(X, X \ {x}; Q) = 0 for i < dim X, and H^{dim X}(X, X \ {x}; Q) = Q.

Wait, no. Rational singularities don't imply rational homology manifold in general. That's a stronger condition (related to intersection cohomology).

Let me reconsider. I think the correct statement is:

For a variety with rational singularities, the intersection cohomology IC_X satisfies IC_X = π_* Q_Y[dim X] (in the derived category, with Q coefficients). This is because the decomposition theorem applies to π_* Q_Y, and the rational singularity condition ensures that the top summand is IC_X and there are no other summands in certain degrees.

Hmm, actually, the decomposition theorem says π_* Q_Y[dim] = IC_X ⊕ (other summands). For rational singularities, the "other summands" might still be present.

Let me think about this more carefully using the decomposition theorem.

By the decomposition theorem (BBD), π_* Q_Y[3] = ⊕ IC_{Z_i}(L_i)[d_i] where Z_i are subvarieties of X, L_i are local systems, and d_i are shifts.

Since π is an isomorphism over X \ Sing(X), the only summands supported on all of X come from X itself, and summands supported on smaller subvarieties come from the singular points.

The top summand is IC_X(Q) (the trivial local system on X). The question is whether there are other summands, particularly those contributing to R^1 π_* Q.

R^1 π_* Q corresponds to the degree -2 part of π_* Q[3] (i.e., the cohomology sheaf in degree -2, which is R^1 π_* Q). The IC_X(Q) summand contributes to degree 0 (R^0 π_* Q = Q) and has no contribution to degree -2 (since IC_X is in degree 0 and has cohomology sheaves only in non-negative degrees relative to its shift).

Wait, I need to be more careful with the shifts. Let me think about this without shifts.

π_* Q_Y = ⊕ R^i π_* Q_Y[-i]. The decomposition theorem says this decomposes as a direct sum of IC sheaves (shifted).

The stalk of R^1 π_* Q at a singular point x is H^1(E, Q) (by proper base change). The question is whether this is 0.

By the decomposition theorem, π_* Q_Y[3] = IC_X ⊕ (summands supported at singular points). The summands supported at a point x are of the form (Q_x) placed in some degree. The contribution to R^1 π_* Q (which is the degree 1 part of π_* Q, or degree -2 of π_* Q[3]) comes from summands Q_x placed in degree -2 of π_* Q[3], i.e., degree 1 of π_* Q.

For a point summand Q_x[d], it contributes to R^{-d} π_* Q at x. So R^1 π_* Q at x gets contributions from summands Q_x[-1], i.e., Q_x[1] in the shifted complex... I'm getting confused with the shifts. Let me just think about it directly.

The decomposition theorem gives: π_* Q_Y = IC_X ⊕ ⊕_j (i_{x_j})_* Q_{x_j} [n_j] where i_{x_j}: {x_j} → X are the singular points and n_j are integers.

The cohomology sheaf H^k(π_* Q_Y) = R^k π_* Q_Y. The IC_X summand contributes to H^0 = R^0 π_* Q = Q (and IC_X has no other cohomology sheaves in the relevant range for a variety with rational singularities... actually IC_X can have cohomology sheaves in negative degrees).

Hmm, this is getting complicated. Let me try a more direct approach.

Let me think about specific examples of 3-dimensional rational singularities and compute H^1(E, Z).

Example 1: Ordinary double point (node). The 3-dimensional ordinary double point is the singularity x_1^2 + x_2^2 + x_3^2 + x_4^2 = 0 in C^4. This is a rational singularity (it's a hypersurface singularity with Milnor number 1, and it's rational because... actually, is it?).

For a hypersurface singularity, rationality is equivalent to the singularity being a rational double point in dimension 2, or more generally, having H^j(E, O_E) = 0 for j > 0 where E is the exceptional fiber.

The ordinary double point in dimension 3: the blow-up of the origin gives the exceptional divisor E = Q^2 ⊂ P^3, a smooth quadric surface. H^1(Q^2, Z) = 0 (since Q^2 ≅ P^1 × P^1). So R^1 π_* Z = 0 for this example.

Example 2: Consider a quotient singularity C^3/G where G is a finite subgroup of SL(3, C). These are rational singularities (by Boutot's theorem). The exceptional fiber of the resolution...

For a quotient singularity C^3/G, the link is S^5/G. The fundamental group of the link is G (since S^5 is simply connected). So π_1(L) = G, which is finite. Hence H^1(L, Z) = 0, and by the injection H^1(E, Z) ↪ H^1(L, Z), we get H^1(E, Z) = 0.

Wait, but does the injection hold? Let me re-examine. From the long exact sequence:
0 → H^1(E, Z) → H^1(L, Z) → H_4(E, Z) → ...

Yes, H^1(E, Z) injects into H^1(L, Z). So if H^1(L, Z) = 0, then H^1(E, Z) = 0.

For quotient singularities, H^1(L, Z) = Hom(G, Z) = 0 since G is finite. So H^1(E, Z) = 0.

Example 3: Cone over a rational surface S with H^1(S, Z) = 0. As I discussed, rational surfaces are simply connected, so H^1(S, Z) = 0, and the exceptional fiber is S, so H^1(E, Z) = 0.

But what if we take a cone over a surface that is not rational but the singularity is still rational? Can that happen?

For a cone over (S, L) where S is a smooth projective surface and L is an ample line bundle, the singularity is rational if and only if H^i(S, O_S) = 0 for i > 0, i.e., S is a rational surface (q = p_g = 0). So the cone is a rational singularity only when S is rational, in which case H^1(S, Z) = 0.

Hmm, so in all the examples I can think of, H^1(E, Z) = 0. This suggests the answer is YES.

Let me try to prove it in general.

Approach: Use the theorem on formal functions and Hodge theory.

From rational singularities: H^i(E, O_E) = 0 for i > 0 (where E is the reduced exceptional fiber, and this follows from the theorem on formal functions applied to R^i π_* O_Y = 0).

Now, I want to show H^1(E, Z) = 0. Since H^1(E, Z) is torsion-free (as I noted earlier, H^1(X, Z) = Hom(H_1(X, Z), Z) is always torsion-free), it suffices to show H^1(E, Q) = 0.

For H^1(E, Q) = 0, I need to show that the first Betti number b_1(E) = 0.

Now, for a projective variety E (possibly singular), b_1(E) = 2q(E) where q(E) = h^1(E, O_E) is the irregularity, BUT this is only true if E has rational singularities (or is smooth). For a general singular variety, b_1(E) can be larger than 2q(E).

Wait, actually, for any projective variety E, we have b_1(E) ≥ 2q(E) (where q(E) = h^1(E, O_E)), with equality if E has rational singularities. But E might not have rational singularities.

So H^1(E, O_E) = 0 doesn't directly imply H^1(E, Q) = 0 for singular E.

Hmm. Let me think about whether E has rational singularities.

The exceptional divisor E of a resolution of a rational singularity... does E itself have rational singularities? Not necessarily.

OK so let me think about this differently. Let me use the normalization of E.

Let ν: Ẽ → E be the normalization. Then E is a reduced projective surface, and Ẽ is a normal projective surface.

Claim: H^1(Ẽ, O_Ẽ) = 0.

Proof: From the exact sequence 0 → O_E → ν_* O_Ẽ → Q → 0, we get:
0 → H^0(O_E) → H^0(ν_* O_Ẽ) → H^0(Q) → H^1(O_E) → H^1(ν_* O_Ẽ) → H^1(Q) → H^2(O_E) → ...

Since H^1(O_E) = 0 and H^2(O_E) = 0:
0 → H^0(ν_* O_Ẽ) → H^0(Q) → 0 → H^1(ν_* O_Ẽ) → H^1(Q) → 0

So H^1(ν_* O_Ẽ) = H^1(Ẽ, O_Ẽ) ↪ H^1(Q) (it's isomorphic to H^1(Q) actually, from the exact sequence).

Hmm, this doesn't directly show H^1(Ẽ, O_Ẽ) = 0.

Let me try another approach. Let me use the fact that E is the exceptional fiber of a blow-up of a point.

If π: Y → X is the blow-up of a point x ∈ X, then E = P(C_x) where C_x is the tangent cone at x. The tangent cone is a 3-dimensional affine variety (the cone in the tangent space).

Actually, E is the exceptional divisor of the blow-up, which is P(T_x X) = Proj of the associated graded ring of O_{X,x}. This is a projective surface.

Hmm, I think I need to use a more sophisticated argument. Let me try to use the result about local fundamental groups.

Theorem (Kollár, 1995, "Shafarevich Maps and Plurigenera"): Let X be a variety with rational singularities over C. If dim X ≥ 3, then for every point x ∈ X, the local fundamental group π_1^{loc}(x, X) is finite.

If this theorem is correct, then:
- π_1(L) is finite, where L is the link of the singularity.
- H^1(L, Z) = Hom(π_1(L)^{ab}, Z) = 0 (since π_1(L) is finite).
- From the long exact sequence, H^1(E, Z) ↪ H^1(L, Z) = 0.
- Therefore H^1(E, Z) = 0.
- Therefore R^1 π_* Z = 0.

So the answer would be YES, R^1 π_* Z = 0.

But I need to verify that Kollár's theorem is indeed correct. Let me think about the proof idea.

The proof of Kollár's theorem uses the following idea: For a rational singularity, the exceptional fiber E of the resolution is "rationally chain connected" in some sense. More precisely, for any two general points on E, there is a chain of rational curves connecting them. This implies that π_1(E) is finite (by Kollár's theorem on rationally chain connected varieties).

But wait, E is the exceptional fiber of a resolution, and it might not be rationally chain connected in general. The rational chain connectedness of E follows from the rationality of the singularity.

Actually, I think the argument is more subtle. Let me recall:

For a rational singularity, R^i π_* O_Y = 0 for i > 0. By the theorem on formal functions, this implies H^i(Ê, O_Ê) = 0 for i > 0, where Ê is the formal completion of E in Y.

Now, Kollár's argument (I think) uses the following: if H^1(Ê, O_Ê) = 0, then the "formal Picard group" is trivial, which implies constraints on π_1(E).

Actually, I think the precise argument goes through the following:

Lemma: If H^1(E, O_E) = 0 (and E is the exceptional fiber of a resolution of an isolated singularity), then H^1(E, Z) is finite.

Wait, but H^1(E, Z) is torsion-free, so if it's finite, it must be 0. So the lemma would say H^1(E, Z) = 0.

Hmm, but I'm not sure this lemma is true without additional assumptions.

Let me think about this more carefully. For a smooth projective surface S, H^1(S, O_S) = 0 implies b_1(S) = 0 (by Hodge theory), so H^1(S, Z) = 0 (since H^1 is torsion-free). But for a singular surface E, this implication might fail.

However, for the normalization Ẽ of E, if Ẽ has rational singularities, then H^1(Ẽ, O_Ẽ) = 0 implies H^1(Ẽ, Z) = 0. And there's a relationship between H^1(E, Z) and H^1(Ẽ, Z).

Let me think about the relationship. We have ν: Ẽ → E, the normalization. The map on fundamental groups: π_1(Ẽ) → π_1(E) is surjective (for a normalization of a surface, the normalization map is a homeomorphism on a dense open set, and the fundamental group of E is a quotient of π_1(Ẽ) by the relations coming from the identifications along the non-normal locus).

Actually, for surfaces, the normalization map ν: Ẽ → E induces a surjection π_1(Ẽ) → π_1(E) → 0 (this is because E is obtained from Ẽ by identifying curves, which can only kill loops, not create them).

So H_1(Ẽ) → H_1(E) → 0, which means H^1(E) ↪ H^1(Ẽ) (dualizing).

So if H^1(Ẽ, Z) = 0, then H^1(E, Z) = 0.

Now, Ẽ is a normal projective surface. Does Ẽ have rational singularities?

Not necessarily. The normalization of the exceptional divisor of a resolution of a rational singularity need not have rational singularities.

Hmm, but we know H^1(Ẽ, O_Ẽ) = 0 (or do we? Let me check).

From the exact sequence 0 → O_E → ν_* O_Ẽ → Q → 0:
H^1(E, O_E) → H^1(E, ν_* O_Ẽ) → H^1(E, Q) → H^2(E, O_E)

H^1(E, ν_* O_Ẽ) = H^1(Ẽ, O_Ẽ).

If H^1(E, O_E) = 0 and H^2(E, O_E) = 0:
0 → H^1(Ẽ, O_Ẽ) → H^1(E, Q) → 0

So H^1(Ẽ, O_Ẽ) ≅ H^1(E, Q). This doesn't tell us H^1(Ẽ, O_Ẽ) = 0.

Hmm. So the vanishing of H^1(E, O_E) doesn't directly give us H^1(Ẽ, O_Ẽ) = 0.

OK let me try a completely different approach. Let me think about what's known in the literature.

I recall that there's a result by Steenbrink (or maybe it's by someone else) that for rational singularities, the mixed Hodge structure on the cohomology of the link has certain properties. Specifically:

For a rational singularity of dimension n, the link L has H^i(L, Q) = 0 for 0 < i < n-1.

Wait, is this true? For a surface rational singularity (n=2), the link is a 3-manifold, and H^1(L, Q) = 0 (since the link is a rational homology sphere). This is consistent with H^i(L, Q) = 0 for 0 < i < n-1 = 1, which gives H^i(L, Q) = 0 for 0 < i < 1, which is vacuous. Hmm, that doesn't match.

Let me reconsider. For a surface rational singularity (n=2), the link L is a 3-manifold with H^1(L, Q) = 0 and H^2(L, Q) = 0 (rational homology sphere). The condition H^i(L, Q) = 0 for 0 < i < n would give H^1(L, Q) = 0 for n = 2. That matches!

For a 3-fold rational singularity (n=3), the link L is a 5-manifold. The condition H^i(L, Q) = 0 for 0 < i < n = 3 would give H^1(L, Q) = 0 and H^2(L, Q) = 0.

If H^1(L, Q) = 0, then H^1(L, Z) is torsion (since H^1(L, Z) is torsion-free, H^1(L, Z) = 0). And then H^1(E, Z) ↪ H^1(L, Z) = 0, so H^1(E, Z) = 0.

So the key question is: for a 3-dimensional rational singularity, is H^1(L, Q) = 0?

I believe this is true, and it follows from the following result:

Theorem (Steenbrink, 1983, or Durfee-Steenbrink): For an isolated rational singularity of dimension n, the link L satisfies H^i(L, Q) = 0 for 0 < i < n-1.

Wait, for n=2, this gives H^i(L, Q) = 0 for 0 < i < 1, which is vacuous. But we know H^1(L, Q) = 0 for surface rational singularities. So the bound 0 < i < n-1 is not tight enough.

Let me reconsider. Maybe the result is H^i(L, Q) = 0 for 0 < i ≤ n-2? For n=2, this gives H^i(L, Q) = 0 for 0 < i ≤ 0, which is also vacuous. Hmm.

Or maybe H^i(L, Q) = 0 for 0 < i < n? For n=2: H^1(L, Q) = 0. For n=3: H^1(L, Q) = H^2(L, Q) = 0. This seems right!

Actually, I think the correct result is:

For an isolated hypersurface singularity with Milnor number μ, the Milnor fiber F has the homotopy type of a wedge of μ spheres of dimension n-1. The link L = ∂F. The long exact sequence of (F, L) gives:
... → H^i(F) → H^i(L) → H^{i+1}(F, L) → ...

For a rational singularity, μ = 0 (the Milnor number is 0), so F is contractible. Then H^i(L) = H^{i+1}(F, L) = H^{i+1}(D, L) (by excision, where D is a small ball). Since D is contractible, H^{i+1}(D, L) = H^i(L) by the long exact sequence of (D, L)... this is circular.

Actually, for a rational singularity, the Milnor fiber is not necessarily contractible. The Milnor number being 0 is for ADE singularities in dimension 2, but in higher dimensions, the relationship is more complex.

Let me try to use the result more directly. I think the key result is:

Theorem: For an isolated rational singularity of dimension n ≥ 2, the link L is a rational homology sphere, i.e., H^i(L, Q) = 0 for 0 < i < 2n-1.

Wait, the link of an isolated singularity of dimension n is a manifold of dimension 2n-1. A rational homology sphere would mean H^i(L, Q) = 0 for 0 < i < 2n-1.

For n=2 (surface): L is a 3-manifold, H^i(L, Q) = 0 for 0 < i < 3, i.e., H^1 = H^2 = 0. This is the rational homology sphere property, which is known for surface rational singularities. ✓

For n=3 (3-fold): L is a 5-manifold, H^i(L, Q) = 0 for 0 < i < 5, i.e., H^1 = H^2 = H^3 = H^4 = 0. This would be a very strong statement.

Is this true? I don't think the link of a 3-dimensional rational singularity is necessarily a rational homology sphere. In fact, I think there are counterexamples.

Consider the cone over P^1 × P^1 with the Segre embedding (or some ample line bundle). The cone is a 3-dimensional singularity. The exceptional fiber is P^1 × P^1, which has H^2(P^1 × P^1, Z) = Z^2. The link L is an S^1-bundle over P^1 × P^1 (the unit circle bundle of the line bundle). So H^1(L, Z) = 0 (since the S^1-bundle over a simply connected base with c_1 ≠ 0 has H^1 = 0), but H^2(L, Z) and H^3(L, Z) might be nonzero.

Actually, for the S^1-bundle over P^1 × P^1 with Chern class c = (a, b) (for the line bundle O(a,b)), the Gysin sequence gives:
... → H^i(P^1×P^1) → H^i(P^1×P^1) → H^{i+1}(L) → H^{i+1}(P^1×P^1) → ...

where the map H^i(P^1×P^1) → H^i(P^1×P^1) is the cup product with c.

For i=1: H^1(P^1×P^1) = 0, so 0 → H^2(L) → H^2(P^1×P^1) → H^2(P^1×P^1) → H^3(L) → H^3(P^1×P^1) = 0

H^2(P^1×P^1) = Z^2, and the cup product with c = (a,b) is the map Z^2 → Z^2 given by (x,y) ↦ (ax+by, ...) ... actually, the cup product with c_1(L) = aH_1 + bH_2 on H^2 is the map H^2 → H^4 given by α ↦ α ∧ c_1. Since H^4(P^1×P^1) = Z, this is the map Z^2 → Z given by (x, y) ↦ ax + by (where x, y are the coefficients of the two generators of H^2).

So: 0 → H^2(L) → Z^2 → Z → H^3(L) → 0

If gcd(a,b) = 1 (primitive class), then the map Z^2 → Z is surjective, so H^2(L) = ker(Z^2 → Z) = Z and H^3(L) = 0.

So H^2(L, Z) = Z ≠ 0, which means L is not a rational homology sphere. But the singularity is rational (cone over P^1×P^1 with an ample line bundle, and P^1×P^1 is a rational surface with H^i(O) = 0 for i > 0).

So the link of a 3-dimensional rational singularity is NOT necessarily a rational homology sphere. However, H^1(L, Z) = 0 in this example.

So maybe the correct statement is H^1(L, Q) = 0 for rational singularities of any dimension, even though higher cohomology of the link can be nonzero.

Let me check: in the cone example, H^1(L, Z) = 0. ✓

And from the long exact sequence, H^1(E, Z) ↪ H^1(L, Z) = 0, so H^1(E, Z) = 0. ✓

So the question is: is H^1(L, Q) = 0 always true for rational singularities?

I think the answer is yes, and it follows from the following:

For a rational singularity, the local fundamental group π_1(L) is finite (at least in dimension ≥ 3, by Kollár's theorem; in dimension 2, it's also finite, as the link of a surface rational singularity is a rational homology sphere with finite π_1).

If π_1(L) is finite, then H_1(L, Z) = π_1(L)^{ab} is finite, so H^1(L, Z) = Hom(H_1(L, Z), Z) = 0.

So the key is Kollár's theorem on the finiteness of local fundamental groups for rational singularities.

Let me try to recall/verify this theorem.

Kollár's theorem (from "Shafarevich Maps and Plurigenera", 1995, and also in his book "Rational Curves on Algebraic Varieties"):

Theorem: Let X be a variety with rational singularities over C, and let x ∈ X be a closed point. If dim X ≥ 3, then π_1^{loc}(x, X) is finite.

The proof idea: 
1. For a resolution π: Y → X with exceptional fiber E over x, the rational singularity condition implies that E is "rationally chain connected" in an appropriate sense.
2. Rationally chain connected varieties have finite fundamental group (Kollár's theorem).
3. The local fundamental group π_1(L) is a quotient of π_1(E) (from the long exact sequence of the pair (V, L) where V retracts to E, we get π_1(E) → π_1(L) → 0... wait, is this right?).

Actually, from the long exact sequence of homotopy groups for the pair (V, L):
... → π_1(L) → π_1(V) → π_1(V, L) → π_0(L) → ...

Since V retracts to E, π_1(V) = π_1(E). And π_1(V, L) relates to the relative homotopy. For the pair (V, L) where V is a manifold with boundary L:
π_1(L) → π_1(V) → π_1(V, L) → π_0(L) → π_0(V)

Since V and L are connected: 0 → π_1(V, L) → 0, so π_1(V, L) = 0 (as a set, it's trivial). Wait, that's the end of the sequence. Let me be more careful.

The long exact sequence of homotopy groups for (V, L):
... → π_2(V, L) → π_1(L) → π_1(V) → π_1(V, L) → π_0(L) → π_0(V)

Since V and L are connected: π_0(L) → π_0(V) is a bijection, so π_1(V, L) → π_0(L) has trivial kernel... actually, π_1(V, L) → π_0(L) → π_0(V) means the image of π_1(V, L) in π_0(L) is the kernel of π_0(L) → π_0(V), which is trivial. So the map π_1(V) → π_1(V, L) is surjective.

And π_1(L) → π_1(V) has image equal to the kernel of π_1(V) → π_1(V, L).

So we have: π_1(L) → π_1(E) → π_1(V, L) → 0

This doesn't directly give us that π_1(L) is a quotient of π_1(E). In fact, π_1(L) → π_1(E) is a map, and its image is a normal subgroup of π_1(E).

Hmm, so the relationship is more complex. Let me reconsider.

Actually, for the purpose of showing H^1(L, Z) = 0, I need π_1(L) to be finite (or at least H_1(L, Z) to be finite). The finiteness of π_1(L) for rational singularities is what Kollár proves, but the proof might not go through π_1(E).

Let me look at this from a different angle. I think Kollár's proof directly shows that π_1(L) is finite, using the rational chain connectedness of the exceptional fiber and some topological arguments.

Actually, I think the argument is as follows:

1. For a rational singularity, the exceptional fiber E is rationally chain connected (RCC). This follows from the vanishing of R^i π_* O_Y and some arguments using the theorem on formal functions.

2. If E is RCC, then any finite étale cover of E is trivial (Kollár's theorem: RCC varieties have no nontrivial étale covers). This means π_1(E) is finite... no, it means the algebraic fundamental group π_1^{ét}(E) is finite. For the topological fundamental group, we need more.

Actually, for normal projective varieties over C, the topological fundamental group is finite if and only if the algebraic fundamental group is finite (this is a consequence of the Riemann existence theorem and the fact that finite étale covers correspond to finite topological covers). But E might not be normal.

Hmm, let me think about this differently.

Actually, I think the key result that Kollár proves is not about π_1(E) but directly about π_1(L). The argument goes:

1. For a rational singularity, the local fundamental group π_1(L) is finite.
2. This is proved by showing that any finite étale cover of a punctured neighborhood of x extends to a finite étale cover of the neighborhood, and then using the rationality condition to show this cover must be trivial.

Actually, I think the precise statement and proof can be found in Kollár's book. Let me just accept the theorem and use it.

So, assuming Kollár's theorem:

Theorem (Kollár): For a variety X with rational singularities over C, dim X ≥ 3, the local fundamental group π_1^{loc}(x, X) is finite for every x ∈ X.

Then:
- π_1(L) is finite.
- H_1(L, Z) = π_1(L)^{ab} is finite.
- H^1(L, Z) = Hom(H_1(L, Z), Z) = 0 (since H_1 is finite).
- From the long exact sequence: 0 → H^1(E, Z) → H^1(L, Z) = 0.
- Therefore H^1(E, Z) = 0.
- Therefore (R^1 π_* Z)_x = H^1(E, Z) = 0 for every singular point x.
- For smooth points, R^1 π_* Z = 0 (since π is an isomorphism there).
- Therefore R^1 π_* Z = 0.

So the answer is YES, R^1 π_* Z = 0.

Wait, but I should double-check the step where I use proper base change to say (R^1 π_* Z)_x = H^1(E, Z). Let me be more careful.

The proper base change theorem says: for a proper morphism π: Y → X and a geometric point x̄ → X, the natural map (R^i π_* F)_{x̄} → H^i(Y_{x̄}, F_{x̄}) is an isomorphism, where Y_{x̄} = Y ×_X x̄ is the geometric fiber.

For a closed point x ∈ X (over C, so x is already a geometric point), Y_x = π^{-1}(x) = E (the exceptional fiber, which is the reduced fiber if the singularity is isolated). And F = Z (the constant sheaf), so F_{x̄} = Z.

So (R^1 π_* Z)_x = H^1(E, Z). ✓

Now, I should also verify that the long exact sequence gives the injection H^1(E, Z) → H^1(L, Z).

We have V = π^{-1}(U) where U is a small Stein neighborhood of x in X. V is a complex manifold with boundary L (the link). E = π^{-1}(x) is a deformation retract of V (since U is contractible to x, and π is a resolution).

Wait, is V a manifold with boundary? V is an open subset of the smooth variety Y, so it's a manifold. But L is not the boundary of V in the topological sense; L is the preimage of the boundary of U.

Let me be more precise. Let B_ε be a small ball around x in X (in some embedding), and let L = ∂B_ε ∩ X_{reg} (the link). Let V = π^{-1}(B_ε) and ∂V = π^{-1}(L). Then V is a manifold with boundary ∂V = π^{-1}(L), and E = π^{-1}(x) is a deformation retract of V.

The long exact sequence of the pair (V, ∂V):
... → H^i(V, ∂V) → H^i(V) → H^i(∂V) → H^{i+1}(V, ∂V) → ...

H^i(V) = H^i(E) (deformation retract).
H^i(V, ∂V) = H_{6-i}(V) = H_{6-i}(E) (Poincaré-Lefschetz duality, since V is an oriented 6-manifold with boundary).

For i = 1:
H^1(V, ∂V) → H^1(V) → H^1(∂V) → H^2(V, ∂V)
= H_5(E) → H^1(E) → H^1(L) → H_4(E)

Since E is a complex surface (real dim 4), H_5(E) = 0. So:
0 → H^1(E) → H^1(L) → H_4(E)

This gives the injection H^1(E, Z) ↪ H^1(L, Z). ✓

So the argument is complete, assuming Kollár's theorem.

Actually, wait. I need to be a bit more careful. The problem says "let π: Y → X be the resolution of singularities obtained by blowing up the singular points." This means π is specifically the blow-up of the singular points. For this to be a resolution, the singularities must be such that a single blow-up resolves them.

Also, I assumed the singularities are isolated (since we're blowing up "the singular points"). If the singular locus has positive dimension, blowing up the singular locus (not points) would be needed. But the problem says "blowing up the singular points," which suggests isolated singularities.

For isolated singularities, the blow-up of the singular point gives an exceptional divisor E which is a projective surface. The above argument applies.

So, to summarize the proof:

1. X has rational singularities, so by Kollár's theorem, the local fundamental group π_1(L) at each singular point is finite (since dim X = 3 ≥ 3).

2. Finiteness of π_1(L) implies H^1(L, Z) = 0 (since H^1(L, Z) = Hom(π_1(L)^{ab}, Z) and there are no nontrivial homomorphisms from a finite group to Z).

3. By the long exact sequence of the pair (V, ∂V) where V is a tubular neighborhood of the exceptional fiber E and ∂V is the link L, we have an injection H^1(E, Z) ↪ H^1(L, Z) = 0.

4. Therefore H^1(E, Z) = 0 for each exceptional fiber.

5. By proper base change, (R^1 π_* Z)_x = H^1(E_x, Z) = 0 for each singular point x, and R^1 π_* Z = 0 on the smooth locus (where π is an isomorphism).

6. Therefore R^1 π_* Z = 0.

Hmm wait, but I should double-check Kollár's theorem. Is it really true that for 3-dimensional rational singularities, the local fundamental group is finite?

Let me think about potential counterexamples. Consider a 3-dimensional singularity that is a cone over an abelian surface. The cone over an abelian surface A with an ample line bundle L: the singularity is rational if and only if H^i(A, O_A) = 0 for i > 0. But H^1(A, O_A) = g (the dimension of A) = 2 ≠ 0. So the cone over an abelian surface is NOT a rational singularity. Good, so this is not a counterexample.

What about a cone over a bielliptic surface? H^1(O) = 1 ≠ 0, so not rational.

What about a cone over an Enriques surface? H^1(O) = 0, H^2(O) = 0 (since p_g = 0 and q = 0 for Enriques surfaces). So the cone over an Enriques surface IS a rational singularity!

The Enriques surface S has π_1(S) = Z/2Z (nontrivial fundamental group). The exceptional fiber E = S. So H^1(E, Z) = Hom(Z/2Z, Z) = 0. ✓

But what about the link? The link L is an S^1-bundle over S. The fundamental group of L fits into:
1 → Z → π_1(L) → π_1(S) = Z/2Z → 1

(This is the homotopy exact sequence of the fibration S^1 → L → S, assuming the bundle is locally trivial, which it is for the link of a cone.)

So π_1(L) is an extension of Z/2Z by Z. This could be Z (if the extension splits as Z → Z → Z/2Z, i.e., the map Z → Z is multiplication by 2) or Z × Z/2Z or something else.

If π_1(L) = Z, then H^1(L, Z) = Z ≠ 0, and the injection H^1(E, Z) → H^1(L, Z) would give 0 → Z, which is fine (0 injects into anything).

But wait, this would mean H^1(L, Z) ≠ 0, which contradicts what I need. However, H^1(E, Z) = 0 still holds (since H^1(Enriques, Z) = 0).

Hmm, so in this case, H^1(L, Z) ≠ 0 but H^1(E, Z) = 0. The injection H^1(E, Z) → H^1(L, Z) is 0 → Z, which is fine.

But this means my argument via Kollár's theorem might be wrong, because π_1(L) is infinite (it contains Z as a subgroup)!

Wait, let me reconsider. Is the cone over an Enriques surface really a rational singularity?

An Enriques surface S has:
- q = h^1(S, O_S) = 0
- p_g = h^2(S, O_S) = 0

The cone over (S, L) for an ample line bundle L is a rational singularity if and only if H^i(S, O_S) = 0 for i > 0, which is satisfied (q = p_g = 0). So yes, the cone over an Enriques surface is a rational singularity.

But the link L has π_1(L) which is an extension of Z/2Z by Z, so π_1(L) is infinite!

This contradicts Kollár's theorem (if the theorem says π_1(L) is finite for dim ≥ 3 rational singularities).

So either:
(a) Kollár's theorem doesn't say what I think it says, or
(b) The cone over an Enriques surface is not a rational singularity, or
(c) My computation of π_1(L) is wrong.

Let me check (b) more carefully. The cone over (S, L) is the affine cone Spec ⊕ H^0(S, L^n). This is a rational singularity if and only if the natural map R^i π_* O_Y → ... vanishes, where π is the resolution.

The resolution of the cone is the total space of L^{-1} = O_S(-D) where L = O_S(D). The exceptional fiber is S. By the theorem on formal functions:
(R^i π_* O_Y)^∧_0 = lim H^i(S, O_S ⊗ L^{-n}/O_S(-nD)) ... 

Actually, the theorem on formal functions says:
(R^i π_* O_Y)^∧_0 = lim_n H^i(E_n, O_{E_n})

where E_n is the n-th infinitesimal neighborhood of E = S in Y. For the total space of L^{-1}, E_n corresponds to the n-th order neighborhood, and H^i(E_n, O_{E_n}) = H^i(S, O_S / m^n) where m is the ideal of E in Y.

Actually, for the total space of a line bundle L^{-1} over S, the n-th infinitesimal neighborhood of S (the zero section) has O_{E_n} = O_S ⊕ L ⊕ L^2 ⊕ ... ⊕ L^{n-1} (as a sheaf on S, using the decomposition coming from the grading). Wait, that's not quite right. Let me think again.

The total space Y = Spec_S ⊕_{k≥0} L^k (where L is the line bundle, and the total space of L^{-1} is Spec of the symmetric algebra of L). The zero section S ⊂ Y has ideal sheaf I = ⊕_{k≥1} L^k. The n-th infinitesimal neighborhood E_n has O_{E_n} = O_Y / I^{n+1} = ⊕_{k=0}^{n} L^k (restricted to S).

So H^i(E_n, O_{E_n}) = ⊕_{k=0}^{n} H^i(S, L^k).

For the singularity to be rational, we need (R^i π_* O_Y)^∧_0 = lim_n ⊕_{k=0}^{n} H^i(S, L^k) = 0 for i > 0.

For i = 1: lim_n ⊕_{k=0}^{n} H^1(S, L^k) = 0. Since H^1(S, O_S) = 0 (q = 0 for Enriques), and for k ≥ 1, H^1(S, L^k) = 0 by Serre vanishing (for k large enough). But for small k, H^1(S, L^k) might be nonzero!

For an Enriques surface, H^1(S, L^k) for k ≥ 1 and L ample: by Kodaira vanishing (or Serre vanishing), H^1(S, L^k) = 0 for k ≥ 1 (since L is ample, L^k is ample for k ≥ 1, and by Kodaira vanishing, H^i(S, L^k ⊗ K_S) = 0 for i > 0; but K_S for Enriques is a 2-torsion, so K_S is not trivial but K_S^2 = O_S. Actually, Kodaira vanishing says H^i(S, L^k ⊗ K_S) = 0 for i > 0 and k ≥ 1. This gives H^i(S, L^k) = H^i(S, (L^k ⊗ K_S) ⊗ K_S^{-1})... hmm, this doesn't directly give H^i(S, L^k) = 0.

Let me use Serre vanishing instead: for L ample, H^i(S, L^k) = 0 for k ≫ 0 and i > 0. But for small k, it might not vanish.

Actually, for an Enriques surface, let me think about what happens. The canonical bundle K_S is a nontrivial 2-torsion element, so K_S ≠ O_S but K_S^{⊗2} = O_S.

By Serre duality: H^1(S, L^k) = H^1(S, L^k)^* = H^1(S, K_S ⊗ L^{-k})^*... wait, Serre duality says H^i(S, F) = H^{2-i}(S, K_S ⊗ F^{-1})^* for a surface. So H^1(S, L^k) = H^1(S, K_S ⊗ L^{-k})^*.

For k ≥ 1, L^{-k} is anti-ample, so K_S ⊗ L^{-k} is also anti-ample (since K_S is numerically trivial for Enriques). By Serre vanishing (or just by ampleness considerations), H^1(S, K_S ⊗ L^{-k}) = 0 for k ≥ 1? No, Serre vanishing says H^i(S, A^m) = 0 for A ample and m ≫ 0. For anti-ample bundles, we can't directly use Serre vanishing.

Actually, for an anti-ample bundle M on a surface, H^0(S, M) = 0 (since global sections of an anti-ample bundle must vanish), and by Serre duality, H^2(S, M) = H^0(S, K_S ⊗ M^{-1})^*. If M = K_S ⊗ L^{-k}, then M^{-1} = K_S^{-1} ⊗ L^k = K_S ⊗ L^k (since K_S^{-1} = K_S for 2-torsion). So H^2(S, K_S ⊗ L^{-k}) = H^0(S, K_S ⊗ K_S ⊗ L^k)^* = H^0(S, L^k)^* (since K_S^2 = O_S). And H^0(S, L^k) ≠ 0 for k ≥ 1 (since L is ample). So H^2(S, K_S ⊗ L^{-k}) ≠ 0.

By Riemann-Roch for surfaces: χ(L^k) = χ(O_S) + (L^k · (L^k - K_S))/2. For Enriques, χ(O_S) = 1 (since q = 0, p_g = 0, χ = 1 - q + p_g = 1). And K_S is numerically trivial, so (L^k · K_S) = 0. So χ(L^k) = 1 + (L^k)^2/2 = 1 + k^2 L^2/2.

χ(L^k) = h^0(L^k) - h^1(L^k) + h^2(L^k).

h^0(L^k) = χ(L^k) + h^1(L^k) - h^2(L^k).

By Serre duality: h^2(L^k) = h^0(K_S ⊗ L^{-k}) = h^0(K_S ⊗ L^{-k}). Since L^{-k} is anti-ample and K_S is numerically trivial, K_S ⊗ L^{-k} is anti-ample, so h^0(K_S ⊗ L^{-k}) = 0.

So h^0(L^k) = 1 + k^2 L^2/2 + h^1(L^k).

For k = 0: h^0(O_S) = 1, χ(O_S) = 1, h^1(O_S) = 0, h^2(O_S) = 0. Check: 1 = 1 + 0 - 0. ✓

For k = 1: h^0(L) = 1 + L^2/2 + h^1(L). If L^2 > 0 (ample), then h^0(L) ≥ 1 + L^2/2 > 1. And h^1(L) = h^0(L) - 1 - L^2/2.

Hmm, I can't determine h^1(L) without more information. But the point is that h^1(L^k) might be nonzero for some k.

If h^1(S, L^k) ≠ 0 for some k ≥ 1, then H^1(E_n, O_{E_n}) ≠ 0 for n ≥ k, and the inverse limit (R^1 π_* O_Y)^∧_0 ≠ 0, which would mean the singularity is NOT rational.

So the question is: for an Enriques surface S with an ample line bundle L, is H^1(S, L^k) = 0 for all k ≥ 1?

By Kodaira vanishing: H^i(S, L^k ⊗ K_S) = 0 for i > 0 and k ≥ 1 (since L^k ⊗ K_S is ample for k ≥ 1, because K_S is numerically trivial). So H^1(S, L^k ⊗ K_S) = 0 for k ≥ 1.

But we want H^1(S, L^k), not H^1(S, L^k ⊗ K_S). Since K_S is a nontrivial 2-torsion, L^k and L^k ⊗ K_S are different line bundles.

So Kodaira vanishing gives H^1(S, L^k ⊗ K_S) = 0 but not H^1(S, L^k) = 0.

Hmm, so it's possible that H^1(S, L^k) ≠ 0 for some k, which would mean the cone over an Enriques surface is NOT a rational singularity.

Let me check for a specific Enriques surface and line bundle. Take S to be an Enriques surface and L = O_S(D) where D is an ample divisor with D^2 = 2 (such divisors exist on Enriques surfaces).

For k = 1: χ(L) = 1 + 2/2 = 2. h^0(L) = 2 + h^1(L) (since h^2(L) = 0 as computed above). By Riemann-Roch, h^0(L) - h^1(L) = 2. So h^0(L) = 2 + h^1(L).

For an Enriques surface, the Picard group has rank 10, and there are many line bundles. For a generic ample L with L^2 = 2, I believe h^0(L) = 2 (by the birational geometry of Enriques surfaces), which would give h^1(L) = 0.

But this might not always be the case. For some special L, h^1(L) might be nonzero.

Actually, for Enriques surfaces, by a result of Cossec and Dolgachev, if L is ample with L^2 = 2, then the linear system |L| has no fixed components and the general member is a smooth curve of genus 2. In this case, h^0(L) = 2 and h^1(L) = 0.

But for other values of L^2, the situation might be different. For example, if L^2 = 0, L is not ample. For L^2 = 4, h^0(L) = 1 + 4/2 + h^1(L) = 3 + h^1(L). If h^0(L) = 3, then h^1(L) = 0.

I think for Enriques surfaces, by Kodaira vanishing applied to L^k ⊗ K_S, and using the fact that K_S is 2-torsion, we can show that h^1(L^k) = 0 for k ≥ 2 (since L^k is "sufficiently ample"). But for k = 1, it depends on the specific L.

Actually, let me use a different approach. For k ≥ 2, L^k is "very ample" (by Serre's theorem), and by Kodaira vanishing with K_S:
H^1(S, L^k ⊗ K_S) = 0 for k ≥ 1.

And also, for k ≥ 2, L^{k-1} is ample (since L is ample), and by Kodaira vanishing:
H^1(S, L^{k-1} ⊗ K_S) = 0 for k ≥ 2.

But I want H^1(S, L^k), not H^1(S, L^k ⊗ K_S). Since K_S is 2-torsion, L^k ⊗ K_S ≠ L^k in general.

Hmm, but there's a trick. Consider the exact sequence:
0 → L^k → L^k ⊗ K_S^{-1} → ... 

No, that doesn't work since K_S is not trivial.

Let me try another approach. By the Kawamata-Viehweg vanishing theorem (which generalizes Kodaira vanishing): if L is ample and big (which it is for L^2 > 0 on a surface), then H^i(S, L ⊗ K_S) = 0 for i > 0. But again, this is for L ⊗ K_S, not L.

For L itself, we can use the fact that L = (L ⊗ K_S) ⊗ K_S^{-1} = (L ⊗ K_S) ⊗ K_S (since K_S^{-1} = K_S for 2-torsion). So L = (L ⊗ K_S) ⊗ K_S. By Kodaira vanishing, H^i(S, L ⊗ K_S) = 0 for i > 0. But this doesn't directly give H^i(S, L) = 0.

OK, I think the issue is that for Enriques surfaces, H^1(S, L) might be nonzero for some ample L, which would mean the cone is not a rational singularity. Let me check this more carefully.

Actually, I recall that for an Enriques surface, the cone over (S, L) is a rational singularity if and only if H^1(S, L^n) = 0 for all n ≥ 1 (and H^2(S, L^n) = 0 for all n ≥ 1, which follows from Kodaira vanishing since H^2(S, L^n) = H^0(S, K_S ⊗ L^{-n})^* = 0 for n ≥ 1).

The condition H^1(S, L^n) = 0 for all n ≥ 1 is equivalent to the section ring R(S, L) being Cohen-Macaulay (by a theorem of Watanabe or similar).

For Enriques surfaces, I believe this is NOT always the case. There exist ample line bundles L on Enriques surfaces such that H^1(S, L) ≠ 0, and in such cases, the cone is NOT a rational singularity.

In fact, I recall that for Enriques surfaces, the section ring R(S, L) is Cohen-Macaulay if and only if L is "non-special" in some sense, and there are examples where it's not Cohen-Macaulay.

So the cone over an Enriques surface might NOT be a rational singularity in general. This resolves the potential contradiction with Kollár's theorem.

But wait, there might be some ample L on an Enriques surface for which H^1(S, L^n) = 0 for all n ≥ 1, making the cone a rational singularity. In that case, the exceptional fiber E = S has H^1(E, Z) = H^1(S, Z) = Hom(π_1(S), Z) = Hom(Z/2Z, Z) = 0. So even in this case, H^1(E, Z) = 0.

So the Enriques surface example, even if it gives a rational singularity, still has H^1(E, Z) = 0. Good.

Let me think of another potential counterexample. What about a cone over a surface S with q = p_g = 0 but H^1(S, Z) ≠ 0?

A surface with q = 0 has b_1 = 0 (for smooth surfaces, b_1 = 2q). So H^1(S, Z) is torsion (since b_1 = 0 means H^1(S, Z) ⊗ Q = 0, and H^1(S, Z) is torsion-free, so H^1(S, Z) = 0). Wait, H^1(S, Z) is always torsion-free (as I noted earlier, H^1 = Hom(H_1, Z) is torsion-free). So if b_1 = 0, then H^1(S, Z) = 0.

So for any smooth surface S with q = 0, H^1(S, Z) = 0. And the cone over S is a rational singularity only if q = p_g = 0. So for cones over smooth surfaces, the rational singularity condition implies H^1(E, Z) = 0.

But the exceptional fiber E might not be a smooth surface in general. It could be a singular surface or a union of surfaces.

Let me think about the case where E is reducible. Suppose E = E_1 ∪ E_2 ∪ ... ∪ E_k, a union of surfaces. Then H^1(E, Z) can be computed using the Mayer-Vietoris sequence.

For a union of two surfaces E = E_1 ∪ E_2:
... → H^0(E_1) ⊕ H^0(E_2) → H^0(E_1 ∩ E_2) → H^1(E) → H^1(E_1) ⊕ H^1(E_2) → H^1(E_1 ∩ E_2) → ...

If E_1 and E_2 are rational surfaces (H^1 = 0) and E_1 ∩ E_2 is a curve (so H^1(E_1 ∩ E_2) could be nonzero), then:
... → H^0(E_1 ∩ E_2) → H^1(E) → 0 → H^1(C) → ...

So H^1(E) ≅ coker(H^0(E_1) ⊕ H^0(E_2) → H^0(E_1 ∩ E_2)).

If E_1 ∩ E_2 is connected, then H^0(E_1 ∩ E_2) = Z, and the map Z ⊕ Z → Z is (a, b) ↦ a + b (or a - b, depending on orientation), which is surjective. So H^1(E) = 0.

If E_1 ∩ E_2 has multiple connected components, then H^0(E_1 ∩ E_2) = Z^m (m components), and the map Z ⊕ Z → Z^m might not be surjective, giving H^1(E) ≠ 0.

But for a resolution of a rational singularity, the exceptional fiber should be connected (since π has connected fibers, as X is normal). And the dual complex of the exceptional fiber (the intersection graph) should be connected. But the individual intersections E_i ∩ E_j could be disconnected.

Hmm, this is getting complicated. Let me go back to the general argument.

I think the correct approach is to use Kollár's theorem on the finiteness of local fundamental groups for rational singularities in dimension ≥ 3. Let me look at this more carefully.

Actually, I now recall that Kollár's theorem might have a more nuanced statement. Let me think about what exactly is proved.

In Kollár's book "Rational Curves on Algebraic Varieties" (Theorem 5.20 or similar), and in his paper "Shafarevich Maps and Plurigenera", the result is:

Theorem: Let X be a variety with rational singularities over C. Then for any point x ∈ X, the local fundamental group π_1^{loc}(x, X) is finite, provided that dim X ≥ 3.

Wait, I think there might be additional hypotheses. Let me think about what the proof requires.

The proof idea (as I recall):
1. For a resolution π: Y → X, the exceptional fiber E is rationally chain connected. This follows from the vanishing of R^1 π_* O_Y (which implies that E has no nontrivial étale covers, by a lifting argument).
2. RCC implies finite π_1 (for normal projective varieties).
3. The local fundamental group π_1(L) is a quotient of π_1(E) (or related to it).

But step 1 might require E to be normal, and step 3 might not be a simple quotient relationship.

Actually, I think the precise statement might be:

Theorem (Kollár): Let X be a variety with rational singularities. Then the local fundamental group π_1^{loc}(x, X) is finite for every x ∈ X if dim X ≥ 3.

And the proof uses:
1. The exceptional fiber E is "rationally chain connected" in the sense that any two general points can be connected by a chain of rational curves.
2. This implies that π_1(E) is finite (for E normal, by Kollár's theorem on RCC varieties).
3. The local fundamental group is related to π_1(E) via the exact sequence of the pair (V, L).

But I'm not sure about step 2 when E is not normal, and step 3 might give that π_1(L) is a quotient of π_1(E) only under certain conditions.

Let me try a different approach entirely. Instead of using Kollár's theorem, let me try to directly prove H^1(E, Z) = 0 using the rational singularity condition.

Approach via exponential sequence and Hodge theory:

From the exponential sequence 0 → Z → O_Y → O_Y^* → 0 on Y, applying Rπ_*:

... → R^0 π_* O_Y → R^0 π_* O_Y^* → R^1 π_* Z → R^1 π_* O_Y → ...

Since R^1 π_* O_Y = 0 (rational singularities):
R^0 π_* O_Y → R^0 π_* O_Y^* → R^1 π_* Z → 0

So R^1 π_* Z is a quotient of R^0 π_* O_Y^* / (image of R^0 π_* O_Y).

Now, R^0 π_* O_Y = O_X (since X is normal and π has connected fibers). And R^0 π_* O_Y^* = π_* O_Y^* is the sheaf of invertible holomorphic functions on Y, pushed forward to X.

At a smooth point x, π is an isomorphism, so (π_* O_Y^*)_x = O_{X,x}^* and the map O_{X,x} → O_{X,x}^* is the exponential map, whose cokernel is 0 (since every invertible function locally has a logarithm). So R^1 π_* Z = 0 at smooth points. ✓

At a singular point x, (π_* O_Y^*)_x is the group of invertible holomorphic functions on V = π^{-1}(U) (for a small neighborhood U of x). The map O_{X,x} → (π_* O_Y^*)_x sends a function f to exp(f) (or rather, the exponential map from O to O^*).

Hmm, this is the map from additive functions to multiplicative functions. The cokernel is (π_* O_Y^*)_x / exp(O_{X,x}).

For the stalk of R^1 π_* Z at x, we have:
(R^1 π_* Z)_x = (π_* O_Y^*)_x / (O_{X,x} / Z_x)

where Z_x is the kernel of O_{X,x} → (π_* O_Y^*)_x, which is the constant functions Z.

So (R^1 π_* Z)_x = (π_* O_Y^*)_x / (O_{X,x}/Z).

This is related to the local Picard group. Specifically, (π_* O_Y^*)_x / O_{X,x}^* is the local Picard group Pic(V) / Pic(U) (roughly), and (R^1 π_* Z)_x is this modulo the image of O_{X,x}/Z.

This is getting complicated. Let me try yet another approach.

Approach via the theorem on formal functions and mixed Hodge structures:

For an isolated singularity x ∈ X of dimension n, with resolution π: Y → X and exceptional fiber E, there is a mixed Hodge structure on H^i(E, Z) (since E is a projective variety). The rational singularity condition imposes constraints on this mixed Hodge structure.

Specifically, by Steenbrink's theory (or the theory of mixed Hodge structures on singular varieties), for a rational singularity:
- The weight filtration on H^i(E, Q) has certain properties.
- In particular, H^1(E, Q) has weights ≥ 2 (or something like that).

Actually, I think the key result is:

For a rational singularity, the mixed Hodge structure on H^i(E, Q) is such that Gr^W_j H^i(E, Q) = 0 for j < i (or some similar condition).

Hmm, I don't remember the exact statement. Let me think about this differently.

Actually, let me go back to the approach using the long exact sequence and try to prove H^1(L, Z) = 0 directly.

From the long exact sequence:
0 → H^1(E, Z) → H^1(L, Z) → H_4(E, Z) → H^2(E, Z) → H^2(L, Z) → H_3(E, Z) → H^3(E, Z) → H^3(L, Z) → H_2(E, Z) → H^2(E, Z) → ...

Wait, I had: H^i(V, ∂V) = H_{6-i}(E) (by Poincaré-Lefschetz duality and deformation retract).

For i=1: H_5(E) → H^1(E) → H^1(L) → H_4(E) → H^2(E) → H^2(L) → H_3(E) → H^3(E) → H^3(L) → H_2(E) → ...

Since E is a complex surface (real dim 4): H_5(E) = 0, H_4(E) = Z^k (k = number of connected components, but E is connected so H_4(E) = Z... wait, H_4(E) for a connected complex surface is Z if E is irreducible, or Z^k if E has k irreducible components. Actually, H_4 of a connected complex surface (real dim 4) is Z if the surface is irreducible, and Z^k if it has k irreducible components (since each component contributes a fundamental class).

Hmm, actually, for a reduced projective surface E with k irreducible components E_1, ..., E_k, H_4(E, Z) = Z^k (each component gives a fundamental class in H_4).

So the sequence becomes:
0 → H^1(E) → H^1(L) → Z^k → H^2(E) → H^2(L) → H_3(E) → ...

Now, the map Z^k → H^2(E) is the map that sends the i-th generator to the class [E_i] ∈ H^2(E) (the cohomology class dual to the fundamental class of E_i, which is the first Chern class of O_Y(E_i)|_E).

For a resolution of a singularity, the intersection matrix (E_i · E_j) is negative definite (by Grauert's theorem). This means the classes [E_i] ∈ H^2(E) are linearly independent over Q (since the intersection matrix is nondegenerate).

So the map Z^k → H^2(E) is injective (over Z, since the classes are linearly independent).

If the map Z^k → H^2(E) is injective, then from the exact sequence:
H^1(L) → Z^k → H^2(E)

the image of H^1(L) in Z^k is the kernel of Z^k → H^2(E), which is 0 (by injectivity). So H^1(L) → Z^k is the zero map, which means H^1(E) → H^1(L) is surjective.

But we also have H^1(E) → H^1(L) is injective (from the 0 on the left). So H^1(E) ≅ H^1(L).

Wait, that's interesting! So H^1(E, Z) ≅ H^1(L, Z) when the intersection matrix is negative definite (which it is for resolutions of singularities).

So R^1 π_* Z = 0 if and only if H^1(L, Z) = 0.

Now, H^1(L, Z) = Hom(π_1(L), Z) (the abelianization). This is 0 if and only if π_1(L) has no surjection onto Z, i.e., π_1(L)^{ab} is a torsion group, i.e., the first Betti number b_1(L) = 0.

So the question reduces to: is b_1(L) = 0 for the link of a 3-dimensional rational singularity?

Now, I need to determine whether b_1(L) = 0 for 3-dimensional rational singularities.

From the isomorphism H^1(E, Z) ≅ H^1(L, Z), we have b_1(E) = b_1(L). So the question is equivalent to: is b_1(E) = 0?

And b_1(E) is the first Betti number of the exceptional fiber.

Now, for a projective variety E (possibly singular), b_1(E) = dim_Q H^1(E, Q). And H^1(E, Q) = Hom(π_1(E), Q) (for reasonable spaces).

For the exceptional fiber of a resolution of a rational singularity, what can we say about π_1(E)?

Claim: For a rational singularity, π_1(E) is finite (and hence b_1(E) = 0).

This is what I need to verify. Let me think about whether this is true.

For surface rational singularities (dim 2), the exceptional fiber is a tree of P^1's, which is simply connected. So π_1(E) = 0, b_1(E) = 0. ✓

For 3-dimensional rational singularities, the exceptional fiber E is a surface (possibly singular, possibly reducible). Is π_1(E) always finite?

I think this is related to Kollár's theorem, but let me think about it more directly.

From the rational singularity condition, H^i(E, O_E) = 0 for i > 0 (by the theorem on formal functions). In particular, H^1(E, O_E) = 0.

Now, for a normal projective surface S, H^1(S, O_S) = 0 implies b_1(S) = 0 (by Hodge theory for normal surfaces: H^1(S, C) = H^1(S, O_S) ⊕ H^0(S, Ω^1_S) where Ω^1_S is the sheaf of reflexive differentials, and H^0(S, Ω^1_S) = H^1(S, O_S) = 0 by Serre duality... wait, this needs more care).

Actually, for a normal projective surface S, the Hodge-to-de Rham spectral sequence might not degenerate at E_1, but we can use the fact that for normal surfaces, H^1(S, C) = H^1(S, O_S) ⊕ H^0(S, ω_S) where ω_S is the dualizing sheaf (by Serre duality and the Hodge decomposition for normal varieties, using the fact that normal surfaces have rational singularities after resolution... no, that's circular).

Hmm, let me think about this differently. For a normal projective surface S with H^1(S, O_S) = 0:

By the exponential sequence 0 → Z → O_S → O_S^* → 0:
H^1(S, Z) → H^1(S, O_S) → H^1(S, O_S^*) → H^2(S, Z) → H^2(S, O_S)

H^1(S, Z) → 0, so the map H^1(S, Z) → H^1(S, O_S) is zero. But this doesn't mean H^1(S, Z) = 0; it just means the map to H^1(S, O_S) is zero.

The map H^1(S, Z) → H^1(S, O_S) is the map H^1(S, Z) → H^1(S, Z) ⊗ C → H^1(S, O_S) (the projection from H^1(S, C) to its (0,1) part). If H^1(S, O_S) = 0, this map is automatically zero, regardless of H^1(S, Z).

So H^1(S, O_S) = 0 does NOT imply H^1(S, Z) = 0 for normal surfaces. We need additional information.

But for smooth surfaces, H^1(S, O_S) = 0 does imply H^1(S, Z) = 0 (by Hodge decomposition: H^1(S, C) = H^{1,0} ⊕ H^{0,1} = H^0(Ω^1) ⊕ H^1(O) = 0).

For normal surfaces with rational singularities, the same holds: if S has rational singularities and H^1(S, O_S) = 0, then H^1(S, Z) = 0 (because for varieties with rational singularities, the Hodge decomposition holds: H^1(S, C) = H^1(S, O_S) ⊕ H^0(S, Ω^1_{[S]}) where Ω^1_{[S]} is the sheaf of reflexive differentials, and H^0(S, Ω^1_{[S]}) = H^1(S, O_S) by Serre duality... hmm, I need to
