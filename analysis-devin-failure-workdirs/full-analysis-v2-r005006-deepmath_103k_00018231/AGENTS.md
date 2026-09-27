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
  <problem_id>deepmath_103k_00018231</problem_id>
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

Find the distance from the point \((2, 3, 4)\) to the line given by \(\frac{x+3}{3} = \frac{y-2}{6} = \frac{z}{2}\), measured parallel to the plane \(3x + 2y + 2z + 5 = 0\).

## Standard Solution

Okay, so I need to find the distance from the point (2, 3, 4) to the line given by (x+3)/3 = (y-2)/6 = z/2, measured parallel to the plane 3x + 2y + 2z + 5 = 0. Hmm, that sounds a bit complicated, but let's break it down step by step.

First, I remember that the distance from a point to a line in 3D space is usually found using the formula involving the cross product. But wait, the problem says "measured parallel to the plane". So, this distance isn't the usual perpendicular distance, but rather the distance measured along a direction that's parallel to the given plane. That probably means we have to project the usual distance onto the plane or something like that. I need to think carefully.

Let me recall that if we need a distance measured in a specific direction or parallel to a plane, it's related to projecting the vector onto a certain subspace. Since the measurement is parallel to the plane, the direction in which we measure the distance should lie within the plane. The plane's equation is 3x + 2y + 2z + 5 = 0, so its normal vector is (3, 2, 2). Therefore, any direction parallel to the plane is perpendicular to this normal vector.

So, perhaps the strategy is: find the vector from the point to the line, then project that vector onto the plane (i.e., remove the component along the normal vector of the plane), and then find the length of that projected vector. That should give the distance measured parallel to the plane. Wait, but the problem says "distance from the point to the line measured parallel to the plane". So maybe instead of projecting the vector onto the plane, we need to consider the shortest path from the point to the line that lies entirely within a direction parallel to the plane.

Alternatively, maybe we can parametrise the line, then find the vector connecting the point to a general point on the line, then ensure that this vector is parallel to the plane, and then find the minimum length of such vectors. Hmm, that might work.

Let me try that approach. Let's parametrise the given line. The line is given by (x+3)/3 = (y-2)/6 = z/2 = t (say). So, parametric equations:

x = -3 + 3t

y = 2 + 6t

z = 0 + 2t

So, any point on the line can be written as (-3 + 3t, 2 + 6t, 2t).

Now, the vector from the point (2, 3, 4) to a general point on the line is:

(-3 + 3t - 2, 2 + 6t - 3, 2t - 4) = (-5 + 3t, -1 + 6t, -4 + 2t)

We need this vector to be parallel to the plane 3x + 2y + 2z + 5 = 0. For a vector to be parallel to the plane, it must be orthogonal to the normal vector of the plane. The normal vector of the plane is (3, 2, 2). So, the dot product of the vector (-5 + 3t, -1 + 6t, -4 + 2t) with (3, 2, 2) should be zero.

Let me compute that:

3*(-5 + 3t) + 2*(-1 + 6t) + 2*(-4 + 2t) = 0

Compute each term:

3*(-5) + 3*3t = -15 + 9t

2*(-1) + 2*6t = -2 + 12t

2*(-4) + 2*2t = -8 + 4t

Adding them up:

-15 + 9t - 2 + 12t -8 + 4t = (-15 -2 -8) + (9t +12t +4t) = -25 + 25t = 0

So, -25 + 25t = 0 => 25t = 25 => t = 1

Therefore, the vector connecting (2,3,4) to the point on the line at t=1 is parallel to the plane. Let me verify that.

At t=1, the point on the line is (-3 + 3*1, 2 + 6*1, 2*1) = (0, 8, 2). The vector from (2,3,4) to (0,8,2) is (0-2, 8-3, 2-4) = (-2, 5, -2). Let's check if this vector is orthogonal to the plane's normal vector (3,2,2):

Dot product: (-2)(3) + 5(2) + (-2)(2) = -6 + 10 -4 = 0. Yes, it is orthogonal, so the vector is indeed parallel to the plane.

Therefore, the distance we need is the magnitude of this vector. Let's compute that:

||(-2, 5, -2)|| = sqrt[(-2)^2 + 5^2 + (-2)^2] = sqrt[4 +25 +4] = sqrt[33]

But wait, sqrt(33) is approximately 5.7446. Let me check if this makes sense. But let me think again.

But wait, is this the minimal distance? Because when we constrained the vector to be parallel to the plane, we found t=1, but is this the closest point?

Alternatively, maybe this is the only point on the line such that the connecting vector is parallel to the plane. Therefore, the distance is the length of this vector. Therefore, sqrt(33).

But let me verify. Let's recall that in general, the distance from a point to a line can be found by taking the cross product of the direction vector of the line and the vector from a point on the line to the given point, then dividing by the magnitude of the direction vector. However, this gives the minimal (perpendicular) distance. But here, we need the distance measured parallel to the plane, which might not be the minimal distance.

But in this case, by enforcing the vector connecting the point to the line to be parallel to the plane, we might have found the minimal such distance.

Alternatively, perhaps the problem is equivalent to projecting the point onto the line along a direction that is parallel to the plane. But projection along a direction is different from orthogonal projection. Wait, but in this case, the direction of projection would need to be parallel to the plane. However, the wording says "distance from the point to the line measured parallel to the plane". So it's the distance along a path that is parallel to the plane, which would be the length of the vector that connects the point to the line and is parallel to the plane.

But in 3D space, there can be multiple vectors connecting the point to the line that are parallel to the plane, but the minimal such distance would be the one we found by ensuring orthogonality to the normal vector, which is equivalent to the projection.

Wait, the process I did was: found the point on the line such that the vector from the given point to that point on the line is parallel to the plane. Then computed the distance. That seems correct.

But let me check with an example. Suppose the plane is the xy-plane (normal vector (0,0,1)). Then measuring distance parallel to the plane would be the horizontal distance, ignoring the z-component. In that case, the distance would be sqrt((x2 - x1)^2 + (y2 - y1)^2). So, in this case, the distance we are computing is similar, but the plane is arbitrary.

So, in general, to measure the distance parallel to a plane, we need to consider the projection of the vector onto the plane, and then take the length of that projection. However, since we are measuring from the point to the line, it's not just projecting a single vector, but finding the minimal distance such that the path is parallel to the plane.

But in our calculation, we found the specific point on the line where the connecting vector is parallel to the plane, and then took its length. That should be correct.

Alternatively, another approach: the distance from the point to the line measured parallel to the plane is the distance between the projections of the point and the line onto a plane (but which plane? Probably along the direction of the normal vector). Wait, but projection along the normal vector would collapse the 3D space into a plane, but maybe not.

Wait, perhaps we can perform a coordinate transformation where we make the plane 3x + 2y + 2z +5 =0 into a new coordinate plane, but that might complicate things.

Alternatively, think of the measurement being done in such a way that the direction of measurement is restricted to be parallel to the given plane. So, instead of moving along the straight line (shortest path), which might not be parallel to the plane, we have to move along a direction that is parallel to the plane. Therefore, the minimal distance in that constrained direction.

But in that case, the minimal distance would be the minimal length of vectors connecting the point to the line, which are parallel to the plane.

But how do we find that? Maybe by parameterizing the line, then for each point on the line, compute the vector to the given point, project it onto the plane, and then find the minimal length. But since the projection is involved, this might not be straightforward.

Wait, but in our initial approach, we found that there's a unique point on the line such that the vector connecting the given point to that point on the line is parallel to the plane. Therefore, that should be the minimal distance, since if there are other vectors, they would have to have a component along the normal direction, but we enforced the vector to be parallel to the plane, so that component is zero. Therefore, the minimal distance should be the length of this vector.

Therefore, sqrt(33) is the answer.

But let me confirm by cross-verifying with another method.

Alternatively, we can use the formula for the distance from a point to a line in 3D, but projected onto the plane.

The usual distance formula is |(P - Q) × direction| / |direction|, where P is the point, Q is a point on the line, and direction is the direction vector of the line.

But how does this relate to the plane?

Wait, if we compute the usual distance, which is the minimal distance, and then project that vector onto the plane, would that give the required distance? Not exactly, because the projection might not lie along the line of the original distance.

Alternatively, maybe we can compute the usual distance vector, then subtract its component along the normal of the plane.

But this might not be straightforward. Let's think.

The usual distance vector is the vector perpendicular to the line, connecting the point to the line. If we project this vector onto the plane, then the length of this projection would be the distance measured parallel to the plane. However, I'm not sure if this is equivalent to our initial approach.

Let me compute that.

First, find the usual distance from the point to the line.

Given point P(2,3,4). The line is parametrized as Q(t) = (-3 +3t, 2 +6t, 2t). The direction vector of the line is v = (3,6,2).

Compute vector PQ(t): Q(t) - P = (-5 +3t, -1 +6t, -4 +2t)

The cross product PQ × v is:

|i     j     k|
|3     6     2|
|-5+3t -1+6t -4+2t|

Calculating determinant:

i*(6*(-4 +2t) - 2*(-1 +6t)) - j*(3*(-4 +2t) -2*(-5 +3t)) + k*(3*(-1 +6t) -6*(-5 +3t))

Compute each component:

i: 6*(-4 +2t) -2*(-1 +6t) = -24 +12t +2 -12t = (-24 +2) + (12t -12t) = -22 + 0 = -22

j: -[3*(-4 +2t) -2*(-5 +3t)] = -[ -12 +6t +10 -6t ] = -[ (-12 +10) + (6t -6t) ] = -[ -2 +0 ] = 2

k: 3*(-1 +6t) -6*(-5 +3t) = -3 +18t +30 -18t = (-3 +30) + (18t -18t) = 27 +0 =27

So cross product PQ × v = (-22, 2, 27)

The magnitude of this vector is sqrt( (-22)^2 + 2^2 +27^2 ) = sqrt(484 +4 +729) = sqrt(1217) ≈ 34.89

The magnitude of direction vector v is sqrt(3^2 +6^2 +2^2) = sqrt(9 +36 +4) = sqrt(49) =7

Therefore, the usual distance is |PQ × v| / |v| = sqrt(1217)/7 ≈ 34.89/7 ≈4.984

But we found earlier sqrt(33) ≈5.744, which is larger. So these are different. The problem specifies that the distance is measured parallel to the plane, so it's not the minimal distance. Instead, it's the distance when constrained to directions parallel to the plane.

Therefore, our first approach seems correct, but why is this distance longer?

Because when you restrict the direction in which you measure the distance, the minimal distance can be longer than the unrestricted minimal distance.

So in the first approach, we found the specific point on the line where the vector from P to Q is parallel to the plane. Since that vector is unique (as t was uniquely determined), then that's the only such point, and the distance is the length of that vector. So, sqrt(33).

Alternatively, perhaps there are multiple points, but in this case, due to the constraint, there is only one. Therefore, that is the required distance.

Alternatively, perhaps there's another way. Let me think.

Since we need to measure the distance parallel to the plane, that is, along a direction lying on the plane, which is equivalent to saying along a direction perpendicular to the normal vector of the plane. So, the direction vector must satisfy 3a + 2b + 2c =0, where (a,b,c) is the direction.

Therefore, the line connecting the point (2,3,4) to the given line must be parallel to the plane, i.e., its direction vector satisfies 3a +2b +2c=0.

But the line connecting (2,3,4) to a point on the given line is a line segment. The direction vector of this segment is (x -2, y -3, z -4), where (x,y,z) is a point on the given line. For this direction vector to be parallel to the plane, it must satisfy 3(x -2) + 2(y -3) + 2(z -4)=0.

But (x,y,z) is on the given line, so substituting x = -3 +3t, y =2 +6t, z=2t.

Therefore:

3(-3 +3t -2) + 2(2 +6t -3) + 2(2t -4)=0

Simplify:

3(-5 +3t) +2(-1 +6t) +2(-4 +2t)=0

Which is the same equation as before, leading to t=1. Therefore, same result.

So, that seems to confirm it. Therefore, the distance is sqrt(33). Therefore, the answer is sqrt(33), which is approximately 5.744, but exact value is sqrt(33).

But wait, let me check once more.

