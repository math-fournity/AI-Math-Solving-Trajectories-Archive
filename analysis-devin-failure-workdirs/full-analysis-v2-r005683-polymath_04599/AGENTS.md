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
  <problem_id>polymath_04599</problem_id>
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

On a $2023 \times 2023$ board, some squares contain a beetle, with at most one beetle per square. After one minute, each beetle moves one square to the left, right, up, or down. After each subsequent minute, each beetle moves one square further, but always makes a 90-degree turn. If a beetle moved left or right in one minute, it will move up or down in the next minute, and vice versa. What is the minimum number of beetles that must be on the board to ensure that at some point, two beetles will end up in the same square at the same time, regardless of where the beetles start and how they move (following the rules)?

## Standard Solution

The answer is $2022^{2}+1$.
First, let's show that $2022^{2}$ is indeed insufficient. For this, we divide a $2022 \times 2022$ sub-board into $2 \times 2$ boards. In each such board, we can place four beetles such that they walk in a small circle (square) clockwise.

Now, suppose we have more than $2022^{2}$ beetles. We want to prove that at some point, two will end up in the same square. To this end, we number the squares from $(1,1)$ to $(2023,2023)$ and color the board as follows: the squares in an odd row and odd column are colored $A$, an odd row and even column are colored $B$, an even row and even column are colored $C$, and an even row and odd column are colored $D$. Thus, half of the diagonals are colored with $A$ and $C$, and the other half with $B$ and $D$. Therefore, there are $1012^{2}$ squares $A$, there are $1011^{2}$ squares $C$, and there are $1011 \cdot 1012$ squares of both $B$ and $D$.

Then each beetle follows a cyclic path $A \rightarrow B \rightarrow C \rightarrow D \rightarrow A$ or $A \rightarrow D \rightarrow C \rightarrow B \rightarrow A$. We note that no more than $1011^{2}$ beetles can start in squares $C$, as there are only $1011^{2}$ of them. Since the number of beetles is greater than $2022^{2}$, there must be more than $1011^{2}$ beetles on squares $A$ or more than $2 \cdot 1011^{2}$ beetles on squares $B$ and $D$ together.

In the first case, after two minutes, there are more than $1011^{2}$ beetles in squares $C$, and we conclude that two beetles meet.

In the second case, after the first minute, there are more than $2 \cdot 1011^{2}$ beetles in the squares $A$ and $C$ together. Thus, two beetles meet in $C$ or we find more than $1011^{2}$ beetles on squares $A$. In that case, after the third minute, there are more than $1011^{2}$ beetles in squares $C$, and we conclude that two beetles meet anyway.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully.

We have a 2023×2023 board. Beetles move: first move one square in a direction (L/R/U/D), then each subsequent minute they move one square further but make a 90-degree turn. So if a beetle moved horizontally in minute 1, it moves vertically in minute 2, horizontally in minute 3, etc.

Wait, "moves one square further" - let me re-read. "After one minute, each beetle moves one square to the left, right, up, or down. After each subsequent minute, each beetle moves one square further, but always makes a 90-degree turn."

Hmm, "moves one square further" - does this mean it moves 1 square in minute 1, then 2 squares in minute 2, then 3 in minute 3? Or does "further" just mean "another square" (i.e., still 1 square)?

Let me re-read: "After one minute, each beetle moves one square to the left, right, up, or down. After each subsequent minute, each beetle moves one square further, but always makes a 90-degree turn."

I think "moves one square further" means moves one more square (i.e., 1 square each minute), but in a direction that's a 90-degree turn from the previous direction. So each minute the beetle moves exactly 1 square, alternating between horizontal and vertical.

Wait, but "one square further" could mean the distance increases. Let me think about this more carefully. Actually "moves one square further" most likely means "moves one additional square" - i.e., moves 1 square each minute. The key constraint is the 90-degree turn.

Actually, re-reading again: "each beetle moves one square further" - I think this means it moves 1 square each minute. The word "further" just means "more" as in "continues to move." The key is the 90-degree turn rule.

So the movement pattern: each beetle alternates between horizontal and vertical moves, 1 square each minute.

Let me set up coordinates. Let the board be {(x,y) : 1 ≤ x,y ≤ 2023}. A beetle starts at position (x₀, y₀). At minute 1, it moves 1 square in some direction. At minute 2, it moves 1 square in a perpendicular direction. And so on.

So the beetle's position at time t:
- If t is odd (relative to start of horizontal phase), the x-coordinate changes by ±1, y stays.
- Actually, itLet me think about this problem carefully.

We have a 2023×2023 board. Beetles move one square per minute. Each beetle alternates between horizontal moves (left/right) and vertical moves (up/down). After one minute, each beetle moves one square in some direction. After each subsequent minute, each beetle makes a 90-degree turn — so if it moved horizontally, next it moves vertically, and vice versa.

We need the minimum number of beetles to guarantee that at some point two beetles occupy the same square at the same time, regardless of starting positions and movement choices.

Let me think about the structure. Each beetle's path is determined by:
- Starting position (row, col)
- First move direction (horizontal or vertical)
- Sequence of choices: at each step, the beetle chooses left/right (if horizontal) or up/down (if vertical).

Actually, let me reconsider. The beetle's position over time: at time 0 it's at some square. At time 1, it moves one square in some direction (L, R, U, D). At time 2, it makes a 90-degree turn, so if it moved horizontally at time 1, it moves vertically at time 2, etc.

So the beetle alternates: horizontal, vertical, horizontal, vertical, ... OR vertical, horizontal, vertical, horizontal, ...

Let me think about parity and invariants.

Consider a beetle's position at time t. Let's track its row and column separately.

If the beetle starts with a horizontal move:
- At odd times (1, 3, 5, ...), it moves horizontally.
- At even times (2, 4, 6, ...), it moves vertically.

Wait, let me re-index. At minute 1, it moves. At minute 2, it moves again with a 90-degree turn. Etc.

So at minute k (k=1,2,3,...), the beetle moves one square. The direction alternates between horizontal and vertical.

If the first move is horizontal:
- Minutes 1, 3, 5, ...: horizontal moves (each ±1 in column)
- Minutes 2, 4, 6, ...: vertical moves (each ±1 in row)

So after t minutes:
- Column = col_0 + (sum of horizontal moves) = col_0 + (number of horizontal moves up to time t with signs)
- Row = row_0 + (sum of vertical moves)

The number of horizontal moves in the first t minutes: if first move is horizontal, then minutes 1,3,5,... are horizontal. That's ceil(t/2) horizontal moves and floor(t/2) vertical moves.

Each horizontal move changes column by ±1, each vertical move changes row by ±1.

Key observation: After t minutes, the column has changed by a sum of ceil(t/2) terms of ±1, and the row has changed by a sum of floor(t/2) terms of ±1 (or vice versa if first move is vertical).

Now, the parity. Column parity: col_0 + ceil(t/2) (mod 2) determines the parity of the column (since each ±1 changes parity). Actually, the parity of the column after t minutes is col_0 + ceil(t/2) mod 2 (if first move horizontal), because each move flips the parity.

Similarly, row parity after t minutes: row_0 + floor(t/2) mod 2.

Hmm, let me think about this differently. Let me think about what positions a beetle can reach at time t.

At time t, a beetle that started at (r, c) with first move horizontal:
- Column = c + (sum of ceil(t/2) values of ±1) → column has same parity as c + ceil(t/2)
- Row = r + (sum of floor(t/2) values of ±1) → row has same parity as r + floor(t/2)

So column ∈ {c - ceil(t/2), c - ceil(t/2) + 2, ..., c + ceil(t/2)} (same parity as c + ceil(t/2))
Row ∈ {r - floor(t/2), r - floor(t/2) + 2, ..., r + floor(t/2)} (same parity as r + floor(t/2))

For a beetle with first move vertical:
- Column = c + (sum of floor(t/2) values of ±1) → parity c + floor(t/2)
- Row = r + (sum of ceil(t/2) values of ±1) → parity r + ceil(t/2)

Now, the question is about guaranteeing a collision. We want the minimum number of beetles such that no matter how they're placed and how they move, two must collide at some time.

This is a pigeonhole-type problem. We need to find the maximum number of beetles that can be placed such that they can all move without ever colliding. Then the answer is that number plus 1.

So we need to find the maximum size of a set of beetles (with starting positions and movement strategies) such that no two ever occupy the same square at the same time.

Let me think about invariants that prevent collision.

Consider two beetles. When can they avoid collision forever?

Let me think about parity-based arguments. Consider the "color" of a beetle's position.

At time t, a beetle at position (r, c). Let's think about r + c mod 2. Each move (L, R, U, D) changes r+c by ±1, so r+c mod 2 changes every step. So at time t, (r+c) mod 2 = (r_0 + c_0 + t) mod 2. This is the same for all beetles! So the checkerboard color at time t is determined by t mod 2 and the starting color. Two beetles starting on the same color will always be on the same color at every time, and two starting on different colors will always be on different colors. So beetles on different colors can never collide. That gives us a lower bound based on the two color classes, but that's just 2 classes, not very helpful directly.

Let me think more carefully. We need a finer invariant.

Let me consider the position at even times and odd times separately, or think about 2-step moves.

Consider what happens over 2 minutes. A beetle moves horizontally then vertically (or vice versa). So in 2 minutes, the beetle's position changes by (±1 in row, ±1 in col) — i.e., it moves to a diagonally adjacent square. The net change in 2 minutes is (±1, ±1) in (row, col).

So at even times (0, 2, 4, ...), the beetle is at positions that differ from the start by (sum of ±1 in row, sum of ±1 in col) where the number of terms is t/2 each.

At even time 2k, a beetle starting at (r, c):
- Position = (r + a, c + b) where a is a sum of k values of ±1, b is a sum of k values of ±1.
- So |a| ≤ k, |b| ≤ k, and a ≡ k (mod 2), b ≡ k (mod 2).

Now, consider two beetles at even times. Beetle 1 at (r1 + a1, c1 + b1) and beetle 2 at (r2 + a2, c2 + b2) at time 2k. They collide if r1 + a1 = r2 + a2 and c1 + b1 = c2 + b2.

This is getting complex. Let me think about the problem from a different angle.

Let me think about the "type" of a beetle based on its starting position and first move direction.

