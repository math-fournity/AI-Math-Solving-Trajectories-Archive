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
  <problem_id>polymath_00626</problem_id>
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

In a country with $2015$ cities there is exactly one two-way flight between each pair of cities. The three flights between any three cities belong to at most two different airline companies. No matter how the flights are shared among any number of companies, if it is guaranteed that there always exists at least one city in which at least $k$ flights belong to the same airline, what is the maximum possible value of $k$?

## Standard Solution

According to the solution, for a general number of cities $n$, the maximum value of $k$ is given by $\lceil 2n/5 \rceil$. The condition "no rainbow triangles" (at most two companies for any three cities) leads to a structure that can be analyzed using Gallai colorings. The optimal configuration for $n=2015$ gives $k = \lceil \frac{2 \times 2015}{5} \rceil = \lceil 806 \rceil = 806$.

## AI's Thinking (Attempted Solution Process)

The problem: 2015 cities, complete graph K_2015, edges colored by airlines. Condition: for any three cities, the three edges between them use at most 2 colors (no rainbow triangle). Find the maximum k such that no matter how the coloring (satisfying the condition) is done, there always exists a city with at least k flights of the same airline.

This is a Gallai coloring problem (no rainbow triangle). 

Gallai's theorem: In a Gallai coloring (no rainbow triangle) of K_n, there exists a vertex with at least... actually the structure theorem says the vertices can be partitioned into nonempty sets such that between parts only two colors are used, and within each part recursively.

We want the maximum k guaranteed. So we need to find the minimum over all Gallai colorings of K_2015 of the maximum monochromatic degree at a vertex.

Actually we want: over all Gallai colorings, the minimum value of (max over vertices of max monochromatic degree at that vertex). And k is this minimum. So k = min over colorings of max over v of max over colors c of deg_c(v).

Let me think. This is a known competition problem. Let me think about the answer.

For Gallai colorings of K_n, there's a result that there's always a vertex with monochromatic degree at least... Let me think about the extremal construction.

Gallai partition: partition vertices into parts V_1, ..., V_m where between parts only 2 colors used, and the reduced graph (on parts) is 2-colored. Recursively within each part.

To minimize the maximum monochromatic degree, we want to balance.

Let me think about small cases and find a pattern.

Claim: the answer is $\lceil (n-1)/2 \rceil$? No, that's for general 2-colorings (pigeonhole). But here we can use more colors, so we might be able to do better (smaller max monochromatic degree). Wait, we want the guaranteed lower bound, so more colors could reduce the max monochromatic degree, making k smaller. But the Gallai condition restricts.

Actually with Gallai coloring we can use many colors. The question is what's the minimum possible max monochromatic degree.

Let me think recursively. Let f(n) = min over Gallai colorings of K_n of max_v max_c deg_c(v).

Hmm, but actually the problem asks for the maximum k that is guaranteed. So k = f(2015) where f(n) is the min over colorings of the max monochromatic degree.

Gallai partition structure: We partition into m parts. Between parts, 2 colors (say red, blue). Within each part, Gallai coloring recursively. The reduced graph on m parts is a 2-coloring of K_m (complete graph on parts, each edge red or blue) — wait, is it? Between parts only 2 colors, and each pair of parts has all edges the same color? Let me recall: In Gallai's theorem, the partition has the property that between any two parts, all edges have the same color, and only two colors are used between parts. Yes.

So the reduced graph is a 2-coloring of K_m. By Ramsey/pigeonhole, in any 2-coloring of K_m there's a vertex (part) with monochromatic degree ≥ ⌈(m-1)/2⌉.

For a vertex v in part V_i: its monochromatic degree in color red = (red degree of part i in reduced graph) × |V_j| summed... no wait, v connects to all vertices in other parts. The color of edge v-w where w in V_j is the color of the reduced edge (i,j). So deg_red(v) = sum over parts j with reduced edge red of |V_j|. Similarly for blue. Plus within V_i, v has some monochromatic degrees from the recursive coloring.

So to minimize, we want to balance sizes and use the recursive structure.

Let me think about the extremal construction to find f(n).

Construction idea: Use a balanced binary tree / recursive halving. Partition into 2 parts of size ~n/2, color between them one color (say red). Then recursively color each part. 

If we partition into 2 parts of sizes a and b (a+b=n), all edges between them red. Then a vertex in part 1 has red degree ≥ b (from cross edges) plus red degree within part 1. To minimize max monochromatic degree, we'd want b small but then part 1 is large and recursion...

Hmm, let me think differently. Let's consider partitioning into m equal parts of size n/m, with the reduced graph being a balanced 2-coloring where each part has red degree and blue degree ~ (m-1)/2.

For a vertex in part i: red degree ≈ ((m-1)/2) × (n/m) = (m-1)/(2m) × n ≈ n/2 (for large m). That's bad — approaches n/2.

So using many parts with 2 colors gives ~n/2 which is the pigeonhole bound. To do better we need fewer parts but then recursion within parts.

Let me think: partition into 2 parts of size n/2, one color between. Vertex in part 1: red degree = n/2 (cross) + (red degree within part 1). The within part 1 contributes recursively. So max monochromatic degree ≥ n/2. That's worse.

Hmm. So 2 parts gives n/2. Many parts gives ~n/2. 

What about the recursion helping? Let's think: partition into m parts, reduced graph 2-colored. For vertex in part i, cross monochromatic degree in dominant color ≥ (something). If parts are equal size s = n/m, and reduced graph is balanced (each part has red degree, blue degree ≈ (m-1)/2), then cross dominant degree ≈ ((m-1)/2) s. Plus within-part contribution f(s).

Total dominant ≥ max( ((m-1)/2) s, f(s) ) roughly, but actually it's cross + within for the same color. The cross color and within color might differ. If the dominant cross color for part i is red, then red degree = cross_red + within_red. within_red ≤ f(s) (well, the max monochromatic within is ≤ f(s) by definition of f being the min... no, f(s) is the min over colorings, so within part we can achieve max monochromatic = f(s), but the dominant color within might not be red).

This is getting complicated. Let me look at it as: we want to find f(n) = min max monochromatic degree.

Let me conjecture f(n) = ⌈log2(n)⌉ or something? No...

Actually let me think about a clean construction. Consider the "complete binary tree" / "lexicographic" Gallai coloring.

Construction: Take n = 2^t. Partition into 2 halves of size 2^{t-1}, color cross edges color 1. Recursively each half: partition into 2, color cross edges color 2. Etc. At level t, single vertices.

For a vertex, at each level it's in a group; the cross edges at that level (to the sibling group) all have one color. The sizes of sibling groups: 2^{t-1}, 2^{t-2}, ..., 1. So the monochromatic degrees are 2^{t-1}, 2^{t-2}, ..., 1, each in a different color. Max = 2^{t-1} = n/2. Bad.

So that gives n/2.

Hmm, so maybe the answer is around n/2? But we can use more colors cleverly.

Wait, let me reconsider. The condition is "at most two different airline companies" for any triangle. This is exactly Gallai coloring (no rainbow triangle). 

Let me reconsider the question: we want the maximum k guaranteed. So we want the minimum over all Gallai colorings of the maximum monochromatic degree.

Let me think about whether we can get below n/2.

Consider n=3. K_3, no rainbow triangle means at most 2 colors. Max monochromatic degree: if 2 edges same color, the middle vertex has degree 2 in that color. So max monochromatic degree = 2. f(3) = 2. ⌈(3-1)/2⌉ = 1, but actual is 2. Hmm wait, can we do better? With 3 vertices and at most 2 colors, by pigeonhole two edges share a color, and they share a vertex (any two edges of a triangle share a vertex), so that vertex has monochromatic degree 2. So f(3) = 2 = n-1.

n=4: K_4 Gallai coloring. Can we get max monochromatic degree = 2? Partition into 2+2, cross edges one color (say red). Each vertex has red degree 2 (cross) + within. Within each pair, 1 edge, some color. So red degree = 2, and the within edge gives degree 1 in another color. Max monochromatic = 2. Can we do max = 1? No, since total degree 3, by pigeonhole (with however many colors) ... actually with many colors we could have all 3 edges different colors at a vertex, but Gallai forbids rainbow triangles. For n=4, can every vertex have all edges distinct colors? That would mean a rainbow K_4 which has rainbow triangles. Not allowed. 

Can we achieve max monochromatic degree 2 for n=4? Yes (the 2+2 construction). Can we achieve 1? Need every vertex's 3 edges all different colors → rainbow K_4 → contains rainbow triangle. Impossible. So f(4) = 2.

n=5: Let's see. Partition 2+3? Cross red. Part of size 2: red degree 3 (cross) + within. So max ≥ 3. Bad. Partition into more parts? 

Let me think: partition into 5 parts of size 1? Then reduced graph is K_5 2-colored (Gallai on the parts... wait the parts are singletons so the whole thing is a 2-coloring of K_5). Max monochromatic degree ≥ ⌈4/2⌉ = 2. So f(5) ≤ 2? But wait, is a 2-coloring of K_5 a valid Gallai coloring? Yes (only 2 colors, no rainbow triangle). Max monochromatic degree in a balanced 2-coloring of K_5: each vertex degree 4, split 2-2, so max = 2. So f(5) ≤ 2.

Can f(5) = 1? No (rainbow K_5 impossible). So f(5) = 2.

n=6: 2-coloring of K_6 balanced: degree 5, split ⌈5/2⌉=3. So max ≥ 3. But maybe Gallai with more colors does better. Partition into 3 parts of size 2, reduced graph K_3 2-colored (say all red, or 2 red 1 blue). If reduced K_3 all red: each vertex cross red degree = 4, plus within. Max ≥ 4. Bad. If reduced K_3 is 2 red 1 blue (a path): part 1 (middle) has red degree 2 parts = 4 vertices red, blue degree 1 part = 2. Part 2 (end) red degree 1 part = 2, blue degree 1 part = 2. So vertex in part 2: red degree 2 + within(1) , blue degree 2 + within(0). Max = 3 (if within red). Hmm.

Alternatively partition into 6 singletons with 2-coloring: max = 3. 

Can we do f(6) = 2? Let's try partition into 2 parts of 3, cross red. Vertex: red degree 3 (cross) + within. Within K_3 Gallai, max monochromatic = 2. If within dominant color is red, red degree = 3+2 = 5. If within dominant is another color, red = 3, other = 2. Max = 3. So f(6) ≤ 3 via this. 

Hmm what about partition 3 parts of size 2 with reduced graph a 2-coloring of K_3 that's a "Gallai" — but K_3 2-colored always Gallai. Best balanced: 2 red, 1 blue. Computed above max = 3. 

