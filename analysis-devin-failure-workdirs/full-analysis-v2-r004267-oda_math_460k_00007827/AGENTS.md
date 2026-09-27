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
  <problem_id>oda_math_460k_00007827</problem_id>
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

A closed rectangular box costs \( A \) cents per square foot for the top and bottom and \( B \) cents per square foot for the sides. If the volume \( V \) is fixed, what should the dimensions of the box be to minimize the cost?

## Standard Solution

<think>Okay, let's try to solve this problem. We need to find the dimensions of a closed rectangular box that minimizes the cost, given that the volume is fixed. The cost depends on the areas of the top/bottom and the sides, with different rates per square foot. 

First, let's define the variables. Let's say the box has length \( l \), width \( w \), and height \( h \). All these are positive real numbers. The volume \( V \) is fixed, so \( V = lwh \). That's our constraint.

Now, let's figure out the cost. The top and bottom are both rectangles with area \( lw \), so together their area is \( 2lw \). The cost for these is \( A \) cents per square foot, so the cost for top and bottom is \( 2lw \times A = 2Alw \).

Next, the sides. There are four sides: two with area \( lh \) (front and back) and two with area \( wh \) (left and right). So the total area of the sides is \( 2lh + 2wh \). The cost for the sides is \( B \) cents per square foot, so the cost for the sides is \( (2lh + 2wh) \times B = 2B(lh + wh) \).

Total cost \( C \) is the sum of these two parts: \( C = 2Alw + 2B(lh + wh) \). Our goal is to minimize \( C \) subject to the volume constraint \( lwh = V \).

Since we have a constraint, we can use the method of Lagrange multipliers, but maybe it's simpler to express one variable in terms of the others using the volume equation and then minimize the cost function with two variables. Let's try that.

From \( V = lwh \), we can solve for \( h \): \( h = V/(lw) \). Let's substitute this into the cost function. Then:

\( C(l, w) = 2Alw + 2B\left(l \times \frac{V}{lw} + w \times \frac{V}{lw}\right) \)

Simplify the terms inside the parentheses:

\( l \times \frac{V}{lw} = V/w \), and \( w \times \frac{V}{lw} = V/l \). So:

\( C(l, w) = 2Alw + 2B\left( \frac{V}{w} + \frac{V}{l} \right) \)

Now, we need to minimize \( C(l, w) \) with respect to \( l \) and \( w \). To find the minimum, we can take partial derivatives with respect to \( l \) and \( w \), set them to zero, and solve the equations.

First, compute the partial derivative of \( C \) with respect to \( l \):

\( \frac{\partial C}{\partial l} = 2A w + 2B \left( 0 - \frac{V}{l^2} \right) \) Wait, no. Let's do it correctly. The term \( 2Alw \) derivative with respect to \( l \) is \( 2A w \). The next term is \( 2B V \left( \frac{1}{l} + \frac{1}{w} \right) \), so derivative with respect to \( l \) is \( 2B V \times (-1/l^2) \). So:

\( \frac{\partial C}{\partial l} = 2A w - \frac{2B V}{l^2} \)

Similarly, partial derivative with respect to \( w \):

\( \frac{\partial C}{\partial w} = 2A l - \frac{2B V}{w^2} \)

Set both partial derivatives to zero for critical points:

1. \( 2A w - \frac{2B V}{l^2} = 0 \) → \( A w = \frac{B V}{l^2} \) → \( w = \frac{B V}{A l^2} \) ...(1)

2. \( 2A l - \frac{2B V}{w^2} = 0 \) → \( A l = \frac{B V}{w^2} \) → \( l = \frac{B V}{A w^2} \) ...(2)

Now, let's substitute equation (1) into equation (2). From (1), \( w = (B V)/(A l^2) \). Let's plug this into (2):

\( l = \frac{B V}{A \left( \frac{B V}{A l^2} \right)^2} \)

Let's simplify the denominator:

\( \left( \frac{B V}{A l^2} \right)^2 = \frac{B^2 V^2}{A^2 l^4} \)

So denominator is \( A \times \frac{B^2 V^2}{A^2 l^4} = \frac{B^2 V^2}{A l^4} \)

Thus, the right-hand side becomes \( \frac{B V}{ \frac{B^2 V^2}{A l^4} } = \frac{B V \times A l^4}{B^2 V^2} = \frac{A l^4}{B V} \)

So equation (2) becomes:

\( l = \frac{A l^4}{B V} \)

Multiply both sides by \( B V \):

\( l B V = A l^4 \)

Assuming \( l \neq 0 \), divide both sides by \( l \):

\( B V = A l^3 \)

Thus, \( l^3 = \frac{B V}{A} \) → \( l = \left( \frac{B V}{A} \right)^{1/3} \)

Now, let's find \( w \) using equation (1). From (1):

\( w = \frac{B V}{A l^2} \)

We know \( l^3 = B V / A \), so \( l^2 = (B V / A)^{2/3} \). Let's substitute:

\( w = \frac{B V}{A} \times \frac{1}{l^2} = \frac{B V}{A} \times \frac{1}{(B V / A)^{2/3}} \)

Simplify \( (B V / A)^{2/3} = (B V / A)^{2/3} \), so:

\( w = (B V / A)^{1 - 2/3} = (B V / A)^{1/3} = l \)

Wait, that's interesting. So \( w = l \). So length and width are equal. That suggests the base is a square. Let's check that.

Alternatively, let's compute \( w \):

Since \( l = (B V / A)^{1/3} \), then \( l^2 = (B V / A)^{2/3} \). Then:

\( w = (B V)/(A l^2) = (B V)/(A) * 1/(B V / A)^{2/3} = (B V / A)^{1 - 2/3} = (B V / A)^{1/3} = l \). Yes, so \( w = l \).

Now, let's find \( h \). Recall \( h = V/(lw) \). Since \( l = w \), then \( lw = l^2 \), so \( h = V / l^2 \).

But we can express \( l \) in terms of \( V \), \( A \), and \( B \). Let's see:

We have \( l^3 = B V / A \), so \( l^2 = (B V / A)^{2/3} \). Then \( h = V / (B V / A)^{2/3} \). Let's simplify that:

\( h = V / ( (B V)^{2/3} / A^{2/3} ) ) = V * A^{2/3} / (B^{2/3} V^{2/3}) ) = A^{2/3} V^{1 - 2/3} / B^{2/3} = A^{2/3} V^{1/3} / B^{2/3} = (A^2 V / B^2)^{1/3} = (V A^2 / B^2)^{1/3} \)

Alternatively, let's express \( h \) in terms of \( l \). Since \( l = (B V / A)^{1/3} \), then \( l^3 = B V / A \), so \( V = A l^3 / B \). Then \( h = V / l^2 = (A l^3 / B) / l^2 = (A l)/B \). So \( h = (A / B) l \). That's another way to write it.

Alternatively, let's see if we can express all variables in terms of each other. Since \( l = w \), let's denote \( l = w = x \), then \( h = V/(x^2) \). Let's check the cost function again with this substitution. Maybe that's a simpler approach. Let's try that.

Let \( l = w = x \), then \( h = V / x^2 \). Then the cost \( C = 2A x^2 + 2B(2x h) \)? Wait, no. Wait, the sides: two sides are \( l h \) (front and back), two sides are \( w h \) (left and right). But if \( l = w = x \), then all four sides are \( x h \), so total side area is \( 4x h \). Wait, no, original sides: 2(lh) + 2(wh). If l = w, then 2xh + 2xh = 4xh. So yes. Then cost for sides is 2B*(4xh)/2? Wait no, original cost for sides is 2B(lh + wh). Since l = w, that's 2B(xh + xh) = 2B(2xh) = 4Bxh. So total cost C = 2A x² + 4B x h. But h = V/x², so C = 2A x² + 4B x (V/x²) = 2A x² + 4B V / x. Then take derivative of C with respect to x: dC/dx = 4A x - 4B V / x². Set to zero: 4A x = 4B V / x² → A x = B V / x² → A x³ = B V → x³ = B V / A → x = (B V / A)^(1/3). Which matches our earlier result for l. Then h = V / x² = V / ( (B V / A)^(2/3) ) = V / ( (B² V² / A²)^(1/3) ) = V / ( B^(2/3) V^(2/3) / A^(2/3) ) ) = V * A^(2/3) / ( B^(2/3) V^(2/3) ) ) = A^(2/3) V^(1/3) / B^(2/3) = (A² V / B²)^(1/3). Alternatively, h = (A² V / B²)^(1/3). 

But let's check if this is indeed a minimum. We can use the second derivative test. For the two-variable case, we can check the Hessian, but since we reduced it to one variable (since l = w), let's see. For the one-variable case, after setting l = w, the second derivative of C with respect to x is 4A + 8B V / x³, which is positive, so it's a minimum.

Alternatively, going back to the original variables. We found that l = w, and h = (A/B) l. Let's verify that. From earlier, h = (A/B) l. Since l = (B V / A)^(1/3), then h = (A/B) * (B V / A)^(1/3) = (A/B) * (B/A)^(1/3) V^(1/3) ) = A^(1 - 1/3) B^( -1 + 1/3) V^(1/3) ) = A^(2/3) B^(-2/3) V^(1/3) = (A² V / B²)^(1/3), which matches the earlier expression for h.

So the dimensions are: length = width = (B V / A)^(1/3), height = (A² V / B²)^(1/3). Alternatively, we can write them in terms of exponents:

Let me denote the cube root as ^(1/3). So:

l = w = (B V / A)^(1/3)

h = (A² V / B²)^(1/3)

Alternatively, we can express h in terms of l. Since l = (B V / A)^(1/3), then h = (A/B) l. Let's check:

(A/B) l = (A/B) * (B V / A)^(1/3) = A^(1) B^(-1) * B^(1/3) V^(1/3) A^(-1/3) ) = A^(1 - 1/3) B^(-1 + 1/3) V^(1/3) = A^(2/3) B^(-2/3) V^(1/3), which is the same as h's expression. So that's correct.

Alternatively, let's see if we can write all dimensions in terms of each other. Let's see:

Let’s denote the cube root of (B V / A) as l, so l = (B V / A)^(1/3). Then:

w = l, as we found.

h = (A² V)/(B²)^(1/3) = (A² / B²)^(1/3) V^(1/3) = (A² / B²)^(1/3) (V)^(1/3) = (A² V / B²)^(1/3). But since V = l w h, and l = w, then V = l² h. Let's check:

l² h = (B V / A)^(2/3) * (A² V / B²)^(1/3) = (B² V² / A²)^(1/3) * (A² V / B²)^(1/3) = [ (B² V² / A²) * (A² V / B²) ]^(1/3) = (V³)^(1/3) = V. Correct, that checks out.

So the minimal cost occurs when length and width are equal, each being the cube root of (B V / A), and height is the cube root of (A² V / B²). 

Alternatively, we can express the dimensions as:

