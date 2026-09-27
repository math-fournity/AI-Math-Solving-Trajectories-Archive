# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   A coloring of all plane points with coordinates belonging to the set $S=\{0,1,\ldots,99\}$ into red and white colors is said to be [i]critical[/i] if for each $i,j\in S$ at least one of the four points $(i,j),(i + 1,j),(i,j + 1)$ and $(i + 1, j + 1)$ $(99 + 1\equiv0)$ is colored red. Find the maximal possible number of red points in a critical coloring which loses its property after recoloring of any red point into white.       — 题目文本
#   To solve this problem, we need to find the maximal number of red points in a critical coloring of the plane points with coordinates in the set \( S = \{0, 1, \ldots, 99\} \). A coloring is critical if for each \( i, j \in S \), at least one of the four points \((i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)\) is colored red, with the condition that \(99 + 1 \equiv 0\).

1. **Initial Setup and Definitions**:
   - Let \( r \) be the number of red points.
   - We need to ensure that each 2x2 square on the grid contains at least one red point.
   - We aim to find the maximum \( r \) such that the coloring is critical and loses its property if any red point is recolored to white.

2. **Constructing the Argument**:
   - Consider the grid as a collection of \( 100 \times 100 = 10000 \) points.
   - We need to cover each 2x2 square with at least one red point.
   - Suppose we have \( r \) red points. We can choose \( r \) 2x2 squares, each containing exactly one red point, ensuring that each red point is in one of these squares.

3. **Average Calculation**:
   - In each white cell, write the number of chosen squares that contain it.
   - The average number written in the white cells is given by:
     \[
     \frac{3r}{10000 - r}
     \]
   - This average is increasing with \( r \) and equals 3 when \( r = 5000 \).

4. **Bounding the Average**:
   - We claim that this average cannot be more than 3.
   - If a number greater than 3 is written in a white cell, then the number must be 4, and it must come in the following configuration:
     \[
     \begin{array}{ccc}
     R & 2 & R \\
     2 & 4 & 2 \\
     R & 2 & R \\
     \end{array}
     \]
     Here, \( R \) represents a red cell, and the numbers are what's written in the white cells.

5. **Pairing and Averaging**:
   - We can pair each occurrence of 4 with the white cell with 2 right above it, and the average of this pair is 3.
   - No white cell is part of two pairs, so by averaging over these pairs and unpaired white cells, we get the average of numbers on the whole board is at most 3.

6. **Conclusion**:
   - Since the average cannot exceed 3, the maximum number of red points \( r \) that satisfies the critical coloring condition is 5000.
   - If we have more than 5000 red points, the average would exceed 3, which is not possible.

The final answer is \( \boxed{5000} \)  — 标准解答
#   Let me solve this problem. We have a 100×100 toroidal grid (indices 0..99 with wraparound), colored red/white. Critical means: for every unit square (2×2 cell) with corners (i,j),(i+1,j),(i,j+1),(i+1,j+1), at least one is red. We want a critical coloring that is minimal in the sense that removing any red point (turning it white) destroys criticality. Find the maximum number of red points in such a minimal critical coloring.

So we want a maximal minimal hitting set: a set R of red points such that:
1. R hits every 2×2 square (every unit cell has ≥1 red point).
2. R is minimal: every red point is essential, i.e., for each red point p, there exists a 2×2 square where p is the only red point.
3. We want to maximize |R|.

This is a classic problem about minimal hitting sets / minimal vertex covers on the hypergraph of 2×2 cells. Each cell is a 4-element hyperedge. We want a minimal transversal (minimal hitting set) of maximum size.

A minimal transversal T of a hypergraph H: T hits every edge, and for every t in T, there's an edge e with e ∩ T = {t} (t is the unique representative of that edge).

We want the maximum size of a minimal transversal.

Let me think about the structure. The grid is 100×100 torus. Cells are indexed by (i,j) with i,j in 0..99, each cell C(i,j) = {(i,j),(i+1,j),(i,j+1),(i+1,j+1)} mod 100.

We want max minimal transversal.

Upper bound approach: For a minimal transversal, each red point needs a "private" cell where it's the only red point. So we can assign to each red point a distinct cell (the private cell). Actually each red point needs at least one private cell, but multiple red points could share... no. A private cell for red point p is a cell where p is the only red point. Two different red points can't share the same private cell (since a cell has only one red point in it as private). So the number of red points ≤ number of cells = 100×100 = 10000. But that's trivial (total points = 10000).

Wait, but each red point needs a private cell, and private cells are distinct. There are 10000 cells. So |R| ≤ 10000, trivially. We need a better bound.

Hmm, but actually the constraint is tighter. Let me think about it differently.

Let me think about which colorings are minimal critical and how many red points.

Consider the complement: white points W. Critical means every 2×2 cell has at least one red = not all-white. So W contains no 2×2 all-white block... no wait, every cell has at least one red means no cell is all white. So W is a set with no 2×2 all-white square, i.e., W has no "full cell". Equivalent: W is a subset such that no 2×2 block is entirely in W.

Minimality: every red point p has a private cell = a cell where the other 3 points are all white. So for each red point p, there's a cell containing p where the other 3 corners are white.

So we want to maximize red = minimize white, but with the constraint that every red point has a cell where it's surrounded by 3 white points (the other 3 corners of some cell are white).

Hmm, let me think about the maximum. Let me consider small cases first to get intuition, like a 1D analog or small torus.

Actually let me think about the structure of private cells. Each red point p=(a,b) is a corner of 4 cells: C(a-1,b-1), C(a-1,b), C(a,b-1), C(a,b) (the cells for which p is bottom-right, bottom-left, top-right, top-left respectively). For p to have a private cell, one of these 4 cells must have its other 3 corners white.

Let me think about an upper bound more carefully.

Consider the "private cell" assignment. Assign each red point to one private cell. This gives an injection from R to cells. Now consider a cell that is a private cell for red point p: it has exactly 1 red (p) and 3 white. 

Now, here's a key constraint: consider the white points. Each white point is in 4 cells. 

Let me think about counting. Let r = |R|, w = |W| = 10000 - r.

Each red point has ≥1 private cell with 3 white corners. So there are ≥ r cells with exactly 1 red and 3 white. The remaining 10000 - r cells have ≥1 red (could be 1,2,3,4 red).

Hmm, let me think about a clever construction for large r and matching upper bound.

Let me think about the problem as: we want a minimal transversal of the 4-uniform hypergraph of 2×2 cells on the torus.

For minimal transversals, there's a general theory. The maximum minimal transversal... Let me think about specific constructions.

Construction idea 1: Checkerboard. Color (i,j) red if i+j even. Then every 2×2 cell has exactly 2 red. Is it critical? Yes, every cell has 2 red ≥1. Is it minimal? No — removing one red point, the cell still has another red. So not minimal. We need each red to have a private cell.

Construction idea 2: Make most points red but ensure each red has a private cell. To have a private cell for red point p, we need a cell where p is the only red, i.e., 3 specific neighbors white. 

If we want to maximize red, we want few white points but arranged so that every red point has a nearby cell with 3 white corners including... wait the cell containing p with 3 white.

Let me think: a private cell for p is a cell C with C∩R = {p}. So C has p red, 3 white. The 3 white points of C are "witnesses" for p.

