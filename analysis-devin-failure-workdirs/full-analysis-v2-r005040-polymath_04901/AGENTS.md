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
  <problem_id>polymath_04901</problem_id>
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

Some cells of a $10 \times 10$ are colored blue. A set of six cells is called [i]gremista[/i] when the cells are the intersection of three rows and two columns, or two rows and three columns, and are painted blue. Determine the greatest value of $n$ for which it is possible to color $n$ chessboard cells blue such that there is not a [i]gremista[/i] set.

## Standard Solution

To solve this problem, we need to determine the maximum number of blue cells that can be placed on a \(10 \times 10\) grid such that no set of six cells forms a *gremista* set. A *gremista* set is defined as a set of six cells that are the intersection of three rows and two columns, or two rows and three columns, and are all painted blue.

### Construction:
We start by constructing a valid \(10 \times 10\) grid with no *gremista* sets. The construction is based on an \(11 \times 11\) grid, where cells are chosen using the pattern \(\{y, y+1, y+2, y+4, y+7\} \pmod{11}\) in the \(y\)-th row. This pattern ensures that no *gremista* sets are formed. By deleting one row and one column from this \(11 \times 11\) grid, we obtain a valid \(10 \times 10\) grid.

### Bound:
To find the upper bound, we use a double-counting argument. Let \(a_i\) be the number of blue cells in the \(i\)-th column. We need to ensure that the sum of the binomial coefficients \(\binom{a_i}{2}\) over all columns does not exceed the total number of ways to choose two rows out of ten, multiplied by two (since a *gremista* set can be formed in two ways: three rows and two columns, or two rows and three columns).

\[
\sum_{i=1}^{10} \binom{a_i}{2} \leq 2 \binom{10}{2} = 90
\]

Since \(\binom{\bullet}{2}\) is a convex function, for a fixed sum \(\sum a_i\), the left-hand side is minimized when the \(a_i\) values are as equal as possible. We need to find the maximum \(n\) such that \(\sum a_i = n\) and \(\sum \binom{a_i}{2} \leq 90\).

Assume \(n = 47\). We need to distribute 47 blue cells among 10 columns such that the sum of the binomial coefficients is minimized. The optimal distribution is 3 columns with 4 blue cells each and 7 columns with 5 blue cells each:

\[
3 \binom{4}{2} + 7 \binom{5}{2} = 3 \cdot 6 + 7 \cdot 10 = 18 + 70 = 88
\]

This satisfies the inequality \(\sum \binom{a_i}{2} \leq 90\). However, if we try \(n = 48\), the sum of the binomial coefficients exceeds 90, making it impossible to have 48 blue cells without forming a *gremista* set.

### Verification:
To ensure that no *gremista* sets are formed, we need to check the distribution of blue cells in the rows. Let \(b_i\) be the number of blue cells in the \(i\)-th row within the 7 columns that have 5 blue cells each. We have:

\[
\sum_{i=1}^{10} b_i = 7 \cdot 5 = 35
\]

We need to ensure that:

\[
\sum_{i=1}^{10} \binom{b_i}{2} \leq 2 \binom{7}{2} = 42
\]

However, the convexity argument shows that:

\[
\sum_{i=1}^{10} \binom{b_i}{2} > 10 \binom{3.5}{2} = 43.75 > 42
\]

This contradiction implies that it is impossible to have 47 blue cells without forming a *gremista* set.

The final answer is \( \boxed{ 46 } \).

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. It's a combinatorics problem about a 10×10 grid where cells are colored blue, and we need to find the maximum number of blue cells such that no "gremista" set exists. A gremista set is 6 cells that form the intersection of 3 rows and 2 columns, or 2 rows and 3 columns, all colored blue.

So we need: no 3 rows and 2 columns where all 6 intersection cells are blue, AND no 2 rows and 3 columns where all 6 intersection cells are blue.

Let me think about this carefully.

A "gremista" set of type 1 (3 rows × 2 columns): 3 rows r1, r2, r3 and 2 columns c1, c2 such that all 6 cells (ri, cj) are blue.

A "gremista" set of type 2 (2 rows × 3 columns): 2 rows r1, r2 and 3 columns c1, c2, c3 such that all 6 cells (ri, cj) are blue.

So we need to avoid both configurations.

Let me think about this as a bipartite graph problem. We have a bipartite graph G with 10 row-vertices and 10 column-vertices, edges = blue cells. 

Type 1 gremista: K_{3,2} as a subgraph (3 rows connected to 2 columns, all 6 edges present).
Type 2 gremista: K_{2,3} as a subgraph (2 rows connected to 3 columns, all 6 edges present).

We need the maximum number of edges in a bipartite graph K_{10,10} that contains neither K_{3,2} nor K_{2,3} as a subgraph.

This is a Zarankiewicz-type problem. The Zarankiewicz number z(m,n;s,t) is the maximum number of edges in an m×n bipartite graph with no K_{s,t} subgraph.

We need min over both constraints: the graph must avoid both K_{3,2} and K_{2,3}.

By symmetry (10×10 is symmetric), avoiding K_{3,2} and avoiding K_{2,3} are symmetric constraints (swap rows and columns). So the maximum with both constraints equals the maximum with just one constraint, by symmetry? No, that's not quite right. The maximum number of edges avoiding both K_{3,2} AND K_{2,3} could be less than avoiding just one.

Actually, let me think about z(10,10;3,2) and z(10,10;2,3). By symmetry of the 10×10 grid, z(10,10;3,2) = z(10,10;2,3) (just transpose). But we need both constraints simultaneously.

Let me think about known results. The Kővári–Sós–Turán theorem gives upper bounds. For z(n,n;2,3) (no K_{2,3}), the bound is roughly n^{3/2} type.

Actually, let me think more carefully. 

For K_{2,3}-free bipartite graphs: this means no two rows share 3 common columns. For K_{3,2}-free: no two columns share 3 common rows.

So the constraint is:
- Any two rows share at most 2 common blue columns.
- Any two columns share at most 2 common blue rows.

This is a symmetric condition! Both say: any two vertices on the same side share at most 2 common neighbors.

So we need a bipartite graph on 10+10 vertices where every pair of vertices on the same side has at most 2 common neighbors. Maximize edges.

This is related to the concept of a "partial linear space" or codes.

If every pair shares at most 1 common neighbor, this is a partial linear space (like a partial Steiner system). With at most 2, it's a generalization.

Let me think about constructions.

Construction 1: Take a projective plane or similar structure. 