Let’s let the length and width be \( x \), then height \( y \). Then from the volume, \( x^2 y = V \) (since l = w = x). Then y = V / x². The cost function is 2A x² + 2B(2x y) [Wait, no. Wait, the sides: 2(lh) + 2(wh) = 2x y + 2x y = 4x y. So cost for sides is 2B*(4x y)/2? No, original cost for sides is 2B(lh + wh). Since l = w = x, that's 2B(x y + x y) = 2B(2x y) = 4B x y. So total cost C = 2A x² + 4B x y. Then with y = V/x², C = 2A x² + 4B x (V/x²) = 2A x² + 4B V / x. Then derivative dC/dx = 4A x - 4B V / x². Setting to zero: 4A x = 4B V / x² → A x³ = B V → x³ = B V / A → x = (B V / A)^(1/3). Then y = V / x² = V / (B V / A)^(2/3) = V / ( (B² V²)/(A²) )^(1/3) ) = V / ( B^(2/3) V^(2/3) / A^(2/3) ) ) = V * A^(2/3) / ( B^(2/3) V^(2/3) ) ) = A^(2/3) V^(1/3) / B^(2/3) = (A² V / B²)^(1/3). So that's consistent.

Therefore, the dimensions that minimize the cost are:

Length = Width = \( \left( \frac{B V}{A} \right)^{1/3} \)

Height = \( \left( \frac{A^2 V}{B^2} \right)^{1/3} \)

Alternatively, we can write the height as \( \frac{A}{B} \times \left( \frac{B V}{A} \right)^{1/3} \), but the first form is probably clearer.

Let me check if there's another way to express these. Let's see:

Let’s denote \( k = \left( \frac{B}{A} \right)^{1/3} \). Then \( \left( \frac{B V}{A} \right)^{1/3} = k V^{1/3} \). Then the height is \( \left( \frac{A^2 V}{B^2} \right)^{1/3} = \left( \frac{A^2}{B^2} V \right)^{1/3} = \left( \left( \frac{A}{B} \right)^2 V \right)^{1/3} = \left( \left( \frac{1}{k^3} \right)^2 V \right)^{1/3} = \left( \frac{V}{k^6} \right)^{1/3} = \frac{V^{1/3}}{k^2} \). But maybe that's not helpful.

Alternatively, let's express all dimensions in terms of V, A, B. The key is that length and width are equal, and height is proportional to (A² V)^(1/3)/B^(2/3). 

So the final answer should state the dimensions: length, width, height. Since the problem says "dimensions of the box", and typically length, width, height, but since length and width are equal, we can say length = width = (B V / A)^(1/3), height = (A² V / B²)^(1/3). 

Alternatively, we can write them using exponents:

Length = \( \left( \frac{B V}{A} \right)^{1/3} \)

Width = same as length, so \( \left( \frac{B V}{A} \right)^{1/3} \)

Height = \( \left( \frac{A^2 V}{B^2} \right)^{1/3} \)

Yes, that's correct. Let me confirm with an example. Suppose A = B. Then the cost for top/bottom and sides is the same. Then what happens? Let's see. If A = B, then length and width would be (B V / A)^(1/3) = V^(1/3), and height would be (A² V / B²)^(1/3) = (V)^(1/3). So all dimensions are equal, which makes sense: a cube, which is the minimal surface area for a given volume, and since all costs are the same, that's the minimal cost. That checks out. So when A = B, we get a cube, which is correct. So that's a good sanity check.

Another check: suppose B is very large, meaning sides are expensive. Then we want to minimize the area of the sides. The sides' area is 2(lh + wh). If B is large, we need to minimize (lh + wh). But volume is fixed. Let's see, with our solution, when B is large, (B V / A)^(1/3) would be large if B is large, but wait, no. Wait, if B increases, (B V / A)^(1/3) increases, so length and width increase, but height is (A² V / B²)^(1/3), which decreases as B increases. Let's see: if B is very large, then length and width are proportional to B^(1/3), height is proportional to B^(-2/3). Then the area of the sides is 2(lh + wh) = 2h(l + w) = 2h(2l) (since l = w) = 4hl. Let's compute hl: h l = (A² V / B²)^(1/3) * (B V / A)^(1/3) = (A² V * B V / A) / B² )^(1/3) = (A V² / B )^(1/3). So hl = (A V² / B)^(1/3). Then 4hl = 4 (A V² / B)^(1/3). As B increases, this term decreases, which is good because B is the cost per area for sides, so larger B means we want to minimize the area. So as B increases, the side area decreases, which aligns with intuition. That's a good check.

Similarly, if A is very large, meaning top and bottom are expensive. Then (B V / A)^(1/3) would be small (since A is large), so length and width are small, and height is (A² V / B²)^(1/3), which is large (since A is large). Then the area of top and bottom is 2lw = 2l². l is (B V / A)^(1/3), so l² = (B V / A)^(2/3), so 2l² = 2 (B² V² / A²)^(1/3). As A increases, this area decreases, which is good because A is expensive. So that also aligns with intuition.

Thus, the solution seems correct.
</think>

To minimize the cost of a closed rectangular box with fixed volume \( V \), we start by defining the dimensions: length \( l \), width \( w \), and height \( h \). The volume constraint is \( V = lwh \). The cost function \( C \) includes \( A \) cents per square foot for the top and bottom (area \( 2lw \)) and \( B \) cents per square foot for the sides (area \( 2(lh + wh) \)). Thus, the total cost is:

\[ C = 2Alw + 2B(lh + wh) \]

Using the volume constraint, we express \( h \) as \( h = \frac{V}{lw} \). Substituting \( h \) into the cost function gives:

\[ C(l, w) = 2Alw + 2B\left( \frac{V}{w} + \frac{V}{l} \right) \]

To minimize \( C \), we take partial derivatives with respect to \( l \) and \( w \), set them to zero, and solve. This leads to the conditions \( l = w \) (length equals width) and solving for \( l \) and \( h \). 

Let \( l = w = x \). Then \( h = \frac{V}{x^2} \). Substituting \( x \) into the cost function and minimizing, we find \( x = \left( \frac{B V}{A} \right)^{1/3} \). The height \( h \) is then:

\[ h = \left( \frac{A^2 V}{B^2} \right)^{1/3} \]

Thus, the dimensions that minimize the cost are:

Length = Width = \( \left( \frac{B V}{A} \right)^{1/3} \), Height = \( \left( \frac{A^2 V}{B^2} \right)^{1/3} \)

\[
\boxed{\text{Length} = \left( \frac{B V}{A} \right)^{1/3},\ \text{Width} = \left( \frac{B V}{A} \right)^{1/3},\ \text{Height} = \left( \frac{A^2 V}{B^2} \right)^{1/3}}
\]

## AI's Thinking (Attempted Solution Process)

The problem asks me to identify all transitive subgroups of S4 up to relabeling, and for each, give an example of a quartic polynomial over Q whose splitting field has that Galois group.

Let me solve this directly in the TUI without using any tools.

First, answer leak check: The problem statement doesn't contain any leaked answers or solutions. It's a clean problem statement.

Now let me solve.

Transitive subgroups of S4: A transitive subgroup of S4 is a subgroup that acts transitively on {1,2,3,4}. The transitive subgroups of S4 up to conjugacy are:

1. C4 (cyclic of order 4) - generated by a 4-cycle, e.g., ⟨(1234)⟩
2. V4 (Klein four-group, the normal one) - {e, (12)(34), (13)(24), (14)(23)} - this is transitive
3. D4 (dihedral of order 8) - the symmetry group of a square, e.g., ⟨(1234), (13)⟩
4. A4 (alternating group of order 12)
5. S4 (order 24)

Wait, I need to be careful. Let me list all transitive subgroups of S4 up to conjugacy.

The transitive subgroups of S4 are classified by their order. By orbit-stabilizer, |G| must be divisible by 4 (since the orbit has size 4). So |G| ∈ {4, 8, 12, 24}.

Order 4: Subgroups of order 4 that are transitive. These are either C4 (cyclic) or V4 (Klein four). 
- C4: ⟨(1234)⟩ is transitive. ✓
- V4: The normal Klein four-group {e, (12)(34), (13)(24), (14)(23)} is transitive. ✓
- Are there other V4 subgroups that are transitive? A V4 subgroup like {e, (12), (34), (12)(34)} is NOT transitive (orbits are {1,2} and {3,4}). So only the normal V4 is transitive.

Order 8: Subgroups of order 8 in S4. These are the Sylow 2-subgroups, all conjugate, isomorphic to D4. They are transitive. ✓

