# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   In a $10 \times 10$ chess board, what is the maximum number of knights that can be placed such that each square on the board can be attacked by at most one knight?       — 题目文本
#   To solve the problem of placing the maximum number of knights on a \(10 \times 10\) chessboard such that each square is attacked by at most one knight, we need to ensure that the attack ranges of the knights do not overlap. Here is a detailed, clean solution:

### Problem Restatement
We need to place the maximum number of knights on a \(10 \times 10\) chessboard such that each square on the board can be attacked by at most one knight. Knights move in an L-shape, covering up to 8 squares.

### Key Observations
1. **Knight's Attack Pattern**: Each knight attacks 8 squares in an L-shape.
2. **Overlap Constraint**: No two knights can attack the same square, either directly or through their attack ranges.
3. **Upper Bound Calculation**: If \(N\) is the number of knights, the total number of attacked squares (including the squares occupied by the knights) must not exceed 100. This gives us the inequality \(8N + N \leq 100\), simplifying to \(9N \leq 100\), and thus \(N \leq \frac{100}{9} \approx 11.11\). Therefore, the maximum integer value for \(N\) is 12.

### Arrangement Strategy
To achieve this upper bound of 12 knights, we can use a systematic placement strategy:
1. **Checkerboard Pattern**: Place knights on a checkerboard pattern but ensure that the knights are spaced sufficiently apart to avoid overlapping attack ranges.
2. **Spacing**: Place knights such that they are at least 3 squares apart in both the horizontal and vertical directions. This ensures that their attack ranges do not overlap.

### Example Placement
1. **First Row**: Place knights at positions \((1,1)\), \((1,4)\), \((1,7)\), and \((1,10)\).
2. **Second Row**: Skip the second row.
3. **Third Row**: Place knights at positions \((3,1)\), \((3,4)\), \((3,7)\), and \((3,10)\).
4. **Fourth Row**: Skip the fourth row.
5. **Fifth Row**: Place knights at positions \((5,1)\), \((5,4)\), \((5,7)\), and \((5,10)\).
6. **Sixth Row**: Skip the sixth row.
7. **Seventh Row**: Place knights at positions \((7,1)\), \((7,4)\), \((7,7)\), and \((7,10)\).
8. **Eighth Row**: Skip the eighth row.
9. **Ninth Row**: Place knights at positions \((9,1)\), \((9,4)\), \((9,7)\), and \((9,10)\).

This pattern ensures that each knight is at least 3 squares apart from any other knight, both horizontally and vertically, thus avoiding overlapping attack ranges.

### Verification
- Each knight attacks up to 8 squares, and with the spacing, these attack ranges do not overlap.
- Each square is attacked by at most one knight, satisfying the problem's constraints.

### Conclusion
The maximum number of knights that can be placed on a \(10 \times 10\) chessboard such that each square is attacked by at most one knight is \(\boxed{12}\).  — 标准解答
#   The problem: On a 10×10 chessboard, what is the maximum number of knights that can be placed such that each square on the board can be attacked by at most one knight?

Let me think about this carefully. We need to place knights such that every square (including occupied ones? or just empty ones?) is attacked by at most one knight.

"each square on the board can be attacked by at most one knight" - this means for every square, the number of knights that attack it is ≤ 1.

Note: a knight doesn't attack its own square. So occupied squares count too - they must be attacked by at most one other knight.

This is a classic problem. Let me think about the structure.

A knight on a square attacks up to 8 squares. The constraint is that no two knights share a common attacked square. In other words, the sets of squares attacked by different knights must be pairwise disjoint.

Wait, more precisely: for each square s, the number of knights attacking s is at most 1. So the "attack sets" of the knights (the squares each knight attacks) must be pairwise disjoint.

Actually, if knight A attacks square s and knight B also attacks square s, then s is attacked by 2 knights, violating the constraint. So yes, the attack sets must be pairwise disjoint.

But also, a knight's attack set includes the squares it attacks. If knight A is placed on a square that knight B attacks, and knight B is placed on a square that knight A attacks... that's fine as long as no square is attacked by 2+ knights.

Wait, but the occupied square of knight A - is it "attacked" by knight A? No, a knight doesn't attack its own square. So the square where knight A sits is attacked by other knights only. The constraint applies to that square too: it must be attacked by at most 1 knight.

So the condition is: the attack sets (squares attacked by each knight, not including its own square) are pairwise disjoint.

The total number of attacked squares = sum of |attack set of each knight|. These must all be disjoint, and they're all within the 100 squares of the board. So sum of attack set sizes ≤ 100.

Each knight attacks between 2 (corner) and 8 (center) squares. To maximize the number of knights, we want each knight to attack as few squares as possible, so we should place knights in corners and near edges.

But we also need the attack sets to be disjoint. This is a complex combinatorial optimization.

Let me think about this differently. This is a known competition problem. Let me try to figure out the answer.

Actually, let me think about lower bounds via construction and upper bounds via counting.

Upper bound: If we place k knights, the total number of attacked squares (with multiplicity, but they must be distinct) is at least... well each knight attacks at least 2 squares (corner knights). But we can't place all knights in corners.

Hmm, let me think about this more carefully with the coloring approach.

Consider the standard chessboard coloring (black/white). A knight always attacks squares of the opposite color. So a knight on a white square attacks black squares, and vice versa.

If we only place knights on white squares, then all attacked squares are black squares. The attack sets are subsets of the 50 black squares, and they must be pairwise disjoint. So the sum of attack set sizes ≤ 50.

Similarly if we place on black squares, attacked squares are white, sum ≤ 50.

But we can mix: some knights on white (attacking black squares), some on black (attacking white squares). The constraint is that the attack sets are all pairwise disjoint. Knights on white attack black squares; knights on black attack white squares. So a white-knight's attack set and a black-knight's attack set are automatically disjoint (different colors)! 

So we can independently optimize: place knights on white squares (attacking black squares, disjoint attack sets within the 50 black squares) and place knights on black squares (attacking white squares, disjoint attack sets within the 50 white squares). The total is the sum.

So the problem decomposes into two independent subproblems, one for each color. By symmetry (the board is symmetric under color swap), both give the same answer. So total = 2 × (max knights on one color).

Wait, but I need to be more careful. When we place knights on white squares, the attacked squares are black. But we also need: no black square is attacked by more than one white-knight. And the white squares where knights sit - they're attacked by black-knights (if any), and those must also be ≤ 1. But since we separated by color, white-knights only attack black squares, black-knights only attack white squares. A white square is attacked only by black-knights (at most 1). A black square is attacked only by white-knights (at most 1). So the decomposition is valid.

So we need to solve: on a 10×10 board, place knights on squares of one color (say white) such that no square of the opposite color (black) is attacked by more than one knight. Maximize the number of knights.

The white squares form a specific pattern. Let me think of the board as coordinates (i,j) with 1≤i,j≤10. White squares: i+j even (say). Black squares: i+j odd.

A knight on white square (i,j) attacks black squares (i±1,j±2) and (i±2,j±1) that are on the board.

We need to select a set of white squares such that the attack sets (subsets of black squares) are pairwise disjoint.

This is equivalent to: no two selected white squares attack a common black square. Two white squares (i1,j1) and (i2,j2) attack a common black square iff there exists a black square attacked by both. 

Two knights attack a common square iff they are both a knight's move away from some square. This means the two knights are at distance... if both are a knight's move from square s, then the two knights are at most 2 knight-moves apart. Actually, two squares share a common attacked square iff they are both knight-neighbors of some square, which happens iff they are at "knight distance 2" or they are the same square.

Hmm, this is getting complicated. Let me think about it as a graph problem.

Actually, let me reconsider. The condition "attack sets are pairwise disjoint" means: for any two knights, their attack sets don't intersect. Two knights' attack sets intersect iff there's a square attacked by both, iff the two knights are both a knight's move from some common square.

Let me think about when two squares (a,b) and (c,d) have a common knight-neighbor. A square (x,y) is a knight-neighbor of (a,b) if (x,y) = (a±1,b±2) or (a±2,b±1). Similarly for (c,d). They share a knight-neighbor if some (x,y) is a knight-neighbor of both.

The set of knight-neighbors of (a,b) is N(a,b) = {(a±1,b±2),(a±2,b±1)} ∩ board.

Two squares share a knight-neighbor iff |N(a,b) ∩ N(c,d)| > 0.

This is complex. Let me try a different approach - just try to find the answer computationally in my head, or recall known results.

Actually, this is a well-known problem. Let me think...

For an n×n board, the maximum number of knights such that each square is attacked by at most one knight. 

Let me try small cases and think about the pattern.

For a 1×n board: knights attack nothing (knight moves go off board). So we can place n knights, each attacking 0 squares. All squares attacked by 0 knights. Answer: n.

Hmm wait, on a 1×10 board, a knight can't attack any square (all knight moves go off the 1-row board). So we can place 10 knights, answer 10.

For 2×n: A knight on (1,j) attacks (2,j±2)... wait no. Knight on (1,j): moves are (1±1, j±2) = (2, j±2) and (1±2, j±1) = off board. So attacks (2,j-2) and (2,j+2). Similarly knight on (2,j) attacks (1,j±2).

So on a 2×n board, a knight on row 1, column j attacks row 2, columns j-2 and j+2. 

For the attack sets to be disjoint... this is like a matching problem.

This is getting complicated for general n. Let me focus on 10×10.

Let me try to think about this problem from the competition math perspective. I believe the answer might be 32 or 34 or something like that.

Let me try the decomposition approach more carefully.

We split into two colors. For each color, we have 50 squares of that color, and we want to place knights on them such that the attack sets (on the 50 squares of the opposite color) are disjoint.

Let me think about the structure of white squares and their attacks on black squares.

On a 10×10 board, label squares (r,c) with r,c ∈ {0,...,9}. White = r+c even.

The white squares form a grid-like pattern. Let me think of them in terms of a transformed coordinate system.

Actually, let me think about this problem differently. 

Consider the "knight graph" where we connect two squares if they're a knight's move apart. The condition is that we select a set S of vertices such that no two vertices in S have a common neighbor. This is called a "2-packing" or "open packing" of the graph. Actually, it's specifically that the open neighborhoods are disjoint, which is called an "open packing" or "total 2-packing."

Wait, actually the condition is that the open neighborhoods N(v) for v ∈ S are pairwise disjoint. This is exactly an "open packing" of the graph.

The maximum open packing number of the knight's graph on a 10×10 board... this is a specific combinatorial quantity.

Hmm, let me try to think about constructions.

Construction idea: Place knights on every other square in a pattern. 

Let me think about a 4×4 block. In a 4×4 block, can we place 4 knights (one per color-pair)?

Actually, let me try to think about tiling the 10×10 board with patterns.

Let me try a specific construction. Consider placing knights on squares where both coordinates are ≡ 0 (mod 4) or both ≡ 1 (mod 4)... no, let me think more carefully.

Let me try: place knights on squares (r, c) where r ≡ 0 (mod 2) and c ≡ 0 (mod 2), i.e., both even. On a 10×10 board (0-9), even coordinates are 0,2,4,6,8, so 5×5 = 25 squares. But these are all white squares (even+even=even). 

A knight on (0,0) attacks (1,2),(2,1). A knight on (0,2) attacks (1,0),(1,4),(2,1),(2,3). Wait, (2,1) is attacked by both (0,0) and (0,2)! So this doesn't work.

Let me try a sparser pattern. Place knights on (r,c) where r ≡ 0 (mod 4) and c ≡ 0 (mod 4): (0,0),(0,4),(0,8),(4,0),(4,4),(4,8),(8,0),(8,4),(8,8) = 9 knights. But these are all same color. Their attack sets:

(0,0): (1,2),(2,1)
(0,4): (1,2),(1,6),(2,3),(2,5) - wait, (1,2) is shared with (0,0)!

So (0,0) and (0,4) both attack (1,2). Doesn't work.

The issue is that knights 4 apart in a row can share attacked squares. Let me think about what distance avoids shared attacks.

Two knights on the same row, columns c1 and c2. They share an attacked square if there's a square (r±1, c*) or (r±2, c*) attacked by both. 

Knight at (r,c1) attacks (r±1, c1±2) and (r±2, c1±1).
Knight at (r,c2) attacks (r±1, c2±2) and (r±2, c2±1).

They share a square if:
- (r±1, c1±2) = (r±1, c2±2): c1±2 = c2±2, so |c1-c2| ∈ {0,4}
- (r±1, c1±2) = (r±1, c2∓2): c1+2 = c2-2 or c1-2 = c2+2, so |c1-c2| = 4
- (r±2, c1±1) = (r±2, c2±1): |c1-c2| ∈ {0,2}
- (r±1, c1±2) = (r±2, c2±1): r±1 = r±2, impossible (different rows unless... r+1 = r+2 no, r+1 = r-2 no, r-1 = r+2 no, r-1 = r-2 no). Actually wait, the row offsets: one gives r+1 or r-1, other gives r+2 or r-2. These are never equal. So no overlap here.
- (r±2, c1±1) = (r±1, c2±2): similarly, r±2 vs r±1, never equal. No overlap.

So two knights on the same row share an attacked square iff |c1-c2| ∈ {2, 4}.