What about more colors: partition into parts of sizes... Let me try to get max = 2 for n=6. Need every vertex monochromatic degree ≤ 2. Total degree 5, so need at least 3 colors per vertex on average. With Gallai... 

Try: 3 parts of size 2. Reduced graph K_3 with colors: edge(1,2)=red, edge(1,3)=blue, edge(2,3)=green? But reduced graph must use at most 2 colors! Gallai partition requires only 2 colors between parts. So reduced graph is 2-colored. So at most 2 colors between parts. So with 3 parts, the 3 reduced edges use ≤2 colors, meaning two edges share a color, and they share a part (vertex of reduced graph), so that part has monochromatic reduced degree 2, meaning vertices in it have cross monochromatic degree 2×2 = 4. Bad.

So 3 parts of size 2 → some part has cross monochromatic degree ≥ 4. Worse.

So for n=6, best seems 3 (from 2-coloring of K_6 or 2+2+2 with balanced reduced... no that gave 4). Let me reconsider: 2-coloring of K_6 gives max monochromatic degree 3 (balanced: 3-2 split, max 3). The 2+2+2 gave 4. The 3+3 gave 3. So f(6) = 3? Can we do 2?

Let me think if f(6)=2 is possible. Suppose max monochromatic degree ≤ 2. Consider Gallai partition into m parts. If m=1, it's all within, recurse—doesn't help base. The top-level partition has m≥2 parts with 2 colors between.

Case m=2: parts A, B sizes a, b, a+b=6, cross one color. Vertex in A has that color degree ≥ b. For ≤2, need b ≤ 2, so b ≤ 2 and a ≥ 4. Then within A (size ≥4) must have max monochromatic ≤ 2, but f(4)=2, ok possibly. And vertex in B has cross degree a ≥ 4 > 2. Contradiction. So m=2 impossible.

Case m≥3: reduced graph K_m 2-colored. Some part has monochromatic reduced degree ≥ ⌈(m-1)/2⌉. Cross monochromatic degree for vertices in that part ≥ ⌈(m-1)/2⌉ × (min part size). If all parts size 1 (m=6): reduced K_6 2-colored, max monochromatic reduced degree ≥ 3 > 2. If some part size ≥2: then m ≤ 5, ⌈(m-1)/2⌉ ≥ 2, times min part size ≥1, but the part with high reduced degree—its vertices have cross degree ≥ ⌈(m-1)/2⌉ × (size of neighbor parts). Hmm, need to be careful: cross monochromatic degree = sum of sizes of parts connected in that color. 

If m=3, sizes (2,2,2): reduced K_3, two edges same color sharing a part, that part has cross monochromatic degree 4. If sizes (3,2,1) or (4,1,1): the part with 2 same-color neighbors... Let's say parts P1,P2,P3 with edges P1P2 and P1P3 red (P2P3 blue). Vertices in P1 have red degree |P2|+|P3| = 6-|P1|. For ≤2 need |P1|≥4. Then |P2|+|P3| ≤ 2. Vertices in P2: red degree |P1| ≥ 4 >2. Contradiction.

m=4: sizes sum 6, so some part size 1, others... reduced K_4 2-colored. Max monochromatic reduced degree ≥ 2 (since degree 3, split ≥2). The part with reduced monochromatic degree 2: cross degree ≥ 2 × (min neighbor size). If that part is size 1 and neighbors size ≥1 each, cross ≥ 2. Could be exactly 2 if neighbors size 1. But then total size = 1+1+1+... Let me try sizes (2,2,1,1) or (3,1,1,1). 

(3,1,1,1): reduced K_4 2-colored. The part of size 3: its 3 reduced edges, by pigeonhole ≥2 same color, cross degree ≥ 2×1 = 2. Parts of size 1: reduced degree 3, ≥2 same color, cross ≥ 2×(neighbor sizes). If two same-color neighbors include the size-3 part, cross ≥ 3 > 2. To avoid, the size-1 part's same-color neighbors must both be size-1. So each size-1 part has its 2 same-color neighbors among the other size-1 parts. But there are 3 size-1 parts; can we 2-color K_4 on {Big, s1, s2, s3} so that each si has its majority color only to other sj's? si has degree 3 (to Big, and two other sj). For si's majority (≥2) to avoid Big, both other sj must be same color, and Big different. So edges si-sj all same color (say blue) for the triangle s1s2s3, and edges si-Big all red. Then si has blue degree 2 (to s2,s3) and red degree 1 (to Big). Cross blue degree = 1+1 = 2. Good. Big has red degree 3 (to s1,s2,s3), cross red degree = 3 > 2. Contradiction (Big has cross red degree 3).

So m=4 with (3,1,1,1) fails. (2,2,1,1): total 6. reduced K_4. Parts A,B size 2, C,D size 1. Need all cross monochromatic degrees ≤2. Vertex in A: cross degree = sum of sizes of same-color neighbors. A's reduced degree 3. If A has 2 same-color neighbors including a size-2 part, cross ≥ 2+1=3 or 2+2=4. To keep ≤2, A's 2 same-color neighbors must both be size 1 (C,D), and B different color. So edges A-C, A-D same color (blue), A-B red. Similarly B-C, B-D blue, B-A red (consistent). Then C has blue degree 2 (A,B) cross = 2+2 = 4 > 2. Contradiction.

So m=4 fails. m=5: sizes (2,1,1,1,1). reduced K_5 2-colored, max monochromatic reduced degree ≥ 2. The size-2 part: reduced degree 4, ≥2 same color. If those 2 neighbors both size 1, cross = 2. The size-1 parts: reduced degree 4, ≥2 same color, cross ≥ 2×1 = 2, but if a same-color neighbor is the size-2 part, cross ≥ 2+1=3. So each size-1 part's ≥2 same-color neighbors must all be size-1. There are 4 size-1 parts forming K_4 among themselves plus edges to Big. Each size-1 part has 4 reduced edges (3 to other size-1, 1 to Big). For majority to avoid Big: ≥2 of the 3 edges to other size-1 parts same color, and Big can be anything but if Big is same color as majority then... we need the 2+ same-color neighbors to not include Big, OR if Big included then total still ≤2 meaning only Big + one other = cross 2+1=3 >2. So Big must not be in the majority color, OR Big is minority. 

Let me just say: it seems hard to get f(6)=2. Let me conjecture f(6)=3.

Pattern: f(3)=2, f(4)=2, f(5)=2, f(6)=3.

Hmm, let me compute f(n) = ⌈(n-1)/2⌉? f(3)=1? No f(3)=2. ⌈2/2⌉=1. No.

f(3)=2, f(4)=2, f(5)=2, f(6)=3. 

⌊n/2⌋? f(3)=1 no. 

Hmm: 2,2,2,3 for n=3,4,5,6. Maybe f(n) = ⌈n/2⌉ - 1? f(3)=1 no. f(n)=⌊(n-1)/2⌋? f(3)=1 no.

Let me recompute f(3). K_3, 2 colors max. Two edges same color (pigeonhole, 3 edges 2 colors). They share a vertex → that vertex monochromatic degree 2. So f(3)=2. Yes.

Sequence 2,2,2,3. Let me get f(7), f(8).

Actually, let me hypothesize the answer relates to a known result. This is a competition problem (likely IMO shortlist or similar). The answer for n=2015...

Let me think about the general Gallai coloring min max monochromatic degree. 

I recall a result: In every Gallai coloring of K_n, there's a vertex with monochromatic degree at least n/2 - 1 or similar. Actually let me think about the construction achieving low values.

Construction: "Balanced Gallai coloring" via recursive 2-partition with alternating... no.

Let me think about the construction that gives the minimum. Consider the following: we want to use many colors but constrained by Gallai.

Key insight: Gallai partition. At the top level, 2 colors between parts. The reduced graph is a 2-coloring of K_m. To minimize the max cross monochromatic degree, we want the reduced graph balanced AND parts equal size, but that gives ~n/2. Alternatively, use few parts and recurse.

Let me define g(n) = min over Gallai colorings of K_n of max monochromatic degree. 

Recursion: g(n) = min over partitions (sizes n_1,...,n_m, m≥2, sum n) and 2-colorings of K_m (reduced) of [ max over parts i of ( max( cross_mono_deg(v in i), g(n_i) ) ) ] where cross_mono_deg(v in i) = max color sum of sizes of same-color reduced neighbors.

Wait but within part i we use a Gallai coloring achieving g(n_i), but the dominant color within might combine with cross color. Actually the max monochromatic degree of v in part i = max over colors c of (cross_c(v) + within_c(v)). We can choose the within coloring to avoid boosting the dominant cross color. So effectively max monochromatic degree for v in part i ≥ cross_dominant(i), and ≥ within max = g(n_i) (achievable), but could be more if colors align. To minimize, choose within coloring so its dominant color differs from cross dominant color. Then max = max(cross_dominant, g(n_i)). 

But this requires the within coloring to have its dominant color be a specific color different from cross dominant. Since we have freedom in colors (Gallai allows many colors), we can always pick fresh colors for within. So yes, max for v in part i = max(cross_dominant(i), g(n_i)).

So g(n) = min over partitions and reduced 2-colorings of max_i max(cross_dominant(i), g(n_i)).

where cross_dominant(i) = max( sum_{j: reduced edge ij red} n_j, sum_{j: reduced edge ij blue} n_j ).

Note sum of the two = n - n_i, so cross_dominant(i) ≥ (n - n_i)/2.

To minimize the max, we want all cross_dominant(i) and g(n_i) balanced.

Simplest: m=2, parts n_1, n_2. Reduced: one color. cross_dominant(1) = n_2, cross_dominant(2) = n_1. So g(n) ≤ max(n_1, n_2, g(n_1), g(n_2)) via this. Minimized when balanced: n_1 = n_2 = n/2, giving g(n) ≤ max(n/2, g(n/2)). So g(n) ≤ n/2 (since g(n/2) ≤ n/2). This gives g(n) ≤ n/2 but we want lower.

