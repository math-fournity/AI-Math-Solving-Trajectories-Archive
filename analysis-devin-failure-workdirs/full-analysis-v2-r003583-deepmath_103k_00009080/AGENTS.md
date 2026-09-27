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

- **CONNECTION_ERROR**: The AI didn't really attempt the problem. The thinking is very short, contains connection errors, or has no meaningful mathematical content. This is a technical failure, not a mathematical one.

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
  <problem_id>deepmath_103k_00009080</problem_id>
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
- If the AI's thinking is too short to analyze (< 500 chars of mathematical content), output CONNECTION_ERROR
- If you cannot determine the turning point type, use "other" and explain in dimension2_explanation

## Problem

Calculate \( \operatorname{Cov}(X + 3, XZ) \) given that \( f_X(x) = \begin{cases} 4x^3 &, \text{if} \ 0 < x < 1 \\\ 0 &, \text{otherwise} \end{cases} \), where \( Z \sim N(1,2) \) and \( X \) and \( Z \) are independent.

## Standard Solution

Okay, so I need to calculate the covariance between \( X + 3 \) and \( XZ \). Let me recall that covariance is defined as \( \operatorname{Cov}(A, B) = E[AB] - E[A]E[B] \). So in this case, that would be \( E[(X + 3)(XZ)] - E[X + 3]E[XZ] \). Let me write that down step by step.

First, expand the product inside the expectation: \( (X + 3)(XZ) = X \cdot XZ + 3 \cdot XZ = X^2Z + 3XZ \). So, the covariance becomes:

\[
\operatorname{Cov}(X + 3, XZ) = E[X^2Z + 3XZ] - E[X + 3]E[XZ]
\]

Let me split the expectations into separate terms. The first term is \( E[X^2Z] + 3E[XZ] \). Then the second part is \( (E[X] + 3)E[XZ] \). So putting it all together:

\[
\operatorname{Cov}(X + 3, XZ) = E[X^2Z] + 3E[XZ] - (E[X] + 3)E[XZ]
\]

Simplify the expression by distributing the second term:

\[
= E[X^2Z] + 3E[XZ] - E[X]E[XZ] - 3E[XZ]
\]

Ah, the \( 3E[XZ] \) and \( -3E[XZ] \) terms cancel each other out. So we're left with:

\[
\operatorname{Cov}(X + 3, XZ) = E[X^2Z] - E[X]E[XZ]
\]

Now, since \( X \) and \( Z \) are independent, I remember that the expectation of the product of independent variables is the product of their expectations. Wait, so does that apply here? Let me check each term.

First, \( E[X^2Z] \). Since \( X \) and \( Z \) are independent, \( X^2 \) and \( Z \) are also independent. Because if \( X \) is independent of \( Z \), then any function of \( X \) is independent of any function of \( Z \). So, \( E[X^2Z] = E[X^2]E[Z] \).

Similarly, \( E[XZ] = E[X]E[Z] \), again because \( X \) and \( Z \) are independent. Therefore, substituting these into our expression:

\[
\operatorname{Cov}(X + 3, XZ) = E[X^2]E[Z] - E[X] \cdot E[X]E[Z]
\]

Factor out \( E[Z] \):

\[
= E[Z] \left( E[X^2] - (E[X])^2 \right )
\]

But \( E[X^2] - (E[X])^2 \) is the variance of \( X \), \( \operatorname{Var}(X) \). So,

\[
\operatorname{Cov}(X + 3, XZ) = E[Z] \cdot \operatorname{Var}(X)
\]

That simplifies things a lot! So now I just need to compute \( E[Z] \), \( \operatorname{Var}(X) \), and plug them in.

Given that \( Z \sim N(1, 2) \), the mean of \( Z \) is 1. So \( E[Z] = 1 \).

Now, for \( X \), the pdf is given as \( f_X(x) = 4x^3 \) for \( 0 < x < 1 \). Let's compute \( E[X] \) and \( E[X^2] \).

First, \( E[X] = \int_{0}^{1} x \cdot 4x^3 dx = 4 \int_{0}^{1} x^4 dx \). The integral of \( x^4 \) is \( x^5 / 5 \), so:

\[
E[X] = 4 \left[ \frac{x^5}{5} \right]_0^1 = 4 \cdot \frac{1}{5} = \frac{4}{5}
\]

Next, \( E[X^2] = \int_{0}^{1} x^2 \cdot 4x^3 dx = 4 \int_{0}^{1} x^5 dx \). The integral of \( x^5 \) is \( x^6 / 6 \):

\[
E[X^2] = 4 \left[ \frac{x^6}{6} \right]_0^1 = 4 \cdot \frac{1}{6} = \frac{4}{6} = \frac{2}{3}
\]

Therefore, the variance \( \operatorname{Var}(X) = E[X^2] - (E[X])^2 = \frac{2}{3} - \left( \frac{4}{5} \right)^2 \).

Calculating that:

First, compute \( \left( \frac{4}{5} \right)^2 = \frac{16}{25} \). Then, express \( \frac{2}{3} \) with denominator 25. Let's see:

\( \frac{2}{3} = \frac{2 \times 25}{3 \times 25} = \frac{50}{75} \)

But maybe better to convert both fractions to common denominators. Let's use 75 as the common denominator:

\( \frac{2}{3} = \frac{50}{75} \) and \( \frac{16}{25} = \frac{48}{75} \)

Therefore:

\[
\operatorname{Var}(X) = \frac{50}{75} - \frac{48}{75} = \frac{2}{75}
\]

Alternatively, compute decimal values:

\( \frac{2}{3} \approx 0.6667 \), \( \frac{16}{25} = 0.64 \), so \( 0.6667 - 0.64 = 0.0267 \), which is \( \frac{2}{75} \approx 0.026666... \). That checks out.

So, putting it all together:

\[
\operatorname{Cov}(X + 3, XZ) = E[Z] \cdot \operatorname{Var}(X) = 1 \cdot \frac{2}{75} = \frac{2}{75}
\]

Wait, but let me double-check. Because covariance ended up being E[Z] times Var(X). That seems straightforward. Let me verify if all the steps make sense.

Starting from Cov(X + 3, XZ) = E[X^2Z] - E[X]E[XZ]. Then, since X and Z are independent, E[X^2Z] = E[X^2]E[Z], and E[XZ] = E[X]E[Z]. Therefore, substituting:

Cov = E[X^2]E[Z] - E[X] * E[X]E[Z] = E[Z](E[X^2] - (E[X])^2) = E[Z]Var(X). Yep, that seems correct.

So since E[Z] = 1, and Var(X) = 2/75, then Cov(X + 3, XZ) = 2/75. Therefore, the answer should be 2/75.

But let me check the variance calculation again. Maybe I miscalculated?

Given f_X(x) = 4x^3 on (0,1). Then E[X] = integral from 0 to1 of x*4x^3 dx = 4 integral x^4 dx = 4*(1/5) = 4/5. Correct.

E[X^2] = integral from 0 to1 of x^2*4x^3 dx = 4 integral x^5 dx = 4*(1/6) = 4/6 = 2/3. Correct.

So Var(X) = 2/3 - (4/5)^2. Let me compute this precisely:

2/3 - 16/25. To subtract these fractions:

Convert to common denominator, which is 75.

2/3 = 50/75

16/25 = 48/75

50/75 - 48/75 = 2/75. Exactly. So Var(X) = 2/75. Correct.

Therefore, Cov = 1 * 2/75 = 2/75.

So the answer is 2/75.

But wait, I want to make sure that the independence between X and Z is correctly applied. Since X and Z are independent, then any function of X is independent of any function of Z. So X^2 is independent of Z, and X is independent of Z. Therefore, when calculating E[X^2Z], it splits into E[X^2]E[Z], and E[XZ] splits into E[X]E[Z]. So all the steps are correct.

Therefore, the covariance is indeed 2/75. Hmm, seems right. Let me just recap all steps once more to be thorough.

1. Covariance formula: Cov(A,B) = E[AB] - E[A]E[B].

2. Let A = X + 3, B = XZ.

3. Compute E[AB] = E[(X + 3)(XZ)] = E[X^2Z + 3XZ] = E[X^2Z] + 3E[XZ].

4. Compute E[A] = E[X + 3] = E[X] + 3.

5. Compute E[B] = E[XZ].

6. So Cov = (E[X^2Z] + 3E[XZ]) - (E[X] + 3)(E[XZ]).

7. Expand the second term: E[X]E[XZ] + 3E[XZ].

8. Then Cov = E[X^2Z] + 3E[XZ] - E[X]E[XZ] - 3E[XZ].

9. The 3E[XZ] terms cancel, leaving Cov = E[X^2Z] - E[X]E[XZ].

10. Since X and Z are independent, E[X^2Z] = E[X^2]E[Z], and E[XZ] = E[X]E[Z].

11. Substitute back: Cov = E[X^2]E[Z] - E[X] * E[X]E[Z] = E[Z](E[X^2] - (E[X])^2) = E[Z]Var(X).

12. Given E[Z] = 1, Var(X) = 2/75, so Cov = 1*(2/75) = 2/75.

All steps check out. Therefore, the covariance is 2/75. I think that's the answer.

**Final Answer**
\boxed{\dfrac{2}{75}}
</think>

To calculate \( \operatorname{Cov}(X + 3, XZ) \), we use the covariance formula:

\[
\operatorname{Cov}(A, B) = E[AB] - E[A]E[B]
\]

Here, \( A = X + 3 \) and \( B = XZ \). Expanding the product inside the expectation:

\[
(X + 3)(XZ) = X^2Z + 3XZ
\]

Thus, the covariance becomes:

\[
\operatorname{Cov}(X + 3, XZ) = E[X^2Z + 3XZ] - E[X + 3]E[XZ]
\]

Splitting the expectations:

\[
= E[X^2Z] + 3E[XZ] - (E[X] + 3)E[XZ]
\]

Simplifying the expression:

\[
= E[X^2Z] + 3E[XZ] - E[X]E[XZ] - 3E[XZ]
\]

The terms \( 3E[XZ] \) and \( -3E[XZ] \) cancel out, leaving:

\[
\operatorname{Cov}(X + 3, XZ) = E[X^2Z] - E[X]E[XZ]
\]

Since \( X \) and \( Z \) are independent, we use the property that the expectation of the product of independent variables is the product of their expectations:

\[
E[X^2Z] = E[X^2]E[Z] \quad \text{and} \quad E[XZ] = E[X]E[Z]
\]

Substituting these into the covariance expression:

\[
\operatorname{Cov}(X + 3, XZ) = E[X^2]E[Z] - (E[X])^2E[Z] = E[Z] \left( E[X^2] - (E[X])^2 \right)
\]

This simplifies to:

\[
\operatorname{Cov}(X + 3, XZ) = E[Z] \cdot \operatorname{Var}(X)
\]

Given \( Z \sim N(1, 2) \), we have \( E[Z] = 1 \). For \( X \), with pdf \( f_X(x) = 4x^3 \) on \( (0, 1) \):

\[
E[X] = \int_{0}^{1} x \cdot 4x^3 \, dx = \frac{4}{5}
\]

\[
E[X^2] = \int_{0}^{1} x^2 \cdot 4x^3 \, dx = \frac{2}{3}
\]

The variance of \( X \) is:

\[
\operatorname{Var}(X) = E[X^2] - (E[X])^2 = \frac{2}{3} - \left( \frac{4}{5} \right)^2 = \frac{2}{75}
\]

Thus, the covariance is:

\[
\operatorname{Cov}(X + 3, XZ) = 1 \cdot \frac{2}{75} = \frac{2}{75}
\]

\[
\boxed{\dfrac{2}{75}}
\]

## AI's Thinking (Attempted Solution Process)

The problem asks whether there exists a family of regular dense graphs with girth at least 5, where every maximal independent set has size at least Ω(n), with n nodes and m ≥ n^{1+ε} edges for some constant ε > 0.

Let me think about this carefully.

First, let me check for answer leaks. The problem statement is clean - no solutions, no proof sketches, no answer values. Good.

Now let me think about the problem.

We need: a family of regular graphs, girth ≥ 5, m ≥ n^{1+ε}, and every maximal independent set has size ≥ Ω(n).

Key concepts:
- Girth ≥ 5 means no triangles and no 4-cycles.
- Regular graph with m ≥ n^{1+ε} means degree d = 2m/n ≥ n^ε, so the graph is "dense" in the sense that degree grows with n.
- Every maximal independent set has size ≥ Ω(n) — this is a strong expansion-like property.

A maximal independent set (MIS) is an independent set that cannot be extended. The size of every MIS being Ω(n) is related to the graph having good "expansion" properties or being "well-spread".

