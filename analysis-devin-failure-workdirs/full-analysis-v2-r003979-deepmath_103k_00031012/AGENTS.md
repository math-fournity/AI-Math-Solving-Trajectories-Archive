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
  <problem_id>deepmath_103k_00031012</problem_id>
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

If a complex number \(z\) satisfies \(|z+3| + |z-3| = 10\), find the value of \(\frac{60|z+3|}{|z+\overline{z}+\frac{50}{3}|}\).

## Standard Solution

Okay, so I need to solve this problem where a complex number \( z \) satisfies \( |z + 3| + |z - 3| = 10 \). Then, I have to find the value of \( \frac{60|z + 3|}{|z + \overline{z} + \frac{50}{3}|} \). Let me try to break this down step by step.

First, the equation \( |z + 3| + |z - 3| = 10 \) reminds me of the definition of an ellipse in the complex plane. An ellipse is the set of points where the sum of the distances from two fixed points (called foci) is constant. In this case, the foci would be at \( -3 \) and \( 3 \) on the real axis, right? And the constant sum is 10. So, \( z \) lies on an ellipse with foci at \( (-3, 0) \) and \( (3, 0) \) and major axis length 10.

Let me recall the standard form of an ellipse. The sum of the distances from any point on the ellipse to the two foci is \( 2a \), where \( a \) is the semi-major axis. The distance between the foci is \( 2c \), so here the distance between \( -3 \) and \( 3 \) is 6, so \( 2c = 6 \) which means \( c = 3 \). Then, the relationship between \( a \), \( b \) (semi-minor axis), and \( c \) is \( c^2 = a^2 - b^2 \).

Given that the sum \( 2a = 10 \), so \( a = 5 \). Then, \( c = 3 \), so \( b^2 = a^2 - c^2 = 25 - 9 = 16 \), so \( b = 4 \). Therefore, the ellipse has semi-major axis 5 and semi-minor axis 4. The standard equation in real coordinates would be \( \frac{x^2}{25} + \frac{y^2}{16} = 1 \).

Since \( z \) is a complex number, we can write \( z = x + yi \), where \( x \) and \( y \) are real numbers. Then, \( |z + 3| \) is the distance from \( z \) to \( (-3, 0) \), and \( |z - 3| \) is the distance from \( z \) to \( (3, 0) \). So, the equation of the ellipse in terms of \( x \) and \( y \) is indeed \( \frac{x^2}{25} + \frac{y^2}{16} = 1 \).

Now, the problem asks for \( \frac{60|z + 3|}{|z + \overline{z} + \frac{50}{3}|} \). Let me try to simplify this expression.

First, note that \( z + \overline{z} = (x + yi) + (x - yi) = 2x \). So, \( |z + \overline{z} + \frac{50}{3}| = |2x + \frac{50}{3}| \). That's straightforward.

Next, \( |z + 3| \) is the distance from \( z \) to \( (-3, 0) \), which on the ellipse, as we know, varies between \( a - c = 5 - 3 = 2 \) and \( a + c = 5 + 3 = 8 \). But since we need an exact value, not just the range, we need to express \( |z + 3| \) in terms of \( x \) and \( y \), perhaps.

Given that \( z \) is on the ellipse \( \frac{x^2}{25} + \frac{y^2}{16} = 1 \), we can express \( y^2 = 16(1 - \frac{x^2}{25}) \). Then, \( |z + 3| = \sqrt{(x + 3)^2 + y^2} \). Let's substitute \( y^2 \):

\( |z + 3| = \sqrt{(x + 3)^2 + 16(1 - \frac{x^2}{25})} \)

Let me expand that:

First, \( (x + 3)^2 = x^2 + 6x + 9 \).

So,

\( \sqrt{x^2 + 6x + 9 + 16 - \frac{16x^2}{25}} \)

Combine like terms:

\( \sqrt{(x^2 - \frac{16x^2}{25}) + 6x + (9 + 16)} \)

Calculate \( x^2 - \frac{16x^2}{25} = \frac{25x^2 - 16x^2}{25} = \frac{9x^2}{25} \)

Then, 9 + 16 = 25.

So, inside the square root, we have \( \frac{9x^2}{25} + 6x + 25 \).

So, \( |z + 3| = \sqrt{\frac{9x^2}{25} + 6x + 25} \)

Hmm, maybe we can factor this expression or simplify it further. Let me try.

First, let's write all terms with denominator 25:

\( \frac{9x^2 + 150x + 625}{25} \)

Wait, 6x is equivalent to \( \frac{150x}{25} \), right? Because 6x = \( \frac{150x}{25} \). And 25 is \( \frac{625}{25} \). So, combining them:

\( \frac{9x^2 + 150x + 625}{25} \)

So, the entire expression under the square root becomes \( \sqrt{\frac{9x^2 + 150x + 625}{25}} = \frac{\sqrt{9x^2 + 150x + 625}}{5} \)

Let me factor the numerator:

9x² + 150x + 625. Let's see if this quadratic factors.

First, check discriminant: \( 150² - 4*9*625 = 22500 - 4*9*625 \)

Calculate 4*9=36, 36*625=22500

So discriminant is 22500 - 22500 = 0. So, it's a perfect square.

Therefore, the quadratic is a perfect square. Let's find its roots.

Since discriminant is zero, the root is at x = -b/(2a) = -150/(2*9) = -150/18 = -25/3.

So, 9x² + 150x + 625 = 9(x + 25/3)²

Wait, let's check:

9(x + 25/3)² = 9(x² + (50/3)x + (625/9)) = 9x² + 150x + 625. Perfect.

So, \( \sqrt{9x² + 150x + 625} = \sqrt{9(x + 25/3)^2} = 3|x + 25/3| \)

But since we have modulus, which is always positive, and since x is a real number (as part of the complex number z = x + yi), we can write this as 3|x + 25/3|

Therefore, \( |z + 3| = \frac{3|x + 25/3|}{5} \)

So, \( |z + 3| = \frac{3}{5}|x + \frac{25}{3}| \)

Interesting. So that gives us a relation between |z + 3| and x.

Now, the denominator in the expression we need to compute is |z + \overline{z} + 50/3| = |2x + 50/3| = |2x + 50/3|

Therefore, the entire expression is:

\( \frac{60|z + 3|}{|2x + 50/3|} = \frac{60*(3/5)|x + 25/3|}{|2x + 50/3|} \)

Simplify constants:

60*(3/5) = 60*(3)/5 = 12*3 = 36

So, numerator is 36|x + 25/3|

Denominator is |2x + 50/3|

Notice that 2x + 50/3 = 2(x + 25/3). So,

Denominator is |2(x + 25/3)| = 2|x + 25/3|

Therefore, the expression becomes:

36|x + 25/3| / (2|x + 25/3|) ) = 36/2 = 18

Wait, that simplifies to 18? But this seems too straightforward. Let me check.

So, starting from:

\( \frac{60|z + 3|}{|z + \overline{z} + \frac{50}{3}|} = \frac{60*(3/5)|x + 25/3|}{2|x + 25/3|} \)

Yes, numerator: 60*(3/5) = 36, denominator: 2

So, 36 / 2 = 18. So the answer is 18?

But that seems surprising. Let me verify each step.

First, starting from |z + 3|. Let's take z = x + yi. Then |z + 3| = sqrt{(x + 3)^2 + y^2}

We substituted y^2 from the ellipse equation: y² = 16(1 - x²/25)

So, |z + 3| = sqrt{(x + 3)^2 + 16(1 - x²/25)}. Then expanding:

(x + 3)^2 = x² + 6x + 9

16(1 - x²/25) = 16 - (16x²)/25

Adding them: x² + 6x + 9 + 16 - (16x²)/25 = (x² - (16x²)/25) + 6x + 25

Which is (9x²)/25 + 6x + 25. Then factoring:

9x² + 150x + 625 over 25. Then factor numerator as 9(x + 25/3)². Then sqrt of that is 3|x +25/3| over 5. Therefore, |z + 3| = (3/5)|x +25/3|

Then z + \overline{z} = 2x, so denominator is |2x + 50/3| = 2|x +25/3|

Therefore, the ratio is (60*(3/5)|x +25/3|) / (2|x +25/3|) = (36|x +25/3|)/(2|x +25/3|) = 18

Yes, the |x +25/3| cancels out, as long as |x +25/3| ≠ 0. But x is on the ellipse. Let me check if x can be -25/3.

Wait, the ellipse is \( \frac{x^2}{25} + \frac{y^2}{16} = 1 \). So x ranges between -5 and 5. Because semi-major axis is 5. But -25/3 is approximately -8.333, which is outside the range of x (-5 to 5). Therefore, |x +25/3| is always positive, since x can't be -25/3. Therefore, the cancellation is valid, and the ratio is indeed 18.

Therefore, the value is 18.

But wait, let me check if my substitution for y² was correct.

Given \( \frac{x^2}{25} + \frac{y^2}{16} = 1 \), solving for y² gives \( y^2 = 16(1 - \frac{x^2}{25}) \). That's correct.

Then, substituting into |z +3|:

sqrt{(x + 3)^2 + 16(1 - x²/25)}. Correct.

Expanding and simplifying led us to the expression. Then factoring into 9(x +25/3)^2, which is correct as we checked discriminant zero.

Therefore, the steps are correct.

Alternatively, is there another approach?

Let me think. Maybe parametrize the ellipse.

Since the ellipse is \( \frac{x^2}{25} + \frac{y^2}{16} = 1 \), we can write parametric equations as \( x = 5\cos\theta \), \( y = 4\sin\theta \), where \( \theta \) is the parameter.

Then, z = 5cosθ + 4i sinθ.

Then, let's compute |z + 3|.

|z + 3| = |5cosθ + 3 + 4i sinθ| = sqrt{(5cosθ + 3)^2 + (4 sinθ)^2}

Similarly, compute this:

Expand (5cosθ +3)^2 = 25cos²θ + 30cosθ +9

(4 sinθ)^2 = 16 sin²θ

So total inside sqrt: 25cos²θ +30cosθ +9 +16 sin²θ

Combine like terms:

25cos²θ +16 sin²θ +30cosθ +9

Note that 25cos²θ +16 sin²θ = 16(cos²θ + sin²θ) +9 cos²θ =16 +9 cos²θ

Therefore, expression becomes 16 +9 cos²θ +30cosθ +9 = 25 +9 cos²θ +30cosθ

Factor this as 9cos²θ +30cosθ +25

Which is (3cosθ +5)^2

Therefore, |z +3| = sqrt{(3cosθ +5)^2} = |3cosθ +5|

But since 3cosθ +5. Given that cosθ ranges between -1 and 1, so 3cosθ ranges between -3 and 3, so 3cosθ +5 ranges between 2 and 8, which is positive. Therefore, |3cosθ +5| = 3cosθ +5.

So, |z +3| = 3cosθ +5.

Similarly, compute the denominator |z + \overline{z} +50/3|.

z + \overline{z} = 2*Re(z) = 2*5cosθ =10cosθ

Therefore, |z + \overline{z} +50/3| = |10cosθ +50/3| = | (30cosθ +50)/3 | = (1/3)|30cosθ +50| = (10/3)|3cosθ +5|

So, denominator is (10/3)|3cosθ +5|. But 3cosθ +5 is positive, as established earlier, so |3cosθ +5| =3cosθ +5.

Therefore, denominator is (10/3)(3cosθ +5)

Therefore, the entire expression is:

60|z +3| / |z + \overline{z} +50/3| = 60*(3cosθ +5) / [ (10/3)(3cosθ +5) ] = 60 / (10/3) = 60*(3/10) = 18.

Same result. So regardless of θ, the ratio is 18. Therefore, the answer is 18.

Hence, the value is \boxed{18}

**Final Answer**
\boxed{18}
</think>

Given a complex number \( z \) that satisfies \( |z + 3| + |z - 3| = 10 \), we recognize that this describes an ellipse with foci at \((-3, 0)\) and \((3, 0)\) and a major axis of length 10. The semi-major axis \( a \) is 5, the distance between the foci \( 2c \) is 6, so \( c = 3 \), and the semi-minor axis \( b \) is 4. The equation of the ellipse is \( \frac{x^2}{25} + \frac{y^2}{16} = 1 \).

We need to find the value of \( \frac{60|z + 3|}{|z + \overline{z} + \frac{50}{3}|} \).

1. **Express \( |z + 3| \) and \( |z + \overline{z} + \frac{50}{3}| \)**:
   - For \( z = x + yi \), \( |z + 3| = \sqrt{(x + 3)^2 + y^2} \).
   - Using the ellipse equation, \( y^2 = 16(1 - \frac{x^2}{25}) \), substitute into \( |z + 3| \):
     \[
     |z + 3| = \sqrt{(x + 3)^2 + 16\left(1 - \frac{x^2}{25}\right)} = \sqrt{\frac{9x^2}{25} + 6x + 25} = \frac{3}{5}|x + \frac{25}{3}|
     \]
   - The denominator \( |z + \overline{z} + \frac{50}{3}| = |2x + \frac{50}{3}| = 2|x + \frac{25}{3}| \).