So on the same row, knights must be at column distance not in {2,4}. They can be at distance 1,3,5,6,7,... But wait, they also need to be on the same color (if we're doing the color decomposition). Same row, same color means column difference is even. So allowed even distances: 6, 8, ... On a 10-wide board, distance 6 or 8.

Hmm, that's very restrictive. On a single row of 10 squares, same color, we can place knights at columns that are pairwise at distance ≥ 6 (and even). So like columns 0 and 6, or 0 and 8, or 2 and 8. At most 2 per row.

But we also need to consider knights on different rows. Let me think about two knights on different rows.

Knight at (r1,c1) and (r2,c2), both white (r1+c1 even, r2+c2 even).

They share an attacked square if some square is attacked by both. 

The attacked squares of (r1,c1) are at rows r1±1, r1±2 and the attacked squares of (r2,c2) are at rows r2±1, r2±2. For overlap, we need some row that's in {r1±1, r1±2} ∩ {r2±1, r2±2}.

Possible row overlaps:
- r1+1 = r2+1 → r1=r2 (same row, handled above)
- r1+1 = r2-1 → r2 = r1+2
- r1+1 = r2+2 → r2 = r1-1
- r1+1 = r2-2 → r2 = r1+3
- r1-1 = r2+1 → r2 = r1-2
- r1-1 = r2-1 → r1=r2
- r1-1 = r2+2 → r2 = r1-3
- r1-1 = r2-2 → r2 = r1+1
- r1+2 = r2+1 → r2 = r1+1
- r1+2 = r2-1 → r2 = r1+3
- r1+2 = r2+2 → r1=r2
- r1+2 = r2-2 → r2 = r1+4
- r1-2 = r2+1 → r2 = r1-3
- r1-2 = r2-1 → r2 = r1-1
- r1-2 = r2+2 → r2 = r1-4
- r1-2 = r2-2 → r1=r2

So |r1-r2| ∈ {0, 1, 2, 3, 4} could potentially cause overlap. But we also need the column to match. Let me be more systematic.

For |r1-r2| = 1: Say r2 = r1+1. The overlapping row could be r1+1 (= r2) or r1+2 (= r2+1) wait no. Let me redo.

If r2 = r1+1:
- r1+1 = r2: attacked by knight 1 at row r1+1 (columns c1±2), attacked by knight 2 at row r2 = r1+1 (columns c2±1, since r2-1 = r1, so row r1+1 = r2 is attacked by knight 2 via the r2-1... no wait.

Let me be more careful. Knight at (r2, c2) attacks rows r2-2, r2-1, r2+1, r2+2 (those that are on the board). At row r2-1, it attacks columns c2±2. At row r2-2, it attacks columns c2±1. At row r2+1, columns c2±2. At row r2+2, columns c2±1.

Knight at (r1, c1) attacks: row r1-1: c1±2; row r1-2: c1±1; row r1+1: c1±2; row r1+2: c1±1.

If r2 = r1+1:
Overlapping rows: 
- r1+1 = r2: knight 1 attacks (r1+1, c1±2), knight 2 attacks (r2, c2±2) = (r1+1, c2±2). Overlap if c1±2 = c2±2, i.e., |c1-c2| ∈ {0,4}.
- r1+2 = r2+1: knight 1 attacks (r1+2, c1±1), knight 2 attacks (r2+1, c2±2) = (r1+2, c2±2). Overlap if c1±1 = c2±2, i.e., |c1-c2| ∈ {1,3}.
- r1-1 = r2-2: knight 1 attacks (r1-1, c1±2), knight 2 attacks (r2-2, c2±1) = (r1-1, c2±1). Overlap if c1±2 = c2±1, i.e., |c1-c2| ∈ {1,3}.

But both knights are white, so c1 and c2 have the same parity as needed for white: r1+c1 even, r2+c2 = r1+1+c2 even, so c2 is odd if c1 is even, and vice versa. So c1 and c2 have different parities, meaning |c1-c2| is odd. So |c1-c2| ∈ {1,3} is possible, |c1-c2| ∈ {0,4} is not.

So for r2 = r1+1 (adjacent rows, both white knights), they share an attacked square iff |c1-c2| ∈ {1,3}.

For r2 = r1+2:
Overlapping rows:
- r1+1 = r2-1: knight 1 attacks (r1+1, c1±2), knight 2 attacks (r2-1, c2±2) = (r1+1, c2±2). Overlap if |c1-c2| ∈ {0,4}.
- r1+2 = r2: knight 1 attacks (r1+2, c1±1), knight 2 attacks (r2, c2±1) = (r1+2, c2±1). Overlap if |c1-c2| ∈ {0,2}.
- r1-1 = r2-3: no (r2-3 not in {r2±1,r2±2}).
- r1-2 = r2-4: no.

Both white: r1+c1 even, r2+c2 = r1+2+c2 even, so c1, c2 same parity. |c1-c2| even. So |c1-c2| ∈ {0,2,4}. All of {0,2,4} cause overlap. So any two white knights in rows differing by 2 always share an attacked square (as long as they're close enough in columns, which on a 10-wide board they might not be... well |c1-c2| ∈ {0,2,4} - but if they're far apart, like c1=0, c2=8, then |c1-c2|=8, not in {0,2,4}, so no overlap).

Wait, I need to be more careful. The overlap condition is |c1-c2| ∈ {0,2,4} AND the specific attacked squares are on the board. But the column condition is necessary. So for rows differing by 2, overlap iff |c1-c2| ∈ {0,2,4}.

For r2 = r1+3:
Overlapping rows:
- r1+1 = r2-2: knight 1 attacks (r1+1, c1±2), knight 2 attacks (r2-2, c2±1) = (r1+1, c2±1). Overlap if c1±2 = c2±1, |c1-c2| ∈ {1,3}.
- r1+2 = r2-1: knight 1 attacks (r1+2, c1±1), knight 2 attacks (r2-1, c2±2) = (r1+2, c2±2). Overlap if |c1-c2| ∈ {1,3}.
- r1-2 = r2-5: no.

Both white: r1+c1 even, r2+c2 = r1+3+c2 even, so c1, c2 different parity. |c1-c2| odd. So |c1-c2| ∈ {1,3} possible. Overlap iff |c1-c2| ∈ {1,3}.

For r2 = r1+4:
Overlapping rows:
- r1+2 = r2-2: knight 1 attacks (r1+2, c1±1), knight 2 attacks (r2-2, c2±1) = (r1+2, c2±1). Overlap if |c1-c2| ∈ {0,2}.

Both white: r1+c1 even, r2+c2 = r1+4+c2 even, c1,c2 same parity. |c1-c2| even. Overlap iff |c1-c2| ∈ {0,2}.

For |r1-r2| ≥ 5: No overlapping rows (since knight attacks reach at most 2 rows away, so rows r1-2 to r1+2 and r2-2 to r2+2; if |r1-r2|≥5, these don't overlap). So no shared attacks.

Summary for two white knights:
- Same row (|Δr|=0): overlap iff |Δc| ∈ {2,4}
- |Δr|=1: overlap iff |Δc| ∈ {1,3}
- |Δr|=2: overlap iff |Δc| ∈ {0,2,4}
- |Δr|=3: overlap iff |Δc| ∈ {1,3}
- |Δr|=4: overlap iff |Δc| ∈ {0,2}
- |Δr|≥5: no overlap

And for white knights, Δr and Δc have the same parity (since both are white: r+c even for both, so Δr+Δc even, meaning Δr and Δc have same parity).

So:
- |Δr|=0 (even): |Δc| even. Overlap iff |Δc|∈{2,4}. Safe if |Δc|∈{0,...} wait |Δc|=0 means same square. So |Δc|≥6 or |Δc|=0 (same square, not applicable). Safe: |Δc|∈{6,8,...} ∪ {|Δc| not in {2,4}}. Actually |Δc| even and not in {2,4}: |Δc| ∈ {0, 6, 8}. But 0 is same square. So |Δc| ≥ 6.
- |Δr|=1 (odd): |Δc| odd. Overlap iff |Δc|∈{1,3}. Safe: |Δc|∈{5,7,9,...}.
- |Δr|=2 (even): |Δc| even. Overlap iff |Δc|∈{0,2,4}. Safe: |Δc|≥6.
- |Δr|=3 (odd): |Δc| odd. Overlap iff |Δc|∈{1,3}. Safe: |Δc|≥5.
- |Δr|=4 (even): |Δc| even. Overlap iff |Δc|∈{0,2}. Safe: |Δc|∈{4,6,8,...}. Wait, |Δc|=4 is safe for |Δr|=4? Let me check: overlap iff |Δc|∈{0,2}. So |Δc|=4 is safe. |Δc|∈{4,6,8}.
- |Δr|≥5: always safe.

So the "conflict" conditions are quite restrictive. Two white knights conflict (share an attacked square) when they're close together. Specifically:

Let me restate: two white knights at (r1,c1) and (r2,c2) conflict iff:
- |Δr|=0 and |Δc|∈{2,4}
- |Δr|=1 and |Δc|∈{1,3}
- |Δr|=2 and |Δc|∈{0,2,4}
- |Δr|=3 and |Δc|∈{1,3}
- |Δr|=4 and |Δc|∈{0,2}

And no conflict if |Δr|≥5 or if the pair doesn't match any above.

Now I need to find the maximum independent set in this "conflict graph" on the 50 white squares. This is a complex optimization.

Let me think about it differently. The conflict conditions essentially say that knights can't be too close. Let me think about what patterns work.

Consider placing knights with a spacing of 5 in both directions. Like (r,c) where r ≡ 0 (mod 5) and c ≡ 0 (mod 5), but only white squares.

r ∈ {0,5}, c ∈ {0,5}: (0,0),(0,5),(5,0),(5,5). Check: (0,0) and (0,5): |Δr|=0,|Δc|=5. Not in {2,4}. Safe. (0,0) and (5,0): |Δr|=5. Safe. (0,0) and (5,5): |Δr|=5. Safe. All safe. But this only gives 4 knights on white squares (and 4 on black, total 8). Way too few.

We can do much better. Let me think about denser packings.

Key insight: |Δr|≥5 is always safe. So knights in rows that are 5+ apart never conflict. We can handle rows 0-4 and rows 5-9 independently (almost - need to check |Δr|=4 between row 4 and rows in 0-3, and between rows 5-9, and |Δr| could be 4 between row 0 and row 4, row 5 and row 9, etc.)

Actually, let me think about this more carefully. Rows 0-4 and rows 5-9: the minimum |Δr| between a row in {0,1,2,3,4} and a row in {5,6,7,8,9} is |4-5|=1. So they're not independent. Hmm.

Let me try a different approach. Let me think about what the maximum could be and try constructions.

Upper bound approach: Each knight attacks some number of squares. The attack sets are disjoint and contained in 50 squares (of the opposite color). So sum of attack set sizes ≤ 50.

If we place k white knights, sum of their attack set sizes ≤ 50. Each knight attacks at least 2 squares (corner) and at most 8 (center). To maximize k, minimize average attack set size.

But the attack set sizes depend on position. Corner white squares: (0,0),(0,8)... wait, on a 10×10 board (0-9), white corners are (0,0),(0,8)?? No. (0,0): 0+0=0, even, white. (0,9): 0+9=9, odd, black. (9,0): 9, odd, black. (9,9): 18, even, white. So white corners: (0,0) and (9,9). And black corners: (0,9) and (9,0).

(0,0) attacks (1,2),(2,1) = 2 squares.
(9,9) attacks (8,7),(7,8) = 2 squares.

Edge white squares (not corner): e.g., (0,2) attacks (1,0),(1,4),(2,1),(2,3) = 4 squares. (0,4): (1,2),(1,6),(2,3),(2,5) = 4. (0,6): (1,4),(1,8),(2,5),(2,7) = 4. (0,8): (1,6),(2,7),(2,9)... wait (0,8): attacks (0±1,8±2)=(1,6),(1,10)off,(−1,6)off; (0±2,8±1)=(2,7),(2,9). So (1,6),(2,7),(2,9) = 3 squares. Hmm, (0,8) is not a corner but near corner. Let me recount: (0,8): (1,6),(1,10)✗,(2,7),(2,9),(-1,6)✗,(-1,10)✗,(-2,7)✗,(-2,9)✗. So attacks (1,6),(2,7),(2,9) = 3 squares.

This is getting complicated. Let me try to think about the problem from a higher level.

I recall that for this type of problem on an n×n board, the answer is often around n²/3 or similar. For 10×10, that would be around 33.

Let me try to think about a good construction.

Construction attempt: Place knights on a "grid" with spacing 3.

Consider white squares (r,c) with r+c even. Place knights where r ≡ 0 (mod 3) and c ≡ 0 (mod 3), but only if r+c even.

r ∈ {0,3,6,9}, c ∈ {0,3,6,9}. White ones (r+c even): (0,0),(0,6),(3,3),(3,9),(6,0),(6,6),(9,3),(9,9). That's 8.

Check conflicts:
(0,0) vs (0,6): |Δr|=0,|Δc|=6. Safe (need |Δc|∉{2,4}, 6∉{2,4} ✓).
(0,0) vs (3,3): |Δr|=3,|Δc|=3. Conflict! (|Δr|=3,|Δc|∈{1,3} → 3∈{1,3} ✓ conflict).

So this doesn't work. The spacing of 3 causes conflicts.

Let me try spacing 4. r ≡ 0 (mod 4), c ≡ 0 (mod 4), white only.
r ∈ {0,4,8}, c ∈ {0,4,8}. White: (0,0),(0,8),(4,4),(8,0),(8,8). 5 knights.

(0,0) vs (4,4): |Δr|=4,|Δc|=4. Conflict? |Δr|=4, overlap iff |Δc|∈{0,2}. 4∉{0,2}. Safe!
(0,0) vs (0,8): |Δr|=0,|Δc|=8. Safe.
(0,0) vs (8,0): |Δr|=8. Safe.
(0,0) vs (8,8): |Δr|=8. Safe.
(0,8) vs (4,4): |Δr|=4,|Δc|=4. Safe.
(0,8) vs (8,0): |Δr|=8. Safe.
(0,8) vs (8,8): |Δr|=8. Safe.
(4,4) vs (8,0): |Δr|=4,|Δc|=4. Safe.
(4,4) vs (8,8): |Δr|=4,|Δc|=4. Safe.
(8,0) vs (8,8): |Δr|=0,|Δc|=8. Safe.

All safe! 5 white knights. But we can likely do much better.

The issue is that this grid is too sparse. Let me think about denser arrangements.

Let me try to think row by row. In each row, white squares are at specific columns. For row r, white columns are those c with r+c even.

Row 0: c ∈ {0,2,4,6,8} (5 white squares)
Row 1: c ∈ {1,3,5,7,9} (5 white squares)
Row 2: c ∈ {0,2,4,6,8}
Row 3: c ∈ {1,3,5,7,9}
Row 4: c ∈ {0,2,4,6,8}
Row 5: c ∈ {1,3,5,7,9}
Row 6: c ∈ {0,2,4,6,8}
Row 7: c ∈ {1,3,5,7,9}
Row 8: c ∈ {0,2,4,6,8}
Row 9: c ∈ {1,3,5,7,9}

Within a single row, two white knights conflict iff |Δc|∈{2,4}. So in row 0 (columns 0,2,4,6,8), we can't have two knights at distance 2 or 4. The allowed distances are 6, 8. So we can place at most 2 knights in a row (e.g., at columns 0 and 8, or 0 and 6).

Actually, columns 0,2,4,6,8: pairs with |Δc|∈{2,4}: (0,2),(0,4),(2,4),(2,6),(4,6),(4,8),(6,8) all conflict. Pairs with |Δc|=6: (0,6),(2,8) - safe. Pairs with |Δc|=8: (0,8) - safe.

So in one row, we can pick at most 2 columns from {0,2,4,6,8} such that no pair has |Δc|∈{2,4}. E.g., {0,6}: |Δc|=6 ✓. {0,8}: |Δc|=8 ✓. {2,8}: |Δc|=6 ✓. Can we pick 3? {0,6,...}: 6 and any other even col in {0,2,4,6,8}: 6 vs 0 ✓, 6 vs 2 (|Δc|=4 ✗), 6 vs 4 (|Δc|=2 ✗), 6 vs 8 (|Δc|=2 ✗). So {0,6} can't be extended. {0,8}: 8 vs 2 (|Δc|=6 ✓), 8 vs 4 (|Δc|=4 ✗), 8 vs 6 (|Δc|=2 ✗). So {0,2,8}: check 0 vs 2 (|Δc|=2 ✗). No. {0,8} can add 2? 0 vs 2 = 2 ✗. Can't. So max 2 per row.

Wait, what about {2,8}? 2 vs 8 = 6 ✓. Can we add another? 0 vs 2 = 2 ✗, 0 vs 8 = 8 ✓ but 0 vs 2 fails. 4 vs 2 = 2 ✗. 6 vs 2 = 4 ✗, 6 vs 8 = 2 ✗. So no. Max 2 per row.

So within a single row, max 2 white knights. With 10 rows, that's at most 20. But cross-row conflicts reduce this.

Now, between adjacent rows (|Δr|=1), conflict iff |Δc|∈{1,3}. Since adjacent rows have white squares on opposite parity columns (row 0: even cols, row 1: odd cols), |Δc| is always odd. So conflict iff |Δc|∈{1,3}.

Row 0 has knights at even columns, row 1 at odd columns. If row 0 has knight at col 0 and row 1 has knight at col 1: |Δc|=1, conflict. At col 3: |Δc|=3, conflict. At col 5: |Δc|=5, safe. At col 7: |Δc|=7, safe. At col 9: |Δc|=9, safe.

So if row 0 has a knight at col 0, row 1 can have knights at cols {5,7,9} (from odd cols {1,3,5,7,9}, excluding 1,3). But within row 1, we also need |Δc|∉{2,4} among the chosen. {5,7,9}: 5 vs 7 = 2 ✗, 5 vs 9 = 4 ✗, 7 vs 9 = 2 ✗. So at most 1 from {5,7,9} in row 1 if row 0 has a knight at col 0.

Hmm, this is getting very complex. Let me try to think about it as an optimization problem and try to find good constructions.

Let me try a pattern where I place knights in a "staggered" fashion.

Pattern attempt 1: Place knights at (r, c) where c = 2r mod 10 (or something like that)... this is hard to reason about.

Let me try a different approach. Let me think about the problem as placing knights on a coarser grid.

Consider the transformation: map white square (r,c) to (⌊r/2⌋, ⌊c/2⌋) or something. Actually, let me think about the white squares as a 5×10 "half-grid."

Hmm, actually, the white squares can be thought of as follows: in even rows (0,2,4,6,8), white squares are at even columns (0,2,4,6,8), and in odd rows (1,3,5,7,9), white squares are at odd columns (1,3,5,7,9).

Let me use a coordinate transform. For even row r=2i (i=0,...,4), white columns are 2j (j=0,...,4). For odd row r=2i+1 (i=0,...,4), white columns are 2j+1 (j=0,...,4).

So white squares are parametrized by (i,j) where:
- Even rows: (2i, 2j), i,j ∈ {0,1,2,3,4}
- Odd rows: (2i+1, 2j+1), i,j ∈ {0,1,2,3,4}

This gives 25 + 25 = 50 white squares. Good.

Now let me re-express the conflict conditions in terms of these coordinates.

Two white squares, one at (r1,c1) and one at (r2,c2).

Case 1: Both in even rows. r1=2i1, r2=2i2, c1=2j1, c2=2j2.
Δr = 2|i1-i2|, Δc = 2|j1-j2|.
- |Δr|=0 (i1=i2): conflict iff |Δc|∈{2,4} iff 2|j1-j2|∈{2,4} iff |j1-j2|∈{1,2}.
- |Δr|=2 (|i1-i2|=1): conflict iff |Δc|∈{0,2,4} iff |j1-j2|∈{0,1,2}.
- |Δr|=4 (|i1-i2|=2): conflict iff |Δc|∈{0,2} iff |j1-j2|∈{0,1}.
- |Δr|≥6 (|i1-i2|≥3): safe.

Case 2: Both in odd rows. r1=2i1+1, r2=2i2+1, c1=2j1+1, c2=2j2+1.
Same as case 1 (differences are the same). So:
- |i1-i2|=0: conflict iff |j1-j2|∈{1,2}.
- |i1-i2|=1: conflict iff |j1-j2|∈{0,1,2}.
- |i1-i2|=2: conflict iff |j1-j2|∈{0,1}.
- |i1-i2|≥3: safe.

Case 3: One even, one odd. r1=2i1, c1=2j1; r2=2i2+1, c2=2j2+1.
Δr = |2i1 - 2i2 - 1| = |2(i1-i2) - 1|, which is odd.
Δc = |2j1 - 2j2 - 1|, which is odd.

- |Δr|=1: |2(i1-i2)-1|=1, so i1=i2 or i1=i2+1. If i1=i2: Δr=1. If i1=i2+1: Δr=1. Conflict iff |Δc|∈{1,3}. |Δc|=|2(j1-j2)-1|. If j1=j2: |Δc|=1. If j1=j2±1: |Δc|=1 or 3. Specifically: j1=j2 → 1; j1=j2+1 → |2-1|=1; j1=j2-1 → |-2-1|=3; j1=j2+2 → |4-1|=3; j1=j2-2 → |-4-1|=5. So |Δc|∈{1,3} iff |j1-j2|∈{0,1,2}.
  - i1=i2: conflict iff |j1-j2|∈{0,1,2}.
  - i1=i2+1 (i.e., i1-i2=1): Δr=|2-1|=1. Same: conflict iff |j1-j2|∈{0,1,2}.
  
  Wait, I need to be more careful. Δr=1 when |2(i1-i2)-1|=1, which gives 2(i1-i2)-1=±1, so i1-i2=0 or i1-i2=1.

- |Δr|=3: |2(i1-i2)-1|=3, so 2(i1-i2)-1=±3, i1-i2=2 or i1-i2=-1. Conflict iff |Δc|∈{1,3}. Same analysis: |j1-j2|∈{0,1,2}.

- |Δr|=5: |2(i1-i2)-1|=5, i1-i2=3 or i1-i2=-2. |Δr|≥5, safe.

So for even-odd pairs:
- |i1-i2|∈{0,1} (Δr=1): conflict iff |j1-j2|∈{0,1,2}.
- |i1-i2|∈{-1,2} (Δr=3): conflict iff |j1-j2|∈{0,1,2}.

Wait, let me redo. i1-i2=0 → Δr=1. i1-i2=1 → Δr=1. i1-i2=-1 → Δr=3. i1-i2=2 → Δr=3. i1-i2=-2 → Δr=5. i1-i2=3 → Δr=5.

So:
- |i1-i2|∈{0,1}: Δr=1, conflict iff |j1-j2|∈{0,1,2}.
- |i1-i2|∈{1,2} but with i1-i2=-1 or 2: Δr=3, conflict iff |j1-j2|∈{0,1,2}.

Hmm wait, |i1-i2|=1 could be i1-i2=1 (Δr=1) or i1-i2=-1 (Δr=3). Both give conflict iff |j1-j2|∈{0,1,2}.

|i1-i2|=0: Δr=1, conflict iff |j1-j2|∈{0,1,2}.
|i1-i2|=1: Δr∈{1,3}, conflict iff |j1-j2|∈{0,1,2}.
|i1-i2|=2: Δr∈{3,5}. If i1-i2=2: Δr=3, conflict iff |j1-j2|∈{0,1,2}. If i1-i2=-2: Δr=5, safe.
|i1-i2|=3: Δr∈{5,7}. Safe.
|i1-i2|=4: Δr∈{7,9}. Safe.

So for even-odd pairs, conflict iff |i1-i2|∈{0,1,2} (with the caveat that |i1-i2|=2 only conflicts in one direction, but since we consider absolute differences, let me re-examine).

Actually, since i1 is from the even-row set and i2 from the odd-row set, and both range over {0,1,2,3,4}:

If i1-i2 = 2: Δr = |2·2-1| = 3. Conflict iff |j1-j2|∈{0,1,2}.
If i1-i2 = -2: Δr = |2·(-2)-1| = 5. Safe.

So it's not symmetric in i1-i2! The even-row index and odd-row index play asymmetric roles.

Let me restate: for an even-row white square at (2i1, 2j1) and an odd-row white square at (2i2+1, 2j2+1):
- Δr = |2i1 - (2i2+1)| = |2(i1-i2) - 1|
- Δc = |2j1 - (2j2+1)| = |2(j1-j2) - 1|

Conflict conditions:
- Δr=1 (i1-i2 ∈ {0,1}): conflict iff Δc∈{1,3} iff (j1-j2) ∈ {0,1,2,-1,-2}... 

Actually Δc = |2(j1-j2)-1|. For j1-j2=0: Δc=1. j1-j2=1: Δc=1. j1-j2=-1: Δc=3. j1-j2=2: Δc=3. j1-j2=-2: Δc=5. j1-j2=3: Δc=5. j1-j2=-3: Δc=7. j1-j2=4: Δc=7. j1-j2=-4: Δc=9.

So Δc∈{1,3} iff j1-j2 ∈ {-2,-1,0,1,2}, i.e., |j1-j2|∈{0,1,2}.

And Δr=1 iff i1-i2∈{0,1}. Δr=3 iff i1-i2∈{-1,2}. Δr=5 iff i1-i2∈{-2,3}. Δr=7 iff i1-i2∈{-3,4}. Δr=9 iff i1-i2∈{-4}.

Conflict (Δr∈{1,3} and Δc∈{1,3}): 
- i1-i2∈{0,1,-1,2} and |j1-j2|∈{0,1,2}.

No conflict if i1-i2∈{-2,3,-3,4,-4} (i.e., |i1-i2|≥2 with i1>i2+1 or i1<i2-1... this is getting messy).

Let me simplify. The even-row knight at (2i1, 2j1) and odd-row knight at (2i2+1, 2j2+1) conflict iff:
- i1-i2 ∈ {0, 1, -1, 2} AND |j1-j2| ∈ {0, 1, 2}

Equivalently, |i1-i2| ≤ 2 (with the specific constraint that i1-i2 ∈ {-1,0,1,2}) AND |j1-j2| ≤ 2.

Note that i1-i2 ∈ {-1,0,1,2} means i1 ∈ [i2-1, i2+2]. Since both range over {0,...,4}, this is almost always satisfied unless they're far apart.

For i1-i2 = -2 (i.e., i1 = i2-2): no conflict (Δr=5).
For i1-i2 = 3 (i.e., i1 = i2+3): no conflict (Δr=5).

So the even-row and odd-row knights conflict iff i1 ∈ [i2-1, i2+2] and |j1-j2| ≤ 2. They're safe if i1 ≤ i2-3 or i1 ≥ i2+3, or if |j1-j2| ≥ 3.

OK this is very complex. Let me try to just find a good construction and then prove an upper bound.

Let me try to think about this problem from the perspective of known results. I believe this is a competition problem, possibly from a Chinese math competition or similar.

Let me try to construct a solution with 32 knights (16 per color).

Actually, let me try a cleaner approach. Let me think about the problem on the full 10×10 board without the color decomposition, and try to find patterns.

Pattern: Place knights on a 4×4 sub-grid pattern. Divide the 10×10 board into blocks and place knights strategically.

Actually, let me try the following construction. Place knights at positions (r, c) where:
- r ≡ 0 (mod 5) and c is even, or
- r ≡ 2 (mod 5) and c is odd, or
- r ≡ 4 (mod 5) and c is even

Wait, I need to be more systematic. Let me try to think about what the answer is.

Let me try to get an upper bound first.

Upper bound via counting: We showed the problem decomposes into two colors. For one color (50 squares), we place knights such that attack sets (on the other 50 squares) are disjoint. Sum of attack set sizes ≤ 50.

Now, what's the minimum attack set size for a knight on a white square? Corner white squares (0,0) and (9,9) have 2 attacks. But there are only 2 such squares per color.

Let me count the attack set sizes for all white squares:
- (0,0): 2 attacks
- (0,8): Let me compute. (0,8) attacks (1,6),(2,7),(2,9). That's 3.
  Wait, (0,8): (0+1,8+2)=(1,10)✗, (0+1,8-2)=(1,6)✓, (0-1,...)✗, (0+2,8+1)=(2,9)✓, (0+2,8-1)=(2,7)✓, (0-2,...)✗. So 3 attacks.
- (9,9): 2 attacks (by symmetry with (0,0))
- (9,1): by symmetry with (0,8)→ hmm, let me think. (9,1): (9-1,1+2)=(8,3)✓, (9-1,1-2)=(8,-1)✗, (9+1,...)✗, (9-2,1+1)=(7,2)✓, (9-2,1-1)=(7,0)✓. So 3 attacks.

Let me categorize white squares by attack set size:

The attack set size of a knight at (r,c) depends on how many of its 8 potential moves stay on the board.

For a 10×10 board (0-9):
- Corners (0,0),(0,9),(9,0),(9,9): 2 moves. White corners: (0,0),(9,9).
- Near-corners: squares adjacent to corner along edge. (0,1),(1,0) have 3 moves; (0,8),(8,0),(1,9),(9,8) have 3 moves. White ones: (0,8) has 3, (8,0) has 3, (1,9)... 1+9=10 even, white, 3 moves. (9,8): 9+8=17 odd, black.

This is getting tedious. Let me just count by position type.

For a square at (r,c) on a 10×10 board, the number of valid knight moves is:
- From row r: can reach r±1 if 0≤r±1≤9, r±2 if 0≤r±2≤9.
- From col c: similarly.

The number of valid moves = (number of valid row offsets among {±1,±2}) × ... no, it's more nuanced. Each knight move is (±1,±2) or (±2,±1). A move (dr,dc) is valid if 0≤r+dr≤9 and 0≤c+dc≤9.

Let me define:
- r1+ = (r+1≤9), r1- = (r-1≥0), r2+ = (r+2≤9), r2- = (r-2≥0)
- c1+ = (c+1≤9), c1- = (c-1≥0), c2+ = (c+2≤9), c2- = (c-2≥0)

Number of moves = (r1+∧c2+) + (r1+∧c2-) + (r1-∧c2+) + (r1-∧c2-) + (r2+∧c1+) + (r2+∧c1-) + (r2-∧c1+) + (r2-∧c1-)

= (r1+)(c2+ + c2-) + (r1-)(c2+ + c2-) + (r2+)(c1+ + c1-) + (r2-)(c1+ + c1-)

where I'm using boolean arithmetic.

Let me define R1 = (r1+) + (r1-) = number of valid ±1 row moves (0,1,or 2)
R2 = (r2+) + (r2-) = number of valid ±2 row moves
C1 = (c1+) + (c1-) = number of valid ±1 col moves
C2 = (c2+) + (c2-) = number of valid ±2 col moves

Then number of moves = R1·C2 + R2·C1.

For a 10×10 board (0-9):
- r=0: R1=1 (only +1), R2=1 (only +2)
- r=1: R1=2, R2=1 (only +2, since 1-2=-1)
- r=2,...,7: R1=2, R2=2
- r=8: R1=2, R2=1 (only -2, since 8+2=10)
- r=9: R1=1, R2=1

Similarly for columns.

So:
- r=0 or 9: R1=1, R2=1
- r=1 or 8: R1=2, R2=1
- r=2,...,7: R1=2, R2=2

Number of moves = R1·C2 + R2·C1.

For white squares, let me enumerate by (row type, col type):

Row types: A (r=0,9): R1=1,R2=1; B (r=1,8): R1=2,R2=1; C (r=2-7): R1=2,R2=2.
Col types: same.

Moves = R1·C2 + R2·C1.

AA: 1·1 + 1·1 = 2
AB: 1·1 + 1·2 = 3 (row A, col B) or 2·1 + 1·1 = 3 (row B, col A). Same.
AC: 1·2 + 1·2 = 4 (row A, col C) or 2·2 + 1·1 = 5 (row C, col A). Different!

Hmm wait. Row A, Col C: R1=1,R2=1 (row), C2=2,C1=2 (col). Moves = 1·2 + 1·2 = 4.
Row C, Col A: R1=2,R2=2 (row), C2=1,C1=1 (col). Moves = 2·1 + 2·1 = 4. 

Oh wait, I made an error. Let me redo. Row C: R1=2, R2=2. Col A: C2=1, C1=1. Moves = R1·C2 + R2·C1 = 2·1 + 2·1 = 4. OK same.

BB: R1=2,R2=1, C2=1,C1=2. Moves = 2·1 + 1·2 = 4.
BC: Row B: R1=2,R2=1. Col C: C2=2,C1=2. Moves = 2·2 + 1·2 = 6. Row C, Col B: R1=2,R2=2, C2=1,C1=2. Moves = 2·1 + 2·2 = 6. Same.
CC: 2·2 + 2·2 = 8.

So attack set sizes:
- AA (corner): 2
- AB (edge near corner): 3
- AC (edge middle): 4
- BB (near-edge): 4
- BC (interior near edge): 6
- CC (center): 8

Now let me count white squares by type:

Row types for white squares:
- Row 0 (A): white cols 0,2,4,6,8. Col types: 0(A),2(C),4(C),6(C),8(B). So: 1A, 1B, 3C.
- Row 1 (B): white cols 1,3,5,7,9. Col types: 1(B),3(C),5(C),7(C),9(A). So: 1A, 1B, 3C.
- Row 2 (C): white cols 0,2,4,6,8. Col types: 0(A),2(C),4(C),6(C),8(B). So: 1A, 1B, 3C.
- Row 3 (C): same as row 2. 1A, 1B, 3C.
- Row 4 (C): same. 1A, 1B, 3C.
- Row 5 (C): white cols 1,3,5,7,9. Col types: 1(B),3(C),5(C),7(C),9(A). 1A, 1B, 3C.
- Row 6 (C): white cols 0,2,4,6,8. 1A, 1B, 3C.
- Row 7 (C): white cols 1,3,5,7,9. 1A, 1B, 3C.
- Row 8 (B): white cols 0,2,4,6,8. Col types: 0(A),2(C),4(C),6(C),8(B). 1A, 1B, 3C.
- Row 9 (A): white cols 1,3,5,7,9. Col types: 1(B),3(C),5(C),7(C),9(A). 1A, 1B, 3C.

So every row has 1A, 1B, 3C white squares.

Now, the (row type, col type) pairs for white squares:
- Row A (rows 0,9): 2 rows × (1A + 1B + 3C) = 2AA + 2AB + 6AC
- Row B (rows 1,8): 2 rows × (1A + 1B + 3C) = 2BA + 2BB + 6BC
- Row C (rows 2-7): 6 rows × (1A + 1B + 3C) = 6CA + 6CB + 18CC

Attack set sizes:
- AA: 2 → 2 squares
- AB: 3 → 2 squares
- AC: 4 → 6 squares
- BA: 3 → 2 squares (same as AB by symmetry)
- BB: 4 → 2 squares
- BC: 6 → 6 squares
- CA: 4 → 6 squares
- CB: 6 → 6 squares
- CC: 8 → 18 squares

Total: 2+2+6+2+2+6+6+6+18 = 50 ✓

Now, for the upper bound: if we place k white knights with disjoint attack sets, sum of attack sizes ≤ 50. To maximize k, we want to use squares with small attack sets.

If we use all AA (2 squares, 2 attacks each): 2 knights, 4 attacks.
AB+BA (4 squares, 3 attacks each): 4 knights, 12 attacks.
AC+CA (12 squares, 4 attacks each): 12 knights, 48 attacks.
BB (2 squares, 4 attacks): 2 knights, 8 attacks.
BC+CB (12 squares, 6 attacks): 12 knights, 72 attacks.
CC (18 squares, 8 attacks): 18 knights, 144 attacks.

If we only use squares with ≤ 4 attacks (AA, AB, BA, AC, CA, BB): 2+4+12+2 = 20 squares, total attacks = 4+12+48+8 = 72 > 50. So we can't use all of them.

To maximize knights with total attacks ≤ 50:
- Use all 2-attack squares (AA): 2 knights, 4 attacks.
- Use all 3-attack squares (AB, BA): 4 knights, 12 attacks. Running total: 6 knights, 16 attacks.
- Use 4-attack squares (AC, CA, BB): 14 squares available, each 4 attacks. We can use at most ⌊(50-16)/4⌋ = ⌊34/4⌋ = 8 more. Total: 14 knights, 16+32 = 48 attacks.
- Could we fit one more 6-attack? 48+6=54 > 50. No. One more 4-attack? 48+4=52 > 50. No.

So upper bound from counting: at most 14 white knights (2+4+8), giving 28 total.

But wait, this assumes we can actually achieve disjoint attack sets with these choices. The counting bound is necessary but not sufficient. Also, I assumed we use the smallest attack sets, but the disjointness constraint might force us to use larger attack sets or might prevent us from using certain small-attack squares.

Hmm, but actually the counting bound gives us: k knights, sum of attacks ≤ 50. The minimum possible sum for k knights is achieved by using the k squares with smallest attack sets. Let me sort:

2 attacks: 2 squares (AA)
3 attacks: 4 squares (AB, BA)
4 attacks: 14 squares (AC, CA, BB)
6 attacks: 12 squares (BC, CB)
8 attacks: 18 squares (CC)

For k knights, minimum total attacks:
k=2: 2×2=4
k=6: 2×2+4×3=16
k=14: 16+8×4=48
k=15: 48+4=52 > 50. 

So k ≤ 14 for one color, giving total ≤ 28.

But can we actually achieve 14? That requires using all 2-attack and 3-attack squares (6 knights) plus 8 of the 4-attack squares, with all attack sets disjoint. This seems very hard to achieve because the small-attack squares are on the edges and their attack sets might overlap.

Let me check: the 2-attack squares are (0,0) and (9,9). (0,0) attacks (1,2),(2,1). (9,9) attacks (8,7),(7,8). These are disjoint. Good.

The 3-attack squares: (0,8) attacks (1,6),(2,7),(2,9). (8,0) attacks (6,1),(7,2),(9,1)... wait let me recompute. (8,0): (8+1,0+2)=(9,2), (8+1,0-2)✗, (8-1,0+2)=(7,2), (8-1,0-2)✗, (8+2,0+1)✗, (8+2,0-1)✗, (8-2,0+1)=(6,1), (8-2,0-1)✗. So (9,2),(7,2),(6,1). 

(1,9): (1+1,9+2)✗,(1+1,9-2)=(2,7),(1-1,9+2)✗,(1-1,9-2)=(0,7),(1+2,9+1)✗,(1+2,9-1)=(3,8),(1-2,...)✗. So (2,7),(0,7),(3,8).

(9,1): (9-1,1+2)=(8,3),(9-1,1-2)✗,(9+1,...)✗,(9-2,1+1)=(7,2),(9-2,1-1)=(7,0). So (8,3),(7,2),(7,0).

Now check overlaps among 3-attack squares:
(0,8) attacks {(1,6),(2,7),(2,9)}
(8,0) attacks {(9,2),(7,2),(6,1)}
(1,9) attacks {(2,7),(0,7),(3,8)}
(9,1) attacks {(8,3),(7,2),(7,0)}

(0,8) and (1,9): both attack (2,7)! Conflict!

So we can't use both (0,8) and (1,9). This means the counting bound of 14 is not achievable.

This is getting really complex. Let me step back and think about whether there's a cleaner approach.

Let me reconsider the problem. Maybe I should think about it as a graph theory problem and look for the answer directly.

Actually, let me reconsider. The problem says "each square on the board can be attacked by at most one knight." I want to make sure I'm interpreting this correctly. A square is "attacked" by a knight if the knight can move to that square (i.e., it's a knight's move away). The square where a knight sits is not attacked by that knight (a knight doesn't attack its own square). But it could be attacked by another knight.

So the condition is: for every square s (whether occupied or not), the number of knights that are a knight's move away from s is at most 1.

This is exactly the open packing condition I described.

Let me try to look at this from a different angle. 

Consider the 10×10 board. A knight's move changes the sum of coordinates by ±1 or ±3. So a knight on a white square (even sum) attacks black squares (odd sum), and vice versa.

As I established, the problem decomposes into two independent subproblems (white knights attacking black squares, black knights attacking white squares). The answer is 2 × (max for one color).

For one color, I need to find the maximum open packing of the "knight graph restricted to white squares attacking black squares."

Let me try a computational approach in my head. Let me try to construct a good solution.

Construction attempt: Let me try to place knights on a pattern with period 5.

Consider placing white knights at positions (r, c) where r ∈ {0, 4, 8} (even rows, well-spaced) and c chosen appropriately.

Wait, let me try a different approach. Let me think about the conflict graph more carefully and try to find a large independent set.

From the analysis, two white knights conflict (share an attacked square) iff they're "close" in a specific sense. The safe pairs are those that are far apart.

Let me try to tile the board with a pattern that avoids conflicts.

Key observation: if two white knights are at (r1,c1) and (r2,c2) with |r1-r2| ≥ 5, they never conflict. So I can handle rows {0,1,2,3,4} and rows {5,6,7,8,9} independently (since the minimum row difference between these groups is |4-5|=1, which is < 5, so they're NOT independent). Hmm, that doesn't work.

Wait, actually |r1-r2| ≥ 5 means rows differ by at least 5. Rows 0-4 and rows 5-9: the closest pair is (4,5) with difference 1. So they're not independent.

But rows 0-4 and rows 5-9 with a gap: if I use rows {0,1,2} and rows {7,8,9}, then the minimum difference is |2-7|=5, so these are independent. But I'm leaving out rows 3,4,5,6.

Hmm, let me think about this differently. Let me try to find the maximum by considering specific constructions.

Construction 1: "Every other row, every 6th column."

Place knights in rows 0, 2, 4, 6, 8 (even rows, white squares at even columns). In each row, place knights at columns 0 and 6 (distance 6, safe within row).

Knights: (0,0),(0,6),(2,0),(2,6),(4,0),(4,6),(6,0),(6,6),(8,0),(8,6). 10 knights.

Check cross-row conflicts:
(0,0) vs (2,0): |Δr|=2,|Δc|=0. Conflict! (|Δr|=2, |Δc|∈{0,2,4}, 0∈{0,2,4}).

So this doesn't work. Knights in rows differing by 2 with same column conflict.

Construction 2: "Rows 0, 4, 8, columns 0 and 6."

(0,0),(0,6),(4,0),(4,6),(8,0),(8,6). 6 knights.

(0,0) vs (4,0): |Δr|=4,|Δc|=0. Conflict! (|Δr|=4, |Δc|∈{0,2}, 0∈{0,2}).

Still conflicts. The issue is that same-column knights in rows differing by 4 conflict.

Construction 3: "Rows 0, 4, 8, staggered columns."

Row 0: cols 0, 6. Row 4: cols 2, 8. Row 8: cols 0, 6.

(0,0),(0,6),(4,2),(4,8),(8,0),(8,6). 6 knights.

(0,0) vs (4,2): |Δr|=4,|Δc|=2. Conflict! (|Δr|=4, |Δc|∈{0,2}, 2∈{0,2}).

Hmm. For |Δr|=4, we need |Δc|∉{0,2}, so |Δc|∈{4,6,8}. 

Construction 4: "Rows 0, 4, 8, columns offset by 4."

Row 0: cols 0, 8. Row 4: cols 4. Row 8: cols 0, 8.

Wait, row 0 white cols: 0,2,4,6,8. Row 4 white cols: 0,2,4,6,8. Row 8 white cols: 0,2,4,6,8.

(0,0),(0,8),(4,4),(8,0),(8,8). 5 knights.

(0,0) vs (4,4): |Δr|=4,|Δc|=4. Safe (4∉{0,2}).
(0,0) vs (8,0): |Δr|=8. Safe.
(0,0) vs (8,8): |Δr|=8. Safe.
(0,8) vs (4,4): |Δr|=4,|Δc|=4. Safe.
(0,8) vs (8,0): |Δr|=8. Safe.
(0,8) vs (8,8): |Δr|=8. Safe.
(4,4) vs (8,0): |Δr|=4,|Δc|=4. Safe.
(4,4) vs (8,8): |Δr|=4,|Δc|=4. Safe.
(8,0) vs (8,8): |Δr|=0,|Δc|=8. Safe.

All safe! 5 white knights. But this is low. Can we do better?

Let me try to add more knights. Can I add knights in other rows?

Add (2, c) for some c. (2,c) is white if c even. 
(2,c) vs (0,0): |Δr|=2, need |Δc|∉{0,2,4}, so |Δc|∈{6,8}. c ∈ {6,8} (from even cols 0,2,4,6,8, with |c-0|∈{6,8}: c=6 or 8).
(2,c) vs (0,8): |Δr|=2, need |Δc|∉{0,2,4}, so |Δc|∈{6,8}. |c-8|∈{6,8}: c=0 or 2.
(2,c) vs (4,4): |Δr|=2, need |Δc|∉{0,2,4}. |c-4|∈{6,8}: c=... |c-4|≥6: c≥10 (impossible) or c≤-2 (impossible). So no valid c!

So we can't add any knight in row 2 because (4,4) blocks everything (|Δr|=2 requires |Δc|≥6, but max |c-4| on the board is 4).

Similarly, row 6 is blocked by (4,4).

What about odd rows? (1,c) white if c odd. 
(1,c) vs (0,0): |Δr|=1, need |Δc|∉{1,3}, so |Δc|∈{5,7,9}. |c-0|∈{5,7,9}: c∈{5,7,9}.
(1,c) vs (0,8): |Δr|=1, need |Δc|∉{1,3}. |c-8|∈{5,7,9}: c∈{1,3}. But we need c∈{5,7,9} ∩ {1,3} = ∅. 

So no knight in row 1 either (blocked by (0,0) and (0,8) together).

This construction is too sparse. The problem is that (0,0) and (0,8) together block most of rows 1 and 2, and (4,4) blocks the rest.

Let me try a different approach entirely. Let me think about what patterns could give a high density.

Idea: Use a "knight's tour" like pattern, or think about the problem as a coding theory problem.

Actually, let me reconsider the structure. The conflict graph on white squares has edges between "close" pairs. I want the maximum independent set.

Let me think about the white squares as a 5×5 grid of "even" squares and a 5×5 grid of "odd" squares (using the (i,j) parametrization from before).

Even squares: E(i,j) = (2i, 2j), i,j ∈ {0,1,2,3,4}.
Odd squares: O(i,j) = (2i+1, 2j+1), i,j ∈ {0,1,2,3,4}.

Conflicts within E (or within O): 
- Same i (same row pair): |j1-j2|∈{1,2} → conflict.
- |i1-i2|=1: |j1-j2|∈{0,1,2} → conflict.
- |i1-i2|=2: |j1-j2|∈{0,1} → conflict.
- |i1-i2|≥3: safe.

Conflicts between E and O:
E(i1,j1) and O(i2,j2): conflict iff i1-i2 ∈ {-1,0,1,2} and |j1-j2| ∈ {0,1,2}.

Note: the condition is asymmetric. Let me also check O(i1,j1) vs E(i2,j2):
O at (2i1+1, 2j1+1), E at (2i2, 2j2). Δr = |2i1+1-2i2| = |2(i1-i2)+1|. 
- i1-i2=0: Δr=1. Conflict iff Δc∈{1,3}. Δc=|2j1+1-2j2|=|2(j1-j2)+1|. |j1-j2|=0→1, =1→1 or 3, =2→3 or 5. So Δc∈{1,3} iff |j1-j2|∈{0,1,2}.
- i1-i2=1: Δr=3. Same: conflict iff |j1-j2|∈{0,1,2}.
- i1-i2=-1: Δr=1. Same.
- i1-i2=2: Δr=5. Safe.
- i1-i2=-2: Δr=3. Conflict iff |j1-j2|∈{0,1,2}.

So O(i1,j1) vs E(i2,j2): conflict iff i1-i2 ∈ {-2,-1,0,1} and |j1-j2|∈{0,1,2}.

Compare with E(i1,j1) vs O(i2,j2): conflict iff i1-i2 ∈ {-1,0,1,2} and |j1-j2|∈{0,1,2}.

These are different! E vs O: i_E - i_O ∈ {-1,0,1,2}. O vs E: i_O - i_E ∈ {-2,-1,0,1}, i.e., i_E - i_O ∈ {-1,0,1,2}. Wait:

O(i1,j1) vs E(i2,j2): i1-i2 ∈ {-2,-1,0,1}. This means i_O - i_E ∈ {-2,-1,0,1}, or equivalently i_E - i_O ∈ {-1,0,1,2}.

E(i1,j1) vs O(i2,j2): i1-i2 ∈ {-1,0,1,2}. This means i_E - i_O ∈ {-1,0,1,2}.

So both give the same condition: i_E - i_O ∈ {-1,0,1,2}. Good, it's symmetric after all (just the direction of the difference matters, but the set {-1,0,1,2} is the same).

Wait, no. E vs O: i_E - i_O ∈ {-1,0,1,2}. O vs E: i_O - i_E ∈ {-2,-1,0,1}, which is i_E - i_O ∈ {-1,0,1,2}. Yes, same condition. Good.

So the conflict between E(i_E, j_E) and O(i_O, j_O) is: i_E - i_O ∈ {-1,0,1,2} AND |j_E - j_O| ∈ {0,1,2}.

Equivalently: |i_E - i_O| ≤ 2 (but not i_E - i_O = -2, i.e., not i_E = i_O - 2) AND |j_E - j_O| ≤ 2.

Hmm, the asymmetry is that i_E - i_O = -2 (i_E = i_O - 2) is safe, but i_E - i_O = 2 (i_E = i_O + 2) is not. This is because the even rows are at 0,2,4,6,8 and odd rows at 1,3,5,7,9. E(i) is at row 2i, O(i) is at row 2i+1. So E(i_E) at row 2i_E and O(i_O) at row 2i_O+1. Δr = |2i_E - 2i_O - 1| = |2(i_E - i_O) - 1|.

If i_E - i_O = 2: Δr = |4-1| = 3. Conflict possible.
If i_E - i_O = -2: Δr = |-4-1| = 5. Safe.

So the asymmetry comes from the fact that even and odd rows are interleaved, and the "distance" depends on direction.

OK, this is a complex combinatorial optimization. Let me try to think about it more cleverly.

Let me try to find the answer by considering a specific good construction.

Construction idea: "Checkerboard of 3×3 blocks."

Divide the 5×5 grid of even squares into blocks. In each 3×3 block of the (i,j) grid, place one knight. But 5/3 doesn't divide evenly.

Let me try another approach. Let me think about the problem on the (i,j) grid for even squares only first, ignoring odd squares.

Within even squares E, conflicts are:
- |Δi|=0: |Δj|∈{1,2} conflict.
- |Δi|=1: |Δj|∈{0,1,2} conflict.
- |Δi|=2: |Δj|∈{0,1} conflict.
- |Δi|≥3: safe.

This is like a graph where each node conflicts with nodes in a 5×5 neighborhood (roughly). The maximum independent set in a 5×5 grid with this conflict structure...

If |Δi|≥3 is safe, then I can handle rows {0,1,2} and {3,4} independently (since |2-3|=1 < 3, not independent). Hmm, no. |Δi|≥3 means rows 0 and 3,4 are safe. But rows 0,1,2 interact with each other and with row 3 (|Δi|=2 for row 1 vs 3, |Δi|=1 for row 2 vs 3).

Actually, rows 0 and 3: |Δi|=3, safe. Rows 0 and 4: |Δi|=4, safe. So row 0 is safe with rows 3,4. Row 1: safe with row 4 (|Δi|=3). Row 2: safe with nothing in {3,4} (|2-3|=1, |2-4|=2, both conflict).

So I could split: {0,1,2} and {3,4}, but row 2 conflicts with rows 3,4. Not independent.

Alternatively: {0,1} and {3,4}, with row 2 separate. Row 0 vs 3,4: safe. Row 1 vs 4: safe. Row 1 vs 3: |Δi|=2, conflict possible. So {0,1} and {3,4} are not independent either (row 1 vs row 3).

Hmm. Let me try: {0,1} and {4}. Row 0 vs 4: safe. Row 1 vs 4: safe. So {0,1} and {4} are independent. Then rows 2,3 are separate.

This is getting complicated. Let me just try to directly construct a good solution.

Let me try to place knights on even squares only (ignoring odd squares for now) and see how many I can get.

Even squares E(i,j), i,j ∈ {0,1,2,3,4}. I want to select a subset with no conflicts.

Conflict: |Δi|=0 ∧ |Δj|∈{1,2}; |Δi|=1 ∧ |Δj|∈{0,1,2}; |Δi|=2 ∧ |Δj|∈{0,1}.

Let me try to place one knight per row of i, choosing j values carefully.

Row i=0: place at j=0. 
Row i=1: need |Δj|∉{0,1,2} from j=0, so j∈{3,4}. Place at j=3.
Row i=2: need |Δj|∉{0,1} from j=0 (|Δi|=2), and |Δj|∉{0,1,2} from j=3 (|Δi|=1). From j=0: j∉{0,1}, so j∈{2,3,4}. From j=3: j∉{1,2,3,4,5}, so j∈{0}. Intersection: {2,3,4} ∩ {0} = ∅. 

Can't place in row 2. Skip.
Row i=3: need |Δj|∉{0,1,2} from j=3 (|Δi|=2), so j∉{1,2,3,4,5}, j∈{0}. Need |Δj|∉{0,1} from j=0 (|Δi|=3, safe). So j=0 works. Place at j=0.
Row i=4: need |Δj|∉{0,1} from j=0 (|Δi|=4, safe). Need |Δj|∉{0,1,2} from j=3 (|Δi|=3, safe). Need |Δj|∉{0,1} from j=0 at i=3 (|Δi|=1, need |Δj|∉{0,1,2}). j=0 at i=3: |Δj|∉{0,1,2} from j=0, so j∈{3,4}. Place at j=3 or 4.

So: E(0,0), E(1,3), E(3,0), E(4,3). 4 knights from even squares.

Can I do better? Let me try a different pattern.

Row i=0: j=0 and j=4 (|Δj|=4, safe within row since |Δj|∉{1,2}).
Row i=1: from j=0, need |Δj|∉{0,1,2}, j∈{3,4}. From j=4, need |Δj|∉{0,1,2}, j∈{0,1}. Intersection: {3,4}∩{0,1}=∅. Can't place in row 1.

Row i=2: from j=0 (|Δi|=2), need |Δj|∉{0,1}, j∈{2,3,4}. From j=4 (|Δi|=2), need |Δj|∉{0,1}, j∈{0,1,2}. Intersection: {2,3,4}∩{0,1,2}={2}. Place at j=2.

Row i=3: from j=0 (|Δi|=3, safe). From j=4 (|Δi|=3, safe). From j=2 (|Δi|=1), need |Δj|∉{0,1,2}, j∈{} (|j-2|≥3 → j≥5 or j≤-1, impossible). Can't place.

Row i=4: from j=0 (|Δi|=4, safe). From j=4 (|Δi|=4, safe). From j=2 (|Δi|=2), need |Δj|∉{0,1}, j∈{0,4}. Place at j=0 or j=4. But need to check within row: only one knight in this row, so fine. Place at j=0.

E(0,0), E(0,4), E(2,2), E(4,0). 4 knights. Same count.

Let me try yet another pattern.

Row i=0: j=0.
Row i=1: j=4 (|Δj|=4 from j=0, safe since |Δi|=1 needs |Δj|∉{0,1,2}, 4∉{0,1,2} ✓).
Row i=2: from j=0 (|Δi|=2, |Δj|∉{0,1}), j∈{2,3,4}. From j=4 (|Δi|=1, |Δj|∉{0,1,2}), j∈{0,1}. Intersection: ∅. Can't place.

Row i=3: from j=0 (|Δi|=3, safe). From j=4 (|Δi|=2, |Δj|∉{0,1}), j∈{0,1,2}. Place at j=0 or 1 or 2.
Row i=4: from j=0 (|Δi|=4, safe). From j=4 (|Δi|=3, safe). From j=0 at i=3 (|Δi|=1, |Δj|∉{0,1,2}), j∈{3,4}. Place at j=3 or 4.

E(0,0), E(1,4), E(3,0), E(4,3). 4 knights.

Hmm, I keep getting 4 from even squares. Let me try to get 5.

Row i=0: j=0.
Row i=1: skip.
Row i=2: j=4 (from j=0, |Δi|=2, |Δj|=4∉{0,1} ✓).
Row i=3: from j=0 (safe), from j=4 (|Δi|=1, |Δj|∉{0,1,2}), j∈{0,1}. Place at j=0.
Row i=4: from j=0 (safe), from j=4 (|Δi|=2, |Δj|∉{0,1}), j∈{0,1,2}. From j=0 at i=3 (|Δi|=1, |Δj|∉{0,1,2}), j∈{3,4}. Intersection of all: {3,4} ∩ {0,1,2} ∩ all = ∅. Can't place.

Still 3. Let me try:

Row i=0: j=2.
Row i=1: from j=2 (|Δi|=1, |Δj|∉{0,1,2}), j∈{} (|j-2|≥3 → j≥5 or j≤-1). Can't place.
Row i=2: from j=2 (|Δi|=2, |Δj|∉{0,1}), j∈{3,4}. Place at j=3.
Row i=3: from j=2 (|Δi|=3, safe). From j=3 (|Δi|=1, |Δj|∉{0,1,2}), j∈{} (|j-3|≥3 → j≥6 or j≤0, so j=0). Place at j=0.
Row i=4: from j=2 (safe). From j=3 (|Δi|=2, |Δj|∉{0,1}), j∈{0,1,5}→{0,1}. From j=0 (|Δi|=1, |Δj|∉{0,1,2}), j∈{3,4}. Intersection: {0,1}∩{3,4}=∅. Can't place.

3 knights. Worse.

Let me try to be smarter. Maybe I should place 2 knights in some rows.

Row i=0: j=0, j=4 (|Δj|=4, safe).
Row i=1: from j=0 (|Δj|∉{0,1,2}, j∈{3,4}), from j=4 (|Δj|∉{0,1,2}, j∈{0,1}). Intersection: ∅. Can't place.
Row i=2: from j=0 (|Δj|∉{0,1}, j∈{2,3,4}), from j=4 (|Δj|∉{0,1}, j∈{0,1,2}). Intersection: {2}. Place at j=2.
Row i=3: from j=0 (safe), from j=4 (safe), from j=2 (|Δi|=1, |Δj|∉{0,1,2}, j∈{} impossible). Can't place.
Row i=4: from j=0 (safe), from j=4 (safe), from j=2 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4}). Place at j=0 or 1 or 4. But j=0 conflicts with... wait, within row i=4, only one knight so far. But j=0: check with j=0 at i=0 (|Δi|=4, safe ✓) and j=4 at i=0 (|Δi|=4, safe ✓) and j=2 at i=2 (|Δi|=2, |Δj|=2, conflict! |Δj|∈{0,1} → 2∉{0,1} ✓ safe). Wait, |Δi|=2, conflict iff |Δj|∈{0,1}. |Δj|=|0-2|=2, 2∉{0,1}. Safe! So j=0 works.

E(0,0), E(0,4), E(2,2), E(4,0). Can I add E(4,4)? Check E(4,4) vs E(4,0): |Δi|=0, |Δj|=4. Safe (4∉{1,2}). E(4,4) vs E(0,4): |Δi|=4, safe. E(4,4) vs E(0,0): |Δi|=4, safe. E(4,4) vs E(2,2): |Δi|=2, |Δj|=2. Conflict iff |Δj|∈{0,1}. 2∉{0,1}. Safe!

So E(0,0), E(0,4), E(2,2), E(4,0), E(4,4). 5 knights! Let me verify all pairs:

(0,0)-(0,4): |Δi|=0,|Δj|=4. Safe ✓
(0,0)-(2,2): |Δi|=2,|Δj|=2. |Δj|∉{0,1}. Safe ✓
(0,0)-(4,0): |Δi|=4. Safe ✓
(0,0)-(4,4): |Δi|=4. Safe ✓
(0,4)-(2,2): |Δi|=2,|Δj|=2. Safe ✓
(0,4)-(4,0): |Δi|=4. Safe ✓
(0,4)-(4,4): |Δi|=4. Safe ✓
(2,2)-(4,0): |Δi|=2,|Δj|=2. Safe ✓
(2,2)-(4,4): |Δi|=2,|Δj|=2. Safe ✓
(4,0)-(4,4): |Δi|=0,|Δj|=4. Safe ✓

All safe! 5 even-square knights.

Can I add more? Let me try adding to row i=1 or i=3.

Row i=1: from E(0,0) (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). From E(0,4) (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). Intersection: ∅. Can't.

Row i=3: from E(2,2) (|Δi|=1, |Δj|∉{0,1,2}, j∈{} since |j-2|≥3 → j≥5 or j≤-1). Can't.

So 5 is the max for this pattern on even squares. Can I do better with a different pattern?

Let me try:
Row i=0: j=1.
Row i=1: from j=1 (|Δi|=1, |Δj|∉{0,1,2}, j∈{4}). Place at j=4.
Row i=2: from j=1 (|Δi|=2, |Δj|∉{0,1}, j∈{3,4}). From j=4 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). Intersection: ∅. Can't.
Row i=3: from j=1 (safe). From j=4 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,2}). Place at j=0.
Row i=4: from j=1 (safe). From j=4 (safe). From j=0 (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). Place at j=3 or 4. j=4: check with j=4 at i=1 (|Δi|=3, safe ✓). Place at j=4.