Order 12: A4 is the only subgroup of order 12 in S4 (it's the unique subgroup of index 2). It's transitive. ✓

Order 24: S4 itself. ✓

So there are exactly 5 transitive subgroups up to conjugacy: C4, V4, D4, A4, S4.

Now I need to give examples of quartic polynomials over Q with each Galois group.

1. **S4**: A generic irreducible quartic with discriminant not a square and whose cubic resolvent is irreducible. Example: x^4 - x - 1. Let me verify. The discriminant of x^4 + px + q is 256q^3 - 27p^4... wait, let me recall the formula. For x^4 + px + q, discriminant is 256q^3 - 27p^4. For x^4 - x - 1: p = -1, q = -1. Disc = 256(-1)^3 - 27(-1)^4 = -256 - 27 = -283. This is not a square, and it's prime (283 is prime). The cubic resolvent of x^4 + px + q is x^3 - 4qx + p^2... hmm, let me be more careful.

Actually, for the quartic x^4 + ax^3 + bx^2 + cx + d, the cubic resolvent depends on the form. Let me use a standard reference.

For x^4 + px^2 + qx + r (depressed quartic), the cubic resolvent is y^3 - py^2 - 4ry + (4pr - q^2).

For x^4 - x - 1 (so p=0, q=-1, r=-1): resolvent is y^3 - 0·y^2 - 4(-1)y + (4·0·(-1) - (-1)^2) = y^3 + 4y - 1.

Is y^3 + 4y - 1 irreducible over Q? By rational root theorem, possible roots are ±1. y=1: 1+4-1=4≠0. y=-1: -1-4-1=-6≠0. So irreducible. 

Discriminant = -283, not a square. So Galois group is S4. ✓

2. **A4**: Need irreducible quartic with square discriminant and irreducible cubic resolvent. 

Example: x^4 - 2x^3 + 2x^2 + 2x - 1... hmm, let me think of a cleaner one.

Actually, a classic example: the discriminant must be a perfect square. 

Let me try x^4 - 4x^2 + 1. Hmm, but this might not be irreducible. x^4 - 4x^2 + 1 = (x^2 - 2)^2 - 3 = (x^2 - 2 - √3)(x^2 - 2 + √3). Not irreducible over Q? Let me check: x^4 - 4x^2 + 1. Try x^2 = t: t^2 - 4t + 1 = 0, t = 2 ± √3. So x^2 = 2+√3 or x^2 = 2-√3. Not rational, so x^4 - 4x^2 + 1 is irreducible over Q? Wait, it could factor as two quadratics over Q: (x^2+ax+b)(x^2-ax+d) = x^4 + (b+d-a^2)x^2 + a(d-b)x + bd. We need b+d-a^2 = -4, a(d-b) = 0, bd = 1. If a=0: b+d = -4, bd = 1, so b,d are roots of t^2+4t+1=0, t = -2±√3. Not rational. If d=b: 2b-a^2 = -4, b^2 = 1, so b=±1. b=1: a^2 = 6, not rational. b=-1: a^2 = 2, not rational. So irreducible over Q. ✓

Discriminant of x^4 + px^2 + r (q=0): For x^4 - 4x^2 + 1, p=-4, r=1. The discriminant... Let me compute. The roots are ±√(2+√3), ±√(2-√3). 

Discriminant = ∏_{i<j}(r_i - r_j)^2. This is complex to compute directly. Let me use the formula for x^4 + px^2 + r: disc = 16r(p^2-4r)^2... no, let me look this up properly.

For f(x) = x^4 + px^2 + qx + r, discriminant = 256r^3 - 128p^2r^2 + 144pq^2r - 27q^4 + 16p^4r - 4p^3q^2.

For x^4 - 4x^2 + 1: p=-4, q=0, r=1.
Disc = 256(1) - 128(16)(1) + 0 - 0 + 16(256)(1) - 0
= 256 - 2048 + 4096
= 256 - 2048 + 4096 = 2304.

√2304 = 48. So discriminant = 48^2 = 2304. It's a perfect square! ✓

Cubic resolvent: y^3 - py^2 - 4ry + (4pr - q^2) = y^3 + 4y^2 - 4y + (-16 - 0) = y^3 + 4y^2 - 4y - 16.

Is this irreducible? Rational roots: ±1, ±2, ±4, ±8, ±16.
y=1: 1+4-4-16=-15≠0
y=-1: -1+4+4-16=-9≠0
y=2: 8+16-8-16=0. Yes! y=2 is a root.

So the cubic resolvent factors, meaning the Galois group is NOT A4 (it would be V4 or C4 or D4). Since the resolvent has a root, the Galois group is contained in D4. Since discriminant is a square, it's contained in A4 ∩ D4 = V4. So the Galois group is V4 (if the polynomial is irreducible, which it is). 

So x^4 - 4x^2 + 1 gives V4, not A4. Good, that's an example for V4!

Let me find an A4 example. I need an irreducible quartic with square discriminant and irreducible cubic resolvent.

Let me try x^4 - 2x^3 - 7x^2 + 8x + 12... this is getting complicated. Let me think more systematically.

Actually, a well-known example for A4: x^4 - 2x^3 + 2x^2 + 2x - 1. Hmm, let me try another approach.

Consider x^4 - 10x^2 + 1. p=-10, q=0, r=1.
Disc = 256 - 128(100) + 16(10000) = 256 - 12800 + 160000 = 147456. √147456 = 384. So disc = 384^2. Square! ✓

Resolvent: y^3 + 10y^2 - 4y - 40. Check y=2: 8+40-8-40=0. Root again. So this is also V4.

The issue is that for x^4 + px^2 + r (biquadratic-like), the resolvent always has a rational root because q=0 makes the resolvent y^3 - py^2 - 4ry + 4pr = y^3 - py^2 - 4ry + 4pr. Let me factor: if y = p/... hmm. Actually y^3 - py^2 - 4ry + 4pr. Try y = -4r/p... no. Let me just note that when q=0, the resolvent is y^3 - py^2 - 4ry + 4pr = (y-p)(y^2 - 4r). So it always factors! That's why biquadratic-type quartics never give A4.

So for A4, I need q ≠ 0. Let me find an example.

Let me try a different approach. I'll look for an irreducible quartic with square discriminant and irreducible resolvent.

Consider f(x) = x^4 - x^3 - 4x^2 + 4x + 1. Let me check if it's irreducible. Try rational roots ±1: f(1) = 1-1-4+4+1=1≠0, f(-1)=1+1-4-4+1=-5≠0. Could factor as (x^2+ax+b)(x^2+cx+d) with a+c=-1, b+d+ac=-4, ad+bc=4, bd=1. bd=1 so b=d=1 or b=d=-1.

If b=d=1: a+c=-1, 2+ac=-4 so ac=-6, a+c=-1. So a,c are roots of t^2+t-6=0, t=2 or t=-3. Then ad+bc = a+c = -1 ≠ 4. No.

If b=d=-1: a+c=-1, -2+ac=-4 so ac=-2, a+c=-1. t^2+t-2=0, t=1 or t=-2. ad+bc = -(a+c) = 1 ≠ 4. No.

If b=1,d=1: already tried. What about b and d not both equal? bd=1, so b=1,d=1 or b=-1,d=-1 (over integers). Over rationals, more options, but for irreducibility over Q we need to check all. Actually, if it factors as two quadratics over Q, by Gauss's lemma it factors over Z. So b,d ∈ Z with bd=1 means b=d=1 or b=d=-1. Both failed. So f is irreducible over Q. ✓

Now compute the discriminant. Let me convert to depressed form. f(x) = x^4 - x^3 - 4x^2 + 4x + 1. Substitute x = t + 1/4 to eliminate the cubic term. This is messy. Let me use the general discriminant formula for x^4 + ax^3 + bx^2 + cx + d.

The discriminant of a general quartic is quite complex. Let me use a different approach.

Actually, let me just use known examples from the literature.

Known examples:
- S4: x^4 - x - 1 (disc = -283, not square, resolvent irreducible) ✓
- A4: x^4 - 2x^3 + 2x^2 + 2x - 1 — let me verify this.

Hmm, actually let me try a cleaner approach. A classic A4 example is the minimal polynomial of a specific algebraic number.

Let me try f(x) = x^4 - 2x^3 - 7x^2 + 8x + 12. Hmm, f(-2) = 16+16-28-16+12 = 0. So -2 is a root. Not irreducible.

Let me try the approach of constructing an A4 extension. A4 is the Galois group of the splitting field of an irreducible quartic whose discriminant is a perfect square and whose cubic resolvent is irreducible.

A well-known example: x^4 - 2x^3 - 7x^2 + 8x + 12 doesn't work. Let me try x^4 - 2x^3 + 2x^2 + 2x - 1.

f(1) = 1-2+2+2-1 = 2 ≠ 0
f(-1) = 1+2+2-2-1 = 2 ≠ 0

Factor as (x^2+ax+b)(x^2+cx+d): a+c=-2, b+d+ac=2, ad+bc=2, bd=-1.
bd=-1: (b,d)=(1,-1) or (-1,1).

Case b=1, d=-1: a+c=-2, ac=2 (since 0+ac=2), ad+bc = -a+c = 2. So c-a=2, a+c=-2. Solving: c=0, a=-2. Check ac=0≠2. No.

Case b=-1, d=1: a+c=-2, ac=2 (since 0+ac=2), ad+bc = a-c = 2. So a-c=2, a+c=-2. a=0, c=-2. ac=0≠2. No.

So irreducible over Q. ✓

Now I need the discriminant. Let me use the formula. For f(x) = x^4 + ax^3 + bx^2 + cx + d, the discriminant is:

Δ = 256d^3 - 192a^2d^2 - 128b^2d^2 + 144a^2bd^2 - 27a^4d^2 + 144bc^2d - 6a^2c^2d - 80ab^2cd + 18a^3bcd + 16b^4d - 4a^2b^3d - 27c^4 + 18abc^3 - 4a^3c^3 - 4b^3c^2 + a^2b^2c^2

This is very messy. Let me use a computational approach in my head, or find a simpler example.

Actually, let me try a well-known clean example. The polynomial x^4 - 10x^2 + 1 has Galois group V4 as we showed. 

For A4, a standard example is x^4 - 2x^3 - 7x^2 + 8x + 12 — but that's reducible.

Let me try x^4 - 4x^3 + 2x^2 + 4x + 4. Hmm, this is getting complicated. Let me try yet another approach.

Actually, I recall that a good A4 example is x^4 - 2x^3 - 7x^2 + 8x + 12 is wrong. Let me think about what kind of quartic gives A4.

A4 extensions: The splitting field has degree 12 over Q. The quartic is irreducible (degree 4), discriminant is a square (so Galois group ⊂ A4), and the resolvent cubic is irreducible (so Galois group is not V4, hence A4).

Let me try f(x) = x^4 - 2x^3 - 7x^2 + 8x + 12. Wait I showed f(-2)=0. Let me try f(x) = x^4 - 2x^3 - 7x^2 + 8x - 12. Hmm, this is trial and error.

Let me try a more systematic approach. Consider the polynomial x^4 - 2x^3 + 2x^2 + 2x - 1 and compute its discriminant using the depressed quartic.

f(x) = x^4 - 2x^3 + 2x^2 + 2x - 1. Let x = t + 1/2 (since a=-2, we substitute x = t - a/4 = t + 1/2).

f(t + 1/2) = (t+1/2)^4 - 2(t+1/2)^3 + 2(t+1/2)^2 + 2(t+1/2) - 1

Let me expand:
(t+1/2)^4 = t^4 + 4t^3(1/2) + 6t^2(1/4) + 4t(1/8) + 1/16 = t^4 + 2t^3 + 3t^2/2 + t/2 + 1/16
-2(t+1/2)^3 = -2(t^3 + 3t^2/2 + 3t/4 + 1/8) = -2t^3 - 3t^2 - 3t/2 - 1/4
2(t+1/2)^2 = 2(t^2 + t + 1/4) = 2t^2 + 2t + 1/2
2(t+1/2) = 2t + 1
-1

Sum:
t^4: 1
t^3: 2 - 2 = 0 ✓
t^2: 3/2 - 3 + 2 = 1/2
t: 1/2 - 3/2 + 2 + 2 = 3
constant: 1/16 - 1/4 + 1/2 + 1 - 1 = 1/16 - 4/16 + 8/16 = 5/16

So depressed form: t^4 + (1/2)t^2 + 3t + 5/16.

Multiply by 16: 16t^4 + 8t^2 + 48t + 5. Or in standard form t^4 + pt^2 + qt + r with p=1/2, q=3, r=5/16.

Discriminant = 256r^3 - 128p^2r^2 + 144pq^2r - 27q^4 + 16p^4r - 4p^3q^2

= 256(5/16)^3 - 128(1/4)(5/16)^2 + 144(1/2)(9)(5/16) - 27(81) + 16(1/16)(5/16) - 4(1/8)(9)

= 256(125/4096) - 128(1/4)(25/256) + 144(1/2)(9)(5/16) - 2187 + 16(1/16)(5/16) - 4(1/8)(9)

= 125/16 - 128·25/1024 + 144·45/32 - 2187 + 5/16 - 9/2

= 125/16 - 25/8 + 6480/32 - 2187 + 5/16 - 9/2

= 125/16 - 50/16 + 3240/16 - 34992/16 + 5/16 - 72/16

= (125 - 50 + 3240 - 34992 + 5 - 72) / 16

= (125 - 50 + 3240 - 34992 + 5 - 72) / 16

= (130 - 50 + 3240 - 34992 - 72) / 16

Hmm, let me redo this more carefully.

125/16: keep
-25/8 = -50/16
6480/32 = 3240/16
-2187 = -34992/16
5/16: keep
-9/2 = -72/16

Sum = (125 - 50 + 3240 - 34992 + 5 - 72) / 16
= (125 + 5 + 3240 - 50 - 72 - 34992) / 16
= (3370 - 35114) / 16
= -31744 / 16
= -1984

So discriminant = -1984. Is this a perfect square? -1984 = -1 · 1984 = -1 · 64 · 31 = -64 · 31. √(-1984) is not rational. So this is NOT a square. So this polynomial doesn't give A4.

This trial and error is inefficient. Let me think of a known A4 example.

A well-known example of an A4 quartic is x^4 - 2x^3 - 7x^2 + 8x + 12 — no, that's reducible.

Let me try the polynomial whose roots generate an A4 extension. 

Actually, I recall that x^4 - 10x^2 + 1 gives V4, and a standard A4 example is something like x^4 - 2x^3 - 7x^2 + 8x + 12 is wrong...

Let me try a completely different approach. I'll use the fact that for the polynomial x^4 + ax^3 + bx^2 + cx + d, I can compute things more carefully with specific nice values.

Actually, let me just try x^4 - 2x^3 - 7x^2 + 8x + 12. Wait, I keep coming back to this. Let me check: f(-2) = 16 + 16 - 28 - 16 + 12 = 0. Yes, -2 is a root. So this is reducible.

How about x^4 - 2x^3 - 7x^2 + 8x - 12? f(2) = 16 - 16 - 28 + 16 - 12 = -24. f(-2) = 16 + 16 - 28 - 16 - 12 = -24. f(3) = 81 - 54 - 63 + 24 - 12 = -24. f(-3) = 81 + 54 - 63 - 24 - 12 = 36. f(1) = 1 - 2 - 7 + 8 - 12 = -12. f(-1) = 1 + 2 - 7 - 8 - 12 = -24. f(6) = 1296 - 432 - 252 + 48 - 12 = 648. Hmm, no rational roots. But could factor as quadratics.

This is getting tedious. Let me use a known result. 

A classic example: the minimal polynomial of 2cos(2π/13) has degree 6, not 4. 

Let me think about this differently. The A4 Galois group arises when we have an irreducible quartic with:
1. Square discriminant
2. Irreducible cubic resolvent

One approach: take a cubic with Galois group A3 (= C3), and adjoin a square root to get an A4 extension. But that's more complex.

Let me try the polynomial x^4 - 4x^3 - 4x^2 + 16x + 8. Hmm.

Actually, you know what, let me just try to use a well-documented example. I believe x^4 - 2x^3 - 7x^2 + 8x + 12 is NOT the right one. 

Let me try x^4 - 2x^3 - 7x^2 + 8x + 12... no. OK let me try a different tactic.

Consider the polynomial f(x) = x^4 - 2x^3 - 7x^2 + 8x + 12. This factors as (x+2)(x^3 - 4x^2 + x + 6) = (x+2)(x-3)(x^2 - x - 2) = (x+2)(x-3)(x-2)(x+1). So it splits completely! Definitely not what I want.

Let me try a systematic search. I want an irreducible quartic f(x) = x^4 + bx^2 + cx + d (depressed, a=0 for simplicity) with:
- Square discriminant
- Irreducible cubic resolvent y^3 - by^2 - 4dy + (4bd - c^2)

For the depressed quartic x^4 + bx^2 + cx + d:
Discriminant = 256d^3 - 128b^2d^2 + 144bc^2d - 27c^4 + 16b^4d - 4b^3c^2

Cubic resolvent: y^3 - by^2 - 4dy + (4bd - c^2)

I need the discriminant to be a perfect square and the resolvent to be irreducible.

Let me try b = 0: x^4 + cx + d.
Disc = 256d^3 - 27c^4.
Resolvent: y^3 - 4dy - c^2.

For x^4 - x - 1 (c=-1, d=-1): Disc = 256(-1) - 27(1) = -283. Not square. Resolvent: y^3 + 4y - 1, irreducible. → S4. ✓

For A4, I need Disc to be a square. With b=0: 256d^3 - 27c^4 = square. This is a Diophantine condition.

Let me try c = 2, d = -1: Disc = 256(-1) - 27(16) = -256 - 432 = -688. Not square.
c = 1, d = 1: Disc = 256 - 27 = 229. Not square.
c = 2, d = 1: Disc = 256 - 27·16 = 256 - 432 = -176. Not square.
c = 3, d = 1: Disc = 256 - 27·81 = 256 - 2187 = -1931. Not square.
c = 1, d = -2: Disc = 256(-8) - 27 = -2048 - 27 = -2075. Not square.
c = 4, d = 1: Disc = 256 - 27·256 = 256 - 6912 = -6656. Not square.
c = 4, d = -1: Disc = -256 - 27·256 = -256 - 6912 = -7168. Not square.
c = 2, d = 2: Disc = 256·8 - 27·16 = 2048 - 432 = 1616. √1616 ≈ 40.2. Not square.
c = 3, d = 2: Disc = 2048 - 27·81 = 2048 - 2187 = -139. Not square.
c = 1, d = 3: Disc = 256·27 - 27 = 27(256-1) = 27·255 = 6885. Not square.

This isn't working easily with b=0. Let me try b ≠ 0.

Let me try b = -4, c = 1, d = 1 (i.e., x^4 - 4x^2 + x + 1).
Disc = 256 - 128·16·1 + 144·(-4)·1·1 - 27 + 16·256·1 - 4·(-64)·1
= 256 - 2048 - 576 - 27 + 4096 + 256
= (256 + 4096 + 256) - (2048 + 576 + 27)
= 4608 - 2651 = 1957. Not square.

Let me try b = -4, c = 2, d = 1 (x^4 - 4x^2 + 2x + 1).
Disc = 256 - 2048 + 144·(-4)·4·1 - 27·16 + 4096 - 4·(-64)·4
= 256 - 2048 - 2304 - 432 + 4096 + 1024
= (256 + 4096 + 1024) - (2048 + 2304 + 432)
= 5376 - 4784 = 592. Not square.

Let me try b = -4, c = 4, d = 1 (x^4 - 4x^2 + 4x + 1).
Disc = 256 - 2048 + 144·(-4)·16·1 - 27·256 + 4096 - 4·(-64)·16
= 256 - 2048 - 9216 - 6912 + 4096 + 4096
= (256 + 4096 + 4096) - (2048 + 9216 + 6912)
= 8448 - 18176 = -9728. Not square.

This brute force isn't efficient. Let me think differently.

I know that for A4, a standard example in many textbooks is the polynomial x^4 - 2x^3 - 7x^2 + 8x + 12 — but that splits completely as I showed.

Another commonly cited example: x^4 - 10x^2 + 1 is V4, not A4.

Let me try the polynomial x^4 - 2x^3 - 7x^2 + 8x + 12... no. 

OK, let me try to construct one. Take a cubic field with Galois group C3 (i.e., discriminant is a square). The simplest is the cubic with discriminant 49 = 7^2. 

A cubic with discriminant 49: x^3 - x^2 - 2x + 1 has discriminant... For x^3 + ax^2 + bx + c, disc = a^2b^2 - 4b^3 - 4a^3c + 18abc - 27c^2.

x^3 - x^2 - 2x + 1: a=-1, b=-2, c=1.
Disc = 1·4 - 4·(-8) - 4·(-1)·1 + 18·(-1)·(-2)·1 - 27·1
= 4 + 32 + 4 + 36 - 27 = 49. ✓

So x^3 - x^2 - 2x + 1 has discriminant 49 = 7^2, and Galois group C3. Its roots are 2cos(2π/7), 2cos(4π/7), 2cos(6π/7).

Now, to get an A4 extension, I can take a quadratic extension of this C3 field and then... actually, the connection is:

A4 has a normal subgroup V4 with quotient C3. So an A4 extension is a degree-3 extension (the fixed field of V4) that is a C3 extension, and then a V4 extension on top.

Alternatively, I can look for the minimal polynomial of an element in an A4 extension. 

Actually, let me just try to find a specific example by a different method. Let me consider the polynomial:

f(x) = x^4 - 2x^3 - 7x^2 + 8x + 12 — no, this splits.

Let me try f(x) = x^4 - 2x^3 - 7x^2 + 8x - 12. Hmm, let me check irreducibility and compute discriminant.

Actually, this trial-and-error approach is too slow. Let me use a known example from the literature that I'm fairly confident about.

I recall that x^4 - 2x^3 - 7x^2 + 8x + 12 is wrong. But I think a valid A4 example is:

x^4 - 2x^3 - 7x^2 + 8x + 12... no.

Let me try yet another approach. Consider the polynomial x^4 - 4x^3 + 2x^2 + 4x - 2. Hmm.

Actually, let me try to use the resolvent cubic approach more carefully. I want:
1. f(x) = x^4 + bx^2 + cx + d irreducible over Q
2. Discriminant is a perfect square
3. Cubic resolvent y^3 - by^2 - 4dy + (4bd - c^2) is irreducible over Q

Let me try b = -1, c = 1, d = -1. f(x) = x^4 - x^2 + x - 1.
Check irreducibility: f(1) = 1-1+1-1=0. So x=1 is a root. Reducible.

b = -1, c = 1, d = 1. f(x) = x^4 - x^2 + x + 1.
f(1) = 1-1+1+1=2, f(-1) = 1-1-1+1=0. x=-1 is a root. Reducible.

b = -1, c = 2, d = 1. f(x) = x^4 - x^2 + 2x + 1.
f(1) = 1-1+2+1=3, f(-1) = 1-1-2+1=-1. No rational roots.
Factor as (x^2+ax+b)(x^2-ax+d): b+d-a^2=-1, a(d-b)=2, bd=1.
bd=1: b=d=1 or b=d=-1.
b=d=1: 2-a^2=-1, a^2=3. Not integer. But could be rational? a=±√3, not rational.
b=d=-1: -2-a^2=-1, a^2=-1. No.
So irreducible. ✓

Disc = 256 - 128·1·1 + 144·(-1)·4·1 - 27·16 + 16·1·1 - 4·(-1)·4
= 256 - 128 - 576 - 432 + 16 + 16
= (256 + 16 + 16) - (128 + 576 + 432)
= 288 - 1136 = -848. Not a square.

b = -1, c = 3, d = 1. f(x) = x^4 - x^2 + 3x + 1.
f(1) = 1-1+3+1=4, f(-1) = 1-1-3+1=-2. No rational roots.
Factor: b+d-a^2=-1, a(d-b)=3, bd=1.
b=d=1: a^2=3, no. b=d=-1: a^2=-1, no.
Irreducible. ✓

Disc = 256 - 128 + 144·(-1)·9·1 - 27·81 + 16 - 4·(-1)·9
= 256 - 128 - 1296 - 2187 + 16 + 36
= (256 + 16 + 36) - (128 + 1296 + 2187)
= 308 - 3611 = -3303. Not square.

b = -2, c = 1, d = 1. f(x) = x^4 - 2x^2 + x + 1.
f(1) = 1-2+1+1=1, f(-1) = 1-2-1+1=-1. No rational roots.
Factor: b+d-a^2=-2, a(d-b)=1, bd=1.
b=d=1: 2-a^2=-2, a^2=4, a=±2. a(d-b)=0≠1. No.
b=d=-1: -2-a^2=-2, a=0. a(d-b)=0≠1. No.
Irreducible. ✓

Disc = 256 - 128·4·1 + 144·(-2)·1·1 - 27 + 16·16·1 - 4·(-8)·1
= 256 - 512 - 288 - 27 + 256 + 32
= (256 + 256 + 32) - (512 + 288 + 27)
= 544 - 827 = -283. Not square (and this is -283, same as x^4-x-1 interestingly).

b = -2, c = 2, d = 1. f(x) = x^4 - 2x^2 + 2x + 1.
f(1) = 1-2+2+1=2, f(-1) = 1-2-2+1=-2. No rational roots.
Factor: b+d-a^2=-2, a(d-b)=2, bd=1.
b=d=1: a^2=4, a(d-b)=0≠2. No.
b=d=-1: a=0, a(d-b)=0≠2. No.
Irreducible. ✓

Disc = 256 - 512 + 144·(-2)·4·1 - 27·16 + 256 - 4·(-8)·4
= 256 - 512 - 1152 - 432 + 256 + 128
= (256+256+128) - (512+1152+432)
= 640 - 2096 = -1456. Not square.

b = -3, c = 1, d = 1. f(x) = x^4 - 3x^2 + x + 1.
f(1) = 1-3+1+1=0. Reducible.

b = -3, c = 2, d = 1. f(x) = x^4 - 3x^2 + 2x + 1.
f(1) = 1-3+2+1=1, f(-1) = 1-3-2+1=-3. No rational roots.
Factor: b+d-a^2=-3, a(d-b)=2, bd=1.
b=d=1: a^2=5, no. b=d=-1: -2-a^2=-3, a^2=1, a=±1. a(d-b)=0≠2. No.
Irreducible. ✓

Disc = 256 - 128·9 + 144·(-3)·4 - 27·16 + 16·81 - 4·(-27)·4
= 256 - 1152 - 1728 - 432 + 1296 + 432
= (256+1296+432) - (1152+1728+432)
= 1984 - 3312 = -1328. Not square.

b = -3, c = 3, d = 1. f(x) = x^4 - 3x^2 + 3x + 1.
f(1) = 1-3+3+1=2, f(-1) = 1-3-3+1=-4. No rational roots.
Factor: b+d-a^2=-3, a(d-b)=3, bd=1.
b=d=1: a^2=5, no. b=d=-1: a^2=1, a(d-b)=0≠3. No.
Irreducible. ✓

Disc = 256 - 1152 + 144·(-3)·9 - 27·81 + 1296 - 4·(-27)·9
= 256 - 1152 - 3888 - 2187 + 1296 + 972
= (256+1296+972) - (1152+3888+2187)
= 2524 - 7227 = -4703. Not square.

b = -4, c = 1, d = 2. f(x) = x^4 - 4x^2 + x + 2.
f(1) = 1-4+1+2=0. Reducible.

b = -4, c = 3, d = 2. f(x) = x^4 - 4x^2 + 3x + 2.
f(1) = 1-4+3+2=2, f(-1) = 1-4-3+2=-4. No rational roots.
f(2) = 16-16+6+2=8, f(-2) = 16-16-6+2=-4. No rational roots.
Factor: b+d-a^2=-4, a(d-b)=3, bd=2.
Options for (b,d): (1,2), (2,1), (-1,-2), (-2,-1).
(b,d)=(1,2): 3-a^2=-4, a^2=7. No.
(b,d)=(2,1): 3-a^2=-4, a^2=7. No.
(b,d)=(-1,-2): -3-a^2=-4, a^2=1, a=±1. a(d-b)=a(-2-(-1))=-a. Need -a=3, a=-3. But a^2=1≠9. No.
(b,d)=(-2,-1): -3-a^2=-4, a^2=1, a=±1. a(d-b)=a(-1-(-2))=a. Need a=3. But a^2=1. No.
Irreducible. ✓

Disc = 256·8 - 128·16·4 + 144·(-4)·9·2 - 27·81 + 16·256·2 - 4·(-64)·9
= 2048 - 8192 - 10368 - 2187 + 8192 + 2304
= (2048+8192+2304) - (8192+10368+2187)
= 12544 - 20747 = -8203. Not square.

This is really tedious. Let me try a completely different approach.

I know that the discriminant of the quartic x^4 + bx^2 + cx + d equals the discriminant of its resolvent cubic times something... actually, the discriminant of the quartic equals the discriminant of the resolvent cubic (up to sign? or exactly?).

Actually, the discriminant of the quartic f equals the discriminant of its resolvent cubic g. Let me verify: for x^4 - x - 1, disc = -283. Resolvent: y^3 + 4y - 1. Disc of y^3 + py + q is -4p^3 - 27q^2 = -4(64) - 27(1) = -256 - 27 = -283. ✓ 

So the discriminant of the quartic equals the discriminant of the resolvent cubic. 

For A4, I need the discriminant to be a perfect square. The discriminant of the resolvent cubic y^3 + py + q (depressed) is -4p^3 - 27q^2. For this to be a perfect square, I need -4p^3 - 27q^2 = k^2 for some integer k.

But wait, the resolvent also needs to be irreducible. An irreducible cubic with square discriminant has Galois group A3 = C3. So I need a cubic with Galois group C3, and then the corresponding quartic has Galois group A4 (if the quartic is irreducible).

So the strategy is: find an irreducible cubic g(y) with square discriminant (Galois group C3), then find the corresponding quartic f(x) that is irreducible.

The resolvent cubic of x^4 + bx^2 + cx + d is y^3 - by^2 - 4dy + (4bd - c^2).

So if I start with a cubic g(y) = y^3 + Py^2 + Qy + R with square discriminant, I need to find b, c, d such that:
-b = P, -4d = Q, 4bd - c^2 = R.

So b = -P, d = -Q/4, c^2 = 4bd - R = 4(-P)(-Q/4) - R = PQ - R.

For c to be rational, I need PQ - R to be a perfect square (of a rational number).

Let me use the C3 cubic x^3 - x^2 - 2x + 1 (disc = 49 = 7^2).
P = -1, Q = -2, R = 1.
b = -P = 1, d = -Q/4 = 1/2, c^2 = PQ - R = (-1)(-2) - 1 = 2 - 1 = 1. So c = ±1.

So the quartic is x^4 + x^2 ± x + 1/2. To clear denominators, multiply by 2: 2x^4 + 2x^2 ± 2x + 1. Hmm, but this has leading coefficient 2. Let me instead use 2f(x) = 2x^4 + 2x^2 + 2x + 1 (taking c=1).

Wait, but I need a monic polynomial with integer coefficients. Let me adjust. The quartic is x^4 + x^2 + x + 1/2. To make it monic with integer coefficients, I can substitute x = u/√2 or something... that changes the field.

Actually, let me just use 2x^4 + 2x^2 + 2x + 1. This is not monic, but its splitting field is the same as that of x^4 + x^2 + x + 1/2 (just scaled). Actually no, the roots of 2x^4 + 2x^2 + 2x + 1 are the same as the roots of x^4 + x^2 + x + 1/2. The splitting field is the same. And the Galois group is the same.

But the problem asks for F(X) ∈ Q[X], so non-monic is fine! Let me use F(x) = 2x^4 + 2x^2 + 2x + 1.

Wait, but I should double-check that this quartic is irreducible over Q. 2x^4 + 2x^2 + 2x + 1. By rational root theorem, possible roots are ±1, ±1/2. 
f(1) = 2+2+2+1=7, f(-1)=2+2-2+1=3, f(1/2)=2/16+2/4+1+1=1/8+1/2+2=21/8, f(-1/2)=1/8+1/2-1+1=5/8. No rational roots.

Could it factor as two quadratics over Q? 2x^4 + 2x^2 + 2x + 1 = (2x^2 + ax + b)(x^2 + cx + d) or (x^2 + ax + b)(2x^2 + cx + d).
Case 1: (2x^2 + ax + b)(x^2 + cx + d) = 2x^4 + (2c+a)x^3 + (2d+ac+b)x^2 + (ad+bc)x + bd.
Need: 2c+a=0, 2d+ac+b=2, ad+bc=2, bd=1.
From first: a = -2c. 
bd=1: (b,d) = (1,1) or (-1,-1).
(b,d)=(1,1): 2+c(-2c)+1=2 → 3-2c^2=2 → c^2=1/2. Not rational.
(b,d)=(-1,-1): -2-2c^2-1=2 → -3-2c^2=2 → c^2=-5/2. No.

Case 2: (x^2 + ax + b)(2x^2 + cx + d) = 2x^4 + (c+2a)x^3 + (d+ac+2b)x^2 + (ad+bc)x + bd.
Need: c+2a=0, d+ac+2b=2, ad+bc=2, bd=1.
c=-2a. bd=1: (b,d)=(1,1) or (-1,-1).
(b,d)=(1,1): 1+(-2a)a+2=2 → 3-2a^2=2 → a^2=1/2. No.
(b,d)=(-1,-1): -1+2a^2-2=2 → 2a^2=5 → a^2=5/2. No.

So 2x^4 + 2x^2 + 2x + 1 is irreducible over Q. ✓

And its discriminant is 49 (same as the resolvent cubic's discriminant), which is 7^2, a perfect square. ✓

And the resolvent cubic is x^3 - x^2 - 2x + 1, which is irreducible (no rational roots: f(1)=-1, f(-1)=1, f(7)=... well, by rational root theorem, possible roots are ±1, and neither works). ✓

So the Galois group is A4. 

So F(x) = 2x^4 + 2x^2 + 2x + 1 has Galois group A4.

Actually wait, let me double-check the correspondence. The resolvent of x^4 + x^2 + x + 1/2 is y^3 - y^2 - 2y + (4·1·1/2 - 1) = y^3 - y^2 - 2y + 1. Yes, that's the C3 cubic. ✓

Great, so A4 example: 2x^4 + 2x^2 + 2x + 1. Or equivalently, I could write it as x^4 + x^2 + x + 1/2, but integer coefficients are nicer. Actually, let me also check: is the discriminant of 2x^4 + 2x^2 + 2x + 1 the same as that of x^4 + x^2 + x + 1/2? The discriminant of a polynomial changes when you scale. If g(x) = a·f(x), the roots are the same, so the discriminant (as ∏(r_i - r_j)^2) is the same. But the "polynomial discriminant" (resultant of f and f') scales. Since we're talking about the splitting field and Galois group, what matters is whether the discriminant is a square in Q, and scaling by a constant doesn't change that (the discriminant of the number field, i.e., the product of differences of roots, is the same). So yes, the Galois group is A4. ✓

Now let me also handle C4 and D4.

3. **D4**: Need an irreducible quartic with non-square discriminant and reducible (but not fully split) cubic resolvent. The Galois group is D4 when the resolvent has exactly one rational root and the discriminant is not a square.

Example: x^4 - 2. This is irreducible (Eisenstein at p=2). Its roots are ±√2, ±i√2. The splitting field is Q(√2, i), which has degree 4 over Q. The Galois group has order 4. 

Wait, what's the Galois group of x^4 - 2? The splitting field is Q(2^{1/4}, i). Actually, the roots are ±α, ±iα where α = 2^{1/4}. The splitting field is Q(α, i). [Q(α):Q] = 4, [Q(α,i):Q(α)] = 2 (since i ∉ Q(α) ⊂ R). So the splitting field has degree 8 over Q, and the Galois group has order 8. 

The Galois group of x^4 - 2 is D4 (dihedral of order 8). Let me verify: the discriminant of x^4 - 2 is... For x^4 + c (b=0, c=0, d=-2 in the form x^4 + bx^2 + cx + d, but actually x^4 - 2 has p=0, q=0, r=-2). Disc = 256(-2)^3 = 256(-8) = -2048 = -2^11. Not a square. ✓

Resolvent: y^3 - 0·y^2 - 4(-2)y + 0 = y^3 + 8y = y(y^2 + 8). This has a rational root y=0. ✓

So the resolvent has exactly one rational root (y=0, and y^2+8 has no rational roots). The discriminant is not a square. So the Galois group is D4. ✓

4. **C4**: Need an irreducible quartic whose Galois group is cyclic of order 4. This happens when the discriminant is not a square, the resolvent has a rational root, and... actually, let me think about this more carefully.

The Galois group of an irreducible quartic is determined by:
- Is the resolvent cubic irreducible? If yes, Gal = S4 or A4 (depending on whether disc is square).
- If the resolvent has exactly one root, Gal = D4 or C4 (depending on whether disc is square).
- If the resolvent splits completely, Gal = V4 (or the Klein four-group, if disc is square) or... well, if disc is not square and resolvent splits, it's a different V4 (not transitive? no...).

Wait, let me be more careful. The standard classification:

For an irreducible quartic f over Q with discriminant Δ and resolvent cubic g:
- g irreducible, Δ not square → S4
- g irreducible, Δ square → A4
- g has exactly one root in Q, Δ not square → D4
- g has exactly one root in Q, Δ square → C4
- g splits completely over Q, Δ not square → V4 (the non-normal Klein four, i.e., {e, (12), (34), (12)(34)} — wait, this isn't transitive!)

Hmm, wait. If g splits completely and Δ is not a square, the Galois group is isomorphic to V4 but it's the non-transitive V4 = {e, (12), (34), (12)(34)}? No, that can't be right since f is irreducible, so the Galois group must be transitive.

Let me reconsider. The transitive subgroups of S4 are C4, V4 (normal), D4, A4, S4. The V4 that is transitive is the normal one {e, (12)(34), (13)(24), (14)(23)}.

The classification should be:
- g irreducible, Δ not square → S4
- g irreducible, Δ square → A4
- g has exactly one root in Q, Δ not square → D4
- g has exactly one root in Q, Δ square → C4
- g splits completely, Δ square → V4 (normal Klein four)
- g splits completely, Δ not square → ? 

If g splits completely and Δ is not a square, then the Galois group is a transitive subgroup of S4 that is contained in D4 (since g has a root) but not in A4 (since Δ is not square), and the Galois group has order 4 (since g splits, the splitting field degree divides 4·something...). Actually, if g splits completely, the splitting field of f has degree dividing 4 (since the resolvent splitting completely means the Galois group is a subgroup of V4... no).

Let me think again. The resolvent cubic g has the property that the splitting field of g is the fixed field of G ∩ V4 (where V4 is the normal Klein four in S4). More precisely, the splitting field of g is the subfield of the splitting field of f fixed by G ∩ V4.

If g splits completely, then G ∩ V4 = G, meaning G ⊂ V4. Since G is transitive and G ⊂ V4 (the normal Klein four), G = V4. And V4 ⊂ A4, so Δ is a square. So if g splits completely, Δ must be a square, and G = V4.

So the case "g splits completely, Δ not square" cannot occur for an irreducible quartic. Good.

So the classification is:
- g irreducible, Δ not square → S4
- g irreducible, Δ square → A4
- g has exactly one root in Q, Δ not square → D4
- g has exactly one root in Q, Δ square → C4
- g splits completely → V4 (and Δ is automatically square)

This gives exactly 5 cases, matching the 5 transitive subgroups. ✓

So for C4, I need an irreducible quartic with:
- Discriminant is a perfect square
- Resolvent cubic has exactly one rational root

Let me find such an example. 

Using the same approach as for A4: I need a reducible cubic g(y) with square discriminant, where g has exactly one rational root and an irreducible quadratic factor. And then the corresponding quartic is irreducible.

Let g(y) = (y - r)(y^2 + sy + t) where the quadratic is irreducible over Q. The discriminant of g is the discriminant of the quadratic factor times (stuff)... actually, disc(g) = disc(quadratic) · (resultant stuff). Hmm, this is more complex.

Actually, let me think about it differently. I need the resolvent to have exactly one rational root and the discriminant (of the quartic = discriminant of the resolvent) to be a perfect square.

Let me try to construct this. Take the resolvent g(y) = y^3 - by^2 - 4dy + (4bd - c^2) with one rational root r. Then g(y) = (y-r)(y^2 + (r-b)y + ...). The discriminant of g equals the discriminant of the quartic.

For the discriminant to be a square, I need disc(g) = square. If g = (y-r)h(y) where h is an irreducible quadratic, then disc(g) = disc(h) · [r and roots of h stuff]. Actually, disc(g) = disc(h) · ∏(r - α_i)^2 where α_i are roots of h... no, that's not right either.

The discriminant of a cubic g(y) = (y-r)(y^2+sy+t) is:
disc(g) = disc(y^2+sy+t) · (r^2 + sr + t)^2

Wait, let me think. If g(y) = (y-r)q(y) where q(y) = y^2 + sy + t, then:
disc(g) = ∏_{i<j}(β_i - β_j)^2 where β_1 = r, β_2, β_3 are roots of q.
= (r - β_2)^2(r - β_3)^2(β_2 - β_3)^2
= [(r - β_2)(r - β_3)]^2 · (β_2 - β_3)^2
= q(r)^2 · disc(q)

So disc(g) = q(r)^2 · disc(q). For this to be a perfect square, I need disc(q) to be a perfect square. But if disc(q) is a perfect square, then q has rational roots, contradicting that q is irreducible. 

Hmm, so this means: if g has exactly one rational root and an irreducible quadratic factor, then disc(g) = q(r)^2 · disc(q), and disc(q) < 0 (if q has no real roots) or disc(q) > 0 but not a perfect square (if q has real but irrational roots). In either case, disc(g) is not a perfect square (since disc(q) is not a square, and q(r)^2 is a square, so disc(g) = square × non-square = non-square).

Wait, but that would mean C4 is impossible! That can't be right. Let me re-examine.

Hmm, actually disc(q) could be negative. If disc(q) < 0, then disc(g) = q(r)^2 · disc(q) < 0, which is certainly not a perfect square (in Q). If disc(q) > 0 but not a perfect square, then disc(g) = q(r)^2 · disc(q) is not a perfect square either.

So it seems like if the resolvent has exactly one rational root, the discriminant cannot be a perfect square. But that would mean C4 never occurs as a Galois group of a quartic, which contradicts what I know.

Wait, I think I'm confusing myself. Let me reconsider. The discriminant of the quartic equals the discriminant of the resolvent cubic. But for C4, the discriminant should be a square (since C4 is not contained in A4... wait, is C4 contained in A4?

C4 = ⟨(1234)⟩ = {e, (1234), (13)(24), (1432)}. The 4-cycle (1234) is an odd permutation. So C4 is NOT contained in A4. So for C4, the discriminant should NOT be a square.

Let me re-examine the classification. I think I had it wrong. Let me redo it.

The key theorem: Let f be an irreducible quartic over Q, G its Galois group (as a transitive subgroup of S4), g its cubic resolvent, and Δ the discriminant.

- G ⊂ A4 iff Δ is a square.
- The splitting field of g is the fixed field of G ∩ V4 (where V4 = {e, (12)(34), (13)(24), (14)(23)} is the normal Klein four).
- g is irreducible iff G acts transitively on the three "pairings" {{1,2},{3,4}}, {{1,3},{2,4}}, {{1,4},{2,3}}, which happens iff G is not contained in any conjugate of D4... actually, iff G/V4∩G acts transitively, which happens when [G : G∩V4] = 3, i.e., when |G|/|G∩V4| = 3.

Let me think about this more carefully for each group:

**S4** (order 24): G∩V4 = V4 (order 4). [G:G∩V4] = 6. The action on 3 pairings: S4/V4 ≅ S3, which acts transitively on 3 elements. So g is irreducible. Δ not square. ✓

**A4** (order 12): G∩V4 = V4 (order 4). [G:G∩V4] = 3. A4/V4 ≅ C3, acts transitively. g irreducible. Δ square. ✓

**D4** (order 8): D4 contains V4 (the normal Klein four is contained in D4). So G∩V4 = V4, [G:G∩V4] = 2. D4/V4 ≅ C2, which has orbits of size 1 and 2 on the 3 pairings. So g has exactly one root. Δ not square (D4 ⊄ A4). ✓

**C4** (order 4): C4 = {e, (1234), (13)(24), (1432)}. G∩V4 = {e, (13)(24)} (order 2). [G:G∩V4] = 2. So g has exactly one root (orbit structure 1+2). Δ: C4 contains (1234) which is odd, so C4 ⊄ A4, Δ not square. ✓

**V4** (normal, order 4): G∩V4 = V4. [G:G∩V4] = 1. g splits completely. V4 ⊂ A4, Δ square. ✓

So the correct classification is:
- g irreducible, Δ not square → S4
- g irreducible, Δ square → A4
- g has exactly one root, Δ not square → D4 or C4
- g splits completely (Δ square) → V4

So D4 and C4 both have g with exactly one root and Δ not a square. How to distinguish them?

The distinction is: D4 has order 8, C4 has order 4. The splitting field of f has degree |G| over Q. So:
- If [splitting field : Q] = 8, it's D4.
- If [splitting field : Q] = 4, it's C4.

Alternatively, there's a criterion: G = C4 iff the splitting field of f equals Q(α) for any root α of f (i.e., the splitting field has degree 4 = [Q(α):Q]). G = D4 iff the splitting field is strictly larger than Q(α).

Another criterion: Let r be the rational root of the resolvent g. Then G = C4 iff the discriminant of the quadratic factor of g (after dividing out (y-r)) is... hmm, actually there's a cleaner criterion.

Actually, I recall the criterion involves checking whether a certain element is a square. Let me think...

When g has exactly one rational root r, we can write g(y) = (y-r)(y^2+sy+t). The splitting field of g is Q(√(s^2-4t)) (adjoining the root of the quadratic). The splitting field of f contains the splitting field of g. 

For D4: |G| = 8, and the splitting field of g has degree 2 over Q (since g has one rational root and one irreducible quadratic). The fixed field of G∩V4 has degree [G:G∩V4] = 2 over Q, which matches.

For C4: |G| = 4, G∩V4 has order 2, [G:G∩V4] = 2. The splitting field of g also has degree 2 over Q.

So both have the same resolvent behavior. The difference is in the degree of the splitting field.

A practical criterion: G = C4 iff Δ · (s^2 - 4t) is a square in Q, where s^2 - 4t is the discriminant of the quadratic factor of g. Wait, I don't think that's exactly right. Let me think more carefully.

Actually, the standard criterion is: Let r be the rational root of the resolvent, and let h(y) = g(y)/(y-r) = y^2 + sy + t. Then:
- G = D4 if the splitting field of f is a degree-2 extension of the splitting field of g.
- G = C4 if the splitting field of f equals the splitting field of g (both degree 4 over Q... wait, no).

Hmm, let me think about this differently. 

For C4: The splitting field has degree 4. Q(α) has degree 4 (f is irreducible). So the splitting field = Q(α), meaning all roots are in Q(α). The resolvent has one rational root r, and the quadratic factor has roots that are in Q(α) (since the splitting field of g is contained in the splitting field of f = Q(α), which has degree 4, and the splitting field of g has degree 2).

For D4: The splitting field has degree 8. Q(α) has degree 4, and the splitting field is a degree-2 extension of Q(α).

The criterion to distinguish: Factor f over Q(√(disc(h))) where h is the quadratic factor of g. If f remains irreducible, it's D4. If f factors, it's C4. But this is hard to check in general.

A simpler criterion I recall: G = C4 iff Δ_f / disc(h) is a square in Q, where h is the irreducible quadratic factor of the resolvent. Wait, Δ_f = disc(g) = q(r)^2 · disc(h) where q is the quadratic factor. So Δ_f / disc(h) = q(r)^2, which is always a square! So this criterion doesn't distinguish.

Hmm. Let me think again. 

Actually, I think the criterion is different. Let me look at it from the perspective of the splitting field.

For D4: The splitting field K has degree 8. K contains Q(α) (degree 4) and Q(√Δ) (degree 2, since Δ is not a square). The resolvent root r gives a degree-2 subextension Q(√(disc(h))).

For C4: The splitting field K has degree 4. K = Q(α). K contains Q(√Δ) (degree 2). But Δ is not a square, so Q(√Δ) is a degree-2 subfield of Q(α). Also, the resolvent's quadratic factor splits over K, so Q(√(disc(h))) ⊂ K.

In the C4 case, Q(√Δ) = Q(√(disc(h))) (both are the unique degree-2 subfield of K = Q(α), since C4 has a unique subgroup of index 2).

In the D4 case, Q(√Δ) and Q(√(disc(h))) may or may not be equal.

So the criterion is: G = C4 iff Q(√Δ) = Q(√(disc(h))), i.e., Δ · disc(h) is a square (up to sign, or more precisely, Δ and disc(h) differ by a square factor).

Since Δ = disc(g) = h(r)^2 · disc(h), we have Δ / disc(h) = h(r)^2, which is always a square. So Δ and disc(h) always differ by a square factor! This means Q(√Δ) = Q(√(disc(h))) always holds.

But that would mean C4 and D4 can't be distinguished this way, which contradicts what I know. Let me re-examine.

Wait, I think the issue is that Δ could be negative. If Δ < 0 and disc(h) < 0, then Q(√Δ) = Q(√(disc(h))) iff Δ/disc(h) is a square, which it is (h(r)^2). But if Δ < 0 and disc(h) > 0, then Q(√Δ) ≠ Q(√(disc(h))) (one is real, one is imaginary). In that case, it's D4.

So the criterion is: G = C4 iff Δ and disc(h) have the same sign (both positive or both negative), and G = D4 iff they have opposite signs.

Hmm, but that's not quite right either. Let me think about specific cases.

For x^4 - 2 (D4): Δ = -2048 < 0. Resolvent: y^3 + 8y = y(y^2+8). Quadratic factor: y^2 + 8, disc = -32 < 0. Same sign (both negative). But this is D4, not C4. So my criterion is wrong.

Let me reconsider. Maybe the criterion is more subtle.

Actually, I think the correct criterion involves factoring f over the field Q(√(disc(h))). Let me think about this more carefully.

Actually, you know what, let me just find explicit examples for C4 and verify them directly.

A classic C4 example: x^4 + 1. Wait, is x^4 + 1 irreducible? x^4 + 1 = (x^2 + √2x + 1)(x^2 - √2x + 1) over R, but over Q? By the factorization check: (x^2+ax+b)(x^2-ax+d) with b+d-a^2=0, a(d-b)=0, bd=1. If a=0: b+d=0, bd=1, so b=-d, -d^2=1, no real solution. If d=b: 2b-a^2=0, b^2=1, b=±1. b=1: a^2=2, no. b=-1: a^2=-2, no. So x^4+1 is irreducible over Q. ✓

The roots of x^4+1 are the primitive 8th roots of unity: ζ_8, ζ_8^3, ζ_8^5, ζ_8^7 where ζ_8 = e^{2πi/8}. The splitting field is Q(ζ_8) = Q(√2, i). Wait, Q(ζ_8) = Q(e^{πi/4}) = Q(√2/2 + i√2/2). Actually, ζ_8 = (1+i)/√2, so Q(ζ_8) = Q(√2, i). This has degree 4 over Q (since Q(√2) has degree 2, and i ∉ Q(√2), so [Q(√2,i):Q] = 4).

The Galois group Gal(Q(ζ_8)/Q) ≅ (Z/8Z)^× = {1,3,5,7} ≅ C2 × C2 = V4. So x^4+1 has Galois group V4, not C4!

OK so x^4+1 gives V4. Let me check: the discriminant of x^4+1. Roots are ζ_8, ζ_8^3, ζ_8^5, ζ_8^7. 

Actually, for x^4 + 1 = x^4 + 0x^2 + 0x + 1, p=0, q=0, r=1. Disc = 256(1) - 0 - 0 - 0 + 0 - 0 = 256 = 16^2. Square! ✓

Resolvent: y^3 - 0 - 4y + 0 = y^3 - 4y = y(y-2)(y+2). Splits completely! ✓

So x^4+1 has Galois group V4. ✓ (This is another V4 example, but we already have x^4 - 4x^2 + 1.)

Now for C4. I need an irreducible quartic with Galois group C4. 

A cyclic quartic extension: Q(ζ_5) has Galois group C4 over Q (since (Z/5Z)^× ≅ C4). The minimal polynomial of ζ_5 is x^4 + x^3 + x^2 + x + 1 (the 5th cyclotomic polynomial). This is irreducible over Q (it's cyclotomic). The splitting field is Q(ζ_5), which has degree 4 over Q, and Galois group C4. ✓

Let me verify: x^4 + x^3 + x^2 + x + 1. 
- Irreducible: yes, it's the 5th cyclotomic polynomial, irreducible over Q. ✓
- Galois group: Gal(Q(ζ_5)/Q) ≅ (Z/5Z)^× ≅ C4. ✓
- Discriminant: The discriminant of x^4 + x^3 + x^2 + x + 1 is 5^3 = 125 (known formula for cyclotomic polynomials: disc(Φ_p) = p^{p-2} for prime p, so disc(Φ_5) = 5^3 = 125). 125 is not a perfect square. ✓ (C4 ⊄ A4, so disc should not be square.)
- Resolvent: Let me compute. Depressed form: x = t - 1/4. 

Actually, let me just use the general resolvent for x^4 + ax^3 + bx^2 + cx + d. The resolvent cubic is:

For x^4 + ax^3 + bx^2 + cx + d, the resolvent is y^3 - by^2 + (ac - 4d)y + (4bd - a^2d - c^2).

For x^4 + x^3 + x^2 + x + 1: a=1, b=1, c=1, d=1.
Resolvent: y^3 - y^2 + (1-4)y + (4-1-1) = y^3 - y^2 - 3y + 2.

Factor: try y=1: 1-1-3+2=-1≠0. y=-1: -1-1+3+2=3≠0. y=2: 8-4-6+2=0. ✓

So y=2 is a root. Factor: (y-2)(y^2+y-1). The quadratic y^2+y-1 has discriminant 1+4=5, not a square, so irreducible. ✓

So the resolvent has exactly one rational root, and the discriminant (125) is not a square. This is consistent with C4 or D4. Since the splitting field has degree 4 (= [Q(ζ_5):Q]), it's C4. ✓

So C4 example: x^4 + x^3 + x^2 + x + 1 (the 5th cyclotomic polynomial). ✓

Now let me also double-check the D4 example. x^4 - 2:
- Irreducible: Eisenstein at p=2. ✓
- Splitting field: Q(2^{1/4}, i), degree 8. ✓
- Galois group: D4 (order 8). ✓
- Discriminant: -2048, not a square. ✓
- Resolvent: y^3 + 8y = y(y^2+8), one rational root y=0. ✓

And V4 example: x^4 - 4x^2 + 1:
- Irreducible: shown above. ✓
- Discriminant: 2304 = 48^2, square. ✓
- Resolvent: y^3 + 4y^2 - 4y - 16 = (y-2)(y^2+6y+8) = (y-2)(y+2)(y+4). Splits completely! ✓
- Galois group: V4. ✓

Wait, let me recheck the resolvent. For x^4 - 4x^2 + 1: a=0, b=-4, c=0, d=1.
Resolvent: y^3 - (-4)y^2 + (0-4)y + (4(-4)(1) - 0 - 0) = y^3 + 4y^2 - 4y - 16.

y=2: 8+16-8-16=0. ✓ Factor: (y-2)(y^2+6y+8) = (y-2)(y+2)(y+4). Yes, splits completely. ✓

So V4 example: x^4 - 4x^2 + 1. ✓

And S4 example: x^4 - x - 1:
- Irreducible: no rational roots (±1 don't work: f(1)=-1, f(-1)=1), and can't factor as quadratics (shown implicitly). Actually let me verify: (x^2+ax+b)(x^2-ax+d) with b+d-a^2=0, a(d-b)=-1, bd=-1. bd=-1: (b,d)=(1,-1) or (-1,1). (b,d)=(1,-1): 0-a^2=0, a=0, a(d-b)=0≠-1. No. (b,d)=(-1,1): 0-a^2=0, a=0, a(d-b)=0≠-1. No. So irreducible. ✓
- Discriminant: -283, not a square. ✓
- Resolvent: y^3 + 4y - 1, irreducible (no rational roots). ✓
- Galois group: S4. ✓

Now let me also verify the A4 example more carefully. F(x) = 2x^4 + 2x^2 + 2x + 1.
- Irreducible: shown above. ✓
- Discriminant: should be 49 = 7^2. But wait, I need to be careful. The discriminant of 2x^4 + 2x^2 + 2x + 1 as a polynomial (in the sense of resultant) is different from the discriminant of x^4 + x^2 + x + 1/2. Let me think about what "discriminant" means here.

The discriminant of a polynomial f(x) = a_n x^n + ... is a_n^{2n-2} ∏(r_i - r_j)^2. For the monic polynomial x^4 + x^2 + x + 1/2, the discriminant is ∏(r_i - r_j)^2. For 2x^4 + 2x^2 + 2x + 1 = 2(x^4 + x^2 + x + 1/2), the polynomial discriminant is 2^{2·4-2} · ∏(r_i - r_j)^2 = 2^6 · disc(monic version).

But what matters for the Galois group is whether the discriminant is a square in Q. The polynomial discriminant of 2x^4 + 2x^2 + 2x + 1 is 64 · 49 = 3136 = 56^2. Still a square! ✓

Actually, more precisely, the discriminant of the polynomial (as defined by (-1)^{n(n-1)/2} a_n^{-1} Res(f, f')) is the same as ∏(r_i - r_j)^2 for monic polynomials, and for non-monic it's a_n^{2n-2} ∏(r_i - r_j)^2. 

For the monic version x^4 + x^2 + x + 1/2: disc = 49 (I computed this as the discriminant of the resolvent cubic, which equals the discriminant of the quartic). 

For 2x^4 + 2x^2 + 2x + 1: disc = 2^6 · 49 = 64 · 49 = 3136 = 56^2. Square! ✓

And the resolvent cubic of 2x^4 + 2x^2 + 2x + 1: For a non-monic polynomial, the resolvent is a bit different. Actually, the resolvent cubic is defined for the monic polynomial. Since 2x^4 + 2x^2 + 2x + 1 has the same roots as x^4 + x^2 + x + 1/2, the resolvent is the same: y^3 - y^2 - 2y + 1, which is irreducible. ✓

So A4 example: 2x^4 + 2x^2 + 2x + 1. ✓

Actually, let me also provide a cleaner A4 example if possible. Let me see if I can find one with integer coefficients that's monic.

From the construction: I need b, c, d integers (or rationals) with the resolvent y^3 - by^2 - 4dy + (4bd - c^2) being an irreducible cubic with square discriminant.

I used the C3 cubic y^3 - y^2 - 2y + 1 (disc = 49). This gives b=1, d=1/2, c^2=1. So c=1, but d=1/2 is not an integer. 

To get integer coefficients, I could try other C3 cubics. Let me try the cubic y^3 - 3y^2 - 6y + 8 (just trying random ones). Actually, let me use a different C3 cubic.

C3 cubics with square discriminant: these are exactly the irreducible cubics whose discriminant is a perfect square. The simplest ones come from the minimal polynomials of 2cos(2π/n) for appropriate n.

For n=7: 2cos(2π/7) has minimal polynomial x^3 + x^2 - 2x - 1, with discriminant 49. (This is the same cubic, just with a sign change on the x^2 term... let me check: x^3 + x^2 - 2x - 1. Disc = 1·4 - 4(-8) - 4·1·(-1) + 18·1·(-2)·(-1) - 27·1 = 4+32+4+36-27 = 49. ✓)

For this cubic: P=1, Q=-2, R=-1. b=-P=-1, d=-Q/4=1/2, c^2=PQ-R=(1)(-2)-(-1)=-2+1=-1. Negative! c is not real. So this doesn't work.

Let me try n=9: 2cos(2π/9) has minimal polynomial x^3 - 3x + 1, discriminant = -4(-3)^3 - 27(1)^2 = 108 - 27 = 81 = 9^2. ✓

P=0, Q=-3, R=1. b=0, d=3/4, c^2 = 0·(-3) - 1 = -1. Negative. Doesn't work.

Let me try n=13: 2cos(2π/13) has degree 6, not 3. 

n=14: 2cos(2π/14) = 2cos(π/7) has minimal polynomial... cos(π/7) is related to the 7th roots. Actually, 2cos(π/7) has minimal polynomial x^3 - x^2 - 2x + 1 (same as before, since cos(π/7) = -cos(6π/7) = -cos(8π/7)... hmm, this is getting complicated).

Let me try a different family. Consider the cubic y^3 - 7y - 7. Disc = -4(-7)^3 - 27(49) = 4·343 - 1323 = 1372 - 1323 = 49 = 7^2. ✓

P=0, Q=-7, R=-7. b=0, d=7/4, c^2 = 0·(-7) - (-7) = 7. c = √7, not rational. Doesn't work.

Let me try y^3 - 7y + 7. Disc = -4(-343) - 27(49) = 1372 - 1323 = 49. ✓
P=0, Q=-7, R=7. b=0, d=7/4, c^2 = 0 - 7 = -7. Negative. No.

y^3 - 13y - 13. Disc = 4·2197 - 27·169 = 8788 - 4563 = 4225 = 65^2. ✓
P=0, Q=-13, R=-13. b=0, d=13/4, c^2 = 0 - (-13) = 13. Not a perfect square. No.

y^3 - 19y - 19. Disc = 4·6859 - 27·361 = 27436 - 9747 = 17689 = 133^2. ✓
c^2 = 19. Not a perfect square.

It seems like for the family y^3 - ny - n (which has disc = 4n^3 - 27n^2 = n^2(4n-27)), we need 4n-27 to be a perfect square. 4n-27 = m^2, so n = (m^2+27)/4. For n to be an integer, m must be odd. m=1: n=7. m=3: n=9. m=5: n=13. m=7: n=19. 

For n=7: c^2 = 7. Not square.
For n=9: c^2 = -9. Negative.
For n=13: c^2 = 13. Not square.
For n=19: c^2 = 19. Not square.

The pattern is c^2 = n, which is never a perfect square (since n = (m^2+27)/4 and we'd need n to be a perfect square, so (m^2+27)/4 = k^2, m^2 = 4k^2 - 27. For k=3: m^2=9, m=3, n=9, but then c^2=9, c=3! Let me check: n=9, m=3. y^3 - 9y - 9. Disc = 81·(36-27) = 81·9 = 729 = 27^2. ✓

P=0, Q=-9, R=-9. b=0, d=9/4, c^2 = 0 - (-9) = 9. c = 3. ✓✓✓

So the quartic is x^4 + 0·x^2 + 3x + 9/4, i.e., x^4 + 3x + 9/4. To clear denominators: 4x^4 + 12x + 9. Or multiply by 4: 4x^4 + 12x + 9.

Wait, but 4x^4 + 12x + 9 is not monic. Let me check if it's irreducible. 4x^4 + 12x + 9. Possible rational roots: ±1, ±3, ±9, ±1/2, ±3/2, ±9/2, ±1/4, ±3/4, ±9/4. 

f(0) = 9, f(1) = 4+12+9=25, f(-1) = 4-12+9=1, f(3) = 324+36+9=369, f(-3)=324-36+9=297, f(1/2) = 4/16+6+9=1/4+15=61/4, f(-1/2)=1/4-6+9=13/4, f(3/2)=4·81/16+18+9=81/4+27=189/4, f(-3/2)=81/4-18+9=81/4-9=45/4, f(9/2)=4·6561/16+54+9=6561/4+63, f(1/4)=4/256+3+9=1/64+12, f(-1/4)=1/64-3+9=385/64, f(3/4)=4·81/256+9+9=81/64+18, f(-3/4)=81/64-9+9=81/64, f(9/4)=4·6561/256+27+9=6561/64+36, f(-9/4)=6561/64-27+9=6561/64-18. None are zero.

Could it factor as (2x^2+ax+b)(2x^2-ax+d) or (4x^2+ax+b)(x^2+cx+d) or (x^2+ax+b)(4x^2+cx+d)?

Case (2x^2+ax+b)(2x^2-ax+d) = 4x^4 + (2d+2b-a^2)x^2 + a(d-b)x + bd.
Need: 2d+2b-a^2=0, a(d-b)=12, bd=9.
bd=9: (b,d) ∈ {(1,9),(3,3),(9,1),(-1,-9),(-3,-3),(-9,-1)}.
(b,d)=(3,3): 12-a^2=0, a=±2√3. Not rational.
(b,d)=(1,9): 20-a^2=0, a=±2√5. Not rational.
(b,d)=(9,1): same.
(b,d)=(-3,-3): -12-a^2=0. No.
(b,d)=(-1,-9): -20-a^2=0. No.

Case (4x^2+ax+b)(x^2+cx+d) = 4x^4 + (4c+a)x^3 + (4d+ac+b)x^2 + (ad+bc)x + bd.
Need: 4c+a=0, 4d+ac+b=0, ad+bc=12, bd=9.
a=-4c. bd=9.
4d-4c^2+b=0, so b=4c^2-4d. 
bd = (4c^2-4d)d = 9, so 4c^2d - 4d^2 = 9.
ad+bc = -4cd + (4c^2-4d)c = -4cd + 4c^3 - 4cd = 4c^3 - 8cd = 12, so c^3 - 2cd = 3, c(c^2-2d)=3.

From 4c^2d - 4d^2 = 9: 4d(c^2-d) = 9. So d = 9/(4(c^2-d)). Hmm, this is getting complicated. Let me try small integer values.

c=1: c(c^2-2d)=3 → 1-2d=3 → d=-1. Check 4d(c^2-d)=4(-1)(1+1)=-8≠9. No.
c=3: 3(9-2d)=3 → 9-2d=1 → d=4. Check 4·4·(9-4)=80≠9. No.
c=-1: -1(1-2d)=3 → 1-2d=-3 → d=2. Check 4·2·(1-2)=-8≠9. No.
c=-3: -3(9-2d)=3 → 9-2d=-1 → d=5. Check 4·5·(9-5)=80≠9. No.

Case (x^2+ax+b)(4x^2+cx+d) = 4x^4 + (c+4a)x^3 + (d+ac+4b)x^2 + (ad+bc)x + bd.
Need: c+4a=0, d+ac+4b=0, ad+bc=12, bd=9.
c=-4a. bd=9.
d-4a^2+4b=0, so d=4a^2-4b.
bd = b(4a^2-4b) = 9, so 4a^2b - 4b^2 = 9.
ad+bc = a(4a^2-4b) + b(-4a) = 4a^3 - 4ab - 4ab = 4a^3 - 8ab = 12, so a^3 - 2ab = 3, a(a^2-2b)=3.

This is the same system as before with a instead of c. Same solutions, none work.

So 4x^4 + 12x + 9 is irreducible over Q. ✓

Now, the resolvent cubic of x^4 + 3x + 9/4 (the monic version) is y^3 - 0·y^2 - 4·(9/4)·y + (0 - 9) = y^3 - 9y - 9. This is irreducible (no rational roots: y=0 gives -9, y=1 gives -17, y=3 gives -9, y=-3 gives -9, y=9 gives 567). Wait, let me check more carefully. Rational roots of y^3 - 9y - 9: ±1, ±3, ±9.
y=1: 1-9-9=-17. y=-1: -1+9-9=-1. y=3: 27-27-9=-9. y=-3: -27+27-9=-9. y=9: 729-81-9=639. y=-9: -729+81-9=-657. None zero. So irreducible. ✓

Discriminant of y^3 - 9y - 9 = 4·729 - 27·81 = 2916 - 2187 = 729 = 27^2. Square! ✓

So the Galois group of 4x^4 + 12x + 9 is A4. ✓

This is a cleaner example. Let me use this one: F(x) = 4x^4 + 12x + 9, or equivalently x^4 + 3x + 9/4. Since the problem asks for F(X) ∈ Q[X], I can use either. Let me use 4x^4 + 12x + 9 for integer coefficients. Actually, hmm, it might be even cleaner to write it as x^4 + 3x + 9/4 but that has fractions. Let me just use 4x^4 + 12x + 9.

Wait, actually I realize I should double-check that the discriminant of 4x^4 + 12x + 9 (as a polynomial) is a perfect square. The monic version x^4 + 3x + 9/4 has discriminant 729 = 27^2. The polynomial 4x^4 + 12x + 9 = 4(x^4 + 3x + 9/4) has discriminant 4^{2·4-2} · 729 = 4^6 · 729 = 4096 · 729 = 2,985,984. √2,985,984 = √(4096 · 729) = 64 · 27 = 1728. So 1728^2 = 2,985,984. ✓ It's a perfect square.

So the A4 example is 4x^4 + 12x + 9. ✓

Actually, I just want to also double-check my V4 example. Let me verify x^4 - 4x^2 + 1 more carefully.

The roots are ±√(2+√3) and ±√(2-√3). Note that √(2+√3) · √(2-√3) = √(4-3) = 1. So if α = √(2+√3), then 1/α = √(2-√3). The roots are α, -α, 1/α, -1/α. The splitting field is Q(α) = Q(√(2+√3)). 

[Q(α):Q]: α^2 = 2+√3, so Q(α^2) = Q(√3), degree 2. α = √(2+√3), and α^2 = 2+√3 ∈ Q(√3). Is α ∈ Q(√3)? If α = a+b√3, then α^2 = a^2+3b^2+2ab√3 = 2+√3, so a^2+3b^2=2 and 2ab=1. From 2ab=1, b=1/(2a). a^2+3/(4a^2)=2, 4a^4-8a^2+3=0, a^2=(8±√(64-48))/8=(8±4)/8. a^2=3/2 or a^2=1/2. Neither gives rational a. So α ∉ Q(√3), and [Q(α):Q] = 4.

The splitting field is Q(α) (since all roots are ±α, ±1/α, and 1/α ∈ Q(α)). So the splitting field has degree 4. The Galois group has order 4.

Since the discriminant is 2304 = 48^2 (a square), the Galois group is contained in A4. The only transitive subgroup of A4 with order 4 is V4 (the normal Klein four). So Gal = V4. ✓

Great. Now let me also verify the D4 example. x^4 - 2. The splitting field is Q(2^{1/4}, i). [Q(2^{1/4}):Q] = 4 (Eisenstein). i ∉ Q(2^{1/4}) (since Q(2^{1/4}) ⊂ R). So [Q(2^{1/4}, i):Q] = 8. Gal has order 8. The only transitive subgroup of S4 with order 8 is D4. ✓

Now let me compile everything and write the proof.

Summary:
1. **C4** (cyclic, order 4): F(x) = x^4 + x^3 + x^2 + x + 1 (5th cyclotomic polynomial)
2. **V4** (Klein four, order 4): F(x) = x^4 - 4x^2 + 1
3. **D4** (dihedral, order 8): F(x) = x^4 - 2
4. **A4** (alternating, order 12): F(x) = 4x^4 + 12x + 9
5. **S4** (symmetric, order 24): F(x) = x^4 - x - 1

Let me now write the complete proof.

Actually, let me reconsider whether I should present the A4 example as 4x^4 + 12x + 9 or find a monic one. The problem says F(X) ∈ Q[X], so non-monic is fine. But let me see if there's a simpler monic example.

Actually, 2x^4 + 2x^2 + 2x + 1 also works (from the n=7 cubic). Let me compare:
- 2x^4 + 2x^2 + 2x + 1: resolvent y^3 - y^2 - 2y + 1 (disc 49)
- 4x^4 + 12x + 9: resolvent y^3 - 9y - 9 (disc 729)

Both are valid. I'll use 4x^4 + 12x + 9 since it has fewer terms.

Hmm, actually, let me reconsider. Is there a monic A4 example with integer coefficients? From the construction, I need b, c, d ∈ Z with the resolvent y^3 - by^2 - 4dy + (4bd - c^2) irreducible with square discriminant.

From the n=9 cubic: b=0, d=9/4, c=3. Not integer d.
From the n=7 cubic: b=1, d=1/2, c=1. Not integer d.

Let me try to find one with integer b, c, d. I need 4d to be an integer (it is if d is rational with denominator dividing 4). For d to be an integer, I need Q ≡ 0 (mod 4) in the cubic y^3 + Py^2 + Qy + R, i.e., Q = -4d for integer d.

Let me look for C3 cubics y^3 + Py^2 + Qy + R with Q divisible by 4 and PQ - R a perfect square.

The cubic y^3 - y^2 - 2y + 1 has Q = -2, not divisible by 4.
The cubic y^3 - 9y - 9 has Q = -9, not divisible by 4.

Let me try to find a C3 cubic with Q divisible by 4. 

Consider y^3 + Py^2 - 4ky + R with disc = square. 

Let me try P = 0, so y^3 - 4ky + R. Disc = 4(4k)^3/... wait, for y^3 + py + q (depressed), disc = -4p^3 - 27q^2. Here p = -4k, q = R. Disc = -4(-4k)^3 - 27R^2 = 256k^3 - 27R^2.

I need 256k^3 - 27R^2 = m^2 for some integer m, and c^2 = 0·(-4k) - R = -R, so R must be negative and -R must be a perfect square. Let R = -s^2. Then disc = 256k^3 - 27s^4 = m^2.

And the quartic would be x^4 + 0·x^2 + sx + (-s^2/4)... wait, d = -Q/4 = k, c = s, b = 0. So the quartic is x^4 + sx + k. For integer coefficients, I need s, k ∈ Z.

Disc of quartic = disc of resolvent = 256k^3 - 27s^4 = m^2.

Let me try s = 1: 256k^3 - 27 = m^2. k=1: 229, not square. k=2: 2048-27=2021, not square. k=3: 6912-27=6885, not square.

s = 2: 256k^3 - 27·16 = 256k^3 - 432 = m^2. k=1: -176, no. k=2: 2048-432=1616, not square. k=3: 6912-432=6480, not square.

s = 3: 256k^3 - 27·81 = 256k^3 - 2187 = m^2. k=1: -1931. k=2: 2048-2187=-139. k=3: 6912-2187=4725, not square. k=4: 16384-2187=14197, not square.

This is hard. Let me try a different approach - use a non-depressed cubic.

Consider y^3 + Py^2 + Qy + R with P ≠ 0, Q = -4d, and the cubic has square discriminant.

Actually, this is getting too complicated. Let me just use the non-monic examples I already have. The problem says F(X) ∈ Q[X], which allows non-monic polynomials. I'll use 4x^4 + 12x + 9 for A4.

Actually, wait. Let me try one more thing. Consider the polynomial x^4 - 2x^3 - 7x^2 + 8x + 12... no, that splits. 

How about trying x^4 - 4x^3 + 2x^2 + 4x - 2? Let me not go down this path. I'll use what I have.

Hmm, actually, let me try one more: the polynomial x^4 - 4x^3 - 4x^2 + 16x + 8. Hmm, I don't know its discriminant off the top of my head.

OK, I'll just go with 4x^4 + 12x + 9 for A4. It's a perfectly valid polynomial in Q[x].

Wait, one more idea. I can try x^4 - 4x^3 + 2x^2 + 4x - 2. Hmm, let me not. Let me also try the approach of using a known A4 example from number theory.

The splitting field of x^4 - 2x^3 - 7x^2 + 8x + 12 is Q itself (it splits). Not useful.

How about the minimal polynomial of √(2 + √(2 + √2))? That's degree 8, not 4.

OK, I'll go with my examples. Let me also think about whether I should present the A4 example differently. 

Actually, I just realized: I can make a monic integer example by substitution. If 4x^4 + 12x + 9 has Galois group A4, then substituting x = 2y gives 4(2y)^4 + 12(2y) + 9 = 64y^4 + 24y + 9. Still not monic. 

Alternatively, 4x^4 + 12x + 9 = 0 ⟺ x^4 + 3x + 9/4 = 0. If I substitute x = y/2: (y/2)^4 + 3(y/2) + 9/4 = y^4/16 + 3y/2 + 9/4 = 
