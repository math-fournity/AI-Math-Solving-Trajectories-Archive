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
  <problem_id>deepmath_103k_00000360</problem_id>
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

Consider the measurable spaces $(A, \mathcal{E}_A)$, $(B, \mathcal{E}_B)$, and $(C, \mathcal{E}_C)$. Let $f$ be a Markov kernel from $(A, \mathcal{E}_A)$ to $(B, \mathcal{E}_B)$, and let $g$ be a Markov kernel from $(A, \mathcal{E}_A)$ to $(C, \mathcal{E}_C)$. Define $h_a$ as the unique measure on $(B \times C, \mathcal{E}_B \otimes \mathcal{E}_C)$ such that \( h_a(E_B \times E_C) = f(a, E_B) \cdot g(a, E_C) \) for all $E_B \in \mathcal{E}_B$ and $E_C \in \mathcal{E}_C$. If we write $h(a, E) = h_a(E)$, determine whether $h$ is a Markov kernel from $(A, \mathcal{E}_A)$ to $(B \times C, \mathcal{E}_B \otimes \mathcal{E}_C)$. Specifically, is the map $a \mapsto h_a(E)$ a real-valued measurable function for all $E \in \mathcal{E}_B \otimes \mathcal{E}_C$?

## Standard Solution

Okay, so I need to figure out if h is a Markov kernel from A to B×C. The definition says that h_a is the unique measure on B×C such that for product sets E_B × E_C, h_a(E_B × E_C) = f(a, E_B) * g(a, E_C). Then h is defined by h(a, E) = h_a(E). To check if h is a Markov kernel, I need to verify two things: for each a in A, h(a, ·) is a probability measure on B×C, and for each E in the product sigma-algebra, the map a ↦ h(a, E) is measurable.

First part: h(a, ·) is a probability measure. Since h_a is defined as the product measure of f(a, ·) and g(a, ·), which are both probability measures (because f and g are Markov kernels), then h_a should indeed be a probability measure on the product space. The product of two probability measures is a probability measure, right? And uniqueness comes from the fact that the product sigma-algebra is generated by the rectangles, so by Caratheodory's extension theorem, the measure is uniquely determined by its values on the rectangles. So that part checks out.

The second part is the measurability. For each E in the product sigma-algebra, we need to show that a ↦ h_a(E) is measurable. The question is specifically about this measurability condition. So, the issue is whether for any E in the product sigma-algebra, the function that sends a to h_a(E) is measurable.

I know that when dealing with product measures, the sigma-algebra is generated by the rectangles E_B × E_C. So, first, we can consider the case where E is a measurable rectangle. For such E, h_a(E) = f(a, E_B) * g(a, E_C). Since f and g are Markov kernels, the maps a ↦ f(a, E_B) and a ↦ g(a, E_C) are measurable functions. The product of measurable functions is measurable, so a ↦ h_a(E_B × E_C) is measurable. That's good for rectangles.

But the sigma-algebra isn't just rectangles; it's all the sets generated by them through countable unions, intersections, complements, etc. So we need to check whether the measurability holds for all such sets. Maybe we can use the pi-system lambda-system theorem. Let’s define the collection of sets E in the product sigma-algebra for which a ↦ h_a(E) is measurable. We know that this collection contains all the rectangles, which form a pi-system. If we can show that this collection is a lambda-system, then by the pi-lambda theorem, it would contain the entire sigma-algebra.

So let's check the lambda-system properties. First, the entire space B×C is a rectangle, so it's in the collection. Second, if E and F are in the collection and E ⊆ F, then F \ E should be in the collection. Since h_a(F \ E) = h_a(F) - h_a(E), and the difference of measurable functions is measurable, this should hold. Third, if E_n is an increasing sequence of sets in the collection, then the union should be in the collection. Because h_a is a measure, h_a(∪E_n) = lim h_a(E_n), and the limit of measurable functions is measurable. Therefore, the collection is a lambda-system. Since it contains the pi-system of rectangles, it must contain the entire sigma-algebra. Therefore, the function a ↦ h_a(E) is measurable for all E in the product sigma-algebra.

Therefore, h is a Markov kernel from A to B×C.

Wait, but hold on. The user mentioned that h_a is the unique measure such that h_a(E_B × E_C) = f(a, E_B) * g(a, E_C). That is, h_a is the product measure of f(a, ·) and g(a, ·). So the key point is that h is the product of the two kernels. Then the question is whether this product is a Markov kernel. Since we have shown measurability in a for each E, then yes. So the answer is yes, h is a Markov kernel.

But let me check if there's a possible problem. For example, sometimes when dealing with product measures, the measurability in the space A might be an issue when moving beyond rectangles. But since we used the pi-lambda theorem, which extends the measurability from the rectangles to the entire sigma-algebra, that should take care of it. So unless there is some hidden non-measurability when dealing with the limits or differences, but in general, the set of E for which a ↦ h_a(E) is measurable should be a sigma-algebra. Since the rectangles generate the product sigma-algebra, and the set of such E is a sigma-algebra containing the rectangles, hence they must coincide.

Therefore, I think the answer is yes, h is a Markov kernel.

**Final Answer**
\boxed{Yes}
</think>

To determine if \( h \) is a Markov kernel from \( (A, \mathcal{E}_A) \) to \( (B \times C, \mathcal{E}_B \otimes \mathcal{E}_C) \), we need to verify two conditions: for each \( a \in A \), \( h(a, \cdot) \) is a probability measure, and for each \( E \in \mathcal{E}_B \otimes \mathcal{E}_C \), the map \( a \mapsto h_a(E) \) is measurable.

1. **Probability Measure**: Since \( h_a \) is defined as the product measure of \( f(a, \cdot) \) and \( g(a, \cdot) \), which are both probability measures (as \( f \) and \( g \) are Markov kernels), \( h_a \) is indeed a probability measure on \( (B \times C, \mathcal{E}_B \otimes \mathcal{E}_C) \).

2. **Measurability**: For each \( E \in \mathcal{E}_B \otimes \mathcal{E}_C \), we need to show \( a \mapsto h_a(E) \) is measurable. 
   - For measurable rectangles \( E_B \times E_C \), \( h_a(E_B \times E_C) = f(a, E_B) \cdot g(a, E_C) \). Since \( f \) and \( g \) are Markov kernels, \( a \mapsto f(a, E_B) \) and \( a \mapsto g(a, E_C) \) are measurable, and their product is measurable.
   - For the general case, consider the collection of sets \( E \) for which \( a \mapsto h_a(E) \) is measurable. This collection contains all rectangles (a \(\pi\)-system) and is closed under complements and countable unions (a \(\lambda\)-system). By the \(\pi\)-\(\lambda\) theorem, this collection is the entire \(\mathcal{E}_B \otimes \mathcal{E}_C \sigma\)-algebra.

Thus, \( h \) satisfies both conditions, making it a Markov kernel from \( (A, \mathcal{E}_A) \) to \( (B \times C, \mathcal{E}_B \otimes \mathcal{E}_C) \).

\[
\boxed{Yes}
\]

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. It's a classical descriptive set theory question.

The question: Let X and Y be Polish spaces, A ⊂ X a Borel subset. Suppose f: A → B ⊂ Y is a homeomorphism. Is B a Borel subset of Y?

This is the classical theorem about Borel isomorphisms and the fact that a homeomorphic image of a Borel set need not be Borel... wait, actually let me think carefully.

Actually, this is a subtle question. The answer is: Yes, B is Borel. This is a classical result in descriptive set theory.

Wait, let me reconsider. The question is whether a homeomorphic image of a Borel set in a Polish space is Borel.

Actually, this is NOT always true. There's a classical counterexample. The homeomorphic image of a Borel set need not be Borel. 

Hmm, but wait. Let me think more carefully. 

Actually, the key theorem here is: If f: A → B is a Borel isomorphism (bijection with f and f^{-1} both Borel measurable) between Borel subsets of Polish spaces, then B is Borel. This is a consequence of the Lusin-Suslin theorem.

But here f is a homeomorphism, which is stronger than a Borel isomorphism. A homeomorphism is in particular a Borel isomorphism. So by Lusin-Suslin, B is Borel.

Wait, but let me be careful. The Lusin-Suslin theorem states: If X, Y are Polish spaces, A ⊂ X is Borel, and f: X → Y is Borel measurable, then f(A) is... no, that's not quite right either.

Let me recall the precise statements.

**Lusin-Suslin Theorem**: Let X, Y be Polish spaces. If A ⊂ X is Borel and f: A → Y is injective and Borel measurable, then f(A) is Borel in Y.

Yes, this is the correct statement. Since f is a homeomorphism, it is in particular injective and Borel measurable (continuous functions are Borel measurable). Therefore, by the Lusin-Suslin theorem, B = f(A) is Borel in Y.

So the answer is: Yes, B is a Borel subset of Y.

Now let me write a complete proof. The proof of the Lusin-Suslin theorem is non-trivial. Let me recall the proof structure.

The proof typically goes through the following steps:

1. **Reduction to standard Borel spaces**: We can assume X = Y = ω^ω (Baire space) or work with general Polish spaces.

2. **Key lemma (Lusin's separation theorem / first separation principle)**: If A_n are analytic sets in a Polish space with pairwise disjoint, and their union is... hmm, let me recall the exact approach.

Actually, let me recall the standard proof of Lusin-Suslin more carefully.

The proof uses the theory of analytic sets. The key facts are:

1. Borel sets are analytic.
2. The image of an analytic set under a Borel measurable function is analytic.
3. **Lusin's separation theorem**: If A and B are disjoint analytic sets in a Polish space, there exists a Borel set C with A ⊂ C and C ∩ B = ∅.
4. **Lusin-Suslin theorem**: If f: A → Y is injective Borel (A Borel in Polish X, Y Polish), then f(A) is Borel.

The proof of (4) from (3): Since f is injective Borel and A is Borel (hence analytic), f(A) is analytic. Also, f(A) is the injective image. We need to show f(A) is Borel. 

The complement Y \ f(A) might not be analytic directly. But we can use the following: f(A) is analytic. If we can show Y \ f(A) is also analytic, then by Lusin's separation theorem applied to f(A) and Y \ f(A), we get that f(A) is Borel (since they can be separated by a Borel set, but they're complements, so the separating Borel set must equal f(A)).

Wait, actually Y \ f(A) being analytic is not obvious. Let me think again.

Actually, the standard proof is different. Let me recall.

**Proof of Lusin-Suslin**:

The key idea is to use the Lusin separation theorem in a more clever way, combined with a "rank" argument or a tree-based argument.

Let me recall the proof from Kechris's "Classical Descriptive Set Theory" or similar.

Actually, the standard proof goes like this:

**Step 1**: Show that if A is Borel in Polish X and f: A → Y is injective Borel, then f(A) is Borel.

The proof uses the following approach:

First, reduce to the case where X is a closed subset of ω^ω (or use the fact that every Borel set is the injective continuous image of a closed subset of ω^ω — but that's for analytic sets).

Actually, let me think about this differently. The cleanest proof I recall:

**Lemma (Lusin-Suslin)**: Let X, Y be Polish, A ⊂ X Borel, f: A → Y injective Borel. Then f(A) is Borel.

**Proof sketch**:

1. Since A is Borel, there exists a Polish topology on A (finer than the subspace topology) making A a Polish space. (By a theorem: every Borel subset of a Polish space is a Lusin space, i.e., there's a finer Polish topology.)

Actually, more precisely: every Borel subset of a Polish space is a Borel subset that can be given a Polish topology compatible with the Borel structure. This is the "Borel = Lusin" characterization.

2. With this Polish topology on A, f: A → Y is still Borel (since the Borel structure is the same). 

3. Now we have: A is Polish (with new topology), f: A → Y is injective Borel, Y is Polish.

4. **Graph theorem**: The graph of a Borel function from a Polish space to a Polish space is Borel. So graph(f) is Borel in A × Y.

5. The projection of graph(f) onto Y is f(A). But projection of Borel need not be Borel (it's analytic). So this alone doesn't work.

Hmm, let me try a different approach. Let me recall the actual proof.

**Actual proof of Lusin-Suslin** (from Kechris, Theorem 15.1):

The proof uses analytic sets and the separation theorem.

**Definition**: A set is analytic (Σ¹₁) if it's the projection of a closed set in X × ω^ω, or equivalently, the continuous image of a Borel set (or equivalently, the image of ω^ω under a Borel map).

**Key facts**:
- Borel ⊂ Analytic
- Continuous (hence Borel) images of analytic sets are analytic.
- **Souslin's theorem**: A set is Borel iff both it and its complement are analytic.
- **Lusin's separation theorem**: If A, B are disjoint analytic sets, there's a Borel set C with A ⊂ C, B ∩ C = ∅.

**Proof of Lusin-Suslin**:

Given: A Borel in Polish X, f: A → Y injective Borel, Y Polish.

1. f(A) is analytic (image of Borel under Borel map).

2. We need to show f(A) is Borel. By Souslin's theorem, it suffices to show Y \ f(A) is analytic.

3. To show Y \ f(A) is analytic: Y \ f(A) = {y ∈ Y : y ∉ f(A)}. 

Hmm, showing the complement is analytic is the tricky part. 

Actually, let me recall the proof more carefully. The proof doesn't directly show the complement is analytic. Instead, it uses a more refined argument.

**The actual proof** (Kechris 15.1):

The proof proceeds by showing that f(A) is Borel using the following strategy:

First, note that we can write A as a union of countably many Borel sets on each of which f is "nice" in some sense. 

Actually, let me recall the proof via the "good parameterization" approach.

Hmm, let me try to recall the proof from Moschovakis or Kechris more carefully.

**Kechris Theorem 15.1 (Lusin-Suslin)**: Let X, Y be Polish spaces, A ⊂ X Borel, and f: A → Y injective Borel. Then f(A) is Borel.

**Proof** (from Kechris):

The proof uses the following key ingredients:
- Analytic sets and their representation via trees
- The boundedness theorem
- Separation theorem

Let me try to reconstruct it.

**Step 1**: We can assume A is closed (in some Polish space). 

Actually, the standard approach: Since A is Borel, there's a continuous bijection g: ω^ω → A (if A is uncountable) or we can handle the countable case separately. Actually, every Borel set is the injective image of a closed subset of ω^ω under a continuous map. More precisely, every Borel set is a one-to-one continuous image of a closed subset of Baire space.

Wait, that's the property of being a "Lusin" space. Every Borel set in a Polish space is a Lusin space.

So: there exists a closed set F ⊂ ω^ω and a continuous bijection g: F → A.

Then f ∘ g: F → Y is injective Borel (in fact, Borel since g is continuous and f is Borel; actually f ∘ g is Borel as a composition of Borel functions, and g is continuous hence Borel).

Actually, f ∘ g: F → Y is injective and Borel. And F is closed in ω^ω, hence Polish (closed subset of Polish is Polish).

So we reduce to: F is Polish (closed in ω^ω), h: F → Y is injective Borel, Y is Polish. Show h(F) is Borel.

**Step 2**: Now F is Polish and h: F → Y is injective Borel. 

By the graph theorem, graph(h) is Borel in F × Y. Since h is injective, graph(h) is the graph of a bijection between F and h(F).

The projection π: F × Y → Y maps graph(h) bijectively onto h(F). 

Now, graph(h) is Borel in F × Y. We want to show that the injective projection of a Borel set is Borel. This is essentially what we're trying to prove, so this circular.

Let me try yet another approach.

**Approach via analytic sets and separation**:

The actual proof in Kechris uses the following:

1. f(A) is analytic.
2. For each Borel set C ⊂ A, f(C) is analytic (image of Borel under Borel = analytic).
3. Use the separation theorem cleverly.

Here's the key argument:

We want to show f(A) is Borel. Since f(A) is analytic, by Souslin's theorem it suffices to show Y \ f(A) is analytic.

Claim: Y \ f(A) is analytic.

To show this, we use the following: Y \ f(A) = {y ∈ Y : ∀x ∈ A, f(x) ≠ y}.

Hmm, this is a co-analytic condition, not obviously analytic.

Let me think about this differently. The actual proof is more subtle.

**The actual proof from Kechris (Theorem 15.1)**:

I'll try to recall the proof structure. Kechris proves it using the following:

First, he proves a lemma about Borel sets having "Borel uniformizations" or uses the theory of ranks on analytic sets.

Actually, I think the proof goes through the following key theorem:

**Theorem (Kechris 13.1 or similar)**: Every analytic set A in a Polish space can be written as A = ⋃_s A_s where {A_s} is a "Souslin scheme" with certain properties, and if A is Borel, the scheme has additional regularity.

Let me try a cleaner approach. I'll use the following well-known proof:

**Proof using the Lusin separation theorem**:

We prove: If A ⊂ X is Borel (X Polish) and f: A → Y is injective Borel (Y Polish), then f(A) is Borel.

**Key Lemma**: Let {B_n} be pairwise disjoint Borel subsets of A. Then {f(B_n)} are pairwise disjoint analytic sets, and by Lusin's separation theorem, there exist pairwise disjoint Borel sets {C_n} in Y with f(B_n) ⊂ C_n.

This is because: for each n, f(B_n) is analytic. The sets f(B_n) are pairwise disjoint (since f is injective). By Lusin's separation theorem (applied iteratively), we can find pairwise disjoint Borel sets C_n ⊃ f(B_n).

Wait, Lusin's separation theorem says: if A_1, A_2 are disjoint analytic, there's a Borel set B with A_1 ⊂ B, A_2 ∩ B = ∅. For countably many pairwise disjoint analytic sets, we can iteratively separate them.

**Main proof**:

We use induction on the "Borel complexity" of A. 

Actually, the cleanest proof I know uses the following:

**Proof**:

We prove the result by showing that the class of Borel sets A ⊂ X such that "for every injective Borel f: A → Y (Y Polish), f(A) is Borel" forms a σ-algebra containing all open sets. Since the Borel σ-algebra is the smallest such, the result follows for all Borel sets.

Wait, but this needs to be done carefully because we need to handle complements.

Let me try this approach:

Let 𝒞 = {A ⊂ X : A is Borel and for every Polish space Y and every injective Borel f: A → Y, f(A) is Borel in Y}.

We want to show 𝒞 contains all Borel sets.

**Step 1**: 𝒞 contains all open sets (and more generally all closed sets, and even all G_δ and F_σ sets... well, let's start with open sets).

If A is open in X, then A is itself a Polish space (open subset of Polish is Polish, with a compatible complete metric). So f: A → Y is an injective Borel map from a Polish space to a Polish space. 

Hmm, but we still need to show f(A) is Borel in this case. So this reduction doesn't immediately help.

Let me try the approach from Kechris more carefully.

Actually, I think the standard proof uses the following key idea:

**Proof (Lusin-Suslin)**:

We use the following facts:
1. Every Borel set in a Polish space is the image of ω^ω under an injective Borel map (actually, every Borel set is a one-to-one continuous image of a closed subset of ω^ω).
2. The Lusin separation theorem.

Here's the proof:

**Step 1**: Reduce to the case where A is a closed subset of ω^ω and f is continuous.

Since A is Borel in X (Polish), there exists a closed set F ⊂ ω^ω and a continuous bijection g: F → A. (This is a standard fact: every Borel set is a one-to-one continuous image of a closed subset of Baire space.)

Let h = f ∘ g: F → Y. Then h is injective and Borel (composition of Borel functions; g is continuous hence Borel, f is Borel). F is closed in ω^ω, hence Polish.

So we need: F Polish (in fact closed in ω^ω), h: F → Y injective Borel, Y Polish ⟹ h(F) is Borel.

**Step 2**: Now F is Polish and h: F → Y is injective Borel. 

By the graph theorem (a Borel function between Polish spaces has Borel graph), the graph Γ = {(x, h(x)) : x ∈ F} is Borel in F × Y.

Consider the projection π_Y: F × Y → Y. Then π_Y(Γ) = h(F). The projection is injective on Γ (since h is injective: if (x₁, h(x₁)) and (x₂, h(x₂)) project to the same y, then h(x₁) = h(x₂), so x₁ = x₂ by injectivity).

So h(F) is the injective image of a Borel set under a continuous projection. But we're going in circles—this is the same type of problem.

Let me try the actual proof from Kechris. I recall it uses the "rank" on analytic sets.

**Proof (Kechris, based on Theorem 15.1)**:

Actually, I think the cleanest self-contained proof uses the following approach:

**Theorem (Lusin-Suslin)**: Let X, Y be Polish, A ⊂ X Borel, f: A → Y injective Borel. Then f(A) is Borel.

**Proof**:

We use the following key tools:
(a) Analytic sets: A set is analytic if it's the continuous image of ω^ω (or equivalently, the projection of a closed set in X × ω^ω).
(b) Borel sets are analytic, and co-analytic sets (complements of analytic) are... well, co-analytic.
(c) **Souslin's theorem**: A set is Borel iff it is both analytic and co-analytic.
(d) **Lusin's separation theorem**: Disjoint analytic sets can be separated by Borel sets.
(e) **Perfect set theorem / boundedness**: Not directly needed.

The proof strategy:
1. f(A) is analytic (Borel image of Borel = analytic).
2. We show f(A) is co-analytic, i.e., Y \ f(A) is analytic.
3. By Souslin's theorem, f(A) is Borel.

So the key is step 2: showing Y \ f(A) is analytic.

**Showing Y \ f(A) is analytic**:

Y \ f(A) = {y ∈ Y : y ∉ f(A)} = {y ∈ Y : ∀x ∈ A, f(x) ≠ y}.

This is a co-analytic description. To show it's analytic, we need a more clever argument.

Here's the key idea: We use the fact that f is injective and Borel, and A is Borel, to "analytically" describe the complement.

Actually, I recall now. The proof doesn't go through showing the complement is analytic directly. Instead, it uses a different argument based on the structure of Borel sets.

Let me recall the proof from Kechris's book. The proof of Theorem 15.1 in Kechris uses the following:

**Proof (Kechris 15.1)**:

The proof is by induction on the complexity of the Borel set A, using the fact that Borel sets are built from open sets by countable unions and complements.

Actually, I think the proof uses the "good separation" property. Let me try to reconstruct it properly.

**Proof**:

We prove the following stronger statement by induction:

For every Borel set A ⊂ X (X Polish), and every injective Borel f: A → Y (Y Polish), f(A) is Borel in Y.

We use the fact that the class of Borel sets is the smallest class containing open sets and closed under countable disjoint unions and complements (relative to X). Actually, it's more convenient to use the following:

The Borel sets form the smallest σ-algebra containing the open sets. But for the inductive proof, we use a different characterization.

Actually, let me use the approach via the "Borel code" or the hierarchy.

Let me try the following clean approach that I'm more confident about:

**Proof using analytic sets and the separation theorem**:

We use the following well-known results:

**Fact 1**: If A ⊂ X is Borel (X Polish) and g: A → Z is Borel (Z Polish), then g(A) is analytic in Z.

**Fact 2 (Lusin's separation theorem)**: If A₁, A₂ are disjoint analytic subsets of a Polish space, there exists a Borel set B with A₁ ⊂ B and B ∩ A₂ = ∅.

**Fact 3 (Souslin's theorem)**: A subset of a Polish space is Borel iff it is both analytic and co-analytic.

**Main proof**:

We prove that f(A) is Borel by showing it's both analytic and co-analytic.

- f(A) is analytic: This is Fact 1 (A is Borel, f is Borel, so f(A) is analytic).

- f(A) is co-analytic, i.e., Y \ f(A) is analytic: This is the hard part.

To show Y \ f(A) is analytic, we use the injectivity of f and the following argument:

Since A is Borel in X, we can write A as a countable union of Borel sets of "bounded complexity." More precisely, we use the following:

**Claim**: For every Borel set A ⊂ X, there exist countably many closed sets F_n ⊂ X and a Borel set structure such that A can be "resolved" into a transfinite sequence of simpler sets.

Hmm, this is getting complicated. Let me try a different, more direct approach.

**Direct proof using the separation theorem**:

Here's a proof that I think works:

**Step 1**: Since A is Borel in X, there exists a sequence of Borel sets (A_s)_{s ∈ ω^{<ω}} (a Souslin scheme) such that:
- A = ⋃_{s ∈ ω^{<ω}} A_s (well, not exactly)
- Each A_s is Borel
- A_s ⊃ A_t when s ⊂ t (nested)
- A_s ∩ A_t = ∅ when s, t are incompatible (disjoint)
- A = ⋃_n A_{(n)} (first level covers A)
- ⋂_k A_{x|k} is a singleton for each x ∈ ω^ω with the corresponding property, or empty.

This is the "regular Souslin scheme" for a Borel set. Actually, this is getting too complicated.

Let me try the simplest proof I can think of.

**Simplest proof**:

We use the following theorem:

**Theorem (Lusin-Suslin, via analytic sets)**: 

*Proof*: 

We prove: if A is Borel in Polish X and f: A → Y is injective Borel (Y Polish), then f(A) is Borel.

The proof proceeds as follows:

1. **Reduction to closed domain**: Since A is Borel in X, by a standard result, there is a closed set F in ω^ω and a continuous bijection g: F → A. Let h = f ∘ g: F → Y. Then h is injective Borel, F is Polish (closed in ω^ω), and h(F) = f(A). So it suffices to prove: if F is Polish and h: F → Y is injective Borel, then h(F) is Borel.

2. **Graph is Borel**: By the graph theorem, Γ = graph(h) = {(x, h(x)) : x ∈ F} is Borel in F × Y.

3. **Key step**: We show that the projection of a Borel set with "countable sections" is Borel. More precisely, we use the following:

**Theorem (Lusin-Novikov)**: If B ⊂ X × Y is Borel (X, Y Polish) and every vertical section B_x = {y : (x,y) ∈ B} is countable, then the projection π_X(B) is Borel, and B has a Borel uniformization (there exist Borel functions selecting points from each nonempty section).

But in our case, the sections of Γ in the Y direction are: for each y, {x ∈ F : (x, y) ∈ Γ} = {x ∈ F : h(x) = y}, which is either a singleton (if y ∈ h(F)) or empty (if y ∉ h(F)). So every section is at most a singleton, hence countable.

By the Lusin-Novikov theorem (applied to Γ ⊂ F × Y, with sections in the F-direction being countable), the projection π_Y(Γ) = h(F) is Borel.

Wait, I need to be careful about the direction. The Lusin-Novikov theorem says: if B ⊂ X × Y is Borel and every section B_x (fixing x, varying y) is countable, then π_X(B) is Borel. 

In our case, Γ ⊂ F × Y. The sections of Γ:
- Fixing x ∈ F: Γ_x = {y ∈ Y : (x,y) ∈ Γ} = {h(x)}, a singleton. Countable. ✓
- Fixing y ∈ Y: Γ^y = {x ∈ F : (x,y) ∈ Γ} = {x ∈ F : h(x) = y}, which is a singleton or empty. Countable. ✓

The Lusin-Novikov theorem (in the direction we need): if B ⊂ X × Y is Borel and every section B^y = {x : (x,y) ∈ B} is countable, then π_Y(B) is Borel.

In our case, every section Γ^y is at most a singleton, so by Lusin-Novikov, π_Y(Γ) = h(F) is Borel. ✓

But wait, the Lusin-Novikov theorem itself is usually proved using the Lusin-Suslin theorem or similar tools. Is there a circularity issue?

Let me check: The Lusin-Novikov theorem is typically proved using the Lusin-Suslin theorem (or at least the separation theorem). So using Lusin-Novikov to prove Lusin-Suslin would be circular.

Hmm. Let me think about whether Lusin-Novikov can be proved independently.

Actually, the Lusin-Novikov theorem is a consequence of the Lusin-Suslin theorem in many presentations. So this approach might be circular.

Let me try yet another approach. Let me look at this from the perspective of the "first separation theorem" and build up.

Actually, let me just present the proof in the standard way, using the separation theorem for analytic sets, which is proved independently.

**Independent proof of the separation theorem**:

The Lusin separation theorem (first separation theorem) states: if A₁, A₂ are disjoint analytic sets in a Polish space, there's a Borel set B with A₁ ⊂ B, A₂ ∩ B = ∅.

This is proved using the representation of analytic sets via trees/Souslin operations, and doesn't require Lusin-Suslin.

**Souslin's theorem** (Borel = analytic ∩ co-analytic) is a direct consequence of the separation theorem: if A is both analytic and co-analytic, then A and A^c are disjoint analytic sets, so they can be separated by a Borel set B with A ⊂ B, A^c ∩ B = ∅, which means B = A, so A is Borel.

Now, to prove Lusin-Suslin, we need to show f(A) is co-analytic (since it's already analytic). The difficulty is showing Y \ f(A) is analytic.

Let me think about this more carefully.

**Showing Y \ f(A) is analytic**:

We have A Borel in X, f: A → Y injective Borel. We want to show Y \ f(A) is analytic.

Y \ f(A) = {y ∈ Y : ∀x ∈ A, f(x) ≠ y}.

The issue is that this has a universal quantifier over an uncountable set, which typically gives co-analytic, not analytic.

But the injectivity of f gives us something extra. Here's the key idea:

Since A is Borel, we can write A as a countable union of compact sets (if A is K_σ) or more generally, we can use the Borel structure.

Actually, here's a cleaner approach. Let me use the following:

**Approach via the "rank" on analytic sets**:

Every analytic set A ⊂ X can be represented as A = proj_X(C) where C is closed in X × ω^ω. For each x ∈ A, define the "rank" |x|_A = sup{|T_x| : T_x is the tree associated with x}, where T_x = {s ∈ ω^{<ω} : (x, s-something) ∈ C}... this is getting too technical.

Let me try a completely different, more elementary approach.

**Elementary proof using the structure of Borel sets**:

We prove the result by transfinite induction on the Borel rank of A.

**Base case**: A is open (or closed).

If A is open in X, then A is a Polish space (with a compatible complete metric). f: A → Y is injective Borel. We need to show f(A) is Borel.

Hmm, even this base case isn't trivial. Let me think...

If A is open and f: A → Y is injective continuous, then f(A) is... well, f is a homeomorphism onto its image (since f is injective continuous from A to f(A), and f^{-1}: f(A) → A is continuous if f is an open map, but continuous injective maps need not be open).

Wait, in our problem, f is a homeomorphism, not just continuous! So f: A → B is a homeomorphism, meaning f is bijective, continuous, and f^{-1} is continuous.

Oh wait, I just realized: the problem says f is a homeomorphism, not just Borel. A homeomorphism is much stronger. Let me re-read the problem.

"Suppose f: A → B ⊂ Y is a homeomorphism."

So f is a homeomorphism between A (with the subspace topology from X) and B (with the subspace topology from Y). This means f is bijective, continuous, and has a continuous inverse.

This is a stronger condition than just being an injective Borel map. But the Lusin-Suslin theorem applies to injective Borel maps, so it certainly applies here.

But maybe with the homeomorphism condition, there's a simpler proof?

Actually, let me think about whether the homeomorphism condition alone (without Borel measurability of f, though continuity implies Borel) gives us the result.

A homeomorphism f: A → B means:
- f is a bijection
- f is continuous (from A with subspace topology to B with subspace topology)
- f^{-1} is continuous

Since f is continuous, it's Borel measurable. Since A is Borel in X, and f: A → Y is injective Borel, by Lusin-Suslin, f(A) = B is Borel.

So the answer is yes, and the proof uses Lusin-Suslin.

But let me also think about whether there's a more direct proof using the homeomorphism property.

**Direct approach using homeomorphism**:

Since f is a homeomorphism, B = f(A) is homeomorphic to A. A is a Borel subset of a Polish space, so A is a "Lusin space" (a space that is Borel-isomorphic to a Polish space, or equivalently, a space that admits a finer Polish topology).

Actually, A with the subspace topology is a "Borel subset of a Polish space," which is a standard Borel space (when equipped with the Borel σ-algebra). The question is whether B, with the subspace topology from Y, is a Borel subset of Y.

The fact that B is homeomorphic to A doesn't immediately tell us B is Borel in Y, because there are non-Borel subsets of Polish spaces that are homeomorphic to Borel subsets (I think? or is this not possible?).

Actually, wait. Is it possible for a non-Borel set to be homeomorphic to a Borel set? 

Consider: let A = {0} (a single point, Borel in ℝ). Let B be any singleton in ℝ, say {π}. Then B is Borel. So singletons are fine.

What about: A = ℚ (rationals, Borel in ℝ, specifically F_σ). Is there a non-Borel set homeomorphic to ℚ? ℚ is countable, so any set homeomorphic to ℚ is countable, hence Borel (countable sets are F_σ). So that doesn't work.

What about uncountable Borel sets? A = Cantor set (closed, Borel). Is there a non-Borel set homeomorphic to the Cantor set? The Cantor set is compact, perfect, totally disconnected. A subset of ℝ homeomorphic to the Cantor set must be compact (since compactness is a topological property), and compact subsets of ℝ are closed, hence Borel. So that doesn't work either.

What about A = Baire space ω^ω (which is a G_δ subset of ℝ^ω or can be embedded as an irrational-like set)? Hmm, this is getting complicated.

Actually, I think the key insight is: a homeomorphic copy of a Borel set in a Polish space is always Borel, and this is precisely the Lusin-Suslin theorem (or a consequence of it). The homeomorphism gives us injectivity + Borel measurability (via continuity), which is exactly what Lusin-Suslin needs.

So the answer is **Yes**, and the proof is by the Lusin-Suslin theorem.

Now let me write a clean, self-contained proof.

**Proof**:

We prove that B = f(A) is Borel in Y.

Since f: A → B is a homeomorphism, f is in particular a continuous injection from A (with the subspace topology inherited from X) into Y. Since A is a Borel subset of the Polish space X, and f is an injective Borel map (continuous ⟹ Borel) from A to the Polish space Y, the Lusin-Suslin theorem applies, giving that f(A) = B is Borel in Y.

Now I need to provide a proof of the Lusin-Suslin theorem (or at least sketch it convincently).

**Lusin-Suslin Theorem**: Let X, Y be Polish spaces, A ⊂ X a Borel set, and f: A → Y an injective Borel map. Then f(A) is Borel in Y.

**Proof of Lusin-Suslin**:

We use the theory of analytic sets. We need the following facts, which we prove or cite:

**Fact 1** (Analytic sets are closed under Borel images): If A ⊂ X is analytic and g: A → Z is Borel (X, Z Polish), then g(A) is analytic in Z.

*Proof*: A is analytic means A = π_X(C) for some closed C ⊂ X × ω^ω. The graph of g, Γ_g = {(a, g(a)) : a ∈ A} is Borel in A × Z (since g is Borel). One can show g(A) is analytic by constructing an appropriate closed set in Z × ω^ω whose projection is g(A). ∎

**Fact 2** (Borel sets are analytic): Every Borel set is analytic. (Follows from: closed sets are analytic, and analytic sets are closed under countable unions and complements... wait, analytic sets are NOT closed under complements. But Borel sets are analytic because: open sets are analytic (as continuous images of ω^ω or as projections of closed sets), and Borel sets are built from open sets by countable operations, and analytic sets are closed under countable unions and intersections, and Borel sets can be built using only countable unions and intersections starting from open sets... actually, the Borel σ-algebra requires complements. But it's a standard result that Borel ⊂ Analytic. The proof uses the fact that analytic sets are closed under countable unions and countable intersections, and the Borel sets are the smallest class containing open sets and closed under countable unions and intersections. Wait, that's not right either—the Borel σ-algebra is closed under complements, not just intersections.

Let me be more careful. The standard proof that Borel ⊂ Analytic uses the following: 
- Open sets are analytic (easy: an open set U = ⋃_n F_n where F_n are closed, and closed sets are analytic (projection of a closed set in X × {0}), and analytic sets are closed under countable unions).
- The class of analytic sets is closed under countable unions and countable intersections.
- The Borel σ-algebra is generated by open sets under countable unions and complements. Since analytic sets are closed under countable unions but NOT complements, we can't directly conclude.

However, the standard proof uses the following: the class of sets that are both analytic and co-analytic is a σ-algebra containing the open sets, hence contains all Borel sets. Since co-analytic sets are complements of analytic sets, and open sets are analytic (and their complements, closed sets, are also analytic), open sets are both analytic and co-analytic. The class of sets that are both analytic and co-analytic is closed under complements (trivially) and under countable unions (since analytic sets are closed under countable unions, and co-analytic sets are closed under countable intersections, which follows from analytic sets being closed under countable unions). So this class is a σ-algebra containing open sets, hence contains all Borel sets. Therefore, every Borel set is both analytic and co-analytic, in particular analytic. ∎

**Fact 3** (Lusin's separation theorem): If A₁, A₂ are disjoint analytic subsets of a Polish space Z, there exists a Borel set C with A₁ ⊂ C and A₂ ∩ C = ∅.

*Proof sketch*: Using the tree representations of A₁ and A₂, one constructs the Borel separating set by a transfinite induction on the "rank" of the trees. The key idea: if A₁ = proj(C₁) and A₂ = proj(C₂) with C₁, C₂ closed, and A₁ ∩ A₂ = ∅, then for every (x, α) ∈ C₁ and (x, β) ∈ C₂, we have a conflict. Using the tree structure, one can define a Borel set that contains A₁ and is disjoint from A₂. ∎

**Fact 4** (Souslin's theorem): A subset of a Polish space is Borel iff it is both analytic and co-analytic.

*Proof*: (⟹) Borel ⟹ analytic and co-analytic: by Fact 2, Borel sets are analytic, and their complements (also Borel) are analytic, so Borel sets are co-analytic too. (⟸) If A is both analytic and co-analytic, then A and A^c are disjoint analytic sets. By Fact 3, there's a Borel set C with A ⊂ C, A^c ∩ C = ∅, so C = A, hence A is Borel. ∎

**Proof of Lusin-Suslin**:

Given: A Borel in X (Polish), f: A → Y injective Borel, Y Polish.

1. f(A) is analytic: A is Borel hence analytic (Fact 2), and f is Borel, so f(A) is analytic (Fact 1).

2. We show Y \ f(A) is analytic. Then by Souslin's theorem (Fact 4), f(A) is Borel.

To show Y \ f(A) is analytic, we use the following argument:

Since A is Borel in X, by a standard result in descriptive set theory, there exists a closed set F ⊂ ω^ω × X and a continuous map such that... 

Hmm, actually, let me use a different approach for step 2.

**Step 2 (alternative)**: We use the following characterization. Since A is Borel, there exists a Polish topology τ on X, finer than the original topology, such that A is clopen (or at least closed) in (X, τ). Wait, that's not quite right.

Actually, the relevant result is: **every Borel subset of a Polish space is itself a Polish space** (with a compatible complete metric that generates a topology finer than the subspace topology, but with the same Borel sets). More precisely, if A is Borel in X, there exists a complete separable metric on A whose topology is finer than the subspace topology from X, but which generates the same Borel σ-algebra on A.

With this Polish topology on A, f: A → Y is still Borel (same Borel σ-algebra). Now A is Polish and f: A → Y is injective Borel.

Now, the graph Γ = {(a, f(a)) : a ∈ A} is Borel in A × Y (graph theorem: the graph of a Borel function between Polish spaces is Borel).

The projection π_Y: A × Y → Y maps Γ bijectively onto f(A) (bijectively because f is injective).

Now, Γ is Borel in A × Y. We want to show π_Y(Γ) = f(A) is Borel.

For each y ∈ Y, the section Γ^y = {a ∈ A : (a, y) ∈ Γ} = {a ∈ A : f(a) = y} is either a singleton (if y ∈ f(A)) or empty. So all sections are countable.

Now we use the **Kondo-Addison theorem** (or Lusin-Novikov), which states: if B ⊂ X × Y is Borel (or even co-analytic) with countable sections, then π_Y(B) is Borel.

But as I noted, this might be circular. Let me check the dependency.

The Lusin-Novikov theorem (countable sections ⟹ Borel projection) is typically proved using the Lusin-Suslin theorem. So using it to prove Lusin-Suslin is circular.

OK so let me go back to the approach of showing Y \ f(A) is analytic directly.

**Direct proof that Y \ f(A) is analytic**:

We use the following key lemma:

**Lemma**: Let A be Borel in Polish X, and f: A → Y injective Borel (Y Polish). Then Y \ f(A) is analytic.

*Proof of Lemma*: 

We use the representation of Borel sets via the "Souslin operation" applied to closed sets.

Since A is Borel, it can be written as A = ⋃_{α ∈ ω^ω} ⋂_n F_{α|n} where (F_s)_{s ∈ ω^{<ω}} is a regular Souslin scheme of closed sets in X with:
- F_s ⊃ F_t when s ⊂ t (nested)
- F_s ∩ F_t = ∅ when s, t are incompatible and |s| = |t| (disjoint at same level)
- diam(F_s) → 0 as |s| → ∞ (vanishing diameter)
- A = ⋃_{α} ⋂_n F_{α|n}

Each "branch" α ∈ ω^ω gives a point x_α = ⋂_n F_{α|n} ∈ A (or the intersection is empty, but for α in the right set, it gives a point).

Actually, this is the representation of a Borel set as a continuous image of a closed subset of ω^ω. Let me be more precise.

Since A is Borel, there exists a closed set D ⊂ ω^ω and a continuous bijection g: D → A. (This is a standard fact: every Borel set is a one-to-one continuous image of a closed subset of Baire space.)

Now, h = f ∘ g: D → Y is injective Borel (g is continuous hence Borel, f is Borel, composition is Borel). D is closed in ω^ω, hence Polish.

h(D) = f(A). We want to show Y \ h(D) is analytic.

Since h: D → Y is injective Borel and D is Polish, the graph Γ = {(d, h(d)) : d ∈ D} is Borel in D × Y, hence Borel in ω^ω × Y (since D is closed in ω^ω).

Now, Y \ h(D) = {y ∈ Y : ∀d ∈ D, h(d) ≠ y} = {y ∈ Y : Γ^y = ∅} where Γ^y = {d ∈ D : (d, y) ∈ Γ}.

Since Γ is Borel in ω^ω × Y, the set {(d, y) : (d, y) ∈ Γ} is Borel. Its complement in D × Y is also Borel: Γ^c = (D × Y) \ Γ is Borel in D × Y.

Now, {y : Γ^y = ∅} = {y : ∀d ∈ D, (d, y) ∉ Γ} = {y : D × {y} ⊂ Γ^c} = {y : (D × {y}) ∩ Γ = ∅}.

The projection of Γ^c onto Y is: π_Y(Γ^c) = {y : ∃d ∈ D, (d, y) ∈ Γ^c} = {y : ∃d ∈ D, (d, y) ∉ Γ} = {y : Γ^y ≠ D}.

Hmm, that's not quite what we want. We want {y : Γ^y = ∅}, not {y : Γ^y ≠ D}.

Let me reconsider. 

Y \ h(D) = {y : Γ^y = ∅} = {y : ∀d, (d,y) ∉ Γ}.

The complement: h(D) = {y : ∃d, (d,y) ∈ Γ} = π_Y(Γ).

So Y \ h(D) = Y \ π_Y(Γ).

π_Y(Γ) is analytic (projection of Borel is analytic). So Y \ π_Y(Γ) is co-analytic. We want to show it's analytic.

This is the crux: why is the complement of an injective Borel image analytic?

The key is the injectivity. Here's the argument:

Since h is injective, for each y, Γ^y is either a singleton or empty. 

Now, consider the set Γ^c = (ω^ω × Y) \ Γ (the complement in the full product, not just D × Y). This is Borel (since Γ is Borel in ω^ω × Y, its complement in ω^ω × Y is Borel).

π_Y(Γ^c) = {y : ∃d ∈ ω^ω, (d, y) ∉ Γ} = {y : ∃d ∈ ω^ω, d ∉ D or h(d) ≠ y}.

Since for d ∉ D, (d, y) ∉ Γ for all y (because Γ ⊂ D × Y), we have:

π_Y(Γ^c) ⊃ {y : ∃d ∉ D, (d,y) ∉ Γ} = Y (since for any y, any d ∉ D gives (d,y) ∉ Γ).

So π_Y(Γ^c) = Y, which is useless.

OK so this approach of taking the complement in the full product doesn't work because D is a proper subset of ω^ω.

Let me try a different approach. Let me use the structure of D as a closed set in ω^ω.

D is closed in ω^ω. So D^c = ω^ω \ D is open, hence a countable union of basic open sets: D^c = ⋃_s U_s where U_s are basic clopen sets in ω^ω.

Hmm, this is getting complicated. Let me try the approach from Kechris's book directly.

**Kechris's proof of Lusin-Suslin (Theorem 15.1)**:

I'll try to recall the proof. I believe Kechris proves it using the following:

1. First, he proves the "good parameterization" theorem for analytic sets.
2. Then uses it to prove Lusin-Suslin.

Actually, I think the proof in Kechris goes through the following:

**Theorem 15.1 (Lusin-Suslin)**: If X, Y are Polish, A ⊂ X is Borel, and f: A → Y is injective Borel, then f(A) is Borel.

**Proof** (Kechris):

The proof uses the following key idea: 

Step 1: Since A is Borel, write A = ⋃_n A_n where each A_n is Borel and "bounded" in some sense.

Actually, I recall now. The proof in Kechris uses the following approach:

He first proves (Theorem 13.1 or similar) that every analytic set A has a "rank" function, and uses the boundedness theorem: if A is analytic and has bounded rank, then A is Borel.

Then for Lusin-Suslin: f(A) is analytic. One shows that f(A) has bounded rank (using the injectivity of f and the Borelness of A), hence f(A) is Borel by the boundedness theorem.

But the details of this are quite technical. Let me try to write a proof that's correct but may reference some standard results.

Actually, let me try a cleaner approach. I'll prove the result using the following strategy:

**Proof strategy**: Show that the class of Borel sets A ⊂ X such that "for every injective Borel f: A → Y (Y Polish), f(A) is Borel" is a σ-algebra containing all closed sets. Since the Borel σ-algebra is the smallest such, the result follows.

**Step 1: Closed sets are in the class.**

If A is closed in X, then A is Polish (closed subset of Polish is Polish). f: A → Y is injective Borel. Since A is Polish and f is Borel, the graph Γ(f) is Borel in A × Y. 

Now, for closed A, we can say more: f: A → Y is injective Borel from a Polish space. We need to show f(A) is Borel.

Hmm, but this is the same problem. The base case doesn't simplify.

Let me try yet another approach. Let me use the following:

**Approach**: We prove the result for injective continuous maps from closed sets, then extend to Borel maps from Borel sets.

**Step 1**: If F is closed in ω^ω and g: F → Y is injective continuous (Y Polish), then g(F) is Borel.

*Proof*: F is closed in ω^ω, hence compact? No, ω^ω is not compact. F is closed but not necessarily compact.

Hmm. But F is a closed subset of ω^ω, which is Polish. g: F → Y is injective continuous.

The graph Γ = {(x, g(x)) : x ∈ F} is closed in F × Y (graph of a continuous function into a Hausdorff space is closed). Since F is closed in ω^ω, Γ is closed in ω^ω × Y.

g(F) = π_Y(Γ), the projection of a closed set. Projections of closed sets are analytic (by definition, analytic sets are projections of closed sets in X × ω^ω, or equivalently, continuous images of ω^ω). So g(F) is analytic.

Now, is g(F) co-analytic? We need Y \ g(F) to be analytic.

Y \ g(F) = {y ∈ Y : ∀x ∈ F, g(x) ≠ y} = {y : Γ^y = ∅}.

Γ is closed in ω^ω × Y. Γ^y = {x ∈ ω^ω : (x, y) ∈ Γ} is closed in ω^ω (section of a closed set is closed).

{y : Γ^y = ∅} = {y : the closed set Γ^y is empty}.

Now, a closed set in ω^ω is empty iff the tree T(Γ^y) is well-founded (has no infinite branch). The set of y for which T(Γ^y) is well-founded is... co-analytic (this is the classic co-analytic set: well-foundedness of trees is co-analytic, not analytic in general).

So this approach gives that Y \ g(F) is co-analytic, not analytic. We're stuck.

The issue is that for a general continuous injective map from a closed set, the complement of the image is co-analytic but not obviously analytic. The injectivity must be used in a more essential way.

Let me think about this differently. The injectivity means that the sections Γ^y are at most singletons. A closed set with at most singleton sections... 

**Key insight**: If Γ is closed in ω^ω × Y and every section Γ^y is at most a singleton, then π_Y(Γ) is Borel (in fact closed? no, not necessarily closed, but Borel).

Actually, let me think about this. If Γ is closed and every section is at most a singleton, is π_Y(Γ) Borel?

Consider: Γ is closed in ω^ω × Y. The projection π_Y(Γ) is analytic. The complement Y \ π_Y(Γ) = {y : Γ^y = ∅}. 

Γ^y is a closed subset of ω^ω. Γ^y = ∅ iff the tree T_y = {s ∈ ω^{<ω} : [s] × {y} intersects Γ in a certain way} is well-founded.

Hmm, but with the singleton section condition, maybe we can say more.

Actually, here's the key: if every section Γ^y is at most a singleton, then the projection π_Y restricted to Γ is a bijection (from Γ to π_Y(Γ)). Since Γ is closed (hence Polish) and π_Y is continuous, π_Y|_Γ: Γ → π_Y(Γ) is a continuous bijection from a Polish space to a (potentially non-Polish) space.

A continuous bijection from a Polish space... the image is analytic. But is it Borel?

By a theorem of Sierpinski or Lusin-Suslin: a continuous injective image of a Borel set is Borel. But this is what we're trying to prove!

OK, I think I need to use a genuinely different approach. Let me look at this from the perspective of the "boundedness theorem" for analytic sets.

**Boundedness Theorem**: If A is an analytic set of "bounded rank" (in the sense of the rank on the associated tree), then A is Borel. More precisely, if A is a co-analytic set (or analytic set) and the associated rank function is bounded, then A is Borel.

Actually, the boundedness theorem states: if A is a co-analytic subset of a Polish space and A is contained in a set of bounded rank, then A is Borel. Or more precisely: if WF is the set of well-founded trees and A ⊂ WF is analytic (as a subset of the space of trees), then A is bounded (there's a countable ordinal bounding the ranks), and hence A is Borel.

Let me try to use this.

**Proof of Lusin-Suslin using boundedness**:

1. f(A) is analytic.
2. We show f(A) is Borel by showing it has bounded rank (or equivalently, that it's co-analytic with bounded rank).

Actually, let me try the following cleaner approach.

**Proof using the separation theorem directly**:

We prove: if A is Borel in Polish X and f: A → Y is injective Borel (Y Polish), then f(A) is Borel.

**Key claim**: Y \ f(A) is analytic.

Once we have this, f(A) is both analytic and co-analytic, hence Borel by Souslin's theorem.

**Proof of the key claim**:

Since A is Borel in X, there exists a closed set D ⊂ ω^ω and a continuous bijection g: D → A. (Standard fact: every Borel set in a Polish space is a one-to-one continuous image of a closed subset of Baire space.)

Let h = f ∘ g: D → Y. Then h is injective Borel, D is closed in ω^ω (hence Polish), and h(D) = f(A).

Now, the graph Γ = {(d, h(d)) : d ∈ D} is Borel in D × Y (graph of a Borel function). Since D is closed in ω^ω, Γ is Borel in ω^ω × Y.

Since h is injective, for each y ∈ Y, the section Γ^y = {d ∈ D : h(d) = y} is either a singleton or empty.

Now, Y \ h(D) = {y : Γ^y = ∅}.

**Sub-claim**: {y : Γ^y = ∅} is analytic, given that Γ is Borel with at most singleton sections.

To prove this, we use the following:

Since Γ is Borel in ω^ω × Y, there exists a closed set C ⊂ ω^ω × Y × ω^ω such that Γ = π_{ω^ω × Y}(C) (i.e., Γ is the projection of a closed set, which is the definition of analytic... wait, Γ is Borel, hence analytic, so it's the projection of a closed set).

Actually, let me use a different approach. Since Γ is Borel, it's both analytic and co-analytic. The complement Γ^c = (ω^ω × Y) \ Γ is also Borel, hence analytic.

Now, Y \ h(D) = {y : Γ^y = ∅} = {y : (ω^ω × {y}) ∩ Γ = ∅} = {y : (ω^ω × {y}) ⊂ Γ^c}.

The set {(d, y) : (d, y) ∈ Γ^c} = Γ^c is Borel (hence analytic). 

{y : ∀d, (d, y) ∈ Γ^c} = {y : ω^ω × {y} ⊂ Γ^c} = {y : (ω^ω × {y}) ∩ Γ = ∅}.

This is a co-analytic condition (universal quantifier). But we need to use the singleton section property to turn it into an analytic condition.

Here's the key: since Γ^y is at most a singleton, Γ^y = ∅ iff Γ^y ≠ {d} for all d. But this is still a universal condition.

Alternatively: Γ^y ≠ ∅ iff ∃d, (d, y) ∈ Γ. So h(D) = π_Y(Γ) is analytic (which we already knew).

And Y \ h(D) = {y : Γ^y = ∅}. 

Hmm, I keep going in circles. Let me try to use the singleton section property more directly.

**Using singleton sections**: Since Γ^y is at most a singleton for each y, the projection π_ω^ω: Γ → ω^ω is a Borel isomorphism (from Γ to D, with inverse being the map d ↦ (d, h(d))). 

Actually, π_ω^ω restricted to Γ is a bijection from Γ to D (since for each d ∈ D, there's exactly one y = h(d) with (d, y) ∈ Γ, and for d ∉ D, there's no such y). So π_ω^ω|_Γ: Γ → D is a bijection. It's continuous (restriction of a continuous projection). Its inverse is d ↦ (d, h(d)), which is Borel (since h is Borel). So π_ω^ω|_Γ is a Borel isomorphism.

Now, Γ is Borel in ω^ω × Y, and π_ω^ω|_Γ: Γ → D is a Borel isomorphism (with D closed in ω^ω). 

Hmm, I'm not sure this helps directly.

Let me try a completely different approach to the whole problem.

**Approach via "Borel sets are preserved under Borel isomorphisms"**:

Actually, the statement we're proving is essentially: "Borel sets are closed under Borel isomorphisms" in the following sense: if A is Borel in X and f: A → Y is a Borel isomorphism (bijection with f and f^{-1} Borel), then f(A) is Borel in Y.

Wait, in our problem, f is a homeomorphism, so f^{-1} is also continuous (hence Borel). So f is a Borel isomorphism. And the result is that f(A) = B is Borel.

This is indeed the Lusin-Suslin theorem: Borel isomorphisms preserve Borelness.

Let me try to prove this using the following approach:

**Proof using the "standard Borel space" theory**:

A standard Borel space is a set equipped with a σ-algebra that is isomorphic to the Borel σ-algebra of a Polish space. 

Key fact: If (Z, ℬ) is a standard Borel space and 𝒜 ⊂ ℬ is a sub-σ-algebra, then... hmm, this doesn't directly help.

Let me try another approach.

**Proof via the "Borel linear order" or "Hahn-Mazurkiewicz" approach**:

Actually, I think the cleanest proof for our specific problem (where f is a homeomorphism, not just Borel) might use the following:

**Theorem**: If A is a Borel subset of a Polish space X, and f: A → Y is a homeomorphism onto B = f(A) ⊂ Y (Y Polish), then B is Borel.

**Proof**:

Since A is Borel in X, A is a Lusin space: there exists a Polish topology τ on A, finer than the subspace topology, such that (A, τ) is Polish and the Borel sets of (A, τ) coincide with the Borel sets of A as a subspace of X.

Now, f: A → B is a homeomorphism (with the subspace topologies). So f is a homeomorphism from (A, subspace topology) to (B, subspace topology).

Consider the topology τ' on B defined by: U ⊂ B is τ'-open iff f^{-1}(U) is τ-open. Then (B, τ') is homeomorphic to (A, τ), hence Polish. And τ' is finer than the subspace topology on B (from Y), because τ is finer than the subspace topology on A (from X), and f is a homeomorphism with respect to the subspace topologies.

Now, (B, τ') is a Polish space, and τ' is finer than the subspace topology from Y. The Borel sets of (B, τ') include all sets that are Borel in the subspace topology (since τ' is finer). 

But we need to show B is Borel in Y, not just that B has a Polish topology.

Hmm, this approach shows that B is a Lusin space (it has a finer Polish topology), but a Lusin subspace of a Polish space is Borel. Wait, is that true?

**Theorem**: If B ⊂ Y (Y Polish) and B admits a Polish topology finer than the subspace topology from Y, then B is Borel in Y.

Is this true? I believe so. This is essentially the content of the following:

**Theorem (Mackey, or classical)**: A subset B of a Polish space Y is Borel iff B is a Lusin space (i.e., B admits a Polish topology finer than the subspace topology that generates the same Borel sets).

Wait, but we need to be careful. The "finer Polish topology" on B generates a σ-algebra that contains the subspace Borel σ-algebra. But does it generate the same σ-algebra?

In our case: (B, τ') is Polish, and τ' is finer than the subspace topology. The Borel σ-algebra of (B, τ') contains the Borel σ-algebra of (B, subspace topology). But it might be strictly larger.

However, we also know that f: (A, τ) → (B, τ') is a homeomorphism, and (A, τ) has the same Borel sets as (A, subspace topology from X). Since f is a homeomorphism with respect to the subspace topologies, the Borel sets of (B, subspace topology) correspond (via f) to the Borel sets of (A, subspace topology), which are the same as the Borel sets of (A, τ). And the Borel sets of (B, τ') correspond (via f) to the Borel sets of (A, τ). So the Borel sets of (B, τ') are the same as the Borel sets of (B, subspace topology).

So: (B, τ') is Polish, τ' is finer than the subspace topology, and the Borel σ-algebras coincide. This means B is a Lusin subspace of Y.

Now, the theorem that "a Lusin subspace of a Polish space is Borel" is what we need. But this theorem is essentially equivalent to what we're trying to prove (or at least closely related).

Hmm, let me think about whether "Lusin subspace ⟹ Borel" can be proved independently.

**Theorem**: If B ⊂ Y (Y Polish) and B admits a Polish topology τ' finer than the subspace topology, with the same Borel σ-algebra, then B is Borel in Y.

**Proof**: Since (B, τ') is Polish, the identity map id: (B, τ') → (B, subspace topology) is a continuous bijection (since τ' is finer than the subspace topology, the identity from τ' to subspace is continuous). It's also Borel (since the Borel σ-algebras are the same). 

Now, consider id: (B, τ') → Y (where Y has its original Polish topology). This is a continuous injection (continuous because τ' is finer than the subspace topology, and the subspace topology is the restriction of Y's topology). (B, τ') is Polish, Y is Polish, and id is injective continuous (hence Borel). 

By the Lusin-Suslin theorem (applied to the Polish space (B, τ'), the Polish space Y, the Borel set (B, τ') itself (which is Borel in itself, trivially), and the injective Borel map id), id(B) = B is Borel in Y.

But this uses Lusin-Suslin, which is what we're trying to prove! So it's circular.

OK, I think I need to just prove the Lusin-Suslin theorem from scratch. Let me look for the most elementary proof.

**Elementary proof of Lusin-Suslin**:

I'll use the approach via the separation theorem and the structure of analytic sets, following the proof in Kechris or Jech.

Let me recall the proof from Jech's "Set Theory" or Moschovakis's "Descriptive Set Theory."

Actually, let me try the proof from Srivastava's "A Course on Borel Sets," which I recall has a clean proof.

**Proof (following Srivastava)**:

We need the following:

1. **Analytic sets**: A ⊂ X is analytic if A = proj_X(C) for some closed C ⊂ X × ω^ω. Equivalently, A is the continuous image of ω^ω.

2. **Borel ⊂ Analytic**: Every Borel set is analytic. (Proved using the fact that the class of analytic sets is closed under countable unions and intersections, and the class of sets that are both analytic and co-analytic is a σ-algebra containing the Borel sets.)

3. **Lusin's separation theorem**: If A₁, A₂ are disjoint analytic sets in a Polish space, they can be separated by a Borel set.

4. **Souslin's theorem**: Borel = Analytic ∩ Co-analytic.

**Proof of Lusin-Suslin**:

Given: A Borel in X (Polish), f: A → Y injective Borel, Y Polish.

f(A) is analytic (Fact 1). We show f(A) is co-analytic, i.e., Y \ f(A) is analytic.

**Key step**: Y \ f(A) is analytic.

Since A is Borel, there is a sequence of Borel sets (A_s)_{s ∈ ω^{<ω}} with:
- A_∅ = A
- A_s = ⋃_n A_{s⌢n} for each s
- A_s ∩ A_t = ∅ when s, t are incompatible (s ⊄ t and t ⊄ s)
- diam(A_s) → 0 as |s| → ∞ (in some complete metric on X)
- For each x ∈ A, there's a unique α ∈ ω^ω with x ∈ ⋂_n A_{α|n}, and this intersection is {x}.

This is a "regular Souslin scheme" or "Lusin scheme" for A. Such a scheme exists because A is Borel (in fact, because A is a Lusin space).

Now, f(A_s) is analytic for each s (image of Borel under Borel). The sets f(A_s) satisfy:
- f(A_∅) = f(A)
- f(A_s) = ⋃_n f(A_{s⌢n}) (since f is a bijection, f(⋃_n A_{s⌢n}) = ⋃_n f(A_{s⌢n}))
- f(A_s) ∩ f(A_t) = ∅ when s, t are incompatible (since f is injective and A_s ∩ A_t = ∅)

So (f(A_s)) is also a Lusin scheme, but for f(A), and each f(A_s) is analytic.

Now, Y \ f(A) = Y \ ⋃_n f(A_{(n)}) = ⋂_n (Y \ f(A_{(n)})).

Since f(A_{(n)}) are analytic, Y \ f(A_{(n)}) are co-analytic. The intersection of co-analytic sets is co-analytic. So Y \ f(A) is co-analytic. But we want it to be analytic!

Hmm, this doesn't directly work. The intersection of co-analytic sets is co-analytic, not analytic.

Let me try a different decomposition. 

Actually, the key is to use the disjointness of the f(A_s) and the separation theorem.

Here's the idea: since f(A_{(n)}) are pairwise disjoint analytic sets, by the separation theorem, there exist pairwise disjoint Borel sets B_n ⊃ f(A_{(n)}). 

Then f(A) = ⋃_n f(A_{(n)}) ⊂ ⋃_n B_n, and ⋃_n B_n is Borel.

But this only shows f(A) ⊂ a Borel set, not that f(A) is Borel. We need to also show that ⋃_n B_n \ f(A) is "small" in some sense, or refine the argument.

Let me continue the argument. We have B_n ⊃ f(A_{(n)}) with B_n pairwise disjoint Borel. Now, within each B_n, we have f(A_{(n)}) ⊂ B_n, and f(A_{(n)}) = ⋃_m f(A_{(n,m)}), where f(A_{(n,m)}) are pairwise disjoint analytic sets.

By the separation theorem again, there exist pairwise disjoint Borel sets B_{(n,m)} ⊂ B_n with B_{(n,m)} ⊃ f(A_{(n,m)}).

Continuing this way, we get a tree of Borel sets (B_s)_{s ∈ ω^{<ω}} with:
- B_s ⊃ f(A_s)
- B_s = ⋃_n B_{s⌢n} (we can ensure this by replacing B_{s⌢n} with B_s ∩ B_{s⌢n} if needed... wait, we need B_{s⌢n} ⊂ B_s. Let me be more careful.)

Actually, let me redo this. We construct B_s by induction on |s|.

Level 0: B_∅ = Y (or some Borel set containing f(A)).

Level 1: f(A_{(n)}) are pairwise disjoint analytic. By separation, there exist pairwise disjoint Borel sets C_n ⊃ f(A_{(n)}). Set B_{(n)} = C_n.

Level 2: For each n, f(A_{(n,m)}) (m = 0, 1, 2, ...) are pairwise disjoint analytic sets contained in f(A_{(n)}) ⊂ B_{(n)}. By separation (within B_{(n)}), there exist pairwise disjoint Borel sets C_{n,m} ⊂ B_{(n)} with C_{n,m} ⊃ f(A_{(n,m)}). Set B_{(n,m)} = C_{n,m}.

And so on. We get B_s Borel with:
- B_s ⊃ f(A_s)
- B_{s⌢n} ⊂ B_s (by construction)
- B_{s⌢n} pairwise disjoint (for fixed s, varying n)
- B_s = ⋃_n B_{s⌢n} ∪ (B_s \ ⋃_n f(A_{s⌢n}))... hmm, actually B_s might not equal ⋃_n B_{s⌢n}. We have ⋃_n B_{s⌢n} ⊂ B_s, but there might be a "remainder" B_s \ ⋃_n B_{s⌢n}.

The remainder R_s = B_s \ ⋃_n B_{s⌢n} is Borel (difference of Borel sets). And R_s ⊂ B_s \ ⋃_n f(A_{s⌢n}) = B_s \ f(A_s) (since f(A_s) = ⋃_n f(A_{s⌢n}) by the Lusin scheme property and injectivity).

So R_s ∩ f(A_s) = ∅, i.e., R_s ⊂ B_s \ f(A_s).

Now, f(A) = ⋃_n f(A_{(n)}). And ⋃_n B_{(n)} ⊃ f(A). The "extra" part is ⋃_n (B_{(n)} \ f(A_{(n)})).

For each n, B_{(n)} \ f(A_{(n)}) = B_{(n)} \ ⋃_m f(A_{(n,m)}) = R_{(n)} ∪ ⋃_m (B_{(n,m)} \ f(A_{(n,m)})).

This gives a recursive decomposition. The idea is that the "extra" part keeps getting refined, and in the limit, the intersection of all the B_s along any branch is either a point in f(A) or empty.

More precisely, for any y ∈ ⋃_n B_{(n)}, there's a unique n with y ∈ B_{(n)} (since B_{(n)} are disjoint). Then either y ∈ R_{(n)} (in which case y ∉ f(A)) or y ∈ B_{(n,m)} for a unique m. Continuing, either y falls into some R_s at some finite stage (y ∉ f(A)), or y ∈ ⋂_k B_{α|k} for some α ∈ ω^ω.

If y ∈ ⋂_k B_{α|k}, then y ∈ ⋂_k B_{α|k} and f(A_{α|k}) ⊂ B_{α|k}. Since diam(A_{α|k}) → 0 and A_{α|k} are nested, ⋂_k A_{α|k} = {x_α} for some x_α ∈ A. Then f(x_α) ∈ ⋂_k f(A_{α|k}) ⊂ ⋂_k B_{α|k}. 

But is y = f(x_α)? We know y ∈ ⋂_k B_{α|k} and f(x_α) ∈ ⋂_k B_{α|k}. If ⋂_k B_{α|k} = {f(x_α)}, then y = f(x_α) ∈ f(A). But ⋂_k B_{α|k} might contain other points.

Hmm, so this approach has a gap: the B_s might not shrink to a point.

To fix this, we need to ensure that the B_s also have vanishing diameter. But B_s are subsets of Y, and we need a metric on Y. If Y is Polish with metric d, we need diam(B_s) → 0.

We can ensure this by choosing the separations carefully. When we separate f(A_{s⌢n}) within B_s, we can use Borel sets that are contained in small balls around f(A_{s⌢n}).

But f(A_{s⌢n}) might not be bounded in a small ball. Hmm, but A_{s⌢n} has small diameter (in X), and f is continuous (it's a homeomorphism!), so f(A_{s⌢n}) should be "small" in some sense. But f is continuous from A (subspace of X) to Y, and A_{s⌢n} has small diameter in X, but f might not be uniformly continuous, so f(A_{s⌢n}) might not have small diameter in Y.

Wait, actually, in our problem, f is a homeomorphism, so f is continuous. But continuous maps on non-compact sets need not be uniformly continuous. So f(A_{s⌢n}) might not have small diameter even if A_{s⌢n} does.

Hmm, but actually, we can choose the Lusin scheme (A_s) more carefully. Instead of requiring diam(A_s) → 0 in X, we can require that f(A_s) has vanishing diameter in Y. Since f is a homeomorphism, f is continuous, and we can choose the scheme on A to be compatible with the topology on B = f(A) (via f).

Actually, let me think about this differently. Since f is a homeomorphism, we can transfer the Lusin scheme from A to B directly. The sets f(A_s) form a Lusin scheme for B = f(A) in Y, with:
- f(A_s) analytic (since A_s is Borel and f is Borel)
- f(A_s) = ⋃_n f(A_{s⌢n})
- f(A_s) ∩ f(A_t) = ∅ for incompatible s, t
- ⋂_k f(A_{α|k}) = {f(x_α)} for each α (since f is a homeomorphism and ⋂_k A_{α|k} = {x_α})

But we need diam(f(A_s)) → 0. If we choose the original scheme (A_s) such that the images f(A_s) have vanishing diameter, this works. Since f is a homeomorphism, the topology on A (subspace from X) is the same as the topology pulled back from B (subspace from Y) via f. So we can choose the scheme (A_s) to be compatible with the metric on Y (via f).

More precisely: choose the Lusin scheme (A_s) such that diam_Y(f(A_s)) → 0 as |s| → ∞. This is possible because f is a homeomorphism, so the topology on A induced by the metric d_Y ∘ (f × f) is the same as the subspace topology from X, and A is Borel (hence Lusin) in this topology as well.

OK so with this setup, we have:
- f(A_s) are analytic, with diam_Y(f(A_s)) → 0
- f(A_s) = ⋃_n f(A_{s⌢n})
- f(A_s) ∩ f(A_t) = ∅ for incompatible s, t
- ⋂_k f(A_{α|k}) = {f(x_α)} (a single point)

Now, we construct B_s ⊃ f(A_s) Borel with:
- B_s Borel
- B_{s⌢n} ⊂ B_s
- B_{s⌢n} pairwise disjoint (for fixed s)
- diam(B_s) → 0 (we can ensure this by choosing B_s inside a small ball around f(A_s))
- B_s ⊃ f(A_s)

Wait, can we ensure diam(B_s) → 0 while also having B_s ⊃ f(A_s)? We need f(A_s) to be contained in a small ball, which requires diam(f(A_s)) → 0. We've arranged this. So we can choose B_s ⊂ {y : d(y, f(A_s)) < ε_s} with ε_s → 0, ensuring diam(B_s) → 0.

But we also need B_s = ⋃_n B_{s⌢n} ∪ R_s where R_s is the "remainder." With diam(B_s) → 0, the remainder R_s also has small diameter.

Now, for y ∈ ⋃_n B_{(n)}:
- Either y ∈ R_{(n)} for some n (y ∉ f(A), and y ∈ R_{(n)} which is Borel)
- Or y ∈ B_{(n,m)} for some (n,m), and then either y ∈ R_{(n,m)} or y ∈ B_{(n,m,k)}, etc.
- Or y ∈ ⋂_k B_{α|k} for some α ∈ ω^ω.

In the last case, since diam(B_{α|k}) → 0, ⋂_k B_{α|k} is a single point {y}. And f(x_α) ∈ ⋂_k f(A_{α|k}) ⊂ ⋂_k B_{α|k} = {y}. So y = f(x_α) ∈ f(A).

Therefore:
⋃_n B_{(n)} = f(A) ⊔ ⋃_{s ∈ ω^{<ω}} R_s

where the union is disjoint, and each R_s is Borel. Wait, is this exactly right? Let me check.

Every y ∈ ⋃_n B_{(n)} either:
(a) Falls into some R_s at a finite stage: y ∈ R_s for some s. These y are not in f(A).
(b) Falls into ⋂_k B_{α|k} for some α: y = f(x_α) ∈ f(A).

And these cases are mutually exclusive and cover all of ⋃_n B_{(n)}.

So ⋃_n B_{(n)} = f(A) ∪ ⋃_s R_s (disjoint union).

Therefore: f(A) = (⋃_n B_{(n)}) \ (⋃_s R_s) = (⋃_n B_{(n)}) ∩ (⋂_s (Y \ R_s)).

Wait, that's not quite right. Let me be more careful.

f(A) = (⋃_n B_{(n)}) \ (⋃_s R_s).

Since ⋃_n B_{(n)} is Borel (countable union of Borel) and ⋃_s R_s is Borel (countable union of Borel), f(A) is Borel! ∎

Wait, is this correct? Let me double-check the key step.

**Claim**: ⋃_n B_{(n)} = f(A) ⊔ ⋃_s R_s (disjoint union).

*Proof*: 
- f(A) ⊂ ⋃_n B_{(n)}: Since f(A) = ⋃_n f(A_{(n)}) ⊂ ⋃_n B_{(n)}. ✓
- ⋃_s R_s ⊂ ⋃_n B_{(n)}: Since R_s ⊂ B_s ⊂ B_{s|1} ⊂ ⋃_n B_{(n)} (for s ≠ ∅; and R_∅ ⊂ B_∅ = ⋃_n B_{(n)} if we set B_∅ = ⋃_n B_{(n)}). ✓ (Need to check: R_s = B_s \ ⋃_n B_{s⌢n} ⊂ B_s. And B_s ⊂ B_{s|1} ⊂ ... ⊂ B_{(s_0)} ⊂ ⋃_n B_{(n)}. ✓)
- f(A) ∩ (⋃_s R_s) = ∅: If y ∈ f(A), then y = f(x) for some x ∈ A. There's a unique α with x ∈ ⋂_k A_{α|k} = {x}. So y = f(x) ∈ ⋂_k f(A_{α|k}) ⊂ ⋂_k B_{α|k}. For y to be in R_s, we'd need y ∈ B_s \ ⋃_n B_{s⌢n}. But y ∈ B_{α|k} for all k, so y ∈ B_{s⌢n} where s = α|k and n = α(k+1). So y ∉ R_s for any s = α|k. And for s not of the form α|k, y might or might not be in B_s, but if y ∈ B_s for some s, then s must be compatible with α (since y ∈ B_{α|k} and B_s ∩ B_t = ∅ for incompatible s, t at the same level... wait, B_s and B_t are disjoint only when s, t are incompatible AND at the same level? No, I said B_{s⌢n} are pairwise disjoint for fixed s, varying n. So B_{(0)} and B_{(1)} are disjoint, B_{(0,0)} and B_{(0,1)} are disjoint, etc. But B_{(0)} and B_{(0,0)} are not disjoint (B_{(0,0)} ⊂ B_{(0)}).

Let me reconsider. If y ∈ ⋂_k B_{α|k}, is y ∉ R_s for all s?

R_s = B_s \ ⋃_n B_{s⌢n}. If y ∈ R_s, then y ∈ B_s and y ∉ B_{s⌢n} for all n.

If s = α|j for some j, then y ∈ B_{α|j} = B_s, and y ∈ B_{α|(j+1)} = B_{s⌢α(j)} ⊂ ⋃_n B_{s⌢n}. So y ∉ R_s. ✓

If s is incompatible with α (i.e., s and α|j| are incompatible for some j), then... y ∈ B_{α|j} for all j. If |s| = j and s is incompatible with α|j, then B_s and B_{α|j} are disjoint (since s and α|j are incompatible at level j, and B_t are pairwise disjoint at each level... wait, are they? B_{(0)} and B_{(1)} are disjoint, but are B_{(0,0)} and B_{(1,0)} disjoint? 

B_{(0,0)} ⊂ B_{(0)} and B_{(1,0)} ⊂ B_{(1)}, and B_{(0)} ∩ B_{(1)} = ∅, so B_{(0,0)} ∩ B_{(1,0)} = ∅. ✓

More generally, if s and t are incompatible (differ at some position), say s and t first differ at position k, then s|k = t|k but s(k) ≠ t(k). So B_s ⊂ B_{s|(k+1)} and B_t ⊂ B_{t|(k+1)}, and B_{s|(k+1)} and B_{t|(k+1)} are disjoint (they're both children of B_{s|k} = B_{t|k} with different indices). So B_s ∩ B_t = ∅. ✓

So if s is incompatible with α, then y ∈ B_{α||s|} and B_s ∩ B_{α||s|} = ∅, so y ∉ B_s, hence y ∉ R_s. ✓

If s is a proper initial segment of α (s = α|j for some j < |α|... well α is infinite, so s = α|j for some finite j), we already handled this: y ∉ R_s. ✓

If s extends α|j for some j but s ≠ α|j' for any j' (i.e., s is a finite extension of some α|j but diverges from α after that), then s is incompatible with α, and we've handled this. ✓

So y ∉ R_s for all s. ✓

- ⋃_n B_{(n)} ⊂ f(A) ∪ ⋃_s R_s: Let y ∈ ⋃_n B_{(n)}. Then y ∈ B_{(n)} for some unique n (since B_{(n)} are pairwise disjoint). Either y ∈ R_{(n)} (done, y ∈ ⋃_s R_s) or y ∈ B_{(n,m)} for some unique m. Either y ∈ R_{(n,m)} (done) or y ∈ B_{(n,m,k)} for some unique k. Continuing, either y ∈ R_s for some s (done), or we get an infinite sequence α = (n, m, k, ...) with y ∈ B_{α|j} for all j. Since diam(B_{α|j}) → 0, ⋂_j B_{α|j} = {y}. And f(x_α) ∈ ⋂_j f(A_{α|j}) ⊂ ⋂_j B_{α|j} = {y}, so y = f(x_α) ∈ f(A). ✓

Great, so the claim is proved, and f(A) = (⋃_n B_{(n)}) \ (⋃_s R_s) is Borel. ∎

Now let me also verify that we can indeed construct the B_s with the required properties.

**Construction of B_s**:

We need: B_s Borel, B_s ⊃ f(A_s), B_{s⌢n} ⊂ B_s, B_{s⌢n} pairwise disjoint (for fixed s, varying n), and diam(B_s) → 0 as |s| → ∞.

We construct B_s by induction on |s|.

**Level 0**: B_∅ = Y (or we can take B_∅ = closure of f(A) if we want, but Y is fine).

**Level 1**: f(A_{(n)}) are pairwise disjoint analytic sets (since A_{(n)} are pairwise disjoint and f is injective). By Lusin's separation theorem, there exist pairwise disjoint Borel sets C_n ⊃ f(A_{(n)}).

Now, we also want diam(C_n) → 0 as... well, not exactly, but we want the B_s to have vanishing diameter at deeper levels. For level 1, we just need C_n to be Borel and disjoint.

Actually, for the vanishing diameter, we need to be more careful. Let me think.

We have diam(f(A_s)) → 0 as |s| → ∞ (by our choice of the Lusin scheme). We want B_s ⊃ f(A_s) with diam(B_s) → 0.

At level 1: f(A_{(n)}) has some diameter. We choose B_{(n)} ⊃ f(A_{(n)}) Borel, with B_{(n)} pairwise disjoint. We don't need B_{(n)} to have small diameter yet.

At level 2: f(A_{(n,m)}) ⊂ f(A_{(n)}) has small diameter (for large enough n+m... well, diam(f(A_{(n,m)})) → 0 as |(n,m)| = n+m+k... hmm, the diameter depends on the length |s|, not on the specific values). So diam(f(A_{(n,m)})) is small when |s| = 2 is large? No, |s| = 2 is fixed. The diameter goes to 0 as |s| → ∞, meaning as we go deeper in the tree.

So at level k, diam(f(A_s)) is small (for |s| = k, with k large). We want B_s (at level k) to also have small diameter.

Here's how: at each level, when we separate f(A_{s⌢n}) within B_s, we choose the separating Borel sets to be contained in small neighborhoods of f(A_{s⌢n}).

Specifically, for each s and n, f(A_{s⌢n}) is analytic and has diameter < ε_{|s|+1} (where ε_k → 0). We can find a Borel set B_{s⌢n} with f(A_{s⌢n}) ⊂ B_{s⌢n} ⊂ {y : d(y, f(A_{s⌢n})) < ε_{|s|+1}}. Then diam(B_{s⌢n}) < 2ε_{|s|+1} + diam(f(A_{s⌢n})) < 3ε_{|s|+1} → 0.

But we also need B_{s⌢n} to be pairwise disjoint (for fixed s, varying n). Since f(A_{s⌢n}) are pairwise disjoint analytic sets, by the separation theorem, there exist pairwise disjoint Borel sets D_n ⊃ f(A_{s⌢n}). Then B_{s⌢n} = D_n ∩ {y : d(y, f(A_{s⌢n})) < ε_{|s|+1}} is Borel, contains f(A_{s⌢n}), has small diameter, and the B_{s⌢n} are pairwise disjoint (since D_n are disjoint). ✓

And B_{s⌢n} ⊂ D_n ⊂ B_s (we need D_n ⊂ B_s; we can ensure this by separating within B_s, i.e., applying the separation theorem to the analytic sets f(A_{s⌢n}) as subsets of the Polish space B_s). ✓

So the construction works. ∎

Now, there's one more thing I need to verify: the existence of the Lusin scheme (A_s) with the property that diam(f(A_s)) → 0.

Since f is a homeomorphism from A (subspace of X) to B = f(A) (subspace of Y), the metric d_Y on Y induces a metric d_Y ∘ (f × f) on A, which is compatible with the subspace topology on A (from X). 

A is Borel in X, hence A is a Lusin space: there exists a Lusin scheme (A_s) for A with diam_X(A_s) → 0. But we need diam_Y(f(A_s)) → 0.

Since f is a homeomorphism, the topology on A induced by d_Y ∘ (f × f) is the same as the subspace topology from X. So A is also Borel (hence Lusin) with respect to this metric. Therefore, there exists a Lusin scheme (A_s) for A with diam_{d_Y ∘ (f×f)}(A_s) → 0, which means diam_Y(f(A_s)) → 0. ✓

Great, so the proof is complete. Let me also handle the case where A is countable (which is simpler) and make sure the proof covers all cases.

If A is countable, then f(A) is countable (since f is injective), and countable subsets of a Polish space are Borel (they're F_σ). So the result is trivial in this case.

If A is uncountable, the Lusin scheme construction applies.

Actually, the Lusin scheme construction works for all Borel sets, countable or not. A countable Borel set can be written as a countable union of singletons, and singletons are closed, so we can build a Lusin scheme. But the argument above works in general.

Let me now write up the complete proof cleanly.

---

Actually, wait. I need to double-check one thing: the Lusin separation theorem is applied to separate countably many pairwise disjoint analytic sets. The standard Lusin separation theorem separates two disjoint analytic sets. For countably many, we apply it iteratively:

Given pairwise disjoint analytic sets A_1, A_2, A_3, ..., we separate A_1 from ⋃_{n≥2} A_n (which is analytic, being a countable union of analytic sets). This gives a Borel set B_1 with A_1 ⊂ B_1, B_1 ∩ (⋃_{n≥2} A_n) = ∅. Then separate A_2 from ⋃_{n≥3} A_n within Y \ B_1, getting B_2, etc. This gives pairwise disjoint Borel sets B_n ⊃ A_n. ✓

Also, I should note that the separation theorem requires the analytic sets to be in a Polish space. In our case, f(A_{s⌢n}) are analytic subsets of Y (Polish), so this is fine. When we separate within B_s, we need B_s to be a Polish space (or at least a standard Borel space). B_s is Borel in Y, hence a standard Borel space, and we can give it a Polish topology. The separation theorem applies to standard Borel spaces (or we can just work in Y and separate there). ✓

Let me also verify: is the countable union of analytic sets analytic? Yes, analytic sets are closed under countable unions. ✓

And is the intersection ⋂_k B_{α|k} a single point when diam(B_{α|k}) → 0? In a Polish space (which is complete and separable), a decreasing sequence of nonempty closed sets with vanishing diameter has a singleton intersection (by the Cantor intersection theorem, using completeness). But B_s are Borel, not necessarily closed. So ⋂_k B_{α|k} might not be a single point even if diam(B_{α|k}) → 0.

Hmm, this is a problem. Let me fix this.

We need ⋂_k B_{α|k} to be a single point (or at most a singleton). If B_s are not closed, the intersection might be larger.

**Fix**: We can take B_s to be closed (or at least ensure the intersection is at most a singleton).

Option 1: Choose B_s to be closed. But the separation theorem gives Borel sets, not necessarily closed.

Option 2: Instead of requiring ⋂_k B_{α|k} to be a singleton, use a different argument.

Actually, let me reconsider. We have:
- y ∈ ⋂_k B_{α|k}
- f(x_α) ∈ ⋂_k f(A_{α|k}) ⊂ ⋂_k B_{α|k}
- diam(B_{α|k}) → 0

Even if B_s are not closed, if diam(B_{α|k}) → 0 and both y and f(x_α) are in B_{α|k} for all k, then d(y, f(x_α)) ≤ diam(B_{α|k}) → 0, so d(y, f(x_α)) = 0, hence y = f(x_α). ✓

So we don't need the intersection to be a singleton a priori; the vanishing diameter ensures that any two points in the intersection are equal. ✓

So the proof works even with B_s being Borel (not necessarily closed). The key is that diam(B_s) → 0, which forces ⋂_k B_{α|k} to be at most a singleton, and since f(x_α) is in the intersection, it's exactly {f(x_α)}.

Great, the proof is complete. Let me write it up.

Actually, let me also make sure about one more detail: we need the Borel sets B_s to satisfy B_{s⌢n} ⊂ B_s. In the construction, when we separate f(A_{s⌢n}) within B_s, we get Borel sets D_n ⊂ B_s with D_n ⊃ f(A_{s⌢n}) and D_n pairwise disjoint. Then B_{s⌢n} = D_n ∩ (small ball around f(A_{s⌢n})) ⊂ D_n ⊂ B_s. ✓

And R_s = B_s \ ⋃_n B_{s⌢n} is Borel (B_s is Borel, ⋃_n B_{s⌢n} is Borel). ✓

And ⋃_s R_s is a countable union (since ω^{<ω} is countable) of Borel sets, hence Borel. ✓

And ⋃_n B_{(n)} is a countable union of Borel sets, hence Borel. ✓

So f(A) = (⋃_n B_{(n)}) \ (⋃_s R_s) is Borel. ✓

The proof is complete. Let me write it up cleanly now.

Let me also think about whether I need to prove the Lusin separation theorem or can just state it. Since this is a proof for a problem, I should either prove it or clearly state it as a known result. Given the complexity, I'll state it as a known result with a brief sketch.

Actually, for a complete proof, let me include a proof of the separation theorem as well, or at least a clear sketch.

**Lusin's Separation Theorem**: If A₁, A₂ are disjoint analytic subsets of a Polish space Z, there exists a Borel set C with A₁ ⊂ C and C ∩ A₂ = ∅.

**Proof sketch**: 

Analytic sets can be represented via trees. If A is analytic, there's a tree T on ω × ω such that A = {x : ∃y ∈ ω^ω, (x|k, y|k) ∈ T for all k} = proj(T), where T is a tree on ω × ω (i.e., a set of pairs (s, t) with s, t ∈ ω^{<ω}, |s| = |t|, closed under initial segments).

If A₁ and A₂ are disjoint analytic sets with corresponding trees T₁ and T₂, then for every x, it's not the case that both T₁(x) and T₂(x) have infinite branches (where T_i(x) is the section of T_i at x). 

The proof constructs a Borel set separating A₁ and A₂ by a transfinite induction on the "derivative" of the trees. Define the derivative T' of a tree T as T' = {s ∈ T : s has at least two incompatible extensions in T}. Iterate this transfinitely: T^(α+1) = (T^(α))', T^(λ) = ⋂_{α<λ} T^(α). For a well-founded tree (no infinite branch), this process stabilizes at ∅ for some countable ordinal.

The key insight: since A₁ ∩ A₂ = ∅, for every x ∈ A₁, the tree T₂(x) is well-founded (has no infinite branch). The set of x where T₂(x) is well-founded is co-analytic, and the set of x where T₁(x) has an infinite branch is analytic (= A₁). 

The separating Borel set is constructed using the ranks of the well-founded trees T₂(x) for x ∈ A₁. Specifically, one shows that the ranks are bounded on A₁ (by the boundedness theorem, since A₁ is analytic and the rank function is a co-analytic rank), and uses this bound to construct a Borel separating set.

This is a standard result in descriptive set theory. ∎

OK, I think for the purpose of this problem, I can state the separation theorem and Souslin's theorem as known results and give the main proof. Let me write the complete proof now.

Let me organize the proof:

1. State the key tools (analytic sets, separation theorem, Souslin's theorem).
2. Prove the main result using these tools.
3. The main proof uses: Lusin scheme for Borel sets, separation theorem to construct Borel approximations, and a decomposition argument.

Here's my final write-up:

---

**Theorem**: Let X and Y be Polish spaces, A ⊂ X a Borel subset, and f: A → B ⊂ Y a homeomorphism. Then B is a Borel subset of Y.

**Proof**:

We prove a stronger result (the Lusin–Suslin theorem): if A ⊂ X is Borel (X Polish) and f: A → Y is injective Borel (Y Polish), then f(A) is Borel in Y. Since a homeomorphism is in particular an injective Borel map (continuous ⟹ Borel), the theorem follows.

We use three standard tools from descriptive set theory:

**(i) Analytic sets.** A subset E of a Polish space Z is *analytic* (Σ¹₁) if E is the projection of a closed set in Z × ω^ω, equivalently, the continuous image of ω^ω. Borel sets are analytic, and the class of analytic sets is closed under countable unions and countable intersections, as well as under Borel images: if E is analytic and g is Borel, then g(E) is analytic.

**(ii) Lusin's Separation Theorem.** If E₁, E₂ are disjoint analytic subsets of a Polish space Z, there exists a Borel set C ⊂ Z with E₁ ⊂ C and E₂ ∩ C = ∅. By iterating, countably many pairwise disjoint analytic sets can be enclosed in pairwise disjoint Borel sets.

**(iii) Souslin's Theorem.** A subset of a Polish space is Borel if and only if it is both analytic and co-analytic (its complement is analytic). This follows from (ii): if E and Z\E are both analytic, they are disjoint analytic sets, so a Borel separator C with E ⊂ C, (Z\E) ∩ C = ∅ must satisfy C = E.

---

**Main proof.** Since A is Borel (hence analytic) and f is Borel, f(A) is analytic by (i). By Souslin's theorem (iii), it suffices to show that Y \ f(A) is analytic. We will in fact show directly that f(A) is Borel.

**Step 1 (Lusin scheme for A).** Since A is Borel in X and f is a homeomorphism, we can build a *Lusin scheme* (A_s)_{s ∈ ω^{<ω}} for A that is compatible with the metric on Y via f. Concretely, there exist Borel sets A_s ⊂ A (s ∈ ω^{<ω}) such that:

- A_∅ = A and A_s = ⋃_{n∈ω} A_{s⌢n} for every s,
- A_s ∩ A_t = ∅ whenever s, t ∈ ω^{<ω} are incompatible (neither s ⊂ t nor t ⊂ s),
- for each x ∈ A there is a unique α ∈ ω^ω with x ∈ ⋂_k A_{α|k}, and this intersection equals {x},
- diam_Y(f(A_s)) → 0 as |s| → ∞.

*Justification.* A is a Borel subset of the Polish space X, hence a Lusin space: it admits a complete separable metric compatible with its topology. Since f is a homeomorphism, the metric d_Y ∘ (f × f) on A is also compatible with A's topology. Building a Lusin scheme with respect to this metric gives the vanishing diameter condition on f(A_s). ∎

**Step 2 (Borel approximation scheme).** We construct Borel sets B_s ⊂ Y (s ∈ ω^{<ω}) with:

(a) f(A_s) ⊂ B_s for every s,
(b) B_{s⌢n} ⊂ B_s for every s, n,
(c) B_{s⌢n} ∩ B_{s⌢m} = ∅ for n ≠ m (pairwise disjoint at each level),
(d) diam(B_s) → 0 as |s| → ∞.

*Construction by induction on |s|.* Set B_∅ = Y. Suppose B_s is given (Borel, containing f(A_s)). The sets f(A_{s⌢n}) (n ∈ ω) are pairwise disjoint analytic subsets of Y (analytic by (i); disjoint because f is injective and the A_{s⌢n} are disjoint). By the separation theorem (ii), there exist pairwise disjoint Borel sets D_n ⊂ B_s with f(A_{s⌢n}) ⊂ D_n. Since diam(f(A_{s⌢n})) → 0, choose ε_{|s|+1} > 0 with ε_k → 0 and define

  B_{s⌢n} = D_n ∩ {y ∈ Y : d_Y(y, f(A_{s⌢n})) < ε_{|s|+1}}.

Then B_{s⌢n} is Borel, contains f(A_{s⌢n}), is contained in B_s (since D_n ⊂ B_s), the B_{s⌢n} are pairwise disjoint (since the D_n are), and diam(B_{s⌢n}) ≤ 2ε_{|s|+1} + diam(f(A_{s⌢n})) → 0. ∎

**Step 3
