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
  <problem_id>polymath_04639</problem_id>
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

For \( A, B, C, K > 0 \), find the maximum value of \( K \) such that the inequality

\[
\frac{A}{A^2 + KBC} + \frac{B}{B^2 + KAC} + \frac{C}{C^2 + KAB} \leq \frac{1}{K+1} \left( \frac{1}{A} + \frac{1}{B} + \frac{1}{C} \right)
\]

holds.

## Standard Solution

To find the maximum value of \( K \) such that the inequality

\[
\frac{A}{A^2 + KBC} + \frac{B}{B^2 + KAC} + \frac{C}{C^2 + KAB} \leq \frac{1}{K+1} \left( \frac{1}{A} + \frac{1}{B} + \frac{1}{C} \right)
\]

holds for all positive \( A, B, C \), we proceed as follows:

1. **Symmetric Case Analysis**:
   Let \( A = B = C = t \). Substituting into the inequality, we get:

   \[
   \frac{t}{t^2 + Kt^2} + \frac{t}{t^2 + Kt^2} + \frac{t}{t^2 + Kt^2} = \frac{3}{t(1 + K)}
   \]

   and

   \[
   \frac{1}{K+1} \left( \frac{1}{t} + \frac{1}{t} + \frac{1}{t} \right) = \frac{3}{t(K+1)}
   \]

   Both sides are equal, indicating that the inequality holds as an equality in this symmetric case for any \( K \).

2. **Critical Case Analysis**:
   To find the maximum \( K \) where the inequality holds for all \( A, B, C \), we need to consider the critical case where the inequality might fail. Consider the case where \( B = C = 1 \) and \( A \) is a variable.

   The inequality becomes:

   \[
   \frac{A}{A^2 + K} + \frac{1}{1 + KA} + \frac{1}{1 + KA} \leq \frac{1}{K+1} \left( \frac{1}{A} + 1 + 1 \right)
   \]

   Simplifying, we have:

   \[
   \frac{A}{A^2 + K} + \frac{2}{1 + KA} \leq \frac{1}{K+1} \left( \frac{1}{A} + 2 \right)
   \]

3. **Formulating the Critical Equation**:
   To find the maximum \( K \), we set the left-hand side equal to the right-hand side:

   \[
   \frac{A}{A^2 + K} + \frac{2}{1 + KA} = \frac{1}{K+1} \left( \frac{1}{A} + 2 \right)
   \]

   Multiply both sides by \( (K+1)(A^2 + K)(1 + KA) \):

   \[
   (K+1) \left[ A(1 + KA) + 2(A^2 + K) \right] = (1 + 2A)(A^2 + K)(1 + KA)
   \]

4. **Simplifying the Equation**:
   Expand and simplify both sides:

   \[
   (K+1) \left[ A + K A^2 + 2A^2 + 2K \right] = (1 + 2A)(A^2 + K + K A^3 + K^2 A)
   \]

   \[
   (K+1)(A + 2A^2 + K A^2 + 2K) = (1 + 2A)(A^2 + K + K A^3 + K^2 A)
   \]

   \[
   (K+1)(A + (K+2)A^2 + 2K) = (1 + 2A)(A^2 + K + K A^3 + K^2 A)
   \]

5. **Finding the Minimal \( K \)**:
   To find the minimal \( K \) where the inequality fails, we need to find the critical points. We set \( A = 1 \):

   \[
   \frac{1}{1 + K} + \frac{2}{1 + K} = \frac{1}{K+1} \left( 1 + 2 \right)
   \]

   Simplifying, we get:

   \[
   \frac{3}{1 + K} = \frac{3}{K+1}
   \]

   This equation holds for any \( K \). To find the critical \( K \), we need to solve for \( K \) in terms of \( A \):

   \[
   K = 2A + 2 + \frac{1}{A}
   \]

6. **Minimizing \( K \)**:
   To find the minimal \( K \), we take the derivative of \( K = 2A + 2 + \frac{1}{A} \) with respect to \( A \):

   \[
   \frac{dK}{dA} = 2 - \frac{1}{A^2}
   \]

   Set the derivative to zero:

   \[
   2 - \frac{1}{A^2} = 0 \implies A^2 = \frac{1}{2} \implies A = \frac{1}{\sqrt{2}}
   \]

   Substitute \( A = \frac{1}{\sqrt{2}} \) back into the expression for \( K \):

   \[
   K = 2 \left( \frac{1}{\sqrt{2}} \right) + 2 + \frac{1}{\frac{1}{\sqrt{2}}} = \sqrt{2} + 2 + \sqrt{2} = 2 + 2\sqrt{2}
   \]

Therefore, the maximum value of \( K \) is:

\[
\boxed{2 + 2\sqrt{2}}
\]

## AI's Thinking (Attempted Solution Process)

The problem asks for the maximum value of $K$ such that the inequality holds for all $A, B, C > 0$.

Let me first check for answer leaks. The problem text doesn't contain any leaked answers or solution sketches. Good.

Now let me solve the problem.

We need to find the maximum $K > 0$ such that for all $A, B, C > 0$:
$$\frac{A}{A^2 + KBC} + \frac{B}{B^2 + KAC} + \frac{C}{C^2 + KAB} \leq \frac{1}{K+1}\left(\frac{1}{A} + \frac{1}{B} + \frac{1}{C}\right)$$

Let me first check the equality case $A = B = C$. Then LHS = $\frac{3A}{A^2 + KA^2} = \frac{3}{A(1+K)}$ and RHS = $\frac{1}{K+1} \cdot \frac{3}{A} = \frac{3}{A(K+1)}$. So equality holds when $A = B = C$ for any $K$. Good, this is consistent.

Now let me think about the structure. Let me substitute $x = 1/A$, $y = 1/B$, $z = 1/C$ or try homogeneity.

The inequality is homogeneous of degree $-1$ on both sides (LHS: each term $\frac{A}{A^2 + KBC}$ has degree $-1$; RHS: $\frac{1}{K+1}(\frac{1}{A}+\frac{1}{B}+\frac{1}{C})$ has degree $-1$). So WLOG we can normalize, e.g., $ABC = 1$ or $A + B + C = 3$ or something.

Let me try $C \to 0$ (or $C \to \infty$). Actually let me think about boundary cases to find the constraint on $K$.

Let me try $A = B = 1$, $C = t$ and see what happens as $t \to 0^+$ and $t \to \infty$.

LHS = $\frac{1}{1 + Kt} + \frac{1}{1 + Kt} + \frac{t}{t^2 + K} = \frac{2}{1+Kt} + \frac{t}{t^2 + K}$

RHS = $\frac{1}{K+1}(1 + 1 + \frac{1}{t}) = \frac{1}{K+1}(2 + \frac{1}{t})$

As $t \to 0^+$: LHS $\to 2 + 0 = 2$, RHS $\to \infty$. So RHS dominates, no constraint from here.

As $t \to \infty$: LHS $\to 0 + \frac{1}{t} \to 0$, RHS $\to \frac{2}{K+1}$. So LHS $\to 0 < $ RHS. No constraint.

Let me try $A = 1, B = 1, C = t$ more carefully and find the maximum of LHS/RHS.

Actually, let me think about this differently. Let me try $A = 1, B = t, C = t$ with $t \to 0$ or $t \to \infty$.

LHS = $\frac{1}{1 + Kt^2} + \frac{t}{t^2 + Kt} + \frac{t}{t^2 + Kt} = \frac{1}{1+Kt^2} + \frac{2t}{t^2 + Kt} = \frac{1}{1+Kt^2} + \frac{2}{t+K}$

RHS = $\frac{1}{K+1}(1 + \frac{2}{t})$

As $t \to 0^+$: LHS $\to 1 + \frac{2}{K}$, RHS $\to \infty$. OK.

As $t \to \infty$: LHS $\to 0 + 0 = 0$, RHS $\to \frac{1}{K+1}$. OK.

Hmm, let me try to find the critical case. Let me set $A = 1, B = 1, C = t$ and compute the ratio $f(t) = \text{LHS}/\text{RHS}$ and find its maximum.

$f(t) = \frac{\frac{2}{1+Kt} + \frac{t}{t^2+K}}{\frac{1}{K+1}(2 + \frac{1}{t})}$

At $t = 1$: $f(1) = \frac{\frac{2}{1+K} + \frac{1}{1+K}}{\frac{3}{K+1}} = \frac{\frac{3}{1+K}}{\frac{3}{K+1}} = 1$. Good.

Let me compute $f'(1) = 0$ should hold by symmetry (since $t=1$ is the symmetric point). Let me verify and then look at the second derivative condition.

Actually, the maximum of $K$ is determined by the condition that $t = 1$ is a local maximum of $f(t)$ (or at least that $f(t) \leq 1$ everywhere). Since $f(1) = 1$, we need $t = 1$ to be a local max, so $f''(1) \leq 0$.

Let me compute. Let $g(t) = \text{LHS}$ and $h(t) = \text{RHS}$, so $f = g/h$.

$g(t) = \frac{2}{1+Kt} + \frac{t}{t^2+K}$

$g'(t) = \frac{-2K}{(1+Kt)^2} + \frac{(t^2+K) - t \cdot 2t}{(t^2+K)^2} = \frac{-2K}{(1+Kt)^2} + \frac{K - t^2}{(t^2+K)^2}$

At $t=1$: $g'(1) = \frac{-2K}{(1+K)^2} + \frac{K-1}{(1+K)^2} = \frac{-2K + K - 1}{(1+K)^2} = \frac{-(K+1)}{(1+K)^2} = \frac{-1}{1+K}$

$h(t) = \frac{1}{K+1}(2 + \frac{1}{t})$, $h'(t) = \frac{1}{K+1} \cdot \frac{-1}{t^2}$, $h'(1) = \frac{-1}{K+1}$

$f'(1) = \frac{g'(1)h(1) - g(1)h'(1)}{h(1)^2}$

$g(1) = \frac{3}{1+K}$, $h(1) = \frac{3}{K+1}$

$f'(1) = \frac{\frac{-1}{1+K} \cdot \frac{3}{K+1} - \frac{3}{1+K} \cdot \frac{-1}{K+1}}{(\frac{3}{K+1})^2} = \frac{0}{...} = 0$. Good, as expected.

Now $f''(1)$. We need $f''(1) \leq 0$.