Actually, let me think about this differently. Consider the incidence structure. Each row is a subset of {1,...,10} (the columns it's connected to). The condition is:
- Any two row-subsets intersect in at most 2 elements.
- Any two column-subsets (sets of rows connected to each column) intersect in at most 2 elements.

We want to maximize the total size of all row-subsets.

Let me think about small cases and known results for the Zarankiewicz problem.

z(10,10;2,2) is known. But we need z with K_{2,3} and K_{3,2} both forbidden.

Hmm, let me think about this more concretely.

If all rows have the same degree d, then the number of edges is 10d. The condition that any two rows share at most 2 columns: Consider the columns. Each column is connected to some set of rows. If column j is connected to a_j rows, then the number of pairs of rows sharing column j is C(a_j, 2). The total number of pairs of rows sharing at least one column is at most sum C(a_j, 2), and since each pair shares at most 2 columns, we have:

sum_j C(a_j, 2) ≤ 2 * C(10, 2) = 2 * 45 = 90.

Also sum_j a_j = 10d (total edges).

By convexity, sum C(a_j, 2) ≥ 10 * C(d, 2) = 10 * d(d-1)/2 = 5d(d-1) when all a_j = d.

So 5d(d-1) ≤ 90, giving d(d-1) ≤ 18, so d ≤ 4 (since 4*3=12 ≤ 18, 5*4=20 > 18).

With d=4: 5*4*3 = 60 ≤ 90. ✓. Edges = 40.

But we also need the column condition: any two columns share at most 2 rows. By the same argument (symmetric), if all columns have degree d' = d = 4, then sum_i C(b_i, 2) ≤ 2*C(10,2) = 90 where b_i are row degrees. Same bound.

So with regular degree 4, we get 40 edges, and we need both conditions. Can we achieve 40?

Wait, but maybe we can do better with non-regular graphs. Let me reconsider.

The double counting gives: sum_j C(a_j, 2) ≤ 90 (from row condition) and sum_i C(b_i, 2) ≤ 90 (from column condition).

We want to maximize E = sum a_j = sum b_i.

By convexity, for fixed E and 10 columns, sum C(a_j, 2) is minimized when all a_j are equal (as equal as possible). So sum C(a_j, 2) ≥ 10 * C(E/10, 2) approximately = 10 * (E/10)(E/10 - 1)/2 = E(E-10)/20.

So E(E-10)/20 ≤ 90, giving E(E-10) ≤ 1800, E² - 10E - 1800 ≤ 0, E ≤ (10 + sqrt(100 + 7200))/2 = (10 + sqrt(7300))/2 ≈ (10 + 85.4)/2 ≈ 47.7.

So E ≤ 47 from the row condition alone. Similarly from the column condition. But both together might give a tighter bound.

Hmm, but actually both conditions give the same bound by symmetry. So E ≤ 47.

But can we actually achieve something close to 47? Let me think about whether 47 is achievable.

Actually, let me reconsider. The bound E ≤ 47 comes from one condition. Both conditions give the same bound. But achieving both simultaneously is the challenge.

Let me think about specific constructions.

Construction idea: Use a finite geometry. Consider GF(q) or something.

Actually, let me think about this problem differently. This is equivalent to finding the maximum number of 1s in a 10×10 0-1 matrix such that no 3×2 or 2×3 all-1s submatrix exists.

Let me think about known competition results. This seems like it could be from a math olympiad. The answer might be around 40-45.

Let me try to think about constructions more carefully.

Construction with degree 4 per row and per column (40 edges):
We need a 4-regular bipartite graph on 10+10 vertices where any two vertices on the same side share at most 2 common neighbors.

Actually, with degree 4 and 10 vertices on each side, any two rows share at most... let's see. Two rows each have 4 neighbors out of 10 columns. By inclusion-exclusion, they share at least 4+4-10 = -2, so no forced sharing. The condition is they share at most 2.

Can we construct such a graph? Let me try.

Think of it as a combinatorial design. We need 10 subsets of {1,...,10}, each of size 4, such that any two intersect in at most 2, AND the dual condition (any two columns' row-sets intersect in at most 2).

If the design is symmetric (self-dual), both conditions are the same.

A symmetric (10, 4, λ) design would have any two blocks intersecting in exactly λ points. We need λ ≤ 2. For a symmetric design, λ = k(k-1)/(v-1) = 4*3/9 = 12/9 = 4/3, which is not an integer. So no symmetric (10,4,λ) design exists.

But we don't need a full design, just a set of 10 subsets of size 4 with pairwise intersection ≤ 2, and the dual condition.

Let me try to construct one. 

Actually, let me think about whether we can do better than 40. Maybe 42 or 44?

Let me try degree 5 for some rows. If we have rows with varying degrees, say some with 5 and some with 4.

Let's say x rows have degree 5 and (10-x) rows have degree 4. Total edges E = 5x + 4(10-x) = 40 + x.

Column condition: sum C(a_j, 2) ≤ 90. With E = 40+x edges over 10 columns, the minimum of sum C(a_j,2) is when columns are as equal as possible. Average column degree = (40+x)/10 = 4 + x/10.

If x = 5, E = 45, average column degree = 4.5. Min sum C(a_j,2) = 5*C(5,2) + 5*C(4,2) = 5*10 + 5*6 = 50 + 30 = 80 ≤ 90. ✓

If x = 7, E = 47, average = 4.7. Min sum = 7*C(5,2) + 3*C(4,2) = 70 + 18 = 88 ≤ 90. ✓ (barely)

If x = 8, E = 48, average = 4.8. Min sum = 8*C(5,2) + 2*C(4,2) = 80 + 12 = 92 > 90. ✗

So from the column condition (or row condition), E ≤ 47.

But we need BOTH conditions. Let me check: if E = 47 with 7 rows of degree 5 and 3 rows of degree 4, then columns have degrees summing to 47. For the row condition (any two columns share ≤ 2 rows), we need sum C(b_i, 2) ≤ 90 where b_i are row degrees. sum C(b_i, 2) = 7*C(5,2) + 3*C(4,2) = 70 + 18 = 88 ≤ 90. ✓

And for the column condition, we need sum C(a_j, 2) ≤ 90 where a_j are column degrees. The column degrees sum to 47, and to minimize sum C(a_j,2), we want them as equal as possible: 7 columns of degree 5 and 3 of degree 4. Then sum = 88 ≤ 90. ✓

So the counting bound allows E = 47. But can we actually construct such a configuration? The counting bound is necessary but not sufficient.

Hmm, this is getting complex. Let me think about whether there's a cleaner approach.

Let me reconsider. The problem is from a competition (looks like it could be from a Latin American olympiad given "gremista"). Let me think about what the answer likely is.

Let me try to think about this more carefully with a construction.

Let me try to use a construction based on a finite field or algebraic structure.

Consider the affine plane or a similar structure. 

Actually, let me try a different approach. Consider the 10×10 grid. Let me try to use a construction based on a 2-(v,k,λ) design or similar.

Let me try thinking about it as follows. We want a bipartite graph where every pair on the same side shares ≤ 2 neighbors. 

One approach: Use a graph based on a projective plane of order 3, which has 13 points and 13 lines, each line has 4 points, each point on 4 lines, any two points on exactly 1 line, any two lines meet in exactly 1 point. If we take a substructure of this...

Projective plane of order 3: PG(2,3). 13 points, 13 lines, each line has 4 points, each point on 4 lines. Any two lines meet in exactly 1 point, any two points determine exactly 1 line.

If we select 10 points and 10 lines from this plane, and use the incidence relation, then any two lines share at most 1 point (good, ≤ 2), and any two points share at most 1 line (good, ≤ 2). The number of edges would be the number of incidences between the selected points and lines.

Each line has 4 points, but some might not be in our selected 10. Each point is on 4 lines, but some might not be in our selected 10.

If we select 10 points and 10 lines, the number of incidences is at most 10*4 = 40 (if every selected line's 4 points are all selected) but likely less.

Hmm, this gives at most 40, and likely less since not all incidences will be within our selection.

Let me think differently.

Actually, maybe I should think about this problem more carefully. Let me reconsider the upper bound.

Upper bound proof:

Let the bipartite graph have 10 row-vertices R and 10 column-vertices C, with E edges (blue cells). The condition is that no K_{3,2} or K_{2,3} exists, i.e., any two vertices on the same side have at most 2 common neighbors.

Counting pairs: For each column c, let d(c) be its degree. The number of pairs of rows that are both adjacent to c is C(d(c), 2). Since each pair of rows has at most 2 common column-neighbors:

∑_c C(d(c), 2) ≤ 2 · C(10, 2) = 90.

Similarly, for each row r with degree d(r):
∑_r C(d(r), 2) ≤ 2 · C(10, 2) = 90.

Now, E = ∑_c d(c) = ∑_r d(r).

By the convexity of f(x) = x(x-1)/2:

∑_c C(d(c), 2) ≥ 10 · C(E/10, 2) = 10 · (E/10)(E/10 - 1)/2 = E(E-10)/20.

So E(E-10)/20 ≤ 90 → E(E-10) ≤ 1800 → E² - 10E - 1800 ≤ 0 → E ≤ (10 + √(100+7200))/2 = (10 + √7300)/2.

√7300 ≈ 85.44, so E ≤ 47.72, thus E ≤ 47.

So the upper bound is 47.

Now I need to check: is 47 achievable? And if not, what's the actual maximum?

Let me try to construct a configuration with 47 edges.

We need 7 rows of degree 5 and 3 rows of degree 4 (or some other split summing to 47), and similarly for columns. And the pairwise intersection conditions.

Actually, let me reconsider. The bound E ≤ 47 requires near-equality in the convexity bound, which means the degrees must be nearly equal. For E = 47, we'd need column degrees to be 7 fives and 3 fours (or 8 fives, 1 four, 1 three — but that gives higher sum of C(a_j,2)).

Let me check: 7 fives and 3 fours: sum = 35 + 12 = 47. ✓. sum C(a_j,2) = 7·10 + 3·6 = 70 + 18 = 88 ≤ 90. ✓

And row degrees: also 7 fives and 3 fours: sum C(b_i,2) = 88 ≤ 90. ✓

So we need a bipartite graph with 7 rows of degree 5, 3 rows of degree 4, 7 columns of degree 5, 3 columns of degree 4, and any two same-side vertices share ≤ 2 neighbors.

This is a very constrained problem. Let me think about whether this is feasible.

Actually, let me think about this differently. Maybe the answer is not 47 but something smaller. Let me think about what constructions are known.

Hmm, let me try to think about this from a coding theory perspective. 

Consider the 10×10 binary matrix M. The condition "any two rows share at most 2 common 1s" means: for any two rows r_i, r_j, the dot product (r_i · r_j) ≤ 2. Similarly for columns.

This is like a code with restricted inner products.

Let me think about a specific construction. 

Construction attempt: Let me use a circulant-type construction.

Consider rows indexed 0-9 and columns indexed 0-9. For row i, color columns {i, i+1, i+2, i+3} mod 10 (4 consecutive columns). Then each row has degree 4, total edges = 40.

Two rows i and j: row i has columns {i, i+1, i+2, i+3}, row j has columns {j, j+1, j+2, j+3}. The intersection size depends on |i-j| mod 10. If |i-j| = 1, intersection = {i+1, i+2, i+3} ∩ ... = 3. That's > 2! So this fails.

Let me try a different construction. 

How about using a difference set approach? 

Take the group Z_10. We want a subset S of size k such that the differences cover each element at most 2 times (for the row condition), and similarly for columns.

If we use the same set S for each row (shifted), i.e., row i connects to columns {i+s : s ∈ S}, then:
- Two rows i, j share columns corresponding to S ∩ (S + (j-i)). The size of this intersection is the number of representations of (j-i) as a difference of elements of S.
- For the column condition, by symmetry (since the construction is symmetric), two columns share the same number of rows.

So we need a subset S ⊆ Z_10 of size k such that every nonzero difference appears at most 2 times as s1 - s2 with s1, s2 ∈ S.

The number of ordered differences is k(k-1). These are distributed among 9 nonzero elements of Z_10. If each appears at most 2 times, we need k(k-1) ≤ 9·2 = 18, so k ≤ 4 (since 4·3 = 12 ≤ 18, 5·4 = 20 > 18).

With k = 4, total edges = 40. We need S of size 4 in Z_10 with each difference appearing ≤ 2 times.

Let me try S = {0, 1, 3, 7}. Differences:
1-0=1, 3-0=3, 7-0=7, 0-1=9, 3-1=2, 7-1=6, 0-3=7, 1-3=8, 7-3=4, 0-7=3, 1-7=4, 3-7=6.

Differences: 1, 3, 7, 9, 2, 6, 7, 8, 4, 3, 4, 6.
Count: 1→1, 2→1, 3→2, 4→2, 6→2, 7→2, 8→1, 9→1. All ≤ 2. ✓

So S = {0, 1, 3, 7} works! This gives a 4-regular bipartite graph with 40 edges, and any two same-side vertices share at most 2 common neighbors.

Can we do better than 40? Let me think about whether we can add more edges to this construction or use a different approach.

The upper bound is 47. Can we achieve more than 40?

Let me think about this. Maybe the answer is 40, or maybe it's higher.

Let me try to think about constructions with more edges.

What if we don't use a circulant construction? Let me try to think about it more generally.

Let me try E = 42. We need, say, 2 rows of degree 5 and 8 rows of degree 4 (sum = 10+32 = 42). Column degrees sum to 42, so maybe 2 columns of degree 5 and 8 of degree 4.

sum C(a_j, 2) = 2·10 + 8·6 = 20 + 48 = 68 ≤ 90. ✓ (lots of room)
sum C(b_i, 2) = 2·10 + 8·6 = 68 ≤ 90. ✓

So the counting bound is satisfied with room to spare. The question is whether such a graph exists.

Hmm, but the counting bound being satisfied doesn't guarantee existence. Let me think about this more carefully.

Actually, I wonder if the answer is 40. Let me think about why.

Consider the projective plane of order 3, PG(2,3). It has 13 points and 13 lines, with 4 points per line and 4 lines per point. Any two points are on exactly 1 common line, any two lines meet in exactly 1 point.

If we could embed a 10×10 substructure... but this gives degree 4 and 40 edges at most (if we could get all incidences).

Actually, let me think about this differently. Let me consider the problem from the perspective of the competition. The answer is likely a "nice" number. Given the upper bound of 47, the answer could be 40, 42, 44, 45, 46, or 47.

Let me try harder to construct something with more than 40 edges.

Let me try to use a computer-search-like reasoning. 

Actually, let me think about this more carefully using a known result. The problem of finding the maximum number of edges in a bipartite graph with no K_{2,3} is the Zarankiewicz problem z(n,n;2,3).

For z(n,n;2,3), known values: z(10,10;2,3) might be known. But we need both K_{2,3} and K_{3,2} forbidden, which by symmetry of 10×10 is the same as just one of them (since the graph and its transpose both need to satisfy the condition, and the max over graphs satisfying both equals... hmm, not exactly).

Wait. z(10,10;2,3) is the max edges with no K_{2,3}. z(10,10;3,2) is the max with no K_{3,2}. By symmetry (transpose), z(10,10;2,3) = z(10,10;3,2). But we need both, which could be less.

Let me look at this from a different angle. 

The condition "any two rows share ≤ 2 columns" is equivalent to "no K_{2,3}" (no 2 rows with 3 common columns). The condition "any two columns share ≤ 2 rows" is equivalent to "no K_{3,2}" (no 2 columns with 3 common rows, which means no 3 rows with 2 common columns... wait, no).

Hmm, let me re-examine. K_{3,2} means 3 rows and 2 columns with all 6 edges. This means 2 columns that are both connected to the same 3 rows, i.e., 2 columns sharing ≥ 3 common rows. So "no K_{3,2}" ⟺ "any two columns share ≤ 2 rows."

K_{2,3} means 2 rows and 3 columns with all 6 edges, i.e., 2 rows sharing ≥ 3 common columns. So "no K_{2,3}" ⟺ "any two rows share ≤ 2 columns."

So our condition is exactly: no K_{2,3} AND no K_{3,2}.

Now, z(10,10;2,3) = max edges with no K_{2,3}. This only constrains row pairs. The column pairs are unconstrained. So z(10,10;2,3) could be larger than our answer.

Similarly, z(10,10;3,2) = max edges with no K_{3,2}, only constraining column pairs.

Our answer is ≤ min(z(10,10;2,3), z(10,10;3,2)) = z(10,10;2,3) (by symmetry).

But our answer could be strictly less, since we need both constraints.

Let me think about what z(10,10;2,3) is. 

For the Zarankiewicz problem, z(m,n;2,t), there are known results. For z(n,n;2,2), it's related to projective planes. For z(n,n;2,3)...

The Kővári–Sós–Turán bound gives z(n,n;2,t) ≤ n^{1+1/t} · t^{1/t} / 2 + n/2 or something like that. For t=3, this is roughly n^{4/3}.

For n=10: 10^{4/3} ≈ 21.5. But this is a rough asymptotic bound. The actual value could be higher for small n.

Hmm, actually the KST bound for z(m,n;s,t) with s=2 is:
z(m,n;2,t) ≤ (t-1)^{1/t} · m · n^{1-1/t} + n/2

For m=n=10, t=3: z ≤ 2^{1/3} · 10 · 10^{2/3} + 5 ≈ 1.26 · 10 · 4.64 + 5 ≈ 58.4 + 5 ≈ 63.

That's a weak bound. Let me use the exact counting argument instead.

For no K_{2,3}: any two rows share ≤ 2 columns. 
∑_c C(d(c), 2) ≤ 2 · C(10, 2) = 90.
∑ C(d(c),2) ≥ 10 · C(E/10, 2) = E(E-10)/20.
So E(E-10) ≤ 1800, E ≤ 47.

This is the same bound as before. So z(10,10;2,3) ≤ 47.

For our problem (both constraints), the same bound applies (both give E ≤ 47).

Now the question is: what's the actual maximum? Is it 47, or less?

Let me try to think about constructions more carefully.

Let me try to construct a graph with 40 edges (degree 4 regular) and then see if I can add edges.

Using S = {0,1,3,7} in Z_10, I get a 4-regular graph with 40 edges. Can I add an edge without creating a K_{2,3} or K_{3,2}?

Adding edge (r, c) where it doesn't currently exist. This increases d(r) to 5 and d(c) to 5. We need to check that no pair of rows now shares 3 columns, and no pair of columns shares 3 rows.

In the circulant construction, row r is connected to {r, r+1, r+3, r+7} mod 10. Adding edge (r, c) means row r is now connected to {r, r+1, r+3, r+7, c}. For any other row r', the intersection with row r's set was at most 2. Adding c could increase it to 3 if c was already in row r''s set and the intersection was already 2.

This is getting complicated. Let me try a different approach.

Let me think about whether the answer might be exactly 40, based on the following reasoning:

Consider the 10 rows as 10 subsets of a 10-element set, with pairwise intersections ≤ 2. The Fisher-type inequality or Ray-Chaudhuri-Wilson theorem might give bounds.

Actually, the Ray-Chaudhuri-Wilson theorem says: if you have m subsets of an n-element set, all of size k, with pairwise intersections in a set L of s values, then m ≤ C(n, s). Here, intersections are in {0, 1, 2}, so s = 3, and m ≤ C(10, 3) = 120. That's not restrictive.

But we also have the dual condition. Hmm.

Let me try yet another approach. Let me think about the problem as a matrix problem.

We have a 10×10 0-1 matrix M with no 3×2 or 2×3 all-1s submatrix. We want to maximize the number of 1s.

Let me think about the complement. Let N = J - M (where J is all-1s). Then N has 100 - E zeros... no, N has 100 - E ones (the non-blue cells). A 3×2 all-1s submatrix in M corresponds to a 3×2 all-0s submatrix in N. So we need: no 3×2 or 2×3 all-0s submatrix in N. We want to minimize the number of 1s in N (= 100 - E), i.e., maximize E.

This is the same problem, just dualized. Not immediately helpful.

Let me try to think about specific constructions with more than 40 edges.

Construction attempt with 44 edges:

Let me try to use a structure based on a 2-(11, 5, 2) design or similar.

Actually, let me think about the Hadamard matrix connection. A Hadamard matrix of order 12 exists. From it, we can derive a 2-(11, 5, 2) design (the Paley design or similar). This design has 11 blocks of size 5 on 11 points, with any two blocks intersecting in exactly 2 points.

If we take this design and remove one point and its block, we might get a structure on 10 points.

The 2-(11, 5, 2) design (Hadamard 2-design): 11 points, 11 blocks, each block has 5 points, each point is in 5 blocks, any two blocks meet in 2 points, any two points are in 2 common blocks.

If we remove one point p and one block B (with p ∈ B), we get a structure on 10 points with 10 blocks. But the blocks no longer all have the same size, and the intersection properties change.

Let me think more carefully. Start with the 2-(11, 5, 2) design. Remove point p. The blocks that contained p now have 4 points (on the remaining 10 points), and the blocks that didn't contain p still have 5 points. There are 5 blocks containing p and 6 blocks not containing p.

If we use all 11 blocks on the 10 remaining points, we get a 10×11 incidence matrix. But we need 10×10. 

Alternatively, remove one block as well. If we remove a block B that doesn't contain p, we have 10 blocks on 10 points: 5 blocks of size 4 (those that contained p) and 5 blocks of size 5 (those that didn't contain p, minus the one we removed). Wait, 6 blocks didn't contain p, removing 1 leaves 5. So 5 blocks of size 4 and 5 blocks of size 5. Total edges = 5·4 + 5·5 = 20 + 25 = 45.

Now check the intersection conditions:
- Any two of the 10 blocks: in the original design, any two blocks intersect in exactly 2 points. After removing p, if both blocks contained p, their intersection decreases by 1 (from 2 to 1). If neither contained p, intersection stays 2. If one contained p and the other didn't, intersection stays 2 (since p wasn't in the second block).

So pairwise intersections: blocks that both contained p intersect in 1 point; all other pairs intersect in 2 points. All ≤ 2. ✓ (row condition satisfied)

Now for the column condition (dual): any two points share at most 2 blocks. In the original design, any two points are in exactly 2 common blocks. After removing point p and block B:
- For two points q, r ≠ p: they were in 2 common blocks. If B was one of those common blocks, now they're in 1 common block. Otherwise, still 2. So ≤ 2. ✓

Wait, but we also removed point p. The columns now correspond to the 10 remaining points. For any two of these points, they were in exactly 2 common blocks in the original 11-block design. We removed one block B, so if B was a common block of q and r, they now share 1 block; otherwise 2. Either way ≤ 2. ✓

So this construction gives 45 edges with both conditions satisfied!

Let me double-check. We start with a 2-(11, 5, 2) design. This is a symmetric design: 11 points, 11 blocks, each block has 5 points, each point in 5 blocks, λ = 2 (any two points in 2 common blocks, any two blocks meet in 2 points).

Remove point p and block B (where B does not contain p, or does it matter?).

Wait, I need to be more careful. Let me re-examine.

We remove point p. Now we have 10 points and 11 blocks, but the blocks that contained p now have 4 points each. We need to remove one block to get 10 blocks. 

If we remove a block B that contained p: then B had 5 points including p, so on the remaining 10 points it had 4 points. We remove this block. Remaining: 10 blocks on 10 points. 4 blocks of size 4 (the other blocks that contained p) and 6 blocks of size 5 (blocks that didn't contain p). Total edges = 4·4 + 6·5 = 16 + 30 = 46.

Check intersections:
- Two blocks that both contained p: originally intersected in 2 points, one of which was p. Now intersect in 1 point. ✓
- Two blocks that both didn't contain p: originally intersected in 2 points, neither was p. Still 2. ✓
- One block that contained p, one that didn't: originally intersected in 2 points. The one that didn't contain p doesn't have p, so the intersection is still 2. ✓

All ≤ 2. ✓

Column condition: any two of the 10 remaining points q, r were in exactly 2 common blocks in the original design. We removed block B (which contained p). If B was a common block of q and r (i.e., q, r ∈ B), then they now share 1 block. Otherwise 2. But wait, B contained p and 4 other points. So for any two of those 4 points in B, B was a common block, so they now share 1 block. For all other pairs, still 2. All ≤ 2. ✓

So this gives 46 edges!

Can we do even better? What if we remove a block B that did NOT contain p?

Remove point p and block B (B not containing p). Remaining: 10 blocks on 10 points. 5 blocks of size 4 (blocks that contained p) and 5 blocks of size 5 (blocks that didn't contain p, minus B). Total edges = 5·4 + 5·5 = 20 + 25 = 45.

That's 45, less than 46. So removing a block containing p is better.

So with 46 edges, we have a valid configuration. Can we get 47?

For 47, we'd need the degree sequence to be 7 fives and 3 fours (or similar). In our construction, we have 4 fours and 6 fives (for rows) and... let me check the column degrees.

In the construction with 46 edges: 4 blocks of size 4 and 6 blocks of size 5. So row degrees (block sizes) are 4,4,4,4,5,5,5,5,5,5. Column degrees (point degrees): each of the 10 remaining points was in 5 blocks in the original design. We removed one block B (which contained p and 4 other points). The 4 points that were in B now have degree 4 (lost one block). The other 6 points still have degree 5. So column degrees are also 4,4,4,4,5,5,5,5,5,5.

Total = 4·4 + 6·5 = 16 + 30 = 46. ✓

sum C(d, 2) for rows = 4·6 + 6·10 = 24 + 60 = 84 ≤ 90. ✓
sum C(d, 2) for columns = 84 ≤ 90. ✓

For 47, we'd need sum = 47, e.g., 3 fours and 7 fives: 3·4 + 7·5 = 12 + 35 = 47. sum C(d,2) = 3·6 + 7·10 = 18 + 70 = 88 ≤ 90. ✓

Can we modify the construction to get 47? We'd need to add one more edge to the 46-edge construction. 

In the 46-edge construction, the 4 points that were in block B (along with p) have degree 4. If we could add one edge to increase one of these to degree 5, we'd have 47 edges. But we need to ensure the intersection conditions are still satisfied.

Adding an edge (r, c) where r is a block (row) and c is a point (column) that are not currently incident. This increases d(r) and d(c) by 1. We need to check:
1. Row r's intersection with every other row is still ≤ 2.
2. Column c's intersection with every other column is still ≤ 2.

Currently, all pairwise intersections are ≤ 2, with some being exactly 2. Adding an edge (r, c) increases the intersection of row r with any row r' that also contains c, by 1. So if row r and row r' currently share 2 points and r' contains c, then after adding (r, c), they share 3 points — violating the condition.

So we need: for the edge (r, c) we add, c is not in any row r' that currently shares 2 points with r.

Similarly for the column condition.

This is very constrained. Let me think about whether it's possible.

In the 2-(11,5,2) design, any two blocks meet in exactly 2 points. After removing p, blocks that both contained p meet in 1 point; all other pairs meet in 2 points.

So in our 10-block, 10-point structure:
- Pairs of blocks that both contained p: intersection = 1.
- All other pairs: intersection = 2.

If we want to add edge (r, c) to block r, we need c not currently in block r, and for every block r' that contains c, the intersection of r and r' is currently ≤ 1 (so it becomes ≤ 2 after adding).

The blocks r' containing c: there are d(c) of them. For each such r', we need |r ∩ r'| ≤ 1 currently.

If r is a block that contained p (size 4, and its intersections with other blocks that contained p are 1, with blocks not containing p are 2), and c is a point not in r:

The blocks containing c: some contained p, some didn't.
- If r' contained p and c ∈ r': |r ∩ r'| = 1 (both contained p). Adding c makes it 2. ✓
- If r' didn't contain p and c ∈ r': |r ∩ r'| = 2. Adding c makes it 3. ✗

So we need: no block r' that doesn't contain p has c as an element and intersects r in 2 points. But all blocks not containing p intersect r in 2 points. So we need: c is not in any block that doesn't contain p.

But c is a point in our 10-point set. How many blocks contain c? d(c) blocks. If c is one of the 4 points that was in B (the removed block), d(c) = 4. These 4 blocks: some contained p, some didn't. 

In the original design, c was in 5 blocks. One of them was B (which we removed). So c is in 4 remaining blocks. Of these 4, how many contained p? In the original design, p and c were together in λ = 2 blocks. One of these 2 blocks was B (since both p and c were in B). So 1 of the 2 blocks containing both p and c was B (removed), leaving 1 block containing both p and c among the remaining 10 blocks. So of the 4 remaining blocks containing c, 1 contained p and 3 didn't.

So c is in 3 blocks that didn't contain p. These all intersect r (which contained p) in 2 points. So adding (r, c) would make these intersections 3. ✗

What if r is a block that didn't contain p (size 5)? Then r intersects all other blocks in 2 points. Adding c to r: for any block r' containing c, |r ∩ r'| = 2, becomes 3. ✗ (unless no block containing c intersects r in 2, but all do).

So it seems impossible to add any edge to the 46-edge construction. 

But maybe a different construction achieves 47? Or maybe 46 is the maximum?

Hmm, let me reconsider. The upper bound is 47, and we've constructed 46. The question is whether 47 is achievable.

Let me think about this more carefully. For 47 edges, we need (roughly) 7 vertices of degree 5 and 3 of degree 4 on each side. The sum of C(d,2) = 88, which is close to the limit of 90. This means almost all pairs must share exactly 2 neighbors (with very few sharing less).

Let me count more carefully. The total number of pairs of rows sharing columns is ∑_c C(d(c), 2) = 88 (if column degrees are 7 fives and 3 fours). This counts the total number of (row-pair, column) incidences where both rows are in that column. Since each pair of rows shares at most 2 columns, the number of row-pairs sharing at least one column is at least 88/2 = 44. But there are C(10,2) = 45 pairs of rows. So at least 44 out of 45 pairs share at least one column, and the total "sharing" is 88, meaning most pairs share exactly 2 columns and at most one pair shares less.

More precisely: let s_{ij} be the number of columns shared by rows i and j. Then ∑_{i<j} s_{ij} = ∑_c C(d(c),2) = 88, and each s_{ij} ≤ 2. There are 45 pairs. If all s_{ij} = 2, the sum would be 90. We have 88, so the deficit is 2. This means either two pairs share 1 column (and the rest share 2), or one pair shares 0 columns (and the rest share 2), etc.

Similarly for columns: ∑_{i<j} t_{ij} = 88 where t_{ij} is the number of rows shared by columns i and j, each ≤ 2, 45 pairs, deficit 2.

This is a very tight structure. It's almost a 2-design. 

In fact, if we had a symmetric 2-(10, 5, 2) design, it would have 10 blocks of size 5, each point in 5 blocks, any two blocks meeting in 2 points, any two points in 2 common blocks. This would give 50 edges. But does such a design exist?

A symmetric 2-(v, k, λ) design requires λ(v-1) = k(k-1). For v=10, k=5, λ=2: 2·9 = 5·4 = 20. ✓. So the parameters are consistent. But does a symmetric 2-(10, 5, 2) design exist?

A symmetric 2-(v, k, λ) design exists only if certain conditions are met. For v=10, k=5, λ=2: the Bruck-Ryser-Chowla theorem says that if v is even, then k-λ must be a perfect square. k-λ = 5-2 = 3, which is not a perfect square. So no symmetric 2-(10, 5, 2) design exists!

So 50 edges is impossible (as expected, since our upper bound is 47).

Now, for 47 edges, we'd need a structure very close to this non-existent design. Given the non-existence of the design and the tightness of the constraints, 47 might be impossible.

Let me think about whether 46 is the answer or if we can push to 47.

Actually, let me reconsider the upper bound more carefully. Maybe I can get a tighter bound.

We have:
∑_c C(d(c), 2) ≤ 90  ... (1)
∑_r C(d(r), 2) ≤ 90  ... (2)
∑_c d(c) = ∑_r d(r) = E  ... (3)

From (1): ∑ d(c)² - ∑ d(c) ≤ 180, so ∑ d(c)² ≤ 180 + E.
From (3): ∑ d(c) = E, and by Cauchy-Schwarz, ∑ d(c)² ≥ E²/10.
So E²/10 ≤ 180 + E, giving E² - 10E - 1800 ≤ 0, E ≤ 47.72, E ≤ 47.

Same bound. Can we get a tighter bound using both (1) and (2) together?

From (1): ∑ d(c)² ≤ 180 + E.
From (2): ∑ d(r)² ≤ 180 + E.

These are the same bound applied to both sides. They don't combine to give a tighter bound directly.

Let me think about other approaches.

Another counting approach: Count triples (r1, r2, c) where r1, r2 are rows, c is a column, and both (r1,c) and (r2,c) are edges. This is ∑_c C(d(c), 2) ≤ 90.

Count triples (r, c1, c2) where r is a row, c1, c2 are columns, and both (r,c1) and (r,c2) are edges. This is ∑_r C(d(r), 2) ≤ 90.

These are the same constraints. I don't see how to combine them for a tighter bound.

Let me try a different approach. Consider the 10×10 matrix M. Let's think about it in terms of the singular values or rank.

Actually, let me try to think about this problem computationally. The answer is likely 40, 42, 44, 45, 46, or 47. We've constructed 46. Let me see if 47 is possible.

For 47, we need a very specific structure. Let me think about what constraints 47 imposes.

With E = 47, column degrees sum to 47. To minimize ∑ C(d(c),2), we want degrees as equal as possible: 7 fives and 3 fours (sum = 35+12 = 47, ∑C = 70+18 = 88) or 8 fives, 1 four, 1 three (sum = 40+4+3 = 47, ∑C = 80+6+3 = 89) or other distributions with higher ∑C.

The minimum ∑C is 88 (with 7 fives, 3 fours), and we need this ≤ 90. ✓

Similarly for rows. So both sides have degree sequence (5,5,5,5,5,5,5,4,4,4) (in some order).

Now, ∑_{i<j} s_{ij} = 88 where s_{ij} ≤ 2 and there are 45 pairs. The maximum possible sum is 90 (all pairs = 2). Deficit = 2.

Case 1: Two pairs have s = 1, rest have s = 2. (deficit = 2)
Case 2: One pair has s = 0, rest have s = 2. (deficit = 2)
Case 3: One pair has s = 1, one pair has s = 1, ... same as case 1.
Case 4: One pair has s = 0, one pair has s = 1, one pair has s = 1. (deficit = 3, too much)

Wait, deficit = 90 - 88 = 2. So:
- Two pairs with s = 1 (deficit 1 each), rest s = 2. Total deficit = 2. ✓
- One pair with s = 0 (deficit 2), rest s = 2. Total deficit = 2. ✓

Similarly for columns.

This is a very rigid structure. Let me think about whether it can be realized.

Actually, let me think about this using the theory of pairwise balanced designs or near-symmetric designs.

The structure we need for 47 edges is very close to a symmetric 2-(10, 5, 2) design (which doesn't exist by BRC). The non-existence of this design might prevent 47 from being achievable, but it's not a direct proof since we're not requiring a full design.

Let me try to think about this differently. Let me consider the specific case and try to either construct 47 or prove it's impossible.

Hmm, this is getting quite involved. Let me think about whether there's a cleaner argument.

Actually, let me reconsider. Let me think about the problem from the competition perspective. This is likely from a math olympiad, and the answer should be provable with elementary methods.

Let me reconsider the upper bound. Maybe I can get a tighter bound.

Alternative upper bound approach:

Consider the 10 rows. Let d_i be the degree of row i. The number of pairs (i, j) with i < j such that rows i and j share at least one column is at most... well, each such pair shares at most 2 columns.

Hmm, let me try a different counting.

For each pair of rows (i, j), let s_{ij} = number of common columns. We have s_{ij} ≤ 2 and ∑_{i<j} s_{ij} = ∑_c C(d(c), 2).

For each pair of columns (a, b), let t_{ab} = number of common rows. We have t_{ab} ≤ 2 and ∑_{a<b} t_{ab} = ∑_r C(d(r), 2).

Now, consider the number of "cherries" or paths of length 2. Actually, let me think about 4-cycles.

A 4-cycle is a set of 2 rows and 2 columns with all 4 edges present. The number of 4-cycles is ∑_{i<j} C(s_{ij}, 2) = ∑_{a<b} C(t_{ab}, 2).

Since s_{ij} ≤ 2, C(s_{ij}, 2) ≤ 1, so the number of 4-cycles ≤ 45 (number of row pairs). Similarly ≤ 45 (number of column pairs).

Also, ∑_{i<j} C(s_{ij}, 2) = ∑_{a<b} C(t_{ab}, 2). Let this be Q.

Now, ∑ s_{ij} = ∑_c C(d(c), 2) and ∑ C(s_{ij}, 2) = Q.

By convexity of C(x,2): ∑ C(s_{ij}, 2) ≥ 45 · C(∑s_{ij}/45, 2) = 45 · C(S/45, 2) where S = ∑ s_{ij}.

Hmm, this gives a relationship between S and Q but I'm not sure it helps directly.

Let me try yet another approach. 

Let me think about the problem in terms of the adjacency matrix. Let M be the 10×10 0-1 matrix. Consider MM^T (10×10 matrix). The (i,j) entry of MM^T is s_{ij} (for i≠j) or d_i (for i=j). The condition is that off-diagonal entries are ≤ 2.

Similarly, M^T M has off-diagonal entries t_{ab} ≤ 2.

The eigenvalues of MM^T and M^T M are the same (both are the squared singular values of M).

trace(MM^T) = ∑ d_i = E.
trace((MM^T)²) = ∑_{i,j} (MM^T)_{ij}² = ∑ d_i² + ∑_{i≠j} s_{ij}².

Since s_{ij} ≤ 2: ∑_{i≠j} s_{ij}² ≤ 4 · ∑_{i≠j} s_{ij} = 4S (where S = ∑_{i≠j} s_{ij} = ∑_c C(d(c),2) ≤ 90).

Also ∑ d_i² ≥ E²/10 (Cauchy-Schwarz).

So trace((MM^T)²) ≤ ∑ d_i² + 4S ≤ (180 + E) + 4·90 = 180 + E + 360 = 540 + E.

Wait, ∑ d_i² ≤ 180 + E (from the constraint ∑ C(d_i, 2) ≤ 90, i.e., ∑ d_i² - E ≤ 180).

And ∑_{i≠j} s_{ij}² ≤ 4 · 90 = 360 (since s_{ij} ≤ 2 and ∑ s_{ij} ≤ 90).

So trace((MM^T)²) ≤ (180 + E) + 360 = 540 + E.

Also, trace((MM^T)²) = ∑ σ_k² where σ_k are singular values of M, and ∑ σ_k² = trace(MM^T) = E (wait, that's ∑ σ_k² = trace(MM^T) = E? No.)

Actually, trace(MM^T) = ∑ σ_k² = E. And trace((MM^T)²) = ∑ σ_k⁴.

By power mean inequality: ∑ σ_k⁴ ≥ (∑ σ_k²)² / rank. If rank ≤ 10, then ∑ σ_k⁴ ≥ E²/10.

So E²/10 ≤ 540 + E, giving E² - 10E - 5400 ≤ 0, E ≤ (10 + √(100 + 21600))/2 = (10 + √21700)/2 ≈ (10 + 147.3)/2 ≈ 78.6.

That's a weaker bound. Not helpful.

Let me try to use the constraint more carefully.

∑_{i≠j} s_{ij}² ≤ 2 · ∑_{i≠j} s_{ij} (since s_{ij} ≤ 2, so s_{ij}² ≤ 2 s_{ij}).

So ∑_{i≠j} s_{ij}² ≤ 2S ≤ 180.

trace((MM^T)²) = ∑ d_i² + ∑_{i≠j} s_{ij}² ≤ (180 + E) + 180 = 360 + E.

And ∑ σ_k⁴ ≥ E²/10.

So E²/10 ≤ 360 + E, E² - 10E - 3600 ≤ 0, E ≤ (10 + √(100 + 14400))/2 = (10 + √14500)/2 ≈ (10 + 120.4)/2 ≈ 65.2.

Still weaker than 47. The spectral approach doesn't seem to help here.

Let me go back to the direct counting approach. The bound E ≤ 47 seems to be the best we can get from simple counting.

Now, the key question: is 47 achievable or is the maximum 46 (or lower)?

Let me think about this more carefully. We've shown a construction with 46 edges. Let me try to determine if 47 is possible.

For 47 edges with degree sequence (5^7, 4^3) on both sides:

The deficit from the "ideal" (all pairs sharing exactly 2) is 2 on each side. This means the structure is almost a 2-design.

Let me think about this using the following approach. Consider the 10×10 matrix M with 47 ones. The complement has 53 zeros. 

Actually, let me think about it differently. Let me consider the "excess" matrix.

Hmm, let me try a more direct approach. Let me try to see if 47 is achievable by attempting a construction or proving impossibility.

Approach: Try to modify the 46-edge construction.

In the 46-edge construction (from the 2-(11,5,2) design), we have 4 rows of degree 4 and 6 rows of degree 5, and similarly for columns. The 4 rows of degree 4 are the blocks that contained p (the removed point), and the 4 columns of degree 4 are the 4 points that were in B (the removed block, which also contained p).

To get 47, we need to increase one row and one column from degree 4 to degree 5. We showed that adding any single edge to the 46-edge construction creates a violation. But maybe a completely different construction achieves 47?

Let me think about whether there's a fundamental obstruction.

Consider the 47-edge case. We have 7 rows of degree 5 and 3 rows of degree 4. The 3 rows of degree 4: call them R1, R2, R3. The 7 rows of degree 5: R4, ..., R10.

∑_{i<j} s_{ij} = 88, deficit 2 from 90.

The 3 degree-4 rows have fewer columns, so they might share fewer columns with others. Let me think about the contribution of the degree-4 rows.

For a degree-4 row R1, the sum of s_{R1, j} over j ≠ 1 is the number of columns in R1, each shared with d(c) - 1 other rows. So ∑_{j≠1} s_{1j} = ∑_{c ∈ R1} (d(c) - 1).

If R1 has degree 4, and the columns it connects to have degrees summing to... well, the columns in R1 have various degrees. 

This is getting complicated. Let me try a different tactic.

Let me think about the problem using the following lemma:

Lemma: In a bipartite graph with parts of size n, if every pair of vertices on the same side has at most λ common neighbors, then the number of edges E satisfies E ≤ n·(1 + √(1 + 4λ(n-1)))/2.

Wait, let me derive this. We have ∑ C(d(c), 2) ≤ λ C(n, 2) = λn(n-1)/2. And ∑ d(c) = E, ∑ d(c)² = 2∑C(d(c),2) + E ≤ λn(n-1) + E.

By Cauchy-Schwarz: E²/n ≤ ∑ d(c)² ≤ λn(n-1) + E.
E² ≤ n(λn(n-1) + E) = λn²(n-1) + nE.
E² - nE - λn²(n-1) ≤ 0.
E ≤ (n + √(n² + 4λn²(n-1)))/2 = n(1 + √(1 + 4λ(n-1)))/2.

For n=10, λ=2: E ≤ 10(1 + √(1 + 72))/2 = 10(1 + √73)/2 = 5(1 + √73) ≈ 5(1 + 8.544) = 5 · 9.544 = 47.72.

So E ≤ 47. Same bound as before.

Now, the question of achievability. For the case n=10, λ=2, the bound gives E ≤ 47. The question is whether equality (or near-equality) can be achieved.

For equality in Cauchy-Schwarz, all d(c) must be equal, so d(c) = E/10 for all c. For E = 47, d(c) = 4.7, which is not an integer. So equality can't be achieved, confirming E ≤ 47 but not E = 47.

Wait, but we already knew E ≤ 47 (integer). The question is whether E = 47 is achievable.

For E = 47, the Cauchy-Schwarz bound gives ∑ d(c)² ≥ 47²/10 = 220.9, so ∑ d(c)² ≥ 221. And ∑ d(c)² = 2·∑C(d(c),2) + 47 ≤ 2·90 + 47 = 227. So 221 ≤ ∑ d(c)² ≤ 227.

With degree sequence (5^7, 4^3): ∑ d(c)² = 7·25 + 3·16 = 175 + 48 = 223. And 2·∑C(d(c),2) + 47 = 2·88 + 47 = 223. ✓. So ∑C(d(c),2) = 88 ≤ 90. ✓

The Cauchy-Schwarz "gap" is 223 - 221 = 2, which is small. This means the degrees are nearly equal, which is consistent.

But the real constraint is not just the sum but the actual pairwise intersection structure. Let me think about whether a 47-edge configuration can exist.

Let me try to think about this using a parity or modular argument.

Consider the 10×10 matrix M with 47 ones. Let's think about the rows of degree 4 (there are 3 of them). Each such row has 4 ones and 6 zeros. 

For a row of degree 4, say row r with columns {a, b, c, d}. The other 9 rows each share at most 2 columns with row r. The total sharing is ∑_{c' ∈ {a,b,c,d}} (d(c') - 1). 

The columns a, b, c, d have degrees that are either 4 or 5 (since column degrees are 5^7, 4^3). Let's say k of them have degree 5 and 4-k have degree 4. Then the total sharing for row r is k·4 + (4-k)·3 = 4k + 12 - 3k = k + 12.

This sharing is distributed among 9 other rows, each contributing at most 2. So k + 12 ≤ 18, i.e., k ≤ 6. Since k ≤ 4 (only 4 columns), this is always satisfied.

Also, each of the 9 other rows shares at least 0 with row r. The sharing k + 12 is at least 12 (when k=0) and at most 16 (when k=4).

Now, the 9 other rows have degrees 5 or 4. There are 6 rows of degree 5 and 2 rows of degree 4 (since row r is one of the 3 degree-4 rows, leaving 2 others).

For a row of degree 5, it shares at most 2 columns with row r. For a row of degree 4, same.

The total sharing is k + 12, distributed among 9 rows with each ≤ 2. So the number of rows sharing 2 columns with r is at least (k + 12) - 9·1 = k + 3 (if the rest share 1 each). Actually, let me think about it differently.

If x rows share 2 columns with r and 9-x rows share 1 column (assuming all share at least 1), then 2x + (9-x) = x + 9 = k + 12, so x = k + 3.

For k = 4 (all 4 columns of r have degree 5): x = 7. So 7 rows share 2 columns with r, 2 rows share 1 column.
For k = 3: x = 6. 6 rows share 2, 3 share 1.
For k = 2: x = 5. 5 rows share 2, 4 share 1.
For k = 1: x = 4. 4 rows share 2, 5 share 1.
For k = 0: x = 3. 3 rows share 2, 6 share 1.

But wait, some rows might share 0 columns with r. Let me redo this.

Let x_0, x_1, x_2 be the number of rows sharing 0, 1, 2 columns with r. Then:
x_0 + x_1 + x_2 = 9
x_1 + 2x_2 = k + 12

So x_0 = 9 - x_1 - x_2 = 9 - (k + 12 - 2x_2) - x_2 = 9 - k - 12 + x_2 = x_2 - k - 3.

For x_0 ≥ 0: x_2 ≥ k + 3.
For x_2 ≤ 9: k + 3 ≤ 9, k ≤ 6. ✓ (k ≤ 4)

So x_2 ≥ k + 3. For k = 4: x_2 ≥ 7, and x_0 = x_2 - 7, x_1 = 9 - x_0 - x_2 = 9 - (x_2 - 7) - x_2 = 16 - 2x_2. For x_1 ≥ 0: x_2 ≤ 8. So x_2 ∈ {7, 8}.

If x_2 = 7: x_0 = 0, x_1 = 2. All 9 rows share at least 1 column with r.
If x_2 = 8: x_0 = 1, x_1 = 0. 8 rows share 2, 1 row shares 0.

This analysis is for one degree-4 row. We have 3 such rows. The analysis gets complex when considering all three simultaneously.

This is getting very involved. Let me step back and think about whether the answer is 40, 46, or 47.

Given that:
1. The upper bound is 47.
2. We have a construction with 46 (from the 2-(11,5,2) design).
3. The structure required for 47 is extremely rigid (almost a non-existent symmetric design).

I suspect the answer might be 40 or 46. But let me think more.

Actually, wait. Let me reconsider. The 2-(11,5,2) design exists (it's the Hadamard 2-design from a Hadamard matrix of order 12). So the construction with 46 is valid.

Let me think about whether we can do better by using a different base design or construction.

What about using a 2-(13, 4, 1) design (projective plane of order 3)? It has 13 points, 13 lines, each line has 4 points, each point on 4 lines. Any two points on 1 line, any two lines meet in 1 point.

If we select 10 points and 10 lines, the incidence structure gives a bipartite graph. Any two lines share at most 1 point (≤ 2 ✓), any two points share at most 1 line (≤ 2 ✓). The number of edges is the number of incidences between selected points and lines.

To maximize incidences: each selected line has 4 points, but some might not be selected. Each selected point is on 4 lines, but some might not be selected.

If we select 10 points and 10 lines, the number of incidences is ∑ (number of selected points on each selected line). Each line has 4 points, and we've selected 10 out of 13 points, so on average 4·10/13 ≈ 3.08 selected points per line. Total ≈ 30.8, so about 31 edges. That's worse than 46.

What about other designs?

Let me think about the 2-(11, 5, 2) design more carefully and see if there's a way to get 47.

Actually, let me reconsider. In the 2-(11, 5, 2) design, instead of removing a point and a block, what if we remove two points and no blocks, or other combinations?

Remove 1 point, keep all 11 blocks: 10 points, 11 blocks. 5 blocks of size 4 (those containing the removed point) and 6 blocks of size 5. Total edges = 5·4 + 6·5 = 50. But we have 11 blocks (rows) and 10 points (columns), which is 11×10, not 10×10.

We need a 10×10 matrix. So we need to remove one more block (to get 10 blocks) or one more point (to get 9 points, but then it's 11×9).

If we remove 1 point and 1 block (as before), we get 10×10 with 46 or 45 edges.

What if we remove 2 points and add... no, we need exactly 10×10.

What about starting from a different design?

Let me think about the 2-(16, 6, 2) design or other designs. Actually, let me think about what designs could give a good 10×10 substructure.

Hmm, let me try a completely different approach. Let me think about the problem as a coding theory problem.

Consider the 10 rows as codewords of length 10 (binary). The condition is that any two codewords have inner product ≤ 2. We want to maximize the total weight.

This is related to the problem of finding a binary code with bounded inner products.

Actually, let me think about it as follows. The 10 rows are 10 binary vectors of length 10. The weight of vector i is d_i. The inner product of vectors i and j is s_{ij} ≤ 2. We want to maximize ∑ d_i.

The Gram matrix G = MM^T has diagonal entries d_i and off-diagonal entries s_{ij} ≤ 2. G is positive semidefinite.

Consider the matrix A = G - 2J + 2I (where J is all-1s and I is identity). Then A has diagonal entries d_i - 2 + 2 = d_i and off-diagonal entries s_{ij} - 2 ≤ 0.

Hmm, this doesn't immediately help.

Let me try another approach. Consider the matrix N = 2J - G (where G = MM^T). N has diagonal entries 2 - d_i and off-diagonal entries 2 - s_{ij} ≥ 0. 

N = 2J - MM^T. For N to be PSD (since G is PSD, this isn't guaranteed)...

Actually, let me think about the eigenvalue approach differently.

The all-1s vector 1 is an eigenvector of G = MM^T. G·1 = M·(M^T·1) = M·d where d is the vector of column degrees. If all column degrees are equal to d, then G·1 = d·M·1 = d·d_row where d_row is the vector of row degrees. If also all row degrees are d, then G·1 = d²·1, so d² is an eigenvalue.

For our near-regular case (degrees 4 and 5), this is approximately true.

Let me try to use the trace more carefully.

trace(G) = E = 47.
trace(G²) = ∑ d_i² + ∑_{i≠j} s_{ij}² = 223 + ∑_{i≠j} s_{ij}².

Now, ∑_{i≠j} s_{ij} = 2·88 = 176 (since ∑_{i<j} s_{ij} = 88 and we sum over ordered pairs).
∑_{i≠j} s_{ij}² ≤ 2·∑_{i≠j} s_{ij} = 352 (since s_{ij} ≤ 2, so s_{ij}² ≤ 2s_{ij}).

So trace(G²) ≤ 223 + 352 = 575.

Also, trace(G²) = ∑ σ_k⁴ ≥ (∑ σ_k²)²/10 = E²/10 = 2209/10 = 220.9. (This is weaker.)

And trace(G²) = ∑ σ_k⁴ ≥ trace(G)²/rank. If rank = 10, trace(G²) ≥ 47²/10 = 220.9.

The constraint trace(G²) ≤ 575 doesn't give a contradiction.

Let me try to use the constraint on M^T M as well. trace(M^T M) = E = 47. trace((M^T M)²) = ∑ d(c)² + ∑_{a≠b} t_{ab}² = 223 + ∑_{a≠b} t_{ab}² ≤ 223 + 352 = 575.

Since trace(G²) = trace((M^T M)²) (same eigenvalues), we get the same bound. No additional constraint.

I think the spectral approach won't give a better bound than 47 for this problem. Let me try to determine the answer by other means.

Let me think about whether 47 is achievable by trying to construct it explicitly.

We need 10 subsets of {1,...,10}, with sizes (5,5,5,5,5,5,5,4,4,4), pairwise intersections ≤ 2, and the dual condition (column degrees (5,5,5,5,5,5,5,4,4,4), pairwise column intersections ≤ 2).

This is equivalent to a bipartite graph that is almost a symmetric 2-(10,5,2) design (which doesn't exist).

Let me try to use the non-existence of the symmetric 2-(10,5,2) design to argue that 47 is impossible.

Hmm, but the non-existence of the design doesn't directly imply that 47 is impossible, since we're not requiring a full design.

Let me try a different approach. Let me think about the problem modulo 2 or using some parity argument.

Consider the 10×10 matrix M over GF(2). The condition s_{ij} ≤ 2 doesn't have a clean interpretation over GF(2).

Let me try thinking about it over the integers.

Actually, let me try to think about the problem using the following approach:

Consider the 3 rows of degree 4. Each has 4 columns. The total number of column-incidences from these 3 rows is 12. These 12 incidences are distributed among the 10 columns. By pigeonhole, some column has at least 2 incidences from these 3 rows, i.e., at least 2 of the 3 degree-4 rows share a column.

More specifically, the 3 degree-4 rows have 4 columns each, with pairwise intersections ≤ 2. The total number of distinct columns covered is at least 4 + 4 + 4 - 2 - 2 - 2 = 6 (by inclusion-exclusion, if all pairwise intersections are 2) and at most 12 (if all disjoint, but they can't be since there are only 10 columns).

If all three pairwise intersections are 2: |A ∪ B ∪ C| = 12 - 6 + |A ∩ B ∩ C|. If |A ∩ B ∩ C| = t, then |A ∪ B ∪ C| = 6 + t. For t = 0: 6 columns. For t = 1: 7 columns. Etc.

The 7 degree-5 rows have 5 columns each. Their columns are drawn from {1,...,10}. 

This is getting very complex. Let me try a different approach entirely.

Let me try to see if the answer is 40 by looking for a cleaner argument.

Wait, actually, I just realized something. Let me reconsider the problem. We've constructed 46, so the answer is at least 46. The upper bound is 47. So the answer is either 46 or 47.

Let me try to determine which one.

Let me try to prove that 47 is impossible.

Assume E = 47. Then both sides have degree sequence (5^7, 4^3). The sum ∑_{i<j} s_{ij} = 88, deficit 2 from 90.

Case analysis on the deficit:

Case A: One pair of rows has s = 0, all others have s = 2.
Case B: Two pairs of rows have s = 1, all others have s = 2.

Similarly for columns.

Let me focus on Case A for rows (one pair with s = 0). Say rows r1 and r2 share no columns. Then r1 and r2 together cover d(r1) + d(r2) columns. Since they share 0, this is d(r1) + d(r2) ≤ 10. If both have degree 5, 10 ≤ 10. ✓ If one has degree 5 and one has degree 4, 9 ≤ 10. ✓

Sub-case A1: r1 and r2 both have degree 5, share 0 columns. Together they cover all 10 columns. Every other row shares exactly 2 columns with r1 and 2 with r2 (since all other pairs have s = 2).

For any other row r (degree 4 or 5), r shares 2 columns with r1 and 2 with r2. Since r1 and r2 partition the columns, r's shared columns with r1 are 2 of r1's 5 columns, and r's shared columns with r2 are 2 of r2's 5 columns. So r has at least 4 columns (2 from r1's side and 2 from r2's side). If r has degree 4, then r's columns are exactly these 4 (2 from each side). If r has degree 5, r has one additional column.

Now, consider two degree-4 rows r3 and r4 (both sharing 2 with r1 and 2 with r2). They share 2 columns with each other (since all pairs except (r1,r2) have s = 2). r3's columns: 2 from r1's side (call this set A3) and 2 from r2's side (call this set B3). Similarly r4: A4 and B4.

r3 ∩ r4 = (A3 ∩ A4) ∪ (B3 ∩ B4). |r3 ∩ r4| = |A3 ∩ A4| + |B3 ∩ B4| = 2.

So |A3 ∩ A4| + |B3 ∩ B4| = 2, with |A3 ∩ A4| ≤ 2 and |B3 ∩ B4| ≤ 2.

Now, the column condition: any two columns share at most 2 rows. Let's think about the columns in r1's side (5 columns, each in r1 and in some other rows). Column c in r1's set: it's in r1 and in some of the other 9 rows. The degree of c is 4 or 5.

This is getting very complex. Let me try to use a computer to check if 47 is achievable. But the problem says not to use tools...

OK let me think about this more carefully. Let me try to consider the column condition in Case A.

In Case A (rows), we have rows r1, r2 of degree 5 partitioning the 10 columns into two sets of 5: C1 = cols of r1, C2 = cols of r2. Every other row has exactly 2 columns in C1 and 2 in C2 (if degree 4) or 2 in C1, 2 in C2, and 1 extra (if degree 5).

Wait, I said degree-4 rows have exactly 2 from each side. But a degree-5 row has 2 from C1, 2 from C2, and 1 more — but from which side? It must be from C1 or C2 (there are no other columns). So a degree-5 row has either 3 from C1 and 2 from C2, or 2 from C1 and 3 from C2.

But we said every other row shares exactly 2 with r1 and 2 with r2. Sharing 2 with r1 means 2 columns in C1. Sharing 2 with r2 means 2 columns in C2. So a degree-5 row has 2 in C1 and 2 in C2, plus 1 more. But the 1 more is in C1 or C2, making it 3 in one and 2 in the other. But then it shares 3 with r1 or 3 with r2, contradicting s = 2!

Wait, no. Sharing 2 with r1 means exactly 2 of the row's columns are in C1 (r1's columns). If the row has 3 columns in C1, it shares 3 with r1, which violates s ≤ 2.

So a degree-5 row can't have 3 columns in C1 or C2. It must have exactly 2 in C1 and 2 in C2, totaling 4. But it has degree 5, so it needs a 5th column. But all columns are in C1 ∪ C2, so the 5th column is in C1 or C2, making it 3 in one side. Contradiction!

So in Case A (where r1 and r2 both have degree 5 and share 0 columns), no other row can have degree 5! But we need 7 rows of degree 5 (including r1 and r2), so 5 more rows of degree 5. Contradiction!

So Case A with r1, r2 both degree 5 is impossible.

Sub-case A2: r1 has degree 5, r2 has degree 4 (or vice versa), share 0 columns. Together they cover 9 columns. One column is in neither.

Every other row shares 2 with r1 and 2 with r2. A degree-5 row: 2 in C1 (r1's 5 columns), 2 in C2 (r2's 4 columns), and 1 more. The 1 more can be in C1, C2, or the uncovered column. If in C1, shares 3 with r1 → contradiction. If in C2, shares 3 with r2 → contradiction. If the uncovered column, then 2 in C1, 2 in C2, 1 uncovered = 5. ✓

So degree-5 rows must include the uncovered column. How many degree-5 rows are there? We need 7 total (including r1). r2 has degree 4. So 7 degree-5 rows: r1 and 6 others. The 6 others all include the uncovered column.

The 3 degree-4 rows: r2 and 2 others. The 2 other degree-4 rows have 2 in C1 and 2 in C2 (total 4, no uncovered column).

Now, the 6 degree-5 rows (other than r1) all include the uncovered column, call it c*. So c* is in 6 rows (these 6) plus possibly r1 (no, r1 doesn't include c* since c* is uncovered by r1 and r2). So d(c*) = 6.

But column degrees must be 4 or 5 (degree sequence 5^7, 4^3). d(c*) = 6 > 5. Contradiction!

So Sub-case A2 is also impossible.

Sub-case A3: r1 and r2 both have degree 4, share 0 columns. Together they cover 8 columns. 2 columns uncovered.

Every other row shares 2 with r1 and 2 with r2. Degree-5 rows: 2 in C1 (r1's 4 columns), 2 in C2 (r2's 4 columns), 1 more. The 1 more is in C1, C2, or the 2 uncovered columns. If in C1 or C2, contradiction (shares 3). So the 5th column is one of the 2 uncovered columns.

All 7 degree-5 rows include one of the 2 uncovered columns. The 2 uncovered columns have degree = number of degree-5 rows that include them = 7 (since all 7 degree-5 rows include one of them). But each uncovered column can be in at most 7 rows, and the total is 7. So either one uncovered column is in all 7 and the other in 0, or they split somehow.

But d(c) ≤ 5 (column degree sequence is 5^7, 4^3). So d(c) ≤ 5 for any column. But the uncovered columns have degree 7 (or some split summing to 7). 7 > 5. Contradiction!

So Case A (one pair with s = 0) is entirely impossible!

Therefore, in any 47-edge configuration, we must be in Case B: two pairs of rows have s = 1, all others have s = 2.

By symmetry, the same holds for columns: two pairs of columns have t = 1, all others have t = 2.

Now let me analyze Case B. Two pairs of rows share exactly 1 column, all other pairs share exactly 2.

Let the two pairs be (r1, r2) and (r3, r4) (possibly overlapping). 

Sub-case B1: The two pairs are disjoint: (r1, r2) and (r3, r4), with {r1,r2} ∩ {r3,r4} = ∅.

Sub-case B2: The two pairs share a row: (r1, r2) and (r1, r3) (or similar).

Sub-case B3: The two pairs are the same: (r1, r2) and (r1, r2). But that's just one pair with s = 1, giving deficit 1, not 2. So this doesn't work. (We need deficit 2.)

Wait, actually, I need to be more careful. The deficit is 2, and each pair with s = 1 contributes deficit 1 (from the max of 2). So we need exactly 2 pairs with s = 1. These could be:
- Two disjoint pairs
- Two pairs sharing one row (like (r1,r2) and (r1,r3))
- Two pairs sharing both rows (same pair, but that's only 1 pair)

So Sub-case B1 or B2.

Let me analyze Sub-case B2: pairs (r1, r2) and (r1, r3) have s = 1, all others s = 2.

Row r1 shares 1 column with r2 and 1 with r3, and 2 with each of r4, ..., r10. Total sharing for r1: 1 + 1 + 7·2 = 16. 

But also, total sharing for r1 = ∑_{c ∈ r1} (d(c) - 1). If r1 has degree d(r1), this is ∑_{c ∈ r1} d(c) - d(r1).

If r1 has degree 5: ∑_{c ∈ r1} d(c) - 5 = 16, so ∑_{c ∈ r1} d(c) = 21. The 5 columns of r1 have degrees summing to 21. Since degrees are 4 or 5: if k columns have degree 5 and 5-k have degree 4, sum = 5k + 4(5-k) = k + 20 = 21, so k = 1. So r1 is connected to 1 column of degree 5 and 4 columns of degree 4.

If r1 has degree 4: ∑_{c ∈ r1} d(c) - 4 = 16, so ∑_{c ∈ r1} d(c) = 20. 4 columns with degrees summing to 20: k + 16 = 20 (if k have degree 5 and 4-k have degree 4), k = 4. So all 4 columns of r1 have degree 5.

Hmm, this is getting complex but let me continue.

Let me also compute the sharing for r2. r2 shares 1 with r1 and 2 with each of r3, ..., r10. Total: 1 + 8·2 = 17.

If r2 has degree 5: ∑_{c ∈ r2} d(c) = 17 + 5 = 22. k + 20 = 22, k = 2. So 2 columns of degree 5, 3 of degree 4.

If r2 has degree 4: ∑_{c ∈ r2} d(c) = 17 + 4 = 21. k + 16 = 21, k = 5. But k ≤ 4, contradiction. So r2 can't have degree 4.

So r2 must have degree 5. Similarly r3 must have degree 5 (by symmetry with r2).

Now, r1: if degree 5, connected to 1 column of degree 5 and 4 of degree 4. If degree 4, connected to 4 columns all of degree 5.

Let me consider both sub-cases for r1's degree.

Sub-case B2a: r1 has degree 5. Then r1 is connected to 1 degree-5 column and 4 degree-4 columns. But there are only 3 degree-4 columns total, and r1 is connected to 4 of them. Contradiction! (4 > 3)

Sub-case B2b: r1 has degree 4. Then r1 is connected to 4 columns all of degree 5. There are 7 degree-5 columns, so this is possible.

So r1 has degree 4, connected to 4 of the 7 degree-5 columns. r2 and r3 have degree 5.

Now, r2 (degree 5) is connected to 2 degree-5 columns and 3 degree-4 columns. But there are only 3 degree-4 columns, so r2 is connected to all 3 degree-4 columns and 2 degree-5 columns.

Similarly, r3 (degree 5) is connected to all 3 degree-4 columns and 2 degree-5 columns.

Now, r1 and r2 share 1 column. r1 is connected to 4 degree-5 columns (call them a subset S1 of the 7 degree-5 columns, |S1| = 4). r2 is connected to 3 degree-4 columns (all of them) and 2 degree-5 columns (subset S2, |S2| = 2). The shared columns of r1 and r2 are in S1 ∩ S2 (since r1 only connects to degree-5 columns, and r2's degree-5 columns are S2). |S1 ∩ S2| = 1 (since s(r1,r2) = 1).

Similarly, r1 and r3 share 1 column: |S1 ∩ S3| = 1 where S3 is r3's degree-5 columns (|S3| = 2).

r2 and r3 share 2 columns (since (r2,r3) is not one of the deficient pairs). r2's columns: 3 degree-4 + S2. r3's columns: 3 degree-4 + S3. Shared: 3 (all degree-4 columns) + |S2 ∩ S3|. So 3 + |S2 ∩ S3| = 2. But 3 + |S2 ∩ S3| ≥ 3 > 2. Contradiction!

So Sub-case B2 is impossible!

Now let me check Sub-case B1: two disjoint pairs (r1, r2) and (r3, r4) with s = 1, all others s = 2.

Total sharing for r1: 1 (with r2) + 1 (with r3? no, s(r1,r3) = 2) + ... Let me recompute. r1 shares 1 with r2, 2 with r3, 2 with r4, and 2 with each of r5,...,r10. Total: 1 + 2 + 2 + 6·2 = 17.

If r1 has degree 5: ∑_{c ∈ r1} d(c) = 17 + 5 = 22. k + 20 = 22, k = 2. So 2 degree-5 columns, 3 degree-4 columns.

If r1 has degree 4: ∑_{c ∈ r1} d(c) = 17 + 4 = 21. k + 16 = 21, k = 5 > 4. Contradiction. So r1 has degree 5.

By symmetry, r2, r3, r4 all have degree 5 (same calculation).

So r1, r2, r3, r4 all have degree 5, each connected to 2 degree-5 columns and 3 degree-4 columns.

The 3 degree-4 columns: each of r1, r2, r3, r4 is connected to all 3 (since they need 3 degree-4 columns and there are exactly 3). So all 4 of these rows are connected to all 3 degree-4 columns.

Now, r1 and r2 share 1 column. They share all 3 degree-4 columns (since both are connected to all 3). So they share at least 3 columns. But s(r1, r2) = 1. Contradiction! (3 > 1)

So Sub-case B1 is also impossible!

Therefore, Case B is entirely impossible, and since Case A is also impossible, E = 47 is impossible!

Wait, let me double-check. In Sub-case B1, I concluded that r1, r2, r3, r4 all have degree 5 and each is connected to all 3 degree-4 columns. Then r1 and r2 share at least 3 columns (the 3 degree-4 columns), but we need s(r1, r2) = 1. Contradiction. ✓

And in Sub-case B2, I got a contradiction from r2 and r3 sharing at least 3 columns (the 3 degree-4 columns) when they should share 2. ✓

And in Case A, all sub-cases led to contradictions. ✓

So E = 47 is impossible, and the maximum is at most 46.

We've constructed a configuration with 46 edges (from the 2-(11, 5, 2) design). So the answer is 46.

Wait, let me double-check the construction more carefully.

The 2-(11, 5, 2) design: This is a symmetric balanced incomplete block design with parameters (v, b, r, k, λ) = (11, 11, 5, 5, 2). It exists (it's the complement of the 2-(11, 6, 3) design, which comes from a Hadamard matrix of order 12).

Properties:
- 11 points, 11 blocks.
- Each block has 5 points.
- Each point is in 5 blocks.
- Any two distinct points are in exactly 2 common blocks.
- Any two distinct blocks intersect in exactly 2 points.

Construction: Remove point p and block B where p ∈ B. 

After removal:
- 10 points (all except p), 10 blocks (all except B).
- Blocks that contained p: these now have 4 points (lost p). There are 5 such blocks (since p is in 5 blocks), but one of them is B (removed). So 4 blocks of size 4.
- Blocks that didn't contain p: these still have 5 points. There are 6 such blocks. So 6 blocks of size 5.
- Total edges: 4·4 + 6·5 = 16 + 30 = 46. ✓

Row (block) intersections:
- Two blocks that both contained p: originally intersected in 2 points. One intersection point was p (since both contained p). After removing p, they intersect in 1 point. ✓ (≤ 2)
- Two blocks that both didn't contain p: originally intersected in 2 points, neither was p. Still 2. ✓
- One block that contained p, one that didn't: originally intersected in 2 points. The one that didn't contain p doesn't have p, so p is not in the intersection. Still 2. ✓

Column (point) intersections:
- Two points q, r ≠ p: originally in 2 common blocks. We removed block B. If B contained both q and r, they now share 1 block. Otherwise, still 2. B contained p and 4 other points. So for two of those 4 points, B was a common block, and they now share 1 block. For all other pairs, still 2. ✓ (≤ 2)

So the construction is valid, and 46 is achievable.

Combined with the proof that 47 is impossible, the answer is 46.

Let me also verify that the 2-(11, 5, 2) design exists. A Hadamard matrix of order 12 exists (Paley's construction using GF(11)). From a Hadamard matrix of order 4n, we get a 2-(4n-1, 2n-1, n-1) design. For n = 3: 2-(11, 5, 2). ✓

So the answer is n = 46.

Let me now write up the proof cleanly.

Actually, wait. Let me re-examine the proof that 47 is impossible more carefully, because I want to make sure I haven't made an error.

For E = 47, both sides have degree sequence (5^7, 4^3) (7 vertices of degree 5, 3 of degree 4). The sum ∑_{i<j} s_{ij} = ∑_c C(d(c), 2) = 7·C(5,2) + 3·C(4,2) = 7·10 + 3·6 = 88. With 45 pairs and max s = 2, the max possible sum is 90. Deficit = 2.

Case A: One pair has s = 0, rest have s = 2. (Deficit = 2 from one pair.)

I showed all sub-cases lead to contradiction. Let me re-verify Sub-case A1 (both degree 5, share 0).

r1, r2 degree 5, share 0 columns. Together cover 10 columns (5+5=10, no overlap). Every other row shares exactly 2 with r1 and 2 with r2 (since all other pairs have s=2).

A degree-5 row r: shares 2 with r1 (2 columns in C1) and 2 with r2 (2 columns in C2). Total: 4 columns. Needs 1 more. The 5th column is in C1 or C2 (no other columns exist). If in C1, shares 3 with r1. If in C2, shares 3 with r2. Both contradict s = 2. ✓ Contradiction.

Sub-case A2: r1 degree 5, r2 degree 4, share 0. Cover 9 columns, 1 uncovered.

Degree-5 row r: 2 in C1, 2 in C2, 1 more. If in C1 or C2, contradiction. So 5th column is the uncovered one c*. All 7 degree-5 rows (r1 and 6 others) — wait, r1 is degree 5 but doesn't include c* (c* is uncovered by both r1 and r2). So the 6 other degree-5 rows include c*. d(c*) = 6. But max degree is 5. Contradiction. ✓

Sub-case A3: r1, r2 both degree 4, share 0. Cover 8 columns, 2 uncovered.

Degree-5 rows: 2 in C1, 2 in C2, 1 more in uncovered set. 7 degree-5 rows, each picks one of 2 uncovered columns. Total incidences to uncovered columns = 7. But max degree is 5, so each uncovered column has degree ≤ 5. Two columns can absorb at most 10, so 7 ≤ 10 is fine... 

Wait, I need to reconsider. The uncovered columns have degree from the degree-5 rows (7 of them, each contributing 1) plus from the degree-4 rows (r1 and r2 don't include them, and the third degree-4 row might or might not).

Actually, let me redo this. The 2 uncovered columns: they're not in r1 or r2. The other 8 rows (7 degree-5 + 1 degree-4, since r1 and r2 are 2 of the 3 degree-4 rows) might include them.

The 7 degree-5 rows each include 1 uncovered column. The 1 remaining degree-4 row: it shares 2 with r1 and 2 with r2, so it has 2 in C1 and 2 in C2, total 4. It doesn't include any uncovered column.

So the 2 uncovered columns have degree 7 total (from the 7 degree-5 rows). Each has degree ≤ 5. So the split is at most 5 + 2 = 7 or 4 + 3 = 7, etc. But we need each ≤ 5, so the split is (5, 2), (4, 3), (3, 4), (2, 5). All have both ≤ 5. ✓

Hmm wait, so Sub-case A3 might not lead to a contradiction as easily. Let me re-examine.

Actually, I made an error earlier. Let me redo Sub-case A3.

r1, r2 degree 4, share 0 columns. C1 = r1's 4 columns, C2 = r2's 4 columns. |C1| = 4, |C2| = 4, C1 ∩ C2 = ∅. Uncovered: 2 columns, call them u1, u2.

The third degree-4 row, call it r3: shares 2 with r1, 2 with r2, 2 with each of the 7 degree-5 rows. r3 has 2 columns in C1 and 2 in C2 (total 4, no uncovered columns).

The 7 degree-5 rows: each has 2 in C1, 2 in C2, and 1 in {u1, u2}.

Now, column degrees. The 3 degree-4 columns: where are they? The column degree sequence is (5^7, 4^3). Let me figure out which columns have degree 4.

Columns in C1 (4 columns): each is in r1 (degree-4 row) and in some of the 7 degree-5 rows (those that have this column in their C1-portion) and possibly r3. 

Each degree-5 row has 2 columns in C1. Total C1-incidences from degree-5 rows: 7·2 = 14. These are distributed among 4 columns in C1. Also, r1 contributes 4 (one to each C1 column) and r3 contributes 2 (to 2 of the 4 C1 columns).

So total C1-incidences = 14 + 4 + 2 = 20. Average degree of C1 columns = 20/4 = 5.

Similarly, C2-incidences = 14 + 4 + 2 = 20. Average degree of C2 columns = 5.

Uncovered columns: 7 incidences from degree-5 rows. Average = 3.5.

Total edges = 20 + 20 + 7 = 47. ✓

Now, the column degree sequence must be (5^7, 4^3). The C1 columns have average degree 5, C2 columns average 5, uncovered average 3.5.

For the 3 degree-4 columns: they must be among the columns with degree 4. The uncovered columns have degree summing to 7, so possible splits: (4,3), (3,4), (5,2), (2,5). If split is (4,3): one uncovered column has degree 4, the other 3. Then we need 2 more degree-4 columns from C1 ∪ C2. The C1 and C2 columns have degrees summing to 20 each, with 4 columns each. If 2 columns have degree 4, the other 6 (in C1 ∪ C2) have degree 5, and the degrees sum: 2·4 + 6·5 + 4 + 3 = 8 + 30 + 7 = 45 ≠ 47. 

Hmm, let me recompute. Total column degrees = 47. Degree sequence (5^7, 4^3): 7·5 + 3·4 = 35 + 12 = 47. ✓

C1 columns: 4 columns, degrees summing to 20. If a of them have degree 5 and 4-a have degree 4: 5a + 4(4-a) = a + 16 = 20, so a = 4. All C1 columns have degree 5.

Similarly, all C2 columns have degree 5.

Uncovered columns: 2 columns, degrees summing to 7. If both have degree 4: sum = 8 ≠ 7. If one 4 and one 3: sum = 7. ✓ But degree 3 is not in our degree sequence (5^7, 4^3). ✗

If one 5 and one 2: sum = 7. Degree 2 not in sequence. ✗

So the uncovered columns must have degrees summing to 7, but the allowed degrees are 4 and 5. 4 + 5 = 9 ≠ 7, 4 + 4 = 8 ≠ 7, 5 + 5 = 10 ≠ 7. None work! Contradiction! ✓

So Sub-case A3 is also impossible. 

So Case A is entirely impossible, and Case B is entirely impossible (as shown above). Therefore E = 47 is impossible.

Since we have a construction with 46 edges, the answer is 46.

Let me also verify the Case B analysis once more.

Case B: Two pairs have s = 1, rest have s = 2. Deficit = 2.

Sub-case B1: Disjoint pairs (r1,r2) and (r3,r4).

Each of r1, r2, r3, r4 has total sharing 17 (1 + 2·8 = 17). 

If degree 5: ∑_{c ∈ r} d(c) = 22, so 2 degree-5 columns and 3 degree-4 columns.
If degree 4: ∑_{c ∈ r} d(c) = 21, so 5 degree-5 columns out of 4 — impossible.

So all four have degree 5, each connected to 2 degree-5 and 3 degree-4 columns. Since there are exactly 3 degree-4 columns, each of r1,...,r4 is connected to all 3 degree-4 columns.

r1 and r2 share at least the 3 degree-4 columns, so s(r1,r2) ≥ 3. But s(r1,r2) = 1. Contradiction. ✓

Sub-case B2: Pairs (r1,r2) and (r1,r3).

r1: sharing = 1 + 1 + 7·2 = 16. 
If degree 5: ∑ d(c) = 21, 1 degree-5 + 4 degree-4. But only 3 degree-4 columns. Contradiction.
If degree 4: ∑ d(c) = 20, 4 degree-5 + 0 degree-4. All 4 columns of r1 are degree-5. ✓

r2: sharing = 1 + 2·8 = 17.
If degree 5: 2 degree-5 + 3 degree-4. ✓ (connected to all 3 degree-4 columns)
If degree 4: impossible (as before).

So r2 degree 5, connected to all 3 degree-4 columns + 2 degree-5 columns.
Similarly r3 degree 5, connected to all 3 degree-4 columns + 2 degree-5 columns.

r2 and r3 share: 3 (degree-4 columns) + |S2 ∩ S3| where S2, S3 are their degree-5 column sets. So s(r2,r3) = 3 + |S2 ∩ S3| ≥ 3. But s(r2,r3) = 2 (not a deficient pair). Contradiction. ✓

Great, so the proof is complete. The answer is 46.

Now let me also think about whether there might be other cases I'm missing. The deficit is 2, and the possible distributions are:
- One pair with s = 0 (deficit 2): Case A
- Two pairs with s = 1 (deficit 1 each): Case B

Are there other possibilities? What about one pair with s = 0 and one with s = 1? That's deficit 3, too much. One pair with s = 1: deficit 1, not enough. Three pairs with s = 1: deficit 3, too much. So only Cases A and B. ✓

I'm now confident the answer is 46. Let me write up the proof.

Actually, let me reconsider one thing. In Case A, I assumed the pair with s = 0 involves specific degree combinations. Let me make sure I covered all cases.

Case A: one pair (r1, r2) with s(r1, r2) = 0, all others s = 2.

The degrees of r1 and r2 can be (5,5), (5,4), or (4,4). (Can't be (4,5) as it's the same as (5,4) by relabeling.)

- (5,5): Sub-case A1. Both degree 5, cover 10 columns. Other