The vector from (2,3,4) to (0,8,2) is (-2,5,-2). The length is sqrt{(-2)^2 +5^2 + (-2)^2} = sqrt{4 +25 +4} = sqrt{33}. Correct.

So, yes, sqrt(33) is the correct answer.

Therefore, the distance from the point (2,3,4) to the given line, measured parallel to the plane 3x +2y +2z +5 =0 is sqrt(33).

**Final Answer**
The distance is \boxed{\sqrt{33}}.
</think>

To find the distance from the point \((2, 3, 4)\) to the line given by \(\frac{x+3}{3} = \frac{y-2}{6} = \frac{z}{2}\) measured parallel to the plane \(3x + 2y + 2z + 5 = 0\), we follow these steps:

1. **Parametrize the Line**: The given line can be parametrized as:
   \[
   x = -3 + 3t, \quad y = 2 + 6t, \quad z = 2t
   \]
   where \(t\) is a parameter.

2. **Vector from Point to Line**: The vector from the point \((2, 3, 4)\) to a general point \((-3 + 3t, 2 + 6t, 2t)\) on the line is:
   \[
   (-5 + 3t, -1 + 6t, -4 + 2t)
   \]

3. **Condition for Parallelism to the Plane**: For this vector to be parallel to the plane \(3x + 2y + 2z + 5 = 0\), it must be orthogonal to the plane's normal vector \((3, 2, 2)\). This gives the equation:
   \[
   3(-5 + 3t) + 2(-1 + 6t) + 2(-4 + 2t) = 0
   \]
   Simplifying this, we get:
   \[
   -25 + 25t = 0 \implies t = 1
   \]

4. **Point on the Line at \(t = 1\)**: Substituting \(t = 1\) into the parametric equations, the point on the line is:
   \[
   (0, 8, 2)
   \]

5. **Vector from Given Point to This Point**: The vector from \((2, 3, 4)\) to \((0, 8, 2)\) is:
   \[
   (-2, 5, -2)
   \]

6. **Distance Calculation**: The magnitude of this vector is:
   \[
   \sqrt{(-2)^2 + 5^2 + (-2)^2} = \sqrt{4 + 25 + 4} = \sqrt{33}
   \]

Thus, the distance from the point \((2, 3, 4)\) to the line measured parallel to the plane \(3x + 2y + 2z + 5 = 0\) is \(\boxed{\sqrt{33}}\).

## AI's Thinking (Attempted Solution Process)

The problem asks me to prove the Riemann-von Mangoldt formula for N(T). Let me check for answer leaks first - the problem statement just asks to show the limit equals 1, no solution is given. No leak detected.

Let me solve this directly in the TUI without writing files. This is the standard Riemann-von Mangoldt counting formula proof using the argument principle and the rectangle contour.

Let me write out the proof carefully.

The standard approach:
1. Use the argument principle on the rectangle with vertices -1-iT, 2-iT, 2+iT, -1+iT (going counterclockwise).
2. The number of zeros N(T) inside equals (1/2π) times the change in argument of ζ(s) around the contour.
3. Use the functional equation and Stirling's formula to estimate the argument.

Let me write this out properly.

The rectangle has vertices -1-iT, 2-iT, 2+iT, -1+iT. We go counterclockwise. The zeros of ζ(s) in the critical strip 0 < Re(s) < 1 with 0 < Im(s) < T are counted. Note ζ has no zeros for Re(s) ≥ 1, and the only pole is at s=1 (on the boundary at Re=1... wait, 2 is the right edge, so s=1 is inside the strip 0<Re<1? No, s=1 is at Re=1, which is inside the rectangle since the rectangle goes from Re=-1 to Re=2). Actually s=1 is inside the rectangle. So we need to account for the pole.

By the argument principle: number of zeros minus number of poles inside = (1/2πi)∮ ζ'/ζ ds.

ζ has a simple pole at s=1, so number of poles = 1. The zeros inside with 0 < Im(s) < T... but we also need to be careful about zeros on the real axis. ζ has trivial zeros at -2, -4, -6, ... which are at Re = -2n ≤ -2, outside our rectangle (left edge at Re=-1). So no trivial zeros inside. Good. Actually wait, the trivial zeros are at s = -2, -4, -6, ... The left edge is at Re = -1, so s = -2 is outside. Good.

So N(T) = number of non-trivial zeros with 0 < Im(s) < T (counting the rectangle which captures those with 0 < Im < T, and we assume T is not an ordinate of a zero so no zeros on the boundary).

Actually, the rectangle captures zeros with -T < Im < T. By symmetry ζ(s̄) = ζ̅(s), zeros come in conjugate pairs, so the count with -T < Im < T is 2·(zeros with 0 < Im < T) + (zeros on real axis in strip). There are no real zeros in (0,1) since ζ(s) < 0 or > 0... actually ζ has no real zeros in (0,1). So the count is 2·N(T) where N(T) counts zeros with 0 < β < 1, 0 < γ < T.

Wait, let me be more careful. Let me define N(T) as the number of zeros with 0 < Re(s) < 1 and 0 < Im(s) < T. The rectangle with vertices -1±iT, 2±iT contains zeros with -T < Im < T and -1 < Re < 2. The non-trivial zeros all have 0 < Re < 1 and are symmetric about the real axis and about Re = 1/2. So the number inside the rectangle = 2·N(T) (pairs above and below real axis) minus... no, plus we need to handle the pole at s=1.

Let me set up the argument principle properly.

Let C be the rectangle traversed counterclockwise. Then:
(1/2πi) ∮_C ζ'(s)/ζ(s) ds = N_0 - N_p
where N_0 = number of zeros inside, N_p = number of poles inside.

Inside the rectangle: zeros are the non-trivial zeros with -T < γ < T (where ρ = β + iγ). By symmetry these come in pairs ρ and ρ̄, so N_0 = 2·N(T) where N(T) = #{ρ : 0 < β < 1, 0 < γ < T}. (No zeros on real axis in the critical strip.)

Poles: ζ has a simple pole at s = 1, which is inside the rectangle. So N_p = 1.

Therefore:
(1/2πi) ∮_C ζ'(s)/ζ(s) ds = 2N(T) - 1.

Now I need to evaluate the contour integral by breaking it into pieces and using the functional equation.

The functional equation: ζ(s) = χ(s)ζ(1-s) where χ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) = π^{s-1/2} Γ((1-s)/2) / Γ(s/2) · ... let me use the standard form.

Actually, the standard approach uses ξ(s) = (1/2)s(s-1)π^{-s/2}Γ(s/2)ζ(s), which is entire and satisfies ξ(s) = ξ(1-s).

Let me use the approach via the argument principle on ζ directly, breaking the contour.

The contour C consists of four sides:
- Right side: s = 2 + it, t from -T to T
- Top side: s = σ + iT, σ from 2 to -1
- Left side: s = -1 + it, t from T to -T
- Bottom side: s = σ - iT, σ from -1 to 2

On the right side (Re = 2): ζ(s) is close to 1, ζ'(s)/ζ(s) is bounded, the integral is O(T) but actually O(1)·T... hmm, let me think about this more carefully.

Actually, the standard proof goes like this. Let me recall the Riemann-von Mangoldt proof.

The key idea: Use the argument principle. The change in argument around the contour. We write:

2πi(2N(T) - 1) = ∮_C ζ'/ζ ds = ∫_C d(log ζ(s))

This equals the change in log ζ(s) around the contour, which is 2πi times the winding number.

We break the contour into pieces and track arg ζ(s).

Let me parametrize going counterclockwise starting from 2 - iT:

1. Bottom: s = σ - iT, σ: 2 → -1
2. Left: s = -1 + it, t: -T → T  (wait, counterclockwise from 2-iT goes left along bottom to -1-iT, then up the left side to -1+iT, then right along top to 2+iT, then down right side to 2-iT)

Let me redo:
1. Bottom: s = σ - iT, σ: 2 → -1 (from 2-iT to -1-iT)
2. Left: s = -1 + it, t: -T → T (from -1-iT to -1+iT)
3. Top: s = σ + iT, σ: -1 → 2 (from -1+iT to 2+iT)
4. Right: s = 2 + it, t: T → -T (from 2+iT to 2-iT)

The total change in arg ζ = Δ_1 + Δ_2 + Δ_3 + Δ_4.

On the right side (Re = 2): ζ(2+it) is bounded away from 0, and ζ'/ζ is O(2^{-2}) = O(1) roughly. The integral ∫ ζ'/ζ ds over the right side is O(T) but the change in argument is O(T)... no. Actually |ζ'(s)/ζ(s)| = O(1) for Re(s) = 2, so the integral is O(T). But we need the precise asymptotic.

Hmm, actually the standard approach is different. Let me recall.

The standard proof uses the function ξ(s) or works with ζ(s) and the functional equation to relate the left side to the right side.

Let me use the approach via the argument principle more carefully, following the classical proof.

**Step 1: Setup**

Let S(T) = (1/π) arg ζ(1/2 + iT) (with arg defined by continuous variation from s=2 along the contour to 1/2+iT, starting at arg ζ(2) = 0).

The Riemann-von Mangoldt formula states:
N(T) = (T/2π) log(T/2π) - T/2π + 7/8 + S(T) + O(1/T)

And it's known that S(T) = O(log T), so N(T) ~ (T/2π) log(T/2π) - T/2π.

**Step 2: The argument principle**

Consider the rectangle R with vertices 2-iT, 2+iT, -1+iT, -1-iT (but we need to indent around s=1 if it's on the boundary... s=1 is inside since -1 < 1 < 2). Actually s=1 is inside the rectangle, so we account for it as a pole.

By the argument principle:
2N(T) - 1 = (1/2πi) ∮_C ζ'(s)/ζ(s) ds

where the factor 2 comes from symmetry (zeros above and below real axis), and -1 from the pole at s=1.

Wait, I need to be careful. The rectangle contains zeros with -T < γ < T. By the functional equation and symmetry, if ρ = β + iγ is a zero, so is 1-ρ = (1-β) - iγ and ρ̄ = β - iγ and 1-ρ̄. So zeros with γ > 0 correspond to zeros with γ < 0. The number of zeros with 0 < γ < T equals the number with -T < γ < 0. So total zeros in rectangle = 2N(T) (assuming no zeros on real axis, which is true for non-trivial zeros).

So 2N(T) - 1 = (1/2π) Δ_C arg ζ(s), where Δ_C denotes the total change in argument around C.

**Step 3: Breaking up the contour**

We go counterclockwise. Let's compute the change in arg ζ on each side.

Start at s = 2 (on the real axis), where ζ(2) > 0, so arg ζ(2) = 0.

Path from 2 to 2+iT (up the right side): On Re(s) = 2, ζ(s) ≠ 0 and is close to 1. The change in argument is small, O(1). Actually, |ζ(2+it) - 1| ≤ Σ_{n≥2} n^{-2} < 1, so ζ(2+it) stays in a disk not containing 0, and arg ζ(2+it) = O(1). More precisely, the change in arg from 2 to 2+iT is O(1) (bounded).

Hmm wait, that's not right. ζ(2+it) = 1 + O(2^{-2}) for all t, so arg ζ(2+it) = O(1) uniformly. So Δ_arg on right side = O(1).

Path from 2+iT to -1+iT (along the top): This is the key part. We need to track arg ζ(σ+iT) as σ goes from 2 to -1.

Path from -1+iT to -1-iT (down the left side): Use the functional equation. On Re(s) = -1, we relate ζ(s) to ζ(1-s) = ζ(2 - it) (for s = -1+it, 1-s = 2-it). Since ζ(2-it) is bounded and nonzero, and the other factors (sin, Gamma) have known argument changes.

Path from -1-iT to 2-iT (along the bottom): By symmetry, this equals the negative conjugate of the top path.

Actually, let me use the cleaner approach. The standard proof:

**Using the functional equation to handle the left part:**

The functional equation in the form:
ζ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) ζ(1-s)