E(0,1), E(1,4), E(3,0), E(4,4). 4 knights. Less.

Let me try to get 6 on even squares.

Hmm, let me think about this more carefully. The 5×5 grid with the conflict structure... Let me think about what the maximum independent set is.

Actually, let me try a pattern where I use rows 0, 2, 4 (every other row) and within each row, use 2 well-separated columns.

Row 0: j=0, j=4 (safe, |Δj|=4).
Row 2: from j=0 (|Δi|=2, |Δj|∉{0,1}, j∈{2,3,4}). From j=4 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,2}). Intersection: {2}. Place at j=2. Can I place a second? j=2 is the only option. Just 1.
Row 4: from j=0 (safe), j=4 (safe), j=2 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4}). Place at j=0 and j=4. Check j=0 vs j=4: |Δj|=4, safe. Check j=0 vs j=2 at row 2: |Δi|=2, |Δj|=2, safe. Check j=4 vs j=2 at row 2: |Δi|=2, |Δj|=2, safe.

E(0,0), E(0,4), E(2,2), E(4,0), E(4,4). 5 knights. Same as before.

Can I use rows 1 and 3 as well?

Row 1: from E(0,0) (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). From E(0,4) (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). Intersection: ∅. Can't.

Row 3: from E(2,2) (|Δi|=1, |Δj|∉{0,1,2}, j∈{} impossible). Can't.

