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
  <problem_id>polymath_00022</problem_id>
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

Call a convex quadrilateral angle-Pythagorean if the degree measures of its angles are integers \(w \leq x \leq y \leq z\) satisfying
\[ w^{2}+x^{2}+y^{2}=z^{2} \]

Determine the maximum possible value of \(x+y\) for an angle-Pythagorean quadrilateral.

## Standard Solution

Solution. Let \(n=180\). We have the constraints

\[ w+x+y+z=2n \quad \text{and} \quad w^{2}+x^{2}+y^{2}=z^{2} \]

Set \(p=n-x, q=n-y\) for ease so that we have \(w+z=p+q\) and hence also

\[ (n-p)^{2}+(n-q)^{2}=(p+q)(z-w) \]

Since \(z=p+q-w\) we have

\[ p+q-2w=\frac{(n-p)^{2}+(n-q)^{2}}{p+q} \]
and so solving for \(w\) gives
\[ w=n-\frac{n^{2}-pq}{p+q} \]

If we set \(r=\frac{n^{2}-pq}{p+q}\) then we want ordered pairs \((p, q)\) for which \(r\) is an integer and \(n-r=w<x=n-p\), i.e. \(r>p\). We now write \(p+q=S\). So we want to find the minimal \(S\) for which there exists a \(p\) such that

\[ \frac{n^{2}-p(S-p)}{S} \]
is an integer \(>p\). An AM-GM bound on \(n^{2}-p(S-p)\) yields that \(S \geq\lceil 2n(\sqrt{2}-1)\rceil=150\). We see that \(S=150\) gives solutions
\[ (p, q)=(90,60),(120,30) \]

but in both of these cases we find that \(w \leq 0\). For \(S=151\), we see that \(r\) being an integer is equivalent to \(151 \mid\left(n^{2}+p^{2}\right)\) which is impossible since \(151\) is a prime \(\equiv 3(\bmod 4)\). Similarly \(152\) can be eliminated since \(19 \mid 152\). Having \(S=153\) finally gives a solution, namely \((w, x, y, z)=(4, 84, 123, 149)\). So \(x+y\) is maximized at \(360-153=207\).

