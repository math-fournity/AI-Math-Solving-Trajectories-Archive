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
  <problem_id>polymath_02695</problem_id>
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

Let \( P \) and \( Q \) be points on a circle of radius 10, and let \( M \) be a point on \( PQ \) such that \( PM = 5 \) and \( QM = 10 \). Let \( A, B, C, D \) be points on the circle such that chords \( AB \) and \( CD \) intersect at \( M \). Let \( X \) be the intersection of \( AD \) and \( PQ \), and let \( Y \) be the intersection of \( BC \) and \( PQ \). If \( XM = 3 \), then find \( YM \).

## Standard Solution

To solve the problem, we need to find the distance \( YM \) given that \( XM = 3 \).

First, let's establish the given information:
- Points \( P \) and \( Q \) lie on a circle with radius 10.
- Point \( M \) is on \( PQ \) such that \( PM = 5 \) and \( QM = 10 \).
- Chords \( AB \) and \( CD \) intersect at \( M \).
- Points \( X \) and \( Y \) are the intersections of \( AD \) and \( BC \) with \( PQ \), respectively.
- \( XM = 3 \).

We need to find \( YM \).

### Step 1: Use the Power of a Point Theorem
The Power of a Point theorem states that for a point \( M \) inside a circle, the product of the segments of one intersecting chord is equal to the product of the segments of the other intersecting chord. Mathematically, this is expressed as:
\[
MA \cdot MB = MC \cdot MD
\]
Given that \( M \) is the intersection of chords \( AB \) and \( CD \), we have:
\[
MA \cdot MB = MC \cdot MD = 50
\]
This is because \( M \) divides \( PQ \) into segments \( PM = 5 \) and \( QM = 10 \), and the total length of \( PQ \) is 15. The product of the segments of \( PQ \) is:
\[
PM \cdot QM = 5 \cdot 10 = 50
\]

### Step 2: Apply the Power of a Point to Points \( X \) and \( Y \)
The Power of a Point theorem also applies to points \( X \) and \( Y \) on \( PQ \). For point \( X \):
\[
XA \cdot XD = XP \cdot XQ
\]
Given \( XM = 3 \), we have:
\[
XP = PM + XM = 5 + 3 = 8
\]
\[
XQ = QM - XM = 10 - 3 = 7
\]
Thus:
\[
XA \cdot XD = 8 \cdot 7 = 56
\]

For point \( Y \):
\[
YB \cdot YC = YP \cdot YQ
\]
Let \( YM = y \). Then:
\[
YP = PM + YM = 5 + y
\]
\[
YQ = QM - YM = 10 - y
\]
Thus:
\[
YB \cdot YC = (5 + y)(10 - y)
\]

### Step 3: Relate the Products
Since \( XA \cdot XD = YB \cdot YC \) (both are equal to the power of point \( M \) with respect to the circle):
\[
56 = (5 + y)(10 - y)
\]

### Step 4: Solve for \( y \)
Expand and solve the equation:
\[
56 = 50 + 5y - 10y - y^2
\]
\[
56 = 50 - 5y - y^2
\]
Rearrange to form a quadratic equation:
\[
y^2 + 5y - 6 = 0
\]

### Step 5: Solve the Quadratic Equation
Use the quadratic formula \( y = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \), where \( a = 1 \), \( b = 5 \), and \( c = -6 \):
\[
y = \frac{-5 \pm \sqrt{5^2 - 4 \cdot 1 \cdot (-6)}}{2 \cdot 1}
\]
\[
y = \frac{-5 \pm \sqrt{25 + 24}}{2}
\]
\[
y = \frac{-5 \pm \sqrt{49}}{2}
\]
\[
y = \frac{-5 \pm 7}{2}
\]

This gives two solutions:
\[
y = \frac{2}{2} = 1 \quad \text{and} \quad y = \frac{-12}{2} = -6
\]

Since \( YM \) must be a positive distance:
\[
YM = 16.6667
\]

Thus, the distance \( YM \) is:
\[
\boxed{\frac{50}{3}}
\]

## AI's Thinking (Attempted Solution Process)

Let me solve this geometry problem. Let me set up coordinates and use the power of a point.

Setup: Circle of radius 10. Points P, Q on circle. M on PQ with PM=5, QM=10. So PQ = 15.

Power of point M with respect to the circle: Since M is inside the circle (PQ is a chord of length 15, and M divides it as PM=5, QM=10), the power is negative: Power(M) = PM · QM = 5·10 = 50, but with sign. Actually for a point inside the circle, power = -PM·QM = -50. Wait, let me be careful.

The power of M = (signed) product. For chords through M, if M is inside, the product of the two segments equals PM·QM. So for any chord through M, MA·MB = MC·MD = PM·QM = 50.

Let me verify M is inside. The chord PQ has length 15. The distance from center O to chord PQ: half-chord = 7.5, radius = 10, so distance = √(100 - 56.25) = √43.75. M is at distance 5 from P along the chord. The midpoint of PQ is at 7.5 from P. So M is at 7.5 - 5 = 2.5 from midpoint, on P's side. Distance from O to M: √(43.75 + 6.25) = √50. So OM = √50 ≈ 7.07 < 10. Yes, M is inside. Power = OM² - R² = 50 - 100 = -50. So MA·MB = MC·MD = 50.

Now, chords AB and CD intersect at M. X = AD ∩ PQ, Y = BC ∩ PQ. XM = 3. Find YM.

This is a classic projective geometry / cross-ratio problem. Let me think about it using the cross-ratio on line PQ.

Consider the complete quadrilateral formed by lines AB, CD, AD, BC (or the four points A, B, C, D on the circle). The line PQ intersects:
- AB at M (since AB passes through M)
- CD at M (since CD passes through M)
- AD at X
- BC at Y

Wait, AB and CD both pass through M. So on line PQ, the intersections are: M (from AB), M (from CD), X (from AD), Y (from BC).

Hmm, this is the setup for the involution / cross-ratio relation.

Actually, let me think about this differently. Consider the pencil from M. The four lines MA, MB, MC, MD... no wait, A and B are on one line through M, C and D on another.

Let me use the cross-ratio approach. Consider the four points A, B, C, D on the circle. The line PQ cuts the sides of the complete quadrilateral ABCD.

The complete quadrilateral has vertices A, B, C, D and its three diagonal points. The sides are AB, BC, CD, DA, AC, BD. The diagonal points are: AB∩CD = M, AC∩BD, AD∩BC.

Line PQ passes through M (= AB∩CD) and intersects AD at X and BC at Y.

There's a classical result: if a line through one diagonal point of a complete quadrilateral inscribed in a conic meets the other two sides, then the cross-ratio is harmonic, or there's an involution.

Actually, let me use the involution on line PQ induced by the conic. The conic (circle) induces an involution on any line: each point on the line is paired with its "conjugate" via the polar relationship. For a point on the line, draw the two tangents... no, for a secant through a point, the involution pairs points that are conjugate with respect to the conic.

