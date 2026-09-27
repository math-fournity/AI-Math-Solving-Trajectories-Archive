# analysis_agents_md.md — devin cli分析任务的AGENTS.md模板
# 
# 占位符（用Python str.format或string.Template填充）：
#   Some bugs are sitting on squares of $10\times 10$ board. Each bug has a direction associated with it [b](up, down, left, right)[/b]. After 1 second, the bugs jump one square in [b]their associated [/b]direction. When the bug reaches the edge of the board, the associated direction reverses (up becomes down, left becomes right, down becomes up, and right becomes left) and the bug moves in that direction. It is observed that it is [b]never[/b] the case that two bugs are on same square. What is the maximum number of bugs possible on the board?       — 题目文本
#   1. **Initial Setup and Problem Understanding:**
   - We have a $10 \times 10$ board.
   - Each bug moves in one of four directions: up, down, left, or right.
   - When a bug reaches the edge of the board, it reverses direction.
   - No two bugs can occupy the same square at any time.

2. **Proving 41 Bugs is Impossible:**
   - Color the board in a chessboard pattern (alternating black and white squares).
   - Each bug moves either in a row or a column.
   - By the Pigeonhole Principle, if there are 41 bugs, at least 3 bugs must be in the same row or column.
   - Again, by the Pigeonhole Principle, at least 2 of these bugs must be on the same color (either both on black squares or both on white squares).
   - Since they are on the same color and move in the same row or column, they will eventually collide.
   - Therefore, having 41 bugs is impossible.

3. **Proving 40 Bugs is Possible:**
   - We need to show that 40 bugs can be placed on the board such that they never collide.
   - Since bugs on white squares never collide with bugs on black squares, we can consider only white squares first.
   - We need to place 20 bugs on white squares such that they never collide.

4. **Labeling and Timing:**
   - Label the rows and columns from $0$ to $9$.
   - Let $r_i$ be the time taken by the bug in the $i^{th}$ row to reach the leftmost column.
   - Let $c_i$ be the time taken by the bug in the $i^{th}$ column to reach the topmost row.
   - Note that $0 \leq r_i, c_i \leq 17$.

5. **Parity Condition:**
   - For all $i$, $r_i - i$ and $c_i - i$ must have the same parity (either both even or both odd).

6. **Non-Collision Condition:**
   - The condition that the bug in the $i^{th}$ row doesn't collide with the one in the $j^{th}$ column is:
     \[
     (r_i \pm j) \neq (c_j \pm i)
     \]
     This simplifies to:
     \[
     (r_i \pm i) \neq (c_j \pm j)
     \]
     Let $a_i = r_i - i$ and $b_i = c_i - i$. Then the condition is:
     \[
     \{a_i, a_i + 2i\} \cap \{b_j, b_j + 2j\} = \emptyset
     \]

7. **Constructing Sets $A$ and $B$:**
   - Let $A = \{a_i \mid i = 0, 1, \dots, 9\}$ and $B = \{b_j \mid j = 0, 1, \dots, 9\}$.
   - Ensure that $A$ and $B$ are disjoint and:
     \[
     \{a_i + 2i \mid i = 0, 1, \dots, 9\} = A
     \]
     \[
     \{b_j + 2j \mid j = 0, 1, \dots, 9\} = B
     \]

8. **Example Construction:**
   - Start with:
     \[
     A = \{2, 4, 6, 10\} \quad \text{and} \quad B = \{8, 12, 14, 16\}
     \]
   - From this, find the sequences:
     \[
     a = (2, 2, 6, 4, 2, 10, 10, 6, 4, 2)
     \]
     \[
     b = (12, 12, 12, 8, 8, 16, 14, 12, 14, 12)
     \]
   - These sequences satisfy the conditions for all $i$ and $j$.

9. **Final Configuration:**
   - Use $r_i = a_i + i$ and $c_i = b_i + i$ to place bugs on white squares.
   - Similarly, place bugs on black squares to get a configuration for 40 bugs that never collide.

The final answer is $\boxed{40}$.  — 标准解答
#   Let me solve this problem. It's about bugs on a 10x10 board, each with a direction. After 1 second, each bug jumps one square in its direction. When a bug reaches the edge, its direction reverses and it moves that way. It's observed that it's never the case that two bugs are on the same square. Find the maximum number of bugs.

Let me think about this carefully.

The board is 10x10. Each bug has a position and a direction (up, down, left, right). After each second, the bug moves one square in its direction. When it reaches the edge, the direction reverses.

Let me think about the motion. A bug moving horizontally: it bounces back and forth. If it's in row r, column c, moving right, it goes c → c+1 → ... → 9 → 8 → ... → 0 → 1 → ... So the column cycles with period 18 (goes 0 to 9 then back to 0, that's 18 steps). Similarly for vertical motion.

Actually, let me think about this more carefully. The bug moves one square per second. When it reaches the edge of the board, the direction reverses. So if a bug is at column 9 moving right, it reverses to left and moves to column 8. If a bug is at column 0 moving left, it reverses to right and moves to column 1.

So the column position as a function of time: starting at column c, moving right. The position cycles through 0,1,...,9,8,7,...,1,0,1,...,9,8,... with period 18.

Actually, let me think of it as a "reflection" model. The position on a line of length 10 (positions 0-9). Moving right from position c: at time t, position is c+t if c+t ≤ 9, then bounces. The period is 18.

Let me use the standard unfolding trick. For a line of n positions (0 to n-1), the motion with reflection has period 2(n-1). For n=10, period is 18.