m=3: reduced K_3 2-colored, two edges one color (say red: 1-2, 1-3), one blue (2-3). cross_dominant: part1 red = n_2+n_3 = n-n_1, blue=0. part2: red=n_1, blue=n_3, dominant = max(n_1,n_3). part3: red=n_1, blue=n_2, dominant=max(n_1,n_2). To minimize max of {n-n_1, max(n_1,n_3), max(n_1,n_2), g(n_1),g(n_2),g(n_3)}. We want n-n_1 small → n_1 large. But then max(n_1, n_2) ≥ n_1 large. Trade-off. Set n_1 = n_2 = n_3? Then part1 dominant = 2n/3. Bad. Set n_1 large, n_2=n_3 small: n_1 = n-2s, n_2=n_3=s. part1 dom = 2s, part2 dom = max(n_1, s)=n_1=n-2s, part3 same. Max ≥ n-2s. Minimize max(2s, n-2s) → 2s = n-2s → s = n/4, n_1 = n/2. Then max = n/2. Same.

Hmm, seems like n/2 is a barrier with these. Let me reconsider—maybe g(n) = ⌈n/2⌉ - 1 or n/2?

Wait f(3)=2 = ⌈3/2⌉ = 2. f(4)=2 = 4/2. f(5)=2 < 5/2=2.5, ⌊5/2⌋=2. f(6)=3 = 6/2. 

So maybe g(n) = ⌊n/2⌋? Check: g(3)=⌊3/2⌋=1 ≠ 2. No.

g(3)=2, g(4)=2, g(5)=2, g(6)=3. ⌈(n-1)/2⌉: 1,2,2,3. g(3)=2≠1. 

Hmm g(3)=2 is special (small). Let me compute g(7). 

For n=7, can we get 3? ⌊7/2⌋=3. Try 2-coloring of K_7: degree 6, balanced 3-3, max=3. So g(7) ≤ 3. Can we get 2? Need max monochromatic degree ≤2, total degree 6, so ≥3 colors per vertex. With Gallai... seems hard. Likely g(7)=3.

g(8): 2-coloring K_8: degree 7, split 4-3, max 4. Can Gallai do 3? Try partition 4+4 cross red: cross dom 4 >3. Partition into m parts... Let me try m=4, sizes 2,2,2,2, reduced K_4 2-colored balanced (each part red degree 2, blue degree 1, or 2-1). Actually K_4 2-coloring: degree 3, max monochromatic ≥2. If balanced 2-1: cross dom = 2×2 = 4 >3. If we use sizes 2,2,2,2 and reduced where each part has mono degree 2 (two neighbors same color): cross dom = 2+2=4. Bad.

Try m=4 sizes 3,3,1,1? reduced K_4. Hmm. Let me try to get g(8)=3.

Try partition into 2 parts of 4, but use 2 colors between them? No, between two parts only 1 color (all edges between part 1 and part 2 same color in Gallai partition). Actually wait—is that required? Gallai partition: between two parts, all edges the same color. Yes. So 2 parts → 1 cross color → cross dom = other part size = 4.

Try m=4, sizes 2,2,2,2. reduced K_4 2-colored. Best: make it a 4-cycle red + 2 diagonals blue? Each part: red degree 2, blue degree 1. cross dom = 2×2 = 4. Or red = matching (2 edges), blue = rest. Each part red degree 1, blue degree 2. cross dom = 2×2=4. Always ≥4 since mono degree ≥2 and sizes 2.

m=8 singletons: 2-coloring K_8, max mono degree ≥4.

m=3 sizes a,b,c: as computed, max ≥ n/2 = 4.

Hmm so g(8) seems to be 4? Let me check if any clever partition gives 3.

m=5 sizes: e.g., 2,2,2,1,1 (sum 8). reduced K_5 2-colored. Max mono reduced degree ≥2. A part with mono reduced degree ≥2: if it's a size-2 part, cross dom ≥ 2×2=4 (if both neighbors size 2) or 2+1=3 (if one size 2 one size 1) or 1+1=2. To get cross dom ≤3 for the size-2 part, its 2 same-color neighbors must have total size ≤3, i.e., one size-2 and one size-1, or two size-1. And the size-1 parts: mono reduced degree ≥2, cross dom ≥ 2 (if neighbors size 1) but if a neighbor is size 2, ≥ 2+1 = 3 or 2+2=4.

This is getting complicated. Let me just guess the pattern g(n) = ⌊n/2⌋ for n≥4, with g(3)=2.

Check: g(4)=2=⌊4/2⌋ ✓, g(5)=2=⌊5/2⌋ ✓, g(6)=3=⌊6/2⌋ ✓, g(7)=3 ✓, g(8)=4 ✓ (if confirmed).

Then for n=2015: g(2015) = ⌊2015/2⌋ = 1007.

But wait, I should double check g(5)=2 and the general lower bound.

Lower bound: In any Gallai coloring of K_n, is there always a vertex with monochromatic degree ≥ ⌊n/2⌋?

Hmm, let me think. Actually I recall a theorem: In every Gallai coloring of K_n, there exist two vertices such that... or there's a vertex with monochromatic degree ≥ n/2. Let me think about whether ⌊n/2⌋ is the right bound or if it's higher.

Actually, wait. Let me reconsider g(5). 2-coloring of K_5 balanced gives max mono degree 2. But can Gallai with 3+ colors give max mono degree 2 as well (yes, 2-coloring is a special case). Can it give 1? No. So g(5)=2. But is there a Gallai coloring of K_5 with max mono degree exactly 2 that's not just 2-coloring? Doesn't matter, 2-coloring works.

Now is the lower bound ⌊n/2⌋? Let me think about n=5: ⌊5/2⌋ = 2. ✓. n=3: ⌊3/2⌋=1 but g(3)=2. So the formula ⌊n/2⌋ fails for n=3. But for large n maybe ⌊n/2⌋.

Hmm, but actually maybe the bound is higher. Let me reconsider.

Let me reconsider whether g(8) could be 3. Let me try harder.

Partition: 3 parts sizes 3,3,2. reduced K_3 2-colored. Two edges red sharing part P1 (size 3), one blue between P2,P3 (sizes 3,2). 
- P1 (size 3): cross red = 3+2 = 5. Too big.

Partition: 3 parts sizes 4,2,2. red edges P1-P2, P1-P3, blue P2-P3.
- P1: cross red = 2+2 = 4. Too big.
Swap: red P1-P2, blue P1-P3, red... no K_3 has 3 edges, 2 one color 1 other. The part with 2 same-color edges is the "center". To minimize its cross dom, make it small. Center = smallest part.

3 parts sizes 2,3,3, center size 2 (P1). red P1-P2, P1-P3 (sizes 3,3), blue P2-P3.
- P1: cross red = 3+3 = 6. Bad (center connects to both large parts).

Hmm, center always has cross dom = sum of other two = n - center size. To make small, center large. But then other parts small, and their dom = max(center, other). 

Center size c, others a, b, a+b = n-c. Center cross dom = a+b = n-c. Other part (size a) cross dom = max(c, b) [red to center = c, blue to other = b]. To minimize max(n-c, max(c,b), max(c,a)) = max(n-c, c, a, b). Since a+b=n-c and we want max(n-c,c) minimized → c = n/2, then n-c = n/2, max = n/2. So m=3 gives n/2.

So m=3 always gives ≥ n/2. m=2 gives ≥ n/2 (balanced). m≥4: Let me think generally.

For m parts with 2-coloring of K_m, and the constraint. Let me think about the lower bound from the reduced graph.

Claim: For any partition into m≥2 parts with 2-coloring of reduced K_m, max_i cross_dominant(i) ≥ (n - max_part)/... hmm.

Actually, let me think about a cleaner lower bound argument for the whole problem.

Lower bound proof idea: In any Gallai coloring of K_n, there's a vertex with monochromatic degree ≥ ⌊n/2⌋.

Hmm, is this true? Let me think about n=4: ⌊4/2⌋=2, g(4)=2 ✓. n=6: 3 ✓.

Let me try to prove: Consider the Gallai partition at top level: parts V_1,...,V_m, 2 colors (red, blue) between parts, reduced graph 2-colored K_m. 

Case 1: m = 1 — not a real partition, the whole graph is "within one part", meaning no top-level partition. But Gallai partition always exists with m≥2 (unless n=1). Actually Gallai's theorem: there's a partition into m≥2 parts (for n≥2). 

Wait, actually the Gallai partition might have m=2 minimum. Let me assume m≥2.

In reduced K_m (2-colored), consider a part V_i. Let R_i = sum of sizes of red-neighbors, B_i = sum of sizes of blue-neighbors, R_i + B_i = n - |V_i|. cross_dominant(i) = max(R_i, B_i) ≥ (n - |V_i|)/2.

For vertices in V_i, monochromatic degree ≥ cross_dominant(i) ≥ (n - |V_i|)/2.

If some |V_i| ≤ n/2, then (n - |V_i|)/2 ≥ n/4. Not enough.

Hmm, this gives n/4 not n/2. So the simple argument gives n/4. Need stronger.

Let me reconsider. Maybe the answer isn't ⌊n/2⌋.

Let me reconsider g(8). Maybe g(8) = 3 or even less with a clever multi-level construction!

Multi-level: Partition into 2 parts of 4, cross red. Within each part of 4, Gallai coloring with g(4)=2, using colors different from red. Then vertex in part 1: red degree = 4 (cross), other colors degree ≤ 2 (within). Max = 4. So max mono degree = 4. Not better.

What if within part we use red too? Then red degree = 4 + within_red. Worse.

So 2-part gives 4 for n=8.

Multi-level with 3 parts: top 3 parts, then recurse. As shown, top-level 3 parts gives ≥ n/2 = 4.

Hmm what about 4 parts at top, sizes 2,2,2,2, reduced K_4 2-colored. We saw cross dom ≥ 4. Then within each part (size 2), g(2)=1. Max = max(4, 1) = 4.

What about 4 parts sizes 3,3,1,1? reduced K_4 2-colored. Let me find the best 2-coloring. We want to minimize max cross_dominant. 

Parts: A(3), B(3), C(1), D(1). Edges: AB, AC, AD, BC, BD, CD. 2-color. 
cross_dominant(A) = max(sum of red-neighbors of A, sum of blue). A's neighbors B,C,D with sizes 3,1,1. 
We want to split {3,1,1} into red and blue to minimize max. Best: red={1,1}, blue={3} → max(2,3)=3. Or red={3}, blue={1,1} → 3. Or red={3,1},blue={1} → 4. So best 3.
Similarly B: best 3.
C: neighbors A,B,D sizes 3,3,1. Split to minimize max: {3},{3,1}→max(3,4)=4; {3,1},{3}→4; {3,3},{1}→6; {1},{3,3}→6. Best 4? Wait {3} red {3,1} blue: max(3,4)=4. Hmm. Actually split {3,3,1}: best is {3},{3,1} giving max(3,4)=4, or {3,1},{3} same. Or {3,3},{1} = 6. So min max = 4. 

