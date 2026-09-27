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
  <problem_id>polymath_00847</problem_id>
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

Let $P(x), Q(x)$ be distinct polynomials of degree $2020$ with non-zero coefficients. Suppose that they have $r$ common real roots counting multiplicity and $s$ common coefficients. Determine the maximum possible value of $r + s$.

[i]Demetres Christofides, Cyprus[/i]

## Standard Solution

To determine the maximum possible value of \( r + s \) where \( P(x) \) and \( Q(x) \) are distinct polynomials of degree 2020 with non-zero coefficients, and they have \( r \) common real roots (counting multiplicity) and \( s \) common coefficients, we proceed as follows:

1. **Construction**:
   - Let \( P(x) = (x^2 + 2x + 1)(x^2 - \alpha_1)(x^2 - \alpha_2) \cdots (x^2 - \alpha_{1009}) \).
   - Let \( Q(x) = (x^2 + x + 1)(x^2 - \alpha_1)(x^2 - \alpha_2) \cdots (x^2 - \alpha_{1009}) \).
   - Here, \( \alpha_i \) are real numbers chosen such that no coefficient of \( P(x) \) and \( Q(x) \) is zero.

2. **Common Real Roots**:
   - \( P(x) \) and \( Q(x) \) share \( 1009 \cdot 2 = 2018 \) real roots, which are \( \sqrt{\alpha_i} \) for \( i = 1, 2, \ldots, 1009 \).

3. **Common Coefficients**:
   - The product \( (x^2 - \alpha_1)(x^2 - \alpha_2) \cdots (x^2 - \alpha_{1009}) \) only contains even powers of \( x \).
   - Therefore, the even powers of \( x \) in \( P(x) \) and \( Q(x) \) both arise from this product, and so these coefficients are equal.
   - There are \( 1011 \) such coefficients (including the constant term).

4. **Sum of Common Roots and Coefficients**:
   - Thus, \( r + s = 2018 + 1011 = 3029 \).

5. **Bound**:
   - Let \( R(x) = P(x) - Q(x) \).
   - \( P(x) \) and \( Q(x) \) share \( r \) common real roots and \( s \) common coefficients, implying \( R(x) \) has at least \( r \) real roots and at most \( s \) zero coefficients.

6. **Maximizing \( r \) and \( s \)**:
   - To maximize \( r \) and \( s \), we want to maximize the number of zero coefficients and real roots of \( R(x) \).
   - This is achieved by making all the real roots of \( R(x) \) shared roots, and setting \( \deg(R) = d-1 \), where \( P(x) \) and \( Q(x) \) are both monic to provide another shared coefficient.

7. **Inductive Proof**:
   - For a polynomial \( R(x) \) with degree \( d \), with a constant term and \( k < d \) zero coefficients, the maximum number of roots is \( d + \left\lfloor \frac{d}{2} \right\rfloor - k \).
   - Base cases and inductive steps are used to establish this result.

8. **Conclusion**:
   - For \( n = 2020 \), the maximum value of \( r + s \) is \( 2020 + \left\lfloor \frac{2020-1}{2} \right\rfloor = 2020 + 1009 = 3029 \).

The final answer is \( \boxed{ 3029 } \).

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have two distinct polynomials P(x), Q(x) of degree 2020 with non-zero coefficients. They have r common real roots (counting multiplicity) and s common coefficients. Find max of r+s.

Let me think about this carefully.

Let P(x) = a_0 + a_1 x + ... + a_{2020} x^{2020} and Q(x) = b_0 + b_1 x + ... + b_{2020} x^{2020}, all coefficients non-zero.

Common coefficients: indices i where a_i = b_i. There are s such indices.
Common real roots counting multiplicity: r.

Let me think about the relationship. Let D(x) = P(x) - Q(x). The degree of D is at most 2020, but since P and Q are distinct and both degree 2020, if a_{2020} = b_{2020} then degree of D is less than 2020.

The common roots of P and Q are roots of D. So D has at least r real roots (counting multiplicity). Actually, common roots counting multiplicity means: if α is a root of P with multiplicity m and root of Q with multiplicity n, it contributes min(m,n) to r. And α is a root of D with multiplicity at least min(m,n).

So D(x) has at least r roots counting multiplicity.