The involution on line PQ: P and Q are conjugate (since PQ is a secant, P and Q are on the circle, they're self-conjugate? No...). Hmm, let me think again.

Actually, the key theorem: Given a complete quadrilateral inscribed in a conic, the three pairs of opposite sides meet the three diagonal point lines in pairs of an involution.

Let me use a more direct approach. 

The involution on line PQ: Consider the conic (circle). For any point Z on line PQ, the polar of Z intersects PQ at Z', and (Z, Z') form an involution. This involution has the property that P and Q are a conjugate pair (since P, Q are on the conic, the polar of P passes through Q? No, the polar of P is the tangent at P, which doesn't pass through Q in general).

Hmm, let me reconsider. The involution on line l induced by conic: for point Z on l, take the two intersections of l with the conic's polar... Actually the standard involution: for a line l not tangent to the conic, the conic cuts l at two points (possibly complex). The involution on l is defined by: Z and Z' are conjugate iff the cross-ratio (Z, Z'; F, G) = -1 where F, G are the intersections of l with the conic. Wait no, that's the harmonic conjugate with respect to F, G.

Actually, the involution is: Z ↔ Z' where Z' is the harmonic conjugate of Z with respect to F and G (the two intersections of l with the conic). This is an involution with fixed points F, G.

For our line PQ, the conic intersects PQ at P and Q. So the involution on PQ is: Z ↔ Z' where (P, Q; Z, Z') = -1 (harmonic conjugate).

Now, the key theorem: If a complete quadrilateral is inscribed in a conic, and a line through one diagonal point meets the other two pairs of opposite sides, then the two intersection points are conjugate under the involution.

The complete quadrilateral ABCD has:
- Diagonal point 1: AB ∩ CD = M
- Diagonal point 2: AC ∩ BD
- Diagonal point 3: AD ∩ BC

The line PQ passes through M (diagonal point 1) and meets AD at X and BC at Y.

The theorem states: X and Y are conjugate under the involution on line PQ induced by the conic. Wait, but AD and BC are opposite sides (they don't share a vertex). The three pairs of opposite sides are: (AB, CD), (AC, BD), (AD, BC). Their intersections are the three diagonal points: M = AB∩CD, N = AC∩BD, L = AD∩BC.

So the line PQ passes through M and meets AD at X and BC at Y. But AD and BC are opposite sides meeting at L. The line PQ meets these two opposite sides at X and Y.

The theorem: A line through diagonal point M meets the pair of opposite sides (AD, BC) at X, Y, and X, Y are conjugate under the involution.

So (P, Q; X, Y) = -1, i.e., X and Y are harmonic conjugates with respect to P and Q.

Let me set up coordinates on line PQ. Let M be the origin. P is at -5 (since PM = 5, P on one side), Q is at +10 (since QM = 10, Q on the other side). Wait, need to check: M is between P and Q? PM = 5, QM = 10, PQ = 15 = 5 + 10, so yes M is between P and Q.

So on the line, let M = 0, P = -5, Q = +10.

X is on PQ with XM = 3. So X = +3 or X = -3.

The harmonic conjugate condition: (P, Q; X, Y) = -1.

Cross-ratio (P, Q; X, Y) = [(X-P)/(X-Q)] / [(Y-P)/(Y-Q)] = -1.

So (X-P)/(X-Q) = -(Y-P)/(Y-Q).

Let me compute. P = -5, Q = 10.

Case 1: X = 3.
(X-P)/(X-Q) = (3-(-5))/(3-10) = 8/(-7) = -8/7.

So -(Y-P)/(Y-Q) = -8/7, meaning (Y-P)/(Y-Q) = 8/7.

(Y+5)/(Y-10) = 8/7
7(Y+5) = 8(Y-10)
7Y + 35 = 8Y - 80
35 + 80 = 8Y - 7Y
Y = 115.

So Y = 115, YM = 115.

Hmm, that seems large. Let me check case 2.

Case 2: X = -3.
(X-P)/(X-Q) = (-3+5)/(-3-10) = 2/(-13) = -2/13.

-(Y-P)/(Y-Q) = -2/13, so (Y-P)/(Y-Q) = 2/13.

(Y+5)/(Y-10) = 2/13
13(Y+5) = 2(Y-10)
13Y + 65 = 2Y - 20
11Y = -85
Y = -85/11.

YM = 85/11.

Hmm, so two possible answers depending on which side X is on. But the problem says "If XM = 3, find YM" suggesting a unique answer.

Wait, I need to think about whether X can be on either side. Let me reconsider the problem. X is the intersection of AD and PQ. X could be on either side of M. But the problem gives XM = 3 as a specific value, and asks for YM. 

Actually, maybe I need to reconsider. The problem might have a unique answer regardless, or the configuration constrains X to one side.

Hmm, but actually, let me reconsider whether the involution theorem gives harmonic conjugacy with respect to P, Q, or with respect to something else.

Wait, actually I should double-check the theorem. Let me reconsider.

The involution on a line l cut by a conic at F, G: the involution pairs Z ↔ Z' where Z' is the harmonic conjugate of Z w.r.t. F, G. This is correct.

Now the theorem about complete quadrilaterals: If a complete quadrilateral is inscribed in a conic, the three pairs of opposite sides determine an involution on any line through a diagonal point. Specifically:

Consider the complete quadrilateral with vertices A, B, C, D on the conic. The three diagonal points are:
- M₁ = AB ∩ CD
- M₂ = AC ∩ BD  
- M₃ = AD ∩ BC

A line through M₁ meets the sides of the quadrilateral. The pairs of opposite sides are (AB, CD), (AC, BD), (AD, BC). The line through M₁ meets:
- AB at M₁ itself (and CD at M₁ itself) — so this pair gives the point M₁ twice
- AC at some point, BD at some point — these form a conjugate pair
- AD at X, BC at Y — these form a conjugate pair

And all these pairs belong to the same involution, which is the involution induced by the conic on the line.

Since the line passes through M₁ = AB ∩ CD, and M₁ is a double point of the involution restricted... Actually, the involution on the line through M₁: the pair (M₁, M₁) is one pair (from sides AB, CD both passing through M₁). The involution induced by the conic has the property that M₁ is paired with itself? That would mean M₁ is a fixed point.

The fixed points of the involution (harmonic conjugacy w.r.t. F, G) are F and G themselves (the intersections of the line with the conic). So M₁ being a fixed point means M₁ is on the conic, which it's not (M is inside the circle).

Hmm, I think I'm confusing things. Let me reconsider.

Actually, the involution determined by the complete quadrilateral on a line through a diagonal point is NOT the same as the involution induced by the conic. Let me re-derive.

Let me use the direct cross-ratio approach. 

Consider the four points A, B, C, D on the circle. Project from M (= AB ∩ CD) onto line PQ. The pencil of lines through M: MA = MB (same line, since A, B, M are collinear), MC = MD (same line). So projecting A, B, C, D from M onto PQ:
- A and B both project to M (since the line MA = MB meets PQ at M)
- C and D both project to M

That's degenerate. So projecting from M doesn't help directly.

Let me project from X instead. X is on AD and on PQ. Project A, B, C, D from X onto PQ:
- A projects to X (since XA = XD line meets PQ at X), and D also projects to X
- B projects to some point, C projects to some point

Hmm, this is getting complicated. Let me try a different approach.

Let me use coordinates and actually compute.

Set up: Circle of radius 10 centered at origin O = (0,0). Let PQ be along a line. Let me place PQ horizontally for simplicity.

The chord PQ has length 15. Let the midpoint of PQ be at (d, 0) where d = √(100 - 56.25) = √43.75 = √(175/4) = (5√7)/2.

Actually, let me place the chord PQ symmetrically. Let PQ be along the x-axis, with midpoint at (h, 0) where h = √(100 - (7.5)²) = √(100 - 56.25) = √43.75.

P = (h - 7.5, 0), Q = (h + 7.5, 0) where h = √43.75.

M is on PQ with PM = 5, so M = P + 5 in the direction of Q = (h - 7.5 + 5, 0) = (h - 2.5, 0).

Check: QM = Q - M = (h + 7.5) - (h - 2.5) = 10. ✓

Now, M = (h - 2.5, 0) where h = √43.75 = 5√7/2 ≈ 6.614.

So M ≈ (4.114, 0).

Now, AB is a chord through M, CD is another chord through M. 

Let me parametrize. A chord through M = (m, 0) with direction angle θ: the line is (m + t cosθ, t sinθ). This intersects the circle x² + y² = 100 at two points. 

(m + t cosθ)² + (t sinθ)² = 100
m² + 2mt cosθ + t² = 100
t² + 2m cosθ · t + (m² - 100) = 0

The two solutions t₁, t₂ satisfy t₁ + t₂ = -2m cosθ, t₁ t₂ = m² - 100 = 50 - 100 = -50 (since m² = (h-2.5)² = h² - 5h + 6.25 = 43.75 - 5·(5√7/2) + 6.25 = 50 - 5√7·(5/2)... 

wait let me recompute. h = 5√7/2, h² = 25·7/4 = 175/4 = 43.75. m = h - 2.5 = 5√7/2 - 5/2 = (5√7 - 5)/2 = 5(√7 - 1)/2.

m² = 25(√7-1)²/4 = 25(7 - 2√7 + 1)/4 = 25(8 - 2√7)/4 = 25(4 - √7)/2.

So m² - 100 = 25(4 - √7)/2 - 100 = (25(4-√7) - 200)/2 = (100 - 25√7 - 200)/2 = (-100 - 25√7)/2.

Hmm, that's not -50. Let me recheck.

Oh wait, I think I made an error. The power of M should be OM² - R². OM = distance from origin to M = |m| = m (assuming m > 0). 

OM² = m² = 25(4-√7)/2 ≈ 25(4-2.646)/2 = 25(1.354)/2 ≈ 16.92. So OM ≈ 4.11. And power = 16.92 - 100 = -83.08. But earlier I computed OM = √50 ≈ 7.07. Contradiction!

Let me recheck. I think I placed the chord wrong. The distance from center to chord is h, and M is at distance from the midpoint of 2.5. So OM² = h² + 2.5² = 43.75 + 6.25 = 50. OM = √50. ✓

But in my coordinate system, M = (h - 2.5, 0) and O = (0,0), so OM = |h - 2.5| = |√43.75 - 2.5| ≈ |6.614 - 2.5| = 4.114. That gives OM² ≈ 16.9, not 50!

The issue is that I placed the chord along the x-axis passing through (h, 0), but the center is at origin. The distance from O to the chord (which is the x-axis, y=0) is 0, not h! 

I need to place the chord at distance h from the center. Let me redo.

Let the chord PQ be on the line y = h (where h = √43.75 is the distance from center to chord). Then:
P = (-7.5, h), Q = (7.5, h).

M is on PQ with PM = 5: M = P + (5, 0) = (-7.5 + 5, h) = (-2.5, h).

Check QM = |Q - M| = |(7.5 - (-2.5), 0)| = |10| = 10. ✓

OM = √((-2.5)² + h²) = √(6.25 + 43.75) = √50. ✓

Power of M = OM² - R² = 50 - 100 = -50. So MA·MB = MC·MD = 50. ✓

Now, let me parametrize chords through M = (-2.5, h) where h = 5√7/2.

A chord through M with direction (cosθ, sinθ): point = M + t(cosθ, sinθ) = (-2.5 + t cosθ, h + t sinθ).

On circle: (-2.5 + t cosθ)² + (h + t sinθ)² = 100
6.25 - 5t cosθ + t² cos²θ + h² + 2ht sinθ + t² sin²θ = 100
t² + t(-5 cosθ + 2h sinθ) + (6.25 + h² - 100) = 0
t² + t(-5 cosθ + 2h sinθ) + (6.25 + 43.75 - 100) = 0
t² + t(-5 cosθ + 2h sinθ) - 50 = 0

So t₁ t₂ = -50, meaning the product of signed distances from M to the two intersection points is -50 (one positive, one negative, as expected for M inside the circle). |MA|·|MB| = 50. ✓

Now let me set up the two chords. 

Chord AB through M with angle α: A = M + t_A (cosα, sinα), B = M + t_B (cosα, sinα), where t_A, t_B are roots of t² + t(-5cosα + 2h sinα) - 50 = 0.

Chord CD through M with angle β: C = M + s_C (cosβ, sinβ), D = M + s_D (cosβ, sinβ), where s_C, s_D are roots of t² + t(-5cosβ + 2h sinβ) - 50 = 0.

Now I need to find X = AD ∩ PQ and Y = BC ∩ PQ, where PQ is the line y = h.

Since PQ is the horizontal line y = h, and M = (-2.5, h) is on PQ, any point on PQ has the form (x, h). The distance from M to a point (x, h) on PQ is |x - (-2.5)| = |x + 2.5|.

So XM = |x_X + 2.5| and YM = |x_Y + 2.5|.

Let me find X = AD ∩ {y = h}.

A = (-2.5 + t_A cosα, h + t_A sinα)
D = (-2.5 + s_D cosβ, h + s_D sinβ)

Line AD: parametrize as A + λ(D - A).
y-coordinate: h + t_A sinα + λ(s_D sinβ - t_A sinα) = h
=> t_A sinα + λ(s_D sinβ - t_A sinα) = 0
=> λ = -t_A sinα / (s_D sinβ - t_A sinα) = t_A sinα / (t_A sinα - s_D sinβ)

x-coordinate of X: x_X = -2.5 + t_A cosα + λ(s_D cosβ - t_A cosα)

This is getting messy. Let me try a different approach—use the cross-ratio/involution theorem more carefully, or use projective coordinates.

Actually, let me revisit the involution theorem. I think the correct statement is:

**Theorem**: Let A, B, C, D be four points on a conic. Let M = AB ∩ CD. A line l through M meets AD at X and BC at Y. Then X and Y are conjugate under the involution on l induced by the conic (i.e., the involution whose fixed points are the intersections of l with the conic).

But wait, in our case l = PQ, and the intersections of l with the conic are P and Q. So the involution on PQ is the harmonic conjugation w.r.t. P, Q. And X, Y are conjugate, meaning (P, Q; X, Y) = -1.

But I got two different answers (115 or 85/11) depending on which side X is. Let me re-examine.

Actually, wait. I need to be more careful. The involution on line l induced by the conic: for a point Z on l, Z' is defined such that the polar of Z passes through Z' (equivalently, the polar of Z' passes through Z). For a line l meeting the conic at F, G, this involution is the one with fixed points F, G, which is the harmonic conjugation w.r.t. F, G.

But actually, is the involution the harmonic conjugation, or is it something else? Let me think...

The involution on l induced by the conic: Z ↔ Z' where Z' is the intersection of l with the polar of Z. For Z on the conic (Z = F or G), the polar of Z is the tangent at Z, which meets l at Z itself (since Z is on l). So F and G are fixed points. The involution with fixed points F, G is indeed the harmonic conjugation w.r.t. F, G. ✓

So (P, Q; X, Y) = -1 should hold. Let me re-examine whether both cases are valid or if the geometry constrains X to one side.

Actually, the problem says "If XM = 3, then find YM." This suggests a unique answer. But I got two possibilities. Let me reconsider.

Hmm, maybe the issue is that X and Y are determined by the configuration, and XM = 3 is given. But different configurations (different choices of chords AB, CD) could give different X positions. The problem asserts that XM = 3 and asks for YM, implying YM is determined regardless of the specific configuration.

But from the harmonic conjugate relation, YM depends on which side X is on. Unless... the problem intends a specific configuration, or there's an additional constraint I'm missing.

Wait, actually, let me reconsider. Maybe the theorem gives a different relation. Let me re-derive from scratch using cross-ratios.

Let me use the cross-ratio of four points on the conic. The cross-ratio (A, B; C, D) on the conic can be computed by projecting from any point on the conic onto any line.

Project A, B, C, D from M onto line PQ. But M = AB ∩ CD, so the projection from M sends A, B to the same point (M itself on PQ) and C, D to the same point (M itself). This is degenerate.

Let me project from X instead. X is on AD and on PQ. Project from X onto PQ:
- A → X (since X, A, D are collinear, A projects to X on PQ... wait, A projects to the intersection of line XA with PQ. Since X is on PQ and X is on line AD, line XA = line XD = line AD, which meets PQ at X. So A → X.
- D → X (same reasoning)
- B → intersection of XB with PQ = some point, call it B'
- C → intersection of XC with PQ = some point, call it C'

So (A, B; C, D) on conic = (X, B'; X, C') on PQ... but A and D both project to X, so this is degenerate too (X appears twice).

Hmm. Let me try projecting from a point on the conic, say A.

Project B, C, D from A onto PQ:
- B → intersection of AB with PQ = M (since AB passes through M which is on PQ)
- C → intersection of AC with PQ = some point, call it C'
- D → intersection of AD with PQ = X (since AD passes through X which is on PQ)

So (A, B; C, D) = (∞, M; C', X) where ∞ is the projection of A from A (which goes to infinity / is undefined). Actually, when projecting from A, the point A itself projects to infinity (or is undefined). The cross-ratio (A, B; C, D) projected from A gives (∞, M; C', X) = (M - C')/(M - X) ... using the convention that when one point is at infinity, the cross-ratio simplifies.

Actually, (∞, M; C', X) = (C' - X)/(M - X) ... let me be careful. Cross-ratio (P₁, P₂; P₃, P₄) = [(P₃-P₁)/(P₃-P₂)] / [(P₄-P₁)/(P₄-P₂)]. With P₁ = ∞:
(∞, M; C', X) = [(C'-∞)/(C'-M)] / [(X-∞)/(X-M)] = [1/(C'-M)] / [1/(X-M)] = (X-M)/(C'-M).

Hmm wait, let me use the standard formula. (P₁, P₂; P₃, P₄) with P₁ = ∞:
= lim_{P₁→∞} [(P₃-P₁)(P₄-P₂)] / [(P₃-P₂)(P₄-P₁)]
= lim [(P₃-P₁)/(P₄-P₁)] · [(P₄-P₂)/(P₃-P₂)]
= 1 · (P₄-P₂)/(P₃-P₂)
= (P₄ - P₂)/(P₃ - P₂)

So (∞, M; C', X) = (X - M)/(C' - M).

Similarly, project from B: (A, B; C, D) projected from B gives (A', ∞; C'', D') where A' = AB ∩ PQ = M, C'' = BC ∩ PQ = Y, D' = BD ∩ PQ = some point.

(A, B; C, D) = (M, ∞; Y, D') = (using P₂ = ∞) (M - D')/(M - Y) ... 

Hmm, this is getting complicated. Let me try yet another approach.

Let me use the fact that (A, B; C, D) is the same when computed from different projections.

From A: (A,B;C,D) = (X - M)/(C' - M) where C' = AC ∩ PQ.
From B: (A,B;C,D) = (M - D')/(M - Y) where D' = BD ∩ PQ, Y = BC ∩ PQ.

Hmm, I still have unknowns C' and D'.

Let me try from C and D.

From C: project A, B, D from C onto PQ.
- A → CA ∩ PQ = C' (same as before)
- B → CB ∩ PQ = Y
- D → CD ∩ PQ = M

(A, B; C, D) projected from C: (C', Y; ∞, M) where ∞ is C's projection.
(C', Y; ∞, M) with P₃ = ∞: = (P₁ - P₄)/(P₂ - P₄) = (C' - M)/(Y - M).

Wait, let me redo. (P₁, P₂; P₃, P₄) with P₃ = ∞:
= [(∞-P₁)(P₄-P₂)] / [(∞-P₂)(P₄-P₁)] = (P₄-P₂)/(P₄-P₁) = (M - Y)/(M - C').

From D: project A, B, C from D onto PQ.
- A → DA ∩ PQ = X
- B → DB ∩ PQ = D'
- C → DC ∩ PQ = M

(A, B; C, D) projected from D: (X, D'; M, ∞) with P₄ = ∞:
= [(M-P₁)(∞-P₂)] / [(M-P₂)(∞-P₁)] = (M-P₁)/(M-P₂) = (M - X)/(M - D').

So we have:
From A: (A,B;C,D) = (X - M)/(C' - M) ... (i)
From C: (A,B;C,D) = (M - Y)/(M - C') ... (ii)
From D: (A,B;C,D) = (M - X)/(M - D') ... (iii)
From B: (A,B;C,D) = (M - D')/(M - Y) ... (iv) [let me verify this]

From B: project A, C, D from B onto PQ.
- A → BA ∩ PQ = M
- C → BC ∩ PQ = Y
- D → BD ∩ PQ = D'

(A, B; C, D) projected from B: (M, ∞; Y, D') with P₂ = ∞:
= [(Y - M)(D' - ∞)] / [(Y - ∞)(D' - M)] = (Y - M)/(D' - M) = -(Y - M)/(M - D') = (M - Y)/(M - D')... 

wait: (Y - M)/(D' - M). Let me just compute directly.
(P₁, P₂; P₃, P₄) = [(P₃-P₁)(P₄-P₂)]/[(P₃-P₂)(P₄-P₁)]
(M, ∞; Y, D') = [(Y-M)(D'-∞)]/[(Y-∞)(D'-M)] = (Y-M)/(D'-M) [the ∞ terms cancel]

So from B: (A,B;C,D) = (Y - M)/(D' - M) ... (iv)

Now from (i) and (ii):
(X - M)/(C' - M) = (M - Y)/(M - C') = -(M - Y)/(C' - M) = (Y - M)/(C' - M)

So (X - M)/(C' - M) = (Y - M)/(C' - M), which gives X - M = Y - M, i.e., X = Y. That can't be right in general...

I think I'm making errors with the cross-ratio conventions. Let me be very careful.

Cross-ratio (A, B; C, D) = [AC/BC] / [AD/BD] where these are signed ratios. In terms of coordinates on a line: (A,B;C,D) = [(C-A)/(C-B)] / [(D-A)/(D-B)] = (C-A)(D-B) / [(C-B)(D-A)].

On the conic, the cross-ratio of four points is defined via projection onto any line from any point on the conic.

Let me redo. Project from A (on conic) onto line PQ. The four points A, B, C, D project to:
- A → ∞ (point at infinity on PQ, since projecting from A, A goes to infinity)
- B → M (AB meets PQ at M)
- C → C' = AC ∩ PQ
- D → X = AD ∩ PQ

Cross-ratio (A, B; C, D) = (∞, M; C', X) = [(C'-∞)(X-M)] / [(C'-M)(X-∞)]

As P₁ → ∞: (C'-P₁)(X-M) / [(C'-M)(X-P₁)] → (X-M)/(C'-M) · lim[(C'-P₁)/(X-P₁)] = (X-M)/(C'-M) · 1 = (X-M)/(C'-M).

Wait, lim_{P₁→∞} (C'-P₁)/(X-P₁) = 1. So (∞, M; C', X) = (X-M)/(C'-M). Hmm, but let me double-check with the formula.

(A,B;C,D) = (C-A)(D-B)/[(C-B)(D-A)]

(∞, M; C', X) = (C'-∞)(X-M)/[(C'-M)(X-∞)] 

As the ∞ terms: (C'-∞)/(X-∞) → 1. So = (X-M)/(C'-M).

OK so (A,B;C,D) = (X-M)/(C'-M). ... (i)

Project from C (on conic) onto PQ:
- C → ∞
- A → C' = AC ∩ PQ
- B → Y = BC ∩ PQ
- D → M = CD ∩ PQ

(A,B;C,D) = (C', Y; ∞, M) = (∞-C')(M-Y)/[(∞-Y)(M-C')]

(∞-C')/(∞-Y) → 1. So = (M-Y)/(M-C'). ... (ii)

From (i) and (ii): (X-M)/(C'-M) = (M-Y)/(M-C').

Note C'-M = -(M-C'), so (X-M)/(C'-M) = -(X-M)/(M-C').

So -(X-M)/(M-C') = (M-Y)/(M-C'), giving -(X-M) = M-Y, so Y-M = X-M, so Y = X.

That's clearly wrong. I must be making an error in the cross-ratio formula or the projection.

Let me reconsider. The cross-ratio of four points on a conic is defined as follows: pick any point S on the conic, and project the four points from S onto any line. The cross-ratio of the four projected points is independent of S and the line. But when S is one of the four points, it projects to infinity.

Actually, I think the issue is that the cross-ratio (A, B; C, D) on the conic, when projected from A, gives the cross-ratio of the pencil of lines (AB, AC, AD) — but that's only three lines. The fourth "line" is the tangent at A, or we use the point at infinity.

Hmm, actually, the cross-ratio of four points on a conic is defined as the cross-ratio of the pencil of four lines from any fifth point on the conic. If we project from one of the four points, we get a degenerate situation.

Let me use a fifth point. Actually, this is getting too complicated. Let me just go with the coordinate computation.

Let me use a cleaner coordinate system. Let me place M at the origin and PQ along the x-axis.

M = (0, 0). P = (-5, 0), Q = (10, 0).

The circle passes through P and Q and has radius 10. Center O = (a, b) with:
(a+5)² + b² = 100 ... (P on circle)
(a-10)² + b² = 100 ... (Q on circle)

Subtracting: (a+5)² - (a-10)² = 0 => (a+5+a-10)(a+5-a+10) = 0 => (2a-5)(15) = 0 => a = 5/2.

So a = 5/2. Then (5/2 + 5)² + b² = 100 => (15/2)² + b² = 100 => 225/4 + b² = 100 => b² = 175/4 => b = ±5√7/2.

Let's take b = 5√7/2 (circle above the x-axis, but it doesn't matter). Center O = (5/2, 5√7/2).

Check: OM = √((5/2)² + (5√7/2)²) = √(25/4 + 175/4) = √(200/4) = √50. Power = 50 - 100 = -50. ✓

Now, a chord through M = (0,0) with direction (cosθ, sinθ): parametrized as (t cosθ, t sinθ).

On circle: (t cosθ - 5/2)² + (t sinθ - 5√7/2)² = 100
t² - 5t cosθ - 5√7 t sinθ + 25/4 + 175/4 = 100
t² - t(5 cosθ + 5√7 sinθ) + 50 = 100
t² - 5t(cosθ + √7 sinθ) - 50 = 0

Let me denote c = cosθ + √7 sinθ. Then t² - 5ct - 50 = 0, so t = [5c ± √(25c² + 200)]/2.

The two roots t₁, t₂ satisfy t₁ + t₂ = 5c, t₁ t₂ = -50.

For chord AB with angle α: A = (t₁ cosα, t₁ sinα), B = (t₂ cosα, t₂ sinα) where t₁ + t₂ = 5(cosα + √7 sinα), t₁ t₂ = -50.

For chord CD with angle β: C = (s₁ cosβ, s₁ sinβ), D = (s₂ cosβ, s₂ sinβ) where s₁ + s₂ = 5(cosβ + √7 sinβ), s₁ s₂ = -50.

Now, X = AD ∩ x-axis (y = 0), Y = BC ∩ x-axis.

Let me find X. Line through A = (t₁ cosα, t₁ sinα) and D = (s₂ cosβ, s₂ sinβ).

Parametrize: (1-λ)A + λD. y-coordinate: (1-λ) t₁ sinα + λ s₂ sinβ = 0.
λ = t₁ sinα / (t₁ sinα - s₂ sinβ).

x-coordinate: x_X = (1-λ) t₁ cosα + λ s₂ cosβ = [t₁ cosα (t₁ sinα - s₂ sinβ) + s₂ cosβ · t₁ sinα] / (t₁ sinα - s₂ sinβ) · ... 

let me redo: x_X = (1-λ) t₁ cosα + λ s₂ cosβ where λ = t₁ sinα / (t₁ sinα - s₂ sinβ).

1 - λ = (t₁ sinα - s₂ sinβ - t₁ sinα) / (t₁ sinα - s₂ sinβ) = -s₂ sinβ / (t₁ sinα - s₂ sinβ).

x_X = [-s₂ sinβ · t₁ cosα + t₁ sinα · s₂ cosβ] / (t₁ sinα - s₂ sinβ)
= [t₁ s₂ (sinα cosβ - cosα sinβ)] / (t₁ sinα - s₂ sinβ)
= [t₁ s₂ sin(α - β)] / (t₁ sinα - s₂ sinβ)

Similarly, Y = BC ∩ x-axis. B = (t₂ cosα, t₂ sinα), C = (s₁ cosβ, s₁ sinβ).

x_Y = [t₂ s₁ sin(α - β)] / (t₂ sinα - s₁ sinβ)

Now, XM = |x_X| (since M is at origin), YM = |x_Y|.

We're given XM = 3, so |x_X| = 3, i.e., x_X = ±3.

We need to find YM = |x_Y|.

Let me denote:
x_X = t₁ s₂ sin(α-β) / (t₁ sinα - s₂ sinβ) ... (*)
x_Y = t₂ s₁ sin(α-β) / (t₂ sinα - s₁ sinβ) ... (**)

We know:
t₁ t₂ = -50, s₁ s₂ = -50.
t₁ + t₂ = 5(cosα + √7 sinα), s₁ + s₂ = 5(cosβ + √7 sinβ).

This is quite complex. Let me see if there's a relation between x_X and x_Y.

Let me compute x_X · x_Y:

x_X · x_Y = [t₁ s₂ sin(α-β) · t₂ s₁ sin(α-β)] / [(t₁ sinα - s₂ sinβ)(t₂ sinα - s₁ sinβ)]
= [t₁ t₂ s₁ s₂ sin²(α-β)] / [(t₁ sinα - s₂ sinβ)(t₂ sinα - s₁ sinβ)]
= [(-50)(-50) sin²(α-β)] / [t₁ t₂ sin²α - t₁ s₁ sinα sinβ - s₂ t₂ sinα sinβ + s₁ s₂ sin²β]
= [2500 sin²(α-β)] / [-50 sin²α - (t₁ s₁ + s₂ t₂) sinα sinβ - 50 sin²β]

Hmm, this has the cross term (t₁ s₁ + s₂ t₂) which I don't know.

Let me try a different approach. Let me compute x_X + x_Y or some other combination.

Actually, let me try to use the involution theorem but verify it with coordinates. Let me pick specific angles and compute.

Let me try α = π/2 (vertical chord) and some β.

α = π/2: cosα = 0, sinα = 1. c_α = 0 + √7 = √7. t² - 5√7 t - 50 = 0. t = [5√7 ± √(175 + 200)]/2 = [5√7 ± √375]/2 = [5√7 ± 5√15]/2.

t₁ = 5(√7 + √15)/2, t₂ = 5(√7 - √15)/2. (Note √15 > √7, so t₂ < 0.)

A = (0, t₁) = (0, 5(√7+√15)/2), B = (0, t₂) = (0, 5(√7-√15)/2).

Let me try β = 0 (horizontal chord). cosβ = 1, sinβ = 0. c_β = 1. s² - 5s - 50 = 0. s = [5 ± √(25+200)]/2 = [5 ± 15]/2. s₁ = 10, s₂ = -5.

C = (10, 0), D = (-5, 0). But wait, C = (10, 0) = Q and D = (-5, 0) = P! So the chord CD is just PQ itself. That's a degenerate case. Let me pick a different β.

Let me try β = π/4. cosβ = sinβ = 1/√2. c_β = (1 + √7)/√2. s² - 5(1+√7)/√2 · s - 50 = 0.

This is getting messy numerically. Let me just use numerical computation.

Let me use α = π/2 (as above) and β = π/6.

α = π/2: t₁ = 5(√7+√15)/2 ≈ 5(2.6458+3.8730)/2 ≈ 5(6.5188)/2 ≈ 16.297, t₂ = 5(√7-√15)/2 ≈ 5(-1.2272)/2 ≈ -3.068.

β = π/6: cosβ = √3/2, sinβ = 1/2. c_β = √3/2 + √7/2 = (√3+√7)/2 ≈ (1.7321+2.6458)/2 ≈ 2.1889.
s² - 5(2.1889)s - 50 = 0 => s = [10.9445 ± √(119.78 + 200)]/2 = [10.9445 ± √319.78]/2 = [10.9445 ± 17.882]/2.
s₁ ≈ 14.413, s₂ ≈ -3.469.

A = (0, 16.297), B = (0, -3.068).
C = (14.413 · √3/2, 14.413 · 1/2) = (12.482, 7.207).
D = (-3.469 · √3/2, -3.469 · 1/2) = (-3.004, -1.735).

X = AD ∩ x-axis:
A = (0, 16.297), D = (-3.004, -1.735).
Line AD: y = 0 at λ where (1-λ)·16.297 + λ·(-1.735) = 0 => 16.297 - 18.032λ = 0 => λ = 0.9038.
x_X = (1-0.9038)·0 + 0.9038·(-3.004) = -2.715.

So x_X ≈ -2.715, XM ≈ 2.715.

Y = BC ∩ x-axis:
B = (0, -3.068), C = (12.482, 7.207).
y = 0 at λ where (1-λ)·(-3.068) + λ·7.207 = 0 => -3.068 + 10.275λ = 0 => λ = 0.2986.
x_Y = (1-0.2986)·0 + 0.2986·12.482 = 3.727.

So x_Y ≈ 3.727, YM ≈ 3.727.

Let me check the harmonic conjugate: (P, Q; X, Y) = -1?
P = -5, Q = 10, X = -2.715, Y = 3.727.

(P,Q;X,Y) = (X-P)(Y-Q)/[(X-Q)(Y-P)] = (-2.715+5)(3.727-10)/[(-2.715-10)(3.727+5)]
= (2.285)(-6.273)/[(-12.715)(8.727)]
= (-14.334)/(-110.95)
= 0.1292.

That's not -1. So the harmonic conjugate theorem doesn't apply directly. My earlier analysis was wrong.

Let me check if maybe it's a different involution. Let me compute x_X · x_Y:
(-2.715)(3.727) = -10.12. Hmm, not obviously -50 or anything nice.

Let me try another configuration to see if there's a pattern. Let me try α = π/3, β = 2π/3.

α = π/3: cosα = 1/2, sinα = √3/2. c_α = 1/2 + √7·√3/2 = (1 + √21)/2 ≈ (1+4.5826)/2 ≈ 2.7913.
t² - 5(2.7913)t - 50 = 0 => t = [13.9565 ± √(194.78+200)]/2 = [13.9565 ± 19.886]/2.
t₁ ≈ 16.921, t₂ ≈ -2.965.

A = (16.921·0.5, 16.921·0.866) = (8.461, 14.650).
B = (-2.965·0.5, -2.965·0.866) = (-1.483, -2.568).

β = 2π/3: cosβ = -1/2, sinβ = √3/2. c_β = -1/2 + √21/2 = (√21-1)/2 ≈ 1.7913.
s² - 5(1.7913)s - 50 = 0 => s = [8.9565 ± √(80.22+200)]/2 = [8.9565 ± 16.740]/2.
s₁ ≈ 12.848, s₂ ≈ -3.892.

C = (12.848·(-0.5), 12.848·0.866) = (-6.424, 11.126).
D = (-3.892·(-0.5), -3.892·0.866) = (1.946, -3.370).

X = AD ∩ x-axis:
A = (8.461, 14.650), D = (1.946, -3.370).
y=0: (1-λ)·14.650 + λ·(-3.370) = 0 => 14.650 - 18.020λ = 0 => λ = 0.8130.
x_X = (1-0.8130)·8.461 + 0.8130·1.946 = 1.583 + 1.582 = 3.165.

Y = BC ∩ x-axis:
B = (-1.483, -2.568), C = (-6.424, 11.126).
y=0: (1-λ)·(-2.568) + λ·11.126 = 0 => -2.568 + 13.694λ = 0 => λ = 0.1875.
x_Y = (1-0.1875)·(-1.483) + 0.1875·(-6.424) = -1.205 - 1.205 = -2.410.

So x_X ≈ 3.165, x_Y ≈ -2.410.

x_X · x_Y = 3.165 · (-2.410) = -7.627.

Hmm, different from before (-10.12). So x_X · x_Y is not constant. Let me check other relations.

In the first example: x_X = -2.715, x_Y = 3.727. x_X + x_Y = 1.012.
In the second: x_X = 3.165, x_Y = -2.410. x_X + x_Y = 0.755.

Not constant either. Let me check 1/x_X + 1/x_Y:
First: 1/(-2.715) + 1/3.727 = -0.3683 + 0.2683 = -0.1000.
Second: 1/3.165 + 1/(-2.410) = 0.3160 - 0.4149 = -0.0989.

Oh interesting! 1/x_X + 1/x_Y ≈ -0.1 in both cases! That's -1/10.

So 1/x_X + 1/x_Y = -1/10, or equivalently (x_X + x_Y)/(x_X · x_Y) = -1/10.

Let me verify more carefully with the first example:
1/(-2.715) + 1/3.727 = -0.36832 + 0.26831 = -0.10001. Yes!

Second: 1/3.165 + 1/(-2.410) = 0.31596 - 0.41494 = -0.09898. Close to -0.1 (rounding errors).

So the relation is: 1/x_X + 1/x_Y = -1/10.

This means: (x_X + x_Y) / (x_X · x_Y) = -1/10, i.e., 10(x_X + x_Y) + x_X · x_Y = 0.

Or: x_X · x_Y + 10 x_X + 10 x_Y = 0, i.e., (x_X + 10)(x_Y + 10) = 100.

Interesting! So (x_X + 10)(x_Y + 10) = 100.

Recall Q = (10, 0), so x_Q = 10. And M = (0,0). So x_X + 10 is the x-coordinate of X relative to Q... actually x_X + 10 = x_X - x_Q + 2·x_Q... no. x_X + 10 is just x_X + 10.

Hmm, let me think in terms of distances. Q is at x = 10. So x_X + 10 = x_X - (-10)... not directly a distance to a notable point.

Wait, actually, let me reconsider. P = (-5, 0), Q = (10, 0). 

(x_X + 10)(x_Y + 10) = 100. Note x + 10 = x - (-10). The point at x = -10 is at distance 5 from P (since P = -5) and distance 20 from Q. Hmm, not obviously meaningful.

Alternatively, let me rewrite. x_X + 10 = x_X - x_Q + 2·10... no. Let me think of it as: the point R at x = -10 is such that... Actually, let me check if it's related to the power of a point or something.

Actually, (x_X + 10)(x_Y + 10) = 100 = R². And x = -10 is the point that is the reflection of Q = 10 about M = 0? No, that would be x = -10, which is the reflection of Q = 10 about M = 0. Yes! The reflection of Q about M is at x = -10.

Hmm, or maybe it's better to think of it as: Let Q' be the point on PQ such that MQ' = MQ = 10 but on the opposite side, so Q' = (-10, 0). Then Q'X · Q'Y = 100 = R².

Actually, Q' = (-10, 0). Q'X = |x_X - (-10)| = |x_X + 10|, Q'Y = |x_Y + (-10)| = |x_Y + 10|. And (x_X+10)(x_Y+10) = 100 (with appropriate signs).

Hmm, but why would Q' be special? Let me check if there's a relation with P instead.

P = (-5, 0). (x_X + 5)(x_Y + 5) = ?
First example: (-2.715+5)(3.727+5) = (2.285)(8.727) = 19.94 ≈ 20.
Second: (3.165+5)(-2.410+5) = (8.165)(2.590) = 21.15. Not 20.

So not constant with P. Let me check (x_X - 10)(x_Y - 10):
First: (-2.715-10)(3.727-10) = (-12.715)(-6.273) = 79.77. Not obviously nice.
Second: (3.165-10)(-2.410-10) = (-6.835)(-12.410) = 84.89. Not constant.

So the relation is specifically (x_X + 10)(x_Y + 10) = 100.

Let me also check: is the relation perhaps 1/x_X + 1/x_Y = constant related to the power? Power = -50, and -1/10... -50/(-1/10) = 500. Hmm, or -1/10 = -50/500. Not obvious.

Actually, wait. Let me reconsider. 1/x_X + 1/x_Y = -1/10. Let me check if this is -2/(t₁+t₂ + s₁+s₂) or something... no, that depends on the angles.

Actually, let me think about what -10 means. The point at x = -10 is the reflection of Q (at x=10) through M (at x=0). Let me call this Q*. 

Alternatively, note that the power of M is -50, and PM·QM = 5·10 = 50. The relation 1/x_X + 1/x_Y = -1/10 can be written as:

1/x_X + 1/x_Y = -1/QM (since QM = 10 and Q is at x = +10, so this is -1/x_Q).

Or equivalently: 1/x_X + 1/x_Y = 1/x_P + 1/x_Q? Let me check: 1/(-5) + 1/10 = -1/5 + 1/10 = -2/10 + 1/10 = -1/10. Yes!!

So 1/x_X + 1/x_Y = 1/x_P + 1/x_Q = 1/(-5) + 1/10 = -1/10.

This is a beautiful relation! The harmonic mean-type relation.

So the relation is: 1/XM_signed + 1/YM_signed = 1/PM_signed + 1/QM_signed.

Where signed distances are from M along PQ. With M at origin: 1/x_X + 1/x_Y = 1/(-5) + 1/10 = -1/10.

Now, given XM = 3, so |x_X| = 3, x_X = ±3.

Case 1: x_X = 3.
1/3 + 1/x_Y = -1/10
1/x_Y = -1/10 - 1/3 = -3/30 - 10/30 = -13/30
x_Y = -30/13.
YM = |x_Y| = 30/13.

Case 2: x_X = -3.
1/(-3) + 1/x_Y = -1/10
1/x_Y = -1/10 + 1/3 = -3/30 + 10/30 = 7/30
x_Y = 30/7.
YM = |x_Y| = 30/7.

So YM = 30/13 or 30/7. Two possible answers. Hmm.

The problem says "If XM = 3, then find YM", suggesting a unique answer. Let me think about whether the configuration constrains X to one side.

Actually, wait. Let me reconsider the problem. The problem says "chords AB and CD intersect at M". It doesn't specify the order of points. But X = AD ∩ PQ and Y = BC ∩ PQ. Depending on the labeling, X could be on either side.

But actually, in competition problems, usually the answer is unique. Let me reconsider whether both cases are actually achievable, or if one is excluded.

Hmm, but actually, the problem might have a unique answer if we consider that the labeling of A, B, C, D matters. If we swap A and B (or C and D), then X and Y swap (roughly). So the problem might be asking for a specific configuration.

Actually wait, let me reconsider. If we swap A↔B, then X = AD∩PQ becomes BD∩PQ and Y = BC∩PQ becomes AC∩PQ. That's different. If we swap C↔D, then X = AD∩PQ becomes AC∩PQ and Y = BC∩PQ becomes BD∩PQ. So swapping changes X and Y.

But the problem fixes X = AD∩PQ and Y = BC∩PQ with specific A, B, C, D. The question is: for a given XM = 3, is YM determined?

From the relation 1/x_X + 1/x_Y = -1/10, if x_X = 3 then x_Y = -30/13, and if x_X = -3 then x_Y = 30/7. These give different YM values. So YM is not uniquely determined by XM = 3 alone, unless there's an additional constraint.

But wait—maybe I need to verify the relation more carefully. Let me re-derive it analytically.

Let me go back to the formulas:
x_X = t₁ s₂ sin(α-β) / (t₁ sinα - s₂ sinβ) ... (*)
x_Y = t₂ s₁ sin(α-β) / (t₂ sinα - s₁ sinβ) ... (**)

1/x_X = (t₁ sinα - s₂ sinβ) / (t₁ s₂ sin(α-β))
1/x_Y = (t₂ sinα - s₁ sinβ) / (t₂ s₁ sin(α-β))

1/x_X + 1/x_Y = [(t₁ sinα - s₂ sinβ) t₂ s₁ + (t₂ sinα - s₁ sinβ) t₁ s₂] / [t₁ t₂ s₁ s₂ sin(α-β)]

Numerator: t₂ s₁ t₁ sinα - t₂ s₁ s₂ sinβ + t₁ s₂ t₂ sinα - t₁ s₂ s₁ sinβ
= t₁ t₂ sinα (s₁ + s₂) - s₁ s₂ sinβ (t₂ + t₁)
= t₁ t₂ (s₁ + s₂) sinα - s₁ s₂ (t₁ + t₂) sinβ

Denominator: t₁ t₂ s₁ s₂ sin(α-β) = (-50)(-50) sin(α-β) = 2500 sin(α-β).

So 1/x_X + 1/x_Y = [t₁ t₂ (s₁+s₂) sinα - s₁ s₂ (t₁+t₂) sinβ] / [2500 sin(α-β)]

Now, t₁ t₂ = -50, s₁ s₂ = -50, t₁+t₂ = 5(cosα + √7 sinα), s₁+s₂ = 5(cosβ + √7 sinβ).

Numerator = (-50) · 5(cosβ + √7 sinβ) · sinα - (-50) · 5(cosα + √7 sinα) · sinβ
= -250(cosβ + √7 sinβ) sinα + 250(cosα + √7 sinα) sinβ
= 250[-(cosβ + √7 sinβ) sinα + (cosα + √7 sinα) sinβ]
= 250[-cosβ sinα - √7 sinβ sinα + cosα sinβ + √7 sinα sinβ]
= 250[-cosβ sinα + cosα sinβ]
= 250[-(sinα cosβ - cosα sinβ)]
= 250[-sin(α-β)]
= -250 sin(α-β)

So 1/x_X + 1/x_Y = -250 sin(α-β) / [2500 sin(α-β)] = -250/2500 = -1/10.

The relation is proven: 1/x_X + 1/x_Y = -1/10, regardless of the angles α and β.

Now, -1/10 = 1/(-5) + 1/10 = 1/x_P + 1/x_Q where P = -5, Q = 10.

So the relation is: 1/x_X + 1/x_Y = 1/x_P + 1/x_Q.

This is a general relation for this configuration. Now, with XM = 3 (|x_X| = 3):

If x_X = 3: 1/x_Y = -1/10 - 1/3 = -13/30, x_Y = -30/13, YM = 30/13.
If x_X = -3: 1/x_Y = -1/10 + 1/3 = 7/30, x_Y = 30/7, YM = 30/7.

Both are valid. The problem should have a unique answer though. Let me reconsider.

Hmm, maybe I need to think about which case is geometrically valid. Let me think about the configuration more carefully.

Actually, in competition math, when they say "chords AB and CD intersect at M", and then define X = AD ∩ PQ, Y = BC ∩ PQ, the labeling of A, B, C, D on the circle matters. The points A, B, C, D are on the circle, and the chords AB and CD cross at M (inside the circle). 

For two chords crossing inside a circle, the four endpoints are in a specific cyclic order on the circle. If AB and CD cross at M, then going around the circle, the order is A, C, B, D (or A, D, B, C). The chords AC and BD don't cross inside (they're the "other" pair), while AD and BC also don't cross inside... wait, actually for a complete quadrilateral inscribed in a circle, if AB and CD are the crossing chords, then AC and BD also cross inside, and AD and BC also cross inside. No wait, that's not right either.

Let me think. If A, B, C, D are on a circle and AB crosses CD at M (inside), then the cyclic order is A, C, B, D (or equivalently A, D, B, C). In this case:
- AB and CD cross inside (given)
- AC and BD: A and C are separated by B and D in the cyclic order? Order is A, C, B, D. AC connects A to C (adjacent in order), BD connects B to D (adjacent). These don't cross inside.
- AD and BC: A to D (A, C, B, D — A and D are separated by C, B), B to C (adjacent). AD goes from A to D, BC from B to C. In the order A, C, B, D: A and D are not adjacent (C, B between them), B and C are adjacent. So AD and BC... do they cross? A is at position 1, D at position 4, B at position 3, C at position 2. AD connects 1-4, BC connects 3-2. In a circle with 4 points, chords 1-4 and 2-3 don't cross (they're on opposite sides). Wait, 1-4 and 2-3: these are the two "outer" chords that don't cross. Actually, for 4 points on a circle in order 1,2,3,4, the crossing chords are 1-3 and 2-4. The non-crossing pairs are 1-2 & 3-4, and 1-4 & 2-3.

So if the order is A, C, B, D (positions 1,2,3,4), the crossing chords are AB (1-3) and CD (2-4). The non-crossing pairs are AC (1-2) & BD (3-4), and AD (1-4) & BC (2-3).

So AD and BC don't cross inside the circle. They might intersect outside the circle, or their lines might intersect on PQ.

Now, X = AD ∩ PQ and Y = BC ∩ PQ. Since AD and BC don't cross inside the circle, X and Y are on the line PQ (which passes through the interior of the circle). 

Hmm, I don't think this constrains X to one side. Let me think about it differently.

Actually, let me reconsider the problem. Maybe both answers are valid and the problem expects both, or maybe I need to look at this more carefully.

Wait, actually, I realize the problem might have additional constraints I haven't used. Let me re-read: "Let A, B, C, D be points on the circle such that chords AB and CD intersect at M." So A, B, C, D are on the circle, AB and CD are chords (so A, B are distinct points on the circle, and the segment AB passes through M; similarly for CD).

"Let X be the intersection of AD and PQ, and let Y be the intersection of BC and PQ."

So X is where line AD meets line PQ, Y is where line BC meets line PQ. These are lines, not segments, so X and Y could be anywhere on line PQ.

"If XM = 3, then find YM."

Given the relation 1/x_X + 1/x_Y = -1/10, and |x_X| = 3, we get two possible values. But maybe the problem is from a competition and expects a specific answer. Let me think about whether there's a reason to prefer one.

Actually, I wonder if the problem is asking for YM as a positive quantity, and both 30/13 and 30/7 are possible, but maybe only one is consistent with the geometry (i.e., X and Y being on the same side or opposite sides of M).

Let me check my numerical examples:
Example 1: x_X = -2.715, x_Y = 3.727. X and Y on opposite sides of M.
Example 2: x_X = 3.165, x_Y = -2.410. X and Y on opposite sides of M.

In both examples, X and Y are on opposite sides of M. Is this always the case?

From the relation 1/x_X + 1/x_Y = -1/10 < 0, if x_X and x_Y have the same sign, then 1/x_X + 1/x_Y has that same sign. For the sum to be negative, either both are negative, or they have opposite signs with the negative one dominating.

If both x_X, x_Y < 0: 1/x_X + 1/x_Y < 0. This is possible.
If both x_X, x_Y > 0: 1/x_X + 1/x_Y > 0 ≠ -1/10. Impossible.
If opposite signs: possible.

So either both negative, or opposite signs. In my examples, they were opposite signs. Let me check if both negative is possible.

If x_X = -3: x_Y = 30/7 > 0. Opposite signs.
If x_X = 3: x_Y = -30/13 < 0. Opposite signs.

So in both cases, X and Y are on opposite sides. 

Hmm, but the problem gives a unique answer. Let me reconsider whether the problem might have a unique answer. 

Actually, maybe I should reconsider the problem statement. It says "If XM = 3, then find YM." In many competition problems, the answer is unique. Perhaps I need to check whether both values of x_X (±3) are achievable.

Let me check: can x_X = 3 be achieved? From my second numerical example, x_X ≈ 3.165, which is close to 3. So yes, x_X = 3 is achievable (by adjusting the angles slightly). Similarly, x_X = -3 should be achievable (my first example had x_X ≈ -2.715, close to -3).

So both cases are achievable, giving YM = 30/13 or YM = 30/7. 

Hmm, but the problem asks for a single answer. Let me reconsider.

Wait, maybe I should reconsider the problem. Perhaps the problem is from a specific competition and the answer is one of these. Let me think about which one is more "natural."

Actually, let me reconsider. Maybe the problem has additional structure I'm not seeing. Let me re-read:

"Let P and Q be points on a circle of radius 10, and let M be a point on PQ such that PM = 5 and QM = 10."

So PQ = 15, and M divides PQ with PM = 5, MQ = 10.

"Let A, B, C, D be points on the circle such that chords AB and CD intersect at M."

"Let X be the intersection of AD and PQ, and let Y be the intersection of BC and PQ."

"If XM = 3, then find YM."

I think the problem might expect both answers, or there might be a convention. But in competition math, usually there's a unique answer. Let me think again...

Actually, you know what, let me reconsider. Maybe the answer is supposed to be unique and I need to think about which case is valid based on the geometry of the situation.

Let me think about it more carefully. The line PQ passes through the circle, with P and Q on the circle. M is inside the circle (since OM = √50 < 10). The chords AB and CD pass through M.

Now, AD and BC are lines connecting points on the circle. X = AD ∩ PQ and Y = BC ∩ PQ.

Since AD is a chord (or its extension) and PQ is a chord (or its extension), X is the intersection of two lines determined by chords. 

Hmm, I think both cases are genuinely possible, and the problem might accept either, or there might be a specific competition context.

Actually, wait. Let me reconsider. Maybe the problem is designed so that YM is the same regardless of which side X is on. Let me re-examine.

If x_X = 3: YM = 30/13 ≈ 2.308
If x_X = -3: YM = 30/7 ≈ 4.286

These are different. So the answer depends on the side.

Hmm, let me reconsider the problem. Maybe there's a constraint that X is between P and Q, or outside, etc.

Actually, in many geometry problems from competitions, when they say "X is the intersection of AD and PQ", they might mean the lines, and X could be anywhere. But the problem gives XM = 3 as a condition, which is a specific value. The question is whether the problem has a unique answer.

Let me search my memory. This looks like it could be from AMC/AIME or a similar competition. The answer 30/7 or 30/13... 

Actually, let me reconsider. Maybe I have the relation wrong. Let me re-derive more carefully.

Actually, I proved the relation 1/x_X + 1/x_Y = -1/10 analytically, and verified it numerically. I'm confident it's correct.

Given XM = 3, the two cases give YM = 30/13 or 30/7.

Hmm, let me think about this differently. Maybe the problem is asking for a specific value and the answer is 30/7, based on some convention or additional geometric constraint.

Actually, let me reconsider the problem. Perhaps the problem intends X to be on a specific side. In many problems, the configuration is such that X is on the extension of PQ beyond P (i.e., on the side of P, which is the negative side in my coordinates). If X is on the P-side, x_X < 0, so x_X = -3, giving YM = 30/7.

Alternatively, if X is on the Q-side, x_X > 0, so x_X = 3, giving YM = 30/13.

Without more context, I think the problem likely has a unique answer. Let me think about whether there's a reason to prefer one.

Actually, I just realized something. Let me reconsider the problem. The problem says "chords AB and CD intersect at M". In the standard interpretation, A, B, C, D are on the circle, and the chords (segments) AB and CD intersect at M. This means M is between A and B, and between C and D.

Now, X = AD ∩ PQ. The line AD meets line PQ at X. Y = BC ∩ PQ.

In the cyclic order A, C, B, D (as I discussed), AD connects A (position 1) to D (position 4), and BC connects B (position 3) to C (position 2). These are the "non-crossing" pairs.

Now, where do AD and BC meet PQ? PQ is a chord through M. 

Hmm, I think the position of X relative to M depends on the specific configuration. Both sides are possible.

Let me try a different approach: maybe the problem has a unique answer and I should look for additional constraints.

Actually, wait. Let me reconsider. Perhaps the problem is from a competition where the answer is 30/7. Let me check: 30/7 is about 4.286, and 30/13 is about 2.308. 

Hmm, let me think about this more carefully. Actually, I think the issue might be that I need to consider the specific labeling. In the problem, AB and CD are chords through M, and X = AD ∩ PQ, Y = BC ∩ PQ. The labeling of which endpoint is A vs B and C vs D matters.

If we fix the chord AB (with A and B as specific endpoints) and chord CD (with C and D as specific endpoints), then X and Y are determined. But the problem doesn't specify which endpoint is which, so there's an ambiguity.

However, the problem says "If XM = 3, find YM", which suggests that regardless of the configuration, YM is determined by XM = 3. But we showed it's not—there are two possibilities.

Unless... the problem is asking for both, or the answer is the same in both cases (which it's not), or I'm missing something.

Let me re-examine. Actually, maybe I need to think about this more carefully. The problem gives specific chords AB and CD, and specific points X and Y. The condition XM = 3 is given. The question is: is YM uniquely determined?

From the relation 1/x_X + 1/x_Y = -1/10, given |x_X| = 3, we get two values of x_Y (and hence YM). But maybe only one of these is geometrically realizable for a given sign of x_X.

But both signs of x_X are realizable (as I showed numerically). So YM is not uniquely determined by XM = 3 alone.

Hmm, unless the problem has a typo or I'm misunderstanding something. Let me re-read the problem once more.

"Let P and Q be points on a circle of radius 10, and let M be a point on PQ such that PM = 5 and QM = 10. Let A, B, C, D be points on the circle such that chords AB and CD intersect at M. Let X be the intersection of AD and PQ, and let Y be the intersection of BC and PQ. If XM = 3, then find YM."

I think the problem is well-posed and has a unique answer. Let me reconsider whether there's an additional constraint.

Oh wait, maybe I need to think about this differently. The problem says "chords AB and CD intersect at M". This means M is the intersection of the chords AB and CD. But it also says M is on PQ. So M is the intersection of AB, CD, and PQ? No, M is on PQ, and AB and CD intersect at M. So M is on all three lines: AB, CD, and PQ. But PQ is a chord, and M is between P and Q.

Now, the key insight: maybe the problem is using a specific convention where X and Y are on the same side of M, or on specific sides.

Actually, let me reconsider. In competition problems, when they say "find YM", they usually expect a unique numerical answer. Given the two possibilities (30/7 and 30/13), maybe the answer is supposed to be 30/7.

But actually, let me reconsider whether both are truly achievable. Let me try to construct a configuration with x_X = 3 and check if it's valid.

From my second numerical example, x_X ≈ 3.165 with α = π/3, β = 2π/3. Let me adjust to get x_X = 3 exactly. It should be possible by continuity. And in that example, x_Y ≈ -2.410, so YM ≈ 2.410, which is close to 30/13 ≈ 2.308. The discrepancy is because x_X wasn't exactly 3.

Similarly, from my first example, x_X ≈ -2.715, x_Y ≈ 3.727. If I adjust to get x_X = -3, then x_Y should be 30/7 ≈ 4.286.

So both are achievable. The problem has two answers. But competition problems usually have one...

Let me reconsider. Maybe the problem is from a specific competition and the expected answer considers both cases. Or maybe I should present both.

Actually, wait. Let me reconsider the problem. Maybe there's a constraint that X is between P and Q, or outside segment PQ. Let me check:

In my first example: x_X = -2.715. P = -5, Q = 10. So X = -2.715 is between P and Q. XM = 2.715.
In my second example: x_X = 3.165. This is also between P and Q. XM = 3.165.

So in both cases, X is between P and Q. Both x_X = 3 and x_X = -3 are between P = -5 and Q = 10.

Hmm, I'm stuck on why the problem would have a unique answer. Let me just go with both answers and see.

Actually, you know what, let me reconsider. Maybe the problem is designed so that the answer is unique, and I need to think about it differently. 

Let me reconsider: maybe the relation isn't 1/x_X + 1/x_Y = -1/10 but something else, and I made an error.

Let me re-derive. I had:

1/x_X + 1/x_Y = [t₁t₂(s₁+s₂)sinα - s₁s₂(t₁+t₂)sinβ] / [t₁t₂s₁s₂ sin(α-β)]

With t₁t₂ = s₁s₂ = -50:

= [-50(s₁+s₂)sinα + 50(t₁+t₂)sinβ] / [2500 sin(α-β)]
= 50[-(s₁+s₂)sinα + (t₁+t₂)sinβ] / [2500 sin(α-β)]

Now, t₁+t₂ = 5(cosα + √7 sinα), s₁+s₂ = 5(cosβ + √7 sinβ).

= 50[-5(cosβ + √7 sinβ)sinα + 5(cosα + √7 sinα)sinβ] / [2500 sin(α-β)]
= 250[-cosβ sinα - √7 sinβ sinα + cosα sinβ + √7 sinα sinβ] / [2500 sin(α-β)]
= 250[-cosβ sinα + cosα sinβ] / [2500 sin(α-β)]
= 250[-(sinα cosβ - cosα sinβ)] / [2500 sin(α-β)]
= 250[-sin(α-β)] / [2500 sin(α-β)]
= -250/2500 = -1/10. ✓

The derivation is correct. The relation is 1/x_X + 1/x_Y = -1/10.

Now, -1/10 = 1/(-5) + 1/(10) = 1/x_P + 1/x_Q.

So the general relation is: **1/XM + 1/YM = 1/PM + 1/QM** (using signed distances from M along PQ, with P on the negative side and Q on the positive side).

This is a known result in projective geometry, related to the concept of "harmonic conjugates" but in a different form. Actually, this is the relation for the "Desargues involution" or something similar.

Given XM = 3 (unsigned), we have two cases. Let me think about whether the problem might expect us to consider X on a specific side.

Actually, I just realized: maybe the problem is from a competition where the answer is 30/7, and the intended configuration has X on the P-side (x_X = -3). Or maybe the answer is 30/13 with X on the Q-side.

Let me think about which is more natural. In the problem, P is closer to M (PM = 5) and Q is farther (QM = 10). If X is on the P-side (between P and M or beyond P), then XM = 3 means X is between P and M (since PM = 5 > 3). If X is on the Q-side, X is between M and Q (since QM = 10 > 3).

Both are geometrically valid. I think the problem might accept either answer, or there might be a specific convention.

Actually, let me reconsider. Perhaps the problem is from a specific source and the answer is 30/7. Let me think about the structure: 30/7 and 30/13. 

Hmm, 30 = 2 · 3 · 5 = PM · XM · 2. And 7 = 10 - 3 = QM - XM, 13 = 10 + 3 = QM + XM. 

So YM = PM · XM / |QM - XM| = 5 · 3 / 7 = 15/7... no, that's not 30/7.

Let me see: 30/7 = 2 · 15/7 = 2 · PM · XM / (QM - XM). And 30/13 = 2 · 15/13 = 2 · PM · XM / (QM + XM).

Actually, from the relation 1/x_X + 1/x_Y = -1/10:

If x_X = -3 (X on P-side): 1/x_Y = -1/10 + 1/3 = 7/30, x_Y = 30/7.
If x_X = 3 (X on Q-side): 1/x_Y = -1/10 - 1/3 = -13/30, x_Y = -30/13.

YM = |x_Y| = 30/7 or 30/13.

Note: 30/7 = 30/(10-3) and 30/13 = 30/(10+3). And 30 = 2·5·3 = 2·PM·XM.

So YM = 2·PM·XM / |QM ∓ XM|.

Hmm, I think the problem likely has a unique answer. Let me reconsider whether there's a constraint that forces X to one side.

Actually, I just thought of something. Maybe the problem is set up so that X and Y are both outside the circle, or both inside, or one inside and one outside. Let me check.

The circle intersects PQ at P = (-5, 0) and Q = (10, 0). Points on PQ inside the circle have x between -5 and 10. Points outside have x < -5 or x > 10.

In my first example: x_X = -2.715 (inside), x_Y = 3.727 (inside). Both inside.
In my second example: x_X = 3.165 (inside), x_Y = -2.410 (inside). Both inside.

So X and Y are both inside the circle (between P and Q) in these examples. Both cases have X and Y inside.

I think the problem genuinely has two answers. But since competition problems usually have one, let me consider the possibility that the answer is 30/7.

Actually, I just realized I should think about this more carefully. The problem says "chords AB and CD intersect at M". This means AB and CD are chords (line segments inside the circle) that cross at M. Then AD and BC are also chords (or their extensions). X = AD ∩ PQ is the intersection of lines AD and PQ. 

Now, AD is a chord of the circle (connecting A and D on the circle). The line AD intersects PQ at X. Since both AD and PQ are chords (or their extensions), X could be inside or outside the circle.

But here's the thing: in the cyclic order A, C, B, D, the chord AD connects non-adjacent points (A and D are separated by C and B). Wait, no: in the order A, C, B, D, A and D are adjacent (D is next to A going the other way). So AD is a side of the quadrilateral ACBD, not a diagonal. Similarly, BC is a side.

The sides AD and BC of the cyclic quadrilateral ACBD don't intersect inside the circle (they're opposite sides). Their lines intersect outside the circle. But X = AD ∩ PQ, not AD ∩ BC. So X is where line AD meets line PQ, which is different from where AD meets BC.

OK I think I'm overcomplicating this. Let me just go with the answer.

Given the relation and the two cases, I believe the problem expects a unique answer. Looking at the structure, I think the answer is **30/7**.

Here's my reasoning: if X is on the same side as P (the closer endpoint), then x_X = -3, and YM = 30/7. If X is on the same side as Q, then YM = 30/13.

Actually, I don't have a strong reason to prefer one over the other. Let me reconsider the problem once more.

Hmm, actually, I wonder if the problem might have a unique answer because of a constraint I haven't considered. Let me think about whether X and Y must be on opposite sides of M.

From the relation 1/x_X + 1/x_Y = -1/10 < 0:
- If x_X > 0 and x_Y > 0: sum > 0. Impossible.
- If x_X < 0 and x_Y < 0: sum < 0. Possible.
- If x_X > 0 and x_Y < 0: possible if |1/x_Y| > 1/x_X.
- If x_X < 0 and x_Y > 0: possible if |1/x_X| > 1/x_Y.

In my examples, X and Y were on opposite sides. But both negative is also possible. Let me check: if x_X = -3, x_Y = 30/7 > 0. Opposite sides. If x_X = 3, x_Y = -30/13 < 0. Opposite sides. So in both cases with |x_X| = 3, X and Y are on opposite sides.

Can both be negative? We'd need 1/x_X + 1/x_Y = -1/10 with both negative. E.g., x_X = -2, then 1/x_Y = -1/10 + 1/2 = 4/10 = 2/5, x_Y = 5/2 > 0. Not both negative. x_X = -20, 1/x_Y = -1/10 + 1/20 = -1/20, x_Y = -20. Both negative! So XM = 20, YM = 20. But that's a different XM.

OK so for XM = 3, both cases give X and Y on opposite sides. The problem has two answers. 

Let me just go with presenting the solution and noting both cases. But actually, for a competition, I think the answer is likely **30/7**.

Wait, actually, let me reconsider. I want to make sure I haven't mixed up which point is X and which is Y. Let me re-examine.

The problem says X = AD ∩ PQ and Y = BC ∩ PQ. In my coordinate system, I computed x_X using A and D, and x_Y using B and C. Let me double-check with the first numerical example.

α = π/2: A = (0, 16.297), B = (0, -3.068). So A is above M, B is below.
β = π/6: C = (12.482, 7.207), D = (-3.004, -1.735). C is to the upper right, D is to the lower left.

X = AD ∩ x-axis: A = (0, 16.297) (above), D = (-3.004, -1.735) (below). Line from A to D crosses x-axis at x ≈ -2.715. ✓

Y = BC ∩ x-axis: B = (0, -3.068) (below), C = (12.482, 7.207) (above). Line from B to C crosses x-axis at x ≈ 3.727. ✓

So X is on the P-side (negative) and Y is on the Q-side (positive). XM ≈ 2.715, YM ≈ 3.727.

If I want XM = 3 with X on the P-side, I'd get YM = 30/7 ≈ 4.286.
If I want XM = 3 with X on the Q-side, I'd get YM = 30/13 ≈ 2.308.

I think the problem might be expecting the answer 30/7, but I'm not 100% sure. Let me think about whether there's a way to determine the side.

Actually, I just realized: maybe the problem is well-posed and the answer is unique because of the way the points are labeled. In the problem, A, B, C, D are specific points, and X and Y are defined in terms of them. The condition XM = 3 might force a specific configuration.

But as I showed, both x_X = 3 and x_X = -3 are achievable with appropriate choices of chords. So the answer is not unique based on XM = 3 alone.

Hmm, let me reconsider. Maybe I should look at this from a different angle (no pun intended).

Actually, I think I might be overthinking this. Let me consider the possibility that the problem has a unique answer of 30/7, based on the convention that X is on the P-side. Or maybe the answer is 30/13.

Let me try to see if there's a pattern. The relation is:

1/x_X + 1/x_Y = 1/x_P + 1/x_Q

With x_P = -5, x_Q = 10, this gives 1/x_X + 1/x_Y = -1/10.

If x_X = -3 (P-side): 1/x_Y = -1/10 + 1/3 = 7/30, YM = 30/7.
If x_X = 3 (Q-side): 1/x_Y = -1/10 - 1/3 = -13/30, YM = 30/13.

Hmm, 30/7 is nicer (smaller denominator). Also, 30/7 = 30/(10-3) and 30/13 = 30/(10+3). 

I think the answer the problem is looking for is **30/7**. This corresponds to X being on the same side as P (between P and M, since PM = 5 > 3 = XM). This seems like the more natural configuration.

But actually, I realize I should think about this more carefully. Let me consider the problem from the perspective of the original problem source. This looks like it could be from HMMT, USAMO, or a similar competition. The answer 30/7 seems more likely for a competition.

Actually, I just thought of something else. Let me reconsider whether the problem might have a unique answer by thinking about what configurations are possible.

The key question is: for the given circle and point M, can we always find chords AB and CD through M such that X = AD ∩ PQ has XM = 3 on either side?

I believe the answer is yes for both sides, as my numerical examples show (with slight adjustments needed to get exactly XM = 3).

So the problem has two answers: 30/7 and 30/13. But if forced to choose one, I'd go with 30/7.

Hmm, actually, wait. Let me reconsider. Maybe the problem is from a competition where the answer is required to be a specific value, and the problem is designed to have a unique answer. Let me think about whether there's a constraint I'm missing.

Oh! I just realized something. Maybe the problem is asking for YM as a function of XM, and the answer is supposed to work for both cases. But 30/7 ≠ 30/13, so that doesn't work.

Let me try yet another approach. Maybe I should use unsigned distances throughout. The relation in terms of unsigned distances:

If X and Y are on opposite sides of M (which they are when XM = 3):
- X on P-side: 1/(-XM) + 1/(YM) = -1/10 => -1/XM + 1/YM = -1/10 => 1/YM = 1/XM - 1/10
  With XM = 3: 1/YM = 1/3 - 1/10 = 7/30, YM = 30/7.
  
- X on Q-side: 1/(XM) + 1/(-YM) = -1/10 => 1/XM - 1/YM = -1/10 => 1/YM = 1/XM + 1/10
  With XM = 3: 1/YM = 1/3 + 1/10 = 13/30, YM = 30/13.

So the two cases give different formulas:
- X on P-side: 1/YM = 1/XM - 1/QM (since QM = 10)
- X on Q-side: 1/YM = 1/XM + 1/QM

Hmm, these are different. The problem doesn't specify which side X is on.

I think the problem might be expecting the answer 30/7, but I'm not certain. Let me just go with 30/7 as my answer, noting the relation and the computation.

Actually, let me reconsider one more time. I want to check if maybe the problem has a unique answer because of some symmetry or additional constraint.

The problem says PM = 5, QM = 10. Note that PM · QM = 50 = |power of M|. And the circle has radius 10. 

Hmm, 5 = R/2 and 10 = R. So PM = R/2 and QM = R. That's a nice relationship. Does this imply anything?

The distance from O to PQ: let me compute. OM = √50, and the foot of perpendicular from O to PQ is at the midpoint of PQ, which is at distance 7.5 from P and 7.5 from Q. M is at 5 from P, so M is 2.5 from the midpoint. OM² = (distance from O to PQ)² + 2.5² = 43.75 + 6.25 = 50. ✓

I don't think the specific values PM = R/2, QM = R add any constraint that would make the answer unique.

OK, I'll go with 30/7 as my answer. But let me also mention 30/13 as an alternative.

Actually, wait. Let me reconsider the problem one more time. I want to make sure I haven't made an error in the relation.

Let me re-derive the relation using a cleaner method. 

Consider the involution on line PQ. The circle induces an involution on PQ as follows: for any point Z on PQ, draw any secant through Z meeting the circle at two points; the involution pairs Z with Z' such that Z' is the other intersection of PQ with the circle's... no, that's not right.

Actually, the correct involution: for a point Z on line PQ, the involution σ maps Z to Z' where Z' is defined by: for any line through Z meeting the circle at U, V, the line through Z' and the pole of line ZUV... this is getting complicated.

Let me use a different approach. The key relation I proved is:

1/x_X + 1/x_Y = 1/x_P + 1/x_Q

where x_P, x_Q, x_X, x_Y are signed coordinates on line PQ with M as origin.

This can be rewritten as: (x_X + x_Y)/(x_X · x_Y) = (x_P + x_Q)/(x_P · x_Q).

Note x_P + x_Q = -5 + 10 = 5 = PQ - 2·PM = 15 - 10 = 5. And x_P · x_Q = (-5)(10) = -50 = power of M.

So (x_X + x_Y)/(x_X · x_Y) = 5/(-50) = -1/10. ✓

This is a cross-ratio-like relation. In fact, it says that the "sum of reciprocals" of X and Y (w.r.t. M) equals the "sum of reciprocals" of P and Q. This is equivalent to saying that M, X, Y and M, P, Q are related by an involution of the form z ↦ c/z (a Möbius involution fixing M=0 and the point at infinity).

Actually, the involution z ↦ -50/z maps P = -5 to -50/(-5) = 10 = Q, and X to -50/x_X. If Y = -50/x_X, then 1/x_X + 1/x_Y = 1/x_X + 1/(-50/x_X) = 1/x_X - x_X/50. For this to equal -1/10, we need 1/x_X - x_X/50 = -1/10, which gives (50 - x_X²)/(50 x_X) = -1/10, so 10(50 - x_X²) = -50 x_X, 500 - 10x_X² = -50x_X, 10x_X² - 50x_X - 500 = 0, x_X² - 5x_X - 50 = 0, x_X = (5 ± √225)/2 = (5 ± 15)/2 = 10 or -5. So this involution maps P to Q and Q to P, but doesn't give the X-Y relation.

Let me try the involution z ↦ c/z for some c. If σ(X) = Y, then Y = c/x_X, and 1/x_X + 1/Y = 1/x_X + x_X/c. For this to equal -1/10 for all X, we'd need 1/x_X + x_X/c = -1/10, which is not constant. So it's not a simple z ↦ c/z involution.

Actually, the relation 1/x_X + 1/x_Y = constant means x_Y = 1/(c - 1/x_X) = x_X/(cx_X - 1) where c = -1/10. This is a Möbius transformation: σ(z) = z/(cz - 1) = z/(-z/10 - 1) = -10z/(z + 10). Let me check: σ(-5) = -10(-5)/(-5+10) = 50/5 = 10 = Q. ✓ σ(10) = -10(10)/(10+10) = -100/20 = -5 = P. ✓ So this involution swaps P and Q, and maps X to Y.

The involution is σ(z) = -10z/(z+10). This is a Möbius involution (σ² = identity) that swaps P = -5 and Q = 10.

Now, σ(z) = -10z/(z+10). σ(3) = -30/13. σ(-3) = 30/7.

So if X = 3, Y = -30/13, YM = 30/13.
If X = -3, Y = 30/7, YM = 30/7.

I'm now fairly confident the answer is one of these two values. For a competition, I'll go with **30/7**.

But actually, let me reconsider. Maybe the problem is designed to have a unique answer, and I need to think about which case is "canonical."

Hmm, I just thought of something. In the problem, P is the point closer to M (PM = 5) and Q is farther (QM = 10). The problem defines X = AD ∩ PQ. In many configurations, X tends to be on the side of the closer point (P-side). But this is just a heuristic.

Actually, let me think about this differently. The problem gives XM = 3 < PM = 5. So X is between P and M (if on the P-side) or between M and Q (if on the Q-side, since QM = 10 > 3). Both are valid.

I think the problem might have two answers, but if I had to choose one for a competition, I'd go with 30/7.

Actually, you know what, let me reconsider the problem from scratch. Maybe I'm wrong about the relation and there's a unique answer.

Let me try a completely different approach: use the power of a point and Menelaus' theorem.

Consider triangle MXY (wait, X, M, Y are collinear on PQ, so that's degenerate). 

Let me use Menelaus' theorem on a suitable triangle.

Consider triangle AXD (wait, X is on AD, so that's degenerate too).

Let me think about this differently. Consider the complete quadrilateral with vertices A, B, C, D. The diagonal triangle has vertices:
- M = AB ∩ CD
- N = AC ∩ BD  
- L = AD ∩ BC

The line PQ passes through M and meets AD at X and BC at Y. Note that L = AD ∩ BC, so X is on line AD and Y is on line BC, and L is the intersection of AD and BC. So X, Y, L are related: X is on AD, Y is on BC, and L = AD ∩ BC.

Now, consider triangle LXY (wait, X is on line LA = LD, Y is on line LB = LC, and L is the vertex). Actually, X is on line LD (= AD) and Y is on line LC (= BC), with L = AD ∩ BC. So in triangle LDC (or LAB), X is on LD and Y is on LC.

Hmm, this is getting complicated. Let me just go with my answer.

I'll present the solution with the relation 1/x_X + 1/x_Y = 1/x_P + 1/x_Q = -1/10, and compute YM for both cases. I believe the intended answer is 30/7.

Wait, actually, I want to reconsider one more time. Let me think about whether the problem might have a unique answer by considering the specific geometry.

The problem says "chords AB and CD intersect at M". In a circle, two chords intersecting at a point inside the circle. The four endpoints A, B, C, D are on the circle. The problem then defines X = AD ∩ PQ and Y = BC ∩ PQ.

Now, here's a key observation: the problem doesn't specify the order of A, B on the chord or C, D on the chord. But the definitions of X and Y depend on the labeling. If we swap A and B, X becomes BD ∩ PQ and Y becomes AC ∩ PQ, which are different points. Similarly for swapping C and D.

So the problem is: given chords AB and CD through M (with specific labeling), X = AD ∩ PQ has XM = 3. Find YM = |BC ∩ PQ - M|.

The answer depends on the labeling and the specific chords. But the relation 1/x_X + 1/x_Y = -1/10 holds regardless. So given XM = 3, YM is either 30/7 or 30/13.

I think for a competition, the answer is likely 30/7. Let me go with that.

Hmm, actually, let me reconsider once more. I want to check if maybe the problem has a unique answer of 30/7 because of some additional geometric constraint that I'm not seeing.

Let me think about the position of X. X = AD ∩ PQ. A and D are on the circle, and the line AD intersects PQ at X. 

In the cyclic order A, C, B, D (going around the circle), A and D are adjacent (they're connected by a side of the quadrilateral). The line AD is a chord of the circle (or its extension). 

Now, PQ is also a chord, passing through M. The line AD intersects line PQ at X. 

For X to be between P and Q (inside the circle), the chord AD must intersect the chord PQ inside the circle. But AD and PQ are both chords, and they intersect at X. If X is inside the circle, then by the power of a point, XA · XD = XP · XQ.

If X is outside the circle, then XA · XD = XP · XQ still holds (with signed lengths).

Hmm, this doesn't directly help. Let me just go with my answer.

I'll present the proof with the key relation and compute YM = 30/7 (assuming X is on the P-side, which I believe is the intended configuration).

Actually, let me reconsider one final time. I want to check: is the answer perhaps unique and equal to 30/7, regardless of which side X is on? No, that can't be, because the two cases give different values.

OK wait, I just want to double-check my formula with a third numerical example to make sure the relation is correct.

Let me try α = π/4, β = 3π/4.

α = π/4: cosα = sinα = 1/√2. c_α = (1 + √7)/√2 ≈ (1 + 2.6458)/1.4142 ≈ 2.5733.
t² - 5(2.5733)t - 50 = 0 => t = [12.8665 ± √(165.55 + 200)]/2 = [12.8665 ± 19.120]/2.
t₁ ≈ 15.993, t₂ ≈ -3.127.

A = (15.993/√2, 15.993/√2) ≈ (11.309, 11.309).
B = (-3.127/√2, -3.127/√2) ≈ (-2.211, -2.211).

β = 3π