Actually, let me think about a key invariant. Consider the quantity (row + column) mod 2 at even times. At time 2k, the position is (r_0 + a, c_0 + b) where a, b are sums of k ±1's. So (r + c) mod 2 = (r_0 + c_0 + a + b) mod 2 = (r_0 + c_0 + 2k) mod 2 = (r_0 + c_0) mod 2. So at even times, the checkerboard color is the same as the starting color. That's consistent with what we found (at time t, color = (r_0 + c_0 + t) mod 2, and at even t, this is r_0 + c_0 mod 2).

Now let me think about a more refined invariant. Consider (row - column) mod 2 at even times. (r_0 + a - c_0 - b) mod 2 = (r_0 - c_0 + a - b) mod 2 = (r_0 - c_0) mod 2 (since a - b has the same parity as a + b = 2k... wait, a and b each have parity k mod 2, so a - b has parity 0 mod 2). So (row - col) mod 2 at even times = (r_0 - c_0) mod 2. This is a fixed invariant!

So at even times, (row + col) mod 2 = (r_0 + c_0) mod 2 and (row - col) mod 2 = (r_0 - c_0) mod 2. These two together determine (row mod 2, col mod 2) at even times: row mod 2 = r_0 mod 2 and col mod 2 = c_0 mod 2. So at even times, the beetle is always on a square with the same (row parity, col parity) as its start. That makes sense since in 2 steps, the beetle moves (±1, ±1), preserving both parities.

Similarly, at odd times, the beetle has moved an odd number of steps. If first move is horizontal: at odd time 2k+1, the beetle has made k+1 horizontal moves and k vertical moves. Position = (r_0 + sum of k ±1's, c_0 + sum of (k+1) ±1's). So row mod 2 = (r_0 + k) mod 2, col mod 2 = (c_0 + k + 1) mod 2.

If first move is vertical: at odd time 2k+1, position = (r_0 + sum of (k+1) ±1's, c_0 + sum of k ±1's). So row mod 2 = (r_0 + k + 1) mod 2, col mod 2 = (c_0 + k) mod 2.

This is getting complicated. Let me think about the problem more abstractly.

The key insight in these types of problems is usually about finding an invariant that partitions the board into classes, where beetles in different classes can never collide. Then the answer is (size of largest class) + 1, but we also need to show that within a class, enough beetles must collide.

Wait, actually, the problem is asking for the minimum number of beetles to GUARANTEE a collision regardless of placement and movement. So we need:
- A lower bound: exhibit a configuration of N-1 beetles with no collision possible (i.e., a strategy to avoid collision).
- An upper bound: show that N beetles always produce a collision.

For the lower bound, we want to place as many beetles as possible such that they can all avoid each other. The invariant approach helps: if we can partition the board into classes such that beetles in different classes never collide, then we can place one beetle per class... but actually we need to be more careful. We need to show that within each class, we can also avoid collisions, or that we can place beetles such that they avoid collisions.

Hmm, let me think about this differently.

Actually, let me think about what "avoid collision" means. Each beetle has freedom in choosing its moves (at each step, it chooses left or right, or up or down, subject to the alternation constraint). The adversary (who wants to avoid collision) chooses both the starting positions and the movement strategies.

So the question is: what is the maximum number of beetles that can be placed (with starting positions and movement strategies) such that no two ever collide? The answer to the problem is this maximum plus 1.

Let me think about the structure of a single beetle's trajectory. A beetle's trajectory is determined by:
1. Starting position (r, c).
2. First move direction: horizontal (H) or vertical (V).
3. At each step, the choice of sign (+1 or -1).

So the trajectory is: (r, c) → (r, c ± 1) → (r ± 1, c ± 1) → (r ± 1, c ± 1 ± 1) → ...

The key constraint is the alternation between H and V.

Let me think about a simpler version first. Consider a 1D version: beetles on a line of length n, each moving ±1 at each step. What's the minimum to guarantee a collision? In 1D, each beetle moves ±1 each step. Two beetles starting at positions with the same parity will always have the same parity at every step. If they start at the same position, they collide at time 0. If they start at different positions with the same parity, they can potentially avoid each other (by moving in the same direction, maintaining distance). Actually in 1D, two beetles at positions a < b with the same parity: at each step, both move ±1. If beetle 1 moves right and beetle 2 moves right, the distance is maintained. So they can avoid collision. But if there are many beetles, by pigeonhole...

Actually, in 1D with no constraints on movement (just ±1 each step), the answer would be related to the number of positions. But with the alternation constraint, it's different.

Let me go back to the 2D problem and think about it more carefully.

Let me consider the positions of beetles at even times only. At even time 2k, each beetle is at a position that differs from its start by (Δr, Δc) where Δr and Δc are each sums of k values of ±1. So the beetle is at (r_0 + Δr, c_0 + Δc) where |Δr| ≤ k, |Δc| ≤ k, Δr ≡ k (mod 2), Δc ≡ k (mod 2).

Now, consider two beetles. At even time 2k, beetle 1 is at (r1 + Δr1, c1 + Δc1) and beetle 2 is at (r2 + Δr2, c2 + Δc2). They collide iff r1 + Δr1 = r2 + Δr2 and c1 + Δc1 = c2 + Δc2, i.e., Δr1 - Δr2 = r2 - r1 and Δc1 - Δc2 = c2 - c1.

Since Δr1 is a sum of k ±1's and Δr2 is a sum of k ±1's, Δr1 - Δr2 is a sum of 2k ±1's, ranging from -2k to 2k with the right parity. Similarly for Δc1 - Δc2.

This is quite flexible, so collision seems hard to avoid for many beetles. But the adversary controls the moves, so they can try to keep beetles apart.

