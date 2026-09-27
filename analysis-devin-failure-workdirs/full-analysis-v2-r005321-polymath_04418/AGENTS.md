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
  <problem_id>polymath_04418</problem_id>
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

There are $2012$ points marked on a circle, dividing it into equal arcs. From them, $k$ points are chosen, and a convex $k$-gon is constructed with vertices at the chosen points. What is the largest $k$ such that this polygon has no parallel sides?

## Standard Solution

Let $A_{1}, A_{2}, \ldots, A_{2012}$ be the marked points in order around the circle (with $A_{2013}=A_{1}, A_{2014}=A_{2}$, etc.). Divide the points into groups of four: $(A_{1}, A_{2}, A_{1007}, A_{1008})$, $(A_{3}, A_{4}, A_{1009}, A_{1010})$, ..., $(A_{1005}, A_{1006}, A_{2011}, A_{2012})$. 

If all four points of any group $(A_{2i-1}, A_{2i}, A_{2i+1005}, A_{2i+1006})$ are chosen as vertices, then the polygon will contain two sides, $A_{2i-1}A_{2i}$ and $A_{2i+1005}A_{2i+1006}$, which are symmetric with respect to the center of the circle and therefore parallel. To avoid parallel sides, in each of the $503$ groups, at most three points can be chosen. Thus, $k \leq 503 \times 3 = 1509$.

To show that $k=1509$ is possible, consider the polygon with vertices $A_{1}, A_{2}, \ldots, A_{1006}, A_{1008}, A_{1010}, \ldots, A_{2012}$ (that is, all points numbered from $1$ to $1006$ and all even-numbered points from $1008$ to $2012$). The sides $A_{2012}A_{1}, A_{1}A_{2}, \ldots, A_{1005}A_{1006}$ lie on one side of the diameter $A_{2012}A_{1006}$ and cannot be parallel; similarly, the sides $A_{1006}A_{1008}, \ldots, A_{2010}A_{2012}$ are pairwise non-parallel. Also, the small diagonal $A_{j}A_{j+2}$ of the regular $2012$-gon is not parallel to its sides, so no two sides of the form $A_{i}A_{i+1}$ and $A_{j}A_{j+2}$ can be parallel.

Therefore, the largest possible $k$ is $\boxed{1509}$.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. 2012 points on a circle, divided into equal arcs. Choose k points, form a convex k-gon. Find largest k such that the polygon has no parallel sides.

Let me think. The points are equally spaced on a circle with 2012 points. A side of the polygon connects two consecutive chosen points (in circular order). A side is a chord between two consecutive chosen vertices. Two sides are parallel if and only if... Let me think about when two chords are parallel. Points are labeled 0, 1, ..., 2011 around the circle. A chord from point a to point b. The direction of the chord... Two chords are parallel iff they have the same direction.

A chord between points i and j (i < j) - the midpoint of the arc. Actually, a chord is parallel to another chord if the sum of the endpoints are equal mod 2012? Let me think. Point i is at angle 2πi/2012. Chord from i to j has direction... The chord from point a to point b is perpendicular to the radius through the midpoint of the arc. Actually the chord direction: the chord connects angles θ_a and θ_b. The direction of the chord is perpendicular to the bisector direction (θ_a + θ_b)/2.

So two chords (a,b) and (c,d) are parallel iff (θ_a + θ_b)/2 ≡ (θ_c + θ_d)/2 mod π, i.e., θ_a + θ_b ≡ θ_c + θ_d mod 2π, OR θ_a + θ_b ≡ θ_c + θ_d + 2π mod 2π... wait.

Parallel means same direction or opposite direction. The chord direction angle is (θ_a + θ_b)/2 + π/2 (perpendicular to bisector). Two chords parallel iff their direction angles are equal mod π. So (θ_a+θ_b)/2 ≡ (θ_c+θ_d)/2 mod π, i.e., θ_a+θ_b ≡ θ_c+θ_d mod 2π.

So in terms of indices: a + b ≡ c + d (mod 2012).

Wait, but need to be careful. θ_a + θ_b = 2π(a+b)/2012. So parallel iff (a+b) ≡ (c+d) mod 2012.

Hmm, but actually we need the chord direction. Let me reconsider. The chord from a to b: vector = (cos θ_b - cos θ_a, sin θ_b - sin θ_a). Using sum-to-product: = (-2 sin((θ_a+θ_b)/2) sin((θ_b-θ_a)/2), 2 cos((θ_a+θ_b)/2) sin((θ_b-θ_a)/2)). So direction is proportional to (-sin((θ_a+θ_b)/2), cos((θ_a+θ_b)/2)), which has angle (θ_a+θ_b)/2 + π/2.

So two chords parallel iff (θ_a+θ_b)/2 ≡ (θ_c+θ_d)/2 mod π, iff (a+b) ≡ (c+d) mod 2012.

So a side of the polygon is a chord between consecutive chosen vertices. Let the chosen vertices in order be v_1 < v_2 < ... < v_k (indices mod 2012). The sides are chords (v_1,v_2), (v_2,v_3), ..., (v_{k-1},v_k), (v_k, v_1) where the last wraps around (v_k to v_1, but as a chord the sum is v_k + v_1, but careful: the chord from v_k to v_1 going the "short way"? No—the polygon is convex, vertices in circular order, so the side from v_k to v_1 is the chord connecting them directly, sum = v_k + v_1).

Wait, but the sum for the wrap-around side: the chord connects point v_k and point v_1. The sum is v_k + v_1. But is that right? The indices are 0..2011. The chord is just the chord between those two points regardless of "direction". So sum = v_1 + v_k.

So we have k sides with sums s_i = v_i + v_{i+1} for i=1..k-1, and s_k = v_k + v_1. We need all these sums to be distinct mod 2012 (no two parallel means no two sums equal mod 2012).

Wait, but also a side could be parallel to itself trivially—no, we need distinct sides to be non-parallel, so all s_i distinct mod 2012.

So we need: choose k distinct points from {0,...,2011}, arrange in circular order v_1<...<v_k, such that the k sums v_i+v_{i+1} (with v_{k+1}=v_1) are all distinct mod 2012.

We want max k.

Note 2012 = 4 × 503. 503 is prime.

Let me think about upper bound. The sums are mod 2012, so there are 2012 possible values. But there's a constraint: sum of all s_i = 2(v_1+...+v_k) mod 2012. Also, s_i = v_i + v_{i+1}.

Hmm, let me think about parity. 2012 is even. Consider sums mod 2. s_i = v_i + v_{i+1} mod 2. The number of even sums vs odd sums. Actually, let's think: if we have k vertices, the sums alternate parity based on consecutive vertex parities. Let me think differently.

Actually let me think about the structure. We need the k sums to be distinct mod 2012. Since there are only 2012 residues, k ≤ 2012. But much smaller due to constraints.

Let me think about what values sums can take. Actually, let me consider the problem more carefully with the constraint that vertices are distinct and in circular order.

Alternative approach: Let's think about it as: we need a set of k points such that the "edge sums" are all distinct mod 2012.

Let me think about small cases / structure. Consider the differences. Let d_i = v_{i+1} - v_i (mod 2012) for i=1..k-1, and d_k = v_1 - v_k mod 2012 = 2012 - (v_k - v_1) ... actually d_k = (v_1 - v_k) mod 2012. The d_i are positive, sum to 2012. Each d_i ≥ 1.

The sum s_i = v_i + v_{i+1} = 2v_i + d_i.

Hmm. Let me think about whether there's a cleaner characterization.

Two sides parallel: s_i = s_j mod 2012. s_i - s_j = (v_i + v_{i+1}) - (v_j + v_{j+1}) = (v_i - v_j) + (v_{i+1} - v_{j+1}).

Let me think about the answer. I suspect the answer is 503. Let me explore.

Actually, let me think about it via the following: the sums s_i mod 2012. Note that s_i + s_{i+1} = v_i + 2v_{i+1} + v_{i+2}... not obviously useful.

Let me think about parity constraint. Among the k sums s_1,...,s_k, how many are even and how many odd? s_i = v_i + v_{i+1}. s_i is even iff v_i, v_{i+1} have same parity. Consider the cyclic sequence of parities of v_1,...,v_k. The number of even sums = number of adjacent pairs with same parity. Number of odd sums = number of adjacent pairs with different parity = number of parity changes in the cyclic sequence.

If among the k vertices, e are even-indexed and o = k-e are odd-indexed. The number of parity changes in a cyclic binary sequence is even, say 2t. Then odd sums = 2t, even sums = k - 2t.

Now, even sums mod 2012: s_i even means s_i ∈ {0,2,4,...,2010}, that's 1006 values. Odd sums: 1006 values.

For all sums distinct, we need #even sums ≤ 1006 and #odd sums ≤ 1006. That's not binding for small k.

Hmm, let me think about a stronger constraint. Consider sums mod 4. 2012 = 4·503. s_i mod 4. Hmm.

Actually, let me reconsider. Let me think about the sums mod 503. Since 2012 = 4·503, reducing mod 503: s_i mod 503 = (v_i + v_{i+1}) mod 503. There are 503 residues. If k > 503, then by pigeonhole two sums are equal mod 503. But equal mod 503 doesn't mean equal mod 2012. So that alone doesn't force parallel.

Hmm wait, parallel requires equal mod 2012, not mod 503. So that's not directly it.

Let me reconsider. Let me think about the actual maximum.

Let me think about construction. Can we get k = 1006? Or k around 1006?

Let me think about a simple construction: take vertices 0, 1, 2, ..., k-1 consecutive. Then sides are (0,1),(1,2),...,(k-2,k-1),(k-1,0). Sums: 1, 3, 5, ..., 2k-3, k-1. For these to be distinct mod 2012... sums are 1,3,5,...,2k-3 (odd numbers) and k-1. If k is even, k-1 is odd, so all sums odd. The odd sums 1,3,...,2k-3 are k-1 distinct odd numbers, plus k-1. Need k-1 not equal to any of 1,3,...,2k-3 and all distinct mod 2012. 2k-3 < 2012 requires k < 1007.5, so k ≤ 1007. And k-1 distinct from 1,3,...,2k-3: k-1 is odd (k even), and 1,3,...,2k-3 includes all odd from 1 to 2k-3. k-1 ≤ 2k-3 for k≥2, and k-1 odd means k-1 ∈ {1,3,...,2k-3} when k-1 ≤ 2k-3 i.e. k≥2. So k-1 is in the set! Collision. So consecutive doesn't work for k even ≥ 2.

