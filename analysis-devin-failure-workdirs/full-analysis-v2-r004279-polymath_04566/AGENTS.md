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
  <problem_id>polymath_04566</problem_id>
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

Adithya and Bill are playing a game on a connected graph with $n > 2$ vertices and $m$ edges. First, Adithya labels two of the vertices $A$ and $B$, so that $A$ and $B$ are distinct and non-adjacent, and announces his choice to Bill. Then Adithya starts on vertex $A$ and Bill starts on $B$.

Now the game proceeds in a series of rounds in which both players move simultaneously. In each round, Bill must move to an adjacent vertex, while Adithya may either move to an adjacent vertex or stay at his current vertex. Adithya loses if he is ever on the same vertex as Bill, and wins if he reaches $B$ alone. Adithya cannot see where Bill is, but Bill can see where Adithya is.

Let $M(n)$ be the maximum possible value of $m$ such that Adithya has a winning strategy. Find the sum $\sum_{n=3}^{10} M(n)$.

## Standard Solution

The original solution establishes that the maximum number of edges $m$ for which Adithya has a winning strategy is $M(n) = \binom{n-1}{2} + 1$. To provide a single numeric answer, we evaluate this formula for $n=3, 4, \dots, 10$ and sum the results.
$M(3) = \binom{2}{2} + 1 = 2$
$M(4) = \binom{3}{2} + 1 = 4$
$M(5) = \binom{4}{2} + 1 = 7$
$M(6) = \binom{5}{2} + 1 = 11$
$M(7) = \binom{6}{2} + 1 = 16$
$M(8) = \binom{7}{2} + 1 = 22$
$M(9) = \binom{8}{2} + 1 = 29$
$M(10) = \binom{9}{2} + 1 = 37$
Sum = $2 + 4 + 7 + 11 + 16 + 22 + 29 + 37 = 128$.

## AI's Thinking (Attempted Solution Process)

Let me analyze this problem carefully. This is a graph theory game theory problem. Let me work through it.

The game: connected graph with n>2 vertices, m edges. Adithya labels two non-adjacent distinct vertices A and B. Adithya starts at A, Bill starts at B. Each round, both move simultaneously. Bill must move to an adjacent vertex. Adithya may move to adjacent vertex or stay. Adithya loses if on same vertex as Bill. Adithya wins if he reaches B alone. Adithya can't see Bill, Bill can see Adithya.

M(n) = maximum m such that Adithya has a winning strategy (for some choice of A, B).

We need sum from n=3 to 10 of M(n).

Let me think about this carefully.

First, Adithya can't see Bill, so Adithya's strategy must work regardless of where Bill is. Bill can see Adithya, so Bill plays optimally to catch Adithya or prevent Adithya from reaching B.

Adithya wins if he reaches B alone. So Adithya needs to get to B without Bill being there at the same time.

Since Adithya can't see Bill, his strategy is a sequence of moves (possibly adaptive based on... nothing, since he can't see Bill). Actually, Adithya's strategy is deterministic based on time only, since he has no information about Bill's position. Wait, he knows the graph and the initial setup. He knows Bill starts at B. But after that, he can't see Bill. So his strategy is a function of time only (a predetermined path, possibly with "stay" moves).

Actually, Adithya knows Bill starts at B. So Adithya knows the initial state. But after round 1, he doesn't know where Bill is. So his strategy from round 1 onward is fixed (not adaptive).

Wait, but Adithya knows Bill's strategy too (both play optimally). Actually, in game theory, Adithya chooses a strategy, Bill chooses a strategy. Adithya's strategy can depend on his own observation, which is nothing after the start. So Adithya's strategy is essentially a predetermined sequence of moves (a walk from A with possible stays).

Bill's strategy can depend on Adithya's position (since Bill can see Adithya). So Bill adaptively chases.

Adithya wins if at some round, Adithya is at B and Bill is not at B.

Adithya loses if at some round, they're on the same vertex.

Let me think about when Adithya can win.

