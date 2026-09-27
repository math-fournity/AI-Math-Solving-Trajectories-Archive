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
  <problem_id>polymath_04196</problem_id>
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

Let \( \triangle ABC \) be an acute triangle with \( AC > AB \). Let \( D, E, \) and \( F \) be the feet of the altitudes from \( A, B, \) and \( C \) onto \( \overline{BC}, \overline{CA}, \) and \( \overline{AB} \), respectively. Let \( K \) be the intersection of \( \overline{EF} \) and \( \overline{AD} \), and let \( I \) be the intersection of \( \overline{EF} \) and \( \overline{BC} \). Let \( W \) be a point on ray \( \overrightarrow{BF} \) such that \( \angle IWF = \angle FWE \). Suppose \( AKBI \) is cyclic and \( \cos(\angle BCA) = \frac{2}{5} \). Find \( \frac{WB}{WI} \).

## Standard Solution

Let \( H \) be the orthocenter of \( \triangle ABC \). Notice that \( AKBI \) being cyclic implies

\[
\measuredangle BAK = \measuredangle BIK = \measuredangle CBE - \measuredangle FEB = \measuredangle DAC - \measuredangle BAH,
\]

i.e., \( 2B - C = 90^\circ \).

**Claim 1:** The quadrilateral \( WIBE \) is cyclic.