So C has cross dom ≥ 4. Bad.

What if sizes 4,2,1,1? A(4),B(2),C(1),D(1). 
A neighbors B,C,D sizes 2,1,1: split {2},{1,1} → max(2,2)=2. 
B neighbors A,C,D sizes 4,1,1: split {4},{1,1}→max(4,2)=4; {4,1},{1}→5; {1,1},{4}→4. Best 4. Bad.

Sizes 5,1,1,1: A(5), B,C,D size 1. A neighbors 1,1,1: split {1,1},{1} → max(2,1)=2. B neighbors A,C,D sizes 5,1,1: split {5},{1,1}→max(5,2)=5; {1,1},{5}→5; {5,1},{1}→6. Best 5. Bad.

Sizes 2,2,2,2 gave 4. Seems 4 is the min for n=8 with m=4.

m=5: sizes summing 8. To have small parts. e.g., 2,2,2,1,1. reduced K_5 2-colored. Max mono reduced degree ≥ ⌈4/2⌉ = 2. 

Let me try to find a 2-coloring of K_5 on parts {A(2),B(2),C(2),D(1),E(1)} minimizing max cross_dominant.

This is complex. Let me think about it as: we want each part's neighbor-size-split to be balanced.

For part D(1): neighbors A,B,C,E sizes 2,2,2,1. Best split: {2,2},{2,1} → max(4,3)=4; {2,2,1},{2}→5; {2},{2,2,1}→5. Best 4. So D has cross dom ≥ 4. Bad.

Hmm. The size-1 parts have 4 neighbors with total size 7, split into 2 colors, max ≥ ⌈7/2⌉ = 4. So cross dom ≥ 4 for size-1 parts. Bad.

Generally, a part of size s has cross dom ≥ ⌈(n-s)/2⌉. For s=1: ⌈(n-1)/2⌉. For n=8: ⌈7/2⌉ = 4. So any size-1 part has cross dom ≥ 4. 

For s=2: ⌈6/2⌉ = 3. For n=8, size-2 part cross dom ≥ 3. 

So if all parts size 2 (m=4): cross dom ≥ 3, but we computed 4 because of the reduced graph structure (mono degree ≥2 forces 2 neighbors same color = 2+2=4). The ⌈(n-s)/2⌉ = 3 is a lower bound but actual is 4 due to integrality/structure.

Hmm wait, ⌈(8-2)/2⌉ = 3, but can a size-2 part achieve cross dom 3? It needs to split neighbors (total size 6) into 3+3. With 4 parts of size 2, neighbors are 3 parts of size 2 each, total 6, split into red {2,2}=4 and blue {2}=2, or red{2} blue{2,2}: max 4. Can't get 3+3 since each neighbor is size 2 (even). So 4. 

With parts of mixed sizes, a size-2 part could split neighbors 3+3. E.g., neighbors sizes 3,3 (m=3): but m=3 means only 2 neighbors. Hmm.

Let me try m=5 with sizes 2,2,2,1,1 but accept size-1 parts have cross dom 4. Bad.

What about making all parts size ≥2? n=8, m=4 all size 2 → 4. m=3 → 4. m=2 → 4. So g(8) = 4? 

But wait, multi-level: what if top level is m=4 parts of size 2, reduced 2-colored giving cross dom 4, but then we DON'T recurse (parts are size 2, g(2)=1 < 4, fine). Max = 4. 

Alternatively, is there a non-partition-based Gallai coloring (i.e., using the recursive structure more cleverly) that beats 4? The Gallai partition is the top level; below it we recurse. But the cross dom at top level already forces 4. Unless the top-level partition has m=1, which isn't allowed.

Wait, actually maybe I'm wrong that g(8)=4. Let me reconsider: maybe a Gallai coloring not following a "balanced" partition can do better. But every Gallai coloring has a Gallai partition, and the argument shows any Gallai partition of K_8 has a part with cross dom ≥ 4 (since for any partition, some part has cross dom ≥ ...). Let me verify: is it true that for ANY partition of 8 into parts with a 2-coloring of reduced K_m, max cross dom ≥ 4?

We need: for any 2-coloring of K_m (m≥2) with vertex weights summing to 8, max_v max(R_v, B_v) ≥ 4 where R_v+B_v = 8 - w_v.

Hmm, consider m=2: weights a, 8-a. cross dom = max(a, 8-a) ≥ 4. ✓.
m=3: as shown ≥ 4 (n/2).
m=4 all weight 2: 4. 
m=4 weights 3,3,1,1: size-1 parts have R+B=7, max≥4 (since ⌈7/2⌉=4). ✓.
m=5: some part weight ≤1, R+B ≥7, max ≥4. ✓ (since min weight 1, ⌈7/2⌉=4).
Actually for m≥5, min weight ≤ 8/5 < 2, so some part weight ≤1, cross dom ≥ ⌈7/2⌉ = 4. ✓.
m=4: min weight ≤ 2. If min weight 1: cross dom ≥ ⌈7/2⌉=4. If all weight 2: cross dom = 4 (shown). ✓.

So for n=8, any Gallai partition has a part with cross dom ≥ 4, hence a vertex with mono degree ≥ 4. So g(8) ≥ 4. And 2-coloring achieves 4. So g(8) = 4 = n/2.

Great, so g(8) = 4. Pattern g(n) = ⌊n/2⌋ holds for n=4,5,6,7,8.

Let me now prove the general lower bound: In any Gallai coloring of K_n, some vertex has monochromatic degree ≥ ⌊n/2⌋.

Proof: Take a Gallai partition into parts V_1,...,V_m (m≥2) with 2 colors between parts. Let s_i = |V_i|. For each i, cross_dominant(i) ≥ ⌈(n - s_i)/2⌉. We want to show max_i cross_dominant(i) ≥ ⌊n/2⌋, OR if not, recurse into a part.

Hmm, but if all cross_dominant(i) < ⌊n/2⌋, we need to look inside parts. This requires induction.

Induction: Claim g(n) ≥ ⌊n/2⌋ for n ≥ 4 (and g(3)=2, g(2)=1, g(1)=0).

Base cases: g(2)=1=⌊2/2⌋, g(3)=2≥⌊3/2⌋=1, g(4)=2.

Inductive step: Consider Gallai partition of K_n, parts sizes s_1,...,s_m, m≥2, 2-colored reduced. 

For each part i, vertices in it have mono degree ≥ max(cross_dominant(i), [mono degree within V_i]). By induction, within V_i (if s_i ≥ 4) there's a vertex with mono degree ≥ ⌊s_i/2⌋ (within V_i). But that vertex's total mono degree in that color = within + cross in same color. Hmm, the within-dominant color might differ from cross-dominant color.

This is the issue: the vertex with high within-mono-degree uses some color c; its cross degree in color c might be 0. So total in color c = within only. So we can't simply add.

So the correct statement: for a vertex v in V_i, mono degree in color c = within_c(v) + cross_c(v). We know max_c within_c(v) ≥ ⌊s_i/2⌋ (by induction, exists some v in V_i). And max_c cross_c(v) = cross_dominant(i) (same for all v in V_i). But these maxes might be different colors.

So mono degree of v ≥ max( max_c within_c(v), cross_dominant(i) ) ≥ max(⌊s_i/2⌋, cross_dominant(i)).

So we need: there exists i such that max(⌊s_i/2⌋, cross_dominant(i)) ≥ ⌊n/2⌋, OR combination... but actually we need a single vertex. The vertex achieving high within degree might not have high cross in same color. So the bound is max(⌊s_i/2⌋, cross_dominant(i)) for the best v in part i, and we need max over i of this ≥ ⌊n/2⌋.

So we need: max_i max(⌊s_i/2⌋, cross_dominant(i)) ≥ ⌊n/2⌋.

cross_dominant(i) ≥ ⌈(n - s_i)/2⌉. So max(⌊s_i/2⌋, ⌈(n-s_i)/2⌉) ≥ ⌊n/2⌋? 

Let's check: ⌊s/2⌋ + ⌈(n-s)/2⌉ = ? If s even: s/2 + (n-s)/2 = n/2 if n-s even, or s/2 + (n-s+1)/2 = (n+1)/2 if n-s odd. If s odd: (s-1)/2 + (n-s+1)/2 = n/2 if... let me just compute max(⌊s/2⌋, ⌈(n-s)/2⌉).

We have ⌊s/2⌋ + ⌈(n-s)/2⌉ ≥ n/2 always (since ⌊s/2⌋ ≥ (s-1)/2 and ⌈(n-s)/2⌉ ≥ (n-s)/2, sum ≥ (n-1)/2; hmm).

Let me just check: is max(⌊s/2⌋, ⌈(n-s)/2⌉) ≥ ⌊n/2⌋ for all s?

If n even, n=2q: ⌊n/2⌋ = q. ⌊s/2⌋ and ⌈(2q-s)/2⌉ = q - ⌊s/2⌋ (if s even: q - s/2; if s odd: q - (s-1)/2 = q - ⌊s/2⌋). So max(⌊s/2⌋, q - ⌊s/2⌋) ≥ q/2... no wait = max(a, q-a) where a=⌊s/2⌋. max(a, q-a) ≥ q/2, but we need ≥ q. That's only if a=0 or a=q. Not always!

E.g., n=8, s=4: max(2, 2) = 2 < 4. So this fails!

So the simple bound max(⌊s_i/2⌋, cross_dominant(i)) ≥ ⌊n/2⌋ is FALSE. For n=8, s=4: ⌊4/2⌋=2, cross_dominant ≥ ⌈4/2⌉=2, max=2 < 4.

But we showed g(8)=4 via a different argument (the reduced graph structure forces higher cross dom). So the induction needs the reduced graph structure, not just the size bound.

So the lower bound proof is more subtle. Let me reconsider.

For n=8, the argument was: any Gallai partition has a part with cross_dominant ≥ 4. This used case analysis on m. Let me generalize.

Claim: For any 2-coloring of K_m with vertex weights w_1,...,w_m summing to n (m≥2), max_v max(R_v, B_v) ≥ ⌊n/2⌋ where R_v (B_v) = sum of weights of red (blue) neighbors.

Is this true? Let me test n=5, weights 1,1,1,1,1 (m=5), 2-coloring K_5. max mono degree ≥ ⌈4/2⌉ = 2 = ⌊5/2⌋. ✓.

n=6, weights 1×6: 2-coloring K_6, max mono ≥ 3 = ⌊6/2⌋. ✓.

n=4, weights 2,2 (m=2): max(2,2)=2=⌊4/2⌋. ✓. weights 1,1,1,1: 2-coloring K_4, max mono ≥ 2. ✓.

