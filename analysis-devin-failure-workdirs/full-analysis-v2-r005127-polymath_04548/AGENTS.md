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
  <problem_id>polymath_04548</problem_id>
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

Let \( \triangle ABC \) be an acute non-equilateral triangle with \(\angle BAC = 60^\circ\). The Euler line of triangle \( \triangle ABC \) intersects side \( BC \) at point \( X \) such that \( B \) lies between \( X \) and \( C \). Given that \( XA = 49 \) and \( XB = 23 \), compute \( XC \).

(The Euler line of a non-equilateral triangle refers to the line through its circumcenter, centroid, and orthocenter.)

## Standard Solution

Let \( H \) and \( O \) denote the orthocenter and circumcenter. We show the existence of two circles from \(\angle A = 60^\circ\) in two claims.

**Claim 1:** In any triangle with \(\angle A = 60^\circ\), we have \( AH = AO = R \), where \( R \) is the circumradius. Hence, one can draw a circle centered at \( A \) through both \( H \) and \( O \).

**Proof:** We use trigonometry. Observe that \(\angle ABH = 90^\circ - \angle BAC = 30^\circ\) and \(\angle BAH = 90^\circ - \angle ABC\). Therefore, \(\angle AHB = 180^\circ - \angle ABH - \angle BAH = 60^\circ + \angle ABC = 180^\circ - \angle ACB\). By the Law of Sines on \(\triangle ABH\), we have

\[
\frac{AH}{\sin \angle ABH} = \frac{AB}{\sin \angle AHB} \Longrightarrow 2AH = \frac{AB}{\sin \angle ACB}.
\]

But the extended law of sines says the right-hand side equals \(2R\), as needed.

**Remark:** In general, for any triangle, it turns out that \( AH = 2R \cos A \), where \( R = AO \) is the circumradius. In the special case \(\angle A = 60^\circ\), we thus get \( AH = AO \).

**Claim 2:** In any triangle with \(\angle A = 60^\circ\), the points \( B, O, H, C \) are cyclic.

**Proof:** Since \(\angle BHC = 180^\circ - \angle A = 120^\circ\) and \(\angle BOC = 2 \angle A = 120^\circ\).

Now on to the main proof. The point \( X \) lies on the radical axis of both circles we just mentioned, so their powers are equal and we get

\[
XA^2 - R^2 = XB \cdot XC = XB(XB + BC).
\]

Since \( XA = 49, XB = 23, BC = 2R \cos 120^\circ = \sqrt{3}R \), we obtain

\[
49^2 - R^2 = 23(23 + R \sqrt{3}) \Longrightarrow R = 16 \sqrt{3}.
\]

Thus \( BC = \sqrt{3} \cdot 16 \sqrt{3} = 48 \) and so \( XC = 23 + 48 = 71 \).

**Remark:** In fact, it turns out that we have a similarity of isosceles triangles

\[
\triangle HAO \sim \triangle AXO.
\]

To see why, let \( M \) and \( N \) be points such that \(\triangle AMO\) and \(\triangle ANO\) are equilateral.

Because \( AO = MO = BO = CO = NO \), we conclude that \( MBCN \) is a cyclic quadrilateral with center \( O \). Similarly, because \( AM = AN = AO = AH \), we conclude that \( MHON \) is a cyclic quadrilateral with center \( A \).

By the Radical Axis Theorem on \((MBCN), (MHON)\), and \((BHOC)\), we see that \( MN \), \( OH \), and \( BC \) are concurrent. Therefore, \( MN \) passes through point \( X \). Because \( MN \) is the perpendicular bisector of \( AO \), we conclude that \( AX = XO \).

Finally, we have shown that \(\triangle AOH\) and \(\triangle AXO\) are both isosceles, and they both share the base angle \(\angle AOH\). Hence, it follows that they are similar.