So 5 is the max with this approach. Let me try completely different patterns.

Pattern: 1 per row, 5 rows.

Row 0: j=0
Row 1: j=3 (|Δi|=1, |Δj|=3∉{0,1,2} ✓)
Row 2: from j=0 (|Δi|=2, |Δj|∉{0,1}, j∈{2,3,4}). From j=3 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0}). Intersection: ∅. Can't.

Row 0: j=0
Row 1: j=4 (|Δj|=4∉{0,1,2} ✓)
Row 2: from j=0 (j∈{2,3,4}). From j=4 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). ∅. Can't.

Row 0: j=1
Row 1: j=4 (|Δj|=3∉{0,1,2} ✓)
Row 2: from j=1 (|Δi|=2, |Δj|∉{0,1}, j∈{3,4}). From j=4 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). ∅. Can't.

It seems hard to get more than 5 on even squares. Let me try 2 in some rows and 0 in others.

Row 0: j=0, j=3. Wait, |Δj|=3, but for |Δi|=0, conflict iff |Δj|∈{1,2}. 3∉{1,2}. Safe! So j=0 and j=3 in same row.

Row 0: j=0, j=3.
Row 1: from j=0 (|Δj|∉{0,1,2}, j∈{3,4}). From j=3 (|Δj|∉{0,1,2}, j∈{0}). ∅. Can't.

Row 2: from j=0 (|Δi|=2, |Δj|∉{0,1}, j∈{2,3,4}). From j=3 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4,5}→{0,1,4}). Intersection: {4}. Place at j=4.

Row 3: from j=0 (safe). From j=3 (safe). From j=4 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). Place at j=0 or 1.
j=0: check with j=0 at row 0 (|Δi|=3, safe ✓), j=3 at row 0 (|Δi|=3, safe ✓), j=4 at row 2 (|Δi|=1, |Δj|=4∉{0,1,2} ✓). Place at j=0.
Can I place a second in row 3? j=1: check with j=0 in row 3 (|Δj|=1, conflict! |Δi|=0, |Δj|∈{1,2}). No. So just j=0.

Row 4: from j=0 row 0 (safe), j=3 row 0 (safe), j=4 row 2 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,2}), j=0 row 3 (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). Intersection: {0,1,2}∩{3,4}=∅. Can't.

E(0,0), E(0,3), E(2,4), E(3,0). 4 knights. Less than 5.

Let me try:
Row 0: j=0, j=4.
Row 2: j=2 (as before).
Row 4: j=0, j=4.
= 5 knights.

Can I add to row 1 or 3? Already checked, no.

What about:
Row 0: j=1, j=4 (|Δj|=3, safe).
Row 1: from j=1 (|Δj|∉{0,1,2}, j∈{4}). From j=4 (|Δj|∉{0,1,2}, j∈{0,1}). ∅. Can't.
Row 2: from j=1 (|Δi|=2, |Δj|∉{0,1}, j∈{3,4}). From j=4 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,2}). ∅. Can't.

Hmm. Let me try:
Row 0: j=0.
Row 1: j=3.
Row 2: can't (shown above).
Row 3: from j=0 (safe), j=3 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4,5}→{0,1,4}). Place at j=0, j=1, or j=4.
  j=4: check with j=3 at row 1 (|Δi|=2, |Δj|=1, conflict! |Δj|∈{0,1}). No.
  j=0: check with j=3 at row 1 (|Δi|=2, |Δj|=3∉{0,1} ✓). Check with j=0 at row 0 (|Δi|=3, safe ✓). Place at j=0.
  j=1: check with j=3 at row 1 (|Δi|=2, |Δj|=2∉{0,1} ✓). Check with j=0 at row 0 (|Δi|=3, safe ✓). Place at j=1.
  Can I place both j=0 and j=1? |Δj|=1, |Δi|=0, conflict. No. Just one.
  Let's say j=1.

Row 4: from j=0 row 0 (safe), j=3 row 1 (safe), j=1 row 3 (|Δi|=1, |Δj|∉{0,1,2}, j∈{4}). Place at j=4.
  Check j=4 with j=3 row 1 (|Δi|=3, safe ✓), j=0 row 0 (|Δi|=4, safe ✓). ✓

E(0,0), E(1,3), E(3,1), E(4,4). 4 knights.

Or with j=0 at row 3:
Row 4: from j=0 row 3 (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). From j=0 row 0 (safe). From j=3 row 1 (safe). Place at j=3 or 4.
  j=3: check with j=3 row 1 (|Δi|=3, safe ✓). ✓
  j=4: check with j=3 row 1 (|Δi|=3, safe ✓). ✓
  Can I place both? |Δj|=1, conflict. No. Just one.

E(0,0), E(1,3), E(3,0), E(4,3). 4 knights.

I keep getting 4-5. Let me try to see if 6 is possible on even squares.

Let me try:
Row 0: j=0.
Row 1: skip.
Row 2: j=3 (|Δi|=2, |Δj|=3∉{0,1} ✓).
Row 3: skip.
Row 4: j=0 (|Δi|=4 from row 0, safe; |Δi|=2 from row 2, |Δj|=3∉{0,1} ✓). 

That's only 3. Add more:
Row 0: j=0, j=4 (|Δj|=4, safe).
Row 2: from j=0 (j∈{2,3,4}), from j=4 (j∈{0,1,2}). Intersection: {2}. j=2.
Row 4: from j=0 (safe), j=4 (safe), j=2 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4}). Place j=0, j=4.

5 knights. Same as before.

What if I try        — AI历史解题过程（thinking）
#   polymath_01400         — 题目ID

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
  <problem_id>polymath_01400</problem_id>
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

In a $10 \times 10$ chess board, what is the maximum number of knights that can be placed such that each square on the board can be attacked by at most one knight?

## Standard Solution

To solve the problem of placing the maximum number of knights on a \(10 \times 10\) chessboard such that each square is attacked by at most one knight, we need to ensure that the attack ranges of the knights do not overlap. Here is a detailed, clean solution:

### Problem Restatement
We need to place the maximum number of knights on a \(10 \times 10\) chessboard such that each square on the board can be attacked by at most one knight. Knights move in an L-shape, covering up to 8 squares.

### Key Observations
1. **Knight's Attack Pattern**: Each knight attacks 8 squares in an L-shape.
2. **Overlap Constraint**: No two knights can attack the same square, either directly or through their attack ranges.
3. **Upper Bound Calculation**: If \(N\) is the number of knights, the total number of attacked squares (including the squares occupied by the knights) must not exceed 100. This gives us the inequality \(8N + N \leq 100\), simplifying to \(9N \leq 100\), and thus \(N \leq \frac{100}{9} \approx 11.11\). Therefore, the maximum integer value for \(N\) is 12.

### Arrangement Strategy
To achieve this upper bound of 12 knights, we can use a systematic placement strategy:
1. **Checkerboard Pattern**: Place knights on a checkerboard pattern but ensure that the knights are spaced sufficiently apart to avoid overlapping attack ranges.
2. **Spacing**: Place knights such that they are at least 3 squares apart in both the horizontal and vertical directions. This ensures that their attack ranges do not overlap.

### Example Placement
1. **First Row**: Place knights at positions \((1,1)\), \((1,4)\), \((1,7)\), and \((1,10)\).
2. **Second Row**: Skip the second row.
3. **Third Row**: Place knights at positions \((3,1)\), \((3,4)\), \((3,7)\), and \((3,10)\).
4. **Fourth Row**: Skip the fourth row.
5. **Fifth Row**: Place knights at positions \((5,1)\), \((5,4)\), \((5,7)\), and \((5,10)\).
6. **Sixth Row**: Skip the sixth row.
7. **Seventh Row**: Place knights at positions \((7,1)\), \((7,4)\), \((7,7)\), and \((7,10)\).
8. **Eighth Row**: Skip the eighth row.
9. **Ninth Row**: Place knights at positions \((9,1)\), \((9,4)\), \((9,7)\), and \((9,10)\).

This pattern ensures that each knight is at least 3 squares apart from any other knight, both horizontally and vertically, thus avoiding overlapping attack ranges.

### Verification
- Each knight attacks up to 8 squares, and with the spacing, these attack ranges do not overlap.
- Each square is attacked by at most one knight, satisfying the problem's constraints.

### Conclusion
The maximum number of knights that can be placed on a \(10 \times 10\) chessboard such that each square is attacked by at most one knight is \(\boxed{12}\).

## AI's Thinking (Attempted Solution Process)

The problem: On a 10×10 chessboard, what is the maximum number of knights that can be placed such that each square on the board can be attacked by at most one knight?

Let me think about this carefully. We need to place knights such that every square (including occupied ones? or just empty ones?) is attacked by at most one knight.

"each square on the board can be attacked by at most one knight" - this means for every square, the number of knights that attack it is ≤ 1.

Note: a knight doesn't attack its own square. So occupied squares count too - they must be attacked by at most one other knight.

This is a classic problem. Let me think about the structure.

A knight on a square attacks up to 8 squares. The constraint is that no two knights share a common attacked square. In other words, the sets of squares attacked by different knights must be pairwise disjoint.

Wait, more precisely: for each square s, the number of knights attacking s is at most 1. So the "attack sets" of the knights (the squares each knight attacks) must be pairwise disjoint.

Actually, if knight A attacks square s and knight B also attacks square s, then s is attacked by 2 knights, violating the constraint. So yes, the attack sets must be pairwise disjoint.

But also, a knight's attack set includes the squares it attacks. If knight A is placed on a square that knight B attacks, and knight B is placed on a square that knight A attacks... that's fine as long as no square is attacked by 2+ knights.

Wait, but the occupied square of knight A - is it "attacked" by knight A? No, a knight doesn't attack its own square. So the square where knight A sits is attacked by other knights only. The constraint applies to that square too: it must be attacked by at most 1 knight.

So the condition is: the attack sets (squares attacked by each knight, not including its own square) are pairwise disjoint.

The total number of attacked squares = sum of |attack set of each knight|. These must all be disjoint, and they're all within the 100 squares of the board. So sum of attack set sizes ≤ 100.

Each knight attacks between 2 (corner) and 8 (center) squares. To maximize the number of knights, we want each knight to attack as few squares as possible, so we should place knights in corners and near edges.

But we also need the attack sets to be disjoint. This is a complex combinatorial optimization.

Let me think about this differently. This is a known competition problem. Let me try to figure out the answer.

Actually, let me think about lower bounds via construction and upper bounds via counting.

Upper bound: If we place k knights, the total number of attacked squares (with multiplicity, but they must be distinct) is at least... well each knight attacks at least 2 squares (corner knights). But we can't place all knights in corners.

Hmm, let me think about this more carefully with the coloring approach.

Consider the standard chessboard coloring (black/white). A knight always attacks squares of the opposite color. So a knight on a white square attacks black squares, and vice versa.

If we only place knights on white squares, then all attacked squares are black squares. The attack sets are subsets of the 50 black squares, and they must be pairwise disjoint. So the sum of attack set sizes ≤ 50.

Similarly if we place on black squares, attacked squares are white, sum ≤ 50.

But we can mix: some knights on white (attacking black squares), some on black (attacking white squares). The constraint is that the attack sets are all pairwise disjoint. Knights on white attack black squares; knights on black attack white squares. So a white-knight's attack set and a black-knight's attack set are automatically disjoint (different colors)! 

So we can independently optimize: place knights on white squares (attacking black squares, disjoint attack sets within the 50 black squares) and place knights on black squares (attacking white squares, disjoint attack sets within the 50 white squares). The total is the sum.

So the problem decomposes into two independent subproblems, one for each color. By symmetry (the board is symmetric under color swap), both give the same answer. So total = 2 × (max knights on one color).

Wait, but I need to be more careful. When we place knights on white squares, the attacked squares are black. But we also need: no black square is attacked by more than one white-knight. And the white squares where knights sit - they're attacked by black-knights (if any), and those must also be ≤ 1. But since we separated by color, white-knights only attack black squares, black-knights only attack white squares. A white square is attacked only by black-knights (at most 1). A black square is attacked only by white-knights (at most 1). So the decomposition is valid.

So we need to solve: on a 10×10 board, place knights on squares of one color (say white) such that no square of the opposite color (black) is attacked by more than one knight. Maximize the number of knights.

The white squares form a specific pattern. Let me think of the board as coordinates (i,j) with 1≤i,j≤10. White squares: i+j even (say). Black squares: i+j odd.

A knight on white square (i,j) attacks black squares (i±1,j±2) and (i±2,j±1) that are on the board.

We need to select a set of white squares such that the attack sets (subsets of black squares) are pairwise disjoint.

This is equivalent to: no two selected white squares attack a common black square. Two white squares (i1,j1) and (i2,j2) attack a common black square iff there exists a black square attacked by both. 

Two knights attack a common square iff they are both a knight's move away from some square. This means the two knights are at distance... if both are a knight's move from square s, then the two knights are at most 2 knight-moves apart. Actually, two squares share a common attacked square iff they are both knight-neighbors of some square, which happens iff they are at "knight distance 2" or they are the same square.

Hmm, this is getting complicated. Let me think about it as a graph problem.

Actually, let me reconsider. The condition "attack sets are pairwise disjoint" means: for any two knights, their attack sets don't intersect. Two knights' attack sets intersect iff there's a square attacked by both, iff the two knights are both a knight's move from some common square.

Let me think about when two squares (a,b) and (c,d) have a common knight-neighbor. A square (x,y) is a knight-neighbor of (a,b) if (x,y) = (a±1,b±2) or (a±2,b±1). Similarly for (c,d). They share a knight-neighbor if some (x,y) is a knight-neighbor of both.

The set of knight-neighbors of (a,b) is N(a,b) = {(a±1,b±2),(a±2,b±1)} ∩ board.

Two squares share a knight-neighbor iff |N(a,b) ∩ N(c,d)| > 0.

This is complex. Let me try a different approach - just try to find the answer computationally in my head, or recall known results.

Actually, this is a well-known problem. Let me think...

For an n×n board, the maximum number of knights such that each square is attacked by at most one knight. 

Let me try small cases and think about the pattern.

For a 1×n board: knights attack nothing (knight moves go off board). So we can place n knights, each attacking 0 squares. All squares attacked by 0 knights. Answer: n.

Hmm wait, on a 1×10 board, a knight can't attack any square (all knight moves go off the 1-row board). So we can place 10 knights, answer 10.

For 2×n: A knight on (1,j) attacks (2,j±2)... wait no. Knight on (1,j): moves are (1±1, j±2) = (2, j±2) and (1±2, j±1) = off board. So attacks (2,j-2) and (2,j+2). Similarly knight on (2,j) attacks (1,j±2).

So on a 2×n board, a knight on row 1, column j attacks row 2, columns j-2 and j+2. 

For the attack sets to be disjoint... this is like a matching problem.

This is getting complicated for general n. Let me focus on 10×10.

Let me try to think about this problem from the competition math perspective. I believe the answer might be 32 or 34 or something like that.

Let me try the decomposition approach more carefully.

We split into two colors. For each color, we have 50 squares of that color, and we want to place knights on them such that the attack sets (on the 50 squares of the opposite color) are disjoint.

Let me think about the structure of white squares and their attacks on black squares.

On a 10×10 board, label squares (r,c) with r,c ∈ {0,...,9}. White = r+c even.

The white squares form a grid-like pattern. Let me think of them in terms of a transformed coordinate system.

Actually, let me think about this problem differently. 

Consider the "knight graph" where we connect two squares if they're a knight's move apart. The condition is that we select a set S of vertices such that no two vertices in S have a common neighbor. This is called a "2-packing" or "open packing" of the graph. Actually, it's specifically that the open neighborhoods are disjoint, which is called an "open packing" or "total 2-packing."

Wait, actually the condition is that the open neighborhoods N(v) for v ∈ S are pairwise disjoint. This is exactly an "open packing" of the graph.

The maximum open packing number of the knight's graph on a 10×10 board... this is a specific combinatorial quantity.

Hmm, let me try to think about constructions.

Construction idea: Place knights on every other square in a pattern. 

Let me think about a 4×4 block. In a 4×4 block, can we place 4 knights (one per color-pair)?

Actually, let me try to think about tiling the 10×10 board with patterns.

Let me try a specific construction. Consider placing knights on squares where both coordinates are ≡ 0 (mod 4) or both ≡ 1 (mod 4)... no, let me think more carefully.

Let me try: place knights on squares (r, c) where r ≡ 0 (mod 2) and c ≡ 0 (mod 2), i.e., both even. On a 10×10 board (0-9), even coordinates are 0,2,4,6,8, so 5×5 = 25 squares. But these are all white squares (even+even=even). 

A knight on (0,0) attacks (1,2),(2,1). A knight on (0,2) attacks (1,0),(1,4),(2,1),(2,3). Wait, (2,1) is attacked by both (0,0) and (0,2)! So this doesn't work.

Let me try a sparser pattern. Place knights on (r,c) where r ≡ 0 (mod 4) and c ≡ 0 (mod 4): (0,0),(0,4),(0,8),(4,0),(4,4),(4,8),(8,0),(8,4),(8,8) = 9 knights. But these are all same color. Their attack sets:

(0,0): (1,2),(2,1)
(0,4): (1,2),(1,6),(2,3),(2,5) - wait, (1,2) is shared with (0,0)!

So (0,0) and (0,4) both attack (1,2). Doesn't work.

The issue is that knights 4 apart in a row can share attacked squares. Let me think about what distance avoids shared attacks.

Two knights on the same row, columns c1 and c2. They share an attacked square if there's a square (r±1, c*) or (r±2, c*) attacked by both. 

Knight at (r,c1) attacks (r±1, c1±2) and (r±2, c1±1).
Knight at (r,c2) attacks (r±1, c2±2) and (r±2, c2±1).

They share a square if:
- (r±1, c1±2) = (r±1, c2±2): c1±2 = c2±2, so |c1-c2| ∈ {0,4}
- (r±1, c1±2) = (r±1, c2∓2): c1+2 = c2-2 or c1-2 = c2+2, so |c1-c2| = 4
- (r±2, c1±1) = (r±2, c2±1): |c1-c2| ∈ {0,2}
- (r±1, c1±2) = (r±2, c2±1): r±1 = r±2, impossible (different rows unless... r+1 = r+2 no, r+1 = r-2 no, r-1 = r+2 no, r-1 = r-2 no). Actually wait, the row offsets: one gives r+1 or r-1, other gives r+2 or r-2. These are never equal. So no overlap here.
- (r±2, c1±1) = (r±1, c2±2): similarly, r±2 vs r±1, never equal. No overlap.

So two knights on the same row share an attacked square iff |c1-c2| ∈ {2, 4}.