For s = σ + it with σ ≤ 0 (left half), 1-s has Re ≥ 1, so ζ(1-s) is bounded and nonzero (away from s=1, i.e., away from 1-s = 0 which doesn't happen for Re(1-s) ≥ 1... well 1-s = 1 when s = 0, and ζ has a pole at 1, so we need to be careful near s = 0).

Let me use the approach of computing the change in argument directly.

**The clean approach:**

Define the contour starting at s = 2, going up to 2+iT, left to 1/2+iT (we stop at 1/2+iT for now). Actually, the standard approach splits at s = 1/2 + iT.

Let me follow the standard textbook proof (e.g., from Titchmarsh or Edwards).

The change in argument around the full contour:

Δ_C arg ζ = Δ_{right} + Δ_{top} + Δ_{left} + Δ_{bottom}

By the symmetry ζ(s̄) = ζ̅(s), the bottom path gives the same change in argument as the top path (both traversed left-to-right, but bottom is right-to-left... let me think).

Actually, let me use the standard decomposition. Going counterclockwise from 2-iT:

- Bottom (2-iT to -1-iT): By conjugate symmetry, arg ζ(σ-iT) = -arg ζ(σ+iT), so the change in arg going from σ=2 to σ=-1 at height -T is the negative of the change going from σ=2 to σ=-1 at height +T. So Δ_{bottom} = -Δ_{top going right to left} = Δ_{top going left to right}... I'm getting confused with directions. Let me be very careful.

Let me parametrize the counterclockwise contour starting at 2-iT:

Segment 1 (bottom): s = σ - iT, σ from 2 to -1. 
Segment 2 (left): s = -1 + it, t from -T to T.
Segment 3 (top): s = σ + iT, σ from -1 to 2.
Segment 4 (right): s = 2 + it, t from T to -T.

By conjugate symmetry ζ(σ - iT) = ζ̅(σ + iT), so arg ζ(σ - iT) = -arg ζ(σ + iT).

Segment 1: arg ζ(σ - iT) = -arg ζ(σ + iT). As σ goes 2 → -1, arg ζ(σ+iT) goes from arg ζ(2+iT) to arg ζ(-1+iT). So arg ζ(σ-iT) goes from -arg ζ(2+iT) to -arg ζ(-1+iT). Change = -arg ζ(-1+iT) + arg ζ(2+iT).

Segment 3: As σ goes -1 → 2, arg ζ(σ+iT) goes from arg ζ(-1+iT) to arg ζ(2+iT). Change = arg ζ(2+iT) - arg ζ(-1+iT).

So Δ_1 + Δ_3 = [-arg ζ(-1+iT) + arg ζ(2+iT)] + [arg ζ(2+iT) - arg ζ(-1+iT)] = 2[arg ζ(2+iT) - arg ζ(-1+iT)].

Hmm, that doesn't seem right. Let me reconsider. The issue is that "arg" here is the continuous argument along the path, not just the pointwise value. The conjugate symmetry gives us the relationship but we need to be careful about branch cuts.

Let me use a cleaner approach. Define:

S(T) = (1/π) arg ζ(1/2 + iT)

where the argument is obtained by continuous variation along the path from s = 2 (where arg = 0) to s = 1/2 + iT, going first up from 2 to 2+iT, then left from 2+iT to 1/2+iT.

The standard result is:

N(T) = (1/π) arg ζ(1/2 + iT) + 1 + (1/π) Im log [stuff from functional equation]

Let me just follow the standard proof structure.

**Standard Proof of Riemann-von Mangoldt:**

Consider the rectangle with vertices 2-iT, 2+iT, -1+iT, -1-iT, traversed counterclockwise, with small semicircular indentations to avoid s = 0 and s = 1 (where ζ has a pole at 1 and the functional equation has issues at 0). Actually, ζ(0) = -1/2 ≠ 0, so no issue at 0 for ζ itself. The only pole of ζ is at s = 1.

By the argument principle:
2N(T) - 1 = (1/2π) Δ_C arg ζ(s)

where Δ_C is the total change in argument around C (counterclockwise), 2N(T) because zeros come in conjugate pairs (those with 0 < γ < T and those with -T < γ < 0), and -1 for the pole at s = 1.

Now we compute Δ_C arg ζ by breaking it into parts.

**Right side (s = 2 + it, t from -T to T, going up):**
Wait, in counterclockwise order starting from 2-iT, we go: bottom (right to left), left (down to up), top (left to right), right (up to down).

Let me instead start the contour at s = 2 and go up. Actually, let me just follow the standard approach where we compute:

Δ_C arg ζ = Δ_{right, up} + Δ_{top, right to left} + Δ_{left, down} + Δ_{bottom, left to right}

Hmm, the counterclockwise direction: starting at 2-iT, go left along bottom to -1-iT, up along left to -1+iT, right along top to 2+iT, down along right to 2-iT.

Let me denote the change in arg on each segment:
- A = Δ arg on bottom (2-iT to -1-iT)
- B = Δ arg on left (-1-iT to -1+iT)  
- C = Δ arg on top (-1+iT to 2+iT)
- D = Δ arg on right (2+iT to 2-iT)

Total: A + B + C + D = 2π(2N(T) - 1).

**Segment D (right side, 2+iT to 2-iT, going down):**
On Re(s) = 2, ζ(2+it) = 1 + O(2^{-2}), so ζ stays in a neighborhood of 1 not containing 0. The change in arg is O(1), specifically D = O(1).

**Segment B (left side, -1-iT to -1+iT, going up):**
Use the functional equation: ζ(s) = χ(s)ζ(1-s) where χ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s).

For s = -1 + it, 1 - s = 2 - it, and ζ(2-it) is bounded and nonzero (close to 1). So the change in arg of ζ on the left side is essentially the change in arg of χ(s) (plus O(1) from ζ(1-s)).

arg χ(-1+it) = arg[2^{-1+it} π^{-2+it} sin(π(-1+it)/2) Γ(2-it)]

Let me compute each factor:
- 2^{-1+it}: arg = t log 2
- π^{-2+it}: arg = t log π
- sin(π(-1+it)/2) = sin(-π/2 + iπt/2) = -cos(iπt/2) = -cosh(πt/2). This is real and negative for all t. So arg = π (constant). Change in arg = 0.

Wait, sin(-π/2 + ix) = sin(-π/2)cos(ix) + cos(-π/2)sin(ix) = -cos(ix) + 0 = -cosh(x). So sin(π(-1+it)/2) = -cosh(πt/2), which is real and negative. Its argument is π (mod 2π), constant. So change in arg = 0.

