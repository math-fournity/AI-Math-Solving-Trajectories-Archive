# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   The numbers from $1$ to $100$ are arranged in a $10\times 10$ table so that any two adjacent numbers have sum no larger than $S$. Find the least value of $S$ for which this is possible.
[i]D. Hramtsov[/i]       — 题目文本
#   1. **Understanding the Problem:**
   We need to arrange the numbers from \(1\) to \(100\) in a \(10 \times 10\) table such that the sum of any two adjacent numbers is no larger than \(S\). We aim to find the smallest possible value of \(S\).

2. **Initial Consideration:**
   Let's consider the largest number \(x\) such that there are \(5\) numbers from \(x\) to \(100\) in the same row or column. We know that \(x \geq 60\), implying that none of \(x, x+1, \ldots, 100\) are adjacent to one another.

3. **Coloring Argument:**
   - Color the numbers \(x, x+1, \ldots, 100\) red.
   - Color all squares neighboring any of these red squares blue.

4. **Lemma:**
   Any row has at least as many blue squares as red squares.
   - **Proof:** This can be shown by simple casework. If a row has \(r\) red squares, then each red square must have at least one blue neighbor in the same row, ensuring that the number of blue squares is at least \(r\).

5. **Deficient Rows:**
   - Define a row as **deficient** if it has the same number of red and blue squares.
   - Claim: There cannot be two adjacent deficient rows.
   - **Proof by Contradiction:**
     - Suppose there are two adjacent deficient rows \(r_1\) and \(r_2\).
     - Let \(R_1, B_1\) be the sets of red and blue squares in \(r_1\), and \(R_2, B_2\) be the sets of red and blue squares in \(r_2\).
     - The squares under \(R_1\) must be in \(R_2 \cup B_2\), and the squares above \(R_2\) must be in \(R_1 \cup B_1\).
     - Since \(R_1\) and \(R_2\) are deficient, \(|R_1| = |B_1| = |R_2| = |B_2|\).
     - This implies \(R_1 = B_2\) and \(R_2 = B_1\), leading to a contradiction.

6. **Counting Blue Squares:**
   - There are at most \(5\) deficient rows.
   - Therefore, there are at least \(100 - x + 1 + 5 = 106 - x\) blue squares.

7. **Conclusion:**
   - One of these blue squares is at least \(106 - x\).
   - Adding this blue square with its neighbor gives a sum of at least \(106\).

Thus, the least value of \(S\) for which this arrangement is possible is \(106\).

The final answer is \(\boxed{106}\).  — 标准解答
#   Let me analyze this problem carefully.

We need to arrange numbers 1 to 100 in a 10×10 grid such that any two adjacent numbers (sharing an edge) have sum ≤ S. Find the minimum S.

First, let me check for answer leaks. The problem statement is clean - just the problem, author attribution, and constraints. No leaked answers.

Now let me solve this.

**Lower bound:**

Consider the largest numbers. The key insight is about the structure of the grid and which numbers must be adjacent.

The grid is a 10×10 grid graph. It has a maximum independent set. The grid graph 10×10 is bipartite (checkerboard coloring). One color class has 50 cells, the other has 50 cells.

In a bipartite graph, if we put the 50 largest numbers (51-100) on one color class and the 50 smallest (1-50) on the other, then every edge connects a large number to a small number. The maximum sum would be maximized when the largest number (100) is adjacent to the largest possible small number.

But we want to minimize the maximum sum. So we need to think about what's forced.

Let me think about this differently. Consider the 50 cells of one color (say black) and 50 cells of the other color (white). Every edge connects a black cell to a white cell. If we place numbers 51-100 on black cells and 1-50 on white cells, then every adjacent pair has one from {51,...,100} and one from {1,...,50}.

The maximum sum would be max over edges of (black_value + white_value). We want to minimize this maximum.

Actually, let's think about it more carefully. We don't have to put 51-100 on one color and 1-50 on the other. But intuitively, to minimize the maximum adjacent sum, we want large numbers adjacent to small numbers.

Let me think about the lower bound first.

**Lower bound argument:**

Consider the numbers 91, 92, ..., 100 (the top 10 numbers). Each of these has degree at least 2 (corner cells have degree 2, edge cells have degree 3, interior cells have degree 4). Actually, we need to think about how many "large" numbers can be placed in non-adjacent positions.

The maximum independent set of the 10×10 grid is 50 (one color class). So we can place at most 50 numbers such that no two are adjacent. 

If we place the 50 largest numbers (51-100) all on one color class, they're pairwise non-adjacent. Then the 50 smallest (1-50) go on the other color class. Every edge connects a number from {51,...,100} to a number from {1,...,50}.

The question is: what's the minimum possible maximum edge sum?

For a number $a$ in {51,...,100} placed at some cell, it's adjacent to some cells in the other color class. The sum $a + b$ where $b$ is the largest neighbor of $a$.

To minimize the maximum sum, we want to pair large numbers with small neighbors. 

Let me think about this as an optimization problem. We have a bipartite graph $G = (B, W, E)$ where $|B| = |W| = 50$. We assign values $\{51, ..., 100\}$ to $B$ and $\{1, ..., 50\}$ to $W$ (or some other split). We want to minimize $\max_{(b,w) \in E} (val(b) + val(w))$.

Actually, we don't even need to split it this way. Let me think about what the optimal split is.

Hmm, let me think about lower bounds more carefully.

**Lower bound via counting:**

Consider any arrangement. Look at the 10 largest numbers: 91, 92, ..., 100. 

Actually, let me think about a cleaner approach. 

Consider the set of numbers $\{k+1, k+2, ..., 100\}$ for some threshold $k$. These are the $100-k$ largest numbers. In the grid, the maximum number of pairwise non-adjacent cells is 50. So if $100 - k > 50$, i.e., $k < 50$, then at least two of these large numbers must be adjacent. But that doesn't directly give us a bound on the sum.

Let me think differently. 

**Key idea:** Consider the numbers $a_1 > a_2 > ... > a_{100}$ (so $a_i = 101 - i$). We want to find the minimum $S$ such that we can arrange them so adjacent sums ≤ S.

Let me think about what numbers must be adjacent to the largest numbers.

Number 100 has degree $d$ (2, 3, or 4 depending on position). Its neighbors must all be ≤ $S - 100$.

Number 99: if not adjacent to 100, its neighbors must be ≤ $S - 99$. If adjacent to 100, then $100 + 99 = 199 ≤ S$ is needed, which would be bad.

So we want 100 and 99 to not be adjacent. More generally, we want large numbers to be non-adjacent to each other.

The maximum independent set is 50. So we can place at most 50 numbers pairwise non-adjacent. 

If we place numbers 51-100 on one color class (50 cells, pairwise non-adjacent), and 1-50 on the other, then every edge sum is at most $100 + 50 = 150$ and at least $51 + 1 = 52$. But can we do better than 150?

The maximum edge sum in this arrangement depends on the specific assignment. We want to minimize the maximum edge sum.

Let me think about it as: we have a bipartite graph. On one side (B, 50 cells), we place numbers from some set $X$ of 50 numbers. On the other side (W, 50 cells), we place numbers from the complement $Y$. We want to minimize the maximum edge sum.

To minimize the maximum edge sum, we should put large numbers on one side and small on the other. So $X = \{51, ..., 100\}$ and $Y = \{1, ..., 50\}$ (or vice versa).

Now, within this, we need to assign specific numbers to specific cells to minimize the maximum edge sum.

The maximum edge sum is $\max_{(b,w) \in E} (f(b) + g(w))$ where $f: B \to \{51,...,100\}$ and $g: W \to \{1,...,50\}$ are bijections.

To minimize this, we want: if $f(b)$ is large, then $g(w)$ should be small for all neighbors $w$ of $b$.

This is related to the structure of the grid graph.

Let me think about the degrees. In the 10×10 grid:
- 4 corner cells: degree 2
- 32 edge cells (non-corner): degree 3
- 64 interior cells: degree 4

In each color class (50 cells):
- 2 corner cells, 16 edge cells, 32 interior cells (one color)
- 2 corner cells, 16 edge cells, 32 interior cells (other color)

Wait, let me recount. The 10×10 grid has positions $(i,j)$ for $1 \le i,j \le 10$. Color = $(i+j) \mod 2$.

Corner cells: $(1,1), (1,10), (10,1), (10,10)$. Colors: $(1+1)=2$ even, $(1+10)=11$ odd, $(10+1)=11$ odd, $(10+10)=20$ even. So 2 corners are even, 2 are odd.

Edge cells (non-corner): cells on the boundary but not corners. There are $4 \times 8 = 32$ such cells. By symmetry, 16 are even and 16 are odd.

Interior cells: $8 \times 8 = 64$ cells. 32 even, 32 odd.

So each color class has: 2 corners (degree 2), 16 edge (degree 3), 32 interior (degree 4). Total = 50. ✓

Now, the cell with the highest value (100) should be placed where it has the fewest neighbors and those neighbors can be made small. A corner cell has only 2 neighbors. So place 100 at a corner.

If 100 is at a corner (say $(1,1)$, which is even color), its neighbors are $(1,2)$ and $(2,1)$, both odd color. These get values from $\{1,...,50\}$. To minimize the max sum involving 100, we'd want these to be as small as possible, say 1 and 2. Then the sums are 101 and 102.

But we also need to consider 99. If 99 is also at a corner of the same color class (even), say $(10,10)$, its neighbors are $(10,9)$ and $(9,10)$, both odd. We'd want these to be small too, say 3 and 4. Sums: 102, 103.

Continuing, 98 at another even corner... but there are only 2 even corners. So 98 goes to an edge cell (degree 3) or interior cell (degree 4).

This is getting complex. Let me think about it more carefully as an optimization problem.

Actually, let me think about a cleaner lower bound argument.

**Lower bound argument:**

Consider the 50 largest numbers $\{51, 52, ..., 100\}$. In any arrangement, consider the set of cells containing these numbers. Since the maximum independent set is 50, it's possible that these 50 cells form an independent set (one color class). But if they don't, some pair of them is adjacent, giving a sum ≥ 51 + 52 = 103.

But even if they form an independent set, each of these cells is adjacent to cells containing numbers from $\{1, ..., 50\}$.

Let me think about the problem differently. 

Consider any valid arrangement with maximum adjacent sum $S$. 

For each number $k \in \{51, ..., 100\}$, all its neighbors are $\leq S - k$. 

The number of cells that are "available" for numbers $\geq m$ (for some threshold) is constrained.

Let me try a different approach. Let's think about the problem in terms of the "conflict graph."

Two numbers $a$ and $b$ "conflict" (cannot be adjacent) if $a + b > S$. We need to arrange 1-100 in the grid so that no two conflicting numbers are adjacent.

For a given $S$, the conflict graph on $\{1, ..., 100\}$ has an edge between $a$ and $b$ iff $a + b > S$. We need to find an arrangement in the grid where no grid-adjacent pair is a conflict pair.

The grid is bipartite. So if we 2-color the grid, we need to partition $\{1,...,100\}$ into two sets $A$ and $B$ (each of size 50) such that no element of $A$ conflicts with any element of $B$ (since all grid edges go between the two color classes). Wait, that's not quite right - we need that for every grid edge $(u,v)$, the numbers at $u$ and $v$ don't conflict. But the grid edges don't connect all pairs between the two color classes - only specific pairs.

However, a sufficient condition is: partition $\{1,...,100\}$ into $A$ and $B$ (each size 50) such that no $a \in A, b \in B$ conflict (i.e., $a + b \leq S$ for all $a \in A, b \in B$). Then place $A$ on one color class and $B$ on the other, and no grid-adjacent pair conflicts.

But this is sufficient, not necessary. The necessary condition is weaker because not all pairs between color classes are grid-adjacent.

For the sufficient condition: we need $\max(A) + \max(B) \leq S$. To minimize this, we want to split $\{1,...,100\}$ into two sets of 50 where the sum of the maxima is minimized. The optimal split is $A = \{1,...,50\}, B = \{51,...,100\}$, giving $\max(A) + \max(B) = 50 + 100 = 150$. Or $A = \{1,...,50\}, B = \{51,...,100\}$, same thing.

But wait, can we do better with the necessary condition? Yes, because not all pairs between the two color classes are adjacent in the grid.

So the answer might be less than 150. Let me think more carefully.

Let me think about what the actual minimum is.

Let me consider a specific construction and lower bound.

**Approach: Think about which numbers can be "high" and what their neighbors must be.**

Let's say $S$ is the target. A number $k$ can only be adjacent to numbers $\leq S - k$. 

For $k = 100$: neighbors must be $\leq S - 100$.
For $k = 99$: neighbors must be $\leq S - 99$.
...

The number 100 has at least 2 neighbors (if at a corner). These neighbors must be $\leq S - 100$. So we need at least 2 numbers $\leq S - 100$.

Number 99: if at a corner, 2 neighbors $\leq S - 99$. But the 2 numbers used for 100's neighbors are already $\leq S - 100 \leq S - 99$, so they could potentially be shared... no, they can't be shared because 99 and 100 are at different cells.

Actually, let me think about it as a matching/flow problem or use a more clever counting argument.

**Better lower bound approach:**

Consider the set $H = \{k : k > S/2\}$. These are the "high" numbers. Any two high numbers that are adjacent would have sum $> S$, which is forbidden. So the high numbers must form an independent set in the grid.

The maximum independent set of the 10×10 grid is 50. So $|H| \leq 50$, which means the number of integers in $\{1,...,100\}$ that are $> S/2$ is at most 50. This gives $100 - \lfloor S/2 \rfloor \leq 50$, so $\lfloor S/2 \rfloor \geq 50$, so $S \geq 100$.

But this is a weak bound. Let me think stronger.

**Stronger approach:**

Consider numbers $k$ and $S - k$ for various $k$. If $k + (S-k) = S$, they can be adjacent (sum exactly $S$). But $k + (S - k + 1) = S + 1 > S$, so $k$ and $S - k + 1$ cannot be adjacent.

Hmm, let me think about this more carefully using the structure of the grid.

**Even stronger lower bound:**

Consider the numbers $\{m, m+1, ..., 100\}$ for some $m$. These are $101 - m$ numbers. They must form an independent set (if any two are adjacent, their sum $\geq m + (m+1) = 2m+1$; for this to exceed $S$, we need $2m + 1 > S$, i.e., $m > (S-1)/2$).

So for $m > (S-1)/2$, the set $\{m, ..., 100\}$ must be an independent set, requiring $101 - m \leq 50$, i.e., $m \geq 51$. This gives $(S-1)/2 < 51$, i.e., $S < 103$, so $S \leq 102$... wait, that's an upper bound on $S$ from this argument? No, let me redo.

If $m > (S-1)/2$, then any two numbers in $\{m, ..., 100\}$ have sum $\geq 2m > S - 1$, so sum $\geq 2m \geq S + 1 > S$ (if $2m > S$). Wait, $m > (S-1)/2$ means $2m > S - 1$, so $2m \geq S$ (if $S$ is integer and $2m$ is integer). So $2m \geq S$, meaning two numbers both $\geq m$ have sum $\geq 2m \geq S$. If $2m > S$, they can't be adjacent. If $2m = S$, they can be adjacent (sum = S is allowed).

So for $2m > S$ (i.e., $m > S/2$), the set $\{m, ..., 100\}$ must be independent, giving $101 - m \leq 50$, so $m \geq 51$, so $S/2 < 51$, $S < 102$, $S \leq 101$.

For $2m = S$ (i.e., $m = S/2$), two numbers both equal to $m$ have sum $S$ (allowed), but $m$ and $m+1$ have sum $S+1 > S$ (not allowed). So the set $\{m+1, ..., 100\}$ must be independent (any two have sum $\geq 2(m+1) = S + 2 > S$). This gives $100 - m \leq 50$, so $m \geq 50$, so $S/2 \geq 50$, $S \geq 100$.

And the set $\{m, m+1, ..., 100\}$ where $m = S/2$: $m$ can be adjacent to $m$ (but there's only one $m$), and $m$ can be adjacent to anything $\leq S - m = m$. So $m$ can be adjacent to numbers $\leq m$. But $m+1$ can only be adjacent to numbers $\leq S - (m+1) = m - 1$.

So the constraint is: $\{m+1, ..., 100\}$ must be independent, requiring $100 - m \leq 50$, i.e., $m \geq 50$, i.e., $S \geq 100$.

This gives $S \geq 100$. But this seems too weak. Let me think about whether we can achieve $S = 100$ or if we need more.

Wait, actually, the independent set constraint gives $S \geq 100$, but there might be additional constraints from the grid structure.

Let me think about $S = 100$. Can we achieve it?

If $S = 100$, then numbers $> 50$ must form an independent set (any two numbers $> 50$ have sum $> 100$). There are 50 such numbers (51-100), and the max independent set is 50. So they must occupy exactly one color class.

Numbers $\leq 50$ occupy the other color class. Now, number 100 must have all neighbors $\leq 100 - 100 = 0$. But there's no number $\leq 0$! So $S = 100$ is impossible.

So $S \geq 101$.

For $S = 101$: number 100 must have all neighbors $\leq 1$. So 100 must be adjacent only to 1 (and possibly other 1's, but there's only one 1). So 100 must be at a corner (degree 2), with both neighbors being... wait, 100 needs neighbors $\leq 1$, so both neighbors must be 1. But there's only one 1. So 100 can have at most one neighbor that is 1, and the other neighbor must also be $\leq 1$, which is impossible.

Wait, 100 needs neighbors $\leq S - 100 = 1$. So every neighbor of 100 must be $\leq 1$, i.e., must be 1. But 100 has at least 2 neighbors (minimum degree is 2 at corners), and there's only one "1". So $S = 101$ is impossible.

For $S = 102$: number 100 needs neighbors $\leq 2$. Number 100 has at least 2 neighbors. If at a corner, exactly 2 neighbors, both must be from $\{1, 2\}$. That's possible: place 100 at a corner, with neighbors 1 and 2.

Number 99 needs neighbors $\leq 3$. If 99 is at a corner, 2 neighbors from $\{1, 2, 3\}$. But 1 and 2 might already be used. If 1 and 2 are neighbors of 100, then 99's neighbors must be from $\{1, 2, 3\} \setminus \{\text{used}\}$... but 99 is at a different corner, so its neighbors are different cells. The values 1 and 2 are placed at specific cells (neighbors of 100), and 99's neighbors are different cells. So 99's neighbors need values $\leq 3$, and we have value 3 available (and possibly 1 or 2 if they happen to also be neighbors of 99, but that's unlikely in a 10×10 grid).

Actually, wait. Let me reconsider. The two neighbors of 100 (at corner (1,1)) are (1,2) and (2,1). If 99 is at corner (10,10), its neighbors are (10,9) and (9,10). These are completely different cells. So 99's neighbors need values $\leq 3$. We need to place two values from $\{1, 2, 3\}$ at (10,9) and (9,10), but 1 and 2 are already used at (1,2) and (2,1). So we only have 3 left, and we need two values $\leq 3$. That's impossible since only 3 is available.

Hmm, so we need to be more careful. Let me reconsider.

For $S = 102$:
- 100 needs 2 neighbors ≤ 2 (if at corner). Use 1, 2.
- 99 needs 2 neighbors ≤ 3 (if at corner). Available values ≤ 3 not yet used: {3}. Only 1 value, need 2. Problem!

Unless 99 is not at a corner but... if 99 is at an edge (degree 3), it needs 3 neighbors ≤ 3, even worse. If at interior (degree 4), 4 neighbors ≤ 3, worse.

So 99 must be at a corner, but even then, we need 2 values ≤ 3, and only 3 is left after using 1 and 2 for 100.

Wait, unless 99 is adjacent to 100. If 99 is adjacent to 100, then 99 + 100 = 199 > 102. Not allowed. So 99 can't be adjacent to 100.

Hmm, so $S = 102$ might not work either. Let me reconsider.

Actually wait. The neighbors of 100 must be ≤ 2. The neighbors of 99 must be ≤ 3. But these neighbor sets might overlap! If 99 is at a corner adjacent to 100's corner... no, in a 10×10 grid, corners are far apart.

Actually, can 99 be at a cell adjacent to one of 100's neighbors? That doesn't help directly.

Let me reconsider. The issue is that we need to "serve" the high numbers with low numbers, and the low numbers are a limited resource.

Let me think about this more systematically.

**Systematic lower bound:**

For a given $S$, number $k$ needs all its neighbors to be $\leq S - k$. Let $d(k)$ be the degree of the cell where $k$ is placed. Then $k$ "consumes" $d(k)$ cells that must have values $\leq S - k$.

Consider the high numbers $100, 99, 98, ..., 51$ (50 numbers). They must be on one color class (independent set). Each has some degree (2, 3, or 4), and their neighbors are on the other color class with values from $\{1, ..., 50\}$.

For number $k$ (where $k \in \{51, ..., 100\}$), its neighbors must be $\leq S - k$. 

Let's think about it from the perspective of the low numbers. Number $j$ (where $j \in \{1, ..., 50\}$) is on the "low" color class. It can be adjacent to high numbers $\leq S - j$. So number $j$ can "support" high numbers up to $S - j$.

The constraint is: for each high number $k$, all its $d(k)$ neighbors must be $\leq S - k$.

This is a complex combinatorial constraint. Let me try to find the answer by thinking about specific constructions.

Let me try $S = 110$ and see if it works, then try to lower it.

Actually, let me think about this problem from a higher level. 

