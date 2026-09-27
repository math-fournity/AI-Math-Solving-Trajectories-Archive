# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   The cells of a square $2011 \times 2011$ array are labelled with the integers $1,2,\ldots, 2011^2$, in such a way that every label is used exactly once. We then identify the left-hand and right-hand edges, and then the top and bottom, in the normal way to form a torus (the surface of a doughnut).
Determine the largest positive integer $M$ such that, no matter which labelling we choose, there exist two neighbouring cells with the difference of their labels at least $M$.
(Cells with coordinates $(x,y)$ and $(x',y')$ are considered to be neighbours if $x=x'$ and $y-y'\equiv\pm1\pmod{2011}$, or if $y=y'$ and $x-x'\equiv\pm1\pmod{2011}$.)

[i](Romania) Dan Schwarz[/i]       — 题目文本
#   To solve this problem, we need to determine the largest positive integer \( M \) such that, no matter how we label the cells of a \( 2011 \times 2011 \) array with the integers \( 1, 2, \ldots, 2011^2 \), there exist two neighboring cells with the difference of their labels at least \( M \).

1. **Understanding the Problem:**
   - We have a \( 2011 \times 2011 \) grid.
   - Each cell is labeled with a unique integer from \( 1 \) to \( 2011^2 \).
   - The grid is wrapped around to form a torus, meaning the left edge is connected to the right edge, and the top edge is connected to the bottom edge.
   - Two cells are neighbors if they share a side.

2. **Neighboring Cells:**
   - For a cell at \((x, y)\), its neighbors are:
     - \((x, y+1)\) and \((x, y-1)\) (modulo 2011 for the y-coordinate).
     - \((x+1, y)\) and \((x-1, y)\) (modulo 2011 for the x-coordinate).

3. **Objective:**
   - We need to find the largest \( M \) such that there are always two neighboring cells with a difference in their labels of at least \( M \).

4. **Key Insight:**
   - The maximum difference between any two labels is \( 2011^2 - 1 \).
   - We need to ensure that the difference between the labels of any two neighboring cells is maximized.

5. **Bounding the Difference:**
   - Consider the worst-case scenario where the labels are as evenly distributed as possible.
   - If we label the cells in a way that minimizes the difference between neighboring cells, the difference between the highest and lowest labels in any \( 2 \times 2 \) block should be minimized.

6. **Calculating the Bound:**
   - In a \( 2011 \times 2011 \) grid, there are \( 2011^2 \) cells.
   - The average difference between labels of neighboring cells can be approximated by considering the total range of labels divided by the number of cells.
   - The total range is \( 2011^2 - 1 \).

7. **Optimal Labeling:**
   - If we label the cells in a snake-like pattern (row-wise or column-wise), the difference between neighboring cells can be controlled.
   - However, due to the toroidal nature, the difference between the highest and lowest labels in any \( 2 \times 2 \) block will be significant.

8. **Conclusion:**
   - The largest possible difference \( M \) such that there are always two neighboring cells with a difference of at least \( M \) is \( 2 \times 2011 - 1 = 4021 \).

The final answer is \( \boxed{4021} \).  — 标准解答
#   Let me solve this problem. It's a torus labeling problem. We have a 2011×2011 torus, cells labeled 1 to 2011². We need to find the largest M such that no matter the labeling, there exist two neighboring cells with label difference at least M.

This is a classic competition problem. Let me think about it.

The answer should be related to the structure. Let me think about the general approach.

We have n×n torus (n=2011), labels 1 to n². Each cell has 4 neighbors. We want to find the maximum M such that in any labeling, some adjacent pair has difference ≥ M.

Upper bound (constructive): We need to construct a labeling where all adjacent differences are ≤ some value. This gives an upper bound on M.

Lower bound: We need to show that in any labeling, some adjacent pair has difference ≥ M.

Let me think about the lower bound first. Consider the cells labeled 1, 2, ..., k for some k. These k cells form a set S. The boundary of S (cells in S adjacent to cells not in S) — actually, let me think differently.

Consider the values. Sort cells by label. Consider the cell with label 1 and the cell with label n². The difference is n²-1. But they might not be adjacent.

Key idea: Consider the "level sets". For each threshold t, consider S_t = {cells with label ≤ t}. As t goes from 1 to n², S_t grows from empty to full. 

Actually, let me think about this more carefully using the standard approach for such problems.

The standard approach: Consider a path on the torus. The torus graph has n² vertices and 2n² edges (each vertex has degree 4, so 2n² edges). 

Lower bound approach: Consider the set of cells with labels in {1, 2, ..., m} and the set with labels in {n²-m+1, ..., n²}. If these two sets are "far apart" in some sense... 

Actually, let me think about the isoperimetric approach. 

Consider the cells labeled 1, 2, ..., k. Call this set A_k. The edge boundary of A_k consists of edges between A_k and its complement. Each such edge connects a cell with label ≤ k to a cell with label > k, so the difference is at least 1 (not helpful directly).

Let me think about it differently. Consider the maximum label difference across all edges. We want to show this is at least M for any labeling, and construct a labeling achieving exactly M (or close).

Let me think about the upper bound (construction). 

On a torus, we can try to label cells so that adjacent cells have small differences. One natural construction: label cells in a "snake" pattern. But on a torus, the snake must close up.

Actually, let me think about what the answer likely is. For an n×n torus, I believe the answer is n² - 1... no, that's too large. 