Each white point can serve as a witness for multiple red points (it's in 4 cells, each cell could be private for a different red point). 

Let me think about how many red points a single white point can witness. A white point w is a corner of 4 cells. In each such cell, w is white; if the other 3 corners have exactly 1 red, that cell is private for that red point, and w witnesses it. So one white point can witness up to 4 red points (one per adjacent cell), but actually it could witness the same... let me think. Each of the 4 cells containing w: if that cell has exactly 1 red point (among the other 3 corners + ... wait the cell has 4 corners including w which is white, so the cell has 1 red among the other 3 corners). That red point is witnessed by w. So w witnesses up to 4 red points (at most one per cell, and 4 cells).

But a red point needs 3 white witnesses (the 3 other corners of its private cell). 

Hmm, let me set up a counting / double counting.

Each red point has a private cell with 3 white corners. Count pairs (red point, white corner in its private cell): each red contributes 3, total 3r. Each white point is in at most 4 cells that could be private cells for some red, so contributes at most 4. Wait, but a white point in a private cell: the private cell has exactly 1 red. The white point w is in 4 cells; for each cell, if it's a private cell (1 red), w is one of its 3 white corners and witnesses that 1 red. So each white point witnesses at most 4 red points (one per cell). So 3r ≤ 4w, i.e., 3r ≤ 4(10000 - r), 7r ≤ 40000, r ≤ 5714.28..., r ≤ 5714.

Wait let me double check: each red point needs 3 white witnesses (the 3 white corners of its chosen private cell). Total witness incidences = 3r. Each white point can be a witness for at most 4 red points (since it's in 4 cells, each cell private for at most 1 red). So 3r ≤ 4w. With w = 10000 - r: 3r ≤ 40000 - 4r, 7r ≤ 40000, r ≤ 5714.28, so r ≤ 5714.

Hmm wait, but is this tight? Let me reconsider. Actually a white point w is in 4 cells. For each cell C containing w, C is private for at most one red point (the unique red in C if |C∩R|=1). And w witnesses that red. So w witnesses ≤ 4 reds. But also, could the same red be witnessed by w via two different cells? Possibly, but we're counting incidences and upper bounding by 4 per white. Actually we want: sum over white points of (number of red points witnessed) ≥ 3r (since each red needs 3 distinct white witnesses, all distinct white points within one cell). 

Hmm, actually each red point p has a private cell C_p with 3 white corners, all distinct. So p is witnessed by 3 distinct white points. Total incidences (p, w) where w is a white corner of C_p = 3r, and these are... could the same (p,w) pair appear? No, p fixed, w ranges over 3 distinct whites. Different p's. So total distinct incidences = 3r. Now each white w: how many red points is w a witness for? w is a corner of 4 cells; for each cell that is private (1 red), w witnesses that red. So ≤ 4. Hence 3r ≤ 4w. Good.

So r ≤ 5714. But is this achievable? Need 7 | 40000? 40000/7 = 5714.28, not integer. So r ≤ 5714. For r=5714, w=4286, 3r=17142, 4w=17144, so slack 2. Possible in principle.

But achieving the bound requires near-perfect arrangement: almost every white point witnesses exactly 4 red points, and almost every red has exactly 3 witnesses (its private cell). Let me think about whether a construction achieving ~5714 exists.

Hmm, this is getting complex. Let me reconsider — maybe the answer is cleaner. Let me reconsider the problem; it's a competition problem likely with a clean answer.

Let me reconsider. Maybe the bound 3r ≤ 4w isn't the right one or maybe there's a better construction giving a cleaner number.

Actually, let me reconsider the witness counting more carefully — maybe I can get a cleaner bound by considering the structure better, or maybe the answer is 5714 or maybe something else.

Let me reconsider. Actually, let me reconsider whether each white can witness 4. For w to witness a red via cell C, C must have exactly 1 red. If w is surrounded such that all 4 cells through w are private cells (each with exactly 1 red), then w witnesses 4 reds. That requires the 8 neighbors of w (in the grid, the cells around w) arranged so each of the 4 cells has exactly 1 red among its 3 non-w corners.

Let me think about a local pattern. Consider white point w at origin (0,0). The 4 cells: C(0,0)={ (0,0),(1,0),(0,1),(1,1)}, C(-1,0)={(-1,0),(0,0),(-1,1),(0,1)}, C(0,-1)={(0,-1),(1,-1),(0,0),(1,0)}, C(-1,-1)={(-1,-1),(0,-1),(-1,0),(0,0)}.

For each to have exactly 1 red among the 3 non-w corners:
- C(0,0): exactly 1 red among (1,0),(0,1),(1,1).
- C(-1,0): exactly 1 red among (-1,0),(-1,1),(0,1).
- C(0,-1): exactly 1 red among (0,-1),(1,-1),(1,0).
- C(-1,-1): exactly 1 red among (-1,-1),(0,-1),(-1,0).

This is a constraint satisfaction. Let me see if there's a periodic pattern.

This is getting complicated. Let me step back and think about the problem more cleverly, maybe there's a cleaner characterization.

Alternative approach: Think of it as a 2D problem. Let me consider rows. 

Actually, let me reconsider the problem from the perspective of "minimal critical" = minimal hitting set of 2×2 cells. The maximum minimal hitting set.

Let me think about 1D version first: points 0..n-1 on a cycle, "edges" are consecutive pairs {(i,i+1)}, critical = every edge has a red point = no two consecutive whites. Minimal critical = minimal vertex cover of cycle = every red has a white neighbor (so that removing it creates two consecutive whites). Max minimal vertex cover of cycle C_n: we want max set with no two consecutive whites (i.e., whites form independent set) and every red adjacent to a white. Whites independent set max size = floor(n/2). Reds = n - floor(n/2) = ceil(n/2). And minimality: every red adjacent to white. With whites being a max independent set (alternating), every red is between two whites, so removing a red creates... red r between two whites w1,w2: removing r, are w1,w2 consecutive? They're at distance 2, not consecutive. Hmm so removing r doesn't create consecutive whites necessarily. Wait the edge {(r-1,r)} and {(r,r+1)}: if r-1 and r+1 are white, removing r: edge {(r-1,r)} now has r-1 white and r white→ all white? No, edge {(r-1,r)} = {r-1, r}, r-1 white, r now white → both white → edge not covered. So yes removing r breaks it. Good, so minimality holds. So in 1D, max minimal vertex cover = ceil(n/2)... but wait we want to maximize red, so we want minimal vertex cover of maximum size. Max size minimal vertex cover of cycle.

Hmm, for cycle, minimal vertex covers: the complement is a maximal independent set. Max minimal vertex cover = n - min maximal independent set. Min maximal independent set of cycle C_n: for n≥... the minimum maximal independent set (independent dominating set) has size ceil(n/3). So max minimal vertex cover = n - ceil(n/3) = floor(2n/3).

Wait I need to recompute. Minimal vertex cover ⟺ complement is maximal independent set. To maximize vertex cover, minimize the maximal independent set (the complement). The minimum size of a maximal independent set = independent domination number = ceil(n/3) for cycle C_n. So max minimal vertex cover = n - ceil(n/3) = floor(2n/3).

For n=100: floor(200/3)=66. So in 1D analog the answer would be 66 out of 100.

OK so for 2D, the analog: minimal transversal of 2×2-cell hypergraph, max size = total - min maximal "independent set" where independent set = set W with no cell fully in W (i.e., W contains no full 2×2 block), and maximal means every red point (every point not in W) has a cell fully... no. Maximal independent set in hypergraph sense: W is independent (no edge ⊆ W) and maximal (can't add any point while staying independent). Adding point p (currently red) to W: W∪{p} independent means no cell ⊆ W∪{p}, i.e., no cell containing p has all other 3 corners in W. So maximality = for every red point p, there's a cell containing p with the other 3 corners in W. That's exactly the private cell condition! Great, consistent.

So max minimal transversal = n_total - min maximal independent set, where independent = no 2×2 all-white block, maximal = every point outside has a cell with other 3 corners inside.

Min maximal independent set = minimum number of white points such that (a) no 2×2 block is all white, and (b) every red point has a cell where the other 3 are white.

We want to minimize white points w. Then r = 10000 - w.

So now: minimize w subject to:
(a) No 2×2 block is entirely white.
(b) Every non-white (red) point p has a cell containing p whose other 3 corners are white.

Condition (b) is strong: every red point must be "adjacent" to a cell of 3 whites. 

Let me re-examine the counting bound 3r ≤ 4w → with r = 10000 - w: 3(10000-w) ≤ 4w → 30000 ≤ 7w → w ≥ 30000/7 = 4285.7 → w ≥ 4286, r ≤ 5714.

So we want to find min w ≥ 4286 (if achievable) such that conditions hold. Then r = 5714.

But is w=4286 achievable? Need 7w ≥ 30000, w=4286 gives 7·4286=30002 ≥ 30000. And 3r=3·5714=17142, 4w=17144, slack 2. So almost tight.

Hmm, but the answer 5714 seems ugly for a competition. Let me reconsider — maybe the counting bound isn't tight and the real answer is different, or maybe the problem expects 5714. Actually competition problems can have answers like 5714. But let me double-check the bound and think about constructions.

Wait, I should double check the witness counting. Let me redo: We need every red point to have a private cell (3 white corners). Choose one private cell per red point. Now count incidences (red point p, white corner w of C_p). Each red gives 3 incidences (3 white corners), total 3r. But the same (p, w) — for fixed p, the 3 whites are distinct. Across different p, could two reds share the same private cell? No, a private cell has exactly 1 red. So all C_p distinct, hence the white corners... a white point w could be a corner of multiple private cells (up to 4 cells contain w). So w appears in up to 4 incidences. So 3r ≤ 4w. Confirmed.

Now, is this achievable? Let me think about a construction. We want a configuration where each white point is a corner of exactly 4 private cells (witnesses 4 reds) — well, almost, since slack is 2, two white points witness only 3, or one witnesses 2, etc. And each red has exactly one private cell (with 3 whites) — but red could have more cells covered, that's fine; we just need ≥1 private.

Actually wait, we also need condition (a): no 2×2 all white. And the private cells have exactly 1 red so they're fine. But other cells (non-private) must also have ≥1 red. With w=4286 white points spread out, need no 2×2 all white. If whites are sparse (4286/10000 ≈ 0.43 density), 2×2 all white is possible if not careful. So arrangement matters.

This is getting really involved. Let me think about whether there's a cleaner formulation or known result.

Hmm, let me reconsider. Let me think about the structure of an optimal solution via "each white witnesses 4 reds" locally.

If every white point w witnesses exactly 4 reds (one per adjacent cell, each adjacent cell private), then each of the 4 cells through w has exactly 1 red (among the 3 non-w corners). Let me figure out the local pattern around an "ideal" white point.

Let me set up coordinates. White at (0,0). Neighbors involved: the 8 points at Chebyshev distance 1: (±1,0),(0,±1),(±1,±1). The 4 cells and their non-w corners:
- NE cell {(0,0),(1,0),(0,1),(1,1)}: corners (1,0),(0,1),(1,1), exactly 1 red.
- NW cell {(-1,0),(0,0),(-1,1),(0,1)}: (-1,0),(-1,1),(0,1), exactly 1 red.
- SE cell {(0,-1),(1,-1),(0,0),(1,0)}: (0,-1),(1,-1),(1,0), exactly 1 red.
- SW cell {(-1,-1),(0,-1),(-1,0),(0,0)}: (-1,-1),(0,-1),(-1,0), exactly 1 red.

Let me denote the 8 neighbors' colors. Let a=(1,0), b=(0,1), c=(1,1) [NE]; d=(-1,0), e=(-1,1), b=(0,1) [NW, shares b]; f=(0,-1), g=(1,-1), a=(1,0) [SE shares a]; h=(-1,-1), f=(0,-1), d=(-1,0) [SW shares d,f].

So the 8 distinct neighbors: a=(1,0), b=(0,1), c=(1,1), d=(-1,0), e=(-1,1), f=(0,-1), g=(1,-1), h=(-1,-1).

Constraints (exactly 1 red in each group):
- NE: {a,b,c}: exactly 1 red.
- NW: {d,e,b}: exactly 1 red.
- SE: {f,g,a}: exactly 1 red.
- SW: {h,f,d}: exactly 1 red.

From NE and NW: both contain b. From NE and SE: both contain a. From NW and SW: both contain d. From SE and SW: both contain f.

Let me solve. Let r(x)=1 if red. 
NE: r(a)+r(b)+r(c)=1.
NW: r(d)+r(e)+r(b)=1.
SE: r(f)+r(g)+r(a)=1.
SW: r(h)+r(f)+r(d)=1.

Case 1: r(b)=1. Then NE: r(a)=r(c)=0. NW: r(d)+r(e)=0 → r(d)=r(e)=0. SE: r(f)+r(g)+0=1 → one of f,g red. SW: r(h)+r(f)+0=1 → r(h)+r(f)=1.
- Subcase f red: then g=0 (SE: f=1 so g=0), and SW: r(h)+1=1→r(h)=0. So f red, others (a,c,d,e,g,h) white, b red. Reds near w: b and f. That's 2 reds among 8 neighbors, plus w white. So 2 reds witnessed... but we wanted w to witness 4 reds (one per cell). Here NE red=b, NW red=b (same!), SE red=f, SW red=f (same). So w witnesses only 2 distinct reds (b and f), via 4 cells but 2 cells each share. So w witnesses 2 reds, not 4. Hmm, so the "4 cells private" doesn't mean 4 distinct reds.

Oh I see, my counting bound assumed each white witnesses ≤4 reds, but actually it could witness fewer distinct reds. The bound 3r ≤ 4w used "each white in ≤4 incidences" where incidences = (red, white) pairs with white in red's private cell. If two cells of w are private for the same red b, that's still 2 incidences? No — incidence is (p, w) where w is a corner of C_p. If C_b (private cell of b) — but b has only one chosen private cell. So even if multiple cells through w are "private for b", b only picks one private cell. So the incidence (b, w) is counted once. So the number of incidences for w = number of distinct reds p such that w ∈ C_p (w is a corner of p's chosen private cell). 

So my bound 3r ≤ 4w requires each white to be a corner of ≤4 chosen private cells, and chosen private cells are distinct (one per red). A white w is a corner of 4 cells total, and each cell is the chosen private cell of at most one red. So w is in ≤4 chosen private cells → ≤4 incidences. So bound holds. But to achieve equality, w must be a corner of 4 distinct chosen private cells, i.e., 4 distinct reds each having a private cell through w. From the case analysis, case 1 gave only 2 distinct reds near w with all 4 cells private. So equality not achievable in that case. Let me find a case with 4 distinct reds.

Case 2: r(b)=0. Then NE: r(a)+r(c)=1. NW: r(d)+r(e)=1. 
Subcase 2a: r(a)=1, r(c)=0. SE: r(f)+r(g)+1=1→r(f)=r(g)=0. NW: r(d)+r(e)=1. SW: r(h)+r(f)+r(d)=r(h)+0+r(d)=1.
- 2a-i: r(d)=1,r(e)=0. SW: r(h)+1=1→r(h)=0. Reds: a,d. NE red=a, NW red=d, SE red=a (same as NE), SW red=d (same). Only 2 distinct. 
- 2a-ii: r(d)=0,r(e)=1. SW: r(h)+0=1→r(h)=1. Reds: a,e,h. NE=a, NW=e, SE=a, SW=h. Distinct reds witnessed: a,e,h = 3. 
Subcase 2b: r(a)=0,r(c)=1. SE: r(f)+r(g)+0=1. NW: r(d)+r(e)=1. SW: r(h)+r(f)+r(d)=1.
- 2b-i: r(d)=1,r(e)=0. SE: r(f)+r(g)=1. SW: r(h)+r(f)+1=1→r(h)+r(f)=0→r(h)=0,r(f)=0. Then SE: r(g)=1. Reds: c,d,g. NE=c,NW=d,SE=g,SW=d. Distinct: c,d,g=3.
- 2b-ii: r(d)=0,r(e)=1. SE: r(f)+r(g)=1. SW: r(h)+r(f)+0=1→r(h)+r(f)=1.
  - r(f)=1,r(g)=0: SW r(h)+1=1→r(h)=0. Reds: c,e,f. NE=c,NW=e,SE=f,SW=f. Distinct: c,e,f=3.
  - r(f)=0,r(g)=1: SW r(h)=1. Reds: c,e,g,h. NE=c,NW=e,SE=g,SW=h. Distinct: 4! 

So case 2b-ii with r(f)=0,r(g)=1: reds at c=(1,1), e=(-1,1), g=(1,-1), h=(-1,-1). I.e., the 4 diagonal neighbors of w are red, the 4 axis neighbors (a,b,d,f) are white. And w white. So around w: w and its 4 axis-neighbors white, 4 diagonal neighbors red. Then all 4 cells through w are private (each has exactly 1 red = the diagonal corner). And w witnesses 4 distinct reds. 

So the ideal local pattern: white points form a "plus" shape, and the 4 diagonals are red. This is like: white at center and 4 axis neighbors, red at 4 diagonals.

This suggests a pattern where whites are arranged so that each white has its 4 axis-neighbors also white and 4 diagonal neighbors red. But that's a strong condition. Let me think globally.

If white points are such that whenever (i,j) is white, (i±1,j) and (i,j±1) are white too — that means white set is closed under axis-adjacency, i.e., white set is a union of "axis-connected" components, and within, all axis-neighbors white. But then white points would form full rows/columns blocks, likely creating 2×2 all-white blocks (violating condition a). Hmm, conflict.

Wait, the local pattern requires for white w: its 4 axis neighbors white. But if w=(0,0) white requires (1,0) white, and (1,0) white requires (2,0) white, etc. → entire row white. Then 2×2 blocks in that row all white → violates (a). Contradiction. So we can't have all whites be "ideal" (witnessing 4). 

So the bound 3r ≤ 4w is not achievable. We need a better analysis. The slack means actual min w is larger, so r smaller.

Hmm. So the ideal pattern is impossible globally. Let me reconsider.

OK this is a hard combinatorial optimization. Let me think differently.

Let me reconsider the problem. Maybe think in terms of rows and a transfer / pattern.

Let me reconsider condition (b): every red point p has a cell with the other 3 corners white. So every red point is "exposed" — there's a 2×2 block where it's the lone red.

And condition (a): no 2×2 block all white.

We want to minimize whites w (maximize reds r=10000-w).

Let me think about it as: place white points to "cover" all red points (each red needs a cell of 3 whites around it) while not forming any all-white 2×2.

Equivalently think of red points: each red must have a "witness cell" (3 whites). 

Let me think about a periodic tiling construction and compute its density, then try to match an upper bound.

Idea: Use a pattern with period dividing 100. Since 100 = 4·25, periods like 4, 5, 10, 20, 25, 50 work.

Let me think about a stripe/column pattern. Suppose we make certain columns white. If column j is all white, then 2×2 blocks within column j and j+1... a 2×2 block uses columns j,j+1. If both columns j,j+1 all white → all-white block. So can't have two consecutive all-white columns. So white columns must be non-consecutive. But also a single all-white column: 2×2 block at columns j,j+1 where j white column, j+1 not: block has 2 points in col j (white) and 2 in col j+1. If col j+1 has some red, fine. So all-white columns isolated is OK for condition (a) as long as no two consecutive white columns... but actually even one all-white column: the 2×2 blocks spanning (col j, col j+1) and (col j-1, col j) — these have 2 white (from col j) and 2 from neighbor column. Not all white if neighbor has red in those rows. If neighbor column is all red, then those blocks have 2 white + 2 red, fine.

But condition (b): red points in neighbor columns need witness cells with 3 whites. If col j is all white and col j+1 all red: a red point (j+1, y) needs a cell with 3 white corners. Cells containing (j+1,y): columns (j,j+1) or (j+1,j+2). Using cell (j,j+1) at rows (y-1,y) or (y,y+1): corners (j,y-1),(j+1,y-1),(j,y),(j+1,y) — wait let me index cell C(i,j) = {(i,j),(i+1,j),(i,j+1),(i+1,j+1)} where i is column, j is row. Let me use (col, row) = (x,y). Cell C(x,y) = {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}.

Red point (j+1, y). Cells containing it: C(j,y) [as (x+1,y) part? C(j,y)={(j,y),(j+1,y),(j,y+1),(j+1,y+1)} contains (j+1,y)], C(j,y-1)={(j,y-1),(j+1,y-1),(j,y),(j+1,y)} contains (j+1,y), C(j+1,y)={(j+1,y),(j+2,y),(j+1,y+1),(j+2,y+1)}, C(j+1,y-1)={(j+1,y-1),(j+2,y-1),(j+1,y),(j+2,y)}.

For witness with 3 whites: use C(j,y) = {(j,y),(j+1,y),(j,y+1),(j+1,y+1)}: (j+1,y) red, need (j,y),(j,y+1),(j+1,y+1) white. (j,y),(j,y+1) are in col j (all white) ✓. (j+1,y+1) is in col j+1 (all red) ✗. So not all white. Try C(j,y-1)={(j,y-1),(j+1,y-1),(j,y),(j+1,y)}: (j+1,y) red, others (j,y-1),(j+1,y-1),(j,y). (j,y-1),(j,y) white ✓, (j+1,y-1) red ✗. So can't get 3 whites from col-j cells because the 4th corner is in col j+1 (red). 

So a single all-white column adjacent to all-red column doesn't give witnesses. We need whites in col j+1 too near each red. So pure column stripes won't work for condition (b).

This is quite intricate. Let me think about small periodic patterns computationally in my head... hard. 

Let me reconsider — maybe approach via known result. This problem: "critical coloring" of grid, maximal minimal. This resembles an IMO/olympiad problem. The answer might be 7500 or 5000 or some clean fraction.

Let me reconsider the counting bound differently to get a cleaner number. 

Alternative bound: Consider rows. For each red point, it needs a witness cell. Let me think about per-row contributions.

Hmm, let me think about the witness cell of red point p=(x,y). The witness cell is one of 4 cells around p, with the other 3 corners white. The 3 white corners are in specific positions. Let me categorize by which cell:
- Cell C(x,y) [p is bottom-left of cell]: whites at (x+1,y),(x,y+1),(x+1,y+1). [p=(x,y) red]
- Cell C(x-1,y) [p is bottom-right]: whites at (x-1,y),(x-1,y+1),(x,y+1).
- Cell C(x,y-1) [p is top-left]: whites at (x+1,y-1),(x,y),(x+1,y)... wait C(x,y-1)={(x,y-1),(x+1,y-1),(x,y),(x+1,y)}, p=(x,y) is in it, others (x,y-1),(x+1,y-1),(x+1,y).
- Cell C(x-1,y-1) [p is top-right]: {(x-1,y-1),(x,y-1),(x-1,y),(x,y)}, p=(x,y), others (x-1,y-1),(x,y-1),(x-1,y).

So each red point's witness cell has 3 white corners forming an "L" shape adjacent to p.

Now let me think about a cleaner global bound. 

Consider the white points and the "L-shapes" they form. Each witness cell is a 2×2 with 1 red + 3 white (an L of whites + 1 red). 

Let me count the number of "L-triominoes of white" — actually each witness cell is a 2×2 block with exactly 3 whites and 1 red. Let me call such a block a "W3-block" (3 whites). Condition (b): every red is in some W3-block (as the lone red). Condition (a): no W4-block (4 whites) and actually no block with 4 whites; blocks can have 1,2,3 whites (≥1 red) — wait ≥1 red means ≤3 whites. So every block has 1,2, or 3 whites (0 whites = all red, allowed since ≥1 red ✓; 4 whites forbidden). And every red is the lone red of some block (a block with exactly 3 whites = 1 red, and that red is p).

So: every block has ≤3 whites (i.e., ≥1 red). Every red point is the unique red of at least one block.

We want to minimize total whites.

Let me think about it as: whites form a set with no 2×2 full block, and every red has a "private" block (block where it's the only red, i.e., the other 3 are white).

Minimize whites. Equivalently maximize reds such that every red has a private block and no block is all-red-... no, blocks can be all red (0 whites) — that's fine, ≥1 red. Wait but if a block is all red (4 reds), that's allowed. But then those reds need private blocks elsewhere.

Hmm OK. Let me think about lower bound on whites via a different counting.

Each red needs a private block (3 whites). Consider the private blocks chosen, one per red. These are 10000-w blocks (one per red), each a 2×2 with 3 whites + 1 red. Distinct blocks? A private block has exactly 1 red, so it's the private block of that unique red. So private blocks are automatically distinct (different reds → different blocks, since a block with 1 red is private for that red only; two reds can't share a private block). Wait, could two reds choose the same block as private? A block with exactly 1 red can only be private for that 1 red. So if red p1 and p2 both have private block B, then B has exactly 1 red, contradiction (it'd need to be both p1 and p2). So private blocks distinct. Good, r distinct private blocks, each with 3 whites.

Now count incidences (white point, private block containing it). Each private block has 3 whites → 3r incidences. Each white point is in 4 blocks total (the 4 cells containing it), so in ≤4 private blocks → ≤4 incidences. So 3r ≤ 4w. Same bound. r ≤ 4w/3, w ≥ 3r/4... with r+w=10000: 3r ≤ 4(10000-r) → 7r ≤ 40000 → r ≤ 5714.28 → r ≤ 5714.

We showed equality needs each white in 4 private blocks, requiring the local "plus" pattern which forces all-white rows → contradiction with no-W4. So strict inequality. So r ≤ 5713? Not necessarily; the bound r ≤ 5714 still holds, equality r=5714 needs near-tight. Let me see how much slack is forced.

Actually the bound r ≤ 5714 is from 7r ≤ 40000, r ≤ 5714.28. So r ≤ 5714 regardless. The question is whether 5714 is achievable or we need r ≤ 5713 or less. The local obstruction shows we can't have all whites saturated (4 incidences), but we might have most saturated and a few unsaturated, still achieving r=5714 if total incidences 3·5714=17142 ≤ 4w - (deficit). With w=4286, 4w=17144, deficit allowed ≤ 2. So only 2 incidences of deficit allowed — meaning almost all whites saturated (4 incidences) except total deficit 2. But saturated whites require the plus pattern locally (axis neighbors white), which cascades into all-white rows. So having ~4286 whites nearly all saturated is impossible. So r=5714 not achievable. The real max is lower.

I need a better bound capturing the cascade. Let me think.

Let me define a white point as "saturated" if it's in 4 private blocks (witnesses 4 reds). Saturated white requires its 4 axis-neighbors white (from case analysis: the only way to witness 4 distinct reds is the plus pattern with axis neighbors white and diagonal neighbors red). Wait, let me double-check that the only way to witness 4 is that pattern. From case analysis, 4 distinct reds witnessed required reds at the 4 diagonals and whites at 4 axis positions. But "witnessing 4 reds" means 4 private blocks through w, each with a distinct lone red. The lone reds are at the 4 diagonal positions, and the axis positions must be white (so that each cell through w has its 3 non-w corners = 2 axis + 1 diagonal, with the diagonal red and 2 axis white → exactly 1 red ✓). For this, axis neighbors of w must be white. So yes, saturated white ⟹ 4 axis neighbors white.

But the 4 axis neighbors being white doesn't require them saturated. However, if w is saturated, its axis neighbors are white. Now consider those axis neighbors — are they saturated? Not necessarily. But the issue: if (1,0) is white (axis neighbor of w=(0,0)), and (1,0) is also axis neighbor of (2,0) etc. The cascade: w saturated ⟹ (1,0) white. (1,0) white — for (1,0) to be saturated, need (2,0),(1,1),(1,-1),(0,0) white. (0,0) is white ✓. So (1,0) saturated needs (2,0) white etc. But (1,0) need not be saturated.

The real contradiction earlier: if ALL whites saturated, then white set closed under axis adjacency → whole rows white → W4 blocks. But we don't need all whites saturated; we need most. Let me quantify: deficit D = 4w - 3r (total missing incidences). For r=5714, w=4286: D = 4·4286 - 3·5714 = 17144 - 17142 = 2. So D=2, meaning only 2 missing incidences total. So all but at most 2 whites are saturated (each saturated white has 4 incidences; unsaturated have fewer; total deficit 2 means e.g. one white with 2 incidences, or two whites with 3). So ≥4284 whites saturated (roughly). 4284 saturated whites, each forcing 4 axis neighbors white. 

Now, saturated whites forcing axis neighbors white: consider the graph on white points where edges are axis-adjacency. Saturated white w has all 4 axis neighbors white, so w has degree 4 in this white-axis-graph (within the white set, considering the 4 axis neighbors all present). Actually it means w is "interior" of white set in axis directions.

If 4284 whites are saturated (interior, all 4 axis neighbors white), then the white set has 4284 interior points. The white set total 4286. So only 2 white points are "boundary" (not saturated, missing an axis neighbor that's red). 

A set of 4286 points on 100×100 torus with 4284 having all 4 axis-neighbors in the set: that means the white set is almost a union of full rows and columns... Let me think. If a white point has all axis neighbors white, then its entire row and column (through propagation) ... no, propagation: w=(0,0) saturated → (1,0) white. Is (1,0) saturated? If yes → (2,0) white, etc. But (1,0) might be one of the 2 unsaturated. With only 2 unsaturated, the propagation can only be "blocked" at 2 points. So along the row through w, the whites extend until hitting an unsaturated point. With 4284 saturated forming large connected axis-components, and only 2 unsaturated to bound them.

A saturated white's axis neighbors are white; those neighbors, if saturated, continue. So a maximal axis-connected run of saturated whites: starts and ends at unsaturated whites (or wraps around torus). With only 2 unsaturated whites total, there are at most 2 "endpoints", so essentially one long run that wraps the torus, or the white set is almost entire rows/columns.

If white set contains a full row (all 100 points in a row white) — then 2×2 blocks within that row and adjacent row: block at (x,y),(x+1,y),(x,y+1),(x+1,y+1) with row y all white: (x,y),(x+1,y) white; need (x,y+1),(x+1,y+1) not both white. If row y+1 also has whites... but more directly, a full white row y: consider block with rows y and y+1: 2 points in row y (white) + 2 in row y+1. For no W4, row y+1 must have at least one red in every consecutive pair... i.e., row y+1 can't have two consecutive whites. Similarly row y-1. 

But more importantly, if white set is ~4286 points mostly in full rows: say k full white rows = 100k whites. 100k ≈ 4286 → k≈42.86, not integer. So maybe 42 full rows (4200 whites) + 86 more. But full white rows: consecutive full white rows create W4 (block entirely in two consecutive white rows). So full white rows must be non-consecutive (separated by ≥1 non-full row). With 42 full white rows among 100 rows, non-consecutive: possible (alternating). 42 white rows + 58 non-white rows, but 42 white rows non-consecutive needs ≥41 gaps, 42+41=83≤100 ok, or with wrap. Actually 42 non-consecutive in cycle of 100: need 42 ≤ 50, ok.

But wait, if row y is full white, then rows y-1 and y+1 must have no two consecutive whites (to avoid W4 with row y). And red points in rows y-1, y+1 need witness blocks. A red point (x, y+1) needs a block with 3 whites. Blocks containing (x,y+1): using rows y,y+1: block {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}: (x,y),(x+1,y) white (row y full), (x,y+1) red, (x+1,y+1) = ? For 3 whites need (x+1,y+1) white. So (x+1,y+1) white. So red (x,y+1) needs (x+1,y+1) white (or use other blocks). Similarly using block {(x-1,y),(x,y),(x-1,y+1),(x,y+1)}: (x-1,y),(x,y) white, (x,y+1) red, need (x-1,y+1) white. So red (x,y+1) needs an adjacent white in row y+1 (left or right) — but row y+1 can't have two consecutive whites (to avoid W4 with row y)! Contradiction: red (x,y+1) needs (x±1,y+1) white, meaning two consecutive whites in row y+1 ((x,y+1) is red, but (x+1,y+1) white and ... wait (x,y+1) red, (x+1,y+1) white — that's not two consecutive whites, that's red then white). Hmm let me redo. Row y+1: (x,y+1) is red. For its witness via block with row y, need (x+1,y+1) white OR (x-1,y+1) white. So at least one neighbor of (x,y+1) in row y+1 is white. That's fine, doesn't create two consecutive whites by itself. But consider the red points in row y+1: each red needs a white neighbor in row y+1 (or witness via row y+2 blocks). 

Hmm, this is getting complicated but maybe full-row approach can work. But 4286 isn't divisible nicely and the deficit analysis says r=5714 needs D=2, extremely tight, basically requiring near-perfect saturation which seems impossible given the row constraints. Let me just try to find the true optimum via a cleaner argument or construction.

Let me reconsider. Maybe the answer is a clean number and my bound is loose. Let me look for a better upper bound.

New idea for upper bound: Consider the witness blocks (private blocks), r of them, each a 2×2 with 3W+1R. Look at the red point in each witness block and the "missing corner" position. Actually, let me think about pairs of adjacent witness blocks or overlaps.

Alternative: think about each 2×2 block's white count. Let a_k = number of blocks with exactly k whites (k=0,1,2,3; k=4 forbidden). Sum k·a_k = total (block, white) incidences = 4w (each white in 4 blocks). Sum a_k = 10000 (total blocks). Witness blocks are those with k=3 (3 whites, 1 red): a_3 ≥ r (each red needs at least one k=3 block, and each k=3 block is witness for its unique red, so a_3 = number of reds that have ≥1... no, a_3 = number of blocks with 3 whites; each such block has 1 red and is a witness for that red; a red could have multiple witness blocks, so a_3 ≥ r? No: a_3 = number of 3-white blocks. Each red needs ≥1 such block containing it. A 3-white block contains exactly 1 red. So the map from 3-white blocks to reds (the unique red) is surjective onto the set of reds (every red has ≥1). So a_3 ≥ r. 

So a_3 ≥ r. And 4w = a_1 + 2a_2 + 3a_3. And a_0+a_1+a_2+a_3 = 10000. We want to maximize r = 10000 - w, minimize w. 

We have a_3 ≥ r = 10000 - w. And 4w = a_1 + 2a_2 + 3a_3 ≥ 3a_3 ≥ 3(10000-w) → 4w ≥ 30000 - 3w → 7w ≥ 30000 → w ≥ 4285.7 → w ≥ 4286, r ≤ 5714. Same bound. The bound 4w ≥ 3a_3 uses a_1+2a_2 ≥ 0. To tighten, need a_1 + 2a_2 > 0 forced, i.e., need to show there must be blocks with 1 or 2 whites (not all blocks 0 or 3 whites). 

If a_1 = a_2 = 0: all blocks are 0-white (all red) or 3-white. Then 4w = 3a_3, and a_0 + a_3 = 10000. Also a_3 ≥ r=10000-w. From 4w=3a_3: a_3 = 4w/3. And a_3 ≥ 10000 - w: 4w/3 ≥ 10000 - w → 7w/3 ≥ 10000 → w ≥ 4285.7. And a_3 = 4w/3 must be integer, w divisible by 3. w=4286: 4·4286/3 = 5714.67 not integer. w=4287: a_3=5716, a_0=10000-5716=4284, r=10000-4287=5713. Check a_3 ≥ r: 5716 ≥ 5713 ✓. So with a_1=a_2=0, w=4287, r=5713. Hmm so this sub-case allows r=5713. But is a_1=a_2=0 achievable (all blocks either all-red or 3-white)? That's a strong structural condition. Let me check if possible.

All blocks 0 or 3 whites. A block with 3 whites + 1 red. Adjacent blocks share edges. Let me see if such a configuration exists on torus. 

Consider two horizontally adjacent blocks C(x,y) and C(x+1,y). C(x,y) = {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}, C(x+1,y) = {(x+1,y),(x+2,y),(x+1,y+1),(x+2,y+1)}. They share edge {(x+1,y),(x+1,y+1)}. If C(x,y) is 3W1R and C(x+1,y) is 3W1R: the shared edge has 2 points; in C(x,y) the red is one of 4 corners; in C(x+1,y) red is one of its 4 corners. The shared points (x+1,y),(x+1,y+1): their colors fixed. 

This is a tiling constraint. Let me try to construct: maybe a pattern where each block has exactly 3 whites and 1 red, and reds form a pattern. But a_0 > 0 also (4284 all-red blocks). Mixed.

Hmm, let me just try to see if r=5713 or 5714 achievable, or find the real answer. This is getting deep. Let me try a concrete periodic construction and compute.

Let me try period-7 or period related to 7 since 7 appears. 100 = 7·14 + 2. Not divisible by 7. Hmm. The bound involves 7. 10000 mod 7 = 10000 - 7·1428 = 10000-9996=4. So 10000 ≡ 4 mod 7. r ≤ floor(40000/7) = 5714 (since 40000 = 7·5714 + 2). 

For a clean construction maybe period 5 or 10. Let me try to find a pattern with a certain white density and verify conditions, then match bound.

Let me think about a "staircase" white pattern. 

Actually, let me reconsider the problem. Let me reconsider whether the answer might be 5000 or 7500 etc. Let me get a better upper bound using a different method: line/row arguments.

Row argument: Consider a fixed row y. Let w_y = whites in row y. Condition (a) no W4: for consecutive rows y, y+1, no two consecutive columns both white in both rows. I.e., the set of columns where both row y and row y+1 are white has no two consecutive. 

Condition (b): every red (x,y) needs a witness block. 

Let me think about witness blocks and rows. A witness block for red (x,y) is a 2×2 block (rows y-1,y or y,y+1) with 3 whites. The 3 whites are in 2 consecutive rows. 

Hmm. Let me think about counting whites per row and the witness requirement per row.

Let me consider the red points in row y. Each needs a witness block, which is either in rows (y-1,y) or rows (y,y+1). A witness block in rows (y,y+1) with red (x,y): block {(x,y),(x+1,y),(x,y+1),(x+1,y+1)} (red at (x,y)) needs (x+1,y),(x,y+1),(x+1,y+1) white; or block {(x-1,y),(x,y),(x-1,y+1),(x,y+1)} (red at (x,y)) needs (x-1,y),(x-1,y+1),(x,y+1) white. So a witness for (x,y) in rows (y,y+1) requires (x,y)'s horizontal neighbor in row y white AND the two corresponding points in row y+1 white. Specifically pattern: row y: ...W R... (white at x-1 or x+1, red at x), row y+1: two consecutive whites at x-1,x or x,x+1.

So roughly, to witness reds in row y using row y+1, we need whites in row y+1 and adjacent whites in row y.

This is complex. Let me just try to guess the answer is 5714 and try to construct, or reconsider.

Actually, let me reconsider the possibility that the intended answer is 7500. Let me get an upper bound of 7500 via a simple argument and a matching construction.

Simple construction giving 7500: Color 3/4 of points red? Let me think. Suppose whites are at positions (i,j) with i≡0 mod 2 and j≡0 mod 2, i.e., a 2×2 sublattice (every other row, every other column). That's 50×50 = 2500 whites, 7500 reds. Check condition (a): no W4 block. A 2×2 block {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}: whites are those with both coords even. Among 4 corners, how many have both even? Depends on parity of x,y. If x,y both even: corners (x,y)✓,(x+1,y)✗,(x,y+1)✗,(x+1,y+1)✗ → 1 white. If x odd, y even: (x,y)✗,(x+1,y)✓,(x,y+1)✗,(x+1,y+1)✗→1. Etc. Always exactly 1 white. So no W4 (only 1 white per block). Condition (a) ✓ (every block has 3 reds ≥1). 

Condition (b): every red point needs a witness block (3 whites). But each block has only 1 white (and 3 reds). So no block has 3 whites! So no red has a witness. Condition (b) fails. So this is critical but NOT minimal (removing a red: the block had 3 reds, now 2, still ≥1; but does removing break criticality? Need some block to become all white. With 1 white per block, removing reds never makes a block all white unless we remove 3 reds from a block. So removing 1 red: all blocks still have ≥1 red (the block containing the removed red had 3→2, others unaffected). So not minimal. Fails.) 

So 7500 with that pattern is critical but not minimal. We need minimality.

To get minimality, we need blocks with 3 whites (witness blocks). So whites must cluster into L-shapes. 

Let me think about a construction with whites forming L-shapes (3 of a 2×2) tiled. 

Construction: tile the plane with 2×2 blocks, each block having 3 whites and 1 red. But adjacent blocks share edges, so can't independently set. Let me try: pattern on 2×2 fundamental domain repeated. 2×2 domain {(0,0),(1,0),(0,1),(1,1)} with 3W1R, say red at (0,0), whites at (1,0),(0,1),(1,1). Repeat with period 2. Then every 2×2 block aligned with the grid... let me check all blocks. Block C(x,y) for various x,y parity:
- x,y even: C(0,0)={(0,0)R,(1,0)W,(0,1)W,(1,1)W}: 3W1R ✓ witness for (0,0).
- x even, y odd: C(0,1)={(0,1)W,(1,1)W,(0,2),(1,2)}. (0,2): 2 even→ (0,0) pattern → R. (1,2): (1,0) pattern → W. So {(0,1)W,(1,1)W,(0,2)R,(1,2)W}: 3W1R, red at (0,2). ✓
- x odd, y even: C(1,0)={(1,0)W,(2,0),(1,1)W,(2,1)}. (2,0)=(0,0)pattern→R, (2,1)=(0,1)pattern→W. So {W,R,W,W}: 3W1R red (2,0). ✓
- x odd,y odd: C(1,1)={(1,1)W,(2,1)W,(1,2)W,(2,2)}. (2,2)=(0,0)→R. So {W,W,W,R}: 3W1R. ✓

So every block has exactly 3 whites and 1 red! So a_3 = 10000, a_0=a_1=a_2=0. Whites = 3/4·10000 = 7500, reds = 2500. Every red has a witness (its block). Condition (a): every block 3W1R, no W4 ✓. Minimality: every red is the unique red of its block, so removing it makes that block all white → criticality lost ✓. So this is minimal critical with r = 2500. But we want MAXIMUM reds, so 2500 is a lower bound (construction), not the answer. We want to maximize reds = minimize whites. 7500 whites here is a lot. We want fewer whites.

So the 3W1R tiling gives r=2500 (min reds, max whites among minimal critical). We want the opposite extreme: max reds (min whites) minimal critical.

So we want as few whites as possible while every red has a witness block (3 whites) and no W4.

The counting bound says w ≥ 4286 (r ≤ 5714). Let me try to construct near that.

We want whites sparse but each red adjacent to a 3-white block. With few whites, whites must be arranged so that each white participates in many witness blocks (up to 4), and reds each have a witness. 

From the local analysis, a white witnesses 4 reds only in the "plus" pattern (axis neighbors white, diagonal red). But that forces axis neighbors white, cascading. So pure 4-witness whites cascade into rows. Let me consider whites witnessing 3 or 2 reds as well, more flexible.

Let me reconsider: maybe the optimum uses whites witnessing 3 reds each (D = 4w - 3r, with each white witnessing 3 → 3r = 3w → r = w, r = 5000). Hmm that gives 5000. Or mix.

Let me reconsider the case analysis for how many distinct reds a white can witness and the required neighbor config:

- 4 reds: axis neighbors white, diagonal red (plus pattern). Forces axis neighbors white.
- 3 reds: cases 2a-ii, 2b-i, 2b-ii(r(f)=1): let me recheck. 2a-ii: r(b)=0,r(a)=1,r(c)=0,r(d)=0,r(e)=1,r(f)=0,r(g)=0,r(h)=1. So reds at a=(1,0), e=(-1,1), h=(-1,-1). Whites at b,c,d,f,g and w. Let me verify all 4 cells private:
  NE {a,b,c}: a red, b,c white → 1 red ✓ (witness a).
  NW {d,e,b}: e red, d,b white → 1 red ✓ (witness e).
  SE {f,g,a}: a red, f,g white → 1 red ✓ (witness a again, same red).
  SW {h,f,d}: h red, f,d white → 1 red ✓ (witness h).
  So distinct reds witnessed: a, e, h = 3. The SE cell witnesses a (already witnessed by NE). So w is in 4 private-eligible cells but only 3 distinct reds. For incidence counting (chosen private blocks), w would be chosen by 3 reds (a,e,h) at most (a chooses one of NE/SE). So w contributes ≤3 incidences. Config: a=(1,0) red [east], e=(-1,1) red [NW diagonal], h=(-1,-1) red [SW diagonal]. Whites: w, b=(0,1) [north], c=(1,1)[NE diag], d=(-1,0)[west], f=(0,-1)[south], g=(1,-1)[SE diag]. So whites: w, north, NE-diag, west, south, SE-diag. Reds: east, NW-diag, SW-diag. 

This doesn't force a full cascade. Let me see what it forces: w white, and north (0,1) white, west (-1,0) white, south (0,-1) white, plus diagonals NE (1,1) white, SE (1,-1) white. Reds: east (1,0), NW(-1,1), SW(-1,-1). So w has 3 axis neighbors white (N,W,S) and 1 axis neighbor red (E). And 2 diagonals white (NE,SE, the ones adjacent to E) and 2 diagonals red (NW,SW). Interesting.

So a white witnessing 3 reds has 3 axis neighbors white and 1 axis neighbor red, with the 2 diagonals adjacent to the red axis neighbor being white, and the 2 diagonals adjacent to... being red. 

This still forces 3 axis neighbors white, partial cascade.

- 2 reds: case 1 (b red, f red) or 2a-i (a,d red). Case 1: r(b)=1, r(a)=r(c)=r(d)=r(e)=0, r(f)=1, r(g)=0, r(h)=0. Reds: b=(0,1)[north], f=(0,-1)[south]. Whites: w, a,c,d,e,g,h. So axis neighbors E,W white (a,d), N,S red (b,f). Diagonals all white (c,e,g,h). w witnesses 2 reds (N and S). Cells: NE{a,b,c}: b red ✓. NW{d,e,b}: b red ✓. SE{f,g,a}: f red ✓. SW{h,f,d}: f red ✓. So 4 cells private but 2 distinct reds. Config: N,S red; E,W, all diagonals white. Forces E,W axis neighbors white and all 4 diagonals white. That's a lot of whites around w (6 whites: E,W,4 diag + w itself). 

Case 2a-i: r(a)=1,r(c)=0,r(d)=1,r(e)=0,r(f)=0,r(g)=0,r(h)=0, r(b)=0. Reds a=(1,0)[E], d=(-1,0)[W]. Whites: w,b,c,e,f,g,h. So N,S axis white (b,f), E,W red, all diagonals white. Symmetric to case 1 rotated. w witnesses 2 reds (E,W). Forces N,S and all diagonals white.

So witnessing 2 reds: the two reds are opposite axis neighbors, and the other 2 axis + 4 diagonals white (6 whites around). Very white-heavy locally.

- 1 red: even more white-heavy.
- 0 reds: w in no private block.

So to minimize whites, we want whites witnessing as many reds as possible (4 ideal), but 4 forces full cascade (all axis neighbors white → rows). 3 forces 3 axis neighbors white. 2 forces 2 axis + 4 diag white.

The cascade issue: whites witnessing 4 need all 4 axis neighbors white. If we have a region of whites all witnessing 4, it's axis-connected and extends. On a torus, a maximal axis-connected white component where every member witnesses 4 must be a union of full rows and full columns (since axis-connected and closed under axis neighbors means if (0,0) in it, (1,0) in it, (2,0) in it, ... entire row 0; and (0,1),(0,-1)... entire column 0; and then their rows...). Actually closure under all 4 axis neighbors means: component is closed under ±x and ±y steps, so it's a Cartesian product of a set of rows and set of columns? No: if (0,0) in C and C closed under axis neighbors, then all (x,0) in C (row 0) and all (0,y) in C (col 0), and then (x,0) in C → (x,y) all? (x,0) closed under y → (x,1),(x,2)... so column x fully in C. So C = entire torus. So the only nonempty axis-closed subset of the torus is the whole torus. So if any white witnesses 4 (needs all 4 axis neighbors white) and those neighbors also witness 4 (need their axis neighbors white)... but they need not witness 4. The cascade only continues if the neighbors also witness 4. 

So we can have isolated whites witnessing 4 as long as their axis neighbors are white but those neighbors witness fewer (so don't force further). Let me reconsider: white w witnesses 4 ⟹ axis neighbors white. Those axis neighbors (say (1,0)) are white; (1,0) might witness only 2 or 3, not forcing (2,0) white. So cascade stops. Good. So we can have whites witnessing 4 without full rows, as long as their axis neighbors are "low-witness" whites.

But the axis neighbors being white and low-witness: e.g., (1,0) white witnessing 2 (case 1 or 2a-i). Case 2a-i for (1,0): needs N=(1,1), S=(1,-1) white and E=(2,0),W=(0,0) red, diagonals (2,1),(2,-1),(0,1),(0,-1) white. But (0,0)=w is white, not red! Contradiction (case 2a-i needs W=(0,0) red). Case 1 for (1,0): needs E=(2,0),W=(0,0) white, N=(1,1),S=(1,-1) red, diagonals white. (0,0)=w white ✓ (W white). So (1,0) witnessing 2 via case 1: E=(2,0) white, W=(0,0) white, N=(1,1) red, S=(1,-1) red, diagonals (2,1),(2,-1),(0,1),(0,-1) white. But w=(0,0) witnesses 4 requires (0,1) red (diagonal of w? no: w's diagonals are (1,1),(−1,1),(1,−1),(−1,−1); w witnessing 4 needs diagonals red, i.e., (1,1) red ✓ (matches (1,0)'s N red), (1,-1) red ✓ (matches (1,0)'s S red), (-1,1) red, (-1,-1) red. And (1,0)'s diagonals (0,1),(0,-1) white — but w witnessing 4 needs (0,1) and (0,-1) white (axis neighbors of w) ✓. And (2,1),(2,-1) white (from (1,0) case1). And (2,0) white (from (1,0) case1 E). 

So combining: w=(0,0) witnesses 4, (1,0) witnesses 2 (case1). Let me list colors so far:
- w=(0,0): W
- w's axis: (1,0)W, (-1,0)W, (0,1)W, (0,-1)W
- w's diagonals: (1,1)R, (-1,1)R, (1,-1)R, (-1,-1)R
- (1,0) case1: E=(2,0)W, diagonals (2,1)W, (2,-1)W, (0,1)W✓, (0,-1)W✓. N=(1,1)R✓, S=(1,-1)R✓.
So new: (2,0)W, (2,1)W, (2,-1)W.

Now (0,1) is white (axis neighbor of w). What does (0,1) witness? Its neighbors: N=(0,2), S=(0,0)=w W, E=(1,1)R, W=(-1,1)R. For (0,1) to witness reds, consider its cells. (0,1) is white. Cells through (0,1): 
- {(0,1),(1,1),(0,2),(1,2)}: (1,1)R, need (0,2),(1,2) for count.
- {(-1,1),(0,1),(-1,2),(0,2)}: (-1,1)R.
- {(0,0),(1,0),(0,1),(1,1)}: = w's NE cell, (1,1)R, (0,0)W,(1,0)W → 1 red (1,1). private for (1,1) ✓. So (0,1) witnesses (1,1).
- {(-1,0),(0,0),(-1,1),(0,1)}: w's NW cell, (-1,1)R, (-1,0)W,(0,0)W → 1 red (-1,1). private ✓. witnesses (-1,1).
So (0,1) witnesses at least (1,1) and (-1,1) via w's cells. Plus possibly more via (0,2),(1,2),(-1,2). 

This is getting complicated but seems consistent. The pattern might extend. Let me try to see the global pattern emerging:

Whites: (0,0), (1,0), (-1,0), (0,1), (0,-1), (2,0), (2,1), (2,-1), ... and by symmetry (-2,0),(-2,1),(-2,-1)? Let me check (-1,0) similar to (1,0): (-1,0) white, by symmetry (reflect x) it'd be case1 with W=(-2,0) white, E=(0,0) white, N=(-1,1)R, S=(-1,-1)R, diagonals (-2,1)W,(-2,-1)W,(0,1)W,(0,-1)W. So (-2,0)W, (-2,1)W, (-2,-1)W.

And (0,-1) similar (reflect y): (0,-2)W, (1,-2)W, (-1,-2)W. (0,1): (0,2)W, (1,2)W, (-1,2)W.

So whites spreading. It seems like the pattern is growing into a diamond/cross shape. Let me see: whites at origin, plus axis arms extending, with reds at diagonals of origin and... Let me map out more.

Current whites: (0,0); (±1,0),(0,±1); (±2,0),(±2,±1),(0,±2),(±1,±2); 
Reds: (±1,±1) [the 4 diagonals of origin].

Now (2,0) is white (from (1,0)'s E). What does (2,0) witness? (2,0) neighbors: E=(3,0), W=(1,0)W, N=(2,1)W, S=(2,-1)W. (2,0) is in cells:
- {(1,0),(2,0),(1,1),(2,1)}: (1,1)R, (1,0)W,(2,0)W,(2,1)W → 1 red (1,1). private ✓. witnesses (1,1).
- {(2,0),(3,0),(2,1),(3,1)}: depends on (3,0),(3,1).
- {(1,-1),(2,-1),(1,0),(2,0)}: (1,-1)R,(2,-1)W,(1,0)W,(2,0)W → 1 red (1,-1). witnesses (1,-1).
- {(2,-1),(3,-1),(2,0),(3,0)}: depends.
So (2,0) witnesses (1,1) and (1,-1) at least. To witness more (via (3,0) cells), need (3,0) etc. If (2,0) is like (1,0) (case1, witnessing 2), then E=(3,0) white, N=(2,1) red?? But (2,1) is white (set above). Contradiction. So (2,0) can't be case1 (needs N=(2,1) red, but (2,1) white). 

Hmm so the pattern breaks. (2,0) has N=(2,1)W, S=(2,-1)W, W=(1,0)W. For (2,0) to witness reds, let me see which case. (2,0) with W=(1,0)W, N=(2,1)W, S=(2,-1)W. The cells:
- NW cell { (1,0),(2,0),(1,1),(2,1) }: (1,1)R → 1 red. witnesses (1,1).
- SW cell { (1,-1),(2,-1),(1,0),(2,0) }: (1,-1)R → 1 red. witnesses (1,-1).
- NE cell { (2,0),(3,0),(2,1),(3,1) }: (2,1)W, need (3,0),(3,1).
- SE cell { (2,-1),(3,-1),(2,0),(3,0) }: (2,-1)W, need (3,0),(3,-1).

For (2,0) to witness a 3rd red, need NE or SE cell to have exactly 1 red. NE: (2,0)W,(2,1)W, so red count among (3,0),(3,1) must be 1 for exactly 1 red total. SE: (2,0)W,(2,-1)W, red among (3,0),(3,-1) =1 for 1 red. 

If (3,0) red: NE has (3,0)R,(3,1)?; SE has (3,0)R,(3,-1)?. For NE exactly 1 red: (3,1) white. For SE exactly 1 red: (3,-1) white. Then NE witnesses (3,0), SE witnesses (3,0) (same). So (2,0) witnesses (1,1),(1,-1),(3,0) = 3 distinct. With (3,0) red, (3,1)W, (3,-1)W. 

So (2,0) witnesses 3 reds (like case 2a-ii or similar). Config: (2,0)W, W=(1,0)W, N=(2,1)W, S=(2,-1)W, E=(3,0)R, and (3,1)W,(3,-1)W. Reds near: (1,1),(1,-1),(3,0). This matches a "3-witness" config (3 axis neighbors white: W,N,S; 1 axis red: E; diagonals adjacent to E (3,1),(3,-1) white; diagonals adjacent to W... (1,1),(1,-1) red). Yes! Exactly case 2a-ii pattern (3 axis white, 1 axis red (E), the two diagonals next to E white, the two diagonals next to W red). 

So (2,0) is a 3-witness white. Good, consistent. So the pattern: along the +x axis, whites at (0,0)[4-wit], (1,0)[2-wit], (2,0)[3-wit], (3,0)[red!]. Wait (3,0) is red. So the arm extends (0,0)W,(1,0)W,(2,0)W,(3,0)R. And (3,0) red needs its own witness. 

(3,0) red: needs a cell with 3 whites. Cells through (3,0):
- {(2,0),(3,0),(2,1),(3,1)}: (2,0)W,(3,0)R,(2,1)W,(3,1)W → 3 whites! ✓ witness for (3,0). 
So (3,0) is witnessed by cell {(2,0),(3,0),(2,1),(3,1)} with whites (2,0),(2,1),(3,1). 

So the arm: ...W(2,0), R(3,0), and (3,0) witnessed. What about (3,0)'s other neighbors and continuing? (3,0) red, (3,1)W, (3,-1)W, (4,0)?. 

Now (3,1) white: neighbors N=(3,2), S=(3,0)R, E=(4,1), W=(2,1)W. (3,1) in cells:
- {(2,1),(3,1),(2,2),(3,2)}: (2,1)W, depends (2,2),(3,2).
- {(3,1),(4,1),(3,2),(4,2)}: depends.
- {(2,0),(3,0),(2,1),(3,1)}: (3,0)R, others W → 1 red. witnesses (3,0).
- {(3,0),(4,0),(3,1),(4,1)}: (3,0)R, (3,1)W, depends (4,0),(4,1).
So (3,1) witnesses (3,0) at least. 

This is getting very intricate. The pattern seems to be a growing cross/arrow. Let me step back and think about whether there's a clean periodic pattern achieving the bound, rather than this ad hoc growth.

Given the complexity, let me reconsider the problem scale: 100×100, answer likely a specific number. The bound r ≤ 5714. Let me hypothesize the answer is 5714 and check if a construction exists, or find the exact value.

Actually, let me reconsider. This is a known competition problem. Let me think about which competition. "Critical coloring" of 100×100 grid, 2×2 cells, maximal minimal. This might be from a Russian olympiad or similar. The answer... let me think.

Let me reconsider the counting bound and whether 5714 is achievable with a clever periodic construction of period 7 (since 7 is the key number, but 100 not divisible by 7). Hmm, 100 = 7·14+2. Period 7 won't tile 100 evenly. But the problem is on a torus of size 100, so the pattern must have period dividing 100. 7 doesn't divide 100. So a period-7 pattern won't work directly. So maybe the bound 5714 isn't achievable and the real answer relates to divisors of 100.

Divisors of 100: 1,2,4,5,10,20,25,50,100. Let me think about period-4 or period-5 patterns.

Let me reconsider. Maybe a cleaner bound gives a number related to 100's divisors. Let me reconsider the witness counting but per-row or using a smarter inequality.

Let me reconsider. Let me think about "each red needs a witness block; witness block has 3 whites in an L; the red is at the missing corner." Consider orienting each witness: the red is at one of 4 corners of its witness block. Assign each red an orientation (which corner it is in its chosen witness block): NE/NW/SE/SW (i.e., red is at bottom-left, bottom-right, top-left, top-right of the witness block). 

Now, a witness block with red at bottom-left (orientation NE, meaning red is SW corner, whites are the other 3 = N, E, NE): block {(x,y)R, (x+1,y)W, (x,y+1)W, (x+1,y+1)W}. The 3 whites form an L (top-right L). 

Let me count whites by "role". Hmm.

Alternative cleaner bound: Let me use a discharging or a per-2×2-block argument with the torus structure.

Actually, let me reconsider. Let me reconsider the possibility that the answer is 5000. Construction: checkerboard-ish? Let me think of whites as one color of a checkerboard: (i+j) even white. Then 5000 whites, 5000 reds. Every 2×2 block has 2 white 2 red. No W4 ✓ (only 2 whites). Condition (b): every red needs a witness block with 3 whites. But every block has exactly 2 whites. So no witness. Fails. 

So checkerboard fails minimality. Need blocks with 3 whites. So we need some blocks with 3 whites (witness) and the rest with ≥1 red. To have many reds, most blocks should have few whites (1 or 0), but we need enough 3-white blocks to witness all reds. Each 3-white block witnesses 1 red. So need ≥ r three-white blocks, i.e., a_3 ≥ r. And total white incidences 4w = a_1 + 2a_2 + 3a_3. To minimize w with a_3 ≥ r = 10000 - w: we want a_1, a_2 small and a_3 large. Max a_3 given 4w = a_1+2a_2+3a_3 and a_0+a_1+a_2+a_3=10000: to maximize a_3, set a_0=a_1=a_2=0 → a_3=10000, 4w=30000, w=7500, r=2500. That's the all-3-white construction (min reds). To minimize w (max reds), we want a_3 = r exactly (just enough witnesses) and a_1,a_2,a_0 absorbing the rest with few white incidences. With a_3 = r = 10000 - w: 4w = a_1 + 2a_2 + 3(10000 - w) → 7w = a_1 + 2a_2 + 30000. To minimize w, minimize a_1 + 2a_2. Minimum is 0 (a_1=a_2=0) → w = 30000/7 ≈ 4285.7 → w=4286 (ceil), r=5714, with a_1+2a_2 = 7·4286 - 30000 = 2. So a_1 + 2a_2 = 2, a_3 = 5714, a_0 = 10000 - a_1 - a_2 - 5714. If a_2=1,a_1=0: a_0=5714-... 10000-1-5714=4285. If a_1=2: a_0=10000-2-5714=4284. So almost all blocks are 0-white (all red) or 3-white, with just 1 or 2 blocks of 1 or 2 whites. 

So the optimal structure (if achievable): almost all blocks either all-red (0 white) or 3-white (witness), with exactly r=5714 three-white blocks and 4285 or 4284 all-red blocks, plus 1-2 exceptional blocks. And a_3 = r means every red has exactly one witness block (no red has 2), and every 3-white block witnesses its red (surjective bijection). 

Now the question: can we tile the 100×100 torus with 0-white and 3-white blocks (each block all-red or 3W1R) such that it's consistent (adjacent blocks agree on shared edges) and the red/white assignment is a valid coloring? With 5714 blocks of 3W1R and 4286 blocks of 0W (all red), and 4286 white points total.

Wait, white points: each 3-white block has 3 whites, but whites shared between blocks. Total whites w=4286. Total white incidences = 3·5714 + 0·4286 = 17142 = 4·4286 - 2 = 17144 - 2. So deficit 2: two white incidences "missing" meaning... 4w = 17144 but a_1+2a_2+3a_3 = 0+0+3·5714=17142. So 4w - (sum) = 2. But 4w must equal sum of incidences exactly! 4w = a_1 + 2a_2 + 3a_3 + 4a_4 but a_4=0. So 4w = a_1 + 2a_2 + 3a_3 exactly. With w=4286: 4w=17144. a_3=5714: 3a_3=17142. So a_1+2a_2 = 2. So we need a_1+2a_2=2 exactly. So either a_2=1 (one 2-white block) or a_1=2 (two 1-white blocks) or a_1=1,a_2=... no a_1+2a_2=2: (a_1=2,a_2=0) or (a_1=0,a_2=1). And a_0 = 10000 - a_1 - a_2 - 5714. For (a_1=2,a_2=0): a_0 = 4284. For (a_1=0,a_2=1): a_0=4285.

So the optimal coloring (r=5714) would have all blocks 0- or 3-white except 1 or 2 exceptional blocks. Is such a near-perfect tiling possible on 100×100 torus?

The constraint that adjacent blocks share an edge and must agree: Let me think about what 0-white and 3-white blocks look like and adjacency. A 0-white block = all 4 red. A 3-white block = 3W1R (red at one corner). 

Two adjacent 3-white blocks sharing an edge: e.g., block A={(0,0),(1,0),(0,1),(1,1)} 3W1R and block B={(1,0),(2,0),(1,1),(2,1)} 3W1R, share edge {(1,0),(1,1)}. The shared edge points have fixed colors. In A, the red is at one corner; in B, red at one corner. The shared edge {(1,0),(1,1)}: if A's red is at (0,0) (so (1,0),(1,1) white), then shared edge both white. Then B's red is at (2,0) or (2,1) (since (1,0),(1,1) white). If B's red at (2,0): B={(1,0)W,(2,0)R,(1,1)W,(2,1)W}. Consistent. So two 3-white blocks can be adjacent with reds on the outer edge (forming a "domino" of reds separated by 2 whites). 

Let me think about tiling with a pattern. Consider a "stripe" of 3-white blocks. Actually, let me think of the following pattern: red points form isolated points, each surrounded by 3 whites in its witness block, and the rest all red. But "rest all red" means 0-white blocks, which are all-red 2×2. But if reds are dense (5714 reds, 4286 whites), and 4284 blocks all-red... an all-red block has 4 reds. 4284 all-red blocks would contain up to 4·4284 red incidences but reds shared. Hmm.

Let me think about the white points' arrangement. 4286 whites, each in 4 blocks, total 17144 incidences, of which 17142 are in 3-white blocks (5714 blocks × 3) and 2 in the exceptional block(s). So almost every white incidence is in a 3-white block. A white point is in 4 blocks; ideally all 4 are 3-white blocks (then it's in 4 witness blocks, witnessing up to 4 reds — the saturated case). With deficit 2, almost all whites are in 4 three-white blocks (saturated), except deficit 2 (e.g., one white in only 2 three-white blocks + 2 in other, or two whites in 3 three-white blocks + 1 other). 

But we showed saturated whites (in 4 three-white blocks) require the plus pattern (axis neighbors white, diagonal red), which cascades. And ~4285 saturated whites cascade into all-white rows → W4 blocks → contradiction (we can't have W4, but saturated whites' axis neighbors are white, not W4 directly; W4 would need a 2×2 all white). Let me re-examine: saturated white w has axis neighbors white and diagonal red. The 2×2 block NE of w = {(0,0)W,(1,0)W,(0,1)W,(1,1)R}: 3W1R, not W4 ✓. So saturated whites don't directly create W4. The issue is whether a large axis-connected white region creates W4 somewhere. 

If we have a 2×2 all-white block, that's W4 (forbidden). When does that happen? A 2×2 block all white means all 4 corners white. In our structure, blocks are 0W or 3W (mostly). A 3W block has 1 red, so not all white. A 0W block all red. So no block is all white! So condition (a) automatically satisfied if all blocks are 0W or 3W. The exceptional block (1 or 2 white) also not all white. So condition (a) is fine. 

So the only obstruction to r=5714 is whether we can realize a coloring where all blocks are 0W or 3W (plus 1-2 exceptions) consistently, with 4286 whites. The cascade argument was about saturated whites forcing axis neighbors white, but that's fine as long as no W4 — and there's no W4 since all blocks 0W/3W. Wait, but does "saturated white forces axis neighbors white" hold, and does that force the structure to be the all-3W tiling (r=2500)? Let me reconsider.

If almost all whites are saturated (in 4 three-white blocks), each saturated white has axis neighbors white and diagonal red. Consider the white set. Saturated white w: axis neighbors white. Are axis neighbors saturated? An axis neighbor (1,0) is white; is it in 4 three-white blocks? (1,0) is in cells: NE{(1,0),(2,0),(1,1),(2,1)}, NW{(0,0),(1,0),(0,1),(1,1)}, SE{(1,-1),(2,-1),(1,0),(2,0)}, SW{(0,-1),(1,-1),(0,0),(1,0)}. For (1,0) to be saturated (all 4 cells 3-white), need each cell to have exactly 1 red. NW cell {(0,0),(1,0),(0,1),(1,1)}: (0,0)W,(1,0)W,(0,1)W,(1,1)R → 1 red ✓ (this is w's NE cell, 3W1R). SE cell {(0,-1),(1,-1),(0,0),(1,0)}: w's SE cell, (1,-1)R, others W → 1 red ✓. NE cell {(1,0),(2,0),(1,1),(2,1)}: (1,1)R, (1,0)W, need (2,0),(2,1): for 1 red total need (2,0)W,(2,1)W. SW cell {(0,-1),(1,-1),(0,0),(1,0)} already counted (that's w's SE). Wait I need the 4 cells of (1,0): 
(1,0) is corner of: C(1,0)={(1,0),(2,0),(1,1),(2,1)} [as bottom-left], C(0,0)={(0,0),(1,0),(0,1),(1,1)} [as bottom-right], C(1,-1)={(1,-1),(2,-1),(1,0),(2,0)} [as top-left], C(0,-1)={(0,-1),(1,-1),(0,0),(1,0)} [as top-right].
- C(0,0) = w's NE cell: 3W1R (red (1,1)) ✓.
- C(0,-1) = w's SE cell: {(0,-1),(1,-1),(0,0),(1,0)}: (1,-1)R, rest W ✓ 3W1R.
- C(1,0) = {(1,0),(2,0),(1,1),(2,1)}: (1,0)W,(1,1)R, need (2,0),(2,1) both W for 3W1R (red (1,1)). 
- C(1,-1) = {(1,-1),(2,-1),(1,0),(2,0)}: (1,-1)R,(1,0)W, need (2,-1),(2,0) both W for 3W1R (red (1,-1)).
So (1,0) saturated needs (2,0)W,(2,1)W,(2,-1)W. I.e., (2,0) white and (2,±1) white. 

So if (1,0) is also saturated, then (2,0) white and (2,1),(2,-1) white. Then (2,0) saturated needs (3,0)W,(3,1)W,(3,-1)W and (2,1)W,(2,-1)W (already). Etc. So the +x arm: (0,0)W,(1,0)W,(2,0)W,(3,0)W,... all white, and (k,±1) white for all k. So entire rows y=0, y=1, y=-1 become white?? (k,1) white for all k → row 1 all white. (k,-1) white → row -1 all white. (k,0) white → row 0 all white. Then rows 0,1,-1 all white → 2×2 blocks within rows 0,1 all white → W4! Contradiction.

So if (1,0) is saturated (in addition to w), we get W4. So we can't have two adjacent saturated whites (axis-adjacent). Because saturated white forces axis neighbors white, and if an axis neighbor is also saturated, it forces the next layer, eventually filling rows → W4. 

More precisely: saturated whites can't be axis-adjacent to each other (else cascade → W4). Actually let me verify: the contradiction came from (1,0) saturated forcing (2,1),(2,-1) white and (2,0) white; then (2,0) saturated forcing (3,±1),(3,0) white; inductively all (k,0),(k,1),(k,-1) white → rows 0,±1 all white → W4. So yes, two axis-adjacent saturated whites → eventually W4. So saturated whites form an independent set in the axis-adjacency graph (no two axis-adjacent). 

But saturated white w forces its 4 axis neighbors to be white. Those axis neighbors are white but NOT saturated (since saturated whites independent, and they're axis-adjacent to w which is saturated). So axis neighbors of saturated whites are non-saturated whites. 

Now, how many saturated whites can we have? They're an independent set in axis-adjacency graph (grid graph), so at most 5000 (checkerboard). But also each saturated white needs 4 axis neighbors white (non-saturated). 

Recall we need ~4285 saturated whites (deficit 2 means ~4285 of the 4286 whites are saturated). But saturated whites must be independent (≤5000, ok) AND each needs 4 white axis neighbors. With 4285 saturated and 4286 total whites, only 1 non-saturated white. But each saturated white needs 4 axis neighbors white (non-saturated, since saturated can't be axis-adjacent). So each saturated white needs 4 distinct non-saturated white neighbors. With only 1 non-saturated white, impossible (can't have 4285 saturated each needing 4 non-saturated neighbors from a pool of 1). 

Contradiction! So r=5714 is impossible. 

Let me formalize: Let s = number of saturated whites (in 4 three-white blocks). Each saturated white has 4 axis neighbors, all white and non-saturated (non-saturated because saturated whites are axis-independent). So number of non-saturated whites ≥ ... each saturated white contributes 4 "requirements" of non-saturated white axis neighbors. A non-saturated white can be axis-neighbor to up to 4 saturated whites. So 4s ≤ 4·(non-saturated whites) → s ≤ non-saturated whites. Total whites w = s + (non-saturated) ≥ 2s. So s ≤ w/2. 

Now the incidence: 3r ≤ 4w - (deficit from non-saturated). Non-saturated whites are in fewer than 4 three-white blocks. Let me bound total incidences in 3-white blocks = 3a_3 ≤ 4s + 3·(non-saturated) [saturated contribute 4, non-saturated contribute ≤3]. Actually non-saturated whites are in ≤3 three-white blocks (since not saturated means <4). So 3a_3 ≤ 4s + 3(w - s) = 3w + s. And a_3 ≥ r = 10000 - w. So 3(10000 - w) ≤ 3w + s ≤ 3w + w/2 = 3.5w. → 30000 - 3w ≤ 3.5w → 30000 ≤ 6.5w → w ≥ 30000/6.5 = 4615.38 → w ≥ 4616, r ≤ 5384.

Hmm, let me double check: 30000 ≤ 6.5 w → w ≥ 4615.38 → w ≥ 4616, r ≤ 10000 - 4616 = 5384.

But wait, I need to double-check the saturated independence claim and the "non-saturated in ≤3 three-white blocks" and refine. Also non-saturated could be in 4 blocks but not all 3-white (some 0-white or 2-white). Let me reconsider: "saturated" = in 4 three-white blocks. A white in 4 blocks total; if not saturated, it's in ≤3 three-white blocks (could be in 4 blocks but one is not 3-white). So non-saturated white contributes ≤3 incidences to three-white blocks. OK.

And saturated independence: two axis-adjacent saturated whites → cascade → W4. Let me re-examine if this is airtight. Saturated white w at (0,0): axis neighbors (1,0),(-1,0),(0,1),(0,-1) white, diagonals (1,1),(-1,1),(1,-1),(-1,-1) red. Now (1,0) saturated: axis neighbors (2,0),(0,0),(1,1),(1,-1) white. But (1,1) is red (from w saturated)! Contradiction immediately. So (1,0) can't be saturated because w saturated forces (1,1) red, but (1,0) saturated forces (1,1) white. 

So saturated whites can't be axis-adjacent (immediate contradiction, no need for cascade). So saturated whites axis-independent. Confirmed, even stronger.

So s ≤ w/2 (each saturated needs 4 non-saturated axis neighbors, each non-saturated serves ≤4 saturated, so 4s ≤ 4(w-s) → s ≤ w-s → s ≤ w/2). 

And 3a_3 ≤ 4s + 3(w-s) = 3w + s ≤ 3w + w/2 = 7w/2. With a_3 ≥ r = 10000 - w: 3(10000-w) ≤ 7w/2 → 30000 - 3w ≤ 7w/2 → 30000 ≤ 13w/2 → w ≥ 60000/13 = 4615.38 → w ≥ 4616, r ≤ 5384.

Can we tighten further? The non-saturated whites that are axis neighbors of saturated whites — what structure? A non-saturated white that's an axis neighbor of a saturated white: e.g., (1,0) with w=(0,0) saturated. (1,0) is white, (1,1) red, (1,-1) red (from w saturated), (0,0) white, (2,0)=?. (1,0)'s cells: C(0,0) [w's NE, 3W1R, red (1,1)], C(0,-1) [w's SE, 3W1R, red (1,-1)], C(1,0)={(1,0),(2,0),(1,1),(2,1)}: (1,0)W,(1,1)R, so this block has ≥1 red (1,1); for it to be 3-white need (2,0),(2,1) white → then 3W1R red(1,1). C(1,-1)={(1,-1),(2,-1),(1,0),(2,0)}: (1,-1)R,(1,0)W, for 3W need (2,-1),(2,0) white. So (1,0) is in 2 three-white blocks for sure (w's NE, SE), and potentially 2 more (C(1,0),C(1,-1)) if (2,0),(2,1),(2,-1) white. If (1,0) is non-saturated (in ≤3 three-white blocks), then at most one of C(1,0), C(1,-1) is 3-white. 

Hmm, so (1,0) contributes 2 or 3 to three-white block incidences. If it contributes exactly 2 (both C(1,0),C(1,-1) not 3-white, i.e., (2,0) or (2,±1) red), then deficit 2 from this white. If 3, deficit 1.

Let me reconsider the bound more carefully. Let me define for each white the number t = number of three-white blocks it's in (0≤t≤4). Saturated: t=4. Sum of t over whites = 3a_3. We have 3a_3 ≥ 3r (since a_3 ≥ r, actually a_3 ≥ r so 3a_3 ≥ 3r; but we want upper bound on 3a_3 to constrain). Wait we want to show w large, so we want 3a_3 ≤ something in terms of w, combined with 3a_3 ≥ 3(10000-w). 

3a_3 = sum t. We need upper bound on sum t given the structure. Saturated (t=4) are axis-independent and each forces 4 axis neighbors white (those have t ≤ 3, and actually let me see their t). 

Let me reconsider: maybe non-saturated whites that are axis-neighbors of saturated have t ≤ 2 or 3. Let me compute the max t for an axis-neighbor of a saturated white. (1,0) with w saturated: t ≥ 2 (w's NE, SE cells). Can be 3 or 4. If t=4, (1,0) saturated → contradiction (shown). So t ≤ 3. Can t=3? Yes if exactly one of C(1,0),C(1,-1) is 3-white. So t∈{2,3} for axis-neighbor of saturated (assuming (1,0) is in w's two cells which are 3-white). Actually t≥2 always for axis-neighbor of saturated. And t≤3. 

What about whites not adjacent to any saturated white? They could have t up to 4 but if t=4 they'd be saturated (and then their axis neighbors white...). Hmm, any t=4 white is saturated and axis-independent from other saturated. 

This is getting complicated. Let me just try to find the exact optimum by considering a clean construction and matching bound. Let me guess the answer involves 13 (from 60000/13). 60000/13 = 4615.38, r ≤ 5384. 5384 = ? 10000 - 4616. Hmm 5384 = 13·414.15 no. 5384/8=673. Not clean. Let me see if the bound tightens to a cleaner number with more analysis, or if 5384 is it.

Actually, let me reconsider whether saturated whites' axis-neighbors have t ≤ 2 (not 3), which would tighten. (1,0) axis-neighbor of saturated w=(0,0). t = number of 3-white blocks through (1,0). We have C(0,0) and C(0,-1) are 3-white (w's        — AI历史解题过程（thinking）
#   polymath_04438         — 题目ID

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
  <problem_id>polymath_04438</problem_id>
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

A coloring of all plane points with coordinates belonging to the set $S=\{0,1,\ldots,99\}$ into red and white colors is said to be [i]critical[/i] if for each $i,j\in S$ at least one of the four points $(i,j),(i + 1,j),(i,j + 1)$ and $(i + 1, j + 1)$ $(99 + 1\equiv0)$ is colored red. Find the maximal possible number of red points in a critical coloring which loses its property after recoloring of any red point into white.

## Standard Solution

To solve this problem, we need to find the maximal number of red points in a critical coloring of the plane points with coordinates in the set \( S = \{0, 1, \ldots, 99\} \). A coloring is critical if for each \( i, j \in S \), at least one of the four points \((i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)\) is colored red, with the condition that \(99 + 1 \equiv 0\).

1. **Initial Setup and Definitions**:
   - Let \( r \) be the number of red points.
   - We need to ensure that each 2x2 square on the grid contains at least one red point.
   - We aim to find the maximum \( r \) such that the coloring is critical and loses its property if any red point is recolored to white.

2. **Constructing the Argument**:
   - Consider the grid as a collection of \( 100 \times 100 = 10000 \) points.
   - We need to cover each 2x2 square with at least one red point.
   - Suppose we have \( r \) red points. We can choose \( r \) 2x2 squares, each containing exactly one red point, ensuring that each red point is in one of these squares.

3. **Average Calculation**:
   - In each white cell, write the number of chosen squares that contain it.
   - The average number written in the white cells is given by:
     \[
     \frac{3r}{10000 - r}
     \]
   - This average is increasing with \( r \) and equals 3 when \( r = 5000 \).

4. **Bounding the Average**:
   - We claim that this average cannot be more than 3.
   - If a number greater than 3 is written in a white cell, then the number must be 4, and it must come in the following configuration:
     \[
     \begin{array}{ccc}
     R & 2 & R \\
     2 & 4 & 2 \\
     R & 2 & R \\
     \end{array}
     \]
     Here, \( R \) represents a red cell, and the numbers are what's written in the white cells.

5. **Pairing and Averaging**:
   - We can pair each occurrence of 4 with the white cell with 2 right above it, and the average of this pair is 3.
   - No white cell is part of two pairs, so by averaging over these pairs and unpaired white cells, we get the average of numbers on the whole board is at most 3.

6. **Conclusion**:
   - Since the average cannot exceed 3, the maximum number of red points \( r \) that satisfies the critical coloring condition is 5000.
   - If we have more than 5000 red points, the average would exceed 3, which is not possible.

The final answer is \( \boxed{5000} \)

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. We have a 100×100 toroidal grid (indices 0..99 with wraparound), colored red/white. Critical means: for every unit square (2×2 cell) with corners (i,j),(i+1,j),(i,j+1),(i+1,j+1), at least one is red. We want a critical coloring that is minimal in the sense that removing any red point (turning it white) destroys criticality. Find the maximum number of red points in such a minimal critical coloring.

So we want a maximal minimal hitting set: a set R of red points such that:
1. R hits every 2×2 square (every unit cell has ≥1 red point).
2. R is minimal: every red point is essential, i.e., for each red point p, there exists a 2×2 square where p is the only red point.
3. We want to maximize |R|.

This is a classic problem about minimal hitting sets / minimal vertex covers on the hypergraph of 2×2 cells. Each cell is a 4-element hyperedge. We want a minimal transversal (minimal hitting set) of maximum size.

A minimal transversal T of a hypergraph H: T hits every edge, and for every t in T, there's an edge e with e ∩ T = {t} (t is the unique representative of that edge).

We want the maximum size of a minimal transversal.

Let me think about the structure. The grid is 100×100 torus. Cells are indexed by (i,j) with i,j in 0..99, each cell C(i,j) = {(i,j),(i+1,j),(i,j+1),(i+1,j+1)} mod 100.

We want max minimal transversal.

Upper bound approach: For a minimal transversal, each red point needs a "private" cell where it's the only red point. So we can assign to each red point a distinct cell (the private cell). Actually each red point needs at least one private cell, but multiple red points could share... no. A private cell for red point p is a cell where p is the only red point. Two different red points can't share the same private cell (since a cell has only one red point in it as private). So the number of red points ≤ number of cells = 100×100 = 10000. But that's trivial (total points = 10000).

Wait, but each red point needs a private cell, and private cells are distinct. There are 10000 cells. So |R| ≤ 10000, trivially. We need a better bound.

Hmm, but actually the constraint is tighter. Let me think about it differently.

Let me think about which colorings are minimal critical and how many red points.

Consider the complement: white points W. Critical means every 2×2 cell has at least one red = not all-white. So W contains no 2×2 all-white block... no wait, every cell has at least one red means no cell is all white. So W is a set with no 2×2 all-white square, i.e., W has no "full cell". Equivalent: W is a subset such that no 2×2 block is entirely in W.

Minimality: every red point p has a private cell = a cell where the other 3 points are all white. So for each red point p, there's a cell containing p where the other 3 corners are white.

So we want to maximize red = minimize white, but with the constraint that every red point has a cell where it's surrounded by 3 white points (the other 3 corners of some cell are white).

Hmm, let me think about the maximum. Let me consider small cases first to get intuition, like a 1D analog or small torus.

Actually let me think about the structure of private cells. Each red point p=(a,b) is a corner of 4 cells: C(a-1,b-1), C(a-1,b), C(a,b-1), C(a,b) (the cells for which p is bottom-right, bottom-left, top-right, top-left respectively). For p to have a private cell, one of these 4 cells must have its other 3 corners white.

Let me think about an upper bound more carefully.

Consider the "private cell" assignment. Assign each red point to one private cell. This gives an injection from R to cells. Now consider a cell that is a private cell for red point p: it has exactly 1 red (p) and 3 white. 

Now, here's a key constraint: consider the white points. Each white point is in 4 cells. 

Let me think about counting. Let r = |R|, w = |W| = 10000 - r.

Each red point has ≥1 private cell with 3 white corners. So there are ≥ r cells with exactly 1 red and 3 white. The remaining 10000 - r cells have ≥1 red (could be 1,2,3,4 red).

Hmm, let me think about a clever construction for large r and matching upper bound.

Let me think about the problem as: we want a minimal transversal of the 4-uniform hypergraph of 2×2 cells on the torus.

For minimal transversals, there's a general theory. The maximum minimal transversal... Let me think about specific constructions.

Construction idea 1: Checkerboard. Color (i,j) red if i+j even. Then every 2×2 cell has exactly 2 red. Is it critical? Yes, every cell has 2 red ≥1. Is it minimal? No — removing one red point, the cell still has another red. So not minimal. We need each red to have a private cell.

Construction idea 2: Make most points red but ensure each red has a private cell. To have a private cell for red point p, we need a cell where p is the only red, i.e., 3 specific neighbors white. 

If we want to maximize red, we want few white points but arranged so that every red point has a nearby cell with 3 white corners including... wait the cell containing p with 3 white.

Let me think: a private cell for p is a cell C with C∩R = {p}. So C has p red, 3 white. The 3 white points of C are "witnesses" for p.

Each white point can serve as a witness for multiple red points (it's in 4 cells, each cell could be private for a different red point). 

Let me think about how many red points a single white point can witness. A white point w is a corner of 4 cells. In each such cell, w is white; if the other 3 corners have exactly 1 red, that cell is private for that red point, and w witnesses it. So one white point can witness up to 4 red points (one per adjacent cell), but actually it could witness the same... let me think. Each of the 4 cells containing w: if that cell has exactly 1 red point (among the other 3 corners + ... wait the cell has 4 corners including w which is white, so the cell has 1 red among the other 3 corners). That red point is witnessed by w. So w witnesses up to 4 red points (at most one per cell, and 4 cells).

But a red point needs 3 white witnesses (the 3 other corners of its private cell). 

Hmm, let me set up a counting / double counting.

Each red point has a private cell with 3 white corners. Count pairs (red point, white corner in its private cell): each red contributes 3, total 3r. Each white point is in at most 4 cells that could be private cells for some red, so contributes at most 4. Wait, but a white point in a private cell: the private cell has exactly 1 red. The white point w is in 4 cells; for each cell, if it's a private cell (1 red), w is one of its 3 white corners and witnesses that 1 red. So each white point witnesses at most 4 red points (one per cell). So 3r ≤ 4w, i.e., 3r ≤ 4(10000 - r), 7r ≤ 40000, r ≤ 5714.28..., r ≤ 5714.

Wait let me double check: each red point needs 3 white witnesses (the 3 white corners of its chosen private cell). Total witness incidences = 3r. Each white point can be a witness for at most 4 red points (since it's in 4 cells, each cell private for at most 1 red). So 3r ≤ 4w. With w = 10000 - r: 3r ≤ 40000 - 4r, 7r ≤ 40000, r ≤ 5714.28, so r ≤ 5714.

Hmm wait, but is this tight? Let me reconsider. Actually a white point w is in 4 cells. For each cell C containing w, C is private for at most one red point (the unique red in C if |C∩R|=1). And w witnesses that red. So w witnesses ≤ 4 reds. But also, could the same red be witnessed by w via two different cells? Possibly, but we're counting incidences and upper bounding by 4 per white. Actually we want: sum over white points of (number of red points witnessed) ≥ 3r (since each red needs 3 distinct white witnesses, all distinct white points within one cell). 

Hmm, actually each red point p has a private cell C_p with 3 white corners, all distinct. So p is witnessed by 3 distinct white points. Total incidences (p, w) where w is a white corner of C_p = 3r, and these are... could the same (p,w) pair appear? No, p fixed, w ranges over 3 distinct whites. Different p's. So total distinct incidences = 3r. Now each white w: how many red points is w a witness for? w is a corner of 4 cells; for each cell that is private (1 red), w witnesses that red. So ≤ 4. Hence 3r ≤ 4w. Good.

So r ≤ 5714. But is this achievable? Need 7 | 40000? 40000/7 = 5714.28, not integer. So r ≤ 5714. For r=5714, w=4286, 3r=17142, 4w=17144, so slack 2. Possible in principle.

But achieving the bound requires near-perfect arrangement: almost every white point witnesses exactly 4 red points, and almost every red has exactly 3 witnesses (its private cell). Let me think about whether a construction achieving ~5714 exists.

Hmm, this is getting complex. Let me reconsider — maybe the answer is cleaner. Let me reconsider the problem; it's a competition problem likely with a clean answer.

Let me reconsider. Maybe the bound 3r ≤ 4w isn't the right one or maybe there's a better construction giving a cleaner number.

Actually, let me reconsider the witness counting more carefully — maybe I can get a cleaner bound by considering the structure better, or maybe the answer is 5714 or maybe something else.

Let me reconsider. Actually, let me reconsider whether each white can witness 4. For w to witness a red via cell C, C must have exactly 1 red. If w is surrounded such that all 4 cells through w are private cells (each with exactly 1 red), then w witnesses 4 reds. That requires the 8 neighbors of w (in the grid, the cells around w) arranged so each of the 4 cells has exactly 1 red among its 3 non-w corners.

Let me think about a local pattern. Consider white point w at origin (0,0). The 4 cells: C(0,0)={ (0,0),(1,0),(0,1),(1,1)}, C(-1,0)={(-1,0),(0,0),(-1,1),(0,1)}, C(0,-1)={(0,-1),(1,-1),(0,0),(1,0)}, C(-1,-1)={(-1,-1),(0,-1),(-1,0),(0,0)}.

For each to have exactly 1 red among the 3 non-w corners:
- C(0,0): exactly 1 red among (1,0),(0,1),(1,1).
- C(-1,0): exactly 1 red among (-1,0),(-1,1),(0,1).
- C(0,-1): exactly 1 red among (0,-1),(1,-1),(1,0).
- C(-1,-1): exactly 1 red among (-1,-1),(0,-1),(-1,0).

This is a constraint satisfaction. Let me see if there's a periodic pattern.

This is getting complicated. Let me step back and think about the problem more cleverly, maybe there's a cleaner characterization.

Alternative approach: Think of it as a 2D problem. Let me consider rows. 

Actually, let me reconsider the problem from the perspective of "minimal critical" = minimal hitting set of 2×2 cells. The maximum minimal hitting set.

Let me think about 1D version first: points 0..n-1 on a cycle, "edges" are consecutive pairs {(i,i+1)}, critical = every edge has a red point = no two consecutive whites. Minimal critical = minimal vertex cover of cycle = every red has a white neighbor (so that removing it creates two consecutive whites). Max minimal vertex cover of cycle C_n: we want max set with no two consecutive whites (i.e., whites form independent set) and every red adjacent to a white. Whites independent set max size = floor(n/2). Reds = n - floor(n/2) = ceil(n/2). And minimality: every red adjacent to white. With whites being a max independent set (alternating), every red is between two whites, so removing a red creates... red r between two whites w1,w2: removing r, are w1,w2 consecutive? They're at distance 2, not consecutive. Hmm so removing r doesn't create consecutive whites necessarily. Wait the edge {(r-1,r)} and {(r,r+1)}: if r-1 and r+1 are white, removing r: edge {(r-1,r)} now has r-1 white and r white→ all white? No, edge {(r-1,r)} = {r-1, r}, r-1 white, r now white → both white → edge not covered. So yes removing r breaks it. Good, so minimality holds. So in 1D, max minimal vertex cover = ceil(n/2)... but wait we want to maximize red, so we want minimal vertex cover of maximum size. Max size minimal vertex cover of cycle.

Hmm, for cycle, minimal vertex covers: the complement is a maximal independent set. Max minimal vertex cover = n - min maximal independent set. Min maximal independent set of cycle C_n: for n≥... the minimum maximal independent set (independent dominating set) has size ceil(n/3). So max minimal vertex cover = n - ceil(n/3) = floor(2n/3).

Wait I need to recompute. Minimal vertex cover ⟺ complement is maximal independent set. To maximize vertex cover, minimize the maximal independent set (the complement). The minimum size of a maximal independent set = independent domination number = ceil(n/3) for cycle C_n. So max minimal vertex cover = n - ceil(n/3) = floor(2n/3).

For n=100: floor(200/3)=66. So in 1D analog the answer would be 66 out of 100.

OK so for 2D, the analog: minimal transversal of 2×2-cell hypergraph, max size = total - min maximal "independent set" where independent set = set W with no cell fully in W (i.e., W contains no full 2×2 block), and maximal means every red point (every point not in W) has a cell fully... no. Maximal independent set in hypergraph sense: W is independent (no edge ⊆ W) and maximal (can't add any point while staying independent). Adding point p (currently red) to W: W∪{p} independent means no cell ⊆ W∪{p}, i.e., no cell containing p has all other 3 corners in W. So maximality = for every red point p, there's a cell containing p with the other 3 corners in W. That's exactly the private cell condition! Great, consistent.

So max minimal transversal = n_total - min maximal independent set, where independent = no 2×2 all-white block, maximal = every point outside has a cell with other 3 corners inside.

Min maximal independent set = minimum number of white points such that (a) no 2×2 block is all white, and (b) every red point has a cell where the other 3 are white.

We want to minimize white points w. Then r = 10000 - w.

So now: minimize w subject to:
(a) No 2×2 block is entirely white.
(b) Every non-white (red) point p has a cell containing p whose other 3 corners are white.

Condition (b) is strong: every red point must be "adjacent" to a cell of 3 whites. 

Let me re-examine the counting bound 3r ≤ 4w → with r = 10000 - w: 3(10000-w) ≤ 4w → 30000 ≤ 7w → w ≥ 30000/7 = 4285.7 → w ≥ 4286, r ≤ 5714.

So we want to find min w ≥ 4286 (if achievable) such that conditions hold. Then r = 5714.

But is w=4286 achievable? Need 7w ≥ 30000, w=4286 gives 7·4286=30002 ≥ 30000. And 3r=3·5714=17142, 4w=17144, slack 2. So almost tight.

Hmm, but the answer 5714 seems ugly for a competition. Let me reconsider — maybe the counting bound isn't tight and the real answer is different, or maybe the problem expects 5714. Actually competition problems can have answers like 5714. But let me double-check the bound and think about constructions.

Wait, I should double check the witness counting. Let me redo: We need every red point to have a private cell (3 white corners). Choose one private cell per red point. Now count incidences (red point p, white corner w of C_p). Each red gives 3 incidences (3 white corners), total 3r. But the same (p, w) — for fixed p, the 3 whites are distinct. Across different p, could two reds share the same private cell? No, a private cell has exactly 1 red. So all C_p distinct, hence the white corners... a white point w could be a corner of multiple private cells (up to 4 cells contain w). So w appears in up to 4 incidences. So 3r ≤ 4w. Confirmed.

Now, is this achievable? Let me think about a construction. We want a configuration where each white point is a corner of exactly 4 private cells (witnesses 4 reds) — well, almost, since slack is 2, two white points witness only 3, or one witnesses 2, etc. And each red has exactly one private cell (with 3 whites) — but red could have more cells covered, that's fine; we just need ≥1 private.

Actually wait, we also need condition (a): no 2×2 all white. And the private cells have exactly 1 red so they're fine. But other cells (non-private) must also have ≥1 red. With w=4286 white points spread out, need no 2×2 all white. If whites are sparse (4286/10000 ≈ 0.43 density), 2×2 all white is possible if not careful. So arrangement matters.

This is getting really involved. Let me think about whether there's a cleaner formulation or known result.

Hmm, let me reconsider. Let me think about the structure of an optimal solution via "each white witnesses 4 reds" locally.

If every white point w witnesses exactly 4 reds (one per adjacent cell, each adjacent cell private), then each of the 4 cells through w has exactly 1 red (among the 3 non-w corners). Let me figure out the local pattern around an "ideal" white point.

Let me set up coordinates. White at (0,0). Neighbors involved: the 8 points at Chebyshev distance 1: (±1,0),(0,±1),(±1,±1). The 4 cells and their non-w corners:
- NE cell {(0,0),(1,0),(0,1),(1,1)}: corners (1,0),(0,1),(1,1), exactly 1 red.
- NW cell {(-1,0),(0,0),(-1,1),(0,1)}: (-1,0),(-1,1),(0,1), exactly 1 red.
- SE cell {(0,-1),(1,-1),(0,0),(1,0)}: (0,-1),(1,-1),(1,0), exactly 1 red.
- SW cell {(-1,-1),(0,-1),(-1,0),(0,0)}: (-1,-1),(0,-1),(-1,0), exactly 1 red.

Let me denote the 8 neighbors' colors. Let a=(1,0), b=(0,1), c=(1,1) [NE]; d=(-1,0), e=(-1,1), b=(0,1) [NW, shares b]; f=(0,-1), g=(1,-1), a=(1,0) [SE shares a]; h=(-1,-1), f=(0,-1), d=(-1,0) [SW shares d,f].

So the 8 distinct neighbors: a=(1,0), b=(0,1), c=(1,1), d=(-1,0), e=(-1,1), f=(0,-1), g=(1,-1), h=(-1,-1).

Constraints (exactly 1 red in each group):
- NE: {a,b,c}: exactly 1 red.
- NW: {d,e,b}: exactly 1 red.
- SE: {f,g,a}: exactly 1 red.
- SW: {h,f,d}: exactly 1 red.

From NE and NW: both contain b. From NE and SE: both contain a. From NW and SW: both contain d. From SE and SW: both contain f.

Let me solve. Let r(x)=1 if red. 
NE: r(a)+r(b)+r(c)=1.
NW: r(d)+r(e)+r(b)=1.
SE: r(f)+r(g)+r(a)=1.
SW: r(h)+r(f)+r(d)=1.

Case 1: r(b)=1. Then NE: r(a)=r(c)=0. NW: r(d)+r(e)=0 → r(d)=r(e)=0. SE: r(f)+r(g)+0=1 → one of f,g red. SW: r(h)+r(f)+0=1 → r(h)+r(f)=1.
- Subcase f red: then g=0 (SE: f=1 so g=0), and SW: r(h)+1=1→r(h)=0. So f red, others (a,c,d,e,g,h) white, b red. Reds near w: b and f. That's 2 reds among 8 neighbors, plus w white. So 2 reds witnessed... but we wanted w to witness 4 reds (one per cell). Here NE red=b, NW red=b (same!), SE red=f, SW red=f (same). So w witnesses only 2 distinct reds (b and f), via 4 cells but 2 cells each share. So w witnesses 2 reds, not 4. Hmm, so the "4 cells private" doesn't mean 4 distinct reds.

Oh I see, my counting bound assumed each white witnesses ≤4 reds, but actually it could witness fewer distinct reds. The bound 3r ≤ 4w used "each white in ≤4 incidences" where incidences = (red, white) pairs with white in red's private cell. If two cells of w are private for the same red b, that's still 2 incidences? No — incidence is (p, w) where w is a corner of C_p. If C_b (private cell of b) — but b has only one chosen private cell. So even if multiple cells through w are "private for b", b only picks one private cell. So the incidence (b, w) is counted once. So the number of incidences for w = number of distinct reds p such that w ∈ C_p (w is a corner of p's chosen private cell). 

So my bound 3r ≤ 4w requires each white to be a corner of ≤4 chosen private cells, and chosen private cells are distinct (one per red). A white w is a corner of 4 cells total, and each cell is the chosen private cell of at most one red. So w is in ≤4 chosen private cells → ≤4 incidences. So bound holds. But to achieve equality, w must be a corner of 4 distinct chosen private cells, i.e., 4 distinct reds each having a private cell through w. From the case analysis, case 1 gave only 2 distinct reds near w with all 4 cells private. So equality not achievable in that case. Let me find a case with 4 distinct reds.

Case 2: r(b)=0. Then NE: r(a)+r(c)=1. NW: r(d)+r(e)=1. 
Subcase 2a: r(a)=1, r(c)=0. SE: r(f)+r(g)+1=1→r(f)=r(g)=0. NW: r(d)+r(e)=1. SW: r(h)+r(f)+r(d)=r(h)+0+r(d)=1.
- 2a-i: r(d)=1,r(e)=0. SW: r(h)+1=1→r(h)=0. Reds: a,d. NE red=a, NW red=d, SE red=a (same as NE), SW red=d (same). Only 2 distinct. 
- 2a-ii: r(d)=0,r(e)=1. SW: r(h)+0=1→r(h)=1. Reds: a,e,h. NE=a, NW=e, SE=a, SW=h. Distinct reds witnessed: a,e,h = 3. 
Subcase 2b: r(a)=0,r(c)=1. SE: r(f)+r(g)+0=1. NW: r(d)+r(e)=1. SW: r(h)+r(f)+r(d)=1.
- 2b-i: r(d)=1,r(e)=0. SE: r(f)+r(g)=1. SW: r(h)+r(f)+1=1→r(h)+r(f)=0→r(h)=0,r(f)=0. Then SE: r(g)=1. Reds: c,d,g. NE=c,NW=d,SE=g,SW=d. Distinct: c,d,g=3.
- 2b-ii: r(d)=0,r(e)=1. SE: r(f)+r(g)=1. SW: r(h)+r(f)+0=1→r(h)+r(f)=1.
  - r(f)=1,r(g)=0: SW r(h)+1=1→r(h)=0. Reds: c,e,f. NE=c,NW=e,SE=f,SW=f. Distinct: c,e,f=3.
  - r(f)=0,r(g)=1: SW r(h)=1. Reds: c,e,g,h. NE=c,NW=e,SE=g,SW=h. Distinct: 4! 

So case 2b-ii with r(f)=0,r(g)=1: reds at c=(1,1), e=(-1,1), g=(1,-1), h=(-1,-1). I.e., the 4 diagonal neighbors of w are red, the 4 axis neighbors (a,b,d,f) are white. And w white. So around w: w and its 4 axis-neighbors white, 4 diagonal neighbors red. Then all 4 cells through w are private (each has exactly 1 red = the diagonal corner). And w witnesses 4 distinct reds. 

So the ideal local pattern: white points form a "plus" shape, and the 4 diagonals are red. This is like: white at center and 4 axis neighbors, red at 4 diagonals.

This suggests a pattern where whites are arranged so that each white has its 4 axis-neighbors also white and 4 diagonal neighbors red. But that's a strong condition. Let me think globally.

If white points are such that whenever (i,j) is white, (i±1,j) and (i,j±1) are white too — that means white set is closed under axis-adjacency, i.e., white set is a union of "axis-connected" components, and within, all axis-neighbors white. But then white points would form full rows/columns blocks, likely creating 2×2 all-white blocks (violating condition a). Hmm, conflict.

Wait, the local pattern requires for white w: its 4 axis neighbors white. But if w=(0,0) white requires (1,0) white, and (1,0) white requires (2,0) white, etc. → entire row white. Then 2×2 blocks in that row all white → violates (a). Contradiction. So we can't have all whites be "ideal" (witnessing 4). 

So the bound 3r ≤ 4w is not achievable. We need a better analysis. The slack means actual min w is larger, so r smaller.

Hmm. So the ideal pattern is impossible globally. Let me reconsider.

OK this is a hard combinatorial optimization. Let me think differently.

Let me reconsider the problem. Maybe think in terms of rows and a transfer / pattern.

Let me reconsider condition (b): every red point p has a cell with the other 3 corners white. So every red point is "exposed" — there's a 2×2 block where it's the lone red.

And condition (a): no 2×2 block all white.

We want to minimize whites w (maximize reds r=10000-w).

Let me think about it as: place white points to "cover" all red points (each red needs a cell of 3 whites around it) while not forming any all-white 2×2.

Equivalently think of red points: each red must have a "witness cell" (3 whites). 

Let me think about a periodic tiling construction and compute its density, then try to match an upper bound.

Idea: Use a pattern with period dividing 100. Since 100 = 4·25, periods like 4, 5, 10, 20, 25, 50 work.

Let me think about a stripe/column pattern. Suppose we make certain columns white. If column j is all white, then 2×2 blocks within column j and j+1... a 2×2 block uses columns j,j+1. If both columns j,j+1 all white → all-white block. So can't have two consecutive all-white columns. So white columns must be non-consecutive. But also a single all-white column: 2×2 block at columns j,j+1 where j white column, j+1 not: block has 2 points in col j (white) and 2 in col j+1. If col j+1 has some red, fine. So all-white columns isolated is OK for condition (a) as long as no two consecutive white columns... but actually even one all-white column: the 2×2 blocks spanning (col j, col j+1) and (col j-1, col j) — these have 2 white (from col j) and 2 from neighbor column. Not all white if neighbor has red in those rows. If neighbor column is all red, then those blocks have 2 white + 2 red, fine.

But condition (b): red points in neighbor columns need witness cells with 3 whites. If col j is all white and col j+1 all red: a red point (j+1, y) needs a cell with 3 white corners. Cells containing (j+1,y): columns (j,j+1) or (j+1,j+2). Using cell (j,j+1) at rows (y-1,y) or (y,y+1): corners (j,y-1),(j+1,y-1),(j,y),(j+1,y) — wait let me index cell C(i,j) = {(i,j),(i+1,j),(i,j+1),(i+1,j+1)} where i is column, j is row. Let me use (col, row) = (x,y). Cell C(x,y) = {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}.

Red point (j+1, y). Cells containing it: C(j,y) [as (x+1,y) part? C(j,y)={(j,y),(j+1,y),(j,y+1),(j+1,y+1)} contains (j+1,y)], C(j,y-1)={(j,y-1),(j+1,y-1),(j,y),(j+1,y)} contains (j+1,y), C(j+1,y)={(j+1,y),(j+2,y),(j+1,y+1),(j+2,y+1)}, C(j+1,y-1)={(j+1,y-1),(j+2,y-1),(j+1,y),(j+2,y)}.

For witness with 3 whites: use C(j,y) = {(j,y),(j+1,y),(j,y+1),(j+1,y+1)}: (j+1,y) red, need (j,y),(j,y+1),(j+1,y+1) white. (j,y),(j,y+1) are in col j (all white) ✓. (j+1,y+1) is in col j+1 (all red) ✗. So not all white. Try C(j,y-1)={(j,y-1),(j+1,y-1),(j,y),(j+1,y)}: (j+1,y) red, others (j,y-1),(j+1,y-1),(j,y). (j,y-1),(j,y) white ✓, (j+1,y-1) red ✗. So can't get 3 whites from col-j cells because the 4th corner is in col j+1 (red). 

So a single all-white column adjacent to all-red column doesn't give witnesses. We need whites in col j+1 too near each red. So pure column stripes won't work for condition (b).

This is quite intricate. Let me think about small periodic patterns computationally in my head... hard. 

Let me reconsider — maybe approach via known result. This problem: "critical coloring" of grid, maximal minimal. This resembles an IMO/olympiad problem. The answer might be 7500 or 5000 or some clean fraction.

Let me reconsider the counting bound differently to get a cleaner number. 

Alternative bound: Consider rows. For each red point, it needs a witness cell. Let me think about per-row contributions.

Hmm, let me think about the witness cell of red point p=(x,y). The witness cell is one of 4 cells around p, with the other 3 corners white. The 3 white corners are in specific positions. Let me categorize by which cell:
- Cell C(x,y) [p is bottom-left of cell]: whites at (x+1,y),(x,y+1),(x+1,y+1). [p=(x,y) red]
- Cell C(x-1,y) [p is bottom-right]: whites at (x-1,y),(x-1,y+1),(x,y+1).
- Cell C(x,y-1) [p is top-left]: whites at (x+1,y-1),(x,y),(x+1,y)... wait C(x,y-1)={(x,y-1),(x+1,y-1),(x,y),(x+1,y)}, p=(x,y) is in it, others (x,y-1),(x+1,y-1),(x+1,y).
- Cell C(x-1,y-1) [p is top-right]: {(x-1,y-1),(x,y-1),(x-1,y),(x,y)}, p=(x,y), others (x-1,y-1),(x,y-1),(x-1,y).

So each red point's witness cell has 3 white corners forming an "L" shape adjacent to p.

Now let me think about a cleaner global bound. 

Consider the white points and the "L-shapes" they form. Each witness cell is a 2×2 with 1 red + 3 white (an L of whites + 1 red). 

Let me count the number of "L-triominoes of white" — actually each witness cell is a 2×2 block with exactly 3 whites and 1 red. Let me call such a block a "W3-block" (3 whites). Condition (b): every red is in some W3-block (as the lone red). Condition (a): no W4-block (4 whites) and actually no block with 4 whites; blocks can have 1,2,3 whites (≥1 red) — wait ≥1 red means ≤3 whites. So every block has 1,2, or 3 whites (0 whites = all red, allowed since ≥1 red ✓; 4 whites forbidden). And every red is the lone red of some block (a block with exactly 3 whites = 1 red, and that red is p).

So: every block has ≤3 whites (i.e., ≥1 red). Every red point is the unique red of at least one block.

We want to minimize total whites.

Let me think about it as: whites form a set with no 2×2 full block, and every red has a "private" block (block where it's the only red, i.e., the other 3 are white).

Minimize whites. Equivalently maximize reds such that every red has a private block and no block is all-red-... no, blocks can be all red (0 whites) — that's fine, ≥1 red. Wait but if a block is all red (4 reds), that's allowed. But then those reds need private blocks elsewhere.

Hmm OK. Let me think about lower bound on whites via a different counting.

Each red needs a private block (3 whites). Consider the private blocks chosen, one per red. These are 10000-w blocks (one per red), each a 2×2 with 3 whites + 1 red. Distinct blocks? A private block has exactly 1 red, so it's the private block of that unique red. So private blocks are automatically distinct (different reds → different blocks, since a block with 1 red is private for that red only; two reds can't share a private block). Wait, could two reds choose the same block as private? A block with exactly 1 red can only be private for that 1 red. So if red p1 and p2 both have private block B, then B has exactly 1 red, contradiction (it'd need to be both p1 and p2). So private blocks distinct. Good, r distinct private blocks, each with 3 whites.

Now count incidences (white point, private block containing it). Each private block has 3 whites → 3r incidences. Each white point is in 4 blocks total (the 4 cells containing it), so in ≤4 private blocks → ≤4 incidences. So 3r ≤ 4w. Same bound. r ≤ 4w/3, w ≥ 3r/4... with r+w=10000: 3r ≤ 4(10000-r) → 7r ≤ 40000 → r ≤ 5714.28 → r ≤ 5714.

We showed equality needs each white in 4 private blocks, requiring the local "plus" pattern which forces all-white rows → contradiction with no-W4. So strict inequality. So r ≤ 5713? Not necessarily; the bound r ≤ 5714 still holds, equality r=5714 needs near-tight. Let me see how much slack is forced.

Actually the bound r ≤ 5714 is from 7r ≤ 40000, r ≤ 5714.28. So r ≤ 5714 regardless. The question is whether 5714 is achievable or we need r ≤ 5713 or less. The local obstruction shows we can't have all whites saturated (4 incidences), but we might have most saturated and a few unsaturated, still achieving r=5714 if total incidences 3·5714=17142 ≤ 4w - (deficit). With w=4286, 4w=17144, deficit allowed ≤ 2. So only 2 incidences of deficit allowed — meaning almost all whites saturated (4 incidences) except total deficit 2. But saturated whites require the plus pattern locally (axis neighbors white), which cascades into all-white rows. So having ~4286 whites nearly all saturated is impossible. So r=5714 not achievable. The real max is lower.

I need a better bound capturing the cascade. Let me think.

Let me define a white point as "saturated" if it's in 4 private blocks (witnesses 4 reds). Saturated white requires its 4 axis-neighbors white (from case analysis: the only way to witness 4 distinct reds is the plus pattern with axis neighbors white and diagonal neighbors red). Wait, let me double-check that the only way to witness 4 is that pattern. From case analysis, 4 distinct reds witnessed required reds at the 4 diagonals and whites at 4 axis positions. But "witnessing 4 reds" means 4 private blocks through w, each with a distinct lone red. The lone reds are at the 4 diagonal positions, and the axis positions must be white (so that each cell through w has its 3 non-w corners = 2 axis + 1 diagonal, with the diagonal red and 2 axis white → exactly 1 red ✓). For this, axis neighbors of w must be white. So yes, saturated white ⟹ 4 axis neighbors white.

But the 4 axis neighbors being white doesn't require them saturated. However, if w is saturated, its axis neighbors are white. Now consider those axis neighbors — are they saturated? Not necessarily. But the issue: if (1,0) is white (axis neighbor of w=(0,0)), and (1,0) is also axis neighbor of (2,0) etc. The cascade: w saturated ⟹ (1,0) white. (1,0) white — for (1,0) to be saturated, need (2,0),(1,1),(1,-1),(0,0) white. (0,0) is white ✓. So (1,0) saturated needs (2,0) white etc. But (1,0) need not be saturated.

The real contradiction earlier: if ALL whites saturated, then white set closed under axis adjacency → whole rows white → W4 blocks. But we don't need all whites saturated; we need most. Let me quantify: deficit D = 4w - 3r (total missing incidences). For r=5714, w=4286: D = 4·4286 - 3·5714 = 17144 - 17142 = 2. So D=2, meaning only 2 missing incidences total. So all but at most 2 whites are saturated (each saturated white has 4 incidences; unsaturated have fewer; total deficit 2 means e.g. one white with 2 incidences, or two whites with 3). So ≥4284 whites saturated (roughly). 4284 saturated whites, each forcing 4 axis neighbors white. 

Now, saturated whites forcing axis neighbors white: consider the graph on white points where edges are axis-adjacency. Saturated white w has all 4 axis neighbors white, so w has degree 4 in this white-axis-graph (within the white set, considering the 4 axis neighbors all present). Actually it means w is "interior" of white set in axis directions.

If 4284 whites are saturated (interior, all 4 axis neighbors white), then the white set has 4284 interior points. The white set total 4286. So only 2 white points are "boundary" (not saturated, missing an axis neighbor that's red). 

A set of 4286 points on 100×100 torus with 4284 having all 4 axis-neighbors in the set: that means the white set is almost a union of full rows and columns... Let me think. If a white point has all axis neighbors white, then its entire row and column (through propagation) ... no, propagation: w=(0,0) saturated → (1,0) white. Is (1,0) saturated? If yes → (2,0) white, etc. But (1,0) might be one of the 2 unsaturated. With only 2 unsaturated, the propagation can only be "blocked" at 2 points. So along the row through w, the whites extend until hitting an unsaturated point. With 4284 saturated forming large connected axis-components, and only 2 unsaturated to bound them.

A saturated white's axis neighbors are white; those neighbors, if saturated, continue. So a maximal axis-connected run of saturated whites: starts and ends at unsaturated whites (or wraps around torus). With only 2 unsaturated whites total, there are at most 2 "endpoints", so essentially one long run that wraps the torus, or the white set is almost entire rows/columns.

If white set contains a full row (all 100 points in a row white) — then 2×2 blocks within that row and adjacent row: block at (x,y),(x+1,y),(x,y+1),(x+1,y+1) with row y all white: (x,y),(x+1,y) white; need (x,y+1),(x+1,y+1) not both white. If row y+1 also has whites... but more directly, a full white row y: consider block with rows y and y+1: 2 points in row y (white) + 2 in row y+1. For no W4, row y+1 must have at least one red in every consecutive pair... i.e., row y+1 can't have two consecutive whites. Similarly row y-1. 

But more importantly, if white set is ~4286 points mostly in full rows: say k full white rows = 100k whites. 100k ≈ 4286 → k≈42.86, not integer. So maybe 42 full rows (4200 whites) + 86 more. But full white rows: consecutive full white rows create W4 (block entirely in two consecutive white rows). So full white rows must be non-consecutive (separated by ≥1 non-full row). With 42 full white rows among 100 rows, non-consecutive: possible (alternating). 42 white rows + 58 non-white rows, but 42 white rows non-consecutive needs ≥41 gaps, 42+41=83≤100 ok, or with wrap. Actually 42 non-consecutive in cycle of 100: need 42 ≤ 50, ok.

But wait, if row y is full white, then rows y-1 and y+1 must have no two consecutive whites (to avoid W4 with row y). And red points in rows y-1, y+1 need witness blocks. A red point (x, y+1) needs a block with 3 whites. Blocks containing (x,y+1): using rows y,y+1: block {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}: (x,y),(x+1,y) white (row y full), (x,y+1) red, (x+1,y+1) = ? For 3 whites need (x+1,y+1) white. So (x+1,y+1) white. So red (x,y+1) needs (x+1,y+1) white (or use other blocks). Similarly using block {(x-1,y),(x,y),(x-1,y+1),(x,y+1)}: (x-1,y),(x,y) white, (x,y+1) red, need (x-1,y+1) white. So red (x,y+1) needs an adjacent white in row y+1 (left or right) — but row y+1 can't have two consecutive whites (to avoid W4 with row y)! Contradiction: red (x,y+1) needs (x±1,y+1) white, meaning two consecutive whites in row y+1 ((x,y+1) is red, but (x+1,y+1) white and ... wait (x,y+1) red, (x+1,y+1) white — that's not two consecutive whites, that's red then white). Hmm let me redo. Row y+1: (x,y+1) is red. For its witness via block with row y, need (x+1,y+1) white OR (x-1,y+1) white. So at least one neighbor of (x,y+1) in row y+1 is white. That's fine, doesn't create two consecutive whites by itself. But consider the red points in row y+1: each red needs a white neighbor in row y+1 (or witness via row y+2 blocks). 

Hmm, this is getting complicated but maybe full-row approach can work. But 4286 isn't divisible nicely and the deficit analysis says r=5714 needs D=2, extremely tight, basically requiring near-perfect saturation which seems impossible given the row constraints. Let me just try to find the true optimum via a cleaner argument or construction.

Let me reconsider. Maybe the answer is a clean number and my bound is loose. Let me look for a better upper bound.

New idea for upper bound: Consider the witness blocks (private blocks), r of them, each a 2×2 with 3W+1R. Look at the red point in each witness block and the "missing corner" position. Actually, let me think about pairs of adjacent witness blocks or overlaps.

Alternative: think about each 2×2 block's white count. Let a_k = number of blocks with exactly k whites (k=0,1,2,3; k=4 forbidden). Sum k·a_k = total (block, white) incidences = 4w (each white in 4 blocks). Sum a_k = 10000 (total blocks). Witness blocks are those with k=3 (3 whites, 1 red): a_3 ≥ r (each red needs at least one k=3 block, and each k=3 block is witness for its unique red, so a_3 = number of reds that have ≥1... no, a_3 = number of blocks with 3 whites; each such block has 1 red and is a witness for that red; a red could have multiple witness blocks, so a_3 ≥ r? No: a_3 = number of 3-white blocks. Each red needs ≥1 such block containing it. A 3-white block contains exactly 1 red. So the map from 3-white blocks to reds (the unique red) is surjective onto the set of reds (every red has ≥1). So a_3 ≥ r. 

So a_3 ≥ r. And 4w = a_1 + 2a_2 + 3a_3. And a_0+a_1+a_2+a_3 = 10000. We want to maximize r = 10000 - w, minimize w. 

We have a_3 ≥ r = 10000 - w. And 4w = a_1 + 2a_2 + 3a_3 ≥ 3a_3 ≥ 3(10000-w) → 4w ≥ 30000 - 3w → 7w ≥ 30000 → w ≥ 4285.7 → w ≥ 4286, r ≤ 5714. Same bound. The bound 4w ≥ 3a_3 uses a_1+2a_2 ≥ 0. To tighten, need a_1 + 2a_2 > 0 forced, i.e., need to show there must be blocks with 1 or 2 whites (not all blocks 0 or 3 whites). 

If a_1 = a_2 = 0: all blocks are 0-white (all red) or 3-white. Then 4w = 3a_3, and a_0 + a_3 = 10000. Also a_3 ≥ r=10000-w. From 4w=3a_3: a_3 = 4w/3. And a_3 ≥ 10000 - w: 4w/3 ≥ 10000 - w → 7w/3 ≥ 10000 → w ≥ 4285.7. And a_3 = 4w/3 must be integer, w divisible by 3. w=4286: 4·4286/3 = 5714.67 not integer. w=4287: a_3=5716, a_0=10000-5716=4284, r=10000-4287=5713. Check a_3 ≥ r: 5716 ≥ 5713 ✓. So with a_1=a_2=0, w=4287, r=5713. Hmm so this sub-case allows r=5713. But is a_1=a_2=0 achievable (all blocks either all-red or 3-white)? That's a strong structural condition. Let me check if possible.

All blocks 0 or 3 whites. A block with 3 whites + 1 red. Adjacent blocks share edges. Let me see if such a configuration exists on torus. 

Consider two horizontally adjacent blocks C(x,y) and C(x+1,y). C(x,y) = {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}, C(x+1,y) = {(x+1,y),(x+2,y),(x+1,y+1),(x+2,y+1)}. They share edge {(x+1,y),(x+1,y+1)}. If C(x,y) is 3W1R and C(x+1,y) is 3W1R: the shared edge has 2 points; in C(x,y) the red is one of 4 corners; in C(x+1,y) red is one of its 4 corners. The shared points (x+1,y),(x+1,y+1): their colors fixed. 

This is a tiling constraint. Let me try to construct: maybe a pattern where each block has exactly 3 whites and 1 red, and reds form a pattern. But a_0 > 0 also (4284 all-red blocks). Mixed.

Hmm, let me just try to see if r=5713 or 5714 achievable, or find the real answer. This is getting deep. Let me try a concrete periodic construction and compute.

Let me try period-7 or period related to 7 since 7 appears. 100 = 7·14 + 2. Not divisible by 7. Hmm. The bound involves 7. 10000 mod 7 = 10000 - 7·1428 = 10000-9996=4. So 10000 ≡ 4 mod 7. r ≤ floor(40000/7) = 5714 (since 40000 = 7·5714 + 2). 

For a clean construction maybe period 5 or 10. Let me try to find a pattern with a certain white density and verify conditions, then match bound.

Let me think about a "staircase" white pattern. 

Actually, let me reconsider the problem. Let me reconsider whether the answer might be 5000 or 7500 etc. Let me get a better upper bound using a different method: line/row arguments.

Row argument: Consider a fixed row y. Let w_y = whites in row y. Condition (a) no W4: for consecutive rows y, y+1, no two consecutive columns both white in both rows. I.e., the set of columns where both row y and row y+1 are white has no two consecutive. 

Condition (b): every red (x,y) needs a witness block. 

Let me think about witness blocks and rows. A witness block for red (x,y) is a 2×2 block (rows y-1,y or y,y+1) with 3 whites. The 3 whites are in 2 consecutive rows. 

Hmm. Let me think about counting whites per row and the witness requirement per row.

Let me consider the red points in row y. Each needs a witness block, which is either in rows (y-1,y) or rows (y,y+1). A witness block in rows (y,y+1) with red (x,y): block {(x,y),(x+1,y),(x,y+1),(x+1,y+1)} (red at (x,y)) needs (x+1,y),(x,y+1),(x+1,y+1) white; or block {(x-1,y),(x,y),(x-1,y+1),(x,y+1)} (red at (x,y)) needs (x-1,y),(x-1,y+1),(x,y+1) white. So a witness for (x,y) in rows (y,y+1) requires (x,y)'s horizontal neighbor in row y white AND the two corresponding points in row y+1 white. Specifically pattern: row y: ...W R... (white at x-1 or x+1, red at x), row y+1: two consecutive whites at x-1,x or x,x+1.

So roughly, to witness reds in row y using row y+1, we need whites in row y+1 and adjacent whites in row y.

This is complex. Let me just try to guess the answer is 5714 and try to construct, or reconsider.

Actually, let me reconsider the possibility that the intended answer is 7500. Let me get an upper bound of 7500 via a simple argument and a matching construction.

Simple construction giving 7500: Color 3/4 of points red? Let me think. Suppose whites are at positions (i,j) with i≡0 mod 2 and j≡0 mod 2, i.e., a 2×2 sublattice (every other row, every other column). That's 50×50 = 2500 whites, 7500 reds. Check condition (a): no W4 block. A 2×2 block {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}: whites are those with both coords even. Among 4 corners, how many have both even? Depends on parity of x,y. If x,y both even: corners (x,y)✓,(x+1,y)✗,(x,y+1)✗,(x+1,y+1)✗ → 1 white. If x odd, y even: (x,y)✗,(x+1,y)✓,(x,y+1)✗,(x+1,y+1)✗→1. Etc. Always exactly 1 white. So no W4 (only 1 white per block). Condition (a) ✓ (every block has 3 reds ≥1). 

Condition (b): every red point needs a witness block (3 whites). But each block has only 1 white (and 3 reds). So no block has 3 whites! So no red has a witness. Condition (b) fails. So this is critical but NOT minimal (removing a red: the block had 3 reds, now 2, still ≥1; but does removing break criticality? Need some block to become all white. With 1 white per block, removing reds never makes a block all white unless we remove 3 reds from a block. So removing 1 red: all blocks still have ≥1 red (the block containing the removed red had 3→2, others unaffected). So not minimal. Fails.) 

So 7500 with that pattern is critical but not minimal. We need minimality.

To get minimality, we need blocks with 3 whites (witness blocks). So whites must cluster into L-shapes. 

Let me think about a construction with whites forming L-shapes (3 of a 2×2) tiled. 

Construction: tile the plane with 2×2 blocks, each block having 3 whites and 1 red. But adjacent blocks share edges, so can't independently set. Let me try: pattern on 2×2 fundamental domain repeated. 2×2 domain {(0,0),(1,0),(0,1),(1,1)} with 3W1R, say red at (0,0), whites at (1,0),(0,1),(1,1). Repeat with period 2. Then every 2×2 block aligned with the grid... let me check all blocks. Block C(x,y) for various x,y parity:
- x,y even: C(0,0)={(0,0)R,(1,0)W,(0,1)W,(1,1)W}: 3W1R ✓ witness for (0,0).
- x even, y odd: C(0,1)={(0,1)W,(1,1)W,(0,2),(1,2)}. (0,2): 2 even→ (0,0) pattern → R. (1,2): (1,0) pattern → W. So {(0,1)W,(1,1)W,(0,2)R,(1,2)W}: 3W1R, red at (0,2). ✓
- x odd, y even: C(1,0)={(1,0)W,(2,0),(1,1)W,(2,1)}. (2,0)=(0,0)pattern→R, (2,1)=(0,1)pattern→W. So {W,R,W,W}: 3W1R red (2,0). ✓
- x odd,y odd: C(1,1)={(1,1)W,(2,1)W,(1,2)W,(2,2)}. (2,2)=(0,0)→R. So {W,W,W,R}: 3W1R. ✓

So every block has exactly 3 whites and 1 red! So a_3 = 10000, a_0=a_1=a_2=0. Whites = 3/4·10000 = 7500, reds = 2500. Every red has a witness (its block). Condition (a): every block 3W1R, no W4 ✓. Minimality: every red is the unique red of its block, so removing it makes that block all white → criticality lost ✓. So this is minimal critical with r = 2500. But we want MAXIMUM reds, so 2500 is a lower bound (construction), not the answer. We want to maximize reds = minimize whites. 7500 whites here is a lot. We want fewer whites.

So the 3W1R tiling gives r=2500 (min reds, max whites among minimal critical). We want the opposite extreme: max reds (min whites) minimal critical.

So we want as few whites as possible while every red has a witness block (3 whites) and no W4.

The counting bound says w ≥ 4286 (r ≤ 5714). Let me try to construct near that.

We want whites sparse but each red adjacent to a 3-white block. With few whites, whites must be arranged so that each white participates in many witness blocks (up to 4), and reds each have a witness. 

From the local analysis, a white witnesses 4 reds only in the "plus" pattern (axis neighbors white, diagonal red). But that forces axis neighbors white, cascading. So pure 4-witness whites cascade into rows. Let me consider whites witnessing 3 or 2 reds as well, more flexible.

Let me reconsider: maybe the optimum uses whites witnessing 3 reds each (D = 4w - 3r, with each white witnessing 3 → 3r = 3w → r = w, r = 5000). Hmm that gives 5000. Or mix.

Let me reconsider the case analysis for how many distinct reds a white can witness and the required neighbor config:

- 4 reds: axis neighbors white, diagonal red (plus pattern). Forces axis neighbors white.
- 3 reds: cases 2a-ii, 2b-i, 2b-ii(r(f)=1): let me recheck. 2a-ii: r(b)=0,r(a)=1,r(c)=0,r(d)=0,r(e)=1,r(f)=0,r(g)=0,r(h)=1. So reds at a=(1,0), e=(-1,1), h=(-1,-1). Whites at b,c,d,f,g and w. Let me verify all 4 cells private:
  NE {a,b,c}: a red, b,c white → 1 red ✓ (witness a).
  NW {d,e,b}: e red, d,b white → 1 red ✓ (witness e).
  SE {f,g,a}: a red, f,g white → 1 red ✓ (witness a again, same red).
  SW {h,f,d}: h red, f,d white → 1 red ✓ (witness h).
  So distinct reds witnessed: a, e, h = 3. The SE cell witnesses a (already witnessed by NE). So w is in 4 private-eligible cells but only 3 distinct reds. For incidence counting (chosen private blocks), w would be chosen by 3 reds (a,e,h) at most (a chooses one of NE/SE). So w contributes ≤3 incidences. Config: a=(1,0) red [east], e=(-1,1) red [NW diagonal], h=(-1,-1) red [SW diagonal]. Whites: w, b=(0,1) [north], c=(1,1)[NE diag], d=(-1,0)[west], f=(0,-1)[south], g=(1,-1)[SE diag]. So whites: w, north, NE-diag, west, south, SE-diag. Reds: east, NW-diag, SW-diag. 

This doesn't force a full cascade. Let me see what it forces: w white, and north (0,1) white, west (-1,0) white, south (0,-1) white, plus diagonals NE (1,1) white, SE (1,-1) white. Reds: east (1,0), NW(-1,1), SW(-1,-1). So w has 3 axis neighbors white (N,W,S) and 1 axis neighbor red (E). And 2 diagonals white (NE,SE, the ones adjacent to E) and 2 diagonals red (NW,SW). Interesting.

So a white witnessing 3 reds has 3 axis neighbors white and 1 axis neighbor red, with the 2 diagonals adjacent to the red axis neighbor being white, and the 2 diagonals adjacent to... being red. 

This still forces 3 axis neighbors white, partial cascade.

- 2 reds: case 1 (b red, f red) or 2a-i (a,d red). Case 1: r(b)=1, r(a)=r(c)=r(d)=r(e)=0, r(f)=1, r(g)=0, r(h)=0. Reds: b=(0,1)[north], f=(0,-1)[south]. Whites: w, a,c,d,e,g,h. So axis neighbors E,W white (a,d), N,S red (b,f). Diagonals all white (c,e,g,h). w witnesses 2 reds (N and S). Cells: NE{a,b,c}: b red ✓. NW{d,e,b}: b red ✓. SE{f,g,a}: f red ✓. SW{h,f,d}: f red ✓. So 4 cells private but 2 distinct reds. Config: N,S red; E,W, all diagonals white. Forces E,W axis neighbors white and all 4 diagonals white. That's a lot of whites around w (6 whites: E,W,4 diag + w itself). 

Case 2a-i: r(a)=1,r(c)=0,r(d)=1,r(e)=0,r(f)=0,r(g)=0,r(h)=0, r(b)=0. Reds a=(1,0)[E], d=(-1,0)[W]. Whites: w,b,c,e,f,g,h. So N,S axis white (b,f), E,W red, all diagonals white. Symmetric to case 1 rotated. w witnesses 2 reds (E,W). Forces N,S and all diagonals white.

So witnessing 2 reds: the two reds are opposite axis neighbors, and the other 2 axis + 4 diagonals white (6 whites around). Very white-heavy locally.

- 1 red: even more white-heavy.
- 0 reds: w in no private block.

So to minimize whites, we want whites witnessing as many reds as possible (4 ideal), but 4 forces full cascade (all axis neighbors white → rows). 3 forces 3 axis neighbors white. 2 forces 2 axis + 4 diag white.

The cascade issue: whites witnessing 4 need all 4 axis neighbors white. If we have a region of whites all witnessing 4, it's axis-connected and extends. On a torus, a maximal axis-connected white component where every member witnesses 4 must be a union of full rows and full columns (since axis-connected and closed under axis neighbors means if (0,0) in it, (1,0) in it, (2,0) in it, ... entire row 0; and (0,1),(0,-1)... entire column 0; and then their rows...). Actually closure under all 4 axis neighbors means: component is closed under ±x and ±y steps, so it's a Cartesian product of a set of rows and set of columns? No: if (0,0) in C and C closed under axis neighbors, then all (x,0) in C (row 0) and all (0,y) in C (col 0), and then (x,0) in C → (x,y) all? (x,0) closed under y → (x,1),(x,2)... so column x fully in C. So C = entire torus. So the only nonempty axis-closed subset of the torus is the whole torus. So if any white witnesses 4 (needs all 4 axis neighbors white) and those neighbors also witness 4 (need their axis neighbors white)... but they need not witness 4. The cascade only continues if the neighbors also witness 4. 

So we can have isolated whites witnessing 4 as long as their axis neighbors are white but those neighbors witness fewer (so don't force further). Let me reconsider: white w witnesses 4 ⟹ axis neighbors white. Those axis neighbors (say (1,0)) are white; (1,0) might witness only 2 or 3, not forcing (2,0) white. So cascade stops. Good. So we can have whites witnessing 4 without full rows, as long as their axis neighbors are "low-witness" whites.

But the axis neighbors being white and low-witness: e.g., (1,0) white witnessing 2 (case 1 or 2a-i). Case 2a-i for (1,0): needs N=(1,1), S=(1,-1) white and E=(2,0),W=(0,0) red, diagonals (2,1),(2,-1),(0,1),(0,-1) white. But (0,0)=w is white, not red! Contradiction (case 2a-i needs W=(0,0) red). Case 1 for (1,0): needs E=(2,0),W=(0,0) white, N=(1,1),S=(1,-1) red, diagonals white. (0,0)=w white ✓ (W white). So (1,0) witnessing 2 via case 1: E=(2,0) white, W=(0,0) white, N=(1,1) red, S=(1,-1) red, diagonals (2,1),(2,-1),(0,1),(0,-1) white. But w=(0,0) witnesses 4 requires (0,1) red (diagonal of w? no: w's diagonals are (1,1),(−1,1),(1,−1),(−1,−1); w witnessing 4 needs diagonals red, i.e., (1,1) red ✓ (matches (1,0)'s N red), (1,-1) red ✓ (matches (1,0)'s S red), (-1,1) red, (-1,-1) red. And (1,0)'s diagonals (0,1),(0,-1) white — but w witnessing 4 needs (0,1) and (0,-1) white (axis neighbors of w) ✓. And (2,1),(2,-1) white (from (1,0) case1). And (2,0) white (from (1,0) case1 E). 

So combining: w=(0,0) witnesses 4, (1,0) witnesses 2 (case1). Let me list colors so far:
- w=(0,0): W
- w's axis: (1,0)W, (-1,0)W, (0,1)W, (0,-1)W
- w's diagonals: (1,1)R, (-1,1)R, (1,-1)R, (-1,-1)R
- (1,0) case1: E=(2,0)W, diagonals (2,1)W, (2,-1)W, (0,1)W✓, (0,-1)W✓. N=(1,1)R✓, S=(1,-1)R✓.
So new: (2,0)W, (2,1)W, (2,-1)W.

Now (0,1) is white (axis neighbor of w). What does (0,1) witness? Its neighbors: N=(0,2), S=(0,0)=w W, E=(1,1)R, W=(-1,1)R. For (0,1) to witness reds, consider its cells. (0,1) is white. Cells through (0,1): 
- {(0,1),(1,1),(0,2),(1,2)}: (1,1)R, need (0,2),(1,2) for count.
- {(-1,1),(0,1),(-1,2),(0,2)}: (-1,1)R.
- {(0,0),(1,0),(0,1),(1,1)}: = w's NE cell, (1,1)R, (0,0)W,(1,0)W → 1 red (1,1). private for (1,1) ✓. So (0,1) witnesses (1,1).
- {(-1,0),(0,0),(-1,1),(0,1)}: w's NW cell, (-1,1)R, (-1,0)W,(0,0)W → 1 red (-1,1). private ✓. witnesses (-1,1).
So (0,1) witnesses at least (1,1) and (-1,1) via w's cells. Plus possibly more via (0,2),(1,2),(-1,2). 

This is getting complicated but seems consistent. The pattern might extend. Let me try to see the global pattern emerging:

Whites: (0,0), (1,0), (-1,0), (0,1), (0,-1), (2,0), (2,1), (2,-1), ... and by symmetry (-2,0),(-2,1),(-2,-1)? Let me check (-1,0) similar to (1,0): (-1,0) white, by symmetry (reflect x) it'd be case1 with W=(-2,0) white, E=(0,0) white, N=(-1,1)R, S=(-1,-1)R, diagonals (-2,1)W,(-2,-1)W,(0,1)W,(0,-1)W. So (-2,0)W, (-2,1)W, (-2,-1)W.

And (0,-1) similar (reflect y): (0,-2)W, (1,-2)W, (-1,-2)W. (0,1): (0,2)W, (1,2)W, (-1,2)W.

So whites spreading. It seems like the pattern is growing into a diamond/cross shape. Let me see: whites at origin, plus axis arms extending, with reds at diagonals of origin and... Let me map out more.

Current whites: (0,0); (±1,0),(0,±1); (±2,0),(±2,±1),(0,±2),(±1,±2); 
Reds: (±1,±1) [the 4 diagonals of origin].

Now (2,0) is white (from (1,0)'s E). What does (2,0) witness? (2,0) neighbors: E=(3,0), W=(1,0)W, N=(2,1)W, S=(2,-1)W. (2,0) is in cells:
- {(1,0),(2,0),(1,1),(2,1)}: (1,1)R, (1,0)W,(2,0)W,(2,1)W → 1 red (1,1). private ✓. witnesses (1,1).
- {(2,0),(3,0),(2,1),(3,1)}: depends on (3,0),(3,1).
- {(1,-1),(2,-1),(1,0),(2,0)}: (1,-1)R,(2,-1)W,(1,0)W,(2,0)W → 1 red (1,-1). witnesses (1,-1).
- {(2,-1),(3,-1),(2,0),(3,0)}: depends.
So (2,0) witnesses (1,1) and (1,-1) at least. To witness more (via (3,0) cells), need (3,0) etc. If (2,0) is like (1,0) (case1, witnessing 2), then E=(3,0) white, N=(2,1) red?? But (2,1) is white (set above). Contradiction. So (2,0) can't be case1 (needs N=(2,1) red, but (2,1) white). 

Hmm so the pattern breaks. (2,0) has N=(2,1)W, S=(2,-1)W, W=(1,0)W. For (2,0) to witness reds, let me see which case. (2,0) with W=(1,0)W, N=(2,1)W, S=(2,-1)W. The cells:
- NW cell { (1,0),(2,0),(1,1),(2,1) }: (1,1)R → 1 red. witnesses (1,1).
- SW cell { (1,-1),(2,-1),(1,0),(2,0) }: (1,-1)R → 1 red. witnesses (1,-1).
- NE cell { (2,0),(3,0),(2,1),(3,1) }: (2,1)W, need (3,0),(3,1).
- SE cell { (2,-1),(3,-1),(2,0),(3,0) }: (2,-1)W, need (3,0),(3,-1).

For (2,0) to witness a 3rd red, need NE or SE cell to have exactly 1 red. NE: (2,0)W,(2,1)W, so red count among (3,0),(3,1) must be 1 for exactly 1 red total. SE: (2,0)W,(2,-1)W, red among (3,0),(3,-1) =1 for 1 red. 

If (3,0) red: NE has (3,0)R,(3,1)?; SE has (3,0)R,(3,-1)?. For NE exactly 1 red: (3,1) white. For SE exactly 1 red: (3,-1) white. Then NE witnesses (3,0), SE witnesses (3,0) (same). So (2,0) witnesses (1,1),(1,-1),(3,0) = 3 distinct. With (3,0) red, (3,1)W, (3,-1)W. 

So (2,0) witnesses 3 reds (like case 2a-ii or similar). Config: (2,0)W, W=(1,0)W, N=(2,1)W, S=(2,-1)W, E=(3,0)R, and (3,1)W,(3,-1)W. Reds near: (1,1),(1,-1),(3,0). This matches a "3-witness" config (3 axis neighbors white: W,N,S; 1 axis red: E; diagonals adjacent to E (3,1),(3,-1) white; diagonals adjacent to W... (1,1),(1,-1) red). Yes! Exactly case 2a-ii pattern (3 axis white, 1 axis red (E), the two diagonals next to E white, the two diagonals next to W red). 

So (2,0) is a 3-witness white. Good, consistent. So the pattern: along the +x axis, whites at (0,0)[4-wit], (1,0)[2-wit], (2,0)[3-wit], (3,0)[red!]. Wait (3,0) is red. So the arm extends (0,0)W,(1,0)W,(2,0)W,(3,0)R. And (3,0) red needs its own witness. 

(3,0) red: needs a cell with 3 whites. Cells through (3,0):
- {(2,0),(3,0),(2,1),(3,1)}: (2,0)W,(3,0)R,(2,1)W,(3,1)W → 3 whites! ✓ witness for (3,0). 
So (3,0) is witnessed by cell {(2,0),(3,0),(2,1),(3,1)} with whites (2,0),(2,1),(3,1). 

So the arm: ...W(2,0), R(3,0), and (3,0) witnessed. What about (3,0)'s other neighbors and continuing? (3,0) red, (3,1)W, (3,-1)W, (4,0)?. 

Now (3,1) white: neighbors N=(3,2), S=(3,0)R, E=(4,1), W=(2,1)W. (3,1) in cells:
- {(2,1),(3,1),(2,2),(3,2)}: (2,1)W, depends (2,2),(3,2).
- {(3,1),(4,1),(3,2),(4,2)}: depends.
- {(2,0),(3,0),(2,1),(3,1)}: (3,0)R, others W → 1 red. witnesses (3,0).
- {(3,0),(4,0),(3,1),(4,1)}: (3,0)R, (3,1)W, depends (4,0),(4,1).
So (3,1) witnesses (3,0) at least. 

This is getting very intricate. The pattern seems to be a growing cross/arrow. Let me step back and think about whether there's a clean periodic pattern achieving the bound, rather than this ad hoc growth.

Given the complexity, let me reconsider the problem scale: 100×100, answer likely a specific number. The bound r ≤ 5714. Let me hypothesize the answer is 5714 and check if a construction exists, or find the exact value.

Actually, let me reconsider. This is a known competition problem. Let me think about which competition. "Critical coloring" of 100×100 grid, 2×2 cells, maximal minimal. This might be from a Russian olympiad or similar. The answer... let me think.

Let me reconsider the counting bound and whether 5714 is achievable with a clever periodic construction of period 7 (since 7 is the key number, but 100 not divisible by 7). Hmm, 100 = 7·14+2. Period 7 won't tile 100 evenly. But the problem is on a torus of size 100, so the pattern must have period dividing 100. 7 doesn't divide 100. So a period-7 pattern won't work directly. So maybe the bound 5714 isn't achievable and the real answer relates to divisors of 100.

Divisors of 100: 1,2,4,5,10,20,25,50,100. Let me think about period-4 or period-5 patterns.

Let me reconsider. Maybe a cleaner bound gives a number related to 100's divisors. Let me reconsider the witness counting but per-row or using a smarter inequality.

Let me reconsider. Let me think about "each red needs a witness block; witness block has 3 whites in an L; the red is at the missing corner." Consider orienting each witness: the red is at one of 4 corners of its witness block. Assign each red an orientation (which corner it is in its chosen witness block): NE/NW/SE/SW (i.e., red is at bottom-left, bottom-right, top-left, top-right of the witness block). 

Now, a witness block with red at bottom-left (orientation NE, meaning red is SW corner, whites are the other 3 = N, E, NE): block {(x,y)R, (x+1,y)W, (x,y+1)W, (x+1,y+1)W}. The 3 whites form an L (top-right L). 

Let me count whites by "role". Hmm.

Alternative cleaner bound: Let me use a discharging or a per-2×2-block argument with the torus structure.

Actually, let me reconsider. Let me reconsider the possibility that the answer is 5000. Construction: checkerboard-ish? Let me think of whites as one color of a checkerboard: (i+j) even white. Then 5000 whites, 5000 reds. Every 2×2 block has 2 white 2 red. No W4 ✓ (only 2 whites). Condition (b): every red needs a witness block with 3 whites. But every block has exactly 2 whites. So no witness. Fails. 

So checkerboard fails minimality. Need blocks with 3 whites. So we need some blocks with 3 whites (witness) and the rest with ≥1 red. To have many reds, most blocks should have few whites (1 or 0), but we need enough 3-white blocks to witness all reds. Each 3-white block witnesses 1 red. So need ≥ r three-white blocks, i.e., a_3 ≥ r. And total white incidences 4w = a_1 + 2a_2 + 3a_3. To minimize w with a_3 ≥ r = 10000 - w: we want a_1, a_2 small and a_3 large. Max a_3 given 4w = a_1+2a_2+3a_3 and a_0+a_1+a_2+a_3=10000: to maximize a_3, set a_0=a_1=a_2=0 → a_3=10000, 4w=30000, w=7500, r=2500. That's the all-3-white construction (min reds). To minimize w (max reds), we want a_3 = r exactly (just enough witnesses) and a_1,a_2,a_0 absorbing the rest with few white incidences. With a_3 = r = 10000 - w: 4w = a_1 + 2a_2 + 3(10000 - w) → 7w = a_1 + 2a_2 + 30000. To minimize w, minimize a_1 + 2a_2. Minimum is 0 (a_1=a_2=0) → w = 30000/7 ≈ 4285.7 → w=4286 (ceil), r=5714, with a_1+2a_2 = 7·4286 - 30000 = 2. So a_1 + 2a_2 = 2, a_3 = 5714, a_0 = 10000 - a_1 - a_2 - 5714. If a_2=1,a_1=0: a_0=5714-... 10000-1-5714=4285. If a_1=2: a_0=10000-2-5714=4284. So almost all blocks are 0-white (all red) or 3-white, with just 1 or 2 blocks of 1 or 2 whites. 

So the optimal structure (if achievable): almost all blocks either all-red (0 white) or 3-white (witness), with exactly r=5714 three-white blocks and 4285 or 4284 all-red blocks, plus 1-2 exceptional blocks. And a_3 = r means every red has exactly one witness block (no red has 2), and every 3-white block witnesses its red (surjective bijection). 

Now the question: can we tile the 100×100 torus with 0-white and 3-white blocks (each block all-red or 3W1R) such that it's consistent (adjacent blocks agree on shared edges) and the red/white assignment is a valid coloring? With 5714 blocks of 3W1R and 4286 blocks of 0W (all red), and 4286 white points total.

Wait, white points: each 3-white block has 3 whites, but whites shared between blocks. Total whites w=4286. Total white incidences = 3·5714 + 0·4286 = 17142 = 4·4286 - 2 = 17144 - 2. So deficit 2: two white incidences "missing" meaning... 4w = 17144 but a_1+2a_2+3a_3 = 0+0+3·5714=17142. So 4w - (sum) = 2. But 4w must equal sum of incidences exactly! 4w = a_1 + 2a_2 + 3a_3 + 4a_4 but a_4=0. So 4w = a_1 + 2a_2 + 3a_3 exactly. With w=4286: 4w=17144. a_3=5714: 3a_3=17142. So a_1+2a_2 = 2. So we need a_1+2a_2=2 exactly. So either a_2=1 (one 2-white block) or a_1=2 (two 1-white blocks) or a_1=1,a_2=... no a_1+2a_2=2: (a_1=2,a_2=0) or (a_1=0,a_2=1). And a_0 = 10000 - a_1 - a_2 - 5714. For (a_1=2,a_2=0): a_0 = 4284. For (a_1=0,a_2=1): a_0=4285.

So the optimal coloring (r=5714) would have all blocks 0- or 3-white except 1 or 2 exceptional blocks. Is such a near-perfect tiling possible on 100×100 torus?

The constraint that adjacent blocks share an edge and must agree: Let me think about what 0-white and 3-white blocks look like and adjacency. A 0-white block = all 4 red. A 3-white block = 3W1R (red at one corner). 

Two adjacent 3-white blocks sharing an edge: e.g., block A={(0,0),(1,0),(0,1),(1,1)} 3W1R and block B={(1,0),(2,0),(1,1),(2,1)} 3W1R, share edge {(1,0),(1,1)}. The shared edge points have fixed colors. In A, the red is at one corner; in B, red at one corner. The shared edge {(1,0),(1,1)}: if A's red is at (0,0) (so (1,0),(1,1) white), then shared edge both white. Then B's red is at (2,0) or (2,1) (since (1,0),(1,1) white). If B's red at (2,0): B={(1,0)W,(2,0)R,(1,1)W,(2,1)W}. Consistent. So two 3-white blocks can be adjacent with reds on the outer edge (forming a "domino" of reds separated by 2 whites). 

Let me think about tiling with a pattern. Consider a "stripe" of 3-white blocks. Actually, let me think of the following pattern: red points form isolated points, each surrounded by 3 whites in its witness block, and the rest all red. But "rest all red" means 0-white blocks, which are all-red 2×2. But if reds are dense (5714 reds, 4286 whites), and 4284 blocks all-red... an all-red block has 4 reds. 4284 all-red blocks would contain up to 4·4284 red incidences but reds shared. Hmm.

Let me think about the white points' arrangement. 4286 whites, each in 4 blocks, total 17144 incidences, of which 17142 are in 3-white blocks (5714 blocks × 3) and 2 in the exceptional block(s). So almost every white incidence is in a 3-white block. A white point is in 4 blocks; ideally all 4 are 3-white blocks (then it's in 4 witness blocks, witnessing up to 4 reds — the saturated case). With deficit 2, almost all whites are in 4 three-white blocks (saturated), except deficit 2 (e.g., one white in only 2 three-white blocks + 2 in other, or two whites in 3 three-white blocks + 1 other). 

But we showed saturated whites (in 4 three-white blocks) require the plus pattern (axis neighbors white, diagonal red), which cascades. And ~4285 saturated whites cascade into all-white rows → W4 blocks → contradiction (we can't have W4, but saturated whites' axis neighbors are white, not W4 directly; W4 would need a 2×2 all white). Let me re-examine: saturated white w has axis neighbors white and diagonal red. The 2×2 block NE of w = {(0,0)W,(1,0)W,(0,1)W,(1,1)R}: 3W1R, not W4 ✓. So saturated whites don't directly create W4. The issue is whether a large axis-connected white region creates W4 somewhere. 

If we have a 2×2 all-white block, that's W4 (forbidden). When does that happen? A 2×2 block all white means all 4 corners white. In our structure, blocks are 0W or 3W (mostly). A 3W block has 1 red, so not all white. A 0W block all red. So no block is all white! So condition (a) automatically satisfied if all blocks are 0W or 3W. The exceptional block (1 or 2 white) also not all white. So condition (a) is fine. 

So the only obstruction to r=5714 is whether we can realize a coloring where all blocks are 0W or 3W (plus 1-2 exceptions) consistently, with 4286 whites. The cascade argument was about saturated whites forcing axis neighbors white, but that's fine as long as no W4 — and there's no W4 since all blocks 0W/3W. Wait, but does "saturated white forces axis neighbors white" hold, and does that force the structure to be the all-3W tiling (r=2500)? Let me reconsider.

If almost all whites are saturated (in 4 three-white blocks), each saturated white has axis neighbors white and diagonal red. Consider the white set. Saturated white w: axis neighbors white. Are axis neighbors saturated? An axis neighbor (1,0) is white; is it in 4 three-white blocks? (1,0) is in cells: NE{(1,0),(2,0),(1,1),(2,1)}, NW{(0,0),(1,0),(0,1),(1,1)}, SE{(1,-1),(2,-1),(1,0),(2,0)}, SW{(0,-1),(1,-1),(0,0),(1,0)}. For (1,0) to be saturated (all 4 cells 3-white), need each cell to have exactly 1 red. NW cell {(0,0),(1,0),(0,1),(1,1)}: (0,0)W,(1,0)W,(0,1)W,(1,1)R → 1 red ✓ (this is w's NE cell, 3W1R). SE cell {(0,-1),(1,-1),(0,0),(1,0)}: w's SE cell, (1,-1)R, others W → 1 red ✓. NE cell {(1,0),(2,0),(1,1),(2,1)}: (1,1)R, (1,0)W, need (2,0),(2,1): for 1 red total need (2,0)W,(2,1)W. SW cell {(0,-1),(1,-1),(0,0),(1,0)} already counted (that's w's SE). Wait I need the 4 cells of (1,0): 
(1,0) is corner of: C(1,0)={(1,0),(2,0),(1,1),(2,1)} [as bottom-left], C(0,0)={(0,0),(1,0),(0,1),(1,1)} [as bottom-right], C(1,-1)={(1,-1),(2,-1),(1,0),(2,0)} [as top-left], C(0,-1)={(0,-1),(1,-1),(0,0),(1,0)} [as top-right].
- C(0,0) = w's NE cell: 3W1R (red (1,1)) ✓.
- C(0,-1) = w's SE cell: {(0,-1),(1,-1),(0,0),(1,0)}: (1,-1)R, rest W ✓ 3W1R.
- C(1,0) = {(1,0),(2,0),(1,1),(2,1)}: (1,0)W,(1,1)R, need (2,0),(2,1) both W for 3W1R (red (1,1)). 
- C(1,-1) = {(1,-1),(2,-1),(1,0),(2,0)}: (1,-1)R,(1,0)W, need (2,-1),(2,0) both W for 3W1R (red (1,-1)).
So (1,0) saturated needs (2,0)W,(2,1)W,(2,-1)W. I.e., (2,0) white and (2,±1) white. 

So if (1,0) is also saturated, then (2,0) white and (2,1),(2,-1) white. Then (2,0) saturated needs (3,0)W,(3,1)W,(3,-1)W and (2,1)W,(2,-1)W (already). Etc. So the +x arm: (0,0)W,(1,0)W,(2,0)W,(3,0)W,... all white, and (k,±1) white for all k. So entire rows y=0, y=1, y=-1 become white?? (k,1) white for all k → row 1 all white. (k,-1) white → row -1 all white. (k,0) white → row 0 all white. Then rows 0,1,-1 all white → 2×2 blocks within rows 0,1 all white → W4! Contradiction.

So if (1,0) is saturated (in addition to w), we get W4. So we can't have two adjacent saturated whites (axis-adjacent). Because saturated white forces axis neighbors white, and if an axis neighbor is also saturated, it forces the next layer, eventually filling rows → W4. 

More precisely: saturated whites can't be axis-adjacent to each other (else cascade → W4). Actually let me verify: the contradiction came from (1,0) saturated forcing (2,1),(2,-1) white and (2,0) white; then (2,0) saturated forcing (3,±1),(3,0) white; inductively all (k,0),(k,1),(k,-1) white → rows 0,±1 all white → W4. So yes, two axis-adjacent saturated whites → eventually W4. So saturated whites form an independent set in the axis-adjacency graph (no two axis-adjacent). 

But saturated white w forces its 4 axis neighbors to be white. Those axis neighbors are white but NOT saturated (since saturated whites independent, and they're axis-adjacent to w which is saturated). So axis neighbors of saturated whites are non-saturated whites. 

Now, how many saturated whites can we have? They're an independent set in axis-adjacency graph (grid graph), so at most 5000 (checkerboard). But also each saturated white needs 4 axis neighbors white (non-saturated). 

Recall we need ~4285 saturated whites (deficit 2 means ~4285 of the 4286 whites are saturated). But saturated whites must be independent (≤5000, ok) AND each needs 4 white axis neighbors. With 4285 saturated and 4286 total whites, only 1 non-saturated white. But each saturated white needs 4 axis neighbors white (non-saturated, since saturated can't be axis-adjacent). So each saturated white needs 4 distinct non-saturated white neighbors. With only 1 non-saturated white, impossible (can't have 4285 saturated each needing 4 non-saturated neighbors from a pool of 1). 

Contradiction! So r=5714 is impossible. 

Let me formalize: Let s = number of saturated whites (in 4 three-white blocks). Each saturated white has 4 axis neighbors, all white and non-saturated (non-saturated because saturated whites are axis-independent). So number of non-saturated whites ≥ ... each saturated white contributes 4 "requirements" of non-saturated white axis neighbors. A non-saturated white can be axis-neighbor to up to 4 saturated whites. So 4s ≤ 4·(non-saturated whites) → s ≤ non-saturated whites. Total whites w = s + (non-saturated) ≥ 2s. So s ≤ w/2. 

Now the incidence: 3r ≤ 4w - (deficit from non-saturated). Non-saturated whites are in fewer than 4 three-white blocks. Let me bound total incidences in 3-white blocks = 3a_3 ≤ 4s + 3·(non-saturated) [saturated contribute 4, non-saturated contribute ≤3]. Actually non-saturated whites are in ≤3 three-white blocks (since not saturated means <4). So 3a_3 ≤ 4s + 3(w - s) = 3w + s. And a_3 ≥ r = 10000 - w. So 3(10000 - w) ≤ 3w + s ≤ 3w + w/2 = 3.5w. → 30000 - 3w ≤ 3.5w → 30000 ≤ 6.5w → w ≥ 30000/6.5 = 4615.38 → w ≥ 4616, r ≤ 5384.

Hmm, let me double check: 30000 ≤ 6.5 w → w ≥ 4615.38 → w ≥ 4616, r ≤ 10000 - 4616 = 5384.

But wait, I need to double-check the saturated independence claim and the "non-saturated in ≤3 three-white blocks" and refine. Also non-saturated could be in 4 blocks but not all 3-white (some 0-white or 2-white). Let me reconsider: "saturated" = in 4 three-white blocks. A white in 4 blocks total; if not saturated, it's in ≤3 three-white blocks (could be in 4 blocks but one is not 3-white). So non-saturated white contributes ≤3 incidences to three-white blocks. OK.

And saturated independence: two axis-adjacent saturated whites → cascade → W4. Let me re-examine if this is airtight. Saturated white w at (0,0): axis neighbors (1,0),(-1,0),(0,1),(0,-1) white, diagonals (1,1),(-1,1),(1,-1),(-1,-1) red. Now (1,0) saturated: axis neighbors (2,0),(0,0),(1,1),(1,-1) white. But (1,1) is red (from w saturated)! Contradiction immediately. So (1,0) can't be saturated because w saturated forces (1,1) red, but (1,0) saturated forces (1,1) white. 

So saturated whites can't be axis-adjacent (immediate contradiction, no need for cascade). So saturated whites axis-independent. Confirmed, even stronger.

So s ≤ w/2 (each saturated needs 4 non-saturated axis neighbors, each non-saturated serves ≤4 saturated, so 4s ≤ 4(w-s) → s ≤ w-s → s ≤ w/2). 

And 3a_3 ≤ 4s + 3(w-s) = 3w + s ≤ 3w + w/2 = 7w/2. With a_3 ≥ r = 10000 - w: 3(10000-w) ≤ 7w/2 → 30000 - 3w ≤ 7w/2 → 30000 ≤ 13w/2 → w ≥ 60000/13 = 4615.38 → w ≥ 4616, r ≤ 5384.

Can we tighten further? The non-saturated whites that are axis neighbors of saturated whites — what structure? A non-saturated white that's an axis neighbor of a saturated white: e.g., (1,0) with w=(0,0) saturated. (1,0) is white, (1,1) red, (1,-1) red (from w saturated), (0,0) white, (2,0)=?. (1,0)'s cells: C(0,0) [w's NE, 3W1R, red (1,1)], C(0,-1) [w's SE, 3W1R, red (1,-1)], C(1,0)={(1,0),(2,0),(1,1),(2,1)}: (1,0)W,(1,1)R, so this block has ≥1 red (1,1); for it to be 3-white need (2,0),(2,1) white → then 3W1R red(1,1). C(1,-1)={(1,-1),(2,-1),(1,0),(2,0)}: (1,-1)R,(1,0)W, for 3W need (2,-1),(2,0) white. So (1,0) is in 2 three-white blocks for sure (w's NE, SE), and potentially 2 more (C(1,0),C(1,-1)) if (2,0),(2,1),(2,-1) white. If (1,0) is non-saturated (in ≤3 three-white blocks), then at most one of C(1,0), C(1,-1) is 3-white. 

Hmm, so (1,0) contributes 2 or 3 to three-white block incidences. If it contributes exactly 2 (both C(1,0),C(1,-1) not 3-white, i.e., (2,0) or (2,±1) red), then deficit 2 from this white. If 3, deficit 1.

Let me reconsider the bound more carefully. Let me define for each white the number t = number of three-white blocks it's in (0≤t≤4). Saturated: t=4. Sum of t over whites = 3a_3. We have 3a_3 ≥ 3r (since a_3 ≥ r, actually a_3 ≥ r so 3a_3 ≥ 3r; but we want upper bound on 3a_3 to constrain). Wait we want to show w large, so we want 3a_3 ≤ something in terms of w, combined with 3a_3 ≥ 3(10000-w). 

3a_3 = sum t. We need upper bound on sum t given the structure. Saturated (t=4) are axis-independent and each forces 4 axis neighbors white (those have t ≤ 3, and actually let me see their t). 

Let me reconsider: maybe non-saturated whites that are axis-neighbors of saturated have t ≤ 2 or 3. Let me compute the max t for an axis-neighbor of a saturated white. (1,0) with w saturated: t ≥ 2 (w's NE, SE cells). Can be 3 or 4. If t=4, (1,0) saturated → contradiction (shown). So t ≤ 3. Can t=3? Yes if exactly one of C(1,0),C(1,-1) is 3-white. So t∈{2,3} for axis-neighbor of saturated (assuming (1,0) is in w's two cells which are 3-white). Actually t≥2 always for axis-neighbor of saturated. And t≤3. 

What about whites not adjacent to any saturated white? They could have t up to 4 but if t=4 they'd be saturated (and then their axis neighbors white...). Hmm, any t=4 white is saturated and axis-independent from other saturated. 

This is getting complicated. Let me just try to find the exact optimum by considering a clean construction and matching bound. Let me guess the answer involves 13 (from 60000/13). 60000/13 = 4615.38, r ≤ 5384. 5384 = ? 10000 - 4616. Hmm 5384 = 13·414.15 no. 5384/8=673. Not clean. Let me see if the bound tightens to a cleaner number with more analysis, or if 5384 is it.

Actually, let me reconsider whether saturated whites' axis-neighbors have t ≤ 2 (not 3), which would tighten. (1,0) axis-neighbor of saturated w=(0,0). t = number of 3-white blocks through (1,0). We have C(0,0) and C(0,-1) are 3-white (w's