So on the same row, knights must be at column distance not in {2,4}. They can be at distance 1,3,5,6,7,... But wait, they also need to be on the same color (if we're doing the color decomposition). Same row, same color means column difference is even. So allowed even distances: 6, 8, ... On a 10-wide board, distance 6 or 8.

Hmm, that's very restrictive. On a single row of 10 squares, same color, we can place knights at columns that are pairwise at distance ≥ 6 (and even). So like columns 0 and 6, or 0 and 8, or 2 and 8. At most 2 per row.

But we also need to consider knights on different rows. Let me think about two knights on different rows.

Knight at (r1,c1) and (r2,c2), both white (r1+c1 even, r2+c2 even).

They share an attacked square if some square is attacked by both. 

The attacked squares of (r1,c1) are at rows r1±1, r1±2 and the attacked squares of (r2,c2) are at rows r2±1, r2±2. For overlap, we need some row that's in {r1±1, r1±2} ∩ {r2±1, r2±2}.

Possible row overlaps:
- r1+1 = r2+1 → r1=r2 (same row, handled above)
- r1+1 = r2-1 → r2 = r1+2
- r1+1 = r2+2 → r2 = r1-1
- r1+1 = r2-2 → r2 = r1+3
- r1-1 = r2+1 → r2 = r1-2
- r1-1 = r2-1 → r1=r2
- r1-1 = r2+2 → r2 = r1-3
- r1-1 = r2-2 → r2 = r1+1
- r1+2 = r2+1 → r2 = r1+1
- r1+2 = r2-1 → r2 = r1+3
- r1+2 = r2+2 → r1=r2
- r1+2 = r2-2 → r2 = r1+4
- r1-2 = r2+1 → r2 = r1-3
- r1-2 = r2-1 → r2 = r1-1
- r1-2 = r2+2 → r2 = r1-4
- r1-2 = r2-2 → r1=r2

So |r1-r2| ∈ {0, 1, 2, 3, 4} could potentially cause overlap. But we also need the column to match. Let me be more systematic.

For |r1-r2| = 1: Say r2 = r1+1. The overlapping row could be r1+1 (= r2) or r1+2 (= r2+1) wait no. Let me redo.

If r2 = r1+1:
- r1+1 = r2: attacked by knight 1 at row r1+1 (columns c1±2), attacked by knight 2 at row r2 = r1+1 (columns c2±1, since r2-1 = r1, so row r1+1 = r2 is attacked by knight 2 via the r2-1... no wait.

Let me be more careful. Knight at (r2, c2) attacks rows r2-2, r2-1, r2+1, r2+2 (those that are on the board). At row r2-1, it attacks columns c2±2. At row r2-2, it attacks columns c2±1. At row r2+1, columns c2±2. At row r2+2, columns c2±1.

Knight at (r1, c1) attacks: row r1-1: c1±2; row r1-2: c1±1; row r1+1: c1±2; row r1+2: c1±1.

If r2 = r1+1:
Overlapping rows: 
- r1+1 = r2: knight 1 attacks (r1+1, c1±2), knight 2 attacks (r2, c2±2) = (r1+1, c2±2). Overlap if c1±2 = c2±2, i.e., |c1-c2| ∈ {0,4}.
- r1+2 = r2+1: knight 1 attacks (r1+2, c1±1), knight 2 attacks (r2+1, c2±2) = (r1+2, c2±2). Overlap if c1±1 = c2±2, i.e., |c1-c2| ∈ {1,3}.
- r1-1 = r2-2: knight 1 attacks (r1-1, c1±2), knight 2 attacks (r2-2, c2±1) = (r1-1, c2±1). Overlap if c1±2 = c2±1, i.e., |c1-c2| ∈ {1,3}.

But both knights are white, so c1 and c2 have the same parity as needed for white: r1+c1 even, r2+c2 = r1+1+c2 even, so c2 is odd if c1 is even, and vice versa. So c1 and c2 have different parities, meaning |c1-c2| is odd. So |c1-c2| ∈ {1,3} is possible, |c1-c2| ∈ {0,4} is not.

So for r2 = r1+1 (adjacent rows, both white knights), they share an attacked square iff |c1-c2| ∈ {1,3}.

For r2 = r1+2:
Overlapping rows:
- r1+1 = r2-1: knight 1 attacks (r1+1, c1±2), knight 2 attacks (r2-1, c2±2) = (r1+1, c2±2). Overlap if |c1-c2| ∈ {0,4}.
- r1+2 = r2: knight 1 attacks (r1+2, c1±1), knight 2 attacks (r2, c2±1) = (r1+2, c2±1). Overlap if |c1-c2| ∈ {0,2}.
- r1-1 = r2-3: no (r2-3 not in {r2±1,r2±2}).
- r1-2 = r2-4: no.

Both white: r1+c1 even, r2+c2 = r1+2+c2 even, so c1, c2 same parity. |c1-c2| even. So |c1-c2| ∈ {0,2,4}. All of {0,2,4} cause overlap. So any two white knights in rows differing by 2 always share an attacked square (as long as they're close enough in columns, which on a 10-wide board they might not be... well |c1-c2| ∈ {0,2,4} - but if they're far apart, like c1=0, c2=8, then |c1-c2|=8, not in {0,2,4}, so no overlap).

Wait, I need to be more careful. The overlap condition is |c1-c2| ∈ {0,2,4} AND the specific attacked squares are on the board. But the column condition is necessary. So for rows differing by 2, overlap iff |c1-c2| ∈ {0,2,4}.

For r2 = r1+3:
Overlapping rows:
- r1+1 = r2-2: knight 1 attacks (r1+1, c1±2), knight 2 attacks (r2-2, c2±1) = (r1+1, c2±1). Overlap if c1±2 = c2±1, |c1-c2| ∈ {1,3}.
- r1+2 = r2-1: knight 1 attacks (r1+2, c1±1), knight 2 attacks (r2-1, c2±2) = (r1+2, c2±2). Overlap if |c1-c2| ∈ {1,3}.
- r1-2 = r2-5: no.

Both white: r1+c1 even, r2+c2 = r1+3+c2 even, so c1, c2 different parity. |c1-c2| odd. So |c1-c2| ∈ {1,3} possible. Overlap iff |c1-c2| ∈ {1,3}.

For r2 = r1+4:
Overlapping rows:
- r1+2 = r2-2: knight 1 attacks (r1+2, c1±1), knight 2 attacks (r2-2, c2±1) = (r1+2, c2±1). Overlap if |c1-c2| ∈ {0,2}.

Both white: r1+c1 even, r2+c2 = r1+4+c2 even, c1,c2 same parity. |c1-c2| even. Overlap iff |c1-c2| ∈ {0,2}.

For |r1-r2| ≥ 5: No overlapping rows (since knight attacks reach at most 2 rows away, so rows r1-2 to r1+2 and r2-2 to r2+2; if |r1-r2|≥5, these don't overlap). So no shared attacks.

Summary for two white knights:
- Same row (|Δr|=0): overlap iff |Δc| ∈ {2,4}
- |Δr|=1: overlap iff |Δc| ∈ {1,3}
- |Δr|=2: overlap iff |Δc| ∈ {0,2,4}
- |Δr|=3: overlap iff |Δc| ∈ {1,3}
- |Δr|=4: overlap iff |Δc| ∈ {0,2}
- |Δr|≥5: no overlap

And for white knights, Δr and Δc have the same parity (since both are white: r+c even for both, so Δr+Δc even, meaning Δr and Δc have same parity).

So:
- |Δr|=0 (even): |Δc| even. Overlap iff |Δc|∈{2,4}. Safe if |Δc|∈{0,...} wait |Δc|=0 means same square. So |Δc|≥6 or |Δc|=0 (same square, not applicable). Safe: |Δc|∈{6,8,...} ∪ {|Δc| not in {2,4}}. Actually |Δc| even and not in {2,4}: |Δc| ∈ {0, 6, 8}. But 0 is same square. So |Δc| ≥ 6.
- |Δr|=1 (odd): |Δc| odd. Overlap iff |Δc|∈{1,3}. Safe: |Δc|∈{5,7,9,...}.
- |Δr|=2 (even): |Δc| even. Overlap iff |Δc|∈{0,2,4}. Safe: |Δc|≥6.
- |Δr|=3 (odd): |Δc| odd. Overlap iff |Δc|∈{1,3}. Safe: |Δc|≥5.
- |Δr|=4 (even): |Δc| even. Overlap iff |Δc|∈{0,2}. Safe: |Δc|∈{4,6,8,...}. Wait, |Δc|=4 is safe for |Δr|=4? Let me check: overlap iff |Δc|∈{0,2}. So |Δc|=4 is safe. |Δc|∈{4,6,8}.
- |Δr|≥5: always safe.

So the "conflict" conditions are quite restrictive. Two white knights conflict (share an attacked square) when they're close together. Specifically:

Let me restate: two white knights at (r1,c1) and (r2,c2) conflict iff:
- |Δr|=0 and |Δc|∈{2,4}
- |Δr|=1 and |Δc|∈{1,3}
- |Δr|=2 and |Δc|∈{0,2,4}
- |Δr|=3 and |Δc|∈{1,3}
- |Δr|=4 and |Δc|∈{0,2}

And no conflict if |Δr|≥5 or if the pair doesn't match any above.

Now I need to find the maximum independent set in this "conflict graph" on the 50 white squares. This is a complex optimization.

Let me think about it differently. The conflict conditions essentially say that knights can't be too close. Let me think about what patterns work.

Consider placing knights with a spacing of 5 in both directions. Like (r,c) where r ≡ 0 (mod 5) and c ≡ 0 (mod 5), but only white squares.

r ∈ {0,5}, c ∈ {0,5}: (0,0),(0,5),(5,0),(5,5). Check: (0,0) and (0,5): |Δr|=0,|Δc|=5. Not in {2,4}. Safe. (0,0) and (5,0): |Δr|=5. Safe. (0,0) and (5,5): |Δr|=5. Safe. All safe. But this only gives 4 knights on white squares (and 4 on black, total 8). Way too few.

We can do much better. Let me think about denser packings.

Key insight: |Δr|≥5 is always safe. So knights in rows that are 5+ apart never conflict. We can handle rows 0-4 and rows 5-9 independently (almost - need to check |Δr|=4 between row 4 and rows in 0-3, and between rows 5-9, and |Δr| could be 4 between row 0 and row 4, row 5 and row 9, etc.)

Actually, let me think about this more carefully. Rows 0-4 and rows 5-9: the minimum |Δr| between a row in {0,1,2,3,4} and a row in {5,6,7,8,9} is |4-5|=1. So they're not independent. Hmm.

Let me try a different approach. Let me think about what the maximum could be and try constructions.

Upper bound approach: Each knight attacks some number of squares. The attack sets are disjoint and contained in 50 squares (of the opposite color). So sum of attack set sizes ≤ 50.

If we place k white knights, sum of their attack set sizes ≤ 50. Each knight attacks at least 2 squares (corner) and at most 8 (center). To maximize k, minimize average attack set size.

But the attack set sizes depend on position. Corner white squares: (0,0),(0,8)... wait, on a 10×10 board (0-9), white corners are (0,0),(0,8)?? No. (0,0): 0+0=0, even, white. (0,9): 0+9=9, odd, black. (9,0): 9, odd, black. (9,9): 18, even, white. So white corners: (0,0) and (9,9). And black corners: (0,9) and (9,0).

(0,0) attacks (1,2),(2,1) = 2 squares.
(9,9) attacks (8,7),(7,8) = 2 squares.

Edge white squares (not corner): e.g., (0,2) attacks (1,0),(1,4),(2,1),(2,3) = 4 squares. (0,4): (1,2),(1,6),(2,3),(2,5) = 4. (0,6): (1,4),(1,8),(2,5),(2,7) = 4. (0,8): (1,6),(2,7),(2,9)... wait (0,8): attacks (0±1,8±2)=(1,6),(1,10)off,(−1,6)off; (0±2,8±1)=(2,7),(2,9). So (1,6),(2,7),(2,9) = 3 squares. Hmm, (0,8) is not a corner but near corner. Let me recount: (0,8): (1,6),(1,10)✗,(2,7),(2,9),(-1,6)✗,(-1,10)✗,(-2,7)✗,(-2,9)✗. So attacks (1,6),(2,7),(2,9) = 3 squares.

This is getting complicated. Let me try to think about the problem from a higher level.

I recall that for this type of problem on an n×n board, the answer is often around n²/3 or similar. For 10×10, that would be around 33.

Let me try to think about a good construction.

Construction attempt: Place knights on a "grid" with spacing 3.

Consider white squares (r,c) with r+c even. Place knights where r ≡ 0 (mod 3) and c ≡ 0 (mod 3), but only if r+c even.

r ∈ {0,3,6,9}, c ∈ {0,3,6,9}. White ones (r+c even): (0,0),(0,6),(3,3),(3,9),(6,0),(6,6),(9,3),(9,9). That's 8.

Check conflicts:
(0,0) vs (0,6): |Δr|=0,|Δc|=6. Safe (need |Δc|∉{2,4}, 6∉{2,4} ✓).
(0,0) vs (3,3): |Δr|=3,|Δc|=3. Conflict! (|Δr|=3,|Δc|∈{1,3} → 3∈{1,3} ✓ conflict).

So this doesn't work. The spacing of 3 causes conflicts.

Let me try spacing 4. r ≡ 0 (mod 4), c ≡ 0 (mod 4), white only.
r ∈ {0,4,8}, c ∈ {0,4,8}. White: (0,0),(0,8),(4,4),(8,0),(8,8). 5 knights.

(0,0) vs (4,4): |Δr|=4,|Δc|=4. Conflict? |Δr|=4, overlap iff |Δc|∈{0,2}. 4∉{0,2}. Safe!
(0,0) vs (0,8): |Δr|=0,|Δc|=8. Safe.
(0,0) vs (8,0): |Δr|=8. Safe.
(0,0) vs (8,8): |Δr|=8. Safe.
(0,8) vs (4,4): |Δr|=4,|Δc|=4. Safe.
(0,8) vs (8,0): |Δr|=8. Safe.
(0,8) vs (8,8): |Δr|=8. Safe.
(4,4) vs (8,0): |Δr|=4,|Δc|=4. Safe.
(4,4) vs (8,8): |Δr|=4,|Δc|=4. Safe.
(8,0) vs (8,8): |Δr|=0,|Δc|=8. Safe.

All safe! 5 white knights. But we can likely do much better.

The issue is that this grid is too sparse. Let me think about denser arrangements.

Let me try to think row by row. In each row, white squares are at specific columns. For row r, white columns are those c with r+c even.

Row 0: c ∈ {0,2,4,6,8} (5 white squares)
Row 1: c ∈ {1,3,5,7,9} (5 white squares)
Row 2: c ∈ {0,2,4,6,8}
Row 3: c ∈ {1,3,5,7,9}
Row 4: c ∈ {0,2,4,6,8}
Row 5: c ∈ {1,3,5,7,9}
Row 6: c ∈ {0,2,4,6,8}
Row 7: c ∈ {1,3,5,7,9}
Row 8: c ∈ {0,2,4,6,8}
Row 9: c ∈ {1,3,5,7,9}

Within a single row, two white knights conflict iff |Δc|∈{2,4}. So in row 0 (columns 0,2,4,6,8), we can't have two knights at distance 2 or 4. The allowed distances are 6, 8. So we can place at most 2 knights in a row (e.g., at columns 0 and 8, or 0 and 6).

Actually, columns 0,2,4,6,8: pairs with |Δc|∈{2,4}: (0,2),(0,4),(2,4),(2,6),(4,6),(4,8),(6,8) all conflict. Pairs with |Δc|=6: (0,6),(2,8) - safe. Pairs with |Δc|=8: (0,8) - safe.

So in one row, we can pick at most 2 columns from {0,2,4,6,8} such that no pair has |Δc|∈{2,4}. E.g., {0,6}: |Δc|=6 ✓. {0,8}: |Δc|=8 ✓. {2,8}: |Δc|=6 ✓. Can we pick 3? {0,6,...}: 6 and any other even col in {0,2,4,6,8}: 6 vs 0 ✓, 6 vs 2 (|Δc|=4 ✗), 6 vs 4 (|Δc|=2 ✗), 6 vs 8 (|Δc|=2 ✗). So {0,6} can't be extended. {0,8}: 8 vs 2 (|Δc|=6 ✓), 8 vs 4 (|Δc|=4 ✗), 8 vs 6 (|Δc|=2 ✗). So {0,2,8}: check 0 vs 2 (|Δc|=2 ✗). No. {0,8} can add 2? 0 vs 2 = 2 ✗. Can't. So max 2 per row.

Wait, what about {2,8}? 2 vs 8 = 6 ✓. Can we add another? 0 vs 2 = 2 ✗, 0 vs 8 = 8 ✓ but 0 vs 2 fails. 4 vs 2 = 2 ✗. 6 vs 2 = 4 ✗, 6 vs 8 = 2 ✗. So no. Max 2 per row.

So within a single row, max 2 white knights. With 10 rows, that's at most 20. But cross-row conflicts reduce this.

Now, between adjacent rows (|Δr|=1), conflict iff |Δc|∈{1,3}. Since adjacent rows have white squares on opposite parity columns (row 0: even cols, row 1: odd cols), |Δc| is always odd. So conflict iff |Δc|∈{1,3}.

Row 0 has knights at even columns, row 1 at odd columns. If row 0 has knight at col 0 and row 1 has knight at col 1: |Δc|=1, conflict. At col 3: |Δc|=3, conflict. At col 5: |Δc|=5, safe. At col 7: |Δc|=7, safe. At col 9: |Δc|=9, safe.

So if row 0 has a knight at col 0, row 1 can have knights at cols {5,7,9} (from odd cols {1,3,5,7,9}, excluding 1,3). But within row 1, we also need |Δc|∉{2,4} among the chosen. {5,7,9}: 5 vs 7 = 2 ✗, 5 vs 9 = 4 ✗, 7 vs 9 = 2 ✗. So at most 1 from {5,7,9} in row 1 if row 0 has a knight at col 0.

Hmm, this is getting very complex. Let me try to think about it as an optimization problem and try to find good constructions.

Let me try a pattern where I place knights in a "staggered" fashion.

Pattern attempt 1: Place knights at (r, c) where c = 2r mod 10 (or something like that)... this is hard to reason about.

Let me try a different approach. Let me think about the problem as placing knights on a coarser grid.

Consider the transformation: map white square (r,c) to (⌊r/2⌋, ⌊c/2⌋) or something. Actually, let me think about the white squares as a 5×10 "half-grid."

Hmm, actually, the white squares can be thought of as follows: in even rows (0,2,4,6,8), white squares are at even columns (0,2,4,6,8), and in odd rows (1,3,5,7,9), white squares are at odd columns (1,3,5,7,9).

Let me use a coordinate transform. For even row r=2i (i=0,...,4), white columns are 2j (j=0,...,4). For odd row r=2i+1 (i=0,...,4), white columns are 2j+1 (j=0,...,4).

So white squares are parametrized by (i,j) where:
- Even rows: (2i, 2j), i,j ∈ {0,1,2,3,4}
- Odd rows: (2i+1, 2j+1), i,j ∈ {0,1,2,3,4}

This gives 25 + 25 = 50 white squares. Good.

Now let me re-express the conflict conditions in terms of these coordinates.

Two white squares, one at (r1,c1) and one at (r2,c2).

Case 1: Both in even rows. r1=2i1, r2=2i2, c1=2j1, c2=2j2.
Δr = 2|i1-i2|, Δc = 2|j1-j2|.
- |Δr|=0 (i1=i2): conflict iff |Δc|∈{2,4} iff 2|j1-j2|∈{2,4} iff |j1-j2|∈{1,2}.
- |Δr|=2 (|i1-i2|=1): conflict iff |Δc|∈{0,2,4} iff |j1-j2|∈{0,1,2}.
- |Δr|=4 (|i1-i2|=2): conflict iff |Δc|∈{0,2} iff |j1-j2|∈{0,1}.
- |Δr|≥6 (|i1-i2|≥3): safe.

Case 2: Both in odd rows. r1=2i1+1, r2=2i2+1, c1=2j1+1, c2=2j2+1.
Same as case 1 (differences are the same). So:
- |i1-i2|=0: conflict iff |j1-j2|∈{1,2}.
- |i1-i2|=1: conflict iff |j1-j2|∈{0,1,2}.
- |i1-i2|=2: conflict iff |j1-j2|∈{0,1}.
- |i1-i2|≥3: safe.

Case 3: One even, one odd. r1=2i1, c1=2j1; r2=2i2+1, c2=2j2+1.
Δr = |2i1 - 2i2 - 1| = |2(i1-i2) - 1|, which is odd.
Δc = |2j1 - 2j2 - 1|, which is odd.

- |Δr|=1: |2(i1-i2)-1|=1, so i1=i2 or i1=i2+1. If i1=i2: Δr=1. If i1=i2+1: Δr=1. Conflict iff |Δc|∈{1,3}. |Δc|=|2(j1-j2)-1|. If j1=j2: |Δc|=1. If j1=j2±1: |Δc|=1 or 3. Specifically: j1=j2 → 1; j1=j2+1 → |2-1|=1; j1=j2-1 → |-2-1|=3; j1=j2+2 → |4-1|=3; j1=j2-2 → |-4-1|=5. So |Δc|∈{1,3} iff |j1-j2|∈{0,1,2}.
  - i1=i2: conflict iff |j1-j2|∈{0,1,2}.
  - i1=i2+1 (i.e., i1-i2=1): Δr=|2-1|=1. Same: conflict iff |j1-j2|∈{0,1,2}.
  
  Wait, I need to be more careful. Δr=1 when |2(i1-i2)-1|=1, which gives 2(i1-i2)-1=±1, so i1-i2=0 or i1-i2=1.

- |Δr|=3: |2(i1-i2)-1|=3, so 2(i1-i2)-1=±3, i1-i2=2 or i1-i2=-1. Conflict iff |Δc|∈{1,3}. Same analysis: |j1-j2|∈{0,1,2}.

- |Δr|=5: |2(i1-i2)-1|=5, i1-i2=3 or i1-i2=-2. |Δr|≥5, safe.

So for even-odd pairs:
- |i1-i2|∈{0,1} (Δr=1): conflict iff |j1-j2|∈{0,1,2}.
- |i1-i2|∈{-1,2} (Δr=3): conflict iff |j1-j2|∈{0,1,2}.

Wait, let me redo. i1-i2=0 → Δr=1. i1-i2=1 → Δr=1. i1-i2=-1 → Δr=3. i1-i2=2 → Δr=3. i1-i2=-2 → Δr=5. i1-i2=3 → Δr=5.

So:
- |i1-i2|∈{0,1}: Δr=1, conflict iff |j1-j2|∈{0,1,2}.
- |i1-i2|∈{1,2} but with i1-i2=-1 or 2: Δr=3, conflict iff |j1-j2|∈{0,1,2}.

Hmm wait, |i1-i2|=1 could be i1-i2=1 (Δr=1) or i1-i2=-1 (Δr=3). Both give conflict iff |j1-j2|∈{0,1,2}.

|i1-i2|=0: Δr=1, conflict iff |j1-j2|∈{0,1,2}.
|i1-i2|=1: Δr∈{1,3}, conflict iff |j1-j2|∈{0,1,2}.
|i1-i2|=2: Δr∈{3,5}. If i1-i2=2: Δr=3, conflict iff |j1-j2|∈{0,1,2}. If i1-i2=-2: Δr=5, safe.
|i1-i2|=3: Δr∈{5,7}. Safe.
|i1-i2|=4: Δr∈{7,9}. Safe.

So for even-odd pairs, conflict iff |i1-i2|∈{0,1,2} (with the caveat that |i1-i2|=2 only conflicts in one direction, but since we consider absolute differences, let me re-examine).

Actually, since i1 is from the even-row set and i2 from the odd-row set, and both range over {0,1,2,3,4}:

If i1-i2 = 2: Δr = |2·2-1| = 3. Conflict iff |j1-j2|∈{0,1,2}.
If i1-i2 = -2: Δr = |2·(-2)-1| = 5. Safe.

So it's not symmetric in i1-i2! The even-row index and odd-row index play asymmetric roles.

Let me restate: for an even-row white square at (2i1, 2j1) and an odd-row white square at (2i2+1, 2j2+1):
- Δr = |2i1 - (2i2+1)| = |2(i1-i2) - 1|
- Δc = |2j1 - (2j2+1)| = |2(j1-j2) - 1|

Conflict conditions:
- Δr=1 (i1-i2 ∈ {0,1}): conflict iff Δc∈{1,3} iff (j1-j2) ∈ {0,1,2,-1,-2}... 

Actually Δc = |2(j1-j2)-1|. For j1-j2=0: Δc=1. j1-j2=1: Δc=1. j1-j2=-1: Δc=3. j1-j2=2: Δc=3. j1-j2=-2: Δc=5. j1-j2=3: Δc=5. j1-j2=-3: Δc=7. j1-j2=4: Δc=7. j1-j2=-4: Δc=9.

So Δc∈{1,3} iff j1-j2 ∈ {-2,-1,0,1,2}, i.e., |j1-j2|∈{0,1,2}.

And Δr=1 iff i1-i2∈{0,1}. Δr=3 iff i1-i2∈{-1,2}. Δr=5 iff i1-i2∈{-2,3}. Δr=7 iff i1-i2∈{-3,4}. Δr=9 iff i1-i2∈{-4}.

Conflict (Δr∈{1,3} and Δc∈{1,3}): 
- i1-i2∈{0,1,-1,2} and |j1-j2|∈{0,1,2}.

No conflict if i1-i2∈{-2,3,-3,4,-4} (i.e., |i1-i2|≥2 with i1>i2+1 or i1<i2-1... this is getting messy).

Let me simplify. The even-row knight at (2i1, 2j1) and odd-row knight at (2i2+1, 2j2+1) conflict iff:
- i1-i2 ∈ {0, 1, -1, 2} AND |j1-j2| ∈ {0, 1, 2}

Equivalently, |i1-i2| ≤ 2 (with the specific constraint that i1-i2 ∈ {-1,0,1,2}) AND |j1-j2| ≤ 2.

Note that i1-i2 ∈ {-1,0,1,2} means i1 ∈ [i2-1, i2+2]. Since both range over {0,...,4}, this is almost always satisfied unless they're far apart.

For i1-i2 = -2 (i.e., i1 = i2-2): no conflict (Δr=5).
For i1-i2 = 3 (i.e., i1 = i2+3): no conflict (Δr=5).

So the even-row and odd-row knights conflict iff i1 ∈ [i2-1, i2+2] and |j1-j2| ≤ 2. They're safe if i1 ≤ i2-3 or i1 ≥ i2+3, or if |j1-j2| ≥ 3.

OK this is very complex. Let me try to just find a good construction and then prove an upper bound.

Let me try to think about this problem from the perspective of known results. I believe this is a competition problem, possibly from a Chinese math competition or similar.

Let me try to construct a solution with 32 knights (16 per color).

Actually, let me try a cleaner approach. Let me think about the problem on the full 10×10 board without the color decomposition, and try to find patterns.

Pattern: Place knights on a 4×4 sub-grid pattern. Divide the 10×10 board into blocks and place knights strategically.

Actually, let me try the following construction. Place knights at positions (r, c) where:
- r ≡ 0 (mod 5) and c is even, or
- r ≡ 2 (mod 5) and c is odd, or
- r ≡ 4 (mod 5) and c is even

Wait, I need to be more systematic. Let me try to think about what the answer is.

Let me try to get an upper bound first.

Upper bound via counting: We showed the problem decomposes into two colors. For one color (50 squares), we place knights such that attack sets (on the other 50 squares) are disjoint. Sum of attack set sizes ≤ 50.

Now, what's the minimum attack set size for a knight on a white square? Corner white squares (0,0) and (9,9) have 2 attacks. But there are only 2 such squares per color.

Let me count the attack set sizes for all white squares:
- (0,0): 2 attacks
- (0,8): Let me compute. (0,8) attacks (1,6),(2,7),(2,9). That's 3.
  Wait, (0,8): (0+1,8+2)=(1,10)✗, (0+1,8-2)=(1,6)✓, (0-1,...)✗, (0+2,8+1)=(2,9)✓, (0+2,8-1)=(2,7)✓, (0-2,...)✗. So 3 attacks.
- (9,9): 2 attacks (by symmetry with (0,0))
- (9,1): by symmetry with (0,8)→ hmm, let me think. (9,1): (9-1,1+2)=(8,3)✓, (9-1,1-2)=(8,-1)✗, (9+1,...)✗, (9-2,1+1)=(7,2)✓, (9-2,1-1)=(7,0)✓. So 3 attacks.

Let me categorize white squares by attack set size:

The attack set size of a knight at (r,c) depends on how many of its 8 potential moves stay on the board.

For a 10×10 board (0-9):
- Corners (0,0),(0,9),(9,0),(9,9): 2 moves. White corners: (0,0),(9,9).
- Near-corners: squares adjacent to corner along edge. (0,1),(1,0) have 3 moves; (0,8),(8,0),(1,9),(9,8) have 3 moves. White ones: (0,8) has 3, (8,0) has 3, (1,9)... 1+9=10 even, white, 3 moves. (9,8): 9+8=17 odd, black.

This is getting tedious. Let me just count by position type.

For a square at (r,c) on a 10×10 board, the number of valid knight moves is:
- From row r: can reach r±1 if 0≤r±1≤9, r±2 if 0≤r±2≤9.
- From col c: similarly.

The number of valid moves = (number of valid row offsets among {±1,±2}) × ... no, it's more nuanced. Each knight move is (±1,±2) or (±2,±1). A move (dr,dc) is valid if 0≤r+dr≤9 and 0≤c+dc≤9.

Let me define:
- r1+ = (r+1≤9), r1- = (r-1≥0), r2+ = (r+2≤9), r2- = (r-2≥0)
- c1+ = (c+1≤9), c1- = (c-1≥0), c2+ = (c+2≤9), c2- = (c-2≥0)

Number of moves = (r1+∧c2+) + (r1+∧c2-) + (r1-∧c2+) + (r1-∧c2-) + (r2+∧c1+) + (r2+∧c1-) + (r2-∧c1+) + (r2-∧c1-)

= (r1+)(c2+ + c2-) + (r1-)(c2+ + c2-) + (r2+)(c1+ + c1-) + (r2-)(c1+ + c1-)

where I'm using boolean arithmetic.

Let me define R1 = (r1+) + (r1-) = number of valid ±1 row moves (0,1,or 2)
R2 = (r2+) + (r2-) = number of valid ±2 row moves
C1 = (c1+) + (c1-) = number of valid ±1 col moves
C2 = (c2+) + (c2-) = number of valid ±2 col moves

Then number of moves = R1·C2 + R2·C1.

For a 10×10 board (0-9):
- r=0: R1=1 (only +1), R2=1 (only +2)
- r=1: R1=2, R2=1 (only +2, since 1-2=-1)
- r=2,...,7: R1=2, R2=2
- r=8: R1=2, R2=1 (only -2, since 8+2=10)
- r=9: R1=1, R2=1

Similarly for columns.

So:
- r=0 or 9: R1=1, R2=1
- r=1 or 8: R1=2, R2=1
- r=2,...,7: R1=2, R2=2

Number of moves = R1·C2 + R2·C1.

For white squares, let me enumerate by (row type, col type):

Row types: A (r=0,9): R1=1,R2=1; B (r=1,8): R1=2,R2=1; C (r=2-7): R1=2,R2=2.
Col types: same.

Moves = R1·C2 + R2·C1.

AA: 1·1 + 1·1 = 2
AB: 1·1 + 1·2 = 3 (row A, col B) or 2·1 + 1·1 = 3 (row B, col A). Same.
AC: 1·2 + 1·2 = 4 (row A, col C) or 2·2 + 1·1 = 5 (row C, col A). Different!

Hmm wait. Row A, Col C: R1=1,R2=1 (row), C2=2,C1=2 (col). Moves = 1·2 + 1·2 = 4.
Row C, Col A: R1=2,R2=2 (row), C2=1,C1=1 (col). Moves = 2·1 + 2·1 = 4. 

Oh wait, I made an error. Let me redo. Row C: R1=2, R2=2. Col A: C2=1, C1=1. Moves = R1·C2 + R2·C1 = 2·1 + 2·1 = 4. OK same.

BB: R1=2,R2=1, C2=1,C1=2. Moves = 2·1 + 1·2 = 4.
BC: Row B: R1=2,R2=1. Col C: C2=2,C1=2. Moves = 2·2 + 1·2 = 6. Row C, Col B: R1=2,R2=2, C2=1,C1=2. Moves = 2·1 + 2·2 = 6. Same.
CC: 2·2 + 2·2 = 8.

So attack set sizes:
- AA (corner): 2
- AB (edge near corner): 3
- AC (edge middle): 4
- BB (near-edge): 4
- BC (interior near edge): 6
- CC (center): 8

Now let me count white squares by type:

Row types for white squares:
- Row 0 (A): white cols 0,2,4,6,8. Col types: 0(A),2(C),4(C),6(C),8(B). So: 1A, 1B, 3C.
- Row 1 (B): white cols 1,3,5,7,9. Col types: 1(B),3(C),5(C),7(C),9(A). So: 1A, 1B, 3C.
- Row 2 (C): white cols 0,2,4,6,8. Col types: 0(A),2(C),4(C),6(C),8(B). So: 1A, 1B, 3C.
- Row 3 (C): same as row 2. 1A, 1B, 3C.
- Row 4 (C): same. 1A, 1B, 3C.
- Row 5 (C): white cols 1,3,5,7,9. Col types: 1(B),3(C),5(C),7(C),9(A). 1A, 1B, 3C.
- Row 6 (C): white cols 0,2,4,6,8. 1A, 1B, 3C.
- Row 7 (C): white cols 1,3,5,7,9. 1A, 1B, 3C.
- Row 8 (B): white cols 0,2,4,6,8. Col types: 0(A),2(C),4(C),6(C),8(B). 1A, 1B, 3C.
- Row 9 (A): white cols 1,3,5,7,9. Col types: 1(B),3(C),5(C),7(C),9(A). 1A, 1B, 3C.

So every row has 1A, 1B, 3C white squares.

Now, the (row type, col type) pairs for white squares:
- Row A (rows 0,9): 2 rows × (1A + 1B + 3C) = 2AA + 2AB + 6AC
- Row B (rows 1,8): 2 rows × (1A + 1B + 3C) = 2BA + 2BB + 6BC
- Row C (rows 2-7): 6 rows × (1A + 1B + 3C) = 6CA + 6CB + 18CC

Attack set sizes:
- AA: 2 → 2 squares
- AB: 3 → 2 squares
- AC: 4 → 6 squares
- BA: 3 → 2 squares (same as AB by symmetry)
- BB: 4 → 2 squares
- BC: 6 → 6 squares
- CA: 4 → 6 squares
- CB: 6 → 6 squares
- CC: 8 → 18 squares

Total: 2+2+6+2+2+6+6+6+18 = 50 ✓

Now, for the upper bound: if we place k white knights with disjoint attack sets, sum of attack sizes ≤ 50. To maximize k, we want to use squares with small attack sets.

If we use all AA (2 squares, 2 attacks each): 2 knights, 4 attacks.
AB+BA (4 squares, 3 attacks each): 4 knights, 12 attacks.
AC+CA (12 squares, 4 attacks each): 12 knights, 48 attacks.
BB (2 squares, 4 attacks): 2 knights, 8 attacks.
BC+CB (12 squares, 6 attacks): 12 knights, 72 attacks.
CC (18 squares, 8 attacks): 18 knights, 144 attacks.

If we only use squares with ≤ 4 attacks (AA, AB, BA, AC, CA, BB): 2+4+12+2 = 20 squares, total attacks = 4+12+48+8 = 72 > 50. So we can't use all of them.

To maximize knights with total attacks ≤ 50:
- Use all 2-attack squares (AA): 2 knights, 4 attacks.
- Use all 3-attack squares (AB, BA): 4 knights, 12 attacks. Running total: 6 knights, 16 attacks.
- Use 4-attack squares (AC, CA, BB): 14 squares available, each 4 attacks. We can use at most ⌊(50-16)/4⌋ = ⌊34/4⌋ = 8 more. Total: 14 knights, 16+32 = 48 attacks.
- Could we fit one more 6-attack? 48+6=54 > 50. No. One more 4-attack? 48+4=52 > 50. No.

So upper bound from counting: at most 14 white knights (2+4+8), giving 28 total.

But wait, this assumes we can actually achieve disjoint attack sets with these choices. The counting bound is necessary but not sufficient. Also, I assumed we use the smallest attack sets, but the disjointness constraint might force us to use larger attack sets or might prevent us from using certain small-attack squares.

Hmm, but actually the counting bound gives us: k knights, sum of attacks ≤ 50. The minimum possible sum for k knights is achieved by using the k squares with smallest attack sets. Let me sort:

2 attacks: 2 squares (AA)
3 attacks: 4 squares (AB, BA)
4 attacks: 14 squares (AC, CA, BB)
6 attacks: 12 squares (BC, CB)
8 attacks: 18 squares (CC)

For k knights, minimum total attacks:
k=2: 2×2=4
k=6: 2×2+4×3=16
k=14: 16+8×4=48
k=15: 48+4=52 > 50. 

So k ≤ 14 for one color, giving total ≤ 28.

But can we actually achieve 14? That requires using all 2-attack and 3-attack squares (6 knights) plus 8 of the 4-attack squares, with all attack sets disjoint. This seems very hard to achieve because the small-attack squares are on the edges and their attack sets might overlap.

Let me check: the 2-attack squares are (0,0) and (9,9). (0,0) attacks (1,2),(2,1). (9,9) attacks (8,7),(7,8). These are disjoint. Good.

The 3-attack squares: (0,8) attacks (1,6),(2,7),(2,9). (8,0) attacks (6,1),(7,2),(9,1)... wait let me recompute. (8,0): (8+1,0+2)=(9,2), (8+1,0-2)✗, (8-1,0+2)=(7,2), (8-1,0-2)✗, (8+2,0+1)✗, (8+2,0-1)✗, (8-2,0+1)=(6,1), (8-2,0-1)✗. So (9,2),(7,2),(6,1). 

(1,9): (1+1,9+2)✗,(1+1,9-2)=(2,7),(1-1,9+2)✗,(1-1,9-2)=(0,7),(1+2,9+1)✗,(1+2,9-1)=(3,8),(1-2,...)✗. So (2,7),(0,7),(3,8).

(9,1): (9-1,1+2)=(8,3),(9-1,1-2)✗,(9+1,...)✗,(9-2,1+1)=(7,2),(9-2,1-1)=(7,0). So (8,3),(7,2),(7,0).

Now check overlaps among 3-attack squares:
(0,8) attacks {(1,6),(2,7),(2,9)}
(8,0) attacks {(9,2),(7,2),(6,1)}
(1,9) attacks {(2,7),(0,7),(3,8)}
(9,1) attacks {(8,3),(7,2),(7,0)}

(0,8) and (1,9): both attack (2,7)! Conflict!

So we can't use both (0,8) and (1,9). This means the counting bound of 14 is not achievable.

This is getting really complex. Let me step back and think about whether there's a cleaner approach.

Let me reconsider the problem. Maybe I should think about it as a graph theory problem and look for the answer directly.

Actually, let me reconsider. The problem says "each square on the board can be attacked by at most one knight." I want to make sure I'm interpreting this correctly. A square is "attacked" by a knight if the knight can move to that square (i.e., it's a knight's move away). The square where a knight sits is not attacked by that knight (a knight doesn't attack its own square). But it could be attacked by another knight.

So the condition is: for every square s (whether occupied or not), the number of knights that are a knight's move away from s is at most 1.

This is exactly the open packing condition I described.

Let me try to look at this from a different angle. 

Consider the 10×10 board. A knight's move changes the sum of coordinates by ±1 or ±3. So a knight on a white square (even sum) attacks black squares (odd sum), and vice versa.

As I established, the problem decomposes into two independent subproblems (white knights attacking black squares, black knights attacking white squares). The answer is 2 × (max for one color).

For one color, I need to find the maximum open packing of the "knight graph restricted to white squares attacking black squares."

Let me try a computational approach in my head. Let me try to construct a good solution.

Construction attempt: Let me try to place knights on a pattern with period 5.

Consider placing white knights at positions (r, c) where r ∈ {0, 4, 8} (even rows, well-spaced) and c chosen appropriately.

Wait, let me try a different approach. Let me think about the conflict graph more carefully and try to find a large independent set.

From the analysis, two white knights conflict (share an attacked square) iff they're "close" in a specific sense. The safe pairs are those that are far apart.

Let me try to tile the board with a pattern that avoids conflicts.

Key observation: if two white knights are at (r1,c1) and (r2,c2) with |r1-r2| ≥ 5, they never conflict. So I can handle rows {0,1,2,3,4} and rows {5,6,7,8,9} independently (since the minimum row difference between these groups is |4-5|=1, which is < 5, so they're NOT independent). Hmm, that doesn't work.

Wait, actually |r1-r2| ≥ 5 means rows differ by at least 5. Rows 0-4 and rows 5-9: the closest pair is (4,5) with difference 1. So they're not independent.

But rows 0-4 and rows 5-9 with a gap: if I use rows {0,1,2} and rows {7,8,9}, then the minimum difference is |2-7|=5, so these are independent. But I'm leaving out rows 3,4,5,6.

Hmm, let me think about this differently. Let me try to find the maximum by considering specific constructions.

Construction 1: "Every other row, every 6th column."

Place knights in rows 0, 2, 4, 6, 8 (even rows, white squares at even columns). In each row, place knights at columns 0 and 6 (distance 6, safe within row).

Knights: (0,0),(0,6),(2,0),(2,6),(4,0),(4,6),(6,0),(6,6),(8,0),(8,6). 10 knights.

Check cross-row conflicts:
(0,0) vs (2,0): |Δr|=2,|Δc|=0. Conflict! (|Δr|=2, |Δc|∈{0,2,4}, 0∈{0,2,4}).

So this doesn't work. Knights in rows differing by 2 with same column conflict.

Construction 2: "Rows 0, 4, 8, columns 0 and 6."

(0,0),(0,6),(4,0),(4,6),(8,0),(8,6). 6 knights.

(0,0) vs (4,0): |Δr|=4,|Δc|=0. Conflict! (|Δr|=4, |Δc|∈{0,2}, 0∈{0,2}).

Still conflicts. The issue is that same-column knights in rows differing by 4 conflict.

Construction 3: "Rows 0, 4, 8, staggered columns."

Row 0: cols 0, 6. Row 4: cols 2, 8. Row 8: cols 0, 6.

(0,0),(0,6),(4,2),(4,8),(8,0),(8,6). 6 knights.

(0,0) vs (4,2): |Δr|=4,|Δc|=2. Conflict! (|Δr|=4, |Δc|∈{0,2}, 2∈{0,2}).

Hmm. For |Δr|=4, we need |Δc|∉{0,2}, so |Δc|∈{4,6,8}. 

Construction 4: "Rows 0, 4, 8, columns offset by 4."

Row 0: cols 0, 8. Row 4: cols 4. Row 8: cols 0, 8.

Wait, row 0 white cols: 0,2,4,6,8. Row 4 white cols: 0,2,4,6,8. Row 8 white cols: 0,2,4,6,8.

(0,0),(0,8),(4,4),(8,0),(8,8). 5 knights.

(0,0) vs (4,4): |Δr|=4,|Δc|=4. Safe (4∉{0,2}).
(0,0) vs (8,0): |Δr|=8. Safe.
(0,0) vs (8,8): |Δr|=8. Safe.
(0,8) vs (4,4): |Δr|=4,|Δc|=4. Safe.
(0,8) vs (8,0): |Δr|=8. Safe.
(0,8) vs (8,8): |Δr|=8. Safe.
(4,4) vs (8,0): |Δr|=4,|Δc|=4. Safe.
(4,4) vs (8,8): |Δr|=4,|Δc|=4. Safe.
(8,0) vs (8,8): |Δr|=0,|Δc|=8. Safe.

All safe! 5 white knights. But this is low. Can we do better?

Let me try to add more knights. Can I add knights in other rows?

Add (2, c) for some c. (2,c) is white if c even. 
(2,c) vs (0,0): |Δr|=2, need |Δc|∉{0,2,4}, so |Δc|∈{6,8}. c ∈ {6,8} (from even cols 0,2,4,6,8, with |c-0|∈{6,8}: c=6 or 8).
(2,c) vs (0,8): |Δr|=2, need |Δc|∉{0,2,4}, so |Δc|∈{6,8}. |c-8|∈{6,8}: c=0 or 2.
(2,c) vs (4,4): |Δr|=2, need |Δc|∉{0,2,4}. |c-4|∈{6,8}: c=... |c-4|≥6: c≥10 (impossible) or c≤-2 (impossible). So no valid c!

So we can't add any knight in row 2 because (4,4) blocks everything (|Δr|=2 requires |Δc|≥6, but max |c-4| on the board is 4).

Similarly, row 6 is blocked by (4,4).

What about odd rows? (1,c) white if c odd. 
(1,c) vs (0,0): |Δr|=1, need |Δc|∉{1,3}, so |Δc|∈{5,7,9}. |c-0|∈{5,7,9}: c∈{5,7,9}.
(1,c) vs (0,8): |Δr|=1, need |Δc|∉{1,3}. |c-8|∈{5,7,9}: c∈{1,3}. But we need c∈{5,7,9} ∩ {1,3} = ∅. 

So no knight in row 1 either (blocked by (0,0) and (0,8) together).

This construction is too sparse. The problem is that (0,0) and (0,8) together block most of rows 1 and 2, and (4,4) blocks the rest.

Let me try a different approach entirely. Let me think about what patterns could give a high density.

Idea: Use a "knight's tour" like pattern, or think about the problem as a coding theory problem.

Actually, let me reconsider the structure. The conflict graph on white squares has edges between "close" pairs. I want the maximum independent set.

Let me think about the white squares as a 5×5 grid of "even" squares and a 5×5 grid of "odd" squares (using the (i,j) parametrization from before).

Even squares: E(i,j) = (2i, 2j), i,j ∈ {0,1,2,3,4}.
Odd squares: O(i,j) = (2i+1, 2j+1), i,j ∈ {0,1,2,3,4}.

Conflicts within E (or within O): 
- Same i (same row pair): |j1-j2|∈{1,2} → conflict.
- |i1-i2|=1: |j1-j2|∈{0,1,2} → conflict.
- |i1-i2|=2: |j1-j2|∈{0,1} → conflict.
- |i1-i2|≥3: safe.

Conflicts between E and O:
E(i1,j1) and O(i2,j2): conflict iff i1-i2 ∈ {-1,0,1,2} and |j1-j2| ∈ {0,1,2}.

Note: the condition is asymmetric. Let me also check O(i1,j1) vs E(i2,j2):
O at (2i1+1, 2j1+1), E at (2i2, 2j2). Δr = |2i1+1-2i2| = |2(i1-i2)+1|. 
- i1-i2=0: Δr=1. Conflict iff Δc∈{1,3}. Δc=|2j1+1-2j2|=|2(j1-j2)+1|. |j1-j2|=0→1, =1→1 or 3, =2→3 or 5. So Δc∈{1,3} iff |j1-j2|∈{0,1,2}.
- i1-i2=1: Δr=3. Same: conflict iff |j1-j2|∈{0,1,2}.
- i1-i2=-1: Δr=1. Same.
- i1-i2=2: Δr=5. Safe.
- i1-i2=-2: Δr=3. Conflict iff |j1-j2|∈{0,1,2}.

So O(i1,j1) vs E(i2,j2): conflict iff i1-i2 ∈ {-2,-1,0,1} and |j1-j2|∈{0,1,2}.

Compare with E(i1,j1) vs O(i2,j2): conflict iff i1-i2 ∈ {-1,0,1,2} and |j1-j2|∈{0,1,2}.

These are different! E vs O: i_E - i_O ∈ {-1,0,1,2}. O vs E: i_O - i_E ∈ {-2,-1,0,1}, i.e., i_E - i_O ∈ {-1,0,1,2}. Wait:

O(i1,j1) vs E(i2,j2): i1-i2 ∈ {-2,-1,0,1}. This means i_O - i_E ∈ {-2,-1,0,1}, or equivalently i_E - i_O ∈ {-1,0,1,2}.

E(i1,j1) vs O(i2,j2): i1-i2 ∈ {-1,0,1,2}. This means i_E - i_O ∈ {-1,0,1,2}.

So both give the same condition: i_E - i_O ∈ {-1,0,1,2}. Good, it's symmetric after all (just the direction of the difference matters, but the set {-1,0,1,2} is the same).

Wait, no. E vs O: i_E - i_O ∈ {-1,0,1,2}. O vs E: i_O - i_E ∈ {-2,-1,0,1}, which is i_E - i_O ∈ {-1,0,1,2}. Yes, same condition. Good.

So the conflict between E(i_E, j_E) and O(i_O, j_O) is: i_E - i_O ∈ {-1,0,1,2} AND |j_E - j_O| ∈ {0,1,2}.

Equivalently: |i_E - i_O| ≤ 2 (but not i_E - i_O = -2, i.e., not i_E = i_O - 2) AND |j_E - j_O| ≤ 2.

Hmm, the asymmetry is that i_E - i_O = -2 (i_E = i_O - 2) is safe, but i_E - i_O = 2 (i_E = i_O + 2) is not. This is because the even rows are at 0,2,4,6,8 and odd rows at 1,3,5,7,9. E(i) is at row 2i, O(i) is at row 2i+1. So E(i_E) at row 2i_E and O(i_O) at row 2i_O+1. Δr = |2i_E - 2i_O - 1| = |2(i_E - i_O) - 1|.

If i_E - i_O = 2: Δr = |4-1| = 3. Conflict possible.
If i_E - i_O = -2: Δr = |-4-1| = 5. Safe.

So the asymmetry comes from the fact that even and odd rows are interleaved, and the "distance" depends on direction.

OK, this is a complex combinatorial optimization. Let me try to think about it more cleverly.

Let me try to find the answer by considering a specific good construction.

Construction idea: "Checkerboard of 3×3 blocks."

Divide the 5×5 grid of even squares into blocks. In each 3×3 block of the (i,j) grid, place one knight. But 5/3 doesn't divide evenly.

Let me try another approach. Let me think about the problem on the (i,j) grid for even squares only first, ignoring odd squares.

Within even squares E, conflicts are:
- |Δi|=0: |Δj|∈{1,2} conflict.
- |Δi|=1: |Δj|∈{0,1,2} conflict.
- |Δi|=2: |Δj|∈{0,1} conflict.
- |Δi|≥3: safe.

This is like a graph where each node conflicts with nodes in a 5×5 neighborhood (roughly). The maximum independent set in a 5×5 grid with this conflict structure...

If |Δi|≥3 is safe, then I can handle rows {0,1,2} and {3,4} independently (since |2-3|=1 < 3, not independent). Hmm, no. |Δi|≥3 means rows 0 and 3,4 are safe. But rows 0,1,2 interact with each other and with row 3 (|Δi|=2 for row 1 vs 3, |Δi|=1 for row 2 vs 3).

Actually, rows 0 and 3: |Δi|=3, safe. Rows 0 and 4: |Δi|=4, safe. So row 0 is safe with rows 3,4. Row 1: safe with row 4 (|Δi|=3). Row 2: safe with nothing in {3,4} (|2-3|=1, |2-4|=2, both conflict).

So I could split: {0,1,2} and {3,4}, but row 2 conflicts with rows 3,4. Not independent.

Alternatively: {0,1} and {3,4}, with row 2 separate. Row 0 vs 3,4: safe. Row 1 vs 4: safe. Row 1 vs 3: |Δi|=2, conflict possible. So {0,1} and {3,4} are not independent either (row 1 vs row 3).

Hmm. Let me try: {0,1} and {4}. Row 0 vs 4: safe. Row 1 vs 4: safe. So {0,1} and {4} are independent. Then rows 2,3 are separate.

This is getting complicated. Let me just try to directly construct a good solution.

Let me try to place knights on even squares only (ignoring odd squares for now) and see how many I can get.

Even squares E(i,j), i,j ∈ {0,1,2,3,4}. I want to select a subset with no conflicts.

Conflict: |Δi|=0 ∧ |Δj|∈{1,2}; |Δi|=1 ∧ |Δj|∈{0,1,2}; |Δi|=2 ∧ |Δj|∈{0,1}.

Let me try to place one knight per row of i, choosing j values carefully.

Row i=0: place at j=0. 
Row i=1: need |Δj|∉{0,1,2} from j=0, so j∈{3,4}. Place at j=3.
Row i=2: need |Δj|∉{0,1} from j=0 (|Δi|=2), and |Δj|∉{0,1,2} from j=3 (|Δi|=1). From j=0: j∉{0,1}, so j∈{2,3,4}. From j=3: j∉{1,2,3,4,5}, so j∈{0}. Intersection: {2,3,4} ∩ {0} = ∅. 

Can't place in row 2. Skip.
Row i=3: need |Δj|∉{0,1,2} from j=3 (|Δi|=2), so j∉{1,2,3,4,5}, j∈{0}. Need |Δj|∉{0,1} from j=0 (|Δi|=3, safe). So j=0 works. Place at j=0.
Row i=4: need |Δj|∉{0,1} from j=0 (|Δi|=4, safe). Need |Δj|∉{0,1,2} from j=3 (|Δi|=3, safe). Need |Δj|∉{0,1} from j=0 at i=3 (|Δi|=1, need |Δj|∉{0,1,2}). j=0 at i=3: |Δj|∉{0,1,2} from j=0, so j∈{3,4}. Place at j=3 or 4.

So: E(0,0), E(1,3), E(3,0), E(4,3). 4 knights from even squares.

Can I do better? Let me try a different pattern.

Row i=0: j=0 and j=4 (|Δj|=4, safe within row since |Δj|∉{1,2}).
Row i=1: from j=0, need |Δj|∉{0,1,2}, j∈{3,4}. From j=4, need |Δj|∉{0,1,2}, j∈{0,1}. Intersection: {3,4}∩{0,1}=∅. Can't place in row 1.

Row i=2: from j=0 (|Δi|=2), need |Δj|∉{0,1}, j∈{2,3,4}. From j=4 (|Δi|=2), need |Δj|∉{0,1}, j∈{0,1,2}. Intersection: {2,3,4}∩{0,1,2}={2}. Place at j=2.

Row i=3: from j=0 (|Δi|=3, safe). From j=4 (|Δi|=3, safe). From j=2 (|Δi|=1), need |Δj|∉{0,1,2}, j∈{} (|j-2|≥3 → j≥5 or j≤-1, impossible). Can't place.

Row i=4: from j=0 (|Δi|=4, safe). From j=4 (|Δi|=4, safe). From j=2 (|Δi|=2), need |Δj|∉{0,1}, j∈{0,4}. Place at j=0 or j=4. But need to check within row: only one knight in this row, so fine. Place at j=0.

E(0,0), E(0,4), E(2,2), E(4,0). 4 knights. Same count.

Let me try yet another pattern.

Row i=0: j=0.
Row i=1: j=4 (|Δj|=4 from j=0, safe since |Δi|=1 needs |Δj|∉{0,1,2}, 4∉{0,1,2} ✓).
Row i=2: from j=0 (|Δi|=2, |Δj|∉{0,1}), j∈{2,3,4}. From j=4 (|Δi|=1, |Δj|∉{0,1,2}), j∈{0,1}. Intersection: ∅. Can't place.

Row i=3: from j=0 (|Δi|=3, safe). From j=4 (|Δi|=2, |Δj|∉{0,1}), j∈{0,1,2}. Place at j=0 or 1 or 2.
Row i=4: from j=0 (|Δi|=4, safe). From j=4 (|Δi|=3, safe). From j=0 at i=3 (|Δi|=1, |Δj|∉{0,1,2}), j∈{3,4}. Place at j=3 or 4.

E(0,0), E(1,4), E(3,0), E(4,3). 4 knights.

Hmm, I keep getting 4 from even squares. Let me try to get 5.

Row i=0: j=0.
Row i=1: skip.
Row i=2: j=4 (from j=0, |Δi|=2, |Δj|=4∉{0,1} ✓).
Row i=3: from j=0 (safe), from j=4 (|Δi|=1, |Δj|∉{0,1,2}), j∈{0,1}. Place at j=0.
Row i=4: from j=0 (safe), from j=4 (|Δi|=2, |Δj|∉{0,1}), j∈{0,1,2}. From j=0 at i=3 (|Δi|=1, |Δj|∉{0,1,2}), j∈{3,4}. Intersection of all: {3,4} ∩ {0,1,2} ∩ all = ∅. Can't place.

Still 3. Let me try:

Row i=0: j=2.
Row i=1: from j=2 (|Δi|=1, |Δj|∉{0,1,2}), j∈{} (|j-2|≥3 → j≥5 or j≤-1). Can't place.
Row i=2: from j=2 (|Δi|=2, |Δj|∉{0,1}), j∈{3,4}. Place at j=3.
Row i=3: from j=2 (|Δi|=3, safe). From j=3 (|Δi|=1, |Δj|∉{0,1,2}), j∈{} (|j-3|≥3 → j≥6 or j≤0, so j=0). Place at j=0.
Row i=4: from j=2 (safe). From j=3 (|Δi|=2, |Δj|∉{0,1}), j∈{0,1,5}→{0,1}. From j=0 (|Δi|=1, |Δj|∉{0,1,2}), j∈{3,4}. Intersection: {0,1}∩{3,4}=∅. Can't place.

3 knights. Worse.

Let me try to be smarter. Maybe I should place 2 knights in some rows.

Row i=0: j=0, j=4 (|Δj|=4, safe).
Row i=1: from j=0 (|Δj|∉{0,1,2}, j∈{3,4}), from j=4 (|Δj|∉{0,1,2}, j∈{0,1}). Intersection: ∅. Can't place.
Row i=2: from j=0 (|Δj|∉{0,1}, j∈{2,3,4}), from j=4 (|Δj|∉{0,1}, j∈{0,1,2}). Intersection: {2}. Place at j=2.
Row i=3: from j=0 (safe), from j=4 (safe), from j=2 (|Δi|=1, |Δj|∉{0,1,2}, j∈{} impossible). Can't place.
Row i=4: from j=0 (safe), from j=4 (safe), from j=2 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4}). Place at j=0 or 1 or 4. But j=0 conflicts with... wait, within row i=4, only one knight so far. But j=0: check with j=0 at i=0 (|Δi|=4, safe ✓) and j=4 at i=0 (|Δi|=4, safe ✓) and j=2 at i=2 (|Δi|=2, |Δj|=2, conflict! |Δj|∈{0,1} → 2∉{0,1} ✓ safe). Wait, |Δi|=2, conflict iff |Δj|∈{0,1}. |Δj|=|0-2|=2, 2∉{0,1}. Safe! So j=0 works.

E(0,0), E(0,4), E(2,2), E(4,0). Can I add E(4,4)? Check E(4,4) vs E(4,0): |Δi|=0, |Δj|=4. Safe (4∉{1,2}). E(4,4) vs E(0,4): |Δi|=4, safe. E(4,4) vs E(0,0): |Δi|=4, safe. E(4,4) vs E(2,2): |Δi|=2, |Δj|=2. Conflict iff |Δj|∈{0,1}. 2∉{0,1}. Safe!

So E(0,0), E(0,4), E(2,2), E(4,0), E(4,4). 5 knights! Let me verify all pairs:

(0,0)-(0,4): |Δi|=0,|Δj|=4. Safe ✓
(0,0)-(2,2): |Δi|=2,|Δj|=2. |Δj|∉{0,1}. Safe ✓
(0,0)-(4,0): |Δi|=4. Safe ✓
(0,0)-(4,4): |Δi|=4. Safe ✓
(0,4)-(2,2): |Δi|=2,|Δj|=2. Safe ✓
(0,4)-(4,0): |Δi|=4. Safe ✓
(0,4)-(4,4): |Δi|=4. Safe ✓
(2,2)-(4,0): |Δi|=2,|Δj|=2. Safe ✓
(2,2)-(4,4): |Δi|=2,|Δj|=2. Safe ✓
(4,0)-(4,4): |Δi|=0,|Δj|=4. Safe ✓

All safe! 5 even-square knights.

Can I add more? Let me try adding to row i=1 or i=3.

Row i=1: from E(0,0) (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). From E(0,4) (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). Intersection: ∅. Can't.

Row i=3: from E(2,2) (|Δi|=1, |Δj|∉{0,1,2}, j∈{} since |j-2|≥3 → j≥5 or j≤-1). Can't.

So 5 is the max for this pattern on even squares. Can I do better with a different pattern?

Let me try:
Row i=0: j=1.
Row i=1: from j=1 (|Δi|=1, |Δj|∉{0,1,2}, j∈{4}). Place at j=4.
Row i=2: from j=1 (|Δi|=2, |Δj|∉{0,1}, j∈{3,4}). From j=4 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). Intersection: ∅. Can't.
Row i=3: from j=1 (safe). From j=4 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,2}). Place at j=0.
Row i=4: from j=1 (safe). From j=4 (safe). From j=0 (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). Place at j=3 or 4. j=4: check with j=4 at i=1 (|Δi|=3, safe ✓). Place at j=4.