The answer to this problem... let me think about what's known. This is a competition problem by D. Hramtsov. Let me think about the answer.

Let me try to find the answer by constructing an arrangement and proving a matching lower bound.

**Construction attempt:**

Place numbers on the grid in a "snake" pattern that alternates high and low. 

Actually, let me think about the problem differently. The grid is bipartite with color classes of size 50 each. Place 51-100 on one class and 1-50 on the other. Now we need to assign specific numbers to minimize the max edge sum.

The key structural feature of the 10×10 grid is the degree distribution and the adjacency structure.

Let me think about a "complementary" pairing. If we pair $k$ with $101 - k$ (so 100 with 1, 99 with 2, etc.), and place each pair on adjacent cells, the sum would be 101. But each cell has multiple neighbors, so we can't just pair them.

Let me think about the problem as follows. We have the bipartite graph $G = (B, W, E)$. We assign $f: B \to \{51,...,100\}$ and $g: W \to \{1,...,50\}$. We want to minimize $\max_{(b,w) \in E} (f(b) + g(w))$.

Equivalently, define $f'(b) = f(b) - 50 \in \{1,...,50\}$ and $g(w) \in \{1,...,50\}$. Then $f(b) + g(w) = f'(b) + g(w) + 50$. So we want to minimize $\max_{(b,w) \in E} (f'(b) + g(w)) + 50$, i.e., minimize $\max_{(b,w) \in E} (f'(b) + g(w))$.

So we have two copies of $\{1,...,50\}$ assigned to the two color classes, and we want to minimize the maximum sum across edges. This is a cleaner formulation.

Let me call this the "bipartite labeling problem": given a bipartite graph $G = (B, W, E)$ with $|B| = |W| = 50$, assign labels $\{1,...,50\}$ to each side, minimizing the maximum edge sum.

For the 10×10 grid, what's the optimal value?

Let me think about lower bounds for this reformulated problem. The answer to the original problem is this value + 50.

**Lower bound for the bipartite labeling problem:**

Consider the vertex $b \in B$ with the highest label, which is 50. Its neighbors in $W$ must have labels $\leq T - 50$ where $T$ is the max edge sum we're trying to minimize. If $b$ has degree $d$, we need $d$ labels $\leq T - 50$.

Similarly, the vertex with label 49 needs its neighbors to have labels $\leq T - 49$.

And from the other side, the vertex $w \in W$ with label 50 needs its neighbors in $B$ to have labels $\leq T - 50$.

So both the highest-labeled vertices on each side impose constraints.

Let me think about the degree structure. In the 10×10 grid, considering one color class (say $B$):
- 2 vertices of degree 2 (corners)
- 16 vertices of degree 3 (edges)
- 32 vertices of degree 4 (interior)

Same for $W$.

The vertex labeled 50 on side $B$: to minimize $T$, place it at a corner (degree 2). Then we need 2 vertices in $W$ with labels $\leq T - 50$.

The vertex labeled 50 on side $W$: place at a corner (degree 2). Need 2 vertices in $B$ with labels $\leq T - 50$.

The vertex labeled 49 on side $B$: place at the other corner (degree 2). Need 2 vertices in $W$ with labels $\leq T - 49$.

The vertex labeled 49 on side $W$: place at the other corner (degree 2). Need 2 vertices in $B$ with labels $\leq T - 49$.

So far, with 4 corners (2 on each side), we place labels 50 and 49 on each side's corners.

For $B$ side: label 50 at corner $c_1$ (degree 2), label 49 at corner $c_2$ (degree 2).
- Neighbors of $c_1$ need labels $\leq T - 50$.
- Neighbors of $c_2$ need labels $\leq T - 49$.

For $W$ side: label 50 at corner $c_3$ (degree 2), label 49 at corner $c_4$ (degree 2).
- Neighbors of $c_3$ need labels $\leq T - 50$.
- Neighbors of $c_4$ need labels $\leq T - 49$.

Now, the neighbors of $c_1$ (in $W$) need labels $\leq T - 50$. The neighbors of $c_3$ (in $B$) need labels $\leq T - 50$. 

If $T - 50 \geq 2$, we have at least labels $\{1, 2\}$ available for these. But we need 2 labels for $c_1$'s neighbors and 2 labels for $c_3$'s neighbors, total 4 labels $\leq T - 50$ (assuming no overlap, which is the case since corners are far apart in a 10×10 grid).

Actually, the neighbors of $c_1$ and $c_3$ are different cells (one set in $W$, one set in $B$), so they use labels from different sides. So we need 2 labels $\leq T-50$ on side $W$ (for $c_1$'s neighbors) and 2 labels $\leq T-50$ on side $B$ (for $c_3$'s neighbors). Each side has 50 labels, so we need at least 2 labels $\leq T-50$ on each side, giving $T - 50 \geq 2$, $T \geq 52$.

But we also need labels for $c_2$'s neighbors (2 labels $\leq T - 49$ on side $W$) and $c_4$'s neighbors (2 labels $\leq T - 49$ on side $B$).

On side $W$: 2 labels $\leq T - 50$ (for $c_1$) and 2 labels $\leq T - 49$ (for $c_2$). The 2 labels for $c_1$ are also $\leq T - 49$ (since $T - 50 < T - 49$). So we need at least 2 labels $\leq T - 50$ and 2 more labels $\leq T - 49$ (but the first 2 also count). Actually, the 4 neighbor cells of $c_1$ and $c_2$ are all distinct (corners are far apart), so we need 4 distinct labels on side $W$, with 2 of them $\leq T - 50$ and all 4 $\leq T - 49$.

So on side $W$: 2 labels $\leq T - 50$ and 2 more labels in $(T-50, T-49]$ (or also $\leq T - 50$). The minimum is: 2 labels $\leq T - 50$, and 2 more labels $\leq T - 49$. So we need at least 2 labels $\leq T-50$ and at least 4 labels $\leq T - 49$ on side $W$.

Similarly on side $B$: 2 labels $\leq T - 50$ and 4 labels $\leq T - 49$.

This gives $T - 50 \geq 2$ (need 2 labels $\leq T-50$ on each side) and $T - 49 \geq 4$ (need 4 labels $\leq T-49$ on each side), so $T \geq 53$.

Continuing this analysis for more high-labeled vertices...

Let me think about this more systematically. Let me consider the top $k$ labels on each side and figure out how many low labels are needed.

On side $B$, the vertices with labels $50, 49, 48, ..., 50-k+1$ (the top $k$ labels) need their neighbors to have low labels. The constraint for label $50 - j$ (for $j = 0, 1, ..., k-1$) is that its $d$ neighbors have labels $\leq T - (50 - j) = T - 50 + j$.

If we place the top $k$ labels at the lowest-degree vertices (corners first, then edges, then interior), we minimize the total number of "low label slots" needed.

Let me think about it as a "demand" problem. 

On side $B$, sort vertices by degree: 2 corners (degree 2), 16 edges (degree 3), 32 interior (degree 4).

Assign labels 50, 49, 48, ... to vertices in order of increasing degree.

Label 50 → corner (degree 2), needs 2 neighbors with labels ≤ T - 50.
Label 49 → corner (degree 2), needs 2 neighbors with labels ≤ T - 49.
Label 48 → edge (degree 3), needs 3 neighbors with labels ≤ T - 48.
Label 47 → edge (degree 3), needs 3 neighbors with labels ≤ T - 47.
...

On side $W$, similarly:
Label 50 → corner (degree 2), needs 2 neighbors (in $B$) with labels ≤ T - 50.
Label 49 → corner (degree 2), needs 2 neighbors (in $B$) with labels ≤ T - 49.
...

Now, the demands on side $W$ (from $B$'s high labels) and the demands on side $B$ (from $W$'s high labels) interact.

Let me think about the demand on side $W$ from $B$'s top labels:
- Label 50 on $B$ (corner, degree 2): 2 cells in $W$ with labels ≤ T - 50.
- Label 49 on $B$ (corner, degree 2): 2 cells in $W$ with labels ≤ T - 49.
- Label 48 on $B$ (edge, degree 3): 3 cells in $W$ with labels ≤ T - 48.
- Label 47 on $B$ (edge, degree 3): 3 cells in $W$ with labels ≤ T - 47.
- ...

And the demand on side $B$ from $W$'s top labels:
- Label 50 on $W$ (corner, degree 2): 2 cells in $B$ with labels ≤ T - 50.
- Label 49 on $W$ (corner, degree 2): 2 cells in $B$ with labels ≤ T - 49.
- ...

These are symmetric. Let me focus on the demand on side $W$.

The total number of cells in $W$ that must have labels ≤ some threshold is constrained by the available labels. Specifically, the number of cells in $W$ with labels ≤ $m$ is exactly $m$ (since labels are 1 to 50). 