$f'' = \frac{(g''h - gh'')h^2 - (g'h - gh') \cdot 2hh'}{h^4}$

At $t=1$, $g'h - gh' = 0$ (since $f'(1) = 0$), so $f''(1) = \frac{g''(1)h(1) - g(1)h''(1)}{h(1)^2}$.

$g''(t) = \frac{4K^2}{(1+Kt)^3} + \frac{d}{dt}\frac{K-t^2}{(t^2+K)^2}$

$\frac{d}{dt}\frac{K-t^2}{(t^2+K)^2} = \frac{-2t(t^2+K)^2 - (K-t^2) \cdot 2(t^2+K) \cdot 2t}{(t^2+K)^4} = \frac{-2t(t^2+K) - 4t(K-t^2)}{(t^2+K)^3} = \frac{-2t[(t^2+K) + 2(K-t^2)]}{(t^2+K)^3} = \frac{-2t[t^2 + K + 2K - 2t^2]}{(t^2+K)^3} = \frac{-2t[3K - t^2]}{(t^2+K)^3}$

At $t=1$: $\frac{-2(3K-1)}{(1+K)^3}$

$g''(1) = \frac{4K^2}{(1+K)^3} + \frac{-2(3K-1)}{(1+K)^3} = \frac{4K^2 - 6K + 2}{(1+K)^3} = \frac{2(2K^2 - 3K + 1)}{(1+K)^3} = \frac{2(2K-1)(K-1)}{(1+K)^3}$

$h''(t) = \frac{1}{K+1} \cdot \frac{2}{t^3}$, $h''(1) = \frac{2}{K+1}$

$f''(1) = \frac{g''(1)h(1) - g(1)h''(1)}{h(1)^2}$

Numerator: $\frac{2(2K-1)(K-1)}{(1+K)^3} \cdot \frac{3}{K+1} - \frac{3}{1+K} \cdot \frac{2}{K+1}$

$= \frac{6(2K-1)(K-1)}{(1+K)^4} - \frac{6}{(1+K)^2}$

$= \frac{6(2K-1)(K-1) - 6(1+K)^2}{(1+K)^4}$

$= \frac{6[(2K-1)(K-1) - (1+K)^2]}{(1+K)^4}$

$(2K-1)(K-1) = 2K^2 - 3K + 1$

$(1+K)^2 = K^2 + 2K + 1$

$(2K-1)(K-1) - (1+K)^2 = 2K^2 - 3K + 1 - K^2 - 2K - 1 = K^2 - 5K = K(K-5)$

So $f''(1) = \frac{6K(K-5)}{(1+K)^4} \cdot \frac{1}{h(1)^2}$... wait let me redo.

$f''(1) = \frac{\text{numerator}}{h(1)^2} = \frac{\frac{6K(K-5)}{(1+K)^4}}{\frac{9}{(K+1)^2}} = \frac{6K(K-5)}{(1+K)^4} \cdot \frac{(K+1)^2}{9} = \frac{6K(K-5)}{9(1+K)^2} = \frac{2K(K-5)}{3(1+K)^2}$

For $f''(1) \leq 0$, we need $K(K-5) \leq 0$, i.e., $K \leq 5$ (since $K > 0$).

So the critical value is $K = 5$. At $K = 5$, $f''(1) = 0$, and we need to check higher order terms or verify the inequality holds.

So the answer should be $K = 5$. But I need to verify that the inequality actually holds for $K = 5$ for all $A, B, C > 0$, not just in this one-parameter family.

Let me first verify with the one-parameter family $A = B = 1, C = t$ at $K = 5$.

$g(t) = \frac{2}{1+5t} + \frac{t}{t^2+5}$, $h(t) = \frac{1}{6}(2 + \frac{1}{t})$

We need $g(t) \leq h(t)$ for all $t > 0$.

$\frac{2}{1+5t} + \frac{t}{t^2+5} \leq \frac{1}{6}(2 + \frac{1}{t})$

Let me check $t = 1$: LHS = $\frac{2}{6} + \frac{1}{6} = \frac{1}{2}$, RHS = $\frac{1}{6} \cdot 3 = \frac{1}{2}$. Equality.

Let me check $t = 2$: LHS = $\frac{2}{11} + \frac{2}{9} = \frac{18 + 22}{99} = \frac{40}{99} \approx 0.4040$. RHS = $\frac{1}{6}(2 + 0.5) = \frac{2.5}{6} \approx 0.4167$. OK, LHS < RHS.

Let me check $t = 0.5$: LHS = $\frac{2}{3.5} + \frac{0.5}{5.25} = \frac{4}{7} + \frac{2}{21} = \frac{12+2}{21} = \frac{14}{21} = \frac{2}{3} \approx 0.6667$. RHS = $\frac{1}{6}(2+2) = \frac{4}{6} = \frac{2}{3}$. Equality again!

Interesting, so at $t = 0.5$ (i.e., $C = 0.5, A = B = 1$) we also get equality when $K = 5$. Let me check $t = 0.5$ more carefully.

Actually $t = 1/2$: $A = B = 1, C = 1/2$. By the substitution $A = B = 1, C = t$, the case $t = 1/2$ corresponds to $C$ being half of $A, B$. And we got equality. This suggests there's a family of equality cases.

Let me check: is there equality when $(A, B, C)$ is a permutation of $(1, 1, t)$ for specific $t$ values? At $K = 5$, we have equality at $t = 1$ and $t = 1/2$. By the symmetry $t \leftrightarrow 1/t$ (which corresponds to swapping the role of $C$ with $A$ or $B$), $t = 2$ should also give equality. But I computed $t = 2$ and got LHS < RHS. Let me recheck.

$t = 2$: $A = B = 1, C = 2$. LHS = $\frac{1}{1+5\cdot1\cdot2} + \frac{1}{1+5\cdot1\cdot2} + \frac{2}{4+5\cdot1\cdot1} = \frac{2}{11} + \frac{2}{9}$. Wait, let me recompute the third term. $C = 2$, so $\frac{C}{C^2 + KAB} = \frac{2}{4 + 5} = \frac{2}{9}$. And the first two terms: $\frac{A}{A^2 + KBC} = \frac{1}{1 + 5 \cdot 1 \cdot 2} = \frac{1}{11}$, same for $B$. So LHS = $\frac{2}{11} + \frac{2}{9} = \frac{18 + 22}{99} = \frac{40}{99}$.

RHS = $\frac{1}{6}(1 + 1 + \frac{1}{2}) = \frac{1}{6} \cdot \frac{5}{2} = \frac{5}{12}$.

$\frac{40}{99} \approx 0.4040$, $\frac{5}{12} \approx 0.4167$. So LHS < RHS. Not equality.

But $t = 1/2$ gave equality. Let me recheck $t = 1/2$.

$A = B = 1, C = 1/2$. LHS = $\frac{1}{1 + 5 \cdot 1 \cdot 1/2} + \frac{1}{1 + 5 \cdot 1 \cdot 1/2} + \frac{1/2}{1/4 + 5 \cdot 1 \cdot 1} = \frac{2}{1 + 5/2} + \frac{1/2}{1/4 + 5} = \frac{2}{7/2} + \frac{1/2}{21/4} = \frac{4}{7} + \frac{2}{21} = \frac{12 + 2}{21} = \frac{14}{21} = \frac{2}{3}$.

RHS = $\frac{1}{6}(1 + 1 + 2) = \frac{4}{6} = \frac{2}{3}$. Equality! Confirmed.

So at $K = 5$, equality holds at $(1,1,1)$ and $(1,1,1/2)$ (and permutations). This is characteristic of the sharp case.

Now I need to prove the inequality holds for $K = 5$ for all $A, B, C > 0$.

Let me think about this more carefully. The inequality at $K = 5$:

$$\frac{A}{A^2 + 5BC} + \frac{B}{B^2 + 5AC} + \frac{C}{C^2 + 5AB} \leq \frac{1}{6}\left(\frac{1}{A} + \frac{1}{B} + \frac{1}{C}\right)$$

By homogeneity, WLOG $ABC = 1$ (or some other normalization). Actually, let me use the substitution $a = 1/A, b = 1/B, c = 1/C$.

Then $\frac{A}{A^2 + 5BC} = \frac{1/a}{1/a^2 + 5/(bc)} = \frac{1/a}{(bc + 5a^2)/(a^2 bc)} = \frac{a \cdot bc}{bc + 5a^2} = \frac{abc \cdot a}{bc + 5a^2}$... hmm, this is getting complicated. Let me try a different approach.

Actually, let me try the substitution where we set $x = A, y = B, z = C$ and use SOS or Schur-like methods.

Alternatively, let me try to prove it by clearing denominators. The inequality is:

$$\sum_{\text{cyc}} \frac{A}{A^2 + 5BC} \leq \frac{1}{6}\sum_{\text{cyc}} \frac{1}{A}$$

This is equivalent to:

$$\sum_{\text{cyc}} \left(\frac{1}{6A} - \frac{A}{A^2 + 5BC}\right) \geq 0$$

$$\sum_{\text{cyc}} \frac{A^2 + 5BC - 6A^2}{6A(A^2 + 5BC)} \geq 0$$

$$\sum_{\text{cyc}} \frac{5BC - 5A^2}{6A(A^2 + 5BC)} \geq 0$$

$$\sum_{\text{cyc}} \frac{BC - A^2}{A(A^2 + 5BC)} \geq 0$$

So we need to prove:

$$\sum_{\text{cyc}} \frac{BC - A^2}{A(A^2 + 5BC)} \geq 0$$

Let me denote $S = \sum_{\text{cyc}} \frac{BC - A^2}{A(A^2 + 5BC)}$.

Note that $\sum_{\text{cyc}} (BC - A^2) = AB + BC + CA - A^2 - B^2 - C^2$, which can be positive or negative. So this isn't a straightforward Schur-type inequality.

Let me try WLOG $A \geq B \geq C$ or use the SOS method.

Actually, let me think about this using the substitution $A = e^x, B = e^y, C = e^z$ or try specific techniques.

Let me try another approach. Let me use the Schur inequality or Muirhead-type reasoning.

Actually, let me try to verify the inequality computationally for $K = 5$ by testing many random points, and also check that $K > 5$ fails.

For $K > 5$, say $K = 5 + \epsilon$, the second derivative $f''(1) > 0$ (for the one-parameter family), so $t = 1$ becomes a local minimum of $f(t)$, meaning $f(t) > 1$ for $t$ near 1, so the inequality fails. This confirms $K \leq 5$ is necessary.

Now I need to prove $K = 5$ works. Let me think about the proof.

We need: $\sum_{\text{cyc}} \frac{BC - A^2}{A(A^2 + 5BC)} \geq 0$.

Let me try the substitution $a = A^2, b = B^2, c = C^2$... no, that doesn't simplify nicely because of $BC$.

Let me try WLOG $A \geq B \geq C > 0$ and use the SOS/Schur approach.

Actually, let me try a different normalization. Since the inequality is homogeneous of degree $-1$, let me set $A + B + C = 3$ or $ABC = 1$.

With $ABC = 1$: $BC = 1/A$, so $A^2 + 5BC = A^2 + 5/A = (A^3 + 5)/A$.

Then $\frac{A}{A^2 + 5BC} = \frac{A}{(A^3+5)/A} = \frac{A^2}{A^3 + 5}$.

And $\frac{1}{A} = \frac{1}{A}$.

So the inequality becomes:

$$\sum_{\text{cyc}} \frac{A^2}{A^3 + 5} \leq \frac{1}{6}\sum_{\text{cyc}} \frac{1}{A}$$

with $ABC = 1$.

Hmm, this is cleaner. We need:

$$\sum_{\text{cyc}} \left(\frac{1}{6A} - \frac{A^2}{A^3+5}\right) \geq 0$$

$$\sum_{\text{cyc}} \frac{A^3 + 5 - 6A^3}{6A(A^3+5)} \geq 0$$

$$\sum_{\text{cyc}} \frac{5 - 5A^3}{6A(A^3+5)} \geq 0$$

$$\sum_{\text{cyc}} \frac{1 - A^3}{A(A^3+5)} \geq 0$$

with $ABC = 1$.

So we need to prove: if $ABC = 1$, then $\sum_{\text{cyc}} \frac{1 - A^3}{A(A^3+5)} \geq 0$.

Let $f(x) = \frac{1 - x^3}{x(x^3+5)} = \frac{1-x^3}{x^4 + 5x}$.

Note $f(1) = 0$. For $x > 1$, $f(x) < 0$; for $x < 1$, $f(x) > 0$.

With $ABC = 1$, we need $f(A) + f(B) + f(C) \geq 0$.

This is a "Schur-like" inequality. The function $f$ changes sign at $x = 1$, and we need the sum to be non-negative when $ABC = 1$.

Let me think about this using the tangent line trick or convexity/concavity arguments.

Actually, let me try the "SOS" (sum of squares) approach or the "pqr" method.

Let me try a different approach. Let me use the substitution $A = x/y, B = y/z, C = z/x$ (so $ABC = 1$). Then:

$f(A) = f(x/y) = \frac{1 - x^3/y^3}{(x/y)(x^3/y^3 + 5)} = \frac{(y^3 - x^3)/y^3}{(x/y) \cdot (x^3 + 5y^3)/y^3} = \frac{y^3 - x^3}{y^3} \cdot \frac{y^4}{x(x^3 + 5y^3)} = \frac{y(y^3 - x^3)}{x(x^3 + 5y^3)}$

This doesn't simplify things much.

Let me try yet another approach. Let me consider the function $g(t) = \frac{1-t^3}{t(t^3+5)}$ and study its properties.

$g(t) = \frac{1-t^3}{t^4+5t} = \frac{-(t^3-1)}{t(t^3+5)} = \frac{-(t-1)(t^2+t+1)}{t(t^3+5)}$

For the tangent line trick: if $ABC = 1$, we can write $A = e^u, B = e^v, C = e^w$ with $u + v + w = 0$. Then we need $g(e^u) + g(e^v) + g(e^w) \geq 0$ when $u + v + w = 0$.

If $h(u) = g(e^u)$ is convex, then by Jensen's, $h(u) + h(v) + h(w) \geq 3h(0) = 0$. But $h$ is not globally convex (it changes sign). However, maybe we can use a modified approach.

Actually, let me check: is $h(u) = g(e^u) = \frac{1 - e^{3u}}{e^u(e^{3u}+5)} = \frac{1-e^{3u}}{e^{4u}+5e^u}$ convex?

$h(0) = 0$, $h'(0) = ?$. Let me compute.

$h(u) = \frac{1-e^{3u}}{e^{4u}+5e^u}$

At $u = 0$: $h(0) = 0$.

$h'(u) = \frac{-3e^{3u}(e^{4u}+5e^u) - (1-e^{3u})(4e^{4u}+5e^u)}{(e^{4u}+5e^u)^2}$

At $u = 0$: $h'(0) = \frac{-3 \cdot 6 - 0}{36} = \frac{-18}{36} = -\frac{1}{2}$.

So $h'(0) = -1/2 \neq 0$. This means $h$ is not symmetric around 0, so simple convexity won't give us $h(u)+h(v)+h(w) \geq 0$.

Hmm, but we need $h(u) + h(v) + h(w) \geq 0$ with $u+v+w = 0$. If $h$ were convex, Jensen gives $\geq 3h(0) = 0$. But $h$ might not be convex.

Let me check $h''(0)$.

Actually, this is getting complicated. Let me try a more computational approach.

Let me try to use the SOS method after clearing denominators. Going back to the original form (without the $ABC=1$ normalization):

We need $\sum_{\text{cyc}} \frac{BC - A^2}{A(A^2+5BC)} \geq 0$.

Let me denote the common denominator approach. Let $D = A(A^2+5BC) \cdot B(B^2+5AC) \cdot C(C^2+5AB)$. Then we need:

$\sum_{\text{cyc}} (BC - A^2) \cdot B(B^2+5AC) \cdot C(C^2+5AB) \geq 0$

This is a polynomial inequality (after clearing denominators, since $D > 0$). Let me expand.

Actually this will be very messy. Let me try a different strategy.

Let me try the "mixing variables" method (also known as the method of Lagrange multipliers or the SOS approach for symmetric inequalities).

Actually, let me try to use the Schur inequality. The Schur inequality states that for $t \geq 0$:

$$A^t(A-B)(A-C) + B^t(B-A)(B-C) + C^t(C-A)(C-B) \geq 0$$

For $t = 1$: $A(A-B)(A-C) + B(B-A)(B-C) + C(C-A)(C-B) \geq 0$, which expands to $A^3 + B^3 + C^3 + ABC \geq AB(A+B) + BC(B+C) + CA(C+A)$, i.e., $A^3+B^3+C^3+ABC \geq (A+B+C)(AB+BC+CA) - 2ABC$... actually let me just recall: Schur for $t=1$ gives $A^3+B^3+C^3+ABC \geq (A+B+C)(AB+BC+CA)/... $ hmm, let me just expand.

$A(A-B)(A-C) = A(A^2 - AC - AB + BC) = A^3 - A^2C - A^2B + ABC$

Sum cyclic: $\sum A^3 - \sum A^2B - \sum A^2C + 3ABC = \sum A^3 - \sum_{sym} A^2B + 3ABC$

where $\sum_{sym} A^2B = A^2B + A^2C + B^2A + B^2C + C^2A + C^2B$.

So Schur $t=1$: $\sum A^3 + 3ABC \geq \sum_{sym} A^2B$, which is $\sum A^3 + 3ABC \geq (A+B+C)(AB+BC+CA) - 3ABC$... no.

$(A+B+C)(AB+BC+CA) = A^2B + A^2C + AB^2 + B^2C + AC^2 + BC^2 + 3ABC = \sum_{sym} A^2B + 3ABC$.

So Schur $t=1$: $\sum A^3 + 3ABC \geq \sum_{sym} A^2B = (A+B+C)(AB+BC+CA) - 3ABC$.

Thus $\sum A^3 + 6ABC \geq (A+B+C)(AB+BC+CA)$.

OK, I'm not sure Schur directly applies here. Let me think differently.

Let me go back to the normalized form: $ABC = 1$, prove $\sum \frac{1-A^3}{A(A^3+5)} \geq 0$.

Let $u = A^3, v = B^3, w = C^3$, so $uvw = 1$ and $A = u^{1/3}$.

$\frac{1-A^3}{A(A^3+5)} = \frac{1-u}{u^{1/3}(u+5)}$

We need $\sum \frac{1-u}{u^{1/3}(u+5)} \geq 0$ with $uvw = 1$.

Hmm, still complicated. Let me try yet another substitution. Let $p = A^3, q = B^3, r = C^3$ with $pqr = 1$.

$\sum \frac{1-p}{p^{1/3}(p+5)} \geq 0$

Let me try $p = e^s, q = e^t, r = e^{-s-t}$ and define $\phi(s) = \frac{1-e^s}{e^{s/3}(e^s+5)} = \frac{1-e^s}{e^{4s/3}+5e^{s/3}}$.

We need $\phi(s) + \phi(t) + \phi(-s-t) \geq 0$.

This is hard to handle analytically. Let me try a completely different approach.

Let me try to prove the inequality by the SOS method after substitution. Going back to:

$$\sum_{\text{cyc}} \frac{BC - A^2}{A(A^2+5BC)} \geq 0$$

Let me try the substitution $A = x^2, B = y^2, C = z^2$ (all positive). Then $BC = y^2z^2$ and:

$$\sum_{\text{cyc}} \frac{y^2z^2 - x^4}{x^2(x^4 + 5y^2z^2)} \geq 0$$

Not obviously simpler.

Let me try a tangent line approach. We want to show $\sum \frac{1-A^3}{A(A^3+5)} \geq 0$ with $ABC = 1$.

Idea: find a linear function $\ell(x) = \alpha + \beta \ln x$ such that $\frac{1-x^3}{x(x^3+5)} \geq \alpha + \beta \ln x$ for all $x > 0$, and $\alpha + \beta \ln A + \alpha + \beta \ln B + \alpha + \beta \ln C = 3\alpha + \beta \ln(ABC) = 3\alpha \geq 0$ when $ABC = 1$.

So we need $3\alpha \geq 0$, i.e., $\alpha \geq 0$, and $\frac{1-x^3}{x(x^3+5)} \geq \alpha + \beta \ln x$ for all $x > 0$.

At $x = 1$: LHS = 0, so $\alpha + 0 \leq 0$, meaning $\alpha \leq 0$. Combined with $\alpha \geq 0$, we get $\alpha = 0$.

So we need $\frac{1-x^3}{x(x^3+5)} \geq \beta \ln x$ for all $x > 0$, and then $\sum \beta \ln A = \beta \ln(ABC) = 0 \geq 0$. But that gives $0 \geq 0$, which is trivially true but doesn't help because we need the sum of LHS $\geq$ sum of $\beta \ln x = 0$.

Wait, if $\frac{1-x^3}{x(x^3+5)} \geq \beta \ln x$ for all $x$, then $\sum \frac{1-A^3}{A(A^3+5)} \geq \beta \sum \ln A = \beta \ln(ABC) = 0$. So we just need to find $\beta$ such that $g(x) := \frac{1-x^3}{x(x^3+5)} \geq \beta \ln x$ for all $x > 0$.

For $x > 1$: $g(x) < 0$ and $\ln x > 0$, so we need $\beta \leq g(x)/\ln x$ (which is negative).
For $x < 1$: $g(x) > 0$ and $\ln x < 0$, so we need $\beta \geq g(x)/\ln x$ (which is negative).

So we need $\sup_{x<1} \frac{g(x)}{\ln x} \leq \beta \leq \inf_{x>1} \frac{g(x)}{\ln x}$.

Let me compute $\lim_{x \to 1} \frac{g(x)}{\ln x}$. By L'Hôpital or Taylor:

$g(x) = \frac{1-x^3}{x(x^3+5)}$, $g(1) = 0$, $g'(x) = \frac{-3x^2 \cdot x(x^3+5) - (1-x^3)(x^3+5+3x^3)}{x^2(x^3+5)^2}$... let me just compute $g'(1)$.

$g(x) = \frac{1-x^3}{x^4+5x}$

$g'(x) = \frac{-3x^2(x^4+5x) - (1-x^3)(4x^3+5)}{(x^4+5x)^2}$

At $x=1$: $g'(1) = \frac{-3 \cdot 6 - 0}{36} = \frac{-18}{36} = -\frac{1}{2}$.

$\frac{d}{dx}\ln x\big|_{x=1} = 1$.

So $\lim_{x\to 1} \frac{g(x)}{\ln x} = \frac{g'(1)}{1} = -\frac{1}{2}$.

So we need $\beta = -1/2$ (if the ratio is constant, which it won't be, but let's check if $\beta = -1/2$ works).

We need $g(x) \geq -\frac{1}{2} \ln x$ for all $x > 0$, i.e., $\frac{1-x^3}{x(x^3+5)} + \frac{1}{2}\ln x \geq 0$ for all $x > 0$.

Let me define $\Phi(x) = \frac{1-x^3}{x(x^3+5)} + \frac{1}{2}\ln x$.

$\Phi(1) = 0 + 0 = 0$.

$\Phi'(x) = g'(x) + \frac{1}{2x}$

$g'(x) = \frac{-3x^2(x^4+5x) - (1-x^3)(4x^3+5)}{(x^4+5x)^2}$

$= \frac{-3x^6 - 15x^3 - 4x^3 - 5 + 4x^6 + 5x^3}{(x^4+5x)^2}$

$= \frac{x^6 - 14x^3 - 5}{(x^4+5x)^2}$

Wait let me redo this more carefully.

Numerator of $g'(x)$: $-3x^2(x^4+5x) - (1-x^3)(4x^3+5)$

$= -3x^6 - 15x^3 - (4x^3 + 5 - 4x^6 - 5x^3)$

$= -3x^6 - 15x^3 - 4x^3 - 5 + 4x^6 + 5x^3$

$= x^6 - 14x^3 - 5$

So $g'(x) = \frac{x^6 - 14x^3 - 5}{(x^4+5x)^2}$.

$\Phi'(x) = \frac{x^6 - 14x^3 - 5}{(x^4+5x)^2} + \frac{1}{2x}$

$= \frac{x^6 - 14x^3 - 5}{x^2(x^3+5)^2} + \frac{1}{2x}$

$= \frac{2(x^6 - 14x^3 - 5) + x(x^3+5)^2}{2x^2(x^3+5)^2}$

Numerator: $2x^6 - 28x^3 - 10 + x(x^6 + 10x^3 + 25) = 2x^6 - 28x^3 - 10 + x^7 + 10x^4 + 25x$

$= x^7 + 2x^6 + 10x^4 - 28x^3 + 25x - 10$

At $x = 1$: $1 + 2 + 10 - 28 + 25 - 10 = 0$. Good, $\Phi'(1) = 0$.

So $x = 1$ is a critical point of $\Phi$. We need $\Phi(x) \geq 0$ for all $x > 0$, with $\Phi(1) = 0$. So $x = 1$ should be a global minimum.

Let me check $\Phi$ at some other points.

$\Phi(2) = \frac{1-8}{2(8+5)} + \frac{1}{2}\ln 2 = \frac{-7}{26} + \frac{0.6931}{2} = -0.2692 + 0.3466 = 0.0774 > 0$. Good.

$\Phi(0.5) = \frac{1 - 0.125}{0.5(0.125+5)} + \frac{1}{2}\ln 0.5 = \frac{0.875}{2.5625} + \frac{-0.6931}{2} = 0.3415 - 0.3466 = -0.0051 < 0$.

Hmm, $\Phi(0.5) < 0$! So the tangent line trick with $\beta = -1/2$ doesn't work.

Let me recompute. $\Phi(0.5) = \frac{1 - 0.125}{0.5 \cdot 5.125} + 0.5 \cdot \ln(0.5) = \frac{0.875}{2.5625} + 0.5 \cdot (-0.6931) = 0.34146 - 0.34657 = -0.00512$.

So it's slightly negative. The tangent line trick with a single $\beta$ doesn't work here.

Let me try a different approach. Maybe I need a quadratic tangent: $g(x) \geq \alpha + \beta \ln x + \gamma (\ln x)^2$ where the sum of $(\ln x)^2$ terms can be bounded.

Actually, this is getting complicated. Let me try the "mixing variables" / "smoothing" approach instead.

The mixing variables method: show that the minimum of $\sum \frac{1-A^3}{A(A^3+5)}$ subject to $ABC = 1$ is achieved when two of the variables are equal, and then reduce to a one-variable problem.

Actually, let me think about this problem from a higher level. The key insight is:

1. $K = 5$ is the critical value (from the second derivative test).
2. We need to prove the inequality at $K = 5$.

For the proof at $K = 5$, let me try the approach of reducing to two variables equal.

**Mixing variables approach:**

We want to show $F(A,B,C) = \sum_{\text{cyc}} \frac{BC - A^2}{A(A^2+5BC)} \geq 0$ for all $A, B, C > 0$.

By homogeneity, WLOG set $C = 1$ (or $ABC = 1$, etc.). Let me set $C = 1$ and show $F(A,B,1) \geq 0$.

$F(A,B,1) = \frac{B - A^2}{A(A^2+5B)} + \frac{A - B^2}{B(B^2+5A)} + \frac{AB - 1}{1+5AB}$

Hmm, this is still a two-variable inequality. Let me try to show that for fixed $AB$ (or fixed $A+B$), the minimum is at $A = B$.

Actually, let me try a slightly different approach. Let me use the SOS method by finding a suitable representation.

Going back to the form with $ABC = 1$:

$$\sum_{\text{cyc}} \frac{1-A^3}{A(A^3+5)} \geq 0$$

Let me substitute $A = x/y, B = y/z, C = z/x$ (so $ABC = 1$). Then $A^3 = x^3/y^3$.

$\frac{1 - x^3/y^3}{(x/y)(x^3/y^3 + 5)} = \frac{(y^3-x^3)/y^3}{(x/y) \cdot (x^3+5y^3)/y^3} = \frac{y^3-x^3}{y^3} \cdot \frac{y^4}{x(x^3+5y^3)} = \frac{y(y^3-x^3)}{x(x^3+5y^3)}$

$= \frac{y(y-x)(y^2+xy+x^2)}{x(x^3+5y^3)}$

So we need:

$$\sum_{\text{cyc}} \frac{y(y-x)(y^2+xy+x^2)}{x(x^3+5y^3)} \geq 0$$

where the cyclic sum is over $(x,y,z) \to (y,z,x) \to (z,x,y)$.

This is still complex. Let me try a computational verification approach and then attempt a proof by SOS or other means.

Actually, let me try to prove the inequality directly using a clever algebraic manipulation.

Let me go back to the original inequality at $K = 5$:

$$\sum_{\text{cyc}} \frac{A}{A^2+5BC} \leq \frac{1}{6}\sum_{\text{cyc}} \frac{1}{A}$$

Cross-multiplying each term:

$$\sum_{\text{cyc}} \frac{BC - A^2}{A(A^2+5BC)} \geq 0$$

Let me try to write this as a sum of non-negative terms. 

Let me try the substitution $a = A^2, b = B^2, c = C^2$ and $p = BC, q = AC, r = AB$. Then $p^2 = bc, q^2 = ac, r^2 = ab$, and $pqr = ABC \cdot ABC = (ABC)^2$... this doesn't lead anywhere clean.

Let me try a direct SOS approach. We need:

$$S = \frac{BC-A^2}{A(A^2+5BC)} + \frac{AC-B^2}{B(B^2+5AC)} + \frac{AB-C^2}{C(C^2+5AB)} \geq 0$$

Let me denote $x = A^2, y = B^2, z = C^2, u = BC, v = AC, w = AB$. Note $u^2 = yz, v^2 = xz, w^2 = xy$, and $uvw = xyz$... wait, $u = BC = \sqrt{yz}$, etc. This substitution doesn't polynomialize things.

Let me try yet another approach. Let me use the Cauchy-Schwarz or other classical inequalities.

Actually, let me try to use the following approach: prove the inequality by showing it's equivalent to a known inequality or can be decomposed into simpler inequalities.

Let me try the approach of "tangent line trick with two tangent lines" - one for $x \geq 1$ and one for $x \leq 1$.

For $x \geq 1$: we want $g(x) \geq \beta_1 \ln x$ for some $\beta_1$.
For $x \leq 1$: we want $g(x) \geq \beta_2 \ln x$ for some $\beta_2$.

Then if two variables are $\geq 1$ and one is $\leq 1$ (or vice versa), we can combine.

But this requires case analysis and is complex. Let me try a more direct approach.

Actually, let me try the following: use the Schur-like approach. We have $ABC = 1$ and want $\sum g(A) \geq 0$ where $g(x) = \frac{1-x^3}{x(x^3+5)}$.

Note that $g(x) = \frac{1-x^3}{x(x^3+5)}$. Let me write $x^3 = t$, so $g = \frac{1-t}{t^{1/3}(t+5)}$.

With $t_1 t_2 t_3 = 1$ (since $A^3 B^3 C^3 = 1$), we need $\sum \frac{1-t_i}{t_i^{1/3}(t_i+5)} \geq 0$.

Hmm, let me try to use the fact that $\frac{1-t}{t+5}$ can be related to simpler expressions.

$\frac{1-t}{t+5} = \frac{6 - (t+5)}{t+5} = \frac{6}{t+5} - 1$

So $g(x) = \frac{1}{x} \cdot \left(\frac{6}{x^3+5} - 1\right) = \frac{6}{x(x^3+5)} - \frac{1}{x}$.

Then $\sum g(A) = 6\sum \frac{1}{A(A^3+5)} - \sum \frac{1}{A}$.

We need $6\sum \frac{1}{A(A^3+5)} \geq \sum \frac{1}{A}$, i.e., $\sum \frac{1}{A(A^3+5)} \geq \frac{1}{6}\sum \frac{1}{A}$.

But this is just the original inequality rewritten. Not helpful.

Let me try to use the Cauchy-Schwarz inequality in a clever way.

By Cauchy-Schwarz (Titu's lemma):

$\sum \frac{A}{A^2+5BC} = \sum \frac{A^2}{A(A^2+5BC)} \geq \frac{(A+B+C)^2}{\sum A(A^2+5BC)} = \frac{(A+B+C)^2}{A^3+B^3+C^3+5(AB \cdot A + BC \cdot B + CA \cdot C)/...}$

Hmm wait, $\sum A(A^2+5BC) = A^3+B^3+C^3 + 5(ABC + ABC + ABC) = A^3+B^3+C^3 + 15ABC$.

Wait no: $A \cdot 5BC = 5ABC$, $B \cdot 5AC = 5ABC$, $C \cdot 5AB = 5ABC$. So $\sum A(A^2+5BC) = A^3+B^3+C^3+15ABC$.

By Cauchy-Schwarz: $\sum \frac{A^2}{A(A^2+5BC)} \geq \frac{(A+B+C)^2}{A^3+B^3+C^3+15ABC}$.

But this gives a lower bound, and we need an upper bound. So Cauchy-Schwarz in this direction doesn't help.

Let me try a different approach. Let me try to use the SOS (Sum of Squares) method by clearing all denominators.

We need: $\sum_{\text{cyc}} (BC-A^2) \cdot B(B^2+5AC) \cdot C(C^2+5AB) \geq 0$.

Let me expand this. Let $P = (BC-A^2) \cdot B(B^2+5AC) \cdot C(C^2+5AB)$ and similarly for cyclic permutations.

$P_A = (BC - A^2) \cdot BC \cdot (B^2+5AC)(C^2+5AB)$

$= BC(BC-A^2)(B^2C^2 + 5AB^3 + 5AC^3 + 25A^2BC)$

This is getting very messy. Let me try a computational approach to verify and then find a proof.

Let me try specific substitutions to gain insight.

**Case $A = B$:** Let $A = B = 1, C = t$.

$S = \frac{t-1}{1+5t} + \frac{t-1}{1+5t} + \frac{1-t^2}{t(t^2+5)} = \frac{2(t-1)}{1+5t} + \frac{(1-t)(1+t)}{t(t^2+5)}$

$= (t-1)\left[\frac{2}{1+5t} - \frac{1+t}{t(t^2+5)}\right]$

$= (t-1) \cdot \frac{2t(t^2+5) - (1+t)(1+5t)}{t(t^2+5)(1+5t)}$

Numerator of bracket: $2t^3 + 10t - (1 + 5t + t + 5t^2) = 2t^3 + 10t - 1 - 6t - 5t^2 = 2t^3 - 5t^2 + 4t - 1$

$= (t-1)(2t^2 - 3t + 1) = (t-1)(2t-1)(t-1) = (t-1)^2(2t-1)$

So $S = \frac{(t-1)^2(2t-1)(t-1)}{t(t^2+5)(1+5t)} = \frac{(t-1)^3(2t-1)}{t(t^2+5)(1+5t)}$.

Wait, that doesn't look right. Let me recheck.

$S = (t-1) \cdot \frac{(t-1)^2(2t-1)}{t(t^2+5)(1+5t)} = \frac{(t-1)^3(2t-1)}{t(t^2+5)(1+5t)}$

For $t > 0$, the denominator is positive. So $\text{sign}(S) = \text{sign}((t-1)^3(2t-1))$.

$(t-1)^3 \geq 0$ when $t \geq 1$ and $< 0$ when $t < 1$.
$(2t-1) \geq 0$ when $t \geq 1/2$ and $< 0$ when $t < 1/2$.

So:
- $t \geq 1$: $(t-1)^3 \geq 0, (2t-1) > 0$, so $S \geq 0$. ✓
- $1/2 \leq t < 1$: $(t-1)^3 < 0, (2t-1) \geq 0$, so $S \leq 0$. ✗!

Wait, this means $S < 0$ for $1/2 \leq t < 1$? That would mean the inequality fails!

Let me recheck. At $t = 0.5$, $S = \frac{(0.5-1)^3(2 \cdot 0.5 - 1)}{0.5(0.25+5)(1+2.5)} = \frac{(-0.5)^3 \cdot 0}{...} = 0$. OK, $S = 0$ at $t = 0.5$.

At $t = 0.75$: $(t-1)^3 = (-0.25)^3 = -0.015625$, $(2t-1) = 0.5$. So $S = \frac{-0.015625 \cdot 0.5}{\text{positive}} < 0$.

This means the inequality FAILS at $K = 5$ for $A = B = 1, C = 0.75$?!

Wait, let me double-check by direct computation.

$A = B = 1, C = 0.75, K = 5$.

LHS = $\frac{1}{1 + 5 \cdot 0.75} + \frac{1}{1 + 5 \cdot 0.75} + \frac{0.75}{0.5625 + 5}$

$= \frac{2}{4.75} + \frac{0.75}{5.5625}$

$= 0.42105 + 0.13483 = 0.55589$

RHS = $\frac{1}{6}(1 + 1 + \frac{1}{0.75}) = \frac{1}{6}(2 + 1.3333) = \frac{3.3333}{6} = 0.55556$

So LHS $\approx 0.55589 > 0.55556 \approx$ RHS. The inequality FAILS!

This means $K = 5$ does NOT work! Let me recheck my second derivative computation.

Hmm, wait. Let me recheck the second derivative. We had $f(t) = g(t)/h(t)$ where $g(t) = \frac{2}{1+Kt} + \frac{t}{t^2+K}$ and $h(t) = \frac{1}{K+1}(2 + 1/t)$.

But wait, this was for $A = B = 1, C = t$. Let me recheck $g(t)$.

$g(t) = \frac{A}{A^2+KBC} + \frac{B}{B^2+KAC} + \frac{C}{C^2+KAB}$

With $A = B = 1, C = t$:

$g(t) = \frac{1}{1+Kt} + \frac{1}{1+Kt} + \frac{t}{t^2+K} = \frac{2}{1+Kt} + \frac{t}{t^2+K}$

$h(t) = \frac{1}{K+1}(1 + 1 + 1/t) = \frac{1}{K+1}(2 + 1/t)$

This is correct.

Now, the issue is that $f''(1) = 0$ at $K = 5$ doesn't mean $K = 5$ works - it means the second derivative test is inconclusive. We need to look at higher-order terms.

From the explicit computation with $A = B = 1, C = t$, we found:

$S = \frac{(t-1)^3(2t-1)}{t(t^2+5)(1+5t)}$ (at $K = 5$)

This is negative for $1/2 < t < 1$, which means the inequality fails. So $K = 5$ is too large.

Let me recheck: at $K = 5$, $t = 0.75$, LHS > RHS. So $K = 5$ doesn't work.

Let me redo the analysis. The condition from the second derivative was $K \leq 5$, but this is necessary, not sufficient. The actual answer might be smaller.

Let me redo the computation for general $K$ with $A = B = 1, C = t$.

$S_K(t) = \sum_{\text{cyc}} \frac{BC - A^2}{A(A^2+KBC)}$ with $A = B = 1, C = t$:

$= \frac{t - 1}{1 \cdot (1+Kt)} + \frac{t - 1}{1 \cdot (1+Kt)} + \frac{1 - t^2}{t(t^2+K)}$

$= \frac{2(t-1)}{1+Kt} + \frac{(1-t)(1+t)}{t(t^2+K)}$

$= (t-1)\left[\frac{2}{1+Kt} - \frac{1+t}{t(t^2+K)}\right]$

$= (t-1) \cdot \frac{2t(t^2+K) - (1+t)(1+Kt)}{t(t^2+K)(1+Kt)}$

Numerator: $2t^3 + 2Kt - (1 + Kt + t + Kt^2) = 2t^3 + 2Kt - 1 - Kt - t - Kt^2 = 2t^3 - Kt^2 + (K-1)t - 1$

So $S_K(t) = \frac{(t-1)(2t^3 - Kt^2 + (K-1)t - 1)}{t(t^2+K)(1+Kt)}$.

Let me factor $2t^3 - Kt^2 + (K-1)t - 1$. At $t = 1$: $2 - K + K - 1 - 1 = 0$. So $(t-1)$ is a factor.

$2t^3 - Kt^2 + (K-1)t - 1 = (t-1)(2t^2 + (2-K)t + 1)$

Check: $(t-1)(2t^2 + (2-K)t + 1) = 2t^3 + (2-K)t^2 + t - 2t^2 - (2-K)t - 1 = 2t^3 + (2-K-2)t^2 + (1-2+K)t - 1 = 2t^3 - Kt^2 + (K-1)t - 1$. ✓

So $S_K(t) = \frac{(t-1)^2(2t^2 + (2-K)t + 1)}{t(t^2+K)(1+Kt)}$.

For $t > 0$, the denominator is positive, and $(t-1)^2 \geq 0$. So $\text{sign}(S_K(t)) = \text{sign}(2t^2 + (2-K)t + 1)$.

For the inequality to hold (for $A = B = 1$), we need $2t^2 + (2-K)t + 1 \geq 0$ for all $t > 0$.

The quadratic $q(t) = 2t^2 + (2-K)t + 1$ has discriminant $\Delta = (2-K)^2 - 8 = K^2 - 4K + 4 - 8 = K^2 - 4K - 4$.

For $q(t) \geq 0$ for all $t > 0$, we need either $\Delta \leq 0$ (i.e., $K^2 - 4K - 4 \leq 0$, i.e., $K \leq 2 + 2\sqrt{2}$) or the roots are $\leq 0$.

$\Delta \leq 0 \iff K \leq 2 + 2\sqrt{2} \approx 4.828$ or $K \geq 2 - 2\sqrt{2}$ (negative, so irrelevant since $K > 0$).

If $\Delta > 0$ (i.e., $K > 2 + 2\sqrt{2}$), the roots are $t = \frac{K-2 \pm \sqrt{K^2-4K-4}}{4}$. For $K > 2 + 2\sqrt{2}$, $K - 2 > 0$, so both roots could be positive. The product of roots is $1/2 > 0$ and sum is $(K-2)/2 > 0$, so both roots are positive. Thus $q(t) < 0$ between the roots, and the inequality fails.

So for the case $A = B$, the inequality holds iff $K \leq 2 + 2\sqrt{2}$.

But we also need to check other cases (not just $A = B$). The maximum $K$ might be even smaller.

Wait, but the case $A = B$ gives us $K \leq 2 + 2\sqrt{2}$. Let me check if this is indeed the answer by testing other configurations.

At $K = 2 + 2\sqrt{2}$, the quadratic $q(t) = 2t^2 + (2 - 2 - 2\sqrt{2})t + 1 = 2t^2 - 2\sqrt{2}t + 1 = 2(t - \frac{\sqrt{2}}{2})^2 = 2(t - \frac{1}{\sqrt{2}})^2 \geq 0$.

So at $K = 2 + 2\sqrt{2}$, $q(t) = 2(t - 1/\sqrt{2})^2 \geq 0$, with equality at $t = 1/\sqrt{2}$.

This means $S_K(t) = 0$ when $t = 1$ (always) or $t = 1/\sqrt{2}$ (at $K = 2+2\sqrt{2}$). The equality cases are $A = B = C$ and $(A, B, C) = (1, 1, 1/\sqrt{2})$ (and permutations).

Now I need to check whether $K = 2 + 2\sqrt{2}$ works for ALL $A, B, C > 0$, not just $A = B$.

Let me test a case where $A, B, C$ are all different. Let me try $A = 1, B = 2, C = 3$ with $K = 2 + 2\sqrt{2} \approx 4.828$.

LHS = $\frac{1}{1 + 4.828 \cdot 6} + \frac{2}{4 + 4.828 \cdot 3} + \frac{3}{9 + 4.828 \cdot 2}$

$= \frac{1}{29.97} + \frac{2}{18.49} + \frac{3}{18.66}$

$= 0.03337 + 0.10817 + 0.16075 = 0.30229$

RHS = $\frac{1}{5.828}(1 + 0.5 + 0.3333) = \frac{1.8333}{5.828} = 0.31460$

LHS < RHS. ✓

Let me try $A = 1, B = 1, C = 0.6$ (close to $1/\sqrt{2} \approx 0.707$).

LHS = $\frac{2}{1 + 4.828 \cdot 0.6} + \frac{0.6}{0.36 + 4.828}$

$= \frac{2}{3.897} + \frac{0.6}{5.188}$

$= 0.51322 + 0.11565 = 0.62887$

RHS = $\frac{1}{5.828}(2 + 1.6667) = \frac{3.6667}{5.828} = 0.62913$

LHS < RHS. ✓ (barely)

Let me try $A = 1, B = 1, C = 0.7$:

LHS = $\frac{2}{1 + 4.828 \cdot 0.7} + \frac{0.7}{0.49 + 4.828}$

$= \frac{2}{4.380} + \frac{0.7}{5.318}$

$= 0.45662 + 0.13163 = 0.58825$

RHS = $\frac{1}{5.828}(2 + 1.4286) = \frac{3.4286}{5.828} = 0.58831$

LHS < RHS. ✓ (very close)

At $t = 1/\sqrt{2} \approx 0.7071$:

LHS = $\frac{2}{1 + 4.828 \cdot 0.7071} + \frac{0.7071}{0.5 + 4.828}$

$= \frac{2}{4.414} + \frac{0.7071}{5.328}$

$= 0.45308 + 0.13271 = 0.58579$

RHS = $\frac{1}{5.828}(2 + 1.4142) = \frac{3.4142}{5.828} = 0.58579$

Equality! ✓

Now let me try a more adversarial case. Let me try $A = 1, B = 0.5, C = 0.5$ (so $B = C$, different from $A$).

By the $A = B$ analysis with roles swapped: set $B = C = 1, A = t$ where $t = 2$ (since $A = 1, B = C = 0.5$ is equivalent to $A = 2, B = C = 1$ by scaling).

$S_K(2) = \frac{(2-1)^2(2 \cdot 4 + (2-K) \cdot 2 + 1)}{2(4+K)(1+2K)} = \frac{8 + 4 - 2K + 1}{2(4+K)(1+2K)} = \frac{13-2K}{2(4+K)(1+2K)}$

At $K = 2 + 2\sqrt{2} \approx 4.828$: $13 - 2(4.828) = 13 - 9.657 = 3.343 > 0$. ✓

Let me try $A = 1, B = 3, C = 1/3$ (so $BC = 1$, $A = 1$).

LHS = $\frac{1}{1 + K} + \frac{3}{9 + K/3} + \frac{1/3}{1/9 + 3K}$

$= \frac{1}{1+K} + \frac{9}{27+K} + \frac{1}{1/3 + 9K}$

$= \frac{1}{1+K} + \frac{9}{27+K} + \frac{3}{1+27K}$

At $K = 2 + 2\sqrt{2} \approx 4.828$:

$= \frac{1}{5.828} + \frac{9}{31.828} + \frac{3}{131.357}$

$= 0.17159 + 0.28278 + 0.02284 = 0.47721$

RHS = $\frac{1}{5.828}(1 + 1/3 + 3) = \frac{4.3333}{5.828} = 0.74359$

LHS < RHS. ✓

Let me try to find a potential counterexample by optimization. The critical case seems to be when two variables are equal. Let me check if there's a worse case with three distinct variables.

Actually, let me think about this more carefully. The condition from $A = B$ gives $K \leq 2 + 2\sqrt{2}$. But maybe a different configuration (not $A = B$) gives a tighter bound.

Let me try the general second-order analysis. Set $A = 1 + \epsilon a, B = 1 + \epsilon b, C = 1 + \epsilon c$ with $a + b + c = 0$ (to stay on the hyperplane $A + B + C = 3$, which is WLOG by homogeneity... actually, the normalization should be such that equality holds at $A = B = C = 1$).

Actually, by homogeneity, we can set $A + B + C = 3$ (or any normalization). At $A = B = C = 1$, equality holds for any $K$. The question is what happens near this point.

Let me set $A = 1 + \epsilon a, B = 1 + \epsilon b, C = 1 + \epsilon c$ with $a + b + c = 0$ and expand to second order in $\epsilon$.

The difference $D = \text{RHS} - \text{LHS}$ should be $\geq 0$. At $\epsilon = 0$, $D = 0$. The first-order term vanishes by symmetry. The second-order term gives a condition on $K$.

Let me compute. Actually, this is the generalization of the second derivative test to all directions $(a, b, c)$ with $a + b + c = 0$.

For the direction $(a, b, c) = (1, -1, 0)$ (which corresponds to $A = 1+\epsilon, B = 1-\epsilon, C = 1$), this is equivalent to the $A = B$ case with $t$ near 1... actually no. Let me think again.

The direction $(1, -1, 0)$ means $A = 1+\epsilon, B = 1-\epsilon, C = 1$. This is different from the $A = B$ case.

For the $A = B$ case, the direction is $(0, 0, 1)$ normalized, i.e., $(a, b, c) = (0, 0, 1)$ with the constraint... but $a + b + c = 0$ requires $c = -a - b$, so the direction $(0, 0, 1)$ doesn't satisfy $a + b + c = 0$.

Hmm, I think the issue is that the $A = B$ case with $C = t$ doesn't stay on the $A + B + C = 3$ hyperplane. Let me use a different normalization.

Actually, by homogeneity, the inequality is invariant under scaling $(A, B, C) \to (\lambda A, \lambda B, \lambda C)$. So we can normalize however we want. The $A = B = 1, C = t$ family is a valid one-parameter family.

The second derivative test at $t = 1$ in this family gave $f''(1) \propto K(K-5)$, suggesting $K \leq 5$. But the exact computation showed the inequality fails for $K = 5$ and even for $K > 2 + 2\sqrt{2}$.

The discrepancy is because $f''(1) = 0$ at $K = 5$ means the second-order term vanishes, and we need to look at higher-order terms. The exact factorization showed that the sign is determined by $q(t) = 2t^2 + (2-K)t + 1$, and the condition is $K \leq 2 + 2\sqrt{2}$.

So the second derivative test was misleading because at $K = 5$, $f''(1) = 0$ but the third-order term matters. The exact computation is more reliable.

Now, the key question: is $K = 2 + 2\sqrt{2}$ the answer, or could a non-$A=B$ configuration give a tighter bound?

Let me check the general second-order condition. Set $A = e^{\epsilon a}, B = e^{\epsilon b}, C = e^{\epsilon c}$ with $a + b + c = 0$ (this ensures $ABC = 1$ for all $\epsilon$, which is a valid normalization).

Define $F(\epsilon) = \sum_{\text{cyc}} \frac{1 - A^3}{A(A^3 + K)}$ where I'm using the $ABC = 1$ normalization (so $BC = 1/A$, etc., and the inequality becomes $\sum \frac{1-A^3}{A(A^3+K)} \geq 0$).

Wait, I need to redo the normalization. With $ABC = 1$, the inequality at general $K$ is:

$\sum \frac{A}{A^2 + KBC} \leq \frac{1}{K+1} \sum \frac{1}{A}$

With $BC = 1/A$: $\frac{A}{A^2 + K/A} = \frac{A^2}{A^3 + K}$.

So $\sum \frac{A^2}{A^3 + K} \leq \frac{1}{K+1} \sum \frac{1}{A}$.

$\sum \left(\frac{1}{(K+1)A} - \frac{A^2}{A^3+K}\right) \geq 0$

$\sum \frac{A^3 + K - (K+1)A^3}{(K+1)A(A^3+K)} \geq 0$

$\sum \frac{K - KA^3}{(K+1)A(A^3+K)} \geq 0$

$\sum \frac{1 - A^3}{A(A^3+K)} \geq 0$

OK so with $ABC = 1$, we need $G(A) + G(B) + G(C) \geq 0$ where $G(x) = \frac{1-x^3}{x(x^3+K)}$.

Now set $A = e^{\epsilon a}, B = e^{\epsilon b}, C = e^{\epsilon c}$, $a+b+c = 0$.

$G(e^{\epsilon a}) = \frac{1 - e^{3\epsilon a}}{e^{\epsilon a}(e^{3\epsilon a}+K)}$

Let $\phi(s) = G(e^s) = \frac{1-e^{3s}}{e^s(e^{3s}+K)} = \frac{1-e^{3s}}{e^{4s}+Ke^s}$.

$\phi(0) = 0$.

$\phi'(s) = \frac{-3e^{3s}(e^{4s}+Ke^s) - (1-e^{3s})(4e^{4s}+Ke^s)}{(e^{4s}+Ke^s)^2}$

At $s = 0$: $\phi'(0) = \frac{-3(1+K) - 0}{(1+K)^2} = \frac{-3}{1+K}$.

$\sum \phi(\epsilon a_i) \approx \epsilon \phi'(0) \sum a_i + \frac{\epsilon^2}{2} \phi''(0) \sum a_i^2 + ...$

Since $\sum a_i = 0$, the first-order term vanishes. The second-order term is $\frac{\epsilon^2}{2}\phi''(0)(a^2+b^2+c^2)$.

For the inequality to hold, we need $\phi''(0) \geq 0$.

Let me compute $\phi''(0)$.

$\phi'(s) = \frac{N(s)}{D(s)^2}$ where $N(s) = -3e^{3s}(e^{4s}+Ke^s) - (1-e^{3s})(4e^{4s}+Ke^s)$ and $D(s) = e^{4s}+Ke^s$.

At $s = 0$: $N(0) = -3(1+K)$, $D(0) = 1+K$.

$N(s) = -3e^{7s} - 3Ke^{4s} - 4e^{4s} - Ke^s + 4e^{7s} + Ke^{4s}$

$= e^{7s} - 2Ke^{4s} - 4e^{4s} - Ke^s$

Wait let me redo:

$N(s) = -3e^{3s} \cdot e^{4s} - 3e^{3s} \cdot Ke^s - (1-e^{3s})(4e^{4s}+Ke^s)$

$= -3e^{7s} - 3Ke^{4s} - 4e^{4s} - Ke^s + 4e^{7s} + Ke^{4s}$

$= e^{7s} - 2Ke^{4s} - 4e^{4s} - Ke^s$

$= e^{7s} - (2K+4)e^{4s} - Ke^s$

$N(0) = 1 - (2K+4) - K = 1 - 2K - 4 - K = -3K - 3 = -3(K+1)$. ✓

$N'(s) = 7e^{7s} - 4(2K+4)e^{4s} - Ke^s$

$N'(0) = 7 - 4(2K+4) - K = 7 - 8K - 16 - K = -9K - 9 = -9(K+1)$

$D(s) = e^{4s} + Ke^s$, $D(0) = 1+K$, $D'(s) = 4e^{4s} + Ke^s$, $D'(0) = 4+K$.

$\phi'(s) = \frac{N(s)}{D(s)^2}$

$\phi''(s) = \frac{N'(s)D(s)^2 - N(s) \cdot 2D(s)D'(s)}{D(s)^4} = \frac{N'(s)D(s) - 2N(s)D'(s)}{D(s)^3}$

$\phi''(0) = \frac{N'(0)D(0) - 2N(0)D'(0)}{D(0)^3} = \frac{-9(K+1)(K+1) - 2(-3(K+1))(K+4)}{(K+1)^3}$

$= \frac{-9(K+1)^2 + 6(K+1)(K+4)}{(K+1)^3} = \frac{(K+1)[-9(K+1) + 6(K+4)]}{(K+1)^3} = \frac{-9K-9+6K+24}{(K+1)^2} = \frac{-3K+15}{(K+1)^2} = \frac{3(5-K)}{(K+1)^2}$

So $\phi''(0) = \frac{3(5-K)}{(K+1)^2}$.

For $\phi''(0) \geq 0$, we need $K \leq 5$.

But we showed that for the $A = B$ family, the condition is $K \leq 2 + 2\sqrt{2} \approx 4.828 < 5$.

This means the second-order analysis (which gives $K \leq 5$) is not tight enough. The $A = B$ family gives a tighter bound. But is $2 + 2\sqrt{2}$ the tightest?

The second-order analysis considers infinitesimal perturbations from $A = B = C$. The $A = B$ family considers finite perturbations. The finite perturbation can be tighter because it captures global behavior, not just local.

But could there be an even tighter constraint from a different family? Let me check.

The $A = B$ family gave the condition $2t^2 + (2-K)t + 1 \geq 0$ for all $t > 0$, which requires $K \leq 2 + 2\sqrt{2}$.

By symmetry, the families $B = C$ and $A = C$ give the same condition.

What about a family where no two variables are equal? Let me try $A = 1, B = s, C = s^2$ (geometric progression) and see if we get a tighter condition.

Actually, let me think about it differently. The equality cases at $K = 2 + 2\sqrt{2}$ are:
1. $A = B = C$ (always)
2. $(A, B, C) = (1, 1, 1/\sqrt{2})$ and permutations (from the $A = B$ family)

If these are the only equality cases, then $K = 2 + 2\sqrt{2}$ is likely the answer.

Let me verify numerically that $K = 2 + 2\sqrt{2}$ works for a few more cases.

Let me try $A = 1, B = 2, C = 0.4$:

$K = 2 + 2\sqrt{2} \approx 4.8284$

LHS = $\frac{1}{1 + 4.8284 \cdot 0.8} + \frac{2}{4 + 4.8284 \cdot 0.4} + \frac{0.4}{0.16 + 4.8284 \cdot 2}$

$= \frac{1}{4.8628} + \frac{2}{5.9314} + \frac{0.4}{9.8169}$

$= 0.20563 + 0.33719 + 0.04074 = 0.58356$

RHS = $\frac{1}{5.8284}(1 + 0.5 + 2.5) = \frac{4}{5.8284} = 0.68629$

LHS < RHS. ✓

Let me try $A = 1, B = 0.8, C = 0.7$:

LHS = $\frac{1}{1 + 4.8284 \cdot 0.56} + \frac{0.8}{0.64 + 4.8284 \cdot 0.7} + \frac{0.7}{0.49 + 4.8284 \cdot 0.8}$

$= \frac{1}{3.7039} + \frac{0.8}{4.0239} + \frac{0.7}{4.3627}$

$= 0.26999 + 0.19881 + 0.16048 = 0.62928$

RHS = $\frac{1}{5.8284}(1 + 1.25 + 1.4286) = \frac{3.6786}{5.8284} = 0.63122$

LHS < RHS. ✓

Let me try to find a near-equality case with three distinct variables. Let me try $A = 1, B = 1/\sqrt{2}, C = 1/\sqrt{2}$ (which is the equality case from $A = B$ family, but with a different pair equal).

$(A, B, C) = (1, 1/\sqrt{2}, 1/\sqrt{2})$: This is the $B = C$ case with $A = 1, B = C = 1/\sqrt{2}$.

By the $A = B$ analysis (with $A$ and $C$ swapped), set $B = C = 1, A = t$ with $t = \sqrt{2}$.

$S_K(\sqrt{2}) = \frac{(\sqrt{2}-1)^2(2 \cdot 2 + (2-K)\sqrt{2} + 1)}{\sqrt{2}(2+K)(1+K\sqrt{2})}$

$= \frac{(\sqrt{2}-1)^2(5 - K\sqrt{2} + 2\sqrt{2})}{\sqrt{2}(2+K)(1+K\sqrt{2})}$

Hmm wait, let me use the formula: $q(t) = 2t^2 + (2-K)t + 1$.

$q(\sqrt{2}) = 2 \cdot 2 + (2-K)\sqrt{2} + 1 = 5 + (2-K)\sqrt{2}$.

At $K = 2 + 2\sqrt{2}$: $q(\sqrt{2}) = 5 + (2 - 2 - 2\sqrt{2})\sqrt{2} = 5 - 2\sqrt{2} \cdot \sqrt{2} = 5 - 4 = 1 > 0$.

So $S > 0$ at this point, not equality. The equality case is $t = 1/\sqrt{2}$ (from the $A = B$ family), which by permutation gives $(A, B, C) = (1/\sqrt{2}, 1, 1)$ or $(1, 1/\sqrt{2}, 1)$ or $(1, 1, 1/\sqrt{2})$.

So the equality cases at $K = 2 + 2\sqrt{2}$ are $A = B = C$ and permutations of $(1, 1, 1/\sqrt{2})$.

Now, I need to prove that $K = 2 + 2\sqrt{2}$ works for all $A, B, C > 0$. Let me attempt a proof.

We need to show: $\sum_{\text{cyc}} \frac{BC - A^2}{A(A^2 + KBC)} \geq 0$ for $K = 2 + 2\sqrt{2}$.

Let me denote $K = 2 + 2\sqrt{2}$ for convenience.

**Approach: SOS after clearing denominators.**

Let me try to clear denominators and show the resulting polynomial is non-negative.

The expression is $\sum_{\text{cyc}} \frac{BC - A^2}{A(A^2 + KBC)}$.

Common denominator: $\prod_{\text{cyc}} A(A^2 + KBC) = ABC \prod_{\text{cyc}} (A^2 + KBC)$.

Numerator: $\sum_{\text{cyc}} (BC - A^2) \cdot B(B^2+KAC) \cdot C(C^2+KAB)$

$= \sum_{\text{cyc}} BC(BC - A^2)(B^2+KAC)(C^2+KAB)$

This is a degree-8 polynomial (each term: $BC$ is degree 2, $(BC-A^2)$ is degree 2, $(B^2+KAC)$ is degree 2, $(C^2+KAB)$ is degree 2, total degree 8).

Let me try to expand this. Actually, this is very tedious. Let me try a different approach.

**Approach: Use the $A = B$ reduction and mixing variables.**

The idea is to show that for fixed $ABC$ (or fixed $A+B+C$, etc.), the expression $S = \sum \frac{BC-A^2}{A(A^2+KBC)}$ is minimized when two variables are equal. Then the $A = B$ analysis gives the bound.

This is the "mixing variables" or "smoothing" method. Let me try to show that if we replace $(B, C)$ by $(\sqrt{BC}, \sqrt{BC})$ (keeping $A$ and $BC$ fixed), the expression decreases (or the LHS of the original inequality increases).

Actually, let me think about what happens when we fix $A$ and $BC$ and vary $B/C$.

Set $B = \sqrt{BC} \cdot e^s, C = \sqrt{BC} \cdot e^{-s}$, so $BC$ is fixed and $B/C = e^{2s}$.

The terms involving $B$ and $C$:

$\frac{BC - A^2}{A(A^2+KBC)}$ is independent of $s$ (depends only on $A$ and $BC$).

$\frac{AC - B^2}{B(B^2+KAC)} = \frac{A\sqrt{BC}e^{-s} - BC \cdot e^{2s}}{\sqrt{BC}e^s(BC \cdot e^{2s} + KA\sqrt{BC}e^{-s})}$

$= \frac{A\sqrt{BC}e^{-s} - BC e^{2s}}{\sqrt{BC}e^s \cdot BC e^{2s} + \sqrt{BC}e^s \cdot KA\sqrt{BC}e^{-s}}$

Hmm, this is getting complicated. Let me try a different approach.

**Approach: Direct proof using algebraic manipulation.**

Let me go back to the $ABC = 1$ normalization. We need:

$$\sum_{\text{cyc}} \frac{1-A^3}{A(A^3+K)} \geq 0, \quad K = 2+2\sqrt{2}$$

Let $f(x) = \frac{1-x^3}{x(x^3+K)}$. We need $f(A) + f(B) + f(C) \geq 0$ with $ABC = 1$.

Note $f(x) = \frac{-(x-1)(x^2+x+1)}{x(x^3+K)}$.

Let me try the substitution $A = e^u, B = e^v, C = e^w, u+v+w = 0$ and define $\psi(u) = f(e^u)$.

We need $\psi(u) + \psi(v) + \psi(w) \geq 0$ with $u+v+w = 0$.

We computed $\psi(0) = 0, \psi'(0) = -3/(K+1), \psi''(0) = 3(5-K)/(K+1)^2$.

At $K = 2+2\sqrt{2}$: $\psi''(0) = 3(5 - 2 - 2\sqrt{2})/(3+2\sqrt{2})^2 = 3(3-2\sqrt{2})/(3+2\sqrt{2})^2$.

$3 - 2\sqrt{2} \approx 3 - 2.828 = 0.172 > 0$. So $\psi''(0) > 0$, meaning $\psi$ is locally convex at 0.

But we need global convexity or some other property. Let me check if $\psi$ is convex everywhere.

$\psi(u) = \frac{1-e^{3u}}{e^{4u}+Ke^u}$

This doesn't look like it's globally convex. Let me try a different approach.

**Approach: Tangent line trick with a better function.**

Instead of $\beta \ln x$, let me try $\alpha + \beta \ln x + \gamma (\ln x)^2$ or some other form.

Actually, let me try the following: find constants $\alpha, \beta$ such that

$$\frac{1-x^3}{x(x^3+K)} \geq \alpha(1 - x^p) + \beta \ln x$$

for all $x > 0$, where $p$ is chosen so that $\sum (1 - A^p) \geq 0$ when $ABC = 1$ (by AM-GM or similar).

By AM-GM, if $p > 0$, $\sum A^p \geq 3(ABC)^{p/3} = 3$, so $\sum (1-A^p) \leq 0$. That's the wrong direction.

If $p < 0$, $\sum A^p \geq 3$ (by AM-GM on $A^p, B^p, C^p$ with product $(ABC)^p = 1$), so $\sum(1-A^p) \leq 0$. Still wrong.

Hmm. Let me think differently.

Actually, the tangent line trick works as follows: we want $f(x) \geq \ell(x)$ where $\ell$ is a linear function of some variable $t = t(x)$, and $\sum \ell(t(A_i)) \geq 0$ when $ABC = 1$.

The standard choice is $t = \ln x$, and $\ell(t) = \alpha + \beta t$, with $\sum t(A_i) = \ln(ABC) = 0$, so $\sum \ell = 3\alpha$. We need $\alpha \leq 0$ (from $f(1) = 0$) and $\alpha \geq 0$ (for $3\alpha \geq 0$), so $\alpha = 0$ and we need $f(x) \geq \beta \ln x$.

We showed this doesn't work with a single $\beta$ (the ratio $f(x)/\ln x$ is not constant).

**Alternative: Use a quadratic in $\ln x$.**

Let $t = \ln x$. We want $f(e^t) \geq at^2 + bt$ for all $t$, where $a \leq 0$ (so the quadratic is concave) and... hmm, but then $\sum (at_i^2 + bt_i) = a \sum t_i^2 + b \sum t_i = a \sum t_i^2$. If $a \leq 0$, this is $\leq 0$, which is the wrong direction.

If $a \geq 0$, then $\sum (at_i^2 + bt_i) = a\sum t_i^2 \geq 0$, which is what we want. But then we need $f(e^t) \geq at^2 + bt$ with $a \geq 0$, meaning $f(e^t) - at^2 - bt \geq 0$ for all $t$. At $t = 0$: $f(1) = 0 \geq 0$. ✓. The derivative at $t = 0$: $f'(e^0) \cdot e^0 - b = \psi'(0) - b = -3/(K+1) - b$. For this to be 0 (tangent), $b = -3/(K+1)$.

Second derivative: $\psi''(0) - 2a = 3(5-K)/(K+1)^2 - 2a$. For $t = 0$ to be a minimum of $f(e^t) - at^2 - bt$, we need $\psi''(0) - 2a \geq 0$, i.e., $a \leq 3(5-K)/(2(K+1)^2)$.

At $K = 2+2\sqrt{2}$: $a \leq 3(3-2\sqrt{2})/(2(3+2\sqrt{2})^2)$.

$(3+2\sqrt{2})^2 = 9 + 12\sqrt{2} + 8 = 17 + 12\sqrt{2}$.

$3(3-2\sqrt{2})/(2(17+12\sqrt{2}))$.

$3-2\sqrt{2} = (3-2\sqrt{2})$, and $17+12\sqrt{2} = (3+2\sqrt{2})^2$. Also $3-2\sqrt{2} = 1/(3+2\sqrt{2})$ (since $(3-2\sqrt{2})(3+2\sqrt{2}) = 9-8 = 1$).

So $a \leq 3/(2(3+2\sqrt{2})^3)$.

This is positive, so we can choose $a > 0$. But we need $f(e^t) \geq at^2 + bt$ for ALL $t$, not just near $t = 0$. This requires checking the global behavior.

This approach might work but requires careful analysis. Let me try a different, more direct approach.

**Approach: Reduce to two variables equal using the method of Lagrange multipliers.**

Claim: The minimum of $S(A,B,C) = \sum \frac{BC-A^2}{A(A^2+KBC)}$ subject to $ABC = 1$ is achieved when at least two of $A, B, C$ are equal.

If this claim is true, then the $A = B$ analysis suffices, and $K = 2 + 2\sqrt{2}$ is the answer.

To prove the claim, we can use the method of Lagrange multipliers. At a critical point of $S$ subject to $ABC = 1$, we have $\nabla S = \lambda \nabla(\ln A + \ln B + \ln C)$, i.e., $\frac{\partial S}{\partial A} = \lambda/A$, etc.

If we can show that the system $\frac{\partial S}{\partial A} \cdot A = \frac{\partial S}{\partial B} \cdot B = \frac{\partial S}{\partial C} \cdot C$ implies $A = B$ or $B = C$ or $A = C$ (at a minimum), then the claim follows.

This is plausible but the computation is involved. Let me try a different approach.

**Approach: SOS decomposition.**

Let me try to directly prove the inequality at $K = 2 + 2\sqrt{2}$ by finding an SOS decomposition.

Going back to the original form (without normalization):

$$\sum_{\text{cyc}} \frac{BC - A^2}{A(A^2 + KBC)} \geq 0, \quad K = 2 + 2\sqrt{2}$$

Let me denote $K = 2 + 2\sqrt{2}$ and $\alpha = \sqrt{2}$ for convenience, so $K = 2(1 + \alpha)$.

Actually, let me try a substitution that simplifies things. Let $A = x^2, B = y^2, C = z^2$. Then $BC = y^2z^2$ and:

$$\sum_{\text{cyc}} \frac{y^2z^2 - x^4}{x^2(x^4 + Ky^2z^2)} \geq 0$$

Not obviously simpler.

Let me try $A = a^2, B = b^2, C = c^2$ and see if the cleared-denominator polynomial has a nice SOS form.

Actually, let me try a completely different approach. Let me use the substitution $u = A^2/(BC), v = B^2/(AC), w = C^2/(AB)$. Note $uvw = ABC/(ABC) = 1$... wait, $u \cdot v \cdot w = \frac{A^2 B^2 C^2}{A^2 B^2 C^2} = 1$. And $u = A^3/(ABC), v = B^3/(ABC), w = C^3/(ABC)$, so $u + v + w = (A^3+B^3+C^3)/(ABC)$ and $uvw = 1$.

With $ABC = 1$: $u = A^3, v = B^3, w = C^3$, $uvw = 1$.

$\frac{BC - A^2}{A(A^2+KBC)} = \frac{1/A - A^2}{A(A^2 + K/A)} = \frac{(1-A^3)/A}{A \cdot (A^3+K)/A} = \frac{1-A^3}{A^3+K} \cdot \frac{1}{A} \cdot \frac{A}{1}$

Hmm wait, let me redo. With $ABC = 1$, $BC = 1/A$:

$\frac{BC - A^2}{A(A^2+KBC)} = \frac{1/A - A^2}{A(A^2 + K/A)} = \frac{(1-A^3)/A}{A \cdot (A^3+K)/A} = \frac{(1-A^3)/A}{(A^3+K)} = \frac{1-A^3}{A(A^3+K)}$

So $S = \sum \frac{1-A^3}{A(A^3+K)} = \sum \frac{1-u}{u^{1/3}(u+K)}$ with $u = A^3, v = B^3, w = C^3, uvw = 1$.

Let me substitute $u = p/q, v = q/r, w = r/p$ (so $uvw = 1$). Then:

$\frac{1-u}{u^{1/3}(u+K)} = \frac{1-p/q}{(p/q)^{1/3}(p/q+K)} = \frac{(q-p)/q}{p^{1/3}/q^{1/3} \cdot (p+Kq)/q} = \frac{(q-p) \cdot q^{1/3}}{p^{1/3}(p+Kq)}$

This doesn't simplify nicely either.

Let me try yet another approach. Let me use the Schur inequality directly.

**Schur inequality approach:**

The Schur inequality (for $t = 2$) states: $\sum A^2(A-B)(A-C) \geq 0$, which expands to $\sum A^4 + ABC \sum A \geq \sum A^3 B + \sum A^3 C = \sum_{sym} A^3 B$.

Hmm, I'm not sure how to connect this to our inequality.

Let me try a more computational approach. Let me verify the answer $K = 2 + 2\sqrt{2}$ by testing many random points numerically (in my head or by reasoning), and then try to construct a proof.

Actually, let me try to prove the inequality at $K = 2 + 2\sqrt{2}$ using the following strategy:

1. Show that the minimum of $S$ subject to $ABC = 1$ occurs when two variables are equal (by the method of mixing variables / smoothing).
2. Use the explicit computation for $A = B$ to conclude.

For step 1, the mixing variables method works as follows: show that for fixed $A$ and $BC$, the expression $S$ is minimized when $B = C = \sqrt{BC}$.

Let me try this. Fix $A$ and $P = BC$. Set $B = \sqrt{P} e^s, C = \sqrt{P} e^{-s}$.

$S = \frac{P - A^2}{A(A^2+KP)} + \frac{A\sqrt{P}e^{-s} - Pe^{2s}}{\sqrt{P}e^s(Pe^{2s} + KA\sqrt{P}e^{-s})} + \frac{A\sqrt{P}e^s - Pe^{-2s}}{\sqrt{P}e^{-s}(Pe^{-2s} + KA\sqrt{P}e^s)}$

The first term is independent of $s$. Let me focus on the sum of the second and third terms.

Second term: $\frac{A\sqrt{P}e^{-s} - Pe^{2s}}{\sqrt{P}e^s(Pe^{2s} + KA\sqrt{P}e^{-s})} = \frac{A\sqrt{P}e^{-s} - Pe^{2s}}{\sqrt{P}e^s \cdot \sqrt{P}( \sqrt{P}e^{2s} + KAe^{-s})}$

Hmm, this is getting messy. Let me simplify by setting $P = 1$ (WLOG by scaling, since we can scale $A, B, C$ together... but we've already fixed $ABC = 1$, so $P = BC = 1/A$, and we can't independently set $P = 1$).

Actually, let me use a different normalization. Since the inequality is homogeneous of degree 0 in the expression $S$ (wait, is it?).

$S = \sum \frac{BC - A^2}{A(A^2+KBC)}$. Under scaling $(A,B,C) \to (\lambda A, \lambda B, \lambda C)$: numerator scales as $\lambda^2$, denominator scales as $\lambda \cdot \lambda^2 = \lambda^3$, so each term scales as $1/\lambda$. So $S$ is homogeneous of degree $-1$, not 0.

So we can normalize, e.g., $A = 1$ (by scaling). Then we need to show $S(1, B, C) \geq 0$ for all $B, C > 0$.

$S(1, B, C) = \frac{BC - 1}{1+KBC} + \frac{C - B^2}{B(B^2+KC)} + \frac{B - C^2}{C(C^2+KB)}$

This is a two-variable inequality. Let me try to show it's non-negative.

Let me substitute $B = e^u, C = e^v$ and check convexity in some direction. Or let me try $B = r \cos\theta, C = r \sin\theta$... no, they're positive, not bounded.

Let me try a different approach. Let me use the substitution $B = t, C = 1/t$ (so $BC = 1$) and vary $t$.

$S(1, t, 1/t) = \frac{1 - 1}{1+K} + \frac{1/t - t^2}{t(t^2 + K/t)} + \frac{t - 1/t^2}{(1/t)(