Key insight: Adithya needs to reach B. Bill starts at B. Bill must move each round (can't stay). So after round 1, Bill leaves B. If Adithya can reach B at some round when Bill is not there, Adithya wins.

But Bill can see Adithya and will try to either catch Adithya or be at B when Adithya arrives.

Let me think about small cases.

n=3: Connected graph with 3 vertices. Max edges for a simple graph on 3 vertices is 3 (triangle). But A and B must be non-adjacent. In a triangle, every pair is adjacent, so no valid A,B. So we need a graph where there exist two non-adjacent vertices. With 3 vertices, the path graph P3 has 2 edges. The only connected graphs on 3 vertices: P3 (2 edges) and K3 (3 edges). K3 has no non-adjacent pair. So for n=3, the graph must be P3 (path of length 2), with 2 edges. Actually, we need A,B non-adjacent. In P3, vertices 1-2-3. Non-adjacent pair: {1,3}. So A=1, B=3 (or vice versa). 

Let me set up: A=1, B=3, middle vertex 2. Adithya at 1, Bill at 3.

Round 1: Bill must move from 3, so Bill goes to 2. Adithya can stay at 1 or move to 2. If Adithya moves to 2, they collide (both at 2), Adithya loses. So Adithya stays at 1.

Round 2: Bill is at 2, must move. Bill can go to 1 or 3. Bill sees Adithya at 1. If Bill goes to 1, they collide, Adithya loses. So Bill goes to 1 and catches Adithya. 

Hmm, so Adithya loses. Let me reconsider.

Round 2: Bill at 2, Adithya at 1. Bill must move. Bill can go to 1 (catches Adithya) or 3. Bill wants to catch Adithya, so Bill goes to 1. Adithya loses.

What if Adithya moves to 2 in round 2? Then Bill at 2 moves... wait, they move simultaneously. In round 2, Adithya moves from 1 to 2, Bill moves from 2 to 1. They swap - they're not on the same vertex. Adithya is at 2, Bill is at 1. No collision!

Round 3: Adithya at 2, Bill at 1. Bill must move from 1, only option is 2. Adithya can move to 1 or 3 or stay at 2. If Adithya moves to 3, Bill moves to 2. Adithya at 3 = B, Bill at 2. Adithya wins!

But wait, Bill can see Adithya. In round 3, Bill sees Adithya at 2. Bill knows Adithya might go to 3. Bill must move from 1 to 2 (only option). So Bill goes to 2. Adithya goes to 3. Adithya is at B alone. Win!

But actually, Bill sees Adithya at 2 in round 3. Bill must move to 2 (only neighbor of 1). Adithya moves to 3. They're at different vertices. Adithya at B. Win!

But wait, could Bill have played differently in round 2? In round 2, Bill at 2, sees Adithya at 1. Bill can go to 1 or 3. If Bill goes to 3: Adithya moves to 2. Adithya at 2, Bill at 3. Round 3: Bill at 3 must move to 2. Adithya at 2 can move to 3 or stay or go to 1. If Adithya goes to 3: Bill goes to 2. Adithya at 3 = B, Bill at 2. Win! If Adithya stays at 2: Bill goes to 2, collision. So Adithya goes to 3. Win!

So regardless of Bill's move in round 2, Adithya wins by going to 2 in round 2 and then to 3 in round 3.

Wait, but I need to check: does Bill see Adithya's move in round 2 before moving? No, they move simultaneously. Bill sees Adithya's position at the start of the round.

Let me redo this more carefully.

Initial: A=1, B=3. Adithya at 1, Bill at 3.

Adithya's strategy: Round 1: stay at 1. Round 2: move to 2. Round 3: move to 3.

Round 1: Adithya stays at 1. Bill must move from 3 → 2. State: A=1, B=2.
Round 2: Adithya moves 1→2. Bill must move from 2. Bill sees Adithya at 1 (start of round). Bill can go to 1 or 3.
  - If Bill goes to 1: A=2, B=1. No collision.
  - If Bill goes to 3: A=2, B=3. No collision.
Round 3: Adithya moves 2→3. Bill must move.
  - If B was at 1: Bill moves 1→2. A=3, B=2. Adithya at B alone. Win!
  - If B was at 3: Bill moves 3→2. A=3, B=2. Adithya at B alone. Win!

So Adithya wins on P3. So M(3) = 2.

Wait, but could there be a graph on 3 vertices with more edges? The max is 3 (triangle), but triangle has no non-adjacent pair. So M(3) = 2.

Hmm wait, actually I need to reconsider. The problem says "Adithya labels two of the vertices A and B, so that A and B are distinct and non-adjacent." So Adithya gets to choose which vertices are A and B. And M(n) is the max m such that Adithya has a winning strategy. So Adithya chooses the graph? No - "a connected graph with n vertices and m edges." The graph is given, and Adithya labels A and B.

Actually, re-reading: "M(n) be the maximum possible value of m such that Adithya has a winning strategy." So we're looking for the maximum m such that there EXISTS a connected graph with n vertices and m edges where Adithya can choose A, B (non-adjacent) and has a winning strategy.

So M(n) = max m such that ∃ connected graph G with n vertices, m edges, and ∃ non-adjacent A, B in G such that Adithya wins the game on G with these A, B.

For n=3: The only connected graphs are P3 (2 edges) and K3 (3 edges). K3 has no non-adjacent pair, so invalid. P3 has 2 edges, and we showed Adithya wins. So M(3) = 2.

Now let me think about the general structure.

Key observations:
1. Bill must move every round (can't stay).
2. Adithya can stay or move.
3. Adithya can't see Bill, so his strategy is predetermined (a walk from A with possible stays).
4. Bill can see Adithya and adaptively chases.
5. Adithya wins by reaching B when Bill isn't there.

Since Adithya's strategy is predetermined, Bill knows Adithya's entire path. Bill can then optimally choose his path to either intercept Adithya or guard B.

So the question becomes: does there exist a walk W from A to B (with possible stays) such that for every walk V that Bill takes (starting at B, moving each step), at no point are they at the same vertex, and at some point Adithya is at B while Bill is not at B?

Since Bill knows Adithya's strategy (and can see Adithya), Bill will play optimally. So Adithya needs a walk that beats all possible Bill walks.

Actually, since Bill can see Adithya, Bill's strategy is adaptive. But since Adithya's strategy is predetermined, Bill effectively knows Adithya's entire path in advance. So Bill can plan his optimal response.

Let me think about this differently. Adithya commits to a path (walk with stays). Bill, knowing this path, chooses his path to either catch Adithya or be at B when Adithya arrives.

Adithya wins if: there's a walk W = (w_0=A, w_1, w_2, ..., w_T=B) such that for every valid Bill walk V = (v_0=B, v_1, v_2, ..., v_T) (where each v_{i+1} is adjacent to v_i), we have:
- w_i ≠ v_i for all i (no collision)
- w_T = B and v_T ≠ B (Adithya reaches B alone)

Actually, Adithya might reach B at some step t ≤ T and win immediately. Let me say Adithya wins at step t if w_t = B and v_t ≠ B, and for all i < t, w_i ≠ v_i.

So Adithya needs: ∃ walk W from A to B, and ∃ step t with w_t = B, such that for all Bill walks V, either (a) they collide at some step before t (Bill wins), or (b) v_t ≠ B (Adithya wins). Wait no, Adithya needs to AVOID collision and reach B alone. So:

Adithya wins with walk W at step t if: for all Bill walks V, w_i ≠ v_i for all i ≤ t, and v_t ≠ B.

Hmm, but Bill is adversarial. Bill will try to either collide with Adithya or be at B at step t. So Adithya wins if: for all Bill walks V, (w_i ≠ v_i for all i ≤ t) AND (v_t ≠ B).

Equivalently, Adithya wins if there's NO Bill walk V that either (collides with Adithya at some step ≤ t) OR (is at B at step t).

Wait, that's not right either. If Bill collides with Adithya, Adithya loses. If Bill is at B at step t, Adithya doesn't win (he's at B but not alone). So Adithya needs: for all Bill walks V, w_i ≠ v_i for all i ≤ t AND v_t ≠ B. This means no Bill walk can collide with Adithya's path up to step t, and no Bill walk can be at B at step t.

The second condition: no Bill walk can be at B at step t. Bill starts at B and must move each step. So Bill is at B at step t iff there's a walk from B back to B of length t. This is possible iff B is in a cycle of length dividing t, or more generally, iff there's a closed walk of length t from B.

The first condition: no Bill walk can be at w_i at step i for any i ≤ t. This means for each i, w_i is not reachable from B in exactly i steps. Actually, it means there's no walk V from B such that v_i = w_i for some i ≤ t.

This is complex. Let me think about specific graph structures.

Let me think about what graphs give Adithya the best chance. Adithya wants a graph where:
1. He can reach B without Bill being able to intercept.
2. Bill can't be at B when Adithya arrives.

Since Bill must move every round, if the graph is bipartite, Bill's position alternates between the two parts. If B is in part X, Bill is in part X on even rounds and part Y on odd rounds.

Similarly, Adithya can stay, so he has more flexibility.

Let me think about a specific useful structure. Consider a graph that is a path: A - v1 - v2 - ... - vk - B. This is a path of length k+1 (k+2 vertices). But this uses only k+2 vertices. For n vertices, we'd have extra vertices.

Actually, let me think about what structure maximizes edges while keeping Adithya winning.

Let me think about the problem from the perspective of: what's the maximum number of edges in a connected graph on n vertices where Adithya can win?

Let me think about when Adithya CAN'T win. If the graph is too connected, Bill can always intercept or guard B.

Let me think about the path graph. Path A - ... - B with n vertices, n-1 edges. Does Adithya win?

On a path, the distance from A to B is n-1. Adithya needs to walk from A to B. Bill starts at B.

Let's say the path is 1-2-3-...-n, with A=1, B=n.

Adithya's strategy: walk toward B, possibly with stays.

Bill's strategy: Bill must move each round. On a path, Bill's options are limited.

Let me think about a path of length d (d+1 vertices, but let's use general path).

Actually, let me think about the parity. On a path 1-2-...-n, the graph is bipartite. Say odd vertices are in part X, even in part Y. B = n. If n is odd, B is in part X. Bill starts at B (part X). After 1 move, Bill is in part Y. After 2 moves, part X. Etc. So Bill is in part X on even steps, part Y on odd steps.

Adithya starts at A=1 (part X, if 1 is odd... well 1 is in the same part as vertices of the same parity as 1). Let me use the coloring: vertex i has color i mod 2. So color 1 = odd, color 0 = even. A=1 has color 1, B=n has color n mod 2.

Adithya can stay, so he can control his parity. If Adithya stays at even steps and moves at odd steps, or various combinations.

Let me think about a specific example. Path 1-2-3-4 (n=4, A=1, B=4).

Distance from A to B is 3. Adithya needs at least 3 moves to reach B. But he can also stay.

Bill starts at 4. Let's see what happens.

Adithya's strategy: Let's try to just walk: 1→2→3→4 (3 steps).

Step 1: A: 1→2. Bill: 4→3 (must move, only option is 3). State: A=2, B=3. No collision.
Step 2: A: 2→3. Bill: 3→? Bill sees A at 2. Bill can go to 2 or 4. If Bill goes to 2: A=3, B=2. If Bill goes to 4: A=3, B=4.
  - If B=2: Step 3: A: 3→4. Bill: 2→3 (only option, since 1 is not adjacent... wait, 2 is adjacent to 1 and 3). Bill can go to 1 or 3. Bill sees A at 3. If Bill goes to 3: collision! A=4? No wait, simultaneous. A moves 3→4, Bill moves 2→3. A=4, B=3. No collision. A at B alone. Win!
  - If B=4: Step 3: A: 3→4. Bill: 4→3. A=4, B=3. A at B alone. Win!

Wait, but in step 2, if Bill goes to 2, then in step 3, Bill at 2 can go to 1 or 3. Bill sees A at 3. If Bill goes to 3 and A goes to 4, they don't collide (A at 4, B at 3). But what if Bill goes to 3 and A is at 3? No, A moves from 3 to 4 simultaneously. So A=4, B=3. No collision. Adithya at B. Win!

Hmm, but what if Bill anticipates and tries to collide? In step 2, Bill at 3 sees A at 2. Bill can go to 2 or 4. If Bill goes to 2, A goes to 3. No collision. If Bill goes to 4, A goes to 3. No collision. In step 3, A goes to 4. Bill at 2 goes to 1 or 3; Bill at 4 goes to 3. Either way, A=4, B≠4. Win!

So on path 1-2-3-4, Adithya wins with the simple walk. 

But wait, I should check: can Bill intercept in step 2? Bill at 3, A at 2. If A moves to 3 and Bill stays... but Bill can't stay! Bill must move. So Bill leaves 3, and A arrives at 3. They don't collide because Bill left. This is the key insight: on a path, when Adithya is moving toward B and Bill is between A and B, Bill must move. If Bill moves toward A, they might swap (no collision). If Bill moves toward B, Adithya follows.

Actually, the critical thing is: can Bill ever be at the same vertex as Adithya? On a path, if Adithya is at position i and Bill is at position j > i (between A and B), and Adithya moves right while Bill moves left, they could collide if |i-j| = 1 and they both move toward each other. But they move simultaneously, so if A at i moves to i+1 and B at i+1 moves to i, they swap - no collision. If A at i moves to i+1 and B at i+1 moves to i+2, then A=i+1, B=i+2, no collision. If A at i stays and B at i+1 moves to i, collision!

So the danger is when Adithya stays and Bill moves onto Adithya's position.

On a path, if Adithya keeps moving toward B, and Bill is ahead of Adithya, Bill must move. If Bill moves toward Adithya, they swap (no collision since simultaneous). If Bill moves away, Adithya gains ground. So Adithya can always advance toward B without collision, as long as he doesn't stay when Bill is adjacent and can move onto him.

Wait, but what if Bill is behind Adithya? Then Bill could catch up. But on a path, if Adithya is moving toward B and Bill is behind, Bill can only move one step per round, same as Adithya. So Bill can't catch up if Adithya keeps moving.

Hmm, but Bill could also be at B and move away, then come back. Let me think more carefully.

On a path 1-2-...-n, A=1, B=n. Let's say Adithya just walks 1→2→...→n without staying. This takes n-1 steps.

At each step, Adithya is at position i+1 (after step i). Bill starts at n and must move each step.

The question is: can Bill ever be at the same position as Adithya at the same step?

At step i, Adithya is at position i+1. Bill is at some position reachable from n in i steps on the path.

Bill's position at step i is n - i + 2k for some k (Bill moves back and forth). Actually, on a path, Bill's position at step i has the same parity as n + i (since each move changes parity). Adithya's position at step i is i+1, which has parity i+1.

Collision at step i: Adithya at i+1, Bill at some position with parity n+i. For collision, i+1 ≡ n+i (mod 2), so 1 ≡ n (mod 2), i.e., n is odd.

So if n is even, Adithya and Bill always have different parities, so they can never be at the same position! Adithya just walks to B and wins.

If n is odd, they could potentially collide. Let me check.

For n odd, path 1-2-...-n. Adithya walks 1→2→...→n. At step i, Adithya at i+1. Bill at n, must move. Bill's position at step i has parity (n+i) mod 2 = (1+i) mod 2 (since n odd) = (i+1) mod 2. Adithya at i+1, parity (i+1) mod 2. Same parity! So collision is possible.

Can Bill actually collide? Bill needs to be at position i+1 at step i. Bill starts at n. Distance from n to i+1 is n - (i+1) = n - i - 1. Bill has i steps. So Bill can reach i+1 iff n - i - 1 ≤ i and (n - i - 1) ≡ i (mod 2) [same parity]. The parity: n - i - 1 and i. n - i - 1 ≡ i (mod 2) iff n - 1 ≡ 0 (mod 2) iff n is odd. Yes, so for n odd, Bill can reach Adithya's position if n - i - 1 ≤ i, i.e., i ≥ (n-1)/2.

So for n odd, at step i = (n-1)/2, Bill can be at position (n-1)/2 + 1 = (n+1)/2. This is the midpoint. Bill can reach there from n in (n-1)/2 steps (distance is n - (n+1)/2 = (n-1)/2). So yes, Bill can collide at the midpoint.

So for odd n, the simple walk doesn't work. Adithya needs a different strategy.

For odd n, Adithya could add a stay. For example, stay at A for one round, then walk. This shifts the parity.

If Adithya stays at 1 for step 1, then walks 1→2→...→n starting from step 2. At step i (for i ≥ 2), Adithya is at position i (since he started walking at step 2, at step 2 he's at 2, at step 3 at 3, etc.). Wait, let me re-index.

Step 1: Adithya stays at 1. Bill moves from n to n-1.
Step 2: Adithya moves 1→2. Bill moves from n-1.
...
Step k (k ≥ 2): Adithya at position k. Bill at some position.

At step k, Adithya at position k (for k ≥ 2, and at step 1, Adithya at 1). Bill's parity at step k: (n + k) mod 2. Adithya's parity: k mod 2. Collision possible when n + k ≡ k (mod 2), i.e., n ≡ 0 (mod 2). But n is odd, so n + k ≡ k + 1 (mod 2) ≠ k (mod 2). So no collision possible!

Wait, that's great. So for odd n, if Adithya stays one round first, then walks, the parities never match, so no collision. But we need to check: does Adithya reach B?

Adithya stays at 1 (step 1), then walks 1→2→...→n. He reaches n at step n. At step n, Adithya at n = B. Bill's parity at step n: (n + n) mod 2 = 0. Adithya at n, parity n mod 2 = 1 (n odd). So Bill can't be at n (different parity). So Adithya is at B alone. Win!

But wait, we also need to check that Bill doesn't collide at step 1. At step 1, Adithya at 1, Bill at n-1 (moved from n). Since n > 2, n-1 ≥ 2 > 1, so no collision (unless n = 2, but n > 2). Actually for n=3: Bill at 2, Adithya at 1. No collision. Good.

So on any path graph 1-2-...-n with A=1, B=n, Adithya wins:
- If n even: walk directly (n-1 steps).
- If n odd: stay 1 round, then walk (n steps).

Great, so paths always work. M(n) ≥ n-1.

Now, can we do better than n-1 edges? Can we add edges to the path while keeping Adithya winning?

The key constraint is that A and B must be non-adjacent. And the graph must remain such that Adithya can win.

Let me think about what edges we can add.

The danger of adding edges is that it gives Bill more mobility, making it easier for Bill to intercept Adithya or guard B.

Let me think about this more carefully. Adithya's strategy is a predetermined walk. Bill, knowing this walk, tries to intercept or guard B.

Let me think about the concept of "Adithya-safe" graphs.

Actually, let me think about this problem differently. Let me consider what happens with various graph structures.

Key insight: Adithya can't see Bill, so his strategy is a fixed walk. Bill knows this walk and can optimally respond. So Adithya wins iff there exists a walk W from A to B such that no Bill walk can intercept W or be at B when W arrives at B.

Let me think about when Bill can intercept. Bill can intercept at step i if Bill can reach w_i in exactly i steps from B. Bill can guard B at step t if Bill can reach B in exactly t steps from B (a closed walk of length t).

So Adithya wins with walk W arriving at B at step t iff:
1. For all i ≤ t, w_i is not reachable from B in exactly i steps. (No interception)
2. B is not reachable from B in exactly t steps. (No guarding, i.e., no closed walk of length t from B)

Condition 2: No closed walk of length t from B. This means B is not in any cycle whose length divides t... actually, it's about closed walks, not just cycles. A closed walk of length t from B exists iff B is in a cycle of length dividing t, or more generally, iff there's a walk from B to B of length t.

In a bipartite graph, closed walks from any vertex have even length. So if t is odd, condition 2 is automatically satisfied in a bipartite graph.

Condition 1: w_i not reachable from B in i steps. This is about the distance and parity.

Let me think about bipartite graphs. If the graph is bipartite with parts X and Y, and B is in part X, then:
- Bill is in part X at even steps, part Y at odd steps.
- If Adithya is in part Y at step i (odd i), and Bill is in part X (even i)... wait, let me be more careful.

If B ∈ X, then at step i, Bill is in X if i is even, Y if i is odd.
If A ∈ Y (A and B non-adjacent, could be same or different part), and Adithya moves to a new vertex each step, Adithya alternates parts. But Adithya can stay, which keeps him in the same part.

If Adithya is in part Y at step i where i is even, then Bill is in part X (even step), so they can't collide. If Adithya is in part X at step i where i is even, they could collide.

So if Adithya arranges to always be in the opposite part from Bill, no collision. Bill is in X at even steps, Y at odd steps. So Adithya should be in Y at even steps, X at odd steps. This means Adithya changes part each step (moves each step). Starting from A:
- If A ∈ Y: step 0 (even) in Y ✓, step 1 (odd) in X ✓, step 2 (even) in Y ✓, etc. So Adithya just moves each step.
- If A ∈ X: step 0 (even) in X ✗ (Bill in X). So Adithya should stay at step 1 (stay in X, but now step 1 is odd, Bill in Y, Adithya in X, different ✓). Then step 2 (even, Bill in X), Adithya moves to Y ✓. Etc.

Wait, I need to be more careful. Let me re-do.

B ∈ X. Bill at step i: X if i even, Y if i odd.
Adithya at step i: we want Adithya in Y if i even, in X if i odd (opposite of Bill).

If A ∈ Y: Adithya starts in Y (step 0, even) ✓. Move to X (step 1, odd) ✓. Move to Y (step 2, even) ✓. So Adithya moves every step. He alternates Y, X, Y, X, ... He reaches B ∈ X at some odd step. At that odd step, Bill is in Y, so Bill is not at B (B ∈ X). Adithya wins!

But we need Adithya to actually reach B. The distance from A to B is some d. If A ∈ Y and B ∈ X, then d is odd. Adithya reaches B at step d (odd). Bill is in Y at odd steps, B ∈ X, so Bill not at B. ✓

If A ∈ X and B ∈ X (same part, non-adjacent): d is even. Adithya starts in X (step 0, even). Bill in X (step 0). But step 0 is the initial state, they're at A and B which are different, so no collision. At step 1 (odd), Adithya should be in X (to be opposite Bill who is in Y). But if Adithya moves, he goes to Y. So Adithya should stay at step 1 (stay in X). Then at step 2 (even), Adithya moves to Y (opposite Bill in X). At step 3 (odd), Adithya in X (opposite Bill in Y). Etc.

So Adithya stays at step 1, then moves every step. He reaches B at step 1 + d (since he wastes one step). d is even, so 1 + d is odd. At odd step, Bill in Y, B ∈ X, Bill not at B. ✓

If A ∈ Y and B ∈ Y (same part): d is even. Adithya starts in Y (step 0, even). Bill in X (step 0). OK. Adithya should be in Y at even steps, X at odd steps. So Adithya moves every step: Y, X, Y, X, ... He reaches B ∈ Y at step d (even). At even step, Bill in X, B ∈ Y, Bill not at B. ✓

If A ∈ X and B ∈ Y: d is odd. Adithya starts in X (step 0, even). Bill in X (step 0). Different vertices, OK. Adithya should be in Y at even, X at odd. But Adithya starts in X at step 0 (even) - same part as Bill. At step 1, Adithya should be in X (odd step, opposite Bill in Y). If Adithya stays, he's in X ✓. Then at step 2, move to Y ✓. Reaches B ∈ Y at step 1 + d (even). At even step, Bill in X, B ∈ Y, Bill not at B. ✓

So in ALL cases with a bipartite graph, Adithya can win by choosing the right parity strategy (possibly staying one round first). The key requirement is that A and B are non-adjacent (so d ≥ 2) and the graph is bipartite.

Wait, but I also need to verify that Adithya can actually follow a path of the right length. Since the graph is connected, there's a path from A to B. Adithya follows this path (with possibly one initial stay). The path has length d. Adithya reaches B at step d or d+1. The parity works out as shown above.

But I also need to make sure that at every intermediate step, Adithya's position is not reachable by Bill. In a bipartite graph, if Adithya is always in the opposite part from Bill, they can never be at the same vertex (since same vertex would mean same part). So condition 1 is automatically satisfied!

So: **In any bipartite graph with non-adjacent A, B, Adithya wins.**

This is a huge insight. So M(n) is at least the maximum number of edges in a connected bipartite graph on n vertices with at least one non-adjacent pair.

The maximum number of edges in a bipartite graph on n vertices is ⌊n²/4⌋ (complete bipartite graph K_{⌊n/2⌋, ⌈n/2⌉}).

But we need A, B non-adjacent. In K_{a,b} with a, b ≥ 2, any two vertices in the same part are non-adjacent. So we can always find non-adjacent A, B (as long as one part has ≥ 2 vertices, which happens when n ≥ 3).

Wait, but we also need the graph to be connected. K_{a,b} is connected if a, b ≥ 1. And we need a non-adjacent pair, which requires max(a,b) ≥ 2, i.e., n ≥ 3.

So for n ≥ 3, the complete bipartite graph K_{⌊n/2⌋, ⌈n/2⌉} has ⌊n²/4⌋ edges, is connected, bipartite, and has non-adjacent pairs. Adithya wins on this graph. So M(n) ≥ ⌊n²/4⌋.

But can we do better? Can we have a non-bipartite graph where Adithya still wins?

If the graph is non-bipartite, it has an odd cycle. Then there exist closed walks of both parities from any vertex (eventually). This makes it harder for Adithya.

Let me think about whether Adithya can win on a non-bipartite graph.

In a non-bipartite graph, there's an odd cycle. Bill can use the odd cycle to change parity, potentially allowing him to reach Adithya's position or guard B.

Let me think about a specific example. Take K_{⌊n/2⌋, ⌈n/2⌉} and add one edge within a part. This creates an odd cycle. Can Adithya still win?

Let me try n=4. K_{2,2} has 4 edges and is bipartite (it's C4). M(4) ≥ 4. Can we get 5 edges? The maximum edges on 4 vertices is 6 (K4). K4 minus one edge has 5 edges. Is K4 minus one edge non-bipartite? K4 has triangles, so K4 minus one edge still has triangles (unless we remove edges to break all triangles, but removing one edge from K4 leaves 5 edges and still has triangles). So K4 - e is non-bipartite.

Can Adithya win on K4 - e? Let's say K4 with vertices 1,2,3,4 and missing edge (1,2). So edges: 13, 14, 23, 24, 34. Non-adjacent pair: {1,2}. A=1, B=2.

Adithya at 1, Bill at 2. Adithya needs to reach 2.

The graph: 1 is connected to 3, 4. 2 is connected to 3, 4. 3 is connected to 1, 2, 4. 4 is connected to 1, 2, 3.

Distance from 1 to 2 is 2 (via 3 or 4).

Adithya's strategy: He needs to get to 2. Let's try: stay at 1 (step 1), then go 1→3→2 or 1→4→2.

Step 1: Adithya stays at 1. Bill must move from 2. Bill can go to 3 or 4.
Step 2: Adithya moves 1→3 (or 1→4). Bill moves from 3 or 4.

Case: Bill went to 3 in step 1. Step 2: Adithya moves 1→3. But Bill is at 3 and must move. Bill sees Adithya at 1 (start of step 2). Bill can go to 1, 2, or 4. If Bill goes to 1: A=3, B=1. If Bill goes to 2: A=3, B=2. If Bill goes to 4: A=3, B=4.

Wait, but Bill sees Adithya at 1 at the start of step 2. Bill knows Adithya's strategy (stay then move). So Bill knows Adithya will move to 3 or 4 in step 2. But Bill doesn't know which one (Adithya's strategy is fixed, so Bill knows which one). Let's say Adithya's strategy is: stay, then 1→3, then 3→2.

Bill knows this. So in step 1, Bill moves from 2. In step 2, Adithya goes to 3. Bill wants to be at 3 at step 2 or at 2 at step 3.

Step 1: Bill at 2, moves to 3 or 4.
Step 2: Adithya at 3. Bill at (3 or 4) moves.
  If Bill was at 3: Bill must move. Bill can go to 1, 2, or 4. To collide with Adithya at 3... but Bill must leave 3, and Adithya arrives at 3. They're not at 3 simultaneously (Bill leaves, Adithya arrives). Wait, no - they move simultaneously. At the start of step 2, Bill is at 3 and Adithya is at 1. They both move. Bill moves from 3 to somewhere, Adithya moves from 1 to 3. After the move, Adithya is at 3, Bill is elsewhere. No collision (they were at different vertices at the start, and they end at different vertices unless Bill moves to 3... but Bill is leaving 3).

Actually, collision happens if they end up at the same vertex after the move, OR if they're at the same vertex at any point. I think collision means they're at the same vertex after the simultaneous move (i.e., at the same step). Let me re-read the problem.

"Adithya loses if he is ever on the same vertex as Bill"

I think this means at any point in time (after each round's simultaneous move). So after each round, we check if they're at the same vertex.

So at step 2: Adithya at 3, Bill at (wherever Bill moved). If Bill was at 3 and moved to 1, 2, or 4, then Bill is not at 3. No collision. If Bill was at 4 and moved to 3, then Bill is at 3 and Adithya is at 3. Collision!

So if Bill went to 4 in step 1, and then to 3 in step 2, collision! Bill can do this: 2→4→3. And Adithya is at 3 at step 2. Collision.

So Adithya's strategy of stay→3→2 doesn't work because Bill can go 2→4→3 and collide at step 2.

What if Adithya tries stay→4→2? Then Bill can go 2→3→4 and collide at step 2.

What if Adithya tries a longer path? Like stay, 1→3, 3→4, 4→2 (4 steps)?

Step 1: Adithya at 1. Bill at 2 → 3 or 4.
Step 2: Adithya at 3. Bill at 3 or 4 → ?
Step 3: Adithya at 4. Bill at ?
Step 4: Adithya at 2. Bill at ?

Bill wants to collide at some step or be at 2 at step 4.

Let me check if Bill can collide. Bill knows Adithya's path: 1, 1, 3, 4, 2 (steps 0-4).

Step 0: A=1, B=2.
Step 1: A=1, B=? (from 2, go to 3 or 4)
Step 2: A=3, B=? 
Step 3: A=4, B=?
Step 4: A=2, B=?

Bill needs to be at 1 at step 1, or 3 at step 2, or 4 at step 3, or 2 at step 4.

Can Bill be at 1 at step 1? From 2, distance to 1 is 2 (2→3→1 or 2→4→1). But Bill has only 1 step. So no.

Can Bill be at 3 at step 2? From 2, reach 3 in 2 steps: 2→3→? No, 2→4→3 or 2→3→(somewhere). 2→4→3 works (2 steps). So Bill can be at 3 at step 2. Collision!

So this doesn't work either. Bill can always reach Adithya's position at step 2 (since the graph is highly connected).

Hmm, what about a longer strategy with more stays?

Adithya: stay, stay, 1→3, 3→4, 4→2 (steps: 1,1,1,3,4,2)

Step 0: A=1, B=2.
Step 1: A=1, B=3 or 4.
Step 2: A=1, B=?
Step 3: A=3, B=?
Step 4: A=4, B=?
Step 5: A=2, B=?

Bill needs to be at 1 at step 1 or 2, or 3 at step 3, or 4 at step 4, or 2 at step 5.

Can Bill be at 1 at step 1? From 2, 1 step: 2→3 or 2→4. Not 1. No.
Can Bill be at 1 at step 2? From 2, 2 steps: 2→3→1 or 2→4→1. Yes! Bill can be at 1 at step 2. Collision!

So Bill can reach 1 in 2 steps. Adithya is at 1 at step 2. Collision.

What if Adithya stays for 3 steps? stay, stay, stay, 1→3, 3→4, 4→2.

Step 3: A=3. Can Bill reach 3 in 3 steps from 2? 2→3→4→3 (3 steps). Yes. Collision.

It seems like on this graph (K4 - e), Bill can always reach Adithya's position because the graph is so connected. The diameter is 2, and Bill can reach any vertex in at most 2 steps. Since Adithya's path visits intermediate vertices, Bill can always get there.

Actually, let me think about this more carefully. The graph K4 - e has diameter 2. Bill can reach any vertex in at most 2 steps. Adithya's walk has length at least 2 (distance from 1 to 2 is 2). At each intermediate step, Adithya is at some vertex, and Bill can reach that vertex in at most 2 steps. But the timing needs to work out.

Let me think about it differently. Adithya's walk is w_0, w_1, ..., w_T where w_0 = 1, w_T = 2. Bill can collide if for some i, Bill can reach w_i in exactly i steps from 2.

The set of vertices reachable from 2 in exactly i steps: since the graph has diameter 2 and is non-bipartite (has odd cycles), for i ≥ 2, Bill can reach any vertex. (In a non-bipartite graph with diameter d, for sufficiently large i, all vertices are reachable in exactly i steps. Here, for i ≥ 2, I think all vertices are reachable.)

Let me verify: from vertex 2 in K4 - e (edges: 13, 14, 23, 24, 34):
- 1 step: {3, 4}
- 2 steps: from 3: {1, 2, 4}; from 4: {1, 2, 3}. Union: {1, 2, 3, 4}. All vertices!
- 3 steps: from any vertex, 1 step reaches {3, 4} or {1, 2, 3} etc. Since 2 steps reaches all, 3 steps also reaches all (just go to some vertex in 2 steps, then take 1 more step... but need exactly 3 steps). From 2, 2 steps reaches all vertices. From any vertex v, 1 step reaches some vertex. So 3 steps from 2 = 2 steps from 2 then 1 more step = reach any vertex in 2 steps, then 1 more step. But we need exactly 3 steps. From 2, reach v in 2 steps, then move to a neighbor of v. Since every vertex has at least 2 neighbors, we can reach any vertex that's a neighbor of some vertex. Actually, since 2 steps reaches all vertices, and from any vertex we can move to a neighbor, 3 steps reaches all vertices that have a neighbor... which is all vertices. So 3 steps reaches all vertices.

So for i ≥ 2, Bill can reach any vertex in exactly i steps. This means Bill can collide with Adithya at any step i ≥ 2 where Adithya is at any vertex. The only safe steps are i = 0 (initial, different vertices) and i = 1.

At step 1, Adithya is at w_1. Bill can reach {3, 4} in 1 step from 2. So if w_1 ∈ {3, 4}, Bill can collide. If w_1 = 1 (Adithya stays), Bill can't reach 1 in 1 step. So Adithya must stay at step 1.

At step 2, Adithya is at w_2. Bill can reach any vertex in 2 steps. So Bill can collide regardless of w_2. 

So Adithya can't survive past step 2 on K4 - e. Since Adithya needs at least 2 steps to reach B (distance 2), and he can't survive step 2, he can't win. (He could stay at step 1, but then he needs to reach B in steps 2+, and step 2 is fatal.)

Wait, Adithya could stay at step 1 and step 2. Then at step 2, Adithya is at 1. Bill can reach 1 in 2 steps (2→3→1). Collision. So even staying doesn't help.

What if Adithya stays for many steps? At step i, Adithya at 1, Bill can reach 1 in i steps for i ≥ 2. So Bill collides at step 2. 

So on K4 - e, Adithya cannot win. This means M(4) = 4 (the bipartite maximum), not 5.

Hmm wait, but maybe there's a different non-bipartite graph on 4 vertices with 5 edges where Adithya can win? The only graph on 4 vertices with 5 edges is K4 - e (up to isomorphism). So M(4) = 4.

Actually wait, I should double-check. Is there a graph on 4 vertices with 5 edges that's bipartite? A bipartite graph on 4 vertices has at most ⌊16/4⌋ = 4 edges (K_{2,2}). So 5 edges forces non-bipartite. And we showed K4 - e doesn't work. So M(4) = 4.

Let me now think about the general principle. 

Claim: Adithya wins if and only if the graph is bipartite (with appropriate A, B).

Wait, that's not quite right. Adithya gets to choose A and B. And the graph is given. M(n) is the max m such that there EXISTS a graph with n vertices and m edges where Adithya can win.

I showed:
1. If the graph is bipartite and has non-adjacent A, B, Adithya wins.
2. On K4 - e (non-bipartite, 5 edges, n=4), Adithya can't win.

But maybe there are some non-bipartite graphs where Adithya can still win? Let me think about this.

Consider a graph that is "almost bipartite" - bipartite plus one edge. The one extra edge creates an odd cycle. Can Adithya still win?

Let me think about a specific case. Take C4 (cycle on 4 vertices: 1-2-3-4-1) which is bipartite with 4 edges. Add edge (1,3) to make it non-bipartite (creates triangle 1-2-3 and triangle 1-3-4). Now 5 edges. Non-adjacent pairs: {2,4} (and {1,3} are now adjacent). So A=2, B=4.

Graph: 1-2, 2-3, 3-4, 4-1, 1-3. Vertices: 1,2,3,4. A=2, B=4.

Distance from 2 to 4: 2→1→4 (length 2) or 2→3→4 (length 2). Diameter is 2.

From B=4, reachable in:
- 1 step: {1, 3}
- 2 steps: from 1: {2, 3, 4}; from 3: {1, 2, 4}. Union: {1, 2, 3, 4}. All.
- 3 steps: all (since 2 steps reaches all, and graph is connected with min degree ≥ 2).

So same situation: for i ≥ 2, Bill can reach any vertex. Adithya must stay at step 1 (since w_1 must not be in {1, 3}, so w_1 = 2, meaning stay). At step 2, Bill can reach any vertex including 2. Collision. So Adithya can't win.

So this non-bipartite graph with 5 edges on 4 vertices also doesn't work. Consistent with M(4) = 4.

Now let me think about larger n. The question is: can we have a non-bipartite graph on n vertices with more than ⌊n²/4⌋ edges where Adithya wins?

By Turán's theorem, the maximum number of edges in a bipartite graph on n vertices is ⌊n²/4⌋. Any graph with more edges is non-bipartite (contains an odd cycle).

So the question is: can Adithya win on any non-bipartite graph?

Let me think about this more carefully. Consider a non-bipartite graph G. It contains an odd cycle. Let's think about what this means for Bill.

In a non-bipartite graph, for any vertex v and sufficiently large k, v can reach any vertex in exactly k steps (for k large enough). This is because the odd cycle allows parity changes.

More precisely, in a connected non-bipartite graph, there exists some k_0 such that for all k ≥ k_0, every vertex is reachable from any starting vertex in exactly k steps. This k_0 is related to the diameter and the odd cycle length.

So if Adithya's walk is long enough (T ≥ k_0), Bill can reach any vertex at any step ≥ k_0, including B at step T. So Bill can guard B.

But what if Adithya's walk is short (T < k_0)? Then maybe Bill can't reach B in exactly T steps.

Hmm, but Adithya needs to reach B, and the distance from A to B is at least 2 (non-adjacent). If the graph has small diameter, Adithya can reach B quickly, but Bill can also reach anywhere quickly.

Let me think about this more carefully. The key question is: for a non-bipartite graph, can Adithya find a walk W from A to B of length T such that:
1. For all i ≤ T, w_i is not reachable from B in exactly i steps.
2. B is not reachable from B in exactly T steps.

Condition 2 is about closed walks of length T from B. In a non-bipartite graph, there exist closed walks of both parities (for large enough lengths). But for small T, maybe not.

Actually, let me think about when condition 2 fails. B is reachable from B in exactly T steps iff there's a closed walk of length T from B. In a non-bipartite graph, B is on or near an odd cycle. If B is on an odd cycle of length L, then there's a closed walk of length L from B. Also, closed walks of length L + 2, L + 4, etc. (go around the cycle, then back and forth on an edge). And closed walks of length 2 (go to neighbor and back). So closed walks of length 2, 4, 6, ... and L, L+2, L+4, ... If L is odd, then we get all lengths ≥ L (both parities) and all even lengths ≥ 2.

So if B is on an odd cycle of length L, closed walks from B exist for all even lengths ≥ 2 and all lengths ≥ L. If L = 3 (triangle), then closed walks exist for all lengths ≥ 2 (even: 2, 4, 6, ...; odd: 3, 5, 7, ...). So for T ≥ 2, B is reachable from B in T steps. Condition 2 fails for all T ≥ 2.

If B is not on an odd cycle but the graph has an odd cycle elsewhere, it's more complex. B might need to travel to the odd cycle and back, which takes more steps.

Hmm, let me think about a graph where the odd cycle is far from B.

Consider a graph that is a path A - ... - B with a triangle attached at the far end from B. Like: A - v1 - v2 - ... - vk - (triangle). And B is somewhere on the path, far from the triangle.

Actually, let me think about a specific construction. Take a path 1-2-3-...-n. Add an edge to create a triangle at one end. Say, add edge (1,3) to create triangle 1-2-3. Now the graph has n vertices and n edges (n-1 path edges + 1 extra). It's non-bipartite.

Let A and B be far from the triangle. Say A = n-1, B = n (or A = n, B = n-1, but they need to be non-adjacent; n-1 and n are adjacent on the path). Let me choose A and B on the path, non-adjacent.

Actually, let me think about this differently. Let me consider a graph that is bipartite except for one edge that creates an odd cycle, and choose A, B far from the odd cycle.

Path: 1-2-3-...-n. Add edge (n-2, n) to create triangle n-2, n-1, n. Now choose A = 1, B = 3 (non-adjacent since distance 2 on path... wait, 1 and 3 are not adjacent on the path, they're distance 2. But is edge (1,3) in the graph? No, only (n-2,n) was added. So 1 and 3 are non-adjacent. Good.

But wait, the triangle is at the other end. B = 3 is far from the triangle (at vertices n-2, n-1, n). The odd cycle is far from B.

In this graph, can Adithya win with A=1, B=3?

The graph is almost a path. The only non-path edge is (n-2, n). For vertices near 1, 2, 3, the graph looks like a path.

Adithya's strategy: stay at 1 (step 1), then walk 1→2→3 (steps 2, 3). Reach B at step 3.

Can Bill collide? Bill starts at 3. 
- Step 1: Bill moves from 3 to 2 or 4. Adithya at 1. No collision (Bill at 2 or 4, Adithya at 1).
- Step 2: Adithya at 2. Bill at 2 or 4, moves. If Bill at 2: must move to 1 or 3. If Bill goes to 1: A=2, B=1. If Bill goes to 3: A=2, B=3. If Bill at 4: must move to 3 or 5. A=2, B=3 or 5. No collision in any case (Adithya at 2, Bill at 1, 3, or 5).
  
  Wait, can Bill be at 2 at step 2? Bill starts at 3. In 2 steps: 3→2→1 or 3→2→3 or 3→4→3 or 3→4→5. So Bill can be at 1, 3, or 5 at step 2. Not 2. (Because to be at 2 at step 2, Bill needs 3→?→2. 3→2→? no, 3→2 is 1 step, then 2→? is another step, so Bill is at 1 or 3 at step 2, not 2.) Wait, I'm confusing myself.

  Bill at step 2: Bill takes 2 steps from 3. Possible positions: 3→2→1 (at 1), 3→2→3 (at 3), 3→4→3 (at 3), 3→4→5 (at 5). So Bill can be at 1, 3, or 5 at step 2. Adithya is at 2. No collision. ✓

- Step 3: Adithya at 3 = B. Bill at 1, 3, or 5 (from step 2), moves. 
  - If Bill at 1: moves to 2. A=3, B=2. Adithya at B alone. Win!
  - If Bill at 3: moves to 2 or 4. A=3, B=2 or 4. But wait, Adithya is at 3 and Bill was at 3 at step 2. That means collision at step 2! No, wait. At step 2, Adithya is at 2 and Bill is at 3. No collision. At step 3, Adithya moves to 3, Bill moves from 3 to 2 or 4. After the move, A=3, B=2 or 4. No collision. But is Bill at B=3? No, Bill is at 2 or 4. Adithya at 3 = B alone. Win!
  - If Bill at 5: moves to 4 or 6. A=3, B=4 or 6. Adithya at B alone. Win!

But wait, I need to also check: can Bill be at 3 at step 3? Bill at 3 at step 3 means a closed walk of length 3 from 3. 3→2→1→2? No, that's at 2. 3→4→3→? No, that's 2 steps to 3, then 1 more step. 3→2→3→2 (at 2), 3→2→3→4 (at 4), 3→4→3→2 (at 2), 3→4→3→4 (at 4), 3→4→5→4 (at 4), 3→4→5→6 (at 6), 3→2→1→2 (at 2). So Bill can be at 2, 4, or 6 at step 3. Not 3! 

Actually, can Bill be at 3 at step 3? 3→2→3→2 or 3→4→3→4 or 3→2→3→4 or 3→4→3→2. So from 3, 2 steps gets to 3 (via 3→2→3 or 3→4→3), then 1 more step gets to 2 or 4. So Bill can't be at 3 at step 3. Because to be at 3 at step 3, need a closed walk of length 3 from 3. The graph near 3 is a path (3-2-1 and 3-4-5-...), so closed walks from 3 have even length (since the local structure is bipartite). The odd cycle is far away (at n-2, n-1, n), so for small step counts, Bill can't use it.

So for step 3, Bill can't be at 3 (no closed walk of length 3 from 3, since the odd cycle is far away). Adithya wins!

But wait, I need to also check that Bill can't collide at step 3. Bill at step 3 can be at 2, 4, or 6 (as computed). Adithya at 3. No collision. ✓

So Adithya wins on this non-bipartite graph! The graph has n vertices and n edges (n-1 + 1). For n ≥ 6 (so that the triangle at one end is far from A=1, B=3), this works.

Wait, but does this give us more edges than ⌊n²/4⌋? For large n, n edges is much less than ⌊n²/4⌋. So this doesn't help beat the bipartite bound.

The question is: can we have a non-bipartite graph with MORE than ⌊n²/4⌋ edges where Adithya wins?

By Turán's theorem, any graph with more than ⌊n²/4⌋ edges is non-bipartite. So we need to check if any non-bipartite graph with > ⌊n²/4⌋ edges allows Adithya to win.

Hmm, but actually, the question is about the maximum m. If all non-bipartite graphs fail, then M(n) = ⌊n²/4⌋. If some non-bipartite graph with more edges works, M(n) > ⌊n²/4⌋.

Let me think about whether a non-bipartite graph with many edges can work.

The issue with non-bipartite graphs is the odd cycle. If the odd cycle is near B, Bill can use it to create closed walks of various lengths, guarding B. If the odd cycle is far from B, it might not help Bill for short walks.

But with many edges, the graph has small diameter, so the odd cycle is close to everything.

Let me think about the maximum edges in a graph where Adithya can win. 

Key insight: Adithya needs to find A, B non-adjacent such that he can win. The graph must be connected. 

Let me think about what structures allow Adithya to win.

Adithya's winning condition (for a fixed walk W of length T):
1. No vertex w_i is reachable from B in exactly i steps, for all 0 ≤ i ≤ T.
2. B is not reachable from B in exactly T steps.

For condition 1, at step 0, w_0 = A, and B is at distance ≥ 2 from A (non-adjacent), so A is not reachable from B in 0 steps (B ≠ A). ✓

For the walk to be short (to avoid Bill's reach expanding), Adithya wants A and B to be close. But they must be non-adjacent, so distance ≥ 2.

If distance from A to B is 2, Adithya can reach B in 2 steps (or 3 with a stay). Let me think about when this works.

With a stay: walk is A, A, v, B (length 3, where v is a common neighbor of A and B).

Condition 1:
- Step 0: A ≠ B. ✓ (A and B are distinct)
- Step 1: A not reachable from B in 1 step. This means A is not adjacent to B. ✓ (given)
- Step 2: v not reachable from B in 2 steps. 
- Step 3: B not reachable from B in 3 steps. (Condition 2)

For step 2: v is a neighbor of both A and B. Is v reachable from B in 2 steps? B → v is 1 step (v is adjacent to B). Then v → v? No, Bill must move. B → v → ? in 2 steps, Bill is at a neighbor of v, not v itself. Wait, I need v to not be reachable from B in exactly 2 steps. B → w → v where w is a neighbor of B and v is a neighbor of w. Since v is a neighbor of B, B → v is 1 step. But we need exactly 2 steps. B → v → v? No. B → (neighbor of B) → v. If there's a neighbor w of B such that v is a neighbor of w, then v is reachable in 2 steps. Since v is a neighbor of B, and B has other neighbors, if any neighbor w of B is also adjacent to v, then v is reachable in 2 steps.

In a dense graph, this is likely. In a sparse graph (like a path), it might not be.

On a path A-v-B (3 vertices), v is the only neighbor of B. B → v → A or B → v → B. So in 2 steps from B, Bill can be at A or B. Not v. So v is not reachable in 2 steps. ✓

But in a denser graph, v might be reachable in 2 steps from B.

For step 3 (condition 2): B not reachable from B in 3 steps. This means no closed walk of length 3 from B. In a bipartite graph, all closed walks have even length, so this is automatic. In a non-bipartite graph, if B is on a triangle, there's a closed walk of length 3. If B is not on a triangle but the graph has an odd cycle elsewhere, there might not be a closed walk of length 3 from B.

So the strategy of "stay, then walk distance 2" works when:
1. v (common neighbor of A, B) is not reachable from B in 2 steps.
2. No closed walk of length 3 from B.

Condition 2 is satisfied if B is not on any triangle and not on any odd cycle of length 3. More generally, if the graph is bipartite, or if B is far from all odd cycles.

Condition 1 is satisfied if v has no common neighbor with B (other than through paths of length 2 that don't go through v). Actually, v is reachable from B in 2 steps iff there's a path B → w → v of length 2. This exists iff v is in the 2-neighborhood of B. Since v is adjacent to B, v is in the 1-neighborhood. For 2-step reachability, we need a different path: B → w → v where w ≠ v. This exists iff B and v have a common neighbor w (w adjacent to both B and v, w ≠ B, w ≠ v).

So condition 1 fails iff B and v have a common neighbor (other than through the direct edge). In a path A-v-B, B and v have no common neighbor (B's only neighbor is v, v's neighbors are A and B, common neighbor would need to be adjacent to both B and v, but B's only neighbor is v). So condition 1 holds. ✓

In a denser graph, B and v likely have a common neighbor, so condition 1 fails.

So the "stay, walk 2" strategy works only in sparse graphs. For dense graphs, Adithya needs a different approach.

Let me reconsider. Maybe for dense non-bipartite graphs, Adithya can't win at all, and M(n) = ⌊n²/4⌋.

Let me try to prove that Adithya can't win on any non-bipartite graph with more than ⌊n²/4⌋ edges.

Hmm, actually, I realize the problem might be more subtle. Let me think about specific small cases.

Let me compute M(n) for n = 3 to 10 by figuring out the maximum edges.

For bipartite graphs, max edges = ⌊n²/4⌋. Let me compute:
- n=3: ⌊9/4⌋ = 2
- n=4: ⌊16/4⌋ = 4
- n=5: ⌊25/4⌋ = 6
- n=6: ⌊36/4⌋ = 9
- n=7: ⌊49/4⌋ = 12
- n=8: ⌊64/4⌋ = 16
- n=9: ⌊81/4⌋ = 20
- n=10: ⌊100/4⌋ = 24

Sum = 2 + 4 + 6 + 9 + 12 + 16 + 20 + 24 = 93.

But I need to check if we can do better with non-bipartite graphs.

Let me think about this more carefully. Is it true that Adithya can't win on any non-bipartite graph?

No, I showed earlier that a path with a far-away triangle (non-bipartite, n edges) allows Adithya to win. But n edges < ⌊n²/4⌋ for n ≥ 5. So it doesn't beat the bipartite bound.

The question is: can a non-bipartite graph with > ⌊n²/4⌋ edges allow Adithya to win?

Let me think about what happens with a graph that has ⌊n²/4⌋ + 1 edges. By Turán's theorem, this is non-bipartite. The graph is very dense (close to complete bipartite plus one edge).

Consider K_{a,b} plus one intra-part edge. Say K_{a,b} with parts X (size a) and Y (size b), plus edge (x1, x2) within X. This creates triangles: x1-x2-y for any y in Y. So every vertex in Y is on a triangle with x1, x2.

Now, can Adithya win? A and B must be non-adjacent. Non-adjacent pairs: within X (other than x1, x2), or within Y. 

Case 1: A, B both in Y. They're non-adjacent (Y is an independent set). B is in Y, and B is on a triangle (B-x1-x2-B, since x1, x2 are adjacent and both adjacent to B). So there's a closed walk of length 3 from B. 

Adithya needs to reach B. Distance from A to B: A is in Y, B is in Y. They're both adjacent to all of X. So distance is 2 (A → x → B for any x in X).

Adithya's walk: stay at A (step 1), then A → x → B (steps 2, 3). Length 3.

Condition 2: B reachable from B in 3 steps? Yes (B → x1 → x2 → B). So condition 2 fails. Bill can be at B at step 3.

What if Adithya uses a different length? Say stay, stay, A → x → B (length 4). Condition 2: B reachable from B in 4 steps? B → x → B → x → B (length 4). Yes. Fails.

Actually, in this graph, B is on a triangle, so closed walks of length 3 exist. Also, closed walks of length 2 exist (B → x → B). So closed walks of length 2, 3, 4, 5, ... all exist. Condition 2 fails for all T ≥ 2.

What about condition 1? At step 1, Adithya at A. A reachable from B in 1 step? A and B are both in Y, not adjacent. So no. ✓ At step 2, Adithya at x (some vertex in X). x reachable from B in 2 steps? B → x' → x where x' is any vertex in X. Since all X vertices are adjacent to B, and x is adjacent to x' iff x = x' or (x, x') is the added edge. If x' = x, then B → x → x? No, need x → x, but no self-loops. So B → x' → x requires x' adjacent to x. If x' ≠ x, then x' and x are both in X, and they're adjacent only if {x', x} = {x1, x2}. So if x is x1 or x2, then B → x2 → x1 (if x = x1) or B → x1 → x2 (if x = x2). So x1 and x2 are reachable from B in 2 steps. If x is not x1 or x2, then no other X vertex is adjacent to x, so x is not reachable from B in 2 steps (the only way would be B → x → x, impossible). 

Wait, I need to reconsider. B → x' → x: x' must be a neighbor of B (so x' ∈ X), and x must be a neighbor of x'. Neighbors of x' in X: only if x' is x1 or x2 (due to the added edge). So:
- If x' = x1: neighbors of x1 in X = {x2}. So x = x2. B → x1 → x2.
- If x' = x2: neighbors of x2 in X = {x1}. So x = x1. B → x2 → x1.
- If x' is another vertex in X: no neighbors in X. So can't reach any X vertex in 2 steps through x'.

So only x1 and x2 are reachable from B in 2 steps (within X). Other X vertices are not reachable from B in 2 steps.

So if Adithya chooses x ∉ {x1, x2} for his intermediate vertex, condition 1 holds at step 2. But condition 2 fails (B is on a triangle, closed walk of length 3 exists, and also length 4, etc.).

So Adithya can't win with A, B both in Y on this graph.

Case 2: A, B both in X, non-adjacent. So A, B ∈ X \ {x1, x2} (or one of them is x1 or x2 but they're not the pair (x1,x2)). Let's say A, B ∈ X, A ≠ B, and (A,B) is not an edge. So at least one of A, B is not in {x1, x2}.

B is in X. Is B on a triangle? If B = x1, then B is on triangles x1-x2-y. If B ∉ {x1, x2}, then B's neighbors are all of Y. Triangles through B: B-y-x'-B where x' is a neighbor of y in X. y is adjacent to all X, so x' can be any X vertex. B-y-x'-B requires x' adjacent to B. x' ∈ X, B ∈ X, so x' adjacent to B iff {x', B} = {x1, x2}. So if B ∉ {x1, x2}, then no x' in X is adjacent to B (except through the added edge, but B is not x1 or x2). So B is not on a triangle.

But is there a closed walk of odd length from B? B → y → x1 → x2 → y' → B (length 5). Yes! So closed walks of length 5 exist from B. Also length 3? B → y → x → B requires x adjacent to B. If B ∉ {x1, x2}, no x in X is adjacent to B. So no triangle through B. Length 3 closed walk: B → y → ? → B. ? must be adjacent to y and B. ? adjacent to y: any X vertex. ? adjacent to B: only Y vertices (since B ∈ X, B's neighbors are in Y) and possibly x1 or x2 if B is one of them. If B ∉ {x1, x2}, ? adjacent to B means ? ∈ Y. But ? adjacent to y means ? ∈ X. Contradiction (? can't be in both X and Y). So no closed walk of length 3 from B.

Length 5: B → y → x1 → x2 → y' → B. This works if y' is adjacent to B (yes, y' ∈ Y, B ∈ X, all Y-X edges exist). So closed walk of length 5 exists.

Length 2: B → y → B. Yes (y is adjacent to B, and B is adjacent to y). So closed walk of length 2 exists.
Length 4: B → y → B → y' → B. Yes.
Length 5: as above. Yes.
Length 6: B → y → B → y → B → y → B. Yes.
Length 7: B → y → x1 → x2 → y' → B → y'' → B. Hmm, that's 7 steps. B→y→x1→x2→y'→B→y''→B. Yes.

So from B, closed walks exist for lengths 2, 4, 5, 6, 7, 8, ... (all lengths ≥ 2 except 3). Length 3 doesn't exist.

So if Adithya arrives at B at step 3, condition 2 is satisfied (no closed walk of length 3 from B). But we need to check condition 1 as well.

Adithya's walk: A → ? → ? → B or stay → A → ? → B (length 3).

Let me try: stay at A (step 1), A → y → B (steps 2, 3), where y ∈ Y.

Condition 1:
- Step 0: A ≠ B. ✓
- Step 1: A not reachable from B in 1 step. A and B both in X, non-adjacent. ✓
- Step 2: y not reachable from B in 2 steps. B → ? → y. ? must be neighbor of B (so ? ∈ Y) and y must be neighbor of ? (so ? ∈ X, since y ∈ Y and y's neighbors are in X). But ? can't be in both X and Y. Contradiction. So y is not reachable from B in 2 steps. ✓ (Because Y is an independent set, you can't go Y → Y in 2 steps through X: B(X) → ?(Y) → y(Y) requires ? adjacent to y, but ? ∈ Y and y ∈ Y, and Y is independent. So no.)

Wait, let me reconsider. B ∈ X. B → ? → y. ? must be adjacent to B, so ? ∈ Y (since B's neighbors are in Y, unless B is x1 or x2 with the extra edge). If B ∉ {x1, x2}, then ? ∈ Y. Then ? → y requires ? adjacent to y. ? ∈ Y, y ∈ Y. Y is independent, so ? not adjacent to y. So y not reachable in 2 steps. ✓

- Step 3: B not reachable from B in 3 steps. We showed no closed walk of length 3 from B (when B ∉ {x1, x2}). ✓

So condition 1 and 2 are both satisfied! Adithya wins with the walk: stay, A → y → B.

But wait, I need to double-check. Bill can see Adithya and adapt. But since Adithya's walk is predetermined, and we've shown that no Bill walk can collide or guard B, Adithya wins regardless of Bill's strategy.

Let me verify more carefully. Bill starts at B. Adithya's walk: A, A, y, B (steps 0, 1, 2, 3).

Bill's possible positions:
- Step 0: B (given)
- Step 1: any neighbor of B. If B ∉ {x1, x2}, neighbors are all of Y. So Bill ∈ Y.
- Step 2: any vertex reachable from B in 2 steps. B → y' → ? where y' ∈ Y, ? ∈ X (since Y's neighbors are in X, plus possibly x1-x2 edge). So ? ∈ X. Bill ∈ X at step 2. Specifically, ? can be any X vertex (since y' is adjacent to all X). So Bill can be at any X vertex at step 2, including A! But Adithya is at y at step 2 (y ∈ Y). Bill is at some X vertex. No collision. ✓
- Step 3: any vertex reachable from B in 3 steps. B → y' → x → ? where y' ∈ Y, x ∈ X, ? ∈ Y (since x's neighbors are in Y, plus possibly x1-x2 edge). If x ∈ {x1, x2}, ? can be in X (via the extra edge) or Y. If x ∉ {x1, x2}, ? ∈ Y. So Bill can be at various Y vertices and possibly some X vertices (if going through x1-x2). Can Bill be at B at step 3? B ∈ X. Bill at X at step 3 requires going through the x1-x2 edge: B → y' → x1 → x2 (if B ≠ x2) or B → y' → x2 → x1 (if B ≠ x1). So Bill can be at x1 or x2 at step 3 (if B is not x1 or x2). But B is not x1 or x2 (we assumed B ∉ {x1, x2}). So Bill can be at x1 or x2 at step 3, but not at B. ✓ (Condition 2 verified.)

Can Bill be at y at step 3? y ∈ Y. Bill at Y at step 3: B → y' → x → y'' where y'' ∈ Y. This is possible (B → y' → x → y'' with y', y'' ∈ Y, x ∈ X). So Bill can be at any Y vertex at step 3, including y. But Adithya is at B at step 3 (B ∈ X). Bill at y ∈ Y. No collision. ✓

So Adithya wins! The walk stay → A → y → B works.

So on K_{a,b} + one edge (within part X), with A, B ∈ X \ {x1, x2} (non-adjacent), Adithya wins. This graph has ab + 1 edges.

For this to work, we need |X \ {x1, x2}| ≥ 2, i.e., a ≥ 4 (so that we can find A, B both in X, both not x1 or x2, and non-adjacent). Wait, actually A and B just need to be non-adjacent and in X. If a ≥ 3, we can pick A = x3, B = x4 (if a ≥ 4) or A = x3, B = x1 (if a = 3, but then B = x1 is on a triangle, which we don't want). 

Hmm, let me reconsider. We need B ∉ {x1, x2} for the no-triangle condition. And A ∉ {x1, x2} would be good too (though the key is B). And A, B non-adjacent (automatically true if both in X and not the pair (x1, x2)).

So we need at least 2 vertices in X other than x1, x2, i.e., a ≥ 4. Wait, we need A and B both in X \ {x1, x2}, and A ≠ B. So |X \ {x1, x2}| ≥ 2, i.e., a ≥ 4.

If a = 3: X = {x1, x2, x3}. We can pick A = x3, B = x3? No, A ≠ B. We can pick A = x1, B = x3 (non-adjacent since (x1, x3) is not an edge, only (x1, x2) is). But B = x3 ∉ {x1, x2}, so B is not on a triangle. And A = x1 is on a triangle, but that's OK (we only need B to not be on a triangle for condition 2). Let me check condition 1 for A = x1.

Actually, condition 1 at step 1: A not reachable from B in 1 step. A = x1, B = x3. Are they adjacent? x1 and x3 are both in X. The only intra-X edge is (x1, x2). So (x1, x3) is not an edge. ✓

So with a = 3, we can pick A = x1, B = x3. B ∉ {x1, x2}, so no triangle through B. The walk stay → x1 → y → x3 works.

But wait, does A = x1 being on a triangle cause any issues? Let me recheck condition 1 at step 2: y not reachable from B = x3 in 2 steps. B = x3 ∈ X. B → ? → y. ? must be adjacent to x3, so ? ∈ Y (x3's neighbors are all of Y, since x3 ∉ {x1, x2} so no intra-X edge). Then ? → y: ? ∈ Y, y ∈ Y, Y independent. Not adjacent. So y not reachable. ✓

And condition 2: no closed walk of length 3 from B = x3. As shown, x3 is not on any triangle. ✓

So a = 3 works. We need a ≥ 3 (so that X has at least 3 vertices, allowing us to pick B ∉ {x1, x2}).

What about a = 2? X = {x1, x2} with edge (x1, x2). Then any A, B in X would be x1, x2, but they're adjacent. So we can't pick A, B both in X. We'd need to pick A, B in Y. But then B ∈ Y, and B is on a triangle (B-x1-x2-B). Condition 2 fails. So a = 2 doesn't work for this strategy.

So for K_{a,b} + 1 edge with a ≥ 3, Adithya wins. Edges = ab + 1. We want to maximize ab + 1 subject to a + b = n and a ≥ 3.

ab is maximized when a and b are as equal as possible. With a ≥ 3:
- If n is even: a = n/2, b = n/2 (if n/2 ≥ 3, i.e., n ≥ 6). Edges = n²/4 + 1.
- If n is odd: a = (n-1)/2 or (n+1)/2, b = the other. Edges = (n²-1)/4 + 1.

But wait, we need a ≥ 3 AND we need to be able to choose which part gets the extra edge. We should put the extra edge in the larger part (or either part if equal).

Actually, let me reconsider. We have K_{a,b} with parts X (size a) and Y (size b). We add an edge within X. We need a ≥ 3 to find B ∈ X \ {x1, x2}. The total edges are ab + 1.

To maximize ab + 1 with a + b = n, a ≥ 3: maximize ab. ab is maximized when a ≈ b ≈ n/2. For a ≥ 3, this is fine as long as n ≥ 6 (so n/2 ≥ 3).

For n = 3, 4, 5: we need a ≥ 3, so a = 3, b = n - 3.
- n=3: a=3, b=0. Not connected (b=0). Invalid.
- n=4: a=3, b=1. Edges = 3 + 1 = 4. Same as ⌊16/4⌋ = 4. No improvement.
- n=5: a=3, b=2. Edges = 6 + 1 = 7. ⌊25/4⌋ = 6. So 7 > 6! Improvement!

Wait, let me check n=5 more carefully. K_{3,2} has 6 edges. Add one edge within the part of size 3. Total 7 edges. A, B in the size-3 part, with B not being one of the two endpoints of the added edge.

X = {x1, x2, x3}, Y = {y1, y2}. Added edge: (x1, x2). A = x1, B = x3 (or A = x3, B = x1, etc.). B = x3 ∉ {x1, x2}. 

Walk: stay at A = x1 (step 1), x1 → y1 (step 2), y1 → x3 = B (step 3).

Condition 1:
- Step 1: x1 not reachable from x3 in 1 step. x1 and x3 both in X. (x1, x3) not an edge (only (x1, x2) is). ✓
- Step 2: y1 not reachable from x3 in 2 steps. x3 → ? → y1. ? adjacent to x3: ? ∈ Y (x3 ∉ {x1,x2}, so x3's neighbors are all Y). ? ∈ Y, then ? → y1: ? ∈ Y, y1 ∈ Y, not adjacent. ✓
- Step 3: x3 not reachable from x3 in 3 steps. x3 is not on any triangle (x3's neighbors are Y, and Y is independent). ✓

Adithya wins! So M(5) ≥ 7.

Can we do even better for n=5? Maximum edges on 5 vertices is 10 (K5). Let's see what's the max m for n=5.

We have 7 from the above. Can we get 8?

K_{3,2} + 2 edges within X: X = {x1, x2, x3}, add edges (x1,x2) and (x1,x3). Now X has edges (x1,x2), (x1,x3). Total edges = 6 + 2 = 8.

Non-adjacent pairs: (x2, x3) in X, and all Y pairs (but Y has only 2 vertices, (y1, y2) is non-adjacent).

If A, B in X: must be non-adjacent, so A = x2, B = x3 (or vice versa). B = x3. Is x3 on a triangle? x3's neighbors: all Y (y1, y2) and x1 (via added edge (x1,x3)). Triangle: x3-x1-y-x3 for any y ∈ Y (since x1 is adjacent to all Y, and x3 is adjacent to all Y). So x3 is on a triangle. Closed walk of length 3 from x3: x3 → x1 → y1 → x3. Condition 2 fails for T=3.

What about T=4? Closed walk of length 4 from x3: x3 → y1 → x3 → y1 → x3. Yes. T=5? x3 → x1 → x2 → y1 → x3 (if x2 adjacent to y1, yes). Length 5. Yes. So closed walks exist for all T ≥ 2 (since x3 is on a triangle, closed walks of length 3 exist, and length 2 exists, so all lengths ≥ 2).

So condition 2 fails for all T ≥ 2. Adithya can't win with B = x3.

What about A, B in Y? A = y1, B = y2. B = y2. Is y2 on a triangle? y2's neighbors: all X (x1, x2, x3). Triangle: y2-x1-x2-y2 (x1-x2 is an edge, x1-y2 and x2-y2 are edges). Yes. So condition 2 fails.

What if A in X, B in Y? They're adjacent (all X-Y edges exist). Not allowed.

So with 8 edges (K_{3,2} + 2 intra-X edges), Adithya can't win. What about other graphs with 8 edges on 5 vertices?

Let me think about what 8-edge graphs on 5 vertices exist. K5 has 10 edges. K5 minus 2 edges has 8 edges. There are different cases depending on which 2 edges are removed.

Case 1: Remove two edges sharing a vertex. E.g., remove (1,2) and (1,3). Then vertex 1 has degree 2 (connected to 4, 5). Non-adjacent pairs: (1,2), (1,3), (2,3) if (2,3) is also missing... wait, (2,3) is not removed, so it's present. Non-adjacent: (1,2) and (1,3).

B = 2 or 3. Say B = 2. Is B on a triangle? 2 is adjacent to 3, 4, 5 (all except 1). Triangle: 2-3-4-2 (if 3-4 is an edge, which it is since we only removed (1,2) and (1,3)). Yes. So B is on a triangle. Condition 2 fails for T=3.

For T=4: closed walk of length 4 from 2: 2→3→2→3→2. Yes. T=5: 2→3→4→2→3→2. Hmm, that's 5 steps: 2→3→4→2→3→2? No, 2→3 is 1, 3→4 is 2, 4→2 is 3, 2→3 is 4, 3→2 is 5. But we need to be at 2 at step 5. 2→3→4→2→4→2: 5 steps, at 2. Yes. So closed walks of all lengths ≥ 2 exist. Condition 2 fails.

Case 2: Remove two non-adjacent edges. E.g., remove (1,2) and (3,4). Non-adjacent pairs: (1,2) and (3,4).

B = 1 (or 2, 3, 4). B = 1. Is 1 on a triangle? 1 is adjacent to 3, 4, 5 (not 2). Triangle: 1-3-5-1 (if 3-5 and 1-5 are edges, yes). So 1 is on a triangle. Condition 2 fails.

B = 3. 3 is adjacent to 1, 2, 5 (not 4). Triangle: 3-1-5-3 (1-5 and 3-5 are edges). Yes. Condition 2 fails.

So in all cases with 8 edges on 5 vertices, every vertex seems to be on a triangle, making condition 2 impossible.

Hmm, let me check: is there any 8-edge graph on 5 vertices where some vertex is not on a triangle?

A vertex v is not on a triangle iff its neighborhood is an independent set. Vertex v has degree d. Its neighbors form an independent set, so no edges among them. The remaining n-1-d vertices can have edges among them and to v's neighbors.

Total edges: edges from v to neighbors: d. Edges among v's neighbors: 0 (independent). Edges among non-neighbors and between non-neighbors and neighbors: at most C(n-1-d, 2) + d*(n-1-d).

Wait, let me think about it differently. For 5 vertices, if v is not on a triangle, v's neighbors are independent. Let d = deg(v). Then edges among v's neighbors = 0. Edges not involving v: among the other 4 vertices, with the constraint that v's d neighbors are independent. 

Max edges: d (from v) + edges among the other 4 vertices. The other 4 vertices include d neighbors of v (which must be independent) and 4-d non-neighbors. Edges among the other 4: at most C(4,2) = 6, minus the edges that must be absent (among v's d neighbors: C(d,2) edges must be absent). So max edges = d + 6 - C(d,2).

For d=2: 2 + 6 - 1 = 7.
For d=3: 3 + 6 - 3 = 6.
For d=4: 4 + 6 - 6 = 4.

So the maximum edges on 5 vertices with some vertex not on a triangle is 7 (achieved when d=2). This is exactly our K_{3,2} + 1 construction!

So for n=5, M(5) = 7.

Let me now think about the general pattern. It seems like M(n) might be ⌊n²/4⌋ + 1 for n ≥ 5 (where we can add one edge to K_{⌊n/2⌋, ⌈n/2⌉} and still win).

Wait, but I need to check if we can add more than one edge.

Let me think about K_{a,b} + k intra-X edges, where the k edges form some graph H on X. We need to find A, B in X (or Y) that are non-adjacent and such that B is not on a triangle.

B is not on a triangle iff B's neighborhood is independent. B ∈ X. B's neighbors: all of Y (since K_{a,b}) plus B's neighbors in H (the intra-X edges). For B's neighborhood to be independent, we need: no edges among Y (Y is independent, ✓), no edges among B's H-neighbors (they're in X, and edges within X are from H), and no edges between Y and B's H-neighbors (but all Y-X edges exist in K_{a,b}, so this fails if B has any H-neighbor!).

Wait, that's the key issue. B's neighbors include all of Y and B's H-neighbors in X. Y is connected to all X vertices. So if B has an H-neighbor x, then x is adjacent to all Y, and B is adjacent to all Y. So B-y-x-B is a triangle for any y ∈ Y. So B is on a triangle iff B has at least one H-neighbor.

So B is NOT on a triangle iff B is isolated in H (no intra-X edges incident to B).

Similarly, A is not on a triangle iff A is isolated in H (but we don't need A to be triangle-free; we need B to be triangle-free for condition 2).

Wait, actually I also need to check condition 1 more carefully. Let me re-examine.

For the walk stay → A → y → B (length 3), with A, B ∈ X, y ∈ Y:

Condition 1:
- Step 1: A not reachable from B in 1 step. A, B ∈ X. A adjacent to B iff (A,B) is an edge in H. So we need (A,B) ∉ H. ✓ (A, B non-adjacent)
- Step 2: y not reachable from B in 2 steps. B → ? → y. ? adjacent to B: ? ∈ Y (all Y) ∪ N_H(B) (H-neighbors of B in X). If B is isolated in H, ? ∈ Y. Then ? → y: ? ∈ Y, y ∈ Y, not adjacent (Y independent). ✓ If B has H-neighbors, ? could be in X. Then ? → y: ? ∈ X, y ∈ Y, adjacent (K_{a,b}). So y IS reachable in 2 steps. ✗

So condition 1 at step 2 requires B to be isolated in H. 

- Step 3: B not reachable from B in 3 steps. If B is isolated in H, B's neighbors are all Y. Closed walk of length 3: B → y → x → B. x must be adjacent to y (x ∈ X, y ∈ Y, ✓) and x adjacent to B (x ∈ X, (x,B) ∈ H or x = B). If B is isolated in H, no x ∈ X is adjacent to B via H. And x = B would mean B → y → B → B, but B → B is not allowed (no self-loop). So no closed walk of length 3. ✓

Great, so the walk stay → A → y → B works when:
1. A, B ∈ X, (A,B) ∉ H (non-adjacent)
2. B is isolated in H (no intra-X edges incident to B)

For this, we need at least one vertex in X that is isolated in H, and another vertex in X that is non-adjacent to it in H (which is automatic if the first is isolated).

So we need |X| ≥ 2 and at least one vertex in X is isolated in H. The number of intra-X edges is k = |E(H)|. The maximum k such that H has at least one isolated vertex: H is a graph on a vertices with at least one isolated vertex. The maximum edges in a graph on a vertices with at least one isolated vertex is C(a-1, 2) (complete graph on a-1 vertices, one isolated).

So k ≤ C(a-1, 2) = (a-1)(a-2)/2.

Total edges: ab + k ≤ ab + (a-1)(a-2)/2.

We want to maximize this over a + b = n, a ≥ 2 (need at least 2 in X for A, B), and b ≥ 1 (connected).

Wait, but we also need A, B non-adjacent. If B is isolated in H, then B is non-adjacent to all other X vertices in H. So any A ∈ X, A ≠ B works (as long as A ≠ B). We need |X| ≥ 2.

Also, I assumed the walk has length 3 (stay + 2 moves). But maybe longer walks could allow more edges? Let me think about this later. First, let me compute with the length-3 walk.

Total edges: f(a, b) = ab + (a-1)(a-2)/2, where a + b = n.

f(a) = a(n-a) + (a-1)(a-2)/2 = an - a² + (a² - 3a + 2)/2 = an - a² + a²/2 - 3a/2 + 1 = an - a²/2 - 3a/2 + 1.

f'(a) = n - a - 3/2. Setting to 0: a = n - 3/2. Since a must be integer, a ≈ n - 1 or n - 2.

Wait, that gives a very unbalanced partition. Let me compute for specific n.

For n = 5: a can be 2, 3, or 4 (b = 3, 2, or 1).
- a=2: f = 2*3 + 0 = 6. (H on 2 vertices with 1 isolated: max 0 edges.)
- a=3: f = 3*2 + 1 = 7. (H on 3 vertices with 1 isolated: max 1 edge, K2 on the other 2.)
- a=4: f = 4*1 + 3 = 7. (H on 4 vertices with 1 isolated: max 3 edges, K3 on the other 3.)

So max is 7 for n=5. Consistent with what we found.

For n = 6: a can be 2, 3, 4, 5.
- a=2: f = 2*4 + 0 = 8.
- a=3: f = 3*3 + 1 = 10.
- a=4: f = 4*2 + 3 = 11.
- a=5: f = 5*1 + 6 = 11.

So max is 11 for n=6. Compare with ⌊36/4⌋ = 9. So M(6) ≥ 11.

Hmm wait, but I should also consider putting the extra edges in Y instead of X. By symmetry, we could have H on Y with b vertices. The formula would be f(b) = ab + (b-1)(b-2)/2. By symmetry, this is the same as f(a) with a and b swapped. So the max over both is max(f(a), f(b)) = max(f(a), f(n-a)).

For n=6: f(4) = 11, f(2) = 8. So max is 11.

But wait, can we also add edges in BOTH X and Y? If we add edges in both parts, we need B to be isolated in H_X (the intra-X graph) and also... hmm, actually, if we add edges in Y as well, that affects things.

Let me reconsider. If we have intra-X edges (forming H_X) and intra-Y edges (forming H_Y), the total edges are ab + |E(H_X)| + |E(H_Y)|.

For the walk stay → A → y → B with A, B ∈ X, y ∈ Y:
- B must be isolated in H_X (for conditions 1 and 2 as before).
- But now Y has internal edges. Does this affect anything?

Condition 1, step 2: y not reachable from B in 2 steps. B → ? → y. ? adjacent to B: ? ∈ Y (all Y, since K_{a,b}) ∪ N_{H_X}(B) (empty, since B isolated in H_X). So ? ∈ Y. Then ? → y: ? ∈ Y, y ∈ Y. If H_Y has an edge (?, y), then yes, y is reachable. So we need y to have no H_Y-neighbors. I.e., y must be isolated in H_Y.

Condition 1, step 1: A not reachable from B in 1 step. A, B ∈ X, (A,B) ∉ H_X. ✓ (B isolated in H_X)

Condition 2, step 3: B not reachable from B in 3 steps. B → ? → ? → B. 
  ?₁ adjacent to B: ?₁ ∈ Y (B isolated in H_X). 
  ?₂ adjacent to ?₁: ?₂ ∈ X (K_{a,b}) ∪ N_{H_Y}(?₁) (Y-neighbors of ?₁).
  B adjacent to ?₂: ?₂ ∈ Y (K_{a,b}) ∪ N_{H_X}(B) (empty). So ?₂ ∈ Y. But ?₂ is adjacent to ?₁ and ?₂ ∈ Y. So ?₂ is an H_Y-neighbor of ?₁. And B adjacent to ?₂: ?₂ ∈ Y, B ∈ X, K_{a,b} edge. ✓. So B → ?₁ → ?₂ → B where ?₁, ?₂ ∈ Y and (?₁, ?₂) ∈ E(H_Y). This is a closed walk of length 3 iff H_Y has an edge.

  Also, ?₂ could be in X: ?₂ ∈ X, adjacent to ?₁ ∈ Y (K_{a,b} ✓). B adjacent to ?₂: ?₂ ∈ X, (B, ?₂) ∈ H_X. But B is isolated in H_X. So no. 

  So closed walk of length 3 from B exists iff H_Y has at least one edge. If H_Y has no edges, no closed walk of length 3. ✓

So if H_Y is empty (no intra-Y edges), condition 2 is satisfied. But then we can't add any intra-Y edges, which defeats the purpose.

Hmm, so adding intra-Y edges breaks condition 2