\(\boxed{71}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this geometry problem.

We have an acute non-equilateral triangle ABC with angle BAC = 60°. The Euler line intersects side BC at point X such that B lies between X and C. Given XA = 49 and XB = 23, compute XC.

Let me set up coordinates. Let me place X at the origin, with BC along the x-axis.

Since B lies between X and C, let me put B at (23, 0) and C at (c, 0) where c = XC > 23 (since B is between X and C, and XB = 23). Wait, actually B lies between X and C means X, B, C are collinear with B between them. So if X is at origin, B is at distance 23 from X, and C is at distance XC from X, with B between them. So B = (23, 0) and C = (XC, 0) where XC > 23.

Wait, but X is on side BC. If B lies between X and C, then X is outside segment BC on the B side. So X, B, C are collinear with order X-B-C. So XB = 23, and XC = XB + BC = 23 + BC. So XC > 23.

Let A = (a, h) for some values. XA = 49, so a² + h² = 49² = 2401.

Now the Euler line passes through X. The Euler line passes through the circumcenter O, centroid G, and orthocenter H.

Let me use the property that the Euler line passes through X which is on line BC.

Let me set up: B = (23, 0), C = (d, 0) where d = XC (what we want to find), X = (0, 0), A = (p, q) with p² + q² = 2401.

Centroid G = ((p + 23 + d)/3, q/3).

Circumcenter O: equidistant from A, B, C. Since B and C are on x-axis, the perpendicular bisector of BC is x = (23 + d)/2. So O = ((23+d)/2, y_O) for some y_O.

O is equidistant from B and A:
((23+d)/2 - 23)² + y_O² = ((23+d)/2 - p)² + (y_O - q)²

Left: ((d-23)/2)² + y_O²
Right: ((23+d)/2 - p)² + y_O² - 2y_O q + q²

So: ((d-23)/2)² = ((23+d)/2 - p)² + q² - 2y_O q

2y_O q = ((23+d)/2 - p)² + q² - ((d-23)/2)²

Let me compute ((23+d)/2 - p)² - ((d-23)/2)². 

Let u = (23+d)/2, v = (d-23)/2. Then u - v = 23, u + v = d.

(u - p)² - v² = u² - 2up + p² - v² = (u² - v²) - 2up + p² = (u-v)(u+v) - 2up + p² = 23d - 2up + p²

So 2y_O q = 23d - 2up + p² + q² = 23d - 2·(23+d)/2·p + 2401 = 23d - (23+d)p + 2401

y_O = [23d - (23+d)p + 2401] / (2q)

Orthocenter H: The orthocenter satisfies H = A + B + C - 2O (in vector form, H = A + B + C - 2O when O is circumcenter). Actually the relation is O + H = A + B + C (the centroid is the midpoint of O and H, and also G = (A+B+C)/3, and G divides OH in ratio 1:2, so H = A+B+C - 2O).

So H = (p + 23 + d, q) - 2·((23+d)/2, y_O) = (p + 23 + d - (23+d), q - 2y_O) = (p, q - 2y_O).

The Euler line passes through O, G, H. It passes through X = (0,0).

Since X is on the Euler line, O, G, H, X are collinear.

The direction of the Euler line: from O to H: H - O = (p - (23+d)/2, q - 2y_O - y_O) = (p - (23+d)/2, q - 3y_O).

Also G - O = ((p+23+d)/3 - (23+d)/2, q/3 - y_O) = ((2p + 46 + 2d - 69 - 3d)/6, q/3 - y_O) = ((2p - 23 - d)/6, q/3 - y_O).

Note H - O = (p - (23+d)/2, q - 3y_O) = (2(2p - 23 - d)/... let me check: 2·(2p-23-d)/6 = (2p-23-d)/3. And p - (23+d)/2 = (2p - 23 - d)/2. So H-O = ((2p-23-d)/2, q - 3y_O). And G-O = ((2p-23-d)/6, q/3 - y_O) = (1/3)·((2p-23-d)/2, q - 3y_O) = (1/3)(H-O). Good, this confirms collinearity of O, G, H.

Now X = (0,0) is on this line. So X - O is parallel to H - O.

X - O = (-(23+d)/2, -y_O).

This must be parallel to (p - (23+d)/2, q - 3y_O).

So: [-(23+d)/2] · (q - 3y_O) = (-y_O) · (p - (23+d)/2)

-(23+d)/2 · (q - 3y_O) = -y_O · (p - (23+d)/2)

(23+d)/2 · (q - 3y_O) = y_O · (p - (23+d)/2)

(23+d)/2 · q - 3(23+d)/2 · y_O = y_O · p - y_O · (23+d)/2

(23+d)/2 · q = y_O · p - y_O · (23+d)/2 + 3(23+d)/2 · y_O

(23+d)/2 · q = y_O · p + 2(23+d)/2 · y_O

(23+d)/2 · q = y_O · (p + 23 + d)

So: y_O = (23+d)/2 · q / (p + 23 + d)

But we also have: y_O = [23d - (23+d)p + 2401] / (2q)

Setting equal:
(23+d)/2 · q / (p + 23 + d) = [23d - (23+d)p + 2401] / (2q)

(23+d) · q² / (p + 23 + d) = 23d - (23+d)p + 2401

Now q² = 2401 - p². So:

(23+d)(2401 - p²) / (p + 23 + d) = 23d - (23+d)p + 2401

Note 2401 - p² = (49 - p)(49 + p). And p + 23 + d... Let me factor differently.

2401 - p² = (49-p)(49+p).

Right side: 23d - (23+d)p + 2401 = 23d - 23p - dp + 2401 = 23(d - p) - dp + 2401.

Hmm, let me try to factor the right side. 23d - (23+d)p + 2401 = 23d - 23p - dp + 2401 = 23(d-p) + 2401 - dp. 

Also = (23-p)(d) + 2401 - 23p + ... let me try: 23d - 23p - dp + 2401 = d(23-p) + 2401 - 23p = d(23-p) + 23(2401/23 - p)... 2401/23 = 104.39... not clean.

Let me try: 23d - (23+d)p + 2401 = (23-p)(d) - dp + 2401 + 23p - 23p... no.

Let me just try: (23-p)(d+23) = 23d + 529 - pd - 23p. Compare to 23d - 23p - dp + 2401. The difference is 2401 - 529 = 1872. So 23d - (23+d)p + 2401 = (23-p)(d+23) + 1872. Hmm, 1872 = 2401 - 529 = 49² - 23² = (49-23)(49+23) = 26·72 = 1872. Yes.

So right side = (23-p)(d+23) + 1872.

Left side: (23+d)(2401-p²)/(p+23+d) = (23+d)(49-p)(49+p)/(p+23+d).

Note 23+d = d+23. And p+23+d = p + (d+23). So left side = (d+23)(49-p)(49+p)/(p + d + 23).

Let me set s = d + 23 (so s = XC + 23... wait, d = XC, so s = XC + 23). Actually let me just keep d.

Let me set u = d + 23. Then:

Left: u(49-p)(49+p)/(p + u)
Right: (23-p)u + 1872

So: u(49-p)(49+p) = (p+u)[(23-p)u + 1872]

u(49²-p²) = (p+u)(23-p)u + 1872(p+u)

u(2401-p²) = u(23-p)(p+u) + 1872(p+u)

u(2401-p²) = u(23p + 23u - p² - pu) + 1872p + 1872u

u(2401-p²) = 23pu + 23u² - p²u - pu² + 1872p + 1872u

2401u - p²u = 23pu + 23u² - p²u - pu² + 1872p + 1872u

2401u = 23pu + 23u² - pu² + 1872p + 1872u

2401u - 1872u = 23pu + 23u² - pu² + 1872p

529u = 23pu + 23u² - pu² + 1872p

529u = u(23p + 23u - pu) + 1872p

529u = u(23p + 23u - pu) + 1872p

Let me rearrange: 529u - 23u² = 23pu - pu² + 1872p = p(23u - u² + 1872) = p(23u - u² + 1872)

So: p = (529u - 23u²) / (23u - u² + 1872) = u(529 - 23u) / (23u - u² + 1872)

Note 529 = 23². So 529 - 23u = 23(23 - u). And 23u - u² + 1872 = -(u² - 23u - 1872) = -(u² - 23u - 1872).

u² - 23u - 1872: discriminant = 529 + 7488 = 8017. √8017... 89² = 7921, 90² = 8100. Not a perfect square. Hmm.

Let me also use the angle condition: angle BAC = 60°.

A = (p, q), B = (23, 0), C = (d, 0).

AB = (23-p, -q), AC = (d-p, -q).

cos(60°) = 1/2 = [(23-p)(d-p) + q²] / (|AB|·|AC|)

|AB|² = (23-p)² + q², |AC|² = (d-p)² + q².

(23-p)(d-p) + q² = (1/2)·|AB|·|AC|

So 2[(23-p)(d-p) + q²] = |AB|·|AC|

4[(23-p)(d-p) + q²]² = |AB|²·|AC|² = [(23-p)² + q²][(d-p)² + q²]

Let me expand. Let a = 23-p, b = d-p. Then q² = 2401 - p².

4[ab + q²]² = [a² + q²][b² + q²]

4a²b² + 8abq² + 4q⁴ = a²b² + a²q² + b²q² + q⁴

3a²b² + 8abq² + 3q⁴ - a²q² - b²q² = 0

3a²b² + q²(8ab - a² - b²) + 3q⁴ = 0

Note 8ab - a² - b² = -(a² - 8ab + b²) = -((a-b)² - 6ab) = 6ab - (a-b)².

Hmm, also note: 8ab - a² - b² = -(a² + b² - 8ab). And a² + b² = (a+b)² - 2ab. So 8ab - a² - b² = 8ab - (a+b)² + 2ab = 10ab - (a+b)².

So: 3a²b² + q²(10ab - (a+b)²) + 3q⁴ = 0

This is a quadratic in ab. Let t = ab.

3t² + q²(10t - (a+b)²) + 3q⁴ = 0

3t² + 10q²t - q²(a+b)² + 3q⁴ = 0

Using quadratic formula:
t = [-10q² ± √(100q⁴ - 12(-q²(a+b)² + 3q⁴))] / 6
= [-10q² ± √(100q⁴ + 12q²(a+b)² - 36q⁴)] / 6
= [-10q² ± √(64q⁴ + 12q²(a+b)²)] / 6
= [-10q² ± q√(64q² + 12(a+b)²)] / 6

For this to give a nice answer, maybe 64q² + 12(a+b)² is a perfect square.

64q² + 12(a+b)² = 4(16q² + 3(a+b)²).

Hmm, this is getting complicated. Let me try a different approach.

Actually, let me use the known result about the Euler line intersecting BC. There's a formula relating the position of X on BC to the triangle's parameters.

Let me use the standard notation: a = BC, b = CA, c = AB, and the angles A, B, C.

The Euler line passes through the centroid G and circumcenter O. Let me find where the Euler line meets BC.

Place B at origin, C at (a, 0). Then A is at some point.

Actually, let me use a coordinate-free approach. The Euler line intersects BC at X. Let me use the ratio.

The centroid G divides the median in ratio 2:1. The foot of the median from A to BC is the midpoint M of BC, with BM = a/2.

G is at 1/3 of the way from M to A, i.e., G = (A + B + C)/3.

The circumcenter O: its projection onto BC is the midpoint of BC (since O is equidistant from B and C). So if we project O onto BC, we get M.

Let me use barycentric or the following: The Euler line in barycentric coordinates.

The circumcenter in barycentric coordinates is (sin 2A : sin 2B : sin 2C).
The centroid is (1 : 1 : 1).

The Euler line in barycentric coordinates passes through these two points. A point on the Euler line is:
(sin 2A + t : sin 2B + t : sin 2C + t) for some parameter t (this is the line through (sin 2A : sin 2B : sin 2C) and (1:1:1)).

Actually, the line through two barycentric points (u1:v1:w1) and (u2:v2:w2) consists of points (λu1+μu2 : λv1+μv2 : λw1+μw2).

So the Euler line consists of points (λ sin 2A + μ : λ sin 2B + μ : λ sin 2C + μ).

This intersects BC (where the first barycentric coordinate is 0) when:
λ sin 2A + μ = 0, i.e., μ = -λ sin 2A.

So the point X on BC has barycentric coordinates (0 : sin 2B - sin 2A : sin 2C - sin 2A).

So X = (0 : sin 2B - sin 2A : sin 2C - sin 2A) on BC.

The ratio BX : XC = (sin 2C - sin 2A) : (sin 2B - sin 2A). 

Wait, in barycentric coordinates on BC, a point (0 : y : z) divides BC such that BX : XC = z : y. Let me double check: B = (0:1:0), C = (0:0:1). A point (0:y:z) = (y·B + z·C)/(y+z). So the point is at parameter z/(y+z) from B. So BX/BC = z/(y+z), and XC/BC = y/(y+z). So BX:XC = z:y.

So BX : XC = (sin 2C - sin 2A) : (sin 2B - sin 2A).

Now, B lies between X and C. This means X is on the extension of BC beyond B. So BX and XC are in opposite directions from B's perspective... actually, if X is beyond B (on the opposite side from C), then X-B-C order. So BX = 23, and XC = XB + BC = 23 + BC. The ratio BX:XC = 23 : XC.

But wait, the barycentric ratio: if X is beyond B, then the barycentric coordinate for B is negative. Let me think again.

If X is on line BC with B between X and C, then in barycentric coordinates (0 : y : z), we need y < 0 (since X is on the B-side extension). Actually, let me think: X = (y·B + z·C)/(y+z). If X is beyond B (away from C), then the weight on C should be negative relative to B... 

Parametrize: X = B + t(C - B) where t = BX/BC (signed). If X is beyond B (opposite side from C), t < 0. Then X = (1-t)B + tC, so barycentric (0 : 1-t : t) with t < 0, meaning 1-t > 1 > 0 and t < 0. So y = 1-t > 0, z = t < 0.

So BX : XC = z : y = t : (1-t). Since t < 0, this ratio is negative. The signed ratio BX/XC = t/(1-t) < 0.

|BX| : |XC| = |t| : |1-t| = (-t) : (1-t) = 23 : XC.

OK so let me just work with signed ratios. Let me define the signed ratio.

X divides BC externally. BX/XC (signed) = -23/XC (since BX = 23 in the direction away from C, and XC is the full distance).

Actually, let me use the formula directly. We have:

BX : XC (as barycentric ratio z:y) = (sin 2C - sin 2A) : (sin 2B - sin 2A)

With X beyond B: the signed ratio BX/XC = (sin 2C - sin 2A)/(sin 2B - sin 2A).

Since X is beyond B, BX and XC have the same sign in terms of directed distances from B... hmm, let me be more careful.

Let me use directed distances along BC from B. Let B be at 0, C at a (where a = BC). X is at position -23 (since XB = 23 and X is on the opposite side from C). XC = a + 23.

The barycentric coordinates of X: (0 : y : z) where X = (y·0 + z·a)/(y+z) = -23. So z·a/(y+z) = -23, meaning z/(y+z) = -23/a. So z = -23(y+z)/a, thus z(1 + 23/a) = -23y/a, z(a+23)/a = -23y/a, z = -23y/(a+23).

So z/y = -23/(a+23) = -23/XC.

And from the formula: z/y = (sin 2C - sin 2A)/(sin 2B - sin 2A).

So: (sin 2C - sin 2A)/(sin 2B - sin 2A) = -23/XC.

Now, A = 60°, so 2A = 120°, sin 2A = sin 120° = √3/2.

sin 2C - sin 2A = sin 2C - √3/2
sin 2B - sin 2A = sin 2B - √3/2

And B + C = 120° (since A = 60°).

Let me also use the condition XA = 49. X is at distance 23 from B on the extension, and A is at distance 49 from X.

Let me use the formula. Let me set B = 120° - C.

sin 2B = sin(240° - 2C) = sin 240° cos 2C - cos 240° sin 2C = (-√3/2)cos 2C - (-1/2)sin 2C = (-√3/2)cos 2C + (1/2)sin 2C.

So sin 2B - √3/2 = (1/2)sin 2C - (√3/2)cos 2C - √3/2 = (1/2)sin 2C - (√3/2)(cos 2C + 1).

cos 2C + 1 = 2cos²C. And (1/2)sin 2C = sin C cos C.

So sin 2B - √3/2 = sin C cos C - √3 cos²C = cos C(sin C - √3 cos C) = cos C · (sin C - √3 cos C).

Similarly, sin 2C - √3/2 = sin 2C - √3/2.

Let me also compute sin 2C - √3/2. Using sin 2C = 2 sin C cos C:
sin 2C - √3/2 = 2 sin C cos C - √3/2.

Hmm, let me try a different approach. Let me use the identity:

sin 2C - sin 2A = 2 cos(C+A) sin(C-A) = 2 cos(120° - C + 60°)... wait, C + A = C + 60°. So sin 2C - sin 2A = 2 cos(C + A) sin(C - A) = 2 cos(C + 60°) sin(C - 60°).

Similarly, sin 2B - sin 2A = 2 cos(B + A) sin(B - A) = 2 cos(B + 60°) sin(B - 60°).

Since B = 120° - C: B + 60° = 180° - C, so cos(B + 60°) = cos(180° - C) = -cos C.
B - 60° = 60° - C, so sin(B - 60°) = sin(60° - C).

So sin 2B - sin 2A = 2(-cos C) sin(60° - C) = -2 cos C sin(60° - C).

And sin 2C - sin 2A = 2 cos(C + 60°) sin(C - 60°) = 2 cos(C + 60°) · (-sin(60° - C)) = -2 cos(C + 60°) sin(60° - C).

So the ratio:
(sin 2C - sin 2A)/(sin 2B - sin 2A) = [-2 cos(C+60°) sin(60°-C)] / [-2 cos C sin(60°-C)] = cos(C+60°)/cos C.

So: cos(C + 60°)/cos C = -23/XC.

Now cos(C + 60°) = cos C cos 60° - sin C sin 60° = (1/2)cos C - (√3/2)sin C.

So cos(C+60°)/cos C = 1/2 - (√3/2) tan C.

Thus: 1/2 - (√3/2) tan C = -23/XC.

So (√3/2) tan C = 1/2 + 23/XC.

tan C = (1 + 46/XC) / √3 = (XC + 46)/(√3 · XC). ... (1)

Now I need another equation from XA = 49.

Let me use the Stewart's theorem or the distance formula. X is on line BC, with XB = 23, XC = d (where d = XC). So BC = d - 23.

XA²: By Stewart's theorem (or just the distance formula), if X is on line BC with XB = 23, XC = d, and X is beyond B:

XA² = (d · AB² - 23 · AC²... hmm, let me use the formula carefully.

Actually, let me use the formula for the distance from A to a point X on line BC.

Place B at origin, C at (BC, 0) = (d-23, 0). X is at (-23, 0). A is at some point (x_A, y_A).

XA² = (x_A + 23)² + y_A² = 49² = 2401.

AB² = x_A² + y_A² = c² (where c = AB).
AC² = (x_A - (d-23))² + y_A² = b² (where b = AC).

From XA²: x_A² + 46x_A + 529 + y_A² = 2401, so c² + 46x_A + 529 = 2401, thus x_A = (2401 - 529 - c²)/46 = (1872 - c²)/46.

Also, AC² = (x_A - (d-23))² + y_A² = x_A² - 2x_A(d-23) + (d-23)² + y_A² = c² - 2x_A(d-23) + (d-23)².

So b² = c² - 2x_A(d-23) + (d-23)².

By the law of cosines: a² = b² + c² - 2bc cos A = b² + c² - bc (since cos 60° = 1/2, so 2bc·(1/2) = bc).

Here a = BC = d - 23.

So (d-23)² = b² + c² - bc.

Also, b² = c² - 2x_A(d-23) + (d-23)², so b² - c² = -2x_A(d-23) + (d-23)² = (d-23)(d-23 - 2x_A).

And from the law of cosines: (d-23)² = b² + c² - bc, so bc = b² + c² - (d-23)².

This is getting complex. Let me try to use the angle C directly.

We have angle C, and we know tan C in terms of d (from equation 1). Let me express things in terms of C and d.

In triangle ABC with A = 60°, B = 120° - C:
a = BC = d - 23
By law of sines: a/sin A = b/sin B = c/sin C = 2R.

So a = 2R sin 60° = R√3, b = 2R sin B = 2R sin(120° - C), c = 2R sin C.

Thus a = R√3, so R = a/√3 = (d-23)/√3.

c = 2R sin C = 2(d-23)/√3 · sin C.
b = 2(d-23)/√3 · sin(120° - C).

Now, XA = 49. Let me compute XA using the formula.

X is beyond B, XB = 23. Using the generalized Stewart's theorem:

For a point X on line BC (extended beyond B), with XB = 23, XC = d:
XA² = (d · c² + 23 · b²... no wait. Let me be careful with signs.

Stewart's theorem for external division: If X divides BC externally with XB = m, XC = n (m = 23, n = d), then:

XA² = (n·c² - m·b²)/(n - m) + m·n... hmm, I need to be careful.

Actually, the standard Stewart's theorem: for cevian from A to point D on BC with BD = m, DC = n, AD = d:
b²m + c²n = a(d² + mn).

For external division, let me use the formula directly. X is at distance 23 from B (on the far side from C), and distance d from C. BC = d - 23.

Using coordinates: B = 0, C = d-23, X = -23, A = (x_A, y_A).

XA² = (x_A + 23)² + y_A²

AB² = c² = x_A² + y_A²
AC² = b² = (x_A - (d-23))² + y_A²

XA² = x_A² + 46x_A + 529 + y_A² = c² + 46x_A + 529 = 2401.

So 46x_A = 2401 - 529 - c² = 1872 - c².
x_A = (1872 - c²)/46.

Also b² = (x_A - (d-23))² + y_A² = x_A² - 2x_A(d-23) + (d-23)² + y_A² = c² - 2x_A(d-23) + (d-23)².

Now, c = 2(d-23)/√3 · sin C, so c² = 4(d-23)²/3 · sin²C.
b = 2(d-23)/√3 · sin(120° - C), so b² = 4(d-23)²/3 · sin²(120° - C).

From b² = c² - 2x_A(d-23) + (d-23)²:

4(d-23)²/3 · sin²(120°-C) = 4(d-23)²/3 · sin²C - 2x_A(d-23) + (d-23)²

Divide by (d-23):

4(d-23)/3 · sin²(120°-C) = 4(d-23)/3 · sin²C - 2x_A + (d-23)

2x_A = 4(d-23)/3 · sin²C - 4(d-23)/3 · sin²(120°-C) + (d-23)

2x_A = (d-23)[4/3(sin²C - sin²(120°-C)) + 1]

sin²C - sin²(120°-C) = [sin C - sin(120°-C)][sin C + sin(120°-C)]

sin C + sin(120°-C) = 2 sin 60° cos(C - 60°) = √3 cos(C-60°)
sin C - sin(120°-C) = 2 cos 60° sin(C - 60°) = sin(C - 60°)

So sin²C - sin²(120°-C) = sin(C-60°) · √3 cos(C-60°) = √3 sin(C-60°)cos(C-60°) = (√3/2) sin(2C - 120°).

So 4/3 · (sin²C - sin²(120°-C)) = 4/3 · (√3/2) sin(2C-120°) = (2√3/3) sin(2C-120°).

2x_A = (d-23)[(2√3/3) sin(2C-120°) + 1]

x_A = (d-23)/2 · [(2√3/3) sin(2C-120°) + 1]

Also from before: x_A = (1872 - c²)/46 = (1872 - 4(d-23)²/3 · sin²C)/46.

This is getting complicated. Let me try a substitution. Let me set t = tan C and express everything in terms of t and d.

From equation (1): tan C = (d + 46)/(√3 d).

Let me denote d = XC (what we want to find).

Let me try to use the condition XA = 49 more directly.

Actually, let me use the formula for XA² in terms of the sides and the position of X.

XA² = c² + 46x_A + 529 where x_A = (1872 - c²)/46.

XA² = c² + 46 · (1872 - c²)/46 + 529 = c² + 1872 - c² + 529 = 2401.

Wait, that's just 2401 = 2401. That's circular! The equation XA = 49 was used to derive x_A, so of course it's satisfied.

I need to use the constraint that A = 60° and the Euler line condition together.

Let me reconsider. I have two conditions:
1. The Euler line passes through X (giving equation 1: tan C = (d+46)/(√3 d))
2. angle A = 60° (already used in the law of sines/cosines)

But I also need to use XA = 49 properly. Let me think about what constrains the triangle.

Given: A = 60°, the Euler line meets BC at X with XB = 23, XC = d, XA = 49.

The triangle is determined by A = 60° and the shape (ratio of sides). The Euler line condition gives a relation between C and d. The XA = 49 condition gives another relation.

Let me parameterize by C (or equivalently by the ratio b:c or by R).

From the Euler line condition: tan C = (d + 46)/(√3 d). This gives d in terms of C:
√3 d tan C = d + 46
d(√3 tan C - 1) = 46
d = 46/(√3 tan C - 1)

Now, XA = 49. Let me express XA in terms of C and R (or C and a = d - 23).

XA² = (x_A + 23)² + y_A² where A = (x_A, y_A) with B at origin, C at (a, 0).

x_A = c cos B (since A projects onto BC at distance c cos B from B). Actually, the foot of the altitude from A to BC is at distance c cos B from B (in an acute triangle, this is between B and C).

Wait, x_A = AB cos B = c cos B. And y_A = c sin B.

So XA² = (c cos B + 23)² + c² sin²B = c² cos²B + 46 c cos B + 529 + c² sin²B = c² + 46 c cos B + 529.

So XA² = c² + 46 c cos B + 529 = 2401.

c² + 46 c cos B = 1872.

Now c = 2R sin C, cos B = cos(120° - C).

c² + 46 c cos B = 4R² sin²C + 92R sin C cos(120° - C) = 1872.

Also a = R√3 = d - 23, so R = (d-23)/√3.

So: 4(d-23)²/3 · sin²C + 92(d-23)/√3 · sin C cos(120°-C) = 1872.

And d = 46/(√3 tan C - 1).

Let me set u = tan C. Then:

d = 46/(√3 u - 1)
d - 23 = 46/(√3u - 1) - 23 = (46 - 23(√3u - 1))/(√3u - 1) = (46 - 23√3u + 23)/(√3u - 1) = (69 - 23√3u)/(√3u - 1) = 23(3 - √3u)/(√3u - 1).

Note: 3 - √3u = √3(√3 - u) and √3u - 1. Hmm.

Let me also compute sin C = u/√(1+u²), cos C = 1/√(1+u²).

cos(120° - C) = cos 120° cos C + sin 120° sin C = (-1/2)(1/√(1+u²)) + (√3/2)(u/√(1+u²)) = (-1 + √3u)/(2√(1+u²)).

sin C cos(120° - C) = [u/√(1+u²)] · [(-1 + √3u)/(2√(1+u²))] = u(-1 + √3u)/(2(1+u²)).

sin²C = u²/(1+u²).

Now plug in:

4(d-23)²/3 · u²/(1+u²) + 92(d-23)/√3 · u(-1+√3u)/(2(1+u²)) = 1872

Let me set w = d - 23 = 23(3 - √3u)/(√3u - 1).

4w²/3 · u²/(1+u²) + 92w/√3 · u(-1+√3u)/(2(1+u²)) = 1872

4w²u²/(3(1+u²)) + 46wu(-1+√3u)/(√3(1+u²)) = 1872

Multiply through by (1+u²):

4w²u²/3 + 46wu(-1+√3u)/√3 = 1872(1+u²)

Let me compute 46/√3 = 46√3/3. So:

4w²u²/3 + 46√3wu(-1+√3u)/3 = 1872(1+u²)

Multiply by 3:

4w²u² + 46√3wu(-1+√3u) = 5616(1+u²)

4w²u² + 46√3wu(√3u - 1) = 5616(1+u²)

4w²u² + 46√3wu·√3u - 46√3wu = 5616(1+u²)

4w²u² + 138wu² - 46√3wu = 5616 + 5616u²

u²(4w² + 138w - 5616) - 46√3wu - 5616 = 0

Now w = 23(3 - √3u)/(√3u - 1). Let me set v = √3u for simplicity. Then u = v/√3, u² = v²/3.

w = 23(3 - v)/(v - 1).

d = 46/(v - 1), d - 23 = w = 23(3-v)/(v-1).

Let me rewrite the equation in terms of v:

(v²/3)(4w² + 138w - 5616) - 46√3·(v/√3)·w - 5616 = 0

(v²/3)(4w² + 138w - 5616) - 46vw - 5616 = 0

Multiply by 3:

v²(4w² + 138w - 5616) - 138vw - 16848 = 0

Now w = 23(3-v)/(v-1). Let me compute w and w².

w = 23(3-v)/(v-1)

Let me set s = v - 1, so v = s + 1, 3 - v = 2 - s.

w = 23(2-s)/s = 23(2/s - 1) = 46/s - 23.

w² = (46/s - 23)² = 2116/s² - 2·46·23/s + 529 = 2116/s² - 2116/s + 529.

4w² = 8464/s² - 8464/s + 2116.

138w = 138(46/s - 23) = 6348/s - 3174.

4w² + 138w - 5616 = 8464/s² - 8464/s + 2116 + 6348/s - 3174 - 5616
= 8464/s² + (-8464 + 6348)/s + (2116 - 3174 - 5616)
= 8464/s² - 2116/s - 6674

Hmm, 2116 - 3174 - 5616 = 2116 - 8790 = -6674.

Let me double check: 2116 + 6348/s - 8464/s - 3174 - 5616. 
Constant: 2116 - 3174 - 5616 = -6674.
1/s: 6348 - 8464 = -2116.
1/s²: 8464.

So 4w² + 138w - 5616 = 8464/s² - 2116/s - 6674.

Note 8464 = 4·2116 = 4·46². And 2116 = 46². And 6674 = ? 6674/2 = 3337. Hmm, 6674 = 6674. Let me check: 6674 = 5616 + 3174 - 2116 = 6674. Or 6674 = 2·3337. 3337 is prime? 3337/47 = 71. 47·71 = 3337. Yes! So 6674 = 2·47·71.

Hmm, not obviously factorable. Let me try a different approach.

Let me factor out 2116 = 46² from the expression:
8464/s² - 2116/s - 6674 = 2116(4/s² - 1/s) - 6674 = 2116(4-s)/(s²) - 6674.

Hmm, 4 - s = 4 - (v-1) = 5 - v. And 6674... let me see if 6674 relates to 2116. 6674/2116 ≈ 3.153. Not clean.

Let me try yet another approach. Let me go back to the equation:

v²(4w² + 138w - 5616) - 138vw - 16848 = 0

with w = 23(3-v)/(v-1) and v = √3 tan C.

Let me substitute w = 23(3-v)/(v-1) directly.

Let me denote r = (3-v)/(v-1). Then w = 23r.

v²(4·529r² + 138·23r - 5616) - 138v·23r - 16848 = 0

v²(2116r² + 3174r - 5616) - 3174vr - 16848 = 0

Factor: 2116 = 4·529, 3174 = 6·529, 5616 = ? 5616/529 ≈ 10.6. Not clean. 5616 = 16·351 = 16·27·13 = 432·13. Hmm. 5616 = 5616. 5616/6 = 936. 5616/4 = 1404. 

Let me try: 2116r² + 3174r - 5616. Divide by 2: 1058r² + 1587r - 2808. 1058 = 2·529 = 2·23². 1587 = 3·529 = 3·23². 2808 = 2808. 2808/23 = 122.08. Not clean.

Let me just plug in and compute numerically to see if there's a nice answer.

Actually, let me try to guess that the answer is a nice number. XC = d. Let me try some values.

d = 46/(√3 tan C - 1). For the triangle to be acute with A = 60°, we need B < 90° and C < 90°, so C ∈ (30°, 90°) (since B = 120° - C > 0 and < 90° means C ∈ (30°, 90°)).

For C ∈ (30°, 90°), tan C ∈ (1/√3, ∞). So √3 tan C ∈ (1, ∞), and √3 tan C - 1 ∈ (0, ∞), so d ∈ (0, ∞). But d > 23 (since XC > XB = 23 as B is between X and C, and BC > 0).

d > 23: 46/(√3 tan C - 1) > 23, so √3 tan C - 1 < 2, √3 tan C < 3, tan C < √3, C < 60°. So C ∈ (30°, 60°).

Let me try d = 26 (a guess). Then √3 tan C - 1 = 46/26 = 23/13, √3 tan C = 36/13, tan C = 36/(13√3) = 12√3/13.

sin C = tan C / √(1+tan²C) = (12√3/13) / √(1 + 432/169) = (12√3/13) / √(601/169) = (12√3/13) / (√601/13) = 12√3/√601.

cos C = 1/√(1+tan²C) = 13/√601.

cos B = cos(120° - C) = cos 120° cos C + sin 120° sin C = (-1/2)(13/√601) + (√3/2)(12√3/√601) = (-13 + 36)/(2√601) = 23/(2√601).

a = d - 23 = 3. R = a/√3 = 3/√3 = √3.

c = 2R sin C = 2√3 · 12√3/√601 = 72/√601.
c² = 5184/601.

XA² = c² + 46c cos B + 529 = 5184/601 + 46·(72/√601)·(23/(2√601)) + 529
= 5184/601 + 46·72·23/(2·601) + 529
= 5184/601 + 46·36·23/601 + 529
= 5184/601 + 38088/601 + 529
= 43272/601 + 529

43272/601 ≈ 72.0. 43272/601 = 72.0? 601·72 = 43272. Yes!

So XA² = 72 + 529 = 601. But we need XA² = 2401 = 49². 601 ≠ 2401.

Hmm, but 601 is interesting. Let me check: if d = 26, XA² = 601, XA = √601 ≈ 24.5. Not 49.

Let me try to find d such that XA = 49.

XA² = c² + 46c cos B + 529 = 2401, so c² + 46c cos B = 1872.

Let me express this in terms of d.

c = 2R sin C = 2(d-23)/√3 · sin C.
cos B = cos(120° - C).

c² + 46c cos B = 4(d-23)²/3 · sin²C + 92(d-23)/√3 · sin C cos(120° - C) = 1872.

Let me use v = √3 tan C, so d = 46/(v-1), d-23 = 23(3-v)/(v-1).

sin C = v/√(3+v²) (since tan C = v/√3, sin C = tan C/√(1+tan²C) = (v/√3)/√(1+v²/3) = (v/√3)/√((3+v²)/3) = v/√(3+v²)).

cos C = √3/√(3+v²).

cos(120° - C) = (-1/2)cos C + (√3/2)sin C = (-1/2)(√3/√(3+v²)) + (√3/2)(v/√(3+v²)) = (√3(v-1))/(2√(3+v²)).

sin C cos(120° - C) = [v/√(3+v²)] · [√3(v-1)/(2√(3+v²))] = √3 v(v-1)/(2(3+v²)).

sin²C = v²/(3+v²).

Now:

4(d-23)²/3 · v²/(3+v²) + 92(d-23)/√3 · √3 v(v-1)/(2(3+v²)) = 1872

4(d-23)²v²/(3(3+v²)) + 92(d-23)v(v-1)/(2(3+v²)) = 1872

4(d-23)²v²/(3(3+v²)) + 46(d-23)v(v-1)/(3+v²) = 1872

Multiply by (3+v²):

4(d-23)²v²/3 + 46(d-23)v(v-1) = 1872(3+v²)

Multiply by 3:

4(d-23)²v² + 138(d-23)v(v-1) = 5616(3+v²)

Let w = d - 23 = 23(3-v)/(v-1).

4w²v² + 138wv(v-1) = 5616(3+v²)

4w²v² + 138wv² - 138wv = 16848 + 5616v²

v²(4w² + 138w - 5616) - 138wv - 16848 = 0

This is the same equation as before. Good.

Now w = 23(3-v)/(v-1). Let me substitute.

Let me set v-1 = t, so v = t+1, 3-v = 2-t, w = 23(2-t)/t.

4w² = 4·529(2-t)²/t² = 2116(2-t)²/t²
138w = 138·23(2-t)/t = 3174(2-t)/t

4w² + 138w - 5616 = 2116(2-t)²/t² + 3174(2-t)/t - 5616

Let me expand (2-t)² = 4 - 4t + t².

= 2116(4 - 4t + t²)/t² + 3174(2-t)/t - 5616
= 2116(4/t² - 4/t + 1) + 3174(2/t - 1) - 5616
= 8464/t² - 8464/t + 2116 + 6348/t - 3174 - 5616
= 8464/t² - 2116/t - 6674

So: v²(8464/t² - 2116/t - 6674) - 138wv - 16848 = 0

With v = t+1, w = 23(2-t)/t:

(t+1)²(8464/t² - 2116/t - 6674) - 138·23(2-t)(t+1)/t - 16848 = 0

(t+1)²(8464/t² - 2116/t - 6674) - 3174(2-t)(t+1)/t - 16848 = 0

Multiply through by t²:

(t+1)²(8464 - 2116t - 6674t²) - 3174(2-t)(t+1)t - 16848t² = 0

Let me expand (t+1)² = t² + 2t + 1.

(t² + 2t + 1)(8464 - 2116t - 6674t²) = ?

Let me compute term by term:
t² · 8464 = 8464t²
t² · (-2116t) = -2116t³
t² · (-6674t²) = -6674t⁴
2t · 8464 = 16928t
2t · (-2116t) = -4232t²
2t · (-6674t²) = -13348t³
1 · 8464 = 8464
1 · (-2116t) = -2116t
1 · (-6674t²) = -6674t²

Sum: -6674t⁴ + (-2116 - 13348)t³ + (8464 - 4232 - 6674)t² + (16928 - 2116)t + 8464
= -6674t⁴ - 15464t³ + (8464 - 4232 - 6674)t² + 14812t + 8464
= -6674t⁴ - 15464t³ - 2442t² + 14812t + 8464

Now the second term: -3174(2-t)(t+1)t = -3174(2t + 2 - t² - t)t = -3174(t + 2 - t²)t = -3174(t² + 2t - t³) = -3174t² - 6348t + 3174t³

Third term: -16848t²

Total: -6674t⁴ - 15464t³ - 2442t² + 14812t + 8464 + 3174t³ - 3174t² - 6348t - 16848t² = 0

= -6674t⁴ + (-15464 + 3174)t³ + (-2442 - 3174 - 16848)t² + (14812 - 6348)t + 8464 = 0

= -6674t⁴ - 12290t³ - 22464t² + 8464t + 8464 = 0

Divide by -2:

3337t⁴ + 6145t³ + 11232t² - 4232t - 4232 = 0

Hmm, let me check if this factors. 3337 = 47·71. 6145 = 5·1229. 11232 = 16·702 = 16·2·351 = 32·351 = 32·27·13 = 32·351. 4232 = 8·529 = 8·23².

Let me try t = 1: 3337 + 6145 + 11232 - 4232 - 4232 = 12250. Not 0.

t = -1: 3337 - 6145 + 11232 + 4232 - 4232 = 8424. Not 0.

Hmm. Let me try to see if there's a rational root. By rational root theorem, possible rational roots are ±(divisors of 4232)/(divisors of 3337).

4232 = 2³ · 23² = 8·529.
3337 = 47·71.

Possible rational roots: ±{1, 2, 4, 8, 23, 46, 92, 184, 529, 1058, 2116, 4232} / {1, 47, 71, 3337} and combinations.

That's a lot. Let me try some simple ones.

t = 2: 3337·16 + 6145·8 + 11232·4 - 4232·2 - 4232 = 53392 + 49160 + 44928 - 8464 - 4232 = 134784. Not 0.

t = 1/2: 3337/16 + 6145/8 + 11232/4 - 4232/2 - 4232 = 208.56 + 768.125 + 2808 - 2116 - 4232 = -2563.3. Not 0.

t = 4/23: This seems unlikely to be nice.

Let me try t = 8/23: 
3337(8/23)⁴ + 6145(8/23)³ + 11232(8/23)² - 4232(8/23) - 4232

This is messy. Let me try a different approach.

Actually, wait. Let me reconsider. Maybe I should look for d being a nice number and work backwards.

Let me try d = 47 (since 47 appears in the factorization).

d = 47: v - 1 = 46/47, v = 93/47. t = v - 1 = 46/47.

Let me check: 3337(46/47)⁴ + 6145(46/47)³ + 11232(46/47)² - 4232(46/47) - 4232

This is messy. Let me compute numerically.

t = 46/47 ≈ 0.9787.

3337(0.9787)⁴ + 6145(0.9787)³ + 11232(0.9787)² - 4232(0.9787) - 4232
≈ 3337(0.9157) + 6145(0.9363) + 11232(0.9579) - 4142.3 - 4232
≈ 3055.7 + 5753.6 + 10759.4 - 4142.3 - 4232
≈ 11194.4. Not 0.

Let me try d = 48. v = 1 + 46/48 = 1 + 23/24 = 47/24. t = 23/24 ≈ 0.9583.

3337(0.9583)⁴ + 6145(0.9583)³ + 11232(0.9583)² - 4232(0.9583) - 4232
≈ 3337(0.8436) + 6145(0.8804) + 11232(0.9184) - 4055.3 - 4232
≈ 2815.0 + 5410.1 + 10314.9 - 4055.3 - 4232
≈ 10252.7. Not 0.

Hmm, the polynomial seems to be always positive for positive t. Let me check the original equation more carefully.

Wait, I think I might have a sign error. Let me recheck.

The equation was: v²(4w² + 138w - 5616) - 138wv - 16848 = 0

Let me recheck the derivation. We had:

4w²v² + 138wv(v-1) = 5616(3+v²)

4w²v² + 138wv² - 138wv = 16848 + 5616v²

v²(4w² + 138w) - 138wv = 16848 + 5616v²

v²(4w² + 138w - 5616) - 138wv - 16848 = 0

Yes, that's correct.

Let me recheck the computation of 4w² + 138w - 5616 with w = 23(2-t)/t, t = v-1.

w = 23(2-t)/t.

4w² = 4·529·(2-t)²/t² = 2116(2-t)²/t²
138w = 3174(2-t)/t

4w² + 138w - 5616 = [2116(2-t)² + 3174(2-t)t - 5616t²] / t²

Let me expand the numerator:
2116(4 - 4t + t²) + 3174(2t - t²) - 5616t²
= 8464 - 8464t + 2116t² + 6348t - 3174t² - 5616t²
= 8464 + (-8464 + 6348)t + (2116 - 3174 - 5616)t²
= 8464 - 2116t - 6674t²

So 4w² + 138w - 5616 = (8464 - 2116t - 6674t²)/t².

Now the equation:
v² · (8464 - 2116t - 6674t²)/t² - 138wv - 16848 = 0

v = t+1, w = 23(2-t)/t:

(t+1)²(8464 - 2116t - 6674t²)/t² - 138·23(2-t)(t+1)/t - 16848 = 0

Multiply by t²:

(t+1)²(8464 - 2116t - 6674t²) - 3174(2-t)(t+1)t - 16848t² = 0

Let me re-expand (t+1)²(8464 - 2116t - 6674t²):

(t² + 2t + 1)(8464 - 2116t - 6674t²)

= t²·8464 + t²·(-2116t) + t²·(-6674t²) + 2t·8464 + 2t·(-2116t) + 2t·(-6674t²) + 1·8464 + 1·(-2116t) + 1·(-6674t²)

= 8464t² - 2116t³ - 6674t⁴ + 16928t - 4232t² - 13348t³ + 8464 - 2116t - 6674t²

= -6674t⁴ + (-2116 - 13348)t³ + (8464 - 4232 - 6674)t² + (16928 - 2116)t + 8464

= -6674t⁴ - 15464t³ + (8464 - 4232 - 6674)t² + 14812t + 8464

8464 - 4232 - 6674 = 8464 - 10906 = -2442

= -6674t⁴ - 15464t³ - 2442t² + 14812t + 8464

Now -3174(2-t)(t+1)t:

(2-t)(t+1) = 2t + 2 - t² - t = t + 2 - t²

(t + 2 - t²)t = t² + 2t - t³

-3174(t² + 2t - t³) = -3174t² - 6348t + 3174t³

Now -16848t².

Total:
-6674t⁴ - 15464t³ - 2442t² + 14812t + 8464 + 3174t³ - 3174t² - 6348t - 16848t²

= -6674t⁴ + (-15464 + 3174)t³ + (-2442 - 3174 - 16848)t² + (14812 - 6348)t + 8464

= -6674t⁴ - 12290t³ + (-22464)t² + 8464t + 8464

So: -6674t⁴ - 12290t³ - 22464t² + 8464t + 8464 = 0

Divide by -2:
3337t⁴ + 6145t³ + 11232t² - 4232t - 4232 = 0

Let me verify with the d=26 case. d=26, v = 1 + 46/26 = 1 + 23/13 = 36/13. t = v-1 = 23/13.

3337(23/13)⁴ + 6145(23/13)³ + 11232(23/13)² - 4232(23/13) - 4232

Let me compute each term:
(23/13)² = 529/169
(23/13)³ = 12167/2197
(23/13)⁴ = 279841/28561

3337 · 279841/28561 = 3337 · 279841 / 28561

This is getting very messy. Let me just verify numerically.

t = 23/13 ≈ 1.7692

3337(1.7692)⁴ + 6145(1.7692)³ + 11232(1.7692)² - 4232(1.7692) - 4232

(1.7692)² ≈ 3.1301
(1.7692)³ ≈ 5.5392
(1.7692)⁴ ≈ 9.8005

3337·9.8005 + 6145·5.5392 + 11232·3.1301 - 4232·1.7692 - 4232
≈ 32703 + 34038 + 35155 - 7488 - 4232
≈ 90176. Not 0.

But we showed d=26 gives XA² = 601, not 2401. So d=26 is not a solution, which is consistent.

Let me think about what value of d would work. We need XA = 49, which is much larger than √601 ≈ 24.5. So d should be much larger.

For large d, v ≈ 1 (since v = 1 + 46/d), t ≈ 46/d ≈ 0. So the polynomial at t≈0 is approximately 8464 - 4232·0 - 4232·0... wait, at t=0: 3337·0 + 6145·0 + 11232·0 - 4232·0 - 4232 = -4232. So the polynomial is -4232 at t=0, which is negative.

At t = 1 (d = 46): 3337 + 6145 + 11232 - 4232 - 4232 = 12250. Positive.

So there's a root between 0 and 1. Since t = 46/d, t ∈ (0, 1) corresponds to d ∈ (46, ∞). But we need d > 23 and C ∈ (30°, 60°), which means d ∈ (23, ∞) and v ∈ (1, 3), t ∈ (0, 2).

Actually, let me check: C ∈ (30°, 60°), tan C ∈ (1/√3, √3), v = √3 tan C ∈ (1, 3), t = v - 1 ∈ (0, 2).

At t = 0: polynomial = -4232 < 0.
At t = 1: polynomial = 12250 > 0.
At t = 2: 3337·16 + 6145·8 + 11232·4 - 4232·2 - 4232 = 53392 + 49160 + 44928 - 8464 - 4232 = 134784 > 0.

So there's a root between 0 and 1. Let me find it.

Let me try t = 0.5: 3337/16 + 6145/8 + 11232/4 - 4232/2 - 4232 = 208.56 + 768.125 + 2808 - 2116 - 4232 = -2563.3. Negative.

t = 0.7: 3337(0.2401) + 6145(0.343) + 11232(0.49) - 4232(0.7) - 4232
= 801.2 + 2107.8 + 5503.7 - 2962.4 - 4232 = 1218.3. Positive.

t = 0.6: 3337(0.1296) + 6145(0.216) + 11232(0.36) - 4232(0.6) - 4232
= 432.5 + 1327.3 + 4043.5 - 2539.2 - 4232 = -967.9. Negative.

t = 0.65: 3337(0.1785) + 6145(0.2746) + 11232(0.4225) - 4232(0.65) - 4232
= 595.6 + 1687.4 + 4745.5 - 2750.8 - 4232 = 45.7. Close to 0!

t = 0.648: 3337(0.1764) + 6145(0.2721) + 11232(0.4199) - 4232(0.648) - 4232
= 588.6 + 1672.2 + 4716.3 - 2742.3 - 4232 = 2.8. Very close!

t = 0.6477: Let me be more precise.

Actually, let me check if t = 2/3 works exactly.

t = 2/3: 3337(16/81) + 6145(8/27) + 11232(4/9) - 4232(2/3) - 4232

= 3337·16/81 + 6145·8/27 + 11232·4/9 - 4232·2/3 - 4232

= 53392/81 + 49160/27 + 44928/9 - 8464/3 - 4232

Convert to 81ths:
= 53392/81 + 147480/81 + 404352/81 - 228528/81 - 342792/81

= (53392 + 147480 + 404352 - 228528 - 342792)/81

= (605224 - 571320)/81 = 33904/81 ≈ 418.6. Not 0.

Let me try t = 23/47 (since 47 is a factor of 3337):

t = 23/47 ≈ 0.4894. Already checked t=0.5 gives negative, so this is negative too.

Let me try t = 46/71 (since 71 is a factor of 3337):

t = 46/71 ≈ 0.6479.

3337(46/71)⁴ + 6145(46/71)³ + 11232(46/71)² - 4232(46/71) - 4232

Note 3337 = 47·71. So 3337/71⁴ = 47·71/71⁴ = 47/71³.

3337·46⁴/71⁴ = 47·46⁴/71³
6145·46³/71³ = 6145·46³/71³
11232·46²/71² = 11232·46²·71/71³
4232·46/71 = 4232·46·71²/71³
4232 = 4232·71³/71³

Common denominator 71³ = 357911.

Numerator = 47·46⁴ + 6145·46³ + 11232·46²·71 - 4232·46·71² - 4232·71³

46² = 2116, 46³ = 97336, 46⁴ = 4477456.

47·4477456 = 210440432
6145·97336 = 598121720
11232·2116·71 = 11232·150236 = 1687052352
4232·46·71² = 4232·46·5041 = 4232·231886 = 981735952
4232·357911 = 1514489752

Numerator = 210440432 + 598121720 + 1687052352 - 981735952 - 1514489752
= (210440432 + 598121720 + 1687052352) - (981735952 + 1514489752)
= 2485614504 - 2496225704
= -10611200

Not 0. Close though? -10611200/357911 ≈ -29.6. Not 0.

Let me try to be more systematic. The root is near t ≈ 0.648. Let me compute more precisely.

f(t) = 3337t⁴ + 6145t³ + 11232t² - 4232t - 4232

f(0.648) = 3337(0.648)⁴ + 6145(0.648)³ + 11232(0.648)² - 4232(0.648) - 4232

0.648² = 0.419904
0.648³ = 0.272098
0.648⁴ = 0.176320

3337·0.176320 = 588.25
6145·0.272098 = 1672.04
11232·0.419904 = 4716.53
4232·0.648 = 2742.34

f = 588.25 + 1672.04 + 4716.53 - 2742.34 - 4232 = 2.48

f(0.6477) = ?
0.6477² = 0.419515
0.6477³ = 0.271715
0.6477⁴ = 0.175983

3337·0.175983 = 587.21
6145·0.271715 = 1670.08
11232·0.419515 = 4712.10
4232·0.6477 = 2741.07

f = 587.21 + 1670.08 + 4712.10 - 2741.07 - 4232 = -3.68

So root is between 0.6477 and 0.648. Let me try 0.6478:

0.6478² = 0.419645
0.6478³ = 0.271831
0.6478⁴ = 0.176066

3337·0.176066 = 587.49
6145·0.271831 = 1670.80
11232·0.419645 = 4713.57
4232·0.6478 = 2741.49

f = 587.49 + 1670.80 + 4713.57 - 2741.49 - 4232 = -1.63

0.6479:
0.6479² = 0.419774
0.6479³ = 0.271947
0.6479⁴ = 0.176149

3337·0.176149 = 587.77
6145·0.271947 = 1671.51
11232·0.419774 = 4715.03
4232·0.6479 = 2741.91

f = 587.77 + 1671.51 + 4715.03 - 2741.91 - 4232 = 0.40

So root ≈ 0.64788. Then d = 46/t ≈ 46/0.64788 ≈ 70.999... ≈ 71!

Let me check d = 71. Then t = 46/71.

f(46/71) = 3337(46/71)⁴ + 6145(46/71)³ + 11232(46/71)² - 4232(46/71) - 4232

I computed this above and got -10611200/357911 ≈ -29.65. That's not 0.

Hmm, but numerically the root is at t ≈ 0.64788, and 46/71 ≈ 0.64789. Very close but not exact.

Let me recheck my computation. Actually, let me recompute more carefully.

3337 = 47 · 71. Let me verify: 47 · 71 = 47 · 70 + 47 = 3290 + 47 = 3337. Yes.

f(46/71): Let me compute with exact fractions.

3337 · (46/71)⁴ = 3337 · 46⁴ / 71⁴ = (47·71) · 46⁴ / 71⁴ = 47 · 46⁴ / 71³

6145 · (46/71)³ = 6145 · 46³ / 71³

11232 · (46/71)² = 11232 · 46² / 71² = 11232 · 46² · 71 / 71³

4232 · (46/71) = 4232 · 46 · 71² / 71³

4232 = 4232 · 71³ / 71³

Common denominator: 71³ = 357911.

Numerator:
47 · 46⁴ + 6145 · 46³ + 11232 · 46² · 71 - 4232 · 46 · 71² - 4232 · 71³

46² = 2116
46³ = 97336
46⁴ = 4477456
71² = 5041
71³ = 357911

47 · 4477456 = 210,440,432
6145 · 97336 = let me compute: 6000 · 97336 = 584,016,000; 145 · 97336 = 14,113,720. Total = 598,129,720.

Wait, let me recompute: 6145 · 97336.
6145 · 97000 = 596,065,000
6145 · 336 = 2,064,720
Total = 598,129,720.

11232 · 2116 · 71:
11232 · 2116 = 11232 · 2000 + 11232 · 116 = 22,464,000 + 1,302,912 = 23,766,912
23,766,912 · 71 = 23,766,912 · 70 + 23,766,912 = 1,663,683,840 + 23,766,912 = 1,687,450,752

4232 · 46 · 5041:
4232 · 46 = 194,672
194,672 · 5041 = 194,672 · 5000 + 194,672 · 41 = 973,360,000 + 7,981,552 = 981,341,552

4232 · 357911:
4232 · 357,911 = 4232 · 357000 + 4232 · 911 = 1,510,824,000 + 3,855,352 = 1,514,679,352

Numerator = 210,440,432 + 598,129,720 + 1,687,450,752 - 981,341,552 - 1,514,679,352

Positive sum: 210,440,432 + 598,129,720 + 1,687,450,752 = 2,496,020,904
Negative sum: 981,341,552 + 1,514,679,352 = 2,496,020,904

Numerator = 2,496,020,904 - 2,496,020,904 = 0!

So f(46/71) = 0! The root is exactly t = 46/71.

So d = 46/t = 46/(46/71) = 71.

Wait, but earlier I got -10611200. I must have made an arithmetic error. Let me trust this computation.

So XC = d = 71.

Let me verify: d = 71, t = 46/71, v = 1 + 46/71 = 117/71.

v = √3 tan C = 117/71, so tan C = 117/(71√3) = 39√3/71.

C = arctan(39√3/71). Let me check this is in (30°, 60°). tan 30° = 1/√3 ≈ 0.577. tan 60° = √3 ≈ 1.732. 39√3/71 ≈ 39·1.732/71 ≈ 67.55/71 ≈ 0.951. So C ≈ 43.5°. In range.

B = 120° - C ≈ 76.5°. B < 90°, so the triangle is acute. Good.

Let me verify XA = 49.

d = 71, a = BC = d - 23 = 48. R = a/√3 = 48/√3 = 16√3.

tan C = 39√3/71. 
sin C = tan C / √(1 + tan²C) = (39√3/71) / √(1 + 39²·3/71²) = (39√3/71) / √((71² + 39²·3)/71²) = (39√3/71) / √((5041 + 4563)/5041) = (39√3/71) / √(9604/5041) = (39√3/71) / (98/71) = 39√3/98.

cos C = 1/√(1 + tan²C) = 71/98.

Check: sin²C + cos²C = (39²·3 + 71²)/98² = (4563 + 5041)/9604 = 9604/9604 = 1. ✓

c = 2R sin C = 2·16√3·39√3/98 = 32√3·39√3/98 = 32·39·3/98 = 3744/98 = 1928/49.

Hmm, let me simplify: 3744/98 = 1872/49.

cos B = cos(120° - C) = cos 120° cos C + sin 120° sin C = (-1/2)(71/98) + (√3/2)(39√3/98) = (-71 + 39·3)/(2·98) = (-71 + 117)/196 = 46/196 = 23/98.

XA² = c² + 46c cos B + 529

c = 1872/49, c² = 1872²/49² = 3504384/2401.

46c cos B = 46 · (1872/49) · (23/98) = 46 · 1872 · 23 / (49 · 98) = 46 · 1872 · 23 / 4802.

46 · 23 = 1058. 1058 · 1872 = 1058 · 1872. 
1000 · 1872 = 1,872,000
58 · 1872 = 108,576
Total = 1,980,576.

49 · 98 = 4802.

46c cos B = 1,980,576 / 4802. 

4802 = 2 · 2401 = 2 · 49². 1,980,576 / 4802 = 1,980,576 / 4802. 

Let me simplify: 1,980,576 / 2 = 990,288. 4802/2 = 2401. So = 990,288/2401.

990288 / 2401: 2401 · 412 = 2401 · 400 + 2401 · 12 = 960400 + 28812 = 989212. 990288 - 989212 = 1076. 1076/2401... not clean. Let me recheck.

Hmm, let me recompute. c = 1872/49. cos B = 23/98.

46 · c · cos B = 46 · (1872/49) · (23/98)

= (46 · 1872 · 23) / (49 · 98)

46 · 23 = 1058
1058 · 1872: 
1058 · 1000 = 1,058,000
1058 · 800 = 846,400
1058 · 72 = 76,176
Total = 1,980,576

49 · 98 = 4,802

1,980,576 / 4,802. Let me try: 4,802 · 412 = 4,802 · 400 + 4,802 · 12 = 1,920,800 + 57,624 = 1,978,424. 1,980,576 - 1,978,424 = 2,152. 2,152/4,802... not clean.

Hmm, let me recheck. Maybe I should simplify before multiplying.

46 · 1872 · 23 / (49 · 98)

1872 = 48 · 39 = 16 · 3 · 39 = 16 · 117. Actually 1872 = 1872. 1872/49 = 1872/49. gcd(1872, 49): 49 = 7². 1872/7 = 267.43. Not divisible. So 1872/49 is already simplified.

98 = 2 · 49. So 49 · 98 = 49 · 2 · 49 = 2 · 49² = 2 · 2401 = 4802.

46 · 23 = 1058 = 2 · 529 = 2 · 23².

So (2 · 23² · 1872) / (2 · 49²) = (23² · 1872) / 49² = (529 · 1872) / 2401.

529 · 1872 = 529 · 1872. 500 · 1872 = 936,000. 29 · 1872 = 54,288. Total = 990,288.

990,288 / 2401. 2401 · 412 = 989,212. 990,288 - 989,212 = 1,076. 1076/2401. 1076 = 4 · 269. 2401 = 49². 269 is prime. So not clean.

Hmm, that's concerning. Let me recheck my computation of c.

c = 2R sin C = 2 · 16√3 · (39√3/98) = 32√3 · 39√3/98 = 32 · 39 · 3/98 = 3744/98.

3744/98: gcd(3744, 98). 98 = 2 · 49. 3744/2 = 1872. 1872/49: 49 · 38 = 1862. 1872 - 1862 = 10. Not divisible. So c = 1872/49.

Hmm wait, let me recheck R. a = BC = d - 23 = 71 - 23 = 48. R = a/√3 = 48/√3 = 16√3. Yes.

Let me recheck sin C. tan C = 39√3/71. 

1 + tan²C = 1 + (39²·3)/71² = 1 + 4563/5041 = (5041 + 4563)/5041 = 9604/5041.

√(9604/5041) = 98/71 (since 98² = 9604 and 71² = 5041).

sin C = tan C / √(1 + tan²C) = (39√3/71) / (98/71) = 39√3/98. ✓

cos C = 1/√(1+tan²C) = 71/98. ✓

c = 2 · 16√3 · 39√3/98 = 32 · 39 · 3/98 = 3744/98 = 1872/49. ✓

cos B = 23/98. ✓

XA² = c² + 46c cos B + 529

= (1872/49)² + 46 · (1872/49) · (23/98) + 529

= 1872²/49² + (46 · 23 · 1872)/(49 · 98) + 529

= 3504384/2401 + (1058 · 1872)/4802 + 529

= 3504384/2401 + 1980576/4802 + 529

Note 4802 = 2 · 2401, so 1980576/4802 = 990288/2401.

XA² = 3504384/2401 + 990288/2401 + 529

= (3504384 + 990288)/2401 + 529

= 4494672/2401 + 529

4494672/2401: 2401 · 1872 = 2401 · 1872. 2401 · 1000 = 2,401,000. 2401 · 800 = 1,920,800. 2401 · 72 = 172,872. Total = 4,494,672. 

So 4494672/2401 = 1872.

XA² = 1872 + 529 = 2401 = 49². ✓

So XA = 49. The answer is XC = 71.

Let me also verify the Euler line condition. We need to verify that the Euler line actually passes through X.

We have d = 71, so XC = 71, XB = 23, BC = 48.

tan C = 39√3/71, C ≈ 43.5°. B = 120° - C ≈ 76.5°. A = 60°.

The Euler line meets BC at X with BX:XC (signed) = (sin 2C - sin 2A)/(sin 2B - sin 2A) = cos(C+60°)/cos C (as derived).

cos(C + 60°) = cos C cos 60° - sin C sin 60° = (71/98)(1/2) - (39√3/98)(√3/2) = (71 - 39·3)/(2·98) = (71 - 117)/196 = -46/196 = -23/98.

cos C = 71/98.

So the ratio = (-23/98)/(71/98) = -23/71.

This means (signed) BX/XC = -23/71, i.e., |BX|/XC = 23/71, so XB = 23 and XC = 71. ✓

And B is between X and C (since the ratio is negative, X is external). ✓

The triangle is acute: A = 60°, B ≈ 76.5° < 90°, C ≈ 43.5° < 90°. ✓

Non-equilateral: clearly not equilateral. ✓

So XC = 71.

Let me write up the proof.

**Proof:**

Let me set up the problem using barycentric coordinates and the Euler line.

**Step 1: Euler line intersection with BC.**

The circumcenter has barycentric coordinates $(\sin 2A : \sin 2B : \sin 2C)$ and the centroid is $(1:1:1)$. The Euler line passes through both. A general point on this line is $(\lambda \sin 2A + \mu : \lambda \sin 2B + \mu : \lambda \sin 2C + \mu)$.

Setting the first coordinate to 0 (to find intersection with $BC$), we get $\mu = -\lambda \sin 2A$, giving $X = (0 : \sin 2B - \sin 2A : \sin 2C - \sin 2A)$.

The signed ratio is:
$$\frac{BX}{XC} = \frac{\sin 2C - \sin 2A}{\sin 2B - \sin 2A}$$

**Step 2: Simplify using A = 60°.**

With $A = 60°$ and $B = 120° - C$:

$\sin 2C - \sin 2A = 2\cos(C + A)\sin(C - A) = 2\cos(C + 60°)\sin(C - 60°)$

$\sin 2B - \sin 2A = 2\cos(B + A)\sin(B - A) = 2\cos(180° - C)\sin(60° - C) = -2\cos C \sin(60° - C)$

Note $\sin(C - 60°) = -\sin(60° - C)$, so:

$$\frac{BX}{XC} = \frac{-2\cos(C + 60°)\sin(60° - C)}{-2\cos C \sin(60° - C)} = \frac{\cos(C + 60°)}{\cos C}$$

Since $B$ lies between $X$ and $C$, this ratio is negative:
$$\frac{\cos(C + 60°)}{\cos C} = -\frac{23}{XC}$$

Expanding: $\cos(C + 60°) = \frac{1}{2}\cos C - \frac{\sqrt{3}}{2}\sin C$, so:

$$\frac{1}{2} - \frac{\sqrt{3}}{2}\tan C = -\frac{23}{XC}$$

$$\tan C = \frac{XC + 46}{\sqrt{3} \cdot XC}$$

**Step 3: Use XA = 49.**

Place $B$ at the origin, $C$ at $(a, 0)$ where $a = BC = XC - 23$. Then $X = (-23, 0)$ and $A = (c\cos B, c\sin B)$ where $c = AB$.

$$XA^2 = (c\cos B + 23)^2 + c^2\sin^2 B = c^2 + 46c\cos B + 529 = 2401$$

So $c^2 + 46c\cos B = 1872$.

By the law of sines with $A = 60°$: $a = R\sqrt{3}$, $c = 2R\sin C$, and $\cos B = \cos(120° - C) = -\frac{1}{2}\cos C + \frac{\sqrt{3}}{2}\sin C$.

Setting $v = \sqrt{3}\tan C$ and $d = XC$, we have $d = \frac{46}{v - 1}$ and $a = d - 23 = \frac{23(3 - v)}{v - 1}$.

Substituting into $c^2 + 46c\cos B = 1872$ and simplifying (using $\sin C = \frac{v}{\sqrt{3 + v^2}}$, $\cos C = \frac{\sqrt{3}}{\sqrt{3 + v^2}}$), we obtain after algebraic manipulation:

$$3337t^4 + 6145t^3 + 11232t^2 - 4232t - 4232 = 0$$

where $t = v - 1 = \frac{46}{d}$.

**Step 4: Solve.**

Testing $t = \frac{46}{71}$ (i.e., $d = 71$): since $3337 = 47 \times 71$, substituting and computing with common denominator $71^3$:

Numerator $= 47 \cdot 46^4 + 6145 \cdot 46^3 + 11232 \cdot 46^2 \cdot 71 - 4232 \cdot 46 \cdot 71^2 - 4232 \cdot 71^3$

$= 210440432 + 598129720 + 1687450752 - 981341552 - 1514679352 = 0$ ✓

So $d = XC = 71$.

**Step 5: Verify.**

With $XC = 71$: $BC = 48$, $R = 16\sqrt{3}$, $\tan C = \frac{39\sqrt{3}}{71}$, $\sin C = \frac{39\sqrt{3}}{98}$, $\cos C = \frac{71}{98}$, $c = \frac{1872}{49}$, $\cos B = \frac{23}{98}$.

$XA^2 = \frac{1872^2}{49^2} + 46 \cdot \frac{1872}{49} \cdot \frac{23}{98} + 529 = \frac{3504384 + 990288}{2401} + 529 = 1872 + 529 = 2401 = 49^2$ ✓

Euler line ratio: $\frac{\cos(C + 60°)}{\cos C} = \frac{-23/98}{71/98} = -\frac{23}{71}$, giving $XB = 23$, $XC = 71$ ✓

Triangle is acute ($A = 60°$, $B \approx 76.5°$, $C \approx 43.5°$) and non-equilateral ✓

$$XC = \boxed{71}$$

### PROOF COMPLETE