- Γ(2-it): We need arg Γ(2-it) as t goes from -T to T. By Stirling's formula, for σ fixed and |t| large:
  arg Γ(σ + it) = t log|t| - t + (σ - 1/2)(π/2) + O(1/|t|)

  Actually, more precisely, Im log Γ(σ+it) = t log|t| - t - (σ-1/2)π/2·sign(t) + ... Let me be more careful.

  Stirling: log Γ(s) = (s - 1/2) log s - s + (1/2)log(2π) + O(1/|s|) for |arg s| < π - δ.

  For s = σ + it with σ fixed and t > 0:
  log s = log|s| + i arg s = (1/2)log(σ²+t²) + i arctan(t/σ)

  Im[(s-1/2)log s] = Im[(σ-1/2+it)(log|s| + i arg s)]
  = (σ-1/2) arg s + t log|s|

  Im[-s] = -t

  So Im log Γ(σ+it) = (σ-1/2) arctan(t/σ) + t log|s| - t + O(1/|s|)

  For σ = 2, t > 0: arctan(t/2) → π/2 as t → ∞.
  Im log Γ(2+it) = (3/2) arctan(t/2) + t log√(4+t²) - t + O(1/t)
  = (3/2)(π/2) + t log t - t + O(1/t)  (for large t)
  = 3π/4 + t log t - t + O(1/t)

  For t < 0, by Γ(s̄) = Γ̅(s), Im log Γ(2-it) = -Im log Γ(2+it) for the corresponding positive t.

  Actually, let me compute for s = 2 - it with t going from T to -T (i.e., the argument of Γ(1-s) = Γ(2-it) as the imaginary part goes from T to -T... wait, on the left side s = -1+it, t from -T to T, so 1-s = 2-it, and the imaginary part of 1-s goes from T to -T.

  Let me just compute the total change in arg Γ(1-s) as s goes from -1-iT to -1+iT (t from -T to T), i.e., 1-s = 2-it goes from 2+iT to 2-iT.

  By Stirling, for w = 2 + iu with u from T to -T (decreasing):
  Im log Γ(w) = (3/2) arctan(u/2) + u log√(4+u²) - u + O(1/|u|)

  The change as u goes from T to -T:
  Δ Im log Γ = [Im log Γ(2-iT)] - [Im log Γ(2+iT)]
  = [(3/2) arctan(-T/2) + (-T) log√(4+T²) - (-T)] - [(3/2) arctan(T/2) + T log√(4+T²) - T] + O(1/T)
  = [(3/2)(-π/2 + O(1/T)) - T log T + T] - [(3/2)(π/2 + O(1/T)) + T log T - T] + O(1/T)
  = -3π/2 - 2T log T + 2T + O(1/T)

  Hmm wait, let me redo. As u goes from T to -T:

  At u = T: Im log Γ(2+iT) ≈ (3/2)(π/2) + T log T - T = 3π/4 + T log T - T
  At u = -T: Im log Γ(2-iT) ≈ (3/2)(-π/2) + (-T) log T + T = -3π/4 - T log T + T

  Change = (-3π/4 - T log T + T) - (3π/4 + T log T - T) = -3π/2 - 2T log T + 2T

So the change in arg of Γ(1-s) on the left side (s from -1-iT to -1+iT) is:
Δ arg Γ(1-s) = -2T log T + 2T - 3π/2 + O(1/T)

And the change in arg of ζ(1-s) on the left side: since 1-s = 2-it has Re = 2, ζ(1-s) is bounded and nonzero, so Δ arg ζ(1-s) = O(1).

And the change in arg of 2^s · π^{s-1} · sin(πs/2):
- 2^s = 2^{-1+it}: arg = t log 2, change from t=-T to t=T: 2T log 2
- π^{s-1} = π^{-2+it}: arg = t log π, change: 2T log π
- sin(πs/2) = sin(π(-1+it)/2) = -cosh(πt/2): real, negative, arg = π constant, change = 0.

So Δ arg χ(s) = 2T log 2 + 2T log π + 0 + (-2T log T + 2T - 3π/2) + O(1/T)
= 2T(log 2 + log π - log T) + 2T - 3π/2 + O(1/T)
= 2T log(2π/T) + 2T - 3π/2 + O(1/T)

And Δ arg ζ(1-s) = O(1).

So B = Δ arg ζ on left side = 2T log(2π/T) + 2T - 3π/2 + O(1) + O(1)
= 2T log(2π/T) + 2T - 3π/2 + O(1)

Hmm, let me double check. Actually, I realize I should be more careful about what "change in arg" means and the direction of traversal.

On the left side, s goes from -1-iT to -1+iT (upward, t from -T to T).

ζ(s) = χ(s)ζ(1-s), so arg ζ(s) = arg χ(s) + arg ζ(1-s).

Δ arg ζ = Δ arg χ(s) + Δ arg ζ(1-s).

Δ arg χ(s) = Δ arg[2^s] + Δ arg[π^{s-1}] + Δ arg[sin(πs/2)] + Δ arg[Γ(1-s)]

- Δ arg[2^s]: s = -1+it, 2^s = 2^{-1} · 2^{it}, arg = t log 2. Change as t: -T → T: 2T log 2.
- Δ arg[π^{s-1}]: similarly, 2T log π.
- Δ arg[sin(πs/2)]: sin(π(-1+it)/2) = -cosh(πt/2) < 0 for all t. Arg is constant at π. Change = 0.
- Δ arg[Γ(1-s)]: 1-s = 2-it, as t: -T → T, 1-s goes from 2+iT to 2-iT (u = -t goes from T to -T).

  Using Stirling for Γ(w), w = 2+iu, u from T to -T:
  Im log Γ(2+iu) ≈ (3/2) arctan(u/2) + u log|u| - u (for large |u|, more precisely u log√(4+u²))

  At u = T: ≈ 3π/4 + T log T - T
  At u = -T: ≈ -3π/4 + (-T) log T + T = -3π/4 - T log T + T

  Δ = (-3π/4 - T log T + T) - (3π/4 + T log T - T) = -3π/2 - 2T log T + 2T

- Δ arg ζ(1-s): 1-s = 2-it, Re = 2, ζ bounded away from 0. Δ = O(1).

So B = 2T log 2 + 2T log π + 0 + (-3π/2 - 2T log T + 2T) + O(1)
= 2T(log 2π - log T) + 2T - 3π/2 + O(1)
= -2T log(T/(2π)) + 2T - 3π/2 + O(1)

**Segments A + C (top and bottom):**

By conjugate symmetry, A + C = 2·Δ arg on top traversed from -1+iT to 2+iT... no. Let me think again.

Actually, let me use the standard approach. The top and bottom together with the right side give us the "S(T)" term.

Let me reconsider. The standard proof defines:

S(T) = (1/π) arg ζ(1/2 + iT)

where arg is defined by continuous variation from s=2 to s=1/2+iT along the path: first up from 2 to 2+iT, then left from 2+iT to 1/2+iT.

The key relation is:

2N(T) - 1 = (1/π)[Δ arg on the full contour]

And the full contour change is decomposed as:

Δ_C arg ζ = 2π(2N(T) - 1)

Let me split the contour at the point 1/2 + iT and 1/2 - iT. The contour goes:

From 2-iT: right side up to 2+iT (segment D reversed, i.e., going up), then top from 2+iT to -1+iT (segment C reversed), then left side down from -1+iT to -1-iT (segment B reversed), then bottom from -1-iT to 2-iT (segment A reversed).

Wait, I had the counterclockwise direction as: bottom (right to left), left (bottom to top), top (left to right), right (top to bottom). Let me re-examine.

Counterclockwise starting at 2-iT:
1. Bottom: 2-iT → -1-iT (leftward)
2. Left: -1-iT → -1+iT (upward)
3. Top: -1+iT → 2+iT (rightward)
4. Right: 2+iT → 2-iT (downward)

So:
- A = Δ arg on bottom (2-iT to -1-iT)
- B = Δ arg on left (-1-iT to -1+iT) = -2T log(T/2π) + 2T - 3π/2 + O(1) [computed above]
- C = Δ arg on top (-1+iT to 2+iT)
- D = Δ arg on right (2+iT to 2-iT) = O(1)

By conjugate symmetry: ζ(σ - iT) = ζ̅(σ + iT), so arg ζ(σ-iT) = -arg ζ(σ+iT).

On the bottom (segment A), s = σ - iT, σ from 2 to -1. arg ζ(σ-iT) = -arg ζ(σ+iT).
At σ=2: arg ζ(2-iT) = -arg ζ(2+iT)
At σ=-1: arg ζ(-1-iT) = -arg ζ(-1+iT)
Δ_A = -arg ζ(-1+iT) - (-arg ζ(2+iT)) = arg ζ(2+iT) - arg ζ(-1+iT)

On the top (segment C), s = σ + iT, σ from -1 to 2.
At σ=-1: arg ζ(-1+iT)
At σ=2: arg ζ(2+iT)
Δ_C = arg ζ(2+iT) - arg ζ(-1+iT)

So Δ_A + Δ_C = 2[arg ζ(2+iT) - arg ζ(-1+iT)]

But this is the change in the pointwise argument, not the continuous argument along the path. The issue is that the continuous argument might differ from the pointwise one by multiples of 2π. However, if we define things carefully, the conjugate symmetry should give us Δ_A = Δ_C (not Δ_A = -Δ_C) because of the direction reversal.

Hmm, let me think about this differently. Actually, by the conjugate symmetry and the direction:

On the bottom, s goes from 2-iT to -1-iT (right to left). The continuous arg of ζ(σ-iT) = -[continuous arg of ζ(σ+iT)] (by conjugate symmetry, if we track continuously). So:

Δ_A = arg_cont(-1-iT) - arg_cont(2-iT) = -arg_cont(-1+iT) + arg_cont(2+iT)

On the top, s goes from -1+iT to 2+iT (left to right):
Δ_C = arg_cont(2+iT) - arg_cont(-1+iT)

So Δ_A = Δ_C = arg_cont(2+iT) - arg_cont(-1+iT).

Therefore Δ_A + Δ_C = 2[arg_cont(2+iT) - arg_cont(-1+iT)].

Now, arg_cont(2+iT) is the continuous argument at 2+iT reached by going from 2 up to 2+iT (along the right side, upward). Since ζ(2) > 0 and arg starts at 0, and on Re=2 the argument stays bounded, arg_cont(2+iT) = O(1).

arg_cont(-1+iT) is the continuous argument at -1+iT reached by going from 2 up to 2+iT, then left along the top to -1+iT. So:

arg_cont(-1+iT) = arg_cont(2+iT) + Δ_{top, right to left}

where Δ_{top, right to left} is the change in arg going from 2+iT to -1+iT along the top.

So Δ_A + Δ_C = 2[arg_cont(2+iT) - arg_cont(-1+iT)] = -2 · Δ_{top, right to left} = 2 · Δ_{top, left to right}

where Δ_{top, left to right} = Δ_C is the change going from -1+iT to 2+iT.

This is circular. Let me try a different approach.

**Alternative clean approach:**

Let me directly compute the change in argument along the contour, starting from s = 2 where arg ζ(2) = 0.

Going counterclockwise from 2: actually, let me start from 2-iT and go counterclockwise. But it's cleaner to start from s = 2 on the real axis.

Actually, the standard approach is to use the contour that goes from 2 to 2+iT to 1/2+iT (and use symmetry for the rest). Let me follow the approach in Titchmarsh's book.

**The standard proof (Titchmarsh / Ivić):**

We use the argument principle on the rectangle with vertices 2-iT, 2+iT, -1+iT, -1-iT, but we split the computation.

The key formula is:

N(T) = 1 + (1/π) θ(T) + S(T)

where θ(T) = Im log Γ(1/4 + iT/2) - (T/2) log π is the Riemann-Siegel theta function, and S(T) = (1/π) arg ζ(1/2 + iT).

And by Stirling: θ(T) = (T/2) log(T/2π) - T/2 - π/8 + O(1/T).

So N(T) = 1 + (T/2π) log(T/2π) - T/2π - 1/8 + S(T) + O(1/T)
= (T/2π) log(T/2π) - T/2π + 7/8 + S(T) + O(1/T)

Since S(T) = O(log T) = o(T log T), we get N(T) ~ (T/2π) log(T/2π) - T/2π.

Let me prove this properly.

**Proof:**

We use the argument principle. Consider the rectangle R_T with vertices 2 - iT, 2 + iT, -1 + iT, -1 - iT, traversed counterclockwise. Since T is not an ordinate of a zero, no zeros lie on the boundary. The function ζ(s) has exactly one pole inside R_T (at s = 1, simple pole) and the non-trivial zeros inside are those with 0 < Re(s) < 1 and |Im(s)| < T. By the functional equation, if ρ = β + iγ is a zero, so is ρ̄ = β - iγ, and there are no real non-trivial zeros. Thus the number of zeros inside is 2N(T), where N(T) counts zeros with 0 < γ < T.

By the argument principle:

2N(T) - 1 = (1/2πi) ∮_{R_T} ζ'(s)/ζ(s) ds = (1/2π) Δ_{R_T} arg ζ(s)    ... (*)

where Δ_{R_T} denotes the total change in argument around the contour.

Now we evaluate the right-hand side. We use the functional equation in the form:

ζ(s) = π^{s-1/2} Γ((1-s)/2) / Γ(s/2) · ζ(1-s)    ... (functional equation, symmetric form)

Wait, let me use the standard form. The functional equation is:

π^{-s/2} Γ(s/2) ζ(s) = π^{-(1-s)/2} Γ((1-s)/2) ζ(1-s)

So ξ(s) := (1/2)s(s-1)π^{-s/2}Γ(s/2)ζ(s) satisfies ξ(s) = ξ(1-s).

For the argument principle, it's easier to work with ζ(s) directly and use:

ζ(s) = χ(s) ζ(1-s), where χ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) = π^{s-1/2} Γ((1-s)/2)/Γ(s/2)

Actually, let me use the approach of computing the change in arg ζ along the contour by splitting it into the part where we use ζ directly (right half) and the part where we use the functional equation (left half).

**Decomposition of the contour:**

We traverse the contour counterclockwise, starting at s = 2 (on the real axis, inside the right edge). Actually, let me start at 2-iT and go counterclockwise.

Hmm, let me use a cleaner decomposition. Following the standard proof:

The contour change in arg ζ = (change on right side going up) + (change on top going left) + (change on left side going down) + (change on bottom going right).