Let me think about this problem from the perspective of known competition problems. This seems like a competition problem (the 2023 × 2023 board suggests it's from a 2023 competition). Let me think about what the answer might be.

Actually, I recall a similar problem. The key idea is often about the "type" of a beetle based on (row parity, column parity, first move direction). Let me explore this.

At even times, a beetle is always at (row ≡ r_0 mod 2, col ≡ c_0 mod 2). So the (row mod 2, col mod 2) is invariant at even times.

At odd times, the position depends on the first move direction:
- If first move H: at odd time 2k+1, row ≡ r_0 + k mod 2, col ≡ c_0 + k + 1 mod 2. So (row mod 2, col mod 2) = (r_0 + k, c_0 + k + 1) mod 2.
- If first move V: at odd time 2k+1, (row mod 2, col mod 2) = (r_0 + k + 1, c_0 + k) mod 2.

Hmm, this depends on k, so it's not a fixed invariant at odd times. Let me reconsider.

Actually, let me think about the quantity (row + col) mod 2 and (row - col) mod 2 at all times.

At time t, (row + col) mod 2 = (r_0 + c_0 + t) mod 2 (since each step changes row+col by ±1, flipping parity).

For (row - col) mod 2: Let's compute. At time t, row = r_0 + R(t), col = c_0 + C(t), where R(t) is the total vertical displacement and C(t) is the total horizontal displacement. R(t) + C(t) = t (total steps). So (row - col) mod 2 = (r_0 - c_0 + R(t) - C(t)) mod 2 = (r_0 - c_0 + R(t) - (t - R(t))) mod 2 = (r_0 - c_0 + 2R(t) - t) mod 2 = (r_0 - c_0 - t) mod 2 = (r_0 - c_0 + t) mod 2.

So (row - col) mod 2 = (r_0 - c_0 + t) mod 2 as well.

So both (row + col) mod 2 and (row - col) mod 2 change by t mod 2 from the start. This means:
- row mod 2 = ((row+col) + (row-col))/2 mod 2... hmm, this isn't straightforward in mod 2.

Let me think in terms of mod 2 directly. row mod 2 and col mod 2. At time t:
- (row + col) mod 2 = (r_0 + c_0 + t) mod 2
- (row - col) mod 2 = (r_0 - c_0 + t) mod 2

From these: row mod 2 = ((row+col) + (row-col)) / 2 mod 2. But division by 2 in mod 2 doesn't work. Let me use mod 4 or think differently.

Actually, (row + col) mod 2 and (row - col) mod 2 together determine (row mod 2, col mod 2) only if we know them mod 2:
- row mod 2 = ((row+col) + (row-col)) / 2 mod 2. But (row+col) and (row-col) have the same parity (both even or both odd, since their difference is 2*col). So (row+col) + (row-col) = 2*row, which is always even. So we can't directly get row mod 2 from (row+col) mod 2 and (row-col) mod 2 alone.

Let me just track row mod 2 and col mod 2 directly.

At time t, the beetle has made some horizontal and some vertical moves. Let h(t) = number of horizontal moves in first t steps, v(t) = number of vertical moves. h(t) + v(t) = t.

If first move is H: h(t) = ceil(t/2), v(t) = floor(t/2).
If first move is V: h(t) = floor(t/2), v(t) = ceil(t/2).

Row = r_0 + (sum of v(t) ±1's), so row mod 2 = (r_0 + v(t)) mod 2.
Col = c_0 + (sum of h(t) ±1's), so col mod 2 = (c_0 + h(t)) mod 2.

Case 1: First move H.
- At even t = 2k: h = k, v = k. Row mod 2 = (r_0 + k) mod 2, Col mod 2 = (c_0 + k) mod 2.
- At odd t = 2k+1: h = k+1, v = k. Row mod 2 = (r_0 + k) mod 2, Col mod 2 = (c_0 + k+1) mod 2.

Case 2: First move V.
- At even t = 2k: h = k, v = k. Row mod 2 = (r_0 + k) mod 2, Col mod 2 = (c_0 + k) mod 2.
- At odd t = 2k+1: h = k, v = k+1. Row mod 2 = (r_0 + k+1) mod 2, Col mod 2 = (c_0 + k) mod 2.

So at even times, both cases give the same: (Row mod 2, Col mod 2) = (r_0 + k, c_0 + k) mod 2. This depends on k, so it's not a fixed invariant. At time 2k, the parity class is (r_0 + k, c_0 + k) mod 2.

At odd times, the two cases differ:
- Case 1 (first H): (r_0 + k, c_0 + k + 1) mod 2 at time 2k+1.
- Case 2 (first V): (r_0 + k + 1, c_0 + k) mod 2 at time 2k+1.

Interesting. So at odd times, the parity class depends on the first move direction.

Now, for two beetles to collide at time t, they must be in the same parity class at time t. Let me see when two beetles can be in the same parity class at all times (a necessary condition for collision).

Actually, for collision avoidance, we want to find beetles that are NEVER in the same parity class at the same time. If two beetles are always in different parity classes, they can never collide.

Let me consider two beetles with starting positions (r1, c1) and (r2, c2) and first move directions d1 and d2 (each H or V).

At even time 2k:
- Beetle 1: parity class (r1 + k, c1 + k) mod 2.
- Beetle 2: parity class (r2 + k, c2 + k) mod 2.
- Same iff (r1 + k, c1 + k) ≡ (r2 + k, c2 + k) mod 2, i.e., (r1, c1) ≡ (r2, c2) mod 2.

So at even times, two beetles are in the same parity class iff their starting positions have the same (row mod 2, col mod 2). This is independent of k and the first move direction!

At odd time 2k+1:
- Beetle 1 (first H): (r1 + k, c1 + k + 1) mod 2.
- Beetle 1 (first V): (r1 + k + 1, c1 + k) mod 2.
- Beetle 2 (first H): (r2 + k, c2 + k + 1) mod 2.
- Beetle 2 (first V): (r2 + k + 1, c2 + k) mod 2.

Case both H: same iff (r1, c1) ≡ (r2, c2) mod 2.
Case both V: same iff (r1, c1) ≡ (r2, c2) mod 2.
Case 1 H, 2 V: (r1 + k, c1 + k + 1) vs (r2 + k + 1, c2 + k). Same iff r1 ≡ r2 + 1 and c1 + 1 ≡ c2 mod 2, i.e., (r1, c1) ≡ (r2 + 1, c2 + 1) mod 2, i.e., (r1 - r2) ≡ 1 and (c1 - c2) ≡ 1 mod 2.
Case 1 V, 2 H: (r1 + k + 1, c1 + k) vs (r2 + k, c2 + k + 1). Same iff r1 + 1 ≡ r2 and c1 ≡ c2 + 1 mod 2, i.e., (r1 - r2) ≡ -1 ≡ 1 and (c1 - c2) ≡ 1 mod 2. Same as above.

So at odd times:
- If both have the same first move direction: same parity class iff (r1, c1) ≡ (r2, c2) mod 2.
- If different first move directions: same parity class iff (r1 - r2) ≡ 1 and (c1 - c2) ≡ 1 mod 2, i.e., r1 and r2 have different parity AND c1 and c2 have different parity.

Now, for two beetles to potentially collide, they need to be in the same parity class at some time. For them to NEVER collide (even potentially), they must be in different parity classes at ALL times.

When are two beetles always in different parity classes?

At even times: different parity classes iff (r1, c1) ≢ (r2, c2) mod 2, i.e., they start in different (row mod 2, col mod 2) classes.

If they start in different parity classes, they're always in different classes at even times. What about odd times?

If (r1, c1) ≢ (r2, c2) mod 2, there are three sub-cases:
(a) r1 ≡ r2 but c1 ≢ c2 mod 2.
(b) r1 ≢ r2 but c1 ≡ c2 mod 2.
(c) r1 ≢ r2 and c1 ≢ c2 mod 2.

At odd times:
- Same first move direction: same parity class iff (r1, c1) ≡ (r2, c2) mod 2, which is false. So different parity classes. Good.
- Different first move directions: same parity class iff (r1 - r2) ≡ 1 and (c1 - c2) ≡ 1 mod 2. This is true only in case (c).

So:
- In cases (a) and (b): at all times (even and odd), the two beetles are in different parity classes, regardless of first move directions. They can NEVER collide.
- In case (c): at even times, they're in different classes. At odd times, if they have different first move directions, they're in the SAME class. If they have the same first move direction, they're in different classes.

So in case (c), if both beetles have the same first move direction, they're always in different parity classes and can never collide. If they have different first move directions, they could potentially collide at odd times.

This gives us a way to place beetles that never collide: place beetles such that any two are in case (a), (b), or (c) with same first move direction.

Let me formalize. Define the "type" of a beetle as (r_0 mod 2, c_0 mod 2, d) where d ∈ {H, V} is the first move direction. There are 4 × 2 = 8 types.

Two beetles of the same type: (r1, c1) ≡ (r2, c2) mod 2 and same d. At even times, same parity class (so they could collide). At odd times, same parity class (same d, same starting parity). So they could collide at all times. Not good for avoidance.

Two beetles with same (r mod 2, c mod 2) but different d: At even times, same parity class. At odd times, different parity class (since different d and (r1-c1) ≡ (r2-c2) mod 2 means (r1-r2) and (c1-c2) are both even, not both odd). So they could collide at even times.

Two beetles with different (r mod 2, c mod 2):
- Cases (a) or (b): always different parity classes. Never collide.
- Case (c) with same d: always different parity classes. Never collide.
- Case (c) with different d: different at even times, same at odd times. Could collide at odd times.

So to maximize non-colliding beetles, we want to choose types such that any two beetles are always in different parity classes.

The types that are "always different" from each other:
- Types in case (a) or (b) relative to each other: these are types where exactly one of (r mod 2, c mod 2) differs. E.g., (0,0,H) and (0,1,H), or (0,0,H) and (1,0,V), etc.
- Types in case (c) with same d: e.g., (0,0,H) and (1,1,H).

Let me enumerate. The 8 types are:
(0,0,H), (0,0,V), (0,1,H), (0,1,V), (1,0,H), (1,0,V), (1,1,H), (1,1,V).

Two types are "compatible" (always different parity classes) if:
- They differ in exactly one of (r mod 2, c mod 2): cases (a), (b). Compatible regardless of d.
- They differ in both (r mod 2, c mod 2) AND have the same d: case (c) with same d. Compatible.

Two types are "incompatible" (could collide) if:
- Same (r mod 2, c mod 2): could collide at even times (and odd times if same d).
- Differ in both (r mod 2, c mod 2) AND different d: could collide at odd times.

So the compatibility graph: we want an independent set in the "incompatibility" graph, or equivalently a clique in the compatibility graph.

Let me list which pairs are compatible:
- (0,0,H) is compatible with: (0,1,*) [case a], (1,0,*) [case b], (1,1,H) [case c same d]. Not compatible with: (0,0,V) [same parity], (1,1,V) [case c diff d].
- (0,0,V) is compatible with: (0,1,*), (1,0,*), (1,1,V). Not compatible with: (0,0,H), (1,1,H).
- (0,1,H) is compatible with: (0,0,*), (1,1,*), (1,0,H). Not compatible with: (0,1,V), (1,0,V).
- (0,1,V) is compatible with: (0,0,*), (1,1,*), (1,0,V). Not compatible with: (0,1,H), (1,0,H).
- (1,0,H) is compatible with: (1,1,*), (0,0,*), (0,1,H). Not compatible with: (1,0,V), (0,1,V).
- (1,0,V) is compatible with: (1,1,*), (0,0,*), (0,1,V). Not compatible with: (1,0,H), (0,1,H).
- (1,1,H) is compatible with: (1,0,*), (0,1,*), (0,0,H). Not compatible with: (1,1,V), (0,0,V).
- (1,1,V) is compatible with: (1,0,*), (0,1,*), (0,0,V). Not compatible with: (1,1,H), (0,0,H).

So the incompatibility pairs are:
- Same (r,c) parity, any d: (0,0,H)-(0,0,V), (0,1,H)-(0,1,V), (1,0,H)-(1,0,V), (1,1,H)-(1,1,V).
- Different (r,c) parity (both differ), different d: (0,0,H)-(1,1,V), (0,0,V)-(1,1,H), (0,1,H)-(1,0,V), (0,1,V)-(1,0,H).

So the incompatibility graph has 8 vertices and 8 edges. We want the maximum independent set.

Let me find it. The edges are:
1. (0,0,H) - (0,0,V)
2. (0,1,H) - (0,1,V)
3. (1,0,H) - (1,0,V)
4. (1,1,H) - (1,1,V)
5. (0,0,H) - (1,1,V)
6. (0,0,V) - (1,1,H)
7. (0,1,H) - (1,0,V)
8. (0,1,V) - (1,0,H)

This graph is a union of two 4-cycles? Let me check.

Vertices: let me label them:
A = (0,0,H), B = (0,0,V), C = (0,1,H), D = (0,1,V), E = (1,0,H), F = (1,0,V), G = (1,1,H), H = (1,1,V).

Edges:
1. A-B
2. C-D
3. E-F
4. G-H
5. A-H
6. B-G
7. C-F
8. D-E

So the graph looks like:
A - B, A - H
B - G
G - H, G - B
C - D, C - F
D - E
E - F, E - D

So we have two connected components:
Component 1: A, B, G, H with edges A-B, A-H, B-G, G-H. This is a 4-cycle A-B-G-H-A.
Component 2: C, D, E, F with edges C-D, C-F, D-E, E-F. This is a 4-cycle C-D-E-F-C.

Each component is a 4-cycle. The maximum independent set of a 4-cycle is 2. So the maximum independent set of the whole graph is 2 + 2 = 4.

So we can have at most 4 types that are pairwise compatible. For example: {A, G} from component 1 (A and G are not adjacent) and {C, E} from component 2 (C and E are not adjacent). Let me verify:
- A = (0,0,H), G = (1,1,H): case (c) same d. Compatible. ✓
- C = (0,1,H), E = (1,0,H): case (c) same d. Compatible. ✓
- A = (0,0,H), C = (0,1,H): case (a). Compatible. ✓
- A = (0,0,H), E = (1,0,H): case (b). Compatible. ✓
- G = (1,1,H), C = (0,1,H): case (b). Compatible. ✓
- G = (1,1,H), E = (1,0,H): case (a). Compatible. ✓

So {A, C, E, G} = {(0,0,H), (0,1,H), (1,0,H), (1,1,H)} is a set of 4 pairwise compatible types. These are all the H types! Similarly, {B, D, F, H} = all V types would also work.

Wait, that makes sense. If all beetles have the same first move direction (all H or all V), then:
- At even times: two beetles are in the same parity class iff same (r mod 2, c mod 2). So beetles in different parity classes are always separated at even times.
- At odd times: with same d, two beetles are in the same parity class iff same (r mod 2, c mod 2). So again, different parity classes are always separated.

So if all beetles move H first, then beetles in different (r mod 2, c mod 2) classes are always in different parity classes. There are 4 parity classes, so we can have 4 groups of beetles, one per parity class, and beetles in different groups never collide.

But within a parity class, beetles could collide. So the question becomes: within a single parity class, how many beetles can we place without collision?

Hmm wait, but we also need to consider the board size. The board is 2023 × 2023. Each parity class has roughly (2023/2)² ≈ 1012² squares (approximately, since 2023 is odd).

Actually, 2023 = 2 × 1011 + 1. So the number of squares with (row mod 2, col mod 2) = (0, 0) is 1012 × 1012 (rows 0, 2, 4, ..., 2022 → 1012 rows; same for columns). Similarly for other parity classes. Actually, rows 1, 3, ..., 2021 → 1011 rows. So:
- (0, 0): 1012 × 1012
- (0, 1): 1012 × 1011
- (1, 0): 1011 × 1012
- (1, 1): 1011 × 1011

OK so the parity classes have different sizes. But the point is, within each parity class, we need to determine how many beetles can coexist without collision.

Now, within a single parity class, all beetles are always in the same parity class at every time (if they all have the same first move direction). So the parity argument doesn't help within a class. We need a different argument.

Let me think about what happens within a parity class. Consider beetles all starting in the same parity class, all with first move H. At even time 2k, all are at positions (r_0 + k mod 2, c_0 + k mod 2) parity. At odd time 2k+1, all are at (r_0 + k mod 2, c_0 + k+1 mod 2) parity.

Hmm, this is still complex. Let me think about the problem differently.

Actually, I think the key insight might be simpler. Let me reconsider.

The problem is about guaranteeing a collision. The answer is likely related to the number of "independent" trajectories possible.

Let me think about it from the perspective of the maximum number of non-colliding beetles.

Claim: The maximum number of beetles that can be placed without any collision is related to the number of squares divided by something, or it could be a small number.

Wait, actually, I think the answer might be much smaller. Let me reconsider.

Consider the "2-step" movement. Every 2 steps, a beetle moves to a diagonally adjacent square (±1 in row, ±1 in col). So at even times, the beetle is doing a random walk on the "diagonal lattice" — it moves to one of 4 diagonal neighbors every 2 steps.

Now, consider the sublattice of positions with the same (r mod 2, c mod 2). This is a lattice of spacing 2. The beetle moves on this lattice, and at each 2-step interval, it moves to one of 4 diagonal neighbors (which are the 4 neighbors on this sublattice).

So at even times, the beetle is doing a standard random walk (4 directions) on a grid of size approximately 1012 × 1012 (for the (0,0) parity class).

Now, the question reduces to: on a grid, how many random walkers can you have such that no two ever collide? Each walker moves to one of 4 neighbors at each step.

But the walkers are controlled by an adversary who wants to avoid collisions. So the adversary chooses the moves.

Hmm, but even with an adversary, if you have too many walkers on a finite grid, they must eventually collide, right? Actually no — the adversary can potentially keep them apart if there's enough space.

Wait, but the grid is finite (2023 × 2023), and the beetles can't leave the board. Actually, can they? The problem says they move left, right, up, or down. If a beetle is at the edge, can it move off the board? The problem doesn't explicitly say they can't leave the board, but it says "on a 2023 × 2023 board," so I think they must stay on the board. Actually, re-reading: "some squares contain a beetle" and "each beetle moves one square to the left, right, up, or down." It doesn't say they can't move off the board. But if they move off, they're no longer on the board, and the question is about two beetles being in the same square. If a beetle leaves the board, it's not in any square, so it can't collide.

Hmm, but that would make the problem trivial — just have all beetles walk off the board. So I think the implicit assumption is that beetles stay on the board, or the problem is about a torus, or the beetles can't leave.

Actually, I think the standard interpretation is that the beetles must stay on the board. If a beetle is at the edge, it can't move in the direction that would take it off the board. Or perhaps the board is a torus. Let me re-read the problem.

"On a 2023 × 2023 board, some squares contain a beetle... After one minute, each beetle moves one square to the left, right, up, or down."

I think the beetles must stay on the board. If a beetle can't move in a certain direction (because it would go off the board), it must choose another direction. But with the alternation constraint, this might not always be possible... unless the board is large enough that edge effects don't matter, or the problem is on a torus.

Actually, for a competition problem, I think the answer doesn't depend on edge effects (the board is large enough), and the key is the combinatorial/parity argument. Let me think about this more carefully.

Let me reconsider the problem. I think the key is:

1. We can partition all possible beetle trajectories into a certain number of "classes" such that beetles in different classes never collide.
2. Within each class, any two beetles must eventually collide (or the class has a maximum size).

For part 1, we found that the "type" (r mod 2, c mod 2, first move direction) gives 8 types, and the maximum set of pairwise compatible types is 4 (either all H or all V, with one beetle per parity class).

But wait, that's the type compatibility. Within a compatible set of types, we can have one beetle per type. But can we have multiple beetles of the same type? No, because beetles of the same type could collide.

Hmm, but that would give an answer of 5 (4 + 1), which seems too small for a 2023 × 2023 board.

I think I'm missing something. Let me reconsider.

Actually, two beetles of the same type (same r mod 2, c mod 2, same first move direction) CAN collide, but they don't HAVE to collide. The adversary controls the moves and can potentially keep them apart. So the question is whether the adversary can keep two same-type beetles apart forever.

So the type analysis gives us: beetles of compatible types can be kept apart (they're in different parity classes at all times). But beetles of incompatible types MIGHT collide — the adversary might or might not be able to avoid collision.

So the type analysis gives a lower bound: we can place 4 beetles (one per parity class, all with first move H) and they never collide. But can we place more?

Yes! We can place multiple beetles in the same parity class, as long as the adversary can keep them apart. For example, two beetles in the same parity class but far apart on the board can be kept apart by moving them in sync.

So the type analysis is not sufficient. We need a more refined argument.

Let me think about this differently. Consider the "2-step walk" on the sublattice. At even times, each beetle is on a sublattice point and moves to a diagonal neighbor. The adversary controls the moves.

The question is: on a grid of size m × m (where m ≈ 1012), how many walkers can the adversary control such that no two ever occupy the same point?

If the walkers can be kept apart, then we can have many beetles. The adversary's strategy: keep all beetles moving in the same direction (e.g., all move (1,1) every 2 steps). Then they maintain their relative positions and never collide, as long as they start at different positions. But they'd eventually hit the boundary...

If the board is finite and beetles can't leave, then eventually they're forced together. But if the board is a torus (wrapping around), they can keep going forever.

Hmm, I think the problem might intend for the board to be finite with boundaries, and beetles can't leave. In that case, the boundary forces collisions eventually.

But actually, even on a finite board, the adversary might be able to keep beetles apart by having them move back and forth. For example, a beetle could oscillate: move right, up, left, down, right, up, ... This is a 4-cycle that stays in a 2×2 area. If each beetle has its own 2×2 area, they never collide.

Wait, but the beetles need to alternate H and V. Let me check: right (H), up (V), left (H), down (V), right (H), ... Yes, this alternates correctly. And the beetle returns to its starting position every 4 steps. So it stays in a 2×2 area.

So if we can pack beetles such that each has its own 2×2 area, they never collide. On a 2023 × 2023 board, we can fit roughly (2023/2)² ≈ 1012² such beetles. But 2023 is odd, so we can fit 1011 × 1011 = 1,022,121 non-overlapping 2×2 blocks, with some squares left over.

But wait, can we do better? Can we pack beetles more densely?

Actually, the 4-cycle (right, up, left, down) uses a 2×2 block. But we could also use a different pattern. For instance, a beetle could move right, up, right, down, left, down, left, up, ... which is a larger cycle. But the 2×2 cycle is the most compact.

However, can two beetles share a 2×2 block without colliding? If they're in the same 2×2 block but at different positions and move in sync, they might avoid collision. For example, in a 2×2 block, place two beetles at diagonally opposite corners, both doing the same 4-cycle. They'd be at diagonally opposite positions at all times, never colliding. So we can fit 2 beetles per 2×2 block!

Wait, let me check. 2×2 block with positions (0,0), (0,1), (1,0), (1,1). Beetle 1 at (0,0) doing cycle: right→(0,1), up→(1,1), left→(1,0), down→(0,0). Wait, "up" should decrease row or increase row? Let me say up = row+1, down = row-1, right = col+1, left = col-1.

Beetle 1 at (0,0): right→(0,1), up→(1,1), left→(1,0), down→(0,0). Cycle: (0,0)→(0,1)→(1,1)→(1,0)→(0,0).

Beetle 2 at (1,1): right→(1,2)... wait, that goes outside the 2×2 block. Let me instead have beetle 2 do the same cycle: (1,1)→(1,2)... no, that's outside.

Let me have beetle 2 start at (1,1) and do the same cycle pattern: right→(1,2), up→(2,2)... that goes outside.

Instead, let me have beetle 2 do the opposite cycle: (1,1)→(1,0)→(0,0)→(0,1)→(1,1). That's left, down, right, up. Let's check alternation: left (H), down (V), right (H), up (V). Yes, alternates correctly.

At time 0: beetle 1 at (0,0), beetle 2 at (1,1). Different. ✓
At time 1: beetle 1 at (0,1), beetle 2 at (1,0). Different. ✓
At time 2: beetle 1 at (1,1), beetle 2 at (0,0). Different. ✓
At time 3: beetle 1 at (1,0), beetle 2 at (0,1). Different. ✓
At time 4: back to start. ✓

So two beetles can share a 2×2 block without colliding. Can we fit 3 or 4 beetles in a 2×2 block?

With 4 beetles in a 2×2 block, one at each position, they'd collide at time 0. So at most 2 per 2×2 block (since there are 4 positions and 2 time steps in a period, we need 4 positions × ... hmm).

Actually, with 2 beetles in a 2×2 block, they occupy 2 of the 4 positions at any time. Could we fit more? Let's think: at any given time, each position in the 2×2 block can have at most 1 beetle. So at most 4 beetles at any time. But they move, so we need to check if 4 beetles can cycle without collision.

4 beetles, one at each position of the 2×2 block, all doing the same cycle direction: (0,0)→(0,1)→(1,1)→(1,0)→(0,0). At time 0: positions (0,0), (0,1), (1,0), (1,1). At time 1: (0,1), (1,1), (0,0), (1,0). Wait, beetle at (0,1) goes to (1,1) (up), beetle at (1,1) goes to (1,0) (left), beetle at (1,0) goes to (0,0) (down), beetle at (0,0) goes to (0,1) (right). So at time 1: (0,1), (1,1), (0,0), (1,0) — same set of positions! No collision. At time 2: each moves again. (0,1)→(1,1), (1,1)→(1,0), (0,0)→(0,1), (1,0)→(0,0). Positions: (1,1), (1,0), (0,1), (0,0). Same set. No collision.

Wait, so 4 beetles can share a 2×2 block if they all cycle in the same direction? Let me recheck.

At time 0: beetles at (0,0), (0,1), (1,0), (1,1) — all 4 positions.
At time 1: beetle from (0,0) → (0,1) [right], beetle from (0,1) → (1,1) [up], beetle from (1,0) → (0,0) [down], beetle from (1,1) → (1,0) [left].
Positions at time 1: (0,1), (1,1), (0,0), (1,0) — all 4 positions, no collision. ✓

At time 2: beetle from (0,1) → (1,1) [up], beetle from (1,1) → (1,0) [left], beetle from (0,0) → (0,1) [right], beetle from (1,0) → (0,0) [down].
Positions: (1,1), (1,0), (0,1), (0,0) — all 4, no collision. ✓

So 4 beetles can share a 2×2 block! They just cycle around. This means we can have 4 beetles per 2×2 block, which is 1 beetle per square. So we can fill the entire board with beetles, one per square, and they never collide?

Wait, that can't be right. If every square has a beetle, they all cycle in their 2×2 blocks. But adjacent 2×2 blocks share boundary squares... no, if we tile the board with non-overlapping 2×2 blocks, each square belongs to exactly one block. With a 2023 × 2023 board, we can tile it with 2×2 blocks covering 2022 × 2022 squares (1011 × 1011 blocks), leaving a row and column of squares uncovered.

So we can place 4 × 1011 × 1011 = 4,088,484 beetles (filling the 2022 × 2022 sub-board) without collision. Plus we might be able to place more in the remaining row and column.

But wait, this means the answer is at least 4,088,485, which is close to 2023² / something. But actually, 2023² = 4,092,529. And 4,088,484 = 2022² = (2023-1)². So we can fill almost the entire board.

Hmm, but can we fill the entire board? The remaining squares form an L-shape: row 2022 (columns 0-2022) and column 2022 (rows 0-2021). Can we place beetles there too?

Actually, let me reconsider. If we tile the 2023 × 2023 board with 2×2 blocks, we can cover 2022 × 2022 = 1011² blocks × 4 = 2022² squares. The remaining 2023² - 2022² = (2023-2022)(2023+2022) = 1 × 4045 = 4045 squares form an L-shape.

For the L-shape, can we place beetles that cycle without colliding with each other or with the beetles in the 2×2 blocks?

The beetles in the 2×2 blocks stay within their blocks. The L-shape beetles would need to stay within the L-shape. But the L-shape is only 1 square wide, so a beetle there can't do a 2×2 cycle. It would need to move along the L-shape, but with the alternation constraint (H, V, H, V, ...), it's hard to stay on a 1-wide path.

Actually, a beetle on a 1-wide path (say a single row) can only move left or right (H moves). But it must alternate H and V. On a single row, V moves (up/down) would take it off the row. So it can't stay on a single row unless it can move up/down within the board.

Hmm, the L-shape consists of the last row (row 2022, all columns) and the last column (column 2022, rows 0-2021). A beetle on the last row can move left/right (H) but when it needs to move V (up/down), moving up goes to row 2021 which is in the 2×2 block region. So it would enter a 2×2 block and potentially collide.

This is getting complicated. Let me step back and think about the problem at a higher level.

I think the key insight is:

1. The 2×2 cycling strategy allows us to place 4 beetles per 2×2 block, which is 1 per square, for a large portion of the board.
2. The remaining L-shape is problematic.
3. The answer is likely 2023² - something + 1, or perhaps just 2023² + 1 (if we can fill the entire board).

Wait, but if we can fill the entire board with beetles (one per square), then the answer would be 2023² + 1, which is trivially true (you can't have more beetles than squares). That can't be the intended answer.

Let me reconsider. Can we actually fill the entire board? The 2×2 cycling works for the 2022 × 2022 sub-board. For the remaining L-shape (4045 squares), we need a different strategy.

Actually, maybe we can use a different tiling. Instead of 2×2 blocks, use a pattern that covers the entire board.

Alternatively, maybe the beetles don't need to cycle in 2×2 blocks. They could follow longer cycles that cover the entire board.

Consider a Hamiltonian cycle on the 2023 × 2023 grid graph. If all beetles are placed on this cycle, equally spaced, and all move along the cycle at the same speed, they never collide. But the cycle alternates between H and V moves? Not necessarily — a grid graph Hamiltonian cycle doesn't necessarily alternate H and V.

Actually, the constraint is that each beetle alternates H and V. If the cycle alternates H and V, then beetles can follow it. A cycle that alternates H and V on a grid is a cycle on the "diagonal" graph (where you move diagonally). Such cycles exist on even × even grids but not on odd × odd grids (since 2023 is odd).

Hmm, let me think about this differently.

Actually, let me reconsider the 2×2 cycling. In a 2×2 block, the cycle is: right, up, left, down (or any rotation/reflection). This alternates H, V, H, V. ✓

For the L-shape, can we find cycles? The L-shape is a path graph (essentially), and path graphs don't have cycles. So beetles on the L-shape can't cycle.

But maybe we can extend the 2×2 blocks to cover more of the board, or use a different pattern.

Alternatively, maybe the answer is 2022² + 1 = 4,088,485. Let me think about whether this makes sense.

Actually, I realize I should think about this more carefully. Let me reconsider the problem.

The problem asks for the minimum number of beetles to GUARANTEE a collision. This is the maximum number of non-colliding beetles plus 1.

We've shown that 2022² beetles can be placed without collision (using 2×2 cycling on the 2022 × 2022 sub-board). Can we do better?

Let me think about whether we can place beetles on the remaining L-shape as well.

The L-shape consists of:
- Row 2022: columns 0, 1, ..., 2022 (2023 squares)
- Column 2022: rows 0, 1, ..., 2021 (2022 squares)
Total: 2023 + 2022 = 4045 squares.

Can we place beetles on these squares that cycle without colliding?

Consider the corner (2022, 2022). A beetle there needs to move. If it moves left (H) to (2022, 2021), then it needs to move V. Up to (2021, 2021) — but that's in a 2×2 block. Down would go off the board. So it must go up to (2021, 2021), entering a 2×2 block.

This means the L-shape beetles interact with the 2×2 block beetles. This makes it hard to add L-shape beetles without collision.

But maybe we can redesign the tiling to include the L-shape. Instead of 2×2 blocks, use a mix of 2×2 blocks and other structures.

Actually, let me think about this more carefully. The key constraint is that beetles must alternate H and V. A 2×2 cycle naturally does this. But are there other cycles that alternate H and V?

A cycle that alternates H and V on the grid: each step is H or V, alternating. So the cycle has even length, and half the steps are H, half are V. The H steps change the column, V steps change the row. For the cycle to close, the net column change must be 0 and net row change must be 0. The H steps sum to 0 (equal left and right), and V steps sum to 0 (equal up and down).

A 2×2 cycle has 4 steps: 2 H (one left, one right) and 2 V (one up, one down). ✓

A larger cycle: e.g., a 4×4 cycle. Go right 2, up 2, left 2, down 2. But this is 8 steps: R, R, U, U, L, L, D, D. The alternation would be H, H, V, V, H, H, V, V. But we need H, V, H, V, ... So this doesn't work!

The alternation requires H, V, H, V, ... So the cycle must be: H, V, H, V, ..., H, V (even number of steps, alternating). Each H step is ±1 in column, each V step is ±1 in row. For the cycle to close, the sum of H steps = 0 and sum of V steps = 0.

With 2k steps (k H and k V), the H steps are k values of ±1 summing to 0, so k must be even. Similarly k must be even for V. So the cycle length is 2k where k is even, i.e., cycle length is divisible by 4.

The 2×2 cycle has k=2 (length 4). The next possibility is k=4 (length 8): 4 H steps (±1 each, summing to 0) and 4 V steps (±1 each, summing to 0), alternating.

An example of a length-8 cycle: R, U, R, D, L, D, L, U. Let me trace: start at (0,0).
R → (0,1), U → (1,1), R → (0,1)... wait, U should be row+1. Let me use (row, col) with up = row+1.
Start (0,0): R→(0,1), U→(1,1), R→(1,2), D→(0,2), L→(0,1), D→(-1,1)... that goes negative. Let me try differently.

Start (1,1): R→(1,2), U→(2,2), L→(2,1), U→(3,1), L→(3,0), D→(2,0), R→(2,1), D→(1,1). Let me check: this is a cycle of length 8. H, V, H, V, H, V, H, V. ✓ And it covers a 4×3 area (rows 1-3, cols 0-2). Hmm, that's 12 squares but only 8 are visited.

This is getting complicated. Let me think about the problem from a higher level again.

I think the answer is 2023² - 2023 + 1 or something like that. Let me think about what structure allows the maximum number of non-colliding beetles.

Actually, let me reconsider. The 2×2 cycling gives us 4 beetles per 2×2 block. On a 2023 × 2023 board, we can fit 1011 × 1011 = 1,022,121 non-overlapping 2×2 blocks, covering 2022 × 2022 = 4,088,484 squares, with 4,088,484 beetles.

But can we do better? Can we use a different pattern to cover more squares?

Consider a 2×n strip. Can we cycle beetles through a 2×n strip? A 2×n strip has 2n squares. We need a cycle that alternates H and V and covers all 2n squares (or at least allows n beetles to cycle without collision).

In a 2×n strip (2 rows, n columns), a cycle that alternates H and V:
- Start at (0,0): R→(0,1), U→(1,1), L→(1,0), D→(0,0). This is a 2×2 cycle covering 4 squares. For a 2×n strip with n > 2, we'd need a longer cycle.

Try: (0,0)→R→(0,1)→U→(1,1)→R→(1,2)→D→(0,2)→R→(0,3)→U→(1,3)→L→(1,2)→D→(0,2)→L→(0,1)→D→(-1,1)... no, that goes outside.

Hmm, it's hard to make long cycles in a 2×n strip that alternate H and V. The 2×2 cycle seems to be the natural unit.

Let me try a different approach. Instead of trying to cover the entire board, let me think about the theoretical maximum.

Key insight: Consider the "phase" of a beetle. At any given time, a beetle is at some position, and its next move is either H or V. Define the "state" of a beetle as (position, next_move_direction). Two beetles collide if they're at the same position at the same time (regardless of next move direction).

Now, consider the "2-step transition": from even time to even time. At even time 2k, a beetle is at some position, and its next move (at time 2k+1) is determined by its type. After 2 steps, it's at a new position. The 2-step transition moves the beetle to a diagonal neighbor.

For the 2-step walk, the beetle moves on a sublattice (determined by its starting parity class). On this sublattice, it moves to one of 4 diagonal neighbors. This is equivalent to a standard random walk on a grid.

Now, the question is: on a grid of size m × m, what is the maximum number of "walkers" (each controlled by an adversary) such that no two ever collide?

If the walkers can cycle (like the 2×2 cycle), then we can have one walker per grid point, all cycling in sync. This gives m² walkers on an m × m grid.

For the (0,0) parity class, the sublattice has 1012 × 1012 points (rows 0,2,...,2022 and cols 0,2,...,2022). Wait, but the 2×2 cycle uses 4 positions in the original board, which corresponds to 1 position in the sublattice (since all 4 positions in a 2×2 block have the same sublattice point at even times). Hmm, no.

Let me reconsider. At even times, a beetle in the (0,0) parity class is at a position (r, c) with r even and c even. The 2×2 cycle: (0,0)→(0,1)→(1,1)→(1,0)→(0,0). At even times (0, 2, 4, ...), the beetle is at (0,0), (1,1), (0,0), (1,1), ... So at even times, it alternates between (0,0) and (1,1). But (0,0) has (even, even) and (1,1) has (odd, odd). So the beetle switches parity class at even times!

Wait, that contradicts what I said earlier. Let me recheck.

Earlier I said: at even time 2k, (row mod 2, col mod 2) = (r_0 + k, c_0 + k) mod 2. So at time 0 (k=0): (r_0, c_0). At time 2 (k=1): (r_0 + 1, c_0 + 1). At time 4 (k=2): (r_0 + 2, c_0 + 2) = (r_0, c_0). So the parity class alternates between (r_0, c_0) and (r_0+1, c_0+1) at even times, with period 2 in k (i.e., period 4 in time).

So the beetle doesn't stay in one parity class at even times! It alternates between two parity classes: (r_0, c_0) and (r_0+1, c_0+1) mod 2.

This means my earlier analysis of "compatible types" was about when two beetles are in different parity classes at ALL times, which is a stronger condition than I thought.

Let me redo the analysis. At even time 2k, beetle with start (r_0, c_0) and first move H:
- Parity class: (r_0 + k, c_0 + k) mod 2.

At odd time 2k+1, beetle with first move H:
- Parity class: (r_0 + k, c_0 + k + 1) mod 2.

So the parity class at time t (first move H):
- t = 2k: (r_0 + k, c_0 + k) mod 2.
- t = 2k+1: (r_0 + k, c_0 + k + 1) mod 2.

Let me unify: at time t, the parity class is (r_0 + ⌊t/2⌋, c_0 + ⌈t/2⌉) mod 2 for first move H.

For first move V:
- t = 2k: (r_0 + k, c_0 + k) mod 2. (Same as H at even times.)
- t = 2k+1: (r_0 + k + 1, c_0 + k) mod 2.

So at time t, parity class for first move V: (r_0 + ⌈t/2⌉, c_0 + ⌊t/2⌋) mod 2.

Now, two beetles (start 1, d1) and (start 2, d2) are in the same parity class at time t iff:
- If d1 = d2 = H: (r1 + ⌊t/2⌋, c1 + ⌈t/2⌉) ≡ (r2 + ⌊t/2⌋, c2 + ⌈t/2⌉) mod 2, i.e., (r1, c1) ≡ (r2, c2) mod 2. Independent of t!
- If d1 = d2 = V: similarly (r1, c1) ≡ (r2, c2) mod 2. Independent of t.
- If d1 = H, d2 = V: (r1 + ⌊t/2⌋, c1 + ⌈t/2⌉) ≡ (r2 + ⌈t/2⌉, c2 + ⌊t/2⌋) mod 2.
  - At even t = 2k: (r1 + k, c1 + k) ≡ (r2 + k, c2 + k), i.e., (r1, c1) ≡ (r2, c2) mod 2.
  - At odd t = 2k+1: (r1 + k, c1 + k+1) ≡ (r2 + k+1, c2 + k), i.e., r1 ≡ r2+1 and c1+1 ≡ c2 mod 2, i.e., (r1-r2) ≡ 1 and (c1-c2) ≡ 1 mod 2.

So for two beetles with different first move directions:
- At even times: same parity class iff (r1,c1) ≡ (r2,c2) mod 2.
- At odd times: same parity class iff (r1-r2) odd and (c1-c2) odd.

For them to NEVER be in the same parity class:
- At even times: (r1,c1) ≢ (r2,c2) mod 2.
- At odd times: NOT((r1-r2) odd and (c1-c2) odd), i.e., (r1-r2) even OR (c1-c2) even.

If (r1,c1) ≢ (r2,c2) mod 2, then either exactly one of (r1-r2), (c1-c2) is odd, or both are odd.
- If exactly one is odd: at odd times, NOT(both odd) = true. So different parity classes at all times. ✓
- If both odd: at odd times, (both odd) = true, so same parity class. ✗

So for different first move directions, the beetles are always in different parity classes iff exactly one of (r1-r2), (c1-c2) is odd, i.e., they differ in exactly one coordinate's parity. This is the same as cases (a) and (b) from before.

For same first move direction, they're always in different parity classes iff (r1,c1) ≢ (r2,c2) mod 2, i.e., they differ in at least one coordinate's parity. This includes cases (a), (b), and (c).

So the compatibility is:
- Same d, different (r,c) parity (at least one differs): always different parity classes. ✓
- Different d, exactly one parity differs: always different. ✓
- Different d, both parities differ: same at odd times. ✗
- Same d, same (r,c) parity: same at all times. ✗

This is the same as before. So the maximum independent set of types is 4 (all H or all V, one per parity class).

But as I noted, this only gives a lower bound of 5, which is too small. The issue is that beetles of the same type CAN be kept apart by the adversary (they don't HAVE to collide just because they're in the same parity class).

So the type analysis gives us: we can have 4 "groups" (one per parity class, all with first move H), and beetles in different groups never collide. Within each group, beetles are in the same parity class at all times, but the adversary can still try to keep them apart.

Now, within a single group (same parity class, same first move direction), how many beetles can the adversary keep apart?

At even times, all beetles in the group are in the same parity class (which alternates between two classes with period 2 in k). At odd times, they're all in another parity class (also alternating).

The beetles move on the board, and at each step, the adversary chooses the direction (subject to alternation). The question is whether the adversary can keep them apart.

The 2×2 cycling strategy shows that 4 beetles can cycle in a 2×2 block without colliding. These 4 beetles are of different types (different parity classes), so they're in different groups. So within a single group, the 2×2 cycle gives only 1 beetle per 2×2 block.

Wait, let me recheck. In a 2×2 block with positions (0,0), (0,1), (1,0), (1,1), the 4 beetles cycling have starts at these 4 positions. Their types:
- (0,0) with first move H: type (0,0,H).
- (0,1) with first move H: type (0,1,H).
- (1,0) with first move H: type (1,0,H).
- (1,1) with first move H: type (1,1,H).

Wait, but the cycle is: (0,0)→R→(0,1)→U→(1,1)→L→(1,0)→D→(0,0). So:
- Beetle starting at (0,0): first move R (H). Type (0,0,H).
- Beetle starting at (0,1): first move U (V). Type (0,1,V).
- Beetle starting at (1,1): first move L (H). Type (1,1,H).
- Beetle starting at (1,0): first move D (V). Type (1,0,V).

So the 4 beetles have types (0,0,H), (0,1,V), (1,1,H), (1,0,V). These are 4 different types. Are they pairwise compatible?
- (0,0,H) and (0,1,V): different d, exactly one parity differs (c differs). Compatible. ✓
- (0,0,H) and (1,1,H): same d, both parities differ. Compatible. ✓
- (0,0,H) and (1,0,V): different d, exactly one parity differs (r differs). Compatible. ✓
- (0,1,V) and (1,1,H): different d, exactly one parity differs (r differs). Compatible. ✓
- (0,1,V) and (1,0,V): same d, both parities differ. Compatible. ✓
- (1,1,H) and (1,0,V): different d, exactly one parity differs (c differs). Compatible. ✓

All pairwise compatible! So this is one of the maximum independent sets of 4 types. And we have 4 beetles, one per type, in a 2×2 block.

Now, the question is: can we have MORE than 4 beetles in a 2×2 block? No, because there are only 4 squares. And can we have multiple beetles of the same type?

Two beetles of the same type (same parity class, same first move direction) are in the same parity class at all times. Can the adversary keep them apart?

Consider two beetles of type (0,0,H) starting at (0,0) and (2,0) (both even row, even col). At even time 2k, they're at positions with parity (k, k) mod 2. At odd time 2k+1, parity (k, k+1) mod 2. They're in the same parity class at all times.

Can the adversary keep them apart? Yes, if they're far apart and move in sync. For example, both do the 2×2 cycle: beetle 1 at (0,0) cycling in the 2×2 block {(0,0),(0,1),(1,1),(1,0)}, beetle 2 at (2,0) cycling in the 2×2 block {(2,0),(2,1),(3,1),(3,0)}. They never collide.

But wait, beetle 2 at (2,0) with first move H: its 2×2 cycle would be (2,0)→R→(2,1)→U→(3,1)→L→(3,0)→D→(2,0). But (3,1) and (3,0) — row 3 is fine if the board is large enough. And these positions don't overlap with beetle 1's positions. So yes, they can coexist.

So within a single type, we can have many beetles, as long as they're far apart and cycle in their own 2×2 blocks. The number of beetles of a single type is limited by the number of 2×2 blocks available for that type.

Hmm, but this brings us back to the 2×2 tiling. With 1011 × 1011 non-overlapping 2×2 blocks covering 2022 × 2022 squares, we have 4 beetles per block, totaling 4 × 1011² = 4,088,484 beetles. Each block has 4 beetles of 4 different types. So each type has 1011² beetles.

Can we add more beetles? The remaining L-shape has 4045 squares. Can we place beetles there?

The L-shape beetles would need to cycle without colliding with each other or with the 2×2 block beetles. The 2×2 block beetles stay in their blocks, so L-shape beetles just need to stay in the L-shape and not collide with each other.

But as I noted, the L-shape is 1 square wide, and beetles need to alternate H and V. On a 1-wide path, a beetle can do H moves along the path, but V moves would take it off the path (into a 2×2 block region or off the board).

Unless the beetle's V move stays within the L-shape. The L-shape has a corner at (2022, 2022). Near the corner, the L-shape is 2-wide (both row 2022 and column 2022). So near the corner, a beetle could do a small cycle.

Actually, the L-shape is:
- Row 2022: (2022, 0), (2022, 1), ..., (2022, 2022).
- Column 2022: (0, 2022), (1, 2022), ..., (2021, 2022).

The corner (2022, 2022) is shared. Near the corner, we have (2022, 2021), (2022, 2022), (2021, 2022). These form an L. Can a beetle cycle here?

A beetle at (2022, 2021): move R to (2022, 2022) [H], move U to (2021, 2022) [V]... wait, (2021, 2022) is in the L-shape. Then move L to (2021, 2021) [H] — but (2021, 2021) is in a 2×2 block! So the beetle enters a 2×2 block.

Hmm. So the L-shape beetles can't easily cycle without entering the 2×2 block region.

But what if we don't use 2×2 blocks for the entire 2022 × 2022 region? What if we use a different tiling that covers more of the board?

Actually, let me think about this differently. The 2×2 cycling gives 4 beetles per 4 squares = 1 beetle per square. Can we achieve 1 beetle per square on the entire 2023 × 2023 board?

For this, we need a set of 2023² beetles, one per square, each cycling without collision. The cycling must be such that at each time step, the beetles form a permutation of the squares (no two at the same square).

This is equivalent to finding a sequence of permutations π_0, π_1, π_2, ... of the squares such that:
- π_0 = identity (each beetle starts at its own square).
- π_t is a permutation for each t (no collision).
- π_{t+1} differs from π_t by each element moving one step (H or V, alternating).

This is like a "rotor-router" or "round-robin" on the grid.

For a 2n × 2n grid, the 2×2 cycling works: partition into 2×2 blocks, each block cycles. This gives 4n² beetles on a 2n × 2n grid.

For a (2n+1) × (2n+1) grid, we can cover the 2n × 2n sub-grid with 2×2 blocks, but the remaining L-shape is problematic.

Can we cover the L-shape with a different cycle? The L-shape has 4n+1 squares (for a (2n+1) × (2n+1) grid, the L-shape has (2n+1) + 2n = 4n+1 squares). For n = 1011, that's 4045 squares.

We need a cycle (or set of cycles) on the L-shape that alternates H and V. The L-shape is a tree (it's a path with a bend), so it has no cycles. Therefore, we can't have beetles cycle on the L-shape.

But maybe we can use a different decomposition of the entire board, not just 2×2 blocks plus L-shape.

For example, consider a 3×3 block. Can 9 beetles cycle in a 3×3 block with alternating H and V?

A 3×3 block has 9 squares. We need a cycle of length 9 (or a set of cycles totaling 9) that alternates H and V. But a cycle alternating H and V must have even length (equal H and V steps). 9 is odd, so a single cycle of length 9 doesn't work. We could have multiple cycles, but they must sum to 9, and each must have length divisible by 4 (as I showed earlier). 9 is not divisible by 4, and 9 = 4 + 4 + 1 (but 1 doesn't work) or 9 = 4 + 5 (5 doesn't work). So we can't decompose 9 into cycle lengths divisible by 4. Hence, we can't have 9 beetles cycling in a 3×3 block.

The maximum number of beetles in a 3×3 block is 8 (two 4-cycles, covering 8 of the 9 squares). So we lose 1 square per 3×3 block.

More generally, for a m × n block, the maximum number of cycling beetles is the maximum number of squares that can be covered by cycles of lengths divisible by 4, where each cycle alternates H and V on the grid.

Each 4-cycle covers a 2×2 block (4 squares). Each 8-cycle covers 8 squares in a larger region. The question is how to tile the board with such cycles to maximize coverage.

For a 2023 × 2023 board, using 2×2 blocks, we cover 2022 × 2022 = 4,088,484 squares, leaving 4045 uncovered.

Can we do better? Let's think about using a mix of 2×2 blocks and larger cycles.

Consider a 2×3 block (6 squares). Can we find a cycle of length 6 that alternates H and V? Length 6 means 3 H and 3 V steps. But 3 is odd, so the H steps (3 values of ±1) can't sum to 0 (sum of 3 ±1's is odd). So no 6-cycle. We could use a 4-cycle (covering 4 of 6 squares), leaving 2 uncovered.

Consider a 4×4 block (16 squares). Can we find a 16-cycle? 16 = 4k with k=4. 8 H steps (summing to 0, so 4 left and 4 right) and 8 V steps (4 up and 4 down). This seems possible. For example, a "snake" cycle. But does it alternate H and V?

Actually, a cycle that alternates H and V on a grid is a cycle on the "king graph" restricted to diagonal moves... no, it's a cycle where edges alternate between horizontal and vertical grid edges. This is a cycle in the grid graph that is "properly edge-colored" with 2 colors (H and V).

A grid graph is bipartite (checkerboard coloring). The edges can be colored H and V. A cycle that alternates H and V is an "alternating cycle" in this edge-colored graph.

In a grid graph, the H edges connect (r, c) to (r, c±1), and V edges connect (r, c) to (r±1, c). An alternating cycle uses H, V, H, V, ... edges.

In a 2a × 2b grid, we can tile with 2×2 blocks, giving ab 4-cycles. But can we find larger alternating cycles?

Consider a 4×4 grid. Can we find a 16-cycle (Hamiltonian alternating cycle)? Let me try:
(0,0)→R→(0,1)→U→(1,1)→R→(1,2)→D→(0,2)→R→(0,3)→U→(1,3)→U→(2,3)→L→(2,2)→D→(1,2)... wait, (1,2) was already visited. Let me try more carefully.

Actually, this is getting very complicated. Let me think about the problem from a completely different angle.

Let me reconsider the problem. Maybe the answer is much simpler than I think.

The problem is from a competition (likely ISL 2023 or similar). The answer for such problems is often a clean expression.

Let me think about the problem in terms of "how many beetles can avoid collision."

Key observation: Consider the quantity (row + col) mod 2. As I noted, at time t, (row + col) mod 2 = (r_0 + c_0 + t) mod 2. So all beetles change their checkerboard color at each step. Two beetles starting on the same color are always on the same color; two on different colors are always on different colors. So beetles on different colors can never collide.

This gives 2 color classes. But we can do better with the 4 parity classes and the first move direction, giving 4 compatible groups.

But the real question is: within a single group, how many beetles can avoid collision?

Let me think about a single group. Say all beetles have type (0,0,H) (starting at even row, even col, first move H). At even time 2k, they're at positions with parity (k, k) mod 2. At odd time 2k+1, parity (k, k+1) mod 2.

Consider the 2-step walk: at even times, the beetles move on a sublattice. The sublattice at even time 2k has parity (k, k) mod 2. As k varies, the sublattice changes. At k=0, it's (even, even); at k=1, it's (odd, odd); at k=2, it's (even, even); etc. So the sublattice alternates between (even, even) and (odd, odd) positions.

The 2-step move: from (r, c) at time 2k, the beetle moves to (r ± 1, c ± 1) at time 2k+2. If at time 2k the beetle is at (even, even), then at time 2k+2 it's at (odd, odd) (since it moved by (±1, ±1)). Wait, but (even ± 1, even ± 1) = (odd, odd). And at time 2(k+1), the parity should be (k+1, k+1) mod 2. If k is even, k+1 is odd, so (odd, odd). ✓

So the 2-step walk alternates between the (even, even) sublattice and the (odd, odd) sublattice. The (even, even) sublattice has 1012 × 1012 points, and the (odd, odd) sublattice has 1011 × 1011 points.

Now, the 2-step walk on these sublattices: from an (even, even) point, the beetle moves to one of 4 diagonal neighbors, which are (odd, odd) points. From an (odd, odd) point, it moves to one of 4 diagonal neighbors, which are (even, even) points.

This is a bipartite walk between the two sublattices. The number of (even, even) points is 1012² and the number of (odd, odd) points is 1011².

Now, the beetles in this group are doing this 2-step walk. At even times, they alternate between the two sublattices. At time 0, they're on (even, even). At time 2, on (odd, odd). At time 4, on (even, even). Etc.

For two beetles to collide at an even time, they must be at the same point on the same sublattice at the same time. Since all beetles in the group are on the same sublattice at the same time (they all have the same parity class at each even time), collisions at even times require two beetles at the same sublattice point.

Now, the adversary controls the 2-step moves. The question is: how many beetles can the adversary keep apart on this bipartite graph?

At time 0, the beetles are on the (even, even) sublattice (1012² points). At time 2, they're on the (odd, odd) sublattice (1011² points). At time 4, back to (even, even). Etc.

The bottleneck is the (odd, odd) sublattice with only 1011² points. At time 2, all beetles must be on distinct points of the (odd, odd) sublattice. So the number of beetles is at most 1011².

Wait, but the adversary chooses the moves. At time 0, the beetles are at distinct (even, even) points. At time 2, they must be at distinct (odd, odd) points. The adversary chooses the 2-step move (which diagonal neighbor to go to). The question is: can the adversary always find an injective mapping from the (even, even) points to the (odd, odd) points such that each beetle moves to a diagonal neighbor?

This is a matching problem. Each (even, even) point has 4 diagonal neighbors (or fewer near the boundary), all of which are (odd, odd) points. We need a perfect matching from the occupied (even, even) points to the (odd, odd) points.

If we have N beetles, we need N ≤ 1011² (the number of (odd, odd) points). And we need a matching from the N occupied (even, even) points to N distinct (odd, odd) points, where each (even, even) point is matched to one of its diagonal neighbors.

By Hall's theorem, this is possible if for every subset S of occupied (even, even) points, |N(S)| ≥ |S|, where N(S) is the set of (odd, odd) points that are diagonal neighbors of some point in S.

For the full (even, even) sublattice (1012² points), the diagonal neighbors cover all (odd, odd) points (1011² points). But 1012² > 1011², so we can't match all (even, even) points to (odd, odd) points. The maximum matching from (even, even) to (odd, odd) has size 1011².

So at most 1011² beetles can be in this group (type (0,0,H)). But we also need the matching to work at every time step, not just time 0 to time 2.

At time 2, the beetles are on (odd, odd) points. At time 4, they move to (even, even) points. Each (odd, odd) point has 4 diagonal neighbors in the (even, even) sublattice. We need a matching from the 1011² occupied (odd, odd) points to 1011² distinct (even, even) points. Since there are 1012² (even, even) points, this is easier (more targets than sources).

But we also need the matching to be consistent over time. The adversary needs to find an infinite sequence of matchings such that no two beetles are ever at the same point.

This is related to the existence of a "permutation" of the sublattice points that can be maintained forever.

Actually, the 2×2 cycling strategy does exactly this. In a 2×2 block, the beetle of type (0,0,H) cycles between (0,0) and (1,1) (at even times). So it alternates between an (even, even) point and an (odd, odd) point. The matching is: (0,0) ↔ (1,1). This is a perfect matching between the (even, even) and (odd, odd) points within each 2×2 block.

With 1011 × 1011 non-overlapping 2×2 blocks (covering rows 0-2021 and cols 0-2021), each block has one (even, even) point and one (odd, odd) point. The (even, even) points in these blocks: (0,0), (2,0), (0,2), (2,2), ..., (2020, 2020). That's 1011² points. The (odd, odd) points: (1,1), (3,1), (1,3), ..., (2021, 2021). Also 1011² points.

But the (even, even) sublattice has 1012² points, including (2022, 0), (0, 2022), (2022, 2022), etc. (the L-shape (even, even) points). These are not in any 2×2 block. So we can have at most 1011² beetles of type (0,0,H) using the 2×2 cycling.

Can we have more? The (even, even) sublattice has 1012² points, but the (odd, odd) sublattice has only 1011² points. At time 2, all beetles must be on distinct (odd, odd) points, so at most 1011² beetles. This is a hard upper bound for this type.

Similarly, for type (0,1,H) (even row, odd col, first move H): at even time 2k, parity (k, k+1) mod 2. At k=0: (even, odd). At k=1: (odd, even). The (even, odd) sublattice has 1012 × 1011 points, and the (odd, even) sublattice has 1011 × 1012 points. The bottleneck is min(1012×1011, 1011×1012) = 1012 × 1011. So at most 1012 × 1011 beetles of this type.

For type (1,0,H) (odd row, even col, first move H): at k=0: (odd, even). At k=1: (even, odd). Same as above, bottleneck 1011 × 1012. So at most 1011 × 1012 beetles.

For type (1,1,H) (odd row, odd col, first move H): at k=0: (odd, odd). At k=1: (even, even). Bottleneck 1011². So at most 1011² beetles.

Total with all H types: 1011² + 1012×1011 + 1011×1012 + 1011² = 2 × 1011² + 2 × 1011 × 1012 = 2 × 1011 × (1011 + 1012) = 2 × 1011 × 2023 = 2 × 1011 × 2023.

Let me compute: 1011 × 2023 = 1011 × 2000 + 1011 × 23 = 2,022,000 + 23,253 = 2,045,253. So 2 × 2,045,253 = 4,090,506.

Hmm, but 2023² = 4,092,529. So 4,090,506 = 2023² - 2023 = 2023 × 2022 = 2023 × 2022.

Let me verify: 2023 × 2022 = 2023 × 2000 + 2023 × 22 = 4,046,000 + 44,506 = 4,090,506. ✓

And 2023² = 2023 × 2023 = 4,092,529. So 2023² - 2023 = 4,090,506. ✓

So the upper bound from the parity argument is 2023 × 2022 = 2023² - 2023.

But wait, I need to verify that this upper bound is achievable. The 2×2 cycling gives 4 × 1011² = 4 × 1,022,121 = 4,088,484 beetles. But the upper bound is 4,090,506. There's a gap of 4,090,506 - 4,088,484 = 2,022.

So the 2×2 cycling doesn't achieve the upper bound. Can we do better?

The gap comes from the L-shape. The 2×2 cycling covers 2022 × 2022 squares, but the upper bound allows 2023 × 2022 beetles. The difference is 2023 × 2022 - 2022 × 2022 = 2022 × (2023 - 2022) = 2022.

Hmm wait, let me recompute. The 2×2 cycling gives 4 × 1011² beetles. The upper bound is 2 × 1011² + 2 × 1011 × 1012. The difference is 2 × 1011 × 1012 - 2 × 1011² = 2 × 1011 × (1012 - 1011) = 2 × 1011 = 2022.

So we need to find 2022 more beetles that can avoid collision. These would come from the L-shape.

Let me think about the L-shape more carefully. The L-shape consists of:
- Row 2022: (2022, c) for c = 0, 1, ..., 2022.
- Column 2022: (r, 2022) for r = 0, 1, ..., 2021.

The 2×2 blocks cover rows 0-2021 and cols 0-2021. The L-shape is the last row and last column.

Now, the types of the L-shape squares:
- (2022, c) with c even: type (0, 0, *) since 2022 is even. Parity (0, c mod 2).
- (2022, c) with c odd: parity (0, 1).
- (r, 2022) with r even: parity (r mod 2, 0).
- (r, 2022) with r odd: parity (1, 0).

The L-shape has:
- Row 2022: 1012 even cols and 1011 odd cols.
- Col 2022: 1012 even rows (including row 2022) and 1011 odd rows. But (2022, 2022) is counted in both. So col 2022 (excluding row 2022): 1011 even rows (0, 2, ..., 2020) and 1011 odd rows (1, 3, ..., 2021).

Parity classes in the L-shape:
- (0, 0): row 2022, even cols (1012 squares) + col 2022, even rows 0-2020 (1011 squares) = 1012 + 1011 = 2023. But (2022, 2022) is in both, so 1012 + 1011 - 1 = 2022... wait, (2022, 2022) has parity (0, 0) and is in both row 2022 and col 2022. So (0,0) squares in L-shape: 1012 (from row 2022, even cols) + 1011 (from col 2022, even rows 0-2020) = 2023. But (2022, 2022) is counted once in each, so total is 1012 + 1011 = 2023. Wait, (2022, 2022) is in row 2022 (even col 2022) and also in col 2022 (even row 2022). So it's counted in both sets. So total = 1012 + 1011 - 1 = 2022.

Hmm, let me just count directly. (0,0) parity in L-shape: (2022, c) with c even: c = 0, 2, ..., 2022 → 1012 squares. (r, 2022) with r even and r < 2022: r = 0, 2, ..., 2020 → 1011 squares. Total: 1012 + 1011 = 2023. But (2022, 2022) is in both sets, so unique count = 2023 - 1 = 2022.

- (0, 1): (2022, c) with c odd: c = 1, 3, ..., 2021 → 1011 squares. (r, 2022) with r odd and r < 2022: none, since 2022 is even. Wait, (r, 2022) with r odd: parity (1, 0), not (0, 1). So (0,1) in L-shape: 1011 squares (all from row 2022, odd cols).

- (1, 0): (2022, c) with c even: parity (0, 0), not (1, 0). (r, 2022) with r odd: r = 1, 3, ..., 2021 → 1011 squares. So (1,0) in L-shape: 1011 squares.

- (1, 1): (2022, c) with c odd: parity (0, 1), not (1, 1). (r, 2022) with r odd: parity (1, 0), not (1, 1). So (1,1) in L-shape: 0 squares.

Wait, that doesn't seem right. Let me recount.

L-shape = {row 2022, all cols 0-2022} ∪ {col 2022, all rows 0-2021}.

(1,1) parity: (r, c) with r odd, c odd. In row 2022: 2022 is even, so no (1,1) squares. In col 2022 (rows 0-2021): 2022 is even, so no (1,1) squares. So indeed 0 squares of (1,1) parity in the L-shape.

So the L-shape has:
- (0,0): 2022 squares
- (0,1): 1011 squares
- (1,0): 1011 squares
- (1,1): 0 squares

Total: 2022 + 1011 + 1011 = 4044. But the L-shape has 2023 + 2022 = 4045 squares. Hmm, 4044 ≠ 4045. Let me recount.

Oh wait, I think I miscounted. Let me be more careful.

L-shape = {(2022, c) : 0 ≤ c ≤ 2022} ∪ {(r, 2022) : 0 ≤ r ≤ 2021}.

The first set has 2023 elements. The second set has 2022 elements. They're disjoint (since the first has row 2022 and the second has rows 0-2021). So total = 2023 + 2022 = 4045.

Parity (0,0): (2022, c) with c even → c = 0, 2, ..., 2022 → 1012 squares. (r, 2022) with r even → r = 0, 2, ..., 2020 → 1011 squares. Total: 1012 + 1011 = 2023.

Parity (0,1): (2022, c) with c odd → c = 1, 3, ..., 2021 → 1011 squares. (r, 2022) with r odd → r = 1, 3, ..., 2021 → 1011 squares. Total: 1011 + 1011 = 2022.

Parity (1,0): (2022, c) with c even → 2022 is even, so parity (0, 0), not (1,0). (r, 2022) with r even → 2022 is even, so parity (0, 0), not (1,0). Wait, I need (r, c) with r odd, c even. In row 2022: r = 2022 is even, so no. In col 2022: c = 2022 is even, r odd → r = 1, 3, ..., 2021 → 1011 squares. So (1,0): 1011.

Parity (1,1): r odd, c odd. In row 2022: r = 2022 is even, no. In col 2022: c = 2022 is even, no. So (1,1): 0.

Total: 2023 + 2022 + 1011 + 0 = 4056. That's more than 4045. I must be making an error.

Let me recount more carefully.

Row 2022: (2022, c) for c = 0, 1, ..., 2022. That's 2023 squares.
- c even: c = 0, 2, ..., 2022 → 1012 squares. Parity (0, 0).
- c odd: c = 1, 3, ..., 2021 → 1011 squares. Parity (0, 1).

Col 2022 (rows 0-2021): (r, 2022) for r = 0, 1, ..., 2021. That's 2022 squares.
- r even: r = 0, 2, ..., 2020 → 1011 squares. Parity (0, 0).
- r odd: r = 1, 3, ..., 2021 → 1011 squares. Parity (1, 0).

Total L-shape: 2023 + 2022 = 4045. ✓

Parity breakdown:
- (0,0): 1012 (row 2022, c even) + 1011 (col 2022, r even) = 2023.
- (0,1): 1011 (row 2022, c odd) = 1011.
- (1,0): 1011 (col 2022, r odd) = 1011.
- (1,1): 0.

Total: 2023 + 1011 + 1011 = 4045. ✓

Now, the upper bounds for each type (with first move H):
- Type (0,0,H): bottleneck sublattice is (odd, odd) with 1011² points. Max beetles: 1011².
- Type (0,1,H): bottleneck is (odd, even) with 1011 × 1012 points. Max: 1011 × 1012.
- Type (1,0,H): bottleneck is (even, odd) with 1012 × 1011 points. Max: 1012 × 1011.
- Type (1,1,H): bottleneck is (even, even) with 1012² points. Max: 1012².

Wait, I need to recompute the bottleneck for each type.

Type (