2. **Simplify the expression**:
   - Substitute the expressions into the given ratio:
     \[
     \frac{60|z + 3|}{|z + \overline{z} + \frac{50}{3}|} = \frac{60 \cdot \frac{3}{5}|x + \frac{25}{3}|}{2|x + \frac{25}{3}|} = \frac{36|x + \frac{25}{3}|}{2|x + \frac{25}{3}|} = \frac{36}{2} = 18
     \]

3. **Verification using parametric form**:
   - Parametrize the ellipse as \( x = 5\cos\theta \), \( y = 4\sin\theta \).
   - Calculate \( |z + 3| = 3\cos\theta + 5 \) and \( |z + \overline{z} + \frac{50}{3}| = \frac{10}{3}(3\cos\theta + 5) \).
   - Simplify the ratio:
     \[
     \frac{60(3\cos\theta + 5)}{\frac{10}{3}(3\cos\theta + 5)} = \frac{60 \cdot 3}{10} = 18
     \]

Thus, the value is \(\boxed{18}\).

## AI's Thinking (Attempted Solution Process)

The problem: Determine the number of positive integers, each with exactly 2^2005 digits, where each digit is either 7 or 8, such that among any two chosen integers, at most half of their corresponding digits are the same.

So we have strings of length n = 2^2005 over alphabet {7,8}. We want the maximum size of a code where any two codewords agree in at most n/2 positions. This is a coding theory question.

Let me think. We have binary code (map 7→0, 8→1) of length n = 2^2005. Condition: any two codewords agree in at most n/2 positions. Agreement in at most n/2 positions means Hamming distance at least n/2.

So we want the maximum size of a binary code of length n with minimum distance d ≥ n/2.

By Plotkin bound: For binary code, if d > n/2, then size ≤ 2·floor(d/(2d-n)). But here d = n/2 exactly (at most n/2 agree means distance ≥ n/2, so d_min ≥ n/2).

When d = n/2 exactly, the Plotkin bound in the standard form... Let me recall. The Plotkin bound states: for a binary code with minimum distance d, if 2d > n, then M ≤ 2⌊d/(2d-n)⌋. When 2d = n, this bound doesn't directly apply (denominator zero).

Actually for d = n/2, we need a different approach. Let me think about the exact maximum.

This is related to Hadamard codes. 

Let me think about the structure. We want binary strings of length n such that any two agree in at most n/2 positions, i.e., differ in at least n/2 positions.

Consider the Hadamard matrix connection. A Hadamard matrix of order n gives n codewords (rows) where any two rows agree in exactly n/2 positions. But we need "at most n/2", so agreement exactly n/2 is allowed.

Actually, let me reconsider. With Hadamard code of length n, we get 2n codewords (using rows and their complements) with pairwise distance exactly n/2. Wait, let me recall.

Hadamard code: from Hadamard matrix H of order n, the rows give n codewords. Any two distinct rows differ in exactly n/2 positions. Including complements gives 2n codewords, but a row and its complement differ in n positions, and two rows differ in n/2, a row and complement of another row differ in n/2 as well. So we get 2n codewords with minimum distance n/2.

But can we do better? The question is about the maximum.

Hmm, let me think about the Plotkin bound more carefully for d = n/2.

Actually, there's a refined result. Let me think about it via the "at most half agree" condition differently.

Let me think about it as: we have M binary vectors of length n. The condition is that for any two, the number of positions where they agree is ≤ n/2.

Equivalently, considering ±1 representation: map 7→+1, 8→-1. Two vectors agree in position i iff their signs are the same. The number of agreements minus disagreements = inner product. If agreements ≤ n/2, then agreements - disagreements ≤ 0, i.e., inner product ≤ 0.

So we need M vectors in {+1,-1}^n such that any two have inner product ≤ 0.

We want the maximum M.

This is a classic problem! The maximum number of vectors in {+1,-1}^n with pairwise non-positive inner products.

Hmm, what's the maximum? 

Let me think. If all pairwise inner products are ≤ 0, what's the max number of such ±1 vectors?

Claim: The maximum is 2n when n is a power of 2, achieved by Hadamard code. Wait, but let me verify the bound.

Actually, let me think about the general bound. Consider vectors v_1, ..., v_M in {+1,-1}^n with ⟨v_i, v_j⟩ ≤ 0 for i ≠ j.

Consider the Gram matrix G where G_{ij} = ⟨v_i, v_j⟩. Diagonal entries are n, off-diagonal ≤ 0.

Consider sum S = v_1 + ... + v_M. Then ||S||^2 = Σ⟨v_i,v_j⟩ = Mn + 2Σ_{i<j}⟨v_i,v_j⟩ ≤ Mn.

Also ||S||^2 ≥ 0.

That gives M ≤ ... not directly.

Let me think differently. Consider the matrix V whose rows are v_i. Then VV^T = G. 

Actually, let's think about it as a bound on M.

Consider the vectors as points. We have ⟨v_i, v_j⟩ ≤ 0 for i≠j.

There's a known result: the maximum number of ±1 vectors in R^n with pairwise nonpositive inner products is at most 2n, and this is achieved when a Hadamard matrix of order n exists.

Let me verify the upper bound of 2n.

Proof of upper bound: Consider the M vectors v_1, ..., v_M in {±1}^n with pairwise inner product ≤ 0.

Consider the matrix A (M×n) with rows v_i. Consider A^T A (n×n). 

Hmm, let me think about the approach using the fact that these vectors are in {±1}^n.

Alternative approach: Let's use the "rank" argument or a direct counting.

Let me consider: we want to show M ≤ 2n.

Consider the 2n vectors: v_1, ..., v_M, and also -v_1, ..., -v_M? No, that doubles.

Let me think about a cleaner approach.

Approach: Consider vectors w_i = v_i for i=1..M. We have ⟨v_i, v_j⟩ ≤ 0 for i≠j.

Now consider adding the all-ones vector or considering complements.

Actually here's a clean argument I recall:

Lemma: If v_1, ..., v_M are vectors in R^n (not necessarily ±1) with ⟨v_i, v_j⟩ ≤ 0 for all i≠j, and all v_i ≠ 0, then M ≤ 2n. 

Wait, that's not true in general for arbitrary vectors. For arbitrary vectors, you can have more... actually no. Let me think. In R^n, the maximum number of nonzero vectors with pairwise nonpositive inner products... 

Hmm, consider n=2. Vectors with pairwise ≤0 inner products. You can have v_1=(1,0), v_2=(0,1), v_3=(-1,-1). Check: ⟨v_1,v_2⟩=0, ⟨v_1,v_3⟩=-1, ⟨v_2,v_3⟩=-1. So M=3 = 2(2)-1. Can we get 4? v_4 = ? Need ⟨v_4, v_1⟩≤0, ⟨v_4,v_2⟩≤0, ⟨v_4,v_3⟩≤0. v_4 = (-a, -b) with a,b... ⟨v_4,v_1⟩ = -a ≤ 0 → a≥0. ⟨v_4,v_2⟩ = -b ≤0 → b≥0. ⟨v_4,v_3⟩ = a+b ≤ 0 → a+b≤0. So a=b=0, v_4=0. Not allowed. So max is 3 for n=2 with arbitrary vectors? But 2n = 4. Hmm so the bound 2n isn't tight for arbitrary vectors, and actually for arbitrary vectors the bound is different.

Wait, but for ±1 vectors in n=2: {±1}^2 has 4 vectors: (1,1),(1,-1),(-1,1),(-1,-1). Inner products: (1,1)·(1,-1)=0, (1,1)·(-1,1)=0, (1,1)·(-1,-1)=-2, (1,-1)·(-1,1)=-2, (1,-1)·(-1,-1)=0, (-1,1)·(-1,-1)=0. So all pairwise inner products are ≤0! So M=4 = 2n for n=2. Great, so for ±1 vectors we can achieve 2n.

So the bound M ≤ 2n for ±1 vectors, achieved when n is a power of 2 (Hadamard matrix exists).

Let me prove M ≤ 2n for ±1 vectors.

Proof: Let v_1, ..., v_M ∈ {±1}^n with ⟨v_i, v_j⟩ ≤ 0 for i ≠ j.

