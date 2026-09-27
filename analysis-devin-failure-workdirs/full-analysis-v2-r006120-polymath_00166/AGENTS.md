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
  <problem_id>polymath_00166</problem_id>
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

Let \( \triangle ABC \) be an acute triangle with circumcenter \( O \) and orthocenter \( H \). Let \( E \) be the intersection of \( BH \) and \( AC \), and let \( M \) and \( N \) be the midpoints of \( HB \) and \( HO \), respectively. Let \( I \) be the incenter of \( \triangle AEM \) and \( J \) be the intersection of \( ME \) and \( AI \). If \( AO = 20 \), \( AN = 17 \), and \(\angle ANM = 90^\circ\), then \(\frac{AI}{AJ} = \frac{m}{n}\) for relatively prime positive integers \( m \) and \( n \). Compute \( 100m + n \).

## Standard Solution

Since \(\angle AEB = \frac{\pi}{2}\), we have that \( AENM \) is cyclic. Let \(\omega\) be the nine-point circle of \(\triangle ABC\). Note that \( N \) is the center of \(\omega\) and \( M \) and \( E \) are on \(\omega\). The radius of \(\omega\) is \(\frac{R}{2}\), where \( R \) is the circumradius of \(\triangle ABC\). Considering the concyclic points \( A, E, N, M \), we have \( MN = NE = \frac{R}{2} = 10 \) and \( AN = 17 \). Since \( AN > MN = NE \), it follows that \( A \) lies on the arc \( ME \) not containing \( N \) on \((AENM)\).

Applying Ptolemy's Theorem to cyclic quadrilateral \( AENM \), we have:
\[
17 \cdot EM = AN \cdot EM = AE \cdot NM + AM \cdot NE = 10(AE + AM).
\]

By the angle bisector theorem on \(\triangle AME\), \(\frac{MJ}{JE} = \frac{MA}{AE}\), so \( MJ = \frac{AM \cdot ME}{AM + AE} \).

By the angle bisector theorem on \(\triangle MAJ\), \(\frac{AI}{IJ} = \frac{AM}{MJ} = \frac{AM + AE}{ME} = \frac{17}{10}\). Thus,
\[
\frac{AI}{AJ} = \frac{AM + AE}{AM + AE + ME} = \frac{17}{27}.
\]