Let me think about small cases. For n=2, we have a 2×2 torus. Each cell is adjacent to every other cell (since on a 2×2 torus, each cell's 4 neighbors are the other 3 cells, with one repeated). Actually on a 2×2 torus, cell (0,0) has neighbors (1,0), (0,1), (1,0) [wrapping], (0,1) [wrapping]. So neighbors are (1,0) and (0,1). And (1,1) has neighbors (0,1) and (1,0). So the graph is a 4-cycle: (0,0)-(1,0)-(1,1)-(0,1)-(0,0). 

Labels 1,2,3,4 on a 4-cycle. We want to minimize the maximum edge difference. Best arrangement: 1,2,4,3 around the cycle gives differences 1,2,1,2. Or 1,3,4,2 gives 2,1,2,1. Or 1,2,3,4 gives 1,1,1,3. The minimum maximum is 2 (achieved by 1,2,4,3 or 1,3,4,2 etc). So M=2 for n=2. Note n²-1 = 3, and 2 = ... hmm. n=2, M=2. 

For n=3: 3×3 torus, 9 cells, 18 edges. This is more complex. Let me think about the general structure.

Actually, let me recall: I think this is a known competition problem (Romania, Dan Schwarz). The answer for n×n torus should be... let me derive it.

Key insight: Consider the "band" structure. On the torus, consider horizontal lines (rows). Each row is a cycle of length n. 

Lower bound: Consider the cells with labels 1 through n. These n cells are somewhere on the torus. Consider the cells with labels n²-n+1 through n². These n cells are somewhere. 

Hmm, let me think about a cleaner approach.

Approach via paths: On the torus, consider any Hamiltonian path. The labels along the path go from some value to another. The sum of absolute differences along the path is at least n²-1 (telescoping from min to max label along the path... no, that's not right either).

Actually, let me think about the "discrete intermediate value" approach.

Consider the function f: cells → labels. Consider a horizontal cycle (a row). The labels along this cycle of length n. The maximum difference between adjacent cells on this cycle is at least... well, if we look at all n rows, the labels 1 to n² are distributed.

Let me think about the problem more carefully.

Lower bound: I'll use the following approach. Consider the set L = {cells with labels 1, ..., n²-n} and H = {cells with labels n²-n+1, ..., n²}. |L| = n²-n, |H| = n.

Claim: There must be an edge between L and H where the difference is large. Actually, every edge between L and H has difference at least 1 (since max of L is n²-n and min of H is n²-n+1). But we want a larger bound.

Hmm, let me think differently.

Better approach: Consider labeling the torus. Look at all horizontal edges (edges between (x,y) and (x+1,y)). There are n² such edges (n rows, each a cycle of n edges, but wait—each row has n edges, and there are n rows, so n² horizontal edges). Similarly n² vertical edges. Total 2n² edges.

For the lower bound, consider the following: Take the n cells with the smallest labels {1,...,n} and the n cells with the largest labels {n²-n+1,...,n²}. 

Actually, I think the key idea is about "rows" and "columns" and using the pigeonhole principle.

Let me think about it from the perspective of the maximum value M we're trying to find.

Construction (upper bound): We want to arrange labels so that every adjacent pair has difference ≤ M. 

One idea: Fill the torus row by row. Row 0: 1, 2, ..., n. Row 1: n+1, ..., 2n. Etc. Then horizontal differences are 1, but vertical differences are n. Also, the wrap-around in each row: the difference between position n and position 1 in the same row is n-1. And the vertical wrap-around: row n-1 to row 0, difference is n²-n - 1 = n(n-1)-1. That's huge.

So this naive construction doesn't work well because of wrap-around.

Better construction: We need to handle the toroidal wrap-around. 

Idea: Use a "diagonal" filling. Label cell (i,j) with value i*n + j + 1 but with some modular arithmetic to handle wrap-around.

Actually, let me think about what construction minimizes the maximum edge difference on a torus.

Consider the labeling where cell (i,j) gets label (i*n + j mod n²) + 1. This is the same as row-by-row. The wrap-around issues remain.

Alternative: Think of the torus as Z_n × Z_n. We want a bijection f: Z_n × Z_n → {1, ..., n²} such that |f(u) - f(v)| is small for all edges uv.

Consider f(i,j) = (a*i + b*j) mod n² + 1 for some constants a, b. For this to be a bijection, we need... well, it's a map from Z_n × Z_n to Z_{n²}. This is a bijection iff... it's complicated.

Let me think about the problem differently. 

I recall that for this type of problem on a torus, the answer involves n²/2 or similar. Let me think about the lower bound more carefully.

Lower bound argument: 

Consider the n cells with labels {1, 2, ..., n} (the "low" set) and the n cells with labels {n²-n+1, ..., n²} (the "high" set). The difference between any low label and any high label is at least n² - 2n + 1 = (n-1)².

Now, on the torus, consider any path from a low cell to a high cell. Along this path, there must be an edge where the label "jumps" from ≤ some value to ≥ some value. 

But we need to be more careful. Let me think about the structure.

Actually, here's a cleaner approach. Consider the set S = {cells with labels 1, ..., k} for some k to be determined. The edge boundary ∂S consists of edges between S and V\S. Each such edge (u,v) with u ∈ S, v ∉ S has f(u) ≤ k < f(v), so the difference f(v) - f(u) ≥ 1. But we can say more: f(v) - f(u) ≥ f(v) - k. 

Hmm, this isn't directly giving us what we want. Let me think about the "maximum difference" more carefully.

Let me reconsider. Let D = max over all edges of |f(u) - f(v)|. We want to find the minimum possible D over all labelings, and that minimum is M (the largest M that works for all labelings).

Wait, re-reading: "Determine the largest positive integer M such that, no matter which labelling we choose, there exist two neighbouring cells with the difference of their labels at least M."

So M = min over all labelings of (max over all edges of |difference|). We want to find this M.

Lower bound on M: Show that for any labeling, max edge difference ≥ M.
Upper bound on M: Exhibit a labeling where max edge difference = M (or ≤ M).

Let me think about the lower bound. 

Consider the cells sorted by label: c_1, c_2, ..., c_{n²} where f(c_i) = i. 

Consider the "graph distance" on the torus. The diameter of the n×n torus is... for odd n, it's 2·⌊n/2⌋ = n-1 (since n=2011 is odd, the distance in each coordinate is at most (n-1)/2, so diameter is n-1).

Now, consider c_1 (label 1) and c_{n²} (label n²). The graph distance between them is at most n-1 (diameter). Consider a shortest path c_1 = v_0, v_1, ..., v_d = c_{n²} where d ≤ n-1. Along this path, the labels go from 1 to n². By telescoping (or rather, by the max jump), there exists an edge on this path where the label difference is at least (n²-1)/d ≥ (n²-1)/(n-1) = n+1.

So M ≥ n+1 = 2012.

But can we do better? Let me think about whether we can get a larger lower bound.

Actually, we can use more than just the two extreme cells. Consider c_1 and c_{n²}. But also consider the structure more carefully.

Let me think about the upper bound. Can we achieve max edge difference = n+1?

Construction attempt: We want to label the n×n torus so that every edge has difference ≤ n+1 (or some value close to n).

Hmm, let me think about the "diagonal" construction. Consider labeling cell (i,j) with f(i,j) = ((i + j) mod n) · n + ((i) mod n) + 1 or something like that.

Actually, let me think about a simpler construction. Consider the "snake" that goes diagonally.

Let me think about the labeling f(i,j) = (i·n + j) but arranged to minimize wrap-around issues.

Actually, here's an idea. Consider the map f(i,j) = (i + j·n) mod n² + 1... no, let me think more carefully.

Let me consider a different approach. Think of the torus as having rows and columns. 

Construction: Label cell (i, j) with value v(i,j) = ((j - i) mod n) · n + i + 1.

Wait, let me think about what properties we want. We want:
- Horizontal neighbors (i,j) and (i, j+1): small difference
- Vertical neighbors (i,j) and (i+1, j): small difference
- Wrap-around: (i, n-1) and (i, 0): small difference; (n-1, j) and (0, j): small difference.

Consider the labeling v(i,j) = (i mod n) · n + (j mod n) + 1, i.e., standard row-by-row. Horizontal edges: difference 1 (except wrap: difference n-1). Vertical edges: difference n (except wrap: difference n²-n). The vertical wrap-around gives difference n²-n which is huge. So this doesn't work.

The issue is the vertical wrap-around. To fix this, we need the bottom row and top row to have similar labels.

Idea: Use a "diagonal" arrangement. v(i,j) = ((i + j) mod n²) ... no.

Let me think about v(i,j) = ((a·i + b·j) mod n²) for suitable a, b. For this to be a bijection from Z_n × Z_n to Z_{n²}, we need... actually Z_n × Z_n has n² elements and Z_{n²} has n² elements, but the map (i,j) → ai + bj mod n² needs to be a bijection. This requires that the map is injective. 

For n prime (2011 is prime!), Z_n × Z_n ≅ Z_n × Z_n, and we can embed into Z_{n²}. Actually, since n is prime, by CRT, Z_{n²} is not isomorphic to Z_n × Z_n (since n² is not coprime to n). So a linear map mod n² won't directly give a bijection from Z_n × Z_n.

Let me think differently. 

Consider the labeling v(i,j) = ((i + j) mod n) · n + ((i + 2j) mod n) + 1. Since n is prime and 1, 2 are "independent" in some sense... actually, the map (i,j) → ((i+j) mod n, (i+2j) mod n) is a bijection on Z_n × Z_n (since the matrix [[1,1],[1,2]] has determinant 1, which is nonzero mod n). So this gives a bijection to {0,...,n-1} × {0,...,n-1}, and then v(i,j) = first_coord · n + second_coord + 1 is a bijection to {1,...,n²}.

Now let's compute edge differences:
- Horizontal: (i,j) → (i, j+1). First coord changes by +1 mod n, second coord changes by +2 mod n.
  - If no wrap in first coord: first coord +1, so v changes by n. Second coord changes by +2 mod n.
    - If no wrap in second: v changes by n + 2.
    - If wrap in second (j+2 ≥ n, i.e., j ≥ n-1, but j+1 is the neighbor so j ranges 0..n-1 and we look at j→j+1 mod n): second coord goes from (i+2j) mod n to (i+2(j+1)) mod n = (i+2j+2) mod n. Wrap happens when i+2j+2 ≥ n, i.e., the second coord wraps. In that case, the change is n + 2 - n = n + 2 - n... wait, let me be more careful.

  v(i,j) = ((i+j) mod n) · n + ((i+2j) mod n) + 1.
  v(i, j+1) = ((i+j+1) mod n) · n + ((i+2j+2) mod n) + 1.
  
  Let a = (i+j) mod n, b = (i+2j) mod n.
  Then v(i,j) = a·n + b + 1.
  v(i,j+1) = ((a+1) mod n) · n + ((b+2) mod n) + 1.
  
  Case 1: a < n-1 and b < n-2 (no wraps): v(i,j+1) = (a+1)·n + (b+2) + 1. Difference = n + 2.
  Case 2: a < n-1 and b ≥ n-2 (b = n-2 or n-1): 
    - b = n-2: (b+2) mod n = 0. v(i,j+1) = (a+1)·n + 0 + 1. v(i,j) = a·n + (n-2) + 1 = a·n + n - 1. Difference = (a+1)·n + 1 - (a·n + n - 1) = n + 1 - n + 1 = 2. Wait: (a+1)·n + 1 - a·n - n + 1 = an + n + 1 - an - n + 1 = 2. So difference = 2.
    - b = n-1: (b+2) mod n = 1. v(i,j+1) = (a+1)·n + 1 + 1 = (a+1)·n + 2. v(i,j) = a·n + n - 1 + 1 = a·n + n. Difference = (a+1)·n + 2 - a·n - n = 2.
  Case 3: a = n-1 and b < n-2: (a+1) mod n = 0. v(i,j+1) = 0·n + (b+2) + 1 = b + 3. v(i,j) = (n-1)·n + b + 1 = n² - n + b + 1. Difference = |b + 3 - n² + n - b - 1| = |2 + n - n²| = n² - n - 2. That's huge!

So this construction has a huge difference when a = n-1 (the first coordinate wraps). This is the same wrap-around problem.

The fundamental issue: on a torus, any "linear" labeling will have wrap-around issues in at least one direction.

Let me reconsider. The key difficulty is the toroidal structure—both directions wrap around.

Let me think about the lower bound more carefully, and also think about what the answer should be.

Lower bound refinement: Instead of just using c_1 and c_{n²}, let me use multiple pairs.

Consider the n cells in the first "row" of the labeling—no, that doesn't make sense since the labeling is arbitrary.

Let me think about it using the concept of "cuts" or "level sets."

For each t from 1 to n²-1, define S_t = {cells with label ≤ t}. The edge boundary ∂S_t is the set of edges between S_t and V \ S_t. 

For each edge e = (u,v) in ∂S_t with f(u) ≤ t < f(v), the difference |f(u) - f(v)| ≥ 1, but more importantly, if we sum over all t, each edge (u,v) with f(u) < f(v) contributes to ∂S_t for t = f(u), f(u)+1, ..., f(v)-1, i.e., it contributes |f(u) - f(v)| times.

So: ∑_{t=1}^{n²-1} |∂S_t| = ∑_{edges (u,v)} |f(u) - f(v)|.

Now, the total number of edges is 2n². If the maximum edge difference is D, then the sum is at most 2n² · D. So D ≥ (∑ |∂S_t|) / (2n²).

We need a lower bound on ∑ |∂S_t|. For this, we need a lower bound on |∂S_t| for each t, which relates to the isoperimetric problem on the torus.

The edge isoperimetric inequality on the n×n torus: for a set S with |S| = s, the edge boundary |∂S| ≥ ... 

On the torus Z_n × Z_n, the edge isoperimetric inequality is known. For a set of size s, the minimum edge boundary is related to the structure of S. 

Actually, let me think about this differently. The sum ∑_{t=1}^{n²-1} |∂S_t| can be bounded below using the fact that the "conductance" of the torus is bounded.

Hmm, this is getting complicated. Let me think about the problem from the answer's perspective.

For the n×n torus with n odd, I believe the answer is M = n² - n + 1 or something related. Wait, let me reconsider.

Actually, let me reconsider the lower bound. We showed M ≥ n+1 using the diameter argument. Can we do better?

Consider c_1, c_2, ..., c_{n²} sorted by label. Consider the graph distance d(c_i, c_j) on the torus. 

For any i < j, there's a path from c_i to c_j of length at most diam = n-1. Along this path, the max label difference on any edge is at least (j - i)/(n-1). So the max edge difference D ≥ (j-i)/(n-1) for all i < j. Taking j - i = n² - 1, we get D ≥ (n²-1)/(n-1) = n+1.

But we can potentially do better by considering multiple paths or a more global argument.

Consider the following: take the labels 1, 2, ..., n². For each consecutive pair (c_i, c_{i+1}), the graph distance d(c_i, c_{i+1}) could be anything from 1 to n-1. If d(c_i, c_{i+1}) = 1, then the edge (c_i, c_{i+1}) has difference 1. If d(c_i, c_{i+1}) > 1, then we need to go through intermediate cells.

Hmm, let me think about a different lower bound approach.

Consider the n cells with the smallest labels: {c_1, ..., c_n} (labels 1 to n). And the n cells with the largest labels: {c_{n²-n+1}, ..., c_{n²}} (labels n²-n+1 to n²).

The minimum label difference between these two sets is (n²-n+1) - n = n² - 2n + 1 = (n-1)².

Now, on the torus, consider the "separation" between these two sets. If there's a path from a low cell to a high cell of length ℓ, then along this path, some edge has difference ≥ (n-1)²/ℓ. The shortest such path has length at most... well, it depends on the arrangement.

But actually, we can be smarter. Consider all edges between the "low half" and "high half" of the labels.

Let me try a different approach. Consider the set A = {cells with labels 1, ..., n²/2} (roughly half). The edge boundary of A has some size. Each edge in the boundary connects a cell with label ≤ n²/2 to one with label > n²/2. The difference on such an edge is at least 1, but could be up to n²/2.

Hmm, I think I need to be more clever. Let me look at this from the construction side to guess the answer.

Construction for upper bound: Let me think about what labeling could achieve a small maximum edge difference.

Key insight: On a torus, we can use a "space-filling curve" type approach, but the wrap-around is the issue.

Let me consider the following construction for odd n. Label the torus using a "knight's move" pattern or a pattern that spreads consecutive labels far apart.

Wait, actually, we want consecutive labels to be CLOSE, not far apart. We want to minimize the maximum edge difference, so we want labels that are close in value to be on adjacent cells.

So we want a Hamiltonian path (or cycle) on the torus where consecutive cells in the path get consecutive labels, and the path uses only edges of the torus. If such a Hamiltonian cycle exists, then the max edge difference along the cycle is 1, but the non-cycle edges could have large differences.

The torus n×n (n odd) does have a Hamiltonian cycle. If we label along a Hamiltonian cycle, the cycle edges have difference 1, but the other edges (the "chords") could have large differences. There are 2n² edges total and n² cycle edges, so n² non-cycle edges. These non-cycle edges connect cells that could be far apart in the cycle, hence have large label differences.

So the Hamiltonian cycle approach gives max edge difference = max over non-cycle edges of |difference|, which could be up to n²-1 in the worst case. Not good.

Let me think about this more carefully. 

Actually, I think the answer is n+1. Let me verify this with the n=2 case: n+1 = 3, but we computed M=2 for n=2. So either the answer isn't n+1, or the n=2 case is special (since n=2 is even and the torus structure is different).

Wait, for n=2, the diameter is 1 (every cell is adjacent to every other cell in the 2×2 torus, since the graph is a 4-cycle but with the torus structure... let me recheck). On the 2×2 torus, cell (0,0) has neighbors (1,0), (0,1), (1,0) [wrapping from (0,-1)=(0,1)], (0,1) [wrapping from (-1,0)=(1,0)]. So the neighbors are (1,0) and (0,1). The graph is a 4-cycle: (0,0)-(1,0)-(1,1)-(0,1)-(0,0). Diameter = 2. So the lower bound gives D ≥ (4-1)/2 = 1.5, so D ≥ 2. And we showed M=2 for n=2. So the bound is tight for n=2!

For n=2, n+1 = 3 but M=2. The diameter is 2 = n, not n-1. For n=2, ⌊n/2⌋ = 1, so diameter = 2·1 = 2 = n. For odd n, diameter = 2·(n-1)/2 = n-1.

So for n=2, the bound gives D ≥ 3/2 → D ≥ 2, and M=2. The bound (n²-1)/diam = 3/2, ceiling is 2. And M=2. So it's tight.

For general odd n, the bound gives D ≥ (n²-1)/(n-1) = n+1. Is this tight? We need a construction achieving D = n+1.

Let me think about whether such a construction exists.

For n=3: M should be 4 if the answer is n+1=4. Let me check if we can label a 3×3 torus with max edge difference 4.

3×3 torus, labels 1-9. We need every edge to have difference ≤ 4.

Let me try:
```
1 2 3
4 5 6
7 8 9
```
Horizontal edges: differences 1, 1, 2 (wrap: 3-1=2). Vertical edges: 3, 3, 3 (wrap: 7-1=6). The vertical wrap gives 6 > 4. Not good.

Let me try a different arrangement:
```
1 5 9
2 6 7
3 4 8
```
Horizontal: |1-5|=4, |5-9|=4, |9-1|=8 (wrap). Bad.

Let me try:
```
1 4 7
5 8 2
9 3 6
```
Horizontal row 0: |1-4|=3, |4-7|=3, |7-1|=6 (wrap). Bad.

The wrap-around is always the problem. Let me think about how to handle it.

For the horizontal wrap in a row: we need the first and last elements of each row to be close. Similarly for vertical.

What if we arrange each row so that it goes up and then comes back down? Like a snake within each row? But on a cycle (which is what each row is), you can't snake—you always have a wrap-around point.

Hmm, let me think about this differently. 

For a cycle of length n with labels being a subset of {1,...,n²}, the minimum possible maximum adjacent difference depends on the labels assigned to that cycle.

Actually, for a cycle of length n with labels a_1 < a_2 < ... < a_n, the minimum max adjacent difference (optimally arranging them on the cycle) is... 

If we arrange them as a_1, a_3, a_5, ..., a_n, a_{n-1}, a_{n-3}, ..., a_2 (or similar zigzag), the max difference is roughly (a_n - a_1) / (n/2) ≈ 2(a_n - a_1)/n.

Wait, for a cycle, the optimal arrangement to minimize max adjacent difference: arrange the sorted values as a_1, a_2, ..., a_n around the cycle. The differences are a_2-a_1, a_3-a_2, ..., a_n - a_{n-1}, and a_n - a_1 (wrap). The wrap is the biggest. To minimize the max, we should interleave: place them as a_1, a_{⌈n/2⌉+1}, a_2, a_{⌈n/2⌉+2}, ..., which gives max difference roughly (a_n - a_1)/⌈n/2⌉.

This is getting complicated. Let me think about the problem from a higher level.

I think the answer is M = n+1 for odd n, and the construction involves a clever arrangement. Let me think about the construction.

Construction idea: Use the fact that n is odd. Consider the labeling:
v(i, j) = ((i + j·(n+1)/2) mod n) · n + i + 1

Wait, I need to think about this more carefully. Let me consider a different approach.

Since n is odd, (n+1)/2 is an integer. Consider the "diagonal" labeling:

v(i, j) = ((j - i·(n-1)/2) mod n) · n + ((i + j) mod n) + 1

Hmm, this is getting complicated. Let me think about what we need.

We need a bijection f: Z_n × Z_n → {1, ..., n²} such that:
1. |f(i, j) - f(i, j±1)| ≤ D for all i, j (horizontal edges)
2. |f(i±1, j) - f(i, j)| ≤ D for all i, j (vertical edges)

And we want D = n+1.

Let me try the construction f(i,j) = ((i + j) mod n) · n + ((i - j) mod n) + 1.

Check bijection: The map (i,j) → ((i+j) mod n, (i-j) mod n). The matrix is [[1, 1], [1, -1]] with determinant -2. Since n is odd, 2 is invertible mod n, so this is a bijection on Z_n × Z_n. Good.

Now, f(i,j) = a·n + b + 1 where a = (i+j) mod n, b = (i-j) mod n.

Horizontal edge (i, j) → (i, j+1):
a' = (i + j + 1) mod n = (a + 1) mod n
b' = (i - j - 1) mod n = (b - 1) mod n

f(i,j+1) - f(i,j) = [(a+1 mod n) - a] · n + [(b-1 mod n) - b]

If a < n-1 and b > 0: difference = n - 1.
If a < n-1 and b = 0: difference = n + (n-1) = 2n - 1. Bad!
If a = n-1 and b > 0: difference = -n·(n-1) + ... wait let me recompute.

a = n-1: a' = 0. So (a'-a) = 0 - (n-1) = -(n-1). Contribution: -(n-1)·n.
b > 0: b' = b-1. Contribution: -1.
Total: -(n-1)·n - 1 = -(n²-n) - 1. Absolute value: n² - n + 1. That's huge.

So this construction also has the wrap-around problem. The issue is that when a wraps from n-1 to 0, the value jumps by n² - n.

The fundamental problem: any labeling of the form v = a·n + b where a and b are linear functions of (i,j) will have wrap-around issues when a crosses the n-1 → 0 boundary.

To avoid this, we need a more sophisticated construction where the "high-order" coordinate doesn't wrap around at the same time as we traverse an edge.

Idea: Use a construction where the "row" index changes slowly. 

Consider the labeling where we traverse the torus in a "diagonal snake" pattern. 

Actually, let me think about this problem differently. Let me consider the problem on a path graph first (no wrap-around), then on a cycle, then on the torus.

On a path of n² vertices: label them 1, 2, ..., n² in order. Max edge difference = 1. Easy.

On a cycle of n² vertices: label them 1, 2, ..., n² in order. The wrap-around edge has difference n²-1. To minimize, use the zigzag: 1, n²/2+1, 2, n²/2+2, ..., n²/2, n². Max difference ≈ 2. Actually for a cycle of m vertices with labels 1..m, the minimum max adjacent difference is ⌈m/2⌉... no. 

For a cycle of m vertices with labels 1, 2, ..., m, the minimum possible maximum adjacent difference is ⌈(m-1)/⌊m/2⌋⌉... let me think. We need to arrange 1, ..., m on a cycle minimizing the max adjacent difference. 

The optimal arrangement: 1, 1+k, 1+2k, ... where k = ⌈m/2⌉. For m even: 1, m/2+1, 2, m/2+2, ..., m/2, m. Differences: m/2, m/2-1, m/2, m/2-1, ..., m/2, m/2-1, and the wrap: m - 1 = m-1. Hmm, that's not right.

Let me think again. For a cycle with labels 1, ..., m, arrange as: 1, ⌊m/2⌋+1, 2, ⌊m/2⌋+2, 3, ⌊m/2⌋+3, ..., ⌊m/2⌋, m, ⌊m/2⌋-1+1, ... 

Actually, the standard result: for a cycle of m vertices labeled 1 to m, the minimum max adjacent difference is ⌈m/2⌉. The arrangement is: 1, 1+⌈m/2⌉, 2, 2+⌈m/2⌉, 3, ... (interleaving the lower half and upper half). For m odd, ⌈m/2⌉ = (m+1)/2.

For m = n² with n odd, ⌈n²/2⌉ = (n²+1)/2. So on a Hamiltonian cycle of the torus, the minimum max adjacent difference would be (n²+1)/2, which is much larger than n+1. So the Hamiltonian cycle approach is bad.

This suggests that we shouldn't just use a Hamiltonian cycle—we need to use the 2D structure of the torus.

Let me reconsider. The torus has 2n² edges, and we're labeling n² vertices. The key is that the torus is 2-dimensional, not 1-dimensional.

Let me think about the construction more carefully.

Construction for D = n+1 on the n×n torus (n odd):

Consider the labeling v(i, j) = ((i · (n+1)/2 + j) mod n²) + 1.

Wait, this is a map from Z_n × Z_n to Z_{n²}. For it to be a bijection, we need i · (n+1)/2 + j to take all values 0, 1, ..., n²-1 exactly once as (i,j) ranges over Z_n × Z_n.

The values taken are: for each i ∈ {0,...,n-1} and j ∈ {0,...,n-1}, the value is i·(n+1)/2 + j mod n². 

For fixed i, as j ranges over 0..n-1, we get the values i·(n+1)/2, i·(n+1)/2 + 1, ..., i·(n+1)/2 + n-1 (mod n²). These are n consecutive values.

For different i, these blocks are: {i·(n+1)/2, ..., i·(n+1)/2 + n-1} for i = 0, 1, ..., n-1.

The blocks start at positions 0, (n+1)/2, 2(n+1)/2, 3(n+1)/2, ..., (n-1)(n+1)/2.

The start positions are 0, (n+1)/2, n+1, 3(n+1)/2, ..., (n-1)(n+1)/2 = (n²-1)/2.

Each block has length n. The gap between consecutive start positions is (n+1)/2. Since (n+1)/2 < n (for n ≥ 3), the blocks overlap! So this is NOT a bijection.

Let me try a different approach. 

Construction: v(i, j) = (i · n + j) mod n² + 1, but with a twist to handle wrap-around.

Actually, the standard row-by-row labeling v(i,j) = i·n + j + 1 has:
- Horizontal edges: difference 1 (except wrap: n-1)
- Vertical edges: difference n (except wrap: n²-n)

The problem is the vertical wrap (n²-n) and to a lesser extent the horizontal wrap (n-1).

What if we "shift" each row to handle the vertical wrap? 

Consider v(i, j) = (i·n + (j + s·i) mod n) + 1 where s is a shift parameter. This is a bijection (for each i, j → (j + s·i) mod n is a bijection on Z_n, and different i give different blocks of n values).

Horizontal edges: (i, j) → (i, j+1). v changes by 1 (if no wrap in j+s·i) or by 1-n (if wrap). So horizontal differences are 1 or n-1.

Vertical edges: (i, j) → (i+1, j). 
v(i, j) = i·n + (j + s·i) mod n + 1.
v(i+1, j) = (i+1)·n + (j + s·(i+1)) mod n + 1 = (i+1)·n + (j + s·i + s) mod n + 1.

Let b = (j + s·i) mod n. Then v(i,j) = i·n + b + 1.
v(i+1, j) = (i+1)·n + (b + s) mod n + 1.

If b + s < n: v(i+1,j) = (i+1)·n + b + s + 1 = i·n + n + b + s + 1. Difference = n + s.
If b + s ≥ n: v(i+1,j) = (i+1)·n + b + s - n + 1 = i·n + b + s + 1. Difference = s.

So vertical differences are n + s or s. To minimize the maximum, we want n + s to be small, so s should be small (or negative). But s ≥ 0 (it's a shift). If s = 0, we get the standard row-by-row with vertical differences n (except wrap). If s = 1, vertical differences are n+1 or 1.

With s = 1:
- Horizontal: 1 or n-1
- Vertical: n+1 or 1
- Vertical wrap (i = n-1 → i = 0): v(n-1, j) = (n-1)·n + (j + n-1) mod n + 1 = n² - n + (j-1) mod n + 1. v(0, j) = 0·n + j + 1 = j + 1. 
  Difference = |j + 1 - n² + n - ((j-1) mod n) - 1| = |j - n² + n - (j-1 mod n)|.
  If j > 0: (j-1) mod n = j-1. Difference = |j - n² + n - j + 1| = |n - n² + 1| = n² - n - 1. Huge!

So the vertical wrap-around is still a problem. The issue is that the last row and first row have very different label ranges.

To fix the vertical wrap, we need the last row and first row to have interleaved labels. This requires a more fundamental change to the construction.

Idea: Instead of filling row by row, fill in a "diagonal" order. 

Consider the labeling v(i, j) = ((i + j) mod n) · n + ((j - i·⌊n/2⌋) mod n) + 1... this is getting too complicated without more structure.

Let me try a completely different approach. 

Think of the torus as Z_n × Z_n. Consider the labeling:
v(i, j) = ((i + j) mod n²) + 1? No, this isn't a bijection since (i+j) only takes values 0 to 2(n-1), not 0 to n²-1.

OK let me think about this more carefully. We need a bijection from Z_n × Z_n to {1, ..., n²}. 

Since n is prime (2011 is prime), Z_n × Z_n is a 2-dimensional vector space over Z_n, and we can use linear algebra.

Consider the map φ: Z_n × Z_n → Z_n × Z_n given by (i, j) → (a₁i + b₁j, a₂i + b₂j) mod n, where the matrix [[a₁, b₁], [a₂, b₂]] is invertible mod n. Then v(i,j) = first_coord · n + second_coord + 1 is a bijection to {1, ..., n²}.

The edge differences depend on the matrix. Let's compute.

For a horizontal edge (i,j) → (i, j+1):
Δfirst = b₁, Δsecond = b₂ (mod n).
If no wrap: difference = b₁ · n + b₂.
If first wraps (depends on current value): difference involves ±n².

The wrap-around issue is fundamental for any linear map. When the first coordinate wraps from n-1 to 0, the value jumps by ±(n²-n).

So linear maps always have this problem. We need a non-linear construction.

Let me think about this differently. 

Maybe the answer is not n+1 but something larger. Let me reconsider the lower bound.

Better lower bound: Consider the cells labeled 1, 2, ..., n (call this set A) and cells labeled n²-n+1, ..., n² (call this set B). |A| = |B| = n. The label difference between any cell in A and any cell in B is at least n² - 2n + 1 = (n-1)².

Now, on the torus, consider the "distance" between A and B. If A and B are far apart, then any path from A to B is long, and the label difference accumulates. If A and B are close (some cell in A is adjacent to some cell in B), then we directly get a large edge difference.

Case 1: Some cell in A is adjacent to some cell in B. Then that edge has difference ≥ (n-1)². Since (n-1)² > n+1 for n ≥ 4, this gives a much better bound.

Case 2: A and B are not adjacent. Then the distance between A and B is at least 2. But we can say more.

Actually, this isn't quite right. The difference between a cell in A (label ≤ n) and a cell in B (label ≥ n²-n+1) is at least n²-2n+1. But if they're not adjacent, we need to find a path and use the intermediate cells.

Hmm, but the intermediate cells have labels between n+1 and n²-n, which could be anything. So the path from A to B might go through cells with labels that gradually increase, and the max edge difference on the path could be small.

So this approach doesn't directly give a better bound. The issue is that the labels could increase gradually along a path from A to B.

Let me reconsider. The lower bound of n+1 from the diameter argument seems hard to beat with simple arguments. Let me think about whether n+1 is actually the answer.

Let me try to construct a labeling with max edge difference n+1 for small n, say n=3.

For n=3, we need max edge difference ≤ 4. The 3×3 torus has 9 cells and 18 edges.

Let me try to find such a labeling by trial.

The cells are (i,j) for i,j ∈ {0,1,2}. Each cell has 4 neighbors.

Let me try:
```
Position (0,0)=1  (0,1)=2  (0,2)=3
Position (1,0)=5  (1,1)=6  (1,2)=4
Position (2,0)=9  (2,1)=7  (2,2)=8
```

Horizontal edges:
Row 0: |1-2|=1, |2-3|=1, |3-1|=2 (wrap)
Row 1: |5-6|=1, |6-4|=2, |4-5|=1 (wrap)
Row 2: |9-7|=2, |7-8|=1, |8-9|=1 (wrap)

Vertical edges:
Col 0: |1-5|=4, |5-9|=4, |9-1|=8 (wrap). BAD! 8 > 4.

The vertical wrap is the problem again. Let me try to make the first and last rows closer.

```
Position (0,0)=1  (0,1)=2  (0,2)=4
Position (1,0)=6  (1,1)=5  (1,2)=3
Position (2,0)=7  (2,1)=9  (2,2)=8
```

Horizontal:
Row 0: |1-2|=1, |2-4|=2, |4-1|=3
Row 1: |6-5|=1, |5-3|=2, |3-6|=3
Row 2: |7-9|=2, |9-8|=1, |8-7|=1

Vertical:
Col 0: |1-6|=5. BAD! 5 > 4.

Let me try yet another arrangement. The challenge is balancing both directions and both wrap-arounds.

```
Position (0,0)=1  (0,1)=3  (0,2)=5
Position (1,0)=4  (1,1)=6  (1,2)=8
Position (2,0)=7  (2,1)=9  (2,2)=2
```

Horizontal:
Row 0: |1-3|=2, |3-5|=2, |5-1|=4
Row 1: |4-6|=2, |6-8|=2, |8-4|=4
Row 2: |7-9|=2, |9-2|=7. BAD!

This is tricky. Let me try a more systematic approach.

For n=3, we need all 18 edges to have difference ≤ 4. Labels 1-9.

Let me think about which labels can be adjacent. Label 1 can be adjacent to labels 2, 3, 4, 5 (difference ≤ 4). Label 9 can be adjacent to 5, 6, 7, 8. Label 5 can be adjacent to 1, 2, 3, 4, 6, 7, 8, 9 (all). 

The constraint is that 1 and 9 cannot be adjacent (difference 8 > 4), 1 and 8 cannot be adjacent (7 > 4), 2 and 9 cannot be adjacent (7 > 4), 2 and 8 cannot be adjacent (6 > 4), 1 and 7 cannot be adjacent (6 > 4), 3 and 9 cannot be adjacent (6 > 4), 1 and 6 cannot be adjacent (5 > 4), 4 and 9 cannot be adjacent (5 > 4), 2 and 7 cannot be adjacent (5 > 4), 3 and 8 cannot be adjacent (5 > 4).

So the "forbidden" adjacencies (difference > 4) are:
(1,6), (1,7), (1,8), (1,9), (2,7), (2,8), (2,9), (3,8), (3,9), (4,9).

And by symmetry: (6,1), (7,1), (7,2), (8,1), (8,2), (8,3), (9,1), (9,2), (9,3), (9,4).

Each cell has 4 neighbors on the torus. Cell with label 1 can only be adjacent to {2,3,4,5}. Cell with label 9 can only be adjacent to {5,6,7,8}.

Let me try to construct this. Place 1 at (0,0). Its neighbors are (1,0), (2,0), (0,1), (0,2). These must be from {2,3,4,5}.

Place 9 at some cell not adjacent to 1. The cells not adjacent to 1 are (1,1), (1,2), (2,1), (2,2). Place 9 at (1,1). Its neighbors are (0,1), (2,1), (1,0), (1,2). These must be from {5,6,7,8}.

So the 4 neighbors of 1 are from {2,3,4,5} and the 4 neighbors of 9 are from {5,6,7,8}. The common element is 5. The neighbors of 1 are {(1,0), (2,0), (0,1), (0,2)} and neighbors of 9 are {(0,1), (2,1), (1,0), (1,2)}. Common cells: (0,1) and (1,0).

So (0,1) and (1,0) are neighbors of both 1 and 9. They must be in {2,3,4,5} ∩ {5,6,7,8} = {5}. But both can't be 5. Contradiction! So we can't have both (0,1) and (1,0) be 5.

Wait, actually only one of them needs to be in the intersection. Let me re-examine. (0,1) is a neighbor of 1 (at (0,0)) and a neighbor of 9 (at (1,1)). So (0,1) must be in {2,3,4,5} ∩ {5,6,7,8} = {5}. Similarly, (1,0) is a neighbor of both, so (1,0) must also be 5. But we can't have two cells with label 5. Contradiction!

So placing 1 and 9 at distance 2 (like (0,0) and (1,1)) doesn't work. What if 1 and 9 are at distance 2 but in a different configuration? On the 3×3 torus, distance 2 cells from (0,0) are: (1,1), (1,2), (2,1), (2,2). By the torus symmetry, all are equivalent. So no distance-2 placement works.

What if 1 and 9 are at distance 1 (adjacent)? Then the edge between them has difference 8 > 4. Not allowed.

What if 1 and 9 are at distance 3 = diameter? On the 3×3 torus, the diameter is 2 (since n=3, diameter = n-1 = 2). So the maximum distance is 2. There's no distance-3 pair.

So for n=3, we can't place 1 and 9 at distance > 2, and we've shown distance 2 doesn't work, and distance 1 doesn't work. This means M > 4 for n=3, i.e., M ≥ 5 = n+2.

Wait, let me double-check. For n=3, diameter = 2. The lower bound from diameter gives D ≥ (9-1)/2 = 4. But we just showed D=4 is impossible. So M ≥ 5 for n=3.

Hmm, so the answer is not n+1. Let me reconsider.

Actually wait, I need to recheck my argument. I showed that 1 and 9 can't be placed at distance 2 with max edge difference 4. But maybe I made an error.

Let me recheck: 1 at (0,0), 9 at (1,1). Neighbors of (0,0): (1,0), (2,0), (0,1), (0,2). Neighbors of (1,1): (0,1), (2,1), (1,0), (1,2). The cells (0,1) and (1,0) are neighbors of both. 

(0,1) must have label in {2,3,4,5} (neighbor of 1, so diff ≤ 4, so label ≤ 5) and in {5,6,7,8} (neighbor of 9, so diff ≤ 4, so label ≥ 5). So (0,1) = 5.
(1,0) must have label in {2,3,4,5} and in {5,6,7,8}. So (1,0) = 5. 

But both can't be 5. Contradiction. So indeed D=4 is impossible for n=3.

So M ≥ 5 for n=3. Is M = 5 achievable? Let me check.

With D=5, the forbidden adjacencies (diff > 5) are:
(1,7), (1,8), (1,9), (2,8), (2,9), (3,9).

So 1 can be adjacent to {2,3,4,5,6}, 9 can be adjacent to {4,5,6,7,8}.

Place 1 at (0,0), 9 at (1,1). Common neighbors: (0,1) and (1,0).
(0,1) must be in {2,3,4,5,6} ∩ {4,5,6,7,8} = {4,5,6}.
(1,0) must be in {4,5,6}.
So we need two distinct values from {4,5,6} for (0,1) and (1,0). That's possible.

Let's say (0,1) = 4, (1,0) = 5. 

Remaining: neighbors of 1: (2,0) and (0,2) must be in {2,3,4,5,6}. 4 and 5 are used, so from {2,3,6}.
Neighbors of 9: (2,1) and (1,2) must be in {4,5,6,7,8}. 4 and 5 are used, so from {6,7,8}.

Let (2,0) = 2, (0,2) = 3, (2,1) = 6, (1,2) = 7.
Remaining cells: (2,2) and the remaining labels: 8.
Wait, used so far: 1,4,5,2,3,6,7,9. Remaining: 8. And remaining cell: (2,2).

So (2,2) = 8.

Let me verify all edges:
```
(0,0)=1  (0,1)=4  (0,2)=3
(1,0)=5  (1,1)=9  (1,2)=7
(2,0)=2  (2,1)=6  (2,2)=8
```

Horizontal:
Row 0: |1-4|=3, |4-3|=1, |3-1|=2 (wrap). ✓
Row 1: |5-9|=4, |9-7|=2, |7-5|=2 (wrap). ✓
Row 2: |2-6|=4, |6-8|=2, |8-2|=6 (wrap). ✗! 6 > 5.

The wrap in row 2 gives |8-2| = 6 > 5. Bad.

Let me try different assignments. Let (2,0) = 3, (0,2) = 2, (2,1) = 8, (1,2) = 6.
Remaining: (2,2) = 7.

```
(0,0)=1  (0,1)=4  (0,2)=2
(1,0)=5  (1,1)=9  (1,2)=6
(2,0)=3  (2,1)=8  (2,2)=7
```

Horizontal:
Row 0: |1-4|=3, |4-2|=2, |2-1|=1. ✓
Row 1: |5-9|=4, |9-6|=3, |6-5|=1. ✓
Row 2: |3-8|=5, |8-7|=1, |7-3|=4. ✓

Vertical:
Col 0: |1-5|=4, |5-3|=2, |3-1|=2. ✓
Col 1: |4-9|=5, |9-8|=1, |8-4|=4. ✓
Col 2: |2-6|=4, |6-7|=1, |7-2|=5. ✓

All differences ≤ 5! So D=5 is achievable for n=3. And we showed D=4 is not. So M=5 for n=3.

Now, 5 = n+2 for n=3. But let me check: is the pattern n+2 or something else?

For n=2, M=2 = n. For n=3, M=5 = n+2. Hmm, these don't fit a simple pattern. Let me reconsider.

Wait, for n=2, the torus is a 4-cycle. M=2. n+2 = 4, which doesn't match. So the pattern might be different.

Actually, for n=2, the structure is very different (the torus is just a 4-cycle). Let me focus on odd n.

For n=3, M=5. Let me think about what 5 is in terms of n. 
- n+2 = 5 ✓
- (n²+1)/2 = 5 ✓ (since (9+1)/2 = 5)
- 2n-1 = 5 ✓

All three formulas give 5 for n=3. I need another data point to distinguish.

Let me try n=5. If the answer is n+2 = 7, or (n²+1)/2 = 13, or 2n-1 = 9, these are very different.

Let me think about the lower bound more carefully.

Refined lower bound: Consider cells with labels 1 and n². They're at distance at most d = (n-1)/2 · 2 = n-1 (diameter of the torus for odd n). Along a shortest path of length ≤ n-1, the max edge difference is ≥ (n²-1)/(n-1) = n+1.

But we showed for n=3 that n+1 = 4 is not achievable, and M = 5. So the lower bound of n+1 is not tight. We need a better lower bound.

Let me think about why n+1 fails for n=3. The issue was that 1 and 9 are at distance 2, and they have 2 common neighbors, both of which need to be in a small intersection.

Generalizing: Consider cells with labels 1 and n² on the n×n torus (n odd). They're at distance at most n-1. 

If they're at distance d, consider a shortest path of length d. The max edge difference on this path is ≥ (n²-1)/d. To minimize this, we want d as large as possible, so d = n-1 (diameter). This gives max diff ≥ n+1.

But the issue is more subtle. When 1 and n² are at distance d, the path between them has d edges and d-1 intermediate cells. These intermediate cells have labels between 1 and n², but they also have other neighbors (not on the path) that impose additional constraints.

Let me think about a better lower bound using the structure of the torus.

Alternative lower bound approach: Consider the "level sets" more carefully.

For each k from 1 to n²-1, let S_k = {cells with label ≤ k}. The edge boundary ∂S_k has |∂S_k| edges. 

Key fact: On the n×n torus, for any set S with |S| = s (where 1 ≤ s ≤ n²-1), the edge boundary |∂S| ≥ 2·min(s, n²-s)·... hmm, actually the isoperimetric inequality on the torus is more complex.

Actually, let me think about a specific level set. Consider S = {cells with labels 1, ..., n}. |S| = n. 

On the n×n torus, what is the minimum edge boundary of a set of size n?

A set of n cells on the n×n torus. The minimum edge boundary... If the n cells form a "row" (a cycle of length n), the edge boundary is 2n (each cell has 2 neighbors outside the row, in the vertical direction). If the n cells form a "diagonal" or some other shape, the boundary could be different.

Actually, for a set of n cells forming a path (not a cycle), the boundary would be... each internal cell of the path has 2 neighbors on the path and 2 outside, contributing 2 to the boundary. The 2 endpoints have 1 neighbor on the path and 3 outside, contributing 3 each. Total: 2(n-2) + 2·3 = 2n+2. But if the path wraps around and forms a cycle, the boundary is 2n.

For a "row" (cycle of length n), boundary = 2n. Can we do better? 

Consider n cells forming an L-shape or a square-ish shape. For n = 5, a 2×3 rectangle minus 1 cell = 5 cells. The boundary would be... this is getting complicated.

Let me think about the isoperimetric inequality on the torus more carefully. 

On the n×n torus, the edge isoperimetric function is known. For small sets (|S| ≤ n²/2), the minimum boundary is achieved by sets that are "as round as possible." 

For |S| = n on the n×n torus, the minimum edge boundary is 2n (achieved by a row or column, which is a cycle of length n). 

Wait, is that right? A row is a cycle of length n. Each cell in the row has 2 horizontal neighbors (in the row) and 2 vertical neighbors (outside the row). So the boundary is 2n. Can we do better?

Consider a "ball" of radius r in the torus graph. For n large, a ball of radius r has about 2r² cells and boundary about 4r. For |S| = n, we'd need r ≈ √(n/2), giving boundary ≈ 4√(n/2) ≈ 2√(2n). For large n, this is much less than 2n. So the minimum boundary for |S| = n is NOT 2n; it's closer to O(√n).

Hmm wait, but on the torus, the "ball" might wrap around. For n = 2011, a ball of radius r ≈ √(n/2) ≈ 31 doesn't wrap around, so the boundary is about 4r ≈ 124, much less than 2n = 4022.

So the minimum edge boundary of a set of size n on the n×n torus is O(√n), not 2n. This changes the analysis significantly.

Let me reconsider the lower bound using the sum of boundaries.

∑_{k=1}^{n²-1} |∂S_k| = ∑_{edges} |f(u) - f(v)| ≤ 2n² · D

where D is the max edge difference. So D ≥ (∑ |∂S_k|) / (2n²).

Now, ∑ |∂S_k| depends on the labeling. To get a lower bound on D that works for ALL labelings, we need a lower bound on ∑ |∂S_k| that holds for all labelings.

But ∑ |∂S_k| depends on the labeling (it determines the order in which cells are added to S_k). So we need: for any ordering of the cells, ∑_{k=1}^{n²-1} |∂S_k| ≥ some function of n.

This is related to the "profile" or "pathwidth" of the graph. Specifically, ∑ |∂S_k| is the "vertex isoperimetric profile" summed over all prefixes, which is related to the pathwidth.

Actually, ∑_{k=1}^{n²-1} |∂S_k| is the sum of edge boundaries over all prefixes of the ordering. This is minimized by the ordering that minimizes the maximum boundary (related to pathwidth), but we're summing, not maximizing.

Hmm, this is getting complex. Let me think about it differently.

Actually, let me think about the problem using a different lower bound technique.

Consider the n cells in any row of the torus. These n cells form a cycle of length n. Their labels are some n distinct values from {1, ..., n²}. 

For a cycle of length n with labels a_1 < a_2 < ... < a_n, the minimum possible maximum adjacent difference (over all arrangements on the cycle) is at least (a_n - a_1) / ⌊n/2⌋.

This is because on a cycle of length n, the maximum distance between any two vertices is ⌊n/2⌋. So the labels a_1 and a_n are at cycle-distance at most ⌊n/2⌋, and along the shorter arc, the max jump is at least (a_n - a_1)/⌊n/2⌋.

Now, consider all n rows. The labels are partitioned into n groups of n. Let the range of group i be r_i = max(group i) - min(group i). Then the max edge difference in row i is at least r_i / ⌊n/2⌋ = 2r_i / (n-1) (since n is odd, ⌊n/2⌋ = (n-1)/2).

The sum of ranges: ∑ r_i. Each r_i ≥ n-1 (since each group has n distinct values, the range is at least n-1). But we can say more.

Actually, the sum of ranges depends on how the labels are distributed among rows. In the worst case (for the lower bound), the labels are distributed to minimize the maximum range. If the labels are distributed as evenly as possible, each row gets a contiguous block of n labels, and the range of each row is n-1. Then the max edge difference per row is ≥ 2(n-1)/(n-1) = 2. That's a weak bound.

But we also have columns! Consider both rows and columns.

Hmm, this approach gives weak bounds when labels are distributed evenly among rows.

Let me think about a completely different approach.

Consider the "sorting" perspective. We have n² cells on the torus, labeled 1 to n². Consider the cell with label k. Define its "coordinate" in the sorted order as k. 

Now, think of the labels as defining a function on the torus. The "Lipschitz constant" of this function (max edge difference) is what we want to minimize.

This is related to the problem of embedding a grid into a line (or vice versa) with small distortion. 

Actually, I think the key insight is about the "bandwidth" of the torus graph. The bandwidth of a graph G is the minimum over all labelings of the maximum |f(u) - f(v)| over all edges uv. This is exactly our problem!

The bandwidth of the n×n torus (Cartesian product C_n × C_n) is a known graph theory parameter. Let me recall what it is.

The bandwidth of the n×n grid (P_n × P_n) is n. The bandwidth of the n×n torus (C_n × C_n) should be larger due to the wrap-around.

For the torus C_n × C_n, I believe the bandwidth is 2n - 1 for odd n. Let me check with n=3: 2·3 - 1 = 5. And we found M=5 for n=3. ✓

For n=2: 2·2 - 1 = 3. But we found M=2 for n=2. ✗. Hmm, but n=2 is even and the torus C_2 × C_2 is a multigraph (or has a different structure). Let me recheck n=2.

On the 2×2 torus, the graph is a 4-cycle (as I computed earlier). The bandwidth of a 4-cycle C_4 is 2. And 2n-1 = 3 ≠ 2. So the formula 2n-1 doesn't work for n=2.

But for odd n, the torus C_n × C_n is a 4-regular graph (no multi-edges), and the bandwidth might be 2n-1.

Let me check n=5: if the bandwidth is 2·5-1 = 9, then M = 9 for n=5.

Actually, let me look up the bandwidth of C_n × C_n. I recall that for the Cartesian product of cycles, the bandwidth has been studied.

The bandwidth of C_m × C_n (for m, n ≥ 3) is... I think it's 2·min(m, n) for even min(m,n) and 2·min(m,n) - 1 for odd min(m,n). But I'm not sure.

Actually, I recall that the bandwidth of the n-dimensional torus and grid graphs has been studied by various authors. For C_n × C_n with n odd, the bandwidth is 2n - 1.

Let me verify this with the lower bound. We need to show that for any labeling, some edge has difference ≥ 2n-1.

Lower bound for 2n-1: 

Consider the cells with labels 1, 2, ..., n and the cells with labels n²-n+1, ..., n². 

Hmm, let me think of a cleaner argument.

Consider the cell with label 1 and the cell with label n². They're at distance at most n-1 on the torus. Along a shortest path of length d ≤ n-1, the max edge difference is ≥ (n²-1)/d.

If d = n-1: max diff ≥ (n²-1)/(n-1) = n+1.
If d = (n-1)/2: max diff ≥ (n²-1)/((n-1)/2) = 2(n+1).
If d = 1: max diff ≥ n²-1.

So the lower bound depends on the distance between cells 1 and n². To get a bound of 2n-1, we need (n²-1)/d ≥ 2n-1, i.e., d ≤ (n²-1)/(2n-1) = (n+1)/2 · (n-1)/(n-1/2)... let me compute: (n²-1)/(2n-1) = (n-1)(n+1)/(2n-1). For large n, this is approximately n/2. So we need d ≤ ~n/2.

But the distance between cells 1 and n² could be as large as n-1 (the diameter). So this approach only gives n+1, not 2n-1.

We need a different approach for the 2n-1 bound. Let me think...

Alternative approach: Consider the n cells in a "row" (a horizontal cycle). Actually, let me think about "antipodal" cells.

On the n×n torus (n odd), for each cell (i,j), the "antipodal" cell is (i + (n-1)/2, j + (n-1)/2), which is at distance n-1 (the diameter). 

Hmm, that's not quite right. The distance between (i,j) and (i+(n-1)/2, j+(n-1)/2) is (n-1)/2 + (n-1)/2 = n-1. Yes, that's the diameter.

Consider the cell with label 1 at position (i,j) and the cell with label n² at position (i', j'). The distance is at most n-1. 

Now, consider a "geodesic" (shortest path) from (i,j) to (i',j'). This path has length d ≤ n-1 and consists of horizontal and vertical steps. 

But I need a stronger argument. Let me think about using multiple cells, not just the extremes.

Consider the following approach. Take the cells labeled 1, 2, ..., n+1. These n+1 cells are on the torus. By the pigeonhole principle, at least two of them are at distance at most... well, n+1 cells on an n×n torus. The torus has n² cells. By pigeonhole, two of the n+1 cells are in the same "row" or... hmm, not directly useful.

Let me try another approach. 

Consider the set A = {cells with labels 1, ..., n} and B = {cells with labels n²-n+1, ..., n²}. |A| = |B| = n. 

The minimum label in B is n²-n+1 and the maximum label in A is n. So any edge between A and B has difference ≥ n²-2n+1 = (n-1)².

Now, on the torus, what's the minimum "distance" between A and B? If some cell in A is adjacent to some cell in B, we get an edge with difference ≥ (n-1)², which is much larger than 2n-1 for n ≥ 5. 

But if A and B are far apart, we need to find a path and use intermediate cells. The issue is that intermediate cells could have labels that bridge the gap smoothly.

Let me think about this more carefully. Consider the "annulus" between A and B. The cells with labels n+1, ..., n²-n form a "middle" set of size n²-2n. 

Hmm, I think the right approach is to consider the "vertex boundary" and use the structure of the torus.

Let me try a different lower bound argument.

Consider the n rows of the torus. Each row is a cycle of length n. The labels in row r are some set L_r of n values. The max edge difference within row r is at least (max L_r - min L_r) / ((n-1)/2) = 2(max L_r - min L_r)/(n-1).

Similarly for columns.

Now, consider the "vertical" edges. Between row r and row r+1, there are n vertical edges. The difference on vertical edge (r, c) ↔ (r+1, c) is |f(r,c) - f(r+1,c)|.

Hmm, I think I need to use a more global argument. Let me try the following:

Consider the n cells with the smallest labels: {1, 2, ..., n}. These cells are distributed among the n rows. By pigeonhole, at least one row contains at least 2 of these cells (if n > n, wait, n cells in n rows, so it's possible each row has exactly 1). Actually, n cells in n rows: it's possible each row has exactly 1 cell from {1,...,n}.

Similarly, the n cells with the largest labels {n²-n+1, ..., n²} are distributed among n rows, possibly one per row.

This doesn't immediately help. Let me think about the problem differently.

Let me try to think about what construction achieves bandwidth 2n-1 for the torus.

Construction for the n×n torus with bandwidth 2n-1 (n odd):

Consider the "diagonal" labeling. For each "diagonal" d = 0, 1, ..., n-1, the diagonal consists of cells (i, (d-i) mod n) for i = 0, ..., n-1. Each diagonal is a cycle of length n (it wraps around in both directions).

Wait, actually each diagonal on the torus is a cycle of length n (since n is odd, the diagonal (i, i+d mod n) for i=0..n-1 visits all n cells in the diagonal, and it's a cycle because the torus wraps).

Hmm, actually the "diagonal" (i, i+d) for i=0,...,n-1: when i goes from 0 to n-1, j = i+d mod n also goes through all values. The next cell after (n-1, n-1+d) would be (0, d) which is (n, n+d) mod n = (0, d). And (n-1, n-1+d) to (0, d): the difference in i is 1 (wrapping) and in j is 1 (wrapping). So this is a "diagonal" step, not a horizontal or vertical step. So the diagonal is not a cycle in the torus graph.

Let me reconsider. The diagonal (i, (d+i) mod n) for i = 0, ..., n-1 consists of n cells, but consecutive cells in this diagonal differ by (1, 1), which is not an edge of the torus (edges are (1,0) and (0,1) steps). So diagonals are not cycles in the torus graph.

OK so let me think about the construction differently.

For the bandwidth of C_n × C_n, let me think about what labeling achieves 2n-1.

I think the construction is: label the cells in "diagonal" order. Specifically, order the cells by their "diagonal index" i+j mod n, and within each diagonal, by i.

Cell (i, j) gets label: (number of cells in diagonals 0, 1, ..., (i+j-1) mod n) + (position within diagonal (i+j) mod n) + 1.

Since each diagonal has n cells, the label of (i, j) is: ((i+j) mod n) · n + i + 1.

Wait, this is the same as v(i,j) = ((i+j) mod n) · n + i + 1. Let me check if this is a bijection. For each value of (i+j) mod n = d, the cells are (i, (d-i) mod n) for i = 0, ..., n-1. These get labels d·n + i + 1 for i = 0, ..., n-1, which are d·n + 1, ..., d·n + n. So yes, it's a bijection to {1, ..., n²}.

Now let's compute edge differences.

Horizontal edge (i, j) → (i, j+1):
v(i, j) = ((i+j) mod n) · n + i + 1.
v(i, j+1) = ((i+j+1) mod n) · n + i + 1.

If i+j < n-1 (mod n): (i+j) mod n = i+j, (i+j+1) mod n = i+j+1. Difference = n.
If i+j ≡ n-1 (mod n): (i+j) mod n = n-1, (i+j+1) mod n = 0. Difference = |0·n + i + 1 - (n-1)·n - i - 1| = |i + 1 - n² + n + i + 1| = |2i + 2 + n - n²|. For i = 0, ..., n-1, this is |2i + 2 + n - n²|. The maximum is at i = n-1: |2n + n - n²| = |3n - n²| = n² - 3n. That's huge!

So this construction has huge differences at the wrap-around. Not good.

The issue is the same as before: the "diagonal index" wraps around, causing a big jump.

Let me think about a different construction. 

Maybe the construction that achieves 2n-1 is not based on diagonals but on something else.

Let me think about the n=3 case where we found a valid labeling:
```
(0,0)=1  (0,1)=4  (0,2)=2
(1,0)=5  (1,1)=9  (1,2)=6
(2,0)=3  (2,1)=8  (2,2)=7
```

Let me see the pattern. The labels by position:
- Diagonal 0 (i+j ≡ 0): (0,0)=1, (1,2)=6, (2,1)=8. Labels: 1, 6, 8.
- Diagonal 1 (i+j ≡ 1): (0,1)=4, (1,0)=5, (2,2)=7. Labels: 4, 5, 7.
- Diagonal 2 (i+j ≡ 2): (0,2)=2, (1,1)=9, (2,0)=3. Labels: 2, 9, 3.

Hmm, the labels within each diagonal aren't consecutive. Let me look at the structure differently.

Let me look at the "snake" pattern. Reading the labels in order 1, 2, 3, ..., 9:
1: (0,0)
2: (0,2)
3: (2,0)
4: (0,1)
5: (1,0)
6: (1,2)
7: (2,2)
8: (2,1)
9: (1,1)

The path 1→2→3→4→5→6→7→8→9 visits:
(0,0) → (0,2) [distance 1, wrap] → (2,0) [distance 2] → (0,1) [distance 2] → (1,0) [distance 1] → (1,2) [distance 1, wrap] → (2,2) [distance 1] → (2,1) [distance 1] → (1,1) [distance 1]

So consecutive labels are sometimes at distance 1 (adjacent) and sometimes at distance 2. The max edge difference is 5, not 1, so consecutive labels aren't always adjacent.

Let me look at the differences more carefully:
- The edge (0,0)-(0,2) has |1-2| = 1. ✓ (these are adjacent on the torus, wrap-around)
- But (0,2) and (2,0) are at distance 2, not adjacent. The label difference |2-3| = 1, but they're not adjacent so this doesn't count.

The max edge difference is max over all 18 edges. We computed all are ≤ 5. The edges with difference 5 are: (0,1)-(1,1) with |4-9|=5, and (2,2)-(0,2) with |7-2|=5 (vertical wrap).

Let me think about the general construction. 

Actually, let me try to think about this problem from the perspective of the known result. I believe the bandwidth of C_n × C_n for odd n is 2n-1. Let me try to prove this.

Lower bound (M ≥ 2n-1):

Consider the n cells with labels 1, 2, ..., n. Call this set A. Consider the n cells with labels n²-n+1, ..., n². Call this set B.

Consider the "separation" between A and B on the torus. 

Define the "annular" region: cells at distance exactly k from A. The cells in B must be at some distance from A.

Actually, let me use a different approach. Consider the cells labeled 1, 2, ..., 2n-1. There are 2n-1 such cells. 

Hmm, let me think about the problem using the concept of "bandwidth" more directly.

The bandwidth of a graph G is min over all bijections f: V → {1, ..., |V|} of max_{uv ∈ E} |f(u) - f(v)|.

There's a known lower bound for bandwidth using the "local density" or "isoperimetric" approach:

bw(G) ≥ max_{S ⊆ V, S ≠ ∅} (|N(S)| / something)... 

Actually, a standard lower bound is: bw(G) ≥ max_{v ∈ V} (|N(v)|) = maximum degree. For the torus, max degree = 4, so bw ≥ 4. Not useful.

A better bound: bw(G) ≥ max_{S ⊆ V} ⌈|∂S| / something⌉... 

Actually, the standard lower bound is: for any set S, bw(G) ≥ |∂_V S| where ∂_V S is the vertex boundary (vertices not in S but adjacent to S). Wait, that's not right either.

Let me recall: the bandwidth is related to the pathwidth. Specifically, bw(G) ≥ pw(G) (pathwidth) and bw(G) ≥ vs(G) (vertex separation). Actually, I think pw(G) = vs(G) and bw(G) ≥ pw(G).

The vertex separation of an ordering v_1, ..., v_N is max_k |{v_j : j > k, ∃ i ≤ k, v_i v_j ∈ E}|. The vertex separation of G is the minimum over all orderings.

The pathwidth of C_n × C_n... for the n×n grid P_n × P_n, the pathwidth is n. For the torus C_n × C_n, the pathwidth should be 2n-1 or similar.

Actually, I recall that the pathwidth of C_n × C_n is 2n-2 for even n and 2n-1 for odd n. And bandwidth ≥ pathwidth. But I need to verify this.

Hmm, let me think about the vertex separation lower bound directly.

Consider any ordering of the n² cells. At some point, exactly n cells have been "processed" (labeled 1 to n). Call this set S. The vertex boundary of S (cells not in S but adjacent to S) has size at least... 

On the n×n torus, for a set S of size n, the vertex boundary has size at least... 

If S is a row (cycle of length n), the vertex boundary consists of the 2n cells in the adjacent rows (row above and row below), but wait, each cell in the row has 2 vertical neighbors, and these are all distinct (since the row is a cycle and the vertical neighbors are in different rows). So the vertex boundary is 2n (the n cells in the row above and n cells in the row below). But the row above and below might share cells if n is small. For n ≥ 3, they're distinct. So vertex boundary = 2n.

But can we do better? If S is a "ball" of size n, the vertex boundary is O(√n), much less than 2n. So the minimum vertex boundary for |S| = n is O(√n), not 2n.

So the vertex separation at the point where |S| = n could be as small as O(√n), which doesn't give us 2n-1.

The vertex separation is the MAXIMUM over all k of the vertex boundary of the first k cells. So we need to find the k where the vertex boundary is largest.

For the torus, the vertex boundary is largest when S is about half the torus. When |S| = n²/2, the vertex boundary is... for a "half-torus" (say, the first n/2 rows), the boundary is 2n (the two boundary rows). But for a "round" set of size n²/2, the boundary is O(n). 

Actually, for the torus, the vertex isoperimetric function at n²/2 is Θ(n). The minimum vertex boundary for a set of size n²/2 is n (achieved by taking n/2 consecutive rows, giving boundary 2n... wait, that's 2n).

Hmm, let me think more carefully. If we take ⌊n/2⌋ consecutive rows (out of n rows), that's ⌊n/2⌋ · n cells. The boundary is 2n (the row above and the row below the block). For n odd, ⌊n/2⌋ = (n-1)/2, so |S| = (n-1)n/2, and boundary = 2n.

Can we do better with a different shape? A "round" set of size ~n²/2 would have boundary ~2√(n²/2) · something... actually, on the torus, a "ball" of radius r has about 2r² cells and boundary about 4r. For |S| = n²/2, r ≈ n/2, and boundary ≈ 2n. So it's about the same.

So the vertex separation of the torus is about 2n. More precisely, for odd n, I believe the vertex separation (and hence bandwidth) of C_n × C_n is 2n-1.

But I need to prove this rigorously. Let me think about the lower bound more carefully.

Lower bound: bw(C_n × C_n) ≥ 2n-1 for odd n.

Proof attempt: Consider any labeling f. Consider the cells with labels 1, ..., k for some k to be chosen. Let S = {v : f(v) ≤ k}. The vertex boundary ∂S = {v ∉ S : ∃ u ∈ S, uv ∈ E}. Every vertex in ∂S has label > k, and is adjacent to a vertex with label ≤ k. So for each v ∈ ∂S, there's an edge uv with f(u) ≤ k < f(v), and |f(u) - f(v)| ≥ f(v) - k ≥ 1. But we want a larger bound.

Actually, the bandwidth bound from vertex separation is: bw(G) ≥ max_k |∂S_k| where S_k = {v : f(v) ≤ k} and ∂S_k is the vertex boundary. This is because each vertex in ∂S_k is adjacent to some vertex in S_k, and the label difference is at least 1, but actually the bound is:

For each v ∈ ∂S_k, there's an edge uv with u ∈ S_k (f(u) ≤ k) and v ∉ S_k (f(v) > k). The difference |f(u) - f(v)| ≥ 1. But we need to relate this to |∂S_k|.

The standard argument: the vertices in ∂S_k have labels in {k+1, k+2, ..., k + bw} (since each is adjacent to a vertex with label ≤ k, so the difference is ≤ bw, meaning f(v) ≤ k + bw). So |∂S_k| ≤ bw. Therefore bw ≥ max_k |∂S_k|.

So bw ≥ max_k |∂S_k|, and we need to show that for any ordering, max_k |∂S_k| ≥ 2n-1.

This is the vertex separation number of the torus, which we need to show is ≥ 2n-1.

Claim: For any set S with (n-1)n/2 ≤ |S| ≤ (n+1)n/2 (i.e., |S| ≈ n²/2), the vertex boundary |∂S| ≥ 2n-1.

Wait, actually we need: for any ordering, there exists some k such that |∂S_k| ≥ 2n-1. This is equivalent to saying the vertex separation of C_n × C_n is ≥ 2n-1.

Let me think about why the vertex separation is 2n-1.

Consider any set S with |S| = ⌊n²/2⌋ = (n²-1)/2 (for odd n). We need to show |∂S| ≥ 2n-1.

On the n×n torus, consider the "rows" (horizontal cycles). Each row has n cells. Let a_i = |S ∩ row i| for i = 0, ..., n-1. Then ∑ a_i = |S| = (n²-1)/2.

The vertex boundary of S includes:
- For each row i, the cells in row i that are not in S but are horizontally adjacent to a cell in S ∩ row i.
- For each pair of adjacent rows (i, i+1), the cells in row i+1 that are not in S but are vertically adjacent to a cell in S ∩ row i, and vice versa.

This is complex. Let me think about a simpler approach.

Alternative approach: Consider the "columns" of the torus. Each column is a cycle of length n. For each column c, let b_c = |S ∩ column c|. Then ∑ b_c = |S|.

If S contains an entire column (b_c = n), then the two adjacent columns contribute at least 2 cells to the boundary (the cells in the adjacent columns that are vertically adjacent to the cells in column c). Actually, each cell in column c has 2 horizontal neighbors, one in each adjacent column. So the adjacent columns have at most n cells each in the boundary, but at least... well, if the adjacent columns are entirely outside S, then all n cells in each adjacent column are in the boundary (each is adjacent to a cell in column c). So the boundary is at least 2n.

But this is for a specific S. We need a bound that works for all S of size (n²-1)/2.

Let me try a different approach. I'll use the "isoperimetric inequality" on the torus.

On the n×n torus (n odd), the vertex isoperimetric inequality states that for a set S with |S| = s ≤ n²/2, the vertex boundary |∂S| ≥ min over all sets of size s of |∂S|. 

For the torus, the optimal sets are "balls" in the L1 metric (diamonds). A ball of radius r has |B_r| = 2r² + 2r + 1 (for r < (n-1)/2) and |∂B_r| = 4r + 4 (for r < (n-1)/2).

Wait, let me recalculate. On the torus Z_n × Z_n with L1 distance, a ball of radius r (for r < n/2) centered at the origin is {(x,y) : |x| + |y| ≤ r} where |x| = min(x, n-x). For r < (n-1)/2, this is the same as on the infinite grid. The ball has 1 + 4·(1 + 2 + ... + r) = 1 + 2r(r+1) = 2r² + 2r + 1 cells. The boundary has 4(r+1) cells.

For |S| = (n²-1)/2, we need 2r² + 2r + 1 ≈ n²/2, so r ≈ n/2. But r < (n-1)/2 is required for the ball not to wrap around. For r = (n-3)/2, |B_r| = 2((n-3)/2)² + 2(n-3)/2 + 1 = (n-3)²/2 + (n-3) + 1 = (n²-6n+9)/2 + n - 2 = (n²-6n+9+2n-4)/2 = (n²-4n+5)/2. And |∂B_r| = 4((n-3)/2 + 1) = 4(n-1)/2 = 2(n-1) = 2n-2.

For r = (n-1)/2, the ball starts to wrap around. |B_{(n-1)/2}| = 2((n-1)/2)² + 2(n-1)/2 + 1 = (n-1)²/2 + (n-1) + 1 = (n²-2n+1)/2 + n = (n²-2n+1+2n)/2 = (n²+1)/2. And the boundary... when r = (n-1)/2, the ball touches itself on the torus, so the boundary is different.

For r = (n-1)/2, the ball B_r = {(x,y) : |x| + |y| ≤ (n-1)/2}. On the torus, |x| ranges from 0 to (n-1)/2 and |y| from 0 to (n-1)/2. The constraint |x| + |y| ≤ (n-1)/2 with |x|, |y| ∈ {0, 1, ..., (n-1)/2}. This gives (n²+1)/2 cells (more than half the torus). The boundary is the set of cells with |x| + |y| = (n+1)/2, but on the torus, |x| + |y| = (n+1)/2 means |x| + |y| = (n+1)/2, and since |x| ≤ (n-1)/2 and |y| ≤ (n-1)/2, we need |x| + |y| = (n+1)/2 with both ≤ (n-1)/2. The number of such cells is... |x| can range from 1 to (n-1)/2 (since |y| = (n+1)/2 - |x| ≥ 1). For each |x| from 1 to (n-1)/2, |y| = (n+1)/2 - |x| from (n-1)/2 down to 1. The number of cells with given (|x|, |y|) is: 4 if both > 0, 2 if one is 0. Here both are always > 0, so 4 cells per (|x|, |y|) pair. Number of pairs: (n-1)/2. So boundary = 4 · (n-1)/2 = 2(n-1) = 2n-2.

Hmm, so the ball of radius (n-1)/2 has (n²+1)/2 cells and boundary 2n-2. But (n²+1)/2 > n²/2, so this is more than half. For |S| = (n²-1)/2 (just under half), the ball of radius (n-3)/2 has (n²-4n+5)/2 cells, which is less than (n²-1)/2. So we need a set slightly larger than the ball of radius (n-3)/2.

The ball of radius (n-3)/2 has (n²-4n+5)/2 cells and boundary 2n-2. We need to add (n²-1)/2 - (n²-4n+5)/2 = (4n-4)/2 = 2n-2 more cells. Adding cells to the ball can only increase or maintain the boundary (adding a boundary cell to S removes it from the boundary but might add new boundary cells). 

Actually, adding a boundary cell to S removes it from the boundary but might add its neighbors (that aren't in S) to the boundary. So the boundary could increase or decrease.

This is getting complicated. Let me try a cleaner approach to the lower bound.

Cleaner lower bound approach:

I'll show that for any labeling of the n×n torus (n odd), there's an edge with difference ≥ 2n-1.

Consider the cells with labels 1, 2, ..., n. Call this set A. |A| = n. 

On the torus, the n cells in A are distributed somehow. Consider the "rows" (horizontal cycles). Let a_i = |A ∩ row i|. Then ∑ a_i = n.

Similarly, consider the "columns" (vertical cycles). Let b_j = |A ∩ column j|. Then ∑ b_j = n.

Now, consider the complement of A, which has n² - n cells. The cells with labels n+1, ..., n² are in the complement.

The vertex boundary of A, ∂A, consists of cells not in A that are adjacent to some cell in A. Each cell in ∂A has label ≥ n+1 and is adjacent to a cell with label ≤ n. So the edge connecting them has difference ≥ (n+1) - n = 1. But we want a larger bound.

Actually, the key insight for the bandwidth lower bound is:

The cells in ∂A all have labels > n (since A = {labels 1,...,n}). Each cell in ∂A is adjacent to a cell in A (label ≤ n). So the label of each cell in ∂A is at most n + bw (since the edge difference is ≤ bw). So all cells in ∂A have labels in {n+1, ..., n + bw}. Therefore |∂A| ≤ bw.

So bw ≥ |∂A|. Now we need to show |∂A| ≥ 2n-1 for any set A of size n on the n×n torus (n odd).

Wait, but A is a specific set (the cells with the n smallest labels), and its structure depends on the labeling. We need to show that for ANY set A of size n, |∂A| ≥ 2n-1.

Is this true? Let me check for n=3. Any set of 3 cells on the 3×3 torus has vertex boundary ≥ 5 = 2·3-1.

The 3×3 torus has 9 cells, each with 4 neighbors. A set of 3 cells:
- If the 3 cells form a "row" (cycle of length 3): boundary = 6 (the other 2 rows, each with 3 cells, all adjacent to the row). Wait, each cell in the row has 2 vertical neighbors. The 3 cells in the row have 6 vertical neighbors, but some might overlap. On the 3×3 torus, row 0 = {(0,0), (0,1), (0,2)}. Vertical neighbors: (1,0), (2,0), (1,1), (2,1), (1,2), (2,2) = all 6 cells not in the row. So boundary = 6 ≥ 5. ✓

- If the 3 cells form an "L" shape, say {(0,0), (0,1), (1,0)}: 
  Neighbors of (0,0) not in A: (2,0), (0,2). 
  Neighbors of (0,1) not in A: (1,1), (2,1), (0,2). 
  Neighbors of (1,0) not in A: (2,0), (1,1), (1,2). 
  Boundary = {(2,0), (0,2), (1,1), (2,1), (1,2)} = 5. ✓

- If the 3 cells form a "diagonal", say {(0,0), (1,1), (2,2)}:
  Neighbors of (0,0): (1,0), (2,0), (0,1), (0,2).
  Neighbors of (1,1): (0,1), (2,1), (1,0), (1,2).
  Neighbors of (2,2): (1,2), (0,2), (2,1), (2,0).
  Boundary = {(1,0), (2,0), (0,1), (0,2), (2,1), (1,2)} = 6. ✓

So for n=3, any set of 3 cells has boundary ≥ 5 = 2n-1. 

Now let me prove this for general odd n.

Claim: On the n×n torus (n odd), any set A of n cells has vertex boundary |∂A| ≥ 2n-1.

Proof: Consider the n rows. Let a_i = |A ∩ row i|, so ∑ a_i = n. 

Case 1: Some row has a_i = 0. Then there's a row with no cells of A. The rows adjacent to this empty row... hmm, this doesn't directly help.

Let me think about this differently. 

Consider the "row boundary": cells in ∂A that are in the same row as a cell of A but not in A. For each row i with 0 < a_i < n, the row boundary in row i is at least 2 (since A ∩ row i is a proper nonempty subset of a cycle of length n, and any such subset has at least 2 boundary vertices on the cycle). Actually, for a subset of a cycle of length n with a_i elements, the vertex boundary on the cycle is at least 2 (if 0 < a_i < n). 

Wait, that's the boundary within the cycle. But we also have the vertical boundary.

Let me separate the boundary into horizontal and vertical components.

Horizontal boundary: cells in ∂A that are in the same row as some cell of A, and are horizontally adjacent to a cell of A. For row i with a_i cells of A (0 < a_i < n), the horizontal boundary in row i is at least 2 (the cycle boundary). If a_i = n, horizontal boundary in row i is 0. If a_i = 0, horizontal boundary in row i is 0 (no cells of A in this row).

Vertical boundary: cells in ∂A that are vertically adjacent to a cell of A. For each cell (i,j) ∈ A, its vertical neighbors (i±1, j) are in ∂A if they're not in A. 

The total boundary is at least the horizontal boundary plus the vertical boundary (minus possible overlaps, but let's not worry about that for a lower bound).

Hmm, this is getting complicated because of overlaps. Let me try a different approach.

Alternative proof of the claim:

Consider the n rows. If all a_i ∈ {0, n}, then since ∑ a_i = n and each a_i is 0 or n, exactly one row has a_i = n and the rest have a_i = 0. Then A is an entire row. The boundary is the 2n cells in the two adjacent rows (each cell in A has 2 vertical neighbors, all distinct, giving 2n boundary cells). So |∂A| = 2n ≥ 2n-1. ✓

If some row has 0 < a_i < n, then the horizontal boundary in that row is at least 2. But we also need to count the vertical boundary.

Let me try to use a different method. 

Method: Count the number of edges between A and V\A. Each cell in A has degree 4, so the total number of edges incident to A is 4n (with multiplicity, counting edges within A twice). The number of edges within A is e(A). The number of edges between A and V\A is 4n - 2e(A). Each boundary vertex is incident to at least 1 such edge, so |∂A| ≤ 4n - 2e(A). But we want a lower bound on |∂A|, not an upper bound.

For a lower bound on |∂A|: each boundary vertex is incident to at most 4 edges from A, so |∂A| ≥ (4n - 2e(A)) / 4 = n - e(A)/2. To minimize |∂A|, we maximize e(A). 

What's the maximum number of edges within a set of n cells on the n×n torus? If the n cells form a cycle (a row),        — AI历史解题过程（thinking）
#   polymath_00260         — 题目ID

# Solver Task

You are a mathematical problem analysis assistant. You will NOT solve any problems.
You will analyze the relationship between a standard solution and an AI's attempted solution.

**CRITICAL CONSTRAINTS:**
- Do NOT use any tools. Do NOT write files. Do NOT execute commands. Do NOT search.
- All information you need is in this AGENTS.md file.
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
  <problem_id>polymath_00260</problem_id>
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

The cells of a square $2011 \times 2011$ array are labelled with the integers $1,2,\ldots, 2011^2$, in such a way that every label is used exactly once. We then identify the left-hand and right-hand edges, and then the top and bottom, in the normal way to form a torus (the surface of a doughnut).
Determine the largest positive integer $M$ such that, no matter which labelling we choose, there exist two neighbouring cells with the difference of their labels at least $M$.
(Cells with coordinates $(x,y)$ and $(x',y')$ are considered to be neighbours if $x=x'$ and $y-y'\equiv\pm1\pmod{2011}$, or if $y=y'$ and $x-x'\equiv\pm1\pmod{2011}$.)

[i](Romania) Dan Schwarz[/i]

## Standard Solution

To solve this problem, we need to determine the largest positive integer \( M \) such that, no matter how we label the cells of a \( 2011 \times 2011 \) array with the integers \( 1, 2, \ldots, 2011^2 \), there exist two neighboring cells with the difference of their labels at least \( M \).

1. **Understanding the Problem:**
   - We have a \( 2011 \times 2011 \) grid.
   - Each cell is labeled with a unique integer from \( 1 \) to \( 2011^2 \).
   - The grid is wrapped around to form a torus, meaning the left edge is connected to the right edge, and the top edge is connected to the bottom edge.
   - Two cells are neighbors if they share a side.

2. **Neighboring Cells:**
   - For a cell at \((x, y)\), its neighbors are:
     - \((x, y+1)\) and \((x, y-1)\) (modulo 2011 for the y-coordinate).
     - \((x+1, y)\) and \((x-1, y)\) (modulo 2011 for the x-coordinate).

3. **Objective:**
   - We need to find the largest \( M \) such that there are always two neighboring cells with a difference in their labels of at least \( M \).

4. **Key Insight:**
   - The maximum difference between any two labels is \( 2011^2 - 1 \).
   - We need to ensure that the difference between the labels of any two neighboring cells is maximized.

5. **Bounding the Difference:**
   - Consider the worst-case scenario where the labels are as evenly distributed as possible.
   - If we label the cells in a way that minimizes the difference between neighboring cells, the difference between the highest and lowest labels in any \( 2 \times 2 \) block should be minimized.

6. **Calculating the Bound:**
   - In a \( 2011 \times 2011 \) grid, there are \( 2011^2 \) cells.
   - The average difference between labels of neighboring cells can be approximated by considering the total range of labels divided by the number of cells.
   - The total range is \( 2011^2 - 1 \).

7. **Optimal Labeling:**
   - If we label the cells in a snake-like pattern (row-wise or column-wise), the difference between neighboring cells can be controlled.
   - However, due to the toroidal nature, the difference between the highest and lowest labels in any \( 2 \times 2 \) block will be significant.

8. **Conclusion:**
   - The largest possible difference \( M \) such that there are always two neighboring cells with a difference of at least \( M \) is \( 2 \times 2011 - 1 = 4021 \).

The final answer is \( \boxed{4021} \).

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. It's a torus labeling problem. We have a 2011×2011 torus, cells labeled 1 to 2011². We need to find the largest M such that no matter the labeling, there exist two neighboring cells with label difference at least M.

This is a classic competition problem. Let me think about it.

The answer should be related to the structure. Let me think about the general approach.

We have n×n torus (n=2011), labels 1 to n². Each cell has 4 neighbors. We want to find the maximum M such that in any labeling, some adjacent pair has difference ≥ M.

Upper bound (constructive): We need to construct a labeling where all adjacent differences are ≤ some value. This gives an upper bound on M.

Lower bound: We need to show that in any labeling, some adjacent pair has difference ≥ M.

Let me think about the lower bound first. Consider the cells labeled 1, 2, ..., k for some k. These k cells form a set S. The boundary of S (cells in S adjacent to cells not in S) — actually, let me think differently.

Consider the values. Sort cells by label. Consider the cell with label 1 and the cell with label n². The difference is n²-1. But they might not be adjacent.

Key idea: Consider the "level sets". For each threshold t, consider S_t = {cells with label ≤ t}. As t goes from 1 to n², S_t grows from empty to full. 

Actually, let me think about this more carefully using the standard approach for such problems.

The standard approach: Consider a path on the torus. The torus graph has n² vertices and 2n² edges (each vertex has degree 4, so 2n² edges). 

Lower bound approach: Consider the set of cells with labels in {1, 2, ..., m} and the set with labels in {n²-m+1, ..., n²}. If these two sets are "far apart" in some sense... 

Actually, let me think about the isoperimetric approach. 

Consider the cells labeled 1, 2, ..., k. Call this set A_k. The edge boundary of A_k consists of edges between A_k and its complement. Each such edge connects a cell with label ≤ k to a cell with label > k, so the difference is at least 1 (not helpful directly).

Let me think about it differently. Consider the maximum label difference across all edges. We want to show this is at least M for any labeling, and construct a labeling achieving exactly M (or close).

Let me think about the upper bound (construction). 

On a torus, we can try to label cells so that adjacent cells have small differences. One natural construction: label cells in a "snake" pattern. But on a torus, the snake must close up.

Actually, let me think about what the answer likely is. For an n×n torus, I believe the answer is n² - 1... no, that's too large. 

Let me think about small cases. For n=2, we have a 2×2 torus. Each cell is adjacent to every other cell (since on a 2×2 torus, each cell's 4 neighbors are the other 3 cells, with one repeated). Actually on a 2×2 torus, cell (0,0) has neighbors (1,0), (0,1), (1,0) [wrapping], (0,1) [wrapping]. So neighbors are (1,0) and (0,1). And (1,1) has neighbors (0,1) and (1,0). So the graph is a 4-cycle: (0,0)-(1,0)-(1,1)-(0,1)-(0,0). 

Labels 1,2,3,4 on a 4-cycle. We want to minimize the maximum edge difference. Best arrangement: 1,2,4,3 around the cycle gives differences 1,2,1,2. Or 1,3,4,2 gives 2,1,2,1. Or 1,2,3,4 gives 1,1,1,3. The minimum maximum is 2 (achieved by 1,2,4,3 or 1,3,4,2 etc). So M=2 for n=2. Note n²-1 = 3, and 2 = ... hmm. n=2, M=2. 

For n=3: 3×3 torus, 9 cells, 18 edges. This is more complex. Let me think about the general structure.

Actually, let me recall: I think this is a known competition problem (Romania, Dan Schwarz). The answer for n×n torus should be... let me derive it.

Key insight: Consider the "band" structure. On the torus, consider horizontal lines (rows). Each row is a cycle of length n. 

Lower bound: Consider the cells with labels 1 through n. These n cells are somewhere on the torus. Consider the cells with labels n²-n+1 through n². These n cells are somewhere. 

Hmm, let me think about a cleaner approach.

Approach via paths: On the torus, consider any Hamiltonian path. The labels along the path go from some value to another. The sum of absolute differences along the path is at least n²-1 (telescoping from min to max label along the path... no, that's not right either).

Actually, let me think about the "discrete intermediate value" approach.

Consider the function f: cells → labels. Consider a horizontal cycle (a row). The labels along this cycle of length n. The maximum difference between adjacent cells on this cycle is at least... well, if we look at all n rows, the labels 1 to n² are distributed.

Let me think about the problem more carefully.

Lower bound: I'll use the following approach. Consider the set L = {cells with labels 1, ..., n²-n} and H = {cells with labels n²-n+1, ..., n²}. |L| = n²-n, |H| = n.

Claim: There must be an edge between L and H where the difference is large. Actually, every edge between L and H has difference at least 1 (since max of L is n²-n and min of H is n²-n+1). But we want a larger bound.

Hmm, let me think differently.

Better approach: Consider labeling the torus. Look at all horizontal edges (edges between (x,y) and (x+1,y)). There are n² such edges (n rows, each a cycle of n edges, but wait—each row has n edges, and there are n rows, so n² horizontal edges). Similarly n² vertical edges. Total 2n² edges.

For the lower bound, consider the following: Take the n cells with the smallest labels {1,...,n} and the n cells with the largest labels {n²-n+1,...,n²}. 

Actually, I think the key idea is about "rows" and "columns" and using the pigeonhole principle.

Let me think about it from the perspective of the maximum value M we're trying to find.

Construction (upper bound): We want to arrange labels so that every adjacent pair has difference ≤ M. 

One idea: Fill the torus row by row. Row 0: 1, 2, ..., n. Row 1: n+1, ..., 2n. Etc. Then horizontal differences are 1, but vertical differences are n. Also, the wrap-around in each row: the difference between position n and position 1 in the same row is n-1. And the vertical wrap-around: row n-1 to row 0, difference is n²-n - 1 = n(n-1)-1. That's huge.

So this naive construction doesn't work well because of wrap-around.

Better construction: We need to handle the toroidal wrap-around. 

Idea: Use a "diagonal" filling. Label cell (i,j) with value i*n + j + 1 but with some modular arithmetic to handle wrap-around.

Actually, let me think about what construction minimizes the maximum edge difference on a torus.

Consider the labeling where cell (i,j) gets label (i*n + j mod n²) + 1. This is the same as row-by-row. The wrap-around issues remain.

Alternative: Think of the torus as Z_n × Z_n. We want a bijection f: Z_n × Z_n → {1, ..., n²} such that |f(u) - f(v)| is small for all edges uv.

Consider f(i,j) = (a*i + b*j) mod n² + 1 for some constants a, b. For this to be a bijection, we need... well, it's a map from Z_n × Z_n to Z_{n²}. This is a bijection iff... it's complicated.

Let me think about the problem differently. 

I recall that for this type of problem on a torus, the answer involves n²/2 or similar. Let me think about the lower bound more carefully.

Lower bound argument: 

Consider the n cells with labels {1, 2, ..., n} (the "low" set) and the n cells with labels {n²-n+1, ..., n²} (the "high" set). The difference between any low label and any high label is at least n² - 2n + 1 = (n-1)².

Now, on the torus, consider any path from a low cell to a high cell. Along this path, there must be an edge where the label "jumps" from ≤ some value to ≥ some value. 

But we need to be more careful. Let me think about the structure.

Actually, here's a cleaner approach. Consider the set S = {cells with labels 1, ..., k} for some k to be determined. The edge boundary ∂S consists of edges between S and V\S. Each such edge (u,v) with u ∈ S, v ∉ S has f(u) ≤ k < f(v), so the difference f(v) - f(u) ≥ 1. But we can say more: f(v) - f(u) ≥ f(v) - k. 

Hmm, this isn't directly giving us what we want. Let me think about the "maximum difference" more carefully.

Let me reconsider. Let D = max over all edges of |f(u) - f(v)|. We want to find the minimum possible D over all labelings, and that minimum is M (the largest M that works for all labelings).

Wait, re-reading: "Determine the largest positive integer M such that, no matter which labelling we choose, there exist two neighbouring cells with the difference of their labels at least M."

So M = min over all labelings of (max over all edges of |difference|). We want to find this M.

Lower bound on M: Show that for any labeling, max edge difference ≥ M.
Upper bound on M: Exhibit a labeling where max edge difference = M (or ≤ M).

Let me think about the lower bound. 

Consider the cells sorted by label: c_1, c_2, ..., c_{n²} where f(c_i) = i. 

Consider the "graph distance" on the torus. The diameter of the n×n torus is... for odd n, it's 2·⌊n/2⌋ = n-1 (since n=2011 is odd, the distance in each coordinate is at most (n-1)/2, so diameter is n-1).

Now, consider c_1 (label 1) and c_{n²} (label n²). The graph distance between them is at most n-1 (diameter). Consider a shortest path c_1 = v_0, v_1, ..., v_d = c_{n²} where d ≤ n-1. Along this path, the labels go from 1 to n². By telescoping (or rather, by the max jump), there exists an edge on this path where the label difference is at least (n²-1)/d ≥ (n²-1)/(n-1) = n+1.

So M ≥ n+1 = 2012.

But can we do better? Let me think about whether we can get a larger lower bound.

Actually, we can use more than just the two extreme cells. Consider c_1 and c_{n²}. But also consider the structure more carefully.

Let me think about the upper bound. Can we achieve max edge difference = n+1?

Construction attempt: We want to label the n×n torus so that every edge has difference ≤ n+1 (or some value close to n).

Hmm, let me think about the "diagonal" construction. Consider labeling cell (i,j) with f(i,j) = ((i + j) mod n) · n + ((i) mod n) + 1 or something like that.

Actually, let me think about a simpler construction. Consider the "snake" that goes diagonally.

Let me think about the labeling f(i,j) = (i·n + j) but arranged to minimize wrap-around issues.

Actually, here's an idea. Consider the map f(i,j) = (i + j·n) mod n² + 1... no, let me think more carefully.

Let me consider a different approach. Think of the torus as having rows and columns. 

Construction: Label cell (i, j) with value v(i,j) = ((j - i) mod n) · n + i + 1.

Wait, let me think about what properties we want. We want:
- Horizontal neighbors (i,j) and (i, j+1): small difference
- Vertical neighbors (i,j) and (i+1, j): small difference
- Wrap-around: (i, n-1) and (i, 0): small difference; (n-1, j) and (0, j): small difference.

Consider the labeling v(i,j) = (i mod n) · n + (j mod n) + 1, i.e., standard row-by-row. Horizontal edges: difference 1 (except wrap: difference n-1). Vertical edges: difference n (except wrap: difference n²-n). The vertical wrap-around gives difference n²-n which is huge. So this doesn't work.

The issue is the vertical wrap-around. To fix this, we need the bottom row and top row to have similar labels.

Idea: Use a "diagonal" arrangement. v(i,j) = ((i + j) mod n²) ... no.

Let me think about v(i,j) = ((a·i + b·j) mod n²) for suitable a, b. For this to be a bijection from Z_n × Z_n to Z_{n²}, we need... actually Z_n × Z_n has n² elements and Z_{n²} has n² elements, but the map (i,j) → ai + bj mod n² needs to be a bijection. This requires that the map is injective. 

For n prime (2011 is prime!), Z_n × Z_n ≅ Z_n × Z_n, and we can embed into Z_{n²}. Actually, since n is prime, by CRT, Z_{n²} is not isomorphic to Z_n × Z_n (since n² is not coprime to n). So a linear map mod n² won't directly give a bijection from Z_n × Z_n.

Let me think differently. 

Consider the labeling v(i,j) = ((i + j) mod n) · n + ((i + 2j) mod n) + 1. Since n is prime and 1, 2 are "independent" in some sense... actually, the map (i,j) → ((i+j) mod n, (i+2j) mod n) is a bijection on Z_n × Z_n (since the matrix [[1,1],[1,2]] has determinant 1, which is nonzero mod n). So this gives a bijection to {0,...,n-1} × {0,...,n-1}, and then v(i,j) = first_coord · n + second_coord + 1 is a bijection to {1,...,n²}.

Now let's compute edge differences:
- Horizontal: (i,j) → (i, j+1). First coord changes by +1 mod n, second coord changes by +2 mod n.
  - If no wrap in first coord: first coord +1, so v changes by n. Second coord changes by +2 mod n.
    - If no wrap in second: v changes by n + 2.
    - If wrap in second (j+2 ≥ n, i.e., j ≥ n-1, but j+1 is the neighbor so j ranges 0..n-1 and we look at j→j+1 mod n): second coord goes from (i+2j) mod n to (i+2(j+1)) mod n = (i+2j+2) mod n. Wrap happens when i+2j+2 ≥ n, i.e., the second coord wraps. In that case, the change is n + 2 - n = n + 2 - n... wait, let me be more careful.

  v(i,j) = ((i+j) mod n) · n + ((i+2j) mod n) + 1.
  v(i, j+1) = ((i+j+1) mod n) · n + ((i+2j+2) mod n) + 1.
  
  Let a = (i+j) mod n, b = (i+2j) mod n.
  Then v(i,j) = a·n + b + 1.
  v(i,j+1) = ((a+1) mod n) · n + ((b+2) mod n) + 1.
  
  Case 1: a < n-1 and b < n-2 (no wraps): v(i,j+1) = (a+1)·n + (b+2) + 1. Difference = n + 2.
  Case 2: a < n-1 and b ≥ n-2 (b = n-2 or n-1): 
    - b = n-2: (b+2) mod n = 0. v(i,j+1) = (a+1)·n + 0 + 1. v(i,j) = a·n + (n-2) + 1 = a·n + n - 1. Difference = (a+1)·n + 1 - (a·n + n - 1) = n + 1 - n + 1 = 2. Wait: (a+1)·n + 1 - a·n - n + 1 = an + n + 1 - an - n + 1 = 2. So difference = 2.
    - b = n-1: (b+2) mod n = 1. v(i,j+1) = (a+1)·n + 1 + 1 = (a+1)·n + 2. v(i,j) = a·n + n - 1 + 1 = a·n + n. Difference = (a+1)·n + 2 - a·n - n = 2.
  Case 3: a = n-1 and b < n-2: (a+1) mod n = 0. v(i,j+1) = 0·n + (b+2) + 1 = b + 3. v(i,j) = (n-1)·n + b + 1 = n² - n + b + 1. Difference = |b + 3 - n² + n - b - 1| = |2 + n - n²| = n² - n - 2. That's huge!

So this construction has a huge difference when a = n-1 (the first coordinate wraps). This is the same wrap-around problem.

The fundamental issue: on a torus, any "linear" labeling will have wrap-around issues in at least one direction.

Let me reconsider. The key difficulty is the toroidal structure—both directions wrap around.

Let me think about the lower bound more carefully, and also think about what the answer should be.

Lower bound refinement: Instead of just using c_1 and c_{n²}, let me use multiple pairs.

Consider the n cells in the first "row" of the labeling—no, that doesn't make sense since the labeling is arbitrary.

Let me think about it using the concept of "cuts" or "level sets."

For each t from 1 to n²-1, define S_t = {cells with label ≤ t}. The edge boundary ∂S_t is the set of edges between S_t and V \ S_t. 

For each edge e = (u,v) in ∂S_t with f(u) ≤ t < f(v), the difference |f(u) - f(v)| ≥ 1, but more importantly, if we sum over all t, each edge (u,v) with f(u) < f(v) contributes to ∂S_t for t = f(u), f(u)+1, ..., f(v)-1, i.e., it contributes |f(u) - f(v)| times.

So: ∑_{t=1}^{n²-1} |∂S_t| = ∑_{edges (u,v)} |f(u) - f(v)|.

Now, the total number of edges is 2n². If the maximum edge difference is D, then the sum is at most 2n² · D. So D ≥ (∑ |∂S_t|) / (2n²).

We need a lower bound on ∑ |∂S_t|. For this, we need a lower bound on |∂S_t| for each t, which relates to the isoperimetric problem on the torus.

The edge isoperimetric inequality on the n×n torus: for a set S with |S| = s, the edge boundary |∂S| ≥ ... 

On the torus Z_n × Z_n, the edge isoperimetric inequality is known. For a set of size s, the minimum edge boundary is related to the structure of S. 

Actually, let me think about this differently. The sum ∑_{t=1}^{n²-1} |∂S_t| can be bounded below using the fact that the "conductance" of the torus is bounded.

Hmm, this is getting complicated. Let me think about the problem from the answer's perspective.

For the n×n torus with n odd, I believe the answer is M = n² - n + 1 or something related. Wait, let me reconsider.

Actually, let me reconsider the lower bound. We showed M ≥ n+1 using the diameter argument. Can we do better?

Consider c_1, c_2, ..., c_{n²} sorted by label. Consider the graph distance d(c_i, c_j) on the torus. 

For any i < j, there's a path from c_i to c_j of length at most diam = n-1. Along this path, the max label difference on any edge is at least (j - i)/(n-1). So the max edge difference D ≥ (j-i)/(n-1) for all i < j. Taking j - i = n² - 1, we get D ≥ (n²-1)/(n-1) = n+1.

But we can potentially do better by considering multiple paths or a more global argument.

Consider the following: take the labels 1, 2, ..., n². For each consecutive pair (c_i, c_{i+1}), the graph distance d(c_i, c_{i+1}) could be anything from 1 to n-1. If d(c_i, c_{i+1}) = 1, then the edge (c_i, c_{i+1}) has difference 1. If d(c_i, c_{i+1}) > 1, then we need to go through intermediate cells.

Hmm, let me think about a different lower bound approach.

Consider the n cells with the smallest labels: {c_1, ..., c_n} (labels 1 to n). And the n cells with the largest labels: {c_{n²-n+1}, ..., c_{n²}} (labels n²-n+1 to n²).

The minimum label difference between these two sets is (n²-n+1) - n = n² - 2n + 1 = (n-1)².

Now, on the torus, consider the "separation" between these two sets. If there's a path from a low cell to a high cell of length ℓ, then along this path, some edge has difference ≥ (n-1)²/ℓ. The shortest such path has length at most... well, it depends on the arrangement.

But actually, we can be smarter. Consider all edges between the "low half" and "high half" of the labels.

Let me try a different approach. Consider the set A = {cells with labels 1, ..., n²/2} (roughly half). The edge boundary of A has some size. Each edge in the boundary connects a cell with label ≤ n²/2 to one with label > n²/2. The difference on such an edge is at least 1, but could be up to n²/2.

Hmm, I think I need to be more clever. Let me look at this from the construction side to guess the answer.

Construction for upper bound: Let me think about what labeling could achieve a small maximum edge difference.

Key insight: On a torus, we can use a "space-filling curve" type approach, but the wrap-around is the issue.

Let me consider the following construction for odd n. Label the torus using a "knight's move" pattern or a pattern that spreads consecutive labels far apart.

Wait, actually, we want consecutive labels to be CLOSE, not far apart. We want to minimize the maximum edge difference, so we want labels that are close in value to be on adjacent cells.

So we want a Hamiltonian path (or cycle) on the torus where consecutive cells in the path get consecutive labels, and the path uses only edges of the torus. If such a Hamiltonian cycle exists, then the max edge difference along the cycle is 1, but the non-cycle edges could have large differences.

The torus n×n (n odd) does have a Hamiltonian cycle. If we label along a Hamiltonian cycle, the cycle edges have difference 1, but the other edges (the "chords") could have large differences. There are 2n² edges total and n² cycle edges, so n² non-cycle edges. These non-cycle edges connect cells that could be far apart in the cycle, hence have large label differences.

So the Hamiltonian cycle approach gives max edge difference = max over non-cycle edges of |difference|, which could be up to n²-1 in the worst case. Not good.

Let me think about this more carefully. 

Actually, I think the answer is n+1. Let me verify this with the n=2 case: n+1 = 3, but we computed M=2 for n=2. So either the answer isn't n+1, or the n=2 case is special (since n=2 is even and the torus structure is different).

Wait, for n=2, the diameter is 1 (every cell is adjacent to every other cell in the 2×2 torus, since the graph is a 4-cycle but with the torus structure... let me recheck). On the 2×2 torus, cell (0,0) has neighbors (1,0), (0,1), (1,0) [wrapping from (0,-1)=(0,1)], (0,1) [wrapping from (-1,0)=(1,0)]. So the neighbors are (1,0) and (0,1). The graph is a 4-cycle: (0,0)-(1,0)-(1,1)-(0,1)-(0,0). Diameter = 2. So the lower bound gives D ≥ (4-1)/2 = 1.5, so D ≥ 2. And we showed M=2 for n=2. So the bound is tight for n=2!

For n=2, n+1 = 3 but M=2. The diameter is 2 = n, not n-1. For n=2, ⌊n/2⌋ = 1, so diameter = 2·1 = 2 = n. For odd n, diameter = 2·(n-1)/2 = n-1.

So for n=2, the bound gives D ≥ 3/2 → D ≥ 2, and M=2. The bound (n²-1)/diam = 3/2, ceiling is 2. And M=2. So it's tight.

For general odd n, the bound gives D ≥ (n²-1)/(n-1) = n+1. Is this tight? We need a construction achieving D = n+1.

Let me think about whether such a construction exists.

For n=3: M should be 4 if the answer is n+1=4. Let me check if we can label a 3×3 torus with max edge difference 4.

3×3 torus, labels 1-9. We need every edge to have difference ≤ 4.

Let me try:
```
1 2 3
4 5 6
7 8 9
```
Horizontal edges: differences 1, 1, 2 (wrap: 3-1=2). Vertical edges: 3, 3, 3 (wrap: 7-1=6). The vertical wrap gives 6 > 4. Not good.

Let me try a different arrangement:
```
1 5 9
2 6 7
3 4 8
```
Horizontal: |1-5|=4, |5-9|=4, |9-1|=8 (wrap). Bad.

Let me try:
```
1 4 7
5 8 2
9 3 6
```
Horizontal row 0: |1-4|=3, |4-7|=3, |7-1|=6 (wrap). Bad.

The wrap-around is always the problem. Let me think about how to handle it.

For the horizontal wrap in a row: we need the first and last elements of each row to be close. Similarly for vertical.

What if we arrange each row so that it goes up and then comes back down? Like a snake within each row? But on a cycle (which is what each row is), you can't snake—you always have a wrap-around point.

Hmm, let me think about this differently. 

For a cycle of length n with labels being a subset of {1,...,n²}, the minimum possible maximum adjacent difference depends on the labels assigned to that cycle.

Actually, for a cycle of length n with labels a_1 < a_2 < ... < a_n, the minimum max adjacent difference (optimally arranging them on the cycle) is... 

If we arrange them as a_1, a_3, a_5, ..., a_n, a_{n-1}, a_{n-3}, ..., a_2 (or similar zigzag), the max difference is roughly (a_n - a_1) / (n/2) ≈ 2(a_n - a_1)/n.

Wait, for a cycle, the optimal arrangement to minimize max adjacent difference: arrange the sorted values as a_1, a_2, ..., a_n around the cycle. The differences are a_2-a_1, a_3-a_2, ..., a_n - a_{n-1}, and a_n - a_1 (wrap). The wrap is the biggest. To minimize the max, we should interleave: place them as a_1, a_{⌈n/2⌉+1}, a_2, a_{⌈n/2⌉+2}, ..., which gives max difference roughly (a_n - a_1)/⌈n/2⌉.

This is getting complicated. Let me think about the problem from a higher level.

I think the answer is M = n+1 for odd n, and the construction involves a clever arrangement. Let me think about the construction.

Construction idea: Use the fact that n is odd. Consider the labeling:
v(i, j) = ((i + j·(n+1)/2) mod n) · n + i + 1

Wait, I need to think about this more carefully. Let me consider a different approach.

Since n is odd, (n+1)/2 is an integer. Consider the "diagonal" labeling:

v(i, j) = ((j - i·(n-1)/2) mod n) · n + ((i + j) mod n) + 1

Hmm, this is getting complicated. Let me think about what we need.

We need a bijection f: Z_n × Z_n → {1, ..., n²} such that:
1. |f(i, j) - f(i, j±1)| ≤ D for all i, j (horizontal edges)
2. |f(i±1, j) - f(i, j)| ≤ D for all i, j (vertical edges)

And we want D = n+1.

Let me try the construction f(i,j) = ((i + j) mod n) · n + ((i - j) mod n) + 1.

Check bijection: The map (i,j) → ((i+j) mod n, (i-j) mod n). The matrix is [[1, 1], [1, -1]] with determinant -2. Since n is odd, 2 is invertible mod n, so this is a bijection on Z_n × Z_n. Good.

Now, f(i,j) = a·n + b + 1 where a = (i+j) mod n, b = (i-j) mod n.

Horizontal edge (i, j) → (i, j+1):
a' = (i + j + 1) mod n = (a + 1) mod n
b' = (i - j - 1) mod n = (b - 1) mod n

f(i,j+1) - f(i,j) = [(a+1 mod n) - a] · n + [(b-1 mod n) - b]

If a < n-1 and b > 0: difference = n - 1.
If a < n-1 and b = 0: difference = n + (n-1) = 2n - 1. Bad!
If a = n-1 and b > 0: difference = -n·(n-1) + ... wait let me recompute.

a = n-1: a' = 0. So (a'-a) = 0 - (n-1) = -(n-1). Contribution: -(n-1)·n.
b > 0: b' = b-1. Contribution: -1.
Total: -(n-1)·n - 1 = -(n²-n) - 1. Absolute value: n² - n + 1. That's huge.

So this construction also has the wrap-around problem. The issue is that when a wraps from n-1 to 0, the value jumps by n² - n.

The fundamental problem: any labeling of the form v = a·n + b where a and b are linear functions of (i,j) will have wrap-around issues when a crosses the n-1 → 0 boundary.

To avoid this, we need a more sophisticated construction where the "high-order" coordinate doesn't wrap around at the same time as we traverse an edge.

Idea: Use a construction where the "row" index changes slowly. 

Consider the labeling where we traverse the torus in a "diagonal snake" pattern. 

Actually, let me think about this problem differently. Let me consider the problem on a path graph first (no wrap-around), then on a cycle, then on the torus.

On a path of n² vertices: label them 1, 2, ..., n² in order. Max edge difference = 1. Easy.

On a cycle of n² vertices: label them 1, 2, ..., n² in order. The wrap-around edge has difference n²-1. To minimize, use the zigzag: 1, n²/2+1, 2, n²/2+2, ..., n²/2, n². Max difference ≈ 2. Actually for a cycle of m vertices with labels 1..m, the minimum max adjacent difference is ⌈m/2⌉... no. 

For a cycle of m vertices with labels 1, 2, ..., m, the minimum possible maximum adjacent difference is ⌈(m-1)/⌊m/2⌋⌉... let me think. We need to arrange 1, ..., m on a cycle minimizing the max adjacent difference. 

The optimal arrangement: 1, 1+k, 1+2k, ... where k = ⌈m/2⌉. For m even: 1, m/2+1, 2, m/2+2, ..., m/2, m. Differences: m/2, m/2-1, m/2, m/2-1, ..., m/2, m/2-1, and the wrap: m - 1 = m-1. Hmm, that's not right.

Let me think again. For a cycle with labels 1, ..., m, arrange as: 1, ⌊m/2⌋+1, 2, ⌊m/2⌋+2, 3, ⌊m/2⌋+3, ..., ⌊m/2⌋, m, ⌊m/2⌋-1+1, ... 

Actually, the standard result: for a cycle of m vertices labeled 1 to m, the minimum max adjacent difference is ⌈m/2⌉. The arrangement is: 1, 1+⌈m/2⌉, 2, 2+⌈m/2⌉, 3, ... (interleaving the lower half and upper half). For m odd, ⌈m/2⌉ = (m+1)/2.

For m = n² with n odd, ⌈n²/2⌉ = (n²+1)/2. So on a Hamiltonian cycle of the torus, the minimum max adjacent difference would be (n²+1)/2, which is much larger than n+1. So the Hamiltonian cycle approach is bad.

This suggests that we shouldn't just use a Hamiltonian cycle—we need to use the 2D structure of the torus.

Let me reconsider. The torus has 2n² edges, and we're labeling n² vertices. The key is that the torus is 2-dimensional, not 1-dimensional.

Let me think about the construction more carefully.

Construction for D = n+1 on the n×n torus (n odd):

Consider the labeling v(i, j) = ((i · (n+1)/2 + j) mod n²) + 1.

Wait, this is a map from Z_n × Z_n to Z_{n²}. For it to be a bijection, we need i · (n+1)/2 + j to take all values 0, 1, ..., n²-1 exactly once as (i,j) ranges over Z_n × Z_n.

The values taken are: for each i ∈ {0,...,n-1} and j ∈ {0,...,n-1}, the value is i·(n+1)/2 + j mod n². 

For fixed i, as j ranges over 0..n-1, we get the values i·(n+1)/2, i·(n+1)/2 + 1, ..., i·(n+1)/2 + n-1 (mod n²). These are n consecutive values.

For different i, these blocks are: {i·(n+1)/2, ..., i·(n+1)/2 + n-1} for i = 0, 1, ..., n-1.

The blocks start at positions 0, (n+1)/2, 2(n+1)/2, 3(n+1)/2, ..., (n-1)(n+1)/2.

The start positions are 0, (n+1)/2, n+1, 3(n+1)/2, ..., (n-1)(n+1)/2 = (n²-1)/2.

Each block has length n. The gap between consecutive start positions is (n+1)/2. Since (n+1)/2 < n (for n ≥ 3), the blocks overlap! So this is NOT a bijection.

Let me try a different approach. 

Construction: v(i, j) = (i · n + j) mod n² + 1, but with a twist to handle wrap-around.

Actually, the standard row-by-row labeling v(i,j) = i·n + j + 1 has:
- Horizontal edges: difference 1 (except wrap: n-1)
- Vertical edges: difference n (except wrap: n²-n)

The problem is the vertical wrap (n²-n) and to a lesser extent the horizontal wrap (n-1).

What if we "shift" each row to handle the vertical wrap? 

Consider v(i, j) = (i·n + (j + s·i) mod n) + 1 where s is a shift parameter. This is a bijection (for each i, j → (j + s·i) mod n is a bijection on Z_n, and different i give different blocks of n values).

Horizontal edges: (i, j) → (i, j+1). v changes by 1 (if no wrap in j+s·i) or by 1-n (if wrap). So horizontal differences are 1 or n-1.

Vertical edges: (i, j) → (i+1, j). 
v(i, j) = i·n + (j + s·i) mod n + 1.
v(i+1, j) = (i+1)·n + (j + s·(i+1)) mod n + 1 = (i+1)·n + (j + s·i + s) mod n + 1.

Let b = (j + s·i) mod n. Then v(i,j) = i·n + b + 1.
v(i+1, j) = (i+1)·n + (b + s) mod n + 1.

If b + s < n: v(i+1,j) = (i+1)·n + b + s + 1 = i·n + n + b + s + 1. Difference = n + s.
If b + s ≥ n: v(i+1,j) = (i+1)·n + b + s - n + 1 = i·n + b + s + 1. Difference = s.

So vertical differences are n + s or s. To minimize the maximum, we want n + s to be small, so s should be small (or negative). But s ≥ 0 (it's a shift). If s = 0, we get the standard row-by-row with vertical differences n (except wrap). If s = 1, vertical differences are n+1 or 1.

With s = 1:
- Horizontal: 1 or n-1
- Vertical: n+1 or 1
- Vertical wrap (i = n-1 → i = 0): v(n-1, j) = (n-1)·n + (j + n-1) mod n + 1 = n² - n + (j-1) mod n + 1. v(0, j) = 0·n + j + 1 = j + 1. 
  Difference = |j + 1 - n² + n - ((j-1) mod n) - 1| = |j - n² + n - (j-1 mod n)|.
  If j > 0: (j-1) mod n = j-1. Difference = |j - n² + n - j + 1| = |n - n² + 1| = n² - n - 1. Huge!

So the vertical wrap-around is still a problem. The issue is that the last row and first row have very different label ranges.

To fix the vertical wrap, we need the last row and first row to have interleaved labels. This requires a more fundamental change to the construction.

Idea: Instead of filling row by row, fill in a "diagonal" order. 

Consider the labeling v(i, j) = ((i + j) mod n) · n + ((j - i·⌊n/2⌋) mod n) + 1... this is getting too complicated without more structure.

Let me try a completely different approach. 

Think of the torus as Z_n × Z_n. Consider the labeling:
v(i, j) = ((i + j) mod n²) + 1? No, this isn't a bijection since (i+j) only takes values 0 to 2(n-1), not 0 to n²-1.

OK let me think about this more carefully. We need a bijection from Z_n × Z_n to {1, ..., n²}. 

Since n is prime (2011 is prime), Z_n × Z_n is a 2-dimensional vector space over Z_n, and we can use linear algebra.

Consider the map φ: Z_n × Z_n → Z_n × Z_n given by (i, j) → (a₁i + b₁j, a₂i + b₂j) mod n, where the matrix [[a₁, b₁], [a₂, b₂]] is invertible mod n. Then v(i,j) = first_coord · n + second_coord + 1 is a bijection to {1, ..., n²}.

The edge differences depend on the matrix. Let's compute.

For a horizontal edge (i,j) → (i, j+1):
Δfirst = b₁, Δsecond = b₂ (mod n).
If no wrap: difference = b₁ · n + b₂.
If first wraps (depends on current value): difference involves ±n².

The wrap-around issue is fundamental for any linear map. When the first coordinate wraps from n-1 to 0, the value jumps by ±(n²-n).

So linear maps always have this problem. We need a non-linear construction.

Let me think about this differently. 

Maybe the answer is not n+1 but something larger. Let me reconsider the lower bound.

Better lower bound: Consider the cells labeled 1, 2, ..., n (call this set A) and cells labeled n²-n+1, ..., n² (call this set B). |A| = |B| = n. The label difference between any cell in A and any cell in B is at least n² - 2n + 1 = (n-1)².

Now, on the torus, consider the "distance" between A and B. If A and B are far apart, then any path from A to B is long, and the label difference accumulates. If A and B are close (some cell in A is adjacent to some cell in B), then we directly get a large edge difference.

Case 1: Some cell in A is adjacent to some cell in B. Then that edge has difference ≥ (n-1)². Since (n-1)² > n+1 for n ≥ 4, this gives a much better bound.

Case 2: A and B are not adjacent. Then the distance between A and B is at least 2. But we can say more.

Actually, this isn't quite right. The difference between a cell in A (label ≤ n) and a cell in B (label ≥ n²-n+1) is at least n²-2n+1. But if they're not adjacent, we need to find a path and use the intermediate cells.

Hmm, but the intermediate cells have labels between n+1 and n²-n, which could be anything. So the path from A to B might go through cells with labels that gradually increase, and the max edge difference on the path could be small.

So this approach doesn't directly give a better bound. The issue is that the labels could increase gradually along a path from A to B.

Let me reconsider. The lower bound of n+1 from the diameter argument seems hard to beat with simple arguments. Let me think about whether n+1 is actually the answer.

Let me try to construct a labeling with max edge difference n+1 for small n, say n=3.

For n=3, we need max edge difference ≤ 4. The 3×3 torus has 9 cells and 18 edges.

Let me try to find such a labeling by trial.

The cells are (i,j) for i,j ∈ {0,1,2}. Each cell has 4 neighbors.

Let me try:
```
Position (0,0)=1  (0,1)=2  (0,2)=3
Position (1,0)=5  (1,1)=6  (1,2)=4
Position (2,0)=9  (2,1)=7  (2,2)=8
```

Horizontal edges:
Row 0: |1-2|=1, |2-3|=1, |3-1|=2 (wrap)
Row 1: |5-6|=1, |6-4|=2, |4-5|=1 (wrap)
Row 2: |9-7|=2, |7-8|=1, |8-9|=1 (wrap)

Vertical edges:
Col 0: |1-5|=4, |5-9|=4, |9-1|=8 (wrap). BAD! 8 > 4.

The vertical wrap is the problem again. Let me try to make the first and last rows closer.

```
Position (0,0)=1  (0,1)=2  (0,2)=4
Position (1,0)=6  (1,1)=5  (1,2)=3
Position (2,0)=7  (2,1)=9  (2,2)=8
```

Horizontal:
Row 0: |1-2|=1, |2-4|=2, |4-1|=3
Row 1: |6-5|=1, |5-3|=2, |3-6|=3
Row 2: |7-9|=2, |9-8|=1, |8-7|=1

Vertical:
Col 0: |1-6|=5. BAD! 5 > 4.

Let me try yet another arrangement. The challenge is balancing both directions and both wrap-arounds.

```
Position (0,0)=1  (0,1)=3  (0,2)=5
Position (1,0)=4  (1,1)=6  (1,2)=8
Position (2,0)=7  (2,1)=9  (2,2)=2
```

Horizontal:
Row 0: |1-3|=2, |3-5|=2, |5-1|=4
Row 1: |4-6|=2, |6-8|=2, |8-4|=4
Row 2: |7-9|=2, |9-2|=7. BAD!

This is tricky. Let me try a more systematic approach.

For n=3, we need all 18 edges to have difference ≤ 4. Labels 1-9.

Let me think about which labels can be adjacent. Label 1 can be adjacent to labels 2, 3, 4, 5 (difference ≤ 4). Label 9 can be adjacent to 5, 6, 7, 8. Label 5 can be adjacent to 1, 2, 3, 4, 6, 7, 8, 9 (all). 

The constraint is that 1 and 9 cannot be adjacent (difference 8 > 4), 1 and 8 cannot be adjacent (7 > 4), 2 and 9 cannot be adjacent (7 > 4), 2 and 8 cannot be adjacent (6 > 4), 1 and 7 cannot be adjacent (6 > 4), 3 and 9 cannot be adjacent (6 > 4), 1 and 6 cannot be adjacent (5 > 4), 4 and 9 cannot be adjacent (5 > 4), 2 and 7 cannot be adjacent (5 > 4), 3 and 8 cannot be adjacent (5 > 4).

So the "forbidden" adjacencies (difference > 4) are:
(1,6), (1,7), (1,8), (1,9), (2,7), (2,8), (2,9), (3,8), (3,9), (4,9).

And by symmetry: (6,1), (7,1), (7,2), (8,1), (8,2), (8,3), (9,1), (9,2), (9,3), (9,4).

Each cell has 4 neighbors on the torus. Cell with label 1 can only be adjacent to {2,3,4,5}. Cell with label 9 can only be adjacent to {5,6,7,8}.

Let me try to construct this. Place 1 at (0,0). Its neighbors are (1,0), (2,0), (0,1), (0,2). These must be from {2,3,4,5}.

Place 9 at some cell not adjacent to 1. The cells not adjacent to 1 are (1,1), (1,2), (2,1), (2,2). Place 9 at (1,1). Its neighbors are (0,1), (2,1), (1,0), (1,2). These must be from {5,6,7,8}.

So the 4 neighbors of 1 are from {2,3,4,5} and the 4 neighbors of 9 are from {5,6,7,8}. The common element is 5. The neighbors of 1 are {(1,0), (2,0), (0,1), (0,2)} and neighbors of 9 are {(0,1), (2,1), (1,0), (1,2)}. Common cells: (0,1) and (1,0).

So (0,1) and (1,0) are neighbors of both 1 and 9. They must be in {2,3,4,5} ∩ {5,6,7,8} = {5}. But both can't be 5. Contradiction! So we can't have both (0,1) and (1,0) be 5.

Wait, actually only one of them needs to be in the intersection. Let me re-examine. (0,1) is a neighbor of 1 (at (0,0)) and a neighbor of 9 (at (1,1)). So (0,1) must be in {2,3,4,5} ∩ {5,6,7,8} = {5}. Similarly, (1,0) is a neighbor of both, so (1,0) must also be 5. But we can't have two cells with label 5. Contradiction!

So placing 1 and 9 at distance 2 (like (0,0) and (1,1)) doesn't work. What if 1 and 9 are at distance 2 but in a different configuration? On the 3×3 torus, distance 2 cells from (0,0) are: (1,1), (1,2), (2,1), (2,2). By the torus symmetry, all are equivalent. So no distance-2 placement works.

What if 1 and 9 are at distance 1 (adjacent)? Then the edge between them has difference 8 > 4. Not allowed.

What if 1 and 9 are at distance 3 = diameter? On the 3×3 torus, the diameter is 2 (since n=3, diameter = n-1 = 2). So the maximum distance is 2. There's no distance-3 pair.

So for n=3, we can't place 1 and 9 at distance > 2, and we've shown distance 2 doesn't work, and distance 1 doesn't work. This means M > 4 for n=3, i.e., M ≥ 5 = n+2.

Wait, let me double-check. For n=3, diameter = 2. The lower bound from diameter gives D ≥ (9-1)/2 = 4. But we just showed D=4 is impossible. So M ≥ 5 for n=3.

Hmm, so the answer is not n+1. Let me reconsider.

Actually wait, I need to recheck my argument. I showed that 1 and 9 can't be placed at distance 2 with max edge difference 4. But maybe I made an error.

Let me recheck: 1 at (0,0), 9 at (1,1). Neighbors of (0,0): (1,0), (2,0), (0,1), (0,2). Neighbors of (1,1): (0,1), (2,1), (1,0), (1,2). The cells (0,1) and (1,0) are neighbors of both. 

(0,1) must have label in {2,3,4,5} (neighbor of 1, so diff ≤ 4, so label ≤ 5) and in {5,6,7,8} (neighbor of 9, so diff ≤ 4, so label ≥ 5). So (0,1) = 5.
(1,0) must have label in {2,3,4,5} and in {5,6,7,8}. So (1,0) = 5. 

But both can't be 5. Contradiction. So indeed D=4 is impossible for n=3.

So M ≥ 5 for n=3. Is M = 5 achievable? Let me check.

With D=5, the forbidden adjacencies (diff > 5) are:
(1,7), (1,8), (1,9), (2,8), (2,9), (3,9).

So 1 can be adjacent to {2,3,4,5,6}, 9 can be adjacent to {4,5,6,7,8}.

Place 1 at (0,0), 9 at (1,1). Common neighbors: (0,1) and (1,0).
(0,1) must be in {2,3,4,5,6} ∩ {4,5,6,7,8} = {4,5,6}.
(1,0) must be in {4,5,6}.
So we need two distinct values from {4,5,6} for (0,1) and (1,0). That's possible.

Let's say (0,1) = 4, (1,0) = 5. 

Remaining: neighbors of 1: (2,0) and (0,2) must be in {2,3,4,5,6}. 4 and 5 are used, so from {2,3,6}.
Neighbors of 9: (2,1) and (1,2) must be in {4,5,6,7,8}. 4 and 5 are used, so from {6,7,8}.

Let (2,0) = 2, (0,2) = 3, (2,1) = 6, (1,2) = 7.
Remaining cells: (2,2) and the remaining labels: 8.
Wait, used so far: 1,4,5,2,3,6,7,9. Remaining: 8. And remaining cell: (2,2).

So (2,2) = 8.

Let me verify all edges:
```
(0,0)=1  (0,1)=4  (0,2)=3
(1,0)=5  (1,1)=9  (1,2)=7
(2,0)=2  (2,1)=6  (2,2)=8
```

Horizontal:
Row 0: |1-4|=3, |4-3|=1, |3-1|=2 (wrap). ✓
Row 1: |5-9|=4, |9-7|=2, |7-5|=2 (wrap). ✓
Row 2: |2-6|=4, |6-8|=2, |8-2|=6 (wrap). ✗! 6 > 5.

The wrap in row 2 gives |8-2| = 6 > 5. Bad.

Let me try different assignments. Let (2,0) = 3, (0,2) = 2, (2,1) = 8, (1,2) = 6.
Remaining: (2,2) = 7.

```
(0,0)=1  (0,1)=4  (0,2)=2
(1,0)=5  (1,1)=9  (1,2)=6
(2,0)=3  (2,1)=8  (2,2)=7
```

Horizontal:
Row 0: |1-4|=3, |4-2|=2, |2-1|=1. ✓
Row 1: |5-9|=4, |9-6|=3, |6-5|=1. ✓
Row 2: |3-8|=5, |8-7|=1, |7-3|=4. ✓

Vertical:
Col 0: |1-5|=4, |5-3|=2, |3-1|=2. ✓
Col 1: |4-9|=5, |9-8|=1, |8-4|=4. ✓
Col 2: |2-6|=4, |6-7|=1, |7-2|=5. ✓

All differences ≤ 5! So D=5 is achievable for n=3. And we showed D=4 is not. So M=5 for n=3.

Now, 5 = n+2 for n=3. But let me check: is the pattern n+2 or something else?

For n=2, M=2 = n. For n=3, M=5 = n+2. Hmm, these don't fit a simple pattern. Let me reconsider.

Wait, for n=2, the torus is a 4-cycle. M=2. n+2 = 4, which doesn't match. So the pattern might be different.

Actually, for n=2, the structure is very different (the torus is just a 4-cycle). Let me focus on odd n.

For n=3, M=5. Let me think about what 5 is in terms of n. 
- n+2 = 5 ✓
- (n²+1)/2 = 5 ✓ (since (9+1)/2 = 5)
- 2n-1 = 5 ✓

All three formulas give 5 for n=3. I need another data point to distinguish.

Let me try n=5. If the answer is n+2 = 7, or (n²+1)/2 = 13, or 2n-1 = 9, these are very different.

Let me think about the lower bound more carefully.

Refined lower bound: Consider cells with labels 1 and n². They're at distance at most d = (n-1)/2 · 2 = n-1 (diameter of the torus for odd n). Along a shortest path of length ≤ n-1, the max edge difference is ≥ (n²-1)/(n-1) = n+1.

But we showed for n=3 that n+1 = 4 is not achievable, and M = 5. So the lower bound of n+1 is not tight. We need a better lower bound.

Let me think about why n+1 fails for n=3. The issue was that 1 and 9 are at distance 2, and they have 2 common neighbors, both of which need to be in a small intersection.

Generalizing: Consider cells with labels 1 and n² on the n×n torus (n odd). They're at distance at most n-1. 

If they're at distance d, consider a shortest path of length d. The max edge difference on this path is ≥ (n²-1)/d. To minimize this, we want d as large as possible, so d = n-1 (diameter). This gives max diff ≥ n+1.

But the issue is more subtle. When 1 and n² are at distance d, the path between them has d edges and d-1 intermediate cells. These intermediate cells have labels between 1 and n², but they also have other neighbors (not on the path) that impose additional constraints.

Let me think about a better lower bound using the structure of the torus.

Alternative lower bound approach: Consider the "level sets" more carefully.

For each k from 1 to n²-1, let S_k = {cells with label ≤ k}. The edge boundary ∂S_k has |∂S_k| edges. 

Key fact: On the n×n torus, for any set S with |S| = s (where 1 ≤ s ≤ n²-1), the edge boundary |∂S| ≥ 2·min(s, n²-s)·... hmm, actually the isoperimetric inequality on the torus is more complex.

Actually, let me think about a specific level set. Consider S = {cells with labels 1, ..., n}. |S| = n. 

On the n×n torus, what is the minimum edge boundary of a set of size n?

A set of n cells on the n×n torus. The minimum edge boundary... If the n cells form a "row" (a cycle of length n), the edge boundary is 2n (each cell has 2 neighbors outside the row, in the vertical direction). If the n cells form a "diagonal" or some other shape, the boundary could be different.

Actually, for a set of n cells forming a path (not a cycle), the boundary would be... each internal cell of the path has 2 neighbors on the path and 2 outside, contributing 2 to the boundary. The 2 endpoints have 1 neighbor on the path and 3 outside, contributing 3 each. Total: 2(n-2) + 2·3 = 2n+2. But if the path wraps around and forms a cycle, the boundary is 2n.

For a "row" (cycle of length n), boundary = 2n. Can we do better? 

Consider n cells forming an L-shape or a square-ish shape. For n = 5, a 2×3 rectangle minus 1 cell = 5 cells. The boundary would be... this is getting complicated.

Let me think about the isoperimetric inequality on the torus more carefully. 

On the n×n torus, the edge isoperimetric function is known. For small sets (|S| ≤ n²/2), the minimum boundary is achieved by sets that are "as round as possible." 

For |S| = n on the n×n torus, the minimum edge boundary is 2n (achieved by a row or column, which is a cycle of length n). 

Wait, is that right? A row is a cycle of length n. Each cell in the row has 2 horizontal neighbors (in the row) and 2 vertical neighbors (outside the row). So the boundary is 2n. Can we do better?

Consider a "ball" of radius r in the torus graph. For n large, a ball of radius r has about 2r² cells and boundary about 4r. For |S| = n, we'd need r ≈ √(n/2), giving boundary ≈ 4√(n/2) ≈ 2√(2n). For large n, this is much less than 2n. So the minimum boundary for |S| = n is NOT 2n; it's closer to O(√n).

Hmm wait, but on the torus, the "ball" might wrap around. For n = 2011, a ball of radius r ≈ √(n/2) ≈ 31 doesn't wrap around, so the boundary is about 4r ≈ 124, much less than 2n = 4022.

So the minimum edge boundary of a set of size n on the n×n torus is O(√n), not 2n. This changes the analysis significantly.

Let me reconsider the lower bound using the sum of boundaries.

∑_{k=1}^{n²-1} |∂S_k| = ∑_{edges} |f(u) - f(v)| ≤ 2n² · D

where D is the max edge difference. So D ≥ (∑ |∂S_k|) / (2n²).

Now, ∑ |∂S_k| depends on the labeling. To get a lower bound on D that works for ALL labelings, we need a lower bound on ∑ |∂S_k| that holds for all labelings.

But ∑ |∂S_k| depends on the labeling (it determines the order in which cells are added to S_k). So we need: for any ordering of the cells, ∑_{k=1}^{n²-1} |∂S_k| ≥ some function of n.

This is related to the "profile" or "pathwidth" of the graph. Specifically, ∑ |∂S_k| is the "vertex isoperimetric profile" summed over all prefixes, which is related to the pathwidth.

Actually, ∑_{k=1}^{n²-1} |∂S_k| is the sum of edge boundaries over all prefixes of the ordering. This is minimized by the ordering that minimizes the maximum boundary (related to pathwidth), but we're summing, not maximizing.

Hmm, this is getting complex. Let me think about it differently.

Actually, let me think about the problem using a different lower bound technique.

Consider the n cells in any row of the torus. These n cells form a cycle of length n. Their labels are some n distinct values from {1, ..., n²}. 

For a cycle of length n with labels a_1 < a_2 < ... < a_n, the minimum possible maximum adjacent difference (over all arrangements on the cycle) is at least (a_n - a_1) / ⌊n/2⌋.

This is because on a cycle of length n, the maximum distance between any two vertices is ⌊n/2⌋. So the labels a_1 and a_n are at cycle-distance at most ⌊n/2⌋, and along the shorter arc, the max jump is at least (a_n - a_1)/⌊n/2⌋.

Now, consider all n rows. The labels are partitioned into n groups of n. Let the range of group i be r_i = max(group i) - min(group i). Then the max edge difference in row i is at least r_i / ⌊n/2⌋ = 2r_i / (n-1) (since n is odd, ⌊n/2⌋ = (n-1)/2).

The sum of ranges: ∑ r_i. Each r_i ≥ n-1 (since each group has n distinct values, the range is at least n-1). But we can say more.

Actually, the sum of ranges depends on how the labels are distributed among rows. In the worst case (for the lower bound), the labels are distributed to minimize the maximum range. If the labels are distributed as evenly as possible, each row gets a contiguous block of n labels, and the range of each row is n-1. Then the max edge difference per row is ≥ 2(n-1)/(n-1) = 2. That's a weak bound.

But we also have columns! Consider both rows and columns.

Hmm, this approach gives weak bounds when labels are distributed evenly among rows.

Let me think about a completely different approach.

Consider the "sorting" perspective. We have n² cells on the torus, labeled 1 to n². Consider the cell with label k. Define its "coordinate" in the sorted order as k. 

Now, think of the labels as defining a function on the torus. The "Lipschitz constant" of this function (max edge difference) is what we want to minimize.

This is related to the problem of embedding a grid into a line (or vice versa) with small distortion. 

Actually, I think the key insight is about the "bandwidth" of the torus graph. The bandwidth of a graph G is the minimum over all labelings of the maximum |f(u) - f(v)| over all edges uv. This is exactly our problem!

The bandwidth of the n×n torus (Cartesian product C_n × C_n) is a known graph theory parameter. Let me recall what it is.

The bandwidth of the n×n grid (P_n × P_n) is n. The bandwidth of the n×n torus (C_n × C_n) should be larger due to the wrap-around.

For the torus C_n × C_n, I believe the bandwidth is 2n - 1 for odd n. Let me check with n=3: 2·3 - 1 = 5. And we found M=5 for n=3. ✓

For n=2: 2·2 - 1 = 3. But we found M=2 for n=2. ✗. Hmm, but n=2 is even and the torus C_2 × C_2 is a multigraph (or has a different structure). Let me recheck n=2.

On the 2×2 torus, the graph is a 4-cycle (as I computed earlier). The bandwidth of a 4-cycle C_4 is 2. And 2n-1 = 3 ≠ 2. So the formula 2n-1 doesn't work for n=2.

But for odd n, the torus C_n × C_n is a 4-regular graph (no multi-edges), and the bandwidth might be 2n-1.

Let me check n=5: if the bandwidth is 2·5-1 = 9, then M = 9 for n=5.

Actually, let me look up the bandwidth of C_n × C_n. I recall that for the Cartesian product of cycles, the bandwidth has been studied.

The bandwidth of C_m × C_n (for m, n ≥ 3) is... I think it's 2·min(m, n) for even min(m,n) and 2·min(m,n) - 1 for odd min(m,n). But I'm not sure.

Actually, I recall that the bandwidth of the n-dimensional torus and grid graphs has been studied by various authors. For C_n × C_n with n odd, the bandwidth is 2n - 1.

Let me verify this with the lower bound. We need to show that for any labeling, some edge has difference ≥ 2n-1.

Lower bound for 2n-1: 

Consider the cells with labels 1, 2, ..., n and the cells with labels n²-n+1, ..., n². 

Hmm, let me think of a cleaner argument.

Consider the cell with label 1 and the cell with label n². They're at distance at most n-1 on the torus. Along a shortest path of length d ≤ n-1, the max edge difference is ≥ (n²-1)/d.

If d = n-1: max diff ≥ (n²-1)/(n-1) = n+1.
If d = (n-1)/2: max diff ≥ (n²-1)/((n-1)/2) = 2(n+1).
If d = 1: max diff ≥ n²-1.

So the lower bound depends on the distance between cells 1 and n². To get a bound of 2n-1, we need (n²-1)/d ≥ 2n-1, i.e., d ≤ (n²-1)/(2n-1) = (n+1)/2 · (n-1)/(n-1/2)... let me compute: (n²-1)/(2n-1) = (n-1)(n+1)/(2n-1). For large n, this is approximately n/2. So we need d ≤ ~n/2.

But the distance between cells 1 and n² could be as large as n-1 (the diameter). So this approach only gives n+1, not 2n-1.

We need a different approach for the 2n-1 bound. Let me think...

Alternative approach: Consider the n cells in a "row" (a horizontal cycle). Actually, let me think about "antipodal" cells.

On the n×n torus (n odd), for each cell (i,j), the "antipodal" cell is (i + (n-1)/2, j + (n-1)/2), which is at distance n-1 (the diameter). 

Hmm, that's not quite right. The distance between (i,j) and (i+(n-1)/2, j+(n-1)/2) is (n-1)/2 + (n-1)/2 = n-1. Yes, that's the diameter.

Consider the cell with label 1 at position (i,j) and the cell with label n² at position (i', j'). The distance is at most n-1. 

Now, consider a "geodesic" (shortest path) from (i,j) to (i',j'). This path has length d ≤ n-1 and consists of horizontal and vertical steps. 

But I need a stronger argument. Let me think about using multiple cells, not just the extremes.

Consider the following approach. Take the cells labeled 1, 2, ..., n+1. These n+1 cells are on the torus. By the pigeonhole principle, at least two of them are at distance at most... well, n+1 cells on an n×n torus. The torus has n² cells. By pigeonhole, two of the n+1 cells are in the same "row" or... hmm, not directly useful.

Let me try another approach. 

Consider the set A = {cells with labels 1, ..., n} and B = {cells with labels n²-n+1, ..., n²}. |A| = |B| = n. 

The minimum label in B is n²-n+1 and the maximum label in A is n. So any edge between A and B has difference ≥ n²-2n+1 = (n-1)².

Now, on the torus, what's the minimum "distance" between A and B? If some cell in A is adjacent to some cell in B, we get an edge with difference ≥ (n-1)², which is much larger than 2n-1 for n ≥ 5. 

But if A and B are far apart, we need to find a path and use intermediate cells. The issue is that intermediate cells could have labels that bridge the gap smoothly.

Let me think about this more carefully. Consider the "annulus" between A and B. The cells with labels n+1, ..., n²-n form a "middle" set of size n²-2n. 

Hmm, I think the right approach is to consider the "vertex boundary" and use the structure of the torus.

Let me try a different lower bound argument.

Consider the n rows of the torus. Each row is a cycle of length n. The labels in row r are some set L_r of n values. The max edge difference within row r is at least (max L_r - min L_r) / ((n-1)/2) = 2(max L_r - min L_r)/(n-1).

Similarly for columns.

Now, consider the "vertical" edges. Between row r and row r+1, there are n vertical edges. The difference on vertical edge (r, c) ↔ (r+1, c) is |f(r,c) - f(r+1,c)|.

Hmm, I think I need to use a more global argument. Let me try the following:

Consider the n cells with the smallest labels: {1, 2, ..., n}. These cells are distributed among the n rows. By pigeonhole, at least one row contains at least 2 of these cells (if n > n, wait, n cells in n rows, so it's possible each row has exactly 1). Actually, n cells in n rows: it's possible each row has exactly 1 cell from {1,...,n}.

Similarly, the n cells with the largest labels {n²-n+1, ..., n²} are distributed among n rows, possibly one per row.

This doesn't immediately help. Let me think about the problem differently.

Let me try to think about what construction achieves bandwidth 2n-1 for the torus.

Construction for the n×n torus with bandwidth 2n-1 (n odd):

Consider the "diagonal" labeling. For each "diagonal" d = 0, 1, ..., n-1, the diagonal consists of cells (i, (d-i) mod n) for i = 0, ..., n-1. Each diagonal is a cycle of length n (it wraps around in both directions).

Wait, actually each diagonal on the torus is a cycle of length n (since n is odd, the diagonal (i, i+d mod n) for i=0..n-1 visits all n cells in the diagonal, and it's a cycle because the torus wraps).

Hmm, actually the "diagonal" (i, i+d) for i=0,...,n-1: when i goes from 0 to n-1, j = i+d mod n also goes through all values. The next cell after (n-1, n-1+d) would be (0, d) which is (n, n+d) mod n = (0, d). And (n-1, n-1+d) to (0, d): the difference in i is 1 (wrapping) and in j is 1 (wrapping). So this is a "diagonal" step, not a horizontal or vertical step. So the diagonal is not a cycle in the torus graph.

Let me reconsider. The diagonal (i, (d+i) mod n) for i = 0, ..., n-1 consists of n cells, but consecutive cells in this diagonal differ by (1, 1), which is not an edge of the torus (edges are (1,0) and (0,1) steps). So diagonals are not cycles in the torus graph.

OK so let me think about the construction differently.

For the bandwidth of C_n × C_n, let me think about what labeling achieves 2n-1.

I think the construction is: label the cells in "diagonal" order. Specifically, order the cells by their "diagonal index" i+j mod n, and within each diagonal, by i.

Cell (i, j) gets label: (number of cells in diagonals 0, 1, ..., (i+j-1) mod n) + (position within diagonal (i+j) mod n) + 1.

Since each diagonal has n cells, the label of (i, j) is: ((i+j) mod n) · n + i + 1.

Wait, this is the same as v(i,j) = ((i+j) mod n) · n + i + 1. Let me check if this is a bijection. For each value of (i+j) mod n = d, the cells are (i, (d-i) mod n) for i = 0, ..., n-1. These get labels d·n + i + 1 for i = 0, ..., n-1, which are d·n + 1, ..., d·n + n. So yes, it's a bijection to {1, ..., n²}.

Now let's compute edge differences.

Horizontal edge (i, j) → (i, j+1):
v(i, j) = ((i+j) mod n) · n + i + 1.
v(i, j+1) = ((i+j+1) mod n) · n + i + 1.

If i+j < n-1 (mod n): (i+j) mod n = i+j, (i+j+1) mod n = i+j+1. Difference = n.
If i+j ≡ n-1 (mod n): (i+j) mod n = n-1, (i+j+1) mod n = 0. Difference = |0·n + i + 1 - (n-1)·n - i - 1| = |i + 1 - n² + n + i + 1| = |2i + 2 + n - n²|. For i = 0, ..., n-1, this is |2i + 2 + n - n²|. The maximum is at i = n-1: |2n + n - n²| = |3n - n²| = n² - 3n. That's huge!

So this construction has huge differences at the wrap-around. Not good.

The issue is the same as before: the "diagonal index" wraps around, causing a big jump.

Let me think about a different construction. 

Maybe the construction that achieves 2n-1 is not based on diagonals but on something else.

Let me think about the n=3 case where we found a valid labeling:
```
(0,0)=1  (0,1)=4  (0,2)=2
(1,0)=5  (1,1)=9  (1,2)=6
(2,0)=3  (2,1)=8  (2,2)=7
```

Let me see the pattern. The labels by position:
- Diagonal 0 (i+j ≡ 0): (0,0)=1, (1,2)=6, (2,1)=8. Labels: 1, 6, 8.
- Diagonal 1 (i+j ≡ 1): (0,1)=4, (1,0)=5, (2,2)=7. Labels: 4, 5, 7.
- Diagonal 2 (i+j ≡ 2): (0,2)=2, (1,1)=9, (2,0)=3. Labels: 2, 9, 3.

Hmm, the labels within each diagonal aren't consecutive. Let me look at the structure differently.

Let me look at the "snake" pattern. Reading the labels in order 1, 2, 3, ..., 9:
1: (0,0)
2: (0,2)
3: (2,0)
4: (0,1)
5: (1,0)
6: (1,2)
7: (2,2)
8: (2,1)
9: (1,1)

The path 1→2→3→4→5→6→7→8→9 visits:
(0,0) → (0,2) [distance 1, wrap] → (2,0) [distance 2] → (0,1) [distance 2] → (1,0) [distance 1] → (1,2) [distance 1, wrap] → (2,2) [distance 1] → (2,1) [distance 1] → (1,1) [distance 1]

So consecutive labels are sometimes at distance 1 (adjacent) and sometimes at distance 2. The max edge difference is 5, not 1, so consecutive labels aren't always adjacent.

Let me look at the differences more carefully:
- The edge (0,0)-(0,2) has |1-2| = 1. ✓ (these are adjacent on the torus, wrap-around)
- But (0,2) and (2,0) are at distance 2, not adjacent. The label difference |2-3| = 1, but they're not adjacent so this doesn't count.

The max edge difference is max over all 18 edges. We computed all are ≤ 5. The edges with difference 5 are: (0,1)-(1,1) with |4-9|=5, and (2,2)-(0,2) with |7-2|=5 (vertical wrap).

Let me think about the general construction. 

Actually, let me try to think about this problem from the perspective of the known result. I believe the bandwidth of C_n × C_n for odd n is 2n-1. Let me try to prove this.

Lower bound (M ≥ 2n-1):

Consider the n cells with labels 1, 2, ..., n. Call this set A. Consider the n cells with labels n²-n+1, ..., n². Call this set B.

Consider the "separation" between A and B on the torus. 

Define the "annular" region: cells at distance exactly k from A. The cells in B must be at some distance from A.

Actually, let me use a different approach. Consider the cells labeled 1, 2, ..., 2n-1. There are 2n-1 such cells. 

Hmm, let me think about the problem using the concept of "bandwidth" more directly.

The bandwidth of a graph G is min over all bijections f: V → {1, ..., |V|} of max_{uv ∈ E} |f(u) - f(v)|.

There's a known lower bound for bandwidth using the "local density" or "isoperimetric" approach:

bw(G) ≥ max_{S ⊆ V, S ≠ ∅} (|N(S)| / something)... 

Actually, a standard lower bound is: bw(G) ≥ max_{v ∈ V} (|N(v)|) = maximum degree. For the torus, max degree = 4, so bw ≥ 4. Not useful.

A better bound: bw(G) ≥ max_{S ⊆ V} ⌈|∂S| / something⌉... 

Actually, the standard lower bound is: for any set S, bw(G) ≥ |∂_V S| where ∂_V S is the vertex boundary (vertices not in S but adjacent to S). Wait, that's not right either.

Let me recall: the bandwidth is related to the pathwidth. Specifically, bw(G) ≥ pw(G) (pathwidth) and bw(G) ≥ vs(G) (vertex separation). Actually, I think pw(G) = vs(G) and bw(G) ≥ pw(G).

The vertex separation of an ordering v_1, ..., v_N is max_k |{v_j : j > k, ∃ i ≤ k, v_i v_j ∈ E}|. The vertex separation of G is the minimum over all orderings.

The pathwidth of C_n × C_n... for the n×n grid P_n × P_n, the pathwidth is n. For the torus C_n × C_n, the pathwidth should be 2n-1 or similar.

Actually, I recall that the pathwidth of C_n × C_n is 2n-2 for even n and 2n-1 for odd n. And bandwidth ≥ pathwidth. But I need to verify this.

Hmm, let me think about the vertex separation lower bound directly.

Consider any ordering of the n² cells. At some point, exactly n cells have been "processed" (labeled 1 to n). Call this set S. The vertex boundary of S (cells not in S but adjacent to S) has size at least... 

On the n×n torus, for a set S of size n, the vertex boundary has size at least... 

If S is a row (cycle of length n), the vertex boundary consists of the 2n cells in the adjacent rows (row above and row below), but wait, each cell in the row has 2 vertical neighbors, and these are all distinct (since the row is a cycle and the vertical neighbors are in different rows). So the vertex boundary is 2n (the n cells in the row above and n cells in the row below). But the row above and below might share cells if n is small. For n ≥ 3, they're distinct. So vertex boundary = 2n.

But can we do better? If S is a "ball" of size n, the vertex boundary is O(√n), much less than 2n. So the minimum vertex boundary for |S| = n is O(√n), not 2n.

So the vertex separation at the point where |S| = n could be as small as O(√n), which doesn't give us 2n-1.

The vertex separation is the MAXIMUM over all k of the vertex boundary of the first k cells. So we need to find the k where the vertex boundary is largest.

For the torus, the vertex boundary is largest when S is about half the torus. When |S| = n²/2, the vertex boundary is... for a "half-torus" (say, the first n/2 rows), the boundary is 2n (the two boundary rows). But for a "round" set of size n²/2, the boundary is O(n). 

Actually, for the torus, the vertex isoperimetric function at n²/2 is Θ(n). The minimum vertex boundary for a set of size n²/2 is n (achieved by taking n/2 consecutive rows, giving boundary 2n... wait, that's 2n).

Hmm, let me think more carefully. If we take ⌊n/2⌋ consecutive rows (out of n rows), that's ⌊n/2⌋ · n cells. The boundary is 2n (the row above and the row below the block). For n odd, ⌊n/2⌋ = (n-1)/2, so |S| = (n-1)n/2, and boundary = 2n.

Can we do better with a different shape? A "round" set of size ~n²/2 would have boundary ~2√(n²/2) · something... actually, on the torus, a "ball" of radius r has about 2r² cells and boundary about 4r. For |S| = n²/2, r ≈ n/2, and boundary ≈ 2n. So it's about the same.

So the vertex separation of the torus is about 2n. More precisely, for odd n, I believe the vertex separation (and hence bandwidth) of C_n × C_n is 2n-1.

But I need to prove this rigorously. Let me think about the lower bound more carefully.

Lower bound: bw(C_n × C_n) ≥ 2n-1 for odd n.

Proof attempt: Consider any labeling f. Consider the cells with labels 1, ..., k for some k to be chosen. Let S = {v : f(v) ≤ k}. The vertex boundary ∂S = {v ∉ S : ∃ u ∈ S, uv ∈ E}. Every vertex in ∂S has label > k, and is adjacent to a vertex with label ≤ k. So for each v ∈ ∂S, there's an edge uv with f(u) ≤ k < f(v), and |f(u) - f(v)| ≥ f(v) - k ≥ 1. But we want a larger bound.

Actually, the bandwidth bound from vertex separation is: bw(G) ≥ max_k |∂S_k| where S_k = {v : f(v) ≤ k} and ∂S_k is the vertex boundary. This is because each vertex in ∂S_k is adjacent to some vertex in S_k, and the label difference is at least 1, but actually the bound is:

For each v ∈ ∂S_k, there's an edge uv with u ∈ S_k (f(u) ≤ k) and v ∉ S_k (f(v) > k). The difference |f(u) - f(v)| ≥ 1. But we need to relate this to |∂S_k|.

The standard argument: the vertices in ∂S_k have labels in {k+1, k+2, ..., k + bw} (since each is adjacent to a vertex with label ≤ k, so the difference is ≤ bw, meaning f(v) ≤ k + bw). So |∂S_k| ≤ bw. Therefore bw ≥ max_k |∂S_k|.

So bw ≥ max_k |∂S_k|, and we need to show that for any ordering, max_k |∂S_k| ≥ 2n-1.

This is the vertex separation number of the torus, which we need to show is ≥ 2n-1.

Claim: For any set S with (n-1)n/2 ≤ |S| ≤ (n+1)n/2 (i.e., |S| ≈ n²/2), the vertex boundary |∂S| ≥ 2n-1.

Wait, actually we need: for any ordering, there exists some k such that |∂S_k| ≥ 2n-1. This is equivalent to saying the vertex separation of C_n × C_n is ≥ 2n-1.

Let me think about why the vertex separation is 2n-1.

Consider any set S with |S| = ⌊n²/2⌋ = (n²-1)/2 (for odd n). We need to show |∂S| ≥ 2n-1.

On the n×n torus, consider the "rows" (horizontal cycles). Each row has n cells. Let a_i = |S ∩ row i| for i = 0, ..., n-1. Then ∑ a_i = |S| = (n²-1)/2.

The vertex boundary of S includes:
- For each row i, the cells in row i that are not in S but are horizontally adjacent to a cell in S ∩ row i.
- For each pair of adjacent rows (i, i+1), the cells in row i+1 that are not in S but are vertically adjacent to a cell in S ∩ row i, and vice versa.

This is complex. Let me think about a simpler approach.

Alternative approach: Consider the "columns" of the torus. Each column is a cycle of length n. For each column c, let b_c = |S ∩ column c|. Then ∑ b_c = |S|.

If S contains an entire column (b_c = n), then the two adjacent columns contribute at least 2 cells to the boundary (the cells in the adjacent columns that are vertically adjacent to the cells in column c). Actually, each cell in column c has 2 horizontal neighbors, one in each adjacent column. So the adjacent columns have at most n cells each in the boundary, but at least... well, if the adjacent columns are entirely outside S, then all n cells in each adjacent column are in the boundary (each is adjacent to a cell in column c). So the boundary is at least 2n.

But this is for a specific S. We need a bound that works for all S of size (n²-1)/2.

Let me try a different approach. I'll use the "isoperimetric inequality" on the torus.

On the n×n torus (n odd), the vertex isoperimetric inequality states that for a set S with |S| = s ≤ n²/2, the vertex boundary |∂S| ≥ min over all sets of size s of |∂S|. 

For the torus, the optimal sets are "balls" in the L1 metric (diamonds). A ball of radius r has |B_r| = 2r² + 2r + 1 (for r < (n-1)/2) and |∂B_r| = 4r + 4 (for r < (n-1)/2).

Wait, let me recalculate. On the torus Z_n × Z_n with L1 distance, a ball of radius r (for r < n/2) centered at the origin is {(x,y) : |x| + |y| ≤ r} where |x| = min(x, n-x). For r < (n-1)/2, this is the same as on the infinite grid. The ball has 1 + 4·(1 + 2 + ... + r) = 1 + 2r(r+1) = 2r² + 2r + 1 cells. The boundary has 4(r+1) cells.

For |S| = (n²-1)/2, we need 2r² + 2r + 1 ≈ n²/2, so r ≈ n/2. But r < (n-1)/2 is required for the ball not to wrap around. For r = (n-3)/2, |B_r| = 2((n-3)/2)² + 2(n-3)/2 + 1 = (n-3)²/2 + (n-3) + 1 = (n²-6n+9)/2 + n - 2 = (n²-6n+9+2n-4)/2 = (n²-4n+5)/2. And |∂B_r| = 4((n-3)/2 + 1) = 4(n-1)/2 = 2(n-1) = 2n-2.

For r = (n-1)/2, the ball starts to wrap around. |B_{(n-1)/2}| = 2((n-1)/2)² + 2(n-1)/2 + 1 = (n-1)²/2 + (n-1) + 1 = (n²-2n+1)/2 + n = (n²-2n+1+2n)/2 = (n²+1)/2. And the boundary... when r = (n-1)/2, the ball touches itself on the torus, so the boundary is different.

For r = (n-1)/2, the ball B_r = {(x,y) : |x| + |y| ≤ (n-1)/2}. On the torus, |x| ranges from 0 to (n-1)/2 and |y| from 0 to (n-1)/2. The constraint |x| + |y| ≤ (n-1)/2 with |x|, |y| ∈ {0, 1, ..., (n-1)/2}. This gives (n²+1)/2 cells (more than half the torus). The boundary is the set of cells with |x| + |y| = (n+1)/2, but on the torus, |x| + |y| = (n+1)/2 means |x| + |y| = (n+1)/2, and since |x| ≤ (n-1)/2 and |y| ≤ (n-1)/2, we need |x| + |y| = (n+1)/2 with both ≤ (n-1)/2. The number of such cells is... |x| can range from 1 to (n-1)/2 (since |y| = (n+1)/2 - |x| ≥ 1). For each |x| from 1 to (n-1)/2, |y| = (n+1)/2 - |x| from (n-1)/2 down to 1. The number of cells with given (|x|, |y|) is: 4 if both > 0, 2 if one is 0. Here both are always > 0, so 4 cells per (|x|, |y|) pair. Number of pairs: (n-1)/2. So boundary = 4 · (n-1)/2 = 2(n-1) = 2n-2.

Hmm, so the ball of radius (n-1)/2 has (n²+1)/2 cells and boundary 2n-2. But (n²+1)/2 > n²/2, so this is more than half. For |S| = (n²-1)/2 (just under half), the ball of radius (n-3)/2 has (n²-4n+5)/2 cells, which is less than (n²-1)/2. So we need a set slightly larger than the ball of radius (n-3)/2.

The ball of radius (n-3)/2 has (n²-4n+5)/2 cells and boundary 2n-2. We need to add (n²-1)/2 - (n²-4n+5)/2 = (4n-4)/2 = 2n-2 more cells. Adding cells to the ball can only increase or maintain the boundary (adding a boundary cell to S removes it from the boundary but might add new boundary cells). 

Actually, adding a boundary cell to S removes it from the boundary but might add its neighbors (that aren't in S) to the boundary. So the boundary could increase or decrease.

This is getting complicated. Let me try a cleaner approach to the lower bound.

Cleaner lower bound approach:

I'll show that for any labeling of the n×n torus (n odd), there's an edge with difference ≥ 2n-1.

Consider the cells with labels 1, 2, ..., n. Call this set A. |A| = n. 

On the torus, the n cells in A are distributed somehow. Consider the "rows" (horizontal cycles). Let a_i = |A ∩ row i|. Then ∑ a_i = n.

Similarly, consider the "columns" (vertical cycles). Let b_j = |A ∩ column j|. Then ∑ b_j = n.

Now, consider the complement of A, which has n² - n cells. The cells with labels n+1, ..., n² are in the complement.

The vertex boundary of A, ∂A, consists of cells not in A that are adjacent to some cell in A. Each cell in ∂A has label ≥ n+1 and is adjacent to a cell with label ≤ n. So the edge connecting them has difference ≥ (n+1) - n = 1. But we want a larger bound.

Actually, the key insight for the bandwidth lower bound is:

The cells in ∂A all have labels > n (since A = {labels 1,...,n}). Each cell in ∂A is adjacent to a cell in A (label ≤ n). So the label of each cell in ∂A is at most n + bw (since the edge difference is ≤ bw). So all cells in ∂A have labels in {n+1, ..., n + bw}. Therefore |∂A| ≤ bw.

So bw ≥ |∂A|. Now we need to show |∂A| ≥ 2n-1 for any set A of size n on the n×n torus (n odd).

Wait, but A is a specific set (the cells with the n smallest labels), and its structure depends on the labeling. We need to show that for ANY set A of size n, |∂A| ≥ 2n-1.

Is this true? Let me check for n=3. Any set of 3 cells on the 3×3 torus has vertex boundary ≥ 5 = 2·3-1.

The 3×3 torus has 9 cells, each with 4 neighbors. A set of 3 cells:
- If the 3 cells form a "row" (cycle of length 3): boundary = 6 (the other 2 rows, each with 3 cells, all adjacent to the row). Wait, each cell in the row has 2 vertical neighbors. The 3 cells in the row have 6 vertical neighbors, but some might overlap. On the 3×3 torus, row 0 = {(0,0), (0,1), (0,2)}. Vertical neighbors: (1,0), (2,0), (1,1), (2,1), (1,2), (2,2) = all 6 cells not in the row. So boundary = 6 ≥ 5. ✓

- If the 3 cells form an "L" shape, say {(0,0), (0,1), (1,0)}: 
  Neighbors of (0,0) not in A: (2,0), (0,2). 
  Neighbors of (0,1) not in A: (1,1), (2,1), (0,2). 
  Neighbors of (1,0) not in A: (2,0), (1,1), (1,2). 
  Boundary = {(2,0), (0,2), (1,1), (2,1), (1,2)} = 5. ✓

- If the 3 cells form a "diagonal", say {(0,0), (1,1), (2,2)}:
  Neighbors of (0,0): (1,0), (2,0), (0,1), (0,2).
  Neighbors of (1,1): (0,1), (2,1), (1,0), (1,2).
  Neighbors of (2,2): (1,2), (0,2), (2,1), (2,0).
  Boundary = {(1,0), (2,0), (0,1), (0,2), (2,1), (1,2)} = 6. ✓

So for n=3, any set of 3 cells has boundary ≥ 5 = 2n-1. 

Now let me prove this for general odd n.

Claim: On the n×n torus (n odd), any set A of n cells has vertex boundary |∂A| ≥ 2n-1.

Proof: Consider the n rows. Let a_i = |A ∩ row i|, so ∑ a_i = n. 

Case 1: Some row has a_i = 0. Then there's a row with no cells of A. The rows adjacent to this empty row... hmm, this doesn't directly help.

Let me think about this differently. 

Consider the "row boundary": cells in ∂A that are in the same row as a cell of A but not in A. For each row i with 0 < a_i < n, the row boundary in row i is at least 2 (since A ∩ row i is a proper nonempty subset of a cycle of length n, and any such subset has at least 2 boundary vertices on the cycle). Actually, for a subset of a cycle of length n with a_i elements, the vertex boundary on the cycle is at least 2 (if 0 < a_i < n). 

Wait, that's the boundary within the cycle. But we also have the vertical boundary.

Let me separate the boundary into horizontal and vertical components.

Horizontal boundary: cells in ∂A that are in the same row as some cell of A, and are horizontally adjacent to a cell of A. For row i with a_i cells of A (0 < a_i < n), the horizontal boundary in row i is at least 2 (the cycle boundary). If a_i = n, horizontal boundary in row i is 0. If a_i = 0, horizontal boundary in row i is 0 (no cells of A in this row).

Vertical boundary: cells in ∂A that are vertically adjacent to a cell of A. For each cell (i,j) ∈ A, its vertical neighbors (i±1, j) are in ∂A if they're not in A. 

The total boundary is at least the horizontal boundary plus the vertical boundary (minus possible overlaps, but let's not worry about that for a lower bound).

Hmm, this is getting complicated because of overlaps. Let me try a different approach.

Alternative proof of the claim:

Consider the n rows. If all a_i ∈ {0, n}, then since ∑ a_i = n and each a_i is 0 or n, exactly one row has a_i = n and the rest have a_i = 0. Then A is an entire row. The boundary is the 2n cells in the two adjacent rows (each cell in A has 2 vertical neighbors, all distinct, giving 2n boundary cells). So |∂A| = 2n ≥ 2n-1. ✓

If some row has 0 < a_i < n, then the horizontal boundary in that row is at least 2. But we also need to count the vertical boundary.

Let me try to use a different method. 

Method: Count the number of edges between A and V\A. Each cell in A has degree 4, so the total number of edges incident to A is 4n (with multiplicity, counting edges within A twice). The number of edges within A is e(A). The number of edges between A and V\A is 4n - 2e(A). Each boundary vertex is incident to at least 1 such edge, so |∂A| ≤ 4n - 2e(A). But we want a lower bound on |∂A|, not an upper bound.

For a lower bound on |∂A|: each boundary vertex is incident to at most 4 edges from A, so |∂A| ≥ (4n - 2e(A)) / 4 = n - e(A)/2. To minimize |∂A|, we maximize e(A). 

What's the maximum number of edges within a set of n cells on the n×n torus? If the n cells form a cycle (a row),