Consider the set S = {v_1, ..., v_M, -v_1, ..., -v_M}. These are 2M vectors (assuming no v_i = -v_j among the original, but actually if v_i = -v_j for some i≠j, then ⟨v_i, v_j⟩ = -n ≤ 0, that's fine, but then -v_i = v_j is a duplicate). 

Hmm, let me think about whether v_i = -v_j can happen. If v_i = -v_j, then they're complements, inner product -n, which is ≤0, allowed. But then in the set S there are duplicates. Let me handle this.

Actually, let me think about the standard proof.

Standard proof of Plotkin-type bound for d = n/2:

Consider the M codewords as ±1 vectors. For any two distinct codewords, ⟨v_i, v_j⟩ ≤ 0.

Consider the sum vector s = Σ v_i. Then:
||s||^2 = Σ_i ||v_i||^2 + 2Σ_{i<j} ⟨v_i, v_j⟩ = Mn + 2Σ_{i<j}⟨v_i,v_j⟩ ≤ Mn.

So ||s||^2 ≤ Mn. ... (1)

Now, ||s||^2 = Σ_{k=1}^n (Σ_i v_i(k))^2 = Σ_{k=1}^n s_k^2 where s_k = Σ_i v_i(k).

Each s_k = (number of +1's in position k) - (number of -1's in position k) = 2p_k - M where p_k = number of +1's in position k.

So s_k = 2p_k - M, and s_k^2 = (2p_k - M)^2.

Now, (2p_k - M)^2 ≥ 0, and since 2p_k - M is an integer with the same parity as M, we have (2p_k - M)^2 ≥ 0, with equality iff p_k = M/2 (requires M even).

So ||s||^2 = Σ_k (2p_k - M)^2 ≥ 0, and if M is even, the minimum per coordinate is 0; if M is odd, the minimum is 1 per coordinate (since 2p_k - M is odd, so |2p_k-M| ≥ 1).

Case 1: M even. Then ||s||^2 ≥ 0, and we need ||s||^2 ≤ Mn. This gives 0 ≤ Mn, trivial. Not helpful enough.

Hmm, this approach gives M ≤ 2n only when we use a stronger bound. Let me reconsider.

Actually wait. Let me reconsider. The bound ||s||^2 ≤ Mn combined with ||s||^2 ≥ 0 doesn't give M ≤ 2n directly. Let me think again.

Let me use a different approach. Consider the matrix approach.

Let V be the M×n matrix with rows v_i. Consider G = VV^T (M×M Gram matrix). G_{ii} = n, G_{ij} ≤ 0 for i≠j.

Consider the vector e = (1,1,...,1) ∈ R^M. Then e^T G e = ||s||^2 ≤ Mn (from above). Also e^T G e = Σ_{ij} G_{ij} = Mn + 2Σ_{i<j}G_{ij}.

Hmm, I need a better approach for the exact bound.

Let me look at this from the Plotkin bound perspective more carefully.

The Plotkin bound for binary codes: If d is the minimum distance and 2d > n, then M ≤ 2⌊d/(2d-n)⌋. 

For d = n/2, 2d = n, so 2d - n = 0, and the bound is infinite (doesn't apply). So we need the "d = n/2" special case.

The result for d = n/2: The maximum size of a binary code of length n with minimum distance n/2 is:
- 2n if there exists a Hadamard matrix of order n (and n > 2... actually need n divisible by 4 or n ∈ {1,2}).
- Otherwise, it's at most 2n, with equality iff Hadamard matrix exists.

Wait, actually I need to be careful. Let me reconsider.

For n = 2^2005, which is divisible by 4 (since 2005 ≥ 2), Hadamard matrix of order 2^2005 exists (Sylvester construction). So the answer should be 2n = 2^2006.

But wait, I need to double check that the maximum is exactly 2n and prove it.

Let me prove the upper bound M ≤ 2n for ±1 vectors with pairwise inner product ≤ 0.

Here's a clean proof:

Consider v_1, ..., v_M ∈ {±1}^n with ⟨v_i, v_j⟩ ≤ 0 for i ≠ j.

We want to show M ≤ 2n.

Consider the 2M vectors {v_1, ..., v_M, -v_1, ..., -v_M} (with duplicates removed if any). Actually, let me think about whether there can be duplicates. If v_i = v_j for i≠j, then ⟨v_i,v_j⟩ = n > 0, contradiction. So all v_i are distinct. If v_i = -v_j for i≠j, that's allowed (inner product -n). So the set {v_i} ∪ {-v_i} might have fewer than 2M elements. Let's say there are t pairs (i,j) with v_i = -v_j. Then the set has 2M - t elements... this is getting complicated.

Let me use a different, cleaner approach.

Approach via linear algebra / the "Rankin bound" or direct:

Consider the M vectors in {±1}^n. Augment each vector with a leading 1: u_i = (1, v_i) ∈ {±1}^{n+1}. Then ⟨u_i, u_j⟩ = 1 + ⟨v_i, v_j⟩ ≤ 1 for i≠j, and = 1 + 0 = 1 if ⟨v_i,v_j⟩ = 0, or ≤ 1 in general. Actually ⟨u_i, u_j⟩ = 1 + ⟨v_i, v_j⟩. Since ⟨v_i, v_j⟩ ≤ 0, we have ⟨u_i, u_j⟩ ≤ 1 = ⟨u_i, u_i⟩/(n+1) · ... hmm this isn't leading anywhere clean.

Let me try the direct approach that I think works:

Claim: M ≤ 2n.

Proof: Consider the M×n matrix V with entries ±1. Let's compute the rank.

Consider the matrix G = VV^T. G is M×M, G_{ii} = n, G_{ij} ≤ 0 for i≠j.

Consider G + nI... no. Let me think about G's eigenvalues or use a trace argument.

Actually, here's a classic approach:

Consider the matrix H = V^T V (n×n matrix). trace(H) = Σ_i Σ_j V_{ij}^2 = Mn. Also H = Σ_i v_i v_i^T (sum of rank-1 matrices). rank(H) ≤ M. Also rank(H) ≤ n. So rank(H) ≤ min(M, n).

Hmm, that gives M ≥ rank but not an upper bound.

Let me try yet another approach. The key inequality:

We have ||s||^2 = Σ_k (2p_k - M)^2 ≤ Mn where s = Σ v_i.

Now, (2p_k - M)^2 ≡ M^2 (mod 4) since 2p_k is even... no. 2p_k - M: if M even, 2p_k - M is even, so (2p_k-M)^2 ≡ 0 (mod 4). If M odd, 2p_k - M is odd, (2p_k - M)^2 ≡ 1 (mod 4), and ≥ 1.

Case M odd: ||s||^2 = Σ_k (2p_k - M)^2 ≥ n·1 = n. Combined with ||s||^2 ≤ Mn, we get n ≤ Mn, i.e., M ≥ 1. Trivial.

This isn't giving M ≤ 2n. Let me reconsider.

Oh wait, I think I'm confusing myself. Let me reconsider the problem. The condition is "at most half of their corresponding digits are the same." So agreements ≤ n/2. In ±1 representation, agreements = (n + ⟨v_i, v_j⟩)/2. So agreements ≤ n/2 ⟺ (n + ⟨v_i,v_j⟩)/2 ≤ n/2 ⟺ ⟨v_i, v_j⟩ ≤ 0. Yes, that's what I had.

Now for the upper bound. Let me think about the Plotkin bound proof that gives 2n.

Actually, I recall now. The relevant bound is:

For a binary code of length n with minimum distance d = n/2, the maximum size is at most 2n, and this is achieved by the Hadamard code when a Hadamard matrix of order n exists.

The proof of the upper bound 2n:

Let the code be C = {c_1, ..., c_M} ⊂ {0,1}^n with d(c_i, c_j) ≥ n/2 for i≠j.

Consider the M codewords. For each coordinate k, let a_k = number of codewords with a 1 in position k. The total number of "1"s is Σ_k a_k. 

The sum of pairwise distances: Σ_{i<j} d(c_i, c_j) = Σ_{k=1}^n a_k(M - a_k).

(This is because for each coordinate k, the number of pairs that differ in position k is a_k(M - a_k).)

Since each d(c_i, c_j) ≥ n/2, we have:
Σ_{i<j} d(c_i, c_j) ≥ (n/2) · C(M,2) = (n/2) · M(M-1)/2 = nM(M-1)/4.

Also, Σ_k a_k(M - a_k) ≤ Σ_k (M/2)^2 = n · M^2/4 (since a_k(M-a_k) ≤ M^2/4 by AM-GM, max at a_k = M/2).

So: nM(M-1)/4 ≤ Σ_k a_k(M-a_k) ≤ nM^2/4.

From the left inequality: nM(M-1)/4 ≤ nM^2/4, which gives M-1 ≤ M, trivial.

Hmm, this gives the bound but not M ≤ 2n. Let me reconsider.

Oh, I see. The bound Σ_k a_k(M-a_k) ≤ nM^2/4 is an equality when a_k = M/2 for all k. And the lower bound nM(M-1)/4 is an equality when all distances are exactly n/2.

So combining: nM(M-1)/4 ≤ nM^2/4, i.e., M(M-1) ≤ M^2, i.e., -M ≤ 0. Trivial. So this approach doesn't give M ≤ 2n either!

So maybe the maximum is NOT 2n? Let me reconsider.

Hmm wait. Let me reconsider with small cases.

n = 2 (2^1): We found M = 4 = 2n. ✓
n = 4 (2^2): Hadamard matrix of order 4 exists. Hadamard code gives 2·4 = 8 codewords with min distance 2 = n/2. Can we do better than 8?

Let me check: can we have 9 or more binary vectors of length 4 with pairwise distance ≥ 2?

Total vectors in {0,1}^4 = 16. We need pairwise distance ≥ 2. 

The maximum code of length 4 with min distance 2: This is A(4,2). A(n,d) is the max size of binary code of length n, min distance d.

A(4,2) = 8. (This is known: it's the extended Hamming code or just all even-weight vectors, which gives 8.)

Wait, all even-weight vectors of length 4: there are 8 of them (half of 16). Any two even-weight vectors: their distance is even, and if distinct, distance ≥ 2. Yes! So A(4,2) = 8 = 2·4. ✓

n = 8 (2^3): A(8,4) = ? Min distance 4 = n/2. The Hadamard code gives 16 = 2·8. Is A(8,4) = 16?

Actually, A(8,4) = 20 is known! Wait, let me recall. The extended Hamming code [8,4,4] has 16 codewords. But can we do better?

Hmm, actually A(8,4) = 20. Let me verify. The best known code of length 8, distance 4... 

From tables: A(8,4) = 20. Yes, this is a known value. So the maximum is 20, not 16 = 2n!

Wait, that contradicts my earlier reasoning. Let me re-examine.

If A(8,4) = 20 > 16 = 2·8, then the maximum is NOT 2n in general!

Hmm, but wait. Let me double-check A(8,4). 

Actually, I need to be more careful. Let me look this up in my memory.

The values A(n,d) for small n:
A(8,4) = 20.

Yes, this is a well-known value. The (8,20,4) code exists. So for n=8, the answer would be 20, not 16.

But wait, the problem asks for n = 2^2005, which is huge. And the answer should be a clean number. Let me reconsider.

Hmm, but if A(8,4) = 20, then for n = 2^2005 the answer isn't simply 2n. Let me reconsider the problem.

Wait, actually, let me re-examine A(8,4). 

The Plotkin bound: for d = n/2 = 4, n = 8. The Plotkin bound when 2d = n... 

Actually, I think I need to be more careful about the Plotkin bound. Let me recall it properly.

Plotkin bound: For a binary (n, M, d) code:
- If d is even and 2d > n: M ≤ 2⌊d/(2d-n)⌋
- If d is odd and 2d+1 > n: M ≤ 2⌊(d+1)/(2d+1-n)⌋
- If d = n/2 (n even, d even): M ≤ 2n (this is the boundary case)
- If d = (n+1)/2 (n odd, d odd): M ≤ 2(n+1) ... 

Hmm wait, but A(8,4) = 20 > 16 = 2·8. So the Plotkin bound M ≤ 2n for d = n/2 must be wrong, or A(8,4) ≠ 20.

Let me re-examine. Let me carefully reconsider A(8,4).

Actually, I might be misremembering. Let me think about it from scratch.

For n=8, d=4: We need binary vectors of length 8 with pairwise Hamming distance ≥ 4.

The extended Hamming code [8,4,4] has 2^4 = 16 codewords, all with pairwise distance ≥ 4 (actually exactly 4 for most pairs, since it's a linear code with minimum distance 4).

Can we add more? The extended Hamming code consists of all vectors x ∈ {0,1}^8 such that Hx = 0 where H is the 4×8 parity check matrix. There are 16 such vectors. The remaining 240 - 16 = 240... wait, 2^8 = 256 total, 256 - 16 = 240 non-codeword vectors.

Can we add any of these to the code while maintaining min distance 4? A vector y not in the code has syndrome Hy ≠ 0. The distance from y to any codeword c is the weight of y - c (in binary, y + c). Since the code is linear, {y + c : c ∈ code} = y + code, which is a coset. The minimum weight in this coset is the minimum distance from y to the code. For the extended Hamming code, the coset leaders have weights 0,1,2 (the covering radius is 2). So any non-codeword y has distance ≤ 2 from some codeword, meaning distance < 4. So we can't add any vector to the [8,4,4] code.

But can we find a completely different code of size > 16?

Let me think about A(8,4) more carefully. 

From the Plotkin bound: For n=8, d=4, 2d = n = 8. The Plotkin bound in this boundary case...

Let me look at this more carefully. The general Plotkin bound proof:

Σ_{i<j} d(c_i,c_j) = Σ_k a_k(M - a_k) ≤ n · (M/2)^2 = nM^2/4 (when M even, a_k = M/2 optimal; when M odd, a_k = (M±1)/2, giving a_k(M-a_k) = (M^2-1)/4).

Also Σ_{i<j} d(c_i,c_j) ≥ d · C(M,2) = dM(M-1)/2.

Case M even: dM(M-1)/2 ≤ nM^2/4, so d(M-1) ≤ nM/2, so 2d(M-1) ≤ nM, so M(2d - n) ≤ 2d, so M ≤ 2d/(2d-n) when 2d > n.

For d = n/2: 2d - n = 0, so this gives M · 0 ≤ 2d = n, i.e., 0 ≤ n. Trivial. No bound!

Case M odd: dM(M-1)/2 ≤ n(M^2-1)/4, so 2dM(M-1) ≤ n(M^2-1) = n(M-1)(M+1), so 2dM ≤ n(M+1), so M(2d-n) ≤ n, so M ≤ n/(2d-n) when 2d > n.

For d = n/2: M · 0 ≤ n, trivial again.

So the Plotkin bound gives NO useful bound when d = n/2 exactly. That means M could potentially be larger than 2n.

So my earlier claim that M ≤ 2n was wrong! Let me reconsider.

OK so for d = n/2, the Plotkin bound doesn't bound M. So what's the actual maximum?

Let me reconsider A(8,4). I'll try to verify whether it's 16 or 20.

Actually, I now recall more carefully: A(8,4) = 20. This is indeed a known result. The code is constructed from the Nordstrom-Robinson code or similar. Wait, the Nordstrom-Robinson code has parameters (16, 256, 6). 

Let me think again. A(8,4): 

From the table of best known codes:
- A(1,1) = 2
- A(2,1) = 4
- A(3,2) = 4
- A(4,2) = 8
- A(5,3) = 4
- A(6,3) = 8
- A(7,4) = 8
- A(8,4) = 16
- A(9,4) = 20
- A(10,5) = 40
- ...

Hmm, wait. Let me reconsider. I think A(8,4) = 16, not 20. Let me re-derive.

For n=8, d=4: We showed the [8,4,4] extended Hamming code gives 16, and we can't add to it. But could a non-linear code be bigger?

Let me use the Plotkin bound more carefully. For d = n/2 with n = 8, d = 4:

If M is odd: from above, M(2d-n) ≤ n gives 0 ≤ 8, trivial.
If M is even: M(2d-n) ≤ 2d gives 0 ≤ 8, trivial.

So Plotkin doesn't help. Let me try another bound.

The Elias-Bassalygo bound or the linear programming bound?

Actually, let me just try to construct a code of size 20 for n=8, d=4, or prove it can't be done.

Hmm, this is getting complicated. Let me reconsider the problem.

Actually, wait. Let me re-read the problem statement. "among any two chosen integers, at most half of their corresponding digits are the same." 

So we need: for any two chosen integers, the number of positions where they have the same digit is at most n/2 = 2^2004.

This is exactly the condition that the Hamming distance is at least n/2, i.e., d ≥ n/2. And we want the maximum number of such integers.

Hmm, but actually, re-reading: "Determine the number of positive integers..." — I think the problem is asking for the maximum number of such integers that can be chosen. So it's asking for A(n, n/2) where n = 2^2005.

Wait, but actually, re-reading again: "Determine the number of positive integers, each with exactly 2^2005 digits, where each digit is either 7 or 8, such that among any two chosen integers, at most half of their corresponding digits are the same."

I think this is asking: what is the maximum number of such integers that can be chosen (i.e., the maximum size of a set of such integers with the given property)?

So the answer is A(2^2005, 2^2004) — the maximum size of a binary code of length 2^2005 with minimum distance 2^2004.

Now, for this specific case where n = 2^2005 and d = n/2 = 2^2004, what is A(n, n/2)?

Let me think about this more carefully. The key special structure here is that n is a power of 2.

For n a power of 2, the Hadamard matrix of order n exists (Sylvester construction). The Hadamard code gives 2n codewords with minimum distance n/2.

But can we do better? From the A(8,4) question: if A(8,4) = 16 = 2·8, then for n = 8 (a power of 2), the Hadamard code is optimal. Let me verify this.

Actually, I think I was wrong about A(8,4) = 20. Let me reconsider.

From MacWilliams and Sloane, or standard coding theory tables:

A(8,4) = 16. The extended Hamming code achieves this.

Wait, but I've also seen A(9,4) = 20. Let me be careful.

The standard table (from Brouwer's tables or similar):
A(8,4) = 16
A(9,4) = 20
A(10,4) = 40
A(11,4) = 72
...

Hmm, but A(10,4) = 40? That seems like a lot. With n=10, d=4, the Plotkin bound for d < n/2 doesn't apply (since 2d = 8 < 10 = n). So for d < n/2, we can have much larger codes.

For d = n/2 exactly: A(4,2) = 8 = 2·4, A(8,4) = 16 = 2·8. 

Let me check A(2,1) = 4 = 2·2. ✓ (All 4 binary vectors of length 2 have pairwise distance ≥ 1.)

A(6,3): n=6, d=3 = n/2. Is A(6,3) = 12 = 2·6? 

Hmm, but 6 is not a power of 2, and Hadamard matrix of order 6 doesn't exist. So the Hadamard code construction doesn't directly work. But maybe another construction gives 12?

Actually, for n=6, d=3: I recall A(6,3) = 8. Wait, that doesn't match 2n = 12.

Hmm, let me reconsider. Maybe the answer 2n only works when n is a power of 2 (Hadamard matrix exists), and the problem specifically chose n = 2^2005 for this reason.

Let me reconsider A(6,3). With n=6, d=3:
- The Plotkin bound: 2d = 6 = n, so no bound from Plotkin.
- Best known: A(6,3) = 8? Or is it larger?

Actually, I think A(6,3) = 8. Let me try to verify. 

Hmm, actually I recall that A(6,3) = 8 might not be right either. Let me think about it differently.

For the problem at hand, n = 2^2005 is a power of 2, so Hadamard matrices exist. The question is whether A(2^k, 2^{k-1}) = 2^{k+1} = 2n.

Let me verify for small powers of 2:
- n=2 (k=1): A(2,1) = 4 = 2·2 ✓
- n=4 (k=2): A(4,2) = 8 = 2·4 ✓
- n=8 (k=3): A(8,4) = 16 = 2·8 ✓ (I'll assume this is correct)

So the pattern suggests A(2^k, 2^{k-1}) = 2^{k+1}.

Now I need to prove that A(n, n/2) ≤ 2n when n is a power of 2 (or more generally, when a Hadamard matrix of order n exists).

Actually, I think the bound A(n, n/2) ≤ 2n holds for ALL even n, not just powers of 2. Let me try to prove it.

Hmm, but A(6,3) — if it's 8 < 12 = 2·6, then the bound 2n is not tight for n=6, but it's still an upper bound. And for n=6, since no Hadamard matrix of order 6 exists, we can't achieve 2n. But the upper bound of 2n still holds.

Wait, but does A(6,3) = 8 or could it be larger? Let me think.

Actually, I just realized I should look at this more carefully. Let me try to prove A(n, n/2) ≤ 2n for all even n.

Proof attempt: Let C = {c_1, ..., c_M} be a binary code of length n with min distance ≥ n/2.

Consider the ±1 representation: v_i ∈ {±1}^n with ⟨v_i, v_j⟩ ≤ 0 for i ≠ j.

We want to show M ≤ 2n.

Consider the M vectors v_1, ..., v_M and also -v_1, ..., -v_M. 

Note: ⟨v_i, -v_j⟩ = -⟨v_i, v_j⟩ ≥ 0 for i ≠ j.

And ⟨v_i, -v_i⟩ = -n < 0.

And ⟨-v_i, -v_j⟩ = ⟨v_i, v_j⟩ ≤ 0 for i ≠ j.

So the set {v_1, ..., v_M, -v_1, ..., -v_M} = 2M vectors. Among these:
- v_i and v_j (i≠j): inner product ≤ 0
- -v_i and -v_j (i≠j): inner product ≤ 0
- v_i and -v_i: inner product = -n < 0
- v_i and -v_j (i≠j): inner product ≥ 0

Hmm, this doesn't directly help.

Let me try a different approach. 

Approach: Use the fact that the vectors are in {±1}^n and apply a volume/dimension argument.

Consider the M vectors v_1, ..., v_M ∈ {±1}^n ⊂ R^n with pairwise inner product ≤ 0.

Claim: M ≤ 2n.

Proof: Consider the vectors u_i = v_i / √n, so ||u_i|| = 1 and ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

These are unit vectors in R^n with pairwise non-positive inner products. 

Now I use the following fact: In R^n, the maximum number of unit vectors with pairwise non-positive inner products is 2n. 

Wait, is this true? For n=2, we can have at most 4 unit vectors with pairwise ≤0 inner products? Let's see: (1,0), (0,1), (-1,0), (0,-1). Inner products: (1,0)·(0,1)=0, (1,0)·(-1,0)=-1, (1,0)·(0,-1)=0, (0,1)·(-1,0)=0, (0,1)·(0,-1)=-1, (-1,0)·(0,-1)=0. All ≤ 0. So 4 = 2·2. ✓

Can we have 5 in R^2? We'd need 5 unit vectors with pairwise ≤0 inner products. The angle between any two must be ≥ 90°. On a circle, we can fit at most 4 vectors with pairwise angles ≥ 90° (since 4 × 90° = 360°). So max is 4 = 2·2. ✓

For general R^n: The maximum number of unit vectors with pairwise angles ≥ 90° (i.e., inner products ≤ 0) is 2n. This is because:

1. We can achieve 2n: take the 2n vectors ±e_1, ..., ±e_n (standard basis and their negatives). Pairwise inner products: e_i · e_j = 0 (i≠j), e_i · (-e_i) = -1, e_i · (-e_j) = 0 (i≠j). All ≤ 0. So 2n vectors. ✓

2. Upper bound: We need to show we can't have more than 2n.

For the upper bound, here's an argument:

Let u_1, ..., u_M be unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

Consider the Gram matrix G (M×M) with G_{ii} = 1, G_{ij} ≤ 0 for i≠j.

G is positive semidefinite (it's a Gram matrix), so all eigenvalues ≥ 0.

Consider G + I (add identity): (G+I)_{ii} = 2, (G+I)_{ij} = G_{ij} ≤ 0. 

Hmm, this is a Z-matrix (off-diagonal ≤ 0) with positive diagonal. If it's also positive semidefinite...

Actually, let me use a different argument. 

Consider the matrix G. trace(G) = M. The eigenvalues of G are λ_1, ..., λ_M ≥ 0 with Σ λ_i = M.

Also, G is PSD with rank ≤ n (since the vectors are in R^n). So at most n eigenvalues are nonzero. Thus at least M - n eigenvalues are 0.

Now, consider e = (1,1,...,1) ∈ R^M. e^T G e = ||Σ u_i||^2 ≥ 0.

Also, e^T G e = Σ_{ij} G_{ij} = M + 2Σ_{i<j} G_{ij} ≤ M (since G_{ij} ≤ 0).

So 0 ≤ e^T G e ≤ M.

Hmm, this gives ||Σ u_i||^2 ≤ M, i.e., ||Σ u_i|| ≤ √M. Not directly useful for bounding M.

Let me try another approach for the upper bound.

Alternative approach: Suppose M > 2n. We want a contradiction.

The vectors u_1, ..., u_M are in R^n, so they're linearly dependent if M > n. In fact, since rank(G) ≤ n, if M > n, there's a nontrivial linear dependence.

Let me think about this differently. 

Here's a cleaner approach I recall:

Theorem (Danzer-Grünbaum / Rankin): The maximum number of points on the unit sphere S^{n-1} such that the angle between any two is at least π/2 is 2n, achieved by the vertices of a cross-polytope (±e_i).

Proof of upper bound: 

Let u_1, ..., u_M be unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

Consider the convex hull P = conv{u_1, ..., u_M}. 

Actually, here's a proof using linear programming / the "simplex bound" idea:

Consider the matrix A = [u_1 | u_2 | ... | u_M] (n × M matrix). Then A^T A = G (the Gram matrix).

Consider AA^T = Σ_{i=1}^M u_i u_i^T (n × n matrix). trace(AA^T) = Σ ||u_i||^2 = M.

Now, for any unit vector x: x^T (AA^T) x = Σ (x^T u_i)^2 = ||A^T x||^2.

Hmm, let me try the approach via the inequality on the Gram matrix more carefully.

We have G PSD, G_{ii} = 1, G_{ij} ≤ 0 (i≠j), rank(G) ≤ n.

Consider the vector e = (1,...,1) ∈ R^M. 

e^T G e = M + 2Σ_{i<j} G_{ij} ≥ 0 (since G is PSD).

So Σ_{i<j} G_{ij} ≥ -M/2.

Now, consider G e = (G_{·1} + ... + G_{·M})... the vector whose i-th entry is Σ_j G_{ij} = 1 + Σ_{j≠i} G_{ij}.

Let s_i = Σ_{j≠i} G_{ij} ≤ 0 (sum of non-positive terms). Then (Ge)_i = 1 + s_i.

e^T G e = Σ_i (1 + s_i) = M + Σ_i s_i ≥ 0, so Σ_i s_i ≥ -M.

Now, consider e^T G^2 e = ||Ge||^2 = Σ_i (1+s_i)^2.

Also, e^T G^2 e = (Ge)^T (Ge) = ... 

And by Cauchy-Schwarz or the PSD property: 

Hmm, let me try yet another approach.

Actually, I think the cleanest proof uses the following:

Lemma: If G is an M×M PSD matrix with G_{ii} = 1 and G_{ij} ≤ 0 for i ≠ j, then M ≤ 2·rank(G).

Proof: Consider G. Since G is PSD, we can write G = B^T B for some matrix B. The columns of B are vectors b_1, ..., b_M with ||b_i||^2 = G_{ii} = 1 and b_i^T b_j = G_{ij} ≤ 0.

Now consider the matrix H = 2I - G. H_{ii} = 1, H_{ij} = -G_{ij} ≥ 0 for i≠j.

H is a nonnegative matrix. Also, H = 2I - G. 

The eigenvalues of H are 2 - λ_i where λ_i are eigenvalues of G. Since G is PSD, λ_i ≥ 0, so eigenvalues of H are ≤ 2. Also, since rank(G) ≤ n, at least M - n eigenvalues of G are 0, so at least M - n eigenvalues of H are 2.

Now, H is a nonneg matrix. By Perron-Frobenius, the spectral radius ρ(H) ≤ max_i Σ_j H_{ij} = max_i (1 + Σ_{j≠i} (-G_{ij})) = max_i (1 - s_i) where s_i = Σ_{j≠i} G_{ij} ≤ 0.

So ρ(H) ≤ max_i (1 - s_i) = 1 - min_i s_i = 1 + max_i (-s_i).

Hmm, this is getting complicated. Let me try a more direct approach.

Direct proof that M ≤ 2n:

Let u_1, ..., u_M be unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

Step 1: Show that any subset of these vectors is linearly independent if it has the property that... no.

Step 2: Use the following. Consider the 2M vectors u_1, ..., u_M, -u_1, ..., -u_M. Note that ⟨u_i, -u_i⟩ = -1 and for i ≠ j, ⟨u_i, -u_j⟩ = -⟨u_i, u_j⟩ ≥ 0.

Hmm, that doesn't help directly.

Let me try the approach from the theory of spherical codes.

The Rankin bound states: For a spherical code in S^{n-1} with minimum angle φ:
- If φ > π/2, then M ≤ n+1 (simplex bound).
- If φ = π/2, then M ≤ 2n.
- If φ < π/2, larger codes are possible.

The case φ = π/2 (inner product ≤ 0) gives M ≤ 2n. This is exactly our situation!

The proof of the Rankin bound for φ = π/2:

Let u_1, ..., u_M be unit vectors with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

Consider the matrix U = [u_1 ... u_M] (n × M). The Gram matrix G = U^T U is M × M, PSD, rank ≤ n.

G_{ii} = 1, G_{ij} ≤ 0 for i ≠ j.

Now consider the matrix J = ee^T (all-ones matrix, M × M). 

Consider G + J. (G+J)_{ii} = 1 + 1 = 2, (G+J)_{ij} = G_{ij} + 1 ≤ 1 for i ≠ j (since G_{ij} ≤ 0).

Hmm, not sure this helps.

Let me try the standard proof:

Consider the sum S = Σ_{i=1}^M u_i. Then:
||S||^2 = M + 2Σ_{i<j} ⟨u_i, u_j⟩ ≤ M (since ⟨u_i, u_j⟩ ≤ 0).

Also, consider the matrix T = Σ_{i=1}^M u_i u_i^T (n × n). This is PSD with trace(T) = M.

For any unit vector x: x^T T x = Σ (x^T u_i)^2 ≥ 0.

Now, consider tr(T^2) = Σ_{i,j} (u_i^T u_j)^2 = Σ_i ||u_i||^4 + 2Σ_{i<j} (u_i^T u_j)^2 = M + 2Σ_{i<j} G_{ij}^2.

Also, tr(T^2) = Σ_{k=1}^n λ_k^2 where λ_k are eigenvalues of T, and Σ λ_k = tr(T) = M, λ_k ≥ 0.

By Cauchy-Schwarz: (Σ λ_k)^2 ≤ n · Σ λ_k^2, so M^2 ≤ n · tr(T^2) = n(M + 2Σ_{i<j} G_{ij}^2).

So M^2/n ≤ M + 2Σ_{i<j} G_{ij}^2.

This gives 2Σ_{i<j} G_{ij}^2 ≥ M^2/n - M = M(M-n)/n.

If M > n, the RHS is positive, so this is a constraint but doesn't directly bound M.

Hmm. Let me try a completely different approach.

OK let me look up the actual proof of the Rankin bound for φ = π/2.

The Rankin bound for φ = π/2 (M ≤ 2n):

Proof: Let u_1, ..., u_M be unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

We use the following approach. Consider the M vectors. We'll show that M ≤ 2n.

Key idea: The vectors u_1, ..., u_M are the vertices of a set on the sphere where all pairwise angles are ≥ π/2. 

Consider the hyperplanes H_{ij} = {x : ⟨x, u_i - u_j⟩ = 0} for i ≠ j. Actually, let me think about this differently.

Here's a proof I think works:

Consider the matrix G (Gram matrix, M × M, PSD, rank ≤ n, G_{ii} = 1, G_{ij} ≤ 0).

Since G is PSD with rank ≤ n, we can find vectors u_i in R^n. 

Now, consider the matrix A = G - I. A_{ii} = 0, A_{ij} = G_{ij} ≤ 0 for i ≠ j. A has rank ≤ n (since G has rank ≤ n, and subtracting I doesn't increase rank beyond max(rank(G), M) = M... actually rank(A) could be up to M).

Hmm, that's not right. A = G - I. rank(A) ≤ rank(G) + rank(I) = n + M, which is trivial.

Let me try yet another approach.

Approach via "kissing number" or direct combinatorial argument:

Actually, I think the proof goes like this:

Theorem: Let u_1, ..., u_M be unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for all i ≠ j. Then M ≤ 2n.

Proof: We proceed by induction on n.

Base case n = 1: Unit vectors in R^1 are ±1. We can have at most 2 = 2·1 with ⟨u_i, u_j⟩ ≤ 0 (namely +1 and -1, with inner product -1 ≤ 0). ✓

Inductive step: Assume the result for R^{n-1}. Consider M unit vectors in R^n with pairwise ≤0 inner products.

If M = 0 or 1, trivial. Assume M ≥ 2.

Pick any two vectors, say u_1 and u_2. Since ⟨u_1, u_2⟩ ≤ 0, the angle between them is ≥ π/2.

Consider the hyperplane H perpendicular to u_1 + u_2 (if u_1 + u_2 ≠ 0) or... hmm, this induction is tricky.

Let me try a different proof.

Proof using linear algebra (the "2n" bound):

Consider the M unit vectors u_1, ..., u_M ∈ R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

Define f_i = u_i for i = 1, ..., M. These are M vectors in R^n.

Consider also the "complementary" structure. 

Actually, here's a clean proof I found in my memory:

Proof: Consider the M × M Gram matrix G. G is PSD, rank(G) ≤ n, G_{ii} = 1, G_{ij} ≤ 0 for i ≠ j.

Consider the matrix B = 2I - G. Then:
- B_{ii} = 1
- B_{ij} = -G_{ij} ≥ 0 for i ≠ j
- B is symmetric
- Eigenvalues of B: 2 - λ_i where λ_i are eigenvalues of G. Since G is PSD, λ_i ≥ 0, so eigenvalues of B are ≤ 2. Since rank(G) ≤ n, at least M - n eigenvalues of G are 0, so at least M - n eigenvalues of B equal 2.

Now, B is a symmetric matrix with nonneg off-diagonal entries. 

Consider the vector e = (1,...,1). Then:
Be = (2I - G)e = 2e - Ge.

(Ge)_i = Σ_j G_{ij} = 1 + Σ_{j≠i} G_{ij} = 1 + s_i where s_i ≤ 0.

So (Be)_i = 2 - (1 + s_i) = 1 - s_i ≥ 1 (since s_i ≤ 0).

So Be ≥ e (componentwise), meaning each entry of Be is ≥ 1.

Now, B has at least M - n eigenvalues equal to 2. The remaining at most n eigenvalues are 2 - λ_i where λ_i > 0 are the positive eigenvalues of G.

By the spectral theorem, since B is symmetric:
e^T B e = Σ_i (Be)_i = Σ_i (1 - s_i) = M - Σ_i s_i.

Also, e^T B e = Σ_k μ_k (c_k)^2 where μ_k are eigenvalues of B and c_k are the components of e in the eigenbasis.

Hmm, this is getting complicated. Let me try to use the fact that B has at least M-n eigenvalues equal to 2 and all eigenvalues ≤ 2.

Since B is symmetric with all eigenvalues ≤ 2, we have B ≤ 2I (in the PSD sense, i.e., 2I - B = G ≥ 0, which we already know).

Now, consider e^T B e. Since B ≤ 2I, e^T B e ≤ 2 e^T e = 2M.

Also, e^T B e = M - Σ_i s_i ≥ M (since s_i ≤ 0, so -Σ s_i ≥ 0).

So M ≤ e^T B e ≤ 2M. This gives 1 ≤ 2, trivial.

Hmm, I'm going in circles. Let me try a completely different strategy.

Let me try the approach using the fact that the vectors are in {±1}^n (not just unit vectors), which is more restrictive.

Since v_i ∈ {±1}^n, the inner products ⟨v_i, v_j⟩ are even integers (for n even) ranging from -n to n. The condition ⟨v_i, v_j⟩ ≤ 0 means ⟨v_i, v_j⟩ ∈ {-n, -n+2, ..., 0}.

Hmm, let me try to use the specific structure of ±1 vectors.

Actually, let me try a proof by contradiction. Suppose M > 2n. 

Consider the n × M matrix V whose columns are v_1, ..., v_M (each in {±1}^n).

Consider VV^T = Σ_{i=1}^M v_i v_i^T (n × n matrix). 

trace(VV^T) = Σ_i ||v_i||^2 = Mn.

(VV^T)_{kl} = Σ_i v_i(k) v_i(l).

Now consider (VV^T)^2. trace((VV^T)^2) = Σ_{k,l} (VV^T)_{kl}^2 = Σ_{k,l} (Σ_i v_i(k) v_i(l))^2.

Also, trace((VV^T)^2) = Σ_{i,j} (v_i^T v_j)^2 = Σ_{i,j} ⟨v_i, v_j⟩^2 = Σ_i n^2 + 2Σ_{i<j} ⟨v_i,v_j⟩^2 = Mn^2 + 2Σ_{i<j} ⟨v_i,v_j⟩^2.

By the eigenvalue bound: trace((VV^T)^2) = Σ_k λ_k^2 where λ_k are eigenvalues of VV^T, Σ_k λ_k = Mn, λ_k ≥ 0, and there are n eigenvalues.

By Cauchy-Schwarz: (Σ λ_k)^2 ≤ n · Σ λ_k^2, so (Mn)^2 ≤ n · trace((VV^T)^2).

So trace((VV^T)^2) ≥ M^2 n.

But also trace((VV^T)^2) = Mn^2 + 2Σ_{i<j} ⟨v_i,v_j⟩^2.

Now, ⟨v_i, v_j⟩ ≤ 0 and ⟨v_i, v_j⟩ ≡ 0 (mod 2) (since both are ±1 vectors of length n, inner product has same parity as n; n = 2^2005 is even, so inner product is even). So ⟨v_i, v_j⟩ ∈ {0, -2, -4, ..., -n}.

Thus ⟨v_i, v_j⟩^2 ≥ 0, and if ⟨v_i, v_j⟩ ≠ 0, then ⟨v_i, v_j⟩^2 ≥ 4.

So: Mn^2 + 2Σ_{i<j} ⟨v_i,v_j⟩^2 ≥ M^2 n.

This gives 2Σ_{i<j} ⟨v_i,v_j⟩^2 ≥ M^2 n - Mn^2 = Mn(M - n).

If M > n, the RHS is positive. But this doesn't bound M from above; it's a lower bound on the sum of squares of inner products.

Hmm. Let me think about upper bounds on trace((VV^T)^2).

Actually, trace((VV^T)^2) = Σ_{k,l} (Σ_i v_i(k) v_i(l))^2.

For k = l: (Σ_i v_i(k)^2)^2 = (Σ_i 1)^2 = M^2. There are n such terms, contributing nM^2.

For k ≠ l: (Σ_i v_i(k) v_i(l))^2 = (Σ_i v_i(k) v_i(l))^2. Let a_{kl} = Σ_i v_i(k) v_i(l). Then a_{kl} has the same parity as M (since each v_i(k)v_i(l) ∈ {±1}, the sum has parity M mod 2). And |a_{kl}| ≤ M.

So trace((VV^T)^2) = nM^2 + Σ_{k≠l} a_{kl}^2.

Also, trace((VV^T)^2) = Mn^2 + 2Σ_{i<j} ⟨v_i,v_j⟩^2.

So: nM^2 + Σ_{k≠l} a_{kl}^2 = Mn^2 + 2Σ_{i<j} ⟨v_i,v_j⟩^2.

And from Cauchy-Schwarz: trace((VV^T)^2) ≥ M^2 n, which gives nM^2 + Σ_{k≠l} a_{kl}^2 ≥ M^2 n, i.e., Σ_{k≠l} a_{kl}^2 ≥ 0. Trivial.

I need an upper bound on trace((VV^T)^2) to get a bound on M. But trace((VV^T)^2) can be as large as... well, it depends on the structure.

Let me try a different approach entirely.

Approach: Direct proof for ±1 vectors using the "double counting" method.

Consider M vectors v_1, ..., v_M ∈ {±1}^n with ⟨v_i, v_j⟩ ≤ 0 for i ≠ j.

For each pair (i, j) with i < j, let a_{ij} = number of positions where v_i and v_j agree, and d_{ij} = number where they disagree. Then a_{ij} + d_{ij} = n and ⟨v_i, v_j⟩ = a_{ij} - d_{ij} = 2a_{ij} - n. The condition ⟨v_i, v_j⟩ ≤ 0 means a_{ij} ≤ n/2.

Now, double-count the total number of agreements across all pairs and all positions:

T = Σ_{i<j} a_{ij} = Σ_{k=1}^n C(p_k, 2) + C(M - p_k, 2)

where p_k = number of vectors with +1 in position k. (For each position k, the number of agreeing pairs is C(p_k, 2) + C(M-p_k, 2), since two vectors agree at position k iff both have +1 or both have -1.)

Wait, let me recompute. At position k, p_k vectors have +1 and M - p_k have -1. The number of pairs agreeing at position k is C(p_k, 2) + C(M - p_k, 2) = [p_k(p_k-1) + (M-p_k)(M-p_k-1)] / 2 = [p_k^2 - p_k + M^2 - 2Mp_k + p_k^2 - M + p_k] / 2 = [2p_k^2 - 2Mp_k + M^2 - M] / 2 = p_k^2 - Mp_k + (M^2 - M)/2.

So T = Σ_k [p_k^2 - Mp_k + (M^2-M)/2] = Σ_k p_k^2 - M Σ_k p_k + n(M^2-M)/2.

Let P = Σ_k p_k = total number of +1 entries = Σ_i (number of +1's in v_i). Let Q = Σ_k p_k^2.

Then T = Q - MP + n(M^2 - M)/2.

Also, T = Σ_{i<j} a_{ij} ≤ Σ_{i<j} n/2 = (n/2) · M(M-1)/2 = nM(M-1)/4.

So: Q - MP + n(M^2-M)/2 ≤ nM(M-1)/4.

Thus: Q - MP ≤ nM(M-1)/4 - n(M^2-M)/2 = nM(M-1)/4 - nM(M-1)/2 = -nM(M-1)/4.

So Q - MP ≤ -nM(M-1)/4, i.e., Q ≤ MP - nM(M-1)/4. ... (*)

Now, by Cauchy-Schwarz, Q = Σ_k p_k^2 ≥ (Σ_k p_k)^2 / n = P^2/n.

So P^2/n ≤ Q ≤ MP - nM(M-1)/4.

Thus P^2/n ≤ MP - nM(M-1)/4.

This is a quadratic in P: P^2/n - MP + nM(M-1)/4 ≤ 0.

For this quadratic in P to have a real solution, the discriminant must be ≥ 0:

M^2 - 4 · (1/n) · nM(M-1)/4 ≥ 0
M^2 - M(M-1) ≥ 0
M^2 - M^2 + M ≥ 0
M ≥ 0.

Trivial again! So this approach also doesn't give M ≤ 2n.

Hmm. So maybe the bound M ≤ 2n is NOT correct for general even n?

Let me reconsider. Maybe for ±1 vectors (not just unit vectors), the bound is different.

Wait, I showed that for n=2, M=4=2n, and for unit vectors in R^2, M≤4=2n (Rankin bound). But for ±1 vectors specifically, the constraint is tighter (vectors must be ±1, not just unit vectors), so the bound should be at most 2n, and possibly less.

But the issue is whether 2n is achievable. For n = power of 2, Hadamard matrices exist, and the Hadamard code achieves 2n. So A(2^k, 2^{k-1}) ≥ 2^{k+1}.

The question is whether A(2^k, 2^{k-1}) ≤ 2^{k+1}, i.e., whether we can't do better than 2n.

From the Rankin bound (for unit vectors, which includes ±1 vectors as a special case), M ≤ 2n. So A(n, n/2) ≤ 2n for all n. And for n = 2^k, A(n, n/2) = 2n.

But wait, I couldn't prove the Rankin bound above! Let me find the actual proof.

OK let me think about the Rankin bound proof more carefully.

Rankin bound for φ = π/2: M ≤ 2n.

I think the proof uses the following idea:

Let u_1, ..., u_M be unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

Consider the matrix G (Gram matrix). G is PSD, rank ≤ n, G_{ii} = 1, G_{ij} ≤ 0.

Key step: Consider the matrix A = G + J where J = ee^T (all ones). 

A_{ii} = 1 + 1 = 2, A_{ij} = G_{ij} + 1 for i ≠ j.

Since G_{ij} ≤ 0, A_{ij} ≤ 1. Since G_{ij} ≥ -1 (as unit vectors), A_{ij} ≥ 0.

So A is a nonneg matrix with A_{ii} = 2 and 0 ≤ A_{ij} ≤ 1 for i ≠ j.

A = G + J = G + ee^T. 

A is PSD (sum of two PSD matrices). rank(A) ≤ rank(G) + rank(J) ≤ n + 1.

Now, A is PSD with rank ≤ n + 1. So A has at most n + 1 positive eigenvalues and at least M - (n+1) zero eigenvalues.

Also, trace(A) = trace(G) + trace(J) = M + M = 2M.

The sum of eigenvalues = 2M, and at most n+1 are positive.

By the AM-QM inequality or just the fact that eigenvalues are nonneg:
(Σ λ_i)^2 ≤ k · Σ λ_i^2 where k = number of positive eigenvalues ≤ n+1.

So (2M)^2 ≤ (n+1) · trace(A^2).

trace(A^2) = trace((G+J)^2) = trace(G^2) + 2trace(GJ) + trace(J^2).

trace(G^2) = Σ_{ij} G_{ij}^2 = M + 2Σ_{i<j} G_{ij}^2 ≤ M + 2Σ_{i<j} 1 = M + M(M-1) = M^2 (since |G_{ij}| ≤ 1).

trace(GJ) = trace(Gee^T) = e^T Ge = Σ_{ij} G_{ij} = M + 2Σ_{i<j} G_{ij} ≤ M (since G_{ij} ≤ 0).

trace(J^2) = trace(ee^T ee^T) = (e^T e)^2 = M^2.

So trace(A^2) ≤ M^2 + 2M + M^2 = 2M^2 + 2M.

Thus (2M)^2 ≤ (n+1)(2M^2 + 2M), so 4M^2 ≤ (n+1) · 2M(M+1) = 2(n+1)M(M+1).

So 4M ≤ 2(n+1)(M+1), i.e., 2M ≤ (n+1)(M+1) = (n+1)M + (n+1).

So 2M - (n+1)M ≤ n+1, i.e., M(2 - n - 1) ≤ n+1, i.e., M(1 - n) ≤ n+1.

For n ≥ 2: 1 - n < 0, so M ≥ (n+1)/(n-1). This is a lower bound, not upper bound! 

So this approach gives a lower bound, not useful.

Hmm. I must be doing something wrong. Let me reconsider.

Actually, I think the issue is that I need a LOWER bound on trace(A^2), not an upper bound, to get an upper bound on M.

Wait no. We have (2M)^2 ≤ (n+1) · trace(A^2), so trace(A^2) ≥ 4M^2/(n+1). This is a lower bound on trace(A^2). To get a contradiction (or bound on M), I need trace(A^2) to also be ≤ something in terms of M and n, and then combine.

But trace(A^2) ≤ 2M^2 + 2M (from above). So:
4M^2/(n+1) ≤ trace(A^2) ≤ 2M^2 + 2M.

From 4M^2/(n+1) ≤ 2M^2 + 2M:
4M^2 ≤ (n+1)(2M^2 + 2M) = 2(n+1)M(M+1).
4M ≤ 2(n+1)(M+1).
2M ≤ (n+1)(M+1) = (n+1)M + n + 1.
2M - (n+1)M ≤ n + 1.
M(2 - n - 1) ≤ n + 1.
M(1 - n) ≤ n + 1.

For n > 1: M ≥ (n+1)/(n-1). Lower bound. Useless.

So this approach doesn't work for getting M ≤ 2n. 

Hmm, I'm stuck. Let me reconsider whether the bound M ≤ 2n is actually correct.

Let me check: is A(8,4) = 16 or 20?

I'll try to construct a code of size 17 for n=8, d=4, or convince myself it's impossible.

Actually, let me look at this from the LP bound perspective. The Delsarte linear programming bound for A(8,4):

The LP bound is the solution to:
maximize Σ_{k=0}^n A_k
subject to:
A_0 = 1, A_k ≥ 0,
Σ_{k=0}^n A_k K_k(i) ≥ 0 for i = 0, ..., n (where K_k are Krawtchouk polynomials)

For n=8, d=4: A_k = 0 for 1 ≤ k ≤ 3.

The LP bound for A(8,4) is known to be 16 (I'm fairly confident). Actually, let me think...

Hmm, I recall that for the extended Hamming code [8,4,4], the code has 16 codewords, and the LP bound confirms A(8,4) = 16. But I also have a nagging memory of A(8,4) = 20.

Let me try to resolve this by trying to construct a (8, 20, 4) code.

Actually, I think I was confusing A(8,4) with A(9,4) or A(10,4). Let me be more careful.

From the table of A(n,d) (Brouwer's table):
- A(8,4) = 16
- A(9,4) = 20
- A(10,4) = 40
- A(11,4) = 72

Yes, I think A(8,4) = 16 is correct. The (9,20,4) code exists but not (8,20,4).

OK so with A(8,4) = 16 = 2·8, the pattern A(2^k, 2^{k-1}) = 2^{k+1} holds for k = 1, 2, 3.

Now I need to prove the upper bound A(n, n/2) ≤ 2n. Let me find the right proof.

Actually, I just realized: the Rankin bound IS a well-known result, and it does state M ≤ 2n for unit vectors with pairwise nonpositive inner products. Let me find the correct proof.

Here's the proof I think works:

Theorem (Rankin): Let u_1, ..., u_M be unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for all i ≠ j. Then M ≤ 2n.

Proof: 

Consider the Gram matrix G (M×M), PSD, rank ≤ n, G_{ii} = 1, G_{ij} ≤ 0 for i ≠ j.

Since G is PSD with rank ≤ n, we can write G = X^T X where X is n × M (columns are the vectors u_i).

Now consider the matrix G' obtained by replacing each off-diagonal entry G_{ij} with |G_{ij}| = -G_{ij} (since G_{ij} ≤ 0). So G' = 2I - G (diagonal: 2-1=1, off-diagonal: -G_{ij} = |G_{ij}| ≥ 0).

Wait, G'_{ii} = 1, G'_{ij} = |G_{ij}| = -G_{ij} ≥ 0. So G' = I + (I - G) = 2I - G.

G' = 2I - G. Since G is PSD with eigenvalues in [0, n] (actually eigenvalues of G are ≤ M but also ≤ n·max eigenvalue... hmm, eigenvalues of G are ≤ trace(G) = M, and there are at most n nonzero ones).

Eigenvalues of G' = 2 - λ_i where λ_i are eigenvalues of G. Since G is PSD, λ_i ≥ 0, so eigenvalues of G' ≤ 2. Since rank(G) ≤ n, at least M - n eigenvalues of G are 0, so at least M - n eigenvalues of G' are 2.

Now, G' is a nonneg matrix (all entries ≥ 0). By Perron-Frobenius, the spectral radius ρ(G') is an eigenvalue, and ρ(G') ≤ max_i Σ_j G'_{ij} (maximum row sum).

Row sum for row i: Σ_j G'_{ij} = 1 + Σ_{j≠i} |G_{ij}| = 1 - Σ_{j≠i} G_{ij} = 1 - s_i where s_i = Σ_{j≠i} G_{ij} ≤ 0.

So row sum = 1 - s_i ≥ 1.

The maximum row sum is max_i (1 - s_i) = 1 - min_i s_i.

Since s_i ≤ 0, we have 1 - s_i ≥ 1, and the max row sum ≥ 1.

Now, ρ(G') ≤ max row sum. Also, G' has at least M - n eigenvalues equal to 2. So ρ(G') ≥ 2 (if M > n, there's at least one eigenvalue equal to 2, and the spectral radius is the largest absolute eigenvalue, which is ≥ 2).

Wait, but eigenvalues of G' could be negative? No: G' = 2I - G. If G has an eigenvalue λ > 2, then G' has eigenvalue 2 - λ < 0. But G is PSD with eigenvalues ≥ 0, and G' = 2I - G has eigenvalues 2 - λ_i. If some λ_i > 2, then G' has negative eigenvalues.

But G' is a nonneg matrix. By Perron-Frobenius, the spectral radius ρ(G') is a nonneg eigenvalue, and |μ| ≤ ρ(G') for all eigenvalues μ. So if G' has an eigenvalue 2 (from the zero eigenvalues of G), then ρ(G') ≥ 2. And if G' has a negative eigenvalue 2 - λ with λ > 2, then |2 - λ| = λ - 2 ≤ ρ(G').

So ρ(G') ≥ max(2, λ_max(G) - 2) where λ_max(G) is the largest eigenvalue of G.

Also, ρ(G') ≤ max row sum = 1 - min_i s_i.

Now, λ_max(G) ≤ max row sum of G = max_i (1 + s_i) = 1 + max_i s_i ≤ 1 (since s_i ≤ 0). 

Wait, that's the max row sum of G: Σ_j G_{ij} = 1 + s_i ≤ 1 (since s_i ≤ 0). So λ_max(G) ≤ max row sum of G ≤ 1? 

No wait, that's not right. For a PSD matrix, λ_max ≤ max row sum? Actually, for any matrix, the spectral radius ≤ max row sum (for nonneg matrices by PF, but for general matrices, ρ ≤ max row sum in absolute value). For a symmetric matrix, λ_max ≤ max_i Σ_j |G_{ij}|. 

For our G: Σ_j |G_{ij}| = 1 + Σ_{j≠i} |G_{ij}| = 1 - s_i (since G_{ij} ≤ 0). So λ_max(G) ≤ max_i (1 - s_i) = 1 - min_i s_i.

Hmm, so λ_max(G) ≤ 1 - min_i s_i, and ρ(G') ≤ 1 - min_i s_i as well. And ρ(G') ≥ 2 (when M > n).

So 2 ≤ ρ(G') ≤ 1 - min_i s_i, giving min_i s_i ≤ -1, i.e., there exists i with s_i ≤ -1, meaning Σ_{j≠i} G_{ij} ≤ -1.

This is a constraint but doesn't directly give M ≤ 2n.

Hmm, I think I need a different approach. Let me look at this problem from a different angle.

Actually, wait. Let me reconsider. I think the correct statement might be slightly different. Let me reconsider whether the bound is 2n or something else.

Let me check for n = 3 (odd, but let's see). Unit vectors in R^3 with pairwise ≤0 inner products. Can we have 6 = 2·3? Yes: ±e_1, ±e_2, ±e_3. Can we have 7? 

The vertices of an icosahedron? No, those have some positive inner products. 

Actually, for n=3, the maximum is 6 = 2n. The cross-polytope (octahedron) achieves this.

For n=4: 8 = 2·4, achieved by ±e_i. Can we do better? The 24-cell has 24 vertices in R^4, but the inner products between vertices include positive values, so it doesn't satisfy our condition.

I believe the Rankin bound M ≤ 2n is correct. Let me find the proof.

OK here's another attempt at the proof:

Proof of M ≤ 2n:

Let u_1, ..., u_M be unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

Consider the set S = {u_1, ..., u_M} ∪ {-u_1, ..., -u_M}. If u_i ≠ -u_j for all i, j (i.e., no vector is the negative of another), then |S| = 2M. If some u_i = -u_j, then |S| < 2M.

Case 1: No u_i = -u_j for i ≠ j (and all u_i distinct, which follows from ⟨u_i, u_j⟩ ≤ 0 < 1 = ⟨u_i, u_i⟩). Then S has 2M vectors.

For any two vectors in S:
- u_i, u_j (i≠j): ⟨u_i, u_j⟩ ≤ 0
- -u_i, -u_j (i≠j): ⟨-u_i, -u_j⟩ = ⟨u_i, u_j⟩ ≤ 0
- u_i, -u_i: ⟨u_i, -u_i⟩ = -1 < 0
- u_i, -u_j (i≠j): ⟨u_i, -u_j⟩ = -⟨u_i, u_j⟩ ≥ 0

So the only non-negative inner products in S are between u_i and -u_j for i ≠ j.

Hmm, this doesn't immediately help.

Let me try yet another approach. I'll use the approach from Alexander's proof of the Rankin bound.

Actually, I found it. Here's the proof:

Proof: Consider the unit vectors u_1, ..., u_M in R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

We use the following key fact: these vectors are the vertices of a set where all pairwise distances are ≥ √2 (since ||u_i - u_j||^2 = 2 - 2⟨u_i, u_j⟩ ≥ 2).

Now, consider the cap bodies or the half-spaces. For each u_i, consider the half-space H_i = {x ∈ R^n : ⟨x, u_i⟩ > 0}. 

The condition ⟨u_i, u_j⟩ ≤ 0 means u_j ∉ H_i for j ≠ i (i.e., u_j is not in the open half-space of u_i). So each u_j (j ≠ i) is in the closed half-space {x : ⟨x, u_i⟩ ≤ 0}.

This means the vectors "see" each other at angles ≥ 90°.

Now, the key insight: Consider the hyperplane arrangement or use the following volume argument.

Actually, here's a clean proof using the "kissing number" idea:

Consider the M unit vectors. For each u_i, consider the open hemisphere centered at u_i: H_i = {x ∈ S^{n-1} : ⟨x, u_i⟩ > 0}. 

The condition says u_j ∉ H_i for all j ≠ i. So each H_i contains exactly one of the M vectors (namely u_i itself).

Now, consider the M hemispheres H_1, ..., H_M. Each is an open hemisphere of S^{n-1}. 

The measure of each H_i is exactly half the sphere (1/2 of the total measure). The M hemispheres each contain exactly one of the M points.

Hmm, this doesn't directly give a bound.

Let me try the approach via the "Rankin bound" as stated in Conway and Sloane or similar.

Actually, I think the proof might go like this:

Consider the matrix V = [u_1, ..., u_M] (n × M). Consider V^T V = G (M × M Gram matrix).

Now, det(G) ≥ 0 (PSD). If M ≤ n, G could be full rank and det(G) > 0. If M > n, det(G) = 0.

For M = n + 1: G is (n+1) × (n+1), PSD, rank ≤ n, so det(G) = 0. The vectors are linearly dependent.

For the simplex case (all inner products equal to -1/n), we get M = n + 1 with all inner products = -1/n < 0. This is the regular simplex, and it's the maximum for strictly negative inner products (φ > π/2).

For φ = π/2 (inner products ≤ 0, allowing 0), we can do better: M = 2n.

Here's the proof I think works:

Proof: We show M ≤ 2n by induction on n.

Base case n = 1: Unit vectors in R^1 are ±1. At most 2 with pairwise ≤0 inner product. ✓

Inductive step: Assume for R^{n-1}, the max is 2(n-1). Consider M unit vectors u_1, ..., u_M in R^n with pairwise ≤0 inner products.

If M ≤ 2, done (2 ≤ 2n for n ≥ 1). Assume M ≥ 3.

Pick u_1. Consider the hyperplane H = {x : ⟨x, u_1⟩ = 0}, which is R^{n-1}.

For each j ≥ 2, decompose u_j = a_j u_1 + w_j where w_j ∈ H (i.e., ⟨w_j, u_1⟩ = 0) and a_j = ⟨u_j, u_1⟩ ≤ 0.

If a_j = 0 for some j, then u_j ∈ H, and we can project all vectors with a_j = 0 onto H and apply induction.

If a_j < 0 for all j ≥ 2, then... hmm, this gets complicated.

Let me try a different induction.

Actually, I think the standard proof uses the following lemma:

Lemma: If u_1, ..., u_M are unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j, and M ≥ 2, then there exist two vectors, say u_1 and u_2, such that ⟨u_1, u_2⟩ = 0 (if M > n + 1) or the configuration is a simplex (if M = n + 1).

Hmm, that's not quite right either.

Let me just try to find the proof online in my memory...

Actually, I recall now. The proof uses the following approach:

Consider the M unit vectors. Define the polynomial:

p(x) = Π_{i=1}^M (1 + ⟨x, u_i⟩) 

Wait, that's for the "kissing number" type bounds.

Let me try a completely different approach. Let me use the specific structure of the problem (n = 2^2005, a power of 2) and the Hadamard matrix.

For n = 2^k, the Sylvester Hadamard matrix H_n of order n exists. The rows of H_n (and their negatives) give 2n vectors in {±1}^n with pairwise inner product 0 (for distinct rows) or -n (for a row and its negative). So we get 2n codewords with min distance n/2.

Now for the upper bound, let me try to use the specific structure.

Actually, let me try the LP (Delsarte) bound for this specific case.

The Delsarte LP bound for A(n, d) with d = n/2:

We need to find the maximum of Σ_{k=0}^n A_k subject to:
- A_0 = 1
- A_k = 0 for 1 ≤ k ≤ d-1 = n/2 - 1
- A_k ≥ 0 for k ≥ d = n/2
- Σ_{k=0}^n A_k K_k(j) ≥ 0 for j = 0, 1, ..., n

where K_k(j) = Σ_{i=0}^k (-1)^i C(j, i) C(n-j, k-i) are Krawtchouk polynomials.

For the specific case n = 2^m, d = n/2 = 2^{m-1}, the LP bound is known to be 2n.

Actually, let me think about this differently. For the Hadamard code, the distance distribution is:
- A_0 = 1
- A_{n/2} = 2n - 2 (all other codewords are at distance n/2 from any given codeword)
- A_n = 1 (the complement is at distance n)

Wait, that's for the Hadamard code of size 2n. Let me verify. The Hadamard code consists of the n rows of H_n and their n negatives. For a given codeword (row r), the other n-1 rows are at distance n/2, the negative of row r is at distance n, and the negatives of the other n-1 rows are at distance n/2. So from any codeword: 1 at distance 0, 2(n-1) at distance n/2, 1 at distance n. Total: 1 + 2(n-1) + 1 = 2n. ✓

So the distance distribution is A_0 = 1, A_{n/2} = 2n-2, A_n = 1, and A_k = 0 otherwise.

For this to be optimal, we need to show that the LP bound gives exactly 2n.

The LP bound: maximize 1 + A_{n/2} + A_n + ... subject to the constraints. The Hadamard code's distance distribution gives 1 + (2n-2) + 1 = 2n. We need to show this is the LP optimum.

To show the LP bound is 2n, we need to find a dual solution (a polynomial f such that f_0 = 1, f_k ≥ 0 for k ≥ d, and the Krawtchouk expansion gives the bound).

This is getting quite involved. Let me try a more elementary approach.

Let me try the following approach specific to n = 2^k:

Approach: Use the Walsh-Hadamard transform.

The key idea: For n = 2^k, the Hadamard matrix H_n has rows that form a group under componentwise multiplication (isomorphic to (Z/2Z)^k). 

Consider any code C ⊂ {±1}^n with pairwise inner product ≤ 0. We want |C| ≤ 2n.

Map each codeword c ∈ {±1}^n to its Walsh-Hadamard transform. The WHT of c is ĉ = c · H_n / n (where · denotes matrix-vector product, and H_n is the normalized Hadamard matrix with H_n H_n^T = nI).

Actually, let me think about this differently.

The characters of the group (Z/2Z)^k are the rows of the Hadamard matrix. For any function f : (Z/2Z)^k → R, the Fourier transform is f̂(χ) = Σ_x f(x) χ(x) for each character χ.

In our setting, each codeword c ∈ {±1}^n can be viewed as a function from (Z/2Z)^k to {±1}. The inner product ⟨c, c'⟩ = Σ_x c(x) c'(x) = n · (correlation).

Hmm, let me think about this more carefully.

Actually, let me try a direct proof for n = 2^k using the structure of the Hadamard matrix.

Proof for n = 2^k:

Let C = {c_1, ..., c_M} ⊂ {±1}^n with ⟨c_i, c_j⟩ ≤ 0 for i ≠ j. We show M ≤ 2n.

Consider the Hadamard matrix H of order n (Sylvester type). The rows h_1, ..., h_n of H form an orthogonal basis of R^n (after normalization): ⟨h_a, h_b⟩ = n δ_{ab}.

Express each c_i in this basis: c_i = Σ_{a=1}^n α_{ia} h_a / n, where α_{ia} = ⟨c_i, h_a⟩.

Since c_i ∈ {±1}^n, ||c_i||^2 = n, so Σ_a α_{ia}^2 / n = n, i.e., Σ_a α_{ia}^2 = n^2.

Also, α_{ia} = ⟨c_i, h_a⟩ is an integer (sum of ±1 · ±1 terms), and α_{ia} ≡ n (mod 2) (since each term is ±1, and there are n terms, the sum has the same parity as n; n = 2^k is even for k ≥ 1, so α_{ia} is even).

Hmm, this is getting complicated. Let me try yet another approach.

Let me go back to trying to prove the Rankin bound M ≤ 2n and be more careful.

Proof of Rankin bound (M ≤ 2n for unit vectors with pairwise nonpositive inner products):

I'll use the approach from the paper / textbook. Here's a proof that I believe is correct:

Let u_1, ..., u_M be unit vectors in R^n with ⟨u_i, u_j⟩ ≤ 0 for i ≠ j.

Step 1: If M ≤ n + 1, then M ≤ 2n trivially (for n ≥ 1). So assume M > n + 1, i.e., M ≥ n + 2.

Step 2: Since M > n, the vectors are linearly dependent. So there exist scalars α_1, ..., α_M, not all zero, with Σ α_i u_i = 0.

Step 3: Let P = {i : α_i > 0} and N = {i : α_i < 0}. (Ignore zero coefficients.) Then Σ_{i∈P} α_i u_i = -Σ_{j∈N} α_j u_j = Σ_{j∈N} |α_j| u_j. Let v = Σ_{i∈P} α_i u_i = Σ_{j∈N} |α_j| u_j.

Step 4: ||v||^2 = ⟨Σ_{i∈P} α_i u_i, Σ_{j∈N} |α_j| u_j⟩ = Σ_{i∈P, j∈N} α_i |α_j| ⟨u_i, u_j⟩ ≤ 0 (since α_i > 0, |α_j| > 0, and ⟨u_i, u_j⟩ ≤ 0).

But also ||v||^2 ≥ 0. So ||v||^2 = 0, hence v = 0.

Step 5: v = 0 means Σ_{i∈P} α_i u_i = 0 and Σ_{j∈N} |α_j| u_j = 0.

So the vectors in P are linearly dependent (if |P| ≥ 2), and the vectors in N are linearly dependent (if |N| ≥ 2).

Step 6: This shows that the vectors can be partitioned into two linearly dependent sets. But this doesn't directly bound M.

Hmm, let me think about this more. The key insight from Step 4 is that ||v||^2 = 0, which means all the inner products ⟨u_i, u_j⟩ for i ∈ P, j ∈ N must be exactly 0 (since they're all ≤ 0 and their weighted sum is 0, with positive weights).

So: ⟨u_i, u_j⟩ = 0 for all i ∈ P, j ∈ N.

This means the vectors in P are orthogonal to the vectors in N.

Step 7: Let's use this. We have a partition of {1, ..., M} into P, N (and possibly some with α_i = 0, which we ignore). The vectors indexed by P are orthogonal to those indexed by N.

Let V_P = span{u_i : i ∈ P} and V_N = span{u_j : j ∈ N}. These are orthogonal subspaces. Let dim(V_P) = p, dim(V_N) = q, with p + q ≤ n.

The vectors in P are in V_P (dimension p), and the vectors in N are in V_N (dimension q).

Now, within P: the vectors {u_i : i ∈ P} are unit vectors in V_P ≅ R^p with pairwise ≤0 inner products. By induction, |P| ≤ 2p.

Similarly, |N| ≤ 2q.

So M = |P| + |N| + |{i : α_i = 0}| ≤ 2p + 2q + |{i : α_i = 0}|.

Hmm, but we also have vectors with α_i = 0. Let Z = {i : α_i = 0}. For i ∈ Z, u_i is orthogonal to... well, not necessarily orthogonal to anything specific.

Wait, actually, the α_i came from a specific linear dependence. Let me reconsider.

We have Σ α_i u_i = 0 with not all α_i zero. P = {i : α_i > 0}, N = {i : α_i < 0}, Z = {i : α_i = 0}.

We showed ⟨u_i, u_j⟩ = 0 for i ∈ P, j ∈ N.

But for i ∈ Z, we don't have specific orthogonality. However, u_i for i ∈ Z can be decomposed as u_i = u_i^P + u_i^N + u_i^⊥ where u_i^P ∈ V_P, u_i^N ∈ V_N, u_i^⊥ ∈ (V_P ⊕ V_N)^⊥.

Since u_i is a unit vector and ⟨u_i, u_j⟩ ≤ 0 for all j ≠ i:

For j ∈ P: ⟨u_i, u_j⟩ = ⟨u_i^P, u_j⟩ ≤ 0 (since u_j ∈ V_P).
For j ∈ N: ⟨u_i, u_j⟩ = ⟨u_i^N, u_j⟩ ≤ 0 (since u_j ∈ V_N).

So u_i^P has nonpositive inner products with all u_j (j ∈ P), and u_i^N has nonpositive inner products with all u_j (j ∈ N).

This is getting very complicated. Let me try to use induction more carefully.

Inductive proof:

Claim: For unit vectors in R^n with pairwise ≤0 inner products, M ≤ 2n.

Base case n = 1: M ≤ 2. ✓

Inductive step: Assume true for dimensions < n. Consider M unit vectors in R^n.

If M ≤ n + 1: M ≤ n + 1 ≤ 2n for n ≥ 1. ✓ (For n = 1: n+1 = 2 = 2n. For n ≥ 2: n+1 ≤ 2n.)

If M > n + 1 (so M ≥ n + 2 ≥ 4, hence n ≥ 2): The vectors are linearly dependent (M > n). Find a dependence Σ α_i u_i = 0 with not all α_i = 0.

As shown, ⟨u_i, u_j⟩ = 0 for all i ∈ P, j ∈ N (where P, N are the positive and negative coefficient sets).

Now, both P and N are nonempty (since the sum is 0 and not all α_i = 0, there must be both positive and negative coefficients).

The vectors in P span a subspace V_P of dimension p ≤ |P| - 1 (since they're linearly dependent: Σ_{i∈P} α_i u_i = 0 with all α_i > 0). Actually, p ≤ |P| - 1 only if the dependence is nontrivial, which it is since all α_i > 0 and the sum is 0 (so there must be at least 2 elements in P). Wait, actually p could be up to |P| - 1, but it could also be less.

Similarly, V_N has dimension q ≤ |N| - 1.

And V_P ⊥ V_N, so p + q ≤ n.

Now, the vectors in P are unit vectors in V_P (dim p) with pairwise ≤0 inner products. By induction, |P| ≤ 2p.

Similarly, |N| ≤ 2q.

For vectors in Z = {i : α_i = 0}: These vectors are in R^n. They have pairwise ≤0 inner products with each other and with all vectors in P and N.

For i ∈ Z and j ∈ P: ⟨u_i, u_j⟩ ≤ 0. Decompose u_i = u_i^P + u_i^{P⊥} where u_i^P ∈ V_P. Then ⟨u_i, u_j⟩ = ⟨u_i^P, u_j⟩ ≤ 0 for all j ∈ P.

If u_i^P ≠ 0, then ū_i^P = u_i^P / ||u_i^P|| is a unit vector in V_P with ⟨ū_i^P, u_j⟩ ≤ 0 for all j ∈ P. But also, the vectors in P have pairwise ≤0 inner products. So {ū_i^P : i ∈ Z, u_i^P ≠ 0} ∪ {u_j : j ∈ P} are unit vectors in V_P with pairwise ≤0 inner products... 

Wait, but I need to check ⟨ū_i^P, ū_k^P⟩ ≤ 0 for i, k ∈ Z. We know ⟨u_i, u_k⟩ ≤ 0, but ⟨u_i^P, u_k^P⟩ could be anything (since the P⊥ components could contribute negatively).

Hmm, ⟨u_i, u_k⟩ = ⟨u_i^P, u_k^P⟩ + ⟨u_i^{P⊥}, u_k^{P⊥}⟩ ≤ 0. So ⟨u_i^P, u_k^P⟩ ≤ -⟨u_i^{P⊥}, u_k^{P⊥}⟩, which could be positive.

So this approach doesn't directly work for handling Z.

This is getting really complicated. Let me try a completely different strategy.

Let me try to use the specific structure of n = 2^2005 (a power of 2) and prove the bound directly for this case.

For n = 2^k, I'll use the Hadamard matrix structure.

Key idea: The rows of the Sylvester Hadamard matrix H_{2^k} form a group G ≅ (Z/2Z)^k under componentwise multiplication. This group has n = 2^k elements.

For any two distinct rows h_a, h_b, we have ⟨h_a, h_b⟩ = 0 (orthogonality). And ⟨h_a, -h_b⟩ = 0 for a ≠ b, ⟨h_a, -h_a⟩ = -n.

The Hadamard code C_H = {h_a : a ∈ G} ∪ {-h_a : a ∈ G} has 2n codewords with pairwise inner product ≤ 0.

Now, for the upper bound, let me use the following approach:

Consider any code C ⊂ {±1}^n with |C| = M and pairwise inner product ≤ 0.

For each codeword c ∈ C, consider its "syndrome" or its expansion in the Hadamard basis.

The Hadamard basis {h_a / √n : a ∈ G} is an orthonormal basis of R^n. So each c ∈ {±1}^n can be written as c = (1/√n) Σ_a ĉ(a) h_a where ĉ(a) = ⟨c, h_a⟩ / √n.

Since ||c||^2 = n, we have Σ_a ĉ(a)^2 = n (Parseval). Also, ĉ(a) = ⟨c, h_a⟩ / √n, and ⟨c, h_a⟩ is an integer with |⟨c, h_a⟩| ≤ n and ⟨c, h_a⟩ ≡ n (mod 2) (even, since n is even).

Now, for two codewords c, c' ∈ C with ⟨c, c'⟩ ≤ 0:

⟨c, c'⟩ = (1/n) Σ_a ĉ(a) ĉ'(a) · n = Σ_a ĉ(a) ĉ'(a) ... 

Wait, let me redo this. c = (1/n) Σ_a ⟨c, h_a⟩ h_a (since h_a are orthogonal with ||h_a||^2 = n, the expansion is c = Σ_a (⟨c, h_a⟩ / n) h_a).

So ⟨c, c'⟩ = Σ_a (⟨c, h_a⟩ / n)(⟨c', h_a⟩ / n) · n = (1/n) Σ_a ⟨c, h_a⟩ ⟨c', h_a⟩.

Let f_c(a) = ⟨c, h_a⟩ (integer, even, |f_c(a)| ≤ n). Then ⟨c, c'⟩ = (1/n) Σ_a f_c(a) f_{c'}(a) ≤ 0.

Also, Σ_a f_c(a)^2 = n · ||c||^2 = n^2 (Parseval).

So we have M functions f_1, ..., f_M : G → Z (where G ≅ (Z/2Z)^k, |G| = n) such that:
- Σ_a f_i(a)^2 = n^2
- (1/n) Σ_a f_i(a) f_j(a) ≤ 0 for i ≠ j, i.e., Σ_a f_i(a) f_j(a) ≤ 0.
- f_i(a) is even, |f_i(a)| ≤ n.

We want to show M ≤ 2n.

Hmm, this reformulation might help but I'm not sure how to proceed.

Let me try yet another approach. Let me use the Plotkin bound proof but more carefully for the d = n/2 case.

Actually, I just realized something. Let me reconsider the Plotkin bound.

The Plotkin bound proof gives: for M even, M(2d - n) ≤ 2d. For d = n/2, this is M · 0 ≤ n, which is always true. So no bound.

But there's a refined version. Let me think about what happens when we use the integrality of the distances.

For binary codes, the distances are integers. If d = n/2 and n is even, then d is an integer. The condition is d(c_i, c_j) ≥ n/2, so d(c_i, c_j) ∈ {n/2, n/2 + 1, ..., n}.

In the ±1 representation, ⟨v_i, v_j⟩ = n - 2d(c_i, c_j) ≤ 0, and ⟨v_i, v_j⟩ ≡ n (mod 2) (even, since n is even). So ⟨v_i, v_j⟩ ∈ {0, -2, -4, ..., -n}.

Now, let me use the refined Plotkin bound with integrality.

From the double counting:
Σ_{i<j} d(c_i, c_j) = Σ_k a_k(M - a_k)

where a_k = number of 1's in position k.

Lower bound: Σ_{i<j} d(c_i, c_j) ≥ (n/2) · M(M-1)/2.

Upper bound: Σ_k a_k(M - a_k) ≤ n · M^2/4 (with equality iff a_k = M/2 for all k, requiring M even).

For M even: (n/2) · M(M-1)/2 ≤ n M^2/4, i.e., M(M-1)/4 ≤ M^2/4, i.e., M-1 ≤ M. Trivial.

But we can get a tighter upper bound using integrality. a_k is an integer, so a_k(M - a_k) is maximized when a_k = M/2 (if M even), giving M^2/4. If M is odd, max is (M-1)(M+1)/4 = (M^2-1)/4.

For M even, the upper bound is exactly nM^2/4, achieved when a_k = M/2 for all k. The lower bound is nM(M-1)/4, achieved when all distances are exactly n/2.

Gap: nM^2/4 - nM(M-1)/4 = nM/4. So there's a gap of nM/4, which means the bound is not tight.

To get a tighter bound, I need to use more structure.

Let me try the approach of considering the code as a subset of {±1}^n and using the Welch bound or similar.

Welch bound: For M unit vectors in R^n, max_{i≠j} |⟨u_i, u_j⟩| ≥ sqrt((M-n)/(n(M-1))).

In our case, ⟨u_i, u_j⟩ ≤ 0, so |⟨u_i, u_j⟩| = -⟨u_i, u_j⟩ ≥ 0. The Welch bound says max_{i≠j} |⟨u_i, u_j⟩| ≥ sqrt((M-n)/(n(M-1))). This is always satisfied for M > n (since the max is at least some positive value). But it doesn't directly bound M.

Actually, the Welch bound gives a lower bound on the maximum correlation, not an upper bound on M. To get an upper bound on M, we'd need an upper bound on the maximum correlation, which we have (it's ≤ 0... but the Welch bound is about |⟨·,·⟩|, and we only know ⟨·,·⟩ ≤ 0, not |⟨·,·⟩| ≤ something).

Hmm. Let me think about this problem differently.

Actually, wait. Let me reconsider the problem. Maybe the answer is not 2n = 2^2006 but something else.

Let me re-examine the small cases more carefully.

n = 2 (2^1): A(2,1) = 4. All 4 binary vectors of length 2 have pairwise distance ≥ 1. 4 = 2·2 = 2^2. ✓

n = 4 (2^2): A(4,2) = 8. All 8 even-weight vectors of length 4 have pairwise distance ≥ 2 (since difference of two even-weight vectors has even weight, and if distinct, weight ≥ 2). 8 = 2·4 = 2^3. ✓

n = 8 (2^3): A(8,4) = 16. The extended Hamming code [8,4,4] gives 16. 16 = 2·8 = 2^4. ✓

So the pattern is A(2^k, 2^{k-1}) = 2^{k+1}, and the answer for n = 2^2005 is 2^2006.

Now I need to prove A(2^k, 2^{k-1}) ≤ 2^{k+1}. Let me try to prove this by induction on k.

Induction on k:

Base case k = 1 (n = 2): A(2,1) = 4 = 2^2. ✓ (Easy to verify: all 4 vectors work, and there are only 4 vectors total.)

Inductive step: Assume A(2^{k-1}, 2^{k-2}) = 2^k. Show A(2^k, 2^{k-1}) ≤ 2^{k+1}.

Let C be a binary code of length n = 2^k with minimum distance d = 2^{k-1} = n/2. We want |C| ≤ 2n = 2^{k+1}.

Idea: Split the code based on the first coordinate (or any fixed coordinate).

Let c_1 be the first digit (position 1) of each codeword. Partition C into:
- C_0 = {c ∈ C : c_1 = 0}
- C_1 = {c ∈ C : c_1 = 1}

For any two codewords in C_0, their distance is the distance in the remaining n-1 coordinates (since they agree in position 1). So C_0 is a code of length n-1 with min distance ≥ n/2.

Similarly for C_1.

But n-1 = 2^k - 1, which is not a power of 2, so the inductive hypothesis doesn't directly apply.

Hmm. Let me try a different splitting.

Alternative: Use the Reed-Muller / Hadamard structure.

For n = 2^k, index the coordinates by elements of GF(2)^k. The Hadamard matrix rows are the characters χ_a(x) = (-1)^{a·x} for a ∈ GF(2)^k.

Consider the code C ⊂ {±1}^n with pairwise inner product ≤ 0.

For each codeword c ∈ C, define its Fourier transform ĉ(a) = Σ_x c(x) χ_a(x) = ⟨c, h_a⟩ (where h_a is the a-th row of the Hadamard matrix).

Properties:

