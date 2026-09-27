# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Ivan places checkers on an $n \times n$ table according to the following rule: a checker can be placed in cell $C$ if there is no checker there yet, and in the remaining $2n - 2$ cells of the row and column of $C$ there is an even number of checkers. After placing $M$ checkers, Ivan found that it is impossible to place any more checkers. Let $f(n)$ be the minimum possible value of $M$. Find the value of $f(20) + f(21)$.       — 题目文本
#   According to the solution, the minimum number of checkers $M$ for a given $n$ is $f(n) = \frac{n^{2} + 1}{2}$ when $n$ is odd, and $f(n) = \frac{n^{2}}{2} + n$ when $n$ is even.
For $n = 20$, $f(20) = \frac{20^2}{2} + 20 = 200 + 20 = 220$.
For $n = 21$, $f(21) = \frac{21^2 + 1}{2} = \frac{441 + 1}{2} = \frac{442}{2} = 221$.
The sum is $220 + 221 = 441$.  — 标准解答
#   Let me analyze this problem carefully.

We have an n×n table. A checker can be placed in cell C if:
1. There is no checker there yet
2. In the remaining 2n-2 cells of the row and column of C, there is an even number of checkers.

After placing M checkers, it's impossible to place any more. f(n) = minimum possible M. Find f(20) + f(21).

Let me think about this. Let's denote the number of checkers in row i as r_i and in column j as c_j. For cell (i,j), the number of checkers in its row and column (excluding itself) is (r_i - [checker at (i,j)]) + (c_j - [checker at (i,j)]) = r_i + c_j - 2*[checker at (i,j)]. Since the cell is empty when we consider placing, this is r_i + c_j.

Wait, the 2n-2 cells are the other cells in row i (n-1 cells) and column j (n-1 cells), total 2n-2. The number of checkers in those cells is r_i + c_j (since cell (i,j) is empty, r_i counts checkers in row i not including (i,j), and c_j counts checkers in column j not including (i,j)). Actually r_i is the total in row i, but since (i,j) is empty, r_i = number of checkers in row i excluding (i,j). Similarly c_j. So the count is r_i + c_j.

So we can place a checker at (i,j) iff (i,j) is empty and r_i + c_j is even.

A configuration is "maximal" (no more checkers can be placed) iff for every empty cell (i,j), r_i + c_j is odd.

We want to minimize the total number of checkers M in a maximal configuration.

Let me think about the structure. Let's say a row is "even" if r_i is even, "odd" if r_i is odd. Similarly for columns.

For an empty cell (i,j), we need r_i + c_j odd, meaning one of r_i, c_j is even and the other is odd.

So: for every empty cell (i,j), row i and column j have different parities.

Equivalently: if row i and column j have the same parity, then cell (i,j) must be occupied.

Let me partition rows into even rows (E_r) and odd rows (O_r), and columns into even columns (E_c) and odd columns (O_c).

Cells where row and column have same parity: (E_r, E_c) and (O_r, O_c) — these must all be occupied.

Cells where row and column have different parity: (E_r, O_c) and (O_r, E_c) — these can be empty or occupied.

But wait, we also need the parities to be consistent. If a row is in E_r, it has an even number of checkers. The occupied cells in that row are: all cells in (E_r row, E_c columns) [same parity, must be occupied] plus possibly some cells in (E_r row, O_c columns) [different parity, optional].

Let me denote:
- a = number of even rows
- b = number of odd rows = n - a
- c = number of even columns
- d = number of odd columns = n - c

For an even row i (in E_r): it must occupy all cells in E_c columns (that's c cells) plus optionally some in O_c columns. The total must be even. c + (optional count) must be even. So optional count must have the same parity as c.

For an odd row i (in O_r): it must occupy all cells in O_c columns (that's d cells) plus optionally some in E_c columns. The total must be odd. d + (optional count) must be odd. So optional count must have parity different from d, i.e., optional count ≡ 1 - d (mod 2) ≡ 1+d (mod 2).

For an even column j (in E_c): it must occupy all cells in E_r rows (that's a cells) plus optionally some in O_r rows. Total must be even. a + optional must be even. So optional ≡ a (mod 2).

For an odd column j (in O_c): it must occupy all cells in O_r rows (that's b cells) plus optionally some in E_r rows. Total must be odd. b + optional must be odd. So optional ≡ 1+b (mod 2) ≡ 1-b (mod 2).

Now, the mandatory checkers are:
- (E_r, E_c): a × c cells
- (O_r, O_c): b × d cells

The optional cells are:
- (E_r, O_c): a × d cells
- (O_r, E_c): b × c cells

We want to minimize total checkers = mandatory + optional.

Mandatory = ac + bd = ac + (n-a)(n-c).

To minimize, we want to minimize the optional checkers placed, subject to parity constraints.

Let me think about the optional cells. Let x = number of optional cells in (E_r, O_c) that are occupied, and y = number of optional cells in (O_r, E_c) that are occupied.

Constraints:
- For each even row: the number of occupied optional cells (in O_c) must have parity ≡ c (mod 2).
- For each odd row: the number of occupied optional cells (in E_c) must have parity ≡ 1+d (mod 2).
- For each even column: the number of occupied optional cells (in O_r) must have parity ≡ a (mod 2).
- For each odd column: the number of occupied optional cells (in E_r) must have parity ≡ 1+b (mod 2).

These are parity constraints on rows and columns of the optional sub-matrices.

Let me think of the (E_r, O_c) sub-matrix of size a × d. Each row (even row) needs the sum to have parity ≡ c (mod 2). Each column (odd column) needs the sum to have parity ≡ 1+b (mod 2).

The minimum number of 1s in an a × d binary matrix where each row sum has a specified parity and each column sum has a specified parity.

For this to be feasible, the total parity must be consistent: sum of row parities ≡ sum of column parities (mod 2).

Sum of row parities for (E_r, O_c): a rows, each with parity c. Total ≡ ac (mod 2).
Sum of column parities for (E_r, O_c): d columns, each with parity 1+b. Total ≡ d(1+b) (mod 2).

Need: ac ≡ d(1+b) (mod 2).

Similarly for (O_r, E_c) sub-matrix of size b × c. Each row (odd row) needs sum parity ≡ 1+d. Each column (even column) needs sum parity ≡ a.

Sum of row parities: b(1+d) (mod 2).
Sum of column parities: ca (mod 2).

Need: b(1+d) ≡ ca (mod 2).

Let me check if these are the same condition. d(1+b) = d + bd. ac. So ac ≡ d + bd (mod 2), i.e., ac + d + bd ≡ 0 (mod 2), i.e., ac + d(1+b) ≡ 0 (mod 2).

Second: b(1+d) ≡ ca (mod 2), i.e., b + bd ≡ ac (mod 2), i.e., ac + b + bd ≡ 0 (mod 2), i.e., ac + b(1+d) ≡ 0 (mod 2).

These are different conditions in general. Let me see... ac + d + bd ≡ 0 and ac + b + bd ≡ 0. Subtracting: d - b ≡ 0 (mod 2), i.e., d ≡ b (mod 2), i.e., (n-c) ≡ (n-a) (mod 2), i.e., a ≡ c (mod 2).

So if a ≡ c (mod 2), both conditions are the same: ac + b + bd ≡ 0 (mod 2).

If a ≢ c (mod 2), the two conditions are contradictory, meaning we can't satisfy both sub-matrix constraints simultaneously? Wait, no — the two sub-matrices are independent. Let me reconsider.

Actually, the (E_r, O_c) and (O_r, E_c) sub-matrices are independent in terms of which cells they cover. But the parity constraints come from the row/column totals which involve both mandatory and optional cells.

Wait, let me re-examine. For an even row i, the total checkers = c (mandatory in E_c) + (optional in O_c). This must be even. So optional in O_c for row i must have parity ≡ c (mod 2). This only involves the (E_r, O_c) sub-matrix. ✓

For an even column j, the total checkers = a (mandatory in E_r) + (optional in O_r). This must be even. So optional in O_r for column j must have parity ≡ a (mod 2). This only involves the (O_r, E_c) sub-matrix. ✓

So the two sub-matrices are indeed independent. Each has its own feasibility condition.

(E_r, O_c): feasible iff ac ≡ d(1+b) (mod 2).
(O_r, E_c): feasible iff b(1+d) ≡ ca (mod 2).

If both are feasible, the minimum optional checkers is the sum of minimums for each sub-matrix.

If one is infeasible, we need to adjust a, c (the partition).

Hmm, this is getting complex. Let me think about the minimum number of 1s in an m × k binary matrix with given row and column parities.

If all row parities are 0 and all column parities are 0: minimum is 0 (all zeros).
If all row parities are 0 and some column parities are 1: need... if all row parities are 0, total is even, so number of odd columns must be even. Minimum: place 1s to make odd columns odd. If there are t odd columns (t even), we can place 2 ones in one row covering 2 odd columns each... actually minimum is t/2 if we can pair them up, but we need t ≤ m×k and... Let me think more carefully.

Actually, the minimum number of 1s in an m×k binary matrix where row i has parity p_i and column j has parity q_j (with sum p_i ≡ sum q_j mod 2) is:

If all p_i = 0 and all q_j = 0: 0.
Otherwise: at least 1, but could be more.

Let me think about specific cases. Actually, let me think about it differently. The minimum is max(number of odd rows, number of odd columns) if that's achievable, but with parity constraint...

Hmm, let me think about it more carefully. In an m×k matrix:
- Let r = number of rows with odd parity
- Let s = number of columns with odd parity
- Need r ≡ s (mod 2)

The minimum number of 1s: We need each odd row to have at least 1 one, and each odd column to have at least 1 one. But a single 1 can satisfy both an odd row and an odd column. 

If r > 0 and s > 0: We can place min(r,s) ones at intersections of odd rows and odd columns (each such one satisfies one odd row and one odd column). Then we have |r-s| remaining odd rows or columns. If r > s, we have r-s odd rows left, each needs one more 1 (in an even column). We can pair them up: place 2 ones in the same even column for 2 odd rows. So we need r-s additional ones if r-s is even (which it is since r ≡ s mod 2). Wait, r-s is even. So (r-s) additional ones, each in a distinct odd row, in even columns. But each such 1 in an even column doesn't change the column parity (it's already even, adding 1 makes it odd — bad). 

Hmm wait, I need to be more careful. Let me reconsider.

Let's say r odd rows and s odd columns, r ≡ s (mod 2).

Case 1: r = 0, s = 0. Min = 0.
Case 2: r = 0, s > 0 (s even). All rows even, s columns odd. We need s columns to be odd but all rows even. Place 2 ones in each odd column (in 2 different rows). That uses 2s ones but... can we do better? Actually, we can place ones such that each odd column gets an odd number and each row gets an even number. The minimum is s (place 1 in each odd column, all in the same row — but then that row has s ones, which is even since s is even). So min = s. Wait, but we need m ≥ 1 and k ≥ s. If s ≤ k and m ≥ 1, we can place 1 one in each odd column, all in row 1. Row 1 has s ones (even, since s is even). All other rows have 0. Each odd column has 1 (odd). Each even column has 0 (even). So min = s.

Case 3: r > 0, s = 0 (r even). Similarly, min = r.

Case 4: r > 0, s > 0. Place ones at (odd row i, odd column j) for i = 1..min(r,s). This gives min(r,s) ones. Each of the first min(r,s) odd rows gets 1 (odd ✓), each of the first min(r,s) odd columns gets 1 (odd ✓). If r > s: remaining r-s odd rows need 1 more each. But all columns are already satisfied (s odd columns are odd, rest are even). Adding a 1 to an even column makes it odd — bad. So we need to add 2 ones to each remaining odd row: one in an even column (making it odd) and one in the same even column in an even row (making it even again). Wait, that's getting complicated.

Actually, let me reconsider. If r > s, we have r - s remaining odd rows. We need each to get one more 1 (to be odd). But adding a 1 to any column changes its parity. If we add it to an already-odd column, it becomes even (bad). If we add it to an even column, it becomes odd (bad). 

So we can't just add single 1s. We need to add pairs. For each remaining odd row, add 2 ones in 2 different even columns. This makes the row have 1+2=3 (odd ✓), and each of the 2 even columns gets 1 (odd — bad). 

Hmm, this is getting complicated. Let me think differently.

Alternative approach: We need a binary matrix with specified row and column parities. The minimum number of 1s.

Think of it as: we need to "fix" the parities. Start with all zeros (all parities 0). We need row parities p_i and column parities q_j.

The minimum number of 1s is related to the structure. Let me think about it as a graph problem or use a known result.

Actually, I think the answer is: if all parities are 0, min = 0. Otherwise, min = max(r, s) where r = number of odd rows, s = number of odd columns, provided r ≡ s (mod 2) and the matrix is large enough.

Wait, let me verify with small cases. 2×2 matrix, row parities (1,1), column parities (1,1). r=2, s=2. max=2. Can we do it with 2? Place ones at (1,1) and (2,2). Row 1: 1 (odd ✓), Row 2: 1 (odd ✓), Col 1: 1 (odd ✓), Col 2: 1 (odd ✓). Yes! Min = 2 = max(2,2). ✓

2×2 matrix, row parities (1,0), column parities (1,0). r=1, s=1. max=1. Place 1 at (1,1). Row 1: 1 (odd ✓), Row 2: 0 (even ✓), Col 1: 1 (odd ✓), Col 2: 0 (even ✓). Min = 1. ✓

3×3 matrix, row parities (1,1,0), column parities (1,0,0). r=2, s=1. max=2. r-s=1 which is odd, but r≡s mod 2 means 2≡1? No, 2≡0, 1≡1, so 2≢1 mod 2. Infeasible! Indeed, sum of row parities = 2 (even), sum of col parities = 1 (odd). Not consistent. ✓

3×3 matrix, row parities (1,1,0), column parities (1,1,0). r=2, s=2. max=2. Place at (1,1),(2,2). Row 1:1, Row 2:1, Row 3:0. Col 1:1, Col 2:1, Col 3:0. ✓ Min=2.

3×3, row parities (1,1,1), col parities (1,1,1). r=3,s=3. max=3. Place at (1,1),(2,2),(3,3). Each row 1, each col 1. ✓ Min=3.

3×3, row parities (1,1,1), col parities (1,0,0). r=3, s=1. 3≡1 mod 2? 3 is odd, 1 is odd, yes. max=3. Can we do 3? Place at (1,1),(2,1),(3,1)? Col 1: 3 (odd ✓), but rows 1,2,3 each have 1 (odd ✓). Cols 2,3: 0 (even ✓). But wait, that's 3 ones all in column 1. Col 1 has 3 (odd ✓). Yes! Min = 3 = max(3,1). 

Hmm wait, but can we do better? With 1 one: place at (1,1). Row 1: odd ✓, Col 1: odd ✓. But rows 2,3 are even (need odd). No. With 2 ones: need 3 odd rows, impossible with 2 ones (each one can make at most 1 row odd, unless... no, each 1 is in one row). Actually with 2 ones in 2 different rows, we get 2 odd rows, need 3. With 2 ones in same row, 1 odd row. So min is 3. But max(3,1)=3. ✓

What about 2×3, row parities (1,1), col parities (1,1,0). r=2, s=2. max=2. Place at (1,1),(2,2). ✓

What about 1×4, row parities (1), col parities (1,0,0,0). r=1, s=1. max=1. Place at (1,1). ✓

1×4, row parities (0), col parities (1,1,0,0). r=0, s=2. max=2. But all rows even, so we need 2 odd columns with an even number in the single row. Place 1 at (1,1) and (1,2). Row 1: 2 (even ✓), Col 1: 1 (odd ✓), Col 2: 1 (odd ✓). Min = 2 = s. ✓ (max(0,2)=2)

1×4, row parities (0), col parities (1,0,0,0). r=0, s=1. 0≡1? No. Infeasible. ✓

OK so it seems like the minimum is max(r, s) when feasible (r ≡ s mod 2), except when r=0 and s=0, min=0 (which is max(0,0)=0 anyway).

Wait, but there might be size constraints. If r > k (number of columns), we can't have r odd rows since each row needs at least 1 one and... actually no, a row can have multiple ones. Let me reconsider.

If r > 0 and s = 0 (r even): we need r odd rows, all columns even. Place 1 one in each of r rows, all in column 1. Column 1 gets r ones (even ✓ since r is even). Each of r rows gets 1 (odd ✓). Min = r. Need k ≥ 1. ✓

If r > 0 and s > 0: We need max(r,s) ones? Let me check r=4, s=2, 4×2 matrix. max=4. Place at (1,1),(2,2),(3,1),(4,2). Row 1:1, Row 2:1, Row 3:1, Row 4:1 (all odd ✓). Col 1:2 (even — bad, need odd). Hmm.

Let me redo. r=4 odd rows, s=2 odd columns. 4×2 matrix. We need 4 odd rows and 2 odd columns. 

Place at (1,1),(2,1),(3,2),(4,2). Col 1: 2 (even, bad). Col 2: 2 (even, bad).

Place at (1,1),(2,2),(3,1),(4,2). Col 1: 2 (even, bad). 

Hmm, with 4 ones in a 4×2 matrix, each column gets an even number if we distribute evenly. To get 2 odd columns, we need each column to have an odd count. With 4 ones total and 2 columns, we need odd+odd = even, so total is even ✓. But 4 = odd + odd means 1+3, 3+1. So col 1 has 1, col 2 has 3. Col 1 odd ✓, col 2 odd ✓. Rows: 3 rows have 1 one (in col 2), 1 row has 1 one (in col 1). All 4 rows odd ✓. So place at (1,1),(2,2),(3,2),(4,2). Col 1: 1 (odd ✓), Col 2: 3 (odd ✓). All rows: 1 each (odd ✓). Min = 4 = max(4,2). ✓

But wait, can we do it with 3? 3 ones, 4 rows: at most 3 rows have a 1, so at most 3 odd rows. Need 4. No. So min = 4. ✓

What about r=2, s=4, 2×4 matrix? max=4. 2 odd rows, 4 odd columns. Need each column odd. With 4 ones: place 1 in each column, distributed in 2 rows. Row 1: 2 (even, bad). Need odd rows. Row 1: 1 or 3, Row 2: 3 or 1. Place (1,1),(1,2),(2,3),(2,4)? Row 1: 2 (even, bad). Place (1,1),(2,2),(2,3),(2,4)? Row 1: 1 (odd ✓), Row 2: 3 (odd ✓). Col 1:1, Col 2:1, Col 3:1, Col 4:1 (all odd ✓). Min = 4. Can we do 3? 3 ones, 4 columns: at most 3 odd columns. Need 4. No. Min = 4 = max(2,4). ✓

So the minimum number of 1s in an m×k binary matrix with r odd rows and s odd columns (r ≡ s mod 2, feasible) is max(r, s).

But we also need m ≥ 1 and k ≥ 1 (non-degenerate), and we need r ≤ m and s ≤ k (can't have more odd rows than rows). Also, if r = 0 and s = 0, min = 0.

Wait, is there a case where max(r,s) doesn't work due to size? If r > 0, s > 0, and say r = m (all rows odd) and s = k (all columns odd), then max(r,s) = max(m,k). We need to place max(m,k) ones. If m ≥ k, place 1 in each row, distributing among k columns such that each column gets an odd number. Total = m ones, each column gets m/k... we need each column odd. m ones in k columns, each odd: sum of k odd numbers = k mod 2. Need m ≡ k (mod 2), which is given (r ≡ s mod 2, i.e., m ≡ k mod 2). So we need to write m as sum of k odd positive integers. Min sum of k odd positive integers = k. So need m ≥ k, i.e., r ≥ s, which is the case. ✓

OK so I'm fairly convinced: **the minimum number of 1s is max(r, s)** when the parity condition is satisfied and r,s are feasible (r ≤ m, s ≤ k), and 0 when r = s = 0.

Now, back to our problem. We have two independent sub-matrices:

**Sub-matrix 1: (E_r, O_c)**, size a × d.
- Row parities: each of the a rows needs parity ≡ c (mod 2). So if c is even, all rows even (r₁ = 0). If c is odd, all rows odd (r₁ = a).
- Column parities: each of the d columns needs parity ≡ 1+b (mod 2). So if 1+b is even (b odd), all columns even (s₁ = 0). If 1+b is odd (b even), all columns odd (s₁ = d).
- Feasibility: r₁ ≡ s₁ (mod 2). r₁ = a·(c mod 2), s₁ = d·((1+b) mod 2) = d·(b mod 2 ... wait let me be careful. 1+b mod 2: if b is even, 1+b is odd, so s₁ = d. If b is odd, 1+b is even, so s₁ = 0.

So:
- If c even: r₁ = 0. If b even: s₁ = d. Need 0 ≡ d (mod 2), i.e., d even. If b odd: s₁ = 0. Always feasible.
- If c odd: r₁ = a. If b even: s₁ = d. Need a ≡ d (mod 2). If b odd: s₁ = 0. Need a ≡ 0 (mod 2), i.e., a even.

Minimum for sub-matrix 1: max(r₁, s₁) if feasible.

**Sub-matrix 2: (O_r, E_c)**, size b × c.
- Row parities: each of the b rows needs parity ≡ 1+d (mod 2). If d even, 1+d odd, so r₂ = b. If d odd, 1+d even, so r₂ = 0.
- Column parities: each of the c columns needs parity ≡ a (mod 2). If a even, s₂ = 0. If a odd, s₂ = c.
- Feasibility: r₂ ≡ s₂ (mod 2).

So:
- If d even: r₂ = b. If a even: s₂ = 0. Need b ≡ 0 (mod 2), i.e., b even. If a odd: s₂ = c. Need b ≡ c (mod 2).
- If d odd: r₂ = 0. If a even: s₂ = 0. Always feasible. If a odd: s₂ = c. Need 0 ≡ c (mod 2), i.e., c even.

Minimum for sub-matrix 2: max(r₂, s₂) if feasible.

Total checkers M = ac + bd + max(r₁, s₁) + max(r₂, s₂), where we choose a, c to minimize, subject to feasibility.

Let me denote a = number of even rows, c = number of even columns. b = n-a, d = n-c.

Let me compute this for n = 20 and n = 21.

This is getting complex. Let me think about which choices of (a, c) are feasible and compute M.

Let me organize by the parities of a, b, c, d. Since b = n-a and d = n-c, we have b ≡ n-a (mod 2) and d ≡ n-c (mod 2).

Let me consider n = 20 (even). Then b ≡ a (mod 2) and d ≡ c (mod 2) (since n is even, b = 20-a ≡ a mod 2, d = 20-c ≡ c mod 2).

For n = 21 (odd). b ≡ 1-a (mod 2) = 1+a (mod 2), d ≡ 1-c (mod 2) = 1+c (mod 2).

Let me handle n = 20 first.

**n = 20**: b ≡ a (mod 2), d ≡ c (mod 2).

Sub-matrix 1 (a × d):
- r₁ = a if c odd, 0 if c even.
- s₁ = d if b even (i.e., a even), 0 if b odd (i.e., a odd).
- Feasibility:
  - c even, a even: r₁=0, s₁=d. Need d even. d ≡ c ≡ 0 (mod 2). ✓ Always feasible.
  - c even, a odd: r₁=0, s₁=0. ✓ Always feasible.
  - c odd, a even: r₁=a, s₁=d. Need a ≡ d (mod 2). a even, d ≡ c ≡ 1 (mod 2), so d odd. a even, d odd: a ≢ d. **Infeasible**.
  - c odd, a odd: r₁=a, s₁=0. Need a ≡ 0 (mod 2). a odd. **Infeasible**.

So for n=20: sub-matrix 1 is feasible iff c is even (regardless of a). If c is odd, infeasible.

Wait, that means if c is odd, sub-matrix 1 is infeasible for n=20. So we must have c even.

Sub-matrix 2 (b × c), b ≡ a, d ≡ c:
- r₂ = b if d even (c even), 0 if d odd (c odd).
- s₂ = c if a odd, 0 if a even.
- Feasibility:
  - c even, a even: r₂=b, s₂=0. Need b ≡ 0 (mod 2). b ≡ a ≡ 0. ✓
  - c even, a odd: r₂=b, s₂=c. Need b ≡ c (mod 2). b ≡ a ≡ 1, c ≡ 0. 1 ≢ 0. **Infeasible**.
  - c odd, a even: r₂=0, s₂=0. ✓
  - c odd, a odd: r₂=0, s₂=c. Need 0 ≡ c (mod 2). c odd. **Infeasible**.

So for n=20: sub-matrix 2 is feasible iff (c even and a even) or (c odd and a even). I.e., a must be even.

Combined: both feasible iff c even and a even.

So for n = 20, we need a even and c even. Let a = 2p, c = 2q, where 0 ≤ p ≤ 10, 0 ≤ q ≤ 10.

b = 20 - 2p, d = 20 - 2q. All even.

Sub-matrix 1 (a × d = 2p × (20-2q)):
- c even → r₁ = 0.
- a even → b even → s₁ = d = 20-2q.
- Feasible (d even ✓).
- Min₁ = max(0, 20-2q) = 20-2q (if q < 10) or 0 (if q = 10).

Sub-matrix 2 (b × c = (20-2p) × 2q):
- c even → d even → r₂ = b = 20-2p.
- a even → s₂ = 0.
- Feasible (b even ✓).
- Min₂ = max(20-2p, 0) = 20-2p (if p < 10) or 0 (if p = 10).

Total M = ac + bd + Min₁ + Min₂
= (2p)(2q) + (20-2p)(20-2q) + (20-2q) + (20-2p)
= 4pq + (20-2p)(20-2q) + (20-2q) + (20-2p)
= 4pq + 400 - 40q - 40p + 4pq + 40 - 2q - 2p
= 8pq + 440 - 42p - 42q

Wait let me recompute. (20-2p)(20-2q) = 400 - 40q - 40p + 4pq.

M = 4pq + 400 - 40q - 40p + 4pq + 20 - 2q + 20 - 2p
= 8pq + 440 - 42p - 42q

Hmm wait, but this is only when p < 10 and q < 10. If p = 10, then b = 0, Min₂ = 0 (not 20-2p = 0, same thing). If q = 10, d = 0, Min₁ = 0. So the formula works for all p, q in range since 20-2p = 0 when p=10.

Let me verify: p=10, q=10: M = 8·100 + 440 - 420 - 420 = 800 + 440 - 840 = 400. That's a = 20, c = 20, all rows even, all columns even. All cells in (E_r, E_c) = all 400 cells occupied. That's the full board. Makes sense but not minimal.

M = 8pq - 42p - 42q + 440.

To minimize, take derivative: ∂M/∂p = 8q - 42, ∂M/∂q = 8p - 42. Setting to 0: q = 42/8 = 5.25, p = 5.25. So optimal around p = q = 5 or 6.

But p, q must be integers in [0, 10].

p=5, q=5: M = 8·25 - 42·5 - 42·5 + 440 = 200 - 210 - 210 + 440 = 220.
p=5, q=6: M = 8·30 - 42·5 - 42·6 + 440 = 240 - 210 - 252 + 440 = 218.
p=6, q=5: M = 8·30 - 42·6 - 42·5 + 440 = 240 - 252 - 210 + 440 = 218.
p=6, q=6: M = 8·36 - 42·6 - 42·6 + 440 = 288 - 252 - 252 + 440 = 224.
p=5, q=7: M = 8·35 - 42·5 - 42·7 + 440 = 280 - 210 - 294 + 440 = 216.
p=7, q=5: M = 216 (symmetric).
p=5, q=8: M = 8·40 - 42·5 - 42·8 + 440 = 320 - 210 - 336 + 440 = 214.
p=8, q=5: M = 214.
p=5, q=9: M = 8·45 - 42·5 - 42·9 + 440 = 360 - 210 - 378 + 440 = 212.
p=9, q=5: M = 212.
p=5, q=10: M = 8·50 - 42·5 - 42·10 + 440 = 400 - 210 - 420 + 440 = 210.
p=10, q=5: M = 210.
p=4, q=10: M = 8·40 - 42·4 - 42·10 + 440 = 320 - 168 - 420 + 440 = 172.
p=10, q=4: M = 172.
p=3, q=10: M = 8·30 - 42·3 - 42·10 + 440 = 240 - 126 - 420 + 440 = 134.
p=10, q=3: M = 134.
p=2, q=10: M = 8·20 - 42·2 - 42·10 + 440 = 160 - 84 - 420 + 440 = 96.
p=10, q=2: M = 96.
p=1, q=10: M = 8·10 - 42·1 - 42·10 + 440 = 80 - 42 - 420 + 440 = 58.
p=10, q=1: M = 58.
p=0, q=10: M = 0 - 0 - 420 + 440 = 20.
p=10, q=0: M = 0 - 420 - 0 + 440 = 20.

Interesting! p=0, q=10: a=0, c=20. All rows odd (b=20), all columns even (c=20, d=0).
M = ac + bd + Min₁ + Min₂ = 0 + 20·0 + 0 + 20 = 20.

Wait, let me check: a=0 (no even rows), c=20 (all even columns), b=20, d=0.
Mandatory: ac + bd = 0 + 20·0 = 0.
Sub-matrix 1: (E_r, O_c) = (0, 0) = empty. Min₁ = 0.
Sub-matrix 2: (O_r, E_c) = (20, 20). r₂ = b = 20 (d even), s₂ = 0 (a even). Min₂ = max(20, 0) = 20.
Total = 0 + 0 + 0 + 20 = 20. ✓

But wait, what does this configuration look like? All rows are odd, all columns are even. Mandatory cells: (E_r, E_c) = empty (no even rows), (O_r, O_c) = empty (no odd columns). So no mandatory cells. Optional: (O_r, E_c) = all 20×20 cells. We need to place 20 checkers such that each row has odd count and each column has even count. That's 20 ones in a 20×20 matrix with all rows odd and all columns even.

Sum of row counts = 20 (odd) × ... wait, 20 rows each odd. Sum = 20 odd numbers = even. Sum of column counts = 20 even numbers = even. Consistent. ✓

Min = 20 (place 1 in each row, all in column 1: column 1 has 20 (even ✓), each row has 1 (odd ✓), other columns 0 (even ✓)). Total = 20. ✓

But is this actually maximal? Let me verify. All rows have odd count, all columns have even count. For any empty cell (i,j): r_i is odd, c_j is even. r_i + c_j = odd + even = odd. ✓ So no more checkers can be placed. It's maximal. ✓

Can we do better than 20? Let me check p=0, q=10 gives M=20. Can we get lower?

p=0, q=9: M = 0 - 0 - 378 + 440 = 62. Worse.
p=1, q=10: M = 58. Worse.
p=0, q=10: M = 20. p=10, q=0: M = 20.

What about p=0, q=10 vs other extremes? Let me check p=0, q=10 more carefully. a=0, c=20.

Actually, let me also check: are there feasible configurations with a odd or c odd that I dismissed? I showed that for n=20, both sub-matrices are feasible only when a even and c even. So we're restricted to a, c both even. The minimum over all even a, c is 20 (at a=0, c=20 or a=20, c=0).

Wait, but a=0 means no even rows. Is that valid? a=0 means all rows are odd. That's fine. c=20 means all columns are even. That's fine.

Hmm, but actually I should double-check: can we get M < 20? Let me think about lower bounds.

Actually, let me reconsider. With a=0, c=20: all rows odd, all columns even. We need at least... each of the 20 rows must have an odd number of checkers, so at least 1 each, so at least 20. And we achieved 20. So M = 20 for this configuration.

Can we do better with a different approach? What if a=0, c=0? All rows odd, all columns odd. Then:
Mandatory: (E_r, E_c) = 0, (O_r, O_c) = 20×20 = 400. That's 400 mandatory. Way too much.

What about a=20, c=0? All rows even, all columns odd.
Mandatory: (E_r, E_c) = 0, (O_r, O_c) = 0. 
Sub-matrix 1: (E_r, O_c) = (20, 20). c=0 even → r₁=0. a=20 even → b=0 even → s₁=d=20. Min₁ = 20.
Sub-matrix 2: (O_r, E_c) = (0, 0). Min₂ = 0.
Total = 0 + 0 + 20 + 0 = 20. Same.

So for n=20, f(20) = 20? Let me think about whether we can do better...

Actually, wait. I need to reconsider. The minimum of 20 checkers for a 20×20 board. Each row must have at least 1 checker (if all rows are odd, each needs ≥1). But what if some rows have 0 checkers (even)? Then we'd have a mix.

With a=0, c=20 (all odd rows, all even columns): each row needs ≥1, so M ≥ 20. Achieved.

With a=2, c=20: 2 even rows, 18 odd rows, all even columns.
Mandatory: ac + bd = 2·20 + 18·0 = 40.
Sub-matrix 1: (2, 0) = empty. Min₁ = 0.
Sub-matrix 2: (18, 20). r₂ = 18, s₂ = 0. Min₂ = 18.
Total = 40 + 0 + 18 = 58. Worse.

So indeed a=0, c=20 (or a=20, c=0) gives the minimum of 20 for n=20.

But wait, I should also check: is 20 really the minimum, or can we be cleverer? Let me think about a lower bound.

In a maximal configuration, every empty cell (i,j) has r_i + c_j odd. Consider the sum S = Σ_i r_i + Σ_j c_j = 2M (each checker counted once in its row and once in its column). 

Hmm, let me think about it differently. If the configuration is maximal, for every empty cell, r_i and c_j have different parities. 

Consider the bipartite graph where rows and columns are vertices, and occupied cells are edges. The degree of row i is r_i, degree of column j is c_j.

For every non-edge (i,j), deg(i) and deg(j) have different parities.

This means: in the bipartite complement graph (non-edges), every edge connects vertices of different parity. So the complement graph is bipartite with respect to the parity partition. I.e., non-edges only go between even-odd pairs.

Equivalently, all same-parity pairs (even row, even column) and (odd row, odd column) must be edges (occupied).

This is exactly what I had before. So the analysis is correct.

Now, for the minimum: we need all (even row, even col) and (odd row, odd col) cells occupied, plus some optional cells to satisfy parity. The minimum over all parity assignments.

For n=20, I found f(20) = 20. Let me now do n=21.

**n = 21**: b = 21-a, d = 21-c. b ≡ 1+a (mod 2) [since 21 is odd], d ≡ 1+c (mod 2).

So: a even → b odd; a odd → b even. c even → d odd; c odd → d even.

Sub-matrix 1 (a × d):
- r₁ = a if c odd, 0 if c even.
- s₁ = d if b even (a odd), 0 if b odd (a even).
- Feasibility:
  - c even, a even: r₁=0, s₁=0 (b odd). ✓
  - c even, a odd: r₁=0, s₁=d (b even). Need 0 ≡ d (mod 2). d ≡ 1+c ≡ 1 (mod 2), d odd. 0 ≢ 1. **Infeasible**.
  - c odd, a even: r₁=a, s₁=0 (b odd). Need a ≡ 0 (mod 2). a even. ✓
  - c odd, a odd: r₁=a, s₁=d (b even). Need a ≡ d (mod 2). a odd, d ≡ 1+c ≡ 0 (mod 2), d even. odd ≢ even. **Infeasible**.

So sub-matrix 1 feasible iff a even (regardless of c).

Sub-matrix 2 (b × c):
- r₂ = b if d even (c odd), 0 if d odd (c even).
- s₂ = c if a odd, 0 if a even.
- Feasibility:
  - c even, a even: r₂=0, s₂=0. ✓
  - c even, a odd: r₂=0, s₂=c. Need 0 ≡ c (mod 2). c even. ✓
  - c odd, a even: r₂=b, s₂=0. Need b ≡ 0 (mod 2). b ≡ 1+a ≡ 1 (mod 2), b odd. odd ≢ 0. **Infeasible**.
  - c odd, a odd: r₂=b, s₂=c. Need b ≡ c (mod 2). b ≡ 1+a ≡ 0 (mod 2), b even. c odd. even ≢ odd. **Infeasible**.

So sub-matrix 2 feasible iff c even (regardless of a).

Combined: both feasible iff a even AND c even.

For n=21, a even, c even. Let a = 2p, c = 2q, 0 ≤ p ≤ 10, 0 ≤ q ≤ 10 (since a ≤ 21, c ≤ 21, and even, so max is 20).

b = 21 - 2p, d = 21 - 2q. Both odd.

Sub-matrix 1 (a × d = 2p × (21-2q)):
- c even → r₁ = 0.
- a even → b odd → s₁ = 0.
- Min₁ = 0.

Sub-matrix 2 (b × c = (21-2p) × 2q):
- c even → d odd → r₂ = 0.
- a even → s₂ = 0.
- Min₂ = 0.

Total M = ac + bd + 0 + 0 = (2p)(2q) + (21-2p)(21-2q) = 4pq + 441 - 42q - 42p + 4pq = 8pq - 42p - 42q + 441.

Minimize: ∂M/∂p = 8q - 42 = 0 → q = 5.25, ∂M/∂q = 8p - 42 = 0 → p = 5.25.

Check boundary: p=0, q=0: M = 441 (all rows odd, all columns odd, all cells mandatory). 
p=0, q=10: M = 0 - 0 - 420 + 441 = 21.
p=10, q=0: M = 0 - 420 - 0 + 441 = 21.
p=10, q=10: M = 800 - 420 - 420 + 441 = 401.
p=5, q=5: M = 200 - 210 - 210 + 441 = 221.
p=0, q=10: M = 21.

Let me check p=0, q=10: a=0, c=20, b=21, d=1.
Mandatory: ac + bd = 0 + 21·1 = 21.
Sub-matrix 1: (0, 1) = empty. Min₁ = 0.
Sub-matrix 2: (21, 20). r₂=0, s₂=0. Min₂=0.
Total = 21. ✓

What's the configuration? a=0 (all rows odd), c=20 (20 even columns), d=1 (1 odd column). Mandatory: (O_r, O_c) = 21×1 = 21 cells (all cells in the single odd column). (E_r, E_c) = 0. No optional cells needed.

So all 21 cells in one column are occupied. Each row has 1 checker (odd ✓). The odd column has 21 checkers (odd ✓). Each even column has 0 (even ✓). For any empty cell (i,j) where j is an even column: r_i = 1 (odd), c_j = 0 (even). 1+0 = 1 (odd ✓). Maximal. ✓

Can we do better? p=0, q=10 gives 21. Let me check other values.

p=1, q=10: M = 8·10 - 42 - 420 + 441 = 80 - 42 - 420 + 441 = 59. Worse.
p=0, q=9: M = 0 - 0 - 378 + 441 = 63. Worse.

So the minimum for n=21 is 21, achieved at (p=0, q=10) or (p=10, q=0).

Wait, but I should check: is there a configuration with a or c odd that could give a lower M? I showed that for n=21, both sub-matrices are feasible only when a even and c even. If a or c is odd, one sub-matrix is infeasible, meaning we can't satisfy the parity constraints. So those configurations are impossible.

Hmm, but wait — I need to reconsider. When a sub-matrix is "infeasible," it means we can't satisfy the parity constraints for that sub-matrix. But the parity constraints come from the requirement that rows have even/odd counts. If we can't satisfy them, that partition (a,c) doesn't work. So indeed we're restricted to a even, c even for n=21.

So f(21) = 21.

And f(20) = 20.

f(20) + f(21) = 20 + 21 = 41.

Wait, but let me double-check f(20) = 20 more carefully. I want to make sure there isn't a configuration outside my framework that does better.

Actually, my framework is complete: any maximal configuration must have the property that all same-parity (row, col) pairs are occupied. The partition into even/odd rows and columns is determined by the configuration. So the framework covers all maximal configurations. The minimum over all valid (a,c) partitions is f(n).

For n=20, the minimum is 20 (at a=0,c=20 or a=20,c=0).
For n=21, the minimum is 21 (at a=0,c=20 or a=10,c=0... wait, a=0,c=20: b=21,d=1, M=21).

Hmm wait, for n=21, let me also check a=20, c=0: p=10, q=0. M = 0 - 420 - 0 + 441 = 21. a=20 (even rows), c=0 (no even columns), b=1, d=21. Mandatory: ac + bd = 0 + 1·21 = 21. Same.

And a=0, c=0: p=0, q=0. M = 441. All rows odd, all columns odd, all 21² = 441 cells mandatory. Bad.

So f(20) + f(21) = 20 + 21 = 41.

But wait, I want to be more careful. Let me re-examine the n=20 case. I claimed the minimum is 20, achieved at a=0, c=20. Let me verify this is truly minimal by checking if there's any way to get fewer than 20.

With a=0, c=20: all 20 rows are odd (each has ≥1 checker), all 20 columns are even. M = 20. Since each row needs at least 1 checker (being odd), M ≥ 20. So 20 is optimal for this partition.

For any other feasible partition (a even, c even, a > 0): we showed M ≥ 58 (at a=2, c=20). So 20 is the overall minimum.

Actually, let me also think about whether there's a smarter lower bound. In any maximal configuration on an n×n board, consider the rows. Each row has some number of checkers. If a row has 0 checkers (even), then for every column j, c_j must be odd (since r_i = 0 is even, we need r_i + c_j odd, so c_j odd). If all columns are odd, then every cell in an even row must be occupied (same parity: even row, odd column... wait, even row and odd column are different parities, so those cells can be empty).

Hmm, let me reconsider. If a row has 0 checkers (even), then for every empty cell in that row, c_j must be odd. But cells in that row that are occupied... there are none (0 checkers). So all cells in that row are empty, and for all of them, c_j must be odd. So all columns must be odd.

If all columns are odd, then each column has ≥1 checker, so M ≥ n. And for n=20, M ≥ 20. For n=21, M ≥ 21.

But can we always achieve M = n? For n=20, we showed yes (a=0, c=20 gives M=20, where all rows are odd and all columns are even — wait, that's different from "all columns odd").

Let me reconsider. With a=0, c=20 for n=20: all rows odd, all columns even. Each row has ≥1, so M ≥ 20. Achieved. ✓

Alternatively, all rows even, all columns odd: a=20, c=0. Each column has ≥1, M ≥ 20. Achieved. ✓

For n=21: a=0, c=20. All rows odd, 20 even columns, 1 odd column. The 1 odd column has all 21 cells occupied (mandatory). M = 21. Each row has exactly 1 checker. ✓

Alternatively, all rows even, all columns odd: a=20, c=0. b=1, d=21. Mandatory: (O_r, O_c) = 1×21 = 21. M = 21. The 1 odd row has all 21 cells occupied. ✓

But could we do better for n=21? What if we have all rows even (a=21)? But a must be even for n=21, and 21 is odd. So a=21 is not even. We can't have all rows even for n=21.

What about all rows odd (a=0) and all columns odd (c=0)? Then all cells are mandatory: 21² = 441. Bad.

What about a=0, c=20 (M=21)? Can we do a=0, c=22? No, c ≤ 21. c=20 is the max even value ≤ 21.

What about a=0, c=18? d=3. Mandatory: bd = 21·3 = 63. Worse.

So for n=21, the minimum is indeed 21.

Hmm, but wait. I should think about whether there's a fundamentally different kind of configuration I'm missing. My analysis assumes that the parities of rows and columns partition the board into four regions, with same-parity regions fully occupied. This is correct because:

In a maximal configuration, for every empty cell (i,j), r_i + c_j is odd, meaning r_i and c_j have different parities. Contrapositive: if r_i and c_j have the same parity, then (i,j) is not empty, i.e., it's occupied.

So yes, all same-parity cells are occupied. The analysis is complete.

Let me also verify with a small case. n=1: 1×1 board. We can place a checker at (1,1) if the remaining 2·1-2 = 0 cells have an even number (0 is even). So we place 1 checker. After that, no more can be placed (board full). f(1) = 1.

Using my formula: n=1 (odd). a even, c even. a ∈ {0}, c ∈ {0}. a=0, c=0: M = 0·0 + 1·1 = 1. ✓

n=2: a even, c even. a ∈ {0,2}, c ∈ {0,2}.
a=0, c=2: M = 0 + 2·0 + 0 + 2 = 2. (All rows odd, all columns even. 2 checkers.)
a=2, c=0: M = 0 + 0 + 2 + 0 = 2.
a=0, c=0: M = 0 + 2·2 = 4.
a=2, c=2: M = 4 + 0 + 0 + 0 = 4.
f(2) = 2. Let me verify: 2×2 board, place checkers at (1,1) and (2,1). Row 1: 1 (odd), Row 2: 1 (odd). Col 1: 2 (even), Col 2: 0 (even). Empty cells: (1,2): r+c = 1+0 = 1 (odd ✓). (2,2): 1+0 = 1 (odd ✓). Maximal with 2 checkers. ✓

n=3: a even, c even. a ∈ {0,2}, c ∈ {0,2}.
a=0, c=2: b=3, d=1. M = 0 + 3·1 + 0 + 0 = 3.
a=2, c=0: b=1, d=3. M = 0 + 1·3 + 0 + 0 = 3.
a=0, c=0: M = 0 + 3·3 = 9.
a=2, c=2: b=1, d=1. M = 4 + 1 + 0 + 0 = 5.
f(3) = 3. Verify: 3×3, all rows odd, 2 even columns, 1 odd column. Odd column has all 3 cells occupied. M=3. Each row has 1 checker (odd ✓). Even columns have 0 (even ✓). Odd column has 3 (odd ✓). Empty cells: (i, even col): r_i + c_j = 1 + 0 = 1 (odd ✓). Maximal. ✓

So the pattern is f(n) = n for all n? Let me check n=4.

n=4: a even, c even. a ∈ {0,2,4}, c ∈ {0,2,4}.
a=0, c=4: M = 0 + 0 + 0 + 4 = 4.
a=0, c=2: b=4, d=2. M = 0 + 8 + 2 + 4 = 14. Wait, let me use the formula: M = 8pq - 42p - 42q + 440? No, that's for n=20. Let me recompute for n=4.

For n=4: M = ac + bd + Min₁ + Min₂.
a=0, c=4: b=4, d=0. M = 0 + 0 + 0 + 4 = 4. (Min₁ = max(0, d) = 0, Min₂ = max(b, 0) = 4.)
a=0, c=2: b=4, d=2. M = 0 + 8 + 2 + 4 = 14.
a=0, c=0: M = 0 + 16 + 4 + 0 = 20. Hmm, Min₁ = max(0, d) = max(0,4) = 4, Min₂ = max(b, 0) = max(4,0) = 4. M = 0 + 16 + 4 + 4 = 24. Wait, let me recompute.

Actually, for n=4, a=0, c=0: all rows odd, all columns odd. Mandatory: (O_r, O_c) = 4×4 = 16. Sub-matrix 1: (E_r, O_c) = (0, 4), empty. Sub-matrix 2: (O_r, E_c) = (4, 0), empty. M = 16. 

Hmm, I think I made an error. Let me recompute using the general formula.

For general n (even), with a=2p, c=2q:
M = 4pq + (n-2p)(n-2q) + (n-2q) + (n-2p) [when p < n/2 and q < n/2]

Wait, I had: M = ac + bd + Min₁ + Min₂ where Min₁ = max(r₁, s₁) and Min₂ = max(r₂, s₂).

For n even, a even, c even:
- r₁ = 0 (c even), s₁ = d (a even → b even → s₁ = d). Min₁ = d = n-c (if d > 0, else 0).
- r₂ = b (c even → d even → r₂ = b), s₂ = 0 (a even). Min₂ = b = n-a (if b > 0, else 0).

M = ac + bd + d + b = ac + (n-a)(n-c) + (n-c) + (n-a)
= ac + n² - n(a+c) + ac + n - c + n - a
= 2ac + n² - n(a+c) + 2n - a - c
= 2ac + n² + 2n - (n+1)(a+c)

For n=4: M = 2ac + 16 + 8 - 5(a+c) = 2ac + 24 - 5(a+c).
a=0, c=4: M = 0 + 24 - 20 = 4. ✓
a=0, c=0: M = 0 + 24 - 0 = 24. But I computed 16 above. Discrepancy!

Let me recheck a=0, c=0 for n=4. a=0, c=0, b=4, d=4.
Mandatory: ac + bd = 0 + 4·4 = 16.
Sub-matrix 1: (E_r, O_c) = (0, 4). Empty (0 rows). Min₁ = 0.
Sub-matrix 2: (O_r, E_c) = (4, 0). Empty (0 columns). Min₂ = 0.
M = 16 + 0 + 0 = 16.

But my formula gives: Min₁ = d = 4, Min₂ = b = 4. That's wrong! When a=0, the sub-matrix (E_r, O_c) has 0 rows, so it's empty and Min₁ = 0, not d.

The issue is that max(r₁, s₁) = max(0, d) = d only works if the sub-matrix is non-empty. If a=0, the sub-matrix has 0 rows, so we can't place any checkers, and the constraint is that all column parities must be 0. But s₁ = d means we need d odd columns, which requires d = 0 (since we can't place any checkers). 

So when a=0, we need s₁ = 0, i.e., d = 0 (for n even, d = n-c, so c = n). OR we need the sub-matrix to not require any checkers, which happens when s₁ = 0.

Wait, I think the issue is more subtle. When a=0 (no even rows), the sub-matrix (E_r, O_c) is empty (0 rows). The column parity constraints for odd columns say: each odd column needs parity ≡ 1+b (mod 2). But if there are no even rows, the optional cells in odd columns (from even rows) don't exist. The column parity is determined entirely by the mandatory cells.

Let me re-examine. For an odd column j (in O_c), the total checkers = b (mandatory in O_r) + (optional in E_r). If a=0, there are no even rows, so optional = 0. Total = b. We need this to be odd. So b must be odd.

For n=4, a=0: b=4 (even). So odd columns would have 4 checkers (even), but we need odd. Contradiction! So a=0, c=0 is actually infeasible for n=4.

Wait, but I said for n even, a even and c even is always feasible. Let me recheck.

For n=4, a=0, c=0: b=4, d=4. 
Sub-matrix 1: (E_r, O_c) = (0, 4). r₁ = 0 (c even), s₁ = d = 4 (a even → b even). Feasibility: 0 ≡ 4 (mod 2)? 0 ≡ 0 ✓. But the sub-matrix has 0 rows! We need s₁ = 4 odd columns, but with 0 rows, we can't place any checkers. So we need s₁ = 0.

Ah, I see the issue. The feasibility condition r₁ ≡ s₁ (mod 2) is necessary but not sufficient when the sub-matrix is degenerate. If the sub-matrix has 0 rows (a=0), then all column sums are 0, so we need all column parities to be 0, i.e., s₁ = 0. Similarly, if 0 columns (d=0), all row sums are 0, need r₁ = 0.

So the actual feasibility conditions are:
- If a = 0: need s₁ = 0 (all column parities in sub-matrix 1 are 0).
- If d = 0: need r₁ = 0.
- If a > 0 and d > 0: need r₁ ≡ s₁ (mod 2) and r₁ ≤ a, s₁ ≤ d (which is automatic since r₁ ∈ {0, a} and s₁ ∈ {0, d}).

Similarly for sub-matrix 2.

Let me redo the analysis more carefully.

For n=4, a=0, c=0: 
Sub-matrix 1: a=0, so need s₁=0. s₁ = d if b even, 0 if b odd. b=4 even, so s₁ = d = 4 ≠ 0. **Infeasible**.

So a=0, c=0 is infeasible for n=4. My earlier analysis was wrong because I didn't account for degenerate sub-matrices.

Let me redo the n=20 and n=21 analyses with this correction.

For n=20 (even), a=2p, c=2q:

Sub-matrix 1 (a × d, d = 20-2q):
- r₁ = 0 (c even), s₁ = d if a even (b even), 0 if a odd. Since a is even, s₁ = d = 20-2q.
- If a = 0 (p=0): need s₁ = 0, i.e., d = 0, i.e., q = 10.
- If a > 0 (p > 0): need r₁ ≡ s₁ (mod 2), i.e., 0 ≡ d (mod 2). d = 20-2q is always even. ✓
- If d = 0 (q=10): need r₁ = 0. r₁ = 0. ✓

Sub-matrix 2 (b × c, b = 20-2p):
- r₂ = b (d even, since c even → d even), s₂ = 0 (a even).
- If b = 0 (p=10): need s₂ = 0. s₂ = 0. ✓ (Also need r₂ = 0, r₂ = b = 0. ✓)
- If c = 0 (q=0): need r₂ = 0. r₂ = b = 20-2p. Need p = 10.
- If b > 0 and c > 0: need r₂ ≡ s₂ (mod 2), i.e., b ≡ 0 (mod 2). b = 20-2p is always even. ✓

So the feasibility conditions for n=20:
- If p = 0: need q = 10 (from sub-matrix 1).
- If q = 0: need p = 10 (from sub-matrix 2).
- If p > 0 and q > 0: always feasible (with p ≤ 10, q ≤ 10).
- If p = 10: sub-matrix 2 is degenerate (b=0), always OK.
- If q = 10: sub-matrix 1 is degenerate (d=0), always OK.

So the feasible (p,q) are:
- p=0, q=10
- p=10, q=0
- p > 0, q > 0 (any p from 1 to 10, q from 1 to 10)
- Also p=10, q=10 (both degenerate, OK)
- p=10, q > 0: b=0, sub-matrix 2 degenerate (OK), sub-matrix 1 non-degenerate if d > 0 (q < 10) → need 0 ≡ d (mod 2), d even ✓. So p=10, q ∈ {1,...,10} feasible.
- p > 0, q=10: d=0, sub-matrix 1 degenerate (OK), sub-matrix 2 non-degenerate if b > 0 (p < 10) → need b ≡ 0 (mod 2), b even ✓. So p ∈ {1,...,10}, q=10 feasible.

So the only infeasible cases are p=0 with q < 10, and q=0 with p < 10.

Now let me compute M for the feasible cases:

M = ac + bd + Min₁ + Min₂.

For p > 0, q > 0 (and p ≤ 10, q ≤ 10), with the degenerate cases handled:

If p > 0 and q < 10 (d > 0): Min₁ = max(0, d) = d = 20-2q.
If q = 10 (d = 0): Min₁ = 0.
If p < 10 and q > 0 (b > 0, c > 0): Min₂ = max(b, 0) = b = 20-2p.
If p = 10 (b = 0): Min₂ = 0.
If q = 0: only feasible if p = 10, then b = 0, Min₂ = 0, and d = 20, Min₁ = max(0, 20) = 20. M = 10·0 + 0·20 + 20 + 0 = 20.

Wait, q=0, p=10: a=20, c=0, b=0, d=20. Mandatory: ac + bd = 0 + 0 = 0. Sub-matrix 1: (20, 20), r₁=0, s₁=20. Min₁ = 20. Sub-matrix 2: (0, 0). Min₂ = 0. M = 0 + 0 + 20 + 0 = 20. ✓

p=0, q=10: a=0, c=20, b=20, d=0. Mandatory: 0 + 0 = 0. Sub-matrix 1: (0, 0). Min₁ = 0. Sub-matrix 2: (20, 20), r₂=20, s₂=0. Min₂ = 20. M = 0 + 0 + 0 + 20 = 20. ✓

So for n=20, the minimum is still 20. Let me check if any other feasible point gives less than 20.

For p > 0, q > 0 (general case):
M = 4pq + (20-2p)(20-2q) + (20-2q) + (20-2p) [when p < 10, q < 10]
= 4pq + 400 - 40p - 40q + 4pq + 40 - 2p - 2q
= 8pq + 440 - 42p - 42q

We need to minimize this over p ∈ {1,...,10}, q ∈ {1,...,10} (and also handle boundary cases p=10 or q=10).

At p=1, q=10: M = 8·10 + 440 - 42 - 420 = 80 + 440 - 462 = 58.
At p=10, q=1: M = 58.
At p=1, q=1: M = 8 + 440 - 42 - 42 = 364.

The function 8pq - 42p - 42q + 440 is minimized at the boundary. Since the coefficient of pq is positive, the minimum is at small p, q. But we also need p ≥ 1, q ≥ 1 (for this formula). The minimum in the interior is at p=q=5.25, which gives a local minimum, not global. The global min on the boundary.

Let me check p=1, q=10: M = 58. p=10, q=1: M = 58. p=1, q=9: M = 72 - 42 - 378 + 440 = 92. 

Hmm, all values with p ≥ 1, q ≥ 1 give M ≥ 58. The minimum of 20 is achieved only at (p=0, q=10) and (p=10, q=0).

So f(20) = 20. ✓

Now for n=21 (odd), a=2p, c=2q, p ∈ {0,...,10}, q ∈ {0,...,10}:

Sub-matrix 1 (a × d, d = 21-2q, d is odd):
- r₁ = 0 (c even), s₁ = 0 (a even → b odd → s₁ = 0).
- If a = 0: need s₁ = 0. s₁ = 0. ✓
- If d = 0: impossible since d = 21-2q is always odd, never 0. Actually d = 21-2q, for q=10, d=1; for q=0, d=21. d is always ≥ 1 and odd.
- Feasibility: r₁ = 0, s₁ = 0. Always feasible. Min₁ = 0.

Sub-matrix 2 (b × c, b = 21-2p, b is odd):
- r₂ = 0 (d odd → r₂ = 0), s₂ = 0 (a even).
- If b = 0: impossible since b = 21-2p is always odd, never 0.
- If c = 0 (q=0): need r₂ = 0. r₂ = 0. ✓
- Feasibility: r₂ = 0, s₂ = 0. Always feasible. Min₂ = 0.

So for n=21, all (p, q) with p ∈ {0,...,10}, q ∈ {0,...,10} are feasible!

M = ac + bd + 0 + 0 = 4pq + (21-2p)(21-2q) = 4pq + 441 - 42p - 42q + 4pq = 8pq - 42p - 42q + 441.

Minimize over p ∈ {0,...,10}, q ∈ {0,...,10}.

∂M/∂p = 8q - 42 = 0 → q = 5.25. ∂M/∂q = 8p - 42 = 0 → p = 5.25.

Since the Hessian is [[0, 8], [8, 0]] with eigenvalues ±8, this is a saddle point, not a minimum. So the minimum is on the boundary.

Boundary values:
- p=0: M = 441 - 42q. Minimized at q=10: M = 441 - 420 = 21.
- q=0: M = 441 - 42p. Minimized at p=10: M = 441 - 420 = 21.
- p=10: M = 80q - 420 - 42q + 441 = 38q + 21. Minimized at q=0: M = 21.
- q=10: M = 80p - 42p - 420 + 441 = 38p + 21. Minimized at p=0: M = 21.

So the minimum is 21, achieved at (p=0, q=10), (p=10, q=0), and along the boundaries.

f(21) = 21. ✓

So f(20) + f(21) = 20 + 21 = 41.

Wait, I should double-check this more carefully. Let me verify the n=21, p=0, q=10 case.

a=0, c=20, b=21, d=1. All rows odd, 20 even columns, 1 odd column.
Mandatory: (E_r, E_c) = 0 (no even rows), (O_r, O_c) = 21 × 1 = 21.
Optional: (E_r, O_c) = 0 × 1 = 0, (O_r, E_c) = 21 × 20 = 420.
Min₁ = 0, Min₂ = 0.
M = 0 + 21 + 0 + 0 = 21.

The configuration: all 21 cells in the single odd column are occupied. Each row has 1 checker (odd ✓). The odd column has 21 checkers (odd ✓). Each even column has 0 (even ✓). 

For any empty cell (i, j) where j is an even column: r_i = 1 (odd), c_j = 0 (even). r_i + c_j = 1 (odd ✓). Can't place. ✓

Maximal with 21 checkers. And 21 is the minimum since each row has at least 1 checker (all rows are odd), so M ≥ 21.

Actually, I realize I should also check: is there a non-even a or c configuration that could work for n=21? I showed earlier that for n=21, both sub-matrices are feasible only when a even and c even. Let me re-examine with the degenerate case correction.

For n=21, a odd, c even:
Sub-matrix 1: r₁ = 0 (c even), s₁ = d (a odd → b even → s₁ = d). 
- If a > 0: need 0 ≡ d (mod 2). d = 21-c, c even, so d is odd. 0 ≢ 1. **Infeasible**.
- If a = 0: but a is odd, so a ≥ 1. Infeasible.

For n=21, a even, c odd:
Sub-matrix 2: r₂ = b (c odd → d even → r₂ = b), s₂ = c (a even → s₂ = 0). Wait, s₂ = c if a odd, 0 if a even. a is even, so s₂ = 0.
- r₂ = b, s₂ = 0. Need b ≡ 0 (mod 2). b = 21-a, a even, so b is odd. odd ≢ 0. **Infeasible** (if b > 0).
- If b = 0: a = 21, but a must be even. 21 is odd. Impossible.

For n=21, a odd, c odd:
Sub-matrix 1: r₁ = a (c odd), s₁ = d (a odd → b even → s₁ = d). Need a ≡ d (mod 2). a odd, d = 21-c, c odd, d even. odd ≢ even. **Infeasible**.

So indeed, for n=21, only a even and c even works. f(21) = 21.

And for n=20, only a even and c even works (I verified this earlier, and the degenerate corrections don't change the feasible set for non-degenerate cases, and the minimum is still 20).

Let me also verify the n=20 case once more with the degenerate correction. For n=20, a odd, c even:
Sub-matrix 1: r₁ = 0 (c even), s₁ = d (a odd → b odd → s₁ = 0). Wait, b = 20-a, a odd → b odd. s₁ = 0 if b odd. So s₁ = 0.
- r₁ = 0, s₁ = 0. Feasible! Min₁ = 0.

Sub-matrix 2: r₂ = b (c even → d even → r₂ = b), s₂ = c (a odd → s₂ = c). Need b ≡ c (mod 2). b = 20-a, a odd, b odd. c even. odd ≢ even. **Infeasible** (if b > 0 and c > 0).
- If b = 0: a = 20, but a is odd. Impossible.
- If c = 0: s₂ = 0, r₂ = b. Need b ≡ 0 (mod 2). b odd. Infeasible.

So a odd, c even is infeasible for n=20 (due to sub-matrix 2). ✓

For n=20, a even, c odd:
Sub-matrix 1: r₁ = a (c odd), s₁ = 0 (a even → b even → b odd? No, b = 20-a, a even → b even. s₁ = d if b even, 0 if b odd. b even → s₁ = d). 
Wait, I need to be more careful. s₁ = d if b even, 0 if b odd. b = 20-a, a even → b even → s₁ = d.
r₁ = a (c odd), s₁ = d. Need a ≡ d (mod 2). a even, d = 20-c, c odd → d odd. even ≢ odd. **Infeasible** (if a > 0 and d > 0).
- If a = 0: r₁ = 0, need s₁ = 0, i.e., d = 0, i.e., c = 20. But c is odd, 20 is even. Impossible.
- If d = 0: c = 20, but c is odd. Impossible.

So a even, c odd is infeasible for n=20. ✓

For n=20, a odd, c odd:
Sub-matrix 1: r₁ = a (c odd), s₁ = 0 (a odd → b odd → s₁ = 0). Need a ≡ 0 (mod 2). a odd. **Infeasible** (if a > 0).
Sub-matrix 2: r₂ = 0 (c odd → d odd → r₂ = 0), s₂ = c (a odd → s₂ = c). Need 0 ≡ c (mod 2). c odd. **Infeasible** (if c > 0).

So a odd, c odd is infeasible. ✓

Great, so for n=20, only a even, c even is feasible, and f(20) = 20.
For n=21, only a even, c even is feasible, and f(21) = 21.

f(20) + f(21) = 41.

Hmm wait, but I want to make sure I haven't made an error. Let me think about this more carefully with a different approach.

Alternative approach: Think about what a maximal configuration looks like.

A configuration is maximal iff for every empty cell (i,j), r_i + c_j is odd.

This means: if r_i is even, then for every empty cell in row i, c_j is odd. If r_i is odd, then for every empty cell in row i, c_j is even.

Consider the rows with r_i = 0 (completely empty rows). For such a row, every cell is empty, so every column must have odd count. If there are k such rows, and all columns are odd, then each column has at least 1 checker, so M ≥ n. But also, the checkers in each column are in the non-empty rows.

Hmm, this is getting complicated. Let me just verify the answer with a slightly larger case.

n=5: a even, c even. a ∈ {0,2,4}, c ∈ {0,2,4}.
M = 4pq + (5-2p)(5-2q) + 0 + 0 = 4pq + 25 - 10p - 10q + 4pq = 8pq - 10p - 10q + 25.

Wait, for n=5 (odd), Min₁ = 0 and Min₂ = 0 always (as I showed for n=21). So M = ac + bd = 4pq + (5-2p)(5-2q).

p=0, q=2: M = 0 + 5·1 = 5. (a=0, c=4, b=5, d=1.)
p=2, q=0: M = 0 + 1·5 = 5. (a=4, c=0, b=1, d=5.)
p=0, q=0: M = 0 + 25 = 25.
p=2, q=2: M = 16 + 1 = 17.

f(5) = 5. Makes sense: place checkers in one column (all 5 cells), each row has 1 (odd), that column has 5 (odd), other columns have 0 (even). Maximal. ✓

n=6: a even, c even. a ∈ {0,2,4,6}, c ∈ {0,2,4,6}.
For non-degenerate cases (p > 0, q > 0, p < 3, q < 3):
M = 4pq + (6-2p)(6-2q) + (6-2q) + (6-2p) = 8pq + 36 + 12 - 6(a+c)/... let me use the formula.

Actually, M = ac + bd + d + b = 2ac + n² + 2n - (n+1)(a+c) for n even.
For n=6: M = 2ac + 36 + 12 - 7(a+c) = 2ac + 48 - 7(a+c).

a=0, c=6: M = 0 + 48 - 42 = 6. (Feasible: p=0, q=3. d=0, sub-matrix 1 degenerate. b=6, sub-matrix 2: r₂=6, s₂=0, Min₂=6. M = 0 + 0 + 0 + 6 = 6. ✓)
a=6, c=0: M = 0 + 48 - 42 = 6.
a=2, c=6: M = 24 + 48 - 56 = 16. (Using general formula: 4·3 + 0 + 0 + 4 = 16. Wait, a=2, c=6, b=4, d=0. Mandatory: 12 + 0 = 12. Sub-matrix 1: (2, 0), degenerate, Min₁=0. Sub-matrix 2: (4, 6), r₂=4, s₂=0, Min₂=4. M = 12 + 0 + 0 + 4 = 16. ✓)

f(6) = 6. ✓

So the pattern f(n) = n holds for all n. This makes intuitive sense: place n checkers in a single column (or row). Each row has 1 checker (odd), that column has n checkers (parity = n mod 2), other columns have 0 (even).

For this to be maximal: for empty cell (i, j) where j ≠ the occupied column: r_i = 1 (odd), c_j = 0 (even). r_i + c_j = 1 (odd). ✓ Can't place.

For the occupied column: all cells are occupied, so no empty cells there.

But wait, we need the occupied column to have the right parity. If n is even, the column has n checkers (even). All rows have 1 (odd). All other columns have 0 (even). For empty cell (i,j), j ≠ occupied column: r_i + c_j = 1 + 0 = 1 (odd ✓). ✓

If n is odd, the column has n checkers (odd). All rows have 1 (odd). All other columns have 0 (even). For empty cell (i,j), j ≠ occupied column: r_i + c_j = 1 + 0 = 1 (odd ✓). ✓

So in both cases, placing n checkers in a single column gives a maximal configuration with M = n. And we showed M ≥ n (since each row has at least 1 checker when all rows are odd, or each column has at least 1 when all columns are odd). 

But wait, is M ≥ n always true? What if some rows have 0 checkers?

If some row has 0 checkers (even), then all columns must be odd (as I argued earlier). If all columns are odd, each has ≥ 1 checker, so M ≥ n. If all rows are odd, each has ≥ 1, so M ≥ n. If some rows are even (but not 0) and some are odd... 

Actually, let me think about this more carefully. In a maximal configuration, can we have M < n?

Suppose M < n. Then the average number of checkers per row is < 1, so some row has 0 checkers. Say row i has r_i = 0. Then for every column j, since cell (i,j) is empty (r_i = 0), we need r_i + c_j odd, so c_j is odd. All columns are odd, so each has ≥ 1 checker, M ≥ n. Contradiction.

So M ≥ n for any maximal configuration. And we showed M = n is achievable. Therefore f(n) = n for all n.

Wait, that's a much simpler argument! Let me make sure it's correct.

Claim: In any maximal configuration, M ≥ n.

Proof: Suppose M < n. Then some row has 0 checkers (by pigeonhole, since M < n checkers in n rows). Say row i is empty. Then every cell (i,j) is empty, and for each such cell, r_i + c_j must be odd. Since r_i = 0 (even), c_j must be odd for all j. So every column has an odd number of checkers, hence ≥ 1. So M = Σc_j ≥ n. Contradiction.

And M = n is achievable (place n checkers in one column). So f(n) = n.

Therefore f(20) + f(21) = 20 + 21 = 41.

That's a clean proof. Let me write it up.

Actually wait, I need to double-check the M = n construction more carefully.

Construction: Place checkers at (1,1), (2,1), ..., (n,1). So all n checkers are in column 1.

Row sums: r_i = 1 for all i (odd).
Column sums: c_1 = n, c_j = 0 for j ≥ 2.

For an empty cell (i,j):
- If j = 1: cell (i,1) is occupied, not empty. Skip.
- If j ≥ 2: r_i + c_j = 1 + 0 = 1 (odd). ✓

So every empty cell has r_i + c_j odd. The configuration is maximal. M = n. ✓

And the lower bound M ≥ n is proven. So f(n) = n, and f(20) + f(21) = 41.

Let me also sanity-check: is the initial placement valid? We need to place checkers one at a time, each time the placement is valid (the cell is empty and the remaining 2n-2 cells have even count).

When we place the first checker at (1,1): row 1 has 0 other checkers, column 1 has 0 other checkers. Total = 0 (even). ✓
When we place the second checker at (2,1): row 2 has 0 other checkers, column 1 has 1 other checker. Total = 1 (odd). ✗!

Oops! The placement at (2,1) is not valid because column 1 already has 1 checker (at (1,1)), and 1 is odd.

So we can't just place all n checkers in one column sequentially! The order matters, and we need to find a valid sequence.

Hmm, this changes things. The problem says Ivan places checkers one at a time, each placement must be valid. The final configuration must be maximal. We want to minimize the number of checkers in a maximal configuration that is reachable by some valid sequence of placements.

So the question is: which maximal configurations are reachable? Not all of them necessarily are.

Let me reconsider. A checker can be placed at cell C if:
1. C is empty.
2. The number of checkers in the other 2n-2 cells of C's row and column is even.

If C = (i,j), the count is (r_i - [C occupied]) + (c_j - [C occupied]) = r_i + c_j (since C is empty, r_i and c_j don't include C). So the condition is r_i + c_j is even.

So at each step, we can place a checker at (i,j) iff (i,j) is empty and r_i + c_j is even.

The final configuration must be maximal: for every empty (i,j), r_i + c_j is odd.

So during the process, we place checkers at cells where r_i + c_j is even, and we stop when all empty cells have r_i + c_j odd.

The question is: what is the minimum M such that there exists a sequence of M valid placements leading to a maximal configuration?

This is different from just finding the minimum maximal configuration! We need the configuration to be reachable.

Let me reconsider. The configuration with all checkers in one column: is it reachable?

Start: all r_i = 0, all c_j = 0. r_i + c_j = 0 (even) for all cells. We can place at any cell.

Place at (1,1): r_1 = 1, c_1 = 1. Now:
- (i, 1) for i ≥ 2: r_i + c_1 = 0 + 1 = 1 (odd). Can't place.
- (1, j) for j ≥ 2: r_1 + c_j = 1 + 0 = 1 (odd). Can't place.
- (i, j) for i ≥ 2, j ≥ 2: r_i + c_j = 0 + 0 = 0 (even). Can place.

So after placing at (1,1), we can only place in the (n-1)×(n-1) sub-board excluding row 1 and column 1.

Place at (2,2): r_2 = 1, c_2 = 1. Now:
- (i, 1) for i ≥ 2: r_i + c_1 = 0 + 1 = 1 (odd). Can't.
- (1, j) for j ≥ 2: r_1 + c_j = 1 + 0 = 1 (odd). Can't.
- (i, 2) for i ≥ 3: r_i + c_2 = 0 + 1 = 1 (odd). Can't.
- (2, j) for j ≥ 3: r_2 + c_j = 1 + 0 = 1 (odd). Can't.
- (i, j) for i ≥ 3, j ≥ 3: r_i + c_j = 0 + 0 = 0 (even). Can place.

So we're forced to place at (3,3), then (4,4), etc. This gives us a diagonal: (1,1), (2,2), ..., (n,n). After placing all n diagonal checkers:
r_i = 1 for all i, c_j = 1 for all j.
For any empty cell (i,j) (i ≠ j): r_i + c_j = 1 + 1 = 2 (even). So we can still place!

So the diagonal is not maximal. We can continue placing.

After the diagonal, we can place at any off-diagonal cell (since r_i + c_j = 2, even). Place at (1,2): r_1 = 2, c_2 = 2. Now:
- (i, 2) for i ≠ 1: r_i + c_2 = 1 + 2 = 3 (odd). Can't place in column 2 (except (1,2) which is occupied).
- (1, j) for j ≠ 2: r_1 + c_j = 2 + 1 = 3 (odd). Can't place in row 1.
- (i, j) for i ≥ 2, j ≥ 3, i ≠ j: r_i + c_j = 1 + 1 = 2 (even). Can place.

So after diagonal + (1,2), we can place in the sub-board excluding rows 1,2 and columns 1,2 (off-diagonal). Place at (3,4): r_3 = 2, c_4 = 2. Etc.

This is getting complicated. Let me think about this differently.

The key insight is that the process is constrained: we can only place at cells where r_i + c_j is even. The final state must have all empty cells with r_i + c_j odd.

Let me think about what final states are reachable.

Observation: At each step, placing a checker at (i,j) changes r_i by +1 and c_j by +1. So r_i + c_j changes by +2 (from even to even, or odd to odd). Wait, the parity of r_i + c_j doesn't change when we place at (i,j)! Because both r_i and c_j increase by 1, so r_i + c_j increases by 2, parity unchanged.

But wait, placing at (i,j) also affects other cells. For cell (i, k) with k ≠ j: r_i increases by 1, c_k unchanged. So r_i + c_k changes parity. For cell (k, j) with k ≠ i: r_k unchanged, c_j increases by 1. So r_k + c_j changes parity.

So placing a checker at (i,j):
- Doesn't change parity of r_i + c_j (the placed cell).
- Flips parity of r_i + c_k for all k ≠ j (same row, different column).
- Flips parity of r_k + c_j for all k ≠ i (same column, different row).
- Doesn't affect r_k + c_l for k ≠ i, l ≠ j.

Interesting. So the parity of r_i + c_j for each cell evolves as we place checkers.

Initially, all r_i + c_j = 0 (even). We can place at any cell.

When we place at (i,j), the parities of cells in row i (except (i,j)) and column j (except (i,j)) flip. The cell (i,j) itself stays even (but becomes occupied, so it doesn't matter).

We want to reach a state where all empty cells have odd parity, and we want to minimize the number of occupied cells.

This is like a lights-out puzzle! We have an n×n grid of parities, all starting even. Each move at (i,j) flips the parities of all cells in row i and column j except (i,j) itself (and (i,j) becomes occupied, removing it from consideration). We want to reach a state where all remaining (empty) cells have odd parity, minimizing the number of moves (occupied cells).

Hmm, this is more complex than I initially thought. Let me reconsider.

Actually, let me think about it in terms of the parity matrix. Let P(i,j) = (r_i + c_j) mod 2. Initially all 0. When we place at (i,j), P(i,k) flips for all k ≠ j, and P(k,j) flips for all k ≠ i. P(i,j) is now irrelevant (cell occupied).

We want: all empty cells have P = 1.

Equivalently, let's track which cells are occupied and the parity matrix. The parity matrix P is determined by the row and column sums: P(i,j) = (r_i + c_j) mod 2.

Let me think about the parity of r_i and c_j. Let R_i = r_i mod 2 and C_j = c_j mod 2. Then P(i,j) = R_i ⊕ C_j.

Initially R_i = 0, C_j = 0 for all i,j. P(i,j) = 0 for all i,j.

When we place at (i,j): R_i flips, C_j flips. So P(i,j) = (R_i ⊕ 1) ⊕ (C_j ⊕ 1) = R_i ⊕ C_j (unchanged). P(i,k) = (R_i ⊕ 1) ⊕ C_k = P(i,k) ⊕ 1 (flips). P(k,j) = R_k ⊕ (C_j ⊕ 1) = P(k,j) ⊕ 1 (flips). P(k,l) = R_k ⊕ C_l (unchanged). ✓

So the state is determined by the vectors R = (R_1, ..., R_n) and C = (C_1, ..., C_n), plus the set of occupied cells. P(i,j) = R_i ⊕ C_j.

The maximal condition: for every empty cell (i,j), R_i ⊕ C_j = 1, i.e., R_i ≠ C_j.

This means: if R_i = C_j, then (i,j) must be occupied. (Same as before.)

The reachability condition: we start with R = 0, C = 0, and at each step, we place at an empty cell (i,j) with R_i ⊕ C_j = 0 (i.e., R_i = C_j), which flips R_i and C_j.

So at each step, we must place at a cell where R_i = C_j, and this flips both R_i and C_j.

We want to reach a state (R, C, occupied set) where:
1. All cells with R_i = C_j are occupied.
2. The number of occupied cells is minimized.

And the state must be reachable from (R=0, C=0, empty) by the above rules.

Let me think about what states (R, C) are reachable. Starting from R=0, C=0, each move flips one R_i and one C_j (where R_i = C_j currently). 

Let's track the number of 1s in R and C. Let a = |{i : R_i = 0}| (even rows), so n-a rows have R_i = 1. Similarly c = |{j : C_j = 0}|.

Initially a = n, c = n (all 0s). 

When we place at (i,j) with R_i = C_j:
- If R_i = C_j = 0: R_i flips to 1, C_j flips to 1. a decreases by 1, c decreases by 1.
- If R_i = C_j = 1: R_i flips to 0, C_j flips to 0. a increases by 1, c increases by 1.

So each move either decreases both a and c by 1, or increases both by 1. Therefore, a - c is invariant! Initially a - c = 0. So a = c always.

This is a key constraint: in any reachable state, the number of even rows equals the number of even columns.

Also, a + c has the same parity as n + n = 2n (always even), and each move changes a + c by ±2, so a + c is always even. Since a = c, this is automatic.

Now, the total number of moves M. Each move changes a by ±1. Starting from a = n, after M moves, a = n + (number of "increase" moves) - (number of "decrease" moves). Let u = increase moves, d = decrease moves. M = u + d, a = n + u - d = n + u - (M - u) = n + 2u - M. So M = n + 2u - a, i.e., M = n - a + 2u.

Since u ≥ 0, M ≥ n - a. Also, a = c, and a ∈ {0, 1, ..., n} with a ≡ n (mod 2)? Let me check: initially a = n. Each move changes a by ±1. So after M moves, a ≡ n - M (mod 2) ... no, a = n + (sum of ±1's), so a ≡ n + M (mod 2) ... actually a ≡ n + (u - d) (mod 2) = n + (2u - M) (mod 2) = n + M (mod 2). So a ≡ n + M (mod 2), i.e., M ≡ a - n (mod 2), i.e., M ≡ a + n (mod 2).

Hmm, let me think about what constraints we have:
1. a = c (from reachability).
2. The occupied cells are exactly: all (i,j) with R_i = C_j, plus possibly some with R_i ≠ C_j (but we want to minimize, so we'd avoid those unless needed for reachability).
3. M ≥ (number of cells with R_i = C_j) = a² + (n-a)² (since a = c, same-parity cells are (even,even) = a² and (odd,odd) = (n-a)²).

Wait, but we also need to account for the optional cells. The minimal maximal configuration for a given (a, c) with a = c has:
Mandatory: a² + (n-a)² cells (since c = a, d = n-a = b).
Optional: we need to satisfy parity constraints.

But now with the reachability constraint a = c, let me redo the analysis.

With a = c, b = n - a, d = n - a = b. So b = d.

Sub-matrix 1 (E_r, O_c) = (a, b):
- r₁ = a if c odd, 0 if c even. c = a, so r₁ = a if a odd, 0 if a even.
- s₁ = b if a even (b even... wait, b = n-a. s₁ = d if b even, 0 if b odd. d = b. s₁ = b if b even, 0 if b odd.

Hmm wait, I need to recompute. s₁ = d if b is even, 0 if b is odd. And d = n - c = n - a = b. So s₁ = b if b even, 0 if b odd.

And r₁ = a if c odd (c = a, so a odd), 0 if a even.

Case 1: a even, b = n-a. 
- r₁ = 0 (a even → c even).
- s₁ = b if b even, 0 if b odd.
- If b even (        — AI历史解题过程（thinking）
#   polymath_00734         — 题目ID

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
  <problem_id>polymath_00734</problem_id>
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

Ivan places checkers on an $n \times n$ table according to the following rule: a checker can be placed in cell $C$ if there is no checker there yet, and in the remaining $2n - 2$ cells of the row and column of $C$ there is an even number of checkers. After placing $M$ checkers, Ivan found that it is impossible to place any more checkers. Let $f(n)$ be the minimum possible value of $M$. Find the value of $f(20) + f(21)$.

## Standard Solution

According to the solution, the minimum number of checkers $M$ for a given $n$ is $f(n) = \frac{n^{2} + 1}{2}$ when $n$ is odd, and $f(n) = \frac{n^{2}}{2} + n$ when $n$ is even.
For $n = 20$, $f(20) = \frac{20^2}{2} + 20 = 200 + 20 = 220$.
For $n = 21$, $f(21) = \frac{21^2 + 1}{2} = \frac{441 + 1}{2} = \frac{442}{2} = 221$.
The sum is $220 + 221 = 441$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have an n×n table. A checker can be placed in cell C if:
1. There is no checker there yet
2. In the remaining 2n-2 cells of the row and column of C, there is an even number of checkers.

After placing M checkers, it's impossible to place any more. f(n) = minimum possible M. Find f(20) + f(21).

Let me think about this. Let's denote the number of checkers in row i as r_i and in column j as c_j. For cell (i,j), the number of checkers in its row and column (excluding itself) is (r_i - [checker at (i,j)]) + (c_j - [checker at (i,j)]) = r_i + c_j - 2*[checker at (i,j)]. Since the cell is empty when we consider placing, this is r_i + c_j.

Wait, the 2n-2 cells are the other cells in row i (n-1 cells) and column j (n-1 cells), total 2n-2. The number of checkers in those cells is r_i + c_j (since cell (i,j) is empty, r_i counts checkers in row i not including (i,j), and c_j counts checkers in column j not including (i,j)). Actually r_i is the total in row i, but since (i,j) is empty, r_i = number of checkers in row i excluding (i,j). Similarly c_j. So the count is r_i + c_j.

So we can place a checker at (i,j) iff (i,j) is empty and r_i + c_j is even.

A configuration is "maximal" (no more checkers can be placed) iff for every empty cell (i,j), r_i + c_j is odd.

We want to minimize the total number of checkers M in a maximal configuration.

Let me think about the structure. Let's say a row is "even" if r_i is even, "odd" if r_i is odd. Similarly for columns.

For an empty cell (i,j), we need r_i + c_j odd, meaning one of r_i, c_j is even and the other is odd.

So: for every empty cell (i,j), row i and column j have different parities.

Equivalently: if row i and column j have the same parity, then cell (i,j) must be occupied.

Let me partition rows into even rows (E_r) and odd rows (O_r), and columns into even columns (E_c) and odd columns (O_c).

Cells where row and column have same parity: (E_r, E_c) and (O_r, O_c) — these must all be occupied.

Cells where row and column have different parity: (E_r, O_c) and (O_r, E_c) — these can be empty or occupied.

But wait, we also need the parities to be consistent. If a row is in E_r, it has an even number of checkers. The occupied cells in that row are: all cells in (E_r row, E_c columns) [same parity, must be occupied] plus possibly some cells in (E_r row, O_c columns) [different parity, optional].

Let me denote:
- a = number of even rows
- b = number of odd rows = n - a
- c = number of even columns
- d = number of odd columns = n - c

For an even row i (in E_r): it must occupy all cells in E_c columns (that's c cells) plus optionally some in O_c columns. The total must be even. c + (optional count) must be even. So optional count must have the same parity as c.

For an odd row i (in O_r): it must occupy all cells in O_c columns (that's d cells) plus optionally some in E_c columns. The total must be odd. d + (optional count) must be odd. So optional count must have parity different from d, i.e., optional count ≡ 1 - d (mod 2) ≡ 1+d (mod 2).

For an even column j (in E_c): it must occupy all cells in E_r rows (that's a cells) plus optionally some in O_r rows. Total must be even. a + optional must be even. So optional ≡ a (mod 2).

For an odd column j (in O_c): it must occupy all cells in O_r rows (that's b cells) plus optionally some in E_r rows. Total must be odd. b + optional must be odd. So optional ≡ 1+b (mod 2) ≡ 1-b (mod 2).

Now, the mandatory checkers are:
- (E_r, E_c): a × c cells
- (O_r, O_c): b × d cells

The optional cells are:
- (E_r, O_c): a × d cells
- (O_r, E_c): b × c cells

We want to minimize total checkers = mandatory + optional.

Mandatory = ac + bd = ac + (n-a)(n-c).

To minimize, we want to minimize the optional checkers placed, subject to parity constraints.

Let me think about the optional cells. Let x = number of optional cells in (E_r, O_c) that are occupied, and y = number of optional cells in (O_r, E_c) that are occupied.

Constraints:
- For each even row: the number of occupied optional cells (in O_c) must have parity ≡ c (mod 2).
- For each odd row: the number of occupied optional cells (in E_c) must have parity ≡ 1+d (mod 2).
- For each even column: the number of occupied optional cells (in O_r) must have parity ≡ a (mod 2).
- For each odd column: the number of occupied optional cells (in E_r) must have parity ≡ 1+b (mod 2).

These are parity constraints on rows and columns of the optional sub-matrices.

Let me think of the (E_r, O_c) sub-matrix of size a × d. Each row (even row) needs the sum to have parity ≡ c (mod 2). Each column (odd column) needs the sum to have parity ≡ 1+b (mod 2).

The minimum number of 1s in an a × d binary matrix where each row sum has a specified parity and each column sum has a specified parity.

For this to be feasible, the total parity must be consistent: sum of row parities ≡ sum of column parities (mod 2).

Sum of row parities for (E_r, O_c): a rows, each with parity c. Total ≡ ac (mod 2).
Sum of column parities for (E_r, O_c): d columns, each with parity 1+b. Total ≡ d(1+b) (mod 2).

Need: ac ≡ d(1+b) (mod 2).

Similarly for (O_r, E_c) sub-matrix of size b × c. Each row (odd row) needs sum parity ≡ 1+d. Each column (even column) needs sum parity ≡ a.

Sum of row parities: b(1+d) (mod 2).
Sum of column parities: ca (mod 2).

Need: b(1+d) ≡ ca (mod 2).

Let me check if these are the same condition. d(1+b) = d + bd. ac. So ac ≡ d + bd (mod 2), i.e., ac + d + bd ≡ 0 (mod 2), i.e., ac + d(1+b) ≡ 0 (mod 2).

Second: b(1+d) ≡ ca (mod 2), i.e., b + bd ≡ ac (mod 2), i.e., ac + b + bd ≡ 0 (mod 2), i.e., ac + b(1+d) ≡ 0 (mod 2).

These are different conditions in general. Let me see... ac + d + bd ≡ 0 and ac + b + bd ≡ 0. Subtracting: d - b ≡ 0 (mod 2), i.e., d ≡ b (mod 2), i.e., (n-c) ≡ (n-a) (mod 2), i.e., a ≡ c (mod 2).

So if a ≡ c (mod 2), both conditions are the same: ac + b + bd ≡ 0 (mod 2).

If a ≢ c (mod 2), the two conditions are contradictory, meaning we can't satisfy both sub-matrix constraints simultaneously? Wait, no — the two sub-matrices are independent. Let me reconsider.

Actually, the (E_r, O_c) and (O_r, E_c) sub-matrices are independent in terms of which cells they cover. But the parity constraints come from the row/column totals which involve both mandatory and optional cells.

Wait, let me re-examine. For an even row i, the total checkers = c (mandatory in E_c) + (optional in O_c). This must be even. So optional in O_c for row i must have parity ≡ c (mod 2). This only involves the (E_r, O_c) sub-matrix. ✓

For an even column j, the total checkers = a (mandatory in E_r) + (optional in O_r). This must be even. So optional in O_r for column j must have parity ≡ a (mod 2). This only involves the (O_r, E_c) sub-matrix. ✓

So the two sub-matrices are indeed independent. Each has its own feasibility condition.

(E_r, O_c): feasible iff ac ≡ d(1+b) (mod 2).
(O_r, E_c): feasible iff b(1+d) ≡ ca (mod 2).

If both are feasible, the minimum optional checkers is the sum of minimums for each sub-matrix.

If one is infeasible, we need to adjust a, c (the partition).

Hmm, this is getting complex. Let me think about the minimum number of 1s in an m × k binary matrix with given row and column parities.

If all row parities are 0 and all column parities are 0: minimum is 0 (all zeros).
If all row parities are 0 and some column parities are 1: need... if all row parities are 0, total is even, so number of odd columns must be even. Minimum: place 1s to make odd columns odd. If there are t odd columns (t even), we can place 2 ones in one row covering 2 odd columns each... actually minimum is t/2 if we can pair them up, but we need t ≤ m×k and... Let me think more carefully.

Actually, the minimum number of 1s in an m×k binary matrix where row i has parity p_i and column j has parity q_j (with sum p_i ≡ sum q_j mod 2) is:

If all p_i = 0 and all q_j = 0: 0.
Otherwise: at least 1, but could be more.

Let me think about specific cases. Actually, let me think about it differently. The minimum is max(number of odd rows, number of odd columns) if that's achievable, but with parity constraint...

Hmm, let me think about it more carefully. In an m×k matrix:
- Let r = number of rows with odd parity
- Let s = number of columns with odd parity
- Need r ≡ s (mod 2)

The minimum number of 1s: We need each odd row to have at least 1 one, and each odd column to have at least 1 one. But a single 1 can satisfy both an odd row and an odd column. 

If r > 0 and s > 0: We can place min(r,s) ones at intersections of odd rows and odd columns (each such one satisfies one odd row and one odd column). Then we have |r-s| remaining odd rows or columns. If r > s, we have r-s odd rows left, each needs one more 1 (in an even column). We can pair them up: place 2 ones in the same even column for 2 odd rows. So we need r-s additional ones if r-s is even (which it is since r ≡ s mod 2). Wait, r-s is even. So (r-s) additional ones, each in a distinct odd row, in even columns. But each such 1 in an even column doesn't change the column parity (it's already even, adding 1 makes it odd — bad). 

Hmm wait, I need to be more careful. Let me reconsider.

Let's say r odd rows and s odd columns, r ≡ s (mod 2).

Case 1: r = 0, s = 0. Min = 0.
Case 2: r = 0, s > 0 (s even). All rows even, s columns odd. We need s columns to be odd but all rows even. Place 2 ones in each odd column (in 2 different rows). That uses 2s ones but... can we do better? Actually, we can place ones such that each odd column gets an odd number and each row gets an even number. The minimum is s (place 1 in each odd column, all in the same row — but then that row has s ones, which is even since s is even). So min = s. Wait, but we need m ≥ 1 and k ≥ s. If s ≤ k and m ≥ 1, we can place 1 one in each odd column, all in row 1. Row 1 has s ones (even, since s is even). All other rows have 0. Each odd column has 1 (odd). Each even column has 0 (even). So min = s.

Case 3: r > 0, s = 0 (r even). Similarly, min = r.

Case 4: r > 0, s > 0. Place ones at (odd row i, odd column j) for i = 1..min(r,s). This gives min(r,s) ones. Each of the first min(r,s) odd rows gets 1 (odd ✓), each of the first min(r,s) odd columns gets 1 (odd ✓). If r > s: remaining r-s odd rows need 1 more each. But all columns are already satisfied (s odd columns are odd, rest are even). Adding a 1 to an even column makes it odd — bad. So we need to add 2 ones to each remaining odd row: one in an even column (making it odd) and one in the same even column in an even row (making it even again). Wait, that's getting complicated.

Actually, let me reconsider. If r > s, we have r - s remaining odd rows. We need each to get one more 1 (to be odd). But adding a 1 to any column changes its parity. If we add it to an already-odd column, it becomes even (bad). If we add it to an even column, it becomes odd (bad). 

So we can't just add single 1s. We need to add pairs. For each remaining odd row, add 2 ones in 2 different even columns. This makes the row have 1+2=3 (odd ✓), and each of the 2 even columns gets 1 (odd — bad). 

Hmm, this is getting complicated. Let me think differently.

Alternative approach: We need a binary matrix with specified row and column parities. The minimum number of 1s.

Think of it as: we need to "fix" the parities. Start with all zeros (all parities 0). We need row parities p_i and column parities q_j.

The minimum number of 1s is related to the structure. Let me think about it as a graph problem or use a known result.

Actually, I think the answer is: if all parities are 0, min = 0. Otherwise, min = max(r, s) where r = number of odd rows, s = number of odd columns, provided r ≡ s (mod 2) and the matrix is large enough.

Wait, let me verify with small cases. 2×2 matrix, row parities (1,1), column parities (1,1). r=2, s=2. max=2. Can we do it with 2? Place ones at (1,1) and (2,2). Row 1: 1 (odd ✓), Row 2: 1 (odd ✓), Col 1: 1 (odd ✓), Col 2: 1 (odd ✓). Yes! Min = 2 = max(2,2). ✓

2×2 matrix, row parities (1,0), column parities (1,0). r=1, s=1. max=1. Place 1 at (1,1). Row 1: 1 (odd ✓), Row 2: 0 (even ✓), Col 1: 1 (odd ✓), Col 2: 0 (even ✓). Min = 1. ✓

3×3 matrix, row parities (1,1,0), column parities (1,0,0). r=2, s=1. max=2. r-s=1 which is odd, but r≡s mod 2 means 2≡1? No, 2≡0, 1≡1, so 2≢1 mod 2. Infeasible! Indeed, sum of row parities = 2 (even), sum of col parities = 1 (odd). Not consistent. ✓

3×3 matrix, row parities (1,1,0), column parities (1,1,0). r=2, s=2. max=2. Place at (1,1),(2,2). Row 1:1, Row 2:1, Row 3:0. Col 1:1, Col 2:1, Col 3:0. ✓ Min=2.

3×3, row parities (1,1,1), col parities (1,1,1). r=3,s=3. max=3. Place at (1,1),(2,2),(3,3). Each row 1, each col 1. ✓ Min=3.

3×3, row parities (1,1,1), col parities (1,0,0). r=3, s=1. 3≡1 mod 2? 3 is odd, 1 is odd, yes. max=3. Can we do 3? Place at (1,1),(2,1),(3,1)? Col 1: 3 (odd ✓), but rows 1,2,3 each have 1 (odd ✓). Cols 2,3: 0 (even ✓). But wait, that's 3 ones all in column 1. Col 1 has 3 (odd ✓). Yes! Min = 3 = max(3,1). 

Hmm wait, but can we do better? With 1 one: place at (1,1). Row 1: odd ✓, Col 1: odd ✓. But rows 2,3 are even (need odd). No. With 2 ones: need 3 odd rows, impossible with 2 ones (each one can make at most 1 row odd, unless... no, each 1 is in one row). Actually with 2 ones in 2 different rows, we get 2 odd rows, need 3. With 2 ones in same row, 1 odd row. So min is 3. But max(3,1)=3. ✓

What about 2×3, row parities (1,1), col parities (1,1,0). r=2, s=2. max=2. Place at (1,1),(2,2). ✓

What about 1×4, row parities (1), col parities (1,0,0,0). r=1, s=1. max=1. Place at (1,1). ✓

1×4, row parities (0), col parities (1,1,0,0). r=0, s=2. max=2. But all rows even, so we need 2 odd columns with an even number in the single row. Place 1 at (1,1) and (1,2). Row 1: 2 (even ✓), Col 1: 1 (odd ✓), Col 2: 1 (odd ✓). Min = 2 = s. ✓ (max(0,2)=2)

1×4, row parities (0), col parities (1,0,0,0). r=0, s=1. 0≡1? No. Infeasible. ✓

OK so it seems like the minimum is max(r, s) when feasible (r ≡ s mod 2), except when r=0 and s=0, min=0 (which is max(0,0)=0 anyway).

Wait, but there might be size constraints. If r > k (number of columns), we can't have r odd rows since each row needs at least 1 one and... actually no, a row can have multiple ones. Let me reconsider.

If r > 0 and s = 0 (r even): we need r odd rows, all columns even. Place 1 one in each of r rows, all in column 1. Column 1 gets r ones (even ✓ since r is even). Each of r rows gets 1 (odd ✓). Min = r. Need k ≥ 1. ✓

If r > 0 and s > 0: We need max(r,s) ones? Let me check r=4, s=2, 4×2 matrix. max=4. Place at (1,1),(2,2),(3,1),(4,2). Row 1:1, Row 2:1, Row 3:1, Row 4:1 (all odd ✓). Col 1:2 (even — bad, need odd). Hmm.

Let me redo. r=4 odd rows, s=2 odd columns. 4×2 matrix. We need 4 odd rows and 2 odd columns. 

Place at (1,1),(2,1),(3,2),(4,2). Col 1: 2 (even, bad). Col 2: 2 (even, bad).

Place at (1,1),(2,2),(3,1),(4,2). Col 1: 2 (even, bad). 

Hmm, with 4 ones in a 4×2 matrix, each column gets an even number if we distribute evenly. To get 2 odd columns, we need each column to have an odd count. With 4 ones total and 2 columns, we need odd+odd = even, so total is even ✓. But 4 = odd + odd means 1+3, 3+1. So col 1 has 1, col 2 has 3. Col 1 odd ✓, col 2 odd ✓. Rows: 3 rows have 1 one (in col 2), 1 row has 1 one (in col 1). All 4 rows odd ✓. So place at (1,1),(2,2),(3,2),(4,2). Col 1: 1 (odd ✓), Col 2: 3 (odd ✓). All rows: 1 each (odd ✓). Min = 4 = max(4,2). ✓

But wait, can we do it with 3? 3 ones, 4 rows: at most 3 rows have a 1, so at most 3 odd rows. Need 4. No. So min = 4. ✓

What about r=2, s=4, 2×4 matrix? max=4. 2 odd rows, 4 odd columns. Need each column odd. With 4 ones: place 1 in each column, distributed in 2 rows. Row 1: 2 (even, bad). Need odd rows. Row 1: 1 or 3, Row 2: 3 or 1. Place (1,1),(1,2),(2,3),(2,4)? Row 1: 2 (even, bad). Place (1,1),(2,2),(2,3),(2,4)? Row 1: 1 (odd ✓), Row 2: 3 (odd ✓). Col 1:1, Col 2:1, Col 3:1, Col 4:1 (all odd ✓). Min = 4. Can we do 3? 3 ones, 4 columns: at most 3 odd columns. Need 4. No. Min = 4 = max(2,4). ✓

So the minimum number of 1s in an m×k binary matrix with r odd rows and s odd columns (r ≡ s mod 2, feasible) is max(r, s).

But we also need m ≥ 1 and k ≥ 1 (non-degenerate), and we need r ≤ m and s ≤ k (can't have more odd rows than rows). Also, if r = 0 and s = 0, min = 0.

Wait, is there a case where max(r,s) doesn't work due to size? If r > 0, s > 0, and say r = m (all rows odd) and s = k (all columns odd), then max(r,s) = max(m,k). We need to place max(m,k) ones. If m ≥ k, place 1 in each row, distributing among k columns such that each column gets an odd number. Total = m ones, each column gets m/k... we need each column odd. m ones in k columns, each odd: sum of k odd numbers = k mod 2. Need m ≡ k (mod 2), which is given (r ≡ s mod 2, i.e., m ≡ k mod 2). So we need to write m as sum of k odd positive integers. Min sum of k odd positive integers = k. So need m ≥ k, i.e., r ≥ s, which is the case. ✓

OK so I'm fairly convinced: **the minimum number of 1s is max(r, s)** when the parity condition is satisfied and r,s are feasible (r ≤ m, s ≤ k), and 0 when r = s = 0.

Now, back to our problem. We have two independent sub-matrices:

**Sub-matrix 1: (E_r, O_c)**, size a × d.
- Row parities: each of the a rows needs parity ≡ c (mod 2). So if c is even, all rows even (r₁ = 0). If c is odd, all rows odd (r₁ = a).
- Column parities: each of the d columns needs parity ≡ 1+b (mod 2). So if 1+b is even (b odd), all columns even (s₁ = 0). If 1+b is odd (b even), all columns odd (s₁ = d).
- Feasibility: r₁ ≡ s₁ (mod 2). r₁ = a·(c mod 2), s₁ = d·((1+b) mod 2) = d·(b mod 2 ... wait let me be careful. 1+b mod 2: if b is even, 1+b is odd, so s₁ = d. If b is odd, 1+b is even, so s₁ = 0.

So:
- If c even: r₁ = 0. If b even: s₁ = d. Need 0 ≡ d (mod 2), i.e., d even. If b odd: s₁ = 0. Always feasible.
- If c odd: r₁ = a. If b even: s₁ = d. Need a ≡ d (mod 2). If b odd: s₁ = 0. Need a ≡ 0 (mod 2), i.e., a even.

Minimum for sub-matrix 1: max(r₁, s₁) if feasible.

**Sub-matrix 2: (O_r, E_c)**, size b × c.
- Row parities: each of the b rows needs parity ≡ 1+d (mod 2). If d even, 1+d odd, so r₂ = b. If d odd, 1+d even, so r₂ = 0.
- Column parities: each of the c columns needs parity ≡ a (mod 2). If a even, s₂ = 0. If a odd, s₂ = c.
- Feasibility: r₂ ≡ s₂ (mod 2).

So:
- If d even: r₂ = b. If a even: s₂ = 0. Need b ≡ 0 (mod 2), i.e., b even. If a odd: s₂ = c. Need b ≡ c (mod 2).
- If d odd: r₂ = 0. If a even: s₂ = 0. Always feasible. If a odd: s₂ = c. Need 0 ≡ c (mod 2), i.e., c even.

Minimum for sub-matrix 2: max(r₂, s₂) if feasible.

Total checkers M = ac + bd + max(r₁, s₁) + max(r₂, s₂), where we choose a, c to minimize, subject to feasibility.

Let me denote a = number of even rows, c = number of even columns. b = n-a, d = n-c.

Let me compute this for n = 20 and n = 21.

This is getting complex. Let me think about which choices of (a, c) are feasible and compute M.

Let me organize by the parities of a, b, c, d. Since b = n-a and d = n-c, we have b ≡ n-a (mod 2) and d ≡ n-c (mod 2).

Let me consider n = 20 (even). Then b ≡ a (mod 2) and d ≡ c (mod 2) (since n is even, b = 20-a ≡ a mod 2, d = 20-c ≡ c mod 2).

For n = 21 (odd). b ≡ 1-a (mod 2) = 1+a (mod 2), d ≡ 1-c (mod 2) = 1+c (mod 2).

Let me handle n = 20 first.

**n = 20**: b ≡ a (mod 2), d ≡ c (mod 2).

Sub-matrix 1 (a × d):
- r₁ = a if c odd, 0 if c even.
- s₁ = d if b even (i.e., a even), 0 if b odd (i.e., a odd).
- Feasibility:
  - c even, a even: r₁=0, s₁=d. Need d even. d ≡ c ≡ 0 (mod 2). ✓ Always feasible.
  - c even, a odd: r₁=0, s₁=0. ✓ Always feasible.
  - c odd, a even: r₁=a, s₁=d. Need a ≡ d (mod 2). a even, d ≡ c ≡ 1 (mod 2), so d odd. a even, d odd: a ≢ d. **Infeasible**.
  - c odd, a odd: r₁=a, s₁=0. Need a ≡ 0 (mod 2). a odd. **Infeasible**.

So for n=20: sub-matrix 1 is feasible iff c is even (regardless of a). If c is odd, infeasible.

Wait, that means if c is odd, sub-matrix 1 is infeasible for n=20. So we must have c even.

Sub-matrix 2 (b × c), b ≡ a, d ≡ c:
- r₂ = b if d even (c even), 0 if d odd (c odd).
- s₂ = c if a odd, 0 if a even.
- Feasibility:
  - c even, a even: r₂=b, s₂=0. Need b ≡ 0 (mod 2). b ≡ a ≡ 0. ✓
  - c even, a odd: r₂=b, s₂=c. Need b ≡ c (mod 2). b ≡ a ≡ 1, c ≡ 0. 1 ≢ 0. **Infeasible**.
  - c odd, a even: r₂=0, s₂=0. ✓
  - c odd, a odd: r₂=0, s₂=c. Need 0 ≡ c (mod 2). c odd. **Infeasible**.

So for n=20: sub-matrix 2 is feasible iff (c even and a even) or (c odd and a even). I.e., a must be even.

Combined: both feasible iff c even and a even.

So for n = 20, we need a even and c even. Let a = 2p, c = 2q, where 0 ≤ p ≤ 10, 0 ≤ q ≤ 10.

b = 20 - 2p, d = 20 - 2q. All even.

Sub-matrix 1 (a × d = 2p × (20-2q)):
- c even → r₁ = 0.
- a even → b even → s₁ = d = 20-2q.
- Feasible (d even ✓).
- Min₁ = max(0, 20-2q) = 20-2q (if q < 10) or 0 (if q = 10).

Sub-matrix 2 (b × c = (20-2p) × 2q):
- c even → d even → r₂ = b = 20-2p.
- a even → s₂ = 0.
- Feasible (b even ✓).
- Min₂ = max(20-2p, 0) = 20-2p (if p < 10) or 0 (if p = 10).

Total M = ac + bd + Min₁ + Min₂
= (2p)(2q) + (20-2p)(20-2q) + (20-2q) + (20-2p)
= 4pq + (20-2p)(20-2q) + (20-2q) + (20-2p)
= 4pq + 400 - 40q - 40p + 4pq + 40 - 2q - 2p
= 8pq + 440 - 42p - 42q

Wait let me recompute. (20-2p)(20-2q) = 400 - 40q - 40p + 4pq.

M = 4pq + 400 - 40q - 40p + 4pq + 20 - 2q + 20 - 2p
= 8pq + 440 - 42p - 42q

Hmm wait, but this is only when p < 10 and q < 10. If p = 10, then b = 0, Min₂ = 0 (not 20-2p = 0, same thing). If q = 10, d = 0, Min₁ = 0. So the formula works for all p, q in range since 20-2p = 0 when p=10.

Let me verify: p=10, q=10: M = 8·100 + 440 - 420 - 420 = 800 + 440 - 840 = 400. That's a = 20, c = 20, all rows even, all columns even. All cells in (E_r, E_c) = all 400 cells occupied. That's the full board. Makes sense but not minimal.

M = 8pq - 42p - 42q + 440.

To minimize, take derivative: ∂M/∂p = 8q - 42, ∂M/∂q = 8p - 42. Setting to 0: q = 42/8 = 5.25, p = 5.25. So optimal around p = q = 5 or 6.

But p, q must be integers in [0, 10].

p=5, q=5: M = 8·25 - 42·5 - 42·5 + 440 = 200 - 210 - 210 + 440 = 220.
p=5, q=6: M = 8·30 - 42·5 - 42·6 + 440 = 240 - 210 - 252 + 440 = 218.
p=6, q=5: M = 8·30 - 42·6 - 42·5 + 440 = 240 - 252 - 210 + 440 = 218.
p=6, q=6: M = 8·36 - 42·6 - 42·6 + 440 = 288 - 252 - 252 + 440 = 224.
p=5, q=7: M = 8·35 - 42·5 - 42·7 + 440 = 280 - 210 - 294 + 440 = 216.
p=7, q=5: M = 216 (symmetric).
p=5, q=8: M = 8·40 - 42·5 - 42·8 + 440 = 320 - 210 - 336 + 440 = 214.
p=8, q=5: M = 214.
p=5, q=9: M = 8·45 - 42·5 - 42·9 + 440 = 360 - 210 - 378 + 440 = 212.
p=9, q=5: M = 212.
p=5, q=10: M = 8·50 - 42·5 - 42·10 + 440 = 400 - 210 - 420 + 440 = 210.
p=10, q=5: M = 210.
p=4, q=10: M = 8·40 - 42·4 - 42·10 + 440 = 320 - 168 - 420 + 440 = 172.
p=10, q=4: M = 172.
p=3, q=10: M = 8·30 - 42·3 - 42·10 + 440 = 240 - 126 - 420 + 440 = 134.
p=10, q=3: M = 134.
p=2, q=10: M = 8·20 - 42·2 - 42·10 + 440 = 160 - 84 - 420 + 440 = 96.
p=10, q=2: M = 96.
p=1, q=10: M = 8·10 - 42·1 - 42·10 + 440 = 80 - 42 - 420 + 440 = 58.
p=10, q=1: M = 58.
p=0, q=10: M = 0 - 0 - 420 + 440 = 20.
p=10, q=0: M = 0 - 420 - 0 + 440 = 20.

Interesting! p=0, q=10: a=0, c=20. All rows odd (b=20), all columns even (c=20, d=0).
M = ac + bd + Min₁ + Min₂ = 0 + 20·0 + 0 + 20 = 20.

Wait, let me check: a=0 (no even rows), c=20 (all even columns), b=20, d=0.
Mandatory: ac + bd = 0 + 20·0 = 0.
Sub-matrix 1: (E_r, O_c) = (0, 0) = empty. Min₁ = 0.
Sub-matrix 2: (O_r, E_c) = (20, 20). r₂ = b = 20 (d even), s₂ = 0 (a even). Min₂ = max(20, 0) = 20.
Total = 0 + 0 + 0 + 20 = 20. ✓

But wait, what does this configuration look like? All rows are odd, all columns are even. Mandatory cells: (E_r, E_c) = empty (no even rows), (O_r, O_c) = empty (no odd columns). So no mandatory cells. Optional: (O_r, E_c) = all 20×20 cells. We need to place 20 checkers such that each row has odd count and each column has even count. That's 20 ones in a 20×20 matrix with all rows odd and all columns even.

Sum of row counts = 20 (odd) × ... wait, 20 rows each odd. Sum = 20 odd numbers = even. Sum of column counts = 20 even numbers = even. Consistent. ✓

Min = 20 (place 1 in each row, all in column 1: column 1 has 20 (even ✓), each row has 1 (odd ✓), other columns 0 (even ✓)). Total = 20. ✓

But is this actually maximal? Let me verify. All rows have odd count, all columns have even count. For any empty cell (i,j): r_i is odd, c_j is even. r_i + c_j = odd + even = odd. ✓ So no more checkers can be placed. It's maximal. ✓

Can we do better than 20? Let me check p=0, q=10 gives M=20. Can we get lower?

p=0, q=9: M = 0 - 0 - 378 + 440 = 62. Worse.
p=1, q=10: M = 58. Worse.
p=0, q=10: M = 20. p=10, q=0: M = 20.

What about p=0, q=10 vs other extremes? Let me check p=0, q=10 more carefully. a=0, c=20.

Actually, let me also check: are there feasible configurations with a odd or c odd that I dismissed? I showed that for n=20, both sub-matrices are feasible only when a even and c even. So we're restricted to a, c both even. The minimum over all even a, c is 20 (at a=0, c=20 or a=20, c=0).

Wait, but a=0 means no even rows. Is that valid? a=0 means all rows are odd. That's fine. c=20 means all columns are even. That's fine.

Hmm, but actually I should double-check: can we get M < 20? Let me think about lower bounds.

Actually, let me reconsider. With a=0, c=20: all rows odd, all columns even. We need at least... each of the 20 rows must have an odd number of checkers, so at least 1 each, so at least 20. And we achieved 20. So M = 20 for this configuration.

Can we do better with a different approach? What if a=0, c=0? All rows odd, all columns odd. Then:
Mandatory: (E_r, E_c) = 0, (O_r, O_c) = 20×20 = 400. That's 400 mandatory. Way too much.

What about a=20, c=0? All rows even, all columns odd.
Mandatory: (E_r, E_c) = 0, (O_r, O_c) = 0. 
Sub-matrix 1: (E_r, O_c) = (20, 20). c=0 even → r₁=0. a=20 even → b=0 even → s₁=d=20. Min₁ = 20.
Sub-matrix 2: (O_r, E_c) = (0, 0). Min₂ = 0.
Total = 0 + 0 + 20 + 0 = 20. Same.

So for n=20, f(20) = 20? Let me think about whether we can do better...

Actually, wait. I need to reconsider. The minimum of 20 checkers for a 20×20 board. Each row must have at least 1 checker (if all rows are odd, each needs ≥1). But what if some rows have 0 checkers (even)? Then we'd have a mix.

With a=0, c=20 (all odd rows, all even columns): each row needs ≥1, so M ≥ 20. Achieved.

With a=2, c=20: 2 even rows, 18 odd rows, all even columns.
Mandatory: ac + bd = 2·20 + 18·0 = 40.
Sub-matrix 1: (2, 0) = empty. Min₁ = 0.
Sub-matrix 2: (18, 20). r₂ = 18, s₂ = 0. Min₂ = 18.
Total = 40 + 0 + 18 = 58. Worse.

So indeed a=0, c=20 (or a=20, c=0) gives the minimum of 20 for n=20.

But wait, I should also check: is 20 really the minimum, or can we be cleverer? Let me think about a lower bound.

In a maximal configuration, every empty cell (i,j) has r_i + c_j odd. Consider the sum S = Σ_i r_i + Σ_j c_j = 2M (each checker counted once in its row and once in its column). 

Hmm, let me think about it differently. If the configuration is maximal, for every empty cell, r_i and c_j have different parities. 

Consider the bipartite graph where rows and columns are vertices, and occupied cells are edges. The degree of row i is r_i, degree of column j is c_j.

For every non-edge (i,j), deg(i) and deg(j) have different parities.

This means: in the bipartite complement graph (non-edges), every edge connects vertices of different parity. So the complement graph is bipartite with respect to the parity partition. I.e., non-edges only go between even-odd pairs.

Equivalently, all same-parity pairs (even row, even column) and (odd row, odd column) must be edges (occupied).

This is exactly what I had before. So the analysis is correct.

Now, for the minimum: we need all (even row, even col) and (odd row, odd col) cells occupied, plus some optional cells to satisfy parity. The minimum over all parity assignments.

For n=20, I found f(20) = 20. Let me now do n=21.

**n = 21**: b = 21-a, d = 21-c. b ≡ 1+a (mod 2) [since 21 is odd], d ≡ 1+c (mod 2).

So: a even → b odd; a odd → b even. c even → d odd; c odd → d even.

Sub-matrix 1 (a × d):
- r₁ = a if c odd, 0 if c even.
- s₁ = d if b even (a odd), 0 if b odd (a even).
- Feasibility:
  - c even, a even: r₁=0, s₁=0 (b odd). ✓
  - c even, a odd: r₁=0, s₁=d (b even). Need 0 ≡ d (mod 2). d ≡ 1+c ≡ 1 (mod 2), d odd. 0 ≢ 1. **Infeasible**.
  - c odd, a even: r₁=a, s₁=0 (b odd). Need a ≡ 0 (mod 2). a even. ✓
  - c odd, a odd: r₁=a, s₁=d (b even). Need a ≡ d (mod 2). a odd, d ≡ 1+c ≡ 0 (mod 2), d even. odd ≢ even. **Infeasible**.

So sub-matrix 1 feasible iff a even (regardless of c).

Sub-matrix 2 (b × c):
- r₂ = b if d even (c odd), 0 if d odd (c even).
- s₂ = c if a odd, 0 if a even.
- Feasibility:
  - c even, a even: r₂=0, s₂=0. ✓
  - c even, a odd: r₂=0, s₂=c. Need 0 ≡ c (mod 2). c even. ✓
  - c odd, a even: r₂=b, s₂=0. Need b ≡ 0 (mod 2). b ≡ 1+a ≡ 1 (mod 2), b odd. odd ≢ 0. **Infeasible**.
  - c odd, a odd: r₂=b, s₂=c. Need b ≡ c (mod 2). b ≡ 1+a ≡ 0 (mod 2), b even. c odd. even ≢ odd. **Infeasible**.

So sub-matrix 2 feasible iff c even (regardless of a).

Combined: both feasible iff a even AND c even.

For n=21, a even, c even. Let a = 2p, c = 2q, 0 ≤ p ≤ 10, 0 ≤ q ≤ 10 (since a ≤ 21, c ≤ 21, and even, so max is 20).

b = 21 - 2p, d = 21 - 2q. Both odd.

Sub-matrix 1 (a × d = 2p × (21-2q)):
- c even → r₁ = 0.
- a even → b odd → s₁ = 0.
- Min₁ = 0.

Sub-matrix 2 (b × c = (21-2p) × 2q):
- c even → d odd → r₂ = 0.
- a even → s₂ = 0.
- Min₂ = 0.

Total M = ac + bd + 0 + 0 = (2p)(2q) + (21-2p)(21-2q) = 4pq + 441 - 42q - 42p + 4pq = 8pq - 42p - 42q + 441.

Minimize: ∂M/∂p = 8q - 42 = 0 → q = 5.25, ∂M/∂q = 8p - 42 = 0 → p = 5.25.

Check boundary: p=0, q=0: M = 441 (all rows odd, all columns odd, all cells mandatory). 
p=0, q=10: M = 0 - 0 - 420 + 441 = 21.
p=10, q=0: M = 0 - 420 - 0 + 441 = 21.
p=10, q=10: M = 800 - 420 - 420 + 441 = 401.
p=5, q=5: M = 200 - 210 - 210 + 441 = 221.
p=0, q=10: M = 21.

Let me check p=0, q=10: a=0, c=20, b=21, d=1.
Mandatory: ac + bd = 0 + 21·1 = 21.
Sub-matrix 1: (0, 1) = empty. Min₁ = 0.
Sub-matrix 2: (21, 20). r₂=0, s₂=0. Min₂=0.
Total = 21. ✓

What's the configuration? a=0 (all rows odd), c=20 (20 even columns), d=1 (1 odd column). Mandatory: (O_r, O_c) = 21×1 = 21 cells (all cells in the single odd column). (E_r, E_c) = 0. No optional cells needed.

So all 21 cells in one column are occupied. Each row has 1 checker (odd ✓). The odd column has 21 checkers (odd ✓). Each even column has 0 (even ✓). For any empty cell (i,j) where j is an even column: r_i = 1 (odd), c_j = 0 (even). 1+0 = 1 (odd ✓). Maximal. ✓

Can we do better? p=0, q=10 gives 21. Let me check other values.

p=1, q=10: M = 8·10 - 42 - 420 + 441 = 80 - 42 - 420 + 441 = 59. Worse.
p=0, q=9: M = 0 - 0 - 378 + 441 = 63. Worse.

So the minimum for n=21 is 21, achieved at (p=0, q=10) or (p=10, q=0).

Wait, but I should check: is there a configuration with a or c odd that could give a lower M? I showed that for n=21, both sub-matrices are feasible only when a even and c even. If a or c is odd, one sub-matrix is infeasible, meaning we can't satisfy the parity constraints. So those configurations are impossible.

Hmm, but wait — I need to reconsider. When a sub-matrix is "infeasible," it means we can't satisfy the parity constraints for that sub-matrix. But the parity constraints come from the requirement that rows have even/odd counts. If we can't satisfy them, that partition (a,c) doesn't work. So indeed we're restricted to a even, c even for n=21.

So f(21) = 21.

And f(20) = 20.

f(20) + f(21) = 20 + 21 = 41.

Wait, but let me double-check f(20) = 20 more carefully. I want to make sure there isn't a configuration outside my framework that does better.

Actually, my framework is complete: any maximal configuration must have the property that all same-parity (row, col) pairs are occupied. The partition into even/odd rows and columns is determined by the configuration. So the framework covers all maximal configurations. The minimum over all valid (a,c) partitions is f(n).

For n=20, the minimum is 20 (at a=0,c=20 or a=20,c=0).
For n=21, the minimum is 21 (at a=0,c=20 or a=10,c=0... wait, a=0,c=20: b=21,d=1, M=21).

Hmm wait, for n=21, let me also check a=20, c=0: p=10, q=0. M = 0 - 420 - 0 + 441 = 21. a=20 (even rows), c=0 (no even columns), b=1, d=21. Mandatory: ac + bd = 0 + 1·21 = 21. Same.

And a=0, c=0: p=0, q=0. M = 441. All rows odd, all columns odd, all 21² = 441 cells mandatory. Bad.

So f(20) + f(21) = 20 + 21 = 41.

But wait, I want to be more careful. Let me re-examine the n=20 case. I claimed the minimum is 20, achieved at a=0, c=20. Let me verify this is truly minimal by checking if there's any way to get fewer than 20.

With a=0, c=20: all 20 rows are odd (each has ≥1 checker), all 20 columns are even. M = 20. Since each row needs at least 1 checker (being odd), M ≥ 20. So 20 is optimal for this partition.

For any other feasible partition (a even, c even, a > 0): we showed M ≥ 58 (at a=2, c=20). So 20 is the overall minimum.

Actually, let me also think about whether there's a smarter lower bound. In any maximal configuration on an n×n board, consider the rows. Each row has some number of checkers. If a row has 0 checkers (even), then for every column j, c_j must be odd (since r_i = 0 is even, we need r_i + c_j odd, so c_j odd). If all columns are odd, then every cell in an even row must be occupied (same parity: even row, odd column... wait, even row and odd column are different parities, so those cells can be empty).

Hmm, let me reconsider. If a row has 0 checkers (even), then for every empty cell in that row, c_j must be odd. But cells in that row that are occupied... there are none (0 checkers). So all cells in that row are empty, and for all of them, c_j must be odd. So all columns must be odd.

If all columns are odd, then each column has ≥1 checker, so M ≥ n. And for n=20, M ≥ 20. For n=21, M ≥ 21.

But can we always achieve M = n? For n=20, we showed yes (a=0, c=20 gives M=20, where all rows are odd and all columns are even — wait, that's different from "all columns odd").

Let me reconsider. With a=0, c=20 for n=20: all rows odd, all columns even. Each row has ≥1, so M ≥ 20. Achieved. ✓

Alternatively, all rows even, all columns odd: a=20, c=0. Each column has ≥1, M ≥ 20. Achieved. ✓

For n=21: a=0, c=20. All rows odd, 20 even columns, 1 odd column. The 1 odd column has all 21 cells occupied (mandatory). M = 21. Each row has exactly 1 checker. ✓

Alternatively, all rows even, all columns odd: a=20, c=0. b=1, d=21. Mandatory: (O_r, O_c) = 1×21 = 21. M = 21. The 1 odd row has all 21 cells occupied. ✓

But could we do better for n=21? What if we have all rows even (a=21)? But a must be even for n=21, and 21 is odd. So a=21 is not even. We can't have all rows even for n=21.

What about all rows odd (a=0) and all columns odd (c=0)? Then all cells are mandatory: 21² = 441. Bad.

What about a=0, c=20 (M=21)? Can we do a=0, c=22? No, c ≤ 21. c=20 is the max even value ≤ 21.

What about a=0, c=18? d=3. Mandatory: bd = 21·3 = 63. Worse.

So for n=21, the minimum is indeed 21.

Hmm, but wait. I should think about whether there's a fundamentally different kind of configuration I'm missing. My analysis assumes that the parities of rows and columns partition the board into four regions, with same-parity regions fully occupied. This is correct because:

In a maximal configuration, for every empty cell (i,j), r_i + c_j is odd, meaning r_i and c_j have different parities. Contrapositive: if r_i and c_j have the same parity, then (i,j) is not empty, i.e., it's occupied.

So yes, all same-parity cells are occupied. The analysis is complete.

Let me also verify with a small case. n=1: 1×1 board. We can place a checker at (1,1) if the remaining 2·1-2 = 0 cells have an even number (0 is even). So we place 1 checker. After that, no more can be placed (board full). f(1) = 1.

Using my formula: n=1 (odd). a even, c even. a ∈ {0}, c ∈ {0}. a=0, c=0: M = 0·0 + 1·1 = 1. ✓

n=2: a even, c even. a ∈ {0,2}, c ∈ {0,2}.
a=0, c=2: M = 0 + 2·0 + 0 + 2 = 2. (All rows odd, all columns even. 2 checkers.)
a=2, c=0: M = 0 + 0 + 2 + 0 = 2.
a=0, c=0: M = 0 + 2·2 = 4.
a=2, c=2: M = 4 + 0 + 0 + 0 = 4.
f(2) = 2. Let me verify: 2×2 board, place checkers at (1,1) and (2,1). Row 1: 1 (odd), Row 2: 1 (odd). Col 1: 2 (even), Col 2: 0 (even). Empty cells: (1,2): r+c = 1+0 = 1 (odd ✓). (2,2): 1+0 = 1 (odd ✓). Maximal with 2 checkers. ✓

n=3: a even, c even. a ∈ {0,2}, c ∈ {0,2}.
a=0, c=2: b=3, d=1. M = 0 + 3·1 + 0 + 0 = 3.
a=2, c=0: b=1, d=3. M = 0 + 1·3 + 0 + 0 = 3.
a=0, c=0: M = 0 + 3·3 = 9.
a=2, c=2: b=1, d=1. M = 4 + 1 + 0 + 0 = 5.
f(3) = 3. Verify: 3×3, all rows odd, 2 even columns, 1 odd column. Odd column has all 3 cells occupied. M=3. Each row has 1 checker (odd ✓). Even columns have 0 (even ✓). Odd column has 3 (odd ✓). Empty cells: (i, even col): r_i + c_j = 1 + 0 = 1 (odd ✓). Maximal. ✓

So the pattern is f(n) = n for all n? Let me check n=4.

n=4: a even, c even. a ∈ {0,2,4}, c ∈ {0,2,4}.
a=0, c=4: M = 0 + 0 + 0 + 4 = 4.
a=0, c=2: b=4, d=2. M = 0 + 8 + 2 + 4 = 14. Wait, let me use the formula: M = 8pq - 42p - 42q + 440? No, that's for n=20. Let me recompute for n=4.

For n=4: M = ac + bd + Min₁ + Min₂.
a=0, c=4: b=4, d=0. M = 0 + 0 + 0 + 4 = 4. (Min₁ = max(0, d) = 0, Min₂ = max(b, 0) = 4.)
a=0, c=2: b=4, d=2. M = 0 + 8 + 2 + 4 = 14.
a=0, c=0: M = 0 + 16 + 4 + 0 = 20. Hmm, Min₁ = max(0, d) = max(0,4) = 4, Min₂ = max(b, 0) = max(4,0) = 4. M = 0 + 16 + 4 + 4 = 24. Wait, let me recompute.

Actually, for n=4, a=0, c=0: all rows odd, all columns odd. Mandatory: (O_r, O_c) = 4×4 = 16. Sub-matrix 1: (E_r, O_c) = (0, 4), empty. Sub-matrix 2: (O_r, E_c) = (4, 0), empty. M = 16. 

Hmm, I think I made an error. Let me recompute using the general formula.

For general n (even), with a=2p, c=2q:
M = 4pq + (n-2p)(n-2q) + (n-2q) + (n-2p) [when p < n/2 and q < n/2]

Wait, I had: M = ac + bd + Min₁ + Min₂ where Min₁ = max(r₁, s₁) and Min₂ = max(r₂, s₂).

For n even, a even, c even:
- r₁ = 0 (c even), s₁ = d (a even → b even → s₁ = d). Min₁ = d = n-c (if d > 0, else 0).
- r₂ = b (c even → d even → r₂ = b), s₂ = 0 (a even). Min₂ = b = n-a (if b > 0, else 0).

M = ac + bd + d + b = ac + (n-a)(n-c) + (n-c) + (n-a)
= ac + n² - n(a+c) + ac + n - c + n - a
= 2ac + n² - n(a+c) + 2n - a - c
= 2ac + n² + 2n - (n+1)(a+c)

For n=4: M = 2ac + 16 + 8 - 5(a+c) = 2ac + 24 - 5(a+c).
a=0, c=4: M = 0 + 24 - 20 = 4. ✓
a=0, c=0: M = 0 + 24 - 0 = 24. But I computed 16 above. Discrepancy!

Let me recheck a=0, c=0 for n=4. a=0, c=0, b=4, d=4.
Mandatory: ac + bd = 0 + 4·4 = 16.
Sub-matrix 1: (E_r, O_c) = (0, 4). Empty (0 rows). Min₁ = 0.
Sub-matrix 2: (O_r, E_c) = (4, 0). Empty (0 columns). Min₂ = 0.
M = 16 + 0 + 0 = 16.

But my formula gives: Min₁ = d = 4, Min₂ = b = 4. That's wrong! When a=0, the sub-matrix (E_r, O_c) has 0 rows, so it's empty and Min₁ = 0, not d.

The issue is that max(r₁, s₁) = max(0, d) = d only works if the sub-matrix is non-empty. If a=0, the sub-matrix has 0 rows, so we can't place any checkers, and the constraint is that all column parities must be 0. But s₁ = d means we need d odd columns, which requires d = 0 (since we can't place any checkers). 

So when a=0, we need s₁ = 0, i.e., d = 0 (for n even, d = n-c, so c = n). OR we need the sub-matrix to not require any checkers, which happens when s₁ = 0.

Wait, I think the issue is more subtle. When a=0 (no even rows), the sub-matrix (E_r, O_c) is empty (0 rows). The column parity constraints for odd columns say: each odd column needs parity ≡ 1+b (mod 2). But if there are no even rows, the optional cells in odd columns (from even rows) don't exist. The column parity is determined entirely by the mandatory cells.

Let me re-examine. For an odd column j (in O_c), the total checkers = b (mandatory in O_r) + (optional in E_r). If a=0, there are no even rows, so optional = 0. Total = b. We need this to be odd. So b must be odd.

For n=4, a=0: b=4 (even). So odd columns would have 4 checkers (even), but we need odd. Contradiction! So a=0, c=0 is actually infeasible for n=4.

Wait, but I said for n even, a even and c even is always feasible. Let me recheck.

For n=4, a=0, c=0: b=4, d=4. 
Sub-matrix 1: (E_r, O_c) = (0, 4). r₁ = 0 (c even), s₁ = d = 4 (a even → b even). Feasibility: 0 ≡ 4 (mod 2)? 0 ≡ 0 ✓. But the sub-matrix has 0 rows! We need s₁ = 4 odd columns, but with 0 rows, we can't place any checkers. So we need s₁ = 0.

Ah, I see the issue. The feasibility condition r₁ ≡ s₁ (mod 2) is necessary but not sufficient when the sub-matrix is degenerate. If the sub-matrix has 0 rows (a=0), then all column sums are 0, so we need all column parities to be 0, i.e., s₁ = 0. Similarly, if 0 columns (d=0), all row sums are 0, need r₁ = 0.

So the actual feasibility conditions are:
- If a = 0: need s₁ = 0 (all column parities in sub-matrix 1 are 0).
- If d = 0: need r₁ = 0.
- If a > 0 and d > 0: need r₁ ≡ s₁ (mod 2) and r₁ ≤ a, s₁ ≤ d (which is automatic since r₁ ∈ {0, a} and s₁ ∈ {0, d}).

Similarly for sub-matrix 2.

Let me redo the analysis more carefully.

For n=4, a=0, c=0: 
Sub-matrix 1: a=0, so need s₁=0. s₁ = d if b even, 0 if b odd. b=4 even, so s₁ = d = 4 ≠ 0. **Infeasible**.

So a=0, c=0 is infeasible for n=4. My earlier analysis was wrong because I didn't account for degenerate sub-matrices.

Let me redo the n=20 and n=21 analyses with this correction.

For n=20 (even), a=2p, c=2q:

Sub-matrix 1 (a × d, d = 20-2q):
- r₁ = 0 (c even), s₁ = d if a even (b even), 0 if a odd. Since a is even, s₁ = d = 20-2q.
- If a = 0 (p=0): need s₁ = 0, i.e., d = 0, i.e., q = 10.
- If a > 0 (p > 0): need r₁ ≡ s₁ (mod 2), i.e., 0 ≡ d (mod 2). d = 20-2q is always even. ✓
- If d = 0 (q=10): need r₁ = 0. r₁ = 0. ✓

Sub-matrix 2 (b × c, b = 20-2p):
- r₂ = b (d even, since c even → d even), s₂ = 0 (a even).
- If b = 0 (p=10): need s₂ = 0. s₂ = 0. ✓ (Also need r₂ = 0, r₂ = b = 0. ✓)
- If c = 0 (q=0): need r₂ = 0. r₂ = b = 20-2p. Need p = 10.
- If b > 0 and c > 0: need r₂ ≡ s₂ (mod 2), i.e., b ≡ 0 (mod 2). b = 20-2p is always even. ✓

So the feasibility conditions for n=20:
- If p = 0: need q = 10 (from sub-matrix 1).
- If q = 0: need p = 10 (from sub-matrix 2).
- If p > 0 and q > 0: always feasible (with p ≤ 10, q ≤ 10).
- If p = 10: sub-matrix 2 is degenerate (b=0), always OK.
- If q = 10: sub-matrix 1 is degenerate (d=0), always OK.

So the feasible (p,q) are:
- p=0, q=10
- p=10, q=0
- p > 0, q > 0 (any p from 1 to 10, q from 1 to 10)
- Also p=10, q=10 (both degenerate, OK)
- p=10, q > 0: b=0, sub-matrix 2 degenerate (OK), sub-matrix 1 non-degenerate if d > 0 (q < 10) → need 0 ≡ d (mod 2), d even ✓. So p=10, q ∈ {1,...,10} feasible.
- p > 0, q=10: d=0, sub-matrix 1 degenerate (OK), sub-matrix 2 non-degenerate if b > 0 (p < 10) → need b ≡ 0 (mod 2), b even ✓. So p ∈ {1,...,10}, q=10 feasible.

So the only infeasible cases are p=0 with q < 10, and q=0 with p < 10.

Now let me compute M for the feasible cases:

M = ac + bd + Min₁ + Min₂.

For p > 0, q > 0 (and p ≤ 10, q ≤ 10), with the degenerate cases handled:

If p > 0 and q < 10 (d > 0): Min₁ = max(0, d) = d = 20-2q.
If q = 10 (d = 0): Min₁ = 0.
If p < 10 and q > 0 (b > 0, c > 0): Min₂ = max(b, 0) = b = 20-2p.
If p = 10 (b = 0): Min₂ = 0.
If q = 0: only feasible if p = 10, then b = 0, Min₂ = 0, and d = 20, Min₁ = max(0, 20) = 20. M = 10·0 + 0·20 + 20 + 0 = 20.

Wait, q=0, p=10: a=20, c=0, b=0, d=20. Mandatory: ac + bd = 0 + 0 = 0. Sub-matrix 1: (20, 20), r₁=0, s₁=20. Min₁ = 20. Sub-matrix 2: (0, 0). Min₂ = 0. M = 0 + 0 + 20 + 0 = 20. ✓

p=0, q=10: a=0, c=20, b=20, d=0. Mandatory: 0 + 0 = 0. Sub-matrix 1: (0, 0). Min₁ = 0. Sub-matrix 2: (20, 20), r₂=20, s₂=0. Min₂ = 20. M = 0 + 0 + 0 + 20 = 20. ✓

So for n=20, the minimum is still 20. Let me check if any other feasible point gives less than 20.

For p > 0, q > 0 (general case):
M = 4pq + (20-2p)(20-2q) + (20-2q) + (20-2p) [when p < 10, q < 10]
= 4pq + 400 - 40p - 40q + 4pq + 40 - 2p - 2q
= 8pq + 440 - 42p - 42q

We need to minimize this over p ∈ {1,...,10}, q ∈ {1,...,10} (and also handle boundary cases p=10 or q=10).

At p=1, q=10: M = 8·10 + 440 - 42 - 420 = 80 + 440 - 462 = 58.
At p=10, q=1: M = 58.
At p=1, q=1: M = 8 + 440 - 42 - 42 = 364.

The function 8pq - 42p - 42q + 440 is minimized at the boundary. Since the coefficient of pq is positive, the minimum is at small p, q. But we also need p ≥ 1, q ≥ 1 (for this formula). The minimum in the interior is at p=q=5.25, which gives a local minimum, not global. The global min on the boundary.

Let me check p=1, q=10: M = 58. p=10, q=1: M = 58. p=1, q=9: M = 72 - 42 - 378 + 440 = 92. 

Hmm, all values with p ≥ 1, q ≥ 1 give M ≥ 58. The minimum of 20 is achieved only at (p=0, q=10) and (p=10, q=0).

So f(20) = 20. ✓

Now for n=21 (odd), a=2p, c=2q, p ∈ {0,...,10}, q ∈ {0,...,10}:

Sub-matrix 1 (a × d, d = 21-2q, d is odd):
- r₁ = 0 (c even), s₁ = 0 (a even → b odd → s₁ = 0).
- If a = 0: need s₁ = 0. s₁ = 0. ✓
- If d = 0: impossible since d = 21-2q is always odd, never 0. Actually d = 21-2q, for q=10, d=1; for q=0, d=21. d is always ≥ 1 and odd.
- Feasibility: r₁ = 0, s₁ = 0. Always feasible. Min₁ = 0.

Sub-matrix 2 (b × c, b = 21-2p, b is odd):
- r₂ = 0 (d odd → r₂ = 0), s₂ = 0 (a even).
- If b = 0: impossible since b = 21-2p is always odd, never 0.
- If c = 0 (q=0): need r₂ = 0. r₂ = 0. ✓
- Feasibility: r₂ = 0, s₂ = 0. Always feasible. Min₂ = 0.

So for n=21, all (p, q) with p ∈ {0,...,10}, q ∈ {0,...,10} are feasible!

M = ac + bd + 0 + 0 = 4pq + (21-2p)(21-2q) = 4pq + 441 - 42p - 42q + 4pq = 8pq - 42p - 42q + 441.

Minimize over p ∈ {0,...,10}, q ∈ {0,...,10}.

∂M/∂p = 8q - 42 = 0 → q = 5.25. ∂M/∂q = 8p - 42 = 0 → p = 5.25.

Since the Hessian is [[0, 8], [8, 0]] with eigenvalues ±8, this is a saddle point, not a minimum. So the minimum is on the boundary.

Boundary values:
- p=0: M = 441 - 42q. Minimized at q=10: M = 441 - 420 = 21.
- q=0: M = 441 - 42p. Minimized at p=10: M = 441 - 420 = 21.
- p=10: M = 80q - 420 - 42q + 441 = 38q + 21. Minimized at q=0: M = 21.
- q=10: M = 80p - 42p - 420 + 441 = 38p + 21. Minimized at p=0: M = 21.

So the minimum is 21, achieved at (p=0, q=10), (p=10, q=0), and along the boundaries.

f(21) = 21. ✓

So f(20) + f(21) = 20 + 21 = 41.

Wait, I should double-check this more carefully. Let me verify the n=21, p=0, q=10 case.

a=0, c=20, b=21, d=1. All rows odd, 20 even columns, 1 odd column.
Mandatory: (E_r, E_c) = 0 (no even rows), (O_r, O_c) = 21 × 1 = 21.
Optional: (E_r, O_c) = 0 × 1 = 0, (O_r, E_c) = 21 × 20 = 420.
Min₁ = 0, Min₂ = 0.
M = 0 + 21 + 0 + 0 = 21.

The configuration: all 21 cells in the single odd column are occupied. Each row has 1 checker (odd ✓). The odd column has 21 checkers (odd ✓). Each even column has 0 (even ✓). 

For any empty cell (i, j) where j is an even column: r_i = 1 (odd), c_j = 0 (even). r_i + c_j = 1 (odd ✓). Can't place. ✓

Maximal with 21 checkers. And 21 is the minimum since each row has at least 1 checker (all rows are odd), so M ≥ 21.

Actually, I realize I should also check: is there a non-even a or c configuration that could work for n=21? I showed earlier that for n=21, both sub-matrices are feasible only when a even and c even. Let me re-examine with the degenerate case correction.

For n=21, a odd, c even:
Sub-matrix 1: r₁ = 0 (c even), s₁ = d (a odd → b even → s₁ = d). 
- If a > 0: need 0 ≡ d (mod 2). d = 21-c, c even, so d is odd. 0 ≢ 1. **Infeasible**.
- If a = 0: but a is odd, so a ≥ 1. Infeasible.

For n=21, a even, c odd:
Sub-matrix 2: r₂ = b (c odd → d even → r₂ = b), s₂ = c (a even → s₂ = 0). Wait, s₂ = c if a odd, 0 if a even. a is even, so s₂ = 0.
- r₂ = b, s₂ = 0. Need b ≡ 0 (mod 2). b = 21-a, a even, so b is odd. odd ≢ 0. **Infeasible** (if b > 0).
- If b = 0: a = 21, but a must be even. 21 is odd. Impossible.

For n=21, a odd, c odd:
Sub-matrix 1: r₁ = a (c odd), s₁ = d (a odd → b even → s₁ = d). Need a ≡ d (mod 2). a odd, d = 21-c, c odd, d even. odd ≢ even. **Infeasible**.

So indeed, for n=21, only a even and c even works. f(21) = 21.

And for n=20, only a even and c even works (I verified this earlier, and the degenerate corrections don't change the feasible set for non-degenerate cases, and the minimum is still 20).

Let me also verify the n=20 case once more with the degenerate correction. For n=20, a odd, c even:
Sub-matrix 1: r₁ = 0 (c even), s₁ = d (a odd → b odd → s₁ = 0). Wait, b = 20-a, a odd → b odd. s₁ = 0 if b odd. So s₁ = 0.
- r₁ = 0, s₁ = 0. Feasible! Min₁ = 0.

Sub-matrix 2: r₂ = b (c even → d even → r₂ = b), s₂ = c (a odd → s₂ = c). Need b ≡ c (mod 2). b = 20-a, a odd, b odd. c even. odd ≢ even. **Infeasible** (if b > 0 and c > 0).
- If b = 0: a = 20, but a is odd. Impossible.
- If c = 0: s₂ = 0, r₂ = b. Need b ≡ 0 (mod 2). b odd. Infeasible.

So a odd, c even is infeasible for n=20 (due to sub-matrix 2). ✓

For n=20, a even, c odd:
Sub-matrix 1: r₁ = a (c odd), s₁ = 0 (a even → b even → b odd? No, b = 20-a, a even → b even. s₁ = d if b even, 0 if b odd. b even → s₁ = d). 
Wait, I need to be more careful. s₁ = d if b even, 0 if b odd. b = 20-a, a even → b even → s₁ = d.
r₁ = a (c odd), s₁ = d. Need a ≡ d (mod 2). a even, d = 20-c, c odd → d odd. even ≢ odd. **Infeasible** (if a > 0 and d > 0).
- If a = 0: r₁ = 0, need s₁ = 0, i.e., d = 0, i.e., c = 20. But c is odd, 20 is even. Impossible.
- If d = 0: c = 20, but c is odd. Impossible.

So a even, c odd is infeasible for n=20. ✓

For n=20, a odd, c odd:
Sub-matrix 1: r₁ = a (c odd), s₁ = 0 (a odd → b odd → s₁ = 0). Need a ≡ 0 (mod 2). a odd. **Infeasible** (if a > 0).
Sub-matrix 2: r₂ = 0 (c odd → d odd → r₂ = 0), s₂ = c (a odd → s₂ = c). Need 0 ≡ c (mod 2). c odd. **Infeasible** (if c > 0).

So a odd, c odd is infeasible. ✓

Great, so for n=20, only a even, c even is feasible, and f(20) = 20.
For n=21, only a even, c even is feasible, and f(21) = 21.

f(20) + f(21) = 41.

Hmm wait, but I want to make sure I haven't made an error. Let me think about this more carefully with a different approach.

Alternative approach: Think about what a maximal configuration looks like.

A configuration is maximal iff for every empty cell (i,j), r_i + c_j is odd.

This means: if r_i is even, then for every empty cell in row i, c_j is odd. If r_i is odd, then for every empty cell in row i, c_j is even.

Consider the rows with r_i = 0 (completely empty rows). For such a row, every cell is empty, so every column must have odd count. If there are k such rows, and all columns are odd, then each column has at least 1 checker, so M ≥ n. But also, the checkers in each column are in the non-empty rows.

Hmm, this is getting complicated. Let me just verify the answer with a slightly larger case.

n=5: a even, c even. a ∈ {0,2,4}, c ∈ {0,2,4}.
M = 4pq + (5-2p)(5-2q) + 0 + 0 = 4pq + 25 - 10p - 10q + 4pq = 8pq - 10p - 10q + 25.

Wait, for n=5 (odd), Min₁ = 0 and Min₂ = 0 always (as I showed for n=21). So M = ac + bd = 4pq + (5-2p)(5-2q).

p=0, q=2: M = 0 + 5·1 = 5. (a=0, c=4, b=5, d=1.)
p=2, q=0: M = 0 + 1·5 = 5. (a=4, c=0, b=1, d=5.)
p=0, q=0: M = 0 + 25 = 25.
p=2, q=2: M = 16 + 1 = 17.

f(5) = 5. Makes sense: place checkers in one column (all 5 cells), each row has 1 (odd), that column has 5 (odd), other columns have 0 (even). Maximal. ✓

n=6: a even, c even. a ∈ {0,2,4,6}, c ∈ {0,2,4,6}.
For non-degenerate cases (p > 0, q > 0, p < 3, q < 3):
M = 4pq + (6-2p)(6-2q) + (6-2q) + (6-2p) = 8pq + 36 + 12 - 6(a+c)/... let me use the formula.

Actually, M = ac + bd + d + b = 2ac + n² + 2n - (n+1)(a+c) for n even.
For n=6: M = 2ac + 36 + 12 - 7(a+c) = 2ac + 48 - 7(a+c).

a=0, c=6: M = 0 + 48 - 42 = 6. (Feasible: p=0, q=3. d=0, sub-matrix 1 degenerate. b=6, sub-matrix 2: r₂=6, s₂=0, Min₂=6. M = 0 + 0 + 0 + 6 = 6. ✓)
a=6, c=0: M = 0 + 48 - 42 = 6.
a=2, c=6: M = 24 + 48 - 56 = 16. (Using general formula: 4·3 + 0 + 0 + 4 = 16. Wait, a=2, c=6, b=4, d=0. Mandatory: 12 + 0 = 12. Sub-matrix 1: (2, 0), degenerate, Min₁=0. Sub-matrix 2: (4, 6), r₂=4, s₂=0, Min₂=4. M = 12 + 0 + 0 + 4 = 16. ✓)

f(6) = 6. ✓

So the pattern f(n) = n holds for all n. This makes intuitive sense: place n checkers in a single column (or row). Each row has 1 checker (odd), that column has n checkers (parity = n mod 2), other columns have 0 (even).

For this to be maximal: for empty cell (i, j) where j ≠ the occupied column: r_i = 1 (odd), c_j = 0 (even). r_i + c_j = 1 (odd). ✓ Can't place.

For the occupied column: all cells are occupied, so no empty cells there.

But wait, we need the occupied column to have the right parity. If n is even, the column has n checkers (even). All rows have 1 (odd). All other columns have 0 (even). For empty cell (i,j), j ≠ occupied column: r_i + c_j = 1 + 0 = 1 (odd ✓). ✓

If n is odd, the column has n checkers (odd). All rows have 1 (odd). All other columns have 0 (even). For empty cell (i,j), j ≠ occupied column: r_i + c_j = 1 + 0 = 1 (odd ✓). ✓

So in both cases, placing n checkers in a single column gives a maximal configuration with M = n. And we showed M ≥ n (since each row has at least 1 checker when all rows are odd, or each column has at least 1 when all columns are odd). 

But wait, is M ≥ n always true? What if some rows have 0 checkers?

If some row has 0 checkers (even), then all columns must be odd (as I argued earlier). If all columns are odd, each has ≥ 1 checker, so M ≥ n. If all rows are odd, each has ≥ 1, so M ≥ n. If some rows are even (but not 0) and some are odd... 

Actually, let me think about this more carefully. In a maximal configuration, can we have M < n?

Suppose M < n. Then the average number of checkers per row is < 1, so some row has 0 checkers. Say row i has r_i = 0. Then for every column j, since cell (i,j) is empty (r_i = 0), we need r_i + c_j odd, so c_j is odd. All columns are odd, so each has ≥ 1 checker, M ≥ n. Contradiction.

So M ≥ n for any maximal configuration. And we showed M = n is achievable. Therefore f(n) = n for all n.

Wait, that's a much simpler argument! Let me make sure it's correct.

Claim: In any maximal configuration, M ≥ n.

Proof: Suppose M < n. Then some row has 0 checkers (by pigeonhole, since M < n checkers in n rows). Say row i is empty. Then every cell (i,j) is empty, and for each such cell, r_i + c_j must be odd. Since r_i = 0 (even), c_j must be odd for all j. So every column has an odd number of checkers, hence ≥ 1. So M = Σc_j ≥ n. Contradiction.

And M = n is achievable (place n checkers in one column). So f(n) = n.

Therefore f(20) + f(21) = 20 + 21 = 41.

That's a clean proof. Let me write it up.

Actually wait, I need to double-check the M = n construction more carefully.

Construction: Place checkers at (1,1), (2,1), ..., (n,1). So all n checkers are in column 1.

Row sums: r_i = 1 for all i (odd).
Column sums: c_1 = n, c_j = 0 for j ≥ 2.

For an empty cell (i,j):
- If j = 1: cell (i,1) is occupied, not empty. Skip.
- If j ≥ 2: r_i + c_j = 1 + 0 = 1 (odd). ✓

So every empty cell has r_i + c_j odd. The configuration is maximal. M = n. ✓

And the lower bound M ≥ n is proven. So f(n) = n, and f(20) + f(21) = 41.

Let me also sanity-check: is the initial placement valid? We need to place checkers one at a time, each time the placement is valid (the cell is empty and the remaining 2n-2 cells have even count).

When we place the first checker at (1,1): row 1 has 0 other checkers, column 1 has 0 other checkers. Total = 0 (even). ✓
When we place the second checker at (2,1): row 2 has 0 other checkers, column 1 has 1 other checker. Total = 1 (odd). ✗!

Oops! The placement at (2,1) is not valid because column 1 already has 1 checker (at (1,1)), and 1 is odd.

So we can't just place all n checkers in one column sequentially! The order matters, and we need to find a valid sequence.

Hmm, this changes things. The problem says Ivan places checkers one at a time, each placement must be valid. The final configuration must be maximal. We want to minimize the number of checkers in a maximal configuration that is reachable by some valid sequence of placements.

So the question is: which maximal configurations are reachable? Not all of them necessarily are.

Let me reconsider. A checker can be placed at cell C if:
1. C is empty.
2. The number of checkers in the other 2n-2 cells of C's row and column is even.

If C = (i,j), the count is (r_i - [C occupied]) + (c_j - [C occupied]) = r_i + c_j (since C is empty, r_i and c_j don't include C). So the condition is r_i + c_j is even.

So at each step, we can place a checker at (i,j) iff (i,j) is empty and r_i + c_j is even.

The final configuration must be maximal: for every empty (i,j), r_i + c_j is odd.

So during the process, we place checkers at cells where r_i + c_j is even, and we stop when all empty cells have r_i + c_j odd.

The question is: what is the minimum M such that there exists a sequence of M valid placements leading to a maximal configuration?

This is different from just finding the minimum maximal configuration! We need the configuration to be reachable.

Let me reconsider. The configuration with all checkers in one column: is it reachable?

Start: all r_i = 0, all c_j = 0. r_i + c_j = 0 (even) for all cells. We can place at any cell.

Place at (1,1): r_1 = 1, c_1 = 1. Now:
- (i, 1) for i ≥ 2: r_i + c_1 = 0 + 1 = 1 (odd). Can't place.
- (1, j) for j ≥ 2: r_1 + c_j = 1 + 0 = 1 (odd). Can't place.
- (i, j) for i ≥ 2, j ≥ 2: r_i + c_j = 0 + 0 = 0 (even). Can place.

So after placing at (1,1), we can only place in the (n-1)×(n-1) sub-board excluding row 1 and column 1.

Place at (2,2): r_2 = 1, c_2 = 1. Now:
- (i, 1) for i ≥ 2: r_i + c_1 = 0 + 1 = 1 (odd). Can't.
- (1, j) for j ≥ 2: r_1 + c_j = 1 + 0 = 1 (odd). Can't.
- (i, 2) for i ≥ 3: r_i + c_2 = 0 + 1 = 1 (odd). Can't.
- (2, j) for j ≥ 3: r_2 + c_j = 1 + 0 = 1 (odd). Can't.
- (i, j) for i ≥ 3, j ≥ 3: r_i + c_j = 0 + 0 = 0 (even). Can place.

So we're forced to place at (3,3), then (4,4), etc. This gives us a diagonal: (1,1), (2,2), ..., (n,n). After placing all n diagonal checkers:
r_i = 1 for all i, c_j = 1 for all j.
For any empty cell (i,j) (i ≠ j): r_i + c_j = 1 + 1 = 2 (even). So we can still place!

So the diagonal is not maximal. We can continue placing.

After the diagonal, we can place at any off-diagonal cell (since r_i + c_j = 2, even). Place at (1,2): r_1 = 2, c_2 = 2. Now:
- (i, 2) for i ≠ 1: r_i + c_2 = 1 + 2 = 3 (odd). Can't place in column 2 (except (1,2) which is occupied).
- (1, j) for j ≠ 2: r_1 + c_j = 2 + 1 = 3 (odd). Can't place in row 1.
- (i, j) for i ≥ 2, j ≥ 3, i ≠ j: r_i + c_j = 1 + 1 = 2 (even). Can place.

So after diagonal + (1,2), we can place in the sub-board excluding rows 1,2 and columns 1,2 (off-diagonal). Place at (3,4): r_3 = 2, c_4 = 2. Etc.

This is getting complicated. Let me think about this differently.

The key insight is that the process is constrained: we can only place at cells where r_i + c_j is even. The final state must have all empty cells with r_i + c_j odd.

Let me think about what final states are reachable.

Observation: At each step, placing a checker at (i,j) changes r_i by +1 and c_j by +1. So r_i + c_j changes by +2 (from even to even, or odd to odd). Wait, the parity of r_i + c_j doesn't change when we place at (i,j)! Because both r_i and c_j increase by 1, so r_i + c_j increases by 2, parity unchanged.

But wait, placing at (i,j) also affects other cells. For cell (i, k) with k ≠ j: r_i increases by 1, c_k unchanged. So r_i + c_k changes parity. For cell (k, j) with k ≠ i: r_k unchanged, c_j increases by 1. So r_k + c_j changes parity.

So placing a checker at (i,j):
- Doesn't change parity of r_i + c_j (the placed cell).
- Flips parity of r_i + c_k for all k ≠ j (same row, different column).
- Flips parity of r_k + c_j for all k ≠ i (same column, different row).
- Doesn't affect r_k + c_l for k ≠ i, l ≠ j.

Interesting. So the parity of r_i + c_j for each cell evolves as we place checkers.

Initially, all r_i + c_j = 0 (even). We can place at any cell.

When we place at (i,j), the parities of cells in row i (except (i,j)) and column j (except (i,j)) flip. The cell (i,j) itself stays even (but becomes occupied, so it doesn't matter).

We want to reach a state where all empty cells have odd parity, and we want to minimize the number of occupied cells.

This is like a lights-out puzzle! We have an n×n grid of parities, all starting even. Each move at (i,j) flips the parities of all cells in row i and column j except (i,j) itself (and (i,j) becomes occupied, removing it from consideration). We want to reach a state where all remaining (empty) cells have odd parity, minimizing the number of moves (occupied cells).

Hmm, this is more complex than I initially thought. Let me reconsider.

Actually, let me think about it in terms of the parity matrix. Let P(i,j) = (r_i + c_j) mod 2. Initially all 0. When we place at (i,j), P(i,k) flips for all k ≠ j, and P(k,j) flips for all k ≠ i. P(i,j) is now irrelevant (cell occupied).

We want: all empty cells have P = 1.

Equivalently, let's track which cells are occupied and the parity matrix. The parity matrix P is determined by the row and column sums: P(i,j) = (r_i + c_j) mod 2.

Let me think about the parity of r_i and c_j. Let R_i = r_i mod 2 and C_j = c_j mod 2. Then P(i,j) = R_i ⊕ C_j.

Initially R_i = 0, C_j = 0 for all i,j. P(i,j) = 0 for all i,j.

When we place at (i,j): R_i flips, C_j flips. So P(i,j) = (R_i ⊕ 1) ⊕ (C_j ⊕ 1) = R_i ⊕ C_j (unchanged). P(i,k) = (R_i ⊕ 1) ⊕ C_k = P(i,k) ⊕ 1 (flips). P(k,j) = R_k ⊕ (C_j ⊕ 1) = P(k,j) ⊕ 1 (flips). P(k,l) = R_k ⊕ C_l (unchanged). ✓

So the state is determined by the vectors R = (R_1, ..., R_n) and C = (C_1, ..., C_n), plus the set of occupied cells. P(i,j) = R_i ⊕ C_j.

The maximal condition: for every empty cell (i,j), R_i ⊕ C_j = 1, i.e., R_i ≠ C_j.

This means: if R_i = C_j, then (i,j) must be occupied. (Same as before.)

The reachability condition: we start with R = 0, C = 0, and at each step, we place at an empty cell (i,j) with R_i ⊕ C_j = 0 (i.e., R_i = C_j), which flips R_i and C_j.

So at each step, we must place at a cell where R_i = C_j, and this flips both R_i and C_j.

We want to reach a state (R, C, occupied set) where:
1. All cells with R_i = C_j are occupied.
2. The number of occupied cells is minimized.

And the state must be reachable from (R=0, C=0, empty) by the above rules.

Let me think about what states (R, C) are reachable. Starting from R=0, C=0, each move flips one R_i and one C_j (where R_i = C_j currently). 

Let's track the number of 1s in R and C. Let a = |{i : R_i = 0}| (even rows), so n-a rows have R_i = 1. Similarly c = |{j : C_j = 0}|.

Initially a = n, c = n (all 0s). 

When we place at (i,j) with R_i = C_j:
- If R_i = C_j = 0: R_i flips to 1, C_j flips to 1. a decreases by 1, c decreases by 1.
- If R_i = C_j = 1: R_i flips to 0, C_j flips to 0. a increases by 1, c increases by 1.

So each move either decreases both a and c by 1, or increases both by 1. Therefore, a - c is invariant! Initially a - c = 0. So a = c always.

This is a key constraint: in any reachable state, the number of even rows equals the number of even columns.

Also, a + c has the same parity as n + n = 2n (always even), and each move changes a + c by ±2, so a + c is always even. Since a = c, this is automatic.

Now, the total number of moves M. Each move changes a by ±1. Starting from a = n, after M moves, a = n + (number of "increase" moves) - (number of "decrease" moves). Let u = increase moves, d = decrease moves. M = u + d, a = n + u - d = n + u - (M - u) = n + 2u - M. So M = n + 2u - a, i.e., M = n - a + 2u.

Since u ≥ 0, M ≥ n - a. Also, a = c, and a ∈ {0, 1, ..., n} with a ≡ n (mod 2)? Let me check: initially a = n. Each move changes a by ±1. So after M moves, a ≡ n - M (mod 2) ... no, a = n + (sum of ±1's), so a ≡ n + M (mod 2) ... actually a ≡ n + (u - d) (mod 2) = n + (2u - M) (mod 2) = n + M (mod 2). So a ≡ n + M (mod 2), i.e., M ≡ a - n (mod 2), i.e., M ≡ a + n (mod 2).

Hmm, let me think about what constraints we have:
1. a = c (from reachability).
2. The occupied cells are exactly: all (i,j) with R_i = C_j, plus possibly some with R_i ≠ C_j (but we want to minimize, so we'd avoid those unless needed for reachability).
3. M ≥ (number of cells with R_i = C_j) = a² + (n-a)² (since a = c, same-parity cells are (even,even) = a² and (odd,odd) = (n-a)²).

Wait, but we also need to account for the optional cells. The minimal maximal configuration for a given (a, c) with a = c has:
Mandatory: a² + (n-a)² cells (since c = a, d = n-a = b).
Optional: we need to satisfy parity constraints.

But now with the reachability constraint a = c, let me redo the analysis.

With a = c, b = n - a, d = n - a = b. So b = d.

Sub-matrix 1 (E_r, O_c) = (a, b):
- r₁ = a if c odd, 0 if c even. c = a, so r₁ = a if a odd, 0 if a even.
- s₁ = b if a even (b even... wait, b = n-a. s₁ = d if b even, 0 if b odd. d = b. s₁ = b if b even, 0 if b odd.

Hmm wait, I need to recompute. s₁ = d if b is even, 0 if b is odd. And d = n - c = n - a = b. So s₁ = b if b even, 0 if b odd.

And r₁ = a if c odd (c = a, so a odd), 0 if a even.

Case 1: a even, b = n-a. 
- r₁ = 0 (a even → c even).
- s₁ = b if b even, 0 if b odd.
- If b even (