Let me think about what makes every MIS large. 

In a d-regular graph, a maximal independent set I has the property that every vertex not in I has a neighbor in I. So I is a dominating set. The size of a minimum maximal independent set is the "independent domination number" i(G).

We want i(G) = Ω(n) for all maximal independent sets, i.e., the minimum maximal independent set is Ω(n).

Actually, we want every MIS to be Ω(n), which means even the smallest MIS is Ω(n). So we need i(G) ≥ c·n for some constant c > 0.

For a d-regular graph with girth ≥ 5:
- By a greedy argument, any maximal independent set has size at least n/(d+1) (since each vertex in I dominates at most d+1 vertices including itself). But this gives n/(d+1) = n/n^ε = n^{1-ε}, which is not Ω(n) when d → ∞.

Wait, so the trivial bound gives n/(d+1) which is sublinear when d grows. So we need something better.

Hmm, but actually the question is whether such graphs EXIST. So we need to find a construction where despite high degree, every MIS is still Ω(n).

Let me think about this differently. The key insight might be related to expansion properties.

Consider a d-regular graph with girth ≥ 5. If the graph is a good expander, then small sets have large neighborhoods. 

For a maximal independent set I, let S = V \ I. Every vertex in S has a neighbor in I. Also, I is independent.

Actually, let me think about the complement. If I is a maximal independent set, then I is independent and I dominates V. 

The question is: can we have a d-regular graph (d → ∞) with girth ≥ 5 where every dominating independent set (i.e., maximal independent set) has size Ω(n)?

Let me think about random d-regular graphs. For random d-regular graphs with d large, the independence number is about (2n log d)/d. The minimum maximal independent set... hmm.

Actually, for random regular graphs, the size of the minimum maximal independent set (independent domination number) is roughly n·(log d)/d for large d. This is sublinear when d → ∞.

So random regular graphs won't work directly.

Let me think about what structure would force every MIS to be large.

Key idea: If the graph has the property that every small set S has |N(S)| ≥ c·|S| for some c > 1 (expansion), then... let's see.

If I is a maximal independent set of size α, then V \ I is dominated by I, meaning N(I) ⊇ V \ I, so |N(I)| ≥ n - α. But also, since I is independent and girth ≥ 5, the neighborhoods of vertices in I don't overlap too much.

Actually, with girth ≥ 5, for an independent set I, the neighborhoods N(v) for v ∈ I are disjoint (because if two vertices u, v ∈ I share a common neighbor w, then u-w-v is a path of length 2, but that's not a problem for girth ≥ 5... wait, that would be a cycle of length... no, u-w-v is just a path, not a cycle. For a cycle we'd need u-w-v-...-u).

Hmm wait. Girth ≥ 5 means no cycles of length 3 or 4. If u, v ∈ I share a neighbor w, then u-w-v is a path of length 2. This doesn't create a cycle. So neighborhoods of independent set vertices CAN overlap.

But if u, v ∈ I share TWO common neighbors w1, w2, then u-w1-v-w2-u is a 4-cycle, which is forbidden. So any two vertices in I share at most one common neighbor.

So for an independent set I in a girth ≥ 5 graph:
- Each v ∈ I has d neighbors.
- Any two vertices in I share at most 1 common neighbor.
- |N(I)| ≥ d|I| - C(|I|, 2) (by inclusion-exclusion, since pairwise intersections are at most 1).

Wait, more precisely: |N(I)| ≥ d|I| - Σ_{pairs} |N(u) ∩ N(v)| ≥ d|I| - C(|I|, 2).

For I to be maximal, N(I) ⊇ V \ I, so |N(I)| ≥ n - |I|.

So: d|I| - C(|I|, 2) ≥ n - |I|
d|I| - |I|(|I|-1)/2 ≥ n - |I|
|I|(d + 1) - |I|(|I|-1)/2 ≥ n
|I|(d + 1 - (|I|-1)/2) ≥ n

If |I| is small compared to d, say |I| ≤ d, then:
|I| · (d + 1 - d/2) ≈ |I| · d/2 ≥ n
So |I| ≥ 2n/d.

That gives |I| ≥ 2n/d = 2n/n^ε = 2n^{1-ε}, which is still sublinear.

Hmm, so the girth ≥ 5 condition alone with the counting argument gives only n^{1-ε}, not Ω(n).

So we need a stronger structural property. The question is whether such graphs exist.

Let me reconsider. Maybe we need expansion. If the graph is a good expander, then small independent sets can't dominate.

Let me think about it from the expansion angle. Suppose the graph is a d-regular expander with the property that for every set S with |S| ≤ n/2, |N(S) \ S| ≥ c|S| for some constant c > 0 (or even c depending on d).

If I is a maximal independent set with |I| = α ≤ n/2, then N(I) ⊇ V \ I, so |N(I)| ≥ n - α. But N(I) ⊆ V \ I (since I is independent, N(I) ∩ I = ∅... wait, no. N(I) is the set of neighbors of I, which could include vertices in I if I is not independent. But I IS independent, so N(I) ∩ I = ∅. So N(I) ⊆ V \ I.)

So |N(I)| ≤ n - α. But we also need N(I) ⊇ V \ I for maximality (every vertex in V \ I has a neighbor in I). So N(I) = V \ I exactly (since N(I) ⊆ V \ I and N(I) ⊇ V \ I).

Wait, that's not quite right. N(I) ⊆ V \ I because I is independent. And for maximality, every vertex in V \ I has a neighbor in I, so V \ I ⊆ N(I). Therefore N(I) = V \ I.

So |N(I)| = n - α.

Now, if the graph has expansion: for |I| ≤ n/2, |N(I)| ≥ c|I| (where c is some expansion factor). Then n - α ≥ cα, so α ≤ n/(1+c). That gives an upper bound on α, not a lower bound.

Hmm, that's the wrong direction. Expansion gives us that N(I) is large, which means V \ I is large, which means I is small. That's the opposite of what we want.

Wait, I think I'm confusing myself. Let me reconsider.

We want every MIS to be LARGE (Ω(n)). The "bad" case is when there exists a SMALL MIS. So we want to prevent small maximal independent sets.

A small MIS I means: I is independent, I is small, and I dominates V \ I (every vertex outside I has a neighbor in I).

To prevent small MIS, we need: for every small independent set I, I does NOT dominate V \ I, i.e., there exists a vertex in V \ I with no neighbor in I.

Equivalently: for every small independent set I, N(I) ≠ V \ I, i.e., there's a vertex outside I ∪ N(I).

So we need: for every independent set I with |I| = o(n), we have I ∪ N(I) ≠ V, i.e., |I ∪ N(I)| < n.

|I ∪ N(I)| = |I| + |N(I)| = |I| + |N(I)| (since I is independent, I ∩ N(I) = ∅).

We need |I| + |N(I)| < n for all small independent I.

But |N(I)| ≤ d|I|, so |I| + |N(I)| ≤ (d+1)|I|. If |I| < n/(d+1), then this is < n. But we need it for |I| up to cn for constant c.

Hmm, so the question becomes: can we have a d-regular graph (d → ∞) with girth ≥ 5 where for every independent set I with |I| ≤ cn (for some constant c), we have |N(I)| < n - |I|?

This is essentially saying that independent sets of linear size don't dominate. Or equivalently, the graph has no independent dominating set of sublinear size, and in fact no independent dominating set smaller than cn.

Let me think about this from a different angle. 

Consider the bipartite double cover or some algebraic construction.

Actually, let me think about specific constructions.

**Bipartite graphs**: A bipartite d-regular graph with girth ≥ 5. In a bipartite graph, each part is an independent set. If the graph is connected and bipartite with parts A, B of size n/2 each, then A is a maximal independent set of size n/2, and B is a maximal independent set of size n/2. But there could be other, smaller maximal independent sets.

Hmm, in a bipartite graph, can we have a small maximal independent set? Yes, potentially. For example, if there's a small set that dominates one side and is independent...

Actually, let me think about a specific construction.

**Ramanujan graphs / LPS graphs**: These are d-regular graphs with girth ~ (2/3)log_{d-1}(n) and good spectral expansion. But do they have the property that every MIS is Ω(n)?

For a d-regular graph with spectral gap (second eigenvalue λ), by the expander mixing lemma, for any set S, |N(S)| ≥ |S|(d - λ)/(something)... Actually, let me think more carefully.

For a d-regular graph with second eigenvalue λ (in absolute value), the expander mixing lemma says:
|e(S, T)| - d|S||T|/n ≤ λ√(|S||T|(1-|S|/n)(1-|T|/n))

For an independent set I, e(I, I) = 0, so:
-d|I|²/n ≥ -λ|I|(1-|I|/n) (approximately, for |I| ≤ n/2)
d|I|/n ≤ λ(1-|I|/n)
This gives |I| ≤ nλ/(d+λ) ≈ nλ/d for λ << d.

For Ramanujan graphs, λ = 2√(d-1), so |I| ≤ n·2√d/d = 2n/√d. This is the independence number bound.

But we care about maximal independent sets, not just maximum. The minimum maximal independent set could be much smaller.

Hmm, let me think about this more carefully.

Actually, I think the answer is YES, such graphs exist, and the key construction might be based on bipartite graphs or specific algebraic constructions.

Let me think about a different approach. 

**Approach via bipartite graphs with good expansion on both sides.**

Consider a d-regular bipartite graph G = (L, R, E) with |L| = |R| = n/2, girth ≥ 6 (which is ≥ 5), and d = n^ε.

In a bipartite graph, an independent set can include vertices from both L and R. A maximal independent set I must dominate: every vertex not in I has a neighbor in I.

Claim: If the bipartite graph is a good expander (specifically, if for every S ⊆ L with |S| ≤ n/4, |N(S)| ≥ c|S| for some c > 1, and similarly for R), then every MIS has size Ω(n).

Let me try to prove this. Let I be a maximal independent set. Let I_L = I ∩ L, I_R = I ∩ R.

Since I is independent, there are no edges between I_L and I_R. So N(I_L) ⊆ R \ I_R and N(I_R) ⊆ L \ I_L.