Let me try k odd, consecutive vertices 0..k-1. Sums: 1,3,...,2k-3 (k-1 values, even count since k-1 even), and k-1 (even). So odd sums: 1,3,...,2k-3 (that's k-1 values, all distinct, all < 2012 if 2k-3<2012 i.e. k≤1007). Even sum: k-1. No collision between even and odd. So all distinct mod 2012 as long as 2k-3 < 2012, i.e., k ≤ 1007. And k-1 < 2012. So for k odd, k ≤ 1007, consecutive vertices 0..k-1 give all distinct sums!

Wait let me double check. k odd, vertices 0,1,...,k-1. Sides: (0,1),(1,2),...,(k-2,k-1),(k-1,0). Sums: 0+1=1, 1+2=3, ..., (k-2)+(k-1)=2k-3, (k-1)+0=k-1. So sums = {1,3,5,...,2k-3} ∪ {k-1}. k odd → k-1 even. The set {1,3,...,2k-3} has (k-1) elements (since 2k-3 = 2(k-1)-1, odd numbers from 1 to 2(k-1)-1, that's k-1 numbers). All odd. k-1 is even, distinct from all. All values < 2012 when 2k-3 ≤ 2011, i.e., k ≤ 1007. So for k = 1007 (odd), works! Sums are 1,3,...,2011 (1006 odd numbers) and 1006. All distinct, all in [1,2011]. 

So k ≥ 1007.

Can we do better? k = 1008? Let's see if possible.

Upper bound argument: We need k distinct sums mod 2012. Let me find an upper bound.

Consider the sums mod 2. As computed, #odd sums = number of parity changes (even number 2t), #even sums = k - 2t. Odd sums take values in 1006 odd residues, even sums in 1006 even residues. So k - 2t ≤ 1006 and 2t ≤ 1006. So k ≤ 1006 + 2t and 2t ≤ 1006, giving k ≤ 1006 + 1006 = 2012. Not helpful directly. But also k = (k-2t) + 2t ≤ 1006 + 1006 = 2012. To maximize k, want both close to 1006: k - 2t = 1006 and 2t = 1006, so k = 2012. But that requires all residues used, impossible since vertices distinct... 

Hmm, that bound is weak. Let me think more carefully.

Let me think about a better upper bound. Consider the sums s_i = v_i + v_{i+1}. Note that:
s_1 + s_3 + s_5 + ... (odd-indexed sides) vs s_2 + s_4 + ... 

Actually, let me think about alternating sum. s_1 - s_2 + s_3 - s_4 + ... = (v_1+v_2) - (v_2+v_3) + (v_3+v_4) - ... = v_1 + (v_2 - v_2) + (-v_3 + v_3) + ... 

For k even: s_1 - s_2 + s_3 - ... - s_k = v_1 - v_k... let me compute. = v_1 + v_2 - v_2 - v_3 + v_3 + v_4 - ... - v_k - v_1? Let me be careful. s_i = v_i + v_{i+1}, v_{k+1}=v_1.

Σ_{i=1}^{k} (-1)^{i+1} s_i = Σ (-1)^{i+1} v_i + Σ (-1)^{i+1} v_{i+1}.

Second sum: let j = i+1, = Σ_{j=2}^{k+1} (-1)^j v_j = Σ_{j=2}^{k} (-1)^j v_j + (-1)^{k+1} v_1.

First sum: Σ_{i=1}^k (-1)^{i+1} v_i.

Total = v_1 + Σ_{i=2}^k [(-1)^{i+1} + (-1)^i] v_i + (-1)^{k+1} v_1 = v_1 + 0 + (-1)^{k+1} v_1 = v_1(1 + (-1)^{k+1}).

If k even: 1 + (-1)^{k+1} = 1 + (-1)^{odd} = 1 - 1 = 0. So alternating sum = 0.
If k odd: 1 + (-1)^{k+1} = 1 + 1 = 2. So alternating sum = 2v_1.

Interesting. For k even, Σ (-1)^{i+1} s_i = 0 mod 2012.

So for k even, the alternating sum of the k sums is 0 mod 2012. The s_i are k distinct residues mod 2012. We need k distinct residues (k even) such that alternating sum is 0 mod 2012, AND they can be realized as edge-sums of a polygon. The alternating sum constraint: s_1 + s_3 + ... + s_{k-1} = s_2 + s_4 + ... + s_k mod 2012 (k/2 terms each).

This is a necessary condition but not obviously bounding k.

Hmm, let me think about the real constraint differently. Let me reconsider the problem. Maybe the answer is 1007 and the upper bound needs a clever argument.

Let me think about it from the perspective of: the k sums are distinct mod 2012. Also note s_i = v_i + v_{i+1}, and the differences d_i = v_{i+1} - v_i > 0, Σ d_i = 2012.

We have v_{i+1} = v_i + d_i, so s_i = 2v_i + d_i. And v_i = v_1 + d_1 + d_2 + ... + d_{i-1}.

Alternatively s_i = v_i + v_{i+1} and s_{i+1} = v_{i+1} + v_{i+2}, so s_{i+1} - s_i = v_{i+2} - v_i = d_i + d_{i+1}.

So consecutive sums differ by d_i + d_{i+1}.

Hmm. Let me think about the upper bound via a different parity/mod argument.

Consider sums mod 2 again but more carefully. Actually, let me reconsider: is 1007 achievable and is it the max? Let me check if k=1008 is impossible.

For k=1008 (even). The alternating sum is 0 mod 2012. We need 1008 distinct residues with alternating sum 0. That's possible in principle (e.g., pair up). But realizability as a polygon...

Let me think about an upper bound using mod 2 more carefully. With k vertices, let e = # even vertices, o = # odd vertices, e + o = k. The number of "odd sums" (s_i odd) = number of edges connecting even-odd pair = number of parity changes in cyclic order = 2t (even). 

Now here's a key constraint: the number of edges between even and odd vertices. In the cyclic sequence, each even vertex is followed by something. Let me count edges from even to odd plus odd to even = 2t. 

Also, edges from even to even: let's call a, edges from odd to odd: b, edges even-odd: 2t. a + b + 2t = k. Even sums = a + b (same parity pairs), odd sums = 2t.

Now, even sums are a+b distinct even residues (out of 1006), odd sums are 2t distinct odd residues (out of 1006).

So a + b ≤ 1006 and 2t ≤ 1006. k = a+b+2t ≤ 2012. Still weak.

But there's another constraint relating a, b, e, o. The number of even-to-even edges a: each even vertex has a "next" vertex. Hmm, in a cyclic sequence, the number of even-to-even transitions... Let me think. Sum over even vertices of [next is even] = a. Sum over odd vertices of [next is odd] = b. 

Actually, consider: number of even vertices e. Each even vertex's successor is either even (contributes to a) or odd. The number of even vertices whose successor is odd = e - a... no wait. Let me define: a = # of i with v_i even and v_{i+1} even. The number of i with v_i even and v_{i+1} odd = e - a. This equals number of even→odd transitions. Similarly odd→even transitions = o - b. And even→odd = odd→even (cyclic), so e - a = o - b = t. So a = e - t, b = o - t. Then a + b = e + o - 2t = k - 2t. Consistent. And a = e - t ≥ 0, b = o - t ≥ 0, so t ≤ min(e,o).

OK so the constraints are: a+b = k-2t ≤ 1006, 2t ≤ 1006, t ≤ min(e,o), e+o=k. To maximize k: set 2t = 1006 (t=503) and k - 2t = 1006, so k = 2012, t = 503, e - t ≥ 0 and o - t ≥ 0 so e,o ≥ 503, e+o = 2012, so e = o = 1006, a = e - t = 503, b = o - t = 503. So in principle k=2012 with all 2012 vertices, all sums distinct (using all residues). But that's impossible since all 2012 vertices means the polygon is the full 2012-gon, and sums would be... v_i = i-1, s_i = (i-1)+i = 2i-1 for i=1..2011, and s_{2012} = 2011 + 0 = 2011. So sums = 1,3,5,...,4021 mod 2012, and 2011. 4021 = 2·2012 - 3, so 2i-1 mod 2012 for i=1..2011 gives 1,3,...,2011,2013,...,4021 mod 2012 = 1,3,...,2011,1,3,...,2009. Duplicates! So full polygon has parallel sides. Right, because 2012 is even, opposite sides are parallel.

So the mod-2 counting bound is too weak. The real constraint is mod 2012 distinctness with the polygon structure.

Let me reconsider. The answer might be 1007. Let me try to prove k ≤ 1007.

Hmm, let me think about the alternating sum constraint for even k more carefully, combined with distinctness.

For k even: s_1 + s_3 + ... + s_{k-1} ≡ s_2 + s_4 + ... + s_k (mod 2012), each side has k/2 distinct residues, and all k are distinct. 

Let A = {s_1, s_3, ...} (k/2 residues), B = {s_2, s_4, ...} (k/2 residues), A ∩ B = ∅, A ∪ B = all k sums, and ΣA ≡ ΣB mod 2012.

Is there a constraint that prevents k/2 from being too large? ΣA ≡ ΣB mod 2012 means ΣA - ΣB ≡ 0 mod 2012. With A, B disjoint subsets of Z_{2012}, |A|=|B|=k/2. 

The total Σ(A∪B) = ΣA + ΣB. And ΣA - ΣB ≡ 0. So 2ΣA ≡ Σ(A∪B) mod 2012... not obviously impossible.

Hmm, I don't think the alternating sum alone gives k ≤ 1007. Let me reconsider whether 1008 is achievable.

Let me try to construct k = 1008. We need 1008 distinct sums. Let me try a different construction.

Actually, wait. Let me reconsider the consecutive construction but with a shift or different pattern to get even k.

Let me try vertices 0, 1, 2, ..., k-1 for general k and check when sums are distinct mod 2012. Sums: 1, 3, 5, ..., 2k-3, k-1. These are distinct mod 2012 iff:
- All of 1,3,...,2k-3 are distinct mod 2012 (they are if 2k-3 < 2012, i.e., k ≤ 1007; if k ≥ 1008, 2k-3 ≥ 2013, and we get wraparound duplicates).
- k-1 not in {1,3,...,2k-3} mod 2012.

For k ≤ 1007: 1,3,...,2k-3 are distinct (all < 2012). k-1: if k even, k-1 odd, and k-1 ∈ [1, 2k-3] for k ≥ 2, so collision. If k odd, k-1 even, no collision with odd sums. So consecutive works for k odd, k ≤ 1007. Max k = 1007.

For k = 1008: 2k-3 = 2013. Sums 1,3,...,2013 mod 2012 = 1,3,...,2011, 1. Duplicate (1 appears twice). So consecutive fails.

Can we do a non-consecutive construction for k = 1008? Let me think.

Let me try to think about the upper bound more seriously. 

Claim: k ≤ 1007. 

Let me think about why. Consider the k sums s_1, ..., s_k, all distinct mod 2012. Consider them mod 2: we showed #odd = 2t ≤ 1006, #even = k - 2t ≤ 1006. For k = 1008: need 2t ≤ 1006 and 1008 - 2t ≤ 1006, i.e., 2t ≥ 2, i.e., t ≥ 1. And 2t ≤ 1006. So t ∈ [1, 503]. Feasible by parity counting.

Hmm. So parity doesn't rule out 1008. Let me think about mod 4.

2012 = 4 · 503. Consider sums mod 4. s_i = v_i + v_{i+1} mod 4. There are 4 residues, each with 503 values mod 2012 (residue r mod 4: r, r+4, ..., r+4·502, that's 503 values). For all sums distinct mod 2012, certainly all distinct mod 4 isn't required, but the count per residue class mod 4 is bounded by 503.

So # of sums ≡ 0 mod 4 ≤ 503, ≡ 1 ≤ 503, ≡ 2 ≤ 503, ≡ 3 ≤ 503. Total k ≤ 2012. Still weak. But for k = 1008, we'd need the distribution mod 4 to have each class ≤ 503, sum = 1008. E.g., 252 each. Feasible.

Let me think about the structure of s_i mod 4 in terms of v_i mod 4. This is getting complicated. Let me think about the problem differently.

Alternative: think about which pairs of sides can be parallel and use a graph/matching argument.

Two sides (v_i, v_{i+1}) and (v_j, v_{j+1}) are parallel iff v_i + v_{i+1} ≡ v_j + v_{j+1} mod 2012.

Hmm, let me think about the "antipodal" structure. 2012 is even, so there are 1006 pairs of antipodal points. A chord is a "diameter" if endpoints are antipodal (differ by 1006). 

Let me think about the problem in terms of the following: each side has a "direction" which is an element of Z_{2012} (the sum mod 2012). We need all k directions distinct. The direction of side (v_i, v_{i+1}) is v_i + v_{i+1} mod 2012. 

Note: direction d and direction d + 1006 correspond to parallel chords? No—parallel means equal mod 2012 (since we established parallel iff sums equal mod 2012). Wait, let me re-examine. Parallel iff (a+b) ≡ (c+d) mod 2012. But actually, should it be mod 2012 or mod 1006? Because direction angle (θ_a+θ_b)/2 + π/2, and parallel means equal mod π. (θ_a + θ_b)/2 ≡ (θ_c+θ_d)/2 mod π means θ_a + θ_b ≡ θ_c + θ_d mod 2π, i.e., (a+b) ≡ (c+d) mod 2012. Yes mod 2012. Good. (Because mod 2π corresponds to mod 2012.)

Wait, but that's not right either. Let me redo. Direction angle = (θ_a + θ_b)/2 + π/2. Parallel (including anti-parallel) means direction angles equal mod π. So (θ_a+θ_b)/2 + π/2 ≡ (θ_c+θ_d)/2 + π/2 mod π, so (θ_a+θ_b)/2 ≡ (θ_c+θ_d)/2 mod π, so θ_a + θ_b ≡ θ_c + θ_d mod 2π. Since θ = 2π·index/2012, this is (a+b) ≡ (c+d) mod 2012. 

So yes, parallel iff sums congruent mod 2012. Good.

So we need k distinct residues (the edge sums) mod 2012. Now I realize the constraint is just that these k sums, which are determined by the vertex set, are distinct mod 2012.

Let me reconsider: is the max really 1007? Let me try to construct k=1008 with a non-consecutive set.

Let me think computationally (in my head) about a smarter construction. 

Idea: Use vertices that form an arithmetic progression with step 2: 0, 2, 4, ..., 2(k-1). Then sides: (0,2),(2,4),...,(2(k-2),2(k-1)),(2(k-1),0). Sums: 2, 6, 10, ..., 4k-6, 2(k-1). All even. Divide by 2: 1, 3, 7, ..., 2k-3, k-1. Wait let me recompute. Sums: (2i + 2(i+1)) = 4i+2 for i=0..k-2, giving 2, 6, 10, ..., 4(k-2)+2 = 4k-6. And last sum 2(k-1)+0 = 2k-2. So sums = {2,6,10,...,4k-6} ∪ {2k-2}. Divide by 2: {1,3,5,...,2k-3} ∪ {k-1}. Same as before! Because it's just the consecutive construction scaled. So same result: k odd ≤ 1007 works (but now need 2(k-1) < 2012, i.e., k ≤ 1006... wait 2(k-1) is the largest vertex index, need < 2012, so k-1 ≤ 1005, k ≤ 1006). Hmm, and sums 4k-6 < 2012 needs k ≤ 504. So this is worse. Scrap this.

Let me think about the upper bound proof for k ≤ 1007.

Key insight attempt: Consider the k edge sums s_1, ..., s_k, all distinct mod 2012. Consider their sum: Σ s_i = 2 Σ v_i mod 2012. Also, consider Σ s_i mod 2: Σ s_i ≡ 2 Σ v_i ≡ 0 mod 2. So the sum of all k sums is even. That means the number of odd sums is even (which we knew: 2t).

Hmm. Let me think about the product or another symmetric function.

Another approach: Let me think about the problem as a graph coloring / Sidon-type problem.

Actually, let me reconsider. Let me think about the upper bound via the following elegant argument:

Consider the k sides. Each side is a chord. Two chords are parallel iff their "midpoints" (in terms of arc midpoint, i.e., (a+b)/2 mod 2012... but careful with the factor 2) coincide. The direction is determined by (a+b) mod 2012. 

Now, here's a thought: consider pairing each side with the side "opposite" to it. Actually, let me think about the following: the k sums s_i are distinct mod 2012. Note that s_i ≡ v_i + v_{i+1}. Consider the "complement" s_i' = s_i + 1006 mod 2012 (the antipodal direction). If both s_i and s_j = s_i + 1006 appear among the sums, that's fine (they're different mod 2012, not parallel). 

Hmm, I keep not finding the bound. Let me just try to verify computationally whether 1008 is possible, by thinking about a specific construction.

Let me try: vertices 0, 1, 2, ..., 1006, 1008. (k = 1008, skipping 1007). Sides: (0,1),(1,2),...,(1005,1006),(1006,1008),(1008,0). Sums: 1,3,5,...,2011 (from (i,i+1) for i=0..1005, giving 2i+1 for i=0..1005 → 1,3,...,2011, that's 1006 values), then (1006+1008)=2014 ≡ 2 mod 2012, then (1008+0)=1008. So sums = {1,3,5,...,2011} ∪ {2, 1008}. The odd sums 1,3,...,2011 are all 1006 odd residues. 2 and 1008 are even. All distinct? 2 ≠ 1008, and both even, distinct from odd sums. So all 1008 sums distinct! 

Wait, so k = 1008 works?! Let me double-check. Vertices: 0,1,2,...,1006,1008. That's 1007 + 1 = 1008 vertices. In circular order on the 2012-gon: 0,1,2,...,1006,1008 (then back to 0). The sides are consecutive in this order:
- (0,1): sum 1
- (1,2): sum 3
- ...
- (1005,1006): sum 2011
- (1006,1008): sum 2014 ≡ 2 (mod 2012)
- (1008,0): sum 1008

Sums mod 2012: {1, 3, 5, ..., 2011} ∪ {2, 1008}. 
- Odd sums: 1,3,...,2011 — all 1006 odd residues, distinct. ✓
- Even sums: 2, 1008 — distinct, and even. ✓
- No odd = even. ✓
All 1008 distinct mod 2012. So no parallel sides! k = 1008 works.

So the answer is at least 1008. Let me push further. Can we do 1009?

Let me try adding more. Vertices 0,1,...,1006,1008,1010? Let me try to add even vertices at the "top".

Actually, let me think systematically. The consecutive block 0,1,...,1006 gives 1006 sides with all odd sums 1,3,...,2011 (using all odd residues). Then I have two "gap" sides connecting the block to extra vertices and back. Each extra vertex added in the gap (between 1006 and 0 going the long way) creates sides.

Let me reconsider. Let me place vertices: a block 0,1,...,1006 (consecutive, 1007 vertices), then extra vertices w_1, w_2, ..., w_m in the arc from 1007 to 2011 (the "far" arc), in increasing order: 1006 < w_1 < w_2 < ... < w_m < 2012 (and then back to 0). Wait, but 1006 to w_1: the side (1006, w_1). Then sides (w_1,w_2),...,(w_{m-1},w_m), and (w_m, 0).

Total vertices k = 1007 + m. Sides:
- (i, i+1) for i=0..1005: sums 1,3,...,2011 (1006 sides, all odd residues). 
- (1006, w_1): sum 1006 + w_1.
- (w_j, w_{j+1}) for j=1..m-1: sums w_j + w_{j+1}.
- (w_m, 0): sum w_m.

We need all these distinct mod 2012 and distinct from {1,3,...,2011}.

The odd residues are all used up (1,3,...,2011). So all the new sums (1006+w_1, w_j+w_{j+1}, w_m) must be even (to avoid collision with odd sums) and distinct mod 2012.

1006 + w_1 even ⟺ w_1 even. w_m even. w_j + w_{j+1} even ⟺ w_j, w_{j+1} same parity. So if all w_j are even, then all new sums are even. 

So let all w_j be even, w_j ∈ {1008, 1010, ..., 2010} (even numbers from 1008 to 2010; note 1006 is the last block vertex, and w_1 > 1006, so w_1 ≥ 1007, but must be even so w_1 ≥ 1008). The available even numbers in (1006, 2012) are 1008, 1010, ..., 2010: that's (2010-1008)/2 + 1 = 502 numbers.

New sums (all even, need distinct mod 2012, and distinct from each other):
- 1006 + w_1 (even, ranges from 1006+1008=2014≡2 to 1006+2010=3016≡1004 mod 2012)
- w_j + w_{j+1} for j=1..m-1
- w_m (even, ranges 1008 to 2010)

We need these m+1 even sums distinct mod 2012. There are 1006 even residues (0,2,...,2010). We've used 0 even residues from the block (block used odd). So up to 1006 even residues available. We need m+1 ≤ 1006, so m ≤ 1005. But m ≤ 502 (only 502 even numbers available). So k = 1007 + m ≤ 1007 + 502 = 1509. But we need the sums to actually be distinct, which is the real constraint.

Let me think about maximizing m. We need the m+1 sums {1006+w_1, w_1+w_2, w_2+w_3, ..., w_{m-1}+w_m, w_m} to be distinct even residues mod 2012.

Let me substitute: let w_j = 2u_j where u_j ∈ {504, 505, ..., 1005} (since w_j ∈ {1008,...,2010}, u_j = w_j/2 ∈ {504,...,1005}). Then sums (divided by 2):
- (1006 + w_1)/2 = 503 + u_1
- (w_j + w_{j+1})/2 = u_j + u_{j+1}
- w_m/2 = u_m

Need these distinct mod 1006 (since even residues mod 2012 ÷ 2 = residues mod 1006). And u_j ∈ {504,...,1005}, distinct (since w_j distinct), increasing.

So we need: {503 + u_1, u_1 + u_2, u_2 + u_3, ..., u_{m-1} + u_m, u_m} all distinct mod 1006, where 504 ≤ u_1 < u_2 < ... < u_m ≤ 1005.

Hmm, this is a similar sub-problem. Let me see how large m can be.

Note u_m ∈ {504,...,1005}, so u_m mod 1006 is just u_m (since ≤ 1005 < 1006). 503 + u_1: u_1 ≥ 504, so 503 + u_1 ≥ 1007 > 1006, so 503 + u_1 mod 1006 = 503 + u_1 - 1006 = u_1 - 503. So 503 + u_1 ≡ u_1 - 503 mod 1006. For u_1 = 504: ≡ 1. For u_1 = 1005: ≡ 502.

u_j + u_{j+1}: ranges from 504+505=1009 to 1004+1005=2009. Mod 1006: 1009 ≡ 3, 2009 ≡ 2009-1006=1003. So u_j+u_{j+1} mod 1006 ∈ [3, 1003] roughly (could wrap). Actually u_j + u_{j+1} ∈ [1009, 2009], mod 1006 ∈ [3, 1003]. 

u_m ∈ [504, 1005].

So the values:
- u_1 - 503 ∈ [1, 502]
- u_j + u_{j+1} mod 1006 ∈ [3, 1003]
- u_m ∈ [504, 1005]

For these to be distinct mod 1006. The first value is in [1,502], the last in [504,1005], so they don't overlap with each other. The middle values in [3,1003] can overlap with both.

This is getting complex. Let me just try to see if we can get m = 502 (all available even vertices), giving k = 1007 + 502 = 1509.

If m = 502, u_j = 503 + j for j = 1..502, i.e., u_j ∈ {504,...,1005} all of them. Then:
- u_1 - 503 = 1.
- u_j + u_{j+1} = (503+j) + (504+j) = 1007 + 2j for j=1..501. Mod 1006: 1 + 2j. So values 3, 5, 7, ..., 1+2·501 = 1003. So {3,5,7,...,1003} = odd numbers from 3 to 1003, that's 501 values.
- u_m = u_{502} = 1005.

So the set is {1} ∪ {3,5,...,1003} ∪ {1005} = {1, 3, 5, ..., 1003, 1005} = all odd numbers from 1 to 1005. That's 503 values. But we need 503 distinct values (m+1 = 503), and we got 503 distinct odd values. Are they all distinct? 1, 3, 5, ..., 1005: yes, 503 distinct odd numbers, all in [1,1005], all < 1006, so distinct mod 1006. 

So m = 502 works! k = 1007 + 502 = 1509.

Wait, let me double-check this. With m = 502, w_j = 2u_j = 2(503+j) = 1006 + 2j, for j=1..502. So w_j = 1008, 1010, 1012, ..., 2010. Vertices: 0,1,2,...,1006, 1008, 1010, 1012, ..., 2010. Total: 1007 + 502 = 1509 vertices.

Sides and sums:
- (i, i+1) for i=0..1005: sums 1, 3, 5, ..., 2011 (1006 odd sums, all odd residues mod 2012). ✓
- (1006, 1008): sum 2014 ≡ 2 mod 2012. 
- (1008, 1010): sum 2018 ≡ 6.
- (1010, 1012): sum 2022 ≡ 10.
- ...pattern: (1006+2j, 1006+2(j+1)) sum = 2012 + 4j + 2 ≡ 4j+2 mod 2012, for j=0..501 (where w_0 = 1006? No). Let me recompute.

Let me recompute the "gap" sides. The vertices after 1006 are w_1=1008, w_2=1010, ..., w_{502}=2010. Sides:
- (1006, w_1) = (1006, 1008): sum = 2014 ≡ 2.
- (w_1, w_2) = (1008, 1010): sum = 2018 ≡ 6.
- (w_2, w_3) = (1010, 1012): sum = 2022 ≡ 10.
- ...
- (w_{501}, w_{502}) = (2010-2, 2010) = (2008, 2010): sum = 4018 ≡ 4018 - 2·2012 = 4018 - 4024 = -6 ≡ 2006. Let me recompute: 2008 + 2010 = 4018. 4018 mod 2012: 4018 - 2012 = 2006, 2006 - 2012 < 0, so 2006. So sum ≡ 2006.
- (w_{502}, 0) = (2010, 0): sum = 2010.

Let me list the gap sums mod 2012:
- (1006, 1008): 2014 ≡ 2
- (1008, 1010): 2018 ≡ 6
- (1010, 1012): 2022 ≡ 10
- In general (w_j, w_{j+1}) = (1006+2j, 1008+2j): sum = 2014 + 4j ≡ 2 + 4j mod 2012, for j=1..501.
  - j=1: 6, j=2: 10, ..., j=501: 2 + 4·501 = 2006.
- (w_{502}, 0) = (2010, 0): 2010.

So gap sums = {2} ∪ {6, 10, 14, ..., 2006} ∪ {2010}.

{6, 10, ..., 2006}: these are 2 + 4j for j=1..501 = 6, 10, ..., 2006. That's 501 values, ≡ 2 mod 4, from 6 to 2006.

So gap sums = {2} ∪ {6,10,...,2006} ∪ {2010} = {2, 6, 10, 14, ..., 2006, 2010}.

Is 2010 in {6,10,...,2006}? 2010 = 2 + 4·502, but j goes up to 501 giving 2006. So 2010 is not in the set {6,...,2006}. And 2 is separate. So gap sums = {2, 6, 10, ..., 2006, 2010} = {2, 6, 10, ..., 2010} = numbers ≡ 2 mod 4 from 2 to 2010. That's (2010-2)/4 + 1 = 503 values. All ≡ 2 mod 4, distinct.

Block sums = {1, 3, 5, ..., 2011} = all odd residues (1006 values).

Gap sums = {2, 6, 10, ..., 2010} = all residues ≡ 2 mod 4 (503 values).

Total sums = odd residues ∪ {≡2 mod 4 residues} = 1006 + 503 = 1509 distinct residues. No overlaps (odd vs even). ✓

So k = 1509 works! All 1509 sums distinct mod 2012.

Can we do even better? The used residues are: all odd (1006) + all ≡2 mod 4 (503) = 1509. Remaining: residues ≡ 0 mod 4 (503 values: 0, 4, 8, ..., 2008). Can we use some of those too?

To get sums ≡ 0 mod 4, we'd need sides with sum ≡ 0 mod 4. Currently the block gives odd sums, gap gives ≡2 mod 4. To add more vertices giving ≡0 mod 4 sums...

Hmm, but we've used all available vertices in the far arc (1008 to 2010 even). The odd vertices in the far arc (1007, 1009, ..., 2011) are not used. There are 503 of them. Can we incorporate some?

If we add an odd vertex, say 1007, between 1006 and 1008: then sides change. (1006,1007) sum 2013≡1, (1007,1008) sum 2015≡3. But 1 and 3 are already in block sums! Collision. So inserting odd vertices into the block region causes collisions.

What if we add odd vertices in the far arc but rearrange? Let me think differently.

Actually, the construction used: block 0..1006 (consecutive), then even vertices 1008..2010. The unused vertices are the odd ones in (1006, 2012): 1007, 1009, ..., 2011 (503 vertices). 

To use them, we'd need to interleave or place them somewhere, but any side involving an odd vertex in the far arc paired with another odd vertex gives even sum, paired with even gives odd sum (collision with block).

Let me think: if we place odd vertices w among the even ones in the far arc, sides between odd-odd give even sums (could be ≡0 mod 4 or ≡2 mod 4), odd-even give odd sums (collision with block's odd sums unless we free up some odd residues).

This is getting complicated. Let me think about the upper bound.

Upper bound: We need k distinct sums mod 2012. The sums are s_i = v_i + v_{i+1}. 

Let me think about the constraint Σ s_i = 2Σ v_i mod 2012. And the alternating sum for even k.

Actually, let me think about an upper bound of 1509. Hmm, is 1509 the answer? Let me check if we can exceed it.

Let me think about the total count. We have 2012 vertices. We're using 1509. Can we use more?

Let me think about the upper bound via mod 4. The sums mod 4 can be 0, 1, 2, 3. Each residue class mod 4 has exactly 503 residues mod 2012. So #sums ≡ r mod 4 ≤ 503 for each r. Total k ≤ 4·503 = 2012. Not helpful alone.

But there's a structural constraint. Let me think about the sums mod 4 in terms of the vertices mod 4.

s_i = v_i + v_{i+1} mod 4. Let n_r = number of vertices ≡ r mod 4, for r=0,1,2,3. Σ n_r = k.

The number of sides with sum ≡ 0 mod 4 = # of (v_i, v_{i+1}) pairs with v_i + v_{i+1} ≡ 0 mod 4 = pairs (0,0) and (1,3) and (2,2) and (3,1). In the cyclic sequence, this is a complex count depending on arrangement.

This is getting very involved. Let me think about whether 1509 is actually the max or if we can do better.

Let me reconsider. Maybe I can use all 2012 vertices minus some. Let me think about the theoretical max.

Actually, let me reconsider the problem. Let me think about the upper bound using the following:

Consider the k sides with sums s_1, ..., s_k, all distinct mod 2012. Note that s_i = v_i + v_{i+1}, so v_{i+1} = s_i - v_i. Then v_{i+2} = s_{i+1} - v_{i+1} = s_{i+1} - s_i + v_i. In general, v_{i+j} = v_i + (s_{i+1} - s_i) + (s_{i+3} - s_{i+2}) + ... hmm, let me think.

v_{i+1} - v_i = s_i - 2v_i. Not clean. 

Alternatively: v_{i+2} - v_i = s_{i+1} - s_i... no. s_{i+1} - s_i = (v_{i+1}+v_{i+2}) - (v_i + v_{i+1}) = v_{i+2} - v_i. Yes! So v_{i+2} - v_i = s_{i+1} - s_i.

So the "skip-one" differences are determined by consecutive sum differences. Since v_{i+2} - v_i must be nonzero mod 2012 (vertices distinct) and the v_i are distinct... 

Also, going around: v_{i+2} - v_i = s_{i+1} - s_i. Summing over all i (both parities):
- For k even: Σ_{i odd} (v_{i+2} - v_i) = 0 (telescopes around the even-indexed cycle), so Σ_{i odd} (s_{i+1} - s_i) = 0. Similarly for even i. This gives the alternating sum = 0 constraint again.
- For k odd: the skip-one goes around all vertices in one cycle of length k.

Hmm. Let me think about the upper bound differently.

Let me consider: the map i ↦ s_i is an injection into Z_{2012}. Also, v_{i+2} - v_i = s_{i+1} - s_i. The v_i are distinct mod 2012. 

Consider the two subsequences: even-indexed vertices v_2, v_4, ... and odd-indexed v_1, v_3, .... For k even, these are two cycles each of length k/2. The differences within each subsequence are s_{i+1} - s_i.

Actually, let me step back and think about whether we can beat 1509.

Let me try to construct a larger example. The key realization: the block 0..1006 uses all odd sum-residues. The even vertices 1008..2010 use all ≡2 mod 4 sum-residues. Can we also use ≡0 mod 4 sum-residues?

To get a sum ≡ 0 mod 4, we need v_i + v_{i+1} ≡ 0 mod 4. Options: (0,0), (2,2), (1,3), (3,1) mod 4.

Currently, the block 0..1006 has vertices of all parities mod 4. The far even vertices 1008..2010 are all even (≡ 0 or 2 mod 4). 

What if instead of the simple block + evens, we use a more clever arrangement?

Let me think about the theoretical maximum. We have 2012 residues for sums. The constraint is that the sums come from a valid polygon (distinct vertices, cyclic order). 

Let me think about an upper bound. Consider the following: for each residue r mod 2012, the "direction" r. A side has direction r = v_i + v_{i+1}. Note that if we use direction r, then the side connects two vertices summing to r. 

Hmm, let me think about the constraint from the fact that vertices are distinct. 

Actually, let me think about it as follows. We have k vertices and k sides. Each side uses a distinct direction. Consider the "antipodal" pairing of directions: direction r and direction r+1006. These are NOT parallel (different mod 2012). But geometrically, direction r and r+1006 correspond to chords perpendicular to bisectors that are antipodal—so the chords are parallel! Wait no. Let me recheck.

Direction r means bisector at angle πr/2012 (since (θ_a+θ_b)/2 = π(a+b)/2012 = πr/2012). Direction r+1006 means bisector at π(r+1006)/2012 = πr/2012 + π/2. So the chords are perpendicular to bisectors differing by π/2, meaning the chords differ in direction by π/2 — they're perpendicular, not parallel. OK so r and r+1006 are perpendicular directions. Fine.

So there's no antipodal pairing issue. The 2012 directions are all distinct directions (well, 2012 directions mod 2012, but direction 0 and direction 2012 are the same, which is why we work mod 2012). Actually there are 2012 distinct directions (for 2012-gon), since direction r for r=0,...,2011 are all distinct (chords at 2012 different angles). Wait, but a chord and the same chord reversed have the same direction. And direction r corresponds to bisector angle πr/2012. For r and r' to give the same chord direction, need πr/2012 ≡ πr'/2012 mod π, i.e., r ≡ r' mod 2012. So yes 2012 distinct directions. Good.

So theoretically k could be up to 2012, but the polygon structure prevents it.

Let me think about the real upper bound. Let me consider the sum of all s_i: Σ s_i = 2Σ v_i mod 2012. The s_i are k distinct residues. Σ v_i is the sum of k distinct residues (the vertices). 

Hmm, let me think about the problem from the competition answer perspective. This is a competition problem (likely Russian olympiad or similar, given 2012). The answer is probably a clean number. 1509 = 3·503. Hmm, 1007 = 1007, 1509 = 3·503. Let me reconsider.

Wait, 2012 = 4·503. 1509 = 3·503. 1006 = 2·503. 503 is prime. So 1509 = 3·503 = 3·2012/4. 

Let me see if we can get to 2012 - 503 = 1509 or beyond. Actually 1509 = 2012 - 503. And we're leaving out 503 vertices (the odd ones in the far arc). Can we include some of them?

Let me try to include a few odd vertices and see if sums can be made distinct.

Suppose we use all 2012 vertices except we remove some to break parallel sides. With all 2012 vertices (full 2012-gon), the sums are s_i = (i-1) + i = 2i-1 for the side from vertex i-1 to vertex i... wait let me use 0-indexed. Vertices 0,1,...,2011. Side (i, i+1) for i=0..2010 has sum 2i+1, and side (2011, 0) has sum 2011. So sums = {1, 3, 5, ..., 4021, 2011} mod 2012. 2i+1 for i=0..2010: 1, 3, ..., 4021. Mod 2012: 1,3,...,2011, then 2013≡1, 2015≡3, ..., 4021 = 2·2010+1 = 4021, 4021 mod 2012 = 4021 - 2012 = 2009. So the values 1,3,...,2011,1,3,...,2009. So residues 1,3,...,2011 appear, with 1,3,...,2009 appearing twice and 2011 appearing once. And 2011 from the last side. So lots of duplicates. The full 2012-gon has many parallel sides (opposite sides are parallel: side (i,i+1) and side (i+1006, i+1007) have sums 2i+1 and 2i+2013 ≡ 2i+1 mod 2012, parallel).

So with all 2012 vertices, we get only 1006 distinct directions (each appearing twice). To get more distinct directions, we remove vertices to break the symmetry.

Each vertex removal can potentially break some parallel pairs. Let me think: in the full 2012-gon, the 1006 pairs of parallel sides are {(i,i+1), (i+1006, i+1007)} for i=0..1005. To break all 1006 pairs, we need to remove at least one vertex from each pair. Removing vertex j breaks all pairs involving j, i.e., pairs {(j-1,j), (j+1005, j+1006)} and {(j, j+1), (j+1006, j+1007)}. So removing vertex j breaks 2 pairs (the pair containing side (j-1,j) and the pair containing side (j,j+1))... actually each vertex is in 2 sides, and each side is in 1 parallel pair, so removing a vertex breaks 2 parallel pairs (unless the two sides are in the same pair, which happens if the polygon has only... no). 

Wait, but removing a vertex also creates a new side (merging two sides into one), which might create new parallelisms. So it's not simply about breaking pairs.

This is the key difficulty. Let me think about it as: we want to choose a subset S of vertices, |S| = k, such that the polygon on S has all distinct side-sums. 

Let me think about the upper bound via the following approach:

Consider the k side-sums s_1, ..., s_k, distinct mod 2012. I'll derive a constraint.

Note: v_{i+2} - v_i = s_{i+1} - s_i (mod 2012). The vertices v_1, v_3, v_5, ... (odd-indexed) form a sequence where consecutive terms differ by s_{i+1} - s_i. For these to be distinct mod 2012 (they're a subset of vertices), and similarly for even-indexed.

For k even: the odd-indexed vertices v_1, v_3, ..., v_{k-1} form a cycle of length k/2 (since v_{k+1} = v_1). The differences are s_2 - s_1, s_4 - s_3, ..., s_k - s_{k-1}. These k/2 differences sum to 0 mod 2012 (cycle). Similarly even-indexed: differences s_3 - s_2, ..., s_1 - s_k (wrapping), summing to 0.

The odd-indexed vertices are distinct, so the partial sums of these differences are all distinct mod 2012 (they're k/2 distinct vertices). Similarly for even-indexed.

So we need: k/2 distinct residues (differences d_j = s_{2j} - s_{2j-1}) whose partial sums (starting from v_1) are all distinct mod 2012. The partial sums being distinct means we need k/2 ≤ 2012 (trivially true). But also the differences are determined by the s_i.

Hmm, this reformulation might help. Let me think of it as: we need two sequences (odd and even indexed vertices), each a "cycle" of distinct residues, with the side-sums being s_{2j-1} = v_{2j-1} + v_{2j} and s_{2j} = v_{2j} + v_{2j+1}.

This is getting complicated. Let me just try to determine if 1509 is optimal or if we can do better, by attempting a construction with more vertices.

Let me try to use all vertices except a minimal set. 

Construction attempt: Use vertices 0, 1, ..., 1006 (block) and 1008, 1010, ..., 2010 (even far), and additionally some odd far vertices.

If I add odd vertex 1007: it goes between 1006 and 1008 in the circular order. New sides: (1006, 1007) sum 2013 ≡ 1, and (1007, 1008) sum 2015 ≡ 3. But 1 and 3 are already used (block sums). Collision! So can't simply insert 1007.

What if I remove some block vertices to free up odd sum-residues? E.g., remove vertex 0 from the block. Then the block becomes 1, 2, ..., 1006, and the side (1006, 1008) ... wait, this changes things. Let me think.

Actually, removing vertex 0: the block was 0,1,...,1006. Without 0, it's 1,...,1006, and the polygon connects ... 2010 → 1 (instead of 2010 → 0 → 1). Wait, the full vertex set is {1,2,...,1006} ∪ {1008,1010,...,2010}. In circular order: 1, 2, ..., 1006, 1008, 1010, ..., 2010. Sides:
- (1,2), (2,3), ..., (1005,1006): sums 3, 5, ..., 2011. (1005 sides, odd sums from 3 to 2011)
- (1006, 1008): sum 2014 ≡ 2.
- (1008,1010),...,(2008,2010): sums 6, 10, ..., 2006. (501 sides)
- (2010, 1): sum 2011.

Wait, (2010, 1): sum = 2011. But 2011 is already in the block sums (3,5,...,2011)! Collision.

Hmm. So removing 0 and adding 1007 doesn't straightforwardly work.

This is getting complicated. Let me think about the upper bound more carefully.

Let me reconsider. Let me think about the problem in terms of the following clean model:

We choose k vertices. The side-sums are s_i = v_i + v_{i+1} mod 2012, all distinct. 

Upper bound idea: Consider the k side-sums. They are distinct mod 2012. Now, note that:
s_i + s_{i+1} = v_i + 2v_{i+1} + v_{i+2} ≡ v_i + v_{i+2} (mod 2).
And s_i - s_{i+1} = v_i - v_{i+2}.

Hmm. Let me think about the following: the side sums s_i and the "diagonal sums" v_i + v_{i+2} = s_i + s_{i+1} - 2v_{i+1}... not clean.

Let me try yet another approach to the upper bound. 

Consider the 2012 directions. Each direction r corresponds to chords perpendicular to bisector at angle πr/2012. A side of our polygon uses direction s_i. 

Now, consider the following: pair up the directions into 1006 pairs {r, r+1006} (perpendicular pairs). Hmm, not sure.

Let me think about the problem as a whole. Let me reconsider: maybe the answer is 1509 and the upper bound is 1509.

Upper bound attempt for k ≤ 1509:

Consider the k vertices. Each vertex v has a "successor" v' (next vertex in polygon). The side-sum is v + v'. Consider the map f: v ↦ v + v' (mod 2012), which is an injection (since all side-sums distinct). 

Consider the "doubled" vertices: for each vertex v, consider 2v mod 2012. Note that 2v mod 2012 takes values in even residues, and 2v = 2w mod 2012 iff v ≡ w mod 1006. So the map v ↦ 2v is 2-to-1 (v and v+1006 map to the same).

Now, s_i = v_i + v_{i+1} = 2v_i + (v_{i+1} - v_i) = 2v_i + d_i where d_i = v_{i+1} - v_i. Also s_i = 2v_{i+1} - d_i. So s_i ≡ 2v_i + d_i ≡ 2v_{i+1} - d_i mod 2012. Adding: 2s_i ≡ 2v_i + 2v_{i+1} mod 2012, which is trivial.

Subtracting: 0 ≡ 2d_i - ... hmm. s_i - 2v_i = d_i. So d_i = s_i - 2v_i. And d_i > 0 (in the circular order sense), Σ d_i = 2012.

Hmm, let me think about the number of vertices mod 1006. The vertices come in antipodal pairs {v, v+1006}. There are 1006 such pairs. If both v and v+1006 are in our vertex set, then... their side-sums involve them. 

Let me think about antipodal vertices. If v and v+1006 are both chosen, say v = v_i and v+1006 = v_j. Then s_i = v_i + v_{i+1} and s_{j-1} = v_{j-1} + v_j = v_{j-1} + v_i + 1006. And s_j = v_j + v_{j+1} = v_i + 1006 + v_{j+1}. 

Hmm, not immediately leading to a parallel pair.

Let me think about it differently. Consider two sides that are "antipodal" in the polygon: side i and side i + k/2 (if k even). Their sums s_i and s_{i+k/2}. Not necessarily related.

OK let me try a completely different approach to the upper bound. Let me think about the problem as a Sidon set / additive combinatorics problem.

We need: v_1, ..., v_k distinct mod 2012, and s_i = v_i + v_{i+1} distinct mod 2012.

Consider the set V = {v_1, ..., v_k} and the set S = {s_1, ..., s_k} = {v_i + v_{i+1}}. |S| = k (all distinct). 

Now, the sums v_i + v_{i+1} are "consecutive pair sums" in the cyclic order. 

Let me think about the relationship between V and S. Note that S ⊂ V + V (sumset). |V + V| can be up to 2k-1 (if V is an arithmetic progression) or more. But we need |S| = k specific sums to be distinct.

Hmm. Let me think about the upper bound via the following clever observation:

Consider the k side-sums s_i, all distinct mod 2012. Consider also the k "other sums" t_i = v_i + v_{i+2} (sums of next-nearest neighbors). Note t_i = s_i + s_{i+1} - 2v_{i+1}... not clean. But t_i = v_i + v_{i+2} and s_i = v_i + v_{i+1}, s_{i+1} = v_{i+1} + v_{i+2}, so t_i = s_i + s_{i+1} - 2v_{i+1}... wait: s_i + s_{i+1} = v_i + 2v_{i+1} + v_{i+2} = t_i + 2v_{i+1}. So t_i = s_i + s_{i+1} - 2v_{i+1}.

Not obviously useful. Let me try to think about the answer being 1509 and find an upper bound proof.

Actually, wait. Let me reconsider the construction. We got 1509 = 1007 + 502. But maybe we can do better with a different construction. Let me think about using three "blocks" or a different pattern.

Let me reconsider. The construction used:
- Block A: 0, 1, ..., 1006 (consecutive). Side-sums: all odd residues (1006 of them).
- Block B: 1008, 1010, ..., 2010 (even, step 2). Side-sums within B and connecting to A and back: all ≡ 2 mod 4 residues (503 of them).

Total distinct sums: 1006 + 503 = 1509. Used residues: odd + ≡2 mod 4 = 1006 + 503 = 1509. Unused: ≡ 0 mod 4 (503 residues).

To use ≡ 0 mod 4 residues, I'd need sides with sum ≡ 0 mod 4. 

What if I use a block of vertices ≡ 0 mod 4? E.g., vertices 0, 4, 8, .... But 0 is already in block A.

Let me think about a completely different construction. 

Idea: Use three blocks to cover three residue classes mod 4 of the sums.

Hmm, but the sums' residue mod 4 depends on both endpoints. Let me think about what vertex arrangements give which sum residues.

Actually, let me think about the upper bound. I'll try to prove k ≤ 1509.

Claim: k ≤ 1509 = 3·503.

Proof attempt: Consider the side-sums mod 4. Let a_r = number of sides with sum ≡ r mod 4, for r = 0,1,2,3. Then a_0 + a_1 + a_2 + a_3 = k, and a_r ≤ 503 for each r (since each residue class mod 4 has 503 elements mod 2012, and sums are distinct). So k ≤ 2012. Need a stronger bound.

Now, the side-sums mod 4 relate to vertices mod 4. Let n_r = number of vertices ≡ r mod 4. The side from v_i to v_{i+1} has sum ≡ (v_i + v_{i+1}) mod 4. 

Consider the sides with odd sum (≡ 1 or 3 mod 4): these connect vertices of different parities (one even, one odd). The number of such sides = number of parity changes = 2t (even). a_1 + a_3 = 2t.

Sides with even sum (≡ 0 or 2 mod 4): connect same-parity vertices. a_0 + a_2 = k - 2t.

Now, a_1 + a_3 = 2t ≤ 1006 (odd residues: 1,3,5,...,2011, that's 1006, split into ≡1 mod 4 (503) and ≡3 mod 4 (503)). So a_1 ≤ 503, a_3 ≤ 503, a_1 + a_3 ≤ 1006.

a_0 + a_2 = k - 2t. a_0 ≤ 503, a_2 ≤ 503, so a_0 + a_2 ≤ 1006.

So k = (a_0 + a_2) + (a_1 + a_3) ≤ 1006 + 1006 = 2012. Still 2012.

Hmm. Need a tighter bound. Let me think about the relationship between a_0, a_2 and the vertex counts.

Sides with sum ≡ 0 mod 4: (0,0), (2,2) mod 4 pairs. Sides with sum ≡ 2 mod 4: (0,2), (2,0) mod 4 pairs. So a_0 = #(0→0) + #(2→2), a_2 = #(0→2) + #(2→0). And a_0 + a_2 = #(even→even) = number of same-even-parity sides.

Similarly a_1 = #(0→1) + #(2→3), a_3 = #(1→0) + #(3→2) [sums ≡ 3: (1,2),(3,0)... wait let me recompute. Sum ≡ 1 mod 4: (0,1),(1,0),(2,3),(3,2). Sum ≡ 3 mod 4: (0,3),(3,0),(1,2),(2,1).]

This is getting complicated. Let me think about whether there's a cleaner upper bound argument.

Alternative upper bound approach: Think about the vertices and their antipodes.

For each vertex v in our set, its antipode is v + 1006 mod 2012. Consider the 1006 antipodal pairs. Let's say our k vertices occupy some pairs fully (both vertices) and some partially (one vertex). Let p = number of fully occupied pairs, q = number of partially occupied pairs. Then k = 2p + q, and p + q ≤ 1006.

Now, if both v and v+1006 are vertices, consider the sides incident to them. Say v = v_i (successor v_{i+1}) and v+1006 = v_j (successor v_{j+1}). Then s_i = v + v_{i+1} and s_j = v + 1006 + v_{j+1}. These are parallel iff s_i ≡ s_j mod 2012, i.e., v_{i+1} ≡ v_{j+1} + 1006 mod 2012, i.e., v_{i+1} and v_{j+1} are antipodal. 

So if v and v+1006 are both vertices, AND their successors are antipodal, then we get parallel sides. To avoid this, for each fully occupied antipodal pair {v, v+1006}, the successors of v and v+1006 must NOT be antipodal.

Hmm, this gives a constraint but I'm not sure it directly bounds k.

Let me think about it more carefully. Actually, let me think about the following: 

For each side (v_i, v_{i+1}) with sum s_i, consider the "antipodal side" which would be (v_i + 1006, v_{i+1} + 1006) with sum s_i + 2012 ≡ s_i. So if both v_i, v_{i+1} and their antipodes v_i+1006, v_{i+1}+1006 are vertices, and moreover v_i+1006 and v_{i+1}+1006 are consecutive in the polygon (forming a side), then we have two parallel sides. But they might not be consecutive.

However, the side (v_i+1006, v_{i+1}+1006) has sum s_i, and if this side exists in the polygon, it collides with side (v_i, v_{i+1}). But (v_i+1006, v_{i+1}+1006) is a side only if v_i+1006 and v_{i+1}+1006 are consecutive vertices in our chosen set. 

So the constraint is: for no side (v_i, v_{i+1}) should the antipodal pair (v_i+1006, v_{i+1}+1006) also be a side. 

This means: the set of sides (as unordered pairs of consecutive vertices) should not contain both a side and its antipodal side. 

Let me think of the sides as chords. There are 2012 possible "side directions" (sums mod 2012). Each direction r corresponds to a set of chords: all chords (a, b) with a + b ≡ r mod 2012. For a fixed r, the chords with sum r are: (a, r-a) for a = 0, ..., 2011, but (a, r-a) = (r-a, a) so there are 1006 distinct chords (or 1006+1 if r is even and a = r/2 gives a degenerate... no, a ≠ r-a since that would mean 2a ≡ r, and the chord would be a point, not a side). Actually for r even, a = r/2 gives 2a = r, so a = r-a, degenerate (not a chord). So for r even, 1005 chords; for r odd, 1006 chords. Wait, let me recount. Chords with sum r: pairs {a, r-a mod 2012} with a ≠ r-a. a = r-a iff 2a ≡ r mod 2012. For r odd: 2a ≡ r has no solution (since 2a is even, r odd), so 1006 chords. For r even: 2a ≡ r mod 2012 has solutions a ≡ r/2 mod 1006, so a = r/2 and a = r/2 + 1006, giving 2 degenerate "chords" (points). So 1006 - 1 = 1005 actual chords. Hmm wait, the pairs {a, r-a}: as a ranges over 0..2011, each pair counted twice. Number of distinct pairs = 2012/2 = 1006, minus degenerate ones (where a = r-a). For r even, 2 degenerate, so 1006 - 2/2... no. Let me think again. The number of distinct unordered pairs {a, b} with a+b ≡ r, a ≠ b: total ordered pairs (a, r-a) is 2012 (a from 0 to 2011), each unordered pair counted twice, minus degenerate (a = r-a) counted once. For r odd: no degenerate, so 2012/2 = 1006 pairs. For r even: 2 degenerate values of a (a = r/2 and r/2 + 1006), contributing 2 degenerate "pairs" (singletons), so distinct non-degenerate pairs = (2012 - 2)/2 = 1005.

OK so each direction has about 1006 chords. Our polygon uses one chord per direction (at most). The constraint is that the chosen chords form a Hamiltonian cycle on the chosen vertices.

This is a complex combinatorial structure. Let me step back and think about whether 1509 is the answer or if there's a better construction.

Let me try to construct k > 1509. 

Let me try: use all even vertices (0, 2, 4, ..., 2010, that's 1006 vertices) plus some odd vertices.

All even vertices: 0, 2, 4, ..., 2010. In order. Sides: (0,2), (2,4), ..., (2008, 2010), (2010, 0). Sums: 2, 6, 10, ..., 4018, 2010. 4018 = 2·2012 - 6, so mod 2012: 2, 6, 10, ..., 2010, 2010-2012+... let me compute. (2i, 2i+2) sum = 4i+2 for i=0..1004 (vertices 0 to 2008): 2, 6, ..., 4·1004+2 = 4018 ≡ 4018 - 2012 = 2006. And (2010, 0) sum = 2010. So sums = {2, 6, 10, ..., 2006, 2010} = {2, 6, ..., 2010} = all ≡ 2 mod 4 residues (503 values). But there are 1006 sides and only 503 distinct sums! So lots of duplicates. Indeed (2i, 2i+2) and (2i+1006, 2i+1008) = (2(i+503), 2(i+504)) have the same sum mod 2012. So the all-even 1006-gon has parallel sides. Only 503 distinct directions.

So using all even vertices gives only 503 distinct sums. Bad.

Let me go back to the 1509 construction and think about whether it's optimal.

Actually, let me reconsider the construction. We have 1509 vertices using 1509 distinct sum-residues. The unused sum-residues are ≡ 0 mod 4 (503 of them). The unused vertices are the 503 odd vertices in the far arc (1007, 1009, ..., 2011).

To add more vertices, we'd need to use some of these 503 odd vertices, and the new sides would need to have sums ≡ 0 mod 4 (the only unused residues) or reuse... no, they must be distinct from existing, so ≡ 0 mod 4.

A side with sum ≡ 0 mod 4 connects vertices (0,0), (2,2), (1,3), or (3,1) mod 4. The new odd vertices are ≡ 1 or 3 mod 4. To get sum ≡ 0 mod 4 from a side involving a new odd vertex, we need the other endpoint ≡ 3 or 1 mod 4 respectively (i.e., odd-odd pair with complementary mod 4), or the other endpoint such that... (1,3) or (3,1) mod 4.

But the existing vertices include all of 0..1006 (which has all mod 4 classes) and even far vertices (≡ 0 or 2 mod 4). So to add an odd far vertex w (≡ 1 or 3 mod 4) and get a side with sum ≡ 0 mod 4, we'd connect it to a vertex ≡ 3 or 1 mod 4. The existing vertices ≡ 1 or 3 mod 4 are in the block 0..1006.

But inserting w into the polygon changes the side structure: it replaces a side (u, u') with two sides (u, w) and (w, u'), changing sums. This could disrupt the existing distinct sums.

This seems hard to do without breaking the construction. Let me think about whether 1509 is actually the maximum, or if a completely different construction does better.

Let me think about the upper bound from a different angle.

Upper bound via counting: Let's count the number of "forbidden" parallel pairs.

Actually, let me think about the following clean upper bound argument:

Lemma: k ≤ 1509.

Consider the k side-sums, all distinct mod 2012. Partition them by residue mod 4: a_0, a_1, a_2, a_3 with a_r ≤ 503.

Now I claim that a_0 + a_2 ≤ 1006 and a_1 + a_3 ≤ 1006 (already shown). But also, I claim a stronger bound. Let me think...

Consider the vertices mod 2. Let E = set of even vertices, O = set of odd vertices, |E| = e, |O| = o, e + o = k. Sides within E (even-even) have even sums, sides within O (odd-odd) have even sums, sides between E and O have odd sums. Number of odd-sum sides = 2t (parity changes). Number of even-sum sides = k - 2t.

Even-sum sides: these are sides within E or within O. A side within E connects two even vertices; its sum is even. A side within O connects two odd vertices; its sum is even. 

Now, the even-sum sides within E: there are some number, say c_E, of sides connecting consecutive even vertices (in the polygon). Similarly c_O for odd. c_E + c_O = k - 2t.

The even sums from E-sides: v + v' where v, v' even, so sum ≡ 0 or 2 mod 4. The even sums from O-sides: v + v' where v, v' odd, so sum ≡ 0 or 2 mod 4 (odd + odd = even). 

Hmm, I don't see a clean strengthening. Let me try to think about whether k = 1510 is possible.

Actually, let me just try to see if the answer might be 1509 by attempting to prove the upper bound k ≤ 1509 using the following approach:

Consider the 2012 points. Define the "reflection" map σ: x ↦ 1006 - x mod 2012 (reflection across the diameter through point 0 and point 1006). Wait, let me think about which reflection gives parallel sides.

Two sides (a,b) and (c,d) are parallel iff a+b ≡ c+d mod 2012. The map that sends a side to a parallel side: (a,b) ↦ (c,d) with c+d ≡ a+b. 

Consider the reflection ρ: x ↦ (a+b) - x mod 2012, which fixes the chord (a,b) (swaps a and b) and maps any point x to its reflection across the diameter perpendicular to... hmm.

Let me think about it differently. The direction r = a+b corresponds to the diameter at angle πr/2012 (the perpendicular bisector direction). The reflection across this diameter maps x ↦ r - x mod 2012. This reflection swaps a and b (since a + b = r, so r - a = b). 

A chord (c, d) with c + d = r is fixed (as a set) by this reflection. A chord (c,d) with c+d = r' is mapped to (r - c, r - d) with sum 2r - r'. 

Hmm, I don't think reflections directly help.

Let me try another approach to the upper bound. 

Consider the k sides as chords. Each chord (v_i, v_{i+1}) has a direction s_i = v_i + v_{i+1}. The directions are all distinct. Now, a chord with direction r has its midpoint at angle πr/2012 (the perpendicular bisector hits the circle at angle πr/2012 and the midpoint of the chord is along that radius). 

The midpoint of chord (a,b) is at angle π(a+b)/2012 = πr/2012, at distance cos(π(b-a)/2012) from center... the exact position doesn't matter. 

Now, the key constraint: the chords form a polygon, so they connect end-to-end. 

Let me think about the "winding" or total turning. The polygon's sides, in order, turn by angles related to the arc lengths d_i = v_{i+1} - v_i. The total turning is 2π (convex polygon). The direction of side i is πs_i/2012 + π/2 (mod π). The change in direction from side i to side i+1 is π(s_{i+1} - s_i)/2012 (mod π). But the actual turning angle is related to d_{i+1} (the arc subtended). Hmm, the exterior angle at vertex v_{i+1} is π·d_{i+1}/2012 · 2... 

Actually, the inscribed angle theorem: the exterior angle at v_{i+1} (turning from side (v_i, v_{i+1}) to side (v_{i+1}, v_{i+2})) equals the arc from v_i to v_{i+2} not containing v_{i+1}, divided by... The turning angle (exterior angle) at v_{i+1} is half the arc from v_i to v_{i+2} (the arc not containing v_{i+1}). The arc from v_i to v_{i+2} not containing v_{i+1} is 2012 - (d_i + d_{i+1}) (in units of arc-steps), so the exterior angle is π(2012 - d_i - d_{i+1})/2012. Hmm, that doesn't seem right for a convex polygon inscribed in a circle.

Wait, for a convex polygon inscribed in a circle, the interior angle at v_{i+1} is π - (exterior angle), and the exterior angle equals the arc from v_i to v_{i+2} (not through v_{i+1}) divided by 2R... Actually, the inscribed angle theorem: the angle at v_{i+1} subtended by the arc from v_i to v_{i+2} (the arc not containing v_{i+1}) is half that arc. The interior angle of the polygon at v_{i+1} is π minus the inscribed angle... no. 

Let me think again. The interior angle at v_{i+1} of the inscribed polygon equals half the arc from v_i to v_{i+2} that does NOT contain v_{i+1}. (Inscribed angle theorem: angle at a point on the circle = half the intercepted arc.) The intercepted arc is the one not containing the vertex. So interior angle = (arc from v_i to v_{i+2} not through v_{i+1}) / 2 = (2012 - d_i - d_{i+1}) · π / 2012. 

For the polygon to be convex, all interior angles < π, which means 2012 - d_i - d_{i+1} < 2012, i.e., d_i + d_{i+1} > 0, always true. And interior angle > 0 means 2012 - d_i - d_{i+1} > 0, i.e., d_i + d_{i+1} < 2012. Since d_i + d_{i+1} ≤ 2012 - (k-2) (as other d's are ≥ 1)... for k ≥ 3 this is fine. Actually d_i + d_{i+1} < 2012 as long as not all other d's are 0, which is true for k ≥ 3. So convexity is automatic for k ≥ 3 (any k distinct points on a circle form a convex k-gon). Good, so convexity is not a real constraint here.

OK so the only constraint is: distinct side-sums mod 2012. Let me get back to finding the max k.

Let me try to think about the upper bound by considering the following:

The side-sums s_1, ..., s_k are distinct mod 2012. The vertices v_1, ..., v_k are distinct mod 2012. We have v_{i+1} = s_i - v_i, so the entire polygon is determined by v_1 and the s_i's. Specifically:
v_2 = s_1 - v_1
v_3 = s_2 - v_2 = s_2 - s_1 + v_1
v_4 = s_3 - v_3 = s_3 - s_2 + s_1 - v_1
...
In general, v_{i+1} = (-1)^i v_1 + Σ_{j=1}^{i} (-1)^{i-j} s_j.

For the polygon to close: v_{k+1} = v_1, which gives:
v_1 = (-1)^k v_1 + Σ_{j=1}^{k} (-1)^{k-j} s_j
(1 - (-1)^k) v_1 = Σ_{j=1}^{k} (-1)^{k-j} s_j mod 2012.

If k is even: 0 = Σ (-1)^{k-j} s_j = Σ (-1)^j s_j (since k even, (-1)^{k-j} = (-1)^j). So Σ_{j=1}^k (-1)^j s_j ≡ 0 mod 2012, i.e., s_1 + s_3 + ... ≡ s_2 + s_4 + ... mod 2012. (Alternating sum = 0.)

If k is odd: 2v_1 = Σ (-1)^{k-j} s_j mod 2012. Since k odd, (-1)^{k-j} = (-1)^{1-j} = -(-1)^{-j} = -(-1)^j (since (-1)^{-j} = (-1)^j). So 2v_1 = -Σ (-1)^j s_j = Σ (-1)^{j+1} s_j mod 2012. This determines v_1 (mod 1006) from the s_i's. So for k odd, the alternating sum determines v_1 mod 1006, and there are 2 choices for v_1 mod 2012 (v_1 and v_1 + 1006).

Also, all v_i must be distinct mod 2012.

So the problem reduces to: choose k distinct residues s_1, ..., s_k mod 2012 (in a specific cyclic order) such that:
1. (If k even) alternating sum = 0 mod 2012.
2. The induced v_i (from v_1 and s_i's) are all distinct mod 2012.
3. The v_i are distinct from each other (and the s_i are the side-sums, which they are by construction).

Wait, but the s_i are ordered (cyclically), and different orderings give different polygons. So we need to find an ordering of k distinct residues such that the induced vertices are distinct.

This is a cleaner formulation. Let me think about the upper bound using this.

For k even: we need k distinct residues s_1, ..., s_k with alternating sum 0 mod 2012, and the induced v_i distinct. The alternating sum constraint means the k residues can be split into two sets A (odd positions) and B (even positions) with |A| = |B| = k/2, ΣA ≡ ΣB mod 2012.

The induced vertices: v_1, v_2 = s_1 - v_1, v_3 = s_2 - s_1 + v_1, etc. For these to be distinct mod 2012.

Hmm, the distinctness of v_i is the key constraint. Let me think about when v_i = v_j.

v_i = v_j iff (from the formula) the difference is 0. v_{i+1} - v_{i-1} = s_i - s_{i-1} - 2v_{i-1} + ... hmm. Actually, v_{i+1} - v_{i-1} = (s_i - v_i) - v_{i-1}... let me use the relation v_{i+2} - v_i = s_{i+1} - s_i (derived earlier). So v_{i+2} - v_i = s_{i+1} - s_i.

For the odd-indexed vertices v_1, v_3, v_5, ..., they form a sequence where v_{2j+1} - v_{2j-1} = s_{2j} - s_{2j-1}. For these to be distinct (as vertices), the partial sums must be distinct mod 2012.

Similarly even-indexed v_2, v_4, ... with v_{2j+2} - v_{2j} = s_{2j+1} - s_{2j}.

And no odd-indexed vertex equals an even-indexed vertex.

For k even, the odd-indexed vertices form a cycle of length k/2 (v_1, v_3, ..., v_{k-1}, and v_{k+1} = v_1). The differences s_2 - s_1, s_4 - s_3, ..., s_k - s_{k-1} sum to 0 (cycle closes). For the k/2 odd-indexed vertices to be distinct, the partial sums of these differences (starting from v_1) must be distinct mod 2012, and nonzero (except the full sum = 0). This is like requiring that the differences form a "cycle" that visits k/2 distinct residues.

The maximum length of such a cycle is 2012 (all residues), but the differences are constrained (they're s_{2j} - s_{2j-1} for distinct s_i). 

Hmm, this is still complex. Let me just try to determine the answer empirically by trying to beat 1509.

Let me try k = 1510. We need 1510 distinct sum-residues. By the mod 4 counting, a_0 + a_1 + a_2 + a_3 = 1510, each ≤ 503. So at least one a_r ≥ 503 (since 4·503 = 2012 ≥ 1510, actually 1510/4 = 377.5, so it's possible to have all ≤ 503). E.g., a_0 = 503, a_1 = 503, a_2 = 503, a_3 = 1. That's feasible by counting.

But the structural constraints might prevent it. Let me think about whether we can modify the 1509 construction to add one more vertex.

In the 1509 construction, unused sum-residues are ≡ 0 mod 4 (503 values: 0, 4, 8, ..., 2008). Unused vertices: 503 odd vertices 1007, 1009, ..., 2011.

To add one more vertex (say w, an odd far vertex) and get one more distinct sum (≡ 0 mod 4), we'd insert w into the polygon, replacing one side (u, u') with (u, w) and (w, u'), changing the sum from u+u' to u+w and w+u'. We need u+w and w+u' to be distinct from all other sums (including the removed u+u').

The removed sum u+u' frees up one residue. The two new sums u+w and w+u' must be distinct from each other and from all remaining sums. So we need 2 new distinct residues but only 1 freed + we need net +1. So we need u+w and w+u' to use the freed residue and one new (unused) residue.

The freed residue is u+u' (which was either odd or ≡2 mod 4 in our construction). The new sums u+w and w+u': w is odd, so if u is even, u+w is odd; if u is odd, u+w is even.

Case 1: Insert w between two even vertices u, u' (both in block or both in far-even). Then u+w and w+u' are both odd. The freed residue u+u' is even. So we use 2 odd residues (u+w, w+u') and free 1 even residue (u+u'). We need u+w, w+u' to be distinct odd residues not already used. But all odd residues are already used (block uses all 1006)! So u+w and w+u' would collide. Unless u+u' was odd... but u, u' both even means u+u' even. So can't do this.

Case 2: Insert w between two odd vertices. But our construction has odd vertices only in the block 0..1006, and they're consecutive there. Inserting w (a far odd vertex) between two block odd vertices would require w to be between them in circular order, but w is in the far arc. So not possible without rearranging.

Case 3: Insert w between an even and an odd vertex. Say u even, u' odd (or vice versa). Then u+w is odd (even+odd), w+u' is even (odd+odd). Freed residue u+u' is odd (even+odd). So we free an odd residue and need u+w (odd) and w+u' (even) to be new. u+w is odd: must be distinct from all used odd residues, but all odd residues are used! Unless u+w = u+u' (the freed one). u+w = u+u' iff w = u', but w ≠ u' (w is a far vertex, u' is a block vertex). So u+w is a "new" odd residue only if it equals the freed one, which requires w = u'. Contradiction. So u+w collides with an existing odd sum. Can't do this.

So the 1509 construction is "locally optimal" — can't add one vertex by simple insertion. But maybe a completely different construction does better?

Let me think about the upper bound. I'll try to prove k ≤ 1509.

Let me think about the following approach. Consider the side-sums mod 4. We have a_0 + a_1 + a_2 + a_3 = k with a_r ≤ 503.

Now consider the vertices mod 4. Let n_0, n_1, n_2, n_3 be the counts of vertices ≡ 0, 1, 2, 3 mod 4. Σ n_r = k.

The sides: a side from a vertex ≡ r to a vertex ≡ r' has sum ≡ r + r' mod 4. 

Let me count a_0 (sides with sum ≡ 0 mod 4): these are sides connecting (0,0), (1,3), (2,2), (3,1) mod 4. Let e_{rr'} = number of sides from a ≡ r vertex to a ≡ r' vertex. Then:
a_0 = e_{00} + e_{13} + e_{22} + e_{31}
a_1 = e_{01} + e_{10} + e_{23} + e_{32}
a_2 = e_{02} + e_{20} + e_{11} + e_{33}
a_3 = e_{03} + e_{30} + e_{12} + e_{21}

And the flow constraints: for each r, the number of sides leaving ≡ r vertices = n_r (each vertex has one outgoing side) and the number entering = n_r. So Σ_{r'} e_{rr'} = n_r and Σ_{r'} e_{r'r} = n_r.

This is a flow conservation constraint. The e_{rr'} form a "circulation" on the mod-4 classes.

Now, a_r ≤ 503 for each r. And k = Σ a_r. We want to maximize k.

Also, the number of sides with sum ≡ 0 mod 4 is a_0 = e_{00} + e_{22} + e_{13} + e_{31}. Note e_{00} ≤ n_0 (sides within class 0), e_{22} ≤ n_2, e_{13} ≤ n_1, e_{31} ≤ n_3. And e_{00} + e_{01} + e_{02} + e_{03} = n_0, etc.

Hmm, the constraint a_r ≤ 503 is already there. The flow constraints don't obviously reduce the max below 2012. Let me think about what additional constraint reduces it.

Wait, I think the key constraint I'm missing is: the side-sums are not just distinct mod 4, but distinct mod 2012. The mod 4 counting only uses a_r ≤ 503. But there might be a stronger constraint from mod 2 or the structure.

Let me reconsider. Maybe the answer is not 1509. Let me reconsider whether a different construction can beat 1509.

Let me try a construction based on three blocks to use three residue classes mod 4.

Idea: 
- Block A: consecutive vertices covering all odd sum-residues.
- Block B: vertices giving ≡ 2 mod 4 sum-residues.
- Block C: vertices giving ≡ 0 mod 4 sum-residues.

But the challenge is arranging them in a single polygon.

Let me think about a "three-arc" construction. Divide the circle into three arcs, each handled differently.

Hmm, this is getting really complex. Let me think about whether the answer is 1509 by trying to prove the upper bound.

Upper bound attempt: 

Consider the k vertices. Each vertex v_i has a successor v_{i+1} and predecessor v_{i-1}. The side-sums s_i = v_i + v_{i+1} are distinct mod 2012.

Consider the "second-order sums": v_i + v_{i+2} = s_i + s_{i+1} - 2v_{i+1}. Hmm, not clean. But v_{i+2} - v_i = s_{i+1} - s_i, so v_i + v_{i+2} = 2v_i + (s_{i+1} - s_i).

Let me think about the following: consider the multiset {v_i + v_{i+1} : i} (the side-sums, all distinct) and {v_i - v_{i+1} : i} (the side-differences, which are the d_i's, positive, summing to 2012). 

Note s_i + d_i = 2v_{i+1} and s_i - d_i = 2v_i. So 2v_i = s_i - d_i and 2v_{i+1} = s_i + d_i. Since v_i are distinct mod 2012, 2v_i are distinct mod 2012 only if no two v_i differ by 1006. If v_i and v_j differ by 1006, then 2v_i = 2v_j mod 2012.

Hmm. Let me think about the constraint that v_i are distinct. 2v_i = s_i - d_i. The values 2v_i mod 2012 are in the even residues (0, 2, ..., 2010), 1006 values, with v_i and v_i + 1006 mapping to the same. So the 2v_i take at most 1006 distinct values, meaning at most 1006 distinct v_i if no two are antipodal, or fewer if some are antipodal. But k can be up to 2012, so this doesn't bound k directly.

Let me try yet another approach. Let me think about the problem as a directed graph.

We have a directed Hamiltonian cycle on k vertices (subset of Z_{2012}). The "label" of each edge (v_i → v_{i+1}) is s_i = v_i + v_{i+1}. We need all labels distinct.

Consider the function f(v) = v + succ(v) where succ is the successor in the cycle. We need f to be injective on the vertex set.

Now, f(v) = v + succ(v). Note that f(v) = v + succ(v) and f(succ(v)) = succ(v) + succ(succ(v)). 

Consider the "antipodal" vertex v + 1006. If v + 1006 is also in the set, with successor w, then f(v+1006) = v + 1006 + w