Therefore, \( 100m + n = 1727 \).
\(\boxed{1727}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this geometry problem step by step.

We have an acute triangle ABC with circumcenter O and orthocenter H. E is the intersection of BH and AC (so E is the foot of the altitude from B to AC). M is the midpoint of HB, N is the midpoint of HO. I is the incenter of triangle AEM, and J is the intersection of ME and AI. Given AO = 20, AN = 17, and ∠ANM = 90°, find AI/AJ = m/n and compute 100m + n.

Let me set up coordinates. Let me think about the key relationships.

First, let me recall some facts:
- O is circumcenter, H is orthocenter
- E is foot of altitude from B to AC (since E is on BH ∩ AC, and BH is the altitude from B)
- M is midpoint of HB
- N is midpoint of HO

Key fact: The midpoint of HB and the midpoint of HO... Let me think about the nine-point circle. The nine-point circle passes through the midpoints of the sides, the feet of the altitudes, and the midpoints of the segments from vertices to orthocenter. So M (midpoint of HB) is on the nine-point circle, and E (foot of altitude from B) is on the nine-point circle. N (midpoint of HO) is the center of the nine-point circle!

So N is the nine-point center. The nine-point circle has center N (midpoint of OH) and radius R/2 where R is the circumradius.

Given AO = 20, so R = 20. The nine-point circle has radius 10.

AN = 17 and ∠ANM = 90°.

Let me set up coordinates. Let me place N at the origin.

Actually, let me think about what we know. N is the nine-point center. M is on the nine-point circle (midpoint of HB), so NM = R/2 = 10. E is on the nine-point circle (foot of altitude), so NE = 10.

∠ANM = 90° means AN ⊥ NM. AN = 17, NM = 10.

Let me set up coordinates with N at origin. Let A be along some direction. Since ∠ANM = 90°, let me place A and M conveniently.

Let me put N at origin. Let A = (17, 0) (so AN = 17 along x-axis). Then since ∠ANM = 90°, NM is perpendicular to NA, so M = (0, 10) or (0, -10). Let's say M = (0, 10) (NM = 10 since M on nine-point circle).

Now, M is the midpoint of HB. So H + B = 2M = (0, 20), thus B = (0, 20) - H.

N is the midpoint of HO. So H + O = 2N = (0, 0), thus O = -H.

Also, AO = 20, so |A - O| = 20. A = (17, 0), O = -H, so |(17, 0) - (-H)| = |(17 + H_x, H_y)| = 20.

Let H = (h_x, h_y). Then O = (-h_x, -h_y).
- AO = 20: (17 + h_x)² + h_y² = 400
- B = (0, 20) - H = (-h_x, 20 - h_y)

Now, E is the foot of the altitude from B to AC. E is on line BH (which is the altitude from B) and on line AC.

Since H is the orthocenter, BH ⊥ AC. The line BH passes through B and H.

Also, E is on the nine-point circle, so NE = 10, i.e., |E| = 10 (since N is origin).

Let me also use the fact that O is the circumcenter, so OA = OB = OC = 20.

OB = 20: |B - O| = |(-h_x, 20 - h_y) - (-h_x, -h_y)| = |(0, 20)| = 20. ✓

Great, so OB = 20 is automatically satisfied! That's a nice check.

Now I need to find C. C is on the circumcircle (|C - O| = 20) and on line AC, and BH ⊥ AC.

Let me think about this differently. Let me use the constraint that E is on the nine-point circle and E is the foot of the altitude from B.

Actually, let me use coordinates more carefully. We have:
- N = (0, 0) (nine-point center)
- A = (17, 0)
- M = (0, 10)
- H = (h_x, h_y), O = (-h_x, -h_y)
- B = (-h_x, 20 - h_y)
- Constraint: (17 + h_x)² + h_y² = 400

E is the foot of altitude from B to AC. E is on line BH and on line AC. Also |E| = 10 (on nine-point circle).

Line BH: passes through B = (-h_x, 20 - h_y) and H = (h_x, h_y).
Direction of BH: H - B = (2h_x, 2h_y - 20) = 2(h_x, h_y - 10).

Since BH ⊥ AC, the direction of AC is perpendicular to (h_x, h_y - 10), so direction of AC is (h_y - 10, -h_x) (or its negative).

A = (17, 0) is on line AC. So line AC: (17, 0) + t(h_y - 10, -h_x).

E is on this line and on line BH.

Line BH: B + s(H - B) = (-h_x, 20 - h_y) + s(2h_x, 2h_y - 20).

Let me parametrize. E = B + s(H - B) for some s. Since E is the foot of the altitude, and H is the orthocenter, E is between B and H (for acute triangle, the orthocenter is inside, and E is the foot on AC).

E = (-h_x + 2s·h_x, 20 - h_y + s(2h_y - 20)) = (h_x(2s - 1), 20 - h_y + 2s(h_y - 10))
= (h_x(2s - 1), 20 - h_y + 2s·h_y - 20s) = (h_x(2s - 1), 20(1 - s) + h_y(2s - 1))

Let u = 2s - 1, so s = (u+1)/2, 1 - s = (1-u)/2.
E = (h_x·u, 20·(1-u)/2 + h_y·u) = (h_x·u, 10(1-u) + h_y·u) = (h_x·u, 10 - 10u + h_y·u) = (h_x·u, 10 + u(h_y - 10))

|E|² = h_x²·u² + (10 + u(h_y - 10))² = 100

h_x²·u² + 100 + 20u(h_y - 10) + u²(h_y - 10)² = 100

u²(h_x² + (h_y - 10)²) + 20u(h_y - 10) = 0

u[u(h_x² + (h_y - 10)²) + 20(h_y - 10)] = 0

So u = 0 (giving E = (0, 10) = M, which would mean E = M, unlikely) or:
u = -20(h_y - 10) / (h_x² + (h_y - 10)²)

If u = 0, then E = M = (0, 10). That would mean the foot of the altitude from B is the midpoint of HB, which would mean B = E, contradiction. So we take the other solution.

Let me denote D = h_x² + (h_y - 10)². Then u = -20(h_y - 10)/D.

E = (h_x·u, 10 + u(h_y - 10))

E_x = h_x · (-20(h_y - 10)/D) = -20·h_x·(h_y - 10)/D
E_y = 10 + (-20(h_y - 10)/D)(h_y - 10) = 10 - 20(h_y - 10)²/D

Now, E must also be on line AC. Line AC passes through A = (17, 0) with direction (h_y - 10, -h_x).

So E = A + t(h_y - 10, -h_x) for some t.
E_x = 17 + t(h_y - 10)
E_y = -t·h_x

From E_y = -t·h_x: t = -E_y/h_x = -(10 - 20(h_y-10)²/D)/h_x

From E_x = 17 + t(h_y - 10):
-20·h_x·(h_y - 10)/D = 17 + (-(10 - 20(h_y-10)²/D)/h_x)·(h_y - 10)

-20·h_x·(h_y - 10)/D = 17 - (h_y - 10)(10 - 20(h_y-10)²/D)/h_x

-20·h_x·(h_y - 10)/D = 17 - (h_y - 10)·10/h_x + 20(h_y-10)³/(D·h_x)

This is getting complicated. Let me try a different approach.

Let me use the constraint (17 + h_x)² + h_y² = 400 and try to find h_x, h_y.

Actually, maybe I should use additional constraints. We need C to be on the circumcircle and on line AC. Let me think about what other constraints we have.

Actually, we have the constraint that BH ⊥ AC, and E is the foot. But we also need C to exist on the circumcircle such that the triangle is valid. Let me think about whether the constraints so far determine the triangle.

We have:
- A = (17, 0), O = (-h_x, -h_y), R = 20
- (17 + h_x)² + h_y² = 400 (AO = 20)
- B = (-h_x, 20 - h_y)
- E is foot of altitude from B to AC, E on nine-point circle (|E| = 10)

The constraint that E is on AC and E is on BH and |E| = 10 gives us one equation (the u equation above). But we also need E to be on line AC, which I was deriving.

Actually, E is automatically on line BH (by construction). The constraint that E is on line AC is the additional one. And |E| = 10 is the nine-point circle constraint. But actually, E being the foot of the altitude from B is automatically on the nine-point circle, so |E| = 10 should be automatic given the geometry. Let me reconsider.

Wait, is that true? The foot of the altitude is always on the nine-point circle. So |E| = 10 is automatic. So the constraint |E| = 10 doesn't give us new information—it's automatically satisfied.

So the real constraints are:
1. (17 + h_x)² + h_y² = 400 (AO = 20)
2. E is on line AC (which is perpendicular to BH through A)

But constraint 2 is also automatically satisfied because E is the foot of the altitude from B to AC, and AC is the line through A perpendicular to BH. So E is on AC by definition.

Hmm, so it seems like we have a one-parameter family of triangles. We need another constraint. Let me re-read the problem.

Oh wait, I think I need to be more careful. The problem says E is the intersection of BH and AC. In a triangle, BH is the altitude from B (since H is the orthocenter), and E is where this altitude meets AC. So E is the foot of the altitude from B. This is all determined by the triangle.

But we have AO = 20, AN = 17, ∠ANM = 90°. These are three constraints. Let me count degrees of freedom.

A triangle up to congruence has 3 degrees of freedom (e.g., three angles, or two sides and an angle, etc.). But we also have the placement. Let me think in terms of our coordinate system.

We placed N at origin, A at (17, 0), M at (0, 10). This uses up the rigid motion freedom (translation and rotation). We have h_x, h_y as free parameters with one constraint (17 + h_x)² + h_y² = 400. So one degree of freedom remains.

But wait, we also need C to be a specific point. C is determined by the triangle. Given A, B, O, and the constraint that O is the circumcenter and H is the orthocenter, C should be determined.

Actually, let me think again. Given A, B, and O (circumcenter), C is the other intersection of line AC with the circumcircle... no, that's circular. Let me think differently.

Given O and R, A and B are on the circumcircle. C is also on the circumcircle. The orthocenter H is determined by A, B, C. But we've already fixed H (as a free parameter). So we need H to be the orthocenter of triangle ABC.

The orthocenter condition: H is the orthocenter means AH ⊥ BC, BH ⊥ AC, CH ⊥ AB.

We already have BH ⊥ AC (this determines the direction of AC). We need AH ⊥ BC and CH ⊥ AB.

Let me use AH ⊥ BC. 
A = (17, 0), H = (h_x, h_y). Direction of AH: (h_x - 17, h_y).
B = (-h_x, 20 - h_y), C = ? Direction of BC: C - B.

Also, C is on the circumcircle: |C - O| = 20, i.e., |C + H| = 20 (since O = -H).
C is on line AC: C = A + t(h_y - 10, -h_x) for some t (direction of AC is perpendicular to BH direction (h_x, h_y - 10)).

So C = (17 + t(h_y - 10), -t·h_x).

|C + H|² = (17 + t(h_y - 10) + h_x)² + (-t·h_x + h_y)² = 400

Let me expand:
(17 + h_x + t(h_y - 10))² + (h_y - t·h_x)² = 400

Let a = 17 + h_x, b = h_y - 10 (so the constraint (17+h_x)² + h_y² = 400 becomes a² + (b+10)² = 400, i.e., a² + b² + 20b + 100 = 400, so a² + b² = 300 - 20b).

(a + tb)² + (b + 10 - ta)² = 400... wait let me redo.

h_y = b + 10, h_x = a - 17.

C = (17 + t·b, -t(a-17))
C + H = (17 + tb + a - 17, -t(a-17) + b + 10) = (a + tb, b + 10 - t(a-17))

|C + H|² = (a + tb)² + (b + 10 - t(a-17))² = 400

Hmm, this is getting messy. Let me try a numerical approach. Let me parameterize h_x using the constraint.

(17 + h_x)² + h_y² = 400

Let 17 + h_x = 20 cos θ, h_y = 20 sin θ. So h_x = 20 cos θ - 17, h_y = 20 sin θ.

Then O = (17 - 20 cos θ, -20 sin θ), A = (17, 0).

Let me also use the orthocenter condition AH ⊥ BC.

Direction AH: H - A = (h_x - 17, h_y) = (20 cos θ - 34, 20 sin θ).

C is on line AC: C = (17, 0) + t(h_y - 10, -h_x) = (17 + t(20 sin θ - 10), -t(20 cos θ - 17)).

B = (-h_x, 20 - h_y) = (17 - 20 cos θ, 20 - 20 sin θ).

Direction BC: C - B = (17 + t(20 sin θ - 10) - 17 + 20 cos θ, -t(20 cos θ - 17) - 20 + 20 sin θ)
= (20 cos θ + t(20 sin θ - 10), -t(20 cos θ - 17) - 20 + 20 sin θ)

AH ⊥ BC: (H - A) · (C - B) = 0

(20 cos θ - 34)(20 cos θ + t(20 sin θ - 10)) + 20 sin θ(-t(20 cos θ - 17) - 20 + 20 sin θ) = 0

Let me expand:
(20 cos θ - 34)(20 cos θ) + (20 cos θ - 34)t(20 sin θ - 10) + 20 sin θ(-t(20 cos θ - 17)) + 20 sin θ(-20 + 20 sin θ) = 0

= 400 cos²θ - 680 cos θ + t(20 cos θ - 34)(20 sin θ - 10) - 20t sin θ(20 cos θ - 17) - 400 sin θ + 400 sin²θ = 0

= 400(cos²θ + sin²θ) - 680 cos θ - 400 sin θ + t[(20 cos θ - 34)(20 sin θ - 10) - 20 sin θ(20 cos θ - 17)] = 0

= 400 - 680 cos θ - 400 sin θ + t[...]

Let me expand the t coefficient:
(20 cos θ - 34)(20 sin θ - 10) - 20 sin θ(20 cos θ - 17)
= 400 cos θ sin θ - 200 cos θ - 680 sin θ + 340 - 400 cos θ sin θ + 340 sin θ
= -200 cos θ - 340 sin θ + 340
= 340 - 200 cos θ - 340 sin θ

So: 400 - 680 cos θ - 400 sin θ + t(340 - 200 cos θ - 340 sin θ) = 0

t = (680 cos θ + 400 sin θ - 400) / (340 - 200 cos θ - 340 sin θ)

Now, we also need C on the circumcircle: |C - O|² = 400.

C - O = (17 + t(20 sin θ - 10) - 17 + 20 cos θ, -t(20 cos θ - 17) + 20 sin θ)
= (20 cos θ + t(20 sin θ - 10), 20 sin θ - t(20 cos θ - 17))

|C - O|² = (20 cos θ + t(20 sin θ - 10))² + (20 sin θ - t(20 cos θ - 17))² = 400

Let me denote p = 20 sin θ - 10, q = 20 cos θ - 17. Then:
C - O = (20 cos θ + tp, 20 sin θ - tq)

|C - O|² = (20 cos θ)² + 2·20 cos θ·tp + t²p² + (20 sin θ)² - 2·20 sin θ·tq + t²q²
= 400 + 2t(20 cos θ·p - 20 sin θ·q) + t²(p² + q²)
= 400

So: 2t(20 cos θ·p - 20 sin θ·q) + t²(p² + q²) = 0

t[2(20 cos θ·p - 20 sin θ·q) + t(p² + q²)] = 0

t = 0 (C = A, degenerate) or:
t = -2(20 cos θ·p - 20 sin θ·q) / (p² + q²)

20 cos θ·p - 20 sin θ·q = 20 cos θ(20 sin θ - 10) - 20 sin θ(20 cos θ - 17)
= 400 cos θ sin θ - 200 cos θ - 400 cos θ sin θ + 340 sin θ
= -200 cos θ + 340 sin θ

p² + q² = (20 sin θ - 10)² + (20 cos θ - 17)²
= 400 sin²θ - 400 sin θ + 100 + 400 cos²θ - 680 cos θ + 289
= 400 - 400 sin θ - 680 cos θ + 389
= 789 - 400 sin θ - 680 cos θ

So t = -2(-200 cos θ + 340 sin θ) / (789 - 400 sin θ - 680 cos θ)
= (400 cos θ - 680 sin θ) / (789 - 400 sin θ - 680 cos θ)

Now we have two expressions for t:
From AH ⊥ BC: t = (680 cos θ + 400 sin θ - 400) / (340 - 200 cos θ - 340 sin θ)
From C on circumcircle: t = (400 cos θ - 680 sin θ) / (789 - 400 sin θ - 680 cos θ)

Setting them equal:
(680 cos θ + 400 sin θ - 400) / (340 - 200 cos θ - 340 sin θ) = (400 cos θ - 680 sin θ) / (789 - 400 sin θ - 680 cos θ)

Let me denote c = cos θ, s = sin θ. Note c² + s² = 1.

(680c + 400s - 400)(789 - 400s - 680c) = (400c - 680s)(340 - 200c - 340s)

This is one equation in one unknown (θ), which should determine the triangle (up to reflection, which we handle by the sign choice for M).

Let me expand both sides. This is going to be messy but let me try.

Left side: (680c + 400s - 400)(789 - 400s - 680c)

Let me factor. 680c + 400s - 400 = 40(17c + 10s - 10)
789 - 400s - 680c = 789 - 40(10s + 17c)

Right side: (400c - 680s)(340 - 200c - 340s) = 40(10c - 17s) · 20(17 - 10c - 17s) = 800(10c - 17s)(17 - 10c - 17s)

Left side: 40(17c + 10s - 10) · (789 - 40(10s + 17c))

Hmm, let me just try to compute numerically. Let me try to find θ.

Actually, let me try a slightly different approach. Let me use the relation that in a triangle, OH² = R²(1 - 8 cos A cos B cos C) and other relations. But this might be complex.

Let me try numerical computation. I'll think through this.

Let me set c = cos θ, s = sin θ, c² + s² = 1.

Equation: (680c + 400s - 400)(789 - 400s - 680c) = (400c - 680s)(340 - 200c - 340s)

Let me expand:

LHS:
680c · 789 = 536520c
680c · (-400s) = -272000cs
680c · (-680c) = -462400c²
400s · 789 = 315600s
400s · (-400s) = -160000s²
400s · (-680c) = -272000cs
-400 · 789 = -315600
-400 · (-400s) = 160000s
-400 · (-680c) = 272000c

LHS = 536520c - 272000cs - 462400c² + 315600s - 160000s² - 272000cs - 315600 + 160000s + 272000c
= (536520 + 272000)c + (315600 + 160000)s - 462400c² - 160000s² - 544000cs - 315600
= 808520c + 475600s - 462400c² - 160000s² - 544000cs - 315600

RHS:
400c · 340 = 136000c
400c · (-200c) = -80000c²
400c · (-340s) = -136000cs
-680s · 340 = -231200s
-680s · (-200c) = 136000cs
-680s · (-340s) = 231200s²

RHS = 136000c - 80000c² - 136000cs - 231200s + 136000cs + 231200s²
= 136000c - 231200s - 80000c² + 231200s²

LHS - RHS = 0:
808520c + 475600s - 462400c² - 160000s² - 544000cs - 315600 - 136000c + 231200s + 80000c² - 231200s² = 0

= (808520 - 136000)c + (475600 + 231200)s + (-462400 + 80000)c² + (-160000 - 231200)s² - 544000cs - 315600 = 0

= 672520c + 706800s - 382400c² - 391200s² - 544000cs - 315600 = 0

Using c² + s² = 1, so s² = 1 - c²:
= 672520c + 706800s - 382400c² - 391200(1 - c²) - 544000cs - 315600 = 0
= 672520c + 706800s - 382400c² - 391200 + 391200c² - 544000cs - 315600 = 0
= 672520c + 706800s + 8800c² - 544000cs - 706800 = 0

Divide by 8800:
= 76.42... hmm, let me check: 672520/8800 = 76.42..., not clean. Let me try dividing by 400:
672520/400 = 1681.3, not clean either.

Let me try dividing by 80:
672520/80 = 8406.5, no.

Let me try 8800: 672520/8800 = 76.42..., 706800/8800 = 80.318..., not clean.

Hmm, let me recheck my arithmetic. Let me redo the expansion more carefully.

Actually, let me just try to solve this numerically. Let me use the equation:
672520c + 706800s + 8800c² - 544000cs - 706800 = 0

Divide by 8800:
672520/8800 = 76.42...
Hmm, 8800 × 76 = 668800, 672520 - 668800 = 3720. 3720/8800 = 0.4227...

Let me try dividing by 40:
672520/40 = 16813
706800/40 = 17670
8800/40 = 220
544000/40 = 13600
706800/40 = 17670

16813c + 17670s + 220c² - 13600cs - 17670 = 0

Divide by... gcd? 16813 is prime? Let me check: 16813/7 = 2401.86, no. 16813/11 = 1528.4, no. 16813/13 = 1293.3, no. 16813/17 = 989, 17×989 = 16813? 17×989 = 17×1000 - 17×11 = 17000 - 187 = 16813. Yes!

So 16813 = 17 × 989. 989 = 23 × 43. So 16813 = 17 × 23 × 43.

17670 = 17670. 17670/17 = 1039.4, no. 17670/23 = 768.3, no. 17670/2 = 8835, /3 = 5890, /5 = 3534, 17670 = 2×3×5×589 = 2×3×5×19×31.

220 = 4×55 = 4×5×11.
13600 = 136×100 = 8×17×100.

Hmm, gcd of 16813, 17670, 220, 13600, 17670. 16813 is odd, so gcd is odd. 16813 = 17×23×43. 17670 = 2×3×5×19×31. No common factors. So gcd = 1.

OK let me just solve numerically. Let me define f(θ) = 672520 cos θ + 706800 sin θ + 8800 cos²θ - 544000 cos θ sin θ - 706800.

Let me try θ = 0: f = 672520 + 0 + 8800 - 0 - 706800 = -25480. Negative.

θ = π/2: f = 0 + 706800 + 0 - 0 - 706800 = 0. Oh! θ = π/2 is a solution!

But θ = π/2 means cos θ = 0, sin θ = 1. Then h_x = 20·0 - 17 = -17, h_y = 20·1 = 20.

Let me check: O = (17, -20), A = (17, 0). AO = |(0, 20)| = 20. ✓
B = (17, 0). Wait, B = (-h_x, 20 - h_y) = (17, 0) = A. That's degenerate!

So θ = π/2 gives a degenerate triangle. Let me look for other solutions.

f(θ) = 672520 cos θ + 706800 sin θ + 8800 cos²θ - 544000 cos θ sin θ - 706800

Let me factor out from the sin θ = 1 solution. Let me write s = sin θ, c = cos θ, s² + c² = 1.

f = 672520c + 706800s + 8800c² - 544000cs - 706800

At s = 1, c = 0: f = 0 + 706800 + 0 - 0 - 706800 = 0. ✓

Let me substitute s² = 1 - c² and see if I can factor.

Actually, let me use the substitution s = 1 - ε for small ε and see the behavior, or let me just look for other roots.

f(π) = -672520 + 0 + 8800 - 0 - 706800 = -1370520. Negative.
f(3π/2) = 0 - 706800 + 0 - 0 - 706800 = -1413600. Negative.
f(π/4): c = s = √2/2 ≈ 0.7071
f = 672520(0.7071) + 706800(0.7071) + 8800(0.5) - 544000(0.5) - 706800
= 475466 + 499854 + 4400 - 272000 - 706800 = 920. Positive!

So f(0) = -25480, f(π/4) ≈ 920, f(π/2) = 0.

So there's a root between 0 and π/4, and θ = π/2 is a root (degenerate).

Let me find the root between 0 and π/4 more precisely.

f(0) = -25480
f(π/6): c = √3/2 ≈ 0.8660, s = 0.5
f = 672520(0.8660) + 706800(0.5) + 8800(0.75) - 544000(0.8660)(0.5) - 706800
= 582382 + 353400 + 6600 - 235532 - 706800
= -18950. Negative.

f(π/5): θ = 36°, c ≈ 0.8090, s ≈ 0.5878
f = 672520(0.8090) + 706800(0.5878) + 8800(0.6545) - 544000(0.8090)(0.5878) - 706800
= 544049 + 415477 + 5760 - 258688 - 706800
= -9202. Negative.

f(π/4.5): θ = 40°, c ≈ 0.7660, s ≈ 0.6428
f = 672520(0.7660) + 706800(0.6428) + 8800(0.5868) - 544000(0.7660)(0.6428) - 706800
= 515151 + 454329 + 5164 - 267815 - 706800
= 35. Very close to 0!

So θ ≈ 40°. Let me be more precise.

f(40°) ≈ 35. Let me try 40.1°.
c = cos(40.1°) ≈ 0.7649, s = sin(40.1°) ≈ 0.6442
f = 672520(0.7649) + 706800(0.6442) + 8800(0.7649²) - 544000(0.7649)(0.6442) - 706800
= 514409 + 455510 + 8800(0.5851) - 544000(0.4928) - 706800
= 514409 + 455510 + 5149 - 268083 - 706800
= 187. Positive, so root is between 40° and... wait, f(40°) ≈ 35 and f(40.1°) ≈ 187? That seems like a big jump. Let me recompute f(40°) more carefully.

θ = 40° = 40π/180 = 2π/9
c = cos(40°) = 0.7660444431
s = sin(40°) = 0.6427876097

672520 × 0.7660444431 = 515,151.6
706800 × 0.6427876097 = 454,328.5
8800 × 0.7660444431² = 8800 × 0.586824 = 5,164.1
544000 × 0.7660444431 × 0.6427876097 = 544000 × 0.492404 = 267,948.0

f = 515151.6 + 454328.5 + 5164.1 - 267948.0 - 706800 = -109.8

Hmm, I get -109.8 now. Let me be more careful.

672520 × 0.7660444431:
672520 × 0.7 = 470764
672520 × 0.06 = 40351.2
672520 × 0.006 = 4035.12
672520 × 0.0000444431 = 29.9
Total: 470764 + 40351.2 + 4035.12 + 29.9 = 515180.2

706800 × 0.6427876097:
706800 × 0.6 = 424080
706800 × 0.04 = 28272
706800 × 0.002 = 1413.6
706800 × 0.0007876097 = 556.8
Total: 424080 + 28272 + 1413.6 + 556.8 = 454322.4

8800 × 0.5868240888 = 5164.1

544000 × 0.7660444431 × 0.6427876097:
0.7660444431 × 0.6427876097 = 0.492403876
544000 × 0.492403876 = 267,947.7

f = 515180.2 + 454322.4 + 5164.1 - 267947.7 - 706800 = -81.0

So f(40°) ≈ -81. Let me try 41°.

θ = 41°, c = 0.75471, s = 0.65606

672520 × 0.75471 = 507,536.5
706800 × 0.65606 = 463,707.6
8800 × 0.75471² = 8800 × 0.56959 = 5,012.4
544000 × 0.75471 × 0.65606 = 544000 × 0.49512 = 269,343.5

f = 507536.5 + 463707.6 + 5012.4 - 269343.5 - 706800 = 114.0

So f(40°) ≈ -81, f(41°) ≈ 114. Root near 40.4°.

Let me try 40.4°: c = cos(40.4°), s = sin(40.4°)
40.4° = 40° + 0.4°
c ≈ 0.76604 × cos(0.4°) - 0.64279 × sin(0.4°) ≈ 0.76604 × 0.99998 - 0.64279 × 0.00698 ≈ 0.76602 - 0.00449 = 0.76153
s ≈ 0.64279 × 0.99998 + 0.76604 × 0.00698 ≈ 0.64278 + 0.00535 = 0.64813

672520 × 0.76153 = 512,131.8
706800 × 0.64813 = 458,077.1
8800 × 0.76153² = 8800 × 0.57993 = 5,103.4
544000 × 0.76153 × 0.64813 = 544000 × 0.49354 = 268,486.3

f = 512131.8 + 458077.1 + 5103.4 - 268486.3 - 706800 = 26.0

Try 40.3°: 
c ≈ 0.76604 × cos(0.3°) - 0.64279 × sin(0.3°) ≈ 0.76604 - 0.64279 × 0.00524 ≈ 0.76604 - 0.00337 = 0.76267
s ≈ 0.64279 + 0.76604 × 0.00524 ≈ 0.64279 + 0.00401 = 0.64680

672520 × 0.76267 = 512,898.5
706800 × 0.64680 = 457,135.2
8800 × 0.76267² = 8800 × 0.58167 = 5,118.7
544000 × 0.76267 × 0.64680 = 544000 × 0.49333 = 268,372.0

f = 512898.5 + 457135.2 + 5118.7 - 268372.0 - 706800 = -19.6

So root between 40.3° and 40.4°, approximately 40.35°.

Hmm, this doesn't seem to give a nice angle. Let me reconsider whether I've set up the problem correctly.

Actually, wait. Let me reconsider. Maybe I should think about this more carefully using known properties.

Let me reconsider the problem. We have:
- N = nine-point center = midpoint of OH
- M = midpoint of HB (on nine-point circle)
- ∠ANM = 90°, AN = 17, AO = R = 20

The nine-point circle has radius R/2 = 10 and center N. M is on it, so NM = 10.

Let me think about what ∠ANM = 90° means geometrically. 

Let me use vectors. Let O be the origin. Then:
- |A| = |B| = |C| = R = 20
- H = A + B + C (orthocenter in terms of circumcenter at origin)
- N = (O + H)/2 = H/2 = (A + B + C)/2
- M = (H + B)/2 = (A + 2B + C)/2

AN = A - N = A - (A + B + C)/2 = (A - B - C)/2
|AN| = |A - B - C|/2 = 17, so |A - B - C| = 34.

NM = M - N = (A + 2B + C)/2 - (A + B + C)/2 = B/2
|NM| = |B|/2 = R/2 = 10. ✓ (This is automatic!)

∠ANM = 90° means AN ⊥ NM, i.e., (A - B - C) · B = 0.
A·B - |B|² - B·C = 0
A·B - 400 - B·C = 0
A·B - B·C = 400

Also, |A - B - C|² = 34² = 1156.
|A|² + |B|² + |C|² - 2A·B - 2A·C + 2B·C = 1156
400 + 400 + 400 - 2A·B - 2A·C + 2B·C = 1156
1200 - 2(A·B + A·C - B·C) = 1156
A·B + A·C - B·C = 22

From A·B - B·C = 400 and A·B + A·C - B·C = 22:
A·C = 22 - (A·B - B·C) = 22 - 400 = -378

So A·C = -378. Since |A| = |C| = 20, A·C = 400 cos(2∠B) ... wait, no. A·C = |A||C| cos(∠AOC) where ∠AOC is the central angle. Actually, the central angle ∠AOC = 2∠B (inscribed angle theorem). So A·C = 400 cos(2B).

400 cos(2B) = -378
cos(2B) = -378/400 = -189/200

Similarly, A·B = 400 cos(2C) (central angle ∠AOB = 2C).
B·C = 400 cos(2A).

From A·B - B·C = 400:
400 cos(2C) - 400 cos(2A) = 400
cos(2C) - cos(2A) = 1

And A·B + A·C - B·C = 22:
400 cos(2C) + 400 cos(2B) - 400 cos(2A) = 22
cos(2C) + cos(2B) - cos(2A) = 22/400 = 11/200

We have:
cos(2B) = -189/200
cos(2C) - cos(2A) = 1
cos(2C) + cos(2B) - cos(2A) = 11/200

From the second and third:
cos(2C) + cos(2B) - cos(2A) = 11/200
(cos(2C) - cos(2A)) + cos(2B) = 11/200
1 + (-189/200) = 11/200
200/200 - 189/200 = 11/200 ✓

Great, so the system is consistent. We have:
cos(2B) = -189/200
cos(2C) - cos(2A) = 1

And A + B + C = π, so 2A + 2B + 2C = 2π.

We need to find cos(2A) and cos(2C). We know cos(2C) = 1 + cos(2A).

Also, 2A + 2C = 2π - 2B, so 2C = 2π - 2B - 2A.
cos(2C) = cos(2π - 2B - 2A) = cos(2B + 2A) = cos(2B)cos(2A) - sin(2B)sin(2A)

Let x = cos(2A), y = cos(2C) = 1 + x.
cos(2B) = -189/200.
sin(2B) = ±√(1 - (189/200)²) = ±√(1 - 35721/40000) = ±√(4279/40000) = ±√4279/200.

Since the triangle is acute, all angles < 90°, so 2A, 2B, 2C < 180°, meaning sin is positive.
sin(2B) = √4279/200.

y = cos(2B)cos(2A) - sin(2B)sin(2A)
1 + x = (-189/200)x - (√4279/200)sin(2A)

sin(2A) = ±√(1 - x²). Since 2A < 180° (A < 90°), sin(2A) > 0.
sin(2A) = √(1 - x²).

1 + x = (-189/200)x - (√4279/200)√(1 - x²)

Multiply by 200:
200 + 200x = -189x - √4279 · √(1 - x²)
200 + 389x = -√4279 · √(1 - x²)

Since the left side must be negative (right side is negative, assuming √4279 > 0):
200 + 389x < 0, so x < -200/389 ≈ -0.514.

Squaring:
(200 + 389x)² = 4279(1 - x²)
40000 + 155600x + 151321x² = 4279 - 4279x²
151321x² + 4279x² + 155600x + 40000 - 4279 = 0
155600x² + 155600x + 35721 = 0

Oh nice! Let me check: 151321 + 4279 = 155600. ✓
40000 - 4279 = 35721. ✓

155600x² + 155600x + 35721 = 0

Using the quadratic formula:
x = (-155600 ± √(155600² - 4·155600·35721)) / (2·155600)
= (-155600 ± √(155600(155600 - 142884))) / 311200
= (-155600 ± √(155600 · 12716)) / 311200

155600 · 12716 = ?
155600 · 12000 = 1,867,200,000
155600 · 700 = 108,920,000
155600 · 16 = 2,489,600
Total = 1,978,609,600

√1,978,609,600 = ?
1400² = 1,960,000
1410² = 1,988,100
1406² = 1,976,836
1407² = 1,979,649
So √1,978,609,600 ≈ 1406.6...

Hmm, let me check if 1,978,609,600 is a perfect square.
√1,978,609,600 ≈ 14066.3... wait, let me recalculate.

155600² = 24,211,360,000
4 × 155600 × 35721 = 622400 × 35721 = ?
622400 × 35000 = 21,784,000,000
622400 × 721 = 448,750,400
Total = 22,232,750,400

Discriminant = 24,211,360,000 - 22,232,750,400 = 1,978,609,600

√1,978,609,600: Let me try 44,480² = 1,978,470,400. Close but not exact.
44,482² = 44480² + 2×44480×2 + 4 = 1,978,470,400 + 177,920 + 4 = 1,978,648,324. Too big.
44,481² = 1,978,470,400 + 44,480 + 44,481 = 1,978,559,361. Still not matching.
Hmm, 1,978,609,600 - 1,978,559,361 = 50,239. Not a perfect square.

Let me factor 1,978,609,600.
1,978,609,600 = 155600 × 12716
155600 = 1556 × 100 = 4 × 389 × 100 = 4 × 389 × 4 × 25 = 16 × 25 × 389 = 400 × 389
12716 = 4 × 3179 = 4 × 3179. Is 3179 prime? 3179/7 = 454.1, /11 = 289, 11 × 289 = 3179? 11 × 289 = 3179. Yes! 289 = 17². So 3179 = 11 × 17².
12716 = 4 × 11 × 17² = 44 × 289.

So 1,978,609,600 = 400 × 389 × 44 × 289 = 400 × 44 × 289 × 389 = 17600 × 289 × 389
= 17600 × 17² × 389
√ = √(17600 × 17² × 389) = 17 × √(17600 × 389)
17600 × 389 = 17600 × 400 - 17600 × 11 = 7,040,000 - 193,600 = 6,846,400
√6,846,400 = ?
2600² = 6,760,000
2616² = 6,843,456
2617² = 6,848,689
Not a perfect square.

Hmm. So the discriminant is not a perfect square, meaning cos(2A) is irrational. That's fine—the final answer might still be rational.

Let me try a different approach. Instead of finding the angles, let me work directly with coordinates and compute AI/AJ.

Let me set up coordinates with O at the origin.

We have:
- A, B, C on circle of radius 20
- H = A + B + C
- N = H/2 = (A + B + C)/2
- M = (H + B)/2 = (A + 2B + C)/2
- E = foot of altitude from B to AC

Key relations:
- A·C = -378 (i.e., cos(2B) = -189/200)
- A·B - B·C = 400 (i.e., cos(2C) - cos(2A) = 1)

Let me choose coordinates. Let me place things conveniently.

Let me put B along a convenient direction. Since NM = B/2 (from the calculation above, M - N = B/2), and ∠ANM = 90° with AN along some direction and NM perpendicular to it.

Let me set up: N at origin (for the nine-point circle analysis), but actually let me keep O at origin.

With O at origin:
- N = (A + B + C)/2
- A - N = (A - B - C)/2, |A - N| = 17
- M - N = B/2

Let me choose coordinates so that A - N is along the x-axis and B is along the y-axis (since AN ⊥ NM and NM = B/2).

A - N = (A - B - C)/2 = (17, 0) → A - B - C = (34, 0)
B = (0, 20) (since |B| = 20 and B is along y-axis; we choose positive y)

Then A - C = (34, 0) + B = (34, 20), so A = C + (34, 20).

Also, |A| = 20 and |C| = 20.
|C + (34, 20)|² = 400
|C|² + 2C·(34,20) + |(34,20)|² = 400
400 + 68C_x + 40C_y + 1156 + 400 = 400
68C_x + 40C_y + 1156 = 0
68C_x + 40C_y = -1156
17C_x + 10C_y = -289

Also |C|² = 400: C_x² + C_y² = 400.

From 17C_x + 10C_y = -289: C_y = (-289 - 17C_x)/10

C_x² + ((-289 - 17C_x)/10)² = 400
C_x² + (289 + 17C_x)²/100 = 400
100C_x² + (289 + 17C_x)² = 40000
100C_x² + 83521 + 9826C_x + 289C_x² = 40000
389C_x² + 9826C_x + 83521 - 40000 = 0
389C_x² + 9826C_x + 43521 = 0

Discriminant: 9826² - 4×389×43521
9826² = 96,550,276
4 × 389 × 43521 = 1556 × 43521 = ?
1556 × 43000 = 66,908,000
1556 × 521 = 810,676
Total = 67,718,676

Discriminant = 96,550,276 - 67,718,676 = 28,831,600

√28,831,600 = ?
5369² = 28,826,161
5370² = 28,836,900
Not exact. Let me factor.

28,831,600 = 288316 × 100 = 288316 × 100
288316 = 4 × 72079
72079 = ? 72079/7 = 10297, 7 × 10297 = 72079. 10297/11 = 936.1, /13 = 792.1, /17 = 605.7, /19 = 542, 19 × 542 = 10298. No. /23 = 447.7, /29 = 355.1, /31 = 332.2, /37 = 278.3, /41 = 251.1, /43 = 239.5, /47 = 218.7, /53 = 194.3, /59 = 174.5, /61 = 168.8, /67 = 153.7, /71 = 145, 71 × 145 = 10295. No. /73 = 141, 73 × 141 = 10293. No. /79 = 130.3, /83 = 124.1, /89 = 115.7, /97 = 106.2, /101 = 102, 101 × 102 = 10302. No. /103 = 99.97, √10297 ≈ 101.5. So 10297 is prime? Let me check more: 10297/107 = 96.2, /109 = 94.5, /113 = 91.1. √10297 ≈ 101.5, so I need to check primes up to 101. I checked 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101. None divide evenly. So 10297 is prime.

28,831,600 = 4 × 7 × 10297 × 100 = 2800 × 7 × 10297 = ... hmm, this doesn't simplify nicely.

√28,831,600 = √(4 × 7207900) = 2√7207900 = 2√(100 × 72079) = 20√72079 = 20√(7 × 10297)

So C_x = (-9826 ± 20√72079) / (2 × 389) = (-9826 ± 20√72079) / 778

This is getting quite messy. Let me try a different approach to the problem.

Actually, maybe I should think about what AI/AJ equals in terms of the triangle AEM.

I is the incenter of triangle AEM. J is the intersection of ME and AI.

In triangle AEM, I is the incenter, and AI is the angle bisector from A. J is where this angle bisector meets side ME.

By the angle bisector theorem (well, the incenter lies on the angle bisector, and the angle bisector from A meets ME at J):

AJ/AI = ? Actually, we need AI/AJ.

In triangle AEM, the angle bisector from A meets ME at J. The incenter I lies on AJ (between A and J). We need AI/AJ.

There's a formula for this. In a triangle with angle bisector from vertex A meeting the opposite side at J, and incenter I on AJ:

AI/AJ = (b + c) / (a + b + c)

where a = ME (side opposite A), b = AE (side opposite M... wait, let me be careful.

In triangle AEM:
- Side opposite A is ME, let's call it a
- Side opposite E is AM, let's call it e (or b)
- Side opposite M is AE, let's call it m (or c)

Actually, let me use standard notation. In triangle AEM, let me relabel vertices as A, E, M with:
- a = EM (opposite A)
- e = AM (opposite E)  
- m = AE (opposite M)

The incenter I lies on the angle bisector from A. The angle bisector from A meets EM at J.

By the angle bisector theorem: EJ/JM = AE/AM = m/e.

The length of the angle bisector from A: AJ = 2em·cos(A/2) / (e + m) ... actually, the angle bisector length formula is:

AJ = 2·e·m·cos(A/2) / (e + m) ... no, that's not right either.

The angle bisector from A to side EM has length:
AJ = (2·e·m·cos(A/2)) / (e + m) ... hmm, I don't think that's right.

Actually, the angle bisector from vertex A to side a (= EM) has length:
l_a = (2·e·m / (e + m)) · cos(A/2)

Wait, I think the formula is:
l_a = √(e·m · (1 - a²/(e+m)²))

Or equivalently: l_a = (2/(e+m)) · √(e·m·s·(s-a)) where s = (a+e+m)/2.

And the distance from A to the incenter:
AI = r / sin(A/2)

where r is the inradius.

Also, AI = (e + m - a) / (2 · cos(A/2)) ... no.

Actually, there's a cleaner formula. The incenter divides the angle bisector such that:
AI = r / sin(A/2)

And the angle bisector length from A is:
AJ = 2·e·m·cos(A/2) / (e + m)

So AI/AJ = [r / sin(A/2)] / [2·e·m·cos(A/2) / (e + m)]
= r·(e + m) / (2·e·m·sin(A/2)·cos(A/2))
= r·(e + m) / (e·m·sin(A))

And r = area / s where s = (a + e + m)/2, and area = (1/2)·e·m·sin(A).

So r = (1/2)·e·m·sin(A) / s = e·m·sin(A) / (a + e + m)

AI/AJ = [e·m·sin(A) / (a + e + m)] · (e + m) / (e·m·sin(A))
= (e + m) / (a + e + m)

So AI/AJ = (e + m) / (a + e + m) = (AM + AE) / (EM + AM + AE)

That's a beautiful formula! So AI/AJ = (AM + AE) / (AM + AE + EM) = (AM + AE) / (perimeter of triangle AEM).

Wait, let me double-check. AI/AJ = (e + m) / (a + e + m) where:
- a = EM (opposite A)
- e = AM (opposite E)
- m = AE (opposite M)

So AI/AJ = (AM + AE) / (EM + AM + AE) = (AM + AE) / P where P is the perimeter.

So I need to find AM, AE, and EM.

Now, let me compute these. With O at origin:
- A, B, C on circle of radius 20
- H = A + B + C
- M = (H + B)/2 = (A + 2B + C)/2
- E = foot of altitude from B to AC

Let me use the coordinate system I set up:
- B = (0, 20)
- A - B - C = (34, 0), so A = C + (34, 20)
- 17C_x + 10C_y = -289
- C_x² + C_y² = 400

From these, C_x = (-9826 ± 20√72079) / 778.

Let me simplify. 778 = 2 × 389. 9826 = 2 × 4913 = 2 × 17³. Oh! 17³ = 4913. So 9826 = 2 × 17³.

C_x = (-2 × 17³ ± 20√72079) / (2 × 389) = (-17³ ± 10√72079) / 389

And 389 is prime (I think). 389/7 = 55.6, /11 = 35.4, /13 = 29.9, /17 = 22.9, /19 = 20.5. √389 ≈ 19.7. So check primes up to 19: 2, 3, 5, 7, 11, 13, 17, 19. 389/19 = 20.47. None divide. So 389 is prime.

72079 = 7 × 10297 (both prime). So √72079 doesn't simplify.

This is getting very messy. Let me try a completely different approach.

Let me think about what AM, AE, EM are in terms of the triangle's elements.

M is the midpoint of HB. So AM is the distance from A to the midpoint of HB.

E is the foot of the altitude from B to AC. So AE is the projection of AB onto AC (well, it's the distance from A to the foot of the altitude from B).

Let me use the standard triangle notation: sides a = BC, b = CA, c = AB, angles A, B, C, circumradius R = 20.

E is the foot of the altitude from B to AC. So:
AE = c·cos(A) (projection of AB onto AC) ... wait, let me think. In triangle ABC, the foot of the altitude from B to AC is E. Then AE = AB·cos(A) = c·cos(A). And CE = BC·cos(C) = a·cos(C). And AE + CE = b.

Actually, AE = c·cos(A) and CE = a·cos(C). Let me verify: AE + CE = c·cos(A) + a·cos(C). By the projection formula, b = c·cos(A) + a·cos(C). ✓

M is the midpoint of HB. H is the orthocenter.

AM: Let me compute this. We know that AH = 2R·cos(A) (distance from vertex to orthocenter). And HB = 2R·cos(B).

M is the midpoint of HB, so HM = MB = HB/2 = R·cos(B).

AM: In triangle AHM, we know AH = 2R·cos(A), HM = R·cos(B), and the angle ∠AHM.

∠AHM is the angle at H in triangle AHM. H is the orthocenter. The angle ∠BHC = 180° - A. The angle ∠AHB = 180° - C. 

Actually, ∠AHB = 180° - C (this is a known result). So in triangle AHB, the angle at H is 180° - C.

M is on HB, so ∠AHM = ∠AHB = 180° - C.

By the law of cosines in triangle AHM:
AM² = AH² + HM² - 2·AH·HM·cos(∠AHM)
= (2R·cos(A))² + (R·cos(B))² - 2·(2R·cos(A))·(R·cos(B))·cos(180° - C)
= 4R²cos²A + R²cos²B + 4R²cos(A)cos(B)cos(C)

Hmm, let me also compute EM.

E is on AC, M is the midpoint of HB. Let me think about the nine-point circle. Both E and M are on the nine-point circle. The nine-point circle has center N and radius R/2.

Actually, let me think about EM differently. E is the foot of the altitude from B, and M is the midpoint of HB. Both are on the nine-point circle, and they're both related to the altitude from B.

In fact, E and M are both on the altitude from B (line BH). E is the foot on AC, and M is the midpoint of HB. So E, M, B, H are collinear (all on line BH).

Wait, that's a key observation! E is on BH (foot of altitude from B) and M is on BH (midpoint of HB). So E, M, H, B are all collinear.

So EM is just a segment on line BH. EM = |EB - MB| or |EB - MB|... let me think about the order.

On line BH: B, E, H are in this order (for an acute triangle, E is between B and H, since the orthocenter is inside the triangle). M is the midpoint of HB, so M is between H and B. Specifically, M is the midpoint of HB.

BE = altitude from B = c·sin(A) = a·sin(C) = 2R·sin(A)·sin(C) ... actually, BE = c·sin(A) where the altitude from B has length h_b = c·sin(A) = a·sin(C).

BH = 2R·cos(B) (distance from B to orthocenter).

So on line BH, from B: E is at distance BE, H is at distance BH, M is at distance BH/2.

EM = |BE - BH/2| or |BE - BH/2|... E is at distance BE from B, M is at distance BH/2 from B.

EM = |BE - BH/2|

For an acute triangle, is E between B and M, or M between B and E?

BE = h_b = c·sin(A) = 2R·sin(C)·sin(A) (using c = 2R·sin(C))
BH = 2R·cos(B)
BH/2 = R·cos(B)

BE = 2R·sin(A)·sin(C)

EM = |2R·sin(A)·sin(C) - R·cos(B)| = R|2sin(A)sin(C) - cos(B)|

Using cos(B) = -cos(A+C) = -(cos(A)cos(C) - sin(A)sin(C)) = sin(A)sin(C) - cos(A)cos(C):
2sin(A)sin(C) - cos(B) = 2sin(A)sin(C) - sin(A)sin(C) + cos(A)cos(C) = sin(A)sin(C) + cos(A)cos(C) = cos(A-C)

So EM = R·|cos(A-C)| = R·cos(A-C) (since for acute triangle, |A-C| < 90° so cos is positive).

EM = 20·cos(A-C).

Now, AE = c·cos(A) = 2R·sin(C)·cos(A).

AM: From the computation above:
AM² = 4R²cos²A + R²cos²B + 4R²cos(A)cos(B)cos(C)
= R²(4cos²A + cos²B + 4cos(A)cos(B)cos(C))

Let me try to simplify. We know that cos²B = (sin(A)sin(C) - cos(A)cos(C))² = sin²(A)sin²(C) - 2sin(A)sin(C)cos(A)cos(C) + cos²(A)cos²(C).

4cos²A + cos²B + 4cos(A)cos(B)cos(C)
= 4cos²A + sin²(A)sin²(C) - 2sin(A)sin(C)cos(A)cos(C) + cos²(A)cos²(C) + 4cos(A)cos(C)(sin(A)sin(C) - cos(A)cos(C))
= 4cos²A + sin²(A)sin²(C) - 2sin(A)sin(C)cos(A)cos(C) + cos²(A)cos²(C) + 4sin(A)sin(C)cos(A)cos(C) - 4cos²(A)cos²(C)
= 4cos²A + sin²(A)sin²(C) + 2sin(A)sin(C)cos(A)cos(C) + cos²(A)cos²(C) - 4cos²(A)cos²(C)
= 4cos²A + (sin(A)sin(C) + cos(A)cos(C))² - 4cos²(A)cos²(C)
= 4cos²A + cos²(A-C) - 4cos²(A)cos²(C)
= 4cos²(A)(1 - cos²(C)) + cos²(A-C)
= 4cos²(A)sin²(C) + cos²(A-C)

So AM² = R²(4cos²(A)sin²(C) + cos²(A-C))
= (2R·cos(A)·sin(C))² + (R·cos(A-C))²
= AE² + EM² (since AE = 2R·sin(C)cos(A) and EM = R·cos(A-C))

Wait, that's interesting! AM² = AE² + EM². That would mean triangle AEM is right-angled at E!

Let me verify: AE = 2R·sin(C)·cos(A), EM = R·cos(A-C), and AM² = AE² + EM².

If triangle AEM is right-angled at E, then ∠AEM = 90°. But E is the foot of the altitude from B to AC, so ∠BEC = 90° and ∠BEA = 90°. Since M is on line BE (which is line BH), ∠AEM = ∠AEB = 90°. Yes! That makes sense!

So triangle AEM is right-angled at E, with:
- AE = 2R·sin(C)·cos(A) (one leg)
- EM = R·cos(A-C) (other leg)
- AM = hypotenuse

And the perimeter P = AE + EM + AM.

AI/AJ = (AM + AE) / P = (AM + AE) / (AM + AE + EM)

Since it's a right triangle at E:
AM = √(AE² + EM²)

Let me denote x = AE, y = EM, z = AM = √(x² + y²).

AI/AJ = (z + x) / (z + x + y)

Now I need to find x, y, z (or their ratios).

x = AE = 2R·sin(C)·cos(A) = 40·sin(C)·cos(A)
y = EM = R·cos(A-C) = 20·cos(A-C)
z = AM = √(x² + y²)

Let me compute z² = x² + y²:
= 1600·sin²(C)·cos²(A) + 400·cos²(A-C)
= 400(4·sin²(C)·cos²(A) + cos²(A-C))

cos(A-C) = cos(A)cos(C) + sin(A)sin(C)
cos²(A-C) = cos²(A)cos²(C) + 2cos(A)cos(C)sin(A)sin(C) + sin²(A)sin²(C)

4sin²(C)cos²(A) + cos²(A-C) = 4sin²(C)cos²(A) + cos²(A)cos²(C) + 2cos(A)cos(C)sin(A)sin(C) + sin²(A)sin²(C)
= cos²(A)(4sin²(C) + cos²(C)) + sin²(A)sin²(C) + 2cos(A)cos(C)sin(A)sin(C)
= cos²(A)(4sin²(C) + cos²(C)) + sin²(A)sin²(C) + 2cos(A)cos(C)sin(A)sin(C)

4sin²(C) + cos²(C) = 4sin²(C) + 1 - sin²(C) = 3sin²(C) + 1

Hmm, this doesn't simplify easily. Let me try a different approach.

z = AM. Let me compute AM directly.

M = (A + 2B + C)/2 (with O at origin).
AM = |M - A| = |(A + 2B + C)/2 - A| = |(-A + 2B + C)/2| = |2B + C - A|/2

|2B + C - A|² = 4|B|² + |C|² + |A|² + 4B·C - 4A·B - 2A·C
= 4·400 + 400 + 400 + 4B·C - 4A·B - 2A·C
= 2400 + 4B·C - 4A·B - 2A·C

We know:
A·C = -378
A·B - B·C = 400, so A·B = 400 + B·C

2400 + 4B·C - 4(400 + B·C) - 2(-378)
= 2400 + 4B·C - 1600 - 4B·C + 756
= 2400 - 1600 + 756
= 1556

So |2B + C - A|² = 1556, and AM = √1556 / 2 = √(1556/4) = √389.

So AM = √389. Interesting!

Now let me compute AE.
AE = 2R·sin(C)·cos(A) = 40·sin(C)·cos(A)

I need sin(C)·cos(A). Let me find this from the known quantities.

We know:
cos(2B) = -189/200
cos(2C) - cos(2A) = 1

And A + B + C = π.

Let me use the identity: sin(C)cos(A) = (1/2)(sin(C+A) + sin(C-A)) = (1/2)(sin(π-B) + sin(C-A)) = (1/2)(sin(B) + sin(C-A)).

Hmm, I still need more info. Let me try to compute AE² directly.

AE = c·cos(A) where c = AB = 2R·sin(C) = 40·sin(C).
AE² = c²·cos²(A) = 1600·sin²(C)·cos²(A) = 400·(2sin(C)cos(A))² = 400·(sin(C+A) + sin(C-A))²/... 

Actually, 2sin(C)cos(A) = sin(C+A) + sin(C-A) = sin(π-B) + sin(C-A) = sin(B) + sin(C-A).

So AE = 40·sin(C)·cos(A) = 20·(sin(B) + sin(C-A)).

Hmm. Let me try computing AE² using coordinates.

With O at origin, B = (0, 20), A = C + (34, 20), and E is the foot of the altitude from B to AC.

E is the projection of B onto line AC. 

A = C + (34, 20). Direction of AC: (34, 20) (from C to A, or A - C = (34, 20)).

Wait, A - C = (34, 20), so the direction of AC is (34, 20).

E = A + t·(C - A) for some t (E is on segment AC), and E is the foot of the perpendicular from B.

Actually, E = C + t·(A - C) = C + t·(34, 20) for some t, and (B - E) · (A - C) = 0.

B - E = (0, 20) - C - t·(34, 20) = -C + (0, 20) - t·(34, 20) = (-C_x - 34t, -C_y + 20 - 20t)

(B - E) · (34, 20) = 34(-C_x - 34t) + 20(-C_y + 20 - 20t) = 0
-34C_x - 1156t - 20C_y + 400 - 400t = 0
-34C_x - 20C_y + 400 - 1556t = 0
t = (400 - 34C_x - 20C_y) / 1556

We know 17C_x + 10C_y = -289, so 34C_x + 20C_y = -578.
t = (400 - (-578)) / 1556 = 978 / 1556 = 489/778

So t = 489/778.

E = C + (489/778)·(34, 20) = (C_x + 489·34/778, C_y + 489·20/778)
= (C_x + 16626/778, C_y + 9780/778)
= (C_x + 8313/389, C_y + 4890/778)
= (C_x + 8313/389, C_y + 2445/389)

AE = |E - A| = |C + t(A-C) - A| = |(1-t)(C - A)| = (1-t)·|C - A| = (1 - 489/778)·|(34, 20)|
Wait, A - C = (34, 20), so |A - C| = √(34² + 20²) = √(1156 + 400) = √1556 = 2√389.

AE = |A - E| = |A - C - t(A-C)| = (1-t)|A - C| = (289/778)·2√389 = 578√389/778 = 289√389/389

So AE = 289√389 / 389 = 289/√389.

Similarly, CE = t·|A - C| = (489/778)·2√389 = 978√389/778 = 489√389/389 = 489/√389.

Check: AE + CE = (289 + 489)/√389 = 778/√389 = 778√389/389 = 2√389. ✓ (since |AC| = 2√389)

Now, EM. E and M are both on line BH. Let me compute their positions.

M = (A + 2B + C)/2 = ((C + (34,20)) + 2(0,20) + C)/2 = (2C + (34, 60))/2 = C + (17, 30)

So M = (C_x + 17, C_y + 30).

E = (C_x + 8313/389, C_y + 2445/389)

EM = |M - E| = |(17 - 8313/389, 30 - 2445/389)|
= |((17·389 - 8313)/389, (30·389 - 2445)/389)|
= |((6613 - 8313)/389, (11670 - 2445)/389)|
= |(-1700/389, 9225/389)|
= (1/389)·√(1700² + 9225²)
= (1/389)·√(2890000 + 85100625)
= (1/389)·√(88000625)

√88000625 = ?
9380² = 87984400
9381² = 88003161
So √88000625 is not an integer. Let me factor.

88000625 = ?
88000625 / 25 = 3520025
3520025 / 25 = 140801
140801 = ?
140801 / 7 = 20114.4, /11 = 12800.1, /13 = 10830.8, /17 = 8282.4, /19 = 7410.6, /23 = 6121.8, /29 = 4855.2, /31 = 4542, 31 × 4542 = 140802. No. /37 = 3805.4, /41 = 3434.2, /43 = 3274.4, /47 = 2995.8, /53 = 2656.6, /59 = 2386.5, /61 = 2308.2, /67 = 2101.5, /71 = 1983.1, /73 = 1928.8, /79 = 1782.3, /83 = 1696.4, /89 = 1582, 89 × 1582 = 140798. No. /97 = 1451.6, /101 = 1394.1, /103 = 1367, 103 × 1367 = 140801? 103 × 1367 = 103 × 1300 + 103 × 67 = 133900 + 6901 = 140801. Yes!

So 140801 = 103 × 1367. Is 1367 prime? 1367/7 = 195.3, /11 = 124.3, /13 = 105.2, /17 = 80.4, /19 = 71.9, /23 = 59.4, /29 = 47.1, /31 = 44.1, /37 = 36.9. √1367 ≈ 37. So check up to 37. None divide. So 1367 is prime. Is 103 prime? Yes.

So 88000625 = 625 × 140801 = 5⁴ × 103 × 1367.
√88000625 = 25√(103 × 1367) = 25√140801

EM = 25√140801 / 389

Hmm, this is getting messy. Let me check if I can simplify 140801/389².
389² = 151321
140801/151321 ≈ 0.930. Not a nice ratio.

Wait, but I showed earlier that EM = R·cos(A-C) = 20·cos(A-C). And also that AM² = AE² + EM² (right angle at E).

Let me verify: AM = √389, AE = 289/√389.
AM² = 389, AE² = 289²/389 = 83521/389.
EM² = AM² - AE² = 389 - 83521/389 = (389² - 83521)/389 = (151321 - 83521)/389 = 67800/389.

EM = √(67800/389) = √67800/√389.

67800 = 678 × 100 = 6 × 113 × 100 = 600 × 113. √67800 = 10√678 = 10√(6×113).

Hmm, let me check: 67800 = 4 × 16950 = 4 × 16950. 16950 = 2 × 8475 = 2 × 3 × 2825 = 6 × 2825 = 6 × 25 × 113 = 150 × 113. So 67800 = 4 × 150 × 113 = 600 × 113. √67800 = √(600 × 113) = 10√(6 × 113) = 10√678.

So EM = 10√678/√389 = 10√(678/389) = 10√(678/389).

678/389: gcd(678, 389)? 678 = 1×389 + 289, 389 = 1×289 + 100, 289 = 2×100 + 89, 100 = 1×89 + 11, 89 = 8×11 + 1. So gcd = 1. The fraction is already in lowest terms.

EM = 10√678 / √389

Let me rationalize: EM = 10√(678 × 389) / 389 = 10√263742 / 389.

263742 = 678 × 389. 678 = 2 × 3 × 113. 389 is prime. So 263742 = 2 × 3 × 113 × 389. Not a perfect square.

OK so let me just compute the ratio AI/AJ = (AM + AE) / (AM + AE + EM).

AM = √389
AE = 289/√389 = 289√389/389
EM = 10√678/√389 = 10√(678×389)/389 = 10√263742/389

Let me express everything with denominator √389:
AM = √389 = 389/√389
AE = 289/√389
EM = 10√678/√389

AM + AE = (389 + 289)/√389 = 678/√389

AM + AE + EM = (389 + 289 + 10√678)/√389 = (678 + 10√678)/√389

AI/AJ = 678 / (678 + 10√678) = 678 / (678 + 10√678)

Factor: 678 = 678, 10√678 = 10√678.
= 678 / (678 + 10√678)
= 678 / (√678(√678 + 10))   ... since 678 = √678 × √678
= √678 / (√678 + 10)

Hmm, but this should be rational (m/n for relatively prime positive integers). So either I made an error, or √678 simplifies, or there's additional constraint I'm missing.

Wait, 678 = 2 × 3 × 113. √678 is irrational. So AI/AJ = √678 / (√678 + 10) is irrational. But the problem says it's m/n for relatively prime positive integers. So I must have made an error somewhere.

Let me re-examine. Let me recheck the computation of EM.

Actually, wait. Let me recheck whether E and M are both on line BH, and recompute EM.

E is the foot of the altitude from B to AC. So E is on line BH (the altitude from B passes through H). ✓
M is the midpoint of HB, so M is on segment HB, which is on line BH. ✓

So E and M are both on line BH. The distance EM should be |BE - BM| or |BE - BM| depending on the order.

BE = altitude from B = h_b.
BM = BH/2.

Let me compute BE and BH.

BH = 2R·cos(B) = 40·cos(B).
BE = h_b = 2R·sin(A)·sin(C) = 40·sin(A)·sin(C) (using h_b = c·sin(A) = 2R·sin(C)·sin(A)).

Actually, let me compute these from coordinates.

B = (0, 20), H = A + B + C = (C + (34,20)) + (0,20) + C = (2C_x + 34, 2C_y + 40).

BH = |H - B| = |(2C_x + 34, 2C_y + 20)| = 2|(C_x + 17, C_y + 10)|

|C + (17, 10)|² = (C_x + 17)² + (C_y + 10)² = C_x² + 34C_x + 289 + C_y² + 20C_y + 100
= 400 + 34C_x + 20C_y + 389
= 789 + 34C_x + 20C_y

We know 34C_x + 20C_y = -578 (from 17C_x + 10C_y = -289, doubled).

= 789 - 578 = 211

So |C + (17, 10)|² = 211, BH = 2√211.

Hmm, but BH = 2R·cos(B) = 40·cos(B). So cos(B) = √211/20. Let me check: cos²(B) = 211/400, sin²(B) = 189/400. cos(2B) = cos²B - sin²B = (211 - 189)/400 = 22/400 = 11/200.

But earlier I computed cos(2B) = -189/200. That's a contradiction! Let me recheck.

Hmm, I think I made an error earlier. Let me recompute A·C.

We had (with O at origin):
A - N = (A - B - C)/2, |A - N| = 17.
|A - B - C|² = 34² = 1156.

|A - B - C|² = |A|² + |B|² + |C|² - 2A·B - 2A·C + 2B·C
= 400 + 400 + 400 - 2A·B - 2A·C + 2B·C
= 1200 - 2(A·B + A·C - B·C) = 1156

So A·B + A·C - B·C = 22. ✓

∠ANM = 90°: (A - N) · (M - N) = 0.
M - N = B/2 (computed earlier).
(A - N) · (B/2) = 0, so (A - B - C) · B = 0.
A·B - |B|² - B·C = 0
A·B - 400 - B·C = 0
A·B - B·C = 400. ✓

From these: A·C = 22 - (A·B - B·C) = 22 - 400 = -378. ✓

Now, A·C = |A||C|cos(∠AOC) = 400·cos(∠AOC). The central angle ∠AOC = 2B (inscribed angle theorem, angle subtended by arc AC at center is twice that at B).

So 400·cos(2B) = -378, cos(2B) = -378/400 = -189/200.

But from coordinates, I got cos(2B) = 11/200. There's a sign error somewhere.

Let me recheck. cos(2B) = 2cos²B - 1. If cos²B = 211/400, then cos(2B) = 2(211/400) - 1 = 422/400 - 1 = 22/400 = 11/200.

But we need cos(2B) = -189/200. So cos²B should satisfy 2cos²B - 1 = -189/200, cos²B = (1 - 189/200)/2 = (11/200)/2 = 11/400. So cos(B) = √11/20.

But from coordinates, I got cos²B = 211/400. These don't match. So I have an error in the coordinate computation.

Let me recheck. BH = 2R·cos(B). Let me verify this formula.

The distance from B to H: BH = 2R·cos(B). This is a standard result. Let me verify with coordinates.

H = A + B + C (with O at origin). BH = |H - B| = |A + C|.

|A + C|² = |A|² + |C|² + 2A·C = 400 + 400 + 2(-378) = 800 - 756 = 44.

BH = √44 = 2√11.

And 2R·cos(B) = 40·cos(B). So cos(B) = 2√11/40 = √11/20. cos²B = 11/400. ✓

So my coordinate computation of BH was wrong. Let me recheck.

H = A + B + C. With A = C + (34, 20), B = (0, 20):
H = (C + (34, 20)) + (0, 20) + C = (2C_x + 34, 2C_y + 40).

BH = |H - B| = |(2C_x + 34, 2C_y + 40) - (0, 20)| = |(2C_x + 34, 2C_y + 20)|

= 2|(C_x + 17, C_y + 10)|

|C + (17, 10)|² = (C_x + 17)² + (C_y + 10)²
= C_x² + 34C_x + 289 + C_y² + 20C_y + 100
= (C_x² + C_y²) + 34C_x + 20C_y + 389
= 400 + 34C_x + 20C_y + 389
= 789 + 34C_x + 20C_y

17C_x + 10C_y = -289, so 34C_x + 20C_y = -578.

= 789 - 578 = 211

So |C + (17,10)|² = 211, BH = 2√211.

But |A + C|² = 44, so BH = 2√11.

These should be equal: 2√211 vs 2√11. They're not. So I have an error.

The issue is: is H = A + B + C with O at origin? Yes, this is the standard formula for the orthocenter when the circumcenter is at the origin.

And BH = |H - B| = |A + C|. Let me compute |A + C|².
A = C + (34, 20), so A + C = 2C + (34, 20).
|A + C|² = |2C + (34, 20)|² = 4|C|² + 4C·(34, 20) + |(34, 20)|²
= 4·400 + 4(34C_x + 20C_y) + 1556
= 1600 + 4(-578) + 1556
= 1600 - 2312 + 1556
= 844

Hmm, that gives 844, not 44. Let me recheck.

A·C = -378. |A + C|² = |A|² + |C|² + 2A·C = 400 + 400 + 2(-378) = 800 - 756 = 44. ✓

But from coordinates: A + C = 2C + (34, 20).
|2C + (34,20)|² = 4|C|² + 4(34C_x + 20C_y) + 34² + 20²
= 1600 + 4(34C_x + 20C_y) + 1556

34C_x + 20C_y = 2(17C_x + 10C_y) = 2(-289) = -578.

= 1600 + 4(-578) + 1556 = 1600 - 2312 + 1556 = 844.

So |A + C|² = 844 from coordinates, but 44 from the dot product. Contradiction!

The issue must be in my coordinate setup. Let me recheck.

I set B = (0, 20) and A - B - C = (34, 0), so A = B + C + (34, 0) = (0, 20) + C + (34, 0) = C + (34, 20).

A·C = (C + (34, 20)) · C = |C|² + 34C_x + 20C_y = 400 + 34C_x + 20C_y = 400 + (-578) = -178.

But we need A·C = -378. So -178 ≠ -378. There's an error!

The issue is that A - B - C = (34, 0) doesn't mean A = B + C + (34, 0). Let me recheck.

A - N = (A - B - C)/2 = (17, 0), so A - B - C = (34, 0), thus A = B + C + (34, 0).

B = (0, 20), so A = (0, 20) + C + (34, 0) = (C_x + 34, C_y + 20).

A·C = (C_x + 34)C_x + (C_y + 20)C_y = C_x² + 34C_x + C_y² + 20C_y = 400 + 34C_x + 20C_y.

17C_x + 10C_y = -289, so 34C_x + 20C_y = -578.

A·C = 400 - 578 = -178.

But we need A·C = -378. So there's a discrepancy of 200.

Hmm, let me recheck the derivation of A·C = -378.

|A - B - C|² = 1156.
|A|² + |B|² + |C|² - 2A·B - 2A·C + 2B·C = 1156
1200 - 2(A·B + A·C - B·C) = 1156
A·B + A·C - B·C = 22

A·B - B·C = 400

Adding: 2A·B = 422, A·B = 211.
Subtracting: 2A·C - 2B·C = 22 - 400 = -378... wait.
A·B + A·C - B·C = 22
A·B - B·C = 400

Subtracting the second from the first: A·C = 22 - 400 = -378. ✓

But from coordinates, A·C = -178. So the coordinate setup is wrong.

Let me recheck. The issue might be with the direction of B.

I set A - N along the x-axis and B along the y-axis (since NM = B/2 is perpendicular to AN).

A - N = (17, 0), so A - B - C = (34, 0).
M - N = B/2, and ∠ANM = 90° means (A-N) ⊥ (M-N), so (34, 0) ⊥ B, meaning B is along the y-axis. ✓

B = (0, ±20). I chose B = (0, 20).

A = B + C + (34, 0) = (C_x + 34, C_y + 20).

|A|² = (C_x + 34)² + (C_y + 20)² = C_x² + 68C_x + 1156 + C_y² + 40C_y + 400
= 400 + 68C_x + 40C_y + 1556
= 1956 + 68C_x + 40C_y

This should equal 400 (since |A| = 20).
68C_x + 40C_y = 400 - 1956 = -1556
17C_x + 10C_y = -389

Ah, I had -289 before, but it should be -389! Let me recheck.

Wait, I think I made an error earlier. Let me redo from scratch.

|A|² = 400:
(C_x + 34)² + (C_y + 20)² = 400
C_x² + 68C_x + 1156 + C_y² + 40C_y + 400 = 400
(C_x² + C_y²) + 68C_x + 40C_y + 1156 = 0
400 + 68C_x + 40C_y + 1156 = 0
68C_x + 40C_y = -1556
17C_x + 10C_y = -389

I had -289 before, which was wrong! The error was that I forgot the +400 from (C_y + 20)² expansion. Let me redo.

(C_y + 20)² = C_y² + 40C_y + 400. And C_x² + C_y² = 400. So:
400 + 68C_x + 40C_y + 1156 + 400 = 400... wait, let me be more careful.

(C_x + 34)² + (C_y + 20)² = C_x² + 68C_x + 1156 + C_y² + 40C_y + 400
= (C_x² + C_y²) + 68C_x + 40C_y + 1556
= 400 + 68C_x + 40C_y + 1556
= 1956 + 68C_x + 40C_y

Set equal to 400:
1956 + 68C_x + 40C_y = 400
68C_x + 40C_y = -1556
17C_x + 10C_y = -389

OK so the correct equation is 17C_x + 10C_y = -389, not -289. I made an arithmetic error earlier. Let me redo everything.

Now: C_x² + C_y² = 400 and 17C_x + 10C_y = -389.

C_y = (-389 - 17C_x)/10

C_x² + ((-389 - 17C_x)/10)² = 400
100C_x² + (389 + 17C_x)² = 40000
100C_x² + 151321 + 13226C_x + 289C_x² = 40000
389C_x² + 13226C_x + 151321 - 40000 = 0
389C_x² + 13226C_x + 111321 = 0

Discriminant: 13226² - 4×389×111321

13226² = ?
13226² = (13000 + 226)² = 169000000 + 2×13000×226 + 226² = 169000000 + 5876000 + 51076 = 174927076

4 × 389 × 111321 = 1556 × 111321
1556 × 111321 = 1556 × 110000 + 1556 × 1321 = 171160000 + 2055476 = 173215476

Discriminant = 174927076 - 173215476 = 1711600

√1711600 = ?
1308² = 1710864
1309² = 1713481
Not exact. Let me factor.

1711600 = 17116 × 100 = 17116 × 100
17116 = 4 × 4279
4279 is prime (checked earlier).
So 1711600 = 400 × 4279
√1711600 =
