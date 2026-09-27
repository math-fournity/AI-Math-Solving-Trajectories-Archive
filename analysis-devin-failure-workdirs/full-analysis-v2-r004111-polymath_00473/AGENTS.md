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
  <problem_id>polymath_00473</problem_id>
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

The square \(DEFG\) is contained in equilateral triangle \(ABC\), with \(E\) on \(\overline{AC}\), \(G\) on \(\overline{AD}\), and \(F\) as the midpoint of \(\overline{BC}\). Find \(AD\) if \(DE=6\).

## Standard Solution

Let the midpoint of \(\overline{DF}\) be \(H\). Since \(\overline{DF} \perp \overline{EH}\), triangle \(AHE\) is a \(30^{\circ}-60^{\circ}-90^{\circ}\) triangle. We have \(EH = DH = \frac{1}{2} DF = \frac{1}{2} \cdot 6\sqrt{2} = 3\sqrt{2}\), and \(AH = \sqrt{3} \cdot EH = 3\sqrt{6}\). Therefore, \(AD = AH - DH = 3\sqrt{6} - 3\sqrt{2}\).
\(3\sqrt{6} - 3\sqrt{2}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this geometry problem. Let me set up coordinates.

We have an equilateral triangle ABC with a square DEFG inside it. E is on AC, G is on AD, F is the midpoint of BC. DE = 6, so the square has side 6.

Wait, let me re-read. "The square DEFG is contained in equilateral triangle ABC, with E on AC, G on AD, and F as the midpoint of BC. Find AD if DE=6."

So DEFG is a square with side length 6 (since DE = 6 and it's a square, all sides are 6).

E on AC, G on AD, F is midpoint of BC.

Wait, G is on AD? AD is a cevian from A to D. Where is D? D must be a point... Let me think. The square is DEFG. So the vertices are D, E, F, G in order. D is a vertex of the square, not necessarily a vertex of the triangle.

Let me set up coordinates. Let the equilateral triangle ABC have:
- B at the origin or some convenient location.

Let me place F (midpoint of BC) conveniently. Let B = (-s, 0), C = (s, 0), so F = (0, 0) is the midpoint of BC. Then A is at the top: A = (0, h) where h = s√3 (since equilateral triangle with side 2s has height s√3).

Actually, let me use side length of triangle = a. Then B = (-a/2, 0), C = (a/2, 0), A = (0, a√3/2). F = midpoint of BC = (0, 0).

The square DEFG has vertices in order D, E, F, G. So the sides are DE, EF, FG, GD. DE = EF = FG = GD = 6.

F = (0, 0) is one vertex of the square.

E is on AC. G is on AD. D is a vertex of the square.

So the square has F at origin, E on line AC, G on line AD, and D is the fourth vertex.

Let me think about the geometry. The square DEFG: going around D→E→F→G→D. So DE and FG are opposite sides, EF and GD are opposite sides.

Actually in a square DEFG, the order is D-E-F-G, so DE, EF, FG, GD are the sides. DE is adjacent to EF, etc.

Let me set up. F = (0,0). The square has side 6. Let me parameterize the square.

Since F is a vertex and E, G are adjacent to F (E-F and F-G are sides), wait no. In DEFG, the sides are DE, EF, FG, GD. So E is adjacent to F (side EF), and G is adjacent to F (side FG). D is opposite to F.

So EF = 6, FG = 6, and D is the vertex opposite F.

E is on AC, G is on AD. D is the opposite vertex from F.

Let me set coordinates. F = (0, 0). Let the square be oriented at some angle. Let's say the direction from F to E makes angle θ, and from F to G makes angle θ - 90° (or θ + 90°).

E = F + 6(cos θ, sin θ) = (6 cos θ, 6 sin θ)
G = F + 6(cos(θ - 90°), sin(θ - 90°)) = (6 sin θ, -6 cos θ)

Wait, let me be careful. In square DEFG, going D→E→F→G, the direction from E to F and from F to G... Let me think of it as: E, F, G are consecutive vertices. So EF and FG are sides meeting at F, perpendicular to each other.

Let me say E = (6 cos θ, 6 sin θ) and G = (6 cos(θ + 90°), 6 sin(θ + 90°)) = (-6 sin θ, 6 cos θ).

Then D = E + G - F = E + G = (6 cos θ - 6 sin θ, 6 sin θ + 6 cos θ).

Now constraints:
- E on AC
- G on AD
- D is opposite F in the square.

Line AC: from A = (0, a√3/2) to C = (a/2, 0).

Parametrize AC: points (t · a/2, a√3/2 · (1 - t)) for t ∈ [0, 1]. Or equation: the line from (0, a√3/2) to (a/2, 0).

Slope of AC = (0 - a√3/2)/(a/2 - 0) = -√3. So line AC: y = -√3 x + a√3/2, i.e., y = √3(a/2 - x).

E = (6 cos θ, 6 sin θ) on AC: 6 sin θ = √3(a/2 - 6 cos θ)
→ 6 sin θ = a√3/2 - 6√3 cos θ
→ 6 sin θ + 6√3 cos θ = a√3/2 ... (1)

Now G on AD. A = (0, a√3/2), D = (6 cos θ - 6 sin θ, 6 sin θ + 6 cos θ).

Line AD: from A to D. G = (-6 sin θ, 6 cos θ) must be on this line.

This is getting complex. Let me use a different approach or just push through.

G on line AD means A, G, D are collinear.

A = (0, a√3/2)
G = (-6 sin θ, 6 cos θ)
D = (6 cos θ - 6 sin θ, 6 sin θ + 6 cos θ)

Collinearity: (G - A) × (D - A) = 0 (cross product in 2D).

G - A = (-6 sin θ, 6 cos θ - a√3/2)
D - A = (6 cos θ - 6 sin θ, 6 sin θ + 6 cos θ - a√3/2)

Cross product = (-6 sin θ)(6 sin θ + 6 cos θ - a√3/2) - (6 cos θ - a√3/2)(6 cos θ - 6 sin θ) = 0

Let me expand:
First term: -6 sin θ (6 sin θ + 6 cos θ - a√3/2) = -36 sin²θ - 36 sin θ cos θ + 3a√3 sin θ

Second term: (6 cos θ - a√3/2)(6 cos θ - 6 sin θ)
= 36 cos²θ - 36 sin θ cos θ - 3a√3 cos θ + 3a√3 sin θ

So cross product = first - second:
= (-36 sin²θ - 36 sin θ cos θ + 3a√3 sin θ) - (36 cos²θ - 36 sin θ cos θ - 3a√3 cos θ + 3a√3 sin θ)
= -36 sin²θ - 36 sin θ cos θ + 3a√3 sin θ - 36 cos²θ + 36 sin θ cos θ + 3a√3 cos θ - 3a√3 sin θ
= -36(sin²θ + cos²θ) + 3a√3 cos θ
= -36 + 3a√3 cos θ = 0

So 3a√3 cos θ = 36 → a√3 cos θ = 12 → cos θ = 12/(a√3) ... (2)

From (1): 6 sin θ + 6√3 cos θ = a√3/2
→ sin θ + √3 cos θ = a√3/12

From (2): cos θ = 12/(a√3) = 4√3/a... wait, 12/(a√3) = 12√3/(3a) = 4√3/a.

So cos θ = 4√3/a.

From (1): sin θ + √3 · 4√3/a = a√3/12
→ sin θ + 12/a = a√3/12
→ sin θ = a√3/12 - 12/a

Now use sin²θ + cos²θ = 1:
(a√3/12 - 12/a)² + (4√3/a)² = 1

Let me expand:
(a√3/12)² - 2·(a√3/12)·(12/a) + (12/a)² + (4√3/a)² = 1
= 3a²/144 - 2√3 + 144/a² + 48/a² = 1
= a²/48 - 2√3 + 192/a² = 1

So: a²/48 + 192/a² = 1 + 2√3

Let u = a². Then:
u/48 + 192/u = 1 + 2√3

Multiply by 48u:
u² + 192·48 = 48u(1 + 2√3)
u² + 9216 = 48u(1 + 2√3)
u² - 48(1 + 2√3)u + 9216 = 0

Let me compute 48(1 + 2√3) = 48 + 96√3.

u² - (48 + 96√3)u + 9216 = 0

Using quadratic formula:
u = [(48 + 96√3) ± √((48 + 96√3)² - 4·9216)] / 2

Compute discriminant:
(48 + 96√3)² = 48² + 2·48·96√3 + (96√3)² = 2304 + 9216√3 + 27648 = 29952 + 9216√3

4·9216 = 36864

Discriminant = 29952 + 9216√3 - 36864 = 9216√3 - 6912

Hmm, let me factor. 9216√3 - 6912 = 2304(4√3 - 3).

√(2304(4√3 - 3)) = 48√(4√3 - 3)

So u = [(48 + 96√3) ± 48√(4√3 - 3)] / 2 = 24(1 + 2√3) ± 24√(4√3 - 3)

Hmm, this is getting messy. Let me check if 4√3 - 3 is a perfect square of something nice.

4√3 - 3 ≈ 4(1.732) - 3 = 6.928 - 3 = 3.928. √3.928 ≈ 1.982. Not obviously nice.

Let me reconsider. Maybe I should check which root is valid and whether AD has a clean form.

Wait, the problem asks for AD, not the side length a. AD is the distance from A to D.

D = (6 cos θ - 6 sin θ, 6 sin θ + 6 cos θ)
A = (0, a√3/2)

AD² = (6 cos θ - 6 sin θ)² + (6 sin θ + 6 cos θ - a√3/2)²

Let me compute. Let me denote c = cos θ, s = sin θ.

AD² = (6c - 6s)² + (6s + 6c - a√3/2)²
= 36(c-s)² + (6(s+c) - a√3/2)²

From (1): 6(s + √3 c) = a√3/2, so a√3/2 = 6s + 6√3 c.

So 6(s+c) - a√3/2 = 6s + 6c - 6s - 6√3 c = 6c - 6√3 c = 6c(1 - √3).

And (6c - 6s)² = 36(c - s)².

AD² = 36(c - s)² + 36c²(1 - √3)²
= 36[(c - s)² + c²(1 - √3)²]
= 36[c² - 2cs + s² + c²(1 - 2√3 + 3)]
= 36[1 - 2cs + c²(4 - 2√3)]

Hmm, still has cs and c² terms. Let me use the values.

c = 4√3/a, s = a√3/12 - 12/a.

cs = (4√3/a)(a√3/12 - 12/a) = 4√3 · √3/12 - 48/a² = 12/12 - 48/a² = 1 - 48/a²

c² = 48/a²

AD² = 36[1 - 2(1 - 48/a²) + (48/a²)(4 - 2√3)]
= 36[1 - 2 + 96/a² + 192/a² - 96√3/a²]
= 36[-1 + 288/a² - 96√3/a²]
= 36[-1 + (288 - 96√3)/a²]
= 36[-1 + 96(3 - √3)/a²]

Now from our equation: a²/48 + 192/a² = 1 + 2√3, so 192/a² = 1 + 2√3 - a²/48.

96/a² = (1 + 2√3 - a²/48)/2 = (1 + 2√3)/2 - a²/96

So 96(3 - √3)/a² = (3 - √3)[(1 + 2√3)/2 - a²/96]
= (3 - √3)(1 + 2√3)/2 - (3 - √3)a²/96

(3 - √3)(1 + 2√3) = 3 + 6√3 - √3 - 2·3 = 3 + 5√3 - 6 = -3 + 5√3

So 96(3 - √3)/a² = (-3 + 5√3)/2 - (3 - √3)a²/96

AD² = 36[-1 + (-3 + 5√3)/2 - (3 - √3)a²/96]
= 36[(-2 - 3 + 5√3)/2 - (3 - √3)a²/96]
= 36[(-5 + 5√3)/2 - (3 - √3)a²/96]
= 36 · 5(√3 - 1)/2 - 36(3 - √3)a²/96
= 90(√3 - 1) - (3/8)(3 - √3)a²

This still depends on a². Let me try a different approach—maybe directly compute AD² in terms of known quantities.

Actually, let me reconsider. Maybe there's a cleaner geometric approach.

Let me reconsider the problem. Actually, let me try to verify with a numerical approach first to see what the answer should be.

From u² - (48 + 96√3)u + 9216 = 0:

48 + 96√3 ≈ 48 + 166.27 = 214.27

u = [214.27 ± √(214.27² - 36864)] / 2 = [214.27 ± √(45911.6 - 36864)] / 2 = [214.27 ± √9047.6] / 2 = [214.27 ± 95.12] / 2

u₁ = (214.27 + 95.12)/2 = 154.7 → a ≈ 12.44
u₂ = (214.27 - 95.12)/2 = 59.58 → a ≈ 7.72

For the square to fit inside the triangle, we need a reasonable size. Let me check both.

For u₁ ≈ 154.7, a ≈ 12.44:
cos θ = 4√3/12.44 ≈ 6.928/12.44 ≈ 0.557, θ ≈ 56.2°
sin θ = a√3/12 - 12/a ≈ 12.44·1.732/12 - 12/12.44 ≈ 1.795 - 0.965 ≈ 0.830

Check: sin² + cos² = 0.689 + 0.310 = 0.999 ✓

E = (6·0.557, 6·0.830) = (3.34, 4.98)
G = (-6·0.830, 6·0.557) = (-4.98, 3.34)
D = E + G = (-1.64, 8.32)

A = (0, 12.44·1.732/2) = (0, 10.77)
C = (6.22, 0), B = (-6.22, 0)

Check E on AC: line from (0, 10.77) to (6.22, 0). At x=3.34: y = 10.77 - (10.77/6.22)·3.34 = 10.77 - 1.732·3.34 = 10.77 - 5.78 = 4.99 ✓

Check G on AD: A=(0, 10.77), D=(-1.64, 8.32). Line AD direction: (-1.64, -2.45). G = (-4.98, 3.34). Is G on ray from A through D? A + t(D - A) = (0 - 1.64t, 10.77 - 2.45t). For x = -4.98: t = 4.98/1.64 = 3.04. Then y = 10.77 - 2.45·3.04 = 10.77 - 7.45 = 3.32 ≈ 3.34 ✓

AD = distance from (0, 10.77) to (-1.64, 8.32) = √(1.64² + 2.45²) = √(2.69 + 6.00) = √8.69 ≈ 2.95

Hmm, that's small. Let me check the other root.

For u₂ ≈ 59.58, a ≈ 7.72:
cos θ = 4√3/7.72 ≈ 6.928/7.72 ≈ 0.897, θ ≈ 26.3°
sin θ = 7.72·1.732/12 - 12/7.72 ≈ 1.114 - 1.554 ≈ -0.440

Hmm, sin θ is negative, meaning E would be below the x-axis, but E should be on AC which is above the x-axis. So this root doesn't work geometrically (E would not be on segment AC properly).

Actually wait, let me check. E = (6 cos θ, 6 sin θ) = (5.38, -2.64). But AC goes from (0, 6.69) to (3.86, 0), all with y ≥ 0. So E at y = -2.64 is not on AC. So u₂ is invalid.

So a² ≈ 154.7, and AD ≈ 2.95. Let me compute AD more precisely.

AD² = 36[-1 + 96(3 - √3)/a²]

With a² = u₁ ≈ 154.7:
96(3 - √3) = 96(3 - 1.732) = 96 · 1.268 = 121.7
96(3 - √3)/a² = 121.7/154.7 = 0.787
AD² = 36(-1 + 0.787) = 36(-0.213) = -7.67

That's negative! Something's wrong.

Let me recheck. Let me recompute AD numerically.

A = (0, 10.77), D = (-1.64, 8.32)
AD = √(1.64² + (10.77-8.32)²) = √(2.69 + 6.00) = √8.69 ≈ 2.948

AD² ≈ 8.69

But my formula gives -7.67. Let me recheck the formula.

AD² = 36(c - s)² + 36c²(1 - √3)²

c = 0.557, s = 0.830
(c - s)² = (-0.273)² = 0.0745
c²(1 - √3)² = 0.310 · (1 - 1.732)² = 0.310 · 0.536 = 0.166

AD² = 36(0.0745 + 0.166) = 36 · 0.241 = 8.67 ✓

OK so the formula is right, but I made an algebra error somewhere. Let me redo.

AD² = 36[1 - 2cs + c²(4 - 2√3)]

cs = 1 - 48/a² = 1 - 48/154.7 = 1 - 0.310 = 0.690
c² = 48/a² = 0.310

AD² = 36[1 - 2(0.690) + 0.310(4 - 2·1.732)]
= 36[1 - 1.380 + 0.310(4 - 3.464)]
= 36[1 - 1.380 + 0.310 · 0.536]
= 36[1 - 1.380 + 0.166]
= 36[-0.214]
= -7.7

But numerically it should be 8.67. So there's an error in my algebra. Let me recheck.

AD² = 36[(c-s)² + c²(1-√3)²]

(c-s)² = c² - 2cs + s² = 1 - 2cs (since c² + s² = 1)

So AD² = 36[1 - 2cs + c²(1-√3)²]

(1-√3)² = 1 - 2√3 + 3 = 4 - 2√3. ✓

cs = 0.557 · 0.830 = 0.462, not 0.690!

Let me recompute cs. cs = (4√3/a)(a√3/12 - 12/a) = 4√3 · √3/12 - 4√3 · 12/a² = 4·3/12 - 48√3/a² = 1 - 48√3/a²

I had 48/a² before, but it should be 48√3/a²! Let me redo.

cs = 1 - 48√3/a²

With a² = 154.7: 48√3/154.7 = 83.14/154.7 = 0.537. cs = 1 - 0.537 = 0.463 ✓

c² = (4√3/a)² = 48/a²

AD² = 36[1 - 2(1 - 48√3/a²) + (48/a²)(4 - 2√3)]
= 36[1 - 2 + 96√3/a² + 192/a² - 96√3/a²]
= 36[-1 + 192/a²]

The √3 terms cancel! 

AD² = 36[-1 + 192/a²] = 36[192/a² - 1]

From our equation: 192/a² = 1 + 2√3 - a²/48

AD² = 36[1 + 2√3 - a²/48 - 1] = 36[2√3 - a²/48] = 72√3 - 36a²/48 = 72√3 - 3a²/4

Hmm, still depends on a². Let me use the exact value of a².

u = a² = 24(1 + 2√3) + 24√(4√3 - 3) (taking the + root)

Wait, let me recheck which root. u₁ ≈ 154.7, u₂ ≈ 59.58.

24(1 + 2√3) = 24(1 + 3.464) = 24 · 4.464 = 107.14
24√(4√3 - 3) = 24√(6.928 - 3) = 24√3.928 = 24 · 1.982 = 47.57

u₁ = 107.14 + 47.57 = 154.7 ✓
u₂ = 107.14 - 47.57 = 59.58 ✓

So a² = 24(1 + 2√3) + 24√(4√3 - 3).

AD² = 72√3 - (3/4)·a² = 72√3 - (3/4)·24(1 + 2√3) - (3/4)·24√(4√3 - 3)
= 72√3 - 18(1 + 2√3) - 18√(4√3 - 3)
= 72√3 - 18 - 36√3 - 18√(4√3 - 3)
= 36√3 - 18 - 18√(4√3 - 3)
= 18(2√3 - 1 - √(4√3 - 3))

Let me compute numerically: 2√3 ≈ 3.464, √(4√3-3) ≈ 1.982
= 18(3.464 - 1 - 1.982) = 18 · 0.482 = 8.68 ✓

So AD = √(18(2√3 - 1 - √(4√3 - 3)))

This doesn't simplify to a nice number. Let me reconsider—maybe I have the geometry wrong.

Hmm, wait. Let me reconsider the problem. "G on AD" — maybe D is a vertex of the triangle? Let me re-read.

"The square DEFG is contained in equilateral triangle ABC, with E on AC, G on AD, and F as the midpoint of BC."

Hmm, if D is a vertex of the triangle, then the triangle would be ABCD? No, it's triangle ABC. So D is not a vertex of the triangle. D is a vertex of the square.

But "G on AD" — AD is a segment from A to D where D is a vertex of the square. That's what I had.

Wait, but maybe I have the ordering of the square wrong. Let me reconsider. Maybe the square is labeled D-E-F-G but not necessarily in that cyclic order. Actually, by convention DEFG means the vertices in order, so DE, EF, FG, GD are sides.

Hmm, but the answer not being clean is suspicious for a competition problem. Let me reconsider.

Actually, wait. Let me reconsider the problem. Maybe "G on AD" means G is on segment AD where D is a vertex of the triangle. But the triangle is ABC, so there's no D vertex. Unless... the problem means something else.

Let me re-read: "The square DEFG is contained in equilateral triangle ABC, with E on AC, G on AD, and F as the midpoint of BC."

Hmm, what if D is on AB? The square DEFG has D on AB, E on AC, F on BC (midpoint), and G on AD. But AD would be from A to D where D is on AB... that doesn't make sense because AD would be part of AB.

Wait, actually, maybe D is on AB and G is on AD meaning G is on the segment from A to D (which is part of AB). Let me reconsider.

If D is on AB, E is on AC, F is on BC (midpoint), and G is on AD (part of AB), then the square DEFG has:
- D on AB
- E on AC
- F on BC (midpoint)
- G on AB (between A and D)

But then both D and G are on AB, and the square has side GD on AB. That could work!

Let me reconsider. Square DEFG with vertices in order D, E, F, G. Sides: DE, EF, FG, GD.

If D and G are both on AB (with G between A and D), then side GD lies along AB. E is on AC, F is on BC.

This makes more geometric sense! The square has one side (GD) on AB, and the opposite side (EF) connecting AC to BC, with F at the midpoint of BC.

Let me redo with this interpretation.

Place the equilateral triangle with:
B = (0, 0), C = (a, 0), A = (a/2, a√3/2).

F = midpoint of BC = (a/2, 0).

AB goes from A = (a/2, a√3/2) to B = (0, 0). Direction: (-a/2, -a√3/2), unit: (-1/2, -√3/2).

Let D be on AB and G be on AB with GD = 6 (side of square). The square DEFG has GD on AB.

Let me parameterize. Let G be at distance t from A along AB, and D at distance t + 6 from A along AB (since GD = 6 and they're on the same line AB, with G closer to A).

G = A + t·(-1/2, -√3/2) = (a/2 - t/2, a√3/2 - t√3/2)
D = A + (t+6)·(-1/2, -√3/2) = (a/2 - (t+6)/2, a√3/2 - (t+6)√3/2)

The square DEFG: from D to E to F to G. The side DE is perpendicular to GD (which is along AB). The direction perpendicular to AB, pointing into the triangle (toward C), is (√3/2, -1/2) (rotating the AB direction by -90°).

Wait, AB direction is (-1/2, -√3/2). Perpendicular directions are (√3/2, -1/2) and (-√3/2, 1/2). The one pointing into the triangle (toward the interior, i.e., toward C) would be... let me check. From the midpoint of AB, the interior is toward C. Midpoint of AB = (a/4, a√3/4). C = (a, 0). Direction from midpoint to C: (3a/4, -a√3/4), roughly (positive x, negative y). So the perpendicular direction (√3/2, -1/2) points into the triangle. Good.

E = D + 6·(√3/2, -1/2) = D + (3√3, -3)
F = G + 6·(√3/2, -1/2) = G + (3√3, -3)

Wait, but in the square DEFG, going D→E→F→G, DE and GF are opposite sides (both perpendicular to GD), and EF and DG are... no. Let me think again.

Square DEFG: D→E→F→G→D. Sides DE, EF, FG, GD.
- GD is on AB (from G to D along AB)
- DE is perpendicular to GD (from D, going into the triangle)
- EF is parallel to GD (from E to F, parallel to AB but in opposite direction)
- FG is perpendicular to GD (from F back to G)

So E = D + 6·(perpendicular direction into triangle) and F = G + 6·(perpendicular direction into triangle).

E = D + (3√3, -3)
F = G + (3√3, -3)

Let me compute F:
F = G + (3√3, -3) = (a/2 - t/2 + 3√3, a√3/2 - t√3/2 - 3)

But F = (a/2, 0) (midpoint of BC). So:
a/2 - t/2 + 3√3 = a/2 → -t/2 + 3√3 = 0 → t = 6√3

a√3/2 - t√3/2 - 3 = 0 → a√3/2 - 6√3·√3/2 - 3 = 0 → a√3/2 - 9 - 3 = 0 → a√3/2 = 12 → a = 24/√3 = 8√3

So the side length of the triangle is 8√3.

Now E must be on AC. Let me verify.
E = D + (3√3, -3)
D = (a/2 - (t+6)/2, a√3/2 - (t+6)√3/2) with a = 8√3, t = 6√3.

D = (8√3/2 - (6√3+6)/2, 8√3·√3/2 - (6√3+6)√3/2)
= (4√3 - 3√3 - 3, 12 - 9 - 3√3)
= (√3 - 3, 3 - 3√3)

E = D + (3√3, -3) = (√3 - 3 + 3√3, 3 - 3√3 - 3) = (4√3 - 3, -3√3)

Now check E on AC. A = (4√3, 12), C = (8√3, 0).

Line AC: from (4√3, 12) to (8√3, 0). Direction: (4√3, -12). Parametric: (4√3 + 4√3·s, 12 - 12s) for s ∈ [0,1].

At E = (4√3 - 3, -3√3):
4√3 + 4√3·s = 4√3 - 3 → 4√3·s = -3 → s = -3/(4√3) = -√3/4

s is negative, so E is not on segment AC but on the extension beyond A. That's not right.

Hmm, so this configuration doesn't work either. Let me reconsider.

Maybe the perpendicular direction should be the other way, or D and G are swapped (D closer to A, G farther).

Let me try: D closer to A, G farther from A on AB. So D at distance t from A, G at distance t+6 from A.

D = A + t·(-1/2, -√3/2)
G = A + (t+6)·(-1/2, -√3/2)

Square DEFG: D→E→F→G. GD is from G to D (along AB toward A). DE perpendicular to GD.

The perpendicular into the triangle is still (√3/2, -1/2).

E = D + 6·(√3/2, -1/2)
F = G + 6·(√3/2, -1/2) ... wait, no. In the square, F = E + (G - D) = E + 6·(-1/2, -√3/2). Hmm, let me think more carefully.

Actually, F = G + (E - D) since EF is parallel to DG... no. Let me just use the square structure.

D→E→F→G is the square. D to E is one side, E to F is the next (perpendicular), F to G is the next (parallel to DE, opposite direction), G to D is the last (parallel to EF, opposite direction).

If GD is along AB, then DE is perpendicular to AB. Let's say DE goes into the triangle.

E = D + 6·n where n is the unit normal to AB pointing into the triangle.
F = E + 6·(unit vector along GD direction) = E + 6·(direction from G to D)

Wait, the direction from D to E is n (perpendicular to AB, into triangle). The direction from E to F should be perpendicular to DE, which is along AB. But which direction? It should be such that F to G closes the square.

F = E + 6·m where m is perpendicular to n, and m is in the direction from D to G (along AB away from A, toward B). Actually, m should be such that G = F + 6·(-n) = F - 6n, i.e., F = G + 6n. And also F = E + 6m.

So G + 6n = E + 6m → G - E = 6m - 6n. Also E = D + 6n, so G - D - 6n = 6m - 6n → G - D = 6m. So m = (G - D)/6, which is the unit vector from D to G. Good.

So if D is closer to A and G is farther (toward B):
m = direction from D to G = direction from A toward B along AB = (-1/2, -√3/2).

F = E + 6·(-1/2, -√3/2) = E + (-3, -3√3)
Also F = G + 6n = G + (3√3, -3)

Let me use F = G + (3√3, -3) and F = (a/2, 0).

G = A + (t+6)·(-1/2, -√3/2) = (a/2 - (t+6)/2, a√3/2 - (t+6)√3/2)

F = G + (3√3, -3) = (a/2 - (t+6)/2 + 3√3, a√3/2 - (t+6)√3/2 - 3) = (a/2, 0)

From x: -(t+6)/2 + 3√3 = 0 → t + 6 = 6√3 → t = 6√3 - 6

From y: a√3/2 - (t+6)√3/2 - 3 = 0 → a√3/2 - 6√3·√3/2 - 3 = 0 → a√3/2 - 9 - 3 = 0 → a = 24/√3 = 8√3

Same result. Now let me check E on AC.

D = A + t·(-1/2, -√3/2) = (a/2 - t/2, a√3/2 - t√3/2) with a = 8√3, t = 6√3 - 6.

D = (4√3 - (6√3-6)/2, 12 - (6√3-6)√3/2)
= (4√3 - 3√3 + 3, 12 - (18 - 6√3)/2)
= (√3 + 3, 12 - 9 + 3√3)
= (√3 + 3, 3 + 3√3)

E = D + (3√3, -3) = (√3 + 3 + 3√3, 3 + 3√3 - 3) = (3 + 4√3, 3√3)

Check E on AC: A = (4√3, 12), C = (8√3, 0).

Parametrize: (4√3 + 4√3·s, 12 - 12s).
x: 4√3 + 4√3·s = 3 + 4√3 → 4√3·s = 3 → s = 3/(4√3) = √3/4
y: 12 - 12·√3/4 = 12 - 3√3 = 12 - 5.196 = 6.804

But E_y = 3√3 ≈ 5.196. So 12 - 3√3 ≠ 3√3 unless 12 = 6√3, i.e., 2 = √3, which is false.

So E is NOT on AC. This configuration doesn't work either!

Hmm. So neither orientation of D, G on AB works. Let me reconsider the problem.

Maybe D is not on AB. Let me re-read the problem once more.

"The square DEFG is contained in equilateral triangle ABC, with E on AC, G on AD, and F as the midpoint of BC."

So the constraints are:
- E on AC
- G on AD (segment from A to D)
- F is midpoint of BC

D is a vertex of the square, and G is on the segment AD. So A, G, D are collinear with G between A and D (or D between A and G).

This is the first interpretation I had. Let me go back to that and check if the answer simplifies.

Actually, wait. Let me reconsider. In my first approach, I got AD² = 18(2√3 - 1 - √(4√3 - 3)). Let me check if this simplifies.

Let me see if 2√3 - 1 - √(4√3 - 3) can be written as a square.

Let 2√3 - 1 - √(4√3 - 3) = (√a - √b)² = a + b - 2√(ab) for some a, b.

Then a + b = 2√3 - 1 and 4ab = 4√3 - 3, so ab = √3 - 3/4.

Hmm, a + b = 2√3 - 1, ab = √3 - 3/4. These are roots of x² - (2√3-1)x + (√3 - 3/4) = 0.

Discriminant: (2√3-1)² - 4(√3 - 3/4) = 12 - 4√3 + 1 - 4√3 + 3 = 16 - 8√3 = 8(2 - √3).

√(8(2-√3)) = 2√(2(2-√3)) = 2√(4-2√3).

Now 4 - 2√3 = (√3 - 1)². So √(4-2√3) = √3 - 1.

So discriminant = 2(√3 - 1).

a, b = [(2√3 - 1) ± 2(√3 - 1)] / 2 = [(2√3 - 1) ± (2√3 - 2)] / 2

a = (2√3 - 1 + 2√3 - 2)/2 = (4√3 - 3)/2
b = (2√3 - 1 - 2√3 + 2)/2 = 1/2

So 2√3 - 1 - √(4√3 - 3) = (√((4√3-3)/2) - √(1/2))² = (√((4√3-3)/2) - 1/√2)²

Let me verify: (√((4√3-3)/2) - 1/√2)² = (4√3-3)/2 + 1/2 - 2·√((4√3-3)/2)·(1/√2) = (4√3-2)/2 - 2·√((4√3-3)/4) = 2√3 - 1 - √(4√3-3). ✓

So AD² = 18 · (√((4√3-3)/2) - 1/√2)²

AD = 3√2 · (√((4√3-3)/2) - 1/√2) = 3√2 · √((4√3-3)/2) - 3√2/√2 = 3√(4√3-3) - 3

So AD = 3√(4√3 - 3) - 3 = 3(√(4√3 - 3) - 1)

Let me verify numerically: 4√3 - 3 ≈ 3.928, √3.928 ≈ 1.982, AD = 3(1.982 - 1) = 3 · 0.982 = 2.946. And earlier I got AD ≈ 2.948. ✓

So AD = 3(√(4√3 - 3) - 1).

Hmm, this is still not a "clean" answer. Let me double-check whether 4√3 - 3 has a nicer form.

4√3 - 3... I don't think this simplifies further. But wait, let me reconsider whether this is a well-known competition problem. The answer 3(√(4√3-3) - 1) seems unusual.

Actually, let me reconsider the problem. Maybe I have the square orientation wrong. Let me reconsider which vertices are adjacent.

In square DEFG, the vertices in order are D, E, F, G. So:
- D is adjacent to E and G
- E is adjacent to D and F
- F is adjacent to E and G
- G is adjacent to F and D

E is on AC, F is on BC (midpoint), G is on AD.

So E and F are adjacent (side EF), F and G are adjacent (side FG), G and D are adjacent (side GD), D and E are adjacent (side DE).

G is on segment AD, so A, G, D are collinear. D is a vertex of the square not on any side of the triangle (it's inside, or on a side). E is on AC, F is on BC.

This is what I had. Let me also consider: maybe D is on AB. The problem doesn't say D is on any side, but maybe it is implicitly.

Actually, in many versions of this problem, D is on AB. Let me check: if D is on AB, G is on AD (so G is between A and D on AB), E is on AC, F is on BC.

I tried this and it didn't work. But maybe I had the wrong perpendicular direction. Let me try the other perpendicular direction (pointing outside the triangle, which doesn't make sense for a contained square) — no, that can't be.

Wait, maybe the issue is that the square isn't oriented with a side on AB. Let me reconsider.

If D is on AB and G is on AD (between A and D), then GD is along AB. But the square DEFG has GD as a side. So one side of the square is along AB. The opposite side EF connects E (on AC) to F (on BC). For this to work, EF must be parallel to AB.

I showed this leads to E not being on AC. So D is NOT on AB (at least not with this configuration).

Let me go back to my first solution. Let me re-examine it more carefully and make sure the geometry is valid.

With a = 8√3... wait no, that was the second approach. Let me go back to the first approach.

First approach: a² = 24(1 + 2√3) + 24√(4√3 - 3), a ≈ 12.44.

Let me verify all constraints:
- B = (-a/2, 0) = (-6.22, 0), C = (a/2, 0) = (6.22, 0), A = (0, a√3/2) = (0, 10.77)
- F = (0, 0) ✓ (midpoint of BC)
- E = (6 cos θ, 6 sin θ) = (3.34, 4.98)
- G = (-6 sin θ, 6 cos θ) = (-4.98, 3.34)
- D = E + G = (-1.64, 8.32)

Check E on AC: line from A(0, 10.77) to C(6.22, 0). At x = 3.34: y = 10.77(1 - 3.34/6.22) = 10.77 · 0.463 = 4.99 ✓

Check G on AD: A(0, 10.77), D(-1.64, 8.32). Parametrize: (−1.64t, 10.77 − 2.45t). At G(−4.98, 3.34): t = 4.98/1.64 = 3.04, y = 10.77 − 2.45·3.04 = 10.77 − 7.45 = 3.32 ≈ 3.34 ✓ (small rounding error)

Check square: DE = |E - D| = |(3.34 - (-1.64), 4.98 - 8.32)| = |(4.98, -3.34)| = √(24.8 + 11.16) = √35.96 ≈ 5.997 ≈ 6 ✓
EF = |F - E| = |(-3.34, -4.98)| = √(11.16 + 24.8) = √35.96 ≈ 6 ✓
FG = |G - F| = |(-4.98, 3.34)| = √(24.8 + 11.16) ≈ 6 ✓
GD = |D - G| = |(-1.64+4.98, 8.32-3.34)| = |(3.34, 4.98)| = √(11.16+24.8) ≈ 6 ✓

Check DE · EF = (4.98)(-3.34) + (-3.34)(-4.98) = -16.63 + 16.63 = 0 ✓ (perpendicular)

So the square is valid and all constraints are satisfied. The answer is AD = 3(√(4√3 - 3) - 1).

But wait, is the square contained in the triangle? Let me check if all vertices are inside or on the triangle.

D = (-1.64, 8.32): Is this inside triangle ABC? The triangle has vertices at (-6.22, 0), (6.22, 0), (0, 10.77). D at (-1.64, 8.32) should be inside. Let me check: the left side AB goes from (-6.22, 0) to (0, 10.77). At y = 8.32, x on AB = -6.22 + 6.22·(8.32/10.77) = -6.22 + 4.81 = -1.41. D has x = -1.64 < -1.41, so D is slightly OUTSIDE the triangle (to the left of AB)!

Hmm, that's a problem. The square should be contained in the triangle. Let me recheck.

Actually, let me be more precise. Let me use exact values.

a² = 24(1 + 2√3) + 24√(4√3 - 3)

Let me compute more precisely.
√3 = 1.7320508...
4√3 - 3 = 6.9282032 - 3 = 3.9282032
√(4√3 - 3) = 1.9820193...
a² = 24(1 + 3.4641016) + 24(1.9820193) = 24(4.4641016) + 47.5684632 = 107.138438 + 47.5684632 = 154.7069012
a = 12.438135...
a/2 = 6.219068
a√3/2 = 12.438135 · 0.8660254 = 10.771356...

cos θ = 4√3/a = 6.9282032/12.438135 = 0.557005
sin θ = a√3/12 - 12/a = 12.438135·1.7320508/12 - 12/12.438135 = 1.795226 - 0.964766 = 0.830460

E = (6·0.557005, 6·0.830460) = (3.34203, 4.98276)
G = (-6·0.830460, 6·0.557005) = (-4.98276, 3.34203)
D = E + G = (-1.64073, 8.32479)

Now check D inside triangle. Line AB from B(-6.219068, 0) to A(0, 10.771356).
At y = 8.32479: parameter t = 8.32479/10.771356 = 0.772866
x on AB = -6.219068 + 6.219068·0.772866 = -6.219068(1 - 0.772866) = -6.219068·0.227134 = -1.412534

D has x = -1.64073, which is less than -1.412534. So D is to the left of line AB, meaning D is OUTSIDE the triangle.

This means the square is NOT contained in the triangle! So this configuration is invalid.

Hmm. So I need to reconsider. Maybe the other root works, or maybe I have the geometry wrong.

Let me check the other root: a² = 24(1 + 2√3) - 24√(4√3 - 3) ≈ 59.57

a ≈ 7.718
cos θ = 4√3/7.718 = 6.928/7.718 = 0.8976
sin θ = 7.718·1.732/12 - 12/7.718 = 1.1135 - 1.5548 = -0.4413

sin θ < 0, so E = (6·0.8976, 6·(-0.4413)) = (5.386, -2.648). E has negative y, so it's below BC. Not on segment AC (which has y from 0 to a√3/2 ≈ 6.68). So this root is invalid.

Both roots give invalid configurations! So my setup must be wrong.

Let me reconsider the problem. Maybe I have the wrong orientation for the square. Let me try different orientations.

The square DEFG has F at the midpoint of BC. E is on AC. G is on AD. Let me consider different possible orientations of the square.

Let me try: maybe E and G are on opposite sides of F (not adjacent to F). Wait, in square DEFG, E and G are both adjacent to F (since the order is D-E-F-G, E is before F and G is after F). So EF and FG are sides of the square, both of length 6.

Hmm, but what if the labeling is D-E-F-G but not in cyclic order? That would be unusual. Let me assume the standard cyclic order.

Let me try a different orientation. Instead of E = F + 6(cos θ, sin θ) and G = F + 6(cos(θ+90°), sin(θ+90°)), let me try G = F + 6(cos(θ-90°), sin(θ-90°)).

G = (6 sin θ, -6 cos θ)
D = E + G - F = (6 cos θ + 6 sin θ, 6 sin θ - 6 cos θ)

G on AD: A, G, D collinear.

A = (0, a√3/2), G = (6 sin θ, -6 cos θ), D = (6 cos θ + 6 sin θ, 6 sin θ - 6 cos θ)

G - A = (6 sin θ, -6 cos θ - a√3/2)
D - A = (6 cos θ + 6 sin θ, 6 sin θ - 6 cos θ - a√3/2)

Cross product = 0:
6 sin θ (6 sin θ - 6 cos θ - a√3/2) - (-6 cos θ - a√3/2)(6 cos θ + 6 sin θ) = 0

= 36 sin²θ - 36 sin θ cos θ - 3a√3 sin θ - (-6 cos θ - a√3/2)(6 cos θ + 6 sin θ)

Let me expand the second part:
(-6 cos θ - a√3/2)(6 cos θ + 6 sin θ) = -36 cos²θ - 36 sin θ cos θ - 3a√3 cos θ - 3a√3 sin θ

So cross product = 36 sin²θ - 36 sin θ cos θ - 3a√3 sin θ + 36 cos²θ + 36 sin θ cos θ + 3a√3 cos θ + 3a√3 sin θ
= 36(sin²θ + cos²θ) + 3a√3 cos θ
= 36 + 3a√3 cos θ = 0

This gives cos θ = -12/(a√3), which is negative. So θ is in the second or third quadrant. Since E should be on AC (which is in the upper part), sin θ should be positive, so θ is in the second quadrant.

E on AC: 6 sin θ = √3(a/2 - 6 cos θ) → 6 sin θ + 6√3 cos θ = a√3/2 ... same as before (equation 1).

cos θ = -12/(a√3) = -4√3/a

From (1): sin θ + √3·(-4√3/a) = a√3/12 → sin θ - 12/a = a√3/12 → sin θ = a√3/12 + 12/a

sin²θ + cos²θ = 1:
(a√3/12 + 12/a)² + 48/a² = 1
3a²/144 + 2·(a√3/12)·(12/a) + 144/a² + 48/a² = 1
a²/48 + 2√3 + 192/a² = 1
a²/48 + 192/a² = 1 - 2√3

But 1 - 2√3 ≈ 1 - 3.464 = -2.464, and the left side is always positive. So no solution! This orientation doesn't work.

Let me try yet another orientation. What if the square is "flipped" — i.e., E and G are on the same side of F?

Actually, in a square DEFG, E and G are on opposite sides of F (they're both adjacent to F but on perpendicular sides). So there are only two orientations (the two I tried). The first gives a solution but D is outside the triangle; the second gives no solution.

Hmm, let me reconsider. Maybe the issue is that D being slightly outside the triangle is due to my assumption about which side of F the square is on. Let me try the first orientation but with the square on the other side (below F instead of above).

First orientation, but E = F + 6(cos θ, sin θ) with θ pointing downward. Actually, E needs to be on AC which is above BC, so E must be above the x-axis. So θ must have sin θ > 0.

Wait, actually, maybe I should consider the possibility that the square extends below BC. But the problem says the square is contained in the triangle, so all vertices must be inside or on the triangle.

Let me reconsider. Maybe D is on AB. The problem says "G on AD" — if D is on AB, then AD is a segment from A to a point D on AB, which is just part of side AB. G being on AD means G is on AB between A and D.

I tried this and got E not on AC. But let me recheck more carefully — maybe I made an error.

Let me redo with D on AB, G on AB (between A and D), E on AC, F = midpoint of BC.

B = (0,0), C = (a, 0), A = (a/2, a√3/2), F = (a/2, 0).

AB: from A(a/2, a√3/2) to B(0,0). Unit vector from A to B: (-1/2, -√3/2).

Let D be at distance d from A along AB: D = (a/2 - d/2, a√3/2 - d√3/2).
Let G be at distance d - 6 from A along AB (since GD = 6): G = (a/2 - (d-6)/2, a√3/2 - (d-6)√3/2).

Wait, GD = 6 and both on AB. If D is farther from A than G, then d_G = d - 6. But we need d ≥ 6.

The square DEFG: D→E→F→G. Side DE is perpendicular to DG (which is along AB). DE goes into the triangle.

Normal to AB pointing into triangle: The triangle interior is to the right of AB (when going from A to B). The direction from A to B is (-1/2, -√3/2). Rotating 90° clockwise (to get the right-hand normal): (-√3/2, 1/2). Hmm, let me check. If I'm going from A to B (downward-left), the interior of the triangle is to my right, which is... Let me think. A is at top, B at bottom-left, C at bottom-right. Going from A to B, the interior (where C is) is to the right. Right of direction (-1/2, -√3/2) is obtained by rotating -90°: (x,y) → (y, -x), so (-√3/2, 1/2). Let me verify: from midpoint of AB = (a/4, a√3/4), adding (-√3/2, 1/2) gives (a/4 - √3/2, a√3/4 + 1/2). Is this toward C = (a, 0)? The direction from midpoint to C is (3a/4, -a√3/4). The direction (-√3/2, 1/2) has positive y, while direction to C has negative y. So this is the wrong normal.

The correct normal (into triangle) is (√3/2, -1/2). Let me verify: from midpoint of AB, adding (√3/2, -1/2) gives (a/4 + √3/2, a√3/4 - 1/2). Direction to C is (3a/4, -a√3/4) which has positive x and negative y. (√3/2, -1/2) also has positive x and negative y. ✓

So E = D + 6·(√3/2, -1/2) = D + (3√3, -3).
F = G + 6·(√3/2, -1/2) = G + (3√3, -3).

F = (a/2, 0):
G + (3√3, -3) = (a/2, 0)
G = (a/2 - 3√3, 3)

G = (a/2 - (d-6)/2, a√3/2 - (d-6)√3/2) = (a/2 - 3√3, 3)

From x: a/2 - (d-6)/2 = a/2 - 3√3 → (d-6)/2 = 3√3 → d - 6 = 6√3 → d = 6 + 6√3

From y: a√3/2 - (d-6)√3/2 = 3 → a√3/2 - 6√3·√3/2 = 3 → a√3/2 - 9 = 3 → a√3/2 = 12 → a = 24/√3 = 8√3

Now E = D + (3√3, -3).
D = (a/2 - d/2, a√3/2 - d√3/2) = (4√3 - (6+6√3)/2, 12 - (6+6√3)√3/2)
= (4√3 - 3 - 3√3, 12 - 3√3 - 9)
= (√3 - 3, 3 - 3√3)

E = (√3 - 3 + 3√3, 3 - 3√3 - 3) = (4√3 - 3, -3√3)

E has y = -3√3 ≈ -5.196, which is negative. But AC is above the x-axis. So E is NOT on AC. ❌

What if G is farther from A than D? I.e., D is between A and G on AB.

D at distance d from A, G at distance d + 6 from A.

D = (a/2 - d/2, a√3/2 - d√3/2)
G = (a/2 - (d+6)/2, a√3/2 - (d+6)√3/2)

Square DEFG: D→E→F→G. Now going from D to G is away from A (toward B). The side DE is perpendicular to DG.

E = D + 6·(√3/2, -1/2) = D + (3√3, -3)
F = G + 6·(√3/2, -1/2) = G + (3√3, -3)

Wait, but the direction from E to F should be parallel to DG (from D to G), which is toward B, i.e., (-1/2, -√3/2). And F = E + 6·(-1/2, -√3/2) = E + (-3, -3√3). Also F = G + 6·(√3/2, -1/2) = G + (3√3, -3).

Let me check consistency: F = E + (-3, -3√3) and F = G + (3√3, -3).
E + (-3, -3√3) = G + (3√3, -3)
D + (3√3, -3) + (-3, -3√3) = G + (3√3, -3)
D + (-3, -3√3) = G
D - G = (3, 3√3)
|D - G| = √(9 + 27) = 6 ✓ (this is the side length, and direction (3, 3√3)/6 = (1/2, √3/2) which is from G to D, i.e., toward A. ✓)

F = G + (3√3, -3) = (a/2, 0)

G = (a/2 - 3√3, 3)

G = (a/2 - (d+6)/2, a√3/2 - (d+6)√3/2) = (a/2 - 3√3, 3)

From x: (d+6)/2 = 3√3 → d + 6 = 6√3 → d = 6√3 - 6

From y: a√3/2 - (d+6)√3/2 = 3 → a√3/2 - 6√3·√3/2 = 3 → a√3/2 - 9 = 3 → a = 8√3

Same as before. Now:
D = (a/2 - d/2, a√3/2 - d√3/2) = (4√3 - (6√3-6)/2, 12 - (6√3-6)√3/2)
= (4√3 - 3√3 + 3, 12 - (18 - 6√3)/2)
= (√3 + 3, 12 - 9 + 3√3)
= (3 + √3, 3 + 3√3)

E = D + (3√3, -3) = (3 + √3 + 3√3, 3 + 3√3 - 3) = (3 + 4√3, 3√3)

Check E on AC: A = (4√3, 12), C = (8√3, 0).
Line AC: parametrize as A + s(C - A) = (4√3 + 4√3s, 12 - 12s).
x: 4√3 + 4√3s = 3 + 4√3 → 4√3s = 3 → s = 3/(4√3) = √3/4
y: 12 - 12·√3/4 = 12 - 3√3

E_y should be 3√3. Is 12 - 3√3 = 3√3? → 12 = 6√3 → 2 = √3. No! ❌

So E is not on AC in this configuration either. The issue is that with a side of the square on AB, E doesn't land on AC.

So D is NOT on AB. Let me go back to the original approach where D is inside the triangle (or on another side).

The problem is that in my first approach, D ended up slightly outside the triangle. Let me reconsider whether there's a different valid configuration.

Actually, wait. Let me reconsider the problem statement. "G on AD" — what if this means G is on segment AD where D is a vertex of the square, and A is a vertex of the triangle? That's what I had. And D ended up outside the triangle.

But the problem says the square is contained in the triangle. So maybe I need a different configuration where D is inside the triangle.

Let me think about this differently. Maybe the square is oriented such that D is inside the triangle (not on any side), E is on AC, F is on BC (midpoint), and G is on segment AD (with G between A and D, and D inside the triangle).

In my first approach, D was at (-1.64, 8.32) and the triangle's left side at that height was at x = -1.41. So D was just barely outside. This suggests maybe I need to check if there's a configuration where D is inside.

Actually, maybe I need to consider that G is between D and A (not between A and D). Or maybe D is between A and G. Let me reconsider.

"G on AD" typically means G is on the segment from A to D. So G is between A and D (or could be at an endpoint). In my first approach, I had A, G, D collinear with G between A and D (t ≈ 3.04, so G is beyond D from A... wait, let me recheck).

A = (0, 10.77), D = (-1.64, 8.32), G = (-4.98, 3.34).

The parametrization was A + t(D - A) with t = 3.04 for G. So G is beyond D from A (t > 1). This means D is between A and G, not G between A and D.

So "G on AD" with G beyond D doesn't satisfy "G on segment AD" (if we interpret AD as the segment from A to D). Unless "AD" refers to the line, not the segment.

Hmm, but in geometry problems, "G on AD" usually means G is on segment AD (between A and D). Let me try the configuration where G is between A and D.

In my first approach, the collinearity condition gave me a unique solution (up to the quadratic). The issue is that in that solution, G is beyond D. Let me see if the other orientation or a different setup gives G between A and D.

Actually, let me reconsider. Maybe I should set up the problem differently. Let me consider that D is inside the triangle, G is between A and D on segment AD, E is on AC, F is on BC.

Let me use a coordinate-free approach. Let me place F at the midpoint of BC. The square DEFG has EF = FG = 6, with E on AC and G on segment AD.

Let me think about this more carefully using angles.

In the equilateral triangle, let me use B = (-s, 0), C = (s, 0), A = (0, s√3) where 2s is the side length. F = (0, 0).

The square DEFG has F at origin. E is on AC, G is on segment AD (D inside triangle). The square has side 6.

Let me parameterize by the angle that FE makes with the positive x-axis. Let E = (6 cos α, 6 sin α) where α is the angle of FE.

Since E is on AC (which goes from A(0, s√3) to C(s, 0)), and E is at distance 6 from F, we need E above the x-axis, so sin α > 0, and E on the right side (cos α > 0 since AC is on the right).

G is perpendicular to E from F (since EFG is a right angle at F in the square). So G = F + 6(cos(α + 90°), sin(α + 90°)) = (-6 sin α, 6 cos α) or G = F + 6(cos(α - 90°), sin(α - 90°)) = (6 sin α, -6 cos α).

For G to be on segment AD where D is inside the triangle, G should be in the upper-left part of the triangle (since A is at top and D is inside). So G = (-6 sin α, 6 cos α) (upper left) makes more sense. This is my first approach.

D = E + G = (6 cos α - 6 sin α, 6 sin α + 6 cos α).

For D to be inside the triangle, we need D to be above BC (y > 0, which is true since sin α + cos α > 0 for α ∈ (0°, 90°)) and inside the left and right sides.

For G to be between A and D (on segment AD), we need the parameter t in A + t(D - A) = G to satisfy 0 ≤ t ≤ 1.

In my numerical solution, t ≈ 3.04, so G is beyond D. For G to be between A and D, we'd need t ∈ [0, 1].

The collinearity condition gave us 3a√3 cos α = 36, i.e., cos α = 12/(a√3). And the parameter t for G on line AD:

G = A + t(D - A)
t = (G_x - A_x)/(D_x - A_x) = (-6 sin α)/(6 cos α - 6 sin α - 0) = -6 sin α/(6(cos α - sin α)) = -sin α/(cos α - sin α) = sin α/(sin α - cos α)

For t ∈ (0, 1), we need sin α > sin α - cos α > 0, i.e., cos α > 0 and sin α > cos α. So α ∈ (45°, 90°).

In my solution, cos α ≈ 0.557, sin α ≈ 0.830. sin α - cos α ≈ 0.273 > 0. t = 0.830/0.273 ≈ 3.04. This is > 1, so G is beyond D.

For t < 1: sin α/(sin α - cos α) < 1 → sin α < sin α - cos α → 0 < -cos α → cos α < 0. But we need cos α > 0 for E on AC (right side). Contradiction!

So with this orientation, G can never be between A and D (for α ∈ (45°, 90°)). G is always beyond D.

This means "G on AD" must mean G is on the line AD (or on ray AD beyond D), not necessarily on segment AD. Or perhaps "G on AD" means G is on segment AD where the segment extends from A through D, and G is between A and D but D is beyond G... no, that doesn't make sense either.

Wait, actually, re-reading: "G on AD" — in many geometry problems, especially at the competition level, "G on AD" means G is on segment AD. But if D is a vertex of the square that's inside the triangle, and G is also a vertex of the square, then G on segment AD means G is between A and D.

But we just showed that's impossible with this orientation. Let me try the other orientation: G = (6 sin α, -6 cos α).

For G to be between A and D: G = (6 sin α, -6 cos α). This has negative y (for α ∈ (0°, 90°)), so G is below the x-axis. But the triangle is above the x-axis (except for BC). So G would be outside the triangle. Not valid.

Hmm. So neither orientation gives G between A and D with all vertices inside the triangle.

Let me reconsider. Maybe "G on AD" means G is on the line segment from A to D, where D is a point such that the segment AD passes through G. In other words, A, G, D are collinear with G between A and D. But we showed this is impossible.

OR: maybe "G on AD" means G is on the ray from A through D, which includes points beyond D. In that case, my first solution works, but D is outside the triangle.

OR: maybe I'm wrong about D being outside the triangle. Let me recheck with exact computation.

Actually, let me reconsider the problem. Maybe D is on side AB. Let me re-read: "The square DEFG is contained in equilateral triangle ABC, with E on AC, G on AD, and F as the midpoint of BC."

If D is on AB, then "G on AD" means G is on segment AD, which is part of side AB (from A to D, where D is on AB). So G is on AB between A and D.

I tried this and E didn't land on AC. But wait—maybe I need to consider that the square could be tilted differently. If D is on AB and G is on AB, then GD is along AB, and the square has one side on AB. But maybe the square doesn't have a side on AB—maybe D is on AB but G is not on AB, and G is on segment AD (which goes from A into the interior to D on AB).

Wait, if D is on AB, then segment AD is part of AB. So G on AD means G is on AB. So both D and G are on AB, and GD is along AB. That's the case I tried.

Hmm, let me try yet another possibility: maybe D is on side AB, but the square is oriented so that DG is NOT a side of the square but a diagonal. Wait, in square DEFG, D and G are adjacent (connected by side GD), so GD is a side, not a diagonal.

OK let me try a completely different approach. Let me consider that maybe the problem has D on AB, and I made a computational error. Let me redo very carefully.

Setup: Equilateral triangle ABC with B = (0,0), C = (a,0), A = (a/2, a√3/2). F = (a/2, 0) (midpoint of BC).

D on AB, G on AB (between A and D), E on AC, square DEFG with side 6.

Let me use a different parameterization. Let D = (d_x, d_y) on AB. AB goes from A(a/2, a√3/2) to B(0,0). Points on AB: (a/2 · (1-t), a√3/2 · (1-t)) for t ∈ [0,1]. So D = (a/2 · (1-p), a√3/2 · (1-p)) for some p.

G is on AB between A and D, at distance 6 from D along AB. The direction from D toward A along AB is (1/2, √3/2) (unit vector). So G = D + 6·(1/2, √3/2) = D + (3, 3√3).

G = (a/2 · (1-p) + 3, a√3/2 · (1-p) + 3√3)

For G to be on segment AD (between A and D), G must be between A and D on AB. Since G = D + 6·(toward A), G is closer to A than D. So G is indeed between A and D (as long as G doesn't go past A, i.e., the distance from A to G is non-negative).

Distance from A to D = 6p (since D is at parameter p from A, and |AB| = a, so distance = pa). Wait, D = A + p·(B - A), so |AD| = p·a. And G = D + 6·(toward A), so |AG| = |AD| - 6 = pa - 6. Need pa ≥ 6.

Now, the square DEFG: D→E→F→G. DE is perpendicular to DG (along AB), pointing into the triangle. The unit normal into the triangle (perpendicular to AB, pointing right/inward) is (√3/2, -1/2).

E = D + 6·(√3/2, -1/2) = D + (3√3, -3)

E must be on AC. AC goes from A(a/2, a√3/2) to C(a, 0). Points on AC: A + q·(C - A) = (a/2 + qa/2, a√3/2 - qa√3/2) for q ∈ [0,1].

E = D + (3√3, -3) = (a/2·(1-p) + 3√3, a√3/2·(1-p) - 3)

Setting E on AC:
a/2·(1-p) + 3√3 = a/2 + qa/2 ... (i)
a√3/2·(1-p) - 3 = a√3/2 - qa√3/2 ... (ii)

From (ii): a√3/2·(1-p) - 3 = a√3/2·(1-q)
→ -3 = a√3/2·(1-q) - a√3/2·(1-p) = a√3/2·(p - q)
→ p - q = -6/(a√3) = -2√3/a ... (*)

From (i): a/2·(1-p) + 3√3 = a/2·(1+q)
→ 3√3 = a/2·(1+q) - a/2·(1-p) = a/2·(p+q)
→ p + q = 6√3/a ... (**)

From (*) and (**):
p = (6√3/a - 2√3/a)/2 = 4√3/(2a) = 2√3/a... wait: p + q = 6√3/a, p - q = -2√3/a. Adding: 2p = 4√3/a, p = 2√3/a. Subtracting: 2q = 8√3/a, q = 4√3/a.

Now F = G + 6·(√3/2, -1/2) = G + (3√3, -3).

G = D + (3, 3√3) = (a/2·(1-p) + 3, a√3/2·(1-p) + 3√3)

F = (a/2·(1-p) + 3 + 3√3, a√3/2·(1-p) + 3√3 - 3)

F = (a/2, 0):
a/2·(1-p) + 3 + 3√3 = a/2 → -a/2·p + 3 + 3√3 = 0 → ap/2 = 3 + 3√3 → ap = 6 + 6√3 ... (I)

a√3/2·(1-p) + 3√3 - 3 = 0 → a√3/2 - a√3p/2 + 3√3 - 3 = 0 → a√3/2·(1-p) = 3 - 3√3 ... (II)

From (I): p = (6 + 6√3)/a
From earlier: p = 2√3/a

So (6 + 6√3)/a = 2√3/a → 6 + 6√3 = 2√3 → 6 = 2√3 - 6√3 = -4√3. This is false!

So there's no solution with D on AB and this orientation. The square with a side on AB doesn't work.

What if the perpendicular direction is the other way (out of the triangle)? That would put the square outside, which doesn't make sense.

OK so D is definitely not on AB with a side of the square along AB. Let me go back to the original approach.

Let me reconsider the problem. Maybe "G on AD" doesn't mean what I think. Let me consider: what if D is on side AB, and G is on segment AD (where AD is a cevian from A to D on BC, not from A to D on AB)?

Wait, but D is a vertex of the square. If D is on BC, then... F is also on BC (midpoint). So both D and F are on BC. Then DF is along BC. In the square DEFG, D and F are opposite vertices (diagonal), not adjacent. So DF would be a diagonal of the square, not a side.

Let me try this! D on BC, F on BC (midpoint), so DF is along BC and is a diagonal of the square.

Square DEFG with diagonal DF along BC. D and F are opposite vertices. The diagonal of a square with side 6 is 6√2. So DF = 6√2. Since F is the midpoint of BC, D is at distance 6√2 from F along BC.

E and G are the other two vertices of the square, above and below BC. Since the square is in the triangle, E and G are above BC. Wait, in a square, if DF is a diagonal, then E and G are on opposite sides of DF. So one is above BC and one is below. But the square is contained in the triangle (above BC), so one vertex would be below BC. That doesn't work unless the square is oriented differently.

Hmm, actually, if the diagonal DF is along BC, then E and G are symmetric about BC, one above and one below. The one below would be outside the triangle. So this doesn't work.

Unless D is not on BC. Let me reconsider.

Actually, wait. Let me re-read the problem once more: "The square DEFG is contained in equilateral triangle ABC, with E on AC, G on AD, and F as the midpoint of BC."

I think the key insight I might be missing is that D is on side AB. Let me re-examine. If D is on AB, then "G on AD" means G is on the segment from A to D. Since D is on AB, the segment AD is part of side AB. So G is on AB.

The square DEFG has:
- D on AB
- G on AB (between A and D, since G is on segment AD)
- E on AC
- F on BC (midpoint)

D and G are adjacent vertices (side GD = 6), both on AB. E is on AC, F is on BC. EF is the opposite side to GD.

I showed this doesn't work because E doesn't land on AC. But let me double-check by trying a different approach.

Actually, wait. I think the issue might be that the square doesn't have a side on AB. What if D is on AB, but G is NOT on AB? G is on segment AD, where AD is a line from A to D. If D is on AB, then AD is along AB, so G on AD means G is on AB. So G must be on AB if D is on AB.

Unless D is not on a side of the triangle at all. Let me consider D inside the triangle.

Going back to my first approach: D is inside (or near) the triangle, G is on line AD (beyond D from A), E is on AC, F is on BC. The issue was D being slightly outside the triangle.

Let me re-examine whether D is actually outside. Let me be very precise.

a² = 24(1 + 2√3) + 24√(4√3 - 3)

Let me compute with high precision.
√3 = 1.7320508075688772
4√3 - 3 = 3.928203230275509
√(4√3 - 3) = 1.9820193252335276
1 + 2√3 = 4.464101615137754
24(1 + 2√3) = 107.13843876330610
24√(4√3 - 3) = 47.568463805604662
a² = 154.70690256891076
a = 12.43813542340481
a/2 = 6.219067711702405
a√3/2 = 10.77135649692708

cos θ = 4√3/a = 6.9282032302755092/12.43813542340481 = 0.5570057176142436
sin θ = a√3/12 - 12/a = 1.7952259416154513 - 0.9647661305727987 = 0.8304598110426526

E = (3.3420343056854616, 4.9827588662559156)
G = (-4.9827588662559156, 3.3420343056854616)
D = (-1.640724560570454, 8.324793171941377)

Line AB: from B(-6.219067711702405, 0) to A(0, 10.77135649692708).
At y = 8.324793171941377:
t = 8.324793171941377 / 10.77135649692708 = 0.7728659089
x = -6.219067711702405 * (1 - 0.7728659089) = -6.219067711702405 * 0.2271340911 = -1.412534...

D_x = -1.6407, but the boundary is at x = -1.4125. So D is at x = -1.64, which is more negative than -1.41, meaning D is to the LEFT of line AB, hence OUTSIDE the triangle.

The difference is about 0.23, which is significant. So D is definitely outside.

Hmm, so the configuration I found has D outside the triangle. This means either:
1. My setup is wrong (wrong orientation of the square)
2. The problem has a different configuration than what I'm imagining

Let me try the other orientation of the square: G = F + 6(cos(α - 90°), sin(α - 90°)) = (6 sin α, -6 cos α).

This puts G below the x-axis (for α ∈ (0°, 90°)), which is outside the triangle. Not valid.

What if α is in a different range? If α ∈ (90°, 180°), then E = (6 cos α, 6 sin α) has cos α < 0, so E is on the left side. But AC is on the right side. So E wouldn't be on AC.

What if E is on the extension of AC? No, the problem says E on AC (the segment).

I'm stuck. Let me try a completely different approach. Let me consider that maybe the square is not oriented with F as a "corner" in the way I think.

Actually, wait. Let me reconsider the labeling. In square DEFG, maybe the vertices go D, E, F, G but not necessarily in the order I assumed. What if the square is labeled such that D and F are adjacent, not opposite?

In a square DEFG, the standard convention is that the vertices are listed in order (either clockwise or counterclockwise). So D-E, E-F, F-G, G-D are the sides, and D-F, E-G are the diagonals.

But what if the problem uses a non-standard labeling? For instance, what if D-E-F-G are listed such that D and F are adjacent? That would be unusual, but let me consider it.

If D and F are adjacent (side DF), and E and G are the other two vertices, then:
- D on AB (possibly), F on BC (midpoint), E on AC, G on AD.

DF is a side of the square, length 6. D on AB, F on BC. E on AC, G on AD.

Let me try this. B = (0,0), C = (a,0), A = (a/2, a√3/2), F = (a/2, 0).

D on AB: D = (a/2·(1-p), a√3/2·(1-p)) for some p ∈ [0,1].

DF = 6: |D - F|² = (a/2·(1-p) - a/2)² + (a√3/2·(1-p))² = (a/2)²·p² + (a√3/2)²·(1-p)² = a²p²/4 + 3a²(1-p)²/4 = a²/4·(p² + 3(1-p)²) = 36

So a²(p² + 3(1-p)²) = 144.

Now, the square with side DF: E and G are the other two vertices. The square DEFG with D, E, F, G in order means D-E-F-G, so DE and EF are sides, and DF is a diagonal. Wait, no. If D-E-F-G is the order, then D-F is a diagonal, not a side.

Hmm, I keep going back and forth. Let me be definitive: in square DEFG listed in order, the sides are DE, EF, FG, GD. The diagonals are DF and EG. So D and F are opposite vertices.

So DF is a diagonal, not a side. The diagonal has length 6√2 (if side is 6). But the problem says DE = 6, and DE is a side, so the side length is 6 and the diagonal is 6√2.

OK so with D and F as opposite vertices (diagonal DF), and DF = 6√2:

D on AB, F = (a/2, 0) on BC. DF = 6√2.

a²/4·(p² + 3(1-p)²) = 72

E and G are the other two vertices, on opposite sides of diagonal DF. E on AC, G on AD.

The midpoint of DF is M = (D + F)/2. The direction from M to E (and G) is perpendicular to DF, with length 6 (half the diagonal times... wait, no. In a square with diagonal d, the distance from the center to a vertex is d/2. The other two vertices are at distance d/2 from the center, perpendicular to the diagonal.

So E = M + 3√2 · n and G = M - 3√2 · n, where n is the unit vector perpendicular to DF.

Wait, the diagonal is 6√2, so half-diagonal is 3√2. The other two vertices are at distance 3√2 from the center, perpendicular to DF.

Let me compute. D = (a/2·(1-p), a√3/2·(1-p)), F = (a/2, 0).

DF direction: F - D = (a/2 - a/2·(1-p), -a√3/2·(1-p)) = (ap/2, -a√3(1-p)/2).

|DF| = a/2·√(p² + 3(1-p)²) = 6√2, so a²(p² + 3(1-p)²)/4 = 72.

Unit vector along DF: (p, -√3(1-p)) / √(p² + 3(1-p)²).

Perpendicular: (√3(1-p), p) / √(p² + 3(1-p)²).

M = ((a/2·(1-p) + a/2)/2, a√3/2·(1-p)/2) = (a(2-p)/4, a√3(1-p)/4).

E = M + 3√2 · (√3(1-p), p) / √(p² + 3(1-p)²)

G = M - 3√2 · (√3(1-p), p) / √(p² + 3(1-p)²)

This is getting complicated. Let me try a numerical approach. Let me pick a value of a and p and see if I can satisfy all constraints.

Actually, this is getting very complicated. Let me step back and think about the problem differently.

Let me reconsider the original problem. Perhaps D is on AB after all, and I need to be more careful.

Actually, you know what, let me reconsider the problem from scratch. Let me re-read it:

"The square DEFG is contained in equilateral triangle ABC, with E on AC, G on AD, and F as the midpoint of BC. Find AD if DE=6."

What if D is on AB? Then:
- D on AB
- E on AC
- F on BC (midpoint)
- G on AD (segment from A to D, which is part of AB)

The square DEFG (in order) has sides DE, EF, FG, GD. D and G are on AB (since G is on AD ⊂ AB). So side GD is on AB.

E is on AC, F is on BC. The opposite side to GD is EF.

I showed this leads to a contradiction. But let me try once more very carefully, because this seems like the most natural configuration.

B = (0,0), C = (a,0), A = (a/2, h) where h = a√3/2. F = (a/2, 0).

Let me place D on AB at distance x from B (so D divides AB with BD = x, AD = a - x). D = B + (x/a)(A - B) = (x/a)(a/2, h) = (x/2, xh/a) = (x/2, x√3/2).

G on AD, with GD = 6. G is between A and D, at distance 6 from D toward A. Direction from D to A: (A - D)/|A - D| = ((a/2 - x/2), (h - x√3/2))/(a - x) = ((a - x)/2, (a√3/2 - x√3/2))/(a-x) = (1/2, √3/2). (This is the unit vector from B to A, which makes sense since D is on AB.)

G = D + 6·(1/2, √3/2) = (x/2 + 3, x√3/2 + 3√3).

For G to be on segment AD (between A and D), we need |AG| ≤ |AD|, i.e., |AD| ≥ 6, i.e., a - x ≥ 6.

Now, the square DEFG: side GD is along AB (direction (1/2, √3/2)). The perpendicular direction (into the triangle) is (√3/2, -1/2) (as I computed before).

E = D + 6·(√3/2, -1/2) = (x/2 + 3√3, x√3/2 - 3).

F = G + 6·(√3/2, -1/2) = (x/2 + 3 + 3√3, x√3/2 + 3√3 - 3).

F = (a/2, 0):
x/2 + 3 + 3√3 = a/2 → a = x + 6 + 6√3 ... (I)
x√3/2 + 3√3 - 3 = 0 → x√3/2 = 3 - 3√3 → x = (3 - 3√3)·2/√3 = (6 - 6√3)/√3 = 6/√3 - 6 = 2√3 - 6... 

Wait, 6/√3 = 2√3. So x = 2√3 - 6 ≈ 3.464 - 6 = -2.536. Negative! x is the distance from B to D along AB, so it must be non-negative. This is impossible.

So with the perpendicular direction (√3/2, -1/2) (into the triangle), we get x < 0, which is invalid.

Let me try the other perpendicular direction: (-√3/2, 1/2) (out of the triangle, toward the left).

E = D + 6·(-√3/2, 1/2) = (x/2 - 3√3, x√3/2 + 3).
F = G + 6·(-√3/2, 1/2) = (x/2 + 3 - 3√3, x√3/2 + 3√3 + 3).

F = (a/2, 0):
x/2 + 3 - 3√3 = a/2 → a = x + 6 - 6√3 ... (I')
x√3/2 + 3√3 + 3 = 0 → x√3/2 = -3 - 3√3 → x = (-3 - 3√3)·2/√3 = -6/√3 - 6 = -2√3 - 6 < 0.

Also negative. So neither perpendicular direction works with D on AB and G between A and D.

What if G is on the other side of D (i.e., D is between A and G)? Then G = D - 6·(1/2, √3/2) = (x/2 - 3, x√3/2 - 3√3). But then G is farther from A than D, so G is not on segment AD (it's on the extension beyond D). Also, G might be outside the triangle.

Hmm. It really seems like D on AB doesn't work. Let me try D on BC.

D on BC: D = (d, 0) for some d ∈ [0, a]. F = (a/2, 0) is also on BC. In square DEFG, D and F are opposite vertices (diagonal). So DF is a diagonal of the square.

|DF| = |d - a/2| = 6√2 (diagonal of square with side 6).

So d = a/2 + 6√2 or d = a/2 - 6√2.

The other two vertices E and G are above and below BC (since the diagonal is along BC). One of them is above (inside the triangle) and one below (outside). For the square to be contained in the triangle, we need both E and G inside, but one is below BC. So this doesn't work.

Unless the square is tilted. But if D and F are both on BC, the diagonal DF is along BC, and E, G are symmetric about BC. One is above, one below. Can't both be in the triangle.

So D is not on BC either. Let me try D on AC. But E is on AC, and D on AC would mean both D and E on AC. In the square, D and E are adjacent (side DE = 6). So DE is along AC. Then the square has one side on AC.

D on AC, E on AC, DE = 6 along AC. F on BC (midpoint), G on AD.

Let me try this. A = (a/2, a√3/2), C = (a, 0). Direction from A to C: (a/2, -a√3/2)/a = (1/2, -√3/2).

Let E be at distance e from A along AC: E = A + e·(1/2, -√3/2) = (a/2 + e/2, a√3/2 - e√3/2).
D is at distance e + 6 from A along AC (or e - 6). Let's say D = A + (e+6)·(1/2, -√3/2) = (a/2 + (e+6)/2, a√3/2 - (e+6)√3/2).

Wait, but G is on AD. If D is on AC, then AD is part of AC. So G is on AC. But G is a vertex of the square, and in the square DEFG, G is adjacent to D and F. If G is on AC, then... GD is a side of the square along AC. But DE is also along AC. In a square, DE and GD are adjacent sides, perpendicular to each other. They can't both be along AC. Contradiction.

Unless D is between E and G on AC, but DE and GD are perpendicular—impossible if both on the same line.

So D is not on AC.

OK so D is not on any side of the triangle. D is inside the triangle. Let me go back to my first approach and accept that "G on AD" might mean G is on the line through A and D (not necessarily the segment), or that G is on the ray from A through D.

Actually, wait. Let me reconsider. In the problem, "G on AD" — what if this means G is on segment AD where D is inside the triangle, and G is between A and D? We showed this is impossible with the square orientation I tried. But maybe there's a different square orientation.

Let me think about this more carefully. The square DEFG has F at the midpoint of BC. E is on AC. G is on segment AD (G between A and D, D inside triangle).

In the square, F is adjacent to E and G. So FE and FG are sides of the square, both length 6, perpendicular.

E is on AC (right side of triangle), G is on segment AD (going from top vertex A into the interior). So E is to the right and G is to the upper-left (roughly).

Let me set up: B = (-s, 0), C = (s, 0), A = (0, s√3), F = (0, 0).

E on AC: E = (6 cos α, 6 sin α) for some angle α (E is at distance 6 from F, on AC which is on the right side, so cos α > 0, sin α > 0).

G is perpendicular to E from F: G = (-6 sin α, 6 cos α) (upper left) or G = (6 sin α, -6 cos α) (lower right). For G to be in the upper-left (toward A), we need G = (-6 sin α, 6 cos α).

D = E + G = (6 cos α - 6 sin α, 6 sin α + 6 cos α).

G on segment AD means A, G, D collinear with G between A and D.

We showed t = sin α/(sin α - cos α) and for t ∈ (0,1), we need cos α < 0, contradicting E on AC.

So G = (-6 sin α, 6 cos α) can't be between A and D.

What about G = (6 sin α, -6 cos α)? This is lower right, below BC. Not in the triangle.

So with F at the midpoint of BC and the standard square orientation, G cannot be between A and D. This means either:
1. "G on AD" means G is on line AD (not segment), or
2. The square has a different orientation than what I'm considering.

For (2), what if the square is "flipped" so that E and G are on the same side of F? In a square, E and G are on perpendicular sides from F, so they can't be on the same side. Unless the labeling is different.

Wait, what if the square is labeled D, E, F, G but in a different order? Like D, E, F, G going around but starting from a different vertex? No, the order D-E-F-G is fixed.

Hmm, let me try yet another possibility. What if the square is oriented so that F is not at a "natural" corner? Like, what if the square is rotated such that F is at the midpoint of BC but the square extends in a different direction?

Actually, I've been assuming F is a vertex of the square, which it is (since DEFG are the vertices). And E, G are adjacent to F. The two orientations I tried are the