Now, the key constraint: at no time do two bugs occupy the same square. This must hold for ALL time (since it's "never" the case).

Let me think about what configurations are possible.

Each bug's state is (row, column, direction). The direction is one of 4. The total state space per bug is 10*10*4 = 400.

But the motion is deterministic. So each bug follows a fixed trajectory. Two bugs collide if at some time t, they're at the same position.

Let me think about the trajectory of a bug. A bug moving right in row r: its row stays r, column cycles with period 18. A bug moving left in row r: same thing but phase-shifted. A bug moving up in column c: column stays c, row cycles with period 18. A bug moving down in column c: same but phase-shifted.

So horizontal bugs stay in their row, vertical bugs stay in their column.

Two horizontal bugs in different rows never collide. Two horizontal bugs in the same row: they could collide. Two vertical bugs in different columns never collide. A horizontal bug and a vertical bug can collide if they're at the intersection at the same time.

Let me think about the period. The whole system has period lcm(18, 18) = 18. So we need to check collisions over 18 time steps (t = 0, 1, ..., 17), or actually we need to check that no two bugs are ever at the same position at the same time.

Wait, actually the period is 18 for both horizontal and vertical motion. So the entire system is periodic with period 18. We need to check t = 0, 1, ..., 17 (and t=0 is the same as t=18).

Hmm, but actually we need to be more careful. The initial state includes the direction. Let me think about the state of a horizontal bug in row r. Its state is (r, c, direction) where direction is left or right. The column motion has period 18, and the direction also has period 18 (it reverses at the edges). So the full state (r, c, direction) of a horizontal bug has period 18.

Similarly for vertical bugs.

So the system has period 18. We need no collisions at any of the 18 time steps t=0,...,17.

Now let me think about maximizing the number of bugs.

First, consider only horizontal bugs. In a given row r, how many horizontal bugs can we place such that no two ever collide?

In row r, a horizontal bug's column position over time is a function of time with period 18. The column takes values 0-9. Two bugs in the same row collide if at some time t, they have the same column.

A horizontal bug in row r with initial column c and direction right: at time t, column = f(c, t) where f is the bouncing function. The key insight: two bugs in the same row never collide if and only if their trajectories never coincide.

Actually, let me think about this differently. In a single row, the motion is on a path of 10 nodes (0-9) with reflection at ends. This is equivalent to motion on a cycle of 18 nodes (the "unfolded" path). Each bug occupies one position on this cycle at each time, and moves one step per unit time on the cycle. Two bugs collide iff they're at the same position on the cycle at the same time, which happens iff they're at the same position on the cycle at time 0 (since they all move at the same speed in the same direction on the cycle).

Wait, that's the key insight! On the unfolded cycle, all bugs move in the same direction (say clockwise) at the same speed (1 per unit time). So two bugs on the same cycle collide iff they start at the same position on the cycle.

The unfolded cycle for a row of 10: positions 0,1,...,9,8,7,...,1 (that's 18 positions, forming a cycle). Each position on the cycle corresponds to a (column, direction) pair. Position 0 on cycle = (col 0, right), position 1 = (col 1, right), ..., position 9 = (col 9, right), position 10 = (col 8, left), position 11 = (col 7, left), ..., position 17 = (col 1, left).

Wait, let me re-derive. A bug at column c moving right: at time 0 it's at column c. At time t, on the unfolded cycle, it's at position c + t (mod 18). The cycle position p maps to: if p ≤ 9, column = p, direction = right; if p > 9, column = 18 - p, direction = left.

So position 0 → (0, R), 1 → (1, R), ..., 9 → (9, R), 10 → (8, L), 11 → (7, L), ..., 17 → (1, L).

A bug at column c moving left: at time 0, on the cycle, where is it? If it's at column c moving left, then at time 1 it's at column c-1 (if c > 0) or it reverses. On the cycle, moving left means... hmm, let me think again.

Actually, on the unfolded cycle, ALL bugs move in the same direction (increasing cycle position). A bug moving right at column c starts at cycle position c. A bug moving left at column c: at time 0 it's at column c moving left. At time 1, it moves to column c-1 (if c > 0). On the cycle, position c-1+1 = c... no wait.

Let me reconsider. The unfolded cycle has 18 positions. At cycle position p, the bug is at column g(p) where g(p) = p if p ≤ 9, and g(p) = 18-p if p ≥ 10. The direction at cycle position p is right if p ≤ 9, left if p ≥ 10.

All bugs move one step forward on the cycle per unit time (p → p+1 mod 18). This is because:
- A bug at cycle position p ≤ 9 (column p, moving right): next position is p+1. If p < 9, that's column p+1, moving right. If p = 9, next is position 10, which is column 8, moving left. That matches: at column 9 moving right, it reverses and moves to column 8. ✓
- A bug at cycle position p ≥ 10 (column 18-p, moving left): next position is p+1. If p < 17, that's column 18-(p+1) = 17-p, moving left. So from column 18-p to column 17-p, moving left. ✓. If p = 17, next is position 0 (mod 18), which is column 0, moving right. From column 1 (18-17=1) moving left, it goes to column 0, then reverses to right. ✓

Great, so all bugs on the same row move in the same direction on the cycle at the same speed. Therefore, two bugs in the same row collide at some time iff they start at the same cycle position iff they have the same (column, direction) pair. But wait, that means two bugs in the same row with different (column, direction) pairs NEVER collide!

That's a powerful result. In a single row, we can place up to 18 horizontal bugs (one at each cycle position), and they never collide with each other. But wait, there are only 10 columns, and 2 directions, so there are 20 possible (column, direction) pairs for horizontal bugs, but only 18 cycle positions. The pairs (0, L) and (9, R) don't appear on the cycle... let me check.

Cycle position 0: (0, R). Position 9: (9, R). Position 10: (8, L). Position 17: (1, L).

What about (0, L)? A bug at column 0 moving left: it immediately reverses (it's at the edge) and moves right. So at time 0, it's at (0, L), but at time 1, it's at (1, R). On the cycle, this would be... at time 0, cycle position should be such that at time 1, it's at position 1 (column 1, right). So at time 0, it's at position 0 (column 0, right). But that contradicts - the bug is at (0, L) not (0, R).

Hmm, I think the issue is that (0, L) and (0, R) are different states but they map to the same cycle position. Let me reconsider.

Actually, when a bug is at column 0 moving left, it's at the edge. The problem says "when the bug reaches the edge of the board, the associated direction reverses and the bug moves in that direction." So if a bug is at column 0 and its direction is left, it's at the edge, so it reverses to right and moves right. So at time 1, it's at column 1 moving right.

But at time 0, it's at column 0 moving left. This is a valid state. On the cycle, this corresponds to... position 0 (since column 0, and the next move is to the right). But position 0 on the cycle is (0, R), not (0, L).

I think the issue is that (0, L) and (0, R) are the same trajectory - they both result in the bug being at column 0 at time 0 and column 1 at time 1. The direction at the edge is ambiguous in some sense, or rather, (0, L) immediately becomes (0, R) before moving.

Actually, re-reading the problem: "After 1 second, the bugs jump one square in their associated direction. When the bug reaches the edge of the board, the associated direction reverses."

So the process is: the bug has a direction. After 1 second, it jumps in that direction. If it reaches the edge (i.e., it's at the edge and would jump off), the direction reverses and it moves in the new direction.

So if a bug is at column 0 with direction left: it's at the edge. The direction reverses to right. It moves to column 1. So after 1 second, it's at column 1 with direction right.

If a bug is at column 0 with direction right: it moves to column 1 with direction right.

So both (0, L) and (0, R) lead to the same next state (1, R). They're effectively the same at the edge. Similarly, (9, R) and (9, L) both lead to (8, L).

So the effective state space for a horizontal bug in a row is 18 states (the 18 cycle positions), where the edge states (0 and 9) have only one effective direction.

OK so in a single row, we can place at most 18 horizontal bugs (one per cycle position), and they never collide. But wait, at time 0, multiple cycle positions can map to the same column. For example, cycle position 0 (column 0, right) and cycle position 18... no, 18 mod 18 = 0. Let me check: which cycle positions map to column 0? Only position 0. Which map to column 9? Only position 9. Which map to column 1? Positions 1 (right) and 17 (left). So at time 0, two bugs at cycle positions 1 and 17 would both be at column 1 - they'd collide at time 0!

So the constraint is not just about the cycle - at time 0, two bugs at different cycle positions can be at the same column. The cycle argument says they never collide at any time t ≥ 0 if they're at different cycle positions. But at time 0, two different cycle positions can map to the same column!

Wait, no. If two bugs are at different cycle positions, they're never at the same cycle position at any time (since they all move at the same speed). And the column is determined by the cycle position. So two bugs at different cycle positions are never at the same column at the same time. At time 0, bug A at cycle position 1 is at column 1, bug B at cycle position 17 is at column 1. Wait, that's the same column!

Hmm, but cycle position 1 maps to column 1, and cycle position 17 maps to column 18-17 = 1. So both are at column 1 at time 0. But they're at different cycle positions (1 and 17), and at time t, they're at positions 1+t and 17+t (mod 18), which are always different. But the columns g(1+t) and g(17+t) could be the same at some time.

Oh wait, I see the issue. Two bugs at different cycle positions are at different cycle positions at all times, but different cycle positions can map to the same column. So they CAN be at the same column at the same time even with different cycle positions!

Let me re-examine. Bug A at cycle position 1, bug B at cycle position 17. At time 0: A at column 1, B at column 1. Collision! So they do collide.

So my earlier reasoning was wrong. Two bugs in the same row collide iff at some time t, their cycle positions map to the same column. Since g(p) = g(18-p) for p ≠ 0 (and g(0) = 0, g(9) = 9), two bugs at cycle positions p and q collide at time t iff g(p+t) = g(q+t) (mod 18), which happens iff p+t ≡ q+t (mod 18) or p+t ≡ -(q+t) (mod 18) and p+t ≠ 0 (well, more precisely g(a) = g(b) iff a ≡ b or a + b ≡ 0 or a + b ≡ 18, but since we're mod 18, a + b ≡ 0 mod 18).

Wait, g(a) = g(b) iff a ≡ b (mod 18) or a + b ≡ 0 (mod 18). Because g(a) = a if a ≤ 9, g(a) = 18-a if a ≥ 10 (for a in 0..17). And g(a) = g(b) means either a = b, or a = 18-b (i.e., a + b = 18), or... let me just check: g(a) = g(b) iff a = b or a + b = 18 (when both in 1..17) or a = b = 0 or a = b = 9. Actually, g(a) = g(b) iff a = b or a + b ≡ 0 (mod 18) with a, b ≠ 0. Hmm, let me just enumerate: g(0)=0, g(1)=1, g(2)=2,...,g(9)=9, g(10)=8, g(11)=7,...,g(17)=1. So g(a)=g(b) with a≠b iff {a,b} = {k, 18-k} for k=1,...,8 (giving g=k), or {a,b}={0,0} (trivial), {9,9} (trivial). Also g(0)=0 is unique, g(9)=9 is unique.

So g(a) = g(b) with a ≠ b iff a + b ≡ 18 (mod 18), i.e., a + b ≡ 0 (mod 18), and a ≠ 0 (since g(0)=0 is unique, and 0+0=0 but that's a=b).

Actually, a+b ≡ 0 (mod 18) with a ≠ b: pairs are (1,17), (2,16), ..., (8,10), and also (0,0) but that's a=b, and (9,9) but that's a=b. So the collision pairs are (k, 18-k) for k=1,...,8.

So two bugs at cycle positions p and q (in the same row) collide at time t iff p+t ≡ q+t (mod 18) [i.e., p=q, same bug] or (p+t) + (q+t) ≡ 0 (mod 18) [i.e., p+q+2t ≡ 0 (mod 18)].

The second condition: p + q + 2t ≡ 0 (mod 18) for some t ∈ {0,...,17}. This is solvable iff gcd(2, 18) | (p+q), i.e., 2 | (p+q), i.e., p and q have the same parity.

So two bugs in the same row at cycle positions p and q (p ≠ q) collide at some time iff p + q is even, i.e., p and q have the same parity.

Therefore, to avoid collisions in a single row, we need all bugs to have cycle positions of the same parity... no wait, we need no two bugs to have the same parity. That means at most one bug of each parity? No, we need all pairs to have different parities, which means all bugs have the same parity? No...

If p and q have the same parity, they collide. If p and q have different parities, they don't collide. So to avoid all collisions, we need all pairs to have different parities, which means... we can have at most 2 bugs? No, that's not right either. We need every pair (p,q) to have different parities. That means all bugs must have the same parity? No, if all have the same parity, then every pair has the same parity, and they all collide.

Wait, I need to re-read. Two bugs collide iff p and q have the same parity. So to AVOID collision, we need p and q to have DIFFERENT parities. For ALL pairs, we need different parities. But with more than 2 bugs, by pigeonhole, at least two will have the same parity. So at most 2 bugs per row? That seems too few.

Hmm wait, let me double-check with a small example. Row of 10, bugs at cycle positions 0 and 2 (both even). At time t, positions are t and t+2 (mod 18). They collide when g(t) = g(t+2), i.e., t + (t+2) ≡ 0 (mod 18), i.e., 2t + 2 ≡ 0 (mod 18), i.e., 2t ≡ -2 ≡ 16 (mod 18), i.e., t ≡ 8 (mod 9). So t = 8 or t = 17. At t=8: positions 8 and 10, g(8)=8, g(10)=8. Yes, collision at column 8. ✓

Bugs at cycle positions 0 and 1 (different parity). Collision when 2t + 1 ≡ 0 (mod 18), i.e., 2t ≡ 17 (mod 18). Since gcd(2,18)=2 and 2∤17, no solution. So they never collide. ✓

So indeed, in a single row, at most 2 horizontal bugs (one even cycle position, one odd cycle position)? Wait, but we could have multiple bugs with even cycle positions as long as no two of them collide. But I just showed that any two bugs with the same parity collide. So indeed, at most 1 even + 1 odd = 2 bugs per row.

Hmm, but that seems very restrictive. Let me reconsider.

Actually wait. I need to also check: two bugs at cycle positions p and q with the same parity always collide? The condition is p + q + 2t ≡ 0 (mod 18) for some t. If p + q is even, then 2t ≡ -(p+q) (mod 18). Since p+q is even, -(p+q) is even, and gcd(2,18) = 2, so 2t ≡ even (mod 18) has solutions. Yes, always solvable. So yes, any two bugs with the same parity in the same row will collide.

So in a single row, at most 2 horizontal bugs. With 10 rows, that's at most 20 horizontal bugs.

Similarly, in a single column, at most 2 vertical bugs. With 10 columns, at most 20 vertical bugs.

But we can mix horizontal and vertical bugs. The constraint is:
1. No two horizontal bugs in the same row with the same parity cycle position.
2. No two vertical bugs in the same column with the same parity cycle position.
3. No horizontal bug and vertical bug at the same position at the same time.

Let me think about constraint 3. A horizontal bug in row r at cycle position p_h: at time t, it's at (r, g(p_h + t)). A vertical bug in column c at cycle position p_v: at time t, it's at (g(p_v + t), c). They collide at time t iff r = g(p_v + t) and c = g(p_h + t).

This is more complex. Let me think about the overall structure.

Total bugs = (horizontal bugs) + (vertical bugs). We want to maximize this.

Let me think about it differently. Each bug has a "cycle position" which is its position on the unfolded cycle (0-17). The parity of the cycle position determines which "class" it's in.

For horizontal bugs in row r: at most one with even cycle position, at most one with odd cycle position. So at most 2 per row.

For vertical bugs in column c: at most one with even cycle position, at most one with odd cycle position. So at most 2 per column.

Now, the cross-constraint between horizontal and vertical bugs.

Let me think about this more carefully using the unfolding idea. 

Actually, let me think about the problem in terms of the "unfolded" coordinates. 

For a horizontal bug in row r with cycle position p: at time t, position is (r, g(p+t)).
For a vertical bug in column c with cycle position q: at time t, position is (g(q+t), c).

Collision at time t: r = g(q+t) and g(p+t) = c.

So we need: for all t, it's not the case that (r = g(q+t) AND c = g(p+t)).

Equivalently, there's no t such that g(q+t) = r AND g(p+t) = c.

g(q+t) = r means q+t ≡ r (mod 18) or q+t ≡ 18-r (mod 18) (i.e., q+t ≡ -r mod 18), assuming r ≠ 0 (if r=0, only q+t ≡ 0; if r=9, only q+t ≡ 9).

Similarly g(p+t) = c means p+t ≡ c or p+t ≡ -c (mod 18).

So we need: there's no t such that (q+t ≡ ±r AND p+t ≡ ±c) (mod 18), where the ± is independent (4 combinations), with the caveat that for r=0 or r=9, only one sign works, and similarly for c.

From q+t ≡ s₁ (mod 18) and p+t ≡ s₂ (mod 18), we get t ≡ s₁ - q ≡ s₂ - p (mod 18), so s₁ - q ≡ s₂ - p (mod 18), i.e., s₁ - s₂ ≡ q - p (mod 18).

So a collision exists iff there exist signs such that (±r) - (±c) ≡ q - p (mod 18), where the four combinations of signs are considered (with restrictions at edges).

The four combinations give: r-c, r+c, -r-c, -r+c, i.e., ±(r-c) and ±(r+c). So collision iff q - p ≡ ±(r-c) or q - p ≡ ±(r+c) (mod 18).

Equivalently, q - p ≡ r - c, r + c, -r - c, or -r + c (mod 18).

Which is q - p ≡ ±(r-c) or q - p ≡ ±(r+c) (mod 18).

Hmm, this is getting complex. Let me think about it from a higher level.

Let me define for each bug a "type" based on the parity of its cycle position. There are two parities (even and odd). 

For horizontal bugs: even parity bugs in different rows don't interact (they're in different rows). Even parity bugs in the same row: at most 1. Similarly for odd parity.

For vertical bugs: even parity bugs in different columns don't interact. Even parity bugs in the same column: at most 1. Similarly for odd.

Cross interactions: a horizontal bug (row r, cycle position p) and a vertical bug (column c, cycle position q) collide iff q - p ≡ ±(r-c) or ±(r+c) (mod 18).

Note that q - p mod 2 = (q mod 2) - (p mod 2) mod 2 = (q + p) mod 2. So the parity of q - p is the parity of p + q.

And ±(r-c) has parity (r+c) mod 2, and ±(r+c) has parity (r+c) mod 2. So all four values ±(r-c), ±(r+c) have the same parity, namely (r+c) mod 2.

So a collision is possible only if (p + q) mod 2 = (r + c) mod 2.

If p and q have the same parity, then p + q is even, so we need r + c even.
If p and q have different parities, then p + q is odd, so we need r + c odd.

This is a necessary condition for collision, not sufficient. But it gives us a parity constraint.

Let me think about this problem differently. Let me consider the "parity class" of a bug. A horizontal bug in row r with cycle position p has parity p mod 2. A vertical bug in column c with cycle position q has parity q mod 2.

Let me split into two independent problems: even-parity bugs and odd-parity bugs. Two bugs of different parities never collide with each other (within the same row/column, we showed same parity collides, different parity doesn't; and for cross interactions, the parity condition shows different parities can only collide if r+c is odd, but...).

Hmm wait, that's not quite right. Let me reconsider.

Two horizontal bugs in the same row: same parity → collide, different parity → don't collide.
Two vertical bugs in the same column: same parity → collide, different parity → don't collide.
Horizontal and vertical bug: can collide only if (p+q) mod 2 = (r+c) mod 2.

So even-parity horizontal bugs and even-parity vertical bugs can collide if r+c is even.
Even-parity horizontal and odd-parity vertical can collide if r+c is odd.
Etc.

This is getting complicated. Let me try a different approach.

Let me think about the problem as a graph coloring / independent set problem.

Actually, let me try to think about small cases first and see if I can find a pattern.

For a 10x10 board, let me try to find the maximum.

Let me consider the "unfolded" representation. Each bug is characterized by:
- Type: H (horizontal) or V (vertical)
- If H: row r (0-9), cycle position p (0-17)
- If V: column c (0-9), cycle position q (0-17)

Constraints:
1. Two H bugs in same row with same parity p: collide. So at most 1 H bug per (row, parity).
2. Two V bugs in same column with same parity q: collide. So at most 1 V bug per (column, parity).
3. H bug (r, p) and V bug (c, q) collide iff q-p ≡ ±(r-c) or ±(r+c) (mod 18), AND (p+q) mod 2 = (r+c) mod 2.

Wait, condition 3 already includes the parity condition. Let me re-derive.

H bug (r, p) and V bug (c, q): collision iff ∃ t such that g(q+t) = r and g(p+t) = c.

g(q+t) = r: q+t ≡ r or q+t ≡ 18-r (mod 18), with the edge cases.
g(p+t) = c: p+t ≡ c or p+t ≡ 18-c (mod 18).

From these: t ≡ (r or 18-r) - q and t ≡ (c or 18-c) - p. So:
(r or 18-r) - q ≡ (c or 18-c) - p (mod 18)

Four cases:
1. r - q ≡ c - p → q - p ≡ r - c
2. r - q ≡ 18-c - p → q - p ≡ r + c - 18 ≡ r + c (mod 18)
3. 18-r - q ≡ c - p → q - p ≡ 18 - r - c ≡ -(r+c) (mod 18)
4. 18-r - q ≡ 18-c - p → q - p ≡ c - r ≡ -(r-c) (mod 18)

So q - p ≡ ±(r-c) or ±(r+c) (mod 18). (With edge case restrictions, but let's ignore those for now and consider them later.)

Now, the key observation: q - p mod 2 determines the parity. And ±(r-c) and ±(r+c) all have the same parity as r+c (since r-c = r+c-2c, same parity as r+c).

So collision requires (q-p) ≡ (r+c) (mod 2), i.e., p+q ≡ r+c (mod 2).

Now, let me think about this as follows. Let's define the "parity" of a bug as p mod 2 (for H bugs) or q mod 2 (for V bugs). And the "position parity" as r mod 2 (for H bugs, since they're in row r) or c mod 2 (for V bugs, since they're in column c).

Actually, let me think about it more carefully. Let me separate bugs by the parity of their cycle position.

Even bugs: cycle position is even.
Odd bugs: cycle position is odd.

Within even bugs:
- Two H bugs in the same row: both even, same parity → collide. At most 1 per row.
- Two V bugs in the same column: both even, same parity → collide. At most 1 per column.
- H bug (r, p_even) and V bug (c, q_even): p+q is even, r+c must be even for collision. So collision possible only if r+c is even.

Within odd bugs: similar, but p+q is even (both odd), so again r+c must be even.

Cross (even H, odd V): p+q is odd, r+c must be odd for collision.
Cross (odd H, even V): p+q is odd, r+c must be odd.

Hmm, this is still complex. Let me try to think about the problem computationally. But the rules say I can't use tools. Let me think more carefully.

Let me try a different approach. Let me think about what happens at each time step.

At time t, each bug is at some position on the board. The constraint is that at every time t, all bugs are at distinct positions. Since there are 100 squares, at most 100 bugs at any time. But the constraint is stronger because it must hold for all t.

Let me think about the period. The system has period 18. At each of the 18 time steps, the bugs occupy distinct squares. So over 18 time steps, each bug visits 18 squares (its trajectory). The constraint is that at each time step, the bugs' positions are distinct.

This is like a scheduling problem. Each bug has a "schedule" (its trajectory of 18 positions, one per time step). We need to select a maximum set of bugs such that at each time step, no two bugs are at the same position.

The total "capacity" is 18 * 100 = 1800 (position-time slots). Each bug uses 18 slots. So a naive upper bound is 1800/18 = 100. But this is just the trivial bound (100 squares).

But the constraint is per-time-step, not total. At each time step, at most 100 bugs. So at most 100 bugs total (since each bug is at exactly one position at each time step). But can we achieve 100?

If we could place 100 bugs such that at each time step, they fill the entire board, that would be optimal. But is that possible?

Let me think about it. At time 0, we need 100 bugs at 100 distinct squares - so every square is occupied. At time 1, every bug moves, and again every square must be occupied. Etc.

This is like a permutation of the 100 squares at each time step, where each bug's movement is constrained by the bouncing rules.

Hmm, but not every permutation is achievable. Each bug either moves horizontally (stays in its row) or vertically (stays in its column). 

Let me think about this. If all bugs are horizontal, then at each time step, the bugs in each row permute among the columns of that row. But with the bouncing constraint, the permutation is very specific.

Actually, with horizontal bugs only: in each row, the bugs move according to the cycle. At time t, a bug at cycle position p is at column g(p+t). If we have k bugs in a row at cycle positions p_1, ..., p_k, then at time t, they're at columns g(p_1+t), ..., g(p_k+t). For these to be distinct, we need g(p_i+t) ≠ g(p_j+t) for all i≠j and all t. As we showed, this requires all p_i to have distinct parities, so at most 2 per row. With 10 rows, at most 20 horizontal bugs.

Similarly, at most 20 vertical bugs.

But with a mix, we can do better. Let me think about the maximum.

Let me consider a specific construction. Suppose we use both horizontal and vertical bugs.

Let me think about the parity classes more carefully.

Define:
- H_even: horizontal bugs with even cycle position. At most 1 per row (10 total).
- H_odd: horizontal bugs with odd cycle position. At most 1 per row (10 total).
- V_even: vertical bugs with even cycle position. At most 1 per column (10 total).
- V_odd: vertical bugs with odd cycle position. At most 1 per column (10 total).

So naive upper bound: 10 + 10 + 10 + 10 = 40.

But cross-constraints reduce this. Let me analyze the cross-constraints.

H bug (r, p) and V bug (c, q) collide iff q-p ≡ ±(r-c) or ±(r+c) (mod 18).

Let me consider the four parity combinations:

1. H_even (p even) and V_even (q even): q-p is even. Collision iff q-p ≡ ±(r-c) or ±(r+c) (mod 18). Since q-p is even, we need ±(r-c) or ±(r+c) to be even, i.e., r+c even. If r+c is odd, no collision. If r+c is even, collision is possible (depends on specific values).

2. H_even (p even) and V_odd (q odd): q-p is odd. Collision requires r+c odd. If r+c even, no collision.

3. H_odd (p odd) and V_even (q even): q-p is odd. Collision requires r+c odd.

4. H_odd (p odd) and V_odd (q odd): q-p is even. Collision requires r+c even.

So:
- Same parity (both even or both odd): collision possible only if r+c even.
- Different parity: collision possible only if r+c odd.

Now, r+c even means r and c have the same parity. r+c odd means r and c have different parities.

Let me think about the board as a chessboard with black (r+c even) and white (r+c odd) squares.

For same-parity bugs (H_even with V_even, or H_odd with V_odd): collision possible only at "black" intersections (r, c) where r+c is even.
For different-parity bugs (H_even with V_odd, or H_odd with V_even): collision possible only at "white" intersections (r, c) where r+c is odd.

This is still complex. Let me try to think about specific constructions.

Let me try to maximize the total. Let me consider using H_even and V_odd (or H_odd and V_even), since different parity combinations have collision only at white squares.

Actually, let me think about this more carefully. Let me try to use H_even and V_even, and see how many we can place.

H_even: at most 1 per row, so at most 10. Let's say we place H_even bugs in rows 0-9, with even cycle positions p_0, ..., p_9.
V_even: at most 1 per column, so at most 10. Let's say we place V_even bugs in columns 0-9, with even cycle positions q_0, ..., q_9.

Collision between H_even(r, p_r) and V_even(c, q_c): requires r+c even AND q_c - p_r ≡ ±(r-c) or ±(r+c) (mod 18).

If r+c is even, we need to avoid q_c - p_r ≡ ±(r-c) or ±(r+c) (mod 18).

The even values mod 18 are: 0, 2, 4, 6, 8, 10, 12, 14, 16. There are 9 even values.

For a given (r, c) with r+c even, the forbidden values of q_c - p_r are: r-c, -(r-c), r+c, -(r+c) (mod 18). Some of these might coincide.

r-c mod 18: since r, c ∈ {0,...,9}, r-c ∈ {-9,...,9}, so r-c mod 18 ∈ {0,...,9, 9,...,17} = {0,...,17}. Actually r-c mod 18 is (r-c+18) mod 18.

The four forbidden values are ±(r-c) and ±(r+c) mod 18. Since r+c ∈ {0,...,18} and r-c ∈ {-9,...,9}:

Let me think about how many distinct forbidden values there are. ±(r-c) gives two values (or one if r=c), and ±(r+c) gives two values (or one if r+c=0 or r+c=9... well r+c=0 only if r=c=0, r+c=18 only if r=c=9).

In general, the four values r-c, -(r-c), r+c, -(r+c) mod 18. Note that r-c and -(r-c) are negatives, r+c and -(r+c) are negatives. Also, r-c = r+c - 2c, so they're related.

The number of distinct forbidden values is at most 4, but could be 2 or 3 in special cases.

This is getting very complex. Let me try a different approach - let me think about the problem in terms of a cleaner formulation.

Alternative approach: Think of each bug as having a "trajectory" which is a set of 18 (position, time) pairs. We need to select a maximum set of bugs with pairwise non-intersecting trajectories.

Actually, let me reconsider the problem. Let me think about what the trajectories look like.

A horizontal bug in row r with cycle position p: at time t, it's at (r, g(p+t)). Its trajectory is {(r, g(p+t)) : t = 0, ..., 17}. Since g has period 18 and g(p+t) takes each value in {0,...,9} with g(k) appearing twice (for k and 18-k) except g(0)=0 and g(9)=9 which appear once. So the bug visits each column in its row, with columns 1-8 visited twice and columns 0, 9 visited once. Total: 8*2 + 2 = 18. ✓

A vertical bug in column c with cycle position q: at time t, it's at (g(q+t), c). Similar.

Now, two bugs collide if their trajectories share a common (position, time) pair.

Let me think about this as a bipartite-like structure. 

Hmm, let me try yet another approach. Let me think about the problem in terms of "lines" on the board.

Each horizontal bug stays in its row. Each vertical bug stays in its column. A horizontal bug in row r and a vertical bug in column c can only collide at the intersection (r, c). They collide at (r, c) if there's a time t when both are there.

The horizontal bug is at (r, c) at times t where g(p+t) = c, i.e., p+t ≡ c or p+t ≡ 18-c (mod 18). So t ≡ c-p or t ≡ 18-c-p (mod 18). Two times (or one if c = 18-c, i.e., c = 9, or c = 0).

The vertical bug is at (r, c) at times t where g(q+t) = r, i.e., t ≡ r-q or t ≡ 18-r-q (mod 18). Two times (or one).

They collide if any of these times coincide, which gives the condition we derived.

OK let me try to think about this more carefully with a cleaner model.

Let me use the "unfolded" coordinates. For a horizontal bug in row r with cycle position p, define its "unfolded column" as u = p (an element of Z_18). At time t, unfolded column is u+t, and actual column is g(u+t).

For a vertical bug in column c with cycle position q, define its "unfolded row" as v = q. At time t, unfolded row is v+t, and actual row is g(v+t).

Collision at time t: g(v+t) = r and g(u+t) = c. In unfolded coordinates: v+t ≡ ±r and u+t ≡ ±c (mod 18). So v-u ≡ ±r ∓ c (mod 18), giving the four cases.

Let me define d = v - u (mod 18) (the difference of unfolded coordinates). Then collision iff d ≡ ±r ± c (mod 18) for some combination of signs, i.e., d ∈ {r-c, r+c, -r-c, -r+c} (mod 18) = {±(r-c), ±(r+c)} (mod 18).

So for a horizontal bug in row r with unfolded column u, and a vertical bug in column c with unfolded row v, they collide iff v - u ≡ ±(r-c) or ±(r+c) (mod 18).

Now, the key insight: this condition depends on r, c, u, v. Specifically, it depends on the difference v - u and the position (r, c).

Let me think about this as follows. Consider the "difference" d = v - u (mod 18). For a given pair (H bug at (r, u), V bug at (c, v)), collision iff d ∈ {±(r-c), ±(r+c)} (mod 18).

Now, for a fixed r and c, the set {±(r-c), ±(r+c)} mod 18 has at most 4 elements. So out of 18 possible values of d, at most 4 cause collision.

But we need to avoid collisions for ALL pairs (H bug, V bug). This is a constraint satisfaction problem.

Let me try to think about upper bounds more carefully.

Upper bound approach: Consider the 18 time steps. At each time step, the bugs occupy distinct squares. Each horizontal bug is always in its row, each vertical bug always in its column.

At time t, in row r, the horizontal bugs in row r occupy some columns, and the vertical bugs whose unfolded row at time t maps to r also occupy some columns in row r. The total in row r is at most 10.

Let me count more carefully. At time t:
- Horizontal bugs in row r: these are at columns g(p_i + t) for each H bug i in row r.
- Vertical bugs at row r at time t: a V bug in column c with unfolded row v is at row g(v+t). It's in row r when g(v+t) = r, i.e., v+t ≡ ±r (mod 18). For each such V bug, it occupies column c in row r.

So at time t, in row r, the occupied columns are: {g(p_i+t) : H bug i in row r} ∪ {c : V bug in column c, g(v_j+t) = r}.

These must all be distinct, and there are at most 10.

This is complex. Let me try to think about specific constructions and upper bounds.

Let me try a cleaner approach. Let me think about the "conflict graph" and try to find the maximum independent set.

Actually, let me try to think about the problem by considering the parity structure more carefully.

Let me define the "color" of a bug. For a horizontal bug in row r with cycle position p, define its color as (p mod 2, r mod 2) ∈ {0,1}². For a vertical bug in column c with cycle position q, define its color as (q mod 2, c mod 2) ∈ {0,1}².

Hmm, I'm not sure this leads anywhere clean. Let me try to think about the problem differently.

Let me consider the following: at each time t, the board is a 10x10 grid. Horizontal bugs occupy positions in their rows, vertical bugs in their columns. The constraint is that at each time, all positions are distinct.

Let me think about a relaxation. Suppose we only care about time t=0. Then we just need all bugs at distinct positions at time 0. This allows up to 100 bugs. But the constraint is for all t.

Let me think about what makes the problem hard. The bouncing motion creates correlations between positions at different times.

Let me try to think about the problem in terms of "conflict" between bugs.

Two horizontal bugs in the same row conflict iff same parity (as shown). 
Two vertical bugs in the same column conflict iff same parity.
A horizontal bug (r, p) and vertical bug (c, v) conflict iff v - p ≡ ±(r-c) or ±(r+c) (mod 18).

Let me try to find the maximum by considering specific constructions.

Construction 1: All horizontal bugs. At most 2 per row (one even, one odd), 10 rows → 20 bugs.

Construction 2: All vertical bugs. Similarly 20.

Construction 3: Mix. Let me try to use some rows for horizontal bugs and some columns for vertical bugs.

Suppose we use rows 0-4 for horizontal bugs (2 per row = 10) and columns 0-4 for vertical bugs (2 per column = 10). But we need to check cross-constraints.

A horizontal bug in row r (r ∈ {0,...,4}) and a vertical bug in column c (c ∈ {0,...,4}) collide iff v - p ≡ ±(r-c) or ±(r+c) (mod 18).

For this to not happen, we need to choose the cycle positions carefully.

Hmm, this is getting complicated. Let me try to think about it from a different angle.

Let me consider the "unfolded board." Instead of a 10x10 board with bouncing, think of an 18x18 unfolded board where bugs move in straight lines.

Actually, here's a cleaner way to think about it. The unfolding maps the 10x10 board with bouncing to an 18x18 torus where bugs move in straight lines. Each bug moves one step per unit time in a fixed direction on the torus.

Horizontal bug in row r: on the torus, it's at "unfolded row" r' and "unfolded column" u, moving in the +column direction. The unfolded row r' is... hmm, the row doesn't change for horizontal bugs, so the unfolded row is just r (or some function of r). Actually, the row stays fixed, so there's no unfolding needed for the row. The column unfolds to 18 positions.

Wait, but the board is 10x10, and only the column unfolds for horizontal bugs (to 18 positions), and only the row unfolds for vertical bugs (to 18 positions). So it's not a clean 18x18 torus.

Let me think about it differently. Let me consider the "state space" of each bug. A horizontal bug's state is (row, unfolded_column) ∈ {0,...,9} × Z_18. A vertical bug's state is (unfolded_row, column) ∈ Z_18 × {0,...,9}. At each time step, the unfolded coordinate advances by 1.

Two horizontal bugs collide iff they have the same (row, unfolded_column) at some time, iff they have the same (row, unfolded_column) at all times (since they move at the same speed), iff they have the same (row, unfolded_column) at time 0. But wait, two different unfolded_columns can map to the same actual column. So they collide in the actual board iff g(u1 + t) = g(u2 + t) for some t, which as we showed happens iff u1 ≡ u2 or u1 + u2 ≡ 0 (mod 18)... no, iff u1 and u2 have the same parity (as I showed earlier, two bugs in the same row collide iff their cycle positions have the same parity).

Wait, I think I need to be more careful. Two bugs in the same row with unfolded columns u1 and u2: they collide at time t iff g(u1+t) = g(u2+t). This happens iff (u1+t) + (u2+t) ≡ 0 (mod 18) [and u1+t ≠ u2+t, but if u1 ≠ u2 this is automatic for the relevant t], i.e., u1 + u2 + 2t ≡ 0 (mod 18). Solvable iff u1 + u2 is even, i.e., same parity.

OK so my earlier analysis was correct.

Let me try to think about the maximum using a counting argument.

Consider the 18 time steps. At each time step, the 100 squares are partitioned among the bugs. Each bug occupies one square per time step. Over 18 time steps, each bug occupies 18 squares (with possible repeats, but at distinct times).

Total bug-time slots: 18 * (number of bugs). These must fit into 18 * 100 = 1800 slots, but with the constraint that at each time step, no two bugs share a square. So the number of bugs ≤ 100 (trivial).

But we can get a better bound by considering the structure.

At time t, in row r, the bugs present are:
- Horizontal bugs in row r (always present in row r)
- Vertical bugs that happen to be in row r at time t

The number of horizontal bugs in row r is at most 2 (as shown). The number of vertical bugs in row r at time t is the number of vertical bugs whose unfolded row at time t maps to r. 

A vertical bug with unfolded row v is at actual row g(v+t). For a given r, g(v+t) = r iff v+t ≡ r or v+t ≡ 18-r (mod 18). So at most 2 unfolded rows map to r at each time (or 1 if r=0 or r=9). But multiple vertical bugs could have the same unfolded row v (they'd be in different columns though).

Hmm, this is getting complicated. Let me try to think about upper bounds by considering specific time steps.

At time t, the board has 100 squares. Horizontal bugs occupy some, vertical bugs occupy others. In each row r, the horizontal bugs in row r occupy at most 2 squares. The remaining squares in row r (at least 8) can be occupied by vertical bugs. But vertical bugs in row r at time t are those whose unfolded row maps to r.

The number of vertical bugs in row r at time t: these are vertical bugs in various columns c whose unfolded row v satisfies g(v+t) = r. For each column c, at most 2 vertical bugs (one even, one odd unfolded row). But only those whose g(v+t) = r are in row r at time t.

For a given column c, the vertical bugs have unfolded rows v_even and v_odd (at most one each). At time t, the bug with unfolded row v is at row g(v+t). So it's in row r iff v+t ≡ ±r (mod 18).

For the even bug: v_even + t ≡ ±r (mod 18). For the odd bug: v_odd + t ≡ ±r (mod 18).

So at time t, in row r, from column c, we get at most 2 vertical bugs (if both v_even+t and v_odd+t map to r), but typically 0 or 1.

This is hard to bound in general. Let me try a different approach.

Let me think about the problem as follows. We have 10 rows and 10 columns. We place horizontal bugs (at most 2 per row) and vertical bugs (at most 2 per column). The cross-constraints determine which combinations are feasible.

Let me try to find the maximum by considering the parity structure.

Let me split the bugs into 4 types:
- HE: horizontal, even cycle position. At most 1 per row → at most 10.
- HO: horizontal, odd cycle position. At most 1 per row → at most 10.
- VE: vertical, even cycle position. At most 1 per column → at most 10.
- VO: vertical, odd cycle position. At most 1 per column → at most 10.

Cross-constraints (collision conditions):
- HE(r, p) & VE(c, q): q-p even, collision iff r+c even and q-p ≡ ±(r-c) or ±(r+c) (mod 18).
- HE(r, p) & VO(c, q): q-p odd, collision iff r+c odd and q-p ≡ ±(r-c) or ±(r+c) (mod 18).
- HO(r, p) & VE(c, q): q-p odd, collision iff r+c odd and q-p ≡ ±(r-c) or ±(r+c) (mod 18).
- HO(r, p) & VO(c, q): q-p even, collision iff r+c even and q-p ≡ ±(r-c) or ±(r+c) (mod 18).

So HE conflicts with VE only at "black" squares (r+c even), and HE conflicts with VO only at "white" squares (r+c odd). Similarly HO conflicts with VE at white squares, HO conflicts with VO at black squares.

Now, the board has 50 black squares and 50 white squares. In each row, 5 black and 5 white squares. In each column, 5 black and 5 white squares.

Let me think about a specific strategy. Suppose we use only HE and VO bugs. Then:
- HE bugs: at most 1 per row, 10 total.
- VO bugs: at most 1 per column, 10 total.
- Cross-constraint: HE(r, p) and VO(c, q) collide iff r+c odd and q-p ≡ ±(r-c) or ±(r+c) (mod 18).

Similarly, we could use HE and VE, or HO and VO, or HO and VE, or all four types.

Let me first try to maximize with just two types: HE and VO (or equivalently HO and VE by symmetry).

With HE and VO:
- 10 HE bugs (one per row) + 10 VO bugs (one per column) = 20.
- But cross-constraints may reduce this.

For HE(r, p_r) and VO(c, q_c): collision iff r+c odd and q_c - p_r ≡ ±(r-c) or ±(r+c) (mod 18).

We need to choose p_r (even, 0-16) for each row r, and q_c (odd, 1-17) for each column c, such that no collision occurs.

For each pair (r, c) with r+c odd, we need q_c - p_r ∉ {±(r-c), ±(r+c)} (mod 18).

There are 50 such pairs (r+c odd). For each, 4 forbidden values of q_c - p_r (out of 18 possible, but q_c - p_r is always odd, so 9 possible odd values, and at most 4 forbidden).

Hmm, this seems like it might be feasible. Let me try a specific construction.

Let me try p_r = 2r (even) for r = 0, ..., 8, and p_9 = 0 or something. Wait, 2r for r=0,...,8 gives 0,2,4,...,16, and for r=9, 2*9=18≡0. So p_r = 2r mod 18.

And q_c = 2c+1 (odd) for c = 0, ..., 8, and q_9 = 2*9+1 = 19 ≡ 1. So q_c = 2c+1 mod 18.

Then q_c - p_r = (2c+1) - 2r = 2(c-r) + 1 (mod 18).

For r+c odd (i.e., r and c have different parities), the forbidden values are ±(r-c) and ±(r+c) mod 18.

Let me check a specific pair. r=0, c=1 (r+c=1, odd). q_1 - p_0 = 2(1-0)+1 = 3. Forbidden: ±(0-1) = ±1 = {1, 17}, ±(0+1) = ±1 = {1, 17}. So forbidden = {1, 17}. 3 ∉ {1, 17}. ✓

r=0, c=3 (r+c=3, odd). q_3 - p_0 = 2(3)+1 = 7. Forbidden: ±(0-3) = {3, 15}, ±(0+3) = {3, 15}. So forbidden = {3, 15}. 7 ∉ {3, 15}. ✓

r=0, c=5. q_5 - p_0 = 11. Forbidden: ±5 = {5, 13}. 11 ∉ {5, 13}. ✓

r=0, c=7. q_7 - p_0 = 15. Forbidden: ±7 = {7, 11}. 15 ∉ {7, 11}. ✓

r=0, c=9. q_9 - p_0 = 2(9)+1 = 19 ≡ 1. Forbidden: ±9 = {9, 9}. So forbidden = {9}. 1 ∉ {9}. ✓

r=1, c=0 (r+c=1, odd). q_0 - p_1 = 1 - 2 = -1 ≡ 17. Forbidden: ±(1-0) = {1, 17}, ±(1+0) = {1, 17}. So forbidden = {1, 17}. 17 ∈ {1, 17}. ✗ Collision!

So this construction doesn't work for (r=1, c=0). Let me try a different construction.

Hmm, let me think about this more carefully. The condition q_c - p_r ≡ ±(r-c) or ±(r+c) (mod 18) can be rewritten. Note that:
- r-c and r+c differ by 2c.
- -(r-c) = c-r and -(r+c) = -r-c.

So the forbidden set is {r-c, c-r, r+c, -r-c} mod 18 = {r-c, c-r, r+c, -(r+c)} mod 18.

Note that (r-c) + (r+c) = 2r, and (r-c) - (r+c) = -2c. Also (c-r) + (r+c) = 2c, and (c-r) + (-(r+c)) = -2r.

Let me try p_r = 0 for all r (all HE bugs at cycle position 0). Then q_c - p_r = q_c. The forbidden values for pair (r, c) with r+c odd are {r-c, c-r, r+c, -(r+c)} mod 18. We need q_c ∉ this set for all r with r+c odd (i.e., r ≠ c mod 2).

For a given c, the forbidden values over all r with r ≠ c mod 2 are:
{r-c, c-r, r+c, -(r+c)} for all r with r ≠ c mod 2, r ∈ {0,...,9}.

Let me compute for c=0: r ∈ {1,3,5,7,9} (odd r).
- r=1: {1, -1≡17, 1, -1≡17} = {1, 17}
- r=3: {3, 15, 3, 15} = {3, 15}
- r=5: {5, 13, 5, 13} = {5, 13}
- r=7: {7, 11, 7, 11} = {7, 11}
- r=9: {9, 9, 9, 9} = {9}

Forbidden for c=0: {1, 3, 5, 7, 9, 11, 13, 15, 17} = all odd numbers! So q_0 must be odd (which it is, since VO) and not in this set. But all odd numbers are forbidden. So no valid q_0 exists!

So p_r = 0 for all r doesn't work. The HE bugs need different cycle positions.

Let me think about this differently. The forbidden set for (r, c) is {±(r-c), ±(r+c)} mod 18. Let me think about what these values are.

For r+c odd, both r-c and r+c are odd. So the forbidden values are all odd. And q_c - p_r is odd (since q_c is odd, p_r is even). So we need q_c - p_r to be an odd number not in the forbidden set.

The odd numbers mod 18 are: 1, 3, 5, 7, 9, 11, 13, 15, 17 (9 values). The forbidden set has at most 4 values. So there are at least 5 allowed values for each pair. But we need to satisfy all pairs simultaneously.

For a given c, the constraint is: for all r with r+c odd, q_c - p_r ∉ {±(r-c), ±(r+c)} mod 18.

This is a constraint on q_c given the p_r values. We need to choose p_r and q_c to satisfy all constraints.

This is a complex combinatorial problem. Let me try to think about it from a higher level.

Actually, let me reconsider the problem. Maybe the answer is 50, or 20, or something else. Let me think about upper bounds more carefully.

Upper bound via counting:

Consider the 18 time steps. At each time step t, the bugs occupy distinct squares. 

For each row r, at time t, the number of bugs in row r is at most 10. These bugs are either horizontal (in row r) or vertical (passing through row r at time t).

The number of horizontal bugs in row r is h_r (at most 2). The number of vertical bugs in row r at time t is the number of vertical bugs whose unfolded row at time t maps to r.

A vertical bug in column c with unfolded row v is at row g(v+t) at time t. It's in row r iff v+t ≡ ±r (mod 18). For a given t and r, the unfolded rows that map to r are: r-t and 18-r-t (mod 18) (or just one if r=0 or r=9).

So at time t, in row r, the vertical bugs are those in columns c where the vertical bug's unfolded row v satisfies v ≡ r-t or v ≡ -(r+t) (mod 18). For each such v, the vertical bugs with that unfolded row are in some columns.

This is getting very involved. Let me try to think about the problem from the perspective of the answer.

Let me consider the possibility that the answer is 50.

Actually, let me think about a cleaner upper bound. 

Consider the "unfolded" representation. Each bug has an unfolded coordinate (u for horizontal, v for vertical) in Z_18, and a fixed coordinate (row r for horizontal, column c for vertical).

At time t, a horizontal bug (r, u) is at position (r, g(u+t)). A vertical bug (v, c) is at position (g(v+t), c).

Now, consider the "sum" s = u + r for a horizontal bug, or s = v + c for a vertical bug. And the "difference" d = u - r for horizontal, d = v - c for vertical.

Hmm, I'm not sure this helps directly. Let me think about invariants.

For a horizontal bug (r, u): at time t, position is (r, g(u+t)). The "unfolded position" is (r, u+t). As t varies, the unfolded column advances.

For a vertical bug (v, c): at time t, position is (g(v+t), c). The "unfolded position" is (v+t, c).

Collision at time t: (r, g(u+t)) = (g(v+t), c), i.e., r = g(v+t) and g(u+t) = c. In unfolded terms: v+t ≡ ±r and u+t ≡ ±c (mod 18).

Let me think about the quantity u + v (mod 18) for a pair (H bug (r,u), V bug (v,c)). Collision requires v+t ≡ ±r and u+t ≡ ±c. Adding: u+v+2t ≡ ±r ± c (mod 18). The four cases give u+v+2t ≡ r+c, r-c, -r+c, -r-c (mod 18), i.e., u+v+2t ≡ ±(r+c) or ±(r-c) (mod 18).

Subtracting: v-u ≡ ±r ∓ c (mod 18), which is the condition we had before.

From the adding version: u+v+2t ≡ ±(r±c) (mod 18). For this to have a solution in t, we need ±(r±c) - (u+v) to be even, i.e., u+v ≡ r±c (mod 2), i.e., u+v ≡ r+c (mod 2) (since r-c ≡ r+c mod 2). This is the parity condition again.

OK I think I need to try a more computational approach, even though I can't use tools. Let me try to carefully construct a solution and find the maximum.

Let me think about the problem differently. Let me consider the "type" of each square (r, c) at time t. 

Actually, let me think about a key structural observation. 

Consider the 18×18 unfolded torus. Each horizontal bug (r, u) corresponds to a line on the torus: at time t, unfolded position (r, u+t) - but r is in {0,...,9}, not Z_18. So it's not a full torus.

Hmm, let me think about this differently. Let me consider the "doubled" board. Instead of a 10×10 board, consider an 18×18 board where the bouncing is unfolded. Each square (r, c) on the 10×10 board corresponds to squares (r, c) and (r, 18-c) on the 18×18 board (for c ≠ 0, 9), and just (r, c) for c = 0, 9. Similarly for rows.

Actually, the standard unfolding for a 1D bouncing motion on {0,...,9} gives a cycle of length 18 in Z_18. The mapping is g: Z_18 → {0,...,9} where g(k) = k if k ≤ 9, g(k) = 18-k if k ≥ 10.

For the 2D board, a horizontal bug unfolds to a point moving on {0,...,9} × Z_18 (row stays, column unfolds). A vertical bug unfolds to a point moving on Z_18 × {0,...,9} (row unfolds, column stays).

Two bugs collide on the original board iff their unfolded positions map to the same original position at the same time.

This is a complex constraint. Let me try to think about the maximum by considering specific constructions.

Let me try to construct a solution with 50 bugs.

Idea: Place 5 horizontal bugs and 5 vertical bugs, or some other split. Actually, let me think about what the maximum could be.

Let me reconsider. With 4 types (HE, HO, VE, VO), each with at most 10 bugs, the naive upper bound is 40. But cross-constraints reduce this. Can we achieve 40? Or is the maximum lower?

Let me think about whether 40 is achievable. We'd need 10 HE + 10 HO + 10 VE + 10 VO = 40 bugs, with all cross-constraints satisfied.

The cross-constraints are:
- HE(r, p) & VE(c, q): r+c even, q-p ≡ ±(r-c) or ±(r+c) (mod 18) → collision.
- HE(r, p) & VO(c, q): r+c odd, q-p ≡ ±(r-c) or ±(r+c) (mod 18) → collision.
- HO(r, p) & VE(c, q): r+c odd, q-p ≡ ±(r-c) or ±(r+c) (mod 18) → collision.
- HO(r, p) & VO(c, q): r+c even, q-p ≡ ±(r-c) or ±(r+c) (mod 18) → collision.

For 40 bugs, we need one HE bug per row, one HO bug per row, one VE bug per column, one VO bug per column. That's a lot of cross-constraints (10*10*4 = 400 pairs to check, roughly).

This seems very hard to achieve. Let me think about whether there's a fundamental obstruction.

Consider the HE and VE bugs. HE has one bug per row, VE has one bug per column. For each pair (r, c) with r+c even (50 pairs), we need q_c - p_r ∉ {±(r-c), ±(r+c)} (mod 18). Since q_c and p_r are both even, q_c - p_r is even. The forbidden values ±(r-c) and ±(r+c) are also even (since r+c even implies r-c even). So we need q_c - p_r to be an even value not in the forbidden set.

The even values mod 18 are: 0, 2, 4, 6, 8, 10, 12, 14, 16 (9 values). The forbidden set has at most 4 values. So at least 5 allowed values per pair.

But with 50 pairs, this is a lot of constraints. Let me think about whether they can all be satisfied.

For a fixed c, the constraints from all r with r+c even (5 values of r) give at most 5*4 = 20 forbidden values for q_c - p_r. But q_c - p_r depends on both q_c and p_r, so it's not just about q_c.

This is a constraint satisfaction problem that's hard to solve by hand. Let me think about whether there's a cleaner upper bound.

Let me try a different approach to the upper bound.

Consider the quantity Q = (unfolded_column + row) mod 2 for horizontal bugs, and Q = (unfolded_row + column) mod 2 for vertical bugs.

For a horizontal bug (r, u): Q_H = (u + r) mod 2.
For a vertical bug (v, c): Q_V = (v + c) mod 2.

Now, when do a horizontal bug (r, u) and vertical bug (v, c) collide? We need v+t ≡ ±r and u+t ≡ ±c (mod 18). 

From v+t ≡ r: v+t ≡ r → v-r ≡ -t. And u+t ≡ c → u-c ≡ -t. So v-r ≡ u-c → v-u ≡ r-c.
From v+t ≡ r, u+t ≡ -c: v-r ≡ u+c → v-u ≡ r+c.
Etc.

The parity condition: (u+v) mod 2 = (r+c) mod 2, i.e., (u-r) mod 2 = (c-v) mod 2, i.e., (u+r) mod 2 = (v+c) mod 2 (since u-r ≡ u+r mod 2 and c-v ≡ c+v mod 2). So Q_H = Q_V!

So a horizontal bug and a vertical bug can only collide if Q_H = Q_V. If Q_H ≠ Q_V, they never collide.

This is a useful observation! It means we can split the bugs into two groups based on Q, and bugs in different groups never collide with each other (cross-type).

But within the same group, horizontal bugs still conflict with each other (same row, same parity), and vertical bugs conflict with each other (same column, same parity).

Wait, let me also check: do two horizontal bugs with different Q values conflict? Two horizontal bugs in the same row r with cycle positions u1, u2: they conflict iff u1 ≡ u2 (mod 2). Q1 = (u1+r) mod 2, Q2 = (u2+r) mod 2. If u1 ≡ u2 (mod 2), then Q1 = Q2. If u1 ≢ u2 (mod 2), then Q1 ≠ Q2 and they don't conflict. So two horizontal bugs in the same row conflict iff they have the same Q. This means in each row, at most one bug per Q value, so at most 2 (one Q=0, one Q=1). Consistent with before.

Similarly for vertical bugs in the same column.

Now, the key insight: if Q_H = Q_V, a horizontal and vertical bug MIGHT collide (need more conditions). If Q_H ≠ Q_V, they NEVER collide.

So let's split into two groups:
- Group 0: bugs with Q = 0.
- Group 1: bugs with Q = 1.

Bugs in different groups never collide (cross-type). Within each group, horizontal bugs in the same row conflict (at most 1 per row per group), vertical bugs in the same column conflict (at most 1 per column per group), and horizontal-vertical pairs might conflict.

So each group has at most 10 horizontal bugs (one per row) + 10 vertical bugs (one per column) = 20 bugs. Two groups → at most 40 bugs. But cross-constraints within each group may reduce this.

Wait, but I already had the bound of 40 from the 4-type analysis. The Q grouping gives the same bound. Let me think about whether 40 is achievable.

Within group 0: at most 10 H bugs + 10 V bugs = 20. Within group 1: at most 10 H bugs + 10 V bugs = 20. Total: 40.

But within each group, the H-V cross-constraints must be satisfied. Let me think about whether we can achieve 20 per group.

In group 0, we have one H bug per row and one V bug per column. The H bug in row r has Q = 0, so (u_r + r) mod 2 = 0, i.e., u_r ≡ r (mod 2). The V bug in column c has Q = 0, so (v_c + c) mod 2 = 0, i.e., v_c ≡ c (mod 2).

Collision condition: v_c - u_r ≡ ±(r-c) or ±(r+c) (mod 18), AND Q_H = Q_V = 0 (which is already satisfied).

So we need: for all (r, c), v_c - u_r ∉ {±(r-c), ±(r+c)} (mod 18).

With u_r ≡ r (mod 2) and v_c ≡ c (mod 2), v_c - u_r ≡ c - r (mod 2). And ±(r-c) ≡ r-c ≡ r+c (mod 2). So v_c - u_r ≡ ±(r-c) (mod 2) always. So the parity condition is always satisfied, meaning collisions are always possible (the parity doesn't rule anything out).

So within a group, we need to avoid the specific forbidden values. This is the hard part.

Let me try to think about this as an assignment problem. We need to choose u_r (even if r even, odd if r odd, for group 0) and v_c (even if c even, odd if c odd, for group 0) such that v_c - u_r ∉ {r-c, c-r, r+c, -(r+c)} (mod 18) for all r, c.

Let me think about the number of choices. For group 0:
- u_r: even if r even (r ∈ {0,2,4,6,8}, u_r ∈ {0,2,4,6,8,10,12,14,16}, 9 choices), odd if r odd (r ∈ {1,3,5,7,9}, u_r ∈ {1,3,5,7,9,11,13,15,17}, 9 choices). So 9 choices per row.
- v_c: similarly 9 choices per column.

We need to satisfy 100 constraints (one per (r,c) pair). Each constraint forbids 4 values of v_c - u_r (out of 18, but with the right parity, out of 9).

This is a complex CSP. Let me try to find a pattern.

Let me try u_r = 2r (mod 18) and v_c = 2c (mod 18) for group 0. Wait, but u_r must have the same parity as r. 2r is always even, so this only works for even r. For odd r, u_r must be odd. Let me try u_r = 2r + (r mod 2) = 2r if r even, 2r+1 if r odd. Hmm, that's just u_r = 2r + (r%2). For r=0: 0, r=1: 3, r=2: 4, r=3: 7, r=4: 8, r=5: 11, r=6: 12, r=7: 15, r=8: 16, r=9: 19≡1.

Similarly v_c = 2c + (c%2). Same values.

Then v_c - u_r = 2(c-r) + (c%2 - r%2). If r and c have the same parity, v_c - u_r = 2(c-r). If different, v_c - u_r = 2(c-r) ± 1.

The forbidden values are {r-c, c-r, r+c, -(r+c)} mod 18.

Let me check r=0, c=0: v_0 - u_0 = 0. Forbidden: {0, 0, 0, 0} = {0}. 0 ∈ {0}. Collision! 

So this doesn't work. Let me try a different approach.

Let me try u_r = 0 for all r (in group 0, u_r must have parity of r, so this only works for even r). Hmm, this doesn't work for odd r.

OK let me think about this more carefully. Maybe I should consider a different splitting.

Actually, let me reconsider the Q value. For group 0, u_r ≡ r (mod 2) and v_c ≡ c (mod 2). The forbidden values for (r,c) are {r-c, c-r, r+c, -(r+c)} mod 18. Note that:
- r-c and c-r are negatives of each other.
- r+c and -(r+c) are negatives.
- r-c and r+c differ by 2c.
- c-r and -(r+c) differ by 2c + 2r = 2(r+c)... no, c-r - (-(r+c)) = c-r+r+c = 2c.

So the four forbidden values are {±(r-c), ±(r+c)}. In Z_18, these are {r-c, 18-(r-c), r+c, 18-(r+c)} (taking representatives in 0-17).

For the pair (r, c) = (0, 0): forbidden = {0, 0, 0, 0} = {0}. So v_0 - u_0 ≠ 0 (mod 18).
For (r, c) = (0, 1): forbidden = {-1, 1, 1, -1} = {1, 17}. So v_1 - u_0 ∉ {1, 17}.
For (r, c) = (1, 0): forbidden = {1, -1, 1, -1} = {1, 17}. So v_0 - u_1 ∉ {1, 17}.
For (r, c) = (1, 1): forbidden = {0, 0, 2, -2} = {0, 2, 16}. So v_1 - u_1 ∉ {0, 2, 16}.

Hmm, let me try a different approach. Let me try to see if 20 per group is achievable by trying small examples.

Actually, let me step back and think about the problem from a higher level. Maybe the answer is not 40 but something else.

Let me reconsider. The problem is on a 10×10 board. Let me think about what's special about 10.

The period is 2(10-1) = 18. The number of even values in Z_18 is 9, and odd values is 9.

Hmm, let me think about the problem for a general n×n board and see if there's a pattern.

For a 2×2 board: period 2. Each row has 2 columns, unfolding to 2 positions. Two horizontal bugs in the same row: cycle positions 0 and 1 (different parity), so they don't collide. So 2 per row, 2 rows = 4 horizontal bugs. But the board only has 4 squares, and at time 0, we'd have 4 bugs on 4 squares. At time 1, each bug moves. A horizontal bug in row 0 at column 0 moving right goes to column 1. A horizontal bug in row 0 at column 1 moving left goes to column 0. So they swap. Similarly for row 1. So at time 1, all 4 squares are still occupied. At time 2, they're back to original. So 4 bugs work for a 2×2 board. Can we do better? No, 4 is the max (only 4 squares).

But wait, can we add vertical bugs too? If all 4 squares are occupied by horizontal bugs, there's no room for vertical bugs. So the max is 4 for a 2×2 board.

For a 3×3 board: period 4. Each row unfolds to 4 positions. Two horizontal bugs in the same row collide iff same parity. So at most 2 per row (one even, one odd), 3 rows = 6 horizontal bugs. Similarly 6 vertical bugs. Can we mix?

With 6 horizontal bugs (2 per row), at time 0, each row has 2 bugs in 2 of its 3 columns. So 6 squares occupied, 3 free. Can we add vertical bugs in those free squares?

A vertical bug in column c at time 0 is at some row. It needs to not collide with any horizontal bug at any time.

This is getting complicated. Let me try to think about the 10×10 case more directly.

Let me try a different approach to the upper bound.

Consider the "diagonal" structure. Define for each bug a value in Z_18:
- Horizontal bug (r, u): define α = u - r (mod 18) and β = u + r (mod 18).
- Vertical bug (v, c): define α = v - c (mod 18) and β = v + c (mod 18).

Wait, let me think about what the collision condition looks like in terms of these.

H bug (r, u) and V bug (v, c) collide iff v - u ≡ ±(r-c) or ±(r+c) (mod 18).

v - u ≡ r - c → (v-c) ≡ (u-r) → α_V = α_H.
v - u ≡ -(r-c) = c-r → (v+c) ≡ (u+r) → β_V = β_H. Wait: v - u = c - r → v + r = u + c → v - c = u - r... no. v - u = c - r → v + r = u + c. Hmm, let me redo.

v - u ≡ r - c (mod 18): rearranging, v + c ≡ u + r (mod 18), i.e., β_V ≡ β_H.
v - u ≡ c - r (mod 18): rearranging, v - c ≡ u - r (mod 18), i.e., α_V ≡ α_H.
v - u ≡ r + c (mod 18): rearranging, v - c ≡ u + r (mod 18), i.e., α_V ≡ β_H.
v - u ≡ -(r + c) (mod 18): rearranging, v + c ≡ u - r (mod 18), i.e., β_V ≡ α_H.

So H bug (r, u) and V bug (v, c) collide iff:
- α_V = α_H, or
- β_V = β_H, or
- α_V = β_H, or
- β_V = α_H.

Where α_H = u - r, β_H = u + r, α_V = v - c, β_V = v + c (all mod 18).

So collision iff {α_V, β_V} ∩ {α_H, β_H} ≠ ∅ (mod 18).

This is a much cleaner condition! A horizontal bug has two "keys" (α_H, β_H) and a vertical bug has two "keys" (α_V, β_V). They collide iff they share a common key.

Now, for a horizontal bug (r, u): α_H = u - r, β_H = u + r. Note that α_H + β_H = 2u and β_H - α_H = 2r. So given α_H and β_H, we can recover u = (α_H + β_H)/2 and r = (β_H - α_H)/2 (mod 9, since we're dividing by 2 mod 18... hmm, division by 2 mod 18 is not well-defined since 2 is not invertible mod 18).

Actually, α_H and β_H have the same parity (since α_H + β_H = 2u is even). So α_H ≡ β_H (mod 2). Similarly, α_V ≡ β_V (mod 2).

Also, r = (β_H - α_H)/2. For this to give a valid r ∈ {0,...,9}, we need β_H - α_H to be even (which it is) and (β_H - α_H)/2 mod 9 ∈ {0,...,9}. Wait, (β_H - α_H)/2 mod 9 gives a value in {0,...,8}, but r can be 0-9. Hmm, since we're working mod 18, β_H - α_H can be any even number mod 18, and dividing by 2 gives a value mod 9, which is 0-8. But r ∈ {0,...,9}. So r = 9 is not achievable? 

Wait, let me reconsider. r ∈ {0,...,9} and u ∈ {0,...,17}. α_H = u - r mod 18, β_H = u + r mod 18. Given r and u, we get specific α_H, β_H. Given α_H, β_H (with same parity), we get u = (α_H + β_H)/2 mod 9 (but u is mod 18, so u = (α_H + β_H)/2 or (α_H + β_H)/2 + 9). And r = (β_H - α_H)/2 mod 9 (but r is 0-9, so r = (β_H - α_H)/2 mod 9, giving 0-8, or r = 9 if...).

Hmm, this is getting messy because of the mod 18 vs mod 9 issue. Let me think about it differently.

The key observation is: H bug (r, u) and V bug (v, c) collide iff {α_H, β_H} ∩ {α_V, β_V} ≠ ∅ (mod 18), where α_H = u-r, β_H = u+r, α_V = v-c, β_V = v+c.

Now, for a horizontal bug, α_H and β_H are two values in Z_18 with the same parity. For a vertical bug, similarly.

The condition is that the horizontal bug's key set {α_H, β_H} and the vertical bug's key set {α_V, β_V} are disjoint.

Now, let's think about the constraints within horizontal bugs. Two horizontal bugs in the same row r with cycle positions u1, u2: they collide iff u1 ≡ u2 (mod 2). In terms of keys: α1 = u1-r, β1 = u1+r, α2 = u2-r, β2 = u2+r. If u1 ≡ u2 (mod 2), then α1 ≡ α2 (mod 2) and β1 ≡ β2 (mod 2). But the collision condition is about same parity, not same key.

Hmm, the key formulation helps for H-V collisions but not for H-H or V-V collisions. Let me focus on the H-V collisions using the key formulation.

So the problem reduces to: choose horizontal bugs (each with a key pair {α, β} of same parity) and vertical bugs (each with a key pair {α, β} of same parity) such that:
1. No two horizontal bugs in the same row have the same parity cycle position.
2. No two vertical bugs in the same column have the same parity cycle position.
3. No horizontal bug's key pair intersects any vertical bug's key pair.

Condition 3 means: the set of all keys used by horizontal bugs and the set of all keys used by vertical bugs are disjoint.

Let S_H = set of all keys used by horizontal bugs = ∪ over all H bugs of {α_H, β_H}.
Let S_V = set of all keys used by vertical bugs = ∪ over all V bugs of {α_V, β_V}.
We need S_H ∩ S_V = ∅.

Now, the keys are in Z_18. There are 18 keys total. S_H and S_V partition a subset of Z_18.

Each horizontal bug uses 2 keys. Each vertical bug uses 2 keys. If we have h horizontal bugs and v vertical bugs, then |S_H| ≤ 2h and |S_V| ≤ 2v (could be less if keys are shared among bugs of the same type).

We need |S_H| + |S_V| ≤ 18 (since they're disjoint subsets of Z_18). So 2h + 2v ≤ 18 is not quite right because keys can be shared within the same type. But it gives h + v ≤ 9 if all keys are distinct, which is too restrictive.

Wait, keys CAN be shared within the same type (H-H or V-V). Two horizontal bugs can share a key as long as they're in different rows or have different parity cycle positions. So |S_H| can be much less than 2h.

Let me think about this more carefully. How many horizontal bugs can share the same key?

A key k is used by a horizontal bug (r, u) if α_H = k (i.e., u - r = k) or β_H = k (i.e., u + r = k). 

For α_H = k: u = r + k (mod 18). For this to be a valid cycle position, u ∈ {0,...,17}, which it is (any r + k mod 18 is in {0,...,17}). And r ∈ {0,...,9}. So there are 10 horizontal bugs with α_H = k (one for each row r, with u = r + k mod 18). But we can only have at most 2 per row (one even, one odd). The parity of u = r + k is (r + k) mod 2. For a given k, in row r, u = r + k has parity (r+k) mod 2. So in each row, there's exactly one bug with α_H = k (the one with u = r+k). But we need to check if two such bugs (in different rows) conflict. They're in different rows, so they don't conflict (H-H collision only happens within the same row). So all 10 bugs with α_H = k can coexist!

Similarly for β_H = k: u = k - r (mod 18), and there are 10 such bugs (one per row), all in different rows, so they can coexist.

But can a bug with α_H = k and a bug with β_H = k coexist? They're both using key k. If they're in different rows, yes. If in the same row, they need different parity cycle positions. Bug 1: u1 = r + k, bug 2: u2 = k - r. u1 - u2 = 2r. If 2r is odd... but 2r is always even. So u1 ≡ u2 (mod 2), meaning they have the same parity and would conflict if in the same row. So in each row, we can have at most one of {α_H = k bug, β_H = k bug}.

So for a given key k, the maximum number of horizontal bugs using key k is 10 (all with α_H = k, one per row) or 10 (all with β_H = k), but not both in the same row. So we could have 10 bugs with α_H = k (one per row) and that's it, or we could mix: in some rows use α_H = k, in others use β_H = k, but not both in the same row. So still at most 10 per key.

But wait, a single bug uses TWO keys. So if we have 10 bugs all with α_H = k, they also each have a β_H key. Bug in row r: α_H = k, β_H = k + 2r (mod 18). So the β_H keys are k, k+2, k+4, ..., k+18 = k. So β_H takes values k, k+2, k+4, k+6, k+8, k+10, k+12, k+14, k+16, k (for r = 0, 1, ..., 9). So β_H = k + 2r mod 18, which for r = 0,...,9 gives k, k+2, k+4, k+6, k+8, k+10, k+12, k+14, k+16, k. So the β_H values are {k, k+2, k+4, k+6, k+8, k+10, k+12, k+14, k+16} = all values with the same parity as k. And k appears twice (r=0 and r=9).

So if all 10 horizontal bugs have α_H = k, then S_H includes k (from α_H) and all same-parity values (from β_H). So S_H = {all values with same parity as k} = 9 values. And these are all the same-parity values in Z_18.

Then S_V must be disjoint from S_H, so S_V ⊆ {values with opposite parity to k} = 9 values. Each vertical bug uses 2 keys, both of the same parity (opposite to k). So vertical bugs' keys are all from these 9 values.

How many vertical bugs can we have using only these 9 keys? Each vertical bug uses 2 keys. The keys are α_V = v - c and β_V = v + c, both with parity opposite to k. 

By the same argument as for horizontal bugs, we can have up to 10 vertical bugs (one per column) using a single key, say α_V = k' (where k' has opposite parity to k). These 10 bugs would use keys {k'} (from α_V) and {k' + 2c : c = 0,...,9} = {all values with same parity as k'} (from β_V). So S_V = {all values with parity opposite to k} = 9 values. And S_H ∩ S_V = ∅. ✓

So we can have 10 horizontal bugs + 10 vertical bugs = 20 bugs, with S_H = {even values} and S_V = {odd values} (or vice versa).

But can we do better? Can we have more than 10 horizontal bugs?

With 10 horizontal bugs (one per row, all with α_H = k), we've used up all 9 keys of one parity. Can we add more horizontal bugs? An additional horizontal bug in row r would need a cycle position of different parity (since we already have one per row). Its keys would be of the opposite parity. But the opposite parity keys are all in S_V. So this additional H bug would share a key with some V bug, causing a collision. Unless we remove some V bugs.

So there's a tradeoff: more H bugs of the opposite parity → fewer V bugs.

Let me think about this more carefully. Suppose we have:
- h1 horizontal bugs with even-parity keys (using some even keys).
- h2 horizontal bugs with odd-parity keys (using some odd keys).
- v1 vertical bugs with even-parity keys.
- v2 vertical bugs with odd-parity keys.

Constraints:
- S_H_even ∩ S_V_even = ∅ (even keys used by H and V must be disjoint).
- S_H_odd ∩ S_V_odd = ∅ (odd keys used by H and V must be disjoint).
- (H-H and V-V constraints as before.)

S_H_even ∪ S_V_even ⊆ {even keys} (9 values).
S_H_odd ∪ S_V_odd ⊆ {odd keys} (9 values).

Each H bug with even keys uses 2 even keys. Each V bug with even keys uses 2 even keys. The total even keys used is |S_H_even| + |S_V_even| ≤ 9.

Now, how many H bugs can use a given set of even keys? As argued, up to 10 H bugs can share a single key (one per row). But each H bug uses 2 keys. If all 10 H bugs share the same α key, they use 1 + 9 = 10... wait, no. They use 1 α key and up to 9 β keys (as computed). So |S_H_even| = 9 (all even keys) if we have 10 bugs all with the same α.

But if we have fewer H bugs, we might use fewer keys, leaving more for V bugs.

Let me think about the tradeoff. Suppose we use e_H even keys for H bugs and e_V even keys for V bugs, with e_H + e_V ≤ 9. Similarly, o_H + o_V ≤ 9 for odd keys.

The number of H bugs with even keys is at most... well, it depends on how the keys are used. Let me think about the maximum number of H bugs using a given number of even keys.

If we have e_H even keys available for H bugs, how many H bugs (with even cycle positions) can we place?

Each H bug with even cycle position u in row r has α = u - r and β = u + r, both even. The bug uses 2 even keys. Multiple bugs can share keys.

In a given row r, we can have at most 1 H bug with even cycle position. So at most 10 H bugs with even cycle positions (one per row).

Each such bug uses 2 even keys. The keys are α = u - r and β = u + r. For bugs in different rows, the keys can overlap.

The question is: what is the minimum number of even keys needed to support 10 H bugs (one per row, each with even cycle position)?

For row r, the bug has u_r (even), α_r = u_r - r, β_r = u_r + r. Note α_r + β_r = 2u_r (even ✓) and β_r - α_r = 2r.

We want to minimize |{α_r, β_r : r = 0,...,9}|.

β_r - α_r = 2r, so α_r and β_r are determined by each other given r. Specifically, β_r = α_r + 2r. So the keys are {α_r, α_r + 2r} for each r.

To minimize the total number of distinct keys, we want the α_r values to be chosen so that the sets {α_r, α_r + 2r} overlap as much as possible.

If we set α_r = k for all r (constant), then the keys are {k, k + 2r : r = 0,...,9} = {k, k+2, k+4, ..., k+16, k+18=k} = {k, k+2, k+4, k+6, k+8, k+10, k+12, k+14, k+16}. That's 9 distinct even values (all even values if k is even). So |S_H_even| = 9.

Can we do better? What if we don't use all 10 rows? If we use only 5 rows, we might use fewer keys. For example, rows 0, 2, 4, 6, 8 (even rows). Set α_r = k for all. Keys: {k, k+2r} for r = 0, 2, 4, 6, 8 = {k, k, k+4, k+8, k+12, k+16} = {k, k+4, k+8, k+12, k+16}. That's 5 keys. So 5 H bugs using 5 even keys.

Or rows 0, 1, 2, 3, 4 with α_r = k: keys = {k, k, k+2, k+2, k+4, k+4, k+6, k+6, k+8, k+8} = {k, k+2, k+4, k+6, k+8}. 5 keys for 5 bugs.

In general, it seems like n H bugs (one per row, with even cycle positions) use at least n even keys (if we're clever about it) and at most 9.

Wait, can we do better than n keys for n bugs? Each bug uses 2 keys, but keys can be shared. Two bugs in rows r1 and r2 share a key if {α_{r1}, β_{r1}} ∩ {α_{r2}, β_{r2}} ≠ ∅. This happens if α_{r1} = α_{r2} or α_{r1} = β_{r2} or β_{r1} = α_{r2} or β_{r1} = β_{r2}.

α_{r1} = α_{r2}: u_{r1} - r1 = u_{r2} - r2, so u_{r1} - u_{r2} = r1 - r2.
β_{r1} = β_{r2}: u_{r1} + r1 = u_{r2} + r2, so u_{r1} - u_{r2} = r2 - r1.
α_{r1} = β_{r2}: u_{r1} - r1 = u_{r2} + r2, so u_{r1} - u_{r2} = r1 + r2.
β_{r1} = α_{r2}: u_{r1} + r1 = u_{r2} - r2, so u_{r1} - u_{r2} = -(r1 + r2).

So bugs in rows r1 and r2 share a key iff u_{r1} - u_{r2} ≡ ±(r1 - r2) or ±(r1 + r2) (mod 18). But this is exactly the collision condition for H-V bugs! Wait, no, this is the condition for two H bugs to share a key, which is different from colliding.

Actually, sharing a key is fine for two H bugs (they're in different rows, so they don't collide). The key sharing just means the key set is smaller.

So to minimize the key set, we want maximum key sharing. The condition for bugs in rows r1, r2 to share a key is u_{r1} - u_{r2} ≡ ±(r1-r2) or ±(r1+r2) (mod 18).

If we set u_r = 2r (even for all r), then u_{r1} - u_{r2} = 2(r1 - r2). The sharing condition: 2(r1-r2) ≡ ±(r1-r2) or ±(r1+r2) (mod 18).
- 2(r1-r2) ≡ (r1-r2): r1-r2 ≡ 0 (mod 18), only if r1=r2.
- 2(r1-r2) ≡ -(r1-r2): 3(r1-r2) ≡ 0 (mod 18), i.e., r1-r2 ≡ 0 (mod 6).
- 2(r1-r2) ≡ (r1+r2): r1-3r2 ≡ 0 (mod 18).
- 2(r1-r2) ≡ -(r1+r2): 3r1-r2 ≡ 0 (mod 18).

So with u_r = 2r, bugs in rows r1 and r2 share a key iff r1-r2 ≡ 0 (mod 6) or r1-3r2 ≡ 0 (mod 18) or 3r1-r2 ≡ 0 (mod 18).

For r1-r2 ≡ 0 (mod 6): rows that differ by 6. So rows 0 and 6, 1 and 7, 2 and 8, 3 and 9 share a key. That's 4 pairs.

This is getting complicated. Let me try a different approach.

Let me think about the problem as an optimization. We want to maximize h + v where h is the number of horizontal bugs and v is the number of vertical bugs, subject to:
- At most 2 H bugs per row (one even, one odd cycle position).
- At most 2 V bugs per column (one even, one odd cycle position).
- S_H ∩ S_V = ∅ (key sets disjoint).

Let me think about the key budget. There are 18 keys (9 even, 9 odd). H bugs use some keys, V bugs use the rest.

For H bugs with even cycle positions: they use even keys. Let's say they use e_H even keys.
For H bugs with odd cycle positions: they use odd keys. Let's say they use o_H odd keys.
For V bugs with even cycle positions: they use even keys. Let's say they use e_V even keys.
For V bugs with odd cycle positions: they use odd keys. Let's say they use o_V odd keys.

Constraints: e_H + e_V ≤ 9, o_H + o_V ≤ 9.

Now, the number of H bugs with even cycle positions is at most 10 (one per row), and they use at least... how many even keys?

Let me think about the minimum number of even keys needed for k H bugs with even cycle positions.

If we place k H bugs (one per row, for k specific rows) with even cycle positions, the minimum number of even keys used is... let me think.

Each bug uses 2 keys. But keys can be shared. The minimum number of keys is at least 1 (if all bugs share both keys, but that's impossible since different rows give different β = α + 2r values).

Actually, if all bugs have the same α key, then the β keys are α + 2r for each row r used. If the rows are r_1, ..., r_k, the β keys are α + 2r_1, ..., α + 2r_k (mod 18). These are distinct iff the 2r_i are distinct mod 18, i.e., the r_i are distinct mod 9. Since r_i ∈ {0,...,9} and we have at most 10 rows, two rows can give the same β: r and r+9 (but r+9 > 9 for r ≥ 1, so only r=0 and r=9 give the same β = α + 0 and α + 18 = α). Wait, 2*0 = 0 and 2*9 = 18 ≡ 0. So rows 0 and 9 give the same β key. So if we use both rows 0 and 9, the β keys overlap.

So for k bugs with the same α key, the number of distinct keys is 1 + |{2r_i mod 18 : i = 1,...,k}|. The 2r_i mod 18 values are distinct unless two rows differ by 9        — AI历史解题过程（thinking）
#   polymath_00218         — 题目ID

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
  <problem_id>polymath_00218</problem_id>
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

Some bugs are sitting on squares of $10\times 10$ board. Each bug has a direction associated with it [b](up, down, left, right)[/b]. After 1 second, the bugs jump one square in [b]their associated [/b]direction. When the bug reaches the edge of the board, the associated direction reverses (up becomes down, left becomes right, down becomes up, and right becomes left) and the bug moves in that direction. It is observed that it is [b]never[/b] the case that two bugs are on same square. What is the maximum number of bugs possible on the board?

## Standard Solution

1. **Initial Setup and Problem Understanding:**
   - We have a $10 \times 10$ board.
   - Each bug moves in one of four directions: up, down, left, or right.
   - When a bug reaches the edge of the board, it reverses direction.
   - No two bugs can occupy the same square at any time.

2. **Proving 41 Bugs is Impossible:**
   - Color the board in a chessboard pattern (alternating black and white squares).
   - Each bug moves either in a row or a column.
   - By the Pigeonhole Principle, if there are 41 bugs, at least 3 bugs must be in the same row or column.
   - Again, by the Pigeonhole Principle, at least 2 of these bugs must be on the same color (either both on black squares or both on white squares).
   - Since they are on the same color and move in the same row or column, they will eventually collide.
   - Therefore, having 41 bugs is impossible.

3. **Proving 40 Bugs is Possible:**
   - We need to show that 40 bugs can be placed on the board such that they never collide.
   - Since bugs on white squares never collide with bugs on black squares, we can consider only white squares first.
   - We need to place 20 bugs on white squares such that they never collide.

4. **Labeling and Timing:**
   - Label the rows and columns from $0$ to $9$.
   - Let $r_i$ be the time taken by the bug in the $i^{th}$ row to reach the leftmost column.
   - Let $c_i$ be the time taken by the bug in the $i^{th}$ column to reach the topmost row.
   - Note that $0 \leq r_i, c_i \leq 17$.

5. **Parity Condition:**
   - For all $i$, $r_i - i$ and $c_i - i$ must have the same parity (either both even or both odd).

6. **Non-Collision Condition:**
   - The condition that the bug in the $i^{th}$ row doesn't collide with the one in the $j^{th}$ column is:
     \[
     (r_i \pm j) \neq (c_j \pm i)
     \]
     This simplifies to:
     \[
     (r_i \pm i) \neq (c_j \pm j)
     \]
     Let $a_i = r_i - i$ and $b_i = c_i - i$. Then the condition is:
     \[
     \{a_i, a_i + 2i\} \cap \{b_j, b_j + 2j\} = \emptyset
     \]

7. **Constructing Sets $A$ and $B$:**
   - Let $A = \{a_i \mid i = 0, 1, \dots, 9\}$ and $B = \{b_j \mid j = 0, 1, \dots, 9\}$.
   - Ensure that $A$ and $B$ are disjoint and:
     \[
     \{a_i + 2i \mid i = 0, 1, \dots, 9\} = A
     \]
     \[
     \{b_j + 2j \mid j = 0, 1, \dots, 9\} = B
     \]

8. **Example Construction:**
   - Start with:
     \[
     A = \{2, 4, 6, 10\} \quad \text{and} \quad B = \{8, 12, 14, 16\}
     \]
   - From this, find the sequences:
     \[
     a = (2, 2, 6, 4, 2, 10, 10, 6, 4, 2)
     \]
     \[
     b = (12, 12, 12, 8, 8, 16, 14, 12, 14, 12)
     \]
   - These sequences satisfy the conditions for all $i$ and $j$.

9. **Final Configuration:**
   - Use $r_i = a_i + i$ and $c_i = b_i + i$ to place bugs on white squares.
   - Similarly, place bugs on black squares to get a configuration for 40 bugs that never collide.

The final answer is $\boxed{40}$.

## AI's Thinking (Attempted Solution Process)

Let me solve this problem. It's about bugs on a 10x10 board, each with a direction. After 1 second, each bug jumps one square in its direction. When a bug reaches the edge, its direction reverses and it moves that way. It's observed that it's never the case that two bugs are on the same square. Find the maximum number of bugs.

Let me think about this carefully.

The board is 10x10. Each bug has a position and a direction (up, down, left, right). After each second, the bug moves one square in its direction. When it reaches the edge, the direction reverses.

Let me think about the motion. A bug moving horizontally: it bounces back and forth. If it's in row r, column c, moving right, it goes c → c+1 → ... → 9 → 8 → ... → 0 → 1 → ... So the column cycles with period 18 (goes 0 to 9 then back to 0, that's 18 steps). Similarly for vertical motion.

Actually, let me think about this more carefully. The bug moves one square per second. When it reaches the edge of the board, the direction reverses. So if a bug is at column 9 moving right, it reverses to left and moves to column 8. If a bug is at column 0 moving left, it reverses to right and moves to column 1.

So the column position as a function of time: starting at column c, moving right. The position cycles through 0,1,...,9,8,7,...,1,0,1,...,9,8,... with period 18.

Actually, let me think of it as a "reflection" model. The position on a line of length 10 (positions 0-9). Moving right from position c: at time t, position is c+t if c+t ≤ 9, then bounces. The period is 18.

Let me use the standard unfolding trick. For a line of n positions (0 to n-1), the motion with reflection has period 2(n-1). For n=10, period is 18.

Now, the key constraint: at no time do two bugs occupy the same square. This must hold for ALL time (since it's "never" the case).

Let me think about what configurations are possible.

Each bug's state is (row, column, direction). The direction is one of 4. The total state space per bug is 10*10*4 = 400.

But the motion is deterministic. So each bug follows a fixed trajectory. Two bugs collide if at some time t, they're at the same position.

Let me think about the trajectory of a bug. A bug moving right in row r: its row stays r, column cycles with period 18. A bug moving left in row r: same thing but phase-shifted. A bug moving up in column c: column stays c, row cycles with period 18. A bug moving down in column c: same but phase-shifted.

So horizontal bugs stay in their row, vertical bugs stay in their column.

Two horizontal bugs in different rows never collide. Two horizontal bugs in the same row: they could collide. Two vertical bugs in different columns never collide. A horizontal bug and a vertical bug can collide if they're at the intersection at the same time.

Let me think about the period. The whole system has period lcm(18, 18) = 18. So we need to check collisions over 18 time steps (t = 0, 1, ..., 17), or actually we need to check that no two bugs are ever at the same position at the same time.

Wait, actually the period is 18 for both horizontal and vertical motion. So the entire system is periodic with period 18. We need to check t = 0, 1, ..., 17 (and t=0 is the same as t=18).

Hmm, but actually we need to be more careful. The initial state includes the direction. Let me think about the state of a horizontal bug in row r. Its state is (r, c, direction) where direction is left or right. The column motion has period 18, and the direction also has period 18 (it reverses at the edges). So the full state (r, c, direction) of a horizontal bug has period 18.

Similarly for vertical bugs.

So the system has period 18. We need no collisions at any of the 18 time steps t=0,...,17.

Now let me think about maximizing the number of bugs.

First, consider only horizontal bugs. In a given row r, how many horizontal bugs can we place such that no two ever collide?

In row r, a horizontal bug's column position over time is a function of time with period 18. The column takes values 0-9. Two bugs in the same row collide if at some time t, they have the same column.

A horizontal bug in row r with initial column c and direction right: at time t, column = f(c, t) where f is the bouncing function. The key insight: two bugs in the same row never collide if and only if their trajectories never coincide.

Actually, let me think about this differently. In a single row, the motion is on a path of 10 nodes (0-9) with reflection at ends. This is equivalent to motion on a cycle of 18 nodes (the "unfolded" path). Each bug occupies one position on this cycle at each time, and moves one step per unit time on the cycle. Two bugs collide iff they're at the same position on the cycle at the same time, which happens iff they're at the same position on the cycle at time 0 (since they all move at the same speed in the same direction on the cycle).

Wait, that's the key insight! On the unfolded cycle, all bugs move in the same direction (say clockwise) at the same speed (1 per unit time). So two bugs on the same cycle collide iff they start at the same position on the cycle.

The unfolded cycle for a row of 10: positions 0,1,...,9,8,7,...,1 (that's 18 positions, forming a cycle). Each position on the cycle corresponds to a (column, direction) pair. Position 0 on cycle = (col 0, right), position 1 = (col 1, right), ..., position 9 = (col 9, right), position 10 = (col 8, left), position 11 = (col 7, left), ..., position 17 = (col 1, left).

Wait, let me re-derive. A bug at column c moving right: at time 0 it's at column c. At time t, on the unfolded cycle, it's at position c + t (mod 18). The cycle position p maps to: if p ≤ 9, column = p, direction = right; if p > 9, column = 18 - p, direction = left.

So position 0 → (0, R), 1 → (1, R), ..., 9 → (9, R), 10 → (8, L), 11 → (7, L), ..., 17 → (1, L).

A bug at column c moving left: at time 0, on the cycle, where is it? If it's at column c moving left, then at time 1 it's at column c-1 (if c > 0) or it reverses. On the cycle, moving left means... hmm, let me think again.

Actually, on the unfolded cycle, ALL bugs move in the same direction (increasing cycle position). A bug moving right at column c starts at cycle position c. A bug moving left at column c: at time 0 it's at column c moving left. At time 1, it moves to column c-1 (if c > 0). On the cycle, position c-1+1 = c... no wait.

Let me reconsider. The unfolded cycle has 18 positions. At cycle position p, the bug is at column g(p) where g(p) = p if p ≤ 9, and g(p) = 18-p if p ≥ 10. The direction at cycle position p is right if p ≤ 9, left if p ≥ 10.

All bugs move one step forward on the cycle per unit time (p → p+1 mod 18). This is because:
- A bug at cycle position p ≤ 9 (column p, moving right): next position is p+1. If p < 9, that's column p+1, moving right. If p = 9, next is position 10, which is column 8, moving left. That matches: at column 9 moving right, it reverses and moves to column 8. ✓
- A bug at cycle position p ≥ 10 (column 18-p, moving left): next position is p+1. If p < 17, that's column 18-(p+1) = 17-p, moving left. So from column 18-p to column 17-p, moving left. ✓. If p = 17, next is position 0 (mod 18), which is column 0, moving right. From column 1 (18-17=1) moving left, it goes to column 0, then reverses to right. ✓

Great, so all bugs on the same row move in the same direction on the cycle at the same speed. Therefore, two bugs in the same row collide at some time iff they start at the same cycle position iff they have the same (column, direction) pair. But wait, that means two bugs in the same row with different (column, direction) pairs NEVER collide!

That's a powerful result. In a single row, we can place up to 18 horizontal bugs (one at each cycle position), and they never collide with each other. But wait, there are only 10 columns, and 2 directions, so there are 20 possible (column, direction) pairs for horizontal bugs, but only 18 cycle positions. The pairs (0, L) and (9, R) don't appear on the cycle... let me check.

Cycle position 0: (0, R). Position 9: (9, R). Position 10: (8, L). Position 17: (1, L).

What about (0, L)? A bug at column 0 moving left: it immediately reverses (it's at the edge) and moves right. So at time 0, it's at (0, L), but at time 1, it's at (1, R). On the cycle, this would be... at time 0, cycle position should be such that at time 1, it's at position 1 (column 1, right). So at time 0, it's at position 0 (column 0, right). But that contradicts - the bug is at (0, L) not (0, R).

Hmm, I think the issue is that (0, L) and (0, R) are different states but they map to the same cycle position. Let me reconsider.

Actually, when a bug is at column 0 moving left, it's at the edge. The problem says "when the bug reaches the edge of the board, the associated direction reverses and the bug moves in that direction." So if a bug is at column 0 and its direction is left, it's at the edge, so it reverses to right and moves right. So at time 1, it's at column 1 moving right.

But at time 0, it's at column 0 moving left. This is a valid state. On the cycle, this corresponds to... position 0 (since column 0, and the next move is to the right). But position 0 on the cycle is (0, R), not (0, L).

I think the issue is that (0, L) and (0, R) are the same trajectory - they both result in the bug being at column 0 at time 0 and column 1 at time 1. The direction at the edge is ambiguous in some sense, or rather, (0, L) immediately becomes (0, R) before moving.

Actually, re-reading the problem: "After 1 second, the bugs jump one square in their associated direction. When the bug reaches the edge of the board, the associated direction reverses."

So the process is: the bug has a direction. After 1 second, it jumps in that direction. If it reaches the edge (i.e., it's at the edge and would jump off), the direction reverses and it moves in the new direction.

So if a bug is at column 0 with direction left: it's at the edge. The direction reverses to right. It moves to column 1. So after 1 second, it's at column 1 with direction right.

If a bug is at column 0 with direction right: it moves to column 1 with direction right.

So both (0, L) and (0, R) lead to the same next state (1, R). They're effectively the same at the edge. Similarly, (9, R) and (9, L) both lead to (8, L).

So the effective state space for a horizontal bug in a row is 18 states (the 18 cycle positions), where the edge states (0 and 9) have only one effective direction.

OK so in a single row, we can place at most 18 horizontal bugs (one per cycle position), and they never collide. But wait, at time 0, multiple cycle positions can map to the same column. For example, cycle position 0 (column 0, right) and cycle position 18... no, 18 mod 18 = 0. Let me check: which cycle positions map to column 0? Only position 0. Which map to column 9? Only position 9. Which map to column 1? Positions 1 (right) and 17 (left). So at time 0, two bugs at cycle positions 1 and 17 would both be at column 1 - they'd collide at time 0!

So the constraint is not just about the cycle - at time 0, two bugs at different cycle positions can be at the same column. The cycle argument says they never collide at any time t ≥ 0 if they're at different cycle positions. But at time 0, two different cycle positions can map to the same column!

Wait, no. If two bugs are at different cycle positions, they're never at the same cycle position at any time (since they all move at the same speed). And the column is determined by the cycle position. So two bugs at different cycle positions are never at the same column at the same time. At time 0, bug A at cycle position 1 is at column 1, bug B at cycle position 17 is at column 1. Wait, that's the same column!

Hmm, but cycle position 1 maps to column 1, and cycle position 17 maps to column 18-17 = 1. So both are at column 1 at time 0. But they're at different cycle positions (1 and 17), and at time t, they're at positions 1+t and 17+t (mod 18), which are always different. But the columns g(1+t) and g(17+t) could be the same at some time.

Oh wait, I see the issue. Two bugs at different cycle positions are at different cycle positions at all times, but different cycle positions can map to the same column. So they CAN be at the same column at the same time even with different cycle positions!

Let me re-examine. Bug A at cycle position 1, bug B at cycle position 17. At time 0: A at column 1, B at column 1. Collision! So they do collide.

So my earlier reasoning was wrong. Two bugs in the same row collide iff at some time t, their cycle positions map to the same column. Since g(p) = g(18-p) for p ≠ 0 (and g(0) = 0, g(9) = 9), two bugs at cycle positions p and q collide at time t iff g(p+t) = g(q+t) (mod 18), which happens iff p+t ≡ q+t (mod 18) or p+t ≡ -(q+t) (mod 18) and p+t ≠ 0 (well, more precisely g(a) = g(b) iff a ≡ b or a + b ≡ 0 or a + b ≡ 18, but since we're mod 18, a + b ≡ 0 mod 18).

Wait, g(a) = g(b) iff a ≡ b (mod 18) or a + b ≡ 0 (mod 18). Because g(a) = a if a ≤ 9, g(a) = 18-a if a ≥ 10 (for a in 0..17). And g(a) = g(b) means either a = b, or a = 18-b (i.e., a + b = 18), or... let me just check: g(a) = g(b) iff a = b or a + b = 18 (when both in 1..17) or a = b = 0 or a = b = 9. Actually, g(a) = g(b) iff a = b or a + b ≡ 0 (mod 18) with a, b ≠ 0. Hmm, let me just enumerate: g(0)=0, g(1)=1, g(2)=2,...,g(9)=9, g(10)=8, g(11)=7,...,g(17)=1. So g(a)=g(b) with a≠b iff {a,b} = {k, 18-k} for k=1,...,8 (giving g=k), or {a,b}={0,0} (trivial), {9,9} (trivial). Also g(0)=0 is unique, g(9)=9 is unique.

So g(a) = g(b) with a ≠ b iff a + b ≡ 18 (mod 18), i.e., a + b ≡ 0 (mod 18), and a ≠ 0 (since g(0)=0 is unique, and 0+0=0 but that's a=b).

Actually, a+b ≡ 0 (mod 18) with a ≠ b: pairs are (1,17), (2,16), ..., (8,10), and also (0,0) but that's a=b, and (9,9) but that's a=b. So the collision pairs are (k, 18-k) for k=1,...,8.

So two bugs at cycle positions p and q (in the same row) collide at time t iff p+t ≡ q+t (mod 18) [i.e., p=q, same bug] or (p+t) + (q+t) ≡ 0 (mod 18) [i.e., p+q+2t ≡ 0 (mod 18)].

The second condition: p + q + 2t ≡ 0 (mod 18) for some t ∈ {0,...,17}. This is solvable iff gcd(2, 18) | (p+q), i.e., 2 | (p+q), i.e., p and q have the same parity.

So two bugs in the same row at cycle positions p and q (p ≠ q) collide at some time iff p + q is even, i.e., p and q have the same parity.

Therefore, to avoid collisions in a single row, we need all bugs to have cycle positions of the same parity... no wait, we need no two bugs to have the same parity. That means at most one bug of each parity? No, we need all pairs to have different parities, which means all bugs have the same parity? No...

If p and q have the same parity, they collide. If p and q have different parities, they don't collide. So to avoid all collisions, we need all pairs to have different parities, which means... we can have at most 2 bugs? No, that's not right either. We need every pair (p,q) to have different parities. That means all bugs must have the same parity? No, if all have the same parity, then every pair has the same parity, and they all collide.

Wait, I need to re-read. Two bugs collide iff p and q have the same parity. So to AVOID collision, we need p and q to have DIFFERENT parities. For ALL pairs, we need different parities. But with more than 2 bugs, by pigeonhole, at least two will have the same parity. So at most 2 bugs per row? That seems too few.

Hmm wait, let me double-check with a small example. Row of 10, bugs at cycle positions 0 and 2 (both even). At time t, positions are t and t+2 (mod 18). They collide when g(t) = g(t+2), i.e., t + (t+2) ≡ 0 (mod 18), i.e., 2t + 2 ≡ 0 (mod 18), i.e., 2t ≡ -2 ≡ 16 (mod 18), i.e., t ≡ 8 (mod 9). So t = 8 or t = 17. At t=8: positions 8 and 10, g(8)=8, g(10)=8. Yes, collision at column 8. ✓

Bugs at cycle positions 0 and 1 (different parity). Collision when 2t + 1 ≡ 0 (mod 18), i.e., 2t ≡ 17 (mod 18). Since gcd(2,18)=2 and 2∤17, no solution. So they never collide. ✓

So indeed, in a single row, at most 2 horizontal bugs (one even cycle position, one odd cycle position)? Wait, but we could have multiple bugs with even cycle positions as long as no two of them collide. But I just showed that any two bugs with the same parity collide. So indeed, at most 1 even + 1 odd = 2 bugs per row.

Hmm, but that seems very restrictive. Let me reconsider.

Actually wait. I need to also check: two bugs at cycle positions p and q with the same parity always collide? The condition is p + q + 2t ≡ 0 (mod 18) for some t. If p + q is even, then 2t ≡ -(p+q) (mod 18). Since p+q is even, -(p+q) is even, and gcd(2,18) = 2, so 2t ≡ even (mod 18) has solutions. Yes, always solvable. So yes, any two bugs with the same parity in the same row will collide.

So in a single row, at most 2 horizontal bugs. With 10 rows, that's at most 20 horizontal bugs.

Similarly, in a single column, at most 2 vertical bugs. With 10 columns, at most 20 vertical bugs.

But we can mix horizontal and vertical bugs. The constraint is:
1. No two horizontal bugs in the same row with the same parity cycle position.
2. No two vertical bugs in the same column with the same parity cycle position.
3. No horizontal bug and vertical bug at the same position at the same time.

Let me think about constraint 3. A horizontal bug in row r at cycle position p_h: at time t, it's at (r, g(p_h + t)). A vertical bug in column c at cycle position p_v: at time t, it's at (g(p_v + t), c). They collide at time t iff r = g(p_v + t) and c = g(p_h + t).

This is more complex. Let me think about the overall structure.

Total bugs = (horizontal bugs) + (vertical bugs). We want to maximize this.

Let me think about it differently. Each bug has a "cycle position" which is its position on the unfolded cycle (0-17). The parity of the cycle position determines which "class" it's in.

For horizontal bugs in row r: at most one with even cycle position, at most one with odd cycle position. So at most 2 per row.

For vertical bugs in column c: at most one with even cycle position, at most one with odd cycle position. So at most 2 per column.

Now, the cross-constraint between horizontal and vertical bugs.

Let me think about this more carefully using the unfolding idea. 

Actually, let me think about the problem in terms of the "unfolded" coordinates. 

For a horizontal bug in row r with cycle position p: at time t, position is (r, g(p+t)).
For a vertical bug in column c with cycle position q: at time t, position is (g(q+t), c).

Collision at time t: r = g(q+t) and g(p+t) = c.

So we need: for all t, it's not the case that (r = g(q+t) AND c = g(p+t)).

Equivalently, there's no t such that g(q+t) = r AND g(p+t) = c.

g(q+t) = r means q+t ≡ r (mod 18) or q+t ≡ 18-r (mod 18) (i.e., q+t ≡ -r mod 18), assuming r ≠ 0 (if r=0, only q+t ≡ 0; if r=9, only q+t ≡ 9).

Similarly g(p+t) = c means p+t ≡ c or p+t ≡ -c (mod 18).

So we need: there's no t such that (q+t ≡ ±r AND p+t ≡ ±c) (mod 18), where the ± is independent (4 combinations), with the caveat that for r=0 or r=9, only one sign works, and similarly for c.

From q+t ≡ s₁ (mod 18) and p+t ≡ s₂ (mod 18), we get t ≡ s₁ - q ≡ s₂ - p (mod 18), so s₁ - q ≡ s₂ - p (mod 18), i.e., s₁ - s₂ ≡ q - p (mod 18).

So a collision exists iff there exist signs such that (±r) - (±c) ≡ q - p (mod 18), where the four combinations of signs are considered (with restrictions at edges).

The four combinations give: r-c, r+c, -r-c, -r+c, i.e., ±(r-c) and ±(r+c). So collision iff q - p ≡ ±(r-c) or q - p ≡ ±(r+c) (mod 18).

Equivalently, q - p ≡ r - c, r + c, -r - c, or -r + c (mod 18).

Which is q - p ≡ ±(r-c) or q - p ≡ ±(r+c) (mod 18).

Hmm, this is getting complex. Let me think about it from a higher level.

Let me define for each bug a "type" based on the parity of its cycle position. There are two parities (even and odd). 

For horizontal bugs: even parity bugs in different rows don't interact (they're in different rows). Even parity bugs in the same row: at most 1. Similarly for odd parity.

For vertical bugs: even parity bugs in different columns don't interact. Even parity bugs in the same column: at most 1. Similarly for odd.

Cross interactions: a horizontal bug (row r, cycle position p) and a vertical bug (column c, cycle position q) collide iff q - p ≡ ±(r-c) or ±(r+c) (mod 18).

Note that q - p mod 2 = (q mod 2) - (p mod 2) mod 2 = (q + p) mod 2. So the parity of q - p is the parity of p + q.

And ±(r-c) has parity (r+c) mod 2, and ±(r+c) has parity (r+c) mod 2. So all four values ±(r-c), ±(r+c) have the same parity, namely (r+c) mod 2.

So a collision is possible only if (p + q) mod 2 = (r + c) mod 2.

If p and q have the same parity, then p + q is even, so we need r + c even.
If p and q have different parities, then p + q is odd, so we need r + c odd.

This is a necessary condition for collision, not sufficient. But it gives us a parity constraint.

Let me think about this problem differently. Let me consider the "parity class" of a bug. A horizontal bug in row r with cycle position p has parity p mod 2. A vertical bug in column c with cycle position q has parity q mod 2.

Let me split into two independent problems: even-parity bugs and odd-parity bugs. Two bugs of different parities never collide with each other (within the same row/column, we showed same parity collides, different parity doesn't; and for cross interactions, the parity condition shows different parities can only collide if r+c is odd, but...).

Hmm wait, that's not quite right. Let me reconsider.

Two horizontal bugs in the same row: same parity → collide, different parity → don't collide.
Two vertical bugs in the same column: same parity → collide, different parity → don't collide.
Horizontal and vertical bug: can collide only if (p+q) mod 2 = (r+c) mod 2.

So even-parity horizontal bugs and even-parity vertical bugs can collide if r+c is even.
Even-parity horizontal and odd-parity vertical can collide if r+c is odd.
Etc.

This is getting complicated. Let me try a different approach.

Let me think about the problem as a graph coloring / independent set problem.

Actually, let me try to think about small cases first and see if I can find a pattern.

For a 10x10 board, let me try to find the maximum.

Let me consider the "unfolded" representation. Each bug is characterized by:
- Type: H (horizontal) or V (vertical)
- If H: row r (0-9), cycle position p (0-17)
- If V: column c (0-9), cycle position q (0-17)

Constraints:
1. Two H bugs in same row with same parity p: collide. So at most 1 H bug per (row, parity).
2. Two V bugs in same column with same parity q: collide. So at most 1 V bug per (column, parity).
3. H bug (r, p) and V bug (c, q) collide iff q-p ≡ ±(r-c) or ±(r+c) (mod 18), AND (p+q) mod 2 = (r+c) mod 2.

Wait, condition 3 already includes the parity condition. Let me re-derive.

H bug (r, p) and V bug (c, q): collision iff ∃ t such that g(q+t) = r and g(p+t) = c.

g(q+t) = r: q+t ≡ r or q+t ≡ 18-r (mod 18), with the edge cases.
g(p+t) = c: p+t ≡ c or p+t ≡ 18-c (mod 18).

From these: t ≡ (r or 18-r) - q and t ≡ (c or 18-c) - p. So:
(r or 18-r) - q ≡ (c or 18-c) - p (mod 18)

Four cases:
1. r - q ≡ c - p → q - p ≡ r - c
2. r - q ≡ 18-c - p → q - p ≡ r + c - 18 ≡ r + c (mod 18)
3. 18-r - q ≡ c - p → q - p ≡ 18 - r - c ≡ -(r+c) (mod 18)
4. 18-r - q ≡ 18-c - p → q - p ≡ c - r ≡ -(r-c) (mod 18)

So q - p ≡ ±(r-c) or ±(r+c) (mod 18). (With edge case restrictions, but let's ignore those for now and consider them later.)

Now, the key observation: q - p mod 2 determines the parity. And ±(r-c) and ±(r+c) all have the same parity as r+c (since r-c = r+c-2c, same parity as r+c).

So collision requires (q-p) ≡ (r+c) (mod 2), i.e., p+q ≡ r+c (mod 2).

Now, let me think about this as follows. Let's define the "parity" of a bug as p mod 2 (for H bugs) or q mod 2 (for V bugs). And the "position parity" as r mod 2 (for H bugs, since they're in row r) or c mod 2 (for V bugs, since they're in column c).

Actually, let me think about it more carefully. Let me separate bugs by the parity of their cycle position.

Even bugs: cycle position is even.
Odd bugs: cycle position is odd.

Within even bugs:
- Two H bugs in the same row: both even, same parity → collide. At most 1 per row.
- Two V bugs in the same column: both even, same parity → collide. At most 1 per column.
- H bug (r, p_even) and V bug (c, q_even): p+q is even, r+c must be even for collision. So collision possible only if r+c is even.

Within odd bugs: similar, but p+q is even (both odd), so again r+c must be even.

Cross (even H, odd V): p+q is odd, r+c must be odd for collision.
Cross (odd H, even V): p+q is odd, r+c must be odd.

Hmm, this is still complex. Let me try to think about the problem computationally. But the rules say I can't use tools. Let me think more carefully.

Let me try a different approach. Let me think about what happens at each time step.

At time t, each bug is at some position on the board. The constraint is that at every time t, all bugs are at distinct positions. Since there are 100 squares, at most 100 bugs at any time. But the constraint is stronger because it must hold for all t.

Let me think about the period. The system has period 18. At each of the 18 time steps, the bugs occupy distinct squares. So over 18 time steps, each bug visits 18 squares (its trajectory). The constraint is that at each time step, the bugs' positions are distinct.

This is like a scheduling problem. Each bug has a "schedule" (its trajectory of 18 positions, one per time step). We need to select a maximum set of bugs such that at each time step, no two bugs are at the same position.

The total "capacity" is 18 * 100 = 1800 (position-time slots). Each bug uses 18 slots. So a naive upper bound is 1800/18 = 100. But this is just the trivial bound (100 squares).

But the constraint is per-time-step, not total. At each time step, at most 100 bugs. So at most 100 bugs total (since each bug is at exactly one position at each time step). But can we achieve 100?

If we could place 100 bugs such that at each time step, they fill the entire board, that would be optimal. But is that possible?

Let me think about it. At time 0, we need 100 bugs at 100 distinct squares - so every square is occupied. At time 1, every bug moves, and again every square must be occupied. Etc.

This is like a permutation of the 100 squares at each time step, where each bug's movement is constrained by the bouncing rules.

Hmm, but not every permutation is achievable. Each bug either moves horizontally (stays in its row) or vertically (stays in its column). 

Let me think about this. If all bugs are horizontal, then at each time step, the bugs in each row permute among the columns of that row. But with the bouncing constraint, the permutation is very specific.

Actually, with horizontal bugs only: in each row, the bugs move according to the cycle. At time t, a bug at cycle position p is at column g(p+t). If we have k bugs in a row at cycle positions p_1, ..., p_k, then at time t, they're at columns g(p_1+t), ..., g(p_k+t). For these to be distinct, we need g(p_i+t) ≠ g(p_j+t) for all i≠j and all t. As we showed, this requires all p_i to have distinct parities, so at most 2 per row. With 10 rows, at most 20 horizontal bugs.

Similarly, at most 20 vertical bugs.

But with a mix, we can do better. Let me think about the maximum.

Let me consider a specific construction. Suppose we use both horizontal and vertical bugs.

Let me think about the parity classes more carefully.

Define:
- H_even: horizontal bugs with even cycle position. At most 1 per row (10 total).
- H_odd: horizontal bugs with odd cycle position. At most 1 per row (10 total).
- V_even: vertical bugs with even cycle position. At most 1 per column (10 total).
- V_odd: vertical bugs with odd cycle position. At most 1 per column (10 total).

So naive upper bound: 10 + 10 + 10 + 10 = 40.

But cross-constraints reduce this. Let me analyze the cross-constraints.

H bug (r, p) and V bug (c, q) collide iff q-p ≡ ±(r-c) or ±(r+c) (mod 18).

Let me consider the four parity combinations:

1. H_even (p even) and V_even (q even): q-p is even. Collision iff q-p ≡ ±(r-c) or ±(r+c) (mod 18). Since q-p is even, we need ±(r-c) or ±(r+c) to be even, i.e., r+c even. If r+c is odd, no collision. If r+c is even, collision is possible (depends on specific values).

2. H_even (p even) and V_odd (q odd): q-p is odd. Collision requires r+c odd. If r+c even, no collision.

3. H_odd (p odd) and V_even (q even): q-p is odd. Collision requires r+c odd.

4. H_odd (p odd) and V_odd (q odd): q-p is even. Collision requires r+c even.

So:
- Same parity (both even or both odd): collision possible only if r+c even.
- Different parity: collision possible only if r+c odd.

Now, r+c even means r and c have the same parity. r+c odd means r and c have different parities.

Let me think about the board as a chessboard with black (r+c even) and white (r+c odd) squares.

For same-parity bugs (H_even with V_even, or H_odd with V_odd): collision possible only at "black" intersections (r, c) where r+c is even.
For different-parity bugs (H_even with V_odd, or H_odd with V_even): collision possible only at "white" intersections (r, c) where r+c is odd.

This is still complex. Let me try to think about specific constructions.

Let me try to maximize the total. Let me consider using H_even and V_odd (or H_odd and V_even), since different parity combinations have collision only at white squares.

Actually, let me think about this more carefully. Let me try to use H_even and V_even, and see how many we can place.

H_even: at most 1 per row, so at most 10. Let's say we place H_even bugs in rows 0-9, with even cycle positions p_0, ..., p_9.
V_even: at most 1 per column, so at most 10. Let's say we place V_even bugs in columns 0-9, with even cycle positions q_0, ..., q_9.

Collision between H_even(r, p_r) and V_even(c, q_c): requires r+c even AND q_c - p_r ≡ ±(r-c) or ±(r+c) (mod 18).

If r+c is even, we need to avoid q_c - p_r ≡ ±(r-c) or ±(r+c) (mod 18).

The even values mod 18 are: 0, 2, 4, 6, 8, 10, 12, 14, 16. There are 9 even values.

For a given (r, c) with r+c even, the forbidden values of q_c - p_r are: r-c, -(r-c), r+c, -(r+c) (mod 18). Some of these might coincide.

r-c mod 18: since r, c ∈ {0,...,9}, r-c ∈ {-9,...,9}, so r-c mod 18 ∈ {0,...,9, 9,...,17} = {0,...,17}. Actually r-c mod 18 is (r-c+18) mod 18.

The four forbidden values are ±(r-c) and ±(r+c) mod 18. Since r+c ∈ {0,...,18} and r-c ∈ {-9,...,9}:

Let me think about how many distinct forbidden values there are. ±(r-c) gives two values (or one if r=c), and ±(r+c) gives two values (or one if r+c=0 or r+c=9... well r+c=0 only if r=c=0, r+c=18 only if r=c=9).

In general, the four values r-c, -(r-c), r+c, -(r+c) mod 18. Note that r-c and -(r-c) are negatives, r+c and -(r+c) are negatives. Also, r-c = r+c - 2c, so they're related.

The number of distinct forbidden values is at most 4, but could be 2 or 3 in special cases.

This is getting very complex. Let me try a different approach - let me think about the problem in terms of a cleaner formulation.

Alternative approach: Think of each bug as having a "trajectory" which is a set of 18 (position, time) pairs. We need to select a maximum set of bugs with pairwise non-intersecting trajectories.

Actually, let me reconsider the problem. Let me think about what the trajectories look like.

A horizontal bug in row r with cycle position p: at time t, it's at (r, g(p+t)). Its trajectory is {(r, g(p+t)) : t = 0, ..., 17}. Since g has period 18 and g(p+t) takes each value in {0,...,9} with g(k) appearing twice (for k and 18-k) except g(0)=0 and g(9)=9 which appear once. So the bug visits each column in its row, with columns 1-8 visited twice and columns 0, 9 visited once. Total: 8*2 + 2 = 18. ✓

A vertical bug in column c with cycle position q: at time t, it's at (g(q+t), c). Similar.

Now, two bugs collide if their trajectories share a common (position, time) pair.

Let me think about this as a bipartite-like structure. 

Hmm, let me try yet another approach. Let me think about the problem in terms of "lines" on the board.

Each horizontal bug stays in its row. Each vertical bug stays in its column. A horizontal bug in row r and a vertical bug in column c can only collide at the intersection (r, c). They collide at (r, c) if there's a time t when both are there.

The horizontal bug is at (r, c) at times t where g(p+t) = c, i.e., p+t ≡ c or p+t ≡ 18-c (mod 18). So t ≡ c-p or t ≡ 18-c-p (mod 18). Two times (or one if c = 18-c, i.e., c = 9, or c = 0).

The vertical bug is at (r, c) at times t where g(q+t) = r, i.e., t ≡ r-q or t ≡ 18-r-q (mod 18). Two times (or one).

They collide if any of these times coincide, which gives the condition we derived.

OK let me try to think about this more carefully with a cleaner model.

Let me use the "unfolded" coordinates. For a horizontal bug in row r with cycle position p, define its "unfolded column" as u = p (an element of Z_18). At time t, unfolded column is u+t, and actual column is g(u+t).

For a vertical bug in column c with cycle position q, define its "unfolded row" as v = q. At time t, unfolded row is v+t, and actual row is g(v+t).

Collision at time t: g(v+t) = r and g(u+t) = c. In unfolded coordinates: v+t ≡ ±r and u+t ≡ ±c (mod 18). So v-u ≡ ±r ∓ c (mod 18), giving the four cases.

Let me define d = v - u (mod 18) (the difference of unfolded coordinates). Then collision iff d ≡ ±r ± c (mod 18) for some combination of signs, i.e., d ∈ {r-c, r+c, -r-c, -r+c} (mod 18) = {±(r-c), ±(r+c)} (mod 18).

So for a horizontal bug in row r with unfolded column u, and a vertical bug in column c with unfolded row v, they collide iff v - u ≡ ±(r-c) or ±(r+c) (mod 18).

Now, the key insight: this condition depends on r, c, u, v. Specifically, it depends on the difference v - u and the position (r, c).

Let me think about this as follows. Consider the "difference" d = v - u (mod 18). For a given pair (H bug at (r, u), V bug at (c, v)), collision iff d ∈ {±(r-c), ±(r+c)} (mod 18).

Now, for a fixed r and c, the set {±(r-c), ±(r+c)} mod 18 has at most 4 elements. So out of 18 possible values of d, at most 4 cause collision.

But we need to avoid collisions for ALL pairs (H bug, V bug). This is a constraint satisfaction problem.

Let me try to think about upper bounds more carefully.

Upper bound approach: Consider the 18 time steps. At each time step, the bugs occupy distinct squares. Each horizontal bug is always in its row, each vertical bug always in its column.

At time t, in row r, the horizontal bugs in row r occupy some columns, and the vertical bugs whose unfolded row at time t maps to r also occupy some columns in row r. The total in row r is at most 10.

Let me count more carefully. At time t:
- Horizontal bugs in row r: these are at columns g(p_i + t) for each H bug i in row r.
- Vertical bugs at row r at time t: a V bug in column c with unfolded row v is at row g(v+t). It's in row r when g(v+t) = r, i.e., v+t ≡ ±r (mod 18). For each such V bug, it occupies column c in row r.

So at time t, in row r, the occupied columns are: {g(p_i+t) : H bug i in row r} ∪ {c : V bug in column c, g(v_j+t) = r}.

These must all be distinct, and there are at most 10.

This is complex. Let me try to think about specific constructions and upper bounds.

Let me try a cleaner approach. Let me think about the "conflict graph" and try to find the maximum independent set.

Actually, let me try to think about the problem by considering the parity structure more carefully.

Let me define the "color" of a bug. For a horizontal bug in row r with cycle position p, define its color as (p mod 2, r mod 2) ∈ {0,1}². For a vertical bug in column c with cycle position q, define its color as (q mod 2, c mod 2) ∈ {0,1}².

Hmm, I'm not sure this leads anywhere clean. Let me try to think about the problem differently.

Let me consider the following: at each time t, the board is a 10x10 grid. Horizontal bugs occupy positions in their rows, vertical bugs in their columns. The constraint is that at each time, all positions are distinct.

Let me think about a relaxation. Suppose we only care about time t=0. Then we just need all bugs at distinct positions at time 0. This allows up to 100 bugs. But the constraint is for all t.

Let me think about what makes the problem hard. The bouncing motion creates correlations between positions at different times.

Let me try to think about the problem in terms of "conflict" between bugs.

Two horizontal bugs in the same row conflict iff same parity (as shown). 
Two vertical bugs in the same column conflict iff same parity.
A horizontal bug (r, p) and vertical bug (c, v) conflict iff v - p ≡ ±(r-c) or ±(r+c) (mod 18).

Let me try to find the maximum by considering specific constructions.

Construction 1: All horizontal bugs. At most 2 per row (one even, one odd), 10 rows → 20 bugs.

Construction 2: All vertical bugs. Similarly 20.

Construction 3: Mix. Let me try to use some rows for horizontal bugs and some columns for vertical bugs.

Suppose we use rows 0-4 for horizontal bugs (2 per row = 10) and columns 0-4 for vertical bugs (2 per column = 10). But we need to check cross-constraints.

A horizontal bug in row r (r ∈ {0,...,4}) and a vertical bug in column c (c ∈ {0,...,4}) collide iff v - p ≡ ±(r-c) or ±(r+c) (mod 18).

For this to not happen, we need to choose the cycle positions carefully.

Hmm, this is getting complicated. Let me try to think about it from a different angle.

Let me consider the "unfolded board." Instead of a 10x10 board with bouncing, think of an 18x18 unfolded board where bugs move in straight lines.

Actually, here's a cleaner way to think about it. The unfolding maps the 10x10 board with bouncing to an 18x18 torus where bugs move in straight lines. Each bug moves one step per unit time in a fixed direction on the torus.

Horizontal bug in row r: on the torus, it's at "unfolded row" r' and "unfolded column" u, moving in the +column direction. The unfolded row r' is... hmm, the row doesn't change for horizontal bugs, so the unfolded row is just r (or some function of r). Actually, the row stays fixed, so there's no unfolding needed for the row. The column unfolds to 18 positions.

Wait, but the board is 10x10, and only the column unfolds for horizontal bugs (to 18 positions), and only the row unfolds for vertical bugs (to 18 positions). So it's not a clean 18x18 torus.

Let me think about it differently. Let me consider the "state space" of each bug. A horizontal bug's state is (row, unfolded_column) ∈ {0,...,9} × Z_18. A vertical bug's state is (unfolded_row, column) ∈ Z_18 × {0,...,9}. At each time step, the unfolded coordinate advances by 1.

Two horizontal bugs collide iff they have the same (row, unfolded_column) at some time, iff they have the same (row, unfolded_column) at all times (since they move at the same speed), iff they have the same (row, unfolded_column) at time 0. But wait, two different unfolded_columns can map to the same actual column. So they collide in the actual board iff g(u1 + t) = g(u2 + t) for some t, which as we showed happens iff u1 ≡ u2 or u1 + u2 ≡ 0 (mod 18)... no, iff u1 and u2 have the same parity (as I showed earlier, two bugs in the same row collide iff their cycle positions have the same parity).

Wait, I think I need to be more careful. Two bugs in the same row with unfolded columns u1 and u2: they collide at time t iff g(u1+t) = g(u2+t). This happens iff (u1+t) + (u2+t) ≡ 0 (mod 18) [and u1+t ≠ u2+t, but if u1 ≠ u2 this is automatic for the relevant t], i.e., u1 + u2 + 2t ≡ 0 (mod 18). Solvable iff u1 + u2 is even, i.e., same parity.

OK so my earlier analysis was correct.

Let me try to think about the maximum using a counting argument.

Consider the 18 time steps. At each time step, the 100 squares are partitioned among the bugs. Each bug occupies one square per time step. Over 18 time steps, each bug occupies 18 squares (with possible repeats, but at distinct times).

Total bug-time slots: 18 * (number of bugs). These must fit into 18 * 100 = 1800 slots, but with the constraint that at each time step, no two bugs share a square. So the number of bugs ≤ 100 (trivial).

But we can get a better bound by considering the structure.

At time t, in row r, the bugs present are:
- Horizontal bugs in row r (always present in row r)
- Vertical bugs that happen to be in row r at time t

The number of horizontal bugs in row r is at most 2 (as shown). The number of vertical bugs in row r at time t is the number of vertical bugs whose unfolded row at time t maps to r. 

A vertical bug with unfolded row v is at actual row g(v+t). For a given r, g(v+t) = r iff v+t ≡ r or v+t ≡ 18-r (mod 18). So at most 2 unfolded rows map to r at each time (or 1 if r=0 or r=9). But multiple vertical bugs could have the same unfolded row v (they'd be in different columns though).

Hmm, this is getting complicated. Let me try to think about upper bounds by considering specific time steps.

At time t, the board has 100 squares. Horizontal bugs occupy some, vertical bugs occupy others. In each row r, the horizontal bugs in row r occupy at most 2 squares. The remaining squares in row r (at least 8) can be occupied by vertical bugs. But vertical bugs in row r at time t are those whose unfolded row maps to r.

The number of vertical bugs in row r at time t: these are vertical bugs in various columns c whose unfolded row v satisfies g(v+t) = r. For each column c, at most 2 vertical bugs (one even, one odd unfolded row). But only those whose g(v+t) = r are in row r at time t.

For a given column c, the vertical bugs have unfolded rows v_even and v_odd (at most one each). At time t, the bug with unfolded row v is at row g(v+t). So it's in row r iff v+t ≡ ±r (mod 18).

For the even bug: v_even + t ≡ ±r (mod 18). For the odd bug: v_odd + t ≡ ±r (mod 18).

So at time t, in row r, from column c, we get at most 2 vertical bugs (if both v_even+t and v_odd+t map to r), but typically 0 or 1.

This is hard to bound in general. Let me try a different approach.

Let me think about the problem as follows. We have 10 rows and 10 columns. We place horizontal bugs (at most 2 per row) and vertical bugs (at most 2 per column). The cross-constraints determine which combinations are feasible.

Let me try to find the maximum by considering the parity structure.

Let me split the bugs into 4 types:
- HE: horizontal, even cycle position. At most 1 per row → at most 10.
- HO: horizontal, odd cycle position. At most 1 per row → at most 10.
- VE: vertical, even cycle position. At most 1 per column → at most 10.
- VO: vertical, odd cycle position. At most 1 per column → at most 10.

Cross-constraints (collision conditions):
- HE(r, p) & VE(c, q): q-p even, collision iff r+c even and q-p ≡ ±(r-c) or ±(r+c) (mod 18).
- HE(r, p) & VO(c, q): q-p odd, collision iff r+c odd and q-p ≡ ±(r-c) or ±(r+c) (mod 18).
- HO(r, p) & VE(c, q): q-p odd, collision iff r+c odd and q-p ≡ ±(r-c) or ±(r+c) (mod 18).
- HO(r, p) & VO(c, q): q-p even, collision iff r+c even and q-p ≡ ±(r-c) or ±(r+c) (mod 18).

So HE conflicts with VE only at "black" squares (r+c even), and HE conflicts with VO only at "white" squares (r+c odd). Similarly HO conflicts with VE at white squares, HO conflicts with VO at black squares.

Now, the board has 50 black squares and 50 white squares. In each row, 5 black and 5 white squares. In each column, 5 black and 5 white squares.

Let me think about a specific strategy. Suppose we use only HE and VO bugs. Then:
- HE bugs: at most 1 per row, 10 total.
- VO bugs: at most 1 per column, 10 total.
- Cross-constraint: HE(r, p) and VO(c, q) collide iff r+c odd and q-p ≡ ±(r-c) or ±(r+c) (mod 18).

Similarly, we could use HE and VE, or HO and VO, or HO and VE, or all four types.

Let me first try to maximize with just two types: HE and VO (or equivalently HO and VE by symmetry).

With HE and VO:
- 10 HE bugs (one per row) + 10 VO bugs (one per column) = 20.
- But cross-constraints may reduce this.

For HE(r, p_r) and VO(c, q_c): collision iff r+c odd and q_c - p_r ≡ ±(r-c) or ±(r+c) (mod 18).

We need to choose p_r (even, 0-16) for each row r, and q_c (odd, 1-17) for each column c, such that no collision occurs.

For each pair (r, c) with r+c odd, we need q_c - p_r ∉ {±(r-c), ±(r+c)} (mod 18).

There are 50 such pairs (r+c odd). For each, 4 forbidden values of q_c - p_r (out of 18 possible, but q_c - p_r is always odd, so 9 possible odd values, and at most 4 forbidden).

Hmm, this seems like it might be feasible. Let me try a specific construction.

Let me try p_r = 2r (even) for r = 0, ..., 8, and p_9 = 0 or something. Wait, 2r for r=0,...,8 gives 0,2,4,...,16, and for r=9, 2*9=18≡0. So p_r = 2r mod 18.

And q_c = 2c+1 (odd) for c = 0, ..., 8, and q_9 = 2*9+1 = 19 ≡ 1. So q_c = 2c+1 mod 18.

Then q_c - p_r = (2c+1) - 2r = 2(c-r) + 1 (mod 18).

For r+c odd (i.e., r and c have different parities), the forbidden values are ±(r-c) and ±(r+c) mod 18.

Let me check a specific pair. r=0, c=1 (r+c=1, odd). q_1 - p_0 = 2(1-0)+1 = 3. Forbidden: ±(0-1) = ±1 = {1, 17}, ±(0+1) = ±1 = {1, 17}. So forbidden = {1, 17}. 3 ∉ {1, 17}. ✓

r=0, c=3 (r+c=3, odd). q_3 - p_0 = 2(3)+1 = 7. Forbidden: ±(0-3) = {3, 15}, ±(0+3) = {3, 15}. So forbidden = {3, 15}. 7 ∉ {3, 15}. ✓

r=0, c=5. q_5 - p_0 = 11. Forbidden: ±5 = {5, 13}. 11 ∉ {5, 13}. ✓

r=0, c=7. q_7 - p_0 = 15. Forbidden: ±7 = {7, 11}. 15 ∉ {7, 11}. ✓

r=0, c=9. q_9 - p_0 = 2(9)+1 = 19 ≡ 1. Forbidden: ±9 = {9, 9}. So forbidden = {9}. 1 ∉ {9}. ✓

r=1, c=0 (r+c=1, odd). q_0 - p_1 = 1 - 2 = -1 ≡ 17. Forbidden: ±(1-0) = {1, 17}, ±(1+0) = {1, 17}. So forbidden = {1, 17}. 17 ∈ {1, 17}. ✗ Collision!

So this construction doesn't work for (r=1, c=0). Let me try a different construction.

Hmm, let me think about this more carefully. The condition q_c - p_r ≡ ±(r-c) or ±(r+c) (mod 18) can be rewritten. Note that:
- r-c and r+c differ by 2c.
- -(r-c) = c-r and -(r+c) = -r-c.

So the forbidden set is {r-c, c-r, r+c, -r-c} mod 18 = {r-c, c-r, r+c, -(r+c)} mod 18.

Note that (r-c) + (r+c) = 2r, and (r-c) - (r+c) = -2c. Also (c-r) + (r+c) = 2c, and (c-r) + (-(r+c)) = -2r.

Let me try p_r = 0 for all r (all HE bugs at cycle position 0). Then q_c - p_r = q_c. The forbidden values for pair (r, c) with r+c odd are {r-c, c-r, r+c, -(r+c)} mod 18. We need q_c ∉ this set for all r with r+c odd (i.e., r ≠ c mod 2).

For a given c, the forbidden values over all r with r ≠ c mod 2 are:
{r-c, c-r, r+c, -(r+c)} for all r with r ≠ c mod 2, r ∈ {0,...,9}.

Let me compute for c=0: r ∈ {1,3,5,7,9} (odd r).
- r=1: {1, -1≡17, 1, -1≡17} = {1, 17}
- r=3: {3, 15, 3, 15} = {3, 15}
- r=5: {5, 13, 5, 13} = {5, 13}
- r=7: {7, 11, 7, 11} = {7, 11}
- r=9: {9, 9, 9, 9} = {9}

Forbidden for c=0: {1, 3, 5, 7, 9, 11, 13, 15, 17} = all odd numbers! So q_0 must be odd (which it is, since VO) and not in this set. But all odd numbers are forbidden. So no valid q_0 exists!

So p_r = 0 for all r doesn't work. The HE bugs need different cycle positions.

Let me think about this differently. The forbidden set for (r, c) is {±(r-c), ±(r+c)} mod 18. Let me think about what these values are.

For r+c odd, both r-c and r+c are odd. So the forbidden values are all odd. And q_c - p_r is odd (since q_c is odd, p_r is even). So we need q_c - p_r to be an odd number not in the forbidden set.

The odd numbers mod 18 are: 1, 3, 5, 7, 9, 11, 13, 15, 17 (9 values). The forbidden set has at most 4 values. So there are at least 5 allowed values for each pair. But we need to satisfy all pairs simultaneously.

For a given c, the constraint is: for all r with r+c odd, q_c - p_r ∉ {±(r-c), ±(r+c)} mod 18.

This is a constraint on q_c given the p_r values. We need to choose p_r and q_c to satisfy all constraints.

This is a complex combinatorial problem. Let me try to think about it from a higher level.

Actually, let me reconsider the problem. Maybe the answer is 50, or 20, or something else. Let me think about upper bounds more carefully.

Upper bound via counting:

Consider the 18 time steps. At each time step t, the bugs occupy distinct squares. 

For each row r, at time t, the number of bugs in row r is at most 10. These bugs are either horizontal (in row r) or vertical (passing through row r at time t).

The number of horizontal bugs in row r is h_r (at most 2). The number of vertical bugs in row r at time t is the number of vertical bugs whose unfolded row at time t maps to r.

A vertical bug in column c with unfolded row v is at row g(v+t) at time t. It's in row r iff v+t ≡ ±r (mod 18). For a given t and r, the unfolded rows that map to r are: r-t and 18-r-t (mod 18) (or just one if r=0 or r=9).

So at time t, in row r, the vertical bugs are those in columns c where the vertical bug's unfolded row v satisfies v ≡ r-t or v ≡ -(r+t) (mod 18). For each such v, the vertical bugs with that unfolded row are in some columns.

This is getting very involved. Let me try to think about the problem from the perspective of the answer.

Let me consider the possibility that the answer is 50.

Actually, let me think about a cleaner upper bound. 

Consider the "unfolded" representation. Each bug has an unfolded coordinate (u for horizontal, v for vertical) in Z_18, and a fixed coordinate (row r for horizontal, column c for vertical).

At time t, a horizontal bug (r, u) is at position (r, g(u+t)). A vertical bug (v, c) is at position (g(v+t), c).

Now, consider the "sum" s = u + r for a horizontal bug, or s = v + c for a vertical bug. And the "difference" d = u - r for horizontal, d = v - c for vertical.

Hmm, I'm not sure this helps directly. Let me think about invariants.

For a horizontal bug (r, u): at time t, position is (r, g(u+t)). The "unfolded position" is (r, u+t). As t varies, the unfolded column advances.

For a vertical bug (v, c): at time t, position is (g(v+t), c). The "unfolded position" is (v+t, c).

Collision at time t: (r, g(u+t)) = (g(v+t), c), i.e., r = g(v+t) and g(u+t) = c. In unfolded terms: v+t ≡ ±r and u+t ≡ ±c (mod 18).

Let me think about the quantity u + v (mod 18) for a pair (H bug (r,u), V bug (v,c)). Collision requires v+t ≡ ±r and u+t ≡ ±c. Adding: u+v+2t ≡ ±r ± c (mod 18). The four cases give u+v+2t ≡ r+c, r-c, -r+c, -r-c (mod 18), i.e., u+v+2t ≡ ±(r+c) or ±(r-c) (mod 18).

Subtracting: v-u ≡ ±r ∓ c (mod 18), which is the condition we had before.

From the adding version: u+v+2t ≡ ±(r±c) (mod 18). For this to have a solution in t, we need ±(r±c) - (u+v) to be even, i.e., u+v ≡ r±c (mod 2), i.e., u+v ≡ r+c (mod 2) (since r-c ≡ r+c mod 2). This is the parity condition again.

OK I think I need to try a more computational approach, even though I can't use tools. Let me try to carefully construct a solution and find the maximum.

Let me think about the problem differently. Let me consider the "type" of each square (r, c) at time t. 

Actually, let me think about a key structural observation. 

Consider the 18×18 unfolded torus. Each horizontal bug (r, u) corresponds to a line on the torus: at time t, unfolded position (r, u+t) - but r is in {0,...,9}, not Z_18. So it's not a full torus.

Hmm, let me think about this differently. Let me consider the "doubled" board. Instead of a 10×10 board, consider an 18×18 board where the bouncing is unfolded. Each square (r, c) on the 10×10 board corresponds to squares (r, c) and (r, 18-c) on the 18×18 board (for c ≠ 0, 9), and just (r, c) for c = 0, 9. Similarly for rows.

Actually, the standard unfolding for a 1D bouncing motion on {0,...,9} gives a cycle of length 18 in Z_18. The mapping is g: Z_18 → {0,...,9} where g(k) = k if k ≤ 9, g(k) = 18-k if k ≥ 10.

For the 2D board, a horizontal bug unfolds to a point moving on {0,...,9} × Z_18 (row stays, column unfolds). A vertical bug unfolds to a point moving on Z_18 × {0,...,9} (row unfolds, column stays).

Two bugs collide on the original board iff their unfolded positions map to the same original position at the same time.

This is a complex constraint. Let me try to think about the maximum by considering specific constructions.

Let me try to construct a solution with 50 bugs.

Idea: Place 5 horizontal bugs and 5 vertical bugs, or some other split. Actually, let me think about what the maximum could be.

Let me reconsider. With 4 types (HE, HO, VE, VO), each with at most 10 bugs, the naive upper bound is 40. But cross-constraints reduce this. Can we achieve 40? Or is the maximum lower?

Let me think about whether 40 is achievable. We'd need 10 HE + 10 HO + 10 VE + 10 VO = 40 bugs, with all cross-constraints satisfied.

The cross-constraints are:
- HE(r, p) & VE(c, q): r+c even, q-p ≡ ±(r-c) or ±(r+c) (mod 18) → collision.
- HE(r, p) & VO(c, q): r+c odd, q-p ≡ ±(r-c) or ±(r+c) (mod 18) → collision.
- HO(r, p) & VE(c, q): r+c odd, q-p ≡ ±(r-c) or ±(r+c) (mod 18) → collision.
- HO(r, p) & VO(c, q): r+c even, q-p ≡ ±(r-c) or ±(r+c) (mod 18) → collision.

For 40 bugs, we need one HE bug per row, one HO bug per row, one VE bug per column, one VO bug per column. That's a lot of cross-constraints (10*10*4 = 400 pairs to check, roughly).

This seems very hard to achieve. Let me think about whether there's a fundamental obstruction.

Consider the HE and VE bugs. HE has one bug per row, VE has one bug per column. For each pair (r, c) with r+c even (50 pairs), we need q_c - p_r ∉ {±(r-c), ±(r+c)} (mod 18). Since q_c and p_r are both even, q_c - p_r is even. The forbidden values ±(r-c) and ±(r+c) are also even (since r+c even implies r-c even). So we need q_c - p_r to be an even value not in the forbidden set.

The even values mod 18 are: 0, 2, 4, 6, 8, 10, 12, 14, 16 (9 values). The forbidden set has at most 4 values. So at least 5 allowed values per pair.

But with 50 pairs, this is a lot of constraints. Let me think about whether they can all be satisfied.

For a fixed c, the constraints from all r with r+c even (5 values of r) give at most 5*4 = 20 forbidden values for q_c - p_r. But q_c - p_r depends on both q_c and p_r, so it's not just about q_c.

This is a constraint satisfaction problem that's hard to solve by hand. Let me think about whether there's a cleaner upper bound.

Let me try a different approach to the upper bound.

Consider the quantity Q = (unfolded_column + row) mod 2 for horizontal bugs, and Q = (unfolded_row + column) mod 2 for vertical bugs.

For a horizontal bug (r, u): Q_H = (u + r) mod 2.
For a vertical bug (v, c): Q_V = (v + c) mod 2.

Now, when do a horizontal bug (r, u) and vertical bug (v, c) collide? We need v+t ≡ ±r and u+t ≡ ±c (mod 18). 

From v+t ≡ r: v+t ≡ r → v-r ≡ -t. And u+t ≡ c → u-c ≡ -t. So v-r ≡ u-c → v-u ≡ r-c.
From v+t ≡ r, u+t ≡ -c: v-r ≡ u+c → v-u ≡ r+c.
Etc.

The parity condition: (u+v) mod 2 = (r+c) mod 2, i.e., (u-r) mod 2 = (c-v) mod 2, i.e., (u+r) mod 2 = (v+c) mod 2 (since u-r ≡ u+r mod 2 and c-v ≡ c+v mod 2). So Q_H = Q_V!

So a horizontal bug and a vertical bug can only collide if Q_H = Q_V. If Q_H ≠ Q_V, they never collide.

This is a useful observation! It means we can split the bugs into two groups based on Q, and bugs in different groups never collide with each other (cross-type).

But within the same group, horizontal bugs still conflict with each other (same row, same parity), and vertical bugs conflict with each other (same column, same parity).

Wait, let me also check: do two horizontal bugs with different Q values conflict? Two horizontal bugs in the same row r with cycle positions u1, u2: they conflict iff u1 ≡ u2 (mod 2). Q1 = (u1+r) mod 2, Q2 = (u2+r) mod 2. If u1 ≡ u2 (mod 2), then Q1 = Q2. If u1 ≢ u2 (mod 2), then Q1 ≠ Q2 and they don't conflict. So two horizontal bugs in the same row conflict iff they have the same Q. This means in each row, at most one bug per Q value, so at most 2 (one Q=0, one Q=1). Consistent with before.

Similarly for vertical bugs in the same column.

Now, the key insight: if Q_H = Q_V, a horizontal and vertical bug MIGHT collide (need more conditions). If Q_H ≠ Q_V, they NEVER collide.

So let's split into two groups:
- Group 0: bugs with Q = 0.
- Group 1: bugs with Q = 1.

Bugs in different groups never collide (cross-type). Within each group, horizontal bugs in the same row conflict (at most 1 per row per group), vertical bugs in the same column conflict (at most 1 per column per group), and horizontal-vertical pairs might conflict.

So each group has at most 10 horizontal bugs (one per row) + 10 vertical bugs (one per column) = 20 bugs. Two groups → at most 40 bugs. But cross-constraints within each group may reduce this.

Wait, but I already had the bound of 40 from the 4-type analysis. The Q grouping gives the same bound. Let me think about whether 40 is achievable.

Within group 0: at most 10 H bugs + 10 V bugs = 20. Within group 1: at most 10 H bugs + 10 V bugs = 20. Total: 40.

But within each group, the H-V cross-constraints must be satisfied. Let me think about whether we can achieve 20 per group.

In group 0, we have one H bug per row and one V bug per column. The H bug in row r has Q = 0, so (u_r + r) mod 2 = 0, i.e., u_r ≡ r (mod 2). The V bug in column c has Q = 0, so (v_c + c) mod 2 = 0, i.e., v_c ≡ c (mod 2).

Collision condition: v_c - u_r ≡ ±(r-c) or ±(r+c) (mod 18), AND Q_H = Q_V = 0 (which is already satisfied).

So we need: for all (r, c), v_c - u_r ∉ {±(r-c), ±(r+c)} (mod 18).

With u_r ≡ r (mod 2) and v_c ≡ c (mod 2), v_c - u_r ≡ c - r (mod 2). And ±(r-c) ≡ r-c ≡ r+c (mod 2). So v_c - u_r ≡ ±(r-c) (mod 2) always. So the parity condition is always satisfied, meaning collisions are always possible (the parity doesn't rule anything out).

So within a group, we need to avoid the specific forbidden values. This is the hard part.

Let me try to think about this as an assignment problem. We need to choose u_r (even if r even, odd if r odd, for group 0) and v_c (even if c even, odd if c odd, for group 0) such that v_c - u_r ∉ {r-c, c-r, r+c, -(r+c)} (mod 18) for all r, c.

Let me think about the number of choices. For group 0:
- u_r: even if r even (r ∈ {0,2,4,6,8}, u_r ∈ {0,2,4,6,8,10,12,14,16}, 9 choices), odd if r odd (r ∈ {1,3,5,7,9}, u_r ∈ {1,3,5,7,9,11,13,15,17}, 9 choices). So 9 choices per row.
- v_c: similarly 9 choices per column.

We need to satisfy 100 constraints (one per (r,c) pair). Each constraint forbids 4 values of v_c - u_r (out of 18, but with the right parity, out of 9).

This is a complex CSP. Let me try to find a pattern.

Let me try u_r = 2r (mod 18) and v_c = 2c (mod 18) for group 0. Wait, but u_r must have the same parity as r. 2r is always even, so this only works for even r. For odd r, u_r must be odd. Let me try u_r = 2r + (r mod 2) = 2r if r even, 2r+1 if r odd. Hmm, that's just u_r = 2r + (r%2). For r=0: 0, r=1: 3, r=2: 4, r=3: 7, r=4: 8, r=5: 11, r=6: 12, r=7: 15, r=8: 16, r=9: 19≡1.

Similarly v_c = 2c + (c%2). Same values.

Then v_c - u_r = 2(c-r) + (c%2 - r%2). If r and c have the same parity, v_c - u_r = 2(c-r). If different, v_c - u_r = 2(c-r) ± 1.

The forbidden values are {r-c, c-r, r+c, -(r+c)} mod 18.

Let me check r=0, c=0: v_0 - u_0 = 0. Forbidden: {0, 0, 0, 0} = {0}. 0 ∈ {0}. Collision! 

So this doesn't work. Let me try a different approach.

Let me try u_r = 0 for all r (in group 0, u_r must have parity of r, so this only works for even r). Hmm, this doesn't work for odd r.

OK let me think about this more carefully. Maybe I should consider a different splitting.

Actually, let me reconsider the Q value. For group 0, u_r ≡ r (mod 2) and v_c ≡ c (mod 2). The forbidden values for (r,c) are {r-c, c-r, r+c, -(r+c)} mod 18. Note that:
- r-c and c-r are negatives of each other.
- r+c and -(r+c) are negatives.
- r-c and r+c differ by 2c.
- c-r and -(r+c) differ by 2c + 2r = 2(r+c)... no, c-r - (-(r+c)) = c-r+r+c = 2c.

So the four forbidden values are {±(r-c), ±(r+c)}. In Z_18, these are {r-c, 18-(r-c), r+c, 18-(r+c)} (taking representatives in 0-17).

For the pair (r, c) = (0, 0): forbidden = {0, 0, 0, 0} = {0}. So v_0 - u_0 ≠ 0 (mod 18).
For (r, c) = (0, 1): forbidden = {-1, 1, 1, -1} = {1, 17}. So v_1 - u_0 ∉ {1, 17}.
For (r, c) = (1, 0): forbidden = {1, -1, 1, -1} = {1, 17}. So v_0 - u_1 ∉ {1, 17}.
For (r, c) = (1, 1): forbidden = {0, 0, 2, -2} = {0, 2, 16}. So v_1 - u_1 ∉ {0, 2, 16}.

Hmm, let me try a different approach. Let me try to see if 20 per group is achievable by trying small examples.

Actually, let me step back and think about the problem from a higher level. Maybe the answer is not 40 but something else.

Let me reconsider. The problem is on a 10×10 board. Let me think about what's special about 10.

The period is 2(10-1) = 18. The number of even values in Z_18 is 9, and odd values is 9.

Hmm, let me think about the problem for a general n×n board and see if there's a pattern.

For a 2×2 board: period 2. Each row has 2 columns, unfolding to 2 positions. Two horizontal bugs in the same row: cycle positions 0 and 1 (different parity), so they don't collide. So 2 per row, 2 rows = 4 horizontal bugs. But the board only has 4 squares, and at time 0, we'd have 4 bugs on 4 squares. At time 1, each bug moves. A horizontal bug in row 0 at column 0 moving right goes to column 1. A horizontal bug in row 0 at column 1 moving left goes to column 0. So they swap. Similarly for row 1. So at time 1, all 4 squares are still occupied. At time 2, they're back to original. So 4 bugs work for a 2×2 board. Can we do better? No, 4 is the max (only 4 squares).

But wait, can we add vertical bugs too? If all 4 squares are occupied by horizontal bugs, there's no room for vertical bugs. So the max is 4 for a 2×2 board.

For a 3×3 board: period 4. Each row unfolds to 4 positions. Two horizontal bugs in the same row collide iff same parity. So at most 2 per row (one even, one odd), 3 rows = 6 horizontal bugs. Similarly 6 vertical bugs. Can we mix?

With 6 horizontal bugs (2 per row), at time 0, each row has 2 bugs in 2 of its 3 columns. So 6 squares occupied, 3 free. Can we add vertical bugs in those free squares?

A vertical bug in column c at time 0 is at some row. It needs to not collide with any horizontal bug at any time.

This is getting complicated. Let me try to think about the 10×10 case more directly.

Let me try a different approach to the upper bound.

Consider the "diagonal" structure. Define for each bug a value in Z_18:
- Horizontal bug (r, u): define α = u - r (mod 18) and β = u + r (mod 18).
- Vertical bug (v, c): define α = v - c (mod 18) and β = v + c (mod 18).

Wait, let me think about what the collision condition looks like in terms of these.

H bug (r, u) and V bug (v, c) collide iff v - u ≡ ±(r-c) or ±(r+c) (mod 18).

v - u ≡ r - c → (v-c) ≡ (u-r) → α_V = α_H.
v - u ≡ -(r-c) = c-r → (v+c) ≡ (u+r) → β_V = β_H. Wait: v - u = c - r → v + r = u + c → v - c = u - r... no. v - u = c - r → v + r = u + c. Hmm, let me redo.

v - u ≡ r - c (mod 18): rearranging, v + c ≡ u + r (mod 18), i.e., β_V ≡ β_H.
v - u ≡ c - r (mod 18): rearranging, v - c ≡ u - r (mod 18), i.e., α_V ≡ α_H.
v - u ≡ r + c (mod 18): rearranging, v - c ≡ u + r (mod 18), i.e., α_V ≡ β_H.
v - u ≡ -(r + c) (mod 18): rearranging, v + c ≡ u - r (mod 18), i.e., β_V ≡ α_H.

So H bug (r, u) and V bug (v, c) collide iff:
- α_V = α_H, or
- β_V = β_H, or
- α_V = β_H, or
- β_V = α_H.

Where α_H = u - r, β_H = u + r, α_V = v - c, β_V = v + c (all mod 18).

So collision iff {α_V, β_V} ∩ {α_H, β_H} ≠ ∅ (mod 18).

This is a much cleaner condition! A horizontal bug has two "keys" (α_H, β_H) and a vertical bug has two "keys" (α_V, β_V). They collide iff they share a common key.

Now, for a horizontal bug (r, u): α_H = u - r, β_H = u + r. Note that α_H + β_H = 2u and β_H - α_H = 2r. So given α_H and β_H, we can recover u = (α_H + β_H)/2 and r = (β_H - α_H)/2 (mod 9, since we're dividing by 2 mod 18... hmm, division by 2 mod 18 is not well-defined since 2 is not invertible mod 18).

Actually, α_H and β_H have the same parity (since α_H + β_H = 2u is even). So α_H ≡ β_H (mod 2). Similarly, α_V ≡ β_V (mod 2).

Also, r = (β_H - α_H)/2. For this to give a valid r ∈ {0,...,9}, we need β_H - α_H to be even (which it is) and (β_H - α_H)/2 mod 9 ∈ {0,...,9}. Wait, (β_H - α_H)/2 mod 9 gives a value in {0,...,8}, but r can be 0-9. Hmm, since we're working mod 18, β_H - α_H can be any even number mod 18, and dividing by 2 gives a value mod 9, which is 0-8. But r ∈ {0,...,9}. So r = 9 is not achievable? 

Wait, let me reconsider. r ∈ {0,...,9} and u ∈ {0,...,17}. α_H = u - r mod 18, β_H = u + r mod 18. Given r and u, we get specific α_H, β_H. Given α_H, β_H (with same parity), we get u = (α_H + β_H)/2 mod 9 (but u is mod 18, so u = (α_H + β_H)/2 or (α_H + β_H)/2 + 9). And r = (β_H - α_H)/2 mod 9 (but r is 0-9, so r = (β_H - α_H)/2 mod 9, giving 0-8, or r = 9 if...).

Hmm, this is getting messy because of the mod 18 vs mod 9 issue. Let me think about it differently.

The key observation is: H bug (r, u) and V bug (v, c) collide iff {α_H, β_H} ∩ {α_V, β_V} ≠ ∅ (mod 18), where α_H = u-r, β_H = u+r, α_V = v-c, β_V = v+c.

Now, for a horizontal bug, α_H and β_H are two values in Z_18 with the same parity. For a vertical bug, similarly.

The condition is that the horizontal bug's key set {α_H, β_H} and the vertical bug's key set {α_V, β_V} are disjoint.

Now, let's think about the constraints within horizontal bugs. Two horizontal bugs in the same row r with cycle positions u1, u2: they collide iff u1 ≡ u2 (mod 2). In terms of keys: α1 = u1-r, β1 = u1+r, α2 = u2-r, β2 = u2+r. If u1 ≡ u2 (mod 2), then α1 ≡ α2 (mod 2) and β1 ≡ β2 (mod 2). But the collision condition is about same parity, not same key.

Hmm, the key formulation helps for H-V collisions but not for H-H or V-V collisions. Let me focus on the H-V collisions using the key formulation.

So the problem reduces to: choose horizontal bugs (each with a key pair {α, β} of same parity) and vertical bugs (each with a key pair {α, β} of same parity) such that:
1. No two horizontal bugs in the same row have the same parity cycle position.
2. No two vertical bugs in the same column have the same parity cycle position.
3. No horizontal bug's key pair intersects any vertical bug's key pair.

Condition 3 means: the set of all keys used by horizontal bugs and the set of all keys used by vertical bugs are disjoint.

Let S_H = set of all keys used by horizontal bugs = ∪ over all H bugs of {α_H, β_H}.
Let S_V = set of all keys used by vertical bugs = ∪ over all V bugs of {α_V, β_V}.
We need S_H ∩ S_V = ∅.

Now, the keys are in Z_18. There are 18 keys total. S_H and S_V partition a subset of Z_18.

Each horizontal bug uses 2 keys. Each vertical bug uses 2 keys. If we have h horizontal bugs and v vertical bugs, then |S_H| ≤ 2h and |S_V| ≤ 2v (could be less if keys are shared among bugs of the same type).

We need |S_H| + |S_V| ≤ 18 (since they're disjoint subsets of Z_18). So 2h + 2v ≤ 18 is not quite right because keys can be shared within the same type. But it gives h + v ≤ 9 if all keys are distinct, which is too restrictive.

Wait, keys CAN be shared within the same type (H-H or V-V). Two horizontal bugs can share a key as long as they're in different rows or have different parity cycle positions. So |S_H| can be much less than 2h.

Let me think about this more carefully. How many horizontal bugs can share the same key?

A key k is used by a horizontal bug (r, u) if α_H = k (i.e., u - r = k) or β_H = k (i.e., u + r = k). 

For α_H = k: u = r + k (mod 18). For this to be a valid cycle position, u ∈ {0,...,17}, which it is (any r + k mod 18 is in {0,...,17}). And r ∈ {0,...,9}. So there are 10 horizontal bugs with α_H = k (one for each row r, with u = r + k mod 18). But we can only have at most 2 per row (one even, one odd). The parity of u = r + k is (r + k) mod 2. For a given k, in row r, u = r + k has parity (r+k) mod 2. So in each row, there's exactly one bug with α_H = k (the one with u = r+k). But we need to check if two such bugs (in different rows) conflict. They're in different rows, so they don't conflict (H-H collision only happens within the same row). So all 10 bugs with α_H = k can coexist!

Similarly for β_H = k: u = k - r (mod 18), and there are 10 such bugs (one per row), all in different rows, so they can coexist.

But can a bug with α_H = k and a bug with β_H = k coexist? They're both using key k. If they're in different rows, yes. If in the same row, they need different parity cycle positions. Bug 1: u1 = r + k, bug 2: u2 = k - r. u1 - u2 = 2r. If 2r is odd... but 2r is always even. So u1 ≡ u2 (mod 2), meaning they have the same parity and would conflict if in the same row. So in each row, we can have at most one of {α_H = k bug, β_H = k bug}.

So for a given key k, the maximum number of horizontal bugs using key k is 10 (all with α_H = k, one per row) or 10 (all with β_H = k), but not both in the same row. So we could have 10 bugs with α_H = k (one per row) and that's it, or we could mix: in some rows use α_H = k, in others use β_H = k, but not both in the same row. So still at most 10 per key.

But wait, a single bug uses TWO keys. So if we have 10 bugs all with α_H = k, they also each have a β_H key. Bug in row r: α_H = k, β_H = k + 2r (mod 18). So the β_H keys are k, k+2, k+4, ..., k+18 = k. So β_H takes values k, k+2, k+4, k+6, k+8, k+10, k+12, k+14, k+16, k (for r = 0, 1, ..., 9). So β_H = k + 2r mod 18, which for r = 0,...,9 gives k, k+2, k+4, k+6, k+8, k+10, k+12, k+14, k+16, k. So the β_H values are {k, k+2, k+4, k+6, k+8, k+10, k+12, k+14, k+16} = all values with the same parity as k. And k appears twice (r=0 and r=9).

So if all 10 horizontal bugs have α_H = k, then S_H includes k (from α_H) and all same-parity values (from β_H). So S_H = {all values with same parity as k} = 9 values. And these are all the same-parity values in Z_18.

Then S_V must be disjoint from S_H, so S_V ⊆ {values with opposite parity to k} = 9 values. Each vertical bug uses 2 keys, both of the same parity (opposite to k). So vertical bugs' keys are all from these 9 values.

How many vertical bugs can we have using only these 9 keys? Each vertical bug uses 2 keys. The keys are α_V = v - c and β_V = v + c, both with parity opposite to k. 

By the same argument as for horizontal bugs, we can have up to 10 vertical bugs (one per column) using a single key, say α_V = k' (where k' has opposite parity to k). These 10 bugs would use keys {k'} (from α_V) and {k' + 2c : c = 0,...,9} = {all values with same parity as k'} (from β_V). So S_V = {all values with parity opposite to k} = 9 values. And S_H ∩ S_V = ∅. ✓

So we can have 10 horizontal bugs + 10 vertical bugs = 20 bugs, with S_H = {even values} and S_V = {odd values} (or vice versa).

But can we do better? Can we have more than 10 horizontal bugs?

With 10 horizontal bugs (one per row, all with α_H = k), we've used up all 9 keys of one parity. Can we add more horizontal bugs? An additional horizontal bug in row r would need a cycle position of different parity (since we already have one per row). Its keys would be of the opposite parity. But the opposite parity keys are all in S_V. So this additional H bug would share a key with some V bug, causing a collision. Unless we remove some V bugs.

So there's a tradeoff: more H bugs of the opposite parity → fewer V bugs.

Let me think about this more carefully. Suppose we have:
- h1 horizontal bugs with even-parity keys (using some even keys).
- h2 horizontal bugs with odd-parity keys (using some odd keys).
- v1 vertical bugs with even-parity keys.
- v2 vertical bugs with odd-parity keys.

Constraints:
- S_H_even ∩ S_V_even = ∅ (even keys used by H and V must be disjoint).
- S_H_odd ∩ S_V_odd = ∅ (odd keys used by H and V must be disjoint).
- (H-H and V-V constraints as before.)

S_H_even ∪ S_V_even ⊆ {even keys} (9 values).
S_H_odd ∪ S_V_odd ⊆ {odd keys} (9 values).

Each H bug with even keys uses 2 even keys. Each V bug with even keys uses 2 even keys. The total even keys used is |S_H_even| + |S_V_even| ≤ 9.

Now, how many H bugs can use a given set of even keys? As argued, up to 10 H bugs can share a single key (one per row). But each H bug uses 2 keys. If all 10 H bugs share the same α key, they use 1 + 9 = 10... wait, no. They use 1 α key and up to 9 β keys (as computed). So |S_H_even| = 9 (all even keys) if we have 10 bugs all with the same α.

But if we have fewer H bugs, we might use fewer keys, leaving more for V bugs.

Let me think about the tradeoff. Suppose we use e_H even keys for H bugs and e_V even keys for V bugs, with e_H + e_V ≤ 9. Similarly, o_H + o_V ≤ 9 for odd keys.

The number of H bugs with even keys is at most... well, it depends on how the keys are used. Let me think about the maximum number of H bugs using a given number of even keys.

If we have e_H even keys available for H bugs, how many H bugs (with even cycle positions) can we place?

Each H bug with even cycle position u in row r has α = u - r and β = u + r, both even. The bug uses 2 even keys. Multiple bugs can share keys.

In a given row r, we can have at most 1 H bug with even cycle position. So at most 10 H bugs with even cycle positions (one per row).

Each such bug uses 2 even keys. The keys are α = u - r and β = u + r. For bugs in different rows, the keys can overlap.

The question is: what is the minimum number of even keys needed to support 10 H bugs (one per row, each with even cycle position)?

For row r, the bug has u_r (even), α_r = u_r - r, β_r = u_r + r. Note α_r + β_r = 2u_r (even ✓) and β_r - α_r = 2r.

We want to minimize |{α_r, β_r : r = 0,...,9}|.

β_r - α_r = 2r, so α_r and β_r are determined by each other given r. Specifically, β_r = α_r + 2r. So the keys are {α_r, α_r + 2r} for each r.

To minimize the total number of distinct keys, we want the α_r values to be chosen so that the sets {α_r, α_r + 2r} overlap as much as possible.

If we set α_r = k for all r (constant), then the keys are {k, k + 2r : r = 0,...,9} = {k, k+2, k+4, ..., k+16, k+18=k} = {k, k+2, k+4, k+6, k+8, k+10, k+12, k+14, k+16}. That's 9 distinct even values (all even values if k is even). So |S_H_even| = 9.

Can we do better? What if we don't use all 10 rows? If we use only 5 rows, we might use fewer keys. For example, rows 0, 2, 4, 6, 8 (even rows). Set α_r = k for all. Keys: {k, k+2r} for r = 0, 2, 4, 6, 8 = {k, k, k+4, k+8, k+12, k+16} = {k, k+4, k+8, k+12, k+16}. That's 5 keys. So 5 H bugs using 5 even keys.

Or rows 0, 1, 2, 3, 4 with α_r = k: keys = {k, k, k+2, k+2, k+4, k+4, k+6, k+6, k+8, k+8} = {k, k+2, k+4, k+6, k+8}. 5 keys for 5 bugs.

In general, it seems like n H bugs (one per row, with even cycle positions) use at least n even keys (if we're clever about it) and at most 9.

Wait, can we do better than n keys for n bugs? Each bug uses 2 keys, but keys can be shared. Two bugs in rows r1 and r2 share a key if {α_{r1}, β_{r1}} ∩ {α_{r2}, β_{r2}} ≠ ∅. This happens if α_{r1} = α_{r2} or α_{r1} = β_{r2} or β_{r1} = α_{r2} or β_{r1} = β_{r2}.

α_{r1} = α_{r2}: u_{r1} - r1 = u_{r2} - r2, so u_{r1} - u_{r2} = r1 - r2.
β_{r1} = β_{r2}: u_{r1} + r1 = u_{r2} + r2, so u_{r1} - u_{r2} = r2 - r1.
α_{r1} = β_{r2}: u_{r1} - r1 = u_{r2} + r2, so u_{r1} - u_{r2} = r1 + r2.
β_{r1} = α_{r2}: u_{r1} + r1 = u_{r2} - r2, so u_{r1} - u_{r2} = -(r1 + r2).

So bugs in rows r1 and r2 share a key iff u_{r1} - u_{r2} ≡ ±(r1 - r2) or ±(r1 + r2) (mod 18). But this is exactly the collision condition for H-V bugs! Wait, no, this is the condition for two H bugs to share a key, which is different from colliding.

Actually, sharing a key is fine for two H bugs (they're in different rows, so they don't collide). The key sharing just means the key set is smaller.

So to minimize the key set, we want maximum key sharing. The condition for bugs in rows r1, r2 to share a key is u_{r1} - u_{r2} ≡ ±(r1-r2) or ±(r1+r2) (mod 18).

If we set u_r = 2r (even for all r), then u_{r1} - u_{r2} = 2(r1 - r2). The sharing condition: 2(r1-r2) ≡ ±(r1-r2) or ±(r1+r2) (mod 18).
- 2(r1-r2) ≡ (r1-r2): r1-r2 ≡ 0 (mod 18), only if r1=r2.
- 2(r1-r2) ≡ -(r1-r2): 3(r1-r2) ≡ 0 (mod 18), i.e., r1-r2 ≡ 0 (mod 6).
- 2(r1-r2) ≡ (r1+r2): r1-3r2 ≡ 0 (mod 18).
- 2(r1-r2) ≡ -(r1+r2): 3r1-r2 ≡ 0 (mod 18).

So with u_r = 2r, bugs in rows r1 and r2 share a key iff r1-r2 ≡ 0 (mod 6) or r1-3r2 ≡ 0 (mod 18) or 3r1-r2 ≡ 0 (mod 18).

For r1-r2 ≡ 0 (mod 6): rows that differ by 6. So rows 0 and 6, 1 and 7, 2 and 8, 3 and 9 share a key. That's 4 pairs.

This is getting complicated. Let me try a different approach.

Let me think about the problem as an optimization. We want to maximize h + v where h is the number of horizontal bugs and v is the number of vertical bugs, subject to:
- At most 2 H bugs per row (one even, one odd cycle position).
- At most 2 V bugs per column (one even, one odd cycle position).
- S_H ∩ S_V = ∅ (key sets disjoint).

Let me think about the key budget. There are 18 keys (9 even, 9 odd). H bugs use some keys, V bugs use the rest.

For H bugs with even cycle positions: they use even keys. Let's say they use e_H even keys.
For H bugs with odd cycle positions: they use odd keys. Let's say they use o_H odd keys.
For V bugs with even cycle positions: they use even keys. Let's say they use e_V even keys.
For V bugs with odd cycle positions: they use odd keys. Let's say they use o_V odd keys.

Constraints: e_H + e_V ≤ 9, o_H + o_V ≤ 9.

Now, the number of H bugs with even cycle positions is at most 10 (one per row), and they use at least... how many even keys?

Let me think about the minimum number of even keys needed for k H bugs with even cycle positions.

If we place k H bugs (one per row, for k specific rows) with even cycle positions, the minimum number of even keys used is... let me think.

Each bug uses 2 keys. But keys can be shared. The minimum number of keys is at least 1 (if all bugs share both keys, but that's impossible since different rows give different β = α + 2r values).

Actually, if all bugs have the same α key, then the β keys are α + 2r for each row r used. If the rows are r_1, ..., r_k, the β keys are α + 2r_1, ..., α + 2r_k (mod 18). These are distinct iff the 2r_i are distinct mod 18, i.e., the r_i are distinct mod 9. Since r_i ∈ {0,...,9} and we have at most 10 rows, two rows can give the same β: r and r+9 (but r+9 > 9 for r ≥ 1, so only r=0 and r=9 give the same β = α + 0 and α + 18 = α). Wait, 2*0 = 0 and 2*9 = 18 ≡ 0. So rows 0 and 9 give the same β key. So if we use both rows 0 and 9, the β keys overlap.

So for k bugs with the same α key, the number of distinct keys is 1 + |{2r_i mod 18 : i = 1,...,k}|. The 2r_i mod 18 values are distinct unless two rows differ by 9