Now, the demand: for each high label on $B$, we need some cells in $W$ with labels ≤ some threshold. But a single cell in $W$ can satisfy the demands of multiple high labels on $B$ (if it's adjacent to multiple high-label $B$ vertices). However, in the grid, each $W$ cell has at most 4 neighbors in $B$.

This is getting complicated. Let me try a different approach: just try to find the answer by constructing a good arrangement and proving a tight lower bound.

Let me try to think about what $T$ (in the reformulated problem) should be, and then $S = T + 50$.

**Trying $T = 55$, so $S = 105$:**

Hmm, let me think about this more carefully. Let me try to think about what the answer might be.

Actually, let me think about a simpler version first. Consider a $2 \times n$ grid. Numbers 1 to $2n$. Bipartite with color classes of size $n$ each. 

For a $2 \times 2$ grid: numbers 1-4. Color classes: {(1,1), (2,2)} and {(1,2), (2,1)}. Each vertex has degree 2. Place 3,4 on one side and 1,2 on the other. The edges are (1,1)-(1,2), (1,1)-(2,1), (2,2)-(1,2), (2,2)-(2,1). So every vertex on one side is adjacent to every vertex on the other side (it's $K_{2,2}$). So the max sum is $\max(3,4) + \max(1,2) = 4 + 2 = 6$. Can we do better? With the split {3,4} and {1,2}, the max edge sum is 6. With split {1,4} and {2,3}: max edge sum = 4 + 3 = 7. With split {1,3} and {2,4}: 4 + 3 = 7. So the best is 6. And $S = 6$ for the $2 \times 2$ grid.

Hmm wait, for $2 \times 2$, the graph is $K_{2,2}$, so every pair across the partition is an edge. The minimum max edge sum is $\min_{\text{partition}} \max(A) + \max(B)$ where $A \cup B = \{1,2,3,4\}$, $|A| = |B| = 2$. Best: $A = \{1,2\}, B = \{3,4\}$, sum = 2 + 4 = 6. So $S = 6$.

For a path graph $P_n$ (1×n grid), the answer would be different because the graph is much sparser.

Let me think about the 10×10 grid more carefully.

Actually, let me think about the problem from the perspective of the "complement" arrangement.

In the reformulated problem, we assign labels 1-50 to each side of the bipartite graph. The max edge sum is $T$. We want to minimize $T$.

**Key observation:** If we use the "reversed" assignment on one side, i.e., assign label $k$ to the vertex that has the "most demanding" position, we can balance things.

Let me think about a specific strategy. On side $B$, assign labels in decreasing order to vertices in order of increasing degree (corners get highest labels, interior gets lowest). On side $W$, assign labels in increasing order to vertices in order of increasing degree (corners get lowest labels, interior gets highest). 

Wait, that doesn't make sense because both sides have the same degree distribution.

Let me think about it differently. The idea is: high labels on one side should be adjacent to low labels on the other side.

If we assign label 50 to a corner of $B$ (degree 2), its 2 neighbors in $W$ should have low labels. If we assign label 1 to a corner of $W$ (degree 2), its 2 neighbors in $B$ should have low labels. But the corner of $B$ with label 50 and the corner of $W$ with label 1 might not be adjacent.

Let me try to think about the grid structure more concretely.

Label the grid positions as $(i,j)$ for $1 \le i,j \le 10$. Even color: $(i+j)$ even. Odd color: $(i+j)$ odd.

$B$ = even cells, $W$ = odd cells.

Corners: $(1,1)$ even, $(1,10)$ odd, $(10,1)$ odd, $(10,10)$ even.

So $B$ has corners $(1,1)$ and $(10,10)$, and $W$ has corners $(1,10)$ and $(10,1)$.

Let me try a specific assignment. On side $B$ (even cells), assign labels based on the "anti-diagonal" or some pattern. 

Actually, let me try a "complementary" approach. Define the label of cell $(i,j)$ on side $B$ as $f(i,j)$ and on side $W$ as $g(i,j)$. We want $f(i,j) + g(i',j') \leq T$ for all adjacent pairs.

One natural approach: make $f$ and $g$ "anti-correlated" in some spatial sense. If $f$ is large at some cell, $g$ should be small at all neighboring cells.

Let me try: $f(i,j) = $ some function that's large at corners and small at center, and $g(i,j) = $ some function that's small at corners and large at center. But the cells of $B$ and $W$ are interleaved, so this needs to be done carefully.

Actually, here's an idea. Consider the "Manhattan distance from center" $d(i,j) = |i - 5.5| + |j - 5.5|$. Cells far from center (corners, edges) have high $d$, cells near center have low $d$.

On side $B$: assign high labels to high-$d$ cells (corners/edges) and low labels to low-$d$ cells (center).
On side $W$: assign low labels to high-$d$ cells and high labels to low-$d$ cells.

This way, at the corners (high $d$), $B$ has high labels and $W$ has low labels. At the center (low $d$), $B$ has low labels and $W$ has high labels. Since adjacent cells have similar $d$ values (differ by 1), the sum $f + g$ would be roughly balanced.

But this is just a heuristic. Let me try to compute the actual max edge sum for such an arrangement.

Hmm, this is getting quite involved. Let me try to think about the problem from the answer's perspective.

For competition problems of this type, the answer is often a "clean" number. Let me guess that the answer might be $S = 110$ or $S = 105$ or something like that.

Actually, let me think about a cleaner lower bound argument.

**Lower bound via "neighbor counting":**

Consider the numbers $100, 99, ..., 100-k+1$ (the top $k$ numbers). Each needs its neighbors to be small. Specifically, number $100-j$ needs all neighbors $\leq S - (100-j) = S - 100 + j$.

The total number of "neighbor slots" for these $k$ numbers is $\sum_{j=0}^{k-1} d(100-j)$, where $d$ is the degree. But neighbors can be shared (a cell can be neighbor to multiple high numbers).

In the grid, a cell can be adjacent to at most 4 high-number cells. But more importantly, the number of distinct cells that are neighbors of the top $k$ numbers is at least... well, it depends on the arrangement.

This is hard to bound in general. Let me try a different approach.

**Lower bound via "label counting" on one side:**

In the reformulated problem, consider side $B$. The vertex with label $m$ has all its neighbors on side $W$ with labels $\leq T - m$. 

For the vertex with label 50 (highest on $B$), placed at a corner (degree 2): 2 neighbors with labels $\leq T - 50$.
For the vertex with label 49, placed at a corner (degree 2): 2 neighbors with labels $\leq T - 49$.
For the vertex with label 48, placed at an edge (degree 3): 3 neighbors with labels $\leq T - 48$.
...

On side $W$, the number of vertices with labels $\leq m$ is exactly $m$. 

Now, the 2 neighbors of label-50 vertex need labels $\leq T - 50$. The 2 neighbors of label-49 vertex need labels $\leq T - 49$. These 4 cells are distinct (corners are far apart). So we need at least 2 labels $\leq T-50$ and 2 more labels $\leq T-49$ on side $W$.

But also, side $W$ has its own high labels (50, 49, ...) that need low-labeled neighbors on side $B$.

Let me think about the combined constraint. 

On side $W$, consider the labels assigned to the neighbors of $B$'s high-label vertices. These must be low. But side $W$ also has high-label vertices that need to be placed somewhere.

The key tension: side $W$ needs some vertices with low labels (to serve as neighbors of $B$'s high labels) and some vertices with high labels (which themselves need low-labeled neighbors on side $B$).

Let me think about a "budget" argument.

On side $W$:
- Some vertices need low labels (neighbors of high-$B$ vertices).
- Some vertices have high labels (and their neighbors on $B$ need low labels).

The vertices of $W$ that are neighbors of high-$B$ vertices are determined by the grid structure. The vertices of $W$ that have high labels are determined by our assignment.

To minimize $T$, we want the high-label $W$ vertices to NOT be neighbors of high-label $B$ vertices. In other words, the high labels on $B$ and $W$ should be "far apart" in the grid.

In the 10×10 grid, the maximum number of vertices that are pairwise at distance $\geq 3$ (so that their neighborhoods don't overlap) is related to the structure.

Hmm, this is getting complex. Let me try to just compute the answer for small cases and see if there's a pattern.

For a $2 \times 2$ grid: $S = 6$ (computed above). Reformulated: $T = S - 2 = 4$? Wait, let me redo. For $2 \times 2$, numbers 1-4. Split into {1,2} and {3,4}. Max edge sum = 2 + 4 = 6. In the reformulated problem with labels 1-2 on each side: max edge sum = 2 + 2 = 4. And $S = T + 2 = 6$. ✓ (since the split is {1,2} → labels {1,2} and {3,4} → labels {1,2} where 3→1, 4→2, so $S = T + 2$).

Wait, I need to be more careful. In the original problem, we split {1,...,2n} into two sets of size $n$. If we split into {1,...,n} and {n+1,...,2n}, then the labels on each side are {1,...,n} and {1,...,n} (after subtracting $n$ from the high side). The max edge sum in the original is $T + n$ where $T$ is the max edge sum in the reformulated problem.

For $2 \times 2$ ($n=2$): $T = 4$, $S = 4 + 2 = 6$. ✓

For a $2 \times 4$ grid: numbers 1-8, $n=4$. Color classes of size 4 each. The graph is a $2 \times 4$ grid. Let me think about the reformulated problem.

Actually, this is getting too complicated for hand computation. Let me think about the 10×10 case directly.

Let me try to think about what $T$ should be for the 10×10 grid.

**Approach: Think about the "bottleneck" — the highest-label vertex on each side.**

The vertex with label 50 on side $B$ (at a corner, degree 2) needs 2 neighbors with labels $\leq T - 50$.
The vertex with label 50 on side $W$ (at a corner, degree 2) needs 2 neighbors with labels $\leq T - 50$.

The 2 neighbors of $B$'s label-50 vertex are on side $W$, and the 2 neighbors of $W$'s label-50 vertex are on side $B$. These are independent constraints.

On side $W$: need 2 labels $\leq T - 50$. So $T - 50 \geq 2$, $T \geq 52$.
On side $B$: need 2 labels $\leq T - 50$. Same, $T \geq 52$.

Now, label 49 on side $B$ (at the other corner, degree 2): 2 neighbors on $W$ with labels $\leq T - 49$.
Label 49 on side $W$ (at the other corner, degree 2): 2 neighbors on $B$ with labels $\leq T - 49$.

On side $W$: need 2 labels $\leq T - 50$ (for $B$'s label 50) and 2 more labels $\leq T - 49$ (for $B$'s label 49). Total: 4 distinct cells, 2 with labels $\leq T-50$ and 2 more with labels $\leq T-49$. So need at least 4 labels $\leq T - 49$ on side $W$, giving $T - 49 \geq 4$, $T \geq 53$.

Similarly on side $B$: $T \geq 53$.

Continuing:
Label 48 on side $B$ (at an edge cell, degree 3): 3 neighbors on $W$ with labels $\leq T - 48$.
Label 48 on side $W$ (at an edge cell, degree 3): 3 neighbors on $B$ with labels $\leq T - 48$.

On side $W$: now need 2 (≤ T-50) + 2 (≤ T-49) + 3 (≤ T-48) = 7 distinct cells. But wait, some of these neighbor cells might overlap! The corner cells and edge cells might share neighbors.

Let me think about the grid structure. In the 10×10 grid:
- Corner $(1,1)$ (even, $B$): neighbors $(1,2)$ and $(2,1)$ (both odd, $W$).
- Corner $(10,10)$ (even, $B$): neighbors $(10,9)$ and $(9,10)$ (both odd, $W$).
- These are 4 distinct cells in $W$.

- Edge cell near corner, say $(1,3)$ (even, $B$): neighbors $(1,2), (1,4), (2,3)$ (all odd, $W$).
  - $(1,2)$ is shared with corner $(1,1)$!

So there IS overlap. The neighbor $(1,2)$ of corner $(1,1)$ is also a neighbor of edge cell $(1,3)$.

This means the counting is more nuanced. Let me think about it more carefully.

If we place label 50 at corner $(1,1)$ and label 48 at edge cell $(1,3)$, then $(1,2)$ is a common neighbor. The constraint on $(1,2)$ is $\leq \min(T - 50, T - 48) = T - 50$. So the shared neighbor just needs to satisfy the tighter constraint.

So the total number of distinct neighbor cells is less than the sum of degrees. Let me think about how to minimize the total number of distinct low-label cells needed.

To minimize overlap (and thus minimize the number of distinct low-label cells needed), we should spread the high-label vertices far apart. But to minimize $T$, we want to minimize the number of distinct low-label cells needed, which means we want MORE overlap.

Wait, no. More overlap means fewer distinct cells need low labels, which is good (we have more freedom). But the overlapping cells need to satisfy the tightest constraint.

Hmm, actually, the question is: what's the minimum number of distinct cells on side $W$ that need labels $\leq T - m$ for each $m$?

This depends on the placement of high-label vertices on side $B$.

Let me think about it differently. Let's say we place the top $k$ labels on side $B$ at specific cells. The union of their neighborhoods in $W$ is some set $N_k \subseteq W$. The constraint is:
- For each $b$ in the top $k$ with label $l(b)$, all neighbors of $b$ have labels $\leq T - l(b)$.

The tightest constraint on a cell $w \in N_k$ is $\leq T - \max_{b \sim w, b \in \text{top } k} l(b)$.

To minimize $T$, we want to:
1. Minimize $|N_k|$ (fewer cells need low labels).
2. Make the constraints as uniform as possible.

To minimize $|N_k|$, we should cluster the high-label vertices (so their neighborhoods overlap). But clustering high-label vertices means they're close together, which means they're in the same region of the grid.

But wait, the high-label vertices on $B$ and the high-label vertices on $W$ should be far apart (so that high labels on $B$ are adjacent to low labels on $W$ and vice versa). If we cluster high labels on $B$ in one corner, then the $W$ cells near that corner need low labels, and the $W$ cells far from that corner can have high labels.

Let me try a specific construction.

**Construction: "Corner-based"**

Place the highest labels on $B$ near corner $(1,1)$ and the highest labels on $W$ near corner $(10,10)$ (which is far from $(1,1)$).

Specifically:
- On side $B$ (even cells), assign labels in decreasing order as we move away from corner $(10,10)$ toward corner $(1,1)$. So the highest $B$ labels are near $(1,1)$.
- On side $W$ (odd cells), assign labels in decreasing order as we move away from corner $(1,1)$ toward corner $(10,10)$. So the highest $W$ labels are near $(10,10)$.

Wait, but $(10,10)$ is an even cell (in $B$), and $(1,1)$ is also even (in $B$). The $W$ corners are $(1,10)$ and $(10,1)$.

Let me reconsider. $B$ (even) corners: $(1,1)$ and $(10,10)$. $W$ (odd) corners: $(1,10)$ and $(10,1)$.

Place highest $B$ labels near $(1,1)$ and highest $W$ labels near $(10,1)$ (or $(1,10)$). The distance between $(1,1)$ and $(10,1)$ is 9, which is large. So high $B$ labels near $(1,1)$ and high $W$ labels near $(10,1)$ are far apart.

But this only uses two corners. What about the other two corners?

Actually, let me think about a different construction. 

**Construction: "Diagonal"**

On side $B$, assign label $k$ to the cell with the $k$-th largest "anti-diagonal sum" $i + j$ (or some similar ordering). On side $W$, assign label $k$ to the cell with the $k$-th smallest "anti-diagonal sum."

Hmm, this is getting complicated. Let me try to think about the problem from the answer.

Let me consider the problem from the perspective of a specific vertex. The center of the grid has cells with degree 4. A cell at position $(5,5)$ (even, $B$) has neighbors $(5,4), (5,6), (4,5), (6,5)$ (all odd, $W$). If this cell has label $l$, its neighbors need labels $\leq T - l$.

If $l$ is around 25 (middle label), then neighbors need labels $\leq T - 25$. If $T = 55$, neighbors need labels $\leq 30$, which is easy (most labels are $\leq 30$).

The binding constraints come from the high-label vertices. Let me focus on those.

**Let me try to compute a lower bound more carefully.**

Consider the top $k$ labels on side $B$: $50, 49, ..., 51-k$. These are placed at cells $b_1, b_2, ..., b_k$ (in some order). Their neighborhoods in $W$ are $N(b_1), ..., N(b_k)$.

For each $w \in \bigcup N(b_i)$, the label of $w$ must be $\leq T - \max\{l(b_i) : w \in N(b_i)\}$.

Now, similarly, the top $k$ labels on side $W$ are placed at cells $w_1, ..., w_k$, and their neighborhoods in $B$ impose constraints on $B$'s labels.

The key insight is: the cells in $W$ that are neighbors of high-$B$ cells need low labels, and the cells in $W$ that have high labels should NOT be neighbors of high-$B$ cells.

So we want: (high labels on $W$) ∩ (neighbors of high labels on $B$) = ∅.

The number of cells in $W$ that are neighbors of the top $k$ $B$-cells is $|\bigcup N(b_i)|$. The number of cells in $W$ with labels $> T - (51-k) = T - 51 + k$ is $50 - (T - 51 + k) = 101 - T - k$ (these are the cells that can be neighbors of the $(k+1)$-th highest $B$ label or higher... hmm, this isn't quite right).

Let me think about it differently.

**Clean lower bound argument:**

Let $T$ be the max edge sum in the reformulated problem. Consider the set of cells on side $B$ with labels $> T/2$. Call this set $B_{\text{high}}$. Similarly, $W_{\text{high}}$ = cells on side $W$ with labels $> T/2$.

If $b \in B_{\text{high}}$ and $w \in W_{\text{high}}$ are adjacent, then $l(b) + l(w) > T/2 + T/2 = T$, contradiction. So $B_{\text{high}}$ and $W_{\text{high}}$ have no edges between them.

The number of cells with labels $> T/2$ on each side is $50 - \lfloor T/2 \rfloor$.

Now, $B_{\text{high}}$ and $W_{\text{high}}$ are two sets with no edges between them. In the grid graph, what's the maximum $|B_{\text{high}}| + |W_{\text{high}}|$ such that there are no edges between them?

If there are no edges between $B_{\text{high}}$ and $W_{\text{high}}$, then $B_{\text{high}} \cup W_{\text{high}}$ is an independent set in the grid (since $B_{\text{high}} \subseteq B$ and $W_{\text{high}} \subseteq W$, and there are no edges within $B$ or within $W$, and no edges between $B_{\text{high}}$ and $W_{\text{high}}$). So $|B_{\text{high}}| + |W_{\text{high}}| \leq 50$ (max independent set).

This gives $2(50 - \lfloor T/2 \rfloor) \leq 50$, so $50 - \lfloor T/2 \rfloor \leq 25$, $\lfloor T/2 \rfloor \geq 25$, $T \geq 50$.

So $S \geq 50 + 50 = 100$. But we already knew $S \geq 102$ from the earlier argument (number 100 needs neighbors ≤ $S - 100$, and with degree ≥ 2, we need at least 2 numbers ≤ $S - 100$).

Let me combine the arguments. In the reformulated problem, the vertex with label 50 on side $B$ needs all neighbors to have labels $\leq T - 50$. If this vertex has degree $d$, we need $d$ labels $\leq T - 50$ on side $W$.

But also, the vertex with label 50 on side $W$ needs all neighbors (on side $B$) to have labels $\leq T - 50$.

Now, the $d$ neighbors of $B$'s label-50 vertex are on side $W$ with labels $\leq T - 50$. The label-50 vertex on side $W$ has label 50 > $T - 50$ (if $T < 100$). So the label-50 vertex on $W$ cannot be a neighbor of the label-50 vertex on $B$. More generally, any vertex on $W$ with label $> T - 50$ cannot be a neighbor of the label-50 vertex on $B$.

The number of $W$-vertices with labels $> T - 50$ is $50 - (T - 50) = 100 - T$.

These $100 - T$ vertices on $W$ must not be in the neighborhood of $B$'s label-50 vertex. The neighborhood has $d$ vertices. So $d \leq 50 - (100 - T) = T - 50$. Since $d \geq 2$ (minimum degree), $T - 50 \geq 2$, $T \geq 52$.

But we can do better. Consider the top $k$ labels on $B$: $50, 49, ..., 51-k$. Their neighborhoods in $W$ must avoid the top $100 - T + k - 1$ labels on $W$... hmm, this is getting complicated.

Let me try a cleaner approach.

**Clean approach:**

In the reformulated problem, let $T$ be the optimal max edge sum. 

For each $m = 1, ..., 50$, let $B_m = \{b \in B : l(b) \geq m\}$ and $W_m = \{w \in W : l(w) \geq m\}$. Then $|B_m| = |W_m| = 51 - m$.

If $b \in B_m$ and $w \in W_{T+1-m}$ are adjacent, then $l(b) + l(w) \geq m + (T+1-m) = T + 1 > T$, contradiction. So there are no edges between $B_m$ and $W_{T+1-m}$.

This means $B_m \cup W_{T+1-m}$ is an independent set, so $|B_m| + |W_{T+1-m}| \leq 50$.

$(51 - m) + (51 - (T+1-m)) \leq 50$
$(51 - m) + (50 - T + m) \leq 50$
$101 - T \leq 50$
$T \geq 51$.

So $T \geq 51$, giving $S \geq 101$. But we showed $S \geq 102$ earlier. Let me recheck.

Earlier: $S = 101$ means number 100 needs neighbors $\leq 1$. Degree $\geq 2$, but only one number (1) is $\leq 1$. So $S \geq 102$.

In the reformulated problem, $S = 101$ corresponds to $T = 51$ (since $S = T + 50$). The vertex with label 50 on side $B$ needs neighbors with labels $\leq 51 - 50 = 1$. Only one label (1) is $\leq 1$, but degree $\geq 2$. So $T \geq 52$, $S \geq 102$.

OK so the independent set argument gives $T \geq 51$, and the degree argument gives $T \geq 52$. Can we push further?

**Pushing further:**

Consider $B_{50}$ (the single vertex with label 50 on side $B$) and $W_{T-49}$ (vertices on $W$ with labels $\geq T - 49$). No edges between them. $|B_{50}| = 1$, $|W_{T-49}| = 50 - (T - 49) + 1 = 100 - T$.

The vertex in $B_{50}$ has degree $d \geq 2$. Its $d$ neighbors are in $W$ and not in $W_{T-49}$. So $d \leq 50 - |W_{T-49}| = 50 - (100 - T) = T - 50$. With $d = 2$ (corner), $T \geq 52$.

Now consider $B_{49}$ (vertices with labels $\geq 49$ on $B$, so 2 vertices) and $W_{T-48}$ (vertices with labels $\geq T - 48$ on $W$). No edges between them. $|B_{49}| = 2$, $|W_{T-48}| = 50 - (T - 48) + 1 = 99 - T$.

The 2 vertices in $B_{49}$ have total degree $\geq 2 + 2 = 4$ (both at corners). Their neighborhoods in $W$ are disjoint (corners are far apart) and avoid $W_{T-48}$. So the neighborhoods have at least 4 distinct vertices, all outside $W_{T-48}$. So $4 \leq 50 - |W_{T-48}| = 50 - (99 - T) = T - 49$. So $T \geq 53$.

Continuing: $B_{48}$ (3 vertices with labels $\geq 48$) and $W_{T-47}$ (vertices with labels $\geq T - 47$). $|B_{48}| = 3$, $|W_{T-47}| = 50 - (T - 47) + 1 = 98 - T$.

The 3 vertices in $B_{48}$: 2 at corners (degree 2 each) and 1 at an edge (degree 3). Total degree = 7. But neighborhoods might overlap.

If we place the 2 corners at $(1,1)$ and $(10,10)$ (far apart, no overlap) and the edge vertex at, say, $(1,3)$ (near corner $(1,1)$), then the neighborhood of $(1,3)$ includes $(1,2)$ which is also a neighbor of $(1,1)$. So overlap = 1, and distinct neighbors = 7 - 1 = 6.

But we want to MINIMIZE the number of distinct neighbors (to make the constraint easier to satisfy). Wait, no — we're proving a lower bound. We want to show that no matter how you place the high-label vertices, you need many distinct low-label neighbors.

For a lower bound, we want to show that the neighborhoods can't overlap too much. But actually, for a lower bound on $T$, we want to show that the number of distinct neighbors is LARGE (forcing many low labels, forcing $T$ to be large).

Hmm wait, I need to be more careful. The constraint is: the neighborhoods of $B_{48}$ must avoid $W_{T-47}$. The number of vertices in $W$ that are NOT in $W_{T-47}$ is $50 - (98 - T) = T - 48$. The neighborhoods of $B_{48}$ must fit within these $T - 48$ vertices. So the number of distinct neighbors of $B_{48}$ must be $\leq T - 48$.

To get a lower bound on $T$, we need a lower bound on the number of distinct neighbors of $B_{48}$, minimized over all possible placements of 3 vertices (2 corners + 1 edge) on side $B$.

To minimize the number of distinct neighbors, we should maximize overlap. Place the 2 corners at $(1,1)$ and $(1,3)$... wait, $(1,3)$ is not a corner. The $B$ corners are $(1,1)$ and $(10,10)$. These are far apart (distance 18), so no overlap.

The edge vertex (degree 3) should be placed to maximize overlap with the corners' neighborhoods. Place it at $(1,3)$ (edge, degree 3, neighbors $(1,2), (1,4), (2,3)$). Corner $(1,1)$ has neighbors $(1,2), (2,1)$. Overlap: $(1,2)$. So distinct neighbors = $2 + 2 + 3 - 1 = 6$.

Or place the edge vertex at $(2,2)$ (interior, degree 4, neighbors $(2,1), (2,3), (1,2), (3,2)$). Wait, $(2,2)$ is even, so it's in $B$. Its neighbors are $(2,1), (2,3), (1,2), (3,2)$, all odd ($W$). Corner $(1,1)$'s neighbors: $(1,2), (2,1)$. Overlap: $(1,2)$ and $(2,1)$. So distinct = $4 + 2 - 2 = 4$. But $(2,2)$ is interior (degree 4), not edge (degree 3). 

Hmm, I said the 3rd highest label goes to an edge cell (degree 3). But actually, we get to choose where to place labels. To minimize the number of distinct neighbors (for the lower bound, we want to show this can't be too small), we should consider the best possible placement.

Wait, I'm confusing myself. For the lower bound, I need to show that for ANY placement, the number of distinct neighbors is at least some value. But the placement is chosen by the optimizer to minimize $T$, so they would choose the placement that minimizes the number of distinct neighbors.

So for the lower bound: the minimum number of distinct neighbors of 3 $B$-vertices (2 corners + 1 non-corner) is achieved by placing them to maximize overlap. The 2 corners are fixed at $(1,1)$ and $(10,10)$ (the only $B$-corners). The 3rd vertex can be anywhere in $B$ (not a corner). To maximize overlap with corner $(1,1)$'s neighborhood $\{(1,2), (2,1)\}$, place the 3rd vertex adjacent to both $(1,2)$ and $(2,1)$. The vertex $(2,2)$ is adjacent to both $(1,2)$ and $(2,1)$ (and also $(2,3)$ and $(3,2)$). So placing the 3rd vertex at $(2,2)$ gives neighbors $\{(1,2), (2,1), (2,3), (3,2)\}$, with overlap 2 with corner $(1,1)$'s neighborhood. Distinct neighbors of all 3: $\{(1,2), (2,1)\} \cup \{(10,9), (9,10)\} \cup \{(1,2), (2,1), (2,3), (3,2)\} = \{(1,2), (2,1), (2,3), (3,2), (10,9), (9,10)\}$. That's 6.

But wait, $(2,2)$ is an interior cell (degree 4), not an edge cell (degree 3). I was assuming the 3rd highest label goes to a degree-3 cell, but actually, the optimizer can choose to put it at a degree-4 cell if that helps. Let me reconsider.

The optimizer wants to minimize $T$. They choose:
1. Which cells get the highest labels.
2. The assignment of labels to cells.

For the lower bound, I should consider the best possible strategy for the optimizer.

The optimizer would place the highest labels at the lowest-degree cells (corners, then edges) to minimize the number of neighbors that need low labels. But they might also consider overlap.

Let me reconsider. The 3 highest labels on $B$ are 50, 49, 48. The optimizer places them at 3 cells in $B$ to minimize the "cost." The cost is related to the number of distinct neighbors and the label constraints.

If placed at 2 corners + 1 interior near a corner:
- Corners $(1,1)$ and $(10,10)$: neighborhoods $\{(1,2),(2,1)\}$ and $\{(10,9),(9,10)\}$.
- Interior $(2,2)$: neighborhood $\{(1,2),(2,1),(2,3),(3,2)\}$.
- Union: $\{(1,2),(2,1),(2,3),(3,2),(10,9),(9,10)\}$, size 6.
- Constraints: $(1,2)$ and $(2,1)$ need labels $\leq \min(T-50, T-48) = T-50$ (since they're neighbors of both label 50 and label 48). $(2,3)$ and $(3,2)$ need labels $\leq T-48$. $(10,9)$ and $(9,10)$ need labels $\leq T-49$ (neighbors of label 49 only).

So we need: 2 labels $\leq T-50$, 2 more labels $\leq T-48$, 2 more labels $\leq T-49$ on side $W$. Total: 6 distinct cells, with 2 having labels $\leq T-50$.

But also, side $W$ has its own top 3 labels (50, 49, 48) that need low-label neighbors on side $B$. By symmetry, the same analysis applies.

Now, the constraint from $B$'s top 3 on $W$: 6 cells in $W$ need specific low labels. The remaining 44 cells in $W$ can have any labels, including the top labels 50, 49, 48.

But $W$'s top labels (50, 49, 48) need their neighbors on $B$ to have low labels. The neighbors of $W$'s top-label cells must avoid $B$'s top-label cells.

This is getting very involved. Let me try to just guess the answer and verify.

Let me think about what $T$ might be. 

For the 10×10 grid, the reformulated problem has labels 1-50 on each side. The grid has 180 edges (10×9 horizontal + 9×10 vertical = 90 + 90 = 180).

Let me think about a "checkerboard complementary" assignment. 

On side $B$ (even cells), assign label $f(i,j)$ based on position. On side $W$ (odd cells), assign label $g(i,j)$. We want $f(i,j) + g(i',j') \leq T$ for all adjacent $(i,j) \in B, (i',j') \in W$.

Idea: Use $f(i,j) = $ rank of $(i,j)$ in some ordering of $B$-cells, and $g(i,j) = 51 - $ rank of $(i,j)$ in the same ordering of $W$-cells. Then $f + g = 51$ for "corresponding" cells, but adjacent cells aren't corresponding.

Hmm, let me try a different idea. 

**Idea: "Row-complementary" assignment**

For each row $i$, the even cells and odd cells alternate. In row $i$, the even cells are at positions $j$ with $j \equiv i \pmod{2}$ (or $j \equiv i+1 \pmod{2}$, depending on convention).

Actually, let me think about a "snake" or "spiral" assignment.

**Idea: "Spiral" assignment**

Assign labels 1 to 50 on side $B$ in a spiral order (from outside in), and labels 1 to 50 on side $W$ in a reverse spiral order (from inside out). Then high labels on $B$ (outer) are adjacent to low labels on $W$ (outer), and low labels on $B$ (inner) are adjacent to high labels on $W$ (inner). The max sum would be at the "transition" point.

Hmm, this might not be optimal. Let me think more carefully.

**Idea: "Anti-diagonal" assignment**

Consider the anti-diagonal sum $s = i + j$. Cells with $s = 2$ (just $(1,1)$) to $s = 20$ (just $(10,10)$). 

On side $B$, assign high labels to cells with low $s$ (near $(1,1)$) and low labels to cells with high $s$ (near $(10,10)$). On side $W$, assign low labels to cells with low $s$ and high labels to cells with high $s$.

Then, adjacent cells have $s$ values differing by 1. A $B$-cell with $s = k$ has label roughly $r_B(k)$, and its $W$-neighbors have $s = k \pm 1$ with labels roughly $r_W(k \pm 1)$. We want $r_B(k) + r_W(k \pm 1) \leq T$.

If $r_B$ is decreasing and $r_W$ is increasing, then $r_B(k) + r_W(k+1) \leq r_B(k) + r_W(k) + \Delta$ where $\Delta$ is the increase per step. The maximum would be at the "crossover" point where $r_B(k) \approx r_W(k)$.

This is still vague. Let me try to think about the answer differently.

**Let me try to think about the problem as a linear program relaxation.**

Actually, let me just try to construct an explicit arrangement and compute $T$.

**Explicit construction:**

Let me try the following. On side $B$ (even cells), sort cells by $i + j$ (anti-diagonal) in increasing order, and assign labels 50, 49, ..., 1. On side $W$ (odd cells), sort cells by $i + j$ in increasing order, and assign labels 1, 2, ..., 50.

So $B$-cells with small $i+j$ get high labels, and $W$-cells with small $i+j$ get low labels.

For a $B$-cell at $(i,j)$ with $s = i+j$, its label is approximately $50 - \text{rank}_B(s)$. For a $W$-cell at $(i',j')$ with $s' = i'+j'$, its label is approximately $\text{rank}_W(s')$.

Adjacent cells have $s$ values differing by 1. A $B$-cell with $s = k$ is adjacent to $W$-cells with $s = k-1$ and $s = k+1$.

The $W$-cell with $s = k+1$ has label $\text{rank}_W(k+1) \approx \text{rank}_W(k) + (\text{number of } W\text{-cells with } s = k+1)$. Hmm, this depends on the distribution of cells across anti-diagonals.

Let me count. For the 10×10 grid, the anti-diagonal $s = i + j$ ranges from 2 to 20. The number of cells with $s = k$ is $\min(k-1, 21-k, 10)$ for $k = 2, ..., 20$.

$s=2$: 1 cell, $s=3$: 2, $s=4$: 3, ..., $s=11$: 10, $s=12$: 9, ..., $s=20$: 1.

Even $s$ (B-cells): $s = 2, 4, 6, 8, 10, 12, 14, 16, 18, 20$.
Counts: 1, 3, 5, 7, 9, 9, 7, 5, 3, 1. Total = 1+3+5+7+9+9+7+5+3+1 = 50. ✓

Odd $s$ (W-cells): $s = 3, 5, 7, 9, 11, 13, 15, 17, 19$.
Counts: 2, 4, 6, 8, 10, 8, 6, 4, 2. Total = 2+4+6+8+10+8+6+4+2 = 50. ✓

Now, on side $B$, assign labels in decreasing order of $s$ (so $s=20$ gets label 1, $s=18$ gets labels 2,3,4, etc.). Wait, I said small $s$ gets high labels. So $s=2$ gets label 50, $s=4$ gets labels 47,48,49, etc.

Actually, let me be more precise. On side $B$, cells with $s=2$ get the highest label (50), cells with $s=4$ get the next 3 highest (47, 48, 49), cells with $s=6$ get the next 5 highest (42, 43, 44, 45, 46), etc.

On side $W$, cells with $s=3$ get the lowest labels (1, 2), cells with $s=5$ get the next 4 (3, 4, 5, 6), etc.

Now, a $B$-cell with $s = k$ is adjacent to $W$-cells with $s = k-1$ and $s = k+1$.

The $B$-cell with $s=2$ (label 50) is adjacent to $W$-cells with $s=1$ (none) and $s=3$ (labels 1, 2). So the max sum involving this cell is $50 + 2 = 52$.

The $B$-cells with $s=4$ (labels 47, 48, 49) are adjacent to $W$-cells with $s=3$ (labels 1, 2) and $s=5$ (labels 3, 4, 5, 6). Max sum: $49 + 6 = 55$.

The $B$-cells with $s=6$ (labels 42-46) are adjacent to $W$-cells with $s=5$ (labels 3-6) and $s=7$ (labels 7-12). Max sum: $46 + 12 = 58$.

The $B$-cells with $s=8$ (labels 35-41) are adjacent to $W$-cells with $s=7$ (labels 7-12) and $s=9$ (labels 13-20). Max sum: $41 + 20 = 61$.

The $B$-cells with $s=10$ (labels 26-34) are adjacent to $W$-cells with $s=9$ (labels 13-20) and $s=11$ (labels 21-30). Max sum: $34 + 30 = 64$.

The $B$-cells with $s=12$ (labels 17-25) are adjacent to $W$-cells with $s=11$ (labels 21-30) and $s=13$ (labels 31-38). Max sum: $25 + 38 = 63$.

The $B$-cells with $s=14$ (labels 10-16) are adjacent to $W$-cells with $s=13$ (labels 31-38) and $s=15$ (labels 39-44). Max sum: $16 + 44 = 60$.

The $B$-cells with $s=16$ (labels 5-9) are adjacent to $W$-cells with $s=15$ (labels 39-44) and $s=17$ (labels 45-48). Max sum: $9 + 48 = 57$.

The $B$-cells with $s=18$ (labels 2-4) are adjacent to $W$-cells with $s=17$ (labels 45-48) and $s=19$ (labels 49-50). Max sum: $4 + 50 = 54$.

The $B$-cell with $s=20$ (label 1) is adjacent to $W$-cells with $s=19$ (labels 49-50). Max sum: $1 + 50 = 51$.

So the maximum over all is $\max(52, 55, 58, 61, 64, 63, 60, 57, 54, 51) = 64$.

But wait, this is a rough calculation. The actual max depends on the specific assignment within each anti-diagonal. The max sum for $s=10$ is $34 + 30 = 64$, but this assumes the worst-case pairing within the anti-diagonal. With a careful assignment, we might do better.

But also, this construction gives $T \approx 64$, so $S \approx 114$. This seems high. Let me see if there's a better construction.

The issue is that the anti-diagonal ordering creates a "gradient" that's too steep in the middle. The max occurs at $s = 10/11$ where both sides have moderate-to-high labels.

**Better idea: "Complementary within anti-diagonals"**

Instead of assigning high labels to low-$s$ $B$-cells and low labels to low-$s$ $W$-cells, what if we interleave more carefully?

Actually, the problem with the above construction is that in the middle of the grid, both $B$ and $W$ cells have moderate labels, and their sums are high. We need a different approach.

**Idea: "Chessboard reversal"**

What if on side $B$, we assign labels in order of $i + j$ (increasing), and on side $W$, we assign labels in order of $i + j$ (decreasing)? Then $B$-cells with small $s$ get low labels, and $W$-cells with small $s$ get high labels. 

$B$-cell with $s=2$ (label 1) adjacent to $W$-cells with $s=3$ (labels 49, 50). Max sum: $1 + 50 = 51$.
$B$-cells with $s=4$ (labels 2, 3, 4) adjacent to $W$-cells with $s=3$ (labels 49, 50) and $s=5$ (labels 45-48). Max sum: $4 + 50 = 54$.

Hmm, this is the same as before but reversed. The max would still be around 64.

The problem is that the anti-diagonal approach creates a gradient, and the max sum is at the point where the two gradients cross.

**Idea: "2D complementary"**

Instead of a 1D gradient (along $i+j$), use a 2D pattern. For example, on side $B$, assign high labels to cells where both $i$ and $j$ are small (corner $(1,1)$ region), and on side $W$, assign high labels to cells where both $i$ and $j$ are large (corner $(10,10)$ region).

But this is essentially the same as the anti-diagonal approach.

**Idea: "Interleaved" assignment**

What if we don't use a gradient at all, but instead interleave high and low labels in a checkerboard-like pattern within each color class?

For example, on side $B$, assign labels such that high labels are surrounded by low labels on side $W$, and vice versa. This is essentially what we want, but the grid structure constrains how we can do this.

Let me think about the problem differently. 

**Reformulation as a graph coloring problem:**

We want to find a bijection $f: B \to \{1,...,50\}$ and $g: W \to \{1,...,50\}$ minimizing $\max_{(b,w) \in E} (f(b) + g(w))$.

This is equivalent to: find the minimum $T$ such that there exist bijections $f, g$ with $f(b) + g(w) \leq T$ for all $(b,w) \in E$.

This is a kind of "bipartite bandwidth" or "labeling" problem.

**Lower bound via edge counting:**

The grid has 180 edges. The sum of all edge sums is $\sum_{(b,w) \in E} (f(b) + g(w)) = \sum_{b \in B} f(b) \cdot d(b) + \sum_{w \in W} g(w) \cdot d(w)$.

To minimize the max edge sum, we'd like the edge sums to be as uniform as possible. The average edge sum is $\frac{\sum_{b} f(b) d(b) + \sum_{w} g(w) d(w)}{180}$.

$\sum_{b} f(b) d(b)$: to minimize this, assign low labels to high-degree cells. $\sum_{w} g(w) d(w)$: same.

The minimum of $\sum_{b} f(b) d(b)$ is achieved by assigning label 1 to the highest-degree cell, label 2 to the next, etc. (rearrangement inequality).

Degree distribution on each side: 2 cells of degree 2, 16 of degree 3, 32 of degree 4.

$\sum_{b} f(b) d(b)$: assign labels 1-32 to degree-4 cells, labels 33-48 to degree-3 cells, labels 49-50 to degree-2 cells.
$= 4 \cdot (1+2+...+32) + 3 \cdot (33+34+...+48) + 2 \cdot (49+50)$
$= 4 \cdot 528 + 3 \cdot 612 + 2 \cdot 99$
$= 2112 + 1836 + 198 = 4146$.

Similarly, $\sum_{w} g(w) d(w) = 4146$ (same degree distribution).

Total edge sum = $4146 + 4146 = 8292$. Average = $8292 / 180 = 46.07$.

So the average edge sum is about 46, meaning the max is at least 47 (since max ≥ average, and max must be an integer). But this is a weak bound.

**Better lower bound:**

Let me think about the "local" structure. Consider a cell $b$ with degree 4 (interior). It has 4 neighbors in $W$. The sum of the 4 edge sums is $4 f(b) + g(w_1) + g(w_2) + g(w_3) + g(w_4)$. The max of these 4 sums is at least $\frac{4 f(b) + g(w_1) + ... + g(w_4)}{4}$.

If $f(b) = 50$ (highest label) and $b$ is interior (degree 4), the 4 neighbors have labels summing to at least $1+2+3+4 = 10$ (if they're the 4 lowest). The max edge sum is at least $(4 \cdot 50 + 10) / 4 = 52.5$, so at least 53.

But we'd place label 50 at a corner (degree 2), not interior. So this doesn't directly apply.

Let me think about the problem more carefully.

**Let me try to find the answer by considering the structure more carefully.**

I'll think about what happens with the "complementary" assignment where we try to make $f(b) + g(w) \approx T$ for all edges.

If we could achieve $f(b) + g(w) = T$ for all edges, that would be ideal. But this is generally impossible due to the graph structure.

For a path graph $P_n$ (1×n grid), the optimal $T$ in the reformulated problem (with $n/2$ labels on each side, assuming $n$ even) can be computed. But the 10×10 grid is more complex.

Let me try a different approach: think about the problem as an integer program and try to find the answer by reasoning about the constraints.

**Key constraint:** For each edge $(b,w)$, $f(b) + g(w) \leq T$. This means $g(w) \leq T - f(b)$ for all neighbors $b$ of $w$, i.e., $g(w) \leq T - \max_{b \sim w} f(b)$. Similarly, $f(b) \leq T - \max_{w \sim b} g(w)$.

So if we define $F(b) = f(b)$ and $G(w) = g(w)$, then:
$G(w) \leq T - \max_{b \sim w} F(b)$ for all $w \in W$.
$F(b) \leq T - \max_{w \sim b} G(w)$ for all $b \in B$.

This is a system of constraints. The question is: what's the minimum $T$ for which there exist bijections $F: B \to \{1,...,50\}$ and $G: W \to \{1,...,50\}$ satisfying these?

Let me think about a "harmonic" or "fixed point" approach. If we set $F(b) = T - \max_{w \sim b} G(w)$ and $G(w) = T - \max_{b \sim w} F(b)$, we get a system that might have a solution.

This is related to the concept of "graph coloring" where the label of each vertex is determined by its neighbors' labels.

Let me try a specific construction.

**Construction: "Row-alternating"**

Divide the grid into two halves: top 5 rows and bottom 5 rows. On side $B$, assign high labels (26-50) to the top half and low labels (1-25) to the bottom half. On side $W$, assign low labels (1-25) to the top half and high labels (26-50) to the bottom half.

Each half has 25 $B$-cells and 25 $W$-cells.

In the top half: $B$-cells have labels 26-50, $W$-cells have labels 1-25. Max edge sum within top half: $50 + 25 = 75$. That's bad.

The boundary between top and bottom halves (between rows 5 and 6): $B$-cells in row 5 have labels 26-50, $W$-cells in row 6 have labels 26-50. Edge sum: up to $50 + 50 = 100$. Even worse.

This doesn't work. The problem is that at the boundary, both sides have high labels.

**Construction: "Finer interleaving"**

What if we interleave at a finer scale? For example, alternate high and low labels in a checkerboard pattern within each color class.

But within a color class, cells are not adjacent (they're on the same side of the bipartition), so we can freely assign labels. The constraint is only between the two color classes.

Let me think about the "dual" problem. We want to find a permutation $\sigma$ of $\{1,...,50\}$ (for $B$) and $\tau$ of $\{1,...,50\}$ (for $W$) such that $\sigma(b) + \tau(w) \leq T$ for all edges $(b,w)$.

Equivalently, $\tau(w) \leq T - \sigma(b)$ for all $b \sim w$, i.e., $\tau(w) \leq T - \max_{b \sim w} \sigma(b)$.

So $\tau(w) \leq T - M(w)$ where $M(w) = \max_{b \sim w} \sigma(b)$.

For $\tau$ to be a bijection onto $\{1,...,50\}$, we need $\max_w \tau(w) = 50$, so $50 \leq T - \min_w M(w)$, i.e., $T \geq 50 + \min_w M(w)$.

Also, the number of $w$'s with $\tau(w) \leq T - M(w)$ must be at least 50 (since $\tau$ is a bijection, all 50 values must be assigned). Actually, $\tau(w) \leq T - M(w)$ for each $w$, and $\tau$ is a bijection, so we need the values $\{1,...,50\}$ to be assignable to the 50 $w$'s such that $\tau(w) \leq T - M(w)$. This is possible iff for each $k$, the number of $w$'s with $T - M(w) \geq k$ is at least $51 - k$ (i.e., at least $51 - k$ $w$'s can take values $\geq k$). 

Actually, the condition is: for each $k \in \{1,...,50\}$, the number of $w$'s with $T - M(w) \geq k$ is at least the number of values in $\{k, k+1, ..., 50\}$ that need to be assigned, which is $51 - k$. But actually, it's a standard matching condition: we can assign values to $w$'s such that $\tau(w) \leq T - M(w)$ iff for every $k$, $|\{w : T - M(w) \geq k\}| \geq 51 - k$.

Equivalently, $|\{w : M(w) \leq T - k\}| \geq 51 - k$ for all $k = 1, ..., 50$.

Let $m = T - k$, so $k = T - m$, and the condition becomes: $|\{w : M(w) \leq m\}| \geq 51 - (T - m) = m + 51 - T$ for all $m$ (where $k$ ranges from 1 to 50, so $m$ ranges from $T - 50$ to $T - 1$).

For $m < T - 50$: the condition is $|\{w : M(w) \leq m\}| \geq m + 51 - T$, but $m + 51 - T \leq 0$, so the condition is trivially satisfied.

For $m \geq T - 50$ (and $m \leq T - 1$): $|\{w : M(w) \leq m\}| \geq m + 51 - T$.

For $m \geq 50$: $|\{w : M(w) \leq m\}| = 50 \geq m + 51 - T$ iff $T \geq m + 1$, which is satisfied for $m \leq T - 1$.

So the binding constraints are for $m$ in $\{T - 50, ..., 49\}$ (assuming $T \geq 51$): $|\{w : M(w) \leq m\}| \geq m + 51 - T$.

Now, $M(w) = \max_{b \sim w} \sigma(b)$, and $\sigma$ is a bijection from $B$ to $\{1,...,50\}$. The function $M(w)$ depends on the assignment $\sigma$.

To minimize $T$, we want to choose $\sigma$ to make $M(w)$ as small as possible for as many $w$'s as possible. But $M(w) = \max_{b \sim w} \sigma(b)$, so to make $M(w)$ small, we need all neighbors of $w$ to have small $\sigma$ values. But each $b$ is a neighbor of multiple $w$'s, so there's a trade-off.

This is essentially the same problem from the other direction. Let me try to think about specific values.

**Symmetric construction attempt:**

Let me try to construct an assignment where $f(b) + g(w) \leq T$ for a specific $T$, and find the minimum such $T$.

Let me try $T = 55$ (so $S = 105$).

We need $f(b) + g(w) \leq 55$ for all edges. So $g(w) \leq 55 - f(b)$ for all $b \sim w$, i.e., $g(w) \leq 55 - \max_{b \sim w} f(b)$.

If $f(b) = 50$ (at a corner, degree 2), its 2 neighbors need $g \leq 5$.
If $f(b) = 49$ (at a corner, degree 2), its 2 neighbors need $g \leq 6$.
If $f(b) = 48$ (at an edge, degree 3), its 3 neighbors need $g \leq 7$.
...

And similarly for $g$'s high values.

Let me think about whether $T = 55$ is achievable.

On side $B$, the top labels and their neighbor constraints:
- Label 50 (corner, deg 2): 2 neighbors need $g \leq 5$.
- Label 49 (corner, deg 2): 2 neighbors need $g \leq 6$.
- Label 48 (edge, deg 3): 3 neighbors need $g \leq 7$.
- Label 47 (edge, deg 3): 3 neighbors need $g \leq 8$.
- ...

On side $W$, the top labels and their neighbor constraints:
- Label 50 (corner, deg 2): 2 neighbors need $f \leq 5$.
- Label 49 (corner, deg 2): 2 neighbors need $f \leq 6$.
- Label 48 (edge, deg 3): 3 neighbors need $f \leq 7$.
- ...

Now, the $W$-cells that are neighbors of $B$'s label-50 cell need $g \leq 5$. There are 2 such cells. The $W$-cells that have $g = 50, 49, 48, ..., 46$ (5 cells) must NOT be among these 2 cells (since $50, 49, 48, 47, 46 > 5$). Similarly, the $W$-cells with $g \geq 46$ must not be neighbors of $B$'s label-50 cell.

Also, the $W$-cells with $g \geq 45$ must not be neighbors of $B$'s label-49 cell (since $45 > 6$). Wait, $g \leq 6$ for neighbors of label 49, so $g \geq 7$ can't be a neighbor. So $W$-cells with $g \geq 7$ must not be neighbors of $B$'s label-49 cell.

Let me think about this more carefully. The $W$-cells with high $g$ values must be far from the $B$-cells with high $f$ values.

Let me try to place the high-$f$ $B$-cells in the top-left corner and the high-$g$ $W$-cells in the bottom-right corner.

$B$-corners: $(1,1)$ and $(10,10)$. $W$-corners: $(1,10)$ and $(10,1)$.

Place $f = 50$ at $B$-corner $(1,1)$ (neighbors: $(1,2), (2,1)$ in $W$).
Place $f = 49$ at $B$-corner $(10,10)$ (neighbors: $(10,9), (9,10)$ in $W$).
Place $g = 50$ at $W$-corner $(10,1)$ (neighbors: $(10,2), (9,1)$ in $B$).
Place $g = 49$ at $W$-corner $(1,10)$ (neighbors: $(1,9), (2,10)$ in $B$).

Check: $f(1,1) = 50$, neighbors $(1,2)$ and $(2,1)$ need $g \leq 5$.
$g(10,1) = 50$, neighbors $(10,2)$ and $(9,1)$ need $f \leq 5$.

Are $(1,2)$ or $(2,1)$ the same as $(10,1)$? No. Good.

Now, $(1,2)$ and $(2,1)$ need $g \leq 5$. $(10,2)$ and $(9,1)$ need $f \leq 5$.

$f = 49$ at $(10,10)$: neighbors $(10,9), (9,10)$ need $g \leq 6$.
$g = 49$ at $(1,10)$: neighbors $(1,9), (2,10)$ need $f \leq 6$.

So on side $W$: $(1,2), (2,1)$ need $g \leq 5$, and $(10,9), (9,10)$ need $g \leq 6$. These are 4 distinct cells. We need 2 labels $\leq 5$ and 2 more labels $\leq 6$.

On side $B$: $(10,2), (9,1)$ need $f \leq 5$, and $(1,9), (2,10)$ need $f \leq 6$. 4 distinct cells. We need 2 labels $\leq 5$ and 2 more labels $\leq 6$.

This seems feasible so far. Let me continue.

$f = 48$ at some $B$-edge cell. Which edge cell? It should be far from the high-$g$ $W$-cells. The high-$g$ $W$-cells are near $(10,1)$ and $(1,10)$. So place $f = 48$ near $(1,1)$, say at $(1,3)$ (edge, degree 3, neighbors $(1,2), (1,4), (2,3)$ in $W$).

$(1,2)$ already needs $g \leq 5$ (from $f=50$). Now also $g \leq 55 - 48 = 7$. The binding constraint is $g \leq 5$.
$(1,4)$ and $(2,3)$ need $g \leq 7$.

$g = 48$ at some $W$-edge cell, far from high-$f$ $B$-cells. Place near $(10,1)$, say at $(10,3)$ (edge, degree 3, neighbors $(10,2), (10,4), (9,3)$ in $B$).

$(10,2)$ already needs $f \leq 5$. Now also $f \leq 7$. Binding: $f \leq 5$.
$(10,4)$ and $(9,3)$ need $f \leq 7$.

Continuing:
$f = 47$ at $(1,5)$ (edge, deg 3, neighbors $(1,4), (1,6), (2,5)$). $(1,4)$ needs $g \leq \min(7, 8) = 7$. $(1,6), (2,5)$ need $g \leq 8$.

$g = 47$ at $(10,5)$ (edge, deg 3, neighbors $(10,4), (10,6), (9,5)$). $(10,4)$ needs $f \leq \min(7, 8) = 7$. $(10,6), (9,5)$ need $f \leq 8$.

$f = 46$ at $(1,7)$ (edge, deg 3, neighbors $(1,6), (1,8), (2,7)$). $(1,6)$ needs $g \leq \min(8, 9) = 8$. $(1,8), (2,7)$ need $g \leq 9$.

$g = 46$ at $(10,7)$ (edge, deg 3, neighbors $(10,6), (10,8), (9,7)$). $(10,6)$ needs $f \leq \min(8, 9) = 8$. $(10,8), (9,7)$ need $f \leq 9$.

$f = 45$ at $(1,9)$ (edge, deg 3, neighbors $(1,8), (1,10), (2,9)$). But $(1,10)$ is a $W$-corner with $g = 49$. Check: $f(1,9) + g(1,10) = 45 + 49 = 94 > 55$. BAD!

So we can't place $f = 45$ at $(1,9)$ because it's adjacent to $g = 49$ at $(1,10)$.

The constraint is $f(1,9) \leq 55 - 49 = 6$. So $(1,9)$ must have $f \leq 6$. But we already said $(1,9)$ needs $f \leq 6$ (from $g = 49$ at $(1,10)$). So $(1,9)$ has $f \leq 6$, which is fine—it's a low-$f$ cell.

So the high-$f$ cells near $(1,1)$ can only go up to the cells that aren't adjacent to high-$g$ cells near $(1,10)$.

The $W$-corner $(1,10)$ has $g = 49$, and its $B$-neighbors are $(1,9)$ and $(2,10)$. These need $f \        — AI历史解题过程（thinking）
#   polymath_00811         — 题目ID

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
  <problem_id>polymath_00811</problem_id>
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

The numbers from $1$ to $100$ are arranged in a $10\times 10$ table so that any two adjacent numbers have sum no larger than $S$. Find the least value of $S$ for which this is possible.
[i]D. Hramtsov[/i]

## Standard Solution

1. **Understanding the Problem:**
   We need to arrange the numbers from \(1\) to \(100\) in a \(10 \times 10\) table such that the sum of any two adjacent numbers is no larger than \(S\). We aim to find the smallest possible value of \(S\).

2. **Initial Consideration:**
   Let's consider the largest number \(x\) such that there are \(5\) numbers from \(x\) to \(100\) in the same row or column. We know that \(x \geq 60\), implying that none of \(x, x+1, \ldots, 100\) are adjacent to one another.

3. **Coloring Argument:**
   - Color the numbers \(x, x+1, \ldots, 100\) red.
   - Color all squares neighboring any of these red squares blue.

4. **Lemma:**
   Any row has at least as many blue squares as red squares.
   - **Proof:** This can be shown by simple casework. If a row has \(r\) red squares, then each red square must have at least one blue neighbor in the same row, ensuring that the number of blue squares is at least \(r\).

5. **Deficient Rows:**
   - Define a row as **deficient** if it has the same number of red and blue squares.
   - Claim: There cannot be two adjacent deficient rows.
   - **Proof by Contradiction:**
     - Suppose there are two adjacent deficient rows \(r_1\) and \(r_2\).
     - Let \(R_1, B_1\) be the sets of red and blue squares in \(r_1\), and \(R_2, B_2\) be the sets of red and blue squares in \(r_2\).
     - The squares under \(R_1\) must be in \(R_2 \cup B_2\), and the squares above \(R_2\) must be in \(R_1 \cup B_1\).
     - Since \(R_1\) and \(R_2\) are deficient, \(|R_1| = |B_1| = |R_2| = |B_2|\).
     - This implies \(R_1 = B_2\) and \(R_2 = B_1\), leading to a contradiction.

6. **Counting Blue Squares:**
   - There are at most \(5\) deficient rows.
   - Therefore, there are at least \(100 - x + 1 + 5 = 106 - x\) blue squares.

7. **Conclusion:**
   - One of these blue squares is at least \(106 - x\).
   - Adding this blue square with its neighbor gives a sum of at least \(106\).

Thus, the least value of \(S\) for which this arrangement is possible is \(106\).

The final answer is \(\boxed{106}\).

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We need to arrange numbers 1 to 100 in a 10×10 grid such that any two adjacent numbers (sharing an edge) have sum ≤ S. Find the minimum S.

First, let me check for answer leaks. The problem statement is clean - just the problem, author attribution, and constraints. No leaked answers.

Now let me solve this.

**Lower bound:**

Consider the largest numbers. The key insight is about the structure of the grid and which numbers must be adjacent.

The grid is a 10×10 grid graph. It has a maximum independent set. The grid graph 10×10 is bipartite (checkerboard coloring). One color class has 50 cells, the other has 50 cells.

In a bipartite graph, if we put the 50 largest numbers (51-100) on one color class and the 50 smallest (1-50) on the other, then every edge connects a large number to a small number. The maximum sum would be maximized when the largest number (100) is adjacent to the largest possible small number.

But we want to minimize the maximum sum. So we need to think about what's forced.

Let me think about this differently. Consider the 50 cells of one color (say black) and 50 cells of the other color (white). Every edge connects a black cell to a white cell. If we place numbers 51-100 on black cells and 1-50 on white cells, then every adjacent pair has one from {51,...,100} and one from {1,...,50}.

The maximum sum would be max over edges of (black_value + white_value). We want to minimize this maximum.

Actually, let's think about it more carefully. We don't have to put 51-100 on one color and 1-50 on the other. But intuitively, to minimize the maximum adjacent sum, we want large numbers adjacent to small numbers.

Let me think about the lower bound first.

**Lower bound argument:**

Consider the numbers 91, 92, ..., 100 (the top 10 numbers). Each of these has degree at least 2 (corner cells have degree 2, edge cells have degree 3, interior cells have degree 4). Actually, we need to think about how many "large" numbers can be placed in non-adjacent positions.

The maximum independent set of the 10×10 grid is 50 (one color class). So we can place at most 50 numbers such that no two are adjacent. 

If we place the 50 largest numbers (51-100) all on one color class, they're pairwise non-adjacent. Then the 50 smallest (1-50) go on the other color class. Every edge connects a number from {51,...,100} to a number from {1,...,50}.

The question is: what's the minimum possible maximum edge sum?

For a number $a$ in {51,...,100} placed at some cell, it's adjacent to some cells in the other color class. The sum $a + b$ where $b$ is the largest neighbor of $a$.

To minimize the maximum sum, we want to pair large numbers with small neighbors. 

Let me think about this as an optimization problem. We have a bipartite graph $G = (B, W, E)$ where $|B| = |W| = 50$. We assign values $\{51, ..., 100\}$ to $B$ and $\{1, ..., 50\}$ to $W$ (or some other split). We want to minimize $\max_{(b,w) \in E} (val(b) + val(w))$.

Actually, we don't even need to split it this way. Let me think about what the optimal split is.

Hmm, let me think about lower bounds more carefully.

**Lower bound via counting:**

Consider any arrangement. Look at the 10 largest numbers: 91, 92, ..., 100. 

Actually, let me think about a cleaner approach. 

Consider the set of numbers $\{k+1, k+2, ..., 100\}$ for some threshold $k$. These are the $100-k$ largest numbers. In the grid, the maximum number of pairwise non-adjacent cells is 50. So if $100 - k > 50$, i.e., $k < 50$, then at least two of these large numbers must be adjacent. But that doesn't directly give us a bound on the sum.

Let me think differently. 

**Key idea:** Consider the numbers $a_1 > a_2 > ... > a_{100}$ (so $a_i = 101 - i$). We want to find the minimum $S$ such that we can arrange them so adjacent sums ≤ S.

Let me think about what numbers must be adjacent to the largest numbers.

Number 100 has degree $d$ (2, 3, or 4 depending on position). Its neighbors must all be ≤ $S - 100$.

Number 99: if not adjacent to 100, its neighbors must be ≤ $S - 99$. If adjacent to 100, then $100 + 99 = 199 ≤ S$ is needed, which would be bad.

So we want 100 and 99 to not be adjacent. More generally, we want large numbers to be non-adjacent to each other.

The maximum independent set is 50. So we can place at most 50 numbers pairwise non-adjacent. 

If we place numbers 51-100 on one color class (50 cells, pairwise non-adjacent), and 1-50 on the other, then every edge sum is at most $100 + 50 = 150$ and at least $51 + 1 = 52$. But can we do better than 150?

The maximum edge sum in this arrangement depends on the specific assignment. We want to minimize the maximum edge sum.

Let me think about it as: we have a bipartite graph. On one side (B, 50 cells), we place numbers from some set $X$ of 50 numbers. On the other side (W, 50 cells), we place numbers from the complement $Y$. We want to minimize the maximum edge sum.

To minimize the maximum edge sum, we should put large numbers on one side and small on the other. So $X = \{51, ..., 100\}$ and $Y = \{1, ..., 50\}$ (or vice versa).

Now, within this, we need to assign specific numbers to specific cells to minimize the maximum edge sum.

The maximum edge sum is $\max_{(b,w) \in E} (f(b) + g(w))$ where $f: B \to \{51,...,100\}$ and $g: W \to \{1,...,50\}$ are bijections.

To minimize this, we want: if $f(b)$ is large, then $g(w)$ should be small for all neighbors $w$ of $b$.

This is related to the structure of the grid graph.

Let me think about the degrees. In the 10×10 grid:
- 4 corner cells: degree 2
- 32 edge cells (non-corner): degree 3
- 64 interior cells: degree 4

In each color class (50 cells):
- 2 corner cells, 16 edge cells, 32 interior cells (one color)
- 2 corner cells, 16 edge cells, 32 interior cells (other color)

Wait, let me recount. The 10×10 grid has positions $(i,j)$ for $1 \le i,j \le 10$. Color = $(i+j) \mod 2$.

Corner cells: $(1,1), (1,10), (10,1), (10,10)$. Colors: $(1+1)=2$ even, $(1+10)=11$ odd, $(10+1)=11$ odd, $(10+10)=20$ even. So 2 corners are even, 2 are odd.

Edge cells (non-corner): cells on the boundary but not corners. There are $4 \times 8 = 32$ such cells. By symmetry, 16 are even and 16 are odd.

Interior cells: $8 \times 8 = 64$ cells. 32 even, 32 odd.

So each color class has: 2 corners (degree 2), 16 edge (degree 3), 32 interior (degree 4). Total = 50. ✓

Now, the cell with the highest value (100) should be placed where it has the fewest neighbors and those neighbors can be made small. A corner cell has only 2 neighbors. So place 100 at a corner.

If 100 is at a corner (say $(1,1)$, which is even color), its neighbors are $(1,2)$ and $(2,1)$, both odd color. These get values from $\{1,...,50\}$. To minimize the max sum involving 100, we'd want these to be as small as possible, say 1 and 2. Then the sums are 101 and 102.

But we also need to consider 99. If 99 is also at a corner of the same color class (even), say $(10,10)$, its neighbors are $(10,9)$ and $(9,10)$, both odd. We'd want these to be small too, say 3 and 4. Sums: 102, 103.

Continuing, 98 at another even corner... but there are only 2 even corners. So 98 goes to an edge cell (degree 3) or interior cell (degree 4).

This is getting complex. Let me think about it more carefully as an optimization problem.

Actually, let me think about a cleaner lower bound argument.

**Lower bound argument:**

Consider the 50 largest numbers $\{51, 52, ..., 100\}$. In any arrangement, consider the set of cells containing these numbers. Since the maximum independent set is 50, it's possible that these 50 cells form an independent set (one color class). But if they don't, some pair of them is adjacent, giving a sum ≥ 51 + 52 = 103.

But even if they form an independent set, each of these cells is adjacent to cells containing numbers from $\{1, ..., 50\}$.

Let me think about the problem differently. 

Consider any valid arrangement with maximum adjacent sum $S$. 

For each number $k \in \{51, ..., 100\}$, all its neighbors are $\leq S - k$. 

The number of cells that are "available" for numbers $\geq m$ (for some threshold) is constrained.

Let me try a different approach. Let's think about the problem in terms of the "conflict graph."

Two numbers $a$ and $b$ "conflict" (cannot be adjacent) if $a + b > S$. We need to arrange 1-100 in the grid so that no two conflicting numbers are adjacent.

For a given $S$, the conflict graph on $\{1, ..., 100\}$ has an edge between $a$ and $b$ iff $a + b > S$. We need to find an arrangement in the grid where no grid-adjacent pair is a conflict pair.

The grid is bipartite. So if we 2-color the grid, we need to partition $\{1,...,100\}$ into two sets $A$ and $B$ (each of size 50) such that no element of $A$ conflicts with any element of $B$ (since all grid edges go between the two color classes). Wait, that's not quite right - we need that for every grid edge $(u,v)$, the numbers at $u$ and $v$ don't conflict. But the grid edges don't connect all pairs between the two color classes - only specific pairs.

However, a sufficient condition is: partition $\{1,...,100\}$ into $A$ and $B$ (each size 50) such that no $a \in A, b \in B$ conflict (i.e., $a + b \leq S$ for all $a \in A, b \in B$). Then place $A$ on one color class and $B$ on the other, and no grid-adjacent pair conflicts.

But this is sufficient, not necessary. The necessary condition is weaker because not all pairs between color classes are grid-adjacent.

For the sufficient condition: we need $\max(A) + \max(B) \leq S$. To minimize this, we want to split $\{1,...,100\}$ into two sets of 50 where the sum of the maxima is minimized. The optimal split is $A = \{1,...,50\}, B = \{51,...,100\}$, giving $\max(A) + \max(B) = 50 + 100 = 150$. Or $A = \{1,...,50\}, B = \{51,...,100\}$, same thing.

But wait, can we do better with the necessary condition? Yes, because not all pairs between the two color classes are adjacent in the grid.

So the answer might be less than 150. Let me think more carefully.

Let me think about what the actual minimum is.

Let me consider a specific construction and lower bound.

**Approach: Think about which numbers can be "high" and what their neighbors must be.**

Let's say $S$ is the target. A number $k$ can only be adjacent to numbers $\leq S - k$. 

For $k = 100$: neighbors must be $\leq S - 100$.
For $k = 99$: neighbors must be $\leq S - 99$.
...

The number 100 has at least 2 neighbors (if at a corner). These neighbors must be $\leq S - 100$. So we need at least 2 numbers $\leq S - 100$.

Number 99: if at a corner, 2 neighbors $\leq S - 99$. But the 2 numbers used for 100's neighbors are already $\leq S - 100 \leq S - 99$, so they could potentially be shared... no, they can't be shared because 99 and 100 are at different cells.

Actually, let me think about it as a matching/flow problem or use a more clever counting argument.

**Better lower bound approach:**

Consider the set $H = \{k : k > S/2\}$. These are the "high" numbers. Any two high numbers that are adjacent would have sum $> S$, which is forbidden. So the high numbers must form an independent set in the grid.

The maximum independent set of the 10×10 grid is 50. So $|H| \leq 50$, which means the number of integers in $\{1,...,100\}$ that are $> S/2$ is at most 50. This gives $100 - \lfloor S/2 \rfloor \leq 50$, so $\lfloor S/2 \rfloor \geq 50$, so $S \geq 100$.

But this is a weak bound. Let me think stronger.

**Stronger approach:**

Consider numbers $k$ and $S - k$ for various $k$. If $k + (S-k) = S$, they can be adjacent (sum exactly $S$). But $k + (S - k + 1) = S + 1 > S$, so $k$ and $S - k + 1$ cannot be adjacent.

Hmm, let me think about this more carefully using the structure of the grid.

**Even stronger lower bound:**

Consider the numbers $\{m, m+1, ..., 100\}$ for some $m$. These are $101 - m$ numbers. They must form an independent set (if any two are adjacent, their sum $\geq m + (m+1) = 2m+1$; for this to exceed $S$, we need $2m + 1 > S$, i.e., $m > (S-1)/2$).

So for $m > (S-1)/2$, the set $\{m, ..., 100\}$ must be an independent set, requiring $101 - m \leq 50$, i.e., $m \geq 51$. This gives $(S-1)/2 < 51$, i.e., $S < 103$, so $S \leq 102$... wait, that's an upper bound on $S$ from this argument? No, let me redo.

If $m > (S-1)/2$, then any two numbers in $\{m, ..., 100\}$ have sum $\geq 2m > S - 1$, so sum $\geq 2m \geq S + 1 > S$ (if $2m > S$). Wait, $m > (S-1)/2$ means $2m > S - 1$, so $2m \geq S$ (if $S$ is integer and $2m$ is integer). So $2m \geq S$, meaning two numbers both $\geq m$ have sum $\geq 2m \geq S$. If $2m > S$, they can't be adjacent. If $2m = S$, they can be adjacent (sum = S is allowed).

So for $2m > S$ (i.e., $m > S/2$), the set $\{m, ..., 100\}$ must be independent, giving $101 - m \leq 50$, so $m \geq 51$, so $S/2 < 51$, $S < 102$, $S \leq 101$.

For $2m = S$ (i.e., $m = S/2$), two numbers both equal to $m$ have sum $S$ (allowed), but $m$ and $m+1$ have sum $S+1 > S$ (not allowed). So the set $\{m+1, ..., 100\}$ must be independent (any two have sum $\geq 2(m+1) = S + 2 > S$). This gives $100 - m \leq 50$, so $m \geq 50$, so $S/2 \geq 50$, $S \geq 100$.

And the set $\{m, m+1, ..., 100\}$ where $m = S/2$: $m$ can be adjacent to $m$ (but there's only one $m$), and $m$ can be adjacent to anything $\leq S - m = m$. So $m$ can be adjacent to numbers $\leq m$. But $m+1$ can only be adjacent to numbers $\leq S - (m+1) = m - 1$.

So the constraint is: $\{m+1, ..., 100\}$ must be independent, requiring $100 - m \leq 50$, i.e., $m \geq 50$, i.e., $S \geq 100$.

This gives $S \geq 100$. But this seems too weak. Let me think about whether we can achieve $S = 100$ or if we need more.

Wait, actually, the independent set constraint gives $S \geq 100$, but there might be additional constraints from the grid structure.

Let me think about $S = 100$. Can we achieve it?

If $S = 100$, then numbers $> 50$ must form an independent set (any two numbers $> 50$ have sum $> 100$). There are 50 such numbers (51-100), and the max independent set is 50. So they must occupy exactly one color class.

Numbers $\leq 50$ occupy the other color class. Now, number 100 must have all neighbors $\leq 100 - 100 = 0$. But there's no number $\leq 0$! So $S = 100$ is impossible.

So $S \geq 101$.

For $S = 101$: number 100 must have all neighbors $\leq 1$. So 100 must be adjacent only to 1 (and possibly other 1's, but there's only one 1). So 100 must be at a corner (degree 2), with both neighbors being... wait, 100 needs neighbors $\leq 1$, so both neighbors must be 1. But there's only one 1. So 100 can have at most one neighbor that is 1, and the other neighbor must also be $\leq 1$, which is impossible.

Wait, 100 needs neighbors $\leq S - 100 = 1$. So every neighbor of 100 must be $\leq 1$, i.e., must be 1. But 100 has at least 2 neighbors (minimum degree is 2 at corners), and there's only one "1". So $S = 101$ is impossible.

For $S = 102$: number 100 needs neighbors $\leq 2$. Number 100 has at least 2 neighbors. If at a corner, exactly 2 neighbors, both must be from $\{1, 2\}$. That's possible: place 100 at a corner, with neighbors 1 and 2.

Number 99 needs neighbors $\leq 3$. If 99 is at a corner, 2 neighbors from $\{1, 2, 3\}$. But 1 and 2 might already be used. If 1 and 2 are neighbors of 100, then 99's neighbors must be from $\{1, 2, 3\} \setminus \{\text{used}\}$... but 99 is at a different corner, so its neighbors are different cells. The values 1 and 2 are placed at specific cells (neighbors of 100), and 99's neighbors are different cells. So 99's neighbors need values $\leq 3$, and we have value 3 available (and possibly 1 or 2 if they happen to also be neighbors of 99, but that's unlikely in a 10×10 grid).

Actually, wait. Let me reconsider. The two neighbors of 100 (at corner (1,1)) are (1,2) and (2,1). If 99 is at corner (10,10), its neighbors are (10,9) and (9,10). These are completely different cells. So 99's neighbors need values $\leq 3$. We need to place two values from $\{1, 2, 3\}$ at (10,9) and (9,10), but 1 and 2 are already used at (1,2) and (2,1). So we only have 3 left, and we need two values $\leq 3$. That's impossible since only 3 is available.

Hmm, so we need to be more careful. Let me reconsider.

For $S = 102$:
- 100 needs 2 neighbors ≤ 2 (if at corner). Use 1, 2.
- 99 needs 2 neighbors ≤ 3 (if at corner). Available values ≤ 3 not yet used: {3}. Only 1 value, need 2. Problem!

Unless 99 is not at a corner but... if 99 is at an edge (degree 3), it needs 3 neighbors ≤ 3, even worse. If at interior (degree 4), 4 neighbors ≤ 3, worse.

So 99 must be at a corner, but even then, we need 2 values ≤ 3, and only 3 is left after using 1 and 2 for 100.

Wait, unless 99 is adjacent to 100. If 99 is adjacent to 100, then 99 + 100 = 199 > 102. Not allowed. So 99 can't be adjacent to 100.

Hmm, so $S = 102$ might not work either. Let me reconsider.

Actually wait. The neighbors of 100 must be ≤ 2. The neighbors of 99 must be ≤ 3. But these neighbor sets might overlap! If 99 is at a corner adjacent to 100's corner... no, in a 10×10 grid, corners are far apart.

Actually, can 99 be at a cell adjacent to one of 100's neighbors? That doesn't help directly.

Let me reconsider. The issue is that we need to "serve" the high numbers with low numbers, and the low numbers are a limited resource.

Let me think about this more systematically.

**Systematic lower bound:**

For a given $S$, number $k$ needs all its neighbors to be $\leq S - k$. Let $d(k)$ be the degree of the cell where $k$ is placed. Then $k$ "consumes" $d(k)$ cells that must have values $\leq S - k$.

Consider the high numbers $100, 99, 98, ..., 51$ (50 numbers). They must be on one color class (independent set). Each has some degree (2, 3, or 4), and their neighbors are on the other color class with values from $\{1, ..., 50\}$.

For number $k$ (where $k \in \{51, ..., 100\}$), its neighbors must be $\leq S - k$. 

Let's think about it from the perspective of the low numbers. Number $j$ (where $j \in \{1, ..., 50\}$) is on the "low" color class. It can be adjacent to high numbers $\leq S - j$. So number $j$ can "support" high numbers up to $S - j$.

The constraint is: for each high number $k$, all its $d(k)$ neighbors must be $\leq S - k$.

This is a complex combinatorial constraint. Let me try to find the answer by thinking about specific constructions.

Let me try $S = 110$ and see if it works, then try to lower it.

Actually, let me think about this problem from a higher level. 

The answer to this problem... let me think about what's known. This is a competition problem by D. Hramtsov. Let me think about the answer.

Let me try to find the answer by constructing an arrangement and proving a matching lower bound.

**Construction attempt:**

Place numbers on the grid in a "snake" pattern that alternates high and low. 

Actually, let me think about the problem differently. The grid is bipartite with color classes of size 50 each. Place 51-100 on one class and 1-50 on the other. Now we need to assign specific numbers to minimize the max edge sum.

The key structural feature of the 10×10 grid is the degree distribution and the adjacency structure.

Let me think about a "complementary" pairing. If we pair $k$ with $101 - k$ (so 100 with 1, 99 with 2, etc.), and place each pair on adjacent cells, the sum would be 101. But each cell has multiple neighbors, so we can't just pair them.

Let me think about the problem as follows. We have the bipartite graph $G = (B, W, E)$. We assign $f: B \to \{51,...,100\}$ and $g: W \to \{1,...,50\}$. We want to minimize $\max_{(b,w) \in E} (f(b) + g(w))$.

Equivalently, define $f'(b) = f(b) - 50 \in \{1,...,50\}$ and $g(w) \in \{1,...,50\}$. Then $f(b) + g(w) = f'(b) + g(w) + 50$. So we want to minimize $\max_{(b,w) \in E} (f'(b) + g(w)) + 50$, i.e., minimize $\max_{(b,w) \in E} (f'(b) + g(w))$.

So we have two copies of $\{1,...,50\}$ assigned to the two color classes, and we want to minimize the maximum sum across edges. This is a cleaner formulation.

Let me call this the "bipartite labeling problem": given a bipartite graph $G = (B, W, E)$ with $|B| = |W| = 50$, assign labels $\{1,...,50\}$ to each side, minimizing the maximum edge sum.

For the 10×10 grid, what's the optimal value?

Let me think about lower bounds for this reformulated problem. The answer to the original problem is this value + 50.

**Lower bound for the bipartite labeling problem:**

Consider the vertex $b \in B$ with the highest label, which is 50. Its neighbors in $W$ must have labels $\leq T - 50$ where $T$ is the max edge sum we're trying to minimize. If $b$ has degree $d$, we need $d$ labels $\leq T - 50$.

Similarly, the vertex with label 49 needs its neighbors to have labels $\leq T - 49$.

And from the other side, the vertex $w \in W$ with label 50 needs its neighbors in $B$ to have labels $\leq T - 50$.

So both the highest-labeled vertices on each side impose constraints.

Let me think about the degree structure. In the 10×10 grid, considering one color class (say $B$):
- 2 vertices of degree 2 (corners)
- 16 vertices of degree 3 (edges)
- 32 vertices of degree 4 (interior)

Same for $W$.

The vertex labeled 50 on side $B$: to minimize $T$, place it at a corner (degree 2). Then we need 2 vertices in $W$ with labels $\leq T - 50$.

The vertex labeled 50 on side $W$: place at a corner (degree 2). Need 2 vertices in $B$ with labels $\leq T - 50$.

The vertex labeled 49 on side $B$: place at the other corner (degree 2). Need 2 vertices in $W$ with labels $\leq T - 49$.

The vertex labeled 49 on side $W$: place at the other corner (degree 2). Need 2 vertices in $B$ with labels $\leq T - 49$.

So far, with 4 corners (2 on each side), we place labels 50 and 49 on each side's corners.

For $B$ side: label 50 at corner $c_1$ (degree 2), label 49 at corner $c_2$ (degree 2).
- Neighbors of $c_1$ need labels $\leq T - 50$.
- Neighbors of $c_2$ need labels $\leq T - 49$.

For $W$ side: label 50 at corner $c_3$ (degree 2), label 49 at corner $c_4$ (degree 2).
- Neighbors of $c_3$ need labels $\leq T - 50$.
- Neighbors of $c_4$ need labels $\leq T - 49$.

Now, the neighbors of $c_1$ (in $W$) need labels $\leq T - 50$. The neighbors of $c_3$ (in $B$) need labels $\leq T - 50$. 

If $T - 50 \geq 2$, we have at least labels $\{1, 2\}$ available for these. But we need 2 labels for $c_1$'s neighbors and 2 labels for $c_3$'s neighbors, total 4 labels $\leq T - 50$ (assuming no overlap, which is the case since corners are far apart in a 10×10 grid).

Actually, the neighbors of $c_1$ and $c_3$ are different cells (one set in $W$, one set in $B$), so they use labels from different sides. So we need 2 labels $\leq T-50$ on side $W$ (for $c_1$'s neighbors) and 2 labels $\leq T-50$ on side $B$ (for $c_3$'s neighbors). Each side has 50 labels, so we need at least 2 labels $\leq T-50$ on each side, giving $T - 50 \geq 2$, $T \geq 52$.

But we also need labels for $c_2$'s neighbors (2 labels $\leq T - 49$ on side $W$) and $c_4$'s neighbors (2 labels $\leq T - 49$ on side $B$).

On side $W$: 2 labels $\leq T - 50$ (for $c_1$) and 2 labels $\leq T - 49$ (for $c_2$). The 2 labels for $c_1$ are also $\leq T - 49$ (since $T - 50 < T - 49$). So we need at least 2 labels $\leq T - 50$ and 2 more labels $\leq T - 49$ (but the first 2 also count). Actually, the 4 neighbor cells of $c_1$ and $c_2$ are all distinct (corners are far apart), so we need 4 distinct labels on side $W$, with 2 of them $\leq T - 50$ and all 4 $\leq T - 49$.

So on side $W$: 2 labels $\leq T - 50$ and 2 more labels in $(T-50, T-49]$ (or also $\leq T - 50$). The minimum is: 2 labels $\leq T - 50$, and 2 more labels $\leq T - 49$. So we need at least 2 labels $\leq T-50$ and at least 4 labels $\leq T - 49$ on side $W$.

Similarly on side $B$: 2 labels $\leq T - 50$ and 4 labels $\leq T - 49$.

This gives $T - 50 \geq 2$ (need 2 labels $\leq T-50$ on each side) and $T - 49 \geq 4$ (need 4 labels $\leq T-49$ on each side), so $T \geq 53$.

Continuing this analysis for more high-labeled vertices...

Let me think about this more systematically. Let me consider the top $k$ labels on each side and figure out how many low labels are needed.

On side $B$, the vertices with labels $50, 49, 48, ..., 50-k+1$ (the top $k$ labels) need their neighbors to have low labels. The constraint for label $50 - j$ (for $j = 0, 1, ..., k-1$) is that its $d$ neighbors have labels $\leq T - (50 - j) = T - 50 + j$.

If we place the top $k$ labels at the lowest-degree vertices (corners first, then edges, then interior), we minimize the total number of "low label slots" needed.

Let me think about it as a "demand" problem. 

On side $B$, sort vertices by degree: 2 corners (degree 2), 16 edges (degree 3), 32 interior (degree 4).

Assign labels 50, 49, 48, ... to vertices in order of increasing degree.

Label 50 → corner (degree 2), needs 2 neighbors with labels ≤ T - 50.
Label 49 → corner (degree 2), needs 2 neighbors with labels ≤ T - 49.
Label 48 → edge (degree 3), needs 3 neighbors with labels ≤ T - 48.
Label 47 → edge (degree 3), needs 3 neighbors with labels ≤ T - 47.
...

On side $W$, similarly:
Label 50 → corner (degree 2), needs 2 neighbors (in $B$) with labels ≤ T - 50.
Label 49 → corner (degree 2), needs 2 neighbors (in $B$) with labels ≤ T - 49.
...

Now, the demands on side $W$ (from $B$'s high labels) and the demands on side $B$ (from $W$'s high labels) interact.

Let me think about the demand on side $W$ from $B$'s top labels:
- Label 50 on $B$ (corner, degree 2): 2 cells in $W$ with labels ≤ T - 50.
- Label 49 on $B$ (corner, degree 2): 2 cells in $W$ with labels ≤ T - 49.
- Label 48 on $B$ (edge, degree 3): 3 cells in $W$ with labels ≤ T - 48.
- Label 47 on $B$ (edge, degree 3): 3 cells in $W$ with labels ≤ T - 47.
- ...

And the demand on side $B$ from $W$'s top labels:
- Label 50 on $W$ (corner, degree 2): 2 cells in $B$ with labels ≤ T - 50.
- Label 49 on $W$ (corner, degree 2): 2 cells in $B$ with labels ≤ T - 49.
- ...

These are symmetric. Let me focus on the demand on side $W$.

The total number of cells in $W$ that must have labels ≤ some threshold is constrained by the available labels. Specifically, the number of cells in $W$ with labels ≤ $m$ is exactly $m$ (since labels are 1 to 50). 

Now, the demand: for each high label on $B$, we need some cells in $W$ with labels ≤ some threshold. But a single cell in $W$ can satisfy the demands of multiple high labels on $B$ (if it's adjacent to multiple high-label $B$ vertices). However, in the grid, each $W$ cell has at most 4 neighbors in $B$.

This is getting complicated. Let me try a different approach: just try to find the answer by constructing a good arrangement and proving a tight lower bound.

Let me try to think about what $T$ (in the reformulated problem) should be, and then $S = T + 50$.

**Trying $T = 55$, so $S = 105$:**

Hmm, let me think about this more carefully. Let me try to think about what the answer might be.

Actually, let me think about a simpler version first. Consider a $2 \times n$ grid. Numbers 1 to $2n$. Bipartite with color classes of size $n$ each. 

For a $2 \times 2$ grid: numbers 1-4. Color classes: {(1,1), (2,2)} and {(1,2), (2,1)}. Each vertex has degree 2. Place 3,4 on one side and 1,2 on the other. The edges are (1,1)-(1,2), (1,1)-(2,1), (2,2)-(1,2), (2,2)-(2,1). So every vertex on one side is adjacent to every vertex on the other side (it's $K_{2,2}$). So the max sum is $\max(3,4) + \max(1,2) = 4 + 2 = 6$. Can we do better? With the split {3,4} and {1,2}, the max edge sum is 6. With split {1,4} and {2,3}: max edge sum = 4 + 3 = 7. With split {1,3} and {2,4}: 4 + 3 = 7. So the best is 6. And $S = 6$ for the $2 \times 2$ grid.

Hmm wait, for $2 \times 2$, the graph is $K_{2,2}$, so every pair across the partition is an edge. The minimum max edge sum is $\min_{\text{partition}} \max(A) + \max(B)$ where $A \cup B = \{1,2,3,4\}$, $|A| = |B| = 2$. Best: $A = \{1,2\}, B = \{3,4\}$, sum = 2 + 4 = 6. So $S = 6$.

For a path graph $P_n$ (1×n grid), the answer would be different because the graph is much sparser.

Let me think about the 10×10 grid more carefully.

Actually, let me think about the problem from the perspective of the "complement" arrangement.

In the reformulated problem, we assign labels 1-50 to each side of the bipartite graph. The max edge sum is $T$. We want to minimize $T$.

**Key observation:** If we use the "reversed" assignment on one side, i.e., assign label $k$ to the vertex that has the "most demanding" position, we can balance things.

Let me think about a specific strategy. On side $B$, assign labels in decreasing order to vertices in order of increasing degree (corners get highest labels, interior gets lowest). On side $W$, assign labels in increasing order to vertices in order of increasing degree (corners get lowest labels, interior gets highest). 

Wait, that doesn't make sense because both sides have the same degree distribution.

Let me think about it differently. The idea is: high labels on one side should be adjacent to low labels on the other side.

If we assign label 50 to a corner of $B$ (degree 2), its 2 neighbors in $W$ should have low labels. If we assign label 1 to a corner of $W$ (degree 2), its 2 neighbors in $B$ should have low labels. But the corner of $B$ with label 50 and the corner of $W$ with label 1 might not be adjacent.

Let me try to think about the grid structure more concretely.

Label the grid positions as $(i,j)$ for $1 \le i,j \le 10$. Even color: $(i+j)$ even. Odd color: $(i+j)$ odd.

$B$ = even cells, $W$ = odd cells.

Corners: $(1,1)$ even, $(1,10)$ odd, $(10,1)$ odd, $(10,10)$ even.

So $B$ has corners $(1,1)$ and $(10,10)$, and $W$ has corners $(1,10)$ and $(10,1)$.

Let me try a specific assignment. On side $B$ (even cells), assign labels based on the "anti-diagonal" or some pattern. 

Actually, let me try a "complementary" approach. Define the label of cell $(i,j)$ on side $B$ as $f(i,j)$ and on side $W$ as $g(i,j)$. We want $f(i,j) + g(i',j') \leq T$ for all adjacent pairs.

One natural approach: make $f$ and $g$ "anti-correlated" in some spatial sense. If $f$ is large at some cell, $g$ should be small at all neighboring cells.

Let me try: $f(i,j) = $ some function that's large at corners and small at center, and $g(i,j) = $ some function that's small at corners and large at center. But the cells of $B$ and $W$ are interleaved, so this needs to be done carefully.

Actually, here's an idea. Consider the "Manhattan distance from center" $d(i,j) = |i - 5.5| + |j - 5.5|$. Cells far from center (corners, edges) have high $d$, cells near center have low $d$.

On side $B$: assign high labels to high-$d$ cells (corners/edges) and low labels to low-$d$ cells (center).
On side $W$: assign low labels to high-$d$ cells and high labels to low-$d$ cells.

This way, at the corners (high $d$), $B$ has high labels and $W$ has low labels. At the center (low $d$), $B$ has low labels and $W$ has high labels. Since adjacent cells have similar $d$ values (differ by 1), the sum $f + g$ would be roughly balanced.

But this is just a heuristic. Let me try to compute the actual max edge sum for such an arrangement.

Hmm, this is getting quite involved. Let me try to think about the problem from the answer's perspective.

For competition problems of this type, the answer is often a "clean" number. Let me guess that the answer might be $S = 110$ or $S = 105$ or something like that.

Actually, let me think about a cleaner lower bound argument.

**Lower bound via "neighbor counting":**

Consider the numbers $100, 99, ..., 100-k+1$ (the top $k$ numbers). Each needs its neighbors to be small. Specifically, number $100-j$ needs all neighbors $\leq S - (100-j) = S - 100 + j$.

The total number of "neighbor slots" for these $k$ numbers is $\sum_{j=0}^{k-1} d(100-j)$, where $d$ is the degree. But neighbors can be shared (a cell can be neighbor to multiple high numbers).

In the grid, a cell can be adjacent to at most 4 high-number cells. But more importantly, the number of distinct cells that are neighbors of the top $k$ numbers is at least... well, it depends on the arrangement.

This is hard to bound in general. Let me try a different approach.

**Lower bound via "label counting" on one side:**

In the reformulated problem, consider side $B$. The vertex with label $m$ has all its neighbors on side $W$ with labels $\leq T - m$. 

For the vertex with label 50 (highest on $B$), placed at a corner (degree 2): 2 neighbors with labels $\leq T - 50$.
For the vertex with label 49, placed at a corner (degree 2): 2 neighbors with labels $\leq T - 49$.
For the vertex with label 48, placed at an edge (degree 3): 3 neighbors with labels $\leq T - 48$.
...

On side $W$, the number of vertices with labels $\leq m$ is exactly $m$. 

Now, the 2 neighbors of label-50 vertex need labels $\leq T - 50$. The 2 neighbors of label-49 vertex need labels $\leq T - 49$. These 4 cells are distinct (corners are far apart). So we need at least 2 labels $\leq T-50$ and 2 more labels $\leq T-49$ on side $W$.

But also, side $W$ has its own high labels (50, 49, ...) that need low-labeled neighbors on side $B$.

Let me think about the combined constraint. 

On side $W$, consider the labels assigned to the neighbors of $B$'s high-label vertices. These must be low. But side $W$ also has high-label vertices that need to be placed somewhere.

The key tension: side $W$ needs some vertices with low labels (to serve as neighbors of $B$'s high labels) and some vertices with high labels (which themselves need low-labeled neighbors on side $B$).

Let me think about a "budget" argument.

On side $W$:
- Some vertices need low labels (neighbors of high-$B$ vertices).
- Some vertices have high labels (and their neighbors on $B$ need low labels).

The vertices of $W$ that are neighbors of high-$B$ vertices are determined by the grid structure. The vertices of $W$ that have high labels are determined by our assignment.

To minimize $T$, we want the high-label $W$ vertices to NOT be neighbors of high-label $B$ vertices. In other words, the high labels on $B$ and $W$ should be "far apart" in the grid.

In the 10×10 grid, the maximum number of vertices that are pairwise at distance $\geq 3$ (so that their neighborhoods don't overlap) is related to the structure.

Hmm, this is getting complex. Let me try to just compute the answer for small cases and see if there's a pattern.

For a $2 \times 2$ grid: $S = 6$ (computed above). Reformulated: $T = S - 2 = 4$? Wait, let me redo. For $2 \times 2$, numbers 1-4. Split into {1,2} and {3,4}. Max edge sum = 2 + 4 = 6. In the reformulated problem with labels 1-2 on each side: max edge sum = 2 + 2 = 4. And $S = T + 2 = 6$. ✓ (since the split is {1,2} → labels {1,2} and {3,4} → labels {1,2} where 3→1, 4→2, so $S = T + 2$).

Wait, I need to be more careful. In the original problem, we split {1,...,2n} into two sets of size $n$. If we split into {1,...,n} and {n+1,...,2n}, then the labels on each side are {1,...,n} and {1,...,n} (after subtracting $n$ from the high side). The max edge sum in the original is $T + n$ where $T$ is the max edge sum in the reformulated problem.

For $2 \times 2$ ($n=2$): $T = 4$, $S = 4 + 2 = 6$. ✓

For a $2 \times 4$ grid: numbers 1-8, $n=4$. Color classes of size 4 each. The graph is a $2 \times 4$ grid. Let me think about the reformulated problem.

Actually, this is getting too complicated for hand computation. Let me think about the 10×10 case directly.

Let me try to think about what $T$ should be for the 10×10 grid.

**Approach: Think about the "bottleneck" — the highest-label vertex on each side.**

The vertex with label 50 on side $B$ (at a corner, degree 2) needs 2 neighbors with labels $\leq T - 50$.
The vertex with label 50 on side $W$ (at a corner, degree 2) needs 2 neighbors with labels $\leq T - 50$.

The 2 neighbors of $B$'s label-50 vertex are on side $W$, and the 2 neighbors of $W$'s label-50 vertex are on side $B$. These are independent constraints.

On side $W$: need 2 labels $\leq T - 50$. So $T - 50 \geq 2$, $T \geq 52$.
On side $B$: need 2 labels $\leq T - 50$. Same, $T \geq 52$.

Now, label 49 on side $B$ (at the other corner, degree 2): 2 neighbors on $W$ with labels $\leq T - 49$.
Label 49 on side $W$ (at the other corner, degree 2): 2 neighbors on $B$ with labels $\leq T - 49$.

On side $W$: need 2 labels $\leq T - 50$ (for $B$'s label 50) and 2 more labels $\leq T - 49$ (for $B$'s label 49). Total: 4 distinct cells, 2 with labels $\leq T-50$ and 2 more with labels $\leq T-49$. So need at least 4 labels $\leq T - 49$ on side $W$, giving $T - 49 \geq 4$, $T \geq 53$.

Similarly on side $B$: $T \geq 53$.

Continuing:
Label 48 on side $B$ (at an edge cell, degree 3): 3 neighbors on $W$ with labels $\leq T - 48$.
Label 48 on side $W$ (at an edge cell, degree 3): 3 neighbors on $B$ with labels $\leq T - 48$.

On side $W$: now need 2 (≤ T-50) + 2 (≤ T-49) + 3 (≤ T-48) = 7 distinct cells. But wait, some of these neighbor cells might overlap! The corner cells and edge cells might share neighbors.

Let me think about the grid structure. In the 10×10 grid:
- Corner $(1,1)$ (even, $B$): neighbors $(1,2)$ and $(2,1)$ (both odd, $W$).
- Corner $(10,10)$ (even, $B$): neighbors $(10,9)$ and $(9,10)$ (both odd, $W$).
- These are 4 distinct cells in $W$.

- Edge cell near corner, say $(1,3)$ (even, $B$): neighbors $(1,2), (1,4), (2,3)$ (all odd, $W$).
  - $(1,2)$ is shared with corner $(1,1)$!

So there IS overlap. The neighbor $(1,2)$ of corner $(1,1)$ is also a neighbor of edge cell $(1,3)$.

This means the counting is more nuanced. Let me think about it more carefully.

If we place label 50 at corner $(1,1)$ and label 48 at edge cell $(1,3)$, then $(1,2)$ is a common neighbor. The constraint on $(1,2)$ is $\leq \min(T - 50, T - 48) = T - 50$. So the shared neighbor just needs to satisfy the tighter constraint.

So the total number of distinct neighbor cells is less than the sum of degrees. Let me think about how to minimize the total number of distinct low-label cells needed.

To minimize overlap (and thus minimize the number of distinct low-label cells needed), we should spread the high-label vertices far apart. But to minimize $T$, we want to minimize the number of distinct low-label cells needed, which means we want MORE overlap.

Wait, no. More overlap means fewer distinct cells need low labels, which is good (we have more freedom). But the overlapping cells need to satisfy the tightest constraint.

Hmm, actually, the question is: what's the minimum number of distinct cells on side $W$ that need labels $\leq T - m$ for each $m$?

This depends on the placement of high-label vertices on side $B$.

Let me think about it differently. Let's say we place the top $k$ labels on side $B$ at specific cells. The union of their neighborhoods in $W$ is some set $N_k \subseteq W$. The constraint is:
- For each $b$ in the top $k$ with label $l(b)$, all neighbors of $b$ have labels $\leq T - l(b)$.

The tightest constraint on a cell $w \in N_k$ is $\leq T - \max_{b \sim w, b \in \text{top } k} l(b)$.

To minimize $T$, we want to:
1. Minimize $|N_k|$ (fewer cells need low labels).
2. Make the constraints as uniform as possible.

To minimize $|N_k|$, we should cluster the high-label vertices (so their neighborhoods overlap). But clustering high-label vertices means they're close together, which means they're in the same region of the grid.

But wait, the high-label vertices on $B$ and the high-label vertices on $W$ should be far apart (so that high labels on $B$ are adjacent to low labels on $W$ and vice versa). If we cluster high labels on $B$ in one corner, then the $W$ cells near that corner need low labels, and the $W$ cells far from that corner can have high labels.

Let me try a specific construction.

**Construction: "Corner-based"**

Place the highest labels on $B$ near corner $(1,1)$ and the highest labels on $W$ near corner $(10,10)$ (which is far from $(1,1)$).

Specifically:
- On side $B$ (even cells), assign labels in decreasing order as we move away from corner $(10,10)$ toward corner $(1,1)$. So the highest $B$ labels are near $(1,1)$.
- On side $W$ (odd cells), assign labels in decreasing order as we move away from corner $(1,1)$ toward corner $(10,10)$. So the highest $W$ labels are near $(10,10)$.

Wait, but $(10,10)$ is an even cell (in $B$), and $(1,1)$ is also even (in $B$). The $W$ corners are $(1,10)$ and $(10,1)$.

Let me reconsider. $B$ (even) corners: $(1,1)$ and $(10,10)$. $W$ (odd) corners: $(1,10)$ and $(10,1)$.

Place highest $B$ labels near $(1,1)$ and highest $W$ labels near $(10,1)$ (or $(1,10)$). The distance between $(1,1)$ and $(10,1)$ is 9, which is large. So high $B$ labels near $(1,1)$ and high $W$ labels near $(10,1)$ are far apart.

But this only uses two corners. What about the other two corners?

Actually, let me think about a different construction. 

**Construction: "Diagonal"**

On side $B$, assign label $k$ to the cell with the $k$-th largest "anti-diagonal sum" $i + j$ (or some similar ordering). On side $W$, assign label $k$ to the cell with the $k$-th smallest "anti-diagonal sum."

Hmm, this is getting complicated. Let me try to think about the problem from the answer.

Let me consider the problem from the perspective of a specific vertex. The center of the grid has cells with degree 4. A cell at position $(5,5)$ (even, $B$) has neighbors $(5,4), (5,6), (4,5), (6,5)$ (all odd, $W$). If this cell has label $l$, its neighbors need labels $\leq T - l$.

If $l$ is around 25 (middle label), then neighbors need labels $\leq T - 25$. If $T = 55$, neighbors need labels $\leq 30$, which is easy (most labels are $\leq 30$).

The binding constraints come from the high-label vertices. Let me focus on those.

**Let me try to compute a lower bound more carefully.**

Consider the top $k$ labels on side $B$: $50, 49, ..., 51-k$. These are placed at cells $b_1, b_2, ..., b_k$ (in some order). Their neighborhoods in $W$ are $N(b_1), ..., N(b_k)$.

For each $w \in \bigcup N(b_i)$, the label of $w$ must be $\leq T - \max\{l(b_i) : w \in N(b_i)\}$.

Now, similarly, the top $k$ labels on side $W$ are placed at cells $w_1, ..., w_k$, and their neighborhoods in $B$ impose constraints on $B$'s labels.

The key insight is: the cells in $W$ that are neighbors of high-$B$ cells need low labels, and the cells in $W$ that have high labels should NOT be neighbors of high-$B$ cells.

So we want: (high labels on $W$) ∩ (neighbors of high labels on $B$) = ∅.

The number of cells in $W$ that are neighbors of the top $k$ $B$-cells is $|\bigcup N(b_i)|$. The number of cells in $W$ with labels $> T - (51-k) = T - 51 + k$ is $50 - (T - 51 + k) = 101 - T - k$ (these are the cells that can be neighbors of the $(k+1)$-th highest $B$ label or higher... hmm, this isn't quite right).

Let me think about it differently.

**Clean lower bound argument:**

Let $T$ be the max edge sum in the reformulated problem. Consider the set of cells on side $B$ with labels $> T/2$. Call this set $B_{\text{high}}$. Similarly, $W_{\text{high}}$ = cells on side $W$ with labels $> T/2$.

If $b \in B_{\text{high}}$ and $w \in W_{\text{high}}$ are adjacent, then $l(b) + l(w) > T/2 + T/2 = T$, contradiction. So $B_{\text{high}}$ and $W_{\text{high}}$ have no edges between them.

The number of cells with labels $> T/2$ on each side is $50 - \lfloor T/2 \rfloor$.

Now, $B_{\text{high}}$ and $W_{\text{high}}$ are two sets with no edges between them. In the grid graph, what's the maximum $|B_{\text{high}}| + |W_{\text{high}}|$ such that there are no edges between them?

If there are no edges between $B_{\text{high}}$ and $W_{\text{high}}$, then $B_{\text{high}} \cup W_{\text{high}}$ is an independent set in the grid (since $B_{\text{high}} \subseteq B$ and $W_{\text{high}} \subseteq W$, and there are no edges within $B$ or within $W$, and no edges between $B_{\text{high}}$ and $W_{\text{high}}$). So $|B_{\text{high}}| + |W_{\text{high}}| \leq 50$ (max independent set).

This gives $2(50 - \lfloor T/2 \rfloor) \leq 50$, so $50 - \lfloor T/2 \rfloor \leq 25$, $\lfloor T/2 \rfloor \geq 25$, $T \geq 50$.

So $S \geq 50 + 50 = 100$. But we already knew $S \geq 102$ from the earlier argument (number 100 needs neighbors ≤ $S - 100$, and with degree ≥ 2, we need at least 2 numbers ≤ $S - 100$).

Let me combine the arguments. In the reformulated problem, the vertex with label 50 on side $B$ needs all neighbors to have labels $\leq T - 50$. If this vertex has degree $d$, we need $d$ labels $\leq T - 50$ on side $W$.

But also, the vertex with label 50 on side $W$ needs all neighbors (on side $B$) to have labels $\leq T - 50$.

Now, the $d$ neighbors of $B$'s label-50 vertex are on side $W$ with labels $\leq T - 50$. The label-50 vertex on side $W$ has label 50 > $T - 50$ (if $T < 100$). So the label-50 vertex on $W$ cannot be a neighbor of the label-50 vertex on $B$. More generally, any vertex on $W$ with label $> T - 50$ cannot be a neighbor of the label-50 vertex on $B$.

The number of $W$-vertices with labels $> T - 50$ is $50 - (T - 50) = 100 - T$.

These $100 - T$ vertices on $W$ must not be in the neighborhood of $B$'s label-50 vertex. The neighborhood has $d$ vertices. So $d \leq 50 - (100 - T) = T - 50$. Since $d \geq 2$ (minimum degree), $T - 50 \geq 2$, $T \geq 52$.

But we can do better. Consider the top $k$ labels on $B$: $50, 49, ..., 51-k$. Their neighborhoods in $W$ must avoid the top $100 - T + k - 1$ labels on $W$... hmm, this is getting complicated.

Let me try a cleaner approach.

**Clean approach:**

In the reformulated problem, let $T$ be the optimal max edge sum. 

For each $m = 1, ..., 50$, let $B_m = \{b \in B : l(b) \geq m\}$ and $W_m = \{w \in W : l(w) \geq m\}$. Then $|B_m| = |W_m| = 51 - m$.

If $b \in B_m$ and $w \in W_{T+1-m}$ are adjacent, then $l(b) + l(w) \geq m + (T+1-m) = T + 1 > T$, contradiction. So there are no edges between $B_m$ and $W_{T+1-m}$.

This means $B_m \cup W_{T+1-m}$ is an independent set, so $|B_m| + |W_{T+1-m}| \leq 50$.

$(51 - m) + (51 - (T+1-m)) \leq 50$
$(51 - m) + (50 - T + m) \leq 50$
$101 - T \leq 50$
$T \geq 51$.

So $T \geq 51$, giving $S \geq 101$. But we showed $S \geq 102$ earlier. Let me recheck.

Earlier: $S = 101$ means number 100 needs neighbors $\leq 1$. Degree $\geq 2$, but only one number (1) is $\leq 1$. So $S \geq 102$.

In the reformulated problem, $S = 101$ corresponds to $T = 51$ (since $S = T + 50$). The vertex with label 50 on side $B$ needs neighbors with labels $\leq 51 - 50 = 1$. Only one label (1) is $\leq 1$, but degree $\geq 2$. So $T \geq 52$, $S \geq 102$.

OK so the independent set argument gives $T \geq 51$, and the degree argument gives $T \geq 52$. Can we push further?

**Pushing further:**

Consider $B_{50}$ (the single vertex with label 50 on side $B$) and $W_{T-49}$ (vertices on $W$ with labels $\geq T - 49$). No edges between them. $|B_{50}| = 1$, $|W_{T-49}| = 50 - (T - 49) + 1 = 100 - T$.

The vertex in $B_{50}$ has degree $d \geq 2$. Its $d$ neighbors are in $W$ and not in $W_{T-49}$. So $d \leq 50 - |W_{T-49}| = 50 - (100 - T) = T - 50$. With $d = 2$ (corner), $T \geq 52$.

Now consider $B_{49}$ (vertices with labels $\geq 49$ on $B$, so 2 vertices) and $W_{T-48}$ (vertices with labels $\geq T - 48$ on $W$). No edges between them. $|B_{49}| = 2$, $|W_{T-48}| = 50 - (T - 48) + 1 = 99 - T$.

The 2 vertices in $B_{49}$ have total degree $\geq 2 + 2 = 4$ (both at corners). Their neighborhoods in $W$ are disjoint (corners are far apart) and avoid $W_{T-48}$. So the neighborhoods have at least 4 distinct vertices, all outside $W_{T-48}$. So $4 \leq 50 - |W_{T-48}| = 50 - (99 - T) = T - 49$. So $T \geq 53$.

Continuing: $B_{48}$ (3 vertices with labels $\geq 48$) and $W_{T-47}$ (vertices with labels $\geq T - 47$). $|B_{48}| = 3$, $|W_{T-47}| = 50 - (T - 47) + 1 = 98 - T$.

The 3 vertices in $B_{48}$: 2 at corners (degree 2 each) and 1 at an edge (degree 3). Total degree = 7. But neighborhoods might overlap.

If we place the 2 corners at $(1,1)$ and $(10,10)$ (far apart, no overlap) and the edge vertex at, say, $(1,3)$ (near corner $(1,1)$), then the neighborhood of $(1,3)$ includes $(1,2)$ which is also a neighbor of $(1,1)$. So overlap = 1, and distinct neighbors = 7 - 1 = 6.

But we want to MINIMIZE the number of distinct neighbors (to make the constraint easier to satisfy). Wait, no — we're proving a lower bound. We want to show that no matter how you place the high-label vertices, you need many distinct low-label neighbors.

For a lower bound, we want to show that the neighborhoods can't overlap too much. But actually, for a lower bound on $T$, we want to show that the number of distinct neighbors is LARGE (forcing many low labels, forcing $T$ to be large).

Hmm wait, I need to be more careful. The constraint is: the neighborhoods of $B_{48}$ must avoid $W_{T-47}$. The number of vertices in $W$ that are NOT in $W_{T-47}$ is $50 - (98 - T) = T - 48$. The neighborhoods of $B_{48}$ must fit within these $T - 48$ vertices. So the number of distinct neighbors of $B_{48}$ must be $\leq T - 48$.

To get a lower bound on $T$, we need a lower bound on the number of distinct neighbors of $B_{48}$, minimized over all possible placements of 3 vertices (2 corners + 1 edge) on side $B$.

To minimize the number of distinct neighbors, we should maximize overlap. Place the 2 corners at $(1,1)$ and $(1,3)$... wait, $(1,3)$ is not a corner. The $B$ corners are $(1,1)$ and $(10,10)$. These are far apart (distance 18), so no overlap.

The edge vertex (degree 3) should be placed to maximize overlap with the corners' neighborhoods. Place it at $(1,3)$ (edge, degree 3, neighbors $(1,2), (1,4), (2,3)$). Corner $(1,1)$ has neighbors $(1,2), (2,1)$. Overlap: $(1,2)$. So distinct neighbors = $2 + 2 + 3 - 1 = 6$.

Or place the edge vertex at $(2,2)$ (interior, degree 4, neighbors $(2,1), (2,3), (1,2), (3,2)$). Wait, $(2,2)$ is even, so it's in $B$. Its neighbors are $(2,1), (2,3), (1,2), (3,2)$, all odd ($W$). Corner $(1,1)$'s neighbors: $(1,2), (2,1)$. Overlap: $(1,2)$ and $(2,1)$. So distinct = $4 + 2 - 2 = 4$. But $(2,2)$ is interior (degree 4), not edge (degree 3). 

Hmm, I said the 3rd highest label goes to an edge cell (degree 3). But actually, we get to choose where to place labels. To minimize the number of distinct neighbors (for the lower bound, we want to show this can't be too small), we should consider the best possible placement.

Wait, I'm confusing myself. For the lower bound, I need to show that for ANY placement, the number of distinct neighbors is at least some value. But the placement is chosen by the optimizer to minimize $T$, so they would choose the placement that minimizes the number of distinct neighbors.

So for the lower bound: the minimum number of distinct neighbors of 3 $B$-vertices (2 corners + 1 non-corner) is achieved by placing them to maximize overlap. The 2 corners are fixed at $(1,1)$ and $(10,10)$ (the only $B$-corners). The 3rd vertex can be anywhere in $B$ (not a corner). To maximize overlap with corner $(1,1)$'s neighborhood $\{(1,2), (2,1)\}$, place the 3rd vertex adjacent to both $(1,2)$ and $(2,1)$. The vertex $(2,2)$ is adjacent to both $(1,2)$ and $(2,1)$ (and also $(2,3)$ and $(3,2)$). So placing the 3rd vertex at $(2,2)$ gives neighbors $\{(1,2), (2,1), (2,3), (3,2)\}$, with overlap 2 with corner $(1,1)$'s neighborhood. Distinct neighbors of all 3: $\{(1,2), (2,1)\} \cup \{(10,9), (9,10)\} \cup \{(1,2), (2,1), (2,3), (3,2)\} = \{(1,2), (2,1), (2,3), (3,2), (10,9), (9,10)\}$. That's 6.

But wait, $(2,2)$ is an interior cell (degree 4), not an edge cell (degree 3). I was assuming the 3rd highest label goes to a degree-3 cell, but actually, the optimizer can choose to put it at a degree-4 cell if that helps. Let me reconsider.

The optimizer wants to minimize $T$. They choose:
1. Which cells get the highest labels.
2. The assignment of labels to cells.

For the lower bound, I should consider the best possible strategy for the optimizer.

The optimizer would place the highest labels at the lowest-degree cells (corners, then edges) to minimize the number of neighbors that need low labels. But they might also consider overlap.

Let me reconsider. The 3 highest labels on $B$ are 50, 49, 48. The optimizer places them at 3 cells in $B$ to minimize the "cost." The cost is related to the number of distinct neighbors and the label constraints.

If placed at 2 corners + 1 interior near a corner:
- Corners $(1,1)$ and $(10,10)$: neighborhoods $\{(1,2),(2,1)\}$ and $\{(10,9),(9,10)\}$.
- Interior $(2,2)$: neighborhood $\{(1,2),(2,1),(2,3),(3,2)\}$.
- Union: $\{(1,2),(2,1),(2,3),(3,2),(10,9),(9,10)\}$, size 6.
- Constraints: $(1,2)$ and $(2,1)$ need labels $\leq \min(T-50, T-48) = T-50$ (since they're neighbors of both label 50 and label 48). $(2,3)$ and $(3,2)$ need labels $\leq T-48$. $(10,9)$ and $(9,10)$ need labels $\leq T-49$ (neighbors of label 49 only).

So we need: 2 labels $\leq T-50$, 2 more labels $\leq T-48$, 2 more labels $\leq T-49$ on side $W$. Total: 6 distinct cells, with 2 having labels $\leq T-50$.

But also, side $W$ has its own top 3 labels (50, 49, 48) that need low-label neighbors on side $B$. By symmetry, the same analysis applies.

Now, the constraint from $B$'s top 3 on $W$: 6 cells in $W$ need specific low labels. The remaining 44 cells in $W$ can have any labels, including the top labels 50, 49, 48.

But $W$'s top labels (50, 49, 48) need their neighbors on $B$ to have low labels. The neighbors of $W$'s top-label cells must avoid $B$'s top-label cells.

This is getting very involved. Let me try to just guess the answer and verify.

Let me think about what $T$ might be. 

For the 10×10 grid, the reformulated problem has labels 1-50 on each side. The grid has 180 edges (10×9 horizontal + 9×10 vertical = 90 + 90 = 180).

Let me think about a "checkerboard complementary" assignment. 

On side $B$ (even cells), assign label $f(i,j)$ based on position. On side $W$ (odd cells), assign label $g(i,j)$. We want $f(i,j) + g(i',j') \leq T$ for all adjacent $(i,j) \in B, (i',j') \in W$.

Idea: Use $f(i,j) = $ rank of $(i,j)$ in some ordering of $B$-cells, and $g(i,j) = 51 - $ rank of $(i,j)$ in the same ordering of $W$-cells. Then $f + g = 51$ for "corresponding" cells, but adjacent cells aren't corresponding.

Hmm, let me try a different idea. 

**Idea: "Row-complementary" assignment**

For each row $i$, the even cells and odd cells alternate. In row $i$, the even cells are at positions $j$ with $j \equiv i \pmod{2}$ (or $j \equiv i+1 \pmod{2}$, depending on convention).

Actually, let me think about a "snake" or "spiral" assignment.

**Idea: "Spiral" assignment**

Assign labels 1 to 50 on side $B$ in a spiral order (from outside in), and labels 1 to 50 on side $W$ in a reverse spiral order (from inside out). Then high labels on $B$ (outer) are adjacent to low labels on $W$ (outer), and low labels on $B$ (inner) are adjacent to high labels on $W$ (inner). The max sum would be at the "transition" point.

Hmm, this might not be optimal. Let me think more carefully.

**Idea: "Anti-diagonal" assignment**

Consider the anti-diagonal sum $s = i + j$. Cells with $s = 2$ (just $(1,1)$) to $s = 20$ (just $(10,10)$). 

On side $B$, assign high labels to cells with low $s$ (near $(1,1)$) and low labels to cells with high $s$ (near $(10,10)$). On side $W$, assign low labels to cells with low $s$ and high labels to cells with high $s$.

Then, adjacent cells have $s$ values differing by 1. A $B$-cell with $s = k$ has label roughly $r_B(k)$, and its $W$-neighbors have $s = k \pm 1$ with labels roughly $r_W(k \pm 1)$. We want $r_B(k) + r_W(k \pm 1) \leq T$.

If $r_B$ is decreasing and $r_W$ is increasing, then $r_B(k) + r_W(k+1) \leq r_B(k) + r_W(k) + \Delta$ where $\Delta$ is the increase per step. The maximum would be at the "crossover" point where $r_B(k) \approx r_W(k)$.

This is still vague. Let me try to think about the answer differently.

**Let me try to think about the problem as a linear program relaxation.**

Actually, let me just try to construct an explicit arrangement and compute $T$.

**Explicit construction:**

Let me try the following. On side $B$ (even cells), sort cells by $i + j$ (anti-diagonal) in increasing order, and assign labels 50, 49, ..., 1. On side $W$ (odd cells), sort cells by $i + j$ in increasing order, and assign labels 1, 2, ..., 50.

So $B$-cells with small $i+j$ get high labels, and $W$-cells with small $i+j$ get low labels.

For a $B$-cell at $(i,j)$ with $s = i+j$, its label is approximately $50 - \text{rank}_B(s)$. For a $W$-cell at $(i',j')$ with $s' = i'+j'$, its label is approximately $\text{rank}_W(s')$.

Adjacent cells have $s$ values differing by 1. A $B$-cell with $s = k$ is adjacent to $W$-cells with $s = k-1$ and $s = k+1$.

The $W$-cell with $s = k+1$ has label $\text{rank}_W(k+1) \approx \text{rank}_W(k) + (\text{number of } W\text{-cells with } s = k+1)$. Hmm, this depends on the distribution of cells across anti-diagonals.

Let me count. For the 10×10 grid, the anti-diagonal $s = i + j$ ranges from 2 to 20. The number of cells with $s = k$ is $\min(k-1, 21-k, 10)$ for $k = 2, ..., 20$.

$s=2$: 1 cell, $s=3$: 2, $s=4$: 3, ..., $s=11$: 10, $s=12$: 9, ..., $s=20$: 1.

Even $s$ (B-cells): $s = 2, 4, 6, 8, 10, 12, 14, 16, 18, 20$.
Counts: 1, 3, 5, 7, 9, 9, 7, 5, 3, 1. Total = 1+3+5+7+9+9+7+5+3+1 = 50. ✓

Odd $s$ (W-cells): $s = 3, 5, 7, 9, 11, 13, 15, 17, 19$.
Counts: 2, 4, 6, 8, 10, 8, 6, 4, 2. Total = 2+4+6+8+10+8+6+4+2 = 50. ✓

Now, on side $B$, assign labels in decreasing order of $s$ (so $s=20$ gets label 1, $s=18$ gets labels 2,3,4, etc.). Wait, I said small $s$ gets high labels. So $s=2$ gets label 50, $s=4$ gets labels 47,48,49, etc.

Actually, let me be more precise. On side $B$, cells with $s=2$ get the highest label (50), cells with $s=4$ get the next 3 highest (47, 48, 49), cells with $s=6$ get the next 5 highest (42, 43, 44, 45, 46), etc.

On side $W$, cells with $s=3$ get the lowest labels (1, 2), cells with $s=5$ get the next 4 (3, 4, 5, 6), etc.

Now, a $B$-cell with $s = k$ is adjacent to $W$-cells with $s = k-1$ and $s = k+1$.

The $B$-cell with $s=2$ (label 50) is adjacent to $W$-cells with $s=1$ (none) and $s=3$ (labels 1, 2). So the max sum involving this cell is $50 + 2 = 52$.

The $B$-cells with $s=4$ (labels 47, 48, 49) are adjacent to $W$-cells with $s=3$ (labels 1, 2) and $s=5$ (labels 3, 4, 5, 6). Max sum: $49 + 6 = 55$.

The $B$-cells with $s=6$ (labels 42-46) are adjacent to $W$-cells with $s=5$ (labels 3-6) and $s=7$ (labels 7-12). Max sum: $46 + 12 = 58$.

The $B$-cells with $s=8$ (labels 35-41) are adjacent to $W$-cells with $s=7$ (labels 7-12) and $s=9$ (labels 13-20). Max sum: $41 + 20 = 61$.

The $B$-cells with $s=10$ (labels 26-34) are adjacent to $W$-cells with $s=9$ (labels 13-20) and $s=11$ (labels 21-30). Max sum: $34 + 30 = 64$.

The $B$-cells with $s=12$ (labels 17-25) are adjacent to $W$-cells with $s=11$ (labels 21-30) and $s=13$ (labels 31-38). Max sum: $25 + 38 = 63$.

The $B$-cells with $s=14$ (labels 10-16) are adjacent to $W$-cells with $s=13$ (labels 31-38) and $s=15$ (labels 39-44). Max sum: $16 + 44 = 60$.

The $B$-cells with $s=16$ (labels 5-9) are adjacent to $W$-cells with $s=15$ (labels 39-44) and $s=17$ (labels 45-48). Max sum: $9 + 48 = 57$.

The $B$-cells with $s=18$ (labels 2-4) are adjacent to $W$-cells with $s=17$ (labels 45-48) and $s=19$ (labels 49-50). Max sum: $4 + 50 = 54$.

The $B$-cell with $s=20$ (label 1) is adjacent to $W$-cells with $s=19$ (labels 49-50). Max sum: $1 + 50 = 51$.

So the maximum over all is $\max(52, 55, 58, 61, 64, 63, 60, 57, 54, 51) = 64$.

But wait, this is a rough calculation. The actual max depends on the specific assignment within each anti-diagonal. The max sum for $s=10$ is $34 + 30 = 64$, but this assumes the worst-case pairing within the anti-diagonal. With a careful assignment, we might do better.

But also, this construction gives $T \approx 64$, so $S \approx 114$. This seems high. Let me see if there's a better construction.

The issue is that the anti-diagonal ordering creates a "gradient" that's too steep in the middle. The max occurs at $s = 10/11$ where both sides have moderate-to-high labels.

**Better idea: "Complementary within anti-diagonals"**

Instead of assigning high labels to low-$s$ $B$-cells and low labels to low-$s$ $W$-cells, what if we interleave more carefully?

Actually, the problem with the above construction is that in the middle of the grid, both $B$ and $W$ cells have moderate labels, and their sums are high. We need a different approach.

**Idea: "Chessboard reversal"**

What if on side $B$, we assign labels in order of $i + j$ (increasing), and on side $W$, we assign labels in order of $i + j$ (decreasing)? Then $B$-cells with small $s$ get low labels, and $W$-cells with small $s$ get high labels. 

$B$-cell with $s=2$ (label 1) adjacent to $W$-cells with $s=3$ (labels 49, 50). Max sum: $1 + 50 = 51$.
$B$-cells with $s=4$ (labels 2, 3, 4) adjacent to $W$-cells with $s=3$ (labels 49, 50) and $s=5$ (labels 45-48). Max sum: $4 + 50 = 54$.

Hmm, this is the same as before but reversed. The max would still be around 64.

The problem is that the anti-diagonal approach creates a gradient, and the max sum is at the point where the two gradients cross.

**Idea: "2D complementary"**

Instead of a 1D gradient (along $i+j$), use a 2D pattern. For example, on side $B$, assign high labels to cells where both $i$ and $j$ are small (corner $(1,1)$ region), and on side $W$, assign high labels to cells where both $i$ and $j$ are large (corner $(10,10)$ region).

But this is essentially the same as the anti-diagonal approach.

**Idea: "Interleaved" assignment**

What if we don't use a gradient at all, but instead interleave high and low labels in a checkerboard-like pattern within each color class?

For example, on side $B$, assign labels such that high labels are surrounded by low labels on side $W$, and vice versa. This is essentially what we want, but the grid structure constrains how we can do this.

Let me think about the problem differently. 

**Reformulation as a graph coloring problem:**

We want to find a bijection $f: B \to \{1,...,50\}$ and $g: W \to \{1,...,50\}$ minimizing $\max_{(b,w) \in E} (f(b) + g(w))$.

This is equivalent to: find the minimum $T$ such that there exist bijections $f, g$ with $f(b) + g(w) \leq T$ for all $(b,w) \in E$.

This is a kind of "bipartite bandwidth" or "labeling" problem.

**Lower bound via edge counting:**

The grid has 180 edges. The sum of all edge sums is $\sum_{(b,w) \in E} (f(b) + g(w)) = \sum_{b \in B} f(b) \cdot d(b) + \sum_{w \in W} g(w) \cdot d(w)$.

To minimize the max edge sum, we'd like the edge sums to be as uniform as possible. The average edge sum is $\frac{\sum_{b} f(b) d(b) + \sum_{w} g(w) d(w)}{180}$.

$\sum_{b} f(b) d(b)$: to minimize this, assign low labels to high-degree cells. $\sum_{w} g(w) d(w)$: same.

The minimum of $\sum_{b} f(b) d(b)$ is achieved by assigning label 1 to the highest-degree cell, label 2 to the next, etc. (rearrangement inequality).

Degree distribution on each side: 2 cells of degree 2, 16 of degree 3, 32 of degree 4.

$\sum_{b} f(b) d(b)$: assign labels 1-32 to degree-4 cells, labels 33-48 to degree-3 cells, labels 49-50 to degree-2 cells.
$= 4 \cdot (1+2+...+32) + 3 \cdot (33+34+...+48) + 2 \cdot (49+50)$
$= 4 \cdot 528 + 3 \cdot 612 + 2 \cdot 99$
$= 2112 + 1836 + 198 = 4146$.

Similarly, $\sum_{w} g(w) d(w) = 4146$ (same degree distribution).

Total edge sum = $4146 + 4146 = 8292$. Average = $8292 / 180 = 46.07$.

So the average edge sum is about 46, meaning the max is at least 47 (since max ≥ average, and max must be an integer). But this is a weak bound.

**Better lower bound:**

Let me think about the "local" structure. Consider a cell $b$ with degree 4 (interior). It has 4 neighbors in $W$. The sum of the 4 edge sums is $4 f(b) + g(w_1) + g(w_2) + g(w_3) + g(w_4)$. The max of these 4 sums is at least $\frac{4 f(b) + g(w_1) + ... + g(w_4)}{4}$.

If $f(b) = 50$ (highest label) and $b$ is interior (degree 4), the 4 neighbors have labels summing to at least $1+2+3+4 = 10$ (if they're the 4 lowest). The max edge sum is at least $(4 \cdot 50 + 10) / 4 = 52.5$, so at least 53.

But we'd place label 50 at a corner (degree 2), not interior. So this doesn't directly apply.

Let me think about the problem more carefully.

**Let me try to find the answer by considering the structure more carefully.**

I'll think about what happens with the "complementary" assignment where we try to make $f(b) + g(w) \approx T$ for all edges.

If we could achieve $f(b) + g(w) = T$ for all edges, that would be ideal. But this is generally impossible due to the graph structure.

For a path graph $P_n$ (1×n grid), the optimal $T$ in the reformulated problem (with $n/2$ labels on each side, assuming $n$ even) can be computed. But the 10×10 grid is more complex.

Let me try a different approach: think about the problem as an integer program and try to find the answer by reasoning about the constraints.

**Key constraint:** For each edge $(b,w)$, $f(b) + g(w) \leq T$. This means $g(w) \leq T - f(b)$ for all neighbors $b$ of $w$, i.e., $g(w) \leq T - \max_{b \sim w} f(b)$. Similarly, $f(b) \leq T - \max_{w \sim b} g(w)$.

So if we define $F(b) = f(b)$ and $G(w) = g(w)$, then:
$G(w) \leq T - \max_{b \sim w} F(b)$ for all $w \in W$.
$F(b) \leq T - \max_{w \sim b} G(w)$ for all $b \in B$.

This is a system of constraints. The question is: what's the minimum $T$ for which there exist bijections $F: B \to \{1,...,50\}$ and $G: W \to \{1,...,50\}$ satisfying these?

Let me think about a "harmonic" or "fixed point" approach. If we set $F(b) = T - \max_{w \sim b} G(w)$ and $G(w) = T - \max_{b \sim w} F(b)$, we get a system that might have a solution.

This is related to the concept of "graph coloring" where the label of each vertex is determined by its neighbors' labels.

Let me try a specific construction.

**Construction: "Row-alternating"**

Divide the grid into two halves: top 5 rows and bottom 5 rows. On side $B$, assign high labels (26-50) to the top half and low labels (1-25) to the bottom half. On side $W$, assign low labels (1-25) to the top half and high labels (26-50) to the bottom half.

Each half has 25 $B$-cells and 25 $W$-cells.

In the top half: $B$-cells have labels 26-50, $W$-cells have labels 1-25. Max edge sum within top half: $50 + 25 = 75$. That's bad.

The boundary between top and bottom halves (between rows 5 and 6): $B$-cells in row 5 have labels 26-50, $W$-cells in row 6 have labels 26-50. Edge sum: up to $50 + 50 = 100$. Even worse.

This doesn't work. The problem is that at the boundary, both sides have high labels.

**Construction: "Finer interleaving"**

What if we interleave at a finer scale? For example, alternate high and low labels in a checkerboard pattern within each color class.

But within a color class, cells are not adjacent (they're on the same side of the bipartition), so we can freely assign labels. The constraint is only between the two color classes.

Let me think about the "dual" problem. We want to find a permutation $\sigma$ of $\{1,...,50\}$ (for $B$) and $\tau$ of $\{1,...,50\}$ (for $W$) such that $\sigma(b) + \tau(w) \leq T$ for all edges $(b,w)$.

Equivalently, $\tau(w) \leq T - \sigma(b)$ for all $b \sim w$, i.e., $\tau(w) \leq T - \max_{b \sim w} \sigma(b)$.

So $\tau(w) \leq T - M(w)$ where $M(w) = \max_{b \sim w} \sigma(b)$.

For $\tau$ to be a bijection onto $\{1,...,50\}$, we need $\max_w \tau(w) = 50$, so $50 \leq T - \min_w M(w)$, i.e., $T \geq 50 + \min_w M(w)$.

Also, the number of $w$'s with $\tau(w) \leq T - M(w)$ must be at least 50 (since $\tau$ is a bijection, all 50 values must be assigned). Actually, $\tau(w) \leq T - M(w)$ for each $w$, and $\tau$ is a bijection, so we need the values $\{1,...,50\}$ to be assignable to the 50 $w$'s such that $\tau(w) \leq T - M(w)$. This is possible iff for each $k$, the number of $w$'s with $T - M(w) \geq k$ is at least $51 - k$ (i.e., at least $51 - k$ $w$'s can take values $\geq k$). 

Actually, the condition is: for each $k \in \{1,...,50\}$, the number of $w$'s with $T - M(w) \geq k$ is at least the number of values in $\{k, k+1, ..., 50\}$ that need to be assigned, which is $51 - k$. But actually, it's a standard matching condition: we can assign values to $w$'s such that $\tau(w) \leq T - M(w)$ iff for every $k$, $|\{w : T - M(w) \geq k\}| \geq 51 - k$.

Equivalently, $|\{w : M(w) \leq T - k\}| \geq 51 - k$ for all $k = 1, ..., 50$.

Let $m = T - k$, so $k = T - m$, and the condition becomes: $|\{w : M(w) \leq m\}| \geq 51 - (T - m) = m + 51 - T$ for all $m$ (where $k$ ranges from 1 to 50, so $m$ ranges from $T - 50$ to $T - 1$).

For $m < T - 50$: the condition is $|\{w : M(w) \leq m\}| \geq m + 51 - T$, but $m + 51 - T \leq 0$, so the condition is trivially satisfied.

For $m \geq T - 50$ (and $m \leq T - 1$): $|\{w : M(w) \leq m\}| \geq m + 51 - T$.

For $m \geq 50$: $|\{w : M(w) \leq m\}| = 50 \geq m + 51 - T$ iff $T \geq m + 1$, which is satisfied for $m \leq T - 1$.

So the binding constraints are for $m$ in $\{T - 50, ..., 49\}$ (assuming $T \geq 51$): $|\{w : M(w) \leq m\}| \geq m + 51 - T$.

Now, $M(w) = \max_{b \sim w} \sigma(b)$, and $\sigma$ is a bijection from $B$ to $\{1,...,50\}$. The function $M(w)$ depends on the assignment $\sigma$.

To minimize $T$, we want to choose $\sigma$ to make $M(w)$ as small as possible for as many $w$'s as possible. But $M(w) = \max_{b \sim w} \sigma(b)$, so to make $M(w)$ small, we need all neighbors of $w$ to have small $\sigma$ values. But each $b$ is a neighbor of multiple $w$'s, so there's a trade-off.

This is essentially the same problem from the other direction. Let me try to think about specific values.

**Symmetric construction attempt:**

Let me try to construct an assignment where $f(b) + g(w) \leq T$ for a specific $T$, and find the minimum such $T$.

Let me try $T = 55$ (so $S = 105$).

We need $f(b) + g(w) \leq 55$ for all edges. So $g(w) \leq 55 - f(b)$ for all $b \sim w$, i.e., $g(w) \leq 55 - \max_{b \sim w} f(b)$.

If $f(b) = 50$ (at a corner, degree 2), its 2 neighbors need $g \leq 5$.
If $f(b) = 49$ (at a corner, degree 2), its 2 neighbors need $g \leq 6$.
If $f(b) = 48$ (at an edge, degree 3), its 3 neighbors need $g \leq 7$.
...

And similarly for $g$'s high values.

Let me think about whether $T = 55$ is achievable.

On side $B$, the top labels and their neighbor constraints:
- Label 50 (corner, deg 2): 2 neighbors need $g \leq 5$.
- Label 49 (corner, deg 2): 2 neighbors need $g \leq 6$.
- Label 48 (edge, deg 3): 3 neighbors need $g \leq 7$.
- Label 47 (edge, deg 3): 3 neighbors need $g \leq 8$.
- ...

On side $W$, the top labels and their neighbor constraints:
- Label 50 (corner, deg 2): 2 neighbors need $f \leq 5$.
- Label 49 (corner, deg 2): 2 neighbors need $f \leq 6$.
- Label 48 (edge, deg 3): 3 neighbors need $f \leq 7$.
- ...

Now, the $W$-cells that are neighbors of $B$'s label-50 cell need $g \leq 5$. There are 2 such cells. The $W$-cells that have $g = 50, 49, 48, ..., 46$ (5 cells) must NOT be among these 2 cells (since $50, 49, 48, 47, 46 > 5$). Similarly, the $W$-cells with $g \geq 46$ must not be neighbors of $B$'s label-50 cell.

Also, the $W$-cells with $g \geq 45$ must not be neighbors of $B$'s label-49 cell (since $45 > 6$). Wait, $g \leq 6$ for neighbors of label 49, so $g \geq 7$ can't be a neighbor. So $W$-cells with $g \geq 7$ must not be neighbors of $B$'s label-49 cell.

Let me think about this more carefully. The $W$-cells with high $g$ values must be far from the $B$-cells with high $f$ values.

Let me try to place the high-$f$ $B$-cells in the top-left corner and the high-$g$ $W$-cells in the bottom-right corner.

$B$-corners: $(1,1)$ and $(10,10)$. $W$-corners: $(1,10)$ and $(10,1)$.

Place $f = 50$ at $B$-corner $(1,1)$ (neighbors: $(1,2), (2,1)$ in $W$).
Place $f = 49$ at $B$-corner $(10,10)$ (neighbors: $(10,9), (9,10)$ in $W$).
Place $g = 50$ at $W$-corner $(10,1)$ (neighbors: $(10,2), (9,1)$ in $B$).
Place $g = 49$ at $W$-corner $(1,10)$ (neighbors: $(1,9), (2,10)$ in $B$).

Check: $f(1,1) = 50$, neighbors $(1,2)$ and $(2,1)$ need $g \leq 5$.
$g(10,1) = 50$, neighbors $(10,2)$ and $(9,1)$ need $f \leq 5$.

Are $(1,2)$ or $(2,1)$ the same as $(10,1)$? No. Good.

Now, $(1,2)$ and $(2,1)$ need $g \leq 5$. $(10,2)$ and $(9,1)$ need $f \leq 5$.

$f = 49$ at $(10,10)$: neighbors $(10,9), (9,10)$ need $g \leq 6$.
$g = 49$ at $(1,10)$: neighbors $(1,9), (2,10)$ need $f \leq 6$.

So on side $W$: $(1,2), (2,1)$ need $g \leq 5$, and $(10,9), (9,10)$ need $g \leq 6$. These are 4 distinct cells. We need 2 labels $\leq 5$ and 2 more labels $\leq 6$.

On side $B$: $(10,2), (9,1)$ need $f \leq 5$, and $(1,9), (2,10)$ need $f \leq 6$. 4 distinct cells. We need 2 labels $\leq 5$ and 2 more labels $\leq 6$.

This seems feasible so far. Let me continue.

$f = 48$ at some $B$-edge cell. Which edge cell? It should be far from the high-$g$ $W$-cells. The high-$g$ $W$-cells are near $(10,1)$ and $(1,10)$. So place $f = 48$ near $(1,1)$, say at $(1,3)$ (edge, degree 3, neighbors $(1,2), (1,4), (2,3)$ in $W$).

$(1,2)$ already needs $g \leq 5$ (from $f=50$). Now also $g \leq 55 - 48 = 7$. The binding constraint is $g \leq 5$.
$(1,4)$ and $(2,3)$ need $g \leq 7$.

$g = 48$ at some $W$-edge cell, far from high-$f$ $B$-cells. Place near $(10,1)$, say at $(10,3)$ (edge, degree 3, neighbors $(10,2), (10,4), (9,3)$ in $B$).

$(10,2)$ already needs $f \leq 5$. Now also $f \leq 7$. Binding: $f \leq 5$.
$(10,4)$ and $(9,3)$ need $f \leq 7$.

Continuing:
$f = 47$ at $(1,5)$ (edge, deg 3, neighbors $(1,4), (1,6), (2,5)$). $(1,4)$ needs $g \leq \min(7, 8) = 7$. $(1,6), (2,5)$ need $g \leq 8$.

$g = 47$ at $(10,5)$ (edge, deg 3, neighbors $(10,4), (10,6), (9,5)$). $(10,4)$ needs $f \leq \min(7, 8) = 7$. $(10,6), (9,5)$ need $f \leq 8$.

$f = 46$ at $(1,7)$ (edge, deg 3, neighbors $(1,6), (1,8), (2,7)$). $(1,6)$ needs $g \leq \min(8, 9) = 8$. $(1,8), (2,7)$ need $g \leq 9$.

$g = 46$ at $(10,7)$ (edge, deg 3, neighbors $(10,6), (10,8), (9,7)$). $(10,6)$ needs $f \leq \min(8, 9) = 8$. $(10,8), (9,7)$ need $f \leq 9$.

$f = 45$ at $(1,9)$ (edge, deg 3, neighbors $(1,8), (1,10), (2,9)$). But $(1,10)$ is a $W$-corner with $g = 49$. Check: $f(1,9) + g(1,10) = 45 + 49 = 94 > 55$. BAD!

So we can't place $f = 45$ at $(1,9)$ because it's adjacent to $g = 49$ at $(1,10)$.

The constraint is $f(1,9) \leq 55 - 49 = 6$. So $(1,9)$ must have $f \leq 6$. But we already said $(1,9)$ needs $f \leq 6$ (from $g = 49$ at $(1,10)$). So $(1,9)$ has $f \leq 6$, which is fine—it's a low-$f$ cell.

So the high-$f$ cells near $(1,1)$ can only go up to the cells that aren't adjacent to high-$g$ cells near $(1,10)$.

The $W$-corner $(1,10)$ has $g = 49$, and its $B$-neighbors are $(1,9)$ and $(2,10)$. These need $f \