n=7, weights 1×7: max mono ≥ 3 = ⌊7/2⌋. ✓.

So the claim might be: For any 2-coloring of complete graph K_m (m≥2) with nonneg integer weights summing to n, max_v max(R_v,B_v) ≥ ⌊n/2⌋.

If this claim is true, then the lower bound follows immediately (take the Gallai partition, the part with max cross_dominant ≥ ⌊n/2⌋ gives vertices with mono degree ≥ ⌊n/2⌋, no induction needed!).

Let me prove this claim. 

Claim: In any 2-coloring of K_m (m ≥ 2) with weights w_i ≥ 0 (integers, but could be 0? parts nonempty so w_i ≥ 1) summing to n, there's a vertex v with max(R_v, B_v) ≥ ⌊n/2⌋.

Proof attempt: Suppose for contradiction all max(R_v, B_v) ≤ ⌊n/2⌋ - 1, i.e., R_v ≤ ⌊n/2⌋-1 and B_v ≤ ⌊n/2⌋-1 for all v. Then R_v + B_v = n - w_v ≤ 2(⌊n/2⌋ - 1) = 2⌊n/2⌋ - 2. So w_v ≥ n - 2⌊n/2⌋ + 2. If n even: w_v ≥ 2. If n odd: w_v ≥ 3. 

Hmm, so all weights ≥ 2 (n even) or ≥ 3 (n odd). 

Case n even: all w_v ≥ 2, m ≤ n/2. Sum of all R_v = sum over red edges (w_i + w_j) = ... Let me think. Sum_v R_v = sum_{red edges ij} (w_i + w_j) = sum_i w_i × (red degree of i). Similarly sum_v B_v = sum_i w_i × (blue degree of i). Total sum_v (R_v + B_v) = sum_i w_i (deg(i)) = sum_i w_i (m-1) = (m-1)n. 

If all R_v ≤ n/2 - 1: sum R_v ≤ m(n/2 - 1). Similarly sum B_v ≤ m(n/2-1). So (m-1)n ≤ 2m(n/2 - 1) = m(n-2) = mn - 2m. So (m-1)n ≤ mn - 2m → -n ≤ -2m → n ≥ 2m. Since m ≤ n/2 (from w_v ≥ 2), we have 2m ≤ n, consistent, equality when m = n/2 and all w_v = 2 and all R_v = B_v = n/2 - 1.

So equality possible: m = n/2, all weights 2, all R_v = B_v = n/2 - 1 = m - 1. R_v = m-1 means red degree × 2... wait R_v = sum of weights of red neighbors = 2 × (red degree) = m - 1. So red degree = (m-1)/2. Need m-1 even, m odd. And blue degree = (m-1)/2 too. So m-1 even, m odd, and each vertex has red degree = blue degree = (m-1)/2. This is a regular 2-coloring. Exists when m odd (e.g., m=5: 2-coloring K_5 with each vertex red degree 2, blue degree 2 — yes, a 5-cycle red, complement blue). 

So for n even, equality achievable: n=10, m=5, weights 2 each, 5-cycle red. Then R_v = 4 = n/2 - 1 = 4. So max(R_v,B_v) = 4 = n/2 - 1 < n/2 = 5. 

So the claim is FALSE! For n=10, we can have a Gallai partition (5 parts of size 2, reduced = 5-cycle red + complement blue) where every part has cross_dominant = 4 < 5 = ⌊n/2⌋.

But then within each part (size 2), g(2) = 1. So vertices have mono degree ≥ max(4, 1) = 4. So this construction gives max mono degree = 4 for n=10? That would mean g(10) ≤ 4 < 5 = ⌊10/2⌋!

Wait, let me double-check. n=10, 5 parts of size 2, reduced K_5 2-colored as 5-cycle (red) + complement (blue, also 5-cycle). Each part: red neighbors = 2 parts (size 2 each) = 4, blue neighbors = 2 parts = 4. So cross_dominant = 4. Within each part (size 2), 1 edge, color it some third color (say green), giving within mono degree 1. So vertex mono degrees: red 4, blue 4, green 1. Max = 4. 

So g(10) ≤ 4! And ⌊10/2⌋ = 5. So g(n) ≠ ⌊n/2⌋. My earlier pattern was wrong for n=10.

So I need to recompute. Let me reconsider.

So g(10) ≤ 4. Can we do even better? Let me reconsider the recursion.

General construction: Partition into m parts, reduced 2-colored, recurse within parts. The max mono degree = max_i max(cross_dominant(i), g(s_i)) [choosing within colors to avoid cross dominant color].

To minimize, we want cross_dominant(i) ≈ g(s_i) for all i, and both small.

If we use equal parts size s = n/m, and a balanced 2-coloring of K_m (each vertex red degree ≈ blue degree ≈ (m-1)/2), then cross_dominant ≈ ((m-1)/2) × s = (m-1)s/2 = (m-1)/(2m) × n. And g(s) within.

So max ≈ max( (m-1)n/(2m), g(n/m) ).

To minimize over m: balance (m-1)n/(2m) and g(n/m).

Let me compute g recursively with this. Let me hypothesize g(n) and compute.

g(1)=0, g(2)=1, g(3)=2.

g(4): m=2, s=2: cross = 2, g(2)=1, max=2. m=4,s=1: cross = ⌈3/2⌉×1=2 (balanced K_4 2-coloring: each vertex degree 3, mono ≥2). max=2. So g(4)=2.

g(5): m=5,s=1: 2-coloring K_5, mono ≥2. max=2. m=2,s=2,3: cross for size-2 part = 3, too big. So g(5)=2.

g(6): m=3,s=2: reduced K_3 2-colored, center cross = 4. Bad. m=6,s=1: 2-coloring K_6, mono ≥3. m=2,s=3: cross=3, g(3)=2, max=3. So g(6)=3.

g(7): m=7,s=1: mono ≥3. m=2,s=3,4: cross for size-4 = 3, g(4)=2; cross for size-3 = 4. max=4. Worse. m=7 gives 3. Can we do better than 3? Need max ≤2. m parts... size-1 parts have cross ≥ ⌈6/2⌉=3. So any part of size 1 has cross ≥3. If all parts size ≥2, m≤3, but m=3 gives ≥ n/2 = 3.5 → 4. So g(7)=3.

g(8): computed = 4. Let me re-examine with the new insight. m=5,s=? 8/5 not integer. m=4,s=2: cross = 4 (as computed, since K_4 2-coloring mono degree ≥2, ×2 = 4). m=8,s=1: mono ≥4. m=2,s=4: cross=4. So g(8)=4. Can we do 3? Need all cross_dominant ≤3 and g(s_i)≤3. Size-1 parts: cross ≥ ⌈7/2⌉=4 >3. So no size-1 parts. All s_i≥2, m≤4. m=4,s=2: cross=4>3. m=3: ≥4. m=2: cross=4. So g(8)=4.

g(9): m=9,s=1: mono ≥4. m=3,s=3: cross = n - center = 6 (center size 3, others 3,3, cross=6). Bad. m=2,s=4,5: cross for size-4 = 5. Bad. Hmm. m=9 gives 4. Can we do better? size-1 parts cross ≥ ⌈8/2⌉=4. So if any size-1 part, cross≥4. All size≥2: m≤4. m=4, sizes sum 9, e.g., 3,2,2,2. reduced K_4 2-colored. size-2 parts: cross ≥ ⌈7/2⌉=4 (R+B=7). So ≥4. So g(9)≥4. m=9 gives 4. g(9)=4.

g(10): m=5,s=2: cross=4 (5-cycle). g(2)=1. max=4. So g(10) ≤ 4! Better than ⌊10/2⌋=5. Can we do 3? size-1 parts cross ≥ ⌈9/2⌉=5. No size-1. All size≥2, m≤5. m=5,s=2: cross=4>3. m=4, sizes sum 10, e.g., 3,3,2,2. size-2 parts: R+B=8, cross ≥4. m=3: ≥5. m=2: cross=5. So g(10)≥4. g(10)=4.

g(11): m=11,s=1: mono ≥5. Can we do 4? size-1 parts cross ≥5. No size-1. All size≥2, m≤5. m=5, sizes sum 11, e.g., 3,2,2,2,2. size-2 parts: R+B=9, cross ≥⌈9/2⌉=5. Bad. sizes 3,3,3,1,1—has size 1. Hmm. m=5 with sizes 3,2,2,2,2: size-2 parts have cross ≥5. m=4 sizes e.g. 3,3,3,2: size-2 part R+B=9, cross≥5. size-3 parts R+B=8, cross≥4. So maybe 4 achievable for size-3 parts but size-2 part has 5. Use sizes 3,3,3,2? No. All size ≥3: m ≤ 3, m=3 gives ≥ n/2 = 5.5. Bad. So g(11) = 5? 

Hmm wait let me reconsider. m=5, sizes 3,2,2,2,2. The size-2 parts have R+B = 9 (n - 2 = 9), so cross_dominant ≥ ⌈9/2⌉ = 5. So ≥5. m=5 sizes 4,2,2,2,1: size-1 cross ≥5. Bad. 

What about m=4, sizes 3,3,3,2: size-2 part R+B=9 → cross ≥5. Bad. Sizes 3,3,3,2 is the only way with min size 2 and m=4 summing 11 (3+3+3+2). 

m=3: ≥6. m=2: cross ≥5 or 6. 

So g(11) = 5? Via m=11 (2-coloring K_11, mono ≥5) or m=2 (5,6 → cross 5 or 6, g(5)=2,g(6)=3, max=5). So g(11)=5.

Hmm wait, but maybe a 2-coloring of K_11 can have max mono degree exactly 5 (balanced: degree 10, split 5-5). Yes. So g(11) ≤ 5. And lower bound 5. So g(11)=5.

g(12): m=6,s=2: reduced K_6 2-colored, mono degree ≥3, cross = 3×2 = 6. Bad. m=2,s=6: cross=6, g(6)=3, max=6. m=12,s=1: mono ≥6. Hmm all give 6? Can we do better?

m=4,s=3: reduced K_4 2-colored, mono degree ≥2, cross = 2×3 = 6. Bad. m=3,s=4: cross = 8 (center). Bad.

What about m=6, s=2 but reduced K_6 2-colored with mono degree exactly 3 (balanced, degree 5, split 3-2, max 3): cross = 3×2 = 6. Or split 2-3. Still 6.