Now, the number of non-zero coefficients of D: D has coefficients c_i = a_i - b_i. The coefficients where a_i = b_i give c_i = 0. So the number of zero coefficients of D is at least s (exactly s if the common coefficient indices are exactly where they're equal, but there could be more zeros if a_i - b_i = 0 for some other reason... no, a_i = b_i iff c_i = 0). So D has exactly 2021 - s non-zero coefficients (assuming the leading coefficient: if a_{2020} = b_{2020}, then c_{2020} = 0, so degree of D < 2020).

Wait, but we need to be careful. D could be the zero polynomial? No, P and Q are distinct, so D ≠ 0.

Let d = deg(D). The number of non-zero coefficients of D is at most 2021 - s (since at least s coefficients are zero). Actually exactly: the number of zero coefficients of D among indices 0..2020 is exactly s (where a_i = b_i). So D has exactly 2021 - s non-zero coefficients, but some of these might be at positions higher than deg(D)... no, the leading coefficient of D is non-zero by definition of degree.

Let me reconsider. Among indices 0, 1, ..., 2020, exactly s of them have a_i = b_i (c_i = 0), and 2021 - s have c_i ≠ 0. The degree d of D is the largest index with c_i ≠ 0. So d ≤ 2020, and the number of non-zero coefficients of D (as a polynomial of degree d) is 2021 - s minus the number of zero c_i's with index > d... 

Hmm, let me reframe. Let's say the non-zero coefficients of D are at positions in some set S ⊆ {0, 1, ..., 2020} with |S| = 2021 - s. The degree d = max(S).

Now, D has at least r roots (counting multiplicity). By a classical result, a polynomial of degree d with t non-zero terms has at most ... roots? 

The key tool: A polynomial with t non-zero terms has at most t - 1 positive real roots (Descartes' rule) and at most t - 1 negative real roots. So total non-zero real roots ≤ 2(t-1) where t is the number of non-zero terms. Plus possibly root at 0.

Wait, but we need to be more careful about multiplicities and the root at 0.

Let me think again. Let t = number of non-zero terms of D = 2021 - s. 

Root at 0: if c_0 = 0, i.e., a_0 = b_0, then 0 is a common root only if 0 is a root of both P and Q. But a_0 ≠ 0 and b_0 ≠ 0 (all coefficients non-zero), so 0 is NOT a root of P or Q. So 0 is never a common root. Good, so all common roots are non-zero.

So D has at least r non-zero real roots (counting multiplicity).

By Descartes' rule applied to D(x) and D(-x): the number of positive real roots of D (counting multiplicity) ≤ (number of sign changes in D) ≤ t - 1. Similarly for negative roots. So total non-zero real roots counting multiplicity ≤ 2(t-1) = 2(2021 - s - 1) = 2(2020 - s).

So r ≤ 2(2020 - s), giving r + s ≤ 2(2020 - s) + s = 4040 - s.

To maximize r + s, we want to minimize s... but wait, that gives r + s ≤ 4040 - s, so to maximize we want s small. If s = 0, r + s ≤ 4040. But r ≤ 2020 (since P has degree 2020, at most 2020 roots counting multiplicity). So r ≤ 2020, giving r + s ≤ 2020 + s.

Hmm wait, r is the number of common roots counting multiplicity, and each of P and Q has degree 2020, so each has at most 2020 roots counting multiplicity (over all complex, but real roots ≤ 2020). So r ≤ 2020.

So we have two bounds:
1. r ≤ 2(2020 - s) from Descartes
2. r ≤ 2020 (trivially)
3. s ≤ 2021 (but P ≠ Q so s ≤ 2020)

From bound 1: r + s ≤ 4040 - s. From bound 2: r + s ≤ 2020 + s.

The first bound is better when s is small, the second when s is large. They cross when 4040 - s = 2020 + s, i.e., 2020 = 2s, s = 1010. At s = 1010, both give r + s ≤ 3030.

So the maximum of min(4040 - s, 2020 + s) over s is achieved at s = 1010, giving 3030.

Wait, but we need to check that this is achievable. Let me verify.

We need r + s = 3030 with s = 1010, r = 2020.

For r = 2020: P and Q share all 2020 roots (counting multiplicity). Since both have degree 2020 with all non-zero coefficients, if they share all roots, then P = c·Q for some constant c. But then all coefficients are scaled by c. For common coefficients, a_i = b_i means c·b_i = b_i, so either b_i = 0 (not allowed) or c = 1. If c = 1, P = Q, contradiction. So r = 2020 forces P = Q. 

So r = 2020 is not achievable with P ≠ Q. Let me reconsider.

If P and Q share r roots counting multiplicity, and r = 2020, then P = cQ. Since all coefficients of Q are non-zero, a_i = c·b_i. Common coefficient means a_i = b_i, so c·b_i = b_i, meaning c = 1 (since b_i ≠ 0). So s = 2021 (all coefficients common) and P = Q. Contradiction.

So r = 2020 is impossible when P ≠ Q. What's the max r?

If P = cQ with c ≠ 1, then r = 2020 (all roots shared) but s = 0 (no common coefficients since c ≠ 1). So r + s = 2020. But wait, is r = 2020 achievable? P = cQ, c ≠ 1, all coefficients of Q non-zero, degree 2020. Then r = 2020, s = 0, r + s = 2020. But we need real roots. Q needs to have 2020 real roots counting multiplicity. E.g., Q(x) = (x-1)(x-2)...(x-2020) has all real roots, but its coefficients might have zeros... Actually (x-1)(x-2)...(x-2020) — does it have all non-zero coefficients? The constant term is 2020! ≠ 0, and by Newton's identities / Vieta's, all elementary symmetric polynomials of 1,2,...,2020 are non-zero? Not necessarily. Hmm.

Actually, let me reconsider the problem. Let me think about what's achievable.

Let me reconsider. The bound r + s ≤ 3030 at s = 1010 requires r = 2020, which we showed is impossible. So the actual maximum might be lower.

Let me think more carefully. 

If P and Q share r roots (counting multiplicity), then D = P - Q has those r roots. But also, P has degree 2020, so r ≤ 2020. And if r = 2020, P = cQ.

Let me think about r = 2019. Then P and Q share 2019 roots. P = (x - α_1)...(x - α_{2019}) · L(x) where deg L = 1, and Q = (x - α_1)...(x - α_{2019}) · M(x) where deg M = 1. So P - Q = (x - α_1)...(x - α_{2019}) · (L(x) - M(x)). L - M is a polynomial of degree ≤ 1. If L ≠ M, then D = P - Q has degree 2020 (if L - M is degree 1) or degree 2019 (if L - M is constant, i.e., L and M have same leading coefficient).

Hmm, this is getting complicated. Let me think about the structure differently.

Let's denote the common roots (with multiplicity) as α_1, ..., α_r. Then P(x) = G(x) · P_1(x) and Q(x) = G(x) · Q_1(x) where G(x) = ∏(x - α_i) has degree r, and P_1, Q_1 have degree 2020 - r, and P_1, Q_1 share no common roots (or rather, the common roots are exactly captured by G — but actually the multiplicities: if α is a root of P with multiplicity m_P and Q with multiplicity m_Q, it contributes min(m_P, m_Q) to r, and G has α with multiplicity min(m_P, m_Q)).

So gcd(P, Q) = G (over reals, considering multiplicities, G captures the common roots). deg G = r. P = G · P_1, Q = G · Q_1, gcd(P_1, Q_1) = 1 (no common roots). deg P_1 = deg Q_1 = 2020 - r.

D = P - Q = G · (P_1 - Q_1). P_1 - Q_1 has degree ≤ 2020 - r (could be less if leading coefficients of P_1 and Q_1 are equal).

D has the r roots from G, plus the roots of P_1 - Q_1. The roots of P_1 - Q_1 are not common roots of P and Q (since gcd(P_1, Q_1) = 1, any root of P_1 - Q_1 that's a root of P_1 would also be a root of Q_1, contradiction). So the roots of P_1 - Q_1 are "extra" roots of D that are not common roots.

Now, the number of non-zero terms of D: D = P - Q. The coefficients of D that are zero correspond to common coefficients of P and Q. So D has 2021 - s non-zero coefficients (among indices 0 to 2020).

Hmm, but I need to relate the number of non-zero terms of D to r.

D = G · (P_1 - Q_1). Let H = P_1 - Q_1, deg H = h ≤ 2020 - r. D = G · H, deg D = r + h ≤ 2020.

The number of non-zero terms of D is at most 2021 - s (could be less if some coefficients cancel, but it's exactly the number of indices where a_i ≠ b_i, which is 2021 - s). Wait, no. D = P - Q, and c_i = a_i - b_i. The number of non-zero c_i is exactly 2021 - s (since s coefficients are equal). So D has exactly 2021 - s non-zero coefficients, but as a polynomial of degree d = deg(D), the non-zero coefficients are among indices 0 to d, and there are 2021 - s of them (some indices between 0 and d might have c_i = 0, and all indices > d have c_i = 0).

Wait, I need to be careful. The 2021 - s non-zero coefficients of D are spread among indices 0 to 2020. The degree d of D is the largest such index. So the number of non-zero terms of D (as a polynomial) is 2021 - s.

Now, by Descartes' rule, D has at most (number of non-zero terms - 1) positive roots and at most (number of non-zero terms - 1) negative roots. So total non-zero real roots ≤ 2(2021 - s - 1) = 2(2020 - s).

But D = G · H, and G contributes r roots (all non-zero since 0 is not a root of P or Q). So r ≤ (total real roots of D) ≤ 2(2020 - s).

So r ≤ 2(2020 - s), i.e., r + s ≤ 4040 - s.

Also r ≤ 2020 (since deg P = 2020). But more precisely, if r = 2020, P = cQ, and as shown s = 0 and P ≠ Q requires c ≠ 1, giving r + s = 2020.

If r = 2019: P = G · P_1, Q = G · Q_1, deg G = 2019, deg P_1 = deg Q_1 = 1. P_1 = a(x - β), Q_1 = b(x - γ) with β ≠ γ (no common roots). H = P_1 - Q_1 = (a-b)x - (aβ - bγ). 

If a = b, H = a(γ - β), a non-zero constant, so D = G · a(γ - β), degree 2019, and D has the same number of non-zero terms as G (scaled). G has degree 2019. The number of non-zero terms of D = number of non-zero terms of G. And 2021 - s = (number of non-zero terms of G). So s = 2021 - (non-zero terms of G).

If a ≠ b, H is degree 1, D = G · H has degree 2020, and the number of non-zero terms of D is at most (non-zero terms of G) + (non-zero terms of G shifted by 1) minus overlaps. 

This is getting complicated. Let me think about the problem from a higher level.

The bound r + s ≤ 3030 (at s = 1010, r = 2020) is not achievable because r = 2020 forces P = Q. So what's the real maximum?

Let me reconsider. We have:
- r ≤ 2(2020 - s) [Descartes]
- r ≤ 2020 [degree bound]
- If r = 2020, then P = cQ, c ≠ 1, s = 0, r + s = 2020.

So for r = 2020, r + s = 2020. For r < 2020, we use r + s ≤ min(4040 - s, 2020 + s).

Actually, let me reconsider whether r can be close to 2020 with large s.

If r = 2019, then from Descartes: 2019 ≤ 2(2020 - s), so s ≤ 2020 - 2019/2 = 2020 - 1009.5, so s ≤ 1010 (since s is integer, s ≤ 1010). Then r + s ≤ 2019 + 1010 = 3029.

If r = 2018: 2018 ≤ 2(2020 - s), s ≤ 2020 - 1009 = 1011. r + s ≤ 2018 + 1011 = 3029.

If r = 2017: 2017 ≤ 2(2020 - s), s ≤ 2020 - 1008.5, s ≤ 1011. r + s ≤ 2017 + 1011 = 3028.

Hmm, so the maximum from these bounds seems to be around 3029 or 3030. But we need to check achievability.

Wait, I need to be more careful. The Descartes bound gives r ≤ 2(2020 - s), but this counts ALL real roots of D, not just the common ones. D = G · H, and H might have additional real roots. So actually:

r + (real roots of H) ≤ 2(2020 - s).

This means r ≤ 2(2020 - s) - (real roots of H). Since H has at least 0 real roots, r ≤ 2(2020 - s). But if H has real roots, the bound on r is tighter.

Hmm, but H = P_1 - Q_1 where P_1, Q_1 have degree 2020 - r and share no common roots. H has degree at most 2020 - r. 

The number of non-zero terms of D = G · H. Let me denote t = 2021 - s (non-zero terms of D). 

Actually, I realize the issue. The Descartes bound applies to D as a whole, and D = G·H. The total number of real roots of D (counting multiplicity) is r + (real roots of H counting multiplicity). And this is ≤ 2(t - 1) = 2(2020 - s).

So r ≤ 2(2020 - s) - (real roots of H). To maximize r, we want H to have no real roots (or as few as possible). If H has no real roots, then r ≤ 2(2020 - s).

But can H have no real roots? H = P_1 - Q_1, deg H ≤ 2020 - r. If 2020 - r is even, H could be a polynomial with no real roots (e.g., always positive). If 2020 - r is odd, H must have at least one real root.

Hmm, this is getting quite involved. Let me think about small cases first to get intuition.

Actually, let me reconsider the problem. The answer for this type of problem is often 3030. Let me check if 3030 is achievable.

For r + s = 3030, we need r = 2020, s = 1010 (from the crossing point). But r = 2020 means P = cQ, which gives s = 0 or s = 2021 (P = Q). So 3030 is not achievable.

What about r + s = 3029? We could have r = 2019, s = 1010. Let's check: Descartes gives r ≤ 2(2020 - 1010) = 2·1010 = 2020. So r = 2019 ≤ 2020. ✓. And r = 2019 ≤ 2020. ✓.

But we need to check achievability. Can we have r = 2019 and s = 1010?

P and Q share 2019 roots. P = G · P_1, Q = G · Q_1, deg G = 2019, deg P_1 = deg Q_1 = 1. P_1 = a(x - β), Q_1 = b(x - γ), β ≠ γ (no common root between P_1 and Q_1). 

D = G · (P_1 - Q_1) = G · ((a-b)x - (aβ - bγ)).

Case 1: a = b. Then D = G · a(γ - β), which is a constant times G. So D has the same non-zero terms as G. Number of non-zero terms of D = number of non-zero terms of G. We need this to be 2021 - s = 2021 - 1010 = 1011. So G needs to have 1011 non-zero terms. G has degree 2019. Can a degree 2019 polynomial with 1011 non-zero terms have 2019 real roots (counting multiplicity)? By Descartes, real roots ≤ 2(1011 - 1) = 2020. So 2019 ≤ 2020. ✓ (barely).

But we also need G to have 2019 real roots. G = ∏(x - α_i) for 2019 roots (with multiplicity). If all roots are real, G has 2019 real roots. The number of non-zero terms of G depends on the roots. For G to have 1011 non-zero terms out of 2020 possible (indices 0 to 2019), we need 1009 zero coefficients.

Hmm, this seems hard to achieve in general. Let me think differently.

Actually, maybe I should think about this more carefully using the structure.

Let me reconsider. The key insight is:

D = P - Q has exactly 2021 - s non-zero coefficients (among positions 0 to 2020), and D has at least r real roots (the common roots, all non-zero). By Descartes' rule of signs, the number of positive real roots of D ≤ (number of sign changes) ≤ (number of non-zero terms - 1), and similarly for negative roots. So:

r ≤ 2(2021 - s - 1) = 2(2020 - s).

Also, r ≤ 2020 (degree of P).

And if r = 2020, P = cQ, s ∈ {0, 2021}, so r + s ∈ {2020, 4041} but 4041 means P = Q (excluded). So r + s = 2020 when r = 2020.

For r ≤ 2019: r + s ≤ min(2(2020-s) + s, 2019 + s) = min(4040 - s, 2019 + s).

These are equal when 4040 - s = 2019 + s, i.e., 2s = 2021, s = 1010.5. So s = 1010 or s = 1011.

At s = 1010: r + s ≤ min(3030, 3029) = 3029.
At s = 1011: r + s ≤ min(3029, 3030) = 3029.

So for r ≤ 2019, r + s ≤ 3029.

Combined with r = 2020 giving r + s = 2020, the overall bound is r + s ≤ 3029.

Now I need to check if 3029 is achievable. Let me try to construct an example with r = 2019, s = 1010.

We need P, Q degree 2020, all coefficients non-zero, sharing 2019 roots (counting multiplicity) and 1010 coefficients.

Let me try: P = G · (x - β), Q = G · (x - γ) where G has degree 2019 with all real roots, β ≠ γ, and all coefficients of P and Q are non-zero.

D = G · (β - γ)·... wait, D = P - Q = G·((x-β) - (x-γ)) = G·(γ - β). So D = (γ - β)·G, a constant times G. The non-zero terms of D = non-zero terms of G. We need 2021 - 1010 = 1011 non-zero terms in G (and hence in D).

G has degree 2019, so it has 2020 coefficients (indices 0 to 2019). We need exactly 1011 non-zero and 1009 zero coefficients.

But G = ∏(x - α_i) with 2019 real roots. Can such a product have many zero coefficients?

Hmm, this is the question. Let me think about whether we can have a degree 2019 polynomial with all real roots and exactly 1011 non-zero terms.

By Descartes, a polynomial with t non-zero terms has at most 2(t-1) non-zero real roots. For t = 1011, that's 2020. We need 2019 real roots, which is ≤ 2020. So the bound allows it.

But can we actually construct such a polynomial? Let me think...

Consider G(x) = (x^2 - 1)^k · (x - 1) for appropriate k. (x^2 - 1)^k has degree 2k, and (x-1) adds 1, so degree 2k+1 = 2019, k = 1009. G = (x^2-1)^{1009} · (x-1) = (x-1)^{1010}(x+1)^{1009}. This has 2019 real roots (1010 at 1, 1009 at -1). 

The number of non-zero terms: (x^2 - 1)^{1009} = ∑_{j=0}^{1009} C(1009,j) x^{2j} (-1)^{1009-j}. This has 1010 non-zero terms (at even powers 0, 2, 4, ..., 2018). Multiplying by (x-1): G = (x^2-1)^{1009} · (x-1) = ∑ C(1009,j)(-1)^{1009-j} x^{2j+1} - ∑ C(1009,j)(-1)^{1009-j} x^{2j}.

The terms are at odd powers 1, 3, ..., 2019 (from x · (x^2-1)^{1009}) and even powers 0, 2, ..., 2018 (from -1 · (x^2-1)^{1009}). So all powers from 0 to 2019 appear, giving 2020 non-zero terms. That's too many.

Let me try a different approach. What about G(x) = (x^2 - 1)^{1009} · x? No, that gives degree 2019 but root at 0, which we can't have (since 0 is not a root of P or Q). Actually wait, G's roots are the common roots of P and Q, and we need them to be non-zero (since P and Q have non-zero constant terms). So G can't have 0 as a root.

Let me try G(x) = (x^2 - a^2)^{1009} · (x - b) for some a, b. This has degree 2019, roots at ±a (each with multiplicity 1009) and b. All non-zero if a, b ≠ 0.

(x^2 - a^2)^{1009} = ∑_{j=0}^{1009} C(1009,j) x^{2j} (-a^2)^{1009-j}. Terms at even powers 0, 2, ..., 2018. That's 1010 terms.

G = (x^2 - a^2)^{1009} · (x - b) = x · (x^2 - a^2)^{1009} - b · (x^2 - a^2)^{1009}.

x · (x^2 - a^2)^{1009}: terms at odd powers 1, 3, ..., 2019. (1010 terms)
-b · (x^2 - a^2)^{1009}: terms at even powers 0, 2, ..., 2018. (1010 terms)

So G has terms at all powers 0 to 2019, total 2020 non-zero terms (assuming no cancellation, which there isn't since odd and even powers are disjoint). So 2020 non-zero terms, meaning s = 2021 - 2020 = 1. That gives r + s = 2019 + 1 = 2020. Not great.

I need G to have fewer non-zero terms. The issue is that multiplying by (x - b) spreads the terms.

What if G itself has a sparse structure? Let me think about polynomials with all real roots and few terms.

A polynomial with t non-zero terms and all real roots: by Descartes, we need 2(t-1) ≥ deg G = 2019, so t ≥ 1011 (since 2·1010 = 2020 ≥ 2019). So the minimum number of non-zero terms for a degree 2019 polynomial with all real roots is 1011 (if achievable).

Wait, actually Descartes gives at most t-1 positive and t-1 negative roots, so at most 2(t-1) non-zero real roots. For 2019 non-zero real roots, we need 2(t-1) ≥ 2019, so t ≥ 1011 (since 2·1010 = 2020 ≥ 2019 but 2·1009 = 2018 < 2019). So t ≥ 1011.

If t = 1011, then we can have at most 2020 non-zero real roots, and we need 2019. So we need almost the maximum. This means the polynomial must have 1010 positive roots and 1009 negative roots (or vice versa), and the sign changes must be exactly t-1 = 1010 in both D(x) and D(-x).

This is very tight. Let me think about whether such a polynomial exists.

Consider the polynomial with terms at positions 0, 2, 4, ..., 2018, 2019. That's 1010 even positions + 1 odd position = 1011 terms. 

Hmm, let me think about this differently. Consider G(x) = (x-1)^{1010}(x+1)^{1009}. This has 1010 roots at 1 and 1009 roots at -1, total 2019 real roots.

The number of non-zero terms: (x-1)^{1010}(x+1)^{1009} = (x-1) · (x^2-1)^{1009}. As computed above, this has 2020 non-zero terms. Not sparse enough.

What about G(x) = (x-a)^{1010}(x+a)^{1009} for some a? Same structure, same number of terms.

Let me try a completely different approach. What about using roots that are not symmetric?

Actually, let me think about this problem differently. Maybe the answer isn't 3029.

Let me reconsider. Perhaps I should look at the problem from the perspective of: what is the maximum of r + s?

Let me think about small cases. Let degree = n (instead of 2020). 

For n = 1: P = a_0 + a_1 x, Q = b_0 + b_1 x, all coefficients non-zero, P ≠ Q.
- Common roots: r = 1 iff P and Q have the same root, i.e., -a_0/a_1 = -b_0/b_1, i.e., a_0 b_1 = a_1 b_0. If r = 1, then P = cQ, so s = 0 (c ≠ 1) or s = 2 (c = 1, P = Q, excluded). So r = 1, s = 0, r + s = 1.
- If r = 0: s can be 0 or 1 (s = 2 means P = Q). r + s = 0 or 1.
- Max r + s = 1.

For n = 1, the formula 2n - 1 = 1. ✓ (if answer is 2n - 1 = 4039 for n = 2020... no that doesn't match).

Hmm wait, let me recompute. For n = 1: max r + s = 1. 

For n = 2: P = a_0 + a_1 x + a_2 x^2, Q = b_0 + b_1 x + b_2 x^2, all non-zero, P ≠ Q.
- r ≤ 2. If r = 2, P = cQ, s = 0, r + s = 2.
- If r = 1: D = P - Q has at least 1 root. D has 3 - s non-zero terms. By Descartes, 1 ≤ 2(3-s-1) = 2(2-s). So s ≤ 1. r + s ≤ 2. Also r + s ≤ 1 + 1 = 2.
- If r = 0: s ≤ 2 (but s = 3 means P = Q). r + s ≤ 2.
- Max r + s = 2.

For n = 2, max = 2. Formula 2n - 2 = 2? Or just n = 2?

For n = 3:
- r = 3: P = cQ, s = 0, r + s = 3.
- r = 2: D has ≥ 2 roots. D has 4 - s non-zero terms. 2 ≤ 2(4-s-1) = 2(3-s). s ≤ 2. r + s ≤ 4. Also r + s ≤ 2 + 2 = 4.
- r = 1: 1 ≤ 2(3-s), s ≤ 2. r + s ≤ 3. Also ≤ 1 + 3 = 4 but s ≤ 2 from Descartes... wait, s can be up to 3 (but s = 4 means P = Q). If s = 3, D has 1 non-zero term, 1 ≤ 2(0) = 0? No, 1 ≤ 0 is false. So s ≤ 2 when r = 1. r + s ≤ 3.
- r = 0: s ≤ 3. r + s ≤ 3.
- Max r + s = 4 (from r = 2, s = 2).

Can we achieve r = 2, s = 2 for n = 3? P and Q share 2 roots, 2 common coefficients. D has 4 - 2 = 2 non-zero terms. D has degree ≤ 3, 2 non-zero terms, and at least 2 real roots. A binomial (2 terms) can have at most 1 positive and 1 negative root = 2 real roots. So we need exactly 2 real roots, one positive and one negative.

D = c x^a - c x^b = c x^a(1 - x^{b-a}) (assuming a < b). Roots: x = 0 (if a > 0) and x^{b-a} = 1. For real roots of x^{b-a} = 1: if b-a is even, x = ±1; if b-a is odd, x = 1. And x = 0 is a root only if a > 0, but 0 is not a common root of P and Q (since constant terms are non-zero). So the roots of D that are common roots must be non-zero.

If D = c(x^3 - x^2) = cx^2(x-1), roots at 0 (mult 2) and 1. But 0 is not a common root. So only 1 common root. Not enough.

If D = c(x^3 - x) = cx(x^2-1) = cx(x-1)(x+1), roots at 0, 1, -1. Only 1 and -1 are non-zero, so 2 common roots. ✓. D has 2 non-zero terms (at positions 1 and 3). So s = 4 - 2 = 2. ✓.

Now we need P and Q with D = P - Q = c(x^3 - x), sharing roots 1 and -1, all coefficients non-zero, degree 3.

P = (x-1)(x+1)(x - α) = (x^2-1)(x-α) = x^3 - αx^2 - x + α.
Q = P - D = x^3 - αx^2 - x + α - c(x^3 - x) = (1-c)x^3 - αx^2 + (c-1)x + α.

For all coefficients of P non-zero: 1, -α, -1, α all non-zero. Need α ≠ 0. ✓ (choose α ≠ 0).
For all coefficients of Q non-zero: (1-c), -α, (c-1), α. Need c ≠ 1 and α ≠ 0. ✓.

Common coefficients: P = [α, -1, -α, 1] (constant to x^3), Q = [α, (c-1), -α, (1-c)]. 
Common: position 0 (α = α ✓), position 2 (-α = -α ✓). Positions 1 and 3: -1 vs (c-1), 1 vs (1-c). These are equal when -1 = c-1 (c=0) and 1 = 1-c (c=0). If c = 0, D = 0, P = Q. So for c ≠ 0, 1, positions 1 and 3 are not common. s = 2. ✓.

r = 2 (roots 1 and -1). r + s = 4. ✓ for n = 3.

So for n = 3, max = 4 = 2·3 - 2.

For n = 1: max = 1 = 2·1 - 1.
For n = 2: max = 2 = 2·2 - 2.
For n = 3: max = 4 = 2·3 - 2.

Hmm, let me check n = 4.
- r = 4: P = cQ, s = 0, r + s = 4.
- r = 3: 3 ≤ 2(5-s-1) = 2(4-s). s ≤ 2 (since 2(4-2) = 4 ≥ 3, 2(4-3) = 2 < 3). Wait, 2(4-s) ≥ 3, so 4-s ≥ 1.5, s ≤ 2. r + s ≤ 5. Also r + s ≤ 3 + 2 = 5.
- r = 2: 2 ≤ 2(4-s), s ≤ 3. r + s ≤ 5. Also ≤ 2 + 3 = 5.
- r = 1: 1 ≤ 2(4-s), s ≤ 3. r + s ≤ 4. Also ≤ 1 + 4 = 5 but s ≤ 3 from Descartes.
- r = 0: s ≤ 4 (s=5 means P=Q). r + s ≤ 4.
- Max r + s = 5 = 2·4 - 3?

Hmm, that doesn't fit a clean pattern. Let me recheck.

For n = 4, max = 5. 2n - 3 = 5. 

n=1: 2n-1 = 1. n=2: 2n-2 = 2. n=3: 2n-2 = 4. n=4: 2n-3 = 5.

That's not clean. Let me recheck n = 4 more carefully.

For n = 4, r = 3, s = 2: r + s = 5. Is this achievable?

D has 5 - 2 = 3 non-zero terms, degree ≤ 4, at least 3 real roots (non-zero). By Descartes, 3 ≤ 2(3-1) = 4. ✓.

D = G · H where deg G = 3, deg H ≤ 1. If H is constant (a = b case), D = const · G, 3 non-zero terms, 3 real roots. G has degree 3, 3 non-zero terms, 3 real roots.

A trinomial of degree 3 with 3 real roots: e.g., x^3 - x = x(x-1)(x+1) has 3 real roots but root at 0. We need non-zero roots. x^3 - x has a root at 0 which is not allowed.

What about x^3 + ax^2 + bx + c with 3 non-zero terms (one coefficient is 0)? If we drop the x^2 term: x^3 + bx + c. This can have 3 real roots if 4b^3 + 27c^2 < 0 (discriminant condition). E.g., x^3 - 7x + 6 = (x-1)(x-2)(x+3). Roots 1, 2, -3, all non-zero. ✓. Non-zero terms: x^3, -7x, 6. That's 3 terms (positions 0, 1, 3; position 2 is zero). ✓.

So G = x^3 - 7x + 6 = (x-1)(x-2)(x+3). D = c · G for some constant c. 

P = G · (x - α) = (x-1)(x-2)(x+3)(x-α). Q = G · (x - β) = (x-1)(x-2)(x+3)(x-β). α ≠ β.

D = G · (β - α) = (β - α)(x^3 - 7x + 6). Non-zero terms at positions 0, 1, 3 (and degree 3, so position 4 is 0). Wait, D has degree 3, but P and Q have degree 4. So D's coefficient at position 4 is 0 (since P and Q have the same leading coefficient, both being G · (x - α) and G · (x - β) with leading coefficient 1).

D = (β-α)(x^3 - 7x + 6). Non-zero terms at positions 0, 1, 3. Position 2 and 4 are zero. So s = 2 (positions 2 and 4 have equal coefficients in P and Q).

P = (x^3 - 7x + 6)(x - α) = x^4 - αx^3 - 7x^2 + 7αx + 6x - 6α = x^4 - αx^3 - 7x^2 + (7α+6)x - 6α.
Q = (x^3 - 7x + 6)(x - β) = x^4 - βx^3 - 7x^2 + (7β+6)x - 6β.

Coefficients:
P: [-6α, 7α+6, -7, -α, 1]
Q: [-6β, 7β+6, -7, -β, 1]

Common coefficients: position 2 (-7 = -7 ✓), position 4 (1 = 1 ✓). Positions 0, 1, 3 differ (since α ≠ β). So s = 2. ✓.

All coefficients non-zero: need α ≠ 0, 7α+6 ≠ 0, -α ≠ 0 (same as α ≠ 0). And β ≠ 0, 7β+6 ≠ 0. Choose α = 1, β = 2: 7·1+6 = 13 ≠ 0, 7·2+6 = 20 ≠ 0. ✓.

r = 3 (roots 1, 2, -3). s = 2. r + s = 5. ✓ for n = 4.

So the pattern: n=1: 1, n=2: 2, n=3: 4, n=4: 5.

Let me compute more carefully. The bound is r + s ≤ min(2n - s, n + s) for r ≤ n-1 (when r = n, r + s = n). Wait, let me redo.

For general n (degree n):
- D has n + 1 - s non-zero terms.
- r ≤ 2(n - s) [Descartes, since D has n+1-s terms, at most 2(n-s) non-zero real roots].
- r ≤ n [degree].
- If r = n, P = cQ, s = 0, r + s = n.

For r ≤ n - 1: r + s ≤ min(2(n-s) + s, (n-1) + s) = min(2n - s, n - 1 + s).

2n - s = n - 1 + s when s = (n+1)/2.

If n is odd, s = (n+1)/2: r + s ≤ 2n - (n+1)/2 = (3n-1)/2 = n - 1 + (n+1)/2 = (3n-1)/2.
If n is even, s = n/2 or s = n/2 + 1:
  s = n/2: r + s ≤ min(2n - n/2, n - 1 + n/2) = min(3n/2, 3n/2 - 1) = 3n/2 - 1.
  s = n/2 + 1: r + s ≤ min(2n - n/2 - 1, n - 1 + n/2 + 1) = min(3n/2 - 1, 3n/2) = 3n/2 - 1.

So for even n: max r + s = 3n/2 - 1 (for r ≤ n-1). Compare with r = n giving n. For n ≥ 2, 3n/2 - 1 ≥ n iff n/2 ≥ 1 iff n ≥ 2. So for even n ≥ 2, max = 3n/2 - 1.

For odd n: max r + s = (3n-1)/2 (for r ≤ n-1). Compare with n. (3n-1)/2 ≥ n iff n ≥ 1. So for odd n ≥ 1, max = (3n-1)/2.

Let me verify: 
n = 1 (odd): (3-1)/2 = 1. ✓
n = 2 (even): 3·2/2 - 1 = 2. ✓
n = 3 (odd): (9-1)/2 = 4. ✓
n = 4 (even): 3·4/2 - 1 = 5. ✓

For n = 2020 (even): max = 3·2020/2 - 1 = 3030 - 1 = 3029.

So the answer should be 3029, provided it's achievable.

Now I need to verify achievability for n = 2020. We need r = 2019, s = 1010 (or r = 2018, s = 1011, etc., all giving 3029).

Let me try r = 2019, s = 1010. We need:
- P, Q degree 2020, all coefficients non-zero.
- 2019 common real roots (counting multiplicity).
- 1010 common coefficients.
- P ≠ Q.

Construction: P = G · (x - α), Q = G · (x - β), where G has degree 2019, all real roots (non-zero), and G has exactly 1011 non-zero terms. Then D = (β - α) · G, which has 1011 non-zero terms, so s = 2021 - 1011 = 1010. And r = 2019 (all roots of G). ✓.

But we also need all coefficients of P and Q to be non-zero. P = G · (x - α) has coefficients that are combinations of G's coefficients and α. We need to choose α, β, and G carefully.

The key question: does there exist a degree 2019 polynomial G with all real (non-zero) roots and exactly 1011 non-zero terms?

By Descartes, a polynomial with t non-zero terms has at most 2(t-1) non-zero real roots. For t = 1011, max roots = 2020. We need 2019 roots. So we need 2019 ≤ 2020. ✓.

But existence is the question. Let me think about constructing such a polynomial.

Consider G(x) = (x - 1)^{1010} (x + 1)^{1009}. This has 2019 real roots (all non-zero). How many non-zero terms?

(x-1)^{1010}(x+1)^{1009} = (x-1) · (x^2-1)^{1009}. 

(x^2-1)^{1009} = ∑_{k=0}^{1009} C(1009,k) (-1)^{1009-k} x^{2k}. This has 1010 non-zero terms at even positions 0, 2, 4, ..., 2018.

(x-1) · (x^2-1)^{1009} = x · (x^2-1)^{1009} - (x^2-1)^{1009}.

x · (x^2-1)^{1009}: terms at odd positions 1, 3, 5, ..., 2019. (1010 terms)
-(x^2-1)^{1009}: terms at even positions 0, 2, 4, ..., 2018. (1010 terms)

Total: 2020 non-zero terms (all positions 0 to 2019). Not sparse enough.

What if I use G(x) = (x^2 - 1)^{1009} · x? No, that has a root at 0.

What about G(x) = (x^2 - a^2)^{1009} · (x^2 - b^2)^{?}... no, that would have even degree.

Let me think differently. I need a degree 2019 polynomial with 1011 non-zero terms and all 2019 roots real and non-zero.

What about a polynomial of the form x^{2019} + a_{2017} x^{2017} + a_{2015} x^{2015} + ... + a_1 x + a_0, i.e., only odd and even powers... no, degree 2019 is odd.

Hmm, let me think about this. A polynomial with 1011 non-zero terms and 2019 real roots. The maximum number of real roots for 1011 terms is 2·1010 = 2020. We need 2019, which is 1 less than the maximum.

For a polynomial to achieve close to the maximum number of real roots, it needs close to the maximum number of sign changes in both D(x) and D(-x).

Let me consider the polynomial:
G(x) = (x - 1)(x - 2)(x - 3)...(x - 2019)

This has 2019 real roots, all non-zero. But it has 2020 non-zero terms (in general). We need to reduce to 1011 terms.

Actually, the number of non-zero terms depends on the specific roots. For generic roots, all 2020 coefficients are non-zero. We need to choose roots so that exactly 1009 coefficients vanish.

This seems very hard to do directly. Let me think of another approach.

What about using the structure (x^k - a^k) type polynomials? 

Consider G(x) = ∏_{j=1}^{m} (x^{d_j} - c_j) where the product of degrees is 2019. Each factor x^{d_j} - c_j has d_j real roots if d_j is odd (roots of c_j^{1/d_j}) or 2 real roots if d_j is even (±c_j^{1/d_j}). Wait, x^d - c has real roots: if d is odd, 1 real root; if d is even and c > 0, 2 real roots; if d is even and c < 0, 0 real roots.

Hmm, this is getting complicated. Let me think about it differently.

What about G(x) = (x^2 - 1)^{1009} · (x - c) for some c ≠ 0, ±1? 

(x^2 - 1)^{1009} has 1010 non-zero terms (at even positions). Multiplying by (x - c):
- x · (x^2-1)^{1009}: 1010 terms at odd positions.
- -c · (x^2-1)^{1009}: 1010 terms at even positions.
Total: 2020 terms. Same problem.

The issue is that multiplying by a linear factor doubles the number of terms (roughly).

What if G has a special structure where many coefficients are already zero?

Let me try: G(x) = x^{2019} - a. This has 2 non-zero terms. Roots: x^{2019} = a. If a > 0, one real root (x = a^{1/2019}). Only 1 real root, not 2019.

What about G(x) = (x^{2019} - 1)/(x - 1) = x^{2018} + x^{2017} + ... + x + 1? This has 2019 non-zero terms (all coefficients 1) and roots are the 2019th roots of unity except 1. These are complex, not real. So 0 real roots. Bad.

Let me try a different approach. What about G(x) = (x - 1)^{2019}? This has 2019 roots (all at 1). The number of non-zero terms: (x-1)^{2019} = ∑ C(2019,k) x^k (-1)^{2019-k}. All 2020 coefficients are non-zero (binomial coefficients are all non-zero). So 2020 terms. Not sparse.

What about (x - 1)^a (x + 1)^b where a + b = 2019? As we saw, this gives 2020 terms.

Hmm. Let me think about whether a degree 2019 polynomial with 1011 non-zero terms and all 2019 roots real can exist.

Actually, let me think about this more carefully using the theory of fewnomials. 

A polynomial with t non-zero terms (a t-nomial) of degree d has at most 2(t-1) non-zero real roots (by Descartes). This bound is tight: the polynomial ∏_{i=1}^{t-1} (x - a_i)(x + b_i) for appropriate a_i, b_i > 0 can be written as a t-nomial... no, that's not right.

Actually, the Descartes bound is tight in the sense that for any t, there exist t-nomials with exactly 2(t-1) real roots. For example, (x-1)(x-2)...(x-(t-1)) · (x+1)(x+2)...(x+(t-1)) has 2(t-1) real roots, but it's not a t-nomial in general.

The question is: can a t-nomial achieve 2(t-1) real roots? 

Consider the polynomial p(x) = (x^{2(t-1)} - 1) / (x^2 - 1) if... no.

Actually, x^{2(t-1)} - 1 = (x-1)(x+1)(x^{2(t-1)-2} + x^{2(t-1)-4} + ... + 1). This is a binomial (2 terms) with 2 real roots. Not helpful.

Let me think about trinomials. A trinomial x^a + bx^c + d has at most 4 real roots (by Descartes, 2 positive + 2 negative). Can it achieve 4? 

x^4 - 5x^2 + 4 = (x^2-1)(x^2-4) = (x-1)(x+1)(x-2)(x+2). This is a trinomial (terms at 0, 2, 4) with 4 real roots. ✓! So a trinomial can achieve 4 = 2(3-1) real roots.

More generally, x^{2m} - (sum)x^{2(m-1)} + ... hmm, let me think about the pattern.

x^{2m} - a_1 x^{2(m-1)} + a_2 x^{2(m-2)} - ... ± a_m. This is a polynomial in x^2 with m+1 terms. If it factors as ∏(x^2 - r_i^2) with all r_i real and non-zero, it has 2m real roots and m+1 non-zero terms. So a (m+1)-nomial with 2m real roots. Here t = m+1, roots = 2m = 2(t-1). This achieves the Descartes bound!

So G(x) = ∏_{i=1}^{m} (x^2 - r_i^2) has degree 2m, m+1 non-zero terms (all at even positions), and 2m real roots. But degree 2m is even, and we need degree 2019 (odd).

For odd degree, we can multiply by (x - c): G(x) = (x - c) · ∏_{i=1}^{m} (x^2 - r_i^2). Degree 2m + 1. 

(x - c) · ∏(x^2 - r_i^2): The product ∏(x^2 - r_i^2) has m+1 terms at even positions 0, 2, ..., 2m. Multiplying by (x - c):
- x · product: m+1 terms at odd positions 1, 3, ..., 2m+1.
- -c · product: m+1 terms at even positions 0, 2, ..., 2m.
Total: 2(m+1) terms (all positions 0 to 2m+1), assuming no cancellation. So 2m+2 terms, degree 2m+1.

For degree 2019 = 2m+1, m = 1009. Number of terms = 2·1010 = 2020. Still too many.

The problem is that multiplying by (x - c) doubles the terms. 

What if instead we use a different structure for odd degree?

Consider G(x) = (x - c) · ∏(x^2 - r_i^2) where c = 0? No, c must be non-zero (root must be non-zero).

Alternatively, what if some coefficients cancel? If c is chosen so that some even-position coefficient from -c · product cancels with an odd-position coefficient from x · product... but they're at different positions, so no cancellation.

Hmm. So for odd degree, the approach of (x-c)·∏(x^2 - r_i^2) gives 2m+2 terms, not m+2.

Let me think differently. What about G(x) = (x^3 - a^3) · ∏(x^2 - r_i^2)? 

x^3 - a^3 = (x - a)(x^2 + ax + a^2). This has 1 real root (x = a) and 2 complex roots. So G has 2m + 1 real roots (1 from x^3 - a^3, 2m from the product), degree 2m + 3.

x^3 - a^3 has 2 non-zero terms. ∏(x^2 - r_i^2) has m+1 non-zero terms at even positions. Product: terms at positions that are sums of {0, 3} and {0, 2, 4, ..., 2m}. So positions: {0, 2, 4, ..., 2m} ∪ {3, 5, 7, ..., 2m+3}. That's (m+1) + (m+1) = 2m+2 terms, assuming no overlap. Overlap occurs when an even position equals an odd position, which never happens. So 2m+2 terms, degree 2m+3.

For degree 2019 = 2m + 3, m = 1008. Terms = 2·1009 = 2018. Still too many (we need 1011).

What about using higher-power factors? G(x) = (x^k - a^k) · ∏(x^{2j} - r_j^{2j})?

Actually, let me think about this more carefully. The key insight is:

A polynomial in x^d (i.e., with terms only at positions that are multiples of d) with t non-zero terms has at most 2(t-1) non-zero real roots... no wait, that's not quite right.

Let me think about it as follows. If G(x) = f(x^d) for some polynomial f of degree m, then G has degree dm, and the non-zero terms of G are at positions 0, d, 2d, ..., md. So G has at most m+1 non-zero terms. The real roots of G are the d-th roots of the real roots of f. If f has a positive real root r, then x^d = r has 2 real roots if d is even, 1 if d is odd. If f has a negative real root r, then x^d = r has 0 real roots if d is even, 1 if d is odd.

So if d is odd: each real root of f gives exactly 1 real root of G. If f has m real roots (all non-zero), G has m real roots, with m+1 non-zero terms, degree dm.

For G to have degree 2019 with m+1 non-zero terms and m real roots: dm = 2019, and we want m+1 = 1011, so m = 1010, d = 2019/1010. But 2019/1010 is not an integer. So this doesn't work directly.

What if d = 3? Then m = 2019/3 = 673. G(x) = f(x^3) where f has degree 673. G has 673 real roots (if f has 673 real roots, all non-zero) and 674 non-zero terms. s = 2021 - 674 = 1347. r + s = 673 + 1347 = 2020. Not great.

What if d = 2019? Then m = 1. G(x) = f(x^{2019}) = a x^{2019} + b. 2 terms, 1 real root. r + s = 1 + 2019 = 2020.

What about d = 1? Then G = f(x), degree 2019, up to 2020 terms. Not sparse.

The issue is that for G(x) = f(x^d) with d odd, we get m = 2019/d real roots and m+1 non-zero terms, giving r + s = m + (2021 - (m+1)) = m + 2020 - m = 2020. Always 2020 regardless of d!

So this approach always gives r + s = 2020. Not helpful for getting 3029.

Let me think about mixed approaches. What if G is not of the form f(x^d) but has a more complex sparse structure?

Actually, I think the key is to not require G to have all its roots be real. Wait, no — r is the number of common real roots, so G's roots (which are the common roots) must all be real.

Hmm, let me reconsider. Maybe I need a different construction where D is not just a scalar multiple of G.

Let me go back to the general setup. P = G · P_1, Q = G · Q_1, D = G · (P_1 - Q_1) = G · H. 

If H is not a constant, then D = G · H has more non-zero terms than G alone, but also H might contribute to making D sparser through cancellations.

Actually, the number of non-zero terms of D is fixed at 2021 - s. The number of real roots of D is r + (real roots of H). By Descartes, r + (real roots of H) ≤ 2(2020 - s).

To maximize r + s, we want r as large as possible and s as large as possible. The constraint is r ≤ 2(2020 - s) - (real roots of H). If H has no real roots, r ≤ 2(2020 - s).

But can H have no real roots? H = P_1 - Q_1, deg H ≤ 2020 - r. If 2020 - r is even, H could have no real roots. If 2020 - r is odd, H must have at least 1 real root (odd degree polynomial has at least one real root).

For r = 2019: 2020 - r = 1, H has degree ≤ 1. If H has degree 1, it has 1 real root. If H has degree 0 (constant), it has 0 real roots. H has degree 0 when P_1 and Q_1 have the same leading coefficient.

So for r = 2019, if H is a non-zero constant, D = const · G, and D has the same non-zero terms as G. We need G to have 2021 - s non-zero terms. And r = 2019 ≤ 2(2020 - s), so s ≤ 1010. r + s ≤ 3029.

For this to work, we need G of degree 2019 with 1011 non-zero terms and 2019 real roots. As I discussed, this requires a very sparse polynomial with many real roots.

Let me try yet another approach. What about:

G(x) = (x^2 - 1)^{1009} · (x - c) where c is chosen specially.

Wait, I showed this gives 2020 terms. But what if c = 0? Then G = x · (x^2-1)^{1009}, which has a root at 0. Not allowed.

What if c = 1? G = (x-1)^{1010} (x+1)^{1009}. Still 2020 terms.

What if c = -1? G = (x-1)^{1009} (x+1)^{1010}. Still 2020 terms.

Hmm. Let me think about whether there's a degree 2019 polynomial with 1011 non-zero terms and 2019 real roots.

Actually, let me think about this more carefully. Consider:

G(x) = ∏_{i=1}^{1010} (x - a_i)(x + a_i) · (x - c) = (x - c) · ∏_{i=1}^{1010} (x^2 - a_i^2)

where all a_i > 0 and c > 0 (or c < 0). This has degree 2·1010 + 1 = 2021. Too high.

For degree 2019: ∏_{i=1}^{1009} (x^2 - a_i^2) · (x - c), degree 2·1009 + 1 = 2019. ✓.

∏_{i=1}^{1009} (x^2 - a_i^2) has 1010 non-zero terms (at even positions 0, 2, ..., 2018). Multiplying by (x - c):
- x · product: 1010 terms at odd positions 1, 3, ..., 2019.
- -c · product: 1010 terms at even positions 0, 2, ..., 2018.
Total: 2020 terms. 

The only way to reduce terms is through cancellation, but odd and even positions don't overlap. So we always get 2020 terms. 

So the (x-c)·∏(x^2 - a_i^2) approach can't give 1011 terms for odd degree.

Let me think about a fundamentally different construction.

What about G(x) = ∏_{j=1}^{k} (x^{d_j} - c_j) where ∑ d_j = 2019, each d_j odd (so each factor has 1 real root), and the product has few non-zero terms?

Each factor x^{d_j} - c_j has 2 non-zero terms. The product of k binomials has at most 2^k non-zero terms (by convolution). But we can choose the d_j and c_j to create cancellations.

For example, (x^a - c)(x^b - c) = x^{a+b} - c·x^a - c·x^b + c^2. If a = b, this is x^{2a} - 2c·x^a + c^2 = (x^a - c)^2, which has 3 non-zero terms. But (x^a - c)^2 has only 1 distinct real root (with multiplicity 2), not 2.

Actually, (x^a - c)(x^b - c) with a ≠ b: 4 non-zero terms (at positions 0, a, b, a+b), assuming a, b, a+b are all distinct and non-zero. This gives 2 real roots (one from each factor, since a, b odd). 4 terms, 2 roots.

What about (x^a - c_1)(x^a - c_2) = x^{2a} - (c_1+c_2)x^a + c_1 c_2. 3 non-zero terms, 2 real roots (x = c_1^{1/a} and x = c_2^{1/a}). Degree 2a.

So for a = 1009, degree 2018, 3 non-zero terms, 2 real roots. But we need degree 2019 and 2019 real roots.

This approach gives very few roots relative to degree. Not useful.

Let me think about the problem differently. Maybe the answer isn't 3029.

Let me reconsider. Perhaps the bound r ≤ 2(2020 - s) is not tight when combined with the constraint that all coefficients of P and Q are non-zero.

Actually, wait. Let me reconsider the Descartes bound more carefully. D has 2021 - s non-zero terms. But D might have degree less than 2020 (if the leading coefficients of P and Q are equal, i.e., s includes position 2020). 

If position 2020 is a common coefficient (a_{2020} = b_{2020}), then deg D < 2020. In this case, the number of non-zero terms of D is still 2021 - s, but the degree is less than 2020.

Descartes' rule: number of positive roots ≤ number of sign changes ≤ (number of non-zero terms - 1). This is independent of the degree. So the bound r ≤ 2(2020 - s) still holds.

But there's a subtlety: if deg D = d < 2020, and D has t = 2021 - s non-zero terms, then D has at most d real roots (counting multiplicity). So r ≤ d. And d ≤ 2020 - 1 = 2019 if the leading coefficients are equal.

Hmm, but this doesn't change the fundamental bound much.

Let me reconsider the problem. Maybe I should think about it as follows:

We want to maximize r + s where:
- r = number of common real roots (with multiplicity) of P and Q
- s = number of common coefficients
- P, Q distinct, degree 2020, all coefficients non-zero

D = P - Q, t = 2021 - s non-zero terms, r ≤ (real roots of D) ≤ 2(t-1) = 2(2020 - s).
Also r ≤ 2020 (and r = 2020 ⟹ P = cQ, s = 0, r + s = 2020).

For r ≤ 2019: r + s ≤ min(2(2020-s) + s, 2019 + s) = min(4040 - s, 2019 + s).
Maximized at s = 1010 or 1011, giving 3029 or 3029.

So the upper bound is 3029. The question is whether it's achievable.

Let me try a different construction. Instead of requiring H to be constant, let me allow H to be non-constant but have no real roots.

For r = 2019, s = 1010: D has 1011 non-zero terms, degree ≤ 2020. D = G · H, deg G = 2019, deg H ≤ 1. If deg H = 1, H has 1 real root, so D has 2020 real roots, but r = 2019 (the extra root is from H, not a common root). By Descartes, 2020 ≤ 2(1011 - 1) = 2020. ✓ (tight!).

So if deg H = 1, D has 2020 real roots (2019 from G, 1 from H), and D has 1011 non-zero terms. By Descartes, this is exactly the maximum: 2(1011-1) = 2020 real roots. This is achievable if D has the maximum number of sign changes.

So the question becomes: can we find D with 1011 non-zero terms, degree 2020, and 2020 real roots (all non-zero)?

A polynomial with t non-zero terms and 2(t-1) real roots is called a polynomial that achieves the Descartes bound. As I noted, ∏(x^2 - r_i^2) with t-1 factors has t non-zero terms and 2(t-1) real roots, degree 2(t-1).

For t = 1011: ∏_{i=1}^{1010} (x^2 - r_i^2) has 1011 non-zero terms, 2020 real roots, degree 2020. ✓!

So D(x) = ∏_{i=1}^{1010} (x^2 - r_i^2) for some positive r_i. This has:
- Degree 2020 ✓
- 1011 non-zero terms (at even positions 0, 2, 4, ..., 2020) ✓
- 2020 real roots (±r_i for each i) ✓
- All roots non-zero (if r_i ≠ 0) ✓

Now, D = P - Q. We need to decompose D into P and Q such that:
1. P and Q have degree 2020 with all non-zero coefficients.
2. P and Q share 2019 of the 2020 roots of D (the 2020th root is the "extra" root from H).
3. s = 1010 common coefficients.

Wait, actually, let me reconsider. D has 2020 real roots. The common roots of P and Q are a subset of these. We want r = 2019, so exactly 2019 of D's roots are common roots, and 1 is not.

D = G · H where G has degree 2019 (the 2019 common roots) and H has degree 1 (the 1 extra root). 

D = ∏_{i=1}^{1010} (x^2 - r_i^2) = ∏_{i=1}^{1010} (x - r_i)(x + r_i). This has 2020 linear factors. We need to split them into G (2019 factors) and H (1 factor).

H = (x - α) for some root α of D. G = D / (x - α) = ∏_{j ≠ α} (x - β_j) (product of remaining 2019 factors).

P = G · P_1, Q = G · Q_1, where P_1 - Q_1 = H = (x - α), and P_1, Q_1 have degree 1. So P_1 = x - β, Q_1 = x - γ, with (x - β) - (x - γ) = γ - β = H... wait, H = x - α, so P_1 - Q_1 = x - α. If P_1 = x - β and Q_1 = x - γ, then P_1 - Q_1 = γ - β, a constant. That's degree 0, not degree 1.

For H to have degree 1, we need P_1 and Q_1 to have different leading coefficients. P_1 = a(x - β), Q_1 = b(x - γ), P_1 - Q_1 = (a-b)x - (aβ - bγ). For this to equal x - α (up to scaling), we need a ≠ b.

Let me set P_1 = a(x - β), Q_1 = b(x - γ), with a ≠ b. Then H = (a-b)x - (aβ - bγ). H has root at x = (aβ - bγ)/(a - b). We need this root to be one of the roots of D, say α. So (aβ - bγ)/(a - b) = α.

P = G · a(x - β) = a · G · (x - β). Q = G · b(x - γ) = b · G · (x - γ).

The roots of P are: roots of G (2019 roots) plus β. The roots of Q are: roots of G (2019 roots) plus γ. Common roots: roots of G (assuming β and γ are not roots of G, and β ≠ γ). So r = 2019. ✓.

Now, D = P - Q = G · ((a-b)x - (aβ - bγ)) = G · H. And H = (a-b)(x - α). So D = (a-b) · G · (x - α) = (a-b) · D/(x-α) · (x-α) = (a-b) · D. 

Wait, that's circular. D = (a-b) · D, which means a - b = 1. OK so let me just set a - b = 1 (WLOG by scaling).

Actually, D = P - Q = G · (P_1 - Q_1) = G · H. And we want D = ∏(x^2 - r_i^2). So G · H = ∏(x^2 - r_i^2). H = (x - α) (up to constant), G = ∏(x^2 - r_i^2) / (x - α).

Now, P = G · P_1, Q = G · Q_1, P_1 - Q_1 = H (up to the constant). 

Let's be concrete. Let D(x) = ∏_{i=1}^{1010} (x^2 - i^2) = (x^2 - 1)(x^2 - 4)(x^2 - 9)...(x^2 - 1010^2). This has 2020 non-zero real roots: ±1, ±2, ..., ±1010. And 1011 non-zero terms (at even positions).

Let α = 1 (one of the roots). H = x - 1. G = D / (x - 1) = (x + 1) · ∏_{i=2}^{1010} (x^2 - i^2). G has degree 2019 and 2019 real roots: -1, ±2, ±3, ..., ±1010.

P_1 - Q_1 = H = x - 1. Let P_1 = x - β, Q_1 = x - γ, then P_1 - Q_1 = γ - β = x - 1? No, that's a constant, not x - 1.

I need P_1 - Q_1 = x - 1 (degree 1). So P_1 and Q_1 must have different leading coefficients. Let P_1 = 2x - 2β, Q_1 = x - γ. Then P_1 - Q_1 = x - (2β - γ). We need 2β - γ = 1 (so that H = x - 1). 

P = G · (2x - 2β) = 2G(x - β). Q = G · (x - γ).

Roots of P: roots of G plus β. Roots of Q: roots of G plus γ. For r = 2019, we need β and γ to not be roots of G, and β ≠ γ. G's roots are -1, ±2, ..., ±1010. So β, γ ∉ {-1, ±2, ..., ±1010} and β ≠ γ and 2β - γ = 1.

Choose β = 0, γ = -1. But γ = -1 is a root of G. Bad.
Choose β = 1/2, γ = 0. γ = 0 is not a root of G (G's roots are all non-zero integers from the set). β = 1/2 is not a root of G. β ≠ γ. 2(1/2) - 0 = 1. ✓.

But wait, we need all coefficients of P and Q to be non-zero. P = 2G(x - 1/2), Q = G(x - 0) = G · x. But Q = G · x has a root at 0, meaning the constant term of Q is 0. But we need all coefficients non-zero! So γ = 0 doesn't work.

Let me choose β = 3/2, γ = 2. But γ = 2 is a root of G. Bad.
β = 1/2, γ = 0: γ = 0 gives Q = Gx, constant term 0. Bad.
β = 3, γ = 5: 2·3 - 5 = 1. ✓. β = 3 is a root of G (since 3 is in {±2, ..., ±1010}). Bad.
β = 1/2, γ = 0: already tried.
β = -1/2, γ = -2: γ = -2 is a root of G. Bad.
β = 1011/2, γ = 1010: γ = 1010 is a root of G. Bad.
β = 1011, γ = 2021: 2·1011 - 2021 = 1. ✓. β = 1011 is not a root of G (roots are ±1, ..., ±1010). γ = 2021 is not a root of G. ✓. β ≠ γ. ✓.

So P = 2G(x - 1011), Q = G(x - 2021).

Now, all coefficients of P and Q must be non-zero. P = 2G · (x - 1011). G = (x+1)∏_{i=2}^{1010}(x^2 - i^2). 

The coefficients of G: G is a product of linear factors with integer roots. The coefficients are (up to sign) elementary symmetric polynomials of the roots. Since the roots are distinct non-zero integers, the elementary symmetric polynomials are all non-zero (as long as no subset of roots sums to zero in a way that cancels a coefficient). Actually, it's not guaranteed that all coefficients are non-zero.

Hmm, this is a potential issue. Let me think about whether G = (x+1)∏_{i=2}^{1010}(x^2 - i^2) has all non-zero coefficients.

Actually, G = D/(x-1) where D = ∏_{i=1}^{1010}(x^2 - i^2). D has non-zero terms only at even positions. D/(x-1): since D(-1) = ∏((-1)^2 - i^2) = ∏(1 - i^2) = 0 (since i=1 gives 0). Wait, D = ∏(x^2 - i^2), so D(1) = ∏(1 - i^2) = 0 (the i=1 factor). So (x-1) divides D. ✓.

G = D/(x-1). D has terms at even positions. Dividing by (x-1): 

If D(x) = ∑_{k=0}^{1010} c_k x^{2k}, then D(x)/(x-1) = D(x) · (1/(x-1)). Since D(1) = 0, (x-1) | D. 

G(x) = D(x)/(x-1). G has degree 2019. The coefficients of G: since D has only even powers and we're dividing by (x-1), G will have terms at all positions 0 through 2019 (both even and odd). 

Specifically, if D(x) = (x-1) · G(x), and D has terms at even positions only, then:
- The odd-position terms of (x-1)·G = x·G - G must cancel. 
- x·G has terms at positions {j+1 : j is a position of G's non-zero term}.
- G has terms at positions {j : j is a position of G's non-zero term}.
- For (x-1)G to have only even positions, the odd-position terms of xG must cancel with the odd-position terms of G, and the even-position terms of xG must cancel with the even-position terms of G (except for the overall even structure).

Actually, let me think about it differently. D = (x-1)G, D has non-zero terms only at even positions 0, 2, 4, ..., 2020. 

(x-1)G = xG - G. If G = ∑_{j=0}^{2019} g_j x^j, then xG = ∑ g_j x^{j+1}, and (x-1)G = ∑ g_j x^{j+1} - ∑ g_j x^j = -g_0 + ∑_{j=1}^{2019} (g_{j-1} - g_j) x^j + g_{2019} x^{2020}.

For D to have non-zero terms only at even positions:
- g_0 ≠ 0 (constant term of D is -g_0, at position 0 which is even) ✓
- g_{j-1} - g_j = 0 for odd j (positions 1, 3, 5, ..., 2019)
- g_{j-1} - g_j ≠ 0 for even j (positions 2, 4, ..., 2018)
- g_{2019} ≠ 0 (position 2020, even) ✓

From g_{j-1} = g_j for odd j: g_0 = g_1, g_2 = g_3, g_4 = g_5, ..., g_{2018} = g_{2019}.

So G has the property that consecutive pairs of coefficients are equal: (g_0, g_1), (g_2, g_3), ..., (g_{2018}, g_{2019}) with g_{2k} = g_{2k+1}.

And the even-position coefficients of D are: d_0 = -g_0, d_{2k} = g_{2k-1} - g_{2k} for k ≥ 1, d_{2020} = g_{2019}.

Since g_{2k-1} = g_{2k-2} (from the pairing with index 2k-2 being even, 2k-1 being odd), we get d_{2k} = g_{2k-2} - g_{2k}.

So the even coefficients of D form a "difference sequence" of the even coefficients of G. Specifically, if we let h_k = g_{2k} = g_{2k+1} for k = 0, 1, ..., 1009, then:
- d_0 = -h_0
- d_{2k} = h_{k-1} - h_k for k = 1, ..., 1009
- d_{2020} = h_{1009}

And D = ∑_{k=0}^{1010} d_{2k} x^{2k} with all d_{2k} ≠ 0 (since D = ∏(x^2 - i^2) has all non-zero coefficients at even positions — is this true?).

D = ∏_{i=1}^{1010} (x^2 - i^2). The coefficient of x^{2k} in D is (-1)^{1010-k} e_{1010-k}(1^2, 2^2, ..., 1010^2) where e_j is the j-th elementary symmetric polynomial. All these are non-zero since 1^2, 2^2, ..., 1010^2 are all positive and distinct. ✓.

So all d_{2k} ≠ 0, which means:
- h_0 ≠ 0 (from d_0 = -h_0)
- h_{k-1} ≠ h_k for k = 1, ..., 1009 (from d_{2k} = h_{k-1} - h_k ≠ 0)
- h_{1009} ≠ 0 (from d_{2020} = h_{1009})

So all h_k ≠ 0 (h_0 ≠ 0, and h_k ≠ h_{k-1} doesn't directly imply h_k ≠ 0, but...). Actually, h_0 ≠ 0, h_0 ≠ h_1, h_1 ≠ h_2, ..., h_{1008} ≠ h_{1009}, h_{1009} ≠ 0. This doesn't directly imply all h_k ≠ 0. For example, h_1 could be 0 as long as h_0 ≠ 0 and h_1 ≠ h_2.

Hmm, so some h_k could be 0, meaning some g_{2k} = g_{2k+1} = 0, meaning G has some zero coefficients. But we need all coefficients of P and Q to be non-zero, and P = 2G(x - 1011), Q = G(x - 2021). 

If G has some zero coefficients, then P and Q might still have all non-zero coefficients (since multiplying by (x - c) mixes adjacent coefficients). Let me check.

P = 2G(x - 1011) = 2(xG - 1011G). If G = ∑ g_j x^j, then P = 2∑(g_{j-1} - 1011 g_j) x^j (with g_{-1} = 0). The coefficient of x^j in P is 2(g_{j-1} - 1011 g_j). For this to be non-zero, we need g_{j-1} ≠ 1011 g_j for all j.

Similarly, Q = G(x - 2021), coefficient of x^j is g_{j-1} - 2021 g_j, need g_{j-1} ≠ 2021 g_j.

Since g_{2k} = g_{2k+1} = h_k, the conditions become:
For P: h_{k-1} ≠ 1011 h_k and h_k ≠ 1011 h_{k+1} (roughly, need to be more careful with indexing).

Actually, let me be more precise. g_j = h_{⌊j/2⌋} for all j (since g_{2k} = g_{2k+1} = h_k).

Coefficient of x^j in P: 2(g_{j-1} - 1011 g_j) = 2(h_{⌊(j-1)/2⌋} - 1011 h_{⌊j/2⌋}).

For j = 2k: 2(h_{k-1} - 1011 h_k) (using ⌊(2k-1)/2⌋ = k-1 for k ≥ 1, and ⌊2k/2⌋ = k).
For j = 2k+1: 2(h_k - 1011 h_k) = 2h_k(1 - 1011) = -2020 h_k.

So for j odd: coefficient = -2020 h_k. This is non-zero iff h_k ≠ 0.
For j even (j = 2k, k ≥ 1): coefficient = 2(h_{k-1} - 1011 h_k). Non-zero iff h_{k-1} ≠ 1011 h_k.
For j = 0: coefficient = 2(0 - 1011 h_0) = -2022 h_0. Non-zero iff h_0 ≠ 0.

Similarly for Q:
For j = 2k+1: coefficient = -2020 h_k. Non-zero iff h_k ≠ 0.
For j = 2k (k ≥ 1): coefficient = h_{k-1} - 2021 h_k. Non-zero iff h_{k-1} ≠ 2021 h_k.
For j = 0: coefficient = -2021 h_0. Non-zero iff h_0 ≠ 0.

So we need:
1. All h_k ≠ 0 (k = 0, ..., 1009).
2. h_{k-1} ≠ 1011 h_k for all k = 1, ..., 1009 (for P's even coefficients).
3. h_{k-1} ≠ 2021 h_k for all k = 1, ..., 1009 (for Q's even coefficients).
4. h_0 ≠ 0 (already in condition 1).

And the h_k are determined by D = ∏(x^2 - i^2). Specifically:
h_0 = -d_0 = e_{1010}(1^2, ..., 1010^2) (up to sign)
h_k = h_0 - ∑_{j=1}^{k} d_{2j} (telescoping from h_{k-1} - h_k = d_{2k}).

Actually, h_k = h_0 - (d_2 + d_4 + ... + d_{2k}). And h_{1009} = d_{2020}.

These are specific values determined by the roots 1, 2, ..., 1010. We need to verify that all h_k ≠ 0 and the ratio conditions hold.

This seems hard to verify directly. But the key point is: we have freedom in choosing the roots r_1, ..., r_{1010} of D. We don't have to use 1, 2, ..., 1010. We can choose them to ensure all the conditions are met.

Actually, the conditions are:
1. h_k ≠ 0 for all k.
2. h_{k-1}/h_k ≠ 1011 and h_{k-1}/h_k ≠ 2021 for all k.

The h_k are continuous functions of the roots r_1, ..., r_{1010}. The conditions fail only on a measure-zero set (when some h_k = 0 or some ratio equals 1011 or 2021). So for generic choices of r_1, ..., r_{1010} (all positive and distinct), all conditions are satisfied.

Wait, but we also need G to have 2019 real roots (all non-zero). G = D/(x-1) where D = ∏(x^2 - r_i^2). G's roots are all roots of D except 1 (assuming 1 = r_1, i.e., we chose r_1 = 1). G's roots are -r_1, ±r_2, ..., ±r_{1010} = -1, ±r_2, ..., ±r_{1010}. All real and non-zero (if r_i > 0). ✓.

So for generic positive distinct r_1, ..., r_{1010} with r_1 = 1, the construction works:
- D = ∏(x^2 - r_i^2), 1011 non-zero terms, 2020 real roots.
- G = D/(x-1), degree 2019, 2019 real roots.
- P = 2G(x - 1011), Q = G(x - 2021), degree 2020, all coefficients non-zero (for generic r_i).
- r = 2019, s = 1010, r + s = 3029.

But wait, I need to also verify that the common coefficients are exactly 1010. D has 1011 non-zero terms at even positions 0, 2, ..., 2020. So D's zero coefficients are at odd positions 1, 3, ..., 2019 (1010 positions) plus... wait, D has degree 2020 and 2021 coefficients (positions 0 to 2020). 1011 non-zero (even positions) and 1010 zero (odd positions). So s = 1010. ✓.

And the common roots: P's roots are G's roots (2019 roots) plus 1011. Q's roots are G's roots (2019 roots) plus 2021. Common roots = G's roots = 2019 roots. ✓ (assuming 1011 and 2021 are not roots of G, which they aren't for generic r_i since G's roots are ±r_i and -r_1 = -1).

Wait, I need to double-check: is 1011 a root of G? G's roots are -1, r_2, -r_2, ..., r_{1010}, -r_{1010}. For 1011 to not be a root, we need r_i ≠ 1011 for all i. Since we can choose r_i freely (e.g., r_i = i for i = 1, ..., 1010, so max r_i = 1010 < 1011), this is fine. Similarly, 2021 is not a root.

Also, I assumed r_1 = 1 so that (x - 1) divides D. Let me re-examine. D = ∏_{i=1}^{1010} (x^2 - r_i^2). D(1) = ∏(1 - r_i^2). For (x-1) to divide D, we need D(1) = 0, so some r_i = 1. Let's say r_1 = 1. Then D(1) = 0 and (x-1) | D. ✓.

Actually, we could choose any root of D to be the "extra" root. Let me choose α to be any root, say α = r_1. Then G = D/(x - r_1), and G's roots are -r_1, ±r_2, ..., ±r_{1010}.

P = 2G(x - β), Q = G(x - γ), with 2β - γ = r_1 (so that P_1 - Q_1 = 2(x-β) - (x-γ) = x - (2β - γ) = x - r_1 = H). 

We need β, γ not roots of G, β ≠ γ, and all coefficients of P, Q non-zero.

Choose β = r_1 + 1, γ = r_1 + 2 (then 2β - γ = 2r_1 + 2 - r_1 - 2 = r_1 ✓). β and γ are not roots of G if r_1 + 1 and r_1 + 2 are not among {-r_1, ±r_2, ..., ±r_{1010}}. For generic r_i, this holds.

So the construction works for generic choices. The answer is 3029.

But wait, I should also verify that P and Q are distinct. P = 2G(x - β) and Q = G(x - γ). P = Q iff 2(x - β) = (x - γ) iff x = 2β - γ = r_1 for all x, which is impossible. So P ≠ Q. ✓.

Also, P and Q have degree 2020. P = 2G(x - β), G has degree 2019, so P has degree 2020. ✓. Leading coefficient of P is 2 (leading coeff of G is 1, times 2 times x). Leading coefficient of Q is 1. Both non-zero. ✓.

And all coefficients of P and Q are non-zero for generic r_i (as argued above, the conditions fail only on a measure-zero set).

So the maximum is 3029.

Wait, I want to make sure I haven't made an error in the upper bound. Let me re-derive it.

Upper bound:
- D = P - Q has exactly 2021 - s non-zero coefficients (among positions 0, ..., 2020).
- D has at least r non-zero real roots (the common roots, which are non-zero since P(0) = a_0 ≠ 0).
- By Descartes' rule of signs, the number of positive real roots of D (counting multiplicity) ≤ (number of sign changes in D's coefficients) ≤ (number of non-zero terms - 1) = 2020 - s.
- Similarly, number of negative real roots ≤ 2020 - s.
- Total non-zero real roots ≤ 2(2020 - s).
- So r ≤ 2(2020 - s).

Also, r ≤ 2020 (since P has degree 2020).

If r = 2020: P = cQ (same roots with same multiplicities). Since all coefficients of Q are non-zero, a_i = c·b_i. Common coefficient: a_i = b_i iff c = 1 (since b_i ≠ 0). If c = 1, P = Q (excluded). If c ≠ 1, s = 0. So r + s = 2020.

If r ≤ 2019: r + s ≤ min(2(2020 - s) + s, 2019 + s) = min(4040 - s, 2019 + s).
- If s ≤ 1010: 4040 - s ≥ 3030 and 2019 + s ≤ 3029. So r + s ≤ 2019 + s ≤ 3029.
- If s ≥ 1011: 4040 - s ≤ 3029 and 2019 + s ≥ 3030. So r + s ≤ 4040 - s ≤ 3029.
- Maximum is 3029, achieved at s = 1010 (r + s ≤ 3029) or s = 1011 (r + s ≤ 3029).

Combining: max r + s = max(2020, 3029) = 3029.

And we showed 3029 is achievable. So the answer is 3029.

Hmm wait, let me double-check the case r = 2020 more carefully. If r = 2020, P and Q have the same 2020 roots with the same multiplicities. Since both have degree 2020, P = c·Q for some constant c ≠ 0. If c = 1, P = Q (excluded). If c ≠ 1, then a_i = c·b_i for all i, and a_i = b_i iff c·b_i = b_i iff (c-1)b_i = 0 iff c = 1 (since b_i ≠ 0). So s = 0, r + s = 2020 < 3029. ✓.

So the answer is $\boxed{3029}$.

Let me also verify the achievability construction once more. We need:
- D(x) = ∏_{i=1}^{1010} (x^2 - r_i^2) with r_1 = 1, r_i > 0 distinct.
- D has 1011 non-zero terms (at even positions), 1010 zero terms (at odd positions). So s = 1010.
- D has 2020 real roots: ±r_1, ..., ±r_{1010} = ±1, ..., ±r_{1010}.
- G = D/(x - 1), degree 2019, 2019 real roots: -1, ±r_2, ..., ±r_{1010}.
- H = x - 1 (degree 1, 1 real root at 1).
- P_1 = 2(x - β), Q_1 = (x - γ), P_1 - Q_1 = x - (2β - γ) = x - 1, so 2β - γ = 1.
- Choose β = 2, γ = 3: 2·2 - 3 = 1. ✓. β = 2, γ = 3 not roots of G (for generic r_i, e.g., r_i = i).
  Wait, if r_i = i, then r_2 = 2, and 2 is a root of G. Bad. Let me choose r_i = i + 100 or something.
  
  Actually, let me choose r_i = i for i = 1, ..., 1010 but then β and γ must avoid the roots. G's roots are -1, ±2, ±3, ..., ±1010. So β = 1011, γ = 2021: 2·1011 - 2021 = 1. ✓. 1011 and 2021 are not in {-1, ±2, ..., ±1010}. ✓.

- P = 2G(x - 1011), Q = G(x - 2021).
- All coefficients non-zero: need h_k ≠ 0, h_{k-1} ≠ 1011 h_k, h_{k-1} ≠ 2021 h_k for all k. For generic r_i, this holds. For r_i = i specifically, we'd need to verify, but the point is that there exist choices of r_i for which this holds.

Actually, to be fully rigorous, I should argue that the set of (r_1, ..., r_{1010}) for which any condition fails is a proper algebraic variety (measure zero), so generic choices work. The conditions are:
- h_k ≠ 0: h_k is a polynomial in r_1^2, ..., r_{1010}^2, and it's not identically zero (since for specific choices it's non-zero). So the set where h_k = 0 is a proper variety.
- h_{k-1} - 1011 h_k ≠ 0: similarly a polynomial condition, not identically zero.
- h_{k-1} - 2021 h_k ≠ 0: similarly.

Since there are finitely many conditions, each failing on a proper variety, the union is still a proper variety, and generic choices satisfy all conditions. ✓.

So the maximum is 3029.

Actually, I realize I should double-check one thing: I claimed D has exactly 1011 non-zero terms. D = ∏_{i=1}^{1010} (x^2 - r_i^2). This is a polynomial in x^2, say D = f(x^2) where f(y) = ∏(y - r_i^2). f has degree 1010 and all roots r_i^2 are positive and distinct. The coefficients of f are the elementary symmetric polynomials of r_1^2, ..., r_{1010}^2 (up to sign), which are all non-zero (since all r_i^2 > 0). So f has 1011 non-zero terms, and D = f(x^2) has 1011 non-zero terms at positions 0, 2, 4, ..., 2020. ✓.

Great, so the answer is 3029.

Let me also sanity-check with the small cases:
- n = 2 (even): 3·2/2 - 1 = 2. ✓ (verified).
- n = 4 (even): 3·4/2 - 1 = 5. ✓ (verified).
- n = 2020 (even): 3·2020/2 - 1 = 3030 - 1 = 3029. ✓.

The answer is $\boxed{3029}$.

Now let me write up the proof properly.