E(0,1), E(1,4), E(3,0), E(4,4). 4 knights. Less.

Let me try to get 6 on even squares.

Hmm, let me think about this more carefully. The 5×5 grid with the conflict structure... Let me think about what the maximum independent set is.

Actually, let me try a pattern where I use rows 0, 2, 4 (every other row) and within each row, use 2 well-separated columns.

Row 0: j=0, j=4 (safe, |Δj|=4).
Row 2: from j=0 (|Δi|=2, |Δj|∉{0,1}, j∈{2,3,4}). From j=4 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,2}). Intersection: {2}. Place at j=2. Can I place a second? j=2 is the only option. Just 1.
Row 4: from j=0 (safe), j=4 (safe), j=2 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4}). Place at j=0 and j=4. Check j=0 vs j=4: |Δj|=4, safe. Check j=0 vs j=2 at row 2: |Δi|=2, |Δj|=2, safe. Check j=4 vs j=2 at row 2: |Δi|=2, |Δj|=2, safe.

E(0,0), E(0,4), E(2,2), E(4,0), E(4,4). 5 knights. Same as before.

Can I use rows 1 and 3 as well?

Row 1: from E(0,0) (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). From E(0,4) (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). Intersection: ∅. Can't.

Row 3: from E(2,2) (|Δi|=1, |Δj|∉{0,1,2}, j∈{} impossible). Can't.