Hmm. What about unequal parts? m=4 sizes 3,3,3,3: cross = 6 (mono degree 2 × 3). m=5 sizes e.g. 3,3,2,2,2: size-2 parts R+B=10, cross ≥5. size-3 parts R+B=9, cross ≥5. So maybe 5? Let me check if achievable.

m=5, sizes 3,3,2,2,2 (sum 12). Need 2-coloring of K_5 such that all cross_dominant ≤ 5 (and g(3)=2, g(2)=1, so within fine). 

size-3 parts: R+B = 9, need max(R,B) ≤ 5, so split 5+4 or 4+5. 
size-2 parts: R+B = 10, need max ≤ 5, so split 5+5.

So size-2 parts need R_v = B_v = 5 exactly. size-3 parts need {R,B} = {4,5}.

Let me see if such a 2-coloring exists. Parts: A,B (size 3), C,D,E (size 2). 

For C (size 2): R_C = B_C = 5. C's neighbors: A,B,D,E with weights 3,3,2,2. Need to split into two groups summing 5 each. 3+2 = 5, 3+2 = 5. So {A,D} red {B,E} blue, or {A,E}{B,D}, or {A,B}... 3+3=6 no. So C's red neighbors = {A, D} (3+2=5) and blue = {B,E} (3+2=5), or similar.

Similarly D: neighbors A,B,C,E (3,3,2,2), split 5+5: {A,C}{B,E} or {A,E}{B,C} etc.
E: neighbors A,B,C,D (3,3,2,2), split 5+5.

For A (size 3): neighbors B,C,D,E (3,2,2,2), R+B=9, need {4,5}. Split: 2+2=4, 3+2=5. So {C,D} red (4) {B,E} blue (5), etc. Or {C,E} red {B,D} blue, {D,E} red {B,C} blue. Or {B} red (3) {C,D,E} blue (6) — no, 6>5. Or {B,C} red (5) {D,E} blue (4). Etc.

This is a constraint satisfaction. Let me try to construct.

Let me denote edges. Let me try:
C: red to A, D; blue to B, E. (R_C = 3+2=5, B_C = 3+2=5 ✓)
D: red to B, C; blue to A, E. (R_D = 3+2=5, B_D = 3+2=5 ✓) [but C-D: C has D red, D has C red ✓ consistent]
E: red to A, B; blue to C, D. (R_E = 3+3=6) ✗. 