**Proof:** Let \( W' = (EBI) \cap \overrightarrow{BF} \) where \( W' \neq B \). Observe \( W \) is unique: it is the second intersection of \( \overrightarrow{BF} \) with the Apollonius circle determined by segment \( \overline{IE} \) and point \( F \). Thus, it is enough to show \( W' = W \). First note \( \measuredangle BIE = \measuredangle BAH = \measuredangle FEB = \measuredangle IEB \), where the first equality comes from \( AKBI \) being cyclic. Then, \( W'IBE \) cyclic implies \( \measuredangle IW'F = \measuredangle FW'E \), so \( W' = W \).

From here, it follows by \( \measuredangle WBI = \measuredangle WEI \) that \( \triangle WIB \sim \triangle WFE \). We compute

\[
\frac{WB}{WI} = \frac{WE}{WF} = \frac{IB}{IF} = \frac{\sin C}{\sin B} = \frac{\sin C}{\sin \left(45^\circ + \frac{C}{2}\right)} = \frac{2 \sin C}{\sqrt{\cos C + 1} + \sqrt{-\cos C + 1}}
\]

so the answer is

\[
\frac{2 \sqrt{21}}{5} \cdot \frac{1}{\sqrt{\frac{7}{5}} + \sqrt{\frac{3}{5}}} = \frac{2 \sqrt{105}(\sqrt{7} - \sqrt{3})}{20} = \frac{7 \sqrt{15} - 3 \sqrt{35}}{10}
\]

\(\frac{7 \sqrt{15} - 3 \sqrt{35}}{10}\)

## AI's Thinking (Attempted Solution Process)

Let me solve this geometry problem. Let me set up coordinates and work through it carefully.

We have acute triangle ABC with AC > AB. D, E, F are feet of altitudes from A, B, C onto BC, CA, AB respectively. K = EF ∩ AD, I = EF ∩ BC. W on ray BF such that ∠IWF = ∠FWE. AKBI cyclic, cos(∠BCA) = 2/5. Find WB/WI.

Let me set up coordinates. Place the triangle conveniently.

Let me use the standard setup. Let me place B at origin, C on the x-axis.

Let B = (0,0), C = (a, 0) where a = BC. Let A = (d, h) where d is the x-coordinate of A (so D = (d, 0)) and h > 0 is the altitude.

Since AC > AB: AC² = (a-d)² + h², AB² = d² + h². AC > AB means (a-d)² > d², i.e., a² - 2ad > 0, i.e., d < a/2.

F is foot of altitude from C to AB. E is foot of altitude from B to CA.

Let me compute E and F.

Line AB: from B(0,0) to A(d,h). Direction (d, h). F is projection of C(a,0) onto line AB.
F = ((C·(d,h))/(d²+h²)) (d,h) = (ad/(d²+h²))(d, h) = (ad²/(d²+h²), adh/(d²+h²)).

Let me denote c² = AB² = d² + h², b² = AC² = (a-d)² + h².

Line CA: from C(a,0) to A(d,h). Direction (d-a, h). E is projection of B(0,0) onto line CA.
E = C + ((B-C)·(d-a,h))/((d-a)²+h²) (d-a, h) = (a,0) + ((-a)(d-a))/(b²) (d-a, h)
= (a,0) + (a(a-d)/b²)(d-a, h)
= (a,0) + (-a(a-d)²/b², -a(a-d)h/b²)

Wait, let me redo. (B-C) = (-a, 0). (d-a, h). Dot product = -a(d-a) = a(a-d). So
E = C + (a(a-d)/b²)(d-a, h) = (a + a(a-d)(d-a)/b², a(a-d)h/b²)
= (a - a(a-d)²/b², a(a-d)h/b²).

So E = (a - a(a-d)²/b², a(a-d)h/b²).

Now EF is the line through E and F. This is related to the orthic triangle.

Actually, there's a known fact: EF is part of the orthic triangle, and the line EF is the polar-related line. Let me think about I = EF ∩ BC.

Since BC is the x-axis, I is where EF meets y=0.

Let me find the equation of line EF.

Actually, let me use a known result. In the orthic triangle, the line EF (feet from B and C) meets BC at a point I, and there's a relation involving the angles.

Let me use the fact that ∠AEF = ∠ABC and ∠AFE = ∠ACB (since AEHF is cyclic with the orthocenter... actually A, E, H, F are concyclic where H is orthocenter, on circle with diameter AH).

Let me think about this more carefully using angles.

Since BE ⊥ CA and CF ⊥ AB, the quadrilateral BCEF... no. Let me think about AEHF. H is the orthocenter. ∠AEH = 90° (since BE ⊥ CA, and E is on CA, so BE ⊥ AE, and H is on BE). ∠AFH = 90° similarly. So A, E, H, F are concyclic on circle with diameter AH.

On this circle, ∠AEF = ∠AHF. And ∠AHF = 90° - ∠HAF... hmm, let me think differently.

Actually, ∠AFE = ∠AHE (angles subtending same arc AE). ∠AHE: H is orthocenter, E is foot from B. In triangle AHE... Actually ∠AHE = 180° - ∠EHC. And ∠EHC = 90° - ∠C (since in triangle EHC, ∠HEC = 90°). So ∠AHE = 180° - (90° - C) = 90° + C. That doesn't seem right for an inscribed angle.

Let me reconsider. ∠AFE is an inscribed angle in circle AEHF subtending arc AE. ∠AHE also subtends arc AE. So ∠AFE = ∠AHE. Now ∠AHE: E is on CA, H is orthocenter on BE. So HE is along BE (perpendicular to CA). ∠AHE is the angle at H between HA and HE. HA is the altitude from A (perpendicular to BC). HE is along BE (perpendicular to CA). So ∠AHE = angle between perpendicular to BC and perpendicular to CA = angle between BC and CA = ∠BCA = C.

So ∠AFE = C. Similarly ∠AEF = B.

Good. So in triangle AEF, ∠AEF = B, ∠AFE = C, ∠EAF = A.

Now I = EF ∩ BC. Let me find the angles at I.

In triangle, EF extended meets BC at I. Consider triangle EIC (or the configuration). Since E is on CA and I is on BC (extended possibly).

∠AEF = B, and ∠AEC = 180° (E on line CA), so ∠FEC = 180° - B. In triangle EIC: ∠EIC is what we want, ∠ECI = C (angle at C of original triangle, since I is on line BC and E is on line CA, so ∠ECI = ∠BCA = C). ∠CEI = 180° - ∠AEF = 180° - B (since ∠AEF + ∠CEI = 180° as they're supplementary along line EF... wait, E is on CA, and EF goes from E. ∠AEF is the angle at E between EA and EF. ∠CEI is the angle at E between EC and EI. Since A, E, C are collinear and F, E, I are collinear (on line EF), ∠AEF + ∠CEI = 180°. So ∠CEI = 180° - B.

In triangle EIC: ∠EIC + ∠ECI + ∠CEI = 180°, so ∠EIC + C + (180° - B) = 180°, giving ∠EIC = B - C.

So ∠BIC = B - C (assuming B > C; we need to check the sign). Since AC > AB, we have B > C (opposite sides). So ∠BIC = B - C > 0. And I is on the extension of BC beyond C (since the angle is positive, I is on the side of C away from B... let me verify).

Actually, let me reconsider the position. If B > C, then... Let me think about where I is. The line EF, when extended, meets line BC. Since ∠BIC = B - C, and this is the angle at I in triangle EIC. The point I could be on either side. Let me just compute with coordinates to be sure.

Now, K = EF ∩ AD. AD is the altitude from A, which is the line x = d (in our coordinate system). K is on EF and on x = d.

Now the condition: AKBI is cyclic. A, K, B, I are concyclic.

Let me use coordinates. Let me parametrize.

Let me set up with specific angle. cos C = 2/5, so sin C = √21/5.

Let me use the angles. Let ∠A = α, ∠B = β, ∠C = γ with cos γ = 2/5, sin γ = √21/5.

Let me use the law of sines: a/sin α = b/sin β = c/sin γ = 2R.

Let me place things in terms of angles and use trigonometric identities.

Let me find I first. I = EF ∩ BC. Using the result ∠BIC = β - γ.

By the sine rule in triangle BIC (if I is beyond C) or considering the configuration:

Actually, let me use the power of a point or cross-ratio approach.

Let me use coordinates with B at origin, C at (a, 0).

Let me use the formula for I. The line EF meets BC at I. 

There's a known result: BI/CI = (c cos B)/(b cos C) ... hmm, I'm not sure. Let me derive it.

Actually, let me use the fact that in the orthic triangle, the line EF (opposite to D in the orthic triangle) meets BC at a point with a nice ratio.

Let me use coordinates. B = (0,0), C = (a, 0), A = (d, h).

F = (ad²/c², adh/c²) where c² = d² + h².
E = (a - a(a-d)²/b², a(a-d)h/b²) where b² = (a-d)² + h².

Let me simplify. Let me use the substitution: d = c cos B (since in triangle, the foot D has BD = c cos B... wait, D is foot from A to BC. BD = AB cos B = c cos B. So d = c cos B. And h = c sin B. Also a - d = b cos C, h = b sin C.

So d = c cos B, h = c sin B = b sin C, a = c cos B + b cos C.

c² = d² + h². b² = (a-d)² + h². Good.

F = (ad²/c², adh/c²) = (a cos²B, a cos B sin B) [since d/c = cos B, h/c = sin B].
So F = (a cos²B, a sin B cos B).

E = (a - a(a-d)²/b², a(a-d)h/b²) = (a - a cos²C, a cos C sin C) [since (a-d)/b = cos C, h/b = sin C].
So E = (a sin²C, a sin C cos C).

Nice. So F = (a cos²B, a sin B cos B) and E = (a sin²C, a sin C cos C).

Line EF: Let me find where it meets y = 0 (the x-axis, which is line BC).

Parametrize: P = E + t(F - E). y-coordinate: a sin C cos C + t(a sin B cos B - a sin C cos C) = 0.
t = -sin C cos C / (sin B cos B - sin C cos C) = sin C cos C / (sin C cos C - sin B cos B).

Using sin 2x = 2 sin x cos x: sin C cos C = (sin 2C)/2, sin B cos B = (sin 2B)/2.
t = sin 2C / (sin 2C - sin 2B).

x-coordinate of I: x_I = a sin²C + t(a cos²B - a sin²C) = a[sin²C + t(cos²B - sin²C)].

cos²B - sin²C = cos 2B... no. cos²B = (1+cos 2B)/2, sin²C = (1-cos 2C)/2. So cos²B - sin²C = (cos 2B + cos 2C)/2.

Hmm, this is getting complicated. Let me use a different approach.

x_I = a sin²C + [sin 2C/(sin 2C - sin 2B)] · a · (cos²B - sin²C).

Let me compute cos²B - sin²C = (1+cos2B)/2 - (1-cos2C)/2 = (cos2B + cos2C)/2.

And sin²C = (1 - cos 2C)/2.

x_I = a [(1-cos2C)/2 + sin2C/(sin2C - sin2B) · (cos2B + cos2C)/2].

Let me denote sB = sin 2B, sC = sin 2C, cB = cos 2B, cC = cos 2C.

x_I = a/2 [(1 - cC) + sC(cB + cC)/(sC - sB)].

= a/2 [(1 - cC)(sC - sB) + sC(cB + cC)] / (sC - sB).

Numerator: (1-cC)(sC - sB) + sC(cB + cC) = sC - sB - cC·sC + cC·sB + sC·cB + sC·cC.

The -cC·sC and +sC·cC cancel. = sC - sB + cC·sB + sC·cB = sC(1 + cB) + sB(cC - 1).

Now 1 + cB = 1 + cos 2B = 2 cos²B. cC - 1 = cos 2C - 1 = -2 sin²C.
So numerator = sC · 2 cos²B + sB · (-2 sin²C) = 2(sin 2C cos²B - sin 2B sin²C).
= 2(2 sin C cos C cos²B - 2 sin B cos B sin²C) = 4(sin C cos C cos²B - sin B cos B sin²C).

Hmm, let me try a different factoring. 

sC(1+cB) - sB(1-cC) = 2 sin C cos C · 2 cos²B - 2 sin B cos B · 2 sin²C
= 4(sin C cos C cos²B - sin B cos B sin²C)
= 4 sin C cos C cos B (cos B) - 4 sin B sin C cos B sin C... 

Let me factor: = 4 sin C cos B (cos C cos B - sin B sin C) = 4 sin C cos B cos(B + C) = 4 sin C cos B cos(π - A) = -4 sin C cos B cos A.

So numerator = -4 sin C cos B cos A.

Denominator: sC - sB = sin 2C - sin 2B = 2 cos(B+C) sin(C-B) = 2 cos(π-A) sin(C-B) = -2 cos A sin(C-B) = 2 cos A sin(B-C).

So x_I = a/2 · (-4 sin C cos B cos A) / (2 cos A sin(B-C)) = a/2 · (-4 sin C cos B) / (2 sin(B-C)) = a · (-sin C cos B) / sin(B-C).

So x_I = -a sin C cos B / sin(B - C).

Since B > C (as AC > AB), sin(B-C) > 0, and sin C, cos B > 0 (acute triangle), so x_I < 0. This means I is on the extension of BC beyond B (on the side of B away from C). So I is to the left of B.

BI = |x_I| = a sin C cos B / sin(B - C).

Now let me find K = EF ∩ AD. AD is the line x = d = c cos B.

K is on line EF at x = c cos B. Let me parametrize: P = E + t(F - E), x = c cos B.

x = a sin²C + t(a cos²B - a sin²C) = c cos B.
t = (c cos B - a sin²C) / (a(cos²B - sin²C)).

This is getting messy. Let me think about the cyclic condition differently.

AKBI cyclic. A, K, B, I on a circle. 

K is on AD (altitude from A) and on EF. I is on BC and on EF. So K and I are both on line EF.

Since AKBI is cyclic, and K, I are on line EF, while A is on line AD and B is on line BC...

Let me use the power of a point or angle conditions.

Since AKBI is cyclic, ∠AKI = ∠ABI (angles subtending same arc AI). Or ∠AKB = ∠AIB.

Actually, let me use: ∠AKI + ∠ABI = 180° (opposite angles in cyclic quad, if K and B are on opposite sides of AI). Or the inscribed angle theorem.

Let me think about which angles. A, K, B, I cyclic. K and I are on EF. A is above, B is at origin.

∠AKB = ∠AIB (both subtend arc AB). 

∠AIB: I is on BC (extended beyond B), A is above. ∠AIB is the angle at I in triangle AIB. Since I is on line BC beyond B, ∠AIB = ∠AIB. In triangle AIB, ∠ABI = 180° - B (since I is beyond B on line BC, the angle at B between BA and BI is 180° - B). And ∠BAI... A is at (d, h), I is at (x_I, 0) with x_I < 0. 

Hmm, let me use the angle ∠AIB. In triangle ABI: ∠ABI = 180° - B (supplementary to ∠ABC = B since I is on extension of BC beyond B). ∠AIB = ? And ∠BAI = ?

Actually, ∠AIB: I is on line BC. The angle ∠AIC (where I is beyond B) ... Let me compute ∠AIB directly.

In triangle AIB: ∠ABI = 180° - B. By sine rule or angle sum, ∠AIB + ∠BAI = B.

Hmm, let me use coordinates. A = (d, h) = (c cos B, c sin B). I = (x_I, 0) where x_I = -a sin C cos B / sin(B-C).

Vector IA = (d - x_I, h) = (c cos B + a sin C cos B/sin(B-C), c sin B).
Vector IB = (0 - x_I, 0) = (a sin C cos B/sin(B-C), 0).

∠AIB is the angle at I between IA and IB. Since IB is along the positive x-direction (I is to the left of B), ∠AIB = angle of IA with positive x-axis = arctan(h / (d - x_I)).

d - x_I = c cos B + a sin C cos B / sin(B-C) = cos B (c + a sin C / sin(B-C)).

By sine rule, a/sin A = c/sin C, so a = c sin A / sin C. So a sin C = c sin A.
d - x_I = cos B (c + c sin A / sin(B-C)) = c cos B (1 + sin A / sin(B-C)) = c cos B (sin(B-C) + sin A) / sin(B-C).

sin A = sin(π - B - C) = sin(B+C). So sin(B-C) + sin(B+C) = 2 sin B cos C.

d - x_I = c cos B · 2 sin B cos C / sin(B-C) = 2c sin B cos B cos C / sin(B-C) = c sin 2B cos C / sin(B-C).

h = c sin B.

tan(∠AIB) = h / (d - x_I) = c sin B / (c sin 2B cos C / sin(B-C)) = sin B sin(B-C) / (sin 2B cos C) = sin B sin(B-C) / (2 sin B cos B cos C) = sin(B-C) / (2 cos B cos C).

So tan(∠AIB) = sin(B-C) / (2 cos B cos C).

Now ∠AKB = ∠AIB (cyclic condition). K is on AD (x = d) and on EF. Let me find ∠AKB.

K is on line AD (vertical line x = d) and on line EF. A is at (d, h), so A is directly above K (or below, but K is below A since K is on EF which is below A). So KA is vertical.

∠AKB is the angle at K between KA (vertical, pointing up) and KB.

K = (d, y_K) where y_K is the y-coordinate on line EF at x = d.

Let me find y_K. On line EF: P = E + t(F - E), x = d = c cos B.
t = (c cos B - a sin²C) / (a(cos²B - sin²C)).

This is complex. Let me try a different approach.

Let me use the angle ∠AKB directly. Since KA is along AD (perpendicular to BC), KA is vertical. The angle ∠AKB is the angle between the vertical (upward from K) and KB.

If K = (d, y_K), then KB direction is (0 - d, 0 - y_K) = (-d, -y_K). KA direction is (0, h - y_K) = (0, positive).

∠AKB = angle between (0, 1) and (-d, -y_K) (normalized). 

tan(∠AKB) = |d| / |y_K| ... let me be careful. The angle between upward vertical and direction to B.

Direction KA: (0, h - y_K), upward. Direction KB: (-d, -y_K).

The angle between them: cos(∠AKB) = (0·(-d) + (h-y_K)(-y_K)) / (|KA||KB|). This is getting complicated.

Let me use the tangent. The angle that KB makes with the horizontal is arctan(y_K / d) (since B is at origin, K is at (d, y_K), so KB goes from K to B, direction (-d, -y_K), the angle below horizontal is arctan(y_K/d)). The angle KA makes with horizontal is 90° (vertical up). So ∠AKB = 90° - arctan(y_K/d) = arctan(d/y_K) (if y_K > 0).

Wait, I need to be more careful. K is on EF, which is inside the triangle (between the feet E and F). The y-coordinate of K should be positive (inside the triangle). And d > 0. So ∠AKB = arctan(d / y_K)? Let me recheck.

KA points straight up (0, positive). KB points to (-d, -y_K), which is down-left. The angle between straight up and down-left... that's more than 90°. Hmm.

Actually, ∠AKB is the angle at K in triangle AKB. A is above K, B is below-left of K. So the angle is between the ray KA (up) and ray KB (down-left). This angle is 90° + arctan(y_K/d) (the angle from up to down-left, going clockwise, is 90° + the angle below horizontal).

Hmm wait. Let me reconsider. The ray KA goes up (angle 90° from horizontal). The ray KB goes to (-d, -y_K), which is in the third quadrant relative to K, at angle 180° + arctan(y_K/d) from positive x, or equivalently, the direction angle is 180° + arctan(y_K/d).

The angle between the two rays = |90° - (180° + arctan(y_K/d))| = |−90° − arctan(y_K/d)| = 90° + arctan(y_K/d).

So ∠AKB = 90° + arctan(y_K / d). Hmm, but this should be less than 180° for a valid angle in a cyclic quadrilateral. If y_K and d are positive and small, this is slightly more than 90°, which is fine.

Actually wait, for a cyclic quadrilateral AKBI, we need ∠AKB + ∠AIB = 180° (opposite angles) or ∠AKB = ∠AIB (same arc). Let me figure out which.

In cyclic quad AKBI, the vertices in order... A is at top, K is on AD inside triangle, B is at origin, I is to the left of B on x-axis. Going around: A → K → B → I → A? Or A → I → B → K → A?

Let me think. A is at (d, h) top. K is at (d, y_K) with 0 < y_K < h, inside triangle. B is at (0,0). I is at (x_I, 0) with x_I < 0.

Going counterclockwise: I (left, on x-axis) → B (origin) → K (inside, above) → A (top) → back to I. So the order is I, B, K, A (or equivalently A, I, B, K).

In cyclic quad AIBK (in order), ∠AKB and ∠AIB are opposite angles? No. ∠A is at vertex A (angle IAB... wait, the angle at A is ∠IAK or ∠BAK? The vertices in order are A, I, B, K. So:
- Angle at A = ∠KAI (between AK and AI)
- Angle at I = ∠AIB (between IA and IB)
- Angle at B = ∠IBK (between BI and BK)
- Angle at K = ∠BKA (between KB and KA)

Opposite pairs: (A, B) and (I, K). So ∠AIB + ∠BKA = 180°.

So ∠AIB + ∠AKB = 180°. (Note ∠BKA = ∠AKB.)

So the cyclic condition is: ∠AIB + ∠AKB = 180°.

We have ∠AKB = 90° + arctan(y_K / d) and ∠AIB = arctan(sin(B-C)/(2 cos B cos C)).

So: arctan(sin(B-C)/(2 cos B cos C)) + 90° + arctan(y_K/d) = 180°.

arctan(y_K/d) = 90° - arctan(sin(B-C)/(2 cos B cos C)).

tan(90° - θ) = cot θ = 1/tan θ. So:

y_K / d = 2 cos B cos C / sin(B-C).

So y_K = d · 2 cos B cos C / sin(B-C) = c cos B · 2 cos B cos C / sin(B-C) = 2c cos²B cos C / sin(B-C).

But we also need K to be on line EF. So this gives us a condition relating the angles. Let me find y_K from the line EF equation and set it equal.

K is on EF at x = d = c cos B. Let me find the y-coordinate.

Line EF passes through E = (a sin²C, a sin C cos C) and F = (a cos²B, a sin B cos B).

Parametrize: at x = c cos B.

Using a = c sin A / sin C:

E = (c sin A sin C / sin C... wait, a sin²C = (c sin A / sin C) sin²C = c sin A sin C.
E = (c sin A sin C, c sin A sin C cos C / sin C) ... let me redo.

a sin²C = (c sin A/sin C) sin²C = c sin A sin C.
a sin C cos C = (c sin A/sin C) sin C cos C = c sin A cos C.
So E = (c sin A sin C, c sin A cos C).

a cos²B = (c sin A/sin C) cos²B.
a sin B cos B = (c sin A/sin C) sin B cos B.
So F = (c sin A cos²B / sin C, c sin A sin B cos B / sin C).

Hmm, these have different forms. Let me use a = c sin A / sin C and also a = b sin A / sin B.

Let me just use the two-point form for the line EF and find y at x = c cos B.

Slope of EF: m = (y_F - y_E)/(x_F - x_E) = (a sin B cos B - a sin C cos C)/(a cos²B - a sin²C) = (sin B cos B - sin C cos C)/(cos²B - sin²C).

Numerator: (sin 2B - sin 2C)/2 = cos(B+C) sin(B-C) = -cos A sin(B-C).
Denominator: (cos 2B + cos 2C)/2 = cos(B+C) cos(B-C) = -cos A cos(B-C).

So m = (-cos A sin(B-C)) / (-cos A cos(B-C)) = tan(B-C).

So the slope of EF is tan(B - C). Interesting!

Now y_K = y_E + m(x_K - x_E) = c sin A cos C + tan(B-C)(c cos B - c sin A sin C).

x_K = c cos B, x_E = c sin A sin C = c sin(B+C) sin C.

c cos B - c sin A sin C = c(cos B - sin A sin C) = c(cos B - sin(B+C) sin C).
sin(B+C) = sin B cos C + cos B sin C.
sin(B+C) sin C = sin B sin C cos C + cos B sin²C.
cos B - sin(B+C) sin C = cos B - sin B sin C cos C - cos B sin²C = cos B(1 - sin²C) - sin B sin C cos C = cos B cos²C - sin B sin C cos C = cos C(cos B cos C - sin B sin C) = cos C cos(B+C) = cos C cos(π - A) = -cos C cos A.

So x_K - x_E = -c cos A cos C.

y_K = c sin A cos C + tan(B-C) · (-c cos A cos C) = c cos C (sin A - cos A tan(B-C)).
= c cos C (sin A cos(B-C) - cos A sin(B-C)) / cos(B-C)
= c cos C sin(A - (B-C)) / cos(B-C)
= c cos C sin(A - B + C) / cos(B-C).

Now A + B + C = π, so A - B + C = π - 2B. sin(π - 2B) = sin 2B.

y_K = c cos C sin 2B / cos(B-C) = c cos C · 2 sin B cos B / cos(B-C) = 2c sin B cos B cos C / cos(B-C).

Now from the cyclic condition: y_K = 2c cos²B cos C / sin(B-C).

Setting equal:
2c sin B cos B cos C / cos(B-C) = 2c cos²B cos C / sin(B-C).

Cancel 2c cos C (nonzero):
sin B cos B / cos(B-C) = cos²B / sin(B-C).

sin B / cos(B-C) = cos B / sin(B-C) (canceling cos B).

sin B sin(B-C) = cos B cos(B-C).

sin B sin(B-C) - cos B cos(B-C) = 0.
-(cos B cos(B-C) - sin B sin(B-C)) = 0.
-cos(B + (B-C)) = 0.
-cos(2B - C) = 0.

So cos(2B - C) = 0, meaning 2B - C = 90° (since the triangle is acute and B > C, 2B - C should be in a reasonable range).

So 2B - C = π/2, i.e., 2B = C + π/2.

With A + B + C = π: A = π - B - C = π - B - (2B - π/2) = π - B - 2B + π/2 = 3π/2 - 3B.

So A = 3π/2 - 3B. For A > 0: B < π/2. For A < π/2 (acute): 3π/2 - 3B < π/2, so 3B > π, B > π/3. Also B < π/2. And C = 2B - π/2 > 0 requires B > π/4. And C < π/2 requires 2B - π/2 < π/2, B < π. Already satisfied.

Also A acute: A = 3π/2 - 3B < π/2 → B > π/3. And A > 0 → B < π/2. C acute: C = 2B - π/2 < π/2 → B < π. OK. C > 0 → B > π/4. B acute: B < π/2. So π/3 < B < π/2.

Now cos C = 2/5. C = 2B - π/2. cos C = cos(2B - π/2) = sin 2B. So sin 2B = 2/5.

Then cos 2B = √(1 - 4/25) = √(21/25) = √21/5 (positive since 2B < π, and B < π/2 so 2B < π, and B > π/3 so 2B > 2π/3, so 2B is in (2π/3, π), where cos is negative!).

Wait, B > π/3 means 2B > 2π/3. And B < π/2 means 2B < π. So 2B ∈ (2π/3, π). In this range, cos 2B < 0. So cos 2B = -√21/5.

Let me verify: sin 2B = 2/5, cos 2B = -√21/5. sin² + cos² = 4/25 + 21/25 = 1. ✓.

Now I need to find WB/WI.

W is on ray BF such that ∠IWF = ∠FWE.

Ray BF: from B through F and beyond. F is the foot of altitude from C to AB, so F is on segment AB. Ray BF goes from B through F (on AB) and beyond.

∠IWF = ∠FWE means WF bisects angle IWE (externally or internally). Since W is on ray BF (beyond F potentially), and I, F, E are on line EF...

Wait, I, F, E are all on line EF. So ∠IWF and ∠FWE are angles at W with one ray being WI and WE respectively, and the other being WF. Since I, F, E are collinear (on line EF), the rays WI, WF, WE all go to points on the same line.

If I, F, E are collinear, then ∠IWF and ∠FWE are the angles that WF makes with WI and WE respectively. Since I, F, E are on a line, and W is off that line, the angles ∠IWF and ∠FWE are on the same side or opposite sides depending on the order of I, F, E.

The condition ∠IWF = ∠FWE means WF is the angle bisector of ∠IWE (if F is between I and E on the line, then WF bisects the angle at W in triangle WIE).

Actually, since I, F, E are collinear, and W is not on this line, the angle ∠IWE is the angle at W in triangle WIE, and F is on side IE. The condition ∠IWF = ∠FWE means WF bisects ∠IWE. By the angle bisector theorem, IF/FE = WI/WE.

But wait, we need to be careful about the order of points on line EF. Let me figure out the order.

I is at (x_I, 0) with x_I < 0 (to the left of B). F is at (a cos²B, a sin B cos B). E is at (a sin²C, a sin C cos C).

x_I < 0, and F, E have positive x-coordinates. So I is to the left, then F and E. The order on the line is I, then F, then E (or I, E, F). Let me check.

The line EF has slope tan(B-C) > 0 (since B > C). So as x increases, y increases. I is at x < 0, y = 0. F is at (a cos²B, a sin B cos B). E is at (a sin²C, a sin C cos C).

x_F = a cos²B, x_E = a sin²C. Which is bigger? cos²B vs sin²C. Since B > π/3 and C = 2B - π/2, let me compute for a specific B.

With B such that sin 2B = 2/5, B ≈ ... 2B ≈ arcsin(0.4) ≈ 0.4115 rad or π - 0.4115 ≈ 2.73 rad. Since 2B > 2π/3 ≈ 2.094, we have 2B ≈ 2.73, B ≈ 1.365 rad ≈ 78.2°. C = 2B - 90° ≈ 156.4° - 90° = 66.4°. A = 180° - 78.2° - 66.4° = 35.4°.

cos B ≈ cos 78.2° ≈ 0.204, sin C ≈ sin 66.4° ≈ 0.916. cos²B ≈ 0.0416, sin²C ≈ 0.839. So x_E > x_F. The order on the line (by x) is I (x<0), F, E. And since slope > 0, by y: I (y=0), F, E.

So on line EF, the order is I, F, E. F is between I and E. So WF bisects ∠IWE, and by angle bisector theorem: WI/WE = IF/FE.

Now I need to find WB/WI. W is on ray BF. Let me set up coordinates for W.

Ray BF: B = (0,0), F = (a cos²B, a sin B cos B). Direction from B to F: (cos²B, sin B cos B) = cos B (cos B, sin B). So the direction is (cos B, sin B), which is the direction of BA! Of course, since F is on AB.

So ray BF is the same as ray BA (from B toward A and beyond). W is on this ray.

W = t · (cos B, sin B) for some t > 0 (where t is the distance from B, since (cos B, sin B) is a unit vector). Actually, W = s(cos B, sin B) where s = BW.

Now I need to find W such that ∠IWF = ∠FWE, i.e., WF bisects ∠IWE.

Using the angle bisector theorem: WI/WE = IF/FE.

But this gives a condition on W. Let me compute.

First, let me find IF and FE.

I = (x_I, 0), F = (a cos²B, a sin B cos B), E = (a sin²C, a sin C cos C).

IF = distance from I to F. FE = distance from F to E.

Since I, F, E are collinear with slope tan(B-C):
IF = √((x_F - x_I)² + (y_F - 0)²) = √((a cos²B - x_I)² + (a sin B cos B)²).

This is getting complex. Let me use the parametric form on the line.

The line EF has direction (1, tan(B-C)) or equivalently (cos(B-C), sin(B-C)).

Let me parametrize points on line EF by a parameter. Let me use the foot of perpendicular or arc length.

Actually, let me use a cleaner approach. Let me place W = s(cos B, sin B) and use the angle bisector condition.

The angle bisector condition ∠IWF = ∠FWE with F between I and E on line IE means:
WI/WE = IF/FE (angle bisector theorem in triangle WIE).

Let me compute IF/FE first.

On line EF with slope tan(B-C), the distance between two points is √(1 + tan²(B-C)) · |Δx| = |Δx| / cos(B-C).

IF = |x_F - x_I| / cos(B-C) = (a cos²B - x_I) / cos(B-C) (since x_F > x_I).
FE = |x_E - x_F| / cos(B-C) = (x_E - x_F) / cos(B-C) (since x_E > x_F).

IF/FE = (a cos²B - x_I) / (x_E - x_F).

x_I = -a sin C cos B / sin(B-C).
a cos²B - x_I = a cos²B + a sin C cos B / sin(B-C) = a cos B (cos B + sin C / sin(B-C)) = a cos B (cos B sin(B-C) + sin C) / sin(B-C).

cos B sin(B-C) + sin C = cos B(sin B cos C - cos B sin C) + sin C = sin B cos B cos C - cos²B sin C + sin C = sin B cos B cos C + sin C(1 - cos²B) = sin B cos B cos C + sin C sin²B = sin B(cos B cos C + sin B sin C) = sin B cos(B - C).

So a cos²B - x_I = a cos B sin B cos(B-C) / sin(B-C) = a sin B cos B cos(B-C) / sin(B-C) = (a/2) sin 2B cos(B-C) / sin(B-C).

x_E - x_F = a sin²C - a cos²B = a(sin²C - cos²B) = a(-(cos²B - sin²C)) = -a(cos 2B + cos 2C)/2.

Hmm wait, sin²C - cos²B = (1-cos2C)/2 - (1+cos2B)/2 = -(cos2B + cos2C)/2.

cos 2B + cos 2C = 2 cos(B+C) cos(B-C) = 2 cos(π-A) cos(B-C) = -2 cos A cos(B-C).

So x_E - x_F = -a · (-2 cos A cos(B-C))/2 = a cos A cos(B-C).

So IF/FE = [(a/2) sin 2B cos(B-C) / sin(B-C)] / [a cos A cos(B-C)] = sin 2B / (2 sin(B-C) cos A).

Now WI/WE = IF/FE = sin 2B / (2 sin(B-C) cos A).

With our specific values: sin 2B = 2/5, cos A = cos(3π/2 - 3B).

A = 3π/2 - 3B. cos A = cos(3π/2 - 3B) = cos(3π/2)cos(3B) + sin(3π/2)sin(3B) = 0·cos(3B) + (-1)·sin(3B) = -sin(3B).

Since A is acute, cos A > 0, so -sin(3B) > 0, sin(3B) < 0. With B ≈ 78.2°, 3B ≈ 234.6°, sin(234.6°) ≈ -0.815. So cos A ≈ 0.815. And A ≈ 35.4°, cos 35.4° ≈ 0.815. ✓.

sin(B-C) = sin(B - (2B - π/2)) = sin(π/2 - B) = cos B.

So IF/FE = sin 2B / (2 cos B cos A) = (2 sin B cos B) / (2 cos B cos A) = sin B / cos A.

So WI/WE = sin B / cos A.

Now I need to find W on ray BF (i.e., W = s(cos B, sin B)) such that WI/WE = sin B / cos A, and then compute WB/WI = s/WI.

Let me compute WI and WE in terms of s.

W = (s cos B, s sin B).
I = (x_I, 0) where x_I = -a sin C cos B / sin(B-C) = -a sin C cos B / cos B = -a sin C.

Oh nice! Since sin(B-C) = cos B, x_I = -a sin C cos B / cos B = -a sin C.

So I = (-a sin C, 0).

WI = √((s cos B + a sin C)² + (s sin B)²) = √(s² cos²B + 2s a sin C cos B + a² sin²C + s² sin²B) = √(s² + 2sa sin C cos B + a² sin²C).

E = (a sin²C, a sin C cos C) = (a sin²C, a sin C cos C).

Wait, let me recompute. E = (c sin A sin C, c sin A cos C). And a = c sin A / sin C, so c sin A = a sin C. So E = (a sin²C, a sin C cos C). ✓.

WE = √((s cos B - a sin²C)² + (s sin B - a sin C cos C)²).

Let me expand:
= √(s² cos²B - 2sa sin²C cos B + a² sin⁴C + s² sin²B - 2sa sin C cos C sin B + a² sin²C cos²C)
= √(s² - 2sa(sin²C cos B + sin C cos C sin B) + a² sin²C(sin²C + cos²C))
= √(s² - 2sa sin C(sin C cos B + cos C sin B) + a² sin²C)
= √(s² - 2sa sin C sin(B + C) + a² sin²C)
= √(s² - 2sa sin C sin A + a² sin²C) [since sin(B+C) = sin(π-A) = sin A].

And WI = √(s² + 2sa sin C cos B + a² sin²C).

So WI² = s² + 2sa sin C cos B + a² sin²C.
WE² = s² - 2sa sin C sin A + a² sin²C.

The condition WI/WE = sin B / cos A means WI²/WE² = sin²B / cos²A.

Let me denote u = s² + a² sin²C, p = 2sa sin C.
WI² = u + p cos B.
WE² = u - p sin A.

So (u + p cos B)/(u - p sin A) = sin²B / cos²A.

Cross multiply: cos²A(u + p cos B) = sin²B(u - p sin A).
u(cos²A - sin²B) + p(cos²A cos B + sin²B sin A) = 0.
u(cos²A - sin²B) = -p(cos²A cos B + sin²B sin A).

Now cos²A - sin²B = cos²A - sin²B. And we need to simplify cos²A cos B + sin²B sin A.

Hmm, this is getting complicated. Let me use the specific angle relations.

We have: 2B - C = π/2, A = 3π/2 - 3B, sin 2B = 2/5, cos 2B = -√21/5.

Let me compute the needed quantities.

cos B: sin 2B = 2 sin B cos B = 2/5. cos 2B = cos²B - sin²B = -√21/5. Also cos²B + sin²B = 1.
cos²B = (1 + cos 2B)/2 = (1 - √21/5)/2 = (5 - √21)/10.
sin²B = (1 - cos 2B)/2 = (1 + √21/5)/2 = (5 + √21)/10.

sin B = √((5 + √21)/10), cos B = √((5 - √21)/10).

C = 2B - π/2. sin C = sin(2B - π/2) = -cos 2B = √21/5. cos C = cos(2B - π/2) = sin 2B = 2/5. ✓ (given cos C = 2/5).

A = 3π/2 - 3B. 
sin A = sin(3π/2 - 3B) = -cos 3B.
cos A = cos(3π/2 - 3B) = -sin 3B.

sin 3B = 3 sin B - 4 sin³B. cos 3B = 4 cos³B - 3 cos B.

Let me compute sin 3B and cos 3B.
sin B = √((5+√21)/10). Let me denote s = sin B, c = cos B.
s² = (5+√21)/10, c² = (5-√21)/10.
sc = sin 2B / 2 = 1/5.

sin 3B = 3s - 4s³ = s(3 - 4s²) = s(3 - 4(5+√21)/10) = s(3 - (20+4√21)/10) = s((30 - 20 - 4√21)/10) = s(10 - 4√21)/10 = s(5 - 2√21)/5.

cos 3B = 4c³ - 3c = c(4c² - 3) = c(4(5-√21)/10 - 3) = c((20-4√21)/10 - 3) = c((20-4√21-30)/10) = c(-10-4√21)/10 = c(-5-2√21)/5.

So sin A = -cos 3B = -c(-5-2√21)/5 = c(5+2√21)/5.
cos A = -sin 3B = -s(5-2√21)/5 = s(2√21-5)/5.

Note: 2√21 ≈ 9.165, so 2√21 - 5 ≈ 4.165 > 0. And 5 - 2√21 ≈ -4.165 < 0. So sin 3B = s(5-2√21)/5 < 0 (since s > 0 and 5-2√21 < 0), which means cos A = -sin 3B > 0. ✓.

Let me verify: cos A = s(2√21 - 5)/5. With s = √((5+√21)/10) ≈ √(0.9589/... wait let me compute numerically.

√21 ≈ 4.5826.
s² = (5 + 4.5826)/10 = 9.5826/10 = 0.95826. s ≈ 0.9789.
c² = (5 - 4.5826)/10 = 0.4174/10 = 0.04174. c ≈ 0.2043.

sin A = c(5 + 2·4.5826)/5 = 0.2043 · (5 + 9.165)/5 = 0.2043 · 14.165/5 = 0.2043 · 2.833 = 0.5788.
cos A = s(2·4.5826 - 5)/5 = 0.9789 · (9.165 - 5)/5 = 0.9789 · 4.165/5 = 0.9789 · 0.833 = 0.8152.

A ≈ arcsin(0.5788) ≈ 35.4°. ✓.

Now let me compute the ratio. We have:

cos²A - sin²B = cos²A - s².
cos²A = s²(2√21-5)²/25 = s²(4·21 - 20√21 + 25)/25 = s²(84 - 20√21 + 25)/25 = s²(109 - 20√21)/25.

cos²A - sin²B = s²(109 - 20√21)/25 - s² = s²((109 - 20√21) - 25)/25 = s²(84 - 20√21)/25 = s²·4(21 - 5√21)/25.

Hmm, 21 - 5√21 = 21 - 5·4.5826 = 21 - 22.913 = -1.913. So this is negative.

cos²A cos B + sin²B sin A:
= [s²(109-20√21)/25] · c + s² · [c(5+2√21)/5]
= s²c [(109-20√21)/25 + (5+2√21)/5]
= s²c [(109-20√21)/25 + 5(5+2√21)/25]
= s²c [(109-20√21 + 25+10√21)/25]
= s²c [(134 - 10√21)/25]
= s²c · 2(67 - 5√21)/25.

Now the equation: u(cos²A - sin²B) = -p(cos²A cos B + sin²B sin A).

u · s²·4(21-5√21)/25 = -p · s²c·2(67-5√21)/25.

Cancel s²/25: u · 4(21-5√21) = -p · 2c(67-5√21).

u/p = -2c(67-5√21) / [4(21-5√21)] = -c(67-5√21) / [2(21-5√21)].

u = s² + a² sin²C, p = 2sa sin C.

u/p = (s² + a² sin²C) / (2sa sin C).

Let me set t = a sin C / s (ratio). Then u = s²(1 + t²), p = 2s²t. u/p = (1+t²)/(2t).

So (1+t²)/(2t) = -c(67-5√21) / [2(21-5√21)].

(1+t²)/t = -c(67-5√21)/(21-5√21).

Let me compute the right side numerically.
67 - 5√21 = 67 - 22.913 = 44.087.
21 - 5√21 = 21 - 22.913 = -1.913.
-c(67-5√21)/(21-5√21) = -0.2043 · 44.087 / (-1.913) = 0.2043 · 44.087 / 1.913 = 0.2043 · 23.04 = 4.707.

So (1+t²)/t = 4.707, i.e., t + 1/t = 4.707, t² - 4.707t + 1 = 0.
t = (4.707 ± √(22.16 - 4))/2 = (4.707 ± √18.16)/2 = (4.707 ± 4.262)/2.
t = 4.485 or t = 0.223.

Since W is on ray BF and we need a specific W, let me figure out which t is correct. t = a sin C / s. a = c sin A / sin C, so a sin C = c sin A. t = c sin A / s = c sin A / sin B.

By sine rule, c/sin C = a/sin A = b/sin B = 2R. So c = 2R sin C, and t = 2R sin C sin A / sin B.

Hmm, this doesn't immediately tell me which root. Let me think about it differently.

We want WB/WI = s/WI. WI = √(s² + 2sa sin C cos B + a² sin²C) = √(u + p cos B) = √(s²(1+t²) + 2s²t cos B) = s√(1 + t² + 2t cos B).

So WB/WI = s / (s√(1 + t² + 2t cos B)) = 1/√(1 + t² + 2t cos B).

For t = 4.485: 1 + t² + 2t cos B = 1 + 20.12 + 2·4.485·0.2043 = 1 + 20.12 + 1.833 = 22.95. WB/WI = 1/√22.95 = 1/4.79 ≈ 0.209.

For t = 0.223: 1 + t² + 2t cos B = 1 + 0.0497 + 2·0.223·0.2043 = 1 + 0.0497 + 0.0911 = 1.141. WB/WI = 1/√1.141 = 1/1.068 ≈ 0.936.

Hmm, I need to determine which root is correct. Let me think about the geometry.

W is on ray BF (from B through F). F is on segment AB. The ray goes from B through F and beyond A. W could be between B and F, at F, between F and A, at A, or beyond A.

The angle bisector condition: WF bisects ∠IWE where I, F, E are on line with F between I and E. For this to make sense, W must be on the opposite side of line IE from... well, W is not on line IE, and the angle bisector from W to side IE hits at F.

For the angle bisector to hit at F (which is between I and E), W must be such that the angle bisector from W in triangle WIE lands at F. This is always possible for any W not on line IE, and the angle bisector theorem gives WI/WE = IF/FE. So both roots might be geometrically valid, but we need to check which gives a valid configuration.

Actually, wait. The problem says W is on ray BF such that ∠IWF = ∠FWE. There might be two such points (one on each side of F along the ray, or the angle bisector condition might have two solutions). But actually, the angle bisector theorem gives a unique ratio WI/WE = IF/FE, and the locus of points with WI/WE = constant is an Apollonius circle, which intersects the ray BF in at most 2 points. So there could be two solutions.

Let me check if both are on the ray (s > 0). s = WB > 0 for both since we're on the ray. Both t values are positive, so both give s > 0. 

Hmm, but the problem says "Let W be a point on ray BF such that..." suggesting there might be a unique such point, or the answer is the same for both. Let me check if the problem expects a unique answer.

Actually, let me reconsider. The condition is ∠IWF = ∠FWE. This means the angle from WI to WF equals the angle from WF to WE. This is the angle bisector condition, but it could also be the external angle bisector. If F is between I and E, then the internal bisector gives WI/WE = IF/FE, and the external bisector gives WI/WE = IF/FE as well but with W on the other side... no, the external bisector would give -WI/WE = IF/FE, which doesn't make sense for distances.

Actually, the internal angle bisector from W in triangle WIE hits side IE at F, giving WI/WE = IF/FE. The external angle bisector would hit the extension of IE, not the segment IE. Since F is between I and E (on the segment), it must be the internal bisector. So WI/WE = IF/FE.

But the Apollonius circle WI/WE = k (constant) can intersect the ray in 0, 1, or 2 points. Here we get 2 points. The problem says "a point," so maybe both give the same WB/WI? Let me check.

For t = 4.485: WB/WI ≈ 0.209.
For t = 0.223: WB/WI ≈ 0.936.

These are different, so the problem must have a unique solution. Let me reconsider.

Maybe I need to check which W actually satisfies ∠IWF = ∠FWE (not just the ratio). The angle bisector theorem gives a necessary condition, but I should verify that F is actually between I and E and that the angles work out.

Actually, the angle bisector theorem is both necessary and sufficient (for internal bisector): if WI/WE = IF/FE and F is between I and E, then WF bisects ∠IWE. So both points satisfy the condition. 

Hmm, but maybe one of them doesn't actually have F between I and E from W's perspective, or the angles are measured differently. Let me reconsider the problem.

Wait, actually, maybe I need to reconsider. The problem says ∠IWF = ∠FWE. These are undirected angles. If W is on one side of line IE, then ∠IWF and ∠FWE are both positive and the condition means WF bisects ∠IWE. But if W is positioned such that I and E are on the same side of WF, then the angles might be different.

Actually, since I, F, E are collinear with F between I and E, and W is off the line, the rays WI, WF, WE emanate from W. The angle ∠IWE is split by WF into ∠IWF and ∠FWE. So ∠IWF = ∠FWE means WF bisects ∠IWE. This is unambiguous.

So both roots are valid. Let me re-examine whether the problem has additional constraints I'm missing.

"Let W be a point on ray BF such that ∠IWF = ∠FWE."

Ray BF starts at B and goes through F. F is on segment AB. So the ray goes from B, through F, through A, and beyond. 

Hmm, maybe the problem expects both solutions to give the same answer, and I made a computational error. Let me recheck.

Actually, let me reconsider. Maybe I should check: is W between B and F, or beyond F? If W is between B and F, then W is inside the triangle, and the angle bisector from W to IE might not hit at F. Let me think...

F is on segment AB. The line IE (= line EF) passes through F. If W is on segment BF (between B and F), then W is on one side of line EF, and the angle bisector from W to line EF would hit at some point on EF. For it to hit at F specifically, we need WI/WE = IF/FE.

Both solutions for t (hence for s = WB) are positive, so both are on the ray. But one might be between B and F, and the other beyond F.

BF = distance from B to F. F = (a cos²B, a sin B cos B). BF = a cos B √(cos²B + sin²B) = a cos B. Wait, F = a cos B (cos B, sin B), so BF = a cos B.

s = WB. We need to compare s with BF = a cos B.

t = a sin C / s, so s = a sin C / t.

BF = a cos B. s/BF = sin C / (t cos B).

sin C = √21/5 ≈ 0.9165, cos B ≈ 0.2043.

For t = 4.485: s/BF = 0.9165 / (4.485 · 0.2043) = 0.9165 / 0.9163 ≈ 1.0002. So s ≈ BF, meaning W ≈ F.

For t = 0.223: s/BF = 0.9165 / (0.223 · 0.2043) = 0.9165 / 0.04556 = 20.12. So W is way beyond F.

Hmm, so for t = 4.485, W is approximately at F. Let me check more carefully.

If W = F, then ∠IWF = ∠IFF which is undefined (W = F). So W can't be exactly at F. But t ≈ 4.485 gives W very close to F. Let me recompute more carefully.

Actually, let me recompute t more carefully using exact values.

We have (1+t²)/t = -c(67-5√21)/(21-5√21).

Let me simplify -c(67-5√21)/(21-5√21).

Note: 21 - 5√21 = √21(√21 - 5). And 67 - 5√21... let me see if there's a simplification.

Actually, let me try to simplify using the relation 2B - C = π/2 more carefully, and see if the answer simplifies.

Let me try a completely different approach. Let me use the specific values and compute everything numerically first, then try to identify the exact answer.

sin 2B = 2/5, cos 2B = -√21/5.
sin B = √((5+√21)/10), cos B = √((5-√21)/10).
sin C = √21/5, cos C = 2/5.
sin A = -cos 3B, cos A = -sin 3B.

Let me compute sin A and cos A exactly.
sin 3B = 3s - 4s³ where s = sin B.
s² = (5+√21)/10.
s³ = s · s² = s(5+√21)/10.
sin 3B = 3s - 4s(5+√21)/10 = s[3 - 2(5+√21)/5] = s[(15 - 10 - 2√21)/5] = s(5 - 2√21)/5.

cos A = -sin 3B = s(2√21 - 5)/5.

cos 3B = 4c³ - 3c where c = cos B.
c² = (5-√21)/10.
c³ = c(5-√21)/10.
cos 3B = 4c(5-√21)/10 - 3c = c[2(5-√21)/5 - 3] = c[(10-2√21-15)/5] = c(-5-2√21)/5.

sin A = -cos 3B = c(5+2√21)/5.

Now let me compute IF/FE = sin B / cos A = s / [s(2√21-5)/5] = 5/(2√21-5).

Rationalize: 5/(2√21-5) = 5(2√21+5)/((2√21)²-25) = 5(2√21+5)/(84-25) = 5(2√21+5)/59 = (10√21+25)/59.

Numerically: (10·4.5826+25)/59 = (45.826+25)/59 = 70.826/59 = 1.2004.

So WI/WE ≈ 1.2004.

Now let me set up the equation for W more carefully. W = s(cos B, sin B) on ray BF.

Let me use coordinates with a = 1 (scale doesn't matter for ratios). Actually, let me keep a general but remember WB/WI is scale-invariant.

Let me set a = 1. Then:
B = (0,0), C = (1, 0).
c = a sin C / sin A = sin C / sin A.
b = a sin B / sin A = sin B / sin A.

I = (-sin C, 0) = (-√21/5, 0).
F = (cos²B, sin B cos B) = ((5-√21)/10, 1/5) [since sin B cos B = sin 2B/2 = 1/5].

Wait, with a = 1: F = (cos²B, sin B cos B) = ((5-√21)/10, 1/5).

E = (sin²C, sin C cos C) = (21/25, 2√21/25).

K is on x = c cos B and on line EF. But we don't need K anymore.

W = s(cos B, sin B) = s(√((5-√21)/10), √((5+√21)/10)).

Let me use the notation: cB = cos B = √((5-√21)/10), sB = sin B = √((5+√21)/10).

W = (s · cB, s · sB).

WI² = (s·cB + √21/5)² + (s·sB)² = s²cB² + 2s·cB·√21/5 + 21/25 + s²sB² = s² + 2s·cB·√21/5 + 21/25.

WE² = (s·cB - 21/25)² + (s·sB - 2√21/25)²
= s²cB² - 2s·cB·21/25 + 441/625 + s²sB² - 2s·sB·2√21/25 + 4·21/625
= s² - 2s(21cB + 2√21·sB)/25 + (441+84)/625
= s² - 2s(21cB + 2√21·sB)/25 + 525/625
= s² - 2s(21cB + 2√21·sB)/25 + 21/25.

So WI² = s² + 2s·cB·√21/5 + 21/25.
WE² = s² - 2s(21cB + 2√21·sB)/25 + 21/25.

Let me simplify 21cB + 2√21·sB.
21cB + 2√21·sB = 21√((5-√21)/10) + 2√21·√((5+√21)/10).

Hmm, let me compute this. Let me factor out 1/√10:
= [21√(5-√21) + 2√21·√(5+√21)] / √10.

This is messy. Let me try a different approach.

Note that 21cB + 2√21 sB = 21 cos B + 2√21 sin B. Can I write this as R cos(B - φ) for some R, φ?

R = √(441 + 4·21) = √(441 + 84) = √525 = 5√21.
So 21 cos B + 2√21 sin B = 5√21 cos(B - φ) where tan φ = 2√21/21 = 2/√21.

Hmm, 5√21 cos(B - φ) where tan φ = 2/√21. Note cos C = 2/5 and sin C = √21/5, so tan C = √21/2, and 1/tan C = 2/√21. So φ = π/2 - C.

So 21 cos B + 2√21 sin B = 5√21 cos(B - (π/2 - C)) = 5√21 cos(B + C - π/2) = 5√21 cos(π - A - π/2) = 5√21 cos(π/2 - A) = 5√21 sin A.

So 21cB + 2√21 sB = 5√21 sin A.

And cB · √21/5 = √21 cos B / 5 = sin C cos B / ... wait, √21/5 = sin C. So cB · √21/5 = sin C cos B.

So:
WI² = s² + 2s sin C cos B + sin²C. [since 21/25 = sin²C]
WE² = s² - 2s · 5√21 sin A / 25 + sin²C = s² - 2s √21 sin A / 5 + sin²C = s² - 2s sin C sin A + sin²C. [since √21/5 = sin C]

Great, this matches what I had before.

WI² = s² + 2s sin C cos B + sin²C.
WE² = s² - 2s sin C sin A + sin²C.

WI²/WE² = (sin B / cos A)² = sin²B / cos²A.

Let me denote k = sin²B / cos²A. Then:
(s² + 2s sin C cos B + sin²C) = k(s² - 2s sin C sin A + sin²C).

(1-k)s² + 2s sin C(cos B + k sin A) + sin²C(1-k) = 0.

If k ≠ 1:
s² + [2 sin C(cos B + k sin A)/(1-k)] s + sin²C = 0.

This is a quadratic in s. The product of roots is sin²C (by Vieta's), and the sum is -2 sin C(cos B + k sin A)/(1-k).

Now WB/WI = s/WI = s/√(s² + 2s sin C cos B + sin²C).

Let me compute this for both roots. Actually, let me try to find WB/WI directly.

WB/WI = s/√(s² + 2s sin C cos B + sin²C).

Let me denote r = WB/WI. Then r² = s²/(s² + 2s sin C cos B + sin²C).

1/r² = 1 + 2 sin C cos B / s + sin²C/s².

Let u = sin C / s. Then 1/r² = 1 + 2u cos B + u² = (u + cos B)² + sin²B.

So r² = 1/((u + cos B)² + sin²B).

Now u = sin C / s, and s satisfies the quadratic. Let me find u.

From s² + [2 sin C(cos B + k sin A)/(1-k)] s + sin²C = 0, dividing by s²:
1 + [2 sin C(cos B + k sin A)/(1-k)] / s + sin²C/s² = 0.
1 + 2u(cos B + k sin A)/(1-k) + u² = 0.
u² + 2u(cos B + k sin A)/(1-k) + 1 = 0.

Product of roots in u: u₁u₂ = 1. Sum: u₁ + u₂ = -2(cos B + k sin A)/(1-k).

For each root u, r² = 1/((u + cos B)² + sin²B).

Let me compute k = sin²B/cos²A.

sin²B = (5+√21)/10.
cos²A = s²(2√21-5)²/25 = [(5+√21)/10] · (2√21-5)²/25.

(2√21-5)² = 4·21 - 20√21 + 25 = 84 - 20√21 + 25 = 109 - 20√21.

cos²A = (5+√21)(109-20√21)/(10·25) = (5+√21)(109-20√21)/250.

Let me compute (5+√21)(109-20√21) = 5·109 - 100√21 + 109√21 - 20·21 = 545 + 9√21 - 420 = 125 + 9√21.

So cos²A = (125 + 9√21)/250.

k = sin²B/cos²A = [(5+√21)/10] / [(125+9√21)/250] = (5+√21)/10 · 250/(125+9√21) = 25(5+√21)/(125+9√21).

Let me rationalize: 25(5+√21)/(125+9√21) = 25(5+√21)(125-9√21)/((125)²-81·21) = 25(5+√21)(125-9√21)/(15625-1701) = 25(5+√21)(125-9√21)/13924.

(5+√21)(125-9√21) = 625 - 45√21 + 125√21 - 9·21 = 625 + 80√21 - 189 = 436 + 80√21.

k = 25(436+80√21)/13924 = 25·4(109+20√21)/13924 = 100(109+20√21)/13924.

13924 = 4·3481 = 4·3481. 3481 = 59². So 13924 = 4·59².

k = 100(109+20√21)/(4·59²) = 25(109+20√21)/59² = 25(109+20√21)/3481.

Hmm, this is getting messy. Let me try numerical approach to identify the answer.

k = sin²B/cos²A ≈ 0.95826/0.6646 ≈ 1.4419.

1-k ≈ -0.4419.

cos B + k sin A ≈ 0.2043 + 1.4419·0.5788 ≈ 0.2043 + 0.8346 = 1.0389.

Sum of u roots: -2·1.0389/(-0.4419) = 2.0778/0.4419 = 4.703.
Product: 1.

u = (4.703 ± √(4.703²-4))/2 = (4.703 ± √(22.12-4))/2 = (4.703 ± √18.12)/2 = (4.703 ± 4.257)/2.
u₁ = 4.480, u₂ = 0.223.

For u₁ = 4.480:
r² = 1/((4.480 + 0.2043)² + 0.95826) = 1/(4.6843² + 0.95826) = 1/(21.94 + 0.958) = 1/22.90 = 0.04367.
r = 0.2090.

For u₂ = 0.223:
r² = 1/((0.223 + 0.2043)² + 0.95826) = 1/(0.4273² + 0.95826) = 1/(0.1826 + 0.9583) = 1/1.1409 = 0.8765.
r = 0.9362.

Hmm, let me see if either of these is a nice number.

r₁ ≈ 0.2090. 1/r₁ ≈ 4.785. r₁² ≈ 0.0437. 1/r₁² ≈ 22.9.

r₂ ≈ 0.9362. 1/r₂ ≈ 1.0681. r₂² ≈ 0.8765. 1/r₂² ≈ 1.1409.

Let me check if 1/r₂² = 1.1409 is something nice. 1.1409 ≈ 59/... 59/51.75... no. Let me try to see if it's a ratio of small integers or involves √21.

1.1409 · 25 = 28.52. Not obviously nice.
1/r₂² = (u₂ + cos B)² + sin²B where u₂ is a root of u² + 2u(cos B + k sin A)/(1-k) + 1 = 0.

This is getting very messy. Let me try a different approach—maybe I should look for the answer in a simpler form.

Let me reconsider. Maybe there's a more elegant geometric approach.

Actually, let me reconsider the problem. W is on ray BF, and ∠IWF = ∠FWE. Since I, F, E are collinear, this means WF bisects ∠IWE. But there's another interpretation: maybe W is chosen so that this angle condition holds, and there's a unique such W on the ray (not two).

Let me reconsider: the Apollonius circle for WI/WE = constant intersects the ray BF in at most 2 points. But maybe one of them doesn't actually satisfy the angle condition (e.g., if F is not between I and E from W's perspective, or if the angles are on the wrong side).

Actually, both points on the ray satisfy WI/WE = IF/FE, and since F is between I and E, both give WF as the angle bisector. So both are valid. But the problem says "a point," suggesting uniqueness. Maybe the problem has a unique answer regardless, or maybe I need to check additional constraints.

Wait, let me re-examine. For W very close to F (u₁ ≈ 4.48, s ≈ BF), W is near F. As W → F, the angle ∠IWF → ∠IFF which is 0 (degenerate). So W = F is a degenerate case. The solution u₁ gives W very close to F but not at F. Let me check: is u₁ exactly giving W = F?

If W = F, then s = BF = a cos B (with a=1, s = cos B). u = sin C / s = sin C / cos B = (√21/5) / √((5-√21)/10) = (√21/5) · √(10/(5-√21)).

√(10/(5-√21)) = √(10(5+√21)/((5-√21)(5+√21))) = √(10(5+√21)/(25-21)) = √(10(5+√21)/4) = √(5(5+√21)/2).

u = (√21/5) · √(5(5+√21)/2) = √21 · √(5(5+√21)/2) / 5 = √(21·5(5+√21)/2) / 5 = √(105(5+√21)/2) / 5.

105(5+√21)/2 = (525 + 105√21)/2. 

Numerically: (525 + 105·4.5826)/2 = (525+481.17)/2 = 1006.17/2 = 503.09. √503.09 = 22.43. u = 22.43/5 = 4.486.

So u at W=F is ≈ 4.486, which matches u₁ ≈ 4.480. The small difference is due to rounding. So u₁ corresponds to W = F!

But W = F is degenerate (∠IWF is undefined). So u₁ is actually the degenerate solution and should be excluded. The valid solution is u₂.

Wait, but u₁ is not exactly at F—it's a root of the quadratic, and the quadratic comes from the angle bisector condition. If W = F exactly, then WI/WE = IF/FE (trivially, since W = F means WI = FI and WE = FE, so WI/WE = IF/FE). So W = F does satisfy the ratio condition! But the angle ∠IWF is undefined at W = F.

So the quadratic has W = F as one root (degenerate) and another root as the actual solution. The actual answer is u₂.

So WB/WI = r₂ ≈ 0.9362.

Let me try to find the exact value. We have:

r² = 1/((u + cos B)² + sin²B) where u = u₂.

Since u₁ · u₂ = 1 and u₁ = sin C / cos B (the value at W = F), we get:
u₂ = 1/u₁ = cos B / sin C.

Let me verify: u₁ = sin C / cos B (at W = F, s = cos B, u = sin C/s = sin C/cos B). Then u₂ = cos B / sin C.

Check: u₁ · u₂ = (sin C/cos B)(cos B/sin C) = 1. ✓.

Check numerically: u₂ = 0.2043/0.9165 = 0.2230. ✓.

So u₂ = cos B / sin C.

r² = 1/((cos B/sin C + cos B)² + sin²B) = 1/(cos²B(1/sin C + 1)² + sin²B)
= 1/(cos²B(1 + sin C)²/sin²C + sin²B)
= 1/((cos²B(1+sin C)² + sin²B sin²C) / sin²C)
= sin²C / (cos²B(1+sin C)² + sin²B sin²C).

Let me expand the denominator:
cos²B(1 + sin C)² + sin²B sin²C = cos²B(1 + 2 sin C + sin²C) + sin²B sin²C
= cos²B + 2 cos²B sin C + cos²B sin²C + sin²B sin²C
= cos²B + 2 cos²B sin C + sin²C(cos²B + sin²B)
= cos²B + 2 cos²B sin C + sin²C.

So r² = sin²C / (cos²B + 2 cos²B sin C + sin²C) = sin²C / (cos²B(1 + 2 sin C) + sin²C).

Now let me plug in the values.
sin C = √21/5, sin²C = 21/25.
cos²B = (5-√21)/10.

cos²B(1 + 2 sin C) = (5-√21)/10 · (1 + 2√21/5) = (5-√21)/10 · (5 + 2√21)/5 = (5-√21)(5+2√21)/50.

(5-√21)(5+2√21) = 25 + 10√21 - 5√21 - 2·21 = 25 + 5√21 - 42 = -17 + 5√21.

cos²B(1 + 2 sin C) = (-17 + 5√21)/50.

Denominator = (-17 + 5√21)/50 + 21/25 = (-17 + 5√21)/50 + 42/50 = (25 + 5√21)/50 = 5(5 + √21)/50 = (5 + √21)/10.

So r² = (21/25) / ((5+√21)/10) = (21/25) · (10/(5+√21)) = 210/(25(5+√21)) = 42/(5(5+√21)).

Rationalize: 42/(5(5+√21)) = 42(5-√21)/(5(25-21)) = 42(5-√21)/(5·4) = 42(5-√21)/20 = 21(5-√21)/10.

So r² = 21(5-√21)/10.

r = √(21(5-√21)/10).

Let me verify numerically: 21(5-4.5826)/10 = 21·0.4174/10 = 8.765/10 = 0.8765. √0.8765 = 0.9362. ✓!

So WB/WI = √(21(5-√21)/10).

Let me simplify. 21(5-√21)/10 = (105 - 21√21)/10.

Can this be simplified further? Let me check if 21(5-√21)/10 is a perfect square of something nice.

21(5-√21) = 105 - 21√21. 

Let me see: (√a - √b)² = a + b - 2√(ab). If a + b = 105/10 = 10.5 and 2√(ab) = 21√21/10 = 2.1√21, then ab = (2.1√21/2)² = (1.05√21)² = 1.1025·21 = 23.1525. And a + b = 10.5, ab = 23.1525. Discriminant: 10.5² - 4·23.1525 = 110.25 - 92.61 = 17.64 = 4.2². So a,b = (10.5 ± 4.2)/2 = 7.35 or 3.15. Not nice.

Let me try another form. r² = 21(5-√21)/10. 

Note that 5 - √21 = (5-√21)(5+√21)/(5+√21) = 4/(5+√21). So r² = 21·4/(10(5+√21)) = 84/(10(5+√21)) = 42/(5(5+√21)).

Hmm, let me try: r = √(21(5-√21)/10). Let me see if this simplifies to something like √(21/10) · √(5-√21).

√(5-√21) = √(5-√21). Note (√3 - √(7/...))²... Let me try √(5-√21) = √a - √b where a+b=5, 2√(ab)=√21, ab=21/4. a+b=5, ab=21/4. Discriminant: 25-21=4. a,b=(5±2)/2=7/2, 3/2. So √(5-√21) = √(7/2) - √(3/2) = (√7-√3)/√2.

So r = √(21/10) · (√7-√3)/√2 = √(21/(10·2)) · (√7-√3) = √(21/20) · (√7-√3) = (√21/(2√5)) · (√7-√3).

= (√21·√7 - √21·√3)/(2√5) = (√147 - √63)/(2√5) = (7√3 - 3√7)/(2√5).

Rationalize: (7√3 - 3√7)/(2√5) = (7√3 - 3√7)√5/(2·5) = (7√15 - 3√35)/10.

Let me verify: (7√15 - 3√35)/10. 
7√15 ≈ 7·3.873 = 27.11. 3√35 ≈ 3·5.916 = 17.75. (27.11-17.75)/10 = 9.36/10 = 0.936. ✓!

So WB/WI = (7√15 - 3√35)/10.

Let me double-check: r² = (7√15 - 3√35)²/100 = (49·15 + 9·35 - 2·7·3·√(15·35))/100 = (735 + 315 - 42√525)/100 = (1050 - 42·5√21)/100 = (1050 - 210√21)/100 = (105 - 21√21)/10 = 21(5-√21)/10. ✓!

So WB/WI = (7√15 - 3√35)/10.

Wait, but I should double-check that u₁ exactly equals sin C / cos B, i.e., that W = F is exactly a root. Let me verify this.

At W = F, s = BF = a cos B (with a = 1, s = cos B). Then:
WI = FI, WE = FE. WI/WE = FI/FE = IF/FE (same thing). And we showed IF/FE = sin B / cos A. So WI/WE = sin B / cos A = √k. So W = F satisfies the ratio condition. ✓.

So the quadratic in s (or u) has W = F as one root, and the other root gives the actual W. Since u = sin C / s, at W = F, u = sin C / cos B. The other root is u = cos B / sin C (product = 1).

Therefore WB/WI = (7√15 - 3√35)/10.

Actually, let me reconsider whether the answer might be expected in the form √(21(5-√21)/10) or (7√15-3√35)/10. Both are equivalent. Let me also verify the whole solution makes sense.

Let me also double-check the key step: the cyclic condition giving cos(2B - C) = 0.

We had:
- ∠AIB + ∠AKB = 180° (opposite angles in cyclic quad AKBI, with vertices in order A, I, B, K).
- ∠AIB = arctan(sin(B-C)/(2 cos B cos C)).
- ∠AKB = 90° + arctan(y_K / d) where d = c cos B and y_K is the y-coordinate of K on EF.

From the cyclic condition: arctan(sin(B-C)/(2cosB cosC)) + 90° + arctan(y_K/d) = 180°.
arctan(y_K/d) = 90° - arctan(sin(B-C)/(2cosB cosC)).
y_K/d = cot(arctan(sin(B-C)/(2cosB cosC))) = 2cosB cosC / sin(B-C).

From the line EF: y_K = 2c sinB cosB cosC / cos(B-C), d = c cosB.
y_K/d = 2 sinB cosC / cos(B-C).

Setting equal: 2 sinB cosC / cos(B-C) = 2 cosB cosC / sin(B-C).
sinB / cos(B-C) = cosB / sin(B-C).
sinB sin(B-C) = cosB cos(B-C).
cos(B + (B-C)) = 0 [since cosB cos(B-C) - sinB sin(B-C) = cos(B+(B-C)) = cos(2B-C)].
cos(2B - C) = 0. ✓.

So 2B - C = π/2 (taking the value in the correct range for an acute triangle with B > C).

Then C = 2B - π/2, and cos C = sin 2B = 2/5. ✓.

Everything checks out. The answer is (7√15 - 3√35)/10.

Let me also verify this is positive: 7√15 ≈ 27.11, 3√35 ≈ 17.75, difference ≈ 9.36, divided by 10 ≈ 0.936. Positive. ✓.

And it's less than 1, which makes sense if WI > WB (W is on ray BF, I is to the left of B, so WI > WB if W is not too far... actually for W beyond F, WI could be larger than WB). ✓.

So the final answer is $\frac{7\sqrt{15} - 3\sqrt{35}}{10}$.

Let me also sanity-check by verifying the answer with a slightly different numerical computation.

With a = 1:
B = (0,0), C = (1,0).
sin C = √21/5 ≈ 0.91652, cos C = 2/5 = 0.4.
I = (-sin C, 0) = (-0.91652, 0).
cos B = √((5-√21)/10) ≈ √(0.041742) ≈ 0.20431.
sin B = √((5+√21)/10) ≈ √(0.95826) ≈ 0.97894.

W = s(cos B, sin B) where s = sin C / u₂ = sin C · sin C / cos B = sin²C / cos B.
s = (21/25) / 0.20431 = 0.84 / 0.20431 = 4.1114.

W = (4.1114 · 0.20431, 4.1114 · 0.97894) = (0.8396, 4.0249).

WB = s = 4.1114.
WI = √((0.8396 + 0.91652)² + 4.0249²) = √(1.7561² + 4.0249²) = √(3.084 + 16.200) = √19.284 = 4.391.

WB/WI = 4.1114/4.391 = 0.9363. ✓ (matches (7√15-3√35)/10 ≈ 0.9362).

Great, the answer is confirmed.

Now let me also verify that the angle condition holds. ∠IWF = ∠FWE.

W = (0.8396, 4.0249), I = (-0.91652, 0), F = (cos²B, sinB cosB) = (0.041742, 0.2), E = (sin²C, sinC cosC) = (0.840, 0.36661).

Wait, E = (sin²C, sinC cosC) = (21/25, 2√21/25) = (0.84, 0.36661). And W = (0.8396, 4.0249). So W is almost directly above E!

WI = distance from W to I = √((0.8396+0.91652)² + 4.0249²) = √(3.084 + 16.200) = √19.284 = 4.391.
WE = distance from W to E = √((0.8396-0.84)² + (4.0249-0.36661)²) = √(0.000016 + 13.374) = √13.374 = 3.657.
WI/WE = 4.391/3.657 = 1.2007.

IF/FE: I = (-0.91652, 0), F = (0.041742, 0.2), E = (0.84, 0.36661).
IF = √((0.041742+0.91652)² + 0.2²) = √(0.91788 + 0.04) = √0.95788 = 0.97881.
FE = √((0.84-0.041742)² + (0.36661-0.2)²) = √(0.63708 + 0.027744) = √0.66482 = 0.81539.
IF/FE = 0.97881/0.81539 = 1.2004.

WI/WE ≈ IF/FE ≈ 1.200. ✓ (small numerical error).

Everything checks out. The answer is $\frac{7\sqrt{15} - 3\sqrt{35}}{10}$.

Now let me write up the proof.