So 5 is the max with this approach. Let me try completely different patterns.

Pattern: 1 per row, 5 rows.

Row 0: j=0
Row 1: j=3 (|Δi|=1, |Δj|=3∉{0,1,2} ✓)
Row 2: from j=0 (|Δi|=2, |Δj|∉{0,1}, j∈{2,3,4}). From j=3 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0}). Intersection: ∅. Can't.

Row 0: j=0
Row 1: j=4 (|Δj|=4∉{0,1,2} ✓)
Row 2: from j=0 (j∈{2,3,4}). From j=4 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). ∅. Can't.

Row 0: j=1
Row 1: j=4 (|Δj|=3∉{0,1,2} ✓)
Row 2: from j=1 (|Δi|=2, |Δj|∉{0,1}, j∈{3,4}). From j=4 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). ∅. Can't.

It seems hard to get more than 5 on even squares. Let me try 2 in some rows and 0 in others.

Row 0: j=0, j=3. Wait, |Δj|=3, but for |Δi|=0, conflict iff |Δj|∈{1,2}. 3∉{1,2}. Safe! So j=0 and j=3 in same row.

Row 0: j=0, j=3.
Row 1: from j=0 (|Δj|∉{0,1,2}, j∈{3,4}). From j=3 (|Δj|∉{0,1,2}, j∈{0}). ∅. Can't.

Row 2: from j=0 (|Δi|=2, |Δj|∉{0,1}, j∈{2,3,4}). From j=3 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4,5}→{0,1,4}). Intersection: {4}. Place at j=4.

Row 3: from j=0 (safe). From j=3 (safe). From j=4 (|Δi|=1, |Δj|∉{0,1,2}, j∈{0,1}). Place at j=0 or 1.
j=0: check with j=0 at row 0 (|Δi|=3, safe ✓), j=3 at row 0 (|Δi|=3, safe ✓), j=4 at row 2 (|Δi|=1, |Δj|=4∉{0,1,2} ✓). Place at j=0.
Can I place a second in row 3? j=1: check with j=0 in row 3 (|Δj|=1, conflict! |Δi|=0, |Δj|∈{1,2}). No. So just j=0.

Row 4: from j=0 row 0 (safe), j=3 row 0 (safe), j=4 row 2 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,2}), j=0 row 3 (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). Intersection: {0,1,2}∩{3,4}=∅. Can't.

E(0,0), E(0,3), E(2,4), E(3,0). 4 knights. Less than 5.

Let me try:
Row 0: j=0, j=4.
Row 2: j=2 (as before).
Row 4: j=0, j=4.
= 5 knights.

Can I add to row 1 or 3? Already checked, no.

What about:
Row 0: j=1, j=4 (|Δj|=3, safe).
Row 1: from j=1 (|Δj|∉{0,1,2}, j∈{4}). From j=4 (|Δj|∉{0,1,2}, j∈{0,1}). ∅. Can't.
Row 2: from j=1 (|Δi|=2, |Δj|∉{0,1}, j∈{3,4}). From j=4 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,2}). ∅. Can't.

Hmm. Let me try:
Row 0: j=0.
Row 1: j=3.
Row 2: can't (shown above).
Row 3: from j=0 (safe), j=3 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4,5}→{0,1,4}). Place at j=0, j=1, or j=4.
  j=4: check with j=3 at row 1 (|Δi|=2, |Δj|=1, conflict! |Δj|∈{0,1}). No.
  j=0: check with j=3 at row 1 (|Δi|=2, |Δj|=3∉{0,1} ✓). Check with j=0 at row 0 (|Δi|=3, safe ✓). Place at j=0.
  j=1: check with j=3 at row 1 (|Δi|=2, |Δj|=2∉{0,1} ✓). Check with j=0 at row 0 (|Δi|=3, safe ✓). Place at j=1.
  Can I place both j=0 and j=1? |Δj|=1, |Δi|=0, conflict. No. Just one.
  Let's say j=1.

Row 4: from j=0 row 0 (safe), j=3 row 1 (safe), j=1 row 3 (|Δi|=1, |Δj|∉{0,1,2}, j∈{4}). Place at j=4.
  Check j=4 with j=3 row 1 (|Δi|=3, safe ✓), j=0 row 0 (|Δi|=4, safe ✓). ✓

E(0,0), E(1,3), E(3,1), E(4,4). 4 knights.

Or with j=0 at row 3:
Row 4: from j=0 row 3 (|Δi|=1, |Δj|∉{0,1,2}, j∈{3,4}). From j=0 row 0 (safe). From j=3 row 1 (safe). Place at j=3 or 4.
  j=3: check with j=3 row 1 (|Δi|=3, safe ✓). ✓
  j=4: check with j=3 row 1 (|Δi|=3, safe ✓). ✓
  Can I place both? |Δj|=1, conflict. No. Just one.

E(0,0), E(1,3), E(3,0), E(4,3). 4 knights.

I keep getting 4-5. Let me try to see if 6 is possible on even squares.

Let me try:
Row 0: j=0.
Row 1: skip.
Row 2: j=3 (|Δi|=2, |Δj|=3∉{0,1} ✓).
Row 3: skip.
Row 4: j=0 (|Δi|=4 from row 0, safe; |Δi|=2 from row 2, |Δj|=3∉{0,1} ✓). 

That's only 3. Add more:
Row 0: j=0, j=4 (|Δj|=4, safe).
Row 2: from j=0 (j∈{2,3,4}), from j=4 (j∈{0,1,2}). Intersection: {2}. j=2.
Row 4: from j=0 (safe), j=4 (safe), j=2 (|Δi|=2, |Δj|∉{0,1}, j∈{0,1,4}). Place j=0, j=4.

5 knights. Same as before.

What if I try