Try E: need R_E = B_E = 5, neighbors A,B,C,D (3,3,2,2). Split {A,C}{B,D}: 3+2=5, 3+2=5. So E red to A,C; blue to B,D.
Check C-E: C has E blue (from C's assignment: blue to B,E ✓), E has C red. Conflict! C-E can't be both red and blue.

Let me be systematic. Variables: color of AB, AC, AD, AE, BC, BD, BE, CD, CE, DE (10 edges).

Constraints:
- C: R_C = w(A if AC red) + w(B if BC red) + w(D if CD red) + w(E if CE red) = 5. B_C = 5.
  So among {AC, BC, CD, CE}, the red ones sum to 5 (weights A=3,B=3,D=2,E=2). 
- D: among {AD, BD, CD, DE}, red sum = 5 (weights A=3,B=3,C=2,E=2).
- E: among {AE, BE, CE, DE}, red sum = 5 (weights A=3,B=3,C=2,D=2).
- A: among {AB, AC, AD, AE}, red sum ∈ {4,5} (weights B=3,C=3,D=2,E=2). [R_A = 4 or 5]
- B: among {AB, BC, BD, BE}, red sum ∈ {4,5} (weights A=3,C=3,D=2,E=2).

Let me try to set CD, CE, DE, and the rest.

For C: red sum from {AC(3), BC(3), CD(2), CE(2)} = 5. Options: 3+2 (one of AC/BC + one of CD/CE). 
For D: red sum from {AD(3), BD(3), CD(2), DE(2)} = 5. Options: 3+2.
For E: red sum from {AE(3), BE(3), CE(2), DE(2)} = 5. Options: 3+2.

So each of C, D, E has exactly one 3-weight edge red and one 2-weight edge red (and the other two blue), among their 4 edges.

Let me pick:
C: AC red, CD red. (3+2=5) → BC blue, CE blue.
D: BD red, CD red. (3+2=5) → AD blue, DE blue. [CD red consistent ✓]
E: AE red, CE... CE is blue (from C). So E needs one 3-weight red (AE or BE) and one 2-weight red (CE or DE). CE blue, DE blue (from D). So no 2-weight edge available for E! Contradiction.

Try different. 
C: AC red, CE red. → BC blue, CD blue.
D: AD red, DE red. → BD blue, CD blue. [CD blue consistent ✓]
E: AE red, CE red. (3+2=5) → BE blue, DE blue. [CE red consistent ✓, DE blue consistent ✓]
Now check A: red edges among {AB, AC, AD, AE}: AC red, AD red, AE red. That's 3 red (C,D,E) + AB?. Red sum so far = 3+2+2 = 7 (weights C=3,D=2,E=2). Already 7 > 5. ✗.

Hmm. A has AC, AD, AE all red → R_A ≥ 7. Bad.

The issue: A is connected to C,D,E and if all three of C,D,E point their red 3-weight edge to A, then A gets too many red.

Let me reconsider. Each of C,D,E picks one 3-weight neighbor (among A,B) to be red. If all pick A, A is overloaded. Distribute: some pick A, some pick B.

C picks A (AC red) or B (BC red). D picks A (AD red) or B (BD red). E picks A (AE red) or B (BE red).

A's red 3-weight edges = number of {C,D,E} that picked A, times... no, weight 3 for C, 2 for D, 2 for E. Wait A's neighbors: B(3), C(3), D(2), E(2). AC red contributes 3, AD red contributes 2, AE red contributes 2.

If C picks A (AC red, +3), D picks B (AD blue), E picks B (AE blue): A's red from C,D,E = 3. Plus AB. R_A = 3 + (AB red? 3 : 0). For R_A ∈ {4,5}: AB red → 6 (too much), AB blue → 3 (too little, need ≥4). ✗.

If C picks A (+3), D picks A (+2), E picks B: A red = 5 + AB. AB blue → 5 ✓ (R_A=5). AB red → 8 ✗. So AB blue, R_A = 5, B_A = 9-5 = 4 ✓.

If C picks A, D picks B, E picks A: A red = 3+2 = 5, AB blue → 5 ✓.

If C picks B, D picks A, E picks A: A red = 2+2 = 4, AB blue → 4 ✓ (R_A=4, B_A=5).

If C picks B, D picks A, E picks B: A red = 2, AB? → 2 or 5. AB red → 5 ✓. AB blue → 2 ✗.

If C picks B, D picks B, E picks A: A red = 2, AB red → 5 ✓.

If C picks B, D picks B, E picks B: A red = 0, AB red → 3 ✗.

OK so several options. Let me pick: C picks A, D picks A, E picks B, AB blue.
- C: AC red. Needs one 2-weight red among CD, CE. 
- D: AD red. Needs one 2-weight red among CD, DE.
- E: BE red. Needs one 2-weight red among CE, DE.

Now the 2-weight choices:
C: CD red or CE red.
D: CD red or DE red.
E: CE red or DE red.

Each picks exactly one. And consistency (CD color same for C and D, etc.).

If C: CD red. D: CD red (consistent) or DE red. 
  - D: CD red: then E needs CE or DE red. E: CE red or DE red. 
    - E: CE red. Check C: C has CD red, CE red → that's TWO 2-weight red for C, but C should have exactly one (R_C = AC(3) + one 2-weight = 5). ✗ (C would have R_C = 3+2+2 = 7).
    
Wait, I need C to have exactly one 2-weight red edge. Let me restate: C has AC red (3-weight) and exactly one of {CD, CE} red (2-weight), the other blue. Similarly D: AD red + exactly one of {CD, DE}. E: BE red + exactly one of {CE, DE}.

C: CD red, CE blue OR CD blue, CE red.
D: CD red, DE blue OR CD blue, DE red.
E: CE red, DE blue OR CE blue, DE red.

Consistency: CD same for C and D. CE same for C and E. DE same for D and E.

Case C: CD red, CE blue.
  D: if CD red (consistent), DE blue. Then E: CE blue (consistent), DE blue (consistent with D). But E needs one of CE,DE red. Both blue. ✗.
  D: if CD blue — inconsistent with C (CD red). ✗.
Case C: CD blue, CE red.
  D: CD blue (consistent), DE red. Then E: CE red (consistent), DE red (consistent). E has CE red, DE red — that's two 2-weight red, but E needs exactly one. ✗.
  D: CD red — inconsistent. ✗.

So no valid assignment with (C→A, D→A, E→B, AB blue). 

Let me try C picks A, D picks B, E picks A, AB blue.
- C: AC red, one of {CD,CE} red.
- D: BD red, one of {CD,DE} red.
- E: AE red, one of {CE,DE} red.

C: CD red/CE blue or CD blue/CE red.
D: CD red/DE blue or CD blue/DE red.
E: CE red/DE blue or CE blue/DE red.

Case C: CD red, CE blue.
  D: CD red (consistent), DE blue. E: CE blue (consistent), DE blue (consistent) → E has none red. ✗.
  D: CD blue ✗ inconsistent.
Case C: CD blue, CE red.
  D: CD blue (consistent), DE red. E: CE red (consistent), DE red (consistent) → E two red. ✗.
  D: CD red ✗.
Same issue. 

The problem: the three 2-weight edges CD, CE, DE form a triangle among C,D,E, and each of C,D,E wants exactly one red among its two triangle edges. That means the red edges among {CD,CE,DE} form a... each vertex incident to exactly one red triangle edge → perfect matching on 3 vertices → impossible (odd cycle).

So with 3 size-2 parts, can't have each pick exactly one 2-weight red in the triangle. So this particular weight config (3,3,2,2,2) with the balanced requirement fails for the size-2 parts needing exactly 5+5.

Hmm. So maybe g(12) > 5? Let me reconsider. Maybe g(12) = 6.

Actually wait, maybe a different partition works for n=12. Let me reconsider.

Let me reconsider the general pattern. It seems g(n) is not simply ⌊n/2⌋. Let me tabulate:
g(1)=0, g(2)=1, g(3)=2, g(4)=2, g(5)=2, g(6)=3, g(7)=3, g(8)=4, g(9)=4, g(10)=4, g(11)=5, g(12)=?

Hmm, let me see: 0,1,2,2,2,3,3,4,4,4,5,?

Differences: 1,1,0,0,1,0,1,0,0,1,...

Let me see if g(n) = ⌈n/3⌉ + something? g(10)=4, ⌈10/3⌉=4. g(8)=4, ⌈8/3⌉=3. No.

Let me think about it differently. The construction for g(10)=4 used 5 parts of size 2, reduced = 5-cycle. The cross dom = 4 = 2×(m-1)/2 = 2 × 2 = 4 where m=5, (m-1)/2 = 2. So cross dom = s × (m-1)/2 = 2 × 2 = 4. And n = sm = 10. cross dom = s(m-1)/2 = (n - s)/2 = (10-2)/2 = 4. 

So with equal parts and perfectly balanced reduced (m odd, regular), cross dom = (n-s)/2 = n/2 - s/2. To minimize, maximize s (minimize m), but m≥2 and need balanced reduced (m≥3 for 2 colors to both appear, m≥5 for regular degree (m-1)/2... actually m=3: reduced K_3 2-colored, not regular (2+1), center has degree 2). 

For m odd ≥5, regular 2-coloring exists (each vertex (m-1)/2 red, (m-1)/2 blue). cross dom = s(m-1)/2. With s = n/m: cross dom = n(m-1)/(2m) = n/2 - n/(2m). Increasing in m. So larger m → larger cross dom. Smaller m → smaller cross dom but s larger, and g(s) might dominate.

So we want to balance cross dom = n(m-1)/(2m) and g(s) = g(n/m).

For the construction to beat ⌊n/2⌋, we need n(m-1)/(2m) < n/2, i.e., always true for m≥2 (strict). But we also need g(n/m) ≤ that.

Let me define the recursion for equal parts (when feasible):
g(n) ≤ min over valid m of max( n(m-1)/(2m), g(n/m) ) [when n/m integer and balanced reduced exists].

But also non-equal parts and non-regular might do better. This is getting complicated. Let me look for the pattern more carefully.

Actually, let me reconsider. This is a known competition problem. Let me recall: "2015 cities" suggests an olympiad problem around 2015. The answer might be a specific number.

Let me think about the problem differently. Let me reconsider the lower bound and upper bound more carefully.

Let me reconsider: maybe the answer is 1008 or 1007 or related to 2015.

Let me reconsider the structure. Let me recompute g more carefully for small n, considering all constructions (not just equal parts).

g(12): Let me try m=4, sizes 3,3,3,3, reduced K_4 2-colored. Best 2-coloring of K_4: each vertex degree 3, mono degree ≥2. Can we get mono degree exactly 2 for all? Yes: 4-cycle red (each vertex red degree 2), diagonals blue (each blue degree 1). Then cross dom = 2×3 = 6. So 6. Or red = matching (degree 1), blue = 4-cycle (degree 2): cross dom = 2×3 = 6. So 6.

m=6, sizes 2,2,2,2,2,2: reduced K_6 2-colored, mono degree ≥3, cross = 3×2 = 6. 

m=3, sizes 4,4,4: center cross = 8. Bad.

m=2, sizes 6,6: cross = 6, g(6)=3, max = 6.

m=12, s=1: 2-coloring K_12, mono ≥6.

m=5, sizes 3,3,2,2,2: we showed the balanced version fails. But maybe a non-balanced 2-coloring gives max cross dom = 5 (not 4)? We need max cross dom ≤ 5 and g ≤ 5. Since size-2 parts have R+B=10, cross dom ≥5. size-3 parts R+B=9, cross dom ≥5 (⌈9/2⌉=5). So all cross dom ≥5. Can we achieve all = 5? Need size-2 parts: R=B=5. size-3 parts: {R,B}={4,5}. 

Earlier I tried to get size-2 parts R=B=5 and hit the odd-cycle problem for the triangle among C,D,E. But that was with a specific 3-weight assignment. Let me reconsider whether ANY assignment works.

Actually the odd-cycle problem: C, D, E (size 2) each need exactly one red among their two mutual edges (CD, CE, DE) to get R=B=5 (given their 3-weight edge is red to one of A,B). Wait, no—R_C = (red 3-weight edge) + (red 2-weight edges among CD, CE). For R_C = 5 = 3 + 2, need exactly one 2-weight red. But could also be R_C = 5 = 0 + 5? No, 2-weight edges sum to at most 4 (two edges × 2). Or R_C = 3 + 2 (one 3-weight red, one 2-weight red) or R_C = 0 + ... no, if no 3-weight red, R_C ≤ 4 < 5, then B_C = 10 - R_C ≥ 6 > 5. So must have exactly one 3-weight red and one 2-weight red. 

So yes, each of C,D,E needs exactly one red 2-weight edge among the triangle CDE. That's a perfect matching on 3 vertices → impossible. So no 2-coloring achieves all size-2 parts R=B=5. So at least one size-2 part has cross dom ≥ 6.

So m=5 sizes (3,3,2,2,2) gives max cross dom ≥ 6. Worse than 6? No, =6. Same as others.

What about m=5 sizes (4,2,2,2,2)? size-2 parts R+B = 10, cross ≥5. size-4 part R+B = 8, cross ≥4. Need size-2 parts R=B=5. C,D,E,F size 2, A size 4. Each size-2 part: neighbors A(4) + two other size-2 (2 each) + ... wait m=5 so 4 neighbors. C's neighbors: A(4), and 3 other size-2 parts (2 each). R+B = 4+2+2+2 = 10. For R=B=5: split {4, ...} hmm 4 + 2 = 6, or 4 alone = 4, or 2+2+2=6, or 2+2=4. To get 5: 4+? no. 4+2=6, 4=4, 2+2+2=6, 2+2=4. Can't make 5! (weights 4,2,2,2; subset sums: 0,2,4,6,8,10... all even). So R_C is even, can't be 5. So R_C ∈ {4,6} → cross dom ≥6. Bad.

So (4,2,2,2,2) gives ≥6.

m=5 sizes (3,3,3,2,1): size-1 part cross ≥ ⌈11/2⌉ = 6. Bad.

So g(12) = 6? Let me confirm no construction gives 5.

For max mono degree ≤ 5: no size-1 parts (cross ≥6). All parts size ≥2. m ≤ 6. 
- m=6: all size 2, cross ≥ 6 (mono degree ≥3 × 2). 
- m=5: sizes sum 12, all ≥2. Options: (2,2,2,2,4), (2,2,2,3,3), (2,2,3,3,2)same, (2,2,2,2,4), (3,3,2,2,2), (4,2,2,2,2), (2,2,2,3,3). 
  - (4,2,2,2,2): size-2 parts can't split to 5 (even weights) → ≥6.
  - (3,3,2,2,2): odd cycle problem → ≥6.
- m=4: sizes sum 12, all ≥2. (3,3,3,3): cross ≥6. (2,2,4,4): size-2 parts R+B=10, weights of neighbors... part size 2 has 3 neighbors. (4,4,2) weights: subset sums to split 10 into ≤5: 4+4=8,4+2=6,2=2,4=4,4+4+2=10. Can't make 5. ≥6. (2,3,3,4): size-2 part neighbors (3,3,4) sum 10, split: 3+3=6,3+4=7,4=4,3=3. Can't make 5. ≥6. (2,2,3,5): size-2 part neighbors (2,3,5) sum 10: 2+3=5! So R=5 possible. size-5 part: neighbors (2,2,3) sum 7, cross ≥⌈7/2⌉=4, need ≤5: split 3+2+2=7, {3,2}{2}→5+2, max 5; {3}{2,2}→3+4, max4; {2}{3,2}→2+5. So {3}{2,2}: R=3,B=4, max 4 ✓. size-3 part: neighbors (2,2,5) sum 9, cross ≥5: split {5}{2,2}→5+4 max5 ✓. size-2 parts: neighbors (2,3,5) sum 10: split {2,3}{5}→5+5 ✓! or {5}{2,3}. So R=B=5 possible.
  
  So m=4, sizes (5,3,2,2)! Let me check if a valid 2-coloring exists with all cross dom ≤ 5.

Parts: A(5), B(3), C(2), D(2). Edges: AB, AC, AD, BC, BD, CD.
- A: neighbors B(3),C(2),D(2), R+B=7. Need max ≤5: {3}{2,2}→3,4 max4 ✓ or {3,2}{2}→5,2 max5 ✓ or {2}{3,2}→2,5 max5 ✓. All fine, A easy.
- B: neighbors A(5),C(2),D(2), R+B=9. Need max ≤5: {5}{2,2}→5,4 ✓ or {5,2}{2}→7,2 ✗ or {2}{5,2}→2,7 ✗. So B must have A red, C&D blue (or A blue, C&D red): {A red, C,D blue} → R=5,B=4 ✓, or {A blue, C,D red} → R=4,B=5 ✓.
- C: neighbors A(5),B(3),D(2), R+B=10. Need max ≤5: {5}{3,2}→5,5 ✓! or {5,3}{2}→8 ✗ etc. So C must have A one color, B&D other: {A red, B&D blue} → R=5, B=5 ✓, or {A blue, B&D red} → R=5,B=5 ✓.
- D: neighbors A(5),B(3),C(2), R+B=10. Need {5}{3,2}: {A red, B&C blue} or {A blue, B&C red}.

So constraints:
B: (A red, C blue, D blue) or (A blue, C red, D red).
C: (A red, B blue, D blue) or (A blue, B red, D red).
D: (A red, B blue, C blue) or (A blue, B red, C red).

Case 1: A red to B, C, D (i.e., AB, AC, AD all red).
  B: A red → C blue, D blue. So BC blue, BD blue.
  C: A red → B blue, D blue. So BC blue (consistent), CD blue.
  D: A red → B blue, C blue. So BD blue (consistent), CD blue (consistent).
  Check A: A red to B,C,D: R_A = 3+2+2 = 7 > 5! ✗.

Case 2: A blue to all.
  B: A blue → C red, D red. BC red, BD red.
  C: A blue → B red, D red. BC red (consistent), CD red.
  D: A blue → B red, C red. BD red, CD red (consistent).
  A: R_A = 0, B_A = 7. max = 7 > 5 ✗.

So A is forced to have all same color to B,C,D (from B,C,D's constraints), giving A cross dom 7. Bad.

Hmm. So (5,3,2,2) fails because A is forced.

The issue: B, C, D all require A to be the "5" in their split, forcing A to one color, overloading A.

What if A's constraint is relaxed—A has R+B=7, max can be up to 5 (we need ≤5). If A all red: R_A=7 >5. If A all blue: B_A=7>5. So A can't be all one color. A needs at least one red and one blue among B,C,D. But B,C,D each force A to a single color. If they disagree, conflict. If they agree, A overloaded. So impossible.

So (5,3,2,2) fails. 

Let me check other m=4 options: (2,2,4,4) done (≥6), (2,3,3,4): size-2 part neighbors (3,3,4) sum 10, can't split to 5 (3+3=6, 3+4=7, 4=4, 3=3, 3+3+4=10). Subset sums: 0,3,4,6,7,10. No 5. ≥6. (2,2,3,5) = (5,3,2,2) failed. (2,2,2,6): size-2 parts neighbors (2,2,6) sum 10: 2+2=4, 6=6, 2+6=8. No 5. ≥6. (3,3,3,3): ≥6. (2,4,3,3) same as (2,3,3,4). 

So all m=4 options give ≥6. m=3 gives ≥6. m=2 gives 6. m=6 gives 6. So g(12) = 6.

So g(12) = 6 = 12/2. Hmm. So g(10)=4 < 5, but g(12)=6=12/2. Interesting.

Let me recompute the sequence: g(1)=0,g(2)=1,g(3)=2,g(4)=2,g(5)=2,g(6)=3,g(7)=3,g(8)=4,g(9)=4,g(10)=4,g(11)=5,g(12)=6.

Hmm, g(10)=4 is the outlier below ⌊n/2⌋=5. Let me double-check g(10)=4 is achievable and correct.

g(10): 5 parts size 2, reduced = 5-cycle (red) + complement 5-cycle (blue). Each part: 2 red neighbors (size 2 each) = 4, 2 blue neighbors = 4. cross dom = 4. Within part (size 2): 1 edge, color green, mono degree 1. So max mono degree = max(4, 1) = 4. ✓. Valid Gallai coloring (5 parts, 2 colors between, within each part trivially Gallai). So g(10) ≤ 4. And lower bound: we showed ≥4 (size-1 parts cross ≥5, all size≥2 m≤5, m=5 sizes (2,2,2,2,2) cross=4, m=4 sizes (2,2,3,3): size-2 parts R+B=8, cross ≥4; can we achieve 4? Let me not worry, g(10)=4 confirmed by construction and the lower bound argument that it can't be 3: size-1 parts cross ≥5, all size≥2 m≤5, m=5 all size 2 cross ≥4 (need ≤3 impossible since ⌈8/2⌉=4). So ≥4. g(10)=4. ✓.

So the sequence has g(10)=4. Let me compute more to find the pattern.

g(13): m=13,s=1: 2-coloring K_13, mono ≥6. Can we do 5? size-1 parts cross ≥6. No size-1. All size≥2, m≤6. m=6 sizes sum 13: (3,2,2,2,2,2). size-2 parts R+B=11, cross ≥⌈11/2⌉=6. Bad. (3,3,2,2,2,1) has size 1. So m=6 with all ≥2: min sum 12, 13 = 3+2+2+2+2+2. size-2 parts cross ≥6. m=5 sizes sum 13 all ≥2: (3,3,3,2,2),(3,3,2,2,3)same,(5,2,2,2,2),(3,3,3,2,2),(4,3,2,2,2). size-2 parts R+B=11, cross ≥6. So ≥6. m=4: sizes sum 13, (3,3,3,4): size-3 parts R+B=10 cross ≥5, size-4 R+B=9 cross ≥5. Maybe 5? Let me check (4,3,3,3). A(4),B(3),C(3),D(3). 
  B: neighbors A(4),C(3),D(3), R+B=10, need ≤5: {4,3}{3}→7 ✗; {4}{3,3}→4,6 ✗; {3,3}{4}→6 ✗; {4,3}... hmm. subset sums of {4,3,3}: 0,3,4,6,7,10. To split 10 into two parts both ≤5: 5+5, but 5 not achievable. 4+6 (6>5). 3+7. None work! So B cross ≥6. Bad.
  (5,3,3,2): size-2 part neighbors (5,3,3) sum 11, cross ≥6. Bad. (4,4,3,2): size-2 neighbors (4,4,3) sum 11 ≥6. (5,4,2,2): size-2 neighbors (5,4,2) sum 11 ≥6. (6,3,2,2): size-2 neighbors (6,3,2) sum 11 ≥6. (7,2,2,2): size-2 neighbors (7,2,2) sum 11 ≥6. So m=4 all bad (≥6). m=3: ≥7. m=2: cross ≥6 or 7. So g(13) = 6.

g(14): m=7,s=2: reduced K_7 2-colored, mono degree ≥3, cross = 3×2 = 6. g(2)=1. max=6. So g(14) ≤ 6! Can we do 5? size-1 parts cross ≥7. No size-1. All size≥2, m≤7. m=7 all size 2: cross = 6 (need ≤5, but ⌈12/2⌉=6). m=6 sizes sum 14 all ≥2: (3,3,2,2,2,2) etc. size-2 parts R+B=12, cross ≥6. m=5: (2,2,2,4,4),(2,2,3,3,4),(2,3,3,3,3),(2,2,2,3,5)... size-2 parts R+B=12 cross ≥6. m=4: (4,4,3,3): size-3 parts R+B=11 cross ≥6. (4,3,3,4)same. (5,3,3,3): size-3 neighbors (5,3,3) sum 11 ≥6. (2,4,4,4): size-2 neighbors (4,4,4) sum 12, split 6+6 or 4+8, cross ≥6. (2,3,4,5): size-2 neighbors (3,4,5) sum 12, split: 3+4=7,5+... 5+3+4=12, 5=5,3+4=7,4+5=9,3+5=8,4=4,3=3. To get ≤5: {5}{3,4}→5+7 ✗; {3}{4,5}→3+9 ✗; {4}{3,5}→4+8 ✗; {3,4}{5}→7 ✗. Hmm 5 alone = 5, rest 7. So min max = 7. ≥6. Actually ≥7. (2,2,5,5): size-2 neighbors (2,5,5) sum 12: 2+5=7, 5=5, 5+5=10, 2=2. {5}{2,5}→5+7. min max 7. ≥6. m=3: ≥7. m=2: 7. So g(14) = 6.

g(15): m=5,s=3: reduced K_5 2-colored regular (5-cycle), mono degree 2, cross = 2×3 = 6. g(3)=2. max=6. So g(15) ≤ 6! Can we do 5? size-1 cross ≥7. No size-1. All ≥2, m≤7. m=7 sizes sum 15 all ≥2: (3,2,2,2,2,2,2). size-2 parts R+B=13, cross ≥7. Bad. m=6: (3,3,2,2,2,3)→(3,3,3,2,2,2) sum 15. size-2 parts R+B=13 cross ≥7. m=5: (3,3,3,3,3): cross = 6 (regular 5-cycle, 2×3). (3,3,3,2,4): size-2 part R+B=13 ≥7. (5,3,3,2,2): size-2 R+B=13 ≥7. (3,3,3,3,3) gives 6. Can m=5 (3,3,3,3,3) give 5? cross = 2×3 = 6 >5. No. m=4: (4,4,4,3): size-3 neighbors (4,4,4) sum 12, split 4+8,6+6 → cross ≥6. (4,4,3,4)same. (5,4,3,3): size-3 neighbors (5,4,3) sum 12: 5+4=9,3+5=8,4+3=7,5=5,4=4,3=3. {5}{4,3}→5+7 ✗. {4}{5,3}→4+8 ✗. {3}{5,4}→3+9 ✗. min max 7. (5,5,3,2): size-2 R+B=13 ≥7. (6,3,3,3): size-3 neighbors (6,3,3) sum 12: 6=6,3+3=6,6+3=9. {6}{3,3}→6+6. cross ≥6. (4,4,4,3) cross ≥6. (7,3,3,2): size-2 ≥7. So m=4 ≥6. m=3: ≥8. m=2: 7 or 8. So g(15) = 6.

g(16): m=2,s=8: cross=8. m=4,s=4: reduced K_4, mono ≥2, cross=2×4=8. m=8,s=2: reduced K_8, mono ≥4, cross=4×2=8. m=16,s=1: mono ≥8. Hmm all 8? Can we do better with unequal? 

m=5 sizes sum 16: (4,3,3,3,3): size-3 parts R+B=13, cross ≥7. (4,4,3,3,2): size-2 R+B=14 ≥7. (2,2,2,5,5): size-2 R+B=14 ≥7. (4,3,3,3,3): size-3 R+B=13 ≥7. size-4 R+B=12 ≥6. Hmm. (6,3,3,2,2): size-2 R+B=14 ≥7. m=5 seems ≥7. 

m=6 sizes (3,3,3,3,2,2) sum 16: size-2 R+B=14 ≥7. m=7 (2,2,2,2,3,3,2)→(3,3,2,2,2,2,2) sum 16: size-2 R+B=14 ≥7. 

m=4 (4,4,4,4): cross = 2×4 = 8. (5,4,4,3): size-3 neighbors (5,4,4) sum 13 ≥7. (5,5,3,3): size-3 neighbors (5,5,3) sum 13: 5+5=10,5+3=8,3=3,5=5. {5}{5,3}→5+8 ✗. {3}{5,5}→3+10 ✗. {5,3}{5}→8 ✗. min max 8. (6,4,3,3): size-3 neighbors (6,4,3) sum 13: 6=6,4+3=7,6+3=9,6+4=10. {6}{4,3}→6+7 ✗. min max 7. (6,4,4,2): size-2 R+B=14 ≥7. (7,3,3,3): size-3 neighbors (7,3,3) sum 13: 7=7,3+3=6,7+3=10. {7}{3,3}→7+6 ✗. min max 7. (8,3,3,2): size-2 ≥7. (5,5,4,2): size-2 ≥7. (4,4,4,4): 8. (6,4,3,3): 7. 

Let me check (6,4,3,3) more carefully. A(6),B(4),C(3),D(3). 
C: neighbors A(6),B(4),D(3), R+B=13. Best split: {6}{4,3}→6+7 max7; {4}{6,3}→4+9 max9; {3}{6,4}→3+10; {6,4}{3}→10+3; {6,3}{4}→9+4; {4,3}{6}→7+6. Min max = 7. So C cross ≥7.
So (6,4,3,3) gives ≥7. Can we achieve 7? Need all ≤7. 
C: {6}{4,3} → A red, B&D blue (R=6,B=7) or A blue, B&D red (R=7,B=6). 
D: same as C (symmetric): A red, B&C blue or A blue, B&C red.
B: neighbors A(6),C(3),D(3), R+B=12. Best: {6}{3,3}→6+6 max6 ✓. So B: A red, C&D blue or A blue, C&D red.
A: neighbors B(4),C(3),D(3), R+B=10. Need ≤7: easy, {4,3}{3}→7+