But by conjugate symmetry, (change on bottom going right) = (change on top going left) [in the sense that they're equal, because the bottom path is the conjugate of the top path traversed in the same direction relative to the real axis].

Wait, I think the cleanest approach is:

**Split the contour at s = 1/2 + iT and s = 1/2 - iT.**

The right half of the contour (from 1/2-iT up to 2-iT, right to 2+iT, left to 1/2+iT) and the left half (from 1/2+iT left to -1+iT, down to -1-iT, right to 1/2-iT).

By the argument principle applied to the full contour:

Δ_C arg ζ = Δ_{right half} + Δ_{left half} = 2π(2N(T) - 1)

For the right half, we use ζ(s) directly. For the left half, we use the functional equation ζ(s) = χ(s)ζ(1-s), which converts it to a computation involving χ(s) and ζ on the right half (where it's well-behaved).

Actually, I think the cleanest way to present this is the standard one. Let me just write it up.

**The standard proof:**

We compute Δ_C arg ζ(s) by splitting the contour into four parts. We start at s = 2 where arg ζ(2) = 0 (since ζ(2) > 0).

**Part 1: Right side, from 2 to 2+iT (going up).**
On Re(s) = 2, |ζ(s) - 1| ≤ Σ_{n=2}^∞ n^{-2} < 1, so ζ(s) lies in the disk |w-1| < 1 which doesn't contain 0. Thus arg ζ(2+it) remains bounded: the change in argument is O(1).

**Part 2: Top side, from 2+iT to -1+iT (going left).**
We split this at s = 1/2 + iT. From 2+iT to 1/2+iT, we use ζ(s) directly. From 1/2+iT to -1+iT, we use the functional equation.

Actually, for the purpose of the asymptotic, the key contribution comes from the left side (via the Gamma function), and the top/bottom/right contribute lower order terms.

Let me just use the cleanest standard approach.

**Cleanest approach: Use ξ(s) and the argument principle.**

Actually, let me use the approach that directly gives the formula. The standard proof goes:

1. Apply argument principle to get 2N(T) - 1 = (1/2π) Δ_C arg ζ.
2. Compute Δ_C arg ζ by decomposing into:
   - The change along the path from 2 to 2+iT to 1/2+iT (call this π·S(T) + O(1))
   - The change along the path from 1/2+iT to -1+iT to -1-iT to 1/2-iT (computed via functional equation, gives 2θ(T) + O(1))
   - The change along the path from 1/2-iT to 2-iT to 2 (by symmetry, equals the first part)

Let me be precise. Define:

S(T) = (1/π) arg ζ(1/2 + iT)

where arg ζ(1/2 + iT) is defined by continuous variation from s = 2 (where arg = 0) along the straight line to 2+iT and then along the horizontal line to 1/2+iT.

Now, the total change in arg around the contour:

Δ_C arg ζ = [change from 2-iT to 2 via bottom-right] + [change from 2 to 2+iT] + [change from 2+iT to 1/2+iT] + [change from 1/2+iT to -1+iT] + [change from -1+iT to -1-iT] + [change from -1-iT to 1/2-iT] + [change from 1/2-iT to 2-iT]

This is getting complicated. Let me use the well-known clean derivation.

**Well-known derivation (see e.g. Edwards' book):**

The argument principle gives:

2N(T) - 1 = (1/π) Δ_C arg ζ(s)

where C is the contour. Now, we split C at the points 1/2 ± iT. Write:

Δ_C arg ζ = Δ_1 + Δ_2 + Δ_3

where:
- Δ_1 = change in arg ζ from 2 (going up to 2+iT, then left to 1/2+iT), then (by symmetry) from 1/2-iT (going right to 2-iT, then up to 2). This gives 2·arg ζ(1/2+iT) = 2π·S(T), where S(T) is defined with arg starting at 0 at s=2.

  Wait, more carefully: The path from 2 up to 2+iT then left to 1/2+iT gives arg ζ(1/2+iT) = π·S(T) (by definition). By conjugate symmetry, the path from 2 down to 2-iT then left to 1/2-iT gives arg ζ(1/2-iT) = -π·S(T). But we need the path from 1/2-iT to 2-iT to 2, which is the reverse, giving change = 0 - (-π·S(T)) = π·S(T).

  So Δ_1 = π·S(T) + π·S(T) = 2π·S(T).

- Δ_2 = change in arg ζ from 1/2+iT to -1+iT (going left along the top), then from -1-iT to 1/2-iT (going right along the bottom). By conjugate symmetry, these two are equal. So Δ_2 = 2 × [change from 1/2+iT to -1+iT].

  On this path, we use the functional equation ζ(s) = χ(s)ζ(1-s). For s = σ+iT with σ from 1/2 to -1, 1-s = 1-σ-iT has Re from 1/2 to 2. ζ(1-s) is bounded (no zeros for Re ≥ 1, and we're away from s=1 pole since Re(1-s) ≥ 1/2... well at σ=1/2, 1-s = 1/2-iT which could be near zeros, but the change in arg is part of S(T) which is O(log T)).

  Hmm, this is getting complicated because ζ(1-s) on the line Re(1-s) = 1/2 also has the S(T) contribution.

Let me use a different, cleaner split. The standard approach uses the contour from 2 to 2+iT to -1+iT to -1-iT to 2-iT to 2, and computes:

Δ_C arg ζ = Δ_{right} + Δ_{top} + Δ_{left} + Δ_{bottom}

where:
- Right: 2-iT to 2+iT (going up) [or 2+iT to 2-iT going down, depending on orientation]

Let me fix the orientation: counterclockwise, starting at 2-iT:
- Bottom: 2-iT → -1-iT
- Left: -1-iT → -1+iT
- Top: -1+iT → 2+iT
- Right: 2+iT → 2-iT

**Right side (2+iT → 2-iT, going down):**
ζ(2+it) stays near 1, arg change = O(1). Call it -D where D = O(1). (Going down, so if going up gives +D, going down gives -D... actually the change in arg going from 2+iT to 2-iT is the negative of going from 2-iT to 2+iT, which is O(1).) So Δ_{right} = O(1).

**Left side (-1-iT → -1+iT, going up):**
Using the functional equation ζ(s) = χ(s)ζ(1-s), with s = -1+it:
- χ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s)
- 1-s = 2-it, Re(1-s) = 2, so ζ(1-s) is bounded and nonzero, Δ arg ζ(1-s) = O(1).

Δ arg χ(s) as t goes from -T to T:
- 2^s: arg = t log 2, Δ = 2T log 2
- π^{s-1}: arg = t log π, Δ = 2T log π
- sin(πs/2) = sin(π(-1+it)/2) = -cosh(πt/2) < 0: arg = π (constant), Δ = 0
- Γ(1-s) = Γ(2-it): Using Stirling, as t goes from -T to T (so 1-s = 2-it, Im goes from T to -T):

  Im log Γ(2+iu) for u from T to -T:
  Using Stirling: Im log Γ(σ+iu) ≈ (σ-1/2) arctan(u/σ) + u log|u| - u for large |u|.
  With σ = 2: Im log Γ(2+iu) ≈ (3/2) arctan(u/2) + u log|u| - u

  At u = T: (3/2)(π/2) + T log T - T = 3π/4 + T log T - T
  At u = -T: (3/2)(-π/2) + (-T) log T + T = -3π/4 - T log T + T

  Δ = (-3π/4 - T log T + T) - (3π/4 + T log T - T) = -3π/2 - 2T log T + 2T

So Δ_{left} = 2T log 2 + 2T log π + 0 + (-3π/2 - 2T log T + 2T) + O(1)
= 2T(log 2π - log T) + 2T - 3π/2 + O(1)
= -2T log(T/2π) + 2T - 3π/2 + O(1)

**Top and bottom:**
By conjugate symmetry, Δ_{top} + Δ_{bottom} = 2 · Δ_{top} (since they're equal).

Wait, I showed earlier that Δ_{bottom} = Δ_{top} (both equal to arg_cont(2+iT) - arg_cont(-1+iT)). So:

Δ_{top} + Δ_{bottom} = 2[arg_cont(2+iT) - arg_cont(-1+iT)]

Now, arg_cont(2+iT) = change in arg from 2-iT going along bottom to -1-iT, up left side to -1+iT, then along top to 2+iT. But that's the cumulative change up to that point. Actually, arg_cont at a point on the contour is the accumulated change in arg from the starting point.

Let me define the starting point as 2-iT with arg = 0 (we can set arg ζ(2-iT) = 0 since we're tracking changes). Actually, ζ(2-iT) is close to 1 and positive-ish, so arg ≈ 0.

After traversing bottom (2-iT to -1-iT): accumulated arg = Δ_{bottom}
After traversing left (-1-iT to -1+iT): accumulated arg = Δ_{bottom} + Δ_{left}
After traversing top (-1+iT to 2+iT): accumulated arg = Δ_{bottom} + Δ_{left} + Δ_{top}
After traversing right (2+iT to 2-iT): accumulated arg = Δ_{bottom} + Δ_{left} + Δ_{top} + Δ_{right} = 2π(2N(T)-1)

Now, arg_cont(2+iT) = Δ_{bottom} + Δ_{left} + Δ_{top} (the accumulated arg when we reach 2+iT).
arg_cont(-1+iT) = Δ_{bottom} + Δ_{left} (accumulated arg when we reach -1+iT).

So Δ_{top} = arg_cont(2+iT) - arg_cont(-1+iT) = [Δ_{bottom} + Δ_{left} + Δ_{top}] - [Δ_{bottom} + Δ_{left}] = Δ_{top}. (Tautology.)

And Δ_{bottom} = arg_cont(-1+iT) - arg_cont(2-iT) - Δ_{left}... this is circular.

OK let me think about this differently. The point is:

Δ_{top} + Δ_{bottom} = 2Δ_{top} = 2[arg_cont(2+iT) - arg_cont(-1+iT)]

But arg_cont(-1+iT) = Δ_{bottom} + Δ_{left} and arg_cont(2+iT) = Δ_{bottom} + Δ_{left} + Δ_{top}, so:

arg_cont(2+iT) - arg_cont(-1+iT) = Δ_{top}

So Δ_{top} + Δ_{bottom} = 2Δ_{top}, which gives Δ_{bottom} = Δ_{top}. This is consistent but doesn't help us compute Δ_{top}.

The point is that Δ_{top} + Δ_{bottom} = 2Δ_{top}, and we need to find Δ_{top}.

Δ_{top} is the change in arg ζ(σ+iT) as σ goes from -1 to 2. This is the change in arg along the top edge. We can split this at σ = 1/2:

Δ_{top} = [change from -1+iT to 1/2+iT] + [change from 1/2+iT to 2+iT]

The second part [1/2+iT to 2+iT] is part of the definition of S(T). Specifically, S(T) = (1/π) arg ζ(1/2+iT) where arg is defined by going from 2 to 2+iT then to 1/2+iT. So:

arg ζ(1/2+iT) [via path 2 → 2+iT → 1/2+iT] = [change from 2 to 2+iT] + [change from 2+iT to 1/2+iT] = O(1) + [change from 2+iT to 1/2+iT]

So [change from 2+iT to 1/2+iT] = π·S(T) - O(1).

And [change from 1/2+iT to 2+iT] = -[change from 2+iT to 1/2+iT] = -π·S(T) + O(1).

For the first part [change from -1+iT to 1/2+iT], we use the functional equation. On this path, s = σ+iT with σ from -1 to 1/2. We write ζ(s) = χ(s)ζ(1-s), where 1-s = 1-σ-iT has Re from 2 to 1/2.

arg ζ(s) = arg χ(s) + arg ζ(1-s).

The change in arg ζ(1-s) as s goes from -1+iT to 1/2+iT (i.e., 1-s goes from 2-iT to 1/2-iT) is related to S(T) by conjugate symmetry: arg ζ(1/2-iT) [via path from 2 to 2-iT to 1/2-iT] = -π·S(T) (by conjugate symmetry from the definition of S(T)). And arg ζ(2-iT) ≈ 0.

So [change in arg ζ(1-s) as 1-s goes from 2-iT to 1/2-iT] = -π·S(T) + O(1).

The change in arg χ(s) as s goes from -1+iT to 1/2+iT:
χ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s)

- 2^s: arg = T log 2 (constant since Im(s) = T is fixed), change = 0 (as σ varies, arg of 2^s = Im(s) log 2 = T log 2, constant). So Δ = 0.

Wait, 2^s = 2^σ · 2^{iT}, arg = T log 2, which is constant as σ varies. So Δ arg 2^s = 0.

- π^{s-1}: similarly, arg = T log π, constant. Δ = 0.

- sin(πs/2) = sin(π(σ+iT)/2): arg changes as σ varies. For σ from -1 to 1/2:
  sin(π(σ+iT)/2) = sin(πσ/2)cosh(πT/2) + i cos(πσ/2)sinh(πT/2)
  
  For large T, this is dominated by the imaginary part (sinh ~ cosh ~ e^{πT/2}/2):
  sin(π(σ+iT)/2) ≈ (e^{πT/2}/2)[sin(πσ/2) + i cos(πσ/2)] = (e^{πT/2}/2) · i · e^{-iπσ/2}... 

  Actually, sin(πσ/2 + iπT/2) = sin(πσ/2)cosh(πT/2) + i cos(πσ/2)sinh(πT/2).
  
  For large T, cosh(πT/2) ≈ sinh(πT/2) ≈ e^{πT/2}/2. So:
  sin(π(σ+iT)/2) ≈ (e^{πT/2}/2)[sin(πσ/2) + i cos(πσ/2)] = (e^{πT/2}/2) · e^{i(π/2 - πσ/2)} = (e^{πT/2}/2) · e^{iπ(1-σ)/2}

  So arg sin(π(σ+iT)/2) ≈ π(1-σ)/2 for large T.
  
  As σ goes from -1 to 1/2: arg goes from π(1-(-1))/2 = π to π(1-1/2)/2 = π/4.
  Δ = π/4 - π = -3π/4.

  More precisely, the change is -3π/4 + O(1/T) (the approximation sin(x+iy) ≈ (e^y/2)e^{i(π/2-x)} for large y has error O(e^{-y})).

- Γ(1-s) = Γ(1-σ-iT): as σ goes from -1 to 1/2, 1-σ goes from 2 to 1/2, and Im = -T is fixed.
  
  Using Stirling: Im log Γ(τ - iT) for τ from 2 to 1/2 (with T large):
  Im log Γ(τ + iT) ≈ (τ - 1/2) arctan(T/τ) + T log T - T (for large T, with τ > 0)
  
  By conjugate symmetry, Im log Γ(τ - iT) = -Im log Γ(τ + iT) ≈ -(τ-1/2)(π/2) - T log T + T.
  
  Wait, more carefully: Im log Γ(τ - iT) = -Im log Γ(τ + iT) (since Γ(s̄) = Γ̅(s)).
  
  Im log Γ(τ + iT) ≈ (τ - 1/2) arctan(T/τ) + T log√(τ²+T²) - T ≈ (τ-1/2)(π/2) + T log T - T
  
  So Im log Γ(τ - iT) ≈ -(τ-1/2)(π/2) - T log T + T.
  
  As τ = 1-σ goes from 2 to 1/2 (σ from -1 to 1/2):
  At τ = 2: Im log Γ(2-iT) ≈ -(3/2)(π/2) - T log T + T = -3π/4 - T log T + T
  At τ = 1/2: Im log Γ(1/2-iT) ≈ -(0)(π/2) - T log T + T = -T log T + T
  
  Δ = (-T log T + T) - (-3π/4 - T log T + T) = 3π/4.

So Δ arg χ(s) on the path from -1+iT to 1/2+iT = 0 + 0 + (-3π/4) + 3π/4 + O(1/T) = O(1/T).

Interesting! The sin and Gamma contributions cancel. So:

[change from -1+iT to 1/2+iT in arg ζ] = Δ arg χ(s) + Δ arg ζ(1-s) = O(1/T) + (-π·S(T) + O(1)) = -π·S(T) + O(1)

And [change from 1/2+iT to 2+iT in arg ζ] = -π·S(T) + O(1) [computed earlier... wait, let me recheck]

Actually, [change from 2+iT to 1/2+iT] = π·S(T) - [change from 2 to 2+iT] = π·S(T) - O(1).
So [change from 1/2+iT to 2+iT] = -(π·S(T) - O(1)) = -π·S(T) + O(1).

Therefore:
Δ_{top} = [change from -1+iT to 1/2+iT] + [change from 1/2+iT to 2+iT]
= (-π·S(T) + O(1)) + (-π·S(T) + O(1))
= -2π·S(T) + O(1)

And Δ_{bottom} = Δ_{top} = -2π·S(T) + O(1).

So Δ_{top} + Δ_{bottom} = -4π·S(T) + O(1).

Now, putting it all together:

2π(2N(T) - 1) = Δ_{bottom} + Δ_{left} + Δ_{top} + Δ_{right}
= (-2π·S(T) + O(1)) + (-2T log(T/2π) + 2T - 3π/2 + O(1)) + (-2π·S(T) + O(1)) + O(1)
= -4π·S(T) - 2T log(T/2π) + 2T - 3π/2 + O(1)

So:
2N(T) - 1 = (1/2π)[-4π·S(T) - 2T log(T/2π) + 2T - 3π/2 + O(1)]
= -2S(T) - (T/π) log(T/2π) + T/π - 3/4 + O(1/π)

Hmm, this doesn't look right. Let me recheck.

Wait, I think I made an error. Let me recheck the contribution from the top and bottom.

Actually, I think the issue is with how S(T) is defined and how the top/bottom contributions work. Let me reconsider.

The problem might be that I'm double-counting S(T). Let me reconsider.

S(T) = (1/π) arg ζ(1/2 + iT), where arg is defined by continuous variation from s = 2 along the path 2 → 2+iT → 1/2+iT, starting with arg ζ(2) = 0.

So: arg ζ(1/2+iT) [along this path] = [Δ arg from 2 to 2+iT] + [Δ arg from 2+iT to 1/2+iT] = O(1) + [Δ arg from 2+iT to 1/2+iT].

Let me call [Δ arg from 2 to 2+iT] = α = O(1) (the change going up the right side).
And [Δ arg from 2+iT to 1/2+iT] = β.

So π·S(T) = α + β, hence β = π·S(T) - α = π·S(T) + O(1).

Now, [Δ arg from 1/2+iT to 2+iT] = -β = -π·S(T) + O(1).

And [Δ arg from -1+iT to 1/2+iT] = (from functional equation) Δ arg χ + Δ arg ζ(1-s).

For Δ arg ζ(1-s): 1-s goes from 2-iT to 1/2-iT as s goes from -1+iT to 1/2+iT. The change in arg ζ(1-s) along this path:

By conjugate symmetry, arg ζ(1/2-iT) [along path 2 → 2-iT → 1/2-iT] = -arg ζ(1/2+iT) [along path 2 → 2+iT → 1/2+iT] = -π·S(T).

And [Δ arg from 2 to 2-iT] = -α (by conjugate symmetry, going down instead of up).

So [Δ arg from 2-iT to 1/2-iT] = -π·S(T) - (-α) = -π·S(T) + α = -π·S(T) + O(1).

Thus Δ arg ζ(1-s) [as 1-s goes from 2-iT to 1/2-iT] = -π·S(T) + O(1).

And Δ arg χ(s) [from -1+iT to 1/2+iT] = O(1/T) (as computed, the sin and Gamma parts cancel).

So [Δ arg from -1+iT to 1/2+iT] = O(1/T) + (-π·S(T) + O(1)) = -π·S(T) + O(1).

Therefore:
Δ_{top} = [Δ arg from -1+iT to 1/2+iT] + [Δ arg from 1/2+iT to 2+iT]
= (-π·S(T) + O(1)) + (-π·S(T) + O(1))
= -2π·S(T) + O(1)

And by symmetry, Δ_{bottom} = Δ_{top} = -2π·S(T) + O(1).

Hmm wait, is Δ_{bottom} = Δ_{top}? Let me recheck.

Δ_{bottom} is the change in arg ζ(σ-iT) as σ goes from 2 to -1 (right to left along the bottom).

By conjugate symmetry, arg ζ(σ-iT) = -arg ζ(σ+iT) (pointwise). But the continuous argument along the bottom path (from 2-iT to -1-iT) relates to the continuous argument along the top path (from 2+iT to -1+iT) by:

arg_cont on bottom at σ = -arg_cont on top at σ (if both start from the same reference point with arg=0).

Actually, let me think about it more carefully. If we define arg_cont on the top starting from 2+iT with arg = arg_cont(2+iT) (the accumulated arg from the start of the contour), and arg_cont on the bottom starting from 2-iT with arg = 0 (if we start the contour there)...

This is getting confusing. Let me use a different approach.

**Cleaner approach: Use the functional equation symmetrically.**

Instead of splitting at 1/2, let me directly compute the change in arg around the full contour using the functional equation on the left half.

The contour goes counterclockwise: 2-iT → -1-iT → -1+iT → 2+iT → 2-iT.

Total change = Δ_{bottom} + Δ_{left} + Δ_{top} + Δ_{right} = 2π(2N(T) - 1).

**Right side (2+iT → 2-iT):** Δ_{right} = O(1).

**Left side (-1-iT → -1+iT):** Δ_{left} = -2T log(T/2π) + 2T - 3π/2 + O(1). [Computed above.]

**Top + Bottom:** I need to compute Δ_{top} + Δ_{bottom}.

Top: -1+iT → 2+iT (left to right).
Bottom: 2-iT → -1-iT (right to left).

By conjugate symmetry, the change in arg along the bottom (right to left) equals the change in arg along the top (right to left), because ζ(σ-iT) = ζ̅(σ+iT) implies arg ζ(σ-iT) = -arg ζ(σ+iT), and as we move right to left on both:

Δ_{bottom} [right to left] = arg ζ(-1-iT) - arg ζ(2-iT) = -arg ζ(-1+iT) + arg ζ(2+iT) = arg ζ(2+iT) - arg ζ(-1+iT)

Δ_{top} [left to right] = arg ζ(2+iT) - arg ζ(-1+iT)

So Δ_{bottom} = Δ_{top} = arg ζ(2+iT) - arg ζ(-1+iT) (in terms of continuous argument).

But this is the continuous argument, which accounts for winding. The issue is that the "continuous argument" at -1+iT depends on the path taken to reach it.

OK, I think the confusion is arising because I'm not being careful about the continuous argument. Let me use a completely different, cleaner approach.

**Cleanest approach: Directly use the argument principle with ξ(s).**

Actually, let me use the standard textbook approach that avoids these issues. The key insight is:

**Theorem (Riemann-von Mangoldt):** N(T) = (T/2π) log(T/2π) - T/2π + O(log T).

**Proof:**

We apply the argument principle to ζ(s) on the rectangle R with vertices 2-iT, 2+iT, -1+iT, -1-iT (counterclockwise). Since T is not an ordinate of a zero, no zeros lie on the boundary. Inside R, ζ has one pole (at s=1) and 2N(T) zeros (the non-trivial zeros with |γ| < T, counting conjugate pairs). Thus:

2N(T) - 1 = (1/2πi) ∮_R (ζ'/ζ)(s) ds = (1/2π) Δ_R arg ζ(s).    (1)

To evaluate Δ_R arg ζ(s), we split the contour into the right half (from 1/2-iT up to 2-iT, across to 2+iT, down to 1/2+iT) and the left half (from 1/2+iT across to -1+iT, down to -1-iT, across to 1/2-iT).

**Right half:** The change in arg ζ along the right half of the contour, starting from 1/2-iT, going right to 2-iT, up to 2+iT, left to 1/2+iT. By the conjugate symmetry ζ(s̄) = ζ̅(s), the change from 1/2-iT to 2-iT to 2+iT to 1/2+iT equals 2·arg ζ(1/2+iT) where the argument is defined by continuous variation from s=2 (where arg ζ(2)=0) along the path to 1/2+iT. Denoting S(T) = (1/π) arg ζ(1/2+iT), the right half contributes 2π·S(T) + O(1).

Hmm, I keep going in circles. Let me just look up the standard proof structure and reproduce it cleanly.

The standard proof (as in Ivić's "The Riemann Zeta-Function" or Titchmarsh):

1. By argument principle: 2N(T) - 1 = (1/2π) Δ_C arg ζ(s), where C is the rectangle.

2. The change in arg is decomposed as:
   Δ_C arg ζ = Δ_{C_R} arg ζ + Δ_{C_L} arg ζ
   where C_R is the right part (from 1/2-iT to 1/2+iT via the right side) and C_L is the left part (from 1/2+iT to 1/2-iT via the left side).

3. For C_R: Δ_{C_R} arg ζ = 2 arg ζ(1/2+iT) = 2π·S(T), where S(T) is defined with continuous arg from s=2.

4. For C_L: Use the functional equation ζ(s) = χ(s)ζ(1-s). On C_L, s goes from 1/2+iT to -1+iT to -1-iT to 1/2-iT. Then 1-s goes from 1/2-iT to 2-iT to 2+iT to 1/2+iT, which is the reverse of C_R. So:

   Δ_{C_L} arg ζ(s) = Δ_{C_L} arg χ(s) + Δ_{C_L} arg ζ(1-s)
   = Δ_{C_L} arg χ(s) - Δ_{C_R} arg ζ(s)    [since 1-s traverses C_R in reverse]
   = Δ_{C_L} arg χ(s) - 2π·S(T)

5. Therefore:
   Δ_C arg ζ = 2π·S(T) + Δ_{C_L} arg χ(s) - 2π·S(T) = Δ_{C_L} arg χ(s)

   So the S(T) terms cancel! And we get:

   2π(2N(T) - 1) = Δ_{C_L} arg χ(s)

6. Now we compute Δ_{C_L} arg χ(s), where C_L goes from 1/2+iT to -1+iT (left along top), down to -1-iT, right to 1/2-iT.

   χ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) = π^{s-1/2} Γ((1-s)/2)/Γ(s/2)

   Let me use the form χ(s) = π^{s-1/2} Γ((1-s)/2)/Γ(s/2).

   On C_L:
   - Top: s = σ+iT, σ from 1/2 to -1
   - Left: s = -1+it, t from T to -T
   - Bottom: s = σ-iT, σ from -1 to 1/2

   Δ_{C_L} arg χ(s) = Δ arg[π^{s-1/2}] + Δ arg[Γ((1-s)/2)] - Δ arg[Γ(s/2)]

   **Δ arg[π^{s-1/2}]:**
   π^{s-1/2} = π^{σ-1/2} · π^{it}, arg = t log π.
   - Top: t = T constant, Δ = 0
   - Left: t from T to -T, Δ = -2T log π
   - Bottom: t = -T constant, Δ = 0
   Total: -2T log π

   **Δ arg[Γ(s/2)]:**
   s/2 goes along the path: (1/4+iT/2) → (-1/2+iT/2) → (-1/2-iT/2) → (1/4-iT/2).
   This is a rectangle with vertices 1/4+iT/2, -1/2+iT/2, -1/2-iT/2, 1/4-iT/2, traversed in the same direction (counterclockwise? Let me check: σ from 1/2 to -1 at height T means s/2 goes from 1/4+iT/2 to -1/2+iT/2, i.e., leftward at the top. Then down the left side. Then rightward at the bottom. This is clockwise!)

   Actually, C_L goes: top (left), left (down), bottom (right). So s/2 traces: top-left, left-down, bottom-right, which is clockwise.

   By the argument principle applied to Γ(s/2) (which has no zeros and poles at s/2 = 0, -1, -2, ..., i.e., s = 0, -2, -4, ...):

   The poles of Γ(s/2) inside the rectangle with vertices 1/4±iT/2, -1/2±iT/2 are at s/2 = 0, -1, ..., i.e., s = 0, -2, .... But s/2 = 0 means s = 0, and s/2 = -1/2 is the left edge. The rectangle in s/2-plane has vertices 1/4±iT/2, -1/2±iT/2. The poles of Γ at 0, -1, -2, ... : 0 is inside (since -1/2 < 0 < 1/4), -1 is on the left edge (s/2 = -1/2), -2 is outside.

   Hmm, this is getting complicated with the poles. Let me use Stirling's formula directly instead.

   **Using Stirling's formula directly:**

   For the change in arg Γ(s/2) along C_L (clockwise), we can use Stirling's formula. But since the path goes through regions where Stirling might not apply (near the negative real axis), let me use the reflection formula or just compute directly.

   Actually, let me use the form χ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s) instead, which might be easier.

   χ(s) = 2^s π^{s-1} sin(πs/2) Γ(1-s)

   On C_L:
   - 2^s: arg = t log 2. Top: t=T, Δ=0. Left: t from T to -T, Δ = -2T log 2. Bottom: t=-T, Δ=0. Total: -2T log 2.
   - π^{s-1}: arg = t log π. Same pattern. Total: -2T log π.
   - sin(πs/2): On the top (s=σ+iT, σ from 1/2 to -1): arg sin(π(σ+iT)/2) ≈ π(1-σ)/2 for large T (as computed earlier). At σ=1/2: arg ≈ π/4. At σ=-1: arg ≈ π. Δ = π - π/4 = 3π/4.
     On the left (s=-1+it, t from T to -T): sin(π(-1+it)/2) = -cosh(πt/2) < 0, arg = π constant. Δ = 0.
     On the bottom (s=σ-iT, σ from -1 to 1/2): By conjugate symmetry, arg sin(π(σ-iT)/2) = -arg sin(π(σ+iT)/2) ≈ -π(1-σ)/2. At σ=-1: arg ≈ -π. At σ=1/2: arg ≈ -π/4. Δ = -π/4 - (-π) = 3π/4.
     Total Δ arg sin(πs/2) = 3π/4 + 0 + 3π/4 = 3π/2.

   - Γ(1-s): 1-s traces C_R in reverse (from 1/2-iT to 2-iT to 2+iT to 1/2+iT, i.e., counterclockwise on the right rectangle). Using Stirling for Γ on the right side where Re is large:

     Actually, 1-s on C_L:
     - Top (s=σ+iT, σ from 1/2 to -1): 1-s = 1-σ-iT, Re from 1/2 to 2, Im = -T.
     - Left (s=-1+it, t from T to -T): 1-s = 2-it, Re = 2, Im from -T to T.
     - Bottom (s=σ-iT, σ from -1 to 1/2): 1-s = 1-σ+iT, Re from 2 to 1/2, Im = T.

     So 1-s traces a path from 1/2-iT → 2-iT → 2+iT → 1/2+iT (going right along bottom, up the right side, left along top). This is counterclockwise around the right rectangle.

     Using Stirling: Im log Γ(w) ≈ (Re(w)-1/2) arg(w) + Im(w) log|w| - Im(w) for large |w|.

     For w = 1-s, we need the change in Im log Γ(1-s) along C_L.

     Let me compute this using Stirling on each piece:

     **Top of C_L (s = σ+iT, σ: 1/2 → -1, so w = 1-σ-iT, Re(w): 1/2 → 2, Im(w) = -T):**
     Im log Γ(w) ≈ (Re(w)-1/2)·arctan(Im(w)/Re(w)) + Im(w)·log|w| - Im(w)
     = (1-σ-1/2)·arctan(-T/(1-σ)) + (-T)·log√((1-σ)²+T²) + T
     ≈ (1/2-σ)·(-π/2) + (-T)·log T + T   (for large T, arctan(-T/a) → -π/2)
     = -π(1/2-σ)/2 - T log T + T

     At σ=1/2 (w=1/2-iT): -π·0/2 - T log T + T = -T log T + T
     At σ=-1 (w=2-iT): -π·3/2/2 - T log T + T = -3π/4 - T log T + T
     Δ = (-3π/4 - T log T + T) - (-T log T + T) = -3π/4

     **Left of C_L (s = -1+it, t: T → -T, so w = 2-it, Re(w)=2, Im(w) = -t: -T → T):**
     Im log Γ(2+iu) ≈ (3/2)·arctan(u/2) + u·log√(4+u²) - u
     At u = -T (t=T): (3/2)·(-π/2) + (-T)·log T + T = -3π/4 - T log T + T
     At u = T (t=-T): (3/2)·(π/2) + T·log T - T = 3π/4 + T log T - T
     Δ = (3π/4 + T log T - T) - (-3π/4 - T log T + T) = 3π/2 + 2T log T - 2T

     **Bottom of C_L (s = σ-iT, σ: -1 → 1/2, so w = 1-σ+iT, Re(w): 2 → 1/2, Im(w) = T):**
     Im log Γ(w) ≈ (Re(w)-1/2)·arctan(T/Re(w)) + T·log|w| - T
     = (1/2-σ)·(π/2) + T·log T - T   (for large T)
     = π(1/2-σ)/2 + T log T - T

     At σ=-1 (w=2+iT): π·3/2/2 + T log T - T = 3π/4 + T log T - T
     At σ=1/2 (w=1/2+iT): π·0/2 + T log T - T = T log T - T
     Δ = (T log T - T) - (3π/4 + T log T - T) = -3π/4

     Total Δ arg Γ(1-s) = -3π/4 + 3π/2 + 2T log T - 2T + (-3π/4) = 2T log T - 2T + 3π/2

   So Δ_{C_L} arg χ(s) = (-2T log 2) + (-2T log π) + 3π/2 + (2T log T - 2T + 3π/2) + O(1)
   = 2T log T - 2T log(2π) - 2T + 3π + O(1)
   = 2T log(T/2π) - 2T + 3π + O(1)

   Wait, let me recheck: -2T log 2 - 2T log π + 2T log T = 2T(log T - log 2 - log π) = 2T log(T/2π). And -2T. And 3π/2 + 3π/2 = 3π.

   So Δ_{C_L} arg χ(s) = 2T log(T/2π) - 2T + 3π + O(1).

   From step 5: 2π(2N(T) - 1) = Δ_{C_L} arg χ(s) = 2T log(T/2π) - 2T + 3π + O(1).

   So: 2N(T) - 1 = (1/2π)[2T log(T/2π) - 2T + 3π + O(1)]
   = (T/π) log(T/2π) - T/π + 3/2 + O(1)

   Hmm, that gives N(T) = (T/2π) log(T/2π) - T/2π + 5/4 + O(1), which has the wrong constant (should be 7/8). Let me check where I went wrong.

   Actually, the constant doesn't matter for the limit—we just need N(T) / [(T/2π)log(T/2π) - T/2π] → 1. The O(1) and constant terms are lower order. So even if I got the constant wrong, the asymptotic is correct.

   But let me double-check the main term. We have:

   2π(2N(T) - 1) = 2T log(T/2π) - 2T + O(1) + (constant)

   So 2N(T) = (T/π) log(T/2π) - T/π + O(1), hence N(T) = (T/2π) log(T/2π) - T/2π + O(1).

   Since the O(1) term is negligible compared to (T/2π) log(T/2π) - T/2π ~ (T/2π) log T, we get:

   N(T) / [(T/2π) log(T/2π) - T/2π] → 1.

   Wait, but I need to verify that the error is indeed O(1) or at most O(log T), not something larger. The error comes from:
   - Stirling's formula errors: O(1/T) on each piece, total O(1/T).
   - The O(1) from ζ(1-s) on the right side: O(1).
   - The approximation of arg sin(πs/2): O(1/T) for large T.

   Actually wait, I need to also account for the fact that on the top and bottom of C_L, when Re(w) = Re(1-s) is close to 1/2, Stirling's formula might not be as accurate, and also ζ(1-s) might not be bounded when Re(1-s) = 1/2 (since there could be zeros nearby). But the change in arg ζ(1-s) on these segments is part of what we're computing, and it's accounted for in the S(T) cancellation.

   Hmm, actually, I think the issue is more subtle. Let me reconsider step 5.

   In step 5, I claimed Δ_{C_L} arg ζ(1-s) = -Δ_{C_R} arg ζ(s) = -2π·S(T). But this requires that 1-s traverses C_R exactly in reverse. Let me verify:

   C_L: 1/2+iT → -1+iT → -1-iT → 1/2-iT
   1-s on C_L: 1/2-iT → 2-iT → 2+iT → 1/2+iT

   C_R (the right half of the contour, counterclockwise): 1/2-iT → 2-iT → 2+iT → 1/2+iT.

   Yes! 1-s on C_L traces exactly C_R (counterclockwise). So:

   Δ_{C_L} arg ζ(1-s) = Δ_{C_R} arg ζ(w) = 2π·S(T) + O(1)

   Wait, is it +2π·S(T) or -2π·S(T)? Since 1-s traces C_R in the same direction (counterclockwise), the change in arg ζ(1-s) along C_L equals the change in arg ζ(w) along C_R, which is 2π·S(T) + O(1).

   Hmm, but then:

   Δ_{C_L} arg ζ(s) = Δ_{C_L} arg χ(s) + Δ_{C_L} arg ζ(1-s) = Δ_{C_L} arg χ(s) + 2π·S(T) + O(1)

   And Δ_C arg ζ = Δ_{C_R} arg ζ + Δ_{C_L} arg ζ = 2π·S(T) + Δ_{C_L} arg χ(s) + 2π·S(T) + O(1)
   = Δ_{C_L} arg χ(s) + 4π·S(T) + O(1)

   So: 2π(2N(T) - 1) = Δ_{C_L} arg χ(s) + 4π·S(T) + O(1)

   And S(T) = O(log T) (this is a known result, but let me see if I need to prove it or if it's enough for the limit).

   Actually, for the limit N(T)/[...] → 1, I need to show that the error terms are o(T log T). Since S(T) = O(log T) and Δ_{C_L} arg χ(s) = 2T log(T/2π) - 2T + O(1), we get:

   2N(T) = 1 + (1/2π)[2T log(T/2π) - 2T + O(1) + 4π·S(T) + O(1)]
   = 1 + (T/π) log(T/2π) - T/π + O(1) + 2S(T)
   = (T/π) log(T/2π) - T/π + O(log T)

   So N(T) = (T/2π) log(T/2π) - T/2π + O(log T), and since O(log T) = o(T log T), the limit follows.

   But wait, I need to verify that S(T) = O(log T). This is a standard result but let me see if I should prove it.

   S(T) = (1/π) arg ζ(1/2 + iT). The bound S(T) = O(log T) follows from the estimate |ζ(1/2 + it)| = O(t^{1/6+ε}) or more elementarily from the functional equation and bounds on ζ'/ζ. Actually, the classical bound S(T) = O(log T) can be proved using the Borel-Carathéodory theorem or Jensen's formula applied to ζ(s) in a disk around 1/2 + iT.

   For the purpose of this proof, I think it's acceptable to cite that S(T) = O(log T) as a standard estimate, since the problem asks to show the limit, not to derive the full asymptotic with error term.

   Actually, let me reconsider whether I even need the S(T) = O(log T) bound. Let me re-examine whether the S(T) terms actually cancel.

   Going back to step 5: I think I made an error. Let me redo this.

   The full contour C = C_R + C_L where:
   - C_R: 1/2-iT → 2-iT → 2+iT → 1/2+iT (right half, counterclockwise)
   - C_L: 1/2+iT → -1+iT → -1-iT → 1/2-iT (left half, counterclockwise)

   Δ_C arg ζ = Δ_{C_R} arg ζ + Δ_{C_L} arg ζ = 2π(2N(T) - 1)

   For C_L, use ζ(s) = χ(s)ζ(1-s):
   Δ_{C_L} arg ζ(s) = Δ_{C_L} arg χ(s) + Δ_{C_L} arg ζ(1-s)

   Now, as s traverses C_L (1/2+iT → -1+iT → -1-iT → 1/2-iT), 1-s traverses:
   1/2-iT → 2-iT → 2+iT → 1/2+iT, which is exactly C_R.

   So Δ_{C_L} arg ζ(1-s) = Δ_{C_R} arg ζ(w).

   Therefore:
   Δ_C arg ζ = Δ_{C_R} arg ζ + Δ_{C_L} arg χ(s) + Δ_{C_R} arg ζ
   = 2·Δ_{C_R} arg ζ + Δ_{C_L} arg χ(s)

   So: 2π(2N(T) - 1) = 2·Δ_{C_R} arg ζ + Δ_{C_L} arg χ(s)

   Now, Δ_{C_R} arg ζ is the change in arg ζ going from 1/2-iT to 2-iT to 2+iT to 1/2+iT. By conjugate symmetry, the change from 1/2-iT to 2-iT to 2+iT to 1/2+iT is twice the change from 2 to 2+iT to 1/2+iT (i.e., 2π·S(T)) plus some correction... actually, let me think about this.

   The path C_R goes: 1/2-iT → 2-iT → 2+iT → 1/2+iT.
   By conjugate symmetry, the change from 1/2-iT to 2-iT (going right at height -T) equals the change from 1/2+iT to 2+iT (going right at height +T) [both are the same by conjugate symmetry, since arg ζ(σ-iT) = -arg ζ(σ+iT), and the change going right is the same].

   Hmm, let me think about this differently. The change from 2-iT to 2+iT (going up the right side) is O(1) (call it α). The change from 2+iT to 1/2+iT (going left at height T) is β. The change from 1/2-iT to 2-iT (going right at height -T) is, by conjugate symmetry, equal to β (the change from 1/2+iT to 2+iT reversed, which is -β... no).

   OK let me just carefully track. Define the continuous argument starting from s = 2 with arg = 0.

   Path from 2 to 2+iT: change = α = O(1). So arg at 2+iT = α.
   Path from 2+iT to 1/2+iT: change = β. So arg at 1/2+iT = α + β = π·S(T).
   Path from 2 to 2-iT: by conjugate symmetry, change = -α. So arg at 2-iT = -α.
   Path from 2-iT to 1/2-iT: by conjugate symmetry, change = -β. So arg at 1/2-iT = -α - β = -π·S(T).

   Now, C_R goes: 1/2-iT → 2-iT → 2+iT → 1/2+iT.
   - 1/2-iT → 2-iT: change = arg(2-iT) - arg(1/2-iT) = (-α) - (-α-β) = β. But wait, this is the change going right from 1/2-iT to 2-iT. By conjugate symmetry, this should be the negative of the change from 1/2+iT to 2+iT, which is -(-β) = β. Yes, it's β.

   Actually, the change from 1/2-iT to 2-iT (going right) = arg(2-iT) - arg(1/2-iT) = -α - (-α-β) = β. ✓

   - 2-iT → 2+iT: change = arg(2+iT) - arg(2-iT) = α - (-α) = 2α.
   
   - 2+iT → 1/2+iT: change = arg(1/2+iT) - arg(2+iT) = (α+β) - α = β.

   So Δ_{C_R} arg ζ = β + 2α + β = 2β + 2α = 2(α + β) = 2π·S(T).

   So Δ_{C_R} arg ζ = 2π·S(T). (The O(1) from α is absorbed into S(T) since S(T) includes it.)

   Therefore:
   2π(2N(T) - 1) = 2·2π·S(T) + Δ_{C_L} arg χ(s) = 4π·S(T) + Δ_{C_L} arg χ(s)

   And Δ_{C_L} arg χ(s) = 2T log(T/2π) - 2T + 3π + O(1) [computed above].

   So:
   2N(T) - 1 = (1/2π)[4π·S(T) + 2T log(T/2π) - 2T + 3π + O(1)]
   = 2S(T) + (T/π) log(T/2π) - T/π + 3/2 + O(1)

   N(T) = (T/2π) log(T/2π) - T/2π + S(T) + O(1)

   Now, S(T) = O(log T) (standard estimate). So:

   N(T) = (T/2π) log(T/2π) - T/2π + O(log T)

   Since (T/2π) log(T/2π) - T/2π ~ (T/2π) log T → ∞ and O(log T) = o(T log T):

   N(T) / [(T/2π) log(T/2π) - T/2π] = 1 + O(log T) / [(T/2π) log(T/2π) - T/2π] → 1.

   Now I need to also justify that S(T) = O(log T). Let me include a brief justification.

   **Bounding S(T):**

   S(T) = (1/π) arg ζ(1/2 + iT). By the functional equation and known bounds, or more directly:

   The bound S(T) = O(log T) follows from standard estimates. One way: use the Borel-Carathéodory theorem applied to log ζ(s) in a disk of radius ~1/log T centered at 1 + iT (or similar), which gives |ζ'/ζ(s)| = O(log T) for s in a region including the path from 2 to 1/2+iT, and then S(T) = (1/π) ∫ Im(ζ'/ζ) ds along the path, which is O(log T) · O(1) = O(log T) (the path has bounded length and |ζ'/ζ| = O(log T)).

   More precisely: for s = σ + iT with 1/2 ≤ σ ≤ 2, we have |ζ'/ζ(s)| = O(log T) (this follows from the standard bounds on ζ'/ζ in the critical strip, which can be derived from the Borel-Carathéodory theorem). Then:

   |S(T)| ≤ (1/π) ∫_{path} |ζ'/ζ(s)| |ds| = O(log T) · O(1) = O(log T)

   since the path from 2 to 2+iT to 1/2+iT has length O(T)... wait, that's O(T), not O(1). The vertical part has length T.

   Hmm, that gives O(T log T), which is too big. Let me reconsider.

   The path from 2 to 2+iT has length T, and |ζ'/ζ(2+it)| = O(1) (since ζ is bounded away from 0 on Re=2), so the contribution is O(T)·O(1) = O(T). That's still too big.

   Wait, no. On Re(s) = 2, |ζ'/ζ(s)| = O(1) (bounded), and the change in arg is the integral of Im(ζ'/ζ) ds, which is O(T)·O(1) = O(T). But we said the change is O(1). Let me reconcile.

   The change in arg on the right side is ∫ Im(ζ'/ζ(2+it)) dt from 0 to T. Since |ζ(2+it) - 1| < 1, we have ζ(2+it) in a disk not containing 0, so the total change in arg is bounded by the total angle subtended, which is O(1). The point is that Im(ζ'/ζ) oscillates and the integral is O(1), not O(T), even though the integrand is O(1).

   More precisely, ζ(2+it) = 1 + O(2^{-2}), so ζ'/ζ(2+it) = O(2^{-2}) = O(1), and the integral ∫_0^T Im(ζ'/ζ(2+it)) dt = O(1) · T... no, that's O(T).

   Hmm, actually ζ'/ζ(s) = -Σ_{n=1}^∞ Λ(n) n^{-s} / ζ(s) for Re(s) > 1. On Re(s) = 2, |ζ'/ζ(s)| ≤ Σ Λ(n) n^{-2} / |ζ(s)| = O(1). And the integral ∫_0^T O(1) dt = O(T). But the actual change in arg is O(1) because the arg of ζ(2+it) is O(1) (it stays near 1).

   The resolution: the change in arg is arg ζ(2+iT) - arg ζ(2), and arg ζ(2+iT) = O(1) since |ζ(2+iT) - 1| < 1. So the change is O(1), even though the integral of |ζ'/ζ| is O(T). The integral of Im(ζ'/ζ) is the change in arg, which is O(1), but this is because Im(ζ'/ζ) oscillates.

   OK so the change on the right side is O(1), and the change from 2+iT to 1/2+iT (horizontal path of length 3/2) is ∫ Im(ζ'/ζ(σ+iT)) dσ, which is O(log T) · O(1) = O(log T) if |ζ'/ζ| = O(log T) on this segment.

   So S(T) = (1/π)[O(1) + O(log T)] = O(log T). ✓

   The bound |ζ'/ζ(σ+iT)| = O(log T) for 1/2 ≤ σ ≤ 2 follows from standard estimates (e.g., from the Borel-Carathéodory theorem or from the Hadamard product for ξ(s)).

   Actually, for σ ≥ 1 + 1/log T, |ζ'/ζ| = O(log T) is easy. For 1/2 ≤ σ < 1, one uses the functional equation or the Borel-Carathéodory theorem. The standard result is that for σ ≥ 1/2 and |t| ≥ 2, |ζ'/ζ(σ+it)| = O(log t) except near zeros, but the integrated bound on S(T) still holds.

   The precise statement is: S(T) = O(log T). This is a classical result of von Mangoldt. For our purposes, we can cite this.

   Actually, I realize I should be more careful. The bound S(T) = O(log T) is indeed classical and follows from the estimate:

   S(T) = O(log T / log log T) ... no, the classical bound is S(T) = O(log T).

   The proof uses the fact that for s = σ + iT with 1/2 ≤ σ ≤ 2, and T not an ordinate of a zero, |ζ'/ζ(s)| = O(log² T) (from the Hadamard product), and then S(T) = (1/π) ∫ Im(ζ'/ζ) ds along a path of length O(1) (the horizontal part from 2+iT to 1/2+iT) plus the vertical part which is O(1). So S(T) = O(log² T) · O(1) = O(log² T).

   Hmm, that gives O(log² T), not O(log T). But O(log² T) is still o(T log T), so it's fine for our limit!

   Actually, the sharper bound S(T) = O(log T) requires more work, but O(log² T) is sufficient for the limit. Let me use O(log² T) to be safe.

   Wait, actually, the standard bound from the Hadamard product gives |ζ'/ζ(s)| = O(log T) for σ ≥ 1/2 (away from zeros), not O(log² T). The O(log² T) bound is for σ near 1/2. But in any case, S(T) = O(log² T) is more than enough.

   Actually, the cleanest bound: by Jensen's formula or the Borel-Carathéodory theorem applied to log ζ(s) in a disk centered at 2+iT of radius 3/2, one can show that |log ζ(s)| = O(log T) for s near 1/2+iT, which gives S(T) = O(log T). But the details are technical.

   For the purpose of this proof, I'll use the fact that S(T) = O(log T) (or even O(log² T), which is easier to prove and still sufficient).

   Let me now also verify the computation of Δ_{C_L} arg χ(s) more carefully.

   Actually, I realize there might be an issue with the sin(πs/2) factor when σ is between -1 and 1/2 on the top/bottom of C_L. Let me recheck.

   On the top of C_L (s = σ + iT, σ from 1/2 to -1):
   sin(πs/2) = sin(πσ/2 + iπT/2) = sin(πσ/2)cosh(πT/2) + i cos(πσ/2)sinh(πT/2)

   For large T, cosh(πT/2) ≈ sinh(πT/2) ≈ e^{πT/2}/2, so:
   sin(πs/2) ≈ (e^{πT/2}/2)[sin(πσ/2) + i cos(πσ/2)] = (e^{πT/2}/2) · e^{i(π/2 - πσ/2)}

   So arg sin(πs/2) ≈ π/2 - πσ/2 = π(1-σ)/2.

   At σ = 1/2: arg ≈ π(1/2)/2 = π/4
   At σ = -1: arg ≈ π(2)/2 = π
   Δ = π - π/4 = 3π/4. ✓

   On the bottom of C_L (s = σ - iT, σ from -1 to 1/2):
   sin(πs/2) = sin(πσ/2 - iπT/2) = sin(πσ/2)cosh(πT/2) - i cos(πσ/2)sinh(πT/2)
   ≈ (e^{πT/2}/2)[sin(πσ/2) - i cos(πσ/2)] = (e^{πT/2}/2) · e^{-i(π/2 - πσ/2)}

   arg ≈ -(π/2 - πσ/2) = -π(1-σ)/2.

   At σ = -1: arg ≈ -π
   At σ = 1/2: arg ≈ -π/4
   Δ = -π/4 - (-π) = 3π/4. ✓

   On the left of C_L (s = -1 + it, t from T to -T):
   sin(πs/2) = sin(-π/2 + iπt/2) = -cosh(πt/2) (real, negative)
   arg = π (constant)
   Δ = 0. ✓

   Total Δ arg sin(πs/2) = 3π/4 + 0 + 3π/4 = 3π/2. ✓

   And the Γ(1-s) computation:
   Total Δ arg Γ(1-s) = -3π/4 +