\(\boxed{207}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. A convex quadrilateral has angles summing to 360°. The angles are integers w ≤ x ≤ y ≤ z with w² + x² + y² = z², and w + x + y + z = 360.

So z = 360 - (w+x+y), and w² + x² + y² = (360 - (w+x+y))².

Let me set s = w + x + y. Then z = 360 - s, and w² + x² + y² = (360-s)².

We want to maximize x + y.

Let me think about constraints. All angles positive integers, w ≤ x ≤ y ≤ z. Also convex means all angles < 180. So z < 180, meaning 360 - s < 180, so s > 180. Also z ≥ y means 360 - s ≥ y.

We want to maximize x + y. Let's denote t = x + y. Then w = s - t, z = 360 - s.

Constraints:
- w ≤ x ≤ y ≤ z, all positive integers
- w = s - t ≥ 1, so s ≥ t + 1
- z = 360 - s ≥ 1, s ≤ 359
- z < 180 (convex), s > 180
- y ≤ z = 360 - s, so y ≤ 360 - s
- x ≤ y
- w ≤ x: s - t ≤ x, i.e., w ≤ x
- w² + x² + y² = z² = (360-s)²

We want max t = x + y.

Let me think. Since w ≤ x ≤ y, we have w² + x² + y² ≤ 3y², and = z² so z² ≤ 3y², z ≤ y√3. Also z ≥ y so y ≤ z ≤ y√3.

Also w² + x² + y² ≥ 3w² (no, w is smallest). Actually w²+x²+y² ≥ y² (just y²), and equals z², so z ≥ y. Good, consistent.

To maximize x+y, we want x and y large. y ≤ z = 360 - s. And x ≤ y. And w = s - t = s - x - y.

Let me try to make w small (like 1) to allow x, y large.

If w = 1: 1 + x² + y² = z², and 1 + x + y + z = 360, so x + y + z = 359, z = 359 - x - y.
1 + x² + y² = (359 - x - y)².

Let u = x + y. Then z = 359 - u. 1 + x² + y² = (359-u)². x² + y² = u² - 2xy. So 1 + u² - 2xy = (359-u)² = 359² - 718u + u². So 1 - 2xy = 359² - 718u. 2xy = 718u - 359² + 1 = 718u - 128881 + 1 = 718u - 128880.

xy = 359u - 64440.

Also x + y = u, xy = 359u - 64440. For x, y real: discriminant u² - 4(359u - 64440) ≥ 0, u² - 1436u + 257760 ≥ 0.

Discriminant of that: 1436² - 4·257760 = 2062096 - 1031040 = 1031056. √1031056 ≈ 1015.4. So u ≤ (1436 - 1015.4)/2 ≈ 210.3 or u ≥ (1436+1015.4)/2 ≈ 1225.7. Since u = x+y ≤ 358 (as z≥1), u ≤ 210 roughly.

Hmm, so with w=1, u = x+y is bounded around 210. That's not great.

Let me reconsider. Maybe w shouldn't be too small. Let me think more generally.

We have w² + x² + y² = z² and w + x + y + z = 360.

Let me parametrize: let a = w, b = x, c = y, d = z. a ≤ b ≤ c ≤ d, a+b+c+d = 360, a²+b²+c² = d².

d = 360 - (a+b+c). Let s = a+b+c. d = 360-s.

a²+b²+c² = (360-s)².

We want to maximize b + c.

Note a²+b²+c² = s² - 2(ab+ac+bc). So s² - 2(ab+ac+bc) = (360-s)² = 360² - 720s + s². So -2(ab+ac+bc) = 360² - 720s. ab+ac+bc = 360s - 360²/2 = 360s - 64800.

So ab + ac + bc = 360s - 64800. With a+b+c = s.

Let me denote b+c = t, a = s - t. Then ab + ac + bc = a(b+c) + bc = (s-t)t + bc = 360s - 64800. So bc = 360s - 64800 - (s-t)t = 360s - 64800 - st + t² = s(360 - t) + t² - 64800.

Hmm, let me just think of it as: given a, b, c, d integers with the constraints, maximize b+c.

Alternative: think of Pythagorean quadruples. a² + b² + c² = d². These are related to Pythagorean quadruples. The general parametrization: a = m²+n²-p²-q², etc. But with the sum constraint it's tricky.

Let me think about it differently. We want b + c large. b ≤ c ≤ d. d = 360 - s where s = a + b + c. 

Since c ≤ d: c ≤ 360 - s = 360 - a - b - c, so 2c ≤ 360 - a - b, c ≤ (360 - a - b)/2.

Also b ≤ c.

To maximize b + c, roughly we want b and c close to d. If b = c = d, then a² + 2d² = d², a² = -d², impossible. So can't have all equal.

Let me think: a² + b² + c² = d², with a ≤ b ≤ c ≤ d. The "most balanced" case. If a = b = c, then 3a² = d², d = a√3, not integer generally.

Let me try to think about what maximizes b+c. We have b + c = t, and d = 360 - a - t. Constraint c ≤ d: c ≤ 360 - a - t. Since b ≤ c, c ≥ t/2. So t/2 ≤ c ≤ 360 - a - t, giving t ≤ 360 - a - t, 2t ≤ 360 - a, t ≤ (360 - a)/2.

Also a² + b² + c² = d² = (360 - a - t)².

b² + c² = t² - 2bc. So a² + t² - 2bc = (360 - a - t)². 

Let me expand (360 - a - t)² = (360 - (a+t))². Let u = a + t = s. Then = (360 - s)² = 360² - 720s + s² = 360² - 720(a+t) + (a+t)².

a² + t² - 2bc = 360² - 720(a+t) + a² + 2at + t².
-2bc = 360² - 720(a+t) + 2at.
bc = -360²/2 + 360(a+t) - at = -64800 + 360a + 360t - at = -64800 + 360a + t(360 - a).

So bc = 360a + t(360 - a) - 64800.

Given a and t, bc is determined. For b, c integers with b+c = t, bc = P, we need b, c roots of X² - tX + P = 0, discriminant Δ = t² - 4P ≥ 0 and perfect square.

Δ = t² - 4(360a + t(360-a) - 64800) = t² - 1440a - 4t(360-a) + 259200 = t² - 1440a - 1440t + 4at + 259200.

= t² + 4at - 1440t - 1440a + 259200 = t² + (4a - 1440)t - 1440a + 259200.

Hmm. Let me also recall constraints: a ≥ 1, b ≥ a, c ≥ b, d ≥ c, d < 180 (convex, all angles < 180). Actually for convex quadrilateral, each angle < 180. So d < 180, i.e., 360 - s < 180, s > 180, i.e., a + t > 180.

Also a ≤ b ≤ c. b ≥ a means the smaller root ≥ a... actually b is the smaller of the two roots (b ≤ c). b = (t - √Δ)/2 ≥ a. c = (t + √Δ)/2.

And c ≤ d = 360 - a - t.

Let me try to search computationally in my head... this is hard. Let me think about the structure.

We want max t = b + c. Upper bound: t ≤ (360 - a)/2 from c ≤ d. To maximize, minimize a. a = 1 gives t ≤ 359/2 = 179.5, so t ≤ 179. But wait, also need s > 180, a + t > 180, with a = 1, t > 179, so t ≥ 180. Contradiction with t ≤ 179! So a = 1 doesn't work for the convex constraint... wait let me recheck.

c ≤ d: c ≤ 360 - a - t. c ≥ t/2 (since c ≥ b and b + c = t, c ≥ t/2). So t/2 ≤ 360 - a - t, 3t/2 ≤ 360 - a, t ≤ (360 - a)·2/3.

Oh wait, I made an error. c ≥ t/2, and c ≤ 360 - a - t. So t/2 ≤ 360 - a - t, giving 3t/2 ≤ 360 - a, t ≤ 2(360-a)/3.

For a = 1: t ≤ 2·359/3 = 239.33, t ≤ 239. And a + t > 180: t > 179, t ≥ 180. So 180 ≤ t ≤ 239. OK so earlier I had the wrong bound. Let me redo.

So with a = 1, t can be up to 239. Let's see if we can achieve large t.

With a = 1: bc = 360·1 + t(360 - 1) - 64800 = 360 + 359t - 64800 = 359t - 64440.

Δ = t² - 4(359t - 64440) = t² - 1436t + 257760.

For Δ ≥ 0: t² - 1436t + 257760 ≥ 0. Roots: t = (1436 ± √(1436² - 4·257760))/2 = (1436 ± √(2062096 - 1031040))/2 = (1436 ± √1031056)/2.

√1031056: 1015² = 1030225, 1016² = 1032256. So √1031056 ≈ 1015.4. Roots: (1436 - 1015.4)/2 ≈ 210.3, (1436 + 1015.4)/2 ≈ 1225.7.

So Δ ≥ 0 when t ≤ 210 or t ≥ 1226. Since t ≤ 239, we need t ≤ 210. And t ≥ 180. So 180 ≤ t ≤ 210.

For t = 210: Δ = 210² - 1436·210 + 257760 = 44100 - 301560 + 257760 = 300. √300 ≈ 17.32, not integer.

t = 209: Δ = 43681 - 300124 + 257760 = 1317. √1317 ≈ 36.3, no.

t = 208: Δ = 43264 - 298688 + 257760 = 2336. √2336 ≈ 48.3, no.

t = 207: Δ = 42849 - 297252 + 257760 = 3357. √3357 ≈ 57.9, no.

t = 206: Δ = 42436 - 295816 + 257760 = 4380. √4380 ≈ 66.2, no.

t = 205: Δ = 42025 - 294380 + 257760 = 5405. √5405 ≈ 73.5, no.

t = 204: Δ = 41616 - 292944 + 257760 = 6432. √6432 ≈ 80.2, no.

t = 203: Δ = 41209 - 291508 + 257760 = 7461. √7461 ≈ 86.4, no.

t = 202: Δ = 40804 - 290072 + 257760 = 8492. √8492 ≈ 92.2, no.

t = 201: Δ = 40401 - 288636 + 257760 = 9525. √9525 ≈ 97.6, no.

t = 200: Δ = 40000 - 287200 + 257760 = 10560. √10560 ≈ 102.8, no.

t = 199: Δ = 39601 - 285764 + 257760 = 11597. √11597 ≈ 107.7, no.

t = 198: Δ = 39204 - 284328 + 257760 = 12636. √12636 ≈ 112.4, no.

t = 197: Δ = 38809 - 282892 + 257760 = 13677. √13677 ≈ 116.9, no.

t = 196: Δ = 38416 - 281456 + 257760 = 14720. √14720 ≈ 121.3, no.

t = 195: Δ = 38025 - 280020 + 257760 = 15765. √15765 ≈ 125.6, no.

t = 194: Δ = 37636 - 278584 + 257760 = 16812. √16812 ≈ 129.7, no.

t = 193: Δ = 37249 - 277148 + 257760 = 17861. √17861 ≈ 133.6, no.

t = 192: Δ = 36864 - 275712 + 257760 = 18912. √18912 ≈ 137.5, no.

t = 191: Δ = 36481 - 274276 + 257760 = 19965. √19965 ≈ 141.3, no.

t = 190: Δ = 36100 - 272840 + 257760 = 21020. √21020 ≈ 145.0, no.

t = 189: Δ = 35721 - 271404 + 257760 = 22077. √22077 ≈ 148.6, no.

t = 188: Δ = 35344 - 269968 + 257760 = 23136. √23136 ≈ 152.1, no.

t = 187: Δ = 34969 - 268532 + 257760 = 24197. √24197 ≈ 155.6, no.

t = 186: Δ = 34596 - 267096 + 257760 = 25260. √25260 ≈ 158.9, no.

t = 185: Δ = 34225 - 265660 + 257760 = 26325. √26325 ≈ 162.3, no.

t = 184: Δ = 33856 - 264224 + 257760 = 27392. √27392 ≈ 165.5, no.

t = 183: Δ = 33489 - 262788 + 257760 = 28461. √28461 ≈ 168.7, no.

t = 182: Δ = 33124 - 261352 + 257760 = 29532. √29532 ≈ 171.9, no.

t = 181: Δ = 32761 - 259916 + 257760 = 30605. √30605 ≈ 174.9, no.

t = 180: Δ = 32400 - 258480 + 257760 = 31680. √31680 ≈ 178.0, no.

Hmm, none of these are perfect squares for a=1. Let me check a few: 31680 = 31680. 178² = 31684. Close but no. 21020: 145² = 21025, no. 300: no. Let me check 18912: 137²=18769, 138²=19044, no. 

So a = 1 gives no solutions in range. Let me try a = 2.

a = 2: bc = 360·2 + t(360-2) - 64800 = 720 + 358t - 64800 = 358t - 64080.

Δ = t² - 4(358t - 64080) = t² - 1432t + 256320.

Roots: (1432 ± √(1432² - 4·256320))/2 = (1432 ± √(2050624 - 1025280))/2 = (1432 ± √1025344)/2. √1025344: 1012² = 1024144, 1013² = 1026169. ≈ 1012.6. Roots: (1432-1012.6)/2 ≈ 209.7, (1432+1012.6)/2 ≈ 1222.3.

So t ≤ 209 (roughly). Constraints: a + t > 180, t > 178, t ≥ 179. And t ≤ 2(360-2)/3 = 238.67, t ≤ 238. And t ≤ 209 from Δ. So 179 ≤ t ≤ 209.

Let me compute Δ for t = 209 down to 179:

t=209: Δ = 43681 - 1432·209 + 256320 = 43681 - 299288 + 256320 = 713. √713 ≈ 26.7, no.
t=208: 43264 - 297856 + 256320 = 1728. √1728 ≈ 41.6, no.
t=207: 42849 - 296424 + 256320 = 2745. √2745 ≈ 52.4, no.
t=206: 42436 - 294992 + 256320 = 3764. √3764 ≈ 61.3, no.
t=205: 42025 - 293560 + 256320 = 4785. √4785 ≈ 69.2, no.
t=204: 41616 - 292128 + 256320 = 5808. √5808 ≈ 76.2, no.
t=203: 41209 - 290696 + 256320 = 6833. √6833 ≈ 82.7, no.
t=202: 40804 - 289264 + 256320 = 7860. √7860 ≈ 88.7, no.
t=201: 40401 - 287832 + 256320 = 8889. √8889 ≈ 94.3, no.
t=200: 40000 - 286400 + 256320 = 9920. √9920 ≈ 99.6, no.
t=199: 39601 - 284968 + 256320 = 10953. √10953 ≈ 104.7, no.
t=198: 39204 - 283536 + 256320 = 11988. √11988 ≈ 109.5, no.
t=197: 38809 - 282104 + 256320 = 13025. √13025 ≈ 114.1, no.
t=196: 38416 - 280672 + 256320 = 14064. √14064 ≈ 118.6, no. 118²=13924, 119²=14161, no.
t=195: 38025 - 279240 + 256320 = 15105. √15105 ≈ 122.9, no.
t=194: 37636 - 277808 + 256320 = 16148. √16148 ≈ 127.1, no.
t=193: 37249 - 276376 + 256320 = 17193. √17193 ≈ 131.1, no.
t=192: 36864 - 274944 + 256320 = 18240. √18240 ≈ 135.1, no.
t=191: 36481 - 273512 + 256320 = 19289. √19289 ≈ 138.9, no.
t=190: 36100 - 272080 + 256320 = 20340. √20340 ≈ 142.6, no.
t=189: 35721 - 270648 + 256320 = 21393. √21393 ≈ 146.3, no.
t=188: 35344 - 269216 + 256320 = 22448. √22448 ≈ 149.8, no.
t=187: 34969 - 267784 + 256320 = 23505. √23505 ≈ 153.3, no.
t=186: 34596 - 266352 + 256320 = 24564. √24564 ≈ 156.7, no.
t=185: 34225 - 264920 + 256320 = 25625. √25625 ≈ 160.1, no. 160²=25600, 161²=25921, no.
t=184: 33856 - 263488 + 256320 = 26688. √26688 ≈ 163.4, no.
t=183: 33489 - 262056 + 256320 = 27753. √27753 ≈ 166.6, no.
t=182: 33124 - 260624 + 256320 = 28820. √28820 ≈ 169.8, no.
t=181: 32761 - 259192 + 256320 = 29889. √29889 ≈ 172.9, no.
t=180: 32400 - 257760 + 256320 = 30960. √30960 ≈ 175.9, no.
t=179: 32041 - 256328 + 256320 = 32033. √32033 ≈ 179.0, no. 179² = 32041. So 32033, no.

No solutions for a = 2 either. This is tedious. Let me think differently.

Maybe I should think about this more cleverly. Let me consider the general approach.

We have a² + b² + c² = d², a + b + c + d = 360, a ≤ b ≤ c ≤ d, all positive integers, d < 180 (convex).

From a + b + c + d = 360 and a² + b² + c² = d²:

Let me use the identity. (a+b+c)² = a²+b²+c² + 2(ab+ac+bc) = d² + 2(ab+ac+bc). Also a+b+c = 360 - d. So (360-d)² = d² + 2(ab+ac+bc). 360² - 720d + d² = d² + 2(ab+ac+bc). ab+ac+bc = (360² - 720d)/2 = 64800 - 360d.

So ab + ac + bc = 64800 - 360d. And a + b + c = 360 - d.

So a, b, c are three positive integers with sum S = 360 - d and pairwise sum P = 64800 - 360d, and a² + b² + c² = d².

Note: a²+b²+c² = S² - 2P = (360-d)² - 2(64800 - 360d) = 360² - 720d + d² - 129600 + 720d = 129600 + d² - 129600 = d². ✓ Good, consistent.

So the constraint is just: a, b, c positive integers, a ≤ b ≤ c ≤ d, a + b + c = 360 - d, ab + bc + ca = 64800 - 360d, and d < 180, d ≥ c.

We want to maximize b + c = (360 - d) - a. To maximize b + c, minimize a and... well b + c = S - a = (360 - d) - a. To maximize, we want small a and large S = 360 - d, i.e., small d. But d ≥ c and c is part of b+c... there's tension.

Actually b + c = 360 - d - a. To maximize, minimize d + a. Since a ≥ 1 and d > 180 (wait, d < 180 for convex). So d ranges. Let me think: d ≥ c ≥ b ≥ a ≥ 1. 

b + c = 360 - d - a. We want this large, so d + a small. a ≥ 1. d ≥ c = (360 - d - a) - b... hmm.

Let me think about bounds. Since c ≤ d and b ≤ c, we have b + c ≤ 2c ≤ 2d. Also b + c = 360 - d - a ≤ 360 - d - 1 = 359 - d. So b + c ≤ min(2d, 359 - d). To maximize min(2d, 359 - d): 2d = 359 - d gives 3d = 359, d ≈ 119.67. So max around d = 120, giving b + c ≤ 239.

But also need a² + b² + c² = d² with a + b + c = 360 - d. And the constraint that a, b, c are positive integers with a ≤ b ≤ c.

So the theoretical max of b + c is around 239 (when d ≈ 120, a = 1). But we saw a = 1, d = 360 - 1 - t, t = b + c. If t = 239, d = 120. Let me check: a = 1, d = 120, b + c = 239, b² + c² = d² - 1 = 14400 - 1 = 14399. b + c = 239, b² + c² = 239² - 2bc = 57121 - 2bc = 14399, 2bc = 42722, bc = 21361. Discriminant: 239² - 4·21361 = 57121 - 85444 = -28323 < 0. No real solution. So t = 239 doesn't work.

The issue is that b² + c² = d² - a² must be achievable. b² + c² ≥ (b+c)²/2 = t²/2. So d² - a² ≥ t²/2. With t = 360 - d - a: d² - a² ≥ (360 - d - a)²/2. 

2(d² - a²) ≥ (360 - d - a)². Let me set a = 1: 2(d² - 1) ≥ (359 - d)². 2d² - 2 ≥ 359² - 718d + d² = 128881 - 718d + d². d² + 718d - 128883 ≥ 0. d = (-718 + √(718² + 4·128883))/2 = (-718 + √(515524 + 515532))/2 = (-718 + √1031056)/2 ≈ (-718 + 1015.4)/2 ≈ 148.7. So d ≥ 149 (for a = 1). Then t = 359 - d ≤ 210. Which matches what we found (t ≤ 210 for a = 1).

So for a = 1, max t = 210, but no perfect square discriminant. Let me try larger a.

Actually, let me reconsider the approach. The constraint for real b, c: Δ = t² - 4bc ≥ 0 where bc = 360a + t(360-a) - 64800 (from earlier). And we need Δ to be a perfect square, and b = (t - √Δ)/2 ≥ a, c = (t + √Δ)/2 ≤ d = 360 - a - t.

Let me think about which (a, d) give valid solutions and maximize t = 360 - d - a.

Actually, let me just try to be systematic. We need d² - a² = b² + c² where b + c = 360 - d - a = t and b ≤ c ≤ d, b ≥ a.

d² - a² = (d-a)(d+a) = b² + c². And b + c = t = 360 - d - a. b² + c² = t² - 2bc.

So (d-a)(d+a) = t² - 2bc, bc = (t² - (d² - a²))/2 = (t² - d² + a²)/2.

With t = 360 - d - a: t² = (360 - d - a)² = 360² - 720(d+a) + (d+a)². t² - d² + a² = 360² - 720(d+a) + (d+a)² - d² + a² = 360² - 720(d+a) + d² + 2da + a² - d² + a² = 360² - 720(d+a) + 2da + 2a² = 360² - 720d - 720a + 2a(d + a) = 360² - 720d - 720a + 2ad + 2a² = 360² - 720d - 720a + 2a² + 2ad.

bc = (360² - 720d - 720a + 2a² + 2ad)/2 = 64800 - 360d - 360a + a² + ad = 64800 - 360(d + a) + a(a + d) = 64800 - 360(d+a) + a(a+d).

Let s = d + a. bc = 64800 - 360s + a·s... wait a(a+d) = a·s. So bc = 64800 - 360s + as = 64800 - s(360 - a). And t = 360 - s. So bc = 64800 - (360 - t)(360 - a) = 64800 - 360² + 360a + 360t - at = 64800 - 129600 + 360a + 360t - at = -64800 + 360a + 360t - at = 360a + t(360 - a) - 64800. Same as before. OK.

This is getting complex. Let me try a computational approach mentally by trying various d values and seeing what works.

Let me reframe: given d, we need a + b + c = 360 - d, ab + bc + ca = 64800 - 360d, a ≤ b ≤ c ≤ d, a ≥ 1. Maximize b + c = 360 - d - a, so minimize a.

For fixed d, a + b + c = S = 360 - d, and ab + ac + bc = P = 64800 - 360d. Then b + c = S - a, bc = P - a(b+c) = P - a(S - a) = P - aS + a². For b, c real: (S-a)² - 4(P - aS + a²) ≥ 0, i.e., S² - 2aS + a² - 4P + 4aS - 4a² ≥ 0, S² + 2aS - 3a² - 4P ≥ 0.

Also b ≥ a: (S - a - √Δ)/2 ≥ a, S - a - √Δ ≥ 2a, √Δ ≤ S - 3a. And c ≤ d: (S - a + √Δ)/2 ≤ d, S - a + √Δ ≤ 2d, √Δ ≤ 2d - S + a = 2d - (360 - d) + a = 3d - 360 + a.

And c ≥ b automatically. c ≥ b means √Δ ≥ 0. Also c ≥ b ≥ a.

Let me just try to find solutions by trying d values around 120-150 and a = 1, 2, 3, ...

Actually, let me think about it as: we need d² - a² = b² + c² to be expressible as sum of two squares with b + c = 360 - d - a, b ≤ c ≤ d, b ≥ a.

d² - a² = (d-a)(d+a). For this to be b² + c² with b + c = t: b² + c² = t² - 2bc, and we need b² + c² = d² - a². So t² - 2bc = d² - a², bc = (t² - d² + a²)/2.

For b, c to be positive integers: t² - d² + a² must be even and ≥ 0, and discriminant t² - 4bc = t² - 2(t² - d² + a²) = 2d² - 2a² - t² = 2(d² - a²) - t² must be ≥ 0 and a perfect square.

So Δ = 2(d² - a²) - t² where t = 360 - d - a. Let me substitute: Δ = 2d² - 2a² - (360 - d - a)² = 2d² - 2a² - 360² + 720(d+a) - (d+a)² = 2d² - 2a² - 129600 + 720d + 720a - d² - 2da - a² = d² - 3a² - 2da + 720d + 720a - 129600.

Hmm. Let me just try specific values.

Let me try d = 130. S = 230, P = 64800 - 46800 = 18000. a + b + c = 230, ab+ac+bc = 18000. b + c = 230 - a, bc = 18000 - a(230 - a) = 18000 - 230a + a². Δ = (230-a)² - 4(18000 - 230a + a²) = 52900 - 460a + a² - 72000 + 920a - 4a² = -19100 + 460a - 3a².

For Δ ≥ 0: 3a² - 460a + 19100 ≤ 0. Discriminant: 460² - 12·19100 = 211600 - 229200 = -17600 < 0. So 3a² - 460a + 19100 > 0 always (since leading coeff positive and no real roots). So Δ < 0 always for d = 130. No solution.

Let me try d = 140. S = 220, P = 64800 - 50400 = 14400. Δ = (220-a)² - 4(14400 - 220a + a²) = 48400 - 440a + a² - 57600 + 880a - 4a² = -9200 + 440a - 3a². ≥ 0: 3a² - 440a + 9200 ≤ 0. Disc: 440² - 12·9200 = 193600 - 110400 = 83200. √83200 ≈ 288.4. a = (440 ± 288.4)/6. a ∈ [25.27, 121.4]. So a from 26 to 121.

But also a ≤ b ≤ c ≤ d = 140, and a + b + c = 220, so a ≤ 220/3 ≈ 73. And b ≥ a. So a from 26 to 73 roughly.

We want to minimize a to maximize b + c = 220 - a. So a = 26: Δ = -9200 + 440·26 - 3·676 = -9200 + 11440 - 2028 = 212. √212 ≈ 14.56, not integer.

a = 27: Δ = -9200 + 11880 - 2187 = 493. √493 ≈ 22.2, no.
a = 28: Δ = -9200 + 12320 - 2352 = 768. √768 ≈ 27.7, no.
a = 29: Δ = -9200 + 12760 - 2523 = 1037. √1037 ≈ 32.2, no.
a = 30: Δ = -9200 + 13200 - 2700 = 1300. √1300 ≈ 36.06, no.
a = 31: Δ = -9200 + 13640 - 2883 = 1557. √1557 ≈ 39.5, no.
a = 32: Δ = -9200 + 14080 - 3072 = 1808. √1808 ≈ 42.5, no.
a = 33: Δ = -9200 + 14520 - 3267 = 2053. √2053 ≈ 45.3, no.
a = 34: Δ = -9200 + 14960 - 3468 = 2292. √2292 ≈ 47.9, no.
a = 35: Δ = -9200 + 15400 - 3675 = 2525. √2525 ≈ 50.2, no.
a = 36: Δ = -9200 + 15840 - 3888 = 2752. √2752 ≈ 52.5, no.
a = 37: Δ = -9200 + 16280 - 4107 = 2973. √2973 ≈ 54.5, no.
a = 38: Δ = -9200 + 16720 - 4332 = 3188. √3188 ≈ 56.5, no.
a = 39: Δ = -9200 + 17160 - 4563 = 3397. √3397 ≈ 58.3, no.
a = 40: Δ = -9200 + 17600 - 4800 = 3600. √3600 = 60! Yes!

a = 40, d = 140: b + c = 220 - 40 = 180. bc = 14400 - 220·40 + 1600 = 14400 - 8800 + 1600 = 7200. b, c roots of X² - 180X + 7200 = 0. Δ = 32400 - 28800 = 3600, √Δ = 60. b = (180-60)/2 = 60, c = (180+60)/2 = 120. Check: a=40, b=60, c=120, d=140. 40 ≤ 60 ≤ 120 ≤ 140 ✓. Sum = 360 ✓. 40² + 60² + 120² = 1600 + 3600 + 14400 = 19600 = 140² ✓. All < 180 ✓. b + c = 180.

So we have a solution with b + c = 180. Can we do better?

Let me continue with d = 140 and smaller a... but a = 26 to 39 gave no perfect squares. Let me check a = 40 is the first. So for d = 140, best is b + c = 180.

Let me try d = 135. S = 225, P = 64800 - 48600 = 16200. Δ = (225-a)² - 4(16200 - 225a + a²) = 50625 - 450a + a² - 64800 + 900a - 4a² = -14175 + 450a - 3a². ≥ 0: 3a² - 450a + 14175 ≤ 0. Disc: 450² - 12·14175 = 202500 - 170100 = 32400, √32400 = 180. a = (450 ± 180)/6 = 45 or 105. So a ∈ [45, 105]. But a ≤ 225/3 = 75. So a from 45 to 75.

Minimize a: a = 45. Δ = -14175 + 450·45 - 3·2025 = -14175 + 20250 - 6075 = 0. √Δ = 0. b = c = (225 - 45)/2 = 90. Check: a=45, b=90, c=90, d=135. 45 ≤ 90 ≤ 90 ≤ 135 ✓. Sum = 360 ✓. 45² + 90² + 90² = 2025 + 8100 + 8100 = 18225 = 135² ✓. b + c = 180. Same.

a = 46: Δ = -14175 + 20700 - 6348 = 177. √177 ≈ 13.3, no.
a = 47: Δ = -14175 + 21150 - 6627 = 348. √348 ≈ 18.7, no.
a = 48: Δ = -14175 + 21600 - 6912 = 513. √513 ≈ 22.6, no.
a = 49: Δ = -14175 + 22050 - 7203 = 672. √672 ≈ 25.9, no.
a = 50: Δ = -14175 + 22500 - 7500 = 825. √825 ≈ 28.7, no.
a = 51: Δ = -14175 + 22950 - 7803 = 972. √972 ≈ 31.2, no.
a = 52: Δ = -14175 + 23400 - 8112 = 1113. √1113 ≈ 33.4, no.
a = 53: Δ = -14175 + 23850 - 8427 = 1248. √1248 ≈ 35.3, no.
a = 54: Δ = -14175 + 24300 - 8748 = 1377. √1377 ≈ 37.1, no.
a = 55: Δ = -14175 + 24750 - 9075 = 1500. √1500 ≈ 38.7, no.
a = 56: Δ = -14175 + 25200 - 9408 = 1617. √1617 ≈ 40.2, no.
a = 57: Δ = -14175 + 25650 - 9747 = 1728. √1728 ≈ 41.6, no.
a = 58: Δ = -14175 + 26100 - 10092 = 1833. √1833 ≈ 42.8, no.
a = 59: Δ = -14175 + 26550 - 10443 = 1932. √1932 ≈ 43.9, no.
a = 60: Δ = -14175 + 27000 - 10800 = 2025. √2025 = 45! Yes!

a = 60, d = 135: b + c = 165. bc = 16200 - 225·60 + 3600 = 16200 - 13500 + 3600 = 6300. b = (165 - 45)/2 = 60, c = (165 + 45)/2 = 105. Check: 60, 60, 105, 135. 60 ≤ 60 ≤ 105 ≤ 135 ✓. Sum = 360 ✓. 60² + 60² + 105² = 3600 + 3600 + 11025 = 18225 = 135² ✓. b + c = 165 < 180.

So d = 135 gives max b + c = 180 (at a = 45). Let me try other d values to see if we can beat 180.

Let me try d = 145. S = 215, P = 64800 - 52200 = 12600. Δ = (215-a)² - 4(12600 - 215a + a²) = 46225 - 430a + a² - 50400 + 860a - 4a² = -4175 + 430a - 3a². ≥ 0: 3a² - 430a + 4175 ≤ 0. Disc: 430² - 12·4175 = 184900 - 50100 = 134800. √134800 ≈ 367.2. a = (430 ± 367.2)/6. a ∈ [10.47, 132.9]. a from 11 to 75 (since a ≤ 215/3 ≈ 71).

a = 11: Δ = -4175 + 4730 - 363 = 192. √192 ≈ 13.9, no.
a = 12: Δ = -4175 + 5160 - 432 = 553. √553 ≈ 23.5, no.
a = 13: Δ = -4175 + 5590 - 507 = 908. √908 ≈ 30.1, no.
a = 14: Δ = -4175 + 6020 - 588 = 1257. √1257 ≈ 35.5, no.
a = 15: Δ = -4175 + 6450 - 675 = 1600. √1600 = 40! Yes!

a = 15, d = 145: b + c = 200. bc = 12600 - 215·15 + 225 = 12600 - 3225 + 225 = 9600. b = (200 - 40)/2 = 80, c = (200 + 40)/2 = 120. Check: 15, 80, 120, 145. 15 ≤ 80 ≤ 120 ≤ 145 ✓. Sum = 360 ✓. 15² + 80² + 120² = 225 + 6400 + 14400 = 21025 = 145² ✓. b + c = 200!

That's better than 180. b + c = 200.

Let me check if c ≤ d: 120 ≤ 145 ✓. And all < 180 ✓.

Can we do even better? Let me try d = 145 with smaller a.

a = 11 to 14 didn't work. a = 15 works with b + c = 200. Let me check if there's a smaller a that works... a = 11, 12, 13, 14 all failed. So for d = 145, best is b + c = 200.

Let me try d = 150. S = 210, P = 64800 - 54000 = 10800. Δ = (210-a)² - 4(10800 - 210a + a²) = 44100 - 420a + a² - 43200 + 840a - 4a² = 900 + 420a - 3a². ≥ 0: 3a² - 420a - 900 ≤ 0. Disc: 420² + 12·900 = 176400 + 10800 = 187200. √187200 ≈ 432.7. a = (420 ± 432.7)/6. Positive root: (420 - 432.7)/6 < 0, so a ≥ 0 always satisfies (for a in valid range). Actually 3a² - 420a - 900 ≤ 0: roots at a = (420 ± 432.7)/6, so a ∈ [-2.12, 142.12]. So for a from 1 to 70 (a ≤ 210/3 = 70), Δ ≥ 0.

a = 1: Δ = 900 + 420 - 3 = 1317. √1317 ≈ 36.3, no.
a = 2: Δ = 900 + 840 - 12 = 1728. √1728 ≈ 41.6, no.
a = 3: Δ = 900 + 1260 - 27 = 2133. √2133 ≈ 46.2, no.
a = 4: Δ = 900 + 1680 - 48 = 2532. √2532 ≈ 50.3, no.
a = 5: Δ = 900 + 2100 - 75 = 2925. √2925 ≈ 54.1, no.
a = 6: Δ = 900 + 2520 - 108 = 3312. √3312 ≈ 57.5, no.
a = 7: Δ = 900 + 2940 - 147 = 3693. √3693 ≈ 60.8, no.
a = 8: Δ = 900 + 3360 - 192 = 4068. √4068 ≈ 63.8, no.
a = 9: Δ = 900 + 3780 - 243 = 4437. √4437 ≈ 66.6, no.
a = 10: Δ = 900 + 4200 - 300 = 4800. √4800 ≈ 69.3, no.
a = 11: Δ = 900 + 4620 - 363 = 5157. √5157 ≈ 71.8, no.
a = 12: Δ = 900 + 5040 - 432 = 5508. √5508 ≈ 74.2, no.
a = 13: Δ = 900 + 5460 - 507 = 5853. √5853 ≈ 76.5, no.
a = 14: Δ = 900 + 5880 - 588 = 6192. √6192 ≈ 78.7, no.
a = 15: Δ = 900 + 6300 - 675 = 6525. √6525 ≈ 80.8, no.
a = 16: Δ = 900 + 6720 - 768 = 6852. √6852 ≈ 82.8, no.
a = 17: Δ = 900 + 7140 - 867 = 7173. √7173 ≈ 84.7, no.
a = 18: Δ = 900 + 7560 - 972 = 7488. √7488 ≈ 86.5, no.
a = 19: Δ = 900 + 7980 - 1083 = 7797. √7797 ≈ 88.3, no.
a = 20: Δ = 900 + 8400 - 1200 = 8100. √8100 = 90! Yes!

a = 20, d = 150: b + c = 190. bc = 10800 - 210·20 + 400 = 10800 - 4200 + 400 = 7000. b = (190 - 90)/2 = 50, c = (190 + 90)/2 = 140. Check: 20, 50, 140, 150. 20 ≤ 50 ≤ 140 ≤ 150 ✓. Sum = 360 ✓. 20² + 50² + 140² = 400 + 2500 + 19600 = 22500 = 150² ✓. b + c = 190 < 200.

So d = 150 gives 190, less than 200.

Let me try d = 144. S = 216, P = 64800 - 51840 = 12960. Δ = (216-a)² - 4(12960 - 216a + a²) = 46656 - 432a + a² - 51840 + 864a - 4a² = -5184 + 432a - 3a². ≥ 0: 3a² - 432a + 5184 ≤ 0. Disc: 432² - 12·5184 = 186624 - 62208 = 124416. √124416 = 352.7... let me compute: 352² = 123904, 353² = 124609. So ≈ 352.7. a = (432 ± 352.7)/6. a ∈ [13.2, 130.8]. a from 14 to 72.

a = 14: Δ = -5184 + 6048 - 588 = 276. √276 ≈ 16.6, no.
a = 15: Δ = -5184 + 6480 - 675 = 621. √621 ≈ 24.9, no.
a = 16: Δ = -5184 + 6912 - 768 = 960. √960 ≈ 31.0, no.
a = 17: Δ = -5184 + 7344 - 867 = 1293. √1293 ≈ 35.96, no.
a = 18: Δ = -5184 + 7776 - 972 = 1620. √1620 ≈ 40.2, no.
a = 19: Δ = -5184 + 8208 - 1083 = 1941. √1941 ≈ 44.1, no.
a = 20: Δ = -5184 + 8640 - 1200 = 2256. √2256 ≈ 47.5, no.
a = 21: Δ = -5184 + 9072 - 1323 = 2565. √2565 ≈ 50.6, no.
a = 22: Δ = -5184 + 9504 - 1452 = 2868. √2868 ≈ 53.6, no.
a = 23: Δ = -5184 + 9936 - 1587 = 3165. √3165 ≈ 56.3, no.
a = 24: Δ = -5184 + 10368 - 1728 = 3456. √3456 ≈ 58.8, no.
a = 25: Δ = -5184 + 10800 - 1875 = 3741. √3741 ≈ 61.2, no.
a = 26: Δ = -5184 + 11232 - 2028 = 4020. √4020 ≈ 63.4, no.
a = 27: Δ = -5184 + 11664 - 2187 = 4293. √4293 ≈ 65.5, no.
a = 28: Δ = -5184 + 12096 - 2352 = 4560. √4560 ≈ 67.5, no.
a = 29: Δ = -5184 + 12528 - 2523 = 4821. √4821 ≈ 69.4, no.
a = 30: Δ = -5184 + 12960 - 2700 = 5076. √5076 ≈ 71.2, no.
a = 31: Δ = -5184 + 13392 - 2883 = 5325. √5325 ≈ 73.0, no.
a = 32: Δ = -5184 + 13824 - 3072 = 5568. √5568 ≈ 74.6, no.
a = 33: Δ = -5184 + 14256 - 3267 = 5805. √5805 ≈ 76.2, no.
a = 34: Δ = -5184 + 14688 - 3468 = 6036. √6036 ≈ 77.7, no.
a = 35: Δ = -5184 + 15120 - 3675 = 6261. √6261 ≈ 79.1, no.
a = 36: Δ = -5184 + 15552 - 3888 = 6480. √6480 ≈ 80.5, no.
a = 37: Δ = -5184 + 15984 - 4107 = 6693. √6693 ≈ 81.8, no.
a = 38: Δ = -5184 + 16416 - 4332 = 6900. √6900 ≈ 83.1, no.
a = 39: Δ = -5184 + 16848 - 4563 = 7101. √7101 ≈ 84.3, no.
a = 40: Δ = -5184 + 17280 - 4800 = 7296. √7296 ≈ 85.4, no.
a = 41: Δ = -5184 + 17712 - 5043 = 7485. √7485 ≈ 86.5, no.
a = 42: Δ = -5184 + 18144 - 5292 = 7668. √7668 ≈ 87.6, no.
a = 43: Δ = -5184 + 18576 - 5547 = 7845. √7845 ≈ 88.6, no.
a = 44: Δ = -5184 + 19008 - 5808 = 8016. √8016 ≈ 89.5, no.
a = 45: Δ = -5184 + 19440 - 6075 = 8181. √8181 ≈ 90.4, no.
a = 46: Δ = -5184 + 19872 - 6348 = 8340. √8340 ≈ 91.3, no.
a = 47: Δ = -5184 + 20304 - 6627 = 8493. √8493 ≈ 92.2, no.
a = 48: Δ = -5184 + 20736 - 6912 = 8640. √8640 ≈ 92.95, no.
a = 49: Δ = -5184 + 21168 - 7203 = 8781. √8781 ≈ 93.7, no.
a = 50: Δ = -5184 + 21600 - 7500 = 8916. √8916 ≈ 94.4, no.

This is taking forever. Let me try d = 145 more carefully, and also try d = 146, 147, etc. to see if we can beat 200.

Actually, let me think about it more cleverly. We found b + c = 200 with (15, 80, 120, 145). Let me see if we can do better.

Let me try d = 146. S = 214, P = 64800 - 52560 = 12240. Δ = (214-a)² - 4(12240 - 214a + a²) = 45796 - 428a + a² - 48960 + 856a - 4a² = -3164 + 428a - 3a². ≥ 0: 3a² - 428a + 3164 ≤ 0. Disc: 428² - 12·3164 = 183184 - 37968 = 145216. √145216: 381² = 145161, 382² = 145924. ≈ 381.07. a = (428 ± 381.07)/6. a ∈ [7.82, 134.8]. a from 8 to 71.

a = 8: Δ = -3164 + 3424 - 192 = 68. √68 ≈ 8.2, no.
a = 9: Δ = -3164 + 3852 - 243 = 445. √445 ≈ 21.1, no.
a = 10: Δ = -3164 + 4280 - 300 = 816. √816 ≈ 28.6, no.
a = 11: Δ = -3164 + 4708 - 363 = 1181. √1181 ≈ 34.4, no.
a = 12: Δ = -3164 + 5136 - 432 = 1540. √1540 ≈ 39.2, no.
a = 13: Δ = -3164 + 5564 - 507 = 1893. √1893 ≈ 43.5, no.
a = 14: Δ = -3164 + 5992 - 588 = 2240. √2240 ≈ 47.3, no.
a = 15: Δ = -3164 + 6420 - 675 = 2581. √2581 ≈ 50.8, no.
a = 16: Δ = -3164 + 6848 - 768 = 2916. √2916 = 54! Yes!

a = 16, d = 146: b + c = 198. bc = 12240 - 214·16 + 256 = 12240 - 3424 + 256 = 9072. b = (198 - 54)/2 = 72, c = (198 + 54)/2 = 126. Check: 16, 72, 126, 146. 16 ≤ 72 ≤ 126 ≤ 146 ✓. Sum = 360 ✓. 16² + 72² + 126² = 256 + 5184 + 15876 = 21316 = 146² ✓. b + c = 198 < 200.

So d = 146 gives 198. Let me try d = 147.

d = 147. S = 213, P = 64800 - 52920 = 11880. Δ = (213-a)² - 4(11880 - 213a + a²) = 45369 - 426a + a² - 47520 + 852a - 4a² = -2151 + 426a - 3a². ≥ 0: 3a² - 426a + 2151 ≤ 0. Disc: 426² - 12·2151 = 181476 - 25812 = 155664. √155664: 394.5² ≈ 155640, 395² = 156025. ≈ 394.55. a = (426 ± 394.55)/6. a ∈ [5.24, 136.8]. a from 6 to 71.

a = 6: Δ = -2151 + 2556 - 108 = 297. √297 ≈ 17.2, no.
a = 7: Δ = -2151 + 2982 - 147 = 684. √684 ≈ 26.2, no.
a = 8: Δ = -2151 + 3408 - 192 = 1065. √1065 ≈ 32.6, no.
a = 9: Δ = -2151 + 3834 - 243 = 1440. √1440 ≈ 37.9, no.
a = 10: Δ = -2151 + 4260 - 300 = 1809. √1809 ≈ 42.5, no.
a = 11: Δ = -2151 + 4686 - 363 = 2172. √2172 ≈ 46.6, no.
a = 12: Δ = -2151 + 5112 - 432 = 2529. √2529 ≈ 50.3, no.
a = 13: Δ = -2151 + 5538 - 507 = 2880. √2880 ≈ 53.7, no.
a = 14: Δ = -2151 + 5964 - 588 = 3225. √3225 ≈ 56.8, no.
a = 15: Δ = -2151 + 6390 - 675 = 3564. √3564 ≈ 59.7, no.
a = 16: Δ = -2151 + 6816 - 768 = 3897. √3897 ≈ 62.4, no.
a = 17: Δ = -2151 + 7242 - 867 = 4224. √4224 ≈ 65.0, no. 65² = 4225. So close! 4224, no.
a = 18: Δ = -2151 + 7668 - 972 = 4545. √4545 ≈ 67.4, no.
a = 19: Δ = -2151 + 8094 - 1083 = 4860. √4860 ≈ 69.7, no.
a = 20: Δ = -2151 + 8520 - 1200 = 5169. √5169 ≈ 71.9, no.
a = 21: Δ = -2151 + 8946 - 1323 = 5472. √5472 ≈ 74.0, no.
a = 22: Δ = -2151 + 9372 - 1452 = 5769. √5769 ≈ 75.9, no.
a = 23: Δ = -2151 + 9798 - 1587 = 6060. √6060 ≈ 77.8, no.
a = 24: Δ = -2151 + 10224 - 1728 = 6345. √6345 ≈ 79.7, no.
a = 25: Δ = -2151 + 10650 - 1875 = 6624. √6624 ≈ 81.4, no.
a = 26: Δ = -2151 + 11076 - 2028 = 6897. √6897 ≈ 83.0, no.
a = 27: Δ = -2151 + 11502 - 2187 = 7164. √7164 ≈ 84.6, no.
a = 28: Δ = -2151 + 11928 - 2352 = 7425. √7425 ≈ 86.2, no.
a = 29: Δ = -2151 + 12354 - 2523 = 7680. √7680 ≈ 87.6, no.
a = 30: Δ = -2151 + 12780 - 2700 = 7929. √7929 ≈ 89.0, no. 89² = 7921, 90² = 8100, no.
a = 31: Δ = -2151 + 13206 - 2883 = 8172. √8172 ≈ 90.4, no.
a = 32: Δ = -2151 + 13632 - 3072 = 8409. √8409 ≈ 91.7, no.
a = 33: Δ = -2151 + 14058 - 3267 = 8640. √8640 ≈ 92.95, no.
a = 34: Δ = -2151 + 14484 - 3468 = 8865. √8865 ≈ 94.2, no.
a = 35: Δ = -2151 + 14910 - 3675 = 9084. √9084 ≈ 95.3, no.
a = 36: Δ = -2151 + 15336 - 3888 = 9297. √9297 ≈ 96.4, no.
a = 37: Δ = -2151 + 15762 - 4107 = 9504. √9504 ≈ 97.5, no.
a = 38: Δ = -2151 + 16188 - 4332 = 9705. √9705 ≈ 98.5, no.
a = 39: Δ = -2151 + 16614 - 4563 = 9900. √9900 ≈ 99.5, no.
a = 40: Δ = -2151 + 17040 - 4800 = 10089. √10089 ≈ 100.4, no. 100² = 10000, 101² = 10201, no.
a = 41: Δ = -2151 + 17466 - 5043 = 10272. √10272 ≈ 101.4, no.
a = 42: Δ = -2151 + 17892 - 5292 = 10449. √10449 ≈ 102.2, no. 102² = 10404, 103² = 10609, no.
a = 43: Δ = -2151 + 18318 - 5547 = 10620. √10620 ≈ 103.0, no.
a = 44: Δ = -2151 + 18744 - 5808 = 10785. √10785 ≈ 103.9, no.
a = 45: Δ = -2151 + 19170 - 6075 = 10944. √10944 ≈ 104.6, no.
a = 46: Δ = -2151 + 19596 - 6348 = 11097. √11097 ≈ 105.3, no.
a = 47: Δ = -2151 + 20022 - 6627 = 11244. √11244 ≈ 106.0, no. 106² = 11236, no.
a = 48: Δ = -2151 + 20448 - 6912 = 11385. √11385 ≈ 106.7, no.
a = 49: Δ = -2151 + 20874 - 7203 = 11520. √11520 ≈ 107.3, no.
a = 50: Δ = -2151 + 21300 - 7500 = 11649. √11649 ≈ 107.9, no. 108² = 11664, no.

Hmm, d = 147 seems to have no solutions. Let me try d = 148.

d = 148. S = 212, P = 64800 - 53280 = 11520. Δ = (212-a)² - 4(11520 - 212a + a²) = 44944 - 424a + a² - 46080 + 848a - 4a² = -1136 + 424a - 3a². ≥ 0: 3a² - 424a + 1136 ≤ 0. Disc: 424² - 12·1136 = 179776 - 13632 = 166144. √166144: 407.6² ≈ 166138, 408² = 166464. ≈ 407.6. a = (424 ± 407.6)/6. a ∈ [2.73, 138.6]. a from 3 to 70.

a = 3: Δ = -1136 + 1272 - 27 = 109. √109 ≈ 10.4, no.
a = 4: Δ = -1136 + 1696 - 48 = 512. √512 ≈ 22.6, no.
a = 5: Δ = -1136 + 2120 - 75 = 909. √909 ≈ 30.1, no.
a = 6: Δ = -1136 + 2544 - 108 = 1300. √1300 ≈ 36.1, no.
a = 7: Δ = -1136 + 2968 - 147 = 1685. √1685 ≈ 41.0, no.
a = 8: Δ = -1136 + 3392 - 192 = 2064. √2064 ≈ 45.4, no.
a = 9: Δ = -1136 + 3816 - 243 = 2437. √2437 ≈ 49.4, no.
a = 10: Δ = -1136 + 4240 - 300 = 2804. √2804 ≈ 52.9, no.
a = 11: Δ = -1136 + 4664 - 363 = 3165. √3165 ≈ 56.3, no.
a = 12: Δ = -1136 + 5088 - 432 = 3520. √3520 ≈ 59.3, no.
a = 13: Δ = -1136 + 5512 - 507 = 3869. √3869 ≈ 62.2, no.
a = 14: Δ = -1136 + 5936 - 588 = 4212. √4212 ≈ 64.9, no.
a = 15: Δ = -1136 + 6360 - 675 = 4549. √4549 ≈ 67.4, no.
a = 16: Δ = -1136 + 6784 - 768 = 4880. √4880 ≈ 69.9, no.
a = 17: Δ = -1136 + 7208 - 867 = 5205. √5205 ≈ 72.1, no.
a = 18: Δ = -1136 + 7632 - 972 = 5524. √5524 ≈ 74.3, no.
a = 19: Δ = -1136 + 8056 - 1083 = 5837. √5837 ≈ 76.4, no.
a = 20: Δ = -1136 + 8480 - 1200 = 6144. √6144 ≈ 78.4, no.
a = 21: Δ = -1136 + 8904 - 1323 = 6445. √6445 ≈ 80.3, no.
a = 22: Δ = -1136 + 9328 - 1452 = 6740. √6740 ≈ 82.1, no.
a = 23: Δ = -1136 + 9752 - 1587 = 7029. √7029 ≈ 83.8, no.
a = 24: Δ = -1136 + 10176 - 1728 = 7312. √7312 ≈ 85.5, no.
a = 25: Δ = -1136 + 10600 - 1875 = 7589. √7589 ≈ 87.1, no.
a = 26: Δ = -1136 + 11024 - 2028 = 7860. √7860 ≈ 88.7, no.
a = 27: Δ = -1136 + 11448 - 2187 = 8125. √8125 ≈ 90.1, no.
a = 28: Δ = -1136 + 11872 - 2352 = 8384. √8384 ≈ 91.6, no.
a = 29: Δ = -1136 + 12296 - 2523 = 8637. √8637 ≈ 92.9, no.
a = 30: Δ = -1136 + 12720 - 2700 = 8884. √8884 ≈ 94.3, no.
a = 31: Δ = -1136 + 13144 - 2883 = 9125. √9125 ≈ 95.5, no.
a = 32: Δ = -1136 + 13568 - 3072 = 9360. √9360 ≈ 96.7, no.
a = 33: Δ = -1136 + 13992 - 3267 = 9589. √9589 ≈ 97.9, no.
a = 34: Δ = -1136 + 14416 - 3468 = 9812. √9812 ≈ 99.1, no.
a = 35: Δ = -1136 + 14840 - 3675 = 10029. √10029 ≈ 100.1, no. 100² = 10000, 101² = 10201, no.
a = 36: Δ = -1136 + 15264 - 3888 = 10240. √10240 ≈ 101.2, no.
a = 37: Δ = -1136 + 15688 - 4107 = 10445. √10445 ≈ 102.2, no.
a = 38: Δ = -1136 + 16112 - 4332 = 10644. √10644 ≈ 103.2, no.
a = 39: Δ = -1136 + 16536 - 4563 = 10837. √10837 ≈ 104.1, no.
a = 40: Δ = -1136 + 16960 - 4800 = 11024. √11024 ≈ 105.0, no. 105² = 11025. So close! 11024, no.
a = 41: Δ = -1136 + 17384 - 5043 = 11205. √11205 ≈ 105.9, no.
a = 42: Δ = -1136 + 17808 - 5292 = 11380. √11380 ≈ 106.7, no.
a = 43: Δ = -1136 + 18232 - 5547 = 11549. √11549 ≈ 107.5, no.
a = 44: Δ = -1136 + 18656 - 5808 = 11712. √11712 ≈ 108.2, no.
a = 45: Δ = -1136 + 19080 - 6075 = 11869. √11869 ≈ 108.9, no.
a = 46: Δ = -1136 + 19504 - 6348 = 12020. √12020 ≈ 109.6, no.
a = 47: Δ = -1136 + 19928 - 6627 = 12165. √12165 ≈ 110.3, no.
a = 48: Δ = -1136 + 20352 - 6912 = 12304. √12304 ≈ 110.9, no.
a = 49: Δ = -1136 + 20776 - 7203 = 12437. √12437 ≈ 111.5, no.
a = 50: Δ = -1136 + 21200 - 7500 = 12564. √12564 ≈ 112.1, no.

d = 148 no solutions so far. This is very tedious. Let me try a different approach.

Let me go back to d = 145 which gave b + c = 200, and try to see if any d gives more.

Let me try d = 143. S = 217, P = 64800 - 51480 = 13320. Δ = (217-a)² - 4(13320 - 217a + a²) = 47089 - 434a + a² - 53280 + 868a - 4a² = -6191 + 434a - 3a². ≥ 0: 3a² - 434a + 6191 ≤ 0. Disc: 434² - 12·6191 = 188356 - 74292 = 114064. √114064: 337.7² ≈ 114041, 338² = 114244. ≈ 337.77. a = (434 ± 337.77)/6. a ∈ [16.04, 128.6]. a from 17 to 72.

a = 17: Δ = -6191 + 7378 - 867 = 320. √320 ≈ 17.9, no.
a = 18: Δ = -6191 + 7812 - 972 = 649. √649 ≈ 25.5, no.
a = 19: Δ = -6191 + 8246 - 1083 = 972. √972 ≈ 31.2, no.
a = 20: Δ = -6191 + 8680 - 1200 = 1289. √1289 ≈ 35.9, no.
a = 21: Δ = -6191 + 9114 - 1323 = 1600. √1600 = 40! Yes!

a = 21, d = 143: b + c = 196. bc = 13320 - 217·21 + 441 = 13320 - 4557 + 441 = 9204. b = (196 - 40)/2 = 78, c = (196 + 40)/2 = 118. Check: 21, 78, 118, 143. 21 ≤ 78 ≤ 118 ≤ 143 ✓. Sum = 360 ✓. 21² + 78² + 118² = 441 + 6084 + 13924 = 20449 = 143² ✓. b + c = 196 < 200.

Let me try d = 145 with a < 15. We had a = 11, 12, 13, 14 fail. What about checking a = 15 gave 200. Let me also check higher a for d = 145 to see if there are other solutions (though they'd give smaller b+c).

Actually, let me focus: can we beat 200? Let me try d = 145, and also try d values like 141, 142, 144 that we haven't fully explored, and d = 149, 155, 160, etc.

Let me try d = 141. S = 219, P = 64800 - 50760 = 14040. Δ = (219-a)² - 4(14040 - 219a + a²) = 47961 - 438a + a² - 56160 + 876a - 4a² = -8199 + 438a - 3a². ≥ 0: 3a² - 438a + 8199 ≤ 0. Disc: 438² - 12·8199 = 191844 - 98388 = 93456. √93456: 305.7² ≈ 93453, 306² = 93636. ≈ 305.7. a = (438 ± 305.7)/6. a ∈ [22.05, 123.95]. a from 23 to 73.

a = 23: Δ = -8199 + 10074 - 1587 = 288. √288 ≈ 17.0, no.
a = 24: Δ = -8199 + 10512 - 1728 = 585. √585 ≈ 24.2, no.
a = 25: Δ = -8199 + 10950 - 1875 = 876. √876 ≈ 29.6, no.
a = 26: Δ = -8199 + 11388 - 2028 = 1161. √1161 ≈ 34.1, no.
a = 27: Δ = -8199 + 11826 - 2187 = 1440. √1440 ≈ 37.9, no.
a = 28: Δ = -8199 + 12264 - 2352 = 1713. √1713 ≈ 41.4, no.
a = 29: Δ = -8199 + 12702 - 2523 = 1980. √1980 ≈ 44.5, no.
a = 30: Δ = -8199 + 13140 - 2700 = 2241. √2241 ≈ 47.3, no.
a = 31: Δ = -8199 + 13578 - 2883 = 2496. √2496 ≈ 49.96, no. 50² = 2500, no.
a = 32: Δ = -8199 + 14016 - 3072 = 2745. √2745 ≈ 52.4, no.
a = 33: Δ = -8199 + 14454 - 3267 = 2988. √2988 ≈ 54.7, no.
a = 34: Δ = -8199 + 14892 - 3468 = 3225. √3225 ≈ 56.8, no.
a = 35: Δ = -8199 + 15330 - 3675 = 3456. √3456 ≈ 58.8, no.
a = 36: Δ = -8199 + 15768 - 3888 = 3681. √3681 ≈ 60.7, no.
a = 37: Δ = -8199 + 16206 - 4107 = 3900. √3900 ≈ 62.4, no.
a = 38: Δ = -8199 + 16644 - 4332 = 4113. √4113 ≈ 64.1, no.
a = 39: Δ = -8199 + 17082 - 4563 = 4320. √4320 ≈ 65.7, no.
a = 40: Δ = -8199 + 17520 - 4800 = 4521. √4521 ≈ 67.2, no.
a = 41: Δ = -8199 + 17958 - 5043 = 4716. √4716 ≈ 68.7, no.
a = 42: Δ = -8199 + 18396 - 5292 = 4905. √4905 ≈ 70.0, no.
a = 43: Δ = -8199 + 18834 - 5547 = 5088. √5088 ≈ 71.3, no.
a = 44: Δ = -8199 + 19272 - 5808 = 5265. √5265 ≈ 72.6, no.
a = 45: Δ = -8199 + 19710 - 6075 = 5436. √5436 ≈ 73.7, no.
a = 46: Δ = -8199 + 20148 - 6348 = 5601. √5601 ≈ 74.8, no.
a = 47: Δ = -8199 + 20586 - 6627 = 5760. √5760 ≈ 75.9, no.
a = 48: Δ = -8199 + 21024 - 6912 = 5913. √5913 ≈ 76.9, no.
a = 49: Δ = -8199 + 21462 - 7203 = 6060. √6060 ≈ 77.8, no.
a = 50: Δ = -8199 + 21900 - 7500 = 6201. √6201 ≈ 78.7, no.

d = 141 no solutions found. Let me try d = 142.

d = 142. S = 218, P = 64800 - 51120 = 13680. Δ = (218-a)² - 4(13680 - 218a + a²) = 47524 - 436a + a² - 54720 + 872a - 4a² = -7196 + 436a - 3a². ≥ 0: 3a² - 436a + 7196 ≤ 0. Disc: 436² - 12·7196 = 190096 - 86352 = 103744. √103744: 322.1² ≈ 103748, 322² = 103684. ≈ 322.09. a = (436 ± 322.09)/6. a ∈ [18.98, 126.35]. a from 19 to 72.

a = 19: Δ = -7196 + 8284 - 1083 = 5. √5 ≈ 2.24, no.
a = 20: Δ = -7196 + 8720 - 1200 = 324. √324 = 18! Yes!

a = 20, d = 142: b + c = 198. bc = 13680 - 218·20 + 400 = 13680 - 4360 + 400 = 9720. b = (198 - 18)/2 = 90, c = (198 + 18)/2 = 108. Check: 20, 90, 108, 142. 20 ≤ 90 ≤ 108 ≤ 142 ✓. Sum = 360 ✓. 20² + 90² + 108² = 400 + 8100 + 11664 = 20164 = 142² ✓. b + c = 198 < 200.

Let me try d = 144 more carefully. We checked a = 14 to 50, none worked. Let me try a = 51 to 72.

Actually, this is extremely tedious. Let me think about whether 200 can be beaten.

The key solution is (15, 80, 120, 145) with b + c = 200. Let me think about whether there's a solution with b + c > 200.

For b + c > 200, we need 360 - d - a > 200, so d + a < 160. With a ≥ 1 and d > 180... wait, d < 180 (convex). Actually d ≥ c ≥ b ≥ a, and d < 180. So d can be up to 179.

If d + a < 160 and a ≥ 1, then d < 159. And d ≥ c, c = (b+c) - b, with b + c > 200 and b ≤ c, so c > 100. And c ≤ d, so d > 100. So d ∈ (100, 159).

Also, we need a² + b² + c² = d² with b + c = t > 200, a = 360 - d - t, and the discriminant to be a perfect square.

Let me think about it from the Pythagorean quadruple angle. We need a² + b² + c² = d². This is a Pythagorean quadruple. The general primitive parametrization: a = 2(mn - pq), b = 2(mp + nq), c = m² + n² - p² - q², d = m² + n² + p² + q² (or similar). But with the sum constraint it's complex.

Let me try d = 155. S = 205, P = 64800 - 55800 = 9000. Δ = (205-a)² - 4(9000 - 205a + a²) = 42025 - 410a + a² - 36000 + 820a - 4a² = 6025 + 410a - 3a². ≥ 0: 3a² - 410a - 6025 ≤ 0. Disc: 410² + 12·6025 = 168100 + 72300 = 240400. √240400 ≈ 490.3. a = (410 ± 490.3)/6. a ∈ [-13.4, 150.05]. So a from 1 to 68 (a ≤ 205/3 ≈ 68).

a = 1: Δ = 6025 + 410 - 3 = 6432. √6432 ≈ 80.2, no.
a = 2: Δ = 6025 + 820 - 12 = 6833. √6833 ≈ 82.7, no.
a = 3: Δ = 6025 + 1230 - 27 = 7228. √7228 ≈ 85.0, no.
a = 4: Δ = 6025 + 1640 - 48 = 7617. √7617 ≈ 87.3, no.
a = 5: Δ = 6025 + 2050 - 75 = 8000. √8000 ≈ 89.4, no.
a = 6: Δ = 6025 + 2460 - 108 = 8377. √8377 ≈ 91.5, no.
a = 7: Δ = 6025 + 2870 - 147 = 8748. √8748 ≈ 93.5, no.
a = 8: Δ = 6025 + 3280 - 192 = 9113. √9113 ≈ 95.5, no.
a = 9: Δ = 6025 + 3690 - 243 = 9472. √9472 ≈ 97.3, no.
a = 10: Δ = 6025 + 4100 - 300 = 9825. √9825 ≈ 99.1, no.
a = 11: Δ = 6025 + 4510 - 363 = 10172. √10172 ≈ 100.9, no.
a = 12: Δ = 6025 + 4920 - 432 = 10513. √10513 ≈ 102.5, no.
a = 13: Δ = 6025 + 5330 - 507 = 10848. √10848 ≈ 104.2, no.
a = 14: Δ = 6025 + 5740 - 588 = 11177. √11177 ≈ 105.7, no.
a = 15: Δ = 6025 + 6150 - 675 = 11500. √11500 ≈ 107.2, no.
a = 16: Δ = 6025 + 6560 - 768 = 11817. √11817 ≈ 108.7, no.
a = 17: Δ = 6025 + 6970 - 867 = 12128. √12128 ≈ 110.1, no.
a = 18: Δ = 6025 + 7380 - 972 = 12433. √12433 ≈ 111.5, no.
a = 19: Δ = 6025 + 7790 - 1083 = 12732. √12732 ≈ 112.8, no.
a = 20: Δ = 6025 + 8200 - 1200 = 13025. √13025 ≈ 114.1, no.
a = 21: Δ = 6025 + 8610 - 1323 = 13312. √13312 ≈ 115.4, no.
a = 22: Δ = 6025 + 9020 - 1452 = 13593. √13593 ≈ 116.6, no.
a = 23: Δ = 6025 + 9430 - 1587 = 13868. √13868 ≈ 117.8, no.
a = 24: Δ = 6025 + 9840 - 1728 = 14137. √14137 ≈ 118.9, no.
a = 25: Δ = 6025 + 10250 - 1875 = 14400. √14400 = 120! Yes!

a = 25, d = 155: b + c = 180. bc = 9000 - 205·25 + 625 = 9000 - 5125 + 625 = 4500. b = (180 - 120)/2 = 30, c = (180 + 120)/2 = 150. Check: 25, 30, 150, 155. 25 ≤ 30 ≤ 150 ≤ 155 ✓. Sum = 360 ✓. 25² + 30² + 150² = 625 + 900 + 22500 = 24025 = 155² ✓. b + c = 180 < 200.

So d = 155 gives 180. The trend seems like d = 145 is special. Let me try d = 149.

d = 149. S = 211, P = 64800 - 53640 = 11160. Δ = (211-a)² - 4(11160 - 211a + a²) = 44521 - 422a + a² - 44640 + 844a - 4a² = -119 + 422a - 3a². ≥ 0: 3a² - 422a + 119 ≤ 0. Disc: 422² - 12·119 = 178084 - 1428 = 176656. √176656: 420.3² ≈ 176652, 421² = 177241. ≈ 420.3. a = (422 ± 420.3)/6. a ∈ [0.28, 140.4]. a from 1 to 70.

a = 1: Δ = -119 + 422 - 3 = 300. √300 ≈ 17.3, no.
a = 2: Δ = -119 + 844 - 12 = 713. √713 ≈ 26.7, no.
a = 3: Δ = -119 + 1266 - 27 = 1120. √1120 ≈ 33.5, no.
a = 4: Δ = -119 + 1688 - 48 = 1521. √1521 = 39! Yes!

a = 4, d = 149: b + c = 207. bc = 11160 - 211·4 + 16 = 11160 - 844 + 16 = 10332. b = (207 - 39)/2 = 84, c = (207 + 39)/2 = 123. Check: 4, 84, 123, 149. 4 ≤ 84 ≤ 123 ≤ 149 ✓. Sum = 360 ✓. 4² + 84² + 123² = 16 + 7056 + 15129 = 22201 = 149² ✓. b + c = 207!

That beats 200! b + c = 207.

Let me check: 149² = 22201. 16 + 7056 = 7072, + 15129 = 22201. ✓

So (4, 84, 123, 149) gives b + c = 207. Can we do better?

Let me try d = 149 with a = 1, 2, 3 (smaller a, larger b + c):
a = 1: Δ = 300, not perfect square.
a = 2: Δ = 713, no.
a = 3: Δ = 1120, no.
a = 4: Δ = 1521 = 39², works, b + c = 207.

So for d = 149, best is 207. Let me try d = 150 again more carefully - we found a = 20 giving b + c = 190. But let me check smaller a.

For d = 150, a = 1 to 19: we checked a = 1 to 19, none were perfect squares (a = 20 gave 8100 = 90²). So d = 150 best is 190.

Let me try d = 149 is good. Let me try nearby values. d = 148 we checked a = 3 to 50, none worked. Let me try d = 151.

d = 151. S = 209, P = 64800 - 54360 = 10440. Δ = (209-a)² - 4(10440 - 209a + a²) = 43681 - 418a + a² - 41760 + 836a - 4a² = 1921 + 418a - 3a². ≥ 0: 3a² - 418a - 1921 ≤ 0. Disc: 418² + 12·1921 = 174724 + 23052 = 197776. √197776: 444.7² ≈ 197758, 446² = 198916. ≈ 444.72. a = (418 ± 444.72)/6. a ∈ [-4.45, 143.8]. a from 1 to 69.

a = 1: Δ = 1921 + 418 - 3 = 2336. √2336 ≈ 48.3, no.
a = 2: Δ = 1921 + 836 - 12 = 2745. √2745 ≈ 52.4, no.
a = 3: Δ = 1921 + 1254 - 27 = 3148. √3148 ≈ 56.1, no.
a = 4: Δ = 1921 + 1672 - 48 = 3545. √3545 ≈ 59.5, no.
a = 5: Δ = 1921 + 2090 - 75 = 3936. √3936 ≈ 62.7, no.
a = 6: Δ = 1921 + 2508 - 108 = 4321. √4321 ≈ 65.7, no.
a = 7: Δ = 1921 + 2926 - 147 = 4700. √4700 ≈ 68.6, no.
a = 8: Δ = 1921 + 3344 - 192 = 5073. √5073 ≈ 71.2, no.
a = 9: Δ = 1921 + 3762 - 243 = 5440. √5440 ≈ 73.8, no.
a = 10: Δ = 1921 + 4180 - 300 = 5801. √5801 ≈ 76.2, no.
a = 11: Δ = 1921 + 4598 - 363 = 6156. √6156 ≈ 78.5, no.
a = 12: Δ = 1921 + 5016 - 432 = 6505. √6505 ≈ 80.7, no.
a = 13: Δ = 1921 + 5434 - 507 = 6848. √6848 ≈ 82.8, no.
a = 14: Δ = 1921 + 5852 - 588 = 7185. √7185 ≈ 84.8, no.
a = 15: Δ = 1921 + 6270 - 675 = 7516.