Since I is maximal, every vertex in L \ I_L has a neighbor in I (which must be in I_R, since I_L ⊆ L and neighbors of L are in R... wait, no. Vertices in L have neighbors in R. So a vertex in L \ I_L has a neighbor in I, and that neighbor is in R, so it's in I_R. So L \ I_L ⊆ N(I_R).)

Similarly, R \ I_R ⊆ N(I_L).

So:
|L \ I_L| ≤ |N(I_R)| ≤ d|I_R|
|R \ I_R| ≤ |N(I_L)| ≤ d|I_L|

From the first: n/2 - |I_L| ≤ d|I_R|
From the second: n/2 - |I_R| ≤ d|I_L|

Adding: n - |I_L| - |I_R| ≤ d(|I_L| + |I_R|)
n - |I| ≤ d|I|
n ≤ (d+1)|I|
|I| ≥ n/(d+1) = n^{1-ε}

This is the trivial bound again. Not enough.

But with expansion, we can do better. If |N(I_R)| ≥ c|I_R| for some c > 1 (when |I_R| is not too large), then:

n/2 - |I_L| ≤ |N(I_R)|, but also |N(I_R)| ≤ n/2 - |I_R| (since N(I_R) ⊆ R \ I_R).

Hmm, this gives n/2 - |I_L| ≤ n/2 - |I_R|, so |I_R| ≤ |I_L|. Similarly |I_L| ≤ |I_R|. So |I_L| = |I_R|, and |I| = 2|I_L|.

But this doesn't give us the lower bound we want.

Let me use expansion more carefully. Suppose the graph has the property that for every S ⊆ L with |S| ≤ n/4, |N(S)| ≥ c·|S| where c > 1. And similarly for subsets of R.

Case 1: |I_R| ≤ n/4. Then |N(I_R)| ≥ c|I_R|. But L \ I_L ⊆ N(I_R), so n/2 - |I_L| ≤ |N(I_R)|. Also, |N(I_R)| ≤ n/2 (trivially). 

Hmm, this gives n/2 - |I_L| ≤ |N(I_R)|, and |N(I_R)| ≤ d|I_R|, so n/2 - |I_L| ≤ d|I_R|.

With expansion: |N(I_R)| ≥ c|I_R|, but we need an upper bound on |N(I_R)| in terms of |I_R| to limit things... no, we need a lower bound on |I|.

Let me try a different approach. Let's use the expansion to bound |I_L| and |I_R| from below.

If |I_R| ≤ n/4, then by expansion, |N(I_R)| ≥ c|I_R|. Since L \ I_L ⊆ N(I_R), we have |L \ I_L| ≤ |N(I_R)|. But we also know |N(I_R)| ≤ n/2 - |I_R| (since N(I_R) ⊆ R \ I_R... wait, no. N(I_R) is in L, not R. I_R ⊆ R, so N(I_R) ⊆ L. And N(I_R) ⊆ L \ I_L (since I is independent, no edge between I_L and I_R, so N(I_R) ∩ I_L = ∅).

So N(I_R) ⊆ L \ I_L, and L \ I_L ⊆ N(I_R) (by maximality). So N(I_R) = L \ I_L.

Therefore |N(I_R)| = n/2 - |I_L|.

If |I_R| ≤ n/4, by expansion |N(I_R)| ≥ c|I_R|, so n/2 - |I_L| ≥ c|I_R|, giving |I_L| ≤ n/2 - c|I_R|.

Similarly, N(I_L) = R \ I_R, so |N(I_L)| = n/2 - |I_R|.

If |I_L| ≤ n/4, by expansion |N(I_L)| ≥ c|I_L|, so n/2 - |I_R| ≥ c|I_L|, giving |I_R| ≤ n/2 - c|I_L|.

Now, |I| = |I_L| + |I_R|. Let's denote a = |I_L|, b = |I_R|, N = n/2.

We have (when a, b ≤ N/2 = n/4):
- N - a ≥ cb → a ≤ N - cb
- N - b ≥ ca → b ≤ N - ca

From the first: a + cb ≤ N.
From the second: b + ca ≤ N.

Adding: (a+b)(1+c) ≤ 2N = n, so |I| ≤ n/(1+c). This is an upper bound, not useful.

Wait, I think I need to use expansion in the other direction. The issue is that expansion says N(S) is LARGE, which means L \ I_L is large, which means I_L is small. That's the wrong direction for our purposes.

Hmm, so expansion actually helps make MIS SMALL, not large. That's the opposite of what we want.

Wait, no. Let me reconsider. We want every MIS to be large. The "danger" is a small MIS. A small MIS I has small |I| but I ∪ N(I) = V. 

If I is small, then N(I) is large (close to n). But if the graph has expansion, then small sets have large neighborhoods, which actually HELPS small sets dominate. So expansion is bad for our purpose!

So we want the OPPOSITE of expansion in some sense. We want small independent sets to NOT dominate, i.e., their neighborhoods should be small relative to n.

But in a d-regular graph with d large, a set of size k has up to dk neighbors, which is large. So it seems hard to prevent small independent sets from dominating.

Wait, but the independent set constraint limits this. If I is independent and small, N(I) could still be up to d|I|, but the actual size depends on the structure.

Let me reconsider the problem. Maybe the answer is NO, such graphs don't exist?

Let me think about an upper bound on the minimum maximal independent set.

**Claim**: In any d-regular graph with d ≥ n^ε, there exists a maximal independent set of size O(n log d / d) = O(n^{1-ε} log n).

This would mean the answer is NO.

The greedy algorithm for maximal independent set: pick a vertex, add to I, remove it and its neighbors, repeat. Each step removes at most d+1 vertices. So the MIS has size at least n/(d+1). But we want an upper bound on the minimum MIS.

Actually, the greedy algorithm (picking vertices in some order) gives a maximal independent set. The size depends on the order. If we pick vertices randomly, the expected size is about n log(d+1)/(d+1) (this is a well-known result for the random greedy MIS).

For d-regular graphs, the random greedy MIS has expected size Θ(n log d / d) when d is not too large compared to n. For d = n^ε, this is Θ(n^{1-ε} · ε log n).

But wait, this is the EXPECTED size of a random greedy MIS. The minimum MIS could be even smaller. But actually, the random greedy gives an upper bound on the minimum MIS (since the minimum is at most the average, which is at most the expected value of any random process).

Hmm, but actually the random greedy MIS size depends on the graph structure. For general d-regular graphs, is it always O(n log d / d)?

Let me think more carefully. The random greedy algorithm: at each step, pick a uniformly random remaining vertex, add it to I, remove it and its neighbors. 

For a d-regular graph, when we pick a vertex v and remove it and its neighbors, we remove d+1 vertices (v and its d neighbors). But the neighbors of v might have already been removed. In the worst case (if the graph is a good expander and we haven't removed much), we remove about d+1 vertices per step.

The number of steps is about n/(d+1) in the worst case, but could be more if neighborhoods overlap.

Actually, the analysis of the random greedy MIS on a d-regular graph is subtle. For graphs with girth ≥ 5, the local structure is tree-like, and the analysis is cleaner.

For a d-regular graph with girth ≥ 5, the random greedy MIS has expected size Θ(n log d / d). This is because locally, the graph looks like a d-regular tree, and the greedy process on a d-regular tree selects a fraction ~log d / d of vertices.

So for d = n^ε, the random greedy MIS has expected size Θ(n^{1-ε} log n), which is o(n).

This means there EXISTS a maximal independent set of size O(n^{1-ε} log n) = o(n), which means NOT every MIS has size Ω(n).

Wait, but I need to be more careful. The random greedy MIS gives an upper bound on the minimum MIS only if the expected size is an upper bound on the minimum. Actually, the minimum MIS ≤ expected size of random greedy MIS, because the minimum is at most any particular realization, and hence at most the expectation. Yes, that's correct.

So if the random greedy MIS has expected size O(n log d / d) = O(n^{1-ε} log n) = o(n), then the minimum MIS is o(n), and hence not every MIS is Ω(n).

But wait, I need to verify that the random greedy MIS on a d-regular graph with girth ≥ 5 and d = n^ε indeed has expected size O(n log d / d).

The key fact: For a d-regular graph with girth g ≥ 2k+1, the random greedy MIS has expected size (1+o(1)) · n · (1 - (1-1/n)^{...}) ... hmm, let me think about this more carefully.

Actually, the standard result is: for a d-regular graph on n vertices with girth ≥ 2k+1 (for k = o(log n)), the random greedy MIS has size (1+o(1)) · n · c_d where c_d is the fraction of vertices selected by the greedy process on the infinite d-regular tree.

For the infinite d-regular tree, the greedy process selects a fraction c_d = (1 + o(1)) · (log d)/d of vertices when d is large.

More precisely, for the d-regular tree, the greedy algorithm (random ordering) selects each vertex with probability approximately (log d)/d for large d. This is a classical result.

So for a d-regular graph with girth ≥ 5 (which is ≥ 2·2+1 = 5, so k=2), the random greedy MIS has expected size approximately n · (log d)/d.

For d = n^ε, this is n · (ε log n) / n^ε = ε n^{1-ε} log n, which is o(n).

Therefore, there exists a maximal independent set of size O(n^{1-ε} log n) = o(n), which means NOT every maximal independent set has size Ω(n).

Wait, but I should double-check: does girth ≥ 5 suffice for this analysis? The girth ≥ 5 condition means the graph is locally tree-like up to radius 2 (no triangles or 4-cycles). For the greedy MIS analysis, we need the graph to be locally tree-like in the neighborhood of each vertex up to some radius. 

The standard result (e.g., from the work of Wormald and others) is that for d-regular graphs with girth ≥ 2k+1, the random greedy process is well-approximated by the process on the d-regular tree, as long as k is large enough (but k = O(log n / log d) suffices, and even k=2 gives a good approximation for the leading term).

Actually, let me be more precise. The result I'm thinking of is:

For a d-regular graph G on n vertices with girth ≥ g, the random greedy MIS has size (1 + o(1)) · n · p_d where p_d is the probability that the root is selected in the random greedy process on the infinite d-regular tree, provided that g → ∞ (or at least g ≥ c log n for some c).

But if g is only 5 (constant), the approximation might not hold exactly. However, the key point is that even with constant girth, the random greedy MIS can't be much larger than the tree prediction.

Hmm, actually, let me reconsider. With girth exactly 5 (constant), the graph could have many 5-cycles, 6-cycles, etc. The local structure is tree-like only up to radius 2. Beyond that, cycles could affect the analysis.

But actually, for the upper bound, we don't need the full tree approximation. We can use a simpler argument.

**Simpler argument**: Consider any d-regular graph G on n vertices (no girth assumption needed). We claim there exists a maximal independent set of size O(n log d / d).

Proof: Use the random greedy algorithm. Process vertices in random order. When we encounter a vertex that's still "alive" (not yet removed), add it to I and remove it and its neighbors.

At any point, let A be the number of alive vertices. When we pick a random alive vertex v and add it to I, we remove v and its alive neighbors. The expected number of alive neighbors of v is (sum of alive degrees of alive vertices) / A... hmm, this is getting complicated because the graph isn't regular anymore after removals.

Let me use a different approach. 

**Caro-Wei type bound or direct greedy analysis:**

Actually, let me use a cleaner argument. 

**Theorem (folklore/easy)**: In any d-regular graph on n vertices, there exists a maximal independent set of size at most n·(1 + ln(d+1))/(d+1).

Proof: Consider the following randomized algorithm. Assign each vertex a uniform random priority in [0,1]. Process vertices in order of priority. When processing vertex v, if v is still alive, add v to I and kill v and its neighbors.

A vertex v is added to I if and only if v has the smallest priority among {v} ∪ N(v) (i.e., v's priority is smaller than all its neighbors' priorities). Wait, that's not quite right because some neighbors might have been killed already.

Actually, the correct statement is: v is added to I if and only if v has the smallest priority among all vertices in {v} ∪ N(v) that are still alive when v is processed. But since we process in priority order, v is processed before any vertex with higher priority. So v is alive when processed if and only if no neighbor of v with smaller priority was added to I (which would kill v). 

v is added to I iff v is alive when processed, which happens iff no neighbor of v with smaller priority was added to I. A neighbor u of v with smaller priority was added to I iff u was alive when processed, which happens iff no neighbor of u with smaller priority was added to I, etc.

This is complex. Let me use a simpler bound.

**Simple bound**: Process vertices in any order. Greedily add to I. Each vertex added to I kills at most d+1 vertices (itself and d neighbors). So |I| ≥ n/(d+1). But this is a lower bound on the greedy MIS, not an upper bound on the minimum MIS.

For an upper bound on the minimum MIS, we need to show that SOME ordering gives a small MIS.

**Random ordering bound**: If we process vertices in random order, the probability that vertex v is added to I is at most 1/(d_v + 1) where d_v is the degree... no, that's the Caro-Wei bound for the MAXIMUM independent set.

Hmm, let me think again.

For the MAXIMAL independent set via random greedy: the probability that v is selected (added to I) is the probability that v is alive when it's processed. v is alive when processed iff no neighbor of v with a smaller random label was selected. 

In a d-regular graph, by symmetry and the tree-like approximation (for high girth), the probability that v is selected is approximately the probability that the root is selected in the greedy process on the d-regular tree.

For the d-regular tree, let p be the probability that the root is selected. The root is selected iff it has the smallest label among its neighbors (and itself). But it's more subtle because of the recursive structure.

Let me use the known result. For the random greedy MIS on a d-regular tree:
- Let p be the probability that the root is selected.
- The root is selected iff it has the smallest label among {root} ∪ N(root).
- But actually, the root is selected iff no neighbor of the root with a smaller label is selected, and the root has a smaller label than all selected... 

This is getting complicated. Let me just cite the known result.

**Known result**: For d-regular graphs with girth ≥ 2k+1 where k → ∞ (or k ≥ C log n / log d), the random greedy MIS has size (1+o(1)) · n · (log d / d) for large d.

But we only have girth ≥ 5 (constant). Does the result still hold?

For constant girth, the result might not hold exactly, but we can still get an upper bound.

**Alternative approach**: Let me directly construct a small maximal independent set.

**Claim**: In any d-regular graph G on n vertices, there exists a maximal independent set of size O(n log d / d).

Proof: We use the following algorithm. Initialize I = ∅, S = V. While S ≠ ∅:
1. Pick a vertex v uniformly at random from S.
2. Add v to I.
3. Remove v and N(v) from S.

Each iteration removes at most d+1 vertices from S but at least 1. The expected number of vertices removed per iteration is 1 + (expected number of alive neighbors of v).

The issue is that as the algorithm progresses, the alive subgraph becomes irregular, and the expected number of alive neighbors changes.

Let me use a cleaner approach based on the "differential equations" method or just a direct counting argument.

**Direct argument**: 

Consider a d-regular graph G on n vertices. We want to show there's a maximal independent set of size O(n log d / d).

Step 1: Find a large independent set α(G) ≥ n/(d+1) (by Turán/greedy). Actually, by the Caro-Wei bound, α(G) ≥ n/(d+1).

Step 2: Take a maximum independent set I_0. |I_0| ≥ n/(d+1). But we want a MAXIMAL independent set that's small, not large.

Hmm, let me think differently.

**Greedy from random order**: Process vertices in a uniformly random order π. Build a maximal independent set I greedily: for each vertex v in order, if v is not adjacent to any vertex in I, add v to I.

The resulting I is a maximal independent set. Its expected size is E[|I|] = Σ_v Pr[v ∈ I].

Pr[v ∈ I] = Pr[no neighbor of v appearing before v in π is in I].

This is hard to compute exactly, but we can bound it. 

For a d-regular graph with girth ≥ 5, the neighborhood of each vertex is an independent set of size d (no triangles), and no two neighbors of v share a common neighbor other than v (no 4-cycles). So the local structure around v up to distance 2 is like a tree.

In the random greedy process on the d-regular tree, the probability that the root is selected is known to be:

p_d = (1 + o(1)) · (log d) / d as d → ∞.

This is a classical result (see, e.g., the analysis by Wormald, or by Gamarnik and Goldberg).

For a d-regular graph with girth ≥ 5, the probability that a specific vertex v is selected in the random greedy MIS is approximately p_d, because the process is determined by the local neighborhood up to the point where v is processed, and with girth ≥ 5, the neighborhood up to distance 2 is tree-like.

More precisely, for girth ≥ 2k+1, the probability that v is selected differs from p_d by at most O(d^{-k}) or something like that. With k=2 (girth ≥ 5), the error is O(1/d) or O(1/d²), which is negligible for large d.

Actually, I realize I should be more careful. Let me look at this from a different angle.

**Key insight**: Even without the full tree approximation, we can prove that the random greedy MIS has expected size O(n log d / d) for any d-regular graph.

Here's a cleaner argument:

**Lemma**: In any d-regular graph G on n vertices, the random greedy MIS (random ordering) has expected size at most n · (1 + ln(d+1)) / (d+1).

Proof: We use the following observation. For a vertex v, let X_v be the indicator that v is selected. Then E[|I|] = Σ_v E[X_v].

Now, Pr[X_v = 1] = Pr[v has the minimum label among {v} ∪ N(v) ∩ A_v] where A_v is the set of alive vertices when v is considered. But this is hard to work with.

Alternative: Use the fact that the greedy MIS is at most the size of any specific independent set plus the number of vertices that are "wasted" (killed but not added to I).

Hmm, let me try yet another approach.

**Approach via independent set + domination:**

A maximal independent set is an independent set that is also a dominating set. So we want to find an independent dominating set that's small.

**Step 1**: Find a small dominating set D. In a d-regular graph, a dominating set of size O(n log d / d) exists (by the probabilistic method: each vertex dominates d+1 vertices, so a random set of size (n log d / d) dominates w.h.p.).

**Step 2**: From D, construct an independent dominating set. This is the tricky part.

Actually, the standard way to get a small maximal independent set is:

1. Find a small independent set I_1 (e.g., via greedy).
2. Extend I_1 to a maximal independent set by greedily adding vertices.

But this gives a maximal independent set that's at least as large as I_1, which could be large.

Alternatively:

1. Find a small dominating set D.
2. Extract an independent set from D (which might be smaller).
3. Extend to a maximal independent set.

This doesn't directly work either.

Let me go back to the random greedy approach and try to prove the bound directly.

**Theorem**: For any d-regular graph G on n vertices with d ≥ 2, the random greedy MIS has expected size at most n(1 + ln d)/d.

Proof: We use a coupling argument. Consider the random greedy process. At each step, a uniformly random alive vertex is selected and added to I, and it and its alive neighbors are killed.

Let A_t be the number of alive vertices after t steps, and let D_t be the total number of alive edges (edges between alive vertices). Initially A_0 = n, D_0 = nd/2.

When we select a random alive vertex v at step t+1:
- v is killed (1 vertex).
- Each alive neighbor of v is killed.
- The number of alive neighbors of v is deg_t(v) (its alive degree).

E[killed vertices] = 1 + E[deg_t(v)] = 1 + D_t · 2 / A_t (since the average alive degree is 2D_t/A_t, and v is chosen uniformly at random from alive vertices, so E[deg_t(v)] = 2D_t/A_t).

Wait, actually E[deg_t(v)] = (1/A_t) Σ_{alive u} deg_t(u) = 2D_t / A_t.

So E[A_{t+1}] = A_t - 1 - 2D_t/A_t.

And the change in D: when v and its neighbors are killed, we remove all edges incident to v and its neighbors. The number of edges removed is deg_t(v) + Σ_{u ∈ N_t(v)} (deg_t(u) - 1) (subtracting 1 for the edge to v which is counted twice). Actually, it's easier to think of it as: we remove all edges incident to the killed vertices.

This is getting complicated. Let me just use the known result.

**Known result (see e.g., Wormald 1999, "Models of random regular graphs")**: For d-regular graphs with girth ≥ 2k+1, as n → ∞ with d fixed or growing, the random greedy MIS has size (1+o(1)) n p_d where p_d is the tree value. For large d, p_d ~ (log d)/d.

For our problem, d = n^ε → ∞, and girth ≥ 5. The tree value p_d ~ (log d)/d = ε(log n)/n^ε.

So the random greedy MIS has expected size ~ n · ε(log n)/n^ε = ε n^{1-ε} log n = o(n).

Since the expected size is o(n), there exists a maximal independent set of size o(n), and hence not every maximal independent set has size Ω(n).

But wait, I need to be more careful about whether the tree approximation holds when girth is only 5 (constant) and d is growing.

Let me think about this more carefully. The issue is that with girth = 5 (constant), the graph has cycles of length 5, 6, 7, etc., and the local structure is only tree-like up to distance 2. For the random greedy MIS, the probability that a vertex v is selected depends on the process in its neighborhood, which could extend beyond distance 2.

However, the key insight is that the probability that v is selected is at most 1/(number of alive vertices in {v} ∪ N(v) when v is processed). In the best case (for making I small), many of v's neighbors are alive, and the probability is about 1/(d+1). But the actual probability could be higher if many neighbors are already dead.

Hmm, but we want an UPPER bound on E[|I|] (to show that some MIS is small). So we need to show that E[|I|] is small.

Actually, let me think about this differently. I'll prove a direct upper bound.

**Direct upper bound on minimum MIS:**

Claim: In any d-regular graph G on n vertices, there exists a maximal independent set of size at most n(1 + ln(d+1))/(d+1).

Proof: We use the following randomized algorithm:
1. Choose a random subset S where each vertex is included independently with probability p = ln(d+1)/(d+1).
2. Let I = {v ∈ S : N(v) ∩ S = ∅} (independent vertices in S).
3. For each vertex v ∉ I ∪ N(I), add v to I (extending to maximal).

Wait, step 3 might add many vertices. Let me think again.

Actually, here's a cleaner approach:

**Theorem**: In any d-regular graph, there exists a maximal independent set of size O(n log d / d).

Proof: 
1. Randomly order the vertices. 
2. Greedily build I: process vertices in order, add v to I if no neighbor of v is already in I.

E[|I|] = Σ_v Pr[v ∈ I] = Σ_v Pr[v is not killed before it's processed].

v is killed before it's processed iff some neighbor u of v with u before v in the order is added to I. u is added to I iff u is not killed before u is processed, which requires no neighbor of u before u is in I, etc.

This is complex. Let me use a simpler bound.

**Simpler bound using sequential selection:**

Algorithm: 
1. While there are alive vertices:
   a. Pick a random alive vertex v.
   b. Add v to I.
   c. Kill v and all alive neighbors of v.

Let T be the number of steps (= |I|). At each step, we kill at least 1 vertex (v itself) and at most d+1 vertices.

The key question is: how many vertices do we kill per step on average?

Initially, all vertices are alive and have degree d. When we pick a random alive vertex v, it has d alive neighbors (initially). So we kill d+1 vertices.

After some steps, the alive subgraph is no longer d-regular. Some alive vertices have fewer alive neighbors. But in the worst case (for our upper bound), we want to show that we kill many vertices per step on average.

Actually, for an upper bound on |I|, we want to show that we kill MANY vertices per step (so few steps are needed). The worst case for us is when we kill FEW vertices per step.

Hmm, but we're choosing v randomly, so we can't control this. Let me think about the expected number of vertices killed per step.

At step t, let A_t be the number of alive vertices. The average alive degree is d̄_t = (sum of alive degrees) / A_t. When we pick a random alive vertex v, E[alive degree of v] = d̄_t. So E[vertices killed] = 1 + d̄_t.

Now, d̄_t ≤ d (since max degree is d). So E[vertices killed per step] ≤ d + 1, giving |I| ≥ n/(d+1). That's a lower bound.

For an upper bound, we need E[vertices killed per step] to be large. But d̄_t could be small if many edges have been removed.

Hmm, this approach gives a lower bound, not an upper bound. Let me think differently.

**Better approach: Use the fact that the graph has high girth to show that the greedy MIS is small.**

For a d-regular graph with girth ≥ 5, the key property is that the neighborhoods of vertices are "spread out" — no two vertices share more than one common neighbor, and neighborhoods are independent sets.

In the random greedy process, the probability that a vertex v is selected is approximately the probability that v has the smallest label among its "closed neighborhood" {v} ∪ N(v), adjusted for the fact that some neighbors might already be dead.

For the d-regular tree, this probability is known to be ~ (log d)/d. The key reason is:

On the d-regular tree, the greedy process can be analyzed using a branching process argument. The probability that the root survives (is not killed by a neighbor) and is selected is related to the survival probability of a branching process.

Let me try to prove the bound directly for girth ≥ 5 graphs.

**Lemma**: For a d-regular graph G on n vertices with girth ≥ 5, the random greedy MIS has expected size at most Cn log d / d for some constant C.

Proof sketch: 

For a vertex v, let's compute Pr[v ∈ I]. v is selected iff when v is processed (according to the random order), no neighbor of v has already been selected.

Let π(v) be v's position in the random order (uniformly random in [0,1] say). v is selected iff:
1. For every neighbor u of v with π(u) < π(v), u was NOT selected.
2. (Then v is alive when processed and gets selected.)

u (a neighbor of v) is not selected iff either u is killed before it's processed (some neighbor w of u with π(w) < π(u) is selected), or u has π(u) > π(v) (so u is processed after v and doesn't affect v).

This is a complex recursive condition. But with girth ≥ 5, the neighborhoods of different neighbors of v are disjoint (except for v itself). Specifically, for two neighbors u₁, u₂ of v, N(u₁) ∩ N(u₂) = {v} (since if they shared another common neighbor, there would be a 4-cycle).

This means that the events "u₁ is selected" and "u₂ is selected" are "approximately independent" (they share only v as a common neighbor, and the dependence is through v's processing order).

This tree-like structure allows us to analyze the process using a recursion on the tree.

For the d-regular tree, let p be the probability that the root is selected. By the tree structure:

p = Pr[root has the minimum label among {root} ∪ N(root)] + Pr[some neighbor has smaller label but that neighbor is not selected]

Actually, the standard analysis gives:

Let p be the probability that the root is selected. The root is selected iff it's alive when processed, i.e., no neighbor with a smaller label is selected. Each neighbor u is selected iff u is alive when processed, i.e., no neighbor of u (other than the root, which has a larger label) with a smaller label is selected. The neighbors of u (other than root) form an independent set of size d-1, and their neighborhoods are disjoint (tree structure).

By the recursion on the tree, if q is the probability that a vertex at level 1 (neighbor of root) is NOT selected, then:

q = Pr[u is killed before processing] + Pr[u is alive when processed but has a larger label than root]... 

This is getting complicated. Let me just use the known result.

**Known result**: For the random greedy MIS on the d-regular tree (and hence on d-regular graphs with sufficiently high girth), the probability that a vertex is selected is:

p_d = (1+o(1)) (log d)/d as d → ∞.

This is proven in several papers, including:
- Wormald (1999): analysis of random regular graphs
- Gamarnik and Goldberg (2010): for random regular graphs

For d-regular graphs with girth ≥ 5 and d → ∞, the expected size of the random greedy MIS is (1+o(1)) n p_d = (1+o(1)) n (log d)/d.

Actually, I realize I should be more careful. The girth ≥ 5 condition means the graph is locally tree-like up to radius 2. For the random greedy MIS, the probability that v is selected depends on the process in a neighborhood of radius O(log d / log(d-1)) ≈ O(1) around v (since the process "propagates" outward). With girth ≥ 5, we have tree-like structure up to radius 2, which might be enough for the leading term.

But actually, for d → ∞, the relevant radius is O(1) (since the tree branching factor is d-1, and the process dies out quickly). So girth ≥ 5 should be sufficient.

Let me try to prove this more carefully.

**Analysis for girth ≥ 5, d → ∞:**

Consider vertex v with d neighbors u_1, ..., u_d. By girth ≥ 5:
- N(u_i) ∩ N(u_j) = {v} for i ≠ j (no 4-cycles).
- The u_i's are independent (no triangles).

v is selected iff no u_i with π(u_i) < π(v) is selected.

For a neighbor u_i with π(u_i) < π(v): u_i is selected iff no neighbor w of u_i with π(w) < π(u_i) is selected. The neighbors of u_i are v (with π(v) > π(u_i), so v doesn't affect u_i's selection) and d-1 other vertices w_{i,1}, ..., w_{i,d-1}.

By girth ≥ 5, the w_{i,j}'s for different i are all distinct (since if w_{i,j} = w_{i',j'} for i ≠ i', then u_i - w - u_{i'} - v - u_i would be a 4-cycle... wait, that's u_i, w, u_{i'}, v. Is that a 4-cycle? u_i - w_{i,j} - u_{i'} - v - u_i. Yes! That's a 4-cycle. So by girth ≥ 5, w_{i,j} ≠ w_{i',j'} for i ≠ i'.)

Also, within the same i, the w_{i,j}'s are all distinct (they're neighbors of u_i). And by girth ≥ 5, no two w_{i,j}'s share a common neighbor other than u_i (no 4-cycles).

So the structure is: v has d neighbors, each neighbor u_i has d-1 "other" neighbors, and all these d(d-1) vertices at distance 2 from v are distinct, and their neighborhoods (beyond u_i) are disjoint.

This means the events "u_i is selected" for different i are independent (they depend on disjoint sets of vertices at distance ≥ 2 from v, and the only shared vertex is v which has π(v) > π(u_i) and thus doesn't affect u_i's selection).

Wait, that's not quite right. The events "u_i is selected" depend on the random labels of u_i and its neighbors w_{i,1}, ..., w_{i,d-1} and their neighbors. Since the w_{i,j}'s and their neighborhoods are disjoint for different i, the events are indeed independent (conditional on π(u_i) < π(v)).

So: Pr[v is selected | π(v) = t] = Π_{i=1}^{d} Pr[u_i is not selected | π(u_i) < t, π(v) = t]... 

Hmm, let me be more careful. Let's condition on π(v) = t.

v is selected iff for all i, u_i is not selected (given π(v) = t). Since the u_i's are independent (as argued above), and the event "u_i is selected" depends only on π(u_i) and the labels in u_i's subtree (excluding v):

Pr[v selected | π(v) = t] = Π_{i=1}^{d} Pr[u_i not selected | π(v) = t]

Since the events are independent and don't depend on π(v) (only on π(u_i) relative to t):

Pr[u_i not selected | π(v) = t] = Pr[u_i not selected | π(u_i) is uniform on [0,1]]

Wait, but we need π(u_i) < t for u_i to affect v. If π(u_i) > t, then u_i is processed after v, so u_i doesn't affect v's selection. If π(u_i) < t, then u_i could be selected (killing v) or not.

So: Pr[v selected | π(v) = t] = Π_{i=1}^{d} [Pr[π(u_i) > t] + Pr[π(u_i) < t and u_i not selected]]

= Π_{i=1}^{d} [(1-t) + t · Pr[u_i not selected | π(u_i) < t]]

Let f(t) = Pr[u_i not selected | π(u_i) < t]. By symmetry, this is the same for all i.

Actually, let me define things more carefully. Let's work on the d-regular tree. Let p(t) = Pr[vertex v is selected | π(v) = t]. By the tree structure and independence:

p(t) = [1 - t + t · q(t)]^d

where q(t) = Pr[a neighbor u is not selected | π(u) < t, and u is a neighbor of v with π(v) = t].

But q(t) depends on the subtree rooted at u (excluding v). Since the subtree is a (d-1)-ary tree (u has d-1 children besides v), and by the tree structure:

q(t) = Pr[u not selected | π(u) < t] = 1 - Pr[u selected | π(u) < t]

Let r(t) = Pr[u selected | π(u) = s] for s < t. Then:

Pr[u selected | π(u) < t] = (1/t) ∫_0^t Pr[u selected | π(u) = s] ds = (1/t) ∫_0^t p_{d-1}(s) ds

where p_{d-1}(s) is the selection probability for a vertex with d-1 children (since u's subtree, excluding v, has d-1 branches).

Hmm, this is getting into the full tree analysis. Let me just use the asymptotic result.

For the d-regular tree with d → ∞, the selection probability is p_d ~ (log d)/d. This is a well-established result.

For a d-regular graph with girth ≥ 5, the selection probability for each vertex is approximately p_d (up to lower-order terms), because the local structure up to distance 2 is tree-like, and for large d, the process is determined by the local structure (the branching process dies out in O(1) levels for large d).

Therefore, E[|I|] ≈ n · p_d ≈ n · (log d)/d.

For d = n^ε: E[|I|] ≈ n · (ε log n) / n^ε = ε n^{1-ε} log n = o(n).

Since the expected size of the random greedy MIS is o(n), there exists a maximal independent set of size o(n). Therefore, NOT every maximal independent set has size Ω(n).

This means the answer to the question is **NO**.

Wait, but let me reconsider. The question asks "Does there exist a family of regular dense graphs with girth at least 5, where every maximal independent set has a size of at least Ω(n)?"

If the answer is NO, I need to prove that for ANY such family, there exists a maximal independent set of size o(n).

Let me make sure my argument is rigorous.

**Rigorous argument:**

We need to show: For any d-regular graph G on n vertices with girth ≥ 5 and d ≥ n^ε (equivalently m = nd/2 ≥ n^{1+ε}/2), there exists a maximal independent set of size O(n log d / d) = O(n^{1-ε} log n) = o(n).

I'll use the random greedy algorithm and show that its expected output size is O(n log d / d).

**Key claim**: For a d-regular graph G with girth ≥ 5 and d → ∞, the random greedy MIS has expected size (1 + o(1)) n (log d)/d.

To prove this, I need to show that for each vertex v, Pr[v is selected] = (1 + o(1)) (log d)/d.

Let me prove this using the tree-like local structure.

**Setup**: Assign each vertex a uniform random label in [0,1]. Process vertices in increasing order of label. v is selected iff no neighbor of v with a smaller label is selected.

**Analysis of Pr[v selected]:**

Let's condition on v's label being t. v is selected iff none of its d neighbors with labels less than t are selected.

For neighbor u_i (with label s_i < t): u_i is selected iff none of u_i's neighbors with labels less than s_i are selected. u_i's neighbors are v (label t > s_i, so v doesn't affect u_i) and d-1 other vertices w_{i,1}, ..., w_{i,d-1}.

By girth ≥ 5:
- All w_{i,j} are distinct (no 4-cycles through v).
- For different i, the sets {w_{i,1}, ..., w_{i,d-1}} are disjoint.
- The events "u_i is selected" depend on disjoint sets of vertices (the w_{i,j}'s and their neighborhoods), so they are independent.

Therefore:
Pr[v selected | label(v) = t] = Π_{i=1}^{d} Pr[u_i not selected | label(u_i) < t]

Wait, I need to be careful. Pr[u_i not selected | label(u_i) < t] — but u_i's label is random. Let me rephrase.

Pr[v selected | label(v) = t] = Π_{i=1}^{d} Pr[u_i does not kill v | label(v) = t]

u_i kills v iff u_i is selected AND label(u_i) < t. So:

Pr[u_i does not kill v | label(v) = t] = Pr[label(u_i) ≥ t] + Pr[label(u_i) < t AND u_i not selected]
= (1-t) + Pr[label(u_i) < t AND u_i not selected]
= (1-t) + t · Pr[u_i not selected | label(u_i) < t, label(v) = t]

Now, Pr[u_i not selected | label(u_i) < t, label(v) = t] — this depends on u_i's subtree (excluding v). Since the subtree is tree-like (girth ≥ 5), and u_i has d-1 children (the w_{i,j}'s):

Let g(t) = Pr[u not selected | label(u) < t] for a vertex u in the tree with d-1 children (and one parent which is already accounted for).

Then:
Pr[v selected | label(v) = t] = [(1-t) + t · g(t)]^d

And g(t) = Pr[u not selected | label(u) < t] = 1 - Pr[u selected | label(u) < t]

Pr[u selected | label(u) < t] = (1/t) ∫_0^t Pr[u selected | label(u) = s] ds

Pr[u selected | label(u) = s] = [(1-s) + s · g(s)]^{d-1}

(Since u has d-1 children, and the same logic applies.)

So we have the system:
- p(t) = [(1-t) + t·g(t)]^d (probability v is selected given label t, v has d children)
- h(s) = [(1-s) + s·g(s)]^{d-1} (probability u is selected given label s, u has d-1 children)
- g(t) = 1 - (1/t)∫_0^t h(s) ds

And E[|I|] = n ∫_0^1 p(t) dt.

This is a complex system, but for large d, we can analyze it asymptotically.

Let me define φ(t) = (1-t) + t·g(t) = 1 - t(1 - g(t)) = 1 - t·(1-g(t)).

Note that 1 - g(t) = Pr[u selected | label(u) < t] = (1/t)∫_0^t h(s) ds.

So φ(t) = 1 - ∫_0^t h(s) ds.

And h(s) = φ(s)^{d-1}, p(t) = φ(t)^d.

So φ(t) = 1 - ∫_0^t φ(s)^{d-1} ds.

This gives us: φ'(t) = -φ(t)^{d-1}, with φ(0) = 1.

This is a separable ODE! 

dφ/dt = -φ^{d-1}
φ^{-(d-1)} dφ = -dt
∫ φ^{-(d-1)} dφ = -t + C
φ^{-(d-2)} / (d-2) = t + C' (for d > 2)

At t=0, φ=1: 1/(d-2) = C', so C' = 1/(d-2).

φ^{-(d-2)} / (d-2) = t + 1/(d-2)
φ^{-(d-2)} = (d-2)t + 1
φ(t) = [(1 + (d-2)t)]^{-1/(d-2)}

For large d, 1/(d-2) ≈ 1/d, and (d-2) ≈ d:

φ(t) ≈ (1 + dt)^{-1/d}

Now, p(t) = φ(t)^d ≈ (1 + dt)^{-1} = 1/(1 + dt).

E[|I|]/n = ∫_0^1 p(t) dt ≈ ∫_0^1 1/(1+dt) dt = (1/d) ln(1+d) ≈ (ln d)/d.

So E[|I|] ≈ n (ln d)/d.

This is exactly the result we need! And the analysis only used the tree-like structure up to distance 2 (girth ≥ 5), which ensures that the neighborhoods of different neighbors of v are disjoint.

Wait, but I made an approximation. Let me be more careful.

The ODE φ'(t) = -φ(t)^{d-1} with φ(0) = 1 gives:

φ(t) = [1 + (d-2)t]^{-1/(d-2)} (for d > 2).

p(t) = φ(t)^d = [1 + (d-2)t]^{-d/(d-2)}.

E[|I|]/n = ∫_0^1 [1 + (d-2)t]^{-d/(d-2)} dt.

Let u = 1 + (d-2)t, du = (d-2)dt:

= (1/(d-2)) ∫_1^{d-1} u^{-d/(d-2)} du

= (1/(d-2)) · [u^{-d/(d-2)+1} / (-d/(d-2)+1)]_1^{d-1}

= (1/(d-2)) · [u^{-2/(d-2)} / (-2/(d-2))]_1^{d-1}

= (1/(d-2)) · (-(d-2)/2) · [u^{-2/(d-2)}]_1^{d-1}

= -1/2 · [(d-1)^{-2/(d-2)} - 1]

= 1/2 · [1 - (d-1)^{-2/(d-2)}]

For large d: (d-1)^{-2/(d-2)} = e^{-2 ln(d-1)/(d-2)} ≈ 1 - 2ln(d-1)/(d-2) + ...

So E[|I|]/n ≈ 1/2 · 2ln(d-1)/(d-2) ≈ ln(d)/d.

More precisely:

E[|I|]/n = (1/2)(1 - (d-1)^{-2/(d-2)})

For any d ≥ 3, this is a fixed value. For d → ∞:

(d-1)^{-2/(d-2)} = exp(-2 ln(d-1)/(d-2)) → exp(0) = 1, but the rate is 2ln(d)/d.

So E[|I|]/n = (1/2)(1 - exp(-2ln(d)/d + o(1))) ≈ (1/2)(2ln(d)/d) = ln(d)/d.

Therefore E[|I|] = (1 + o(1)) n ln(d)/d.

But wait, I need to verify that the tree approximation is valid for girth ≥ 5. The key step was claiming that the events "u_i is selected" are independent for different neighbors u_i of v. This requires that the neighborhoods of u_i (excluding v) are disjoint, which is guaranteed by girth ≥ 5 (no 4-cycles).

But there's a subtlety: the events "u_i is selected" depend on the entire subtree rooted at u_i, not just the immediate neighbors. For the independence to hold, we need the subtrees to be disjoint, which requires that there are no cycles involving v's distance-2 neighborhood. With girth ≥ 5, cycles have length ≥ 5, so the distance-2 neighborhoods are tree-like. But the subtrees extend beyond distance 2, where cycles could exist.

Hmm, so the independence might not be exact. Let me think about this more carefully.

Actually, the issue is that the random greedy process on vertex v depends on the labels of all vertices, not just the local neighborhood. However, the dependence decays with distance. For large d, the process "dies out" quickly (the branching process has a high death rate), so the dependence on far-away vertices is negligible.

But for a rigorous proof, I need to be more careful. Let me think about whether the tree approximation gives an upper bound or just an approximation.

Actually, for the purpose of this problem, I think the tree approximation gives an upper bound on Pr[v is selected], because cycles can only help v survive (by creating dependencies that prevent neighbors from being selected). Wait, that's not obviously true either.

Let me think about this differently. Instead of trying to get the exact tree approximation, let me prove a direct upper bound.

**Direct upper bound:**

I'll show that for any d-regular graph with girth ≥ 5, the random greedy MIS has expected size at most Cn log d / d.

**Key inequality**: For a vertex v with label t, Pr[v selected | label(v) = t] ≤ [1 - t + t·g(t)]^d where g(t) is defined by the tree recursion.

Wait, actually, cycles could make Pr[v selected] either larger or smaller than the tree value. Let me think about which direction.

In the tree, the events "u_i is selected" are independent. In a graph with cycles, these events could be positively or negatively correlated. If they're positively correlated (if one u_i being selected makes it more likely that another u_j is selected), then Pr[none selected] is smaller, so Pr[v selected] is larger. If negatively correlated, Pr[v selected] is smaller.

Hmm, it's not clear which direction the correlation goes. So the tree approximation might not give a bound in either direction.

Let me try a completely different approach.

**Approach via explicit construction of small MIS:**

I'll show that in any d-regular graph with girth ≥ 5, there exists a maximal independent set of size O(n log d / d).

**Algorithm:**
1. Initialize I = ∅, S = V (alive vertices).
2. While S ≠ ∅:
   a. Pick any vertex v ∈ S.
   b. Add v to I.
   c. Remove v and N(v) from S.

This gives a maximal independent set. The size depends on the order of picking.

If we pick v to be a vertex of maximum alive degree, we kill more vertices per step, getting a smaller I. But in a d-regular graph, all vertices initially have degree d.

Actually, let me use a different strategy. 

**Strategy: Pick vertices that kill the most alive vertices.**

Initially, all vertices have alive degree d. Pick any vertex v, add to I, kill v and its d neighbors. Now d+1 vertices are dead.

The remaining graph has n - d - 1 vertices. Some of them lost neighbors. A vertex at distance 2 from v lost 1 neighbor (since girth ≥ 5, no vertex at distance 2 is adjacent to 2 neighbors of v). There are d(d-1) such vertices (each neighbor of v has d-1 other neighbors, all distinct by girth ≥ 5). Each of these now has alive degree d-1.

Other vertices (at distance ≥ 3 from v) still have alive degree d.

Now, pick a vertex w of maximum alive degree. If there's a vertex with alive degree d (at distance ≥ 3 from v), pick it. Kill w and its alive neighbors (at least 1 + d - (number of already-dead neighbors of w)). If w is at distance ≥ 3 from v, all its neighbors are alive, so we kill d+1 vertices.

We can keep picking vertices at distance ≥ 3 from all previously picked vertices, killing d+1 vertices each time, until no such vertices remain.

The number of vertices killed per step is d+1 (as long as we can find a vertex whose entire neighborhood is alive). The number of such steps is at least n / (d+1)² · something... hmm, this isn't quite right.

Let me think about this more carefully using a packing argument.

**Packing argument**: 

We want to find a set of vertices {v_1, v_2, ...} such that the closed neighborhoods N[v_i] = {v_i} ∪ N(v_i) are disjoint. Each N[v_i] has d+1 vertices. If we can find k such disjoint neighborhoods, then we can select v_1, ..., v_k as our independent set, and they kill at least k(d+1) vertices. But we also need the set to be MAXIMAL.

Actually, the greedy algorithm doesn't require disjoint neighborhoods. Let me reconsider.

**Better approach: Sequential greedy with random ordering, direct analysis.**

Let me go back to the random greedy approach but prove the bound more carefully.

I'll prove: E[|I|] ≤ n · (1 + ln d) / (d - 1) for d-regular graphs with girth ≥ 5.

**Proof:**

We use the random greedy algorithm (random permutation of vertices). For each vertex v, let A_v = {v} ∪ N(v) be the closed neighborhood. v is selected iff v has the smallest label in A_v among all vertices in A_v that are "alive" when the first vertex in A_v is processed.

Actually, here's a cleaner way to think about it. v is selected iff v has the smallest label in A_v. Wait, is that true?

No, that's not true in general. v is selected iff no neighbor of v with a smaller label is selected. A neighbor u with a smaller label is selected iff no neighbor of u with a smaller label than u's label is selected, etc.

But here's a key observation: v is NOT selected iff some neighbor u of v with a smaller label is selected. And u is selected iff u has the smallest label in A_u among alive vertices when u is processed.

Hmm, this is still complex. Let me use a different approach.

**Approach via the ODE (which I solved above):**

I showed that on the d-regular tree, the selection probability gives E[|I|]/n = (1/2)(1 - (d-1)^{-2/(d-2)}).

For the graph with girth ≥ 5, I need to show that the tree approximation is valid, or at least that it gives an upper bound.

**Claim**: For a d-regular graph G with girth ≥ 5, the random greedy MIS has expected size at most (1 + o(1)) n ln(d)/d.

The key insight is that with girth ≥ 5, the analysis on the tree is exact up to the second level, and the error from higher levels is negligible for large d.

Let me make this precise. The ODE analysis I did above used the fact that the events "u_i is selected" are independent for different neighbors u_i of v. This independence holds exactly on the tree and approximately on the graph (with girth ≥ 5).

On the graph, the events "u_i is selected" might not be exactly independent because of cycles of length ≥ 5. However, the dependence is through vertices at distance ≥ 3 from v, and for large d, the contribution of these far-away vertices is negligible.

More precisely, the probability that the random greedy process "reaches" distance k from v is roughly (d-1)^{-k} (since the branching process dies out). For k = 3 (where cycles might start to matter), this is (d-1)^{-3} = O(d^{-3}), which is negligible.

So the tree approximation is valid up to an error of O(d^{-3}) per vertex, giving:

Pr[v selected] = (1 + O(d^{-3})) · (tree value)

And E[|I|] = (1 + O(d^{-3})) · n · (tree value) = (1 + o(1)) n ln(d)/d.

Hmm, but I'm not being fully rigorous about the error term. Let me try to be more careful.

Actually, let me take a step back. The ODE I derived was:

φ'(t) = -φ(t)^{d-1}, φ(0) = 1

This came from the tree recursion where the events at different branches are independent. On the graph, the events might not be independent, but by the FKG inequality or similar, we might be able to bound the effect.

Actually, I think there's a cleaner way to get an upper bound without worrying about the tree approximation.

**Clean upper bound via sequential algorithm:**

Here's a simple algorithm that gives a small MIS:

1. Process vertices in a random order.
2. Greedily build I.

I'll show E[|I|] = O(n log d / d) directly.

**Key lemma**: For a d-regular graph with girth ≥ 5, Pr[v is selected] ≤ C log d / d for some constant C.

**Proof of lemma**: 

v is selected iff no neighbor of v with a smaller label is selected. 

Let's condition on v's label being t. Let u_1, ..., u_d be v's neighbors. For each u_i, let B_i be the event that u_i is selected and has label < t.

v is selected iff none of B_1, ..., B_d occurs.

Now, Pr[B_i] = Pr[u_i selected | label(u_i) < t] · t = t · Pr[u_i selected | label(u_i) < t].

By the tree-like structure (girth ≥ 5), the B_i's are "approximately independent." But even without independence, we can use the union bound:

Pr[v not selected | label(v) = t] ≤ Σ Pr[B_i] = d · t · Pr[u selected | label(u) < t]

This gives a lower bound on Pr[v not selected], hence an upper bound on Pr[v selected]:

Pr[v selected | label(v) = t] ≥ 1 - d · t · Pr[u selected | label(u) < t]

That's a lower bound, not an upper bound. The union bound goes the wrong way.

For an upper bound on Pr[v selected], I need a lower bound on Pr[v not selected]. Without independence, I can't easily get this.

Hmm, let me try a different approach entirely.

**Approach via dominating set:**

A maximal independent set is an independent dominating set. I'll show that there exists a small independent dominating set.

Step 1: Find a small dominating set D of size O(n log d / d). This is standard: each vertex dominates d+1 vertices, so a random set of size (n ln(d+1))/(d+1) dominates w.h.p. (by the probabilistic method with coupon collector argument).

Step 2: From D, extract an independent set I ⊆ D. Since G[D] has at most |D|²/2 edges and each vertex in D has degree at most d, we can find an independent subset of D of size at least |D|/(d+1) (by Turán). But this gives |I| ≥ n log d / (d(d+1)), which is even smaller.

Step 3: Extend I to a maximal independent set I'. Since I is already a dominating set (as a subset of D), I' ⊇ I and I' is independent and dominating. But I' could be larger than I.

Wait, actually, if I ⊆ D and D is a dominating set, then I might not be dominating. Let me reconsider.

Actually, the approach should be:

Step 1: Find a dominating set D of size O(n log d / d).
Step 2: Find an independent set I inside D (of size at least |D|/(Δ(D)+1) where Δ(G[D]) is the max degree in G[D]).
Step 3: Extend I to a maximal independent set I'. The vertices added in step 3 are those not dominated by I. Since D is dominating, every vertex is either in D or adjacent to D. The vertices not dominated by I are those in D \ I that are not adjacent to I, plus those not in D that are only adjacent to D \ I.

This is getting complicated. Let me try yet another approach.

**Direct construction of small MIS:**

Algorithm:
1. Initialize I = ∅.
2. While there are undominated vertices:
   a. Pick a random undominated vertex v.
   b. If v is not adjacent to any vertex in I, add v to I.
   c. Otherwise, v is dominated, remove it from the undominated set.
3. Return I.

Hmm, this doesn't quite work because in step 2a, we might pick a vertex that's adjacent to I, and then we just remove it without adding to I.

Let me think about this more carefully.

**Simple algorithm that works:**

1. Initialize I = ∅, S = V.
2. While S ≠ ∅:
   a. Pick v ∈ S uniformly at random.
   b. Add v to I.
   c. Remove {v} ∪ (N(v) ∩ S) from S.
3. Return I.

This is the random greedy MIS. I need to bound E[|I|].

At each step, we remove 1 + |N(v) ∩ S| vertices. The key is to lower-bound |N(v) ∩ S|.

Initially, |N(v) ∩ S| = d for all v. After some steps, some neighbors of v might be removed.

**Claim**: At any point, for a random alive vertex v, E[|N(v) ∩ S|] ≥ (1-o(1))d as long as |S| ≥ n/2 (say).

This would mean that each step removes (1+o(1))(d+1) vertices on average, giving |I| ≈ n/(d+1) ≈ n/d. But this is n^{1-ε}, not n log d / d.

Hmm, so the simple analysis gives n/d, which is already o(n). But the actual bound is n log d / d, which is slightly larger (by a log factor). The log factor comes from the fact that as the algorithm progresses, the alive degree decreases, and later steps remove fewer vertices.

But for our purposes, n/d = n^{1-ε} is already o(n), so even this weaker bound suffices!

Wait, let me double-check. We need to show that there exists a MIS of size o(n). If E[|I|] = O(n/d) = O(n^{1-ε}), then there exists a MIS of size O(n^{1-ε}) = o(n). That's sufficient!

But is the claim E[|N(v) ∩ S|] ≥ (1-o(1))d correct? Let me think about this.

After k steps, we've removed at most k(d+1) vertices. The remaining |S| ≥ n - k(d+1) vertices. For a random alive vertex v, how many of its d neighbors are alive?

Each neighbor of v is alive with probability approximately |S|/n (if the removals are "spread out"). But the removals are not uniform — we remove neighborhoods, which creates correlations.

However, by girth ≥ 5, the neighborhoods of different selected vertices don't overlap too much (any two selected vertices share at most 1 common neighbor). So the removals are "spread out" and the approximation |N(v) ∩ S| ≈ d · |S|/n is reasonable.

More precisely, after k steps, the number of removed vertices is at most k(d+1) and at least k. The number of removed edges is at most kd. For a random alive vertex v, the expected number of alive neighbors is:

E[|N(v) ∩ S|] = d - E[|N(v) ∩ (V \ S)|]

A neighbor u of v is removed if u was selected (added to I) or u was killed (adjacent to a selected vertex). The probability that u is removed after k steps is at most k(d+1)/n (by union bound over the k selected vertices and their neighborhoods).

So E[|N(v) ∩ S|] ≥ d - d · k(d+1)/n = d(1 - k(d+1)/n).

When k ≤ n/(2(d+1)), this gives E[|N(v) ∩ S|] ≥ d/2.

So for the first n/(2(d+1)) steps, each step removes at least 1 + d/2 vertices on average. After these steps, at most n - n/(2(d+1)) · (1 + d/2) ≈ n - n/2 = n/2 vertices remain.

Wait, let me be more careful. In the first k ≤ n/(2(d+1)) steps, each step removes at least 1 + d/2 vertices on average. So after k steps, at most n - k(1+d/2) vertices remain. We need k(1+d/2) ≥ n/2, i.e., k ≥ n/(d+2). So after n/(d+2) steps, about n/2 vertices remain.

For the remaining n/2 vertices, we can't guarantee that the alive degree is still d/2. But we can repeat the argument: for the next phase, the alive degree is at least d · (1/2) = d/2 (roughly), and we need k' steps with k' ≤ (n/2)/(2(d/2+1)) = n/(2(d+2)), each removing at least 1 + d/4 vertices.

This gives a logarithmic number of phases, each reducing the alive count by a constant factor, with the number of steps per phase being O(n/d). The total number of steps is O(n log d / d)... 

Hmm wait, let me think about this more carefully. Actually, the number of phases is O(log n) or O(log d)?

Let me think about it as follows. Define the "potential" as the number of alive vertices. In each step, we remove 1 + (alive degree of selected vertex) vertices. The alive degree decreases over time.

Phase 1: Alive degree ≥ d/2. Each step removes ≥ 1 + d/2 vertices. Number of steps: ≤ n/(d/2 + 1) ≈ 2n/d. After this phase, the number of alive vertices is at most n - 2n/d · (d/2) = n - n = 0? No, that's not right because the bound on alive degree is an expectation, not a worst case.

Let me use a more careful analysis.

Actually, I think the simple bound E[|I|] = O(n/d) is not quite right. The issue is that as the algorithm progresses, the alive degree decreases, and later steps remove fewer vertices. The total number of steps is more like n log d / d.

But for our purposes, even O(n/d) would suffice (it's o(n) when d → ∞). Let me see if I can prove O(n/d) or even O(n log d / d).

**Simpler approach: just use the first moment.**

E[|I|] = Σ_v Pr[v is selected].

I need an upper bound on Pr[v is selected]. 

v is selected iff v is alive when processed. v is alive when processed iff no neighbor of v with a smaller label was selected.

A neighbor u of v is selected only if u is alive when u is processed, which requires no neighbor of u with a smaller label was selected.

The key observation: v is selected only if v has the smallest label among {v} ∪ (N(v) ∩ alive(v)), where alive(v) is the set of vertices alive when v is processed. But this is circular.

Let me try a different approach. 

**Approach: Pr[v selected] ≤ 1/(1 + number of alive neighbors of v when v is processed).**

When v is processed, it's selected iff it's alive (no neighbor was selected before). If v is alive, it's selected (the algorithm always selects alive vertices). So Pr[v selected] = Pr[v is alive when processed].

v is alive when processed iff no neighbor of v with a smaller label was selected. 

Now, here's an upper bound: Pr[v is alive when processed] ≤ Pr[v has the smallest label in {v} ∪ N(v)] = 1/(d+1).

This is because if v has the smallest label in {v} ∪ N(v), then v is definitely alive when processed (no neighbor has a smaller label). But v could also be alive even if some neighbors have smaller labels (if those neighbors were not selected because they were killed). So Pr[v alive] ≥ 1/(d+1), and the upper bound Pr[v alive] ≤ 1/(d+1) is NOT true in general.

Hmm, so this simple bound doesn't give an upper bound.

Let me think about this differently. 

**Upper bound on Pr[v selected]:**

Pr[v selected] = Pr[v is alive when processed].

v is NOT alive when processed iff some neighbor u of v with label(u) < label(v) is selected.

Pr[v not selected] = Pr[∃ u ∈ N(v) : label(u) < label(v) and u is selected]

By the tree-like structure (girth ≥ 5), the events "u_i is selected and label(u_i) < label(v)" for different neighbors u_i are approximately independent. So:

Pr[v not selected] ≈ 1 - (1 - p)^d

where p = Pr[u is selected and label(u) < label(v)] for a random neighbor u.

p = ∫_0^1 Pr[u selected | label(u) = s] · Pr[label(v) > s] ds = ∫_0^1 Pr[u selected | label(u) = s] · (1-s) ds

This is getting back to the tree analysis. Let me just go with the ODE result.

**Conclusion:**

I proved (via the ODE analysis on the tree-like local structure) that for a d-regular graph with girth ≥ 5 and d → ∞:

E[|I|] = (1/2)(1 - (d-1)^{-2/(d-2)}) · n ≈ (ln d / d) · n

This is o(n) when d → ∞ (specifically d = n^ε).

Since E[|I|] = o(n), there exists a maximal independent set of size o(n), and hence NOT every maximal independent set has size Ω(n).

But wait, I need to address the issue that the tree approximation might not be exact for graphs with girth exactly 5. Let me think about whether the ODE gives an upper bound or just an approximation.

Actually, I realize there's a cleaner way to get an upper bound that doesn't rely on the tree approximation being exact.

**Clean upper bound:**

I'll show that for any d-regular graph (no girth assumption), there exists a maximal independent set of size O(n log d / d).

**Theorem**: For any d-regular graph G on n vertices with d ≥ 2, there exists a maximal independent set of size at most n(1 + ln d)/d.

**Proof**: 

We use the following algorithm:
1. Pick a random subset S where each vertex is included independently with probability p = ln(d+1)/(d+1).
2. Let I = {v ∈ S : N(v) ∩ S = ∅} (independent vertices in S, i.e., vertices in S with no neighbor in S).
3. For each vertex v ∉ I ∪ N(I), add v to I (greedily, one by one, ensuring I remains independent).

After step 2, I is an independent set (since no two vertices in I are adjacent — each has no neighbor in S, and I ⊆ S).

After step 3, I is a maximal independent set (every vertex not in I is either in N(I) or was added to I).

**Size of I after step 2:**

E[|I|] = Σ_v Pr[v ∈ S and N(v) ∩ S = ∅] = Σ_v p(1-p)^{d_v} = n · p(1-p)^d.

For p = ln(d+1)/(d+1) and large d: p ≈ ln d / d, (1-p)^d ≈ e^{-pd} = e^{-ln d} = 1/d.

So E[|I|] ≈ n · (ln d / d) · (1/d) = n ln d / d². This is very small.

**Size of the extension in step 3:**

A vertex v is not in I ∪ N(I) after step 2 iff v ∉ S and v has no neighbor in S that is independent (i.e., no neighbor u with u ∈ S and N(u) ∩ S = ∅).

Actually, v ∉ I ∪ N(I) means:
- v ∉ I: either v ∉ S, or v ∈ S but has a neighbor in S.
- v ∉ N(I): no neighbor of v is in I, i.e., no neighbor u of v satisfies u ∈ S and N(u) ∩ S = ∅.

This is complex. Let me simplify.

A vertex v is "undominated" after step 2 if v ∉ I and v ∉ N(I). This means:
- v ∉ I: v ∈ S with a neighbor in S, or v ∉ S.
- v ∉ N(I): no neighbor of v is in I.

If v ∉ S and no neighbor of v is in I: v is undominated.

Pr[v ∉ S and no neighbor of v is in I] = (1-p) · Pr[no neighbor of v is in I | v ∉ S]

A neighbor u of v is in I iff u ∈ S and N(u) ∩ S = ∅. Given v ∉ S, Pr[u ∈ I] = p · (1-p)^{deg(u) - 1} (since u has d neighbors, one of which is v which is not in S, so the other d-1 neighbors must not be in S). Wait, N(u) ∩ S = ∅ requires all neighbors of u to not be in S. u has d neighbors, including v. Given v ∉ S, we need the other d-1 neighbors to not be in S. So Pr[u ∈ I | v ∉ S] = p · (1-p)^{d-1}.

The events "u_i ∈ I" for different neighbors u_i of v are not independent (they share neighbors through v's distance-2 neighborhood). But we can use a union bound or Markov's inequality.

Pr[no neighbor of v is in I | v ∉ S] ≤ 1 (trivially).

Pr[v is undominated] ≤ Pr[v ∉ S] = 1 - p.

That's too loose. Let me use a better bound.

Pr[v is undominated] = Pr[v ∉ S] · Pr[no neighbor in I | v ∉ S]

By Markov's inequality: Pr[no neighbor in I | v ∉ S] = 1 - Pr[at least one neighbor in I | v ∉ S]

E[number of neighbors in I | v ∉ S] = d · p(1-p)^{d-1}

By Markov: Pr[at least one neighbor in I | v ∉ S] ≤ d · p(1-p)^{d-1}

So Pr[no neighbor in I | v ∉ S] ≥ 1 - d · p(1-p)^{d-1}

Hmm, this gives a lower bound, not an upper bound. I need an upper bound on Pr[no neighbor in I].

Let me use the second moment method or a direct calculation.

Actually, let me use a simpler approach. The number of undominated vertices after step 2 is at most n · (1-p) · (1 - p(1-p)^{d-1})^d... no, this assumes independence which doesn't hold.

Let me try a different approach. 

**Approach via the Lovász Local Lemma or direct probabilistic argument:**

Actually, let me just use a cleaner version of the probabilistic argument.

**Theorem (well-known)**: Every graph G with n vertices and maximum degree Δ has a maximal independent set of size at most n(1 + ln(Δ+1))/(Δ+1).

This is a standard result. Let me recall the proof.

**Proof**: Consider the following random process. Pick a random permutation of vertices. Process vertices in order. For each vertex v, if v is not yet dominated (no neighbor in I and v ∉ I), add v to I.

Wait, that's not quite the standard proof. Let me recall.

Actually, the standard result is about the independent domination number (minimum maximal independent set). 

**Theorem**: For any graph G with n vertices and maximum degree Δ, the independent domination number i(G) ≤ n(1 + ln(Δ+1))/(Δ+1).

**Proof**: (Arnautov, 1974; Payan, 1975; etc.)

The proof uses the probabilistic method. Pick a random subset S where each vertex is included with probability p. Let I = S \ N(S) (vertices in S with no neighbor in S — these form an independent set). Then extend I to a maximal independent set by adding vertices greedily.

E[|I|] = np(1-p)^Δ (using max degree Δ, so (1-p)^{deg(v)} ≥ (1-p)^Δ, but actually for an upper bound on the final MIS, we need to count the extension too).

Hmm, let me look at this more carefully. The standard proof goes:

1. Pick random S with Pr[v ∈ S] = p.
2. Let I_0 = {v ∈ S : N(v) ∩ S = ∅} (independent set).
3. Let U = V \ (I_0 ∪ N(I_0)) (undominated vertices).
4. Extend I_0 to maximal I by adding one vertex from each "undominated" region.

E[|I_0|] = np(1-p)^{d} (for d-regular graph).

E[|U|] = n · Pr[v is undominated] = n · Pr[v ∉ S and N(v) ∩ I_0 = ∅].

Pr[v ∉ S and N(v) ∩ I_0 = ∅] = (1-p) · Pr[∀u ∈ N(v): u ∉ I_0 | v ∉ S]

u ∉ I_0 means u ∉ S or N(u) ∩ S ≠ ∅. Given v ∉ S:

Pr[u ∉ I_0 | v ∉ S] = Pr[u ∉ S] + Pr[u ∈ S and ∃w ∈ N(u)\{v}: w ∈ S | v ∉ S]
= (1-p) + p(1 - (1-p)^{d-1})
= 1 - p(1-p)^{d-1}

If the events for different u ∈ N(v) were independent (which they're not in general, but are approximately independent for high girth):

Pr[∀u ∈ N(v): u ∉ I_0 | v ∉ S] ≈ (1 - p(1-p)^{d-1})^d

So Pr[v undominated] ≈ (1-p)(1 - p(1-p)^{d-1})^d.

The total size of the final MIS is |I_0| + (extension). The extension adds at most |U| vertices (one per undominated vertex, but actually we can be smarter — each added vertex dominates at least one undominated vertex, and possibly more). Actually, the extension adds at most |U| vertices, but each added vertex also dominates some undominated vertices, so the extension is at most |U| but could be less.

For a rough bound: |I| ≤ |I_0| + |U|.

E[|I|] ≤ E[|I_0|] + E[|U|] = np(1-p)^d + n(1-p)(1 - p(1-p)^{d-1})^d.

Now, optimize over p. Set p = ln(d+1)/d (approximately).

p(1-p)^d ≈ (ln d / d) · e^{-ln d} = (ln d / d) · (1/d) = ln d / d².

(1-p)(1 - p(1-p)^{d-1})^d ≈ 1 · (1 - (ln d / d) · (1/d))^d ≈ (1 - ln d / d²)^d ≈ e^{-ln d / d} ≈ 1 - ln d / d.

Hmm, that gives E[|U|] ≈ n, which is way too large. The issue is that with this p, most vertices are undominated.

Let me reconsider. The standard approach uses a different p.

Actually, I think the standard result uses a different algorithm. Let me recall.

**Standard proof of i(G) ≤ n(1 + ln(Δ+1))/(Δ+1):**

The proof is by induction on n. Or by a direct probabilistic argument with a different approach.

Actually, I think the correct approach is:

1. Pick a random subset S with Pr[v ∈ S] = p.
2. For each vertex v ∈ S with a neighbor in S, remove v from S (i.e., I_0 = {v ∈ S : N(v) ∩ S = ∅}).
3. I_0 is independent. Now, every vertex in V \ (I_0 ∪ N(I_0)) is undominated. Add these vertices to I_0 one by one (each addition dominates at least the added vertex).

The key is that in step 3, each added vertex dominates at least itself, so the number of added vertices is at most |U|. But actually, we can be smarter: the added vertices form an independent set in G[U], and each dominates at least itself and possibly others.

For the bound, we use:

E[|I|] ≤ E[|I_0|] + E[|U|]

With the right choice of p, this gives O(n log d / d).

Let me compute more carefully.

E[|I_0|] = np(1-p)^d

For the undominated vertices, we need:

Pr[v ∈ U] = Pr[v ∉ I_0 and v ∉ N(I_0)]

v ∉ I_0: either v ∉ S, or v ∈ S with a neighbor in S.
v ∉ N(I_0): no neighbor of v is in I_0.

Case 1: v ∈ S with a neighbor in S, and no neighbor in I_0. 
Case 2: v ∉ S, and no neighbor in I_0.

Pr[Case 2] = (1-p) · Pr[no neighbor in I_0 | v ∉ S]

As computed: Pr[u ∈ I_0 | v ∉ S] = p(1-p)^{d-1} for each neighbor u.

If independent: Pr[no neighbor in I_0 | v ∉ S] = (1 - p(1-p)^{d-1})^d.

Pr[Case 2] = (1-p)(1 - p(1-p)^{d-1})^d.

Pr[Case 1] = p · Pr[v has a neighbor in S | v ∈ S] · Pr[no neighbor in I_0 | v ∈ S, v has a neighbor in S]

This is more complex. Let me just bound Pr[v ∈ U] ≤ Pr[v ∉ S and no neighbor in I_0] = (1-p)(1 - p(1-p)^{d-1})^d.

Actually wait, Pr[v ∈ U] ≤ Pr[no neighbor in I_0] (since v ∈ U requires no neighbor in I_0).

Pr[no neighbor in I_0] = Pr[∀u ∈ N(v): u ∉ I_0]

u ∉ I_0 iff u ∉ S or u has a neighbor in S.

Pr[u ∉ I_0] = 1 - p(1-p)^d (since u ∈ I_0 iff u ∈ S and no neighbor of u in S, which has probability p(1-p)^d).

If independent: Pr[no neighbor in I_0] = (1 - p(1-p)^d)^d.

So Pr[v ∈ U] ≤ (1 - p(1-p)^d)^d.

E[|U|] ≤ n(1 - p(1-p)^d)^d.

E[|I|] ≤ np(1-p)^d + n(1 - p(1-p)^d)^d.

Let q = p(1-p)^d. Then:

E[|I|] ≤ nq + n(1-q)^d.

We want to minimize q + (1-q)^d over q ∈ (0,1).

Take derivative: 1 - d(1-q)^{d-1} · (-1) = 1 + d(1-q)^{d-1}... wait, d/dq [q + (1-q)^d] = 1 - d(1-q)^{d-1}.

Set to 0: 1 = d(1-q)^{d-1}, so (1-q)^{d-1} = 1/d, so 1-q = d^{-1/(d-1)}, so q = 1 - d^{-1/(d-1)}.

For large d: q ≈ 1 - e^{-ln d/(d-1)} ≈ ln d / d.

Then (1-q)^d = d^{-d/(d-1)} ≈ d^{-1} = 1/d.

E[|I|]/n ≤ q + (1-q)^d ≈ (ln d)/d + 1/d = (1 + ln d)/d.

So E[|I|] ≤ n(1 + ln d)/d.

Now, we need to check that q = p(1-p)^d can be set to the optimal value. We need p(1-p)^d = q = 1 - d^{-1/(d-1)} ≈ ln d / d.

For p = ln d / d: p(1-p)^d ≈ (ln d / d) · e^{-ln d} = (ln d / d) · (1/d) = ln d / d². This is too small (we need ln d / d, not ln d / d²).

For p = 1 - 1/d^{1/d} ≈ ln d / d (for large d): (1-p)^d = (1/d^{1/d})^d = 1/d. So p(1-p)^d ≈ (ln d / d)(1/d) = ln d / d². Still too small.

Hmm, the issue is that p(1-p)^d is maximized at p = 1/(d+1), giving p(1-p)^d = (1/(d+1))(d/(d+1))^d ≈ 1/(ed). So the maximum of q = p(1-p)^d is about 1/(ed), which is much smaller than ln d / d.

So we can't achieve q = ln d / d with this method. The bound becomes:

E[|I|]/n ≤ q + (1-q)^d where q ≤ 1/(ed).

With q = 1/(ed): (1-q)^d ≈ e^{-d/(ed)} = e^{-1/e} ≈ 0.69.

So E[|I|]/n ≤ 1/(ed) + 0.69, which is about 0.69. That's a constant, not o(1).

This approach doesn't give a good bound. The issue is that the independence assumption for the events "u ∉ I_0" doesn't hold, and the bound is too loose.

Let me go back to the tree-based ODE analysis, which gave the correct answer.

**Revisiting the ODE analysis:**

I showed that for the d-regular tree (and approximately for d-regular graphs with girth ≥ 5), the random greedy MIS has expected size:

E[|I|]/n = (1/2)(1 - (d-1)^{-2/(d-2)})

For d = n^ε → ∞:

(d-1)^{-2/(d-2)} = exp(-2 ln(d-1)/(d-2)) → 1, but at rate 2 ln d / d.

So E[|I|]/n = (1/2)(2 ln d / d + O((ln d)²/d²)) = ln d / d + O((ln d)²/d²).

E[|I|] = n ln d / d (1 + o(1)) = n^{1-ε} · ε ln n · (1 + o(1)).

This is o(n).

Now, the key question is: does the tree analysis give an upper bound for graphs with girth ≥ 5, or just an approximation?

Let me think about this. The ODE analysis assumed that the events "u_i is selected" for different neighbors u_i of v are independent. On the tree, they are exactly independent. On a graph with girth ≥ 5, they are not exactly independent because of cycles of length ≥ 5.

However, I claim that for girth ≥ 5, the tree analysis gives an UPPER BOUND on E[|I|]. Here's why:

The events "u_i is selected" for different neighbors of v are positively correlated (or at least not negatively correlated) due to the FKG inequality, because the selection of one neighbor makes it slightly more likely that another is selected (through shared descendants at distance ≥ 3). Wait, actually I'm not sure about the direction.

Let me think about it differently. The key property is:

Pr[v selected | label(v) = t] = Π_i Pr[u_i doesn't kill v | label(v) = t] (on the tree, by independence)

On the graph, Pr[v selected | label(v) = t] ≤ Π_i Pr[u_i doesn't kill v | label(v) = t] (if the events are negatively correlated) or ≥ (if positively correlated).

If the events "u_i kills v" are positively correlated, then Pr[none kills v] ≤ Π Pr[u_i doesn't kill v], so Pr[v selected] ≤ tree value. This would give an upper bound.

If negatively correlated, Pr[v selected] ≥ tree value, giving a lower bound.

For the random greedy process, I believe the events are positively correlated (by the FKG inequality, since the process has a natural monotonicity structure). If so, the tree value is an upper bound, and we're done.

But I'm not confident about the FKG application here. Let me try a different approach to get a rigorous upper bound.

**Rigorous upper bound without tree approximation:**

I'll prove that for any d-regular graph with girth ≥ 5, E[|I|] ≤ Cn ln d / d for some constant C, where I is the random greedy MIS.

**Proof:**

We use the random greedy algorithm with random labels in [0,1]. For each vertex v, let f(v) = label(v). v is selected iff no neighbor u with f(u) < f(v) is selected.

**Key observation**: v is selected only if v is the "local minimum" in some sense. Specifically, consider the set A_v = {v} ∪ N(v). If v has the minimum label in A_v, then v is definitely selected (no neighbor has a smaller label, so no neighbor is processed before v, so v is alive when processed). This happens with probability 1/(d+1).

But v could also be selected even if it's not the minimum in A_v (if the minimum neighbor is killed by its own neighbors). So Pr[v selected] ≥ 1/(d+1).

For an upper bound, I need to show Pr[v selected] ≤ C ln d / d.

**Upper bound approach**: v is selected implies v is alive when processed. v is alive when processed implies no neighbor u with f(u) < f(v) is selected. 

Consider the neighbors of v with labels less than f(v) = t. There are about dt such neighbors (in expectation). For v to be selected, ALL of them must be not selected. Each such neighbor u is not selected iff u is killed before it's processed (some neighbor of u with a smaller label is selected).

By girth ≥ 5, the neighborhoods of different neighbors of v (excluding v) are disjoint. So the events "u_i is killed before processing" are independent (they depend on disjoint sets of vertices).

Wait, but "u_i is killed" depends on the selection of vertices in u_i's neighborhood (excluding v), which are disjoint for different i. So the events are independent!

Let me formalize this. For a neighbor u_i of v with f(u_i) = s_i < t:

u_i is not selected iff u_i is killed before processing, i.e., some neighbor w of u_i with f(w) < s_i is selected. The neighbors of u_i are v (with f(v) = t > s_i, so v doesn't kill u_i) and w_{i,1}, ..., w_{i,d-1}.

The events "u_i is killed" depend on {w_{i,j}} and their neighborhoods. By girth ≥ 5, the sets {w_{i,j} : j=1,...,d-1} are disjoint for different i, AND their neighborhoods (beyond u_i) are also disjoint (no 4-cycles). 

But what about longer cycles? Could w_{i,j} and w_{i',j'} share a common neighbor (at distance 3 from v)? Yes, if there's a 5-cycle or longer. In that case, the events "u_i is killed" and "u_{i'} is killed" would not be independent.

However, the dependence is through vertices at distance ≥ 3 from v, and the effect is small for large d (the branching process dies out quickly).

For a rigorous bound, let me use the following approach:

**Upper bound via sequential conditioning:**

Process the neighbors u_1, ..., u_d of v one by one (in order of their labels). At each step, condition on the outcome of the previous neighbors.

Pr[v selected | f(v) = t] = Pr[no u_i with f(u_i) < t is selected]

= Π_{i: f(u_i) < t} Pr[u_i not selected | previous u_j's not selected, f(v) = t]

The key is that conditioning on "previous u_j's not selected" can only DECREASE the probability that u_i is selected (because the previous u_j's not being selected means their neighborhoods were "active", which could have killed some of u_i's neighbors, making u_i less likely to be selected).

Wait, actually, it's the opposite. If previous u_j's were not selected, it means their killing vertices (in their neighborhoods) were selected. These killing vertices are at distance 2 from v, and they could be shared with u_i's neighborhood (at distance 3 from v, through 5-cycles). If a killing vertex for u_j is also a neighbor of a neighbor of u_i, it could kill u_i's neighbor, making u_i less likely to be selected. So conditioning on "u_j not selected" could make "u_i not selected" more likely (positive correlation).

If the events are positively correlated, then:

Pr
